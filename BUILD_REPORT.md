# BUILD REPORT — Candidate A (Hard Gate Broadsheet, WINNER) — news-image-20261127

- Built: Fri 27 Nov 2026 ~07:10–07:55 WIB, session started after competition
  open (2026-11-27T00:00:00Z). Account @seannbeez. Builder session id:
  e87d774a-e5f5-4de3-bf4c-bee39f51561d.
- No GitHub repo created, no `makefun` bundle/check/submit/record run.

## Deliverables

| File | Detail |
|---|---|
| `entry.png` | 1024×1024 PNG, **186,086 bytes** (limit 1,048,576), sha256 `d91a3b7d687ef16b5169308c2f68b4d4a13fc904b5435f5e33bb613b5e7451d4` |
| `entry-300px.png` | 300×300 LANCZOS downscale (in cand-a/), sha256 `9e8fc2181059b91880f0a65ce5e6e9465e677c8434a2f231adb471d4bd016a43` |
| `build.py` | Deterministic Pillow renderer, written fresh in this session |
| `gate.py` | Determinism + size + dimensions gate |
| `main.py` | Stdlib-only entrypoint: copies vendored `entry.png` to `/output/entry.png` |
| `README.md` | Live make.fun badge SVG only (never shields.io) |
| `LICENSE` | MIT |
| `BUILD_REPORT.md` | This file |

## Gate result

- `python3 gate.py` → **GATE PASS**. Build exit 0, zero audit problems
  (all tracked text boxes inside the canvas), two runs byte-identical
  (sha256 `d91a3b7d…`), 1024×1024, 186,086 B ≤ 1 MiB.
- Entrypoint verified sandbox-style: `MAKEFUN_OUTPUT_DIR=out python3 main.py`
  run twice; both outputs byte-identical to repo `entry.png`.

## 300px verdict — PASS (visually inspected + Gemini judge)

- Date "FRIDAY 27 NOVEMBER 2026" is the largest readable element.
- All 6 numbers in the navy strip readable: 800,000+ · 77,000 · 7,000 ·
  4.3% · 2 · 2.
- All 3 heroes identifiable (drone + radar, storm + balloon, rocket);
  timeline, map and ALSO structure read clearly at 300px.
- Two mini bodies overflowed their cards in the first render (minis 7
  and 15, third line clipped) — caught on visual inspection, shortened,
  gate re-passed.

## Layout (broadsheet)

Micro-bar → giant serif masthead date + red italic sub-dek → 6-number
navy strip → 7-tick UTC timeline → 3 hero cards in one row (inked
flat-vector art) → 12 numbered minis (4 cols × 3 rows, status shown by
the colour of the number cell) → world pin map (left) + ALSO list
(right, 3 cols) → DATE CHECK box → legend + sources + disputed-claims
footer.

## Story / region counts

- **32 stories, 8 regions**: 3 heroes + 12 minis + 17 ALSO.
  - Heroes: 1 Drone strike kills two Italians in Kuwait (CLAIM — Italy
    and Kuwait blame Iran; Tehran denies), 2 Thanksgiving storm cuts
    power to 800,000+, 100th Macy's parade postponed first time
    (CONFIRMED), 3 Musk: two SpaceX shares per US child, ~$18bn
    (CONFIRMED).
  - Minis 4–15: Gaza 9 killed incl. Hamas deputy minister (CONFIRMED),
    UK net migration 77,000 (CONFIRMED), Chess Game 3 60-move draw
    1.5–1.5 (CONFIRMED), Ibiza tanker Med Emre sinks, 1 dead
    (CONFIRMED), Trump demands GDP probe, Q3 revised 4.3%
    (CONFIRMED), Black Friday sales +4.2% to >$1tn (CONFIRMED),
    Depardieu to stand trial (CONFIRMED), Zelensky to BBC (CONFIRMED),
    Duterte ICC trial starts Monday (CONFIRMED), NZ final results
    today (CONFIRMED), Bangkok refinery blast 9 injured (REPORTED —
    toll disputed 9 vs 7), India top court quashes release (CONFIRMED).
  - ALSO 16–32: Europe stocks rally, Bank of Korea +25bp, Kenya KWS
    convictions, Kenya schools census, France far right, Kim nuclear
    vow, Spain snap elections, Myanmar ICJ refusal, HIV jab Africa, UK
    train knifeman, Michigan State 70–67, India–NZ Test, China drones,
    India GST auto-cancellation, UK reservists, FIFA cyberattack,
    Brazil budget cuts.
  - Regions: North America, Europe, Middle East, Africa, East Asia,
    South Asia, Oceania, Latin America.
- World pin map: 15 numbered pins (heroes + minis); Europe/Middle East
  cluster fanned with label offsets (still dense — known weakness).
- Timeline: 7 ticks 17:17–01:00 UTC; only sourced times labelled
  (Kuwait deaths 17:17, chess draw 18:56, KWS verdict 20:58, Ibiza
  22:01, Kuwait update 22:33, Europe roundup 00:02, edition closed
  01:00).
- DATE CHECK: Huawei 10/12 (25 Nov), CIA/ODNI hack (25 Nov), Cairo
  tanker fire 31 dead (26 Nov), Houthi refinery claim (25 Nov), F1
  Qatar feud (25 Nov), Colombia 76-hostage siege (25 Nov); NOT YET:
  NZ final results, Chess Game 4 (Sat), Duterte plea (Mon), Macy's
  parade (Sat).

## Numbers strip (safe figures only)

800,000+ without power (USA Today + People + PowerOutage.us; Times
later 900,000) · 77,000 UK net migration (ONS via Times/Reuters/NYT) ·
7,000 t diesel aboard Med Emre (Reuters + BBC) · 4.3% US Q3 GDP
(BEA via Reuters) · 2 SpaceX shares per child (Reuters + Times +
Hindu) · 2 Italians killed in Kuwait (Reuters + CNN + BBC + WSJ).

## Duel result — WHY A WON (Gemini judge, gemini-3.6-flash, pool key 1)

- 300px, order 1 (A vs B): **A 92 – B 78**. Order 2 (B vs A): **A 94 – B 78**.
  Mean 300px: **A 93 – B 78**. Full frame (A vs B): **A 95 – B 80**.
  Same image wins in all three calls — no label bias.
- Judge's reasons (all three calls agree): A's balanced three-column
  hero grid gives a stronger focal point and reading flow; B's
  asymmetric layout compresses hero 3 into an irregular box beneath
  the map; A's map plots numbered story pins (functional) vs B's
  generic region bubbles; A's 4×3 mini grid has comfortable
  typography vs B's narrow 6-column rows.
- Local criteria check agrees on C1 (both name the day), C2 (identical
  32-story set), C4 (identical facts); A wins C3 (reads) and C5 (craft /
  300px) on grid balance, hero size and mini typography. All local
  scores are LOCAL ESTIMATES, never official scores.
- No live Top-1 existed at duel time (board: submissionCount 5,
  entries [] — no entries ranked yet), so no champion duel was possible.

## Known weaknesses / uncertainties

- Hero 1 art (drone + radar) reads weakly — the radar dish is small;
  the drone dominates. Hero 2 balloon reads as a red disc at 300px.
- World map pin cluster over Europe / Middle East is dense; individual
  pin numbers are hard to read even at full frame.
- Edition closed 01:00 UTC 27 Nov (08:00 WIB) — the day's later news
  (NZ final results, US Friday session) is NOT in this edition.
- Several ALSO items are REPORTED on a single live roundup source each
  (see RESEARCH.md); they are badged REPORTED, not CONFIRMED.
- Chronology note: stories are those first reported in Fri 27 Nov
  editions (Asia-Pacific morning press / overnight UTC 26–27 Nov);
  event dates are recorded per story in RESEARCH.md. Items that led
  the 26-Nov edition are excluded via DATE CHECK.

## Fonts used

- Liberation Serif Bold (masthead), Liberation Serif Italic (sub-dek),
  Liberation Sans Bold/Regular (all other text). Local system fonts only.

## Content provenance

Every story, number and date comes from
`~/workspace/makefun/news-image-20261127/RESEARCH.md` only (edition
closed 01:00 UTC 27 Nov 2026). No story or number invented. Flat vector
art only (Pillow-drawn shapes); no photos, no AI/painterly images.
