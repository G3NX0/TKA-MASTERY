# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Kimia (SMA/MA Saintek)
Dataset: Simulasi CBT HOTS (35 Authentic Questions, kim-sim-01 to 35)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
Composition:
  - 25 Authentic Single MCQ HOTS (kim-sim-01 to 25)
  - 5 Complex Multi-select HOTS (kim-sim-26 to 30)
  - 5 Matrix Benar-Salah HOTS (kim-sim-31 to 35)
"""

KIMIA_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 SINGLE MCQ HOTS (kim-sim-01 to kim-sim-25)
    # -------------------------------------------------------------
    {
        "id": "kim-sim-01",
        "materi": "TERMODINAMIKA & ENERGI KISI KRISTAL",
        "topic": "Siklus Born-Haber Pembentukan Natrium Klorida",
        "stem": "Dalam siklus Born-Haber untuk pembentukan kristal natrium klorida, $\\text{NaCl}(s)$, diketahui data termokimia standar berikut:<br>• Entalpi pembentukan standar: $\\Delta H_f^\\circ[\\text{NaCl}(s)] = -411\\text{ kJ/mol}$<br>• Entalpi sublimasi natrium: $\\Delta H_{\\text{sub}}[\\text{Na}(s)] = +108\\text{ kJ/mol}$<br>• Energi ionisasi pertama natrium: $IE_1[\\text{Na}(g)] = +496\\text{ kJ/mol}$<br>• Energi disosiasi ikatan klorin: $D[\\text{Cl}_2(g)] = +242\\text{ kJ/mol}$<br>• Afinitas elektron klorin: $EA[\\text{Cl}(g)] = -349\\text{ kJ/mol}$<br>Besarnya energi kisi ($U_{\\text{kisi}}$) kristal $\\text{NaCl}(s)$ yang didefinisikan sebagai perubahan entalpi pada reaksi: $\\text{Na}^+(g) + \\text{Cl}^-(g) \\rightarrow \\text{NaCl}(s)$ adalah...",
        "correct": "$U_{\\text{kisi}} = -787\\text{ kJ/mol}$, karena menurut Hukum Hess pada siklus Born-Haber, $\\Delta H_f^\\circ = \\Delta H_{\\text{sub}} + IE_1 + \\frac{1}{2}D(\\text{Cl}_2) + EA + U_{\\text{kisi}}$. Maka $-411 = +108 + 496 + \\frac{1}{2}(242) + (-349) + U_{\\text{kisi}} = 108 + 496 + 121 - 349 + U_{\\text{kisi}} = +376 + U_{\\text{kisi}}$, sehingga $U_{\\text{kisi}} = -411 - 376 = -787\\text{ kJ/mol}$.",
        "distractors": [
            "$U_{\\text{kisi}} = -908\\text{ kJ/mol}$, akibat lupa mengalikan disosiasi ikatan gas klorin dengan koefisien setengah pada pembentukan satu mol atom Cl.",
            "$U_{\\text{kisi}} = -438\\text{ kJ/mol}$, dihitung dengan memperlakukan nilai afinitas elektron klorin sebagai proses endotermik bertanda positif.",
            "$U_{\\text{kisi}} = +787\\text{ kJ/mol}$, karena salah mendefinisikan pembentukan kisi kristal dari ion gas sebagai pemutusan kisi ionik menjadi gas.",
            "$U_{\\text{kisi}} = -666\\text{ kJ/mol}$, akibat salah mengurangkan energi ionisasi natrium dari nilai entalpi pembentukan kristal."
        ],
        "formula": {
            "title": "SIKLUS BORN-HABER PEMBENTUKAN KRISTAL IONIK",
            "latex": "\\Delta H_f^\\circ = \\Delta H_{\\text{sub}} + IE_1 + \\frac{1}{2}D_{\\text{Cl-Cl}} + EA + U_{\\text{kisi}} \\implies U_{\\text{kisi}} = -411 - (108 + 496 + 121 - 349) = -787\\text{ kJ/mol}",
            "legend": "• Entalpi pembentukan kristal $\\Delta H_f^\\circ = -411\\text{ kJ/mol}$<br>• Atomisasi gas Cl: $\\frac{1}{2} D = +121\\text{ kJ/mol}$<br>• Jumlah tahap endoterm-eksoterm gas = $+376\\text{ kJ/mol}$<br>• Energi kisi eksotermik pembentukan = $-787\\text{ kJ/mol}$"
        },
        "hints": {
            "concept": "Gunakan Hukum Hess pada siklus Born-Haber: Delta Hf = Delta Hsub + IE1 + 0.5*D(Cl2) + EA + U_kisi. Perhatikan bahwa hanya dibutuhkan 1 mol atom Cl(g), jadi disosiasi Cl2 dikalikan 1/2.",
            "execution": "Jumlahkan: 108 + 496 + 121 - 349 = 376 kJ/mol. Maka U_kisi = -411 - 376 = -787 kJ/mol."
        }
    },
    {
        "id": "kim-sim-02",
        "materi": "KINETIKA KIMIA & MEKANISME REAKSI",
        "topic": "Pendekatan Keadaan Tunak (Steady-State Approximation) Dekomposisi Ozon",
        "stem": "Dekomposisi gas ozon di stratosfer dihancurkan melalui mekanisme dua tahap:<br>Tahap 1 (cepat, bolak-balik): $\\text{O}_3(g) \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} \\text{O}_2(g) + \\text{O}(g)$<br>Tahap 2 (lambat): $\\text{O}_3(g) + \\text{O}(g) \\xrightarrow{k_2} 2\\text{O}_2(g)$<br>Dengan menerapkan pendekatan keadaan tunak ($\\textit{steady-state approximation}$) pada spesi radikal oksigen intermediet $[\\text{O}]$, hukum laju pembentukan gas $\\text{O}_2$ atau laju penguraian gas $\\text{O}_3$ ($r = -\\frac{d[\\text{O}_3]}{dt}$) dinyatakan oleh persamaan...",
        "correct": "$r = \\frac{2 k_1 k_2 [\\text{O}_3]^2}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$, karena pada keadaan tunak laju pembentukan radikal $[\\text{O}]$ sama dengan laju konsumsinya: $\\frac{d[\\text{O}]}{dt} = k_1 [\\text{O}_3] - k_{-1} [\\text{O}_2][\\text{O}] - k_2 [\\text{O}_3][\\text{O}] = 0 \\implies [\\text{O}] = \\frac{k_1 [\\text{O}_3]}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$. Substitusi ke laju penguraian netral: $-\\frac{d[\\text{O}_3]}{dt} = k_1 [\\text{O}_3] - k_{-1}[\\text{O}_2][\\text{O}] + k_2[\\text{O}_3][\\text{O}] = 2 k_2 [\\text{O}_3][\\text{O}] = \\frac{2 k_1 k_2 [\\text{O}_3]^2}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$.",
        "distractors": [
            "$r = k_2 [\\text{O}_3][\\text{O}_2]$, karena mengabaikan kesetimbangan tahap pertama dan hanya menuliskan perkalian konsentrasi produk stabil.",
            "$r = \\frac{k_1 [\\text{O}_3]}{k_{-1} [\\text{O}_2]}$, yang hanya merupakan ungkapan tetapan kesetimbangan parsial konsentrasi tahap pertama.",
            "$r = k_1 k_2 [\\text{O}_3]^2 [\\text{O}_2]^{-2}$, akibat salah mengkuadratkan ketergantungan balik gas oksigen.",
            "$r = 2 k_2 [\\text{O}_3]^2$, yang mengasumsikan radikal oksigen terbentuk secara stoikiometrik tanpa reaksi balik dengan oksigen molekuler."
        ],
        "formula": {
            "title": "STEADY-STATE APPROXIMATION DEKOMPOSISI OZON",
            "latex": "\\frac{d[\\text{O}]}{dt} = 0 \\implies [\\text{O}] = \\frac{k_1 [\\text{O}_3]}{k_{-1}[\\text{O}_2] + k_2[\\text{O}_3]}; \\quad r = 2 k_2 [\\text{O}_3][\\text{O}] = \\frac{2 k_1 k_2 [\\text{O}_3]^2}{k_{-1}[\\text{O}_2] + k_2[\\text{O}_3]}",
            "legend": "• Intermediet $[\\text{O}]$ tidak boleh muncul dalam persamaan laju akhir<br>• Jika $k_{-1}[\\text{O}_2] \\gg k_2[\\text{O}_3]$, laju tereduksi menjadi $r \\approx k' \\frac{[\\text{O}_3]^2}{[\\text{O}_2]}$ (orde -1 terhadap $\\text{O}_2$)<br>• Menjelaskan mengapa keberadaan oksigen menghambat laju perusakan ozon"
        },
        "hints": {
            "concept": "Pada steady-state: d[O]/dt = 0, sehingga laju pembentukan O pada tahap 1 sama dengan laju reaksi balik tahap 1 ditambah laju konsumsi pada tahap 2.",
            "execution": "Dapatkan [O] = k1[O3] / (k-1[O2] + k2[O3]), lalu substitusikan ke laju konsumsi O3 yaitu 2*k2*[O3]*[O]."
        }
    },
    {
        "id": "kim-sim-03",
        "materi": "KESETIMBANGAN KIMIA INDUSTRI",
        "topic": "Optimalisasi Sintesis Amonia Proses Haber-Bosch",
        "stem": "Sintesis amonia industri berlangsung menurut reaksi eksotermik:<br>$\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g) \\quad \\Delta H^\\circ = -92\\text{ kJ/mol}$<br>Dalam reaktor industri modern, reaksi dioperasikan pada suhu kompromi sekitar $450^\\circ\\text{C}$ dan tekanan tinggi $200\\text{ atm}$ dengan katalis besi terpromosi ($\alpha\\text{-Fe}$ dengan $\\text{K}_2\\text{O}$ dan $\\text{Al}_2\\text{O}_3$). Alasan ilmiah utama mengapa tidak digunakan suhu kamar ($25^\\circ\\text{C}$) meskipun secara termodinamika nilai $K_p$ jauh lebih besar pada suhu rendah adalah...",
        "correct": "Energi aktivasi pemutusan ikatan kovalen rangkap tiga $\\text{N}\\equiv\\text{N}$ ($945\\text{ kJ/mol}$) sangat tinggi sehingga pada suhu rendah laju reaksi praktis nol (kinetika sangat lambat); suhu $450^\\circ\\text{C}$ merupakan kompromi antara laju reaksi yang cukup cepat mencapai kesetimbangan dan perolehan yield yang memadai pada tekanan $200\\text{ atm}$.",
        "distractors": [
            "Pada suhu kamar reaksi bersifat endotermik sehingga membutuhkan pasokan kalor kontinu yang sangat mahal untuk menggerakkan turbin kompresor.",
            "Gas amonia yang terbentuk pada suhu kamar akan langsung terkondensasi dan menyumbat pori-pori katalis besi secara permanen.",
            "Molekul nitrogen akan mengalami disosiasi total menjadi ion radikal bebas yang merusak dinding bejana baja reaktor pada suhu rendah.",
            "Katalis besi baru mulai meleleh dan aktif mengikat gas hidrogen pada suhu di atas $600^\\circ\\text{C}$ sehingga suhu kamar tidak fungsional."
        ],
        "formula": {
            "title": "PRINSIP KOMPROMI TERMODINAMIKA VS KINETIKA INDUSTRI",
            "latex": "\\Delta n_g = 2 - (1+3) = -2 < 0; \\quad \\Delta H < 0 \\implies K_p \\downarrow \\text{ jika } T \\uparrow; \\quad k = A e^{-E_a/RT} \\uparrow \\text{ jika } T \\uparrow",
            "legend": "• Termodinamika: Suhu rendah menaikkan nilai tetapan $K_p$, namun...<br>• Kinetika: Energi ikatan $N\\equiv N = 945\\text{ kJ/mol}$ menuntut suhu operasi tinggi agar laju reaksi komersial tercapai<br>• Tekanan tinggi ($200\\text{ atm}$) menggeser kesetimbangan ke arah produk (mol gas lebih sedikit)"
        },
        "hints": {
            "concept": "Pertimbangkan pertentangan antara termodinamika (yield) dan kinetika (kecepatan). Ikatan rangkap tiga N≡N sangat kuat (945 kJ/mol).",
            "execution": "Tanpa suhu yang cukup tinggi, tumbukan efektif partikel tidak mampu melampaui energi aktivasi, sehingga reaksi memakan waktu bertahun-tahun."
        }
    },
    {
        "id": "kim-sim-04",
        "materi": "LARUTAN ASAM-BASA POLIPROTIK",
        "topic": "Kurva Titrasi Asam Fosfat dan Identifikasi Spesi Dominan",
        "stem": "Sebanyak $25{,}0\\text{ mL}$ larutan asam ortofosfat, $\\text{H}_3\\text{PO}_4$ $0{,}10\\text{ M}$ ($K_{a1} = 7{,}5 \\times 10^{-3}$, $K_{a2} = 6{,}2 \\times 10^{-8}$, $K_{a3} = 4{,}2 \\times 10^{-13}$) dititrasi dengan larutan baku $\\text{NaOH}$ $0{,}10\\text{ M}$. Pada saat penambahan volume titran $\\text{NaOH}$ tepat mencapai $37{,}5\\text{ mL}$ (antara titik ekuivalen pertama $25\\text{ mL}$ dan kedua $50\\text{ mL}$), spesi ion fosfat yang dominan di dalam larutan dan nilai $pH$ larutan adalah...",
        "correct": "Spesi dominan berupa campuran ekivalen $[\\text{H}_2\\text{PO}_4^-] = [\\text{HPO}_4^{2-}]$ dengan $pH = 7{,}21$, karena $25\\text{ mL}$ pertama $\\text{NaOH}$ telah sempurna mengubah $\\text{H}_3\\text{PO}_4$ menjadi $\\text{H}_2\\text{PO}_4^-$, dan penambahan $12{,}5\\text{ mL}$ berikutnya tepat menetralkan separuh mol $\\text{H}_2\\text{PO}_4^-$ membentuk buffer equimolar dengan $pH = pK_{a2} = -\\log(6{,}2 \\times 10^{-8}) = 7{,}21$.",
        "distractors": [
            "Spesi dominan berupa ion $\\text{PO}_4^{3-}$ dengan $pH = 12{,}38$, karena titran basa kuat telah ditambahkan berlebih melampaui volume asam awal.",
            "Spesi dominan berupa molekul $\\text{H}_3\\text{PO}_4$ tak terdisosiasi dengan $pH = 2{,}12$, karena asam fosfat merupakan asam lemah bertingkat tiga.",
            "Spesi dominan berupa ion amfiprotik tunggal $\\text{H}_2\\text{PO}_4^-$ dengan $pH = 4{,}67$, dihitung dari rata-rata akar tetapan disosiasi pertama dan kedua.",
            "Spesi dominan berupa endapan garam natrium fosfat netral dengan $pH = 7{,}00$ tepat seperti titrasi asam-basa kuat."
        ],
        "formula": {
            "title": "TITRASI ASAM POLIPROTIK & BUFFER BUFFERING HALF-WAY",
            "latex": "\\text{Pada } V = 37{,}5\\text{ mL}: \\quad n_{\\text{H}_2\\text{PO}_4^-} = n_{\\text{HPO}_4^{2-}} \\implies pH = pK_{a2} + \\log\\frac{[\\text{HPO}_4^{2-}]}{[\\text{H}_2\\text{PO}_4^-]} = pK_{a2} = 7{,}21",
            "legend": "• Titik ekuivalen 1: $V = 25\\text{ mL}$ (spesi dominan $\\text{H}_2\\text{PO}_4^-$, $pH = \\frac{pK_{a1}+pK_{a2}}{2} = 4{,}67$)<br>• Setengah TE 2: $V = 37{,}5\\text{ mL}$ (sistem buffer fosfat, $pH = pK_{a2} = 7{,}21$)<br>• Titik ekuivalen 2: $V = 50\\text{ mL}$ (spesi dominan $\\text{HPO}_4^{2-}$, $pH = \\frac{pK_{a2}+pK_{a3}}{2} = 9{,}79$)"
        },
        "hints": {
            "concept": "V = 37.5 mL berada tepat di tengah-tengah antara TE 1 (25 mL) dan TE 2 (50 mL). Ini adalah titik setengah netralisasi tahap kedua, di mana [H2PO4-] = [HPO4(2-)].",
            "execution": "Berdasarkan persamaan Henderson-Hasselbalch tahap 2: pH = pKa2 + log(1) = -log(6,2 x 10^-8) = 7,21."
        }
    },
    {
        "id": "kim-sim-05",
        "materi": "LARUTAN PENYANGGA BIOLOGIS",
        "topic": "Kapasitas Buffer Darah Karbonat pada Asidosis Metabolik",
        "stem": "Dalam plasma darah manusia, sistem penyangga utama dipertahankan oleh kesetimbangan asam karbonat–bikarbonat:<br>$\\text{CO}_2(d) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{H}_2\\text{CO}_3(aq) \\rightleftharpoons \\text{H}^+(aq) + \\text{HCO}_3^-(aq) \\quad (pK_a' = 6{,}10)$<br>Pada kondisi fisiologis normal, darah memiliki $pH = 7{,}40$. Jika seorang atlet mengalami penumpukan asam laktat akibat aktivitas anaerobik hebat sehingga konsentrasi $[\\text{HCO}_3^-]$ turun dari $24\\text{ mM}$ menjadi $12\\text{ mM}$ sementara $[\\text{CO}_2]$ terlarut dipertahankan konstan oleh hiperventilasi paru-paru pada $1{,}2\\text{ mM}$, nilai $pH$ darah atlet tersebut berubah menjadi...",
        "correct": "$pH = 7{,}10$ (mengalami asidosis metabolik terkompensasi parsial), karena menurut persamaan Henderson-Hasselbalch klinis: $pH = pK_a' + \\log\\frac{[\\text{HCO}_3^-]}{[\\text{CO}_2]} = 6{,}10 + \\log\\frac{12}{1{,}2} = 6{,}10 + \\log(10) = 6{,}10 + 1{,}00 = 7{,}10$.",
        "distractors": [
            "$pH = 6{,}70$, akibat salah mengurangkan nilai logaritma dari nilai pKa sistem buffer.",
            "$pH = 7{,}40$, karena menganggap sistem penyangga mampu meniadakan 100% perubahan asam laktat tanpa pergeseran rasio ion sama sekali.",
            "$pH = 7{,}70$, dihitung dengan membalik perbandingan konsentrasi asam terlarut terhadap basa konjugasi.",
            "$pH = 6{,}10$, karena mengira seluruh bikarbonat habis bereaksi sehingga pH sama persis dengan nilai pKa murni."
        ],
        "formula": {
            "title": "PERSAMAAN HENDERSON-HASSELBALCH BUFFER DARAH",
            "latex": "pH = pK_a' + \\log\\frac{[\\text{HCO}_3^-]}{[\\text{CO}_2]} = 6{,}10 + \\log\\left(\\frac{12\\text{ mM}}{1{,}2\\text{ mM}}\\right) = 6{,}10 + 1{,}00 = 7{,}10",
            "legend": "• Normal: $pH = 6{,}10 + \\log(24/1{,}2) = 6{,}10 + 1{,}30 = 7{,}40$<br>• Penurunan $[\\text{HCO}_3^-]$ menjadi $12\\text{ mM}$ menghasilkan rasio $10:1$<br>• $pH$ turun menjadi $7{,}10$ (gejala asidosis metabolik)"
        },
        "hints": {
            "concept": "Gunakan persamaan Henderson-Hasselbalch klinis: pH = pKa' + log([HCO3-] / [CO2]). Masukkan konsentrasi akhir.",
            "execution": "pH = 6,10 + log(12 / 1,2) = 6,10 + log(10) = 6,10 + 1,00 = 7,10."
        }
    },
    {
        "id": "kim-sim-06",
        "materi": "KELARUTAN & PENGENDAPAN FRAKSIONAL",
        "topic": "Pemisahan Selektif Kation Sulfida Golongan II dan III dengan Kontrol pH",
        "stem": "Suatu larutan mengandung campuran ion logam $\\text{Cu}^{2+}$ $0{,}01\\text{ M}$ dan ion logam $\\text{Zn}^{2+}$ $0{,}01\\text{ M}$. Ke dalam larutan dialirkan gas hidrogen sulfida, $\\text{H}_2\\text{S}$, hingga jenuh ($[\\text{H}_2\\text{S}] = 0{,}10\\text{ M}$). Diketahui data kesetimbangan:<br>• $\\text{H}_2\\text{S} \\rightleftharpoons 2\\text{H}^+ + \\text{S}^{2-} \\quad (K_{a1}K_{a2} = 1{,}0 \\times 10^{-20})$<br>• $K_{sp}[\\text{CuS}] = 6{,}0 \\times 10^{-36}$<br>• $K_{sp}[\\text{ZnS}] = 2{,}0 \\times 10^{-22}$<br>Agar ion $\\text{Cu}^{2+}$ mengendap sempurna sebagai $\\text{CuS}$ sedangkan ion $\\text{Zn}^{2+}$ tetap larut seutuhnya tanpa mengendap sebagai $\\text{ZnS}$, konsentrasi ion $[\\text{H}^+]$ larutan harus diatur pada batas...",
        "correct": "$[\\text{H}^+] > 7{,}07 \\times 10^{-1}\\text{ M}$ (atau $pH < 0{,}15$), karena agar $\\text{ZnS}$ tidak mengendap, syaratnya $Q_{sp}[\\text{ZnS}] = [\\text{Zn}^{2+}][\\text{S}^{2-}] < K_{sp}[\\text{ZnS}] \\implies [\\text{S}^{2-}] < \\frac{2{,}0 \\times 10^{-22}}{0{,}01} = 2{,}0 \\times 10^{-20}\\text{ M}$. Dari kesetimbangan disosiasi asam sulfida: $[\\text{S}^{2-}] = \\frac{K_{a1}K_{a2}[\\text{H}_2\\text{S}]}{[\\text{H}^+]^2} = \\frac{10^{-20} \\times 0{,}10}{[\\text{H}^+]^2} = \\frac{10^{-21}}{[\\text{H}^+]^2}$. Syarat tak mengendap: $\\frac{10^{-21}}{[\\text{H}^+]^2} < 2{,}0 \\times 10^{-20} \\implies [\\text{H}^+]^2 > 0{,}05 \\implies [\\text{H}^+] > 0{,}22\\text{ M}$. Sementara pada kondisi ini $[\\text{S}^{2-}] \\approx 10^{-20}\\text{ M}$ jauh melampaui $K_{sp}[\\text{CuS}]$ ($Q_{sp} = 10^{-22} \\gg 6 \\times 10^{-36}$) sehingga $\\text{CuS}$ mengendap tuntas.",
        "distractors": [
            "$[\\text{H}^+] < 10^{-7}\\text{ M}$ ($pH > 7$), karena pada kondisi basa kedua ion akan mengendap bersamaan sehingga pemisahan gagal total.",
            "$[\\text{H}^+] = 10^{-14}\\text{ M}$, di mana konsentrasi ion sulfida menjadi maksimum dan seluruh kation membentuk hidroksida dan sulfida sekaligus.",
            "$[\\text{H}^+] < 10^{-4}\\text{ M}$, karena konsentrasi sulfida bebas akan terlalu besar dan memicu kopresipitasi seng sulfida.",
            "$[\\text{H}^+] = 10^{-10}\\text{ M}$, karena larutan asam kuat tidak mampu mendisosiasikan tembaga sulfida."
        ],
        "formula": {
            "title": "PENGENDAPAN SELEKTIF SULFIDA DENGAN KONTROL PH",
            "latex": "[\\text{S}^{2-}]_{\\max} = \\frac{K_{sp}[\\text{ZnS}]}{[\\text{Zn}^{2+}]} = \\frac{2 \\times 10^{-22}}{10^{-2}} = 2 \\times 10^{-20}\\text{ M}; \\quad [\\text{H}^+] = \\sqrt{\\frac{K_{a1}K_{a2}[\\text{H}_2\\text{S}]}{[\\text{S}^{2-}]_{\\max}}} > 0{,}22\\text{ M}",
            "legend": "• Suasana sangat asam ($pH < 0{,}66$) menekan konsentrasi $[\\text{S}^{2-}]$ sangat rendah<br>• $[\\text{S}^{2-}]$ cukup untuk melampaui $K_{sp}$ $\\text{CuS}$ yang super kecil ($10^{-36}$)<br>• $[\\text{S}^{2-}]$ tidak cukup untuk melampaui $K_{sp}$ $\\text{ZnS}$ ($10^{-22}$), sehingga $\\text{Zn}^{2+}$ lolos dalam filtrat"
        },
        "hints": {
            "concept": "Hitung [S(2-)] maksimum agar ZnS tidak mengendap: [S(2-)] < Ksp(ZnS)/[Zn2+]. Lalu hubungkan dengan kesetimbangan asam H2S: [S2-] = (Ka1Ka2 * [H2S]) / [H+]^2.",
            "execution": "[S2-] < 2 x 10^-20 M. Maka [H+]^2 > (10^-20 * 0,1) / (2 x 10^-20) = 0,05 -> [H+] > 0,22 M (suasana asam pekat, pH rendah)."
        }
    },
    {
        "id": "kim-sim-07",
        "materi": "SIFAT KOLIGATIF & TEORI ELEKTROLIT NYATA",
        "topic": "Penyimpangan Faktor Van 't Hoff Larutan Elektrolit Encer",
        "stem": "Pengukuran eksperimen penurunan titik beku dari larutan magnesium sulfat, $\\text{MgSO}_4$, dengan konsentrasi $0{,}05\\text{ m}$ dalam pelarut air murni ($K_f = 1{,}86^\\circ\\text{C/m}$) memberikan nilai $\\Delta T_f = 0{,}130^\\circ\\text{C}$. Padahal, secara stoikiometri garam $\\text{MgSO}_4$ terurai menjadi dua ion ($\\text{Mg}^{2+}$ dan $\\text{SO}_4^{2-}$, $n = 2$). Derajat disosiasi semu (faktor van 't Hoff eksperimen $i$) dan penjelasan fenomena termodinamika tersebut adalah...",
        "correct": "$i_{\\text{eksp}} = 1{,}40$; nilai $i < 2$ disebabkan oleh pembentukan pasangan ion ($\\textit{ion-pairing}$) antarion bivalen bermuatan tinggi ($\\text{Mg}^{2+}$ dan $\\text{SO}_4^{2-}$) akibat gaya tarik elektrostatik antarion menurut teori Debye-Hückel sehingga jumlah partikel kinetik bebas berkurang.",
        "distractors": [
            "$i_{\\text{eksp}} = 2{,}00$; garam magnesium sulfat selalu terdisosiasi sempurna 100% tanpa adanya interaksi elektrostatik ionik dalam air.",
            "$i_{\\text{eksp}} = 0{,}70$; ion magnesium mengalami polimerisasi kovalen membentuk rantai makromolekul padat dalam larutan encer.",
            "$i_{\\text{eksp}} = 2{,}80$; terjadi hidrolisis total yang menghasilkan tambahan ion hidrogen dan hidroksida berlipat ganda dalam air.",
            "$i_{\\text{eksp}} = 1{,}00$; magnesium sulfat tidak larut dalam air sehingga berperilaku seperti senyawa non-elektrolit murni."
        ],
        "formula": {
            "title": "FAKTOR VAN 'T HOFF EKSPERIMEN & ION-PAIRING",
            "latex": "\\Delta T_f = m \\cdot K_f \\cdot i \\implies i_{\\text{eksp}} = \\frac{\\Delta T_f}{m \\cdot K_f} = \\frac{0{,}130}{0{,}05 \\times 1,86} = \\frac{0{,}130}{0{,}093} \\approx 1{,}40",
            "legend": "• Untuk elektrolit bivalen ($2+$ dan $2-$), gaya Coulomb antarion $\\propto q_1 q_2 = 4$ kali lebih kuat dibanding elektrolit univalen ($1+$ dan $1-$)<br>• Terjadi asosiasi sementara membentuk pasangan ion netral $[\\text{Mg}^{2+}\\text{SO}_4^{2-}]^0$<br>• Partikel efektif terukur $i = 1{,}40 < 2{,}00$"
        },
        "hints": {
            "concept": "Hitung faktor van 't Hoff dari data penurunan titik beku terukur: i = Delta Tf / (m * Kf). Pahami interaksi Debye-Huckel untuk ion bermuatan ganda.",
            "execution": "i = 0,130 / (0,05 * 1,86) = 0,130 / 0,093 = 1,40. Kation Mg(2+) dan anion SO4(2-) saling berpasangan (ion pair)."
        }
    },
    {
        "id": "kim-sim-08",
        "materi": "ELEKTROKIMIA & BATERAI SEKUNDER",
        "topic": "Reaksi Interkalasi Baterai Ion Litium (Li-ion Battery)",
        "stem": "Baterai sekunder ion litium yang digunakan pada ponsel pintar dan kendaraan listrik bekerja berdasarkan mekanisme interkalasi ion $\\text{Li}^+$ bolak-balik antara anoda grafit ($\\text{Li}_x\\text{C}_6$) dan katoda oksida kobalt litium ($\\text{Li}_{1-x}\\text{CoO}_2$). Selama proses pengosongan baterai ($\\textit{discharge}$), proses kimia yang terjadi di anoda dan katoda adalah...",
        "correct": "Di anoda terjadi oksidasi de-interkalasi ion $\\text{Li}^+$ dari kisi grafit ($\\text{Li}_x\\text{C}_6 \\rightarrow 6\\text{C} + x\\text{Li}^+ + x e^-$), dan di katoda terjadi reduksi kobalt disertai interkalasi ion $\\text{Li}^+$ ke dalam matriks kristal oksida kobalt ($\\text{Li}_{1-x}\\text{CoO}_2 + x\\text{Li}^+ + x e^- \\rightarrow \\text{LiCoO}_2$).",
        "distractors": [
            "Di anoda terjadi reduksi logam litium cair menjadi endapan litium oksida pejal yang menyerap elektron dari sirkuit luar.",
            "Di katoda terjadi dekomposisi elektrolit organik menjadi gas hidrogen dan gas oksigen bertekanan tinggi.",
            "Ion litium mengalami perubahan bilangan oksidasi dari $+1$ menjadi ion trivalen $+3$ di kedua kutub elektroda.",
            "Di anoda terjadi pengendapan kristal garam litium karbonat padat yang mengisolasi aliran arus listrik secara permanen."
        ],
        "formula": {
            "title": "REAKSI DISCHARGE BATERAI LITIUM-ION",
            "latex": "\\text{Anoda: } \\text{Li}_x\\text{C}_6 \\rightarrow 6\\text{C} + x\\text{Li}^+ + x e^-; \\quad \\text{Katoda: } \\text{Li}_{1-x}\\text{CoO}_2 + x\\text{Li}^+ + x e^- \\rightarrow \\text{LiCoO}_2",
            "legend": "• Reaksi total pelepasan muatan: $\\text{Li}_x\\text{C}_6 + \\text{Li}_{1-x}\\text{CoO}_2 \\rightarrow 6\\text{C} + \\text{LiCoO}_2$<br>• Ion $\\text{Li}^+$ bermigrasi melalui elektrolit dari anoda ke katoda<br>• Elektron mengalir melalui kawat luar menyediakan daya listrik bagi beban"
        },
        "hints": {
            "concept": "Pada discharge (berfungsi sebagai sel volta): anoda mengalami oksidasi (melepas elektron dan ion Li+ keluar dari grafit), katoda mengalami reduksi (menerima ion Li+ dan elektron).",
            "execution": "Anoda: LixC6 -> 6C + xLi+ + x e-. Katoda: Li(1-x)CoO2 + xLi+ + x e- -> LiCoO2."
        }
    },
    {
        "id": "kim-sim-09",
        "materi": "ELEKTROLISIS INDUSTRI METALURGI",
        "topic": "Proses Hall-Héroult Ekstraksi Aluminium dari Bauksit",
        "stem": "Dalam ekstraksi komersial logam aluminium melalui proses Hall-Héroult, alumina ($\\text{Al}_2\\text{O}_3$) dilarutkan dalam lelehan kriolit cair ($\\text{Na}_3\\text{AlF}_6$) pada suhu sekitar $950^\\circ\\text{C}$ dan dielektrolisis menggunakan anoda karbon (grafit). Peran krusial penambahan lelehan kriolit serta fenomena kimia yang menyebabkan anoda karbon harus diganti secara berkala adalah...",
        "correct": "Kriolit berfungsi menurunkan titik leleh alumina dari $\\sim 2050^\\circ\\text{C}$ menjadi $\\sim 950^\\circ\\text{C}$ dan meningkatkan konduktivitas listrik; anoda karbon habis bereaksi karena gas oksigen yang dihasilkan pada anoda bereaksi dengan karbon membentuk gas $\\text{CO}_2$ pada suhu tinggi ($C(s) + O_2(g) \\rightarrow CO_2(g)$).",
        "distractors": [
            "Kriolit bertindak sebagai zat pengoksidasi kuat ion aluminium; anoda karbon aus akibat terkorosi oleh asam sulfat pekat yang dihasilkan reaksi.",
            "Kriolit mencegah pembentukan gas fluorin beracun; anoda karbon meleleh karena suhu busur listrik melampaui $4000^\\circ\\text{C}$.",
            "Kriolit menyerap gas karbon dioksida di katoda; anoda karbon menyublim secara spontan menjadi intan kristalin.",
            "Kriolit berfungsi sebagai sumber ion natrium logam pengganti; anoda karbon hancur akibat gesekan mekanik aliran lelehan logam cair."
        ],
        "formula": {
            "title": "REAKSI ELEKTROLISIS PROSES HALL-HÉROULT",
            "latex": "\\text{Katoda: } \\text{Al}^{3+} + 3e^- \\rightarrow \\text{Al}(l); \\quad \\text{Anoda: } 2\\text{O}^{2-} + \\text{C}(s) \\rightarrow \\text{CO}_2(g) + 4e^-",
            "legend": "• Reaksi netto: $2\\text{Al}_2\\text{O}_3 + 3\\text{C}(s) \\xrightarrow{\\text{kriolit, } 950^\\circ\\text{C}} 4\\text{Al}(l) + 3\\text{CO}_2(g)$<br>• Kriolit ($\text{Na}_3\\text{AlF}_6$) menghemat konsumsi energi termal pabrik secara masif<br>• Karbon anoda dikonsumsi secara stoikiometris membentuk $\\text{CO}_2$"
        },
        "hints": {
            "concept": "Titik leleh Al2O3 murni sangat tinggi (>2000 C). Kriolit menurunkannya ke ~950 C. Di anoda, ion oksida dioksidasi menghasilkan O2 yang langsung membakar karbon anoda menjadi CO2.",
            "execution": "Pilih opsi yang menjelaskan peran penurunan titik leleh oleh kriolit dan oksidasi anoda karbon menjadi CO2."
        }
    },
    {
        "id": "kim-sim-10",
        "materi": "KIMIA UNSUR & TREN PERIODIK",
        "topic": "Anomali Titik Didih Hidrida Non-Logam Golongan 15, 16, dan 17",
        "stem": "Grafik titik didih hidrida non-logam golongan 14, 15, 16, dan 17 terhadap periode menunjukkan bahwa hidrida periode 2 ($\\text{H}_2\\text{O}$, $\\text{HF}$, dan $\\text{NH}_3$) memiliki titik didih yang jauh lebih tinggi secara anomali dibandingkan hidrida periode 3 di bawahnya ($\\text{H}_2\\text{S}$, $\\text{HCl}$, dan $\\text{PH}_3$). Namun, untuk golongan 14, titik didih metana ($\\text{CH}_4$) justru lebih rendah daripada silana ($\\text{SiH}_4$). Penjelasan ilmiah yang paling tepat untuk fenomena ini adalah...",
        "correct": "Atom $\\text{O}$, $\\text{F}$, dan $\\text{N}$ memiliki elektronegativitas sangat tinggi dan jari-jari atom kecil dengan pasangan elektron bebas sehingga mampu membentuk ikatan hidrogen intermolekul yang sangat kuat; sebaliknya $\\text{CH}_4$ bersifat nonpolar dan atom C tidak memiliki PEB sehingga interaksinya hanya gaya dispersi London yang meningkat seiring ukuran massa molekul ke $\\text{SiH}_4$.",
        "distractors": [
            "Molekul $\\text{CH}_4$ memiliki ikatan ionik yang mudah putus, sedangkan molekul $\\text{SiH}_4$ membentuk ikatan kovalen raksasa mirip struktur intan kristal.",
            "Senyawa $\\text{H}_2\\text{O}$, $\\text{HF}$, dan $\\text{NH}_3$ mengalami ionisasi sempurna menjadi ion-ion bebas dalam fasa gas yang meningkatkan gaya Coulomb.",
            "Gaya van der Waals pada $\\text{H}_2\\text{S}$ dan $\\text{HCl}$ lebih kuat daripada $\\text{H}_2\\text{O}$ karena belerang memiliki lebih banyak proton dalam intinya.",
            "Atom karbon mengalami hibridisasi sp sedangkan atom silikon mengalami hibridisasi sp3d2 dalam senyawa hidridanya."
        ],
        "formula": {
            "title": "IKATAN HIDROGEN VS GAYA DISPERSI LONDON",
            "latex": "T_b: \\text{H}_2\\text{O} (100^\\circ\\text{C}) \\gg \\text{H}_2\\text{S} (-60^\\circ\\text{C}); \\quad T_b: \\text{HF} (20^\\circ\\text{C}) \\gg \\text{HCl} (-85^\\circ\\text{C}); \\quad T_b: \\text{CH}_4 (-161^\\circ\\text{C}) < \\text{SiH}_4 (-112^\\circ\\text{C})",
            "legend": "• Ikatan hidrogen hanya terbentuk jika atom H terikat kovalen pada N, O, atau F (sangat elektronegatif & ada PEB)<br>• Golongan 14 ($\text{CH}_4$, $\text{SiH}_4$, $\text{GeH}_4$) bersifat nonpolar sempurna tanpa PEB: tren titik didih murni dikendalikan oleh massa molekul dan kepolarisasian awan elektron (gaya London)"
        },
        "hints": {
            "concept": "Ikatan hidrogen intermolekul yang kuat hanya terjadi pada N, O, F karena elektronegativitas tinggi dan ukuran atom kecil. CH4 tidak membentuk ikatan hidrogen karena nonpolar dan tidak ada PEB.",
            "execution": "Pilih jawaban yang membedakan keberadaan ikatan hidrogen pada H2O/HF/NH3 dengan dominasi gaya dispersi London pada deret hidrida golongan 14."
        }
    },
    {
        "id": "kim-sim-11",
        "materi": "KIMIA KOORDINASI MEDIS",
        "topic": "Stereokimia Senyawa Kompleks Cis-Platin sebagai Kemoterapi Kanker",
        "stem": "Senyawa kompleks platina(II) $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$ memiliki bentuk geometri bujur sangkar ($\\textit{square planar}$). Senyawa ini memiliki dua isomer geometri: isomer $\\textit{cis}$ (cisplatin) dan isomer $\\textit{trans}$ (transplatin). Cisplatin digunakan secara luas sebagai agen kemoterapi kanker yang sangat poten, sedangkan transplatin sama sekali tidak aktif secara klinis. Mekanisme biokimia molekuler yang mendasari perbedaan efektivitas medis ini adalah...",
        "correct": "Pada isomer $\\textit{cis}$, kedua ligan klorida yang labil terletak berdampingan dengan jarak $\\sim 3{,}3\\text{ Å}$, tepat cocok untuk melakukan koordinasi silang bifungsional intra-untai ($\\textit{intrastrand cross-link}$) pada dua basa nitrogen guanin bersebelahan pada DNA heliks ganda sel kanker sehingga memicu distorsi struktural dan apoptosis sel.",
        "distractors": [
            "Pada isomer $\\textit{trans}$, kedua atom platina saling berikatan membentuk polimer logam berat yang tidak mampu menembus membran sel sama sekali.",
            "Isomer $\\textit{cis}$ mengalami disosiasi total menghasilkan gas amonia pekat yang meracuni mitokondria sel kanker secara selektif.",
            "Isomer $\\textit{trans}$ bersifat sangat mudah terbakar di dalam plasma darah sehingga terurai sebelum mencapai target inti sel.",
            "Cisplatin bekerja murni sebagai antioksidan pemulung radikal bebas di dalam sitoplasma sel darah putih normal."
        ],
        "formula": {
            "title": "MEKANISME KERJA CISPLATIN TERHADAP DNA SEL TUMOR",
            "latex": "\\textit{cis}\\text{-}[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2] + 2\\text{H}_2\\text{O} \\rightarrow \\textit{cis}\\text{-}[\\text{Pt}(\\text{NH}_3)_2(\\text{H}_2\\text{O})_2]^{2+} + 2\\text{Cl}^- \\xrightarrow{\\text{Guanin } N7} 1{,}2\\text{-intrastrand crosslink}",
            "legend": "• Jarak ligan Cl-Cl pada isomer $\\textit{cis}$ = $3{,}3\\text{ Å}$ cocok dengan jarak $N7$ dua guanin adjacent ($3{,}4\\text{ Å}$)<br>• Isomer $\\textit{trans}$ memiliki ligan berseberangan ($180^\\circ$) berjarak $> 4\\text{ Å}$, gagal membentuk crosslink efektif<br>• Distorsi tekukan DNA sebesar $30-40^\\circ$ memblokir replikasi dan transkripsi DNA tumor"
        },
        "hints": {
            "concept": "Isomer cis menempatkan dua ligan klorida labil berdampingan (sudut 90 derajat). Posisi ini memungkinkan platina mengikat dua basa guanin bersebelahan pada untai DNA yang sama (intrastrand crosslink).",
            "execution": "Pilih opsi yang menjelaskan pengikatan silang intra-untai dua basa guanin oleh isomer cis."
        }
    },
    {
        "id": "kim-sim-12",
        "materi": "KIMIA ORGANIK SINTESIS",
        "topic": "Sintesis Aspirin (Asam Asetilsalisilat) dan Uji Kemurnian",
        "stem": "Dalam sintesis aspirin di laboratorium kimia organik, asam salisilat (asam $o$-hidroksibenzoat, $M_r = 138$) direaksikan dengan anhidrida asetat berlebih ($M_r = 102$) menggunakan katalis beberapa tetes asam sulfat pekat ($\\text{H}_2\\text{SO}_4$) menghasilkan asam asetilsalisilat ($M_r = 180$) dan produk samping asam asetat. Untuk menguji apakah produk aspirin hasil kristalisasi masih mengandung sisa asam salisilat yang belum bereaksi, pereaksi uji laboratorium yang paling tepat dan perubahan yang teramati adalah...",
        "correct": "Penambahan beberapa tetes larutan $\\text{FeCl}_3$ encer; jika masih terdapat pengotor asam salisilat, larutan akan menghasilkan warna ungu pekat akibat pembentukan kompleks besi(III) fenolat dengan gugus fenol bebas $-\\text{OH}$ asam salisilat.",
        "distractors": [
            "Penambahan larutan Fehling A dan B dipanaskan; jika terbentuk endapan merah bata menunjukkan adanya gugus aldehida pada asam salisilat.",
            "Penambahan pereaksi Tollens menghasilkan cermin perak mengkilap di dinding tabung reaksi akibat oksidasi gugus karboksilat.",
            "Penambahan larutan bromin dalam $\\text{CCl}_4$; jika warna coklat hilang menandakan adanya ikatan rangkap tiga terisolasi pada aspirin murni.",
            "Uji kertas lakmus merah; aspirin murni akan mengubah lakmus merah menjadi biru pekat karena bersifat basa nitrogen kuat."
        ],
        "formula": {
            "title": "SINTESIS ASPIRIN & UJI FENOL BEBAS DENGAN FECL3",
            "latex": "\\text{C}_7\\text{H}_6\\text{O}_3 + (\\text{CH}_3\\text{CO})_2\\text{O} \\xrightarrow{\\text{H}_2\\text{SO}_4} \\text{C}_9\\text{H}_8\\text{O}_4 + \\text{CH}_3\\text{COOH}; \\quad 6\\text{ArOH} + \\text{Fe}^{3+} \\rightarrow [\\text{Fe}(\\text{OAr})_6]^{3-} \\text{ (ungu)}",
            "legend": "• Asam salisilat memiliki gugus $-\\text{OH}$ fenolik bebas yang bereaksi dengan $\\text{Fe}^{3+}$ membentuk kompleks ungu<br>• Pada aspirin murni, gugus $-\\text{OH}$ telah terasetilasi menjadi gugus ester asetil ($-\\text{OCOCH}_3$) sehingga tidak bereaksi dengan $\\text{FeCl}_3$"
        },
        "hints": {
            "concept": "Asam salisilat memiliki gugus fenolik (-OH menempel pada cincin benzena), sedangkan aspirin telah diubah menjadi ester sehingga tidak memiliki gugus fenol bebas. Uji spesifik fenol menggunakan FeCl3.",
            "execution": "Reaksi ion Fe3+ dengan fenol menghasilkan kompleks koordinasi berwarna ungu pekat."
        }
    },
    {
        "id": "kim-sim-13",
        "materi": "MEKANISME REAKSI ORGANIK",
        "topic": "Penelusuran Isotopik Oksigen-18 pada Reaksi Esterifikasi Fischer",
        "stem": "Reaksi esterifikasi Fischer antara asam asetat berlabel isotop oksigen-16 biasa ($\\text{CH}_3\\text{COOH}$) dengan etanol yang dilabeli isotop stabil oksigen-18 pada atom oksigen hidroksilnya ($\\text{CH}_3\\text{CH}_2^{18}\\text{OH}$) dilangsungkan dengan katalis asam kuat $\\text{H}^+$. Setelah mencapai kesetimbangan, analisis spektrometri massa menunjukkan bahwa atom isotop $^{18}\\text{O}$ terlokalisasi pada molekul...",
        "correct": "Etil asetat pada atom oksigen penjembatan ester ($\\text{CH}_3\\text{CO-}^{18}\\text{OCH}_2\\text{CH}_3$), sedangkan molekul air yang tereliminasi murni mengandung isotop oksigen biasa ($\\text{H}_2^{16}\\text{O}$), membuktikan bahwa pemutusan ikatan terjadi pada ikatan asil–oksigen ($\text{C-OH}$) dari asam karboksilat.",
        "distractors": [
            "Molekul air sebagai $\\text{H}_2^{18}\\text{O}$, membuktikan bahwa gugus hidroksil etanol terlepas utuh diserang oleh proton asam asetat.",
            "Kedua atom oksigen asam asetat secara acak karena terjadi pertukaran isotop simetris melalui radikal bebas gas metana.",
            "Gas karbon dioksida terbebas akibat dekarboksilasi spontan esterifikasi asam karboksilat alifatik jenuh.",
            "Tidak satu pun molekul produk yang mengandung $^{18}\\text{O}$ karena isotop oksigen meluruh menjadi isotop fluorin radioaktif selama pemanasan."
        ],
        "formula": {
            "title": "MEKANISME ASILASI ESTERIFIKASI FISCHER (ISOTOPIC LABELING)",
            "latex": "\\text{R-C}(=\\text{O})-\\text{OH} + \\text{H-}^{18}\\text{O-R}' \\underset{\\text{katalis } \\text{H}^+}{\\rightleftharpoons} \\text{R-C}(=\\text{O})-^{18}\\text{O-R}' + \\text{H}_2\\text{O}",
            "legend": "• Nukleofil alkohol $\\text{R}'^{18}\\text{OH}$ menyerang karbon karbonil terprotonasi asam karboksilat<br>• Terbentuk zat antara tetrahedral<br>• Gugus pergi ($\\textit{leaving group}$) adalah molekul air dari gugus $-\\text{OH}$ asam karboksilat awal<br>• Atom $^{18}\\text{O}$ tetap menempel pada gugus alkoksi ester yang dihasilkan"
        },
        "hints": {
            "concept": "Pada esterifikasi Fischer, gugus -OH dilepas oleh asam karboksilat, sedangkan alkohol hanya melepas atom H (ikatan C-O alkohol TIDAK putus).",
            "execution": "Atom 18O dari alkohol tetap berada pada molekul ester (etil asetat), sedangkan H2O berasal dari -OH asam karboksilat dan proton H."
        }
    },
    {
        "id": "kim-sim-14",
        "materi": "BIOKIMIA & KINETIKA ENZIM",
        "topic": "Penentuan Tipe Inhibisi Enzim Menggunakan Plot Lineweaver-Burk",
        "stem": "Dalam penelitian kinetika suatu enzim metabolik, diperoleh data laju reaksi awal ($V_0$) terhadap konsentrasi substrat ($[S]$). Saat ditambahkan senyawa inhibitor $X$, diperoleh kurva ganda resiprokal Lineweaver-Burk ($\\frac{1}{V_0}$ vs $\\frac{1}{[S]}$) dengan karakteristik:<br>• Titik potong sumbu vertikal ($1/V_{\\max}$) tidak berubah sama sekali dibandingkan tanpa inhibitor.<br>• Titik potong sumbu horizontal ($-1/K_m$) bergeser mendekati titik nol (nilai $K_m$ semu meningkat).<br>Berdasarkan data tersebut, jenis mekanisme inhibisi yang dilakukan oleh senyawa $X$ dan cara menanggulangi efek penghambatan tersebut adalah...",
        "correct": "Inhibisi kompetitif; inhibitor $X$ memiliki kemiripan struktur dengan substrat dan bersaing merebutkan sisi aktif enzim bebas, sehingga efek penghambatan dapat diatasi tuntas dengan meningkatkan konsentrasi substrat $[S]$ hingga sangat tinggi.",
        "distractors": [
            "Inhibisi non-kompetitif; inhibitor mengikat sisi alosterik enzim sehingga nilai laju maksimum $V_{\\max}$ turun permanen apapun konsentrasi substratnya.",
            "Inhibisi un-kompetitif; inhibitor hanya dapat mengikat kompleks enzim-substrat yang menurunkan nilai $V_{\\max}$ dan $K_m$ secara bersamaan.",
            "Inhibisi irreversibel bunuh diri; inhibitor membentuk ikatan kovalen permanen yang merusak struktur primer rantai polipeptida enzim.",
            "Inhibisi umpan balik alosterik; inhibitor mempercepat laju denaturasi termal protein enzim pada suhu fisiologis."
        ],
        "formula": {
            "title": "PERSAMAAN LINEWEAVER-BURK & INHIBISI KOMPETITIF",
            "latex": "\\frac{1}{V_0} = \\left(\\frac{K_m^{\\text{app}}}{V_{\\max}}\\right)\\frac{1}{[S]} + \\frac{1}{V_{\\max}}; \\quad K_m^{\\text{app}} = K_m \\left(1 + \\frac{[I]}{K_I}\\right); \\quad V_{\\max} = \\text{konstan}",
            "legend": "• Titik potong sumbu-$Y$ ($1/V_{\\max}$) tetap $\\implies V_{\\max}$ tidak berubah<br>• Titik potong sumbu-$X$ ($-1/K_m^{\\text{app}}$) bergeser ke kanan mendekati 0 $\\implies K_m^{\\text{app}} > K_m$<br>• Merupakan ciri khas absolut inhibisi enzim tipe kompetitif"
        },
        "hints": {
            "concept": "Ingat rumus Lineweaver-Burk. Jika perpotongan sumbu-Y tetap (Vmax sama), tetapi kemiringan berubah dan perpotongan sumbu-X bergeser (Km bertambah), itu adalah inhibisi kompetitif.",
            "execution": "Inhibitor bersaing langsung di sisi aktif. Dapat diatasi dengan menambahkan konsentrasi substrat berlebih."
        }
    },
    {
        "id": "kim-sim-15",
        "materi": "POLIMER & MATERIAL MAJU",
        "topic": "Struktur dan Kekuatan Tarik Balistik Serat Polimer Kevlar",
        "stem": "Kevlar (poli-p-fenilena tereftalamida) adalah polimer sintetis aramid berkekuatan tarik lima kali lebih kuat daripada baja dengan massa yang sama, digunakan untuk rompi antipeluru dan komponen pesawat ruang angkasa. Kevlar disintesis melalui reaksi polimerisasi kondensasi antara 1,4-fenilenadiamina dan tereftaloil klorida. Faktor struktural molekuler yang memberikan kekuatan tarik dan ketahanan mekanik yang luar biasa pada serat Kevlar adalah...",
        "correct": "Rantai-rantai polimer memiliki konformasi lurus kaku dengan cincin benzena tersubstitusi para yang tersusun sangat teratur dan saling dihubungkan secara masif oleh jaringan ikatan hidrogen antarrantai antara gugus amida ($\\text{N-H}\\cdots\\text{O=C}$) serta penumpukan interaksi $\\pi-\\pi$ antar cincin aromatik.",
        "distractors": [
            "Terbentuknya ikatan kovalen silang jembatan disulfida antara atom belerang yang ditambahkan pada proses vulkanisasi termal.",
            "Tingginya percabangan rantai samping alifatik yang membuat polimer bersifat amorf dan elastis menyerap benturan proyektil.",
            "Kandungan atom klorin yang membentuk kisi kristal garam ionik dengan kerapatan massa jenis mendekati logam berat raksa.",
            "Kemampuan rantai polimer untuk berotasi bebas $360^\\circ$ pada suhu kamar sehingga berperilaku seperti cairan superkritis."
        ],
        "formula": {
            "title": "POLIMERISASI KONDENSASI & IKATAN ANTARRANTAL KEVLAR",
            "latex": "n\\text{ H}_2\\text{N-C}_6\\text{H}_4\\text{-NH}_2 + n\\text{ Cl-CO-C}_6\\text{H}_4\\text{-CO-Cl} \\rightarrow [-\\text{NH-C}_6\\text{H}_4\\text{-NH-CO-C}_6\\text{H}_4\\text{-CO}-]_n + 2n\\text{ HCl}",
            "legend": "• Gugus amida ($-\\text{CONH}-$) membentuk jalinan ikatan hidrogen terarah antarrantai sejajar<br>• Orientasi posisi para ($1,4$) pada cincin benzena menghasilkan geometri molekul linear planar kaku ($\\textit{rigid-rod}$)<br>• Menghasilkan derajat kristalinitas dan kekuatan tarik balistik luar biasa tinggi"
        },
        "hints": {
            "concept": "Kevlar tersusun dari cincin benzena posisi para yang kaku dan dihubungkan oleh gugus amida. Antarrantai sejajar terbentuk ikatan hidrogen N-H...O=C yang sangat rapat dan kuat.",
            "execution": "Pilih jawaban yang menyebutkan konformasi lurus kaku dengan ikatan hidrogen antarrantai dan interaksi penumpukan pi-pi aromatik."
        }
    },
    {
        "id": "kim-sim-16",
        "materi": "KIMIA HIJAU (GREEN CHEMISTRY)",
        "topic": "Perhitungan Ekonomi Atom (Atom Economy) Sintesis Etilen Oksida",
        "stem": "Dalam kerangka 12 Prinsip Kimia Hijau, efisiensi reaksi dinilai dari persentase ekonomi atom ($\\textit{atom economy}$). Senyawa etilen oksida ($\\text{C}_2\\text{H}_4\\text{O}$, $M_r = 44$) dapat diproduksi melalui dua rute industri berlainan:<br>Rute Tradisional (Klorohidrin):<br>$\\text{C}_2\\text{H}_4 + \\text{Cl}_2 + \\text{Ca(OH)}_2 \\rightarrow \\text{C}_2\\text{H}_4\\text{O} + \\text{CaCl}_2 + \\text{H}_2\\text{O}$<br>($M_r$: $\\text{C}_2\\text{H}_4 = 28$, $\\text{Cl}_2 = 71$, $\\text{Ca(OH)}_2 = 74$, $\\text{C}_2\\text{H}_4\\text{O} = 44$, $\\text{CaCl}_2 = 111$, $\\text{H}_2\\text{O} = 18$)<br>Rute Katalitik Modern (Oksidasi Langsung):<br>$\\text{C}_2\\text{H}_4 + \\frac{1}{2}\\text{O}_2 \\xrightarrow{\\text{Ag}} \\text{C}_2\\text{H}_4\\text{O}$<br>Persentase ekonomi atom untuk rute klorohidrin tradisional dan rute oksidasi langsung berturut-turut adalah...",
        "correct": "$25{,}4\\%$ pada rute klorohidrin dan $100\\%$ pada rute oksidasi langsung, karena rute tradisional menghasilkan massa produk samping limbah ($\\text{CaCl}_2$ dan $\\text{H}_2\\text{O}$) yang jauh lebih besar daripada produk target: $\\frac{44}{28 + 71 + 74} \\times 100\\% = \\frac{44}{173} \\times 100\\% = 25{,}4\\%$, sedangkan rute katalitik langsung mengintegrasikan 100% massa seluruh reaktan ke dalam produk akhir tanpa limbah.",
        "distractors": [
            "$50{,}0\\%$ pada rute klorohidrin dan $50{,}0\\%$ pada rute oksidasi langsung, karena kedua reaksi sama-sama menghasilkan 1 mol etilen oksida.",
            "$80{,}5\\%$ pada rute klorohidrin dan $20{,}0\\%$ pada rute oksidasi langsung, dihitung dari rasio koefisien stoikiometri reaktan pembatas.",
            "$100\\%$ pada rute klorohidrin dan $44{,}0\\%$ pada rute oksidasi langsung, akibat salah membagi massa produk samping dengan massa reaktan.",
            "$33{,}3\\%$ pada rute klorohidrin dan $66{,}7\\%$ pada rute oksidasi langsung, dihitung dari rasio jumlah atom karbon terhadap hidrogen."
        ],
        "formula": {
            "title": "PERSAMAAN EKONOMI ATOM (ATOM ECONOMY)",
            "latex": "\\%\\text{ Atom Economy} = \\frac{\\text{Massa Molar Produk Diinginkan}}{\\sum \\text{Massa Molar Seluruh Reaktan}} \\times 100\\%",
            "legend": "• Rute Klorohidrin: $\\frac{44}{28 + 71 + 74} \\times 100\\% = \\frac{44}{173} \\times 100\\% = 25{,}43\\%$<br>• Rute Oksidasi Katalitik: $\\frac{44}{28 + 16} \\times 100\\% = \\frac{44}{44} \\times 100\\% = 100\\%$<br>• Rute oksidasi langsung mematuhi prinsip green chemistry pencegahan limbah"
        },
        "hints": {
            "concept": "Rumus Ekonomi Atom = (Mr produk target / total Mr semua reaktan) * 100%. Untuk rute adisi langsung tanpa produk samping, ekonomi atomnya selalu 100%.",
            "execution": "Rute 1: 44 / (28 + 71 + 74) = 44 / 173 = 25,4%. Rute 2: 44 / (28 + 16) = 44 / 44 = 100%."
        }
    },
    {
        "id": "kim-sim-17",
        "materi": "RADIOKIMIA & KEDOKTERAN NUKLIR",
        "topic": "Peluruhan Radioisotop Teknesium-99m dalam Diagnosis Medis",
        "stem": "Radioisotop Teknesium-99m ($^{99m}_{43}\\text{Tc}$) merupakan agen pencitraan medis ($\\textit{radiotracer}$) yang paling banyak digunakan di dunia untuk pemindaian organ vital. Isomer nuklir ini memiliki waktu paruh $T_{1/2} = 6{,}0\\text{ jam}$ dan meluruh menjadi bentuk dasarnya, $^{99}_{43}\\text{Tc}$, sambil memancarkan radiasi gamma murni berenergi $140\\text{ keV}$. Jika suatu rumah sakit menerima sediaan awal $^{99m}\\text{Tc}$ dengan aktivitas radioaktif $800\\text{ MBq}$, aktivitas radiasi yang tersisa setelah dibiarkan selama $24\\text{ jam}$ adalah...",
        "correct": "$50\\text{ MBq}$, karena selang waktu $t = 24\\text{ jam}$ setara dengan $n = \\frac{t}{T_{1/2}} = \\frac{24}{6{,}0} = 4$ kali waktu paruh. Aktivitas sisa dihitung dengan rumus peluruhan radioaktif orde pertama: $A_t = A_0 \\left(\\frac{1}{2}\\right)^n = 800 \\times \\left(\\frac{1}{2}\\right)^4 = 800 \\times \\frac{1}{16} = 50\\text{ MBq}$.",
        "distractors": [
            "$200\\text{ MBq}$, dihitung dari asumsi aktivitas radioaktif berkurang secara linear sebesar 25% setiap 6 jam.",
            "$100\\text{ MBq}$, dihitung jika hanya mengalami 3 kali waktu paruh (18 jam peluruhan).",
            "$25\\text{ MBq}$, dihitung jika waktu peluruhan diasumsikan telah berlangsung selama 5 kali waktu paruh (30 jam).",
            "$0\\text{ MBq}$, karena mengasumsikan zat radioaktif telah musnah tak bersisa setelah melampaui waktu satu hari semalam."
        ],
        "formula": {
            "title": "HUKUM PELURUHAN RADIOAKTIF ORDE PERTAMA",
            "latex": "n = \\frac{t}{T_{1/2}} = \\frac{24\\text{ jam}}{6\\text{ jam}} = 4; \\quad A_t = A_0 \\left(\\frac{1}{2}\\right)^n = 800\\text{ MBq} \\times \\left(\\frac{1}{2}\\right)^4 = \\frac{800}{16} = 50\\text{ MBq}",
            "legend": "• Waktu paruh $T_{1/2} = 6{,}0\\text{ jam}$<br>• Jumlah siklus peluruhan $n = 4$<br>• Aktivitas akhir $A_t = 50\\text{ MBq}$ (tersisa $6{,}25\\%$ dari aktivitas mula-mula)"
        },
        "hints": {
            "concept": "Peluruhan radioaktif mengikuti kinetika orde pertama: A_t = A_0 * (1/2)^n, dengan n = t / T_1/2.",
            "execution": "n = 24 / 6 = 4. Maka A_t = 800 * (1/2)^4 = 800 / 16 = 50 MBq."
        }
    },
    {
        "id": "kim-sim-18",
        "materi": "IKATAN KIMIA & KEPOLARAN MOLEKUL",
        "topic": "Analisis Momen Dipol Relatif Molekul BF3, NF3, dan NH3",
        "stem": "Berdasarkan teori domain elektron (VSEPR) dan momen dipol ikatan, molekul boron trifluorida ($\\text{BF}_3$), nitrogen trifluorida ($\\text{NF}_3$), dan amonia ($\\text{NH}_3$) memiliki karakteristik kepolaran yang sangat berbeda. Diketahui bahwa elektronegativitas $\\text{F} (4{,}0) > \\text{N} (3{,}0) > \\text{H} (2{,}1) > \\text{B} (2{,}0)$. Perbandingan momen dipol molekul ($\\mu$) yang benar beserta alasan geometrinya adalah...",
        "correct": "$\\mu[\\text{BF}_3] = 0\\text{ D} < \\mu[\\text{NF}_3] (0{,}24\\text{ D}) < \\mu[\\text{NH}_3] (1{,}47\\text{ D})$; $\\text{BF}_3$ nonpolar karena geometri trigonal planar simetris membatalkan seluruh dipol ikatan; pada $\\text{NF}_3$ dipol ikatan polar $\\text{N}-\\text{F}$ berlawanan arah dengan dipol pasangan elektron bebas sehingga saling melemahkan, sedangkan pada $\\text{NH}_3$ dipol ikatan $\\text{N}-\\text{H}$ dan dipol pasangan elektron bebas searah sehingga saling memperkuat.",
        "distractors": [
            "$\\mu[\\text{NF}_3] > \\mu[\\text{NH}_3] > \\mu[\\text{BF}_3]$, karena atom fluorin memiliki elektronegativitas terbesar di tabel periodik sehingga dipol ikatannya selalu mendominasi mutlak.",
            "$\\mu[\\text{BF}_3] > \\mu[\\text{NF}_3] > \\mu[\\text{NH}_3]$, karena ikatan kovalen antara boron dan fluorin memiliki selisih elektronegativitas paling besar.",
            "$\\mu[\\text{BF}_3] = \\mu[\\text{NF}_3] = \\mu[\\text{NH}_3] = 0\\text{ D}$, karena ketiga molekul sama-sama mengikat tiga atom ligan yang identik mengelilingi atom pusat.",
            "$\\mu[\\text{NH}_3] = 0\\text{ D}$, karena gaya tolak pasangan elektron bebas menetralkan muatan parsial positif pada ketiga atom hidrogen."
        ],
        "formula": {
            "title": "VEKTOR MOMEN DIPOL MOLEKUL POLIATIK",
            "latex": "\\vec{\\mu}_{\\text{total}} = \\sum \\vec{\\mu}_{\\text{ikatan}} + \\vec{\\mu}_{\\text{PEB}}; \\quad \\mu(\\text{BF}_3) = 0\\text{ D}; \\quad \\mu(\\text{NF}_3) = 0{,}24\\text{ D}; \\quad \\mu(\\text{NH}_3) = 1{,}47\\text{ D}",
            "legend": "• $\\text{BF}_3$: Geometri segitiga datar simetris ($120^\\circ$, tanpa PEB) $\\implies \\sum \\vec{\\mu} = 0$<br>• $\\text{NF}_3$: Dipol PEB mengarah ke atas, dipol $\\text{N}\\rightarrow \\text{F}$ mengarah ke bawah (saling melawan)<br>• $\\text{NH}_3$: Dipol $\\text{H}\\rightarrow \\text{N}$ mengarah ke atas dan dipol PEB ke atas (saling memperkuat)"
        },
        "hints": {
            "concept": "Perhatikan resultan vektor dipol ikatan dan dipol PEB. Pada BF3 simetri planar membatalkan dipol. Pada NF3, dipol ikatan N-F melawan dipol PEB. Pada NH3, dipol ikatan H-N searah dengan dipol PEB.",
            "execution": "Urutan momen dipol: BF3 (0) < NF3 (0,24 D) < NH3 (1,47 D)."
        }
    },
    {
        "id": "kim-sim-19",
        "materi": "TERMODINAMIKA SPONTANITAS",
        "topic": "Termodinamika Pelarutan Endotermik Garam Amonium Nitrat pada Cold Pack",
        "stem": "Kompres dingin instan ($\\textit{cold pack}$) bekerja berdasarkan reaksi pelarutan spontan garam amonium nitrat padat ke dalam air murni:<br>$\\text{NH}_4\\text{NO}_3(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{NH}_4^+(aq) + \\text{NO}_3^-(aq) \\quad \\Delta H^\\circ = +25{,}7\\text{ kJ/mol}$<br>Meskipun proses pelarutan ini bersifat endotermik (menyerap kalor dari lingkungan sehingga suhu turun drastis), proses ini berlangsung secara spontan pada suhu kamar ($298\\text{ K}$). Penjelasan termodinamika yang paling valid berdasarkan Hukum Kedua Termodinamika adalah...",
        "correct": "Pelarutan kristal padat menjadi ion-ion terhidrasi bebas meningkatkan derajat ketidakteraturan sistem secara drastis ($\\Delta S^\\circ_{\\text{sistem}} \\gg 0$), sehingga pada suhu kamar suku pengurang termal $T\\Delta S^\\circ$ bernilai positif sangat besar dan melampaui nilai $\\Delta H^\\circ$, menghasilkan perubahan energi bebas Gibbs bernilai negatif ($\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ < 0$).",
        "distractors": [
            "Proses pelarutan menghasilkan energi kisi kristal yang sangat eksotermik sehingga energi aktivasi reaksi menjadi bernilai negatif.",
            "Suhu dingin yang tercipta memicu penurunan entropi semesta secara spontan sesuai Hukum Ketiga Termodinamika.",
            "Ion amonium mengalami reaksi fusi nuklir dengan molekul air melepaskan radiasi partikel alfa yang menetralkan nilai entalpi.",
            "Reaksi tersebut sebenarnya tidak spontan dan hanya dapat berlangsung jika diberi bantuan arus listrik luar secara kontinu."
        ],
        "formula": {
            "title": "PERSAMAAN ENERGI BEBAS GIBBS & SPONTANITAS ENDOTERMIK",
            "latex": "\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ < 0 \\iff T\\Delta S^\\circ > \\Delta H^\\circ > 0",
            "legend": "• $\\Delta H^\\circ = +25{,}7\\text{ kJ/mol}$ (endotermik, menyerap kalor)<br>• $\\Delta S^\\circ \\approx +108\\text{ J/(mol K)}$ (peningkatan keteracakan kisi ionik padat menjadi ion terlarut)<br>• Pada $298\\text{ K}$: $T\\Delta S^\\circ = 298 \\times 0{,}108 = +32{,}2\\text{ kJ/mol} > \\Delta H^\\circ$<br>• $\\Delta G^\\circ = 25{,}7 - 32{,}2 = -6{,}5\\text{ kJ/mol} < 0$ (spontan digerakkan oleh entropi)"
        },
        "hints": {
            "concept": "Reaksi endotermik (Delta H > 0) hanya bisa spontan jika didorong oleh peningkatan entropi yang besar (Delta S > 0) pada suhu di mana T*Delta S > Delta H, sehingga Delta G < 0.",
            "execution": "Pilih opsi yang menjelaskan dominasi kenaikan entropi (Delta S sistem > 0) yang membuat Delta G negatif pada suhu kamar."
        }
    },
    {
        "id": "kim-sim-20",
        "materi": "KIMIA KOLOID & PENGOLAHAN AIR",
        "topic": "Mekanisme Koagulasi Koloid Berdasarkan Aturan Schulze-Hardy",
        "stem": "Dalam proses penjernihan air minum PDAM, air sungai yang keruh mengandung partikel koloid lumpur lempung yang bermuatan negatif dan stabil melayang dalam air. Untuk mengendapkan koloid lumpur tersebut, ditambahkan koagulan tawas (tawas aluminium sulfat, $\\text{Al}_2(\\text{SO}_4)_3$). Menurut aturan Schulze-Hardy, keefektifan ion koagulan dalam menggumpalkan koloid ditentukan oleh valensi muatannya. Perbandingan efektivitas koagulasi ion $\\text{Al}^{3+}$, $\\text{Mg}^{2+}$, dan $\\text{Na}^+$ terhadap koloid lumpur bermuatan negatif tersebut adalah...",
        "correct": "$\\text{Al}^{3+} \\gg \\text{Mg}^{2+} \\gg \\text{Na}^+$; daya koagulasi meningkat secara eksponensial sebanding dengan pangkat enam valensi muatan kation penyerap ($\\text{daya} \\propto z^6$), sehingga ion trivalen $\\text{Al}^{3+}$ memiliki daya pengendapan sekitar 700–1000 kali lebih kuat dibanding ion monovalen $\\text{Na}^+$ dalam menetralkan lapisan rangkap listrik koloid.",
        "distractors": [
            "$\\text{Na}^+ > \\text{Mg}^{2+} > \\text{Al}^{3+}$, karena ion natrium berukuran paling kecil sehingga mobilitas difusinya dalam air paling cepat.",
            "$\\text{Al}^{3+} = \\text{Mg}^{2+} = \\text{Na}^+$, karena seluruh kation logam golongan utama memiliki kemampuan koagulasi identik per mol ion.",
            "Koagulasi ditentukan oleh anion sulfida bukan oleh kation, sehingga jenis logam tidak mempengaruhi pengendapan koloid lumpur.",
            "Ion $\\text{Al}^{3+}$ tidak mampu mengendapkan koloid karena aluminium bersifat amfoter yang langsung larut kembali sebagai aluminat."
        ],
        "formula": {
            "title": "ATURAN SCHULZE-HARDY PADA KOAGULASI KOLOID",
            "latex": "\\text{Konsentrasi Koagulasi Kritis (CCC)} \\propto \\frac{1}{z^6}; \\quad \\text{Rasio Daya Koagulasi: } 1^6 : 2^6 : 3^6 = 1 : 64 : 729",
            "legend": "• Koloid lumpur bermuatan negatif dinetralkan oleh kation (ion lawan/counter-ion)<br>• Kation dengan muatan lebih tinggi ($z = 3$ untuk $\\text{Al}^{3+}$) menekan lapisan difus listrik jauh lebih efisien dibanding $z = 1$ ($\text{Na}^+$)<br>• Tawas aluminium sulfat merupakan koagulan air industri yang sangat hemat dan efektif"
        },
        "hints": {
            "concept": "Aturan Schulze-Hardy: ion lawan dengan valensi lebih tinggi memiliki daya koagulasi jauh lebih dahsyat (sebanding dengan z^6). Untuk koloid bermuatan negatif, kation penentu efektivitasnya.",
            "execution": "Valensi kation: Al3+ (z=3) > Mg2+ (z=2) > Na+ (z=1). Daya koagulasi Al3+ >> Mg2+ >> Na+."
        }
    },
    {
        "id": "kim-sim-21",
        "materi": "SPEKTROSKOPI STRUKTUR ORGANIK",
        "topic": "Identifikasi Gugus Fungsi Isomer Senyawa C3H6O via Spektroskopi IR",
        "stem": "Dua senyawa organik cair tak berwarna, senyawa $A$ dan senyawa $B$, memiliki rumus molekul identik $\\text{C}_3\\text{H}_6\\text{O}$ ($M_r = 58$). Analisis spektroskopi inframerah (FTIR) memberikan data puncak serapan serapan berikut:<br>• Senyawa $A$: Menunjukkan puncak serapan sangat kuat dan tajam pada bilangan gelombang $1715\\text{ cm}^{-1}$, serta puncak getaran ulur $\\text{C-H}$ aldehida kembar (fermi resonance) pada $2720\\text{ cm}^{-1}$ dan $2820\\text{ cm}^{-1}$.<br>• Senyawa $B$: Menunjukkan puncak tajam sangat kuat pada $1715\\text{ cm}^{-1}$, namun tidak menunjukkan serapan sama sekali pada daerah $2700-2850\\text{ cm}^{-1}$ maupun daerah serapan lebar di atas $3200\\text{ cm}^{-1}$.<br>Identitas senyawa $A$ dan senyawa $B$ yang tepat adalah...",
        "correct": "Senyawa $A$ adalah propanal (propionaldehida) dan senyawa $B$ adalah propanon (aseton); serapan $1715\\text{ cm}^{-1}$ adalah vibrasi ulur gugus karbonil ($\\text{C=O}$), sedangkan serapan khas $2720$ dan $2820\\text{ cm}^{-1}$ adalah sidik jari ulur $\\text{C-H}$ aldehida yang tidak dimiliki oleh gugus keton propanon.",
        "distractors": [
            "Senyawa $A$ adalah 1-propanol dan senyawa $B$ adalah metil etil eter, dengan puncak $1715\\text{ cm}^{-1}$ merupakan vibrasi ikatan eter kovalen.",
            "Senyawa $A$ adalah asam propanoat dan senyawa $B$ adalah metil etanoat, karena memiliki atom oksigen tunggal dalam rumus strukturnya.",
            "Senyawa $A$ adalah propanon dan senyawa $B$ adalah propanal, terbalik karena keton selalu memiliki serapan ulur C-H fermi resonance.",
            "Senyawa $A$ adalah siklopropanol dan senyawa $B$ adalah propilena glikol jenuh."
        ],
        "formula": {
            "title": "KARAKTERISTIK SERAPAN INFRAMERAH (IR) GUGUS KARBONIL",
            "latex": "\\nu(\\text{C=O}): 1710 - 1720\\text{ cm}^{-1}; \\quad \\nu(\\text{C-H}_{\\text{aldehida}}): 2720\\text{ cm}^{-1} \\text{ & } 2820\\text{ cm}^{-1} \\text{ (doublet)}",
            "legend": "• Senyawa $A$ (Propanal, $\\text{CH}_3\\text{CH}_2\\text{CHO}$): Memiliki $\\text{C=O}$ dan $\\text{C-H}$ aldehida kembar<br>• Senyawa $B$ (Propanon/Aseton, $\\text{CH}_3\\text{COCH}_3$): Memiliki $\\text{C=O}$ keton tanpa $\\text{C-H}$ karbonil<br>• Tidak ada serapan lebar pada $3300\\text{ cm}^{-1}$ membuktikan ketiadaan gugus $-\\text{OH}$ alkohol"
        },
        "hints": {
            "concept": "Puncak kuat di 1715 cm^-1 adalah gugus karbonil C=O. Pasangan puncak di 2720 dan 2820 cm^-1 adalah ciri khas unik C-H aldehida (fermi resonance). Keton tidak memilikinya.",
            "execution": "Senyawa A memiliki C-H aldehida -> Propanal. Senyawa B tidak memilikinya -> Propanon (aseton)."
        }
    },
    {
        "id": "kim-sim-22",
        "materi": "KIMIA LINGKUNGAN & TERAPI KELASI",
        "topic": "Terapi Kelasi Intoksikasi Timbal (Pb2+) dengan Ligan EDTA",
        "stem": "Keracunan ion logam berat timbal ($\\text{Pb}^{2+}$) sangat berbahaya bagi sistem saraf manusia karena mengikat gugus tiol ($-\\text{SH}$) pada enzim tubuh. Dalam penanganan medis darurat, diberikan obat kelasi kalsium dinatrium edetat ($\\text{CaNa}_2\\text{EDTA}$). Alasan mengapa digunakan garam kompleks $\\text{CaNa}_2\\text{EDTA}$ dan bukan asam murni $\\text{Na}_2\\text{H}_2\\text{EDTA}$, serta mekanisme penggantian ion logam dalam darah adalah...",
        "correct": "Konstanta kestabilan pembentukan kompleks $[\\text{Pb(EDTA)}]^{2-}$ ($K_f = 10^{18{,}0}$) jauh lebih besar daripada $[\\text{Ca(EDTA)}]^{2-}$ ($K_f = 10^{10{,}7}$), sehingga ion $\\text{Pb}^{2+}$ mampu mendesak keluar ion $\\text{Ca}^{2+}$ dari ligan secara spontan; penggunaan garam Ca mencegah pengikatan ion kalsium bebas dalam darah yang dapat memicu hipokalsemia fatal.",
        "distractors": [
            "Ion $\\text{Pb}^{2+}$ mengendap sebagai garam sulfat tak larut di dalam ginjal sehingga tidak perlu diikat oleh ligan pengkhelat.",
            "EDTA murni akan menguap menjadi gas nitrogen dioksida yang merusak alveolus paru-paru jika tidak distabilkan oleh kalsium padat.",
            "Ion timbal bereaksi dengan kalsium membentuk amalgam logam padat yang langsung dikeluarkan lewat kelenjar keringat kulit.",
            "Konstanta kestabilan kompleks timbal lebih kecil daripada kalsium sehingga ion kalsium yang membunuh ion timbal secara enzimatik."
        ],
        "formula": {
            "title": "TERMODINAMIKA PERTUKARAN LIGAN KELASI EDTA",
            "latex": "[\\text{Ca(EDTA)}]^{2-} + \\text{Pb}^{2+} \\rightleftharpoons [\\text{Pb(EDTA)}]^{2-} + \\text{Ca}^{2+}; \\quad K_{\\text{tukar}} = \\frac{K_f(\\text{Pb})}{K_f(\\text{Ca})} = \\frac{10^{18{,}0}}{10^{10{,}7}} = 10^{7{,}3} \\approx 2 \\times 10^7",
            "legend": "• $K_f[\\text{Pb(EDTA)}^{2-}] = 10^{18{,}0} \\gg K_f[\\text{Ca(EDTA)}^{2-}] = 10^{10{,}7}$<br>• Nilai $K_{\\text{tukar}} = 2 \\times 10^7 \\gg 1$ menggeser reaksi hampir 100% ke arah pengikatan $\\text{Pb}^{2+}$<br>• Ion $\\text{Ca}^{2+}$ yang dilepaskan aman bagi darah, dan kelat $[\\text{Pb(EDTA)}]^{2-}$ larut dalam air sehingga dibuang lewat urin"
        },
        "hints": {
            "concept": "Pahami efek kelat dan konstanta pembentukan Kf. Kf(Pb-EDTA) jauh melampaui Kf(Ca-EDTA). Garam kalsium digunakan agar EDTA tidak merampas Ca2+ darah yang dapat menyebabkan kejang hipokalsemia.",
            "execution": "Pilih jawaban yang menjelaskan perbandingan nilai Kf (Pb mendesak Ca) dan pencegahan hipokalsemia."
        }
    },
    {
        "id": "kim-sim-23",
        "materi": "LARUTAN & CAMPURAN AZEOTROP",
        "topic": "Penyimpangan Negatif Hukum Raoult pada Campuran Aseton-Kloroform",
        "stem": "Pencampuran cairan aseton ($\\text{CH}_3\\text{COCH}_3$) dan kloroform ($\\text{CHCl}_3$) menghasilkan sistem larutan non-ideal yang mengalami penyimpangan negatif ($\\textit{negative deviation}$) terhadap Hukum Raoult, disertai pelepasan kalor ($\\Delta H_{\\text{campuran}} < 0$). Campuran ini membentuk azeotrop titik didih maksimum pada komposisi tertentu. Penyebab fisis-kimia dari fenomena penyimpangan negatif ini pada tingkat molekuler adalah...",
        "correct": "Terbentuknya ikatan hidrogen intermolekul yang kuat antara atom hidrogen yang bersifat asam pada kloroform (akibat tarikan tiga atom klorin yang sangat elektronegatif) dengan pasangan elektron bebas pada atom oksigen karbonil aseton, sehingga gaya tarik antarmolekul tak sejenis ($A-B$) lebih kuat daripada gaya tarik antarmolekul sejenis ($A-A$ dan $B-B$).",
        "distractors": [
            "Terjadi reaksi kimia adisi eliminasi permanen yang membentuk garam ester kovalen tak terionisasi di dalam larutan.",
            "Gaya tolak elektrostatik antara atom klorin kloroform dan gugus metil aseton menyebabkan molekul lebih mudah menguap ke udara bebas.",
            "Molekul aseton mengalami kondensasi aldol membentuk polimer padat yang mengendap di dasar bejana pencampur.",
            "Kloroform bertindak sebagai ligan bidentat yang mengikat atom karbon aseton membentuk sangkar khelat koordinasi."
        ],
        "formula": {
            "title": "PENYIMPANGAN NEGATIF HUKUM RAOULT",
            "latex": "P_{\\text{total}} < P_A^\\circ X_A + P_B^\\circ X_B; \\quad \\Delta H_{\\text{mix}} < 0; \\quad \\Delta V_{\\text{mix}} < 0; \\quad \\text{Ikatan H: } \\text{Cl}_3\\text{C-H}\\cdots\\text{O=C}(\\text{CH}_3)_2",
            "legend": "• Interaksi $A-B$ (aseton-kloroform) > interaksi $A-A$ dan $B-B$<br>• Tekanan uap jenuh total campuran lebih rendah daripada nilai ideal Raoult<br>• Titik didih campuran lebih tinggi daripada titik didih komponen murninya (Azeotrop Titik Didih Maksimum)"
        },
        "hints": {
            "concept": "Penyimpangan negatif terjadi jika interaksi A-B lebih kuat daripada A-A dan B-B. Atom H pada CHCl3 terpolarisasi positif kuat oleh 3 atom Cl, membentuk ikatan hidrogen dengan atom O pada aseton.",
            "execution": "Pilih penjelasan pembentukan ikatan hidrogen intermolekul A-B yang lebih kuat dari interaksi molekul murninya."
        }
    },
    {
        "id": "kim-sim-24",
        "materi": "RADIOKIMIA & PENANGGALAN PURBA",
        "topic": "Penanggalan Karbon-14 (Radiocarbon Dating) pada Fosil Kayu",
        "stem": "Suatu sampel kayu purba yang ditemukan di situs arkeologi megalitikum diuji aktivitas radiokarbon $^{14}\\text{C}$-nya ($T_{1/2} = 5730\\text{ tahun}$). Kayu hidup segar saat ini memiliki aktivitas spesifik $^{14}\\text{C}$ sebesar $15{,}3\\text{ desintegrasi per menit per gram karbon}$ ($15{,}3\\text{ dpm/g}$). Jika sampel kayu purba tersebut menunjukkan aktivitas radiokarbon sebesar $1{,}91\\text{ dpm/g}$, perkiraan usia sampel kayu purba tersebut adalah...",
        "correct": "$17.190\\text{ tahun}$, karena rasio aktivitas sampel purba terhadap kayu segar adalah $\\frac{A_t}{A_0} = \\frac{1{,}91}{15{,}3} = \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3$. Hal ini membuktikan bahwa sampel kayu telah meluruh selama $n = 3$ kali waktu paruh, sehingga usia kayu adalah $t = 3 \\times T_{1/2} = 3 \\times 5730 = 17.190\\text{ tahun}$.",
        "distractors": [
            "$11.460\\text{ tahun}$, dihitung jika aktivitas sampel diasumsikan telah meluruh sebesar dua kali waktu paruh (seperempat aktivitas awal).",
            "$5.730\\text{ tahun}$, dihitung jika aktivitas kayu purba diasumsikan tersisa separuh dari aktivitas awal.",
            "$22.920\\text{ tahun}$, dihitung jika kayu telah melewati 4 kali waktu paruh (seperenam belas aktivitas awal).",
            "$34.380\\text{ tahun}$, dihitung dari perkalian langsung faktor pembagi aktivitas dengan waktu paruh zat."
        ],
        "formula": {
            "title": "PENANGGALAN RADIOMETRIK KARBON-14",
            "latex": "\\frac{A_t}{A_0} = \\left(\\frac{1}{2}\\right)^{\\frac{t}{T_{1/2}}} \\implies \\frac{1{,}91}{15{,}3} = 0{,}1248 \\approx \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3 \\implies t = 3 \\times 5730 = 17.190\\text{ tahun}",
            "legend": "• Aktivitas awal kayu hidup: $A_0 = 15{,}3\\text{ dpm/g}$<br>• Aktivitas kayu purba terukur: $A_t = 1{,}91\\text{ dpm/g}$<br>• Fraksi sisa: $\\frac{1{,}91}{15{,}3} = \\frac{1}{8}$ ($n = 3$ siklus)<br>• Usia arkeologis: $17.190\\text{ tahun}$"
        },
        "hints": {
            "concept": "Hitung perbandingan aktivitas sisa terhadap awal: At / A0 = 1,91 / 15,3 = 1/8. Karena (1/2)^3 = 1/8, maka waktu yang berlalu adalah 3 kali waktu paruh.",
            "execution": "t = 3 * 5730 tahun = 17.190 tahun."
        }
    },
    {
        "id": "kim-sim-25",
        "materi": "REAKSI KONDENSASI SENYAWA KARBONIL",
        "topic": "Sintesis Dibenzalaseton Melalui Kondensasi Claisen-Schmidt",
        "stem": "Dalam sintesis zat penyerap sinar UV tabir surya dibenzalaseton, benzaldehida direaksikan dengan aseton dalam suasana basa encer ($\\text{NaOH}$) dengan perbandingan stoikiometri mol $2 : 1$ menurut reaksi kondensasi Claisen-Schmidt:<br>$2\\text{C}_6\\text{H}_5\\text{CHO} + \\text{CH}_3\\text{COCH}_3 \\xrightarrow{\\text{OH}^-} \\text{C}_6\\text{H}_5\\text{-CH=CH-CO-CH=CH-C}_6\\text{H}_5 + 2\\text{H}_2\\text{O}$<br>Alasan kimia mengapa benzaldehida tidak dapat melakukan kondensasi mandiri ($\\textit{self-condensation}$) melainkan hanya dapat bertindak sebagai elektrofil yang diserang oleh ion enolat aseton adalah...",
        "correct": "Molekul benzaldehida tidak memiliki atom hidrogen alfa ($\\alpha\\text{-H}$) pada karbon di sebelah gugus karbonilnya sehingga tidak dapat melepaskan proton untuk membentuk ion enolat; sebaliknya aseton memiliki enam atom $\\alpha\\text{-H}$ asam yang mudah dideprotonasi oleh basa $\\text{OH}^-$ membentuk nukleofil enolat penyerang.",
        "distractors": [
            "Cincin benzena benzaldehida bermuatan positif kuat yang menolak interaksi dengan molekul pelarut air.",
            "Gugus aldehida pada benzaldehida bersifat sangat basa sehingga menetralkan katalis NaOH sebelum reaksi dimulai.",
            "Molekul aseton tidak memiliki gugus karbonil sehingga hanya berperan sebagai pelarut inert tanpa ikut bereaksi.",
            "Benzaldehida memiliki titik didih yang terlalu rendah sehingga langsung menguap sebelum sempat membentuk ikatan karbon-karbon baru."
        ],
        "formula": {
            "title": "MEKANISME KONDENSASI CLAISEN-SCHMIDT (ALDOL SILANG)",
            "latex": "\\text{CH}_3\\text{COCH}_3 + \\text{OH}^- \\rightleftharpoons [\\text{CH}_2\\text{COCH}_3]^- + \\text{H}_2\\text{O}; \\quad \\text{Ar-CHO} + [\\text{CH}_2\\text{COCH}_3]^- \\rightarrow \\text{Ar-CH(OH)-CH}_2\\text{COCH}_3 \\xrightarrow{-\\text{H}_2\\text{O}} \\text{Dibenzalaseton}",
            "legend": "• Benzaldehida ($\text{C}_6\text{H}_5\text{CHO}$) tidak memiliki hidrogen alfa ($\alpha$-H)<br>• Aseton memiliki atom hidrogen alfa yang bersifat asam ($pK_a \\sim 20$)<br>• Deprotonasi aseton membentuk ion enolat yang bertindak sebagai nukleofil menyerang C karbonil benzaldehida"
        },
        "hints": {
            "concept": "Syarat pembentukan ion enolat adalah keberadaan hidrogen alfa (atom H yang terikat pada karbon di samping gugus C=O). Benzaldehida tidak punya H-alfa.",
            "execution": "Pilih jawaban yang menerangkan ketiadaan hidrogen alfa pada benzaldehida dan keberadaan H-alfa asam pada aseton."
        }
    },

    # -------------------------------------------------------------
    # 5 COMPLEX MULTI-SELECT HOTS (kim-sim-26 to kim-sim-30)
    # -------------------------------------------------------------
    {
        "id": "kim-sim-26",
        "type": "multi",
        "materi": "KIMIA HIJAU (GREEN CHEMISTRY)",
        "topic": "12 Prinsip Kimia Hijau dalam Desain Proses Kimia Lestari",
        "stem": "Prinsip Kimia Hijau ($\\textit{Green Chemistry}$) yang dirumuskan oleh Paul Anastas dan John Warner bertujuan merancang produk dan proses kimia yang meminimalkan atau meniadakan penggunaan serta pembentukan zat-zat berbahaya. Manakah TIGA pernyataan berikut yang merupakan implementasi nyata dari 12 Prinsip Kimia Hijau dalam industri manufaktur kimia modern? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Memprioritaskan pemanfaatan katalis selektif dibandingkan reagen stoikiometris konvensional untuk menurunkan kebutuhan energi dan mencegah produk samping limbah."},
            {"key": "B", "text": "Menggunakan bahan baku terbarukan (seperti biomassa tanaman) dibandingkan bahan baku tak terbarukan berbasis fosil minyak bumi."},
            {"key": "C", "text": "Merancang sintesis kimia dengan prinsip ekonomi atom maksimal sehingga persentase massa seluruh bahan baku terinkorporasi penuh ke dalam produk akhir yang diinginkan."},
            {"key": "D", "text": "Menggunakan pelarut organik klorinasi volatil (seperti kloroform dan karbon tetraklorida) dalam jumlah besar untuk mempercepat pendinginan reaktor."},
            {"key": "E", "text": "Meningkatkan pembentukan produk samping beracun asalkan proses pembuangan ke sungai dilakukan pada tengah malam saat tidak terpantau."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "12 PRINSIP UTAMA KIMIA HIJAU (ANASTAS & WARNER)",
            "latex": "\\text{Prinsip: Pencegahan Limbah} \\ | \\ \\text{Ekonomi Atom} \\ | \\ \\text{Katalisis} \\ | \\ \\text{Bahan Terbarukan} \\ | \\ \\text{Pelarut Ramah Lingkungan}",
            "legend": "• A BENAR: Prinsip Katalisis (Prinsip 9)<br>• B BENAR: Pemanfaatan Bahan Baku Terbarukan (Prinsip 7)<br>• C BENAR: Ekonomi Atom Maksimal (Prinsip 2)<br>• D SALAH: Bertentangan dengan Prinsip 5 (Pelarut dan zat penolong yang aman)<br>• E SALAH: Melanggar etika lingkungan dan Prinsip 1 (Pencegahan Limbah)"
        },
        "hints": {
            "concept": "Pahami 12 prinsip green chemistry: pencegahan limbah, ekonomi atom, sintesis lebih aman, bahan terbarukan, penggunaan katalis selektif, dan degradabilitas produk.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "kim-sim-27",
        "type": "multi",
        "materi": "KOROSI & PROTEKSI ELEKTROKIMIA",
        "topic": "Faktor Pemicu dan Mekanisme Pencegahan Korosi Logam Besi",
        "stem": "Korosi pada besi ($\\text{Fe}$) merupakan proses elektrokimia spontan yang merugikan secara ekonomi miliaran rupiah per tahun pada jembatan dan kapal laut. Manakah TIGA pernyataan berikut yang secara ilmiah BENAR mengenai mekanisme dan faktor-faktor yang mempengaruhi laju korosi pada besi? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Keberadaan gas oksigen ($\\text{O}_2$) dan air ($\\text{H}_2\\text{O}$) merupakan syarat mutlak terjadinya perkaratan; besi tidak akan berkarat di dalam air murni yang telah dididihkan dan diisolasi dari udara luar."},
            {"key": "B", "text": "Larutan elektrolit (seperti garam $\\text{NaCl}$ air laut) dan suasana asam ($pH < 7$) mempercepat laju korosi besi secara signifikan karena meningkatkan konduktivitas transfer ion dan potensial reduksi katoda."},
            {"key": "C", "text": "Pada metode proteksi katodik anoda korban, logam dengan potensial reduksi standar ($E^\\circ$) lebih negatif daripada besi (seperti $\\text{Mg}$ atau $\\text{Zn}$) dihubungkan ke struktur pipa besi sehingga logam tersebut teroksidasi lebih dahulu."},
            {"key": "D", "text": "Melapisi besi dengan logam tembaga ($\\text{Cu}$) memberikan perlindungan katodik permanen; jika lapisan tembaga tergores, besi justru akan semakin tahan terhadap karat."},
            {"key": "E", "text": "Besi akan terkorosi jauh lebih lambat jika dihubungkan secara kontak galvanik langsung dengan logam emas murni ($\\text{Au}$)."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "MEKANISME ELEKTROKIMIA PERKARATAN BESI",
            "latex": "\\text{Anoda: } \\text{Fe} \\rightarrow \\text{Fe}^{2+} + 2e^-; \\quad \\text{Katoda: } \\text{O}_2 + 4\\text{H}^+ + 4e^- \\rightarrow 2\\text{H}_2\\text{O} \\ (\\text{atau } \\text{O}_2 + 2\\text{H}_2\\text{O} + 4e^- \\rightarrow 4\\text{OH}^-)",
            "legend": "• A BENAR: Air dan oksigen adalah reaktan redoks esensial pembentuk karat $\\text{Fe}_2\\text{O}_3\\cdot x\\text{H}_2\\text{O}$<br>• B BENAR: Elektrolit mempercepat jembatan garam mikro, asam menambah spesi pengoksidasi $\\text{H}^+$<br>• C BENAR: Logam Mg ($E^\\circ = -2{,}37\\text{ V}$) dan Zn ($-0{,}76\\text{ V}$) lebih mudah teroksidasi dari Fe ($-0{,}44\\text{ V}$)<br>• D dan E SALAH: Logam Cu ($+0{,}34\\text{ V}$) dan Au ($+1{,}50\\text{ V}$) memiliki $E^\\circ$ lebih positif; jika tergores, Fe menjadi anoda yang terkorosi jauh lebih cepat"
        },
        "hints": {
            "concept": "Syarat korosi besi: H2O dan O2. Elektrolit dan asam mempercepat korosi. Anoda korban harus memiliki E-nol lebih negatif dari besi (Mg atau Zn). Logam mulia (Cu, Au) justru mempercepat korosi jika lapisan tergores.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "kim-sim-28",
        "type": "multi",
        "materi": "TERMODINAMIKA & ENTROPI SISTEM",
        "topic": "Proses-Proses Fisis dan Kimia yang Menghasilkan Kenaikan Entropi",
        "stem": "Entropi ($S$) adalah besaran termodinamika yang mengukur derajat ketidakteraturan molekuler atau dispersi energi dalam suatu sistem. Manakah TIGA proses kimia atau fisis berikut yang menghasilkan perubahan entropi sistem bertanda positif ($\\Delta S_{\\text{sistem}} > 0$)? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Sublimasi dry ice (karbon dioksida padat) menjadi gas karbon dioksida: $\\text{CO}_2(s) \\rightarrow \\text{CO}_2(g)$."},
            {"key": "B", "text": "Reaksi peruraian termal batu kapur menghasilkan gas: $\\text{CaCO}_3(s) \\rightarrow \\text{CaO}(s) + \\text{CO}_2(g)$."},
            {"key": "C", "text": "Pelarutan kristal garam dapur di dalam air murni: $\\text{NaCl}(s) \\xrightarrow{\\text{H}_2\\text{O}} \\text{Na}^+(aq) + \\text{Cl}^-(aq)$."},
            {"key": "D", "text": "Pengembunan uap air menjadi tetesan air hujan pada pembentukan awan: $\\text{H}_2\\text{O}(g) \\rightarrow \\text{H}_2\\text{O}(l)$."},
            {"key": "E", "text": "Pembentukan kristal es dari air cair pada freezer lemari es: $\\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{O}(s)$."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "PRINSIP PENINGKATAN ENTROPI SISTEM",
            "latex": "\\Delta S_{\\text{sistem}} > 0 \\iff S_{\\text{gas}} \\gg S_{\\text{cair}} > S_{\\text{padat}}; \\quad \\Delta n_{\\text{gas}} > 0",
            "legend": "• A BENAR: Perubahan fasa padat $\\rightarrow$ gas menghasilkan kenaikan ruang gerak partikel sangat masif ($\\Delta S > 0$)<br>• B BENAR: Reaksi menghasilkan mol gas dari zat padat murni ($\\Delta n_g = +1 > 0$)<br>• C BENAR: Pembongkaran kisi kristal teratur menjadi ion-ion terlarut acak ($\\Delta S > 0$)<br>• D dan E SALAH: Kondensasi dan pembekuan menurunkan ketidakteraturan partikel ($\\Delta S < 0$)"
        },
        "hints": {
            "concept": "Entropi naik (Delta S > 0) jika: jumlah mol gas bertambah, terjadi transisi fasa padat -> cair -> gas, atau pelarutan kristal padat menjadi ion larutan.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "kim-sim-29",
        "type": "multi",
        "materi": "MAKROMOLEKUL & STRUKTUR PROTEIN",
        "topic": "Interaksi Kimia Penstabil Struktur Tersier dan Kuaterner Protein",
        "stem": "Struktur konformasi 3D aktif (tertier dan kuaterner) suatu protein enzim sangat menentukan fungsi biologisnya. Kerusakan konformasi ini mengakibatkan denaturasi protein. Manakah TIGA jenis interaksi kimia berikut yang secara langsung bertanggung jawab menstabilkan pelipatan struktur tersier rantai polipeptida protein? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Jembatan disulfida (ikatan kovalen $-\\text{S}-\\text{S}-$) yang terbentuk dari oksidasi gugus tiol antara dua residu asam amino sistein."},
            {"key": "B", "text": "Jembatan garam (ikatan ionik / interaksi elektrostatik) antara gugus samping bermuatan positif (seperti lisin/arginin) dengan gugus samping bermuatan negatif (seperti aspartat/glutamat)."},
            {"key": "C", "text": "Interaksi hidrofobik antarrantai samping nonpolar (seperti valin, leusin, fenilalanin) yang cenderung berkumpul menjauhi pelarut air di inti bagian dalam molekul protein."},
            {"key": "D", "text": "Ikatan logam radioaktif antara gugus amida dengan radikal bebas isotop kalium."},
            {"key": "E", "text": "Pembentukan ikatan kovalen rangkap tiga antara seluruh karbon alfa di sepanjang rantai utama."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "GAYA PENSTABIL KONFORMASI TERSIER PROTEIN",
            "latex": "\\text{Stabilisasi 3D} = \\text{Jembatan Disulfida } (-\\text{S-S}-) + \\text{Jembatan Garam } (-\\text{NH}_3^+ \\cdots ^-\\text{OOC}-) + \\text{Gaya Hidrofobik} + \\text{Ikatan H}",
            "legend": "• A BENAR: Jembatan disulfida adalah satu-satunya ikatan kovalen penstabil struktur tersier<br>• B BENAR: Jembatan garam adalah atraksi ionik antar residu bermuatan lawan<br>• C BENAR: Gaya penggerak utama pelipatan protein dalam lingkungan akuatik sel<br>• D dan E adalah opsi nonsens tanpa dasar biokimia"
        },
        "hints": {
            "concept": "Empat interaksi penstabil struktur tersier protein: jembatan disulfida (-S-S-), jembatan garam (ionik), interaksi hidrofobik gugus nonpolar, dan ikatan hidrogen.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "kim-sim-30",
        "type": "multi",
        "materi": "KIMIA UNSUR TRANSISI PERIODE 4",
        "topic": "Sifat Khas Fisika dan Kimia Logam Transisi Periode 4",
        "stem": "Unsur-unsur transisi periode 4 (dari skandium hingga tembaga) memiliki karakteristik khas yang membedakannya secara tajam dari unsur-unsur golongan utama (blok s dan blok p). Manakah TIGA sifat karakteristik berikut yang merupakan sifat khas yang dimiliki oleh sebagian besar unsur transisi periode keempat? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Mampu memiliki lebih dari satu bilangan oksidasi (tingkat oksidasi bervariasi) dalam berbagai senyawanya, seperti $\\text{Mn}$ yang memiliki biloks $+2, +3, +4, +6,$ dan $+7$."},
            {"key": "B", "text": "Membentuk ion-ion kompleks koordinasi yang seringkali berwarna cerah akibat eksitasi elektron transisi orbital $d-d$ pada penyerapan spektrum cahaya tampak."},
            {"key": "C", "text": "Banyak unsur dan senyawanya yang memiliki sifat paramagnetik (ditarik medan magnet) karena memiliki satu atau lebih elektron tak berpasangan pada subkulit $3d$."},
            {"key": "D", "text": "Selalu membentuk ikatan ionik murni dan tidak pernah mampu membentuk ikatan kovalen koordinasi dengan molekul netral."},
            {"key": "E", "text": "Semua logam transisi memiliki massa jenis yang lebih rendah daripada air murni sehingga selalu terapung di permukaan danau."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "KARAKTERISTIK SUBKULIT 3D LOGAM TRANSISI",
            "latex": "\\text{Konfigurasi: } [\\text{Ar}] 4s^2 3d^n; \\quad \\Delta E = h\\nu \\text{ (transisi } d-d); \\quad \\mu_s = \\sqrt{n(n+2)} \\text{ BM}",
            "legend": "• A BENAR: Tingkat energi orbital $4s$ dan $3d$ sangat berdekatan sehingga elektron pada kedua subkulit dapat dilepaskan bertahap<br>• B BENAR: Pembelahan medan kristal ($\\Delta_o$ atau $\\Delta_t$) menyerap foton tampak memunculkan warna komplementer<br>• C BENAR: Momen magnet spin elektron tak berpasangan $\\implies$ paramagnetik / feromagnetik<br>• D SALAH: Logam transisi justru merupakan pembentuk senyawa koordinasi kovalen terbaik<br>• E SALAH: Logam transisi memiliki massa jenis tinggi ($> 3\\text{ g/cm}^3$)"
        },
        "hints": {
            "concept": "Sifat khas logam transisi periode 4: biloks bervariasi, senyawa kompleks berwarna (transisi d-d), memiliki sifat paramagnetik (elektron 3d tak berpasangan), dan berfungsi sebagai katalis.",
            "execution": "Pilih A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH HOTS (kim-sim-31 to kim-sim-35)
    # -------------------------------------------------------------
    {
        "id": "kim-sim-31",
        "type": "matrix",
        "materi": "TERMODINAMIKA & KESETIMBANGAN KIMIA",
        "topic": "Prinsip Energi Bebas Gibbs dan Kesetimbangan Termodinamika",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai Energi Bebas Gibbs, Entalpi, dan Kesetimbangan Kimia!",
        "statements": [
            {
                "text": "Jika suatu reaksi kimia memiliki Delta H bernilai negatif (eksotermik) dan Delta S bernilai positif (entropi meningkat), maka reaksi tersebut pasti berlangsung spontan pada segala suhu (Delta G selalu negatif).",
                "correct": True
            },
            {
                "text": "Pada kondisi kesetimbangan kimia dinamis pada suhu dan tekanan konstan, nilai perubahan energi bebas Gibbs sistem bernilai nol (Delta G = 0).",
                "correct": True
            },
            {
                "text": "Jika nilai tetapan kesetimbangan suatu reaksi K > 1, maka nilai perubahan energi bebas Gibbs standar reaksi tersebut (Delta G nol) selalu bertanda positif.",
                "correct": False
            },
            {
                "text": "Katalis dapat mengubah nilai perubahan energi bebas Gibbs standar (Delta G nol) sehingga mampu mengubah reaksi non-spontan menjadi reaksi spontan.",
                "correct": False
            }
        ],
        "formula": {
            "title": "PRINSIP ENERGI BEBAS GIBBS & KESETIMBANGAN",
            "latex": "\\Delta G = \\Delta H - T\\Delta S; \\quad \\Delta G = 0 \\text{ (saat setimbang)}; \\quad \\Delta G^\\circ = -RT \\ln K",
            "legend": "• Pernyataan 1 BENAR: $\\Delta H < 0$ dan $\\Delta S > 0 \\implies \\Delta G = (-) - T(+) < 0$ pada semua $T$<br>• Pernyataan 2 BENAR: Kriteria kesetimbangan termodinamika sistem tertutup adalah $\\Delta G = 0$<br>• Pernyataan 3 SALAH: Karena $\\Delta G^\\circ = -RT \\ln K$, jika $K > 1$ maka $\\ln K > 0$ sehingga $\\Delta G^\\circ < 0$ (negatif)<br>• Pernyataan 4 SALAH: Katalis hanya menurunkan energi aktivasi ($E_a$), tidak mempengaruhi fungsi keadaan termodinamika $\\Delta G^\\circ$"
        },
        "hints": {
            "concept": "Pahami rumus Delta G = Delta H - T*Delta S dan Delta G0 = -RT ln K. Saat setimbang Delta G = 0. Katalis TIDAK pernah mengubah Delta G atau kesetimbangan K.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
        }
    },
    {
        "id": "kim-sim-32",
        "type": "matrix",
        "materi": "TEORI ASAM-BASA & HSAB",
        "topic": "Konsep Asam-Basa Lewis, Brønsted-Lowry, dan Prinsip HSAB",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai teori asam-basa modern dan interaksi kation-anion!",
        "statements": [
            {
                "text": "Menurut teori Lewis, suatu basa didefinisikan sebagai spesi kimia yang bertindak sebagai donor pasangan elektron bebas untuk membentuk ikatan kovalen koordinasi.",
                "correct": True
            },
            {
                "text": "Molekul boron trifluorida (BF3) bertindak sebagai asam Lewis kuat karena atom boron memiliki orbital p kosong yang belum memenuhi kaidah oktet.",
                "correct": True
            },
            {
                "text": "Semakin kuat suatu asam Brønsted-Lowry, maka basa konjugasi yang dihasilkannya akan memiliki kekuatan kebasaan yang semakin kuat pula.",
                "correct": False
            },
            {
                "text": "Menurut prinsip HSAB (Hard and Soft Acids and Bases), asam keras (seperti Al3+ atau Ti4+) cenderung lebih stabil berikatan dengan basa lunak (seperti ion I- atau fosfina R3P).",
                "correct": False
            }
        ],
        "formula": {
            "title": "TEORI ASAM BASA LEWIS & PRINSIP PEARSON (HSAB)",
            "latex": "\\text{Asam Lewis: Akseptor PEB}; \\quad \\text{Basa Lewis: Donor PEB}; \\quad \\text{Hard-Hard & Soft-Soft Preference}",
            "legend": "• Pernyataan 1 BENAR: Definisi resmi asam-basa Lewis<br>• Pernyataan 2 BENAR: Boron pada $\\text{BF}_3$ hanya dikelilingi 6 elektron (hipovalen, ada orbital $2p$ kosong)<br>• Pernyataan 3 SALAH: Asam sangat kuat memiliki basa konjugasi yang sangat lemah (stabil)<br>• Pernyataan 4 SALAH: Prinsip HSAB menyatakan asam keras menyukai basa keras (gaya ionik), dan asam lunak menyukai basa lunak (gaya kovalen)"
        },
        "hints": {
            "concept": "Basa Lewis = donor PEB, Asam Lewis = akseptor PEB. Asam kuat punya basa konjugasi sangat lemah. Prinsip HSAB: Keras-Keras dan Lunak-Lunak.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
        }
    },
    {
        "id": "kim-sim-33",
        "type": "matrix",
        "materi": "KINETIKA KIMIA & TEORI TUMBUKAN",
        "topic": "Energi Aktivasi, Persamaan Arrhenius, dan Katalisis",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai laju reaksi dan mekanisme katalis kimia!",
        "statements": [
            {
                "text": "Kenaikan suhu reaksi mempercepat laju reaksi terutama karena meningkatkan fraksi molekul reaktan yang memiliki energi kinetik melampaui energi aktivasi (Ea).",
                "correct": True
            },
            {
                "text": "Nilai energi aktivasi (Ea) suatu reaksi kimia selalu berbanding lurus dengan perubahan entalpi reaksi (Delta H).",
                "correct": False
            },
            {
                "text": "Penambahan katalis mempercepat tercapainya keadaan setimbang dengan cara menyediakan jalur mekanisme reaksi alternatif yang memiliki energi aktivasi lebih rendah.",
                "correct": True
            },
            {
                "text": "Katalis heterogen (seperti serbuk platina padat pada reaksi fasa gas) bekerja dengan cara mengadsorpsi molekul reaktan pada permukaannya sehingga melemahkan ikatan kimia reaktan.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PERSAMAAN ARRHENIUS & TEORI TUMBUKAN",
            "latex": "k = A e^{-E_a/RT}; \\quad f = e^{-E_a/RT} \\text{ (fraksi molekul berenergi } \\ge E_a); \\quad E_a \\text{ independen dari } \\Delta H",
            "legend": "• Pernyataan 1 BENAR: Penjelasan distribusi Boltzmann Maxwell (fraksi molekul efektif naik)<br>• Pernyataan 2 SALAH: Energi aktivasi adalah rintangan kinetika transisi, sedangkan $\\Delta H$ adalah selisih termodinamika keadaan awal dan akhir<br>• Pernyataan 3 BENAR: Definisi fungsi kerja katalis<br>• Pernyataan 4 BENAR: Mekanisme adsorpsi fisiosorpsi/kemisorpsi pada katalisis heterogen"
        },
        "hints": {
            "concept": "Suhu menaikkan fraksi partikel dengan energi >= Ea. Ea tidak berhubungan langsung dengan Delta H. Katalis menurunkan Ea melalui mekanisme alternatif (adsorpsi pada permukaan katalis heterogen).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "kim-sim-34",
        "type": "matrix",
        "materi": "ELEKTROKIMIA & SEL ELEKTROLISIS",
        "topic": "Hukum Faraday, Elektrolisis Larutan, dan Potensial Sel",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai elektrokimia sel volta dan elektrolisis!",
        "statements": [
            {
                "text": "Pada elektrolisis larutan NaCl encer menggunakan elektroda karbon inert, gas yang dihasilkan di kutub katoda adalah gas hidrogen (H2), bukan endapan logam natrium.",
                "correct": True
            },
            {
                "text": "Menurut Hukum Faraday I, massa zat yang diendapkan pada elektroda berbanding lurus dengan muatan listrik total (kuat arus dikali waktu) yang dialirkan ke dalam sel.",
                "correct": True
            },
            {
                "text": "Reaksi redoks dalam sel volta berlangsung spontan dengan potensial sel standar selalu bertanda negatif (E sel nol < 0).",
                "correct": False
            },
            {
                "text": "Pada proses pemurnian tembaga kotor (electrorefining), logam tembaga kotor dipasang sebagai katoda sedangkan tembaga murni dipasang sebagai anoda.",
                "correct": False
            }
        ],
        "formula": {
            "title": "HUKUM ELEKTROKIMIA & ATURAN ELEKTROLISIS",
            "latex": "w = \\frac{e \\cdot i \\cdot t}{96500}; \\quad \\Delta G^\\circ = -n F E_{\\text{sel}}^\\circ < 0 \\implies E_{\\text{sel}}^\\circ > 0 \\text{ (spontan)}",
            "legend": "• Pernyataan 1 BENAR: Logam aktif Golongan IA ($E^\\circ = -2{,}71\\text{ V}$) kalah bersaing dengan air ($E^\\circ = -0{,}83\\text{ V}$), sehingga air tereduksi menjadi $\\text{H}_2$<br>• Pernyataan 2 BENAR: Hukum Faraday I ($w \\propto Q = I \\cdot t$)<br>• Pernyataan 3 SALAH: Sel volta spontan memiliki $E_{\\text{sel}}^\\circ > 0$ (positif)<br>• Pernyataan 4 SALAH: Tembaga kotor harus dioksidasi di ANODA, dan tembaga murni mengendap di KATODA"
        },
        "hints": {
            "concept": "Di katoda larutan NaCl: air tereduksi menjadi H2 karena E0 reduksi Na sangat negatif. Faraday I: w ~ I*t. Sel volta spontan E0_sel > 0. Electrorefining Cu: anoda = Cu kotor, katoda = Cu murni.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
        }
    },
    {
        "id": "kim-sim-35",
        "type": "matrix",
        "materi": "IKATAN KIMIA & GAYA ANTARMOLEKUL",
        "topic": "Hibridisasi Orbital, Geometri Molekul, dan Gaya Antarmolekul",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai struktur ikatan kovalen dan interaksi antarmolekul!",
        "statements": [
            {
                "text": "Molekul metana (CH4) memiliki hibridisasi sp3 pada atom pusat C dengan bentuk geometri molekul tetrahedral sempurna dan sudut ikatan 109,5 derajat.",
                "correct": True
            },
            {
                "text": "Molekul air (H2O) memiliki sudut ikatan H-O-H sekitar 104,5 derajat (lebih kecil dari sudut tetrahedral ideal) akibat tolakan kuat dari dua pasangan elektron bebas pada atom oksigen.",
                "correct": True
            },
            {
                "text": "Ikatan kovalen rangkap dua (C=C) selalu tersusun dari dua buah ikatan pi yang terbentuk dari tumpang tindih orbital sisi-ke-sisi.",
                "correct": False
            },
            {
                "text": "Kekuatan gaya dispersi London antara molekul-molekul nonpolar meningkat seiring bertambahnya massa molar dan ukuran awan elektron molekul tersebut.",
                "correct": True
            }
        ],
        "formula": {
            "title": "TEORI VSEPR & HIBRIDISASI VALENSI",
            "latex": "\\text{Ikatan Rangkap 2 } (\\text{C=C}) = 1\\sigma + 1\\pi; \\quad \\text{Tolakan: PEB-PEB} > \\text{PEB-PEI} > \\text{PEI-PEI}",
            "legend": "• Pernyataan 1 BENAR: Metana memiliki 4 domain ikatan (hibridisasi $sp^3$, tetrahedral sempurna $109{,}5^\\circ$)<br>• Pernyataan 2 BENAR: Air memiliki 2 PEI dan 2 PEB; tolakan PEB mendistorsi sudut menjadi $104{,}5^\\circ$<br>• Pernyataan 3 SALAH: Ikatan rangkap dua terdiri atas 1 ikatan sigma ($\\sigma$) dan 1 ikatan pi ($\\pi$), bukan dua ikatan pi<br>• Pernyataan 4 BENAR: Awan elektron yang lebih besar lebih mudah dipolarisasikan (daya dispersi meningkat)"
        },
        "hints": {
            "concept": "CH4 tetrahedral sp3 (109,5). H2O sudut menyusut jadi 104,5 karena tolakan 2 PEB. Ikatan rangkap 2 = 1 sigma + 1 pi. Gaya London makin kuat jika Mr dan awan elektron makin besar.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    }
]
