"""Build docs/checklist/howzit-reel-checklist.html from template.html + the prompts in prompts/gemini.md.

Usage (from the repo folder):  python tools/make_checklist.py
Run it after editing prompts/gemini.md so the checklist's copy buttons stay identical to the prompts.
Step ids are stable, so saved ticks survive a rebuild.
"""
import html
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from studio.prompts import gemini_blocks  # noqa: E402

B = gemini_blocks()
STYLE = B["STYLE"][0].strip()


def prompt(key, i=0):
    return B[key][i].replace("[PASTE 3D STYLE BLOCK]", STYLE)


def code(text, label="", cmd=False, short=False):
    cls = "code short" if short or cmd else "code"
    if cmd:
        inner = f'<pre data-cmd="{html.escape(text, quote=True)}">{html.escape(text.replace("{EP}", "<episode>"))}</pre>'
    else:
        inner = f"<pre>{html.escape(text)}</pre>"
    lab = f'<span class="label">{html.escape(label)}</span>' if label else ""
    return f'<div class="{cls}">{inner}<button class="copy" type="button">Copy</button>{lab}</div>'


CHIP = {"gemini": ("gem", "Gemini"), "ps": ("ps", "PowerShell"), "ig": ("ig", "Instagram"),
        "notepad": ("np", "Notepad"), "phone": ("np", "Phone"), "claude": ("np", "Claude")}


def step(sid, title, chips, body):
    ch = "".join(f'<span class="chip {CHIP[c][0]}">{CHIP[c][1]}</span>' for c in chips)
    return (f'<div class="step" data-id="{sid}"><input type="checkbox" id="c-{sid}" aria-label="{html.escape(title)}">'
            f'<span class="box" aria-hidden="true"></span><div class="body"><h3>{html.escape(title)} {ch}</h3>{body}</div></div>')


def phase(n, title, intro, steps):
    return (f'<section class="phase" aria-labelledby="p{n}"><div class="phase-head"><span class="n">{n:02d}</span>'
            f'<h2 id="p{n}">{html.escape(title)}</h2><span class="pc"></span></div>'
            + (f"<p class=\"lede\">{intro}</p>" if intro else "") + "".join(steps) + "</section>")


P = []
P.append(phase(1, "Once: set up the laptop", "Do this the first time only. Untick nothing here when you start a new video.", [
    step("a1", "Check the project folder", ["ps"],
         "<p>The project lives in <code>G:\\Apps\\animated-explainers</code>. If it isn't there, unzip <code>animated-explainers.zip</code> into <code>G:\\Apps</code>.</p>"
         + code("cd G:\\Apps\\animated-explainers\ndir", cmd=True)),
    step("a2", "Install ffmpeg", ["ps"],
         "<p>Close and reopen PowerShell afterwards, then check it prints a version.</p>"
         + code("winget install Gyan.FFmpeg", cmd=True) + code("ffmpeg -version", cmd=True)),
    step("a3", "Create the Python environment", ["ps"],
         "<p><b>Easiest:</b> double-click <code>setup.bat</code> in the project folder. It installs ffmpeg and the Python packages, "
         "makes the voice samples (step 7) and a test render (step 4). Or run the commands yourself:</p>"
         +
         code("cd G:\\Apps\\animated-explainers\npython -m venv .venv\n.venv\\Scripts\\Activate.ps1\npython -m pip install -r requirements.txt", cmd=True)
         + "<p class=\"save\">If PowerShell blocks <code>Activate.ps1</code>, run <code>Set-ExecutionPolicy -Scope CurrentUser RemoteSigned</code> once and answer Y.</p>"),
    step("a4", "Test render the sample", ["ps"],
         "<p>Makes a half-size draft with the real voice. Open the mp4 it prints and check you hear the narrator.</p>"
         + code("python -m studio.build episodes\\microwave-heating --draft", cmd=True)),
    step("a5", "Confirm the Lowkey Genius Instagram handle", ["notepad"],
         "<p>Open <code>brand\\brand.yaml</code> and set <code>collab: instagram:</code> to the exact Lowkey Genius page handle. It's used in every posting note.</p>"
         + code("notepad brand\\brand.yaml", cmd=True)),
    step("a7", "Pick your narrator voice", ["ps"],
         "<p>Writes the same two lines in 8 free voices. Play them and choose the one closest to the reference Reel "
         "(young, quick, friendly). Put its name, rate and pitch under <code>voice:</code> in <code>presets\\explainer.yaml</code>. "
         "For an even more natural read, use Google AI Studio per video (phase 3).</p>"
         + code("python -m studio.voices", cmd=True) + code("start voice-tests", cmd=True)
         + code("notepad presets\\explainer.yaml", cmd=True)),
    step("a8", "Add background music", [],
         "<p>Download 3–5 instrumental tracks from <a href=\"https://pixabay.com/music/\" target=\"_blank\" rel=\"noopener\">Pixabay Music</a> "
         "(search <i>curious</i>, <i>suspense</i>, <i>documentary</i>; no vocals; skip tracks with the shield icon) into "
         "<code>assets\\music\\</code>. The first track is used automatically and dips under the voice.</p>"
         + code("start assets\\music", cmd=True)),
    step("a9", "Optional: sharper pictures with Real-ESRGAN", ["ps"],
         "<p>Free AI upscaler that runs on your laptop's graphics card. Open "
         "<a href=\"https://github.com/xinntao/Real-ESRGAN/releases\" target=\"_blank\" rel=\"noopener\">Real-ESRGAN releases</a>, "
         "download <code>realesrgan-ncnn-vulkan-…-windows.zip</code>, and unzip it so the file "
         "<code>tools\\realesrgan\\realesrgan-ncnn-vulkan.exe</code> exists (with its <code>models</code> folder next to it). "
         "Final renders then upscale small pictures automatically.</p>"
         + code("dir tools\\realesrgan", cmd=True)),
    step("a10", "Optional: install faster-whisper for voiceover files", ["ps"],
         "<p>Needed only when you use an AI Studio or self-recorded voiceover. The first use downloads a speech model once.</p>"
         + code("python -m pip install faster-whisper", cmd=True)),
    step("a6", "Save the project in git", ["ps"],
         code('git init\ngit add .\ngit commit -m "Start HowZit animated explainers"', cmd=True)),
]))

P.append(phase(2, "Story to script", "Every new video starts here. Press <b>New video</b> at the top to clear the ticks from phase 2 on.", [
    step("b0", "Pick a viral idea (Gemini G0)", ["gemini", "notepad"],
         "<p>Skip this if you already have a story. Open the idea list, copy its titles into the last HowZit rule of G0, "
         "and send G0 in a new Gemini chat. Pick the title you would tap on first, and add the other good ones to the list "
         "with status <code>idea</code>.</p>"
         + code("notepad ideas\\backlog.csv", cmd=True)
         + code(prompt("G0"), "G0")),
    step("b1", "Make the episode folder", ["ps"],
         "<p>Use a short title. The command prints the folder name; type that name into <b>Episode folder</b> at the top.</p>"
         + code('.venv\\Scripts\\Activate.ps1\npython -m studio.new "Why do onions make you cry"', cmd=True)),
    step("b2", "Paste your story", ["notepad"],
         "<p>Write or paste the story, the facts you know, and the twist if there is one. If you only have a title from G0, paste just the title: G1 researches it. Save.</p>"
         + code("notepad episodes\\{EP}\\story.md", cmd=True)),
    step("b3", "Decide: hook or reveal", [],
         '<div class="tbl"><table><thead><tr><th>Use</th><th>When</th><th>How it plays</th></tr></thead><tbody>'
         "<tr><td><b>hook</b></td><td>There's a surprising fact or a question people already ask (how does Wi-Fi work?)</td><td>Question + surprising fact in the first 3 s, in the lime hook box. Three steps, then the payoff.</td></tr>"
         "<tr><td><b>reveal</b></td><td>The story has a twist, a mystery or a surprising ending (an invention by accident, a hidden reason)</td><td>Scene 1 teases the ending. An open loop every 2–3 scenes (\"but that wasn't the strangest part\"). The answer only in the last scene, with the one lime pop-up.</td></tr>"
         "</tbody></table></div><p class=\"save\">G1 picks one for you. To force it, add <code>Use structure: reveal.</code> after your story.</p>"),
    step("b4", "Gemini G1: write the script", ["gemini"],
         "<p>Open a <b>new chat</b> in Gemini. Copy this, replace the last line with your story, send.</p>"
         + code(prompt("G1"), "G1")),
    step("b5", "Gemini G2: fact check", ["gemini"],
         "<p>Same chat. Copy, then paste Gemini's YAML from G1 where it says. Read every ⚠️ and ❌ yourself.</p>"
         + code(prompt("G2"), "G2")),
    step("b6", "Gemini G3: keep people watching", ["gemini"],
         "<p>Same chat, with the YAML from G2. Aim for a first-3-seconds score of 8 or more; if lower, ask: <i>Give me 5 stronger first lines</i>.</p>"
         + code(prompt("G3"), "G3")),
    step("b7", "Save script.yaml", ["notepad"],
         "<p>Click the copy button on Gemini's last YAML block. In Notepad press Ctrl+A, paste, Ctrl+S.</p>"
         + code("notepad episodes\\{EP}\\script.yaml", cmd=True)),
]))

P.append(phase(3, "Voice, music and timing", "Cheap to fix now, before any pictures exist.", [
    step("c0", "Choose the voice for this video", ["gemini"],
         "<p><b>Quick:</b> do nothing; the voice from step 1·7 reads the script. "
         "<b>Most natural:</b> run the draft once (next step), open the prompts file, and use the G8 block in "
         "<a href=\"https://aistudio.google.com\" target=\"_blank\" rel=\"noopener\">Google AI Studio</a> (speech generation, single speaker, try Puck or Fenrir). "
         "Save the WAV as <code>audio\\voiceover.wav</code> in the episode folder and add this line to script.yaml:</p>"
         + code("voiceover: audio\\voiceover.wav", short=True)
         + code(prompt("G8"), "G8 style line")),
    step("c1", "Draft render", ["ps"],
         "<p>Placeholder cards instead of pictures, real narrator, real timing. Also writes the filled-in picture prompts for phase 4.</p>"
         + code("python -m studio.build episodes\\{EP} --draft", cmd=True)),
    step("c2", "Watch and listen to the draft", ["ps"],
         "<p>The draft is half size and blurry on purpose (fast). Judge timing and sound only.</p>"
         "<ul><li>Do the first 3 seconds make you want to keep watching?</li><li>Is the voice clear over the music? Music too loud → lower <code>music: volume</code> in the preset.</li>"
         "<li>Do pop-ups land on the right word, with a pop sound?</li><li>Any line too long or hard to follow? Shorten it in script.yaml.</li><li>45–60 seconds long?</li></ul>"
         + code("start episodes\\{EP}\\output\\{EP}_howzit_draft.mp4", cmd=True)),
    step("c3", "Fix warnings and re-run", ["ps", "notepad"],
         "<p><code>pop-up word not found</code> → make <code>at_word</code> match the narration exactly. <code>hook text is long</code> → shorten <code>hook</code> to 3–7 words. "
         "<code>formatting problem near line N</code> → re-copy the YAML with Gemini's copy button. Re-running is fast: the voice is cached.</p>"),
]))

P.append(phase(4, "Pictures and clips in Gemini", "Keep every picture for this episode in one Gemini chat so the characters stay the same.", [
    step("d1", "Open the filled-in prompts", ["notepad"],
         "<p>The draft wrote every G4, G5 and G6 prompt with your characters and scenes already filled in. Use those blocks; the templates below are for reference.</p>"
         + code("notepad episodes\\{EP}\\output\\{EP}_gemini_prompts.md", cmd=True)),
    step("d2", "G4: reference sheet for each character or key object", ["gemini"],
         "<p>New Gemini chat. One sheet per character. Regenerate until it looks right, then keep that chat open.</p>"
         + code(prompt("G4"), "G4 template")),
    step("d3", "G5: one picture per scene", ["gemini"],
         "<p>First scene: attach the reference sheet and send the first block. Every next scene: the short block. "
         "If Gemini offers an image size, pick the largest. Download each picture with the download button (never a screenshot).</p>"
         + code(prompt("G5", 0), "G5 first scene") + code(prompt("G5", 1), "G5 next scenes", short=True)
         + '<p class="save">Save as <b>episodes\\&lt;episode&gt;\\images\\s01.png</b>, s02.png … (the scene id). If a character drifts, re-attach the sheet and say <i>same character as the reference, same clothes</i>. Reject any picture with text or letters in it.</p>'),
    step("d4", "G6: 2–3 moving clips with Veo", ["gemini"],
         "<p>Only for scenes with a <code>veo:</code> line. Attach that scene's picture. Gemini Pro has a daily limit on videos, so pick the best moments.</p>"
         + code(prompt("G6"), "G6 template")
         + '<p class="save">Save as <b>episodes\\&lt;episode&gt;\\clips\\s05.mp4</b> (the scene id). Its own sound is dropped.</p>'),
    step("d5", "Check every scene has a picture", ["ps"],
         code("dir episodes\\{EP}\\images\ndir episodes\\{EP}\\clips", cmd=True)),
]))

P.append(phase(5, "Final render and phone check", "", [
    step("e1", "Final render", ["ps"],
         "<p>Full quality: 1080×1920, smooth camera moves, near-lossless video, music and sound effects. Takes several minutes.</p>"
         + code("python -m studio.build episodes\\{EP}", cmd=True)),
    step("e2", "Watch it on your phone, full screen", ["phone"],
         "<p>Send <code>output\\&lt;episode&gt;_howzit.mp4</code> to your phone (WhatsApp to yourself as a document, or Google Drive). Check:</p>"
         "<ul><li>The hook works in the first 3 seconds (or the reveal teaser makes you curious).</li><li>Captions are readable over every picture.</li><li>No text or letters inside Gemini's pictures.</li>"
         "<li>Voice clear, music audible but quiet, whoosh and pop not too loud.</li><li>Pictures sharp, no blocky or smeared patches.</li><li>Nothing important under Instagram's buttons (right edge, bottom).</li><li>HowZit watermark top-right, HowZit end card at the end.</li><li>People look realistic → remember to turn on Instagram's AI label when posting.</li><li>For reveal videos: the answer isn't given away early.</li></ul>"),
    step("e3", "Fix one scene quickly if needed", ["ps"],
         "<p>Replace the picture or edit the line, check just that scene, then run the final render again.</p>"
         + code("python -m studio.build episodes\\{EP} --draft --only s04", cmd=True)),
    step("e4", "Every fact has 2 sources", ["notepad"],
         "<p>The table at the top of the posting note must have no <b>NEEDS 2 SOURCES</b> left. If it does, run G2 again for those claims.</p>"
         + code("notepad episodes\\{EP}\\output\\{EP}_post.md", cmd=True)),
]))

P.append(phase(6, "Post on HowZit, Collab with Lowkey Genius", "", [
    step("f1", "Get the caption, hashtags, cover text", ["notepad"],
         "<p>All in the posting note: the caption (first line is the hook), exactly 5 hashtags, cover text and alt text.</p>"
         + code("notepad episodes\\{EP}\\output\\{EP}_post.md", cmd=True)),
    step("f2", "Optional, Gemini G7: fresher caption", ["gemini"],
         "<p>Uses Google Search for how people search the topic right now. Paste your script.yaml where it says.</p>"
         + code(prompt("G7"), "G7")),
    step("f3", "Post the Reel on @howzit.explains", ["ig"],
         "<ol><li>+ → Reel → pick the video → Next.</li><li>Paste the caption and hashtags.</li><li>Edit cover → pick the frame with the lime hook box.</li>"
         "<li>Tag people → <b>Invite collaborator</b> → the Lowkey Genius page.</li><li>Advanced settings → turn on the <b>AI label</b> (the 3D scenes are AI-made and look fairly real).</li><li>If Advanced settings shows Accessibility → Alt text, paste the alt text.</li><li>Share.</li></ol>"),
    step("f4", "Accept the Collab on the Lowkey Genius page", ["ig"],
         "<p>Switch to the Lowkey Genius account → DMs → open the invite → Accept. The Reel then shows on both pages and likes, comments, shares and saves are combined.</p>"),
    step("f5", "Pin a question comment, reply in the first hour", ["ig"],
         "<p>Pin the question from the caption (\"Did you know…? 👇\"). Reply to every comment in the first hour; note new questions as topic ideas.</p>"),
]))

P.append(phase(7, "After 48 hours", "", [
    step("g1", "Read the Reel's insights", ["ig"],
         "<p>Note plays, average watch time, how many watched to the end, shares and saves. Shares and full watches matter most.</p>"),
    step("g2", "Learn one thing for the next video", [],
         "<ul><li>Most people leave in the first 3 s → stronger hook or teaser next time.</li><li>People leave in the middle → shorter scenes, more open loops.</li>"
         "<li>Lots of shares or saves → make a part 2 on the same topic.</li></ul>"
         "<p class=\"save\">Log the topic as posted in <code>G:\\Apps\\youtube_clipping\\templates\\trackers\\explainer-ideas.csv</code>.</p>"),
]))

TRENDING = ('<div class="note"><b>About trending.</b> Nobody can guarantee it. Instagram pushes Reels that people watch to the end, rewatch, '
            'share and save; hashtags only help a little, and Instagram allows 5. So the work that matters most is the hook or the reveal (phase 2) '
            'and the phone check (phase 5).</div>')

tpl = (ROOT / "docs" / "checklist" / "template.html").read_text(encoding="utf-8")
out = tpl.replace("<!--PHASES-->", TRENDING + "\n" + "\n".join(P))
dest = ROOT / "docs" / "checklist" / "howzit-reel-checklist.html"
dest.write_text(out, encoding="utf-8")
print(dest.relative_to(ROOT))
