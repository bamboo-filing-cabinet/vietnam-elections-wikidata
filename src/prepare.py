"""Phase 2: generate QuickStatements for unmatched persons.

Emits labels (vi + folded en) and statements: P31 -> Q5, P569 dob,
P21 gender, P27 -> Q881, P172 ethnicity (mapped to QIDs), P39 ->
Q17144338 qualified with P2937 term, P768 electoral district,
P580/P582 term dates, and P1343 source. Writes
statements/<cycle>-create.qs (QuickStatements v2).
"""


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
