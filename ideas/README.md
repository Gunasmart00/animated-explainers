# Ideas

`backlog.csv` is the list of video ideas. Columns:

| Column | Values |
|---|---|
| title | the video title (3–10 words) |
| format | how-it-works · what-happens-if · survival · weird · body · hidden-function (the 6 viral formats in prompt G0) |
| status | idea → scripting → in-production → posted (also: sample, dropped) |
| episode | the folder name in `episodes\` once it exists |
| notes | anything worth remembering |

New ideas: run prompt **G0** in Gemini (`prompts\gemini.md`), paste the backlog titles into its last rule so it
doesn't repeat them, and add the good ones here with status `idea`. Ask Claude Code "add these to the backlog"
if you'd rather not edit the file yourself. The owner's original prompt is in `prompts\viral-ideas-generator.md`.
