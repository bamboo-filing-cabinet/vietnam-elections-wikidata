# Lào Cai electoral unit No. 4 (Q140469765) — constituent parts

Verified reconciliation of the 25 constituents of **Đơn vị bầu cử số 4, tỉnh Lào Cai**
for the 16th National Assembly (2026), per **Resolution 85/NQ-HĐBCQG**.

Source: https://web.archive.org/web/20260311093639/https://xaydungchinhsach.chinhphu.vn/nghi-quyet-85-nq-hdbcqg-ve-so-don-vi-bau-cu-danh-sach-cac-don-vi-bau-cu-so-luong-dai-bieu-quoc-hoi-duoc-bau-o-moi-don-vi-bau-cu-119260104122958567.htm
Reconciled: 2026-07-09.

Unit No. 4 = 1 phường + 24 xã, 2 seats. Each QID is a **post-2025-reform**
commune/ward item, **not** the pre-reform rural-district item.

## Old → new administrative relationship (2025 reform)

Unit 4 is entirely on the **former Lào Cai side**, so — unlike unit 1 (Yên Bái
side) — the **province did not change**: it was Lào Cai (`Q36446`) before and
after. The only structural change is the **abolition of the district (huyện)
tier**:

- **Before:** commune → **district** (TX Sa Pa / huyện Bảo Thắng / Bảo Yên / Văn Bàn) → **Lào Cai** (`Q36446`)
- **After:** commune → **Lào Cai** (`Q36446`) directly

Old districts (all abolished 2025): **TX Sa Pa** (`Q1000140`, now a phường; the
pre-reform thị xã was also modelled as `Q7395483` — two Sa Pa items exist),
**huyện Bảo Thắng** `Q4857427`, **huyện Bảo Yên** `Q4857432`, **huyện Văn Bàn**
`Q7913140`. These four are exactly the P527 parts of the XV item Q140469739 —
confirming the unit-2 (XV) → unit-4 (XVI) territorial succession.

## Crosswalk table

`QID` = current item (unit's P527). old parent from WD `P131`; **new parent for
every row = Lào Cai `Q36446`**. Most parts carry both old-district and new-province
P131 (partially re-parented); a few (Tả Van, Nậm Chày) only show `Q36446`.

| # | Constituent | type | QID | old parent (district) | old parent QID |
|---|-------------|------|-----|-----------------------|----------------|
| 1 | Sa Pa | phường | Q1000140 | (is the old TX Sa Pa) | Q1000140 · cf. Q7395483 |
| 2 | Bản Hồ | xã | Q10743168 | TX Sa Pa | Q1000140 |
| 3 | Mường Bo | xã | Q10824869 | TX Sa Pa | Q1000140 |
| 4 | Ngũ Chỉ Sơn | xã | Q10743169 | TX Sa Pa | Q1000140 |
| 5 | Tả Phìn | xã | Q10831526 | TX Sa Pa | Q1000140 |
| 6 | Tả Van | xã | Q32589143 | TX Sa Pa (P131→Q36446 only) | Q1000140 (inferred) |
| 7 | Bảo Thắng | xã | Q10807147 | huyện Bảo Thắng | Q4857427 |
| 8 | Gia Phú | xã | Q10761368 | huyện Bảo Thắng | Q4857427 |
| 9 | Phong Hải | xã | Q10805443 | huyện Bảo Thắng | Q4857427 |
| 10 | Tằng Loỏng | xã | Q10831604 | huyện Bảo Thắng | Q4857427 |
| 11 | Xuân Quang | xã | Q10835054 | huyện Bảo Thắng | Q4857427 |
| 12 | Phúc Khánh | xã | Q10786858 | huyện Bảo Yên | Q4857432 |
| 13 | Thượng Hà | xã | Q10826066 | huyện Bảo Yên | Q4857432 |
| 14 | Bảo Hà | xã | Q10743241 | huyện Bảo Yên | Q4857432 |
| 15 | Bảo Yên | xã | Q10807154 | huyện Bảo Yên | Q4857432 |
| 16 | Nghĩa Đô | xã | Q10798879 | huyện Bảo Yên | Q4857432 |
| 17 | Xuân Hòa | xã | Q10834922 | huyện Bảo Yên | Q4857432 |
| 18 | Chiềng Ken | xã | Q10747244 | huyện Văn Bàn | Q7913140 |
| 19 | Dương Quỳ | xã | Q10757598 | huyện Văn Bàn | Q7913140 |
| 20 | Khánh Yên | xã | Q10779681 | huyện Văn Bàn | Q7913140 |
| 21 | Minh Lương | xã | Q10793915 | huyện Văn Bàn | Q7913140 |
| 22 | Nậm Chày | xã | Q32291418 | huyện Văn Bàn (P131→Q36446 only) | Q7913140 (inferred) |
| 23 | Nậm Xé | xã | Q10802190 | huyện Văn Bàn | Q7913140 |
| 24 | Văn Bàn | xã | Q10779678 | huyện Văn Bàn | Q7913140 |
| 25 | Võ Lao | xã | Q10833253 | huyện Văn Bàn | Q7913140 |

Reconciliation notes: Sa Pa Q1000140 is the ward (the pre-reform thị xã is
Q7395483); Tả Phìn Q10831526 is the Sa Pa one (NOT the Hà Giang/Lai Châu Tả
Phìn); Phong Hải Q10805443 is in Bảo Thắng (NOT Quảng Yên Q10805442).

## Legislative-term (P2937) qualifier rule

Where the term qualifier may live on an electoral-unit item:

| Property | P2937 as qualifier | Notes |
|----------|--------------------|-------|
| P1342 (number of seats) | ✅ yes | in P1342's allowed-qualifiers list |
| P527 (has part) | ✅ yes | valid/meaningful — composition can vary by term; used for multi-term (persistent) units |
| P131 (located in) | ❌ no | a location is not scoped to a parliamentary term; drop it |

- **Q140469765 (unit 4)** is a single-term (16th NA) item, so its 25 parts carry
  **no** per-part P2937 — that is correct, not a gap. The term qualifier sits on
  P1342 = 2.
- **Q140469739 (unit 2, pre-2025 reform)** is multi-term, so its P527 parts are correctly
  qualified with P2937. Its **P131 = Q36446 still carries an invalid P2937
  qualifier that should be removed** (manual Wikidata edit).

## Correction history

The item was first loaded with 31 has-part(s) that actually belong to **Đơn vị số 2**
(Nghĩa Lộ / Mù Cang Chải / Trạm Tấu / Văn Chấn / Văn Yên area). Those 31 must be
removed and replaced with the 25 above. Wrong QIDs (do not use for unit 4):

Q10752402, Q10828398, Q7022345, Q10829214, Q10829215, Q10805758, Q10830262,
Q30923256, Q10748730, Q16481064, Q10802128, Q10784405, Q10796265, Q10809845,
Q10831293, Q10748247, Q10840701, Q20025131, Q10805428, Q10805429, Q10796533,
Q10830553, Q10835172, Q10796604, Q10751825, Q10748703, Q10823337, Q10761337,
Q10823389, Q10798862, Q10826051.
