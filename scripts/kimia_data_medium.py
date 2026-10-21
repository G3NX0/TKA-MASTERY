# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Kimia (SMA/MA Saintek)
Dataset: Medium Practice (25 Authentic Questions, kim-lat-m-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

KIMIA_MEDIUM_ITEMS = [
    {
        "id": "kim-lat-m-01",
        "materi": "STRUKTUR ATOM & ION LOGAM TRANSISI",
        "topic": "Konfigurasi Elektron Ion dan Sifat Kemagnetan",
        "stem": "Unsur kromium memiliki nomor atom $Z = 24$. Konfigurasi elektron kation $\\text{Cr}^{3+}$ pada keadaan dasar dan sifat kemagnetannya berdasarkan jumlah elektron yang tidak berpasangan adalah...",
        "correct": "$[\\text{Ar}]\\,3d^3$ dan bersifat paramagnetik, karena atom netral kromium memiliki konfigurasi stabil setengah penuh $[\\text{Ar}]\\,4s^1\\,3d^5$. Ketika melepaskan 3 elektron untuk membentuk kation $\\text{Cr}^{3+}$, 1 elektron pada subkulit terluar $4s$ dan 2 elektron pada subkulit $3d$ dilepaskan terlebih dahulu, menyisakan 3 elektron tunggal yang tidak berpasangan di subkulit $3d$ ($[\\text{Ar}]\\,3d^3$) sehingga ditarik oleh medan magnet luar (paramagnetik).",
        "distractors": [
            "$[\\text{Ar}]\\,4s^2\\,3d^1$ dan bersifat diamagnetik, karena elektron subkulit 4s keliru dianggap tidak dilepaskan saat pembentukan kation.",
            "$[\\text{Ar}]\\,3d^3$ dan bersifat diamagnetik, karena menganggap seluruh elektron pada orbital subkulit d selalu berpasangan secara simetris.",
            "$[\\text{Ar}]\\,4s^1\\,3d^2$ dan bersifat feromagnetik permanen, karena mengasumsikan pelepasan elektron hanya berasal dari subkulit dalam.",
            "$[\\text{Ar}]\\,3d^5$ dan bersifat paramagnetik kuat, karena menyamakan konfigurasi kation dengan konfigurasi atom netral kromium."
        ],
        "formula": {
            "title": "KONFIGURASI ELEKTRON ION TRANSISI",
            "latex": "{}_{24}\\text{Cr}: [\\text{Ar}]\\,4s^1\\,3d^5 \\xrightarrow{-3e^-} \\text{Cr}^{3+}: [\\text{Ar}]\\,3d^3; \\quad \\text{Elektron tak berpasangan } n = 3 \\implies \\text{Paramagnetik}",
            "legend": "• Elektron kulit terluar ($4s$) selalu dilepaskan lebih dahulu daripada elektron subkulit dalam ($3d$)<br>• Momen magnetik spin: $\\mu_s = \\sqrt{n(n+2)} = \\sqrt{3(5)} = \\sqrt{15} \\approx 3{,}87\\text{ BM}$"
        },
        "hints": {
            "concept": "Cr netral: [Ar] 4s1 3d5. Cr3+ melepas 1 elektron dari 4s dan 2 elektron dari 3d -> [Ar] 3d3. Ada 3 elektron tak berpasangan -> paramagnetik.",
            "execution": "[Ar] 3d3, paramagnetik."
        }
    },
    {
        "id": "kim-lat-m-02",
        "materi": "GEOMETRI MOLEKUL (TEORI VSEPR & HIBRIDISASI)",
        "topic": "Hibridisasi dan Bentuk Molekul SF4",
        "stem": "Belerang tetrafluorida ($\\text{SF}_4$) terbentuk dari atom belerang ($_{16}\\text{S}$) sebagai atom pusat dan empat atom fluorin ($_{9}\\text{F}$). Hibridisasi orbital pada atom pusat, tipe geometri molekul VSEPR, dan bentuk ruang molekul $\\text{SF}_4$ adalah...",
        "correct": "Hibridisasi $sp^3d$, tipe $AX_4E$ (4 PEI dan 1 PEB), dengan bentuk molekul jungkat-jungkit (tetrahedral terdistorsi / see-saw), karena belerang memiliki 6 elektron valensi, 4 elektron digunakan untuk berikatan tunggal dengan F, dan 2 elektron tersisa membentuk 1 pasangan elektron bebas (PEB) yang menempati posisi ekuatorial untuk meminimalkan tolakan.",
        "distractors": [
            "Hibridisasi $sp^3$, tipe $AX_4$ (4 PEI dan 0 PEB), dengan bentuk molekul tetrahedral simetris dan bersifat nonpolar.",
            "Hibridisasi $sp^3d^2$, tipe $AX_4E_2$ (4 PEI dan 2 PEB), dengan bentuk molekul bujur sangkar datar.",
            "Hibridisasi $dsp^2$, tipe $AX_4$, dengan bentuk molekul bujur sangkar planar simetris.",
            "Hibridisasi $sp^3d$, tipe $AX_5$, dengan bentuk molekul bipiramida trigonal sempurna."
        ],
        "formula": {
            "title": "GEOMETRI MOLEKUL BELERANG TETRAFLUORIDA",
            "latex": "\\text{Domain Elektron} = 4\\text{ PEI} + 1\\text{ PEB} = 5 \\implies \\text{Hibridisasi } sp^3d, \\quad \\text{Tipe } AX_4E \\implies \\text{Bentuk Jungkat-Jungkit (See-Saw)}",
            "legend": "• PEB selalu memilih posisi ekuatorial pada geometri dasar bipiramida trigonal karena hanya membentuk 2 tolakan $90^\\circ$ dengan ligan aksial<br>• Menghasilkan molekul bersifat polar ($\\mu > 0$)"
        },
        "hints": {
            "concept": "Elektron valensi S = 6. Digunakan 4 untuk ikatan dengan F -> sisa 2 elektron = 1 PEB. Total domain = 4 PEI + 1 PEB = 5 (hibridisasi sp3d, tipe AX4E). Bentuk = jungkat-jungkit (see-saw).",
            "execution": "sp3d, tipe AX4E, bentuk jungkat-jungkit (see-saw)."
        }
    },
    {
        "id": "kim-lat-m-03",
        "materi": "STOIKIOMETRI (RUMUS EMPIRIS & MOLEKUL)",
        "topic": "Penentuan Rumus Molekul dari Analisis Pembakaran",
        "stem": "Pembakaran sempurna $4{,}4\\text{ gram}$ suatu senyawa hidrokarbon menghasilkan $13{,}2\\text{ gram}$ gas karbon dioksida ($\\text{CO}_2$, $M_r = 44$) dan $7{,}2\\text{ gram}$ uap air ($\\text{H}_2\\text{O}$, $M_r = 18$). Jika massa molekul relatif senyawa tersebut adalah $M_r = 44\\text{ g/mol}$ ($A_r\\,\\text{C} = 12$, $A_r\\,\\text{H} = 1$), rumus empiris dan rumus molekul senyawa hidrokarbon tersebut adalah...",
        "correct": "Rumus empiris $\\text{C}_3\\text{H}_8$ dan rumus molekul $\\text{C}_3\\text{H}_8$ (propana), karena massa karbon adalah $m_C = \\frac{12}{44} \\times 13{,}2\\text{ g} = 3{,}6\\text{ g}$ ($n_C = \\frac{3{,}6}{12} = 0{,}3\\text{ mol}$) dan massa hidrogen adalah $m_H = \\frac{2}{18} \\times 7{,}2\\text{ g} = 0{,}8\\text{ g}$ ($n_H = \\frac{0{,}8}{1} = 0{,}8\\text{ mol}$). Perbandingan mol $\\text{C} : \\text{H} = 0{,}3 : 0{,}8 = 3 : 8$, sehingga rumus empirisnya $(\\text{C}_3\\text{H}_8)_n$. Karena $M_r = (3 \\times 12 + 8 \\times 1)n = 44n = 44 \\implies n = 1$, maka rumus molekulnya adalah $\\text{C}_3\\text{H}_8$.",
        "distractors": [
            "Rumus empiris $\\text{CH}_2$ dan rumus molekul $\\text{C}_3\\text{H}_6$ (propena), karena hidrogen keliru dihitung tanpa mengalikan faktor dua pada molekul air.",
            "Rumus empiris $\\text{C}_2\\text{H}_5$ dan rumus molekul $\\text{C}_4\\text{H}_{10}$ (butana), dihitung dari kesalahan pembagian perbandingan mol atom.",
            "Rumus empiris $\\text{CH}_4$ dan rumus molekul $\\text{CH}_4$ (metana), karena mengabaikan total massa produk pembakaran yang dihasilkan.",
            "Rumus empiris $\\text{C}_3\\text{H}_4$ dan rumus molekul $\\text{C}_3\\text{H}_4$ (propuna), dihitung dari perbandingan stoikiometri gas asetilena."
        ],
        "formula": {
            "title": "ANALISIS ELEMENTER PERSENTASE MASSA",
            "latex": "n_C = \\frac{12}{44} \\times \\frac{13{,}2}{12} = 0{,}3\\text{ mol}; \\quad n_H = \\frac{2}{18} \\times \\frac{7{,}2}{1} = 0{,}8\\text{ mol}; \\quad C : H = 0{,}3 : 0{,}8 = 3 : 8 \\implies (\\text{C}_3\\text{H}_8)_1",
            "legend": "• Massa C $= 3{,}6\\text{ g}$, Massa H $= 0{,}8\\text{ g}$ (Total $= 4{,}4\\text{ g}$, terbukti hanya mengandung C dan H)<br>• $M_r (\\text{C}_3\\text{H}_8) = 3(12) + 8(1) = 44\\text{ g/mol}$"
        },
        "hints": {
            "concept": "Massa C = (12/44) * 13,2 = 3,6 g -> mol C = 0,3 mol. Massa H = (2/18) * 7,2 = 0,8 g -> mol H = 0,8 mol. Rasio C : H = 3 : 8. RE = C3H8. Karena Mr = 44, RM = C3H8.",
            "execution": "Rumus empiris dan molekul: C3H8."
        }
    },
    {
        "id": "kim-lat-m-04",
        "materi": "STOIKIOMETRI (PEREAKSI PEMBATAS & PERSEN HASIL)",
        "topic": "Penentuan Pereaksi Pembatas dan Rendemen Teoritis",
        "stem": "Sebanyak $5{,}4\\text{ gram}$ logam aluminium ($A_r\\,\\text{Al} = 27$) direaksikan dengan $100\\text{ mL}$ larutan asam sulfat $\\text{H}_2\\text{SO}_4\\,1{,}5\\text{ M}$ menurut persamaan reaksi:<br>$$2\\,\\text{Al}(s) + 3\\,\\text{H}_2\\text{SO}_4(aq) \\to \\text{Al}_2(\\text{SO}_4)_3(aq) + 3\\,\\text{H}_2(g)$$<br>Zat yang bertindak sebagai pereaksi pembatas dan volume gas hidrogen yang dihasilkan pada kondisi standar (STP, $0^\\circ\\text{C}$, $1\\text{ atm}$) adalah...",
        "correct": "$\\text{H}_2\\text{SO}_4$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 3{,}36\\text{ liter}$, karena mol $\\text{Al} = \\frac{5{,}4}{27} = 0{,}2\\text{ mol}$ (rasio mol/koefisien = $\\frac{0{,}2}{2} = 0{,}10$) dan mol $\\text{H}_2\\text{SO}_4 = 0{,}1\\text{ L} \\times 1{,}5\\text{ M} = 0{,}15\\text{ mol}$ (rasio mol/koefisien = $\\frac{0{,}15}{3} = 0{,}05$). Karena $0{,}05 < 0{,}10$, maka $\\text{H}_2\\text{SO}_4$ habis bereaksi lebih dulu (pereaksi pembatas). Mol $\\text{H}_2$ yang dihasilkan adalah $\\frac{3}{3} \\times 0{,}15 = 0{,}15\\text{ mol}$. Pada STP, volume gas adalah $V = 0{,}15\\text{ mol} \\times 22{,}4\\text{ L/mol} = 3{,}36\\text{ liter}$.",
        "distractors": [
            "$\\text{Al}$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 6{,}72\\text{ liter}$, karena salah menentukan pereaksi pembatas dan mengasumsikan aluminium habis bereaksi.",
            "$\\text{H}_2\\text{SO}_4$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 2{,}24\\text{ liter}$, dihitung dari rasio satu banding satu terhadap koefisien aluminium.",
            "Kedua pereaksi tepat habis bereaksi dan volume $\\text{H}_2 = 4{,}48\\text{ liter}$, dihitung dari asumsi campuran ekimolar stoikiometri.",
            "$\\text{Al}$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 3{,}36\\text{ liter}$, karena meskipun volume gas benar namun identifikasi pereaksi pembatas keliru."
        ],
        "formula": {
            "title": "PENENTUAN PEREAKSI PEMBATAS (LIMITING REAGENT)",
            "latex": "\\frac{n_{\\text{Al}}}{2} = \\frac{0{,}2}{2} = 0{,}10; \\quad \\frac{n_{\\text{H}_2\\text{SO}_4}}{3} = \\frac{0{,}15}{3} = 0{,}05 \\implies \\text{H}_2\\text{SO}_4 \\text{ Pembatas}; \\quad V_{\\text{H}_2} = 0{,}15 \\times 22{,}4 = 3{,}36\\text{ L}",
            "legend": "• Pereaksi pembatas adalah zat dengan perbandingan (mol / koefisien) terkecil<br>• Gas $\\text{H}_2$ diukur pada STP ($V_m = 22{,}4\\text{ L/mol}$)<br>• $V_{\\text{H}_2} = 3{,}36\\text{ liter}$"
        },
        "hints": {
            "concept": "Hitung mol Al: 5,4/27 = 0,2 mol (mol/koef = 0,1). Mol H2SO4: 0,1 * 1,5 = 0,15 mol (mol/koef = 0,05). H2SO4 pembatas. Mol H2 = 3/3 * 0,15 = 0,15 mol. V_STP = 0,15 * 22,4.",
            "execution": "Pereaksi pembatas = H2SO4, V(H2) = 3,36 liter."
        }
    },
    {
        "id": "kim-lat-m-05",
        "materi": "TITRASI ASAM-BASA & KURVA TITRASI",
        "topic": "Titik Ekuivalen dan Pemilihan Indikator pH",
        "stem": "Sebanyak $25\\text{ mL}$ larutan amonia ($\\text{NH}_4\\text{OH}$, basa lemah) dititrasi dengan larutan standar asam klorida ($\\text{HCl}$, asam kuat) berkonsentrasi $0{,}1\\text{ M}$. Pada titik ekuivalen, perkiraan rentang pH larutan dan indikator asam-basa yang paling tepat digunakan adalah...",
        "correct": "$\\text{pH} < 7$ (sekitar $\\text{pH } 5 - 6$) dan indikator yang tepat adalah metil merah (trayek pH $4{,}4 - 6{,}2$), karena pada titik ekuivalen terbentuk garam amonium klorida ($\\text{NH}_4\\text{Cl}$) yang kationnya mengalami hidrolisis parsial menghasilkan ion $\\text{H}^+$ sehingga larutan bersifat asam.",
        "distractors": [
            "$\\text{pH} = 7$ (netral) dan indikator yang tepat adalah bromtimol biru (trayek pH $6{,}0 - 7{,}6$), karena titik ekuivalen dianggap selalu menghasilkan larutan netral.",
            "$\\text{pH} > 7$ (sekitar $\\text{pH } 8 - 9$) dan indikator yang tepat adalah fenolftalein (trayek pH $8{,}3 - 10{,}0$), karena titrasi melibatkan basa amonia.",
            "$\\text{pH} = 1$ dan indikator yang tepat adalah metil jingga (trayek pH $3{,}1 - 4{,}4$), karena asam klorida adalah asam kuat yang mendominasi campuran.",
            "$\\text{pH} = 7$ dan indikator yang tepat adalah fenolftalein karena menghasilkan perubahan warna dari merah muda menjadi tidak berwarna."
        ],
        "formula": {
            "title": "TITRASI ASAM KUAT DENGAN BASA LEMAH",
            "latex": "\\text{HCl} + \\text{NH}_4\\text{OH} \\to \\text{NH}_4\\text{Cl} + \\text{H}_2\\text{O}; \\quad \\text{NH}_4^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4\\text{OH} + \\text{H}^+ \\implies \\text{pH}_{\\text{ekuivalen}} < 7",
            "legend": "• Titik ekuivalen berada di daerah asam ($\\text{pH } \\approx 5{,}3$)<br>• Indikator harus memiliki trayek perubahan warna yang memotong kurva lonjakan pH di titik ekuivalen (Metil Merah: $4{,}4 - 6{,}2$)<br>• Fenolftalein TIDAK cocok karena berubah warna jauh sebelum titik ekuivalen tercapai"
        },
        "hints": {
            "concept": "Titrasi basa lemah dengan asam kuat menghasilkan titik ekuivalen di daerah asam (pH < 7) akibat hidrolisis kation NH4+. Gunakan indikator metil merah (trayek 4,4 - 6,2).",
            "execution": "pH < 7, indikator metil merah."
        }
    },
    {
        "id": "kim-lat-m-06",
        "materi": "LARUTAN PENYANGGA (MEKANISME KERJA BUFFER)",
        "topic": "Perubahan pH Larutan Buffer saat Ditambah Sedikit Asam Kuat",
        "stem": "Satu liter larutan penyangga mengandung $0{,}1\\text{ mol } \\text{CH}_3\\text{COOH}$ dan $0{,}1\\text{ mol } \\text{CH}_3\\text{COONa}$ ($K_a = 1 \\times 10^{-5}$, $\\text{pH awal} = 5$). Jika ke dalam larutan tersebut ditambahkan $0{,}01\\text{ mol}$ gas $\\text{HCl}$ tanpa perubahan volume larutan yang berarti, nilai pH larutan penyangga setelah penambahan asam tersebut adalah... (Diketahui $\\log 1{,}22 \\approx 0{,}09$)",
        "correct": "$\\text{pH} = 5 - \\log\\left(\\frac{11}{9}\\right) \\approx 4{,}91$, karena penambahan ion $\\text{H}^+$ dari $\\text{HCl}$ dinetralisasi oleh ion basa konjugasi asetat: $\\text{CH}_3\\text{COO}^- + \\text{H}^+ \\to \\text{CH}_3\\text{COOH}$. Jumlah mol garam asetat berkurang menjadi $0{,}10 - 0{,}01 = 0{,}09\\text{ mol}$ dan mol asam asetat bertambah menjadi $0{,}10 + 0{,}01 = 0{,}11\\text{ mol}$. Maka $[\\text{H}^+] = K_a \\times \\frac{0{,}11}{0{,}09} = 10^{-5} \\times 1{,}222 = 1{,}222 \\times 10^{-5}\\text{ M} \\implies \\text{pH} = 5 - \\log(1{,}22) \\approx 4{,}91$ (terbukti pH larutan relatif konstan hanya turun $0{,}09$ satuan).",
        "distractors": [
            "$\\text{pH} = 2{,}00$, karena larutan dianggap kehilangan daya penyangga dan langsung mengikuti konsentrasi asam kuat HCl.",
            "$\\text{pH} = 5{,}09$, karena ion asam asetat keliru dihitung bertambah pada komponen garam basa konjugasi.",
            "$\\text{pH} = 4{,}00$, dihitung dari pengurangan satu satuan skala pH penuh.",
            "$\\text{pH} = 7{,}00$, karena penambahan asam dianggap menetralkan seluruh sifat keasaman larutan penyangga."
        ],
        "formula": {
            "title": "MEKANISME KERJA BUFFER TERHADAP ASAM KUAT",
            "latex": "[\\text{H}^+] = K_a \\cdot \\frac{n_{\\text{asam}} + n_{\\text{HCl}}}{n_{\\text{garam}} - n_{\\text{HCl}}} = 10^{-5} \\times \\frac{0{,}10 + 0{,}01}{0{,}10 - 0{,}01} = 10^{-5} \\times \\frac{0{,}11}{0{,}09} = 1{,}222 \\times 10^{-5}\\text{ M} \\implies \\text{pH} \\approx 4{,}91",
            "legend": "• Penambahan asam kuat menggeser komposisi: asam bertambah ($+0{,}01$), basa konjugasi berkurang ($-0{,}01$)<br>• Kapasitas buffer menjaga pH tetap stabil di sekitar $4{,}91$"
        },
        "hints": {
            "concept": "Saat ditambah asam kuat, ion H+ bereaksi dengan basa konjugasi CH3COO-. Asam bertambah: 0,1 + 0,01 = 0,11 mol. Garam berkurang: 0,1 - 0,01 = 0,09 mol. [H+] = Ka * (0,11 / 0,09).",
            "execution": "[H+] = 1e-5 * (11/9) -> pH = 5 - log(11/9) = 5 - 0,09 = 4,91."
        }
    },
    {
        "id": "kim-lat-m-07",
        "materi": "HIDROLISIS GARAM DARI ASAM LEMAH & BASA LEMAH",
        "topic": "Penentuan pH Garam Terhidrolisis Total",
        "stem": "Garam amonium format ($\\text{HCOONH}_4$) dilarutkan ke dalam air. Diketahui tetapan ionisasi asam format $K_a = 2 \\times 10^{-4}$, tetapan ionisasi basa amonia $K_b = 1 \\times 10^{-5}$, dan tetapan ionisasi air $K_w = 1 \\times 10^{-14}$. Sifat larutan garam tersebut dan nilai pH-nya adalah... (Gunakan $\\log 2{,}24 \\approx 0{,}35$)",
        "correct": "Bersifat asam dengan $\\text{pH} = 7 - \\frac{1}{2}(\\text{p}K_a - \\text{p}K_b) = 6{,}35$, karena nilai $K_a > K_b$ ($2 \\times 10^{-4} > 1 \\times 10^{-5}$), sehingga ionisasi kation $\\text{NH}_4^+$ menghasilkan ion $\\text{H}^+$ yang lebih dominan daripada ion $\\text{OH}^-$ dari anion format. Konsentrasi $[\\text{H}^+] = \\sqrt{\\frac{K_w \\cdot K_a}{K_b}} = \\sqrt{\\frac{10^{-14} \\times (2 \\times 10^{-4})}{10^{-5}}} = \\sqrt{2 \\times 10^{-13}} = \\sqrt{20 \\times 10^{-14}} \\approx 4{,}47 \\times 10^{-7}\\text{ M} \\implies \\text{pH} = 7 - \\log(4{,}47) \\approx 6{,}35$.",
        "distractors": [
            "Bersifat basa dengan $\\text{pH} = 7{,}65$, karena nilai tetapan basa amonia keliru dianggap lebih mendominasi.",
            "Bersifat netral dengan $\\text{pH} = 7{,}00$, karena kedua komponen penyusunnya sama-sama lemah sehingga dianggap saling meniadakan sempurna.",
            "Bersifat asam dengan $\\text{pH} = 4{,}50$, dihitung tanpa menyertakan faktor pembagian setengah pada logaritma tetapan kesetimbangan.",
            "Bersifat basa dengan $\\text{pH} = 9{,}50$, dihitung dari rumus hidrolisis kation asam kuat basa lemah."
        ],
        "formula": {
            "title": "HIDROLISIS TOTAL (ASAM LEMAH + BASA LEMAH)",
            "latex": "[\\text{H}^+] = \\sqrt{\\frac{K_w \\cdot K_a}{K_b}} = \\sqrt{\\frac{10^{-14} \\times 2 \\times 10^{-4}}{10^{-5}}} = \\sqrt{4 \\times 10^{-13}}... \\implies \\text{pH} = \\frac{1}{2}(\\text{p}K_w + \\text{p}K_a - \\text{p}K_b) = \\frac{1}{2}(14 + 3{,}70 - 5{,}0) = 6{,}35",
            "legend": "• $K_a > K_b \\implies$ Larutan bersifat asam ($\\text{pH} < 7$)<br>• $K_a < K_b \\implies$ Larutan bersifat basa ($\\text{pH} > 7$)<br>• $K_a = K_b \\implies$ Larutan bersifat netral ($\\text{pH} = 7$)<br>• pH garam ini tidak bergantung pada konsentrasi molaritas garam"
        },
        "hints": {
            "concept": "Garam dari asam lemah dan basa lemah: [H+] = sqrt(Kw * Ka / Kb). Karena Ka > Kb, larutan bersifat asam (pH < 7). pH = 0,5 * (pKw + pKa - pKb).",
            "execution": "pKa = 4 - log 2 = 3,70. pKb = 5. pH = 0,5 * (14 + 3,70 - 5) = 0,5 * 12,70 = 6,35 (asam)."
        }
    },
    {
        "id": "kim-lat-m-08",
        "materi": "KELARUTAN & HASIL KALI KELARUTAN (Ksp)",
        "topic": "Prediksi Terjadinya Endapan dengan Membandingkan Qsp dan Ksp",
        "stem": "Sebanyak $50\\text{ mL}$ larutan $\\text{AgNO}_3\\,2 \\times 10^{-4}\\text{ M}$ dicampurkan dengan $50\\text{ mL}$ larutan $\\text{K}_2\\text{CrO}_4\\,2 \\times 10^{-4}\\text{ M}$. Diketahui nilai $K_{sp}\\,\\text{Ag}_2\\text{CrO}_4 = 2{,}4 \\times 10^{-12}$. Pernyataan yang benar mengenai kondisi larutan setelah pencampuran adalah...",
        "correct": "Terbentuk endapan $\\text{Ag}_2\\text{CrO}_4$, karena nilai hasil kali kuosien reaksi $Q_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (10^{-4})^2 \\times (10^{-4}) = 1 \\times 10^{-12} < K_{sp}$... mari cek konsentrasi campuran dengan cermat: Volume total = $100\\text{ mL}$. $[\\text{Ag}^+] = \\frac{50 \\times 2 \\times 10^{-4}}{100} = 1 \\times 10^{-4}\\text{ M}$. $[\\text{CrO}_4^{2-}] = \\frac{50 \\times 2 \\times 10^{-4}}{100} = 1 \\times 10^{-4}\\text{ M}$. Maka $Q_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (10^{-4})^2 \\times (10^{-4}) = 10^{-8} \\times 10^{-4} = 10^{-12} = 1{,}0 \\times 10^{-12}$. Karena $Q_{sp} = 1{,}0 \\times 10^{-12} < K_{sp} = 2{,}4 \\times 10^{-12}$, maka larutan belum jenuh dan TIDAK terbentuk endapan.",
        "distractors": [
            "Terbentuk endapan $\\text{Ag}_2\\text{CrO}_4$ berwarna merah bata karena nilai kuosien reaksi $Q_{sp} > K_{sp}$.",
            "Larutan tepat jenuh dan mulai terbentuk kristal mikro karena nilai $Q_{sp} = K_{sp}$.",
            "Terjadi reaksi redoks pembentukan logam perak bebas dan gas oksigen di dalam wadah bejana.",
            "Terbentuk endapan kalium nitrat $\\text{KNO}_3$ karena memiliki kelarutan yang sangat rendah di air."
        ],
        "formula": {
            "title": "PREDIKSI PENGENDAPAN (Qsp VS Ksp)",
            "latex": "[\\text{Ag}^+] = 10^{-4}\\text{ M}; \\quad [\\text{CrO}_4^{2-}] = 10^{-4}\\text{ M}; \\quad Q_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (10^{-4})^2 (10^{-4}) = 10^{-12}; \\quad Q_{sp} < K_{sp} \\implies \\text{Belum Mengendap}",
            "legend": "• $Q_{sp} = 1{,}0 \\times 10^{-12}$<br>• $K_{sp} = 2{,}4 \\times 10^{-12}$<br>• $Q_{sp} < K_{sp} \\implies$ Larutan belum jenuh, tidak ada endapan terbentuk"
        },
        "hints": {
            "concept": "Hitung konsentrasi ion setelah pengenceran: [Ag+] = 1e-4 M, [CrO4 2-] = 1e-4 M. Hitung Qsp = [Ag+]^2 * [CrO4 2-] = (1e-4)^2 * 1e-4 = 1e-12. Bandingkan dengan Ksp = 2,4e-12.",
            "execution": "Karena Qsp (1e-12) < Ksp (2,4e-12), larutan belum jenuh sehingga tidak terbentuk endapan."
        }
    },
    {
        "id": "kim-lat-m-09",
        "materi": "SIFAT KOLIGATIF (LARUTAN ELEKTROLIT)",
        "topic": "Kenaikan Titik Didih Elektrolit Biner dan Faktor Van 't Hoff",
        "stem": "Sebanyak $11{,}7\\text{ gram}$ garam dapur ($\\text{NaCl}$, $M_r = 58{,}5$) dilarutkan ke dalam $500\\text{ gram}$ air murni ($K_b\\,\\text{air} = 0{,}52^\\circ\\text{C/m}$). Jika garam $\\text{NaCl}$ terionisasi sempurna di dalam air (derajat ionisasi $\\alpha = 1$), kenaikan titik didih ($\\Delta T_b$) dan titik didih larutan ($T_b$) pada tekanan 1 atm berturut-turut adalah...",
        "correct": "$\\Delta T_b = 0{,}416^\\circ\\text{C}$ dan $T_b = 100{,}416^\\circ\\text{C}$, karena $\\text{NaCl}$ adalah elektrolit kuat biner ($n = 2$ ion: $\\text{Na}^+$ dan $\\text{Cl}^-$) dengan faktor Van 't Hoff $i = 1 + (2 - 1)(1) = 2$. Jumlah mol $\\text{NaCl}$ adalah $n = \\frac{11{,}7}{58{,}5} = 0{,}2\\text{ mol}$. Molalitasnya adalah $m = \\frac{0{,}2\\text{ mol}}{0{,}5\\text{ kg}} = 0{,}4\\text{ m}$. Kenaikan titik didih dihitung dari $\\Delta T_b = m \\times K_b \\times i = 0{,}4 \\times 0{,}52 \\times 2 = 0{,}416^\\circ\\text{C}$. Maka titik didih larutan adalah $T_b = 100 + 0{,}416 = 100{,}416^\\circ\\text{C}$.",
        "distractors": [
            "$\\Delta T_b = 0{,}208^\\circ\\text{C}$ dan $T_b = 100{,}208^\\circ\\text{C}$, karena mengabaikan faktor Van 't Hoff larutan elektrolit ($i = 1$).",
            "$\\Delta T_b = 0{,}832^\\circ\\text{C}$ dan $T_b = 100{,}832^\\circ\\text{C}$, dihitung dengan mengalikan faktor Van 't Hoff empat ion poliatomik.",
            "$\\Delta T_b = 0{,}416^\\circ\\text{C}$ dan $T_b = 99{,}584^\\circ\\text{C}$, karena titik didih larutan keliru dikurangkan dari titik didih pelarut air.",
            "$\\Delta T_b = 1{,}040^\\circ\\text{C}$ dan $T_b = 101{,}040^\\circ\\text{C}$, dihitung dari asumsi konsentrasi satu molal elektrolit kuat."
        ],
        "formula": {
            "title": "KENAIKAN TITIK DIDIH LARUTAN ELEKTROLIT",
            "latex": "i = 1 + (n - 1)\\alpha = 1 + (2 - 1)(1) = 2; \\quad m = \\frac{11{,}7}{58{,}5} \\times \\frac{1.000}{500} = 0{,}4\\text{ m}; \\quad \\Delta T_b = m \\cdot K_b \\cdot i = 0{,}4 \\times 0{,}52 \\times 2 = 0{,}416^\\circ\\text{C}",
            "legend": "• Titik didih air murni $T_b^0 = 100^\\circ\\text{C}$<br>• $T_b = 100 + 0{,}416 = 100{,}416^\\circ\\text{C}$"
        },
        "hints": {
            "concept": "NaCl terurai jadi 2 ion (i = 2). Mol = 11,7 / 58,5 = 0,2 mol. Molalitas m = 0,2 / 0,5 = 0,4 m. Delta_Tb = m * Kb * i = 0,4 * 0,52 * 2 = 0,416 C. Tb = 100 + 0,416 C.",
            "execution": "Delta_Tb = 0,416 C, Tb = 100,416 C."
        }
    },
    {
        "id": "kim-lat-m-10",
        "materi": "SIFAT KOLIGATIF (TEKANAN OSMOTIK)",
        "topic": "Penentuan Massa Molar Makromolekul dari Tekanan Osmotik",
        "stem": "Sebanyak $3\\text{ gram}$ suatu senyawa makromolekul nonelektrolit dilarutkan dalam air hingga volume larutan mencapai $250\\text{ mL}$ pada suhu $27^\\circ\\text{C}$ ($T = 300\\text{ K}$). Larutan tersebut memiliki tekanan osmotik sebesar $\\pi = 2{,}46\\text{ atmosfer}$. Jika tetapan gas ideal $R = 0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)}$, massa molekul relatif ($M_r$) senyawa tersebut adalah...",
        "correct": "$M_r = 120\\text{ g/mol}$, karena menurut persamaan tekanan osmotik Van 't Hoff $\\pi = M R T = \\frac{g}{M_r} \\times \\frac{1.000}{V\\text{ (mL)}} \\times R T$, sehingga massa molekul relatif adalah $M_r = \\frac{g \\times 1.000 \\times R T}{\\pi \\times V} = \\frac{3 \\times 1.000 \\times 0{,}082 \\times 300}{2{,}46 \\times 250} = \\frac{73.800}{615} = 120\\text{ g/mol}$.",
        "distractors": [
            "$M_r = 60\\text{ g/mol}$, karena volume larutan keliru dihitung sebesar 500 mL.",
            "$M_r = 240\\text{ g/mol}$, karena tekanan osmotik keliru dikalikan dengan faktor dua elektrolit biner.",
            "$M_r = 180\\text{ g/mol}$, dihitung dari pendekatan massa molar glukosa standar tanpa analisis persamaan Van 't Hoff.",
            "$M_r = 300\\text{ g/mol}$, dihitung dari perkalian suhu mutlak dengan massa zat terlarut."
        ],
        "formula": {
            "title": "TEKANAN OSMOTIK VAN 'T HOFF",
            "latex": "\\pi = \\frac{n}{V} R T = \\frac{g}{M_r \\cdot V} R T \\implies M_r = \\frac{g R T}{\\pi V} = \\frac{3 \\times 0{,}082 \\times 300}{2{,}46 \\times 0{,}25} = \\frac{73{,}8}{0{,}615} = 120\\text{ g/mol}",
            "legend": "• $V = 250\\text{ mL} = 0{,}25\\text{ L}$<br>• $T = 27 + 273 = 300\\text{ K}$<br>• $M_r = 120\\text{ g/mol}$"
        },
        "hints": {
            "concept": "Gunakan pi = (g / Mr) * (R * T / V). Mr = (g * R * T) / (pi * V). V = 0,25 L, T = 300 K.",
            "execution": "Mr = (3 * 0,082 * 300) / (2,46 * 0,25) = 73,8 / 0,615 = 120 g/mol."
        }
    },
    {
        "id": "kim-lat-m-11",
        "materi": "TERMOKIMIA (HUKUM HESS & SIKLUS ENERGI)",
        "topic": "Perhitungan Entalpi Reaksi dari Diagram Tingkat Energi",
        "stem": "Diketahui entalpi pembentukan standar ($\\Delta H_f^\\circ$) dari senyawa-senyawa berikut:<br>• $\\Delta H_f^\\circ\\,\\text{C}_3\\text{H}_8(g) = -104\\text{ kJ/mol}$<br>• $\\Delta H_f^\\circ\\,\\text{CO}_2(g) = -394\\text{ kJ/mol}$<br>• $\\Delta H_f^\\circ\\,\\text{H}_2\\text{O}(l) = -286\\text{ kJ/mol}$<br>Besar kalor pembakaran standar ($\\Delta H_c^\\circ$) untuk satu mol gas propana menurut reaksi:<br>$$\\text{C}_3\\text{H}_8(g) + 5\\,\\text{O}_2(g) \\to 3\\,\\text{CO}_2(g) + 4\\,\\text{H}_2\\text{O}(l)$$<br>adalah...",
        "correct": "$\\Delta H_c^\\circ = -2.222\\text{ kJ/mol}$, karena entalpi reaksi dihitung dari selisih entalpi produk dikurangi entalpi reaktan: $\\Delta H = \\sum \\Delta H_f^\\circ(\\text{produk}) - \\sum \\Delta H_f^\\circ(\\text{reaktan}) = [3(-394) + 4(-286)] - [-104 + 5(0)] = [-1.182 - 1.144] - [-104] = -2.326 + 104 = -2.222\\text{ kJ/mol}$.",
        "distractors": [
            "$\\Delta H_c^\\circ = +2.222\\text{ kJ/mol}$, karena salah memberikan tanda positif pada reaksi pembakaran yang terbukti eksotermik membebaskan kalor.",
            "$\\Delta H_c^\\circ = -2.430\\text{ kJ/mol}$, karena entalpi pembentukan propana keliru dijumlahkan dengan produk bukan dikurangkan.",
            "$\\Delta H_c^\\circ = -1.182\\text{ kJ/mol}$, karena hanya memperhitungkan entalpi pembentukan gas karbon dioksida tanpa uap air.",
            "$\\Delta H_c^\\circ = -576\\text{ kJ/mol}$, dihitung dari selisih aljabar langsung tanpa mengalikan koefisien reaksi pembakaran."
        ],
        "formula": {
            "title": "HUKUM HESS DARI ENTALPI PEMBENTUKAN STANDAR",
            "latex": "\\Delta H_c^\\circ = [3\\Delta H_f^\\circ(\\text{CO}_2) + 4\\Delta H_f^\\circ(\\text{H}_2\\text{O})] - \\Delta H_f^\\circ(\\text{C}_3\\text{H}_8) = [3(-394) + 4(-286)] - (-104) = -2.326 + 104 = -2.222\\text{ kJ/mol}",
            "legend": "• $\\Delta H_f^\\circ$ unsur bebas ($\\text{O}_2$) dalam keadaan standar adalah nol<br>• Reaksi pembakaran propana melepaskan kalor sebesar $2.222\\text{ kJ/mol}$"
        },
        "hints": {
            "concept": "Delta H = Sigma Delta Hf (produk / kanan) - Sigma Delta Hf (reaktan / kiri). Produk = 3 * (-394) + 4 * (-286) = -2.326 kJ. Reaktan = -104 kJ.",
            "execution": "Delta H = -2.326 - (-104) = -2.222 kJ/mol."
        }
    },
    {
        "id": "kim-lat-m-12",
        "materi": "KINETIKA KIMIA & PENGARUH SUHU",
        "topic": "Pengaruh Kenaikan Suhu terhadap Laju Reaksi",
        "stem": "Suatu reaksi kimia berlangsung 3 kali lebih cepat setiap kenaikan suhu sebesar $10^\\circ\\text{C}$. Jika pada suhu $25^\\circ\\text{C}$ reaksi tersebut membutuhkan waktu $54\\text{ menit}$ untuk selesai sempurna, waktu yang dibutuhkan agar reaksi tersebut selesai pada suhu $55^\\circ\\text{C}$ adalah...",
        "correct": "$2\\text{ menit}$, karena kenaikan suhu adalah $\\Delta T = 55^\\circ\\text{C} - 25^\\circ\\text{C} = 30^\\circ\\text{C}$. Jumlah kenaikan kelipatan sepuluh derajat adalah $n = \\frac{\\Delta T}{10} = \\frac{30}{10} = 3$. Laju reaksi meningkat sebesar $3^n = 3^3 = 27$ kali lebih cepat. Karena waktu reaksi berbanding terbalik dengan laju reaksi ($t \\propto 1/v$), maka waktu yang dibutuhkan pada suhu $55^\\circ\\text{C}$ adalah $t_2 = \\frac{t_1}{3^n} = \\frac{54\\text{ menit}}{27} = 2\\text{ menit}$.",
        "distractors": [
            "$6\\text{ menit}$, karena laju reaksi keliru dianggap hanya meningkat sembilan kali lipat.",
            "$18\\text{ menit}$, karena laju reaksi hanya dikalikan tiga satu kali tanpa pemangkatan jumlah kenaikan suhu.",
            "$1\\text{ menit}$, dihitung dari asumsi laju reaksi meningkat secara kuadratik eksponensial.",
            "$27\\text{ menit}$, dihitung dari pengurangan separuh waktu reaksi awal."
        ],
        "formula": {
            "title": "PENGARUH SUHU TERHADAP WAKTU REAKSI",
            "latex": "v_2 = v_1 \\times (\\Delta v)^{\\frac{\\Delta T}{T_0}} \\implies t_2 = t_1 \\times \\left(\\frac{1}{\\Delta v}\\right)^{\\frac{\\Delta T}{T_0}} = 54 \\times \\left(\\frac{1}{3}\\right)^{\\frac{55-25}{10}} = \\frac{54}{3^3} = \\frac{54}{27} = 2\\text{ menit}",
            "legend": "• Kenaikan suhu meningkatkan energi kinetik molekul dan frekuensi tumbukan efektif partikel yang melampaui energi aktivasi ($E_a$)<br>• Waktu reaksi berkurang drastis dari 54 menit menjadi 2 menit"
        },
        "hints": {
            "concept": "Laju naik 3 kali lipat tiap 10 C. Delta T = 55 - 25 = 30 C -> n = 30/10 = 3 periode. Laju naik 3^3 = 27 kali. Waktu t2 = t1 / 27.",
            "execution": "t2 = 54 / 27 = 2 menit."
        }
    },
    {
        "id": "kim-lat-m-13",
        "materi": "KESETIMBANGAN KIMIA (DERAJAT DISOSIASI & Kp)",
        "topic": "Perhitungan Kp dari Derajat Disosiasi dan Tekanan Total",
        "stem": "Gas fosforus pentaklorida ($\\text{PCl}_5$) mengalami disosiasi dalam wadah tertutup pada suhu tertentu menurut reaksi:<br>$$\\text{PCl}_5(g) \\rightleftharpoons \\text{PCl}_3(g) + \\text{Cl}_2(g)$$<br>Mula-mula dimasukkan $1\\text{ mol } \\text{PCl}_5$. Pada keadaan setimbang, sepertiga bagian dari $\\text{PCl}_5$ telah terurai (derajat disosiasi $\\alpha = \\frac{1}{3}$) dan tekanan total gas di dalam bejana adalah $P_{\\text{total}} = 4\\text{ atmosfer}$. Nilai tetapan kesetimbangan tekanan ($K_p$) reaksi tersebut adalah...",
        "correct": "$K_p = 0{,}5\\text{ atm}$, karena mol $\\text{PCl}_5$ yang terurai adalah $\\frac{1}{3}\\text{ mol}$, menyisakan $\\text{PCl}_5 = 1 - \\frac{1}{3} = \\frac{2}{3}\\text{ mol}$, terbentuk $\\text{PCl}_3 = \\frac{1}{3}\\text{ mol}$, dan $\\text{Cl}_2 = \\frac{1}{3}\\text{ mol}$. Total mol gas pada kesetimbangan adalah $n_{\\text{total}} = \\frac{2}{3} + \\frac{1}{3} + \\frac{1}{3} = \\frac{4}{3}\\text{ mol}$. Tekanan parsial masing-masing gas: $P_{\\text{PCl}_5} = \\frac{2/3}{4/3} \\times 4 = 2\\text{ atm}$, $P_{\\text{PCl}_3} = \\frac{1/3}{4/3} \\times 4 = 1\\text{ atm}$, dan $P_{\\text{Cl}_2} = 1\\text{ atm}$. Maka $K_p = \\frac{P_{\\text{PCl}_3} \\cdot P_{\\text{Cl}_2}}{P_{\\text{PCl}_5}} = \\frac{1 \\times 1}{2} = 0{,}5\\text{ atm}$.",
        "distractors": [
            "$K_p = 1{,}0\\text{ atm}$, karena tekanan parsial reaktan keliru dihitung sama dengan tekanan produk.",
            "$K_p = 0{,}25\\text{ atm}$, dihitung dari pengkuadratan rasio mol tanpa mengalikan dengan tekanan total gas.",
            "$K_p = 2{,}0\\text{ atm}$, karena rumus Kp keliru dibalik menjadi tekanan reaktan dibagi tekanan produk.",
            "$K_p = 0{,}75\\text{ atm}$, dihitung dari pendekatan pembulatan fraksi mol kesetimbangan kimia."
        ],
        "formula": {
            "title": "PERHITUNGAN Kp DARI TEKANAN PARSIAL GAS",
            "latex": "n_{\\text{total}} = \\frac{4}{3}\\text{ mol}; \\quad P_{\\text{PCl}_5} = 2\\text{ atm}; \\quad P_{\\text{PCl}_3} = 1\\text{ atm}; \\quad P_{\\text{Cl}_2} = 1\\text{ atm}; \\quad K_p = \\frac{1 \\times 1}{2} = 0{,}5\\text{ atm}",
            "legend": "• Fraksi mol $\\text{PCl}_5 = 2/4 = 0{,}5$, $\\text{PCl}_3 = 1/4 = 0{,}25$, $\\text{Cl}_2 = 1/4 = 0{,}25$<br>• $P_i = X_i \\times P_{\\text{total}}$<br>• $K_p = 0{,}5\\text{ atm}$"
        },
        "hints": {
            "concept": "Mol setimbang: PCl5 = 2/3, PCl3 = 1/3, Cl2 = 1/3. Total mol = 4/3. Tekanan parsial: P(PCl5) = (2/4)*4 = 2 atm, P(PCl3) = (1/4)*4 = 1 atm, P(Cl2) = 1 atm. Kp = 1*1 / 2.",
            "execution": "Kp = 1 / 2 = 0,5 atm."
        }
    },
    {
        "id": "kim-lat-m-14",
        "materi": "REAKSI REDOKS (PENYETARAAN ION-ELEKTRON)",
        "topic": "Penyetaraan Reaksi Redoks dalam Suasana Asam",
        "stem": "Diberikan persamaan reaksi redoks dalam suasana asam (belum setara):<br>$$a\\,\\text{MnO}_4^-(aq) + b\\,\\text{Fe}^{2+}(aq) + c\\,\\text{H}^+(aq) \\to d\\,\\text{Mn}^{2+}(aq) + e\\,\\text{Fe}^{3+}(aq) + f\\,\\text{H}_2\\text{O}(l)$$<br>Nilai koefisien reaksi $a$, $b$, $c$, $d$, $e$, dan $f$ yang benar setelah disetarakan berturut-turut adalah...",
        "correct": "$a = 1$, $b = 5$, $c = 8$, $d = 1$, $e = 5$, dan $f = 4$, karena setengah reaksi reduksi permanganat adalah $\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$ (melibatkan 5 elektron), dan setengah reaksi oksidasi besi adalah $\\text{Fe}^{2+} \\to \\text{Fe}^{3+} + e^-$. Menyamakan jumlah transfer elektron menuntut pengalian 5 pada setengah reaksi oksidasi sehingga diperoleh perbandingan koefisien $1 : 5 : 8 \\to 1 : 5 : 4$.",
        "distractors": [
            "$a = 2$, $b = 5$, $c = 16$, $d = 2$, $e = 5$, dan $f = 8$, karena jumlah koefisien ion besi tidak dikalikan dua mengikuti permanganat.",
            "$a = 1$, $b = 3$, $c = 4$, $d = 1$, $e = 3$, dan $f = 2$, karena jumlah ion hidrogen tidak menyetarakan muatan listrik di kedua ruas.",
            "$a = 1$, $b = 1$, $c = 8$, $d = 1$, $e = 1$, dan $f = 4$, karena mengabaikan kesetaraan transfer jumlah elektron redoks.",
            "$a = 2$, $b = 10$, $c = 8$, $d = 2$, $e = 10$, dan $f = 4$, karena koefisien asam hidrogen tidak digandakan saat pengalian koefisien dua."
        ],
        "formula": {
            "title": "METODE SETENGAH REAKSI (ION ELEKTRON) SUASANA ASAM",
            "latex": "\\begin{aligned} \\text{Reduksi: } & \\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O} \\quad (\\times 1) \\\\ \\text{Oksidasi: } & \\text{Fe}^{2+} \\to \\text{Fe}^{3+} + e^- \\quad (\\times 5) \\\\ \\hline \\text{Net: } & \\text{MnO}_4^- + 5\\text{Fe}^{2+} + 8\\text{H}^+ \\to \\text{Mn}^{2+} + 5\\text{Fe}^{3+} + 4\\text{H}_2\\text{O} \\end{aligned}",
            "legend": "• Muatan ruas kiri $= (-1) + 5(+2) + 8(+1) = +17$<br>• Muatan ruas kanan $= (+2) + 5(+3) = +17$ (Setara muatan dan atom)"
        },
        "hints": {
            "concept": "MnO4- -> Mn2+ butuh 5 elektron dan 8 H+ untuk menghasilkan 4 H2O. Fe2+ -> Fe3+ melepas 1 elektron (kalikan 5 agar elektron sama).",
            "execution": "Koefisien: 1, 5, 8 -> 1, 5, 4."
        }
    },
    {
        "id": "kim-lat-m-15",
        "materi": "ELEKTROKIMIA (KOROSI & PROTEKSI KATODIK)",
        "topic": "Pemilihan Logam Tumbal Pencegah Karat Besi",
        "stem": "Pipa besi bawah tanah ($E^\\circ\\,\\text{Fe}^{2+}/\\text{Fe} = -0{,}44\\text{ V}$) dapat dilindungi dari bahaya perkaratan dengan metode proteksi katodik (anoda korban). Diberikan data potensial reduksi standar beberapa logam:<br>• $\\text{Mg}^{2+}/\\text{Mg} \\quad E^\\circ = -2{,}37\\text{ V}$<br>• $\\text{Zn}^{2+}/\\text{Zn} \\quad E^\\circ = -0{,}76\\text{ V}$<br>• $\\text{Sn}^{2+}/\\text{Sn} \\quad E^\\circ = -0{,}14\\text{ V}$<br>• $\\text{Cu}^{2+}/\\text{Cu} \\quad E^\\circ = +0{,}34\\text{ V}$<br>• $\\text{Ag}^{+}/\\text{Ag} \\quad E^\\circ = +0{,}80\\text{ V}$<br>Pasangan logam yang paling efektif digunakan sebagai anoda korban untuk melindungi pipa besi tersebut adalah...",
        "correct": "Magnesium ($\\text{Mg}$) dan seng ($\\text{Zn}$), karena keduanya memiliki potensial reduksi standar yang jauh lebih negatif daripada besi ($E^\\circ_{\\text{Mg}} = -2{,}37\\text{ V}$ dan $E^\\circ_{\\text{Zn}} = -0{,}76\\text{ V} < E^\\circ_{\\text{Fe}} = -0{,}44\\text{ V}$), sehingga logam $\\text{Mg}$ dan $\\text{Zn}$ lebih mudah teroksidasi dan bertindak sebagai anoda korban yang mengorbankan dirinya terkorosi demi melindungi besi.",
        "distractors": [
            "Tembaga ($\\text{Cu}$) dan perak ($\\text{Ag}$), karena keduanya merupakan logam mulia yang tahan karat sehingga dianggap mampu melindungi besi.",
            "Timah ($\\text{Sn}$) dan tembaga ($\\text{Cu}$), karena timah umum digunakan pada kaleng makanan kemasan baja.",
            "Hanya perak ($\\text{Ag}$), karena perak memiliki potensial reduksi tertinggi sehingga mendominasi seluruh reaksi elektrokimia.",
            "Semua logam di atas (Mg, Zn, Sn, Cu, dan Ag) dapat melindungi besi dengan efektivitas yang persis sama."
        ],
        "formula": {
            "title": "PRINSIP PROTEKSI KATODIK (ANODA KORBAN)",
            "latex": "E^\\circ_{\\text{anoda korban}} < E^\\circ_{\\text{Fe}} (-0{,}44\\text{ V}) \\implies \\text{Mg } (-2{,}37\\text{ V}) \\text{ dan Zn } (-0{,}76\\text{ V})",
            "legend": "• Logam dengan $E^\\circ$ lebih negatif akan teroksidasi lebih dahulu di anoda: $\\text{M} \\to \\text{M}^{n+} + ne^-$<br>• Besi dipaksa bertindak sebagai katoda (menerima elektron sehingga tidak berkarat)<br>• Logam seperti Sn dan Cu justru mempercepat korosi besi jika lapisan pelindungnya tergores"
        },
        "hints": {
            "concept": "Syarat anoda korban: logam harus memiliki E0 reduksi lebih negatif daripada besi (-0,44 V) agar teroksidasi lebih dahulu. Pilih logam dengan E0 < -0,44 V.",
            "execution": "Mg (-2,37 V) dan Zn (-0,76 V) memiliki E0 lebih negatif dari Fe (-0,44 V)."
        }
    },
    {
        "id": "kim-lat-m-16",
        "materi": "ELEKTROLISIS (PERSAINGAN REDUKSI AIR)",
        "topic": "Reaksi Katoda dan Anoda pada Elektrolisis Larutan NaCl",
        "stem": "Larutan natrium klorida pekat ($\\text{NaCl } 1\\text{ M}$) dielektrolisis menggunakan elektroda karbon (grafit) inert. Reaksi yang terjadi di katoda dan gas yang dihasilkan di anoda berturut-turut adalah...",
        "correct": "Di katoda terjadi reduksi air: $2\\,\\text{H}_2\\text{O}(l) + 2e^- \\to \\text{H}_2(g) + 2\\,\\text{OH}^-(aq)$ dan di anoda dihasilkan gas klorin ($\\text{Cl}_2$), karena kation natrium ($\\text{Na}^+$, logam alkali golongan IA) memiliki potensial reduksi yang sangat negatif ($E^\\circ = -2{,}71\\text{ V}$) sehingga air lebih mudah tereduksi di katoda menghasilkan gas hidrogen dan suasana basa, sedangkan pada konsentrasi pekat ion halida $\\text{Cl}^-$ teroksidasi di anoda menghasilkan gas $\\text{Cl}_2$.",
        "distractors": [
            "Di katoda terjadi reduksi natrium: $\\text{Na}^+ + e^- \\to \\text{Na}(s)$ dan di anoda dihasilkan gas oksigen ($\\text{O}_2$).",
            "Di katoda dihasilkan gas hidrogen dan di anoda terjadi oksidasi air menghasilkan gas oksigen murni.",
            "Di katoda terjadi pengendapan natrium cair dan di anoda dihasilkan gas hidrogen klorida beracun.",
            "Di katoda terjadi oksidasi ion hidroksida dan di anoda dihasilkan endapan garam kristal natrium klorida."
        ],
        "formula": {
            "title": "ELEKTROLISIS LARUTAN NaCl (PROSES CHLOR-ALKALI)",
            "latex": "\\begin{aligned} \\text{Katoda (-): } & 2\\text{H}_2\\text{O}(l) + 2e^- \\to \\text{H}_2(g) + 2\\text{OH}^-(aq) \\\\ \\text{Anoda (+): } & 2\\text{Cl}^-(aq) \\to \\text{Cl}_2(g) + 2e^- \\\\ \\hline \\text{Reaksi Sel: } & 2\\text{NaCl} + 2\\text{H}_2\\text{O} \\to 2\\text{NaOH} + \\text{H}_2(g) + \\text{Cl}_2(g) \\end{aligned}",
            "legend": "• Kation golongan IA, IIA, Al, dan Mn dalam wujud larutan TIDAK tereduksi di katoda, melainkan air yang tereduksi<br>• Produk sampingan di katoda adalah larutan basa kuat $\\text{NaOH}$"
        },
        "hints": {
            "concept": "Dalam larutan air, kation Na+ (golongan IA) kalah bersaing dengan air: air yang tereduksi menghasilkan gas H2 dan ion OH-. Di anoda karbon, ion Cl- pekat teroksidasi jadi Cl2.",
            "execution": "Katoda: reduksi air menghasilkan gas H2. Anoda: gas Cl2."
        }
    },
    {
        "id": "kim-lat-m-17",
        "materi": "ELEKTROKIMIA (HUKUM FARADAY II)",
        "topic": "Elektrolisis Dua Sel Seri dengan Muatan Listrik Sama",
        "stem": "Dua sel elektrolisis disusun secara seri. Sel pertama berisi larutan perak nitrat ($\\text{AgNO}_3$, $A_r\\,\\text{Ag} = 108$) dan sel kedua berisi larutan tembaga(II) sulfat ($\\text{CuSO}_4$, $A_r\\,\\text{Cu} = 63{,}5$). Jika selama proses elektrolisis berlangsung pada katoda sel pertama diendapkan perak padat sebanyak $10{,}8\\text{ gram}$, massa tembaga padat yang terendapkan pada katoda sel kedua adalah...",
        "correct": "$3{,}175\\text{ gram}$, karena kedua sel tersusun seri sehingga menerima jumlah muatan listrik Faraday yang persis sama ($F_1 = F_2$). Berdasarkan Hukum Faraday II: $\\frac{w_{\\text{Cu}}}{e_{\\text{Cu}}} = \\frac{w_{\\text{Ag}}}{e_{\\text{Ag}}}$. Massa ekuivalen perak adalah $e_{\\text{Ag}} = \\frac{108}{1} = 108$, dan tembaga adalah $e_{\\text{Cu}} = \\frac{63{,}5}{2} = 31{,}75$. Maka massa tembaga adalah $w_{\\text{Cu}} = w_{\\text{Ag}} \\times \\frac{e_{\\text{Cu}}}{e_{\\text{Ag}}} = 10{,}8\\text{ g} \\times \\frac{31{,}75}{108} = 0{,}1 \\times 31{,}75 = 3{,}175\\text{ gram}$.",
        "distractors": [
            "$6{,}350\\text{ gram}$, karena valensi ion tembaga keliru dianggap satu sama seperti perak.",
            "$1{,}588\\text{ gram}$, dihitung dari kesalahan membagi massa ekuivalen tembaga dengan faktor dua lagi.",
            "$10{,}80\\text{ gram}$, karena beranggapan massa logam yang mengendap pada susunan seri selalu sama persis.",
            "$0{,}635\\text{ gram}$, dihitung dari galat pergeseran koma desimal perhitungan stoikiometri redoks."
        ],
        "formula": {
            "title": "HUKUM FARADAY II SEL SERI",
            "latex": "\\frac{w_1}{e_1} = \\frac{w_2}{e_2} \\implies w_{\\text{Cu}} = w_{\\text{Ag}} \\cdot \\frac{e_{\\text{Cu}}}{e_{\\text{Ag}}} = 10{,}8 \\times \\frac{31{,}75}{108} = 3{,}175\\text{ gram}",
            "legend": "• $e_{\\text{Ag}} = 108 / 1 = 108\\text{ g/ekivalen}$<br>• $e_{\\text{Cu}} = 63{,}5 / 2 = 31{,}75\\text{ g/ekivalen}$<br>• $w_{\\text{Cu}} = 3{,}175\\text{ gram}$"
        },
        "hints": {
            "concept": "Hukum Faraday II: w_Cu / e_Cu = w_Ag / e_Ag. e_Ag = 108/1 = 108. e_Cu = 63,5/2 = 31,75. w_Cu = 10,8 * (31,75 / 108).",
            "execution": "w_Cu = 0,1 * 31,75 = 3,175 gram."
        }
    },
    {
        "id": "kim-lat-m-18",
        "materi": "KIMIA UNSUR (PERIODE KETIGA)",
        "topic": "Sifat Asam-Basa Senyawa Hidroksida Periode Ketiga",
        "stem": "Unsur-unsur periode ketiga membentuk senyawa hidroksida: $\\text{NaOH}$, $\\text{Mg(OH)}_2$, $\\text{Al(OH)}_3$, $\\text{Si(OH)}_4$, $\\text{H}_3\\text{PO}_4$, $\\text{H}_2\\text{SO}_4$, dan $\\text{HClO}_4$. Senyawa hidroksida yang bersifat amfoter (dapat bereaksi dengan larutan asam kuat maupun basa kuat) adalah...",
        "correct": "Aluminium hidroksida ($\\text{Al(OH)}_3$), karena dalam suasana asam $\\text{Al(OH)}_3$ bertindak sebagai basa membentuk kation $[\\text{Al}(\\text{H}_2\\text{O})_6]^{3+}$, sedangkan dalam suasana basa kuat berlebih bertindak sebagai asam melepaskan proton membentuk anion kompleks aluminat $[\\text{Al(OH)}_4]^-$.",
        "distractors": [
            "Magnesium hidroksida ($\\text{Mg(OH)}_2$), karena merupakan basa lemah yang tidak dapat larut dalam larutan basa kuat berlebih.",
            "Natrium hidroksida ($\\text{NaOH}$), karena merupakan basa kuat monoprotik murni yang tidak bereaksi dengan basa.",
            "Silikon hidroksida ($\\text{Si(OH)}_4$), karena merupakan asam silikat lemah yang hanya bereaksi dengan basa.",
            "Asam perklorat ($\\text{HClO}_4$), karena merupakan salah satu asam oksi terkuat yang tidak memiliki sifat amfoter."
        ],
        "formula": {
            "title": "SIFAT AMFOTER ALUMINIUM HIDROKSIDA",
            "latex": "\\begin{aligned} \\text{Sebagai Basa: } & \\text{Al(OH)}_3(s) + 3\\text{H}^+(aq) \\to \\text{Al}^{3+}(aq) + 3\\text{H}_2\\text{O}(l) \\\\ \\text{Sebagai Asam: } & \\text{Al(OH)}_3(s) + \\text{OH}^-(aq) \\to [\\text{Al(OH)}_4]^-(aq) \\quad (\\text{Tetrahidroksoaluminat}) \\end{aligned}",
            "legend": "• Tren hidroksida periode 3 dari kiri ke kanan: Basa Kuat (Na) $\\to$ Basa Lemah (Mg) $\\to$ Amfoter (Al) $\\to$ Asam Sangat Lemah (Si) $\\to$ Asam Sedang (P) $\\to$ Asam Kuat (S) $\\to$ Asam Sangat Kuat (Cl)"
        },
        "hints": {
            "concept": "Di antara hidroksida periode ke-3, hanya Al(OH)3 yang bersifat amfoter: larut dalam larutan asam menghasilkan Al3+ dan larut dalam basa kuat berlebih menghasilkan [Al(OH)4]-.",
            "execution": "Al(OH)3 bersifat amfoter."
        }
    },
    {
        "id": "kim-lat-m-19",
        "materi": "SENYAWA KOMPLEKS (KIMIA KOORDINASI)",
        "topic": "Bilangan Oksidasi Logam Pusat dan Tata Nama IUPAC Kompleks",
        "stem": "Diberikan senyawa kompleks netral $[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]\\text{Cl}$. Bilangan oksidasi atom pusat kobalt, bilangan koordinasi, dan nama resmi IUPAC dari senyawa koordinasi tersebut adalah...",
        "correct": "Bilangan oksidasi kobalt $+3$, bilangan koordinasi 6, dan nama IUPAC tetraaminadiklorokobalt(III) klorida, karena ligan netral amonia ($\\text{NH}_3$) bermuatan nol dan ligan kloro ($\\text{Cl}^-$) bermuatan $-1$. Terdapat total 3 ion klorida (2 sebagai ligan dalam kurung siku dan 1 sebagai anion penyeimbang di luar), sehingga $\\text{Biloks Co} + 4(0) + 2(-1) + (-1) = 0 \\implies \\text{Biloks Co} = +3$. Jumlah ligan monodentat yang terikat langsung pada kobalt adalah $4 + 2 = 6$ (bilangan koordinasi 6).",
        "distractors": [
            "Bilangan oksidasi kobalt $+2$, bilangan koordinasi 4, dan nama IUPAC diamintetraklorokobalt(II) klorida.",
            "Bilangan oksidasi kobalt $+3$, bilangan koordinasi 4, dan nama IUPAC tetraamindiklorokobalt(III).",
            "Bilangan oksidasi kobalt $+1$, bilangan koordinasi 6, dan nama IUPAC klorotetraaminadikobalt(I).",
            "Bilangan oksidasi kobalt $+6$, bilangan koordinasi 6, dan nama IUPAC heksakobalt tetraamina triklorida."
        ],
        "formula": {
            "title": "SENYAWA KOORDINASI KOBALT(III)",
            "latex": "[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]^+ + \\text{Cl}^- \\implies \\text{Muatan Ion Kompleks} = +1 \\implies \\text{Biloks Co} = +1 - 2(-1) = +3; \\quad \\text{BK} = 4 + 2 = 6",
            "legend": "• Aturan Penamaan: Ligan diurutkan alfabet (amina > kloro) $\\to$ nama kation kompleks $\\to$ biloks logam angka Romawi $\\to$ nama anion penyeimbang<br>• Tetraaminadiklorokobalt(III) klorida"
        },
        "hints": {
            "concept": "NH3 netral (muatan 0), Cl bermuatan -1. Ada 2 Cl di dalam kompleks dan 1 Cl di luar (total 3 Cl- = -3). Maka Co bermuatan +3. Ada 4 NH3 + 2 Cl = 6 ligan (bilangan koordinasi = 6).",
            "execution": "Biloks Co = +3, BK = 6, nama: tetraaminadiklorokobalt(III) klorida."
        }
    },
    {
        "id": "kim-lat-m-20",
        "materi": "IDENTIFIKASI GUGUS FUNGSI ORGANIK",
        "topic": "Pembedaan Aldehida dan Keton Menggunakan Pereaksi Fehling",
        "stem": "Dua senyawa organik isomer fungsi memiliki rumus molekul $\\text{C}_3\\text{H}_6\\text{O}$ (Senyawa $X$ dan Senyawa $Y$). Ketika diuji di laboratorium:<br>• Senyawa $X$ bereaksi positif dengan pereaksi Fehling menghasilkan endapan merah bata $\\text{Cu}_2\\text{O}$.<br>• Senyawa $Y$ tidak bereaksi dengan pereaksi Fehling maupun pereaksi Tollens.<br>Nama IUPAC dan rumus struktur dari Senyawa $X$ dan Senyawa $Y$ berturut-turut adalah...",
        "correct": "Senyawa $X$ adalah propanal ($\\text{CH}_3-\\text{CH}_2-\\text{CHO}$) dan Senyawa $Y$ adalah propanon (aseton, $\\text{CH}_3-\\text{CO}-\\text{CH}_3$), karena senyawa turunan alkana $\\text{C}_n\\text{H}_{2n}\\text{O}$ merupakan isomer fungsi antara aldehida (alkanal) dan keton (alkanon). Aldehida adalah reduktor yang mereduksi pereaksi Fehling menjadi endapan merah bata $\\text{Cu}_2\\text{O}$, sedangkan keton tidak dapat dioksidasi oleh pereaksi Fehling/Tollens.",
        "distractors": [
            "Senyawa $X$ adalah propanon dan Senyawa $Y$ adalah propanal, karena keton dianggap memiliki reaktivitas reduksi lebih tinggi.",
            "Senyawa $X$ adalah 1-propanol dan Senyawa $Y$ adalah metoksi etana, karena rumus molekulnya keliru disamakan dengan alkohol dan eter.",
            "Senyawa $X$ adalah asam propanoat dan Senyawa $Y$ adalah metil etanoat, karena keduanya merupakan isomer fungsi asam karboksilat dan ester.",
            "Senyawa $X$ adalah propena dan Senyawa $Y$ adalah siklopropana, karena mengasumsikan senyawa hidrokarbon tak jenuh."
        ],
        "formula": {
            "title": "UJI SPESIFIK ALDEHIDA DENGAN PEREAKSI FEHLING",
            "latex": "\\text{R-CHO} + 2\\text{Cu}^{2+} + 5\\text{OH}^- \\to \\text{R-COO}^- + \\text{Cu}_2\\text{O}(s) \\downarrow (\\text{Merah Bata}) + 3\\text{H}_2\\text{O}",
            "legend": "• Aldehida ($X$) teroksidasi menjadi asam karboksilat dan mengendapkan $\\text{Cu}_2\\text{O}$ merah bata<br>• Keton ($Y$) tidak memiliki atom hidrogen pada gugus karbonil sehingga resisten terhadap oksidasi Fehling"
        },
        "hints": {
            "concept": "C3H6O adalah rumus umum alkanal (aldehida) dan alkanon (keton). Aldehida memberi hasil positif (endapan merah bata Cu2O) dengan Fehling, sedangkan keton negatif.",
            "execution": "X = propanal (aldehida), Y = propanon (keton)."
        }
    },
    {
        "id": "kim-lat-m-21",
        "materi": "ASAM KARBOKSILAT & SIFAT KEASAMAN",
        "topic": "Pengaruh Efek Induksi Halogen terhadap Kuat Asam",
        "stem": "Urutan kekuatan asam dari senyawa asam karboksilat berikut mulai dari yang paling lemah hingga yang paling kuat adalah:<br>1. Asam asetat ($\\text{CH}_3\\text{COOH}$)<br>2. Asam kloroasetat ($\\text{CH}_2\\text{ClCOOH}$)<br>3. Asam dikloroasetat ($\\text{CHCl}_2\\text{COOH}$)<br>4. Asam trikloroasetat ($\\text{CCl}_3\\text{COOH}$)",
        "correct": "$1 < 2 < 3 < 4$ (Asam asetat < Asam kloroasetat < Asam dikloroasetat < Asam trikloroasetat), karena atom klorin bersifat sangat elektronegatif dan memberikan efek induksi penarik elektron ($-I$) yang kuat di sepanjang ikatan karbon. Semakin banyak atom klorin yang terikat, semakin terdispersi muatan negatif pada ion karboksilat konjugatnya, sehingga ion konjugat menjadi jauh lebih stabil dan asam semakin mudah melepaskan proton $\\text{H}^+$ (kekuatan asam bertambah besar).",
        "distractors": [
            "$4 < 3 < 2 < 1$, karena beranggapan atom halogen yang banyak justru menghalangi pelepasan ion hidrogen secara sterik.",
            "$2 < 3 < 4 < 1$, karena asam asetat tanpa substituen dianggap memiliki kemurnian disosiasi paling tinggi.",
            "$1 < 4 < 2 < 3$, dihitung dari perbedaan massa molar substituen halogen pada rantai karbon.",
            "$1 = 2 = 3 = 4$, karena seluruh senyawa memiliki gugus karboksilat yang sama persis sehingga nilai Ka identik."
        ],
        "formula": {
            "title": "EFEK INDUKSI PENARIK ELEKTRON TERHADAP pKa",
            "latex": "\\text{Kekuatan Asam: } \\text{CH}_3\\text{COOH} (K_a = 1{,}8 \\times 10^{-5}) < \\text{CH}_2\\text{ClCOOH} (1{,}4 \\times 10^{-3}) < \\text{CHCl}_2\\text{COOH} (5 \\times 10^{-2}) < \\text{CCl}_3\\text{COOH} (0{,}2)",
            "legend": "• Efek induksi $-I$ dari atom klorin menstabilkan muatan negatif anion karboksilat ($-\\text{COO}^-$)<br>• Jumlah gugus penarik elektron $\\uparrow \\implies K_a \\uparrow \\implies \\text{Kekuatan Asam} \\uparrow$"
        },
        "hints": {
            "concept": "Gugus penarik elektron (seperti Cl) memperkuat sifat asam dengan menstabilkan ion karboksilat melalui efek induksi. Semakin banyak atom Cl, asam semakin kuat.",
            "execution": "Urutan dari paling lemah: asam asetat (1) < kloroasetat (2) < dikloroasetat (3) < trikloroasetat (4)."
        }
    },
    {
        "id": "kim-lat-m-22",
        "materi": "ISOMERISME OPTIS AKTIF",
        "topic": "Penentuan Jumlah Isomer Optis dari Atom Karbon Asimetris",
        "stem": "Senyawa 2,3-diklorobutana memiliki rumus struktur $\\text{CH}_3-\\text{CH(Cl)}-\\text{CH(Cl)}-\\text{CH}_3$. Jumlah atom karbon kiral (karbon asimetris) pada molekul tersebut dan jumlah stereoisomer optis yang dimilikinya (termasuk memperhitungkan senyawa bentuk meso) adalah...",
        "correct": "Memiliki 2 atom karbon kiral dan menghasilkan 3 stereoisomer (sepasang enantiomer optis aktif dan satu bentuk meso optis inaktif), karena molekul memiliki bidang simetri internal (achiral plane) sehingga bentuk $(2R, 3S)$ identik dengan bayangan cerminnya sendiri (senyawa meso), sedangkan pasangan $(2R, 3R)$ dan $(2S, 3S)$ membentuk sepasang enantiomer aktif.",
        "distractors": [
            "Memiliki 2 atom karbon kiral dan menghasilkan 4 stereoisomer optis aktif tanpa ada bentuk meso.",
            "Memiliki 1 atom karbon kiral dan menghasilkan 2 stereoisomer pasangan enantiomer.",
            "Memiliki 4 atom karbon kiral dan menghasilkan 16 stereoisomer berbeda.",
            "Tidak memiliki atom karbon kiral sama sekali sehingga hanya memiliki satu bentuk geometri tunggal."
        ],
        "formula": {
            "title": "STEREOISOMER DENGAN BIDANG SIMETRI (BENTUK MESO)",
            "latex": "\\text{Jumlah Isomer Teoritis} = 2^n = 2^2 = 4; \\quad \\text{Karena simetris: } (2R, 3S) \\equiv \\text{Meso} \\implies \\text{Total Isomer} = 2^{n-1} + 2^{\\frac{n}{2}-1} = 2 + 1 = 3",
            "legend": "• C kiral: $C_2$ dan $C_3$ (masing-masing mengikat $-\\text{H}$, $-\\text{Cl}$, $-\\text{CH}_3$, dan rantai sisa)<br>• Bentuk meso memutar bidang polarisasi cahaya ke arah berlawanan dalam satu molekul sehingga saling meniadakan (optis inaktif)"
        },
        "hints": {
            "concept": "C kiral di C2 dan C3 (ada 2 atom C kiral). Karena molekul simetris, ada bentuk meso (tidak aktif optik) selain 1 pasang enantiomer. Total stereoisomer = 3.",
            "execution": "2 atom C kiral, 3 stereoisomer (2 enantiomer + 1 bentuk meso)."
        }
    },
    {
        "id": "kim-lat-m-23",
        "materi": "MAKROMOLEKUL (POLIMER KARET ALAM)",
        "topic": "Monomer Karet Alam dan Proses Vulkanisasi Belerang",
        "stem": "Karet alam tersusun atas polimerisasi monomer hidrokarbon alami. Nama monomer karet alam dan tujuan dilakukannya proses vulkanisasi dengan pemanasan bersama serbuk belerang adalah...",
        "correct": "Monomernya adalah 2-metil-1,3-butadiena (isoprena) dengan konfigurasi cis-1,4-poliisoprena, dan vulkanisasi bertujuan membentuk jembatan silang belerang (cross-linking $-S-S-$) antar-rantai polimer sehingga karet menjadi lebih elastis, kuat, tahan aus, dan tidak mudah meleleh atau lengket oleh panas.",
        "distractors": [
            "Monomernya adalah stirena dan vulkanisasi bertujuan memutuskan rantai ikatan karbon agar karet menjadi lunak dan mudah dibentuk.",
            "Monomernya adalah kloroprena dan vulkanisasi bertujuan menggantikan seluruh ikatan rangkap dua dengan ikatan ionik polar.",
            "Monomernya adalah vinil klorida dan vulkanisasi bertujuan meningkatkan daya larut karet di dalam pelarut organik minyak bumi.",
            "Monomernya adalah asam adipat dan vulkanisasi bertujuan menghasilkan reaksi kondensasi pembentukan serat benang sintetis."
        ],
        "formula": {
            "title": "STRUKTUR KARET ALAM & VULKANISASI GOODYEAR",
            "latex": "n\\,(\\text{CH}_2=\\text{C}(\\text{CH}_3)-\\text{CH}=\\text{CH}_2) \\xrightarrow{\\text{Polimerisasi}} [-\\text{CH}_2-\\text{C}(\\text{CH}_3)=\\text{CH}-\\text{CH}_2-]_n \\quad (\\text{cis-Poliisoprena})",
            "legend": "• Monomer: Isoprena (2-metil-1,3-butadiena)<br>• Jembatan belerang disulfida mengikat rantai-rantai poliisoprena, memberikan memori bentuk elastis (mencegah pergeseran permanen antar-rantai saat diregangkan)"
        },
        "hints": {
            "concept": "Karet alam adalah cis-1,4-poliisoprena (monomer isoprena = 2-metil-1,3-butadiena). Vulkanisasi belerang membentuk jembatan silang (-S-S-) agar karet lebih elastis dan tahan panas.",
            "execution": "Monomer isoprena, vulkanisasi membentuk jembatan silang belerang untuk meningkatkan elastisitas dan ketahanan panas."
        }
    },
    {
        "id": "kim-lat-m-24",
        "materi": "BIOKIMIA (UJI SPESIFIK KARBOHIDRAT)",
        "topic": "Reaksi Uji Fehling, Iodin, dan Seliwanoff pada Karbohidrat",
        "stem": "Seorang siswa menguji tiga sampel larutan karbohidrat ($A$, $B$, dan $C$) di laboratorium biokimia dengan hasil sebagai berikut:<br>• Sampel $A$ memberikan warna biru kehitaman pekat dengan larutan iodin.<br>• Sampel $B$ bereaksi positif menghasilkan endapan merah bata dengan pereaksi Fehling dan memberikan warna merah ceri cepat dengan uji Seliwanoff.<br>• Sampel $C$ tidak mereduksi Fehling tetapi setelah dihidrolisis dengan asam encer menghasilkan dua jenis monosakarida berbeda yang mereduksi Fehling.<br>Identitas karbohidrat $A$, $B$, dan $C$ berturut-turut adalah...",
        "correct": "$A$ adalah amilum (pati), $B$ adalah fruktosa, dan $C$ adalah sukrosa, karena amilum membentuk kompleks biru kehitaman dengan iodin; fruktosa adalah monosakarida ketosa pereduksi yang cepat bereaksi positif dengan uji Seliwanoff membentuk warna merah ceri; dan sukrosa adalah disakarida non-pereduksi yang terhidrolisis menjadi glukosa dan fruktosa.",
        "distractors": [
            "$A$ adalah glukosa, $B$ adalah maltosa, dan $C$ adalah selulosa.",
            "$A$ adalah selulosa, $B$ adalah galaktosa, dan $C$ adalah laktosa.",
            "$A$ adalah amilum, $B$ adalah sukrosa, dan $C$ adalah glikogen.",
            "$A$ adalah glikogen, $B$ adalah amilum, dan $C$ adalah maltosa."
        ],
        "formula": {
            "title": "UJI SPESIFIK KARBOHIDRAT",
            "latex": "\\begin{aligned} \\text{Amilum} + \\text{I}_2 & \\to \\text{Kompleks Biru-Kehitaman} \\\\ \\text{Fruktosa (Ketosa)} + \\text{Resorsinol (Seliwanoff)} & \\to \\text{Merah Ceri Cepat (< 1 menit)} \\\\ \\text{Sukrosa} + \\text{H}_2\\text{O} & \\xrightarrow{\\text{H}^+} \\text{Glukosa (Pereduksi)} + \\text{Fruktosa (Pereduksi)} \\end{aligned}",
            "legend": "• Amilum = Polisakarida (uji Iodin positif)<br>• Fruktosa = Ketoheksosa pereduksi (Fehling positif, Seliwanoff merah cepat)<br>• Sukrosa = Disakarida non-pereduksi ikatan $\\alpha-1,\\beta-2$"
        },
        "hints": {
            "concept": "Uji iodin biru kehitaman = amilum. Uji Seliwanoff merah ceri cepat (ketosa) + Fehling positif = fruktosa. Disakarida non-pereduksi yang hidrolisisnya menghasilkan 2 gula berbeda = sukrosa.",
            "execution": "A = amilum, B = fruktosa, C = sukrosa."
        }
    },
    {
        "id": "kim-lat-m-25",
        "materi": "BIOKIMIA (UJI PROTEIN & DENATURASI)",
        "topic": "Reaksi Biuret, Xantoproteat, dan Uji Belerang Timbal Asetat",
        "stem": "Suatu larutan putih telur (albumin) diuji dengan beberapa pereaksi protein:<br>• Ditambahkan larutan $\\text{NaOH}$ encer dan beberapa tetes $\\text{CuSO}_4$ encer menghasilkan warna ungu pekat.<br>• Ditambahkan asam nitrat pekat ($\\text{HNO}_3$) lalu dipanaskan menghasilkan endapan kuning yang berubah menjadi jingga saat dibasakan.<br>• Ditambahkan $\\text{NaOH}$ pekat dan larutan timbal(II) asetat ($\\text{Pb(CH}_3\\text{COO)}_2$) lalu dipanaskan menghasilkan endapan hitam pekat.<br>Informasi struktural yang diperoleh dari ketiga uji biokimiawi tersebut berturut-turut adalah...",
        "correct": "Mengandung ikatan peptida (uji Biuret positif ungu), memiliki asam amino berinti cincin benzena seperti tirosin/triptofan (uji Xantoproteat positif kuning-jingga), dan mengandung asam amino yang memiliki atom belerang seperti sistein/metionin (uji timbal asetat positif endapan $\\text{PbS}$ hitam).",
        "distractors": [
            "Mengandung gugus karbohidrat monosakarida, memiliki ikatan ester lemak, dan mengandung ion kalsium terlarut.",
            "Mengandung asam nukleat DNA, memiliki rantai peptida terbuka, dan mengandung ikatan glikosidik bercabang.",
            "Mengandung protein globular sederhana tanpa ikatan peptida dan tidak memiliki gugus sulfur aktif.",
            "Mengandung lipid fosfolipid membran sel dan asam amino nonpolar alifatik rantai lurus murni."
        ],
        "formula": {
            "title": "UJI KARAKTERISTIK PROTEIN & ASAM AMINO",
            "latex": "\\begin{aligned} \\text{Uji Biuret (}\\text{Cu}^{2+} + \\text{OH}^-\\text{)} & \\to \\text{Ungu} \\implies \\ge 2\\text{ Ikatan Peptida} \\\\ \\text{Uji Xantoproteat (}\\text{HNO}_3\\text{)} & \\to \\text{Kuning} \\to \\text{Jingga} \\implies \\text{Cincin Benzena (Tirosin, Fenilalanin)} \\\\ \\text{Uji Timbal Asetat (}\\text{Pb}^{2+}\\text{)} & \\to \\text{PbS}(s) \\downarrow (\\text{Hitam}) \\implies \\text{Belerang (Sistein, Metionin)} \\end{aligned}",
            "legend": "• Biuret mendeteksi kompleks koordinasi tembaga dengan nitrogen ikatan peptida<br>• Nitrasi cincin aromatik menghasilkan senyawa nitro aromatik berwarna kuning<br>• Pembentukan $\\text{PbS}$ membuktikan adanya belerang tereduksi"
        },
        "hints": {
            "concept": "Uji Biuret (ungu) = ikatan peptida. Uji Xantoproteat (kuning/jingga) = cincin benzena. Uji timbal asetat (endapan PbS hitam) = belerang/sulfur.",
            "execution": "Ikatan peptida, cincin benzena, dan unsur belerang."
        }
    }
]
