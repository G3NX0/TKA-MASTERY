import glob
import re
import json

files = sorted(glob.glob("data/questions_*.js"))

rows = []

for f in files:
    if "questions_db.js" in f:
        continue
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    match = re.search(r"=\s*(\[.*\]);?\s*$", content, re.DOTALL)
    if not match:
        continue
    
    try:
        data = json.loads(match.group(1))
    except Exception as e:
        continue
    
    subj = f.replace("data\\questions_", "").replace("data/questions_", "").replace(".js", "")
    
    lat_easy = sum(1 for q in data if q.get("mode") == "latihan" and q.get("difficulty") == "easy")
    lat_med = sum(1 for q in data if q.get("mode") == "latihan" and q.get("difficulty") == "medium")
    lat_hard = sum(1 for q in data if q.get("mode") == "latihan" and q.get("difficulty") == "hard")
    sim = sum(1 for q in data if q.get("mode") == "simulasi" or q.get("isSimulation") is True)
    
    total_lat = lat_easy + lat_med + lat_hard
    total = len(data)
    
    rows.append({
        "subject": subj,
        "total": total,
        "lat_easy": lat_easy,
        "lat_med": lat_med,
        "lat_hard": lat_hard,
        "total_lat": total_lat,
        "sim": sim,
        "balanced": (lat_easy == lat_med == lat_hard and total_lat + sim == total)
    })

print("=" * 86)
print(f"{'Mata Pelajaran':<24} | {'Total':<5} | {'Easy':<5} | {'Med':<5} | {'Hard':<5} | {'TotLat':<6} | {'Simulasi':<8} | {'Status':<8}")
print("=" * 86)
for r in rows:
    status = "VALID OK" if r["balanced"] else "UNBALANCED"
    print(f"{r['subject']:<24} | {r['total']:<5} | {r['lat_easy']:<5} | {r['lat_med']:<5} | {r['lat_hard']:<5} | {r['total_lat']:<6} | {r['sim']:<8} | {status:<8}")
print("=" * 86)

grand_total = sum(r["total"] for r in rows)
grand_lat = sum(r["total_lat"] for r in rows)
grand_sim = sum(r["sim"] for r in rows)
print(f"Grand Total Soal: {grand_total} | Total Latihan: {grand_lat} | Total Simulasi HOTS: {grand_sim}")
