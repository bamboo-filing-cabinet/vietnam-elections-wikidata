# vietnam-elections-wikidata

Reconcile and create Wikidata items for Vietnamese National Assembly delegates,
starting with the 15th National Assembly (2021), using the structured data in
[`vietnam-elections`](https://github.com/bamboo-filing-cabinet/vietnam-elections).

Plan and background: [bamboo-filing-cabinet/vietnam-elections#33](https://github.com/bamboo-filing-cabinet/vietnam-elections/issues/33).

## Phases

1. **Reconciliation** (`src/reconcile.py`) — match ~500 elected NA15 delegates
   against existing Wikidata items by name + DOB. Outputs
   `reconciliation/na15-2021.csv` (`person_id`, `name`, `dob`, `wikidata_qid`,
   `match_status`, `match_notes`).
2. **Prepare statements** (`src/prepare.py`) — generate QuickStatements v2 for
   unmatched persons (P31 human, P569 DOB, P21 gender, P27 Vietnam, P172
   ethnicity, P39 member of the National Assembly with term/district/date
   qualifiers). Outputs `statements/na15-2021-create.qs`.
3. **Upload** (`src/upload.py`) — batch create via QuickStatements or the
   Wikidata API. Logs to `uploads/na15-2021-log.csv`.
4. **Backfill QIDs** — merge reconciliation + upload results into
   `mappings/` (`person_id` → `wikidata_qid`) and contribute back to
   `vietnam-elections`.

## Data access

`src/loader.py` reads election data from the sibling checkout
(`../vietnam-elections/public/data/elections/na15-2021/`) when running inside
the [monorepo](https://github.com/bamboo-filing-cabinet/monorepo), and falls
back to the published exports at
`https://bamboo-filing-cabinet.github.io/vietnam-elections/data/elections/na15-2021/`.

## Development

Python project managed with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run python -m src.reconcile
```
