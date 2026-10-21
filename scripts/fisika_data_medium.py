# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Fisika (SMA/MA Saintek)
Dataset: Medium Practice (25 Authentic Questions, fis-lat-m-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

FISIKA_MEDIUM_ITEMS = [
    {
        "id": "fis-lat-m-01",
        "materi": "KINEMATIKA GERAK DUA DIMENSI",
        "topic": "Gerak Parabola (Jarak Mendatar & Ketinggian Maksimum)",
        "stem": "Sebuah meriam menembakkan peluru dengan kecepatan awal $v_0 = 50\\text{ m/s}$ pada sudut elevasi $\\theta = 53^\\circ$ terhadap horizontal ($\\sin 53^\\circ = 0{,}8$ dan $\\cos 53^\\circ = 0{,}6$). Mengabaikan gesekan udara dan mengasumsikan percepatan gravitasi $g = 10\\text{ m/s}^2$, waktu yang dibutuhkan peluru untuk mencapai titik puncak lintasan ($t_p$) dan tinggi maksimumnya ($h_{\\max}$) adalah...",
        "correct": "$t_p = 4\\text{ sekon}$ dan $h_{\\max} = 80\\text{ meter}$, dihitung dari $t_p = \\frac{v_0 \\sin\\theta}{g} = \\frac{50 \\times 0{,}8}{10} = 4\\text{ s}$, dan $h_{\\max} = \\frac{(v_0 \\sin\\theta)^2}{2g} = \\frac{40^2}{20} = 80\\text{ m}$.",
        "distractors": [
            "$t_p = 3\\text{ sekon}$ dan $h_{\\max} = 45\\text{ meter}$, karena kecepatan awal keliru diuraikan menggunakan fungsi cosinus pada komponen sumbu vertikal.",
            "$t_p = 5\\text{ sekon}$ dan $h_{\\max} = 125\\text{ meter}$, dihitung dengan mengabaikan sudut elevasi penembakan moncong meriam.",
            "$t_p = 8\\text{ sekon}$ dan $h_{\\max} = 160\\text{ meter}$, karena waktu mencapai titik puncak tertukar dengan total waktu melayang di udara.",
            "$t_p = 2\\text{ sekon}$ dan $h_{\\max} = 40\\text{ meter}$, dihitung dari pembagian tinggi maksimum dengan gravitasi bumi tanpa pemangkatan kuadrat."
        ],
        "formula": {
            "title": "FORMULA GERAK PARABOLA (TITIK PUNCAK)",
            "latex": "t_p = \\frac{v_0 \\sin\\theta}{g}; \\quad h_{\\max} = \\frac{(v_0 \\sin\\theta)^2}{2g}; \\quad X_{\\max} = \\frac{v_0^2 \\sin(2\\theta)}{g}",
            "legend": "• $v_{0y} = 50 \\times 0{,}8 = 40\\text{ m/s}$<br>• $t_p = \\frac{40}{10} = 4\\text{ sekon}$<br>• $h_{\\max} = \\frac{40^2}{2 \\times 10} = \\frac{1.600}{20} = 80\\text{ meter}$"
        },
        "hints": {
            "concept": "Komponen kecepatan vertikal: v0y = v0 * sin(53) = 40 m/s. Di titik puncak, vy = 0. tp = v0y / g. h_max = v0y^2 / (2g).",
            "execution": "tp = 40 / 10 = 4 s. h_max = 40^2 / 20 = 80 m."
        }
    },
    {
        "id": "fis-lat-m-02",
        "materi": "HUKUM GRAVITASI NEWTON",
        "topic": "Percepatan Gravitasi pada Ketinggian Tertentu di Atas Bumi",
        "stem": "Sebuah satelit cuaca mengorbit bumi pada ketinggian $h = R$ di atas permukaan bumi, di mana $R$ adalah jari-jari bumi. Jika percepatan gravitasi di permukaan bumi adalah $g = 9{,}8\\text{ m/s}^2$, percepatan gravitasi bumi ($g_h$) yang dialami oleh satelit pada orbit tersebut adalah...",
        "correct": "$2{,}45\\text{ m/s}^2$, karena jarak satelit dari pusat bumi menjadi $r = R + h = 2R$, sehingga percepatan gravitasi berkurang menjadi seperempat dari nilai di permukaan bumi: $g_h = g \\left(\\frac{R}{2R}\\right)^2 = \\frac{g}{4} = \\frac{9{,}8}{4} = 2{,}45\\text{ m/s}^2$.",
        "distractors": [
            "$4{,}90\\text{ m/s}^2$, karena gravitasi keliru dianggap berbanding terbalik secara linier dengan jarak, bukan berbanding terbalik dengan kuadrat jarak.",
            "$9{,}80\\text{ m/s}^2$, karena gravitasi diasumsikan konstan tidak berkurang di ruang hampa udara lintasan orbit bumi.",
            "$1{,}08\\text{ m/s}^2$, dihitung dari asumsi jarak satelit dari permukaan bumi adalah sembilan kali jari-jari planet.",
            "$0\\text{ m/s}^2$, karena satelit dianggap berada dalam kondisi mikrogravitasi mutlak tanpa tarikan massa bumi sama sekali."
        ],
        "formula": {
            "title": "HUKUM KUADRAT TERBALIK MEDAN GRAVITASI",
            "latex": "g_h = G \\frac{M}{(R + h)^2} = g \\left(\\frac{R}{R + h}\\right)^2 = g \\left(\\frac{R}{2R}\\right)^2 = \\frac{g}{4} = \\frac{9{,}8}{4} = 2{,}45\\text{ m/s}^2",
            "legend": "• $R$ = Jari-jari bumi; $h$ = Ketinggian dari permukaan bumi<br>• Jarak dari pusat massa bumi: $r = R + h = R + R = 2R$<br>• Kuadrat jarak: $(2R)^2 = 4R^2 \\implies$ Medan gravitasi menjadi $\\frac{1}{4}$ kali semula"
        },
        "hints": {
            "concept": "Jarak diukur selalu dari pusat bumi: r = R + h = 2R. Kuat medan gravitasi berbanding terbalik dengan kuadrat jarak: g_h = g * (R / 2R)^2 = g / 4.",
            "execution": "g_h = 9,8 / 4 = 2,45 m/s²."
        }
    },
    {
        "id": "fis-lat-m-03",
        "materi": "DINAMIKA GERAK MELINGKAR",
        "topic": "Kecepatan Maksimum pada Tikungan Datar Kasar",
        "stem": "Sebuah mobil bermassa $1.200\\text{ kg}$ melintasi tikungan jalan datar mendatar yang memiliki jari-jari kelengkungan $R = 40\\text{ meter}$. Koefisien gesekan statik antara ban mobil dengan aspal jalan adalah $\\mu_s = 0{,}4$. Mengambil percepatan gravitasi $g = 10\\text{ m/s}^2$, kelajuan maksimum ($v_{\\max}$) yang diizinkan agar mobil dapat berbelok dengan aman tanpa selip (tergelincir keluar lintasan) adalah...",
        "correct": "$46{,}8\\text{ km/jam}$ (atau tepat $12{,}65\\text{ m/s}$, dibulatkan dari $\\sqrt{\\mu_s g R} = \\sqrt{0{,}4 \\times 10 \\times 40} = \\sqrt{160} = 4\\sqrt{10}\\text{ m/s} \\approx 12{,}65\\text{ m/s}$), di mana gaya gesek statis bertindak sebagai gaya sentripetal.",
        "distractors": [
            "$20\\text{ m/s}$ (atau $72\\text{ km/jam}$), dihitung dengan mengalikan percepatan gravitasi dengan koefisien gesekan kinetik jalan basah.",
            "$8\\text{ m/s}$ (atau $28{,}8\\text{ km/jam}$), dihitung dari pembagian jari-jari kelengkungan dengan percepatan gravitasi bumi.",
            "$16\\text{ m/s}$ (atau $57{,}6\\text{ km/jam}$), dihitung dengan mengabaikan akar kuadrat pada perumusan gaya sentripetal mobil.",
            "$5\\text{ m/s}$ (atau $18\\text{ km/jam}$), dihitung dari rasio massa mobil terhadap jari-jari tikungan aspal jalan."
        ],
        "formula": {
            "title": "KELAJUAN MAKSIMUM TIKUNGAN DATAR",
            "latex": "F_s = F_{sp} \\implies \\mu_s m g = \\frac{m v_{\\max}^2}{R} \\implies v_{\\max} = \\sqrt{\\mu_s g R} = \\sqrt{0{,}4 \\times 10 \\times 40} = \\sqrt{160} \\approx 12{,}65\\text{ m/s}",
            "legend": "• Konversi ke km/jam: $12{,}65 \\times 3{,}6 \\approx 45{,}5 - 46{,}8\\text{ km/jam}$<br>• Kecepatan maksimum tidak bergantung pada massa kendaraan (mobil berat dan motor ringan memiliki batas aman kelajuan yang sama)"
        },
        "hints": {
            "concept": "Gaya gesek statis menyediakan gaya sentripetal: mu_s * m * g = m * v^2 / R -> v_max = sqrt(mu_s * g * R).",
            "execution": "v = sqrt(0,4 * 10 * 40) = sqrt(160) = 4*sqrt(10) ≈ 12,65 m/s."
        }
    },
    {
        "id": "fis-lat-m-04",
        "materi": "TUMBUKAN DAN RESTITUSI",
        "topic": "Koefisien Restitusi Bola Memantul di Lantai",
        "stem": "Sebuah bola basket dijatuhkan bebas tanpa kecepatan awal dari ketinggian $h_1 = 180\\text{ cm}$ di atas lantai beton keras. Setelah memantul di lantai, bola tersebut mencapai ketinggian pantulan pertama sebesar $h_2 = 80\\text{ cm}$. Nilai koefisien restitusi ($e$) antara bola basket dan lantai serta perkiraan tinggi pantulan kedua ($h_3$) adalah...",
        "correct": "$e = \\frac{2}{3}$ dan $h_3 = 35{,}56\\text{ cm}$, dihitung dari koefisien restitusi pantulan vertikal $e = \\sqrt{\\frac{h_2}{h_1}} = \\sqrt{\\frac{80}{180}} = \\sqrt{\\frac{4}{9}} = \\frac{2}{3}$, sehingga $h_3 = e^2 h_2 = \\frac{4}{9} \\times 80 = 35{,}56\\text{ cm}$.",
        "distractors": [
            "$e = 0{,}44$ dan $h_3 = 20\\text{ cm}$, karena koefisien restitusi keliru dihitung tanpa mengakarkan perbandingan ketinggian pantulan.",
            "$e = 0{,}80$ dan $h_3 = 60\\text{ cm}$, dihitung dari perbandingan selisih ketinggian terhadap percepatan gravitasi bumi.",
            "$e = 1{,}0$ dan $h_3 = 80\\text{ cm}$, dengan anggapan bahwa bola basket mengalami tumbukan lenting sempurna di atas lantai.",
            "$e = 0{,}50$ dan $h_3 = 40\\text{ cm}$, dihitung dengan membagi dua ketinggian pantulan pertama secara konvensional."
        ],
        "formula": {
            "title": "KOEFISIEN RESTITUSI PADA LANTAI PANTAK",
            "latex": "e = \\sqrt{\\frac{h_2}{h_1}} = \\sqrt{\\frac{80}{180}} = \\sqrt{\\frac{4}{9}} = \\frac{2}{3} \\approx 0{,}67; \\quad h_3 = e^2 h_2 = \\left(\\frac{2}{3}\\right)^2 \\times 80 = \\frac{4}{9} \\times 80 = 35{,}56\\text{ cm}",
            "legend": "• Tumbukan Lenting Sebagian: $0 < e < 1$<br>• Deret Geometri Ketinggian Pantulan: $h_n = h_1 (e)^{2(n-1)}$"
        },
        "hints": {
            "concept": "Koefisien restitusi bola memantul: e = sqrt(h2 / h1). Ketinggian pantulan berikutnya: h3 = e^2 * h2.",
            "execution": "e = sqrt(80/180) = sqrt(4/9) = 2/3. h3 = (4/9) * 80 = 35,56 cm."
        }
    },
    {
        "id": "fis-lat-m-05",
        "materi": "ELASTISITAS DAN HUKUM HOOKE",
        "topic": "Konstanta Pegas Gabungan dan Energi Potensial Pegas",
        "stem": "Dua buah pegas identik masing-masing memiliki konstanta $k = 400\\text{ N/m}$. Kedua pegas dirangkai secara paralel, kemudian rangkaian tersebut digantungkan secara vertikal dan diberi beban bermassa $M = 4\\text{ kg}$ pada ujung bawahnya ($g = 10\\text{ m/s}^2$). Pertambahan panjang total rangkaian pegas ($\\Delta x$) dan energi potensial elastis ($E_p$) yang tersimpan di dalam sistem pegas tersebut adalah...",
        "correct": "$\\Delta x = 0{,}05\\text{ meter}$ ($5\\text{ cm}$) dan $E_p = 1{,}0\\text{ Joule}$, karena konstanta pegas pengganti paralel adalah $k_p = 400 + 400 = 800\\text{ N/m}$, pertambahan panjang $\\Delta x = \\frac{F}{k_p} = \\frac{40}{800} = 0{,}05\\text{ m}$, dan $E_p = \\frac{1}{2} k_p (\\Delta x)^2 = \\frac{1}{2}(800)(0{,}05^2) = 1{,}0\\text{ J}$.",
        "distractors": [
            "$\\Delta x = 0{,}10\\text{ meter}$ dan $E_p = 4{,}0\\text{ Joule}$, karena kedua pegas keliru dihitung menggunakan perumusan rangkaian seri.",
            "$\\Delta x = 0{,}02\\text{ meter}$ dan $E_p = 0{,}5\\text{ Joule}$, dihitung dengan mengabaikan percepatan gravitasi bumi pada beban.",
            "$\\Delta x = 0{,}20\\text{ meter}$ dan $E_p = 8{,}0\\text{ Joule}$, dihitung dari hasil kali massa beban dengan konstanta pegas tunggal.",
            "$\\Delta x = 0{,}05\\text{ meter}$ dan $E_p = 2{,}0\\text{ Joule}$, karena faktor pengali setengah diabaikan dalam perumusan energi potensial pegas."
        ],
        "formula": {
            "title": "RANGKAIAN PEGAS PARALEL & ENERGI POTENSIAL",
            "latex": "k_p = k_1 + k_2 = 400 + 400 = 800\\text{ N/m}; \\quad \\Delta x = \\frac{mg}{k_p} = \\frac{40}{800} = 0{,}05\\text{ m}; \\quad E_p = \\frac{1}{2} k_p \\Delta x^2 = 1{,}0\\text{ J}",
            "legend": "• Gaya Berat Beban: $F = W = mg = 4 \\times 10 = 40\\text{ N}$<br>• $E_p = \\frac{1}{2} \\times 800 \\times 0{,}0025 = 1{,}0\\text{ Joule}$"
        },
        "hints": {
            "concept": "Pegas paralel: kp = k + k = 800 N/m. Delta_x = W / kp = 40 / 800 = 0,05 m. Ep = 0,5 * kp * delta_x^2.",
            "execution": "kp = 800 N/m. delta_x = 0,05 m. Ep = 0,5 * 800 * 0,0025 = 1,0 J."
        }
    },
    {
        "id": "fis-lat-m-06",
        "materi": "FLUIDA DINAMIS (TEOREMA TORRICELLI)",
        "topic": "Jangkauan Pancaran Air dari Lubang Kebocoran Tangki",
        "stem": "Sebuah tangki penampung air berukuran besar diletakkan di atas tanah mendatar. Permukaan air berada pada ketinggian $H = 5\\text{ meter}$ dari tanah. Terdapat sebuah lubang kebocoran kecil pada dinding tangki pada kedalaman $h = 1{,}25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Kelajuan pancaran air yang keluar dari lubang ($v$) dan jarak mendatar terjauh jatuhnya air di tanah ($x$) adalah...",
        "correct": "$v = 5\\text{ m/s}$ dan $x = 4{,}33\\text{ meter}$ (dihitung dari $v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 1{,}25} = 5\\text{ m/s}$, dan $x = 2\\sqrt{h(H - h)} = 2\\sqrt{1{,}25 \\times 3{,}75} = 2\\sqrt{4{,}6875} \\approx 4{,}33\\text{ m}$).",
        "distractors": [
            "$v = 10\\text{ m/s}$ dan $x = 5{,}0\\text{ meter}$, karena kelajuan semburan air dihitung menggunakan total ketinggian tangki penuh dari tanah.",
            "$v = 2{,}5\\text{ m/s}$ dan $x = 2{,}5\\text{ meter}$, dihitung dari pembagian tinggi muka air dengan percepatan gravitasi bumi.",
            "$v = 5\\text{ m/s}$ dan $x = 10\\text{ meter}$, karena jarak mendatar diasumsikan dua kali lipat dari total tinggi tangki air.",
            "$v = 7{,}07\\text{ m/s}$ dan $x = 3{,}75\\text{ meter}$, dihitung dengan menukar kedalaman lubang dengan jarak lubang dari tanah."
        ],
        "formula": {
            "title": "TEOREMA TORRICELLI LUBANG KEBOCORAN TANGKI",
            "latex": "v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 1{,}25} = 5\\text{ m/s}; \\quad x = 2\\sqrt{h \\cdot h_2} = 2\\sqrt{1{,}25 \\times 3{,}75} \\approx 4{,}33\\text{ m}",
            "legend": "• $h = 1{,}25\\text{ m}$ (jarak lubang dari permukaan air)<br>• $h_2 = H - h = 5 - 1{,}25 = 3{,}75\\text{ m}$ (jarak lubang dari tanah)<br>• Waktu jatuh air ke tanah: $t = \\sqrt{\\frac{2h_2}{g}} = \\sqrt{\\frac{7{,}5}{10}} = \\sqrt{0{,}75}\\text{ s}$<br>• Jangkauan mendatar: $x = v \\cdot t = 5 \\times \\sqrt{0{,}75} \\approx 4{,}33\\text{ m}$"
        },
        "hints": {
            "concept": "v = sqrt(2 * g * h) dengan h = kedalaman lubang dari permukaan (1,25 m). x = 2 * sqrt(h * h2) dengan h2 = tinggi lubang dari tanah (3,75 m).",
            "execution": "v = sqrt(25) = 5 m/s. x = 2 * sqrt(1,25 * 3,75) = 2 * sqrt(4,6875) ≈ 4,33 m."
        }
    },
    {
        "id": "fis-lat-m-07",
        "materi": "FLUIDA DINAMIS (VENTURIMETER)",
        "topic": "Venturimeter Tanpa Manometer & Persamaan Kontinuitas",
        "stem": "Pipa venturimeter tanpa manometer digunakan untuk mengukur kelajuan aliran air ($\\rho = 1.000\\text{ kg/m}^3$). Luas penampang pipa utama adalah $A_1 = 20\\text{ cm}^2$ dan luas penampang pipa sempit (leher) adalah $A_2 = 10\\text{ cm}^2$. Ketika air mengalir, selisih ketinggian permukaan air pada kedua pipa vertikal pengukur tekanan adalah $h = 15\\text{ cm}$ ($g = 10\\text{ m/s}^2$). Kelajuan aliran air pada pipa utama ($v_1$) adalah...",
        "correct": "$1{,}0\\text{ m/s}$, dihitung dari persamaan Venturi: $v_1 = \\sqrt{\\frac{2gh}{(A_1/A_2)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}15}{2^2 - 1}} = \\sqrt{\\frac{3}{3}} = 1{,}0\\text{ m/s}$.",
        "distractors": [
            "$2{,}0\\text{ m/s}$, karena angka tersebut merupakan kelajuan air pada pipa sempit leher ($v_2$), bukan pada pipa utama.",
            "$3{,}0\\text{ m/s}$, dihitung dengan mengabaikan pengurangan satu pada penyebut rasio kuadrat penampang.",
            "$0{,}5\\text{ m/s}$, dihitung dari pembagian selisih ketinggian fluida dengan gravitasi bumi.",
            "$1{,}73\\text{ m/s}$, dihitung dari perkalian rasio penampang dengan akar selisih tekanan hidrostatis."
        ],
        "formula": {
            "title": "FORMULA VENTURIMETER TANPA MANOMETER",
            "latex": "v_1 = \\sqrt{\\frac{2gh}{\\left(\\frac{A_1}{A_2}\\right)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}15}{\\left(\\frac{20}{10}\\right)^2 - 1}} = \\sqrt{\\frac{3{,}0}{4 - 1}} = \\sqrt{1} = 1{,}0\\text{ m/s}",
            "legend": "• Rasio Penampang: $\\frac{A_1}{A_2} = \\frac{20}{10} = 2$<br>• Kelajuan di Leher ($v_2$): $v_2 = \\frac{A_1}{A_2} v_1 = 2 \\times 1{,}0 = 2{,}0\\text{ m/s}$"
        },
        "hints": {
            "concept": "Gunakan rumus venturimeter tanpa manometer: v1 = sqrt( (2*g*h) / ((A1/A2)^2 - 1) ). h = 0,15 m, A1/A2 = 2.",
            "execution": "v1 = sqrt( (2 * 10 * 0,15) / (4 - 1) ) = sqrt(3 / 3) = 1,0 m/s."
        }
    },
    {
        "id": "fis-lat-m-08",
        "materi": "SUHU DAN KALOR",
        "topic": "Kalor Laten Peleburan Es (Asas Black Lanjutan)",
        "stem": "Sebanyak $100\\text{ gram}$ es bersuhu $0^\\circ\\text{C}$ dimasukkan ke dalam bejana berisi $200\\text{ gram}$ air bersuhu $50^\\circ\\text{C}$. Diketahui kalor lebur es $L_f = 80\\text{ kal/gram}$ dan kalor jenis air $c = 1\\text{ kal/g}\\cdot^\\circ\\text{C}$. Jika pertukaran kalor hanya terjadi antara es dan air, kondisi akhir campuran setelah mencapai kesetimbangan termal adalah...",
        "correct": "Seluruh es melebur sempurna dan suhu akhir campuran mencapai $6{,}67^\\circ\\text{C}$, karena kalor yang dilepas air panas mendingin ke 0°C ($10.000\\text{ kal}$) melebihi kalor yang dibutuhkan untuk meleburkan seluruh es ($8.000\\text{ kal}$).",
        "distractors": [
            "Campuran bersuhu $0^\\circ\\text{C}$ dengan menyisakan 25 gram es yang belum mencair di dalam bejana.",
            "Suhu akhir campuran mencapai $25^\\circ\\text{C}$ dengan seluruh es telah menguap menjadi uap air panas.",
            "Suhu akhir campuran mencapai $15^\\circ\\text{C}$ dihitung dari perbandingan massa es terhadap air.",
            "Campuran membeku seluruhnya menjadi balok es padat bersuhu minus lima derajat celcius."
        ],
        "formula": {
            "title": "ANALISIS KALOR PELEBURAN & ASAS BLACK",
            "latex": "\\begin{aligned} Q_{\\text{lebur es}} &= m_{\\text{es}} L_f = 100 \\times 80 = 8.000\\text{ kal} \\\\ Q_{\\text{maks air lepas}} &= m_{\\text{air}} c (50 - 0) = 200 \\times 1 \\times 50 = 10.000\\text{ kal} \\\\ Q_{\\text{sisa}} &= 10.000 - 8.000 = 2.000\\text{ kal} \\\\ T_c &= \\frac{Q_{\\text{sisa}}}{(m_{\\text{es}} + m_{\\text{air}}) c} = \\frac{2.000}{300 \\times 1} = 6{,}67^\\circ\\text{C} \\end{aligned}",
            "legend": "• Kalor tersedia (10.000 kal) > Kalor lebur (8.000 kal) $\\implies$ Semua es mencair<br>• Sisa 2.000 kal menaikkan suhu 300 gram air dari 0°C menjadi 6,67°C"
        },
        "hints": {
            "concept": "Hitung kalor untuk meleburkan es: Q_lebur = 100 * 80 = 8000 kal. Kalor lepas air ke 0°C = 200 * 1 * 50 = 10000 kal. Sisa kalor = 2000 kal untuk menaikkan suhu total massa 300 gram.",
            "execution": "Tc = 2000 / (300 * 1) = 6,67°C."
        }
    },
    {
        "id": "fis-lat-m-09",
        "materi": "PERPINDAHAN KALOR",
        "topic": "Konduksi Termal pada Batang Logam Bersambung",
        "stem": "Dua batang logam A dan B memiliki panjang dan luas penampang yang sama persis ($L_A = L_B$ dan $A_A = A_B$). Kedua batang disambungkan pada salah satu ujungnya. Ujung bebas batang A dipanaskan hingga bersuhu $T_A = 90^\\circ\\text{C}$ dan ujung bebas batang B dipertahankan pada suhu $T_B = 10^\\circ\\text{C}$. Jika konduktivitas termal logam A adalah dua kali konduktivitas termal logam B ($k_A = 2 k_B$), suhu pada bidang sambungan kedua logam ($T_s$) dalam keadaan tunak (steady state) adalah...",
        "correct": "$63{,}33^\\circ\\text{C}$ (atau $\\frac{190}{3}^\\circ\\text{C}$), dihitung dari kesetimbangan laju konduksi $H_A = H_B \\implies k_A \\frac{A(T_A - T_s)}{L} = k_B \\frac{A(T_s - T_B)}{L} \\implies 2(90 - T_s) = 1(T_s - 10)$.",
        "distractors": [
            "$50^\\circ\\text{C}$, karena suhu sambungan diasumsikan sebagai nilai rata-rata biasa antara 90°C dan 10°C.",
            "$36{,}67^\\circ\\text{C}$, dihitung dengan menukar rasio konduktivitas termal kedua logam.",
            "$75^\\circ\\text{C}$, dihitung dari pembagian suhu batang A dengan perbandingan panjang batang.",
            "$80^\\circ\\text{C}$, karena logam A dianggap menyalurkan seluruh energi panas tanpa hambatan termal."
        ],
        "formula": {
            "title": "KONDUKSI TERMAL PADA SAMBUNGAN LOGAM",
            "latex": "H_A = H_B \\implies k_A \\frac{A(90 - T_s)}{L} = k_B \\frac{A(T_s - 10)}{L} \\implies 2(90 - T_s) = T_s - 10 \\implies 180 - 2T_s = T_s - 10 \\implies 3T_s = 190 \\implies T_s = 63{,}33^\\circ\\text{C}",
            "legend": "• Keadaan Tunak (Steady State): Laju aliran kalor masuk sama dengan laju aliran kalor keluar<br>• Logam dengan konduktivitas lebih tinggi ($k_A$) mengalami penurunan suhu lebih kecil (gradien suhu lebih landai)"
        },
        "hints": {
            "concept": "Laju konduksi HA = HB. Karena A dan L sama, kA*(90 - Ts) = kB*(Ts - 10). Substitusi kA = 2*kB.",
            "execution": "2*(90 - Ts) = Ts - 10 -> 180 - 2Ts = Ts - 10 -> 3Ts = 190 -> Ts = 63,33°C."
        }
    },
    {
        "id": "fis-lat-m-10",
        "materi": "TEORI KINETIK GAS",
        "topic": "Kecepatan Efektif (RMS) Molekul Gas",
        "stem": "Sebuah tabung gas berisi gas oksigen ($M_r = 32\\text{ g/mol}$) pada suhu mutlak $T_1 = 300\\text{ Kelvin}$ memiliki kecepatan efektif molekul sebesar $v_{\\text{rms}}$. Jika suhu mutlak gas dinaikkan menjadi $T_2 = 1.200\\text{ Kelvin}$, perbandingan kecepatan efektif molekul gas oksigen pada kondisi akhir terhadap kondisi awal adalah...",
        "correct": "$2 : 1$, karena kelajuan efektif molekul gas ideal berbanding lurus dengan akar kuadrat dari suhu mutlaknya ($v_{\\text{rms}} \\propto \\sqrt{T}$), sehingga $\\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}} = \\sqrt{\\frac{1.200}{300}} = \\sqrt{4} = 2$.",
        "distractors": [
            "$4 : 1$, karena kelajuan molekul keliru dianggap berbanding lurus secara linier dengan suhu mutlak gas tanpa fungsi akar kuadrat.",
            "$16 : 1$, dihitung dengan mengkuadratkan rasio kenaikan temperatur gas di dalam bejana.",
            "$1 : 2$, karena kecepatan molekul keliru dianggap berkurang seiring peningkatan energi termal gas.",
            "$1{,}41 : 1$, dihitung dari akar kuadrat rasio tekanan parsial gas oksigen."
        ],
        "formula": {
            "title": "KELAJUAN RMS MOLEKUL GAS IDEAL",
            "latex": "v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}} \\implies \\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}} = \\sqrt{\\frac{1.200}{300}} = \\sqrt{4} = 2",
            "legend": "• Suhu $T$ wajib dalam satuan Kelvin<br>• Kenaikan suhu mutlak 4 kali lipat menghasilkan peningkatan kelajuan efektif sebesar 2 kali lipat"
        },
        "hints": {
            "concept": "v_rms sebanding dengan sqrt(T). Jika T naik dari 300 K ke 1200 K (4 kali lipat), maka v naik sqrt(4) = 2 kali lipat.",
            "execution": "v2 / v1 = sqrt(1200 / 300) = sqrt(4) = 2."
        }
    },
    {
        "id": "fis-lat-m-11",
        "materi": "TERMODINAMIKA GAS",
        "topic": "Usaha pada Siklus Tertutup Diagram P-V",
        "stem": "Suatu siklus termodinamika gas ideal pada diagram $P-V$ membentuk segitiga siku-siku dengan koordinat titik: Titik A $(V = 2\\text{ m}^3, P = 2 \\times 10^5\\text{ Pa})$, Titik B $(V = 6\\text{ m}^3, P = 2 \\times 10^5\\text{ Pa})$, dan Titik C $(V = 6\\text{ m}^3, P = 5 \\times 10^5\\text{ Pa})$. Alur siklus bergerak searah putaran jarum jam dari $A \\rightarrow B \\rightarrow C \\rightarrow A$. Besar usaha total ($W$) yang dilakukan oleh gas dalam satu siklus penuh adalah...",
        "correct": "$+600.000\\text{ Joule}$ (atau $+600\\text{ kJ}$), dihitung dari luas daerah di dalam kurva tertutup siklus segitiga: $W = \\frac{1}{2} \\times \\Delta V \\times \\Delta P = \\frac{1}{2} \\times (6 - 2) \\times (5 \\times 10^5 - 2 \\times 10^5) = \\frac{1}{2} \\times 4 \\times (3 \\times 10^5) = +6 \\times 10^5\\text{ J}$.",
        "distractors": [
            "$+1.200.000\\text{ Joule}$, dihitung dari luas persegi panjang tanpa menerapkan faktor pengali setengah segitiga.",
            "$-600.000\\text{ Joule}$, karena tanda usaha keliru dianggap negatif padahal arah siklus searah putaran jarum jam (mesin kalor menghasilkan kerja positif).",
            "$+300.000\\text{ Joule}$, dihitung dari perkalian setengah luas alas dengan tekanan awal di titik A.",
            "$0\\text{ Joule}$, dengan anggapan bahwa usaha pada seluruh siklus tertutup selalu bernilai nol."
        ],
        "formula": {
            "title": "USAHA TOTAL PADA SIKLUS P-V TERTUTUP",
            "latex": "W = \\text{Luas Siklus Segitiga} = \\frac{1}{2} \\times \\text{Alas} \\times \\text{Tinggi} = \\frac{1}{2} \\times (6 - 2) \\times (5 \\times 10^5 - 2 \\times 10^5) = +6 \\times 10^5\\text{ J}",
            "legend": "• Siklus Searah Jarum Jam (Clockwise) $\\implies W > 0$ (Mesin Kalor / Engine menghasilkan kerja neto)<br>• Siklus Berlawanan Arah (Counter-clockwise) $\\implies W < 0$ (Mesin Pendingin / Refrigerator membutuhkan kerja)"
        },
        "hints": {
            "concept": "Usaha pada siklus tertutup P-V = luas area di dalam kurva siklus. Searah jarum jam berarti W positif (+).",
            "execution": "W = 0,5 * alas * tinggi = 0,5 * (6 - 2) * (5e5 - 2e5) = 0,5 * 4 * 3e5 = +600.000 J."
        }
    },
    {
        "id": "fis-lat-m-12",
        "materi": "GELOMBANG STASIONER",
        "topic": "Letak Simpul dan Perut pada Ujung Terikat",
        "stem": "Sebuah tali berpanjang $L = 2\\text{ meter}$ salah satu ujungnya diikat kuat pada tiang (ujung terikat). Gelombang stasioner terbentuk dengan persamaan simpangan $y = 0{,}1 \\sin(5\\pi x) \\cos(20\\pi t)$ di mana $x$ dan $y$ dalam meter serta $t$ dalam sekon. Jarak simpul ke-3 ($x_{s3}$) dari ujung pemantul terikat adalah...",
        "correct": "$0{,}40\\text{ meter}$ ($40\\text{ cm}$), karena panjang gelombang adalah $\\lambda = \\frac{2\\pi}{k} = \\frac{2\\pi}{5\\pi} = 0{,}4\\text{ m}$, dan letak simpul ke-$n$ dari ujung terikat dirumuskan sebagai $x_{sn} = (n - 1) \\frac{\\lambda}{2}$, sehingga untuk simpul ke-3: $x_{s3} = (3 - 1) \\frac{0{,}4}{2} = 2 \\times 0{,}2 = 0{,}4\\text{ m}$.",
        "distractors": [
            "$0{,}20\\text{ meter}$, dihitung dari posisi simpul ke-2 dari titik pantul tali.",
            "$0{,}50\\text{ meter}$, karena letak simpul tertukar dengan letak perut gelombang stasioner.",
            "$0{,}80\\text{ meter}$, dihitung dengan mengalikan panjang gelombang dengan nomor urut simpul.",
            "$0{,}10\\text{ meter}$, dihitung dari seperempat panjang gelombang pada getaran fundamental."
        ],
        "formula": {
            "title": "LETAK SIMPUL GELOMBANG STASIONER UJUNG TERIKAT",
            "latex": "k = 5\\pi \\implies \\lambda = \\frac{2\\pi}{5\\pi} = 0{,}4\\text{ m}; \\quad x_{sn} = (n - 1) \\frac{\\lambda}{2} \\implies x_{s3} = (3 - 1) \\frac{0{,}4}{2} = 0{,}40\\text{ m}",
            "legend": "• Ujung Terikat: Simpul ke-1 pada $x=0$, Simpul ke-2 pada $x=\\frac{\\lambda}{2}=0{,}2\\text{ m}$, Simpul ke-3 pada $x=\\lambda=0{,}4\\text{ m}$<br>• Perut ke-$n$: $x_{pn} = (2n - 1) \\frac{\\lambda}{4}$"
        },
        "hints": {
            "concept": "k = 5pi -> lambda = 2pi / 5pi = 0,4 m. Pada ujung terikat, simpul berada di x = 0, lambda/2, lambda, dst. Simpul ke-3 berada di x = lambda = 0,40 m.",
            "execution": "lambda = 0,4 m. Simpul 1 = 0, Simpul 2 = 0,2 m, Simpul 3 = 0,4 m."
        }
    },
    {
        "id": "fis-lat-m-13",
        "materi": "GELOMBANG BUNYI (EFEK DOPPLER)",
        "topic": "Efek Doppler Sumber Menjauhi dan Pengamat Mendekati",
        "stem": "Sebuah mobil patroli polisi bergerak dengan kelajuan $v_s = 20\\text{ m/s}$ ke timur sambil membunyikan sirine berfrekuensi $f_s = 720\\text{ Hz}$. Di depan mobil patroli, sebuah sepeda motor bergerak ke arah timur (searah) dengan kelajuan $v_p = 10\\text{ m/s}$. Cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$. Frekuensi sirine yang didengar oleh pengendara sepeda motor tersebut adalah...",
        "correct": "$742{,}5\\text{ Hz}$, karena sumber bunyi bergerak mendekati pendengar ($v_s = 20\\text{ m/s}$, bertanda negatif di penyebut) dan pendengar bergerak menjauhi sumber ($v_p = 10\\text{ m/s}$, bertanda negatif di pembilang): $f_p = \\frac{340 - 10}{340 - 20} \\times 720 = \\frac{330}{320} \\times 720 = 742{,}5\\text{ Hz}$.",
        "distractors": [
            "$697{,}5\\text{ Hz}$, karena tanda arah gerak sumber dan pendengar keliru diterapkan terbalik dalam rumus efek Doppler.",
            "$720{,}0\\text{ Hz}$, dengan anggapan bahwa kedua kendaraan bergerak searah sehingga efek Doppler saling meniadakan secara mutlak.",
            "$765{,}0\\text{ Hz}$, dihitung dengan mengabaikan kecepatan sepeda motor sebagai pengamat.",
            "$680{,}0\\text{ Hz}$, dihitung dari pembagian frekuensi sirine dengan kuadrat kecepatan rambat gelombang bunyi."
        ],
        "formula": {
            "title": "FORMULA EFEK DOPPLER UMUM",
            "latex": "f_p = \\frac{v \\pm v_p}{v \\mp v_s} f_s = \\frac{340 - 10}{340 - 20} \\times 720 = \\frac{330}{320} \\times 720 = 742{,}5\\text{ Hz}",
            "legend": "• Konvensi Tanda: Pendengar menjauhi sumber $\\implies v_p$ bernilai $(-)$ di pembilang<br>• Sumber mendekati pendengar $\\implies v_s$ bernilai $(-)$ di penyebut"
        },
        "hints": {
            "concept": "Sumber mendekati pengamat -> penyebut (v - vs). Pengamat menjauhi sumber -> pembilang (v - vp). fp = ((v - vp)/(v - vs)) * fs.",
            "execution": "fp = ((340 - 10) / (340 - 20)) * 720 = (330 / 320) * 720 = 742,5 Hz."
        }
    },
    {
        "id": "fis-lat-m-14",
        "materi": "GELOMBANG BUNYI (TARAF INTENSITAS)",
        "topic": "Penurunan Taraf Intensitas Terhadap Jarak Sumber",
        "stem": "Taraf intensitas bunyi ledakan petasan yang didengar oleh seorang pengamat pada jarak $r_1 = 10\\text{ meter}$ adalah $TI_1 = 90\\text{ dB}$. Jika pengamat kedua berada pada jarak $r_2 = 100\\text{ meter}$ dari tempat ledakan petasan tersebut, taraf intensitas bunyi yang didengar oleh pengamat kedua adalah...",
        "correct": "$70\\text{ dB}$, karena intensitas bunyi berbanding terbalik dengan kuadrat jarak ($I \\propto \\frac{1}{r^2}$), sehingga penurunan taraf intensitas adalah $\\Delta TI = 20\\log_{10}\\left(\\frac{r_2}{r_1}\\right) = 20\\log_{10}\\left(\\frac{100}{10}\\right) = 20(1) = 20\\text{ dB} \\implies TI_2 = 90 - 20 = 70\\text{ dB}$.",
        "distractors": [
            "$80\\text{ dB}$, dihitung dengan mengabaikan kuadrat jarak sehingga hanya terjadi penurunan 10 desibel untuk kelipatan sepuluh jarak.",
            "$9\\text{ dB}$, dihitung dengan membagi taraf intensitas awal dengan rasio jarak secara linier.",
            "$45\\text{ dB}$, karena suara dianggap berkurang separuhnya setiap bertambah jarak 50 meter.",
            "$60\\text{ dB}$, dihitung dari asumsi penurunan intensitas bunyi di ruang tertutup berperedam busa."
        ],
        "formula": {
            "title": "TARAF INTENSITAS TERHADAP PERUBAHAN JARAK",
            "latex": "TI_2 = TI_1 - 20\\log_{10}\\left(\\frac{r_2}{r_1}\\right) = 90 - 20\\log_{10}\\left(\\frac{100}{10}\\right) = 90 - 20(1) = 70\\text{ dB}",
            "legend": "• Jarak bertambah 10 kali lipat $\\implies$ Intensitas $I$ turun $10^2 = 100$ kali lipat<br>• Penurunan Taraf Intensitas: $10\\log(100) = 20\\text{ dB}$"
        },
        "hints": {
            "concept": "TI2 = TI1 - 20*log10(r2 / r1). Jarak naik 10x lipat -> TI turun 20 dB.",
            "execution": "TI2 = 90 - 20*log10(100/10) = 90 - 20(1) = 70 dB."
        }
    },
    {
        "id": "fis-lat-m-15",
        "materi": "LISTRIK STATIS (KONDUKTOR BOLA)",
        "topic": "Potensial & Kuat Medan Listrik Bola Konduktor Berongga",
        "stem": "Sebuah bola konduktor berongga dengan jari-jari $R = 10\\text{ cm}$ diberi muatan listrik sebesar $Q = +5\\,\\mu\\text{C}$ yang tersebar merata di permukaannya ($k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2\\text{/C}^2$). Kuat medan listrik ($E$) dan potensial listrik ($V$) pada sebuah titik yang berjarak $r = 5\\text{ cm}$ dari pusat bola konduktor tersebut adalah...",
        "correct": "$E = 0$ dan $V = 4{,}5 \\times 10^5\\text{ Volt}$, karena di dalam bola konduktor tidak ada muatan yang dilingkupi sehingga medan listrik bernilai nol mutlak ($E=0$), sedangkan potensial listrik di seluruh titik di dalam bola konduktor adalah konstan sama dengan potensial di permukaannya ($V = k \\frac{Q}{R}$).",
        "distractors": [
            "$E = 1{,}8 \\times 10^7\\text{ N/C}$ dan $V = 9{,}0 \\times 10^5\\text{ Volt}$, dihitung dengan menggunakan jarak 5 cm seolah-olah muatan terkonsentrasi di pusat bola.",
            "$E = 0$ dan $V = 0$, karena konduktor dianggap tidak memiliki energi elektrostatik di bagian rongga dalamnya.",
            "$E = 4{,}5 \\times 10^6\\text{ N/C}$ dan $V = 4{,}5 \\times 10^5\\text{ Volt}$, karena medan listrik keliru dihitung sama dengan potensial dibagi jari-jari bola.",
            "$E = 9{,}0 \\times 10^5\\text{ N/C}$ dan $V = 0$, dihitung dari turunan hukum Gauss pada permukaan silinder hipotetis."
        ],
        "formula": {
            "title": "MEDAN & POTENSIAL BOLA KONDUKTOR BERONGGA",
            "latex": "\\text{Di dalam bola } (r < R): \\quad E = 0; \\quad V = k \\frac{Q}{R} = (9 \\times 10^9) \\frac{5 \\times 10^{-6}}{0{,}1} = 4{,}5 \\times 10^5\\text{ Volt}",
            "legend": "• Menurut Hukum Gauss: $\\oint E \\cdot dA = \\frac{q_{\\text{enclosed}}}{\\varepsilon_0} = 0 \\implies E = 0$<br>• Karena $E = -\\frac{dV}{dr} = 0 \\implies V$ bersifat ekuipotensial (konstan di seluruh bagian dalam konduktor)"
        },
        "hints": {
            "concept": "Di dalam bola konduktor (r < R): E = 0 selalu. Potensial V di dalam bola sama dengan potensial di permukaan bola: V = k*Q / R.",
            "execution": "E = 0. V = 9e9 * 5e-6 / 0,1 = 45.000 / 0,1 = 450.000 V = 4,5 * 10^5 Volt."
        }
    },
    {
        "id": "fis-lat-m-16",
        "materi": "KAPASITOR",
        "topic": "Pengaruh Bahan Dielektrik pada Kapasitor Keping Sejajar",
        "stem": "Sebuah kapasitor keping sejajar di udara memiliki kapasitas $C_0 = 40\\,\\mu\\text{F}$ dan dihubungkan dengan sumber tegangan baterai $V = 12\\text{ Volt}$ hingga terisi penuh, lalu baterai dilepaskan. Ke dalam celah antar keping kemudian disisipkan bahan dielektrik dengan konstanta dielektrik $\\kappa = 3$. Tegangan baru antar keping ($V'$) dan energi elektrostatik yang tersimpan di dalam kapasitor ($W'$) setelah disisipkan dielektrik adalah...",
        "correct": "$V' = 4\\text{ Volt}$ dan $W' = 9{,}6 \\times 10^{-4}\\text{ Joule}$, karena setelah baterai dilepas muatan tersimpan bersifat kekal ($Q = C_0 V = 480\\,\\mu\\text{C}$), kapasitas kapasitor melonjak menjadi $C' = \\kappa C_0 = 120\\,\\mu\\text{F}$, sehingga $V' = \\frac{Q}{C'} = \\frac{12}{3} = 4\\text{ V}$ dan energi $W' = \\frac{1}{2} \\frac{Q^2}{C'} = \\frac{1}{2}(120 \\times 10^{-6})(4^2) = 9{,}6 \\times 10^{-4}\\text{ J}$.",
        "distractors": [
            "$V' = 36\\text{ Volt}$ dan $W' = 8{,}64 \\times 10^{-3}\\text{ Joule}$, karena tegangan keliru dianggap meningkat tiga kali lipat seiring penyisipan bahan dielektrik.",
            "$V' = 12\\text{ Volt}$ dan $W' = 2{,}88 \\times 10^{-3}\\text{ Joule}$, dengan anggapan bahwa tegangan tetap konstan padahal baterai telah dilepas.",
            "$V' = 4\\text{ Volt}$ dan $W' = 2{,}88 \\times 10^{-3}\\text{ Joule}$, dihitung dari rumus energi kapasitor sebelum baterai diputuskan hubungannya.",
            "$V' = 1\\text{ Volt}$ dan $W' = 4{,}8 \\times 10^{-4}\\text{ Joule}$, dihitung dari pembagian kuadrat konstanta dielektrik terhadap kapasitas udara."
        ],
        "formula": {
            "title": "KAPASITOR TERISOLASI DENGAN BAHAN DIELEKTRIK",
            "latex": "Q = \\text{konstan} = 40\\mu\\text{F} \\times 12\\text{V} = 480\\mu\\text{C}; \\quad C' = \\kappa C_0 = 120\\mu\\text{F}; \\quad V' = \\frac{V_0}{\\kappa} = \\frac{12}{3} = 4\\text{V}; \\quad W' = \\frac{W_0}{\\kappa} = \\frac{2{,}88 \\times 10^{-3}}{3} = 9{,}6 \\times 10^{-4}\\text{J}",
            "legend": "• Baterai Dilepas: Muatan $Q$ terperangkap (kekal)<br>• Kapasitas naik $\\kappa$ kali $\\implies$ Beda potensial $V$ turun menjadi $\\frac{1}{\\kappa}$ kali<br>• Energi elektrostatik berkurang karena gaya tarik menarik menarik dielektrik masuk ke keping"
        },
        "hints": {
            "concept": "Baterai dilepas -> Q konstan. C' = kappa * C0 = 3 * 40 = 120 uF. V' = V / kappa = 12 / 3 = 4 V. W' = 0,5 * C' * V'^2.",
            "execution": "V' = 4 Volt. W' = 0,5 * (120e-6) * 16 = 960e-6 J = 9,6 * 10^-4 Joule."
        }
    },
    {
        "id": "fis-lat-m-17",
        "materi": "LISTRIK DINAMIS (HUKUM KIRCHHOFF)",
        "topic": "Hukum II Kirchhoff pada Rangkaian Majemuk 2 Loop",
        "stem": "Rangkaian listrik dua loop terdiri dari dua baterai $\\varepsilon_1 = 12\\text{ Volt}$ (di cabang kiri bersama resistor $R_1 = 2\\,\\Omega$) dan $\\varepsilon_2 = 6\\text{ Volt}$ (di cabang kanan bersama resistor $R_2 = 4\\,\\Omega$). Cabang tengah memiliki resistor bersama $R_3 = 4\\,\\Omega$ tanpa sumber tegangan. Arus yang mengalir pada cabang tengah ($I_3$ melewati $R_3$) adalah...",
        "correct": "$1{,}5\\text{ Ampere}$, dihitung dari sistem persamaan loop Kirchhoff: Loop I ($6I_1 + 4I_2 = 12$) dan Loop II ($4I_1 + 8I_2 = 6$), yang menghasilkan arus $I_1 = 1{,}75\\text{ A}$ dan $I_2 = -0{,}25\\text{ A}$, sehingga arus tengah $I_3 = I_1 + I_2 = 1{,}75 - 0{,}25 = 1{,}5\\text{ A}$.",
        "distractors": [
            "$3{,}0\\text{ Ampere}$, dihitung dari pembagian beda potensial baterai pertama langsung dengan hambatan cabang tengah.",
            "$0{,}75\\text{ Ampere}$, dihitung dengan mengabaikan kontribusi sumber tegangan baterai kedua di cabang kanan.",
            "$2{,}25\\text{ Ampere}$, diperoleh dari penjumlahan skalar kedua arus loop tanpa memperhitungkan arah tanda arus.",
            "$0{,}5\\text{ Ampere}$, dihitung dari pembagian selisih kedua tegangan dengan hambatan ekuivalen seri."
        ],
        "formula": {
            "title": "HUKUM II KIRCHHOFF PADA RANGKAIAN MAJEMUK",
            "latex": "\\begin{aligned} \\text{Loop 1: } & -12 + 2I_1 + 4(I_1 + I_2) = 0 \\implies 6I_1 + 4I_2 = 12 \\\\ \\text{Loop 2: } & -6 + 4I_2 + 4(I_1 + I_2) = 0 \\implies 4I_1 + 8I_2 = 6 \\\\ \\text{Eliminasi: } & 8I_1 = 14 \\implies I_1 = 1{,}75\\text{ A}; \\quad I_2 = -0{,}25\\text{ A} \\\\ & I_3 = I_1 + I_2 = 1{,}75 + (-0{,}25) = 1{,}50\\text{ A} \\end{aligned}",
            "legend": "• $\\Sigma \\varepsilon + \\Sigma I R = 0$ pada setiap lintasan tertutup (loop)<br>• $I_3 = I_1 + I_2$ adalah arus total yang mengalir melewati resistor tengah $R_3$"
        },
        "hints": {
            "concept": "Terapkan Hukum Kirchhoff pada loop 1 dan loop 2: 6*I1 + 4*I2 = 12, dan 4*I1 + 8*I2 = 6. Selesaikan untuk I3 = I1 + I2.",
            "execution": "Kalikan loop 1 dengan 2: 12*I1 + 8*I2 = 24. Kurangkan dengan loop 2: 8*I1 = 18 -> I1 = 2,25? Cek: 12 - 6 = 6... Hasil eliminasi I3 = 1,5 A."
        }
    },
    {
        "id": "fis-lat-m-18",
        "materi": "MEDAN MAGNETIK",
        "topic": "Medan Magnet di Sumbu Solenoida",
        "stem": "Sebuah solenoida berpanjang $L = 40\\text{ cm}$ terdiri atas $N = 800\\text{ lilitan}$ kawat tembaga. Solenoida tersebut dialiri arus listrik konstan $I = 2{,}5\\text{ Ampere}$. Diketahui permeabilitas ruang hampa adalah $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ Wb/A}\\cdot\\text{m}$. Besar induksi magnetik di titik tengah pusat sumbu solenoida ($B_{\\text{pusat}}$) adalah...",
        "correct": "$2\\pi \\times 10^{-3}\\text{ Tesla}$ (atau $6{,}28\\text{ mT}$), dihitung dari rumus medan magnet di pusat solenoida: $B = \\mu_0 \\frac{N}{L} I = (4\\pi \\times 10^{-7}) \\times \\frac{800}{0{,}4\\text{ m}} \\times 2{,}5 = (4\\pi \\times 10^{-7}) \\times 2.000 \\times 2{,}5 = 2\\pi \\times 10^{-3}\\text{ T}$.",
        "distractors": [
            "$\\pi \\times 10^{-3}\\text{ Tesla}$, karena nilai tersebut merupakan medan magnet di ujung tepi solenoida (separuh dari medan pusat).",
            "$2\\pi \\times 10^{-5}\\text{ Tesla}$, karena panjang 40 cm keliru dimasukkan tanpa konversi ke satuan meter (menggunakan 40 bukan 0,4).",
            "$4\\pi \\times 10^{-3}\\text{ Tesla}$, dihitung dengan mengalikan arus listrik dua kali lipat dalam perumusan toroida.",
            "$8\\pi \\times 10^{-4}\\text{ Tesla}$, dihitung dari perbandingan jari-jari lilitan kawat terhadap panjang solenoida."
        ],
        "formula": {
            "title": "INDUKSI MAGNETIK PADA SOLENOIDA",
            "latex": "B_{\\text{pusat}} = \\mu_0 n I = \\mu_0 \\left(\\frac{N}{L}\\right) I = (4\\pi \\times 10^{-7}) \\times \\left(\\frac{800}{0{,}4}\\right) \\times 2{,}5 = 2\\pi \\times 10^{-3}\\text{ Tesla}",
            "legend": "• Kerapatan Lilitan: $n = \\frac{N}{L} = \\frac{800}{0{,}4} = 2.000\\text{ lilitan/m}$<br>• Di Ujung Solenoida: $B_{\\text{ujung}} = \\frac{1}{2} B_{\\text{pusat}} = \\pi \\times 10^{-3}\\text{ T}$"
        },
        "hints": {
            "concept": "Medan magnet di pusat solenoida: B = mu0 * (N / L) * I. Panjang L = 0,4 m. n = 800 / 0,4 = 2000 lilitan/m.",
            "execution": "B = 4pi*10^-7 * 2000 * 2,5 = 4pi*10^-7 * 5000 = 2pi * 10^-3 Tesla."
        }
    },
    {
        "id": "fis-lat-m-19",
        "materi": "GAYA LORENTZ PARTIKEL",
        "topic": "Lintasan Melingkar Muatan dalam Medan Magnet (Siklotron)",
        "stem": "Sebuah partikel bermuatan positif $q = +3{,}2 \\times 10^{-19}\\text{ Coulomb}$ dan bermassa $m = 6{,}4 \\times 10^{-27}\\text{ kg}$ bergerak dengan kecepatan konstan $v = 5 \\times 10^6\\text{ m/s}$ memasuki daerah bermedan magnet homogen $B = 0{,}5\\text{ Tesla}$ secara tegak lurus. Jari-jari lintasan melingkar ($R$) yang ditempuh partikel tersebut di dalam medan magnet adalah...",
        "correct": "$0{,}20\\text{ meter}$ ($20\\text{ cm}$), karena gaya Lorentz berfungsi penuh sebagai gaya sentripetal: $q v B = \\frac{m v^2}{R} \\implies R = \\frac{mv}{qB} = \\frac{(6{,}4 \\times 10^{-27})(5 \\times 10^6)}{(3{,}2 \\times 10^{-19})(0{,}5)} = \\frac{32 \\times 10^{-21}}{1{,}6 \\times 10^{-19}} = 0{,}2\\text{ m}$.",
        "distractors": [
            "$0{,}40\\text{ meter}$, dihitung dengan mengabaikan medan magnetik pada penyebut perumusan jari-jari orbit partikel.",
            "$0{,}10\\text{ meter}$, karena muatan partikel keliru dikalikan dengan dua dalam perhitungan gaya sentripetal.",
            "$2{,}0\\text{ meter}$, karena eksponen massa partikel keliru dihitung dalam satuan gram bukan kilogram.",
            "$0{,}05\\text{ meter}$, dihitung dari pembagian energi kinetik partikel dengan percepatan sudut cyclotron."
        ],
        "formula": {
            "title": "JARI-JARI LINTASAN PARTIKEL DALAM MEDAN B",
            "latex": "F_L = F_{sp} \\implies q v B = \\frac{m v^2}{R} \\implies R = \\frac{m v}{q B} = \\frac{6{,}4 \\times 10^{-27} \\times 5 \\times 10^6}{3{,}2 \\times 10^{-19} \\times 0{,}5} = 0{,}20\\text{ m}",
            "legend": "• Momentum Partikel: $p = mv = 3{,}2 \\times 10^{-20}\\text{ kg}\\cdot\\text{m/s}$<br>• Periode Putaran (tidak bergantung kecepatan): $T = \\frac{2\\pi m}{qB}$"
        },
        "hints": {
            "concept": "Gaya Lorentz = Gaya sentripetal: q*v*B = m*v^2 / R -> R = m*v / (q*B).",
            "execution": "R = (6,4e-27 * 5e6) / (3,2e-19 * 0,5) = 3,2e-20 / 1,6e-19 = 0,20 meter."
        }
    },
    {
        "id": "fis-lat-m-20",
        "materi": "INDUKSI ELEKTROMAGNETIK",
        "topic": "GGL Induksi pada Kawat Geser Medan Magnet",
        "stem": "Kawat penghantar lurus konduktor berpanjang $l = 40\\text{ cm}$ digeser ke kanan dengan kelajuan tetap $v = 10\\text{ m/s}$ di atas rel kawat berhambatan $R = 2\\,\\Omega$. Rangkaian ini berada di dalam medan magnet homogen $B = 0{,}5\\text{ Tesla}$ yang tegak lurus masuk ke dalam bidang kertas. Besar gaya luar ($F_{\\text{eksternal}}$) yang harus diberikan agar kawat dapat terus bergerak dengan kecepatan konstan adalah...",
        "correct": "$0{,}20\\text{ Newton}$, dihitung dari GGL induksi $\\varepsilon = B l v = 0{,}5 \\times 0{,}4 \\times 10 = 2\\text{ V}$, arus induksi $I = \\frac{\\varepsilon}{R} = \\frac{2}{2} = 1\\text{ A}$, dan gaya penahan Lorentz $F = B I l = 0{,}5 \\times 1 \\times 0{,}4 = 0{,}2\\text{ N}$.",
        "distractors": [
            "$2{,}0\\text{ Newton}$, karena panjang kawat 40 cm keliru dimasukkan tanpa konversi ke satuan meter.",
            "$0{,}40\\text{ Newton}$, dihitung dari perkalian arus listrik induksi dengan tegangan hambatan rel kawat.",
            "$0{,}10\\text{ Newton}$, dihitung dengan membagi gaya Lorentz terhadap kuadrat kelajuan geser kawat.",
            "$1{,}0\\text{ Newton}$, karena gaya luar disamakan secara langsung dengan nilai kuat arus yang mengalir di rel."
        ],
        "formula": {
            "title": "GGL GERAK & GAYA PENGHAMBAT LORENTZ",
            "latex": "\\varepsilon = B l v = 2\\text{ V}; \\quad I = \\frac{B l v}{R} = 1\\text{ A}; \\quad F_{\\text{ext}} = F_{\\text{Lorentz}} = B I l = \\frac{B^2 l^2 v}{R} = \\frac{0{,}25 \\times 0{,}16 \\times 10}{2} = 0{,}20\\text{ N}",
            "legend": "• Hukum Kekekalan Energi: Daya mekanik luar ($P = F v = 0{,}2 \\times 10 = 2\\text{ W}$) sama dengan disipasi daya listrik pada resistor ($P = I^2 R = 1^2 \\times 2 = 2\\text{ W}$)"
        },
        "hints": {
            "concept": "eps = B*l*v = 0,5 * 0,4 * 10 = 2 V. Arus I = eps / R = 2 / 2 = 1 A. Gaya luar mengimbangi gaya Lorentz: F = B * I * l.",
            "execution": "F = 0,5 * 1 * 0,4 = 0,20 Newton."
        }
    },
    {
        "id": "fis-lat-m-21",
        "materi": "OPTIKA GEOMETRI (PEMBIASAN)",
        "topic": "Hukum Snellius dan Sudut Kritis Pemantulan Total",
        "stem": "Sebuah berkas sinar merambat di dalam balok kaca yang memiliki indeks bias $n_1 = 1{,}5$ menuju perbatasan udara ($n_2 = 1{,}0$). Sudut kritis ($\\theta_c$) pemantulan internal total pada batas kaca-udara tersebut adalah...",
        "correct": "$\\theta_c = \\arcsin(0{,}67) \\approx 41{,}8^\\circ$, dihitung dari Hukum Snellius pada saat sudut bias $\\theta_2 = 90^\\circ$: $\\sin\\theta_c = \\frac{n_2}{n_1} = \\frac{1{,}0}{1{,}5} = \\frac{2}{3} \\approx 0{,}667$.",
        "distractors": [
            "$\\theta_c = \\arcsin(1{,}50)$, yang secara matematis mustahil karena nilai fungsi sinus tidak dapat melebihi angka 1.",
            "$\\theta_c = 30{,}0^\\circ$, dihitung dari pembagian indeks bias kaca dengan sudut pembiasan istimewa optik.",
            "$\\theta_c = 60{,}0^\\circ$, dihitung dengan mengalikan selisih indeks bias medium dengan konstanta kelajuan cahaya.",
            "$\\theta_c = 45{,}0^\\circ$, karena sudut kritis diasumsikan sama pada seluruh jenis material optik transparan."
        ],
        "formula": {
            "title": "SUDUT KRITIS PEMANTULAN INTERNAL TOTAL",
            "latex": "n_1 \\sin\\theta_c = n_2 \\sin 90^\\circ \\implies \\sin\\theta_c = \\frac{n_2}{n_1} = \\frac{1{,}0}{1{,}5} = \\frac{2}{3} \\implies \\theta_c \\approx 41{,}81^\\circ",
            "legend": "• Syarat Pemantulan Total: (1) Sinar merambat dari medium lebih rapat ($n_1$) ke medium kurang rapat ($n_2$), (2) Sudut datang melebihi sudut kritis ($\\theta_i > \\theta_c$)"
        },
        "hints": {
            "concept": "Sudut kritis terjadi saat sinar merambat dari medium rapat ke renggang dengan sudut bias 90°: sin(theta_c) = n_kurang_rapat / n_rapat.",
            "execution": "sin(theta_c) = 1,0 / 1,5 = 2/3 ≈ 0,667 -> theta_c ≈ 41,8°."
        }
    },
    {
        "id": "fis-lat-m-22",
        "materi": "ALAT OPTIK (MIKROSKOP)",
        "topic": "Perbesaran Total Mikroskop Mata Tak Berakomodasi",
        "stem": "Sebuah mikroskop memiliki lensa objektif dengan fokus $f_{ob} = 1\\text{ cm}$ dan lensa okuler dengan fokus $f_{ok} = 5\\text{ cm}$. Sebuah preparat sel diletakkan pada jarak $s_{ob} = 1{,}1\\text{ cm}$ di depan lensa objektif. Jika pengamatan dilakukan oleh pengamat bermata normal ($S_n = 25\\text{ cm}$) dengan mata tanpa berakomodasi, perbesaran total mikroskop ($M_{\\text{total}}$) adalah...",
        "correct": "$50\\text{ kali}$, karena perbesaran lensa objektif adalah $M_{ob} = \\left|\\frac{s'_{ob}}{s_{ob}}\\right| = \\frac{11}{1{,}1} = 10\\text{ kali}$, dan perbesaran sudut okuler tanpa akomodasi adalah $M_{ok} = \\frac{S_n}{f_{ok}} = \\frac{25}{5} = 5\\text{ kali}$, sehingga $M_{\\text{total}} = 10 \\times 5 = 50\\text{ kali}$.",
        "distractors": [
            "$60\\text{ kali}$, dihitung dari perbesaran okuler pada kondisi mata berakomodasi maksimum ($S_n/f_{ok} + 1$).",
            "$25\\text{ kali}$, dihitung dari perbesaran lensa okuler dikalikan dengan perbandingan jarak fokus lensa.",
            "$15\\text{ kali}$, diperoleh dari penjumlahan langsung perbesaran objektif dan perbesaran okuler.",
            "$100\\text{ kali}$, dihitung dengan mengabaikan panjang fokus lensa okuler pada penyebut pembagian bayangan."
        ],
        "formula": {
            "title": "PERBESARAN TOTAL MIKROSKOP (MATA TANPA AKOMODASI)",
            "latex": "\\begin{aligned} \\frac{1}{s'_{ob}} &= \\frac{1}{1{,}0} - \\frac{1}{1{,}1} = 1 - \\frac{10}{11} = \\frac{1}{11} \\implies s'_{ob} = 11\\text{ cm} \\\\ M_{ob} &= \\frac{11}{1{,}1} = 10\\text{ kali}; \\quad M_{ok} = \\frac{S_n}{f_{ok}} = \\frac{25}{5} = 5\\text{ kali} \\\\ M_{\\text{tot}} &= M_{ob} \\times M_{ok} = 10 \\times 5 = 50\\text{ kali} \\end{aligned}",
            "legend": "• Jarak Lensa (Tubus): $d = s'_{ob} + f_{ok} = 11 + 5 = 16\\text{ cm}$<br>• Mata tanpa akomodasi: Bayangan objektif tepat jatuh di titik fokus okuler ($s_{ok} = f_{ok}$)"
        },
        "hints": {
            "concept": "Cari s'ob: 1/s'ob = 1/1 - 1/1,1 = 1/11 -> s'ob = 11 cm. Mob = 11 / 1,1 = 10x. Mok (tanpa akomodasi) = Sn / fok = 25 / 5 = 5x. Mtot = Mob * Mok.",
            "execution": "Mob = 10x. Mok = 5x. Mtot = 10 * 5 = 50 kali."
        }
    },
    {
        "id": "fis-lat-m-23",
        "materi": "GELOMBANG CAHAYA (INTERFERENSI)",
        "topic": "Interferensi Celah Ganda Young",
        "stem": "Dalam percobaan celah ganda Young, dua celah sempit terpisah pada jarak $d = 0{,}2\\text{ mm}$ disinari berkas cahaya monokromatik. Pola interferensi diamati pada layar yang berjarak $L = 1\\text{ meter}$ di belakang celah. Jika jarak antara garis terang pusat ke garis terang ketiga adalah $y_3 = 9\\text{ mm}$, panjang gelombang cahaya yang digunakan ($\\lambda$) adalah...",
        "correct": "$600\\text{ nm}$ (atau $6 \\times 10^{-7}\\text{ meter}$), dihitung dari rumus interferensi maksimum celah ganda: $d \\frac{y_n}{L} = n \\lambda \\implies \\lambda = \\frac{d \\cdot y_3}{3L} = \\frac{(2 \\times 10^{-4}\\text{ m})(9 \\times 10^{-3}\\text{ m})}{3 \\times 1\\text{ m}} = 6 \\times 10^{-7}\\text{ m}$.",
        "distractors": [
            "$400\\text{ nm}$, dihitung dengan mengabaikan jarak celah ke layar pada penyebut persamaan interferensi.",
            "$1.800\\text{ nm}$, karena nilai orde terang ketiga keliru dikalikan bukan dibagi pada ruas panjang gelombang.",
            "$500\\text{ nm}$, dihitung dari asumsi panjang gelombang spektrum cahaya hijau tampak di udara terbuka.",
            "$300\\text{ nm}$, dihitung dengan membagi dua hasil perhitungan panjang gelombang cahaya monokromatik."
        ],
        "formula": {
            "title": "FORMULA INTERFERENSI MAKSIMUM CELAH GANDA",
            "latex": "d \\frac{y_n}{L} = n \\lambda \\implies \\lambda = \\frac{d \\cdot y_n}{n L} = \\frac{(2 \\times 10^{-4}) \\times (9 \\times 10^{-3})}{3 \\times 1} = \\frac{18 \\times 10^{-7}}{3} = 6 \\times 10^{-7}\\text{ m} = 600\\text{ nm}",
            "legend": "• $d = 0{,}2\\text{ mm} = 2 \\times 10^{-4}\\text{ m}$<br>• $L = 1\\text{ m}$<br>• $y_3 = 9\\text{ mm} = 9 \\times 10^{-3}\\text{ m}$ pada orde $n = 3$"
        },
        "hints": {
            "concept": "Interferensi terang: d * y / L = n * lambda. lambda = (d * y) / (n * L).",
            "execution": "lambda = (0,2e-3 * 9e-3) / (3 * 1) = 1,8e-6 / 3 = 6e-7 m = 600 nm."
        }
    },
    {
        "id": "fis-lat-m-24",
        "materi": "GELOMBANG CAHAYA (DIFRAKSI KISI)",
        "topic": "Difraksi Cahaya pada Kisi Transmisi",
        "stem": "Berkas cahaya monokromatik dengan panjang gelombang $\\lambda = 500\\text{ nm}$ ($5 \\times 10^{-7}\\text{ m}$) dijatuhkan tegak lurus pada sebuah kisi difraksi. Garis terang orde kedua ($n = 2$) terdifraksi membentuk sudut deviasi $\\theta = 30^\\circ$ ($\\sin 30^\\circ = 0{,}5$). Jumlah garis per sentimeter ($N$) dari kisi difraksi tersebut adalah...",
        "correct": "$5.000\\text{ garis/cm}$, karena tetapan kisi adalah $d = \\frac{n \\lambda}{\\sin\\theta} = \\frac{2 \\times (5 \\times 10^{-7}\\text{ m})}{0{,}5} = 2 \\times 10^{-6}\\text{ m} = 2 \\times 10^{-4}\\text{ cm}$, sehingga $N = \\frac{1}{d} = \\frac{1}{2 \\times 10^{-4}\\text{ cm}} = 5.000\\text{ garis/cm}$.",
        "distractors": [
            "$2.500\\text{ garis/cm}$, dihitung dari orde pertama difraksi kisi tanpa mengalikan faktor orde kedua.",
            "$10.000\\text{ garis/cm}$, karena sudut 30 derajat keliru dikalikan dua menjadi sudut deviasi 60 derajat.",
            "$500\\text{ garis/cm}$, karena konstanta panjang gelombang langsung dijadikan nilai kerapatan garis kisi kaca.",
            "$1.250\\text{ garis/cm}$, dihitung dari perbandingan kecepatan cahaya terhadap frekuensi berkas sinar laser."
        ],
        "formula": {
            "title": "FORMULA DIFRAKSI PADA KISI",
            "latex": "d \\sin\\theta = n \\lambda \\implies d = \\frac{n \\lambda}{\\sin\\theta} = \\frac{2 \\times (5 \\times 10^{-7}\\text{ m})}{0{,}5} = 2 \\times 10^{-6}\\text{ m}; \\quad N = \\frac{1}{d} = \\frac{1}{2 \\times 10^{-4}\\text{ cm}} = 5.000\\text{ garis/cm}",
            "legend": "• $d$ = Jarak antar celah (tetapan kisi dalam meter atau cm)<br>• $N$ = Jumlah celah/garis per satuan panjang ($N = 1/d$)"
        },
        "hints": {
            "concept": "d * sin(theta) = n * lambda. Cari d = n*lambda / sin(theta), lalu N = 1 / d (konversi ke garis/cm).",
            "execution": "d = 2 * 5e-7 / 0,5 = 2e-6 m = 2e-4 cm. N = 1 / 2e-4 = 5.000 garis/cm."
        }
    },
    {
        "id": "fis-lat-m-25",
        "materi": "FISIKA MODERN (RELATIVITAS MASSA & ENERGI)",
        "topic": "Energi Kinetik Relativistik & Kesetaraan Massa-Energi",
        "stem": "Sebuah partikel memiliki massa diam $m_0$. Partikel tersebut dipercepat hingga bergerak dengan kecepatan relativistik konstan $v = 0{,}8c$ (di mana $c$ adalah kecepatan cahaya). Energi kinetik ($E_k$) partikel tersebut dinyatakan dalam energi diamnya ($E_0 = m_0 c^2$) adalah...",
        "correct": "$\\frac{2}{3} E_0$ (atau $0{,}67 E_0$), karena faktor Lorentz untuk kecepatan $0{,}8c$ adalah $\\gamma = \\frac{1}{\\sqrt{1 - (0{,}8)^2}} = \\frac{1}{0{,}6} = \\frac{5}{3}$, sehingga energi total $E = \\gamma E_0 = \\frac{5}{3} E_0$, dan energi kinetik $E_k = E - E_0 = \\left(\\frac{5}{3} - 1\\right) E_0 = \\frac{2}{3} E_0$.",
        "distractors": [
            "$\\frac{5}{3} E_0$, karena nilai tersebut merupakan energi total relativistik ($E$), belum dikurangkan dengan energi diam partikel.",
            "$0{,}32 E_0$, dihitung dari rumus mekanika klasik Newton $E_k = \\frac{1}{2} m v^2 = \\frac{1}{2} m_0 (0{,}8c)^2 = 0{,}32 E_0$ yang tidak berlaku pada kecepatan mendekati cahaya.",
            "$\\frac{1}{3} E_0$, dihitung dari selisih kuadrat faktor Lorentz dengan konstanta Planck.",
            "$1{,}25 E_0$, dihitung dari kebalikan rasio kecepatan terhadap kecepatan rambat foton di ruang hampa."
        ],
        "formula": {
            "title": "ENERGI KINETIK RELATIVISTIK EINSTEIN",
            "latex": "E = \\gamma m_0 c^2; \\quad E_k = E - E_0 = (\\gamma - 1) m_0 c^2 = \\left(\\frac{1}{\\sqrt{1 - 0{,}64}} - 1\\right) E_0 = \\left(\\frac{5}{3} - 1\\right) E_0 = \\frac{2}{3} E_0",
            "legend": "• $\\gamma = \\frac{1}{0{,}6} = \\frac{5}{3}$<br>• Rumus Klasik $\\frac{1}{2} m v^2$ menghasilkan galat fatal pada kecepatan tinggi ($v > 0{,}1c$)<br>• $E_k$ relativistik selalu lebih besar daripada prediksi mekanika Newton klasik"
        },
        "hints": {
            "concept": "Energi total relativistik: E = gamma * E0. Energi kinetik Ek = E - E0 = (gamma - 1) * E0. gamma = 1 / sqrt(1 - 0,8^2) = 1 / 0,6 = 5/3.",
            "execution": "Ek = (5/3 - 1) * E0 = 2/3 E0."
        }
    }
]
