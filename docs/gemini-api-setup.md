# Gemini API setup for image generation (tools/gen_image.py)

Generates our stills (cast sheets, K0 start frames) with Nano Banana from `episodes/<name>/images.yaml`, so the owner
runs one command instead of copy-pasting prompts. API images carry only Google's invisible SynthID mark, no visible
sparkle (unlike Flow's image tool).

## Cost (checked 2026-10-24, ai.google.dev pricing)
- The Gemini API has **no free tier for images**. Nano Banana 2.1 (`gemini-nano-banana-2.1`): about **$0.034 (1K)**,
  **$0.05 (2K)**, $0.11 (4K) per image. A typical episode (cast sheet + start frames, ~20 tries) costs about $1.
- A **Google AI Pro plan does not cover API calls** ("billed and managed separately"). Pro does raise limits inside the
  AI Studio website. Pro subscribers with Cloud Billing on may get monthly Google Developer Program cloud credits that
  apply to the API.

## Get a key (one time)
1. Open https://aistudio.google.com and sign in with your Google account.
2. Left menu → **Get API key** → **Create API key** → pick or create a project (e.g. "howzit").
3. Billing: on the API keys page, click **Set up billing** next to the project, add a payment method in Google Cloud
   Billing and link it to the project. Optional: Cloud Billing → Budgets & alerts → a $10/month budget with email alerts.
4. Copy the key. **Never paste it into a chat, a prompt, a script or a commit.**

## Put the key in the repo (one time)
1. In `G:\Apps\animated-explainers`, create a file named `.env` (no other name) containing one line:
   `GEMINI_API_KEY=your-key-here`
2. `.env` is in `.gitignore`. Check: `git status` must not list `.env`.
3. Install the library: `.venv\Scripts\python.exe -m pip install -r requirements.txt`

## Use
```
.venv\Scripts\python.exe tools\gen_image.py episodes\<name> --list
.venv\Scripts\python.exe tools\gen_image.py episodes\<name> cast            (3 versions, about $0.15)
.venv\Scripts\python.exe tools\gen_image.py episodes\<name> K0 -n 4
.venv\Scripts\python.exe tools\gen_image.py episodes\<name> K0 --dry-run    (shows the request, costs nothing)
```
Results: `episodes/<name>/images/<job>_v1.png ...`, never overwritten; the log with cost estimates is
`images/gen_log.csv`. Tell Claude which version you like; it becomes `images/<job>.png` and later jobs use it as a
reference.
