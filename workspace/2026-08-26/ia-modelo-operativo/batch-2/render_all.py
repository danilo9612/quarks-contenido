import json, subprocess, sys, os, pathlib
SKILL = pathlib.Path(os.path.expanduser("~/.claude/skills/ig-carousels"))
BRAND = pathlib.Path(os.path.expanduser("~/.claude/skills/quarks-brand/brand_style_guide.md"))
slides = json.load(open("copy.json", encoding="utf-8"))
tmp = pathlib.Path("slide_data"); tmp.mkdir(exist_ok=True)
for s in slides:
    n = s["slide_num"]
    f = tmp / f"slide_{n:02d}.json"
    f.write_text(json.dumps(s, ensure_ascii=False), encoding="utf-8")
    out = f"slide_{n:02d}.png"
    r = subprocess.run([sys.executable, str(SKILL/"tools"/"render_slide.py"),
        "--template", "slide_statement", "--data-file", str(f),
        "--brand-style", str(BRAND), "--output", out],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(n, "OK" if r.returncode == 0 else "FAIL")
    if r.returncode: print(r.stdout[-1500:], r.stderr[-1500:])
