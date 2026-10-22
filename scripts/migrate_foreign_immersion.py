import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

def arab_rules(qid, qh):
    latin_letters = re.findall(r'[a-zA-Z]{3,}', re.sub(r'<[^>]+>', '', qh))
    if not latin_letters:
        return qh
    
    quotes = re.findall(r"('[\u0600-\u06FF\s\.\!\?،؛\:\-]+')", qh)
    
    if ("1)" in qh and "2)" in qh) or ("١)" in qh and "٢)" in qh):
        s1 = re.search(r"[1١]\)\s*('[\u0600-\u06FF\s\.\!\?،؛\:\-]+')", qh)
        s2 = re.search(r"[2٢]\)\s*('[\u0600-\u06FF\s\.\!\?،؛\:\-]+')", qh)
        if s1 and s2:
            return f"تَأَمَّلِ الجُمْلَتَيْنِ التَّالِيَتَيْنِ:\\n١) {s1.group(1)}\\n٢) {s2.group(1)}\\nمَا التَّحْلِيلُ النَّحْوِيُّ الصَّحِيحُ لَهُمَا؟"
            
    if "benar atau salah" in qh.lower() or "kategori benar" in qh.lower():
        return "حَدِّدْ صِحَّةَ العِبَارَاتِ التَّالِيَةِ (صَحِيحٌ / خَطَأٌ):"
        
    if quotes:
        main_q = quotes[0]
        if "..." in main_q or "…" in main_q:
            return f"تَأَمَّلِ الجُمْلَةَ التَّالِيَةَ:\\n{main_q}\\nاخْتَرْ الكَلِمَةَ الصَّحِيحَةَ لِمَلْءِ الفَرَاغِ:"
        elif "antonim" in qh.lower() or "lawan kata" in qh.lower() or "المتضاد" in qh.lower():
            return f"مَا الكَلِمَةُ المُضَادَّةُ لِلْكَلِمَةِ التَّالِيَةِ فِي المَعْنَى؟\\n{main_q}"
        elif "sinonim" in qh.lower() or "persamaan kata" in qh.lower() or "المرادف" in qh.lower():
            return f"مَا الكَلِمَةُ المُرَادِفَةُ لِلْكَلِمَةِ التَّالِيَةِ فِي المَعْنَى؟\\n{main_q}"
        else:
            return f"تَأَمَّلِ العِبَارَةَ التَّالِيَةَ:\\n{main_q}\\nاخْتَرْ الإِجَابَةَ الصَّحِيحَةَ:"
            
    return qh

def jpn_rules(qid, qh):
    latin_letters = re.findall(r'[a-zA-Z]{3,}', re.sub(r'<[^>]+>', '', qh))
    if not latin_letters:
        return qh
        
    jp_quotes = re.findall(r"('[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF\s\.\!\?、。\(\)（）\[\]A-Za-z0-9：:-]+')", qh)
    clean_quotes = [q for q in jp_quotes if re.search(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]', q)]
    
    if "benar atau salah" in qh.lower() or "kategori benar" in qh.lower():
        return "次の各文の正誤（正しい・誤り）を判断しなさい："
        
    if clean_quotes:
        main_q = clean_quotes[0]
        if "[" in main_q and "]" in main_q:
            return f"次の文の [ ... ] の言葉の正しい読み方を選びなさい：\\n{main_q}"
        if "（" in main_q or "(" in main_q or "..." in main_q or "…" in main_q:
            return f"次の文の（ ... ）に入る最も適切な言葉を選びなさい：\\n{main_q}"
        return f"次の文章を読んで、最も適切な答えを選びなさい：\\n{main_q}"
        
    return qh

def man_rules(qid, qh):
    latin_letters = re.findall(r'[a-zA-Z]{3,}', re.sub(r'<[^>]+>', '', qh))
    if not latin_letters:
        return qh
        
    cn_quotes = re.findall(r"('[\u4E00-\u9FAF\s\.\!\?，。、\(\)（）A-Za-z0-9：:-]+')", qh)
    clean_quotes = [q for q in cn_quotes if re.search(r'[\u4E00-\u9FAF]', q)]
    
    if "benar atau salah" in qh.lower() or "kategori benar" in qh.lower():
        return "判断下列各句的正确与错误："
        
    if clean_quotes:
        main_q = clean_quotes[0]
        if "..." in main_q or "…" in main_q or "(" in main_q or "（" in main_q:
            return f"选择最恰当的词语填空：\\n{main_q}"
        if "pinyin" in qh.lower() or "nada" in qh.lower() or "pelafalan" in qh.lower():
            return f"根据汉语拼音规则，选择正确的一项：\\n{main_q}"
        return f"阅读下列句子，选择正确答案：\\n{main_q}"
        
    return qh

def ger_rules(qid, qh):
    quotes = re.findall(r"('[\wäöüÄÖÜß\s\.\!\?\,\:\;\-\(\)\/\–]{10,}')", qh)
    if "benar atau salah" in qh.lower() or "kategori benar" in qh.lower():
        return "Bestimmen Sie, ob die folgenden Aussagen RICHTIG oder FALSCH sind:"
        
    if quotes:
        main_q = quotes[0]
        if "..." in main_q or "…" in main_q or "(" in main_q:
            return f"Wählen Sie die richtige Option, um den Satz zu ergänzen:\\n{main_q}"
        return f"Lesen Sie den folgenden Satz und wählen Sie die passende Antwort:\\n{main_q}"
        
    return qh

def fra_rules(qid, qh):
    quotes = re.findall(r"('[\wàâéèêëîïôùûüçœæÀÂÉÈÊËÎÏÔÙÛÜÇ\s\.\!\?\,\:\;\-\(\)\/\–]{10,}')", qh)
    if "benar atau salah" in qh.lower() or "kategori benar" in qh.lower():
        return "Indiquez si chaque affirmation est VRAIE ou FAUSSE :"
        
    if quotes:
        main_q = quotes[0]
        if "..." in main_q or "…" in main_q or "(" in main_q:
            return f"Choisissez la bonne réponse pour compléter la phrase :\\n{main_q}"
        return f"Lisez le texte suivant et choisissez la bonne réponse :\\n{main_q}"
        
    return qh

def kor_rules(qid, qh):
    quotes = re.findall(r"('[\uAC00-\uD7AF\u1100-\u11FF\s\.\!\?\,\:\;\-\(\)\/]{6,}')", qh)
    if "benar atau salah" in qh.lower() or "kategori benar" in qh.lower():
        return "다음 내용이 맞으면 O, 틀리면 X를 선택하십시오:"
        
    if quotes:
        main_q = quotes[0]
        if "..." in main_q or "…" in main_q or "(" in main_q:
            return f"다음 문장의 빈칸에 들어갈 가장 알맞은 것을 고르십시오:\\n{main_q}"
        return f"다음을 읽고 물음에 가장 알맞은 것을 고르십시오:\\n{main_q}"
        
    return qh

langs = [
    ('Bahasa Arab', 'data/questions_bahasa_arab.js', arab_rules),
    ('Bahasa Jepang', 'data/questions_bahasa_jepang.js', jpn_rules),
    ('Bahasa Mandarin', 'data/questions_bahasa_mandarin.js', man_rules),
    ('Bahasa Jerman', 'data/questions_bahasa_jerman.js', ger_rules),
    ('Bahasa Prancis', 'data/questions_bahasa_prancis.js', fra_rules),
    ('Bahasa Korea', 'data/questions_bahasa_korea.js', kor_rules)
]

for name, fp, rule in langs:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find question blocks
    q_matches = list(re.finditer(r'\{\s*"id":\s*"([^"]+)",[\s\S]*?"questionHtml":\s*"((?:\\.|[^"\\])*)"', content))
    print(f"\nProcessing {name} ({fp}): found {len(q_matches)} questions")
    
    modified_count = 0
    new_content = content
    
    for m in q_matches:
        qid = m.group(1)
        old_qhtml = m.group(2)
        
        new_qhtml = rule(qid, old_qhtml)
        if new_qhtml and new_qhtml != old_qhtml:
            pattern = re.compile(rf'("id":\s*"{re.escape(qid)}",[\s\S]*?"questionHtml":\s*")' + re.escape(old_qhtml) + r'(")')
            match = pattern.search(new_content)
            if match:
                new_content = new_content[:match.start()] + match.group(1) + new_qhtml + match.group(2) + new_content[match.end():]
                modified_count += 1
            else:
                print(f"  [WARN] Failed to replace questionHtml for {qid}")

    print(f"-> Successfully transformed {modified_count} questions in {name}")
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("\nALL 6 LANGUAGES TRANSFORMED SUCCESSFULLY TO NATIVE IMMERSION PROMPTS!")
