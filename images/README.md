# Image intake folder

Drop new kaiju art here, then run:

```powershell
python scripts/import-images.py
```

The script optimizes and copies files into `assets/` for the app.

## Recognized filenames

| Drop this file in `images/` | Becomes |
|-----------------------------|---------|
| `Burning Godzilla.png` | `assets/hero/godzilla-atomic.png` |
| `Godzilla.png` | `assets/hero/godzilla-main.png` |
| `King Ghidorah.jpg` or `.png` | `assets/enemies/king-ghidorah.png` |
| `mechagodzilla.png` | `assets/enemies/mechagodzilla.png` |
| `rodan.png` | `assets/enemies/rodan.png` |
| `mothra.png` | `assets/enemies/mothra.png` |
| `gigan.png` | `assets/enemies/gigan.png` |
| `destoroyah.png` | `assets/enemies/destoroyah.png` |
| `anguirus.png` | `assets/enemies/anguirus.png` |
| `biollante.png` | `assets/enemies/biollante.png` |
| `spacegodzilla.png` | `assets/enemies/spacegodzilla.png` |
| `king caesar.png` | `assets/enemies/king-caesar.png` |
| `hedorah.png` | `assets/enemies/hedorah.png` |
| `megaguirus.png` | `assets/enemies/megaguirus.png` |
| `city-battle-bg.png` | `assets/city/city-battle-bg.png` |
| `city-skyline.png` | `assets/city/city-skyline.png` |
| `kaiju-roster-reference.png` | `assets/roster/kaiju-roster-reference.png` |

Names are case-insensitive. Keep your original files here; the app reads from `assets/` only.

After importing, refresh the app in the browser (hard refresh on phone if needed).
