# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Kimia (SMA/MA Saintek)
Dataset: Hard Practice (25 Authentic Questions, kim-lat-h-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

KIMIA_HARD_ITEMS = [
    {
        "id": "kim-lat-h-01",
        "materi": "STRUKTUR ATOM & TEORI ORBITAL MOLEKUL",
        "topic": "Orde Ikatan dan Sifat Kemagnetan Spesies Dioksigen",
        "stem": "Berdasarkan Teori Orbital Molekul (Molecular Orbital Theory) untuk molekul diatomik homointi periode kedua, konfigurasi orbital molekul tingkat valensi gas oksigen ($\\text{O}_2$) memiliki dua elektron tak berpasangan pada orbital anti-ikatan $\\pi^*_{2p_x}$ dan $\\pi^*_{2p_y}$. Jika molekul $\\text{O}_2$ tereduksi menjadi ion peroksida ($\\text{O}_2^{2-}$), perubahan orde ikatan (bond order) dan sifat kemagnetan yang terjadi adalah...",
        "correct": "Orde ikatan turun dari 2 menjadi 1 dan sifat kemagnetan berubah dari paramagnetik menjadi diamagnetik, karena penambahan 2 elektron pada $\\text{O}_2^{2-}$ mengisi penuh orbital anti-ikatan $\\pi^*_{2p_x}$ dan $\\pi^*_{2p_y}$ sehingga seluruh elektron berpasangan (diamagnetik), dan orde ikatan dihitung dari $\\text{BO} = \\frac{N_b - N_a}{2} = \\frac{8 - 6}{2} = 1$ (pada $\\text{O}_2$ nilainya $\\frac{8 - 4}{2} = 2$).",
        "distractors": [
            "Orde ikatan naik dari 2 menjadi 3 dan sifat kemagnetan tetap paramagnetik dengan medan magnet kuat.",
            "Orde ikatan turun dari 2 menjadi 1{,}5 dan sifat kemagnetan tetap paramagnetik seperti ion superoksida.",
            "Orde ikatan tidak berubah (tetap 2) dan sifat kemagnetan tetap paramagnetik dengan spin sejajar.",
            "Orde ikatan menjadi nol dan molekul peroksida langsung terdisosiasi spontan menjadi atom bebas."
        ],
        "formula": {
            "title": "ORDE IKATAN TEORI ORBITAL MOLEKUL (MO)",
            "latex": "\\text{BO} = \\frac{N_{\\text{bonding}} - N_{\\text{antibonding}}}{2}; \\quad \\text{BO}(\\text{O}_2) = \\frac{8 - 4}{2} = 2 \\text{ (Paramagnetik)}; \\quad \\text{BO}(\\text{O}_2^{2-}) = \\frac{8 - 6}{2} = 1 \\text{ (Diamagnetik)}",
            "legend": "• Konfigurasi valensi $\\text{O}_2$: $(\\sigma_{2s})^2(\\sigma^*_{2s})^2(\\sigma_{2p_z})^2(\\pi_{2p_x})^2(\\pi_{2p_y})^2(\\pi^*_{2p_x})^1(\\pi^*_{2p_y})^1$<br>• Ion $\\text{O}_2^{2-}$ memiliki orbital $(\\pi^*_{2p})^4$ penuh $\\implies$ Diamagnetik dan ikatan melemah"
        },
        "hints": {
            "concept": "O2 memiliki 2 elektron tak berpasangan di orbital pi* (paramagnetik, BO = (8-4)/2 = 2). Menambah 2e- membentuk O2(2-) mengisi penuh orbital pi* -> semua elektron berpasangan (diamagnetik), BO = (8-6)/2 = 1.",
            "execution": "Orde ikatan turun dari 2 ke 1, paramagnetik berubah menjadi diamagnetik."
        }
    },
    {
        "id": "kim-lat-h-02",
        "materi": "KIMIA KOORDINASI (TEORI MEDAN KRISTAL / CFT)",
        "topic": "Pembelahan Orbital d Kompleks Oktahedral Spin Tinggi vs Rendah",
        "stem": "Ion kompleks heksasianoferat(II) $[\\text{Fe}(\\text{CN})_6]^{4-}$ bersifat diamagnetik, sedangkan ion kompleks heksaaquabesi(II) $[\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}$ bersifat paramagnetik kuat dengan 4 elektron tak berpasangan. Padahal kedua ion kompleks tersebut sama-sama memiliki ion pusat $\\text{Fe}^{2+}$ berkonsfigurasi $3d^6$. Penjelasan teoritis yang tepat berdasarkan Teori Medan Kristal (Crystal Field Theory) adalah...",
        "correct": "Ligan $\\text{CN}^-$ adalah ligan medan kuat ($\\Delta_o > P$, energi pemisahan medan oktahedral lebih besar daripada energi perpasangan elektron) yang memaksa keenam elektron $3d$ berpasangan di orbital energi rendah $t_{2g}$ membentuk kompleks spin rendah ($t_{2g}^6\\,e_g^0$, diamagnetik); sedangkan ligan $\\text{H}_2\\text{O}$ adalah ligan medan lemah ($\\Delta_o < P$) sehingga elektron mengisi orbital $t_{2g}$ dan $e_g$ secara terdistribusi membentuk kompleks spin tinggi ($t_{2g}^4\\,e_g^2$, 4 elektron tak berpasangan).",
        "distractors": [
            "Ligan $\\text{CN}^-$ mengoksidasi atom besi menjadi bilangan oksidasi $+3$, sedangkan ligan $\\text{H}_2\\text{O}$ mereduksinya menjadi besi nol.",
            "Ligan $\\text{H}_2\\text{O}$ memiliki pasangan elektron bebas lebih banyak sehingga mendistorsi simetri medan ligan oktahedral menjadi bujur sangkar.",
            "Kompleks $[\\text{Fe}(\\text{CN})_6]^{4-}$ memiliki geometri tetrahedral sedangkan $[\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}$ memiliki geometri oktahedral.",
            "Ligan $\\text{CN}^-$ membentuk ikatan ionik murni sedangkan molekul air membentuk ikatan hidrogen kovalen koordinasi polar."
        ],
        "formula": {
            "title": "PEMBELAHAN ORBITAL d OKTAHEDRAL (CFT)",
            "latex": "\\Delta_o > P \\implies [\\text{Fe}(\\text{CN})_6]^{4-}: t_{2g}^6\\,e_g^0 \\quad (n=0, \\text{Low Spin/Diamagnetik}); \\quad \\Delta_o < P \\implies [\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}: t_{2g}^4\\,e_g^2 \\quad (n=4, \\text{High Spin/Paramagnetik})",
            "legend": "• Deret spektrokimia: $\\text{I}^- < \\text{Br}^- < \\text{Cl}^- < \\text{F}^- < \\text{OH}^- < \\text{H}_2\\text{O} < \\text{NH}_3 < \\text{en} < \\text{CN}^- < \\text{CO}$<br>• Ligan kuat menghasilkan medan kristal $\\Delta_o$ besar"
        },
        "hints": {
            "concept": "CN- adalah ligan kuat (Delta_o besar, spin rendah): 6 elektron mengisi t2g berpasangan semua (diamagnetik). H2O ligan lemah (Delta_o kecil, spin tinggi): konfigurasi t2g^4 eg^2 ada 4 elektron tak berpasangan (paramagnetik).",
            "execution": "CN- ligan medan kuat (spin rendah, t2g^6 eg^0), H2O ligan medan lemah (spin tinggi, t2g^4 eg^2)."
        }
    },
    {
        "id": "kim-lat-h-03",
        "materi": "STOIKIOMETRI TITRASI PENGENDAPAN (ARGENTOMETRI)",
        "topic": "Penentuan Kadar Klorida dengan Metode Mohr",
        "stem": "Sebanyak $0{,}585\\text{ gram}$ sampel garam dapur dilarutkan dalam air hingga volume $100\\text{ mL}$. Sebanyak $25\\text{ mL}$ alikuot larutan tersebut dititrasi dengan larutan standar $\\text{AgNO}_3\\,0{,}1\\text{ M}$ menggunakan indikator kalium kromat ($\\text{K}_2\\text{CrO}_4$). Titik akhir titrasi tercapai saat terbentuk endapan merah bata $\\text{Ag}_2\\text{CrO}_4$ dan volume $\\text{AgNO}_3$ yang terpakai adalah tepat $24\\text{ mL}$. Kemurnian persentase massa natrium klorida ($\\text{NaCl}$, $M_r = 58{,}5\\text{ g/mol}$) dalam sampel garam dapur tersebut adalah...",
        "correct": "$96{,}0\\%$, karena jumlah mol ion $\\text{Ag}^+$ yang bereaksi pada titrasi alikuot $25\\text{ mL}$ adalah $n = V \\times M = 24\\text{ mL} \\times 0{,}1\\text{ M} = 2{,}4\\text{ mmol}$. Karena reaksi pengendapan $\\text{Ag}^+ + \\text{Cl}^- \\to \\text{AgCl}(s)$ memiliki perbandingan mol $1 : 1$, maka mol $\\text{NaCl}$ dalam $25\\text{ mL}$ adalah $2{,}4\\text{ mmol}$. Total mol $\\text{NaCl}$ dalam seluruh $100\\text{ mL}$ larutan sampel adalah $2{,}4\\text{ mmol} \\times \\frac{100}{25} = 9{,}6\\text{ mmol} = 9{,}6 \\times 10^{-3}\\text{ mol}$. Massa $\\text{NaCl}$ murni adalah $m = 9{,}6 \\times 10^{-3}\\text{ mol} \\times 58{,}5\\text{ g/mol} = 0{,}5616\\text{ gram}$. Persentase kemurnian adalah $\\frac{0{,}5616\\text{ g}}{0{,}585\\text{ g}} \\times 100\\% = 96{,}0\\%$.",
        "distractors": [
            "$24{,}0\\%$, karena mengabaikan faktor pengenceran alikuot sampel empat kali lipat.",
            "$48{,}0\\%$, dihitung dengan membagi massa sampel dengan volume titran tanpa massa molar.",
            "$80{,}0\\%$, dihitung dari rasio kelarutan perak klorida terhadap perak kromat.",
            "$100{,}0\\%$, karena beranggapan sampel garam dapur bebas dari zat pengotor higroskopis."
        ],
        "formula": {
            "title": "TITRASI ARGENTOMETRI METODE MOHR",
            "latex": "n_{\\text{Cl}^-} = V_{\\text{AgNO}_3} \\times M_{\\text{AgNO}_3} = 24 \\times 0{,}1 = 2{,}4\\text{ mmol}; \\quad n_{\\text{total}} = 2{,}4 \\times \\frac{100}{25} = 9{,}6\\text{ mmol}; \\quad \\% = \\frac{9{,}6 \\times 10^{-3} \\times 58{,}5}{0{,}585} \\times 100\\% = 96\\%",
            "legend": "• Titrasi Mohr menggunakan indikator $\\text{CrO}_4^{2-}$ yang membentuk endapan merah bata $\\text{Ag}_2\\text{CrO}_4$ setelah seluruh $\\text{Cl}^-$ mengendap putih<br>• Kadar $\\text{NaCl} = 96{,}0\\%$"
        },
        "hints": {
            "concept": "Mol Ag+ = 24 mL * 0,1 M = 2,4 mmol. Ini terdapat dalam 25 mL sampel. Total dalam 100 mL = 2,4 * 4 = 9,6 mmol. Massa NaCl = 9,6 mmol * 58,5 mg/mmol = 561,6 mg = 0,5616 g. % = 0,5616 / 0,585 * 100%.",
            "execution": "% kemurnian = (0,5616 / 0,585) * 100% = 96,0%."
        }
    },
    {
        "id": "kim-lat-h-04",
        "materi": "GAS NYATA (PERSAMAAN VAN DER WAALS)",
        "topic": "Koreksi Tekanan dan Volume Molekuler Gas Nyata",
        "stem": "Persamaan Van der Waals untuk satu mol gas nyata dinyatakan sebagai:<br>$$\\left(P + \\frac{a}{V_m^2}\\right)(V_m - b) = R T$$<br>Makna fisis dari tetapan koreksi $a$ dan tetapan koreksi $b$ dalam menjelaskan penyimpangan gas nyata dari perilaku gas ideal adalah...",
        "correct": "Tetapan $a$ mengoreksi adanya gaya tarik-menarik antarmolekul gas nyata (intermolecular attraction) yang memperkecil tekanan terukur pada dinding bejana, sedangkan tetapan $b$ mengoreksi volume nyata yang ditempati oleh partikel molekul gas itu sendiri (excluded volume) yang tidak dapat ditembus oleh molekul lain.",
        "distractors": [
            "Tetapan $a$ mengoreksi volume fisik molekul gas padat dan tetapan $b$ mengoreksi energi kinetik translasi partikel.",
            "Tetapan $a$ mengoreksi tumbukan lenting sempurna molekul dan tetapan $b$ menyatakan laju disosiasi endotermik gas.",
            "Tetapan $a$ mengoreksi gravitasi bumi di dalam bejana dan tetapan $b$ menyatakan konduktivitas termal wadah.",
            "Kedua tetapan $a$ dan $b$ merupakan konstanta empiris tanpa makna fisis yang hanya berfungsi sebagai penyeimbang dimensi satuan."
        ],
        "formula": {
            "title": "PERSAMAAN GAS NYATA VAN DER WAALS",
            "latex": "\\left(P + \\frac{a n^2}{V^2}\\right)(V - n b) = n R T",
            "legend": "• Suku $\\frac{a n^2}{V^2}$ = Tekanan internal akibat gaya tarik intermolekul (kohesi)<br>• Suku $n b$ = Volume eksklusi yang ditempati molekul secara berhingga<br>• Gas nyata mendekati sifat gas ideal pada tekanan sangat rendah dan suhu sangat tinggi"
        },
        "hints": {
            "concept": "a mengoreksi gaya tarik-menarik antarmolekul (yang mengurangi tekanan terukur). b mengoreksi volume fisik yang ditempati molekul gas (volume eksklusi).",
            "execution": "a = gaya tarik antarmolekul, b = volume fisik partikel molekul."
        }
    },
    {
        "id": "kim-lat-h-05",
        "materi": "LARUTAN PENYANGGA POLIPROTIK (BUFFER SITOPLASMA)",
        "topic": "Sistem Penyangga Dihidrogen Fosfat dalam Sel Tubuh",
        "stem": "Asam fosfat ($\\text{H}_3\\text{PO}_4$) adalah asam triprotik dengan tiga tetapan ionisasi bertingkat berturut-turut: $K_{a1} = 7{,}5 \\times 10^{-3}$ ($\\text{p}K_{a1} = 2{,}12$), $K_{a2} = 6{,}2 \\times 10^{-8}$ ($\\text{p}K_{a2} = 7{,}21$), dan $K_{a3} = 4{,}2 \\times 10^{-13}$ ($\\text{p}K_{a3} = 12{,}38$). Pasangan spesi kimia yang berperan sebagai larutan penyangga utama dalam cairan intraseluler pada pH fisiologis tubuh manusia ($\\text{pH} \\approx 7{,}4$) beserta perbandingan rasio molar $[\\text{Basa Konjugasi}] / [\\text{Asam Konjugasi}]$ adalah... (Gunakan $10^{0{,}19} \\approx 1{,}55$)",
        "correct": "Pasangan $\\text{H}_2\\text{PO}_4^-$ (asam) dan $\\text{HPO}_4^{2-}$ (basa konjugasi) dengan rasio $[\\text{HPO}_4^{2-}] / [\\text{H}_2\\text{PO}_4^-] \\approx 1{,}55$, karena nilai $\\text{p}K_{a2} = 7{,}21$ berada paling dekat dengan rentang pH fisiologis $7{,}4$. Menurut persamaan Henderson-Hasselbalch: $\\text{pH} = \\text{p}K_{a2} + \\log\\frac{[\\text{HPO}_4^{2-}]}{[\\text{H}_2\\text{PO}_4^-]} \\implies 7{,}40 = 7{,}21 + \\log(\\text{rasio}) \\implies \\log(\\text{rasio}) = 0{,}19 \\implies \\text{rasio} = 10^{0{,}19} \\approx 1{,}55$.",
        "distractors": [
            "Pasangan $\\text{H}_3\\text{PO}_4$ dan $\\text{H}_2\\text{PO}_4^-$ dengan rasio molar $100 : 1$, karena asam triprotik harus dimulai dari pelepasan proton pertama.",
            "Pasangan $\\text{HPO}_4^{2-}$ dan $\\text{PO}_4^{3-}$ dengan rasio molar $1 : 10$, karena ion fosfat bebas memiliki muatan tiga negatif.",
            "Pasangan $\\text{H}_2\\text{PO}_4^-$ dan $\\text{HPO}_4^{2-}$ dengan rasio $[\\text{HPO}_4^{2-}] / [\\text{H}_2\\text{PO}_4^-] = 0{,}65$, karena formula rasio logaritma Henderson-Hasselbalch keliru dibalik.",
            "Pasangan $\\text{H}_3\\text{PO}_4$ dan $\\text{PO}_4^{3-}$ dengan rasio $1 : 1$, karena mengabaikan tahapan disosiasi bertingkat asam poliprotik."
        ],
        "formula": {
            "title": "SISTEM PENYANGGA FOSFAT INTRASELULER",
            "latex": "\\text{H}_2\\text{PO}_4^- \\rightleftharpoons \\text{HPO}_4^{2-} + \\text{H}^+; \\quad \\text{pH} = \\text{p}K_{a2} + \\log\\frac{[\\text{HPO}_4^{2-}]}{[\\text{H}_2\\text{PO}_4^-]}; \\quad 7{,}40 = 7{,}21 + \\log(\\text{rasio}) \\implies \\text{rasio} \\approx 1{,}55",
            "legend": "• Buffer paling efektif bekerja pada rentang $\\text{pH} = \\text{p}K_a \\pm 1$<br>• Pada pH $7{,}4$, spesi dominan adalah $\\text{HPO}_4^{2-}$ (basa konjugasi sedikit lebih banyak dari asam konjugasi)"
        },
        "hints": {
            "concept": "Cari pKa yang paling dekat dengan pH fisiologis 7,4, yaitu pKa2 = 7,21 (pasangan H2PO4- dan HPO4 2-). Gunakan pH = pKa2 + log([HPO4 2-] / [H2PO4 -]).",
            "execution": "log(rasio) = 7,40 - 7,21 = 0,19 -> rasio = 10^0,19 = 1,55. Pasangan H2PO4- dan HPO4 2-."
        }
    },
    {
        "id": "kim-lat-h-06",
        "materi": "HIDROLISIS BERTINGKAT GARAM POLIPROTIK",
        "topic": "Perhitungan pH Larutan Natrium Karbonat Na2CO3",
        "stem": "Natrium karbonat ($\\text{Na}_2\\text{CO}_3$) dilarutkan ke dalam air menghasilkan larutan berkonsentrasi $0{,}1\\text{ M}$. Diketahui asam karbonat memiliki dua tetapan ionisasi: $K_{a1} = 4 \\times 10^{-7}$ dan $K_{a2} = 5 \\times 10^{-11}$, serta $K_w = 1 \\times 10^{-14}$. Nilai pH larutan natrium karbonat tersebut berdasarkan hidrolisis tahap pertamanya adalah...",
        "correct": "$\\text{pH} = 11{,}65$ (karena $[\\text{OH}^-] \\approx 4{,}47 \\times 10^{-3}\\text{ M}$), karena anion karbonat ($\\text{CO}_3^{2-}$) mengalami hidrolisis tahap pertama melepaskan ion hidroksida: $\\text{CO}_3^{2-} + \\text{H}_2\\text{O} \\rightleftharpoons \\text{HCO}_3^- + \\text{OH}^-$ dengan tetapan hidrolisis $K_{h1} = \\frac{K_w}{K_{a2}} = \\frac{10^{-14}}{5 \\times 10^{-11}} = 2 \\times 10^{-4}$. Konsentrasi ion hidroksida dihitung dari $[\\text{OH}^-] = \\sqrt{K_{h1} [\\text{CO}_3^{2-}]} = \\sqrt{(2 \\times 10^{-4}) \\times 0{,}1} = \\sqrt{2 \\times 10^{-5}} = \\sqrt{20 \\times 10^{-6}} \\approx 4{,}47 \\times 10^{-3}\\text{ M}$. Maka $\\text{pOH} = 3 - \\log(4{,}47) \\approx 2{,}35$, sehingga $\\text{pH} = 14 - 2{,}35 = 11{,}65$.",
        "distractors": [
            "$\\text{pH} = 9{,}70$, karena tetapan hidrolisis keliru dihitung menggunakan Ka1 bukan Ka2 dari asam diprotik.",
            "$\\text{pH} = 13{,}00$, karena larutan garam dianggap terdisosiasi sempurna menghasilkan basa kuat bebas.",
            "$\\text{pH} = 7{,}00$, karena menganggap hidrolisis tahap kedua menetralkan seluruh ion hidroksida tahap pertama.",
            "$\\text{pH} = 8{,}35$, dihitung dari nilai logaritma konsentrasi garam tanpa memperhitungkan tetapan kesetimbangan air."
        ],
        "formula": {
            "title": "HIDROLISIS TAHAP PERTAMA ANION KARBONAT",
            "latex": "K_{h1} = \\frac{K_w}{K_{a2}} = \\frac{10^{-14}}{5 \\times 10^{-11}} = 2 \\times 10^{-4}; \\quad [\\text{OH}^-] = \\sqrt{K_{h1} C} = \\sqrt{2 \\times 10^{-5}} \\approx 4{,}47 \\times 10^{-3}\\text{ M}; \\quad \\text{pH} = 14 - \\text{pOH} \\approx 11{,}65",
            "legend": "• Hidrolisis tahap pertama sangat dominan dibandingkan tahap kedua ($K_{h1} \\gg K_{h2}$)<br>• $K_{h2} = K_w / K_{a1} = 10^{-14} / 4 \\times 10^{-7} = 2{,}5 \\times 10^{-8}$ dapat diabaikan<br>• $\\text{pH} = 11{,}65$ (bersifat sangat basa)"
        },
        "hints": {
            "concept": "Garam Na2CO3 terhidrolisis menghasilkan OH-: CO3(2-) + H2O <-> HCO3- + OH-. Tetapan hidrolisis Kh1 = Kw / Ka2. Hitung [OH-] = sqrt(Kh1 * [garam]), lalu pH = 14 - pOH.",
            "execution": "Kh1 = 1e-14 / 5e-11 = 2e-4. [OH-] = sqrt(2e-4 * 0,1) = sqrt(2e-5) = 4,47e-3 M. pOH = 2,35 -> pH = 11,65."
        }
    },
    {
        "id": "kim-lat-h-07",
        "materi": "KELARUTAN FRAKSIONAL & PEMISAHAN ION",
        "topic": "Pengendapan Selektif Campuran Kation Halida",
        "stem": "Suatu larutan mengandung ion $\\text{Ag}^+$ berkonsentrasi $0{,}01\\text{ M}$ dan ion $\\text{Pb}^{2+}$ berkonsentrasi $0{,}01\\text{ M}$. Ke dalam larutan tersebut diteteskan larutan $\\text{NaCl}$ encer secara perlahan. Diketahui $K_{sp}\\,\\text{AgCl} = 1{,}8 \\times 10^{-10}$ dan $K_{sp}\\,\\text{PbCl}_2 = 1{,}7 \\times 10^{-5}$. Kation yang mengendap pertama kali dan konsentrasi ion klorida ($[\\text{Cl}^-]$) saat endapan kedua tepat mulai terbentuk berturut-turut adalah...",
        "correct": "$\\text{Ag}^+$ mengendap pertama kali, dan endapan kedua ($\\text{PbCl}_2$) tepat mulai terbentuk pada saat $[\\text{Cl}^-] = \\sqrt{1{,}7 \\times 10^{-3}} \\approx 4{,}12 \\times 10^{-2}\\text{ M}$, karena $\\text{AgCl}$ mulai mengendap saat $[\\text{Cl}^-] = \\frac{K_{sp}\\,\\text{AgCl}}{[\\text{Ag}^+]} = \\frac{1{,}8 \\times 10^{-10}}{0{,}01} = 1{,}8 \\times 10^{-8}\\text{ M}$ (jauh lebih kecil, sehingga $\\text{Ag}^+$ mengendap jauh lebih dulu). Endapan $\\text{PbCl}_2$ baru mulai mengendap saat $[\\text{Cl}^-] = \\sqrt{\\frac{K_{sp}\\,\\text{PbCl}_2}{[\\text{Pb}^{2+}]}} = \\sqrt{\\frac{1{,}7 \\times 10^{-5}}{0{,}01}} = \\sqrt{1{,}7 \\times 10^{-3}} \\approx 4{,}12 \\times 10^{-2}\\text{ M}$.",
        "distractors": [
            "$\\text{Pb}^{2+}$ mengendap pertama kali karena memiliki koefisien ion klorida berpangkat dua.",
            "$\\text{Ag}^+$ mengendap pertama kali, dan endapan kedua mulai terbentuk pada saat $[\\text{Cl}^-] = 1{,}7 \\times 10^{-3}\\text{ M}$ tanpa menarik akar kuadrat.",
            "Kedua kation mengendap secara bersamaan karena memiliki konsentrasi molaritas awal yang identik.",
            "$\\text{Pb}^{2+}$ mengendap pertama kali saat konsentrasi klorida mencapai sepuluh pangkat minus lima molar."
        ],
        "formula": {
            "title": "PENGENDAPAN FRAKSIONAL SELEKTIF",
            "latex": "[\\text{Cl}^-]_{\\text{AgCl}} = \\frac{1{,}8 \\times 10^{-10}}{10^{-2}} = 1{,}8 \\times 10^{-8}\\text{ M}; \\quad [\\text{Cl}^-]_{\\text{PbCl}_2} = \\sqrt{\\frac{1{,}7 \\times 10^{-5}}{10^{-2}}} = \\sqrt{1{,}7 \\times 10^{-3}} \\approx 4{,}12 \\times 10^{-2}\\text{ M}",
            "legend": "• Ion yang membutuhkan $[\\text{Cl}^-]$ terendah mengendap lebih dulu ($\\text{AgCl}$ pada $1{,}8 \\times 10^{-8}\\text{ M}$)<br>• Saat $\\text{PbCl}_2$ mulai mengendap, sisa $[\\text{Ag}^+]$ tinggal $\\frac{1{,}8 \\times 10^{-10}}{4{,}12 \\times 10^{-2}} \\approx 4{,}37 \\times 10^{-9}\\text{ M}$ (hampir $100\\%$ terpisah)"
        },
        "hints": {
            "concept": "Hitung [Cl-] yang dibutuhkan untuk mulai mengendapkan AgCl: [Cl-] = Ksp(AgCl) / [Ag+]. Hitung [Cl-] untuk PbCl2: [Cl-] = sqrt(Ksp(PbCl2) / [Pb2+]). Yang butuh konsentrasi lebih kecil mengendap duluan.",
            "execution": "[Cl-] AgCl = 1,8e-8 M (mengendap pertama). [Cl-] PbCl2 = sqrt(1,7e-5 / 0,01) = 4,12 x 10^-2 M."
        }
    },
    {
        "id": "kim-lat-h-08",
        "materi": "TERMODINAMIKA KIMIA (ENERGI BEBAS GIBBS)",
        "topic": "Suhu Kespontanan Reaksi Endotermik Dekomposisi",
        "stem": "Reaksi penguraian termal batu kapur memenuhi persamaan termodinamika:<br>$$\\text{CaCO}_3(s) \\to \\text{CaO}(s) + \\text{CO}_2(g)$$<br>Diketahui perubahan entalpi standar reaksi adalah $\\Delta H^\\circ = +178\\text{ kJ/mol}$ dan perubahan entropi standar adalah $\\Delta S^\\circ = +160\\text{ J/(mol}\\cdot\\text{K)}$. Mengasumsikan $\\Delta H^\\circ$ dan $\\Delta S^\\circ$ tidak berubah terhadap suhu, suhu minimum ($T$) agar reaksi penguraian tersebut berlangsung spontan pada tekanan 1 atm adalah...",
        "correct": "$T > 1.112{,}5\\text{ K}$ (atau di atas $839{,}5^\\circ\\text{C}$), karena syarat kespontanan menurut kriteria Gibbs adalah $\\Delta G^\\circ = \\Delta H^\\circ - T \\Delta S^\\circ < 0$. Pada titik transisi kesetimbangan $\\Delta G^\\circ = 0$, suhu tercapai saat $T = \\frac{\\Delta H^\\circ}{\\Delta S^\\circ} = \\frac{178.000\\text{ J/mol}}{160\\text{ J/(mol}\\cdot\\text{K)}} = 1.112{,}5\\text{ K}$. Agar reaksi berjalan spontan ($\\Delta G^\\circ < 0$), suhu sistem harus dinaikkan melebihi $1.112{,}5\\text{ Kelvin}$.",
        "distractors": [
            "$T < 1.112{,}5\\text{ K}$, karena salah mengasumsikan reaksi endotermik lebih spontan pada suhu rendah.",
            "$T > 890\\text{ K}$, karena satuan kiloJoule pada entalpi tidak dikonversikan ke satuan Joule saat pembagian entropi.",
            "$T > 2.225\\text{ K}$, dihitung dari penggandaan suhu akibat adanya dua partikel produk dekomposisi.",
            "$T < 273\\text{ K}$, karena beranggapan seluruh reaksi spontan hanya dapat berlangsung di bawah titik beku es."
        ],
        "formula": {
            "title": "KRITERIA KESPONTANAN ENERGI BEBAS GIBBS",
            "latex": "\\Delta G^\\circ = \\Delta H^\\circ - T \\Delta S^\\circ < 0 \\implies T > \\frac{\\Delta H^\\circ}{\\Delta S^\\circ} = \\frac{178 \\times 10^3\\text{ J/mol}}{160\\text{ J/(mol}\\cdot\\text{K)}} = 1.112{,}5\\text{ K} = 839{,}5^\\circ\\text{C}",
            "legend": "• $\\Delta H > 0$ dan $\\Delta S > 0 \\implies$ Spontan pada suhu tinggi ($T > \\Delta H / \\Delta S$)<br>• Pada suhu kamar ($298\\text{ K}$), $\\Delta G^\\circ > 0$ sehingga batu kapur sangat stabil dan tidak terurai"
        },
        "hints": {
            "concept": "Syarat spontan: Delta G = Delta H - T * Delta S < 0. Suhu saat setimbang T = Delta H / Delta S. Konversi Delta H ke Joule: 178 kJ = 178.000 J.",
            "execution": "T = 178.000 / 160 = 1.112,5 K. Suhu harus T > 1.112,5 K."
        }
    },
    {
        "id": "kim-lat-h-09",
        "materi": "TERMODINAMIKA (DELTA G STANDAR & K)",
        "topic": "Hubungan Delta G Standar dengan Tetapan Kesetimbangan K",
        "stem": "Suatu reaksi kimia isomerisasi fasa gas $A(g) \\rightleftharpoons B(g)$ memiliki tetapan kesetimbangan $K_p = 100$ pada suhu $T = 300\\text{ K}$. Jika tetapan gas ideal $R = 8{,}314\\text{ J/(mol}\\cdot\\text{K)}$ dan $\\ln 100 \\approx 4{,}605$, nilai perubahan energi bebas Gibbs standar ($\\Delta G^\\circ$) untuk reaksi isomerisasi tersebut adalah...",
        "correct": "$\\Delta G^\\circ \\approx -11{,}49\\text{ kJ/mol}$, karena menurut hubungan fundamental termodinamika kimia: $\\Delta G^\\circ = -R T \\ln K = -(8{,}314\\text{ J/(mol}\\cdot\\text{K)}) \\times 300\\text{ K} \\times \\ln(100) = -(2.494{,}2) \\times 4{,}605 = -11.485{,}8\\text{ J/mol} \\approx -11{,}49\\text{ kJ/mol}$.",
        "distractors": [
            "$\\Delta G^\\circ \\approx +11{,}49\\text{ kJ/mol}$, karena salah menghilangkan tanda minus pada perumusan potensial termodinamika isotermal.",
            "$\\Delta G^\\circ \\approx -2{,}49\\text{ kJ/mol}$, dihitung tanpa mengalikan nilai logaritma natural tetapan kesetimbangan.",
            "$\\Delta G^\\circ \\approx -23{,}0\\text{ kJ/mol}$, karena keliru menggunakan nilai logaritma desimal basis 10 dikalikan faktor dua.",
            "$\\Delta G^\\circ = 0\\text{ kJ/mol}$, karena menyamakan energi bebas Gibbs standar dengan energi bebas saat campuran telah mencapai kesetimbangan dinamis."
        ],
        "formula": {
            "title": "RELASI ENERGI BEBAS GIBBS DENGAN KESETIMBANGAN",
            "latex": "\\Delta G^\\circ = -R T \\ln K = -8{,}314 \\times 300 \\times 4{,}605 = -11.486\\text{ J/mol} = -11{,}49\\text{ kJ/mol}",
            "legend": "• $K > 1 \\implies \\ln K > 0 \\implies \\Delta G^\\circ < 0$ (Pembentukan produk sangat disukai secara termodinamika)<br>• Catatan: $\\Delta G = 0$ pada keadaan setimbang, namun $\\Delta G^\\circ \\ne 0$"
        },
        "hints": {
            "concept": "Gunakan Delta G0 = -R * T * ln(K). R = 8,314 J/(mol.K), T = 300 K, ln(100) = 4,605.",
            "execution": "Delta G0 = -8,314 * 300 * 4,605 = -11.486 J/mol = -11,49 kJ/mol."
        }
    },
    {
        "id": "kim-lat-h-10",
        "materi": "KINETIKA KIMIA (PERSAMAAN ARRHENIUS)",
        "topic": "Penentuan Energi Aktivasi Reaksi dari Dua Suhu Berbeda",
        "stem": "Konstanta laju reaksi ($k$) untuk suatu reaksi dekomposisi meningkat dua kali lipat ($k_2 = 2 k_1$) ketika suhu reaksi dinaikkan dari $T_1 = 300\\text{ K}$ menjadi $T_2 = 310\\text{ K}$. Diketahui tetapan gas umum $R = 8{,}314\\text{ J/(mol}\\cdot\\text{K)}$ dan $\\ln 2 \\approx 0{,}693$. Besar energi aktivasi ($E_a$) dari reaksi dekomposisi tersebut adalah...",
        "correct": "$E_a \\approx 53{,}58\\text{ kJ/mol}$, karena menurut bentuk linear persamaan Arrhenius dua suhu: $\\ln\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{R} \\left(\\frac{1}{T_1} - \\frac{1}{T_2}\\right) = \\frac{E_a}{R} \\left(\\frac{T_2 - T_1}{T_1 T_2}\\right)$. Substitusi data: $0{,}693 = \\frac{E_a}{8{,}314} \\left(\\frac{10}{300 \\times 310}\\right) = \\frac{E_a}{8{,}314} \\left(\\frac{10}{93.000}\\right) \\implies E_a = \\frac{0{,}693 \\times 8{,}314 \\times 93.000}{10} = \\frac{535.824}{10} \\approx 53.582\\text{ J/mol} \\approx 53{,}58\\text{ kJ/mol}$.",
        "distractors": [
            "$E_a \\approx 26{,}79\\text{ kJ/mol}$, karena faktor selisih suhu keliru digandakan menjadi dua puluh derajat.",
            "$E_a \\approx 107{,}16\\text{ kJ/mol}$, dihitung dari pemangkatan kuadrat rasio konstanta laju reaksi.",
            "$E_a \\approx 5{,}36\\text{ kJ/mol}$, karena galat konversi dari satuan Joule ke kiloJoule.",
            "$E_a \\approx 83{,}14\\text{ kJ/mol}$, dihitung dari perkalian langsung konstanta gas dengan kelipatan suhu mutlak."
        ],
        "formula": {
            "title": "PERSAMAAN ARRHENIUS DUA SUHU",
            "latex": "\\ln\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{R} \\left(\\frac{T_2 - T_1}{T_1 T_2}\\right) \\implies E_a = \\frac{R \\cdot T_1 T_2 \\cdot \\ln(k_2/k_1)}{T_2 - T_1} = \\frac{8{,}314 \\times 300 \\times 310 \\times 0{,}693}{10} \\approx 53{,}58\\text{ kJ/mol}",
            "legend": "• $E_a$ menyatakan batas energi penghalang minimum yang harus dilampaui molekul agar tumbukan menghasilkan reaksi kimia<br>• $E_a \\approx 53{,}58\\text{ kJ/mol}$"
        },
        "hints": {
            "concept": "Persamaan Arrhenius: ln(k2/k1) = (Ea / R) * (1/T1 - 1/T2). Ea = R * ln(2) * (T1 * T2) / (T2 - T1).",
            "execution": "Ea = 8,314 * 0,693 * (300 * 310) / 10 = 5,7616 * 9.300 = 53.583 J/mol = 53,58 kJ/mol."
        }
    },
    {
        "id": "kim-lat-h-11",
        "materi": "ELEKTROKIMIA (PERSAMAAN NERNEST)",
        "topic": "Potensial Sel Non-Standar Sel Daniell",
        "stem": "Sebuah sel Volta Daniell dirangkai dengan reaksi sel:<br>$$\\text{Zn}(s) + \\text{Cu}^{2+}(aq) \\to \\text{Zn}^{2+}(aq) + \\text{Cu}(s) \\quad E^\\circ_{\\text{sel}} = +1{,}10\\text{ Volt}$$<br>Sel dioperasikan pada suhu $25^\\circ\\text{C}$ dengan konsentrasi ion $[\\text{Zn}^{2+}] = 0{,}1\\text{ M}$ dan konsentrasi ion $[\\text{Cu}^{2+}] = 0{,}001\\text{ M} = 10^{-3}\\text{ M}$. Berdasarkan persamaan Nernst ($E_{\\text{sel}} = E^\\circ_{\\text{sel}} - \\frac{0{,}0592}{n} \\log Q$), besar potensial sel non-standar ($E_{\\text{sel}}$) yang dihasilkan adalah...",
        "correct": "$E_{\\text{sel}} = 1{,}0408\\text{ Volt}$ (atau sekitar $1{,}04\\text{ V}$), karena jumlah transfer elektron dalam reaksi adalah $n = 2$. Kuosien reaksi adalah $Q = \\frac{[\\text{Zn}^{2+}]}{[\\text{Cu}^{2+}]} = \\frac{0{,}1}{10^{-3}} = 100 = 10^2$, sehingga $\\log Q = 2$. Menurut persamaan Nernst: $E_{\\text{sel}} = 1{,}10\\text{ V} - \\frac{0{,}0592}{2} \\log(100) = 1{,}10 - (0{,}0296 \\times 2) = 1{,}10 - 0{,}0592 = 1{,}0408\\text{ Volt}$.",
        "distractors": [
            "$E_{\\text{sel}} = 1{,}1592\\text{ Volt}$, karena suku koreksi Nernst keliru ditambahkan pada potensial sel standar padahal konsentrasi produk lebih besar dari reaktan.",
            "$E_{\\text{sel}} = 1{,}1000\\text{ Volt}$, karena mengabaikan pengaruh perbedaan konsentrasi larutan elektrolit.",
            "$E_{\\text{sel}} = 0{,}9816\\text{ Volt}$, dihitung dari pemangkatan kuadrat jumlah transfer elektron pada penyebut.",
            "$E_{\\text{sel}} = 1{,}0704\\text{ Volt}$, dihitung dengan membagi suku Nernst dengan faktor empat.",
        ],
        "formula": {
            "title": "PERSAMAAN NERNST PADA SUHU 298 K",
            "latex": "E_{\\text{sel}} = E^\\circ_{\\text{sel}} - \\frac{0{,}0592}{n} \\log Q = 1{,}10 - \\frac{0{,}0592}{2} \\log\\left(\\frac{0{,}1}{10^{-3}}\\right) = 1{,}10 - 0{,}0296(2) = 1{,}0408\\text{ V}",
            "legend": "• $n = 2$ (transfer 2 mol elektron)<br>• $Q = 100 \\implies E_{\\text{sel}} < E^\\circ_{\\text{sel}}$ (penurunan voltase seiring berkurangnya reaktan $\\text{Cu}^{2+}$)"
        },
        "hints": {
            "concept": "Persamaan Nernst: E_sel = E0_sel - (0,0592 / n) * log(Q). n = 2. Q = [Zn2+] / [Cu2+] = 0,1 / 1e-3 = 100. log(100) = 2.",
            "execution": "E_sel = 1,10 - (0,0592 / 2) * 2 = 1,10 - 0,0592 = 1,0408 Volt."
        }
    },
    {
        "id": "kim-lat-h-12",
        "materi": "ELEKTROLISIS INDUSTRI (ELEKTROREFINING TEMBAGA)",
        "topic": "Pemurnian Tembaga dan Pembentukan Lumpur Anoda",
        "stem": "Dalam proses pemurnian tembaga secara elektrolisis di industri (electrorefining), kawat tembaga murni dijadikan katoda dan lempengan tembaga kasar (blister copper) yang mengandung pengotor besi, seng, emas, dan perak dijadikan anoda di dalam larutan elektrolit $\\text{CuSO}_4$ diasamkan. Peristiwa elektrokimia yang terjadi pada pengotor seng, emas, dan perak selama proses berlangsung adalah...",
        "correct": "Seng teroksidasi menjadi ion $\\text{Zn}^{2+}$ dan larut tetap berada di dalam larutan elektrolit karena potensial reduksinya sangat negatif sehingga tidak tereduksi di katoda, sedangkan emas dan perak tidak teroksidasi di anoda dan jatuh mengendap ke dasar bejana membentuk lumpur anoda (anode slime) yang bernilai ekonomis tinggi.",
        "distractors": [
            "Seluruh pengotor seng, emas, dan perak ikut teroksidasi dan terendapkan bersama tembaga di katoda.",
            "Emas dan perak teroksidasi membentuk ion kompleks larut, sedangkan seng mengendap di dasar sel elektrolisis.",
            "Seng, emas, dan perak bereaksi dengan gas belerang membentuk lapisan pasivasi yang menghentikan arus listrik.",
            "Pengotor emas dan perak menguap sebagai gas mulia beracun di atas permukaan sel elektrolisis industri."
        ],
        "formula": {
            "title": "ELEKTROREFINING BLISTER TEMBAGA",
            "latex": "\\begin{aligned} \\text{Anoda (Oksidasi): } & \\text{Cu}(s) \\to \\text{Cu}^{2+} + 2e^-; \\quad \\text{Zn, Fe teroksidasi jadi ion larut} \\\\ \\text{Lumpur Anoda: } & \\text{Ag, Au, Pt tidak teroksidasi (}\\text{karena } E^\\circ > E^\\circ_{\\text{Cu}}\\text{) dan mengendap} \\\\ \\text{Katoda (Reduksi): } & \\text{Cu}^{2+} + 2e^- \\to \\text{Cu}(s) \\quad (\\text{Hanya Cu tereduksi murni 99,99\\%}) \\end{aligned}"
        },
        "hints": {
            "concept": "Logam lebih aktif dari Cu (Zn, Fe, E0 lebih negatif) teroksidasi jadi ion di larutan. Logam lebih mulia dari Cu (Ag, Au, E0 lebih positif) tidak teroksidasi dan jatuh jadi lumpur anoda.",
            "execution": "Zn larut sebagai ion di elektrolit, Au dan Ag mengendap menjadi lumpur anoda."
        }
    },
    {
        "id": "kim-lat-h-13",
        "materi": "KIMIA ORGANIK (MEKANISME SUBSTITUSI NUKLEOFILIK)",
        "topic": "Komparasi Mekanisme Reaksi SN1 dan SN2",
        "stem": "Reaksi substitusi nukleofilik antara alkil halida dengan ion hidroksida dapat berlangsung melalui mekanisme $S_N1$ atau $S_N2$. Karakteristik yang benar membedakan reaksi $S_N1$ pada ters-butil bromida dengan reaksi $S_N2$ pada metil bromida adalah...",
        "correct": "Reaksi $S_N1$ berlangsung dua tahap melalui pembentukan zat antara karbokation datar yang menghasilkan rasemisasi optik (inversi dan retensi), sedangkan reaksi $S_N2$ berlangsung satu tahap serentak (concerted) dengan serangan nukleofil dari arah belakang yang menghasilkan inversi konfigurasi Walden $100\\%$.",
        "distractors": [
            "Reaksi $S_N1$ berlangsung satu tahap dengan keadaan transisi siklik, sedangkan $S_N2$ berlangsung melalui zat antara radikal bebas.",
            "Reaksi $S_N1$ sangat dipengaruhi oleh kekuatan nukleofil sedangkan $S_N2$ lajunya hanya bergantung pada konsentrasi substrat alkil halida.",
            "Reaksi $S_N1$ menghasilkan pembalikan konfigurasi Walden murni, sedangkan $S_N2$ selalu menghasilkan produk retensi.",
            "Reaksi $S_N1$ lebih disukai oleh pelarut aprotik nonpolar sedangkan $S_N2$ membutuhkan pelarut protik berair kuat."
        ],
        "formula": {
            "title": "MEKANISME SUBSTITUSI NUKLEOFILIK (SN1 VS SN2)",
            "latex": "\\begin{aligned} S_N1: & \\quad v = k[\\text{R-X}] \\quad (\\text{Karbokation 3}^\\circ, \\text{Rasemisasi}, \\text{Pelarut Protik Polar}) \\\\ S_N2: & \\quad v = k[\\text{R-X}][\\text{Nu}^-] \\quad (\\text{Serangan Belakang 1}^\\circ, \\text{Inversi Walden}, \\text{Pelarut Aprotik}) \\end{aligned}"
        },
        "hints": {
            "concept": "SN1: 2 tahap via intermediat karbokation datar -> menghasilkan campuran rasemat. SN2: 1 tahap serentak (serangan nukleofil dari belakang) -> menghasilkan inversi Walden 100%.",
            "execution": "SN1 via karbokation menghasilkan rasemisasi; SN2 satu tahap menghasilkan inversi Walden."
        }
    },
    {
        "id": "kim-lat-h-14",
        "materi": "KIMIA ORGANIK (REAKSI ELIMINASI & ATURAN ZAITSEV)",
        "topic": "Regioselektifitas Dehidrohalogenasi Alkil Halida",
        "stem": "Senyawa 2-bromobutana dipanaskan bersama larutan kalium hidroksida dalam alkohol ($\\text{KOH/etanol}$). Berdasarkan Aturan Zaitsev (Saytzeff), produk utama yang dihasilkan beserta alasan regioselektifitasnya adalah...",
        "correct": "2-butena (khususnya trans-2-butena), karena aturan Zaitsev menyatakan bahwa eliminasi hidrogen halida dari alkil halida akan mendominasi pembentukan alkena yang memiliki gugus alkil substituen terbanyak (alkena terdisubstitusi yang secara termodinamika memiliki kestabilan ikatan pi lebih tinggi dibanding 1-butena monosubstitusi).",
        "distractors": [
            "1-butena, karena proton hidrogen pada karbon nomor satu paling mudah diserang oleh basa kuat karena rintangan sterik minimal.",
            "2-butanol, karena terjadi reaksi substitusi nukleofilik murni tanpa eliminasi ikatan rangkap.",
            "Siklobutana, karena rantai karbon mengalami penutupan cincin intramolekuler.",
            "Butuna, karena terjadi pelepasan dua molekul asam bromida secara simultan."
        ],
        "formula": {
            "title": "ATURAN ELIMINASI ZAITSEV",
            "latex": "\\text{CH}_3-\\text{CH}_2-\\text{CH(Br)}-\\text{CH}_3 + \\text{KOH} \\xrightarrow{\\text{Etanol, } \\Delta} \\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3 \\text{ (2-butena, } 80\\%\\text{)} + \\text{CH}_3-\\text{CH}_2-\\text{CH}=\\text{CH}_2 \\text{ (1-butena, } 20\\%)",
            "legend": "• Produk Zaitsev (2-butena) = Alkena terdisubstitusi (lebih stabil akibat hiperkonjugasi)<br>• Produk Hofmann (1-butena) = Alkena termonosubstitusi (produk minor)"
        },
        "hints": {
            "concept": "Aturan Zaitsev: pada eliminasi dehidrohalogenasi, produk utama adalah alkena dengan substituen terbanyak (paling stabil). 2-butena (disubstitusi) adalah produk utama.",
            "execution": "2-butena (produk Zaitsev yang lebih stabil)."
        }
    },
    {
        "id": "kim-lat-h-15",
        "materi": "KIMIA AROMATIK (SUBSTITUSI ELEKTROFILIK BENZENA)",
        "topic": "Pengaruh Pengarah Substituen Orto-Para vs Meta pada Benzena",
        "stem": "Fenol direaksikan dengan campuran asam nitrat encer dan asam sulfat encer pada suhu kamar menghasilkan campuran senyawa orto-nitrofenol dan para-nitrofenol. Sedangkan reaksi nitrasi pada nitrobenzena membutuhkan kondisi asam pekat berpemanas tinggi dan menghasilkan meta-dinitrobenzena. Alasan mendasar perbedaan orientasi dan reaktivitas cincin aromatik tersebut adalah...",
        "correct": "Gugus hidroksil ($-\\text{OH}$) pada fenol memiliki pasangan elektron bebas yang didonorkan ke cincin benzena melalui resonansi ($+M$), bersifat pengaktif kuat cincin dan mengarahkan elektrofil baru ke posisi orto dan para; sedangkan gugus nitro ($-\\text{NO}_2$) bersifat penarik elektron kuat ($-M$ dan $-I$) yang mendeaktivasi cincin dan mengarahkan elektrofil ke posisi meta yang kerapatan elektronnya paling sedikit berkurang.",
        "distractors": [
            "Gugus $-\\text{OH}$ bersifat penarik elektron kuat melalui efek induksi sehingga mendeaktivasi posisi meta cincin aromatik.",
            "Gugus $-\\text{NO}_2$ mendonorkan pasangan elektron bebas nitrogen ke cincin sehingga mengaktifkan posisi meta secara spesifik.",
            "Fenol mengalami reaksi adisi ikatan rangkap benzena sedangkan nitrobenzena mengalami reaksi substitusi nukleofilik aromatik.",
            "Perbedaan orientasi disebabkan semata-mata oleh perbedaan massa molar kedua substituen organik."
        ],
        "formula": {
            "title": "EFEK PENGARAH SUBSTITUEN PADA CINCIN BENZENA",
            "latex": "\\begin{aligned} \\text{Pengarah Orto-Para (Aktivator): } & -\\text{OH}, -\\text{NH}_2, -\\text{OCH}_3, -\\text{R} \\quad (\\text{Donasi resonansi } +M) \\\\ \\text{Pengarah Meta (Deaktivator): } & -\\text{NO}_2, -\\text{COOH}, -\\text{CHO}, -\\text{CN} \\quad (\\text{Penarik elektron } -M, -I) \\end{aligned}"
        },
        "hints": {
            "concept": "-OH adalah aktivator cincin (mendonorkan PEB via resonansi), mengarahkan ke orto dan para. -NO2 adalah deaktivator kuat (menarik elektron dari cincin), mengarahkan ke meta.",
            "execution": "-OH aktivator pengarah orto-para; -NO2 deaktivator pengarah meta."
        }
    },
    {
        "id": "kim-lat-h-16",
        "materi": "BIOKIMIA (ASAM AMINO & TITIK ISOELEKTRIK)",
        "topic": "Bentuk Zwitterion dan Perhitungan Titik Isoelektrik Alanin",
        "stem": "Asam amino alanin memiliki dua gugus yang dapat terionisasi dengan nilai $\\text{p}K_{a1} = 2{,}34$ (gugus karboksilat $-\\text{COOH}$) dan $\\text{p}K_{a2} = 9{,}69$ (gugus amino $-\\text{NH}_3^+$). Pada pH berapakah alanin berada dalam bentuk zwitterion netral dominan (titik isoelektrik, pI) dan bagaimana arah migrasinya dalam medan elektroforesis pada $\\text{pH} = 11$?",
        "correct": "Titik isoelektrik $\\text{pI} = 6{,}015$ dan pada $\\text{pH} = 11$ alanin bermuatan negatif sehingga bermigrasi menuju kutub anoda positif, karena titik isoelektrik dihitung dari rata-rata $\\text{pI} = \\frac{\\text{p}K_{a1} + \\text{p}K_{a2}}{2} = \\frac{2{,}34 + 9{,}69}{2} = \\frac{12{,}03}{2} = 6{,}015$. Pada lingkungan sangat basa ($\\text{pH } 11 > \\text{pI}$), gugus amino melepaskan protonnya ($-\\text{NH}_2$) sementara karboksilat tetap terionisasi ($-\\text{COO}^-$), sehingga menghasilkan ion bermuatan negatif netto (anion) yang ditarik oleh anoda.",
        "distractors": [
            "$\\text{pI} = 7{,}00$ dan pada $\\text{pH } 11$ alanin diam di tempat tidak bermigrasi karena bermuatan netral.",
            "$\\text{pI} = 6{,}015$ dan pada $\\text{pH } 11$ alanin bermuatan positif sehingga bermigrasi menuju kutub katoda negatif.",
            "$\\text{pI} = 2{,}34$ dan pada $\\text{pH } 11$ alanin terurai menjadi gas amonia dan asam laktat.",
            "$\\text{pI} = 9{,}69$ dan pada $\\text{pH } 11$ alanin mengendap sebagai kristal padat tak larut."
        ],
        "formula": {
            "title": "TITIK ISOELEKTRIK ASAM AMINO DIPROTIK",
            "latex": "\\text{pI} = \\frac{\\text{p}K_{a1} + \\text{p}K_{a2}}{2} = \\frac{2{,}34 + 9{,}69}{2} = 6{,}015; \\quad \\text{Pada pH } > \\text{pI}: \\text{Bentuk Anion } \\text{H}_2\\text{N-CH(CH}_3\\text{)-COO}^- \\implies \\text{Migrasi ke Anoda (+)}",
            "legend": "• Zwitterion netral mendominasi tepat pada $\\text{pH} = \\text{pI}$ (kelarutan minimum)<br>• $\\text{pH} < \\text{pI} \\implies$ Kation (+) bergerak ke Katoda (-)<br>• $\\text{pH} > \\text{pI} \\implies$ Anion (-) bergerak ke Anoda (+)"
        },
        "hints": {
            "concept": "Titik isoelektrik asam amino netral: pI = (pKa1 + pKa2) / 2 = (2,34 + 9,69)/2 = 6,015. Pada pH 11 > pI, asam amino bermuatan negatif (anion) sehingga bergerak ke kutub positif (anoda).",
            "execution": "pI = 6,015; bermuatan negatif dan bermigrasi ke anoda."
        }
    },
    {
        "id": "kim-lat-h-17",
        "materi": "STEREOKIMIA (KONFIGURASI ABSOLUT R/S)",
        "topic": "Penentuan Konfigurasi R/S Cahn-Ingold-Prelog pada Asam Laktat",
        "stem": "Asam laktat memiliki rumus struktur $\\text{CH}_3-\\text{C}^*\\text{H(OH)}-\\text{COOH}$ dengan satu atom karbon kiral ($C^*$). Berdasarkan aturan prioritas Cahn-Ingold-Prelog (CIP), urutan prioritas keempat gugus yang terikat pada karbon kiral dan konfigurasi absolut jika gugus prioritas terendah berada di belakang bidang proyeksi adalah...",
        "correct": "Urutan prioritas: $-\\text{OH} > -\\text{COOH} > -\\text{CH}_3 > -\\text{H}$, karena penentuan didasarkan pada nomor atom yang terikat langsung ($O=8 > C=6 > H=1$). Antara $-\\text{COOH}$ dan $-\\text{CH}_3$, atom karbon pada karboksilat mengikat $(O, O, O)$ sedangkan pada metil mengikat $(H, H, H)$, sehingga $-\\text{COOH}$ memiliki prioritas lebih tinggi. Jika penomoran prioritas $1 \\to 2 \\to 3$ searah jarum jam dengan gugus $4\\,(-\\text{H})$ di belakang, konfigurasinya adalah $(R)$.",
        "distractors": [
            "Urutan prioritas: $-\\text{COOH} > -\\text{OH} > -\\text{CH}_3 > -\\text{H}$ dengan konfigurasi absolut selalu $(S)$.",
            "Urutan prioritas: $-\\text{CH}_3 > -\\text{COOH} > -\\text{OH} > -\\text{H}$ berdasarkan rantai karbon utama terpanjang.",
            "Urutan prioritas: $-\\text{H} > -\\text{CH}_3 > -\\text{COOH} > -\\text{OH}$ diurutkan dari massa molar terkecil ke terbesar.",
            "Urutan prioritas: $-\\text{OH} > -\\text{CH}_3 > -\\text{COOH} > -\\text{H}$ dengan konfigurasi rasemat optis inaktif."
        ],
        "formula": {
            "title": "ATURAN PRIORITAS CAHN-INGOLD-PRELOG (CIP)",
            "latex": "\\text{Prioritas: } (1) -\\text{OH } (Z=8) > (2) -\\text{COOH } (C \\text{ terikat } O,O,O) > (3) -\\text{CH}_3 \\text{ (}C \\text{ terikat } H,H,H) > (4) -\\text{H } (Z=1)",
            "legend": "• Prioritas ditentukan dari nomor atom ($Z$) tertinggi pada titik perbedaan pertama<br>• Putaran $1 \\to 2 \\to 3$ searah jarum jam $\\implies$ Konfigurasi $(R)$ (Rectus)<br>• Putaran berlawanan jarum jam $\\implies$ Konfigurasi $(S)$ (Sinister)"
        },
        "hints": {
            "concept": "Aturan CIP: Nomor atom tertinggi menang: -OH (O=8) nomor 1, -H (H=1) nomor 4. Bandingkan -COOH vs -CH3: C pada -COOH mengikat atom O, sehingga -COOH menang jadi nomor 2, -CH3 nomor 3.",
            "execution": "Prioritas: -OH > -COOH > -CH3 > -H. Konfigurasi (R) jika searah jarum jam."
        }
    },
    {
        "id": "kim-lat-h-18",
        "materi": "KIMIA INTI & PENANGGALAN RADIOMETRIK",
        "topic": "Penanggalan Radiokarbon Karbon-14 pada Fosil Kayu Purba",
        "stem": "Sampel fosil kayu purba dari situs purbakala dianalisis aktivitas radiasi karbon-14 ($^{14}\\text{C}$) miliknya dan diperoleh aktivitas sebesar $A_t = 3{,}125\\text{ dpm/gram karbon}$ (desintegrasi per menit). Sampel kayu hidup modern yang sejenis memiliki aktivitas radiasi awal $A_0 = 12{,}5\\text{ dpm/gram karbon}$. Jika waktu paruh isotop $^{14}\\text{C}$ adalah $T_{1/2} = 5.730\\text{ tahun}$, usia fosil kayu purba tersebut adalah...",
        "correct": "$11.460\\text{ tahun}$, karena rasio aktivitas radiasi sisa terhadap aktivitas awal adalah $\\frac{A_t}{A_0} = \\frac{3{,}125}{12{,}5} = \\frac{1}{4} = \\left(\\frac{1}{2}\\right)^2$. Hal ini menunjukkan bahwa sampel telah meluruh selama $n = 2$ periode waktu paruh. Maka usia fosil tersebut adalah $t = n \\times T_{1/2} = 2 \\times 5.730\\text{ tahun} = 11.460\\text{ tahun}$.",
        "distractors": [
            "$5.730\\text{ tahun}$, karena hanya memperhitungkan 1 periode waktu paruh peluruhan radiasi.",
            "$17.190\\text{ tahun}$, dihitung dari asumsi bahwa zat telah meluruh selama 3 periode paruh.",
            "$22.920\\text{ tahun}$, dihitung dari 4 periode waktu paruh peluruhan radioaktif.",
            "$2.865\\text{ tahun}$, karena waktu paruh keliru dibagi dua alih-alih dikalikan dengan jumlah periode peluruhan."
        ],
        "formula": {
            "title": "PENANGGALAN RADIOKARBON KARBON-14",
            "latex": "\\frac{A_t}{A_0} = \\left(\\frac{1}{2}\\right)^{\\frac{t}{T_{1/2}}} \\implies \\frac{3{,}125}{12{,}5} = \\frac{1}{4} = \\left(\\frac{1}{2}\\right)^2 \\implies \\frac{t}{5.730} = 2 \\implies t = 11.460\\text{ tahun}",
            "legend": "• Karbon-14 terbentuk di atmosfer atas oleh sinar kosmik dan diserap oleh tumbuhan fotosintesis<br>• Setelah organisme mati, penyerapan terhenti dan $^{14}\\text{C}$ meluruh menjadi $^{14}\\text{N}$ dengan $T_{1/2} = 5.730\\text{ tahun}$"
        },
        "hints": {
            "concept": "At / A0 = 3,125 / 12,5 = 1/4 = (1/2)^2. Artinya telah melewati n = 2 kali waktu paruh. Usia fosil t = 2 * 5.730 tahun.",
            "execution": "t = 2 * 5.730 = 11.460 tahun."
        }
    },
    {
        "id": "kim-lat-h-19",
        "materi": "KIMIA POLIMER (POLIMER BIODEGRADABLE)",
        "topic": "Sintesis Asam Polilaktat (PLA) dari Asam Laktat",
        "stem": "Polilaktida atau asam polilaktat (Poly Lactic Acid / PLA) adalah poliester termoplastik ramah lingkungan yang banyak digunakan pada filamen printer 3D dan benang jahit bedah medis yang dapat diserap tubuh. Reaksi pembentukan PLA dari monomer asam 2-hidroksipropanoat (asam laktat) digolongkan sebagai polimerisasi...",
        "correct": "Polimerisasi kondensasi (atau polimerisasi pembukaan cincin ester siklik laktida), karena gugus karboksilat ($-\\text{COOH}$) pada satu molekul bereaksi dengan gugus hidroksil ($-\\text{OH}$) pada molekul lain membentuk ikatan ester (poliester) dengan melepaskan molekul air ($\\text{H}_2\\text{O}$) sebagai produk sampingan.",
        "distractors": [
            "Polimerisasi adisi radikal bebas, karena membuka ikatan rangkap dua karbon-karbon pada asam laktat.",
            "Polimerisasi adisi kationik, karena membutuhkan inisiator asam kuat tanpa melepaskan molekul kecil.",
            "Vulkanisasi silang belerang, karena menghubungkan rantai peptida dengan ikatan disulfida.",
            "Polimerisasi penataan ulang fotokimiawi isomer tanpa adanya reaksi kondensasi gugus fungsi."
        ],
        "formula": {
            "title": "POLIMERISASI POLIESTER ASAM POLILAKTAT (PLA)",
            "latex": "n\\,(\\text{CH}_3-\\text{CH(OH)}-\\text{COOH}) \\xrightarrow{\\text{Kondensasi}} [-\\text{O}-\\text{CH}(\\text{CH}_3)-\\text{CO}-]_n + (n-1)\\,\\text{H}_2\\text{O}",
            "legend": "• Asam laktat memiliki 2 gugus fungsi: $-\\text{OH}$ dan $-\\text{COOH}$ (bifungsional)<br>• Bersifat biokompatibel dan terurai secara alami oleh mikroorganisme menjadi air dan $\\text{CO}_2$"
        },
        "hints": {
            "concept": "Asam laktat memiliki gugus -OH dan -COOH yang bereaksi membentuk ikatan ester dengan melepaskan H2O. Reaksi polimerisasi yang melepaskan molekul kecil (H2O) adalah polimerisasi kondensasi.",
            "execution": "Polimerisasi kondensasi menghasilkan poliester dan air."
        }
    },
    {
        "id": "kim-lat-h-20",
        "materi": "KESETIMBANGAN KIMIA HETEROGEN",
        "topic": "Perhitungan Tekanan Parsial Gas pada Kesetimbangan Heterogen",
        "stem": "Dalam ruang hampa bervolume $10\\text{ liter}$ pada suhu $T = 1.000\\text{ K}$, dimasukkan $100\\text{ gram}$ padatan kalsium karbonat ($\\text{CaCO}_3(s)$). Terjadi reaksi kesetimbangan heterogen:<br>$$\\text{CaCO}_3(s) \\rightleftharpoons \\text{CaO}(s) + \\text{CO}_2(g) \\quad K_p = 0{,}82\\text{ atmosfer}$$<br>Jika pada keadaan setimbang masih terdapat sisa padatan $\\text{CaCO}_3$, tekanan parsial gas $\\text{CO}_2$ di dalam wadah dan massa gas $\\text{CO}_2$ yang berada dalam fasa gas ($M_r\\,\\text{CO}_2 = 44$, $R = 0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)}$) berturut-turut adalah...",
        "correct": "$P_{\\text{CO}_2} = 0{,}82\\text{ atm}$ dan massa $\\text{CO}_2 = 4{,}4\\text{ gram}$, karena pada kesetimbangan heterogen zat berwujud padat murni tidak disertakan dalam persamaan aksi massa, sehingga $K_p = P_{\\text{CO}_2} = 0{,}82\\text{ atm}$. Jumlah mol gas $\\text{CO}_2$ dihitung dari persamaan gas ideal $n = \\frac{P V}{R T} = \\frac{0{,}82\\text{ atm} \\times 10\\text{ L}}{0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)} \\times 1.000\\text{ K}} = \\frac{8{,}2}{82} = 0{,}1\\text{ mol}$. Massa gas adalah $m = 0{,}1\\text{ mol} \\times 44\\text{ g/mol} = 4{,}4\\text{ gram}$.",
        "distractors": [
            "$P_{\\text{CO}_2} = 0{,}41\\text{ atm}$ dan massa $\\text{CO}_2 = 2{,}2\\text{ gram}$, karena tekanan gas keliru dibagi dua oleh keberadaan dua fasa padatan.",
            "$P_{\\text{CO}_2} = 0{,}82\\text{ atm}$ dan massa $\\text{CO}_2 = 44\\text{ gram}$, karena gas dianggap berjumlah satu mol penuh.",
            "$P_{\\text{CO}_2} = 1{,}64\\text{ atm}$ dan massa $\\text{CO}_2 = 8{,}8\\text{ gram}$, dihitung dari penggandaan tekanan kesetimbangan.",
            "$P_{\\text{CO}_2} = 0{,}082\\text{ atm}$ dan massa $\\text{CO}_2 = 0{,}44\\text{ gram}$, karena galat penempatan koma desimal konstanta gas ideal."
        ],
        "formula": {
            "title": "KESETIMBANGAN HETEROGEN DEKOMPOSISI KARBONAT",
            "latex": "K_p = P_{\\text{CO}_2} = 0{,}82\\text{ atm}; \\quad n = \\frac{P V}{R T} = \\frac{0{,}82 \\times 10}{0{,}082 \\times 1.000} = 0{,}1\\text{ mol}; \\quad m = 0{,}1 \\times 44 = 4{,}4\\text{ g}",
            "legend": "• Aktivitas padatan murni $\\text{CaCO}_3(s)$ dan $\\text{CaO}(s)$ sama dengan 1<br>• Tekanan kesetimbangan hanya ditentukan oleh tekanan gas $\\text{CO}_2$<br>• Massa $\\text{CO}_2 = 4{,}4\\text{ gram}$"
        },
        "hints": {
            "concept": "Padatan murni tidak masuk rumus Kp, jadi Kp = P(CO2) = 0,82 atm. Gunakan gas ideal: n = P * V / (R * T) = 0,82 * 10 / (0,082 * 1000) = 0,1 mol. Massa = n * Mr = 0,1 * 44 = 4,4 g.",
            "execution": "P(CO2) = 0,82 atm, massa CO2 = 4,4 gram."
        }
    },
    {
        "id": "kim-lat-h-21",
        "materi": "SIFAT UNSUR TRANSISI (WARNA ION KOMPLEKS)",
        "topic": "Penyerapan Cahaya Transisi d-d dan Warna Komplementer",
        "stem": "Larutan tembaga(II) sulfat yang mengandung ion kompleks $[\text{Cu}(\text{H}_2\text{O})_6]^{2+}$ tampak berwarna biru cerah di mata pengamat. Berdasarkan Teori Medan Kristal dan roda warna komplementer, warna berkas cahaya tampak yang diserap paling kuat oleh larutan tersebut dan mekanisme elektroniknya adalah...",
        "correct": "Menyerap cahaya berwarna jingga (oranye, panjang gelombang $\\approx 600 - 620\\text{ nm}$), dan warna biru yang terlihat adalah warna komplementer yang diteruskan ke mata akibat adanya eksitasi elektron dari orbital $t_{2g}$ ke orbital $e_g$ (transisi $d-d$).",
        "distractors": [
            "Menyerap cahaya berwarna biru cerah dan memancarkan kembali cahaya biru melalui peristiwa fluoresensi foton atomik.",
            "Menyerap sinar ultraviolet tak tampak dan meneruskan seluruh spektrum warna tampak secara seragam.",
            "Menyerap cahaya berwarna hijau dan meneruskan warna merah melalui hamburan Rayleigh intermolekul pelarut.",
            "Menyerap gelombang inframerah termal akibat getaran ikatan kovalen koordinasi ligan air."
        ],
        "formula": {
            "title": "TRANSISI d-d & RODA WARNA KOMPLEMENTER",
            "latex": "\\Delta_o = h \\nu = \\frac{h c}{\\lambda_{\\text{serap}}}; \\quad \\text{Warna Diserap: Jingga } (\\approx 600\\text{ nm}) \\iff \\text{Warna Diteruskan: Biru (Komplementer)}",
            "legend": "• Konfigurasi $\\text{Cu}^{2+} = 3d^9$ (memiliki 1 lubang elektron pada orbital $e_g$)<br>• Penyerapan foton berenergi $\\Delta_o$ mengeksitasi elektron $t_{2g} \\to e_g$<br>• Warna yang diamati mata selalu merupakan warna komplementer dari warna foton yang diserap"
        },
        "hints": {
            "concept": "Warna larutan yang terlihat adalah warna komplementer dari cahaya yang diserap. Warna komplementer dari biru adalah jingga (oranye). Warna muncul karena eksitasi transisi elektron d-d.",
            "execution": "Menyerap cahaya jingga (transisi d-d), warna komplementer biru diteruskan."
        }
    },
    {
        "id": "kim-lat-h-22",
        "materi": "KINETIKA KIMIA (MEKANISME REAKSI MULTITAHAP)",
        "topic": "Tahap Penentu Laju dan Penurunan Hukum Laju Reaksi",
        "stem": "Reaksi pembentukan gas dinitrogen monoksida memiliki persamaan stoikiometri:<br>$$2\\,\\text{NO}(g) + \\text{H}_2(g) \\to \\text{N}_2\\text{O}(g) + \\text{H}_2\\text{O}(g)$$<br>Diusulkan mekanisme reaksi dua tahap sebagai berikut:<br>• Tahap 1 (Cepat, Kesetimbangan): $2\\,\\text{NO}(g) \\rightleftharpoons \\text{N}_2\\text{O}_2(g) \\quad (K_c)$<br>• Tahap 2 (Lambat): $\\text{N}_2\\text{O}_2(g) + \\text{H}_2(g) \\xrightarrow{k_2} \\text{N}_2\\text{O}(g) + \\text{H}_2\\text{O}(g)$<br>Persamaan laju reaksi yang sesuai dengan mekanisme tersebut dan spesi yang bertindak sebagai zat antara (intermediate) adalah...",
        "correct": "$v = k [\\text{NO}]^2 [\\text{H}_2]$ dengan zat antara $\\text{N}_2\\text{O}_2$, karena tahap lambat (tahap 2) adalah tahap penentu laju (Rate-Determining Step / RDS) sehingga $v = k_2 [\\text{N}_2\\text{O}_2][\\text{H}_2]$. Dari kesetimbangan cepat tahap 1: $[\\text{N}_2\\text{O}_2] = K_c [\\text{NO}]^2$. Substitusi ke tahap 2 menghasilkan $v = k_2 K_c [\\text{NO}]^2 [\\text{H}_2] = k [\\text{NO}]^2 [\\text{H}_2]$. Spesi $\\text{N}_2\\text{O}_2$ terbentuk pada tahap 1 dan dikonsumsi pada tahap 2 sehingga berstatus sebagai zat antara.",
        "distractors": [
            "$v = k [\\text{NO}] [\\text{H}_2]$ dengan zat antara $\\text{H}_2\\text{O}$.",
            "$v = k [\\text{N}_2\\text{O}_2] [\\text{H}_2]$ dengan zat antara $\\text{NO}_2$.",
            "$v = k [\\text{NO}]^2 [\\text{H}_2]^2$ dengan zat antara $\\text{N}_2\\text{O}$.",
            "$v = k [\\text{NO}]^2$ dengan zat antara atom oksigen radikal."
        ],
        "formula": {
            "title": "PENENTUAN HUKUM LAJU DARI TAHAP PENENTU LAJU (RDS)",
            "latex": "v = k_2 [\\text{N}_2\\text{O}_2][\\text{H}_2]; \\quad K_c = \\frac{[\\text{N}_2\\text{O}_2]}{[\\text{NO}]^2} \\implies [\\text{N}_2\\text{O}_2] = K_c [\\text{NO}]^2 \\implies v = k [\\text{NO}]^2 [\\text{H}_2]",
            "legend": "• Tahap lambat = Rate Determining Step (RDS)<br>• Zat antara (intermediate) tidak boleh muncul pada persamaan laju reaksi final<br>• $\\text{N}_2\\text{O}_2$ adalah zat antara"
        },
        "hints": {
            "concept": "Laju reaksi ditentukan oleh tahap lambat (tahap 2): v = k2 * [N2O2] * [H2]. Karena N2O2 adalah zat antara, substitusi dari kesetimbangan tahap 1: [N2O2] = Kc * [NO]^2. Maka v = k [NO]^2 [H2].",
            "execution": "v = k [NO]^2 [H2], zat antara = N2O2."
        }
    },
    {
        "id": "kim-lat-h-23",
        "materi": "REAKSI SAPONIFIKASI & BILANGAN PENYABUNAN",
        "topic": "Hidrolisis Basa Trigliserida dan Penentuan Angka Penyabunan",
        "stem": "Suatu sampel minyak nabati berupa trigliserida murni tripalmitin ($\\text{C}_{51}\\text{H}_{98}\\text{O}_6$, $M_r = 806\\text{ g/mol}$) dihidrolisis sempurna dengan larutan kalium hidroksida ($\\text{KOH}$, $M_r = 56\\text{ g/mol}$) menurut reaksi saponifikasi:<br>$$\\text{C}_{51}\\text{H}_{98}\\text{O}_6 + 3\\,\\text{KOH} \\to 3\\,\\text{C}_{15}\\text{H}_{31}\\text{COOK} + \\text{C}_3\\text{H}_5(\\text{OH})_3$$<br>Massa $\\text{KOH}$ dalam miligram yang dibutuhkan untuk menyabunkan secara sempurna $1\\text{ gram}$ minyak tripalmitin tersebut (angka penyabunan / saponification value) adalah...",
        "correct": "$208{,}4\\text{ mg KOH/gram minyak}$, karena satu mol trigliserida membutuhkan tepat 3 mol $\\text{KOH}$ untuk memutus 3 ikatan ester membentuk sabun dan gliserol. Jumlah mol tripalmitin dalam $1\\text{ gram}$ adalah $n = \\frac{1\\text{ g}}{806\\text{ g/mol}} \\approx 1{,}2407 \\times 10^{-3}\\text{ mol}$. Mol $\\text{KOH}$ yang dibutuhkan adalah $3 \\times 1{,}2407 \\times 10^{-3} = 3{,}722 \\times 10^{-3}\\text{ mol}$. Massa $\\text{KOH}$ adalah $m = 3{,}722 \\times 10^{-3}\\text{ mol} \\times 56\\text{ g/mol} \\approx 0{,}2084\\text{ gram} = 208{,}4\\text{ miligram}$.",
        "distractors": [
            "$69{,}5\\text{ mg KOH/gram minyak}$, karena mol KOH keliru dihitung hanya satu mol tanpa dikalikan koefisien tiga trigliserida.",
            "$416{,}8\\text{ mg KOH/gram minyak}$, dihitung dari penggandaan reaksi penyabunan asam lemak bebas.",
            "$806{,}0\\text{ mg KOH/gram minyak}$, karena menyamakan angka penyabunan dengan massa molar trigliserida.",
            "$112{,}0\\text{ mg KOH/gram minyak}$, dihitung dari pembagian massa molar KOH terhadap jumlah ikatan ester."
        ],
        "formula": {
            "title": "RUMUS ANGKA PENYABUNAN (SAPONIFICATION VALUE)",
            "latex": "\\text{Angka Penyabunan} = \\frac{3 \\times M_r(\\text{KOH}) \\times 1.000}{M_r(\\text{Trigliserida})} = \\frac{3 \\times 56 \\times 1.000}{806} = \\frac{168.000}{806} \\approx 208{,}44\\text{ mg KOH/g}",
            "legend": "• Angka penyabunan = miligram KOH untuk menyabunkan 1 gram minyak/lemak<br>• Semakin kecil $M_r$ rata-rata asam lemak, semakin besar angka penyabunannya<br>• Tripalmitin $= 208{,}4\\text{ mg KOH/g}$"
        },
        "hints": {
            "concept": "1 mol trigliserida bereaksi dengan 3 mol KOH. Angka penyabunan = (3 * 56 * 1000) / Mr_minyak. Mr tripalmitin = 806.",
            "execution": "Angka penyabunan = 168.000 / 806 = 208,4 mg KOH/g."
        }
    },
    {
        "id": "kim-lat-h-24",
        "materi": "LARUTAN BINER IDEAL (HUKUM RAOULT)",
        "topic": "Tekanan Uap Total dan Komposisi Uap Campuran Biner",
        "stem": "Dua cairan organik yang saling melarutkan, benzena ($\\text{C}_6\\text{H}_6$) dan toluena ($\\text{C}_7\\text{H}_8$), membentuk larutan ideal pada suhu $25^\\circ\\text{C}$. Pada suhu tersebut, tekanan uap murni benzena adalah $P_B^\\circ = 96\\text{ mmHg}$ dan tekanan uap murni toluena adalah $P_T^\\circ = 32\\text{ mmHg}$. Jika campuran dibuat dengan mencampurkan $1\\text{ mol}$ benzena dan $3\\text{ mol}$ toluena, tekanan uap total campuran ($P_{\\text{total}}$) dan fraksi mol benzena dalam fase uap di atas larutan ($Y_B$) adalah...",
        "correct": "$P_{\\text{total}} = 48\\text{ mmHg}$ dan $Y_B = 0{,}50$ (atau $50\\%$), karena fraksi mol benzena dalam fase cair adalah $X_B = \\frac{1}{1 + 3} = 0{,}25$ dan toluena $X_T = \\frac{3}{4} = 0{,}75$. Menurut Hukum Raoult: tekanan parsial benzena $P_B = X_B \\cdot P_B^\\circ = 0{,}25 \\times 96 = 24\\text{ mmHg}$ dan toluena $P_T = X_T \\cdot P_T^\\circ = 0{,}75 \\times 32 = 24\\text{ mmHg}$. Tekanan total adalah $P_{\\text{total}} = P_B + P_T = 24 + 24 = 48\\text{ mmHg}$. Fraksi mol benzena dalam fase uap adalah $Y_B = \\frac{P_B}{P_{\\text{total}}} = \\frac{24}{48} = 0{,}50$ (uap menjadi lebih kaya akan komponen yang lebih volatil / titik didih lebih rendah).",
        "distractors": [
            "$P_{\\text{total}} = 64\\text{ mmHg}$ dan $Y_B = 0{,}25$, dihitung dari rata-rata tekanan murni dan menyamakan fraksi uap dengan fase cair.",
            "$P_{\\text{total}} = 48\\text{ mmHg}$ dan $Y_B = 0{,}25$, karena mengabaikan peningkatan konsentrasi uap komponen volatil.",
            "$P_{\\text{total}} = 128\\text{ mmHg}$ dan $Y_B = 0{,}75$, dihitung dari penjumlahan langsung kedua tekanan uap murni pelarut.",
            "$P_{\\text{total}} = 36\\text{ mmHg}$ dan $Y_B = 0{,}33$, dihitung dari perbandingan mol terbalik larutan biner."
        ],
        "formula": {
            "title": "HUKUM RAOULT LARUTAN BINER IDEAL",
            "latex": "P_B = X_B P_B^\\circ = 0{,}25(96) = 24\\text{ mmHg}; \\quad P_T = X_T P_T^\\circ = 0{,}75(32) = 24\\text{ mmHg}; \\quad P_{\\text{total}} = 48\\text{ mmHg}; \\quad Y_B = \\frac{P_B}{P_{\\text{total}}} = \\frac{24}{48} = 0{,}50",
            "legend": "• Komponen lebih mudah menguap (benzena, $P^\\circ = 96$) terkonsentrasi di fasa uap ($X_B = 0{,}25 \\to Y_B = 0{,}50$)<br>• Prinsip ini mendasari operasi distilasi fraksionasi minyak bumi"
        },
        "hints": {
            "concept": "Fraksi mol cair: XB = 1/4 = 0,25, XT = 3/4 = 0,75. Tekanan parsial: PB = 0,25 * 96 = 24 mmHg, PT = 0,75 * 32 = 24 mmHg. P_total = 24 + 24 = 48 mmHg. Fraksi mol uap: YB = PB / P_total = 24 / 48 = 0,50.",
            "execution": "P_total = 48 mmHg, YB = 0,50."
        }
    },
    {
        "id": "kim-lat-h-25",
        "materi": "KIMIA POLIMER & KONDENSASI",
        "topic": "Sintesis Nilon-6,6 dan Perhitungan Derajat Polimerisasi",
        "stem": "Polimer sintetik nilon-6,6 diproduksi melalui polimerisasi kondensasi antara asam heksanadioat (asam adipat) dan 1,6-diaminoheksana (heksametilendiamin). Jika massa molekul relatif satu unit berulang (repeating unit) nilon-6,6 adalah $M_r = 226\\text{ g/mol}$ dan suatu serat nilon-6,6 memiliki massa molar rata-rata $M_n = 22.600\\text{ g/mol}$, derajat polimerisasi rata-rata ($DP$) dari rantai polimer tersebut adalah...",
        "correct": "$DP = 100$, karena derajat polimerisasi menyatakan jumlah unit berulang monomerik yang menyusun satu rantai makromolekul polimer, yang dihitung dari perbandingan massa molar total polimer terhadap massa molar satu unit berulang: $DP = \\frac{M_n}{M_r\\text{ (unit berulang)}} = \\frac{22.600\\text{ g/mol}}{226\\text{ g/mol}} = 100$.",
        "distractors": [
            "$DP = 50$, karena menganggap satu unit berulang berasal dari dua rantai polimer terpisah.",
            "$DP = 200$, dihitung dari penjumlahan jumlah atom karbon dalam kedua monomer pembentuk.",
            "$DP = 66$, karena terpengaruh oleh penomoran nama dagang nilon-6,6.",
            "$DP = 1.000$, dihitung dari pembagian massa polimer dengan massa molar gas hidrogen sampingan."
        ],
        "formula": {
            "title": "DERAJAT POLIMERISASI (DEGREE OF POLYMERIZATION)",
            "latex": "DP = \\frac{M_n}{M_0} = \\frac{22.600\\text{ g/mol}}{226\\text{ g/mol}} = 100",
            "legend": "• Unit berulang nilon-6,6: $[-\\text{NH}-(\\text{CH}_2)_6-\\text{NH}-\\text{CO}-(\\text{CH}_2)_4-\\text{CO}-]$ dengan rumus $(\\text{C}_{12}\\text{H}_{22}\\text{N}_2\\text{O}_2)$ bernilai $M_0 = 226\\text{ g/mol}$<br>• $DP = 100$ unit berulang terhubung ikatan amida"
        },
        "hints": {
            "concept": "Derajat polimerisasi (DP) = Massa molar polimer (Mn) / Massa molar unit berulang (M0).",
            "execution": "DP = 22.600 / 226 = 100."
        }
    }
]
