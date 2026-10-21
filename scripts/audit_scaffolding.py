import os
import glob
import re
import json

data_dir = r"c:\Users\glixer\.gemini\antigravity-ide\scratch\tka-mastery-hub\data"
files = sorted([f for f in glob.glob(os.path.join(data_dir, "questions_*.js")) if "questions_db.js" not in f])

print(f"Auditing scaffolding and difficulty across {len(files)} files...\n")

results = []

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    match = re.search(r"window\.\w+\s*=\s*(\[\s*\{.*\}\s*\]);?", content, re.DOTALL)
    if not match:
        print(f"FAILED TO PARSE: {fname}")
        continue
    
    try:
        items = json.loads(match.group(1))
    except Exception as e:
        print(f"JSON ERROR {fname}: {e}")
        continue
    
    diff_counts = {}
    missing_formula = 0
    missing_hints = 0
    missing_clue1 = 0
    missing_clue2 = 0
    missing_explanation = 0
    generic_explanation = 0
    
    for q in items:
        # Difficulty
        d = q.get("difficulty", "MISSING")
        diff_counts[d] = diff_counts.get(d, 0) + 1
        
        # Formula / Konsep
        formula = q.get("formulaHud") or q.get("formula") or q.get("concept")
        if not formula or not str(formula).strip():
            missing_formula += 1
            
        # Hints
        hints = q.get("hints")
        c1 = None
        c2 = None
        if isinstance(hints, dict):
            c1 = hints.get("concept") or hints.get("clue1")
            c2 = hints.get("execution") or hints.get("clue2")
        elif q.get("concept_hint") or q.get("execution_hint"):
            c1 = q.get("concept_hint")
            c2 = q.get("execution_hint")
            
        if not hints and not (q.get("concept_hint") or q.get("execution_hint")):
            missing_hints += 1
        if not c1 or not str(c1).strip():
            missing_clue1 += 1
        if not c2 or not str(c2).strip():
            missing_clue2 += 1
            
        # Explanation
        exp = q.get("explanation") or q.get("solution")
        if not exp or not str(exp).strip():
            missing_explanation += 1
        elif len(str(exp).strip()) < 20 or "panduan pengerjaan bertahap tersedia" in str(exp).lower():
            generic_explanation += 1
            
    results.append({
        "file": fname,
        "total": len(items),
        "difficulties": diff_counts,
        "missing_formula": missing_formula,
        "missing_hints": missing_hints,
        "missing_clue1": missing_clue1,
        "missing_clue2": missing_clue2,
        "missing_exp": missing_explanation,
        "generic_exp": generic_explanation
    })

print(f"{'FILE':<30} | {'TOTAL':<5} | {'DIFFICULTIES':<35} | {'NO FORM':<7} | {'NO C1':<6} | {'NO C2':<6} | {'NO EXP':<6}")
print("-" * 115)
for r in results:
    diff_str = ", ".join(f"{k}:{v}" for k, v in r["difficulties"].items())
    print(f"{r['file']:<30} | {r['total']:<5} | {diff_str:<35} | {r['missing_formula']:<7} | {r['missing_clue1']:<6} | {r['missing_clue2']:<6} | {r['missing_exp']:<6}")
