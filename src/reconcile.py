"""Phase 1: match delegates against existing Wikidata items.

Strategy (name-first, DOB-confirmed — Vietnamese names collide heavily, so a
name match alone is never treated as confident):

1. Pull the pool of existing "member of the National Assembly of Vietnam"
   holders (P39 = Q10841192) with their folded names + DOB in one SPARQL query.
2. For each winner, look for a pool entry whose folded name matches. If exactly
   one also matches on DOB -> matched. Name-only or multiple -> needs review.
3. For winners with no pool hit, search Wikidata by name and confirm via DOB.

Writes reconciliation/<cycle>.csv with:
  person_id, name, dob, wikidata_qid, match_status, match_notes
where match_status is one of: matched | ambiguous | unmatched.
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

import loader
import wikidata as wd

OUT_DIR = Path(__file__).resolve().parents[1] / "reconciliation"


def _fetch_pool() -> dict[str, list[dict]]:
    """folded name -> list of {qid, dob} for every current NA member on Wikidata."""
    query = f"""
    SELECT ?person ?dob ?name WHERE {{
      ?person wdt:P39 wd:{wd.POSITION_MEMBER_NA} .
      OPTIONAL {{ ?person wdt:P569 ?dob. }}
      {{ ?person rdfs:label ?name. FILTER(LANG(?name) IN ("vi","en")) }}
      UNION
      {{ ?person skos:altLabel ?name. FILTER(LANG(?name) IN ("vi","en")) }}
    }}
    """
    by_name: dict[str, dict[str, str | None]] = defaultdict(dict)
    for b in wd.sparql(query):
        qid = b["person"]["value"].rsplit("/", 1)[-1]
        folded = wd.fold(b["name"]["value"])
        dob = b.get("dob", {}).get("value")
        dob_iso = dob[:10] if dob else None
        if folded:
            # keep a dob if any binding for this qid has one
            by_name[folded][qid] = by_name[folded].get(qid) or dob_iso
    return {name: [{"qid": q, "dob": d} for q, d in qids.items()] for name, qids in by_name.items()}


def _match_via_search(winner: dict) -> tuple[str, str, str]:
    """Return (qid, status, notes) by searching Wikidata for an unmatched winner."""
    candidate_qids: list[str] = []
    for term, lang in ((winner["name_vi"], "vi"), (winner["name_folded"], "en")):
        if term:
            candidate_qids.extend(wd.search_entities(term, language=lang, limit=10))
    candidate_qids = list(dict.fromkeys(candidate_qids))  # dedupe, keep order
    if not candidate_qids:
        return "", "unmatched", "no name candidates on Wikidata"

    entities = wd.get_entities(candidate_qids)
    winner_folded = winner["name_folded"] or wd.fold(winner["name_vi"] or "")
    dob = winner["dob_iso"]

    name_hits: list[str] = []
    dob_hits: list[str] = []
    for qid in candidate_qids:
        ent = entities.get(qid)
        if not ent or not wd.entity_is_human(ent):
            continue
        if winner_folded and winner_folded in wd.entity_names(ent):
            name_hits.append(qid)
            if dob and wd.entity_dob(ent) == dob:
                dob_hits.append(qid)

    if len(dob_hits) == 1:
        return dob_hits[0], "matched", "name + DOB match via search"
    if len(dob_hits) > 1:
        return "", "ambiguous", f"multiple name+DOB matches: {', '.join(dob_hits)}"
    if name_hits:
        return "", "ambiguous", f"name match, DOB unconfirmed: {', '.join(name_hits)}"
    return "", "unmatched", f"candidates found but no name match ({len(candidate_qids)} searched)"


FIELDNAMES = ["person_id", "name", "dob", "wikidata_qid", "match_status", "match_notes"]


def _classify(w: dict, pool: dict[str, list[dict]]) -> dict:
    folded = w["name_folded"] or wd.fold(w["name_vi"] or "")
    dob = w["dob_iso"]
    qid, status, notes = "", "unmatched", ""

    pool_hits = pool.get(folded, [])
    if pool_hits:
        dob_matches = [h["qid"] for h in pool_hits if dob and h["dob"] == dob]
        if len(dob_matches) == 1:
            qid, status, notes = dob_matches[0], "matched", "name + DOB match in NA-member pool"
        elif len(dob_matches) > 1:
            status, notes = "ambiguous", f"multiple pool name+DOB matches: {', '.join(dob_matches)}"
        else:
            qids = ", ".join(h["qid"] for h in pool_hits)
            status, notes = "ambiguous", f"pool name match, DOB unconfirmed: {qids}"
    else:
        qid, status, notes = _match_via_search(w)

    return {
        "person_id": w["person_id"],
        "name": w["name_vi"],
        "dob": w["dob_iso"] or w["dob_raw"] or "",
        "wikidata_qid": qid,
        "match_status": status,
        "match_notes": notes,
    }


def _load_done(out_path: Path) -> set[str]:
    """person_ids already written, so a re-run resumes instead of redoing work."""
    if not out_path.exists():
        return set()
    with open(out_path, newline="", encoding="utf-8") as f:
        return {row["person_id"] for row in csv.DictReader(f)}


def main() -> None:
    cycle = sys.argv[1] if len(sys.argv) > 1 else "na15-2021"
    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / f"{cycle}.csv"

    winners = loader.load_winners(cycle)
    done = _load_done(out_path)
    todo = [w for w in winners if w["person_id"] not in done]
    print(f"{len(winners)} winners; {len(done)} already done; {len(todo)} to process", file=sys.stderr)
    if not todo:
        print("Nothing to do.", file=sys.stderr)
        return

    print("Fetching existing NA-member pool from Wikidata...", file=sys.stderr)
    pool = _fetch_pool()
    print(f"Pool: {sum(len(v) for v in pool.values())} name->qid entries", file=sys.stderr)

    # Append incrementally, flushing each row so an interrupt never loses progress.
    with open(out_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not done:
            writer.writeheader()
        for i, w in enumerate(todo, 1):
            writer.writerow(_classify(w, pool))
            f.flush()
            if i % 25 == 0:
                print(f"  processed {i}/{len(todo)}", file=sys.stderr)

    # Final summary over the whole file.
    with open(out_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["match_status"]] = counts.get(r["match_status"], 0) + 1
    print(f"\n{out_path} now has {len(rows)} rows", file=sys.stderr)
    print(f"Summary: {counts}", file=sys.stderr)


if __name__ == "__main__":
    main()
