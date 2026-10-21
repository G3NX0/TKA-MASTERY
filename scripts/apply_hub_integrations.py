"""
Script untuk mengintegrasikan Mapel Lanjutan ke dalam:
1. data/questions_db.js (update targetSubjectKey dan available di electiveCatalog)
2. index.html (tambahkan deck switcher dan update counter ke 810)
3. app.js (support renderHomeDeck untuk wajib & lanjut, event listener switcher, dan tombol buka elective)
"""
import re

# 1. Update questions_db.js
with open('data/questions_db.js', 'r', encoding='utf-8') as f:
    db_text = f.read()

# Update mtk-lanjut
db_text = db_text.replace(
    'id: "mtk-lanjut",\n      group: "MIPA / SAINTEK",\n      title: "Matematika Tingkat Lanjut",\n      badge: "Aljabar Tinggi & Vektor",\n      topics: "Polinomial & Teorema Sisa, Matriks Ordo Tinggi, Vektor 3D, Irisan Kerucut, Kalkulus Diferensial Lanjut",\n      targetCompetency: "Pembuktian analitis aljabar abstrak, transformasi spasial geometri analitik, dan dekomposisi fungsi kompleks.",\n      available: "Segera Hadir"',
    'id: "mtk-lanjut",\n      targetSubjectKey: "mtk_lanjut",\n      group: "MIPA / SAINTEK",\n      title: "Matematika Tingkat Lanjut",\n      badge: "Aljabar Tinggi & Vektor",\n      topics: "Polinomial & Teorema Sisa, Matriks Ordo Tinggi, Vektor 3D, Irisan Kerucut, Kalkulus Diferensial Lanjut",\n      targetCompetency: "Pembuktian analitis aljabar abstrak, transformasi spasial geometri analitik, dan dekomposisi fungsi kompleks.",\n      available: "135 Soal Siap"'
)

# Update indo-lanjut
db_text = db_text.replace(
    'id: "indo-lanjut",\n      group: "BAHASA & SASTRA",\n      title: "Bahasa & Sastra Indonesia Lanjut",\n      badge: "Stilistika & Semiotika",\n      topics: "Kritik Sastra Kontemporer, Analisis Semiotika Puisi/Prosa, Stilistika Retorika, Linguistik Korpus, Penulisan Akademik",\n      targetCompetency: "Dekonstruksi makna kias sastra, apresiasi estetika bahasa, dan sintesis argumen esai ilmiah formal.",\n      available: "Segera Hadir"',
    'id: "indo-lanjut",\n      targetSubjectKey: "ind_lanjut",\n      group: "BAHASA & SASTRA",\n      title: "Bahasa & Sastra Indonesia Lanjut",\n      badge: "Stilistika & Semiotika",\n      topics: "Kritik Sastra Kontemporer, Analisis Semiotika Puisi/Prosa, Stilistika Retorika, Linguistik Korpus, Penulisan Akademik",\n      targetCompetency: "Dekonstruksi makna kias sastra, apresiasi estetika bahasa, dan sintesis argumen esai ilmiah formal.",\n      available: "135 Soal Siap"'
)

# Update inggris-lanjut
db_text = db_text.replace(
    'id: "inggris-lanjut",\n      group: "BAHASA & SASTRA",\n      title: "Bahasa & Sastra Inggris Lanjut",\n      badge: "Discourse & Literary Prose",\n      topics: "Advanced Rhetorical Devices, Expository Prose Synthesis, Western Literary Heritage, Formal Debating, CEFR B2-C1",\n      targetCompetency: "Critical subtext deconstruction, evaluating stylistic nuance, and articulating cohesive counter-arguments.",\n      available: "Segera Hadir"',
    'id: "inggris-lanjut",\n      targetSubjectKey: "eng_lanjut",\n      group: "BAHASA & SASTRA",\n      title: "Bahasa & Sastra Inggris Lanjut",\n      badge: "Discourse & Literary Prose",\n      topics: "Advanced Rhetorical Devices, Expository Prose Synthesis, Western Literary Heritage, Formal Debating, CEFR B2-C1",\n      targetCompetency: "Critical subtext deconstruction, evaluating stylistic nuance, and articulating cohesive counter-arguments.",\n      available: "135 Soal Siap"'
)

with open('data/questions_db.js', 'w', encoding='utf-8') as f:
    f.write(db_text)
print("[1] questions_db.js updated with active elective linkage.")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add deck group switcher above panorama stage
old_stage = '<div class="panorama-stage-wrapper">'
new_stage = """<!-- Subject Category Filter Switcher -->
      <div class="deck-group-switcher" id="deckGroupSwitcher">
        <button class="btn-group-tab active" data-deck="wajib">Mapel Wajib (3 Mapel)</button>
        <button class="btn-group-tab" data-deck="lanjut">Mapel Lanjutan (3 Mapel)</button>
      </div>

      <!-- 3D Panorama Curved Stage for Subject Cards -->
      <div class="panorama-stage-wrapper">"""

if old_stage in html and 'id="deckGroupSwitcher"' not in html:
    html = html.replace(old_stage, new_stage)
    print("[2] index.html updated with deckGroupSwitcher.")

# Update total soal stat to 810
html = html.replace(
    '<span class="stat-number highlight-indigo" id="homeTotalSoalStat">405</span>',
    '<span class="stat-number highlight-indigo" id="homeTotalSoalStat">810</span>'
)
html = html.replace(
    '<span class="stat-caption">Total Bank Soal HOTS (3 Mapel)</span>',
    '<span class="stat-caption">Total Bank Soal HOTS (6 Mapel)</span>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("[3] index.html stats and markup updated.")
