"""Phase 1: match delegates against existing Wikidata items.

Matches by name + DOB via the Wikidata API / SPARQL, handling Vietnamese
diacritics, folded forms, and name order. Writes
reconciliation/<cycle>.csv with person_id, name, dob, wikidata_qid,
match_status (matched | unmatched | ambiguous), match_notes.
"""


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
