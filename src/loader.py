"""Load vietnam-elections data from the sibling checkout or published exports.

Prefers ../vietnam-elections/public/data/elections/<cycle>/ when running
inside the monorepo; falls back to the GitHub Pages exports.
"""

import glob
import json
from pathlib import Path

SIBLING_ROOT = Path(__file__).resolve().parents[2] / "vietnam-elections" / "public" / "data" / "elections"
HTTP_ROOT = "https://bamboo-filing-cabinet.github.io/vietnam-elections/data/elections"


def _cycle_dir(cycle: str) -> Path | None:
    d = SIBLING_ROOT / cycle
    return d if d.is_dir() else None


def _load_json_file(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_results(cycle: str = "na15-2021") -> dict:
    """Return the parsed results.json for a cycle (sibling checkout only)."""
    d = _cycle_dir(cycle)
    if d is None:
        raise FileNotFoundError(
            f"No sibling checkout at {SIBLING_ROOT / cycle}. "
            "HTTP fallback for results.json is not yet implemented."
        )
    return _load_json_file(d / "results.json")


def _person_details(cycle: str) -> dict[str, dict]:
    """Map person_id -> person detail block, scanning candidates_detail/."""
    d = _cycle_dir(cycle)
    if d is None:
        raise FileNotFoundError(f"No sibling checkout at {SIBLING_ROOT / cycle}.")
    out: dict[str, dict] = {}
    for f in glob.glob(str(d / "candidates_detail" / "*.json")):
        rec = _load_json_file(Path(f))
        person = rec.get("person") or {}
        pid = person.get("id")
        if pid and pid not in out:
            out[pid] = person
    return out


def _dob_to_iso(dob: str) -> str | None:
    """Convert a 'D/M/YYYY' birth date to ISO 'YYYY-MM-DD'; None if unparseable."""
    if not dob:
        return None
    parts = dob.strip().split("/")
    if len(parts) != 3:
        return None
    day, month, year = parts
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return None
    if len(year) != 4:
        return None
    return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"


def load_winners(cycle: str = "na15-2021") -> list[dict]:
    """Return one record per winning person (statuses containing 'won').

    Each record joins the result row with the candidate detail block so it
    carries dob_iso, gender, and ethnicity for reconciliation.
    """
    results = load_results(cycle)
    details = _person_details(cycle)
    winners: list[dict] = []
    seen: set[str] = set()
    for r in results["records"]:
        if "won" not in (r.get("statuses") or []):
            continue
        pid = r["person_id"]
        if pid in seen:
            continue
        seen.add(pid)
        person = details.get(pid, {})
        winners.append(
            {
                "person_id": pid,
                "name_vi": person.get("full_name") or r.get("candidate_name_vi"),
                "name_folded": person.get("full_name_folded") or r.get("candidate_name_folded"),
                "dob_raw": person.get("dob"),
                "dob_iso": _dob_to_iso(person.get("dob", "")),
                "gender": person.get("gender"),
                "ethnicity": person.get("ethnicity"),
                "locality_vi": r.get("unit_description_vi"),
            }
        )
    return winners


if __name__ == "__main__":
    w = load_winners()
    print(f"{len(w)} winners; sample:")
    for row in w[:3]:
        print(row)
