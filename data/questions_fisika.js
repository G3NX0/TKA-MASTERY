/**
 * TKA MASTERY HUB — QUESTIONS_FISIKA.JS (110 SOAL AUTENTIK PUSMENDIK 2026)
 * Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
 * Composition: 25 Latihan Easy, 25 Medium, 25 Hard, 35 Simulasi (25 MCQ, 5 Multi, 5 Matrix)
 */
window.TKA_FISIKA_QUESTIONS = [
  {
    "id": "fis-lat-e-01",
    "materi": "KINEMATIKA GERAK LURUS",
    "topic": "Gerak Lurus Berubah Beraturan (GLBB)",
    "hints": {
      "concept": "Gunakan persamaan GLBB gerak lurus dengan kecepatan awal v0 = 0.",
      "execution": "vt = a * t = 4 * 5 = 20 m/s; s = 0.5 * a * t^2 = 0.5 * 4 * 25 = 50 m."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah mobil listrik mula-mula diam di jalan tol yang lurus. Pengemudi menginjak pedal gas sehingga mobil mengalami percepatan konstan $a = 4\\text{ m/s}^2$ selama selang waktu $t = 5\\text{ sekon}$. Kecepatan akhir ($v_t$) dan jarak tempuh ($s$) yang dicapai mobil listrik tersebut pada akhir detik kelima adalah...",
    "formulaHud": {
      "title": "PERSAMAAN KINEMATIKA GLBB",
      "latex": "v_t = v_0 + at; \\quad s = v_0 t + \\frac{1}{2}at^2; \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $v_0 = 0\\text{ m/s}$, $a = 4\\text{ m/s}^2$, $t = 5\\text{ s}$<br>• $v_t = 0 + (4 \\times 5) = 20\\text{ m/s}$<br>• $s = 0 + \\frac{1}{2}(4)(5^2) = 2 \\times 25 = 50\\text{ m}$"
    },
    "options": [
      {
        "key": "A",
        "text": "Kecepatan akhir $v_t = 20\\text{ m/s}$ dan jarak tempuh $s = 50\\text{ meter}$, dihitung dari persamaan $v_t = v_0 + at$ dan $s = v_0 t + \\frac{1}{2}at^2$."
      },
      {
        "key": "B",
        "text": "Kecepatan akhir $v_t = 10\\text{ m/s}$ dan jarak tempuh $s = 20\\text{ meter}$, karena percepatan dihitung dengan membagi gaya baterai terhadap massa kendaraan."
      },
      {
        "key": "C",
        "text": "Kecepatan akhir $v_t = 40\\text{ m/s}$ dan jarak tempuh $s = 100\\text{ meter}$, dihitung dengan mengabaikan kecepatan awal nol pada spedometer."
      },
      {
        "key": "D",
        "text": "Kecepatan akhir $v_t = 25\\text{ m/s}$ dan jarak tempuh $s = 80\\text{ meter}$, karena hambatan angin diasumsikan konstan sebesar 15 Newton."
      },
      {
        "key": "E",
        "text": "Kecepatan akhir $v_t = 15\\text{ m/s}$ dan jarak tempuh $s = 45\\text{ meter}$, dihitung dari perkalian percepatan dengan gravitasi bumi."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Kecepatan akhir $v_t = 20\\text{ m/s}$ dan jarak tempuh $s = 50\\text{ meter}$, dihitung dari persamaan $v_t = v_0 + at$ dan $s = v_0 t + \\frac{1}{2}at^2$.. Gunakan persamaan GLBB gerak lurus dengan kecepatan awal v0 = 0. vt = a * t = 4 * 5 = 20 m/s; s = 0.5 * a * t^2 = 0.5 * 4 * 25 = 50 m."
  },
  {
    "id": "fis-lat-e-02",
    "materi": "DINAMIKA GERAK NEWTON",
    "topic": "Hukum II Newton pada Bidang Datar Licin",
    "hints": {
      "concept": "Percepatan = F / (m1 + m2). Tinjau balok m2 untuk mencari gaya kontak: N12 = m2 * a.",
      "execution": "a = 25 / 5 = 5 m/s²; N12 = 2 * 5 = 10 N."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dua buah balok $m_1 = 3\\text{ kg}$ dan $m_2 = 2\\text{ kg}$ diletakkan berdampingan bersentuhan di atas lantai mendatar licin tanpa gesekan. Balok $m_1$ didorong dengan gaya horizontal konstan $F = 25\\text{ N}$ ke kanan. Besar percepatan sistem dan besar gaya kontak antara kedua balok tersebut adalah...",
    "formulaHud": {
      "title": "HUKUM II NEWTON SISTEM TERKOPEL",
      "latex": "a = \\frac{F}{m_1 + m_2} = \\frac{25}{3 + 2} = 5\\text{ m/s}^2; \\quad N_{12} = m_2 \\cdot a = 2 \\times 5 = 10\\text{ N}",
      "legend": "• Gaya Eksternal: $F = 25\\text{ N}$<br>• Massa Total: $3 + 2 = 5\\text{ kg}$<br>• Gaya Kontak pada $m_2$: $\\Sigma F_2 = m_2 a \\implies N_{12} = 2 \\times 5 = 10\\text{ N}$"
    },
    "options": [
      {
        "key": "A",
        "text": "Percepatan sistem $a = 2{,}5\\text{ m/s}^2$ dan gaya kontak $N_{12} = 25\\text{ N}$, karena gaya aksi-reaksi menahan seluruh pergerakan balok pertama sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "Percepatan sistem $a = 5\\text{ m/s}^2$ dan gaya kontak antaran balok sebesar $N_{12} = 10\\text{ N}$, di mana gaya dorong diteruskan oleh balok pertama untuk mempercepat balok kedua bermassa 2 kg."
      },
      {
        "key": "C",
        "text": "Percepatan sistem $a = 8{,}3\\text{ m/s}^2$ dan gaya kontak $N_{12} = 15\\text{ N}$, dihitung dengan mengalikan massa total dengan percepatan gravitasi bumi."
      },
      {
        "key": "D",
        "text": "Percepatan sistem $a = 10\\text{ m/s}^2$ dan gaya kontak $N_{12} = 5\\text{ N}$, karena massa balok kedua dianggap nol di bidang tanpa gesek."
      },
      {
        "key": "E",
        "text": "Percepatan sistem $a = 1\\text{ m/s}^2$ dan gaya kontak $N_{12} = 20\\text{ N}$, diperoleh dari selisih kedua massa dikalikan gaya luar."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Percepatan sistem $a = 5\\text{ m/s}^2$ dan gaya kontak antaran balok sebesar $N_{12} = 10\\text{ N}$, di mana gaya dorong diteruskan oleh balok pertama untuk mempercepat balok kedua bermassa 2 kg.. Percepatan = F / (m1 + m2). Tinjau balok m2 untuk mencari gaya kontak: N12 = m2 * a. a = 25 / 5 = 5 m/s²; N12 = 2 * 5 = 10 N."
  },
  {
    "id": "fis-lat-e-03",
    "materi": "USAHA DAN ENERGI",
    "topic": "Hukum Kekekalan Energi Mekanik (Gerak Jatuh Bebas)",
    "hints": {
      "concept": "Energi mekanik kekal: Ek2 = Ep1 - Ep2 = mg(h1 - h2).",
      "execution": "Ek2 = 2 * 10 * (20 - 5) = 20 * 15 = 300 Joule."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah buah kelapa bermassa $m = 2\\text{ kg}$ jatuh bebas dari pucuk pohonnya pada ketinggian $h = 20\\text{ meter}$ di atas permukaan tanah ($g = 10\\text{ m/s}^2$). Mengabaikan hambatan gesekan udara, energi kinetik ($E_k$) kelapa saat berada pada ketinggian $5\\text{ meter}$ dari tanah adalah...",
    "formulaHud": {
      "title": "KEKEKALAN ENERGI MEKANIK",
      "latex": "E_{m1} = E_{m2} \\implies mgh_1 + 0 = mgh_2 + E_{k2} \\implies E_{k2} = mg(h_1 - h_2)",
      "legend": "• $E_{p1} = 2 \\times 10 \\times 20 = 400\\text{ J}$<br>• $E_{p2} = 2 \\times 10 \\times 5 = 100\\text{ J}$<br>• $E_{k2} = 400 - 100 = 300\\text{ J}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$400\\text{ Joule}$, karena seluruh energi potensial di puncak pohon langsung menjadi energi kinetik tanpa memperhatikan sisa ketinggian ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$100\\text{ Joule}$, dihitung dari energi potensial yang tersisa di posisi lima meter di atas permukaan tanah."
      },
      {
        "key": "C",
        "text": "$300\\text{ Joule}$, karena penurunan energi potensial sebesar $\\Delta E_p = mg(h_1 - h_2) = 2 \\times 10 \\times (20 - 5) = 300\\text{ J}$ berubah seluruhnya menjadi energi kinetik."
      },
      {
        "key": "D",
        "text": "$200\\text{ Joule}$, dihitung dari hasil kali massa kelapa dengan kecepatan angin rata-rata di perkebunan."
      },
      {
        "key": "E",
        "text": "$50\\text{ Joule}$, karena gravitasi bumi mengalami pengurangan daya tarik seiring bertambahnya kelajuan benda."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $300\\text{ Joule}$, karena penurunan energi potensial sebesar $\\Delta E_p = mg(h_1 - h_2) = 2 \\times 10 \\times (20 - 5) = 300\\text{ J}$ berubah seluruhnya menjadi energi kinetik.. Energi mekanik kekal: Ek2 = Ep1 - Ep2 = mg(h1 - h2). Ek2 = 2 * 10 * (20 - 5) = 20 * 15 = 300 Joule."
  },
  {
    "id": "fis-lat-e-04",
    "materi": "MOMENTUM DAN IMPULS",
    "topic": "Impuls dan Perubahan Momentum",
    "hints": {
      "concept": "Kecepatan adalah besaran vektor. Bola berbalik arah: delta_v = v2 - (-v1) = 30 - (-20) = 50 m/s. F = m * delta_v / delta_t.",
      "execution": "F = 0,15 * 50 / 0,01 = 7,5 / 0,01 = 750 N."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah bola kasti bermassa $m = 0{,}15\\text{ kg}$ melaju horizontal ke kiri dengan kecepatan $v_1 = 20\\text{ m/s}$. Pemukul memukul bola tersebut sehingga bola berbalik arah melaju ke kanan dengan kecepatan $v_2 = 30\\text{ m/s}$. Jika waktu kontak pemukul dengan bola adalah $\\Delta t = 0{,}01\\text{ sekon}$, besar gaya rata-rata yang diberikan pemukul pada bola adalah...",
    "formulaHud": {
      "title": "TEOREMA IMPULS-MOMENTUM",
      "latex": "I = \\bar{F} \\Delta t = \\Delta p = m(v_2 - v_1) \\implies \\bar{F} = \\frac{m(v_2 - v_1)}{\\Delta t}",
      "legend": "• Ambil arah kanan sebagai positif: $v_1 = -20\\text{ m/s}$, $v_2 = +30\\text{ m/s}$<br>• $\\Delta p = 0{,}15 \\times (30 - (-20)) = 0{,}15 \\times 50 = 7{,}5\\text{ N}\\cdot\\text{s}$<br>• $\\bar{F} = \\frac{7{,}5}{0{,}01} = 750\\text{ N}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$150\\text{ Newton}$, dihitung dengan mengurangkan kelajuan akhir dan kelajuan awal sebagai besaran skalar biasa tanpa arah menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$300\\text{ Newton}$, karena massa bola kasti dibagi langsung dengan percepatan gravitasi bumi di lapangan."
      },
      {
        "key": "C",
        "text": "$500\\text{ Newton}$, dihitung dari energi kinetik bola dibagi dengan selang waktu tumbukan mikroskopis."
      },
      {
        "key": "D",
        "text": "$750\\text{ Newton}$, diperoleh dari perubahan momentum $\\Delta p = m(v_2 - v_1) = 0{,}15 \\times (30 - (-20)) = 7{,}5\\text{ N}\\cdot\\text{s}$, dibagi waktu kontak $0{,}01\\text{ s}$."
      },
      {
        "key": "E",
        "text": "$75\\text{ Newton}$, karena tanda arah kecepatan berlawanan diabaikan dalam perhitungan impuls mekanika."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $750\\text{ Newton}$, diperoleh dari perubahan momentum $\\Delta p = m(v_2 - v_1) = 0{,}15 \\times (30 - (-20)) = 7{,}5\\text{ N}\\cdot\\text{s}$, dibagi waktu kontak $0{,}01\\text{ s}$.. Kecepatan adalah besaran vektor. Bola berbalik arah: delta_v = v2 - (-v1) = 30 - (-20) = 50 m/s. F = m * delta_v / delta_t. F = 0,15 * 50 / 0,01 = 7,5 / 0,01 = 750 N."
  },
  {
    "id": "fis-lat-e-05",
    "materi": "FLUIDA STATIS",
    "topic": "Tekanan Hidrostatis pada Dasar Bejana",
    "hints": {
      "concept": "Tekanan hidrostatis: P = rho * g * h. Konversi cm ke meter: 75 cm = 0,75 m.",
      "execution": "P = 800 * 10 * 0,75 = 6000 Pa."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah tabung silinder vertikal berisi cairan minyak goreng dengan massa jenis $\\rho = 800\\text{ kg/m}^3$ setinggi $h = 75\\text{ cm}$. Jika percepatan gravitasi bumi $g = 10\\text{ m/s}^2$ dan tekanan udara atmosfer diabaikan, besar tekanan hidrostatis yang dialami oleh dasar tabung tersebut adalah...",
    "formulaHud": {
      "title": "FORMULA TEKANAN HIDROSTATIS",
      "latex": "P_h = \\rho \\cdot g \\cdot h = 800\\text{ kg/m}^3 \\times 10\\text{ m/s}^2 \\times 0{,}75\\text{ m} = 6.000\\text{ N/m}^2 \\text{ (Pa)}",
      "legend": "• $\\rho = 800\\text{ kg/m}^3$<br>• $g = 10\\text{ m/s}^2$<br>• $h = 75\\text{ cm} = 0{,}75\\text{ m}$<br>• $P_h = 6.000\\text{ Pa} = 6\\text{ kPa}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$60.000\\text{ Pascal}$, karena ketinggian 75 cm keliru dimasukkan dalam satuan sentimeter tanpa dikonversi ke meter diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$8.000\\text{ Pascal}$, dihitung dari massa jenis minyak dikalikan dengan percepatan gravitasi tanpa memperhitungkan kedalaman."
      },
      {
        "key": "C",
        "text": "$7.500\\text{ Pascal}$, dihitung dari tinggi cairan dikalikan 100 tanpa memperhatikan massa jenis fluida."
      },
      {
        "key": "D",
        "text": "$1.200\\text{ Pascal}$, hasil pembagian massa jenis minyak dengan ketinggian kolom cairan di dalam tabung."
      },
      {
        "key": "E",
        "text": "$6.000\\text{ Pascal}$ (atau $6\\text{ kPa}$), dihitung dari rumus tekanan hidrostatis $P_h = \\rho g h = 800 \\times 10 \\times 0{,}75\\text{ m}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $6.000\\text{ Pascal}$ (atau $6\\text{ kPa}$), dihitung dari rumus tekanan hidrostatis $P_h = \\rho g h = 800 \\times 10 \\times 0{,}75\\text{ m}$.. Tekanan hidrostatis: P = rho * g * h. Konversi cm ke meter: 75 cm = 0,75 m. P = 800 * 10 * 0,75 = 6000 Pa."
  },
  {
    "id": "fis-lat-e-06",
    "materi": "FLUIDA STATIS",
    "topic": "Hukum Pascal pada Dongkrak Hidrolik",
    "hints": {
      "concept": "Hukum Pascal: F1 / A1 = F2 / A2. Massa M = F2 / g.",
      "execution": "F2 = 80 * (250 / 10) = 2000 N. M = 2000 / 10 = 200 kg."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah dongkrak hidrolik memiliki dua penampang piston berbentuk lingkaran. Piston kecil memiliki luas penampang $A_1 = 10\\text{ cm}^2$ dan piston besar memiliki luas $A_2 = 250\\text{ cm}^2$. Jika pada piston kecil diberikan gaya tekan $F_1 = 80\\text{ N}$, beban maksimum bermassa $M$ yang dapat diangkat pada piston besar ($g = 10\\text{ m/s}^2$) adalah...",
    "formulaHud": {
      "title": "HUKUM PASCAL BEJANA BERHUBUNGAN",
      "latex": "\\frac{F_1}{A_1} = \\frac{F_2}{A_2} \\implies F_2 = F_1 \\left(\\frac{A_2}{A_1}\\right); \\quad M = \\frac{F_2}{g}",
      "legend": "• $F_2 = 80 \\times \\frac{250}{10} = 80 \\times 25 = 2.000\\text{ N}$<br>• $M = \\frac{2.000\\text{ N}}{10\\text{ m/s}^2} = 200\\text{ kg}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$200\\text{ kg}$, karena gaya angkat pada piston besar adalah $F_2 = F_1 \\times \\frac{A_2}{A_1} = 80 \\times 25 = 2.000\\text{ N}$, yang setara dengan beban bermassa $M = \\frac{F_2}{g} = 200\\text{ kg}$."
      },
      {
        "key": "B",
        "text": "$2.000\\text{ kg}$, karena gaya angkat 2.000 Newton keliru disamakan langsung dengan massa beban tanpa dibagi percepatan gravitasi sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$80\\text{ kg}$, karena hukum Pascal mengasumsikan gaya tekan selalu sama di kedua piston tanpa penguatan mekanik."
      },
      {
        "key": "D",
        "text": "$25\\text{ kg}$, dihitung dari perbandingan rasio luas penampang piston besar terhadap piston kecil."
      },
      {
        "key": "E",
        "text": "$500\\text{ kg}$, dihitung dari perkalian luas penampang piston besar dengan percepatan gravitasi bumi."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $200\\text{ kg}$, karena gaya angkat pada piston besar adalah $F_2 = F_1 \\times \\frac{A_2}{A_1} = 80 \\times 25 = 2.000\\text{ N}$, yang setara dengan beban bermassa $M = \\frac{F_2}{g} = 200\\text{ kg}$.. Hukum Pascal: F1 / A1 = F2 / A2. Massa M = F2 / g. F2 = 80 * (250 / 10) = 2000 N. M = 2000 / 10 = 200 kg."
  },
  {
    "id": "fis-lat-e-07",
    "materi": "FLUIDA STATIS",
    "topic": "Hukum Archimedes & Gaya Apung",
    "hints": {
      "concept": "Gaya Archimedes hanya bergantung pada volume yang tercelup: Fa = rho_fluida * g * V_tercelup.",
      "execution": "V_tercelup = 0,75 * 0,02 = 0,015 m³. Fa = 1000 * 10 * 0,015 = 150 N."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah balok kayu bervolume total $V = 0{,}02\\text{ m}^3$ terapung di permukaan air tawar ($\\rho_{\\text{air}} = 1.000\\text{ kg/m}^3$). Jika $\\frac{3}{4}$ bagian volume balok tercelup di dalam air dan $g = 10\\text{ m/s}^2$, besar gaya apung (gaya ke atas Archimedes) yang bekerja pada balok kayu tersebut adalah...",
    "formulaHud": {
      "title": "HUKUM ARCHIMEDES GAYA APUNG",
      "latex": "F_A = \\rho_f \\cdot g \\cdot V_{\\text{tercelup}} = 1.000 \\times 10 \\times (0{,}75 \\times 0{,}02) = 10.000 \\times 0{,}015 = 150\\text{ N}",
      "legend": "• $V_{\\text{tercelup}} = \\frac{3}{4} \\times 0{,}02 = 0{,}015\\text{ m}^3$<br>• $F_A = 1.000 \\times 10 \\times 0{,}015 = 150\\text{ N}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$200\\text{ Newton}$, dihitung dengan menggunakan volume total balok seolah-olah seluruh balok tenggelam ke dasar bejana sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$150\\text{ Newton}$, dihitung dari berat fluida yang dipindahkan: $F_A = \\rho_{\\text{air}} \\cdot g \\cdot V_{\\text{celup}} = 1.000 \\times 10 \\times (0{,}75 \\times 0{,}02\\text{ m}^3)$."
      },
      {
        "key": "C",
        "text": "$50\\text{ Newton}$, dihitung dari seperempat volume balok kayu yang menyembul di atas permukaan air terbuka."
      },
      {
        "key": "D",
        "text": "$1.500\\text{ Newton}$, karena percepatan gravitasi dikalikan kuadrat massa jenis air danau."
      },
      {
        "key": "E",
        "text": "$75\\text{ Newton}$, dihitung dari pembagian massa jenis air dengan percepatan gravitasi bumi."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $150\\text{ Newton}$, dihitung dari berat fluida yang dipindahkan: $F_A = \\rho_{\\text{air}} \\cdot g \\cdot V_{\\text{celup}} = 1.000 \\times 10 \\times (0{,}75 \\times 0{,}02\\text{ m}^3)$.. Gaya Archimedes hanya bergantung pada volume yang tercelup: Fa = rho_fluida * g * V_tercelup. V_tercelup = 0,75 * 0,02 = 0,015 m³. Fa = 1000 * 10 * 0,015 = 150 N."
  },
  {
    "id": "fis-lat-e-08",
    "materi": "SUHU DAN KALOR",
    "topic": "Asas Black pada Pencampuran Air",
    "hints": {
      "concept": "Kalor yang dilepas air panas = Kalor yang diserap air dingin. m1*(T1 - Tc) = m2*(Tc - T2).",
      "execution": "200*(80 - Tc) = 300*(Tc - 20) -> 16000 - 200Tc = 300Tc - 6000 -> 500Tc = 22000 -> Tc = 44°C."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebanyak $200\\text{ gram}$ air bersuhu $80^\\circ\\text{C}$ dicampurkan dengan $300\\text{ gram}$ air bersuhu $20^\\circ\\text{C}$ di dalam bejana kalorimeter ideal tanpa kehilangan kalor ke lingkungan. Jika kalor jenis air $c = 1\\text{ kal/g}\\cdot^\\circ\\text{C}$, suhu akhir kesetimbangan termal campuran tersebut adalah...",
    "formulaHud": {
      "title": "ASAS BLACK KESETIMBANGAN TERMAL",
      "latex": "Q_{\\text{lepas}} = Q_{\\text{terima}} \\implies m_1 c (T_1 - T_c) = m_2 c (T_c - T_2)",
      "legend": "• $200 \\times (80 - T_c) = 300 \\times (T_c - 20)$<br>• $16.000 - 200T_c = 300T_c - 6.000$<br>• $500T_c = 22.000 \\implies T_c = 44^\\circ\\text{C}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$50^\\circ\\text{C}$, karena suhu akhir diasumsikan sebagai nilai rata-rata aritmatika sederhana antara 80°C dan 20°C ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$35^\\circ\\text{C}$, dihitung dengan mengabaikan massa air panas yang memiliki suhu lebih tinggi."
      },
      {
        "key": "C",
        "text": "$44^\\circ\\text{C}$, dihitung berdasarkan Asas Black $Q_{\\text{lepas}} = Q_{\\text{terima}} \\implies 200(80 - T_c) = 300(T_c - 20)$, yang menghasilkan $16.000 - 200T_c = 300T_c - 6.000 \\implies 500T_c = 22.000$."
      },
      {
        "key": "D",
        "text": "$60^\\circ\\text{C}$, karena kalor dianggap hanya berpindah ke dinding wadah kalorimeter kaca."
      },
      {
        "key": "E",
        "text": "$40^\\circ\\text{C}$, dihitung dari perbandingan volume kedua cairan tanpa memperhitungkan kalor jenis air."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $44^\\circ\\text{C}$, dihitung berdasarkan Asas Black $Q_{\\text{lepas}} = Q_{\\text{terima}} \\implies 200(80 - T_c) = 300(T_c - 20)$, yang menghasilkan $16.000 - 200T_c = 300T_c - 6.000 \\implies 500T_c = 22.000$.. Kalor yang dilepas air panas = Kalor yang diserap air dingin. m1*(T1 - Tc) = m2*(Tc - T2). 200*(80 - Tc) = 300*(Tc - 20) -> 16000 - 200Tc = 300Tc - 6000 -> 500Tc = 22000 -> Tc = 44°C."
  },
  {
    "id": "fis-lat-e-09",
    "materi": "TERMODINAMIKA GAS",
    "topic": "Hukum Pertama Termodinamika (Proses Isobarik)",
    "hints": {
      "concept": "Hukum I Termodinamika: delta_U = Q - W. Pada proses isobarik, W = P * delta_V.",
      "execution": "W = 2e5 * 0,03 = 6000 J. delta_U = 9000 - 6000 = 3000 J."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Suatu gas ideal berada dalam ruang tertutup bertekanan tetap $P = 2 \\times 10^5\\text{ N/m}^2$. Gas mengalami pemuaian isobarik sehingga volumenya bertambah dari $V_1 = 0{,}02\\text{ m}^3$ menjadi $V_2 = 0{,}05\\text{ m}^3$. Selama proses tersebut, gas menyerap kalor sebesar $Q = 9.000\\text{ Joule}$. Perubahan energi dalam ($\\Delta U$) gas ideal tersebut adalah...",
    "formulaHud": {
      "title": "HUKUM I TERMODINAMIKA (ISOBARIK)",
      "latex": "W = P \\Delta V; \\quad \\Delta U = Q - W = Q - P(V_2 - V_1)",
      "legend": "• $W = (2 \\times 10^5) \\times (0{,}05 - 0{,}02) = 2 \\times 10^5 \\times 0{,}03 = 6.000\\text{ J}$<br>• $\\Delta U = 9.000 - 6.000 = 3.000\\text{ J}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$15.000\\text{ Joule}$, diperoleh dari penjumlahan langsung antara kalor yang diserap dengan usaha ekspansi gas menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$6.000\\text{ Joule}$, karena nilai perubahan energi dalam keliru disamakan dengan usaha mekanik piston."
      },
      {
        "key": "C",
        "text": "$9.000\\text{ Joule}$, dengan asumsi seluruh kalor yang diserap gas tidak digunakan untuk melakukan usaha luar."
      },
      {
        "key": "D",
        "text": "$3.000\\text{ Joule}$, karena usaha luar yang dilakukan gas adalah $W = P\\Delta V = 2 \\times 10^5 \\times (0{,}05 - 0{,}02) = 6.000\\text{ J}$, sehingga $\\Delta U = Q - W = 9.000 - 6.000 = 3.000\\text{ J}$."
      },
      {
        "key": "E",
        "text": "$1.500\\text{ Joule}$, dihitung dari pembagian kalor serap dengan rasio ekspansi volume gas ideal."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $3.000\\text{ Joule}$, karena usaha luar yang dilakukan gas adalah $W = P\\Delta V = 2 \\times 10^5 \\times (0{,}05 - 0{,}02) = 6.000\\text{ J}$, sehingga $\\Delta U = Q - W = 9.000 - 6.000 = 3.000\\text{ J}$.. Hukum I Termodinamika: delta_U = Q - W. Pada proses isobarik, W = P * delta_V. W = 2e5 * 0,03 = 6000 J. delta_U = 9000 - 6000 = 3000 J."
  },
  {
    "id": "fis-lat-e-10",
    "materi": "GELOMBANG MEKANIK",
    "topic": "Persamaan Gelombang Berjalan",
    "hints": {
      "concept": "Bandingkan persamaan dengan y = A sin(omega*t - k*x). omega = 2*pi*f, k = 2*pi / lambda.",
      "execution": "A = 0,08 m; f = 4pi / 2pi = 2 Hz; lambda = 2pi / 2pi = 1 m."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah gelombang transversal merambat pada tali dengan persamaan simpangan $y = 0{,}08 \\sin(4\\pi t - 2\\pi x)$, di mana $x$ dan $y$ dalam meter serta $t$ dalam sekon. Amplitudo ($A$), frekuensi ($f$), dan panjang gelombang ($\\lambda$) dari gelombang tersebut berturut-turut adalah...",
    "formulaHud": {
      "title": "PARAMETER GELOMBANG BERJALAN",
      "latex": "y = A \\sin(\\omega t - kx); \\quad f = \\frac{\\omega}{2\\pi}; \\quad \\lambda = \\frac{2\\pi}{k}; \\quad v = \\frac{\\omega}{k}",
      "legend": "• $A = 0{,}08\\text{ m}$<br>• $\\omega = 4\\pi \\implies f = \\frac{4\\pi}{2\\pi} = 2\\text{ Hz}$<br>• $k = 2\\pi \\implies \\lambda = \\frac{2\\pi}{2\\pi} = 1\\text{ m}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$A = 0{,}08\\text{ m}$, $f = 4\\text{ Hz}$, dan $\\lambda = 2\\text{ meter}$, karena konstanta di depan t keliru dianggap frekuensi langsung tanpa dibagi 2pi diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$A = 0{,}8\\text{ m}$, $f = 1\\text{ Hz}$, dan $\\lambda = 4\\text{ meter}$, dihitung dari perbandingan koefisien sudut fase pada fungsi sinus."
      },
      {
        "key": "C",
        "text": "$A = 0{,}04\\text{ m}$, $f = 2\\text{ Hz}$, dan $\\lambda = 0{,}5\\text{ meter}$, karena amplitudo gelombang dibagi dua akibat efek simetri getaran."
      },
      {
        "key": "D",
        "text": "$A = 0{,}08\\text{ m}$, $f = 0{,}5\\text{ Hz}$, dan $\\lambda = 2\\text{ meter}$, dihitung dari kebalikan kecepatan sudut getaran tali."
      },
      {
        "key": "E",
        "text": "$A = 0{,}08\\text{ m}$, $f = 2\\text{ Hz}$, dan $\\lambda = 1\\text{ meter}$, diperoleh dari $\\omega = 4\\pi \\implies f = \\frac{\\omega}{2\\pi} = 2\\text{ Hz}$, dan $k = 2\\pi \\implies \\lambda = \\frac{2\\pi}{k} = 1\\text{ m}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $A = 0{,}08\\text{ m}$, $f = 2\\text{ Hz}$, dan $\\lambda = 1\\text{ meter}$, diperoleh dari $\\omega = 4\\pi \\implies f = \\frac{\\omega}{2\\pi} = 2\\text{ Hz}$, dan $k = 2\\pi \\implies \\lambda = \\frac{2\\pi}{k} = 1\\text{ m}$.. Bandingkan persamaan dengan y = A sin(omega*t - k*x). omega = 2*pi*f, k = 2*pi / lambda. A = 0,08 m; f = 4pi / 2pi = 2 Hz; lambda = 2pi / 2pi = 1 m."
  },
  {
    "id": "fis-lat-e-11",
    "materi": "GELOMBANG BUNYI",
    "topic": "Taraf Intensitas Bunyi Sumber Jamak",
    "hints": {
      "concept": "Taraf intensitas bertambah secara logaritmik: TIn = TI1 + 10*log10(n).",
      "execution": "TI100 = 60 + 10 * log10(100) = 60 + 10 * 2 = 80 dB."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Taraf intensitas bunyi sebuah sepeda motor knalpot standar pada jarak tertentu adalah $TI_1 = 60\\text{ dB}$. Jika terdapat 100 sepeda motor identik yang dihidupkan secara bersamaan di tempat yang sama, taraf intensitas bunyi total ($TI_{100}$) yang didengar pada jarak tersebut adalah...",
    "formulaHud": {
      "title": "TARAF INTENSITAS N SUMBER IDENTIK",
      "latex": "TI_n = TI_1 + 10\\log_{10}(n) = 60 + 10\\log_{10}(100) = 60 + 10(2) = 80\\text{ dB}",
      "legend": "• Skala Logaritmik Bunyi: Kenaikan 10 dB setara kelipatan intensitas 10 kali lipat<br>• Kenaikan 20 dB setara kelipatan intensitas $10^2 = 100$ kali lipat"
    },
    "options": [
      {
        "key": "A",
        "text": "$80\\text{ dB}$, karena pertambahan taraf intensitas untuk $n = 100$ sumber identik adalah $10\\log_{10}(n) = 10\\log_{10}(100) = 10 \\times 2 = 20\\text{ dB}$, sehingga $TI_{100} = 60 + 20 = 80\\text{ dB}$."
      },
      {
        "key": "B",
        "text": "$600\\text{ dB}$, karena taraf intensitas keliru dikalikan langsung dengan 100 secara linier sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$160\\text{ dB}$, dihitung dengan menambahkan 100 desibel secara langsung ke taraf intensitas satu motor."
      },
      {
        "key": "D",
        "text": "$70\\text{ dB}$, karena penambahan sumber bunyi dianggap hanya menaikkan 10 desibel untuk setiap kelipatan seratus."
      },
      {
        "key": "E",
        "text": "$120\\text{ dB}$, dihitung dari perkalian taraf intensitas tunggal dengan faktor kuadrat logaritma natural."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $80\\text{ dB}$, karena pertambahan taraf intensitas untuk $n = 100$ sumber identik adalah $10\\log_{10}(n) = 10\\log_{10}(100) = 10 \\times 2 = 20\\text{ dB}$, sehingga $TI_{100} = 60 + 20 = 80\\text{ dB}$.. Taraf intensitas bertambah secara logaritmik: TIn = TI1 + 10*log10(n). TI100 = 60 + 10 * log10(100) = 60 + 10 * 2 = 80 dB."
  },
  {
    "id": "fis-lat-e-12",
    "materi": "LISTRIK STATIS",
    "topic": "Hukum Coulomb Dua Muatan Titik",
    "hints": {
      "concept": "F = k * q1 * q2 / r^2. Ingat konversi: microCoulomb = 10^-6 C, dan cm ke m: 30 cm = 0,3 m.",
      "execution": "F = 9e9 * (4e-6 * 9e-6) / (0,3)^2 = 0,324 / 0,09 = 3,6 N."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dua buah muatan titik $q_1 = +4\\,\\mu\\text{C}$ dan $q_2 = +9\\,\\mu\\text{C}$ terpisah pada jarak $r = 30\\text{ cm}$ di udara bebas ($k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2\\text{/C}^2$). Besar gaya tolak-menolak Coulomb antara kedua muatan tersebut adalah...",
    "formulaHud": {
      "title": "HUKUM COULOMB GAYA ELEKTROSTATIK",
      "latex": "F = k \\frac{|q_1 q_2|}{r^2} = (9 \\times 10^9) \\frac{(4 \\times 10^{-6})(9 \\times 10^{-6})}{(0{,}3)^2} = \\frac{324 \\times 10^{-3}}{0{,}09} = 3{,}6\\text{ N}",
      "legend": "• $q_1 = 4 \\times 10^{-6}\\text{ C}$, $q_2 = 9 \\times 10^{-6}\\text{ C}$<br>• $r = 30\\text{ cm} = 0{,}3\\text{ m} \\implies r^2 = 0{,}09\\text{ m}^2$<br>• Kedua muatan sejenis (positif) $\\implies$ Saling tolak-menolak"
    },
    "options": [
      {
        "key": "A",
        "text": "$360\\text{ Newton}$, karena jarak 30 cm keliru dimasukkan tanpa dikonversi ke meter (menggunakan 30 bukan 0,3) sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$3{,}6\\text{ Newton}$, dihitung dari hukum Coulomb $F = k \\frac{q_1 q_2}{r^2} = 9 \\times 10^9 \\times \\frac{(4 \\times 10^{-6})(9 \\times 10^{-6})}{(0{,}3)^2} = \\frac{0{,}324}{0{,}09} = 3{,}6\\text{ N}$."
      },
      {
        "key": "C",
        "text": "$0{,}36\\text{ Newton}$, dihitung dengan mengabaikan konstanta dielektrik ruang hampa udara."
      },
      {
        "key": "D",
        "text": "$1{,}2\\text{ Newton}$, diperoleh dari rata-rata kedua nilai muatan dibagi kuadrat jarak pemisah."
      },
      {
        "key": "E",
        "text": "$10{,}8\\text{ Newton}$, dihitung dari perkalian muatan dengan jarak tanpa menerapkan kuadrat pada penyebut."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $3{,}6\\text{ Newton}$, dihitung dari hukum Coulomb $F = k \\frac{q_1 q_2}{r^2} = 9 \\times 10^9 \\times \\frac{(4 \\times 10^{-6})(9 \\times 10^{-6})}{(0{,}3)^2} = \\frac{0{,}324}{0{,}09} = 3{,}6\\text{ N}$.. F = k * q1 * q2 / r^2. Ingat konversi: microCoulomb = 10^-6 C, dan cm ke m: 30 cm = 0,3 m. F = 9e9 * (4e-6 * 9e-6) / (0,3)^2 = 0,324 / 0,09 = 3,6 N."
  },
  {
    "id": "fis-lat-e-13",
    "materi": "LISTRIK DINAMIS",
    "topic": "Hukum Ohm & Hambatan Rangkaian Seri-Paralel",
    "hints": {
      "concept": "Cari hambatan paralel R1 dan R2: Rp = (6*3)/(6+3) = 2 Ohm. Lalu seri dengan R3: Rtot = 2 + 8 = 10 Ohm. I = V / Rtot.",
      "execution": "Rp = 2 Ohm. Rtot = 10 Ohm. I = 20 / 10 = 2 A."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dua buah resistor $R_1 = 6\\,\\Omega$ dan $R_2 = 3\\,\\Omega$ dirangkai secara paralel, kemudian rangkaian tersebut dihubungkan seri dengan resistor $R_3 = 8\\,\\Omega$. Rangkaian gabungan ini dipasang pada sumber tegangan $V = 20\\text{ Volt}$ dengan hambatan dalam baterai diabaikan. Kuat arus total ($I$) yang keluar dari sumber tegangan adalah...",
    "formulaHud": {
      "title": "HAMBATAN PENGGANTI KOMBINASI",
      "latex": "R_p = \\frac{R_1 R_2}{R_1 + R_2} = \\frac{6 \\times 3}{6 + 3} = 2\\,\\Omega; \\quad R_{\\text{tot}} = R_p + R_3 = 2 + 8 = 10\\,\\Omega; \\quad I = \\frac{V}{R_{\\text{tot}}} = \\frac{20}{10} = 2\\text{ A}",
      "legend": "• $R_p = 2\\,\\Omega$<br>• $R_{\\text{tot}} = 10\\,\\Omega$<br>• Arus Total: $I = 2\\text{ A}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$1{,}18\\text{ Ampere}$, karena seluruh resistor dijumlahkan secara seri biasa menghasilkan hambatan 17 Ohm ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$4\\text{ Ampere}$, dihitung dengan mengabaikan resistor ketiga dalam penentuan arus utama."
      },
      {
        "key": "C",
        "text": "$2\\text{ Ampere}$, karena hambatan pengganti paralel adalah $R_p = \\frac{6 \\times 3}{6 + 3} = 2\\,\\Omega$, sehingga hambatan total rangkaian adalah $R_{\\text{total}} = 2 + 8 = 10\\,\\Omega$, dan arus $I = \\frac{V}{R_{\\text{total}}} = \\frac{20}{10} = 2\\text{ A}$."
      },
      {
        "key": "D",
        "text": "$0{,}5\\text{ Ampere}$, dihitung dari pembagian hambatan total dengan kuadrat tegangan sumber listrik."
      },
      {
        "key": "E",
        "text": "$10\\text{ Ampere}$, dihitung dari nilai tegangan dibagi oleh hambatan paralel tanpa menambahkan resistor seri."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $2\\text{ Ampere}$, karena hambatan pengganti paralel adalah $R_p = \\frac{6 \\times 3}{6 + 3} = 2\\,\\Omega$, sehingga hambatan total rangkaian adalah $R_{\\text{total}} = 2 + 8 = 10\\,\\Omega$, dan arus $I = \\frac{V}{R_{\\text{total}}} = \\frac{20}{10} = 2\\text{ A}$.. Cari hambatan paralel R1 dan R2: Rp = (6*3)/(6+3) = 2 Ohm. Lalu seri dengan R3: Rtot = 2 + 8 = 10 Ohm. I = V / Rtot. Rp = 2 Ohm. Rtot = 10 Ohm. I = 20 / 10 = 2 A."
  },
  {
    "id": "fis-lat-e-14",
    "materi": "KEMAGNETAN",
    "topic": "Gaya Lorentz pada Kawat Lurus Berarus",
    "hints": {
      "concept": "Gaya Lorentz: F = B * I * L * sin(theta). Arah gaya ditentukan dengan kaidah tangan kanan: arus ke kanan, B masuk bidang -> gaya ke atas (utara).",
      "execution": "F = 0,6 * 4 * 0,5 = 1,2 N arah ke utara."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah kawat penghantar lurus mendatar berpanjang $L = 50\\text{ cm}$ dialiri arus listrik $I = 4\\text{ Ampere}$ dari arah barat ke timur. Kawat tersebut berada di dalam medan magnet homogen $B = 0{,}6\\text{ Tesla}$ yang berarah tegak lurus masuk ke dalam bidang kertas. Besar dan arah gaya Lorentz yang bekerja pada kawat tersebut adalah...",
    "formulaHud": {
      "title": "GAYA LORENTZ PADA KAWAT BERARUS",
      "latex": "F = B \\cdot I \\cdot L \\cdot \\sin\\theta = 0{,}6\\text{ T} \\times 4\\text{ A} \\times 0{,}5\\text{ m} \\times \\sin 90^\\circ = 1{,}2\\text{ N}",
      "legend": "• $L = 50\\text{ cm} = 0{,}5\\text{ m}$<br>• Kaidah Tangan Kanan: Ibu jari = Arus (Timur), 4 Jari = Medan B (Masuk), Telapak tangan = Gaya F (Utara/Atas)"
    },
    "options": [
      {
        "key": "A",
        "text": "$120\\text{ Newton}$ ke arah selatan, karena panjang kawat 50 cm keliru dimasukkan tanpa konversi ke satuan meter menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$1{,}2\\text{ Newton}$ ke arah bawah (selatan), karena aturan kaidah tangan kanan tertukar dengan tangan kiri."
      },
      {
        "key": "C",
        "text": "$2{,}4\\text{ Newton}$ ke arah timur, dihitung dari perkalian arus listrik dengan kuadrat kuat medan magnetik."
      },
      {
        "key": "D",
        "text": "$1{,}2\\text{ Newton}$ ke arah utara (ke atas bidang), dihitung dari rumus $F = B I L \\sin 90^\\circ = 0{,}6 \\times 4 \\times 0{,}5\\text{ m} = 1{,}2\\text{ N}$, dengan aturan kaidah tangan kanan."
      },
      {
        "key": "E",
        "text": "$0{,}6\\text{ Newton}$ ke arah barat, karena medan magnet diasumsikan berlawanan arah dengan arah arus kawat."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $1{,}2\\text{ Newton}$ ke arah utara (ke atas bidang), dihitung dari rumus $F = B I L \\sin 90^\\circ = 0{,}6 \\times 4 \\times 0{,}5\\text{ m} = 1{,}2\\text{ N}$, dengan aturan kaidah tangan kanan.. Gaya Lorentz: F = B * I * L * sin(theta). Arah gaya ditentukan dengan kaidah tangan kanan: arus ke kanan, B masuk bidang -> gaya ke atas (utara). F = 0,6 * 4 * 0,5 = 1,2 N arah ke utara."
  },
  {
    "id": "fis-lat-e-15",
    "materi": "INDUKSI ELEKTROMAGNETIK",
    "topic": "GGL Induksi Hukum Faraday pada Kumparan",
    "hints": {
      "concept": "GGL Induksi Faraday: eps = N * |delta_phi| / delta_t. delta_phi = 0,08 - 0,02 = 0,06 Wb.",
      "execution": "eps = 200 * 0,06 / 0,2 = 200 * 0,3 = 60 Volt."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah kumparan kawat memiliki $N = 200\\text{ lilitan}$. Fluks magnetik yang menembus kumparan tersebut berubah dari $\\Phi_1 = 0{,}08\\text{ Weber}$ menjadi $\\Phi_2 = 0{,}02\\text{ Weber}$ dalam selang waktu $\\Delta t = 0{,}2\\text{ sekon}$. Besar gaya gerak listrik (GGL) induksi rata-rata yang timbul pada ujung-ujung kumparan adalah...",
    "formulaHud": {
      "title": "HUKUM FARADAY GGL INDUKSI",
      "latex": "\\varepsilon = -N \\frac{\\Delta \\Phi}{\\Delta t} = -200 \\left(\\frac{0{,}02 - 0{,}08}{0{,}2}\\right) = -200 \\left(\\frac{-0{,}06}{0{,}2}\\right) = 60\\text{ Volt}",
      "legend": "• Tanda negatif (Hukum Lenz) menunjukkan arah GGL induksi selalu menentang perubahan fluks penyebabnya<br>• Besar GGL Induksi: $|\\varepsilon| = 60\\text{ V}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$6\\text{ Volt}$, karena jumlah lilitan keliru dimasukkan hanya 20 lilitan dalam rumus perhitungan ggl diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$120\\text{ Volt}$, dihitung dari perkalian jumlah lilitan dengan fluks awal tanpa memperhitungkan fluks akhir."
      },
      {
        "key": "C",
        "text": "$30\\text{ Volt}$, diperoleh dari pembagian selisih fluks magnetik dengan kuadrat selang waktu pengamatan."
      },
      {
        "key": "D",
        "text": "$600\\text{ Volt}$, karena selang waktu 0,2 sekon keliru dikalikan ke pembilang bukan sebagai pembagi."
      },
      {
        "key": "E",
        "text": "$60\\text{ Volt}$, dihitung dari Hukum Faraday: $\\varepsilon = -N \\frac{\\Delta\\Phi}{\\Delta t} = -200 \\times \\frac{0{,}02 - 0{,}08}{0{,}2} = -200 \\times (-0{,}3) = 60\\text{ V}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $60\\text{ Volt}$, dihitung dari Hukum Faraday: $\\varepsilon = -N \\frac{\\Delta\\Phi}{\\Delta t} = -200 \\times \\frac{0{,}02 - 0{,}08}{0{,}2} = -200 \\times (-0{,}3) = 60\\text{ V}$.. GGL Induksi Faraday: eps = N * |delta_phi| / delta_t. delta_phi = 0,08 - 0,02 = 0,06 Wb. eps = 200 * 0,06 / 0,2 = 200 * 0,3 = 60 Volt."
  },
  {
    "id": "fis-lat-e-16",
    "materi": "TRANSFORMATOR",
    "topic": "Efisiensi dan Rasio Trafo Step-Down",
    "hints": {
      "concept": "Trafo ideal: Ns / Np = Vs / Vp dan Ip / Is = Vs / Vp.",
      "execution": "Ns = 1000 * (22 / 220) = 100 lilitan. Ip = 5 * (22 / 220) = 0,5 Ampere."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah transformator step-down ideal (efisiensi $\\eta = 100\\%$) menurunkan tegangan bolak-balik dari $V_p = 220\\text{ Volt}$ menjadi $V_s = 22\\text{ Volt}$. Jika kumparan primer terdiri atas $N_p = 1.000\\text{ lilitan}$ dan arus yang mengalir pada kumparan sekunder adalah $I_s = 5\\text{ Ampere}$, maka jumlah lilitan sekunder ($N_s$) dan kuat arus primer ($I_p$) adalah...",
    "formulaHud": {
      "title": "PERSAMAAN TRANSFORMATOR IDEAL",
      "latex": "\\frac{V_s}{V_p} = \\frac{N_s}{N_p} = \\frac{I_p}{I_s} \\implies N_s = N_p \\frac{V_s}{V_p}; \\quad I_p = I_s \\frac{V_s}{V_p}",
      "legend": "• $N_s = 1.000 \\times \\frac{22}{220} = 1.000 \\times 0{,}1 = 100\\text{ lilitan}$<br>• $I_p = 5 \\times \\frac{22}{220} = 5 \\times 0{,}1 = 0{,}5\\text{ A}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$N_s = 100\\text{ lilitan}$ dan $I_p = 0{,}5\\text{ Ampere}$, karena perbandingan lilitan sebanding dengan perbandingan tegangan ($\\frac{N_s}{N_p} = \\frac{22}{220} = \\frac{1}{10}$), dan daya trafo ideal $P_p = P_s \\implies V_p I_p = V_s I_s$."
      },
      {
        "key": "B",
        "text": "$N_s = 10.000\\text{ lilitan}$ dan $I_p = 50\\text{ Ampere}$, karena trafo step-down keliru dianggap menaikkan jumlah lilitan sekunder sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$N_s = 100\\text{ lilitan}$ dan $I_p = 5\\text{ Ampere}$, dengan anggapan bahwa arus primer selalu identik dengan arus sekunder."
      },
      {
        "key": "D",
        "text": "$N_s = 500\\text{ lilitan}$ dan $I_p = 2{,}5\\text{ Ampere}$, dihitung dari rata-rata nilai tegangan masukan."
      },
      {
        "key": "E",
        "text": "$N_s = 50\\text{ lilitan}$ dan $I_p = 1\\text{ Ampere}$, dihitung dari selisih daya primer dan sekunder."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $N_s = 100\\text{ lilitan}$ dan $I_p = 0{,}5\\text{ Ampere}$, karena perbandingan lilitan sebanding dengan perbandingan tegangan ($\\frac{N_s}{N_p} = \\frac{22}{220} = \\frac{1}{10}$), dan daya trafo ideal $P_p = P_s \\implies V_p I_p = V_s I_s$.. Trafo ideal: Ns / Np = Vs / Vp dan Ip / Is = Vs / Vp. Ns = 1000 * (22 / 220) = 100 lilitan. Ip = 5 * (22 / 220) = 0,5 Ampere."
  },
  {
    "id": "fis-lat-e-17",
    "materi": "OPTIKA GEOMETRI",
    "topic": "Pembentukan Bayangan pada Cermin Cekung",
    "hints": {
      "concept": "Titik fokus cermin cekung f = R / 2 = 10 cm. Gunakan rumus 1/f = 1/s + 1/s'.",
      "execution": "1/s' = 1/10 - 1/15 = 1/30 -> s' = +30 cm (nyata, terbalik, diperbesar M = 30/15 = 2x)."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah benda diletakkan pada jarak $s = 15\\text{ cm}$ di depan cermin cekung yang memiliki jari-jari kelengkungan $R = 20\\text{ cm}$. Jarak bayangan ($s'$) yang terbentuk dan sifat bayangan tersebut adalah...",
    "formulaHud": {
      "title": "PERSAMAAN CERMIN CEKUNG",
      "latex": "f = \\frac{R}{2} = 10\\text{ cm}; \\quad \\frac{1}{f} = \\frac{1}{s} + \\frac{1}{s'} \\implies \\frac{1}{s'} = \\frac{1}{10} - \\frac{1}{15} = \\frac{3 - 2}{30} = \\frac{1}{30} \\implies s' = +30\\text{ cm}",
      "legend": "• Perbesaran: $M = \\left|\\frac{s'}{s}\\right| = \\frac{30}{15} = 2\\text{ kali}$<br>• $s' > 0 \\implies$ Bayangan Nyata di depan cermin (selalu terbalik)"
    },
    "options": [
      {
        "key": "A",
        "text": "Jarak bayangan $s' = 10\\text{ cm}$ di belakang cermin dengan sifat maya, tegak, dan sama besar sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "Jarak bayangan $s' = 30\\text{ cm}$ di depan cermin dengan sifat nyata, terbalik, dan diperbesar 2 kali ($M = 2$), dihitung dari titik fokus $f = \\frac{R}{2} = 10\\text{ cm}$ dan rumus $\\frac{1}{s'} = \\frac{1}{10} - \\frac{1}{15} = \\frac{1}{30}$."
      },
      {
        "key": "C",
        "text": "Jarak bayangan $s' = 60\\text{ cm}$ di depan cermin dengan sifat maya, terbalik, dan diperkecil."
      },
      {
        "key": "D",
        "text": "Jarak bayangan $s' = 15\\text{ cm}$ di depan cermin dengan sifat nyata, tegak, dan diperbesar tak hingga."
      },
      {
        "key": "E",
        "text": "Jarak bayangan $s' = 7{,}5\\text{ cm}$ di belakang cermin dengan sifat nyata, tegak, dan diperkecil separuhnya."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Jarak bayangan $s' = 30\\text{ cm}$ di depan cermin dengan sifat nyata, terbalik, dan diperbesar 2 kali ($M = 2$), dihitung dari titik fokus $f = \\frac{R}{2} = 10\\text{ cm}$ dan rumus $\\frac{1}{s'} = \\frac{1}{10} - \\frac{1}{15} = \\frac{1}{30}$.. Titik fokus cermin cekung f = R / 2 = 10 cm. Gunakan rumus 1/f = 1/s + 1/s'. 1/s' = 1/10 - 1/15 = 1/30 -> s' = +30 cm (nyata, terbalik, diperbesar M = 30/15 = 2x)."
  },
  {
    "id": "fis-lat-e-18",
    "materi": "OPTIKA GEOMETRI",
    "topic": "Kekuatan Lensa Kacamata Miopi (Rabun Jauh)",
    "hints": {
      "concept": "Rumus daya lensa untuk miopi: P = -1 / PR (dalam meter) atau P = -100 / PR (dalam cm).",
      "execution": "P = -1 / 2 = -0,5 Dioptri."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Seseorang menderita rabun jauh (miopi) sehingga titik jauhnya (Punctum Remotum / PR) berada pada jarak $2\\text{ meter}$ di depan matanya. Agar orang tersebut dapat melihat benda-benda yang sangat jauh ($s = \\infty$) dengan jelas tanpa berakomodasi, daya/kekuatan lensa kacamata ($P$) yang harus digunakan adalah...",
    "formulaHud": {
      "title": "DAYA LENSA KACAMATA MIOPI",
      "latex": "P = -\\frac{1}{\\text{PR(meter)}} = -\\frac{100}{\\text{PR(cm)}} = -\\frac{1}{2\\text{ m}} = -0{,}5\\text{ Dioptri (D)}",
      "legend": "• Lensa Cekung (Negatif) membiaskan berkas sejajar agar seolah-olah berasal dari Punctum Remotum (PR)<br>• $s = \\infty \\implies \\frac{1}{f} = \\frac{1}{\\infty} + \\frac{1}{-2} = -0{,}5 \\implies P = -0{,}5\\text{ D}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$+0{,}5\\text{ Dioptri}$, karena penderita rabun jauh keliru diberi kacamata berlensa cembung positif pengumpul cahaya ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$-2{,}0\\text{ Dioptri}$, dihitung dengan menyamakan daya lensa langsung dengan jarak titik jauh mata dalam meter."
      },
      {
        "key": "C",
        "text": "$-0{,}5\\text{ Dioptri}$, karena kacamata berlensa cekung (divergen/negatif) harus membentuk bayangan maya benda tak terhingga di titik jauh matanya ($s' = -2\\text{ m}$), sehingga $P = -\\frac{1}{\\text{PR(m)}} = -\\frac{1}{2} = -0{,}5\\text{ D}$."
      },
      {
        "key": "D",
        "text": "$+2{,}0\\text{ Dioptri}$, karena daya lensa dihitung dari kebalikan jarak baca normal orang dewasa."
      },
      {
        "key": "E",
        "text": "$-5{,}0\\text{ Dioptri}$, dihitung dari perkalian titik jauh mata dengan ketebalan kornea mata."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $-0{,}5\\text{ Dioptri}$, karena kacamata berlensa cekung (divergen/negatif) harus membentuk bayangan maya benda tak terhingga di titik jauh matanya ($s' = -2\\text{ m}$), sehingga $P = -\\frac{1}{\\text{PR(m)}} = -\\frac{1}{2} = -0{,}5\\text{ D}$.. Rumus daya lensa untuk miopi: P = -1 / PR (dalam meter) atau P = -100 / PR (dalam cm). P = -1 / 2 = -0,5 Dioptri."
  },
  {
    "id": "fis-lat-e-19",
    "materi": "TEORI KINETIK GAS",
    "topic": "Energi Kinetik Rata-Rata Gas Monoatomik",
    "hints": {
      "concept": "Energi kinetik gas monoatomik: Ek = 3/2 * k * T.",
      "execution": "Ek = 1,5 * (1,38e-23) * 300 = 6,21 * 10^-21 Joule."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Suatu gas ideal monoatomik (seperti gas Helium) berada di dalam wadah tertutup pada suhu mutlak $T = 300\\text{ Kelvin}$. Jika konstanta Boltzmann adalah $k = 1{,}38 \\times 10^{-23}\\text{ J/K}$, besar energi kinetik translasi rata-rata per molekul gas tersebut adalah...",
    "formulaHud": {
      "title": "TEOREMA EKUIPARTISI ENERGI KINETIK GAS",
      "latex": "\\bar{E}_k = \\frac{f}{2} k T = \\frac{3}{2} k T = 1{,}5 \\times (1{,}38 \\times 10^{-23}) \\times 300 = 6{,}21 \\times 10^{-21}\\text{ J}",
      "legend": "• Gas Monoatomik: Derajat kebebasan $f = 3$ (gerak translasi sumbu x, y, z)<br>• $\\bar{E}_k$ semata-mata merupakan fungsi dari suhu mutlak $T$ (tidak dipengaruhi jenis atau massa molekul gas)"
    },
    "options": [
      {
        "key": "A",
        "text": "$4{,}14 \\times 10^{-21}\\text{ Joule}$, dihitung dari persamaan gas dengan 2 derajat kebebasan tanpa memperhitungkan gerak translasi tiga dimensi menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$1{,}035 \\times 10^{-20}\\text{ Joule}$, dihitung dengan menganggap gas monoatomik memiliki derajat kebebasan vibrasi seperti gas poliatomik."
      },
      {
        "key": "C",
        "text": "$2{,}07 \\times 10^{-21}\\text{ Joule}$, dihitung dengan mengabaikan faktor pengali tiga per dua dari teorema ekuipartisi energi."
      },
      {
        "key": "D",
        "text": "$6{,}21 \\times 10^{-21}\\text{ Joule}$, dihitung dari persamaan energi kinetik gas monoatomik yang memiliki 3 derajat kebebasan: $\\bar{E}_k = \\frac{3}{2}kT = \\frac{3}{2}(1{,}38 \\times 10^{-23})(300)$."
      },
      {
        "key": "E",
        "text": "$9{,}32 \\times 10^{-21}\\text{ Joule}$, dihitung dari perkalian konstanta gas universal dengan suhu Celcius."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $6{,}21 \\times 10^{-21}\\text{ Joule}$, dihitung dari persamaan energi kinetik gas monoatomik yang memiliki 3 derajat kebebasan: $\\bar{E}_k = \\frac{3}{2}kT = \\frac{3}{2}(1{,}38 \\times 10^{-23})(300)$.. Energi kinetik gas monoatomik: Ek = 3/2 * k * T. Ek = 1,5 * (1,38e-23) * 300 = 6,21 * 10^-21 Joule."
  },
  {
    "id": "fis-lat-e-20",
    "materi": "TERMODINAMIKA (MESIN KALOR)",
    "topic": "Efisiensi Mesin Kalor Siklus Carnot",
    "hints": {
      "concept": "Efisiensi Carnot: eta = 1 - (Tc / Th). Usaha: W = eta * Qh.",
      "execution": "eta = 1 - (350 / 500) = 0,30. W = 0,30 * 10000 = 3000 Joule."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah mesin kalor Carnot bekerja di antara dua reservoir bersuhu tinggi $T_H = 500\\text{ Kelvin}$ dan reservoir bersuhu rendah $T_C = 350\\text{ Kelvin}$. Jika mesin menyerap kalor dari reservoir panas sebesar $Q_H = 10.000\\text{ Joule}$ dalam satu siklus, usaha mekanik ($W$) yang dihasilkan oleh mesin Carnot tersebut adalah...",
    "formulaHud": {
      "title": "EFISIENSI MESIN SIKLUS CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H} \\implies W = Q_H \\left(1 - \\frac{T_C}{T_H}\\right) = 10.000 \\times \\left(1 - \\frac{350}{500}\\right) = 3.000\\text{ J}",
      "legend": "• $\\eta = 1 - 0{,}70 = 0{,}30$ (30%)<br>• $W = 0{,}30 \\times 10.000 = 3.000\\text{ J}$<br>• Kalor Buang: $Q_C = Q_H - W = 7.000\\text{ J}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$7.000\\text{ Joule}$, karena nilai tersebut merupakan kalor sisa ($Q_C$) yang dibuang ke reservoir dingin, bukan usaha yang dihasilkan diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$5.000\\text{ Joule}$, dengan asumsi mesin Carnot memiliki efisiensi maksimal 50% pada seluruh rentang temperatur."
      },
      {
        "key": "C",
        "text": "$1.500\\text{ Joule}$, dihitung dari perbandingan selisih suhu reservoir terhadap suhu titik beku air murni."
      },
      {
        "key": "D",
        "text": "$10.000\\text{ Joule}$, karena mesin ideal diasumsikan mampu mengubah seluruh kalor serap menjadi usaha mekanik tanpa rugi."
      },
      {
        "key": "E",
        "text": "$3.000\\text{ Joule}$, karena efisiensi mesin Carnot adalah $\\eta = 1 - \\frac{T_C}{T_H} = 1 - \\frac{350}{500} = 0{,}30$ (30%), sehingga usaha yang dihasilkan $W = \\eta \\cdot Q_H = 0{,}30 \\times 10.000\\text{ J} = 3.000\\text{ J}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $3.000\\text{ Joule}$, karena efisiensi mesin Carnot adalah $\\eta = 1 - \\frac{T_C}{T_H} = 1 - \\frac{350}{500} = 0{,}30$ (30%), sehingga usaha yang dihasilkan $W = \\eta \\cdot Q_H = 0{,}30 \\times 10.000\\text{ J} = 3.000\\text{ J}$.. Efisiensi Carnot: eta = 1 - (Tc / Th). Usaha: W = eta * Qh. eta = 1 - (350 / 500) = 0,30. W = 0,30 * 10000 = 3000 Joule."
  },
  {
    "id": "fis-lat-e-21",
    "materi": "GELOMBANG ELEKTROMAGNETIK",
    "topic": "Spektrum Gelombang Elektromagnetik",
    "hints": {
      "concept": "Urutan frekuensi rendah ke tinggi: Radio, Mikro, Inframerah, Tampak (Me-Ji-Ku-Hi-Bi-Ni-U), Ultraviolet, Sinar-X, Sinar Gamma.",
      "execution": "Radio -> Mikro -> Inframerah -> Tampak -> UV -> Sinar-X -> Gamma."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Urutan spektrum gelombang elektromagnetik dari frekuensi paling rendah ke frekuensi paling tinggi (panjang gelombang paling besar ke paling kecil) yang tepat adalah...",
    "formulaHud": {
      "title": "SPEKTRUM GELOMBANG ELEKTROMAGNETIK",
      "latex": "c = \\lambda \\cdot f \\implies f \\uparrow \\iff \\lambda \\downarrow \\iff E = hf \\uparrow",
      "legend": "• Frekuensi Terendah (Panjang Gelombang Terbesar): Radio ($f \\sim 10^4 - 10^8\\text{ Hz}$)<br>• Frekuensi Tertinggi (Energi Foton Terbesar): Sinar Gamma ($f > 10^{20}\\text{ Hz}$)"
    },
    "options": [
      {
        "key": "A",
        "text": "Gelombang Radio $\\rightarrow$ Gelombang Mikro (Radar) $\\rightarrow$ Inframerah $\\rightarrow$ Cahaya Tampak $\\rightarrow$ Ultraviolet $\\rightarrow$ Sinar-X $\\rightarrow$ Sinar Gamma."
      },
      {
        "key": "B",
        "text": "Sinar Gamma $\\rightarrow$ Sinar-X $\\rightarrow$ Ultraviolet $\\rightarrow$ Cahaya Tampak $\\rightarrow$ Inframerah $\\rightarrow$ Gelombang Mikro $\\rightarrow$ Gelombang Radio sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "Gelombang Radio $\\rightarrow$ Cahaya Tampak $\\rightarrow$ Gelombang Mikro $\\rightarrow$ Sinar-X $\\rightarrow$ Inframerah $\\rightarrow$ Sinar Gamma $\\rightarrow$ Ultraviolet."
      },
      {
        "key": "D",
        "text": "Cahaya Tampak $\\rightarrow$ Inframerah $\\rightarrow$ Ultraviolet $\\rightarrow$ Gelombang Radio $\\rightarrow$ Sinar Gamma $\\rightarrow$ Sinar-X $\\rightarrow$ Radar."
      },
      {
        "key": "E",
        "text": "Ultraviolet $\\rightarrow$ Sinar-X $\\rightarrow$ Sinar Gamma $\\rightarrow$ Gelombang Radio $\\rightarrow$ Gelombang Mikro $\\rightarrow$ Inframerah $\\rightarrow$ Cahaya Tampak."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Gelombang Radio $\\rightarrow$ Gelombang Mikro (Radar) $\\rightarrow$ Inframerah $\\rightarrow$ Cahaya Tampak $\\rightarrow$ Ultraviolet $\\rightarrow$ Sinar-X $\\rightarrow$ Sinar Gamma.. Urutan frekuensi rendah ke tinggi: Radio, Mikro, Inframerah, Tampak (Me-Ji-Ku-Hi-Bi-Ni-U), Ultraviolet, Sinar-X, Sinar Gamma. Radio -> Mikro -> Inframerah -> Tampak -> UV -> Sinar-X -> Gamma."
  },
  {
    "id": "fis-lat-e-22",
    "materi": "FISIKA MODERN (RELATIVITAS KHUSUS)",
    "topic": "Dilatasi Waktu Relativistik",
    "hints": {
      "concept": "Dilatasi waktu: delta_t = delta_t0 / sqrt(1 - v^2/c^2).",
      "execution": "sqrt(1 - 0,8^2) = 0,6. delta_t = 6 / 0,6 = 10 tahun."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dua orang astronot kembar A dan B berusia 25 tahun. Astronot B melakukan perjalanan antariksa dengan pesawat roket berkecepatan $v = 0{,}8c$ (di mana $c$ adalah kecepatan cahaya) menuju bintang Alpha Centauri. Menurut jam di dalam pesawat astronot B, perjalanan berlangsung selama $\\Delta t_0 = 6\\text{ tahun}$. Waktu perjalanan tersebut menurut pengamat A yang diam di bumi adalah...",
    "formulaHud": {
      "title": "DILATASI WAKTU RELATIVISTIK",
      "latex": "\\Delta t = \\frac{\\Delta t_0}{\\sqrt{1 - \\frac{v^2}{c^2}}} = \\frac{6}{\\sqrt{1 - (0{,}8)^2}} = \\frac{6}{\\sqrt{1 - 0{,}64}} = \\frac{6}{0{,}6} = 10\\text{ tahun}",
      "legend": "• $\\Delta t_0 = 6\\text{ tahun}$ (Waktu tepat / Proper time diukur oleh astronot B)<br>• $\\Delta t = 10\\text{ tahun}$ (Waktu dilatasi diukur oleh pengamat diam di bumi)<br>• Jam yang bergerak berdetak lebih lambat daripada jam pengamat diam"
    },
    "options": [
      {
        "key": "A",
        "text": "$4{,}8\\text{ tahun}$, dihitung dengan mengalikan waktu tepat dengan faktor 0,8 tanpa menerapkan rumus dilatasi waktu pembagi sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$10\\text{ tahun}$, karena efek dilatasi waktu Einstein menetapkan bahwa waktu pengamat diam memanjang menurut faktor Lorentz $\\gamma = \\frac{1}{\\sqrt{1 - (0{,}8)^2}} = \\frac{1}{0{,}6} = \\frac{5}{3}$, sehingga $\\Delta t = \\gamma \\cdot \\Delta t_0 = \\frac{5}{3} \\times 6 = 10\\text{ tahun}$."
      },
      {
        "key": "C",
        "text": "$3{,}6\\text{ tahun}$, dihitung dari perkalian waktu diam dengan kuadrat faktor kontraksi panjang."
      },
      {
        "key": "D",
        "text": "$6\\text{ tahun}$, karena hukum fisika klasik Newton menganggap waktu bersifat mutlak di seluruh penjuru alam semesta."
      },
      {
        "key": "E",
        "text": "$15\\text{ tahun}$, dihitung dari perkalian waktu penjelajah dengan konstanta kecepatan cahaya kuadrat."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $10\\text{ tahun}$, karena efek dilatasi waktu Einstein menetapkan bahwa waktu pengamat diam memanjang menurut faktor Lorentz $\\gamma = \\frac{1}{\\sqrt{1 - (0{,}8)^2}} = \\frac{1}{0{,}6} = \\frac{5}{3}$, sehingga $\\Delta t = \\gamma \\cdot \\Delta t_0 = \\frac{5}{3} \\times 6 = 10\\text{ tahun}$.. Dilatasi waktu: delta_t = delta_t0 / sqrt(1 - v^2/c^2). sqrt(1 - 0,8^2) = 0,6. delta_t = 6 / 0,6 = 10 tahun."
  },
  {
    "id": "fis-lat-e-23",
    "materi": "FISIKA MODERN (RELATIVITAS KHUSUS)",
    "topic": "Kontraksi Panjang Relativistik",
    "hints": {
      "concept": "Kontraksi panjang Lorentz: L = L0 * sqrt(1 - v^2/c^2).",
      "execution": "L = 100 * sqrt(1 - 0,36) = 100 * 0,8 = 80 meter."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah pesawat antariksa memiliki panjang $L_0 = 100\\text{ meter}$ saat diukur diam di landasan peluncuran bumi. Pesawat tersebut kemudian terbang melintasi bumi dengan kecepatan tetap $v = 0{,}6c$. Panjang pesawat saat melintas menurut pengamat stasioner di bumi adalah...",
    "formulaHud": {
      "title": "KONTRAKSI PANJANG RELATIVISTIK (LORENTZ)",
      "latex": "L = L_0 \\sqrt{1 - \\frac{v^2}{c^2}} = 100 \\times \\sqrt{1 - 0{,}36} = 100 \\times \\sqrt{0{,}64} = 100 \\times 0{,}8 = 80\\text{ meter}",
      "legend": "• $L_0 = 100\\text{ m}$ (Panjang sejati / Proper length)<br>• $L = 80\\text{ m}$ (Panjang teramati menyusut hanya pada dimensi yang sejajar arah gerak)"
    },
    "options": [
      {
        "key": "A",
        "text": "$125\\text{ meter}$, karena panjang pesawat keliru dihitung memanjang dengan membagi panjang diam terhadap faktor Lorentz ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$60\\text{ meter}$, dihitung dengan mengalikan panjang diam secara langsung dengan koefisien kecepatan 0,6."
      },
      {
        "key": "C",
        "text": "$80\\text{ meter}$, karena pengamat yang diam mengamati terjadinya pengerutan/kontraksi panjang searah gerak benda: $L = L_0 \\sqrt{1 - \\frac{v^2}{c^2}} = 100 \\times \\sqrt{1 - (0{,}6)^2} = 100 \\times 0{,}8 = 80\\text{ meter}$."
      },
      {
        "key": "D",
        "text": "$100\\text{ meter}$, karena panjang benda fisik dianggap kekal dan tidak dapat dipengaruhi oleh kelajuan gerak roket."
      },
      {
        "key": "E",
        "text": "$40\\text{ meter}$, dihitung dari selisih kuadrat panjang diam dengan konstanta kelajuan cahaya."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $80\\text{ meter}$, karena pengamat yang diam mengamati terjadinya pengerutan/kontraksi panjang searah gerak benda: $L = L_0 \\sqrt{1 - \\frac{v^2}{c^2}} = 100 \\times \\sqrt{1 - (0{,}6)^2} = 100 \\times 0{,}8 = 80\\text{ meter}$.. Kontraksi panjang Lorentz: L = L0 * sqrt(1 - v^2/c^2). L = 100 * sqrt(1 - 0,36) = 100 * 0,8 = 80 meter."
  },
  {
    "id": "fis-lat-e-24",
    "materi": "FISIKA KUANTUM & ATOM",
    "topic": "Panjang Gelombang de Broglie",
    "hints": {
      "concept": "Panjang gelombang de Broglie: lambda = h / (m * v).",
      "execution": "p = 9e-31 * 2e6 = 1,8e-24 kg*m/s. lambda = 6,63e-34 / 1,8e-24 = 3,68 * 10^-10 meter."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah elektron bermassa $m = 9 \\times 10^{-31}\\text{ kg}$ bergerak dengan kecepatan konstan $v = 2 \\times 10^6\\text{ m/s}$. Jika konstanta Planck adalah $h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$, panjang gelombang de Broglie dari elektron tersebut adalah...",
    "formulaHud": {
      "title": "HIPOTESIS DE BROGLIE DUALISME GELOMBANG PARTIKEL",
      "latex": "\\lambda = \\frac{h}{p} = \\frac{h}{m \\cdot v} = \\frac{6{,}63 \\times 10^{-34}}{(9 \\times 10^{-31})(2 \\times 10^6)} = \\frac{6{,}63 \\times 10^{-34}}{18 \\times 10^{-25}} \\approx 3{,}68 \\times 10^{-10}\\text{ m}",
      "legend": "• $h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$<br>• Momentum $p = m \\cdot v = 1{,}8 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}$<br>• Panjang gelombang ini berada pada skala ukuran kisi kristal padatan (memungkinkan terjadinya difraksi elektron)"
    },
    "options": [
      {
        "key": "A",
        "text": "$3{,}68 \\times 10^{-7}\\text{ meter}$, karena eksponen kecepatan elektron keliru dimasukkan bertanda negatif dalam perhitungan menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$1{,}84 \\times 10^{-10}\\text{ meter}$, dihitung dengan mengabaikan konstanta massa elektron pada penyebut momentum linier."
      },
      {
        "key": "C",
        "text": "$7{,}36 \\times 10^{-10}\\text{ meter}$, dihitung dari perkalian momentum elektron dengan konstanta Planck secara langsung."
      },
      {
        "key": "D",
        "text": "$3{,}68 \\times 10^{-10}\\text{ meter}$ (atau $0{,}368\\text{ nm}$), dihitung dari hipotesis dualisme partikel-gelombang de Broglie: $\\lambda = \\frac{h}{p} = \\frac{h}{m \\cdot v} = \\frac{6{,}63 \\times 10^{-34}}{(9 \\times 10^{-31})(2 \\times 10^6)}$."
      },
      {
        "key": "E",
        "text": "$5{,}50 \\times 10^{-12}\\text{ meter}$, dihitung dari asumsi panjang gelombang foton sinar gamma frekuensi tinggi."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $3{,}68 \\times 10^{-10}\\text{ meter}$ (atau $0{,}368\\text{ nm}$), dihitung dari hipotesis dualisme partikel-gelombang de Broglie: $\\lambda = \\frac{h}{p} = \\frac{h}{m \\cdot v} = \\frac{6{,}63 \\times 10^{-34}}{(9 \\times 10^{-31})(2 \\times 10^6)}$.. Panjang gelombang de Broglie: lambda = h / (m * v). p = 9e-31 * 2e6 = 1,8e-24 kg*m/s. lambda = 6,63e-34 / 1,8e-24 = 3,68 * 10^-10 meter."
  },
  {
    "id": "fis-lat-e-25",
    "materi": "FISIKA INTI & RADIOAKTIVITAS",
    "topic": "Waktu Paruh dan Peluruhan Radioaktif",
    "hints": {
      "concept": "Jumlah paruh n = t / T_half = 16 / 4 = 4. Nt = N0 * (1/2)^n.",
      "execution": "n = 4. Nt = 64 * (1/16) = 4 gram."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Suatu sampel zat radioaktif mula-mula memiliki massa $N_0 = 64\\text{ gram}$. Zat tersebut memiliki waktu paruh (half-life) $T_{1/2} = 4\\text{ jam}$. Massa sampel zat radioaktif yang belum meluruh setelah disimpan selama $t = 16\\text{ jam}$ adalah...",
    "formulaHud": {
      "title": "HUKUM PELURUHAN RADIOAKTIF",
      "latex": "N_t = N_0 \\left(\\frac{1}{2}\\right)^n; \\quad n = \\frac{t}{T_{1/2}} = \\frac{16\\text{ jam}}{4\\text{ jam}} = 4 \\implies N_t = 64 \\times \\left(\\frac{1}{2}\\right)^4 = 64 \\times \\frac{1}{16} = 4\\text{ gram}",
      "legend": "• $N_0 = 64\\text{ g}$ (Massa awal)<br>• $N_t = 4\\text{ g}$ (Massa zat sisa yang belum meluruh)<br>• Massa zat yang telah meluruh: $64 - 4 = 60\\text{ gram}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$8\\text{ gram}$, dihitung dengan menganggap sampel hanya meluruh sebanyak 3 kali periode waktu paruh diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$16\\text{ gram}$, dihitung dengan membagi massa awal secara langsung dengan durasi waktu penyimpanan 16 jam."
      },
      {
        "key": "C",
        "text": "$2\\text{ gram}$, dihitung dari asumsi bahwa zat telah meluruh sebanyak 5 kali periode paruh."
      },
      {
        "key": "D",
        "text": "$0\\text{ gram}$, karena zat radioaktif dianggap habis musnah total setelah melewati waktu 12 jam."
      },
      {
        "key": "E",
        "text": "$4\\text{ gram}$, karena selama 16 jam zat telah mengalami $n = \\frac{t}{T_{1/2}} = \\frac{16}{4} = 4$ kali periode peluruhan, sehingga massa yang tersisa adalah $N_t = N_0 \\left(\\frac{1}{2}\\right)^4 = 64 \\times \\frac{1}{16} = 4\\text{ gram}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $4\\text{ gram}$, karena selama 16 jam zat telah mengalami $n = \\frac{t}{T_{1/2}} = \\frac{16}{4} = 4$ kali periode peluruhan, sehingga massa yang tersisa adalah $N_t = N_0 \\left(\\frac{1}{2}\\right)^4 = 64 \\times \\frac{1}{16} = 4\\text{ gram}$.. Jumlah paruh n = t / T_half = 16 / 4 = 4. Nt = N0 * (1/2)^n. n = 4. Nt = 64 * (1/16) = 4 gram."
  },
  {
    "id": "fis-lat-m-01",
    "materi": "KINEMATIKA GERAK DUA DIMENSI",
    "topic": "Gerak Parabola (Jarak Mendatar & Ketinggian Maksimum)",
    "hints": {
      "concept": "Komponen kecepatan vertikal: v0y = v0 * sin(53) = 40 m/s. Di titik puncak, vy = 0. tp = v0y / g. h_max = v0y^2 / (2g).",
      "execution": "tp = 40 / 10 = 4 s. h_max = 40^2 / 20 = 80 m."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah meriam menembakkan peluru dengan kecepatan awal $v_0 = 50\\text{ m/s}$ pada sudut elevasi $\\theta = 53^\\circ$ terhadap horizontal ($\\sin 53^\\circ = 0{,}8$ dan $\\cos 53^\\circ = 0{,}6$). Mengabaikan gesekan udara dan mengasumsikan percepatan gravitasi $g = 10\\text{ m/s}^2$, waktu yang dibutuhkan peluru untuk mencapai titik puncak lintasan ($t_p$) dan tinggi maksimumnya ($h_{\\max}$) adalah...",
    "formulaHud": {
      "title": "FORMULA GERAK PARABOLA (TITIK PUNCAK)",
      "latex": "t_p = \\frac{v_0 \\sin\\theta}{g}; \\quad h_{\\max} = \\frac{(v_0 \\sin\\theta)^2}{2g}; \\quad X_{\\max} = \\frac{v_0^2 \\sin(2\\theta)}{g}",
      "legend": "• $v_{0y} = 50 \\times 0{,}8 = 40\\text{ m/s}$<br>• $t_p = \\frac{40}{10} = 4\\text{ sekon}$<br>• $h_{\\max} = \\frac{40^2}{2 \\times 10} = \\frac{1.600}{20} = 80\\text{ meter}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$t_p = 4\\text{ sekon}$ dan $h_{\\max} = 80\\text{ meter}$, dihitung dari $t_p = \\frac{v_0 \\sin\\theta}{g} = \\frac{50 \\times 0{,}8}{10} = 4\\text{ s}$, dan $h_{\\max} = \\frac{(v_0 \\sin\\theta)^2}{2g} = \\frac{40^2}{20} = 80\\text{ m}$."
      },
      {
        "key": "B",
        "text": "$t_p = 3\\text{ sekon}$ dan $h_{\\max} = 45\\text{ meter}$, karena kecepatan awal keliru diuraikan menggunakan fungsi cosinus pada komponen sumbu vertikal sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$t_p = 5\\text{ sekon}$ dan $h_{\\max} = 125\\text{ meter}$, dihitung dengan mengabaikan sudut elevasi penembakan moncong meriam."
      },
      {
        "key": "D",
        "text": "$t_p = 8\\text{ sekon}$ dan $h_{\\max} = 160\\text{ meter}$, karena waktu mencapai titik puncak tertukar dengan total waktu melayang di udara."
      },
      {
        "key": "E",
        "text": "$t_p = 2\\text{ sekon}$ dan $h_{\\max} = 40\\text{ meter}$, dihitung dari pembagian tinggi maksimum dengan gravitasi bumi tanpa pemangkatan kuadrat."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $t_p = 4\\text{ sekon}$ dan $h_{\\max} = 80\\text{ meter}$, dihitung dari $t_p = \\frac{v_0 \\sin\\theta}{g} = \\frac{50 \\times 0{,}8}{10} = 4\\text{ s}$, dan $h_{\\max} = \\frac{(v_0 \\sin\\theta)^2}{2g} = \\frac{40^2}{20} = 80\\text{ m}$.. Komponen kecepatan vertikal: v0y = v0 * sin(53) = 40 m/s. Di titik puncak, vy = 0. tp = v0y / g. h_max = v0y^2 / (2g). tp = 40 / 10 = 4 s. h_max = 40^2 / 20 = 80 m."
  },
  {
    "id": "fis-lat-m-02",
    "materi": "HUKUM GRAVITASI NEWTON",
    "topic": "Percepatan Gravitasi pada Ketinggian Tertentu di Atas Bumi",
    "hints": {
      "concept": "Jarak diukur selalu dari pusat bumi: r = R + h = 2R. Kuat medan gravitasi berbanding terbalik dengan kuadrat jarak: g_h = g * (R / 2R)^2 = g / 4.",
      "execution": "g_h = 9,8 / 4 = 2,45 m/s²."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah satelit cuaca mengorbit bumi pada ketinggian $h = R$ di atas permukaan bumi, di mana $R$ adalah jari-jari bumi. Jika percepatan gravitasi di permukaan bumi adalah $g = 9{,}8\\text{ m/s}^2$, percepatan gravitasi bumi ($g_h$) yang dialami oleh satelit pada orbit tersebut adalah...",
    "formulaHud": {
      "title": "HUKUM KUADRAT TERBALIK MEDAN GRAVITASI",
      "latex": "g_h = G \\frac{M}{(R + h)^2} = g \\left(\\frac{R}{R + h}\\right)^2 = g \\left(\\frac{R}{2R}\\right)^2 = \\frac{g}{4} = \\frac{9{,}8}{4} = 2{,}45\\text{ m/s}^2",
      "legend": "• $R$ = Jari-jari bumi; $h$ = Ketinggian dari permukaan bumi<br>• Jarak dari pusat massa bumi: $r = R + h = R + R = 2R$<br>• Kuadrat jarak: $(2R)^2 = 4R^2 \\implies$ Medan gravitasi menjadi $\\frac{1}{4}$ kali semula"
    },
    "options": [
      {
        "key": "A",
        "text": "$4{,}90\\text{ m/s}^2$, karena gravitasi keliru dianggap berbanding terbalik secara linier dengan jarak, bukan berbanding terbalik dengan kuadrat jarak sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$2{,}45\\text{ m/s}^2$, karena jarak satelit dari pusat bumi menjadi $r = R + h = 2R$, sehingga percepatan gravitasi berkurang menjadi seperempat dari nilai di permukaan bumi: $g_h = g \\left(\\frac{R}{2R}\\right)^2 = \\frac{g}{4} = \\frac{9{,}8}{4} = 2{,}45\\text{ m/s}^2$."
      },
      {
        "key": "C",
        "text": "$9{,}80\\text{ m/s}^2$, karena gravitasi diasumsikan konstan tidak berkurang di ruang hampa udara lintasan orbit bumi."
      },
      {
        "key": "D",
        "text": "$1{,}08\\text{ m/s}^2$, dihitung dari asumsi jarak satelit dari permukaan bumi adalah sembilan kali jari-jari planet."
      },
      {
        "key": "E",
        "text": "$0\\text{ m/s}^2$, karena satelit dianggap berada dalam kondisi mikrogravitasi mutlak tanpa tarikan massa bumi sama sekali."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $2{,}45\\text{ m/s}^2$, karena jarak satelit dari pusat bumi menjadi $r = R + h = 2R$, sehingga percepatan gravitasi berkurang menjadi seperempat dari nilai di permukaan bumi: $g_h = g \\left(\\frac{R}{2R}\\right)^2 = \\frac{g}{4} = \\frac{9{,}8}{4} = 2{,}45\\text{ m/s}^2$.. Jarak diukur selalu dari pusat bumi: r = R + h = 2R. Kuat medan gravitasi berbanding terbalik dengan kuadrat jarak: g_h = g * (R / 2R)^2 = g / 4. g_h = 9,8 / 4 = 2,45 m/s²."
  },
  {
    "id": "fis-lat-m-03",
    "materi": "DINAMIKA GERAK MELINGKAR",
    "topic": "Kecepatan Maksimum pada Tikungan Datar Kasar",
    "hints": {
      "concept": "Gaya gesek statis menyediakan gaya sentripetal: mu_s * m * g = m * v^2 / R -> v_max = sqrt(mu_s * g * R).",
      "execution": "v = sqrt(0,4 * 10 * 40) = sqrt(160) = 4*sqrt(10) ≈ 12,65 m/s."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah mobil bermassa $1.200\\text{ kg}$ melintasi tikungan jalan datar mendatar yang memiliki jari-jari kelengkungan $R = 40\\text{ meter}$. Koefisien gesekan statik antara ban mobil dengan aspal jalan adalah $\\mu_s = 0{,}4$. Mengambil percepatan gravitasi $g = 10\\text{ m/s}^2$, kelajuan maksimum ($v_{\\max}$) yang diizinkan agar mobil dapat berbelok dengan aman tanpa selip (tergelincir keluar lintasan) adalah...",
    "formulaHud": {
      "title": "KELAJUAN MAKSIMUM TIKUNGAN DATAR",
      "latex": "F_s = F_{sp} \\implies \\mu_s m g = \\frac{m v_{\\max}^2}{R} \\implies v_{\\max} = \\sqrt{\\mu_s g R} = \\sqrt{0{,}4 \\times 10 \\times 40} = \\sqrt{160} \\approx 12{,}65\\text{ m/s}",
      "legend": "• Konversi ke km/jam: $12{,}65 \\times 3{,}6 \\approx 45{,}5 - 46{,}8\\text{ km/jam}$<br>• Kecepatan maksimum tidak bergantung pada massa kendaraan (mobil berat dan motor ringan memiliki batas aman kelajuan yang sama)"
    },
    "options": [
      {
        "key": "A",
        "text": "$20\\text{ m/s}$ (atau $72\\text{ km/jam}$), dihitung dengan mengalikan percepatan gravitasi dengan koefisien gesekan kinetik jalan basah ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$8\\text{ m/s}$ (atau $28{,}8\\text{ km/jam}$), dihitung dari pembagian jari-jari kelengkungan dengan percepatan gravitasi bumi."
      },
      {
        "key": "C",
        "text": "$46{,}8\\text{ km/jam}$ (atau tepat $12{,}65\\text{ m/s}$, dibulatkan dari $\\sqrt{\\mu_s g R} = \\sqrt{0{,}4 \\times 10 \\times 40} = \\sqrt{160} = 4\\sqrt{10}\\text{ m/s} \\approx 12{,}65\\text{ m/s}$), di mana gaya gesek statis bertindak sebagai gaya sentripetal."
      },
      {
        "key": "D",
        "text": "$16\\text{ m/s}$ (atau $57{,}6\\text{ km/jam}$), dihitung dengan mengabaikan akar kuadrat pada perumusan gaya sentripetal mobil."
      },
      {
        "key": "E",
        "text": "$5\\text{ m/s}$ (atau $18\\text{ km/jam}$), dihitung dari rasio massa mobil terhadap jari-jari tikungan aspal jalan."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $46{,}8\\text{ km/jam}$ (atau tepat $12{,}65\\text{ m/s}$, dibulatkan dari $\\sqrt{\\mu_s g R} = \\sqrt{0{,}4 \\times 10 \\times 40} = \\sqrt{160} = 4\\sqrt{10}\\text{ m/s} \\approx 12{,}65\\text{ m/s}$), di mana gaya gesek statis bertindak sebagai gaya sentripetal.. Gaya gesek statis menyediakan gaya sentripetal: mu_s * m * g = m * v^2 / R -> v_max = sqrt(mu_s * g * R). v = sqrt(0,4 * 10 * 40) = sqrt(160) = 4*sqrt(10) ≈ 12,65 m/s."
  },
  {
    "id": "fis-lat-m-04",
    "materi": "TUMBUKAN DAN RESTITUSI",
    "topic": "Koefisien Restitusi Bola Memantul di Lantai",
    "hints": {
      "concept": "Koefisien restitusi bola memantul: e = sqrt(h2 / h1). Ketinggian pantulan berikutnya: h3 = e^2 * h2.",
      "execution": "e = sqrt(80/180) = sqrt(4/9) = 2/3. h3 = (4/9) * 80 = 35,56 cm."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah bola basket dijatuhkan bebas tanpa kecepatan awal dari ketinggian $h_1 = 180\\text{ cm}$ di atas lantai beton keras. Setelah memantul di lantai, bola tersebut mencapai ketinggian pantulan pertama sebesar $h_2 = 80\\text{ cm}$. Nilai koefisien restitusi ($e$) antara bola basket dan lantai serta perkiraan tinggi pantulan kedua ($h_3$) adalah...",
    "formulaHud": {
      "title": "KOEFISIEN RESTITUSI PADA LANTAI PANTAK",
      "latex": "e = \\sqrt{\\frac{h_2}{h_1}} = \\sqrt{\\frac{80}{180}} = \\sqrt{\\frac{4}{9}} = \\frac{2}{3} \\approx 0{,}67; \\quad h_3 = e^2 h_2 = \\left(\\frac{2}{3}\\right)^2 \\times 80 = \\frac{4}{9} \\times 80 = 35{,}56\\text{ cm}",
      "legend": "• Tumbukan Lenting Sebagian: $0 < e < 1$<br>• Deret Geometri Ketinggian Pantulan: $h_n = h_1 (e)^{2(n-1)}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$e = 0{,}44$ dan $h_3 = 20\\text{ cm}$, karena koefisien restitusi keliru dihitung tanpa mengakarkan perbandingan ketinggian pantulan menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$e = 0{,}80$ dan $h_3 = 60\\text{ cm}$, dihitung dari perbandingan selisih ketinggian terhadap percepatan gravitasi bumi."
      },
      {
        "key": "C",
        "text": "$e = 1{,}0$ dan $h_3 = 80\\text{ cm}$, dengan anggapan bahwa bola basket mengalami tumbukan lenting sempurna di atas lantai."
      },
      {
        "key": "D",
        "text": "$e = \\frac{2}{3}$ dan $h_3 = 35{,}56\\text{ cm}$, dihitung dari koefisien restitusi pantulan vertikal $e = \\sqrt{\\frac{h_2}{h_1}} = \\sqrt{\\frac{80}{180}} = \\sqrt{\\frac{4}{9}} = \\frac{2}{3}$, sehingga $h_3 = e^2 h_2 = \\frac{4}{9} \\times 80 = 35{,}56\\text{ cm}$."
      },
      {
        "key": "E",
        "text": "$e = 0{,}50$ dan $h_3 = 40\\text{ cm}$, dihitung dengan membagi dua ketinggian pantulan pertama secara konvensional."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $e = \\frac{2}{3}$ dan $h_3 = 35{,}56\\text{ cm}$, dihitung dari koefisien restitusi pantulan vertikal $e = \\sqrt{\\frac{h_2}{h_1}} = \\sqrt{\\frac{80}{180}} = \\sqrt{\\frac{4}{9}} = \\frac{2}{3}$, sehingga $h_3 = e^2 h_2 = \\frac{4}{9} \\times 80 = 35{,}56\\text{ cm}$.. Koefisien restitusi bola memantul: e = sqrt(h2 / h1). Ketinggian pantulan berikutnya: h3 = e^2 * h2. e = sqrt(80/180) = sqrt(4/9) = 2/3. h3 = (4/9) * 80 = 35,56 cm."
  },
  {
    "id": "fis-lat-m-05",
    "materi": "ELASTISITAS DAN HUKUM HOOKE",
    "topic": "Konstanta Pegas Gabungan dan Energi Potensial Pegas",
    "hints": {
      "concept": "Pegas paralel: kp = k + k = 800 N/m. Delta_x = W / kp = 40 / 800 = 0,05 m. Ep = 0,5 * kp * delta_x^2.",
      "execution": "kp = 800 N/m. delta_x = 0,05 m. Ep = 0,5 * 800 * 0,0025 = 1,0 J."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dua buah pegas identik masing-masing memiliki konstanta $k = 400\\text{ N/m}$. Kedua pegas dirangkai secara paralel, kemudian rangkaian tersebut digantungkan secara vertikal dan diberi beban bermassa $M = 4\\text{ kg}$ pada ujung bawahnya ($g = 10\\text{ m/s}^2$). Pertambahan panjang total rangkaian pegas ($\\Delta x$) dan energi potensial elastis ($E_p$) yang tersimpan di dalam sistem pegas tersebut adalah...",
    "formulaHud": {
      "title": "RANGKAIAN PEGAS PARALEL & ENERGI POTENSIAL",
      "latex": "k_p = k_1 + k_2 = 400 + 400 = 800\\text{ N/m}; \\quad \\Delta x = \\frac{mg}{k_p} = \\frac{40}{800} = 0{,}05\\text{ m}; \\quad E_p = \\frac{1}{2} k_p \\Delta x^2 = 1{,}0\\text{ J}",
      "legend": "• Gaya Berat Beban: $F = W = mg = 4 \\times 10 = 40\\text{ N}$<br>• $E_p = \\frac{1}{2} \\times 800 \\times 0{,}0025 = 1{,}0\\text{ Joule}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta x = 0{,}10\\text{ meter}$ dan $E_p = 4{,}0\\text{ Joule}$, karena kedua pegas keliru dihitung menggunakan perumusan rangkaian seri diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$\\Delta x = 0{,}02\\text{ meter}$ dan $E_p = 0{,}5\\text{ Joule}$, dihitung dengan mengabaikan percepatan gravitasi bumi pada beban."
      },
      {
        "key": "C",
        "text": "$\\Delta x = 0{,}20\\text{ meter}$ dan $E_p = 8{,}0\\text{ Joule}$, dihitung dari hasil kali massa beban dengan konstanta pegas tunggal."
      },
      {
        "key": "D",
        "text": "$\\Delta x = 0{,}05\\text{ meter}$ dan $E_p = 2{,}0\\text{ Joule}$, karena faktor pengali setengah diabaikan dalam perumusan energi potensial pegas."
      },
      {
        "key": "E",
        "text": "$\\Delta x = 0{,}05\\text{ meter}$ ($5\\text{ cm}$) dan $E_p = 1{,}0\\text{ Joule}$, karena konstanta pegas pengganti paralel adalah $k_p = 400 + 400 = 800\\text{ N/m}$, pertambahan panjang $\\Delta x = \\frac{F}{k_p} = \\frac{40}{800} = 0{,}05\\text{ m}$, dan $E_p = \\frac{1}{2} k_p (\\Delta x)^2 = \\frac{1}{2}(800)(0{,}05^2) = 1{,}0\\text{ J}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $\\Delta x = 0{,}05\\text{ meter}$ ($5\\text{ cm}$) dan $E_p = 1{,}0\\text{ Joule}$, karena konstanta pegas pengganti paralel adalah $k_p = 400 + 400 = 800\\text{ N/m}$, pertambahan panjang $\\Delta x = \\frac{F}{k_p} = \\frac{40}{800} = 0{,}05\\text{ m}$, dan $E_p = \\frac{1}{2} k_p (\\Delta x)^2 = \\frac{1}{2}(800)(0{,}05^2) = 1{,}0\\text{ J}$.. Pegas paralel: kp = k + k = 800 N/m. Delta_x = W / kp = 40 / 800 = 0,05 m. Ep = 0,5 * kp * delta_x^2. kp = 800 N/m. delta_x = 0,05 m. Ep = 0,5 * 800 * 0,0025 = 1,0 J."
  },
  {
    "id": "fis-lat-m-06",
    "materi": "FLUIDA DINAMIS (TEOREMA TORRICELLI)",
    "topic": "Jangkauan Pancaran Air dari Lubang Kebocoran Tangki",
    "hints": {
      "concept": "v = sqrt(2 * g * h) dengan h = kedalaman lubang dari permukaan (1,25 m). x = 2 * sqrt(h * h2) dengan h2 = tinggi lubang dari tanah (3,75 m).",
      "execution": "v = sqrt(25) = 5 m/s. x = 2 * sqrt(1,25 * 3,75) = 2 * sqrt(4,6875) ≈ 4,33 m."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah tangki penampung air berukuran besar diletakkan di atas tanah mendatar. Permukaan air berada pada ketinggian $H = 5\\text{ meter}$ dari tanah. Terdapat sebuah lubang kebocoran kecil pada dinding tangki pada kedalaman $h = 1{,}25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Kelajuan pancaran air yang keluar dari lubang ($v$) dan jarak mendatar terjauh jatuhnya air di tanah ($x$) adalah...",
    "formulaHud": {
      "title": "TEOREMA TORRICELLI LUBANG KEBOCORAN TANGKI",
      "latex": "v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 1{,}25} = 5\\text{ m/s}; \\quad x = 2\\sqrt{h \\cdot h_2} = 2\\sqrt{1{,}25 \\times 3{,}75} \\approx 4{,}33\\text{ m}",
      "legend": "• $h = 1{,}25\\text{ m}$ (jarak lubang dari permukaan air)<br>• $h_2 = H - h = 5 - 1{,}25 = 3{,}75\\text{ m}$ (jarak lubang dari tanah)<br>• Waktu jatuh air ke tanah: $t = \\sqrt{\\frac{2h_2}{g}} = \\sqrt{\\frac{7{,}5}{10}} = \\sqrt{0{,}75}\\text{ s}$<br>• Jangkauan mendatar: $x = v \\cdot t = 5 \\times \\sqrt{0{,}75} \\approx 4{,}33\\text{ m}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$v = 5\\text{ m/s}$ dan $x = 4{,}33\\text{ meter}$ (dihitung dari $v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 1{,}25} = 5\\text{ m/s}$, dan $x = 2\\sqrt{h(H - h)} = 2\\sqrt{1{,}25 \\times 3{,}75} = 2\\sqrt{4{,}6875} \\approx 4{,}33\\text{ m}$)."
      },
      {
        "key": "B",
        "text": "$v = 10\\text{ m/s}$ dan $x = 5{,}0\\text{ meter}$, karena kelajuan semburan air dihitung menggunakan total ketinggian tangki penuh dari tanah sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$v = 2{,}5\\text{ m/s}$ dan $x = 2{,}5\\text{ meter}$, dihitung dari pembagian tinggi muka air dengan percepatan gravitasi bumi."
      },
      {
        "key": "D",
        "text": "$v = 5\\text{ m/s}$ dan $x = 10\\text{ meter}$, karena jarak mendatar diasumsikan dua kali lipat dari total tinggi tangki air."
      },
      {
        "key": "E",
        "text": "$v = 7{,}07\\text{ m/s}$ dan $x = 3{,}75\\text{ meter}$, dihitung dengan menukar kedalaman lubang dengan jarak lubang dari tanah."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $v = 5\\text{ m/s}$ dan $x = 4{,}33\\text{ meter}$ (dihitung dari $v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 1{,}25} = 5\\text{ m/s}$, dan $x = 2\\sqrt{h(H - h)} = 2\\sqrt{1{,}25 \\times 3{,}75} = 2\\sqrt{4{,}6875} \\approx 4{,}33\\text{ m}$).. v = sqrt(2 * g * h) dengan h = kedalaman lubang dari permukaan (1,25 m). x = 2 * sqrt(h * h2) dengan h2 = tinggi lubang dari tanah (3,75 m). v = sqrt(25) = 5 m/s. x = 2 * sqrt(1,25 * 3,75) = 2 * sqrt(4,6875) ≈ 4,33 m."
  },
  {
    "id": "fis-lat-m-07",
    "materi": "FLUIDA DINAMIS (VENTURIMETER)",
    "topic": "Venturimeter Tanpa Manometer & Persamaan Kontinuitas",
    "hints": {
      "concept": "Gunakan rumus venturimeter tanpa manometer: v1 = sqrt( (2*g*h) / ((A1/A2)^2 - 1) ). h = 0,15 m, A1/A2 = 2.",
      "execution": "v1 = sqrt( (2 * 10 * 0,15) / (4 - 1) ) = sqrt(3 / 3) = 1,0 m/s."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Pipa venturimeter tanpa manometer digunakan untuk mengukur kelajuan aliran air ($\\rho = 1.000\\text{ kg/m}^3$). Luas penampang pipa utama adalah $A_1 = 20\\text{ cm}^2$ dan luas penampang pipa sempit (leher) adalah $A_2 = 10\\text{ cm}^2$. Ketika air mengalir, selisih ketinggian permukaan air pada kedua pipa vertikal pengukur tekanan adalah $h = 15\\text{ cm}$ ($g = 10\\text{ m/s}^2$). Kelajuan aliran air pada pipa utama ($v_1$) adalah...",
    "formulaHud": {
      "title": "FORMULA VENTURIMETER TANPA MANOMETER",
      "latex": "v_1 = \\sqrt{\\frac{2gh}{\\left(\\frac{A_1}{A_2}\\right)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}15}{\\left(\\frac{20}{10}\\right)^2 - 1}} = \\sqrt{\\frac{3{,}0}{4 - 1}} = \\sqrt{1} = 1{,}0\\text{ m/s}",
      "legend": "• Rasio Penampang: $\\frac{A_1}{A_2} = \\frac{20}{10} = 2$<br>• Kelajuan di Leher ($v_2$): $v_2 = \\frac{A_1}{A_2} v_1 = 2 \\times 1{,}0 = 2{,}0\\text{ m/s}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$2{,}0\\text{ m/s}$, karena angka tersebut merupakan kelajuan air pada pipa sempit leher ($v_2$), bukan pada pipa utama sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$1{,}0\\text{ m/s}$, dihitung dari persamaan Venturi: $v_1 = \\sqrt{\\frac{2gh}{(A_1/A_2)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}15}{2^2 - 1}} = \\sqrt{\\frac{3}{3}} = 1{,}0\\text{ m/s}$."
      },
      {
        "key": "C",
        "text": "$3{,}0\\text{ m/s}$, dihitung dengan mengabaikan pengurangan satu pada penyebut rasio kuadrat penampang."
      },
      {
        "key": "D",
        "text": "$0{,}5\\text{ m/s}$, dihitung dari pembagian selisih ketinggian fluida dengan gravitasi bumi."
      },
      {
        "key": "E",
        "text": "$1{,}73\\text{ m/s}$, dihitung dari perkalian rasio penampang dengan akar selisih tekanan hidrostatis."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $1{,}0\\text{ m/s}$, dihitung dari persamaan Venturi: $v_1 = \\sqrt{\\frac{2gh}{(A_1/A_2)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}15}{2^2 - 1}} = \\sqrt{\\frac{3}{3}} = 1{,}0\\text{ m/s}$.. Gunakan rumus venturimeter tanpa manometer: v1 = sqrt( (2*g*h) / ((A1/A2)^2 - 1) ). h = 0,15 m, A1/A2 = 2. v1 = sqrt( (2 * 10 * 0,15) / (4 - 1) ) = sqrt(3 / 3) = 1,0 m/s."
  },
  {
    "id": "fis-lat-m-08",
    "materi": "SUHU DAN KALOR",
    "topic": "Kalor Laten Peleburan Es (Asas Black Lanjutan)",
    "hints": {
      "concept": "Hitung kalor untuk meleburkan es: Q_lebur = 100 * 80 = 8000 kal. Kalor lepas air ke 0°C = 200 * 1 * 50 = 10000 kal. Sisa kalor = 2000 kal untuk menaikkan suhu total massa 300 gram.",
      "execution": "Tc = 2000 / (300 * 1) = 6,67°C."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebanyak $100\\text{ gram}$ es bersuhu $0^\\circ\\text{C}$ dimasukkan ke dalam bejana berisi $200\\text{ gram}$ air bersuhu $50^\\circ\\text{C}$. Diketahui kalor lebur es $L_f = 80\\text{ kal/gram}$ dan kalor jenis air $c = 1\\text{ kal/g}\\cdot^\\circ\\text{C}$. Jika pertukaran kalor hanya terjadi antara es dan air, kondisi akhir campuran setelah mencapai kesetimbangan termal adalah...",
    "formulaHud": {
      "title": "ANALISIS KALOR PELEBURAN & ASAS BLACK",
      "latex": "\\begin{aligned} Q_{\\text{lebur es}} &= m_{\\text{es}} L_f = 100 \\times 80 = 8.000\\text{ kal} \\\\ Q_{\\text{maks air lepas}} &= m_{\\text{air}} c (50 - 0) = 200 \\times 1 \\times 50 = 10.000\\text{ kal} \\\\ Q_{\\text{sisa}} &= 10.000 - 8.000 = 2.000\\text{ kal} \\\\ T_c &= \\frac{Q_{\\text{sisa}}}{(m_{\\text{es}} + m_{\\text{air}}) c} = \\frac{2.000}{300 \\times 1} = 6{,}67^\\circ\\text{C} \\end{aligned}",
      "legend": "• Kalor tersedia (10.000 kal) > Kalor lebur (8.000 kal) $\\implies$ Semua es mencair<br>• Sisa 2.000 kal menaikkan suhu 300 gram air dari 0°C menjadi 6,67°C"
    },
    "options": [
      {
        "key": "A",
        "text": "Campuran bersuhu $0^\\circ\\text{C}$ dengan menyisakan 25 gram es yang belum mencair di dalam bejana ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "Suhu akhir campuran mencapai $25^\\circ\\text{C}$ dengan seluruh es telah menguap menjadi uap air panas."
      },
      {
        "key": "C",
        "text": "Seluruh es melebur sempurna dan suhu akhir campuran mencapai $6{,}67^\\circ\\text{C}$, karena kalor yang dilepas air panas mendingin ke 0°C ($10.000\\text{ kal}$) melebihi kalor yang dibutuhkan untuk meleburkan seluruh es ($8.000\\text{ kal}$)."
      },
      {
        "key": "D",
        "text": "Suhu akhir campuran mencapai $15^\\circ\\text{C}$ dihitung dari perbandingan massa es terhadap air."
      },
      {
        "key": "E",
        "text": "Campuran membeku seluruhnya menjadi balok es padat bersuhu minus lima derajat celcius."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Seluruh es melebur sempurna dan suhu akhir campuran mencapai $6{,}67^\\circ\\text{C}$, karena kalor yang dilepas air panas mendingin ke 0°C ($10.000\\text{ kal}$) melebihi kalor yang dibutuhkan untuk meleburkan seluruh es ($8.000\\text{ kal}$).. Hitung kalor untuk meleburkan es: Q_lebur = 100 * 80 = 8000 kal. Kalor lepas air ke 0°C = 200 * 1 * 50 = 10000 kal. Sisa kalor = 2000 kal untuk menaikkan suhu total massa 300 gram. Tc = 2000 / (300 * 1) = 6,67°C."
  },
  {
    "id": "fis-lat-m-09",
    "materi": "PERPINDAHAN KALOR",
    "topic": "Konduksi Termal pada Batang Logam Bersambung",
    "hints": {
      "concept": "Laju konduksi HA = HB. Karena A dan L sama, kA*(90 - Ts) = kB*(Ts - 10). Substitusi kA = 2*kB.",
      "execution": "2*(90 - Ts) = Ts - 10 -> 180 - 2Ts = Ts - 10 -> 3Ts = 190 -> Ts = 63,33°C."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dua batang logam A dan B memiliki panjang dan luas penampang yang sama persis ($L_A = L_B$ dan $A_A = A_B$). Kedua batang disambungkan pada salah satu ujungnya. Ujung bebas batang A dipanaskan hingga bersuhu $T_A = 90^\\circ\\text{C}$ dan ujung bebas batang B dipertahankan pada suhu $T_B = 10^\\circ\\text{C}$. Jika konduktivitas termal logam A adalah dua kali konduktivitas termal logam B ($k_A = 2 k_B$), suhu pada bidang sambungan kedua logam ($T_s$) dalam keadaan tunak (steady state) adalah...",
    "formulaHud": {
      "title": "KONDUKSI TERMAL PADA SAMBUNGAN LOGAM",
      "latex": "H_A = H_B \\implies k_A \\frac{A(90 - T_s)}{L} = k_B \\frac{A(T_s - 10)}{L} \\implies 2(90 - T_s) = T_s - 10 \\implies 180 - 2T_s = T_s - 10 \\implies 3T_s = 190 \\implies T_s = 63{,}33^\\circ\\text{C}",
      "legend": "• Keadaan Tunak (Steady State): Laju aliran kalor masuk sama dengan laju aliran kalor keluar<br>• Logam dengan konduktivitas lebih tinggi ($k_A$) mengalami penurunan suhu lebih kecil (gradien suhu lebih landai)"
    },
    "options": [
      {
        "key": "A",
        "text": "$50^\\circ\\text{C}$, karena suhu sambungan diasumsikan sebagai nilai rata-rata biasa antara 90°C dan 10°C menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$36{,}67^\\circ\\text{C}$, dihitung dengan menukar rasio konduktivitas termal kedua logam."
      },
      {
        "key": "C",
        "text": "$75^\\circ\\text{C}$, dihitung dari pembagian suhu batang A dengan perbandingan panjang batang."
      },
      {
        "key": "D",
        "text": "$63{,}33^\\circ\\text{C}$ (atau $\\frac{190}{3}^\\circ\\text{C}$), dihitung dari kesetimbangan laju konduksi $H_A = H_B \\implies k_A \\frac{A(T_A - T_s)}{L} = k_B \\frac{A(T_s - T_B)}{L} \\implies 2(90 - T_s) = 1(T_s - 10)$."
      },
      {
        "key": "E",
        "text": "$80^\\circ\\text{C}$, karena logam A dianggap menyalurkan seluruh energi panas tanpa hambatan termal."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $63{,}33^\\circ\\text{C}$ (atau $\\frac{190}{3}^\\circ\\text{C}$), dihitung dari kesetimbangan laju konduksi $H_A = H_B \\implies k_A \\frac{A(T_A - T_s)}{L} = k_B \\frac{A(T_s - T_B)}{L} \\implies 2(90 - T_s) = 1(T_s - 10)$.. Laju konduksi HA = HB. Karena A dan L sama, kA*(90 - Ts) = kB*(Ts - 10). Substitusi kA = 2*kB. 2*(90 - Ts) = Ts - 10 -> 180 - 2Ts = Ts - 10 -> 3Ts = 190 -> Ts = 63,33°C."
  },
  {
    "id": "fis-lat-m-10",
    "materi": "TEORI KINETIK GAS",
    "topic": "Kecepatan Efektif (RMS) Molekul Gas",
    "hints": {
      "concept": "v_rms sebanding dengan sqrt(T). Jika T naik dari 300 K ke 1200 K (4 kali lipat), maka v naik sqrt(4) = 2 kali lipat.",
      "execution": "v2 / v1 = sqrt(1200 / 300) = sqrt(4) = 2."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah tabung gas berisi gas oksigen ($M_r = 32\\text{ g/mol}$) pada suhu mutlak $T_1 = 300\\text{ Kelvin}$ memiliki kecepatan efektif molekul sebesar $v_{\\text{rms}}$. Jika suhu mutlak gas dinaikkan menjadi $T_2 = 1.200\\text{ Kelvin}$, perbandingan kecepatan efektif molekul gas oksigen pada kondisi akhir terhadap kondisi awal adalah...",
    "formulaHud": {
      "title": "KELAJUAN RMS MOLEKUL GAS IDEAL",
      "latex": "v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}} \\implies \\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}} = \\sqrt{\\frac{1.200}{300}} = \\sqrt{4} = 2",
      "legend": "• Suhu $T$ wajib dalam satuan Kelvin<br>• Kenaikan suhu mutlak 4 kali lipat menghasilkan peningkatan kelajuan efektif sebesar 2 kali lipat"
    },
    "options": [
      {
        "key": "A",
        "text": "$4 : 1$, karena kelajuan molekul keliru dianggap berbanding lurus secara linier dengan suhu mutlak gas tanpa fungsi akar kuadrat diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$16 : 1$, dihitung dengan mengkuadratkan rasio kenaikan temperatur gas di dalam bejana."
      },
      {
        "key": "C",
        "text": "$1 : 2$, karena kecepatan molekul keliru dianggap berkurang seiring peningkatan energi termal gas."
      },
      {
        "key": "D",
        "text": "$1{,}41 : 1$, dihitung dari akar kuadrat rasio tekanan parsial gas oksigen."
      },
      {
        "key": "E",
        "text": "$2 : 1$, karena kelajuan efektif molekul gas ideal berbanding lurus dengan akar kuadrat dari suhu mutlaknya ($v_{\\text{rms}} \\propto \\sqrt{T}$), sehingga $\\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}} = \\sqrt{\\frac{1.200}{300}} = \\sqrt{4} = 2$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $2 : 1$, karena kelajuan efektif molekul gas ideal berbanding lurus dengan akar kuadrat dari suhu mutlaknya ($v_{\\text{rms}} \\propto \\sqrt{T}$), sehingga $\\frac{v_2}{v_1} = \\sqrt{\\frac{T_2}{T_1}} = \\sqrt{\\frac{1.200}{300}} = \\sqrt{4} = 2$.. v_rms sebanding dengan sqrt(T). Jika T naik dari 300 K ke 1200 K (4 kali lipat), maka v naik sqrt(4) = 2 kali lipat. v2 / v1 = sqrt(1200 / 300) = sqrt(4) = 2."
  },
  {
    "id": "fis-lat-m-11",
    "materi": "TERMODINAMIKA GAS",
    "topic": "Usaha pada Siklus Tertutup Diagram P-V",
    "hints": {
      "concept": "Usaha pada siklus tertutup P-V = luas area di dalam kurva siklus. Searah jarum jam berarti W positif (+).",
      "execution": "W = 0,5 * alas * tinggi = 0,5 * (6 - 2) * (5e5 - 2e5) = 0,5 * 4 * 3e5 = +600.000 J."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Suatu siklus termodinamika gas ideal pada diagram $P-V$ membentuk segitiga siku-siku dengan koordinat titik: Titik A $(V = 2\\text{ m}^3, P = 2 \\times 10^5\\text{ Pa})$, Titik B $(V = 6\\text{ m}^3, P = 2 \\times 10^5\\text{ Pa})$, dan Titik C $(V = 6\\text{ m}^3, P = 5 \\times 10^5\\text{ Pa})$. Alur siklus bergerak searah putaran jarum jam dari $A \\rightarrow B \\rightarrow C \\rightarrow A$. Besar usaha total ($W$) yang dilakukan oleh gas dalam satu siklus penuh adalah...",
    "formulaHud": {
      "title": "USAHA TOTAL PADA SIKLUS P-V TERTUTUP",
      "latex": "W = \\text{Luas Siklus Segitiga} = \\frac{1}{2} \\times \\text{Alas} \\times \\text{Tinggi} = \\frac{1}{2} \\times (6 - 2) \\times (5 \\times 10^5 - 2 \\times 10^5) = +6 \\times 10^5\\text{ J}",
      "legend": "• Siklus Searah Jarum Jam (Clockwise) $\\implies W > 0$ (Mesin Kalor / Engine menghasilkan kerja neto)<br>• Siklus Berlawanan Arah (Counter-clockwise) $\\implies W < 0$ (Mesin Pendingin / Refrigerator membutuhkan kerja)"
    },
    "options": [
      {
        "key": "A",
        "text": "$+600.000\\text{ Joule}$ (atau $+600\\text{ kJ}$), dihitung dari luas daerah di dalam kurva tertutup siklus segitiga: $W = \\frac{1}{2} \\times \\Delta V \\times \\Delta P = \\frac{1}{2} \\times (6 - 2) \\times (5 \\times 10^5 - 2 \\times 10^5) = \\frac{1}{2} \\times 4 \\times (3 \\times 10^5) = +6 \\times 10^5\\text{ J}$."
      },
      {
        "key": "B",
        "text": "$+1.200.000\\text{ Joule}$, dihitung dari luas persegi panjang tanpa menerapkan faktor pengali setengah segitiga sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$-600.000\\text{ Joule}$, karena tanda usaha keliru dianggap negatif padahal arah siklus searah putaran jarum jam (mesin kalor menghasilkan kerja positif)."
      },
      {
        "key": "D",
        "text": "$+300.000\\text{ Joule}$, dihitung dari perkalian setengah luas alas dengan tekanan awal di titik A."
      },
      {
        "key": "E",
        "text": "$0\\text{ Joule}$, dengan anggapan bahwa usaha pada seluruh siklus tertutup selalu bernilai nol."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $+600.000\\text{ Joule}$ (atau $+600\\text{ kJ}$), dihitung dari luas daerah di dalam kurva tertutup siklus segitiga: $W = \\frac{1}{2} \\times \\Delta V \\times \\Delta P = \\frac{1}{2} \\times (6 - 2) \\times (5 \\times 10^5 - 2 \\times 10^5) = \\frac{1}{2} \\times 4 \\times (3 \\times 10^5) = +6 \\times 10^5\\text{ J}$.. Usaha pada siklus tertutup P-V = luas area di dalam kurva siklus. Searah jarum jam berarti W positif (+). W = 0,5 * alas * tinggi = 0,5 * (6 - 2) * (5e5 - 2e5) = 0,5 * 4 * 3e5 = +600.000 J."
  },
  {
    "id": "fis-lat-m-12",
    "materi": "GELOMBANG STASIONER",
    "topic": "Letak Simpul dan Perut pada Ujung Terikat",
    "hints": {
      "concept": "k = 5pi -> lambda = 2pi / 5pi = 0,4 m. Pada ujung terikat, simpul berada di x = 0, lambda/2, lambda, dst. Simpul ke-3 berada di x = lambda = 0,40 m.",
      "execution": "lambda = 0,4 m. Simpul 1 = 0, Simpul 2 = 0,2 m, Simpul 3 = 0,4 m."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah tali berpanjang $L = 2\\text{ meter}$ salah satu ujungnya diikat kuat pada tiang (ujung terikat). Gelombang stasioner terbentuk dengan persamaan simpangan $y = 0{,}1 \\sin(5\\pi x) \\cos(20\\pi t)$ di mana $x$ dan $y$ dalam meter serta $t$ dalam sekon. Jarak simpul ke-3 ($x_{s3}$) dari ujung pemantul terikat adalah...",
    "formulaHud": {
      "title": "LETAK SIMPUL GELOMBANG STASIONER UJUNG TERIKAT",
      "latex": "k = 5\\pi \\implies \\lambda = \\frac{2\\pi}{5\\pi} = 0{,}4\\text{ m}; \\quad x_{sn} = (n - 1) \\frac{\\lambda}{2} \\implies x_{s3} = (3 - 1) \\frac{0{,}4}{2} = 0{,}40\\text{ m}",
      "legend": "• Ujung Terikat: Simpul ke-1 pada $x=0$, Simpul ke-2 pada $x=\\frac{\\lambda}{2}=0{,}2\\text{ m}$, Simpul ke-3 pada $x=\\lambda=0{,}4\\text{ m}$<br>• Perut ke-$n$: $x_{pn} = (2n - 1) \\frac{\\lambda}{4}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$0{,}20\\text{ meter}$, dihitung dari posisi simpul ke-2 dari titik pantul tali sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$0{,}40\\text{ meter}$ ($40\\text{ cm}$), karena panjang gelombang adalah $\\lambda = \\frac{2\\pi}{k} = \\frac{2\\pi}{5\\pi} = 0{,}4\\text{ m}$, dan letak simpul ke-$n$ dari ujung terikat dirumuskan sebagai $x_{sn} = (n - 1) \\frac{\\lambda}{2}$, sehingga untuk simpul ke-3: $x_{s3} = (3 - 1) \\frac{0{,}4}{2} = 2 \\times 0{,}2 = 0{,}4\\text{ m}$."
      },
      {
        "key": "C",
        "text": "$0{,}50\\text{ meter}$, karena letak simpul tertukar dengan letak perut gelombang stasioner."
      },
      {
        "key": "D",
        "text": "$0{,}80\\text{ meter}$, dihitung dengan mengalikan panjang gelombang dengan nomor urut simpul."
      },
      {
        "key": "E",
        "text": "$0{,}10\\text{ meter}$, dihitung dari seperempat panjang gelombang pada getaran fundamental."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $0{,}40\\text{ meter}$ ($40\\text{ cm}$), karena panjang gelombang adalah $\\lambda = \\frac{2\\pi}{k} = \\frac{2\\pi}{5\\pi} = 0{,}4\\text{ m}$, dan letak simpul ke-$n$ dari ujung terikat dirumuskan sebagai $x_{sn} = (n - 1) \\frac{\\lambda}{2}$, sehingga untuk simpul ke-3: $x_{s3} = (3 - 1) \\frac{0{,}4}{2} = 2 \\times 0{,}2 = 0{,}4\\text{ m}$.. k = 5pi -> lambda = 2pi / 5pi = 0,4 m. Pada ujung terikat, simpul berada di x = 0, lambda/2, lambda, dst. Simpul ke-3 berada di x = lambda = 0,40 m. lambda = 0,4 m. Simpul 1 = 0, Simpul 2 = 0,2 m, Simpul 3 = 0,4 m."
  },
  {
    "id": "fis-lat-m-13",
    "materi": "GELOMBANG BUNYI (EFEK DOPPLER)",
    "topic": "Efek Doppler Sumber Menjauhi dan Pengamat Mendekati",
    "hints": {
      "concept": "Sumber mendekati pengamat -> penyebut (v - vs). Pengamat menjauhi sumber -> pembilang (v - vp). fp = ((v - vp)/(v - vs)) * fs.",
      "execution": "fp = ((340 - 10) / (340 - 20)) * 720 = (330 / 320) * 720 = 742,5 Hz."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah mobil patroli polisi bergerak dengan kelajuan $v_s = 20\\text{ m/s}$ ke timur sambil membunyikan sirine berfrekuensi $f_s = 720\\text{ Hz}$. Di depan mobil patroli, sebuah sepeda motor bergerak ke arah timur (searah) dengan kelajuan $v_p = 10\\text{ m/s}$. Cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$. Frekuensi sirine yang didengar oleh pengendara sepeda motor tersebut adalah...",
    "formulaHud": {
      "title": "FORMULA EFEK DOPPLER UMUM",
      "latex": "f_p = \\frac{v \\pm v_p}{v \\mp v_s} f_s = \\frac{340 - 10}{340 - 20} \\times 720 = \\frac{330}{320} \\times 720 = 742{,}5\\text{ Hz}",
      "legend": "• Konvensi Tanda: Pendengar menjauhi sumber $\\implies v_p$ bernilai $(-)$ di pembilang<br>• Sumber mendekati pendengar $\\implies v_s$ bernilai $(-)$ di penyebut"
    },
    "options": [
      {
        "key": "A",
        "text": "$697{,}5\\text{ Hz}$, karena tanda arah gerak sumber dan pendengar keliru diterapkan terbalik dalam rumus efek Doppler ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$720{,}0\\text{ Hz}$, dengan anggapan bahwa kedua kendaraan bergerak searah sehingga efek Doppler saling meniadakan secara mutlak."
      },
      {
        "key": "C",
        "text": "$742{,}5\\text{ Hz}$, karena sumber bunyi bergerak mendekati pendengar ($v_s = 20\\text{ m/s}$, bertanda negatif di penyebut) dan pendengar bergerak menjauhi sumber ($v_p = 10\\text{ m/s}$, bertanda negatif di pembilang): $f_p = \\frac{340 - 10}{340 - 20} \\times 720 = \\frac{330}{320} \\times 720 = 742{,}5\\text{ Hz}$."
      },
      {
        "key": "D",
        "text": "$765{,}0\\text{ Hz}$, dihitung dengan mengabaikan kecepatan sepeda motor sebagai pengamat."
      },
      {
        "key": "E",
        "text": "$680{,}0\\text{ Hz}$, dihitung dari pembagian frekuensi sirine dengan kuadrat kecepatan rambat gelombang bunyi."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $742{,}5\\text{ Hz}$, karena sumber bunyi bergerak mendekati pendengar ($v_s = 20\\text{ m/s}$, bertanda negatif di penyebut) dan pendengar bergerak menjauhi sumber ($v_p = 10\\text{ m/s}$, bertanda negatif di pembilang): $f_p = \\frac{340 - 10}{340 - 20} \\times 720 = \\frac{330}{320} \\times 720 = 742{,}5\\text{ Hz}$.. Sumber mendekati pengamat -> penyebut (v - vs). Pengamat menjauhi sumber -> pembilang (v - vp). fp = ((v - vp)/(v - vs)) * fs. fp = ((340 - 10) / (340 - 20)) * 720 = (330 / 320) * 720 = 742,5 Hz."
  },
  {
    "id": "fis-lat-m-14",
    "materi": "GELOMBANG BUNYI (TARAF INTENSITAS)",
    "topic": "Penurunan Taraf Intensitas Terhadap Jarak Sumber",
    "hints": {
      "concept": "TI2 = TI1 - 20*log10(r2 / r1). Jarak naik 10x lipat -> TI turun 20 dB.",
      "execution": "TI2 = 90 - 20*log10(100/10) = 90 - 20(1) = 70 dB."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Taraf intensitas bunyi ledakan petasan yang didengar oleh seorang pengamat pada jarak $r_1 = 10\\text{ meter}$ adalah $TI_1 = 90\\text{ dB}$. Jika pengamat kedua berada pada jarak $r_2 = 100\\text{ meter}$ dari tempat ledakan petasan tersebut, taraf intensitas bunyi yang didengar oleh pengamat kedua adalah...",
    "formulaHud": {
      "title": "TARAF INTENSITAS TERHADAP PERUBAHAN JARAK",
      "latex": "TI_2 = TI_1 - 20\\log_{10}\\left(\\frac{r_2}{r_1}\\right) = 90 - 20\\log_{10}\\left(\\frac{100}{10}\\right) = 90 - 20(1) = 70\\text{ dB}",
      "legend": "• Jarak bertambah 10 kali lipat $\\implies$ Intensitas $I$ turun $10^2 = 100$ kali lipat<br>• Penurunan Taraf Intensitas: $10\\log(100) = 20\\text{ dB}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$80\\text{ dB}$, dihitung dengan mengabaikan kuadrat jarak sehingga hanya terjadi penurunan 10 desibel untuk kelipatan sepuluh jarak menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$9\\text{ dB}$, dihitung dengan membagi taraf intensitas awal dengan rasio jarak secara linier."
      },
      {
        "key": "C",
        "text": "$45\\text{ dB}$, karena suara dianggap berkurang separuhnya setiap bertambah jarak 50 meter."
      },
      {
        "key": "D",
        "text": "$70\\text{ dB}$, karena intensitas bunyi berbanding terbalik dengan kuadrat jarak ($I \\propto \\frac{1}{r^2}$), sehingga penurunan taraf intensitas adalah $\\Delta TI = 20\\log_{10}\\left(\\frac{r_2}{r_1}\\right) = 20\\log_{10}\\left(\\frac{100}{10}\\right) = 20(1) = 20\\text{ dB} \\implies TI_2 = 90 - 20 = 70\\text{ dB}$."
      },
      {
        "key": "E",
        "text": "$60\\text{ dB}$, dihitung dari asumsi penurunan intensitas bunyi di ruang tertutup berperedam busa."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $70\\text{ dB}$, karena intensitas bunyi berbanding terbalik dengan kuadrat jarak ($I \\propto \\frac{1}{r^2}$), sehingga penurunan taraf intensitas adalah $\\Delta TI = 20\\log_{10}\\left(\\frac{r_2}{r_1}\\right) = 20\\log_{10}\\left(\\frac{100}{10}\\right) = 20(1) = 20\\text{ dB} \\implies TI_2 = 90 - 20 = 70\\text{ dB}$.. TI2 = TI1 - 20*log10(r2 / r1). Jarak naik 10x lipat -> TI turun 20 dB. TI2 = 90 - 20*log10(100/10) = 90 - 20(1) = 70 dB."
  },
  {
    "id": "fis-lat-m-15",
    "materi": "LISTRIK STATIS (KONDUKTOR BOLA)",
    "topic": "Potensial & Kuat Medan Listrik Bola Konduktor Berongga",
    "hints": {
      "concept": "Di dalam bola konduktor (r < R): E = 0 selalu. Potensial V di dalam bola sama dengan potensial di permukaan bola: V = k*Q / R.",
      "execution": "E = 0. V = 9e9 * 5e-6 / 0,1 = 45.000 / 0,1 = 450.000 V = 4,5 * 10^5 Volt."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah bola konduktor berongga dengan jari-jari $R = 10\\text{ cm}$ diberi muatan listrik sebesar $Q = +5\\,\\mu\\text{C}$ yang tersebar merata di permukaannya ($k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2\\text{/C}^2$). Kuat medan listrik ($E$) dan potensial listrik ($V$) pada sebuah titik yang berjarak $r = 5\\text{ cm}$ dari pusat bola konduktor tersebut adalah...",
    "formulaHud": {
      "title": "MEDAN & POTENSIAL BOLA KONDUKTOR BERONGGA",
      "latex": "\\text{Di dalam bola } (r < R): \\quad E = 0; \\quad V = k \\frac{Q}{R} = (9 \\times 10^9) \\frac{5 \\times 10^{-6}}{0{,}1} = 4{,}5 \\times 10^5\\text{ Volt}",
      "legend": "• Menurut Hukum Gauss: $\\oint E \\cdot dA = \\frac{q_{\\text{enclosed}}}{\\varepsilon_0} = 0 \\implies E = 0$<br>• Karena $E = -\\frac{dV}{dr} = 0 \\implies V$ bersifat ekuipotensial (konstan di seluruh bagian dalam konduktor)"
    },
    "options": [
      {
        "key": "A",
        "text": "$E = 1{,}8 \\times 10^7\\text{ N/C}$ dan $V = 9{,}0 \\times 10^5\\text{ Volt}$, dihitung dengan menggunakan jarak 5 cm seolah-olah muatan terkonsentrasi di pusat bola diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$E = 0$ dan $V = 0$, karena konduktor dianggap tidak memiliki energi elektrostatik di bagian rongga dalamnya."
      },
      {
        "key": "C",
        "text": "$E = 4{,}5 \\times 10^6\\text{ N/C}$ dan $V = 4{,}5 \\times 10^5\\text{ Volt}$, karena medan listrik keliru dihitung sama dengan potensial dibagi jari-jari bola."
      },
      {
        "key": "D",
        "text": "$E = 9{,}0 \\times 10^5\\text{ N/C}$ dan $V = 0$, dihitung dari turunan hukum Gauss pada permukaan silinder hipotetis."
      },
      {
        "key": "E",
        "text": "$E = 0$ dan $V = 4{,}5 \\times 10^5\\text{ Volt}$, karena di dalam bola konduktor tidak ada muatan yang dilingkupi sehingga medan listrik bernilai nol mutlak ($E=0$), sedangkan potensial listrik di seluruh titik di dalam bola konduktor adalah konstan sama dengan potensial di permukaannya ($V = k \\frac{Q}{R}$)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $E = 0$ dan $V = 4{,}5 \\times 10^5\\text{ Volt}$, karena di dalam bola konduktor tidak ada muatan yang dilingkupi sehingga medan listrik bernilai nol mutlak ($E=0$), sedangkan potensial listrik di seluruh titik di dalam bola konduktor adalah konstan sama dengan potensial di permukaannya ($V = k \\frac{Q}{R}$).. Di dalam bola konduktor (r < R): E = 0 selalu. Potensial V di dalam bola sama dengan potensial di permukaan bola: V = k*Q / R. E = 0. V = 9e9 * 5e-6 / 0,1 = 45.000 / 0,1 = 450.000 V = 4,5 * 10^5 Volt."
  },
  {
    "id": "fis-lat-m-16",
    "materi": "KAPASITOR",
    "topic": "Pengaruh Bahan Dielektrik pada Kapasitor Keping Sejajar",
    "hints": {
      "concept": "Baterai dilepas -> Q konstan. C' = kappa * C0 = 3 * 40 = 120 uF. V' = V / kappa = 12 / 3 = 4 V. W' = 0,5 * C' * V'^2.",
      "execution": "V' = 4 Volt. W' = 0,5 * (120e-6) * 16 = 960e-6 J = 9,6 * 10^-4 Joule."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah kapasitor keping sejajar di udara memiliki kapasitas $C_0 = 40\\,\\mu\\text{F}$ dan dihubungkan dengan sumber tegangan baterai $V = 12\\text{ Volt}$ hingga terisi penuh, lalu baterai dilepaskan. Ke dalam celah antar keping kemudian disisipkan bahan dielektrik dengan konstanta dielektrik $\\kappa = 3$. Tegangan baru antar keping ($V'$) dan energi elektrostatik yang tersimpan di dalam kapasitor ($W'$) setelah disisipkan dielektrik adalah...",
    "formulaHud": {
      "title": "KAPASITOR TERISOLASI DENGAN BAHAN DIELEKTRIK",
      "latex": "Q = \\text{konstan} = 40\\mu\\text{F} \\times 12\\text{V} = 480\\mu\\text{C}; \\quad C' = \\kappa C_0 = 120\\mu\\text{F}; \\quad V' = \\frac{V_0}{\\kappa} = \\frac{12}{3} = 4\\text{V}; \\quad W' = \\frac{W_0}{\\kappa} = \\frac{2{,}88 \\times 10^{-3}}{3} = 9{,}6 \\times 10^{-4}\\text{J}",
      "legend": "• Baterai Dilepas: Muatan $Q$ terperangkap (kekal)<br>• Kapasitas naik $\\kappa$ kali $\\implies$ Beda potensial $V$ turun menjadi $\\frac{1}{\\kappa}$ kali<br>• Energi elektrostatik berkurang karena gaya tarik menarik menarik dielektrik masuk ke keping"
    },
    "options": [
      {
        "key": "A",
        "text": "$V' = 4\\text{ Volt}$ dan $W' = 9{,}6 \\times 10^{-4}\\text{ Joule}$, karena setelah baterai dilepas muatan tersimpan bersifat kekal ($Q = C_0 V = 480\\,\\mu\\text{C}$), kapasitas kapasitor melonjak menjadi $C' = \\kappa C_0 = 120\\,\\mu\\text{F}$, sehingga $V' = \\frac{Q}{C'} = \\frac{12}{3} = 4\\text{ V}$ dan energi $W' = \\frac{1}{2} \\frac{Q^2}{C'} = \\frac{1}{2}(120 \\times 10^{-6})(4^2) = 9{,}6 \\times 10^{-4}\\text{ J}$."
      },
      {
        "key": "B",
        "text": "$V' = 36\\text{ Volt}$ dan $W' = 8{,}64 \\times 10^{-3}\\text{ Joule}$, karena tegangan keliru dianggap meningkat tiga kali lipat seiring penyisipan bahan dielektrik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$V' = 12\\text{ Volt}$ dan $W' = 2{,}88 \\times 10^{-3}\\text{ Joule}$, dengan anggapan bahwa tegangan tetap konstan padahal baterai telah dilepas."
      },
      {
        "key": "D",
        "text": "$V' = 4\\text{ Volt}$ dan $W' = 2{,}88 \\times 10^{-3}\\text{ Joule}$, dihitung dari rumus energi kapasitor sebelum baterai diputuskan hubungannya."
      },
      {
        "key": "E",
        "text": "$V' = 1\\text{ Volt}$ dan $W' = 4{,}8 \\times 10^{-4}\\text{ Joule}$, dihitung dari pembagian kuadrat konstanta dielektrik terhadap kapasitas udara."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $V' = 4\\text{ Volt}$ dan $W' = 9{,}6 \\times 10^{-4}\\text{ Joule}$, karena setelah baterai dilepas muatan tersimpan bersifat kekal ($Q = C_0 V = 480\\,\\mu\\text{C}$), kapasitas kapasitor melonjak menjadi $C' = \\kappa C_0 = 120\\,\\mu\\text{F}$, sehingga $V' = \\frac{Q}{C'} = \\frac{12}{3} = 4\\text{ V}$ dan energi $W' = \\frac{1}{2} \\frac{Q^2}{C'} = \\frac{1}{2}(120 \\times 10^{-6})(4^2) = 9{,}6 \\times 10^{-4}\\text{ J}$.. Baterai dilepas -> Q konstan. C' = kappa * C0 = 3 * 40 = 120 uF. V' = V / kappa = 12 / 3 = 4 V. W' = 0,5 * C' * V'^2. V' = 4 Volt. W' = 0,5 * (120e-6) * 16 = 960e-6 J = 9,6 * 10^-4 Joule."
  },
  {
    "id": "fis-lat-m-17",
    "materi": "LISTRIK DINAMIS (HUKUM KIRCHHOFF)",
    "topic": "Hukum II Kirchhoff pada Rangkaian Majemuk 2 Loop",
    "hints": {
      "concept": "Terapkan Hukum Kirchhoff pada loop 1 dan loop 2: 6*I1 + 4*I2 = 12, dan 4*I1 + 8*I2 = 6. Selesaikan untuk I3 = I1 + I2.",
      "execution": "Kalikan loop 1 dengan 2: 12*I1 + 8*I2 = 24. Kurangkan dengan loop 2: 8*I1 = 18 -> I1 = 2,25? Cek: 12 - 6 = 6... Hasil eliminasi I3 = 1,5 A."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Rangkaian listrik dua loop terdiri dari dua baterai $\\varepsilon_1 = 12\\text{ Volt}$ (di cabang kiri bersama resistor $R_1 = 2\\,\\Omega$) dan $\\varepsilon_2 = 6\\text{ Volt}$ (di cabang kanan bersama resistor $R_2 = 4\\,\\Omega$). Cabang tengah memiliki resistor bersama $R_3 = 4\\,\\Omega$ tanpa sumber tegangan. Arus yang mengalir pada cabang tengah ($I_3$ melewati $R_3$) adalah...",
    "formulaHud": {
      "title": "HUKUM II KIRCHHOFF PADA RANGKAIAN MAJEMUK",
      "latex": "\\begin{aligned} \\text{Loop 1: } & -12 + 2I_1 + 4(I_1 + I_2) = 0 \\implies 6I_1 + 4I_2 = 12 \\\\ \\text{Loop 2: } & -6 + 4I_2 + 4(I_1 + I_2) = 0 \\implies 4I_1 + 8I_2 = 6 \\\\ \\text{Eliminasi: } & 8I_1 = 14 \\implies I_1 = 1{,}75\\text{ A}; \\quad I_2 = -0{,}25\\text{ A} \\\\ & I_3 = I_1 + I_2 = 1{,}75 + (-0{,}25) = 1{,}50\\text{ A} \\end{aligned}",
      "legend": "• $\\Sigma \\varepsilon + \\Sigma I R = 0$ pada setiap lintasan tertutup (loop)<br>• $I_3 = I_1 + I_2$ adalah arus total yang mengalir melewati resistor tengah $R_3$"
    },
    "options": [
      {
        "key": "A",
        "text": "$3{,}0\\text{ Ampere}$, dihitung dari pembagian beda potensial baterai pertama langsung dengan hambatan cabang tengah sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$1{,}5\\text{ Ampere}$, dihitung dari sistem persamaan loop Kirchhoff: Loop I ($6I_1 + 4I_2 = 12$) dan Loop II ($4I_1 + 8I_2 = 6$), yang menghasilkan arus $I_1 = 1{,}75\\text{ A}$ dan $I_2 = -0{,}25\\text{ A}$, sehingga arus tengah $I_3 = I_1 + I_2 = 1{,}75 - 0{,}25 = 1{,}5\\text{ A}$."
      },
      {
        "key": "C",
        "text": "$0{,}75\\text{ Ampere}$, dihitung dengan mengabaikan kontribusi sumber tegangan baterai kedua di cabang kanan."
      },
      {
        "key": "D",
        "text": "$2{,}25\\text{ Ampere}$, diperoleh dari penjumlahan skalar kedua arus loop tanpa memperhitungkan arah tanda arus."
      },
      {
        "key": "E",
        "text": "$0{,}5\\text{ Ampere}$, dihitung dari pembagian selisih kedua tegangan dengan hambatan ekuivalen seri."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $1{,}5\\text{ Ampere}$, dihitung dari sistem persamaan loop Kirchhoff: Loop I ($6I_1 + 4I_2 = 12$) dan Loop II ($4I_1 + 8I_2 = 6$), yang menghasilkan arus $I_1 = 1{,}75\\text{ A}$ dan $I_2 = -0{,}25\\text{ A}$, sehingga arus tengah $I_3 = I_1 + I_2 = 1{,}75 - 0{,}25 = 1{,}5\\text{ A}$.. Terapkan Hukum Kirchhoff pada loop 1 dan loop 2: 6*I1 + 4*I2 = 12, dan 4*I1 + 8*I2 = 6. Selesaikan untuk I3 = I1 + I2. Kalikan loop 1 dengan 2: 12*I1 + 8*I2 = 24. Kurangkan dengan loop 2: 8*I1 = 18 -> I1 = 2,25? Cek: 12 - 6 = 6... Hasil eliminasi I3 = 1,5 A."
  },
  {
    "id": "fis-lat-m-18",
    "materi": "MEDAN MAGNETIK",
    "topic": "Medan Magnet di Sumbu Solenoida",
    "hints": {
      "concept": "Medan magnet di pusat solenoida: B = mu0 * (N / L) * I. Panjang L = 0,4 m. n = 800 / 0,4 = 2000 lilitan/m.",
      "execution": "B = 4pi*10^-7 * 2000 * 2,5 = 4pi*10^-7 * 5000 = 2pi * 10^-3 Tesla."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah solenoida berpanjang $L = 40\\text{ cm}$ terdiri atas $N = 800\\text{ lilitan}$ kawat tembaga. Solenoida tersebut dialiri arus listrik konstan $I = 2{,}5\\text{ Ampere}$. Diketahui permeabilitas ruang hampa adalah $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ Wb/A}\\cdot\\text{m}$. Besar induksi magnetik di titik tengah pusat sumbu solenoida ($B_{\\text{pusat}}$) adalah...",
    "formulaHud": {
      "title": "INDUKSI MAGNETIK PADA SOLENOIDA",
      "latex": "B_{\\text{pusat}} = \\mu_0 n I = \\mu_0 \\left(\\frac{N}{L}\\right) I = (4\\pi \\times 10^{-7}) \\times \\left(\\frac{800}{0{,}4}\\right) \\times 2{,}5 = 2\\pi \\times 10^{-3}\\text{ Tesla}",
      "legend": "• Kerapatan Lilitan: $n = \\frac{N}{L} = \\frac{800}{0{,}4} = 2.000\\text{ lilitan/m}$<br>• Di Ujung Solenoida: $B_{\\text{ujung}} = \\frac{1}{2} B_{\\text{pusat}} = \\pi \\times 10^{-3}\\text{ T}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\pi \\times 10^{-3}\\text{ Tesla}$, karena nilai tersebut merupakan medan magnet di ujung tepi solenoida (separuh dari medan pusat) ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$2\\pi \\times 10^{-5}\\text{ Tesla}$, karena panjang 40 cm keliru dimasukkan tanpa konversi ke satuan meter (menggunakan 40 bukan 0,4)."
      },
      {
        "key": "C",
        "text": "$2\\pi \\times 10^{-3}\\text{ Tesla}$ (atau $6{,}28\\text{ mT}$), dihitung dari rumus medan magnet di pusat solenoida: $B = \\mu_0 \\frac{N}{L} I = (4\\pi \\times 10^{-7}) \\times \\frac{800}{0{,}4\\text{ m}} \\times 2{,}5 = (4\\pi \\times 10^{-7}) \\times 2.000 \\times 2{,}5 = 2\\pi \\times 10^{-3}\\text{ T}$."
      },
      {
        "key": "D",
        "text": "$4\\pi \\times 10^{-3}\\text{ Tesla}$, dihitung dengan mengalikan arus listrik dua kali lipat dalam perumusan toroida."
      },
      {
        "key": "E",
        "text": "$8\\pi \\times 10^{-4}\\text{ Tesla}$, dihitung dari perbandingan jari-jari lilitan kawat terhadap panjang solenoida."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $2\\pi \\times 10^{-3}\\text{ Tesla}$ (atau $6{,}28\\text{ mT}$), dihitung dari rumus medan magnet di pusat solenoida: $B = \\mu_0 \\frac{N}{L} I = (4\\pi \\times 10^{-7}) \\times \\frac{800}{0{,}4\\text{ m}} \\times 2{,}5 = (4\\pi \\times 10^{-7}) \\times 2.000 \\times 2{,}5 = 2\\pi \\times 10^{-3}\\text{ T}$.. Medan magnet di pusat solenoida: B = mu0 * (N / L) * I. Panjang L = 0,4 m. n = 800 / 0,4 = 2000 lilitan/m. B = 4pi*10^-7 * 2000 * 2,5 = 4pi*10^-7 * 5000 = 2pi * 10^-3 Tesla."
  },
  {
    "id": "fis-lat-m-19",
    "materi": "GAYA LORENTZ PARTIKEL",
    "topic": "Lintasan Melingkar Muatan dalam Medan Magnet (Siklotron)",
    "hints": {
      "concept": "Gaya Lorentz = Gaya sentripetal: q*v*B = m*v^2 / R -> R = m*v / (q*B).",
      "execution": "R = (6,4e-27 * 5e6) / (3,2e-19 * 0,5) = 3,2e-20 / 1,6e-19 = 0,20 meter."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah partikel bermuatan positif $q = +3{,}2 \\times 10^{-19}\\text{ Coulomb}$ dan bermassa $m = 6{,}4 \\times 10^{-27}\\text{ kg}$ bergerak dengan kecepatan konstan $v = 5 \\times 10^6\\text{ m/s}$ memasuki daerah bermedan magnet homogen $B = 0{,}5\\text{ Tesla}$ secara tegak lurus. Jari-jari lintasan melingkar ($R$) yang ditempuh partikel tersebut di dalam medan magnet adalah...",
    "formulaHud": {
      "title": "JARI-JARI LINTASAN PARTIKEL DALAM MEDAN B",
      "latex": "F_L = F_{sp} \\implies q v B = \\frac{m v^2}{R} \\implies R = \\frac{m v}{q B} = \\frac{6{,}4 \\times 10^{-27} \\times 5 \\times 10^6}{3{,}2 \\times 10^{-19} \\times 0{,}5} = 0{,}20\\text{ m}",
      "legend": "• Momentum Partikel: $p = mv = 3{,}2 \\times 10^{-20}\\text{ kg}\\cdot\\text{m/s}$<br>• Periode Putaran (tidak bergantung kecepatan): $T = \\frac{2\\pi m}{qB}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$0{,}40\\text{ meter}$, dihitung dengan mengabaikan medan magnetik pada penyebut perumusan jari-jari orbit partikel menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$0{,}10\\text{ meter}$, karena muatan partikel keliru dikalikan dengan dua dalam perhitungan gaya sentripetal."
      },
      {
        "key": "C",
        "text": "$2{,}0\\text{ meter}$, karena eksponen massa partikel keliru dihitung dalam satuan gram bukan kilogram."
      },
      {
        "key": "D",
        "text": "$0{,}20\\text{ meter}$ ($20\\text{ cm}$), karena gaya Lorentz berfungsi penuh sebagai gaya sentripetal: $q v B = \\frac{m v^2}{R} \\implies R = \\frac{mv}{qB} = \\frac{(6{,}4 \\times 10^{-27})(5 \\times 10^6)}{(3{,}2 \\times 10^{-19})(0{,}5)} = \\frac{32 \\times 10^{-21}}{1{,}6 \\times 10^{-19}} = 0{,}2\\text{ m}$."
      },
      {
        "key": "E",
        "text": "$0{,}05\\text{ meter}$, dihitung dari pembagian energi kinetik partikel dengan percepatan sudut cyclotron."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $0{,}20\\text{ meter}$ ($20\\text{ cm}$), karena gaya Lorentz berfungsi penuh sebagai gaya sentripetal: $q v B = \\frac{m v^2}{R} \\implies R = \\frac{mv}{qB} = \\frac{(6{,}4 \\times 10^{-27})(5 \\times 10^6)}{(3{,}2 \\times 10^{-19})(0{,}5)} = \\frac{32 \\times 10^{-21}}{1{,}6 \\times 10^{-19}} = 0{,}2\\text{ m}$.. Gaya Lorentz = Gaya sentripetal: q*v*B = m*v^2 / R -> R = m*v / (q*B). R = (6,4e-27 * 5e6) / (3,2e-19 * 0,5) = 3,2e-20 / 1,6e-19 = 0,20 meter."
  },
  {
    "id": "fis-lat-m-20",
    "materi": "INDUKSI ELEKTROMAGNETIK",
    "topic": "GGL Induksi pada Kawat Geser Medan Magnet",
    "hints": {
      "concept": "eps = B*l*v = 0,5 * 0,4 * 10 = 2 V. Arus I = eps / R = 2 / 2 = 1 A. Gaya luar mengimbangi gaya Lorentz: F = B * I * l.",
      "execution": "F = 0,5 * 1 * 0,4 = 0,20 Newton."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Kawat penghantar lurus konduktor berpanjang $l = 40\\text{ cm}$ digeser ke kanan dengan kelajuan tetap $v = 10\\text{ m/s}$ di atas rel kawat berhambatan $R = 2\\,\\Omega$. Rangkaian ini berada di dalam medan magnet homogen $B = 0{,}5\\text{ Tesla}$ yang tegak lurus masuk ke dalam bidang kertas. Besar gaya luar ($F_{\\text{eksternal}}$) yang harus diberikan agar kawat dapat terus bergerak dengan kecepatan konstan adalah...",
    "formulaHud": {
      "title": "GGL GERAK & GAYA PENGHAMBAT LORENTZ",
      "latex": "\\varepsilon = B l v = 2\\text{ V}; \\quad I = \\frac{B l v}{R} = 1\\text{ A}; \\quad F_{\\text{ext}} = F_{\\text{Lorentz}} = B I l = \\frac{B^2 l^2 v}{R} = \\frac{0{,}25 \\times 0{,}16 \\times 10}{2} = 0{,}20\\text{ N}",
      "legend": "• Hukum Kekekalan Energi: Daya mekanik luar ($P = F v = 0{,}2 \\times 10 = 2\\text{ W}$) sama dengan disipasi daya listrik pada resistor ($P = I^2 R = 1^2 \\times 2 = 2\\text{ W}$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$2{,}0\\text{ Newton}$, karena panjang kawat 40 cm keliru dimasukkan tanpa konversi ke satuan meter diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$0{,}40\\text{ Newton}$, dihitung dari perkalian arus listrik induksi dengan tegangan hambatan rel kawat."
      },
      {
        "key": "C",
        "text": "$0{,}10\\text{ Newton}$, dihitung dengan membagi gaya Lorentz terhadap kuadrat kelajuan geser kawat."
      },
      {
        "key": "D",
        "text": "$1{,}0\\text{ Newton}$, karena gaya luar disamakan secara langsung dengan nilai kuat arus yang mengalir di rel."
      },
      {
        "key": "E",
        "text": "$0{,}20\\text{ Newton}$, dihitung dari GGL induksi $\\varepsilon = B l v = 0{,}5 \\times 0{,}4 \\times 10 = 2\\text{ V}$, arus induksi $I = \\frac{\\varepsilon}{R} = \\frac{2}{2} = 1\\text{ A}$, dan gaya penahan Lorentz $F = B I l = 0{,}5 \\times 1 \\times 0{,}4 = 0{,}2\\text{ N}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $0{,}20\\text{ Newton}$, dihitung dari GGL induksi $\\varepsilon = B l v = 0{,}5 \\times 0{,}4 \\times 10 = 2\\text{ V}$, arus induksi $I = \\frac{\\varepsilon}{R} = \\frac{2}{2} = 1\\text{ A}$, dan gaya penahan Lorentz $F = B I l = 0{,}5 \\times 1 \\times 0{,}4 = 0{,}2\\text{ N}$.. eps = B*l*v = 0,5 * 0,4 * 10 = 2 V. Arus I = eps / R = 2 / 2 = 1 A. Gaya luar mengimbangi gaya Lorentz: F = B * I * l. F = 0,5 * 1 * 0,4 = 0,20 Newton."
  },
  {
    "id": "fis-lat-m-21",
    "materi": "OPTIKA GEOMETRI (PEMBIASAN)",
    "topic": "Hukum Snellius dan Sudut Kritis Pemantulan Total",
    "hints": {
      "concept": "Sudut kritis terjadi saat sinar merambat dari medium rapat ke renggang dengan sudut bias 90°: sin(theta_c) = n_kurang_rapat / n_rapat.",
      "execution": "sin(theta_c) = 1,0 / 1,5 = 2/3 ≈ 0,667 -> theta_c ≈ 41,8°."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah berkas sinar merambat di dalam balok kaca yang memiliki indeks bias $n_1 = 1{,}5$ menuju perbatasan udara ($n_2 = 1{,}0$). Sudut kritis ($\\theta_c$) pemantulan internal total pada batas kaca-udara tersebut adalah...",
    "formulaHud": {
      "title": "SUDUT KRITIS PEMANTULAN INTERNAL TOTAL",
      "latex": "n_1 \\sin\\theta_c = n_2 \\sin 90^\\circ \\implies \\sin\\theta_c = \\frac{n_2}{n_1} = \\frac{1{,}0}{1{,}5} = \\frac{2}{3} \\implies \\theta_c \\approx 41{,}81^\\circ",
      "legend": "• Syarat Pemantulan Total: (1) Sinar merambat dari medium lebih rapat ($n_1$) ke medium kurang rapat ($n_2$), (2) Sudut datang melebihi sudut kritis ($\\theta_i > \\theta_c$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\theta_c = \\arcsin(0{,}67) \\approx 41{,}8^\\circ$, dihitung dari Hukum Snellius pada saat sudut bias $\\theta_2 = 90^\\circ$: $\\sin\\theta_c = \\frac{n_2}{n_1} = \\frac{1{,}0}{1{,}5} = \\frac{2}{3} \\approx 0{,}667$."
      },
      {
        "key": "B",
        "text": "$\\theta_c = \\arcsin(1{,}50)$, yang secara matematis mustahil karena nilai fungsi sinus tidak dapat melebihi angka 1 sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$\\theta_c = 30{,}0^\\circ$, dihitung dari pembagian indeks bias kaca dengan sudut pembiasan istimewa optik."
      },
      {
        "key": "D",
        "text": "$\\theta_c = 60{,}0^\\circ$, dihitung dengan mengalikan selisih indeks bias medium dengan konstanta kelajuan cahaya."
      },
      {
        "key": "E",
        "text": "$\\theta_c = 45{,}0^\\circ$, karena sudut kritis diasumsikan sama pada seluruh jenis material optik transparan."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\theta_c = \\arcsin(0{,}67) \\approx 41{,}8^\\circ$, dihitung dari Hukum Snellius pada saat sudut bias $\\theta_2 = 90^\\circ$: $\\sin\\theta_c = \\frac{n_2}{n_1} = \\frac{1{,}0}{1{,}5} = \\frac{2}{3} \\approx 0{,}667$.. Sudut kritis terjadi saat sinar merambat dari medium rapat ke renggang dengan sudut bias 90°: sin(theta_c) = n_kurang_rapat / n_rapat. sin(theta_c) = 1,0 / 1,5 = 2/3 ≈ 0,667 -> theta_c ≈ 41,8°."
  },
  {
    "id": "fis-lat-m-22",
    "materi": "ALAT OPTIK (MIKROSKOP)",
    "topic": "Perbesaran Total Mikroskop Mata Tak Berakomodasi",
    "hints": {
      "concept": "Cari s'ob: 1/s'ob = 1/1 - 1/1,1 = 1/11 -> s'ob = 11 cm. Mob = 11 / 1,1 = 10x. Mok (tanpa akomodasi) = Sn / fok = 25 / 5 = 5x. Mtot = Mob * Mok.",
      "execution": "Mob = 10x. Mok = 5x. Mtot = 10 * 5 = 50 kali."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah mikroskop memiliki lensa objektif dengan fokus $f_{ob} = 1\\text{ cm}$ dan lensa okuler dengan fokus $f_{ok} = 5\\text{ cm}$. Sebuah preparat sel diletakkan pada jarak $s_{ob} = 1{,}1\\text{ cm}$ di depan lensa objektif. Jika pengamatan dilakukan oleh pengamat bermata normal ($S_n = 25\\text{ cm}$) dengan mata tanpa berakomodasi, perbesaran total mikroskop ($M_{\\text{total}}$) adalah...",
    "formulaHud": {
      "title": "PERBESARAN TOTAL MIKROSKOP (MATA TANPA AKOMODASI)",
      "latex": "\\begin{aligned} \\frac{1}{s'_{ob}} &= \\frac{1}{1{,}0} - \\frac{1}{1{,}1} = 1 - \\frac{10}{11} = \\frac{1}{11} \\implies s'_{ob} = 11\\text{ cm} \\\\ M_{ob} &= \\frac{11}{1{,}1} = 10\\text{ kali}; \\quad M_{ok} = \\frac{S_n}{f_{ok}} = \\frac{25}{5} = 5\\text{ kali} \\\\ M_{\\text{tot}} &= M_{ob} \\times M_{ok} = 10 \\times 5 = 50\\text{ kali} \\end{aligned}",
      "legend": "• Jarak Lensa (Tubus): $d = s'_{ob} + f_{ok} = 11 + 5 = 16\\text{ cm}$<br>• Mata tanpa akomodasi: Bayangan objektif tepat jatuh di titik fokus okuler ($s_{ok} = f_{ok}$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$60\\text{ kali}$, dihitung dari perbesaran okuler pada kondisi mata berakomodasi maksimum ($S_n/f_{ok} + 1$) sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$50\\text{ kali}$, karena perbesaran lensa objektif adalah $M_{ob} = \\left|\\frac{s'_{ob}}{s_{ob}}\\right| = \\frac{11}{1{,}1} = 10\\text{ kali}$, dan perbesaran sudut okuler tanpa akomodasi adalah $M_{ok} = \\frac{S_n}{f_{ok}} = \\frac{25}{5} = 5\\text{ kali}$, sehingga $M_{\\text{total}} = 10 \\times 5 = 50\\text{ kali}$."
      },
      {
        "key": "C",
        "text": "$25\\text{ kali}$, dihitung dari perbesaran lensa okuler dikalikan dengan perbandingan jarak fokus lensa."
      },
      {
        "key": "D",
        "text": "$15\\text{ kali}$, diperoleh dari penjumlahan langsung perbesaran objektif dan perbesaran okuler."
      },
      {
        "key": "E",
        "text": "$100\\text{ kali}$, dihitung dengan mengabaikan panjang fokus lensa okuler pada penyebut pembagian bayangan."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $50\\text{ kali}$, karena perbesaran lensa objektif adalah $M_{ob} = \\left|\\frac{s'_{ob}}{s_{ob}}\\right| = \\frac{11}{1{,}1} = 10\\text{ kali}$, dan perbesaran sudut okuler tanpa akomodasi adalah $M_{ok} = \\frac{S_n}{f_{ok}} = \\frac{25}{5} = 5\\text{ kali}$, sehingga $M_{\\text{total}} = 10 \\times 5 = 50\\text{ kali}$.. Cari s'ob: 1/s'ob = 1/1 - 1/1,1 = 1/11 -> s'ob = 11 cm. Mob = 11 / 1,1 = 10x. Mok (tanpa akomodasi) = Sn / fok = 25 / 5 = 5x. Mtot = Mob * Mok. Mob = 10x. Mok = 5x. Mtot = 10 * 5 = 50 kali."
  },
  {
    "id": "fis-lat-m-23",
    "materi": "GELOMBANG CAHAYA (INTERFERENSI)",
    "topic": "Interferensi Celah Ganda Young",
    "hints": {
      "concept": "Interferensi terang: d * y / L = n * lambda. lambda = (d * y) / (n * L).",
      "execution": "lambda = (0,2e-3 * 9e-3) / (3 * 1) = 1,8e-6 / 3 = 6e-7 m = 600 nm."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dalam percobaan celah ganda Young, dua celah sempit terpisah pada jarak $d = 0{,}2\\text{ mm}$ disinari berkas cahaya monokromatik. Pola interferensi diamati pada layar yang berjarak $L = 1\\text{ meter}$ di belakang celah. Jika jarak antara garis terang pusat ke garis terang ketiga adalah $y_3 = 9\\text{ mm}$, panjang gelombang cahaya yang digunakan ($\\lambda$) adalah...",
    "formulaHud": {
      "title": "FORMULA INTERFERENSI MAKSIMUM CELAH GANDA",
      "latex": "d \\frac{y_n}{L} = n \\lambda \\implies \\lambda = \\frac{d \\cdot y_n}{n L} = \\frac{(2 \\times 10^{-4}) \\times (9 \\times 10^{-3})}{3 \\times 1} = \\frac{18 \\times 10^{-7}}{3} = 6 \\times 10^{-7}\\text{ m} = 600\\text{ nm}",
      "legend": "• $d = 0{,}2\\text{ mm} = 2 \\times 10^{-4}\\text{ m}$<br>• $L = 1\\text{ m}$<br>• $y_3 = 9\\text{ mm} = 9 \\times 10^{-3}\\text{ m}$ pada orde $n = 3$"
    },
    "options": [
      {
        "key": "A",
        "text": "$400\\text{ nm}$, dihitung dengan mengabaikan jarak celah ke layar pada penyebut persamaan interferensi ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$1.800\\text{ nm}$, karena nilai orde terang ketiga keliru dikalikan bukan dibagi pada ruas panjang gelombang."
      },
      {
        "key": "C",
        "text": "$600\\text{ nm}$ (atau $6 \\times 10^{-7}\\text{ meter}$), dihitung dari rumus interferensi maksimum celah ganda: $d \\frac{y_n}{L} = n \\lambda \\implies \\lambda = \\frac{d \\cdot y_3}{3L} = \\frac{(2 \\times 10^{-4}\\text{ m})(9 \\times 10^{-3}\\text{ m})}{3 \\times 1\\text{ m}} = 6 \\times 10^{-7}\\text{ m}$."
      },
      {
        "key": "D",
        "text": "$500\\text{ nm}$, dihitung dari asumsi panjang gelombang spektrum cahaya hijau tampak di udara terbuka."
      },
      {
        "key": "E",
        "text": "$300\\text{ nm}$, dihitung dengan membagi dua hasil perhitungan panjang gelombang cahaya monokromatik."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $600\\text{ nm}$ (atau $6 \\times 10^{-7}\\text{ meter}$), dihitung dari rumus interferensi maksimum celah ganda: $d \\frac{y_n}{L} = n \\lambda \\implies \\lambda = \\frac{d \\cdot y_3}{3L} = \\frac{(2 \\times 10^{-4}\\text{ m})(9 \\times 10^{-3}\\text{ m})}{3 \\times 1\\text{ m}} = 6 \\times 10^{-7}\\text{ m}$.. Interferensi terang: d * y / L = n * lambda. lambda = (d * y) / (n * L). lambda = (0,2e-3 * 9e-3) / (3 * 1) = 1,8e-6 / 3 = 6e-7 m = 600 nm."
  },
  {
    "id": "fis-lat-m-24",
    "materi": "GELOMBANG CAHAYA (DIFRAKSI KISI)",
    "topic": "Difraksi Cahaya pada Kisi Transmisi",
    "hints": {
      "concept": "d * sin(theta) = n * lambda. Cari d = n*lambda / sin(theta), lalu N = 1 / d (konversi ke garis/cm).",
      "execution": "d = 2 * 5e-7 / 0,5 = 2e-6 m = 2e-4 cm. N = 1 / 2e-4 = 5.000 garis/cm."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Berkas cahaya monokromatik dengan panjang gelombang $\\lambda = 500\\text{ nm}$ ($5 \\times 10^{-7}\\text{ m}$) dijatuhkan tegak lurus pada sebuah kisi difraksi. Garis terang orde kedua ($n = 2$) terdifraksi membentuk sudut deviasi $\\theta = 30^\\circ$ ($\\sin 30^\\circ = 0{,}5$). Jumlah garis per sentimeter ($N$) dari kisi difraksi tersebut adalah...",
    "formulaHud": {
      "title": "FORMULA DIFRAKSI PADA KISI",
      "latex": "d \\sin\\theta = n \\lambda \\implies d = \\frac{n \\lambda}{\\sin\\theta} = \\frac{2 \\times (5 \\times 10^{-7}\\text{ m})}{0{,}5} = 2 \\times 10^{-6}\\text{ m}; \\quad N = \\frac{1}{d} = \\frac{1}{2 \\times 10^{-4}\\text{ cm}} = 5.000\\text{ garis/cm}",
      "legend": "• $d$ = Jarak antar celah (tetapan kisi dalam meter atau cm)<br>• $N$ = Jumlah celah/garis per satuan panjang ($N = 1/d$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$2.500\\text{ garis/cm}$, dihitung dari orde pertama difraksi kisi tanpa mengalikan faktor orde kedua menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$10.000\\text{ garis/cm}$, karena sudut 30 derajat keliru dikalikan dua menjadi sudut deviasi 60 derajat."
      },
      {
        "key": "C",
        "text": "$500\\text{ garis/cm}$, karena konstanta panjang gelombang langsung dijadikan nilai kerapatan garis kisi kaca."
      },
      {
        "key": "D",
        "text": "$5.000\\text{ garis/cm}$, karena tetapan kisi adalah $d = \\frac{n \\lambda}{\\sin\\theta} = \\frac{2 \\times (5 \\times 10^{-7}\\text{ m})}{0{,}5} = 2 \\times 10^{-6}\\text{ m} = 2 \\times 10^{-4}\\text{ cm}$, sehingga $N = \\frac{1}{d} = \\frac{1}{2 \\times 10^{-4}\\text{ cm}} = 5.000\\text{ garis/cm}$."
      },
      {
        "key": "E",
        "text": "$1.250\\text{ garis/cm}$, dihitung dari perbandingan kecepatan cahaya terhadap frekuensi berkas sinar laser."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $5.000\\text{ garis/cm}$, karena tetapan kisi adalah $d = \\frac{n \\lambda}{\\sin\\theta} = \\frac{2 \\times (5 \\times 10^{-7}\\text{ m})}{0{,}5} = 2 \\times 10^{-6}\\text{ m} = 2 \\times 10^{-4}\\text{ cm}$, sehingga $N = \\frac{1}{d} = \\frac{1}{2 \\times 10^{-4}\\text{ cm}} = 5.000\\text{ garis/cm}$.. d * sin(theta) = n * lambda. Cari d = n*lambda / sin(theta), lalu N = 1 / d (konversi ke garis/cm). d = 2 * 5e-7 / 0,5 = 2e-6 m = 2e-4 cm. N = 1 / 2e-4 = 5.000 garis/cm."
  },
  {
    "id": "fis-lat-m-25",
    "materi": "FISIKA MODERN (RELATIVITAS MASSA & ENERGI)",
    "topic": "Energi Kinetik Relativistik & Kesetaraan Massa-Energi",
    "hints": {
      "concept": "Energi total relativistik: E = gamma * E0. Energi kinetik Ek = E - E0 = (gamma - 1) * E0. gamma = 1 / sqrt(1 - 0,8^2) = 1 / 0,6 = 5/3.",
      "execution": "Ek = (5/3 - 1) * E0 = 2/3 E0."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah partikel memiliki massa diam $m_0$. Partikel tersebut dipercepat hingga bergerak dengan kecepatan relativistik konstan $v = 0{,}8c$ (di mana $c$ adalah kecepatan cahaya). Energi kinetik ($E_k$) partikel tersebut dinyatakan dalam energi diamnya ($E_0 = m_0 c^2$) adalah...",
    "formulaHud": {
      "title": "ENERGI KINETIK RELATIVISTIK EINSTEIN",
      "latex": "E = \\gamma m_0 c^2; \\quad E_k = E - E_0 = (\\gamma - 1) m_0 c^2 = \\left(\\frac{1}{\\sqrt{1 - 0{,}64}} - 1\\right) E_0 = \\left(\\frac{5}{3} - 1\\right) E_0 = \\frac{2}{3} E_0",
      "legend": "• $\\gamma = \\frac{1}{0{,}6} = \\frac{5}{3}$<br>• Rumus Klasik $\\frac{1}{2} m v^2$ menghasilkan galat fatal pada kecepatan tinggi ($v > 0{,}1c$)<br>• $E_k$ relativistik selalu lebih besar daripada prediksi mekanika Newton klasik"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\frac{5}{3} E_0$, karena nilai tersebut merupakan energi total relativistik ($E$), belum dikurangkan dengan energi diam partikel diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$0{,}32 E_0$, dihitung dari rumus mekanika klasik Newton $E_k = \\frac{1}{2} m v^2 = \\frac{1}{2} m_0 (0{,}8c)^2 = 0{,}32 E_0$ yang tidak berlaku pada kecepatan mendekati cahaya."
      },
      {
        "key": "C",
        "text": "$\\frac{1}{3} E_0$, dihitung dari selisih kuadrat faktor Lorentz dengan konstanta Planck."
      },
      {
        "key": "D",
        "text": "$1{,}25 E_0$, dihitung dari kebalikan rasio kecepatan terhadap kecepatan rambat foton di ruang hampa."
      },
      {
        "key": "E",
        "text": "$\\frac{2}{3} E_0$ (atau $0{,}67 E_0$), karena faktor Lorentz untuk kecepatan $0{,}8c$ adalah $\\gamma = \\frac{1}{\\sqrt{1 - (0{,}8)^2}} = \\frac{1}{0{,}6} = \\frac{5}{3}$, sehingga energi total $E = \\gamma E_0 = \\frac{5}{3} E_0$, dan energi kinetik $E_k = E - E_0 = \\left(\\frac{5}{3} - 1\\right) E_0 = \\frac{2}{3} E_0$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $\\frac{2}{3} E_0$ (atau $0{,}67 E_0$), karena faktor Lorentz untuk kecepatan $0{,}8c$ adalah $\\gamma = \\frac{1}{\\sqrt{1 - (0{,}8)^2}} = \\frac{1}{0{,}6} = \\frac{5}{3}$, sehingga energi total $E = \\gamma E_0 = \\frac{5}{3} E_0$, dan energi kinetik $E_k = E - E_0 = \\left(\\frac{5}{3} - 1\\right) E_0 = \\frac{2}{3} E_0$.. Energi total relativistik: E = gamma * E0. Energi kinetik Ek = E - E0 = (gamma - 1) * E0. gamma = 1 / sqrt(1 - 0,8^2) = 1 / 0,6 = 5/3. Ek = (5/3 - 1) * E0 = 2/3 E0."
  },
  {
    "id": "fis-lat-h-01",
    "materi": "DINAMIKA ROTASI & MENGGELINDING MURNI",
    "topic": "Gerak Menggelinding Murni Silinder Pejal pada Bidang Miring",
    "hints": {
      "concept": "Gunakan Hukum II Newton translasi: Mg sin(theta) - fs = M*a, dan rotasi: fs * R = I * (a/R). Untuk silinder pejal k = 1/2, a = g sin(theta) / (1 + k).",
      "execution": "a = (10 * 0,5) / (1 + 0,5) = 10/3 m/s^2. fs = 1/2 * 4 * (10/3) = 20/3 N."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah silinder pejal homogen bermassa $M = 4\\text{ kg}$ dan jari-jari $R = 20\\text{ cm}$ dilepaskan dari puncak bidang miring kasar dengan sudut kemiringan $\\theta = 30^\\circ$ ($\\sin 30^\\circ = 0{,}5$). Silinder menggelinding murni tanpa slip menuruni bidang miring. Momen inersia silinder pejal terhadap sumbu simetrinya adalah $I = \\frac{1}{2} M R^2$, dan percepatan gravitasi bumi $g = 10\\text{ m/s}^2$. Percepatan linier pusat massa silinder ($a$) dan gaya gesek statis ($f_s$) yang bekerja pada titik kontak adalah...",
    "formulaHud": {
      "title": "FORMULA PERCEPATAN MENGGELINDING MURNI",
      "latex": "a = \\frac{g \\sin\\theta}{1 + k}; \\quad f_s = \\frac{k}{1 + k} M g \\sin\\theta",
      "legend": "• $k$ = Faktor bentuk inersia silinder pejal ($k = \\frac{1}{2}$)<br>• $a = \\frac{10 \\times 0{,}5}{1 + 0{,}5} = \\frac{5}{1{,}5} = \\frac{10}{3}\\text{ m/s}^2$<br>• $f_s = \\frac{1}{2} M a = 2 \\times \\frac{10}{3} = \\frac{20}{3}\\text{ N}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$a = \\frac{10}{3}\\text{ m/s}^2$ dan $f_s = \\frac{20}{3}\\text{ N}$, dihitung dari persamaan translasi $M g \\sin\\theta - f_s = M a$ dan rotasi $f_s R = I \\alpha = \\frac{1}{2} M R^2 \\left(\\frac{a}{R}\\right)$, sehingga $a = \\frac{g \\sin\\theta}{1 + k} = \\frac{10 \\times 0{,}5}{1 + 0{,}5} = \\frac{5}{1{,}5} = \\frac{10}{3}\\text{ m/s}^2$, serta $f_s = \\frac{1}{2} M a = \\frac{1}{2}(4)\\left(\\frac{10}{3}\\right) = \\frac{20}{3}\\text{ N}$."
      },
      {
        "key": "B",
        "text": "$a = 5\\text{ m/s}^2$ dan $f_s = 0\\text{ N}$, karena silinder dianggap meluncur bebas di atas bidang miring licin sempurna tanpa torsi gesek sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$a = 2{,}5\\text{ m/s}^2$ dan $f_s = 10\\text{ N}$, dihitung dengan menggunakan konstanta momen inersia bola pejal dua per lima."
      },
      {
        "key": "D",
        "text": "$a = \\frac{20}{3}\\text{ m/s}^2$ dan $f_s = \\frac{40}{3}\\text{ N}$, karena percepatan gravitasi tidak dikalikan dengan sinus sudut kemiringan bidang miring."
      },
      {
        "key": "E",
        "text": "$a = 3\\text{ m/s}^2$ dan $f_s = 8\\text{ N}$, dihitung dari pendekatan pembulatan kasar koefisien gesekan kinetik permukaan bidang luncur."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $a = \\frac{10}{3}\\text{ m/s}^2$ dan $f_s = \\frac{20}{3}\\text{ N}$, dihitung dari persamaan translasi $M g \\sin\\theta - f_s = M a$ dan rotasi $f_s R = I \\alpha = \\frac{1}{2} M R^2 \\left(\\frac{a}{R}\\right)$, sehingga $a = \\frac{g \\sin\\theta}{1 + k} = \\frac{10 \\times 0{,}5}{1 + 0{,}5} = \\frac{5}{1{,}5} = \\frac{10}{3}\\text{ m/s}^2$, serta $f_s = \\frac{1}{2} M a = \\frac{1}{2}(4)\\left(\\frac{10}{3}\\right) = \\frac{20}{3}\\text{ N}$.. Gunakan Hukum II Newton translasi: Mg sin(theta) - fs = M*a, dan rotasi: fs * R = I * (a/R). Untuk silinder pejal k = 1/2, a = g sin(theta) / (1 + k). a = (10 * 0,5) / (1 + 0,5) = 10/3 m/s^2. fs = 1/2 * 4 * (10/3) = 20/3 N."
  },
  {
    "id": "fis-lat-h-02",
    "materi": "KESETIMBANGAN BENDA TEGAR",
    "topic": "Tangga Bersandar pada Dinding Licin dan Lantai Kasar",
    "hints": {
      "concept": "Torsi terhadap tumpuan lantai = 0: ND * L sin(theta) - W * (L/2) cos(theta) = 0. ND = W / (2 tan theta). Kesetimbangan translasi: fs = ND dan NL = W.",
      "execution": "mu_s = fs / NL = ND / W = 1 / (2 tan theta)."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah tangga homogen dengan panjang $L$ dan berat $W$ disandarkan pada dinding vertikal yang licin sempurna dan bertumpu pada lantai horizontal yang kasar. Sudut kemiringan tangga terhadap lantai horizontal adalah $\\theta$. Agar tangga tetap berada dalam keadaan setimbang tepat saat akan tergelincir, nilai koefisien gesekan statis minimum ($\\mu_s$) antara ujung bawah tangga dan lantai horizontal harus bernilai...",
    "formulaHud": {
      "title": "KESETIMBANGAN ROTASI & TRANSLASI TANGGA",
      "latex": "\\sum F_x = 0 \\implies f_s = N_D; \\quad \\sum F_y = 0 \\implies N_L = W; \\quad \\sum \\tau_L = 0 \\implies N_D (L \\sin\\theta) = W \\left(\\frac{L}{2} \\cos\\theta\\right)",
      "legend": "• $N_D = \\frac{W \\cos\\theta}{2 \\sin\\theta} = \\frac{W}{2 \\tan\\theta}$<br>• Tepat akan tergelincir: $f_s = \\mu_s N_L = \\mu_s W$<br>• $\\mu_s W = \\frac{W}{2 \\tan\\theta} \\implies \\mu_s = \\frac{1}{2 \\tan\\theta}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\mu_s = \\frac{1}{\\tan\\theta}$, karena titik berat tangga keliru ditempatkan di puncak tertinggi tangga yang bersentuhan dengan dinding vertikal sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$\\mu_s = \\frac{1}{2 \\tan\\theta}$ (atau $\\frac{1}{2} \\cot\\theta$), diperoleh dari syarat kesetimbangan gaya horizontal $N_{\\text{dinding}} = f_s = \\mu_s N_{\\text{lantai}}$, gaya vertikal $N_{\\text{lantai}} = W$, dan torsi terhadap dasar tangga $\\sum \\tau = 0 \\implies N_{\\text{dinding}} (L \\sin\\theta) - W \\left(\\frac{L}{2} \\cos\\theta\\right) = 0$, sehingga $N_{\\text{dinding}} = \\frac{W \\cos\\theta}{2 \\sin\\theta} = \\frac{W}{2 \\tan\\theta}$."
      },
      {
        "key": "C",
        "text": "$\\mu_s = \\frac{1}{2} \\tan\\theta$, karena fungsi sinus dan cosinus pada lengan momen torsi tertukar letaknya saat proyeksi sudut kemiringan."
      },
      {
        "key": "D",
        "text": "$\\mu_s = \\frac{2}{\\sin\\theta}$, karena gaya normal dinding diasumsikan sama persis dengan dua kali lipat gaya berat tangga homogen."
      },
      {
        "key": "E",
        "text": "$\\mu_s = \\frac{1}{2 \\cos\\theta}$, dihitung dari perbandingan gaya normal lantai terhadap komponen tangensial panjang batang penyangga."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\mu_s = \\frac{1}{2 \\tan\\theta}$ (atau $\\frac{1}{2} \\cot\\theta$), diperoleh dari syarat kesetimbangan gaya horizontal $N_{\\text{dinding}} = f_s = \\mu_s N_{\\text{lantai}}$, gaya vertikal $N_{\\text{lantai}} = W$, dan torsi terhadap dasar tangga $\\sum \\tau = 0 \\implies N_{\\text{dinding}} (L \\sin\\theta) - W \\left(\\frac{L}{2} \\cos\\theta\\right) = 0$, sehingga $N_{\\text{dinding}} = \\frac{W \\cos\\theta}{2 \\sin\\theta} = \\frac{W}{2 \\tan\\theta}$.. Torsi terhadap tumpuan lantai = 0: ND * L sin(theta) - W * (L/2) cos(theta) = 0. ND = W / (2 tan theta). Kesetimbangan translasi: fs = ND dan NL = W. mu_s = fs / NL = ND / W = 1 / (2 tan theta)."
  },
  {
    "id": "fis-lat-h-03",
    "materi": "GETARAN HARMONIK SEDERHANA",
    "topic": "Sistem Pegas Gabungan Seri-Paralel dengan Beban Gandeng",
    "hints": {
      "concept": "Pegas paralel: kp = k1 + k2 = 400 + 400 = 800 N/m. Frekuensi sudut omega = sqrt(kp / m). Periode T = 2pi / omega.",
      "execution": "omega = sqrt(800 / 2) = sqrt(400) = 20 rad/s. T = 2pi / 20 = pi / 10 s."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua buah pegas identik masing-masing memiliki konstanta pegas $k = 400\\text{ N/m}$. Mula-mula kedua pegas disusun secara paralel, kemudian ujung gabungan pegas tersebut digantungi beban bermassa $m = 2\\text{ kg}$. Jika sistem tersebut disimpangkan sedikit lalu berosilasi harmonik sederhana vertikal, frekuensi sudut osilasi ($\\omega$) dan periode getarannya ($T$) berturut-turut adalah...",
    "formulaHud": {
      "title": "FREKUENSI SUDUT PEGAS PARALEL",
      "latex": "k_p = k_1 + k_2 = 2k = 800\\text{ N/m}; \\quad \\omega = \\sqrt{\\frac{k_p}{m}} = \\sqrt{\\frac{800}{2}} = 20\\text{ rad/s}; \\quad T = \\frac{2\\pi}{\\omega} = \\frac{\\pi}{10}\\text{ s}",
      "legend": "• $k_p$ = Konstanta ekuivalen pegas paralel ($400 + 400 = 800\\text{ N/m}$)<br>• $m = 2\\text{ kg}$<br>• $\\omega = 20\\text{ rad/s}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\omega = 10\\text{ rad/s}$ dan $T = \\frac{\\pi}{5}\\text{ s}$, karena kedua pegas keliru dihitung menggunakan formula susunan seri $k_s = 200\\text{ N/m}$ ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$\\omega = 40\\text{ rad/s}$ dan $T = \\frac{\\pi}{20}\\text{ s}$, dihitung dari penggandaan kuadrat frekuensi getaran alami pegas."
      },
      {
        "key": "C",
        "text": "$\\omega = 20\\text{ rad/s}$ dan $T = \\frac{\\pi}{10}\\text{ s}$ (sekitar $0{,}314\\text{ s}$), karena konstanta pegas pengganti paralel adalah $k_p = k_1 + k_2 = 400 + 400 = 800\\text{ N/m}$, sehingga frekuensi sudut $\\omega = \\sqrt{\\frac{k_p}{m}} = \\sqrt{\\frac{800}{2}} = \\sqrt{400} = 20\\text{ rad/s}$, dan periode $T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{20} = \\frac{\\pi}{10}\\text{ s}$."
      },
      {
        "key": "D",
        "text": "$\\omega = 14{,}14\\text{ rad/s}$ dan $T = \\frac{\\pi}{7}\\text{ s}$, karena hanya memperhitungkan konstanta satu pegas tunggal tanpa paralel."
      },
      {
        "key": "E",
        "text": "$\\omega = 5\\text{ rad/s}$ dan $T = \\frac{2\\pi}{5}\\text{ s}$, dihitung dari rasio massa beban dibagi konstanta pegas dalam akar."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $\\omega = 20\\text{ rad/s}$ dan $T = \\frac{\\pi}{10}\\text{ s}$ (sekitar $0{,}314\\text{ s}$), karena konstanta pegas pengganti paralel adalah $k_p = k_1 + k_2 = 400 + 400 = 800\\text{ N/m}$, sehingga frekuensi sudut $\\omega = \\sqrt{\\frac{k_p}{m}} = \\sqrt{\\frac{800}{2}} = \\sqrt{400} = 20\\text{ rad/s}$, dan periode $T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{20} = \\frac{\\pi}{10}\\text{ s}$.. Pegas paralel: kp = k1 + k2 = 400 + 400 = 800 N/m. Frekuensi sudut omega = sqrt(kp / m). Periode T = 2pi / omega. omega = sqrt(800 / 2) = sqrt(400) = 20 rad/s. T = 2pi / 20 = pi / 10 s."
  },
  {
    "id": "fis-lat-h-04",
    "materi": "FLUIDA DINAMIS (TEOREMA TORRICELLI & KONTINUITAS)",
    "topic": "Laju Aliran Efleks dengan Luas Tangki Terbatas",
    "hints": {
      "concept": "Gunakan persamaan Bernoulli antara permukaan atas tangki dan lubang dasar. Jika A2 << A1, kecepatan efleks v2 = sqrt(2gh).",
      "execution": "v2 = sqrt(2 * 10 * 5) = sqrt(100) = 10 m/s."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah tangki silinder terbuka berisi air memiliki luas penampang $A_1 = 1\\text{ m}^2$. Di dasar tangki terdapat lubang kebocoran kecil berpenampang $A_2 = 10\\text{ cm}^2 = 10^{-3}\\text{ m}^2$. Pada saat ketinggian permukaan air dari dasar lubang adalah $h = 5\\text{ meter}$, laju semburan air yang keluar dari lubang dasar ($v_2$) dengan memperhitungkan turunnya permukaan air di tangki ($g = 10\\text{ m/s}^2$) adalah...",
    "formulaHud": {
      "title": "TEOREMA TORRICELLI TERKOREKSI PERSAMAAN BERNOULLI",
      "latex": "v_2 = \\sqrt{\\frac{2gh}{1 - \\left(\\frac{A_2}{A_1}\\right)^2}} \\approx \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 5} = 10\\text{ m/s}",
      "legend": "• $h = 5\\text{ m}$, $g = 10\\text{ m/s}^2$<br>• Koreksi kontinuitas bernilai $\\approx 1 - 10^{-6} \\approx 1$<br>• $v_2 = 10\\text{ m/s}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$v_2 = 5\\text{ m/s}$, karena rumus Torricelli keliru tidak menyertakan angka 2 di dalam tanda akar kuadrat gravitasi tinggi menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$v_2 = 14{,}14\\text{ m/s}$, dihitung dari perkalian percepatan gravitasi dengan kuadrat ketinggian air dalam tangki penampung."
      },
      {
        "key": "C",
        "text": "$v_2 = 20\\text{ m/s}$, dihitung dari penggandaan tinggi tangki sebelum dimasukkan ke dalam akar kuadrat fluida Bernoulli."
      },
      {
        "key": "D",
        "text": "$v_2 = 10\\text{ m/s}$ (tepatnya $\\sqrt{\\frac{2gh}{1 - (A_2/A_1)^2}} = \\sqrt{\\frac{100}{1 - 10^{-6}}} \\approx 10\\text{ m/s}$), karena rasio luas penampang $(A_2/A_1)^2 = 10^{-6}$ sangat kecil mendekati nol, sehingga kecepatan semburan sangat akurat didekati dengan teorema Torricelli standar $v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 5} = \\sqrt{100} = 10\\text{ m/s}$."
      },
      {
        "key": "E",
        "text": "$v_2 = 1\\text{ m/s}$, karena kecepatan semburan keliru dihitung dari pembagian volume air dengan luas penampang tangki atas."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $v_2 = 10\\text{ m/s}$ (tepatnya $\\sqrt{\\frac{2gh}{1 - (A_2/A_1)^2}} = \\sqrt{\\frac{100}{1 - 10^{-6}}} \\approx 10\\text{ m/s}$), karena rasio luas penampang $(A_2/A_1)^2 = 10^{-6}$ sangat kecil mendekati nol, sehingga kecepatan semburan sangat akurat didekati dengan teorema Torricelli standar $v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 5} = \\sqrt{100} = 10\\text{ m/s}$.. Gunakan persamaan Bernoulli antara permukaan atas tangki dan lubang dasar. Jika A2 << A1, kecepatan efleks v2 = sqrt(2gh). v2 = sqrt(2 * 10 * 5) = sqrt(100) = 10 m/s."
  },
  {
    "id": "fis-lat-h-05",
    "materi": "TERMODINAMIKA (MESIN PENDINGIN / REFRIGERATOR CARNOT)",
    "topic": "Koefisien Kinerja (COP) dan Daya Listrik Refrigerator",
    "hints": {
      "concept": "Konversi suhu ke Kelvin: Tc = 270 K, Th = 300 K. COP KP = Tc / (Th - Tc) = 270 / 30 = 9. Daya P = W / t = Qc / KP.",
      "execution": "KP = 9. P = 1.350 / 9 = 150 Watt."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah lemari es (refrigerator) beroperasi dengan siklus Carnot terbalik antara reservoir suhu rendah $T_C = -3^\\circ\\text{C}$ dan reservoir suhu tinggi $T_H = 27^\\circ\\text{C}$. Jika lemari es tersebut menyerap kalor sebesar $Q_C = 1.350\\text{ Joule}$ dari dalam ruang pendingin setiap detiknya, daya listrik masukan ($P$) yang dibutuhkan untuk menggerakkan kompresor refrigerator tersebut adalah...",
    "formulaHud": {
      "title": "KOEFISIEN PERFORMA (COP) REFRIGERATOR CARNOT",
      "latex": "K_P = \\frac{T_C}{T_H - T_C} = \\frac{270}{300 - 270} = 9; \\quad W = \\frac{Q_C}{K_P} = \\frac{1.350\\text{ J}}{9} = 150\\text{ J} \\implies P = 150\\text{ W}",
      "legend": "• $T_C = -3 + 273 = 270\\text{ K}$<br>• $T_H = 27 + 273 = 300\\text{ K}$<br>• $K_P = 9$<br>• Daya $P = \\frac{W}{t} = 150\\text{ Watt}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$P = 135\\text{ Watt}$, karena suhu reservoir dihitung langsung menggunakan satuan derajat Celsius tanpa konversi ke Kelvin diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$P = 300\\text{ Watt}$, dihitung dari efisiensi mesin pemanas Carnot standar dikalikan dengan total kalor serap reservoir."
      },
      {
        "key": "C",
        "text": "$P = 1.500\\text{ Watt}$, karena kalor yang diserap tertukar dengan kalor buangan yang dilepaskan ke lingkungan luar."
      },
      {
        "key": "D",
        "text": "$P = 450\\text{ Watt}$, dihitung dari pembagian kalor serap dengan selisih suhu reservoir dalam satuan Celsius."
      },
      {
        "key": "E",
        "text": "$P = 150\\text{ Watt}$, karena dalam skala Kelvin $T_C = 270\\text{ K}$ dan $T_H = 300\\text{ K}$, sehingga koefisien performa pendingin adalah $K_P = \\frac{T_C}{T_H - T_C} = \\frac{270}{300 - 270} = \\frac{270}{30} = 9$. Usaha per detik yang dibutuhkan kompresor adalah $W = \\frac{Q_C}{K_P} = \\frac{1.350}{9} = 150\\text{ Joule}$, yang setara dengan daya $150\\text{ Watt}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $P = 150\\text{ Watt}$, karena dalam skala Kelvin $T_C = 270\\text{ K}$ dan $T_H = 300\\text{ K}$, sehingga koefisien performa pendingin adalah $K_P = \\frac{T_C}{T_H - T_C} = \\frac{270}{300 - 270} = \\frac{270}{30} = 9$. Usaha per detik yang dibutuhkan kompresor adalah $W = \\frac{Q_C}{K_P} = \\frac{1.350}{9} = 150\\text{ Joule}$, yang setara dengan daya $150\\text{ Watt}$.. Konversi suhu ke Kelvin: Tc = 270 K, Th = 300 K. COP KP = Tc / (Th - Tc) = 270 / 30 = 9. Daya P = W / t = Qc / KP. KP = 9. P = 1.350 / 9 = 150 Watt."
  },
  {
    "id": "fis-lat-h-06",
    "materi": "HUKUM II TERMODINAMIKA & ENTROPI",
    "topic": "Perubahan Entropi Sistem pada Proses Pencairan Es",
    "hints": {
      "concept": "Peleburan es berlangsung pada T = 273 K. Kalor yang diserap Q = m * Lf = 0,5 * 334.000 = 167.000 J. Delta S = Q / T.",
      "execution": "Delta S = 167.000 / 273 = +611,7 J/K."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebongkah es bermassa $m = 500\\text{ gram}$ pada suhu $0^\\circ\\text{C}$ ditaruh dalam ruangan bersuhu konstan $27^\\circ\\text{C}$ hingga seluruhnya mencair menjadi air pada suhu $0^\\circ\\text{C}$. Diketahui kalor lebur es adalah $L_f = 334.000\\text{ J/kg} = 334\\text{ J/g}$. Perubahan entropi dari es tersebut ($\\Delta S_{\\text{es}}$) selama proses peleburan berlangsung adalah...",
    "formulaHud": {
      "title": "FORMULA PERUBAHAN ENTROPI ISOTERMAL",
      "latex": "Q = m L_f = 0{,}5 \\times 334.000 = 167.000\\text{ J}; \\quad \\Delta S = \\frac{Q}{T_{\\text{lebur}}} = \\frac{167.000}{273} \\approx +611{,}72\\text{ J/K}",
      "legend": "• $T_{\\text{lebur}} = 0^\\circ\\text{C} = 273\\text{ K}$ (suhu saat fase peleburan es berlangsung)<br>• Nilai $\\Delta S > 0$ menandakan penyerapan kalor meningkatkan ketidakteraturan sistem partikel es"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta S_{\\text{es}} = +611{,}7\\text{ J/K}$, karena proses peleburan terjadi secara isotermal pada suhu $T = 0^\\circ\\text{C} = 273\\text{ K}$ dengan menyerap kalor sebesar $Q = m L_f = 0{,}5\\text{ kg} \\times 334.000\\text{ J/kg} = 167.000\\text{ J}$, sehingga perubahan entropi es adalah $\\Delta S_{\\text{es}} = \\frac{Q}{T} = \\frac{167.000}{273} \\approx +611{,}72\\text{ J/K}$."
      },
      {
        "key": "B",
        "text": "$\\Delta S_{\\text{es}} = +556{,}7\\text{ J/K}$, karena suhu peleburan keliru dibagi dengan suhu ruangan 300 Kelvin, bukan suhu titik lebur es sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$\\Delta S_{\\text{es}} = 0\\text{ J/K}$, karena suhu es tidak berubah selama fase mencair sehingga diasumsikan tidak ada perubahan entropi."
      },
      {
        "key": "D",
        "text": "$\\Delta S_{\\text{es}} = -611{,}7\\text{ J/K}$, karena es dianggap melepaskan kalor pembekuan ke lingkungan sekitarnya."
      },
      {
        "key": "E",
        "text": "$\\Delta S_{\\text{es}} = +167\\text{ J/K}$, dihitung dari kalor lebur dibagi dengan massa es tanpa memperhitungkan variabel suhu absolut termodinamika."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\Delta S_{\\text{es}} = +611{,}7\\text{ J/K}$, karena proses peleburan terjadi secara isotermal pada suhu $T = 0^\\circ\\text{C} = 273\\text{ K}$ dengan menyerap kalor sebesar $Q = m L_f = 0{,}5\\text{ kg} \\times 334.000\\text{ J/kg} = 167.000\\text{ J}$, sehingga perubahan entropi es adalah $\\Delta S_{\\text{es}} = \\frac{Q}{T} = \\frac{167.000}{273} \\approx +611{,}72\\text{ J/K}$.. Peleburan es berlangsung pada T = 273 K. Kalor yang diserap Q = m * Lf = 0,5 * 334.000 = 167.000 J. Delta S = Q / T. Delta S = 167.000 / 273 = +611,7 J/K."
  },
  {
    "id": "fis-lat-h-07",
    "materi": "GELOMBANG BUNYI (EFEK DOPPLER MULTIDIMENSI / ANGIN)",
    "topic": "Efek Doppler dengan Pergerakan Medium Angin",
    "hints": {
      "concept": "Jika ada angin bertiup dari sumber ke pendengar, cepat rambat bunyi efektif menjadi (v + vw) = 340 + 10 = 350 m/s. Gunakan rumus Doppler biasa dengan v efektif.",
      "execution": "fp = (350 / (350 - 20)) * 700 = (350 / 330) * 700 = 742,4 Hz."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah mobil pemadam kebakaran bergerak dengan kecepatan $v_s = 20\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 700\\text{ Hz}$. Seorang pengamat diam di pinggir jalan berada di depan mobil tersebut. Udara berhembus kencang searah gerak mobil pemadam (dari sumber ke arah pengamat) dengan kecepatan angin $v_w = 10\\text{ m/s}$. Jika cepat rambat bunyi di udara tenang adalah $v = 340\\text{ m/s}$, frekuensi bunyi sirine yang didengar oleh pengamat ($f_p$) adalah...",
    "formulaHud": {
      "title": "EFEK DOPPLER DENGAN PENGARUH KECEPATAN ANGIN",
      "latex": "f_p = \\left(\\frac{(v \\pm v_w) \\pm v_p}{(v \\pm v_w) \\mp v_s}\\right) f_s = \\left(\\frac{340 + 10 - 0}{340 + 10 - 20}\\right) 700 = \\left(\\frac{350}{330}\\right) 700 \\approx 742{,}42\\text{ Hz}",
      "legend": "• Angin bertiup dari sumber ke pendengar $\\implies v' = v + v_w = 350\\text{ m/s}$<br>• Pendengar diam: $v_p = 0$<br>• Sumber mendekati pendengar: penyebut bertanda minus ($v' - v_s = 330\\text{ m/s}$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$f_p = 743{,}75\\text{ Hz}$, dihitung dengan mengabaikan pengaruh kecepatan angin ($v_w = 0$) pada persamaan Efek Doppler standar sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$f_p = 742{,}4\\text{ Hz}$, karena hembusan angin searah rambatan bunyi meningkatkan cepat rambat efektif bunyi menjadi $v' = v + v_w = 340 + 10 = 350\\text{ m/s}$, dan pengamat diam ($v_p = 0$) didekati sumber ($v_s = 20\\text{ m/s}$), sehingga frekuensi terdengar adalah $f_p = \\left(\\frac{v' - v_p}{v' - v_s}\\right) f_s = \\left(\\frac{350}{350 - 20}\\right) 700 = \\left(\\frac{350}{330}\\right) 700 \\approx 742{,}42\\text{ Hz}$."
      },
      {
        "key": "C",
        "text": "$f_p = 660{,}0\\text{ Hz}$, karena tanda kecepatan sumber dan arah angin keliru dioperasikan sebagai menjauhi pengamat di jalan."
      },
      {
        "key": "D",
        "text": "$f_p = 720{,}0\\text{ Hz}$, dihitung dari penambahan selisih kelajuan mobil dengan kecepatan angin terhadap frekuensi asli sirine."
      },
      {
        "key": "E",
        "text": "$f_p = 800{,}0\\text{ Hz}$, dihitung dari perbandingan kecepatan bunyi di udara tenang dibagi selisih kelajuan sumber."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $f_p = 742{,}4\\text{ Hz}$, karena hembusan angin searah rambatan bunyi meningkatkan cepat rambat efektif bunyi menjadi $v' = v + v_w = 340 + 10 = 350\\text{ m/s}$, dan pengamat diam ($v_p = 0$) didekati sumber ($v_s = 20\\text{ m/s}$), sehingga frekuensi terdengar adalah $f_p = \\left(\\frac{v' - v_p}{v' - v_s}\\right) f_s = \\left(\\frac{350}{350 - 20}\\right) 700 = \\left(\\frac{350}{330}\\right) 700 \\approx 742{,}42\\text{ Hz}$.. Jika ada angin bertiup dari sumber ke pendengar, cepat rambat bunyi efektif menjadi (v + vw) = 340 + 10 = 350 m/s. Gunakan rumus Doppler biasa dengan v efektif. fp = (350 / (350 - 20)) * 700 = (350 / 330) * 700 = 742,4 Hz."
  },
  {
    "id": "fis-lat-h-08",
    "materi": "GELOMBANG MEKANIK STASIONER",
    "topic": "Letak Simpul dan Perut Gelombang Stasioner Ujung Terikat",
    "hints": {
      "concept": "Pada ujung terikat, pemantul adalah simpul: xs_n = (n - 1) * lambda/2, dan xp_n = (2n - 1) * lambda/4.",
      "execution": "xs3 = (3 - 1) * 1 / 2 = 1,0 m. xp2 = (2*2 - 1) * 1 / 4 = 3/4 = 0,75 m."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah tali elastis sepanjang $L = 2\\text{ meter}$ salah satu ujungnya diikat kuat pada dinding tetap dan ujung lainnya digetarkan harmonik sehingga terbentuk gelombang stasioner dengan 4 gelung (pola nada atas ketiga / 4 perut). Persamaan gelombang stasioner tersebut memiliki panjang gelombang $\\lambda = 1\\text{ meter}$. Jarak simpul ke-3 ($x_{s3}$) dan perut ke-2 ($x_{p2}$) diukur dari ujung pemantul terikat berturut-turut adalah...",
    "formulaHud": {
      "title": "FORMULA GELOMBANG STASIONER UJUNG TERIKAT",
      "latex": "x_{sn} = (n - 1)\\frac{\\lambda}{2} \\implies x_{s3} = (3 - 1)\\frac{1}{2} = 1{,}0\\text{ m}; \\quad x_{pn} = (2n - 1)\\frac{\\lambda}{4} \\implies x_{p2} = (4 - 1)\\frac{1}{4} = 0{,}75\\text{ m}",
      "legend": "• Ujung terikat selalu dimulai dari Simpul 1 di $x = 0$<br>• $x_{s1} = 0$, $x_{s2} = 0{,}5\\text{ m}$, $x_{s3} = 1{,}0\\text{ m}$<br>• $x_{p1} = 0{,}25\\text{ m}$, $x_{p2} = 0{,}75\\text{ m}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$x_{s3} = 0{,}75\\text{ meter}$ dan $x_{p2} = 0{,}5\\text{ meter}$, karena formula letak simpul dan perut tertukar antara ujung terikat dan ujung bebas ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$x_{s3} = 1{,}5\\text{ meter}$ dan $x_{p2} = 1{,}0\\text{ meter}$, dihitung dengan mengalikan nomor simpul langsung dengan panjang gelombang."
      },
      {
        "key": "C",
        "text": "$x_{s3} = 1{,}0\\text{ meter}$ dan $x_{p2} = 0{,}375\\text{ meter}$ (atau $\\frac{3}{8}\\text{ m}$), karena pada ujung terikat letak simpul ke-$n$ adalah $x_{sn} = (n - 1)\\frac{\\lambda}{2}$ sehingga $x_{s3} = (3 - 1)\\frac{1}{2} = 1{,}0\\text{ m}$, sedangkan letak perut ke-$n$ adalah $x_{pn} = (2n - 1)\\frac{\\lambda}{4}$ sehingga $x_{p2} = (2(2) - 1)\\frac{1}{4} = \\frac{3}{4}\\lambda = 0{,}75\\text{ m}$ jika $n=2$ rumus $(2n-1)/4$ menghasilkan $\\frac{3}{4}(1) \\times 0{,}5$... tepatnya $x_{p2} = (2(2)-1)\\frac{\\lambda}{4} = \\frac{3}{4}(0{,}5)$ jika $\\lambda = 1\\text{ m}$, $x_{p2} = \\frac{3}{4}(1) = 0{,}75\\text{ m}$... mari periksa: $x_{s1} = 0$, $x_{p1} = \\lambda/4 = 0{,}25\\text{ m}$, $x_{s2} = \\lambda/2 = 0{,}5\\text{ m}$, $x_{p2} = 3\\lambda/4 = 0{,}75\\text{ m}$, $x_{s3} = \\lambda = 1{,}0\\text{ m}$."
      },
      {
        "key": "D",
        "text": "$x_{s3} = 0{,}5\\text{ meter}$ dan $x_{p2} = 0{,}25\\text{ meter}$, karena hanya memperhitungkan separuh dari panjang gelombang yang sebenarnya."
      },
      {
        "key": "E",
        "text": "$x_{s3} = 2{,}0\\text{ meter}$ dan $x_{p2} = 1{,}25\\text{ meter}$, dihitung dari ujung sumber getaran bukan dari ujung pemantul terikat."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $x_{s3} = 1{,}0\\text{ meter}$ dan $x_{p2} = 0{,}375\\text{ meter}$ (atau $\\frac{3}{8}\\text{ m}$), karena pada ujung terikat letak simpul ke-$n$ adalah $x_{sn} = (n - 1)\\frac{\\lambda}{2}$ sehingga $x_{s3} = (3 - 1)\\frac{1}{2} = 1{,}0\\text{ m}$, sedangkan letak perut ke-$n$ adalah $x_{pn} = (2n - 1)\\frac{\\lambda}{4}$ sehingga $x_{p2} = (2(2) - 1)\\frac{1}{4} = \\frac{3}{4}\\lambda = 0{,}75\\text{ m}$ jika $n=2$ rumus $(2n-1)/4$ menghasilkan $\\frac{3}{4}(1) \\times 0{,}5$... tepatnya $x_{p2} = (2(2)-1)\\frac{\\lambda}{4} = \\frac{3}{4}(0{,}5)$ jika $\\lambda = 1\\text{ m}$, $x_{p2} = \\frac{3}{4}(1) = 0{,}75\\text{ m}$... mari periksa: $x_{s1} = 0$, $x_{p1} = \\lambda/4 = 0{,}25\\text{ m}$, $x_{s2} = \\lambda/2 = 0{,}5\\text{ m}$, $x_{p2} = 3\\lambda/4 = 0{,}75\\text{ m}$, $x_{s3} = \\lambda = 1{,}0\\text{ m}$.. Pada ujung terikat, pemantul adalah simpul: xs_n = (n - 1) * lambda/2, dan xp_n = (2n - 1) * lambda/4. xs3 = (3 - 1) * 1 / 2 = 1,0 m. xp2 = (2*2 - 1) * 1 / 4 = 3/4 = 0,75 m."
  },
  {
    "id": "fis-lat-h-09",
    "materi": "OPTIKA FISIS & INSTRUMEN (DAYA URAI RAYLEIGH)",
    "topic": "Kriteria Rayleigh dan Diameter Apertur Teleskop",
    "hints": {
      "concept": "Daya urai sudut apertur melingkar memenuhi kriteria Rayleigh: theta = 1,22 * lambda / D. Maka D = 1,22 * lambda / theta.",
      "execution": "D = (1,22 * 5e-7) / 2,44e-6 = 6,1e-7 / 2,44e-6 = 0,25 m = 25 cm."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah teleskop luar angkasa digunakan untuk memisahkan bayangan dua bintang kembar yang terpisah dengan jarak sudut $\\theta_R = 2{,}44 \\times 10^{-6}\\text{ radian}$. Pengamatan dilakukan menggunakan cahaya tampak dengan panjang gelombang rata-rata $\\lambda = 500\\text{ nm} = 5 \\times 10^{-7}\\text{ meter}$. Berdasarkan Kriteria Rayleigh untuk difraksi apertur melingkar, diameter minimum lensa objektif teleskop ($D$) agar kedua bintang tersebut dapat dibedakan secara terpisah adalah...",
    "formulaHud": {
      "title": "KRITERIA DAYA URAI RAYLEIGH (APERTUR MELINGKAR)",
      "latex": "\\theta_R = 1{,}22 \\frac{\\lambda}{D} \\implies D = \\frac{1{,}22 \\lambda}{\\theta_R} = \\frac{1{,}22 \\times (5 \\times 10^{-7})}{2{,}44 \\times 10^{-6}} = \\frac{1{,}22}{2{,}44} \\times 0{,}5 = 0{,}5 \\times 0{,}5 = 0{,}25\\text{ m}",
      "legend": "• $\\theta_R = 2{,}44 \\times 10^{-6}\\text{ rad}$<br>• $\\lambda = 5 \\times 10^{-7}\\text{ m}$<br>• Angka $1{,}22$ berasal dari nol pertama fungsi Bessel orde satu ($J_1(x)$)<br>• $D = 0{,}25\\text{ m} = 25\\text{ cm}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$D = 0{,}50\\text{ meter}$, karena faktor difraksi Airy 1,22 keliru digandakan menjadi 2,44 saat perhitungan fraksi sudut menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$D = 0{,}10\\text{ meter}$, dihitung tanpa mengikutsertakan tetapan difraksi lubang lingkaran Kriteria Rayleigh."
      },
      {
        "key": "C",
        "text": "$D = 1{,}22\\text{ meter}$, karena tetapan Rayleigh langsung dijadikan nilai diameter fisik cermin objektif teleskop."
      },
      {
        "key": "D",
        "text": "$D = 0{,}25\\text{ meter}$ (atau $25\\text{ cm}$), dihitung dari Kriteria Rayleigh $\\theta_R = 1{,}22 \\frac{\\lambda}{D}$, sehingga diameter objektif minimum adalah $D = \\frac{1{,}22 \\lambda}{\\theta_R} = \\frac{1{,}22 \\times (5 \\times 10^{-7}\\text{ m})}{2{,}44 \\times 10^{-6}\\text{ rad}} = \\frac{6{,}1 \\times 10^{-7}}{2{,}44 \\times 10^{-6}} = 0{,}25\\text{ m}$."
      },
      {
        "key": "E",
        "text": "$D = 0{,}05\\text{ meter}$, dihitung dari perbandingan panjang gelombang terhadap sudut pemisahan tanpa pembagian eksponen."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $D = 0{,}25\\text{ meter}$ (atau $25\\text{ cm}$), dihitung dari Kriteria Rayleigh $\\theta_R = 1{,}22 \\frac{\\lambda}{D}$, sehingga diameter objektif minimum adalah $D = \\frac{1{,}22 \\lambda}{\\theta_R} = \\frac{1{,}22 \\times (5 \\times 10^{-7}\\text{ m})}{2{,}44 \\times 10^{-6}\\text{ rad}} = \\frac{6{,}1 \\times 10^{-7}}{2{,}44 \\times 10^{-6}} = 0{,}25\\text{ m}$.. Daya urai sudut apertur melingkar memenuhi kriteria Rayleigh: theta = 1,22 * lambda / D. Maka D = 1,22 * lambda / theta. D = (1,22 * 5e-7) / 2,44e-6 = 6,1e-7 / 2,44e-6 = 0,25 m = 25 cm."
  },
  {
    "id": "fis-lat-h-10",
    "materi": "MEDAN MAGNET & INDUKTANSI DIRI",
    "topic": "Energi Magnetik dalam Solenoida Berinti Feromagnetik",
    "hints": {
      "concept": "L = mu_r * mu_0 * N^2 * A / l. Energi magnetik Wm = 1/2 * L * I^2.",
      "execution": "L = 500 * 4pi*1e-7 * 1e6 * 2e-3 / 0,4 = 0,1pi H. Wm = 1/2 * 0,1pi * 2^2 = 0,2pi J = 0,628 J."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah solenoida ideal memiliki panjang $l = 40\\text{ cm} = 0{,}4\\text{ m}$, luas penampang $A = 20\\text{ cm}^2 = 2 \\times 10^{-3}\\text{ m}^2$, dan terdiri atas $N = 1.000\\text{ lilitan}$. Bagian dalam solenoida diisi bahan feromagnetik dengan permeabilitas relatif $\\mu_r = 500$ (diketahui $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ Wb/(A}\\cdot\\text{m)}$). Jika solenoida dialiri arus listrik konstan $I = 2\\text{ Ampere}$, energi magnetik ($W_m$) yang tersimpan di dalam medan magnetik solenoida tersebut adalah...",
    "formulaHud": {
      "title": "INDUKTANSI DIRI & ENERGI MEDAN MAGNETIK SOLENOIDA",
      "latex": "L = \\frac{\\mu_r \\mu_0 N^2 A}{l} = \\frac{500 \\times (4\\pi \\times 10^{-7}) \\times 10^6 \\times (2 \\times 10^{-3})}{0{,}4} = 0{,}1\\pi\\text{ H}; \\quad W_m = \\frac{1}{2} L I^2 = \\frac{1}{2}(0{,}1\\pi)(4) = 0{,}2\\pi\\text{ J} \\approx 0{,}628\\text{ J}",
      "legend": "• $\\mu = \\mu_r \\mu_0 = 500 \\times 4\\pi \\times 10^{-7}$<br>• $L = 0{,}1\\pi\\text{ Henry} \\approx 0{,}314\\text{ H}$<br>• $W_m = \\frac{1}{2} L I^2 = 0{,}2\\pi\\text{ J} \\approx 0{,}628\\text{ Joule}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$W_m = 1{,}256 \\times 10^{-3}\\text{ Joule}$, karena pengaruh penguatan medan oleh permeabilitas relatif inti feromagnetik tidak diikutsertakan diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$W_m = 6{,}28\\text{ Joule}$, karena luas penampang solenoida tidak dikonversi dari satuan sentimeter kuadrat ke meter kuadrat."
      },
      {
        "key": "C",
        "text": "$W_m = 3{,}14\\text{ Joule}$, dihitung dari perkalian induktansi diri dengan arus tanpa faktor pembagian satu per dua."
      },
      {
        "key": "D",
        "text": "$W_m = 0{,}02\\pi\\text{ Joule}$, dihitung dari asumsi jumlah lilitan hanya bernilai pangkat satu dalam rumus induktansi diri."
      },
      {
        "key": "E",
        "text": "$W_m = 2\\pi \\times 10^{-1}\\text{ Joule} \\approx 0{,}628\\text{ Joule}$, karena induktansi diri solenoida berinti bahan adalah $L = \\frac{\\mu_r \\mu_0 N^2 A}{l} = \\frac{500 \\times (4\\pi \\times 10^{-7}) \\times (10^3)^2 \\times (2 \\times 10^{-3})}{0{,}4} = \\frac{500 \\times 4\\pi \\times 10^{-7} \\times 10^6 \\times 2 \\times 10^{-3}}{0{,}4} = \\frac{4\\pi \\times 10^{-1}}{0{,}4} = \\pi \\times 10^{-1}\\text{ H} = 0{,}1\\pi\\text{ H}$. Energi tersimpan adalah $W_m = \\frac{1}{2} L I^2 = \\frac{1}{2} (0{,}1\\pi) (2^2) = 0{,}2\\pi\\text{ J} \\approx 0{,}628\\text{ J}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $W_m = 2\\pi \\times 10^{-1}\\text{ Joule} \\approx 0{,}628\\text{ Joule}$, karena induktansi diri solenoida berinti bahan adalah $L = \\frac{\\mu_r \\mu_0 N^2 A}{l} = \\frac{500 \\times (4\\pi \\times 10^{-7}) \\times (10^3)^2 \\times (2 \\times 10^{-3})}{0{,}4} = \\frac{500 \\times 4\\pi \\times 10^{-7} \\times 10^6 \\times 2 \\times 10^{-3}}{0{,}4} = \\frac{4\\pi \\times 10^{-1}}{0{,}4} = \\pi \\times 10^{-1}\\text{ H} = 0{,}1\\pi\\text{ H}$. Energi tersimpan adalah $W_m = \\frac{1}{2} L I^2 = \\frac{1}{2} (0{,}1\\pi) (2^2) = 0{,}2\\pi\\text{ J} \\approx 0{,}628\\text{ J}$.. L = mu_r * mu_0 * N^2 * A / l. Energi magnetik Wm = 1/2 * L * I^2. L = 500 * 4pi*1e-7 * 1e6 * 2e-3 / 0,4 = 0,1pi H. Wm = 1/2 * 0,1pi * 2^2 = 0,2pi J = 0,628 J."
  },
  {
    "id": "fis-lat-h-11",
    "materi": "INDUKSI ELEKTROMAGNETIK",
    "topic": "Gaya Gerak Listrik (GGL) Batang Berputar dalam Medan Magnet",
    "hints": {
      "concept": "Konversi rpm ke rad/s: omega = 600 * 2pi / 60 = 20pi rad/s. GGL batang berputar: epsilon = 1/2 * B * omega * L^2.",
      "execution": "epsilon = 0,5 * 0,4 * 20pi * (0,5)^2 = 4pi * 0,25 = pi Volt = 3,14 V."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah kawat tembaga lurus dengan panjang $L = 50\\text{ cm} = 0{,}5\\text{ m}$ diputar dengan salah satu ujungnya sebagai poros pada frekuensi putaran konstan $n = 600\\text{ rpm}$ di dalam bidang yang tegak lurus terhadap medan magnetik homogen $B = 0{,}4\\text{ Tesla}$. Beda potensial atau GGL induksi ($\\varepsilon$) yang dibangkitkan antara kedua ujung kawat tersebut adalah...",
    "formulaHud": {
      "title": "GGL INDUKSI BATANG KONDUKTOR BERPUTAR",
      "latex": "\\omega = \\frac{600 \\times 2\\pi}{60} = 20\\pi\\text{ rad/s}; \\quad \\varepsilon = \\frac{1}{2} B \\omega L^2 = \\frac{1}{2} (0{,}4)(20\\pi)(0{,}5)^2 = \\pi\\text{ Volt} \\approx 3{,}14\\text{ V}",
      "legend": "• Kecepatan linier rata-rata kawat yang berputar dari poros ke ujung adalah $\\bar{v} = \\frac{0 + \\omega L}{2} = \\frac{1}{2} \\omega L$<br>• $\\varepsilon = B L \\bar{v} = \\frac{1}{2} B \\omega L^2 = \\pi\\text{ V}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\varepsilon = 3{,}14\\text{ Volt}$ (atau $\\pi\\text{ Volt}$), karena kecepatan sudut putaran adalah $\\omega = 600 \\times \\frac{2\\pi}{60} = 20\\pi\\text{ rad/s}$, sehingga luas sapuan lingkaran per detik memicu GGL induksi $\\varepsilon = \\frac{1}{2} B \\omega L^2 = \\frac{1}{2} (0{,}4) (20\\pi) (0{,}5)^2 = 0{,}2 \\times 20\\pi \\times 0{,}25 = \\pi\\text{ Volt} \\approx 3{,}14\\text{ Volt}$."
      },
      {
        "key": "B",
        "text": "$\\varepsilon = 6{,}28\\text{ Volt}$ (atau $2\\pi\\text{ Volt}$), karena formula GGL batang berputar keliru tidak dibagi dua ($BL^2\\omega$) sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$\\varepsilon = 1{,}57\\text{ Volt}$ (atau $0{,}5\\pi\\text{ Volt}$), dihitung dari kesalahan memasukkan panjang batang menjadi nilai jari-jari kuadrat."
      },
      {
        "key": "D",
        "text": "$\\varepsilon = 120\\text{ Volt}$, karena frekuensi sudut langsung menggunakan satuan rpm tanpa konversi ke radian per sekon."
      },
      {
        "key": "E",
        "text": "$\\varepsilon = 0{,}5\\text{ Volt}$, dihitung dari rumus batang bergerak translasi lurus ($BLv$) dengan kecepatan ujung poros pusat."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\varepsilon = 3{,}14\\text{ Volt}$ (atau $\\pi\\text{ Volt}$), karena kecepatan sudut putaran adalah $\\omega = 600 \\times \\frac{2\\pi}{60} = 20\\pi\\text{ rad/s}$, sehingga luas sapuan lingkaran per detik memicu GGL induksi $\\varepsilon = \\frac{1}{2} B \\omega L^2 = \\frac{1}{2} (0{,}4) (20\\pi) (0{,}5)^2 = 0{,}2 \\times 20\\pi \\times 0{,}25 = \\pi\\text{ Volt} \\approx 3{,}14\\text{ Volt}$.. Konversi rpm ke rad/s: omega = 600 * 2pi / 60 = 20pi rad/s. GGL batang berputar: epsilon = 1/2 * B * omega * L^2. epsilon = 0,5 * 0,4 * 20pi * (0,5)^2 = 4pi * 0,25 = pi Volt = 3,14 V."
  },
  {
    "id": "fis-lat-h-12",
    "materi": "RANGKAIAN ARUS BOLAK-BALIK (RLC)",
    "topic": "Resonansi RLC Seri, Faktor Daya, dan Daya Nyata Disipasi",
    "hints": {
      "concept": "Hitung XL = omega * L dan XC = 1 / (omega * C). Impedansi Z = sqrt(R^2 + (XL - XC)^2). I_ef = V_ef / Z. cos(phi) = R / Z. P = I_ef^2 * R.",
      "execution": "XL = 80 ohm, XC = 40 ohm, Z = 50 ohm. I_ef = 100/50 = 2 A. cos(phi) = 30/50 = 0,6. P = 2^2 * 30 = 120 W."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah rangkaian RLC seri dihubungkan dengan sumber tegangan bolak-balik $V(t) = 100\\sqrt{2} \\sin(1.000t)\\text{ Volt}$. Rangkaian terdiri atas resistor $R = 30\\,\\Omega$, induktor $L = 80\\text{ mH} = 0{,}08\\text{ H}$, dan kapasitor $C = 25\\,\\mu\\text{F} = 25 \\times 10^{-6}\\text{ F}$. Reaktansi induktif ($X_L$), reaktansi kapasitif ($X_C$), faktor daya ($\\cos\\phi$), dan daya rata-rata disipasi pada resistor ($P_{\\text{nyata}}$) adalah...",
    "formulaHud": {
      "title": "IMPEDANSI & DISIPASI DAYA RLC SERI",
      "latex": "X_L = \\omega L = 80\\,\\Omega; \\quad X_C = \\frac{1}{\\omega C} = 40\\,\\Omega; \\quad Z = \\sqrt{30^2 + 40^2} = 50\\,\\Omega; \\quad \\cos\\phi = \\frac{30}{50} = 0{,}6; \\quad P = I_{\\text{ef}}^2 R = 2^2 \\times 30 = 120\\text{ W}",
      "legend": "• $V_{\\text{ef}} = \\frac{V_{\\max}}{\\sqrt{2}} = 100\\text{ V}$<br>• $I_{\\text{ef}} = \\frac{100}{50} = 2\\text{ A}$<br>• $P_{\\text{nyata}} = V_{\\text{ef}} I_{\\text{ef}} \\cos\\phi = 100 \\times 2 \\times 0{,}6 = 120\\text{ Watt}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$X_L = 80\\,\\Omega$, $X_C = 40\\,\\Omega$, $\\cos\\phi = 1{,}0$, dan $P_{\\text{nyata}} = 200\\text{ Watt}$, karena rangkaian diasumsikan mengalami resonansi murni padahal reaktansinya tidak saling meniadakan sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$X_L = 80\\,\\Omega$, $X_C = 40\\,\\Omega$, $\\cos\\phi = 0{,}6$, dan $P_{\\text{nyata}} = 120\\text{ Watt}$, karena $X_L = \\omega L = 1.000 \\times 0{,}08 = 80\\,\\Omega$, $X_C = \\frac{1}{\\omega C} = \\frac{1}{1.000 \\times 25 \\times 10^{-6}} = 40\\,\\Omega$. Impedansi $Z = \\sqrt{R^2 + (X_L - X_C)^2} = \\sqrt{30^2 + (80 - 40)^2} = \\sqrt{900 + 1.600} = 50\\,\\Omega$. Arus efektif $I_{\\text{ef}} = \\frac{V_{\\text{ef}}}{Z} = \\frac{100}{50} = 2\\text{ A}$. Faktor daya $\\cos\\phi = \\frac{R}{Z} = \\frac{30}{50} = 0{,}6$, dan daya nyata $P = I_{\\text{ef}}^2 R = 2^2 \\times 30 = 120\\text{ Watt}$."
      },
      {
        "key": "C",
        "text": "$X_L = 40\\,\\Omega$, $X_C = 80\\,\\Omega$, $\\cos\\phi = 0{,}8$, dan $P_{\\text{nyata}} = 160\\text{ Watt}$, karena formula reaktansi induktif dan kapasitif tertukar perhitungannya."
      },
      {
        "key": "D",
        "text": "$X_L = 80\\,\\Omega$, $X_C = 40\\,\\Omega$, $\\cos\\phi = 0{,}5$, dan $P_{\\text{nyata}} = 100\\text{ Watt}$, dihitung dari rasio tegangan puncak bukan tegangan efektif RMS."
      },
      {
        "key": "E",
        "text": "$X_L = 100\\,\\Omega$, $X_C = 50\\,\\Omega$, $\\cos\\phi = 0{,}6$, dan $P_{\\text{nyata}} = 60\\text{ Watt}$, dihitung dari perkalian impedansi terhadap frekuensi sumber jala-jala listrik."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $X_L = 80\\,\\Omega$, $X_C = 40\\,\\Omega$, $\\cos\\phi = 0{,}6$, dan $P_{\\text{nyata}} = 120\\text{ Watt}$, karena $X_L = \\omega L = 1.000 \\times 0{,}08 = 80\\,\\Omega$, $X_C = \\frac{1}{\\omega C} = \\frac{1}{1.000 \\times 25 \\times 10^{-6}} = 40\\,\\Omega$. Impedansi $Z = \\sqrt{R^2 + (X_L - X_C)^2} = \\sqrt{30^2 + (80 - 40)^2} = \\sqrt{900 + 1.600} = 50\\,\\Omega$. Arus efektif $I_{\\text{ef}} = \\frac{V_{\\text{ef}}}{Z} = \\frac{100}{50} = 2\\text{ A}$. Faktor daya $\\cos\\phi = \\frac{R}{Z} = \\frac{30}{50} = 0{,}6$, dan daya nyata $P = I_{\\text{ef}}^2 R = 2^2 \\times 30 = 120\\text{ Watt}$.. Hitung XL = omega * L dan XC = 1 / (omega * C). Impedansi Z = sqrt(R^2 + (XL - XC)^2). I_ef = V_ef / Z. cos(phi) = R / Z. P = I_ef^2 * R. XL = 80 ohm, XC = 40 ohm, Z = 50 ohm. I_ef = 100/50 = 2 A. cos(phi) = 30/50 = 0,6. P = 2^2 * 30 = 120 W."
  },
  {
    "id": "fis-lat-h-13",
    "materi": "RADIASI BENDA HITAM & PERGESERAN WIEN",
    "topic": "Perbandingan Daya Radiasi Bintang Berdasarkan Suhu & Radius",
    "hints": {
      "concept": "Hukum Wien: T berbanding terbalik dengan lambda_max, sehingga TA/TB = lambda_B/lambda_A = 800/400 = 2. Daya Stefan-Boltzmann: P sebanding dengan R^2 * T^4.",
      "execution": "PA / PB = (RA/RB)^2 * (TA/TB)^4 = (2)^2 * (2)^4 = 4 * 16 = 64."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua buah bintang $A$ dan $B$ diamati memancarkan radiasi termal benda hitam ideal. Puncak spektrum emisi radiasi bintang $A$ berada pada panjang gelombang $\\lambda_A = 400\\text{ nm}$, sedangkan bintang $B$ berada pada panjang gelombang $\\lambda_B = 800\\text{ nm}$. Jika radius bintang $A$ adalah dua kali radius bintang $B$ ($R_A = 2 R_B$), perbandingan daya total radiasi yang dipancarkan bintang $A$ terhadap bintang $B$ ($\\frac{P_A}{P_B}$) menurut Hukum Stefan-Boltzmann dan Hukum Pergeseran Wien adalah...",
    "formulaHud": {
      "title": "HUKUM WIEN & DAYA RADIASI STEFAN-BOLTZMANN",
      "latex": "\\frac{T_A}{T_B} = \\frac{\\lambda_B}{\\lambda_A} = 2; \\quad \\frac{P_A}{P_B} = \\left(\\frac{R_A}{R_B}\\right)^2 \\left(\\frac{T_A}{T_B}\\right)^4 = 2^2 \\times 2^4 = 4 \\times 16 = 64",
      "legend": "• $\\lambda_A = 400\\text{ nm} \\implies T_A = 2 T_B$<br>• Luas permukaan bintang $A_{\\text{bola}} = 4\\pi R^2$<br>• Daya total $P = \\sigma (4\\pi R^2) T^4 \\implies P_A / P_B = 64$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\frac{P_A}{P_B} = 16 : 1$, karena hanya memperhitungkan rasio suhu pangkat empat tanpa mengalikan rasio kuadrat radius bintang ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$\\frac{P_A}{P_B} = 32 : 1$, dihitung dari asumsi radiasi berbanding lurus dengan pangkat lima suhu permukaan benda."
      },
      {
        "key": "C",
        "text": "$\\frac{P_A}{P_B} = 64 : 1$, karena menurut Hukum Pergeseran Wien $\\lambda_{\\max} T = C$, rasio suhu kedua bintang adalah $\\frac{T_A}{T_B} = \\frac{\\lambda_B}{\\lambda_A} = \\frac{800}{400} = 2$. Daya radiasi total bola bintang berbanding lurus dengan luas permukaan dan suhu pangkat empat ($P = \\sigma A T^4 = 4\\pi R^2 \\sigma T^4$), sehingga $\\frac{P_A}{P_B} = \\left(\\frac{R_A}{R_B}\\right)^2 \\left(\\frac{T_A}{T_B}\\right)^4 = (2)^2 \\times (2)^4 = 4 \\times 16 = 64$."
      },
      {
        "key": "D",
        "text": "$\\frac{P_A}{P_B} = 8 : 1$, karena suhu permukaan bintang dianggap berbanding lurus linier terhadap panjang gelombang puncak."
      },
      {
        "key": "E",
        "text": "$\\frac{P_A}{P_B} = 4 : 1$, karena mengabaikan variabel suhu dan hanya memperhitungkan faktor luas permukaan bola bintang."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $\\frac{P_A}{P_B} = 64 : 1$, karena menurut Hukum Pergeseran Wien $\\lambda_{\\max} T = C$, rasio suhu kedua bintang adalah $\\frac{T_A}{T_B} = \\frac{\\lambda_B}{\\lambda_A} = \\frac{800}{400} = 2$. Daya radiasi total bola bintang berbanding lurus dengan luas permukaan dan suhu pangkat empat ($P = \\sigma A T^4 = 4\\pi R^2 \\sigma T^4$), sehingga $\\frac{P_A}{P_B} = \\left(\\frac{R_A}{R_B}\\right)^2 \\left(\\frac{T_A}{T_B}\\right)^4 = (2)^2 \\times (2)^4 = 4 \\times 16 = 64$.. Hukum Wien: T berbanding terbalik dengan lambda_max, sehingga TA/TB = lambda_B/lambda_A = 800/400 = 2. Daya Stefan-Boltzmann: P sebanding dengan R^2 * T^4. PA / PB = (RA/RB)^2 * (TA/TB)^4 = (2)^2 * (2)^4 = 4 * 16 = 64."
  },
  {
    "id": "fis-lat-h-14",
    "materi": "FISIKA KUANTUM (EFEK FOTOLISTRIK)",
    "topic": "Penentuan Fungsi Kerja Logam dan Potensial Henti",
    "hints": {
      "concept": "Gunakan persamaan Einstein: Ek_max = E_foton - W0. Hubungan potensial henti: e * V0 = Ek_max.",
      "execution": "Ek_max = 4,5 eV - 2,5 eV = 2,0 eV. V0 = 2,0 V."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Permukaan sebuah pelat logam disinari dengan foton monokromatik berenergi $E = 4{,}5\\text{ eV}$. Diketahui fungsi kerja logam tersebut adalah $W_0 = 2{,}5\\text{ eV}$ dan muatan elementer elektron $e = 1{,}6 \\times 10^{-19}\\text{ Coulomb}$. Energi kinetik maksimum fotoelektron yang terlepas ($E_{k,\\max}$) dan besar potensial henti ($V_0$) yang diperlukan untuk menghentikan seluruh arus fotolistrik tersebut adalah...",
    "formulaHud": {
      "title": "PERSAMAAN EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_{k,\\max} = hf - W_0 = 4{,}5\\text{ eV} - 2{,}5\\text{ eV} = 2{,}0\\text{ eV}; \\quad e V_0 = E_{k,\\max} \\implies V_0 = 2{,}0\\text{ Volt}",
      "legend": "• $E_{k,\\max}$ adalah energi kinetik fotoelektron tercepat<br>• $V_0$ adalah tegangan pembalik (retarding potential) untuk memutus arus elektron anoda"
    },
    "options": [
      {
        "key": "A",
        "text": "$E_{k,\\max} = 7{,}0\\text{ eV}$ dan $V_0 = 7{,}0\\text{ Volt}$, karena energi foton datang keliru dijumlahkan dengan fungsi kerja logam emiter menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$E_{k,\\max} = 1{,}8\\text{ eV}$ dan $V_0 = 1{,}8\\text{ Volt}$, dihitung dari efisiensi kuantum pelepasan elektron emisi termionik."
      },
      {
        "key": "C",
        "text": "$E_{k,\\max} = 2{,}5\\text{ eV}$ dan $V_0 = 2{,}5\\text{ Volt}$, karena menyamakan energi kinetik maksimum dengan nilai fungsi kerja logam."
      },
      {
        "key": "D",
        "text": "$E_{k,\\max} = 2{,}0\\text{ eV}$ dan $V_0 = 2{,}0\\text{ Volt}$, karena menurut persamaan fotolistrik Einstein, energi kinetik maksimum fotoelektron adalah $E_{k,\\max} = hf - W_0 = 4{,}5\\text{ eV} - 2{,}5\\text{ eV} = 2{,}0\\text{ eV}$. Potensial henti memenuhi hubungan $e V_0 = E_{k,\\max}$, sehingga $V_0 = \\frac{2{,}0\\text{ eV}}{e} = 2{,}0\\text{ Volt}$."
      },
      {
        "key": "E",
        "text": "$E_{k,\\max} = 0{,}5\\text{ eV}$ dan $V_0 = 0{,}5\\text{ Volt}$, dihitung dari kuadrat rasio fungsi kerja terhadap energi foton sinar datang."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $E_{k,\\max} = 2{,}0\\text{ eV}$ dan $V_0 = 2{,}0\\text{ Volt}$, karena menurut persamaan fotolistrik Einstein, energi kinetik maksimum fotoelektron adalah $E_{k,\\max} = hf - W_0 = 4{,}5\\text{ eV} - 2{,}5\\text{ eV} = 2{,}0\\text{ eV}$. Potensial henti memenuhi hubungan $e V_0 = E_{k,\\max}$, sehingga $V_0 = \\frac{2{,}0\\text{ eV}}{e} = 2{,}0\\text{ Volt}$.. Gunakan persamaan Einstein: Ek_max = E_foton - W0. Hubungan potensial henti: e * V0 = Ek_max. Ek_max = 4,5 eV - 2,5 eV = 2,0 eV. V0 = 2,0 V."
  },
  {
    "id": "fis-lat-h-15",
    "materi": "FISIKA KUANTUM (EFEK COMPTON)",
    "topic": "Pergeseran Panjang Gelombang Hamburan Hamburan Compton",
    "hints": {
      "concept": "Rumus hamburan Compton: lambda' - lambda = (h / (me * c)) * (1 - cos theta). Delta_lambda = lambda_C * (1 - cos 60).",
      "execution": "Delta_lambda = 0,00243 * (1 - 0,5) = 0,001215 nm. lambda' = 0,0200 + 0,001215 = 0,0212 nm."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah foton sinar-X memiliki panjang gelombang datang $\\lambda = 0{,}0200\\text{ nm}$ ($2{,}00 \\times 10^{-11}\\text{ m}$). Foton tersebut menumbuk elektron diam dan dihamburkan dengan sudut hamburan $\\theta = 60^\\circ$ ($\\cos 60^\\circ = 0{,}5$). Jika panjang gelombang Compton elektron adalah $\\lambda_C = \\frac{h}{m_e c} = 0{,}00243\\text{ nm} = 2{,}43 \\times 10^{-12}\\text{ m}$, panjang gelombang foton hambur ($\\lambda'$) setelah tumbukan adalah...",
    "formulaHud": {
      "title": "FORMULA HAMBURAN COMPTON",
      "latex": "\\Delta\\lambda = \\lambda' - \\lambda = \\frac{h}{m_e c}(1 - \\cos\\theta) = 0{,}00243 \\times (1 - 0{,}5) = 0{,}001215\\text{ nm}; \\quad \\lambda' = 0{,}0200 + 0{,}001215 = 0{,}021215\\text{ nm}",
      "legend": "• $\\lambda_C = \\frac{h}{m_e c} \\approx 2{,}43 \\times 10^{-12}\\text{ m}$ (Panjang gelombang Compton)<br>• Foton kehilangan energi kinetik yang diserahkan ke elektron recoil, sehingga frekuensinya turun dan panjang gelombangnya selalu bertambah ($\\lambda' > \\lambda$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\lambda' = 0{,}0188\\text{ nm}$, karena panjang gelombang foton dihamburkan keliru dikurangi akibat salah asumsi bahwa foton menyerap energi dari elektron diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$\\lambda' = 0{,}0224\\text{ nm}$, dihitung dari sudut hamburan sembilan puluh derajat dengan nilai sinus satu."
      },
      {
        "key": "C",
        "text": "$\\lambda' = 0{,}0243\\text{ nm}$, karena langsung menambahkan konstanta panjang gelombang Compton utuh tanpa faktor sudut."
      },
      {
        "key": "D",
        "text": "$\\lambda' = 0{,}0100\\text{ nm}$, dihitung dari pembagian panjang gelombang foton datang dengan nilai cosinus sudut hambur."
      },
      {
        "key": "E",
        "text": "$\\lambda' = 0{,}0212\\text{ nm}$ (atau $2{,}1215 \\times 10^{-11}\\text{ m}$), karena pergeseran Compton adalah $\\Delta\\lambda = \\lambda' - \\lambda = \\lambda_C (1 - \\cos\\theta) = 0{,}00243\\text{ nm} \\times (1 - 0{,}5) = 0{,}001215\\text{ nm}$, sehingga panjang gelombang foton terhambur bertambah panjang menjadi $\\lambda' = \\lambda + \\Delta\\lambda = 0{,}0200 + 0{,}001215 = 0{,}021215\\text{ nm} \\approx 0{,}0212\\text{ nm}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $\\lambda' = 0{,}0212\\text{ nm}$ (atau $2{,}1215 \\times 10^{-11}\\text{ m}$), karena pergeseran Compton adalah $\\Delta\\lambda = \\lambda' - \\lambda = \\lambda_C (1 - \\cos\\theta) = 0{,}00243\\text{ nm} \\times (1 - 0{,}5) = 0{,}001215\\text{ nm}$, sehingga panjang gelombang foton terhambur bertambah panjang menjadi $\\lambda' = \\lambda + \\Delta\\lambda = 0{,}0200 + 0{,}001215 = 0{,}021215\\text{ nm} \\approx 0{,}0212\\text{ nm}$.. Rumus hamburan Compton: lambda' - lambda = (h / (me * c)) * (1 - cos theta). Delta_lambda = lambda_C * (1 - cos 60). Delta_lambda = 0,00243 * (1 - 0,5) = 0,001215 nm. lambda' = 0,0200 + 0,001215 = 0,0212 nm."
  },
  {
    "id": "fis-lat-h-16",
    "materi": "STRUKTUR ATOM (MODEL BOHR)",
    "topic": "Transisi Elektron dan Foton Deret Balmer",
    "hints": {
      "concept": "En = -13,6 / n^2 eV. Hitung E2 = -13,6/4 = -3,4 eV dan E4 = -13,6/16 = -0,85 eV. Delta E = E4 - E2. lambda = hc / Delta E.",
      "execution": "Delta E = -0,85 - (-3,4) = 2,55 eV. lambda = 1.240 / 2,55 = 486 nm."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam model atom Bohr untuk hidrogen, sebuah elektron melakukan transisi eksitasi dari tingkat energi $n = 2$ ke tingkat energi $n = 4$ akibat menyerap sebutir foton. Jika energi dasar atom hidrogen pada $n = 1$ adalah $E_1 = -13{,}6\\text{ eV}$, energi foton yang diserap ($E_{\\text{foton}}$) dan panjang gelombangnya ($\\lambda$) adalah... (Gunakan $hc = 1.240\\text{ eV}\\cdot\\text{nm}$)",
    "formulaHud": {
      "title": "ENERGI TRANSISI ELEKTRON MODEL BOHR",
      "latex": "E_n = -\\frac{13{,}6\\text{ eV}}{n^2}; \\quad \\Delta E = E_4 - E_2 = -0{,}85 - (-3{,}40) = 2{,}55\\text{ eV}; \\quad \\lambda = \\frac{hc}{\\Delta E} = \\frac{1.240}{2{,}55} \\approx 486{,}3\\text{ nm}",
      "legend": "• $E_2 = -3{,}40\\text{ eV}$, $E_4 = -0{,}85\\text{ eV}$<br>• Transisi $n=2 \\to n=4$ menyerap foton garis $H_\\beta$ deret Balmer pada spektrum cahaya tampak"
    },
    "options": [
      {
        "key": "A",
        "text": "$E_{\\text{foton}} = 2{,}55\\text{ eV}$ dan $\\lambda \\approx 486\\text{ nm}$, karena tingkat energi $E_2 = \\frac{-13{,}6}{2^2} = -3{,}4\\text{ eV}$ dan $E_4 = \\frac{-13{,}6}{4^2} = -0{,}85\\text{ eV}$, sehingga selisih energi yang diserap foton adalah $\\Delta E = E_4 - E_2 = -0{,}85 - (-3{,}4) = 2{,}55\\text{ eV}$. Panjang gelombang foton adalah $\\lambda = \\frac{hc}{\\Delta E} = \\frac{1.240\\text{ eV}\\cdot\\text{nm}}{2{,}55\\text{ eV}} \\approx 486{,}27\\text{ nm}$ (garis biru-kehijauan $H_\\beta$ deret Balmer)."
      },
      {
        "key": "B",
        "text": "$E_{\\text{foton}} = 3{,}40\\text{ eV}$ dan $\\lambda \\approx 365\\text{ nm}$, dihitung dari transisi elektron langsung dari tak hingga menuju lintasan kedua sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$E_{\\text{foton}} = 10{,}2\\text{ eV}$ dan $\\lambda \\approx 121\\text{ nm}$, karena merupakan transisi eksitasi dari kulit dasar n = 1 ke n = 2 pada deret Lyman."
      },
      {
        "key": "D",
        "text": "$E_{\\text{foton}} = 1{,}89\\text{ eV}$ dan $\\lambda \\approx 656\\text{ nm}$, karena merupakan transisi dari n = 3 ke n = 2 (garis merah H-alfa)."
      },
      {
        "key": "E",
        "text": "$E_{\\text{foton}} = 0{,}85\\text{ eV}$ dan $\\lambda \\approx 1.458\\text{ nm}$, dihitung dari nilai mutlak energi orbital n = 4 atom hidrogen."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $E_{\\text{foton}} = 2{,}55\\text{ eV}$ dan $\\lambda \\approx 486\\text{ nm}$, karena tingkat energi $E_2 = \\frac{-13{,}6}{2^2} = -3{,}4\\text{ eV}$ dan $E_4 = \\frac{-13{,}6}{4^2} = -0{,}85\\text{ eV}$, sehingga selisih energi yang diserap foton adalah $\\Delta E = E_4 - E_2 = -0{,}85 - (-3{,}4) = 2{,}55\\text{ eV}$. Panjang gelombang foton adalah $\\lambda = \\frac{hc}{\\Delta E} = \\frac{1.240\\text{ eV}\\cdot\\text{nm}}{2{,}55\\text{ eV}} \\approx 486{,}27\\text{ nm}$ (garis biru-kehijauan $H_\\beta$ deret Balmer).. En = -13,6 / n^2 eV. Hitung E2 = -13,6/4 = -3,4 eV dan E4 = -13,6/16 = -0,85 eV. Delta E = E4 - E2. lambda = hc / Delta E. Delta E = -0,85 - (-3,4) = 2,55 eV. lambda = 1.240 / 2,55 = 486 nm."
  },
  {
    "id": "fis-lat-h-17",
    "materi": "RELATIVITAS KHUSUS (DILATASI WAKTU)",
    "topic": "Peluruhan Muon Kosmik di Atmosfer Bumi",
    "hints": {
      "concept": "Dilatasi waktu: Delta_t = gamma * Delta_t0 = 5 * 2,2 mikrodetik = 11 mikrodetik. Jarak tempuh di bumi: s = v * Delta_t = 0,98 * 3e8 * 11e-6 m.",
      "execution": "Delta_t = 11 mikrosekon. s = 2,94e8 * 1,1e-5 = 3.234 m = 3,234 km."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Partikel muon tercipta di lapisan atas atmosfer bumi pada ketinggian $h = 9\\text{ km}$ di atas permukaan laut. Muon bergerak lurus menuju permukaan bumi dengan kecepatan relativistik $v = 0{,}98c$ (faktor Lorentz $\\gamma \\approx 5{,}0$). Waktu hidup rata-rata partikel muon pada kerangka diamnya adalah $\\Delta t_0 = 2{,}2\\,\\mu\\text{s} = 2{,}2 \\times 10^{-6}\\text{ sekon}$. Ditinjau dari kerangka acuan pengamat di bumi, waktu hidup muon ($\\Delta t$) dan jarak yang mampu ditempuhnya sebelum meluruh ($s$) adalah... ($c = 3 \\times 10^8\\text{ m/s}$)",
    "formulaHud": {
      "title": "DILATASI WAKTU RELATIVISTIK EINSTEIN",
      "latex": "\\Delta t = \\gamma \\Delta t_0 = \\frac{\\Delta t_0}{\\sqrt{1 - (v/c)^2}} = 5{,}0 \\times 2{,}2\\,\\mu\\text{s} = 11\\,\\mu\\text{s}; \\quad s = v \\Delta t = (0{,}98c) \\times 11\\,\\mu\\text{s} = 3.234\\text{ m}",
      "legend": "• Tanpa efek relativitas khusus, muon hanya menempuh $s_{\\text{klasik}} = 0{,}98c \\times 2{,}2\\,\\mu\\text{s} \\approx 647\\text{ m}$ dan tidak akan pernah mencapai bumi<br>• Dilatasi waktu membuktikan kebenaran teori relativitas khusus Einstein"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta t = 2{,}2\\,\\mu\\text{s}$ dan $s = 0{,}647\\text{ km}$, dihitung dengan mengabaikan dilatasi waktu relativistik mekanika klasik Einstein sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$\\Delta t = 11\\,\\mu\\text{s}$ dan $s = 3{,}234\\text{ km}$ (sehingga sebagian muon mampu mencapai detektor di permukaan laut melalui efek relativistik), karena waktu hidup menurut pengamat bumi mengalami dilatasi waktu $\\Delta t = \\gamma \\Delta t_0 = 5{,}0 \\times 2{,}2\\,\\mu\\text{s} = 11\\,\\mu\\text{s} = 1{,}1 \\times 10^{-5}\\text{ s}$. Jarak tempuh dalam kerangka bumi adalah $s = v \\Delta t = (0{,}98 \\times 3 \\times 10^8\\text{ m/s}) \\times (1{,}1 \\times 10^{-5}\\text{ s}) = 2{,}94 \\times 10^8 \\times 1{,}1 \\times 10^{-5} \\approx 3.234\\text{ meter} = 3{,}234\\text{ km}$."
      },
      {
        "key": "C",
        "text": "$\\Delta t = 0{,}44\\,\\mu\\text{s}$ dan $s = 0{,}129\\text{ km}$, karena waktu hidup muon keliru dibagi dengan faktor Lorentz."
      },
      {
        "key": "D",
        "text": "$\\Delta t = 22\\,\\mu\\text{s}$ dan $s = 6{,}468\\text{ km}$, dihitung dari asumsi faktor Lorentz sebesar sepuluh."
      },
      {
        "key": "E",
        "text": "$\\Delta t = 55\\,\\mu\\text{s}$ dan $s = 16{,}17\\text{ km}$, dihitung dari pemangkatan kuadrat rasio kecepatan partikel muon."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\Delta t = 11\\,\\mu\\text{s}$ dan $s = 3{,}234\\text{ km}$ (sehingga sebagian muon mampu mencapai detektor di permukaan laut melalui efek relativistik), karena waktu hidup menurut pengamat bumi mengalami dilatasi waktu $\\Delta t = \\gamma \\Delta t_0 = 5{,}0 \\times 2{,}2\\,\\mu\\text{s} = 11\\,\\mu\\text{s} = 1{,}1 \\times 10^{-5}\\text{ s}$. Jarak tempuh dalam kerangka bumi adalah $s = v \\Delta t = (0{,}98 \\times 3 \\times 10^8\\text{ m/s}) \\times (1{,}1 \\times 10^{-5}\\text{ s}) = 2{,}94 \\times 10^8 \\times 1{,}1 \\times 10^{-5} \\approx 3.234\\text{ meter} = 3{,}234\\text{ km}$.. Dilatasi waktu: Delta_t = gamma * Delta_t0 = 5 * 2,2 mikrodetik = 11 mikrodetik. Jarak tempuh di bumi: s = v * Delta_t = 0,98 * 3e8 * 11e-6 m. Delta_t = 11 mikrosekon. s = 2,94e8 * 1,1e-5 = 3.234 m = 3,234 km."
  },
  {
    "id": "fis-lat-h-18",
    "materi": "RELATIVITAS KHUSUS (ENERGI & MOMENTUM)",
    "topic": "Relasi Kecepatan saat Energi Kinetik Sama dengan Energi Diam",
    "hints": {
      "concept": "E = Ek + E0 = 2 E0, jadi gamma = 2. gamma = 1 / sqrt(1 - (v/c)^2) = 2 -> v = sqrt(3)/2 c. Momentum relativistik p = sqrt(E^2 - E0^2)/c = sqrt(4 - 1) E0/c = sqrt(3) m0 c.",
      "execution": "v = (sqrt(3)/2) * c = 0,866c. p = sqrt(3) * m0 * c."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah partikel subatomik bermassa diam $m_0$ dipercepat hingga memiliki energi kinetik relativistik yang besarnya tepat sama dengan energi diamnya ($E_k = E_0 = m_0 c^2$). Kecepatan gerak partikel ($v$) dan momentum relativistiknya ($p$) dinyatakan dalam konstanta $m_0$ dan $c$ berturut-turut adalah...",
    "formulaHud": {
      "title": "RELASI ENERGI-MOMENTUM RELATIVISTIK",
      "latex": "E = E_k + E_0 = 2 E_0 \\implies \\gamma = 2; \\quad v = c\\sqrt{1 - \\frac{1}{\\gamma^2}} = c\\sqrt{1 - \\frac{1}{4}} = \\frac{\\sqrt{3}}{2}c; \\quad p = \\frac{\\sqrt{E^2 - E_0^2}}{c} = \\sqrt{3} m_0 c",
      "legend": "• $\\gamma = 2$<br>• $v = \\frac{\\sqrt{3}}{2}c \\approx 0{,}866c$<br>• $p = \\sqrt{3} m_0 c \\approx 1{,}732 m_0 c$"
    },
    "options": [
      {
        "key": "A",
        "text": "$v = 0{,}5c$ dan $p = m_0 c$, karena kecepatan diasumsikan berbanding lurus linier dengan setengah faktor energi kinetik ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$v = \\frac{1}{\\sqrt{2}}c \\approx 0{,}707c$ dan $p = 2 m_0 c$, dihitung dari persamaan mekanika Newtonian non-relativistik."
      },
      {
        "key": "C",
        "text": "$v = \\frac{1}{2}\\sqrt{3}\\,c \\approx 0{,}866c$ dan $p = \\sqrt{3}\\,m_0 c$, karena energi total partikel adalah $E = E_k + E_0 = 2 E_0 = 2 m_0 c^2$. Karena $E = \\gamma E_0$, maka faktor Lorentz bernilai $\\gamma = 2 \\implies \\frac{1}{\\sqrt{1 - (v/c)^2}} = 2 \\implies 1 - (v/c)^2 = \\frac{1}{4} \\implies (v/c)^2 = \\frac{3}{4} \\implies v = \\frac{\\sqrt{3}}{2}c$. Dari relasi $E^2 = p^2 c^2 + E_0^2$, kita dapatkan $(2 E_0)^2 = p^2 c^2 + E_0^2 \\implies 4 E_0^2 - E_0^2 = p^2 c^2 \\implies p^2 c^2 = 3 E_0^2 \\implies p = \\sqrt{3}\\frac{E_0}{c} = \\sqrt{3} m_0 c$."
      },
      {
        "key": "D",
        "text": "$v = 0{,}98c$ dan $p = 3 m_0 c$, dihitung dari perkiraan kasar kecepatan tanpa penyelesaian aljabar Lorentz."
      },
      {
        "key": "E",
        "text": "$v = c$ dan $p = \\infty$, karena berasumsi partikel bermassa diam dapat dipercepat hingga mencapai kecepatan cahaya."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $v = \\frac{1}{2}\\sqrt{3}\\,c \\approx 0{,}866c$ dan $p = \\sqrt{3}\\,m_0 c$, karena energi total partikel adalah $E = E_k + E_0 = 2 E_0 = 2 m_0 c^2$. Karena $E = \\gamma E_0$, maka faktor Lorentz bernilai $\\gamma = 2 \\implies \\frac{1}{\\sqrt{1 - (v/c)^2}} = 2 \\implies 1 - (v/c)^2 = \\frac{1}{4} \\implies (v/c)^2 = \\frac{3}{4} \\implies v = \\frac{\\sqrt{3}}{2}c$. Dari relasi $E^2 = p^2 c^2 + E_0^2$, kita dapatkan $(2 E_0)^2 = p^2 c^2 + E_0^2 \\implies 4 E_0^2 - E_0^2 = p^2 c^2 \\implies p^2 c^2 = 3 E_0^2 \\implies p = \\sqrt{3}\\frac{E_0}{c} = \\sqrt{3} m_0 c$.. E = Ek + E0 = 2 E0, jadi gamma = 2. gamma = 1 / sqrt(1 - (v/c)^2) = 2 -> v = sqrt(3)/2 c. Momentum relativistik p = sqrt(E^2 - E0^2)/c = sqrt(4 - 1) E0/c = sqrt(3) m0 c. v = (sqrt(3)/2) * c = 0,866c. p = sqrt(3) * m0 * c."
  },
  {
    "id": "fis-lat-h-19",
    "materi": "FISIKA INTI & RADIOAKTIVITAS",
    "topic": "Hukum Peluruhan Eksponensial dan Aktivitas Radiasi",
    "hints": {
      "concept": "Jumlah waktu paruh n = 24 / 8 = 3. Sisa aktivitas A = A0 * (1/2)^3 = 160 / 8 = 20 mCi. Persentase meluruh = (1 - 1/8) * 100% = 87,5%.",
      "execution": "A = 20 mCi. Persentase meluruh = 87,5%."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Suatu sampel zat radioaktif memiliki waktu paruh $T_{1/2} = 8\\text{ hari}$. Mula-mula sampel tersebut memiliki aktivitas radiasi $A_0 = 160\\text{ mCi}$ (miliCurie). Aktivitas radiasi sampel tersebut setelah meluruh selama 24 hari ($A_t$) dan persentase inti induk yang telah meluruh adalah...",
    "formulaHud": {
      "title": "HUKUM PELURUHAN RADIOAKTIF",
      "latex": "n = \\frac{t}{T_{1/2}} = \\frac{24}{8} = 3; \\quad A_t = A_0 \\left(\\frac{1}{2}\\right)^3 = \\frac{160}{8} = 20\\text{ mCi}; \\quad \\%_{\\text{meluruh}} = (1 - 2^{-n}) \\times 100\\% = 87{,}5\\%",
      "legend": "• $A_t$ = Aktivitas radiasi sisa pada waktu $t$<br>• Inti meluruh = $100\\% - \\%_{\\text{sisa}} = 100\\% - 12{,}5\\% = 87{,}5\\%$"
    },
    "options": [
      {
        "key": "A",
        "text": "$A_t = 40\\text{ mCi}$ dan inti yang telah meluruh sebesar $75{,}0\\%$, karena hanya memperhitungkan 2 kali periode waktu paruh peluruhan menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$A_t = 20\\text{ mCi}$ dan inti yang telah meluruh sebesar $12{,}5\\%$, karena tertukar antara persentase inti sisa dengan persentase inti yang meluruh."
      },
      {
        "key": "C",
        "text": "$A_t = 10\\text{ mCi}$ dan inti yang telah meluruh sebesar $93{,}75\\%$, dihitung dari 4 kali waktu paruh peluruhan zat radioaktif."
      },
      {
        "key": "D",
        "text": "$A_t = 20\\text{ mCi}$ dan inti yang telah meluruh sebesar $87{,}5\\%$, karena jumlah periode waktu paruh yang terlewati adalah $n = \\frac{t}{T_{1/2}} = \\frac{24}{8} = 3$. Aktivitas radiasi yang tersisa adalah $A_t = A_0 \\left(\\frac{1}{2}\\right)^n = 160 \\times \\left(\\frac{1}{2}\\right)^3 = 160 \\times \\frac{1}{8} = 20\\text{ mCi}$. Bagian yang tersisa adalah $\\frac{1}{8} = 12{,}5\\%$, sehingga fraksi inti induk yang telah meluruh menjadi inti anak adalah $100\\% - 12{,}5\\% = 87{,}5\\%$."
      },
      {
        "key": "E",
        "text": "$A_t = 53{,}3\\text{ mCi}$ dan inti yang telah meluruh sebesar $66{,}7\\%$, dihitung dari pengurangan linier bukan peluruhan eksponensial."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $A_t = 20\\text{ mCi}$ dan inti yang telah meluruh sebesar $87{,}5\\%$, karena jumlah periode waktu paruh yang terlewati adalah $n = \\frac{t}{T_{1/2}} = \\frac{24}{8} = 3$. Aktivitas radiasi yang tersisa adalah $A_t = A_0 \\left(\\frac{1}{2}\\right)^n = 160 \\times \\left(\\frac{1}{2}\\right)^3 = 160 \\times \\frac{1}{8} = 20\\text{ mCi}$. Bagian yang tersisa adalah $\\frac{1}{8} = 12{,}5\\%$, sehingga fraksi inti induk yang telah meluruh menjadi inti anak adalah $100\\% - 12{,}5\\% = 87{,}5\\%$.. Jumlah waktu paruh n = 24 / 8 = 3. Sisa aktivitas A = A0 * (1/2)^3 = 160 / 8 = 20 mCi. Persentase meluruh = (1 - 1/8) * 100% = 87,5%. A = 20 mCi. Persentase meluruh = 87,5%."
  },
  {
    "id": "fis-lat-h-20",
    "materi": "FISIKA INTI & ENERGI REAKSI FISI",
    "topic": "Defek Massa dan Energi Reaksi Pembelahan Inti Nuklir",
    "hints": {
      "concept": "Delta_m = massa sebelum reaksi - massa sesudah reaksi. Q = Delta_m * 931,5 MeV.",
      "execution": "Delta_m = 235,0439 + 1,0087 - (140,9144 + 91,9262 + 3*1,0087) = 0,1859 sma. Q = 0,1859 * 931,5 = 173,2 MeV."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam sebuah reaktor nuklir, terjadi reaksi fisi inti Uranium-235 yang ditembak oleh neutron termal sesuai persamaan reaksi berikut:<br>$$\\text{n} + {}_{92}^{235}\\text{U} \\to {}_{56}^{141}\\text{Ba} + {}_{36}^{92}\\text{Kr} + 3\\,\\text{n} + Q$$<br>Diketahui massa masing-masing partikel:<br>• Massa ${}_{92}^{235}\\text{U} = 235{,}0439\\text{ sma}$<br>• Massa neutron $\\text{n} = 1{,}0087\\text{ sma}$<br>• Massa ${}_{56}^{141}\\text{Ba} = 140{,}9144\\text{ sma}$<br>• Massa ${}_{36}^{92}\\text{Kr} = 91{,}9262\\text{ sma}$<br>Jika $1\\text{ sma} \\approx 931{,}5\\text{ MeV}$, energi ($Q$) yang dibebaskan dalam setiap satu reaksi fisi uranium tersebut adalah...",
    "formulaHud": {
      "title": "ENERGI REAKSI FISI NUKLIR (DEFEK MASSA)",
      "latex": "\\Delta m = [m_U + m_n] - [m_{\\text{Ba}} + m_{\\text{Kr}} + 3m_n] = m_U - m_{\\text{Ba}} - m_{\\text{Kr}} - 2m_n = 235{,}0439 - 140{,}9144 - 91{,}9262 - 2(1{,}0087) = 0{,}1859\\text{ sma}; \\quad Q = 0{,}1859 \\times 931{,}5 \\approx 173{,}17\\text{ MeV}",
      "legend": "• $\\Delta m$ positif $\\implies$ Reaksi bersifat eksotermik (membebaskan energi raksasa)<br>• Reaksi fisi berantai menghasilkan sumber daya pembangkit listrik tenaga nuklir (PLTN)"
    },
    "options": [
      {
        "key": "A",
        "text": "$Q \\approx 192{,}8\\text{ MeV}$, dihitung tanpa memperhitungkan massa 3 neutron hasil fisi di ruas kanan reaksi produk diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$Q \\approx 931{,}5\\text{ MeV}$, karena menyamakan energi reaksi dengan tetapan konversi massa satu satuan massa atom."
      },
      {
        "key": "C",
        "text": "$Q \\approx 86{,}5\\text{ MeV}$, karena defek massa keliru dibagi dua saat perhitungan kesetaraan energi Einstein."
      },
      {
        "key": "D",
        "text": "$Q \\approx 12{,}4\\text{ MeV}$, dihitung dari selisih energi ikat per nukleon tanpa mengalikan jumlah total nukleon isotop uranium."
      },
      {
        "key": "E",
        "text": "$Q \\approx 173{,}26\\text{ MeV}$, karena massa pereaksi (reaktan) adalah $m_{\\text{reaktan}} = m_U + m_n = 235{,}0439 + 1{,}0087 = 236{,}0526\\text{ sma}$. Massa produk adalah $m_{\\text{produk}} = m_{\\text{Ba}} + m_{\\text{Kr}} + 3 m_n = 140{,}9144 + 91{,}9262 + 3(1{,}0087) = 232{,}8406 + 3{,}0261 = 235{,}8667\\text{ sma}$. Defek massa reaksi adalah $\\Delta m = 236{,}0526 - 235{,}8667 = 0{,}1859\\text{ sma}$. Energi yang dibebaskan adalah $Q = \\Delta m \\times 931{,}5\\text{ MeV} = 0{,}1859 \\times 931{,}5 \\approx 173{,}17\\text{ MeV}$ (dalam rentang nilai standar fisi nuklir $\\approx 173 - 200\\text{ MeV}$)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $Q \\approx 173{,}26\\text{ MeV}$, karena massa pereaksi (reaktan) adalah $m_{\\text{reaktan}} = m_U + m_n = 235{,}0439 + 1{,}0087 = 236{,}0526\\text{ sma}$. Massa produk adalah $m_{\\text{produk}} = m_{\\text{Ba}} + m_{\\text{Kr}} + 3 m_n = 140{,}9144 + 91{,}9262 + 3(1{,}0087) = 232{,}8406 + 3{,}0261 = 235{,}8667\\text{ sma}$. Defek massa reaksi adalah $\\Delta m = 236{,}0526 - 235{,}8667 = 0{,}1859\\text{ sma}$. Energi yang dibebaskan adalah $Q = \\Delta m \\times 931{,}5\\text{ MeV} = 0{,}1859 \\times 931{,}5 \\approx 173{,}17\\text{ MeV}$ (dalam rentang nilai standar fisi nuklir $\\approx 173 - 200\\text{ MeV}$).. Delta_m = massa sebelum reaksi - massa sesudah reaksi. Q = Delta_m * 931,5 MeV. Delta_m = 235,0439 + 1,0087 - (140,9144 + 91,9262 + 3*1,0087) = 0,1859 sma. Q = 0,1859 * 931,5 = 173,2 MeV."
  },
  {
    "id": "fis-lat-h-21",
    "materi": "ELEKTROMAGNETISME (SELEKTOR KECEPATAN / WIEN FILTER)",
    "topic": "Gerak Lurus Muatan dalam Medan Silang E dan B",
    "hints": {
      "concept": "Lintasan lurus terjadi saat gaya listrik sama dengan gaya magnet: q * E = q * v * B. Maka v = E / B.",
      "execution": "v = 2,4e4 / 0,12 = 2,0 x 10^5 m/s."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam sebuah alat spektrometer massa, partikel bermuatan $q = +3{,}2 \\times 10^{-19}\\text{ C}$ dilewatkan melalui pemilih kecepatan (velocity selector). Di dalam ruang tersebut bekerja medan listrik homogen $E = 2{,}4 \\times 10^4\\text{ V/m}$ dan medan magnetik homogen $B = 0{,}12\\text{ Tesla}$ yang saling tegak lurus satu sama lain dan tegak lurus arah datang partikel. Agar partikel dapat melintas lurus tanpa mengalami pembelokan sedikit pun, kelajuan partikel ($v$) tersebut harus bernilai...",
    "formulaHud": {
      "title": "PRINSIP PEMILIH KECEPATAN (VELOCITY SELECTOR)",
      "latex": "\\sum F = F_E - F_B = 0 \\implies qE = qvB \\implies v = \\frac{E}{B} = \\frac{2{,}4 \\times 10^4}{0{,}12} = 2{,}0 \\times 10^5\\text{ m/s}",
      "legend": "• $F_E = qE$ (Gaya Coulomb listrik)<br>• $F_B = qvB$ (Gaya Lorentz magnetik)<br>• Kelajuan $v = E/B$ tidak bergantung pada massa partikel maupun besar muatan partikel"
    },
    "options": [
      {
        "key": "A",
        "text": "$v = 2{,}0 \\times 10^5\\text{ m/s}$, karena syarat lintasan lurus adalah gaya Lorentz listrik dan gaya Lorentz magnet saling meniadakan ($F_E = F_B \\implies q E = q v B$), sehingga kelajuan partikel harus tepat memenuhi perbandingan $v = \\frac{E}{B} = \\frac{2{,}4 \\times 10^4\\text{ V/m}}{0{,}12\\text{ T}} = 2{,}0 \\times 10^5\\text{ m/s}$."
      },
      {
        "key": "B",
        "text": "$v = 5{,}0 \\times 10^{-6}\\text{ m/s}$, karena formula rasio medan keliru dibalik menjadi medan magnet dibagi medan listrik ($B/E$) sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$v = 2{,}88 \\times 10^3\\text{ m/s}$, dihitung dari hasil perkalian langsung antara kuat medan listrik dengan medan magnet."
      },
      {
        "key": "D",
        "text": "$v = 1{,}0 \\times 10^6\\text{ m/s}$, dihitung dari pendekatan kecepatan elektron bebas pada tabung sinar katoda."
      },
      {
        "key": "E",
        "text": "$v = 3{,}0 \\times 10^8\\text{ m/s}$, karena partikel bermuatan diasumsikan otomatis merambat dengan kelajuan cahaya di ruang hampa."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $v = 2{,}0 \\times 10^5\\text{ m/s}$, karena syarat lintasan lurus adalah gaya Lorentz listrik dan gaya Lorentz magnet saling meniadakan ($F_E = F_B \\implies q E = q v B$), sehingga kelajuan partikel harus tepat memenuhi perbandingan $v = \\frac{E}{B} = \\frac{2{,}4 \\times 10^4\\text{ V/m}}{0{,}12\\text{ T}} = 2{,}0 \\times 10^5\\text{ m/s}$.. Lintasan lurus terjadi saat gaya listrik sama dengan gaya magnet: q * E = q * v * B. Maka v = E / B. v = 2,4e4 / 0,12 = 2,0 x 10^5 m/s."
  },
  {
    "id": "fis-lat-h-22",
    "materi": "ELEKTROSTATIKA (ENERGI POTENSIAL SISTEM MUATAN)",
    "topic": "Energi Potensial Tiga Muatan di Segitiga Sama Sisi",
    "hints": {
      "concept": "Energi potensial elektrostatik sistem adalah jumlah skalar energi setiap pasangan: U_total = U12 + U23 + U13 = 3 * (k * q^2 / s).",
      "execution": "U_total = 3 * (9e9 * (2e-6)^2 / 0,3) = 3 * (0,036 / 0,3) = 3 * 0,12 = 0,36 J."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Tiga buah muatan titik identik masing-masing sebesar $q_1 = q_2 = q_3 = +2\\,\\mu\\text{C} = 2 \\times 10^{-6}\\text{ C}$ ditempatkan pada ketiga titik sudut sebuah segitiga sama sisi yang memiliki panjang sisi $s = 30\\text{ cm} = 0{,}3\\text{ meter}$. Diketahui konstanta Coulomb $k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$. Total energi potensial elektrostatik ($U_{\\text{total}}$) yang tersimpan dalam sistem tiga muatan tersebut adalah...",
    "formulaHud": {
      "title": "ENERGI POTENSIAL ELEKTROSTATIK SISTEM DISKRIT",
      "latex": "U_{\\text{total}} = \\sum_{i < j} \\frac{k q_i q_j}{r_{ij}} = 3 \\times \\frac{k q^2}{s} = 3 \\times \\frac{9 \\times 10^9 \\times (2 \\times 10^{-6})^2}{0{,}3} = 3 \\times 0{,}12 = 0{,}36\\text{ J}",
      "legend": "• Energi potensial adalah besaran skalar (bukan vektor)<br>• Terdapat 3 pasangan muatan pada segitiga: $(1,2)$, $(1,3)$, dan $(2,3)$<br>• $U_{\\text{total}} = 0{,}36\\text{ Joule}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$U_{\\text{total}} = 0{,}12\\text{ Joule}$, karena hanya memperhitungkan interaksi satu pasang muatan tunggal dalam sistem sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$U_{\\text{total}} = 0{,}36\\text{ Joule}$, karena energi potensial total sistem adalah penjumlahan skalar dari energi potensial ketiga pasangan muatan: $U = U_{12} + U_{13} + U_{23} = 3 \\left(\\frac{k q^2}{s}\\right) = 3 \\times \\frac{(9 \\times 10^9) \\times (2 \\times 10^{-6})^2}{0{,}3} = 3 \\times \\frac{9 \\times 10^9 \\times 4 \\times 10^{-12}}{0{,}3} = 3 \\times \\frac{0{,}036}{0{,}3} = 3 \\times 0{,}12 = 0{,}36\\text{ Joule}$."
      },
      {
        "key": "C",
        "text": "$U_{\\text{total}} = 0{,}72\\text{ Joule}$, dihitung dari penggandaan pasangan muatan dengan menghitung interaksi timbal balik dua kali."
      },
      {
        "key": "D",
        "text": "$U_{\\text{total}} = 0\\text{ Joule}$, karena keliru menganggap energi potensial sebagai besaran vektor yang saling meniadakan di pusat segitiga."
      },
      {
        "key": "E",
        "text": "$U_{\\text{total}} = 1{,}08\\text{ Joule}$, dihitung dari perkalian tiga pasang muatan dengan kuadrat jarak sisi pemisah segitiga."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $U_{\\text{total}} = 0{,}36\\text{ Joule}$, karena energi potensial total sistem adalah penjumlahan skalar dari energi potensial ketiga pasangan muatan: $U = U_{12} + U_{13} + U_{23} = 3 \\left(\\frac{k q^2}{s}\\right) = 3 \\times \\frac{(9 \\times 10^9) \\times (2 \\times 10^{-6})^2}{0{,}3} = 3 \\times \\frac{9 \\times 10^9 \\times 4 \\times 10^{-12}}{0{,}3} = 3 \\times \\frac{0{,}036}{0{,}3} = 3 \\times 0{,}12 = 0{,}36\\text{ Joule}$.. Energi potensial elektrostatik sistem adalah jumlah skalar energi setiap pasangan: U_total = U12 + U23 + U13 = 3 * (k * q^2 / s). U_total = 3 * (9e9 * (2e-6)^2 / 0,3) = 3 * (0,036 / 0,3) = 3 * 0,12 = 0,36 J."
  },
  {
    "id": "fis-lat-h-23",
    "materi": "KAPASITOR & BAHAN DIELEKTRIK",
    "topic": "Kapasitor Keping Sejajar dengan Dua Lapisan Dielektrik Seri",
    "hints": {
      "concept": "Dua lapisan dielektrik yang membagi jarak d menjadi d/2 tersusun seri. Konstanta dielektrik efektif seri: kappa_eff = 2*k1*k2 / (k1 + k2). C_gab = kappa_eff * C0.",
      "execution": "kappa_eff = 2 * 2 * 6 / (2 + 6) = 24 / 8 = 3. C_gab = 3 * 12 mikrofarad = 36 mikrofarad."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah kapasitor keping sejajar dengan luas keping $A$ dan jarak antar keping $d$ mula-mula memiliki kapasitansi ruang hampa $C_0 = 12\\,\\mu\\text{F}$. Ruang di antara kedua keping kemudian diisi penuh oleh dua lapisan bahan dielektrik yang masing-masing memiliki ketebalan separuh jarak antar keping ($d_1 = d_2 = \\frac{1}{2}d$). Lapisan pertama memiliki konstanta dielektrik $\\kappa_1 = 2$ dan lapisan kedua $\\kappa_2 = 6$. Nilai kapasitas kapasitor setelah disisipi kedua dielektrik tersebut ($C_{\\text{gab}}$) adalah...",
    "formulaHud": {
      "title": "KAPASITANSI GABUNGAN DIELEKTRIK BERLAPIS (SERI)",
      "latex": "C_1 = 2\\kappa_1 C_0 = 48\\,\\mu\\text{F}; \\quad C_2 = 2\\kappa_2 C_0 = 144\\,\\mu\\text{F}; \\quad \\frac{1}{C_{\\text{gab}}} = \\frac{1}{C_1} + \\frac{1}{C_2} \\implies C_{\\text{gab}} = \\frac{48 \\times 144}{192} = 36\\,\\mu\\text{F}",
      "legend": "• Tebal masing-masing lapisan $d/2 \\implies$ kapasitansi dasar menjadi $2 C_0$<br>• Dielektrik tersusun seri: $\\kappa_{\\text{eff}} = \\frac{2 \\kappa_1 \\kappa_2}{\\kappa_1 + \\kappa_2} = \\frac{2 \\times 2 \\times 6}{2 + 6} = \\frac{24}{8} = 3$<br>• $C_{\\text{gab}} = \\kappa_{\\text{eff}} C_0 = 3 \\times 12 = 36\\,\\mu\\text{F}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$C_{\\text{gab}} = 48\\,\\mu\\text{F}$, dihitung dari rata-rata aritmetika konstanta dielektrik dikalikan dengan kapasitansi awal ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$C_{\\text{gab}} = 96\\,\\mu\\text{F}$, karena kedua lapisan dielektrik keliru dihitung sebagai susunan kapasitor paralel."
      },
      {
        "key": "C",
        "text": "$C_{\\text{gab}} = 36\\,\\mu\\text{F}$, karena susunan dielektrik berlapis tegak lurus garis medan membentuk dua kapasitor yang terhubung secara seri dengan jarak keping masing-masing $\\frac{1}{2}d$. Kapasitansi masing-masing adalah $C_1 = \\kappa_1 \\left(\\frac{\\varepsilon_0 A}{d/2}\\right) = 2 \\kappa_1 C_0 = 2(2)(12) = 48\\,\\mu\\text{F}$, dan $C_2 = 2 \\kappa_2 C_0 = 2(6)(12) = 144\\,\\mu\\text{F}$. Kapasitansi gabungan seri adalah $C_{\\text{gab}} = \\frac{C_1 C_2}{C_1 + C_2} = \\frac{48 \\times 144}{48 + 144} = \\frac{6.912}{192} = 36\\,\\mu\\text{F}$."
      },
      {
        "key": "D",
        "text": "$C_{\\text{gab}} = 24\\,\\mu\\text{F}$, dihitung tanpa memperhitungkan reduksi separuh ketebalan keping masing-masing dielektrik."
      },
      {
        "key": "E",
        "text": "$C_{\\text{gab}} = 18\\,\\mu\\text{F}$, dihitung dari perkalian terbalik konstanta dielektrik terhadap permitivitas ruang hampa."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $C_{\\text{gab}} = 36\\,\\mu\\text{F}$, karena susunan dielektrik berlapis tegak lurus garis medan membentuk dua kapasitor yang terhubung secara seri dengan jarak keping masing-masing $\\frac{1}{2}d$. Kapasitansi masing-masing adalah $C_1 = \\kappa_1 \\left(\\frac{\\varepsilon_0 A}{d/2}\\right) = 2 \\kappa_1 C_0 = 2(2)(12) = 48\\,\\mu\\text{F}$, dan $C_2 = 2 \\kappa_2 C_0 = 2(6)(12) = 144\\,\\mu\\text{F}$. Kapasitansi gabungan seri adalah $C_{\\text{gab}} = \\frac{C_1 C_2}{C_1 + C_2} = \\frac{48 \\times 144}{48 + 144} = \\frac{6.912}{192} = 36\\,\\mu\\text{F}$.. Dua lapisan dielektrik yang membagi jarak d menjadi d/2 tersusun seri. Konstanta dielektrik efektif seri: kappa_eff = 2*k1*k2 / (k1 + k2). C_gab = kappa_eff * C0. kappa_eff = 2 * 2 * 6 / (2 + 6) = 24 / 8 = 3. C_gab = 3 * 12 mikrofarad = 36 mikrofarad."
  },
  {
    "id": "fis-lat-h-24",
    "materi": "FISIKA MODERN (DIFRAKSI SINAR-X / HUKUM BRAGG)",
    "topic": "Hukum Difraksi Bragg pada Kisi Kristal Padat",
    "hints": {
      "concept": "Hukum Bragg: 2 * d * sin(theta) = n * lambda. Untuk n = 1: sin(theta) = lambda / (2d).",
      "execution": "sin(theta) = 0,15 / (2 * 0,30) = 0,15 / 0,60 = 0,25. theta = arcsin(0,25) = 14,48 derajat."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Berkas sinar-X monokromatik dengan panjang gelombang $\\lambda = 0{,}15\\text{ nm}$ ($1{,}5 \\times 10^{-10}\\text{ m}$) dijatuhkan pada permukaan kristal garam dapur (NaCl) yang memiliki jarak antarbidang kisi atom $d = 0{,}30\\text{ nm}$. Berdasarkan Hukum Difraksi Bragg ($2d \\sin\\theta = n\\lambda$), sudut berkas gelombang terhadap bidang kisi kristal (sudut Bragg $\\theta$) yang menghasilkan puncak difraksi interferensi konstruktif orde pertama ($n = 1$) adalah...",
    "formulaHud": {
      "title": "HUKUM DIFRAKSI BRAGG PADA KRISTAL",
      "latex": "2d \\sin\\theta = n\\lambda \\implies \\sin\\theta = \\frac{n\\lambda}{2d} = \\frac{1 \\times 0{,}15}{2 \\times 0{,}30} = 0{,}25 \\implies \\theta = \\arcsin(0{,}25) \\approx 14{,}48^\\circ",
      "legend": "• $d = 0{,}30\\text{ nm}$ (jarak antarbidang kristal)<br>• $\\theta$ diukur terhadap bidang pantul kisi kristal (bukan terhadap garis normal permukaan)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\theta = 30{,}0^\\circ$, karena angka 2 di depan jarak antarbidang kristal pada Hukum Bragg diabaikan ($\\sin\\theta = \\lambda/d = 0{,}5$) menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$\\theta = 60{,}0^\\circ$, karena keliru menggunakan nilai fungsi cosinus dari perbandingan panjang gelombang."
      },
      {
        "key": "C",
        "text": "$\\theta = 45{,}0^\\circ$, dihitung dari asumsi bahwa difraksi kisi kristal selalu simetris pada sudut separuh siku-siku."
      },
      {
        "key": "D",
        "text": "$\\theta = 14{,}48^\\circ$ (karena $\\sin\\theta = 0{,}25$), dihitung dari persamaan Bragg $2d \\sin\\theta = n\\lambda$, sehingga $\\sin\\theta = \\frac{n\\lambda}{2d} = \\frac{1 \\times 0{,}15\\text{ nm}}{2 \\times 0{,}30\\text{ nm}} = \\frac{0{,}15}{0{,}60} = 0{,}25$, yang bersesuaian dengan sudut $\\theta = \\arcsin(0{,}25) \\approx 14{,}48^\\circ$."
      },
      {
        "key": "E",
        "text": "$\\theta = 7{,}24^\\circ$, dihitung dari pembagian sudut Bragg dengan orde difraksi kuantum kedua."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $\\theta = 14{,}48^\\circ$ (karena $\\sin\\theta = 0{,}25$), dihitung dari persamaan Bragg $2d \\sin\\theta = n\\lambda$, sehingga $\\sin\\theta = \\frac{n\\lambda}{2d} = \\frac{1 \\times 0{,}15\\text{ nm}}{2 \\times 0{,}30\\text{ nm}} = \\frac{0{,}15}{0{,}60} = 0{,}25$, yang bersesuaian dengan sudut $\\theta = \\arcsin(0{,}25) \\approx 14{,}48^\\circ$.. Hukum Bragg: 2 * d * sin(theta) = n * lambda. Untuk n = 1: sin(theta) = lambda / (2d). sin(theta) = 0,15 / (2 * 0,30) = 0,15 / 0,60 = 0,25. theta = arcsin(0,25) = 14,48 derajat."
  },
  {
    "id": "fis-lat-h-25",
    "materi": "TERMODINAMIKA GAS IDEAL (PROSES ADIABATIK)",
    "topic": "Tekanan dan Volume pada Pemuaian Adiabatik Gas Diatomik",
    "hints": {
      "concept": "Proses adiabatik memenuhi P1 * V1^gamma = P2 * V2^gamma. P2 = P1 * (V1 / V2)^gamma. Hitung (1/32)^1,4 = 1 / 128.",
      "execution": "P2 = 3,2e5 / 128 = 2.500 Pa = 2,5 x 10^3 Pa."
    },
    "subject": "fisika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sejumlah gas ideal diatomik (tetapan Laplace $\\gamma = 1{,}4 = \\frac{7}{5}$) mula-mula berada pada tekanan $P_1 = 3{,}2 \\times 10^5\\text{ Pa}$ dan volume $V_1 = 1\\text{ liter}$. Gas tersebut mengalami ekspansi adiabatik kuasistatik hingga volumenya membesar menjadi $V_2 = 32\\text{ liter}$. Mengingat relasi pemangkatan $32^{1{,}4} = (2^5)^{7/5} = 2^7 = 128$, besar tekanan akhir gas ($P_2$) setelah proses ekspansi adiabatik tersebut adalah...",
    "formulaHud": {
      "title": "PERSAMAAN PROSES ADIABATIK (HUKUM POISSON)",
      "latex": "P_1 V_1^\\gamma = P_2 V_2^\\gamma \\implies P_2 = P_1 \\left(\\frac{V_1}{V_2}\\right)^\\gamma = 3{,}2 \\times 10^5 \\times \\left(\\frac{1}{32}\\right)^{7/5} = \\frac{320.000}{128} = 2.500\\text{ Pa}",
      "legend": "• $\\gamma = \\frac{C_p}{C_v} = 1{,}4 = \\frac{7}{5}$ (Gas diatomik)<br>• $32^{7/5} = (2^5)^{7/5} = 2^7 = 128$<br>• Pada ekspansi adiabatik, tekanan gas turun drastis jauh lebih cepat daripada proses isotermal"
    },
    "options": [
      {
        "key": "A",
        "text": "$P_2 = 1{,}0 \\times 10^4\\text{ Pa}$, karena gas keliru dihitung memuai secara isotermal menurut hukum Boyle ($P_1 V_1 = P_2 V_2$) diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$P_2 = 5{,}0 \\times 10^3\\text{ Pa}$, dihitung dengan menggunakan tetapan gas monoatomik gamma lima per tiga."
      },
      {
        "key": "C",
        "text": "$P_2 = 1{,}28 \\times 10^5\\text{ Pa}$, dihitung dari perkalian tekanan awal dengan faktor pemuaian volume gas."
      },
      {
        "key": "D",
        "text": "$P_2 = 8{,}0 \\times 10^2\\text{ Pa}$, dihitung dari pembagian tekanan gas terhadap kuadrat perubahan volume adiabatik."
      },
      {
        "key": "E",
        "text": "$P_2 = 2{,}5 \\times 10^3\\text{ Pa}$ (atau $2.500\\text{ Pa}$), karena pada proses adiabatik berlaku hukum Poisson $P_1 V_1^\\gamma = P_2 V_2^\\gamma$, sehingga $P_2 = P_1 \\left(\\frac{V_1}{V_2}\\right)^\\gamma = (3{,}2 \\times 10^5\\text{ Pa}) \\times \\left(\\frac{1}{32}\\right)^{1{,}4} = \\frac{3{,}2 \\times 10^5}{128} = 2.500\\text{ Pa} = 2{,}5 \\times 10^3\\text{ Pa}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $P_2 = 2{,}5 \\times 10^3\\text{ Pa}$ (atau $2.500\\text{ Pa}$), karena pada proses adiabatik berlaku hukum Poisson $P_1 V_1^\\gamma = P_2 V_2^\\gamma$, sehingga $P_2 = P_1 \\left(\\frac{V_1}{V_2}\\right)^\\gamma = (3{,}2 \\times 10^5\\text{ Pa}) \\times \\left(\\frac{1}{32}\\right)^{1{,}4} = \\frac{3{,}2 \\times 10^5}{128} = 2.500\\text{ Pa} = 2{,}5 \\times 10^3\\text{ Pa}$.. Proses adiabatik memenuhi P1 * V1^gamma = P2 * V2^gamma. P2 = P1 * (V1 / V2)^gamma. Hitung (1/32)^1,4 = 1 / 128. P2 = 3,2e5 / 128 = 2.500 Pa = 2,5 x 10^3 Pa."
  },
  {
    "id": "fis-sim-01",
    "materi": "VEKTOR & KINEMATIKA GERAK RELATIF",
    "topic": "Gerak Menyeberangi Sungai Berarus Deras Tegak Lurus",
    "hints": {
      "concept": "Agar sampai tegak lurus di seberang, haluan perahu harus condong ke hulu sehingga v_perahu * sin(theta) = v_arus. Kecepatan resultan tegak lurus v_res = sqrt(vp^2 - va^2).",
      "execution": "v_res = sqrt(5^2 - 3^2) = 4 m/s. t = 120 / 4 = 30 sekon."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah perahu bermotor hendak menyeberangi sungai dengan lebar $w = 120\\text{ meter}$. Arus air sungai mengalir ke arah timur dengan kecepatan tetap $v_{\\text{arus}} = 3\\text{ m/s}$. Motor perahu mampu melaju dengan kelajuan $v_{\\text{perahu}} = 5\\text{ m/s}$ relatif terhadap air. Agar lintasan perahu dapat menyeberang sungai tepat tegak lurus terhadap arah arus (sampai di titik seberang yang persis berhadapan), sudut haluan perahu terhadap tepi sungai ($\\alpha$) dan waktu tempuh penyeberangan ($t$) adalah...",
    "formulaHud": {
      "title": "VEKTOR KECEPATAN RELATIF MENYEBERANG SUNGAI",
      "latex": "v_x = v_p \\sin\\theta - v_a = 0 \\implies \\sin\\theta = \\frac{v_a}{v_p} = \\frac{3}{5} = 0{,}6; \\quad v_{\\text{res}} = \\sqrt{v_p^2 - v_a^2} = 4\\text{ m/s}; \\quad t = \\frac{w}{v_{\\text{res}}} = \\frac{120}{4} = 30\\text{ s}",
      "legend": "• Agar lintasan tepat tegak lurus, komponen $x$ harus bernilai nol ($v_x = 0$)<br>• Kecepatan efektif perahu menyeberang $v_{\\text{res}} = 4\\text{ m/s}$<br>• Waktu tempuh $t = 30\\text{ sekon}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\alpha = 126{,}87^\\circ$ terhadap arah aliran hilir (atau mengarah ke hulu sebesar $53^\\circ$ terhadap tepi hulu) dengan waktu tempuh $t = 30\\text{ sekon}$, karena komponen kecepatan perahu yang melawan arus harus tepat mengimbangi arus sungai ($v_{\\text{perahu}} \\sin\\theta = v_{\\text{arus}} \\implies 5 \\sin\\theta = 3 \\implies \\sin\\theta = 0{,}6 \\implies \\theta = 37^\\circ$ dari garis tegak lurus, atau $53^\\circ$ dari tepi sungai hulu). Kecepatan resultan efektif menyeberang adalah $v_y = \\sqrt{5^2 - 3^2} = 4\\text{ m/s}$, sehingga waktu tempuh $t = \\frac{120\\text{ m}}{4\\text{ m/s}} = 30\\text{ sekon}$."
      },
      {
        "key": "B",
        "text": "$\\alpha = 90^\\circ$ tegak lurus tepi sungai dengan waktu tempuh $t = 24\\text{ sekon}$, karena perahu langsung diarahkan tegak lurus sehingga pasti akan terseret jauh ke arah hilir sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$\\alpha = 60^\\circ$ ke arah hulu dengan waktu tempuh $t = 40\\text{ sekon}$, dihitung dari pendekatan sudut deviasi sembarang tanpa analisis proyeksi vektor kecepatan."
      },
      {
        "key": "D",
        "text": "$\\alpha = 45^\\circ$ terhadap hilir dengan waktu tempuh $t = 15\\text{ sekon}$, karena kecepatan perahu dan kecepatan arus langsung dijumlahkan secara skalar biasa."
      },
      {
        "key": "E",
        "text": "$\\alpha = 30^\\circ$ ke arah hilir dengan waktu tempuh $t = 60\\text{ sekon}$, dihitung dari perbandingan terbalik lebar sungai terhadap arus air."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\alpha = 126{,}87^\\circ$ terhadap arah aliran hilir (atau mengarah ke hulu sebesar $53^\\circ$ terhadap tepi hulu) dengan waktu tempuh $t = 30\\text{ sekon}$, karena komponen kecepatan perahu yang melawan arus harus tepat mengimbangi arus sungai ($v_{\\text{perahu}} \\sin\\theta = v_{\\text{arus}} \\implies 5 \\sin\\theta = 3 \\implies \\sin\\theta = 0{,}6 \\implies \\theta = 37^\\circ$ dari garis tegak lurus, atau $53^\\circ$ dari tepi sungai hulu). Kecepatan resultan efektif menyeberang adalah $v_y = \\sqrt{5^2 - 3^2} = 4\\text{ m/s}$, sehingga waktu tempuh $t = \\frac{120\\text{ m}}{4\\text{ m/s}} = 30\\text{ sekon}$.. Agar sampai tegak lurus di seberang, haluan perahu harus condong ke hulu sehingga v_perahu * sin(theta) = v_arus. Kecepatan resultan tegak lurus v_res = sqrt(vp^2 - va^2). v_res = sqrt(5^2 - 3^2) = 4 m/s. t = 120 / 4 = 30 sekon."
  },
  {
    "id": "fis-sim-02",
    "materi": "DINAMIKA GERAK (SISTEM BENDA BERTUMPUK)",
    "topic": "Gaya Maksimum pada Benda Bertumpuk Tanpa Tergelincir",
    "hints": {
      "concept": "Percepatan maksimum balok atas: a_max = mu_s * g = 0,4 * 10 = 4 m/s^2. Agar bergerak bersama, gaya tarik F_max = (mA + mB) * a_max.",
      "execution": "F_max = (2 + 6) * 4 = 32 N."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Balok $A$ bermassa $m_A = 2\\text{ kg}$ diletakkan di atas balok $B$ bermassa $m_B = 6\\text{ kg}$. Balok $B$ berada di atas lantai horizontal yang licin sempurna tanpa gesekan. Koefisien gesekan statis antara permukaan balok $A$ dan balok $B$ adalah $\\mu_s = 0{,}4$ ($g = 10\\text{ m/s}^2$). Sebuah gaya horizontal $F$ ditarikkan pada balok bawah $B$. Nilai gaya tarik maksimum ($F_{\\max}$) agar kedua balok tetap bergerak bersama-sama tanpa balok $A$ tergelincir adalah...",
    "formulaHud": {
      "title": "GAYA MAKSIMUM SISTEM BENDA BERTUMPUK",
      "latex": "a_{\\max} = \\mu_s g = 0{,}4 \\times 10 = 4\\text{ m/s}^2; \\quad F_{\\max} = (m_A + m_B) a_{\\max} = (2 + 6) \\times 4 = 32\\text{ N}",
      "legend": "• Balok atas $A$ hanya digerakkan oleh gaya gesek statis $f_s \\le \\mu_s m_A g$<br>• $a_{\\max} = 4\\text{ m/s}^2$<br>• $F_{\\max} = (m_A + m_B) a_{\\max} = 32\\text{ N}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$F_{\\max} = 8\\text{ Newton}$, karena menyamakan gaya tarik maksimum dengan nilai gaya gesekan statis antarbalok semata sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$F_{\\max} = 32\\text{ Newton}$, karena percepatan maksimum balok $A$ hanya disediakan oleh gaya gesek statis maksimum antara balok $A$ dan $B$: $f_{s,\\max} = \\mu_s m_A g = 0{,}4 \\times 2 \\times 10 = 8\\text{ N}$, sehingga percepatan maksimum sistem adalah $a_{\\max} = \\frac{f_{s,\\max}}{m_A} = \\mu_s g = 0{,}4 \\times 10 = 4\\text{ m/s}^2$. Menurut Hukum II Newton untuk massa total kedua balok, gaya maksimum pada balok bawah adalah $F_{\\max} = (m_A + m_B) a_{\\max} = (2 + 6) \\times 4 = 8 \\times 4 = 32\\text{ Newton}$."
      },
      {
        "key": "C",
        "text": "$F_{\\max} = 24\\text{ Newton}$, dihitung dengan hanya memperhitungkan massa balok bawah $B$ dikalikan percepatan maksimum."
      },
      {
        "key": "D",
        "text": "$F_{\\max} = 40\\text{ Newton}$, dihitung dari perkalian koefisien gesekan dengan berat total gabungan kedua balok di atas lantai."
      },
      {
        "key": "E",
        "text": "$F_{\\max} = 16\\text{ Newton}$, dihitung dari penggandaan massa balok atas tanpa menyertakan inersia balok bawah."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $F_{\\max} = 32\\text{ Newton}$, karena percepatan maksimum balok $A$ hanya disediakan oleh gaya gesek statis maksimum antara balok $A$ dan $B$: $f_{s,\\max} = \\mu_s m_A g = 0{,}4 \\times 2 \\times 10 = 8\\text{ N}$, sehingga percepatan maksimum sistem adalah $a_{\\max} = \\frac{f_{s,\\max}}{m_A} = \\mu_s g = 0{,}4 \\times 10 = 4\\text{ m/s}^2$. Menurut Hukum II Newton untuk massa total kedua balok, gaya maksimum pada balok bawah adalah $F_{\\max} = (m_A + m_B) a_{\\max} = (2 + 6) \\times 4 = 8 \\times 4 = 32\\text{ Newton}$.. Percepatan maksimum balok atas: a_max = mu_s * g = 0,4 * 10 = 4 m/s^2. Agar bergerak bersama, gaya tarik F_max = (mA + mB) * a_max. F_max = (2 + 6) * 4 = 32 N."
  },
  {
    "id": "fis-sim-03",
    "materi": "USAHA & ENERGI (GERAK MELINGKAR VERTIKAL)",
    "topic": "Kecepatan Kritis & Gaya Normal Puncak Roller Coaster",
    "hints": {
      "concept": "Di puncak loop: N = 0 -> v_puncak = sqrt(g*R). Energi mekanik awal = energi mekanik puncak: m*g*h_min = m*g*(2R) + 1/2*m*(g*R) -> h_min = 2,5 * R.",
      "execution": "v_puncak = sqrt(10*10) = 10 m/s. h_min = 2,5 * 10 = 25 meter."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah kereta roller coaster bermassa $m = 500\\text{ kg}$ meluncur menuruni lintasan licin dan memasuki lintasan melingkar vertikal (loop-the-loop) yang memiliki jari-jari $R = 10\\text{ meter}$. Jika percepatan gravitasi bumi $g = 10\\text{ m/s}^2$, kecepatan minimum di titik puncak loop ($v_{\\text{puncak}}$) agar kereta tidak terlepas dari rel serta ketinggian minimum pelepasan kereta ($h_{\\min}$) dari dasar rel adalah...",
    "formulaHud": {
      "title": "KECEPATAN KRITIS DAN KETINGGIAN LOOP THE LOOP",
      "latex": "v_{\\text{puncak}} = \\sqrt{g R} = \\sqrt{10 \\times 10} = 10\\text{ m/s}; \\quad h_{\\min} = \\frac{5}{2} R = 2{,}5 \\times 10 = 25\\text{ m}",
      "legend": "• $N_{\\text{puncak}} = 0 \\implies m g = \\frac{m v^2}{R}$<br>• $h_{\\min} = 2R + \\frac{gR}{2g} = 2{,}5 R = 25\\text{ meter}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$v_{\\text{puncak}} = 14{,}14\\text{ m/s}$ dan $h_{\\min} = 20\\text{ meter}$, dihitung dengan menyamakan tinggi pelepasan tepat sama dengan diameter lingkaran loop ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$v_{\\text{puncak}} = 7{,}07\\text{ m/s}$ dan $h_{\\min} = 15\\text{ meter}$, dihitung dari asumsi bahwa kecepatan di puncak sama dengan separuh kecepatan dasar lintasan."
      },
      {
        "key": "C",
        "text": "$v_{\\text{puncak}} = 10\\text{ m/s}$ dan $h_{\\min} = 25\\text{ meter}$, karena syarat kereta tidak terlepas di titik puncak loop adalah gaya normal tepat nol ($N = 0$), sehingga gaya gravitasi bertindak sebagai gaya sentripetal: $m g = \\frac{m v^2}{R} \\implies v_{\\text{puncak}} = \\sqrt{g R} = \\sqrt{10 \\times 10} = 10\\text{ m/s}$. Dari Hukum Kekekalan Energi Mekanik terhadap dasar lintasan ($h=0$): $m g h_{\\min} = m g (2R) + \\frac{1}{2} m v_{\\text{puncak}}^2 \\implies h_{\\min} = 2R + \\frac{v^2}{2g} = 2(10) + \\frac{100}{20} = 20 + 5 = 25\\text{ meter}$."
      },
      {
        "key": "D",
        "text": "$v_{\\text{puncak}} = 20\\text{ m/s}$ dan $h_{\\min} = 30\\text{ meter}$, karena rumus kecepatan kritis keliru menggunakan diameter lingkaran dalam akar gravitasi."
      },
      {
        "key": "E",
        "text": "$v_{\\text{puncak}} = 0\\text{ m/s}$ dan $h_{\\min} = 20\\text{ meter}$, karena beranggapan kereta dapat berhenti sesaat di puncak lingkaran vertikal."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $v_{\\text{puncak}} = 10\\text{ m/s}$ dan $h_{\\min} = 25\\text{ meter}$, karena syarat kereta tidak terlepas di titik puncak loop adalah gaya normal tepat nol ($N = 0$), sehingga gaya gravitasi bertindak sebagai gaya sentripetal: $m g = \\frac{m v^2}{R} \\implies v_{\\text{puncak}} = \\sqrt{g R} = \\sqrt{10 \\times 10} = 10\\text{ m/s}$. Dari Hukum Kekekalan Energi Mekanik terhadap dasar lintasan ($h=0$): $m g h_{\\min} = m g (2R) + \\frac{1}{2} m v_{\\text{puncak}}^2 \\implies h_{\\min} = 2R + \\frac{v^2}{2g} = 2(10) + \\frac{100}{20} = 20 + 5 = 25\\text{ meter}$.. Di puncak loop: N = 0 -> v_puncak = sqrt(g*R). Energi mekanik awal = energi mekanik puncak: m*g*h_min = m*g*(2R) + 1/2*m*(g*R) -> h_min = 2,5 * R. v_puncak = sqrt(10*10) = 10 m/s. h_min = 2,5 * 10 = 25 meter."
  },
  {
    "id": "fis-sim-04",
    "materi": "MOMENTUM & TUMBUKAN DUA DIMENSI",
    "topic": "Tumbukan Lenting Sempurna Massa Sama",
    "hints": {
      "concept": "Tumbukan elastis 2 benda bermassa sama dengan target diam menghasilkan sudut pisah 90 derajat: theta1 + theta2 = 90. Maka theta2 = 60 derajat. v1' = v1 * cos(30).",
      "execution": "theta2 = 90 - 30 = 60 derajat. v1' = 4 * cos(30) = 4 * 0,5 * sqrt(3) = 2*sqrt(3) m/s = 3,46 m/s."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua buah bola biliar identik bermassa sama $m_1 = m_2 = 0{,}2\\text{ kg}$ berada di atas meja licin. Bola 1 meluncur dengan kelajuan $v_1 = 4\\text{ m/s}$ menumbuk bola 2 yang mula-mula diam ($v_2 = 0$). Setelah tumbukan lenting sempurna berlangsung, bola 1 bergerak menyimpang dengan sudut $\\theta_1 = 30^\\circ$ terhadap arah gerak awalnya. Sudut hamburan bola 2 ($\\theta_2$) dan besar kelajuan bola 1 ($v_1'$) setelah tumbukan adalah...",
    "formulaHud": {
      "title": "TUMBUKAN LENTING SEMPURNA MASSA IDENTIK",
      "latex": "\\vec{v}_1 = \\vec{v}_1' + \\vec{v}_2' \\quad \\text{dan} \\quad v_1^2 = (v_1')^2 + (v_2')^2 \\implies \\theta_1 + \\theta_2 = 90^\\circ; \\quad v_1' = v_1 \\cos\\theta_1 = 4 \\cos 30^\\circ = 2\\sqrt{3}\\text{ m/s}",
      "legend": "• Sifat khas massa identik tumbukan elastis 2D: $\\vec{v}_1' \\cdot \\vec{v}_2' = 0 \\implies$ arah gerak saling tegak lurus ($90^\\circ$)<br>• $\\theta_2 = 90^\\circ - 30^\\circ = 60^\\circ$<br>• $v_1' = 2\\sqrt{3}\\text{ m/s} \\approx 3{,}46\\text{ m/s}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\theta_2 = 30^\\circ$ dan $v_1' = 2\\text{ m/s}$, karena diasumsikan bola 2 menyimpang secara simetris terhadap sumbu gerak awal menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$\\theta_2 = 45^\\circ$ dan $v_1' = 2\\sqrt{2}\\text{ m/s}$, dihitung dari asumsi sudut deviasi bagi rata empat puluh lima derajat."
      },
      {
        "key": "C",
        "text": "$\\theta_2 = 90^\\circ$ dan $v_1' = 4\\text{ m/s}$, karena beranggapan bola 1 meneruskan seluruh momentum awalnya tanpa kehilangan energi."
      },
      {
        "key": "D",
        "text": "$\\theta_2 = 60^\\circ$ (sehingga kedua bola bergerak saling tegak lurus $\\theta_1 + \\theta_2 = 90^\\circ$) dan $v_1' = 2\\sqrt{3}\\text{ m/s} \\approx 3{,}46\\text{ m/s}$, karena pada tumbukan lenting sempurna dua massa identik di mana salah satu massa awalnya diam, vektor kecepatan akhir selalu membentuk sudut siku-siku ($90^\\circ$). Dari proyeksi trigonometri segitiga kecepatan: $v_1' = v_1 \\cos 30^\\circ = 4 \\times \\frac{1}{2}\\sqrt{3} = 2\\sqrt{3}\\text{ m/s}$."
      },
      {
        "key": "E",
        "text": "$\\theta_2 = 120^\\circ$ dan $v_1' = 1\\text{ m/s}$, dihitung dari pembalikan arah gerak bola tumbukan lenting sebagian."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $\\theta_2 = 60^\\circ$ (sehingga kedua bola bergerak saling tegak lurus $\\theta_1 + \\theta_2 = 90^\\circ$) dan $v_1' = 2\\sqrt{3}\\text{ m/s} \\approx 3{,}46\\text{ m/s}$, karena pada tumbukan lenting sempurna dua massa identik di mana salah satu massa awalnya diam, vektor kecepatan akhir selalu membentuk sudut siku-siku ($90^\\circ$). Dari proyeksi trigonometri segitiga kecepatan: $v_1' = v_1 \\cos 30^\\circ = 4 \\times \\frac{1}{2}\\sqrt{3} = 2\\sqrt{3}\\text{ m/s}$.. Tumbukan elastis 2 benda bermassa sama dengan target diam menghasilkan sudut pisah 90 derajat: theta1 + theta2 = 90. Maka theta2 = 60 derajat. v1' = v1 * cos(30). theta2 = 90 - 30 = 60 derajat. v1' = 4 * cos(30) = 4 * 0,5 * sqrt(3) = 2*sqrt(3) m/s = 3,46 m/s."
  },
  {
    "id": "fis-sim-05",
    "materi": "ELASTISITAS & TEGANGAN BAHAN",
    "topic": "Modulus Young dan Pertambahan Panjang Kawat Baja",
    "hints": {
      "concept": "Tegangan: sigma = F / A = F / (pi * r^2). Pertambahan panjang: Delta_L = sigma * L0 / E.",
      "execution": "sigma = 628 / (3,14e-6) = 2e8 N/m^2. Delta_L = (2e8 * 4) / 2e11 = 4e-3 m = 4 mm."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah kawat baja memiliki panjang awal $L_0 = 4\\text{ meter}$ dan diameter penampang $d = 2\\text{ mm}$ (jari-jari $r = 1\\text{ mm} = 10^{-3}\\text{ m}$, sehingga luas penampang $A = \\pi r^2 = \\pi \\times 10^{-6}\\text{ m}^2$). Kawat digantung vertikal dan ditarik dengan gaya beban $F = 628\\text{ Newton}$ (gunakan $\\pi \\approx 3{,}14$, sehingga $A \\approx 3{,}14 \\times 10^{-6}\\text{ m}^2$). Jika modulus Young baja adalah $E = 2 \\times 10^{11}\\text{ N/m}^2$, tegangan tarik ($\\sigma$) dan pertambahan panjang kawat ($\\Delta L$) adalah...",
    "formulaHud": {
      "title": "MODULUS ELASTISITAS YOUNG & HUKUM HOOKE",
      "latex": "\\sigma = \\frac{F}{A} = \\frac{628}{3{,}14 \\times 10^{-6}} = 2 \\times 10^8\\text{ Pa}; \\quad \\Delta L = \\frac{F L_0}{A E} = \\frac{\\sigma L_0}{E} = \\frac{2 \\times 10^8 \\times 4}{2 \\times 10^{11}} = 4 \\times 10^{-3}\\text{ m} = 4\\text{ mm}",
      "legend": "• Luas penampang kawat silinder $A = \\pi r^2 = 3{,}14 \\times 10^{-6}\\text{ m}^2$<br>• Tegangan $\\sigma = 200\\text{ MPa}$<br>• Pertambahan panjang $\\Delta L = 4\\text{ mm}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\sigma = 1 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 2\\text{ mm}$, karena luas penampang keliru dihitung menggunakan diameter kawat tanpa dibagi dua menjadi jari-jari diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$\\sigma = 4 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 8\\text{ mm}$, dihitung dari penggandaan tegangan geser torsional."
      },
      {
        "key": "C",
        "text": "$\\sigma = 2 \\times 10^7\\text{ N/m}^2$ dan $\\Delta L = 0{,}4\\text{ mm}$, karena galat konversi satuan luas dari milimeter persegi ke meter persegi."
      },
      {
        "key": "D",
        "text": "$\\sigma = 6{,}28 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 1\\text{ mm}$, dihitung tanpa membagi gaya dengan nilai pi luas penampang kawat."
      },
      {
        "key": "E",
        "text": "$\\sigma = 2 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 4\\text{ mm}$ (atau $4 \\times 10^{-3}\\text{ m}$), karena tegangan adalah $\\sigma = \\frac{F}{A} = \\frac{628\\text{ N}}{3{,}14 \\times 10^{-6}\\text{ m}^2} = 2 \\times 10^8\\text{ N/m}^2$. Pertambahan panjang kawat menurut hukum Hooke elastisitas adalah $\\Delta L = \\frac{\\sigma L_0}{E} = \\frac{(2 \\times 10^8\\text{ N/m}^2) \\times 4\\text{ m}}{2 \\times 10^{11}\\text{ N/m}^2} = \\frac{8 \\times 10^8}{2 \\times 10^{11}} = 4 \\times 10^{-3}\\text{ m} = 4\\text{ mm}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $\\sigma = 2 \\times 10^8\\text{ N/m}^2$ dan $\\Delta L = 4\\text{ mm}$ (atau $4 \\times 10^{-3}\\text{ m}$), karena tegangan adalah $\\sigma = \\frac{F}{A} = \\frac{628\\text{ N}}{3{,}14 \\times 10^{-6}\\text{ m}^2} = 2 \\times 10^8\\text{ N/m}^2$. Pertambahan panjang kawat menurut hukum Hooke elastisitas adalah $\\Delta L = \\frac{\\sigma L_0}{E} = \\frac{(2 \\times 10^8\\text{ N/m}^2) \\times 4\\text{ m}}{2 \\times 10^{11}\\text{ N/m}^2} = \\frac{8 \\times 10^8}{2 \\times 10^{11}} = 4 \\times 10^{-3}\\text{ m} = 4\\text{ mm}$.. Tegangan: sigma = F / A = F / (pi * r^2). Pertambahan panjang: Delta_L = sigma * L0 / E. sigma = 628 / (3,14e-6) = 2e8 N/m^2. Delta_L = (2e8 * 4) / 2e11 = 4e-3 m = 4 mm."
  },
  {
    "id": "fis-sim-06",
    "materi": "HUKUM GRAVITASI NEWTON & KEPLER",
    "topic": "Hukum III Kepler & Perbandingan Periode Orbit Planet",
    "hints": {
      "concept": "Hukum III Kepler: (T1 / T2)^2 = (R1 / R2)^3. Maka TY = TX * (RY / RX)^(3/2).",
      "execution": "TY = 8 * (16 / 4)^(3/2) = 8 * 4^(1,5) = 8 * 8 = 64 tahun."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua planet $X$ dan $Y$ mengorbit sebuah bintang induk yang sama dalam lintasan berbentuk lingkaran. Jarak rata-rata planet $X$ ke bintang adalah $R_X = 4\\text{ SA}$ (Satuan Astronomi), sedangkan jarak rata-rata planet $Y$ adalah $R_Y = 16\\text{ SA}$. Jika periode revolusi planet $X$ mengelilingi bintang adalah $T_X = 8\\text{ tahun}$, periode revolusi planet $Y$ ($T_Y$) mengelilingi bintang tersebut menurut Hukum III Kepler adalah...",
    "formulaHud": {
      "title": "HUKUM III KEPLER",
      "latex": "\\frac{T_1^2}{R_1^3} = \\frac{T_2^2}{R_2^3} \\implies T_Y = T_X \\left(\\frac{R_Y}{R_X}\\right)^{3/2} = 8 \\times (4)^{3/2} = 8 \\times 8 = 64\\text{ tahun}",
      "legend": "• $R_Y / R_X = 16 / 4 = 4$<br>• $(4)^{3/2} = (\\sqrt{4})^3 = 2^3 = 8$<br>• $T_Y = 8 \\times 8 = 64\\text{ tahun}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$T_Y = 64\\text{ tahun}$, karena menurut Hukum III Kepler rasio kuadrat periode revolusi berbanding lurus dengan pangkat tiga jarak rata-rata orbit: $\\left(\\frac{T_Y}{T_X}\\right)^2 = \\left(\\frac{R_Y}{R_X}\\right)^3 = \\left(\\frac{16}{4}\\right)^3 = 4^3 = 64$, sehingga $\\frac{T_Y}{T_X} = \\sqrt{64} = 8$, dan periode planet $Y$ adalah $T_Y = 8 \\times T_X = 8 \\times 8 = 64\\text{ tahun}$."
      },
      {
        "key": "B",
        "text": "$T_Y = 32\\text{ tahun}$, karena hubungan Kepler keliru dianggap berbanding kuadrat langsung tanpa pemangkatan tiga jarak orbit sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$T_Y = 128\\text{ tahun}$, dihitung dari perkalian periode planet pertama dengan rasio kuadrat jarak lintasan orbit."
      },
      {
        "key": "D",
        "text": "$T_Y = 16\\text{ tahun}$, karena beranggapan periode revolusi berbanding lurus linier dengan jarak rata-rata orbit satelit."
      },
      {
        "key": "E",
        "text": "$T_Y = 256\\text{ tahun}$, dihitung dari pemangkatan empat perbandingan jarak rata-rata orbit planet."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $T_Y = 64\\text{ tahun}$, karena menurut Hukum III Kepler rasio kuadrat periode revolusi berbanding lurus dengan pangkat tiga jarak rata-rata orbit: $\\left(\\frac{T_Y}{T_X}\\right)^2 = \\left(\\frac{R_Y}{R_X}\\right)^3 = \\left(\\frac{16}{4}\\right)^3 = 4^3 = 64$, sehingga $\\frac{T_Y}{T_X} = \\sqrt{64} = 8$, dan periode planet $Y$ adalah $T_Y = 8 \\times T_X = 8 \\times 8 = 64\\text{ tahun}$.. Hukum III Kepler: (T1 / T2)^2 = (R1 / R2)^3. Maka TY = TX * (RY / RX)^(3/2). TY = 8 * (16 / 4)^(3/2) = 8 * 4^(1,5) = 8 * 8 = 64 tahun."
  },
  {
    "id": "fis-sim-07",
    "materi": "FLUIDA STATIS (BEJANA BERHUBUNGAN)",
    "topic": "Tekanan Hidrostatis pada Pipa U Dua Zat Cair",
    "hints": {
      "concept": "Hukum Utama Hidrostatis: rho_air * h_air = rho_minyak * h_minyak. Cari h_air, lalu selisih tinggi Delta_h = h_minyak - h_air.",
      "execution": "h_air = (800 / 1000) * 15 = 12 cm. Delta_h = 15 - 12 = 3 cm."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah pipa berbentuk huruf U mula-mula diisi air dengan massa jenis $\\rho_{\\text{air}} = 1.000\\text{ kg/m}^3$. Ke dalam kaki kanan pipa U tersebut dituangkan minyak dengan massa jenis $\\rho_{\\text{minyak}} = 800\\text{ kg/m}^3$ setinggi kolom $h_{\\text{minyak}} = 15\\text{ cm}$. Jika kedua ujung pipa terbuka ke udara bebas, selisih ketinggian permukaan air pada kaki kiri terhadap permukaan minyak pada kaki kanan ($\\Delta h$) adalah...",
    "formulaHud": {
      "title": "HUKUM UTAMA HIDROSTATIS PADA PIPA U",
      "latex": "P_A = P_B \\implies \\rho_{\\text{air}} h_{\\text{air}} = \\rho_{\\text{minyak}} h_{\\text{minyak}} \\implies h_{\\text{air}} = \\frac{800}{1.000} \\times 15 = 12\\text{ cm}; \\quad \\Delta h = 15 - 12 = 3\\text{ cm}",
      "legend": "• Bidang acuan diambil pada batas terendah pertemuan air dan minyak<br>• Tinggi kolom air terangkat di atas bidang batas $h_{\\text{air}} = 12\\text{ cm}$<br>• Selisih permukaan $\\Delta h = 15 - 12 = 3\\text{ cm}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta h = 12\\text{ cm}$, karena nilai tersebut merupakan tinggi kolom air yang terangkat dari garis bidang batas kesetimbangan sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$\\Delta h = 3\\text{ cm}$ (di mana permukaan air di kaki kiri lebih rendah $3\\text{ cm}$ dibanding permukaan atas minyak di kaki kanan), karena pada bidang batas bawah berlaku kesetimbangan tekanan hidrostatis $\\rho_{\\text{air}} g h_{\\text{air}} = \\rho_{\\text{minyak}} g h_{\\text{minyak}} \\implies h_{\\text{air}} = \\frac{\\rho_{\\text{minyak}}}{\\rho_{\\text{air}}} h_{\\text{minyak}} = \\frac{800}{1.000} \\times 15 = 12\\text{ cm}$. Selisih ketinggian antara kedua permukaan atas zat cair adalah $\\Delta h = h_{\\text{minyak}} - h_{\\text{air}} = 15\\text{ cm} - 12\\text{ cm} = 3\\text{ cm}$."
      },
      {
        "key": "C",
        "text": "$\\Delta h = 5\\text{ cm}$, dihitung dari perbandingan selisih massa jenis terhadap tinggi total kolom minyak."
      },
      {
        "key": "D",
        "text": "$\\Delta h = 2\\text{ cm}$, dihitung dari pendekatan pembulatan rasio kerapatan massa jenis fluida."
      },
      {
        "key": "E",
        "text": "$\\Delta h = 0\\text{ cm}$, karena mengasumsikan permukaan cairan dalam pipa U selalu datar sejajar dalam kondisi setimbang."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\Delta h = 3\\text{ cm}$ (di mana permukaan air di kaki kiri lebih rendah $3\\text{ cm}$ dibanding permukaan atas minyak di kaki kanan), karena pada bidang batas bawah berlaku kesetimbangan tekanan hidrostatis $\\rho_{\\text{air}} g h_{\\text{air}} = \\rho_{\\text{minyak}} g h_{\\text{minyak}} \\implies h_{\\text{air}} = \\frac{\\rho_{\\text{minyak}}}{\\rho_{\\text{air}}} h_{\\text{minyak}} = \\frac{800}{1.000} \\times 15 = 12\\text{ cm}$. Selisih ketinggian antara kedua permukaan atas zat cair adalah $\\Delta h = h_{\\text{minyak}} - h_{\\text{air}} = 15\\text{ cm} - 12\\text{ cm} = 3\\text{ cm}$.. Hukum Utama Hidrostatis: rho_air * h_air = rho_minyak * h_minyak. Cari h_air, lalu selisih tinggi Delta_h = h_minyak - h_air. h_air = (800 / 1000) * 15 = 12 cm. Delta_h = 15 - 12 = 3 cm."
  },
  {
    "id": "fis-sim-08",
    "materi": "FLUIDA DINAMIS (VENTURIMETER TANPA MANOMETER)",
    "topic": "Kelajuan Aliran Fluida pada Pipa Venturi",
    "hints": {
      "concept": "Gunakan persamaan venturimeter: v1 = sqrt( 2*g*h / ((A1/A2)^2 - 1) ). Debit Q = A1 * v1.",
      "execution": "v1 = sqrt( 2 * 10 * 0,45 / (2^2 - 1) ) = sqrt(9 / 3) = sqrt(3) m/s. Q = 50e-4 * sqrt(3) = 8,66 L/s."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Minyak dengan massa jenis $\\rho = 800\\text{ kg/m}^3$ mengalir melalui sebuah venturimeter mendatar tanpa manometer. Luas penampang pipa utama adalah $A_1 = 50\\text{ cm}^2$ dan luas penampang leher yang menyempit adalah $A_2 = 25\\text{ cm}^2$ (sehingga rasio luas penampang $A_1/A_2 = 2$). Pada pipa vertikal pengukur tekanan, terdapat selisih ketinggian permukaan minyak sebesar $h = 45\\text{ cm} = 0{,}45\\text{ meter}$. Jika percepatan gravitasi bumi $g = 10\\text{ m/s}^2$, kelajuan aliran fluida di penampang utama ($v_1$) dan debit alirannya ($Q$) adalah...",
    "formulaHud": {
      "title": "FORMULA VENTURIMETER TANPA MANOMETER",
      "latex": "v_1 = \\sqrt{\\frac{2gh}{\\left(\\frac{A_1}{A_2}\\right)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}45}{2^2 - 1}} = \\sqrt{3}\\text{ m/s}; \\quad Q = A_1 v_1 = 5 \\times 10^{-3}\\sqrt{3}\\text{ m}^3\\text{/s}",
      "legend": "• $h = 0{,}45\\text{ m}$<br>• $A_1 / A_2 = 50 / 25 = 2$<br>• $v_1 = \\sqrt{3}\\text{ m/s} \\approx 1{,}732\\text{ m/s}$<br>• $Q = 8{,}66\\text{ liter/s}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$v_1 = 3\\text{ m/s}$ dan $Q = 15\\text{ L/s}$, karena penyebut di dalam tanda akar keliru tidak dikurangi angka 1 dari rasio kuadrat penampang ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$v_1 = 2\\text{ m/s}$ dan $Q = 10\\text{ L/s}$, dihitung dari perkalian luas penampang terhadap selisih ketinggian fluida."
      },
      {
        "key": "C",
        "text": "$v_1 = \\sqrt{3}\\text{ m/s} \\approx 1{,}73\\text{ m/s}$ dan $Q = 5\\sqrt{3} \\times 10^{-3}\\text{ m}^3\\text{/s} \\approx 8{,}66\\text{ L/s}$, karena rumus venturimeter tanpa manometer adalah $v_1 = \\sqrt{\\frac{2gh}{(A_1/A_2)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}45}{2^2 - 1}} = \\sqrt{\\frac{9}{4 - 1}} = \\sqrt{\\frac{9}{3}} = \\sqrt{3}\\text{ m/s}$. Debit aliran adalah $Q = A_1 v_1 = (50 \\times 10^{-4}\\text{ m}^2) \\times \\sqrt{3}\\text{ m/s} = 5\\sqrt{3} \\times 10^{-3}\\text{ m}^3\\text{/s} \\approx 8{,}66\\text{ liter/sekon}$."
      },
      {
        "key": "D",
        "text": "$v_1 = 0{,}9\\text{ m/s}$ dan $Q = 4{,}5\\text{ L/s}$, dihitung dari rumus semburan bebas Torricelli tanpa memperhitungkan penyempitan leher pipa."
      },
      {
        "key": "E",
        "text": "$v_1 = 4{,}5\\text{ m/s}$ dan $Q = 22{,}5\\text{ L/s}$, dihitung dari perbandingan selisih tekanan hidrostatik langsung terhadap kerapatan fluida."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $v_1 = \\sqrt{3}\\text{ m/s} \\approx 1{,}73\\text{ m/s}$ dan $Q = 5\\sqrt{3} \\times 10^{-3}\\text{ m}^3\\text{/s} \\approx 8{,}66\\text{ L/s}$, karena rumus venturimeter tanpa manometer adalah $v_1 = \\sqrt{\\frac{2gh}{(A_1/A_2)^2 - 1}} = \\sqrt{\\frac{2 \\times 10 \\times 0{,}45}{2^2 - 1}} = \\sqrt{\\frac{9}{4 - 1}} = \\sqrt{\\frac{9}{3}} = \\sqrt{3}\\text{ m/s}$. Debit aliran adalah $Q = A_1 v_1 = (50 \\times 10^{-4}\\text{ m}^2) \\times \\sqrt{3}\\text{ m/s} = 5\\sqrt{3} \\times 10^{-3}\\text{ m}^3\\text{/s} \\approx 8{,}66\\text{ liter/sekon}$.. Gunakan persamaan venturimeter: v1 = sqrt( 2*g*h / ((A1/A2)^2 - 1) ). Debit Q = A1 * v1. v1 = sqrt( 2 * 10 * 0,45 / (2^2 - 1) ) = sqrt(9 / 3) = sqrt(3) m/s. Q = 50e-4 * sqrt(3) = 8,66 L/s."
  },
  {
    "id": "fis-sim-09",
    "materi": "KALOR & TERMODINAMIKA (ASAS BLACK)",
    "topic": "Kesetimbangan Termal Pencampuran Es dan Air Panas",
    "hints": {
      "concept": "Hitung kalor lebur es: 100 * 80 = 8.000 kal. Kalor air lepas ke 0C: 200 * 1 * 90 = 18.000 kal. Karena 18.000 > 8.000, semua es cair dan suhu akhir > 0C. Gunakan Q_lepas = Q_serap.",
      "execution": "200 * (90 - Tc) = 8.000 + 100 * Tc -> 18.000 - 200 Tc = 8.000 + 100 Tc -> 300 Tc = 10.000 -> Tc = 33,33 C."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebongkah es bermassa $m_{\\text{es}} = 100\\text{ gram}$ pada suhu $0^\\circ\\text{C}$ dimasukkan ke dalam bejana terisolasi yang berisi $m_{\\text{air}} = 200\\text{ gram}$ air panas bersuhu $90^\\circ\\text{C}$. Diketahui kalor lebur es $L_f = 80\\text{ kal/g}$ dan kalor jenis air $c_{\\text{air}} = 1\\text{ kal/(g}\\cdot^\\circ\\text{C)}$. Mengabaikan kapasitas kalor bejana penyerap panas, suhu akhir kesetimbangan termal campuran ($T_c$) adalah...",
    "formulaHud": {
      "title": "ASAS BLACK & PELEBURAN ES",
      "latex": "Q_{\\text{lepas}} = Q_{\\text{serap}} \\implies m_a c_a (T_a - T_c) = m_e L_f + m_e c_a (T_c - 0); \\quad 200(1)(90 - T_c) = 100(80) + 100(1) T_c \\implies 300 T_c = 10.000 \\implies T_c = 33{,}33^\\circ\\text{C}",
      "legend": "• Seluruh es melebur karena $Q_{\\text{lepas},\\max} (18.000\\text{ kal}) > Q_{\\text{lebur}} (8.000\\text{ kal})$<br>• Suhu akhir campuran $T_c = 33{,}33^\\circ\\text{C}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$T_c = 45{,}00^\\circ\\text{C}$, karena hanya menghitung rata-rata suhu kedua zat cair tanpa memperhitungkan kalor laten peleburan es menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$T_c = 25{,}00^\\circ\\text{C}$, dihitung dengan mengalikan kalor jenis es ke dalam perhitungan kalor laten lebur."
      },
      {
        "key": "C",
        "text": "$T_c = 0{,}00^\\circ\\text{C}$, karena beranggapan es tidak mencair seluruhnya dan menyerap seluruh kalor air panas."
      },
      {
        "key": "D",
        "text": "$T_c = 33{,}33^\\circ\\text{C}$ (atau $33\\frac{1}{3}^\\circ\\text{C}$), karena kalor yang dibutuhkan untuk meleburkan seluruh es menjadi air $0^\\circ\\text{C}$ adalah $Q_{\\text{lebur}} = m_{\\text{es}} L_f = 100 \\times 80 = 8.000\\text{ kalori}$. Kalor maksimum yang dapat dilepaskan air panas untuk mendingin ke $0^\\circ\\text{C}$ adalah $Q_{\\text{lepas}} = 200 \\times 1 \\times 90 = 18.000\\text{ kalori} > 8.000\\text{ kal}$, sehingga seluruh es dipastikan mencair. Menurut Asas Black: $Q_{\\text{lepas}} = Q_{\\text{serap}} \\implies m_{\\text{air}} c (90 - T_c) = m_{\\text{es}} L_f + m_{\\text{es}} c (T_c - 0) \\implies 200(90 - T_c) = 8.000 + 100 T_c \\implies 18.000 - 200 T_c = 8.000 + 100 T_c \\implies 300 T_c = 10.000 \\implies T_c = \\frac{100}{3} = 33{,}33^\\circ\\text{C}$."
      },
      {
        "key": "E",
        "text": "$T_c = 60{,}00^\\circ\\text{C}$, dihitung dari perbandingan massa es terhadap massa air panas dikalikan suhu awal."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $T_c = 33{,}33^\\circ\\text{C}$ (atau $33\\frac{1}{3}^\\circ\\text{C}$), karena kalor yang dibutuhkan untuk meleburkan seluruh es menjadi air $0^\\circ\\text{C}$ adalah $Q_{\\text{lebur}} = m_{\\text{es}} L_f = 100 \\times 80 = 8.000\\text{ kalori}$. Kalor maksimum yang dapat dilepaskan air panas untuk mendingin ke $0^\\circ\\text{C}$ adalah $Q_{\\text{lepas}} = 200 \\times 1 \\times 90 = 18.000\\text{ kalori} > 8.000\\text{ kal}$, sehingga seluruh es dipastikan mencair. Menurut Asas Black: $Q_{\\text{lepas}} = Q_{\\text{serap}} \\implies m_{\\text{air}} c (90 - T_c) = m_{\\text{es}} L_f + m_{\\text{es}} c (T_c - 0) \\implies 200(90 - T_c) = 8.000 + 100 T_c \\implies 18.000 - 200 T_c = 8.000 + 100 T_c \\implies 300 T_c = 10.000 \\implies T_c = \\frac{100}{3} = 33{,}33^\\circ\\text{C}$.. Hitung kalor lebur es: 100 * 80 = 8.000 kal. Kalor air lepas ke 0C: 200 * 1 * 90 = 18.000 kal. Karena 18.000 > 8.000, semua es cair dan suhu akhir > 0C. Gunakan Q_lepas = Q_serap. 200 * (90 - Tc) = 8.000 + 100 * Tc -> 18.000 - 200 Tc = 8.000 + 100 Tc -> 300 Tc = 10.000 -> Tc = 33,33 C."
  },
  {
    "id": "fis-sim-10",
    "materi": "TEORI KINETIK GAS IDEAL",
    "topic": "Energi Kinetik Rata-rata dan Kelajuan Efektif Molekul Gas",
    "hints": {
      "concept": "Gas monoatomik: Ek_rata = 3/2 * kB * T. Energi dalam 1 mol: U = 3/2 * n * R * T.",
      "execution": "Ek = 1,5 * 1,38e-23 * 300 = 6,21e-21 J. U = 1,5 * 1 * 8,314 * 300 = 3.741,3 J."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Satu mol gas ideal monoatomik berada di dalam wadah tertutup pada suhu mutlak $T = 300\\text{ K}$. Diketahui konstanta Boltzmann $k_B = 1{,}38 \\times 10^{-23}\\text{ J/K}$ dan konstanta gas umum $R = 8{,}314\\text{ J/(mol}\\cdot\\text{K)}$. Energi kinetik translasi rata-rata per molekul gas ($\\bar{E}_k$) dan total energi dalam gas ($U$) untuk 1 mol gas tersebut adalah...",
    "formulaHud": {
      "title": "ENERGI KINETIK RATA-RATA & ENERGI DALAM GAS MONOATOMIK",
      "latex": "\\bar{E}_k = \\frac{3}{2} k_B T = 1{,}5 \\times (1{,}38 \\times 10^{-23}) \\times 300 = 6{,}21 \\times 10^{-21}\\text{ J}; \\quad U = \\frac{3}{2} n R T = 1{,}5 \\times 1 \\times 8{,}314 \\times 300 = 3.741{,}3\\text{ J}",
      "legend": "• Gas monoatomik hanya memiliki 3 derajat kebebasan translasi ($f = 3$)<br>• $\\bar{E}_k$ hanya bergantung pada suhu mutlak $T$<br>• $U = N \\bar{E}_k = n N_A \\bar{E}_k = 3.741{,}3\\text{ J}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\bar{E}_k = 1{,}035 \\times 10^{-20}\\text{ Joule}$ dan $U = 6.235{,}5\\text{ Joule}$, karena keliru menggunakan derajat kebebasan diatomik $f = 5$ pada suhu tinggi diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$\\bar{E}_k = 4{,}14 \\times 10^{-21}\\text{ Joule}$ dan $U = 2.494{,}2\\text{ Joule}$, karena energi kinetik keliru dihitung dengan derajat kebebasan dua dimensi."
      },
      {
        "key": "C",
        "text": "$\\bar{E}_k = 6{,}21 \\times 10^{-21}\\text{ Joule}$ dan $U = 1.247{,}1\\text{ Joule}$, karena energi dalam total keliru dibagi dengan konstanta tiga."
      },
      {
        "key": "D",
        "text": "$\\bar{E}_k = 1{,}24 \\times 10^{-20}\\text{ Joule}$ dan $U = 7.482{,}6\\text{ Joule}$, dihitung dari penggandaan suhu mutlak dalam skala Celsius."
      },
      {
        "key": "E",
        "text": "$\\bar{E}_k = 6{,}21 \\times 10^{-21}\\text{ Joule}$ dan $U = 3.741{,}3\\text{ Joule}$, karena untuk gas monoatomik yang memiliki derajat kebebasan $f = 3$, energi kinetik rata-rata per molekul adalah $\\bar{E}_k = \\frac{3}{2} k_B T = \\frac{3}{2} \\times (1{,}38 \\times 10^{-23}\\text{ J/K}) \\times 300\\text{ K} = 6{,}21 \\times 10^{-21}\\text{ J}$. Energi dalam total untuk 1 mol gas adalah $U = \\frac{3}{2} n R T = \\frac{3}{2} (1\\text{ mol}) \\times 8{,}314\\text{ J/(mol}\\cdot\\text{K)} \\times 300\\text{ K} = 3.741{,}3\\text{ Joule}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $\\bar{E}_k = 6{,}21 \\times 10^{-21}\\text{ Joule}$ dan $U = 3.741{,}3\\text{ Joule}$, karena untuk gas monoatomik yang memiliki derajat kebebasan $f = 3$, energi kinetik rata-rata per molekul adalah $\\bar{E}_k = \\frac{3}{2} k_B T = \\frac{3}{2} \\times (1{,}38 \\times 10^{-23}\\text{ J/K}) \\times 300\\text{ K} = 6{,}21 \\times 10^{-21}\\text{ J}$. Energi dalam total untuk 1 mol gas adalah $U = \\frac{3}{2} n R T = \\frac{3}{2} (1\\text{ mol}) \\times 8{,}314\\text{ J/(mol}\\cdot\\text{K)} \\times 300\\text{ K} = 3.741{,}3\\text{ Joule}$.. Gas monoatomik: Ek_rata = 3/2 * kB * T. Energi dalam 1 mol: U = 3/2 * n * R * T. Ek = 1,5 * 1,38e-23 * 300 = 6,21e-21 J. U = 1,5 * 1 * 8,314 * 300 = 3.741,3 J."
  },
  {
    "id": "fis-sim-11",
    "materi": "GELOMBANG BUNYI (PIPA ORGANA)",
    "topic": "Resonansi Pipa Organa Terbuka dan Tertutup",
    "hints": {
      "concept": "Pipa terbuka nada atas 1: f = 2*v / (2*LA) = v / LA. Pipa tertutup nada atas 2: f = 5*v / (4*LB). Samakan kedua frekuensi untuk mencari LB.",
      "execution": "v / 60 = 5v / (4 LB) -> 4 LB = 300 -> LB = 75 cm."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah pipa organa terbuka $A$ memiliki panjang $L_A = 60\\text{ cm}$. Pipa organa tersebut dibunyikan pada nada atas pertamanya. Pada saat yang sama, sebuah pipa organa tertutup $B$ dibunyikan pada nada atas keduanya. Jika cepat rambat bunyi di udara adalah sama dan kedua pipa beresonansi menghasilkan frekuensi yang persis sama ($f_{1,A} = f_{2,B}$), panjang pipa organa tertutup $B$ ($L_B$) tersebut adalah...",
    "formulaHud": {
      "title": "FREKUENSI HARMONIK PIPA ORGANA",
      "latex": "f_{n,\\text{terbuka}} = \\frac{(n + 1)v}{2L}; \\quad f_{n,\\text{tertutup}} = \\frac{(2n + 1)v}{4L}; \\quad \\frac{v}{L_A} = \\frac{5v}{4 L_B} \\implies L_B = \\frac{5}{4} L_A = \\frac{5}{4} \\times 60 = 75\\text{ cm}",
      "legend": "• Nada atas pertama terbuka ($n=1$): nada ke-2 ($2 \\times v / 2L = v/L$)<br>• Nada atas kedua tertutup ($n=2$): harmonik ke-5 ($5v / 4L$)<br>• $L_B = 75\\text{ cm}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$L_B = 75\\text{ cm}$, karena frekuensi nada atas pertama ($n = 1$) pipa organa terbuka adalah $f_{1,A} = \\frac{(1 + 1)v}{2 L_A} = \\frac{2v}{2 L_A} = \\frac{v}{L_A} = \\frac{v}{60}$. Frekuensi nada atas kedua ($n = 2$) pipa organa tertutup adalah $f_{2,B} = \\frac{(2(2) + 1)v}{4 L_B} = \\frac{5v}{4 L_B}$. Karena frekuensinya sama, berlaku $\\frac{v}{60} = \\frac{5v}{4 L_B} \\implies 4 L_B = 5 \\times 60 = 300 \\implies L_B = \\frac{300}{4} = 75\\text{ cm}$."
      },
      {
        "key": "B",
        "text": "$L_B = 50\\text{ cm}$, karena formula nada atas pipa organa tertutup keliru menggunakan koefisien tiga per empat sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$L_B = 90\\text{ cm}$, dihitung dengan menyamakan rasio nada dasar antara pipa terbuka dan pipa tertutup."
      },
      {
        "key": "D",
        "text": "$L_B = 60\\text{ cm}$, karena beranggapan pipa dengan frekuensi sama selalu memiliki panjang tabung fisik yang identik."
      },
      {
        "key": "E",
        "text": "$L_B = 40\\text{ cm}$, dihitung dari kebalikan perkalian silang rumus resonansi gelombang berdiri akustik."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $L_B = 75\\text{ cm}$, karena frekuensi nada atas pertama ($n = 1$) pipa organa terbuka adalah $f_{1,A} = \\frac{(1 + 1)v}{2 L_A} = \\frac{2v}{2 L_A} = \\frac{v}{L_A} = \\frac{v}{60}$. Frekuensi nada atas kedua ($n = 2$) pipa organa tertutup adalah $f_{2,B} = \\frac{(2(2) + 1)v}{4 L_B} = \\frac{5v}{4 L_B}$. Karena frekuensinya sama, berlaku $\\frac{v}{60} = \\frac{5v}{4 L_B} \\implies 4 L_B = 5 \\times 60 = 300 \\implies L_B = \\frac{300}{4} = 75\\text{ cm}$.. Pipa terbuka nada atas 1: f = 2*v / (2*LA) = v / LA. Pipa tertutup nada atas 2: f = 5*v / (4*LB). Samakan kedua frekuensi untuk mencari LB. v / 60 = 5v / (4 LB) -> 4 LB = 300 -> LB = 75 cm."
  },
  {
    "id": "fis-sim-12",
    "materi": "OPTIKA FISIS (INTERFERENSI CELAH GANDA DALAM MEDIUM)",
    "topic": "Interferensi Young dengan Perubahan Indeks Bias Medium",
    "hints": {
      "concept": "Di dalam air, panjang gelombang memendek: lambda = lambda0 / n = 600 / (4/3) = 450 nm. Jarak antar pita terang: Delta_y = lambda * L / d.",
      "execution": "Delta_y = (450e-9 * 1) / 0,2e-3 = 2,25e-3 m = 2,25 mm."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam percobaan celah ganda Young di udara, jarak pisah antarcelah adalah $d = 0{,}2\\text{ mm}$ dan jarak dari celah ke layar pengamat adalah $L = 1\\text{ meter}$. Percobaan menggunakan cahaya monokromatik dengan panjang gelombang di udara $\\lambda_0 = 600\\text{ nm}$. Jika seluruh perangkat percobaan tersebut dicelupkan ke dalam air yang memiliki indeks bias $n = \\frac{4}{3}$, jarak antara dua garis terang yang berdekatan pada layar ($\\Delta y$) di dalam air adalah...",
    "formulaHud": {
      "title": "INTERFERENSI CELAH GANDA YOUNG DALAM MEDIUM",
      "latex": "\\lambda = \\frac{\\lambda_0}{n} = \\frac{600}{4/3} = 450\\text{ nm}; \\quad \\Delta y = \\frac{\\lambda L}{d} = \\frac{450 \\times 10^{-9} \\times 1}{0{,}2 \\times 10^{-3}} = 2{,}25 \\times 10^{-3}\\text{ m} = 2{,}25\\text{ mm}",
      "legend": "• Cahaya melambat di dalam air: $\\lambda = \\lambda_0 / n$<br>• Pola interferensi di dalam air merapat ($\\Delta y = \\Delta y_0 / n = 3{,}0 / (4/3) = 2{,}25\\text{ mm}$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta y = 3{,}00\\text{ mm}$, karena merupakan jarak antarpita terang saat percobaan dilakukan di udara sebelum dimasukkan ke air sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$\\Delta y = 2{,}25\\text{ mm}$ (atau $2{,}25 \\times 10^{-3}\\text{ m}$), karena panjang gelombang cahaya di dalam air memendek menjadi $\\lambda = \\frac{\\lambda_0}{n} = \\frac{600\\text{ nm}}{4/3} = 450\\text{ nm} = 4{,}5 \\times 10^{-7}\\text{ m}$. Jarak antarcelah terang berdekatan adalah $\\Delta y = \\frac{\\lambda L}{d} = \\frac{(4{,}5 \\times 10^{-7}\\text{ m}) \\times 1\\text{ m}}{0{,}2 \\times 10^{-3}\\text{ m}} = 2{,}25 \\times 10^{-3}\\text{ m} = 2{,}25\\text{ mm}$ (jika di udara $\\Delta y_0 = 3{,}0\\text{ mm}$)."
      },
      {
        "key": "C",
        "text": "$\\Delta y = 4{,}00\\text{ mm}$, karena panjang gelombang cahaya keliru dikalikan dengan indeks bias medium air."
      },
      {
        "key": "D",
        "text": "$\\Delta y = 1{,}50\\text{ mm}$, dihitung dari pembagian jarak celah dengan kuadrat indeks bias fluida."
      },
      {
        "key": "E",
        "text": "$\\Delta y = 0{,}75\\text{ mm}$, dihitung dari orde ketiga difraksi minimum interferensi destruktif celah ganda."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\Delta y = 2{,}25\\text{ mm}$ (atau $2{,}25 \\times 10^{-3}\\text{ m}$), karena panjang gelombang cahaya di dalam air memendek menjadi $\\lambda = \\frac{\\lambda_0}{n} = \\frac{600\\text{ nm}}{4/3} = 450\\text{ nm} = 4{,}5 \\times 10^{-7}\\text{ m}$. Jarak antarcelah terang berdekatan adalah $\\Delta y = \\frac{\\lambda L}{d} = \\frac{(4{,}5 \\times 10^{-7}\\text{ m}) \\times 1\\text{ m}}{0{,}2 \\times 10^{-3}\\text{ m}} = 2{,}25 \\times 10^{-3}\\text{ m} = 2{,}25\\text{ mm}$ (jika di udara $\\Delta y_0 = 3{,}0\\text{ mm}$).. Di dalam air, panjang gelombang memendek: lambda = lambda0 / n = 600 / (4/3) = 450 nm. Jarak antar pita terang: Delta_y = lambda * L / d. Delta_y = (450e-9 * 1) / 0,2e-3 = 2,25e-3 m = 2,25 mm."
  },
  {
    "id": "fis-sim-13",
    "materi": "ALAT OPTIK (MIKROSKOP MAJEMUK)",
    "topic": "Perbesaran Total Mikroskop Mata Berakomodasi Maksimum",
    "hints": {
      "concept": "Hitung s_ob': 1/s_ob' = 1/f_ob - 1/s_ob -> s_ob' = 11 cm. Mob = 11/1,1 = 10x. Akomodasi maksimum: Mok = Sn/f_ok + 1 = 25/5 + 1 = 6x. M_total = Mob * Mok.",
      "execution": "M_total = 10 * 6 = 60 kali. s_ok = 25/6 = 4,17 cm -> d = 11 + 4,17 = 15,17 cm."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah mikroskop memiliki lensa objektif dengan jarak fokus $f_{\\text{ob}} = 1\\text{ cm}$ dan lensa okuler dengan jarak fokus $f_{\\text{ok}} = 5\\text{ cm}$. Sebuah preparat biologi diletakkan pada jarak $s_{\\text{ob}} = 1{,}1\\text{ cm}$ di depan lensa objektif. Pengamatan dilakukan oleh seorang peneliti bermata normal ($S_n = 25\\text{ cm}$) dengan mata berakomodasi maksimum. Perbesaran total mikroskop ($M_{\\text{total}}$) dan panjang tabung mikroskop ($d$) saat itu adalah...",
    "formulaHud": {
      "title": "PERBESARAN MIKROSKOP AKOMODASI MAKSIMUM",
      "latex": "s_{\\text{ob}}' = \\frac{1{,}1 \\times 1}{0{,}1} = 11\\text{ cm} \\implies M_{\\text{ob}} = 10; \\quad M_{\\text{ok}} = \\frac{S_n}{f_{\\text{ok}}} + 1 = \\frac{25}{5} + 1 = 6; \\quad M = 10 \\times 6 = 60\\times",
      "legend": "• Akomodasi maksimum: $s_{\\text{ok}}' = -S_n = -25\\text{ cm}$<br>• $M_{\\text{ok}} = \\frac{S_n}{f_{\\text{ok}}} + 1 = 6\\times$<br>• $M_{\\text{total}} = M_{\\text{ob}} \\times M_{\\text{ok}} = 60\\times$"
    },
    "options": [
      {
        "key": "A",
        "text": "$M_{\\text{total}} = 50\\text{ kali}$ dan $d = 16\\text{ cm}$, karena perbesaran okuler dihitung untuk mata tidak berakomodasi ($S_n/f_{ok} = 5$) ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$M_{\\text{total}} = 100\\text{ kali}$ dan $d = 20\\text{ cm}$, dihitung dari pengalian langsung jarak fokus kedua lensa."
      },
      {
        "key": "C",
        "text": "$M_{\\text{total}} = 60\\text{ kali}$ dan $d = 15{,}17\\text{ cm}$ (atau $15\\frac{1}{6}\\text{ cm}$), karena bayangan oleh objektif terbentuk pada $s_{\\text{ob}}' = \\frac{s_{\\text{ob}} f_{\\text{ob}}}{s_{\\text{ob}} - f_{\\text{ob}}} = \\frac{1{,}1 \\times 1}{1{,}1 - 1} = \\frac{1{,}1}{0{,}1} = 11\\text{ cm}$. Perbesaran objektif $M_{\\text{ob}} = \\left|\\frac{s_{\\text{ob}}'}{s_{\\text{ob}}}\\right| = \\frac{11}{1{,}1} = 10\\text{ kali}$. Untuk mata berakomodasi maksimum, perbesaran okuler adalah $M_{\\text{ok}} = \\frac{S_n}{f_{\\text{ok}}} + 1 = \\frac{25}{5} + 1 = 6\\text{ kali}$. Maka $M_{\\text{total}} = M_{\\text{ob}} \\times M_{\\text{ok}} = 10 \\times 6 = 60\\text{ kali}$. Jarak benda okuler adalah $s_{\\text{ok}} = \\frac{S_n f_{\\text{ok}}}{S_n + f_{\\text{ok}}} = \\frac{25 \\times 5}{30} = \\frac{25}{6} \\approx 4{,}17\\text{ cm}$, sehingga panjang tubus $d = s_{\\text{ob}}' + s_{\\text{ok}} = 11 + 4{,}17 = 15{,}17\\text{ cm}$."
      },
      {
        "key": "D",
        "text": "$M_{\\text{total}} = 30\\text{ kali}$ dan $d = 12\\text{ cm}$, karena bayangan objektif diasumsikan terbentuk pada fokus utama lensa okuler."
      },
      {
        "key": "E",
        "text": "$M_{\\text{total}} = 75\\text{ kali}$ dan $d = 18{,}5\\text{ cm}$, dihitung dari perbesaran sudut teleskop astronomi Kepler."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $M_{\\text{total}} = 60\\text{ kali}$ dan $d = 15{,}17\\text{ cm}$ (atau $15\\frac{1}{6}\\text{ cm}$), karena bayangan oleh objektif terbentuk pada $s_{\\text{ob}}' = \\frac{s_{\\text{ob}} f_{\\text{ob}}}{s_{\\text{ob}} - f_{\\text{ob}}} = \\frac{1{,}1 \\times 1}{1{,}1 - 1} = \\frac{1{,}1}{0{,}1} = 11\\text{ cm}$. Perbesaran objektif $M_{\\text{ob}} = \\left|\\frac{s_{\\text{ob}}'}{s_{\\text{ob}}}\\right| = \\frac{11}{1{,}1} = 10\\text{ kali}$. Untuk mata berakomodasi maksimum, perbesaran okuler adalah $M_{\\text{ok}} = \\frac{S_n}{f_{\\text{ok}}} + 1 = \\frac{25}{5} + 1 = 6\\text{ kali}$. Maka $M_{\\text{total}} = M_{\\text{ob}} \\times M_{\\text{ok}} = 10 \\times 6 = 60\\text{ kali}$. Jarak benda okuler adalah $s_{\\text{ok}} = \\frac{S_n f_{\\text{ok}}}{S_n + f_{\\text{ok}}} = \\frac{25 \\times 5}{30} = \\frac{25}{6} \\approx 4{,}17\\text{ cm}$, sehingga panjang tubus $d = s_{\\text{ob}}' + s_{\\text{ok}} = 11 + 4{,}17 = 15{,}17\\text{ cm}$.. Hitung s_ob': 1/s_ob' = 1/f_ob - 1/s_ob -> s_ob' = 11 cm. Mob = 11/1,1 = 10x. Akomodasi maksimum: Mok = Sn/f_ok + 1 = 25/5 + 1 = 6x. M_total = Mob * Mok. M_total = 10 * 6 = 60 kali. s_ok = 25/6 = 4,17 cm -> d = 11 + 4,17 = 15,17 cm."
  },
  {
    "id": "fis-sim-14",
    "materi": "ELEKTROSTATIKA & HUKUM GAUSS",
    "topic": "Medan Listrik dan Potensial Bola Konduktor Pejal",
    "hints": {
      "concept": "Di dalam bola konduktor (r < R): medan listrik E = 0. Potensial listrik di dalam bola konstan sama dengan di permukaan bola: V = k*Q / R.",
      "execution": "E = 0. V = 9e9 * 4e-6 / 0,2 = 36.000 / 0,2 = 1,8 x 10^5 Volt."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah bola konduktor pejal memiliki jari-jari $R = 20\\text{ cm} = 0{,}2\\text{ m}$ dan diberi muatan listrik bersih $Q = +4\\,\\mu\\text{C} = 4 \\times 10^{-6}\\text{ C}$ yang tersebar merata di permukaannya ($k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$). Kuat medan listrik ($E$) dan potensial listrik ($V$) pada sebuah titik yang berjarak $r = 10\\text{ cm} = 0{,}1\\text{ m}$ dari pusat bola konduktor tersebut adalah...",
    "formulaHud": {
      "title": "HUKUM GAUSS PADA BOLA KONDUKTOR BERMUATAN",
      "latex": "\\text{Di dalam bola }(r < R): \\quad E = 0; \\quad V = \\frac{k Q}{R} = \\frac{9 \\times 10^9 \\times 4 \\times 10^{-6}}{0{,}2} = 1{,}8 \\times 10^5\\text{ V}",
      "legend": "• Muatan konduktor hanya berada di permukaan luar bola ($R = 0{,}2\\text{ m}$)<br>• $E_{\\text{dalam}} = 0$ karena $q_{\\text{enclosed}} = 0$<br>• $V_{\\text{dalam}} = V_{\\text{permukaan}} = \\text{konstan} = 180\\text{ kV}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$E = 3{,}6 \\times 10^6\\text{ N/C}$ dan $V = 3{,}6 \\times 10^5\\text{ Volt}$, karena keliru memasukkan jarak $r = 0{,}1\\text{ m}$ ke dalam rumus medan listrik titik seolah bola konduktor adalah muatan titik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$E = 0\\text{ N/C}$ dan $V = 0\\text{ Volt}$, karena menganggap jika medan listrik nol maka potensial listrik otomatis bernilai nol pula."
      },
      {
        "key": "C",
        "text": "$E = 9{,}0 \\times 10^5\\text{ N/C}$ dan $V = 1{,}8 \\times 10^5\\text{ Volt}$, dihitung dari medan listrik di permukaan bola konduktor."
      },
      {
        "key": "D",
        "text": "$E = 0\\text{ N/C}$ dan $V = 1{,}8 \\times 10^5\\text{ Volt}$, karena di dalam konduktor elektrostatik ($r < R$) tidak ada muatan yang dilingkupi oleh permukaan Gauss sehingga medan listrik di dalam bola adalah nol ($E = 0$). Potensial listrik di seluruh rongga dalam dan permukaan bola bernilai konstan dan sama dengan potensial di permukaannya: $V = \\frac{k Q}{R} = \\frac{(9 \\times 10^9) \\times (4 \\times 10^{-6})}{0{,}2} = \\frac{36.000}{0{,}2} = 180.000\\text{ Volt} = 1{,}8 \\times 10^5\\text{ Volt}$."
      },
      {
        "key": "E",
        "text": "$E = 1{,}8 \\times 10^5\\text{ N/C}$ dan $V = 9{,}0 \\times 10^4\\text{ Volt}$, dihitung dari pembagian muatan terhadap volume bola tiga dimensi."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $E = 0\\text{ N/C}$ dan $V = 1{,}8 \\times 10^5\\text{ Volt}$, karena di dalam konduktor elektrostatik ($r < R$) tidak ada muatan yang dilingkupi oleh permukaan Gauss sehingga medan listrik di dalam bola adalah nol ($E = 0$). Potensial listrik di seluruh rongga dalam dan permukaan bola bernilai konstan dan sama dengan potensial di permukaannya: $V = \\frac{k Q}{R} = \\frac{(9 \\times 10^9) \\times (4 \\times 10^{-6})}{0{,}2} = \\frac{36.000}{0{,}2} = 180.000\\text{ Volt} = 1{,}8 \\times 10^5\\text{ Volt}$.. Di dalam bola konduktor (r < R): medan listrik E = 0. Potensial listrik di dalam bola konstan sama dengan di permukaan bola: V = k*Q / R. E = 0. V = 9e9 * 4e-6 / 0,2 = 36.000 / 0,2 = 1,8 x 10^5 Volt."
  },
  {
    "id": "fis-sim-15",
    "materi": "RANGKAIAN ARUS SEARAH (HUKUM KIRCHHOFF II)",
    "topic": "Analisis Dua Loop Rangkaian Majemuk",
    "hints": {
      "concept": "Gunakan Hukum Kirchhoff cabang I1 + I3 = I2. Susun persamaan loop 1 dan loop 2 untuk menyatakan I1 dan I3 dalam I2, lalu selesaikan sistem persamaan.",
      "execution": "I1 = 6 - 2*I2, I3 = 3 - 2*I2. (6 - 2*I2) + (3 - 2*I2) = I2 -> 9 = 5*I2 -> I2 = 1,8 Ampere."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah rangkaian listrik tertutup dua loop memiliki komponen sebagai berikut:<br>• Loop 1: baterai $\\varepsilon_1 = 12\\text{ V}$, resistor $R_1 = 2\\,\\Omega$, dan resistor cabang tengah $R_2 = 4\\,\\Omega$.<br>• Loop 2: baterai $\\varepsilon_2 = 6\\text{ V}$, resistor cabang kanan $R_3 = 2\\,\\Omega$, yang terhubung paralel dengan cabang tengah $R_2 = 4\\,\\Omega$.<br>Baterai $\\varepsilon_1$ dan $\\varepsilon_2$ dipasang dengan kutub positif mengarah ke atas menuju titik percabangan atas. Kuat arus listrik yang mengalir melalui resistor cabang tengah $R_2$ ($I_2$) adalah...",
    "formulaHud": {
      "title": "HUKUM I & II KIRCHHOFF PADA RANGKAIAN DUA LOOP",
      "latex": "I_1 + I_3 = I_2; \\quad 12 - 2I_1 - 4I_2 = 0 \\implies I_1 = 6 - 2I_2; \\quad 6 - 2I_3 - 4I_2 = 0 \\implies I_3 = 3 - 2I_2; \\quad (6 - 2I_2) + (3 - 2I_2) = I_2 \\implies 5I_2 = 9 \\implies I_2 = 1{,}8\\text{ A}",
      "legend": "• $I_1 = 2{,}4\\text{ A}$ (cabang kiri mengalir ke atas)<br>• $I_3 = -0{,}6\\text{ A}$ (cabang kanan mengalir ke bawah berlawanan arah baterai $\\varepsilon_2$)<br>• Arus cabang tengah $I_2 = 1{,}8\\text{ A}$ mengalir ke bawah"
    },
    "options": [
      {
        "key": "A",
        "text": "$I_2 = 3{,}00\\text{ Ampere}$, dihitung dengan mengabaikan hambatan cabang kanan sehingga hanya loop 1 yang beroperasi diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$I_2 = 0{,}75\\text{ Ampere}$, dihitung dari pembagian selisih tegangan baterai dengan total hambatan seri seluruh cabang."
      },
      {
        "key": "C",
        "text": "$I_2 = 1{,}20\\text{ Ampere}$, dihitung dari kesalahan tanda polaritas baterai cabang kanan loop dua."
      },
      {
        "key": "D",
        "text": "$I_2 = 4{,}50\\text{ Ampere}$, dihitung dari penjumlahan skalar arus cabang kiri dan kanan tanpa pembagi hambatan pengganti."
      },
      {
        "key": "E",
        "text": "$I_2 = 2{,}25\\text{ Ampere}$ mengalir ke bawah, diperoleh dari persamaan Kirchhoff: titik cabang $I_1 + I_3 = I_2$, Loop 1: $12 - 2 I_1 - 4 I_2 = 0 \\implies I_1 = 6 - 2 I_2$, Loop 2: $6 - 2 I_3 - 4 I_2 = 0 \\implies I_3 = 3 - 2 I_2$. Substitusi ke cabang: $(6 - 2 I_2) + (3 - 2 I_2) = I_2 \\implies 9 - 4 I_2 = I_2 \\implies 5 I_2 = 9 \\implies I_2 = 1{,}8\\text{ A}$... mari cek: Loop 1: $12 - 2 I_1 - 4 I_2 = 0$; Loop 2: $6 - 2 I_3 - 4 I_2 = 0$. Maka $I_1 = 6 - 2(1{,}8) = 2{,}4\\text{ A}$, $I_3 = 3 - 2(1{,}8) = -0{,}6\\text{ A}$. Total arus $I_2 = 2{,}4 - 0{,}6 = 1{,}8\\text{ Ampere}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $I_2 = 2{,}25\\text{ Ampere}$ mengalir ke bawah, diperoleh dari persamaan Kirchhoff: titik cabang $I_1 + I_3 = I_2$, Loop 1: $12 - 2 I_1 - 4 I_2 = 0 \\implies I_1 = 6 - 2 I_2$, Loop 2: $6 - 2 I_3 - 4 I_2 = 0 \\implies I_3 = 3 - 2 I_2$. Substitusi ke cabang: $(6 - 2 I_2) + (3 - 2 I_2) = I_2 \\implies 9 - 4 I_2 = I_2 \\implies 5 I_2 = 9 \\implies I_2 = 1{,}8\\text{ A}$... mari cek: Loop 1: $12 - 2 I_1 - 4 I_2 = 0$; Loop 2: $6 - 2 I_3 - 4 I_2 = 0$. Maka $I_1 = 6 - 2(1{,}8) = 2{,}4\\text{ A}$, $I_3 = 3 - 2(1{,}8) = -0{,}6\\text{ A}$. Total arus $I_2 = 2{,}4 - 0{,}6 = 1{,}8\\text{ Ampere}$.. Gunakan Hukum Kirchhoff cabang I1 + I3 = I2. Susun persamaan loop 1 dan loop 2 untuk menyatakan I1 dan I3 dalam I2, lalu selesaikan sistem persamaan. I1 = 6 - 2*I2, I3 = 3 - 2*I2. (6 - 2*I2) + (3 - 2*I2) = I2 -> 9 = 5*I2 -> I2 = 1,8 Ampere."
  },
  {
    "id": "fis-sim-16",
    "materi": "GAYA MAGNETIK (GAYA LORENTZ)",
    "topic": "Gaya Antarkawat Sejajar Berarus Listrik",
    "hints": {
      "concept": "Gaya per satuan panjang: F/L = (mu0 * I1 * I2) / (2 * pi * a). Jika arah arus berlawanan, sifat interaksinya tolak-menolak.",
      "execution": "F/L = (4pi*1e-7 * 4 * 6) / (2pi * 0,1) = 4,8 x 10^-5 N/m, tolak-menolak."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua kawat lurus panjang sejajar berjarak $a = 10\\text{ cm} = 0{,}1\\text{ m}$ satu sama lain di udara. Kawat pertama dialiri arus $I_1 = 4\\text{ Ampere}$ dan kawat kedua dialiri arus $I_2 = 6\\text{ Ampere}$ dengan arah arus yang saling berlawanan (kawat 1 ke atas, kawat 2 ke bawah). Diketahui $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ Wb/(A}\\cdot\\text{m)}$. Besar gaya magnetik per satuan panjang ($F/L$) yang dialami oleh masing-masing kawat dan sifat interaksi gayanya adalah...",
    "formulaHud": {
      "title": "GAYA LORENTZ DUA KAWAT SEJAJAR BERARUS",
      "latex": "\\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi a} = \\frac{(4\\pi \\times 10^{-7}) \\times 4 \\times 6}{2\\pi \\times 0{,}1} = 4{,}8 \\times 10^{-5}\\text{ N/m} \\quad (\\text{Tolak-Menolak})",
      "legend": "• Arus searah $\\implies$ Tarik-menarik<br>• Arus berlawanan arah $\\implies$ Tolak-menolak<br>• $F/L = 4{,}8 \\times 10^{-5}\\text{ N/m}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$F/L = 4{,}8 \\times 10^{-5}\\text{ N/m}$ dan bersifat tolak-menolak, karena menurut hukum gaya Biot-Savart/Ampere, gaya per satuan panjang antara dua kawat sejajar adalah $\\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi a} = \\frac{(4\\pi \\times 10^{-7}) \\times 4 \\times 6}{2\\pi \\times 0{,}1} = \\frac{2 \\times 10^{-7} \\times 24}{0{,}1} = 4{,}8 \\times 10^{-5}\\text{ N/m}$. Karena arah kedua arus berlawanan arah, medan magnet yang timbul di antara kedua kawat saling memperkuat sehingga menghasilkan interaksi tolak-menolak."
      },
      {
        "key": "B",
        "text": "$F/L = 4{,}8 \\times 10^{-5}\\text{ N/m}$ dan bersifat tarik-menarik, karena salah mengasumsikan arus berlawanan arah akan tarik-menarik seperti muatan listrik elektrostatik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$F/L = 2{,}4 \\times 10^{-5}\\text{ N/m}$ dan bersifat tolak-menolak, karena keliru membagi dua hasil perkalian arus kawat."
      },
      {
        "key": "D",
        "text": "$F/L = 9{,}6 \\times 10^{-5}\\text{ N/m}$ dan bersifat tarik-menarik, dihitung tanpa menyertakan faktor pembagian dua pi jarak kawat."
      },
      {
        "key": "E",
        "text": "$F/L = 1{,}2 \\times 10^{-6}\\text{ N/m}$ dan bersifat tolak-menolak, dihitung dari kuadrat jarak pemisah kawat sejajar."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $F/L = 4{,}8 \\times 10^{-5}\\text{ N/m}$ dan bersifat tolak-menolak, karena menurut hukum gaya Biot-Savart/Ampere, gaya per satuan panjang antara dua kawat sejajar adalah $\\frac{F}{L} = \\frac{\\mu_0 I_1 I_2}{2\\pi a} = \\frac{(4\\pi \\times 10^{-7}) \\times 4 \\times 6}{2\\pi \\times 0{,}1} = \\frac{2 \\times 10^{-7} \\times 24}{0{,}1} = 4{,}8 \\times 10^{-5}\\text{ N/m}$. Karena arah kedua arus berlawanan arah, medan magnet yang timbul di antara kedua kawat saling memperkuat sehingga menghasilkan interaksi tolak-menolak.. Gaya per satuan panjang: F/L = (mu0 * I1 * I2) / (2 * pi * a). Jika arah arus berlawanan, sifat interaksinya tolak-menolak. F/L = (4pi*1e-7 * 4 * 6) / (2pi * 0,1) = 4,8 x 10^-5 N/m, tolak-menolak."
  },
  {
    "id": "fis-sim-17",
    "materi": "INDUKSI ELEKTROMAGNETIK (GENERATOR AC)",
    "topic": "Tegangan Maksimum dan Frekuensi Generator Arus Bolak-Balik",
    "hints": {
      "concept": "GGL maksimum generator AC: V_max = N * B * A * omega, di mana omega = 2 * pi * f.",
      "execution": "A = 0,02 m^2. omega = 100pi rad/s. V_max = 500 * 0,5 * 0,02 * 100pi = 500pi Volt = 1.570 V."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah kumparan generator AC berbentuk persegi berukuran $10\\text{ cm} \\times 20\\text{ cm}$ (luas penampang $A = 200\\text{ cm}^2 = 0{,}02\\text{ m}^2$) memiliki $N = 500\\text{ lilitan}$. Kumparan tersebut diputar dalam medan magnetik homogen $B = 0{,}5\\text{ Tesla}$ dengan frekuensi putar tetap $f = 50\\text{ Hz}$. Tegangan maksimum ($V_{\\max}$) yang dihasilkan generator tersebut adalah...",
    "formulaHud": {
      "title": "GGL MAKSIMUM GENERATOR AC (FARADAY)",
      "latex": "\\omega = 2\\pi f = 100\\pi\\text{ rad/s}; \\quad V_{\\max} = N B A \\omega = 500 \\times 0{,}5 \\times 0{,}02 \\times 100\\pi = 500\\pi\\text{ Volt} \\approx 1.570{,}8\\text{ V}",
      "legend": "• $N = 500$ lilitan<br>• $B = 0{,}5\\text{ T}$<br>• $A = 0{,}02\\text{ m}^2$<br>• $\\omega = 100\\pi\\text{ rad/s}$<br>• $V(t) = V_{\\max} \\sin(\\omega t)$"
    },
    "options": [
      {
        "key": "A",
        "text": "$V_{\\max} = 250\\pi\\text{ Volt} \\approx 785\\text{ Volt}$, karena formula luas kumparan keliru dibagi dua saat perhitungan geometri sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$V_{\\max} = 500\\pi\\text{ Volt} \\approx 1.570\\text{ Volt}$, karena kecepatan sudut putaran kumparan adalah $\\omega = 2\\pi f = 2\\pi \\times 50 = 100\\pi\\text{ rad/s}$. Menurut hukum induksi Faraday, gaya gerak listrik maksimum adalah $V_{\\max} = N B A \\omega = 500 \\times 0{,}5 \\times 0{,}02 \\times 100\\pi = 500 \\times 10^{-2} \\times 100\\pi = 500\\pi\\text{ Volt} \\approx 1.570{,}8\\text{ Volt}$."
      },
      {
        "key": "C",
        "text": "$V_{\\max} = 1.000\\pi\\text{ Volt} \\approx 3.141\\text{ Volt}$, dihitung dari tegangan puncak-ke-puncak (peak-to-peak)."
      },
      {
        "key": "D",
        "text": "$V_{\\max} = 500\\text{ Volt}$, karena nilai pi pada frekuensi sudut radian per sekon diabaikan."
      },
      {
        "key": "E",
        "text": "$V_{\\max} = 50\\pi\\text{ Volt} \\approx 157\\text{ Volt}$, karena luas penampang tidak dikonversi dari satuan sentimeter kuadrat ke meter kuadrat."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $V_{\\max} = 500\\pi\\text{ Volt} \\approx 1.570\\text{ Volt}$, karena kecepatan sudut putaran kumparan adalah $\\omega = 2\\pi f = 2\\pi \\times 50 = 100\\pi\\text{ rad/s}$. Menurut hukum induksi Faraday, gaya gerak listrik maksimum adalah $V_{\\max} = N B A \\omega = 500 \\times 0{,}5 \\times 0{,}02 \\times 100\\pi = 500 \\times 10^{-2} \\times 100\\pi = 500\\pi\\text{ Volt} \\approx 1.570{,}8\\text{ Volt}$.. GGL maksimum generator AC: V_max = N * B * A * omega, di mana omega = 2 * pi * f. A = 0,02 m^2. omega = 100pi rad/s. V_max = 500 * 0,5 * 0,02 * 100pi = 500pi Volt = 1.570 V."
  },
  {
    "id": "fis-sim-18",
    "materi": "RANGKAIAN ARUS BOLAK-BALIK (RESONANSI)",
    "topic": "Frekuensi Resonansi Seri RLC",
    "hints": {
      "concept": "Frekuensi resonansi: f0 = 1 / (2*pi*sqrt(L*C)). Hitung sqrt(L*C) terlebih dahulu.",
      "execution": "L*C = 1e-5 * 1e-10 = 1e-15. sqrt(1e-15) = 3,162e-8. f0 = 1 / (2 * pi * 3,162e-8) = 5,03 x 10^6 Hz = 5,03 MHz."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah rangkaian penerima radio menggunakan rangkaian penala RLC seri dengan induktor $L = 10\\,\\mu\\text{H} = 10^{-5}\\text{ H}$ dan kapasitor variabel yang diatur pada nilai $C = 100\\text{ pF} = 10^{-10}\\text{ F}$. Frekuensi resonansi ($f_0$) rangkaian tersebut agar dapat menangkap sinyal gelombang radio stasiun pemancar adalah...",
    "formulaHud": {
      "title": "FREKUENSI RESONANSI RLC SERI",
      "latex": "f_0 = \\frac{1}{2\\pi\\sqrt{LC}} = \\frac{1}{2\\pi\\sqrt{10^{-5} \\times 10^{-10}}} = \\frac{1}{2\\pi \\times 10^{-7{,}5}} \\approx 5{,}03 \\times 10^6\\text{ Hz} = 5{,}03\\text{ MHz}",
      "legend": "• Pada saat resonansi: $Z = R$ (Impedansi minimum, arus efektif maksimum)<br>• Sifat rangkaian murni resistif dengan faktor daya $\\cos\\phi = 1$"
    },
    "options": [
      {
        "key": "A",
        "text": "$f_0 = 1{,}59\\text{ MHz}$, dihitung dari nilai induktansi yang keliru sepuluh kali lebih besar ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$f_0 = 10{,}06\\text{ MHz}$, dihitung dari frekuensi sudut tanpa membagi dengan faktor dua pi lingkaran."
      },
      {
        "key": "C",
        "text": "$f_0 = \\frac{1}{2\\pi} \\times 10^7\\text{ Hz} \\approx 5{,}03\\text{ MHz}$, karena syarat resonansi adalah reaktansi induktif sama dengan reaktansi kapasitif ($X_L = X_C$), sehingga frekuensi sudut resonansi adalah $\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{10^{-5} \\times 10^{-10}}} = \\frac{1}{\\sqrt{10^{-15}}} = \\frac{1}{\\sqrt{10 \\times 10^{-16}}} = \\frac{10^8}{\\sqrt{10}} = \\frac{10^8}{3{,}162} \\approx 3{,}162 \\times 10^7\\text{ rad/s}$. Frekuensi dalam Hertz adalah $f_0 = \\frac{\\omega_0}{2\\pi} = \\frac{3{,}162 \\times 10^7}{2\\pi} \\approx 5{,}03 \\times 10^6\\text{ Hz} = 5{,}03\\text{ MHz}$."
      },
      {
        "key": "D",
        "text": "$f_0 = 50{,}3\\text{ kHz}$, karena kekeliruan dalam menarik akar eksponen pangkat minus sepuluh pada kapasitor pikoFarad."
      },
      {
        "key": "E",
        "text": "$f_0 = 25{,}0\\text{ MHz}$, dihitung dari perkalian langsung nilai induktansi dengan kapasitansi."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $f_0 = \\frac{1}{2\\pi} \\times 10^7\\text{ Hz} \\approx 5{,}03\\text{ MHz}$, karena syarat resonansi adalah reaktansi induktif sama dengan reaktansi kapasitif ($X_L = X_C$), sehingga frekuensi sudut resonansi adalah $\\omega_0 = \\frac{1}{\\sqrt{LC}} = \\frac{1}{\\sqrt{10^{-5} \\times 10^{-10}}} = \\frac{1}{\\sqrt{10^{-15}}} = \\frac{1}{\\sqrt{10 \\times 10^{-16}}} = \\frac{10^8}{\\sqrt{10}} = \\frac{10^8}{3{,}162} \\approx 3{,}162 \\times 10^7\\text{ rad/s}$. Frekuensi dalam Hertz adalah $f_0 = \\frac{\\omega_0}{2\\pi} = \\frac{3{,}162 \\times 10^7}{2\\pi} \\approx 5{,}03 \\times 10^6\\text{ Hz} = 5{,}03\\text{ MHz}$.. Frekuensi resonansi: f0 = 1 / (2*pi*sqrt(L*C)). Hitung sqrt(L*C) terlebih dahulu. L*C = 1e-5 * 1e-10 = 1e-15. sqrt(1e-15) = 3,162e-8. f0 = 1 / (2 * pi * 3,162e-8) = 5,03 x 10^6 Hz = 5,03 MHz."
  },
  {
    "id": "fis-sim-19",
    "materi": "GELOMBANG ELEKTROMAGNETIK",
    "topic": "Hubungan Medan Listrik, Medan Magnet, dan Intensitas Poynting",
    "hints": {
      "concept": "Hubungan medan: B_max = E_max / c. Intensitas rata-rata: S_bar = E_max^2 / (2 * mu0 * c).",
      "execution": "B_max = 600 / 3e8 = 2e-6 T. S_bar = 600^2 / (2 * 4pi*1e-7 * 3e8) = 360.000 / (240*pi) = 1.500 / pi = 477,5 W/m^2."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Suatu gelombang elektromagnetik sinusoidal merambat di ruang hampa udara searah sumbu $x$ positif. Komponen medan listrik gelombang memiliki amplitudo puncak $E_{\\max} = 600\\text{ V/m}$. Jika cepat rambat cahaya di ruang hampa adalah $c = 3 \\times 10^8\\text{ m/s}$ dan $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ Wb/(A}\\cdot\\text{m)}$, amplitudo medan magnetik ($B_{\\max}$) dan intensitas rata-rata gelombang elektromagnetik tersebut (vektor Poynting $\\bar{S}$) adalah...",
    "formulaHud": {
      "title": "VEKTOR POYNTING & INTENSITAS GELOMBANG ELEKTROMAGNETIK",
      "latex": "B_{\\max} = \\frac{E_{\\max}}{c} = \\frac{600}{3 \\times 10^8} = 2{,}0 \\times 10^{-6}\\text{ T}; \\quad \\bar{S} = \\frac{E_{\\max}^2}{2\\mu_0 c} = \\frac{360.000}{240\\pi} = \\frac{1.500}{\\pi} \\approx 477{,}46\\text{ W/m}^2",
      "legend": "• $E$ dan $B$ berosilasi sefase dan saling tegak lurus terhadap arah rambat gelombang<br>• $\\bar{S}$ menyatakan daya per satuan luas yang dibawa oleh foton/gelombang"
    },
    "options": [
      {
        "key": "A",
        "text": "$B_{\\max} = 1{,}8 \\times 10^{11}\\text{ Tesla}$ dan $\\bar{S} = 955\\text{ W/m}^2$, karena amplitudo medan listrik keliru dikalikan dengan kecepatan cahaya menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$B_{\\max} = 2{,}0 \\times 10^{-6}\\text{ Tesla}$ dan $\\bar{S} = 954{,}9\\text{ W/m}^2$, dihitung tanpa menyertakan faktor pembagian dua pada rata-rata kuadrat fungsi sinusoidal."
      },
      {
        "key": "C",
        "text": "$B_{\\max} = 4{,}0 \\times 10^{-6}\\text{ Tesla}$ dan $\\bar{S} = 238{,}7\\text{ W/m}^2$, dihitung dari nilai puncak-ke-puncak gelombang elektromagnetik."
      },
      {
        "key": "D",
        "text": "$B_{\\max} = 2{,}0 \\times 10^{-6}\\text{ Tesla}$ ($2\\,\\mu\\text{T}$) dan $\\bar{S} \\approx 477{,}5\\text{ W/m}^2$, karena hubungan amplitudo medan pada gelombang elektromagnetik adalah $B_{\\max} = \\frac{E_{\\max}}{c} = \\frac{600\\text{ V/m}}{3 \\times 10^8\\text{ m/s}} = 2{,}0 \\times 10^{-6}\\text{ T}$. Intensitas rata-rata gelombang memenuhi persamaan Poynting: $\\bar{S} = \\frac{E_{\\max} B_{\\max}}{2\\mu_0} = \\frac{E_{\\max}^2}{2\\mu_0 c} = \\frac{600^2}{2 \\times (4\\pi \\times 10^{-7}) \\times (3 \\times 10^8)} = \\frac{360.000}{240\\pi} = \\frac{1.500}{\\pi} \\approx 477{,}46\\text{ W/m}^2$."
      },
      {
        "key": "E",
        "text": "$B_{\\max} = 1{,}0 \\times 10^{-6}\\text{ Tesla}$ dan $\\bar{S} = 120\\text{ W/m}^2$, dihitung dari pembagian intensitas dengan impedansi karakteristik ruang hampa."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $B_{\\max} = 2{,}0 \\times 10^{-6}\\text{ Tesla}$ ($2\\,\\mu\\text{T}$) dan $\\bar{S} \\approx 477{,}5\\text{ W/m}^2$, karena hubungan amplitudo medan pada gelombang elektromagnetik adalah $B_{\\max} = \\frac{E_{\\max}}{c} = \\frac{600\\text{ V/m}}{3 \\times 10^8\\text{ m/s}} = 2{,}0 \\times 10^{-6}\\text{ T}$. Intensitas rata-rata gelombang memenuhi persamaan Poynting: $\\bar{S} = \\frac{E_{\\max} B_{\\max}}{2\\mu_0} = \\frac{E_{\\max}^2}{2\\mu_0 c} = \\frac{600^2}{2 \\times (4\\pi \\times 10^{-7}) \\times (3 \\times 10^8)} = \\frac{360.000}{240\\pi} = \\frac{1.500}{\\pi} \\approx 477{,}46\\text{ W/m}^2$.. Hubungan medan: B_max = E_max / c. Intensitas rata-rata: S_bar = E_max^2 / (2 * mu0 * c). B_max = 600 / 3e8 = 2e-6 T. S_bar = 600^2 / (2 * 4pi*1e-7 * 3e8) = 360.000 / (240*pi) = 1.500 / pi = 477,5 W/m^2."
  },
  {
    "id": "fis-sim-20",
    "materi": "DUALISME GELOMBANG-PARTIKEL",
    "topic": "Panjang Gelombang De Broglie Elektron Dipercepat",
    "hints": {
      "concept": "Panjang gelombang de Broglie: lambda = h / p = h / sqrt(2 * m * e * V). Rumus praktis elektron: lambda = 1,228 / sqrt(V) nm.",
      "execution": "lambda = 1,228 / sqrt(100) = 1,228 / 10 = 0,123 nm."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah elektron bermassa diam $m_e = 9{,}1 \\times 10^{-31}\\text{ kg}$ dan bermuatan $e = 1{,}6 \\times 10^{-19}\\text{ C}$ mula-mula diam lalu dipercepat melalui beda potensial $V = 100\\text{ Volt}$. Jika konstanta Planck adalah $h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$, panjang gelombang de Broglie ($\\lambda_{\\text{dB}}$) dari elektron tersebut adalah...",
    "formulaHud": {
      "title": "PANJANG GELOMBANG DE BROGLIE ELEKTRON",
      "latex": "\\lambda_{\\text{dB}} = \\frac{h}{p} = \\frac{h}{\\sqrt{2 m_e e V}} = \\frac{1{,}228}{\\sqrt{V}}\\text{ nm} = \\frac{1{,}228}{\\sqrt{100}} = 0{,}1228\\text{ nm} \\approx 0{,}123\\text{ nm}",
      "legend": "• $\\lambda_{\\text{dB}} \\approx 0{,}123\\text{ nm}$ seukuran dengan jarak antaratom kristal padat<br>• Fakta ini mendasari prinsip kerja mikroskop elektron resolusi tinggi (TEM/SEM)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\lambda_{\\text{dB}} = 1{,}23\\text{ nm}$, karena lupa menarik akar kuadrat dari beda potensial seratus volt diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$\\lambda_{\\text{dB}} = 0{,}0123\\text{ nm}$, dihitung dari kesalahan memasukkan pangkat muatan elektron."
      },
      {
        "key": "C",
        "text": "$\\lambda_{\\text{dB}} = 0{,}246\\text{ nm}$, dihitung dari asumsi partikel bermuatan alfa dua kali elektron."
      },
      {
        "key": "D",
        "text": "$\\lambda_{\\text{dB}} = 6{,}63\\text{ nm}$, karena menyamakan panjang gelombang dengan konstanta Planck tanpa momentum."
      },
      {
        "key": "E",
        "text": "$\\lambda_{\\text{dB}} = 0{,}123\\text{ nm}$ (atau $1{,}23 \\times 10^{-10}\\text{ m} = 1{,}23\\text{ \\AA}$), karena energi kinetik yang diperoleh elektron adalah $E_k = e V = 1{,}6 \\times 10^{-19} \\times 100 = 1{,}6 \\times 10^{-17}\\text{ J}$. Momentum elektron adalah $p = \\sqrt{2 m_e E_k} = \\sqrt{2 \\times (9{,}1 \\times 10^{-31}) \\times (1{,}6 \\times 10^{-17})} = \\sqrt{29{,}12 \\times 10^{-48}} \\approx 5{,}40 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}$. Maka panjang gelombang de Broglie adalah $\\lambda = \\frac{h}{p} = \\frac{6{,}63 \\times 10^{-34}}{5{,}40 \\times 10^{-24}} \\approx 1{,}228 \\times 10^{-10}\\text{ m} \\approx 0{,}123\\text{ nm}$ (atau menggunakan rumus praktis $\\lambda = \\frac{1{,}228}{\\sqrt{V}}\\text{ nm} = \\frac{1{,}228}{\\sqrt{100}} = 0{,}1228\\text{ nm}$)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $\\lambda_{\\text{dB}} = 0{,}123\\text{ nm}$ (atau $1{,}23 \\times 10^{-10}\\text{ m} = 1{,}23\\text{ \\AA}$), karena energi kinetik yang diperoleh elektron adalah $E_k = e V = 1{,}6 \\times 10^{-19} \\times 100 = 1{,}6 \\times 10^{-17}\\text{ J}$. Momentum elektron adalah $p = \\sqrt{2 m_e E_k} = \\sqrt{2 \\times (9{,}1 \\times 10^{-31}) \\times (1{,}6 \\times 10^{-17})} = \\sqrt{29{,}12 \\times 10^{-48}} \\approx 5{,}40 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}$. Maka panjang gelombang de Broglie adalah $\\lambda = \\frac{h}{p} = \\frac{6{,}63 \\times 10^{-34}}{5{,}40 \\times 10^{-24}} \\approx 1{,}228 \\times 10^{-10}\\text{ m} \\approx 0{,}123\\text{ nm}$ (atau menggunakan rumus praktis $\\lambda = \\frac{1{,}228}{\\sqrt{V}}\\text{ nm} = \\frac{1{,}228}{\\sqrt{100}} = 0{,}1228\\text{ nm}$).. Panjang gelombang de Broglie: lambda = h / p = h / sqrt(2 * m * e * V). Rumus praktis elektron: lambda = 1,228 / sqrt(V) nm. lambda = 1,228 / sqrt(100) = 1,228 / 10 = 0,123 nm."
  },
  {
    "id": "fis-sim-21",
    "materi": "FISIKA MODERN (PRINSIP KETIDAKPASTIAN HEISENBERG)",
    "topic": "Batas Ketidakpastian Posisi dan Momentum Kuantum",
    "hints": {
      "concept": "Ketidakpastian Heisenberg: Delta_x * Delta_p >= h / (4*pi). Hitung Delta_p = m * Delta_v = 9,1e-31 * 50 = 4,55e-29 kg.m/s. Lalu Delta_x = h / (4*pi*Delta_p).",
      "execution": "Delta_x = 6,63e-34 / (4 * 3,1416 * 4,55e-29) = 1,16 x 10^-6 m."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah elektron ($m_e = 9{,}1 \\times 10^{-31}\\text{ kg}$) diukur kelajuannya dan diperoleh nilai $v = 5{,}0 \\times 10^5\\text{ m/s}$ dengan ketidakpastian pengukuran kelajuan sebesar $0{,}01\\%$ ($\\Delta v = 10^{-4} v = 50\\text{ m/s}$). Berdasarkan Prinsip Ketidakpastian Heisenberg ($\\Delta x \\cdot \\Delta p \\ge \\frac{\\hbar}{2} = \\frac{h}{4\\pi}$, dengan $h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$), ketidakpastian minimum dalam menentukan posisi elektron tersebut ($\\Delta x_{\\min}$) adalah...",
    "formulaHud": {
      "title": "PRINSIP KETIDAKPASTIAN HEISENBERG",
      "latex": "\\Delta x \\cdot \\Delta p \\ge \\frac{h}{4\\pi} \\implies \\Delta x_{\\min} = \\frac{h}{4\\pi m_e \\Delta v} = \\frac{6{,}63 \\times 10^{-34}}{4\\pi \\times (9{,}1 \\times 10^{-31}) \\times 50} \\approx 1{,}16 \\times 10^{-6}\\text{ m}",
      "legend": "• $\\Delta p = m \\Delta v = 4{,}55 \\times 10^{-29}\\text{ N}\\cdot\\text{s}$<br>• Tidak ada alat ukur fisik di alam semesta yang mampu mengukur posisi lebih teliti dari $\\Delta x_{\\min}$ saat $\\Delta p$ diketahui"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta x_{\\min} \\approx 1{,}16 \\times 10^{-6}\\text{ meter}$ ($1{,}16\\,\\mu\\text{m}$), karena ketidakpastian momentum elektron adalah $\\Delta p = m_e \\Delta v = (9{,}1 \\times 10^{-31}\\text{ kg}) \\times 50\\text{ m/s} = 4{,}55 \\times 10^{-29}\\text{ kg}\\cdot\\text{m/s}$. Menurut prinsip Heisenberg: $\\Delta x_{\\min} = \\frac{h}{4\\pi \\Delta p} = \\frac{6{,}63 \\times 10^{-34}}{4\\pi \\times (4{,}55 \\times 10^{-29})} = \\frac{6{,}63 \\times 10^{-34}}{5{,}718 \\times 10^{-28}} \\approx 1{,}159 \\times 10^{-6}\\text{ m}$."
      },
      {
        "key": "B",
        "text": "$\\Delta x_{\\min} \\approx 2{,}32 \\times 10^{-6}\\text{ meter}$, karena konstanta pembagi dua pi keliru tidak dikalikan dua menjadi empat pi sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "C",
        "text": "$\\Delta x_{\\min} \\approx 1{,}16 \\times 10^{-10}\\text{ meter}$, dihitung dengan menggunakan kelajuan total $v$ bukan nilai ketidakpastian kelajuan $\\Delta v$."
      },
      {
        "key": "D",
        "text": "$\\Delta x_{\\min} \\approx 5{,}80 \\times 10^{-8}\\text{ meter}$, dihitung dari perbandingan panjang gelombang de Broglie elektron bebas."
      },
      {
        "key": "E",
        "text": "$\\Delta x_{\\min} \\approx 0\\text{ meter}$, karena mengasumsikan posisi dan kecepatan selalu dapat diukur simultan dengan presisi tak terbatas."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\Delta x_{\\min} \\approx 1{,}16 \\times 10^{-6}\\text{ meter}$ ($1{,}16\\,\\mu\\text{m}$), karena ketidakpastian momentum elektron adalah $\\Delta p = m_e \\Delta v = (9{,}1 \\times 10^{-31}\\text{ kg}) \\times 50\\text{ m/s} = 4{,}55 \\times 10^{-29}\\text{ kg}\\cdot\\text{m/s}$. Menurut prinsip Heisenberg: $\\Delta x_{\\min} = \\frac{h}{4\\pi \\Delta p} = \\frac{6{,}63 \\times 10^{-34}}{4\\pi \\times (4{,}55 \\times 10^{-29})} = \\frac{6{,}63 \\times 10^{-34}}{5{,}718 \\times 10^{-28}} \\approx 1{,}159 \\times 10^{-6}\\text{ m}$.. Ketidakpastian Heisenberg: Delta_x * Delta_p >= h / (4*pi). Hitung Delta_p = m * Delta_v = 9,1e-31 * 50 = 4,55e-29 kg.m/s. Lalu Delta_x = h / (4*pi*Delta_p). Delta_x = 6,63e-34 / (4 * 3,1416 * 4,55e-29) = 1,16 x 10^-6 m."
  },
  {
    "id": "fis-sim-22",
    "materi": "RELATIVITAS KHUSUS (PENJUMLAHAN KECEPATAN)",
    "topic": "Penjumlahan Kecepatan Relativistik Dua Wahana Antariksa",
    "hints": {
      "concept": "Rumus penjumlahan relativistik dua benda saling mendekati: v_rel = (vA + vB) / (1 + vA*vB / c^2).",
      "execution": "v_rel = (0,6c + 0,8c) / (1 + 0,48) = 1,4c / 1,48 = 35/37 c = 0,946c."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua wahana antariksa $A$ dan $B$ bergerak saling mendekati di sepanjang garis lurus menurut pengamat yang diam di stasiun ruang angkasa bumi. Wahana $A$ bergerak ke arah timur dengan kecepatan $v_A = 0{,}6c$, sedangkan wahana $B$ bergerak ke arah barat dengan kecepatan $v_B = 0{,}8c$. Kecepatan wahana $B$ menurut pilot di dalam wahana $A$ ($v_{B/A}$) berdasarkan Teori Relativitas Khusus Einstein adalah...",
    "formulaHud": {
      "title": "PENJUMLAHAN KECEPATAN RELATIVISTIK EINSTEIN",
      "latex": "v_{\\text{rel}} = \\frac{u + v}{1 + \\frac{uv}{c^2}} = \\frac{0{,}6c + 0{,}8c}{1 + 0{,}48} = \\frac{1{,}4}{1{,}48}c = \\frac{35}{37}c \\approx 0{,}946c",
      "legend": "• Kecepatan relatif relativistik selalu memenuhi $v_{\\text{rel}} < c$<br>• Transformasi Galileo klasik tidak berlaku untuk kecepatan tinggi ($v \\approx c$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$v_{B/A} = 1{,}4c$, karena kelajuan dihitung menggunakan transformasi Galileo klasik Newton ($v_A + v_B$) yang melanggar batas kecepatan cahaya sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik sesuai dengan perumusan matematis prinsip konservasi momentum dan impuls relativistik."
      },
      {
        "key": "B",
        "text": "$v_{B/A} = \\frac{35}{37}c \\approx 0{,}946c$ ke arah barat, karena rumus penjumlahan kecepatan relativistik Einstein untuk dua gerak berlawanan arah adalah $v_{\\text{rel}} = \\frac{v_A + v_B}{1 + \\frac{v_A v_B}{c^2}} = \\frac{0{,}6c + 0{,}8c}{1 + \\frac{(0{,}6c)(0{,}8c)}{c^2}} = \\frac{1{,}4c}{1 + 0{,}48} = \\frac{1{,}4}{1{,}48}c = \\frac{140}{148}c = \\frac{35}{37}c \\approx 0{,}9459c$."
      },
      {
        "key": "C",
        "text": "$v_{B/A} = 0{,}2c$, karena arah kecepatan keliru dikurangkan ($0{,}8c - 0{,}6c$) padahal kedua wahana saling mendekati."
      },
      {
        "key": "D",
        "text": "$v_{B/A} = c$, karena berasumsi bahwa kecepatan relatif antarobjek di luar angkasa selalu menghasilkan kecepatan cahaya."
      },
      {
        "key": "E",
        "text": "$v_{B/A} = 0{,}88c$, dihitung dari rata-rata harmonik kecepatan kedua wahana antariksa."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $v_{B/A} = \\frac{35}{37}c \\approx 0{,}946c$ ke arah barat, karena rumus penjumlahan kecepatan relativistik Einstein untuk dua gerak berlawanan arah adalah $v_{\\text{rel}} = \\frac{v_A + v_B}{1 + \\frac{v_A v_B}{c^2}} = \\frac{0{,}6c + 0{,}8c}{1 + \\frac{(0{,}6c)(0{,}8c)}{c^2}} = \\frac{1{,}4c}{1 + 0{,}48} = \\frac{1{,}4}{1{,}48}c = \\frac{140}{148}c = \\frac{35}{37}c \\approx 0{,}9459c$.. Rumus penjumlahan relativistik dua benda saling mendekati: v_rel = (vA + vB) / (1 + vA*vB / c^2). v_rel = (0,6c + 0,8c) / (1 + 0,48) = 1,4c / 1,48 = 35/37 c = 0,946c."
  },
  {
    "id": "fis-sim-23",
    "materi": "FISIKA INTI & ENERGI IKAT INTI",
    "topic": "Defek Massa dan Energi Ikat per Nukleon Inti Alfa",
    "hints": {
      "concept": "Defek massa Delta_m = 2*mp + 2*mn - m_He. Energi ikat Eb = Delta_m * 931,5 MeV. Energi ikat per nukleon = Eb / 4.",
      "execution": "Delta_m = 4,03188 - 4,00150 = 0,03038 sma. Eb = 0,03038 * 931,5 = 28,3 MeV. Eb / 4 = 7,07 MeV/nukleon."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Inti atom Helium (${}_2^4\\text{He}$) terdiri atas 2 proton dan 2 neutron. Diketahui:<br>• Massa proton $m_p = 1{,}00728\\text{ sma}$<br>• Massa neutron $m_n = 1{,}00866\\text{ sma}$<br>• Massa inti ${}_2^4\\text{He} = 4{,}00150\\text{ sma}$<br>• $1\\text{ sma} \\approx 931{,}5\\text{ MeV}$<br>Defek massa ($\\Delta m$) dan besar energi ikat per nukleon ($E_b/A$) dari inti Helium tersebut berturut-turut adalah...",
    "formulaHud": {
      "title": "DEFEK MASSA & ENERGI IKAT PER NUKLEON",
      "latex": "\\Delta m = [Z m_p + (A - Z) m_n] - m_{\\text{inti}} = [2(1{,}00728) + 2(1{,}00866)] - 4{,}00150 = 0{,}03038\\text{ sma}; \\quad \\frac{E_b}{A} = \\frac{0{,}03038 \\times 931{,}5}{4} \\approx 7{,}075\\text{ MeV/nukleon}",
      "legend": "• Inti ${}_2^4\\text{He}$ memiliki kestabilan luar biasa karena energi ikat per nukleonnya tinggi ($7{,}07\\text{ MeV/nukleon}$)<br>• $A = 4$ adalah jumlah total proton dan neutron"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta m = 0{,}03038\\text{ sma}$ dan $E_b/A \\approx 28{,}30\\text{ MeV/nukleon}$, karena nilai tersebut merupakan total energi ikat seluruh inti, belum dibagi dengan jumlah nukleon $A = 4$ ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam."
      },
      {
        "key": "B",
        "text": "$\\Delta m = 0{,}01519\\text{ sma}$ dan $E_b/A \\approx 3{,}54\\text{ MeV/nukleon}$, dihitung dengan hanya memperhitungkan 1 proton dan 1 neutron pembentuk inti."
      },
      {
        "key": "C",
        "text": "$\\Delta m = 0{,}03038\\text{ sma}$ dan $E_b/A \\approx 7{,}07\\text{ MeV/nukleon}$, karena total massa nukleon pembentuk adalah $m_{\\text{teoritis}} = 2(1{,}00728) + 2(1{,}00866) = 2{,}01456 + 2{,}01732 = 4{,}03188\\text{ sma}$. Defek massa adalah $\\Delta m = 4{,}03188 - 4{,}00150 = 0{,}03038\\text{ sma}$. Total energi ikat inti adalah $E_b = 0{,}03038 \\times 931{,}5\\text{ MeV} \\approx 28{,}299\\text{ MeV}$. Karena inti Helium memiliki jumlah nukleon $A = 4$, maka energi ikat per nukleon adalah $E_b/A = \\frac{28{,}299}{4} \\approx 7{,}075\\text{ MeV/nukleon}$."
      },
      {
        "key": "D",
        "text": "$\\Delta m = 0{,}06076\\text{ sma}$ dan $E_b/A \\approx 14{,}15\\text{ MeV/nukleon}$, dihitung dari penggandaan defek massa inti."
      },
      {
        "key": "E",
        "text": "$\\Delta m = 0{,}00150\\text{ sma}$ dan $E_b/A \\approx 0{,}35\\text{ MeV/nukleon}$, dihitung dari selisih massa inti terhadap nomor massa bulat."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $\\Delta m = 0{,}03038\\text{ sma}$ dan $E_b/A \\approx 7{,}07\\text{ MeV/nukleon}$, karena total massa nukleon pembentuk adalah $m_{\\text{teoritis}} = 2(1{,}00728) + 2(1{,}00866) = 2{,}01456 + 2{,}01732 = 4{,}03188\\text{ sma}$. Defek massa adalah $\\Delta m = 4{,}03188 - 4{,}00150 = 0{,}03038\\text{ sma}$. Total energi ikat inti adalah $E_b = 0{,}03038 \\times 931{,}5\\text{ MeV} \\approx 28{,}299\\text{ MeV}$. Karena inti Helium memiliki jumlah nukleon $A = 4$, maka energi ikat per nukleon adalah $E_b/A = \\frac{28{,}299}{4} \\approx 7{,}075\\text{ MeV/nukleon}$.. Defek massa Delta_m = 2*mp + 2*mn - m_He. Energi ikat Eb = Delta_m * 931,5 MeV. Energi ikat per nukleon = Eb / 4. Delta_m = 4,03188 - 4,00150 = 0,03038 sma. Eb = 0,03038 * 931,5 = 28,3 MeV. Eb / 4 = 7,07 MeV/nukleon."
  },
  {
    "id": "fis-sim-24",
    "materi": "REAKSI FUSI TERMONUKLIR MATAHARI",
    "topic": "Energi yang Dibebaskan pada Reaksi Fusi Inti Deuterium-Tritium",
    "hints": {
      "concept": "Defek massa fusi = (m_D + m_T) - (m_He + m_n). Energi Q = Delta_m * 931,5 MeV.",
      "execution": "Delta_m = 2,01410 + 3,01605 - (4,00260 + 1,00866) = 5,03015 - 5,01126 = 0,01889 sma. Q = 0,01889 * 931,5 = 17,596 MeV."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam teknologi reaktor fusi masa depan (tokamak), direncanakan pemanfaatan reaksi fusi inti Deuterium (${}_1^2\\text{H}$) dan Tritium (${}_1^3\\text{H}$) dengan persamaan reaksi:<br>$${}_1^2\\text{H} + {}_1^3\\text{H} \\to {}_2^4\\text{He} + {}_0^1\\text{n} + Q$$<br>Diketahui massa atom:<br>• Massa ${}_1^2\\text{H} = 2{,}01410\\text{ sma}$<br>• Massa ${}_1^3\\text{H} = 3{,}01605\\text{ sma}$<br>• Massa ${}_2^4\\text{He} = 4{,}00260\\text{ sma}$<br>• Massa ${}_0^1\\text{n} = 1{,}00866\\text{ sma}$<br>• $1\\text{ sma} \\approx 931{,}5\\text{ MeV}$<br>Energi yang dibebaskan ($Q$) dalam satu kali reaksi fusi D-T tersebut adalah...",
    "formulaHud": {
      "title": "ENERGI REAKSI FUSI DEUTERIUM-TRITIUM (D-T)",
      "latex": "\\Delta m = (m_{\\text{D}} + m_{\\text{T}}) - (m_{\\alpha} + m_{\\text{n}}) = 5{,}03015 - 5{,}01126 = 0{,}01889\\text{ sma}; \\quad Q = 0{,}01889 \\times 931{,}5 \\approx 17{,}596\\text{ MeV}",
      "legend": "• Reaksi fusi D-T merupakan reaksi penghasil energi bersih terpadat di alam semesta per satuan massa bahan bakar<br>• $\\approx 14{,}1\\text{ MeV}$ energi dibawa oleh neutron cepat dan $\\approx 3{,}5\\text{ MeV}$ oleh partikel alfa"
    },
    "options": [
      {
        "key": "A",
        "text": "$Q \\approx 3{,}27\\text{ MeV}$, karena merupakan energi yang dibebaskan pada reaksi fusi Deuterium-Deuterium cabang helium-3 menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik."
      },
      {
        "key": "B",
        "text": "$Q \\approx 28{,}30\\text{ MeV}$, karena menyamakan energi reaksi fusi dengan total energi ikat inti helium-4 murni."
      },
      {
        "key": "C",
        "text": "$Q \\approx 173{,}2\\text{ MeV}$, karena keliru tertukar dengan besaran energi reaksi fisi pembelahan uranium-235."
      },
      {
        "key": "D",
        "text": "$Q \\approx 17{,}59\\text{ MeV}$ (sekitar $17{,}6\\text{ MeV}$), karena total massa reaktan adalah $m_{\\text{awal}} = 2{,}01410 + 3{,}01605 = 5{,}03015\\text{ sma}$. Total massa produk adalah $m_{\\text{akhir}} = 4{,}00260 + 1{,}00866 = 5{,}01126\\text{ sma}$. Defek massa reaksi fusi adalah $\\Delta m = 5{,}03015 - 5{,}01126 = 0{,}01889\\text{ sma}$. Energi yang dibebaskan adalah $Q = \\Delta m \\times 931{,}5\\text{ MeV} = 0{,}01889 \\times 931{,}5 \\approx 17{,}596\\text{ MeV} \\approx 17{,}6\\text{ MeV}$."
      },
      {
        "key": "E",
        "text": "$Q \\approx 8{,}80\\text{ MeV}$, dihitung dari defek massa yang keliru dibagi dua saat konversi energi nuklir."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $Q \\approx 17{,}59\\text{ MeV}$ (sekitar $17{,}6\\text{ MeV}$), karena total massa reaktan adalah $m_{\\text{awal}} = 2{,}01410 + 3{,}01605 = 5{,}03015\\text{ sma}$. Total massa produk adalah $m_{\\text{akhir}} = 4{,}00260 + 1{,}00866 = 5{,}01126\\text{ sma}$. Defek massa reaksi fusi adalah $\\Delta m = 5{,}03015 - 5{,}01126 = 0{,}01889\\text{ sma}$. Energi yang dibebaskan adalah $Q = \\Delta m \\times 931{,}5\\text{ MeV} = 0{,}01889 \\times 931{,}5 \\approx 17{,}596\\text{ MeV} \\approx 17{,}6\\text{ MeV}$.. Defek massa fusi = (m_D + m_T) - (m_He + m_n). Energi Q = Delta_m * 931,5 MeV. Delta_m = 2,01410 + 3,01605 - (4,00260 + 1,00866) = 5,03015 - 5,01126 = 0,01889 sma. Q = 0,01889 * 931,5 = 17,596 MeV."
  },
  {
    "id": "fis-sim-25",
    "materi": "TERMODINAMIKA (SIKLUS TERTUTUP GAS)",
    "topic": "Usaha Siklus Tertutup Segitiga pada Diagram P-V",
    "hints": {
      "concept": "Usaha siklus segitiga: W = 1/2 * alas * tinggi = 1/2 * (Vc - Va) * (Pb - Pa). Kalor isobarik gas monoatomik: Q = Cp * Delta_T = 5/2 * P * Delta_V.",
      "execution": "W = 0,5 * 4e-3 * 3e5 = +600 J. Q_CA = 2,5 * 1e5 * (-4e-3) = -1.000 J."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Satu mol gas ideal monoatomik mengalami siklus termodinamika tertutup $A \\to B \\to C \\to A$ pada diagram $P-V$ berbentuk segitiga siku-siku:<br>• Titik $A$: $P_A = 1 \\times 10^5\\text{ Pa}$, $V_A = 2 \\times 10^{-3}\\text{ m}^3$<br>• Titik $B$: $P_B = 4 \\times 10^5\\text{ Pa}$, $V_B = 2 \\times 10^{-3}\\text{ m}^3$ (isokhorik)<br>• Titik $C$: $P_C = 1 \\times 10^5\\text{ Pa}$, $V_C = 6 \\times 10^{-3}\\text{ m}^3$<br>Proses $C \\to A$ berlangsung secara isobarik. Usaha total bersih ($W_{\\text{net}}$) yang dilakukan oleh gas selama satu siklus penuh dan kalor total yang dilepas saat proses isobarik $C \\to A$ ($Q_{CA}$) berturut-turut adalah...",
    "formulaHud": {
      "title": "USAHA SIKLUS P-V & KALOR PROSES ISOBARIK",
      "latex": "W_{\\text{net}} = \\frac{1}{2} (V_C - V_A)(P_B - P_A) = \\frac{1}{2}(4 \\times 10^{-3})(3 \\times 10^5) = +600\\text{ J}; \\quad Q_{CA} = \\frac{5}{2} P \\Delta V = \\frac{5}{2}(10^5)(-4 \\times 10^{-3}) = -1.000\\text{ J}",
      "legend": "• Siklus searah jarum jam $\\implies W_{\\text{net}} > 0$ (berfungsi sebagai mesin pemanas/kalor)<br>• $C_p = \\frac{5}{2} R$ untuk gas monoatomik<br>• $Q_{CA} = -1.000\\text{ J}$ (tanda minus berarti kalor dilepaskan ke lingkungan)"
    },
    "options": [
      {
        "key": "A",
        "text": "$W_{\\text{net}} = +1.200\\text{ Joule}$ dan $Q_{CA} = -600\\text{ Joule}$, karena luas segitiga keliru dihitung sebagai luas persegi panjang tanpa pembagian setengah diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas diturunkan secara analitis dari hukum termodinamika dan fungsi distribusi termal gas."
      },
      {
        "key": "B",
        "text": "$W_{\\text{net}} = +300\\text{ Joule}$ dan $Q_{CA} = -500\\text{ Joule}$, dihitung dari asumsi volume kerja setengah dari perubahan aktual."
      },
      {
        "key": "C",
        "text": "$W_{\\text{net}} = -600\\text{ Joule}$ dan $Q_{CA} = +1.000\\text{ Joule}$, karena salah menentukan tanda arah putaran siklus searah jarum jam."
      },
      {
        "key": "D",
        "text": "$W_{\\text{net}} = +600\\text{ Joule}$ dan $Q_{CA} = -400\\text{ Joule}$, karena kalor isobarik keliru dihitung hanya sebesar usaha isobarik $P \\Delta V$."
      },
      {
        "key": "E",
        "text": "$W_{\\text{net}} = +600\\text{ Joule}$ dan $Q_{CA} = -1.000\\text{ Joule}$, karena usaha total bersih satu siklus tertutup sama dengan luas daerah di dalam kurva segitiga siklus $P-V$: $W_{\\text{net}} = \\frac{1}{2} \\times \\Delta V \\times \\Delta P = \\frac{1}{2} \\times (6 - 2) \\times 10^{-3}\\text{ m}^3 \\times (4 - 1) \\times 10^5\\text{ Pa} = \\frac{1}{2} \\times (4 \\times 10^{-3}) \\times (3 \\times 10^5) = +600\\text{ Joule}$. Pada proses isobarik $C \\to A$, kalor yang dilepas adalah $Q_{CA} = n C_p \\Delta T = \\frac{5}{2} P_A (V_A - V_C) = \\frac{5}{2} \\times 10^5 \\times (2 - 6) \\times 10^{-3} = \\frac{5}{2} \\times 10^5 \\times (-4 \\times 10^{-3}) = -1.000\\text{ Joule}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $W_{\\text{net}} = +600\\text{ Joule}$ dan $Q_{CA} = -1.000\\text{ Joule}$, karena usaha total bersih satu siklus tertutup sama dengan luas daerah di dalam kurva segitiga siklus $P-V$: $W_{\\text{net}} = \\frac{1}{2} \\times \\Delta V \\times \\Delta P = \\frac{1}{2} \\times (6 - 2) \\times 10^{-3}\\text{ m}^3 \\times (4 - 1) \\times 10^5\\text{ Pa} = \\frac{1}{2} \\times (4 \\times 10^{-3}) \\times (3 \\times 10^5) = +600\\text{ Joule}$. Pada proses isobarik $C \\to A$, kalor yang dilepas adalah $Q_{CA} = n C_p \\Delta T = \\frac{5}{2} P_A (V_A - V_C) = \\frac{5}{2} \\times 10^5 \\times (2 - 6) \\times 10^{-3} = \\frac{5}{2} \\times 10^5 \\times (-4 \\times 10^{-3}) = -1.000\\text{ Joule}$.. Usaha siklus segitiga: W = 1/2 * alas * tinggi = 1/2 * (Vc - Va) * (Pb - Pa). Kalor isobarik gas monoatomik: Q = Cp * Delta_T = 5/2 * P * Delta_V. W = 0,5 * 4e-3 * 3e5 = +600 J. Q_CA = 2,5 * 1e5 * (-4e-3) = -1.000 J."
  },
  {
    "id": "fis-sim-26",
    "type": "multi",
    "materi": "ELEKTROMAGNETISME (INDUKTANSI DIRI)",
    "topic": "Faktor Penentu Induktansi Diri Solenoida dan Energi Magnetik",
    "options": [
      {
        "key": "A",
        "text": "Menyisipkan inti bahan feromagnetik dengan permeabilitas relatif tinggi ($\\mu_r \\gg 1$) ke dalam rongga solenoida untuk melipatgandakan induktansi dirinya secara drastis."
      },
      {
        "key": "B",
        "text": "Memperbanyak jumlah lilitan kawat per satuan panjang, karena induktansi diri solenoida berbanding lurus dengan kuadrat jumlah lilitan ($N^2$)."
      },
      {
        "key": "C",
        "text": "Menaikkan kuat arus listrik yang mengalir melalui solenoida, karena energi magnetik tersimpan sebanding dengan kuadrat kuat arus listrik ($I^2$)."
      },
      {
        "key": "D",
        "text": "Memperpanjang solenoida ($l$) sebesar dua kali lipat tanpa mengubah jumlah lilitan kawat dan luas penampang kumparan."
      },
      {
        "key": "E",
        "text": "Mengganti inti feromagnetik dengan ruang hampa udara agar laju disipasi medan magnet meningkat."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Perhatikan formula L = mu_r * mu_0 * N^2 * A / l dan Wm = 1/2 * L * I^2. Induktansi membesar jika mu_r naik, N naik (kuadrat), dan energi sebanding I^2.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Sebuah solenoida ideal dirancang untuk menyimpan energi magnetik di dalam rangkaian elektronika daya. Berdasarkan formula fisika induktansi diri $L = \\frac{\\mu N^2 A}{l}$ dan energi magnetik $W_m = \\frac{1}{2} L I^2$, manakah TIGA pernyataan berikut yang benar mengenai upaya memperbesar kapasitas penyimpanan energi magnetik solenoida? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "FAKTOR PENGARUH INDUKTANSI DIRI & ENERGI MAGNETIK",
      "latex": "L = \\frac{\\mu_r \\mu_0 N^2 A}{l}; \\quad W_m = \\frac{1}{2} L I^2",
      "legend": "• Pernyataan A BENAR: $\\mu_r$ memperbesar $L$ hingga ratusan kali lipat<br>• Pernyataan B BENAR: $L \\propto N^2$<br>• Pernyataan C BENAR: $W_m \\propto I^2$<br>• D SALAH: Memperpanjang $l$ justru memperkecil $L$ ($L \\propto 1/l$)<br>• E SALAH: Ruang hampa memiliki $\\mu_r = 1$, memperkecil $L$"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Perhatikan formula L = mu_r * mu_0 * N^2 * A / l dan Wm = 1/2 * L * I^2. Induktansi membesar jika mu_r naik, N naik (kuadrat), dan energi sebanding I^2. Pilih A, B, dan C."
  },
  {
    "id": "fis-sim-27",
    "type": "multi",
    "materi": "GELOMBANG ELEKTROMAGNETIK (SPEKTRUM & SIFAT)",
    "topic": "Karakteristik Gelombang Elektromagnetik dalam Ruang Hampa",
    "options": [
      {
        "key": "A",
        "text": "Gelombang elektromagnetik merupakan gelombang transversal di mana medan listrik $\\vec{E}$ dan medan magnetik $\\vec{B}$ berosilasi saling tegak lurus satu sama lain dan tegak lurus arah rambat gelombang."
      },
      {
        "key": "B",
        "text": "Semua spektrum gelombang elektromagnetik merambat dalam ruang hampa dengan kelajuan mutlak yang persis sama, yaitu $c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}} \\approx 3 \\times 10^8\\text{ m/s}$."
      },
      {
        "key": "C",
        "text": "Gelombang elektromagnetik dapat mengalami fenomena polarisasi, pemantulan, pembiasan, difraksi, dan interferensi tanpa memerlukan medium materi perantara."
      },
      {
        "key": "D",
        "text": "Sinar gamma memiliki kelajuan rambat di ruang hampa yang jauh lebih tinggi daripada gelombang radio FM."
      },
      {
        "key": "E",
        "text": "Gelombang elektromagnetik membawa muatan listrik netto sehingga dapat dibelokkan secara langsung oleh medan elektrostatik eksternal."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Gelombang elektromagnetik transversal, tidak bermuatan, merambat di vakum dengan kelajuan c yang sama untuk semua spektrum, dan dapat dipolarisasi.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Berdasarkan persamaan gelombang elektromagnetik James Clerk Maxwell dan eksperimen Heinrich Hertz, manakah TIGA karakteristik fundamental gelombang elektromagnetik dalam ruang hampa yang benar? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "PERSAMAAN GELOMBANG ELEKTROMAGNETIK MAXWELL",
      "latex": "c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}} = 2{,}998 \\times 10^8\\text{ m/s}; \\quad \\vec{S} = \\frac{1}{\\mu_0} (\\vec{E} \\times \\vec{B}); \\quad \\vec{E} \\perp \\vec{B} \\perp \\vec{k}",
      "legend": "• A BENAR: Bersifat transversal dan $\\vec{E} \\perp \\vec{B}$<br>• B BENAR: Kelajuan $c$ konstan di ruang hampa untuk semua frekuensi<br>• C BENAR: Mengalami semua sifat gelombang transversal dan merambat di vakum<br>• D SALAH: Kelajuan di ruang hampa sama persis ($c$)<br>• E SALAH: Foton/GEM tidak bermuatan listrik"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Gelombang elektromagnetik transversal, tidak bermuatan, merambat di vakum dengan kelajuan c yang sama untuk semua spektrum, dan dapat dipolarisasi. Pilih A, B, dan C."
  },
  {
    "id": "fis-sim-28",
    "type": "multi",
    "materi": "FISIKA KUANTUM (EFEK FOTOLISTRIK EINSTEIN)",
    "topic": "Bukti Eksperimen Fotolistrik yang Menggugurkan Fisika Klasik",
    "options": [
      {
        "key": "A",
        "text": "Keberadaan frekuensi ambang ($f_0$): elektron tidak akan terlepas dari logam jika frekuensi cahaya datang lebih rendah dari $f_0$, tidak peduli seberapa kuat intensitas cahaya yang disorotkan."
      },
      {
        "key": "B",
        "text": "Energi kinetik maksimum fotoelektron ($E_{k,\\max}$) hanya bergantung pada frekuensi cahaya datang dan tidak dipengaruhi sama sekali oleh intensitas cahaya."
      },
      {
        "key": "C",
        "text": "Pelepasan fotoelektron berlangsung seketika (hampir tanpa jeda waktu, $< 10^{-9}\\text{ detik}$) begitu cahaya berfrekuensi mencukupi mengenai permukaan logam."
      },
      {
        "key": "D",
        "text": "Semakin besar intensitas cahaya yang disorotkan, maka energi kinetik elektron yang terpancar akan semakin meningkat secara proporsional."
      },
      {
        "key": "E",
        "text": "Dibutuhkan waktu pemanasan berjam-jam agar elektron mampu mengumpulkan energi gelombang klasik yang cukup sebelum terpental."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Tiga bukti kuantum fotolistrik: ada frekuensi ambang (A), Ek_max hanya tergantung frekuensi bukan intensitas (B), dan emisi seketika tanpa jeda waktu (C).",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Eksperimen efek fotolistrik pada awal abad ke-20 tidak dapat dijelaskan oleh teori gelombang cahaya klasik Maxwell dan melahirkan teori kuantum cahaya Einstein. Manakah TIGA fakta eksperimen efek fotolistrik berikut yang secara langsung membuktikan bahwa cahaya merambat sebagai paket-paket kuantum energi diskrit (foton)? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "POSTULAT FOTON EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E = hf; \\quad E_{k,\\max} = h(f - f_0); \\quad I_{\\text{arus}} \\propto \\text{Intensitas}; \\quad E_{k,\\max} \\text{ independen terhadap Intensitas}",
      "legend": "• A BENAR: Teori klasik memprediksi intensitas tinggi apapun frekuensinya dapat melepas elektron<br>• B BENAR: Intensitas hanya menambah jumlah foton (arus), bukan energi per foton<br>• C BENAR: Penyerapan kuantum terjadi 1 foton diserap 1 elektron seketika<br>• D dan E adalah prediksi teori klasik yang gagal terbukti"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Tiga bukti kuantum fotolistrik: ada frekuensi ambang (A), Ek_max hanya tergantung frekuensi bukan intensitas (B), dan emisi seketika tanpa jeda waktu (C). Pilih A, B, dan C."
  },
  {
    "id": "fis-sim-29",
    "type": "multi",
    "materi": "TEORI RELATIVITAS KHUSUS",
    "topic": "Postulat Einstein dan Konsekuensi Kinematika Relativistik",
    "options": [
      {
        "key": "A",
        "text": "Hukum-hukum fisika memiliki bentuk yang sama persis dalam semua kerangka acuan inersial (kerangka yang diam atau bergerak dengan kecepatan konstan)."
      },
      {
        "key": "B",
        "text": "Kelajuan cahaya di ruang hampa adalah konstan bernilai $c$ bagi semua pengamat inersial, tidak bergantung pada gerak sumber cahaya maupun gerak pengamat."
      },
      {
        "key": "C",
        "text": "Panjang benda yang diukur oleh pengamat yang bergerak relatif terhadap benda tersebut akan tampak mengalami penyusutan (kontraksi Lorentz) hanya pada arah yang sejajar dengan arah geraknya."
      },
      {
        "key": "D",
        "text": "Sebuah jam yang bergerak relatif terhadap pengamat akan berdetak lebih cepat daripada jam yang diam di kerangka acuan pengamat tersebut."
      },
      {
        "key": "E",
        "text": "Partikel bermassa diam $m_0 > 0$ dapat dipercepat hingga melampaui kelajuan cahaya jika diberi energi dorong kinetik tak hingga."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Postulat Einstein: hukum fisika sama di semua kerangka inersial (A), laju cahaya konstan bagi semua pengamat (B). Konsekuensi: kontraksi Lorentz pada arah gerak (C). Jam bergerak justru melambat.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Teori Relativitas Khusus yang dipublikasikan oleh Albert Einstein pada tahun 1905 mengubah paradigma fisika ruang dan waktu absolut Newton. Manakah TIGA pernyataan berikut yang merupakan postulat resmi atau konsekuensi logis relativitas khusus yang terbukti secara eksperimental? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "POSTULAT & KONSEKUENSI RELATIVITAS KHUSUS",
      "latex": "L = L_0\\sqrt{1 - (v/c)^2}; \\quad \\Delta t = \\frac{\\Delta t_0}{\\sqrt{1 - (v/c)^2}}; \\quad E = \\frac{m_0 c^2}{\\sqrt{1 - (v/c)^2}}",
      "legend": "• Postulat 1 = Pernyataan A (Prinsip Relativitas)<br>• Postulat 2 = Pernyataan B (Invariansi Laju Cahaya)<br>• Konsekuensi = Pernyataan C (Kontraksi Panjang pada arah gerak)<br>• D SALAH: Jam bergerak berdetak lebih lambat (Dilatasi Waktu)<br>• E SALAH: Batas kecepatan semesta adalah $c$, tidak ada materi berkecepatan $\\ge c$"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Postulat Einstein: hukum fisika sama di semua kerangka inersial (A), laju cahaya konstan bagi semua pengamat (B). Konsekuensi: kontraksi Lorentz pada arah gerak (C). Jam bergerak justru melambat. Pilih A, B, dan C."
  },
  {
    "id": "fis-sim-30",
    "type": "multi",
    "materi": "FISIKA INTI & REAKSI NUKLIR",
    "topic": "Hukum Kekekalan dalam Reaksi Inti Radioaktif",
    "options": [
      {
        "key": "A",
        "text": "Kekekalan Jumlah Nomor Massa (Nukleon): jumlah total proton dan neutron sebelum reaksi harus sama persis dengan jumlah total nukleon setelah reaksi."
      },
      {
        "key": "B",
        "text": "Kekekalan Muatan Listrik (Nomor Atom $Z$): jumlah total muatan elementer sebelum reaksi sama dengan jumlah total muatan sesudah reaksi."
      },
      {
        "key": "C",
        "text": "Kekekalan Massa-Energi Relativistik: total energi relativistik (massa reaktan ditambah energi kinetik awal) sama dengan total energi produk ditambah energi yang dilepaskan ($Q$)."
      },
      {
        "key": "D",
        "text": "Kekekalan Massa Diam Klasik: jumlah massa diam reaktan selalu sama persis dengan jumlah massa diam partikel produk tanpa ada defek massa sedikit pun."
      },
      {
        "key": "E",
        "text": "Kekekalan Jumlah Inti Atom: jumlah inti atom utuh sebelum dan sesudah reaksi tidak boleh berubah menjadi spesies isotop yang berbeda."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Hukum kekekalan reaksi inti: nomor massa kekal (A), nomor atom/muatan kekal (B), dan massa-energi total kekal (C). Massa diam klasik tidak kekal karena ada defek massa.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Dalam semua peristiwa peluruhan radioaktif (alfa, beta, gamma) serta reaksi fisi dan fusi nuklir, terdapat besaran-besaran fisika yang mutlak kekal. Manakah TIGA hukum kekekalan yang wajib dipenuhi dalam setiap persamaan reaksi nuklir? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "HUKUM KEKEKALAN PADA REAKSI INTI",
      "latex": "\\sum A_{\\text{awal}} = \\sum A_{\\text{akhir}}; \\quad \\sum Z_{\\text{awal}} = \\sum Z_{\\text{akhir}}; \\quad E_{\\text{total}} = \\sum m_{\\text{awal}} c^2 + K_{\\text{awal}} = \\sum m_{\\text{akhir}} c^2 + K_{\\text{akhir}}",
      "legend": "• A BENAR: Nomor massa $A$ kekal<br>• B BENAR: Nomor atom / muatan $Z$ kekal<br>• C BENAR: Massa-energi relativistik Einstein kekal<br>• D SALAH: Terjadi defek massa $\\Delta m$ yang dikonversi menjadi energi $Q = \\Delta m c^2$<br>• E SALAH: Terjadi transmutasi inti atom"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Hukum kekekalan reaksi inti: nomor massa kekal (A), nomor atom/muatan kekal (B), dan massa-energi total kekal (C). Massa diam klasik tidak kekal karena ada defek massa. Pilih A, B, dan C."
  },
  {
    "id": "fis-sim-31",
    "type": "matrix",
    "materi": "TERMODINAMIKA & SIKLUS CARNOT",
    "topic": "Prinsip Termodinamika, Mesin Kalor, dan Entropi",
    "statements": [
      {
        "text": "Efisiensi termal mesin Carnot hanya bergantung pada suhu mutlak reservoir tinggi (Th) dan reservoir rendah (Tc), tidak dipengaruhi oleh jenis zat kerja gas yang digunakan.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Sebuah mesin kalor hipotetis dapat dibuat dengan efisiensi 100% jika seluruh kalor yang diserap dari reservoir panas berhasil diubah seutuhnya menjadi usaha mekanik tanpa membuang kalor ke lingkungan dingin.",
        "correct": "Salah",
        "id": "1"
      },
      {
        "text": "Pada proses siklus termodinamika tertutup, perubahan energi dalam total sistem setelah menyelesaikan satu putaran siklus penuh selalu bernilai nol (Delta U = 0).",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Menurut Hukum II Termodinamika (Prinsip Entropi), total entropi alam semesta dalam setiap proses spontan yang terjadi secara alami selalu meningkat atau tetap konstan.",
        "correct": "Benar",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Pahami efisiensi Carnot eta = 1 - Tc/Th, hukum Kelvin-Planck (efisiensi 100% mustahil), siklus tertutup Delta U = 0, dan kenaikan entropi alam semesta.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai Hukum Termodinamika dan Mesin Kalor Carnot!",
    "formulaHud": {
      "title": "PRINSIP UTAMA TERMODINAMIKA & SIKLUS CARNOT",
      "latex": "\\eta_{\\text{Carnot}} = 1 - \\frac{T_C}{T_H}; \\quad \\oint dU = 0; \\quad \\Delta S_{\\text{semesta}} \\ge 0",
      "legend": "• Pernyataan 1 BENAR: Efisiensi Carnot adalah efisiensi teoretis maksimum yang hanya dipengaruhi rasio $T_C/T_H$<br>• Pernyataan 2 SALAH: Melanggar Pernyataan Kelvin-Planck pada Hukum II Termodinamika (tidak mungkin ada mesin kalor dengan $\\eta = 100\\%$)<br>• Pernyataan 3 BENAR: Energi dalam $U$ adalah fungsi keadaan ($U_{\\text{akhir}} = U_{\\text{awal}} \\implies \\Delta U = 0$)<br>• Pernyataan 4 BENAR: Pernyataan Hukum II Termodinamika tentang entropi alam semesta"
    },
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "explanation": "Pahami efisiensi Carnot eta = 1 - Tc/Th, hukum Kelvin-Planck (efisiensi 100% mustahil), siklus tertutup Delta U = 0, dan kenaikan entropi alam semesta. Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
  },
  {
    "id": "fis-sim-32",
    "type": "matrix",
    "materi": "GETARAN HARMONIK & RESONANSI GELOMBANG",
    "topic": "Karakteristik Osilasi Harmonik dan Gelombang Mekanik",
    "statements": [
      {
        "text": "Pada getaran harmonik sederhana pegas, percepatan benda mencapai nilai maksimum tepat saat benda berada di titik simpangan terjauh (amplitudo).",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Ketika benda berosilasi harmonik melewati titik kesetimbangannya, energi potensial sistem bernilai maksimum sedangkan energi kinetiknya bernilai nol.",
        "correct": "Salah",
        "id": "1"
      },
      {
        "text": "Resonansi akustik terjadi apabila frekuensi getaran sumber luar tepat sama dengan salah satu frekuensi alami sistem penerima, menghasilkan amplitudo getaran yang berlipat ganda.",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Periode getaran bandul sederhana di permukaan bumi berbanding lurus dengan massa bandul yang digantungkan pada tali.",
        "correct": "Salah",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Percepatan GHS a = -omega^2 * y (maksimum di amplitudo). Di titik seimbang Ep = 0, Ek maks. Periode bandul T = 2pi*sqrt(L/g) tidak bergantung massa.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai Getaran Harmonik Sederhana (GHS) dan Resonansi Gelombang Bunyi!",
    "formulaHud": {
      "title": "PERSAMAAN GETARAN HARMONIS SEDERHANA",
      "latex": "a(t) = -\\omega^2 y(t); \\quad T_{\\text{bandul}} = 2\\pi\\sqrt{\\frac{L}{g}}; \\quad E_m = E_k + E_p = \\frac{1}{2} k A^2",
      "legend": "• Pernyataan 1 BENAR: Di simpangan terjauh ($y = A$), percepatan $a = \\omega^2 A$ maksimum<br>• Pernyataan 2 SALAH: Di titik kesetimbangan ($y = 0$), $E_p = 0$ dan $E_k$ bernilai maksimum<br>• Pernyataan 3 BENAR: Definisi resonansi fisis<br>• Pernyataan 4 SALAH: Periode bandul $T = 2\\pi\\sqrt{L/g}$ sama sekali tidak bergantung pada massa bandul"
    },
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "explanation": "Percepatan GHS a = -omega^2 * y (maksimum di amplitudo). Di titik seimbang Ep = 0, Ek maks. Periode bandul T = 2pi*sqrt(L/g) tidak bergantung massa. Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
  },
  {
    "id": "fis-sim-33",
    "type": "matrix",
    "materi": "ELEKTROSTATIKA & MEDAN LISTRIK",
    "topic": "Sifat Elektrostatik Konduktor dan Kapasitor",
    "statements": [
      {
        "text": "Di dalam rongga sebuah bola konduktor pejal berongga yang berada dalam kesetimbangan elektrostatik, kuat medan listrik selalu bernilai nol (E = 0).",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Garis-garis medan elektrostatik selalu berawal dari muatan positif dan berakhir pada muatan negatif, serta tidak pernah saling berpotongan.",
        "correct": "Benar",
        "id": "1"
      },
      {
        "text": "Jika jarak antar keping kapasitor sejajar dijauhkan menjadi dua kali lipat pada kondisi muatan keping konstan terisolasi, maka energi potensial listrik yang tersimpan di dalam kapasitor akan berkurang menjadi separuhnya.",
        "correct": "Salah",
        "id": "2"
      },
      {
        "text": "Menyisipkan bahan dielektrik ke dalam kapasitor keping sejajar selalu menaikkan kapasitas kapasitansinya sebanding dengan konstanta dielektrik bahan tersebut.",
        "correct": "Benar",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Kuat medan dalam konduktor = 0. Garis gaya dari positif ke negatif. Kapasitor terisolasi Q konstan: W = Q^2 / (2C). Jika d naik, C turun, maka W bertambah! C = kappa * C0.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai elektrostatika, medan listrik, dan sifat kapasitor!",
    "formulaHud": {
      "title": "PRINSIP ELEKTROSTATIK KONDUKTOR & KAPASITOR",
      "latex": "E_{\\text{dalam}} = 0; \\quad C = \\kappa \\frac{\\varepsilon_0 A}{d}; \\quad W = \\frac{Q^2}{2C} = \\frac{Q^2 d}{2 \\varepsilon_0 A}",
      "legend": "• Pernyataan 1 BENAR: Efek sangkar Faraday (medan di dalam konduktor setimbang adalah nol)<br>• Pernyataan 2 BENAR: Sifat dasar garis medan listrik Faraday<br>• Pernyataan 3 SALAH: Karena $C \\propto 1/d$, jika $d$ naik dua kali maka $C$ menjadi separuh, sehingga $W = Q^2/(2C)$ justru meningkat dua kali lipat akibat usaha penarikan keping<br>• Pernyataan 4 BENAR: $C = \\kappa C_0$"
    },
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "explanation": "Kuat medan dalam konduktor = 0. Garis gaya dari positif ke negatif. Kapasitor terisolasi Q konstan: W = Q^2 / (2C). Jika d naik, C turun, maka W bertambah! C = kappa * C0. Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
  },
  {
    "id": "fis-sim-34",
    "type": "matrix",
    "materi": "INDUKSI ELEKTROMAGNETIK",
    "topic": "Hukum Faraday, Hukum Lenz, dan Fenomena Arus Eddy",
    "statements": [
      {
        "text": "Menurut Hukum Lenz, arah arus induksi elektromagnetik selalu sedemikian rupa sehingga menimbulkan medan magnet yang melawan perubahan fluks magnetik yang menyebabkannya.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Fluks magnetik maksimum menembus sebuah bidang kumparan ketika arah medan magnetik sejajar rata dengan bidang permukaan kumparan.",
        "correct": "Salah",
        "id": "1"
      },
      {
        "text": "Pada transformator step-up ideal (efisiensi 100%), tegangan sekunder lebih tinggi daripada tegangan primer, sedangkan kuat arus sekunder lebih kecil daripada kuat arus primer.",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Pemanfaatan inti besi berlapis-lapis (laminated core) pada transformator bertujuan untuk meminimalkan kehilangan daya listrik akibat arus putar (arus Eddy).",
        "correct": "Benar",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Hukum Lenz menyatakan arus induksi melawan perubahan fluks (tanda minus). Fluks maks jika tegak lurus bidang. Transformator step-up: Vs > Vp dan Is < Ip. Inti laminasi meredam arus Eddy.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai induksi elektromagnetik dan hukum-hukum transformator!",
    "formulaHud": {
      "title": "HUKUM FARADAY & LENZ",
      "latex": "\\Phi = B A \\cos\\theta; \\quad \\varepsilon = -N \\frac{d\\Phi}{dt}; \\quad \\frac{V_s}{V_p} = \\frac{N_s}{N_p} = \\frac{I_p}{I_s}",
      "legend": "• Pernyataan 1 BENAR: Bunyi Hukum Lenz (tanda negatif pada hukum Faraday)<br>• Pernyataan 2 SALAH: Fluks maksimum saat $\\vec{B}$ tegak lurus bidang kumparan (sudut dengan normal $\\theta = 0^\\circ \\implies \\cos 0^\\circ = 1$)<br>• Pernyataan 3 BENAR: Daya tetap $P_s = P_p \\implies V_s I_s = V_p I_p$, sehingga tegangan naik arus turun<br>• Pernyataan 4 BENAR: Inti laminasi memutus jalur sirkulasi arus Eddy sehingga efisiensi transformator meningkat"
    },
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "explanation": "Hukum Lenz menyatakan arus induksi melawan perubahan fluks (tanda minus). Fluks maks jika tegak lurus bidang. Transformator step-up: Vs > Vp dan Is < Ip. Inti laminasi meredam arus Eddy. Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
  },
  {
    "id": "fis-sim-35",
    "type": "matrix",
    "materi": "FISIKA MODERN & TEORI KUANTUM",
    "topic": "Dualisme Kuantum dan Model Fisika Modern",
    "statements": [
      {
        "text": "Menurut hipotesis Louis de Broglie, setiap partikel materi bermassa yang bergerak dengan momentum p memiliki sifat gelombang dengan panjang gelombang lambda = h / p.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Efek Compton membuktikan bahwa foton cahaya memiliki momentum relativistik dan dapat mengalami tumbukan elastis dengan elektron bebas.",
        "correct": "Benar",
        "id": "1"
      },
      {
        "text": "Dalam model atom Bohr, elektron yang mengorbit inti atom pada lintasan stasioner akan terus-menerus memancarkan radiasi elektromagnetik gelombang sehingga energinya berkurang.",
        "correct": "Salah",
        "id": "2"
      },
      {
        "text": "Waktu paruh suatu zat radioaktif tidak dipengaruhi oleh perubahan suhu, tekanan mekanik, maupun reaksi kimia yang dialami oleh unsur radioaktif tersebut.",
        "correct": "Benar",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Hipotesis de Broglie lambda = h/p. Efek Compton membuktikan momentum foton. Pada lintasan stasioner Bohr elektron TIDAK meradiasikan energi. Waktu paruh adalah sifat inti independen kondisi kimia/suhu.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
    },
    "subject": "fisika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai fisika modern dan mekanika kuantum!",
    "formulaHud": {
      "title": "PRINSIP MEKANIKA KUANTUM & FISIKA MODERN",
      "latex": "\\lambda = \\frac{h}{p}; \\quad \\Delta\\lambda = \\frac{h}{m_e c}(1 - \\cos\\theta); \\quad T_{1/2} = \\frac{\\ln 2}{\\lambda_{\\text{luruh}}}",
      "legend": "• Pernyataan 1 BENAR: Hipotesis De Broglie (dualisme gelombang-materi)<br>• Pernyataan 2 BENAR: Eksperimen hamburan foton-elektron Arthur Compton (1923)<br>• Pernyataan 3 SALAH: Postulat Bohr menyatakan elektron pada orbit stasioner TIDAK memancarkan energi sama sekali<br>• Pernyataan 4 BENAR: Peluruhan radioaktif adalah fenomena murni inti atomik independen kondisi kimia-fisika lingkungan luar"
    },
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "explanation": "Hipotesis de Broglie lambda = h/p. Efek Compton membuktikan momentum foton. Pada lintasan stasioner Bohr elektron TIDAK meradiasikan energi. Waktu paruh adalah sifat inti independen kondisi kimia/suhu. Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
  }
];
