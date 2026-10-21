# -*- coding: utf-8 -*-
with open(r"C:\Users\glixer\Downloads\tka-mastery-hub\data\questions_fisika.js", "r", encoding="utf-8") as f:
    text = f.read()

pos_table = text.find('"type": "complex_table"')
if pos_table != -1:
    start = text.rfind('{', 0, pos_table)
    end = text.find('},\n  {', pos_table)
    print("=== EXAMPLE COMPLEX_TABLE ===")
    print(text[start:end+1])

pos_multi = text.find('"type": "multiple_response"')
if pos_multi != -1:
    start = text.rfind('{', 0, pos_multi)
    end = text.find('},\n  {', pos_multi)
    print("\n=== EXAMPLE MULTIPLE_RESPONSE ===")
    print(text[start:end+1])
