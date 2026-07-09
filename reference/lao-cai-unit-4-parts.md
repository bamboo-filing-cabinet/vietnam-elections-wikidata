# Lào Cai electoral unit No. 4 (Q140469765) — constituent parts

Verified reconciliation of the 25 constituents of **Đơn vị bầu cử số 4, tỉnh Lào Cai**
for the 16th National Assembly (2026), per **Resolution 85/NQ-HĐBCQG**.

Source: https://web.archive.org/web/20260311093639/https://xaydungchinhsach.chinhphu.vn/nghi-quyet-85-nq-hdbcqg-ve-so-don-vi-bau-cu-danh-sach-cac-don-vi-bau-cu-so-luong-dai-bieu-quoc-hoi-duoc-bau-o-moi-don-vi-bau-cu-119260104122958567.htm
Reconciled: 2026-07-09.

Unit No. 4 = 1 phường + 24 xã, 2 seats. Each is a **post-2025-merger** commune/ward
item (P31 = commune/ward/commune-level town of Vietnam), **not** the pre-merger
rural-district item.

| # | Constituent | QID | Notes |
|---|-------------|-----|-------|
| 1 | Sa Pa (phường) | Q1000140 | ward; NOT old town Q7395483 |
| 2 | Bản Hồ | Q10743168 | |
| 3 | Mường Bo | Q10824869 | |
| 4 | Ngũ Chỉ Sơn | Q10743169 | |
| 5 | Tả Phìn | Q10831526 | in Sa Pa; NOT the Hà Giang/Lai Châu Tả Phìn |
| 6 | Tả Van | Q32589143 | |
| 7 | Bảo Thắng | Q10807147 | commune; NOT old district Q4857427 |
| 8 | Gia Phú | Q10761368 | |
| 9 | Phong Hải | Q10805443 | in Bảo Thắng; NOT Quảng Yên Q10805442 |
| 10 | Tằng Loỏng | Q10831604 | |
| 11 | Xuân Quang | Q10835054 | |
| 12 | Phúc Khánh | Q10786858 | |
| 13 | Thượng Hà | Q10826066 | |
| 14 | Bảo Hà | Q10743241 | |
| 15 | Bảo Yên | Q10807154 | commune; NOT old district Q4857432 |
| 16 | Nghĩa Đô | Q10798879 | |
| 17 | Xuân Hòa | Q10834922 | |
| 18 | Chiềng Ken | Q10747244 | |
| 19 | Dương Quỳ | Q10757598 | in Văn Bàn |
| 20 | Khánh Yên | Q10779681 | |
| 21 | Minh Lương | Q10793915 | |
| 22 | Nậm Chày | Q32291418 | |
| 23 | Nậm Xé | Q10802190 | |
| 24 | Văn Bàn | Q10779678 | commune-level town; NOT old district Q7913140 |
| 25 | Võ Lao | Q10833253 | |

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
- **Q140469739 (unit 2, pre-2025 merger)** is multi-term, so its P527 parts are correctly
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
