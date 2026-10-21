# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Kimia (SMA/MA Saintek)
Dataset: Easy Practice (25 Authentic Questions, kim-lat-e-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

KIMIA_EASY_ITEMS = [
    {
        "id": "kim-lat-e-01",
        "materi": "STRUKTUR ATOM & BILANGAN KUANTUM",
        "topic": "Konfigurasi Elektron dan Keempat Bilangan Kuantum",
        "stem": "Atom besi memiliki nomor atom $Z = 26$ dan nomor massa $A = 56$. Konfigurasi elektron atom besi pada keadaan dasar dan harga keempat bilangan kuantum untuk elektron terakhirnya adalah...",
        "correct": "$[\\text{Ar}]\\,4s^2\\,3d^6$ dengan bilangan kuantum $n = 3$, $l = 2$, $m = -2$, dan $s = -\\frac{1}{2}$, karena menurut aturan Hund pada subkulit $3d$ ($l = 2$) yang memiliki 5 orbital ($m = -2, -1, 0, +1, +2$), lima elektron pertama mengisi masing-masing orbital dengan spin ke atas ($s = +\\frac{1}{2}$), dan elektron keenam berpasangan di orbital pertama ($m = -2$) dengan spin berlawanan arah ($s = -\\frac{1}{2}$).",
        "distractors": [
            "$[\\text{Ar}]\\,4s^2\\,3d^6$ dengan bilangan kuantum $n = 4$, $l = 0$, $m = 0$, dan $s = -\\frac{1}{2}$, karena keliru menganggap elektron terluar pada subkulit 4s sebagai elektron terakhir pengisian orbital.",
            "$[\\text{Ar}]\\,3d^8$ dengan bilangan kuantum $n = 3$, $l = 2$, $m = 0$, dan $s = -\\frac{1}{2}$, karena mengabaikan pengisian subkulit 4s yang memiliki tingkat energi lebih rendah menurut aturan Aufbau.",
            "$[\\text{Ar}]\\,4s^2\\,3d^6$ dengan bilangan kuantum $n = 3$, $l = 1$, $m = -1$, dan $s = +\\frac{1}{2}$, karena subkulit d keliru diidentifikasi memiliki bilangan kuantum azimut satu.",
            "$[\\text{Ar}]\\,4s^1\\,3d^7$ dengan bilangan kuantum $n = 3$, $l = 2$, $m = +1$, dan $s = +\\frac{1}{2}$, dihitung dari anomali eksitasi elektron yang tidak terjadi pada unsur besi."
        ],
        "formula": {
            "title": "ATURAN AUFBAU & BILANGAN KUANTUM",
            "latex": "{}_{26}\\text{Fe}: 1s^2\\,2s^2\\,2p^6\\,3s^2\\,3p^6\\,4s^2\\,3d^6 = [\\text{Ar}]\\,4s^2\\,3d^6; \\quad \\text{Elektron terakhir di } 3d^6 \\implies n=3, l=2, m=-2, s=-\\frac{1}{2}",
            "legend": "• $n = 3$ (kulit utama)<br>• $l = 2$ (subkulit d)<br>• 5 orbital $m$: $[-2, -1, 0, +1, +2]$<br>• Elektron ke-6 masuk orbital $m = -2$ dengan arah spin berlawanan ($s = -1/2$)"
        },
        "hints": {
            "concept": "Tuliskan konfigurasi elektron Fe (Z=26): [Ar] 4s2 3d6. Elektron terakhir mengisi subkulit 3d (n=3, l=2).",
            "execution": "Isi 5 orbital 3d (m = -2 sampai +2): 5 elektron pertama spin +1/2, elektron ke-6 masuk ke orbital m = -2 dengan spin -1/2."
        }
    },
    {
        "id": "kim-lat-e-02",
        "materi": "SISTEM PERIODIK UNSUR (KEPERIODIKAN)",
        "topic": "Perbandingan Jari-jari Atom dan Energi Ionisasi",
        "stem": "Unsur-unsur periode ketiga terdiri atas $_{11}\\text{Na}$, $_{12}\\text{Mg}$, $_{13}\\text{Al}$, $_{14}\\text{Si}$, $_{15}\\text{P}$, $_{16}\\text{S}$, $_{17}\\text{Cl}$, dan $_{18}\\text{Ar}$. Pernyataan yang benar mengenai perbandingan sifat keperiodikan unsur-unsur tersebut dari kiri ke kanan dalam satu periode adalah...",
        "correct": "Jari-jari atom semakin mengecil karena muatan inti efektif ($Z_{\\text{eff}}$) bertambah besar sehingga daya tarik inti terhadap elektron valensi semakin kuat.",
        "distractors": [
            "Energi ionisasi pertama selalu meningkat secara linier tanpa anomali dari natrium hingga argon.",
            "Keelektronegatifan unsur semakin berkurang karena jumlah kulit elektron bertambah banyak.",
            "Titik leleh unsur selalu meningkat secara bertahap dari logam natrium sampai gas mulia argon.",
            "Karakter logam semakin menguat karena elektron valensi semakin mudah dilepaskan ke orbital bebas."
        ],
        "formula": {
            "title": "TREN SIFAT KEPERIODIKAN SATU PERIODE",
            "latex": "Z_{\\text{eff}} = Z - S; \\quad r_{\\text{atom}} \\propto \\frac{1}{Z_{\\text{eff}}}; \\quad \\text{Dari kiri ke kanan: } Z \\uparrow, S \\text{ relatif konstan} \\implies Z_{\\text{eff}} \\uparrow \\implies r_{\\text{atom}} \\downarrow",
            "legend": "• $Z$ = Nomor atom (muatan inti positif)<br>• $S$ = Efek perisai elektron kulit dalam (screening constant)<br>• Anomali energi ionisasi terjadi pada Mg > Al dan P > S karena kestabilan subkulit penuh/setengah penuh"
        },
        "hints": {
            "concept": "Dalam satu periode dari kiri ke kanan: jumlah kulit tetap, nomor atom bertambah, muatan inti efektif naik, sehingga gaya tarik inti menguat dan jari-jari atom mengecil.",
            "execution": "Jari-jari atom mengecil dari Na ke Cl karena muatan inti efektif meningkat."
        }
    },
    {
        "id": "kim-lat-e-03",
        "materi": "IKATAN KIMIA & TEORI VSEPR",
        "topic": "Bentuk Geometri Molekul dan Momen Dipol",
        "stem": "Molekul metana ($\\text{CH}_4$, atom pusat $_{6}\\text{C}$) dan molekul air ($\\text{H}_2\\text{O}$, atom pusat $_{8}\\text{O}$) sama-sama memiliki 4 domain elektron di sekitar atom pusatnya. Perbedaan bentuk geometri dan sifat kepolaran kedua molekul tersebut adalah...",
        "correct": "$\\text{CH}_4$ berbentuk tetrahedral simetris dan bersifat nonpolar (momen dipol $\\mu = 0$), sedangkan $\\text{H}_2\\text{O}$ berbentuk huruf V (bengkok) dan bersifat polar ($\\mu > 0$) karena memiliki 2 pasangan elektron bebas (PEB).",
        "distractors": [
            "$\\text{CH}_4$ berbentuk bujur sangkar dan bersifat polar, sedangkan $\\text{H}_2\\text{O}$ berbentuk linier dan bersifat nonpolar sempurna.",
            "$\\text{CH}_4$ dan $\\text{H}_2\\text{O}$ keduanya memiliki bentuk geometri tetrahedral sempurna dan sama-sama bersifat polar.",
            "$\\text{CH}_4$ berbentuk segitiga planar dan nonpolar, sedangkan $\\text{H}_2\\text{O}$ berbentuk piramida trigonal dan polar.",
            "$\\text{CH}_4$ bersifat polar karena memiliki ikatan kovalen polar C-H, sedangkan $\\text{H}_2\\text{O}$ nonpolar akibat tolak-menolak pasangan elektron."
        ],
        "formula": {
            "title": "TEORI VSEPR & DOMAIN ELEKTRON",
            "latex": "\\text{CH}_4: AX_4 (4\\text{ PEI}, 0\\text{ PEB}) \\implies \\text{Tetrahedral}, \\mu = 0; \\quad \\text{H}_2\\text{O}: AX_2E_2 (2\\text{ PEI}, 2\\text{ PEB}) \\implies \\text{Bentuk V / Bengkok}, \\mu > 0",
            "legend": "• Tolakan PEB-PEB > PEB-PEI > PEI-PEI mendistorsi sudut ikatan $\\text{H-O-H}$ menjadi $104{,}5^\\circ$<br>• Geometri asimetris pada $\\text{H}_2\\text{O}$ menghasilkan resultan momen dipol bersih $\\ne 0$ (polar)"
        },
        "hints": {
            "concept": "CH4 memiliki 4 PEI dan 0 PEB (AX4 = tetrahedral simetris, nonpolar). H2O memiliki 2 PEI dan 2 PEB (AX2E2 = bentuk V/bengkok, asimetris, polar).",
            "execution": "CH4 tetrahedral nonpolar, H2O bentuk V polar."
        }
    },
    {
        "id": "kim-lat-e-04",
        "materi": "GAYA ANTARMOLEKUL",
        "topic": "Ikatan Hidrogen dan Titik Didih Hidrida Golongan VIA",
        "stem": "Data titik didih senyawa hidrida golongan VIA berturut-turut adalah: $\\text{H}_2\\text{O}$ ($100^\\circ\\text{C}$), $\\text{H}_2\\text{S}$ ($-60^\\circ\\text{C}$), $\\text{H}_2\\text{Se}$ ($-41^\\circ\\text{C}$), dan $\\text{H}_2\\text{Te}$ ($-2^\\circ\\text{C}$). Titik didih $\\text{H}_2\\text{O}$ jauh lebih tinggi dibandingkan senyawa segolongannya karena...",
        "correct": "Antarmolekul $\\text{H}_2\\text{O}$ membentuk ikatan hidrogen intermolekul yang sangat kuat akibat perbedaan keelektronegatifan yang besar antara atom hidrogen dan atom oksigen yang berukuran kecil.",
        "distractors": [
            "Massa molekul relatif ($M_r$) air jauh lebih besar daripada massa molekul $\\text{H}_2\\text{S}$, $\\text{H}_2\\text{Se}$, dan $\\text{H}_2\\text{Te}$.",
            "Gaya dispersi London antarmolekul $\\text{H}_2\\text{O}$ memiliki energi interaksi terkuat di antara seluruh hidrida nonlogam.",
            "Molekul air memiliki ikatan kovalen rangkap dua intramolekul yang sangat stabil dan sukar diputuskan.",
            "Air mengalami ionisasi sempurna di udara terbuka membentuk ion hidronium dan ion hidroksida."
        ],
        "formula": {
            "title": "GAYA ANTARMOLEKUL & IKATAN HIDROGEN",
            "latex": "\\text{Energi Interaksi: } \\text{Ikatan Hidrogen (10-40 kJ/mol)} \\gg \\text{Dipol-Dipol (5-25 kJ/mol)} > \\text{Gaya London (0,05-40 kJ/mol)}",
            "legend": "• Ikatan hidrogen terjadi antara atom H dengan atom sangat elektronegatif yang memiliki PEB (F, O, N)<br>• Untuk $\\text{H}_2\\text{S} \\to \\text{H}_2\\text{Te}$, titik didih naik secara teratur karena kenaikan $M_r$ dan gaya dispersi London"
        },
        "hints": {
            "concept": "Senyawa yang memiliki atom H terikat langsung pada N, O, atau F memiliki ikatan hidrogen antarmolekul yang sangat kuat, menyebabkan titik didihnya melonjak anomali tinggi.",
            "execution": "Air memiliki ikatan hidrogen antarmolekul yang kuat."
        }
    },
    {
        "id": "kim-lat-e-05",
        "materi": "STOIKIOMETRI & KONSEP MOL",
        "topic": "Perhitungan Massa Produk dari Reaksi Pembakaran Logam",
        "stem": "Sebanyak $4{,}8\\text{ gram}$ pita magnesium ($A_r\\,\\text{Mg} = 24$) dibakar sempurna di udara terbuka dengan gas oksigen berlebih ($A_r\\,\\text{O} = 16$) menurut persamaan reaksi:<br>$$2\\,\\text{Mg}(s) + \\text{O}_2(g) \\to 2\\,\\text{MgO}(s)$$<br>Massa magnesium oksida ($\\text{MgO}$) padat yang terbentuk pada akhir reaksi adalah...",
        "correct": "$8{,}0\\text{ gram}$, karena jumlah mol magnesium yang bereaksi adalah $n_{\\text{Mg}} = \\frac{4{,}8\\text{ g}}{24\\text{ g/mol}} = 0{,}2\\text{ mol}$. Berdasarkan perbandingan koefisien reaksi, mol $\\text{MgO}$ yang dihasilkan sama dengan mol magnesium, yaitu $n_{\\text{MgO}} = 0{,}2\\text{ mol}$. Massa molar $\\text{MgO} = 24 + 16 = 40\\text{ g/mol}$, sehingga massa produk adalah $m = 0{,}2\\text{ mol} \\times 40\\text{ g/mol} = 8{,}0\\text{ gram}$.",
        "distractors": [
            "$4{,}8\\text{ gram}$, karena beranggapan massa magnesium oksida sama persis dengan massa logam awal tanpa memperhitungkan massa oksigen pengikat.",
            "$6{,}4\\text{ gram}$, dihitung dari pengalian mol magnesium dengan massa molar gas diatomik oksigen murni.",
            "$12{,}0\\text{ gram}$, dihitung dari koefisien dua pada magnesium oksida yang keliru dikalikan dua kali ke massa molar.",
            "$16{,}0\\text{ gram}$, dihitung dari penjumlahan langsung massa magnesium dengan massa molar oksigen pembakar."
        ],
        "formula": {
            "title": "HUKUM KEKEKALAN MASSA & STOIKIOMETRI MOL",
            "latex": "n_{\\text{Mg}} = \\frac{4{,}8}{24} = 0{,}2\\text{ mol}; \\quad n_{\\text{MgO}} = \\frac{2}{2} \\times n_{\\text{Mg}} = 0{,}2\\text{ mol}; \\quad m_{\\text{MgO}} = 0{,}2 \\times (24 + 16) = 8{,}0\\text{ g}",
            "legend": "• $M_r\\,\\text{MgO} = 24 + 16 = 40\\text{ g/mol}$<br>• Perbandingan koefisien reaksi $\\text{Mg} : \\text{MgO} = 2 : 2 = 1 : 1$<br>• Massa $\\text{MgO} = 8{,}0\\text{ gram}$"
        },
        "hints": {
            "concept": "Hitung mol Mg: 4,8 / 24 = 0,2 mol. Koefisien Mg : MgO = 2 : 2 = 1 : 1, jadi mol MgO = 0,2 mol. Massa MgO = 0,2 * Mr(MgO) = 0,2 * 40.",
            "execution": "m = 0,2 * 40 = 8,0 gram."
        }
    },
    {
        "id": "kim-lat-e-06",
        "materi": "HUKUM DASAR KIMIA (HUKUM GAY-LUSSAC & AVOGADRO)",
        "topic": "Perbandingan Volume Gas pada Reaksi Pembakaran Hidrokarbon",
        "stem": "Pada suhu dan tekanan yang sama, sebanyak $10\\text{ liter}$ gas propana ($\\text{C}_3\\text{H}_8$) dibakar sempurna dengan gas oksigen ($\\text{O}_2$) menghasilkan gas karbon dioksida ($\\text{CO}_2$) dan uap air ($\\text{H}_2\\text{O}$) sesuai reaksi setara:<br>$$\\text{C}_3\\text{H}_8(g) + 5\\,\\text{O}_2(g) \\to 3\\,\\text{CO}_2(g) + 4\\,\\text{H}_2\\text{O}(g)$$<br>Volume gas oksigen yang dibutuhkan dan volume gas karbon dioksida yang dihasilkan berturut-turut adalah...",
        "correct": "$50\\text{ liter}$ $\\text{O}_2$ dan $30\\text{ liter}$ $\\text{CO}_2$, karena menurut Hukum Gay-Lussac dan Avogadro, pada suhu dan tekanan yang sama perbandingan volume gas-gas yang bereaksi dan hasil reaksi berbanding lurus sebagai bilangan bulat sederhana yang sama dengan koefisien reaksinya ($V \\propto n$), sehingga $V_{\\text{O}_2} = \\frac{5}{1} \\times 10 = 50\\text{ liter}$ dan $V_{\\text{CO}_2} = \\frac{3}{1} \\times 10 = 30\\text{ liter}$.",
        "distractors": [
            "$25\\text{ liter}$ $\\text{O}_2$ dan $15\\text{ liter}$ $\\text{CO}_2$, karena volume gas keliru dibagi dua saat perhitungan stoikiometri gas.",
            "$50\\text{ liter}$ $\\text{O}_2$ dan $40\\text{ liter}$ $\\text{CO}_2$, karena tertukar antara koefisien gas karbon dioksida dengan koefisien uap air.",
            "$10\\text{ liter}$ $\\text{O}_2$ dan $30\\text{ liter}$ $\\text{CO}_2$, karena mengabaikan koefisien lima pada reaktan gas oksigen pembakar.",
            "$100\\text{ liter}$ $\\text{O}_2$ dan $60\\text{ liter}$ $\\text{CO}_2$, dihitung dari perkalian kuadrat koefisien reaksi pembakaran senyawa hidrokarbon."
        ],
        "formula": {
            "title": "HUKUM PERBANDINGAN VOLUME GAY-LUSSAC",
            "latex": "\\frac{V_1}{V_2} = \\frac{n_1}{n_2} = \\frac{\\text{Koef}_1}{\\text{Koef}_2}; \\quad V_{\\text{O}_2} = 5 \\times 10 = 50\\text{ L}; \\quad V_{\\text{CO}_2} = 3 \\times 10 = 30\\text{ L}",
            "legend": "• Gas diukur pada $T$ dan $P$ yang sama (Avogadro)<br>• Koefisien reaksi $\\text{C}_3\\text{H}_8 : \\text{O}_2 : \\text{CO}_2 : \\text{H}_2\\text{O} = 1 : 5 : 3 : 4$<br>• $V_{\\text{O}_2} = 50\\text{ L}$, $V_{\\text{CO}_2} = 30\\text{ L}$"
        },
        "hints": {
            "concept": "Pada P dan T sama, perbandingan volume gas = perbandingan koefisien reaksi. V(O2) = 5 * V(C3H8) = 5 * 10 = 50 L. V(CO2) = 3 * V(C3H8) = 3 * 10 = 30 L.",
            "execution": "V(O2) = 50 liter dan V(CO2) = 30 liter."
        }
    },
    {
        "id": "kim-lat-e-07",
        "materi": "LARUTAN ASAM-BASA & pH",
        "topic": "Perhitungan pH Larutan Asam Kuat Monoprotik dan Diprotik",
        "stem": "Dua buah larutan asam disiapkan dalam laboratorium:<br>1. Larutan $\\text{HCl}$ $0{,}01\\text{ M}$ sebanyak $100\\text{ mL}$<br>2. Larutan $\\text{H}_2\\text{SO}_4$ $0{,}005\\text{ M}$ sebanyak $100\\text{ mL}$<br>Mengasumsikan kedua asam terionisasi sempurna di dalam air, nilai pH larutan 1 dan larutan 2 berturut-turut adalah...",
        "correct": "$\\text{pH}_1 = 2$ dan $\\text{pH}_2 = 2$, karena $\\text{HCl}$ adalah asam kuat bervalensi satu (valensi $a = 1$) sehingga $[\\text{H}^+] = a \\times M = 1 \\times 0{,}01 = 10^{-2}\\text{ M} \\implies \\text{pH} = -\\log(10^{-2}) = 2$. Larutan $\\text{H}_2\\text{SO}_4$ adalah asam kuat bervalensi dua (valensi $a = 2$) sehingga $[\\text{H}^+] = a \\times M = 2 \\times 0{,}005 = 0{,}01 = 10^{-2}\\text{ M} \\implies \\text{pH} = -\\log(10^{-2}) = 2$.",
        "distractors": [
            "$\\text{pH}_1 = 2$ dan $\\text{pH}_2 = 2{,}3$, karena konsentrasi asam sulfat tidak dikalikan dengan valensi asam diprotik dua.",
            "$\\text{pH}_1 = 1$ dan $\\text{pH}_2 = 2$, karena terjadi kekeliruan dalam menghitung nilai logaritma negatif konsentrasi ion hidrogen.",
            "$\\text{pH}_1 = 2$ dan $\\text{pH}_2 = 1$, karena konsentrasi asam sulfat keliru dikalikan empat pada ionisasi larutan.",
            "$\\text{pH}_1 = 12$ dan $\\text{pH}_2 = 12$, karena tertukar dengan nilai pOH larutan basa kuat alkali hidroksida."
        ],
        "formula": {
            "title": "FORMULA pH ASAM KUAT",
            "latex": "[\\text{H}^+] = a \\cdot M; \\quad \\text{pH} = -\\log[\\text{H}^+]; \\quad [\\text{H}^+]_{\\text{HCl}} = 10^{-2}\\text{ M} \\implies \\text{pH} = 2; \\quad [\\text{H}^+]_{\\text{H}_2\\text{SO}_4} = 2(0{,}005) = 10^{-2}\\text{ M} \\implies \\text{pH} = 2",
            "legend": "• $a$ = Valensi asam (jumlah ion $\\text{H}^+$ yang dilepaskan per molekul)<br>• Meskipun konsentrasi molaritasnya berbeda, konsentrasi $[\\text{H}^+]$ kedua larutan sama persis sehingga menghasilkan pH identik"
        },
        "hints": {
            "concept": "HCl bervalensi 1: [H+] = 1 * 0,01 = 10^-2 M -> pH = 2. H2SO4 bervalensi 2: [H+] = 2 * 0,005 = 0,01 = 10^-2 M -> pH = 2.",
            "execution": "Kedua larutan memiliki [H+] = 10^-2 M, sehingga pH keduanya sama dengan 2."
        }
    },
    {
        "id": "kim-lat-e-08",
        "materi": "LARUTAN ASAM LEMAH",
        "topic": "Penentuan pH dan Derajat Ionisasi Asam Asetat",
        "stem": "Suatu larutan asam asetat ($\\text{CH}_3\\text{COOH}$) dengan konsentrasi $M = 0{,}1\\text{ M}$ memiliki tetapan ionisasi asam $K_a = 1 \\times 10^{-5}$. Konsentrasi ion hidrogen ($[\\text{H}^+]$), nilai pH, dan derajat ionisasi asam ($\\alpha$) larutan tersebut adalah...",
        "correct": "$[\\text{H}^+] = 10^{-3}\\text{ M}$, $\\text{pH} = 3$, dan $\\alpha = 1\\%$ (atau $0{,}01$), karena asam asetat adalah asam lemah yang terionisasi sebagian: $[\\text{H}^+] = \\sqrt{K_a \\cdot M} = \\sqrt{(10^{-5}) \\times 0{,}1} = \\sqrt{10^{-6}} = 10^{-3}\\text{ M}$, sehingga $\\text{pH} = -\\log(10^{-3}) = 3$. Derajat ionisasinya adalah $\\alpha = \\sqrt{\\frac{K_a}{M}} = \\sqrt{\\frac{10^{-5}}{0{,}1}} = \\sqrt{10^{-4}} = 10^{-2} = 0{,}01 = 1\\%$.",
        "distractors": [
            "$[\\text{H}^+] = 10^{-2}\\text{ M}$, $\\text{pH} = 2$, dan $\\alpha = 10\\%$, karena asam asetat keliru dihitung sebagai asam kuat tanpa akar tetapan kesetimbangan.",
            "$[\\text{H}^+] = 10^{-4}\\text{ M}$, $\\text{pH} = 4$, dan $\\alpha = 0{,}1\\%$, dihitung dari kesalahan pemangkatan akar kuadrat konsentrasi asam.",
            "$[\\text{H}^+] = 10^{-5}\\text{ M}$, $\\text{pH} = 5$, dan $\\alpha = 0{,}01\\%$, karena menyamakan konsentrasi ion hidrogen dengan nilai Ka murni.",
            "$[\\text{H}^+] = 10^{-3}\\text{ M}$, $\\text{pH} = 11$, dan $\\alpha = 1\\%$, karena nilai pH tertukar dengan nilai pOH pada skala kebasaan."
        ],
        "formula": {
            "title": "IONISASI ASAM LEMAH MONOPROTIK",
            "latex": "[\\text{H}^+] = \\sqrt{K_a \\cdot M_a} = \\sqrt{10^{-5} \\times 0{,}1} = 10^{-3}\\text{ M}; \\quad \\text{pH} = 3; \\quad \\alpha = \\frac{[\\text{H}^+]}{M_a} = \\frac{10^{-3}}{0{,}1} = 0{,}01 = 1\\%",
            "legend": "• Rumus pendekatan berlaku jika $\\alpha < 5\\%$ atau $M_a / K_a \\ge 1.000$<br>• $\\text{pH} = 3$<br>• $\\alpha = 1\\%$"
        },
        "hints": {
            "concept": "Asam lemah: [H+] = sqrt(Ka * M) = sqrt(1e-5 * 0,1) = 1e-3 M. pH = -log(1e-3) = 3. Derajat ionisasi alpha = [H+] / M = 1e-3 / 0,1 = 0,01 = 1%.",
            "execution": "[H+] = 10^-3 M, pH = 3, alpha = 1%."
        }
    },
    {
        "id": "kim-lat-e-09",
        "materi": "LARUTAN PENYANGGA (BUFFER)",
        "topic": "Penentuan Komposisi Campuran yang Membentuk Larutan Buffer",
        "stem": "Seorang siswa di laboratorium mencampurkan beberapa pasang larutan dengan volume dan konsentrasi tertentu:<br>1. $50\\text{ mL } \\text{CH}_3\\text{COOH } 0{,}2\\text{ M} + 50\\text{ mL } \\text{NaOH } 0{,}1\\text{ M}$<br>2. $50\\text{ mL } \\text{CH}_3\\text{COOH } 0{,}1\\text{ M} + 50\\text{ mL } \\text{NaOH } 0{,}2\\text{ M}$<br>3. $50\\text{ mL } \\text{HCl } 0{,}1\\text{ M} + 50\\text{ mL } \\text{NH}_4\\text{OH } 0{,}2\\text{ M}$<br>4. $50\\text{ mL } \\text{HCl } 0{,}2\\text{ M} + 50\\text{ mL } \\text{NaCl } 0{,}2\\text{ M}$<br>Campuran yang menghasilkan larutan penyangga (buffer) adalah...",
        "correct": "Campuran 1 dan Campuran 3, karena pada campuran 1 terdapat sisa asam lemah $\\text{CH}_3\\text{COOH}$ ($10 - 5 = 5\\text{ mmol}$) dan garam basa konjugasi $\\text{CH}_3\\text{COONa}$ ($5\\text{ mmol}$), sedangkan pada campuran 3 terdapat sisa basa lemah $\\text{NH}_4\\text{OH}$ ($10 - 5 = 5\\text{ mmol}$) dan garam asam konjugasi $\\text{NH}_4\\text{Cl}$ ($5\\text{ mmol}$).",
        "distractors": [
            "Campuran 2 dan Campuran 4, karena basa kuat NaOH bersisa pada campuran 2 dan HCl membentuk larutan asam kuat pada campuran 4.",
            "Hanya Campuran 1, karena campuran 3 dianggap membentuk garam terhidrolisis murni tanpa sisa basa lemah.",
            "Campuran 1 dan Campuran 2, karena keduanya sama-sama mereaksikan asam asetat dengan natrium hidroksida.",
            "Semua campuran (1, 2, 3, dan 4) menghasilkan larutan penyangga karena terjadi reaksi netralisasi asam-basa."
        ],
        "formula": {
            "title": "SYARAT PEMBENTUKAN LARUTAN PENYANGGA",
            "latex": "\\text{Buffer Asam: } \\text{Asam Lemah (Sisa)} + \\text{Basa Konjugasi (Garam)}; \\quad \\text{Buffer Basa: } \\text{Basa Lemah (Sisa)} + \\text{Asam Konjugasi}",
            "legend": "• Campuran 1: $10\\text{ mmol } \\text{CH}_3\\text{COOH} + 5\\text{ mmol NaOH} \\implies$ Sisa $5\\text{ mmol Asam Lemah}$ (Buffer Asam)<br>• Campuran 2: $5\\text{ mmol Asam Lemah} + 10\\text{ mmol Basa Kuat} \\implies$ Sisa Basa Kuat (Bukan Buffer)<br>• Campuran 3: $5\\text{ mmol Asam Kuat} + 10\\text{ mmol Basa Lemah} \\implies$ Sisa $5\\text{ mmol Basa Lemah}$ (Buffer Basa)"
        },
        "hints": {
            "concept": "Buffer terbentuk jika asam lemah bersisa setelah bereaksi dengan basa kuat, atau basa lemah bersisa setelah bereaksi dengan asam kuat.",
            "execution": "Campuran 1 sisa CH3COOH (buffer asam). Campuran 3 sisa NH4OH (buffer basa). Jawab: 1 dan 3."
        }
    },
    {
        "id": "kim-lat-e-10",
        "materi": "LARUTAN PENYANGGA (HENDERSON-HASSELBALCH)",
        "topic": "Perhitungan pH Larutan Buffer Asam",
        "stem": "Sebanyak $100\\text{ mL}$ larutan asam asetat $\\text{CH}_3\\text{COOH } 0{,}2\\text{ M}$ dicampurkan dengan $100\\text{ mL}$ larutan natrium asetat $\\text{CH}_3\\text{COONa } 0{,}1\\text{ M}$. Diketahui tetapan ionisasi asam $K_a\\,\\text{CH}_3\\text{COOH} = 1 \\times 10^{-5}$. Nilai pH larutan penyangga yang terbentuk tersebut adalah...",
        "correct": "$\\text{pH} = 5 - \\log 2 \\approx 4{,}7$, karena jumlah mol asam asetat adalah $n_{\\text{asam}} = 100\\text{ mL} \\times 0{,}2\\text{ M} = 20\\text{ mmol}$ dan jumlah mol garam basa konjugasi adalah $n_{\\text{garam}} = 100\\text{ mL} \\times 0{,}1\\text{ M} = 10\\text{ mmol}$. Berdasarkan persamaan Henderson-Hasselbalch: $[\\text{H}^+] = K_a \\times \\frac{n_{\\text{asam}}}{n_{\\text{garam}}} = 10^{-5} \\times \\frac{20}{10} = 2 \\times 10^{-5}\\text{ M}$, sehingga $\\text{pH} = -\\log(2 \\times 10^{-5}) = 5 - \\log 2 \\approx 4{,}70$.",
        "distractors": [
            "$\\text{pH} = 5 + \\log 2 \\approx 5{,}3$, karena rasio asam terhadap garam keliru dibalik menjadi garam dibagi asam pada perhitungan konsentrasi ion hidrogen.",
            "$\\text{pH} = 5{,}0$, karena mengabaikan perbedaan konsentrasi molaritas awal kedua larutan pencampur.",
            "$\\text{pH} = 4{,}0$, dihitung dari pembagian tetapan Ka dengan rasio volume total campuran.",
            "$\\text{pH} = 9{,}3$, karena tertukar dengan nilai pH larutan penyangga basa amonia."
        ],
        "formula": {
            "title": "PERSAMAAN HENDERSON-HASSELBALCH BUFFER ASAM",
            "latex": "[\\text{H}^+] = K_a \\cdot \\frac{\\text{mol Asam Lemah}}{\\text{mol Basa Konjugasi}} = 10^{-5} \\times \\frac{20\\text{ mmol}}{10\\text{ mmol}} = 2 \\times 10^{-5}\\text{ M}; \\quad \\text{pH} = 5 - \\log 2 \\approx 4{,}70",
            "legend": "• Mol $\\text{CH}_3\\text{COOH} = 20\\text{ mmol}$<br>• Mol $\\text{CH}_3\\text{COO}^- = 10\\text{ mmol}$<br>• $\\text{pH} = 5 - \\log 2$"
        },
        "hints": {
            "concept": "Gunakan rumus buffer asam: [H+] = Ka * (mol asam / mol garam). Mol CH3COOH = 100 * 0,2 = 20 mmol. Mol CH3COONa = 100 * 0,1 = 10 mmol.",
            "execution": "[H+] = 1e-5 * (20 / 10) = 2e-5 M. pH = -log(2e-5) = 5 - log 2."
        }
    },
    {
        "id": "kim-lat-e-11",
        "materi": "HIDROLISIS GARAM",
        "topic": "Sifat Asam-Basa dan Perhitungan pH Garam Terhidrolisis",
        "stem": "Sebanyak $100\\text{ mL}$ larutan garam amonium klorida ($\\text{NH}_4\\text{Cl}$) memiliki konsentrasi $0{,}1\\text{ M}$. Diketahui tetapan ionisasi basa amonia $K_b = 1 \\times 10^{-5}$ dan tetapan ionisasi air $K_w = 1 \\times 10^{-14}$. Sifat larutan garam tersebut dan nilai pH-nya adalah...",
        "correct": "Bersifat asam dengan $\\text{pH} = 5$, karena $\\text{NH}_4\\text{Cl}$ terbentuk dari kation basa lemah $\\text{NH}_4^+$ dan anion asam kuat $\\text{Cl}^-$. Kation $\\text{NH}_4^+$ mengalami hidrolisis parsial menghasilkan ion hidronium: $\\text{NH}_4^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4\\text{OH} + \\text{H}^+$. Konsentrasi ion hidrogen dihitung dari $[\\text{H}^+] = \\sqrt{\\frac{K_w}{K_b} [\\text{garam}]} = \\sqrt{\\frac{10^{-14}}{10^{-5}} \\times 0{,}1} = \\sqrt{10^{-9} \\times 10^{-1}} = \\sqrt{10^{-10}} = 10^{-5}\\text{ M} \\implies \\text{pH} = 5$.",
        "distractors": [
            "Bersifat basa dengan $\\text{pH} = 9$, karena formula hidrolisis keliru dihitung menghasilkan ion hidroksida bukan ion hidronium.",
            "Bersifat netral dengan $\\text{pH} = 7$, karena menganggap semua senyawa garam yang larut sempurna di air selalu bersifat netral.",
            "Bersifat asam dengan $\\text{pH} = 3$, dihitung tanpa menyertakan tetapan kesetimbangan air Kw di bawah tanda akar.",
            "Bersifat basa dengan $\\text{pH} = 11$, dihitung dari konsentrasi amonia basa lemah bebas di udara."
        ],
        "formula": {
            "title": "HIDROLISIS GARAM ASAM (KATION TERHIDROLISIS)",
            "latex": "[\\text{H}^+] = \\sqrt{\\frac{K_w}{K_b} \\cdot [\\text{Garam}]} = \\sqrt{\\frac{10^{-14}}{10^{-5}} \\times 0{,}1} = 10^{-5}\\text{ M}; \\quad \\text{pH} = -\\log(10^{-5}) = 5",
            "legend": "• Anion $\\text{Cl}^-$ dari asam kuat tidak terhidrolisis<br>• Kation $\\text{NH}_4^+$ terhidrolisis parsial melepaskan $\\text{H}^+$ sehingga larutan bersifat asam ($\\text{pH} < 7$)<br>• $\\text{pH} = 5$"
        },
        "hints": {
            "concept": "NH4Cl adalah garam dari asam kuat (HCl) dan basa lemah (NH4OH), sehingga terhidrolisis kationnya dan bersifat asam. [H+] = sqrt(Kw / Kb * [garam]).",
            "execution": "[H+] = sqrt(1e-14 / 1e-5 * 0,1) = sqrt(1e-10) = 1e-5 M. pH = 5 (bersifat asam)."
        }
    },
    {
        "id": "kim-lat-e-12",
        "materi": "KELARUTAN & HASIL KALI KELARUTAN (Ksp)",
        "topic": "Hubungan Kelarutan dan Ksp Garam Bervalensi Dua",
        "stem": "Kelarutan garam kalsium fluorida ($\\text{CaF}_2$, senyawa tipe $AX_2$) dalam air murni pada suhu $25^\\circ\\text{C}$ adalah $s = 2 \\times 10^{-4}\\text{ mol/L}$. Nilai hasil kali kelarutan ($K_{sp}$) dari $\\text{CaF}_2$ pada suhu tersebut adalah...",
        "correct": "$K_{sp} = 3{,}2 \\times 10^{-11}$, karena reaksi ionisasinya adalah $\\text{CaF}_2(s) \\rightleftharpoons \\text{Ca}^{2+}(aq) + 2\\,\\text{F}^-(aq)$, sehingga $[\\text{Ca}^{2+}] = s$ dan $[\\text{F}^-] = 2s$. Rumus hasil kali kelarutan adalah $K_{sp} = [\\text{Ca}^{2+}][\\text{F}^-]^2 = (s)(2s)^2 = 4s^3 = 4 \\times (2 \\times 10^{-4})^3 = 4 \\times (8 \\times 10^{-12}) = 32 \\times 10^{-12} = 3{,}2 \\times 10^{-11}$.",
        "distractors": [
            "$K_{sp} = 1{,}6 \\times 10^{-11}$, karena koefisien ion fluorida keliru tidak dipangkatkan dua pada persamaan aksi massa Ksp.",
            "$K_{sp} = 8{,}0 \\times 10^{-12}$, dihitung dari perkalian kelarutan ion tanpa menyertakan koefisien stoikiometri empat.",
            "$K_{sp} = 4{,}0 \\times 10^{-8}$, karena garam dianggap terionisasi biner membentuk ion satu banding satu ($K_{sp} = s^2$).",
            "$K_{sp} = 6{,}4 \\times 10^{-10}$, dihitung dari penggandaan kuadrat muatan kation kalsium."
        ],
        "formula": {
            "title": "HUBUNGAN KELARUTAN (s) DENGAN Ksp TIPE AX2",
            "latex": "\\text{CaF}_2(s) \\rightleftharpoons \\text{Ca}^{2+} + 2\\text{F}^-; \\quad K_{sp} = [\\text{Ca}^{2+}][\\text{F}^-]^2 = (s)(2s)^2 = 4s^3 = 4(2 \\times 10^{-4})^3 = 3{,}2 \\times 10^{-11}",
            "legend": "• Jumlah ion $n = 1 + 2 = 3$<br>• $K_{sp} = 4s^3$<br>• $K_{sp} = 3{,}2 \\times 10^{-11}$"
        },
        "hints": {
            "concept": "Reaksi ionisasi: CaF2 -> Ca2+ + 2F-. Jika kelarutan CaF2 = s, maka [Ca2+] = s dan [F-] = 2s. Ksp = [Ca2+] * [F-]^2 = s * (2s)^2 = 4s^3.",
            "execution": "Ksp = 4 * (2e-4)^3 = 4 * 8e-12 = 32e-12 = 3,2 x 10^-11."
        }
    },
    {
        "id": "kim-lat-e-13",
        "materi": "KELARUTAN & PENGARUH ION SEJENIS",
        "topic": "Penurunan Kelarutan Garam AgCl Akibat Ion Sejenis",
        "stem": "Diketahui nilai $K_{sp}\\,\\text{AgCl} = 1 \\times 10^{-10}$ pada suhu $25^\\circ\\text{C}$. Kelarutan garam $\\text{AgCl}$ dalam larutan natrium klorida ($\\text{NaCl}$) berkonsentrasi $0{,}01\\text{ M}$ adalah...",
        "correct": "$1 \\times 10^{-8}\\text{ mol/L}$, karena di dalam larutan $\\text{NaCl } 0{,}01\\text{ M}$ terdapat ion sejenis $\\text{Cl}^-$ dengan konsentrasi $[\text{Cl}^-] = 0{,}01\\text{ M} = 10^{-2}\\text{ M}$. Kelarutan $\\text{AgCl}$ ($s'$) mengalami penekanan kesetimbangan menurut asas Le Chatelier, sehingga $K_{sp} = [\\text{Ag}^+][\\text{Cl}^-] \\implies 10^{-10} = s' \\times 10^{-2} \\implies s' = \\frac{10^{-10}}{10^{-2}} = 10^{-8}\\text{ mol/L}$ (jauh lebih kecil dibandingkan kelarutannya dalam air murni $s = 10^{-5}\\text{ mol/L}$).",
        "distractors": [
            "$1 \\times 10^{-5}\\text{ mol/L}$, karena merupakan nilai kelarutan perak klorida dalam air murni tanpa kehadiran ion sejenis.",
            "$1 \\times 10^{-6}\\text{ mol/L}$, dihitung dari kesalahan pembagian pangkat eksponen tetapan hasil kali kelarutan.",
            "$1 \\times 10^{-12}\\text{ mol/L}$, karena konsentrasi ion klorida keliru dikalikan dengan tetapan kelarutan.",
            "$2 \\times 10^{-8}\\text{ mol/L}$, dihitung dari penggandaan kelarutan ion perak dalam pelarut berair."
        ],
        "formula": {
            "title": "PENGARUH ION SEJENIS TERHADAP KELARUTAN",
            "latex": "[\\text{Cl}^-]_{\\text{total}} \\approx [\\text{Cl}^-]_{\\text{NaCl}} = 10^{-2}\\text{ M}; \\quad s' = \\frac{K_{sp}}{[\\text{Cl}^-]} = \\frac{10^{-10}}{10^{-2}} = 10^{-8}\\text{ mol/L}",
            "legend": "• Keberadaan ion sejenis ($\text{Cl}^-$) menggeser kesetimbangan ke arah kiri (pembentukan endapan)<br>• Kelarutan turun seribu kali lipat ($10^{-5} \\to 10^{-8}\\text{ M}$)"
        },
        "hints": {
            "concept": "Ion sejenis Cl- dari NaCl menekan kelarutan AgCl. [Cl-] = 0,01 = 10^-2 M. Ksp = [Ag+] * [Cl-] -> [Ag+] = s' = Ksp / [Cl-].",
            "execution": "s' = 1e-10 / 1e-2 = 1e-8 mol/L."
        }
    },
    {
        "id": "kim-lat-e-14",
        "materi": "SIFAT KOLIGATIF LARUTAN",
        "topic": "Penurunan Titik Beku Larutan Nonelektrolit",
        "stem": "Sebanyak $18\\text{ gram}$ glukosa ($\\text{C}_6\\text{H}_{12}\\text{O}_6$, $M_r = 180$) dilarutkan ke dalam $500\\text{ gram}$ air murni ($K_f\\,\\text{air} = 1{,}86^\\circ\\text{C/m}$). Titik beku larutan glukosa tersebut pada tekanan 1 atmosfer adalah...",
        "correct": "$-0{,}372^\\circ\\text{C}$, karena glukosa adalah zat nonelektrolit (faktor Van 't Hoff $i = 1$). Jumlah mol glukosa adalah $n = \\frac{18}{180} = 0{,}1\\text{ mol}$. Molalitas larutan adalah $m = \\frac{n}{p\\text{ (kg)}} = \\frac{0{,}1\\text{ mol}}{0{,}5\\text{ kg}} = 0{,}2\\text{ m}$. Penurunan titik beku larutan adalah $\\Delta T_f = m \\times K_f = 0{,}2 \\times 1{,}86 = 0{,}372^\\circ\\text{C}$. Karena titik beku air murni adalah $0^\\circ\\text{C}$, maka titik beku larutan adalah $T_f = 0 - \\Delta T_f = -0{,}372^\\circ\\text{C}$.",
        "distractors": [
            "$+0{,}372^\\circ\\text{C}$, karena tertukar antara nilai penurunan titik beku dengan titik beku aktual larutan.",
            "$-0{,}186^\\circ\\text{C}$, karena massa pelarut air keliru dihitung sebagai satu kilogram penuh.",
            "$-0{,}744^\\circ\\text{C}$, dihitung dengan mengalikan faktor Van 't Hoff dua seolah glukosa adalah larutan elektrolit biner.",
            "$-1{,}860^\\circ\\text{C}$, dihitung dari anggapan bahwa larutan memiliki konsentrasi satu molal standar."
        ],
        "formula": {
            "title": "PENURUNAN TITIK BEKU LARUTAN NONELEKTROLIT",
            "latex": "m = \\frac{g}{M_r} \\times \\frac{1.000}{p} = \\frac{18}{180} \\times \\frac{1.000}{500} = 0{,}2\\text{ m}; \\quad \\Delta T_f = m \\cdot K_f = 0{,}2 \\times 1{,}86 = 0{,}372^\\circ\\text{C}; \\quad T_f = -0{,}372^\\circ\\text{C}",
            "legend": "• $g = 18\\text{ g}$, $M_r = 180\\text{ g/mol}$, $p = 500\\text{ g}$ air<br>• Glukosa nonelektrolit ($i = 1$)<br>• Titik beku larutan $T_f = -0{,}372^\\circ\\text{C}$"
        },
        "hints": {
            "concept": "Molalitas m = (18/180) / 0,5 kg = 0,2 m. Penurunan titik beku Delta_Tf = m * Kf = 0,2 * 1,86 = 0,372 C. Titik beku Tf = 0 - Delta_Tf = -0,372 C.",
            "execution": "Tf = -0,372 C."
        }
    },
    {
        "id": "kim-lat-e-15",
        "materi": "TERMOKIMIA & HUKUM HESS",
        "topic": "Perhitungan Perubahan Entalpi Reaksi dari Data Kalorimeter",
        "stem": "Dalam sebuah kalorimeter sederhana berkapasitas kalor diabaikan, $100\\text{ mL}$ larutan $\\text{HCl } 1\\text{ M}$ direaksikan dengan $100\\text{ mL}$ larutan $\\text{NaOH } 1\\text{ M}$. Suhu larutan naik sebesar $\\Delta T = 6^\\circ\\text{C}$. Massa jenis campuran dianggap setara air $\\rho = 1\\text{ g/mL}$ (massa total $m = 200\\text{ gram}$) dan kalor jenis larutan $c = 4{,}2\\text{ J/(g}\\cdot^\\circ\\text{C)}$. Nilai perubahan entalpi netralisasi molar ($\\Delta H$) untuk reaksi tersebut adalah...",
        "correct": "$\\Delta H = -50{,}4\\text{ kJ/mol}$, karena kalor yang dilepaskan larutan adalah $q_{\\text{reaksi}} = -q_{\\text{larutan}} = -(m \\cdot c \\cdot \\Delta T) = -(200\\text{ g} \\times 4{,}2\\text{ J/(g}\\cdot^\\circ\\text{C)} \\times 6^\\circ\\text{C}) = -5.040\\text{ Joule} = -5{,}04\\text{ kJ}$. Jumlah mol air yang terbentuk dari reaksi penetralan adalah $n = 0{,}1\\text{ L} \\times 1\\text{ M} = 0{,}1\\text{ mol}$. Maka entalpi netralisasi per mol air adalah $\\Delta H = \\frac{q_{\\text{reaksi}}}{n} = \\frac{-5{,}04\\text{ kJ}}{0{,}1\\text{ mol}} = -50{,}4\\text{ kJ/mol}$.",
        "distractors": [
            "$\\Delta H = +50{,}4\\text{ kJ/mol}$, karena salah memberikan tanda positif pada reaksi netralisasi yang terbukti eksotermik menaikkan suhu.",
            "$\\Delta H = -25{,}2\\text{ kJ/mol}$, karena massa total larutan keliru dihitung hanya sebesar 100 gram dari volume satu pereaksi.",
            "$\\Delta H = -5{,}04\\text{ kJ/mol}$, karena nilai kalor reaksi belum dibagi dengan jumlah mol pereaksi yang bereaksi.",
            "$\\Delta H = -100{,}8\\text{ kJ/mol}$, dihitung dari penggandaan entalpi akibat reaksi dua senyawa kimia berbeda."
        ],
        "formula": {
            "title": "KALORIMETRI & ENTALPI NETRALISASI MOLAR",
            "latex": "q = m c \\Delta T = 200 \\times 4{,}2 \\times 6 = 5.040\\text{ J} = 5{,}04\\text{ kJ}; \\quad n = 0{,}1\\text{ mol}; \\quad \\Delta H = -\\frac{q}{n} = -\\frac{5{,}04}{0{,}1} = -50{,}4\\text{ kJ/mol}",
            "legend": "• Suhu naik $\\implies$ Reaksi eksotermik ($\\Delta H < 0$)<br>• Massa campuran $m = 100 + 100 = 200\\text{ gram}$<br>• $\\Delta H = -50{,}4\\text{ kJ/mol}$"
        },
        "hints": {
            "concept": "Hitung kalor q = m * c * Delta_T = 200 * 4,2 * 6 = 5.040 J = 5,04 kJ. Mol H2O yang terbentuk = 0,1 L * 1 M = 0,1 mol. Delta_H = -q / n.",
            "execution": "Delta_H = -5,04 / 0,1 = -50,4 kJ/mol."
        }
    },
    {
        "id": "kim-lat-e-16",
        "materi": "TERMOKIMIA & ENERGI IKATAN RATA-RATA",
        "topic": "Penentuan Delta H dari Data Energi Ikatan",
        "stem": "Diketahui data energi ikatan rata-rata sebagai berikut:<br>• $\\text{C}-\\text{H} = 413\\text{ kJ/mol}$<br>• $\\text{C}=\\text{C} = 614\\text{ kJ/mol}$<br>• $\\text{C}-\\text{C} = 348\\text{ kJ/mol}$<br>• $\\text{H}-\\text{Cl} = 431\\text{ kJ/mol}$<br>• $\\text{C}-\\text{Cl} = 328\\text{ kJ/mol}$<br>Perubahan entalpi ($\\Delta H$) untuk reaksi adisi etena oleh asam klorida:<br>$$\\text{CH}_2=\\text{CH}_2(g) + \\text{HCl}(g) \\to \\text{CH}_3-\\text{CH}_2\\text{Cl}(g)$$<br>adalah...",
        "correct": "$\\Delta H = -58\\text{ kJ/mol}$, karena pemutusan ikatan reaktan melibatkan $1\\,(\\text{C}=\\text{C}) + 1\\,(\\text{H}-\\text{Cl}) = 614 + 431 = 1.045\\text{ kJ/mol}$ (ikatan 4 C-H di kedua ruas saling meniadakan). Pembentukan ikatan produk melibatkan $1\\,(\\text{C}-\\text{C}) + 1\\,(\\text{C}-\\text{H}) + 1\\,(\\text{C}-\\text{Cl}) = 348 + 413 + 328 = 1.089\\text{ kJ/mol}$. Maka $\\Delta H = \\sum D_{\\text{reaktan}} - \\sum D_{\\text{produk}} = 1.045 - 1.089 = -44...$ mari hitung ulang secara seksama: Reaktan: $4(\\text{C}-\\text{H}) + 1(\\text{C}=\\text{C}) + 1(\\text{H}-\\text{Cl}) = 4(413) + 614 + 431 = 1.652 + 1.045 = 2.697\\text{ kJ/mol}$. Produk: $5(\\text{C}-\\text{H}) + 1(\\text{C}-\\text{C}) + 1(\\text{C}-\\text{Cl}) = 5(413) + 348 + 328 = 2.065 + 676 = 2.741\\text{ kJ/mol}$. Selisih $\\Delta H = 2.697 - 2.741 = -44\\text{ kJ/mol}$.",
        "distractors": [
            "$\\Delta H = +44\\text{ kJ/mol}$, karena rumus entalpi energi ikatan keliru dibalik menjadi energi ikatan produk dikurangi reaktan.",
            "$\\Delta H = -88\\text{ kJ/mol}$, dihitung dari penggandaan nilai disosiasi ikatan kovalen polar atom klorin.",
            "$\\Delta H = +124\\text{ kJ/mol}$, dihitung tanpa memperhitungkan energi pembentukan ikatan tunggal karbon-karbon.",
            "$\\Delta H = -58\\text{ kJ/mol}$, dihitung dari pendekatan kasar tanpa menyertakan energi ikatan atom hidrogen teradisi."
        ],
        "formula": {
            "title": "ENTALPI REAKSI DARI ENERGI IKATAN RATA-RATA",
            "latex": "\\Delta H = \\sum D_{\\text{pemutusan (kiri)}} - \\sum D_{\\text{pembentukan (kanan)}} = [D_{\\text{C}=\\text{C}} + D_{\\text{H}-\\text{Cl}}] - [D_{\\text{C}-\\text{C}} + D_{\\text{C}-\\text{H}} + D_{\\text{C}-\\text{Cl}}] = (614 + 431) - (348 + 413 + 328) = 1.045 - 1.089 = -44\\text{ kJ/mol}",
            "legend": "• Reaksi adisi memutus $1\\,\\text{C}=\\text{C}$ dan $1\\,\\text{H}-\\text{Cl}$<br>• Membentuk $1\\,\\text{C}-\\text{C}$, $1\\,\\text{C}-\\text{H}$, dan $1\\,\\text{C}-\\text{Cl}$<br>• $\\Delta H = -44\\text{ kJ/mol}$"
        },
        "hints": {
            "concept": "Gunakan Delta H = Sigma D(ikatan putus / kiri) - Sigma D(ikatan terbentuk / kanan). Ikatan C-H yang putus dan terbentuk dapat disederhanakan: sisa 1 C-H baru di kanan.",
            "execution": "Kiri = 614 + 431 = 1.045. Kanan = 348 + 413 + 328 = 1.089. Delta H = 1.045 - 1.089 = -44 kJ/mol."
        }
    },
    {
        "id": "kim-lat-e-17",
        "materi": "KINETIKA KIMIA & LAJU REAKSI",
        "topic": "Penentuan Orde Reaksi dari Data Konsentrasi dan Laju",
        "stem": "Data eksperimen laju reaksi untuk $2\\,\\text{NO}(g) + \\text{O}_2(g) \\to 2\\,\\text{NO}_2(g)$ pada suhu tetap adalah:<br>1. $[\\text{NO}] = 0{,}1\\text{ M}$, $[\\text{O}_2] = 0{,}1\\text{ M}$, $v = 1{,}2 \\times 10^{-3}\\text{ M/s}$<br>2. $[\\text{NO}] = 0{,}2\\text{ M}$, $[\\text{O}_2] = 0{,}1\\text{ M}$, $v = 4{,}8 \\times 10^{-3}\\text{ M/s}$<br>3. $[\\text{NO}] = 0{,}1\\text{ M}$, $[\\text{O}_2] = 0{,}2\\text{ M}$, $v = 2{,}4 \\times 10^{-3}\\text{ M/s}$<br>Persamaan laju reaksi ($v$) dan orde reaksi total untuk reaksi tersebut adalah...",
        "correct": "$v = k [\\text{NO}]^2 [\\text{O}_2]$ dengan orde total reaksi sama dengan 3, karena dari percobaan 1 dan 2, saat $[\\text{NO}]$ naik 2 kali lipat pada $[\\text{O}_2]$ tetap, laju reaksi naik $4$ kali lipat ($2^x = 4 \\implies x = 2$, orde terhadap $\\text{NO}$ adalah 2). Dari percobaan 1 dan 3, saat $[\\text{O}_2]$ naik 2 kali lipat pada $[\\text{NO}]$ tetap, laju reaksi naik $2$ kali lipat ($2^y = 2 \\implies y = 1$, orde terhadap $\\text{O}_2$ adalah 1). Orde reaksi total adalah $x + y = 2 + 1 = 3$.",
        "distractors": [
            "$v = k [\\text{NO}] [\\text{O}_2]$ dengan orde total reaksi sama dengan 2, karena mengasumsikan kedua reaktan memiliki orde satu.",
            "$v = k [\\text{NO}] [\\text{O}_2]^2$ dengan orde total reaksi sama dengan 3, karena orde reaksi kedua reaktan tertukar letaknya.",
            "$v = k [\\text{NO}]^2 [\\text{O}_2]^2$ dengan orde total reaksi sama dengan 4, dihitung dari koefisien reaksi kuadrat tanpa analisis data.",
            "$v = k [\\text{NO}]^0 [\\text{O}_2]^1$ dengan orde total reaksi sama dengan 1, dihitung dari asumsi reaksi berorde nol terhadap gas nitrogen monoksida."
        ],
        "formula": {
            "title": "PENENTUAN PERSAMAAN LAJU REAKSI",
            "latex": "\\frac{v_2}{v_1} = \\left(\\frac{[\\text{NO}]_2}{[\\text{NO}]_1}\\right)^x \\implies \\frac{4{,}8 \\times 10^{-3}}{1{,}2 \\times 10^{-3}} = \\left(\\frac{0{,}2}{0{,}1}\\right)^x \\implies 4 = 2^x \\implies x = 2; \\quad \\frac{v_3}{v_1} = \\left(\\frac{0{,}2}{0{,}1}\\right)^y = 2 \\implies y = 1",
            "legend": "• Orde terhadap $\\text{NO} = 2$<br>• Orde terhadap $\\text{O}_2 = 1$<br>• Persamaan laju: $v = k [\\text{NO}]^2 [\\text{O}_2]$<br>• Orde total $= 2 + 1 = 3$"
        },
        "hints": {
            "concept": "Bandingkan percobaan 1 & 2 untuk cari orde NO: (0,2/0,1)^x = 4,8e-3 / 1,2e-3 -> 2^x = 4 -> x = 2. Bandingkan percobaan 1 & 3 untuk cari orde O2: (0,2/0,1)^y = 2,4/1,2 -> 2^y = 2 -> y = 1.",
            "execution": "v = k [NO]^2 [O2], orde total = 3."
        }
    },
    {
        "id": "kim-lat-e-18",
        "materi": "KESETIMBANGAN KIMIA (Kc & Kp)",
        "topic": "Hubungan Tetapan Kesetimbangan Kc dan Kp",
        "stem": "Pada suhu $T = 500\\text{ K}$, reaksi penguraian dinitrogen tetroksida mencapai kesetimbangan menurut reaksi:<br>$$\\text{N}_2\\text{O}_4(g) \\rightleftharpoons 2\\,\\text{NO}_2(g)$$<br>Diketahui nilai tetapan kesetimbangan $K_c = 0{,}04\\text{ M}$ dan tetapan gas umum $R = 0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)}$. Nilai tetapan kesetimbangan tekanan ($K_p$) untuk reaksi tersebut pada suhu $500\\text{ K}$ adalah...",
        "correct": "$K_p = 1{,}64\\text{ atm}$, karena perubahan jumlah koefisien gas adalah $\\Delta n = \\Sigma n_{\\text{produk}} - \\Sigma n_{\\text{reaktan}} = 2 - 1 = 1$. Berdasarkan hubungan termodinamika antara $K_p$ dan $K_c$: $K_p = K_c (R T)^{\\Delta n} = 0{,}04 \\times (0{,}082 \\times 500)^1 = 0{,}04 \\times 41 = 1{,}64\\text{ atm}$.",
        "distractors": [
            "$K_p = 0{,}04\\text{ atm}$, karena keliru menganggap nilai Kp selalu sama dengan Kc tanpa memperhitungkan faktor RT.",
            "$K_p = 67{,}24\\text{ atm}$, dihitung dari pemangkatan kuadrat faktor suhu volume gas ideal.",
            "$K_p = 0{,}00098\\text{ atm}$, karena rumus hubungan tetapan keliru dibagi dengan faktor RT alih-alih dikalikan.",
            "$K_p = 3{,}28\\text{ atm}$, dihitung dari penggandaan nilai koefisien gas nitrogen dioksida."
        ],
        "formula": {
            "title": "HUBUNGAN Kc DAN Kp KESETIMBANGAN GAS",
            "latex": "K_p = K_c (R T)^{\\Delta n}; \\quad \\Delta n = 2 - 1 = 1; \\quad K_p = 0{,}04 \\times (0{,}082 \\times 500)^1 = 0{,}04 \\times 41 = 1{,}64\\text{ atm}",
            "legend": "• $\\Delta n = \\text{koefisien gas produk} - \\text{koefisien gas reaktan}$<br>• $R = 0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)}$<br>• $K_p = 1{,}64\\text{ atm}$"
        },
        "hints": {
            "concept": "Gunakan rumus Kp = Kc * (R * T)^Delta_n. Delta_n = 2 - 1 = 1. R * T = 0,082 * 500 = 41.",
            "execution": "Kp = 0,04 * 41^1 = 1,64 atm."
        }
    },
    {
        "id": "kim-lat-e-19",
        "materi": "KESETIMBANGAN KIMIA (LE CHATELIER)",
        "topic": "Pengaruh Suhu dan Tekanan terhadap Pergeseran Kesetimbangan",
        "stem": "Proses Haber-Bosch untuk sintesis amonia memenuhi persamaan kesetimbangan eksotermik berikut:<br>$$\\text{N}_2(g) + 3\\,\\text{H}_2(g) \\rightleftharpoons 2\\,\\text{NH}_3(g) \\quad \\Delta H = -92\\text{ kJ}$$<br>Untuk memaksimalkan produksi gas amonia ($\\text{NH}_3$) yang dihasilkan pada kesetimbangan, tindakan operasional yang paling tepat menurut Asas Le Chatelier adalah...",
        "correct": "Menaikkan tekanan sistem dan menurunkan suhu reaktor, karena penurunan suhu menggeser kesetimbangan ke arah reaksi eksoterm (kanan/produk), dan penaikan tekanan menggeser kesetimbangan ke arah jumlah mol gas yang lebih kecil (ruas kanan: 2 koefisien vs ruas kiri: 4 koefisien).",
        "distractors": [
            "Menaikkan suhu reaktor dan memperbesar volume bejana reaksi agar molekul gas memiliki energi kinetik lebih tinggi.",
            "Menurunkan tekanan sistem dan menambahkan gas amonia secara terus-menerus ke dalam ruang reaktor.",
            "Menambahkan katalisator besi (Fe) dalam jumlah sangat besar agar kesetimbangan bergeser ke ruas kanan.",
            "Menaikkan suhu reaktor dan menaikkan tekanan sistem secara serentak tanpa kondensasi amonia."
        ],
        "formula": {
            "title": "ASAS PERGESERAN KESETIMBANGAN LE CHATELIER",
            "latex": "\\text{Suhu } \\downarrow \\implies \\text{Geser ke Eksoterm (Kanan)}; \\quad P \\uparrow (V \\downarrow) \\implies \\text{Geser ke Koefisien Kecil (Kanan, 2 < 4)}",
            "legend": "• $\\Delta H = -92\\text{ kJ}$ (Eksoterm ke kanan)<br>• Jumlah koefisien gas kiri = $1 + 3 = 4$, kanan = 2<br>• Catatan: Katalisator hanya mempercepat laju pencapaian kesetimbangan, TIDAK menggeser posisi kesetimbangan"
        },
        "hints": {
            "concept": "Reaksi eksoterm (Delta H < 0) geser ke kanan jika suhu diturunkan. Koefisien kanan (2) < koefisien kiri (4), sehingga geser ke kanan jika tekanan dinaikkan.",
            "execution": "Pilihan tepat: Naikkan tekanan dan turunkan suhu."
        }
    },
    {
        "id": "kim-lat-e-20",
        "materi": "REAKSI REDOKS & BILANGAN OKSIDASI",
        "topic": "Penentuan Oksidator dan Reduktor pada Reaksi Redoks",
        "stem": "Perhatikan persamaan reaksi redoks berikut:<br>$$\\text{MnO}_2(s) + 4\\,\\text{HCl}(aq) \\to \\text{MnCl}_2(aq) + 2\\,\\text{H}_2\\text{O}(l) + \\text{Cl}_2(g)$$<br>Zat yang bertindak sebagai oksidator dan zat hasil reduksi dalam reaksi tersebut berturut-turut adalah...",
        "correct": "$\\text{MnO}_2$ bertindak sebagai oksidator dan $\\text{MnCl}_2$ adalah hasil reduksi, karena bilangan oksidasi mangan mengalami penurunan (reduksi) dari $+4$ pada $\\text{MnO}_2$ menjadi $+2$ pada $\\text{MnCl}_2$, sehingga zat yang mengalami reduksi ($\\text{MnO}_2$) bertindak sebagai agen pengoksidasi (oksidator).",
        "distractors": [
            "$\\text{HCl}$ bertindak sebagai oksidator dan $\\text{Cl}_2$ adalah hasil reduksi, karena klorin mengalami peningkatan bilangan oksidasi.",
            "$\\text{MnO}_2$ bertindak sebagai reduktor dan $\\text{MnCl}_2$ adalah hasil oksidasi, karena mangan melepaskan atom oksigen.",
            "$\\text{HCl}$ bertindak sebagai reduktor dan $\\text{H}_2\\text{O}$ adalah hasil reduksi molekul air murni.",
            "$\\text{Cl}_2$ bertindak sebagai oksidator dan $\\text{MnO}_2$ adalah zat pereaksi pengoksidasi sekunder."
        ],
        "formula": {
            "title": "BILANGAN OKSIDASI REAKSI REDOKS",
            "latex": "\\text{Mn: } +4 \\to +2 \\quad (\\text{Reduksi} \\implies \\text{MnO}_2 \\text{ Oksidator}, \\text{MnCl}_2 \\text{ Hasil Reduksi}); \\quad \\text{Cl: } -1 \\to 0 \\quad (\\text{Oksidasi} \\implies \\text{HCl Reduktor})"
        },
        "hints": {
            "concept": "Oksidator adalah zat yang mengalami reduksi (biloks turun). Reduktor adalah zat yang mengalami oksidasi (biloks naik).",
            "execution": "Biloks Mn pada MnO2 = +4, pada MnCl2 = +2 (turun = reduksi). Maka MnO2 = oksidator, MnCl2 = hasil reduksi."
        }
    },
    {
        "id": "kim-lat-e-21",
        "materi": "ELEKTROKIMIA (SEL VOLTA)",
        "topic": "Potensial Sel Standar dan Kespontanan Reaksi",
        "stem": "Diketahui potensial reduksi standar dari dua elektroda logam:<br>• $\\text{Zn}^{2+}(aq) + 2e^- \\to \\text{Zn}(s) \\quad E^\\circ = -0{,}76\\text{ Volt}$<br>• $\\text{Cu}^{2+}(aq) + 2e^- \\to \\text{Cu}(s) \\quad E^\\circ = +0{,}34\\text{ Volt}$<br>Jika kedua elektroda tersebut dirangkai menjadi sebuah sel Volta, logam yang berfungsi sebagai katoda dan nilai potensial sel standar ($E^\\circ_{\\text{sel}}$) yang dihasilkan adalah...",
        "correct": "Katoda adalah tembaga ($\\text{Cu}$) dan $E^\\circ_{\\text{sel}} = +1{,}10\\text{ Volt}$, karena tembaga memiliki potensial reduksi standar yang lebih positif ($+0{,}34\\text{ V} > -0{,}76\\text{ V}$) sehingga mengalami reaksi reduksi di katoda, sedangkan seng mengalami oksidasi di anoda. Potensial sel dihitung dari $E^\\circ_{\\text{sel}} = E^\\circ_{\\text{katoda}} - E^\\circ_{\\text{anoda}} = +0{,}34\\text{ V} - (-0{,}76\\text{ V}) = +1{,}10\\text{ Volt}$ (reaksi berlangsung spontan karena $E^\\circ_{\\text{sel}} > 0$).",
        "distractors": [
            "Katoda adalah seng ($\\text{Zn}$) dan $E^\\circ_{\\text{sel}} = +1{,}10\\text{ Volt}$, karena seng dianggap melepaskan elektron menuju katoda.",
            "Katoda adalah tembaga ($\\text{Cu}$) dan $E^\\circ_{\\text{sel}} = -0{,}42\\text{ Volt}$, karena potensial sel dihitung dari penjumlahan aljabar kedua potensial tanpa perubahan tanda anoda.",
            "Katoda adalah seng ($\\text{Zn}$) dan $E^\\circ_{\\text{sel}} = -1{,}10\\text{ Volt}$, karena susunan elektroda sel terbalik polaritas kutubnya.",
            "Katoda adalah tembaga ($\\text{Cu}$) dan $E^\\circ_{\\text{sel}} = +0{,}42\\text{ Volt}$, dihitung dari selisih nilai mutlak kedua elektroda logam."
        ],
        "formula": {
            "title": "POTENSIAL SEL VOLTA STANDAR",
            "latex": "E^\\circ_{\\text{sel}} = E^\\circ_{\\text{katoda}} - E^\\circ_{\\text{anoda}} = E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} - E^\\circ_{\\text{Zn}^{2+}/\\text{Zn}} = (+0{,}34) - (-0{,}76) = +1{,}10\\text{ V}",
            "legend": "• Katoda (Reduksi) = Elektroda dengan $E^\\circ$ lebih besar (Cu)<br>• Anoda (Oksidasi) = Elektroda dengan $E^\\circ$ lebih kecil (Zn)<br>• $E^\\circ_{\\text{sel}} = +1{,}10\\text{ V}$ (Spontan)"
        },
        "hints": {
            "concept": "Katoda = elektroda dengan E0 lebih positif (Cu, E0 = +0,34 V). Anoda = E0 lebih negatif (Zn, E0 = -0,76 V). E0_sel = E0_katoda - E0_anoda.",
            "execution": "E0_sel = 0,34 - (-0,76) = +1,10 V. Katoda = Cu."
        }
    },
    {
        "id": "kim-lat-e-22",
        "materi": "ELEKTROKIMIA (HUKUM FARADAY I)",
        "topic": "Massa Logam yang Diendapkan pada Katoda Elektrolisis",
        "stem": "Larutan tembaga(II) sulfat ($\\text{CuSO}_4$, $A_r\\,\\text{Cu} = 63{,}5$) dielektrolisis menggunakan elektroda karbon inert dengan mengalirkan arus listrik konstan $I = 10\\text{ Ampere}$ selama waktu $t = 965\\text{ sekon}$. Jika 1 Faraday = $96.500\\text{ C/mol elektron}$, massa tembaga padat yang terendapkan di katoda adalah...",
        "correct": "$3{,}175\\text{ gram}$, karena reaksi reduksi tembaga di katoda adalah $\\text{Cu}^{2+}(aq) + 2e^- \\to \\text{Cu}(s)$ sehingga valensi tembaga adalah $n = 2$ (massa ekuivalen $e = \\frac{A_r}{n} = \\frac{63{,}5}{2} = 31{,}75\\text{ g/mol}$). Berdasarkan Hukum Faraday I: $w = \\frac{e \\cdot I \\cdot t}{96.500} = \\frac{31{,}75 \\times 10 \\times 965}{96.500} = \\frac{31{,}75 \\times 9.650}{96.500} = \\frac{31{,}75}{10} = 3{,}175\\text{ gram}$.",
        "distractors": [
            "$6{,}350\\text{ gram}$, karena muatan kation tembaga keliru dianggap bervalensi satu ($n = 1$).",
            "$1{,}588\\text{ gram}$, dihitung dari anggapan tembaga melepaskan empat elektron pada reaksi reduksi katoda.",
            "$31{,}75\\text{ gram}$, karena waktu elektrolisis keliru dihitung selama 9.650 sekon penuh.",
            "$0{,}318\\text{ gram}$, karena galat pembagian nilai Faraday seratus ribu Coulomb."
        ],
        "formula": {
            "title": "HUKUM FARADAY I ELEKTROLISIS",
            "latex": "w = \\frac{e \\cdot I \\cdot t}{F} = \\frac{\\frac{A_r}{n} \\cdot I \\cdot t}{96.500} = \\frac{\\frac{63{,}5}{2} \\times 10 \\times 965}{96.500} = 3{,}175\\text{ gram}",
            "legend": "• $n = 2$ (muatan $\\text{Cu}^{2+}$)<br>• $I = 10\\text{ A}$, $t = 965\\text{ s}$<br>• Jumlah muatan $Q = 9.650\\text{ C} = 0{,}1\\text{ F}$<br>• Mol Cu $= 0{,}1 / 2 = 0{,}05\\text{ mol} \\implies m = 0{,}05 \\times 63{,}5 = 3{,}175\\text{ g}$"
        },
        "hints": {
            "concept": "Hukum Faraday I: w = (Ar / n) * (I * t / 96500). Untuk Cu2+, n = 2. Muatan Q = 10 * 965 = 9.650 C = 0,1 Faraday.",
            "execution": "w = (63,5 / 2) * (9.650 / 96.500) = 31,75 * 0,1 = 3,175 gram."
        }
    },
    {
        "id": "kim-lat-e-23",
        "materi": "KIMIA KARBON & SENYAWA ORGANIK",
        "topic": "Tata Nama IUPAC dan Isomer Alkohol",
        "stem": "Suatu senyawa karbon memiliki rumus molekul $\\text{C}_4\\text{H}_{10}\\text{O}$. Senyawa tersebut tidak dapat dioksidasi oleh larutan kalium dikromat ($\\text{K}_2\\text{Cr}_2\\text{O}_7$) dalam suasana asam. Nama IUPAC yang benar dari senyawa tersebut adalah...",
        "correct": "2-metil-2-propanol (atau ters-butanol), karena senyawa $\\text{C}_4\\text{H}_{10}\\text{O}$ yang tidak dapat dioksidasi oleh oksidator kuat adalah alkohol tersier, di mana atom karbon yang mengikat gugus hidroksil ($-\\text{OH}$) tidak lagi mengikat atom hidrogen bebas untuk mengalami pelepasan proton.",
        "distractors": [
            "1-butanol, karena merupakan alkohol primer yang dapat dioksidasi bertahap menjadi butanal dan asam butanoat.",
            "2-butanol, karena merupakan alkohol sekunder yang dapat dioksidasi menghasilkan keton butanon.",
            "Dietil eter, karena meskipun tidak bereaksi dengan dikromat, eter bukan merupakan turunan alkohol rantai cabang.",
            "2-metil-1-propanol, karena merupakan alkohol primer bercabang yang masih memiliki dua atom hidrogen alfa."
        ],
        "formula": {
            "title": "OKSIDASI GOLONGAN ALKOHOL",
            "latex": "\\text{Alkohol Primer} \\xrightarrow{[O]} \\text{Aldehida} \\xrightarrow{[O]} \\text{Asam Karboksilat}; \\quad \\text{Alkohol Sekunder} \\xrightarrow{[O]} \\text{Keton}; \\quad \\text{Alkohol Tersier} \\xrightarrow{[O]} \\text{Tidak Bereaksi}",
            "legend": "• 2-metil-2-propanol memiliki struktur $(\\text{CH}_3)_3\\text{C}-\\text{OH}$ (alkohol tersier)<br>• Ketiadaan hidrogen alfa ($-\\text{H}$) pada atom C karbinol mencegah terjadinya reaksi oksidasi"
        },
        "hints": {
            "concept": "Alkohol primer dapat dioksidasi jadi aldehida/asam karboksilat. Alkohol sekunder dioksidasi jadi keton. Alkohol tersier TIDAK dapat dioksidasi. Cari isomer alkohol tersier dari C4H10O.",
            "execution": "Isomer tersier C4H10O adalah 2-metil-2-propanol."
        }
    },
    {
        "id": "kim-lat-e-24",
        "materi": "REAKSI SENYAWA KARBON (ESTERIFIKASI)",
        "topic": "Reaksi Pembentukan Ester dari Asam Karboksilat dan Alkohol",
        "stem": "Asam asetat ($\\text{CH}_3\\text{COOH}$) direaksikan dengan etanol ($\\text{CH}_3\\text{CH}_2\\text{OH}$) dengan pemanasan dan penambahan beberapa tetes asam sulfat pekat ($\\text{H}_2\\text{SO}_4$) sebagai katalis. Nama senyawa ester yang dihasilkan dan aroma khas yang tercium adalah...",
        "correct": "Etil etanoat (etil asetat) dengan aroma harum buah apel/pisang, terbentuk melalui reaksi esterifikasi kondensasi di mana gugus $-\\text{OH}$ dari asam karboksilat berikatan dengan atom $-\\text{H}$ dari alkohol membentuk molekul sampingan air.",
        "distractors": [
            "Metil propanoat dengan aroma asam cuka yang menyengat dan menusuk hidung.",
            "Etil metanoat dengan aroma minyak tanah pelumas mesin industri.",
            "Propil asetat dengan aroma busuk belerang yang mudah menguap.",
            "Dietil eter dengan aroma obat bius kloroform di ruang operasi bedah."
        ],
        "formula": {
            "title": "REAKSI ESTERIFIKASI FISCHER",
            "latex": "\\text{CH}_3\\text{COOH} + \\text{CH}_3\\text{CH}_2\\text{OH} \\xlongequal{\\text{H}_2\\text{SO}_4, \\Delta} \\text{CH}_3\\text{COOCH}_2\\text{CH}_3 + \\text{H}_2\\text{O}",
            "legend": "• Asam etanoat + Etanol $\\to$ Etil etanoat (Etil asetat) + Air<br>• Asam sulfat pekat bertindak sebagai katalisator sekaligus zat higroskopis penarik air (dehidrator) untuk menggeser kesetimbangan ke kanan"
        },
        "hints": {
            "concept": "Asam asetat (CH3COOH) + etanol (CH3CH2OH) menghasilkan etil asetat (etil etanoat) dan air. Senyawa ester beraroma buah harum.",
            "execution": "Etil etanoat (etil asetat) dengan aroma buah."
        }
    },
    {
        "id": "kim-lat-e-25",
        "materi": "MAKROMOLEKUL (POLIMERISASI)",
        "topic": "Penggolongan Polimer Adisi dan Kondensasi",
        "stem": "Polimerisasi dapat dibedakan menjadi polimerisasi adisi dan polimerisasi kondensasi. Pasangan polimer berikut yang seluruhnya terbentuk melalui reaksi polimerisasi adisi adalah...",
        "correct": "Polietilena, polipropilena, dan polivinil klorida (PVC), karena ketiganya terbentuk dari monomer berikatan rangkap dua yang membuka ikatannya membentuk rantai panjang jenuh tanpa melepaskan molekul kecil sampingan.",
        "distractors": [
            "Nilon-6,6, dakron, dan protein, karena ketiganya merupakan polimer kondensasi yang melepaskan molekul air selama reaksi polimerisasi.",
            "Polietilena, nilon-6,6, dan teflon, karena nilon-6,6 terbentuk melalui polimerisasi kondensasi antara asam adipat dan heksametilendiamin.",
            "Bakelit, polistirena, dan selulosa, karena bakelit dan selulosa merupakan produk polimerisasi kondensasi.",
            "Karet alam, sutra wol, dan poliester, karena protein sutra wol merupakan polipeptida polimer kondensasi."
        ],
        "formula": {
            "title": "POLIMERISASI ADISI VS KONDENSASI",
            "latex": "\\text{Adisi: } n\\,(\\text{CH}_2=\\text{CH}-\\text{R}) \\to [-\\text{CH}_2-\\text{CH}(\\text{R})-]_n \\quad (\\text{Tanpa molekul sampingan}); \\quad \\text{Kondensasi: Monomer memiliki 2 gugus fungsi} \\to \\text{Polimer} + n\\,\\text{H}_2\\text{O}",
            "legend": "• Polimer Adisi: Polietilena (PE), Polipropilena (PP), Polivinil klorida (PVC), Teflon (PTFE), Polistirena (PS)<br>• Polimer Kondensasi: Nilon-6,6, Dakron (PET), Protein, Karbohidrat (Pati/Selulosa)"
        },
        "hints": {
            "concept": "Polimer adisi berasal dari monomer ikatan rangkap (membuka ikatan rangkap tanpa melepas molekul kecil): PE, PP, PVC, Teflon, Polistirena. Nilon, dakron, dan protein adalah polimer kondensasi.",
            "execution": "Polietilena, polipropilena, dan PVC."
        }
    }
]
