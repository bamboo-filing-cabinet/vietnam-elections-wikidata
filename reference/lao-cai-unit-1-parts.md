# Lào Cai electoral unit No. 1 — constituent parts + old↔new crosswalk

Wikidata item: **Q140478357** (created 2026-07-09).

Constituents of **Đơn vị bầu cử số 1, tỉnh Lào Cai** (merged province, post-2025
reform) for the 16th National Assembly (2026) — the **former Yên Bái core**, the
unit Sùng A Lềnh (Q116946987) actually ran in (issue #6).

Sources:
- Resolution 85/NQ-HĐBCQG (unit → territory): `vietnam-elections/data/na16-2026/congressional-units.md`
- Resolution 151/NQ-HĐBCQG (candidate list, confirms the unit): `vietnam-elections/data/na16-2026/candidates-list/`
- Reconciled 2026-07-09; 3 seats, 5 candidates.

## Old → new administrative relationship (2025 reform)

These constituent items are the **pre-reform commune/ward items** — Wikidata
reused them, mostly only updating the description to "…tỉnh Lào Cai". The reform
changed their **hierarchy**, which is the real old-vs-new difference:

- **Before:** commune/ward → **district (huyện)** → **Yên Bái province** (`Q36349`)
- **2025 reform:** the **huyện tier was abolished**; Yên Bái **merged into** Lào Cai (`Q36446`)
- **After:** commune/ward → **Lào Cai province** (`Q36446`) **directly** (no district tier)

Old districts, all abolished in 2025: **huyện Yên Bình** `Q8052180`, **huyện Lục
Yên** `Q6695817`, **huyện Trấn Yên** `Q7833347`, and **TP Yên Bái** `Q26019` (the
city the 4 wards came from).

⚠️ **Wikidata is mid-migration:** most items' `P131` still points at the old
huyện/province (only Nam Cường is re-parented to `Q36446`), and several `P31`
types still say "commune" even where Resolution 85 lists a *phường*. The reform
isn't fully reflected on Wikidata yet — the "WD P131 now" column flags it.

## Crosswalk table

`QID` = the current item (used for the unit's P527). `old parent (huyện)` = the
pre-reform district it sat under; **new parent for every row = Lào Cai `Q36446`**.

| # | Constituent | Res 85 type | QID | old parent (huyện / city) | old parent QID | WD P131 now |
|---|-------------|-------------|-----|---------------------------|----------------|-------------|
| 1 | Âu Lâu | phường | Q10838761 | TP Yên Bái | Q26019 | Q36349 (stale) |
| 2 | Nam Cường | phường | Q10797037 | TP Yên Bái | Q26019 | Q36446 ✓ |
| 3 | Văn Phú | phường | Q10833414 | TP Yên Bái | Q26019 | Q36349 (stale) |
| 4 | Yên Bái | phường | Q135228953 | TP Yên Bái | Q26019 | none (new item) |
| 5 | Bảo Ái | xã | Q10743295 | huyện Yên Bình | Q8052180 | Q8052180 (stale) |
| 6 | Thác Bà | xã | Q10825632 | huyện Yên Bình | Q8052180 | Q8052180 (stale) |
| 7 | Yên Bình | xã | Q10837974 | huyện Yên Bình | Q8052180 | Q8052180 (stale) |
| 8 | Cảm Nhân | xã | Q10752253 | huyện Yên Bình | Q8052180 | Q8052180 (stale) |
| 9 | Yên Thành | xã | Q10838151 | huyện Yên Bình | Q8052180 | Q8052180 (stale) |
| 10 | Khánh Hòa | xã | Q10779585 | huyện Lục Yên | Q6695817 | Q6695817 (stale) |
| 11 | Lâm Thượng | xã | Q10787498 | huyện Lục Yên | Q6695817 | Q6695817 (stale) |
| 12 | Lục Yên | xã | Q140480524 | huyện Lục Yên | Q6695817 | Q36446 ✓ (new item, issue #7; P1889 "different from" ≠ Q6695817) |
| 13 | Mường Lai | xã | Q10796388 | huyện Lục Yên | Q6695817 | Q6695817 (stale) |
| 14 | Phúc Lợi | xã | Q10806228 | huyện Lục Yên | Q6695817 | Q6695817 (stale) |
| 15 | Tân Lĩnh | xã | Q10830607 | huyện Lục Yên | Q6695817 | Q6695817 (stale) |
| 16 | Hưng Khánh | xã | Q10771342 | huyện Trấn Yên (inferred) | Q7833347 | none |
| 17 | Lương Thịnh | xã | Q10788398 | huyện Trấn Yên | Q7833347 | Q7833347 (stale) |
| 18 | Quy Mông | xã | Q10810129 | huyện Trấn Yên | Q7833347 | Q7833347 (stale) |
| 19 | Trấn Yên | xã | Q10752656 | huyện Trấn Yên | Q7833347 | Q7833347 (stale) |
| 20 | Việt Hồng | xã | Q10832840 | huyện Trấn Yên | Q7833347 | Q7833347 (stale) |

Notes:
- WD `P31` currently reads "commune"/"commune-level town" for most rows (incl. the
  phường 1–4) — pre-reform types, not yet updated to the Res 85 phường/xã.
- Row 16 Hưng Khánh: `P131` is unset on Wikidata; huyện Trấn Yên is inferred from
  the pre-reform geography, not verified from WD — treat as tentative.
- 20/20 now have a post-reform commune/ward item. **Lục Yên** `Q140480524` was
  created (issue #7) to fill the last gap — previously the only "Lục Yên" on WD
  was the old huyện `Q6695817`. The two are kept distinct: the new xã carries
  `P1889` (different from) → `Q6695817`, and the old huyện is now marked dissolved
  (`P576` = 2025, `different from` → `Q140480524`). Unit P527 is complete at 20/20.

P527 usage: add each `QID` as `has part(s)` on Q140478357; the P2937 (16th NA)
qualifier is optional for this single-term current item.

## If this format works, graduate to a JSON crosswalk

The columns above map onto the proposed `mappings/admin-units-crosswalk.json`
(province-merge level + commune level, backed by P7888/P1365/P1366/P571/P576/P131).
This table is the lightweight prototype of that per-commune level.
