# -*- coding: utf-8 -*-
with open(r"C:\Users\glixer\Downloads\tka-mastery-hub\app.js", "r", encoding="utf-8") as f:
    text = f.read()

import re
types = set(re.findall(r"type\s*===?\s*['\"]([^'\"]+)['\"]", text))
print("Types checked in app.js:", types)

pos_render = text.find("function renderQuestion")
if pos_render != -1:
    print("\nrenderQuestion function snippet:")
    print(text[pos_render:pos_render+1500])
