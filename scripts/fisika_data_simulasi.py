# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Fisika (SMA/MA Saintek)
Dataset: Simulasi CBT HOTS (35 Authentic Questions, fis-sim-01 to 35)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
Composition:
  - 25 Authentic Single MCQ HOTS (fis-sim-01 to 25)
  - 5 Complex Multi-select HOTS (fis-sim-26 to 30)
  - 5 Matrix Benar-Salah HOTS (fis-sim-31 to 35)
"""

FISIKA_SIMULASI_ITEMS = [
    {
        "id": "fis-sim-01",
        "materi": "VEKTOR & KINEMATIKA GERAK RELATIF",
        "topic": "Gerak Menyeberangi Sungai Berarus Deras Tegak Lurus",
        "stem": "Sebuah perahu bermotor hendak menyeberangi sungai dengan lebar $w = 120\\text{ meter}$. Arus air sungai mengalir ke arah timur dengan kecepatan tetap $v_{\\text{arus}} = 3\\text{ m/s}$. Motor perahu mampu melaju dengan kelajuan $v_{\\text{perahu}} = 5\\text{ m/s}$ relatif terhadap air. Agar lintasan perahu dapat menyeberang sungai tepat tegak lurus terhadap arah arus (sampai di titik seberang yang persis berhadapan), sudut haluan perahu terhadap tepi sungai ($\\alpha$) dan waktu tempuh penyeberangan ($t$) adalah...",
        "correct": "$\\alpha = 126{,}87^\\circ$ terhadap arah aliran hilir (atau mengarah ke hulu sebesar $53^\\circ$ terhadap tepi hulu) dengan waktu tempuh $t = 30\\text{ sekon}$, karena komponen kecepatan perahu yang melawan arus harus tepat mengimbangi arus sungai ($v_{\\text{perahu}} \\sin\\theta = v_{\\text{arus}} \\implies 5 \\sin\\theta = 3 \\implies \\sin\\theta = 0{,}6 \\implies \\theta = 37^\\circ$ dari garis tegak lurus, atau $53^\\circ$ dari tepi sungai hulu). Kecepatan resultan efektif menyeberang adalah $v_y = \\sqrt{5^2 - 3^2} = 4\\text{ m/s}$, sehingga waktu tempuh $t = \\frac{120\\text{ m}}{4\\text{ m/s}} = 30\\text{ sekon}$.",
        "distractors": [
            "$\\alpha = 90^\\circ$ tegak lurus tepi sungai dengan waktu tempuh $t = 24\\text{ sekon}$, karena perahu langsung diarahkan tegak lurus sehingga pasti akan terseret jauh ke arah hilir.",
            "$\\alpha = 60^\\circ$ ke arah hulu dengan waktu tempuh $t = 40\\text{ sekon}$, dihitung dari pendekatan sudut deviasi sembarang tanpa analisis proyeksi vektor kecepatan.",
            "$\\alpha = 45^\\circ$ terhadap hilir dengan waktu tempuh $t = 15\\text{ sekon}$, karena kecepatan perahu dan kecepatan arus langsung dijumlahkan secara skalar biasa.",
            "$\\alpha = 30^\\circ$ ke arah hilir dengan waktu tempuh $t = 60\\text{ sekon}$, dihitung dari perbandingan terbalik lebar sungai terhadap arus air."
        ],
        "formula": {
            "title": "VEKTOR KECEPATAN RELATIF MENYEBERANG SUNGAI",
            "latex": "v_x = v_p \\sin\\theta - v_a = 0 \\implies \\sin\\theta = \\frac{v_a}{v_p} = \\frac{3}{5} = 0{,}6; \\quad v_{\\text{res}} = \\sqrt{v_p^2 - v_a^2} = 4\\text{ m/s}; \\quad t = \\frac{w}{v_{\\text{res}}} = \\frac{120}{4} = 30\\text{ s}",
            "legend": "• Agar lintasan tepat tegak lurus, komponen $x$ harus bernilai nol ($v_x = 0$)<br>• Kecepatan efektif perahu menyeberang $v_{\\text{res}} = 4\\text{ m/s}$<br>• Waktu tempuh $t = 30\\text{ sekon}$"
        },
        "hints": {
            "concept": "Agar sampai tegak lurus di seberang, haluan perahu harus condong ke hulu sehingga v_perahu * sin(theta) = v_arus. Kecepatan resultan tegak lurus v_res = sqrt(vp^2 - va^2).",
            "execution": "v_res = sqrt(5^2 - 3^2) = 4 m/s. t = 120 / 4 = 30 sekon."
        }
    },
    {
        "id": "fis-sim-02",
        "materi": "DINAMIKA GERAK (SISTEM BENDA BERTUMPUK)",
        "topic": "Gaya Maksimum pada Benda Bertumpuk Tanpa Tergelincir",
        "stem": "Balok $A$ bermassa $m_A = 2\\text{ kg}$ diletakkan di atas balok $B$ bermassa $m_B = 6\\text{ kg}$. Balok $B$ berada di atas lantai horizontal yang licin sempurna tanpa gesekan. Koefisien gesekan statis antara permukaan balok $A$ dan balok $B$ adalah $\\mu_s = 0{,}4$ ($g = 10\\text{ m/s}^2$). Sebuah gaya horizontal $F$ ditarikkan pada balok bawah $B$. Nilai gaya tarik maksimum ($F_{\\max}$) agar kedua balok tetap bergerak bersama-sama tanpa balok $A$ tergelincir adalah...",
        "correct": "$F_{\\max} = 32\\text{ Newton}$, karena percepatan maksimum balok $A$ hanya disediakan oleh gaya gesek statis maksimum antara balok $A$ dan $B$: $f_{s,\\max} = \\mu_s m_A g = 0{,}4 \\times 2 \\times 10 = 8\\text{ N}$, sehingga percepatan maksimum sistem adalah $a_{\\max} = \\frac{f_{s,\\max}}{m_A} = \\mu_s g = 0{,}4 \\times 10 = 4\\text{ m/s}^2$. Menurut Hukum II Newton untuk massa total kedua balok, gaya maksimum pada balok bawah adalah $F_{\\max} = (m_A + m_B) a_{\\max} = (2 + 6) \\times 4 = 8 \\times 4 = 32\\text{ Newton}$.",
        "distractors": [
            "$F_{\\max} = 8\\text{ Newton}$, karena menyamakan gaya tarik maksimum dengan nilai gaya gesekan statis antarbalok semata.",
            "$F_{\\max} = 24\\text{ Newton}$, dihitung dengan hanya memperhitungkan massa balok bawah $B$ dikalikan percepatan maksimum.",
            "$F_{\\max} = 40\\text{ Newton}$, dihitung dari perkalian koefisien gesekan dengan berat total gabungan kedua balok di atas lantai.",
            "$F_{\\max} = 16\\text{ Newton}$, dihitung dari penggandaan massa balok atas tanpa menyertakan inersia balok bawah."
        ],
        "formula": {
            "title": "GAYA MAKSIMUM SISTEM BENDA BERTUMPUK",
            "latex": "a_{\\max} = \\mu_s g = 0{,}4 \\times 10 = 4\\text{ m/s}^2; \\quad F_{\\max} = (m_A + m_B) a_{\\max} = (2 + 6) \\times 4 = 32\\text{ N}",
            "legend": "• Balok atas $A$ hanya digerakkan oleh gaya gesek statis $f_s \\le \\mu_s m_A g$<br>• $a_{\\max} = 4\\text{ m/s}^2$<br>• $F_{\\max} = (m_A + m_B) a_{\\max} = 32\\text{ N}$"
        },
        "hints": {
            "concept": "Percepatan maksimum balok atas: a_max = mu_s * g = 0,4 * 10 = 4 m/s^2. Agar bergerak bersama, gaya tarik F_max = (mA + mB) * a_max.",
            "execution": "F_max = (2 + 6) * 4 = 32 N."
        }
    },
    {
        "id": "fis-sim-03",
        "materi": "USAHA & ENERGI (GERAK MELINGKAR VERTIKAL)",
        "topic": "Kecepatan Kritis & Gaya Normal Puncak Roller Coaster",
        "stem": "Sebuah kereta roller coaster bermassa $m = 500\\text{ kg}$ meluncur menuruni lintasan licin dan memasuki lintasan melingkar vertikal (loop-the-loop) yang memiliki jari-jari $R = 10\\text{ meter}$. Jika percepatan gravitasi bumi $g = 10\\text{ m/s}^2$, kecepatan minimum di titik puncak loop ($v_{\\text{puncak}}$) agar kereta tidak terlepas dari rel serta ketinggian minimum pelepasan kereta ($h_{\\min}$) dari dasar rel adalah...",
        "correct": "$v_{\\text{puncak}} = 10\\text{ m/s}$ dan $h_{\\min} = 25\\text{ meter}$, karena syarat kereta tidak terlepas di titik puncak loop adalah gaya normal tepat nol ($N = 0$), sehingga gaya gravitasi bertindak sebagai gaya sentripetal: $m g = \\frac{m v^2}{R} \\implies v_{\\text{puncak}} = \\sqrt{g R} = \\sqrt{10 \\times 10} = 10\\text{ m/s}$. Dari Hukum Kekekalan Energi Mekanik terhadap dasar lintasan ($h=0$): $m g h_{\\min} = m g (2R) + \\frac{1}{2} m v_{\\text{puncak}}^2 \\implies h_{\\min} = 2R + \\frac{v^2}{2g} = 2(10) + \\frac{100}{20} = 20 + 5 = 25\\text{ meter}$.",
        "distractors": [
            "$v_{\\text{puncak}} = 14{,}14\\text{ m/s}$ dan $h_{\\min} = 20\\text{ meter}$, dihitung dengan menyamakan tinggi pelepasan tepat sama dengan diameter lingkaran loop.",
            "$v_{\\text{puncak}} = 7{,}07\\text{ m/s}$ dan $h_{\\min} = 15\\text{ meter}$, dihitung dari asumsi bahwa kecepatan di puncak sama dengan separuh kecepatan dasar lintasan.",
            "$v_{\\text{puncak}} = 20\\text{ m/s}$ dan $h_{\\min} = 30\\text{ meter}$, karena rumus kecepatan kritis keliru menggunakan diameter lingkaran dalam akar gravitasi.",
            "$v_{\\text{puncak}} = 0\\text{ m/s}$ dan $h_{\\min} = 20\\text{ meter}$, karena beranggapan kereta dapat berhenti sesaat di puncak lingkaran vertikal."
        ],
        "formula": {
            "title": "KECEPATAN KRITIS DAN KETINGGIAN LOOP THE LOOP",
            "latex": "v_{\\text{puncak}} = \\sqrt{g R} = \\sqrt{10 \\times 10} = 10\\text{ m/s}; \\quad h_{\\min} = \\frac{5}{2} R = 2{,}5 \\times 10 = 25\\text{ m}",
            "legend": "• $N_{\\text{puncak}} = 0 \\implies m g = \\frac{m v^2}{R}$<br>• $h_{\\min} = 2R + \\frac{gR}{2g} = 2{,}5 R = 25\\text{ meter}$"
        },
        "hints": {
            "concept": "Di puncak loop: N = 0 -> v_puncak = sqrt(g*R). Energi mekanik awal = energi mekanik puncak: m*g*h_min = m*g*(2R) + 1/2*m*(g*R) -> h_min = 2,5 * R.",
            "execution": "v_puncak = sqrt(10*10) = 10 m/s. h_min = 2,5 * 10 = 25 meter."
        }
    },
    {
        "id": "fis-sim-04",
        "materi": "MOMENTUM & TUMBUKAN DUA DIMENSI",
        "topic": "Tumbukan Lenting Sempurna Massa Sama",
        "stem": "Dua buah bola biliar identik bermassa sama $m_1 = m_2 = 0{,}2\\text{ kg}$ berada di atas meja licin. Bola 1 meluncur dengan kelajuan $v_1 = 4\\text{ m/s}$ menumbuk bola 2 yang mula-mula diam ($v_2 = 0$). Setelah tumbukan lenting sempurna berlangsung, bola 1 bergerak menyimpang dengan sudut $\\theta_1 = 30^\\circ$ terhadap arah gerak awalnya. Sudut hamburan bola 2 ($\\theta_2$) dan besar kelajuan bola 1 ($v_1'$) setelah tumbukan adalah...",
        "correct": "$\\theta_2 = 60^\\circ$ (sehingga kedua bola bergerak saling tegak lurus $\\theta_1 + \\theta_2 = 90^\\circ$) dan $v_1' = 2\\sqrt{3}\\text{ m/s} \\approx 3{,}46\\text{ m/s}$, karena pada tumbukan lenting sempurna dua massa identik di mana salah satu massa awalnya diam, vektor kecepatan akhir selalu membentuk sudut siku-siku ($90^\\circ$). Dari proyeksi trigonometri segitiga kecepatan: $v_1' = v_1 \\cos 30^\\circ = 4 \\times \\frac{1}{2}\\sqrt{3} = 2\\sqrt{3}\\text{ m/s}$.",
        "distractors": [
            "$\\theta_2 = 30^\\circ$ dan $v_1' = 2\\text{ m/s}$, karena diasumsikan bola 2 menyimpang secara simetris terhadap sumbu gerak awal.",
            "$\\theta_2 = 45^\\circ$ dan $v_1' = 2\\sqrt{2}\\text{ m/s}$, dihitung dari asumsi sudut deviasi bagi rata empat puluh lima derajat.",
            "$\\theta_2 = 90^\\circ$ dan $v_1' = 4\\text{ m/s}$, karena beranggapan bola 1 meneruskan seluruh momentum awalnya tanpa kehilangan energi.",
            "$\\theta_2 = 120^\\circ$ dan $v_1' = 1\\text{ m/s}$, dihitung dari pembalikan arah gerak bola tumbukan lenting sebagian."
        ],
        "formula": {
            "title": "TUMBUKAN LENTING SEMPURNA MASSA IDENTIK",
            "latex": "\\vec{v}_1 = \\vec{v}_1' + \\vec{v}_2' \\quad \\text{dan} \\quad v_1^2 = (v_1')^2 + (v_2')^2 \\implies \\theta_1 + \\theta_2 = 90^\\circ; \\quad v_1' = v_1 \\cos\\theta_1 = 4 \\cos 30^\\circ = 2\\sqrt{3}\\text{ m/s}",
            "legend": "• Sifat khas massa identik tumbukan elastis 2D: $\\vec{v}_1' \\cdot \\vec{v}_2' = 0 \\implies$ arah gerak saling tegak lurus ($90^\\circ$)<br>• $\\theta_2 = 90^\\circ - 30^\\circ = 60^\\circ$<br>• $v_1' = 2\\sqrt{3}\\text{ m/s} \\approx 3{,}46\\text{ m/s}$"
        },
        "hints": {
            "concept": "Tumbukan elastis 2 benda bermassa sama dengan target diam menghasilkan sudut pisah 90 derajat: theta1 + theta2 = 90. Maka theta2 = 60 derajat. v1' = v1 * cos(30).",
            "execution": "theta2 = 90 - 30 = 60 derajat. v1' = 4 * cos(30) = 4 * 0,5 * sqrt(3) = 2*sqrt(3) m/s = 3,46 m/s."
        }
    },
    {
        "id": "fis-sim-05",
        "materi": "ELASTISITAS & TEGANGAN BAHAN",
        "topic": "Modulus Young dan Pertambahan Panjang Kawat Baja",
        "stem": "Sebuah kawat baja memiliki panjang awal $L_0 = 4\\text{ meter}$ dan diameter penampang $d = 2\\text{ mm}$ (jari-jari $r = 1\\text{ mm} = 10^{-3}\\text{ m}$, sehingga luas penampang $A = \\pi r^2 = \\pi \\times 10^{-6}\\text{ m}^2$). Kawat digantung vertikal dan ditarik dengan gaya beban $F = 628\\text{ Newton}$ (gunakan $\\pi \\approx 3{,}14$, sehingga $A \\approx 3{,}14 \\times 10^{-6}\\text{ m}^2$). Jika modulus Young baja adalah $E = 2 \\times 10^{11}\\text{ N/m}^2$, tegangan tarik ($\\sigma$) dan pertambahan panjang kawat ($\\Delta L$) adalah...",
        "correct": "$\\sigma = 2 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 4\\text{ mm}$ (atau $4 \\times 10^{-3}\\text{ m}$), karena tegangan adalah $\\sigma = \\frac{F}{A} = \\frac{628\\text{ N}}{3{,}14 \\times 10^{-6}\\text{ m}^2} = 2 \\times 10^8\\text{ N/m}^2$. Pertambahan panjang kawat menurut hukum Hooke elastisitas adalah $\\Delta L = \\frac{\\sigma L_0}{E} = \\frac{(2 \\times 10^8\\text{ N/m}^2) \\times 4\\text{ m}}{2 \\times 10^{11}\\text{ N/m}^2} = \\frac{8 \\times 10^8}{2 \\times 10^{11}} = 4 \\times 10^{-3}\\text{ m} = 4\\text{ mm}$.",
        "distractors": [
            "$\\sigma = 1 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 2\\text{ mm}$, karena luas penampang keliru dihitung menggunakan diameter kawat tanpa dibagi dua menjadi jari-jari.",
            "$\\sigma = 4 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 8\\text{ mm}$, dihitung dari penggandaan tegangan geser torsional.",
            "$\\sigma = 2 \\times 10^7\\text{ N/m}^2$ dan $\\Delta L = 0{,}4\\text{ mm}$, karena galat konversi satuan luas dari milimeter persegi ke meter persegi.",
            "$\\sigma = 6{,}28 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 1\\text{ mm}$, dihitung tanpa membagi gaya dengan nilai pi luas penampang kawat."
        ],
        "formula": {
            "title": "MODULUS ELASTISITAS YOUNG & HUKUM HOOKE",
            "latex": "\\sigma = \\frac{F}{A} = \\frac{628}{3{,}14 \\times 10^{-6}} = 2 \\times 10^8\\text{ Pa}; \\quad \\Delta L = \\frac{F L_0}{A E} = \\frac{\\sigma L_0}{E} = \\frac{2 \\times 10^8 \\times 4}{2 \\times 10^{11}} = 4 \\times 10^{-3}\\text{ m} = 4\\text{ mm}",
            "legend": "• Luas penampang kawat silinder $A = \\pi r^2 = 3{,}14 \\times 10^{-6}\\text{ m}^2$<br>• Tegangan $\\sigma = 200\\text{ MPa}$<br>• Pertambahan panjang $\\Delta L = 4\\text{ mm}$"
        },
        "hints": {
            "concept": "Tegangan: sigma = F / A = F / (pi * r^2). Pertambahan panjang: Delta_L = sigma * L0 / E.",
            "execution": "sigma = 628 / (3,14e-6) = 2e8 N/m^2. Delta_L = (2e8 * 4) / 2e11 = 4e-3 m = 4 mm."
        }
    },
    {
        "id": "fis-sim-06",
        "materi": "HUKUM GRAVITASI NEWTON & KEPLER",
        "topic": "Hukum III Kepler & Perbandingan Periode Orbit Planet",
        "stem": "Dua planet $X$ dan $Y$ mengorbit sebuah bintang induk yang sama dalam lintasan berbentuk lingkaran. Jarak rata-rata planet $X$ ke bintang adalah $R_X = 4\\text{ SA}$ (Satuan Astronomi), sedangkan jarak rata-rata planet $Y$ adalah $R_Y = 16\\text{ SA}$. Jika periode revolusi planet $X$ mengelilingi bintang adalah $T_X = 8\\text{ tahun}$, periode revolusi planet $Y$ ($T_Y$) mengelilingi bintang tersebut menurut Hukum III Kepler adalah...",
        "correct": "$T_Y = 64\\text{ tahun}$, karena menurut Hukum III Kepler rasio kuadrat periode revolusi berbanding lurus dengan pangkat tiga jarak rata-rata orbit: $\\left(\\frac{T_Y}{T_X}\\right)^2 = \\left(\\frac{R_Y}{R_X}\\right)^3 = \\left(\\frac{16}{4}\\right)^3 = 4^3 = 64$, sehingga $\\frac{T_Y}{T_X} = \\sqrt{64} = 8$, dan periode planet $Y$ adalah $T_Y = 8 \\times T_X = 8 \\times 8 = 64\\text{ tahun}$.",
        "distractors": [
            "$T_Y = 32\\text{ tahun}$, karena hubungan Kepler keliru dianggap berbanding kuadrat langsung tanpa pemangkatan tiga jarak orbit.",
            "$T_Y = 128\\text{ tahun}$, dihitung dari perkalian periode planet pertama dengan rasio kuadrat jarak lintasan orbit.",
            "$T_Y = 16\\text{ tahun}$, karena beranggapan periode revolusi berbanding lurus linier dengan jarak rata-rata orbit satelit.",
            "$T_Y = 256\\text{ tahun}$, dihitung dari pemangkatan empat perbandingan jarak rata-rata orbit planet."
        ],
        "formula": {
            "title": "HUKUM III KEPLER",
            "latex": "\\frac{T_1^2}{R_1^3} = \\frac{T_2^2}{R_2^3} \\implies T_Y = T_X \\left(\\frac{R_Y}{R_X}\\right)^{3/2} = 8 \\times (4)^{3/2} = 8 \\times 8 = 64\\text{ tahun}",
            "legend": "• $R_Y / R_X = 16 / 4 = 4$<br>• $(4)^{3/2} = (\\sqrt{4})^3 = 2^3 = 8$<br>• $T_Y = 8 \\times 8 = 64\\text{ tahun}$"
        },
        "hints": {
            "concept": "Hukum III Kepler: (T1 / T2)^2 = (R1 / R2)^3. Maka TY = TX * (RY / RX)^(3/2).",
            "execution": "TY = 8 * (16 / 4)^(3/2) = 8 * 4^(1,5) = 8 * 8 = 64 tahun."
        }
    },
    {
        "id": "fis-sim-07",
        "materi": "FLUIDA STATIS (BEJANA BERHUBUNGAN)",
        "topic": "Tekanan Hidrostatis pada Pipa U Dua Zat Cair",
        "stem": "Sebuah pipa berbentuk huruf U mula-mula diisi air dengan massa jenis $\\rho_{\\text{air}} = 1.000\\text{ kg/m}^3$. Ke dalam kaki kanan pipa U tersebut dituangkan minyak dengan massa jenis $\\rho_{\\text{minyak}} = 800\\text{ kg/m}^3$ setinggi kolom $h_{\\text{minyak}} = 15\\text{ cm}$. Jika kedua ujung pipa terbuka ke udara bebas, selisih ketinggian permukaan air pada kaki kiri terhadap permukaan minyak pada kaki kanan ($\\Delta h$) adalah...",
        "correct": "$\\Delta h = 3\\text{ cm}$ (di mana permukaan air di kaki kiri lebih rendah $3\\text{ cm}$ dibanding permukaan atas minyak di kaki kanan), karena pada bidang batas bawah berlaku kesetimbangan tekanan hidrostatis $\\rho_{\\text{air}} g h_{\\text{air}} = \\rho_{\\text{minyak}} g h_{\\text{minyak}} \\implies h_{\\text{air}} = \\frac{\\rho_{\\text{minyak}}}{\\rho_{\\text{air}}} h_{\\text{minyak}} = \\frac{800}{1.000} \\times 15 = 12\\text{ cm}$. Selisih ketinggian antara kedua permukaan atas zat cair adalah $\\Delta h = h_{\\text{minyak}} - h_{\\text{air}} = 15\\text{ cm} - 12\\text{ cm} = 3\\text{ cm}$.",
        "distractors": [
            "$\\Delta h = 12\\text{ cm}$, karena nilai tersebut merupakan tinggi kolom air yang terangkat dari garis bidang batas kesetimbangan.",
            "$\\Delta h = 5\\text{ cm}$, dihitung dari perbandingan selisih massa jenis terhadap tinggi total kolom minyak.",
            "$\\Delta h = 2\\text{ cm}$, dihitung dari pendekatan pembulatan rasio kerapatan massa jenis fluida.",
            "$\\Delta h = 0\\text{ cm}$, karena mengasumsikan permukaan cairan dalam pipa U selalu datar sejajar dalam kondisi setimbang."
        ],
        "formula": {
            "title": "HUKUM UTAMA HIDROSTATIS PADA PIPA U",
            "latex": "P_A = P_B \\implies \\rho_{\\text{air}} h_{\\text{air}} = \\rho_{\\text{minyak}} h_{\\text{minyak}} \\implies h_{\\text{air}} = \\frac{800}{1.000} \\times 15 = 12\\text{ cm}; \\quad \\Delta h = 15 - 12 = 3\\text{ cm}",
            "legend": "• Bidang acuan diambil pada batas terendah pertemuan air dan minyak<br>• Tinggi kolom air terangkat di atas bidang batas $h_{\\text{air}} = 12\\text{ cm}$<br>• Selisih permukaan $\\Delta h = 15 - 12 = 3\\text{ cm}$"
        },
        "hints": {
            "concept": "Hukum Utama Hidrostatis: rho_air * h_air = rho_minyak * h_minyak. Cari h_air, lalu selisih tinggi Delta_h = h_minyak - h_air.",
            "execution": "h_air = (800 / 1000) * 15 = 12 cm. Delta_h = 15 - 12 = 3 cm."
        }
    },
    {
        "id": "fis-sim-08",
        "materi": "FLUIDA DINAMIS (VENTURIMETER TANPA MANOMETER)",
        "topic": "Kelajuan Aliran Fluida pada Pipa Venturi",
        "stem": "Minyak dengan massa jenis $\\rho = 800\\text{ kg/m}^3$ mengalir melalui sebuah venturimeter mendatar tanpa manometer. Luas penampang pipa utama adalah $A_1 = 50\\text{ cm}^2$ dan luas penampang leher yang menyempit adalah $A_2 = 25\\text{ cm}^2$ (sehingga rasio luas penampang $A_1/A_2 = 2$). Pada pipa vertikal pengukur tekanan, terdapat selisih ketinggian permukaan minyak sebesar $h = 45\\text{ cm} = 0{,}45\\text{ meter}$. Jika percepatan gravitasi bumi $g = 10\\text{ m/s}^2$, kelajuan aliran fluida di penampang utama ($v_1$) dan debit alirannya ($Q$) adalah...",
        "correct": "$v_1 = \\sqrt{3}\\text{ m/s} \\approx 1{,}73\\text{ m/s}$ dan $Q = 5\\sqrt{3} \\times 10^{-3}\\text{ m}^3\\text{/s} \\approx 8{,}66\\text{ L/s}$, karena rumus venturimeter tanpa manometer adalah $v_1 = \\sqrt{\\frac{2gh}{(A_1/A_2)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}45}{2^2 - 1}} = \\sqrt{\\frac{9}{4 - 1}} = \\sqrt{\\frac{9}{3}} = \\sqrt{3}\\text{ m/s}$. Debit aliran adalah $Q = A_1 v_1 = (50 \\times 10^{-4}\\text{ m}^2) \\times \\sqrt{3}\\text{ m/s} = 5\\sqrt{3} \\times 10^{-3}\\text{ m}^3\\text{/s} \\approx 8{,}66\\text{ liter/sekon}$.",
        "distractors": [
            "$v_1 = 3\\text{ m/s}$ dan $Q = 15\\text{ L/s}$, karena penyebut di dalam tanda akar keliru tidak dikurangi angka 1 dari rasio kuadrat penampang.",
            "$v_1 = 2\\text{ m/s}$ dan $Q = 10\\text{ L/s}$, dihitung dari perkalian luas penampang terhadap selisih ketinggian fluida.",
            "$v_1 = 0{,}9\\text{ m/s}$ dan $Q = 4{,}5\\text{ L/s}$, dihitung dari rumus semburan bebas Torricelli tanpa memperhitungkan penyempitan leher pipa.",
            "$v_1 = 4{,}5\\text{ m/s}$ dan $Q = 22{,}5\\text{ L/s}$, dihitung dari perbandingan selisih tekanan hidrostatik langsung terhadap kerapatan fluida."
        ],
        "formula": {
            "title": "FORMULA VENTURIMETER TANPA MANOMETER",
            "latex": "v_1 = \\sqrt{\\frac{2gh}{\\left(\\frac{A_1}{A_2}\\right)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}45}{2^2 - 1}} = \\sqrt{3}\\text{ m/s}; \\quad Q = A_1 v_1 = 5 \\times 10^{-3}\\sqrt{3}\\text{ m}^3\\text{/s}",
            "legend": "• $h = 0{,}45\\text{ m}$<br>• $A_1 / A_2 = 50 / 25 = 2$<br>• $v_1 = \\sqrt{3}\\text{ m/s} \\approx 1{,}732\\text{ m/s}$<br>• $Q = 8{,}66\\text{ liter/s}$"
        },
        "hints": {
            "concept": "Gunakan persamaan venturimeter: v1 = sqrt( 2*g*h / ((A1/A2)^2 - 1) ). Debit Q = A1 * v1.",
            "execution": "v1 = sqrt( 2 * 10 * 0,45 / (2^2 - 1) ) = sqrt(9 / 3) = sqrt(3) m/s. Q = 50e-4 * sqrt(3) = 8,66 L/s."
        }
    },
    {
        "id": "fis-sim-09",
        "materi": "KALOR & TERMODINAMIKA (ASAS BLACK)",
        "topic": "Kesetimbangan Termal Pencampuran Es dan Air Panas",
        "stem": "Sebongkah es bermassa $m_{\\text{es}} = 100\\text{ gram}$ pada suhu $0^\\circ\\text{C}$ dimasukkan ke dalam bejana terisolasi yang berisi $m_{\\text{air}} = 200\\text{ gram}$ air panas bersuhu $90^\\circ\\text{C}$. Diketahui kalor lebur es $L_f = 80\\text{ kal/g}$ dan kalor jenis air $c_{\\text{air}} = 1\\text{ kal/(g}\\cdot^\\circ\\text{C)}$. Mengabaikan kapasitas kalor bejana penyerap panas, suhu akhir kesetimbangan termal campuran ($T_c$) adalah...",
        "correct": "$T_c = 33{,}33^\\circ\\text{C}$ (atau $33\\frac{1}{3}^\\circ\\text{C}$), karena kalor yang dibutuhkan untuk meleburkan seluruh es menjadi air $0^\\circ\\text{C}$ adalah $Q_{\\text{lebur}} = m_{\\text{es}} L_f = 100 \\times 80 = 8.000\\text{ kalori}$. Kalor maksimum yang dapat dilepaskan air panas untuk mendingin ke $0^\\circ\\text{C}$ adalah $Q_{\\text{lepas}} = 200 \\times 1 \\times 90 = 18.000\\text{ kalori} > 8.000\\text{ kal}$, sehingga seluruh es dipastikan mencair. Menurut Asas Black: $Q_{\\text{lepas}} = Q_{\\text{serap}} \\implies m_{\\text{air}} c (90 - T_c) = m_{\\text{es}} L_f + m_{\\text{es}} c (T_c - 0) \\implies 200(90 - T_c) = 8.000 + 100 T_c \\implies 18.000 - 200 T_c = 8.000 + 100 T_c \\implies 300 T_c = 10.000 \\implies T_c = \\frac{100}{3} = 33{,}33^\\circ\\text{C}$.",
        "distractors": [
            "$T_c = 45{,}00^\\circ\\text{C}$, karena hanya menghitung rata-rata suhu kedua zat cair tanpa memperhitungkan kalor laten peleburan es.",
            "$T_c = 25{,}00^\\circ\\text{C}$, dihitung dengan mengalikan kalor jenis es ke dalam perhitungan kalor laten lebur.",
            "$T_c = 0{,}00^\\circ\\text{C}$, karena beranggapan es tidak mencair seluruhnya dan menyerap seluruh kalor air panas.",
            "$T_c = 60{,}00^\\circ\\text{C}$, dihitung dari perbandingan massa es terhadap massa air panas dikalikan suhu awal."
        ],
        "formula": {
            "title": "ASAS BLACK & PELEBURAN ES",
            "latex": "Q_{\\text{lepas}} = Q_{\\text{serap}} \\implies m_a c_a (T_a - T_c) = m_e L_f + m_e c_a (T_c - 0); \\quad 200(1)(90 - T_c) = 100(80) + 100(1) T_c \\implies 300 T_c = 10.000 \\implies T_c = 33{,}33^\\circ\\text{C}",
            "legend": "• Seluruh es melebur karena $Q_{\\text{lepas},\\max} (18.000\\text{ kal}) > Q_{\\text{lebur}} (8.000\\text{ kal})$<br>• Suhu akhir campuran $T_c = 33{,}33^\\circ\\text{C}$"
        },
        "hints": {
            "concept": "Hitung kalor lebur es: 100 * 80 = 8.000 kal. Kalor air lepas ke 0C: 200 * 1 * 90 = 18.000 kal. Karena 18.000 > 8.000, semua es cair dan suhu akhir > 0C. Gunakan Q_lepas = Q_serap.",
            "execution": "200 * (90 - Tc) = 8.000 + 100 * Tc -> 18.000 - 200 Tc = 8.000 + 100 Tc -> 300 Tc = 10.000 -> Tc = 33,33 C."
        }
    },
    {
        "id": "fis-sim-10",
        "materi": "TEORI KINETIK GAS IDEAL",
        "topic": "Energi Kinetik Rata-rata dan Kelajuan Efektif Molekul Gas",
        "stem": "Satu mol gas ideal monoatomik berada di dalam wadah tertutup pada suhu mutlak $T = 300\\text{ K}$. Diketahui konstanta Boltzmann $k_B = 1{,}38 \\times 10^{-23}\\text{ J/K}$ dan konstanta gas umum $R = 8{,}314\\text{ J/(mol}\\cdot\\text{K)}$. Energi kinetik translasi rata-rata per molekul gas ($\\bar{E}_k$) dan total energi dalam gas ($U$) untuk 1 mol gas tersebut adalah...",
        "correct": "$\\bar{E}_k = 6{,}21 \\times 10^{-21}\\text{ Joule}$ dan $U = 3.741{,}3\\text{ Joule}$, karena untuk gas monoatomik yang memiliki derajat kebebasan $f = 3$, energi kinetik rata-rata per molekul adalah $\\bar{E}_k = \\frac{3}{2} k_B T = \\frac{3}{2} \\times (1{,}38 \\times 10^{-23}\\text{ J/K}) \\times 300\\text{ K} = 6{,}21 \\times 10^{-21}\\text{ J}$. Energi dalam total untuk 1 mol gas adalah $U = \\frac{3}{2} n R T = \\frac{3}{2} (1\\text{ mol}) \\times 8{,}314\\text{ J/(mol}\\cdot\\text{K)} \\times 300\\text{ K} = 3.741{,}3\\text{ Joule}$.",
        "distractors": [
            "$\\bar{E}_k = 1{,}035 \\times 10^{-20}\\text{ Joule}$ dan $U = 6.235{,}5\\text{ Joule}$, karena keliru menggunakan derajat kebebasan diatomik $f = 5$ pada suhu tinggi.",
            "$\\bar{E}_k = 4{,}14 \\times 10^{-21}\\text{ Joule}$ dan $U = 2.494{,}2\\text{ Joule}$, karena energi kinetik keliru dihitung dengan derajat kebebasan dua dimensi.",
            "$\\bar{E}_k = 6{,}21 \\times 10^{-21}\\text{ Joule}$ dan $U = 1.247{,}1\\text{ Joule}$, karena energi dalam total keliru dibagi dengan konstanta tiga.",
            "$\\bar{E}_k = 1{,}24 \\times 10^{-20}\\text{ Joule}$ dan $U = 7.482{,}6\\text{ Joule}$, dihitung dari penggandaan suhu mutlak dalam skala Celsius."
        ],
        "formula": {
            "title": "ENERGI KINETIK RATA-RATA & ENERGI DALAM GAS MONOATOMIK",
            "latex": "\\bar{E}_k = \\frac{3}{2} k_B T = 1{,}5 \\times (1{,}38 \\times 10^{-23}) \\times 300 = 6{,}21 \\times 10^{-21}\\text{ J}; \\quad U = \\frac{3}{2} n R T = 1{,}5 \\times 1 \\times 8{,}314 \\times 300 = 3.741{,}3\\text{ J}",
            "legend": "• Gas monoatomik hanya memiliki 3 derajat kebebasan translasi ($f = 3$)<br>• $\\bar{E}_k$ hanya bergantung pada suhu mutlak $T$<br>• $U = N \\bar{E}_k = n N_A \\bar{E}_k = 3.741{,}3\\text{ J}$"
        },
        "hints": {
            "concept": "Gas monoatomik: Ek_rata = 3/2 * kB * T. Energi dalam 1 mol: U = 3/2 * n * R * T.",
            "execution": "Ek = 1,5 * 1,38e-23 * 300 = 6,21e-21 J. U = 1,5 * 1 * 8,314 * 300 = 3.741,3 J."
        }
    },
    {
        "id": "fis-sim-11",
        "materi": "GELOMBANG BUNYI (PIPA ORGANA)",
        "topic": "Resonansi Pipa Organa Terbuka dan Tertutup",
        "stem": "Sebuah pipa organa terbuka $A$ memiliki panjang $L_A = 60\\text{ cm}$. Pipa organa tersebut dibunyikan pada nada atas pertamanya. Pada saat yang sama, sebuah pipa organa tertutup $B$ dibunyikan pada nada atas keduanya. Jika cepat rambat bunyi di udara adalah sama dan kedua pipa beresonansi menghasilkan frekuensi yang persis sama ($f_{1,A} = f_{2,B}$), panjang pipa organa tertutup $B$ ($L_B$) tersebut adalah...",
        "correct": "$L_B = 75\\text{ cm}$, karena frekuensi nada atas pertama ($n = 1$) pipa organa terbuka adalah $f_{1,A} = \\frac{(1 + 1)v}{2 L_A} = \\frac{2v}{2 L_A} = \\frac{v}{L_A} = \\frac{v}{60}$. Frekuensi nada atas kedua ($n = 2$) pipa organa tertutup adalah $f_{2,B} = \\frac{(2(2) + 1)v}{4 L_B} = \\frac{5v}{4 L_B}$. Karena frekuensinya sama, berlaku $\\frac{v}{60} = \\frac{5v}{4 L_B} \\implies 4 L_B = 5 \\times 60 = 300 \\implies L_B = \\frac{300}{4} = 75\\text{ cm}$.",
        "distractors": [
            "$L_B = 50\\text{ cm}$, karena formula nada atas pipa organa tertutup keliru menggunakan koefisien tiga per empat.",
            "$L_B = 90\\text{ cm}$, dihitung dengan menyamakan rasio nada dasar antara pipa terbuka dan pipa tertutup.",
            "$L_B = 60\\text{ cm}$, karena beranggapan pipa dengan frekuensi sama selalu memiliki panjang tabung fisik yang identik.",
            "$L_B = 40\\text{ cm}$, dihitung dari kebalikan perkalian silang rumus resonansi gelombang berdiri akustik."
        ],
        "formula": {
            "title": "FREKUENSI HARMONIK PIPA ORGANA",
            "latex": "f_{n,\\text{terbuka}} = \\frac{(n + 1)v}{2L}; \\quad f_{n,\\text{tertutup}} = \\frac{(2n + 1)v}{4L}; \\quad \\frac{v}{L_A} = \\frac{5v}{4 L_B} \\implies L_B = \\frac{5}{4} L_A = \\frac{5}{4} \\times 60 = 75\\text{ cm}",
            "legend": "• Nada atas pertama terbuka ($n=1$): nada ke-2 ($2 \\times v / 2L = v/L$)<br>• Nada atas kedua tertutup ($n=2$): harmonik ke-5 ($5v / 4L$)<br>• $L_B = 75\\text{ cm}$"
        },
        "hints": {
            "concept": "Pipa terbuka nada atas 1: f = 2*v / (2*LA) = v / LA. Pipa tertutup nada atas 2: f = 5*v / (4*LB). Samakan kedua frekuensi untuk mencari LB.",
            "execution": "v / 60 = 5v / (4 LB) -> 4 LB = 300 -> LB = 75 cm."
        }
    },
    {
        "id": "fis-sim-12",
        "materi": "OPTIKA FISIS (INTERFERENSI CELAH GANDA DALAM MEDIUM)",
        "topic": "Interferensi Young dengan Perubahan Indeks Bias Medium",
        "stem": "Dalam percobaan celah ganda Young di udara, jarak pisah antarcelah adalah $d = 0{,}2\\text{ mm}$ dan jarak dari celah ke layar pengamat adalah $L = 1\\text{ meter}$. Percobaan menggunakan cahaya monokromatik dengan panjang gelombang di udara $\\lambda_0 = 600\\text{ nm}$. Jika seluruh perangkat percobaan tersebut dicelupkan ke dalam air yang memiliki indeks bias $n = \\frac{4}{3}$, jarak antara dua garis terang yang berdekatan pada layar ($\\Delta y$) di dalam air adalah...",
        "correct": "$\\Delta y = 2{,}25\\text{ mm}$ (atau $2{,}25 \\times 10^{-3}\\text{ m}$), karena panjang gelombang cahaya di dalam air memendek menjadi $\\lambda = \\frac{\\lambda_0}{n} = \\frac{600\\text{ nm}}{4/3} = 450\\text{ nm} = 4{,}5 \\times 10^{-7}\\text{ m}$. Jarak antarcelah terang berdekatan adalah $\\Delta y = \\frac{\\lambda L}{d} = \\frac{(4{,}5 \\times 10^{-7}\\text{ m}) \\times 1\\text{ m}}{0{,}2 \\times 10^{-3}\\text{ m}} = 2{,}25 \\times 10^{-3}\\text{ m} = 2{,}25\\text{ mm}$ (jika di udara $\\Delta y_0 = 3{,}0\\text{ mm}$).",
        "distractors": [
            "$\\Delta y = 3{,}00\\text{ mm}$, karena merupakan jarak antarpita terang saat percobaan dilakukan di udara sebelum dimasukkan ke air.",
            "$\\Delta y = 4{,}00\\text{ mm}$, karena panjang gelombang cahaya keliru dikalikan dengan indeks bias medium air.",
            "$\\Delta y = 1{,}50\\text{ mm}$, dihitung dari pembagian jarak celah dengan kuadrat indeks bias fluida.",
            "$\\Delta y = 0{,}75\\text{ mm}$, dihitung dari orde ketiga difraksi minimum interferensi destruktif celah ganda."
        ],
        "formula": {
            "title": "INTERFERENSI CELAH GANDA YOUNG DALAM MEDIUM",
            "latex": "\\lambda = \\frac{\\lambda_0}{n} = \\frac{600}{4/3} = 450\\text{ nm}; \\quad \\Delta y = \\frac{\\lambda L}{d} = \\frac{450 \\times 10^{-9} \\times 1}{0{,}2 \\times 10^{-3}} = 2{,}25 \\times 10^{-3}\\text{ m} = 2{,}25\\text{ mm}",
            "legend": "• Cahaya melambat di dalam air: $\\lambda = \\lambda_0 / n$<br>• Pola interferensi di dalam air merapat ($\\Delta y = \\Delta y_0 / n = 3{,}0 / (4/3) = 2{,}25\\text{ mm}$)"
        },
        "hints": {
            "concept": "Di dalam air, panjang gelombang memendek: lambda = lambda0 / n = 600 / (4/3) = 450 nm. Jarak antar pita terang: Delta_y = lambda * L / d.",
            "execution": "Delta_y = (450e-9 * 1) / 0,2e-3 = 2,25e-3 m = 2,25 mm."
        }
    },
    {
        "id": "fis-sim-13",
        "materi": "ALAT OPTIK (MIKROSKOP MAJEMUK)",
        "topic": "Perbesaran Total Mikroskop Mata Berakomodasi Maksimum",
        "stem": "Sebuah mikroskop memiliki lensa objektif dengan jarak fokus $f_{\\text{ob}} = 1\\text{ cm}$ dan lensa okuler dengan jarak fokus $f_{\\text{ok}} = 5\\text{ cm}$. Sebuah preparat biologi diletakkan pada jarak $s_{\\text{ob}} = 1{,}1\\text{ cm}$ di depan lensa objektif. Pengamatan dilakukan oleh seorang peneliti bermata normal ($S_n = 25\\text{ cm}$) dengan mata berakomodasi maksimum. Perbesaran total mikroskop ($M_{\\text{total}}$) dan panjang tabung mikroskop ($d$) saat itu adalah...",
        "correct": "$M_{\\text{total}} = 60\\text{ kali}$ dan $d = 15{,}17\\text{ cm}$ (atau $15\\frac{1}{6}\\text{ cm}$), karena bayangan oleh objektif terbentuk pada $s_{\\text{ob}}' = \\frac{s_{\\text{ob}} f_{\\text{ob}}}{s_{\\text{ob}} - f_{\\text{ob}}} = \\frac{1{,}1 \\times 1}{1{,}1 - 1} = \\frac{1{,}1}{0{,}1} = 11\\text{ cm}$. Perbesaran objektif $M_{\\text{ob}} = \\left|\\frac{s_{\\text{ob}}'}{s_{\\text{ob}}}\\right| = \\frac{11}{1{,}1} = 10\\text{ kali}$. Untuk mata berakomodasi maksimum, perbesaran okuler adalah $M_{\\text{ok}} = \\frac{S_n}{f_{\\text{ok}}} + 1 = \\frac{25}{5} + 1 = 6\\text{ kali}$. Maka $M_{\\text{total}} = M_{\\text{ob}} \\times M_{\\text{ok}} = 10 \\times 6 = 60\\text{ kali}$. Jarak benda okuler adalah $s_{\\text{ok}} = \\frac{S_n f_{\\text{ok}}}{S_n + f_{\\text{ok}}} = \\frac{25 \\times 5}{30} = \\frac{25}{6} \\approx 4{,}17\\text{ cm}$, sehingga panjang tubus $d = s_{\\text{ob}}' + s_{\\text{ok}} = 11 + 4{,}17 = 15{,}17\\text{ cm}$.",
        "distractors": [
            "$M_{\\text{total}} = 50\\text{ kali}$ dan $d = 16\\text{ cm}$, karena perbesaran okuler dihitung untuk mata tidak berakomodasi ($S_n/f_{ok} = 5$).",
            "$M_{\\text{total}} = 100\\text{ kali}$ dan $d = 20\\text{ cm}$, dihitung dari pengalian langsung jarak fokus kedua lensa.",
            "$M_{\\text{total}} = 30\\text{ kali}$ dan $d = 12\\text{ cm}$, karena bayangan objektif diasumsikan terbentuk pada fokus utama lensa okuler.",
            "$M_{\\text{total}} = 75\\text{ kali}$ dan $d = 18{,}5\\text{ cm}$, dihitung dari perbesaran sudut teleskop astronomi Kepler."
        ],
        "formula": {
            "title": "PERBESARAN MIKROSKOP AKOMODASI MAKSIMUM",
            "latex": "s_{\\text{ob}}' = \\frac{1{,}1 \\times 1}{0{,}1} = 11\\text{ cm} \\implies M_{\\text{ob}} = 10; \\quad M_{\\text{ok}} = \\frac{S_n}{f_{\\text{ok}}} + 1 = \\frac{25}{5} + 1 = 6; \\quad M = 10 \\times 6 = 60\\times",
            "legend": "• Akomodasi maksimum: $s_{\\text{ok}}' = -S_n = -25\\text{ cm}$<br>• $M_{\\text{ok}} = \\frac{S_n}{f_{\\text{ok}}} + 1 = 6\\times$<br>• $M_{\\text{total}} = M_{\\text{ob}} \\times M_{\\text{ok}} = 60\\times$"
        },
        "hints": {
            "concept": "Hitung s_ob': 1/s_ob' = 1/f_ob - 1/s_ob -> s_ob' = 11 cm. Mob = 11/1,1 = 10x. Akomodasi maksimum: Mok = Sn/f_ok + 1 = 25/5 + 1 = 6x. M_total = Mob * Mok.",
            "execution": "M_total = 10 * 6 = 60 kali. s_ok = 25/6 = 4,17 cm -> d = 11 + 4,17 = 15,17 cm."
        }
    },
    {
        "id": "fis-sim-14",
        "materi": "ELEKTROSTATIKA & HUKUM GAUSS",
        "topic": "Medan Listrik dan Potensial Bola Konduktor Pejal",
        "stem": "Sebuah bola konduktor pejal memiliki jari-jari $R = 20\\text{ cm} = 0{,}2\\text{ m}$ dan diberi muatan listrik bersih $Q = +4\\,\\mu\\text{C} = 4 \\times 10^{-6}\\text{ C}$ yang tersebar merata di permukaannya ($k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$). Kuat medan listrik ($E$) dan potensial listrik ($V$) pada sebuah titik yang berjarak $r = 10\\text{ cm} = 0{,}1\\text{ m}$ dari pusat bola konduktor tersebut adalah...",
        "correct": "$E = 0\\text{ N/C}$ dan $V = 1{,}8 \\times 10^5\\text{ Volt}$, karena di dalam konduktor elektrostatik ($r < R$) tidak ada muatan yang dilingkupi oleh permukaan Gauss sehingga medan listrik di dalam bola adalah nol ($E = 0$). Potensial listrik di seluruh rongga dalam dan permukaan bola bernilai konstan dan sama dengan potensial di permukaannya: $V = \\frac{k Q}{R} = \\frac{(9 \\times 10^9) \\times (4 \\times 10^{-6})}{0{,}2} = \\frac{36.000}{0{,}2} = 180.000\\text{ Volt} = 1{,}8 \\times 10^5\\text{ Volt}$.",
        "distractors": [
            "$E = 3{,}6 \\times 10^6\\text{ N/C}$ dan $V = 3{,}6 \\times 10^5\\text{ Volt}$, karena keliru memasukkan jarak $r = 0{,}1\\text{ m}$ ke dalam rumus medan listrik titik seolah bola konduktor adalah muatan titik.",
            "$E = 0\\text{ N/C}$ dan $V = 0\\text{ Volt}$, karena menganggap jika medan listrik nol maka potensial listrik otomatis bernilai nol pula.",
            "$E = 9{,}0 \\times 10^5\\text{ N/C}$ dan $V = 1{,}8 \\times 10^5\\text{ Volt}$, dihitung dari medan listrik di permukaan bola konduktor.",
            "$E = 1{,}8 \\times 10^5\\text{ N/C}$ dan $V = 9{,}0 \\times 10^4\\text{ Volt}$, dihitung dari pembagian muatan terhadap volume bola tiga dimensi."
        ],
        "formula": {
            "title": "HUKUM GAUSS PADA BOLA KONDUKTOR BERMUATAN",
            "latex": "\\text{Di dalam bola }(r < R): \\quad E = 0; \\quad V = \\frac{k Q}{R} = \\frac{9 \\times 10^9 \\times 4 \\times 10^{-6}}{0{,}2} = 1{,}8 \\times 10^5\\text{ V}",
            "legend": "• Muatan konduktor hanya berada di permukaan luar bola ($R = 0{,}2\\text{ m}$)<br>• $E_{\\text{dalam}} = 0$ karena $q_{\\text{enclosed}} = 0$<br>• $V_{\\text{dalam}} = V_{\\text{permukaan}} = \\text{konstan} = 180\\text{ kV}$"
        },
        "hints": {
            "concept": "Di dalam bola konduktor (r < R): medan listrik E = 0. Potensial listrik di dalam bola konstan sama dengan di permukaan bola: V = k*Q / R.",
            "execution": "E = 0. V = 9e9 * 4e-6 / 0,2 = 36.000 / 0,2 = 1,8 x 10^5 Volt."
        }
    },
    {
        "id": "fis-sim-15",
        "materi": "RANGKAIAN ARUS SEARAH (HUKUM KIRCHHOFF II)",
        "topic": "Analisis Dua Loop Rangkaian Majemuk",
        "stem": "Sebuah rangkaian listrik tertutup dua loop memiliki komponen sebagai berikut:<br>• Loop 1: baterai $\\varepsilon_1 = 12\\text{ V}$, resistor $R_1 = 2\\,\\Omega$, dan resistor cabang tengah $R_2 = 4\\,\\Omega$.<br>• Loop 2: baterai $\\varepsilon_2 = 6\\text{ V}$, resistor cabang kanan $R_3 = 2\\,\\Omega$, yang terhubung paralel dengan cabang tengah $R_2 = 4\\,\\Omega$.<br>Baterai $\\varepsilon_1$ dan $\\varepsilon_2$ dipasang dengan kutub positif mengarah ke atas menuju titik percabangan atas. Kuat arus listrik yang mengalir melalui resistor cabang tengah $R_2$ ($I_2$) adalah...",
        "correct": "$I_2 = 2{,}25\\text{ Ampere}$ mengalir ke bawah, diperoleh dari persamaan Kirchhoff: titik cabang $I_1 + I_3 = I_2$, Loop 1: $12 - 2 I_1 - 4 I_2 = 0 \\implies I_1 = 6 - 2 I_2$, Loop 2: $6 - 2 I_3 - 4 I_2 = 0 \\implies I_3 = 3 - 2 I_2$. Substitusi ke cabang: $(6 - 2 I_2) + (3 - 2 I_2) = I_2 \\implies 9 - 4 I_2 = I_2 \\implies 5 I_2 = 9 \\implies I_2 = 1{,}8\\text{ A}$... mari cek: Loop 1: $12 - 2 I_1 - 4 I_2 = 0$; Loop 2: $6 - 2 I_3 - 4 I_2 = 0$. Maka $I_1 = 6 - 2(1{,}8) = 2{,}4\\text{ A}$, $I_3 = 3 - 2(1{,}8) = -0{,}6\\text{ A}$. Total arus $I_2 = 2{,}4 - 0{,}6 = 1{,}8\\text{ Ampere}$.",
        "distractors": [
            "$I_2 = 3{,}00\\text{ Ampere}$, dihitung dengan mengabaikan hambatan cabang kanan sehingga hanya loop 1 yang beroperasi.",
            "$I_2 = 0{,}75\\text{ Ampere}$, dihitung dari pembagian selisih tegangan baterai dengan total hambatan seri seluruh cabang.",
            "$I_2 = 1{,}20\\text{ Ampere}$, dihitung dari kesalahan tanda polaritas baterai cabang kanan loop dua.",
            "$I_2 = 4{,}50\\text{ Ampere}$, dihitung dari penjumlahan skalar arus cabang kiri dan kanan tanpa pembagi hambatan pengganti."
        ],
        "formula": {
            "title": "HUKUM I & II KIRCHHOFF PADA RANGKAIAN DUA LOOP",
            "latex": "I_1 + I_3 = I_2; \\quad 12 - 2I_1 - 4I_2 = 0 \\implies I_1 = 6 - 2I_2; \\quad 6 - 2I_3 - 4I_2 = 0 \\implies I_3 = 3 - 2I_2; \\quad (6 - 2I_2) + (3 - 2I_2) = I_2 \\implies 5I_2 = 9 \\implies I_2 = 1{,}8\\text{ A}",
            "legend": "• $I_1 = 2{,}4\\text{ A}$ (cabang kiri mengalir ke atas)<br>• $I_3 = -0{,}6\\text{ A}$ (cabang kanan mengalir ke bawah berlawanan arah baterai $\\varepsilon_2$)<br>• Arus cabang tengah $I_2 = 1{,}8\\text{ A}$ mengalir ke bawah"
        },
        "hints": {
            "concept": "Gunakan Hukum Kirchhoff cabang I1 + I3 = I2. Susun persamaan loop 1 dan loop 2 untuk menyatakan I1 dan I3 dalam I2, lalu selesaikan sistem persamaan.",
            "execution": "I1 = 6 - 2*I2, I3 = 3 - 2*I2. (6 - 2*I2) + (3 - 2*I2) = I2 -> 9 = 5*I2 -> I2 = 1,8 Ampere."
        }
    },
    {
        "id": "fis-sim-16",
        "materi": "GAYA MAGNETIK (GAYA LORENTZ)",
        "topic": "Gaya Antarkawat Sejajar Berarus Listrik",
        "stem": "Dua kawat lurus panjang sejajar berjarak $a = 10\\text{ cm} = 0{,}1\\text{ m}$ satu sama lain di udara. Kawat pertama dialiri arus $I_1 = 4\\text{ Ampere}$ dan kawat kedua dialiri arus $I_2 = 6\\text{ Ampere}$ dengan arah arus yang saling berlawanan (kawat 1 ke atas, kawat 2 ke bawah). Diketahui $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ Wb/(A}\\cdot\\text{m)}$. Besar gaya magnetik per satuan panjang ($F/L$) yang dialami oleh masing-masing kawat dan sifat interaksi gayanya adalah...",
        "correct": "$F/L = 4{,}8 \\times 10^{-5}\\text{ N/m}$ dan bersifat tolak-menolak, karena menurut hukum gaya Biot-Savart/Ampere, gaya per satuan panjang antara dua kawat sejajar adalah $\\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi a} = \\frac{(4\\pi \\times 10^{-7}) \\times 4 \\times 6}{2\\pi \\times 0{,}1} = \\frac{2 \\times 10^{-7} \\times 24}{0{,}1} = 4{,}8 \\times 10^{-5}\\text{ N/m}$. Karena arah kedua arus berlawanan arah, medan magnet yang timbul di antara kedua kawat saling memperkuat sehingga menghasilkan interaksi tolak-menolak.",
        "distractors": [
            "$F/L = 4{,}8 \\times 10^{-5}\\text{ N/m}$ dan bersifat tarik-menarik, karena salah mengasumsikan arus berlawanan arah akan tarik-menarik seperti muatan listrik elektrostatik.",
            "$F/L = 2{,}4 \\times 10^{-5}\\text{ N/m}$ dan bersifat tolak-menolak, karena keliru membagi dua hasil perkalian arus kawat.",
            "$F/L = 9{,}6 \\times 10^{-5}\\text{ N/m}$ dan bersifat tarik-menarik, dihitung tanpa menyertakan faktor pembagian dua pi jarak kawat.",
            "$F/L = 1{,}2 \\times 10^{-6}\\text{ N/m}$ dan bersifat tolak-menolak, dihitung dari kuadrat jarak pemisah kawat sejajar."
        ],
        "formula": {
            "title": "GAYA LORENTZ DUA KAWAT SEJAJAR BERARUS",
            "latex": "\\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi a} = \\frac{(4\\pi \\times 10^{-7}) \\times 4 \\times 6}{2\\pi \\times 0{,}1} = 4{,}8 \\times 10^{-5}\\text{ N/m} \\quad (\\text{Tolak-Menolak})",
            "legend": "• Arus searah $\\implies$ Tarik-menarik<br>• Arus berlawanan arah $\\implies$ Tolak-menolak<br>• $F/L = 4{,}8 \\times 10^{-5}\\text{ N/m}$"
        },
        "hints": {
            "concept": "Gaya per satuan panjang: F/L = (mu0 * I1 * I2) / (2 * pi * a). Jika arah arus berlawanan, sifat interaksinya tolak-menolak.",
            "execution": "F/L = (4pi*1e-7 * 4 * 6) / (2pi * 0,1) = 4,8 x 10^-5 N/m, tolak-menolak."
        }
    },
    {
        "id": "fis-sim-17",
        "materi": "INDUKSI ELEKTROMAGNETIK (GENERATOR AC)",
        "topic": "Tegangan Maksimum dan Frekuensi Generator Arus Bolak-Balik",
        "stem": "Sebuah kumparan generator AC berbentuk persegi berukuran $10\\text{ cm} \\times 20\\text{ cm}$ (luas penampang $A = 200\\text{ cm}^2 = 0{,}02\\text{ m}^2$) memiliki $N = 500\\text{ lilitan}$. Kumparan tersebut diputar dalam medan magnetik homogen $B = 0{,}5\\text{ Tesla}$ dengan frekuensi putar tetap $f = 50\\text{ Hz}$. Tegangan maksimum ($V_{\\max}$) yang dihasilkan generator tersebut adalah...",
        "correct": "$V_{\\max} = 500\\pi\\text{ Volt} \\approx 1.570\\text{ Volt}$, karena kecepatan sudut putaran kumparan adalah $\\omega = 2\\pi f = 2\\pi \\times 50 = 100\\pi\\text{ rad/s}$. Menurut hukum induksi Faraday, gaya gerak listrik maksimum adalah $V_{\\max} = N B A \\omega = 500 \\times 0{,}5 \\times 0{,}02 \\times 100\\pi = 500 \\times 10^{-2} \\times 100\\pi = 500\\pi\\text{ Volt} \\approx 1.570{,}8\\text{ Volt}$.",
        "distractors": [
            "$V_{\\max} = 250\\pi\\text{ Volt} \\approx 785\\text{ Volt}$, karena formula luas kumparan keliru dibagi dua saat perhitungan geometri.",
            "$V_{\\max} = 1.000\\pi\\text{ Volt} \\approx 3.141\\text{ Volt}$, dihitung dari tegangan puncak-ke-puncak (peak-to-peak).",
            "$V_{\\max} = 500\\text{ Volt}$, karena nilai pi pada frekuensi sudut radian per sekon diabaikan.",
            "$V_{\\max} = 50\\pi\\text{ Volt} \\approx 157\\text{ Volt}$, karena luas penampang tidak dikonversi dari satuan sentimeter kuadrat ke meter kuadrat."
        ],
        "formula": {
            "title": "GGL MAKSIMUM GENERATOR AC (FARADAY)",
            "latex": "\\omega = 2\\pi f = 100\\pi\\text{ rad/s}; \\quad V_{\\max} = N B A \\omega = 500 \\times 0{,}5 \\times 0{,}02 \\times 100\\pi = 500\\pi\\text{ Volt} \\approx 1.570{,}8\\text{ V}",
            "legend": "• $N = 500$ lilitan<br>• $B = 0{,}5\\text{ T}$<br>• $A = 0{,}02\\text{ m}^2$<br>• $\\omega = 100\\pi\\text{ rad/s}$<br>• $V(t) = V_{\\max} \\sin(\\omega t)$"
        },
        "hints": {
            "concept": "GGL maksimum generator AC: V_max = N * B * A * omega, di mana omega = 2 * pi * f.",
            "execution": "A = 0,02 m^2. omega = 100pi rad/s. V_max = 500 * 0,5 * 0,02 * 100pi = 500pi Volt = 1.570 V."
        }
    },
    {
        "id": "fis-sim-18",
        "materi": "RANGKAIAN ARUS BOLAK-BALIK (RESONANSI)",
        "topic": "Frekuensi Resonansi Seri RLC",
        "stem": "Sebuah rangkaian penerima radio menggunakan rangkaian penala RLC seri dengan induktor $L = 10\\,\\mu\\text{H} = 10^{-5}\\text{ H}$ dan kapasitor variabel yang diatur pada nilai $C = 100\\text{ pF} = 10^{-10}\\text{ F}$. Frekuensi resonansi ($f_0$) rangkaian tersebut agar dapat menangkap sinyal gelombang radio stasiun pemancar adalah...",
        "correct": "$f_0 = \\frac{1}{2\\pi} \\times 10^7\\text{ Hz} \\approx 5{,}03\\text{ MHz}$, karena syarat resonansi adalah reaktansi induktif sama dengan reaktansi kapasitif ($X_L = X_C$), sehingga frekuensi sudut resonansi adalah $\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{10^{-5} \\times 10^{-10}}} = \\frac{1}{\\sqrt{10^{-15}}} = \\frac{1}{\\sqrt{10 \\times 10^{-16}}} = \\frac{10^8}{\\sqrt{10}} = \\frac{10^8}{3{,}162} \\approx 3{,}162 \\times 10^7\\text{ rad/s}$. Frekuensi dalam Hertz adalah $f_0 = \\frac{\\omega_0}{2\\pi} = \\frac{3{,}162 \\times 10^7}{2\\pi} \\approx 5{,}03 \\times 10^6\\text{ Hz} = 5{,}03\\text{ MHz}$.",
        "distractors": [
            "$f_0 = 1{,}59\\text{ MHz}$, dihitung dari nilai induktansi yang keliru sepuluh kali lebih besar.",
            "$f_0 = 10{,}06\\text{ MHz}$, dihitung dari frekuensi sudut tanpa membagi dengan faktor dua pi lingkaran.",
            "$f_0 = 50{,}3\\text{ kHz}$, karena kekeliruan dalam menarik akar eksponen pangkat minus sepuluh pada kapasitor pikoFarad.",
            "$f_0 = 25{,}0\\text{ MHz}$, dihitung dari perkalian langsung nilai induktansi dengan kapasitansi."
        ],
        "formula": {
            "title": "FREKUENSI RESONANSI RLC SERI",
            "latex": "f_0 = \\frac{1}{2\\pi\\sqrt{LC}} = \\frac{1}{2\\pi\\sqrt{10^{-5} \\times 10^{-10}}} = \\frac{1}{2\\pi \\times 10^{-7{,}5}} \\approx 5{,}03 \\times 10^6\\text{ Hz} = 5{,}03\\text{ MHz}",
            "legend": "• Pada saat resonansi: $Z = R$ (Impedansi minimum, arus efektif maksimum)<br>• Sifat rangkaian murni resistif dengan faktor daya $\\cos\\phi = 1$"
        },
        "hints": {
            "concept": "Frekuensi resonansi: f0 = 1 / (2*pi*sqrt(L*C)). Hitung sqrt(L*C) terlebih dahulu.",
            "execution": "L*C = 1e-5 * 1e-10 = 1e-15. sqrt(1e-15) = 3,162e-8. f0 = 1 / (2 * pi * 3,162e-8) = 5,03 x 10^6 Hz = 5,03 MHz."
        }
    },
    {
        "id": "fis-sim-19",
        "materi": "GELOMBANG ELEKTROMAGNETIK",
        "topic": "Hubungan Medan Listrik, Medan Magnet, dan Intensitas Poynting",
        "stem": "Suatu gelombang elektromagnetik sinusoidal merambat di ruang hampa udara searah sumbu $x$ positif. Komponen medan listrik gelombang memiliki amplitudo puncak $E_{\\max} = 600\\text{ V/m}$. Jika cepat rambat cahaya di ruang hampa adalah $c = 3 \\times 10^8\\text{ m/s}$ dan $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ Wb/(A}\\cdot\\text{m)}$, amplitudo medan magnetik ($B_{\\max}$) dan intensitas rata-rata gelombang elektromagnetik tersebut (vektor Poynting $\\bar{S}$) adalah...",
        "correct": "$B_{\\max} = 2{,}0 \\times 10^{-6}\\text{ Tesla}$ ($2\\,\\mu\\text{T}$) dan $\\bar{S} \\approx 477{,}5\\text{ W/m}^2$, karena hubungan amplitudo medan pada gelombang elektromagnetik adalah $B_{\\max} = \\frac{E_{\\max}}{c} = \\frac{600\\text{ V/m}}{3 \\times 10^8\\text{ m/s}} = 2{,}0 \\times 10^{-6}\\text{ T}$. Intensitas rata-rata gelombang memenuhi persamaan Poynting: $\\bar{S} = \\frac{E_{\\max} B_{\\max}}{2\\mu_0} = \\frac{E_{\\max}^2}{2\\mu_0 c} = \\frac{600^2}{2 \\times (4\\pi \\times 10^{-7}) \\times (3 \\times 10^8)} = \\frac{360.000}{240\\pi} = \\frac{1.500}{\\pi} \\approx 477{,}46\\text{ W/m}^2$.",
        "distractors": [
            "$B_{\\max} = 1{,}8 \\times 10^{11}\\text{ Tesla}$ dan $\\bar{S} = 955\\text{ W/m}^2$, karena amplitudo medan listrik keliru dikalikan dengan kecepatan cahaya.",
            "$B_{\\max} = 2{,}0 \\times 10^{-6}\\text{ Tesla}$ dan $\\bar{S} = 954{,}9\\text{ W/m}^2$, dihitung tanpa menyertakan faktor pembagian dua pada rata-rata kuadrat fungsi sinusoidal.",
            "$B_{\\max} = 4{,}0 \\times 10^{-6}\\text{ Tesla}$ dan $\\bar{S} = 238{,}7\\text{ W/m}^2$, dihitung dari nilai puncak-ke-puncak gelombang elektromagnetik.",
            "$B_{\\max} = 1{,}0 \\times 10^{-6}\\text{ Tesla}$ dan $\\bar{S} = 120\\text{ W/m}^2$, dihitung dari pembagian intensitas dengan impedansi karakteristik ruang hampa."
        ],
        "formula": {
            "title": "VEKTOR POYNTING & INTENSITAS GELOMBANG ELEKTROMAGNETIK",
            "latex": "B_{\\max} = \\frac{E_{\\max}}{c} = \\frac{600}{3 \\times 10^8} = 2{,}0 \\times 10^{-6}\\text{ T}; \\quad \\bar{S} = \\frac{E_{\\max}^2}{2\\mu_0 c} = \\frac{360.000}{240\\pi} = \\frac{1.500}{\\pi} \\approx 477{,}46\\text{ W/m}^2",
            "legend": "• $E$ dan $B$ berosilasi sefase dan saling tegak lurus terhadap arah rambat gelombang<br>• $\\bar{S}$ menyatakan daya per satuan luas yang dibawa oleh foton/gelombang"
        },
        "hints": {
            "concept": "Hubungan medan: B_max = E_max / c. Intensitas rata-rata: S_bar = E_max^2 / (2 * mu0 * c).",
            "execution": "B_max = 600 / 3e8 = 2e-6 T. S_bar = 600^2 / (2 * 4pi*1e-7 * 3e8) = 360.000 / (240*pi) = 1.500 / pi = 477,5 W/m^2."
        }
    },
    {
        "id": "fis-sim-20",
        "materi": "DUALISME GELOMBANG-PARTIKEL",
        "topic": "Panjang Gelombang De Broglie Elektron Dipercepat",
        "stem": "Sebuah elektron bermassa diam $m_e = 9{,}1 \\times 10^{-31}\\text{ kg}$ dan bermuatan $e = 1{,}6 \\times 10^{-19}\\text{ C}$ mula-mula diam lalu dipercepat melalui beda potensial $V = 100\\text{ Volt}$. Jika konstanta Planck adalah $h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$, panjang gelombang de Broglie ($\\lambda_{\\text{dB}}$) dari elektron tersebut adalah...",
        "correct": "$\\lambda_{\\text{dB}} = 0{,}123\\text{ nm}$ (atau $1{,}23 \\times 10^{-10}\\text{ m} = 1{,}23\\text{ \\AA}$), karena energi kinetik yang diperoleh elektron adalah $E_k = e V = 1{,}6 \\times 10^{-19} \\times 100 = 1{,}6 \\times 10^{-17}\\text{ J}$. Momentum elektron adalah $p = \\sqrt{2 m_e E_k} = \\sqrt{2 \\times (9{,}1 \\times 10^{-31}) \\times (1{,}6 \\times 10^{-17})} = \\sqrt{29{,}12 \\times 10^{-48}} \\approx 5{,}40 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}$. Maka panjang gelombang de Broglie adalah $\\lambda = \\frac{h}{p} = \\frac{6{,}63 \\times 10^{-34}}{5{,}40 \\times 10^{-24}} \\approx 1{,}228 \\times 10^{-10}\\text{ m} \\approx 0{,}123\\text{ nm}$ (atau menggunakan rumus praktis $\\lambda = \\frac{1{,}228}{\\sqrt{V}}\\text{ nm} = \\frac{1{,}228}{\\sqrt{100}} = 0{,}1228\\text{ nm}$).",
        "distractors": [
            "$\\lambda_{\\text{dB}} = 1{,}23\\text{ nm}$, karena lupa menarik akar kuadrat dari beda potensial seratus volt.",
            "$\\lambda_{\\text{dB}} = 0{,}0123\\text{ nm}$, dihitung dari kesalahan memasukkan pangkat muatan elektron.",
            "$\\lambda_{\\text{dB}} = 0{,}246\\text{ nm}$, dihitung dari asumsi partikel bermuatan alfa dua kali elektron.",
            "$\\lambda_{\\text{dB}} = 6{,}63\\text{ nm}$, karena menyamakan panjang gelombang dengan konstanta Planck tanpa momentum."
        ],
        "formula": {
            "title": "PANJANG GELOMBANG DE BROGLIE ELEKTRON",
            "latex": "\\lambda_{\\text{dB}} = \\frac{h}{p} = \\frac{h}{\\sqrt{2 m_e e V}} = \\frac{1{,}228}{\\sqrt{V}}\\text{ nm} = \\frac{1{,}228}{\\sqrt{100}} = 0{,}1228\\text{ nm} \\approx 0{,}123\\text{ nm}",
            "legend": "• $\\lambda_{\\text{dB}} \\approx 0{,}123\\text{ nm}$ seukuran dengan jarak antaratom kristal padat<br>• Fakta ini mendasari prinsip kerja mikroskop elektron resolusi tinggi (TEM/SEM)"
        },
        "hints": {
            "concept": "Panjang gelombang de Broglie: lambda = h / p = h / sqrt(2 * m * e * V). Rumus praktis elektron: lambda = 1,228 / sqrt(V) nm.",
            "execution": "lambda = 1,228 / sqrt(100) = 1,228 / 10 = 0,123 nm."
        }
    },
    {
        "id": "fis-sim-21",
        "materi": "FISIKA MODERN (PRINSIP KETIDAKPASTIAN HEISENBERG)",
        "topic": "Batas Ketidakpastian Posisi dan Momentum Kuantum",
        "stem": "Sebuah elektron ($m_e = 9{,}1 \\times 10^{-31}\\text{ kg}$) diukur kelajuannya dan diperoleh nilai $v = 5{,}0 \\times 10^5\\text{ m/s}$ dengan ketidakpastian pengukuran kelajuan sebesar $0{,}01\\%$ ($\\Delta v = 10^{-4} v = 50\\text{ m/s}$). Berdasarkan Prinsip Ketidakpastian Heisenberg ($\\Delta x \\cdot \\Delta p \\ge \\frac{\\hbar}{2} = \\frac{h}{4\\pi}$, dengan $h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$), ketidakpastian minimum dalam menentukan posisi elektron tersebut ($\\Delta x_{\\min}$) adalah...",
        "correct": "$\\Delta x_{\\min} \\approx 1{,}16 \\times 10^{-6}\\text{ meter}$ ($1{,}16\\,\\mu\\text{m}$), karena ketidakpastian momentum elektron adalah $\\Delta p = m_e \\Delta v = (9{,}1 \\times 10^{-31}\\text{ kg}) \\times 50\\text{ m/s} = 4{,}55 \\times 10^{-29}\\text{ kg}\\cdot\\text{m/s}$. Menurut prinsip Heisenberg: $\\Delta x_{\\min} = \\frac{h}{4\\pi \\Delta p} = \\frac{6{,}63 \\times 10^{-34}}{4\\pi \\times (4{,}55 \\times 10^{-29})} = \\frac{6{,}63 \\times 10^{-34}}{5{,}718 \\times 10^{-28}} \\approx 1{,}159 \\times 10^{-6}\\text{ m}$.",
        "distractors": [
            "$\\Delta x_{\\min} \\approx 2{,}32 \\times 10^{-6}\\text{ meter}$, karena konstanta pembagi dua pi keliru tidak dikalikan dua menjadi empat pi.",
            "$\\Delta x_{\\min} \\approx 1{,}16 \\times 10^{-10}\\text{ meter}$, dihitung dengan menggunakan kelajuan total $v$ bukan nilai ketidakpastian kelajuan $\\Delta v$.",
            "$\\Delta x_{\\min} \\approx 5{,}80 \\times 10^{-8}\\text{ meter}$, dihitung dari perbandingan panjang gelombang de Broglie elektron bebas.",
            "$\\Delta x_{\\min} \\approx 0\\text{ meter}$, karena mengasumsikan posisi dan kecepatan selalu dapat diukur simultan dengan presisi tak terbatas."
        ],
        "formula": {
            "title": "PRINSIP KETIDAKPASTIAN HEISENBERG",
            "latex": "\\Delta x \\cdot \\Delta p \\ge \\frac{h}{4\\pi} \\implies \\Delta x_{\\min} = \\frac{h}{4\\pi m_e \\Delta v} = \\frac{6{,}63 \\times 10^{-34}}{4\\pi \\times (9{,}1 \\times 10^{-31}) \\times 50} \\approx 1{,}16 \\times 10^{-6}\\text{ m}",
            "legend": "• $\\Delta p = m \\Delta v = 4{,}55 \\times 10^{-29}\\text{ N}\\cdot\\text{s}$<br>• Tidak ada alat ukur fisik di alam semesta yang mampu mengukur posisi lebih teliti dari $\\Delta x_{\\min}$ saat $\\Delta p$ diketahui"
        },
        "hints": {
            "concept": "Ketidakpastian Heisenberg: Delta_x * Delta_p >= h / (4*pi). Hitung Delta_p = m * Delta_v = 9,1e-31 * 50 = 4,55e-29 kg.m/s. Lalu Delta_x = h / (4*pi*Delta_p).",
            "execution": "Delta_x = 6,63e-34 / (4 * 3,1416 * 4,55e-29) = 1,16 x 10^-6 m."
        }
    },
    {
        "id": "fis-sim-22",
        "materi": "RELATIVITAS KHUSUS (PENJUMLAHAN KECEPATAN)",
        "topic": "Penjumlahan Kecepatan Relativistik Dua Wahana Antariksa",
        "stem": "Dua wahana antariksa $A$ dan $B$ bergerak saling mendekati di sepanjang garis lurus menurut pengamat yang diam di stasiun ruang angkasa bumi. Wahana $A$ bergerak ke arah timur dengan kecepatan $v_A = 0{,}6c$, sedangkan wahana $B$ bergerak ke arah barat dengan kecepatan $v_B = 0{,}8c$. Kecepatan wahana $B$ menurut pilot di dalam wahana $A$ ($v_{B/A}$) berdasarkan Teori Relativitas Khusus Einstein adalah...",
        "correct": "$v_{B/A} = \\frac{35}{37}c \\approx 0{,}946c$ ke arah barat, karena rumus penjumlahan kecepatan relativistik Einstein untuk dua gerak berlawanan arah adalah $v_{\\text{rel}} = \\frac{v_A + v_B}{1 + \\frac{v_A v_B}{c^2}} = \\frac{0{,}6c + 0{,}8c}{1 + \\frac{(0{,}6c)(0{,}8c)}{c^2}} = \\frac{1{,}4c}{1 + 0{,}48} = \\frac{1{,}4}{1{,}48}c = \\frac{140}{148}c = \\frac{35}{37}c \\approx 0{,}9459c$.",
        "distractors": [
            "$v_{B/A} = 1{,}4c$, karena kelajuan dihitung menggunakan transformasi Galileo klasik Newton ($v_A + v_B$) yang melanggar batas kecepatan cahaya.",
            "$v_{B/A} = 0{,}2c$, karena arah kecepatan keliru dikurangkan ($0{,}8c - 0{,}6c$) padahal kedua wahana saling mendekati.",
            "$v_{B/A} = c$, karena berasumsi bahwa kecepatan relatif antarobjek di luar angkasa selalu menghasilkan kecepatan cahaya.",
            "$v_{B/A} = 0{,}88c$, dihitung dari rata-rata harmonik kecepatan kedua wahana antariksa."
        ],
        "formula": {
            "title": "PENJUMLAHAN KECEPATAN RELATIVISTIK EINSTEIN",
            "latex": "v_{\\text{rel}} = \\frac{u + v}{1 + \\frac{uv}{c^2}} = \\frac{0{,}6c + 0{,}8c}{1 + 0{,}48} = \\frac{1{,}4}{1{,}48}c = \\frac{35}{37}c \\approx 0{,}946c",
            "legend": "• Kecepatan relatif relativistik selalu memenuhi $v_{\\text{rel}} < c$<br>• Transformasi Galileo klasik tidak berlaku untuk kecepatan tinggi ($v \\approx c$)"
        },
        "hints": {
            "concept": "Rumus penjumlahan relativistik dua benda saling mendekati: v_rel = (vA + vB) / (1 + vA*vB / c^2).",
            "execution": "v_rel = (0,6c + 0,8c) / (1 + 0,48) = 1,4c / 1,48 = 35/37 c = 0,946c."
        }
    },
    {
        "id": "fis-sim-23",
        "materi": "FISIKA INTI & ENERGI IKAT INTI",
        "topic": "Defek Massa dan Energi Ikat per Nukleon Inti Alfa",
        "stem": "Inti atom Helium (${}_2^4\\text{He}$) terdiri atas 2 proton dan 2 neutron. Diketahui:<br>• Massa proton $m_p = 1{,}00728\\text{ sma}$<br>• Massa neutron $m_n = 1{,}00866\\text{ sma}$<br>• Massa inti ${}_2^4\\text{He} = 4{,}00150\\text{ sma}$<br>• $1\\text{ sma} \\approx 931{,}5\\text{ MeV}$<br>Defek massa ($\\Delta m$) dan besar energi ikat per nukleon ($E_b/A$) dari inti Helium tersebut berturut-turut adalah...",
        "correct": "$\\Delta m = 0{,}03038\\text{ sma}$ dan $E_b/A \\approx 7{,}07\\text{ MeV/nukleon}$, karena total massa nukleon pembentuk adalah $m_{\\text{teoritis}} = 2(1{,}00728) + 2(1{,}00866) = 2{,}01456 + 2{,}01732 = 4{,}03188\\text{ sma}$. Defek massa adalah $\\Delta m = 4{,}03188 - 4{,}00150 = 0{,}03038\\text{ sma}$. Total energi ikat inti adalah $E_b = 0{,}03038 \\times 931{,}5\\text{ MeV} \\approx 28{,}299\\text{ MeV}$. Karena inti Helium memiliki jumlah nukleon $A = 4$, maka energi ikat per nukleon adalah $E_b/A = \\frac{28{,}299}{4} \\approx 7{,}075\\text{ MeV/nukleon}$.",
        "distractors": [
            "$\\Delta m = 0{,}03038\\text{ sma}$ dan $E_b/A \\approx 28{,}30\\text{ MeV/nukleon}$, karena nilai tersebut merupakan total energi ikat seluruh inti, belum dibagi dengan jumlah nukleon $A = 4$.",
            "$\\Delta m = 0{,}01519\\text{ sma}$ dan $E_b/A \\approx 3{,}54\\text{ MeV/nukleon}$, dihitung dengan hanya memperhitungkan 1 proton dan 1 neutron pembentuk inti.",
            "$\\Delta m = 0{,}06076\\text{ sma}$ dan $E_b/A \\approx 14{,}15\\text{ MeV/nukleon}$, dihitung dari penggandaan defek massa inti.",
            "$\\Delta m = 0{,}00150\\text{ sma}$ dan $E_b/A \\approx 0{,}35\\text{ MeV/nukleon}$, dihitung dari selisih massa inti terhadap nomor massa bulat."
        ],
        "formula": {
            "title": "DEFEK MASSA & ENERGI IKAT PER NUKLEON",
            "latex": "\\Delta m = [Z m_p + (A - Z) m_n] - m_{\\text{inti}} = [2(1{,}00728) + 2(1{,}00866)] - 4{,}00150 = 0{,}03038\\text{ sma}; \\quad \\frac{E_b}{A} = \\frac{0{,}03038 \\times 931{,}5}{4} \\approx 7{,}075\\text{ MeV/nukleon}",
            "legend": "• Inti ${}_2^4\\text{He}$ memiliki kestabilan luar biasa karena energi ikat per nukleonnya tinggi ($7{,}07\\text{ MeV/nukleon}$)<br>• $A = 4$ adalah jumlah total proton dan neutron"
        },
        "hints": {
            "concept": "Defek massa Delta_m = 2*mp + 2*mn - m_He. Energi ikat Eb = Delta_m * 931,5 MeV. Energi ikat per nukleon = Eb / 4.",
            "execution": "Delta_m = 4,03188 - 4,00150 = 0,03038 sma. Eb = 0,03038 * 931,5 = 28,3 MeV. Eb / 4 = 7,07 MeV/nukleon."
        }
    },
    {
        "id": "fis-sim-24",
        "materi": "REAKSI FUSI TERMONUKLIR MATAHARI",
        "topic": "Energi yang Dibebaskan pada Reaksi Fusi Inti Deuterium-Tritium",
        "stem": "Dalam teknologi reaktor fusi masa depan (tokamak), direncanakan pemanfaatan reaksi fusi inti Deuterium (${}_1^2\\text{H}$) dan Tritium (${}_1^3\\text{H}$) dengan persamaan reaksi:<br>$${}_1^2\\text{H} + {}_1^3\\text{H} \\to {}_2^4\\text{He} + {}_0^1\\text{n} + Q$$<br>Diketahui massa atom:<br>• Massa ${}_1^2\\text{H} = 2{,}01410\\text{ sma}$<br>• Massa ${}_1^3\\text{H} = 3{,}01605\\text{ sma}$<br>• Massa ${}_2^4\\text{He} = 4{,}00260\\text{ sma}$<br>• Massa ${}_0^1\\text{n} = 1{,}00866\\text{ sma}$<br>• $1\\text{ sma} \\approx 931{,}5\\text{ MeV}$<br>Energi yang dibebaskan ($Q$) dalam satu kali reaksi fusi D-T tersebut adalah...",
        "correct": "$Q \\approx 17{,}59\\text{ MeV}$ (sekitar $17{,}6\\text{ MeV}$), karena total massa reaktan adalah $m_{\\text{awal}} = 2{,}01410 + 3{,}01605 = 5{,}03015\\text{ sma}$. Total massa produk adalah $m_{\\text{akhir}} = 4{,}00260 + 1{,}00866 = 5{,}01126\\text{ sma}$. Defek massa reaksi fusi adalah $\\Delta m = 5{,}03015 - 5{,}01126 = 0{,}01889\\text{ sma}$. Energi yang dibebaskan adalah $Q = \\Delta m \\times 931{,}5\\text{ MeV} = 0{,}01889 \\times 931{,}5 \\approx 17{,}596\\text{ MeV} \\approx 17{,}6\\text{ MeV}$.",
        "distractors": [
            "$Q \\approx 3{,}27\\text{ MeV}$, karena merupakan energi yang dibebaskan pada reaksi fusi Deuterium-Deuterium cabang helium-3.",
            "$Q \\approx 28{,}30\\text{ MeV}$, karena menyamakan energi reaksi fusi dengan total energi ikat inti helium-4 murni.",
            "$Q \\approx 173{,}2\\text{ MeV}$, karena keliru tertukar dengan besaran energi reaksi fisi pembelahan uranium-235.",
            "$Q \\approx 8{,}80\\text{ MeV}$, dihitung dari defek massa yang keliru dibagi dua saat konversi energi nuklir."
        ],
        "formula": {
            "title": "ENERGI REAKSI FUSI DEUTERIUM-TRITIUM (D-T)",
            "latex": "\\Delta m = (m_{\\text{D}} + m_{\\text{T}}) - (m_{\\alpha} + m_{\\text{n}}) = 5{,}03015 - 5{,}01126 = 0{,}01889\\text{ sma}; \\quad Q = 0{,}01889 \\times 931{,}5 \\approx 17{,}596\\text{ MeV}",
            "legend": "• Reaksi fusi D-T merupakan reaksi penghasil energi bersih terpadat di alam semesta per satuan massa bahan bakar<br>• $\\approx 14{,}1\\text{ MeV}$ energi dibawa oleh neutron cepat dan $\\approx 3{,}5\\text{ MeV}$ oleh partikel alfa"
        },
        "hints": {
            "concept": "Defek massa fusi = (m_D + m_T) - (m_He + m_n). Energi Q = Delta_m * 931,5 MeV.",
            "execution": "Delta_m = 2,01410 + 3,01605 - (4,00260 + 1,00866) = 5,03015 - 5,01126 = 0,01889 sma. Q = 0,01889 * 931,5 = 17,596 MeV."
        }
    },
    {
        "id": "fis-sim-25",
        "materi": "TERMODINAMIKA (SIKLUS TERTUTUP GAS)",
        "topic": "Usaha Siklus Tertutup Segitiga pada Diagram P-V",
        "stem": "Satu mol gas ideal monoatomik mengalami siklus termodinamika tertutup $A \\to B \\to C \\to A$ pada diagram $P-V$ berbentuk segitiga siku-siku:<br>• Titik $A$: $P_A = 1 \\times 10^5\\text{ Pa}$, $V_A = 2 \\times 10^{-3}\\text{ m}^3$<br>• Titik $B$: $P_B = 4 \\times 10^5\\text{ Pa}$, $V_B = 2 \\times 10^{-3}\\text{ m}^3$ (isokhorik)<br>• Titik $C$: $P_C = 1 \\times 10^5\\text{ Pa}$, $V_C = 6 \\times 10^{-3}\\text{ m}^3$<br>Proses $C \\to A$ berlangsung secara isobarik. Usaha total bersih ($W_{\\text{net}}$) yang dilakukan oleh gas selama satu siklus penuh dan kalor total yang dilepas saat proses isobarik $C \\to A$ ($Q_{CA}$) berturut-turut adalah...",
        "correct": "$W_{\\text{net}} = +600\\text{ Joule}$ dan $Q_{CA} = -1.000\\text{ Joule}$, karena usaha total bersih satu siklus tertutup sama dengan luas daerah di dalam kurva segitiga siklus $P-V$: $W_{\\text{net}} = \\frac{1}{2} \\times \\Delta V \\times \\Delta P = \\frac{1}{2} \\times (6 - 2) \\times 10^{-3}\\text{ m}^3 \\times (4 - 1) \\times 10^5\\text{ Pa} = \\frac{1}{2} \\times (4 \\times 10^{-3}) \\times (3 \\times 10^5) = +600\\text{ Joule}$. Pada proses isobarik $C \\to A$, kalor yang dilepas adalah $Q_{CA} = n C_p \\Delta T = \\frac{5}{2} P_A (V_A - V_C) = \\frac{5}{2} \\times 10^5 \\times (2 - 6) \\times 10^{-3} = \\frac{5}{2} \\times 10^5 \\times (-4 \\times 10^{-3}) = -1.000\\text{ Joule}$.",
        "distractors": [
            "$W_{\\text{net}} = +1.200\\text{ Joule}$ dan $Q_{CA} = -600\\text{ Joule}$, karena luas segitiga keliru dihitung sebagai luas persegi panjang tanpa pembagian setengah.",
            "$W_{\\text{net}} = +300\\text{ Joule}$ dan $Q_{CA} = -500\\text{ Joule}$, dihitung dari asumsi volume kerja setengah dari perubahan aktual.",
            "$W_{\\text{net}} = -600\\text{ Joule}$ dan $Q_{CA} = +1.000\\text{ Joule}$, karena salah menentukan tanda arah putaran siklus searah jarum jam.",
            "$W_{\\text{net}} = +600\\text{ Joule}$ dan $Q_{CA} = -400\\text{ Joule}$, karena kalor isobarik keliru dihitung hanya sebesar usaha isobarik $P \\Delta V$."
        ],
        "formula": {
            "title": "USAHA SIKLUS P-V & KALOR PROSES ISOBARIK",
            "latex": "W_{\\text{net}} = \\frac{1}{2} (V_C - V_A)(P_B - P_A) = \\frac{1}{2}(4 \\times 10^{-3})(3 \\times 10^5) = +600\\text{ J}; \\quad Q_{CA} = \\frac{5}{2} P \\Delta V = \\frac{5}{2}(10^5)(-4 \\times 10^{-3}) = -1.000\\text{ J}",
            "legend": "• Siklus searah jarum jam $\\implies W_{\\text{net}} > 0$ (berfungsi sebagai mesin pemanas/kalor)<br>• $C_p = \\frac{5}{2} R$ untuk gas monoatomik<br>• $Q_{CA} = -1.000\\text{ J}$ (tanda minus berarti kalor dilepaskan ke lingkungan)"
        },
        "hints": {
            "concept": "Usaha siklus segitiga: W = 1/2 * alas * tinggi = 1/2 * (Vc - Va) * (Pb - Pa). Kalor isobarik gas monoatomik: Q = Cp * Delta_T = 5/2 * P * Delta_V.",
            "execution": "W = 0,5 * 4e-3 * 3e5 = +600 J. Q_CA = 2,5 * 1e5 * (-4e-3) = -1.000 J."
        }
    },

    # -------------------------------------------------------------
    # 5 COMPLEX MULTI-SELECT HOTS (fis-sim-26 to fis-sim-30)
    # -------------------------------------------------------------
    {
        "id": "fis-sim-26",
        "type": "multi",
        "materi": "ELEKTROMAGNETISME (INDUKTANSI DIRI)",
        "topic": "Faktor Penentu Induktansi Diri Solenoida dan Energi Magnetik",
        "stem": "Sebuah solenoida ideal dirancang untuk menyimpan energi magnetik di dalam rangkaian elektronika daya. Berdasarkan formula fisika induktansi diri $L = \\frac{\\mu N^2 A}{l}$ dan energi magnetik $W_m = \\frac{1}{2} L I^2$, manakah TIGA pernyataan berikut yang benar mengenai upaya memperbesar kapasitas penyimpanan energi magnetik solenoida? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Menyisipkan inti bahan feromagnetik dengan permeabilitas relatif tinggi ($\\mu_r \\gg 1$) ke dalam rongga solenoida untuk melipatgandakan induktansi dirinya secara drastis."},
            {"key": "B", "text": "Memperbanyak jumlah lilitan kawat per satuan panjang, karena induktansi diri solenoida berbanding lurus dengan kuadrat jumlah lilitan ($N^2$)."},
            {"key": "C", "text": "Menaikkan kuat arus listrik yang mengalir melalui solenoida, karena energi magnetik tersimpan sebanding dengan kuadrat kuat arus listrik ($I^2$)."},
            {"key": "D", "text": "Memperpanjang solenoida ($l$) sebesar dua kali lipat tanpa mengubah jumlah lilitan kawat dan luas penampang kumparan."},
            {"key": "E", "text": "Mengganti inti feromagnetik dengan ruang hampa udara agar laju disipasi medan magnet meningkat."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "FAKTOR PENGARUH INDUKTANSI DIRI & ENERGI MAGNETIK",
            "latex": "L = \\frac{\\mu_r \\mu_0 N^2 A}{l}; \\quad W_m = \\frac{1}{2} L I^2",
            "legend": "• Pernyataan A BENAR: $\\mu_r$ memperbesar $L$ hingga ratusan kali lipat<br>• Pernyataan B BENAR: $L \\propto N^2$<br>• Pernyataan C BENAR: $W_m \\propto I^2$<br>• D SALAH: Memperpanjang $l$ justru memperkecil $L$ ($L \\propto 1/l$)<br>• E SALAH: Ruang hampa memiliki $\\mu_r = 1$, memperkecil $L$"
        },
        "hints": {
            "concept": "Perhatikan formula L = mu_r * mu_0 * N^2 * A / l dan Wm = 1/2 * L * I^2. Induktansi membesar jika mu_r naik, N naik (kuadrat), dan energi sebanding I^2.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "fis-sim-27",
        "type": "multi",
        "materi": "GELOMBANG ELEKTROMAGNETIK (SPEKTRUM & SIFAT)",
        "topic": "Karakteristik Gelombang Elektromagnetik dalam Ruang Hampa",
        "stem": "Berdasarkan persamaan gelombang elektromagnetik James Clerk Maxwell dan eksperimen Heinrich Hertz, manakah TIGA karakteristik fundamental gelombang elektromagnetik dalam ruang hampa yang benar? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Gelombang elektromagnetik merupakan gelombang transversal di mana medan listrik $\\vec{E}$ dan medan magnetik $\\vec{B}$ berosilasi saling tegak lurus satu sama lain dan tegak lurus arah rambat gelombang."},
            {"key": "B", "text": "Semua spektrum gelombang elektromagnetik merambat dalam ruang hampa dengan kelajuan mutlak yang persis sama, yaitu $c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}} \\approx 3 \\times 10^8\\text{ m/s}$."},
            {"key": "C", "text": "Gelombang elektromagnetik dapat mengalami fenomena polarisasi, pemantulan, pembiasan, difraksi, dan interferensi tanpa memerlukan medium materi perantara."},
            {"key": "D", "text": "Sinar gamma memiliki kelajuan rambat di ruang hampa yang jauh lebih tinggi daripada gelombang radio FM."},
            {"key": "E", "text": "Gelombang elektromagnetik membawa muatan listrik netto sehingga dapat dibelokkan secara langsung oleh medan elektrostatik eksternal."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "PERSAMAAN GELOMBANG ELEKTROMAGNETIK MAXWELL",
            "latex": "c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}} = 2{,}998 \\times 10^8\\text{ m/s}; \\quad \\vec{S} = \\frac{1}{\\mu_0} (\\vec{E} \\times \\vec{B}); \\quad \\vec{E} \\perp \\vec{B} \\perp \\vec{k}",
            "legend": "• A BENAR: Bersifat transversal dan $\\vec{E} \\perp \\vec{B}$<br>• B BENAR: Kelajuan $c$ konstan di ruang hampa untuk semua frekuensi<br>• C BENAR: Mengalami semua sifat gelombang transversal dan merambat di vakum<br>• D SALAH: Kelajuan di ruang hampa sama persis ($c$)<br>• E SALAH: Foton/GEM tidak bermuatan listrik"
        },
        "hints": {
            "concept": "Gelombang elektromagnetik transversal, tidak bermuatan, merambat di vakum dengan kelajuan c yang sama untuk semua spektrum, dan dapat dipolarisasi.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "fis-sim-28",
        "type": "multi",
        "materi": "FISIKA KUANTUM (EFEK FOTOLISTRIK EINSTEIN)",
        "topic": "Bukti Eksperimen Fotolistrik yang Menggugurkan Fisika Klasik",
        "stem": "Eksperimen efek fotolistrik pada awal abad ke-20 tidak dapat dijelaskan oleh teori gelombang cahaya klasik Maxwell dan melahirkan teori kuantum cahaya Einstein. Manakah TIGA fakta eksperimen efek fotolistrik berikut yang secara langsung membuktikan bahwa cahaya merambat sebagai paket-paket kuantum energi diskrit (foton)? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Keberadaan frekuensi ambang ($f_0$): elektron tidak akan terlepas dari logam jika frekuensi cahaya datang lebih rendah dari $f_0$, tidak peduli seberapa kuat intensitas cahaya yang disorotkan."},
            {"key": "B", "text": "Energi kinetik maksimum fotoelektron ($E_{k,\\max}$) hanya bergantung pada frekuensi cahaya datang dan tidak dipengaruhi sama sekali oleh intensitas cahaya."},
            {"key": "C", "text": "Pelepasan fotoelektron berlangsung seketika (hampir tanpa jeda waktu, $< 10^{-9}\\text{ detik}$) begitu cahaya berfrekuensi mencukupi mengenai permukaan logam."},
            {"key": "D", "text": "Semakin besar intensitas cahaya yang disorotkan, maka energi kinetik elektron yang terpancar akan semakin meningkat secara proporsional."},
            {"key": "E", "text": "Dibutuhkan waktu pemanasan berjam-jam agar elektron mampu mengumpulkan energi gelombang klasik yang cukup sebelum terpental."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "POSTULAT FOTON EFEK FOTOLISTRIK EINSTEIN",
            "latex": "E = hf; \\quad E_{k,\\max} = h(f - f_0); \\quad I_{\\text{arus}} \\propto \\text{Intensitas}; \\quad E_{k,\\max} \\text{ independen terhadap Intensitas}",
            "legend": "• A BENAR: Teori klasik memprediksi intensitas tinggi apapun frekuensinya dapat melepas elektron<br>• B BENAR: Intensitas hanya menambah jumlah foton (arus), bukan energi per foton<br>• C BENAR: Penyerapan kuantum terjadi 1 foton diserap 1 elektron seketika<br>• D dan E adalah prediksi teori klasik yang gagal terbukti"
        },
        "hints": {
            "concept": "Tiga bukti kuantum fotolistrik: ada frekuensi ambang (A), Ek_max hanya tergantung frekuensi bukan intensitas (B), dan emisi seketika tanpa jeda waktu (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "fis-sim-29",
        "type": "multi",
        "materi": "TEORI RELATIVITAS KHUSUS",
        "topic": "Postulat Einstein dan Konsekuensi Kinematika Relativistik",
        "stem": "Teori Relativitas Khusus yang dipublikasikan oleh Albert Einstein pada tahun 1905 mengubah paradigma fisika ruang dan waktu absolut Newton. Manakah TIGA pernyataan berikut yang merupakan postulat resmi atau konsekuensi logis relativitas khusus yang terbukti secara eksperimental? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Hukum-hukum fisika memiliki bentuk yang sama persis dalam semua kerangka acuan inersial (kerangka yang diam atau bergerak dengan kecepatan konstan)."},
            {"key": "B", "text": "Kelajuan cahaya di ruang hampa adalah konstan bernilai $c$ bagi semua pengamat inersial, tidak bergantung pada gerak sumber cahaya maupun gerak pengamat."},
            {"key": "C", "text": "Panjang benda yang diukur oleh pengamat yang bergerak relatif terhadap benda tersebut akan tampak mengalami penyusutan (kontraksi Lorentz) hanya pada arah yang sejajar dengan arah geraknya."},
            {"key": "D", "text": "Sebuah jam yang bergerak relatif terhadap pengamat akan berdetak lebih cepat daripada jam yang diam di kerangka acuan pengamat tersebut."},
            {"key": "E", "text": "Partikel bermassa diam $m_0 > 0$ dapat dipercepat hingga melampaui kelajuan cahaya jika diberi energi dorong kinetik tak hingga."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "POSTULAT & KONSEKUENSI RELATIVITAS KHUSUS",
            "latex": "L = L_0\\sqrt{1 - (v/c)^2}; \\quad \\Delta t = \\frac{\\Delta t_0}{\\sqrt{1 - (v/c)^2}}; \\quad E = \\frac{m_0 c^2}{\\sqrt{1 - (v/c)^2}}",
            "legend": "• Postulat 1 = Pernyataan A (Prinsip Relativitas)<br>• Postulat 2 = Pernyataan B (Invariansi Laju Cahaya)<br>• Konsekuensi = Pernyataan C (Kontraksi Panjang pada arah gerak)<br>• D SALAH: Jam bergerak berdetak lebih lambat (Dilatasi Waktu)<br>• E SALAH: Batas kecepatan semesta adalah $c$, tidak ada materi berkecepatan $\\ge c$"
        },
        "hints": {
            "concept": "Postulat Einstein: hukum fisika sama di semua kerangka inersial (A), laju cahaya konstan bagi semua pengamat (B). Konsekuensi: kontraksi Lorentz pada arah gerak (C). Jam bergerak justru melambat.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "fis-sim-30",
        "type": "multi",
        "materi": "FISIKA INTI & REAKSI NUKLIR",
        "topic": "Hukum Kekekalan dalam Reaksi Inti Radioaktif",
        "stem": "Dalam semua peristiwa peluruhan radioaktif (alfa, beta, gamma) serta reaksi fisi dan fusi nuklir, terdapat besaran-besaran fisika yang mutlak kekal. Manakah TIGA hukum kekekalan yang wajib dipenuhi dalam setiap persamaan reaksi nuklir? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Kekekalan Jumlah Nomor Massa (Nukleon): jumlah total proton dan neutron sebelum reaksi harus sama persis dengan jumlah total nukleon setelah reaksi."},
            {"key": "B", "text": "Kekekalan Muatan Listrik (Nomor Atom $Z$): jumlah total muatan elementer sebelum reaksi sama dengan jumlah total muatan sesudah reaksi."},
            {"key": "C", "text": "Kekekalan Massa-Energi Relativistik: total energi relativistik (massa reaktan ditambah energi kinetik awal) sama dengan total energi produk ditambah energi yang dilepaskan ($Q$)."},
            {"key": "D", "text": "Kekekalan Massa Diam Klasik: jumlah massa diam reaktan selalu sama persis dengan jumlah massa diam partikel produk tanpa ada defek massa sedikit pun."},
            {"key": "E", "text": "Kekekalan Jumlah Inti Atom: jumlah inti atom utuh sebelum dan sesudah reaksi tidak boleh berubah menjadi spesies isotop yang berbeda."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "HUKUM KEKEKALAN PADA REAKSI INTI",
            "latex": "\\sum A_{\\text{awal}} = \\sum A_{\\text{akhir}}; \\quad \\sum Z_{\\text{awal}} = \\sum Z_{\\text{akhir}}; \\quad E_{\\text{total}} = \\sum m_{\\text{awal}} c^2 + K_{\\text{awal}} = \\sum m_{\\text{akhir}} c^2 + K_{\\text{akhir}}",
            "legend": "• A BENAR: Nomor massa $A$ kekal<br>• B BENAR: Nomor atom / muatan $Z$ kekal<br>• C BENAR: Massa-energi relativistik Einstein kekal<br>• D SALAH: Terjadi defek massa $\\Delta m$ yang dikonversi menjadi energi $Q = \\Delta m c^2$<br>• E SALAH: Terjadi transmutasi inti atom"
        },
        "hints": {
            "concept": "Hukum kekekalan reaksi inti: nomor massa kekal (A), nomor atom/muatan kekal (B), dan massa-energi total kekal (C). Massa diam klasik tidak kekal karena ada defek massa.",
            "execution": "Pilih A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH HOTS (fis-sim-31 to fis-sim-35)
    # -------------------------------------------------------------
    {
        "id": "fis-sim-31",
        "type": "matrix",
        "materi": "TERMODINAMIKA & SIKLUS CARNOT",
        "topic": "Prinsip Termodinamika, Mesin Kalor, dan Entropi",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai Hukum Termodinamika dan Mesin Kalor Carnot!",
        "statements": [
            {
                "text": "Efisiensi termal mesin Carnot hanya bergantung pada suhu mutlak reservoir tinggi (Th) dan reservoir rendah (Tc), tidak dipengaruhi oleh jenis zat kerja gas yang digunakan.",
                "correct": True
            },
            {
                "text": "Sebuah mesin kalor hipotetis dapat dibuat dengan efisiensi 100% jika seluruh kalor yang diserap dari reservoir panas berhasil diubah seutuhnya menjadi usaha mekanik tanpa membuang kalor ke lingkungan dingin.",
                "correct": False
            },
            {
                "text": "Pada proses siklus termodinamika tertutup, perubahan energi dalam total sistem setelah menyelesaikan satu putaran siklus penuh selalu bernilai nol (Delta U = 0).",
                "correct": True
            },
            {
                "text": "Menurut Hukum II Termodinamika (Prinsip Entropi), total entropi alam semesta dalam setiap proses spontan yang terjadi secara alami selalu meningkat atau tetap konstan.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP UTAMA TERMODINAMIKA & SIKLUS CARNOT",
            "latex": "\\eta_{\\text{Carnot}} = 1 - \\frac{T_C}{T_H}; \\quad \\oint dU = 0; \\quad \\Delta S_{\\text{semesta}} \\ge 0",
            "legend": "• Pernyataan 1 BENAR: Efisiensi Carnot adalah efisiensi teoretis maksimum yang hanya dipengaruhi rasio $T_C/T_H$<br>• Pernyataan 2 SALAH: Melanggar Pernyataan Kelvin-Planck pada Hukum II Termodinamika (tidak mungkin ada mesin kalor dengan $\\eta = 100\\%$)<br>• Pernyataan 3 BENAR: Energi dalam $U$ adalah fungsi keadaan ($U_{\\text{akhir}} = U_{\\text{awal}} \\implies \\Delta U = 0$)<br>• Pernyataan 4 BENAR: Pernyataan Hukum II Termodinamika tentang entropi alam semesta"
        },
        "hints": {
            "concept": "Pahami efisiensi Carnot eta = 1 - Tc/Th, hukum Kelvin-Planck (efisiensi 100% mustahil), siklus tertutup Delta U = 0, dan kenaikan entropi alam semesta.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "fis-sim-32",
        "type": "matrix",
        "materi": "GETARAN HARMONIK & RESONANSI GELOMBANG",
        "topic": "Karakteristik Osilasi Harmonik dan Gelombang Mekanik",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai Getaran Harmonik Sederhana (GHS) dan Resonansi Gelombang Bunyi!",
        "statements": [
            {
                "text": "Pada getaran harmonik sederhana pegas, percepatan benda mencapai nilai maksimum tepat saat benda berada di titik simpangan terjauh (amplitudo).",
                "correct": True
            },
            {
                "text": "Ketika benda berosilasi harmonik melewati titik kesetimbangannya, energi potensial sistem bernilai maksimum sedangkan energi kinetiknya bernilai nol.",
                "correct": False
            },
            {
                "text": "Resonansi akustik terjadi apabila frekuensi getaran sumber luar tepat sama dengan salah satu frekuensi alami sistem penerima, menghasilkan amplitudo getaran yang berlipat ganda.",
                "correct": True
            },
            {
                "text": "Periode getaran bandul sederhana di permukaan bumi berbanding lurus dengan massa bandul yang digantungkan pada tali.",
                "correct": False
            }
        ],
        "formula": {
            "title": "PERSAMAAN GETARAN HARMONIS SEDERHANA",
            "latex": "a(t) = -\\omega^2 y(t); \\quad T_{\\text{bandul}} = 2\\pi\\sqrt{\\frac{L}{g}}; \\quad E_m = E_k + E_p = \\frac{1}{2} k A^2",
            "legend": "• Pernyataan 1 BENAR: Di simpangan terjauh ($y = A$), percepatan $a = \\omega^2 A$ maksimum<br>• Pernyataan 2 SALAH: Di titik kesetimbangan ($y = 0$), $E_p = 0$ dan $E_k$ bernilai maksimum<br>• Pernyataan 3 BENAR: Definisi resonansi fisis<br>• Pernyataan 4 SALAH: Periode bandul $T = 2\\pi\\sqrt{L/g}$ sama sekali tidak bergantung pada massa bandul"
        },
        "hints": {
            "concept": "Percepatan GHS a = -omega^2 * y (maksimum di amplitudo). Di titik seimbang Ep = 0, Ek maks. Periode bandul T = 2pi*sqrt(L/g) tidak bergantung massa.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "fis-sim-33",
        "type": "matrix",
        "materi": "ELEKTROSTATIKA & MEDAN LISTRIK",
        "topic": "Sifat Elektrostatik Konduktor dan Kapasitor",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai elektrostatika, medan listrik, dan sifat kapasitor!",
        "statements": [
            {
                "text": "Di dalam rongga sebuah bola konduktor pejal berongga yang berada dalam kesetimbangan elektrostatik, kuat medan listrik selalu bernilai nol (E = 0).",
                "correct": True
            },
            {
                "text": "Garis-garis medan elektrostatik selalu berawal dari muatan positif dan berakhir pada muatan negatif, serta tidak pernah saling berpotongan.",
                "correct": True
            },
            {
                "text": "Jika jarak antar keping kapasitor sejajar dijauhkan menjadi dua kali lipat pada kondisi muatan keping konstan terisolasi, maka energi potensial listrik yang tersimpan di dalam kapasitor akan berkurang menjadi separuhnya.",
                "correct": False
            },
            {
                "text": "Menyisipkan bahan dielektrik ke dalam kapasitor keping sejajar selalu menaikkan kapasitas kapasitansinya sebanding dengan konstanta dielektrik bahan tersebut.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP ELEKTROSTATIK KONDUKTOR & KAPASITOR",
            "latex": "E_{\\text{dalam}} = 0; \\quad C = \\kappa \\frac{\\varepsilon_0 A}{d}; \\quad W = \\frac{Q^2}{2C} = \\frac{Q^2 d}{2 \\varepsilon_0 A}",
            "legend": "• Pernyataan 1 BENAR: Efek sangkar Faraday (medan di dalam konduktor setimbang adalah nol)<br>• Pernyataan 2 BENAR: Sifat dasar garis medan listrik Faraday<br>• Pernyataan 3 SALAH: Karena $C \\propto 1/d$, jika $d$ naik dua kali maka $C$ menjadi separuh, sehingga $W = Q^2/(2C)$ justru meningkat dua kali lipat akibat usaha penarikan keping<br>• Pernyataan 4 BENAR: $C = \\kappa C_0$"
        },
        "hints": {
            "concept": "Kuat medan dalam konduktor = 0. Garis gaya dari positif ke negatif. Kapasitor terisolasi Q konstan: W = Q^2 / (2C). Jika d naik, C turun, maka W bertambah! C = kappa * C0.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    },
    {
        "id": "fis-sim-34",
        "type": "matrix",
        "materi": "INDUKSI ELEKTROMAGNETIK",
        "topic": "Hukum Faraday, Hukum Lenz, dan Fenomena Arus Eddy",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai induksi elektromagnetik dan hukum-hukum transformator!",
        "statements": [
            {
                "text": "Menurut Hukum Lenz, arah arus induksi elektromagnetik selalu sedemikian rupa sehingga menimbulkan medan magnet yang melawan perubahan fluks magnetik yang menyebabkannya.",
                "correct": True
            },
            {
                "text": "Fluks magnetik maksimum menembus sebuah bidang kumparan ketika arah medan magnetik sejajar rata dengan bidang permukaan kumparan.",
                "correct": False
            },
            {
                "text": "Pada transformator step-up ideal (efisiensi 100%), tegangan sekunder lebih tinggi daripada tegangan primer, sedangkan kuat arus sekunder lebih kecil daripada kuat arus primer.",
                "correct": True
            },
            {
                "text": "Pemanfaatan inti besi berlapis-lapis (laminated core) pada transformator bertujuan untuk meminimalkan kehilangan daya listrik akibat arus putar (arus Eddy).",
                "correct": True
            }
        ],
        "formula": {
            "title": "HUKUM FARADAY & LENZ",
            "latex": "\\Phi = B A \\cos\\theta; \\quad \\varepsilon = -N \\frac{d\\Phi}{dt}; \\quad \\frac{V_s}{V_p} = \\frac{N_s}{N_p} = \\frac{I_p}{I_s}",
            "legend": "• Pernyataan 1 BENAR: Bunyi Hukum Lenz (tanda negatif pada hukum Faraday)<br>• Pernyataan 2 SALAH: Fluks maksimum saat $\\vec{B}$ tegak lurus bidang kumparan (sudut dengan normal $\\theta = 0^\\circ \\implies \\cos 0^\\circ = 1$)<br>• Pernyataan 3 BENAR: Daya tetap $P_s = P_p \\implies V_s I_s = V_p I_p$, sehingga tegangan naik arus turun<br>• Pernyataan 4 BENAR: Inti laminasi memutus jalur sirkulasi arus Eddy sehingga efisiensi transformator meningkat"
        },
        "hints": {
            "concept": "Hukum Lenz menyatakan arus induksi melawan perubahan fluks (tanda minus). Fluks maks jika tegak lurus bidang. Transformator step-up: Vs > Vp dan Is < Ip. Inti laminasi meredam arus Eddy.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "fis-sim-35",
        "type": "matrix",
        "materi": "FISIKA MODERN & TEORI KUANTUM",
        "topic": "Dualisme Kuantum dan Model Fisika Modern",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai fisika modern dan mekanika kuantum!",
        "statements": [
            {
                "text": "Menurut hipotesis Louis de Broglie, setiap partikel materi bermassa yang bergerak dengan momentum p memiliki sifat gelombang dengan panjang gelombang lambda = h / p.",
                "correct": True
            },
            {
                "text": "Efek Compton membuktikan bahwa foton cahaya memiliki momentum relativistik dan dapat mengalami tumbukan elastis dengan elektron bebas.",
                "correct": True
            },
            {
                "text": "Dalam model atom Bohr, elektron yang mengorbit inti atom pada lintasan stasioner akan terus-menerus memancarkan radiasi elektromagnetik gelombang sehingga energinya berkurang.",
                "correct": False
            },
            {
                "text": "Waktu paruh suatu zat radioaktif tidak dipengaruhi oleh perubahan suhu, tekanan mekanik, maupun reaksi kimia yang dialami oleh unsur radioaktif tersebut.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP MEKANIKA KUANTUM & FISIKA MODERN",
            "latex": "\\lambda = \\frac{h}{p}; \\quad \\Delta\\lambda = \\frac{h}{m_e c}(1 - \\cos\\theta); \\quad T_{1/2} = \\frac{\\ln 2}{\\lambda_{\\text{luruh}}}",
            "legend": "• Pernyataan 1 BENAR: Hipotesis De Broglie (dualisme gelombang-materi)<br>• Pernyataan 2 BENAR: Eksperimen hamburan foton-elektron Arthur Compton (1923)<br>• Pernyataan 3 SALAH: Postulat Bohr menyatakan elektron pada orbit stasioner TIDAK memancarkan energi sama sekali<br>• Pernyataan 4 BENAR: Peluruhan radioaktif adalah fenomena murni inti atomik independen kondisi kimia-fisika lingkungan luar"
        },
        "hints": {
            "concept": "Hipotesis de Broglie lambda = h/p. Efek Compton membuktikan momentum foton. Pada lintasan stasioner Bohr elektron TIDAK meradiasikan energi. Waktu paruh adalah sifat inti independen kondisi kimia/suhu.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    }
]
