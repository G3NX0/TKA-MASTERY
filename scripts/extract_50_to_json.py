import re
import json

with open('extracted_pplg_pdf.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove page header lines like "Halaman X dari 21Simulasi TKA PPLG/RPL SMK/MAK — 50 Soal Sesuai Kisi-Kisi Resmi"
text = re.sub(r'Halaman \d+ dari \d+Simulasi TKA PPLG/RPL SMK/MAK — 50 Soal Sesuai Kisi-Kisi Resmi', '', text)
text = re.sub(r'=== PAGE \d+ ===', '', text)

# Split by "Soal X — "
pattern = r'(Soal\s+(\d+)\s+—\s+Elemen\s+(\d+):\s+([^\n]+))'
matches = list(re.finditer(pattern, text))
print(f"Total question matches: {len(matches)}")

extracted = []
for i in range(len(matches)):
    start = matches[i].start()
    end = matches[i+1].start() if i+1 < len(matches) else len(text)
    q_text = text[start:end].strip()
    q_num = int(matches[i].group(2))
    elem_num = int(matches[i].group(3))
    header_info = matches[i].group(4).strip()
    
    extracted.append({
        "num": q_num,
        "elem_num": elem_num,
        "header_info": header_info,
        "raw_text": q_text
    })

print(f"Extracted count: {len(extracted)}")
with open('scripts/extracted_50_questions.json', 'w', encoding='utf-8') as f:
    json.dump(extracted, f, indent=2, ensure_ascii=False)
print("Saved to scripts/extracted_50_questions.json")
