# -*- coding: utf-8 -*-
import sys

builtins = __import__('builtins')
builtins.true = True
builtins.false = False
builtins.null = None

sys.path.append('scripts')
import pplg_data_easy
import pplg_data_medium
import pplg_data_hard
import pplg_data_simulasi

all_q = (
    pplg_data_easy.EASY_QUESTIONS +
    pplg_data_medium.MEDIUM_QUESTIONS +
    pplg_data_hard.HARD_QUESTIONS +
    pplg_data_simulasi.SIMULASI_QUESTIONS
)

errors = []
ids = set()

for i, q in enumerate(all_q):
    qid = q.get('id')
    if not qid:
        errors.append(f'Question {i}: missing id')
    elif qid in ids:
        errors.append(f'Duplicate id: {qid}')
    else:
        ids.add(qid)
    
    if q.get('subject') != 'rpl':
        errors.append(f"{qid}: subject is {q.get('subject')} (expected 'rpl')")
    
    q_type = q.get('type')
    if q_type == 'mcq':
        opts = q.get('options', [])
        if not opts or len(opts) < 4:
            errors.append(f"{qid}: mcq options count < 4 ({len(opts)})")
        opt_keys = [o.get('key') for o in opts]
        if q.get('correctKey') not in opt_keys:
            errors.append(f"{qid}: correctKey {q.get('correctKey')} not in {opt_keys}")
    elif q_type == 'multi':
        opts = q.get('options', [])
        opt_keys = [o.get('key') for o in opts]
        c_keys = q.get('correctKeys', [])
        if not c_keys or not isinstance(c_keys, list):
            errors.append(f"{qid}: multi missing valid correctKeys")
        for ck in c_keys:
            if ck not in opt_keys:
                errors.append(f"{qid}: correctKey {ck} not in {opt_keys}")
    elif q_type == 'matrix':
        stmts = q.get('statements', [])
        ans = q.get('correctAnswers', {})
        if not stmts or not ans:
            errors.append(f"{qid}: matrix missing statements or correctAnswers")
        stmt_ids = [s.get('id') for s in stmts]
        for sid in stmt_ids:
            if sid not in ans or not isinstance(ans[sid], bool):
                errors.append(f"{qid}: matrix missing boolean answer for statement {sid}")
    else:
        errors.append(f"{qid}: unknown type {q_type}")
        
    hud = q.get('formulaHud')
    if not hud or not hud.get('title') or not hud.get('latex'):
        errors.append(f"{qid}: formulaHud missing or incomplete")
        
    hints = q.get('hints')
    if not hints or not hints.get('concept') or not hints.get('execution'):
        errors.append(f"{qid}: hints missing concept or execution")
        
    if not q.get('explanation'):
        errors.append(f"{qid}: missing explanation")

print(f"Total questions checked: {len(all_q)}")
print(f"Total unique IDs: {len(ids)}")
if errors:
    print(f"Found {len(errors)} issues:")
    for e in errors[:30]:
        print(" -", e)
else:
    print("SUCCESS: ALL 110 QUESTIONS VALIDATED WITH ZERO ERRORS!")
