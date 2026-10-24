# -*- coding: utf-8 -*-
"""
Script to build the full 110 authentic questions for TKA PPLG (SMK)
Strictly based on Simulasi_TKA_PPLG_SMK_50_Soal.pdf (BSKAP No. 046/H/KR/2025)
Total: 110 Soal
- 25 Soal Latihan Easy (rpl-lat-e-01 s.d. 25)
- 25 Soal Latihan Medium (rpl-lat-m-01 s.d. 25)
- 25 Soal Latihan Hard / HOTS (rpl-lat-h-01 s.d. 25)
- 35 Soal Simulasi Resmi (rpl-sim-01 s.d. 35: 25 MCQ, 5 Multi, 5 Matrix)
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

builtins = __import__('builtins')
builtins.true = True
builtins.false = False
builtins.null = None

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pplg_data_easy
import pplg_data_medium
import pplg_data_hard
import pplg_data_simulasi

easy = pplg_data_easy.EASY_QUESTIONS
medium = pplg_data_medium.MEDIUM_QUESTIONS
hard = pplg_data_hard.HARD_QUESTIONS
sim = pplg_data_simulasi.SIMULASI_QUESTIONS

print(f"Loaded: Easy={len(easy)}, Medium={len(medium)}, Hard={len(hard)}, Simulasi={len(sim)}")

all_questions = easy + medium + hard + sim
total = len(all_questions)
print(f"Total compiled questions: {total}")
assert total == 110, f"Expected 110 questions, got {total}"

# Verify uniqueness of IDs
ids = [q['id'] for q in all_questions]
assert len(ids) == len(set(ids)), f"Duplicate IDs detected: {len(ids)} vs {len(set(ids))}"

# Verify schema
for q in all_questions:
    assert q.get('subject') == 'rpl'
    assert q.get('materi')
    assert q.get('topic')
    assert q.get('type') in ['mcq', 'multi', 'matrix']
    assert q.get('questionHtml')
    assert q.get('formulaHud') and q['formulaHud'].get('title') and q['formulaHud'].get('latex')
    assert q.get('hints') and q['hints'].get('concept') and q['hints'].get('execution')
    assert q.get('explanation')

out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'questions_rpl.js')
js_content = "window.TKA_RPL_QUESTIONS = " + json.dumps(all_questions, indent=2, ensure_ascii=False) + ";\n"

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated {out_path} ({len(js_content)} bytes)")
