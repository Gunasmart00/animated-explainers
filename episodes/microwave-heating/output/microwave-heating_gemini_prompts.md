# How a Microwave Heats Food — Gemini picture prompts

Open a **new Gemini chat** for this episode and keep every picture in that one chat.
Copy each block in order. Save each picture as `images\<scene id>.png`, each clip as `clips\<scene id>.mp4`.

## G4 — Reference sheets (do these first, keep the ones you like)

### the microwave
```
Create a reference sheet for a 3D animated explainer, vertical 9:16.
Subject: the microwave: a rounded retro countertop microwave oven, pale mint body, dark glass door, glowing lime interior light
Show: front view, three-quarter view, side view, and one close-up detail (the face, for a character), neutral pose, on a plain dark-green background (#13261A).
Style: High-end 3D animated render with the look of a polished 3D explainer short: semi-realistic 3D characters with natural skin, expressive faces and detailed clothing; clean, modern, well-lit spaces with soft pastel blue-grey walls and simple props; soft global illumination, gentle shadows and warm accent lights; shallow depth of field with a softly blurred background; crisp, sharp, highly detailed, rendered like Unreal Engine 5. Not a photograph and not a cartoon. Highest quality, sharp focus, no blur on the main subject.
No text, letters, numbers, logos or watermarks.
```

## G5 — Scene pictures

### s01 → save as `images\s01.png`
_Narration: Your microwave can boil water in two minutes, but the oven itself barely gets warm. So where does the heat come from?_
```
Use the attached reference for the microwave: keep exactly the same look, shape, clothes and colours.
Create one frame of a 3D animated explainer, vertical 9:16 (1080x1920).
Scene: the microwave on a dark kitchen counter, door open, a mug of water inside with steam rising, low-angle close-up
Composition: the main subject in the middle of the frame, between 20% and 62% of the height. Keep the area around 70% of the height calm, because captions go there, and put nothing important at the right edge or the bottom 20%.
Style: High-end 3D animated render with the look of a polished 3D explainer short: semi-realistic 3D characters with natural skin, expressive faces and detailed clothing; clean, modern, well-lit spaces with soft pastel blue-grey walls and simple props; soft global illumination, gentle shadows and warm accent lights; shallow depth of field with a softly blurred background; crisp, sharp, highly detailed, rendered like Unreal Engine 5. Not a photograph and not a cartoon. Highest quality, sharp focus, no blur on the main subject.
No text, letters, numbers, logos or watermarks anywhere in the image.
```

### s02 → save as `images\s02.png`
_Narration: Inside, a part called a magnetron makes invisible waves called microwaves._
```
Same characters, same style, same composition rules. Next frame, vertical 9:16: cutaway of the microwave, the magnetron glowing lime in the corner, sending soft wavy beams into the cooking chamber. No text in the image.
```

### s03 → save as `images\s03.png`
_Narration: The metal walls bounce the waves around, and the tiny holes in the door are too small for them to escape._
```
Same characters, same style, same composition rules. Next frame, vertical 9:16: inside the microwave chamber, glowing wave beams bouncing off shiny metal walls and stopping at the door mesh, wide shot. No text in the image.
```

### s04 → save as `images\s04.png`
_Narration: Now the clever part. Every water molecule has a slightly positive end and a slightly negative end._
```
Same characters, same style, same composition rules. Next frame, vertical 9:16: one big glossy water molecule floating, a lime oxygen ball with two mint hydrogen balls, dramatic close-up. No text in the image.
```

### s05 → save as `images\s05.png`
_Narration: The waves flip direction about 2.45 billion times every second, and the water molecules twist back and forth to keep up._
```
Same characters, same style, same composition rules. Next frame, vertical 9:16: hundreds of tiny water molecules spinning back and forth inside a bowl of soup, motion blur, top-down. No text in the image.
```

### s06 → save as `images\s06.png`
_Narration: All that twisting jostles the molecules around them, and that motion turns into heat._
```
Same characters, same style, same composition rules. Next frame, vertical 9:16: molecules bumping into each other, a soft lime glow of heat building in the middle of the soup. No text in the image.
```

### s07 → save as `images\s07.png`
_Narration: That's why wet food heats up fast, while a dry plate stays cool._
```
Same characters, same style, same composition rules. Next frame, vertical 9:16: a steaming bowl of soup glowing warm on a plain cool plate, side view. No text in the image.
```

### s08 → save as `images\s08.png`
_Narration: And the spinning plate? The waves leave hot and cold spots, so turning the food evens them out._
```
Same characters, same style, same composition rules. Next frame, vertical 9:16: top view of the turntable spinning with the soup, faint glowing hot spots and dim cold spots on the floor of the oven. No text in the image.
```

## G6 — Moving clips (Veo)

### s01 → attach `images\s01.png`, save as `clips\s01.mp4`
```
Animate the attached image into an 8-second vertical 9:16 video.
Motion: steam curls up from the mug while the microwave's lime interior light pulses softly.
Camera: slow push-in.
Keep the characters, colours and 3D style exactly the same as the image. No text, no subtitles, no music, no talking, no new characters.
```

### s05 → attach `images\s05.png`, save as `clips\s05.mp4`
```
Animate the attached image into an 8-second vertical 9:16 video.
Motion: the water molecules twist rapidly back and forth; the soup surface starts to shimmer.
Camera: slow push-in.
Keep the characters, colours and 3D style exactly the same as the image. No text, no subtitles, no music, no talking, no new characters.
```

## G8 — Voiceover in Google AI Studio (optional)
Paste the style line, then the narration below it. Save the WAV as `audio\voiceover.wav` and add `voiceover: audio\voiceover.wav` to script.yaml.
```
Read this as a young American male storyteller for a 60-second animated explainer: quick, energetic, curious and a little playful, like telling a friend a surprising story. Natural short pauses between sentences, a little extra emphasis on numbers and surprising words. Read every word exactly as written; don't add or change anything.

Your microwave can boil water in two minutes, but the oven itself barely gets warm. So where does the heat come from?

Inside, a part called a magnetron makes invisible waves called microwaves.

The metal walls bounce the waves around, and the tiny holes in the door are too small for them to escape.

Now the clever part. Every water molecule has a slightly positive end and a slightly negative end.

The waves flip direction about 2.45 billion times every second, and the water molecules twist back and forth to keep up.

All that twisting jostles the molecules around them, and that motion turns into heat.

That's why wet food heats up fast, while a dry plate stays cool.

And the spinning plate? The waves leave hot and cold spots, so turning the food evens them out.
```
