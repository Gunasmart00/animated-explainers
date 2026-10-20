# Brand guide — Lowkey Genius + HowZit

Approved 2026-10-11. Logo **A5 Orbit bulb**, palette **G2 Alien Force** (green / black / lime, nano honeycomb texture).
These are the only brand values. Every video, thumbnail, cover and profile uses them.

| Account | Platform | Content |
|---|---|---|
| **Lowkey Genius** | YouTube (one channel) | Clips (primary) + animated "how things work" explainers |
| **HowZit** | Instagram | Explainer Reels |

## Colours

| Token | Hex | RGB | Use |
|---|---|---|---|
| `ground` | `#08110B` | 8, 17, 11 | Backgrounds, thumbnails, covers, text on lime |
| `surface` | `#13261A` | 19, 38, 26 | Cards, panels, lower thirds |
| `ink` | `#E6F4E8` | 230, 244, 232 | Main text, orbit ring, bulb base |
| `lime` | `#6CFF2E` | 108, 255, 46 | Main accent: bulb, hook box, highlighted caption word, progress bar |
| `forest` | `#1E7B3C` | 30, 123, 60 | Second accent: circuit lines, diagrams, secondary shapes |
| `white` | `#FFFFFF` | 255, 255, 255 | Caption text, the eye |
| `black` | `#000000` | 0, 0, 0 | Caption outline only |

Rules
- Lime is for **one** thing per frame (the hook, or the highlighted word, or the key object). Never body text on dark backgrounds longer than a few words.
- Text on lime is always `ground` (`#08110B`), never white.
- `forest` is decoration only; never use it for text (too dark on `ground`).
- Honeycomb texture: lime hexagons at 10–14% opacity on `ground`. Circuit lines: `forest`, ending in a lime dot.

## Typography
- Font: **Bricolage Grotesque** (Google Fonts, free). Weights: 300 Light, 500 Medium, 800 ExtraBold.
- Wordmark: `lowkey` in 300 + `genius` in 800, no space, lowercase.
- HowZit: `How` in ink + `Zit` in lime, 800, capital Z always.
- Captions: 800, white, 6 px black outline, highlighted word in lime.
- Fallback when the font isn't available (e.g. phone editors): Montserrat ExtraBold, then any heavy sans.

## Logo files (`brand/`)
| File | Size | Use |
|---|---|---|
| `logo/mark-on-dark.png/.svg` | 1000×1000, transparent | The bulb on dark backgrounds |
| `logo/mark-on-light.png/.svg` | 1000×1000, transparent | The bulb on light backgrounds |
| `logo/lockup-on-dark.png/.svg` | 1600×400, transparent | Bulb + wordmark (end screens, intros) |
| `youtube/profile-800.png` | 800×800 | YouTube profile picture |
| `youtube/banner-2560x1440.png` | 2560×1440 | YouTube banner (content inside the 1235×338 centre safe area) |
| `youtube/watermark-150.png` | 150×150, transparent | YouTube Studio branding watermark + in-video watermark |
| `howzit/profile-1080.png` | 1080×1080 | HowZit Instagram profile picture |
| `instagram/lowkeygenius-profile-1080.png` | 1080×1080 | Lowkey Genius clips Instagram profile picture |
| `howzit/wordmark-on-dark.png` | 1200×320, transparent | HowZit logo for Reel covers/intros |
| `video/shorts-safe-zone-guide.png` | 1080×1920 | Editing guide layer only — **never export it into a video** |

Regenerate PNGs after editing an SVG: `python tools/render_brand.py`.

Logo don'ts: don't recolour the bulb, stretch it, add shadows/glows, remove the orbit, or put it on busy footage without the dark circle (use `watermark-150.png`).

## Video layout (Shorts / Reels, 1080×1920)
Open `video/shorts-safe-zone-guide.png` as a top layer while editing, then hide it before export.
- **Hook box** (first 3 s): lime box, `ground` text, top area (y 260–460), left of the watermark.
- **Watermark**: `watermark-150.png` at ~110 px, top-right (about x 834, y 236), 85–100% opacity, whole video.
- **Captions**: 2–4 words at a time, centred, inside y 1080–1380.
- **Keep clear**: top 220 px, bottom 420 px, right 120 px (app buttons, title, channel name). These are third-party estimates; check on a real phone.
- **Progress bar** (optional): 8 px lime bar at the very bottom.

## Video layout (long videos, 1920×1080)
- Watermark: Studio → Customization → Branding → Video watermark → `watermark-150.png`, display **Entire video**.
- Lower thirds: `surface` panel, `ink` text, lime 6 px accent line.
- Thumbnails 1280×720: `ground` background + honeycomb, 2–4 words in 800 weight (one word lime), bulb bottom-right.
- End screen: `lockup-on-dark.png` centred for the last 20 s.

## Explainer animation style
- Background `ground` with honeycomb; objects drawn flat, lime for the "star" object, `forest` for supporting parts, `ink` for labels.
- Line weight consistent (4–6 px at 1080p). Rounded joins. No gradients except a soft lime glow behind the key object.
- Every explainer ends with the HowZit bubble (Instagram) or the bulb lockup (YouTube).

## Colour sources
Inspired by Ben 10 series palettes; only the Omnitrix green `#91FF16` came from a (fan) source, others are estimates. Colours are not trademarks, but **never** use Ben 10 names, the Omnitrix hourglass symbol or characters.
