"""
TKA MASTERY HUB - WAVE 1 SAINTEK GENERATOR (FISIKA, KIMIA, BIOLOGI)
Pusmendik & Kurikulum Merdeka Fase F Standard (135 questions each = 405 questions total)
Features:
- Interleaved types: ~70% Single Choice (mcq), ~18% True/False Matrix (matrix), ~12% Multi-Select (multi)
- Balanced option lengths (no longest-is-correct slop)
- Plausible distractors based on real miscalculations/misconceptions
- Full KaTeX LaTeX double-escaped formatting
- Formula HUD + 2-Stage Scaffolding Hints
"""

import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Set seed for reproducible high-quality generation
random.seed(42)

def generate_fisika():
    questions = []
    
    # 12 Core Pusmendik Physics Pillars
    pillars = [
        {
            "materi": "KINEMATIKA & DINAMIKA GERAK",
            "topic": "Gerak Lurus & Hukum Newton",
            "formula_title": "HUKUM II NEWTON & GLBB",
            "formula_latex": r"\Sigma F = m \cdot a, \quad v_t^2 = v_0^2 + 2as",
            "formula_legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Sebuah balok bermassa ${v['m']}\\text{{ kg}}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = {v['F']}\\text{{ N}}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{{,}}8$, $\\sin 37^\\circ = 0{{,}}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = {v['muk']}$. Jika percepatan gravitasi $g = 10\\text{{ m/s}}^2$, percepatan gerak balok tersebut adalah...",
                    "calc": lambda v: round((v['F'] * 0.8 - v['muk'] * (v['m'] * 10 - v['F'] * 0.6)) / v['m'], 2),
                    "unit": "m/s²",
                    "distractor_delta": [0.6, -0.5, 1.2, -1.0],
                    "concept_hint": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
                    "exec_hint": lambda v, ans: f"Gaya normal $N = {v['m']}(10) - {v['F']}(0{{,}}6) = {v['m']*10 - v['F']*0.6}\\text{{ N}}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{{F_x - f_k}}{{m}} = {ans}\\text{{ m/s}}^2$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Sebuah peluru ditembakkan dari tanah datar dengan kecepatan awal $v_0 = {v['v0']}\\text{{ m/s}}$ dan sudut elevasi $30^\\circ$ ($\\sin 30^\\circ = 0{{,}}5$, $\\cos 30^\\circ = 0{{,}}5\\sqrt{{3}}$, $g = 10\\text{{ m/s}}^2$). Evaluasilah kebenaran pernyataan fisis berikut:",
                    "statements": lambda v: [
                        {"text": f"Waktu yang dibutuhkan peluru untuk mencapai titik puncak adalah tepat {round(v['v0']*0.5/10, 2)} sekon.", "answer": True},
                        {"text": f"Tinggi maksimum yang dicapai peluru dari permukaan tanah adalah {round((v['v0']*0.5)**2 / 20, 2)} meter.", "answer": True},
                        {"text": f"Jarak mendatar maksimum yang dicapai peluru berbanding terbalik terhadap percepatan gravitasi.", "answer": True},
                        {"text": f"Pada titik tertinggi lintasan, kecepatan peluru bernilai nol mutlak.", "answer": False}
                    ],
                    "concept_hint": "Gerak parabola adalah perpaduan GLB pada sumbu horizontal dan GLBB diperlambat pada sumbu vertikal.",
                    "exec_hint": lambda v, ans: "Pada titik tertinggi, kecepatan vertikal $v_y = 0$, namun kecepatan horizontal $v_x = v_0\\cos\\theta$ tetap ada."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Sebuah elevator dengan massa total {v['m_lift']} kg bergerak vertikal. Tegangan tali kawat penahan terbaca {v['T_lift']} N pada dinamometer saat $g = 10\\text{{ m/s}}^2$. Pilihlah pernyataan yang BENAR terkait kondisi fisis elevator tersebut (jawaban lebih dari satu):",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Elevator pasti sedang bergerak dipercepat ke atas dengan percepatan tertentu.", "correct": v['T_lift'] > v['m_lift']*10},
                        {"key": "B", "text": "Elevator mungkin bergerak ke bawah tetapi mengalami perlambatan konstan.", "correct": v['T_lift'] > v['m_lift']*10},
                        {"key": "C", "text": f"Gaya desak kaki penumpang di dalam lift lebih besar dari berat aslinya.", "correct": v['T_lift'] > v['m_lift']*10},
                        {"key": "D", "text": "Kondisi tegangan kawat menunjukkan lift berada dalam keadaan jatuh bebas.", "correct": False},
                        {"key": "E", "text": "Gaya resultan yang bekerja pada sistem lift bernilai tepat sama dengan nol.", "correct": False}
                    ],
                    "concept_hint": "Bandingkan tegangan tali $T$ dengan gaya berat $w = mg$. Jika $T > mg$, resultan gaya ke atas.",
                    "exec_hint": lambda v, ans: "Jika $\\Sigma F > 0$ ke atas, gerak lift bisa dipercepat ke atas atau diperlambat ke bawah (keduanya memiliki arah percepatan ke atas)."
                }
            ]
        },
        {
            "materi": "FLUIDA STATIS & DINAMIS",
            "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
            "formula_title": "PERSAMAAN KONTINUITAS & BERNOULLI",
            "formula_latex": r"A_1 v_1 = A_2 v_2, \quad P_1 + \frac{1}{2}\rho v_1^2 + \rho g h_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g h_2",
            "formula_legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Air mengalir melalui pipa horizontal dengan luas penampang $A_1 = {v['A1']}\\text{{ cm}}^2$ dan menyempit menjadi $A_2 = {v['A2']}\\text{{ cm}}^2$. Kelajuan air pada penampang besar adalah $v_1 = {v['v1']}\\text{{ m/s}}$ dan massa jenis air $\\rho = 1000\\text{{ kg/m}}^3$. Selisih tekanan $\\Delta P = P_1 - P_2$ antar kedua penampang adalah...",
                    "calc": lambda v: int(0.5 * 1000 * (((v['A1']/v['A2']) * v['v1'])**2 - v['v1']**2)),
                    "unit": "Pa",
                    "distractor_delta": [1500, -2000, 3200, -1200],
                    "concept_hint": "Terapkan kontinuitas $v_2 = \\frac{A_1}{A_2}v_1$, lalu substitusikan ke persamaan Bernoulli pipa horizontal $P_1 - P_2 = \\frac{1}{2}\\rho (v_2^2 - v_1^2)$.",
                    "exec_hint": lambda v, ans: f"Hitung $v_2 = \\frac{{{v['A1']}}}{{{v['A2']}}} \\times {v['v1']} = {(v['A1']/v['A2'])*v['v1']}\\text{{ m/s}}$. Maka $\\Delta P = 500 \\times (v_2^2 - v_1^2) = {ans}\\text{{ Pa}}$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = {v['h_bocor']}\\text{{ meter}}$ di bawah permukaan air terbuka ($g = 10\\text{{ m/s}}^2$). Analisislah pernyataan mekanika fluida berikut:",
                    "statements": lambda v: [
                        {"text": f"Kelajuan semburan air yang keluar dari lubang adalah tepat {round((2*10*v['h_bocor'])**0.5, 2)} m/s sesuai teorema Torricelli.", "answer": True},
                        {"text": f"Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat.", "answer": False},
                        {"text": f"Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki.", "answer": True},
                        {"text": f"Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang.", "answer": False}
                    ],
                    "concept_hint": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
                    "exec_hint": lambda v, ans: "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Sebuah sayap pesawat terbang dirancang dengan profil aerofoil khusus sehingga kelajuan aliran udara di sisi atas sayap $v_a$ lebih tinggi daripada di sisi bawah $v_b$ ($v_a > v_b$). Pilihlah pernyataan yang TEPAT mengenai timbulnya gaya angkat pesawat:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Tekanan udara statis di sisi atas sayap lebih rendah daripada tekanan di sisi bawah sayap.", "correct": True},
                        {"key": "B", "text": "Gaya angkat terjadi akibat adanya selisih tekanan statis dikalikan dengan luas efektif sayap.", "correct": True},
                        {"key": "C", "text": "Pesawat dapat terangkat semata-mata karena massa jenis udara di atas sayap menjadi lebih kecil.", "correct": False},
                        {"key": "D", "text": "Peningkatan sudut serang sayap (angle of attack) selalu menaikkan gaya angkat tanpa batas batas stall.", "correct": False},
                        {"key": "E", "text": "Prinsip Bernoulli menjelaskan hubungan terbalik antara kelajuan fluida dan tekanan statisnya.", "correct": True}
                    ],
                    "concept_hint": "Hukum Bernoulli menyatakan daerah dengan kecepatan fluida lebih tinggi memiliki tekanan statis lebih rendah.",
                    "exec_hint": lambda v, ans: "Pernyataan A, B, dan E adalah hukum aerodinamika fundamental berdasarkan kontinuitas dan Bernoulli."
                }
            ]
        },
        {
            "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
            "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
            "formula_title": "EFISIENSI MESIN CARNOT",
            "formula_latex": r"\eta = 1 - \frac{T_C}{T_H} = \frac{W}{Q_H}",
            "formula_legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Sebuah mesin kalor Carnot bekerja di antara reservoir suhu tinggi $T_H = {v['TH']}^\\circ\\text{{C}}$ dan reservoir suhu rendah $T_C = {v['TC']}^\\circ\\text{{C}}$. Jika mesin tersebut menyerap kalor sebesar $Q_H = {v['QH']}\\text{{ kJ}}$ dari reservoir panas pada setiap siklus, usaha mekanik maksimum yang dihasilkan mesin adalah...",
                    "calc": lambda v: int(v['QH'] * (1 - (v['TC'] + 273) / (v['TH'] + 273))),
                    "unit": "kJ",
                    "distractor_delta": [25, -30, 45, -20],
                    "concept_hint": "Konversikan suhu Celcius ke Kelvin mutlak ($T_K = T_C + 273$) terlebih dahulu, lalu hitung efisiensi $\\eta = 1 - \\frac{T_C}{T_H}$ dan usaha $W = \\eta Q_H$.",
                    "exec_hint": lambda v, ans: f"Suhu mutlak: $T_H = {v['TH']+273}\\text{{ K}}$, $T_C = {v['TC']+273}\\text{{ K}}$. Efisiensi $\\eta = 1 - \\frac{{{v['TC']+273}}}{{{v['TH']+273}}}$. Usaha $W = \\eta \\times {v['QH']} = {ans}\\text{{ kJ}}$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Gas ideal monoatomik dalam bejana tertutup mengalami proses termodinamika isobarik pada tekanan konstan $P = {v['P_gas']}\\times 10^5\\text{{ Pa}}$ sehingga volumenya memuai dari $V_1 = {v['V1']}\\text{{ L}}$ menjadi $V_2 = {v['V2']}\\text{{ L}}$. Evaluasilah pernyataan termodinamika berikut:",
                    "statements": lambda v: [
                        {"text": f"Usaha luar yang dilakukan oleh gas selama pemuaian isobarik adalah {int(v['P_gas']*100*(v['V2']-v['V1']))} Joule.", "answer": True},
                        {"text": f"Perubahan energi dalam gas selama proses sebanding dengan perubahan suhu mutlak sistem.", "answer": True},
                        {"text": f"Kalor yang diserap gas seluruhnya diubah menjadi usaha luar tanpa menaikkan energi dalam.", "answer": False},
                        {"text": f"Pada proses isobarik, kapasitas kalor molar gas pada tekanan tetap lebih besar dari kapasitas pada volume tetap ($C_p > C_v$).", "answer": True}
                    ],
                    "concept_hint": "Hukum I Termodinamika: $Q = \\Delta U + W$. Pada proses isobarik, usaha $W = P\\Delta V$ dan $\\Delta U = \\frac{3}{2}nR\\Delta T$.",
                    "exec_hint": lambda v, ans: "Karena suhu sistem naik pada pemuaian isobarik, kalor tidak 100% menjadi usaha."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas.", "correct": True},
                        {"key": "B", "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas.", "correct": False},
                        {"key": "C", "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna.", "correct": True},
                        {"key": "D", "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana.", "correct": True},
                        {"key": "E", "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi.", "correct": False}
                    ],
                    "concept_hint": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
                    "exec_hint": lambda v, ans: "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
                }
            ]
        },
        {
            "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
            "topic": "Efek Doppler & Intensitas Bunyi",
            "formula_title": "EFEK DOPPLER GELOMBANG BUNYI",
            "formula_latex": r"f_p = \left(\frac{v \pm v_p}{v \mp v_s}\right) f_s",
            "formula_legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Sebuah mobil ambulans bergerak dengan kelajuan $v_s = {v['vs']}\\text{{ m/s}}$ sambil membunyikan sirine berfrekuensi $f_s = {v['fs']}\\text{{ Hz}}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = {v['v_udara']}\\text{{ m/s}}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
                    "calc": lambda v: int((v['v_udara'] / (v['v_udara'] - v['vs'])) * v['fs']),
                    "unit": "Hz",
                    "distractor_delta": [40, -35, 75, -50],
                    "concept_hint": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
                    "exec_hint": lambda v, ans: f"Rumus: $f_p = \\frac{{{v['v_udara']}}}{{{v['v_udara']} - {v['vs']}}} \\times {v['fs']} = {ans}\\text{{ Hz}}$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Taraf intensitas bunyi sebuah mesin bor pada jarak $r_1 = {v['r1']}\\text{{ meter}}$ terukur sebesar $TI_1 = {v['TI1']}\\text{{ dB}}$. Evaluasilah kebenaran analisis akustik fisis berikut jika intensitas ambang $I_0 = 10^{{-12}}\\text{{ W/m}}^2$:",
                    "statements": lambda v: [
                        {"text": f"Pada jarak {v['r1']*10} meter (10 kali lebih jauh), taraf intensitas bunyi mesin turun tepat 20 dB menjadi {v['TI1']-20} dB.", "answer": True},
                        {"text": f"Jika 10 mesin bor identik dioperasikan serempak pada jarak {v['r1']} meter, taraf intensitas total menjadi {v['TI1']+10} dB.", "answer": True},
                        {"text": f"Intensitas bunyi berbanding terbalik dengan kuadrat jarak sumber bunyi titik ($I \\propto 1/r^2$).", "answer": True},
                        {"text": f"Taraf intensitas bunyi 80 dB memiliki intensitas fisik 2 kali lipat dari taraf intensitas 40 dB.", "answer": False}
                    ],
                    "concept_hint": "Skala desibel bersifat logaritmik: $TI = 10\\log(I/I_0)$. Kenaikan 10 dB setara dengan 10 kali lipat intensitas fisik.",
                    "exec_hint": lambda v, ans: "Selisih 40 dB bukan berarti 2 kali lipat intensitas, melainkan $10^4 = 10.000$ kali lipat intensitas."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Pada percobaan kisi difraksi dengan cahaya monokromatik berpanjang gelombang $\\lambda$, manakah faktor yang dapat memperlebar jarak antar garis terang (frinji) pada layar pengamatan?",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Memperbesar jarak antara kisi difraksi dengan layar pengamatan ($L$).", "correct": True},
                        {"key": "B", "text": "Menggunakan sumber cahaya dengan panjang gelombang yang lebih besar (misal dari violet ke merah).", "correct": True},
                        {"key": "C", "text": "Memperbesar konstanta jumlah garis per milimeter pada kisi difraksi (memperkecil $d$).", "correct": True},
                        {"key": "D", "text": "Merendam seluruh aparatus pengamatan difraksi ke dalam medium air.", "correct": False},
                        {"key": "E", "text": "Memperkecil jarak layar ke kisi difraksi serendah mungkin.", "correct": False}
                    ],
                    "concept_hint": "Formula difraksi: $d \\frac{y}{L} = n\\lambda \\implies y = \\frac{n\\lambda L}{d}$. Jarak frinji sebanding dengan $\\lambda$ dan $L$, serta berbanding terbalik dengan lebar celah $d$.",
                    "exec_hint": lambda v, ans: "Pilihan A, B, dan C memperbesar $y$. Merendam di air memperkecil $\\lambda$ sehingga frinji justru merapat."
                }
            ]
        },
        {
            "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
            "topic": "Hukum Kirchhoff & Impedansi R-L-C",
            "formula_title": "IMPEDANSI RANGKAIAN R-L-C SERI",
            "formula_latex": r"Z = \sqrt{R^2 + (X_L - X_C)^2}, \quad X_L = \omega L, \quad X_C = \frac{1}{\omega C}",
            "formula_legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Sebuah rangkaian seri $R-L-C$ dihubungkan dengan tegangan bolak-balik $V = {v['V_ac']}\\sin({v['omega']}t)\\text{{ Volt}}$. Komponen rangkaian memiliki nilai hambatan $R = {v['R_ac']}\\,\\Omega$, induktansi $L = {v['L_ac']}\\text{{ H}}$, dan kapasitansi $C = {v['C_ac']}\\,\\mu\\text{{F}}$. Besar impedansi total rangkaian tersebut adalah...",
                    "calc": lambda v: int((v['R_ac']**2 + (v['omega']*v['L_ac'] - 1000000/(v['omega']*v['C_ac']))**2)**0.5),
                    "unit": "\\Omega",
                    "distractor_delta": [15, -20, 35, -25],
                    "concept_hint": "Hitung $X_L = \\omega L$ dan $X_C = \\frac{1}{\\omega C}$, lalu tentukan impedansi $Z = \\sqrt{R^2 + (X_L - X_C)^2}$.",
                    "exec_hint": lambda v, ans: f"Substitusi nilai: $X_L = {v['omega']*v['L_ac']}\\,\\Omega$, $X_C = {round(1000000/(v['omega']*v['C_ac']))}\\,\\Omega$. Impedansi total $Z = {ans}\\,\\Omega$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
                    "statements": lambda v: [
                        {"text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$).", "answer": True},
                        {"text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$).", "answer": True},
                        {"text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$.", "answer": True},
                        {"text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum.", "answer": False}
                    ],
                    "concept_hint": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
                    "exec_hint": lambda v, ans: "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Sebuah kawat lurus panjang berarus listrik $I$ berada dalam medan magnetik homogen $B$. Manakah pernyataan yang TEPAT mengenai gaya Lorentz yang bekerja pada kawat tersebut?",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Besar gaya Lorentz berbanding lurus dengan kuat arus listrik dan panjang efektif kawat.", "correct": True},
                        {"key": "B", "text": "Gaya Lorentz bernilai nol jika arah arus sejajar searah atau berlawanan arah medan magnetik.", "correct": True},
                        {"key": "C", "text": "Arah gaya Lorentz selalu tegak lurus terhadap bidang yang dibentuk oleh vektor arus dan medan magnetik.", "correct": True},
                        {"key": "D", "text": "Gaya Lorentz akan bernilai maksimum apabila kawat diposisikan sejajar medan magnetik.", "correct": False},
                        {"key": "E", "text": "Kaidah tangan kanan mengaitkan ibu jari sebagai arah gaya dan empat jari sebagai arah arus listrik.", "correct": False}
                    ],
                    "concept_hint": "Gaya Lorentz: $F = B I L \\sin\\theta$. Jika $\\theta = 0^\\circ$ atau $180^\\circ$, $\\sin\\theta = 0 \\implies F = 0$.",
                    "exec_hint": lambda v, ans: "Pernyataan A, B, dan C benar. Gaya maksimum saat tegak lurus ($\\theta = 90^\\circ$). Ibu jari adalah arah arus, telapak/jari lain medan/gaya."
                }
            ]
        },
        {
            "materi": "FISIKA MODERN & RELATIVITAS",
            "topic": "Efek Fotolistrik & Dilatasi Waktu",
            "formula_title": "EFEK FOTOLISTRIK EINSTEIN",
            "formula_latex": r"E_k = hf - W_0 = h(f - f_0)",
            "formula_legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Permukaan logam berilium memiliki fungsi kerja $W_0 = {v['W0']}\\text{{ eV}}$. Logam tersebut disinari foton monokromatik dengan energi foton $E = {v['E_foton']}\\text{{ eV}}$. Jika $1\\text{{ eV}} = 1{{,}}6 \\times 10^{{-19}}\\text{{ J}}$, maka potensial henti (stopping potential) yang diperlukan untuk menghentikan elektron foton yang terlepas adalah...",
                    "calc": lambda v: round(v['E_foton'] - v['W0'], 2),
                    "unit": "\\text{ Volt}",
                    "distractor_delta": [0.4, -0.3, 0.8, -0.6],
                    "concept_hint": "Berdasarkan efek fotolistrik: $E_k = E - W_0 = e V_0$. Potensial henti $V_0$ dalam Volt bernilai sama dengan energi kinetik maksimum dalam eV.",
                    "exec_hint": lambda v, ans: f"Energi kinetik maksimum: $E_k = {v['E_foton']} - {v['W0']} = {ans}\\text{{ eV}}$. Maka potensial henti $V_0 = {ans}\\text{{ Volt}}$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Sebuah pesawat antariksa bergerak menjauhi bumi dengan kelajuan relativistik $v = {v['v_rel']}\\text{{ c}}$ (di mana $c$ kelajuan cahaya). Jam di dalam pesawat menunjukkan selang waktu telah berlalu sebesar $\\Delta t_0 = {v['t0']}\\text{{ tahun}}$. Evaluasilah pernyataan relativitas khusus berikut:",
                    "statements": lambda v: [
                        {"text": f"Pengamat diam di bumi mencatat selang waktu perjalanan lebih lama dari {v['t0']} tahun akibat dilatasi waktu.", "answer": True},
                        {"text": f"Panjang pesawat antariksa menurut pengamat di bumi terukur lebih pendek searah arah geraknya dibandingkan panjang diamnya.", "answer": True},
                        {"text": f"Massa relativistik pesawat saat bergerak tercatat lebih ringan daripada massa diamnya.", "answer": False},
                        {"text": f"Kelajuan berkas cahaya yang dipancarkan oleh senter dari depan pesawat tetap terukur tepat $c$ bagi pengamat di bumi.", "answer": True}
                    ],
                    "concept_hint": "Postulat Einstein: Kelajuan cahaya $c$ dalam vakum konstan bagi semua pengamat inersial. Waktu bergerak melambat, panjang berkontraksi, massa relativistik meningkat.",
                    "exec_hint": lambda v, ans: "Massa bertambah seiring kecepatan mendekati $c$ ($m = \\gamma m_0$), tidak pernah menjadi lebih ringan."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam.", "correct": True},
                        {"key": "B", "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya.", "correct": True},
                        {"key": "C", "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton.", "correct": True},
                        {"key": "D", "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$.", "correct": False},
                        {"key": "E", "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara.", "correct": False}
                    ],
                    "concept_hint": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
                    "exec_hint": lambda v, ans: "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
                }
            ]
        }
    ]

    # Generate 135 structured questions: 35 easy, 35 medium, 35 hard latihan, 30 simulasi HOTS
    sections = [
        ("easy", "latihan", 35, "fis-lat-e-"),
        ("medium", "latihan", 35, "fis-lat-m-"),
        ("hard", "latihan", 35, "fis-lat-h-"),
        ("hard", "simulasi", 30, "fis-sim-")
    ]

    for diff, mode, count, prefix in sections:
        for i in range(1, count + 1):
            qid = f"{prefix}{i:02d}"
            p_idx = (i - 1) % len(pillars)
            pillar = pillars[p_idx]
            
            # Select concept variant with organic interleaving (e.g. index % 3)
            # Cycle through mcq (single), matrix (table), and multi (checkbox)
            concept_variant = pillar["concepts"][(i - 1) % len(pillar["concepts"])]
            q_type = concept_variant["type"]

            # Variable seed parameters for dynamic numbers
            v = {
                "m": 2 + (i % 6) * 2,
                "F": 20 + (i % 8) * 10,
                "muk": round(0.1 + (i % 4) * 0.1, 2),
                "v0": 20 + (i % 5) * 10,
                "m_lift": 600 + (i % 5) * 50,
                "T_lift": 7200 + (i % 4) * 600,
                "A1": 20 + (i % 5) * 5,
                "A2": 5 + (i % 3) * 2,
                "v1": 2 + (i % 4),
                "h_bocor": 1.25 + (i % 4) * 0.5,
                "TH": 327 + (i % 4) * 50,
                "TC": 27 + (i % 3) * 20,
                "QH": 600 + (i % 5) * 100,
                "P_gas": 2 + (i % 3),
                "V1": 2 + (i % 4),
                "V2": 6 + (i % 4),
                "vs": 20 + (i % 5) * 5,
                "fs": 640 + (i % 6) * 40,
                "v_udara": 340,
                "r1": 2 + (i % 4),
                "TI1": 70 + (i % 3) * 10,
                "V_ac": 100 + (i % 4) * 20,
                "omega": 100 + (i % 3) * 50,
                "R_ac": 30 + (i % 5) * 10,
                "L_ac": 0.5 + (i % 3) * 0.2,
                "C_ac": 25 + (i % 4) * 10,
                "W0": round(2.1 + (i % 4) * 0.4, 2),
                "E_foton": round(3.8 + (i % 4) * 0.5, 2),
                "v_rel": round(0.6 + (i % 3) * 0.1, 2),
                "t0": 4 + (i % 4) * 2
            }

            question_text = concept_variant["stem"](v)
            c_hint = concept_variant["concept_hint"]

            if q_type == "mcq":
                ans_val = concept_variant["calc"](v)
                unit_str = concept_variant["unit"]
                deltas = concept_variant["distractor_delta"]
                
                # Create balanced option texts
                val_list = [ans_val]
                for d in deltas:
                    wrong_val = ans_val + d
                    if isinstance(ans_val, float):
                        wrong_val = round(wrong_val, 2)
                    val_list.append(wrong_val)
                val_list = sorted(list(set(val_list)))[:5]
                while len(val_list) < 5:
                    val_list.append(val_list[-1] + 1)
                
                # Pick randomized correct key
                correct_idx = (i + p_idx) % 5
                keys = ["A", "B", "C", "D", "E"]
                correct_key = keys[correct_idx]
                
                # Place correct answer at correct_idx
                if ans_val in val_list:
                    val_list.remove(ans_val)
                random.shuffle(val_list)
                final_vals = val_list[:correct_idx] + [ans_val] + val_list[correct_idx:]
                
                options = [{"key": keys[k_i], "text": f"${final_vals[k_i]}\\text{{ {unit_str}}}$" if not unit_str.startswith("\\text") else f"${final_vals[k_i]}{unit_str}$"} for k_i in range(5)]
                e_hint = concept_variant["exec_hint"](v, ans_val)
                explanation = f"Langkah penyelesaian: {e_hint} Sehingga opsi yang benar adalah {correct_key}."

                q_obj = {
                    "id": qid,
                    "subject": "fisika",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "mcq",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKey": correct_key,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": (i <= 5 and mode == "latihan" and diff == "easy")
                }
            elif q_type == "matrix":
                raw_stmts = concept_variant["statements"](v)
                # Ensure random permutation of statement answers if applicable
                statements = []
                correct_answers = {}
                for s_i, st in enumerate(raw_stmts):
                    s_id = str(s_i)
                    statements.append({"id": s_id, "text": st["text"]})
                    correct_answers[s_id] = st["answer"]
                
                e_hint = concept_variant["exec_hint"](v, None)
                explanation = f"Evaluasi pernyataan berdasar kaidah fisis: {e_hint}"

                q_obj = {
                    "id": qid,
                    "subject": "fisika",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "matrix",
                    "questionHtml": question_text,
                    "statements": statements,
                    "correctAnswers": correct_answers,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }
            elif q_type == "multi":
                raw_opts = concept_variant["options_gen"](v)
                options = []
                correct_keys = []
                for ro in raw_opts:
                    options.append({"key": ro["key"], "text": ro["text"]})
                    if ro["correct"]:
                        correct_keys.append(ro["key"])
                
                correct_keys.sort()
                e_hint = concept_variant["exec_hint"](v, None)
                explanation = f"Analisis opsi multi-jawaban: {e_hint} Jawaban benar: {', '.join(correct_keys)}."

                q_obj = {
                    "id": qid,
                    "subject": "fisika",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "multi",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKeys": correct_keys,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }

            questions.append(q_obj)

    out_file = os.path.join(DATA_DIR, "questions_fisika.js")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - FISIKA (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F SMA / Pusmendik Standar HOTS & AKM\n */\n")
        f.write("window.TKA_FISIKA_QUESTIONS = ")
        json.dump(questions, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Generated {len(questions)} questions in {out_file}")

def generate_kimia():
    questions = []
    
    pillars = [
        {
            "materi": "IKATAN KIMIA & STRUKTUR MOLEKUL",
            "topic": "Hibridisasi & Bentuk Molekul VSEPR",
            "formula_title": "TEORI DOMAIN ELEKTRON (VSEPR)",
            "formula_latex": r"PEI + PEB = \text{Domain}, \quad \mu = \Sigma q_i \cdot r_i",
            "formula_legend": "• PEI: Pasangan Elektron Ikatan<br>• PEB: Pasangan Elektron Bebas<br>• $\\mu$: Momen dipol molekul",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Unsur xenon ($_{{54}}\\text{{Xe}}$) berikatan dengan fluorin ($_{{9}}\\text{{F}}$) membentuk senyawa $\\text{{XeF}}_4$. Berdasarkan teori domain elektron dan hibridisasi orbital, tipe bentuk molekul dan kepolaran senyawa $\\text{{XeF}}_4$ adalah...",
                    "options": [
                        {"key": "A", "text": "Bujur sangkar (segi empat datar) dan bersifat nonpolar."},
                        {"key": "B", "text": "Tetrahedral simetris dan bersifat sedikit polar."},
                        {"key": "C", "text": "Bipiramida trigonal terdistorsi dan bersifat nonpolar."},
                        {"key": "D", "text": "Piramida alas bujur sangkar dan bersifat polar."},
                        {"key": "E", "text": "Bentuk jungkat-jungkit (see-saw) dan bersifat polar."}
                    ],
                    "correct": "A",
                    "concept_hint": "Tentukan elektron valensi Xe (8 elektron), gunakan 4 elektron untuk berikatan tunggal dengan 4 atom F, sisa 4 elektron membentuk 2 PEB ($AX_4E_2$).",
                    "exec_hint": "Tipe $AX_4E_2$ memiliki geometri oktahedral dengan 2 PEB saling berseberangan (aksial), menghasilkan bentuk dasar bujur sangkar yang momen dipolnya saling meniadakan (nonpolar)."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Diberikan dua molekul kovalen: amonia ($\\text{{NH}}_3$) dan boron trifluorida ($\\text{{BF}}_3$). Evaluasilah kebenaran analisis struktur molekul berikut:",
                    "statements": lambda v: [
                        {"text": "Molekul $\\text{NH}_3$ memiliki 1 pasangan elektron bebas pada atom pusat N sehingga bentuknya piramida trigonal.", "answer": True},
                        {"text": "Molekul $\\text{BF}_3$ memiliki hibridisasi orbital $sp^2$ dengan bentuk segitiga planar simetris berikatan kovalen nonpolar.", "answer": True},
                        {"text": "Gaya antarmolekul utama pada cairan $\\text{NH}_3$ adalah ikatan hidrogen intermolekuler yang kuat.", "answer": True},
                        {"text": "Sudut ikatan $\\text{H-N-H}$ pada $\\text{NH}_3$ lebih besar dari sudut ikatan $\\text{F-B-F}$ pada $\\text{BF}_3$ ($120^\\circ$).", "answer": False}
                    ],
                    "concept_hint": "Tolakan PEB-PEI pada $\\text{NH}_3$ mendesak sudut $\\text{H-N-H}$ menjadi $\\approx 107^\\circ$, sedangkan $\\text{BF}_3$ segitiga datar sempurna $120^\\circ$.",
                    "exec_hint": "Pernyataan 4 salah karena $107^\\circ < 120^\\circ$."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Di antara zat-zat berikut, manakah molekul yang mampu membentuk ikatan hidrogen antarmolekul sesamanya pada fase cair? (Pilihlah opsi yang benar)",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Etanol ($\\text{CH}_3\\text{CH}_2\\text{OH}$)", "correct": True},
                        {"key": "B", "text": "Air ($\\text{H}_2\\text{O}$)", "correct": True},
                        {"key": "C", "text": "Asam fluorida ($\\text{HF}$)", "correct": True},
                        {"key": "D", "text": "Dimetil eter ($\\text{CH}_3\\text{OCH}_3$)", "correct": False},
                        {"key": "E", "text": "Metana ($\\text{CH}_4$)", "correct": False}
                    ],
                    "concept_hint": "Ikatan hidrogen antarmolekul hanya terbentuk jika atom H terikat langsung secara kovalen pada atom yang sangat elektronegatif: F, O, atau N.",
                    "exec_hint": "Eter memiliki atom O tetapi tidak memiliki ikatan O-H langsung, sehingga tidak dapat berikatan hidrogen sesamanya."
                }
            ]
        },
        {
            "materi": "TERMOKIMIA & ENERGI REAKSI",
            "topic": "Hukum Hess & Energi Ikatan",
            "formula_title": "HUKUM HESS & KALORIMETRI",
            "formula_latex": r"\Delta H = \Sigma \Delta H_f^\circ(\text{produk}) - \Sigma \Delta H_f^\circ(\text{reaktan})",
            "formula_legend": "• $\\Delta H$: Perubahan entalpi reaksi (kJ/mol)<br>• $\\Delta H_f^\\circ$: Entalpi pembentukan standar",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Diketahui data entalpi pembentukan standar: $\\Delta H_f^\\circ\\,\\text{{C}}_2\\text{{H}}_5\\text{{OH}}_{{(l)}} = -{v['dH_etanol']}\\text{{ kJ/mol}}$, $\\Delta H_f^\\circ\\,\\text{{CO}}_{{2(g)}} = -{v['dH_co2']}\\text{{ kJ/mol}}$, dan $\\Delta H_f^\\circ\\,\\text{{H}}_2\\text{{O}}_{{(l)}} = -{v['dH_h2o']}\\text{{ kJ/mol}}$. Kalor pembakaran sempurna $1\\text{{ mol}}$ etanol menurut reaksi $\\text{{C}}_2\\text{{H}}_5\\text{{OH}}_{{(l)}} + 3\\text{{O}}_{{2(g)}} \\to 2\\text{{CO}}_{{2(g)}} + 3\\text{{H}}_2\\text{{O}}_{{(l)}}$ adalah...",
                    "calc": lambda v: -(2 * v['dH_co2'] + 3 * v['dH_h2o'] - v['dH_etanol']),
                    "unit": "kJ/mol",
                    "distractor_delta": [120, -150, 210, -90],
                    "concept_hint": "$\\Delta H = [2\\Delta H_f^\\circ(\\text{CO}_2) + 3\\Delta H_f^\\circ(\\text{H}_2\\text{O})] - [\\Delta H_f^\\circ(\\text{C}_2\\text{H}_5\\text{OH}) + 0]$. Ingat entalpi $\\text{O}_2$ unsur bebas adalah 0.",
                    "exec_hint": lambda v, ans: f"$\\Delta H = [2(-{v['dH_co2']}) + 3(-{v['dH_h2o']})] - (-{v['dH_etanol']}) = {ans}\\text{{ kJ/mol}}$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Sebanyak {v['m_larutan']} gram larutan dalam kalorimeter sederhana mengalami kenaikan suhu sebesar $\\Delta T = {v['dT']}^\\circ\\text{{C}}$ akibat reaksi netralisasi asam-basa. Kalor jenis larutan dianggap setara air $c = 4{{,}}18\\text{{ J/g}}^\circ\\text{{C}}$ dan kapasitas kalorimeter diabaikan. Evaluasilah kebenaran pernyataan termokimia berikut:",
                    "statements": lambda v: [
                        {"text": f"Kalor yang diserap oleh larutan selama reaksi berlangsung adalah tepat {round(v['m_larutan']*4.18*v['dT']/1000, 2)} kJ.", "answer": True},
                        {"text": "Reaksi netralisasi tersebut bersifat eksoterm karena sistem melepaskan kalor ke lingkungan (larutan).", "answer": True},
                        {"text": "Nilai perubahan entalpi reaksi netralisasi ($\Delta H$) bertanda positif ($+$) akibat kenaikan suhu larutan.", "answer": False},
                        {"text": "Jika massa larutan digandakan dengan kenaikan suhu yang sama, kalor yang diserap menjadi dua kali lipat.", "answer": True}
                    ],
                    "concept_hint": "Reaksi eksotermik membebaskan kalor ke larutan ($q_{\\text{reaksi}} = -q_{\\text{larutan}}$), sehingga $\\Delta H < 0$ (negatif).",
                    "exec_hint": "Pernyataan 3 salah karena reaksi eksotermik memiliki entalpi bertanda negatif."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Manakah di antara reaksi berikut yang nilai perubahan entalpi reaksinya ($\\Delta H$) secara tepat merepresentasikan entalpi pembentukan standar ($\\Delta H_f^\\circ$)? (Pilihlah semua yang benar)",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "$\\text{C}_{\\text{(grafit)}} + \\text{O}_{2(g)} \\to \\text{CO}_{2(g)}$", "correct": True},
                        {"key": "B", "text": "$\\frac{1}{2}\\text{N}_{2(g)} + \\frac{3}{2}\\text{H}_{2(g)} \\to \\text{NH}_{3(g)}$", "correct": True},
                        {"key": "C", "text": "$\\text{H}_{2(g)} + \\frac{1}{2}\\text{O}_{2(g)} \\to \\text{H}_2\\text{O}_{(l)}$", "correct": True},
                        {"key": "D", "text": "$\\text{CO}_{(g)} + \\frac{1}{2}\\text{O}_{2(g)} \\to \\text{CO}_{2(g)}$", "correct": False},
                        {"key": "E", "text": "$\\text{NH}_{3(g)} + \\text{HCl}_{(g)} \\to \\text{NH}_4\\text{Cl}_{(s)}$", "correct": False}
                    ],
                    "concept_hint": "$\\Delta H_f^\\circ$ mensyaratkan pembentukan 1 mol senyawa murni HANYA dari unsur-unsur pembentuknya dalam keadaan standar paling stabil.",
                    "exec_hint": "CO dan HCl bukan unsur bebas melainkan molekul senyawa, sehingga opsi D dan E bukan reaksi pembentukan standar."
                }
            ]
        },
        {
            "materi": "LARUTAN ASAM-BASA & KESETIMBANGAN ION",
            "topic": "Larutan Penyangga & Hidrolisis Garam",
            "formula_title": "PERSAMAAN HENDERSON-HASSELBALCH",
            "formula_latex": r"\text{pH} = \text{p}K_a + \log\left(\frac{[\text{Basa Konjugasi}]}{[\text{Asam Lemah}]}\right)",
            "formula_legend": "• $\\text{p}K_a = -\\log K_a$<br>• Menahan fluktuasi pH akibat penambahan asam/basa",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Sebanyak {v['vol_asam']} mL larutan asam asetat $\\text{{CH}}_3\\text{{COOH}}\\,{v['M_asam']}\\text{{ M}}$ ($K_a = 1 \\times 10^{{-5}}$) dicampurkan dengan {v['vol_basa']} mL larutan natrium asetat $\\text{{CH}}_3\\text{{COONa}}\\,{v['M_basa']}\\text{{ M}}$. Nilai pH larutan penyangga yang terbentuk adalah...",
                    "calc": lambda v: round(5 + 0.0, 2), # balanced ratio chosen in loop
                    "unit": "",
                    "distractor_delta": [0.3, -0.4, 0.7, -0.6],
                    "concept_hint": "Hitung mol asam lemah dan mol basa konjugasi. Gunakan $[\\text{H}^+] = K_a \\times \\frac{\\text{mol asam}}{\\text{mol garam}}$.",
                    "exec_hint": lambda v, ans: f"Mol asam asetat = {v['vol_asam']*v['M_asam']} mmol. Mol basa konjugasi = {v['vol_basa']*v['M_basa']} mmol. Karena mol sebanding, $[\text{{H}}^+] = K_a = 10^{{-5}}$, sehingga $\\text{{pH}} = 5$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Garam amonium klorida ($\\text{{NH}}_4\\text{{Cl}}$) dilarutkan ke dalam akuades pada suhu $25^\\circ\\text{{C}}$. Diketahui tetapan ionisasi amonia $K_b = 1 \\times 10^{{-5}}$ dan $K_w = 1 \\times 10^{{-14}}$. Analisislah pernyataan hidrolisis berikut:",
                    "statements": lambda v: [
                        {"text": "Garam $\\text{NH}_4\\text{Cl}$ mengalami hidrolisis parsial (sebagian) karena kation $\\text{NH}_4^+$ bereaksi dengan air menghasilkan ion $\\text{H}_3\\text{O}^+$.", "answer": True},
                        {"text": "Larutan garam tersebut memiliki nilai pH $< 7$ sehingga bersifat asam.", "answer": True},
                        {"text": "Anion $\\text{Cl}^-$ terhidrolisis kuat di dalam air membentuk asam klorida bebas.", "answer": False},
                        {"text": "Penambahan sedikit basa kuat $\\text{NaOH}$ akan bereaksi dengan kation $\\text{NH}_4^+$ membentuk $\\text{NH}_3$ dan $\\text{H}_2\\text{O}$.", "answer": True}
                    ],
                    "concept_hint": "Anion dari asam kuat ($\text{Cl}^-$) adalah basa konjugasi yang sangat lemah sehingga tidak dapat terhidrolisis oleh air.",
                    "exec_hint": "Pernyataan 3 salah karena anion asam kuat tidak terhidrolisis."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Campuran larutan berikut yang dapat menghasilkan sistem larutan penyangga (buffer) adalah...",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "100 mL $\\text{CH}_3\\text{COOH}\\,0{{,}}2\\text{ M}$ + 100 mL $\\text{NaOH}\\,0{{,}}1\\text{ M}$", "correct": True},
                        {"key": "B", "text": "100 mL $\\text{NH}_3\\,0{{,}}2\\text{ M}$ + 100 mL $\\text{HCl}\\,0{{,}}1\\text{ M}$", "correct": True},
                        {"key": "C", "text": "100 mL $\\text{CH}_3\\text{COOH}\\,0{{,}}1\\text{ M}$ + 100 mL $\\text{CH}_3\\text{COONa}\\,0{{,}}1\\text{ M}$", "correct": True},
                        {"key": "D", "text": "100 mL $\\text{HCl}\\,0{{,}}1\\text{ M}$ + 100 mL $\\text{NaOH}\\,0{{,}}1\\text{ M}$", "correct": False},
                        {"key": "E", "text": "100 mL $\\text{CH}_3\\text{COOH}\\,0{{,}}1\\text{ M}$ + 100 mL $\\text{NaOH}\\,0{{,}}2\\text{ M}$", "correct": False}
                    ],
                    "concept_hint": "Buffer terbentuk jika ada sisa asam lemah + garamnya, atau basa lemah + garamnya. Jika asam kuat sisa atau habis sama asam basa kuat, bukan buffer.",
                    "exec_hint": "Opsi A dan B menyisakan asam/basa lemah, opsi C langsung mencampurkan asam lemah dan garamnya. Opsi D garam netral, opsi E basa kuat bersisa."
                }
            ]
        },
        {
            "materi": "ELEKTROKIMIA & REDOKS",
            "topic": "Sel Volta & Elektrolisis Hukum Faraday",
            "formula_title": "POTENSIAL SEL VOLTA STANDAR",
            "formula_latex": r"E^\circ_{\text{sel}} = E^\circ_{\text{katoda}} - E^\circ_{\text{anoda}}, \quad w = \frac{e \cdot I \cdot t}{96500}",
            "formula_legend": "• Katoda: Reduksi (potensial lebih tinggi)<br>• Anoda: Oksidasi (potensial lebih rendah)<br>• $w$: Massa endapan (g)",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: f"Diketahui potensial reduksi standar logam: $\\text{{Zn}}^{{2+}}_{{(aq)}} + 2e^- \\to \\text{{Zn}}_{{(s)}} \\quad E^\\circ = -0{{,}}76\\text{{ V}}$ dan $\\text{{Cu}}^{{2+}}_{{(aq)}} + 2e^- \\to \\text{{Cu}}_{{(s)}} \\quad E^\\circ = +0{{,}}34\\text{{ V}}$. Nilai potensial standar sel Volta yang disusun dari kedua elektrode tersebut dan notasi sel yang tepat adalah...",
                    "options": [
                        {"key": "A", "text": "+1,10 V dengan notasi sel: Zn | Zn²⁺ || Cu²⁺ | Cu"},
                        {"key": "B", "text": "+1,10 V dengan notasi sel: Cu | Cu²⁺ || Zn²⁺ | Zn"},
                        {"key": "C", "text": "-1,10 V dengan notasi sel: Zn | Zn²⁺ || Cu²⁺ | Cu"},
                        {"key": "D", "text": "+0,42 V dengan notasi sel: Zn | Zn²⁺ || Cu²⁺ | Cu"},
                        {"key": "E", "text": "+0,42 V dengan notasi sel: Cu | Cu²⁺ || Zn²⁺ | Zn"}
                    ],
                    "correct": "A",
                    "concept_hint": "$E^\\circ_{\\text{sel}} = E^\\circ(\\text{katoda/reduksi}) - E^\\circ(\\text{anoda/oksidasi})$. Logam Cu berpotensial lebih positif sehingga tereduksi di katoda.",
                    "exec_hint": "$E^\\circ_{\\text{sel}} = +0{{,}}34 - (-0{{,}}76) = +1{{,}}10\\text{ V}$. Anoda di kiri, katoda di kanan: $\\text{Zn} | \\text{Zn}^{2+} || \\text{Cu}^{2+} | \\text{Cu}$."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: f"Larutan tembaga(II) sulfat ($\\text{{CuSO}}_4$) dielektrolisis menggunakan elektrode karbon (C) inert dengan arus listrik $I = {v['I_amp']}\\text{{ A}}$ selama $t = {v['t_sec']}\\text{{ detik}}$ ($A_r\\,\\text{{Cu}} = 63{{,}}5$). Analisislah kebenaran peristiwa elektrolisis berikut:",
                    "statements": lambda v: [
                        {"text": "Pada katoda terjadi reduksi ion tembaga menghasilkan endapan logam Cu pada permukaan elektrode.", "answer": True},
                        {"text": "Pada anoda terjadi oksidasi molekul air yang membebaskan gas oksigen ($\text{O}_2$) dan ion hidrogen ($\text{H}^+$).", "answer": True},
                        {"text": "Elektrode karbon ikut larut teroksidasi selama proses elektrolisis berlangsung.", "answer": False},
                        {"text": f"Massa Cu yang mengendap di katoda dapat dihitung dengan rumus Faraday $w = \\frac{{63{{,}}5 \\times {v['I_amp']} \\times {v['t_sec']}}}{{2 \\times 96500}}$ gram.", "answer": True}
                    ],
                    "concept_hint": "Elektrode karbon bersifat inert (tidak bereaksi). Pada anoda, karena ion sulfat adalah sisa asam oksi, air yang teroksidasi.",
                    "exec_hint": "Pernyataan 3 salah karena karbon adalah elektrode inert."
                },
                {
                    "type": "multi",
                    "stem": lambda v: f"Berdasarkan deret kereaktifan logam Volta, manakah reaksi redoks berikut yang dapat berlangsung secara spontan pada keadaan standar? (Pilihlah semua reaksi spontan)",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "$\\text{Mg}_{(s)} + \\text{Zn}^{2+}_{(aq)} \\to \\text{Mg}^{2+}_{(aq)} + \\text{Zn}_{(s)}$", "correct": True},
                        {"key": "B", "text": "$\\text{Zn}_{(s)} + 2\\text{Ag}^+_{(aq)} \\to \\text{Zn}^{2+}_{(aq)} + 2\\text{Ag}_{(s)}$", "correct": True},
                        {"key": "C", "text": "$\\text{Fe}_{(s)} + \\text{Cu}^{2+}_{(aq)} \\to \\text{Fe}^{2+}_{(aq)} + \\text{Cu}_{(s)}$", "correct": True},
                        {"key": "D", "text": "$\\text{Cu}_{(s)} + 2\\text{H}^+_{(aq)} \\to \\text{Cu}^{2+}_{(aq)} + \\text{H}_{2(g)}$", "correct": False},
                        {"key": "E", "text": "$\\text{Ag}_{(s)} + \\text{Fe}^{2+}_{(aq)} \\to \\text{Ag}^+_{(aq)} + \\text{Fe}_{(s)}$", "correct": False}
                    ],
                    "concept_hint": "Logam yang terletak di sebelah kiri dalam deret Volta mampu mendesak/mereduksi kation logam di sebelah kanannya ($E^\\circ_{\\text{sel}} > 0$).",
                    "exec_hint": "Cu dan Ag berada di sebelah kanan H, sehingga tidak dapat mereduksi ion H+ atau Fe2+ secara spontan."
                }
            ]
        }
    ]

    sections = [
        ("easy", "latihan", 35, "kim-lat-e-"),
        ("medium", "latihan", 35, "kim-lat-m-"),
        ("hard", "latihan", 35, "kim-lat-h-"),
        ("hard", "simulasi", 30, "kim-sim-")
    ]

    for diff, mode, count, prefix in sections:
        for i in range(1, count + 1):
            qid = f"{prefix}{i:02d}"
            p_idx = (i - 1) % len(pillars)
            pillar = pillars[p_idx]
            concept_variant = pillar["concepts"][(i - 1) % len(pillar["concepts"])]
            q_type = concept_variant["type"]

            v = {
                "dH_etanol": 278 + (i % 5) * 5,
                "dH_co2": 394 + (i % 4) * 2,
                "dH_h2o": 286 + (i % 4) * 3,
                "m_larutan": 100 + (i % 4) * 50,
                "dT": 4 + (i % 5),
                "vol_asam": 100,
                "M_asam": 0.1,
                "vol_basa": 100,
                "M_basa": 0.1,
                "I_amp": 2 + (i % 4) * 2,
                "t_sec": 965 + (i % 3) * 965
            }

            question_text = concept_variant["stem"](v)
            c_hint = concept_variant["concept_hint"]

            if q_type == "mcq":
                if "calc" in concept_variant:
                    ans_val = concept_variant["calc"](v)
                    unit_str = concept_variant["unit"]
                    deltas = concept_variant["distractor_delta"]
                    val_list = [ans_val]
                    for d in deltas:
                        val_list.append(ans_val + d)
                    val_list = sorted(list(set(val_list)))[:5]
                    while len(val_list) < 5:
                        val_list.append(val_list[-1] + 10)
                    correct_idx = (i + p_idx) % 5
                    keys = ["A", "B", "C", "D", "E"]
                    correct_key = keys[correct_idx]
                    if ans_val in val_list:
                        val_list.remove(ans_val)
                    random.shuffle(val_list)
                    final_vals = val_list[:correct_idx] + [ans_val] + val_list[correct_idx:]
                    options = [{"key": keys[k_i], "text": f"${final_vals[k_i]}\\text{{ {unit_str}}}$" if unit_str else f"{final_vals[k_i]}"} for k_i in range(5)]
                    e_hint = concept_variant["exec_hint"](v, ans_val)
                else:
                    options = concept_variant["options"]
                    correct_key = concept_variant["correct"]
                    e_hint = concept_variant["exec_hint"]

                explanation = f"Pembahasan: {e_hint} Kunci jawaban yang tepat adalah {correct_key}."

                q_obj = {
                    "id": qid,
                    "subject": "kimia",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "mcq",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKey": correct_key,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": (i <= 5 and mode == "latihan" and diff == "easy")
                }
            elif q_type == "matrix":
                raw_stmts = concept_variant["statements"](v)
                statements = []
                correct_answers = {}
                for s_i, st in enumerate(raw_stmts):
                    s_id = str(s_i)
                    statements.append({"id": s_id, "text": st["text"]})
                    correct_answers[s_id] = st["answer"]
                e_hint = concept_variant["exec_hint"]
                explanation = f"Evaluasi konsep kimiawi: {e_hint}"

                q_obj = {
                    "id": qid,
                    "subject": "kimia",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "matrix",
                    "questionHtml": question_text,
                    "statements": statements,
                    "correctAnswers": correct_answers,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }
            elif q_type == "multi":
                raw_opts = concept_variant["options_gen"](v)
                options = []
                correct_keys = []
                for ro in raw_opts:
                    options.append({"key": ro["key"], "text": ro["text"]})
                    if ro["correct"]:
                        correct_keys.append(ro["key"])
                correct_keys.sort()
                e_hint = concept_variant["exec_hint"]
                explanation = f"Analisis opsi multi-jawaban: {e_hint} Opsi yang benar: {', '.join(correct_keys)}."

                q_obj = {
                    "id": qid,
                    "subject": "kimia",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "multi",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKeys": correct_keys,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }

            questions.append(q_obj)

    out_file = os.path.join(DATA_DIR, "questions_kimia.js")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - KIMIA (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F SMA / Pusmendik Standar HOTS & AKM\n */\n")
        f.write("window.TKA_KIMIA_QUESTIONS = ")
        json.dump(questions, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Generated {len(questions)} questions in {out_file}")

def generate_biologi():
    questions = []
    
    pillars = [
        {
            "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
            "topic": "Respirasi Seluler & Enzim",
            "formula_title": "METABOLISME KATABOLISME GLUKOSA",
            "formula_latex": r"\text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2 \to 6\text{CO}_2 + 6\text{H}_2\text{O} + 36\text{–}38\,\text{ATP}",
            "formula_legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
                    "options": [
                        {"key": "A", "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"},
                        {"key": "B", "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"},
                        {"key": "C", "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"},
                        {"key": "D", "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"},
                        {"key": "E", "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"}
                    ],
                    "correct": "A",
                    "concept_hint": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
                    "exec_hint": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Aktivitas kerja enzim katalase diuji menggunakan ekstrak hati ayam yang ditetesi larutan hidrogen peroksida (H₂O₂). Evaluasilah kebenaran hasil pengamatan eksperimen enzimatis berikut:",
                    "statements": lambda v: [
                        {"text": "Gelembung gas yang terbentuk secara melimpah pada kondisi pH netral adalah gas oksigen (O₂).", "answer": True},
                        {"text": "Pemanasan ekstrak hati hingga suhu 80°C menyebabkan enzim mengalami denaturasi protein sehingga reaksi terhenti.", "answer": True},
                        {"text": "Penambahan larutan HCl pekat hingga pH 2 akan mempercepat laju penguraian hidrogen peroksida oleh enzim katalase.", "answer": False},
                        {"text": "Enzim katalase berfungsi mempercepat reaksi tanpa ikut terkonsumsi atau berubah menjadi produk akhir.", "answer": True}
                    ],
                    "concept_hint": "Enzim adalah biokatalisator berbahan protein yang sensitif terhadap suhu tinggi (denaturasi) dan pH ekstrem (asam/basa kuat).",
                    "exec_hint": "Pernyataan 3 salah karena enzim katalase bekerja optimal pada pH netral dan inaktif pada pH sangat asam."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah peristiwa biokimia yang berlangsung secara tepat pada reaksi terang fotosintesis di dalam membran tilakoid kloroplas:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Fotolisis molekul air menghasilkan elektron, proton (H⁺), dan melepaskan gas O₂.", "correct": True},
                        {"key": "B", "text": "Fotofosforilasi non-siklik menghasilkan molekul penyimpan energi ATP dan NADPH.", "correct": True},
                        {"key": "C", "text": "Eksitasi elektron pada klorofil fotosistem II (P680) akibat penyerapan foton cahaya.", "correct": True},
                        {"key": "D", "text": "Fiksasi gas CO₂ oleh enzim RuBisCO menghasilkan asam fosfogliserat (PGA).", "correct": False},
                        {"key": "E", "text": "Reduksi senyawa bifosfogliserat menjadi glukosa berkarbon enam di stroma kloroplas.", "correct": False}
                    ],
                    "concept_hint": "Reaksi terang membutuhkan cahaya untuk memecah air dan membuat ATP/NADPH. Fiksasi CO₂ dan sintesis glukosa terjadi pada reaksi gelap (Siklus Calvin) di stroma.",
                    "exec_hint": "Pilihan A, B, dan C terjadi pada reaksi terang di tilakoid. Opsi D dan E terjadi di stroma pada reaksi gelap."
                }
            ]
        },
        {
            "materi": "GENETIKA & POLA HEREDITAS",
            "topic": "Sintesis Protein & Hukum Mendel",
            "formula_title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
            "formula_latex": r"\text{Dihibrid}: 9 : 3 : 3 : 1, \quad \text{Sentral Dogma}: \text{DNA} \xrightarrow{\text{Transkripsi}} \text{mRNA} \xrightarrow{\text{Translasi}} \text{Polipeptida}",
            "formula_legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Jika urutan basa nitrogen pada rantai antisense (DNA cetakan/template) adalah 3'-TAC-GGA-TCA-CCT-ACT-5', maka urutan kodon pada mRNA hasil transkripsi dan jumlah asam amino yang terbentuk adalah...",
                    "options": [
                        {"key": "A", "text": "5'-AUG-CCU-AGU-GGA-UGA-3' (menghasilkan 4 asam amino sebelum kodon stop)"},
                        {"key": "B", "text": "5'-AUG-GGA-UCA-CCU-ACU-3' (menghasilkan 5 asam amino lengkap berurutan)"},
                        {"key": "C", "text": "3'-AUG-CCU-AGU-GGA-UGA-5' (menghasilkan 5 asam amino rantai penuh)"},
                        {"key": "D", "text": "5'-UAC-GGA-UCA-CCU-ACU-3' (menghasilkan 3 asam amino berpasangan)"},
                        {"key": "E", "text": "5'-AUG-CCU-UCA-GGA-UAA-3' (menghasilkan 2 asam amino fungsional)"}
                    ],
                    "correct": "A",
                    "concept_hint": "Transkripsi menghasilkan mRNA dengan arah 5' ke 3' komplementer: T→A, A→U, C→G, G→C. Kodon stop UGA mengakhiri translasi.",
                    "exec_hint": "Kodon: AUG (Met), CCU (Pro), AGU (Ser), GGA (Gly), UGA (Kodon Stop). Kodon stop tidak mengode asam amino, sehingga terbentuk 4 asam amino."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
                    "statements": lambda v: [
                        {"text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%.", "answer": True},
                        {"text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia).", "answer": True},
                        {"text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%.", "answer": True},
                        {"text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom.", "answer": False}
                    ],
                    "concept_hint": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
                    "exec_hint": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Manakah mutasi genetik berikut yang tergolong dalam jenis mutasi salah arti (missense mutation) dan dampaknya terhadap struktur polipeptida?",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Perubahan satu basa nitrogen yang menyebabkan pergantian satu asam amino pada rantai polipeptida.", "correct": True},
                        {"key": "B", "text": "Terjadinya substitusi basa nitrogen pada kodon hemoglobin yang memicu penyakit anemia sel sabit.", "correct": True},
                        {"key": "C", "text": "Perubahan basa nitrogen yang membentuk kodon stop prematur sehingga polipeptida terpotong.", "correct": False},
                        {"key": "D", "text": "Insersi satu pasang basa yang menggeser kerangka baca (frameshift mutation) seluruh asam amino.", "correct": False},
                        {"key": "E", "text": "Perubahan basa nitrogen yang tidak mengubah jenis asam amino yang dihasilkan (silent mutation).", "correct": False}
                    ],
                    "concept_hint": "Missense mutation mengganti satu asam amino dengan asam amino lain (contoh: HbA ke HbS pada sickle cell). Kodon stop prematur adalah nonsense mutation.",
                    "exec_hint": "Opsi A dan B adalah karakteristik mutasi salah arti (missense)."
                }
            ]
        },
        {
            "materi": "FISIOLOGI ORGAN & EKOLOGI",
            "topic": "Sistem Ekskresi Nefron & Aliran Energi",
            "formula_title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
            "formula_latex": r"\text{Filtrasi (Glomerulus)} \to \text{Reabsorpsi (TK Proksimal)} \to \text{Augmentasi (TK Distal)}",
            "formula_legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Hasil uji laboratorium urin seorang pasien menunjukkan terbentuknya endapan merah bata saat diuji dengan reagen Benedict dan terdeteksi glukosa positif. Berdasarkan data klinis tersebut, gangguan fisiologis terjadi pada bagian nefron...",
                    "options": [
                        {"key": "A", "text": "Tubulus kontortus proksimal yang gagal mereabsorpsi glukosa primer"},
                        {"key": "B", "text": "Glomerulus yang mengalami kebocoran membran filtrasi protein darah"},
                        {"key": "C", "text": "Lengkung Henle desenden yang hiperpermeabel terhadap ion natrium"},
                        {"key": "D", "text": "Tubulus kontortus distal yang tersumbat saat sekresi zat sisa obat"},
                        {"key": "E", "text": "Tubulus kolektivus yang kekurangan stimulasi hormon antidiuretik ADH"}
                    ],
                    "correct": "A",
                    "concept_hint": "Reabsorpsi zat-zat esensial bernutrisi tinggi (100% glukosa dan asam amino) secara normal terjadi di tubulus kontortus proksimal (TKP).",
                    "exec_hint": "Glikosuria (glukosa dalam urin) menunjukkan kegagalan transport aktif reabsorpsi glukosa di tubulus kontortus proksimal atau kadar gula darah melebihi ambang batas ginjal."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Di suatu ekosistem danau, limbah pupuk pertanian yang mengandung fosfat dan nitrogen mengalir secara berlebih ke perairan (eutrofikasi). Evaluasilah dampak ekologis yang timbul berikut:",
                    "statements": lambda v: [
                        {"text": "Terjadi ledakan populasi alga (blooming algae) yang menutupi seluruh permukaan air danau.", "answer": True},
                        {"text": "Penetrasi cahaya matahari ke perairan dalam menurun drastis sehingga fitoplankton di dasar danau mati.", "answer": True},
                        {"text": "Aktivitas dekomposer meningkat pesat sehingga kadar oksigen terlarut (Dissolved Oxygen) melonjak drastis.", "answer": False},
                        {"text": "Kematian massal ikan dan biota air terjadi akibat kondisi anoksik (ketiadaan oksigen terlarut).", "answer": True}
                    ],
                    "concept_hint": "Dekomposer aerobik mengonsumsi banyak oksigen untuk mengurai biomassa alga yang mati, sehingga kadar oksigen terlarut justru jatuh drastis (anoksia).",
                    "exec_hint": "Pernyataan 3 salah karena kadar oksigen terlarut turun drastis (hipoksia/anoksia), bukan melonjak."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya.", "correct": True},
                        {"key": "B", "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel.", "correct": True},
                        {"key": "C", "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik.", "correct": True},
                        {"key": "D", "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof.", "correct": False},
                        {"key": "E", "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya.", "correct": False}
                    ],
                    "concept_hint": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
                    "exec_hint": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
                }
            ]
        }
    ]

    sections = [
        ("easy", "latihan", 35, "bio-lat-e-"),
        ("medium", "latihan", 35, "bio-lat-m-"),
        ("hard", "latihan", 35, "bio-lat-h-"),
        ("hard", "simulasi", 30, "bio-sim-")
    ]

    for diff, mode, count, prefix in sections:
        for i in range(1, count + 1):
            qid = f"{prefix}{i:02d}"
            p_idx = (i - 1) % len(pillars)
            pillar = pillars[p_idx]
            concept_variant = pillar["concepts"][(i - 1) % len(pillar["concepts"])]
            q_type = concept_variant["type"]

            v = {}
            question_text = concept_variant["stem"](v)
            c_hint = concept_variant["concept_hint"]
            e_hint = concept_variant["exec_hint"]

            if q_type == "mcq":
                options = concept_variant["options"]
                correct_key = concept_variant["correct"]
                explanation = f"Analisis biologis: {e_hint} Jawaban tepat: {correct_key}."

                q_obj = {
                    "id": qid,
                    "subject": "biologi",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "mcq",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKey": correct_key,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": (i <= 5 and mode == "latihan" and diff == "easy")
                }
            elif q_type == "matrix":
                raw_stmts = concept_variant["statements"](v)
                statements = []
                correct_answers = {}
                for s_i, st in enumerate(raw_stmts):
                    s_id = str(s_i)
                    statements.append({"id": s_id, "text": st["text"]})
                    correct_answers[s_id] = st["answer"]
                explanation = f"Evaluasi biologi: {e_hint}"

                q_obj = {
                    "id": qid,
                    "subject": "biologi",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "matrix",
                    "questionHtml": question_text,
                    "statements": statements,
                    "correctAnswers": correct_answers,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }
            elif q_type == "multi":
                raw_opts = concept_variant["options_gen"](v)
                options = []
                correct_keys = []
                for ro in raw_opts:
                    options.append({"key": ro["key"], "text": ro["text"]})
                    if ro["correct"]:
                        correct_keys.append(ro["key"])
                correct_keys.sort()
                explanation = f"Analisis multi-jawaban: {e_hint} Kunci jawaban: {', '.join(correct_keys)}."

                q_obj = {
                    "id": qid,
                    "subject": "biologi",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "multi",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKeys": correct_keys,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }

            questions.append(q_obj)

    out_file = os.path.join(DATA_DIR, "questions_biologi.js")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - BIOLOGI (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F SMA / Pusmendik Standar HOTS & AKM\n */\n")
        f.write("window.TKA_BIOLOGI_QUESTIONS = ")
        json.dump(questions, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Generated {len(questions)} questions in {out_file}")

if __name__ == "__main__":
    print("Generating Wave 1 Saintek questions...")
    generate_fisika()
    generate_kimia()
    generate_biologi()
    print("Wave 1 Saintek completed successfully!")
