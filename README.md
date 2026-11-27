# Friday 27 November 2026 — the world in one image

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/seannbeez/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/seannbeez/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A classic financial broadsheet that sums up Friday 27 November 2026 in a
single 1024×1024 image: **32 stories across 8 regions** — 3 illustrated
heroes, 12 numbered minis, and 17 more in the ALSO list.

- **Heroes:** drone strike kills two Italians in Kuwait (Iran denies);
  Thanksgiving storm cuts power to 800,000+ and postpones the 100th
  Macy's parade for the first time; Musk pledges two SpaceX shares for
  every US child.
- **The day in numbers:** 800,000+ without power · 77,000 UK net
  migration · 7,000 tonnes of diesel aboard the Med Emre · 4.3% US Q3
  GDP growth · 2 SpaceX shares per child · 2 Italians killed in Kuwait.
- **Also inside:** a 7-tick UTC timeline (sourced times only), a world
  pin map, a DATE CHECK box listing the 25–26 Nov stories deliberately
  left out, and a legend explaining the CONFIRMED / CLAIM / REPORTED
  badges. Every story was first reported in 27 Nov 2026 editions;
  edition closed 01:00 UTC.

## How the program works

`build.py` is a deterministic Pillow renderer written for this entry
(standard library + Pillow at build time; the shipped program needs
only the standard library). It draws flat vector art only — no photos,
no network, no clock, no randomness — and writes `entry.png`
(1024×1024, ≤1 MiB) plus a 300×300 LANCZOS downscale.

`main.py` is the entrypoint: it copies the vendored `entry.png` into
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), so two runs write
byte-identical bytes. `gate.py` rebuilds twice, checks determinism,
size, dimensions, and the 300px downscale.

## Verify

```sh
python3 gate.py            # GATE PASS: two runs byte-identical
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see `LICENSE`.
