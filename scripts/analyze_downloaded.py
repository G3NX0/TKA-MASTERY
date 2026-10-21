# -*- coding: utf-8 -*-
import os
import re
from collections import Counter

download_dir = r"C:\Users\glixer\Downloads\tka-mastery-hub\data"

print("=== ANALYZING ALL DOWNLOADED QUESTION FILES ===")
summary = {}

for filename in os.listdir(download_dir):
    if filename.startswith("questions_") and filename.endswith(".js"):
        filepath = os.path.join(download_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        types = Counter(re.findall(r'"type":\s*"([^"]+)"', content))
        q_count = len(re.findall(r'"id":\s*"([^"]+)"', content))
        
        # Check options format: array or object
        has_options_array = '"options": [' in content
        has_options_dict = '"options": {' in content
        has_table_statements = 'tableStatements' in content
        has_table_rows = 'tableRows' in content
        
        # Check length of correct answer vs wrong options
        summary[filename] = {
            "total_questions": q_count,
            "types": dict(types),
            "options_array": has_options_array,
            "options_dict": has_options_dict,
            "tableStatements": has_table_statements,
            "tableRows": has_table_rows
        }

for k, v in summary.items():
    print(f"\n{k}:")
    print(f"  Count: {v['total_questions']}")
    print(f"  Types: {v['types']}")
    print(f"  Options format: array={v['options_array']}, dict={v['options_dict']}")
    print(f"  Table properties: tableStatements={v['tableStatements']}, tableRows={v['tableRows']}")
