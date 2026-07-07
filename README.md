# Kaiju Quest: City Defender

A family quest dashboard for tracking missions, city restoration, kaiju threats, and rewards — built in the same static style as Hero's Journey.

**Current:** Runnable quest dashboard with missions, progression, rewards, and monster image slots (local storage only). Firebase sync comes later.

## Stack

- Static `index.html` (embedded CSS + JavaScript)
- `localStorage` persistence (`kq_rpg_state`, `kq_rpg_settings`)
- Firebase stub (inactive — plan for a **new** Kaiju Quest Firebase project)
- No Node, npm, or build step required

## Run locally

**Option A — open directly**

Double-click `index.html` or open it in your browser:

```
file:///C:/Users/Rorian/OneDrive/Jason%20Things/Programming/Godzilla%20App/index.html
```

**Option B — simple local server (recommended for PWA manifest testing)**

```powershell
cd "C:\Users\Rorian\OneDrive\Jason Things\Programming\Godzilla App"
python -m http.server 8080
```

Then visit: http://localhost:8080/index.html

## Project layout

```
├── index.html              # Main app
├── manifest.webmanifest    # PWA manifest (icons TBD)
├── assets/
│   ├── hero/               # Player kaiju images
│   ├── enemies/            # Boss / rival kaiju images
│   ├── city/               # City skyline / battle backgrounds
│   ├── badges/             # Badge icon images
│   └── ui/                 # Small UI icons (shields, markers)
├── backups/                # Local progress snapshots (gitignored)
├── scripts/
│   ├── check-syntax.py     # Verify inline JS parses
│   └── smoke-test.py       # Headless load test (requires Playwright)
└── .cursor/rules/          # Backup-before-change workflow
```

## Dev checks

```powershell
python scripts/check-syntax.py
python scripts/smoke-test.py   # pip install playwright && playwright install chromium
```

## Firebase (later)

Do **not** reuse Hero's Journey Firebase keys, `localStorage` keys, collections, or documents. Create a new Firebase project for Kaiju Quest when ready.


## Monster images (Phase 7)

The app reads image paths from the `IMAGE_MAP` object in `index.html`. Drop PNG files into the folders below using these default filenames (or change the paths in `IMAGE_MAP`):

| Purpose | Folder | Default file |
|---------|--------|--------------|
| Player kaiju | `assets/hero/` | `godzilla-main.png` |
| Current boss | `assets/enemies/` | `storm-colossus.png` |
| City / battle background | `assets/city/` | `city-skyline.png` |
| Badge icons | `assets/badges/` | `first-defender.png`, `daily-defender.png`, `storm-breaker.png`, `city-builder.png`, `rising-titan.png` |
| UI icons | `assets/ui/` | `shield-icon.png` (district markers) |

**Missing images:** The app still runs without image files. Each image slot shows a dashed placeholder box with a text label until the file loads. Broken or missing files never crash the UI.

**Tips:** Use transparent PNGs for kaiju art. Keep hero/boss images roughly square. City images work well as wide banners.

## Copyright note

This is a private family app. Add your own images for personal use. Do not redistribute copyrighted character art.
