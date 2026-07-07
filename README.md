# Kaiju Quest: City Defender

A family quest dashboard for tracking missions, city restoration, kaiju threats, and rewards — built in the same static style as Hero's Journey.

**Current:** Runnable Godzilla quest dashboard with missions, progression, rewards, and real kaiju image slots (local storage only). Firebase sync comes later.

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
│   ├── hero/               # Godzilla player images
│   ├── enemies/            # Enemy kaiju images
│   ├── city/               # City skyline / battle backgrounds
│   ├── badges/             # Badge / trophy images
│   ├── ui/                 # Small UI icons
│   └── roster/             # Kaiju roster reference image
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


## Kaiju images (manual assets)

This is a **private family app**. You provide real Godzilla/kaiju PNG files manually. Paths are configured in `PLAYER_CONFIG`, `ENEMY_KAIJU_DEFS`, and `IMAGE_MAP` inside `index.html`.

### Folders

| Folder | Purpose |
|--------|---------|
| `assets/hero/` | Godzilla (player) images |
| `assets/enemies/` | Enemy kaiju battle images |
| `assets/city/` | City skyline and battle backgrounds |
| `assets/badges/` | Badge/trophy icons |
| `assets/ui/` | Small UI icons (district markers) |
| `assets/roster/` | Reference roster image for your son |

### Hero (Godzilla)

| File | Use |
|------|-----|
| `assets/hero/godzilla-main.png` | Default Godzilla |
| `assets/hero/godzilla-atomic.png` | Powered-up Godzilla (shows after enough kaiju energy) |

### Enemy kaiju

Place one PNG per kaiju. The app starts with **King Ghidorah** as the active rival; others are configured for later.

| File |
|------|
| `assets/enemies/king-ghidorah.png` |
| `assets/enemies/mechagodzilla.png` |
| `assets/enemies/rodan.png` |
| `assets/enemies/mothra.png` |
| `assets/enemies/gigan.png` |
| `assets/enemies/destoroyah.png` |
| `assets/enemies/anguirus.png` |
| `assets/enemies/biollante.png` |
| `assets/enemies/spacegodzilla.png` |
| `assets/enemies/king-caesar.png` |
| `assets/enemies/hedorah.png` |
| `assets/enemies/megaguirus.png` |

### City / backgrounds

| File | Use |
|------|-----|
| `assets/city/city-battle-bg.png` | Dashboard battle scene background |
| `assets/city/city-skyline.png` | City tab banner |

### Badges

| File |
|------|
| `assets/badges/first-defender.png` |
| `assets/badges/daily-defender.png` |
| `assets/badges/storm-breaker.png` |
| `assets/badges/city-builder.png` |
| `assets/badges/rising-titan.png` |
| `assets/badges/kaiju-champion.png` |

### Roster reference

| File | Use |
|------|-----|
| `assets/roster/kaiju-roster-reference.png` | Optional kaiju roster reference (Kaiju tab) |

### Missing images

The app **does not** use fake emoji monsters. If a file is missing, each slot shows:

`Add image: assets/.../filename.png`

Drop in the PNG and refresh — the image appears automatically. The app keeps working without images.

## Copyright note

This is a private family app. Add your own images for personal use. Do not redistribute copyrighted character art.
