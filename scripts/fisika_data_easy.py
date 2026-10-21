# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Fisika (SMA/MA Saintek)
Dataset: Easy Practice (25 Authentic Questions, fis-lat-e-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

FISIKA_EASY_ITEMS = [
    {
        "id": "fis-lat-e-01",
        "materi": "KINEMATIKA GERAK LURUS",
        "topic": "Gerak Lurus Berubah Beraturan (GLBB)",
        "stem": "Sebuah mobil listrik mula-mula diam di jalan tol yang lurus. Pengemudi menginjak pedal gas sehingga mobil mengalami percepatan konstan $a = 4\\text{ m/s}^2$ selama selang waktu $t = 5\\text{ sekon}$. Kecepatan akhir ($v_t$) dan jarak tempuh ($s$) yang dicapai mobil listrik tersebut pada akhir detik kelima adalah...",
        "correct": "Kecepatan akhir $v_t = 20\\text{ m/s}$ dan jarak tempuh $s = 50\\text{ meter}$, dihitung dari persamaan $v_t = v_0 + at$ dan $s = v_0 t + \\frac{1}{2}at^2$.",
        "distractors": [
            "Kecepatan akhir $v_t = 10\\text{ m/s}$ dan jarak tempuh $s = 20\\text{ meter}$, karena percepatan dihitung dengan membagi gaya baterai terhadap massa kendaraan.",
            "Kecepatan akhir $v_t = 40\\text{ m/s}$ dan jarak tempuh $s = 100\\text{ meter}$, dihitung dengan mengabaikan kecepatan awal nol pada spedometer.",
            "Kecepatan akhir $v_t = 25\\text{ m/s}$ dan jarak tempuh $s = 80\\text{ meter}$, karena hambatan angin diasumsikan konstan sebesar 15 Newton.",
            "Kecepatan akhir $v_t = 15\\text{ m/s}$ dan jarak tempuh $s = 45\\text{ meter}$, dihitung dari perkalian percepatan dengan gravitasi bumi."
        ],
        "formula": {
            "title": "PERSAMAAN KINEMATIKA GLBB",
            "latex": "v_t = v_0 + at; \\quad s = v_0 t + \\frac{1}{2}at^2; \\quad v_t^2 = v_0^2 + 2as",
            "legend": "• $v_0 = 0\\text{ m/s}$, $a = 4\\text{ m/s}^2$, $t = 5\\text{ s}$<br>• $v_t = 0 + (4 \\times 5) = 20\\text{ m/s}$<br>• $s = 0 + \\frac{1}{2}(4)(5^2) = 2 \\times 25 = 50\\text{ m}$"
        },
        "hints": {
            "concept": "Gunakan persamaan GLBB gerak lurus dengan kecepatan awal v0 = 0.",
            "execution": "vt = a * t = 4 * 5 = 20 m/s; s = 0.5 * a * t^2 = 0.5 * 4 * 25 = 50 m."
        }
    },
    {
        "id": "fis-lat-e-02",
        "materi": "DINAMIKA GERAK NEWTON",
        "topic": "Hukum II Newton pada Bidang Datar Licin",
        "stem": "Dua buah balok $m_1 = 3\\text{ kg}$ dan $m_2 = 2\\text{ kg}$ diletakkan berdampingan bersentuhan di atas lantai mendatar licin tanpa gesekan. Balok $m_1$ didorong dengan gaya horizontal konstan $F = 25\\text{ N}$ ke kanan. Besar percepatan sistem dan besar gaya kontak antara kedua balok tersebut adalah...",
        "correct": "Percepatan sistem $a = 5\\text{ m/s}^2$ dan gaya kontak antaran balok sebesar $N_{12} = 10\\text{ N}$, di mana gaya dorong diteruskan oleh balok pertama untuk mempercepat balok kedua bermassa 2 kg.",
        "distractors": [
            "Percepatan sistem $a = 2{,}5\\text{ m/s}^2$ dan gaya kontak $N_{12} = 25\\text{ N}$, karena gaya aksi-reaksi menahan seluruh pergerakan balok pertama.",
            "Percepatan sistem $a = 8{,}3\\text{ m/s}^2$ dan gaya kontak $N_{12} = 15\\text{ N}$, dihitung dengan mengalikan massa total dengan percepatan gravitasi bumi.",
            "Percepatan sistem $a = 10\\text{ m/s}^2$ dan gaya kontak $N_{12} = 5\\text{ N}$, karena massa balok kedua dianggap nol di bidang tanpa gesek.",
            "Percepatan sistem $a = 1\\text{ m/s}^2$ dan gaya kontak $N_{12} = 20\\text{ N}$, diperoleh dari selisih kedua massa dikalikan gaya luar."
        ],
        "formula": {
            "title": "HUKUM II NEWTON SISTEM TERKOPEL",
            "latex": "a = \\frac{F}{m_1 + m_2} = \\frac{25}{3 + 2} = 5\\text{ m/s}^2; \\quad N_{12} = m_2 \\cdot a = 2 \\times 5 = 10\\text{ N}",
            "legend": "• Gaya Eksternal: $F = 25\\text{ N}$<br>• Massa Total: $3 + 2 = 5\\text{ kg}$<br>• Gaya Kontak pada $m_2$: $\\Sigma F_2 = m_2 a \\implies N_{12} = 2 \\times 5 = 10\\text{ N}$"
        },
        "hints": {
            "concept": "Percepatan = F / (m1 + m2). Tinjau balok m2 untuk mencari gaya kontak: N12 = m2 * a.",
            "execution": "a = 25 / 5 = 5 m/s²; N12 = 2 * 5 = 10 N."
        }
    },
    {
        "id": "fis-lat-e-03",
        "materi": "USAHA DAN ENERGI",
        "topic": "Hukum Kekekalan Energi Mekanik (Gerak Jatuh Bebas)",
        "stem": "Sebuah buah kelapa bermassa $m = 2\\text{ kg}$ jatuh bebas dari pucuk pohonnya pada ketinggian $h = 20\\text{ meter}$ di atas permukaan tanah ($g = 10\\text{ m/s}^2$). Mengabaikan hambatan gesekan udara, energi kinetik ($E_k$) kelapa saat berada pada ketinggian $5\\text{ meter}$ dari tanah adalah...",
        "correct": "$300\\text{ Joule}$, karena penurunan energi potensial sebesar $\\Delta E_p = mg(h_1 - h_2) = 2 \\times 10 \\times (20 - 5) = 300\\text{ J}$ berubah seluruhnya menjadi energi kinetik.",
        "distractors": [
            "$400\\text{ Joule}$, karena seluruh energi potensial di puncak pohon langsung menjadi energi kinetik tanpa memperhatikan sisa ketinggian.",
            "$100\\text{ Joule}$, dihitung dari energi potensial yang tersisa di posisi lima meter di atas permukaan tanah.",
            "$200\\text{ Joule}$, dihitung dari hasil kali massa kelapa dengan kecepatan angin rata-rata di perkebunan.",
            "$50\\text{ Joule}$, karena gravitasi bumi mengalami pengurangan daya tarik seiring bertambahnya kelajuan benda."
        ],
        "formula": {
            "title": "KEKEKALAN ENERGI MEKANIK",
            "latex": "E_{m1} = E_{m2} \\implies mgh_1 + 0 = mgh_2 + E_{k2} \\implies E_{k2} = mg(h_1 - h_2)",
            "legend": "• $E_{p1} = 2 \\times 10 \\times 20 = 400\\text{ J}$<br>• $E_{p2} = 2 \\times 10 \\times 5 = 100\\text{ J}$<br>• $E_{k2} = 400 - 100 = 300\\text{ J}$"
        },
        "hints": {
            "concept": "Energi mekanik kekal: Ek2 = Ep1 - Ep2 = mg(h1 - h2).",
            "execution": "Ek2 = 2 * 10 * (20 - 5) = 20 * 15 = 300 Joule."
        }
    },
    {
        "id": "fis-lat-e-04",
        "materi": "MOMENTUM DAN IMPULS",
        "topic": "Impuls dan Perubahan Momentum",
        "stem": "Sebuah bola kasti bermassa $m = 0{,}15\\text{ kg}$ melaju horizontal ke kiri dengan kecepatan $v_1 = 20\\text{ m/s}$. Pemukul memukul bola tersebut sehingga bola berbalik arah melaju ke kanan dengan kecepatan $v_2 = 30\\text{ m/s}$. Jika waktu kontak pemukul dengan bola adalah $\\Delta t = 0{,}01\\text{ sekon}$, besar gaya rata-rata yang diberikan pemukul pada bola adalah...",
        "correct": "$750\\text{ Newton}$, diperoleh dari perubahan momentum $\\Delta p = m(v_2 - v_1) = 0{,}15 \\times (30 - (-20)) = 7{,}5\\text{ N}\\cdot\\text{s}$, dibagi waktu kontak $0{,}01\\text{ s}$.",
        "distractors": [
            "$150\\text{ Newton}$, dihitung dengan mengurangkan kelajuan akhir dan kelajuan awal sebagai besaran skalar biasa tanpa arah.",
            "$300\\text{ Newton}$, karena massa bola kasti dibagi langsung dengan percepatan gravitasi bumi di lapangan.",
            "$500\\text{ Newton}$, dihitung dari energi kinetik bola dibagi dengan selang waktu tumbukan mikroskopis.",
            "$75\\text{ Newton}$, karena tanda arah kecepatan berlawanan diabaikan dalam perhitungan impuls mekanika."
        ],
        "formula": {
            "title": "TEOREMA IMPULS-MOMENTUM",
            "latex": "I = \\bar{F} \\Delta t = \\Delta p = m(v_2 - v_1) \\implies \\bar{F} = \\frac{m(v_2 - v_1)}{\\Delta t}",
            "legend": "• Ambil arah kanan sebagai positif: $v_1 = -20\\text{ m/s}$, $v_2 = +30\\text{ m/s}$<br>• $\\Delta p = 0{,}15 \\times (30 - (-20)) = 0{,}15 \\times 50 = 7{,}5\\text{ N}\\cdot\\text{s}$<br>• $\\bar{F} = \\frac{7{,}5}{0{,}01} = 750\\text{ N}$"
        },
        "hints": {
            "concept": "Kecepatan adalah besaran vektor. Bola berbalik arah: delta_v = v2 - (-v1) = 30 - (-20) = 50 m/s. F = m * delta_v / delta_t.",
            "execution": "F = 0,15 * 50 / 0,01 = 7,5 / 0,01 = 750 N."
        }
    },
    {
        "id": "fis-lat-e-05",
        "materi": "FLUIDA STATIS",
        "topic": "Tekanan Hidrostatis pada Dasar Bejana",
        "stem": "Sebuah tabung silinder vertikal berisi cairan minyak goreng dengan massa jenis $\\rho = 800\\text{ kg/m}^3$ setinggi $h = 75\\text{ cm}$. Jika percepatan gravitasi bumi $g = 10\\text{ m/s}^2$ dan tekanan udara atmosfer diabaikan, besar tekanan hidrostatis yang dialami oleh dasar tabung tersebut adalah...",
        "correct": "$6.000\\text{ Pascal}$ (atau $6\\text{ kPa}$), dihitung dari rumus tekanan hidrostatis $P_h = \\rho g h = 800 \\times 10 \\times 0{,}75\\text{ m}$.",
        "distractors": [
            "$60.000\\text{ Pascal}$, karena ketinggian 75 cm keliru dimasukkan dalam satuan sentimeter tanpa dikonversi ke meter.",
            "$8.000\\text{ Pascal}$, dihitung dari massa jenis minyak dikalikan dengan percepatan gravitasi tanpa memperhitungkan kedalaman.",
            "$7.500\\text{ Pascal}$, dihitung dari tinggi cairan dikalikan 100 tanpa memperhatikan massa jenis fluida.",
            "$1.200\\text{ Pascal}$, hasil pembagian massa jenis minyak dengan ketinggian kolom cairan di dalam tabung."
        ],
        "formula": {
            "title": "FORMULA TEKANAN HIDROSTATIS",
            "latex": "P_h = \\rho \\cdot g \\cdot h = 800\\text{ kg/m}^3 \\times 10\\text{ m/s}^2 \\times 0{,}75\\text{ m} = 6.000\\text{ N/m}^2 \\text{ (Pa)}",
            "legend": "• $\\rho = 800\\text{ kg/m}^3$<br>• $g = 10\\text{ m/s}^2$<br>• $h = 75\\text{ cm} = 0{,}75\\text{ m}$<br>• $P_h = 6.000\\text{ Pa} = 6\\text{ kPa}$"
        },
        "hints": {
            "concept": "Tekanan hidrostatis: P = rho * g * h. Konversi cm ke meter: 75 cm = 0,75 m.",
            "execution": "P = 800 * 10 * 0,75 = 6000 Pa."
        }
    },
    {
        "id": "fis-lat-e-06",
        "materi": "FLUIDA STATIS",
        "topic": "Hukum Pascal pada Dongkrak Hidrolik",
        "stem": "Sebuah dongkrak hidrolik memiliki dua penampang piston berbentuk lingkaran. Piston kecil memiliki luas penampang $A_1 = 10\\text{ cm}^2$ dan piston besar memiliki luas $A_2 = 250\\text{ cm}^2$. Jika pada piston kecil diberikan gaya tekan $F_1 = 80\\text{ N}$, beban maksimum bermassa $M$ yang dapat diangkat pada piston besar ($g = 10\\text{ m/s}^2$) adalah...",
        "correct": "$200\\text{ kg}$, karena gaya angkat pada piston besar adalah $F_2 = F_1 \\times \\frac{A_2}{A_1} = 80 \\times 25 = 2.000\\text{ N}$, yang setara dengan beban bermassa $M = \\frac{F_2}{g} = 200\\text{ kg}$.",
        "distractors": [
            "$2.000\\text{ kg}$, karena gaya angkat 2.000 Newton keliru disamakan langsung dengan massa beban tanpa dibagi percepatan gravitasi.",
            "$80\\text{ kg}$, karena hukum Pascal mengasumsikan gaya tekan selalu sama di kedua piston tanpa penguatan mekanik.",
            "$25\\text{ kg}$, dihitung dari perbandingan rasio luas penampang piston besar terhadap piston kecil.",
            "$500\\text{ kg}$, dihitung dari perkalian luas penampang piston besar dengan percepatan gravitasi bumi."
        ],
        "formula": {
            "title": "HUKUM PASCAL BEJANA BERHUBUNGAN",
            "latex": "\\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\left(\\frac{A_2}{A_1}\\right); \\quad M = \\frac{F_2}{g}",
            "legend": "• $F_2 = 80 \\times \\frac{250}{10} = 80 \\times 25 = 2.000\\text{ N}$<br>• $M = \\frac{2.000\\text{ N}}{10\\text{ m/s}^2} = 200\\text{ kg}$"
        },
        "hints": {
            "concept": "Hukum Pascal: F1 / A1 = F2 / A2. Massa M = F2 / g.",
            "execution": "F2 = 80 * (250 / 10) = 2000 N. M = 2000 / 10 = 200 kg."
        }
    },
    {
        "id": "fis-lat-e-07",
        "materi": "FLUIDA STATIS",
        "topic": "Hukum Archimedes & Gaya Apung",
        "stem": "Sebuah balok kayu bervolume total $V = 0{,}02\\text{ m}^3$ terapung di permukaan air tawar ($\\rho_{\\text{air}} = 1.000\\text{ kg/m}^3$). Jika $\\frac{3}{4}$ bagian volume balok tercelup di dalam air dan $g = 10\\text{ m/s}^2$, besar gaya apung (gaya ke atas Archimedes) yang bekerja pada balok kayu tersebut adalah...",
        "correct": "$150\\text{ Newton}$, dihitung dari berat fluida yang dipindahkan: $F_A = \\rho_{\\text{air}} \\cdot g \\cdot V_{\\text{celup}} = 1.000 \\times 10 \\times (0{,}75 \\times 0{,}02\\text{ m}^3)$.",
        "distractors": [
            "$200\\text{ Newton}$, dihitung dengan menggunakan volume total balok seolah-olah seluruh balok tenggelam ke dasar bejana.",
            "$50\\text{ Newton}$, dihitung dari seperempat volume balok kayu yang menyembul di atas permukaan air terbuka.",
            "$1.500\\text{ Newton}$, karena percepatan gravitasi dikalikan kuadrat massa jenis air danau.",
            "$75\\text{ Newton}$, dihitung dari pembagian massa jenis air dengan percepatan gravitasi bumi."
        ],
        "formula": {
            "title": "HUKUM ARCHIMEDES GAYA APUNG",
            "latex": "F_A = \\rho_f \\cdot g \\cdot V_{\\text{tercelup}} = 1.000 \\times 10 \\times (0{,}75 \\times 0{,}02) = 10.000 \\times 0{,}015 = 150\\text{ N}",
            "legend": "• $V_{\\text{tercelup}} = \\frac{3}{4} \\times 0{,}02 = 0{,}015\\text{ m}^3$<br>• $F_A = 1.000 \\times 10 \\times 0{,}015 = 150\\text{ N}$"
        },
        "hints": {
            "concept": "Gaya Archimedes hanya bergantung pada volume yang tercelup: Fa = rho_fluida * g * V_tercelup.",
            "execution": "V_tercelup = 0,75 * 0,02 = 0,015 m³. Fa = 1000 * 10 * 0,015 = 150 N."
        }
    },
    {
        "id": "fis-lat-e-08",
        "materi": "SUHU DAN KALOR",
        "topic": "Asas Black pada Pencampuran Air",
        "stem": "Sebanyak $200\\text{ gram}$ air bersuhu $80^\\circ\\text{C}$ dicampurkan dengan $300\\text{ gram}$ air bersuhu $20^\\circ\\text{C}$ di dalam bejana kalorimeter ideal tanpa kehilangan kalor ke lingkungan. Jika kalor jenis air $c = 1\\text{ kal/g}\\cdot^\\circ\\text{C}$, suhu akhir kesetimbangan termal campuran tersebut adalah...",
        "correct": "$44^\\circ\\text{C}$, dihitung berdasarkan Asas Black $Q_{\\text{lepas}} = Q_{\\text{terima}} \\implies 200(80 - T_c) = 300(T_c - 20)$, yang menghasilkan $16.000 - 200T_c = 300T_c - 6.000 \\implies 500T_c = 22.000$.",
        "distractors": [
            "$50^\\circ\\text{C}$, karena suhu akhir diasumsikan sebagai nilai rata-rata aritmatika sederhana antara 80°C dan 20°C.",
            "$35^\\circ\\text{C}$, dihitung dengan mengabaikan massa air panas yang memiliki suhu lebih tinggi.",
            "$60^\\circ\\text{C}$, karena kalor dianggap hanya berpindah ke dinding wadah kalorimeter kaca.",
            "$40^\\circ\\text{C}$, dihitung dari perbandingan volume kedua cairan tanpa memperhitungkan kalor jenis air."
        ],
        "formula": {
            "title": "ASAS BLACK KESETIMBANGAN TERMAL",
            "latex": "Q_{\\text{lepas}} = Q_{\\text{terima}} \\implies m_1 c (T_1 - T_c) = m_2 c (T_c - T_2)",
            "legend": "• $200 \\times (80 - T_c) = 300 \\times (T_c - 20)$<br>• $16.000 - 200T_c = 300T_c - 6.000$<br>• $500T_c = 22.000 \\implies T_c = 44^\\circ\\text{C}$"
        },
        "hints": {
            "concept": "Kalor yang dilepas air panas = Kalor yang diserap air dingin. m1*(T1 - Tc) = m2*(Tc - T2).",
            "execution": "200*(80 - Tc) = 300*(Tc - 20) -> 16000 - 200Tc = 300Tc - 6000 -> 500Tc = 22000 -> Tc = 44°C."
        }
    },
    {
        "id": "fis-lat-e-09",
        "materi": "TERMODINAMIKA GAS",
        "topic": "Hukum Pertama Termodinamika (Proses Isobarik)",
        "stem": "Suatu gas ideal berada dalam ruang tertutup bertekanan tetap $P = 2 \\times 10^5\\text{ N/m}^2$. Gas mengalami pemuaian isobarik sehingga volumenya bertambah dari $V_1 = 0{,}02\\text{ m}^3$ menjadi $V_2 = 0{,}05\\text{ m}^3$. Selama proses tersebut, gas menyerap kalor sebesar $Q = 9.000\\text{ Joule}$. Perubahan energi dalam ($\\Delta U$) gas ideal tersebut adalah...",
        "correct": "$3.000\\text{ Joule}$, karena usaha luar yang dilakukan gas adalah $W = P\\Delta V = 2 \\times 10^5 \\times (0{,}05 - 0{,}02) = 6.000\\text{ J}$, sehingga $\\Delta U = Q - W = 9.000 - 6.000 = 3.000\\text{ J}$.",
        "distractors": [
            "$15.000\\text{ Joule}$, diperoleh dari penjumlahan langsung antara kalor yang diserap dengan usaha ekspansi gas.",
            "$6.000\\text{ Joule}$, karena nilai perubahan energi dalam keliru disamakan dengan usaha mekanik piston.",
            "$9.000\\text{ Joule}$, dengan asumsi seluruh kalor yang diserap gas tidak digunakan untuk melakukan usaha luar.",
            "$1.500\\text{ Joule}$, dihitung dari pembagian kalor serap dengan rasio ekspansi volume gas ideal."
        ],
        "formula": {
            "title": "HUKUM I TERMODINAMIKA (ISOBARIK)",
            "latex": "W = P \\Delta V; \\quad \\Delta U = Q - W = Q - P(V_2 - V_1)",
            "legend": "• $W = (2 \\times 10^5) \\times (0{,}05 - 0{,}02) = 2 \\times 10^5 \\times 0{,}03 = 6.000\\text{ J}$<br>• $\\Delta U = 9.000 - 6.000 = 3.000\\text{ J}$"
        },
        "hints": {
            "concept": "Hukum I Termodinamika: delta_U = Q - W. Pada proses isobarik, W = P * delta_V.",
            "execution": "W = 2e5 * 0,03 = 6000 J. delta_U = 9000 - 6000 = 3000 J."
        }
    },
    {
        "id": "fis-lat-e-10",
        "materi": "GELOMBANG MEKANIK",
        "topic": "Persamaan Gelombang Berjalan",
        "stem": "Sebuah gelombang transversal merambat pada tali dengan persamaan simpangan $y = 0{,}08 \\sin(4\\pi t - 2\\pi x)$, di mana $x$ dan $y$ dalam meter serta $t$ dalam sekon. Amplitudo ($A$), frekuensi ($f$), dan panjang gelombang ($\\lambda$) dari gelombang tersebut berturut-turut adalah...",
        "correct": "$A = 0{,}08\\text{ m}$, $f = 2\\text{ Hz}$, dan $\\lambda = 1\\text{ meter}$, diperoleh dari $\\omega = 4\\pi \\implies f = \\frac{\\omega}{2\\pi} = 2\\text{ Hz}$, dan $k = 2\\pi \\implies \\lambda = \\frac{2\\pi}{k} = 1\\text{ m}$.",
        "distractors": [
            "$A = 0{,}08\\text{ m}$, $f = 4\\text{ Hz}$, dan $\\lambda = 2\\text{ meter}$, karena konstanta di depan t keliru dianggap frekuensi langsung tanpa dibagi 2pi.",
            "$A = 0{,}8\\text{ m}$, $f = 1\\text{ Hz}$, dan $\\lambda = 4\\text{ meter}$, dihitung dari perbandingan koefisien sudut fase pada fungsi sinus.",
            "$A = 0{,}04\\text{ m}$, $f = 2\\text{ Hz}$, dan $\\lambda = 0{,}5\\text{ meter}$, karena amplitudo gelombang dibagi dua akibat efek simetri getaran.",
            "$A = 0{,}08\\text{ m}$, $f = 0{,}5\\text{ Hz}$, dan $\\lambda = 2\\text{ meter}$, dihitung dari kebalikan kecepatan sudut getaran tali."
        ],
        "formula": {
            "title": "PARAMETER GELOMBANG BERJALAN",
            "latex": "y = A \\sin(\\omega t - kx); \\quad f = \\frac{\\omega}{2\\pi}; \\quad \\lambda = \\frac{2\\pi}{k}; \\quad v = \\frac{\\omega}{k}",
            "legend": "• $A = 0{,}08\\text{ m}$<br>• $\\omega = 4\\pi \\implies f = \\frac{4\\pi}{2\\pi} = 2\\text{ Hz}$<br>• $k = 2\\pi \\implies \\lambda = \\frac{2\\pi}{2\\pi} = 1\\text{ m}$"
        },
        "hints": {
            "concept": "Bandingkan persamaan dengan y = A sin(omega*t - k*x). omega = 2*pi*f, k = 2*pi / lambda.",
            "execution": "A = 0,08 m; f = 4pi / 2pi = 2 Hz; lambda = 2pi / 2pi = 1 m."
        }
    },
    {
        "id": "fis-lat-e-11",
        "materi": "GELOMBANG BUNYI",
        "topic": "Taraf Intensitas Bunyi Sumber Jamak",
        "stem": "Taraf intensitas bunyi sebuah sepeda motor knalpot standar pada jarak tertentu adalah $TI_1 = 60\\text{ dB}$. Jika terdapat 100 sepeda motor identik yang dihidupkan secara bersamaan di tempat yang sama, taraf intensitas bunyi total ($TI_{100}$) yang didengar pada jarak tersebut adalah...",
        "correct": "$80\\text{ dB}$, karena pertambahan taraf intensitas untuk $n = 100$ sumber identik adalah $10\\log_{10}(n) = 10\\log_{10}(100) = 10 \\times 2 = 20\\text{ dB}$, sehingga $TI_{100} = 60 + 20 = 80\\text{ dB}$.",
        "distractors": [
            "$600\\text{ dB}$, karena taraf intensitas keliru dikalikan langsung dengan 100 secara linier.",
            "$160\\text{ dB}$, dihitung dengan menambahkan 100 desibel secara langsung ke taraf intensitas satu motor.",
            "$70\\text{ dB}$, karena penambahan sumber bunyi dianggap hanya menaikkan 10 desibel untuk setiap kelipatan seratus.",
            "$120\\text{ dB}$, dihitung dari perkalian taraf intensitas tunggal dengan faktor kuadrat logaritma natural."
        ],
        "formula": {
            "title": "TARAF INTENSITAS N SUMBER IDENTIK",
            "latex": "TI_n = TI_1 + 10\\log_{10}(n) = 60 + 10\\log_{10}(100) = 60 + 10(2) = 80\\text{ dB}",
            "legend": "• Skala Logaritmik Bunyi: Kenaikan 10 dB setara kelipatan intensitas 10 kali lipat<br>• Kenaikan 20 dB setara kelipatan intensitas $10^2 = 100$ kali lipat"
        },
        "hints": {
            "concept": "Taraf intensitas bertambah secara logaritmik: TIn = TI1 + 10*log10(n).",
            "execution": "TI100 = 60 + 10 * log10(100) = 60 + 10 * 2 = 80 dB."
        }
    },
    {
        "id": "fis-lat-e-12",
        "materi": "LISTRIK STATIS",
        "topic": "Hukum Coulomb Dua Muatan Titik",
        "stem": "Dua buah muatan titik $q_1 = +4\\,\\mu\\text{C}$ dan $q_2 = +9\\,\\mu\\text{C}$ terpisah pada jarak $r = 30\\text{ cm}$ di udara bebas ($k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2\\text{/C}^2$). Besar gaya tolak-menolak Coulomb antara kedua muatan tersebut adalah...",
        "correct": "$3{,}6\\text{ Newton}$, dihitung dari hukum Coulomb $F = k \\frac{q_1 q_2}{r^2} = 9 \\times 10^9 \\times \\frac{(4 \\times 10^{-6})(9 \\times 10^{-6})}{(0{,}3)^2} = \\frac{0{,}324}{0{,}09} = 3{,}6\\text{ N}$.",
        "distractors": [
            "$360\\text{ Newton}$, karena jarak 30 cm keliru dimasukkan tanpa dikonversi ke meter (menggunakan 30 bukan 0,3).",
            "$0{,}36\\text{ Newton}$, dihitung dengan mengabaikan konstanta dielektrik ruang hampa udara.",
            "$1{,}2\\text{ Newton}$, diperoleh dari rata-rata kedua nilai muatan dibagi kuadrat jarak pemisah.",
            "$10{,}8\\text{ Newton}$, dihitung dari perkalian muatan dengan jarak tanpa menerapkan kuadrat pada penyebut."
        ],
        "formula": {
            "title": "HUKUM COULOMB GAYA ELEKTROSTATIK",
            "latex": "F = k \\frac{|q_1 q_2|}{r^2} = (9 \\times 10^9) \\frac{(4 \\times 10^{-6})(9 \\times 10^{-6})}{(0{,}3)^2} = \\frac{324 \\times 10^{-3}}{0{,}09} = 3{,}6\\text{ N}",
            "legend": "• $q_1 = 4 \\times 10^{-6}\\text{ C}$, $q_2 = 9 \\times 10^{-6}\\text{ C}$<br>• $r = 30\\text{ cm} = 0{,}3\\text{ m} \\implies r^2 = 0{,}09\\text{ m}^2$<br>• Kedua muatan sejenis (positif) $\\implies$ Saling tolak-menolak"
        },
        "hints": {
            "concept": "F = k * q1 * q2 / r^2. Ingat konversi: microCoulomb = 10^-6 C, dan cm ke m: 30 cm = 0,3 m.",
            "execution": "F = 9e9 * (4e-6 * 9e-6) / (0,3)^2 = 0,324 / 0,09 = 3,6 N."
        }
    },
    {
        "id": "fis-lat-e-13",
        "materi": "LISTRIK DINAMIS",
        "topic": "Hukum Ohm & Hambatan Rangkaian Seri-Paralel",
        "stem": "Dua buah resistor $R_1 = 6\\,\\Omega$ dan $R_2 = 3\\,\\Omega$ dirangkai secara paralel, kemudian rangkaian tersebut dihubungkan seri dengan resistor $R_3 = 8\\,\\Omega$. Rangkaian gabungan ini dipasang pada sumber tegangan $V = 20\\text{ Volt}$ dengan hambatan dalam baterai diabaikan. Kuat arus total ($I$) yang keluar dari sumber tegangan adalah...",
        "correct": "$2\\text{ Ampere}$, karena hambatan pengganti paralel adalah $R_p = \\frac{6 \\times 3}{6 + 3} = 2\\,\\Omega$, sehingga hambatan total rangkaian adalah $R_{\\text{total}} = 2 + 8 = 10\\,\\Omega$, dan arus $I = \\frac{V}{R_{\\text{total}}} = \\frac{20}{10} = 2\\text{ A}$.",
        "distractors": [
            "$1{,}18\\text{ Ampere}$, karena seluruh resistor dijumlahkan secara seri biasa menghasilkan hambatan 17 Ohm.",
            "$4\\text{ Ampere}$, dihitung dengan mengabaikan resistor ketiga dalam penentuan arus utama.",
            "$0{,}5\\text{ Ampere}$, dihitung dari pembagian hambatan total dengan kuadrat tegangan sumber listrik.",
            "$10\\text{ Ampere}$, dihitung dari nilai tegangan dibagi oleh hambatan paralel tanpa menambahkan resistor seri."
        ],
        "formula": {
            "title": "HAMBATAN PENGGANTI KOMBINASI",
            "latex": "R_p = \\frac{R_1 R_2}{R_1 + R_2} = \\frac{6 \\times 3}{6 + 3} = 2\\,\\Omega; \\quad R_{\\text{tot}} = R_p + R_3 = 2 + 8 = 10\\,\\Omega; \\quad I = \\frac{V}{R_{\\text{tot}}} = \\frac{20}{10} = 2\\text{ A}",
            "legend": "• $R_p = 2\\,\\Omega$<br>• $R_{\\text{tot}} = 10\\,\\Omega$<br>• Arus Total: $I = 2\\text{ A}$"
        },
        "hints": {
            "concept": "Cari hambatan paralel R1 dan R2: Rp = (6*3)/(6+3) = 2 Ohm. Lalu seri dengan R3: Rtot = 2 + 8 = 10 Ohm. I = V / Rtot.",
            "execution": "Rp = 2 Ohm. Rtot = 10 Ohm. I = 20 / 10 = 2 A."
        }
    },
    {
        "id": "fis-lat-e-14",
        "materi": "KEMAGNETAN",
        "topic": "Gaya Lorentz pada Kawat Lurus Berarus",
        "stem": "Sebuah kawat penghantar lurus mendatar berpanjang $L = 50\\text{ cm}$ dialiri arus listrik $I = 4\\text{ Ampere}$ dari arah barat ke timur. Kawat tersebut berada di dalam medan magnet homogen $B = 0{,}6\\text{ Tesla}$ yang berarah tegak lurus masuk ke dalam bidang kertas. Besar dan arah gaya Lorentz yang bekerja pada kawat tersebut adalah...",
        "correct": "$1{,}2\\text{ Newton}$ ke arah utara (ke atas bidang), dihitung dari rumus $F = B I L \\sin 90^\\circ = 0{,}6 \\times 4 \\times 0{,}5\\text{ m} = 1{,}2\\text{ N}$, dengan aturan kaidah tangan kanan.",
        "distractors": [
            "$120\\text{ Newton}$ ke arah selatan, karena panjang kawat 50 cm keliru dimasukkan tanpa konversi ke satuan meter.",
            "$1{,}2\\text{ Newton}$ ke arah bawah (selatan), karena aturan kaidah tangan kanan tertukar dengan tangan kiri.",
            "$2{,}4\\text{ Newton}$ ke arah timur, dihitung dari perkalian arus listrik dengan kuadrat kuat medan magnetik.",
            "$0{,}6\\text{ Newton}$ ke arah barat, karena medan magnet diasumsikan berlawanan arah dengan arah arus kawat."
        ],
        "formula": {
            "title": "GAYA LORENTZ PADA KAWAT BERARUS",
            "latex": "F = B \\cdot I \\cdot L \\cdot \\sin\\theta = 0{,}6\\text{ T} \\times 4\\text{ A} \\times 0{,}5\\text{ m} \\times \\sin 90^\\circ = 1{,}2\\text{ N}",
            "legend": "• $L = 50\\text{ cm} = 0{,}5\\text{ m}$<br>• Kaidah Tangan Kanan: Ibu jari = Arus (Timur), 4 Jari = Medan B (Masuk), Telapak tangan = Gaya F (Utara/Atas)"
        },
        "hints": {
            "concept": "Gaya Lorentz: F = B * I * L * sin(theta). Arah gaya ditentukan dengan kaidah tangan kanan: arus ke kanan, B masuk bidang -> gaya ke atas (utara).",
            "execution": "F = 0,6 * 4 * 0,5 = 1,2 N arah ke utara."
        }
    },
    {
        "id": "fis-lat-e-15",
        "materi": "INDUKSI ELEKTROMAGNETIK",
        "topic": "GGL Induksi Hukum Faraday pada Kumparan",
        "stem": "Sebuah kumparan kawat memiliki $N = 200\\text{ lilitan}$. Fluks magnetik yang menembus kumparan tersebut berubah dari $\\Phi_1 = 0{,}08\\text{ Weber}$ menjadi $\\Phi_2 = 0{,}02\\text{ Weber}$ dalam selang waktu $\\Delta t = 0{,}2\\text{ sekon}$. Besar gaya gerak listrik (GGL) induksi rata-rata yang timbul pada ujung-ujung kumparan adalah...",
        "correct": "$60\\text{ Volt}$, dihitung dari Hukum Faraday: $\\varepsilon = -N \\frac{\\Delta\\Phi}{\\Delta t} = -200 \\times \\frac{0{,}02 - 0{,}08}{0{,}2} = -200 \\times (-0{,}3) = 60\\text{ V}$.",
        "distractors": [
            "$6\\text{ Volt}$, karena jumlah lilitan keliru dimasukkan hanya 20 lilitan dalam rumus perhitungan ggl.",
            "$120\\text{ Volt}$, dihitung dari perkalian jumlah lilitan dengan fluks awal tanpa memperhitungkan fluks akhir.",
            "$30\\text{ Volt}$, diperoleh dari pembagian selisih fluks magnetik dengan kuadrat selang waktu pengamatan.",
            "$600\\text{ Volt}$, karena selang waktu 0,2 sekon keliru dikalikan ke pembilang bukan sebagai pembagi."
        ],
        "formula": {
            "title": "HUKUM FARADAY GGL INDUKSI",
            "latex": "\\varepsilon = -N \\frac{\\Delta \\Phi}{\\Delta t} = -200 \\left(\\frac{0{,}02 - 0{,}08}{0{,}2}\\right) = -200 \\left(\\frac{-0{,}06}{0{,}2}\\right) = 60\\text{ Volt}",
            "legend": "• Tanda negatif (Hukum Lenz) menunjukkan arah GGL induksi selalu menentang perubahan fluks penyebabnya<br>• Besar GGL Induksi: $|\\varepsilon| = 60\\text{ V}$"
        },
        "hints": {
            "concept": "GGL Induksi Faraday: eps = N * |delta_phi| / delta_t. delta_phi = 0,08 - 0,02 = 0,06 Wb.",
            "execution": "eps = 200 * 0,06 / 0,2 = 200 * 0,3 = 60 Volt."
        }
    },
    {
        "id": "fis-lat-e-16",
        "materi": "TRANSFORMATOR",
        "topic": "Efisiensi dan Rasio Trafo Step-Down",
        "stem": "Sebuah transformator step-down ideal (efisiensi $\\eta = 100\\%$) menurunkan tegangan bolak-balik dari $V_p = 220\\text{ Volt}$ menjadi $V_s = 22\\text{ Volt}$. Jika kumparan primer terdiri atas $N_p = 1.000\\text{ lilitan}$ dan arus yang mengalir pada kumparan sekunder adalah $I_s = 5\\text{ Ampere}$, maka jumlah lilitan sekunder ($N_s$) dan kuat arus primer ($I_p$) adalah...",
        "correct": "$N_s = 100\\text{ lilitan}$ dan $I_p = 0{,}5\\text{ Ampere}$, karena perbandingan lilitan sebanding dengan perbandingan tegangan ($\\frac{N_s}{N_p} = \\frac{22}{220} = \\frac{1}{10}$), dan daya trafo ideal $P_p = P_s \\implies V_p I_p = V_s I_s$.",
        "distractors": [
            "$N_s = 10.000\\text{ lilitan}$ dan $I_p = 50\\text{ Ampere}$, karena trafo step-down keliru dianggap menaikkan jumlah lilitan sekunder.",
            "$N_s = 100\\text{ lilitan}$ dan $I_p = 5\\text{ Ampere}$, dengan anggapan bahwa arus primer selalu identik dengan arus sekunder.",
            "$N_s = 500\\text{ lilitan}$ dan $I_p = 2{,}5\\text{ Ampere}$, dihitung dari rata-rata nilai tegangan masukan.",
            "$N_s = 50\\text{ lilitan}$ dan $I_p = 1\\text{ Ampere}$, dihitung dari selisih daya primer dan sekunder."
        ],
        "formula": {
            "title": "PERSAMAAN TRANSFORMATOR IDEAL",
            "latex": "\\frac{V_s}{V_p} = \\frac{N_s}{N_p} = \\frac{I_p}{I_s} \\implies N_s = N_p \\frac{V_s}{V_p}; \\quad I_p = I_s \\frac{V_s}{V_p}",
            "legend": "• $N_s = 1.000 \\times \\frac{22}{220} = 1.000 \\times 0{,}1 = 100\\text{ lilitan}$<br>• $I_p = 5 \\times \\frac{22}{220} = 5 \\times 0{,}1 = 0{,}5\\text{ A}$"
        },
        "hints": {
            "concept": "Trafo ideal: Ns / Np = Vs / Vp dan Ip / Is = Vs / Vp.",
            "execution": "Ns = 1000 * (22 / 220) = 100 lilitan. Ip = 5 * (22 / 220) = 0,5 Ampere."
        }
    },
    {
        "id": "fis-lat-e-17",
        "materi": "OPTIKA GEOMETRI",
        "topic": "Pembentukan Bayangan pada Cermin Cekung",
        "stem": "Sebuah benda diletakkan pada jarak $s = 15\\text{ cm}$ di depan cermin cekung yang memiliki jari-jari kelengkungan $R = 20\\text{ cm}$. Jarak bayangan ($s'$) yang terbentuk dan sifat bayangan tersebut adalah...",
        "correct": "Jarak bayangan $s' = 30\\text{ cm}$ di depan cermin dengan sifat nyata, terbalik, dan diperbesar 2 kali ($M = 2$), dihitung dari titik fokus $f = \\frac{R}{2} = 10\\text{ cm}$ dan rumus $\\frac{1}{s'} = \\frac{1}{10} - \\frac{1}{15} = \\frac{1}{30}$.",
        "distractors": [
            "Jarak bayangan $s' = 10\\text{ cm}$ di belakang cermin dengan sifat maya, tegak, dan sama besar.",
            "Jarak bayangan $s' = 60\\text{ cm}$ di depan cermin dengan sifat maya, terbalik, dan diperkecil.",
            "Jarak bayangan $s' = 15\\text{ cm}$ di depan cermin dengan sifat nyata, tegak, dan diperbesar tak hingga.",
            "Jarak bayangan $s' = 7{,}5\\text{ cm}$ di belakang cermin dengan sifat nyata, tegak, dan diperkecil separuhnya."
        ],
        "formula": {
            "title": "PERSAMAAN CERMIN CEKUNG",
            "latex": "f = \\frac{R}{2} = 10\\text{ cm}; \\quad \\frac{1}{f} = \\frac{1}{s} + \\frac{1}{s'} \\implies \\frac{1}{s'} = \\frac{1}{10} - \\frac{1}{15} = \\frac{3 - 2}{30} = \\frac{1}{30} \\implies s' = +30\\text{ cm}",
            "legend": "• Perbesaran: $M = \\left|\\frac{s'}{s}\\right| = \\frac{30}{15} = 2\\text{ kali}$<br>• $s' > 0 \\implies$ Bayangan Nyata di depan cermin (selalu terbalik)"
        },
        "hints": {
            "concept": "Titik fokus cermin cekung f = R / 2 = 10 cm. Gunakan rumus 1/f = 1/s + 1/s'.",
            "execution": "1/s' = 1/10 - 1/15 = 1/30 -> s' = +30 cm (nyata, terbalik, diperbesar M = 30/15 = 2x)."
        }
    },
    {
        "id": "fis-lat-e-18",
        "materi": "OPTIKA GEOMETRI",
        "topic": "Kekuatan Lensa Kacamata Miopi (Rabun Jauh)",
        "stem": "Seseorang menderita rabun jauh (miopi) sehingga titik jauhnya (Punctum Remotum / PR) berada pada jarak $2\\text{ meter}$ di depan matanya. Agar orang tersebut dapat melihat benda-benda yang sangat jauh ($s = \\infty$) dengan jelas tanpa berakomodasi, daya/kekuatan lensa kacamata ($P$) yang harus digunakan adalah...",
        "correct": "$-0{,}5\\text{ Dioptri}$, karena kacamata berlensa cekung (divergen/negatif) harus membentuk bayangan maya benda tak terhingga di titik jauh matanya ($s' = -2\\text{ m}$), sehingga $P = -\\frac{1}{\\text{PR(m)}} = -\\frac{1}{2} = -0{,}5\\text{ D}$.",
        "distractors": [
            "$+0{,}5\\text{ Dioptri}$, karena penderita rabun jauh keliru diberi kacamata berlensa cembung positif pengumpul cahaya.",
            "$-2{,}0\\text{ Dioptri}$, dihitung dengan menyamakan daya lensa langsung dengan jarak titik jauh mata dalam meter.",
            "$+2{,}0\\text{ Dioptri}$, karena daya lensa dihitung dari kebalikan jarak baca normal orang dewasa.",
            "$-5{,}0\\text{ Dioptri}$, dihitung dari perkalian titik jauh mata dengan ketebalan kornea mata."
        ],
        "formula": {
            "title": "DAYA LENSA KACAMATA MIOPI",
            "latex": "P = -\\frac{1}{\\text{PR(meter)}} = -\\frac{100}{\\text{PR(cm)}} = -\\frac{1}{2\\text{ m}} = -0{,}5\\text{ Dioptri (D)}",
            "legend": "• Lensa Cekung (Negatif) membiaskan berkas sejajar agar seolah-olah berasal dari Punctum Remotum (PR)<br>• $s = \\infty \\implies \\frac{1}{f} = \\frac{1}{\\infty} + \\frac{1}{-2} = -0{,}5 \\implies P = -0{,}5\\text{ D}$"
        },
        "hints": {
            "concept": "Rumus daya lensa untuk miopi: P = -1 / PR (dalam meter) atau P = -100 / PR (dalam cm).",
            "execution": "P = -1 / 2 = -0,5 Dioptri."
        }
    },
    {
        "id": "fis-lat-e-19",
        "materi": "TEORI KINETIK GAS",
        "topic": "Energi Kinetik Rata-Rata Gas Monoatomik",
        "stem": "Suatu gas ideal monoatomik (seperti gas Helium) berada di dalam wadah tertutup pada suhu mutlak $T = 300\\text{ Kelvin}$. Jika konstanta Boltzmann adalah $k = 1{,}38 \\times 10^{-23}\\text{ J/K}$, besar energi kinetik translasi rata-rata per molekul gas tersebut adalah...",
        "correct": "$6{,}21 \\times 10^{-21}\\text{ Joule}$, dihitung dari persamaan energi kinetik gas monoatomik yang memiliki 3 derajat kebebasan: $\\bar{E}_k = \\frac{3}{2}kT = \\frac{3}{2}(1{,}38 \\times 10^{-23})(300)$.",
        "distractors": [
            "$4{,}14 \\times 10^{-21}\\text{ Joule}$, dihitung dari persamaan gas dengan 2 derajat kebebasan tanpa memperhitungkan gerak translasi tiga dimensi.",
            "$1{,}035 \\times 10^{-20}\\text{ Joule}$, dihitung dengan menganggap gas monoatomik memiliki derajat kebebasan vibrasi seperti gas poliatomik.",
            "$2{,}07 \\times 10^{-21}\\text{ Joule}$, dihitung dengan mengabaikan faktor pengali tiga per dua dari teorema ekuipartisi energi.",
            "$9{,}32 \\times 10^{-21}\\text{ Joule}$, dihitung dari perkalian konstanta gas universal dengan suhu Celcius."
        ],
        "formula": {
            "title": "TEOREMA EKUIPARTISI ENERGI KINETIK GAS",
            "latex": "\\bar{E}_k = \\frac{f}{2} k T = \\frac{3}{2} k T = 1{,}5 \\times (1{,}38 \\times 10^{-23}) \\times 300 = 6{,}21 \\times 10^{-21}\\text{ J}",
            "legend": "• Gas Monoatomik: Derajat kebebasan $f = 3$ (gerak translasi sumbu x, y, z)<br>• $\\bar{E}_k$ semata-mata merupakan fungsi dari suhu mutlak $T$ (tidak dipengaruhi jenis atau massa molekul gas)"
        },
        "hints": {
            "concept": "Energi kinetik gas monoatomik: Ek = 3/2 * k * T.",
            "execution": "Ek = 1,5 * (1,38e-23) * 300 = 6,21 * 10^-21 Joule."
        }
    },
    {
        "id": "fis-lat-e-20",
        "materi": "TERMODINAMIKA (MESIN KALOR)",
        "topic": "Efisiensi Mesin Kalor Siklus Carnot",
        "stem": "Sebuah mesin kalor Carnot bekerja di antara dua reservoir bersuhu tinggi $T_H = 500\\text{ Kelvin}$ dan reservoir bersuhu rendah $T_C = 350\\text{ Kelvin}$. Jika mesin menyerap kalor dari reservoir panas sebesar $Q_H = 10.000\\text{ Joule}$ dalam satu siklus, usaha mekanik ($W$) yang dihasilkan oleh mesin Carnot tersebut adalah...",
        "correct": "$3.000\\text{ Joule}$, karena efisiensi mesin Carnot adalah $\\eta = 1 - \\frac{T_C}{T_H} = 1 - \\frac{350}{500} = 0{,}30$ (30%), sehingga usaha yang dihasilkan $W = \\eta \\cdot Q_H = 0{,}30 \\times 10.000\\text{ J} = 3.000\\text{ J}$.",
        "distractors": [
            "$7.000\\text{ Joule}$, karena nilai tersebut merupakan kalor sisa ($Q_C$) yang dibuang ke reservoir dingin, bukan usaha yang dihasilkan.",
            "$5.000\\text{ Joule}$, dengan asumsi mesin Carnot memiliki efisiensi maksimal 50% pada seluruh rentang temperatur.",
            "$1.500\\text{ Joule}$, dihitung dari perbandingan selisih suhu reservoir terhadap suhu titik beku air murni.",
            "$10.000\\text{ Joule}$, karena mesin ideal diasumsikan mampu mengubah seluruh kalor serap menjadi usaha mekanik tanpa rugi."
        ],
        "formula": {
            "title": "EFISIENSI MESIN SIKLUS CARNOT",
            "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H} \\implies W = Q_H \\left(1 - \\frac{T_C}{T_H}\\right) = 10.000 \\times \\left(1 - \\frac{350}{500}\\right) = 3.000\\text{ J}",
            "legend": "• $\\eta = 1 - 0{,}70 = 0{,}30$ (30%)<br>• $W = 0{,}30 \\times 10.000 = 3.000\\text{ J}$<br>• Kalor Buang: $Q_C = Q_H - W = 7.000\\text{ J}$"
        },
        "hints": {
            "concept": "Efisiensi Carnot: eta = 1 - (Tc / Th). Usaha: W = eta * Qh.",
            "execution": "eta = 1 - (350 / 500) = 0,30. W = 0,30 * 10000 = 3000 Joule."
        }
    },
    {
        "id": "fis-lat-e-21",
        "materi": "GELOMBANG ELEKTROMAGNETIK",
        "topic": "Spektrum Gelombang Elektromagnetik",
        "stem": "Urutan spektrum gelombang elektromagnetik dari frekuensi paling rendah ke frekuensi paling tinggi (panjang gelombang paling besar ke paling kecil) yang tepat adalah...",
        "correct": "Gelombang Radio $\\rightarrow$ Gelombang Mikro (Radar) $\\rightarrow$ Inframerah $\\rightarrow$ Cahaya Tampak $\\rightarrow$ Ultraviolet $\\rightarrow$ Sinar-X $\\rightarrow$ Sinar Gamma.",
        "distractors": [
            "Sinar Gamma $\\rightarrow$ Sinar-X $\\rightarrow$ Ultraviolet $\\rightarrow$ Cahaya Tampak $\\rightarrow$ Inframerah $\\rightarrow$ Gelombang Mikro $\\rightarrow$ Gelombang Radio.",
            "Gelombang Radio $\\rightarrow$ Cahaya Tampak $\\rightarrow$ Gelombang Mikro $\\rightarrow$ Sinar-X $\\rightarrow$ Inframerah $\\rightarrow$ Sinar Gamma $\\rightarrow$ Ultraviolet.",
            "Cahaya Tampak $\\rightarrow$ Inframerah $\\rightarrow$ Ultraviolet $\\rightarrow$ Gelombang Radio $\\rightarrow$ Sinar Gamma $\\rightarrow$ Sinar-X $\\rightarrow$ Radar.",
            "Ultraviolet $\\rightarrow$ Sinar-X $\\rightarrow$ Sinar Gamma $\\rightarrow$ Gelombang Radio $\\rightarrow$ Gelombang Mikro $\\rightarrow$ Inframerah $\\rightarrow$ Cahaya Tampak."
        ],
        "formula": {
            "title": "SPEKTRUM GELOMBANG ELEKTROMAGNETIK",
            "latex": "c = \\lambda \\cdot f \\implies f \\uparrow \\iff \\lambda \\downarrow \\iff E = hf \\uparrow",
            "legend": "• Frekuensi Terendah (Panjang Gelombang Terbesar): Radio ($f \\sim 10^4 - 10^8\\text{ Hz}$)<br>• Frekuensi Tertinggi (Energi Foton Terbesar): Sinar Gamma ($f > 10^{20}\\text{ Hz}$)"
        },
        "hints": {
            "concept": "Urutan frekuensi rendah ke tinggi: Radio, Mikro, Inframerah, Tampak (Me-Ji-Ku-Hi-Bi-Ni-U), Ultraviolet, Sinar-X, Sinar Gamma.",
            "execution": "Radio -> Mikro -> Inframerah -> Tampak -> UV -> Sinar-X -> Gamma."
        }
    },
    {
        "id": "fis-lat-e-22",
        "materi": "FISIKA MODERN (RELATIVITAS KHUSUS)",
        "topic": "Dilatasi Waktu Relativistik",
        "stem": "Dua orang astronot kembar A dan B berusia 25 tahun. Astronot B melakukan perjalanan antariksa dengan pesawat roket berkecepatan $v = 0{,}8c$ (di mana $c$ adalah kecepatan cahaya) menuju bintang Alpha Centauri. Menurut jam di dalam pesawat astronot B, perjalanan berlangsung selama $\\Delta t_0 = 6\\text{ tahun}$. Waktu perjalanan tersebut menurut pengamat A yang diam di bumi adalah...",
        "correct": "$10\\text{ tahun}$, karena efek dilatasi waktu Einstein menetapkan bahwa waktu pengamat diam memanjang menurut faktor Lorentz $\\gamma = \\frac{1}{\\sqrt{1 - (0{,}8)^2}} = \\frac{1}{0{,}6} = \\frac{5}{3}$, sehingga $\\Delta t = \\gamma \\cdot \\Delta t_0 = \\frac{5}{3} \\times 6 = 10\\text{ tahun}$.",
        "distractors": [
            "$4{,}8\\text{ tahun}$, dihitung dengan mengalikan waktu tepat dengan faktor 0,8 tanpa menerapkan rumus dilatasi waktu pembagi.",
            "$3{,}6\\text{ tahun}$, dihitung dari perkalian waktu diam dengan kuadrat faktor kontraksi panjang.",
            "$6\\text{ tahun}$, karena hukum fisika klasik Newton menganggap waktu bersifat mutlak di seluruh penjuru alam semesta.",
            "$15\\text{ tahun}$, dihitung dari perkalian waktu penjelajah dengan konstanta kecepatan cahaya kuadrat."
        ],
        "formula": {
            "title": "DILATASI WAKTU RELATIVISTIK",
            "latex": "\\Delta t = \\frac{\\Delta t_0}{\\sqrt{1 - \\frac{v^2}{c^2}}} = \\frac{6}{\\sqrt{1 - (0{,}8)^2}} = \\frac{6}{\\sqrt{1 - 0{,}64}} = \\frac{6}{0{,}6} = 10\\text{ tahun}",
            "legend": "• $\\Delta t_0 = 6\\text{ tahun}$ (Waktu tepat / Proper time diukur oleh astronot B)<br>• $\\Delta t = 10\\text{ tahun}$ (Waktu dilatasi diukur oleh pengamat diam di bumi)<br>• Jam yang bergerak berdetak lebih lambat daripada jam pengamat diam"
        },
        "hints": {
            "concept": "Dilatasi waktu: delta_t = delta_t0 / sqrt(1 - v^2/c^2).",
            "execution": "sqrt(1 - 0,8^2) = 0,6. delta_t = 6 / 0,6 = 10 tahun."
        }
    },
    {
        "id": "fis-lat-e-23",
        "materi": "FISIKA MODERN (RELATIVITAS KHUSUS)",
        "topic": "Kontraksi Panjang Relativistik",
        "stem": "Sebuah pesawat antariksa memiliki panjang $L_0 = 100\\text{ meter}$ saat diukur diam di landasan peluncuran bumi. Pesawat tersebut kemudian terbang melintasi bumi dengan kecepatan tetap $v = 0{,}6c$. Panjang pesawat saat melintas menurut pengamat stasioner di bumi adalah...",
        "correct": "$80\\text{ meter}$, karena pengamat yang diam mengamati terjadinya pengerutan/kontraksi panjang searah gerak benda: $L = L_0 \\sqrt{1 - \\frac{v^2}{c^2}} = 100 \\times \\sqrt{1 - (0{,}6)^2} = 100 \\times 0{,}8 = 80\\text{ meter}$.",
        "distractors": [
            "$125\\text{ meter}$, karena panjang pesawat keliru dihitung memanjang dengan membagi panjang diam terhadap faktor Lorentz.",
            "$60\\text{ meter}$, dihitung dengan mengalikan panjang diam secara langsung dengan koefisien kecepatan 0,6.",
            "$100\\text{ meter}$, karena panjang benda fisik dianggap kekal dan tidak dapat dipengaruhi oleh kelajuan gerak roket.",
            "$40\\text{ meter}$, dihitung dari selisih kuadrat panjang diam dengan konstanta kelajuan cahaya."
        ],
        "formula": {
            "title": "KONTRAKSI PANJANG RELATIVISTIK (LORENTZ)",
            "latex": "L = L_0 \\sqrt{1 - \\frac{v^2}{c^2}} = 100 \\times \\sqrt{1 - 0{,}36} = 100 \\times \\sqrt{0{,}64} = 100 \\times 0{,}8 = 80\\text{ meter}",
            "legend": "• $L_0 = 100\\text{ m}$ (Panjang sejati / Proper length)<br>• $L = 80\\text{ m}$ (Panjang teramati menyusut hanya pada dimensi yang sejajar arah gerak)"
        },
        "hints": {
            "concept": "Kontraksi panjang Lorentz: L = L0 * sqrt(1 - v^2/c^2).",
            "execution": "L = 100 * sqrt(1 - 0,36) = 100 * 0,8 = 80 meter."
        }
    },
    {
        "id": "fis-lat-e-24",
        "materi": "FISIKA KUANTUM & ATOM",
        "topic": "Panjang Gelombang de Broglie",
        "stem": "Sebuah elektron bermassa $m = 9 \\times 10^{-31}\\text{ kg}$ bergerak dengan kecepatan konstan $v = 2 \\times 10^6\\text{ m/s}$. Jika konstanta Planck adalah $h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$, panjang gelombang de Broglie dari elektron tersebut adalah...",
        "correct": "$3{,}68 \\times 10^{-10}\\text{ meter}$ (atau $0{,}368\\text{ nm}$), dihitung dari hipotesis dualisme partikel-gelombang de Broglie: $\\lambda = \\frac{h}{p} = \\frac{h}{m \\cdot v} = \\frac{6{,}63 \\times 10^{-34}}{(9 \\times 10^{-31})(2 \\times 10^6)}$.",
        "distractors": [
            "$3{,}68 \\times 10^{-7}\\text{ meter}$, karena eksponen kecepatan elektron keliru dimasukkan bertanda negatif dalam perhitungan.",
            "$1{,}84 \\times 10^{-10}\\text{ meter}$, dihitung dengan mengabaikan konstanta massa elektron pada penyebut momentum linier.",
            "$7{,}36 \\times 10^{-10}\\text{ meter}$, dihitung dari perkalian momentum elektron dengan konstanta Planck secara langsung.",
            "$5{,}50 \\times 10^{-12}\\text{ meter}$, dihitung dari asumsi panjang gelombang foton sinar gamma frekuensi tinggi."
        ],
        "formula": {
            "title": "HIPOTESIS DE BROGLIE DUALISME GELOMBANG PARTIKEL",
            "latex": "\\lambda = \\frac{h}{p} = \\frac{h}{m \\cdot v} = \\frac{6{,}63 \\times 10^{-34}}{(9 \\times 10^{-31})(2 \\times 10^6)} = \\frac{6{,}63 \\times 10^{-34}}{18 \\times 10^{-25}} \\approx 3{,}68 \\times 10^{-10}\\text{ m}",
            "legend": "• $h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$<br>• Momentum $p = m \\cdot v = 1{,}8 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}$<br>• Panjang gelombang ini berada pada skala ukuran kisi kristal padatan (memungkinkan terjadinya difraksi elektron)"
        },
        "hints": {
            "concept": "Panjang gelombang de Broglie: lambda = h / (m * v).",
            "execution": "p = 9e-31 * 2e6 = 1,8e-24 kg*m/s. lambda = 6,63e-34 / 1,8e-24 = 3,68 * 10^-10 meter."
        }
    },
    {
        "id": "fis-lat-e-25",
        "materi": "FISIKA INTI & RADIOAKTIVITAS",
        "topic": "Waktu Paruh dan Peluruhan Radioaktif",
        "stem": "Suatu sampel zat radioaktif mula-mula memiliki massa $N_0 = 64\\text{ gram}$. Zat tersebut memiliki waktu paruh (half-life) $T_{1/2} = 4\\text{ jam}$. Massa sampel zat radioaktif yang belum meluruh setelah disimpan selama $t = 16\\text{ jam}$ adalah...",
        "correct": "$4\\text{ gram}$, karena selama 16 jam zat telah mengalami $n = \\frac{t}{T_{1/2}} = \\frac{16}{4} = 4$ kali periode peluruhan, sehingga massa yang tersisa adalah $N_t = N_0 \\left(\\frac{1}{2}\\right)^4 = 64 \\times \\frac{1}{16} = 4\\text{ gram}$.",
        "distractors": [
            "$8\\text{ gram}$, dihitung dengan menganggap sampel hanya meluruh sebanyak 3 kali periode waktu paruh.",
            "$16\\text{ gram}$, dihitung dengan membagi massa awal secara langsung dengan durasi waktu penyimpanan 16 jam.",
            "$2\\text{ gram}$, dihitung dari asumsi bahwa zat telah meluruh sebanyak 5 kali periode paruh.",
            "$0\\text{ gram}$, karena zat radioaktif dianggap habis musnah total setelah melewati waktu 12 jam."
        ],
        "formula": {
            "title": "HUKUM PELURUHAN RADIOAKTIF",
            "latex": "N_t = N_0 \\left(\\frac{1}{2}\\right)^n; \\quad n = \\frac{t}{T_{1/2}} = \\frac{16\\text{ jam}}{4\\text{ jam}} = 4 \\implies N_t = 64 \\times \\left(\\frac{1}{2}\\right)^4 = 64 \\times \\frac{1}{16} = 4\\text{ gram}",
            "legend": "• $N_0 = 64\\text{ g}$ (Massa awal)<br>• $N_t = 4\\text{ g}$ (Massa zat sisa yang belum meluruh)<br>• Massa zat yang telah meluruh: $64 - 4 = 60\\text{ gram}$"
        },
        "hints": {
            "concept": "Jumlah paruh n = t / T_half = 16 / 4 = 4. Nt = N0 * (1/2)^n.",
            "execution": "n = 4. Nt = 64 * (1/16) = 4 gram."
        }
    }
]
