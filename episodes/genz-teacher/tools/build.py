"""Build the Gen Z teacher Reel: 9 Flow clips + ElevenLabs narration + captions + pop-ups + SFX."""
import glob, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "/mnt/user-data/uploads/Downloads"
NARR = "/tmp/claude-0/-home-claude/bed6b360-1ef6-53ca-9b82-f68e813a662f/scratchpad/audio/narration.mp3"
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
END = 32.30  # narration cut 31.95 + short tail

# (timeline start, end, file prefix, source in, speed)
SEG = [
    (0.00, 3.30, "Teacher_walking_in_exam", 0.30, 1.0),          # C01
    (3.30, 5.50, "Students_sharing_sly", 1.80, 1.0),              # C02
    (5.50, 7.90, "Students_passing_exam_papers", 3.40, 1.0),      # C03
    (7.90, 10.10, "Students_sharing_answer_booklet", 0.50, 1.0),  # C04
    (10.10, 12.80, "Boy_cheating_on_exam", 1.60, 1.0),            # C05
    (12.80, 18.90, "Teacher_walking_holding_phone", 0.60, 1.0),   # C06b
    (18.90, 21.90, "Teacher_filming_cheating", 0.40, 1.0),        # C07a part 1 (phone sideways, boxes lock on)
    (21.90, 23.75, "Teacher_filming_cheating", 5.20, 1.0),        # C07a part 2 (closer: every face boxed)
    (23.75, 27.90, "Cartoon_student_drops_exam", 3.80, 1.0),      # C08
    (27.90, END, "Students_and_teacher_in_classroom", 3.60, 1.0), # C09
]

CAPS = [(0.08,"The teacher"),(0.55,"turned her back"),(1.36,"and slowly"),(2.09,"walked down"),(2.61,"the aisle,"),
 (3.29,"so the students"),(3.94,"thought they"),(4.26,"were safe."),(5.50,"Papers started"),(6.17,"flying across"),
 (7.04,"the desks,"),(7.88,"one kid passed"),(8.67,"his whole"),(9.21,"answer sheet,"),(10.18,"and another"),
 (10.66,"grabbed a"),(10.98,"cheat sheet"),(11.52,"off the floor."),(12.72,"But behind"),(13.25,"her back,"),
 (13.95,"she was holding"),(14.56,"her phone"),(14.96,"sideways,"),(15.88,"with the"),(16.21,"ultra-wide camera"),
 (17.20,"pointed right"),(17.95,"at them."),(18.88,"And as it"),(19.20,"recorded"),(19.68,"in 4K,"),
 (20.79,"it locked onto"),(21.64,"every single"),(22.40,"face"),(22.77,"in the room."),(23.75,"So by the time"),
 (24.44,"one kid"),(24.86,"looked up"),(25.34,"and saw"),(25.66,"the screen,"),(26.51,"it was"),
 (26.76,"already too late,"),(28.00,"and the only"),(28.58,"thing they"),(28.88,"passed that day"),
 (29.80,"was the paper…"),(30.87,"not the exam.")]
CAP_END = {"were safe.":5.0, "off the floor.":12.6, "at them.":18.75, "in the room.":23.6, "already too late,":27.85, "not the exam.":32.2}

def t(s):
    h=int(s//3600); m=int(s%3600//60); return f"{h}:{m:02d}:{s%60:05.2f}"

def write_ass(path):
    W,H=1080,1920
    hdr=f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Poppins,104,&H00FFFFFF,&H00FFFFFF,&H00161616,&H90000000,-1,0,0,0,100,100,0,0,1,7,4,2,60,60,{int(H*0.22)},1
Style: Top,Poppins,78,&H00FFFFFF,&H00FFFFFF,&H00161616,&H90000000,-1,0,0,0,100,100,0,0,1,6,4,8,70,70,190,1
Style: Big,Poppins,360,&H0035F5C8,&H00FFFFFF,&H00161616,&H90000000,-1,0,0,0,100,100,0,0,1,12,8,5,0,0,0,1
Style: Rec,Poppins,64,&H003C3CFF,&H00FFFFFF,&H00161616,&H90000000,-1,0,0,0,100,100,4,0,1,5,3,8,0,0,160,1
Style: Bang,Poppins,260,&H002E2EFF,&H00FFFFFF,&H00FFFFFF,&H90000000,-1,0,0,0,100,100,0,0,1,10,6,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev=[]
    pop=r"{\fscx80\fscy80\t(0,90,\fscx100\fscy100)}"
    for i,(s,txt) in enumerate(CAPS):
        e=CAP_END.get(txt, CAPS[i+1][0] if i+1<len(CAPS) else END)
        ev.append(f"Dialogue: 1,{t(s)},{t(e)},Cap,,0,0,0,,{pop}{txt}")
    # hook title (from the script) and end title
    ev.append(f"Dialogue: 2,{t(0.0)},{t(3.25)},Top,,0,0,0,,{{\\fad(120,150)}}Rule #1: Don't underestimate\\NGen Z teachers.")
    ev.append(f"Dialogue: 2,{t(28.0)},{t(END)},Top,,0,0,0,,{{\\fad(150,0)\\fscx85\\fscy85\\t(0,200,\\fscx100\\fscy100)}}NEVER underestimate\\Na Gen Z teacher.")
    ev.append(f"Dialogue: 3,{t(18.90)},{t(23.70)},Rec,,0,0,0,,● REC")
    ev.append(f"Dialogue: 3,{t(19.70)},{t(21.20)},Big,,0,0,0,,{{\\pos(540,820)\\fscx40\\fscy40\\t(0,140,\\fscx110\\fscy110)\\t(140,260,\\fscx100\\fscy100)\\fad(0,200)}}4K")
    ev.append(f"Dialogue: 3,{t(24.86)},{t(25.90)},Bang,,0,0,0,,{{\\pos(540,560)\\fscx30\\fscy30\\t(0,120,\\fscx110\\fscy110)\\t(120,220,\\fscx100\\fscy100)\\fad(0,150)}}!")
    open(path,"w").write(hdr+"\n".join(ev)+"\n")

def skull_png(path, size=120):
    f=ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",109)
    im=Image.new("RGBA",(136,128),(0,0,0,0)); ImageDraw.Draw(im).text((0,0),"\U0001F480",font=f,embedded_color=True)
    sk=im.crop(im.getbbox()).resize((size,size),Image.LANCZOS)
    pf=ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf",100)
    lab=Image.new("RGBA",(1000,170),(0,0,0,0)); d=ImageDraw.Draw(lab)
    d.text((20,85),"Caught in 4K",font=pf,anchor="lm",fill=(200,245,53,255),stroke_width=8,stroke_fill=(22,22,22,255))
    w=int(d.textlength("Caught in 4K",font=pf))+20+16
    lab.alpha_composite(sk,(w+10,(170-size)//2))
    lab=lab.crop(lab.getbbox()); lab.save(path.replace(".png","_label.png")); sk.save(path)

def find(prefix):
    m=sorted(glob.glob(os.path.join(SRC, prefix+"*.mp4")))
    return m[-1] if m else None

def main():
    ass=os.path.join(OUT,"captions.ass"); write_ass(ass)
    sk=os.path.join(OUT,"skull.png"); skull_png(sk)
    parts=[]
    for i,(a,b,pre,sin,sp) in enumerate(SEG):
        f=find(pre); dur=b-a; p=os.path.join(OUT,f"seg{i+1:02d}.mp4")
        if not f:
            print("MISSING", pre); subprocess.run(["ffmpeg","-y","-v","error","-f","lavfi","-i",f"color=c=0x203040:s=1080x1920:r=24:d={dur}",
                "-f","lavfi","-i",f"anullsrc=r=48000:cl=stereo","-t",f"{dur}","-c:v","libx264","-pix_fmt","yuv420p","-c:a","aac",p],check=True)
        else:
            srcdur=dur*sp
            vf=f"setpts=(PTS-STARTPTS)/{sp},fps=24,scale=1080:1920:flags=lanczos"
            if pre.startswith("Students_and_teacher"): vf+=",eq=saturation=0.45:contrast=1.08"   # slow-mo 'caught' grade
            af=f"asetpts=PTS-STARTPTS,atempo={sp},aresample=48000"
            subprocess.run(["ffmpeg","-y","-v","error","-ss",f"{sin}","-t",f"{srcdur+0.05}","-i",f,
                "-vf",vf,"-af",af,"-t",f"{dur}","-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p",
                "-c:a","aac","-b:a","192k","-ac","2",p],check=True)
        parts.append(p)
    lst=os.path.join(OUT,"list.txt"); open(lst,"w").write("".join(f"file '{p}'\n" for p in parts))
    vid=os.path.join(OUT,"video_raw.mp4")
    subprocess.run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",lst,"-c:v","libx264","-crf","16","-preset","medium",
                    "-c:a","aac","-b:a","192k",vid],check=True)
    # SFX cues: (file, time, gain dB)
    S=lambda n: os.path.join(HERE,n)
    cues=[("whoosh.wav",5.40,-8),("whoosh.wav",7.80,-8),("whoosh.wav",10.00,-8),("scratch.wav",12.62,-4),("impact.wav",12.80,-2),
          ("pop.wav",19.70,-6),("whoosh.wav",21.80,-10),("impact.wav",19.72,-5),("impact.wav",24.86,-2),("whoosh.wav",27.80,-6)]
    inputs=["-i",vid,"-i",NARR,"-f","lavfi","-i","nullsrc=s=16x16:d=0.1","-loop","1","-t",f"{END}","-i",sk.replace(".png","_label.png")]
    for c in cues: inputs+=["-i",S(c[0])]
    fc=[f"[0:v]subtitles='{ass}':fontsdir=/usr/share/fonts/truetype/google-fonts[v1]",
        "[3:v]format=rgba[lb]",
        "[v1]null[v2]",
        f"[v2][lb]overlay=x=(W-w)/2:y=400:enable='between(t,30.87,{END})'[v]",
        "[0:a]volume=-9dB[clip]",
        f"[1:a]atrim=0:31.95,afade=t=out:st=31.75:d=0.2,aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-15:TP=-2:LRA=7[nar]"]
    mix=["[nar]","[clip]"]
    for k,(n,tm,g) in enumerate(cues):
        idx=4+k; ms=int(tm*1000)
        fc.append(f"[{idx}:a]aresample=48000,aformat=channel_layouts=stereo,volume={g}dB,adelay={ms}|{ms}[s{k}]"); mix.append(f"[s{k}]")
    fc.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=first,atrim=0:{END},loudnorm=I=-14:TP=-1:LRA=9[a]")
    final=os.path.join(OUT,"genz-teacher-final.mp4")
    subprocess.run(["ffmpeg","-y","-v","error",*inputs,"-filter_complex",";".join(fc),"-map","[v]","-map","[a]","-t",f"{END}",
        "-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p","-r","24","-c:a","aac","-b:a","192k","-ar","48000",
        "-movflags","+faststart",final],check=True)
    print("done", final)

if __name__=="__main__":
    main()
