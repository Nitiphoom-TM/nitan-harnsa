#!/usr/bin/env python3
import re, sys, asyncio, os
import edge_tts

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(PROJECT, "index.html")
AUDIO_DIR = os.path.join(PROJECT, "audio")
VOICE = "th-TH-PremwadeeNeural"

def extract_stories():
    src = open(HTML, encoding="utf-8").read()
    # จำกัดขอบเขตเฉพาะ array STORIES
    start = src.index("const STORIES = [")
    end = src.index("\n];", start)
    block = src[start:end]
    stories = []
    cur = None
    # ไล่ทีละบรรทัดตามลำดับ เพื่อคงการจับคู่ id -> scenes
    for m in re.finditer(r"id:\s*'([a-z0-9-]+)'|text:\s*'([^']*)'", block):
        if m.group(1) is not None:
            cur = {"id": m.group(1), "scenes": []}
            stories.append(cur)
        elif m.group(2) is not None and cur is not None:
            cur["scenes"].append(m.group(2))
    return stories

async def synth(text, out_mp3):
    comm = edge_tts.Communicate(text, VOICE, rate="+0%", pitch="+8Hz")
    with open(out_mp3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])

async def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    os.makedirs(AUDIO_DIR, exist_ok=True)
    stories = extract_stories()
    print(f"พบ {len(stories)} เรื่อง: " + ", ".join(f"{s['id']}({len(s['scenes'])})" for s in stories))
    for s in stories:
        if only and s["id"] != only:
            continue
        for i, text in enumerate(s["scenes"]):
            key = f"{s['id']}-{i}"
            out = os.path.join(AUDIO_DIR, key + ".mp3")
            await synth(text, out)
            print(f"  ✓ {key}  {os.path.getsize(out)} bytes")

asyncio.run(main())
