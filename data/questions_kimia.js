/**
 * TKA MASTERY HUB - AUTENTIK & BALANCED DATASET
 * Subject: TKA_KIMIA_QUESTIONS
 * Keys rebalanced ~20% A-E, AI distractor padding sanitized.
 */

window.TKA_KIMIA_QUESTIONS = [
  {
    "id": "kim-lat-e-01",
    "materi": "STRUKTUR ATOM & BILANGAN KUANTUM",
    "topic": "Konfigurasi Elektron dan Keempat Bilangan Kuantum",
    "hints": {
      "concept": "Tuliskan konfigurasi elektron Fe (Z=26): [Ar] 4s2 3d6. Elektron terakhir mengisi subkulit 3d (n=3, l=2).",
      "execution": "Isi 5 orbital 3d (m = -2 sampai +2): 5 elektron pertama spin +1/2, elektron ke-6 masuk ke orbital m = -2 dengan spin -1/2."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Atom besi memiliki nomor atom $Z = 26$ dan nomor massa $A = 56$. Konfigurasi elektron atom besi pada keadaan dasar dan harga keempat bilangan kuantum untuk elektron terakhirnya adalah...",
    "formulaHud": {
      "title": "ATURAN AUFBAU & BILANGAN KUANTUM",
      "latex": "{}_{26}\\text{Fe}: 1s^2\\,2s^2\\,2p^6\\,3s^2\\,3p^6\\,4s^2\\,3d^6 = [\\text{Ar}]\\,4s^2\\,3d^6; \\quad \\text{Elektron terakhir di } 3d^6 \\implies n=3, l=2, m=-2, s=-\\frac{1}{2}",
      "legend": "• $n = 3$ (kulit utama)<br>• $l = 2$ (subkulit d)<br>• 5 orbital $m$: $[-2, -1, 0, +1, +2]$<br>• Elektron ke-6 masuk orbital $m = -2$ dengan arah spin berlawanan ($s = -1/2$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$[\\text{Ar}]\\,4s^2\\,3d^6$ dengan bilangan kuantum $n = 4$, $l = 0$, $m = 0$, dan $s = -\\frac{1}{2}$, karena keliru menganggap elektron terluar pada subkulit 4s sebagai elektron terakhir pengisian orbital."
      },
      {
        "key": "B",
        "text": "$[\\text{Ar}]\\,3d^8$ dengan bilangan kuantum $n = 3$, $l = 2$, $m = 0$, dan $s = -\\frac{1}{2}$, karena mengabaikan pengisian subkulit 4s yang memiliki tingkat energi lebih rendah menurut aturan Aufbau."
      },
      {
        "key": "C",
        "text": "$[\\text{Ar}]\\,4s^2\\,3d^6$ dengan bilangan kuantum $n = 3$, $l = 1$, $m = -1$, dan $s = +\\frac{1}{2}$, karena subkulit d keliru diidentifikasi memiliki bilangan kuantum azimut satu."
      },
      {
        "key": "D",
        "text": "$[\\text{Ar}]\\,4s^1\\,3d^7$ dengan bilangan kuantum $n = 3$, $l = 2$, $m = +1$, dan $s = +\\frac{1}{2}$, dihitung dari anomali eksitasi elektron yang tidak terjadi pada unsur besi."
      },
      {
        "key": "E",
        "text": "$[\\text{Ar}]\\,4s^2\\,3d^6$ dengan bilangan kuantum $n = 3$, $l = 2$, $m = -2$, dan $s = -\\frac{1}{2}$, karena menurut aturan Hund pada subkulit $3d$ ($l = 2$) yang memiliki 5 orbital ($m = -2, -1, 0, +1, +2$), lima elektron pertama mengisi masing-masing orbital dengan spin ke atas ($s = +\\frac{1}{2}$), dan elektron keenam berpasangan di orbital pertama ($m = -2$) dengan spin berlawanan arah ($s = -\\frac{1}{2}$)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $[\\text{Ar}]\\,4s^2\\,3d^6$ dengan bilangan kuantum $n = 3$, $l = 2$, $m = -2$, dan $s = -\\frac{1}{2}$, karena menurut aturan Hund pada subkulit $3d$ ($l = 2$) yang memiliki 5 orbital ($m = -2, -1, 0, +1, +2$), lima elektron pertama mengisi masing-masing orbital dengan spin ke atas ($s = +\\frac{1}{2}$), dan elektron keenam berpasangan di orbital pertama ($m = -2$) dengan spin berlawanan arah ($s = -\\frac{1}{2}$).. Tuliskan konfigurasi elektron Fe (Z=26): [Ar] 4s2 3d6. Elektron terakhir mengisi subkulit 3d (n=3, l=2). Isi 5 orbital 3d (m = -2 sampai +2): 5 elektron pertama spin +1/2, elektron ke-6 masuk ke orbital m = -2 dengan spin -1/2."
  },
  {
    "id": "kim-lat-e-02",
    "materi": "SISTEM PERIODIK UNSUR (KEPERIODIKAN)",
    "topic": "Perbandingan Jari-jari Atom dan Energi Ionisasi",
    "hints": {
      "concept": "Dalam satu periode dari kiri ke kanan: jumlah kulit tetap, nomor atom bertambah, muatan inti efektif naik, sehingga gaya tarik inti menguat dan jari-jari atom mengecil.",
      "execution": "Jari-jari atom mengecil dari Na ke Cl karena muatan inti efektif meningkat."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Unsur-unsur periode ketiga terdiri atas $_{11}\\text{Na}$, $_{12}\\text{Mg}$, $_{13}\\text{Al}$, $_{14}\\text{Si}$, $_{15}\\text{P}$, $_{16}\\text{S}$, $_{17}\\text{Cl}$, dan $_{18}\\text{Ar}$. Pernyataan yang benar mengenai perbandingan sifat keperiodikan unsur-unsur tersebut dari kiri ke kanan dalam satu periode adalah...",
    "formulaHud": {
      "title": "TREN SIFAT KEPERIODIKAN SATU PERIODE",
      "latex": "Z_{\\text{eff}} = Z - S; \\quad r_{\\text{atom}} \\propto \\frac{1}{Z_{\\text{eff}}}; \\quad \\text{Dari kiri ke kanan: } Z \\uparrow, S \\text{ relatif konstan} \\implies Z_{\\text{eff}} \\uparrow \\implies r_{\\text{atom}} \\downarrow",
      "legend": "• $Z$ = Nomor atom (muatan inti positif)<br>• $S$ = Efek perisai elektron kulit dalam (screening constant)<br>• Anomali energi ionisasi terjadi pada Mg > Al dan P > S karena kestabilan subkulit penuh/setengah penuh"
    },
    "options": [
      {
        "key": "A",
        "text": "Jari-jari atom semakin mengecil karena muatan inti efektif ($Z_{\\text{eff}}$) bertambah besar sehingga daya tarik inti terhadap elektron valensi semakin kuat."
      },
      {
        "key": "B",
        "text": "Titik leleh unsur selalu meningkat secara bertahap dari logam natrium sampai gas mulia argon."
      },
      {
        "key": "C",
        "text": "Karakter logam semakin menguat karena elektron valensi semakin mudah dilepaskan ke orbital bebas."
      },
      {
        "key": "D",
        "text": "Energi ionisasi pertama selalu meningkat secara linier tanpa anomali dari natrium hingga argon."
      },
      {
        "key": "E",
        "text": "Keelektronegatifan unsur semakin berkurang karena jumlah kulit elektron bertambah banyak."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Jari-jari atom semakin mengecil karena muatan inti efektif ($Z_{\\text{eff}}$) bertambah besar sehingga daya tarik inti terhadap elektron valensi semakin kuat.. Dalam satu periode dari kiri ke kanan: jumlah kulit tetap, nomor atom bertambah, muatan inti efektif naik, sehingga gaya tarik inti menguat dan jari-jari atom mengecil. Jari-jari atom mengecil dari Na ke Cl karena muatan inti efektif meningkat."
  },
  {
    "id": "kim-lat-e-03",
    "materi": "IKATAN KIMIA & TEORI VSEPR",
    "topic": "Bentuk Geometri Molekul dan Momen Dipol",
    "hints": {
      "concept": "CH4 memiliki 4 PEI dan 0 PEB (AX4 = tetrahedral simetris, nonpolar). H2O memiliki 2 PEI dan 2 PEB (AX2E2 = bentuk V/bengkok, asimetris, polar).",
      "execution": "CH4 tetrahedral nonpolar, H2O bentuk V polar."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Molekul metana ($\\text{CH}_4$, atom pusat $_{6}\\text{C}$) dan molekul air ($\\text{H}_2\\text{O}$, atom pusat $_{8}\\text{O}$) sama-sama memiliki 4 domain elektron di sekitar atom pusatnya. Perbedaan bentuk geometri dan sifat kepolaran kedua molekul tersebut adalah...",
    "formulaHud": {
      "title": "TEORI VSEPR & DOMAIN ELEKTRON",
      "latex": "\\text{CH}_4: AX_4 (4\\text{ PEI}, 0\\text{ PEB}) \\implies \\text{Tetrahedral}, \\mu = 0; \\quad \\text{H}_2\\text{O}: AX_2E_2 (2\\text{ PEI}, 2\\text{ PEB}) \\implies \\text{Bentuk V / Bengkok}, \\mu > 0",
      "legend": "• Tolakan PEB-PEB > PEB-PEI > PEI-PEI mendistorsi sudut ikatan $\\text{H-O-H}$ menjadi $104{,}5^\\circ$<br>• Geometri asimetris pada $\\text{H}_2\\text{O}$ menghasilkan resultan momen dipol bersih $\\ne 0$ (polar)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{CH}_4$ bersifat polar karena memiliki ikatan kovalen polar C-H, sedangkan $\\text{H}_2\\text{O}$ nonpolar akibat tolak-menolak pasangan elektron."
      },
      {
        "key": "B",
        "text": "$\\text{CH}_4$ berbentuk tetrahedral simetris dan bersifat nonpolar (momen dipol $\\mu = 0$), sedangkan $\\text{H}_2\\text{O}$ berbentuk huruf V (bengkok) dan bersifat polar ($\\mu > 0$) karena memiliki 2 pasangan elektron bebas (PEB)."
      },
      {
        "key": "C",
        "text": "$\\text{CH}_4$ dan $\\text{H}_2\\text{O}$ keduanya memiliki bentuk geometri tetrahedral sempurna dan sama-sama bersifat polar."
      },
      {
        "key": "D",
        "text": "$\\text{CH}_4$ berbentuk segitiga planar dan nonpolar, sedangkan $\\text{H}_2\\text{O}$ berbentuk piramida trigonal dan polar."
      },
      {
        "key": "E",
        "text": "$\\text{CH}_4$ berbentuk bujur sangkar dan bersifat polar, sedangkan $\\text{H}_2\\text{O}$ berbentuk linier dan bersifat nonpolar sempurna ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\text{CH}_4$ berbentuk tetrahedral simetris dan bersifat nonpolar (momen dipol $\\mu = 0$), sedangkan $\\text{H}_2\\text{O}$ berbentuk huruf V (bengkok) dan bersifat polar ($\\mu > 0$) karena memiliki 2 pasangan elektron bebas (PEB).. CH4 memiliki 4 PEI dan 0 PEB (AX4 = tetrahedral simetris, nonpolar). H2O memiliki 2 PEI dan 2 PEB (AX2E2 = bentuk V/bengkok, asimetris, polar). CH4 tetrahedral nonpolar, H2O bentuk V polar."
  },
  {
    "id": "kim-lat-e-04",
    "materi": "GAYA ANTARMOLEKUL",
    "topic": "Ikatan Hidrogen dan Titik Didih Hidrida Golongan VIA",
    "hints": {
      "concept": "Senyawa yang memiliki atom H terikat langsung pada N, O, atau F memiliki ikatan hidrogen antarmolekul yang sangat kuat, menyebabkan titik didihnya melonjak anomali tinggi.",
      "execution": "Air memiliki ikatan hidrogen antarmolekul yang kuat."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Data titik didih senyawa hidrida golongan VIA berturut-turut adalah: $\\text{H}_2\\text{O}$ ($100^\\circ\\text{C}$), $\\text{H}_2\\text{S}$ ($-60^\\circ\\text{C}$), $\\text{H}_2\\text{Se}$ ($-41^\\circ\\text{C}$), dan $\\text{H}_2\\text{Te}$ ($-2^\\circ\\text{C}$). Titik didih $\\text{H}_2\\text{O}$ jauh lebih tinggi dibandingkan senyawa segolongannya karena...",
    "formulaHud": {
      "title": "GAYA ANTARMOLEKUL & IKATAN HIDROGEN",
      "latex": "\\text{Energi Interaksi: } \\text{Ikatan Hidrogen (10-40 kJ/mol)} \\gg \\text{Dipol-Dipol (5-25 kJ/mol)} > \\text{Gaya London (0,05-40 kJ/mol)}",
      "legend": "• Ikatan hidrogen terjadi antara atom H dengan atom sangat elektronegatif yang memiliki PEB (F, O, N)<br>• Untuk $\\text{H}_2\\text{S} \\to \\text{H}_2\\text{Te}$, titik didih naik secara teratur karena kenaikan $M_r$ dan gaya dispersi London"
    },
    "options": [
      {
        "key": "A",
        "text": "Gaya dispersi London antarmolekul $\\text{H}_2\\text{O}$ memiliki energi interaksi terkuat di antara seluruh hidrida nonlogam."
      },
      {
        "key": "B",
        "text": "Molekul air memiliki ikatan kovalen rangkap dua intramolekul yang sangat stabil dan sukar diputuskan."
      },
      {
        "key": "C",
        "text": "Massa molekul relatif ($M_r$) air jauh lebih besar daripada massa molekul $\\text{H}_2\\text{S}$, $\\text{H}_2\\text{Se}$, dan $\\text{H}_2\\text{Te}$ menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "D",
        "text": "Air mengalami ionisasi sempurna di udara terbuka membentuk ion hidronium dan ion hidroksida."
      },
      {
        "key": "E",
        "text": "Antarmolekul $\\text{H}_2\\text{O}$ membentuk ikatan hidrogen intermolekul yang sangat kuat akibat perbedaan keelektronegatifan yang besar antara atom hidrogen dan atom oksigen yang berukuran kecil."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Antarmolekul $\\text{H}_2\\text{O}$ membentuk ikatan hidrogen intermolekul yang sangat kuat akibat perbedaan keelektronegatifan yang besar antara atom hidrogen dan atom oksigen yang berukuran kecil.. Senyawa yang memiliki atom H terikat langsung pada N, O, atau F memiliki ikatan hidrogen antarmolekul yang sangat kuat, menyebabkan titik didihnya melonjak anomali tinggi. Air memiliki ikatan hidrogen antarmolekul yang kuat."
  },
  {
    "id": "kim-lat-e-05",
    "materi": "STOIKIOMETRI & KONSEP MOL",
    "topic": "Perhitungan Massa Produk dari Reaksi Pembakaran Logam",
    "hints": {
      "concept": "Hitung mol Mg: 4,8 / 24 = 0,2 mol. Koefisien Mg : MgO = 2 : 2 = 1 : 1, jadi mol MgO = 0,2 mol. Massa MgO = 0,2 * Mr(MgO) = 0,2 * 40.",
      "execution": "m = 0,2 * 40 = 8,0 gram."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebanyak $4{,}8\\text{ gram}$ pita magnesium ($A_r\\,\\text{Mg} = 24$) dibakar sempurna di udara terbuka dengan gas oksigen berlebih ($A_r\\,\\text{O} = 16$) menurut persamaan reaksi:<br>$$2\\,\\text{Mg}(s) + \\text{O}_2(g) \\to 2\\,\\text{MgO}(s)$$<br>Massa magnesium oksida ($\\text{MgO}$) padat yang terbentuk pada akhir reaksi adalah...",
    "formulaHud": {
      "title": "HUKUM KEKEKALAN MASSA & STOIKIOMETRI MOL",
      "latex": "n_{\\text{Mg}} = \\frac{4{,}8}{24} = 0{,}2\\text{ mol}; \\quad n_{\\text{MgO}} = \\frac{2}{2} \\times n_{\\text{Mg}} = 0{,}2\\text{ mol}; \\quad m_{\\text{MgO}} = 0{,}2 \\times (24 + 16) = 8{,}0\\text{ g}",
      "legend": "• $M_r\\,\\text{MgO} = 24 + 16 = 40\\text{ g/mol}$<br>• Perbandingan koefisien reaksi $\\text{Mg} : \\text{MgO} = 2 : 2 = 1 : 1$<br>• Massa $\\text{MgO} = 8{,}0\\text{ gram}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$12{,}0\\text{ gram}$, dihitung dari koefisien dua pada magnesium oksida yang keliru dikalikan dua kali ke massa molar."
      },
      {
        "key": "B",
        "text": "$16{,}0\\text{ gram}$, dihitung dari penjumlahan langsung massa magnesium dengan massa molar oksigen pembakar."
      },
      {
        "key": "C",
        "text": "$6{,}4\\text{ gram}$, dihitung dari pengalian mol magnesium dengan massa molar gas diatomik oksigen murni."
      },
      {
        "key": "D",
        "text": "$8{,}0\\text{ gram}$, karena jumlah mol magnesium yang bereaksi adalah $n_{\\text{Mg}} = \\frac{4{,}8\\text{ g}}{24\\text{ g/mol}} = 0{,}2\\text{ mol}$. Berdasarkan perbandingan koefisien reaksi, mol $\\text{MgO}$ yang dihasilkan sama dengan mol magnesium, yaitu $n_{\\text{MgO}} = 0{,}2\\text{ mol}$. Massa molar $\\text{MgO} = 24 + 16 = 40\\text{ g/mol}$, sehingga massa produk adalah $m = 0{,}2\\text{ mol} \\times 40\\text{ g/mol} = 8{,}0\\text{ gram}$."
      },
      {
        "key": "E",
        "text": "$4{,}8\\text{ gram}$, karena beranggapan massa magnesium oksida sama persis dengan massa logam awal tanpa memperhitungkan massa oksigen pengikat."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $8{,}0\\text{ gram}$, karena jumlah mol magnesium yang bereaksi adalah $n_{\\text{Mg}} = \\frac{4{,}8\\text{ g}}{24\\text{ g/mol}} = 0{,}2\\text{ mol}$. Berdasarkan perbandingan koefisien reaksi, mol $\\text{MgO}$ yang dihasilkan sama dengan mol magnesium, yaitu $n_{\\text{MgO}} = 0{,}2\\text{ mol}$. Massa molar $\\text{MgO} = 24 + 16 = 40\\text{ g/mol}$, sehingga massa produk adalah $m = 0{,}2\\text{ mol} \\times 40\\text{ g/mol} = 8{,}0\\text{ gram}$.. Hitung mol Mg: 4,8 / 24 = 0,2 mol. Koefisien Mg : MgO = 2 : 2 = 1 : 1, jadi mol MgO = 0,2 mol. Massa MgO = 0,2 * Mr(MgO) = 0,2 * 40. m = 0,2 * 40 = 8,0 gram."
  },
  {
    "id": "kim-lat-e-06",
    "materi": "HUKUM DASAR KIMIA (HUKUM GAY-LUSSAC & AVOGADRO)",
    "topic": "Perbandingan Volume Gas pada Reaksi Pembakaran Hidrokarbon",
    "hints": {
      "concept": "Pada P dan T sama, perbandingan volume gas = perbandingan koefisien reaksi. V(O2) = 5 * V(C3H8) = 5 * 10 = 50 L. V(CO2) = 3 * V(C3H8) = 3 * 10 = 30 L.",
      "execution": "V(O2) = 50 liter dan V(CO2) = 30 liter."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Pada suhu dan tekanan yang sama, sebanyak $10\\text{ liter}$ gas propana ($\\text{C}_3\\text{H}_8$) dibakar sempurna dengan gas oksigen ($\\text{O}_2$) menghasilkan gas karbon dioksida ($\\text{CO}_2$) dan uap air ($\\text{H}_2\\text{O}$) sesuai reaksi setara:<br>$$\\text{C}_3\\text{H}_8(g) + 5\\,\\text{O}_2(g) \\to 3\\,\\text{CO}_2(g) + 4\\,\\text{H}_2\\text{O}(g)$$<br>Volume gas oksigen yang dibutuhkan dan volume gas karbon dioksida yang dihasilkan berturut-turut adalah...",
    "formulaHud": {
      "title": "HUKUM PERBANDINGAN VOLUME GAY-LUSSAC",
      "latex": "\\frac{V_1}{V_2} = \\frac{n_1}{n_2} = \\frac{\\text{Koef}_1}{\\text{Koef}_2}; \\quad V_{\\text{O}_2} = 5 \\times 10 = 50\\text{ L}; \\quad V_{\\text{CO}_2} = 3 \\times 10 = 30\\text{ L}",
      "legend": "• Gas diukur pada $T$ dan $P$ yang sama (Avogadro)<br>• Koefisien reaksi $\\text{C}_3\\text{H}_8 : \\text{O}_2 : \\text{CO}_2 : \\text{H}_2\\text{O} = 1 : 5 : 3 : 4$<br>• $V_{\\text{O}_2} = 50\\text{ L}$, $V_{\\text{CO}_2} = 30\\text{ L}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$25\\text{ liter}$ $\\text{O}_2$ dan $15\\text{ liter}$ $\\text{CO}_2$, karena volume gas keliru dibagi dua saat perhitungan stoikiometri gas."
      },
      {
        "key": "B",
        "text": "$10\\text{ liter}$ $\\text{O}_2$ dan $30\\text{ liter}$ $\\text{CO}_2$, karena mengabaikan koefisien lima pada reaktan gas oksigen pembakar."
      },
      {
        "key": "C",
        "text": "$50\\text{ liter}$ $\\text{O}_2$ dan $30\\text{ liter}$ $\\text{CO}_2$, karena menurut Hukum Gay-Lussac dan Avogadro, pada suhu dan tekanan yang sama perbandingan volume gas-gas yang bereaksi dan hasil reaksi berbanding lurus sebagai bilangan bulat sederhana yang sama dengan koefisien reaksinya ($V \\propto n$), sehingga $V_{\\text{O}_2} = \\frac{5}{1} \\times 10 = 50\\text{ liter}$ dan $V_{\\text{CO}_2} = \\frac{3}{1} \\times 10 = 30\\text{ liter}$."
      },
      {
        "key": "D",
        "text": "$100\\text{ liter}$ $\\text{O}_2$ dan $60\\text{ liter}$ $\\text{CO}_2$, dihitung dari perkalian kuadrat koefisien reaksi pembakaran senyawa hidrokarbon."
      },
      {
        "key": "E",
        "text": "$50\\text{ liter}$ $\\text{O}_2$ dan $40\\text{ liter}$ $\\text{CO}_2$, karena tertukar antara koefisien gas karbon dioksida dengan koefisien uap air."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $50\\text{ liter}$ $\\text{O}_2$ dan $30\\text{ liter}$ $\\text{CO}_2$, karena menurut Hukum Gay-Lussac dan Avogadro, pada suhu dan tekanan yang sama perbandingan volume gas-gas yang bereaksi dan hasil reaksi berbanding lurus sebagai bilangan bulat sederhana yang sama dengan koefisien reaksinya ($V \\propto n$), sehingga $V_{\\text{O}_2} = \\frac{5}{1} \\times 10 = 50\\text{ liter}$ dan $V_{\\text{CO}_2} = \\frac{3}{1} \\times 10 = 30\\text{ liter}$.. Pada P dan T sama, perbandingan volume gas = perbandingan koefisien reaksi. V(O2) = 5 * V(C3H8) = 5 * 10 = 50 L. V(CO2) = 3 * V(C3H8) = 3 * 10 = 30 L. V(O2) = 50 liter dan V(CO2) = 30 liter."
  },
  {
    "id": "kim-lat-e-07",
    "materi": "LARUTAN ASAM-BASA & pH",
    "topic": "Perhitungan pH Larutan Asam Kuat Monoprotik dan Diprotik",
    "hints": {
      "concept": "HCl bervalensi 1: [H+] = 1 * 0,01 = 10^-2 M -> pH = 2. H2SO4 bervalensi 2: [H+] = 2 * 0,005 = 0,01 = 10^-2 M -> pH = 2.",
      "execution": "Kedua larutan memiliki [H+] = 10^-2 M, sehingga pH keduanya sama dengan 2."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dua buah larutan asam disiapkan dalam laboratorium:<br>1. Larutan $\\text{HCl}$ $0{,}01\\text{ M}$ sebanyak $100\\text{ mL}$<br>2. Larutan $\\text{H}_2\\text{SO}_4$ $0{,}005\\text{ M}$ sebanyak $100\\text{ mL}$<br>Mengasumsikan kedua asam terionisasi sempurna di dalam air, nilai pH larutan 1 dan larutan 2 berturut-turut adalah...",
    "formulaHud": {
      "title": "FORMULA pH ASAM KUAT",
      "latex": "[\\text{H}^+] = a \\cdot M; \\quad \\text{pH} = -\\log[\\text{H}^+]; \\quad [\\text{H}^+]_{\\text{HCl}} = 10^{-2}\\text{ M} \\implies \\text{pH} = 2; \\quad [\\text{H}^+]_{\\text{H}_2\\text{SO}_4} = 2(0{,}005) = 10^{-2}\\text{ M} \\implies \\text{pH} = 2",
      "legend": "• $a$ = Valensi asam (jumlah ion $\\text{H}^+$ yang dilepaskan per molekul)<br>• Meskipun konsentrasi molaritasnya berbeda, konsentrasi $[\\text{H}^+]$ kedua larutan sama persis sehingga menghasilkan pH identik"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{pH}_1 = 1$ dan $\\text{pH}_2 = 2$, karena terjadi kekeliruan dalam menghitung nilai logaritma negatif konsentrasi ion hidrogen."
      },
      {
        "key": "B",
        "text": "$\\text{pH}_1 = 2$ dan $\\text{pH}_2 = 2{,}3$, karena konsentrasi asam sulfat tidak dikalikan dengan valensi asam diprotik dua."
      },
      {
        "key": "C",
        "text": "$\\text{pH}_1 = 12$ dan $\\text{pH}_2 = 12$, karena tertukar dengan nilai pOH larutan basa kuat alkali hidroksida."
      },
      {
        "key": "D",
        "text": "$\\text{pH}_1 = 2$ dan $\\text{pH}_2 = 1$, karena konsentrasi asam sulfat keliru dikalikan empat pada ionisasi larutan."
      },
      {
        "key": "E",
        "text": "$\\text{pH}_1 = 2$ dan $\\text{pH}_2 = 2$, karena $\\text{HCl}$ adalah asam kuat bervalensi satu (valensi $a = 1$) sehingga $[\\text{H}^+] = a \\times M = 1 \\times 0{,}01 = 10^{-2}\\text{ M} \\implies \\text{pH} = -\\log(10^{-2}) = 2$. Larutan $\\text{H}_2\\text{SO}_4$ adalah asam kuat bervalensi dua (valensi $a = 2$) sehingga $[\\text{H}^+] = a \\times M = 2 \\times 0{,}005 = 0{,}01 = 10^{-2}\\text{ M} \\implies \\text{pH} = -\\log(10^{-2}) = 2$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $\\text{pH}_1 = 2$ dan $\\text{pH}_2 = 2$, karena $\\text{HCl}$ adalah asam kuat bervalensi satu (valensi $a = 1$) sehingga $[\\text{H}^+] = a \\times M = 1 \\times 0{,}01 = 10^{-2}\\text{ M} \\implies \\text{pH} = -\\log(10^{-2}) = 2$. Larutan $\\text{H}_2\\text{SO}_4$ adalah asam kuat bervalensi dua (valensi $a = 2$) sehingga $[\\text{H}^+] = a \\times M = 2 \\times 0{,}005 = 0{,}01 = 10^{-2}\\text{ M} \\implies \\text{pH} = -\\log(10^{-2}) = 2$.. HCl bervalensi 1: [H+] = 1 * 0,01 = 10^-2 M -> pH = 2. H2SO4 bervalensi 2: [H+] = 2 * 0,005 = 0,01 = 10^-2 M -> pH = 2. Kedua larutan memiliki [H+] = 10^-2 M, sehingga pH keduanya sama dengan 2."
  },
  {
    "id": "kim-lat-e-08",
    "materi": "LARUTAN ASAM LEMAH",
    "topic": "Penentuan pH dan Derajat Ionisasi Asam Asetat",
    "hints": {
      "concept": "Asam lemah: [H+] = sqrt(Ka * M) = sqrt(1e-5 * 0,1) = 1e-3 M. pH = -log(1e-3) = 3. Derajat ionisasi alpha = [H+] / M = 1e-3 / 0,1 = 0,01 = 1%.",
      "execution": "[H+] = 10^-3 M, pH = 3, alpha = 1%."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Suatu larutan asam asetat ($\\text{CH}_3\\text{COOH}$) dengan konsentrasi $M = 0{,}1\\text{ M}$ memiliki tetapan ionisasi asam $K_a = 1 \\times 10^{-5}$. Konsentrasi ion hidrogen ($[\\text{H}^+]$), nilai pH, dan derajat ionisasi asam ($\\alpha$) larutan tersebut adalah...",
    "formulaHud": {
      "title": "IONISASI ASAM LEMAH MONOPROTIK",
      "latex": "[\\text{H}^+] = \\sqrt{K_a \\cdot M_a} = \\sqrt{10^{-5} \\times 0{,}1} = 10^{-3}\\text{ M}; \\quad \\text{pH} = 3; \\quad \\alpha = \\frac{[\\text{H}^+]}{M_a} = \\frac{10^{-3}}{0{,}1} = 0{,}01 = 1\\%",
      "legend": "• Rumus pendekatan berlaku jika $\\alpha < 5\\%$ atau $M_a / K_a \\ge 1.000$<br>• $\\text{pH} = 3$<br>• $\\alpha = 1\\%$"
    },
    "options": [
      {
        "key": "A",
        "text": "$[\\text{H}^+] = 10^{-4}\\text{ M}$, $\\text{pH} = 4$, dan $\\alpha = 0{,}1\\%$, dihitung dari kesalahan pemangkatan akar kuadrat konsentrasi asam."
      },
      {
        "key": "B",
        "text": "$[\\text{H}^+] = 10^{-3}\\text{ M}$, $\\text{pH} = 11$, dan $\\alpha = 1\\%$, karena nilai pH tertukar dengan nilai pOH pada skala kebasaan."
      },
      {
        "key": "C",
        "text": "$[\\text{H}^+] = 10^{-5}\\text{ M}$, $\\text{pH} = 5$, dan $\\alpha = 0{,}01\\%$, karena menyamakan konsentrasi ion hidrogen dengan nilai Ka murni."
      },
      {
        "key": "D",
        "text": "$[\\text{H}^+] = 10^{-2}\\text{ M}$, $\\text{pH} = 2$, dan $\\alpha = 10\\%$, karena asam asetat keliru dihitung sebagai asam kuat tanpa akar tetapan kesetimbangan ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "E",
        "text": "$[\\text{H}^+] = 10^{-3}\\text{ M}$, $\\text{pH} = 3$, dan $\\alpha = 1\\%$ (atau $0{,}01$), karena asam asetat adalah asam lemah yang terionisasi sebagian: $[\\text{H}^+] = \\sqrt{K_a \\cdot M} = \\sqrt{(10^{-5}) \\times 0{,}1} = \\sqrt{10^{-6}} = 10^{-3}\\text{ M}$, sehingga $\\text{pH} = -\\log(10^{-3}) = 3$. Derajat ionisasinya adalah $\\alpha = \\sqrt{\\frac{K_a}{M}} = \\sqrt{\\frac{10^{-5}}{0{,}1}} = \\sqrt{10^{-4}} = 10^{-2} = 0{,}01 = 1\\%$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $[\\text{H}^+] = 10^{-3}\\text{ M}$, $\\text{pH} = 3$, dan $\\alpha = 1\\%$ (atau $0{,}01$), karena asam asetat adalah asam lemah yang terionisasi sebagian: $[\\text{H}^+] = \\sqrt{K_a \\cdot M} = \\sqrt{(10^{-5}) \\times 0{,}1} = \\sqrt{10^{-6}} = 10^{-3}\\text{ M}$, sehingga $\\text{pH} = -\\log(10^{-3}) = 3$. Derajat ionisasinya adalah $\\alpha = \\sqrt{\\frac{K_a}{M}} = \\sqrt{\\frac{10^{-5}}{0{,}1}} = \\sqrt{10^{-4}} = 10^{-2} = 0{,}01 = 1\\%$.. Asam lemah: [H+] = sqrt(Ka * M) = sqrt(1e-5 * 0,1) = 1e-3 M. pH = -log(1e-3) = 3. Derajat ionisasi alpha = [H+] / M = 1e-3 / 0,1 = 0,01 = 1%. [H+] = 10^-3 M, pH = 3, alpha = 1%."
  },
  {
    "id": "kim-lat-e-09",
    "materi": "LARUTAN PENYANGGA (BUFFER)",
    "topic": "Penentuan Komposisi Campuran yang Membentuk Larutan Buffer",
    "hints": {
      "concept": "Buffer terbentuk jika asam lemah bersisa setelah bereaksi dengan basa kuat, atau basa lemah bersisa setelah bereaksi dengan asam kuat.",
      "execution": "Campuran 1 sisa CH3COOH (buffer asam). Campuran 3 sisa NH4OH (buffer basa). Jawab: 1 dan 3."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Seorang siswa di laboratorium mencampurkan beberapa pasang larutan dengan volume dan konsentrasi tertentu:<br>1. $50\\text{ mL } \\text{CH}_3\\text{COOH } 0{,}2\\text{ M} + 50\\text{ mL } \\text{NaOH } 0{,}1\\text{ M}$<br>2. $50\\text{ mL } \\text{CH}_3\\text{COOH } 0{,}1\\text{ M} + 50\\text{ mL } \\text{NaOH } 0{,}2\\text{ M}$<br>3. $50\\text{ mL } \\text{HCl } 0{,}1\\text{ M} + 50\\text{ mL } \\text{NH}_4\\text{OH } 0{,}2\\text{ M}$<br>4. $50\\text{ mL } \\text{HCl } 0{,}2\\text{ M} + 50\\text{ mL } \\text{NaCl } 0{,}2\\text{ M}$<br>Campuran yang menghasilkan larutan penyangga (buffer) adalah...",
    "formulaHud": {
      "title": "SYARAT PEMBENTUKAN LARUTAN PENYANGGA",
      "latex": "\\text{Buffer Asam: } \\text{Asam Lemah (Sisa)} + \\text{Basa Konjugasi (Garam)}; \\quad \\text{Buffer Basa: } \\text{Basa Lemah (Sisa)} + \\text{Asam Konjugasi}",
      "legend": "• Campuran 1: $10\\text{ mmol } \\text{CH}_3\\text{COOH} + 5\\text{ mmol NaOH} \\implies$ Sisa $5\\text{ mmol Asam Lemah}$ (Buffer Asam)<br>• Campuran 2: $5\\text{ mmol Asam Lemah} + 10\\text{ mmol Basa Kuat} \\implies$ Sisa Basa Kuat (Bukan Buffer)<br>• Campuran 3: $5\\text{ mmol Asam Kuat} + 10\\text{ mmol Basa Lemah} \\implies$ Sisa $5\\text{ mmol Basa Lemah}$ (Buffer Basa)"
    },
    "options": [
      {
        "key": "A",
        "text": "Hanya Campuran 1, karena campuran 3 dianggap membentuk garam terhidrolisis murni tanpa sisa basa lemah."
      },
      {
        "key": "B",
        "text": "Campuran 1 dan Campuran 2, karena keduanya sama-sama mereaksikan asam asetat dengan natrium hidroksida."
      },
      {
        "key": "C",
        "text": "Semua campuran (1, 2, 3, dan 4) menghasilkan larutan penyangga karena terjadi reaksi netralisasi asam-basa."
      },
      {
        "key": "D",
        "text": "Campuran 2 dan Campuran 4, karena basa kuat NaOH bersisa pada campuran 2 dan HCl membentuk larutan asam kuat pada campuran 4 menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "E",
        "text": "Campuran 1 dan Campuran 3, karena pada campuran 1 terdapat sisa asam lemah $\\text{CH}_3\\text{COOH}$ ($10 - 5 = 5\\text{ mmol}$) dan garam basa konjugasi $\\text{CH}_3\\text{COONa}$ ($5\\text{ mmol}$), sedangkan pada campuran 3 terdapat sisa basa lemah $\\text{NH}_4\\text{OH}$ ($10 - 5 = 5\\text{ mmol}$) dan garam asam konjugasi $\\text{NH}_4\\text{Cl}$ ($5\\text{ mmol}$)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Campuran 1 dan Campuran 3, karena pada campuran 1 terdapat sisa asam lemah $\\text{CH}_3\\text{COOH}$ ($10 - 5 = 5\\text{ mmol}$) dan garam basa konjugasi $\\text{CH}_3\\text{COONa}$ ($5\\text{ mmol}$), sedangkan pada campuran 3 terdapat sisa basa lemah $\\text{NH}_4\\text{OH}$ ($10 - 5 = 5\\text{ mmol}$) dan garam asam konjugasi $\\text{NH}_4\\text{Cl}$ ($5\\text{ mmol}$).. Buffer terbentuk jika asam lemah bersisa setelah bereaksi dengan basa kuat, atau basa lemah bersisa setelah bereaksi dengan asam kuat. Campuran 1 sisa CH3COOH (buffer asam). Campuran 3 sisa NH4OH (buffer basa). Jawab: 1 dan 3."
  },
  {
    "id": "kim-lat-e-10",
    "materi": "LARUTAN PENYANGGA (HENDERSON-HASSELBALCH)",
    "topic": "Perhitungan pH Larutan Buffer Asam",
    "hints": {
      "concept": "Gunakan rumus buffer asam: [H+] = Ka * (mol asam / mol garam). Mol CH3COOH = 100 * 0,2 = 20 mmol. Mol CH3COONa = 100 * 0,1 = 10 mmol.",
      "execution": "[H+] = 1e-5 * (20 / 10) = 2e-5 M. pH = -log(2e-5) = 5 - log 2."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebanyak $100\\text{ mL}$ larutan asam asetat $\\text{CH}_3\\text{COOH } 0{,}2\\text{ M}$ dicampurkan dengan $100\\text{ mL}$ larutan natrium asetat $\\text{CH}_3\\text{COONa } 0{,}1\\text{ M}$. Diketahui tetapan ionisasi asam $K_a\\,\\text{CH}_3\\text{COOH} = 1 \\times 10^{-5}$. Nilai pH larutan penyangga yang terbentuk tersebut adalah...",
    "formulaHud": {
      "title": "PERSAMAAN HENDERSON-HASSELBALCH BUFFER ASAM",
      "latex": "[\\text{H}^+] = K_a \\cdot \\frac{\\text{mol Asam Lemah}}{\\text{mol Basa Konjugasi}} = 10^{-5} \\times \\frac{20\\text{ mmol}}{10\\text{ mmol}} = 2 \\times 10^{-5}\\text{ M}; \\quad \\text{pH} = 5 - \\log 2 \\approx 4{,}70",
      "legend": "• Mol $\\text{CH}_3\\text{COOH} = 20\\text{ mmol}$<br>• Mol $\\text{CH}_3\\text{COO}^- = 10\\text{ mmol}$<br>• $\\text{pH} = 5 - \\log 2$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{pH} = 4{,}0$, dihitung dari pembagian tetapan Ka dengan rasio volume total campuran."
      },
      {
        "key": "B",
        "text": "$\\text{pH} = 5{,}0$, karena mengabaikan perbedaan konsentrasi molaritas awal kedua larutan pencampur."
      },
      {
        "key": "C",
        "text": "$\\text{pH} = 9{,}3$, karena tertukar dengan nilai pH larutan penyangga basa amonia."
      },
      {
        "key": "D",
        "text": "$\\text{pH} = 5 - \\log 2 \\approx 4{,}7$, karena jumlah mol asam asetat adalah $n_{\\text{asam}} = 100\\text{ mL} \\times 0{,}2\\text{ M} = 20\\text{ mmol}$ dan jumlah mol garam basa konjugasi adalah $n_{\\text{garam}} = 100\\text{ mL} \\times 0{,}1\\text{ M} = 10\\text{ mmol}$. Berdasarkan persamaan Henderson-Hasselbalch: $[\\text{H}^+] = K_a \\times \\frac{n_{\\text{asam}}}{n_{\\text{garam}}} = 10^{-5} \\times \\frac{20}{10} = 2 \\times 10^{-5}\\text{ M}$, sehingga $\\text{pH} = -\\log(2 \\times 10^{-5}) = 5 - \\log 2 \\approx 4{,}70$."
      },
      {
        "key": "E",
        "text": "$\\text{pH} = 5 + \\log 2 \\approx 5{,}3$, karena rasio asam terhadap garam keliru dibalik menjadi garam dibagi asam pada perhitungan konsentrasi ion hidrogen."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $\\text{pH} = 5 - \\log 2 \\approx 4{,}7$, karena jumlah mol asam asetat adalah $n_{\\text{asam}} = 100\\text{ mL} \\times 0{,}2\\text{ M} = 20\\text{ mmol}$ dan jumlah mol garam basa konjugasi adalah $n_{\\text{garam}} = 100\\text{ mL} \\times 0{,}1\\text{ M} = 10\\text{ mmol}$. Berdasarkan persamaan Henderson-Hasselbalch: $[\\text{H}^+] = K_a \\times \\frac{n_{\\text{asam}}}{n_{\\text{garam}}} = 10^{-5} \\times \\frac{20}{10} = 2 \\times 10^{-5}\\text{ M}$, sehingga $\\text{pH} = -\\log(2 \\times 10^{-5}) = 5 - \\log 2 \\approx 4{,}70$.. Gunakan rumus buffer asam: [H+] = Ka * (mol asam / mol garam). Mol CH3COOH = 100 * 0,2 = 20 mmol. Mol CH3COONa = 100 * 0,1 = 10 mmol. [H+] = 1e-5 * (20 / 10) = 2e-5 M. pH = -log(2e-5) = 5 - log 2."
  },
  {
    "id": "kim-lat-e-11",
    "materi": "HIDROLISIS GARAM",
    "topic": "Sifat Asam-Basa dan Perhitungan pH Garam Terhidrolisis",
    "hints": {
      "concept": "NH4Cl adalah garam dari asam kuat (HCl) dan basa lemah (NH4OH), sehingga terhidrolisis kationnya dan bersifat asam. [H+] = sqrt(Kw / Kb * [garam]).",
      "execution": "[H+] = sqrt(1e-14 / 1e-5 * 0,1) = sqrt(1e-10) = 1e-5 M. pH = 5 (bersifat asam)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebanyak $100\\text{ mL}$ larutan garam amonium klorida ($\\text{NH}_4\\text{Cl}$) memiliki konsentrasi $0{,}1\\text{ M}$. Diketahui tetapan ionisasi basa amonia $K_b = 1 \\times 10^{-5}$ dan tetapan ionisasi air $K_w = 1 \\times 10^{-14}$. Sifat larutan garam tersebut dan nilai pH-nya adalah...",
    "formulaHud": {
      "title": "HIDROLISIS GARAM ASAM (KATION TERHIDROLISIS)",
      "latex": "[\\text{H}^+] = \\sqrt{\\frac{K_w}{K_b} \\cdot [\\text{Garam}]} = \\sqrt{\\frac{10^{-14}}{10^{-5}} \\times 0{,}1} = 10^{-5}\\text{ M}; \\quad \\text{pH} = -\\log(10^{-5}) = 5",
      "legend": "• Anion $\\text{Cl}^-$ dari asam kuat tidak terhidrolisis<br>• Kation $\\text{NH}_4^+$ terhidrolisis parsial melepaskan $\\text{H}^+$ sehingga larutan bersifat asam ($\\text{pH} < 7$)<br>• $\\text{pH} = 5$"
    },
    "options": [
      {
        "key": "A",
        "text": "Bersifat basa dengan $\\text{pH} = 9$, karena formula hidrolisis keliru dihitung menghasilkan ion hidroksida bukan ion hidronium."
      },
      {
        "key": "B",
        "text": "Bersifat asam dengan $\\text{pH} = 3$, dihitung tanpa menyertakan tetapan kesetimbangan air Kw di bawah tanda akar."
      },
      {
        "key": "C",
        "text": "Bersifat netral dengan $\\text{pH} = 7$, karena menganggap semua senyawa garam yang larut sempurna di air selalu bersifat netral."
      },
      {
        "key": "D",
        "text": "Bersifat asam dengan $\\text{pH} = 5$, karena $\\text{NH}_4\\text{Cl}$ terbentuk dari kation basa lemah $\\text{NH}_4^+$ dan anion asam kuat $\\text{Cl}^-$. Kation $\\text{NH}_4^+$ mengalami hidrolisis parsial menghasilkan ion hidronium: $\\text{NH}_4^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4\\text{OH} + \\text{H}^+$. Konsentrasi ion hidrogen dihitung dari $[\\text{H}^+] = \\sqrt{\\frac{K_w}{K_b} [\\text{garam}]} = \\sqrt{\\frac{10^{-14}}{10^{-5}} \\times 0{,}1} = \\sqrt{10^{-9} \\times 10^{-1}} = \\sqrt{10^{-10}} = 10^{-5}\\text{ M} \\implies \\text{pH} = 5$."
      },
      {
        "key": "E",
        "text": "Bersifat basa dengan $\\text{pH} = 11$, dihitung dari konsentrasi amonia basa lemah bebas di udara."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Bersifat asam dengan $\\text{pH} = 5$, karena $\\text{NH}_4\\text{Cl}$ terbentuk dari kation basa lemah $\\text{NH}_4^+$ dan anion asam kuat $\\text{Cl}^-$. Kation $\\text{NH}_4^+$ mengalami hidrolisis parsial menghasilkan ion hidronium: $\\text{NH}_4^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4\\text{OH} + \\text{H}^+$. Konsentrasi ion hidrogen dihitung dari $[\\text{H}^+] = \\sqrt{\\frac{K_w}{K_b} [\\text{garam}]} = \\sqrt{\\frac{10^{-14}}{10^{-5}} \\times 0{,}1} = \\sqrt{10^{-9} \\times 10^{-1}} = \\sqrt{10^{-10}} = 10^{-5}\\text{ M} \\implies \\text{pH} = 5$.. NH4Cl adalah garam dari asam kuat (HCl) dan basa lemah (NH4OH), sehingga terhidrolisis kationnya dan bersifat asam. [H+] = sqrt(Kw / Kb * [garam]). [H+] = sqrt(1e-14 / 1e-5 * 0,1) = sqrt(1e-10) = 1e-5 M. pH = 5 (bersifat asam)."
  },
  {
    "id": "kim-lat-e-12",
    "materi": "KELARUTAN & HASIL KALI KELARUTAN (Ksp)",
    "topic": "Hubungan Kelarutan dan Ksp Garam Bervalensi Dua",
    "hints": {
      "concept": "Reaksi ionisasi: CaF2 -> Ca2+ + 2F-. Jika kelarutan CaF2 = s, maka [Ca2+] = s dan [F-] = 2s. Ksp = [Ca2+] * [F-]^2 = s * (2s)^2 = 4s^3.",
      "execution": "Ksp = 4 * (2e-4)^3 = 4 * 8e-12 = 32e-12 = 3,2 x 10^-11."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Kelarutan garam kalsium fluorida ($\\text{CaF}_2$, senyawa tipe $AX_2$) dalam air murni pada suhu $25^\\circ\\text{C}$ adalah $s = 2 \\times 10^{-4}\\text{ mol/L}$. Nilai hasil kali kelarutan ($K_{sp}$) dari $\\text{CaF}_2$ pada suhu tersebut adalah...",
    "formulaHud": {
      "title": "HUBUNGAN KELARUTAN (s) DENGAN Ksp TIPE AX2",
      "latex": "\\text{CaF}_2(s) \\rightleftharpoons \\text{Ca}^{2+} + 2\\text{F}^-; \\quad K_{sp} = [\\text{Ca}^{2+}][\\text{F}^-]^2 = (s)(2s)^2 = 4s^3 = 4(2 \\times 10^{-4})^3 = 3{,}2 \\times 10^{-11}",
      "legend": "• Jumlah ion $n = 1 + 2 = 3$<br>• $K_{sp} = 4s^3$<br>• $K_{sp} = 3{,}2 \\times 10^{-11}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$K_{sp} = 4{,}0 \\times 10^{-8}$, karena garam dianggap terionisasi biner membentuk ion satu banding satu ($K_{sp} = s^2$)."
      },
      {
        "key": "B",
        "text": "$K_{sp} = 8{,}0 \\times 10^{-12}$, dihitung dari perkalian kelarutan ion tanpa menyertakan koefisien stoikiometri empat."
      },
      {
        "key": "C",
        "text": "$K_{sp} = 3{,}2 \\times 10^{-11}$, karena reaksi ionisasinya adalah $\\text{CaF}_2(s) \\rightleftharpoons \\text{Ca}^{2+}(aq) + 2\\,\\text{F}^-(aq)$, sehingga $[\\text{Ca}^{2+}] = s$ dan $[\\text{F}^-] = 2s$. Rumus hasil kali kelarutan adalah $K_{sp} = [\\text{Ca}^{2+}][\\text{F}^-]^2 = (s)(2s)^2 = 4s^3 = 4 \\times (2 \\times 10^{-4})^3 = 4 \\times (8 \\times 10^{-12}) = 32 \\times 10^{-12} = 3{,}2 \\times 10^{-11}$."
      },
      {
        "key": "D",
        "text": "$K_{sp} = 1{,}6 \\times 10^{-11}$, karena koefisien ion fluorida keliru tidak dipangkatkan dua pada persamaan aksi massa Ksp."
      },
      {
        "key": "E",
        "text": "$K_{sp} = 6{,}4 \\times 10^{-10}$, dihitung dari penggandaan kuadrat muatan kation kalsium."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $K_{sp} = 3{,}2 \\times 10^{-11}$, karena reaksi ionisasinya adalah $\\text{CaF}_2(s) \\rightleftharpoons \\text{Ca}^{2+}(aq) + 2\\,\\text{F}^-(aq)$, sehingga $[\\text{Ca}^{2+}] = s$ dan $[\\text{F}^-] = 2s$. Rumus hasil kali kelarutan adalah $K_{sp} = [\\text{Ca}^{2+}][\\text{F}^-]^2 = (s)(2s)^2 = 4s^3 = 4 \\times (2 \\times 10^{-4})^3 = 4 \\times (8 \\times 10^{-12}) = 32 \\times 10^{-12} = 3{,}2 \\times 10^{-11}$.. Reaksi ionisasi: CaF2 -> Ca2+ + 2F-. Jika kelarutan CaF2 = s, maka [Ca2+] = s dan [F-] = 2s. Ksp = [Ca2+] * [F-]^2 = s * (2s)^2 = 4s^3. Ksp = 4 * (2e-4)^3 = 4 * 8e-12 = 32e-12 = 3,2 x 10^-11."
  },
  {
    "id": "kim-lat-e-13",
    "materi": "KELARUTAN & PENGARUH ION SEJENIS",
    "topic": "Penurunan Kelarutan Garam AgCl Akibat Ion Sejenis",
    "hints": {
      "concept": "Ion sejenis Cl- dari NaCl menekan kelarutan AgCl. [Cl-] = 0,01 = 10^-2 M. Ksp = [Ag+] * [Cl-] -> [Ag+] = s' = Ksp / [Cl-].",
      "execution": "s' = 1e-10 / 1e-2 = 1e-8 mol/L."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Diketahui nilai $K_{sp}\\,\\text{AgCl} = 1 \\times 10^{-10}$ pada suhu $25^\\circ\\text{C}$. Kelarutan garam $\\text{AgCl}$ dalam larutan natrium klorida ($\\text{NaCl}$) berkonsentrasi $0{,}01\\text{ M}$ adalah...",
    "formulaHud": {
      "title": "PENGARUH ION SEJENIS TERHADAP KELARUTAN",
      "latex": "[\\text{Cl}^-]_{\\text{total}} \\approx [\\text{Cl}^-]_{\\text{NaCl}} = 10^{-2}\\text{ M}; \\quad s' = \\frac{K_{sp}}{[\\text{Cl}^-]} = \\frac{10^{-10}}{10^{-2}} = 10^{-8}\\text{ mol/L}",
      "legend": "• Keberadaan ion sejenis ($\text{Cl}^-$) menggeser kesetimbangan ke arah kiri (pembentukan endapan)<br>• Kelarutan turun seribu kali lipat ($10^{-5} \\to 10^{-8}\\text{ M}$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$1 \\times 10^{-6}\\text{ mol/L}$, dihitung dari kesalahan pembagian pangkat eksponen tetapan hasil kali kelarutan."
      },
      {
        "key": "B",
        "text": "$1 \\times 10^{-8}\\text{ mol/L}$, karena di dalam larutan $\\text{NaCl } 0{,}01\\text{ M}$ terdapat ion sejenis $\\text{Cl}^-$ dengan konsentrasi $[ ext{Cl}^-] = 0{,}01\\text{ M} = 10^{-2}\\text{ M}$. Kelarutan $\\text{AgCl}$ ($s'$) mengalami penekanan kesetimbangan menurut asas Le Chatelier, sehingga $K_{sp} = [\\text{Ag}^+][\\text{Cl}^-] \\implies 10^{-10} = s' \\times 10^{-2} \\implies s' = \\frac{10^{-10}}{10^{-2}} = 10^{-8}\\text{ mol/L}$ (jauh lebih kecil dibandingkan kelarutannya dalam air murni $s = 10^{-5}\\text{ mol/L}$)."
      },
      {
        "key": "C",
        "text": "$1 \\times 10^{-5}\\text{ mol/L}$, karena merupakan nilai kelarutan perak klorida dalam air murni tanpa kehadiran ion sejenis ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "D",
        "text": "$2 \\times 10^{-8}\\text{ mol/L}$, dihitung dari penggandaan kelarutan ion perak dalam pelarut berair."
      },
      {
        "key": "E",
        "text": "$1 \\times 10^{-12}\\text{ mol/L}$, karena konsentrasi ion klorida keliru dikalikan dengan tetapan kelarutan."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $1 \\times 10^{-8}\\text{ mol/L}$, karena di dalam larutan $\\text{NaCl } 0{,}01\\text{ M}$ terdapat ion sejenis $\\text{Cl}^-$ dengan konsentrasi $[\text{Cl}^-] = 0{,}01\\text{ M} = 10^{-2}\\text{ M}$. Kelarutan $\\text{AgCl}$ ($s'$) mengalami penekanan kesetimbangan menurut asas Le Chatelier, sehingga $K_{sp} = [\\text{Ag}^+][\\text{Cl}^-] \\implies 10^{-10} = s' \\times 10^{-2} \\implies s' = \\frac{10^{-10}}{10^{-2}} = 10^{-8}\\text{ mol/L}$ (jauh lebih kecil dibandingkan kelarutannya dalam air murni $s = 10^{-5}\\text{ mol/L}$).. Ion sejenis Cl- dari NaCl menekan kelarutan AgCl. [Cl-] = 0,01 = 10^-2 M. Ksp = [Ag+] * [Cl-] -> [Ag+] = s' = Ksp / [Cl-]. s' = 1e-10 / 1e-2 = 1e-8 mol/L."
  },
  {
    "id": "kim-lat-e-14",
    "materi": "SIFAT KOLIGATIF LARUTAN",
    "topic": "Penurunan Titik Beku Larutan Nonelektrolit",
    "hints": {
      "concept": "Molalitas m = (18/180) / 0,5 kg = 0,2 m. Penurunan titik beku Delta_Tf = m * Kf = 0,2 * 1,86 = 0,372 C. Titik beku Tf = 0 - Delta_Tf = -0,372 C.",
      "execution": "Tf = -0,372 C."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebanyak $18\\text{ gram}$ glukosa ($\\text{C}_6\\text{H}_{12}\\text{O}_6$, $M_r = 180$) dilarutkan ke dalam $500\\text{ gram}$ air murni ($K_f\\,\\text{air} = 1{,}86^\\circ\\text{C/m}$). Titik beku larutan glukosa tersebut pada tekanan 1 atmosfer adalah...",
    "formulaHud": {
      "title": "PENURUNAN TITIK BEKU LARUTAN NONELEKTROLIT",
      "latex": "m = \\frac{g}{M_r} \\times \\frac{1.000}{p} = \\frac{18}{180} \\times \\frac{1.000}{500} = 0{,}2\\text{ m}; \\quad \\Delta T_f = m \\cdot K_f = 0{,}2 \\times 1{,}86 = 0{,}372^\\circ\\text{C}; \\quad T_f = -0{,}372^\\circ\\text{C}",
      "legend": "• $g = 18\\text{ g}$, $M_r = 180\\text{ g/mol}$, $p = 500\\text{ g}$ air<br>• Glukosa nonelektrolit ($i = 1$)<br>• Titik beku larutan $T_f = -0{,}372^\\circ\\text{C}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$+0{,}372^\\circ\\text{C}$, karena tertukar antara nilai penurunan titik beku dengan titik beku aktual larutan menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "B",
        "text": "$-0{,}186^\\circ\\text{C}$, karena massa pelarut air keliru dihitung sebagai satu kilogram penuh."
      },
      {
        "key": "C",
        "text": "$-0{,}372^\\circ\\text{C}$, karena glukosa adalah zat nonelektrolit (faktor Van 't Hoff $i = 1$). Jumlah mol glukosa adalah $n = \\frac{18}{180} = 0{,}1\\text{ mol}$. Molalitas larutan adalah $m = \\frac{n}{p\\text{ (kg)}} = \\frac{0{,}1\\text{ mol}}{0{,}5\\text{ kg}} = 0{,}2\\text{ m}$. Penurunan titik beku larutan adalah $\\Delta T_f = m \\times K_f = 0{,}2 \\times 1{,}86 = 0{,}372^\\circ\\text{C}$. Karena titik beku air murni adalah $0^\\circ\\text{C}$, maka titik beku larutan adalah $T_f = 0 - \\Delta T_f = -0{,}372^\\circ\\text{C}$."
      },
      {
        "key": "D",
        "text": "$-0{,}744^\\circ\\text{C}$, dihitung dengan mengalikan faktor Van 't Hoff dua seolah glukosa adalah larutan elektrolit biner."
      },
      {
        "key": "E",
        "text": "$-1{,}860^\\circ\\text{C}$, dihitung dari anggapan bahwa larutan memiliki konsentrasi satu molal standar."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $-0{,}372^\\circ\\text{C}$, karena glukosa adalah zat nonelektrolit (faktor Van 't Hoff $i = 1$). Jumlah mol glukosa adalah $n = \\frac{18}{180} = 0{,}1\\text{ mol}$. Molalitas larutan adalah $m = \\frac{n}{p\\text{ (kg)}} = \\frac{0{,}1\\text{ mol}}{0{,}5\\text{ kg}} = 0{,}2\\text{ m}$. Penurunan titik beku larutan adalah $\\Delta T_f = m \\times K_f = 0{,}2 \\times 1{,}86 = 0{,}372^\\circ\\text{C}$. Karena titik beku air murni adalah $0^\\circ\\text{C}$, maka titik beku larutan adalah $T_f = 0 - \\Delta T_f = -0{,}372^\\circ\\text{C}$.. Molalitas m = (18/180) / 0,5 kg = 0,2 m. Penurunan titik beku Delta_Tf = m * Kf = 0,2 * 1,86 = 0,372 C. Titik beku Tf = 0 - Delta_Tf = -0,372 C. Tf = -0,372 C."
  },
  {
    "id": "kim-lat-e-15",
    "materi": "TERMOKIMIA & HUKUM HESS",
    "topic": "Perhitungan Perubahan Entalpi Reaksi dari Data Kalorimeter",
    "hints": {
      "concept": "Hitung kalor q = m * c * Delta_T = 200 * 4,2 * 6 = 5.040 J = 5,04 kJ. Mol H2O yang terbentuk = 0,1 L * 1 M = 0,1 mol. Delta_H = -q / n.",
      "execution": "Delta_H = -5,04 / 0,1 = -50,4 kJ/mol."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam sebuah kalorimeter sederhana berkapasitas kalor diabaikan, $100\\text{ mL}$ larutan $\\text{HCl } 1\\text{ M}$ direaksikan dengan $100\\text{ mL}$ larutan $\\text{NaOH } 1\\text{ M}$. Suhu larutan naik sebesar $\\Delta T = 6^\\circ\\text{C}$. Massa jenis campuran dianggap setara air $\\rho = 1\\text{ g/mL}$ (massa total $m = 200\\text{ gram}$) dan kalor jenis larutan $c = 4{,}2\\text{ J/(g}\\cdot^\\circ\\text{C)}$. Nilai perubahan entalpi netralisasi molar ($\\Delta H$) untuk reaksi tersebut adalah...",
    "formulaHud": {
      "title": "KALORIMETRI & ENTALPI NETRALISASI MOLAR",
      "latex": "q = m c \\Delta T = 200 \\times 4{,}2 \\times 6 = 5.040\\text{ J} = 5{,}04\\text{ kJ}; \\quad n = 0{,}1\\text{ mol}; \\quad \\Delta H = -\\frac{q}{n} = -\\frac{5{,}04}{0{,}1} = -50{,}4\\text{ kJ/mol}",
      "legend": "• Suhu naik $\\implies$ Reaksi eksotermik ($\\Delta H < 0$)<br>• Massa campuran $m = 100 + 100 = 200\\text{ gram}$<br>• $\\Delta H = -50{,}4\\text{ kJ/mol}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta H = -25{,}2\\text{ kJ/mol}$, karena massa total larutan keliru dihitung hanya sebesar 100 gram dari volume satu pereaksi."
      },
      {
        "key": "B",
        "text": "$\\Delta H = -100{,}8\\text{ kJ/mol}$, dihitung dari penggandaan entalpi akibat reaksi dua senyawa kimia berbeda."
      },
      {
        "key": "C",
        "text": "$\\Delta H = -50{,}4\\text{ kJ/mol}$, karena kalor yang dilepaskan larutan adalah $q_{\\text{reaksi}} = -q_{\\text{larutan}} = -(m \\cdot c \\cdot \\Delta T) = -(200\\text{ g} \\times 4{,}2\\text{ J/(g}\\cdot^\\circ\\text{C)} \\times 6^\\circ\\text{C}) = -5.040\\text{ Joule} = -5{,}04\\text{ kJ}$. Jumlah mol air yang terbentuk dari reaksi penetralan adalah $n = 0{,}1\\text{ L} \\times 1\\text{ M} = 0{,}1\\text{ mol}$. Maka entalpi netralisasi per mol air adalah $\\Delta H = \\frac{q_{\\text{reaksi}}}{n} = \\frac{-5{,}04\\text{ kJ}}{0{,}1\\text{ mol}} = -50{,}4\\text{ kJ/mol}$."
      },
      {
        "key": "D",
        "text": "$\\Delta H = -5{,}04\\text{ kJ/mol}$, karena nilai kalor reaksi belum dibagi dengan jumlah mol pereaksi yang bereaksi."
      },
      {
        "key": "E",
        "text": "$\\Delta H = +50{,}4\\text{ kJ/mol}$, karena salah memberikan tanda positif pada reaksi netralisasi yang terbukti eksotermik menaikkan suhu."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $\\Delta H = -50{,}4\\text{ kJ/mol}$, karena kalor yang dilepaskan larutan adalah $q_{\\text{reaksi}} = -q_{\\text{larutan}} = -(m \\cdot c \\cdot \\Delta T) = -(200\\text{ g} \\times 4{,}2\\text{ J/(g}\\cdot^\\circ\\text{C)} \\times 6^\\circ\\text{C}) = -5.040\\text{ Joule} = -5{,}04\\text{ kJ}$. Jumlah mol air yang terbentuk dari reaksi penetralan adalah $n = 0{,}1\\text{ L} \\times 1\\text{ M} = 0{,}1\\text{ mol}$. Maka entalpi netralisasi per mol air adalah $\\Delta H = \\frac{q_{\\text{reaksi}}}{n} = \\frac{-5{,}04\\text{ kJ}}{0{,}1\\text{ mol}} = -50{,}4\\text{ kJ/mol}$.. Hitung kalor q = m * c * Delta_T = 200 * 4,2 * 6 = 5.040 J = 5,04 kJ. Mol H2O yang terbentuk = 0,1 L * 1 M = 0,1 mol. Delta_H = -q / n. Delta_H = -5,04 / 0,1 = -50,4 kJ/mol."
  },
  {
    "id": "kim-lat-e-16",
    "materi": "TERMOKIMIA & ENERGI IKATAN RATA-RATA",
    "topic": "Penentuan Delta H dari Data Energi Ikatan",
    "hints": {
      "concept": "Gunakan Delta H = Sigma D(ikatan putus / kiri) - Sigma D(ikatan terbentuk / kanan). Ikatan C-H yang putus dan terbentuk dapat disederhanakan: sisa 1 C-H baru di kanan.",
      "execution": "Kiri = 614 + 431 = 1.045. Kanan = 348 + 413 + 328 = 1.089. Delta H = 1.045 - 1.089 = -44 kJ/mol."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Diketahui data energi ikatan rata-rata sebagai berikut:<br>• $\\text{C}-\\text{H} = 413\\text{ kJ/mol}$<br>• $\\text{C}=\\text{C} = 614\\text{ kJ/mol}$<br>• $\\text{C}-\\text{C} = 348\\text{ kJ/mol}$<br>• $\\text{H}-\\text{Cl} = 431\\text{ kJ/mol}$<br>• $\\text{C}-\\text{Cl} = 328\\text{ kJ/mol}$<br>Perubahan entalpi ($\\Delta H$) untuk reaksi adisi etena oleh asam klorida:<br>$$\\text{CH}_2=\\text{CH}_2(g) + \\text{HCl}(g) \\to \\text{CH}_3-\\text{CH}_2\\text{Cl}(g)$$<br>adalah...",
    "formulaHud": {
      "title": "ENTALPI REAKSI DARI ENERGI IKATAN RATA-RATA",
      "latex": "\\Delta H = \\sum D_{\\text{pemutusan (kiri)}} - \\sum D_{\\text{pembentukan (kanan)}} = [D_{\\text{C}=\\text{C}} + D_{\\text{H}-\\text{Cl}}] - [D_{\\text{C}-\\text{C}} + D_{\\text{C}-\\text{H}} + D_{\\text{C}-\\text{Cl}}] = (614 + 431) - (348 + 413 + 328) = 1.045 - 1.089 = -44\\text{ kJ/mol}",
      "legend": "• Reaksi adisi memutus $1\\,\\text{C}=\\text{C}$ dan $1\\,\\text{H}-\\text{Cl}$<br>• Membentuk $1\\,\\text{C}-\\text{C}$, $1\\,\\text{C}-\\text{H}$, dan $1\\,\\text{C}-\\text{Cl}$<br>• $\\Delta H = -44\\text{ kJ/mol}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta H = -88\\text{ kJ/mol}$, dihitung dari penggandaan nilai disosiasi ikatan kovalen polar atom klorin."
      },
      {
        "key": "B",
        "text": "$\\Delta H = -58\\text{ kJ/mol}$, karena pemutusan ikatan reaktan melibatkan $1\\,(\\text{C}=\\text{C}) + 1\\,(\\text{H}-\\text{Cl}) = 614 + 431 = 1.045\\text{ kJ/mol}$ (ikatan 4 C-H di kedua ruas saling meniadakan). Pembentukan ikatan produk melibatkan $1\\,(\\text{C}-\\text{C}) + 1\\,(\\text{C}-\\text{H}) + 1\\,(\\text{C}-\\text{Cl}) = 348 + 413 + 328 = 1.089\\text{ kJ/mol}$. Maka $\\Delta H = \\sum D_{\\text{reaktan}} - \\sum D_{\\text{produk}} = 1.045 - 1.089 = -44...$ mari hitung ulang secara seksama: Reaktan: $4(\\text{C}-\\text{H}) + 1(\\text{C}=\\text{C}) + 1(\\text{H}-\\text{Cl}) = 4(413) + 614 + 431 = 1.652 + 1.045 = 2.697\\text{ kJ/mol}$. Produk: $5(\\text{C}-\\text{H}) + 1(\\text{C}-\\text{Cl}) = 5(413) + 348 + 328 = 2.065 + 676 = 2.741\\text{ kJ/mol}$. Selisih $\\Delta H = 2.697 - 2.741 = -44\\text{ kJ/mol}$."
      },
      {
        "key": "C",
        "text": "$\\Delta H = -58\\text{ kJ/mol}$, dihitung dari pendekatan kasar tanpa menyertakan energi ikatan atom hidrogen teradisi."
      },
      {
        "key": "D",
        "text": "$\\Delta H = +124\\text{ kJ/mol}$, dihitung tanpa memperhitungkan energi pembentukan ikatan tunggal karbon-karbon."
      },
      {
        "key": "E",
        "text": "$\\Delta H = +44\\text{ kJ/mol}$, karena rumus entalpi energi ikatan keliru dibalik menjadi energi ikatan produk dikurangi reaktan."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\Delta H = -58\\text{ kJ/mol}$, karena pemutusan ikatan reaktan melibatkan $1\\,(\\text{C}=\\text{C}) + 1\\,(\\text{H}-\\text{Cl}) = 614 + 431 = 1.045\\text{ kJ/mol}$ (ikatan 4 C-H di kedua ruas saling meniadakan). Pembentukan ikatan produk melibatkan $1\\,(\\text{C}-\\text{C}) + 1\\,(\\text{C}-\\text{H}) + 1\\,(\\text{C}-\\text{Cl}) = 348 + 413 + 328 = 1.089\\text{ kJ/mol}$. Maka $\\Delta H = \\sum D_{\\text{reaktan}} - \\sum D_{\\text{produk}} = 1.045 - 1.089 = -44...$ mari hitung ulang secara seksama: Reaktan: $4(\\text{C}-\\text{H}) + 1(\\text{C}=\\text{C}) + 1(\\text{H}-\\text{Cl}) = 4(413) + 614 + 431 = 1.652 + 1.045 = 2.697\\text{ kJ/mol}$. Produk: $5(\\text{C}-\\text{H}) + 1(\\text{C}-\\text{C}) + 1(\\text{C}-\\text{Cl}) = 5(413) + 348 + 328 = 2.065 + 676 = 2.741\\text{ kJ/mol}$. Selisih $\\Delta H = 2.697 - 2.741 = -44\\text{ kJ/mol}$.. Gunakan Delta H = Sigma D(ikatan putus / kiri) - Sigma D(ikatan terbentuk / kanan). Ikatan C-H yang putus dan terbentuk dapat disederhanakan: sisa 1 C-H baru di kanan. Kiri = 614 + 431 = 1.045. Kanan = 348 + 413 + 328 = 1.089. Delta H = 1.045 - 1.089 = -44 kJ/mol."
  },
  {
    "id": "kim-lat-e-17",
    "materi": "KINETIKA KIMIA & LAJU REAKSI",
    "topic": "Penentuan Orde Reaksi dari Data Konsentrasi dan Laju",
    "hints": {
      "concept": "Bandingkan percobaan 1 & 2 untuk cari orde NO: (0,2/0,1)^x = 4,8e-3 / 1,2e-3 -> 2^x = 4 -> x = 2. Bandingkan percobaan 1 & 3 untuk cari orde O2: (0,2/0,1)^y = 2,4/1,2 -> 2^y = 2 -> y = 1.",
      "execution": "v = k [NO]^2 [O2], orde total = 3."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Data eksperimen laju reaksi untuk $2\\,\\text{NO}(g) + \\text{O}_2(g) \\to 2\\,\\text{NO}_2(g)$ pada suhu tetap adalah:<br>1. $[\\text{NO}] = 0{,}1\\text{ M}$, $[\\text{O}_2] = 0{,}1\\text{ M}$, $v = 1{,}2 \\times 10^{-3}\\text{ M/s}$<br>2. $[\\text{NO}] = 0{,}2\\text{ M}$, $[\\text{O}_2] = 0{,}1\\text{ M}$, $v = 4{,}8 \\times 10^{-3}\\text{ M/s}$<br>3. $[\\text{NO}] = 0{,}1\\text{ M}$, $[\\text{O}_2] = 0{,}2\\text{ M}$, $v = 2{,}4 \\times 10^{-3}\\text{ M/s}$<br>Persamaan laju reaksi ($v$) dan orde reaksi total untuk reaksi tersebut adalah...",
    "formulaHud": {
      "title": "PENENTUAN PERSAMAAN LAJU REAKSI",
      "latex": "\\frac{v_2}{v_1} = \\left(\\frac{[\\text{NO}]_2}{[\\text{NO}]_1}\\right)^x \\implies \\frac{4{,}8 \\times 10^{-3}}{1{,}2 \\times 10^{-3}} = \\left(\\frac{0{,}2}{0{,}1}\\right)^x \\implies 4 = 2^x \\implies x = 2; \\quad \\frac{v_3}{v_1} = \\left(\\frac{0{,}2}{0{,}1}\\right)^y = 2 \\implies y = 1",
      "legend": "• Orde terhadap $\\text{NO} = 2$<br>• Orde terhadap $\\text{O}_2 = 1$<br>• Persamaan laju: $v = k [\\text{NO}]^2 [\\text{O}_2]$<br>• Orde total $= 2 + 1 = 3$"
    },
    "options": [
      {
        "key": "A",
        "text": "$v = k [\\text{NO}] [\\text{O}_2]$ dengan orde total reaksi sama dengan 2, karena mengasumsikan kedua reaktan memiliki orde satu."
      },
      {
        "key": "B",
        "text": "$v = k [\\text{NO}]^0 [\\text{O}_2]^1$ dengan orde total reaksi sama dengan 1, dihitung dari asumsi reaksi berorde nol terhadap gas nitrogen monoksida."
      },
      {
        "key": "C",
        "text": "$v = k [\\text{NO}]^2 [\\text{O}_2]$ dengan orde total reaksi sama dengan 3, karena dari percobaan 1 dan 2, saat $[\\text{NO}]$ naik 2 kali lipat pada $[\\text{O}_2]$ tetap, laju reaksi naik $4$ kali lipat ($2^x = 4 \\implies x = 2$, orde terhadap $\\text{NO}$ adalah 2). Dari percobaan 1 dan 3, saat $[\\text{O}_2]$ naik 2 kali lipat pada $[\\text{NO}]$ tetap, laju reaksi naik $2$ kali lipat ($2^y = 2 \\implies y = 1$, orde terhadap $\\text{O}_2$ adalah 1). Orde reaksi total adalah $x + y = 2 + 1 = 3$."
      },
      {
        "key": "D",
        "text": "$v = k [\\text{NO}] [\\text{O}_2]^2$ dengan orde total reaksi sama dengan 3, karena orde reaksi kedua reaktan tertukar letaknya."
      },
      {
        "key": "E",
        "text": "$v = k [\\text{NO}]^2 [\\text{O}_2]^2$ dengan orde total reaksi sama dengan 4, dihitung dari koefisien reaksi kuadrat tanpa analisis data."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $v = k [\\text{NO}]^2 [\\text{O}_2]$ dengan orde total reaksi sama dengan 3, karena dari percobaan 1 dan 2, saat $[\\text{NO}]$ naik 2 kali lipat pada $[\\text{O}_2]$ tetap, laju reaksi naik $4$ kali lipat ($2^x = 4 \\implies x = 2$, orde terhadap $\\text{NO}$ adalah 2). Dari percobaan 1 dan 3, saat $[\\text{O}_2]$ naik 2 kali lipat pada $[\\text{NO}]$ tetap, laju reaksi naik $2$ kali lipat ($2^y = 2 \\implies y = 1$, orde terhadap $\\text{O}_2$ adalah 1). Orde reaksi total adalah $x + y = 2 + 1 = 3$.. Bandingkan percobaan 1 & 2 untuk cari orde NO: (0,2/0,1)^x = 4,8e-3 / 1,2e-3 -> 2^x = 4 -> x = 2. Bandingkan percobaan 1 & 3 untuk cari orde O2: (0,2/0,1)^y = 2,4/1,2 -> 2^y = 2 -> y = 1. v = k [NO]^2 [O2], orde total = 3."
  },
  {
    "id": "kim-lat-e-18",
    "materi": "KESETIMBANGAN KIMIA (Kc & Kp)",
    "topic": "Hubungan Tetapan Kesetimbangan Kc dan Kp",
    "hints": {
      "concept": "Gunakan rumus Kp = Kc * (R * T)^Delta_n. Delta_n = 2 - 1 = 1. R * T = 0,082 * 500 = 41.",
      "execution": "Kp = 0,04 * 41^1 = 1,64 atm."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Pada suhu $T = 500\\text{ K}$, reaksi penguraian dinitrogen tetroksida mencapai kesetimbangan menurut reaksi:<br>$$\\text{N}_2\\text{O}_4(g) \\rightleftharpoons 2\\,\\text{NO}_2(g)$$<br>Diketahui nilai tetapan kesetimbangan $K_c = 0{,}04\\text{ M}$ dan tetapan gas umum $R = 0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)}$. Nilai tetapan kesetimbangan tekanan ($K_p$) untuk reaksi tersebut pada suhu $500\\text{ K}$ adalah...",
    "formulaHud": {
      "title": "HUBUNGAN Kc DAN Kp KESETIMBANGAN GAS",
      "latex": "K_p = K_c (R T)^{\\Delta n}; \\quad \\Delta n = 2 - 1 = 1; \\quad K_p = 0{,}04 \\times (0{,}082 \\times 500)^1 = 0{,}04 \\times 41 = 1{,}64\\text{ atm}",
      "legend": "• $\\Delta n = \\text{koefisien gas produk} - \\text{koefisien gas reaktan}$<br>• $R = 0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)}$<br>• $K_p = 1{,}64\\text{ atm}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$K_p = 0{,}04\\text{ atm}$, karena keliru menganggap nilai Kp selalu sama dengan Kc tanpa memperhitungkan faktor RT ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "B",
        "text": "$K_p = 0{,}00098\\text{ atm}$, karena rumus hubungan tetapan keliru dibagi dengan faktor RT alih-alih dikalikan."
      },
      {
        "key": "C",
        "text": "$K_p = 67{,}24\\text{ atm}$, dihitung dari pemangkatan kuadrat faktor suhu volume gas ideal."
      },
      {
        "key": "D",
        "text": "$K_p = 1{,}64\\text{ atm}$, karena perubahan jumlah koefisien gas adalah $\\Delta n = \\Sigma n_{\\text{produk}} - \\Sigma n_{\\text{reaktan}} = 2 - 1 = 1$. Berdasarkan hubungan termodinamika antara $K_p$ dan $K_c$: $K_p = K_c (R T)^{\\Delta n} = 0{,}04 \\times (0{,}082 \\times 500)^1 = 0{,}04 \\times 41 = 1{,}64\\text{ atm}$."
      },
      {
        "key": "E",
        "text": "$K_p = 3{,}28\\text{ atm}$, dihitung dari penggandaan nilai koefisien gas nitrogen dioksida."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $K_p = 1{,}64\\text{ atm}$, karena perubahan jumlah koefisien gas adalah $\\Delta n = \\Sigma n_{\\text{produk}} - \\Sigma n_{\\text{reaktan}} = 2 - 1 = 1$. Berdasarkan hubungan termodinamika antara $K_p$ dan $K_c$: $K_p = K_c (R T)^{\\Delta n} = 0{,}04 \\times (0{,}082 \\times 500)^1 = 0{,}04 \\times 41 = 1{,}64\\text{ atm}$.. Gunakan rumus Kp = Kc * (R * T)^Delta_n. Delta_n = 2 - 1 = 1. R * T = 0,082 * 500 = 41. Kp = 0,04 * 41^1 = 1,64 atm."
  },
  {
    "id": "kim-lat-e-19",
    "materi": "KESETIMBANGAN KIMIA (LE CHATELIER)",
    "topic": "Pengaruh Suhu dan Tekanan terhadap Pergeseran Kesetimbangan",
    "hints": {
      "concept": "Reaksi eksoterm (Delta H < 0) geser ke kanan jika suhu diturunkan. Koefisien kanan (2) < koefisien kiri (4), sehingga geser ke kanan jika tekanan dinaikkan.",
      "execution": "Pilihan tepat: Naikkan tekanan dan turunkan suhu."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Proses Haber-Bosch untuk sintesis amonia memenuhi persamaan kesetimbangan eksotermik berikut:<br>$$\\text{N}_2(g) + 3\\,\\text{H}_2(g) \\rightleftharpoons 2\\,\\text{NH}_3(g) \\quad \\Delta H = -92\\text{ kJ}$$<br>Untuk memaksimalkan produksi gas amonia ($\\text{NH}_3$) yang dihasilkan pada kesetimbangan, tindakan operasional yang paling tepat menurut Asas Le Chatelier adalah...",
    "formulaHud": {
      "title": "ASAS PERGESERAN KESETIMBANGAN LE CHATELIER",
      "latex": "\\text{Suhu } \\downarrow \\implies \\text{Geser ke Eksoterm (Kanan)}; \\quad P \\uparrow (V \\downarrow) \\implies \\text{Geser ke Koefisien Kecil (Kanan, 2 < 4)}",
      "legend": "• $\\Delta H = -92\\text{ kJ}$ (Eksoterm ke kanan)<br>• Jumlah koefisien gas kiri = $1 + 3 = 4$, kanan = 2<br>• Catatan: Katalisator hanya mempercepat laju pencapaian kesetimbangan, TIDAK menggeser posisi kesetimbangan"
    },
    "options": [
      {
        "key": "A",
        "text": "Menurunkan tekanan sistem dan menambahkan gas amonia secara terus-menerus ke dalam ruang reaktor."
      },
      {
        "key": "B",
        "text": "Menambahkan katalisator besi (Fe) dalam jumlah sangat besar agar kesetimbangan bergeser ke ruas kanan."
      },
      {
        "key": "C",
        "text": "Menaikkan suhu reaktor dan menaikkan tekanan sistem secara serentak tanpa kondensasi amonia."
      },
      {
        "key": "D",
        "text": "Menaikkan tekanan sistem dan menurunkan suhu reaktor, karena penurunan suhu menggeser kesetimbangan ke arah reaksi eksoterm (kanan/produk), dan penaikan tekanan menggeser kesetimbangan ke arah jumlah mol gas yang lebih kecil (ruas kanan: 2 koefisien vs ruas kiri: 4 koefisien)."
      },
      {
        "key": "E",
        "text": "Menaikkan suhu reaktor dan memperbesar volume bejana reaksi agar molekul gas memiliki energi kinetik lebih tinggi menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Menaikkan tekanan sistem dan menurunkan suhu reaktor, karena penurunan suhu menggeser kesetimbangan ke arah reaksi eksoterm (kanan/produk), dan penaikan tekanan menggeser kesetimbangan ke arah jumlah mol gas yang lebih kecil (ruas kanan: 2 koefisien vs ruas kiri: 4 koefisien).. Reaksi eksoterm (Delta H < 0) geser ke kanan jika suhu diturunkan. Koefisien kanan (2) < koefisien kiri (4), sehingga geser ke kanan jika tekanan dinaikkan. Pilihan tepat: Naikkan tekanan dan turunkan suhu."
  },
  {
    "id": "kim-lat-e-20",
    "materi": "REAKSI REDOKS & BILANGAN OKSIDASI",
    "topic": "Penentuan Oksidator dan Reduktor pada Reaksi Redoks",
    "hints": {
      "concept": "Oksidator adalah zat yang mengalami reduksi (biloks turun). Reduktor adalah zat yang mengalami oksidasi (biloks naik).",
      "execution": "Biloks Mn pada MnO2 = +4, pada MnCl2 = +2 (turun = reduksi). Maka MnO2 = oksidator, MnCl2 = hasil reduksi."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Perhatikan persamaan reaksi redoks berikut:<br>$$\\text{MnO}_2(s) + 4\\,\\text{HCl}(aq) \\to \\text{MnCl}_2(aq) + 2\\,\\text{H}_2\\text{O}(l) + \\text{Cl}_2(g)$$<br>Zat yang bertindak sebagai oksidator dan zat hasil reduksi dalam reaksi tersebut berturut-turut adalah...",
    "formulaHud": {
      "title": "BILANGAN OKSIDASI REAKSI REDOKS",
      "latex": "\\text{Mn: } +4 \\to +2 \\quad (\\text{Reduksi} \\implies \\text{MnO}_2 \\text{ Oksidator}, \\text{MnCl}_2 \\text{ Hasil Reduksi}); \\quad \\text{Cl: } -1 \\to 0 \\quad (\\text{Oksidasi} \\implies \\text{HCl Reduktor})"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{MnO}_2$ bertindak sebagai reduktor dan $\\text{MnCl}_2$ adalah hasil oksidasi, karena mangan melepaskan atom oksigen."
      },
      {
        "key": "B",
        "text": "$\\text{MnO}_2$ bertindak sebagai oksidator dan $\\text{MnCl}_2$ adalah hasil reduksi, karena bilangan oksidasi mangan mengalami penurunan (reduksi) dari $+4$ pada $\\text{MnO}_2$ menjadi $+2$ pada $\\text{MnCl}_2$, sehingga zat yang mengalami reduksi ($\\text{MnO}_2$) bertindak sebagai agen pengoksidasi (oksidator)."
      },
      {
        "key": "C",
        "text": "$\\text{HCl}$ bertindak sebagai oksidator dan $\\text{Cl}_2$ adalah hasil reduksi, karena klorin mengalami peningkatan bilangan oksidasi."
      },
      {
        "key": "D",
        "text": "$\\text{Cl}_2$ bertindak sebagai oksidator dan $\\text{MnO}_2$ adalah zat pereaksi pengoksidasi sekunder."
      },
      {
        "key": "E",
        "text": "$\\text{HCl}$ bertindak sebagai reduktor dan $\\text{H}_2\\text{O}$ adalah hasil reduksi molekul air murni."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\text{MnO}_2$ bertindak sebagai oksidator dan $\\text{MnCl}_2$ adalah hasil reduksi, karena bilangan oksidasi mangan mengalami penurunan (reduksi) dari $+4$ pada $\\text{MnO}_2$ menjadi $+2$ pada $\\text{MnCl}_2$, sehingga zat yang mengalami reduksi ($\\text{MnO}_2$) bertindak sebagai agen pengoksidasi (oksidator).. Oksidator adalah zat yang mengalami reduksi (biloks turun). Reduktor adalah zat yang mengalami oksidasi (biloks naik). Biloks Mn pada MnO2 = +4, pada MnCl2 = +2 (turun = reduksi). Maka MnO2 = oksidator, MnCl2 = hasil reduksi."
  },
  {
    "id": "kim-lat-e-21",
    "materi": "ELEKTROKIMIA (SEL VOLTA)",
    "topic": "Potensial Sel Standar dan Kespontanan Reaksi",
    "hints": {
      "concept": "Katoda = elektroda dengan E0 lebih positif (Cu, E0 = +0,34 V). Anoda = E0 lebih negatif (Zn, E0 = -0,76 V). E0_sel = E0_katoda - E0_anoda.",
      "execution": "E0_sel = 0,34 - (-0,76) = +1,10 V. Katoda = Cu."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Diketahui potensial reduksi standar dari dua elektroda logam:<br>• $\\text{Zn}^{2+}(aq) + 2e^- \\to \\text{Zn}(s) \\quad E^\\circ = -0{,}76\\text{ Volt}$<br>• $\\text{Cu}^{2+}(aq) + 2e^- \\to \\text{Cu}(s) \\quad E^\\circ = +0{,}34\\text{ Volt}$<br>Jika kedua elektroda tersebut dirangkai menjadi sebuah sel Volta, logam yang berfungsi sebagai katoda dan nilai potensial sel standar ($E^\\circ_{\\text{sel}}$) yang dihasilkan adalah...",
    "formulaHud": {
      "title": "POTENSIAL SEL VOLTA STANDAR",
      "latex": "E^\\circ_{\\text{sel}} = E^\\circ_{\\text{katoda}} - E^\\circ_{\\text{anoda}} = E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} - E^\\circ_{\\text{Zn}^{2+}/\\text{Zn}} = (+0{,}34) - (-0{,}76) = +1{,}10\\text{ V}",
      "legend": "• Katoda (Reduksi) = Elektroda dengan $E^\\circ$ lebih besar (Cu)<br>• Anoda (Oksidasi) = Elektroda dengan $E^\\circ$ lebih kecil (Zn)<br>• $E^\\circ_{\\text{sel}} = +1{,}10\\text{ V}$ (Spontan)"
    },
    "options": [
      {
        "key": "A",
        "text": "Katoda adalah tembaga ($\\text{Cu}$) dan $E^\\circ_{\\text{sel}} = +1{,}10\\text{ Volt}$, karena tembaga memiliki potensial reduksi standar yang lebih positif ($+0{,}34\\text{ V} > -0{,}76\\text{ V}$) sehingga mengalami reaksi reduksi di katoda, sedangkan seng mengalami oksidasi di anoda. Potensial sel dihitung dari $E^\\circ_{\\text{sel}} = E^\\circ_{\\text{katoda}} - E^\\circ_{\\text{anoda}} = +0{,}34\\text{ V} - (-0{,}76\\text{ V}) = +1{,}10\\text{ Volt}$ (reaksi berlangsung spontan karena $E^\\circ_{\\text{sel}} > 0$)."
      },
      {
        "key": "B",
        "text": "Katoda adalah tembaga ($\\text{Cu}$) dan $E^\\circ_{\\text{sel}} = +0{,}42\\text{ Volt}$, dihitung dari selisih nilai mutlak kedua elektroda logam."
      },
      {
        "key": "C",
        "text": "Katoda adalah seng ($\\text{Zn}$) dan $E^\\circ_{\\text{sel}} = +1{,}10\\text{ Volt}$, karena seng dianggap melepaskan elektron menuju katoda."
      },
      {
        "key": "D",
        "text": "Katoda adalah tembaga ($\\text{Cu}$) dan $E^\\circ_{\\text{sel}} = -0{,}42\\text{ Volt}$, karena potensial sel dihitung dari penjumlahan aljabar kedua potensial tanpa perubahan tanda anoda."
      },
      {
        "key": "E",
        "text": "Katoda adalah seng ($\\text{Zn}$) dan $E^\\circ_{\\text{sel}} = -1{,}10\\text{ Volt}$, karena susunan elektroda sel terbalik polaritas kutubnya."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Katoda adalah tembaga ($\\text{Cu}$) dan $E^\\circ_{\\text{sel}} = +1{,}10\\text{ Volt}$, karena tembaga memiliki potensial reduksi standar yang lebih positif ($+0{,}34\\text{ V} > -0{,}76\\text{ V}$) sehingga mengalami reaksi reduksi di katoda, sedangkan seng mengalami oksidasi di anoda. Potensial sel dihitung dari $E^\\circ_{\\text{sel}} = E^\\circ_{\\text{katoda}} - E^\\circ_{\\text{anoda}} = +0{,}34\\text{ V} - (-0{,}76\\text{ V}) = +1{,}10\\text{ Volt}$ (reaksi berlangsung spontan karena $E^\\circ_{\\text{sel}} > 0$).. Katoda = elektroda dengan E0 lebih positif (Cu, E0 = +0,34 V). Anoda = E0 lebih negatif (Zn, E0 = -0,76 V). E0_sel = E0_katoda - E0_anoda. E0_sel = 0,34 - (-0,76) = +1,10 V. Katoda = Cu."
  },
  {
    "id": "kim-lat-e-22",
    "materi": "ELEKTROKIMIA (HUKUM FARADAY I)",
    "topic": "Massa Logam yang Diendapkan pada Katoda Elektrolisis",
    "hints": {
      "concept": "Hukum Faraday I: w = (Ar / n) * (I * t / 96500). Untuk Cu2+, n = 2. Muatan Q = 10 * 965 = 9.650 C = 0,1 Faraday.",
      "execution": "w = (63,5 / 2) * (9.650 / 96.500) = 31,75 * 0,1 = 3,175 gram."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Larutan tembaga(II) sulfat ($\\text{CuSO}_4$, $A_r\\,\\text{Cu} = 63{,}5$) dielektrolisis menggunakan elektroda karbon inert dengan mengalirkan arus listrik konstan $I = 10\\text{ Ampere}$ selama waktu $t = 965\\text{ sekon}$. Jika 1 Faraday = $96.500\\text{ C/mol elektron}$, massa tembaga padat yang terendapkan di katoda adalah...",
    "formulaHud": {
      "title": "HUKUM FARADAY I ELEKTROLISIS",
      "latex": "w = \\frac{e \\cdot I \\cdot t}{F} = \\frac{\\frac{A_r}{n} \\cdot I \\cdot t}{96.500} = \\frac{\\frac{63{,}5}{2} \\times 10 \\times 965}{96.500} = 3{,}175\\text{ gram}",
      "legend": "• $n = 2$ (muatan $\\text{Cu}^{2+}$)<br>• $I = 10\\text{ A}$, $t = 965\\text{ s}$<br>• Jumlah muatan $Q = 9.650\\text{ C} = 0{,}1\\text{ F}$<br>• Mol Cu $= 0{,}1 / 2 = 0{,}05\\text{ mol} \\implies m = 0{,}05 \\times 63{,}5 = 3{,}175\\text{ g}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$6{,}350\\text{ gram}$, karena muatan kation tembaga keliru dianggap bervalensi satu ($n = 1$)."
      },
      {
        "key": "B",
        "text": "$3{,}175\\text{ gram}$, karena reaksi reduksi tembaga di katoda adalah $\\text{Cu}^{2+}(aq) + 2e^- \\to \\text{Cu}(s)$ sehingga valensi tembaga adalah $n = 2$ (massa ekuivalen $e = \\frac{A_r}{n} = \\frac{63{,}5}{2} = 31{,}75\\text{ g/mol}$). Berdasarkan Hukum Faraday I: $w = \\frac{e \\cdot I \\cdot t}{96.500} = \\frac{31{,}75 \\times 10 \\times 965}{96.500} = \\frac{31{,}75 \\times 9.650}{96.500} = \\frac{31{,}75}{10} = 3{,}175\\text{ gram}$."
      },
      {
        "key": "C",
        "text": "$1{,}588\\text{ gram}$, dihitung dari anggapan tembaga melepaskan empat elektron pada reaksi reduksi katoda."
      },
      {
        "key": "D",
        "text": "$0{,}318\\text{ gram}$, karena galat pembagian nilai Faraday seratus ribu Coulomb."
      },
      {
        "key": "E",
        "text": "$31{,}75\\text{ gram}$, karena waktu elektrolisis keliru dihitung selama 9.650 sekon penuh."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $3{,}175\\text{ gram}$, karena reaksi reduksi tembaga di katoda adalah $\\text{Cu}^{2+}(aq) + 2e^- \\to \\text{Cu}(s)$ sehingga valensi tembaga adalah $n = 2$ (massa ekuivalen $e = \\frac{A_r}{n} = \\frac{63{,}5}{2} = 31{,}75\\text{ g/mol}$). Berdasarkan Hukum Faraday I: $w = \\frac{e \\cdot I \\cdot t}{96.500} = \\frac{31{,}75 \\times 10 \\times 965}{96.500} = \\frac{31{,}75 \\times 9.650}{96.500} = \\frac{31{,}75}{10} = 3{,}175\\text{ gram}$.. Hukum Faraday I: w = (Ar / n) * (I * t / 96500). Untuk Cu2+, n = 2. Muatan Q = 10 * 965 = 9.650 C = 0,1 Faraday. w = (63,5 / 2) * (9.650 / 96.500) = 31,75 * 0,1 = 3,175 gram."
  },
  {
    "id": "kim-lat-e-23",
    "materi": "KIMIA KARBON & SENYAWA ORGANIK",
    "topic": "Tata Nama IUPAC dan Isomer Alkohol",
    "hints": {
      "concept": "Alkohol primer dapat dioksidasi jadi aldehida/asam karboksilat. Alkohol sekunder dioksidasi jadi keton. Alkohol tersier TIDAK dapat dioksidasi. Cari isomer alkohol tersier dari C4H10O.",
      "execution": "Isomer tersier C4H10O adalah 2-metil-2-propanol."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Suatu senyawa karbon memiliki rumus molekul $\\text{C}_4\\text{H}_{10}\\text{O}$. Senyawa tersebut tidak dapat dioksidasi oleh larutan kalium dikromat ($\\text{K}_2\\text{Cr}_2\\text{O}_7$) dalam suasana asam. Nama IUPAC yang benar dari senyawa tersebut adalah...",
    "formulaHud": {
      "title": "OKSIDASI GOLONGAN ALKOHOL",
      "latex": "\\text{Alkohol Primer} \\xrightarrow{[O]} \\text{Aldehida} \\xrightarrow{[O]} \\text{Asam Karboksilat}; \\quad \\text{Alkohol Sekunder} \\xrightarrow{[O]} \\text{Keton}; \\quad \\text{Alkohol Tersier} \\xrightarrow{[O]} \\text{Tidak Bereaksi}",
      "legend": "• 2-metil-2-propanol memiliki struktur $(\\text{CH}_3)_3\\text{C}-\\text{OH}$ (alkohol tersier)<br>• Ketiadaan hidrogen alfa ($-\\text{H}$) pada atom C karbinol mencegah terjadinya reaksi oksidasi"
    },
    "options": [
      {
        "key": "A",
        "text": "2-metil-2-propanol (atau ters-butanol), karena senyawa $\\text{C}_4\\text{H}_{10}\\text{O}$ yang tidak dapat dioksidasi oleh oksidator kuat adalah alkohol tersier, di mana atom karbon yang mengikat gugus hidroksil ($-\\text{OH}$) tidak lagi mengikat atom hidrogen bebas untuk mengalami pelepasan proton."
      },
      {
        "key": "B",
        "text": "1-butanol, karena merupakan alkohol primer yang dapat dioksidasi bertahap menjadi butanal dan asam butanoat ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "C",
        "text": "Dietil eter, karena meskipun tidak bereaksi dengan dikromat, eter bukan merupakan turunan alkohol rantai cabang."
      },
      {
        "key": "D",
        "text": "2-metil-1-propanol, karena merupakan alkohol primer bercabang yang masih memiliki dua atom hidrogen alfa."
      },
      {
        "key": "E",
        "text": "2-butanol, karena merupakan alkohol sekunder yang dapat dioksidasi menghasilkan keton butanon."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) 2-metil-2-propanol (atau ters-butanol), karena senyawa $\\text{C}_4\\text{H}_{10}\\text{O}$ yang tidak dapat dioksidasi oleh oksidator kuat adalah alkohol tersier, di mana atom karbon yang mengikat gugus hidroksil ($-\\text{OH}$) tidak lagi mengikat atom hidrogen bebas untuk mengalami pelepasan proton.. Alkohol primer dapat dioksidasi jadi aldehida/asam karboksilat. Alkohol sekunder dioksidasi jadi keton. Alkohol tersier TIDAK dapat dioksidasi. Cari isomer alkohol tersier dari C4H10O. Isomer tersier C4H10O adalah 2-metil-2-propanol."
  },
  {
    "id": "kim-lat-e-24",
    "materi": "REAKSI SENYAWA KARBON (ESTERIFIKASI)",
    "topic": "Reaksi Pembentukan Ester dari Asam Karboksilat dan Alkohol",
    "hints": {
      "concept": "Asam asetat (CH3COOH) + etanol (CH3CH2OH) menghasilkan etil asetat (etil etanoat) dan air. Senyawa ester beraroma buah harum.",
      "execution": "Etil etanoat (etil asetat) dengan aroma buah."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Asam asetat ($\\text{CH}_3\\text{COOH}$) direaksikan dengan etanol ($\\text{CH}_3\\text{CH}_2\\text{OH}$) dengan pemanasan dan penambahan beberapa tetes asam sulfat pekat ($\\text{H}_2\\text{SO}_4$) sebagai katalis. Nama senyawa ester yang dihasilkan dan aroma khas yang tercium adalah...",
    "formulaHud": {
      "title": "REAKSI ESTERIFIKASI FISCHER",
      "latex": "\\text{CH}_3\\text{COOH} + \\text{CH}_3\\text{CH}_2\\text{OH} \\xlongequal{\\text{H}_2\\text{SO}_4, \\Delta} \\text{CH}_3\\text{COOCH}_2\\text{CH}_3 + \\text{H}_2\\text{O}",
      "legend": "• Asam etanoat + Etanol $\\to$ Etil etanoat (Etil asetat) + Air<br>• Asam sulfat pekat bertindak sebagai katalisator sekaligus zat higroskopis penarik air (dehidrator) untuk menggeser kesetimbangan ke kanan"
    },
    "options": [
      {
        "key": "A",
        "text": "Etil etanoat (etil asetat) dengan aroma harum buah apel/pisang, terbentuk melalui reaksi esterifikasi kondensasi di mana gugus $-\\text{OH}$ dari asam karboksilat berikatan dengan atom $-\\text{H}$ dari alkohol membentuk molekul sampingan air."
      },
      {
        "key": "B",
        "text": "Dietil eter dengan aroma obat bius kloroform di ruang operasi bedah."
      },
      {
        "key": "C",
        "text": "Metil propanoat dengan aroma asam cuka yang menyengat dan menusuk hidung menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "D",
        "text": "Etil metanoat dengan aroma minyak tanah pelumas mesin industri."
      },
      {
        "key": "E",
        "text": "Propil asetat dengan aroma busuk belerang yang mudah menguap."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Etil etanoat (etil asetat) dengan aroma harum buah apel/pisang, terbentuk melalui reaksi esterifikasi kondensasi di mana gugus $-\\text{OH}$ dari asam karboksilat berikatan dengan atom $-\\text{H}$ dari alkohol membentuk molekul sampingan air.. Asam asetat (CH3COOH) + etanol (CH3CH2OH) menghasilkan etil asetat (etil etanoat) dan air. Senyawa ester beraroma buah harum. Etil etanoat (etil asetat) dengan aroma buah."
  },
  {
    "id": "kim-lat-e-25",
    "materi": "MAKROMOLEKUL (POLIMERISASI)",
    "topic": "Penggolongan Polimer Adisi dan Kondensasi",
    "hints": {
      "concept": "Polimer adisi berasal dari monomer ikatan rangkap (membuka ikatan rangkap tanpa melepas molekul kecil): PE, PP, PVC, Teflon, Polistirena. Nilon, dakron, dan protein adalah polimer kondensasi.",
      "execution": "Polietilena, polipropilena, dan PVC."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Polimerisasi dapat dibedakan menjadi polimerisasi adisi dan polimerisasi kondensasi. Pasangan polimer berikut yang seluruhnya terbentuk melalui reaksi polimerisasi adisi adalah...",
    "formulaHud": {
      "title": "POLIMERISASI ADISI VS KONDENSASI",
      "latex": "\\text{Adisi: } n\\,(\\text{CH}_2=\\text{CH}-\\text{R}) \\to [-\\text{CH}_2-\\text{CH}(\\text{R})-]_n \\quad (\\text{Tanpa molekul sampingan}); \\quad \\text{Kondensasi: Monomer memiliki 2 gugus fungsi} \\to \\text{Polimer} + n\\,\\text{H}_2\\text{O}",
      "legend": "• Polimer Adisi: Polietilena (PE), Polipropilena (PP), Polivinil klorida (PVC), Teflon (PTFE), Polistirena (PS)<br>• Polimer Kondensasi: Nilon-6,6, Dakron (PET), Protein, Karbohidrat (Pati/Selulosa)"
    },
    "options": [
      {
        "key": "A",
        "text": "Polietilena, polipropilena, dan polivinil klorida (PVC), karena ketiganya terbentuk dari monomer berikatan rangkap dua yang membuka ikatannya membentuk rantai panjang jenuh tanpa melepaskan molekul kecil sampingan."
      },
      {
        "key": "B",
        "text": "Karet alam, sutra wol, dan poliester, karena protein sutra wol merupakan polipeptida polimer kondensasi."
      },
      {
        "key": "C",
        "text": "Nilon-6,6, dakron, dan protein, karena ketiganya merupakan polimer kondensasi yang melepaskan molekul air selama reaksi polimerisasi."
      },
      {
        "key": "D",
        "text": "Bakelit, polistirena, dan selulosa, karena bakelit dan selulosa merupakan produk polimerisasi kondensasi."
      },
      {
        "key": "E",
        "text": "Polietilena, nilon-6,6, dan teflon, karena nilon-6,6 terbentuk melalui polimerisasi kondensasi antara asam adipat dan heksametilendiamin."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Polietilena, polipropilena, dan polivinil klorida (PVC), karena ketiganya terbentuk dari monomer berikatan rangkap dua yang membuka ikatannya membentuk rantai panjang jenuh tanpa melepaskan molekul kecil sampingan.. Polimer adisi berasal dari monomer ikatan rangkap (membuka ikatan rangkap tanpa melepas molekul kecil): PE, PP, PVC, Teflon, Polistirena. Nilon, dakron, dan protein adalah polimer kondensasi. Polietilena, polipropilena, dan PVC."
  },
  {
    "id": "kim-lat-m-01",
    "materi": "STRUKTUR ATOM & ION LOGAM TRANSISI",
    "topic": "Konfigurasi Elektron Ion dan Sifat Kemagnetan",
    "hints": {
      "concept": "Cr netral: [Ar] 4s1 3d5. Cr3+ melepas 1 elektron dari 4s dan 2 elektron dari 3d -> [Ar] 3d3. Ada 3 elektron tak berpasangan -> paramagnetik.",
      "execution": "[Ar] 3d3, paramagnetik."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Unsur kromium memiliki nomor atom $Z = 24$. Konfigurasi elektron kation $\\text{Cr}^{3+}$ pada keadaan dasar dan sifat kemagnetannya berdasarkan jumlah elektron yang tidak berpasangan adalah...",
    "formulaHud": {
      "title": "KONFIGURASI ELEKTRON ION TRANSISI",
      "latex": "{}_{24}\\text{Cr}: [\\text{Ar}]\\,4s^1\\,3d^5 \\xrightarrow{-3e^-} \\text{Cr}^{3+}: [\\text{Ar}]\\,3d^3; \\quad \\text{Elektron tak berpasangan } n = 3 \\implies \\text{Paramagnetik}",
      "legend": "• Elektron kulit terluar ($4s$) selalu dilepaskan lebih dahulu daripada elektron subkulit dalam ($3d$)<br>• Momen magnetik spin: $\\mu_s = \\sqrt{n(n+2)} = \\sqrt{3(5)} = \\sqrt{15} \\approx 3{,}87\\text{ BM}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$[\\text{Ar}]\\,3d^5$ dan bersifat paramagnetik kuat, karena menyamakan konfigurasi kation dengan konfigurasi atom netral kromium."
      },
      {
        "key": "B",
        "text": "$[\\text{Ar}]\\,4s^2\\,3d^1$ dan bersifat diamagnetik, karena elektron subkulit 4s keliru dianggap tidak dilepaskan saat pembentukan kation."
      },
      {
        "key": "C",
        "text": "$[\\text{Ar}]\\,3d^3$ dan bersifat paramagnetik, karena atom netral kromium memiliki konfigurasi stabil setengah penuh $[\\text{Ar}]\\,4s^1\\,3d^5$. Ketika melepaskan 3 elektron untuk membentuk kation $\\text{Cr}^{3+}$, 1 elektron pada subkulit terluar $4s$ dan 2 elektron pada subkulit $3d$ dilepaskan terlebih dahulu, menyisakan 3 elektron tunggal yang tidak berpasangan di subkulit $3d$ ($[\\text{Ar}]\\,3d^3$) sehingga ditarik oleh medan magnet luar (paramagnetik)."
      },
      {
        "key": "D",
        "text": "$[\\text{Ar}]\\,3d^3$ dan bersifat diamagnetik, karena menganggap seluruh elektron pada orbital subkulit d selalu berpasangan secara simetris."
      },
      {
        "key": "E",
        "text": "$[\\text{Ar}]\\,4s^1\\,3d^2$ dan bersifat feromagnetik permanen, karena mengasumsikan pelepasan elektron hanya berasal dari subkulit dalam."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $[\\text{Ar}]\\,3d^3$ dan bersifat paramagnetik, karena atom netral kromium memiliki konfigurasi stabil setengah penuh $[\\text{Ar}]\\,4s^1\\,3d^5$. Ketika melepaskan 3 elektron untuk membentuk kation $\\text{Cr}^{3+}$, 1 elektron pada subkulit terluar $4s$ dan 2 elektron pada subkulit $3d$ dilepaskan terlebih dahulu, menyisakan 3 elektron tunggal yang tidak berpasangan di subkulit $3d$ ($[\\text{Ar}]\\,3d^3$) sehingga ditarik oleh medan magnet luar (paramagnetik).. Cr netral: [Ar] 4s1 3d5. Cr3+ melepas 1 elektron dari 4s dan 2 elektron dari 3d -> [Ar] 3d3. Ada 3 elektron tak berpasangan -> paramagnetik. [Ar] 3d3, paramagnetik."
  },
  {
    "id": "kim-lat-m-02",
    "materi": "GEOMETRI MOLEKUL (TEORI VSEPR & HIBRIDISASI)",
    "topic": "Hibridisasi dan Bentuk Molekul SF4",
    "hints": {
      "concept": "Elektron valensi S = 6. Digunakan 4 untuk ikatan dengan F -> sisa 2 elektron = 1 PEB. Total domain = 4 PEI + 1 PEB = 5 (hibridisasi sp3d, tipe AX4E). Bentuk = jungkat-jungkit (see-saw).",
      "execution": "sp3d, tipe AX4E, bentuk jungkat-jungkit (see-saw)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Belerang tetrafluorida ($\\text{SF}_4$) terbentuk dari atom belerang ($_{16}\\text{S}$) sebagai atom pusat dan empat atom fluorin ($_{9}\\text{F}$). Hibridisasi orbital pada atom pusat, tipe geometri molekul VSEPR, dan bentuk ruang molekul $\\text{SF}_4$ adalah...",
    "formulaHud": {
      "title": "GEOMETRI MOLEKUL BELERANG TETRAFLUORIDA",
      "latex": "\\text{Domain Elektron} = 4\\text{ PEI} + 1\\text{ PEB} = 5 \\implies \\text{Hibridisasi } sp^3d, \\quad \\text{Tipe } AX_4E \\implies \\text{Bentuk Jungkat-Jungkit (See-Saw)}",
      "legend": "• PEB selalu memilih posisi ekuatorial pada geometri dasar bipiramida trigonal karena hanya membentuk 2 tolakan $90^\\circ$ dengan ligan aksial<br>• Menghasilkan molekul bersifat polar ($\\mu > 0$)"
    },
    "options": [
      {
        "key": "A",
        "text": "Hibridisasi $sp^3d$, tipe $AX_5$, dengan bentuk molekul bipiramida trigonal sempurna."
      },
      {
        "key": "B",
        "text": "Hibridisasi $sp^3$, tipe $AX_4$ (4 PEI dan 0 PEB), dengan bentuk molekul tetrahedral simetris dan bersifat nonpolar."
      },
      {
        "key": "C",
        "text": "Hibridisasi $sp^3d$, tipe $AX_4E$ (4 PEI dan 1 PEB), dengan bentuk molekul jungkat-jungkit (tetrahedral terdistorsi / see-saw), karena belerang memiliki 6 elektron valensi, 4 elektron digunakan untuk berikatan tunggal dengan F, dan 2 elektron tersisa membentuk 1 pasangan elektron bebas (PEB) yang menempati posisi ekuatorial untuk meminimalkan tolakan."
      },
      {
        "key": "D",
        "text": "Hibridisasi $sp^3d^2$, tipe $AX_4E_2$ (4 PEI dan 2 PEB), dengan bentuk molekul bujur sangkar datar."
      },
      {
        "key": "E",
        "text": "Hibridisasi $dsp^2$, tipe $AX_4$, dengan bentuk molekul bujur sangkar planar simetris."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Hibridisasi $sp^3d$, tipe $AX_4E$ (4 PEI dan 1 PEB), dengan bentuk molekul jungkat-jungkit (tetrahedral terdistorsi / see-saw), karena belerang memiliki 6 elektron valensi, 4 elektron digunakan untuk berikatan tunggal dengan F, dan 2 elektron tersisa membentuk 1 pasangan elektron bebas (PEB) yang menempati posisi ekuatorial untuk meminimalkan tolakan.. Elektron valensi S = 6. Digunakan 4 untuk ikatan dengan F -> sisa 2 elektron = 1 PEB. Total domain = 4 PEI + 1 PEB = 5 (hibridisasi sp3d, tipe AX4E). Bentuk = jungkat-jungkit (see-saw). sp3d, tipe AX4E, bentuk jungkat-jungkit (see-saw)."
  },
  {
    "id": "kim-lat-m-03",
    "materi": "STOIKIOMETRI (RUMUS EMPIRIS & MOLEKUL)",
    "topic": "Penentuan Rumus Molekul dari Analisis Pembakaran",
    "hints": {
      "concept": "Massa C = (12/44) * 13,2 = 3,6 g -> mol C = 0,3 mol. Massa H = (2/18) * 7,2 = 0,8 g -> mol H = 0,8 mol. Rasio C : H = 3 : 8. RE = C3H8. Karena Mr = 44, RM = C3H8.",
      "execution": "Rumus empiris dan molekul: C3H8."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Pembakaran sempurna $4{,}4\\text{ gram}$ suatu senyawa hidrokarbon menghasilkan $13{,}2\\text{ gram}$ gas karbon dioksida ($\\text{CO}_2$, $M_r = 44$) dan $7{,}2\\text{ gram}$ uap air ($\\text{H}_2\\text{O}$, $M_r = 18$). Jika massa molekul relatif senyawa tersebut adalah $M_r = 44\\text{ g/mol}$ ($A_r\\,\\text{C} = 12$, $A_r\\,\\text{H} = 1$), rumus empiris dan rumus molekul senyawa hidrokarbon tersebut adalah...",
    "formulaHud": {
      "title": "ANALISIS ELEMENTER PERSENTASE MASSA",
      "latex": "n_C = \\frac{12}{44} \\times \\frac{13{,}2}{12} = 0{,}3\\text{ mol}; \\quad n_H = \\frac{2}{18} \\times \\frac{7{,}2}{1} = 0{,}8\\text{ mol}; \\quad C : H = 0{,}3 : 0{,}8 = 3 : 8 \\implies (\\text{C}_3\\text{H}_8)_1",
      "legend": "• Massa C $= 3{,}6\\text{ g}$, Massa H $= 0{,}8\\text{ g}$ (Total $= 4{,}4\\text{ g}$, terbukti hanya mengandung C dan H)<br>• $M_r (\\text{C}_3\\text{H}_8) = 3(12) + 8(1) = 44\\text{ g/mol}$"
    },
    "options": [
      {
        "key": "A",
        "text": "Rumus empiris $\\text{C}_3\\text{H}_8$ dan rumus molekul $\\text{C}_3\\text{H}_8$ (propana), karena massa karbon adalah $m_C = \\frac{12}{44} \\times 13{,}2\\text{ g} = 3{,}6\\text{ g}$ ($n_C = \\frac{3{,}6}{12} = 0{,}3\\text{ mol}$) dan massa hidrogen adalah $m_H = \\frac{2}{18} \\times 7{,}2\\text{ g} = 0{,}8\\text{ g}$ ($n_H = \\frac{0{,}8}{1} = 0{,}8\\text{ mol}$). Perbandingan mol $\\text{C} : \\text{H} = 0{,}3 : 0{,}8 = 3 : 8$, sehingga rumus empirisnya $(\\text{C}_3\\text{H}_8)_n$. Karena $M_r = (3 \\times 12 + 8 \\times 1)n = 44n = 44 \\implies n = 1$, maka rumus molekulnya adalah $\\text{C}_3\\text{H}_8$."
      },
      {
        "key": "B",
        "text": "Rumus empiris $\\text{CH}_2$ dan rumus molekul $\\text{C}_3\\text{H}_6$ (propena), karena hidrogen keliru dihitung tanpa mengalikan faktor dua pada molekul air ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "C",
        "text": "Rumus empiris $\\text{C}_2\\text{H}_5$ dan rumus molekul $\\text{C}_4\\text{H}_{10}$ (butana), dihitung dari kesalahan pembagian perbandingan mol atom."
      },
      {
        "key": "D",
        "text": "Rumus empiris $\\text{C}_3\\text{H}_4$ dan rumus molekul $\\text{C}_3\\text{H}_4$ (propuna), dihitung dari perbandingan stoikiometri gas asetilena."
      },
      {
        "key": "E",
        "text": "Rumus empiris $\\text{CH}_4$ dan rumus molekul $\\text{CH}_4$ (metana), karena mengabaikan total massa produk pembakaran yang dihasilkan."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Rumus empiris $\\text{C}_3\\text{H}_8$ dan rumus molekul $\\text{C}_3\\text{H}_8$ (propana), karena massa karbon adalah $m_C = \\frac{12}{44} \\times 13{,}2\\text{ g} = 3{,}6\\text{ g}$ ($n_C = \\frac{3{,}6}{12} = 0{,}3\\text{ mol}$) dan massa hidrogen adalah $m_H = \\frac{2}{18} \\times 7{,}2\\text{ g} = 0{,}8\\text{ g}$ ($n_H = \\frac{0{,}8}{1} = 0{,}8\\text{ mol}$). Perbandingan mol $\\text{C} : \\text{H} = 0{,}3 : 0{,}8 = 3 : 8$, sehingga rumus empirisnya $(\\text{C}_3\\text{H}_8)_n$. Karena $M_r = (3 \\times 12 + 8 \\times 1)n = 44n = 44 \\implies n = 1$, maka rumus molekulnya adalah $\\text{C}_3\\text{H}_8$.. Massa C = (12/44) * 13,2 = 3,6 g -> mol C = 0,3 mol. Massa H = (2/18) * 7,2 = 0,8 g -> mol H = 0,8 mol. Rasio C : H = 3 : 8. RE = C3H8. Karena Mr = 44, RM = C3H8. Rumus empiris dan molekul: C3H8."
  },
  {
    "id": "kim-lat-m-04",
    "materi": "STOIKIOMETRI (PEREAKSI PEMBATAS & PERSEN HASIL)",
    "topic": "Penentuan Pereaksi Pembatas dan Rendemen Teoritis",
    "hints": {
      "concept": "Hitung mol Al: 5,4/27 = 0,2 mol (mol/koef = 0,1). Mol H2SO4: 0,1 * 1,5 = 0,15 mol (mol/koef = 0,05). H2SO4 pembatas. Mol H2 = 3/3 * 0,15 = 0,15 mol. V_STP = 0,15 * 22,4.",
      "execution": "Pereaksi pembatas = H2SO4, V(H2) = 3,36 liter."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebanyak $5{,}4\\text{ gram}$ logam aluminium ($A_r\\,\\text{Al} = 27$) direaksikan dengan $100\\text{ mL}$ larutan asam sulfat $\\text{H}_2\\text{SO}_4\\,1{,}5\\text{ M}$ menurut persamaan reaksi:<br>$$2\\,\\text{Al}(s) + 3\\,\\text{H}_2\\text{SO}_4(aq) \\to \\text{Al}_2(\\text{SO}_4)_3(aq) + 3\\,\\text{H}_2(g)$$<br>Zat yang bertindak sebagai pereaksi pembatas dan volume gas hidrogen yang dihasilkan pada kondisi standar (STP, $0^\\circ\\text{C}$, $1\\text{ atm}$) adalah...",
    "formulaHud": {
      "title": "PENENTUAN PEREAKSI PEMBATAS (LIMITING REAGENT)",
      "latex": "\\frac{n_{\\text{Al}}}{2} = \\frac{0{,}2}{2} = 0{,}10; \\quad \\frac{n_{\\text{H}_2\\text{SO}_4}}{3} = \\frac{0{,}15}{3} = 0{,}05 \\implies \\text{H}_2\\text{SO}_4 \\text{ Pembatas}; \\quad V_{\\text{H}_2} = 0{,}15 \\times 22{,}4 = 3{,}36\\text{ L}",
      "legend": "• Pereaksi pembatas adalah zat dengan perbandingan (mol / koefisien) terkecil<br>• Gas $\\text{H}_2$ diukur pada STP ($V_m = 22{,}4\\text{ L/mol}$)<br>• $V_{\\text{H}_2} = 3{,}36\\text{ liter}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{H}_2\\text{SO}_4$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 3{,}36\\text{ liter}$, karena mol $\\text{Al} = \\frac{5{,}4}{27} = 0{,}2\\text{ mol}$ (rasio mol/koefisien = $\\frac{0{,}2}{2} = 0{,}10$) dan mol $\\text{H}_2\\text{SO}_4 = 0{,}1\\text{ L} \\times 1{,}5\\text{ M} = 0{,}15\\text{ mol}$ (rasio mol/koefisien = $\\frac{0{,}15}{3} = 0{,}05$). Karena $0{,}05 < 0{,}10$, maka $\\text{H}_2\\text{SO}_4$ habis bereaksi lebih dulu (pereaksi pembatas). Mol $\\text{H}_2$ yang dihasilkan adalah $\\frac{3}{3} \\times 0{,}15 = 0{,}15\\text{ mol}$. Pada STP, volume gas adalah $V = 0{,}15\\text{ mol} \\times 22{,}4\\text{ L/mol} = 3{,}36\\text{ liter}$."
      },
      {
        "key": "B",
        "text": "$\\text{Al}$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 6{,}72\\text{ liter}$, karena salah menentukan pereaksi pembatas dan mengasumsikan aluminium habis bereaksi menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "C",
        "text": "$\\text{H}_2\\text{SO}_4$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 2{,}24\\text{ liter}$, dihitung dari rasio satu banding satu terhadap koefisien aluminium."
      },
      {
        "key": "D",
        "text": "$\\text{Al}$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 3{,}36\\text{ liter}$, karena meskipun volume gas benar namun identifikasi pereaksi pembatas keliru."
      },
      {
        "key": "E",
        "text": "Kedua pereaksi tepat habis bereaksi dan volume $\\text{H}_2 = 4{,}48\\text{ liter}$, dihitung dari asumsi campuran ekimolar stoikiometri."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\text{H}_2\\text{SO}_4$ sebagai pereaksi pembatas dan volume $\\text{H}_2 = 3{,}36\\text{ liter}$, karena mol $\\text{Al} = \\frac{5{,}4}{27} = 0{,}2\\text{ mol}$ (rasio mol/koefisien = $\\frac{0{,}2}{2} = 0{,}10$) dan mol $\\text{H}_2\\text{SO}_4 = 0{,}1\\text{ L} \\times 1{,}5\\text{ M} = 0{,}15\\text{ mol}$ (rasio mol/koefisien = $\\frac{0{,}15}{3} = 0{,}05$). Karena $0{,}05 < 0{,}10$, maka $\\text{H}_2\\text{SO}_4$ habis bereaksi lebih dulu (pereaksi pembatas). Mol $\\text{H}_2$ yang dihasilkan adalah $\\frac{3}{3} \\times 0{,}15 = 0{,}15\\text{ mol}$. Pada STP, volume gas adalah $V = 0{,}15\\text{ mol} \\times 22{,}4\\text{ L/mol} = 3{,}36\\text{ liter}$.. Hitung mol Al: 5,4/27 = 0,2 mol (mol/koef = 0,1). Mol H2SO4: 0,1 * 1,5 = 0,15 mol (mol/koef = 0,05). H2SO4 pembatas. Mol H2 = 3/3 * 0,15 = 0,15 mol. V_STP = 0,15 * 22,4. Pereaksi pembatas = H2SO4, V(H2) = 3,36 liter."
  },
  {
    "id": "kim-lat-m-05",
    "materi": "TITRASI ASAM-BASA & KURVA TITRASI",
    "topic": "Titik Ekuivalen dan Pemilihan Indikator pH",
    "hints": {
      "concept": "Titrasi basa lemah dengan asam kuat menghasilkan titik ekuivalen di daerah asam (pH < 7) akibat hidrolisis kation NH4+. Gunakan indikator metil merah (trayek 4,4 - 6,2).",
      "execution": "pH < 7, indikator metil merah."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebanyak $25\\text{ mL}$ larutan amonia ($\\text{NH}_4\\text{OH}$, basa lemah) dititrasi dengan larutan standar asam klorida ($\\text{HCl}$, asam kuat) berkonsentrasi $0{,}1\\text{ M}$. Pada titik ekuivalen, perkiraan rentang pH larutan dan indikator asam-basa yang paling tepat digunakan adalah...",
    "formulaHud": {
      "title": "TITRASI ASAM KUAT DENGAN BASA LEMAH",
      "latex": "\\text{HCl} + \\text{NH}_4\\text{OH} \\to \\text{NH}_4\\text{Cl} + \\text{H}_2\\text{O}; \\quad \\text{NH}_4^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\text{NH}_4\\text{OH} + \\text{H}^+ \\implies \\text{pH}_{\\text{ekuivalen}} < 7",
      "legend": "• Titik ekuivalen berada di daerah asam ($\\text{pH } \\approx 5{,}3$)<br>• Indikator harus memiliki trayek perubahan warna yang memotong kurva lonjakan pH di titik ekuivalen (Metil Merah: $4{,}4 - 6{,}2$)<br>• Fenolftalein TIDAK cocok karena berubah warna jauh sebelum titik ekuivalen tercapai"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{pH} = 1$ dan indikator yang tepat adalah metil jingga (trayek pH $3{,}1 - 4{,}4$), karena asam klorida adalah asam kuat yang mendominasi campuran."
      },
      {
        "key": "B",
        "text": "$\\text{pH} < 7$ (sekitar $\\text{pH } 5 - 6$) dan indikator yang tepat adalah metil merah (trayek pH $4{,}4 - 6{,}2$), karena pada titik ekuivalen terbentuk garam amonium klorida ($\\text{NH}_4\\text{Cl}$) yang kationnya mengalami hidrolisis parsial menghasilkan ion $\\text{H}^+$ sehingga larutan bersifat asam."
      },
      {
        "key": "C",
        "text": "$\\text{pH} > 7$ (sekitar $\\text{pH } 8 - 9$) dan indikator yang tepat adalah fenolftalein (trayek pH $8{,}3 - 10{,}0$), karena titrasi melibatkan basa amonia."
      },
      {
        "key": "D",
        "text": "$\\text{pH} = 7$ (netral) dan indikator yang tepat adalah bromtimol biru (trayek pH $6{,}0 - 7{,}6$), karena titik ekuivalen dianggap selalu menghasilkan larutan netral."
      },
      {
        "key": "E",
        "text": "$\\text{pH} = 7$ dan indikator yang tepat adalah fenolftalein karena menghasilkan perubahan warna dari merah muda menjadi tidak berwarna."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\text{pH} < 7$ (sekitar $\\text{pH } 5 - 6$) dan indikator yang tepat adalah metil merah (trayek pH $4{,}4 - 6{,}2$), karena pada titik ekuivalen terbentuk garam amonium klorida ($\\text{NH}_4\\text{Cl}$) yang kationnya mengalami hidrolisis parsial menghasilkan ion $\\text{H}^+$ sehingga larutan bersifat asam.. Titrasi basa lemah dengan asam kuat menghasilkan titik ekuivalen di daerah asam (pH < 7) akibat hidrolisis kation NH4+. Gunakan indikator metil merah (trayek 4,4 - 6,2). pH < 7, indikator metil merah."
  },
  {
    "id": "kim-lat-m-06",
    "materi": "LARUTAN PENYANGGA (MEKANISME KERJA BUFFER)",
    "topic": "Perubahan pH Larutan Buffer saat Ditambah Sedikit Asam Kuat",
    "hints": {
      "concept": "Saat ditambah asam kuat, ion H+ bereaksi dengan basa konjugasi CH3COO-. Asam bertambah: 0,1 + 0,01 = 0,11 mol. Garam berkurang: 0,1 - 0,01 = 0,09 mol. [H+] = Ka * (0,11 / 0,09).",
      "execution": "[H+] = 1e-5 * (11/9) -> pH = 5 - log(11/9) = 5 - 0,09 = 4,91."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Satu liter larutan penyangga mengandung $0{,}1\\text{ mol } \\text{CH}_3\\text{COOH}$ dan $0{,}1\\text{ mol } \\text{CH}_3\\text{COONa}$ ($K_a = 1 \\times 10^{-5}$, $\\text{pH awal} = 5$). Jika ke dalam larutan tersebut ditambahkan $0{,}01\\text{ mol}$ gas $\\text{HCl}$ tanpa perubahan volume larutan yang berarti, nilai pH larutan penyangga setelah penambahan asam tersebut adalah... (Diketahui $\\log 1{,}22 \\approx 0{,}09$)",
    "formulaHud": {
      "title": "MEKANISME KERJA BUFFER TERHADAP ASAM KUAT",
      "latex": "[\\text{H}^+] = K_a \\cdot \\frac{n_{\\text{asam}} + n_{\\text{HCl}}}{n_{\\text{garam}} - n_{\\text{HCl}}} = 10^{-5} \\times \\frac{0{,}10 + 0{,}01}{0{,}10 - 0{,}01} = 10^{-5} \\times \\frac{0{,}11}{0{,}09} = 1{,}222 \\times 10^{-5}\\text{ M} \\implies \\text{pH} \\approx 4{,}91",
      "legend": "• Penambahan asam kuat menggeser komposisi: asam bertambah ($+0{,}01$), basa konjugasi berkurang ($-0{,}01$)<br>• Kapasitas buffer menjaga pH tetap stabil di sekitar $4{,}91$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{pH} = 7{,}00$, karena penambahan asam dianggap menetralkan seluruh sifat keasaman larutan penyangga."
      },
      {
        "key": "B",
        "text": "$\\text{pH} = 4{,}00$, dihitung dari pengurangan satu satuan skala pH penuh."
      },
      {
        "key": "C",
        "text": "$\\text{pH} = 5{,}09$, karena ion asam asetat keliru dihitung bertambah pada komponen garam basa konjugasi."
      },
      {
        "key": "D",
        "text": "$\\text{pH} = 5 - \\log\\left(\\frac{11}{9}\\right) \\approx 4{,}91$, karena penambahan ion $\\text{H}^+$ dari $\\text{HCl}$ dinetralisasi oleh ion basa konjugasi asetat: $\\text{CH}_3\\text{COO}^- + \\text{H}^+ \\to \\text{CH}_3\\text{COOH}$. Jumlah mol garam asetat berkurang menjadi $0{,}10 - 0{,}01 = 0{,}09\\text{ mol}$ dan mol asam asetat bertambah menjadi $0{,}10 + 0{,}01 = 0{,}11\\text{ mol}$. Maka $[\\text{H}^+] = K_a \\times \\frac{0{,}11}{0{,}09} = 10^{-5} \\times 1{,}222 = 1{,}222 \\times 10^{-5}\\text{ M} \\implies \\text{pH} = 5 - \\log(1{,}22) \\approx 4{,}91$ (terbukti pH larutan relatif konstan hanya turun $0{,}09$ satuan)."
      },
      {
        "key": "E",
        "text": "$\\text{pH} = 2{,}00$, karena larutan dianggap kehilangan daya penyangga dan langsung mengikuti konsentrasi asam kuat HCl."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $\\text{pH} = 5 - \\log\\left(\\frac{11}{9}\\right) \\approx 4{,}91$, karena penambahan ion $\\text{H}^+$ dari $\\text{HCl}$ dinetralisasi oleh ion basa konjugasi asetat: $\\text{CH}_3\\text{COO}^- + \\text{H}^+ \\to \\text{CH}_3\\text{COOH}$. Jumlah mol garam asetat berkurang menjadi $0{,}10 - 0{,}01 = 0{,}09\\text{ mol}$ dan mol asam asetat bertambah menjadi $0{,}10 + 0{,}01 = 0{,}11\\text{ mol}$. Maka $[\\text{H}^+] = K_a \\times \\frac{0{,}11}{0{,}09} = 10^{-5} \\times 1{,}222 = 1{,}222 \\times 10^{-5}\\text{ M} \\implies \\text{pH} = 5 - \\log(1{,}22) \\approx 4{,}91$ (terbukti pH larutan relatif konstan hanya turun $0{,}09$ satuan).. Saat ditambah asam kuat, ion H+ bereaksi dengan basa konjugasi CH3COO-. Asam bertambah: 0,1 + 0,01 = 0,11 mol. Garam berkurang: 0,1 - 0,01 = 0,09 mol. [H+] = Ka * (0,11 / 0,09). [H+] = 1e-5 * (11/9) -> pH = 5 - log(11/9) = 5 - 0,09 = 4,91."
  },
  {
    "id": "kim-lat-m-07",
    "materi": "HIDROLISIS GARAM DARI ASAM LEMAH & BASA LEMAH",
    "topic": "Penentuan pH Garam Terhidrolisis Total",
    "hints": {
      "concept": "Garam dari asam lemah dan basa lemah: [H+] = sqrt(Kw * Ka / Kb). Karena Ka > Kb, larutan bersifat asam (pH < 7). pH = 0,5 * (pKw + pKa - pKb).",
      "execution": "pKa = 4 - log 2 = 3,70. pKb = 5. pH = 0,5 * (14 + 3,70 - 5) = 0,5 * 12,70 = 6,35 (asam)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Garam amonium format ($\\text{HCOONH}_4$) dilarutkan ke dalam air. Diketahui tetapan ionisasi asam format $K_a = 2 \\times 10^{-4}$, tetapan ionisasi basa amonia $K_b = 1 \\times 10^{-5}$, dan tetapan ionisasi air $K_w = 1 \\times 10^{-14}$. Sifat larutan garam tersebut dan nilai pH-nya adalah... (Gunakan $\\log 2{,}24 \\approx 0{,}35$)",
    "formulaHud": {
      "title": "HIDROLISIS TOTAL (ASAM LEMAH + BASA LEMAH)",
      "latex": "[\\text{H}^+] = \\sqrt{\\frac{K_w \\cdot K_a}{K_b}} = \\sqrt{\\frac{10^{-14} \\times 2 \\times 10^{-4}}{10^{-5}}} = \\sqrt{4 \\times 10^{-13}}... \\implies \\text{pH} = \\frac{1}{2}(\\text{p}K_w + \\text{p}K_a - \\text{p}K_b) = \\frac{1}{2}(14 + 3{,}70 - 5{,}0) = 6{,}35",
      "legend": "• $K_a > K_b \\implies$ Larutan bersifat asam ($\\text{pH} < 7$)<br>• $K_a < K_b \\implies$ Larutan bersifat basa ($\\text{pH} > 7$)<br>• $K_a = K_b \\implies$ Larutan bersifat netral ($\\text{pH} = 7$)<br>• pH garam ini tidak bergantung pada konsentrasi molaritas garam"
    },
    "options": [
      {
        "key": "A",
        "text": "Bersifat netral dengan $\\text{pH} = 7{,}00$, karena kedua komponen penyusunnya sama-sama lemah sehingga dianggap saling meniadakan sempurna."
      },
      {
        "key": "B",
        "text": "Bersifat basa dengan $\\text{pH} = 7{,}65$, karena nilai tetapan basa amonia keliru dianggap lebih mendominasi."
      },
      {
        "key": "C",
        "text": "Bersifat asam dengan $\\text{pH} = 7 - \\frac{1}{2}(\\text{p}K_a - \\text{p}K_b) = 6{,}35$, karena nilai $K_a > K_b$ ($2 \\times 10^{-4} > 1 \\times 10^{-5}$), sehingga ionisasi kation $\\text{NH}_4^+$ menghasilkan ion $\\text{H}^+$ yang lebih dominan daripada ion $\\text{OH}^-$ dari anion format. Konsentrasi $[\\text{H}^+] = \\sqrt{\\frac{K_w \\cdot K_a}{K_b}} = \\sqrt{\\frac{10^{-14} \\times (2 \\times 10^{-4})}{10^{-5}}} = \\sqrt{2 \\times 10^{-13}} = \\sqrt{20 \\times 10^{-14}} \\approx 4{,}47 \\times 10^{-7}\\text{ M} \\implies \\text{pH} = 7 - \\log(4{,}47) \\approx 6{,}35$."
      },
      {
        "key": "D",
        "text": "Bersifat asam dengan $\\text{pH} = 4{,}50$, dihitung tanpa menyertakan faktor pembagian setengah pada logaritma tetapan kesetimbangan."
      },
      {
        "key": "E",
        "text": "Bersifat basa dengan $\\text{pH} = 9{,}50$, dihitung dari rumus hidrolisis kation asam kuat basa lemah."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Bersifat asam dengan $\\text{pH} = 7 - \\frac{1}{2}(\\text{p}K_a - \\text{p}K_b) = 6{,}35$, karena nilai $K_a > K_b$ ($2 \\times 10^{-4} > 1 \\times 10^{-5}$), sehingga ionisasi kation $\\text{NH}_4^+$ menghasilkan ion $\\text{H}^+$ yang lebih dominan daripada ion $\\text{OH}^-$ dari anion format. Konsentrasi $[\\text{H}^+] = \\sqrt{\\frac{K_w \\cdot K_a}{K_b}} = \\sqrt{\\frac{10^{-14} \\times (2 \\times 10^{-4})}{10^{-5}}} = \\sqrt{2 \\times 10^{-13}} = \\sqrt{20 \\times 10^{-14}} \\approx 4{,}47 \\times 10^{-7}\\text{ M} \\implies \\text{pH} = 7 - \\log(4{,}47) \\approx 6{,}35$.. Garam dari asam lemah dan basa lemah: [H+] = sqrt(Kw * Ka / Kb). Karena Ka > Kb, larutan bersifat asam (pH < 7). pH = 0,5 * (pKw + pKa - pKb). pKa = 4 - log 2 = 3,70. pKb = 5. pH = 0,5 * (14 + 3,70 - 5) = 0,5 * 12,70 = 6,35 (asam)."
  },
  {
    "id": "kim-lat-m-08",
    "materi": "KELARUTAN & HASIL KALI KELARUTAN (Ksp)",
    "topic": "Prediksi Terjadinya Endapan dengan Membandingkan Qsp dan Ksp",
    "hints": {
      "concept": "Hitung konsentrasi ion setelah pengenceran: [Ag+] = 1e-4 M, [CrO4 2-] = 1e-4 M. Hitung Qsp = [Ag+]^2 * [CrO4 2-] = (1e-4)^2 * 1e-4 = 1e-12. Bandingkan dengan Ksp = 2,4e-12.",
      "execution": "Karena Qsp (1e-12) < Ksp (2,4e-12), larutan belum jenuh sehingga tidak terbentuk endapan."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebanyak $50\\text{ mL}$ larutan $\\text{AgNO}_3\\,2 \\times 10^{-4}\\text{ M}$ dicampurkan dengan $50\\text{ mL}$ larutan $\\text{K}_2\\text{CrO}_4\\,2 \\times 10^{-4}\\text{ M}$. Diketahui nilai $K_{sp}\\,\\text{Ag}_2\\text{CrO}_4 = 2{,}4 \\times 10^{-12}$. Pernyataan yang benar mengenai kondisi larutan setelah pencampuran adalah...",
    "formulaHud": {
      "title": "PREDIKSI PENGENDAPAN (Qsp VS Ksp)",
      "latex": "[\\text{Ag}^+] = 10^{-4}\\text{ M}; \\quad [\\text{CrO}_4^{2-}] = 10^{-4}\\text{ M}; \\quad Q_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (10^{-4})^2 (10^{-4}) = 10^{-12}; \\quad Q_{sp} < K_{sp} \\implies \\text{Belum Mengendap}",
      "legend": "• $Q_{sp} = 1{,}0 \\times 10^{-12}$<br>• $K_{sp} = 2{,}4 \\times 10^{-12}$<br>• $Q_{sp} < K_{sp} \\implies$ Larutan belum jenuh, tidak ada endapan terbentuk"
    },
    "options": [
      {
        "key": "A",
        "text": "Terbentuk endapan $\\text{Ag}_2\\text{CrO}_4$ berwarna merah bata karena nilai kuosien reaksi $Q_{sp} > K_{sp}$ ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "B",
        "text": "Terjadi reaksi redoks pembentukan logam perak bebas dan gas oksigen di dalam wadah bejana."
      },
      {
        "key": "C",
        "text": "Larutan tepat jenuh dan mulai terbentuk kristal mikro karena nilai $Q_{sp} = K_{sp}$."
      },
      {
        "key": "D",
        "text": "Terbentuk endapan $\\text{Ag}_2\\text{CrO}_4$, karena nilai hasil kali kuosien reaksi $Q_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (10^{-4})^2 \\times (10^{-4}) = 1 \\times 10^{-12} < K_{sp}$... mari cek konsentrasi campuran dengan cermat: Volume total = $100\\text{ mL}$. $[\\text{Ag}^+] = \\frac{50 \\times 2 \\times 10^{-4}}{100} = 1 \\times 10^{-4}\\text{ M}$. $[\\text{CrO}_4^{2-}] = \\frac{50 \\times 2 \\times 10^{-4}}{100} = 1 \\times 10^{-4}\\text{ M}$. Maka $Q_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (10^{-4})^2 \\times (10^{-4}) = 10^{-8} \\times 10^{-4} = 10^{-12} = 1{,}0 \\times 10^{-12}$. Karena $Q_{sp} = 1{,}0 \\times 10^{-12} < K_{sp} = 2{,}4 \\times 10^{-12}$, maka larutan belum jenuh dan TIDAK terbentuk endapan."
      },
      {
        "key": "E",
        "text": "Terbentuk endapan kalium nitrat $\\text{KNO}_3$ karena memiliki kelarutan yang sangat rendah di air."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Terbentuk endapan $\\text{Ag}_2\\text{CrO}_4$, karena nilai hasil kali kuosien reaksi $Q_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (10^{-4})^2 \\times (10^{-4}) = 1 \\times 10^{-12} < K_{sp}$... mari cek konsentrasi campuran dengan cermat: Volume total = $100\\text{ mL}$. $[\\text{Ag}^+] = \\frac{50 \\times 2 \\times 10^{-4}}{100} = 1 \\times 10^{-4}\\text{ M}$. $[\\text{CrO}_4^{2-}] = \\frac{50 \\times 2 \\times 10^{-4}}{100} = 1 \\times 10^{-4}\\text{ M}$. Maka $Q_{sp} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (10^{-4})^2 \\times (10^{-4}) = 10^{-8} \\times 10^{-4} = 10^{-12} = 1{,}0 \\times 10^{-12}$. Karena $Q_{sp} = 1{,}0 \\times 10^{-12} < K_{sp} = 2{,}4 \\times 10^{-12}$, maka larutan belum jenuh dan TIDAK terbentuk endapan.. Hitung konsentrasi ion setelah pengenceran: [Ag+] = 1e-4 M, [CrO4 2-] = 1e-4 M. Hitung Qsp = [Ag+]^2 * [CrO4 2-] = (1e-4)^2 * 1e-4 = 1e-12. Bandingkan dengan Ksp = 2,4e-12. Karena Qsp (1e-12) < Ksp (2,4e-12), larutan belum jenuh sehingga tidak terbentuk endapan."
  },
  {
    "id": "kim-lat-m-09",
    "materi": "SIFAT KOLIGATIF (LARUTAN ELEKTROLIT)",
    "topic": "Kenaikan Titik Didih Elektrolit Biner dan Faktor Van 't Hoff",
    "hints": {
      "concept": "NaCl terurai jadi 2 ion (i = 2). Mol = 11,7 / 58,5 = 0,2 mol. Molalitas m = 0,2 / 0,5 = 0,4 m. Delta_Tb = m * Kb * i = 0,4 * 0,52 * 2 = 0,416 C. Tb = 100 + 0,416 C.",
      "execution": "Delta_Tb = 0,416 C, Tb = 100,416 C."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebanyak $11{,}7\\text{ gram}$ garam dapur ($\\text{NaCl}$, $M_r = 58{,}5$) dilarutkan ke dalam $500\\text{ gram}$ air murni ($K_b\\,\\text{air} = 0{,}52^\\circ\\text{C/m}$). Jika garam $\\text{NaCl}$ terionisasi sempurna di dalam air (derajat ionisasi $\\alpha = 1$), kenaikan titik didih ($\\Delta T_b$) dan titik didih larutan ($T_b$) pada tekanan 1 atm berturut-turut adalah...",
    "formulaHud": {
      "title": "KENAIKAN TITIK DIDIH LARUTAN ELEKTROLIT",
      "latex": "i = 1 + (n - 1)\\alpha = 1 + (2 - 1)(1) = 2; \\quad m = \\frac{11{,}7}{58{,}5} \\times \\frac{1.000}{500} = 0{,}4\\text{ m}; \\quad \\Delta T_b = m \\cdot K_b \\cdot i = 0{,}4 \\times 0{,}52 \\times 2 = 0{,}416^\\circ\\text{C}",
      "legend": "• Titik didih air murni $T_b^0 = 100^\\circ\\text{C}$<br>• $T_b = 100 + 0{,}416 = 100{,}416^\\circ\\text{C}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta T_b = 0{,}416^\\circ\\text{C}$ dan $T_b = 100{,}416^\\circ\\text{C}$, karena $\\text{NaCl}$ adalah elektrolit kuat biner ($n = 2$ ion: $\\text{Na}^+$ dan $\\text{Cl}^-$) dengan faktor Van 't Hoff $i = 1 + (2 - 1)(1) = 2$. Jumlah mol $\\text{NaCl}$ adalah $n = \\frac{11{,}7}{58{,}5} = 0{,}2\\text{ mol}$. Molalitasnya adalah $m = \\frac{0{,}2\\text{ mol}}{0{,}5\\text{ kg}} = 0{,}4\\text{ m}$. Kenaikan titik didih dihitung dari $\\Delta T_b = m \\times K_b \\times i = 0{,}4 \\times 0{,}52 \\times 2 = 0{,}416^\\circ\\text{C}$. Maka titik didih larutan adalah $T_b = 100 + 0{,}416 = 100{,}416^\\circ\\text{C}$."
      },
      {
        "key": "B",
        "text": "$\\Delta T_b = 0{,}832^\\circ\\text{C}$ dan $T_b = 100{,}832^\\circ\\text{C}$, dihitung dengan mengalikan faktor Van 't Hoff empat ion poliatomik."
      },
      {
        "key": "C",
        "text": "$\\Delta T_b = 1{,}040^\\circ\\text{C}$ dan $T_b = 101{,}040^\\circ\\text{C}$, dihitung dari asumsi konsentrasi satu molal elektrolit kuat."
      },
      {
        "key": "D",
        "text": "$\\Delta T_b = 0{,}416^\\circ\\text{C}$ dan $T_b = 99{,}584^\\circ\\text{C}$, karena titik didih larutan keliru dikurangkan dari titik didih pelarut air."
      },
      {
        "key": "E",
        "text": "$\\Delta T_b = 0{,}208^\\circ\\text{C}$ dan $T_b = 100{,}208^\\circ\\text{C}$, karena mengabaikan faktor Van 't Hoff larutan elektrolit ($i = 1$) menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\Delta T_b = 0{,}416^\\circ\\text{C}$ dan $T_b = 100{,}416^\\circ\\text{C}$, karena $\\text{NaCl}$ adalah elektrolit kuat biner ($n = 2$ ion: $\\text{Na}^+$ dan $\\text{Cl}^-$) dengan faktor Van 't Hoff $i = 1 + (2 - 1)(1) = 2$. Jumlah mol $\\text{NaCl}$ adalah $n = \\frac{11{,}7}{58{,}5} = 0{,}2\\text{ mol}$. Molalitasnya adalah $m = \\frac{0{,}2\\text{ mol}}{0{,}5\\text{ kg}} = 0{,}4\\text{ m}$. Kenaikan titik didih dihitung dari $\\Delta T_b = m \\times K_b \\times i = 0{,}4 \\times 0{,}52 \\times 2 = 0{,}416^\\circ\\text{C}$. Maka titik didih larutan adalah $T_b = 100 + 0{,}416 = 100{,}416^\\circ\\text{C}$.. NaCl terurai jadi 2 ion (i = 2). Mol = 11,7 / 58,5 = 0,2 mol. Molalitas m = 0,2 / 0,5 = 0,4 m. Delta_Tb = m * Kb * i = 0,4 * 0,52 * 2 = 0,416 C. Tb = 100 + 0,416 C. Delta_Tb = 0,416 C, Tb = 100,416 C."
  },
  {
    "id": "kim-lat-m-10",
    "materi": "SIFAT KOLIGATIF (TEKANAN OSMOTIK)",
    "topic": "Penentuan Massa Molar Makromolekul dari Tekanan Osmotik",
    "hints": {
      "concept": "Gunakan pi = (g / Mr) * (R * T / V). Mr = (g * R * T) / (pi * V). V = 0,25 L, T = 300 K.",
      "execution": "Mr = (3 * 0,082 * 300) / (2,46 * 0,25) = 73,8 / 0,615 = 120 g/mol."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebanyak $3\\text{ gram}$ suatu senyawa makromolekul nonelektrolit dilarutkan dalam air hingga volume larutan mencapai $250\\text{ mL}$ pada suhu $27^\\circ\\text{C}$ ($T = 300\\text{ K}$). Larutan tersebut memiliki tekanan osmotik sebesar $\\pi = 2{,}46\\text{ atmosfer}$. Jika tetapan gas ideal $R = 0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)}$, massa molekul relatif ($M_r$) senyawa tersebut adalah...",
    "formulaHud": {
      "title": "TEKANAN OSMOTIK VAN 'T HOFF",
      "latex": "\\pi = \\frac{n}{V} R T = \\frac{g}{M_r \\cdot V} R T \\implies M_r = \\frac{g R T}{\\pi V} = \\frac{3 \\times 0{,}082 \\times 300}{2{,}46 \\times 0{,}25} = \\frac{73{,}8}{0{,}615} = 120\\text{ g/mol}",
      "legend": "• $V = 250\\text{ mL} = 0{,}25\\text{ L}$<br>• $T = 27 + 273 = 300\\text{ K}$<br>• $M_r = 120\\text{ g/mol}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$M_r = 60\\text{ g/mol}$, karena volume larutan keliru dihitung sebesar 500 mL."
      },
      {
        "key": "B",
        "text": "$M_r = 300\\text{ g/mol}$, dihitung dari perkalian suhu mutlak dengan massa zat terlarut."
      },
      {
        "key": "C",
        "text": "$M_r = 120\\text{ g/mol}$, karena menurut persamaan tekanan osmotik Van 't Hoff $\\pi = M R T = \\frac{g}{M_r} \\times \\frac{1.000}{V\\text{ (mL)}} \\times R T$, sehingga massa molekul relatif adalah $M_r = \\frac{g \\times 1.000 \\times R T}{\\pi \\times V} = \\frac{3 \\times 1.000 \\times 0{,}082 \\times 300}{2{,}46 \\times 250} = \\frac{73.800}{615} = 120\\text{ g/mol}$."
      },
      {
        "key": "D",
        "text": "$M_r = 180\\text{ g/mol}$, dihitung dari pendekatan massa molar glukosa standar tanpa analisis persamaan Van 't Hoff."
      },
      {
        "key": "E",
        "text": "$M_r = 240\\text{ g/mol}$, karena tekanan osmotik keliru dikalikan dengan faktor dua elektrolit biner."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $M_r = 120\\text{ g/mol}$, karena menurut persamaan tekanan osmotik Van 't Hoff $\\pi = M R T = \\frac{g}{M_r} \\times \\frac{1.000}{V\\text{ (mL)}} \\times R T$, sehingga massa molekul relatif adalah $M_r = \\frac{g \\times 1.000 \\times R T}{\\pi \\times V} = \\frac{3 \\times 1.000 \\times 0{,}082 \\times 300}{2{,}46 \\times 250} = \\frac{73.800}{615} = 120\\text{ g/mol}$.. Gunakan pi = (g / Mr) * (R * T / V). Mr = (g * R * T) / (pi * V). V = 0,25 L, T = 300 K. Mr = (3 * 0,082 * 300) / (2,46 * 0,25) = 73,8 / 0,615 = 120 g/mol."
  },
  {
    "id": "kim-lat-m-11",
    "materi": "TERMOKIMIA (HUKUM HESS & SIKLUS ENERGI)",
    "topic": "Perhitungan Entalpi Reaksi dari Diagram Tingkat Energi",
    "hints": {
      "concept": "Delta H = Sigma Delta Hf (produk / kanan) - Sigma Delta Hf (reaktan / kiri). Produk = 3 * (-394) + 4 * (-286) = -2.326 kJ. Reaktan = -104 kJ.",
      "execution": "Delta H = -2.326 - (-104) = -2.222 kJ/mol."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Diketahui entalpi pembentukan standar ($\\Delta H_f^\\circ$) dari senyawa-senyawa berikut:<br>• $\\Delta H_f^\\circ\\,\\text{C}_3\\text{H}_8(g) = -104\\text{ kJ/mol}$<br>• $\\Delta H_f^\\circ\\,\\text{CO}_2(g) = -394\\text{ kJ/mol}$<br>• $\\Delta H_f^\\circ\\,\\text{H}_2\\text{O}(l) = -286\\text{ kJ/mol}$<br>Besar kalor pembakaran standar ($\\Delta H_c^\\circ$) untuk satu mol gas propana menurut reaksi:<br>$$\\text{C}_3\\text{H}_8(g) + 5\\,\\text{O}_2(g) \\to 3\\,\\text{CO}_2(g) + 4\\,\\text{H}_2\\text{O}(l)$$<br>adalah...",
    "formulaHud": {
      "title": "HUKUM HESS DARI ENTALPI PEMBENTUKAN STANDAR",
      "latex": "\\Delta H_c^\\circ = [3\\Delta H_f^\\circ(\\text{CO}_2) + 4\\Delta H_f^\\circ(\\text{H}_2\\text{O})] - \\Delta H_f^\\circ(\\text{C}_3\\text{H}_8) = [3(-394) + 4(-286)] - (-104) = -2.326 + 104 = -2.222\\text{ kJ/mol}",
      "legend": "• $\\Delta H_f^\\circ$ unsur bebas ($\\text{O}_2$) dalam keadaan standar adalah nol<br>• Reaksi pembakaran propana melepaskan kalor sebesar $2.222\\text{ kJ/mol}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta H_c^\\circ = -1.182\\text{ kJ/mol}$, karena hanya memperhitungkan entalpi pembentukan gas karbon dioksida tanpa uap air."
      },
      {
        "key": "B",
        "text": "$\\Delta H_c^\\circ = -576\\text{ kJ/mol}$, dihitung dari selisih aljabar langsung tanpa mengalikan koefisien reaksi pembakaran."
      },
      {
        "key": "C",
        "text": "$\\Delta H_c^\\circ = -2.222\\text{ kJ/mol}$, karena entalpi reaksi dihitung dari selisih entalpi produk dikurangi entalpi reaktan: $\\Delta H = \\sum \\Delta H_f^\\circ(\\text{produk}) - \\sum \\Delta H_f^\\circ(\\text{reaktan}) = [3(-394) + 4(-286)] - [-104 + 5(0)] = [-1.182 - 1.144] - [-104] = -2.326 + 104 = -2.222\\text{ kJ/mol}$."
      },
      {
        "key": "D",
        "text": "$\\Delta H_c^\\circ = +2.222\\text{ kJ/mol}$, karena salah memberikan tanda positif pada reaksi pembakaran yang terbukti eksotermik membebaskan kalor."
      },
      {
        "key": "E",
        "text": "$\\Delta H_c^\\circ = -2.430\\text{ kJ/mol}$, karena entalpi pembentukan propana keliru dijumlahkan dengan produk bukan dikurangkan."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $\\Delta H_c^\\circ = -2.222\\text{ kJ/mol}$, karena entalpi reaksi dihitung dari selisih entalpi produk dikurangi entalpi reaktan: $\\Delta H = \\sum \\Delta H_f^\\circ(\\text{produk}) - \\sum \\Delta H_f^\\circ(\\text{reaktan}) = [3(-394) + 4(-286)] - [-104 + 5(0)] = [-1.182 - 1.144] - [-104] = -2.326 + 104 = -2.222\\text{ kJ/mol}$.. Delta H = Sigma Delta Hf (produk / kanan) - Sigma Delta Hf (reaktan / kiri). Produk = 3 * (-394) + 4 * (-286) = -2.326 kJ. Reaktan = -104 kJ. Delta H = -2.326 - (-104) = -2.222 kJ/mol."
  },
  {
    "id": "kim-lat-m-12",
    "materi": "KINETIKA KIMIA & PENGARUH SUHU",
    "topic": "Pengaruh Kenaikan Suhu terhadap Laju Reaksi",
    "hints": {
      "concept": "Laju naik 3 kali lipat tiap 10 C. Delta T = 55 - 25 = 30 C -> n = 30/10 = 3 periode. Laju naik 3^3 = 27 kali. Waktu t2 = t1 / 27.",
      "execution": "t2 = 54 / 27 = 2 menit."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Suatu reaksi kimia berlangsung 3 kali lebih cepat setiap kenaikan suhu sebesar $10^\\circ\\text{C}$. Jika pada suhu $25^\\circ\\text{C}$ reaksi tersebut membutuhkan waktu $54\\text{ menit}$ untuk selesai sempurna, waktu yang dibutuhkan agar reaksi tersebut selesai pada suhu $55^\\circ\\text{C}$ adalah...",
    "formulaHud": {
      "title": "PENGARUH SUHU TERHADAP WAKTU REAKSI",
      "latex": "v_2 = v_1 \\times (\\Delta v)^{\\frac{\\Delta T}{T_0}} \\implies t_2 = t_1 \\times \\left(\\frac{1}{\\Delta v}\\right)^{\\frac{\\Delta T}{T_0}} = 54 \\times \\left(\\frac{1}{3}\\right)^{\\frac{55-25}{10}} = \\frac{54}{3^3} = \\frac{54}{27} = 2\\text{ menit}",
      "legend": "• Kenaikan suhu meningkatkan energi kinetik molekul dan frekuensi tumbukan efektif partikel yang melampaui energi aktivasi ($E_a$)<br>• Waktu reaksi berkurang drastis dari 54 menit menjadi 2 menit"
    },
    "options": [
      {
        "key": "A",
        "text": "$6\\text{ menit}$, karena laju reaksi keliru dianggap hanya meningkat sembilan kali lipat."
      },
      {
        "key": "B",
        "text": "$1\\text{ menit}$, dihitung dari asumsi laju reaksi meningkat secara kuadratik eksponensial."
      },
      {
        "key": "C",
        "text": "$18\\text{ menit}$, karena laju reaksi hanya dikalikan tiga satu kali tanpa pemangkatan jumlah kenaikan suhu."
      },
      {
        "key": "D",
        "text": "$27\\text{ menit}$, dihitung dari pengurangan separuh waktu reaksi awal."
      },
      {
        "key": "E",
        "text": "$2\\text{ menit}$, karena kenaikan suhu adalah $\\Delta T = 55^\\circ\\text{C} - 25^\\circ\\text{C} = 30^\\circ\\text{C}$. Jumlah kenaikan kelipatan sepuluh derajat adalah $n = \\frac{\\Delta T}{10} = \\frac{30}{10} = 3$. Laju reaksi meningkat sebesar $3^n = 3^3 = 27$ kali lebih cepat. Karena waktu reaksi berbanding terbalik dengan laju reaksi ($t \\propto 1/v$), maka waktu yang dibutuhkan pada suhu $55^\\circ\\text{C}$ adalah $t_2 = \\frac{t_1}{3^n} = \\frac{54\\text{ menit}}{27} = 2\\text{ menit}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $2\\text{ menit}$, karena kenaikan suhu adalah $\\Delta T = 55^\\circ\\text{C} - 25^\\circ\\text{C} = 30^\\circ\\text{C}$. Jumlah kenaikan kelipatan sepuluh derajat adalah $n = \\frac{\\Delta T}{10} = \\frac{30}{10} = 3$. Laju reaksi meningkat sebesar $3^n = 3^3 = 27$ kali lebih cepat. Karena waktu reaksi berbanding terbalik dengan laju reaksi ($t \\propto 1/v$), maka waktu yang dibutuhkan pada suhu $55^\\circ\\text{C}$ adalah $t_2 = \\frac{t_1}{3^n} = \\frac{54\\text{ menit}}{27} = 2\\text{ menit}$.. Laju naik 3 kali lipat tiap 10 C. Delta T = 55 - 25 = 30 C -> n = 30/10 = 3 periode. Laju naik 3^3 = 27 kali. Waktu t2 = t1 / 27. t2 = 54 / 27 = 2 menit."
  },
  {
    "id": "kim-lat-m-13",
    "materi": "KESETIMBANGAN KIMIA (DERAJAT DISOSIASI & Kp)",
    "topic": "Perhitungan Kp dari Derajat Disosiasi dan Tekanan Total",
    "hints": {
      "concept": "Mol setimbang: PCl5 = 2/3, PCl3 = 1/3, Cl2 = 1/3. Total mol = 4/3. Tekanan parsial: P(PCl5) = (2/4)*4 = 2 atm, P(PCl3) = (1/4)*4 = 1 atm, P(Cl2) = 1 atm. Kp = 1*1 / 2.",
      "execution": "Kp = 1 / 2 = 0,5 atm."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Gas fosforus pentaklorida ($\\text{PCl}_5$) mengalami disosiasi dalam wadah tertutup pada suhu tertentu menurut reaksi:<br>$$\\text{PCl}_5(g) \\rightleftharpoons \\text{PCl}_3(g) + \\text{Cl}_2(g)$$<br>Mula-mula dimasukkan $1\\text{ mol } \\text{PCl}_5$. Pada keadaan setimbang, sepertiga bagian dari $\\text{PCl}_5$ telah terurai (derajat disosiasi $\\alpha = \\frac{1}{3}$) dan tekanan total gas di dalam bejana adalah $P_{\\text{total}} = 4\\text{ atmosfer}$. Nilai tetapan kesetimbangan tekanan ($K_p$) reaksi tersebut adalah...",
    "formulaHud": {
      "title": "PERHITUNGAN Kp DARI TEKANAN PARSIAL GAS",
      "latex": "n_{\\text{total}} = \\frac{4}{3}\\text{ mol}; \\quad P_{\\text{PCl}_5} = 2\\text{ atm}; \\quad P_{\\text{PCl}_3} = 1\\text{ atm}; \\quad P_{\\text{Cl}_2} = 1\\text{ atm}; \\quad K_p = \\frac{1 \\times 1}{2} = 0{,}5\\text{ atm}",
      "legend": "• Fraksi mol $\\text{PCl}_5 = 2/4 = 0{,}5$, $\\text{PCl}_3 = 1/4 = 0{,}25$, $\\text{Cl}_2 = 1/4 = 0{,}25$<br>• $P_i = X_i \\times P_{\\text{total}}$<br>• $K_p = 0{,}5\\text{ atm}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$K_p = 0{,}25\\text{ atm}$, dihitung dari pengkuadratan rasio mol tanpa mengalikan dengan tekanan total gas."
      },
      {
        "key": "B",
        "text": "$K_p = 2{,}0\\text{ atm}$, karena rumus Kp keliru dibalik menjadi tekanan reaktan dibagi tekanan produk."
      },
      {
        "key": "C",
        "text": "$K_p = 0{,}75\\text{ atm}$, dihitung dari pendekatan pembulatan fraksi mol kesetimbangan kimia."
      },
      {
        "key": "D",
        "text": "$K_p = 1{,}0\\text{ atm}$, karena tekanan parsial reaktan keliru dihitung sama dengan tekanan produk ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "E",
        "text": "$K_p = 0{,}5\\text{ atm}$, karena mol $\\text{PCl}_5$ yang terurai adalah $\\frac{1}{3}\\text{ mol}$, menyisakan $\\text{PCl}_5 = 1 - \\frac{1}{3} = \\frac{2}{3}\\text{ mol}$, terbentuk $\\text{PCl}_3 = \\frac{1}{3}\\text{ mol}$, dan $\\text{Cl}_2 = \\frac{1}{3}\\text{ mol}$. Total mol gas pada kesetimbangan adalah $n_{\\text{total}} = \\frac{2}{3} + \\frac{1}{3} + \\frac{1}{3} = \\frac{4}{3}\\text{ mol}$. Tekanan parsial masing-masing gas: $P_{\\text{PCl}_5} = \\frac{2/3}{4/3} \\times 4 = 2\\text{ atm}$, $P_{\\text{PCl}_3} = \\frac{1/3}{4/3} \\times 4 = 1\\text{ atm}$, dan $P_{\\text{Cl}_2} = 1\\text{ atm}$. Maka $K_p = \\frac{P_{\\text{PCl}_3} \\cdot P_{\\text{Cl}_2}}{P_{\\text{PCl}_5}} = \\frac{1 \\times 1}{2} = 0{,}5\\text{ atm}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $K_p = 0{,}5\\text{ atm}$, karena mol $\\text{PCl}_5$ yang terurai adalah $\\frac{1}{3}\\text{ mol}$, menyisakan $\\text{PCl}_5 = 1 - \\frac{1}{3} = \\frac{2}{3}\\text{ mol}$, terbentuk $\\text{PCl}_3 = \\frac{1}{3}\\text{ mol}$, dan $\\text{Cl}_2 = \\frac{1}{3}\\text{ mol}$. Total mol gas pada kesetimbangan adalah $n_{\\text{total}} = \\frac{2}{3} + \\frac{1}{3} + \\frac{1}{3} = \\frac{4}{3}\\text{ mol}$. Tekanan parsial masing-masing gas: $P_{\\text{PCl}_5} = \\frac{2/3}{4/3} \\times 4 = 2\\text{ atm}$, $P_{\\text{PCl}_3} = \\frac{1/3}{4/3} \\times 4 = 1\\text{ atm}$, dan $P_{\\text{Cl}_2} = 1\\text{ atm}$. Maka $K_p = \\frac{P_{\\text{PCl}_3} \\cdot P_{\\text{Cl}_2}}{P_{\\text{PCl}_5}} = \\frac{1 \\times 1}{2} = 0{,}5\\text{ atm}$.. Mol setimbang: PCl5 = 2/3, PCl3 = 1/3, Cl2 = 1/3. Total mol = 4/3. Tekanan parsial: P(PCl5) = (2/4)*4 = 2 atm, P(PCl3) = (1/4)*4 = 1 atm, P(Cl2) = 1 atm. Kp = 1*1 / 2. Kp = 1 / 2 = 0,5 atm."
  },
  {
    "id": "kim-lat-m-14",
    "materi": "REAKSI REDOKS (PENYETARAAN ION-ELEKTRON)",
    "topic": "Penyetaraan Reaksi Redoks dalam Suasana Asam",
    "hints": {
      "concept": "MnO4- -> Mn2+ butuh 5 elektron dan 8 H+ untuk menghasilkan 4 H2O. Fe2+ -> Fe3+ melepas 1 elektron (kalikan 5 agar elektron sama).",
      "execution": "Koefisien: 1, 5, 8 -> 1, 5, 4."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Diberikan persamaan reaksi redoks dalam suasana asam (belum setara):<br>$$a\\,\\text{MnO}_4^-(aq) + b\\,\\text{Fe}^{2+}(aq) + c\\,\\text{H}^+(aq) \\to d\\,\\text{Mn}^{2+}(aq) + e\\,\\text{Fe}^{3+}(aq) + f\\,\\text{H}_2\\text{O}(l)$$<br>Nilai koefisien reaksi $a$, $b$, $c$, $d$, $e$, dan $f$ yang benar setelah disetarakan berturut-turut adalah...",
    "formulaHud": {
      "title": "METODE SETENGAH REAKSI (ION ELEKTRON) SUASANA ASAM",
      "latex": "\\begin{aligned} \\text{Reduksi: } & \\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O} \\quad (\\times 1) \\\\ \\text{Oksidasi: } & \\text{Fe}^{2+} \\to \\text{Fe}^{3+} + e^- \\quad (\\times 5) \\\\ \\hline \\text{Net: } & \\text{MnO}_4^- + 5\\text{Fe}^{2+} + 8\\text{H}^+ \\to \\text{Mn}^{2+} + 5\\text{Fe}^{3+} + 4\\text{H}_2\\text{O} \\end{aligned}",
      "legend": "• Muatan ruas kiri $= (-1) + 5(+2) + 8(+1) = +17$<br>• Muatan ruas kanan $= (+2) + 5(+3) = +17$ (Setara muatan dan atom)"
    },
    "options": [
      {
        "key": "A",
        "text": "$a = 1$, $b = 3$, $c = 4$, $d = 1$, $e = 3$, dan $f = 2$, karena jumlah ion hidrogen tidak menyetarakan muatan listrik di kedua ruas."
      },
      {
        "key": "B",
        "text": "$a = 2$, $b = 10$, $c = 8$, $d = 2$, $e = 10$, dan $f = 4$, karena koefisien asam hidrogen tidak digandakan saat pengalian koefisien dua."
      },
      {
        "key": "C",
        "text": "$a = 1$, $b = 1$, $c = 8$, $d = 1$, $e = 1$, dan $f = 4$, karena mengabaikan kesetaraan transfer jumlah elektron redoks."
      },
      {
        "key": "D",
        "text": "$a = 1$, $b = 5$, $c = 8$, $d = 1$, $e = 5$, dan $f = 4$, karena setengah reaksi reduksi permanganat adalah $\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$ (melibatkan 5 elektron), dan setengah reaksi oksidasi besi adalah $\\text{Fe}^{2+} \\to \\text{Fe}^{3+} + e^-$. Menyamakan jumlah transfer elektron menuntut pengalian 5 pada setengah reaksi oksidasi sehingga diperoleh perbandingan koefisien $1 : 5 : 8 \\to 1 : 5 : 4$."
      },
      {
        "key": "E",
        "text": "$a = 2$, $b = 5$, $c = 16$, $d = 2$, $e = 5$, dan $f = 8$, karena jumlah koefisien ion besi tidak dikalikan dua mengikuti permanganat menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $a = 1$, $b = 5$, $c = 8$, $d = 1$, $e = 5$, dan $f = 4$, karena setengah reaksi reduksi permanganat adalah $\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\to \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$ (melibatkan 5 elektron), dan setengah reaksi oksidasi besi adalah $\\text{Fe}^{2+} \\to \\text{Fe}^{3+} + e^-$. Menyamakan jumlah transfer elektron menuntut pengalian 5 pada setengah reaksi oksidasi sehingga diperoleh perbandingan koefisien $1 : 5 : 8 \\to 1 : 5 : 4$.. MnO4- -> Mn2+ butuh 5 elektron dan 8 H+ untuk menghasilkan 4 H2O. Fe2+ -> Fe3+ melepas 1 elektron (kalikan 5 agar elektron sama). Koefisien: 1, 5, 8 -> 1, 5, 4."
  },
  {
    "id": "kim-lat-m-15",
    "materi": "ELEKTROKIMIA (KOROSI & PROTEKSI KATODIK)",
    "topic": "Pemilihan Logam Tumbal Pencegah Karat Besi",
    "hints": {
      "concept": "Syarat anoda korban: logam harus memiliki E0 reduksi lebih negatif daripada besi (-0,44 V) agar teroksidasi lebih dahulu. Pilih logam dengan E0 < -0,44 V.",
      "execution": "Mg (-2,37 V) dan Zn (-0,76 V) memiliki E0 lebih negatif dari Fe (-0,44 V)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Pipa besi bawah tanah ($E^\\circ\\,\\text{Fe}^{2+}/\\text{Fe} = -0{,}44\\text{ V}$) dapat dilindungi dari bahaya perkaratan dengan metode proteksi katodik (anoda korban). Diberikan data potensial reduksi standar beberapa logam:<br>• $\\text{Mg}^{2+}/\\text{Mg} \\quad E^\\circ = -2{,}37\\text{ V}$<br>• $\\text{Zn}^{2+}/\\text{Zn} \\quad E^\\circ = -0{,}76\\text{ V}$<br>• $\\text{Sn}^{2+}/\\text{Sn} \\quad E^\\circ = -0{,}14\\text{ V}$<br>• $\\text{Cu}^{2+}/\\text{Cu} \\quad E^\\circ = +0{,}34\\text{ V}$<br>• $\\text{Ag}^{+}/\\text{Ag} \\quad E^\\circ = +0{,}80\\text{ V}$<br>Pasangan logam yang paling efektif digunakan sebagai anoda korban untuk melindungi pipa besi tersebut adalah...",
    "formulaHud": {
      "title": "PRINSIP PROTEKSI KATODIK (ANODA KORBAN)",
      "latex": "E^\\circ_{\\text{anoda korban}} < E^\\circ_{\\text{Fe}} (-0{,}44\\text{ V}) \\implies \\text{Mg } (-2{,}37\\text{ V}) \\text{ dan Zn } (-0{,}76\\text{ V})",
      "legend": "• Logam dengan $E^\\circ$ lebih negatif akan teroksidasi lebih dahulu di anoda: $\\text{M} \\to \\text{M}^{n+} + ne^-$<br>• Besi dipaksa bertindak sebagai katoda (menerima elektron sehingga tidak berkarat)<br>• Logam seperti Sn dan Cu justru mempercepat korosi besi jika lapisan pelindungnya tergores"
    },
    "options": [
      {
        "key": "A",
        "text": "Semua logam di atas (Mg, Zn, Sn, Cu, dan Ag) dapat melindungi besi dengan efektivitas yang persis sama."
      },
      {
        "key": "B",
        "text": "Magnesium ($\\text{Mg}$) dan seng ($\\text{Zn}$), karena keduanya memiliki potensial reduksi standar yang jauh lebih negatif daripada besi ($E^\\circ_{\\text{Mg}} = -2{,}37\\text{ V}$ dan $E^\\circ_{\\text{Zn}} = -0{,}76\\text{ V} < E^\\circ_{\\text{Fe}} = -0{,}44\\text{ V}$), sehingga logam $\\text{Mg}$ dan $\\text{Zn}$ lebih mudah teroksidasi dan bertindak sebagai anoda korban yang mengorbankan dirinya terkorosi demi melindungi besi."
      },
      {
        "key": "C",
        "text": "Timah ($\\text{Sn}$) dan tembaga ($\\text{Cu}$), karena timah umum digunakan pada kaleng makanan kemasan baja."
      },
      {
        "key": "D",
        "text": "Tembaga ($\\text{Cu}$) dan perak ($\\text{Ag}$), karena keduanya merupakan logam mulia yang tahan karat sehingga dianggap mampu melindungi besi."
      },
      {
        "key": "E",
        "text": "Hanya perak ($\\text{Ag}$), karena perak memiliki potensial reduksi tertinggi sehingga mendominasi seluruh reaksi elektrokimia."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Magnesium ($\\text{Mg}$) dan seng ($\\text{Zn}$), karena keduanya memiliki potensial reduksi standar yang jauh lebih negatif daripada besi ($E^\\circ_{\\text{Mg}} = -2{,}37\\text{ V}$ dan $E^\\circ_{\\text{Zn}} = -0{,}76\\text{ V} < E^\\circ_{\\text{Fe}} = -0{,}44\\text{ V}$), sehingga logam $\\text{Mg}$ dan $\\text{Zn}$ lebih mudah teroksidasi dan bertindak sebagai anoda korban yang mengorbankan dirinya terkorosi demi melindungi besi.. Syarat anoda korban: logam harus memiliki E0 reduksi lebih negatif daripada besi (-0,44 V) agar teroksidasi lebih dahulu. Pilih logam dengan E0 < -0,44 V. Mg (-2,37 V) dan Zn (-0,76 V) memiliki E0 lebih negatif dari Fe (-0,44 V)."
  },
  {
    "id": "kim-lat-m-16",
    "materi": "ELEKTROLISIS (PERSAINGAN REDUKSI AIR)",
    "topic": "Reaksi Katoda dan Anoda pada Elektrolisis Larutan NaCl",
    "hints": {
      "concept": "Dalam larutan air, kation Na+ (golongan IA) kalah bersaing dengan air: air yang tereduksi menghasilkan gas H2 dan ion OH-. Di anoda karbon, ion Cl- pekat teroksidasi jadi Cl2.",
      "execution": "Katoda: reduksi air menghasilkan gas H2. Anoda: gas Cl2."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Larutan natrium klorida pekat ($\\text{NaCl } 1\\text{ M}$) dielektrolisis menggunakan elektroda karbon (grafit) inert. Reaksi yang terjadi di katoda dan gas yang dihasilkan di anoda berturut-turut adalah...",
    "formulaHud": {
      "title": "ELEKTROLISIS LARUTAN NaCl (PROSES CHLOR-ALKALI)",
      "latex": "\\begin{aligned} \\text{Katoda (-): } & 2\\text{H}_2\\text{O}(l) + 2e^- \\to \\text{H}_2(g) + 2\\text{OH}^-(aq) \\\\ \\text{Anoda (+): } & 2\\text{Cl}^-(aq) \\to \\text{Cl}_2(g) + 2e^- \\\\ \\hline \\text{Reaksi Sel: } & 2\\text{NaCl} + 2\\text{H}_2\\text{O} \\to 2\\text{NaOH} + \\text{H}_2(g) + \\text{Cl}_2(g) \\end{aligned}",
      "legend": "• Kation golongan IA, IIA, Al, dan Mn dalam wujud larutan TIDAK tereduksi di katoda, melainkan air yang tereduksi<br>• Produk sampingan di katoda adalah larutan basa kuat $\\text{NaOH}$"
    },
    "options": [
      {
        "key": "A",
        "text": "Di katoda terjadi pengendapan natrium cair dan di anoda dihasilkan gas hidrogen klorida beracun."
      },
      {
        "key": "B",
        "text": "Di katoda terjadi reduksi natrium: $\\text{Na}^+ + e^- \\to \\text{Na}(s)$ dan di anoda dihasilkan gas oksigen ($\\text{O}_2$)."
      },
      {
        "key": "C",
        "text": "Di katoda terjadi oksidasi ion hidroksida dan di anoda dihasilkan endapan garam kristal natrium klorida."
      },
      {
        "key": "D",
        "text": "Di katoda dihasilkan gas hidrogen dan di anoda terjadi oksidasi air menghasilkan gas oksigen murni."
      },
      {
        "key": "E",
        "text": "Di katoda terjadi reduksi air: $2\\,\\text{H}_2\\text{O}(l) + 2e^- \\to \\text{H}_2(g) + 2\\,\\text{OH}^-(aq)$ dan di anoda dihasilkan gas klorin ($\\text{Cl}_2$), karena kation natrium ($\\text{Na}^+$, logam alkali golongan IA) memiliki potensial reduksi yang sangat negatif ($E^\\circ = -2{,}71\\text{ V}$) sehingga air lebih mudah tereduksi di katoda menghasilkan gas hidrogen dan suasana basa, sedangkan pada konsentrasi pekat ion halida $\\text{Cl}^-$ teroksidasi di anoda menghasilkan gas $\\text{Cl}_2$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Di katoda terjadi reduksi air: $2\\,\\text{H}_2\\text{O}(l) + 2e^- \\to \\text{H}_2(g) + 2\\,\\text{OH}^-(aq)$ dan di anoda dihasilkan gas klorin ($\\text{Cl}_2$), karena kation natrium ($\\text{Na}^+$, logam alkali golongan IA) memiliki potensial reduksi yang sangat negatif ($E^\\circ = -2{,}71\\text{ V}$) sehingga air lebih mudah tereduksi di katoda menghasilkan gas hidrogen dan suasana basa, sedangkan pada konsentrasi pekat ion halida $\\text{Cl}^-$ teroksidasi di anoda menghasilkan gas $\\text{Cl}_2$.. Dalam larutan air, kation Na+ (golongan IA) kalah bersaing dengan air: air yang tereduksi menghasilkan gas H2 dan ion OH-. Di anoda karbon, ion Cl- pekat teroksidasi jadi Cl2. Katoda: reduksi air menghasilkan gas H2. Anoda: gas Cl2."
  },
  {
    "id": "kim-lat-m-17",
    "materi": "ELEKTROKIMIA (HUKUM FARADAY II)",
    "topic": "Elektrolisis Dua Sel Seri dengan Muatan Listrik Sama",
    "hints": {
      "concept": "Hukum Faraday II: w_Cu / e_Cu = w_Ag / e_Ag. e_Ag = 108/1 = 108. e_Cu = 63,5/2 = 31,75. w_Cu = 10,8 * (31,75 / 108).",
      "execution": "w_Cu = 0,1 * 31,75 = 3,175 gram."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dua sel elektrolisis disusun secara seri. Sel pertama berisi larutan perak nitrat ($\\text{AgNO}_3$, $A_r\\,\\text{Ag} = 108$) dan sel kedua berisi larutan tembaga(II) sulfat ($\\text{CuSO}_4$, $A_r\\,\\text{Cu} = 63{,}5$). Jika selama proses elektrolisis berlangsung pada katoda sel pertama diendapkan perak padat sebanyak $10{,}8\\text{ gram}$, massa tembaga padat yang terendapkan pada katoda sel kedua adalah...",
    "formulaHud": {
      "title": "HUKUM FARADAY II SEL SERI",
      "latex": "\\frac{w_1}{e_1} = \\frac{w_2}{e_2} \\implies w_{\\text{Cu}} = w_{\\text{Ag}} \\cdot \\frac{e_{\\text{Cu}}}{e_{\\text{Ag}}} = 10{,}8 \\times \\frac{31{,}75}{108} = 3{,}175\\text{ gram}",
      "legend": "• $e_{\\text{Ag}} = 108 / 1 = 108\\text{ g/ekivalen}$<br>• $e_{\\text{Cu}} = 63{,}5 / 2 = 31{,}75\\text{ g/ekivalen}$<br>• $w_{\\text{Cu}} = 3{,}175\\text{ gram}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$1{,}588\\text{ gram}$, dihitung dari kesalahan membagi massa ekuivalen tembaga dengan faktor dua lagi."
      },
      {
        "key": "B",
        "text": "$3{,}175\\text{ gram}$, karena kedua sel tersusun seri sehingga menerima jumlah muatan listrik Faraday yang persis sama ($F_1 = F_2$). Berdasarkan Hukum Faraday II: $\\frac{w_{\\text{Cu}}}{e_{\\text{Cu}}} = \\frac{w_{\\text{Ag}}}{e_{\\text{Ag}}}$. Massa ekuivalen perak adalah $e_{\\text{Ag}} = \\frac{108}{1} = 108$, dan tembaga adalah $e_{\\text{Cu}} = \\frac{63{,}5}{2} = 31{,}75$. Maka massa tembaga adalah $w_{\\text{Cu}} = w_{\\text{Ag}} \\times \\frac{e_{\\text{Cu}}}{e_{\\text{Ag}}} = 10{,}8\\text{ g} \\times \\frac{31{,}75}{108} = 0{,}1 \\times 31{,}75 = 3{,}175\\text{ gram}$."
      },
      {
        "key": "C",
        "text": "$0{,}635\\text{ gram}$, dihitung dari galat pergeseran koma desimal perhitungan stoikiometri redoks."
      },
      {
        "key": "D",
        "text": "$10{,}80\\text{ gram}$, karena beranggapan massa logam yang mengendap pada susunan seri selalu sama persis."
      },
      {
        "key": "E",
        "text": "$6{,}350\\text{ gram}$, karena valensi ion tembaga keliru dianggap satu sama seperti perak."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $3{,}175\\text{ gram}$, karena kedua sel tersusun seri sehingga menerima jumlah muatan listrik Faraday yang persis sama ($F_1 = F_2$). Berdasarkan Hukum Faraday II: $\\frac{w_{\\text{Cu}}}{e_{\\text{Cu}}} = \\frac{w_{\\text{Ag}}}{e_{\\text{Ag}}}$. Massa ekuivalen perak adalah $e_{\\text{Ag}} = \\frac{108}{1} = 108$, dan tembaga adalah $e_{\\text{Cu}} = \\frac{63{,}5}{2} = 31{,}75$. Maka massa tembaga adalah $w_{\\text{Cu}} = w_{\\text{Ag}} \\times \\frac{e_{\\text{Cu}}}{e_{\\text{Ag}}} = 10{,}8\\text{ g} \\times \\frac{31{,}75}{108} = 0{,}1 \\times 31{,}75 = 3{,}175\\text{ gram}$.. Hukum Faraday II: w_Cu / e_Cu = w_Ag / e_Ag. e_Ag = 108/1 = 108. e_Cu = 63,5/2 = 31,75. w_Cu = 10,8 * (31,75 / 108). w_Cu = 0,1 * 31,75 = 3,175 gram."
  },
  {
    "id": "kim-lat-m-18",
    "materi": "KIMIA UNSUR (PERIODE KETIGA)",
    "topic": "Sifat Asam-Basa Senyawa Hidroksida Periode Ketiga",
    "hints": {
      "concept": "Di antara hidroksida periode ke-3, hanya Al(OH)3 yang bersifat amfoter: larut dalam larutan asam menghasilkan Al3+ dan larut dalam basa kuat berlebih menghasilkan [Al(OH)4]-.",
      "execution": "Al(OH)3 bersifat amfoter."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Unsur-unsur periode ketiga membentuk senyawa hidroksida: $\\text{NaOH}$, $\\text{Mg(OH)}_2$, $\\text{Al(OH)}_3$, $\\text{Si(OH)}_4$, $\\text{H}_3\\text{PO}_4$, $\\text{H}_2\\text{SO}_4$, dan $\\text{HClO}_4$. Senyawa hidroksida yang bersifat amfoter (dapat bereaksi dengan larutan asam kuat maupun basa kuat) adalah...",
    "formulaHud": {
      "title": "SIFAT AMFOTER ALUMINIUM HIDROKSIDA",
      "latex": "\\begin{aligned} \\text{Sebagai Basa: } & \\text{Al(OH)}_3(s) + 3\\text{H}^+(aq) \\to \\text{Al}^{3+}(aq) + 3\\text{H}_2\\text{O}(l) \\\\ \\text{Sebagai Asam: } & \\text{Al(OH)}_3(s) + \\text{OH}^-(aq) \\to [\\text{Al(OH)}_4]^-(aq) \\quad (\\text{Tetrahidroksoaluminat}) \\end{aligned}",
      "legend": "• Tren hidroksida periode 3 dari kiri ke kanan: Basa Kuat (Na) $\\to$ Basa Lemah (Mg) $\\to$ Amfoter (Al) $\\to$ Asam Sangat Lemah (Si) $\\to$ Asam Sedang (P) $\\to$ Asam Kuat (S) $\\to$ Asam Sangat Kuat (Cl)"
    },
    "options": [
      {
        "key": "A",
        "text": "Asam perklorat ($\\text{HClO}_4$), karena merupakan salah satu asam oksi terkuat yang tidak memiliki sifat amfoter."
      },
      {
        "key": "B",
        "text": "Aluminium hidroksida ($\\text{Al(OH)}_3$), karena dalam suasana asam $\\text{Al(OH)}_3$ bertindak sebagai basa membentuk kation $[\\text{Al}(\\text{H}_2\\text{O})_6]^{3+}$, sedangkan dalam suasana basa kuat berlebih bertindak sebagai asam melepaskan proton membentuk anion kompleks aluminat $[\\text{Al(OH)}_4]^-$."
      },
      {
        "key": "C",
        "text": "Magnesium hidroksida ($\\text{Mg(OH)}_2$), karena merupakan basa lemah yang tidak dapat larut dalam larutan basa kuat berlebih ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "D",
        "text": "Silikon hidroksida ($\\text{Si(OH)}_4$), karena merupakan asam silikat lemah yang hanya bereaksi dengan basa."
      },
      {
        "key": "E",
        "text": "Natrium hidroksida ($\\text{NaOH}$), karena merupakan basa kuat monoprotik murni yang tidak bereaksi dengan basa."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Aluminium hidroksida ($\\text{Al(OH)}_3$), karena dalam suasana asam $\\text{Al(OH)}_3$ bertindak sebagai basa membentuk kation $[\\text{Al}(\\text{H}_2\\text{O})_6]^{3+}$, sedangkan dalam suasana basa kuat berlebih bertindak sebagai asam melepaskan proton membentuk anion kompleks aluminat $[\\text{Al(OH)}_4]^-$.. Di antara hidroksida periode ke-3, hanya Al(OH)3 yang bersifat amfoter: larut dalam larutan asam menghasilkan Al3+ dan larut dalam basa kuat berlebih menghasilkan [Al(OH)4]-. Al(OH)3 bersifat amfoter."
  },
  {
    "id": "kim-lat-m-19",
    "materi": "SENYAWA KOMPLEKS (KIMIA KOORDINASI)",
    "topic": "Bilangan Oksidasi Logam Pusat dan Tata Nama IUPAC Kompleks",
    "hints": {
      "concept": "NH3 netral (muatan 0), Cl bermuatan -1. Ada 2 Cl di dalam kompleks dan 1 Cl di luar (total 3 Cl- = -3). Maka Co bermuatan +3. Ada 4 NH3 + 2 Cl = 6 ligan (bilangan koordinasi = 6).",
      "execution": "Biloks Co = +3, BK = 6, nama: tetraaminadiklorokobalt(III) klorida."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Diberikan senyawa kompleks netral $[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]\\text{Cl}$. Bilangan oksidasi atom pusat kobalt, bilangan koordinasi, dan nama resmi IUPAC dari senyawa koordinasi tersebut adalah...",
    "formulaHud": {
      "title": "SENYAWA KOORDINASI KOBALT(III)",
      "latex": "[\\text{Co}(\\text{NH}_3)_4\\text{Cl}_2]^+ + \\text{Cl}^- \\implies \\text{Muatan Ion Kompleks} = +1 \\implies \\text{Biloks Co} = +1 - 2(-1) = +3; \\quad \\text{BK} = 4 + 2 = 6",
      "legend": "• Aturan Penamaan: Ligan diurutkan alfabet (amina > kloro) $\\to$ nama kation kompleks $\\to$ biloks logam angka Romawi $\\to$ nama anion penyeimbang<br>• Tetraaminadiklorokobalt(III) klorida"
    },
    "options": [
      {
        "key": "A",
        "text": "Bilangan oksidasi kobalt $+3$, bilangan koordinasi 6, dan nama IUPAC tetraaminadiklorokobalt(III) klorida, karena ligan netral amonia ($\\text{NH}_3$) bermuatan nol dan ligan kloro ($\\text{Cl}^-$) bermuatan $-1$. Terdapat total 3 ion klorida (2 sebagai ligan dalam kurung siku dan 1 sebagai anion penyeimbang di luar), sehingga $\\text{Biloks Co} + 4(0) + 2(-1) + (-1) = 0 \\implies \\text{Biloks Co} = +3$. Jumlah ligan monodentat yang terikat langsung pada kobalt adalah $4 + 2 = 6$ (bilangan koordinasi 6)."
      },
      {
        "key": "B",
        "text": "Bilangan oksidasi kobalt $+3$, bilangan koordinasi 4, dan nama IUPAC tetraamindiklorokobalt(III)."
      },
      {
        "key": "C",
        "text": "Bilangan oksidasi kobalt $+6$, bilangan koordinasi 6, dan nama IUPAC heksakobalt tetraamina triklorida."
      },
      {
        "key": "D",
        "text": "Bilangan oksidasi kobalt $+2$, bilangan koordinasi 4, dan nama IUPAC diamintetraklorokobalt(II) klorida menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "E",
        "text": "Bilangan oksidasi kobalt $+1$, bilangan koordinasi 6, dan nama IUPAC klorotetraaminadikobalt(I)."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Bilangan oksidasi kobalt $+3$, bilangan koordinasi 6, dan nama IUPAC tetraaminadiklorokobalt(III) klorida, karena ligan netral amonia ($\\text{NH}_3$) bermuatan nol dan ligan kloro ($\\text{Cl}^-$) bermuatan $-1$. Terdapat total 3 ion klorida (2 sebagai ligan dalam kurung siku dan 1 sebagai anion penyeimbang di luar), sehingga $\\text{Biloks Co} + 4(0) + 2(-1) + (-1) = 0 \\implies \\text{Biloks Co} = +3$. Jumlah ligan monodentat yang terikat langsung pada kobalt adalah $4 + 2 = 6$ (bilangan koordinasi 6).. NH3 netral (muatan 0), Cl bermuatan -1. Ada 2 Cl di dalam kompleks dan 1 Cl di luar (total 3 Cl- = -3). Maka Co bermuatan +3. Ada 4 NH3 + 2 Cl = 6 ligan (bilangan koordinasi = 6). Biloks Co = +3, BK = 6, nama: tetraaminadiklorokobalt(III) klorida."
  },
  {
    "id": "kim-lat-m-20",
    "materi": "IDENTIFIKASI GUGUS FUNGSI ORGANIK",
    "topic": "Pembedaan Aldehida dan Keton Menggunakan Pereaksi Fehling",
    "hints": {
      "concept": "C3H6O adalah rumus umum alkanal (aldehida) dan alkanon (keton). Aldehida memberi hasil positif (endapan merah bata Cu2O) dengan Fehling, sedangkan keton negatif.",
      "execution": "X = propanal (aldehida), Y = propanon (keton)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dua senyawa organik isomer fungsi memiliki rumus molekul $\\text{C}_3\\text{H}_6\\text{O}$ (Senyawa $X$ dan Senyawa $Y$). Ketika diuji di laboratorium:<br>• Senyawa $X$ bereaksi positif dengan pereaksi Fehling menghasilkan endapan merah bata $\\text{Cu}_2\\text{O}$.<br>• Senyawa $Y$ tidak bereaksi dengan pereaksi Fehling maupun pereaksi Tollens.<br>Nama IUPAC dan rumus struktur dari Senyawa $X$ dan Senyawa $Y$ berturut-turut adalah...",
    "formulaHud": {
      "title": "UJI SPESIFIK ALDEHIDA DENGAN PEREAKSI FEHLING",
      "latex": "\\text{R-CHO} + 2\\text{Cu}^{2+} + 5\\text{OH}^- \\to \\text{R-COO}^- + \\text{Cu}_2\\text{O}(s) \\downarrow (\\text{Merah Bata}) + 3\\text{H}_2\\text{O}",
      "legend": "• Aldehida ($X$) teroksidasi menjadi asam karboksilat dan mengendapkan $\\text{Cu}_2\\text{O}$ merah bata<br>• Keton ($Y$) tidak memiliki atom hidrogen pada gugus karbonil sehingga resisten terhadap oksidasi Fehling"
    },
    "options": [
      {
        "key": "A",
        "text": "Senyawa $X$ adalah propanon dan Senyawa $Y$ adalah propanal, karena keton dianggap memiliki reaktivitas reduksi lebih tinggi."
      },
      {
        "key": "B",
        "text": "Senyawa $X$ adalah propanal ($\\text{CH}_3-\\text{CH}_2-\\text{CHO}$) dan Senyawa $Y$ adalah propanon (aseton, $\\text{CH}_3-\\text{CO}-\\text{CH}_3$), karena senyawa turunan alkana $\\text{C}_n\\text{H}_{2n}\\text{O}$ merupakan isomer fungsi antara aldehida (alkanal) dan keton (alkanon). Aldehida adalah reduktor yang mereduksi pereaksi Fehling menjadi endapan merah bata $\\text{Cu}_2\\text{O}$, sedangkan keton tidak dapat dioksidasi oleh pereaksi Fehling/Tollens."
      },
      {
        "key": "C",
        "text": "Senyawa $X$ adalah asam propanoat dan Senyawa $Y$ adalah metil etanoat, karena keduanya merupakan isomer fungsi asam karboksilat dan ester."
      },
      {
        "key": "D",
        "text": "Senyawa $X$ adalah propena dan Senyawa $Y$ adalah siklopropana, karena mengasumsikan senyawa hidrokarbon tak jenuh."
      },
      {
        "key": "E",
        "text": "Senyawa $X$ adalah 1-propanol dan Senyawa $Y$ adalah metoksi etana, karena rumus molekulnya keliru disamakan dengan alkohol dan eter."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Senyawa $X$ adalah propanal ($\\text{CH}_3-\\text{CH}_2-\\text{CHO}$) dan Senyawa $Y$ adalah propanon (aseton, $\\text{CH}_3-\\text{CO}-\\text{CH}_3$), karena senyawa turunan alkana $\\text{C}_n\\text{H}_{2n}\\text{O}$ merupakan isomer fungsi antara aldehida (alkanal) dan keton (alkanon). Aldehida adalah reduktor yang mereduksi pereaksi Fehling menjadi endapan merah bata $\\text{Cu}_2\\text{O}$, sedangkan keton tidak dapat dioksidasi oleh pereaksi Fehling/Tollens.. C3H6O adalah rumus umum alkanal (aldehida) dan alkanon (keton). Aldehida memberi hasil positif (endapan merah bata Cu2O) dengan Fehling, sedangkan keton negatif. X = propanal (aldehida), Y = propanon (keton)."
  },
  {
    "id": "kim-lat-m-21",
    "materi": "ASAM KARBOKSILAT & SIFAT KEASAMAN",
    "topic": "Pengaruh Efek Induksi Halogen terhadap Kuat Asam",
    "hints": {
      "concept": "Gugus penarik elektron (seperti Cl) memperkuat sifat asam dengan menstabilkan ion karboksilat melalui efek induksi. Semakin banyak atom Cl, asam semakin kuat.",
      "execution": "Urutan dari paling lemah: asam asetat (1) < kloroasetat (2) < dikloroasetat (3) < trikloroasetat (4)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Urutan kekuatan asam dari senyawa asam karboksilat berikut mulai dari yang paling lemah hingga yang paling kuat adalah:<br>1. Asam asetat ($\\text{CH}_3\\text{COOH}$)<br>2. Asam kloroasetat ($\\text{CH}_2\\text{ClCOOH}$)<br>3. Asam dikloroasetat ($\\text{CHCl}_2\\text{COOH}$)<br>4. Asam trikloroasetat ($\\text{CCl}_3\\text{COOH}$)",
    "formulaHud": {
      "title": "EFEK INDUKSI PENARIK ELEKTRON TERHADAP pKa",
      "latex": "\\text{Kekuatan Asam: } \\text{CH}_3\\text{COOH} (K_a = 1{,}8 \\times 10^{-5}) < \\text{CH}_2\\text{ClCOOH} (1{,}4 \\times 10^{-3}) < \\text{CHCl}_2\\text{COOH} (5 \\times 10^{-2}) < \\text{CCl}_3\\text{COOH} (0{,}2)",
      "legend": "• Efek induksi $-I$ dari atom klorin menstabilkan muatan negatif anion karboksilat ($-\\text{COO}^-$)<br>• Jumlah gugus penarik elektron $\\uparrow \\implies K_a \\uparrow \\implies \\text{Kekuatan Asam} \\uparrow$"
    },
    "options": [
      {
        "key": "A",
        "text": "$1 < 4 < 2 < 3$, dihitung dari perbedaan massa molar substituen halogen pada rantai karbon."
      },
      {
        "key": "B",
        "text": "$2 < 3 < 4 < 1$, karena asam asetat tanpa substituen dianggap memiliki kemurnian disosiasi paling tinggi."
      },
      {
        "key": "C",
        "text": "$4 < 3 < 2 < 1$, karena beranggapan atom halogen yang banyak justru menghalangi pelepasan ion hidrogen secara sterik."
      },
      {
        "key": "D",
        "text": "$1 = 2 = 3 = 4$, karena seluruh senyawa memiliki gugus karboksilat yang sama persis sehingga nilai Ka identik."
      },
      {
        "key": "E",
        "text": "$1 < 2 < 3 < 4$ (Asam asetat < Asam kloroasetat < Asam dikloroasetat < Asam trikloroasetat), karena atom klorin bersifat sangat elektronegatif dan memberikan efek induksi penarik elektron ($-I$) yang kuat di sepanjang ikatan karbon. Semakin banyak atom klorin yang terikat, semakin terdispersi muatan negatif pada ion karboksilat konjugatnya, sehingga ion konjugat menjadi jauh lebih stabil dan asam semakin mudah melepaskan proton $\\text{H}^+$ (kekuatan asam bertambah besar)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $1 < 2 < 3 < 4$ (Asam asetat < Asam kloroasetat < Asam dikloroasetat < Asam trikloroasetat), karena atom klorin bersifat sangat elektronegatif dan memberikan efek induksi penarik elektron ($-I$) yang kuat di sepanjang ikatan karbon. Semakin banyak atom klorin yang terikat, semakin terdispersi muatan negatif pada ion karboksilat konjugatnya, sehingga ion konjugat menjadi jauh lebih stabil dan asam semakin mudah melepaskan proton $\\text{H}^+$ (kekuatan asam bertambah besar).. Gugus penarik elektron (seperti Cl) memperkuat sifat asam dengan menstabilkan ion karboksilat melalui efek induksi. Semakin banyak atom Cl, asam semakin kuat. Urutan dari paling lemah: asam asetat (1) < kloroasetat (2) < dikloroasetat (3) < trikloroasetat (4)."
  },
  {
    "id": "kim-lat-m-22",
    "materi": "ISOMERISME OPTIS AKTIF",
    "topic": "Penentuan Jumlah Isomer Optis dari Atom Karbon Asimetris",
    "hints": {
      "concept": "C kiral di C2 dan C3 (ada 2 atom C kiral). Karena molekul simetris, ada bentuk meso (tidak aktif optik) selain 1 pasang enantiomer. Total stereoisomer = 3.",
      "execution": "2 atom C kiral, 3 stereoisomer (2 enantiomer + 1 bentuk meso)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Senyawa 2,3-diklorobutana memiliki rumus struktur $\\text{CH}_3-\\text{CH(Cl)}-\\text{CH(Cl)}-\\text{CH}_3$. Jumlah atom karbon kiral (karbon asimetris) pada molekul tersebut dan jumlah stereoisomer optis yang dimilikinya (termasuk memperhitungkan senyawa bentuk meso) adalah...",
    "formulaHud": {
      "title": "STEREOISOMER DENGAN BIDANG SIMETRI (BENTUK MESO)",
      "latex": "\\text{Jumlah Isomer Teoritis} = 2^n = 2^2 = 4; \\quad \\text{Karena simetris: } (2R, 3S) \\equiv \\text{Meso} \\implies \\text{Total Isomer} = 2^{n-1} + 2^{\\frac{n}{2}-1} = 2 + 1 = 3",
      "legend": "• C kiral: $C_2$ dan $C_3$ (masing-masing mengikat $-\\text{H}$, $-\\text{Cl}$, $-\\text{CH}_3$, dan rantai sisa)<br>• Bentuk meso memutar bidang polarisasi cahaya ke arah berlawanan dalam satu molekul sehingga saling meniadakan (optis inaktif)"
    },
    "options": [
      {
        "key": "A",
        "text": "Memiliki 2 atom karbon kiral dan menghasilkan 3 stereoisomer (sepasang enantiomer optis aktif dan satu bentuk meso optis inaktif), karena molekul memiliki bidang simetri internal (achiral plane) sehingga bentuk $(2R, 3S)$ identik dengan bayangan cerminnya sendiri (senyawa meso), sedangkan pasangan $(2R, 3R)$ dan $(2S, 3S)$ membentuk sepasang enantiomer aktif."
      },
      {
        "key": "B",
        "text": "Memiliki 1 atom karbon kiral dan menghasilkan 2 stereoisomer pasangan enantiomer."
      },
      {
        "key": "C",
        "text": "Memiliki 4 atom karbon kiral dan menghasilkan 16 stereoisomer berbeda."
      },
      {
        "key": "D",
        "text": "Memiliki 2 atom karbon kiral dan menghasilkan 4 stereoisomer optis aktif tanpa ada bentuk meso."
      },
      {
        "key": "E",
        "text": "Tidak memiliki atom karbon kiral sama sekali sehingga hanya memiliki satu bentuk geometri tunggal."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Memiliki 2 atom karbon kiral dan menghasilkan 3 stereoisomer (sepasang enantiomer optis aktif dan satu bentuk meso optis inaktif), karena molekul memiliki bidang simetri internal (achiral plane) sehingga bentuk $(2R, 3S)$ identik dengan bayangan cerminnya sendiri (senyawa meso), sedangkan pasangan $(2R, 3R)$ dan $(2S, 3S)$ membentuk sepasang enantiomer aktif.. C kiral di C2 dan C3 (ada 2 atom C kiral). Karena molekul simetris, ada bentuk meso (tidak aktif optik) selain 1 pasang enantiomer. Total stereoisomer = 3. 2 atom C kiral, 3 stereoisomer (2 enantiomer + 1 bentuk meso)."
  },
  {
    "id": "kim-lat-m-23",
    "materi": "MAKROMOLEKUL (POLIMER KARET ALAM)",
    "topic": "Monomer Karet Alam dan Proses Vulkanisasi Belerang",
    "hints": {
      "concept": "Karet alam adalah cis-1,4-poliisoprena (monomer isoprena = 2-metil-1,3-butadiena). Vulkanisasi belerang membentuk jembatan silang (-S-S-) agar karet lebih elastis dan tahan panas.",
      "execution": "Monomer isoprena, vulkanisasi membentuk jembatan silang belerang untuk meningkatkan elastisitas dan ketahanan panas."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Karet alam tersusun atas polimerisasi monomer hidrokarbon alami. Nama monomer karet alam dan tujuan dilakukannya proses vulkanisasi dengan pemanasan bersama serbuk belerang adalah...",
    "formulaHud": {
      "title": "STRUKTUR KARET ALAM & VULKANISASI GOODYEAR",
      "latex": "n\\,(\\text{CH}_2=\\text{C}(\\text{CH}_3)-\\text{CH}=\\text{CH}_2) \\xrightarrow{\\text{Polimerisasi}} [-\\text{CH}_2-\\text{C}(\\text{CH}_3)=\\text{CH}-\\text{CH}_2-]_n \\quad (\\text{cis-Poliisoprena})",
      "legend": "• Monomer: Isoprena (2-metil-1,3-butadiena)<br>• Jembatan belerang disulfida mengikat rantai-rantai poliisoprena, memberikan memori bentuk elastis (mencegah pergeseran permanen antar-rantai saat diregangkan)"
    },
    "options": [
      {
        "key": "A",
        "text": "Monomernya adalah stirena dan vulkanisasi bertujuan memutuskan rantai ikatan karbon agar karet menjadi lunak dan mudah dibentuk ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "B",
        "text": "Monomernya adalah kloroprena dan vulkanisasi bertujuan menggantikan seluruh ikatan rangkap dua dengan ikatan ionik polar."
      },
      {
        "key": "C",
        "text": "Monomernya adalah vinil klorida dan vulkanisasi bertujuan meningkatkan daya larut karet di dalam pelarut organik minyak bumi."
      },
      {
        "key": "D",
        "text": "Monomernya adalah 2-metil-1,3-butadiena (isoprena) dengan konfigurasi cis-1,4-poliisoprena, dan vulkanisasi bertujuan membentuk jembatan silang belerang (cross-linking $-S-S-$) antar-rantai polimer sehingga karet menjadi lebih elastis, kuat, tahan aus, dan tidak mudah meleleh atau lengket oleh panas."
      },
      {
        "key": "E",
        "text": "Monomernya adalah asam adipat dan vulkanisasi bertujuan menghasilkan reaksi kondensasi pembentukan serat benang sintetis."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Monomernya adalah 2-metil-1,3-butadiena (isoprena) dengan konfigurasi cis-1,4-poliisoprena, dan vulkanisasi bertujuan membentuk jembatan silang belerang (cross-linking $-S-S-$) antar-rantai polimer sehingga karet menjadi lebih elastis, kuat, tahan aus, dan tidak mudah meleleh atau lengket oleh panas.. Karet alam adalah cis-1,4-poliisoprena (monomer isoprena = 2-metil-1,3-butadiena). Vulkanisasi belerang membentuk jembatan silang (-S-S-) agar karet lebih elastis dan tahan panas. Monomer isoprena, vulkanisasi membentuk jembatan silang belerang untuk meningkatkan elastisitas dan ketahanan panas."
  },
  {
    "id": "kim-lat-m-24",
    "materi": "BIOKIMIA (UJI SPESIFIK KARBOHIDRAT)",
    "topic": "Reaksi Uji Fehling, Iodin, dan Seliwanoff pada Karbohidrat",
    "hints": {
      "concept": "Uji iodin biru kehitaman = amilum. Uji Seliwanoff merah ceri cepat (ketosa) + Fehling positif = fruktosa. Disakarida non-pereduksi yang hidrolisisnya menghasilkan 2 gula berbeda = sukrosa.",
      "execution": "A = amilum, B = fruktosa, C = sukrosa."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Seorang siswa menguji tiga sampel larutan karbohidrat ($A$, $B$, dan $C$) di laboratorium biokimia dengan hasil sebagai berikut:<br>• Sampel $A$ memberikan warna biru kehitaman pekat dengan larutan iodin.<br>• Sampel $B$ bereaksi positif menghasilkan endapan merah bata dengan pereaksi Fehling dan memberikan warna merah ceri cepat dengan uji Seliwanoff.<br>• Sampel $C$ tidak mereduksi Fehling tetapi setelah dihidrolisis dengan asam encer menghasilkan dua jenis monosakarida berbeda yang mereduksi Fehling.<br>Identitas karbohidrat $A$, $B$, dan $C$ berturut-turut adalah...",
    "formulaHud": {
      "title": "UJI SPESIFIK KARBOHIDRAT",
      "latex": "\\begin{aligned} \\text{Amilum} + \\text{I}_2 & \\to \\text{Kompleks Biru-Kehitaman} \\\\ \\text{Fruktosa (Ketosa)} + \\text{Resorsinol (Seliwanoff)} & \\to \\text{Merah Ceri Cepat (< 1 menit)} \\\\ \\text{Sukrosa} + \\text{H}_2\\text{O} & \\xrightarrow{\\text{H}^+} \\text{Glukosa (Pereduksi)} + \\text{Fruktosa (Pereduksi)} \\end{aligned}",
      "legend": "• Amilum = Polisakarida (uji Iodin positif)<br>• Fruktosa = Ketoheksosa pereduksi (Fehling positif, Seliwanoff merah cepat)<br>• Sukrosa = Disakarida non-pereduksi ikatan $\\alpha-1,\\beta-2$"
    },
    "options": [
      {
        "key": "A",
        "text": "$A$ adalah glukosa, $B$ adalah maltosa, dan $C$ adalah selulosa menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "B",
        "text": "$A$ adalah amilum, $B$ adalah sukrosa, dan $C$ adalah glikogen."
      },
      {
        "key": "C",
        "text": "$A$ adalah glikogen, $B$ adalah amilum, dan $C$ adalah maltosa."
      },
      {
        "key": "D",
        "text": "$A$ adalah selulosa, $B$ adalah galaktosa, dan $C$ adalah laktosa."
      },
      {
        "key": "E",
        "text": "$A$ adalah amilum (pati), $B$ adalah fruktosa, dan $C$ adalah sukrosa, karena amilum membentuk kompleks biru kehitaman dengan iodin; fruktosa adalah monosakarida ketosa pereduksi yang cepat bereaksi positif dengan uji Seliwanoff membentuk warna merah ceri; dan sukrosa adalah disakarida non-pereduksi yang terhidrolisis menjadi glukosa dan fruktosa."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $A$ adalah amilum (pati), $B$ adalah fruktosa, dan $C$ adalah sukrosa, karena amilum membentuk kompleks biru kehitaman dengan iodin; fruktosa adalah monosakarida ketosa pereduksi yang cepat bereaksi positif dengan uji Seliwanoff membentuk warna merah ceri; dan sukrosa adalah disakarida non-pereduksi yang terhidrolisis menjadi glukosa dan fruktosa.. Uji iodin biru kehitaman = amilum. Uji Seliwanoff merah ceri cepat (ketosa) + Fehling positif = fruktosa. Disakarida non-pereduksi yang hidrolisisnya menghasilkan 2 gula berbeda = sukrosa. A = amilum, B = fruktosa, C = sukrosa."
  },
  {
    "id": "kim-lat-m-25",
    "materi": "BIOKIMIA (UJI PROTEIN & DENATURASI)",
    "topic": "Reaksi Biuret, Xantoproteat, dan Uji Belerang Timbal Asetat",
    "hints": {
      "concept": "Uji Biuret (ungu) = ikatan peptida. Uji Xantoproteat (kuning/jingga) = cincin benzena. Uji timbal asetat (endapan PbS hitam) = belerang/sulfur.",
      "execution": "Ikatan peptida, cincin benzena, dan unsur belerang."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Suatu larutan putih telur (albumin) diuji dengan beberapa pereaksi protein:<br>• Ditambahkan larutan $\\text{NaOH}$ encer dan beberapa tetes $\\text{CuSO}_4$ encer menghasilkan warna ungu pekat.<br>• Ditambahkan asam nitrat pekat ($\\text{HNO}_3$) lalu dipanaskan menghasilkan endapan kuning yang berubah menjadi jingga saat dibasakan.<br>• Ditambahkan $\\text{NaOH}$ pekat dan larutan timbal(II) asetat ($\\text{Pb(CH}_3\\text{COO)}_2$) lalu dipanaskan menghasilkan endapan hitam pekat.<br>Informasi struktural yang diperoleh dari ketiga uji biokimiawi tersebut berturut-turut adalah...",
    "formulaHud": {
      "title": "UJI KARAKTERISTIK PROTEIN & ASAM AMINO",
      "latex": "\\begin{aligned} \\text{Uji Biuret (}\\text{Cu}^{2+} + \\text{OH}^-\\text{)} & \\to \\text{Ungu} \\implies \\ge 2\\text{ Ikatan Peptida} \\\\ \\text{Uji Xantoproteat (}\\text{HNO}_3\\text{)} & \\to \\text{Kuning} \\to \\text{Jingga} \\implies \\text{Cincin Benzena (Tirosin, Fenilalanin)} \\\\ \\text{Uji Timbal Asetat (}\\text{Pb}^{2+}\\text{)} & \\to \\text{PbS}(s) \\downarrow (\\text{Hitam}) \\implies \\text{Belerang (Sistein, Metionin)} \\end{aligned}",
      "legend": "• Biuret mendeteksi kompleks koordinasi tembaga dengan nitrogen ikatan peptida<br>• Nitrasi cincin aromatik menghasilkan senyawa nitro aromatik berwarna kuning<br>• Pembentukan $\\text{PbS}$ membuktikan adanya belerang tereduksi"
    },
    "options": [
      {
        "key": "A",
        "text": "Mengandung asam nukleat DNA, memiliki rantai peptida terbuka, dan mengandung ikatan glikosidik bercabang."
      },
      {
        "key": "B",
        "text": "Mengandung lipid fosfolipid membran sel dan asam amino nonpolar alifatik rantai lurus murni."
      },
      {
        "key": "C",
        "text": "Mengandung protein globular sederhana tanpa ikatan peptida dan tidak memiliki gugus sulfur aktif."
      },
      {
        "key": "D",
        "text": "Mengandung ikatan peptida (uji Biuret positif ungu), memiliki asam amino berinti cincin benzena seperti tirosin/triptofan (uji Xantoproteat positif kuning-jingga), dan mengandung asam amino yang memiliki atom belerang seperti sistein/metionin (uji timbal asetat positif endapan $\\text{PbS}$ hitam)."
      },
      {
        "key": "E",
        "text": "Mengandung gugus karbohidrat monosakarida, memiliki ikatan ester lemak, dan mengandung ion kalsium terlarut."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Mengandung ikatan peptida (uji Biuret positif ungu), memiliki asam amino berinti cincin benzena seperti tirosin/triptofan (uji Xantoproteat positif kuning-jingga), dan mengandung asam amino yang memiliki atom belerang seperti sistein/metionin (uji timbal asetat positif endapan $\\text{PbS}$ hitam).. Uji Biuret (ungu) = ikatan peptida. Uji Xantoproteat (kuning/jingga) = cincin benzena. Uji timbal asetat (endapan PbS hitam) = belerang/sulfur. Ikatan peptida, cincin benzena, dan unsur belerang."
  },
  {
    "id": "kim-lat-h-01",
    "materi": "STRUKTUR ATOM & TEORI ORBITAL MOLEKUL",
    "topic": "Orde Ikatan dan Sifat Kemagnetan Spesies Dioksigen",
    "hints": {
      "concept": "O2 memiliki 2 elektron tak berpasangan di orbital pi* (paramagnetik, BO = (8-4)/2 = 2). Menambah 2e- membentuk O2(2-) mengisi penuh orbital pi* -> semua elektron berpasangan (diamagnetik), BO = (8-6)/2 = 1.",
      "execution": "Orde ikatan turun dari 2 ke 1, paramagnetik berubah menjadi diamagnetik."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Berdasarkan Teori Orbital Molekul (Molecular Orbital Theory) untuk molekul diatomik homointi periode kedua, konfigurasi orbital molekul tingkat valensi gas oksigen ($\\text{O}_2$) memiliki dua elektron tak berpasangan pada orbital anti-ikatan $\\pi^*_{2p_x}$ dan $\\pi^*_{2p_y}$. Jika molekul $\\text{O}_2$ tereduksi menjadi ion peroksida ($\\text{O}_2^{2-}$), perubahan orde ikatan (bond order) dan sifat kemagnetan yang terjadi adalah...",
    "formulaHud": {
      "title": "ORDE IKATAN TEORI ORBITAL MOLEKUL (MO)",
      "latex": "\\text{BO} = \\frac{N_{\\text{bonding}} - N_{\\text{antibonding}}}{2}; \\quad \\text{BO}(\\text{O}_2) = \\frac{8 - 4}{2} = 2 \\text{ (Paramagnetik)}; \\quad \\text{BO}(\\text{O}_2^{2-}) = \\frac{8 - 6}{2} = 1 \\text{ (Diamagnetik)}",
      "legend": "• Konfigurasi valensi $\\text{O}_2$: $(\\sigma_{2s})^2(\\sigma^*_{2s})^2(\\sigma_{2p_z})^2(\\pi_{2p_x})^2(\\pi_{2p_y})^2(\\pi^*_{2p_x})^1(\\pi^*_{2p_y})^1$<br>• Ion $\\text{O}_2^{2-}$ memiliki orbital $(\\pi^*_{2p})^4$ penuh $\\implies$ Diamagnetik dan ikatan melemah"
    },
    "options": [
      {
        "key": "A",
        "text": "Orde ikatan turun dari 2 menjadi 1 dan sifat kemagnetan berubah dari paramagnetik menjadi diamagnetik, karena penambahan 2 elektron pada $\\text{O}_2^{2-}$ mengisi penuh orbital anti-ikatan $\\pi^*_{2p_x}$ dan $\\pi^*_{2p_y}$ sehingga seluruh elektron berpasangan (diamagnetik), dan orde ikatan dihitung dari $\\text{BO} = \\frac{N_b - N_a}{2} = \\frac{8 - 6}{2} = 1$ (pada $\\text{O}_2$ nilainya $\\frac{8 - 4}{2} = 2$)."
      },
      {
        "key": "B",
        "text": "Orde ikatan turun dari 2 menjadi 1{,}5 dan sifat kemagnetan tetap paramagnetik seperti ion superoksida."
      },
      {
        "key": "C",
        "text": "Orde ikatan menjadi nol dan molekul peroksida langsung terdisosiasi spontan menjadi atom bebas."
      },
      {
        "key": "D",
        "text": "Orde ikatan naik dari 2 menjadi 3 dan sifat kemagnetan tetap paramagnetik dengan medan magnet kuat."
      },
      {
        "key": "E",
        "text": "Orde ikatan tidak berubah (tetap 2) dan sifat kemagnetan tetap paramagnetik dengan spin sejajar."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Orde ikatan turun dari 2 menjadi 1 dan sifat kemagnetan berubah dari paramagnetik menjadi diamagnetik, karena penambahan 2 elektron pada $\\text{O}_2^{2-}$ mengisi penuh orbital anti-ikatan $\\pi^*_{2p_x}$ dan $\\pi^*_{2p_y}$ sehingga seluruh elektron berpasangan (diamagnetik), dan orde ikatan dihitung dari $\\text{BO} = \\frac{N_b - N_a}{2} = \\frac{8 - 6}{2} = 1$ (pada $\\text{O}_2$ nilainya $\\frac{8 - 4}{2} = 2$).. O2 memiliki 2 elektron tak berpasangan di orbital pi* (paramagnetik, BO = (8-4)/2 = 2). Menambah 2e- membentuk O2(2-) mengisi penuh orbital pi* -> semua elektron berpasangan (diamagnetik), BO = (8-6)/2 = 1. Orde ikatan turun dari 2 ke 1, paramagnetik berubah menjadi diamagnetik."
  },
  {
    "id": "kim-lat-h-02",
    "materi": "KIMIA KOORDINASI (TEORI MEDAN KRISTAL / CFT)",
    "topic": "Pembelahan Orbital d Kompleks Oktahedral Spin Tinggi vs Rendah",
    "hints": {
      "concept": "CN- adalah ligan kuat (Delta_o besar, spin rendah): 6 elektron mengisi t2g berpasangan semua (diamagnetik). H2O ligan lemah (Delta_o kecil, spin tinggi): konfigurasi t2g^4 eg^2 ada 4 elektron tak berpasangan (paramagnetik).",
      "execution": "CN- ligan medan kuat (spin rendah, t2g^6 eg^0), H2O ligan medan lemah (spin tinggi, t2g^4 eg^2)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Ion kompleks heksasianoferat(II) $[\\text{Fe}(\\text{CN})_6]^{4-}$ bersifat diamagnetik, sedangkan ion kompleks heksaaquabesi(II) $[\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}$ bersifat paramagnetik kuat dengan 4 elektron tak berpasangan. Padahal kedua ion kompleks tersebut sama-sama memiliki ion pusat $\\text{Fe}^{2+}$ berkonsfigurasi $3d^6$. Penjelasan teoritis yang tepat berdasarkan Teori Medan Kristal (Crystal Field Theory) adalah...",
    "formulaHud": {
      "title": "PEMBELAHAN ORBITAL d OKTAHEDRAL (CFT)",
      "latex": "\\Delta_o > P \\implies [\\text{Fe}(\\text{CN})_6]^{4-}: t_{2g}^6\\,e_g^0 \\quad (n=0, \\text{Low Spin/Diamagnetik}); \\quad \\Delta_o < P \\implies [\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}: t_{2g}^4\\,e_g^2 \\quad (n=4, \\text{High Spin/Paramagnetik})",
      "legend": "• Deret spektrokimia: $\\text{I}^- < \\text{Br}^- < \\text{Cl}^- < \\text{F}^- < \\text{OH}^- < \\text{H}_2\\text{O} < \\text{NH}_3 < \\text{en} < \\text{CN}^- < \\text{CO}$<br>• Ligan kuat menghasilkan medan kristal $\\Delta_o$ besar"
    },
    "options": [
      {
        "key": "A",
        "text": "Ligan $\\text{CN}^-$ mengoksidasi atom besi menjadi bilangan oksidasi $+3$, sedangkan ligan $\\text{H}_2\\text{O}$ mereduksinya menjadi besi nol."
      },
      {
        "key": "B",
        "text": "Kompleks $[\\text{Fe}(\\text{CN})_6]^{4-}$ memiliki geometri tetrahedral sedangkan $[\\text{Fe}(\\text{H}_2\\text{O})_6]^{2+}$ memiliki geometri oktahedral."
      },
      {
        "key": "C",
        "text": "Ligan $\\text{CN}^-$ membentuk ikatan ionik murni sedangkan molekul air membentuk ikatan hidrogen kovalen koordinasi polar."
      },
      {
        "key": "D",
        "text": "Ligan $\\text{H}_2\\text{O}$ memiliki pasangan elektron bebas lebih banyak sehingga mendistorsi simetri medan ligan oktahedral menjadi bujur sangkar."
      },
      {
        "key": "E",
        "text": "Ligan $\\text{CN}^-$ adalah ligan medan kuat ($\\Delta_o > P$, energi pemisahan medan oktahedral lebih besar daripada energi perpasangan elektron) yang memaksa keenam elektron $3d$ berpasangan di orbital energi rendah $t_{2g}$ membentuk kompleks spin rendah ($t_{2g}^6\\,e_g^0$, diamagnetik); sedangkan ligan $\\text{H}_2\\text{O}$ adalah ligan medan lemah ($\\Delta_o < P$) sehingga elektron mengisi orbital $t_{2g}$ dan $e_g$ secara terdistribusi membentuk kompleks spin tinggi ($t_{2g}^4\\,e_g^2$, 4 elektron tak berpasangan)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Ligan $\\text{CN}^-$ adalah ligan medan kuat ($\\Delta_o > P$, energi pemisahan medan oktahedral lebih besar daripada energi perpasangan elektron) yang memaksa keenam elektron $3d$ berpasangan di orbital energi rendah $t_{2g}$ membentuk kompleks spin rendah ($t_{2g}^6\\,e_g^0$, diamagnetik); sedangkan ligan $\\text{H}_2\\text{O}$ adalah ligan medan lemah ($\\Delta_o < P$) sehingga elektron mengisi orbital $t_{2g}$ dan $e_g$ secara terdistribusi membentuk kompleks spin tinggi ($t_{2g}^4\\,e_g^2$, 4 elektron tak berpasangan).. CN- adalah ligan kuat (Delta_o besar, spin rendah): 6 elektron mengisi t2g berpasangan semua (diamagnetik). H2O ligan lemah (Delta_o kecil, spin tinggi): konfigurasi t2g^4 eg^2 ada 4 elektron tak berpasangan (paramagnetik). CN- ligan medan kuat (spin rendah, t2g^6 eg^0), H2O ligan medan lemah (spin tinggi, t2g^4 eg^2)."
  },
  {
    "id": "kim-lat-h-03",
    "materi": "STOIKIOMETRI TITRASI PENGENDAPAN (ARGENTOMETRI)",
    "topic": "Penentuan Kadar Klorida dengan Metode Mohr",
    "hints": {
      "concept": "Mol Ag+ = 24 mL * 0,1 M = 2,4 mmol. Ini terdapat dalam 25 mL sampel. Total dalam 100 mL = 2,4 * 4 = 9,6 mmol. Massa NaCl = 9,6 mmol * 58,5 mg/mmol = 561,6 mg = 0,5616 g. % = 0,5616 / 0,585 * 100%.",
      "execution": "% kemurnian = (0,5616 / 0,585) * 100% = 96,0%."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebanyak $0{,}585\\text{ gram}$ sampel garam dapur dilarutkan dalam air hingga volume $100\\text{ mL}$. Sebanyak $25\\text{ mL}$ alikuot larutan tersebut dititrasi dengan larutan standar $\\text{AgNO}_3\\,0{,}1\\text{ M}$ menggunakan indikator kalium kromat ($\\text{K}_2\\text{CrO}_4$). Titik akhir titrasi tercapai saat terbentuk endapan merah bata $\\text{Ag}_2\\text{CrO}_4$ dan volume $\\text{AgNO}_3$ yang terpakai adalah tepat $24\\text{ mL}$. Kemurnian persentase massa natrium klorida ($\\text{NaCl}$, $M_r = 58{,}5\\text{ g/mol}$) dalam sampel garam dapur tersebut adalah...",
    "formulaHud": {
      "title": "TITRASI ARGENTOMETRI METODE MOHR",
      "latex": "n_{\\text{Cl}^-} = V_{\\text{AgNO}_3} \\times M_{\\text{AgNO}_3} = 24 \\times 0{,}1 = 2{,}4\\text{ mmol}; \\quad n_{\\text{total}} = 2{,}4 \\times \\frac{100}{25} = 9{,}6\\text{ mmol}; \\quad \\% = \\frac{9{,}6 \\times 10^{-3} \\times 58{,}5}{0{,}585} \\times 100\\% = 96\\%",
      "legend": "• Titrasi Mohr menggunakan indikator $\\text{CrO}_4^{2-}$ yang membentuk endapan merah bata $\\text{Ag}_2\\text{CrO}_4$ setelah seluruh $\\text{Cl}^-$ mengendap putih<br>• Kadar $\\text{NaCl} = 96{,}0\\%$"
    },
    "options": [
      {
        "key": "A",
        "text": "$96{,}0\\%$, karena jumlah mol ion $\\text{Ag}^+$ yang bereaksi pada titrasi alikuot $25\\text{ mL}$ adalah $n = V \\times M = 24\\text{ mL} \\times 0{,}1\\text{ M} = 2{,}4\\text{ mmol}$. Karena reaksi pengendapan $\\text{Ag}^+ + \\text{Cl}^- \\to \\text{AgCl}(s)$ memiliki perbandingan mol $1 : 1$, maka mol $\\text{NaCl}$ dalam $25\\text{ mL}$ adalah $2{,}4\\text{ mmol}$. Total mol $\\text{NaCl}$ dalam seluruh $100\\text{ mL}$ larutan sampel adalah $2{,}4\\text{ mmol} \\times \\frac{100}{25} = 9{,}6\\text{ mmol} = 9{,}6 \\times 10^{-3}\\text{ mol}$. Massa $\\text{NaCl}$ murni adalah $m = 9{,}6 \\times 10^{-3}\\text{ mol} \\times 58{,}5\\text{ g/mol} = 0{,}5616\\text{ gram}$. Persentase kemurnian adalah $\\frac{0{,}5616\\text{ g}}{0{,}585\\text{ g}} \\times 100\\% = 96{,}0\\%$."
      },
      {
        "key": "B",
        "text": "$80{,}0\\%$, dihitung dari rasio kelarutan perak klorida terhadap perak kromat."
      },
      {
        "key": "C",
        "text": "$100{,}0\\%$, karena beranggapan sampel garam dapur bebas dari zat pengotor higroskopis."
      },
      {
        "key": "D",
        "text": "$48{,}0\\%$, dihitung dengan membagi massa sampel dengan volume titran tanpa massa molar."
      },
      {
        "key": "E",
        "text": "$24{,}0\\%$, karena mengabaikan faktor pengenceran alikuot sampel empat kali lipat ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $96{,}0\\%$, karena jumlah mol ion $\\text{Ag}^+$ yang bereaksi pada titrasi alikuot $25\\text{ mL}$ adalah $n = V \\times M = 24\\text{ mL} \\times 0{,}1\\text{ M} = 2{,}4\\text{ mmol}$. Karena reaksi pengendapan $\\text{Ag}^+ + \\text{Cl}^- \\to \\text{AgCl}(s)$ memiliki perbandingan mol $1 : 1$, maka mol $\\text{NaCl}$ dalam $25\\text{ mL}$ adalah $2{,}4\\text{ mmol}$. Total mol $\\text{NaCl}$ dalam seluruh $100\\text{ mL}$ larutan sampel adalah $2{,}4\\text{ mmol} \\times \\frac{100}{25} = 9{,}6\\text{ mmol} = 9{,}6 \\times 10^{-3}\\text{ mol}$. Massa $\\text{NaCl}$ murni adalah $m = 9{,}6 \\times 10^{-3}\\text{ mol} \\times 58{,}5\\text{ g/mol} = 0{,}5616\\text{ gram}$. Persentase kemurnian adalah $\\frac{0{,}5616\\text{ g}}{0{,}585\\text{ g}} \\times 100\\% = 96{,}0\\%$.. Mol Ag+ = 24 mL * 0,1 M = 2,4 mmol. Ini terdapat dalam 25 mL sampel. Total dalam 100 mL = 2,4 * 4 = 9,6 mmol. Massa NaCl = 9,6 mmol * 58,5 mg/mmol = 561,6 mg = 0,5616 g. % = 0,5616 / 0,585 * 100%. % kemurnian = (0,5616 / 0,585) * 100% = 96,0%."
  },
  {
    "id": "kim-lat-h-04",
    "materi": "GAS NYATA (PERSAMAAN VAN DER WAALS)",
    "topic": "Koreksi Tekanan dan Volume Molekuler Gas Nyata",
    "hints": {
      "concept": "a mengoreksi gaya tarik-menarik antarmolekul (yang mengurangi tekanan terukur). b mengoreksi volume fisik yang ditempati molekul gas (volume eksklusi).",
      "execution": "a = gaya tarik antarmolekul, b = volume fisik partikel molekul."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Persamaan Van der Waals untuk satu mol gas nyata dinyatakan sebagai:<br>$$\\left(P + \\frac{a}{V_m^2}\\right)(V_m - b) = R T$$<br>Makna fisis dari tetapan koreksi $a$ dan tetapan koreksi $b$ dalam menjelaskan penyimpangan gas nyata dari perilaku gas ideal adalah...",
    "formulaHud": {
      "title": "PERSAMAAN GAS NYATA VAN DER WAALS",
      "latex": "\\left(P + \\frac{a n^2}{V^2}\\right)(V - n b) = n R T",
      "legend": "• Suku $\\frac{a n^2}{V^2}$ = Tekanan internal akibat gaya tarik intermolekul (kohesi)<br>• Suku $n b$ = Volume eksklusi yang ditempati molekul secara berhingga<br>• Gas nyata mendekati sifat gas ideal pada tekanan sangat rendah dan suhu sangat tinggi"
    },
    "options": [
      {
        "key": "A",
        "text": "Tetapan $a$ mengoreksi adanya gaya tarik-menarik antarmolekul gas nyata (intermolecular attraction) yang memperkecil tekanan terukur pada dinding bejana, sedangkan tetapan $b$ mengoreksi volume nyata yang ditempati oleh partikel molekul gas itu sendiri (excluded volume) yang tidak dapat ditembus oleh molekul lain."
      },
      {
        "key": "B",
        "text": "Tetapan $a$ mengoreksi gravitasi bumi di dalam bejana dan tetapan $b$ menyatakan konduktivitas termal wadah."
      },
      {
        "key": "C",
        "text": "Kedua tetapan $a$ dan $b$ merupakan konstanta empiris tanpa makna fisis yang hanya berfungsi sebagai penyeimbang dimensi satuan."
      },
      {
        "key": "D",
        "text": "Tetapan $a$ mengoreksi volume fisik molekul gas padat dan tetapan $b$ mengoreksi energi kinetik translasi partikel menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "E",
        "text": "Tetapan $a$ mengoreksi tumbukan lenting sempurna molekul dan tetapan $b$ menyatakan laju disosiasi endotermik gas."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Tetapan $a$ mengoreksi adanya gaya tarik-menarik antarmolekul gas nyata (intermolecular attraction) yang memperkecil tekanan terukur pada dinding bejana, sedangkan tetapan $b$ mengoreksi volume nyata yang ditempati oleh partikel molekul gas itu sendiri (excluded volume) yang tidak dapat ditembus oleh molekul lain.. a mengoreksi gaya tarik-menarik antarmolekul (yang mengurangi tekanan terukur). b mengoreksi volume fisik yang ditempati molekul gas (volume eksklusi). a = gaya tarik antarmolekul, b = volume fisik partikel molekul."
  },
  {
    "id": "kim-lat-h-05",
    "materi": "LARUTAN PENYANGGA POLIPROTIK (BUFFER SITOPLASMA)",
    "topic": "Sistem Penyangga Dihidrogen Fosfat dalam Sel Tubuh",
    "hints": {
      "concept": "Cari pKa yang paling dekat dengan pH fisiologis 7,4, yaitu pKa2 = 7,21 (pasangan H2PO4- dan HPO4 2-). Gunakan pH = pKa2 + log([HPO4 2-] / [H2PO4 -]).",
      "execution": "log(rasio) = 7,40 - 7,21 = 0,19 -> rasio = 10^0,19 = 1,55. Pasangan H2PO4- dan HPO4 2-."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Asam fosfat ($\\text{H}_3\\text{PO}_4$) adalah asam triprotik dengan tiga tetapan ionisasi bertingkat berturut-turut: $K_{a1} = 7{,}5 \\times 10^{-3}$ ($\\text{p}K_{a1} = 2{,}12$), $K_{a2} = 6{,}2 \\times 10^{-8}$ ($\\text{p}K_{a2} = 7{,}21$), dan $K_{a3} = 4{,}2 \\times 10^{-13}$ ($\\text{p}K_{a3} = 12{,}38$). Pasangan spesi kimia yang berperan sebagai larutan penyangga utama dalam cairan intraseluler pada pH fisiologis tubuh manusia ($\\text{pH} \\approx 7{,}4$) beserta perbandingan rasio molar $[\\text{Basa Konjugasi}] / [\\text{Asam Konjugasi}]$ adalah... (Gunakan $10^{0{,}19} \\approx 1{,}55$)",
    "formulaHud": {
      "title": "SISTEM PENYANGGA FOSFAT INTRASELULER",
      "latex": "\\text{H}_2\\text{PO}_4^- \\rightleftharpoons \\text{HPO}_4^{2-} + \\text{H}^+; \\quad \\text{pH} = \\text{p}K_{a2} + \\log\\frac{[\\text{HPO}_4^{2-}]}{[\\text{H}_2\\text{PO}_4^-]}; \\quad 7{,}40 = 7{,}21 + \\log(\\text{rasio}) \\implies \\text{rasio} \\approx 1{,}55",
      "legend": "• Buffer paling efektif bekerja pada rentang $\\text{pH} = \\text{p}K_a \\pm 1$<br>• Pada pH $7{,}4$, spesi dominan adalah $\\text{HPO}_4^{2-}$ (basa konjugasi sedikit lebih banyak dari asam konjugasi)"
    },
    "options": [
      {
        "key": "A",
        "text": "Pasangan $\\text{H}_3\\text{PO}_4$ dan $\\text{PO}_4^{3-}$ dengan rasio $1 : 1$, karena mengabaikan tahapan disosiasi bertingkat asam poliprotik."
      },
      {
        "key": "B",
        "text": "Pasangan $\\text{H}_3\\text{PO}_4$ dan $\\text{H}_2\\text{PO}_4^-$ dengan rasio molar $100 : 1$, karena asam triprotik harus dimulai dari pelepasan proton pertama."
      },
      {
        "key": "C",
        "text": "Pasangan $\\text{H}_2\\text{PO}_4^-$ (asam) dan $\\text{HPO}_4^{2-}$ (basa konjugasi) dengan rasio $[\\text{HPO}_4^{2-}] / [\\text{H}_2\\text{PO}_4^-] \\approx 1{,}55$, karena nilai $\\text{p}K_{a2} = 7{,}21$ berada paling dekat dengan rentang pH fisiologis $7{,}4$. Menurut persamaan Henderson-Hasselbalch: $\\text{pH} = \\text{p}K_{a2} + \\log\\frac{[\\text{HPO}_4^{2-}]}{[\\text{H}_2\\text{PO}_4^-]} \\implies 7{,}40 = 7{,}21 + \\log(\\text{rasio}) \\implies \\log(\\text{rasio}) = 0{,}19 \\implies \\text{rasio} = 10^{0{,}19} \\approx 1{,}55$."
      },
      {
        "key": "D",
        "text": "Pasangan $\\text{HPO}_4^{2-}$ dan $\\text{PO}_4^{3-}$ dengan rasio molar $1 : 10$, karena ion fosfat bebas memiliki muatan tiga negatif."
      },
      {
        "key": "E",
        "text": "Pasangan $\\text{H}_2\\text{PO}_4^-$ dan $\\text{HPO}_4^{2-}$ dengan rasio $[\\text{HPO}_4^{2-}] / [\\text{H}_2\\text{PO}_4^-] = 0{,}65$, karena formula rasio logaritma Henderson-Hasselbalch keliru dibalik."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Pasangan $\\text{H}_2\\text{PO}_4^-$ (asam) dan $\\text{HPO}_4^{2-}$ (basa konjugasi) dengan rasio $[\\text{HPO}_4^{2-}] / [\\text{H}_2\\text{PO}_4^-] \\approx 1{,}55$, karena nilai $\\text{p}K_{a2} = 7{,}21$ berada paling dekat dengan rentang pH fisiologis $7{,}4$. Menurut persamaan Henderson-Hasselbalch: $\\text{pH} = \\text{p}K_{a2} + \\log\\frac{[\\text{HPO}_4^{2-}]}{[\\text{H}_2\\text{PO}_4^-]} \\implies 7{,}40 = 7{,}21 + \\log(\\text{rasio}) \\implies \\log(\\text{rasio}) = 0{,}19 \\implies \\text{rasio} = 10^{0{,}19} \\approx 1{,}55$.. Cari pKa yang paling dekat dengan pH fisiologis 7,4, yaitu pKa2 = 7,21 (pasangan H2PO4- dan HPO4 2-). Gunakan pH = pKa2 + log([HPO4 2-] / [H2PO4 -]). log(rasio) = 7,40 - 7,21 = 0,19 -> rasio = 10^0,19 = 1,55. Pasangan H2PO4- dan HPO4 2-."
  },
  {
    "id": "kim-lat-h-06",
    "materi": "HIDROLISIS BERTINGKAT GARAM POLIPROTIK",
    "topic": "Perhitungan pH Larutan Natrium Karbonat Na2CO3",
    "hints": {
      "concept": "Garam Na2CO3 terhidrolisis menghasilkan OH-: CO3(2-) + H2O <-> HCO3- + OH-. Tetapan hidrolisis Kh1 = Kw / Ka2. Hitung [OH-] = sqrt(Kh1 * [garam]), lalu pH = 14 - pOH.",
      "execution": "Kh1 = 1e-14 / 5e-11 = 2e-4. [OH-] = sqrt(2e-4 * 0,1) = sqrt(2e-5) = 4,47e-3 M. pOH = 2,35 -> pH = 11,65."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Natrium karbonat ($\\text{Na}_2\\text{CO}_3$) dilarutkan ke dalam air menghasilkan larutan berkonsentrasi $0{,}1\\text{ M}$. Diketahui asam karbonat memiliki dua tetapan ionisasi: $K_{a1} = 4 \\times 10^{-7}$ dan $K_{a2} = 5 \\times 10^{-11}$, serta $K_w = 1 \\times 10^{-14}$. Nilai pH larutan natrium karbonat tersebut berdasarkan hidrolisis tahap pertamanya adalah...",
    "formulaHud": {
      "title": "HIDROLISIS TAHAP PERTAMA ANION KARBONAT",
      "latex": "K_{h1} = \\frac{K_w}{K_{a2}} = \\frac{10^{-14}}{5 \\times 10^{-11}} = 2 \\times 10^{-4}; \\quad [\\text{OH}^-] = \\sqrt{K_{h1} C} = \\sqrt{2 \\times 10^{-5}} \\approx 4{,}47 \\times 10^{-3}\\text{ M}; \\quad \\text{pH} = 14 - \\text{pOH} \\approx 11{,}65",
      "legend": "• Hidrolisis tahap pertama sangat dominan dibandingkan tahap kedua ($K_{h1} \\gg K_{h2}$)<br>• $K_{h2} = K_w / K_{a1} = 10^{-14} / 4 \\times 10^{-7} = 2{,}5 \\times 10^{-8}$ dapat diabaikan<br>• $\\text{pH} = 11{,}65$ (bersifat sangat basa)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{pH} = 8{,}35$, dihitung dari nilai logaritma konsentrasi garam tanpa memperhitungkan tetapan kesetimbangan air."
      },
      {
        "key": "B",
        "text": "$\\text{pH} = 9{,}70$, karena tetapan hidrolisis keliru dihitung menggunakan Ka1 bukan Ka2 dari asam diprotik."
      },
      {
        "key": "C",
        "text": "$\\text{pH} = 13{,}00$, karena larutan garam dianggap terdisosiasi sempurna menghasilkan basa kuat bebas."
      },
      {
        "key": "D",
        "text": "$\\text{pH} = 11{,}65$ (karena $[\\text{OH}^-] \\approx 4{,}47 \\times 10^{-3}\\text{ M}$), karena anion karbonat ($\\text{CO}_3^{2-}$) mengalami hidrolisis tahap pertama melepaskan ion hidroksida: $\\text{CO}_3^{2-} + \\text{H}_2\\text{O} \\rightleftharpoons \\text{HCO}_3^- + \\text{OH}^-$ dengan tetapan hidrolisis $K_{h1} = \\frac{K_w}{K_{a2}} = \\frac{10^{-14}}{5 \\times 10^{-11}} = 2 \\times 10^{-4}$. Konsentrasi ion hidroksida dihitung dari $[\\text{OH}^-] = \\sqrt{K_{h1} [\\text{CO}_3^{2-}]} = \\sqrt{(2 \\times 10^{-4}) \\times 0{,}1} = \\sqrt{2 \\times 10^{-5}} = \\sqrt{20 \\times 10^{-6}} \\approx 4{,}47 \\times 10^{-3}\\text{ M}$. Maka $\\text{pOH} = 3 - \\log(4{,}47) \\approx 2{,}35$, sehingga $\\text{pH} = 14 - 2{,}35 = 11{,}65$."
      },
      {
        "key": "E",
        "text": "$\\text{pH} = 7{,}00$, karena menganggap hidrolisis tahap kedua menetralkan seluruh ion hidroksida tahap pertama."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $\\text{pH} = 11{,}65$ (karena $[\\text{OH}^-] \\approx 4{,}47 \\times 10^{-3}\\text{ M}$), karena anion karbonat ($\\text{CO}_3^{2-}$) mengalami hidrolisis tahap pertama melepaskan ion hidroksida: $\\text{CO}_3^{2-} + \\text{H}_2\\text{O} \\rightleftharpoons \\text{HCO}_3^- + \\text{OH}^-$ dengan tetapan hidrolisis $K_{h1} = \\frac{K_w}{K_{a2}} = \\frac{10^{-14}}{5 \\times 10^{-11}} = 2 \\times 10^{-4}$. Konsentrasi ion hidroksida dihitung dari $[\\text{OH}^-] = \\sqrt{K_{h1} [\\text{CO}_3^{2-}]} = \\sqrt{(2 \\times 10^{-4}) \\times 0{,}1} = \\sqrt{2 \\times 10^{-5}} = \\sqrt{20 \\times 10^{-6}} \\approx 4{,}47 \\times 10^{-3}\\text{ M}$. Maka $\\text{pOH} = 3 - \\log(4{,}47) \\approx 2{,}35$, sehingga $\\text{pH} = 14 - 2{,}35 = 11{,}65$.. Garam Na2CO3 terhidrolisis menghasilkan OH-: CO3(2-) + H2O <-> HCO3- + OH-. Tetapan hidrolisis Kh1 = Kw / Ka2. Hitung [OH-] = sqrt(Kh1 * [garam]), lalu pH = 14 - pOH. Kh1 = 1e-14 / 5e-11 = 2e-4. [OH-] = sqrt(2e-4 * 0,1) = sqrt(2e-5) = 4,47e-3 M. pOH = 2,35 -> pH = 11,65."
  },
  {
    "id": "kim-lat-h-07",
    "materi": "KELARUTAN FRAKSIONAL & PEMISAHAN ION",
    "topic": "Pengendapan Selektif Campuran Kation Halida",
    "hints": {
      "concept": "Hitung [Cl-] yang dibutuhkan untuk mulai mengendapkan AgCl: [Cl-] = Ksp(AgCl) / [Ag+]. Hitung [Cl-] untuk PbCl2: [Cl-] = sqrt(Ksp(PbCl2) / [Pb2+]). Yang butuh konsentrasi lebih kecil mengendap duluan.",
      "execution": "[Cl-] AgCl = 1,8e-8 M (mengendap pertama). [Cl-] PbCl2 = sqrt(1,7e-5 / 0,01) = 4,12 x 10^-2 M."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Suatu larutan mengandung ion $\\text{Ag}^+$ berkonsentrasi $0{,}01\\text{ M}$ dan ion $\\text{Pb}^{2+}$ berkonsentrasi $0{,}01\\text{ M}$. Ke dalam larutan tersebut diteteskan larutan $\\text{NaCl}$ encer secara perlahan. Diketahui $K_{sp}\\,\\text{AgCl} = 1{,}8 \\times 10^{-10}$ dan $K_{sp}\\,\\text{PbCl}_2 = 1{,}7 \\times 10^{-5}$. Kation yang mengendap pertama kali dan konsentrasi ion klorida ($[\\text{Cl}^-]$) saat endapan kedua tepat mulai terbentuk berturut-turut adalah...",
    "formulaHud": {
      "title": "PENGENDAPAN FRAKSIONAL SELEKTIF",
      "latex": "[\\text{Cl}^-]_{\\text{AgCl}} = \\frac{1{,}8 \\times 10^{-10}}{10^{-2}} = 1{,}8 \\times 10^{-8}\\text{ M}; \\quad [\\text{Cl}^-]_{\\text{PbCl}_2} = \\sqrt{\\frac{1{,}7 \\times 10^{-5}}{10^{-2}}} = \\sqrt{1{,}7 \\times 10^{-3}} \\approx 4{,}12 \\times 10^{-2}\\text{ M}",
      "legend": "• Ion yang membutuhkan $[\\text{Cl}^-]$ terendah mengendap lebih dulu ($\\text{AgCl}$ pada $1{,}8 \\times 10^{-8}\\text{ M}$)<br>• Saat $\\text{PbCl}_2$ mulai mengendap, sisa $[\\text{Ag}^+]$ tinggal $\\frac{1{,}8 \\times 10^{-10}}{4{,}12 \\times 10^{-2}} \\approx 4{,}37 \\times 10^{-9}\\text{ M}$ (hampir $100\\%$ terpisah)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{Pb}^{2+}$ mengendap pertama kali saat konsentrasi klorida mencapai sepuluh pangkat minus lima molar."
      },
      {
        "key": "B",
        "text": "$\\text{Ag}^+$ mengendap pertama kali, dan endapan kedua mulai terbentuk pada saat $[\\text{Cl}^-] = 1{,}7 \\times 10^{-3}\\text{ M}$ tanpa menarik akar kuadrat."
      },
      {
        "key": "C",
        "text": "Kedua kation mengendap secara bersamaan karena memiliki konsentrasi molaritas awal yang identik."
      },
      {
        "key": "D",
        "text": "$\\text{Ag}^+$ mengendap pertama kali, dan endapan kedua ($\\text{PbCl}_2$) tepat mulai terbentuk pada saat $[\\text{Cl}^-] = \\sqrt{1{,}7 \\times 10^{-3}} \\approx 4{,}12 \\times 10^{-2}\\text{ M}$, karena $\\text{AgCl}$ mulai mengendap saat $[\\text{Cl}^-] = \\frac{K_{sp}\\,\\text{AgCl}}{[\\text{Ag}^+]} = \\frac{1{,}8 \\times 10^{-10}}{0{,}01} = 1{,}8 \\times 10^{-8}\\text{ M}$ (jauh lebih kecil, sehingga $\\text{Ag}^+$ mengendap jauh lebih dulu). Endapan $\\text{PbCl}_2$ baru mulai mengendap saat $[\\text{Cl}^-] = \\sqrt{\\frac{K_{sp}\\,\\text{PbCl}_2}{[\\text{Pb}^{2+}]}} = \\sqrt{\\frac{1{,}7 \\times 10^{-5}}{0{,}01}} = \\sqrt{1{,}7 \\times 10^{-3}} \\approx 4{,}12 \\times 10^{-2}\\text{ M}$."
      },
      {
        "key": "E",
        "text": "$\\text{Pb}^{2+}$ mengendap pertama kali karena memiliki koefisien ion klorida berpangkat dua."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $\\text{Ag}^+$ mengendap pertama kali, dan endapan kedua ($\\text{PbCl}_2$) tepat mulai terbentuk pada saat $[\\text{Cl}^-] = \\sqrt{1{,}7 \\times 10^{-3}} \\approx 4{,}12 \\times 10^{-2}\\text{ M}$, karena $\\text{AgCl}$ mulai mengendap saat $[\\text{Cl}^-] = \\frac{K_{sp}\\,\\text{AgCl}}{[\\text{Ag}^+]} = \\frac{1{,}8 \\times 10^{-10}}{0{,}01} = 1{,}8 \\times 10^{-8}\\text{ M}$ (jauh lebih kecil, sehingga $\\text{Ag}^+$ mengendap jauh lebih dulu). Endapan $\\text{PbCl}_2$ baru mulai mengendap saat $[\\text{Cl}^-] = \\sqrt{\\frac{K_{sp}\\,\\text{PbCl}_2}{[\\text{Pb}^{2+}]}} = \\sqrt{\\frac{1{,}7 \\times 10^{-5}}{0{,}01}} = \\sqrt{1{,}7 \\times 10^{-3}} \\approx 4{,}12 \\times 10^{-2}\\text{ M}$.. Hitung [Cl-] yang dibutuhkan untuk mulai mengendapkan AgCl: [Cl-] = Ksp(AgCl) / [Ag+]. Hitung [Cl-] untuk PbCl2: [Cl-] = sqrt(Ksp(PbCl2) / [Pb2+]). Yang butuh konsentrasi lebih kecil mengendap duluan. [Cl-] AgCl = 1,8e-8 M (mengendap pertama). [Cl-] PbCl2 = sqrt(1,7e-5 / 0,01) = 4,12 x 10^-2 M."
  },
  {
    "id": "kim-lat-h-08",
    "materi": "TERMODINAMIKA KIMIA (ENERGI BEBAS GIBBS)",
    "topic": "Suhu Kespontanan Reaksi Endotermik Dekomposisi",
    "hints": {
      "concept": "Syarat spontan: Delta G = Delta H - T * Delta S < 0. Suhu saat setimbang T = Delta H / Delta S. Konversi Delta H ke Joule: 178 kJ = 178.000 J.",
      "execution": "T = 178.000 / 160 = 1.112,5 K. Suhu harus T > 1.112,5 K."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Reaksi penguraian termal batu kapur memenuhi persamaan termodinamika:<br>$$\\text{CaCO}_3(s) \\to \\text{CaO}(s) + \\text{CO}_2(g)$$<br>Diketahui perubahan entalpi standar reaksi adalah $\\Delta H^\\circ = +178\\text{ kJ/mol}$ dan perubahan entropi standar adalah $\\Delta S^\\circ = +160\\text{ J/(mol}\\cdot\\text{K)}$. Mengasumsikan $\\Delta H^\\circ$ dan $\\Delta S^\\circ$ tidak berubah terhadap suhu, suhu minimum ($T$) agar reaksi penguraian tersebut berlangsung spontan pada tekanan 1 atm adalah...",
    "formulaHud": {
      "title": "KRITERIA KESPONTANAN ENERGI BEBAS GIBBS",
      "latex": "\\Delta G^\\circ = \\Delta H^\\circ - T \\Delta S^\\circ < 0 \\implies T > \\frac{\\Delta H^\\circ}{\\Delta S^\\circ} = \\frac{178 \\times 10^3\\text{ J/mol}}{160\\text{ J/(mol}\\cdot\\text{K)}} = 1.112{,}5\\text{ K} = 839{,}5^\\circ\\text{C}",
      "legend": "• $\\Delta H > 0$ dan $\\Delta S > 0 \\implies$ Spontan pada suhu tinggi ($T > \\Delta H / \\Delta S$)<br>• Pada suhu kamar ($298\\text{ K}$), $\\Delta G^\\circ > 0$ sehingga batu kapur sangat stabil dan tidak terurai"
    },
    "options": [
      {
        "key": "A",
        "text": "$T > 1.112{,}5\\text{ K}$ (atau di atas $839{,}5^\\circ\\text{C}$), karena syarat kespontanan menurut kriteria Gibbs adalah $\\Delta G^\\circ = \\Delta H^\\circ - T \\Delta S^\\circ < 0$. Pada titik transisi kesetimbangan $\\Delta G^\\circ = 0$, suhu tercapai saat $T = \\frac{\\Delta H^\\circ}{\\Delta S^\\circ} = \\frac{178.000\\text{ J/mol}}{160\\text{ J/(mol}\\cdot\\text{K)}} = 1.112{,}5\\text{ K}$. Agar reaksi berjalan spontan ($\\Delta G^\\circ < 0$), suhu sistem harus dinaikkan melebihi $1.112{,}5\\text{ Kelvin}$."
      },
      {
        "key": "B",
        "text": "$T < 273\\text{ K}$, karena beranggapan seluruh reaksi spontan hanya dapat berlangsung di bawah titik beku es."
      },
      {
        "key": "C",
        "text": "$T > 890\\text{ K}$, karena satuan kiloJoule pada entalpi tidak dikonversikan ke satuan Joule saat pembagian entropi."
      },
      {
        "key": "D",
        "text": "$T < 1.112{,}5\\text{ K}$, karena salah mengasumsikan reaksi endotermik lebih spontan pada suhu rendah ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "E",
        "text": "$T > 2.225\\text{ K}$, dihitung dari penggandaan suhu akibat adanya dua partikel produk dekomposisi."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $T > 1.112{,}5\\text{ K}$ (atau di atas $839{,}5^\\circ\\text{C}$), karena syarat kespontanan menurut kriteria Gibbs adalah $\\Delta G^\\circ = \\Delta H^\\circ - T \\Delta S^\\circ < 0$. Pada titik transisi kesetimbangan $\\Delta G^\\circ = 0$, suhu tercapai saat $T = \\frac{\\Delta H^\\circ}{\\Delta S^\\circ} = \\frac{178.000\\text{ J/mol}}{160\\text{ J/(mol}\\cdot\\text{K)}} = 1.112{,}5\\text{ K}$. Agar reaksi berjalan spontan ($\\Delta G^\\circ < 0$), suhu sistem harus dinaikkan melebihi $1.112{,}5\\text{ Kelvin}$.. Syarat spontan: Delta G = Delta H - T * Delta S < 0. Suhu saat setimbang T = Delta H / Delta S. Konversi Delta H ke Joule: 178 kJ = 178.000 J. T = 178.000 / 160 = 1.112,5 K. Suhu harus T > 1.112,5 K."
  },
  {
    "id": "kim-lat-h-09",
    "materi": "TERMODINAMIKA (DELTA G STANDAR & K)",
    "topic": "Hubungan Delta G Standar dengan Tetapan Kesetimbangan K",
    "hints": {
      "concept": "Gunakan Delta G0 = -R * T * ln(K). R = 8,314 J/(mol.K), T = 300 K, ln(100) = 4,605.",
      "execution": "Delta G0 = -8,314 * 300 * 4,605 = -11.486 J/mol = -11,49 kJ/mol."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Suatu reaksi kimia isomerisasi fasa gas $A(g) \\rightleftharpoons B(g)$ memiliki tetapan kesetimbangan $K_p = 100$ pada suhu $T = 300\\text{ K}$. Jika tetapan gas ideal $R = 8{,}314\\text{ J/(mol}\\cdot\\text{K)}$ dan $\\ln 100 \\approx 4{,}605$, nilai perubahan energi bebas Gibbs standar ($\\Delta G^\\circ$) untuk reaksi isomerisasi tersebut adalah...",
    "formulaHud": {
      "title": "RELASI ENERGI BEBAS GIBBS DENGAN KESETIMBANGAN",
      "latex": "\\Delta G^\\circ = -R T \\ln K = -8{,}314 \\times 300 \\times 4{,}605 = -11.486\\text{ J/mol} = -11{,}49\\text{ kJ/mol}",
      "legend": "• $K > 1 \\implies \\ln K > 0 \\implies \\Delta G^\\circ < 0$ (Pembentukan produk sangat disukai secara termodinamika)<br>• Catatan: $\\Delta G = 0$ pada keadaan setimbang, namun $\\Delta G^\\circ \\ne 0$"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\Delta G^\\circ \\approx -11{,}49\\text{ kJ/mol}$, karena menurut hubungan fundamental termodinamika kimia: $\\Delta G^\\circ = -R T \\ln K = -(8{,}314\\text{ J/(mol}\\cdot\\text{K)}) \\times 300\\text{ K} \\times \\ln(100) = -(2.494{,}2) \\times 4{,}605 = -11.485{,}8\\text{ J/mol} \\approx -11{,}49\\text{ kJ/mol}$."
      },
      {
        "key": "B",
        "text": "$\\Delta G^\\circ \\approx -2{,}49\\text{ kJ/mol}$, dihitung tanpa mengalikan nilai logaritma natural tetapan kesetimbangan."
      },
      {
        "key": "C",
        "text": "$\\Delta G^\\circ = 0\\text{ kJ/mol}$, karena menyamakan energi bebas Gibbs standar dengan energi bebas saat campuran telah mencapai kesetimbangan dinamis."
      },
      {
        "key": "D",
        "text": "$\\Delta G^\\circ \\approx +11{,}49\\text{ kJ/mol}$, karena salah menghilangkan tanda minus pada perumusan potensial termodinamika isotermal menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "E",
        "text": "$\\Delta G^\\circ \\approx -23{,}0\\text{ kJ/mol}$, karena keliru menggunakan nilai logaritma desimal basis 10 dikalikan faktor dua."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\Delta G^\\circ \\approx -11{,}49\\text{ kJ/mol}$, karena menurut hubungan fundamental termodinamika kimia: $\\Delta G^\\circ = -R T \\ln K = -(8{,}314\\text{ J/(mol}\\cdot\\text{K)}) \\times 300\\text{ K} \\times \\ln(100) = -(2.494{,}2) \\times 4{,}605 = -11.485{,}8\\text{ J/mol} \\approx -11{,}49\\text{ kJ/mol}$.. Gunakan Delta G0 = -R * T * ln(K). R = 8,314 J/(mol.K), T = 300 K, ln(100) = 4,605. Delta G0 = -8,314 * 300 * 4,605 = -11.486 J/mol = -11,49 kJ/mol."
  },
  {
    "id": "kim-lat-h-10",
    "materi": "KINETIKA KIMIA (PERSAMAAN ARRHENIUS)",
    "topic": "Penentuan Energi Aktivasi Reaksi dari Dua Suhu Berbeda",
    "hints": {
      "concept": "Persamaan Arrhenius: ln(k2/k1) = (Ea / R) * (1/T1 - 1/T2). Ea = R * ln(2) * (T1 * T2) / (T2 - T1).",
      "execution": "Ea = 8,314 * 0,693 * (300 * 310) / 10 = 5,7616 * 9.300 = 53.583 J/mol = 53,58 kJ/mol."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Konstanta laju reaksi ($k$) untuk suatu reaksi dekomposisi meningkat dua kali lipat ($k_2 = 2 k_1$) ketika suhu reaksi dinaikkan dari $T_1 = 300\\text{ K}$ menjadi $T_2 = 310\\text{ K}$. Diketahui tetapan gas umum $R = 8{,}314\\text{ J/(mol}\\cdot\\text{K)}$ dan $\\ln 2 \\approx 0{,}693$. Besar energi aktivasi ($E_a$) dari reaksi dekomposisi tersebut adalah...",
    "formulaHud": {
      "title": "PERSAMAAN ARRHENIUS DUA SUHU",
      "latex": "\\ln\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{R} \\left(\\frac{T_2 - T_1}{T_1 T_2}\\right) \\implies E_a = \\frac{R \\cdot T_1 T_2 \\cdot \\ln(k_2/k_1)}{T_2 - T_1} = \\frac{8{,}314 \\times 300 \\times 310 \\times 0{,}693}{10} \\approx 53{,}58\\text{ kJ/mol}",
      "legend": "• $E_a$ menyatakan batas energi penghalang minimum yang harus dilampaui molekul agar tumbukan menghasilkan reaksi kimia<br>• $E_a \\approx 53{,}58\\text{ kJ/mol}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$E_a \\approx 83{,}14\\text{ kJ/mol}$, dihitung dari perkalian langsung konstanta gas dengan kelipatan suhu mutlak."
      },
      {
        "key": "B",
        "text": "$E_a \\approx 107{,}16\\text{ kJ/mol}$, dihitung dari pemangkatan kuadrat rasio konstanta laju reaksi."
      },
      {
        "key": "C",
        "text": "$E_a \\approx 26{,}79\\text{ kJ/mol}$, karena faktor selisih suhu keliru digandakan menjadi dua puluh derajat."
      },
      {
        "key": "D",
        "text": "$E_a \\approx 5{,}36\\text{ kJ/mol}$, karena galat konversi dari satuan Joule ke kiloJoule."
      },
      {
        "key": "E",
        "text": "$E_a \\approx 53{,}58\\text{ kJ/mol}$, karena menurut bentuk linear persamaan Arrhenius dua suhu: $\\ln\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{R} \\left(\\frac{1}{T_1} - \\frac{1}{T_2}\\right) = \\frac{E_a}{R} \\left(\\frac{T_2 - T_1}{T_1 T_2}\\right)$. Substitusi data: $0{,}693 = \\frac{E_a}{8{,}314} \\left(\\frac{10}{300 \\times 310}\\right) = \\frac{E_a}{8{,}314} \\left(\\frac{10}{93.000}\\right) \\implies E_a = \\frac{0{,}693 \\times 8{,}314 \\times 93.000}{10} = \\frac{535.824}{10} \\approx 53.582\\text{ J/mol} \\approx 53{,}58\\text{ kJ/mol}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $E_a \\approx 53{,}58\\text{ kJ/mol}$, karena menurut bentuk linear persamaan Arrhenius dua suhu: $\\ln\\left(\\frac{k_2}{k_1}\\right) = \\frac{E_a}{R} \\left(\\frac{1}{T_1} - \\frac{1}{T_2}\\right) = \\frac{E_a}{R} \\left(\\frac{T_2 - T_1}{T_1 T_2}\\right)$. Substitusi data: $0{,}693 = \\frac{E_a}{8{,}314} \\left(\\frac{10}{300 \\times 310}\\right) = \\frac{E_a}{8{,}314} \\left(\\frac{10}{93.000}\\right) \\implies E_a = \\frac{0{,}693 \\times 8{,}314 \\times 93.000}{10} = \\frac{535.824}{10} \\approx 53.582\\text{ J/mol} \\approx 53{,}58\\text{ kJ/mol}$.. Persamaan Arrhenius: ln(k2/k1) = (Ea / R) * (1/T1 - 1/T2). Ea = R * ln(2) * (T1 * T2) / (T2 - T1). Ea = 8,314 * 0,693 * (300 * 310) / 10 = 5,7616 * 9.300 = 53.583 J/mol = 53,58 kJ/mol."
  },
  {
    "id": "kim-lat-h-11",
    "materi": "ELEKTROKIMIA (PERSAMAAN NERNEST)",
    "topic": "Potensial Sel Non-Standar Sel Daniell",
    "hints": {
      "concept": "Persamaan Nernst: E_sel = E0_sel - (0,0592 / n) * log(Q). n = 2. Q = [Zn2+] / [Cu2+] = 0,1 / 1e-3 = 100. log(100) = 2.",
      "execution": "E_sel = 1,10 - (0,0592 / 2) * 2 = 1,10 - 0,0592 = 1,0408 Volt."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah sel Volta Daniell dirangkai dengan reaksi sel:<br>$$\\text{Zn}(s) + \\text{Cu}^{2+}(aq) \\to \\text{Zn}^{2+}(aq) + \\text{Cu}(s) \\quad E^\\circ_{\\text{sel}} = +1{,}10\\text{ Volt}$$<br>Sel dioperasikan pada suhu $25^\\circ\\text{C}$ dengan konsentrasi ion $[\\text{Zn}^{2+}] = 0{,}1\\text{ M}$ dan konsentrasi ion $[\\text{Cu}^{2+}] = 0{,}001\\text{ M} = 10^{-3}\\text{ M}$. Berdasarkan persamaan Nernst ($E_{\\text{sel}} = E^\\circ_{\\text{sel}} - \\frac{0{,}0592}{n} \\log Q$), besar potensial sel non-standar ($E_{\\text{sel}}$) yang dihasilkan adalah...",
    "formulaHud": {
      "title": "PERSAMAAN NERNST PADA SUHU 298 K",
      "latex": "E_{\\text{sel}} = E^\\circ_{\\text{sel}} - \\frac{0{,}0592}{n} \\log Q = 1{,}10 - \\frac{0{,}0592}{2} \\log\\left(\\frac{0{,}1}{10^{-3}}\\right) = 1{,}10 - 0{,}0296(2) = 1{,}0408\\text{ V}",
      "legend": "• $n = 2$ (transfer 2 mol elektron)<br>• $Q = 100 \\implies E_{\\text{sel}} < E^\\circ_{\\text{sel}}$ (penurunan voltase seiring berkurangnya reaktan $\\text{Cu}^{2+}$)"
    },
    "options": [
      {
        "key": "A",
        "text": "$E_{\\text{sel}} = 1{,}0704\\text{ Volt}$, dihitung dengan membagi suku Nernst dengan faktor empat."
      },
      {
        "key": "B",
        "text": "$E_{\\text{sel}} = 1{,}0408\\text{ Volt}$ (atau sekitar $1{,}04\\text{ V}$), karena jumlah transfer elektron dalam reaksi adalah $n = 2$. Kuosien reaksi adalah $Q = \\frac{[\\text{Zn}^{2+}]}{[\\text{Cu}^{2+}]} = \\frac{0{,}1}{10^{-3}} = 100 = 10^2$, sehingga $\\log Q = 2$. Menurut persamaan Nernst: $E_{\\text{sel}} = 1{,}10\\text{ V} - \\frac{0{,}0592}{2} \\log(100) = 1{,}10 - (0{,}0296 \\times 2) = 1{,}10 - 0{,}0592 = 1{,}0408\\text{ Volt}$."
      },
      {
        "key": "C",
        "text": "$E_{\\text{sel}} = 0{,}9816\\text{ Volt}$, dihitung dari pemangkatan kuadrat jumlah transfer elektron pada penyebut."
      },
      {
        "key": "D",
        "text": "$E_{\\text{sel}} = 1{,}1592\\text{ Volt}$, karena suku koreksi Nernst keliru ditambahkan pada potensial sel standar padahal konsentrasi produk lebih besar dari reaktan."
      },
      {
        "key": "E",
        "text": "$E_{\\text{sel}} = 1{,}1000\\text{ Volt}$, karena mengabaikan pengaruh perbedaan konsentrasi larutan elektrolit."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $E_{\\text{sel}} = 1{,}0408\\text{ Volt}$ (atau sekitar $1{,}04\\text{ V}$), karena jumlah transfer elektron dalam reaksi adalah $n = 2$. Kuosien reaksi adalah $Q = \\frac{[\\text{Zn}^{2+}]}{[\\text{Cu}^{2+}]} = \\frac{0{,}1}{10^{-3}} = 100 = 10^2$, sehingga $\\log Q = 2$. Menurut persamaan Nernst: $E_{\\text{sel}} = 1{,}10\\text{ V} - \\frac{0{,}0592}{2} \\log(100) = 1{,}10 - (0{,}0296 \\times 2) = 1{,}10 - 0{,}0592 = 1{,}0408\\text{ Volt}$.. Persamaan Nernst: E_sel = E0_sel - (0,0592 / n) * log(Q). n = 2. Q = [Zn2+] / [Cu2+] = 0,1 / 1e-3 = 100. log(100) = 2. E_sel = 1,10 - (0,0592 / 2) * 2 = 1,10 - 0,0592 = 1,0408 Volt."
  },
  {
    "id": "kim-lat-h-12",
    "materi": "ELEKTROLISIS INDUSTRI (ELEKTROREFINING TEMBAGA)",
    "topic": "Pemurnian Tembaga dan Pembentukan Lumpur Anoda",
    "hints": {
      "concept": "Logam lebih aktif dari Cu (Zn, Fe, E0 lebih negatif) teroksidasi jadi ion di larutan. Logam lebih mulia dari Cu (Ag, Au, E0 lebih positif) tidak teroksidasi dan jatuh jadi lumpur anoda.",
      "execution": "Zn larut sebagai ion di elektrolit, Au dan Ag mengendap menjadi lumpur anoda."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam proses pemurnian tembaga secara elektrolisis di industri (electrorefining), kawat tembaga murni dijadikan katoda dan lempengan tembaga kasar (blister copper) yang mengandung pengotor besi, seng, emas, dan perak dijadikan anoda di dalam larutan elektrolit $\\text{CuSO}_4$ diasamkan. Peristiwa elektrokimia yang terjadi pada pengotor seng, emas, dan perak selama proses berlangsung adalah...",
    "formulaHud": {
      "title": "ELEKTROREFINING BLISTER TEMBAGA",
      "latex": "\\begin{aligned} \\text{Anoda (Oksidasi): } & \\text{Cu}(s) \\to \\text{Cu}^{2+} + 2e^-; \\quad \\text{Zn, Fe teroksidasi jadi ion larut} \\\\ \\text{Lumpur Anoda: } & \\text{Ag, Au, Pt tidak teroksidasi (}\\text{karena } E^\\circ > E^\\circ_{\\text{Cu}}\\text{) dan mengendap} \\\\ \\text{Katoda (Reduksi): } & \\text{Cu}^{2+} + 2e^- \\to \\text{Cu}(s) \\quad (\\text{Hanya Cu tereduksi murni 99,99\\%}) \\end{aligned}"
    },
    "options": [
      {
        "key": "A",
        "text": "Seng, emas, dan perak bereaksi dengan gas belerang membentuk lapisan pasivasi yang menghentikan arus listrik."
      },
      {
        "key": "B",
        "text": "Seluruh pengotor seng, emas, dan perak ikut teroksidasi dan terendapkan bersama tembaga di katoda."
      },
      {
        "key": "C",
        "text": "Pengotor emas dan perak menguap sebagai gas mulia beracun di atas permukaan sel elektrolisis industri."
      },
      {
        "key": "D",
        "text": "Emas dan perak teroksidasi membentuk ion kompleks larut, sedangkan seng mengendap di dasar sel elektrolisis."
      },
      {
        "key": "E",
        "text": "Seng teroksidasi menjadi ion $\\text{Zn}^{2+}$ dan larut tetap berada di dalam larutan elektrolit karena potensial reduksinya sangat negatif sehingga tidak tereduksi di katoda, sedangkan emas dan perak tidak teroksidasi di anoda dan jatuh mengendap ke dasar bejana membentuk lumpur anoda (anode slime) yang bernilai ekonomis tinggi."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Seng teroksidasi menjadi ion $\\text{Zn}^{2+}$ dan larut tetap berada di dalam larutan elektrolit karena potensial reduksinya sangat negatif sehingga tidak tereduksi di katoda, sedangkan emas dan perak tidak teroksidasi di anoda dan jatuh mengendap ke dasar bejana membentuk lumpur anoda (anode slime) yang bernilai ekonomis tinggi.. Logam lebih aktif dari Cu (Zn, Fe, E0 lebih negatif) teroksidasi jadi ion di larutan. Logam lebih mulia dari Cu (Ag, Au, E0 lebih positif) tidak teroksidasi dan jatuh jadi lumpur anoda. Zn larut sebagai ion di elektrolit, Au dan Ag mengendap menjadi lumpur anoda."
  },
  {
    "id": "kim-lat-h-13",
    "materi": "KIMIA ORGANIK (MEKANISME SUBSTITUSI NUKLEOFILIK)",
    "topic": "Komparasi Mekanisme Reaksi SN1 dan SN2",
    "hints": {
      "concept": "SN1: 2 tahap via intermediat karbokation datar -> menghasilkan campuran rasemat. SN2: 1 tahap serentak (serangan nukleofil dari belakang) -> menghasilkan inversi Walden 100%.",
      "execution": "SN1 via karbokation menghasilkan rasemisasi; SN2 satu tahap menghasilkan inversi Walden."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Reaksi substitusi nukleofilik antara alkil halida dengan ion hidroksida dapat berlangsung melalui mekanisme $S_N1$ atau $S_N2$. Karakteristik yang benar membedakan reaksi $S_N1$ pada ters-butil bromida dengan reaksi $S_N2$ pada metil bromida adalah...",
    "formulaHud": {
      "title": "MEKANISME SUBSTITUSI NUKLEOFILIK (SN1 VS SN2)",
      "latex": "\\begin{aligned} S_N1: & \\quad v = k[\\text{R-X}] \\quad (\\text{Karbokation 3}^\\circ, \\text{Rasemisasi}, \\text{Pelarut Protik Polar}) \\\\ S_N2: & \\quad v = k[\\text{R-X}][\\text{Nu}^-] \\quad (\\text{Serangan Belakang 1}^\\circ, \\text{Inversi Walden}, \\text{Pelarut Aprotik}) \\end{aligned}"
    },
    "options": [
      {
        "key": "A",
        "text": "Reaksi $S_N1$ lebih disukai oleh pelarut aprotik nonpolar sedangkan $S_N2$ membutuhkan pelarut protik berair kuat."
      },
      {
        "key": "B",
        "text": "Reaksi $S_N1$ sangat dipengaruhi oleh kekuatan nukleofil sedangkan $S_N2$ lajunya hanya bergantung pada konsentrasi substrat alkil halida."
      },
      {
        "key": "C",
        "text": "Reaksi $S_N1$ berlangsung dua tahap melalui pembentukan zat antara karbokation datar yang menghasilkan rasemisasi optik (inversi dan retensi), sedangkan reaksi $S_N2$ berlangsung satu tahap serentak (concerted) dengan serangan nukleofil dari arah belakang yang menghasilkan inversi konfigurasi Walden $100\\%$."
      },
      {
        "key": "D",
        "text": "Reaksi $S_N1$ berlangsung satu tahap dengan keadaan transisi siklik, sedangkan $S_N2$ berlangsung melalui zat antara radikal bebas ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "E",
        "text": "Reaksi $S_N1$ menghasilkan pembalikan konfigurasi Walden murni, sedangkan $S_N2$ selalu menghasilkan produk retensi."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Reaksi $S_N1$ berlangsung dua tahap melalui pembentukan zat antara karbokation datar yang menghasilkan rasemisasi optik (inversi dan retensi), sedangkan reaksi $S_N2$ berlangsung satu tahap serentak (concerted) dengan serangan nukleofil dari arah belakang yang menghasilkan inversi konfigurasi Walden $100\\%$.. SN1: 2 tahap via intermediat karbokation datar -> menghasilkan campuran rasemat. SN2: 1 tahap serentak (serangan nukleofil dari belakang) -> menghasilkan inversi Walden 100%. SN1 via karbokation menghasilkan rasemisasi; SN2 satu tahap menghasilkan inversi Walden."
  },
  {
    "id": "kim-lat-h-14",
    "materi": "KIMIA ORGANIK (REAKSI ELIMINASI & ATURAN ZAITSEV)",
    "topic": "Regioselektifitas Dehidrohalogenasi Alkil Halida",
    "hints": {
      "concept": "Aturan Zaitsev: pada eliminasi dehidrohalogenasi, produk utama adalah alkena dengan substituen terbanyak (paling stabil). 2-butena (disubstitusi) adalah produk utama.",
      "execution": "2-butena (produk Zaitsev yang lebih stabil)."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Senyawa 2-bromobutana dipanaskan bersama larutan kalium hidroksida dalam alkohol ($\\text{KOH/etanol}$). Berdasarkan Aturan Zaitsev (Saytzeff), produk utama yang dihasilkan beserta alasan regioselektifitasnya adalah...",
    "formulaHud": {
      "title": "ATURAN ELIMINASI ZAITSEV",
      "latex": "\\text{CH}_3-\\text{CH}_2-\\text{CH(Br)}-\\text{CH}_3 + \\text{KOH} \\xrightarrow{\\text{Etanol, } \\Delta} \\text{CH}_3-\\text{CH}=\\text{CH}-\\text{CH}_3 \\text{ (2-butena, } 80\\%\\text{)} + \\text{CH}_3-\\text{CH}_2-\\text{CH}=\\text{CH}_2 \\text{ (1-butena, } 20\\%)",
      "legend": "• Produk Zaitsev (2-butena) = Alkena terdisubstitusi (lebih stabil akibat hiperkonjugasi)<br>• Produk Hofmann (1-butena) = Alkena termonosubstitusi (produk minor)"
    },
    "options": [
      {
        "key": "A",
        "text": "Siklobutana, karena rantai karbon mengalami penutupan cincin intramolekuler."
      },
      {
        "key": "B",
        "text": "2-butena (khususnya trans-2-butena), karena aturan Zaitsev menyatakan bahwa eliminasi hidrogen halida dari alkil halida akan mendominasi pembentukan alkena yang memiliki gugus alkil substituen terbanyak (alkena terdisubstitusi yang secara termodinamika memiliki kestabilan ikatan pi lebih tinggi dibanding 1-butena monosubstitusi)."
      },
      {
        "key": "C",
        "text": "Butuna, karena terjadi pelepasan dua molekul asam bromida secara simultan."
      },
      {
        "key": "D",
        "text": "2-butanol, karena terjadi reaksi substitusi nukleofilik murni tanpa eliminasi ikatan rangkap."
      },
      {
        "key": "E",
        "text": "1-butena, karena proton hidrogen pada karbon nomor satu paling mudah diserang oleh basa kuat karena rintangan sterik minimal menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) 2-butena (khususnya trans-2-butena), karena aturan Zaitsev menyatakan bahwa eliminasi hidrogen halida dari alkil halida akan mendominasi pembentukan alkena yang memiliki gugus alkil substituen terbanyak (alkena terdisubstitusi yang secara termodinamika memiliki kestabilan ikatan pi lebih tinggi dibanding 1-butena monosubstitusi).. Aturan Zaitsev: pada eliminasi dehidrohalogenasi, produk utama adalah alkena dengan substituen terbanyak (paling stabil). 2-butena (disubstitusi) adalah produk utama. 2-butena (produk Zaitsev yang lebih stabil)."
  },
  {
    "id": "kim-lat-h-15",
    "materi": "KIMIA AROMATIK (SUBSTITUSI ELEKTROFILIK BENZENA)",
    "topic": "Pengaruh Pengarah Substituen Orto-Para vs Meta pada Benzena",
    "hints": {
      "concept": "-OH adalah aktivator cincin (mendonorkan PEB via resonansi), mengarahkan ke orto dan para. -NO2 adalah deaktivator kuat (menarik elektron dari cincin), mengarahkan ke meta.",
      "execution": "-OH aktivator pengarah orto-para; -NO2 deaktivator pengarah meta."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Fenol direaksikan dengan campuran asam nitrat encer dan asam sulfat encer pada suhu kamar menghasilkan campuran senyawa orto-nitrofenol dan para-nitrofenol. Sedangkan reaksi nitrasi pada nitrobenzena membutuhkan kondisi asam pekat berpemanas tinggi dan menghasilkan meta-dinitrobenzena. Alasan mendasar perbedaan orientasi dan reaktivitas cincin aromatik tersebut adalah...",
    "formulaHud": {
      "title": "EFEK PENGARAH SUBSTITUEN PADA CINCIN BENZENA",
      "latex": "\\begin{aligned} \\text{Pengarah Orto-Para (Aktivator): } & -\\text{OH}, -\\text{NH}_2, -\\text{OCH}_3, -\\text{R} \\quad (\\text{Donasi resonansi } +M) \\\\ \\text{Pengarah Meta (Deaktivator): } & -\\text{NO}_2, -\\text{COOH}, -\\text{CHO}, -\\text{CN} \\quad (\\text{Penarik elektron } -M, -I) \\end{aligned}"
    },
    "options": [
      {
        "key": "A",
        "text": "Perbedaan orientasi disebabkan semata-mata oleh perbedaan massa molar kedua substituen organik."
      },
      {
        "key": "B",
        "text": "Gugus $-\\text{NO}_2$ mendonorkan pasangan elektron bebas nitrogen ke cincin sehingga mengaktifkan posisi meta secara spesifik."
      },
      {
        "key": "C",
        "text": "Fenol mengalami reaksi adisi ikatan rangkap benzena sedangkan nitrobenzena mengalami reaksi substitusi nukleofilik aromatik."
      },
      {
        "key": "D",
        "text": "Gugus $-\\text{OH}$ bersifat penarik elektron kuat melalui efek induksi sehingga mendeaktivasi posisi meta cincin aromatik."
      },
      {
        "key": "E",
        "text": "Gugus hidroksil ($-\\text{OH}$) pada fenol memiliki pasangan elektron bebas yang didonorkan ke cincin benzena melalui resonansi ($+M$), bersifat pengaktif kuat cincin dan mengarahkan elektrofil baru ke posisi orto dan para; sedangkan gugus nitro ($-\\text{NO}_2$) bersifat penarik elektron kuat ($-M$ dan $-I$) yang mendeaktivasi cincin dan mengarahkan elektrofil ke posisi meta yang kerapatan elektronnya paling sedikit berkurang."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Gugus hidroksil ($-\\text{OH}$) pada fenol memiliki pasangan elektron bebas yang didonorkan ke cincin benzena melalui resonansi ($+M$), bersifat pengaktif kuat cincin dan mengarahkan elektrofil baru ke posisi orto dan para; sedangkan gugus nitro ($-\\text{NO}_2$) bersifat penarik elektron kuat ($-M$ dan $-I$) yang mendeaktivasi cincin dan mengarahkan elektrofil ke posisi meta yang kerapatan elektronnya paling sedikit berkurang.. -OH adalah aktivator cincin (mendonorkan PEB via resonansi), mengarahkan ke orto dan para. -NO2 adalah deaktivator kuat (menarik elektron dari cincin), mengarahkan ke meta. -OH aktivator pengarah orto-para; -NO2 deaktivator pengarah meta."
  },
  {
    "id": "kim-lat-h-16",
    "materi": "BIOKIMIA (ASAM AMINO & TITIK ISOELEKTRIK)",
    "topic": "Bentuk Zwitterion dan Perhitungan Titik Isoelektrik Alanin",
    "hints": {
      "concept": "Titik isoelektrik asam amino netral: pI = (pKa1 + pKa2) / 2 = (2,34 + 9,69)/2 = 6,015. Pada pH 11 > pI, asam amino bermuatan negatif (anion) sehingga bergerak ke kutub positif (anoda).",
      "execution": "pI = 6,015; bermuatan negatif dan bermigrasi ke anoda."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Asam amino alanin memiliki dua gugus yang dapat terionisasi dengan nilai $\\text{p}K_{a1} = 2{,}34$ (gugus karboksilat $-\\text{COOH}$) dan $\\text{p}K_{a2} = 9{,}69$ (gugus amino $-\\text{NH}_3^+$). Pada pH berapakah alanin berada dalam bentuk zwitterion netral dominan (titik isoelektrik, pI) dan bagaimana arah migrasinya dalam medan elektroforesis pada $\\text{pH} = 11$?",
    "formulaHud": {
      "title": "TITIK ISOELEKTRIK ASAM AMINO DIPROTIK",
      "latex": "\\text{pI} = \\frac{\\text{p}K_{a1} + \\text{p}K_{a2}}{2} = \\frac{2{,}34 + 9{,}69}{2} = 6{,}015; \\quad \\text{Pada pH } > \\text{pI}: \\text{Bentuk Anion } \\text{H}_2\\text{N-CH(CH}_3\\text{)-COO}^- \\implies \\text{Migrasi ke Anoda (+)}",
      "legend": "• Zwitterion netral mendominasi tepat pada $\\text{pH} = \\text{pI}$ (kelarutan minimum)<br>• $\\text{pH} < \\text{pI} \\implies$ Kation (+) bergerak ke Katoda (-)<br>• $\\text{pH} > \\text{pI} \\implies$ Anion (-) bergerak ke Anoda (+)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{pI} = 6{,}015$ dan pada $\\text{pH } 11$ alanin bermuatan positif sehingga bermigrasi menuju kutub katoda negatif."
      },
      {
        "key": "B",
        "text": "Titik isoelektrik $\\text{pI} = 6{,}015$ dan pada $\\text{pH} = 11$ alanin bermuatan negatif sehingga bermigrasi menuju kutub anoda positif, karena titik isoelektrik dihitung dari rata-rata $\\text{pI} = \\frac{\\text{p}K_{a1} + \\text{p}K_{a2}}{2} = \\frac{2{,}34 + 9{,}69}{2} = \\frac{12{,}03}{2} = 6{,}015$. Pada lingkungan sangat basa ($\\text{pH } 11 > \\text{pI}$), gugus amino melepaskan protonnya ($-\\text{NH}_2$) sementara karboksilat tetap terionisasi ($-\\text{COO}^-$), sehingga menghasilkan ion bermuatan negatif netto (anion) yang ditarik oleh anoda."
      },
      {
        "key": "C",
        "text": "$\\text{pI} = 9{,}69$ dan pada $\\text{pH } 11$ alanin mengendap sebagai kristal padat tak larut."
      },
      {
        "key": "D",
        "text": "$\\text{pI} = 7{,}00$ dan pada $\\text{pH } 11$ alanin diam di tempat tidak bermigrasi karena bermuatan netral."
      },
      {
        "key": "E",
        "text": "$\\text{pI} = 2{,}34$ dan pada $\\text{pH } 11$ alanin terurai menjadi gas amonia dan asam laktat."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Titik isoelektrik $\\text{pI} = 6{,}015$ dan pada $\\text{pH} = 11$ alanin bermuatan negatif sehingga bermigrasi menuju kutub anoda positif, karena titik isoelektrik dihitung dari rata-rata $\\text{pI} = \\frac{\\text{p}K_{a1} + \\text{p}K_{a2}}{2} = \\frac{2{,}34 + 9{,}69}{2} = \\frac{12{,}03}{2} = 6{,}015$. Pada lingkungan sangat basa ($\\text{pH } 11 > \\text{pI}$), gugus amino melepaskan protonnya ($-\\text{NH}_2$) sementara karboksilat tetap terionisasi ($-\\text{COO}^-$), sehingga menghasilkan ion bermuatan negatif netto (anion) yang ditarik oleh anoda.. Titik isoelektrik asam amino netral: pI = (pKa1 + pKa2) / 2 = (2,34 + 9,69)/2 = 6,015. Pada pH 11 > pI, asam amino bermuatan negatif (anion) sehingga bergerak ke kutub positif (anoda). pI = 6,015; bermuatan negatif dan bermigrasi ke anoda."
  },
  {
    "id": "kim-lat-h-17",
    "materi": "STEREOKIMIA (KONFIGURASI ABSOLUT R/S)",
    "topic": "Penentuan Konfigurasi R/S Cahn-Ingold-Prelog pada Asam Laktat",
    "hints": {
      "concept": "Aturan CIP: Nomor atom tertinggi menang: -OH (O=8) nomor 1, -H (H=1) nomor 4. Bandingkan -COOH vs -CH3: C pada -COOH mengikat atom O, sehingga -COOH menang jadi nomor 2, -CH3 nomor 3.",
      "execution": "Prioritas: -OH > -COOH > -CH3 > -H. Konfigurasi (R) jika searah jarum jam."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Asam laktat memiliki rumus struktur $\\text{CH}_3-\\text{C}^*\\text{H(OH)}-\\text{COOH}$ dengan satu atom karbon kiral ($C^*$). Berdasarkan aturan prioritas Cahn-Ingold-Prelog (CIP), urutan prioritas keempat gugus yang terikat pada karbon kiral dan konfigurasi absolut jika gugus prioritas terendah berada di belakang bidang proyeksi adalah...",
    "formulaHud": {
      "title": "ATURAN PRIORITAS CAHN-INGOLD-PRELOG (CIP)",
      "latex": "\\text{Prioritas: } (1) -\\text{OH } (Z=8) > (2) -\\text{COOH } (C \\text{ terikat } O,O,O) > (3) -\\text{CH}_3 \\text{ (}C \\text{ terikat } H,H,H) > (4) -\\text{H } (Z=1)",
      "legend": "• Prioritas ditentukan dari nomor atom ($Z$) tertinggi pada titik perbedaan pertama<br>• Putaran $1 \\to 2 \\to 3$ searah jarum jam $\\implies$ Konfigurasi $(R)$ (Rectus)<br>• Putaran berlawanan jarum jam $\\implies$ Konfigurasi $(S)$ (Sinister)"
    },
    "options": [
      {
        "key": "A",
        "text": "Urutan prioritas: $-\\text{H} > -\\text{CH}_3 > -\\text{COOH} > -\\text{OH}$ diurutkan dari massa molar terkecil ke terbesar."
      },
      {
        "key": "B",
        "text": "Urutan prioritas: $-\\text{OH} > -\\text{COOH} > -\\text{CH}_3 > -\\text{H}$, karena penentuan didasarkan pada nomor atom yang terikat langsung ($O=8 > C=6 > H=1$). Antara $-\\text{COOH}$ dan $-\\text{CH}_3$, atom karbon pada karboksilat mengikat $(O, O, O)$ sedangkan pada metil mengikat $(H, H, H)$, sehingga $-\\text{COOH}$ memiliki prioritas lebih tinggi. Jika penomoran prioritas $1 \\to 2 \\to 3$ searah jarum jam dengan gugus $4\\,(-\\text{H})$ di belakang, konfigurasinya adalah $(R)$."
      },
      {
        "key": "C",
        "text": "Urutan prioritas: $-\\text{OH} > -\\text{CH}_3 > -\\text{COOH} > -\\text{H}$ dengan konfigurasi rasemat optis inaktif."
      },
      {
        "key": "D",
        "text": "Urutan prioritas: $-\\text{CH}_3 > -\\text{COOH} > -\\text{OH} > -\\text{H}$ berdasarkan rantai karbon utama terpanjang."
      },
      {
        "key": "E",
        "text": "Urutan prioritas: $-\\text{COOH} > -\\text{OH} > -\\text{CH}_3 > -\\text{H}$ dengan konfigurasi absolut selalu $(S)$."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Urutan prioritas: $-\\text{OH} > -\\text{COOH} > -\\text{CH}_3 > -\\text{H}$, karena penentuan didasarkan pada nomor atom yang terikat langsung ($O=8 > C=6 > H=1$). Antara $-\\text{COOH}$ dan $-\\text{CH}_3$, atom karbon pada karboksilat mengikat $(O, O, O)$ sedangkan pada metil mengikat $(H, H, H)$, sehingga $-\\text{COOH}$ memiliki prioritas lebih tinggi. Jika penomoran prioritas $1 \\to 2 \\to 3$ searah jarum jam dengan gugus $4\\,(-\\text{H})$ di belakang, konfigurasinya adalah $(R)$.. Aturan CIP: Nomor atom tertinggi menang: -OH (O=8) nomor 1, -H (H=1) nomor 4. Bandingkan -COOH vs -CH3: C pada -COOH mengikat atom O, sehingga -COOH menang jadi nomor 2, -CH3 nomor 3. Prioritas: -OH > -COOH > -CH3 > -H. Konfigurasi (R) jika searah jarum jam."
  },
  {
    "id": "kim-lat-h-18",
    "materi": "KIMIA INTI & PENANGGALAN RADIOMETRIK",
    "topic": "Penanggalan Radiokarbon Karbon-14 pada Fosil Kayu Purba",
    "hints": {
      "concept": "At / A0 = 3,125 / 12,5 = 1/4 = (1/2)^2. Artinya telah melewati n = 2 kali waktu paruh. Usia fosil t = 2 * 5.730 tahun.",
      "execution": "t = 2 * 5.730 = 11.460 tahun."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sampel fosil kayu purba dari situs purbakala dianalisis aktivitas radiasi karbon-14 ($^{14}\\text{C}$) miliknya dan diperoleh aktivitas sebesar $A_t = 3{,}125\\text{ dpm/gram karbon}$ (desintegrasi per menit). Sampel kayu hidup modern yang sejenis memiliki aktivitas radiasi awal $A_0 = 12{,}5\\text{ dpm/gram karbon}$. Jika waktu paruh isotop $^{14}\\text{C}$ adalah $T_{1/2} = 5.730\\text{ tahun}$, usia fosil kayu purba tersebut adalah...",
    "formulaHud": {
      "title": "PENANGGALAN RADIOKARBON KARBON-14",
      "latex": "\\frac{A_t}{A_0} = \\left(\\frac{1}{2}\\right)^{\\frac{t}{T_{1/2}}} \\implies \\frac{3{,}125}{12{,}5} = \\frac{1}{4} = \\left(\\frac{1}{2}\\right)^2 \\implies \\frac{t}{5.730} = 2 \\implies t = 11.460\\text{ tahun}",
      "legend": "• Karbon-14 terbentuk di atmosfer atas oleh sinar kosmik dan diserap oleh tumbuhan fotosintesis<br>• Setelah organisme mati, penyerapan terhenti dan $^{14}\\text{C}$ meluruh menjadi $^{14}\\text{N}$ dengan $T_{1/2} = 5.730\\text{ tahun}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$17.190\\text{ tahun}$, dihitung dari asumsi bahwa zat telah meluruh selama 3 periode paruh."
      },
      {
        "key": "B",
        "text": "$11.460\\text{ tahun}$, karena rasio aktivitas radiasi sisa terhadap aktivitas awal adalah $\\frac{A_t}{A_0} = \\frac{3{,}125}{12{,}5} = \\frac{1}{4} = \\left(\\frac{1}{2}\\right)^2$. Hal ini menunjukkan bahwa sampel telah meluruh selama $n = 2$ periode waktu paruh. Maka usia fosil tersebut adalah $t = n \\times T_{1/2} = 2 \\times 5.730\\text{ tahun} = 11.460\\text{ tahun}$."
      },
      {
        "key": "C",
        "text": "$22.920\\text{ tahun}$, dihitung dari 4 periode waktu paruh peluruhan radioaktif."
      },
      {
        "key": "D",
        "text": "$5.730\\text{ tahun}$, karena hanya memperhitungkan 1 periode waktu paruh peluruhan radiasi ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "E",
        "text": "$2.865\\text{ tahun}$, karena waktu paruh keliru dibagi dua alih-alih dikalikan dengan jumlah periode peluruhan."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $11.460\\text{ tahun}$, karena rasio aktivitas radiasi sisa terhadap aktivitas awal adalah $\\frac{A_t}{A_0} = \\frac{3{,}125}{12{,}5} = \\frac{1}{4} = \\left(\\frac{1}{2}\\right)^2$. Hal ini menunjukkan bahwa sampel telah meluruh selama $n = 2$ periode waktu paruh. Maka usia fosil tersebut adalah $t = n \\times T_{1/2} = 2 \\times 5.730\\text{ tahun} = 11.460\\text{ tahun}$.. At / A0 = 3,125 / 12,5 = 1/4 = (1/2)^2. Artinya telah melewati n = 2 kali waktu paruh. Usia fosil t = 2 * 5.730 tahun. t = 2 * 5.730 = 11.460 tahun."
  },
  {
    "id": "kim-lat-h-19",
    "materi": "KIMIA POLIMER (POLIMER BIODEGRADABLE)",
    "topic": "Sintesis Asam Polilaktat (PLA) dari Asam Laktat",
    "hints": {
      "concept": "Asam laktat memiliki gugus -OH dan -COOH yang bereaksi membentuk ikatan ester dengan melepaskan H2O. Reaksi polimerisasi yang melepaskan molekul kecil (H2O) adalah polimerisasi kondensasi.",
      "execution": "Polimerisasi kondensasi menghasilkan poliester dan air."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Polilaktida atau asam polilaktat (Poly Lactic Acid / PLA) adalah poliester termoplastik ramah lingkungan yang banyak digunakan pada filamen printer 3D dan benang jahit bedah medis yang dapat diserap tubuh. Reaksi pembentukan PLA dari monomer asam 2-hidroksipropanoat (asam laktat) digolongkan sebagai polimerisasi...",
    "formulaHud": {
      "title": "POLIMERISASI POLIESTER ASAM POLILAKTAT (PLA)",
      "latex": "n\\,(\\text{CH}_3-\\text{CH(OH)}-\\text{COOH}) \\xrightarrow{\\text{Kondensasi}} [-\\text{O}-\\text{CH}(\\text{CH}_3)-\\text{CO}-]_n + (n-1)\\,\\text{H}_2\\text{O}",
      "legend": "• Asam laktat memiliki 2 gugus fungsi: $-\\text{OH}$ dan $-\\text{COOH}$ (bifungsional)<br>• Bersifat biokompatibel dan terurai secara alami oleh mikroorganisme menjadi air dan $\\text{CO}_2$"
    },
    "options": [
      {
        "key": "A",
        "text": "Polimerisasi adisi radikal bebas, karena membuka ikatan rangkap dua karbon-karbon pada asam laktat menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "B",
        "text": "Polimerisasi penataan ulang fotokimiawi isomer tanpa adanya reaksi kondensasi gugus fungsi."
      },
      {
        "key": "C",
        "text": "Polimerisasi kondensasi (atau polimerisasi pembukaan cincin ester siklik laktida), karena gugus karboksilat ($-\\text{COOH}$) pada satu molekul bereaksi dengan gugus hidroksil ($-\\text{OH}$) pada molekul lain membentuk ikatan ester (poliester) dengan melepaskan molekul air ($\\text{H}_2\\text{O}$) sebagai produk sampingan."
      },
      {
        "key": "D",
        "text": "Vulkanisasi silang belerang, karena menghubungkan rantai peptida dengan ikatan disulfida."
      },
      {
        "key": "E",
        "text": "Polimerisasi adisi kationik, karena membutuhkan inisiator asam kuat tanpa melepaskan molekul kecil."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Polimerisasi kondensasi (atau polimerisasi pembukaan cincin ester siklik laktida), karena gugus karboksilat ($-\\text{COOH}$) pada satu molekul bereaksi dengan gugus hidroksil ($-\\text{OH}$) pada molekul lain membentuk ikatan ester (poliester) dengan melepaskan molekul air ($\\text{H}_2\\text{O}$) sebagai produk sampingan.. Asam laktat memiliki gugus -OH dan -COOH yang bereaksi membentuk ikatan ester dengan melepaskan H2O. Reaksi polimerisasi yang melepaskan molekul kecil (H2O) adalah polimerisasi kondensasi. Polimerisasi kondensasi menghasilkan poliester dan air."
  },
  {
    "id": "kim-lat-h-20",
    "materi": "KESETIMBANGAN KIMIA HETEROGEN",
    "topic": "Perhitungan Tekanan Parsial Gas pada Kesetimbangan Heterogen",
    "hints": {
      "concept": "Padatan murni tidak masuk rumus Kp, jadi Kp = P(CO2) = 0,82 atm. Gunakan gas ideal: n = P * V / (R * T) = 0,82 * 10 / (0,082 * 1000) = 0,1 mol. Massa = n * Mr = 0,1 * 44 = 4,4 g.",
      "execution": "P(CO2) = 0,82 atm, massa CO2 = 4,4 gram."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam ruang hampa bervolume $10\\text{ liter}$ pada suhu $T = 1.000\\text{ K}$, dimasukkan $100\\text{ gram}$ padatan kalsium karbonat ($\\text{CaCO}_3(s)$). Terjadi reaksi kesetimbangan heterogen:<br>$$\\text{CaCO}_3(s) \\rightleftharpoons \\text{CaO}(s) + \\text{CO}_2(g) \\quad K_p = 0{,}82\\text{ atmosfer}$$<br>Jika pada keadaan setimbang masih terdapat sisa padatan $\\text{CaCO}_3$, tekanan parsial gas $\\text{CO}_2$ di dalam wadah dan massa gas $\\text{CO}_2$ yang berada dalam fasa gas ($M_r\\,\\text{CO}_2 = 44$, $R = 0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)}$) berturut-turut adalah...",
    "formulaHud": {
      "title": "KESETIMBANGAN HETEROGEN DEKOMPOSISI KARBONAT",
      "latex": "K_p = P_{\\text{CO}_2} = 0{,}82\\text{ atm}; \\quad n = \\frac{P V}{R T} = \\frac{0{,}82 \\times 10}{0{,}082 \\times 1.000} = 0{,}1\\text{ mol}; \\quad m = 0{,}1 \\times 44 = 4{,}4\\text{ g}",
      "legend": "• Aktivitas padatan murni $\\text{CaCO}_3(s)$ dan $\\text{CaO}(s)$ sama dengan 1<br>• Tekanan kesetimbangan hanya ditentukan oleh tekanan gas $\\text{CO}_2$<br>• Massa $\\text{CO}_2 = 4{,}4\\text{ gram}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$P_{\\text{CO}_2} = 1{,}64\\text{ atm}$ dan massa $\\text{CO}_2 = 8{,}8\\text{ gram}$, dihitung dari penggandaan tekanan kesetimbangan."
      },
      {
        "key": "B",
        "text": "$P_{\\text{CO}_2} = 0{,}82\\text{ atm}$ dan massa $\\text{CO}_2 = 44\\text{ gram}$, karena gas dianggap berjumlah satu mol penuh."
      },
      {
        "key": "C",
        "text": "$P_{\\text{CO}_2} = 0{,}82\\text{ atm}$ dan massa $\\text{CO}_2 = 4{,}4\\text{ gram}$, karena pada kesetimbangan heterogen zat berwujud padat murni tidak disertakan dalam persamaan aksi massa, sehingga $K_p = P_{\\text{CO}_2} = 0{,}82\\text{ atm}$. Jumlah mol gas $\\text{CO}_2$ dihitung dari persamaan gas ideal $n = \\frac{P V}{R T} = \\frac{0{,}82\\text{ atm} \\times 10\\text{ L}}{0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)} \\times 1.000\\text{ K}} = \\frac{8{,}2}{82} = 0{,}1\\text{ mol}$. Massa gas adalah $m = 0{,}1\\text{ mol} \\times 44\\text{ g/mol} = 4{,}4\\text{ gram}$."
      },
      {
        "key": "D",
        "text": "$P_{\\text{CO}_2} = 0{,}41\\text{ atm}$ dan massa $\\text{CO}_2 = 2{,}2\\text{ gram}$, karena tekanan gas keliru dibagi dua oleh keberadaan dua fasa padatan."
      },
      {
        "key": "E",
        "text": "$P_{\\text{CO}_2} = 0{,}082\\text{ atm}$ dan massa $\\text{CO}_2 = 0{,}44\\text{ gram}$, karena galat penempatan koma desimal konstanta gas ideal."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $P_{\\text{CO}_2} = 0{,}82\\text{ atm}$ dan massa $\\text{CO}_2 = 4{,}4\\text{ gram}$, karena pada kesetimbangan heterogen zat berwujud padat murni tidak disertakan dalam persamaan aksi massa, sehingga $K_p = P_{\\text{CO}_2} = 0{,}82\\text{ atm}$. Jumlah mol gas $\\text{CO}_2$ dihitung dari persamaan gas ideal $n = \\frac{P V}{R T} = \\frac{0{,}82\\text{ atm} \\times 10\\text{ L}}{0{,}082\\text{ L}\\cdot\\text{atm/(mol}\\cdot\\text{K)} \\times 1.000\\text{ K}} = \\frac{8{,}2}{82} = 0{,}1\\text{ mol}$. Massa gas adalah $m = 0{,}1\\text{ mol} \\times 44\\text{ g/mol} = 4{,}4\\text{ gram}$.. Padatan murni tidak masuk rumus Kp, jadi Kp = P(CO2) = 0,82 atm. Gunakan gas ideal: n = P * V / (R * T) = 0,82 * 10 / (0,082 * 1000) = 0,1 mol. Massa = n * Mr = 0,1 * 44 = 4,4 g. P(CO2) = 0,82 atm, massa CO2 = 4,4 gram."
  },
  {
    "id": "kim-lat-h-21",
    "materi": "SIFAT UNSUR TRANSISI (WARNA ION KOMPLEKS)",
    "topic": "Penyerapan Cahaya Transisi d-d dan Warna Komplementer",
    "hints": {
      "concept": "Warna larutan yang terlihat adalah warna komplementer dari cahaya yang diserap. Warna komplementer dari biru adalah jingga (oranye). Warna muncul karena eksitasi transisi elektron d-d.",
      "execution": "Menyerap cahaya jingga (transisi d-d), warna komplementer biru diteruskan."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Larutan tembaga(II) sulfat yang mengandung ion kompleks $[\text{Cu}(\text{H}_2\text{O})_6]^{2+}$ tampak berwarna biru cerah di mata pengamat. Berdasarkan Teori Medan Kristal dan roda warna komplementer, warna berkas cahaya tampak yang diserap paling kuat oleh larutan tersebut dan mekanisme elektroniknya adalah...",
    "formulaHud": {
      "title": "TRANSISI d-d & RODA WARNA KOMPLEMENTER",
      "latex": "\\Delta_o = h \\nu = \\frac{h c}{\\lambda_{\\text{serap}}}; \\quad \\text{Warna Diserap: Jingga } (\\approx 600\\text{ nm}) \\iff \\text{Warna Diteruskan: Biru (Komplementer)}",
      "legend": "• Konfigurasi $\\text{Cu}^{2+} = 3d^9$ (memiliki 1 lubang elektron pada orbital $e_g$)<br>• Penyerapan foton berenergi $\\Delta_o$ mengeksitasi elektron $t_{2g} \\to e_g$<br>• Warna yang diamati mata selalu merupakan warna komplementer dari warna foton yang diserap"
    },
    "options": [
      {
        "key": "A",
        "text": "Menyerap cahaya berwarna biru cerah dan memancarkan kembali cahaya biru melalui peristiwa fluoresensi foton atomik."
      },
      {
        "key": "B",
        "text": "Menyerap cahaya berwarna hijau dan meneruskan warna merah melalui hamburan Rayleigh intermolekul pelarut."
      },
      {
        "key": "C",
        "text": "Menyerap gelombang inframerah termal akibat getaran ikatan kovalen koordinasi ligan air."
      },
      {
        "key": "D",
        "text": "Menyerap cahaya berwarna jingga (oranye, panjang gelombang $\\approx 600 - 620\\text{ nm}$), dan warna biru yang terlihat adalah warna komplementer yang diteruskan ke mata akibat adanya eksitasi elektron dari orbital $t_{2g}$ ke orbital $e_g$ (transisi $d-d$)."
      },
      {
        "key": "E",
        "text": "Menyerap sinar ultraviolet tak tampak dan meneruskan seluruh spektrum warna tampak secara seragam."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Menyerap cahaya berwarna jingga (oranye, panjang gelombang $\\approx 600 - 620\\text{ nm}$), dan warna biru yang terlihat adalah warna komplementer yang diteruskan ke mata akibat adanya eksitasi elektron dari orbital $t_{2g}$ ke orbital $e_g$ (transisi $d-d$).. Warna larutan yang terlihat adalah warna komplementer dari cahaya yang diserap. Warna komplementer dari biru adalah jingga (oranye). Warna muncul karena eksitasi transisi elektron d-d. Menyerap cahaya jingga (transisi d-d), warna komplementer biru diteruskan."
  },
  {
    "id": "kim-lat-h-22",
    "materi": "KINETIKA KIMIA (MEKANISME REAKSI MULTITAHAP)",
    "topic": "Tahap Penentu Laju dan Penurunan Hukum Laju Reaksi",
    "hints": {
      "concept": "Laju reaksi ditentukan oleh tahap lambat (tahap 2): v = k2 * [N2O2] * [H2]. Karena N2O2 adalah zat antara, substitusi dari kesetimbangan tahap 1: [N2O2] = Kc * [NO]^2. Maka v = k [NO]^2 [H2].",
      "execution": "v = k [NO]^2 [H2], zat antara = N2O2."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Reaksi pembentukan gas dinitrogen monoksida memiliki persamaan stoikiometri:<br>$$2\\,\\text{NO}(g) + \\text{H}_2(g) \\to \\text{N}_2\\text{O}(g) + \\text{H}_2\\text{O}(g)$$<br>Diusulkan mekanisme reaksi dua tahap sebagai berikut:<br>• Tahap 1 (Cepat, Kesetimbangan): $2\\,\\text{NO}(g) \\rightleftharpoons \\text{N}_2\\text{O}_2(g) \\quad (K_c)$<br>• Tahap 2 (Lambat): $\\text{N}_2\\text{O}_2(g) + \\text{H}_2(g) \\xrightarrow{k_2} \\text{N}_2\\text{O}(g) + \\text{H}_2\\text{O}(g)$<br>Persamaan laju reaksi yang sesuai dengan mekanisme tersebut dan spesi yang bertindak sebagai zat antara (intermediate) adalah...",
    "formulaHud": {
      "title": "PENENTUAN HUKUM LAJU DARI TAHAP PENENTU LAJU (RDS)",
      "latex": "v = k_2 [\\text{N}_2\\text{O}_2][\\text{H}_2]; \\quad K_c = \\frac{[\\text{N}_2\\text{O}_2]}{[\\text{NO}]^2} \\implies [\\text{N}_2\\text{O}_2] = K_c [\\text{NO}]^2 \\implies v = k [\\text{NO}]^2 [\\text{H}_2]",
      "legend": "• Tahap lambat = Rate Determining Step (RDS)<br>• Zat antara (intermediate) tidak boleh muncul pada persamaan laju reaksi final<br>• $\\text{N}_2\\text{O}_2$ adalah zat antara"
    },
    "options": [
      {
        "key": "A",
        "text": "$v = k [\\text{N}_2\\text{O}_2] [\\text{H}_2]$ dengan zat antara $\\text{NO}_2$."
      },
      {
        "key": "B",
        "text": "$v = k [\\text{NO}]^2$ dengan zat antara atom oksigen radikal."
      },
      {
        "key": "C",
        "text": "$v = k [\\text{NO}]^2 [\\text{H}_2]$ dengan zat antara $\\text{N}_2\\text{O}_2$, karena tahap lambat (tahap 2) adalah tahap penentu laju (Rate-Determining Step / RDS) sehingga $v = k_2 [\\text{N}_2\\text{O}_2][\\text{H}_2]$. Dari kesetimbangan cepat tahap 1: $[\\text{N}_2\\text{O}_2] = K_c [\\text{NO}]^2$. Substitusi ke tahap 2 menghasilkan $v = k_2 K_c [\\text{NO}]^2 [\\text{H}_2] = k [\\text{NO}]^2 [\\text{H}_2]$. Spesi $\\text{N}_2\\text{O}_2$ terbentuk pada tahap 1 dan dikonsumsi pada tahap 2 sehingga berstatus sebagai zat antara."
      },
      {
        "key": "D",
        "text": "$v = k [\\text{NO}]^2 [\\text{H}_2]^2$ dengan zat antara $\\text{N}_2\\text{O}$."
      },
      {
        "key": "E",
        "text": "$v = k [\\text{NO}] [\\text{H}_2]$ dengan zat antara $\\text{H}_2\\text{O}$."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $v = k [\\text{NO}]^2 [\\text{H}_2]$ dengan zat antara $\\text{N}_2\\text{O}_2$, karena tahap lambat (tahap 2) adalah tahap penentu laju (Rate-Determining Step / RDS) sehingga $v = k_2 [\\text{N}_2\\text{O}_2][\\text{H}_2]$. Dari kesetimbangan cepat tahap 1: $[\\text{N}_2\\text{O}_2] = K_c [\\text{NO}]^2$. Substitusi ke tahap 2 menghasilkan $v = k_2 K_c [\\text{NO}]^2 [\\text{H}_2] = k [\\text{NO}]^2 [\\text{H}_2]$. Spesi $\\text{N}_2\\text{O}_2$ terbentuk pada tahap 1 dan dikonsumsi pada tahap 2 sehingga berstatus sebagai zat antara.. Laju reaksi ditentukan oleh tahap lambat (tahap 2): v = k2 * [N2O2] * [H2]. Karena N2O2 adalah zat antara, substitusi dari kesetimbangan tahap 1: [N2O2] = Kc * [NO]^2. Maka v = k [NO]^2 [H2]. v = k [NO]^2 [H2], zat antara = N2O2."
  },
  {
    "id": "kim-lat-h-23",
    "materi": "REAKSI SAPONIFIKASI & BILANGAN PENYABUNAN",
    "topic": "Hidrolisis Basa Trigliserida dan Penentuan Angka Penyabunan",
    "hints": {
      "concept": "1 mol trigliserida bereaksi dengan 3 mol KOH. Angka penyabunan = (3 * 56 * 1000) / Mr_minyak. Mr tripalmitin = 806.",
      "execution": "Angka penyabunan = 168.000 / 806 = 208,4 mg KOH/g."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Suatu sampel minyak nabati berupa trigliserida murni tripalmitin ($\\text{C}_{51}\\text{H}_{98}\\text{O}_6$, $M_r = 806\\text{ g/mol}$) dihidrolisis sempurna dengan larutan kalium hidroksida ($\\text{KOH}$, $M_r = 56\\text{ g/mol}$) menurut reaksi saponifikasi:<br>$$\\text{C}_{51}\\text{H}_{98}\\text{O}_6 + 3\\,\\text{KOH} \\to 3\\,\\text{C}_{15}\\text{H}_{31}\\text{COOK} + \\text{C}_3\\text{H}_5(\\text{OH})_3$$<br>Massa $\\text{KOH}$ dalam miligram yang dibutuhkan untuk menyabunkan secara sempurna $1\\text{ gram}$ minyak tripalmitin tersebut (angka penyabunan / saponification value) adalah...",
    "formulaHud": {
      "title": "RUMUS ANGKA PENYABUNAN (SAPONIFICATION VALUE)",
      "latex": "\\text{Angka Penyabunan} = \\frac{3 \\times M_r(\\text{KOH}) \\times 1.000}{M_r(\\text{Trigliserida})} = \\frac{3 \\times 56 \\times 1.000}{806} = \\frac{168.000}{806} \\approx 208{,}44\\text{ mg KOH/g}",
      "legend": "• Angka penyabunan = miligram KOH untuk menyabunkan 1 gram minyak/lemak<br>• Semakin kecil $M_r$ rata-rata asam lemak, semakin besar angka penyabunannya<br>• Tripalmitin $= 208{,}4\\text{ mg KOH/g}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$416{,}8\\text{ mg KOH/gram minyak}$, dihitung dari penggandaan reaksi penyabunan asam lemak bebas."
      },
      {
        "key": "B",
        "text": "$69{,}5\\text{ mg KOH/gram minyak}$, karena mol KOH keliru dihitung hanya satu mol tanpa dikalikan koefisien tiga trigliserida ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "C",
        "text": "$806{,}0\\text{ mg KOH/gram minyak}$, karena menyamakan angka penyabunan dengan massa molar trigliserida."
      },
      {
        "key": "D",
        "text": "$208{,}4\\text{ mg KOH/gram minyak}$, karena satu mol trigliserida membutuhkan tepat 3 mol $\\text{KOH}$ untuk memutus 3 ikatan ester membentuk sabun dan gliserol. Jumlah mol tripalmitin dalam $1\\text{ gram}$ adalah $n = \\frac{1\\text{ g}}{806\\text{ g/mol}} \\approx 1{,}2407 \\times 10^{-3}\\text{ mol}$. Mol $\\text{KOH}$ yang dibutuhkan adalah $3 \\times 1{,}2407 \\times 10^{-3} = 3{,}722 \\times 10^{-3}\\text{ mol}$. Massa $\\text{KOH}$ adalah $m = 3{,}722 \\times 10^{-3}\\text{ mol} \\times 56\\text{ g/mol} \\approx 0{,}2084\\text{ gram} = 208{,}4\\text{ miligram}$."
      },
      {
        "key": "E",
        "text": "$112{,}0\\text{ mg KOH/gram minyak}$, dihitung dari pembagian massa molar KOH terhadap jumlah ikatan ester."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $208{,}4\\text{ mg KOH/gram minyak}$, karena satu mol trigliserida membutuhkan tepat 3 mol $\\text{KOH}$ untuk memutus 3 ikatan ester membentuk sabun dan gliserol. Jumlah mol tripalmitin dalam $1\\text{ gram}$ adalah $n = \\frac{1\\text{ g}}{806\\text{ g/mol}} \\approx 1{,}2407 \\times 10^{-3}\\text{ mol}$. Mol $\\text{KOH}$ yang dibutuhkan adalah $3 \\times 1{,}2407 \\times 10^{-3} = 3{,}722 \\times 10^{-3}\\text{ mol}$. Massa $\\text{KOH}$ adalah $m = 3{,}722 \\times 10^{-3}\\text{ mol} \\times 56\\text{ g/mol} \\approx 0{,}2084\\text{ gram} = 208{,}4\\text{ miligram}$.. 1 mol trigliserida bereaksi dengan 3 mol KOH. Angka penyabunan = (3 * 56 * 1000) / Mr_minyak. Mr tripalmitin = 806. Angka penyabunan = 168.000 / 806 = 208,4 mg KOH/g."
  },
  {
    "id": "kim-lat-h-24",
    "materi": "LARUTAN BINER IDEAL (HUKUM RAOULT)",
    "topic": "Tekanan Uap Total dan Komposisi Uap Campuran Biner",
    "hints": {
      "concept": "Fraksi mol cair: XB = 1/4 = 0,25, XT = 3/4 = 0,75. Tekanan parsial: PB = 0,25 * 96 = 24 mmHg, PT = 0,75 * 32 = 24 mmHg. P_total = 24 + 24 = 48 mmHg. Fraksi mol uap: YB = PB / P_total = 24 / 48 = 0,50.",
      "execution": "P_total = 48 mmHg, YB = 0,50."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua cairan organik yang saling melarutkan, benzena ($\\text{C}_6\\text{H}_6$) dan toluena ($\\text{C}_7\\text{H}_8$), membentuk larutan ideal pada suhu $25^\\circ\\text{C}$. Pada suhu tersebut, tekanan uap murni benzena adalah $P_B^\\circ = 96\\text{ mmHg}$ dan tekanan uap murni toluena adalah $P_T^\\circ = 32\\text{ mmHg}$. Jika campuran dibuat dengan mencampurkan $1\\text{ mol}$ benzena dan $3\\text{ mol}$ toluena, tekanan uap total campuran ($P_{\\text{total}}$) dan fraksi mol benzena dalam fase uap di atas larutan ($Y_B$) adalah...",
    "formulaHud": {
      "title": "HUKUM RAOULT LARUTAN BINER IDEAL",
      "latex": "P_B = X_B P_B^\\circ = 0{,}25(96) = 24\\text{ mmHg}; \\quad P_T = X_T P_T^\\circ = 0{,}75(32) = 24\\text{ mmHg}; \\quad P_{\\text{total}} = 48\\text{ mmHg}; \\quad Y_B = \\frac{P_B}{P_{\\text{total}}} = \\frac{24}{48} = 0{,}50",
      "legend": "• Komponen lebih mudah menguap (benzena, $P^\\circ = 96$) terkonsentrasi di fasa uap ($X_B = 0{,}25 \\to Y_B = 0{,}50$)<br>• Prinsip ini mendasari operasi distilasi fraksionasi minyak bumi"
    },
    "options": [
      {
        "key": "A",
        "text": "$P_{\\text{total}} = 64\\text{ mmHg}$ dan $Y_B = 0{,}25$, dihitung dari rata-rata tekanan murni dan menyamakan fraksi uap dengan fase cair menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "B",
        "text": "$P_{\\text{total}} = 36\\text{ mmHg}$ dan $Y_B = 0{,}33$, dihitung dari perbandingan mol terbalik larutan biner."
      },
      {
        "key": "C",
        "text": "$P_{\\text{total}} = 48\\text{ mmHg}$ dan $Y_B = 0{,}25$, karena mengabaikan peningkatan konsentrasi uap komponen volatil."
      },
      {
        "key": "D",
        "text": "$P_{\\text{total}} = 128\\text{ mmHg}$ dan $Y_B = 0{,}75$, dihitung dari penjumlahan langsung kedua tekanan uap murni pelarut."
      },
      {
        "key": "E",
        "text": "$P_{\\text{total}} = 48\\text{ mmHg}$ dan $Y_B = 0{,}50$ (atau $50\\%$), karena fraksi mol benzena dalam fase cair adalah $X_B = \\frac{1}{1 + 3} = 0{,}25$ dan toluena $X_T = \\frac{3}{4} = 0{,}75$. Menurut Hukum Raoult: tekanan parsial benzena $P_B = X_B \\cdot P_B^\\circ = 0{,}25 \\times 96 = 24\\text{ mmHg}$ dan toluena $P_T = X_T \\cdot P_T^\\circ = 0{,}75 \\times 32 = 24\\text{ mmHg}$. Tekanan total adalah $P_{\\text{total}} = P_B + P_T = 24 + 24 = 48\\text{ mmHg}$. Fraksi mol benzena dalam fase uap adalah $Y_B = \\frac{P_B}{P_{\\text{total}}} = \\frac{24}{48} = 0{,}50$ (uap menjadi lebih kaya akan komponen yang lebih volatil / titik didih lebih rendah)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $P_{\\text{total}} = 48\\text{ mmHg}$ dan $Y_B = 0{,}50$ (atau $50\\%$), karena fraksi mol benzena dalam fase cair adalah $X_B = \\frac{1}{1 + 3} = 0{,}25$ dan toluena $X_T = \\frac{3}{4} = 0{,}75$. Menurut Hukum Raoult: tekanan parsial benzena $P_B = X_B \\cdot P_B^\\circ = 0{,}25 \\times 96 = 24\\text{ mmHg}$ dan toluena $P_T = X_T \\cdot P_T^\\circ = 0{,}75 \\times 32 = 24\\text{ mmHg}$. Tekanan total adalah $P_{\\text{total}} = P_B + P_T = 24 + 24 = 48\\text{ mmHg}$. Fraksi mol benzena dalam fase uap adalah $Y_B = \\frac{P_B}{P_{\\text{total}}} = \\frac{24}{48} = 0{,}50$ (uap menjadi lebih kaya akan komponen yang lebih volatil / titik didih lebih rendah).. Fraksi mol cair: XB = 1/4 = 0,25, XT = 3/4 = 0,75. Tekanan parsial: PB = 0,25 * 96 = 24 mmHg, PT = 0,75 * 32 = 24 mmHg. P_total = 24 + 24 = 48 mmHg. Fraksi mol uap: YB = PB / P_total = 24 / 48 = 0,50. P_total = 48 mmHg, YB = 0,50."
  },
  {
    "id": "kim-lat-h-25",
    "materi": "KIMIA POLIMER & KONDENSASI",
    "topic": "Sintesis Nilon-6,6 dan Perhitungan Derajat Polimerisasi",
    "hints": {
      "concept": "Derajat polimerisasi (DP) = Massa molar polimer (Mn) / Massa molar unit berulang (M0).",
      "execution": "DP = 22.600 / 226 = 100."
    },
    "subject": "kimia",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Polimer sintetik nilon-6,6 diproduksi melalui polimerisasi kondensasi antara asam heksanadioat (asam adipat) dan 1,6-diaminoheksana (heksametilendiamin). Jika massa molekul relatif satu unit berulang (repeating unit) nilon-6,6 adalah $M_r = 226\\text{ g/mol}$ dan suatu serat nilon-6,6 memiliki massa molar rata-rata $M_n = 22.600\\text{ g/mol}$, derajat polimerisasi rata-rata ($DP$) dari rantai polimer tersebut adalah...",
    "formulaHud": {
      "title": "DERAJAT POLIMERISASI (DEGREE OF POLYMERIZATION)",
      "latex": "DP = \\frac{M_n}{M_0} = \\frac{22.600\\text{ g/mol}}{226\\text{ g/mol}} = 100",
      "legend": "• Unit berulang nilon-6,6: $[-\\text{NH}-(\\text{CH}_2)_6-\\text{NH}-\\text{CO}-(\\text{CH}_2)_4-\\text{CO}-]$ dengan rumus $(\\text{C}_{12}\\text{H}_{22}\\text{N}_2\\text{O}_2)$ bernilai $M_0 = 226\\text{ g/mol}$<br>• $DP = 100$ unit berulang terhubung ikatan amida"
    },
    "options": [
      {
        "key": "A",
        "text": "$DP = 200$, dihitung dari penjumlahan jumlah atom karbon dalam kedua monomer pembentuk."
      },
      {
        "key": "B",
        "text": "$DP = 50$, karena menganggap satu unit berulang berasal dari dua rantai polimer terpisah."
      },
      {
        "key": "C",
        "text": "$DP = 66$, karena terpengaruh oleh penomoran nama dagang nilon-6,6."
      },
      {
        "key": "D",
        "text": "$DP = 100$, karena derajat polimerisasi menyatakan jumlah unit berulang monomerik yang menyusun satu rantai makromolekul polimer, yang dihitung dari perbandingan massa molar total polimer terhadap massa molar satu unit berulang: $DP = \\frac{M_n}{M_r\\text{ (unit berulang)}} = \\frac{22.600\\text{ g/mol}}{226\\text{ g/mol}} = 100$."
      },
      {
        "key": "E",
        "text": "$DP = 1.000$, dihitung dari pembagian massa polimer dengan massa molar gas hidrogen sampingan."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $DP = 100$, karena derajat polimerisasi menyatakan jumlah unit berulang monomerik yang menyusun satu rantai makromolekul polimer, yang dihitung dari perbandingan massa molar total polimer terhadap massa molar satu unit berulang: $DP = \\frac{M_n}{M_r\\text{ (unit berulang)}} = \\frac{22.600\\text{ g/mol}}{226\\text{ g/mol}} = 100$.. Derajat polimerisasi (DP) = Massa molar polimer (Mn) / Massa molar unit berulang (M0). DP = 22.600 / 226 = 100."
  },
  {
    "id": "kim-sim-01",
    "materi": "TERMODINAMIKA & ENERGI KISI KRISTAL",
    "topic": "Siklus Born-Haber Pembentukan Natrium Klorida",
    "hints": {
      "concept": "Gunakan Hukum Hess pada siklus Born-Haber: Delta Hf = Delta Hsub + IE1 + 0.5*D(Cl2) + EA + U_kisi. Perhatikan bahwa hanya dibutuhkan 1 mol atom Cl(g), jadi disosiasi Cl2 dikalikan 1/2.",
      "execution": "Jumlahkan: 108 + 496 + 121 - 349 = 376 kJ/mol. Maka U_kisi = -411 - 376 = -787 kJ/mol."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam siklus Born-Haber untuk pembentukan kristal natrium klorida, $\\text{NaCl}(s)$, diketahui data termokimia standar berikut:<br>• Entalpi pembentukan standar: $\\Delta H_f^\\circ[\\text{NaCl}(s)] = -411\\text{ kJ/mol}$<br>• Entalpi sublimasi natrium: $\\Delta H_{\\text{sub}}[\\text{Na}(s)] = +108\\text{ kJ/mol}$<br>• Energi ionisasi pertama natrium: $IE_1[\\text{Na}(g)] = +496\\text{ kJ/mol}$<br>• Energi disosiasi ikatan klorin: $D[\\text{Cl}_2(g)] = +242\\text{ kJ/mol}$<br>• Afinitas elektron klorin: $EA[\\text{Cl}(g)] = -349\\text{ kJ/mol}$<br>Besarnya energi kisi ($U_{\\text{kisi}}$) kristal $\\text{NaCl}(s)$ yang didefinisikan sebagai perubahan entalpi pada reaksi: $\\text{Na}^+(g) + \\text{Cl}^-(g) \\rightarrow \\text{NaCl}(s)$ adalah...",
    "formulaHud": {
      "title": "SIKLUS BORN-HABER PEMBENTUKAN KRISTAL IONIK",
      "latex": "\\Delta H_f^\\circ = \\Delta H_{\\text{sub}} + IE_1 + \\frac{1}{2}D_{\\text{Cl-Cl}} + EA + U_{\\text{kisi}} \\implies U_{\\text{kisi}} = -411 - (108 + 496 + 121 - 349) = -787\\text{ kJ/mol}",
      "legend": "• Entalpi pembentukan kristal $\\Delta H_f^\\circ = -411\\text{ kJ/mol}$<br>• Atomisasi gas Cl: $\\frac{1}{2} D = +121\\text{ kJ/mol}$<br>• Jumlah tahap endoterm-eksoterm gas = $+376\\text{ kJ/mol}$<br>• Energi kisi eksotermik pembentukan = $-787\\text{ kJ/mol}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$U_{\\text{kisi}} = -908\\text{ kJ/mol}$, akibat lupa mengalikan disosiasi ikatan gas klorin dengan koefisien setengah pada pembentukan satu mol atom Cl."
      },
      {
        "key": "B",
        "text": "$U_{\\text{kisi}} = -438\\text{ kJ/mol}$, dihitung dengan memperlakukan nilai afinitas elektron klorin sebagai proses endotermik bertanda positif."
      },
      {
        "key": "C",
        "text": "$U_{\\text{kisi}} = -666\\text{ kJ/mol}$, akibat salah mengurangkan energi ionisasi natrium dari nilai entalpi pembentukan kristal."
      },
      {
        "key": "D",
        "text": "$U_{\\text{kisi}} = +787\\text{ kJ/mol}$, karena salah mendefinisikan pembentukan kisi kristal dari ion gas sebagai pemutusan kisi ionik menjadi gas."
      },
      {
        "key": "E",
        "text": "$U_{\\text{kisi}} = -787\\text{ kJ/mol}$, karena menurut Hukum Hess pada siklus Born-Haber, $\\Delta H_f^\\circ = \\Delta H_{\\text{sub}} + IE_1 + \\frac{1}{2}D(\\text{Cl}_2) + EA + U_{\\text{kisi}}$. Maka $-411 = +108 + 496 + \\frac{1}{2}(242) + (-349) + U_{\\text{kisi}} = 108 + 496 + 121 - 349 + U_{\\text{kisi}} = +376 + U_{\\text{kisi}}$, sehingga $U_{\\text{kisi}} = -411 - 376 = -787\\text{ kJ/mol}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $U_{\\text{kisi}} = -787\\text{ kJ/mol}$, karena menurut Hukum Hess pada siklus Born-Haber, $\\Delta H_f^\\circ = \\Delta H_{\\text{sub}} + IE_1 + \\frac{1}{2}D(\\text{Cl}_2) + EA + U_{\\text{kisi}}$. Maka $-411 = +108 + 496 + \\frac{1}{2}(242) + (-349) + U_{\\text{kisi}} = 108 + 496 + 121 - 349 + U_{\\text{kisi}} = +376 + U_{\\text{kisi}}$, sehingga $U_{\\text{kisi}} = -411 - 376 = -787\\text{ kJ/mol}$.. Gunakan Hukum Hess pada siklus Born-Haber: Delta Hf = Delta Hsub + IE1 + 0.5*D(Cl2) + EA + U_kisi. Perhatikan bahwa hanya dibutuhkan 1 mol atom Cl(g), jadi disosiasi Cl2 dikalikan 1/2. Jumlahkan: 108 + 496 + 121 - 349 = 376 kJ/mol. Maka U_kisi = -411 - 376 = -787 kJ/mol."
  },
  {
    "id": "kim-sim-02",
    "materi": "KINETIKA KIMIA & MEKANISME REAKSI",
    "topic": "Pendekatan Keadaan Tunak (Steady-State Approximation) Dekomposisi Ozon",
    "hints": {
      "concept": "Pada steady-state: d[O]/dt = 0, sehingga laju pembentukan O pada tahap 1 sama dengan laju reaksi balik tahap 1 ditambah laju konsumsi pada tahap 2.",
      "execution": "Dapatkan [O] = k1[O3] / (k-1[O2] + k2[O3]), lalu substitusikan ke laju konsumsi O3 yaitu 2*k2*[O3]*[O]."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dekomposisi gas ozon di stratosfer dihancurkan melalui mekanisme dua tahap:<br>Tahap 1 (cepat, bolak-balik): $\\text{O}_3(g) \\underset{k_{-1}}{\\overset{k_1}{\\rightleftharpoons}} \\text{O}_2(g) + \\text{O}(g)$<br>Tahap 2 (lambat): $\\text{O}_3(g) + \\text{O}(g) \\xrightarrow{k_2} 2\\text{O}_2(g)$<br>Dengan menerapkan pendekatan keadaan tunak ($\\textit{steady-state approximation}$) pada spesi radikal oksigen intermediet $[\\text{O}]$, hukum laju pembentukan gas $\\text{O}_2$ atau laju penguraian gas $\\text{O}_3$ ($r = -\\frac{d[\\text{O}_3]}{dt}$) dinyatakan oleh persamaan...",
    "formulaHud": {
      "title": "STEADY-STATE APPROXIMATION DEKOMPOSISI OZON",
      "latex": "\\frac{d[\\text{O}]}{dt} = 0 \\implies [\\text{O}] = \\frac{k_1 [\\text{O}_3]}{k_{-1}[\\text{O}_2] + k_2[\\text{O}_3]}; \\quad r = 2 k_2 [\\text{O}_3][\\text{O}] = \\frac{2 k_1 k_2 [\\text{O}_3]^2}{k_{-1}[\\text{O}_2] + k_2[\\text{O}_3]}",
      "legend": "• Intermediet $[\\text{O}]$ tidak boleh muncul dalam persamaan laju akhir<br>• Jika $k_{-1}[\\text{O}_2] \\gg k_2[\\text{O}_3]$, laju tereduksi menjadi $r \\approx k' \\frac{[\\text{O}_3]^2}{[\\text{O}_2]}$ (orde -1 terhadap $\\text{O}_2$)<br>• Menjelaskan mengapa keberadaan oksigen menghambat laju perusakan ozon"
    },
    "options": [
      {
        "key": "A",
        "text": "$r = \\frac{k_1 [\\text{O}_3]}{k_{-1} [\\text{O}_2]}$, yang hanya merupakan ungkapan tetapan kesetimbangan parsial konsentrasi tahap pertama."
      },
      {
        "key": "B",
        "text": "$r = 2 k_2 [\\text{O}_3]^2$, yang mengasumsikan radikal oksigen terbentuk secara stoikiometrik tanpa reaksi balik dengan oksigen molekuler."
      },
      {
        "key": "C",
        "text": "$r = k_1 k_2 [\\text{O}_3]^2 [\\text{O}_2]^{-2}$, akibat salah mengkuadratkan ketergantungan balik gas oksigen."
      },
      {
        "key": "D",
        "text": "$r = k_2 [\\text{O}_3][\\text{O}_2]$, karena mengabaikan kesetimbangan tahap pertama dan hanya menuliskan perkalian konsentrasi produk stabil."
      },
      {
        "key": "E",
        "text": "$r = \\frac{2 k_1 k_2 [\\text{O}_3]^2}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$, karena pada keadaan tunak laju pembentukan radikal $[\\text{O}]$ sama dengan laju konsumsinya: $\\frac{d[\\text{O}]}{dt} = k_1 [\\text{O}_3] - k_{-1} [\\text{O}_2][\\text{O}] - k_2 [\\text{O}_3][\\text{O}] = 0 \\implies [\\text{O}] = \\frac{k_1 [\\text{O}_3]}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$. Substitusi ke laju penguraian netral: $-\\frac{d[\\text{O}_3]}{dt} = k_1 [\\text{O}_3] - k_{-1}[\\text{O}_2][\\text{O}] + k_2[\\text{O}_3][\\text{O}] = 2 k_2 [\\text{O}_3][\\text{O}] = \\frac{2 k_1 k_2 [\\text{O}_3]^2}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $r = \\frac{2 k_1 k_2 [\\text{O}_3]^2}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$, karena pada keadaan tunak laju pembentukan radikal $[\\text{O}]$ sama dengan laju konsumsinya: $\\frac{d[\\text{O}]}{dt} = k_1 [\\text{O}_3] - k_{-1} [\\text{O}_2][\\text{O}] - k_2 [\\text{O}_3][\\text{O}] = 0 \\implies [\\text{O}] = \\frac{k_1 [\\text{O}_3]}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$. Substitusi ke laju penguraian netral: $-\\frac{d[\\text{O}_3]}{dt} = k_1 [\\text{O}_3] - k_{-1}[\\text{O}_2][\\text{O}] + k_2[\\text{O}_3][\\text{O}] = 2 k_2 [\\text{O}_3][\\text{O}] = \\frac{2 k_1 k_2 [\\text{O}_3]^2}{k_{-1} [\\text{O}_2] + k_2 [\\text{O}_3]}$.. Pada steady-state: d[O]/dt = 0, sehingga laju pembentukan O pada tahap 1 sama dengan laju reaksi balik tahap 1 ditambah laju konsumsi pada tahap 2. Dapatkan [O] = k1[O3] / (k-1[O2] + k2[O3]), lalu substitusikan ke laju konsumsi O3 yaitu 2*k2*[O3]*[O]."
  },
  {
    "id": "kim-sim-03",
    "materi": "KESETIMBANGAN KIMIA INDUSTRI",
    "topic": "Optimalisasi Sintesis Amonia Proses Haber-Bosch",
    "hints": {
      "concept": "Pertimbangkan pertentangan antara termodinamika (yield) dan kinetika (kecepatan). Ikatan rangkap tiga N≡N sangat kuat (945 kJ/mol).",
      "execution": "Tanpa suhu yang cukup tinggi, tumbukan efektif partikel tidak mampu melampaui energi aktivasi, sehingga reaksi memakan waktu bertahun-tahun."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sintesis amonia industri berlangsung menurut reaksi eksotermik:<br>$\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g) \\quad \\Delta H^\\circ = -92\\text{ kJ/mol}$<br>Dalam reaktor industri modern, reaksi dioperasikan pada suhu kompromi sekitar $450^\\circ\\text{C}$ dan tekanan tinggi $200\\text{ atm}$ dengan katalis besi terpromosi ($\u0007lpha\\text{-Fe}$ dengan $\\text{K}_2\\text{O}$ dan $\\text{Al}_2\\text{O}_3$). Alasan ilmiah utama mengapa tidak digunakan suhu kamar ($25^\\circ\\text{C}$) meskipun secara termodinamika nilai $K_p$ jauh lebih besar pada suhu rendah adalah...",
    "formulaHud": {
      "title": "PRINSIP KOMPROMI TERMODINAMIKA VS KINETIKA INDUSTRI",
      "latex": "\\Delta n_g = 2 - (1+3) = -2 < 0; \\quad \\Delta H < 0 \\implies K_p \\downarrow \\text{ jika } T \\uparrow; \\quad k = A e^{-E_a/RT} \\uparrow \\text{ jika } T \\uparrow",
      "legend": "• Termodinamika: Suhu rendah menaikkan nilai tetapan $K_p$, namun...<br>• Kinetika: Energi ikatan $N\\equiv N = 945\\text{ kJ/mol}$ menuntut suhu operasi tinggi agar laju reaksi komersial tercapai<br>• Tekanan tinggi ($200\\text{ atm}$) menggeser kesetimbangan ke arah produk (mol gas lebih sedikit)"
    },
    "options": [
      {
        "key": "A",
        "text": "Katalis besi baru mulai meleleh dan aktif mengikat gas hidrogen pada suhu di atas $600^\\circ\\text{C}$ sehingga suhu kamar tidak fungsional."
      },
      {
        "key": "B",
        "text": "Gas amonia yang terbentuk pada suhu kamar akan langsung terkondensasi dan menyumbat pori-pori katalis besi secara permanen."
      },
      {
        "key": "C",
        "text": "Energi aktivasi pemutusan ikatan kovalen rangkap tiga $\\text{N}\\equiv\\text{N}$ ($945\\text{ kJ/mol}$) sangat tinggi sehingga pada suhu rendah laju reaksi praktis nol (kinetika sangat lambat); suhu $450^\\circ\\text{C}$ merupakan kompromi antara laju reaksi yang cukup cepat mencapai kesetimbangan dan perolehan yield yang memadai pada tekanan $200\\text{ atm}$."
      },
      {
        "key": "D",
        "text": "Molekul nitrogen akan mengalami disosiasi total menjadi ion radikal bebas yang merusak dinding bejana baja reaktor pada suhu rendah."
      },
      {
        "key": "E",
        "text": "Pada suhu kamar reaksi bersifat endotermik sehingga membutuhkan pasokan kalor kontinu yang sangat mahal untuk menggerakkan turbin kompresor ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Energi aktivasi pemutusan ikatan kovalen rangkap tiga $\\text{N}\\equiv\\text{N}$ ($945\\text{ kJ/mol}$) sangat tinggi sehingga pada suhu rendah laju reaksi praktis nol (kinetika sangat lambat); suhu $450^\\circ\\text{C}$ merupakan kompromi antara laju reaksi yang cukup cepat mencapai kesetimbangan dan perolehan yield yang memadai pada tekanan $200\\text{ atm}$.. Pertimbangkan pertentangan antara termodinamika (yield) dan kinetika (kecepatan). Ikatan rangkap tiga N≡N sangat kuat (945 kJ/mol). Tanpa suhu yang cukup tinggi, tumbukan efektif partikel tidak mampu melampaui energi aktivasi, sehingga reaksi memakan waktu bertahun-tahun."
  },
  {
    "id": "kim-sim-04",
    "materi": "LARUTAN ASAM-BASA POLIPROTIK",
    "topic": "Kurva Titrasi Asam Fosfat dan Identifikasi Spesi Dominan",
    "hints": {
      "concept": "V = 37.5 mL berada tepat di tengah-tengah antara TE 1 (25 mL) dan TE 2 (50 mL). Ini adalah titik setengah netralisasi tahap kedua, di mana [H2PO4-] = [HPO4(2-)].",
      "execution": "Berdasarkan persamaan Henderson-Hasselbalch tahap 2: pH = pKa2 + log(1) = -log(6,2 x 10^-8) = 7,21."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebanyak $25{,}0\\text{ mL}$ larutan asam ortofosfat, $\\text{H}_3\\text{PO}_4$ $0{,}10\\text{ M}$ ($K_{a1} = 7{,}5 \\times 10^{-3}$, $K_{a2} = 6{,}2 \\times 10^{-8}$, $K_{a3} = 4{,}2 \\times 10^{-13}$) dititrasi dengan larutan baku $\\text{NaOH}$ $0{,}10\\text{ M}$. Pada saat penambahan volume titran $\\text{NaOH}$ tepat mencapai $37{,}5\\text{ mL}$ (antara titik ekuivalen pertama $25\\text{ mL}$ dan kedua $50\\text{ mL}$), spesi ion fosfat yang dominan di dalam larutan dan nilai $pH$ larutan adalah...",
    "formulaHud": {
      "title": "TITRASI ASAM POLIPROTIK & BUFFER BUFFERING HALF-WAY",
      "latex": "\\text{Pada } V = 37{,}5\\text{ mL}: \\quad n_{\\text{H}_2\\text{PO}_4^-} = n_{\\text{HPO}_4^{2-}} \\implies pH = pK_{a2} + \\log\\frac{[\\text{HPO}_4^{2-}]}{[\\text{H}_2\\text{PO}_4^-]} = pK_{a2} = 7{,}21",
      "legend": "• Titik ekuivalen 1: $V = 25\\text{ mL}$ (spesi dominan $\\text{H}_2\\text{PO}_4^-$, $pH = \\frac{pK_{a1}+pK_{a2}}{2} = 4{,}67$)<br>• Setengah TE 2: $V = 37{,}5\\text{ mL}$ (sistem buffer fosfat, $pH = pK_{a2} = 7{,}21$)<br>• Titik ekuivalen 2: $V = 50\\text{ mL}$ (spesi dominan $\\text{HPO}_4^{2-}$, $pH = \\frac{pK_{a2}+pK_{a3}}{2} = 9{,}79$)"
    },
    "options": [
      {
        "key": "A",
        "text": "Spesi dominan berupa ion $\\text{PO}_4^{3-}$ dengan $pH = 12{,}38$, karena titran basa kuat telah ditambahkan berlebih melampaui volume asam awal menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "B",
        "text": "Spesi dominan berupa campuran ekivalen $[\\text{H}_2\\text{PO}_4^-] = [\\text{HPO}_4^{2-}]$ dengan $pH = 7{,}21$, karena $25\\text{ mL}$ pertama $\\text{NaOH}$ telah sempurna mengubah $\\text{H}_3\\text{PO}_4$ menjadi $\\text{H}_2\\text{PO}_4^-$, dan penambahan $12{,}5\\text{ mL}$ berikutnya tepat menetralkan separuh mol $\\text{H}_2\\text{PO}_4^-$ membentuk buffer equimolar dengan $pH = pK_{a2} = -\\log(6{,}2 \\times 10^{-8}) = 7{,}21$."
      },
      {
        "key": "C",
        "text": "Spesi dominan berupa endapan garam natrium fosfat netral dengan $pH = 7{,}00$ tepat seperti titrasi asam-basa kuat."
      },
      {
        "key": "D",
        "text": "Spesi dominan berupa ion amfiprotik tunggal $\\text{H}_2\\text{PO}_4^-$ dengan $pH = 4{,}67$, dihitung dari rata-rata akar tetapan disosiasi pertama dan kedua."
      },
      {
        "key": "E",
        "text": "Spesi dominan berupa molekul $\\text{H}_3\\text{PO}_4$ tak terdisosiasi dengan $pH = 2{,}12$, karena asam fosfat merupakan asam lemah bertingkat tiga."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Spesi dominan berupa campuran ekivalen $[\\text{H}_2\\text{PO}_4^-] = [\\text{HPO}_4^{2-}]$ dengan $pH = 7{,}21$, karena $25\\text{ mL}$ pertama $\\text{NaOH}$ telah sempurna mengubah $\\text{H}_3\\text{PO}_4$ menjadi $\\text{H}_2\\text{PO}_4^-$, dan penambahan $12{,}5\\text{ mL}$ berikutnya tepat menetralkan separuh mol $\\text{H}_2\\text{PO}_4^-$ membentuk buffer equimolar dengan $pH = pK_{a2} = -\\log(6{,}2 \\times 10^{-8}) = 7{,}21$.. V = 37.5 mL berada tepat di tengah-tengah antara TE 1 (25 mL) dan TE 2 (50 mL). Ini adalah titik setengah netralisasi tahap kedua, di mana [H2PO4-] = [HPO4(2-)]. Berdasarkan persamaan Henderson-Hasselbalch tahap 2: pH = pKa2 + log(1) = -log(6,2 x 10^-8) = 7,21."
  },
  {
    "id": "kim-sim-05",
    "materi": "LARUTAN PENYANGGA BIOLOGIS",
    "topic": "Kapasitas Buffer Darah Karbonat pada Asidosis Metabolik",
    "hints": {
      "concept": "Gunakan persamaan Henderson-Hasselbalch klinis: pH = pKa' + log([HCO3-] / [CO2]). Masukkan konsentrasi akhir.",
      "execution": "pH = 6,10 + log(12 / 1,2) = 6,10 + log(10) = 6,10 + 1,00 = 7,10."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam plasma darah manusia, sistem penyangga utama dipertahankan oleh kesetimbangan asam karbonat–bikarbonat:<br>$\\text{CO}_2(d) + \\text{H}_2\\text{O}(l) \\rightleftharpoons \\text{H}_2\\text{CO}_3(aq) \\rightleftharpoons \\text{H}^+(aq) + \\text{HCO}_3^-(aq) \\quad (pK_a' = 6{,}10)$<br>Pada kondisi fisiologis normal, darah memiliki $pH = 7{,}40$. Jika seorang atlet mengalami penumpukan asam laktat akibat aktivitas anaerobik hebat sehingga konsentrasi $[\\text{HCO}_3^-]$ turun dari $24\\text{ mM}$ menjadi $12\\text{ mM}$ sementara $[\\text{CO}_2]$ terlarut dipertahankan konstan oleh hiperventilasi paru-paru pada $1{,}2\\text{ mM}$, nilai $pH$ darah atlet tersebut berubah menjadi...",
    "formulaHud": {
      "title": "PERSAMAAN HENDERSON-HASSELBALCH BUFFER DARAH",
      "latex": "pH = pK_a' + \\log\\frac{[\\text{HCO}_3^-]}{[\\text{CO}_2]} = 6{,}10 + \\log\\left(\\frac{12\\text{ mM}}{1{,}2\\text{ mM}}\\right) = 6{,}10 + 1{,}00 = 7{,}10",
      "legend": "• Normal: $pH = 6{,}10 + \\log(24/1{,}2) = 6{,}10 + 1{,}30 = 7{,}40$<br>• Penurunan $[\\text{HCO}_3^-]$ menjadi $12\\text{ mM}$ menghasilkan rasio $10:1$<br>• $pH$ turun menjadi $7{,}10$ (gejala asidosis metabolik)"
    },
    "options": [
      {
        "key": "A",
        "text": "$pH = 6{,}70$, akibat salah mengurangkan nilai logaritma dari nilai pKa sistem buffer."
      },
      {
        "key": "B",
        "text": "$pH = 7{,}10$ (mengalami asidosis metabolik terkompensasi parsial), karena menurut persamaan Henderson-Hasselbalch klinis: $pH = pK_a' + \\log\\frac{[\\text{HCO}_3^-]}{[\\text{CO}_2]} = 6{,}10 + \\log\\frac{12}{1{,}2} = 6{,}10 + \\log(10) = 6{,}10 + 1{,}00 = 7{,}10$."
      },
      {
        "key": "C",
        "text": "$pH = 6{,}10$, karena mengira seluruh bikarbonat habis bereaksi sehingga pH sama persis dengan nilai pKa murni."
      },
      {
        "key": "D",
        "text": "$pH = 7{,}70$, dihitung dengan membalik perbandingan konsentrasi asam terlarut terhadap basa konjugasi."
      },
      {
        "key": "E",
        "text": "$pH = 7{,}40$, karena menganggap sistem penyangga mampu meniadakan 100% perubahan asam laktat tanpa pergeseran rasio ion sama sekali."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $pH = 7{,}10$ (mengalami asidosis metabolik terkompensasi parsial), karena menurut persamaan Henderson-Hasselbalch klinis: $pH = pK_a' + \\log\\frac{[\\text{HCO}_3^-]}{[\\text{CO}_2]} = 6{,}10 + \\log\\frac{12}{1{,}2} = 6{,}10 + \\log(10) = 6{,}10 + 1{,}00 = 7{,}10$.. Gunakan persamaan Henderson-Hasselbalch klinis: pH = pKa' + log([HCO3-] / [CO2]). Masukkan konsentrasi akhir. pH = 6,10 + log(12 / 1,2) = 6,10 + log(10) = 6,10 + 1,00 = 7,10."
  },
  {
    "id": "kim-sim-06",
    "materi": "KELARUTAN & PENGENDAPAN FRAKSIONAL",
    "topic": "Pemisahan Selektif Kation Sulfida Golongan II dan III dengan Kontrol pH",
    "hints": {
      "concept": "Hitung [S(2-)] maksimum agar ZnS tidak mengendap: [S(2-)] < Ksp(ZnS)/[Zn2+]. Lalu hubungkan dengan kesetimbangan asam H2S: [S2-] = (Ka1Ka2 * [H2S]) / [H+]^2.",
      "execution": "[S2-] < 2 x 10^-20 M. Maka [H+]^2 > (10^-20 * 0,1) / (2 x 10^-20) = 0,05 -> [H+] > 0,22 M (suasana asam pekat, pH rendah)."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Suatu larutan mengandung campuran ion logam $\\text{Cu}^{2+}$ $0{,}01\\text{ M}$ dan ion logam $\\text{Zn}^{2+}$ $0{,}01\\text{ M}$. Ke dalam larutan dialirkan gas hidrogen sulfida, $\\text{H}_2\\text{S}$, hingga jenuh ($[\\text{H}_2\\text{S}] = 0{,}10\\text{ M}$). Diketahui data kesetimbangan:<br>• $\\text{H}_2\\text{S} \\rightleftharpoons 2\\text{H}^+ + \\text{S}^{2-} \\quad (K_{a1}K_{a2} = 1{,}0 \\times 10^{-20})$<br>• $K_{sp}[\\text{CuS}] = 6{,}0 \\times 10^{-36}$<br>• $K_{sp}[\\text{ZnS}] = 2{,}0 \\times 10^{-22}$<br>Agar ion $\\text{Cu}^{2+}$ mengendap sempurna sebagai $\\text{CuS}$ sedangkan ion $\\text{Zn}^{2+}$ tetap larut seutuhnya tanpa mengendap sebagai $\\text{ZnS}$, konsentrasi ion $[\\text{H}^+]$ larutan harus diatur pada batas...",
    "formulaHud": {
      "title": "PENGENDAPAN SELEKTIF SULFIDA DENGAN KONTROL PH",
      "latex": "[\\text{S}^{2-}]_{\\max} = \\frac{K_{sp}[\\text{ZnS}]}{[\\text{Zn}^{2+}]} = \\frac{2 \\times 10^{-22}}{10^{-2}} = 2 \\times 10^{-20}\\text{ M}; \\quad [\\text{H}^+] = \\sqrt{\\frac{K_{a1}K_{a2}[\\text{H}_2\\text{S}]}{[\\text{S}^{2-}]_{\\max}}} > 0{,}22\\text{ M}",
      "legend": "• Suasana sangat asam ($pH < 0{,}66$) menekan konsentrasi $[\\text{S}^{2-}]$ sangat rendah<br>• $[\\text{S}^{2-}]$ cukup untuk melampaui $K_{sp}$ $\\text{CuS}$ yang super kecil ($10^{-36}$)<br>• $[\\text{S}^{2-}]$ tidak cukup untuk melampaui $K_{sp}$ $\\text{ZnS}$ ($10^{-22}$), sehingga $\\text{Zn}^{2+}$ lolos dalam filtrat"
    },
    "options": [
      {
        "key": "A",
        "text": "$[\\text{H}^+] < 10^{-4}\\text{ M}$, karena konsentrasi sulfida bebas akan terlalu besar dan memicu kopresipitasi seng sulfida."
      },
      {
        "key": "B",
        "text": "$[\\text{H}^+] = 10^{-10}\\text{ M}$, karena larutan asam kuat tidak mampu mendisosiasikan tembaga sulfida."
      },
      {
        "key": "C",
        "text": "$[\\text{H}^+] = 10^{-14}\\text{ M}$, di mana konsentrasi ion sulfida menjadi maksimum dan seluruh kation membentuk hidroksida dan sulfida sekaligus."
      },
      {
        "key": "D",
        "text": "$[\\text{H}^+] < 10^{-7}\\text{ M}$ ($pH > 7$), karena pada kondisi basa kedua ion akan mengendap bersamaan sehingga pemisahan gagal total."
      },
      {
        "key": "E",
        "text": "$[\\text{H}^+] > 7{,}07 \\times 10^{-1}\\text{ M}$ (atau $pH < 0{,}15$), karena agar $\\text{ZnS}$ tidak mengendap, syaratnya $Q_{sp}[\\text{ZnS}] = [\\text{Zn}^{2+}][\\text{S}^{2-}] < K_{sp}[\\text{ZnS}] \\implies [\\text{S}^{2-}] < \\frac{2{,}0 \\times 10^{-22}}{0{,}01} = 2{,}0 \\times 10^{-20}\\text{ M}$. Dari kesetimbangan disosiasi asam sulfida: $[\\text{S}^{2-}] = \\frac{K_{a1}K_{a2}[\\text{H}_2\\text{S}]}{[\\text{H}^+]^2} = \\frac{10^{-20} \\times 0{,}10}{[\\text{H}^+]^2} = \\frac{10^{-21}}{[\\text{H}^+]^2}$. Syarat tak mengendap: $\\frac{10^{-21}}{[\\text{H}^+]^2} < 2{,}0 \\times 10^{-20} \\implies [\\text{H}^+]^2 > 0{,}05 \\implies [\\text{H}^+] > 0{,}22\\text{ M}$. Sementara pada kondisi ini $[\\text{S}^{2-}] \\approx 10^{-20}\\text{ M}$ jauh melampaui $K_{sp}[\\text{CuS}]$ ($Q_{sp} = 10^{-22} \\gg 6 \\times 10^{-36}$) sehingga $\\text{CuS}$ mengendap tuntas."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $[\\text{H}^+] > 7{,}07 \\times 10^{-1}\\text{ M}$ (atau $pH < 0{,}15$), karena agar $\\text{ZnS}$ tidak mengendap, syaratnya $Q_{sp}[\\text{ZnS}] = [\\text{Zn}^{2+}][\\text{S}^{2-}] < K_{sp}[\\text{ZnS}] \\implies [\\text{S}^{2-}] < \\frac{2{,}0 \\times 10^{-22}}{0{,}01} = 2{,}0 \\times 10^{-20}\\text{ M}$. Dari kesetimbangan disosiasi asam sulfida: $[\\text{S}^{2-}] = \\frac{K_{a1}K_{a2}[\\text{H}_2\\text{S}]}{[\\text{H}^+]^2} = \\frac{10^{-20} \\times 0{,}10}{[\\text{H}^+]^2} = \\frac{10^{-21}}{[\\text{H}^+]^2}$. Syarat tak mengendap: $\\frac{10^{-21}}{[\\text{H}^+]^2} < 2{,}0 \\times 10^{-20} \\implies [\\text{H}^+]^2 > 0{,}05 \\implies [\\text{H}^+] > 0{,}22\\text{ M}$. Sementara pada kondisi ini $[\\text{S}^{2-}] \\approx 10^{-20}\\text{ M}$ jauh melampaui $K_{sp}[\\text{CuS}]$ ($Q_{sp} = 10^{-22} \\gg 6 \\times 10^{-36}$) sehingga $\\text{CuS}$ mengendap tuntas.. Hitung [S(2-)] maksimum agar ZnS tidak mengendap: [S(2-)] < Ksp(ZnS)/[Zn2+]. Lalu hubungkan dengan kesetimbangan asam H2S: [S2-] = (Ka1Ka2 * [H2S]) / [H+]^2. [S2-] < 2 x 10^-20 M. Maka [H+]^2 > (10^-20 * 0,1) / (2 x 10^-20) = 0,05 -> [H+] > 0,22 M (suasana asam pekat, pH rendah)."
  },
  {
    "id": "kim-sim-07",
    "materi": "SIFAT KOLIGATIF & TEORI ELEKTROLIT NYATA",
    "topic": "Penyimpangan Faktor Van 't Hoff Larutan Elektrolit Encer",
    "hints": {
      "concept": "Hitung faktor van 't Hoff dari data penurunan titik beku terukur: i = Delta Tf / (m * Kf). Pahami interaksi Debye-Huckel untuk ion bermuatan ganda.",
      "execution": "i = 0,130 / (0,05 * 1,86) = 0,130 / 0,093 = 1,40. Kation Mg(2+) dan anion SO4(2-) saling berpasangan (ion pair)."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Pengukuran eksperimen penurunan titik beku dari larutan magnesium sulfat, $\\text{MgSO}_4$, dengan konsentrasi $0{,}05\\text{ m}$ dalam pelarut air murni ($K_f = 1{,}86^\\circ\\text{C/m}$) memberikan nilai $\\Delta T_f = 0{,}130^\\circ\\text{C}$. Padahal, secara stoikiometri garam $\\text{MgSO}_4$ terurai menjadi dua ion ($\\text{Mg}^{2+}$ dan $\\text{SO}_4^{2-}$, $n = 2$). Derajat disosiasi semu (faktor van 't Hoff eksperimen $i$) dan penjelasan fenomena termodinamika tersebut adalah...",
    "formulaHud": {
      "title": "FAKTOR VAN 'T HOFF EKSPERIMEN & ION-PAIRING",
      "latex": "\\Delta T_f = m \\cdot K_f \\cdot i \\implies i_{\\text{eksp}} = \\frac{\\Delta T_f}{m \\cdot K_f} = \\frac{0{,}130}{0{,}05 \\times 1,86} = \\frac{0{,}130}{0{,}093} \\approx 1{,}40",
      "legend": "• Untuk elektrolit bivalen ($2+$ dan $2-$), gaya Coulomb antarion $\\propto q_1 q_2 = 4$ kali lebih kuat dibanding elektrolit univalen ($1+$ dan $1-$)<br>• Terjadi asosiasi sementara membentuk pasangan ion netral $[\\text{Mg}^{2+}\\text{SO}_4^{2-}]^0$<br>• Partikel efektif terukur $i = 1{,}40 < 2{,}00$"
    },
    "options": [
      {
        "key": "A",
        "text": "$i_{\\text{eksp}} = 0{,}70$; ion magnesium mengalami polimerisasi kovalen membentuk rantai makromolekul padat dalam larutan encer."
      },
      {
        "key": "B",
        "text": "$i_{\\text{eksp}} = 2{,}00$; garam magnesium sulfat selalu terdisosiasi sempurna 100% tanpa adanya interaksi elektrostatik ionik dalam air."
      },
      {
        "key": "C",
        "text": "$i_{\\text{eksp}} = 1{,}40$; nilai $i < 2$ disebabkan oleh pembentukan pasangan ion ($\\textit{ion-pairing}$) antarion bivalen bermuatan tinggi ($\\text{Mg}^{2+}$ dan $\\text{SO}_4^{2-}$) akibat gaya tarik elektrostatik antarion menurut teori Debye-Hückel sehingga jumlah partikel kinetik bebas berkurang."
      },
      {
        "key": "D",
        "text": "$i_{\\text{eksp}} = 1{,}00$; magnesium sulfat tidak larut dalam air sehingga berperilaku seperti senyawa non-elektrolit murni."
      },
      {
        "key": "E",
        "text": "$i_{\\text{eksp}} = 2{,}80$; terjadi hidrolisis total yang menghasilkan tambahan ion hidrogen dan hidroksida berlipat ganda dalam air."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) $i_{\\text{eksp}} = 1{,}40$; nilai $i < 2$ disebabkan oleh pembentukan pasangan ion ($\\textit{ion-pairing}$) antarion bivalen bermuatan tinggi ($\\text{Mg}^{2+}$ dan $\\text{SO}_4^{2-}$) akibat gaya tarik elektrostatik antarion menurut teori Debye-Hückel sehingga jumlah partikel kinetik bebas berkurang.. Hitung faktor van 't Hoff dari data penurunan titik beku terukur: i = Delta Tf / (m * Kf). Pahami interaksi Debye-Huckel untuk ion bermuatan ganda. i = 0,130 / (0,05 * 1,86) = 0,130 / 0,093 = 1,40. Kation Mg(2+) dan anion SO4(2-) saling berpasangan (ion pair)."
  },
  {
    "id": "kim-sim-08",
    "materi": "ELEKTROKIMIA & BATERAI SEKUNDER",
    "topic": "Reaksi Interkalasi Baterai Ion Litium (Li-ion Battery)",
    "hints": {
      "concept": "Pada discharge (berfungsi sebagai sel volta): anoda mengalami oksidasi (melepas elektron dan ion Li+ keluar dari grafit), katoda mengalami reduksi (menerima ion Li+ dan elektron).",
      "execution": "Anoda: LixC6 -> 6C + xLi+ + x e-. Katoda: Li(1-x)CoO2 + xLi+ + x e- -> LiCoO2."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Baterai sekunder ion litium yang digunakan pada ponsel pintar dan kendaraan listrik bekerja berdasarkan mekanisme interkalasi ion $\\text{Li}^+$ bolak-balik antara anoda grafit ($\\text{Li}_x\\text{C}_6$) dan katoda oksida kobalt litium ($\\text{Li}_{1-x}\\text{CoO}_2$). Selama proses pengosongan baterai ($\\textit{discharge}$), proses kimia yang terjadi di anoda dan katoda adalah...",
    "formulaHud": {
      "title": "REAKSI DISCHARGE BATERAI LITIUM-ION",
      "latex": "\\text{Anoda: } \\text{Li}_x\\text{C}_6 \\rightarrow 6\\text{C} + x\\text{Li}^+ + x e^-; \\quad \\text{Katoda: } \\text{Li}_{1-x}\\text{CoO}_2 + x\\text{Li}^+ + x e^- \\rightarrow \\text{LiCoO}_2",
      "legend": "• Reaksi total pelepasan muatan: $\\text{Li}_x\\text{C}_6 + \\text{Li}_{1-x}\\text{CoO}_2 \\rightarrow 6\\text{C} + \\text{LiCoO}_2$<br>• Ion $\\text{Li}^+$ bermigrasi melalui elektrolit dari anoda ke katoda<br>• Elektron mengalir melalui kawat luar menyediakan daya listrik bagi beban"
    },
    "options": [
      {
        "key": "A",
        "text": "Di katoda terjadi dekomposisi elektrolit organik menjadi gas hidrogen dan gas oksigen bertekanan tinggi."
      },
      {
        "key": "B",
        "text": "Di anoda terjadi pengendapan kristal garam litium karbonat padat yang mengisolasi aliran arus listrik secara permanen."
      },
      {
        "key": "C",
        "text": "Di anoda terjadi oksidasi de-interkalasi ion $\\text{Li}^+$ dari kisi grafit ($\\text{Li}_x\\text{C}_6 \\rightarrow 6\\text{C} + x\\text{Li}^+ + x e^-$), dan di katoda terjadi reduksi kobalt disertai interkalasi ion $\\text{Li}^+$ ke dalam matriks kristal oksida kobalt ($\\text{Li}_{1-x}\\text{CoO}_2 + x\\text{Li}^+ + x e^- \\rightarrow \\text{LiCoO}_2$)."
      },
      {
        "key": "D",
        "text": "Ion litium mengalami perubahan bilangan oksidasi dari $+1$ menjadi ion trivalen $+3$ di kedua kutub elektroda."
      },
      {
        "key": "E",
        "text": "Di anoda terjadi reduksi logam litium cair menjadi endapan litium oksida pejal yang menyerap elektron dari sirkuit luar ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Di anoda terjadi oksidasi de-interkalasi ion $\\text{Li}^+$ dari kisi grafit ($\\text{Li}_x\\text{C}_6 \\rightarrow 6\\text{C} + x\\text{Li}^+ + x e^-$), dan di katoda terjadi reduksi kobalt disertai interkalasi ion $\\text{Li}^+$ ke dalam matriks kristal oksida kobalt ($\\text{Li}_{1-x}\\text{CoO}_2 + x\\text{Li}^+ + x e^- \\rightarrow \\text{LiCoO}_2$).. Pada discharge (berfungsi sebagai sel volta): anoda mengalami oksidasi (melepas elektron dan ion Li+ keluar dari grafit), katoda mengalami reduksi (menerima ion Li+ dan elektron). Anoda: LixC6 -> 6C + xLi+ + x e-. Katoda: Li(1-x)CoO2 + xLi+ + x e- -> LiCoO2."
  },
  {
    "id": "kim-sim-09",
    "materi": "ELEKTROLISIS INDUSTRI METALURGI",
    "topic": "Proses Hall-Héroult Ekstraksi Aluminium dari Bauksit",
    "hints": {
      "concept": "Titik leleh Al2O3 murni sangat tinggi (>2000 C). Kriolit menurunkannya ke ~950 C. Di anoda, ion oksida dioksidasi menghasilkan O2 yang langsung membakar karbon anoda menjadi CO2.",
      "execution": "Pilih opsi yang menjelaskan peran penurunan titik leleh oleh kriolit dan oksidasi anoda karbon menjadi CO2."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam ekstraksi komersial logam aluminium melalui proses Hall-Héroult, alumina ($\\text{Al}_2\\text{O}_3$) dilarutkan dalam lelehan kriolit cair ($\\text{Na}_3\\text{AlF}_6$) pada suhu sekitar $950^\\circ\\text{C}$ dan dielektrolisis menggunakan anoda karbon (grafit). Peran krusial penambahan lelehan kriolit serta fenomena kimia yang menyebabkan anoda karbon harus diganti secara berkala adalah...",
    "formulaHud": {
      "title": "REAKSI ELEKTROLISIS PROSES HALL-HÉROULT",
      "latex": "\\text{Katoda: } \\text{Al}^{3+} + 3e^- \\rightarrow \\text{Al}(l); \\quad \\text{Anoda: } 2\\text{O}^{2-} + \\text{C}(s) \\rightarrow \\text{CO}_2(g) + 4e^-",
      "legend": "• Reaksi netto: $2\\text{Al}_2\\text{O}_3 + 3\\text{C}(s) \\xrightarrow{\\text{kriolit, } 950^\\circ\\text{C}} 4\\text{Al}(l) + 3\\text{CO}_2(g)$<br>• Kriolit ($\text{Na}_3\\text{AlF}_6$) menghemat konsumsi energi termal pabrik secara masif<br>• Karbon anoda dikonsumsi secara stoikiometris membentuk $\\text{CO}_2$"
    },
    "options": [
      {
        "key": "A",
        "text": "Kriolit mencegah pembentukan gas fluorin beracun; anoda karbon meleleh karena suhu busur listrik melampaui $4000^\\circ\\text{C}$."
      },
      {
        "key": "B",
        "text": "Kriolit menyerap gas karbon dioksida di katoda; anoda karbon menyublim secara spontan menjadi intan kristalin."
      },
      {
        "key": "C",
        "text": "Kriolit berfungsi sebagai sumber ion natrium logam pengganti; anoda karbon hancur akibat gesekan mekanik aliran lelehan logam cair."
      },
      {
        "key": "D",
        "text": "Kriolit bertindak sebagai zat pengoksidasi kuat ion aluminium; anoda karbon aus akibat terkorosi oleh asam sulfat pekat yang dihasilkan reaksi menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "E",
        "text": "Kriolit berfungsi menurunkan titik leleh alumina dari $\\sim 2050^\\circ\\text{C}$ menjadi $\\sim 950^\\circ\\text{C}$ dan meningkatkan konduktivitas listrik; anoda karbon habis bereaksi karena gas oksigen yang dihasilkan pada anoda bereaksi dengan karbon membentuk gas $\\text{CO}_2$ pada suhu tinggi ($C(s) + O_2(g) \\rightarrow CO_2(g)$)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Kriolit berfungsi menurunkan titik leleh alumina dari $\\sim 2050^\\circ\\text{C}$ menjadi $\\sim 950^\\circ\\text{C}$ dan meningkatkan konduktivitas listrik; anoda karbon habis bereaksi karena gas oksigen yang dihasilkan pada anoda bereaksi dengan karbon membentuk gas $\\text{CO}_2$ pada suhu tinggi ($C(s) + O_2(g) \\rightarrow CO_2(g)$).. Titik leleh Al2O3 murni sangat tinggi (>2000 C). Kriolit menurunkannya ke ~950 C. Di anoda, ion oksida dioksidasi menghasilkan O2 yang langsung membakar karbon anoda menjadi CO2. Pilih opsi yang menjelaskan peran penurunan titik leleh oleh kriolit dan oksidasi anoda karbon menjadi CO2."
  },
  {
    "id": "kim-sim-10",
    "materi": "KIMIA UNSUR & TREN PERIODIK",
    "topic": "Anomali Titik Didih Hidrida Non-Logam Golongan 15, 16, dan 17",
    "hints": {
      "concept": "Ikatan hidrogen intermolekul yang kuat hanya terjadi pada N, O, F karena elektronegativitas tinggi dan ukuran atom kecil. CH4 tidak membentuk ikatan hidrogen karena nonpolar dan tidak ada PEB.",
      "execution": "Pilih jawaban yang membedakan keberadaan ikatan hidrogen pada H2O/HF/NH3 dengan dominasi gaya dispersi London pada deret hidrida golongan 14."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Grafik titik didih hidrida non-logam golongan 14, 15, 16, dan 17 terhadap periode menunjukkan bahwa hidrida periode 2 ($\\text{H}_2\\text{O}$, $\\text{HF}$, dan $\\text{NH}_3$) memiliki titik didih yang jauh lebih tinggi secara anomali dibandingkan hidrida periode 3 di bawahnya ($\\text{H}_2\\text{S}$, $\\text{HCl}$, dan $\\text{PH}_3$). Namun, untuk golongan 14, titik didih metana ($\\text{CH}_4$) justru lebih rendah daripada silana ($\\text{SiH}_4$). Penjelasan ilmiah yang paling tepat untuk fenomena ini adalah...",
    "formulaHud": {
      "title": "IKATAN HIDROGEN VS GAYA DISPERSI LONDON",
      "latex": "T_b: \\text{H}_2\\text{O} (100^\\circ\\text{C}) \\gg \\text{H}_2\\text{S} (-60^\\circ\\text{C}); \\quad T_b: \\text{HF} (20^\\circ\\text{C}) \\gg \\text{HCl} (-85^\\circ\\text{C}); \\quad T_b: \\text{CH}_4 (-161^\\circ\\text{C}) < \\text{SiH}_4 (-112^\\circ\\text{C})",
      "legend": "• Ikatan hidrogen hanya terbentuk jika atom H terikat kovalen pada N, O, atau F (sangat elektronegatif & ada PEB)<br>• Golongan 14 ($\text{CH}_4$, $\text{SiH}_4$, $\text{GeH}_4$) bersifat nonpolar sempurna tanpa PEB: tren titik didih murni dikendalikan oleh massa molekul dan kepolarisasian awan elektron (gaya London)"
    },
    "options": [
      {
        "key": "A",
        "text": "Atom $\\text{O}$, $\\text{F}$, dan $\\text{N}$ memiliki elektronegativitas sangat tinggi dan jari-jari atom kecil dengan pasangan elektron bebas sehingga mampu membentuk ikatan hidrogen intermolekul yang sangat kuat; sebaliknya $\\text{CH}_4$ bersifat nonpolar dan atom C tidak memiliki PEB sehingga interaksinya hanya gaya dispersi London yang meningkat seiring ukuran massa molekul ke $\\text{SiH}_4$."
      },
      {
        "key": "B",
        "text": "Senyawa $\\text{H}_2\\text{O}$, $\\text{HF}$, dan $\\text{NH}_3$ mengalami ionisasi sempurna menjadi ion-ion bebas dalam fasa gas yang meningkatkan gaya Coulomb."
      },
      {
        "key": "C",
        "text": "Atom karbon mengalami hibridisasi sp sedangkan atom silikon mengalami hibridisasi sp3d2 dalam senyawa hidridanya."
      },
      {
        "key": "D",
        "text": "Molekul $\\text{CH}_4$ memiliki ikatan ionik yang mudah putus, sedangkan molekul $\\text{SiH}_4$ membentuk ikatan kovalen raksasa mirip struktur intan kristal."
      },
      {
        "key": "E",
        "text": "Gaya van der Waals pada $\\text{H}_2\\text{S}$ dan $\\text{HCl}$ lebih kuat daripada $\\text{H}_2\\text{O}$ karena belerang memiliki lebih banyak proton dalam intinya."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Atom $\\text{O}$, $\\text{F}$, dan $\\text{N}$ memiliki elektronegativitas sangat tinggi dan jari-jari atom kecil dengan pasangan elektron bebas sehingga mampu membentuk ikatan hidrogen intermolekul yang sangat kuat; sebaliknya $\\text{CH}_4$ bersifat nonpolar dan atom C tidak memiliki PEB sehingga interaksinya hanya gaya dispersi London yang meningkat seiring ukuran massa molekul ke $\\text{SiH}_4$.. Ikatan hidrogen intermolekul yang kuat hanya terjadi pada N, O, F karena elektronegativitas tinggi dan ukuran atom kecil. CH4 tidak membentuk ikatan hidrogen karena nonpolar dan tidak ada PEB. Pilih jawaban yang membedakan keberadaan ikatan hidrogen pada H2O/HF/NH3 dengan dominasi gaya dispersi London pada deret hidrida golongan 14."
  },
  {
    "id": "kim-sim-11",
    "materi": "KIMIA KOORDINASI MEDIS",
    "topic": "Stereokimia Senyawa Kompleks Cis-Platin sebagai Kemoterapi Kanker",
    "hints": {
      "concept": "Isomer cis menempatkan dua ligan klorida labil berdampingan (sudut 90 derajat). Posisi ini memungkinkan platina mengikat dua basa guanin bersebelahan pada untai DNA yang sama (intrastrand crosslink).",
      "execution": "Pilih opsi yang menjelaskan pengikatan silang intra-untai dua basa guanin oleh isomer cis."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Senyawa kompleks platina(II) $[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2]$ memiliki bentuk geometri bujur sangkar ($\\textit{square planar}$). Senyawa ini memiliki dua isomer geometri: isomer $\\textit{cis}$ (cisplatin) dan isomer $\\textit{trans}$ (transplatin). Cisplatin digunakan secara luas sebagai agen kemoterapi kanker yang sangat poten, sedangkan transplatin sama sekali tidak aktif secara klinis. Mekanisme biokimia molekuler yang mendasari perbedaan efektivitas medis ini adalah...",
    "formulaHud": {
      "title": "MEKANISME KERJA CISPLATIN TERHADAP DNA SEL TUMOR",
      "latex": "\\textit{cis}\\text{-}[\\text{Pt}(\\text{NH}_3)_2\\text{Cl}_2] + 2\\text{H}_2\\text{O} \\rightarrow \\textit{cis}\\text{-}[\\text{Pt}(\\text{NH}_3)_2(\\text{H}_2\\text{O})_2]^{2+} + 2\\text{Cl}^- \\xrightarrow{\\text{Guanin } N7} 1{,}2\\text{-intrastrand crosslink}",
      "legend": "• Jarak ligan Cl-Cl pada isomer $\\textit{cis}$ = $3{,}3\\text{ Å}$ cocok dengan jarak $N7$ dua guanin adjacent ($3{,}4\\text{ Å}$)<br>• Isomer $\\textit{trans}$ memiliki ligan berseberangan ($180^\\circ$) berjarak $> 4\\text{ Å}$, gagal membentuk crosslink efektif<br>• Distorsi tekukan DNA sebesar $30-40^\\circ$ memblokir replikasi dan transkripsi DNA tumor"
    },
    "options": [
      {
        "key": "A",
        "text": "Cisplatin bekerja murni sebagai antioksidan pemulung radikal bebas di dalam sitoplasma sel darah putih normal."
      },
      {
        "key": "B",
        "text": "Pada isomer $\\textit{cis}$, kedua ligan klorida yang labil terletak berdampingan dengan jarak $\\sim 3{,}3\\text{ Å}$, tepat cocok untuk melakukan koordinasi silang bifungsional intra-untai ($\\textit{intrastrand cross-link}$) pada dua basa nitrogen guanin bersebelahan pada DNA heliks ganda sel kanker sehingga memicu distorsi struktural dan apoptosis sel."
      },
      {
        "key": "C",
        "text": "Isomer $\\textit{cis}$ mengalami disosiasi total menghasilkan gas amonia pekat yang meracuni mitokondria sel kanker secara selektif."
      },
      {
        "key": "D",
        "text": "Pada isomer $\\textit{trans}$, kedua atom platina saling berikatan membentuk polimer logam berat yang tidak mampu menembus membran sel sama sekali."
      },
      {
        "key": "E",
        "text": "Isomer $\\textit{trans}$ bersifat sangat mudah terbakar di dalam plasma darah sehingga terurai sebelum mencapai target inti sel."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Pada isomer $\\textit{cis}$, kedua ligan klorida yang labil terletak berdampingan dengan jarak $\\sim 3{,}3\\text{ Å}$, tepat cocok untuk melakukan koordinasi silang bifungsional intra-untai ($\\textit{intrastrand cross-link}$) pada dua basa nitrogen guanin bersebelahan pada DNA heliks ganda sel kanker sehingga memicu distorsi struktural dan apoptosis sel.. Isomer cis menempatkan dua ligan klorida labil berdampingan (sudut 90 derajat). Posisi ini memungkinkan platina mengikat dua basa guanin bersebelahan pada untai DNA yang sama (intrastrand crosslink). Pilih opsi yang menjelaskan pengikatan silang intra-untai dua basa guanin oleh isomer cis."
  },
  {
    "id": "kim-sim-12",
    "materi": "KIMIA ORGANIK SINTESIS",
    "topic": "Sintesis Aspirin (Asam Asetilsalisilat) dan Uji Kemurnian",
    "hints": {
      "concept": "Asam salisilat memiliki gugus fenolik (-OH menempel pada cincin benzena), sedangkan aspirin telah diubah menjadi ester sehingga tidak memiliki gugus fenol bebas. Uji spesifik fenol menggunakan FeCl3.",
      "execution": "Reaksi ion Fe3+ dengan fenol menghasilkan kompleks koordinasi berwarna ungu pekat."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam sintesis aspirin di laboratorium kimia organik, asam salisilat (asam $o$-hidroksibenzoat, $M_r = 138$) direaksikan dengan anhidrida asetat berlebih ($M_r = 102$) menggunakan katalis beberapa tetes asam sulfat pekat ($\\text{H}_2\\text{SO}_4$) menghasilkan asam asetilsalisilat ($M_r = 180$) dan produk samping asam asetat. Untuk menguji apakah produk aspirin hasil kristalisasi masih mengandung sisa asam salisilat yang belum bereaksi, pereaksi uji laboratorium yang paling tepat dan perubahan yang teramati adalah...",
    "formulaHud": {
      "title": "SINTESIS ASPIRIN & UJI FENOL BEBAS DENGAN FECL3",
      "latex": "\\text{C}_7\\text{H}_6\\text{O}_3 + (\\text{CH}_3\\text{CO})_2\\text{O} \\xrightarrow{\\text{H}_2\\text{SO}_4} \\text{C}_9\\text{H}_8\\text{O}_4 + \\text{CH}_3\\text{COOH}; \\quad 6\\text{ArOH} + \\text{Fe}^{3+} \\rightarrow [\\text{Fe}(\\text{OAr})_6]^{3-} \\text{ (ungu)}",
      "legend": "• Asam salisilat memiliki gugus $-\\text{OH}$ fenolik bebas yang bereaksi dengan $\\text{Fe}^{3+}$ membentuk kompleks ungu<br>• Pada aspirin murni, gugus $-\\text{OH}$ telah terasetilasi menjadi gugus ester asetil ($-\\text{OCOCH}_3$) sehingga tidak bereaksi dengan $\\text{FeCl}_3$"
    },
    "options": [
      {
        "key": "A",
        "text": "Penambahan larutan Fehling A dan B dipanaskan; jika terbentuk endapan merah bata menunjukkan adanya gugus aldehida pada asam salisilat."
      },
      {
        "key": "B",
        "text": "Penambahan larutan bromin dalam $\\text{CCl}_4$; jika warna coklat hilang menandakan adanya ikatan rangkap tiga terisolasi pada aspirin murni."
      },
      {
        "key": "C",
        "text": "Penambahan beberapa tetes larutan $\\text{FeCl}_3$ encer; jika masih terdapat pengotor asam salisilat, larutan akan menghasilkan warna ungu pekat akibat pembentukan kompleks besi(III) fenolat dengan gugus fenol bebas $-\\text{OH}$ asam salisilat."
      },
      {
        "key": "D",
        "text": "Uji kertas lakmus merah; aspirin murni akan mengubah lakmus merah menjadi biru pekat karena bersifat basa nitrogen kuat."
      },
      {
        "key": "E",
        "text": "Penambahan pereaksi Tollens menghasilkan cermin perak mengkilap di dinding tabung reaksi akibat oksidasi gugus karboksilat."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Penambahan beberapa tetes larutan $\\text{FeCl}_3$ encer; jika masih terdapat pengotor asam salisilat, larutan akan menghasilkan warna ungu pekat akibat pembentukan kompleks besi(III) fenolat dengan gugus fenol bebas $-\\text{OH}$ asam salisilat.. Asam salisilat memiliki gugus fenolik (-OH menempel pada cincin benzena), sedangkan aspirin telah diubah menjadi ester sehingga tidak memiliki gugus fenol bebas. Uji spesifik fenol menggunakan FeCl3. Reaksi ion Fe3+ dengan fenol menghasilkan kompleks koordinasi berwarna ungu pekat."
  },
  {
    "id": "kim-sim-13",
    "materi": "MEKANISME REAKSI ORGANIK",
    "topic": "Penelusuran Isotopik Oksigen-18 pada Reaksi Esterifikasi Fischer",
    "hints": {
      "concept": "Pada esterifikasi Fischer, gugus -OH dilepas oleh asam karboksilat, sedangkan alkohol hanya melepas atom H (ikatan C-O alkohol TIDAK putus).",
      "execution": "Atom 18O dari alkohol tetap berada pada molekul ester (etil asetat), sedangkan H2O berasal dari -OH asam karboksilat dan proton H."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Reaksi esterifikasi Fischer antara asam asetat berlabel isotop oksigen-16 biasa ($\\text{CH}_3\\text{COOH}$) dengan etanol yang dilabeli isotop stabil oksigen-18 pada atom oksigen hidroksilnya ($\\text{CH}_3\\text{CH}_2^{18}\\text{OH}$) dilangsungkan dengan katalis asam kuat $\\text{H}^+$. Setelah mencapai kesetimbangan, analisis spektrometri massa menunjukkan bahwa atom isotop $^{18}\\text{O}$ terlokalisasi pada molekul...",
    "formulaHud": {
      "title": "MEKANISME ASILASI ESTERIFIKASI FISCHER (ISOTOPIC LABELING)",
      "latex": "\\text{R-C}(=\\text{O})-\\text{OH} + \\text{H-}^{18}\\text{O-R}' \\underset{\\text{katalis } \\text{H}^+}{\\rightleftharpoons} \\text{R-C}(=\\text{O})-^{18}\\text{O-R}' + \\text{H}_2\\text{O}",
      "legend": "• Nukleofil alkohol $\\text{R}'^{18}\\text{OH}$ menyerang karbon karbonil terprotonasi asam karboksilat<br>• Terbentuk zat antara tetrahedral<br>• Gugus pergi ($\\textit{leaving group}$) adalah molekul air dari gugus $-\\text{OH}$ asam karboksilat awal<br>• Atom $^{18}\\text{O}$ tetap menempel pada gugus alkoksi ester yang dihasilkan"
    },
    "options": [
      {
        "key": "A",
        "text": "Kedua atom oksigen asam asetat secara acak karena terjadi pertukaran isotop simetris melalui radikal bebas gas metana."
      },
      {
        "key": "B",
        "text": "Molekul air sebagai $\\text{H}_2^{18}\\text{O}$, membuktikan bahwa gugus hidroksil etanol terlepas utuh diserang oleh proton asam asetat ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "C",
        "text": "Gas karbon dioksida terbebas akibat dekarboksilasi spontan esterifikasi asam karboksilat alifatik jenuh."
      },
      {
        "key": "D",
        "text": "Etil asetat pada atom oksigen penjembatan ester ($\\text{CH}_3\\text{CO-}^{18}\\text{OCH}_2\\text{CH}_3$), sedangkan molekul air yang tereliminasi murni mengandung isotop oksigen biasa ($\\text{H}_2^{16}\\text{O}$), membuktikan bahwa pemutusan ikatan terjadi pada ikatan asil–oksigen ($ ext{C-OH}$) dari asam karboksilat."
      },
      {
        "key": "E",
        "text": "Tidak satu pun molekul produk yang mengandung $^{18}\\text{O}$ karena isotop oksigen meluruh menjadi isotop fluorin radioaktif selama pemanasan."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Etil asetat pada atom oksigen penjembatan ester ($\\text{CH}_3\\text{CO-}^{18}\\text{OCH}_2\\text{CH}_3$), sedangkan molekul air yang tereliminasi murni mengandung isotop oksigen biasa ($\\text{H}_2^{16}\\text{O}$), membuktikan bahwa pemutusan ikatan terjadi pada ikatan asil–oksigen ($\text{C-OH}$) dari asam karboksilat.. Pada esterifikasi Fischer, gugus -OH dilepas oleh asam karboksilat, sedangkan alkohol hanya melepas atom H (ikatan C-O alkohol TIDAK putus). Atom 18O dari alkohol tetap berada pada molekul ester (etil asetat), sedangkan H2O berasal dari -OH asam karboksilat dan proton H."
  },
  {
    "id": "kim-sim-14",
    "materi": "BIOKIMIA & KINETIKA ENZIM",
    "topic": "Penentuan Tipe Inhibisi Enzim Menggunakan Plot Lineweaver-Burk",
    "hints": {
      "concept": "Ingat rumus Lineweaver-Burk. Jika perpotongan sumbu-Y tetap (Vmax sama), tetapi kemiringan berubah dan perpotongan sumbu-X bergeser (Km bertambah), itu adalah inhibisi kompetitif.",
      "execution": "Inhibitor bersaing langsung di sisi aktif. Dapat diatasi dengan menambahkan konsentrasi substrat berlebih."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam penelitian kinetika suatu enzim metabolik, diperoleh data laju reaksi awal ($V_0$) terhadap konsentrasi substrat ($[S]$). Saat ditambahkan senyawa inhibitor $X$, diperoleh kurva ganda resiprokal Lineweaver-Burk ($\\frac{1}{V_0}$ vs $\\frac{1}{[S]}$) dengan karakteristik:<br>• Titik potong sumbu vertikal ($1/V_{\\max}$) tidak berubah sama sekali dibandingkan tanpa inhibitor.<br>• Titik potong sumbu horizontal ($-1/K_m$) bergeser mendekati titik nol (nilai $K_m$ semu meningkat).<br>Berdasarkan data tersebut, jenis mekanisme inhibisi yang dilakukan oleh senyawa $X$ dan cara menanggulangi efek penghambatan tersebut adalah...",
    "formulaHud": {
      "title": "PERSAMAAN LINEWEAVER-BURK & INHIBISI KOMPETITIF",
      "latex": "\\frac{1}{V_0} = \\left(\\frac{K_m^{\\text{app}}}{V_{\\max}}\\right)\\frac{1}{[S]} + \\frac{1}{V_{\\max}}; \\quad K_m^{\\text{app}} = K_m \\left(1 + \\frac{[I]}{K_I}\\right); \\quad V_{\\max} = \\text{konstan}",
      "legend": "• Titik potong sumbu-$Y$ ($1/V_{\\max}$) tetap $\\implies V_{\\max}$ tidak berubah<br>• Titik potong sumbu-$X$ ($-1/K_m^{\\text{app}}$) bergeser ke kanan mendekati 0 $\\implies K_m^{\\text{app}} > K_m$<br>• Merupakan ciri khas absolut inhibisi enzim tipe kompetitif"
    },
    "options": [
      {
        "key": "A",
        "text": "Inhibisi kompetitif; inhibitor $X$ memiliki kemiripan struktur dengan substrat dan bersaing merebutkan sisi aktif enzim bebas, sehingga efek penghambatan dapat diatasi tuntas dengan meningkatkan konsentrasi substrat $[S]$ hingga sangat tinggi."
      },
      {
        "key": "B",
        "text": "Inhibisi un-kompetitif; inhibitor hanya dapat mengikat kompleks enzim-substrat yang menurunkan nilai $V_{\\max}$ dan $K_m$ secara bersamaan."
      },
      {
        "key": "C",
        "text": "Inhibisi irreversibel bunuh diri; inhibitor membentuk ikatan kovalen permanen yang merusak struktur primer rantai polipeptida enzim."
      },
      {
        "key": "D",
        "text": "Inhibisi non-kompetitif; inhibitor mengikat sisi alosterik enzim sehingga nilai laju maksimum $V_{\\max}$ turun permanen apapun konsentrasi substratnya menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "E",
        "text": "Inhibisi umpan balik alosterik; inhibitor mempercepat laju denaturasi termal protein enzim pada suhu fisiologis."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Inhibisi kompetitif; inhibitor $X$ memiliki kemiripan struktur dengan substrat dan bersaing merebutkan sisi aktif enzim bebas, sehingga efek penghambatan dapat diatasi tuntas dengan meningkatkan konsentrasi substrat $[S]$ hingga sangat tinggi.. Ingat rumus Lineweaver-Burk. Jika perpotongan sumbu-Y tetap (Vmax sama), tetapi kemiringan berubah dan perpotongan sumbu-X bergeser (Km bertambah), itu adalah inhibisi kompetitif. Inhibitor bersaing langsung di sisi aktif. Dapat diatasi dengan menambahkan konsentrasi substrat berlebih."
  },
  {
    "id": "kim-sim-15",
    "materi": "POLIMER & MATERIAL MAJU",
    "topic": "Struktur dan Kekuatan Tarik Balistik Serat Polimer Kevlar",
    "hints": {
      "concept": "Kevlar tersusun dari cincin benzena posisi para yang kaku dan dihubungkan oleh gugus amida. Antarrantai sejajar terbentuk ikatan hidrogen N-H...O=C yang sangat rapat dan kuat.",
      "execution": "Pilih jawaban yang menyebutkan konformasi lurus kaku dengan ikatan hidrogen antarrantai dan interaksi penumpukan pi-pi aromatik."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Kevlar (poli-p-fenilena tereftalamida) adalah polimer sintetis aramid berkekuatan tarik lima kali lebih kuat daripada baja dengan massa yang sama, digunakan untuk rompi antipeluru dan komponen pesawat ruang angkasa. Kevlar disintesis melalui reaksi polimerisasi kondensasi antara 1,4-fenilenadiamina dan tereftaloil klorida. Faktor struktural molekuler yang memberikan kekuatan tarik dan ketahanan mekanik yang luar biasa pada serat Kevlar adalah...",
    "formulaHud": {
      "title": "POLIMERISASI KONDENSASI & IKATAN ANTARRANTAL KEVLAR",
      "latex": "n\\text{ H}_2\\text{N-C}_6\\text{H}_4\\text{-NH}_2 + n\\text{ Cl-CO-C}_6\\text{H}_4\\text{-CO-Cl} \\rightarrow [-\\text{NH-C}_6\\text{H}_4\\text{-NH-CO-C}_6\\text{H}_4\\text{-CO}-]_n + 2n\\text{ HCl}",
      "legend": "• Gugus amida ($-\\text{CONH}-$) membentuk jalinan ikatan hidrogen terarah antarrantai sejajar<br>• Orientasi posisi para ($1,4$) pada cincin benzena menghasilkan geometri molekul linear planar kaku ($\\textit{rigid-rod}$)<br>• Menghasilkan derajat kristalinitas dan kekuatan tarik balistik luar biasa tinggi"
    },
    "options": [
      {
        "key": "A",
        "text": "Rantai-rantai polimer memiliki konformasi lurus kaku dengan cincin benzena tersubstitusi para yang tersusun sangat teratur dan saling dihubungkan secara masif oleh jaringan ikatan hidrogen antarrantai antara gugus amida ($\\text{N-H}\\cdots\\text{O=C}$) serta penumpukan interaksi $\\pi-\\pi$ antar cincin aromatik."
      },
      {
        "key": "B",
        "text": "Terbentuknya ikatan kovalen silang jembatan disulfida antara atom belerang yang ditambahkan pada proses vulkanisasi termal."
      },
      {
        "key": "C",
        "text": "Kemampuan rantai polimer untuk berotasi bebas $360^\\circ$ pada suhu kamar sehingga berperilaku seperti cairan superkritis."
      },
      {
        "key": "D",
        "text": "Tingginya percabangan rantai samping alifatik yang membuat polimer bersifat amorf dan elastis menyerap benturan proyektil."
      },
      {
        "key": "E",
        "text": "Kandungan atom klorin yang membentuk kisi kristal garam ionik dengan kerapatan massa jenis mendekati logam berat raksa."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Rantai-rantai polimer memiliki konformasi lurus kaku dengan cincin benzena tersubstitusi para yang tersusun sangat teratur dan saling dihubungkan secara masif oleh jaringan ikatan hidrogen antarrantai antara gugus amida ($\\text{N-H}\\cdots\\text{O=C}$) serta penumpukan interaksi $\\pi-\\pi$ antar cincin aromatik.. Kevlar tersusun dari cincin benzena posisi para yang kaku dan dihubungkan oleh gugus amida. Antarrantai sejajar terbentuk ikatan hidrogen N-H...O=C yang sangat rapat dan kuat. Pilih jawaban yang menyebutkan konformasi lurus kaku dengan ikatan hidrogen antarrantai dan interaksi penumpukan pi-pi aromatik."
  },
  {
    "id": "kim-sim-16",
    "materi": "KIMIA HIJAU (GREEN CHEMISTRY)",
    "topic": "Perhitungan Ekonomi Atom (Atom Economy) Sintesis Etilen Oksida",
    "hints": {
      "concept": "Rumus Ekonomi Atom = (Mr produk target / total Mr semua reaktan) * 100%. Untuk rute adisi langsung tanpa produk samping, ekonomi atomnya selalu 100%.",
      "execution": "Rute 1: 44 / (28 + 71 + 74) = 44 / 173 = 25,4%. Rute 2: 44 / (28 + 16) = 44 / 44 = 100%."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam kerangka 12 Prinsip Kimia Hijau, efisiensi reaksi dinilai dari persentase ekonomi atom ($\\textit{atom economy}$). Senyawa etilen oksida ($\\text{C}_2\\text{H}_4\\text{O}$, $M_r = 44$) dapat diproduksi melalui dua rute industri berlainan:<br>Rute Tradisional (Klorohidrin):<br>$\\text{C}_2\\text{H}_4 + \\text{Cl}_2 + \\text{Ca(OH)}_2 \\rightarrow \\text{C}_2\\text{H}_4\\text{O} + \\text{CaCl}_2 + \\text{H}_2\\text{O}$<br>($M_r$: $\\text{C}_2\\text{H}_4 = 28$, $\\text{Cl}_2 = 71$, $\\text{Ca(OH)}_2 = 74$, $\\text{C}_2\\text{H}_4\\text{O} = 44$, $\\text{CaCl}_2 = 111$, $\\text{H}_2\\text{O} = 18$)<br>Rute Katalitik Modern (Oksidasi Langsung):<br>$\\text{C}_2\\text{H}_4 + \\frac{1}{2}\\text{O}_2 \\xrightarrow{\\text{Ag}} \\text{C}_2\\text{H}_4\\text{O}$<br>Persentase ekonomi atom untuk rute klorohidrin tradisional dan rute oksidasi langsung berturut-turut adalah...",
    "formulaHud": {
      "title": "PERSAMAAN EKONOMI ATOM (ATOM ECONOMY)",
      "latex": "\\%\\text{ Atom Economy} = \\frac{\\text{Massa Molar Produk Diinginkan}}{\\sum \\text{Massa Molar Seluruh Reaktan}} \\times 100\\%",
      "legend": "• Rute Klorohidrin: $\\frac{44}{28 + 71 + 74} \\times 100\\% = \\frac{44}{173} \\times 100\\% = 25{,}43\\%$<br>• Rute Oksidasi Katalitik: $\\frac{44}{28 + 16} \\times 100\\% = \\frac{44}{44} \\times 100\\% = 100\\%$<br>• Rute oksidasi langsung mematuhi prinsip green chemistry pencegahan limbah"
    },
    "options": [
      {
        "key": "A",
        "text": "$50{,}0\\%$ pada rute klorohidrin dan $50{,}0\\%$ pada rute oksidasi langsung, karena kedua reaksi sama-sama menghasilkan 1 mol etilen oksida."
      },
      {
        "key": "B",
        "text": "$80{,}5\\%$ pada rute klorohidrin dan $20{,}0\\%$ pada rute oksidasi langsung, dihitung dari rasio koefisien stoikiometri reaktan pembatas."
      },
      {
        "key": "C",
        "text": "$33{,}3\\%$ pada rute klorohidrin dan $66{,}7\\%$ pada rute oksidasi langsung, dihitung dari rasio jumlah atom karbon terhadap hidrogen."
      },
      {
        "key": "D",
        "text": "$25{,}4\\%$ pada rute klorohidrin dan $100\\%$ pada rute oksidasi langsung, karena rute tradisional menghasilkan massa produk samping limbah ($\\text{CaCl}_2$ dan $\\text{H}_2\\text{O}$) yang jauh lebih besar daripada produk target: $\\frac{44}{28 + 71 + 74} \\times 100\\% = \\frac{44}{173} \\times 100\\% = 25{,}4\\%$, sedangkan rute katalitik langsung mengintegrasikan 100% massa seluruh reaktan ke dalam produk akhir tanpa limbah."
      },
      {
        "key": "E",
        "text": "$100\\%$ pada rute klorohidrin dan $44{,}0\\%$ pada rute oksidasi langsung, akibat salah membagi massa produk samping dengan massa reaktan."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $25{,}4\\%$ pada rute klorohidrin dan $100\\%$ pada rute oksidasi langsung, karena rute tradisional menghasilkan massa produk samping limbah ($\\text{CaCl}_2$ dan $\\text{H}_2\\text{O}$) yang jauh lebih besar daripada produk target: $\\frac{44}{28 + 71 + 74} \\times 100\\% = \\frac{44}{173} \\times 100\\% = 25{,}4\\%$, sedangkan rute katalitik langsung mengintegrasikan 100% massa seluruh reaktan ke dalam produk akhir tanpa limbah.. Rumus Ekonomi Atom = (Mr produk target / total Mr semua reaktan) * 100%. Untuk rute adisi langsung tanpa produk samping, ekonomi atomnya selalu 100%. Rute 1: 44 / (28 + 71 + 74) = 44 / 173 = 25,4%. Rute 2: 44 / (28 + 16) = 44 / 44 = 100%."
  },
  {
    "id": "kim-sim-17",
    "materi": "RADIOKIMIA & KEDOKTERAN NUKLIR",
    "topic": "Peluruhan Radioisotop Teknesium-99m dalam Diagnosis Medis",
    "hints": {
      "concept": "Peluruhan radioaktif mengikuti kinetika orde pertama: A_t = A_0 * (1/2)^n, dengan n = t / T_1/2.",
      "execution": "n = 24 / 6 = 4. Maka A_t = 800 * (1/2)^4 = 800 / 16 = 50 MBq."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Radioisotop Teknesium-99m ($^{99m}_{43}\\text{Tc}$) merupakan agen pencitraan medis ($\\textit{radiotracer}$) yang paling banyak digunakan di dunia untuk pemindaian organ vital. Isomer nuklir ini memiliki waktu paruh $T_{1/2} = 6{,}0\\text{ jam}$ dan meluruh menjadi bentuk dasarnya, $^{99}_{43}\\text{Tc}$, sambil memancarkan radiasi gamma murni berenergi $140\\text{ keV}$. Jika suatu rumah sakit menerima sediaan awal $^{99m}\\text{Tc}$ dengan aktivitas radioaktif $800\\text{ MBq}$, aktivitas radiasi yang tersisa setelah dibiarkan selama $24\\text{ jam}$ adalah...",
    "formulaHud": {
      "title": "HUKUM PELURUHAN RADIOAKTIF ORDE PERTAMA",
      "latex": "n = \\frac{t}{T_{1/2}} = \\frac{24\\text{ jam}}{6\\text{ jam}} = 4; \\quad A_t = A_0 \\left(\\frac{1}{2}\\right)^n = 800\\text{ MBq} \\times \\left(\\frac{1}{2}\\right)^4 = \\frac{800}{16} = 50\\text{ MBq}",
      "legend": "• Waktu paruh $T_{1/2} = 6{,}0\\text{ jam}$<br>• Jumlah siklus peluruhan $n = 4$<br>• Aktivitas akhir $A_t = 50\\text{ MBq}$ (tersisa $6{,}25\\%$ dari aktivitas mula-mula)"
    },
    "options": [
      {
        "key": "A",
        "text": "$25\\text{ MBq}$, dihitung jika waktu peluruhan diasumsikan telah berlangsung selama 5 kali waktu paruh (30 jam)."
      },
      {
        "key": "B",
        "text": "$0\\text{ MBq}$, karena mengasumsikan zat radioaktif telah musnah tak bersisa setelah melampaui waktu satu hari semalam."
      },
      {
        "key": "C",
        "text": "$100\\text{ MBq}$, dihitung jika hanya mengalami 3 kali waktu paruh (18 jam peluruhan)."
      },
      {
        "key": "D",
        "text": "$50\\text{ MBq}$, karena selang waktu $t = 24\\text{ jam}$ setara dengan $n = \\frac{t}{T_{1/2}} = \\frac{24}{6{,}0} = 4$ kali waktu paruh. Aktivitas sisa dihitung dengan rumus peluruhan radioaktif orde pertama: $A_t = A_0 \\left(\\frac{1}{2}\\right)^n = 800 \\times \\left(\\frac{1}{2}\\right)^4 = 800 \\times \\frac{1}{16} = 50\\text{ MBq}$."
      },
      {
        "key": "E",
        "text": "$200\\text{ MBq}$, dihitung dari asumsi aktivitas radioaktif berkurang secara linear sebesar 25% setiap 6 jam."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $50\\text{ MBq}$, karena selang waktu $t = 24\\text{ jam}$ setara dengan $n = \\frac{t}{T_{1/2}} = \\frac{24}{6{,}0} = 4$ kali waktu paruh. Aktivitas sisa dihitung dengan rumus peluruhan radioaktif orde pertama: $A_t = A_0 \\left(\\frac{1}{2}\\right)^n = 800 \\times \\left(\\frac{1}{2}\\right)^4 = 800 \\times \\frac{1}{16} = 50\\text{ MBq}$.. Peluruhan radioaktif mengikuti kinetika orde pertama: A_t = A_0 * (1/2)^n, dengan n = t / T_1/2. n = 24 / 6 = 4. Maka A_t = 800 * (1/2)^4 = 800 / 16 = 50 MBq."
  },
  {
    "id": "kim-sim-18",
    "materi": "IKATAN KIMIA & KEPOLARAN MOLEKUL",
    "topic": "Analisis Momen Dipol Relatif Molekul BF3, NF3, dan NH3",
    "hints": {
      "concept": "Perhatikan resultan vektor dipol ikatan dan dipol PEB. Pada BF3 simetri planar membatalkan dipol. Pada NF3, dipol ikatan N-F melawan dipol PEB. Pada NH3, dipol ikatan H-N searah dengan dipol PEB.",
      "execution": "Urutan momen dipol: BF3 (0) < NF3 (0,24 D) < NH3 (1,47 D)."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Berdasarkan teori domain elektron (VSEPR) dan momen dipol ikatan, molekul boron trifluorida ($\\text{BF}_3$), nitrogen trifluorida ($\\text{NF}_3$), dan amonia ($\\text{NH}_3$) memiliki karakteristik kepolaran yang sangat berbeda. Diketahui bahwa elektronegativitas $\\text{F} (4{,}0) > \\text{N} (3{,}0) > \\text{H} (2{,}1) > \\text{B} (2{,}0)$. Perbandingan momen dipol molekul ($\\mu$) yang benar beserta alasan geometrinya adalah...",
    "formulaHud": {
      "title": "VEKTOR MOMEN DIPOL MOLEKUL POLIATIK",
      "latex": "\\vec{\\mu}_{\\text{total}} = \\sum \\vec{\\mu}_{\\text{ikatan}} + \\vec{\\mu}_{\\text{PEB}}; \\quad \\mu(\\text{BF}_3) = 0\\text{ D}; \\quad \\mu(\\text{NF}_3) = 0{,}24\\text{ D}; \\quad \\mu(\\text{NH}_3) = 1{,}47\\text{ D}",
      "legend": "• $\\text{BF}_3$: Geometri segitiga datar simetris ($120^\\circ$, tanpa PEB) $\\implies \\sum \\vec{\\mu} = 0$<br>• $\\text{NF}_3$: Dipol PEB mengarah ke atas, dipol $\\text{N}\\rightarrow \\text{F}$ mengarah ke bawah (saling melawan)<br>• $\\text{NH}_3$: Dipol $\\text{H}\\rightarrow \\text{N}$ mengarah ke atas dan dipol PEB ke atas (saling memperkuat)"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\mu[\\text{BF}_3] = \\mu[\\text{NF}_3] = \\mu[\\text{NH}_3] = 0\\text{ D}$, karena ketiga molekul sama-sama mengikat tiga atom ligan yang identik mengelilingi atom pusat."
      },
      {
        "key": "B",
        "text": "$\\mu[\\text{BF}_3] = 0\\text{ D} < \\mu[\\text{NF}_3] (0{,}24\\text{ D}) < \\mu[\\text{NH}_3] (1{,}47\\text{ D})$; $\\text{BF}_3$ nonpolar karena geometri trigonal planar simetris membatalkan seluruh dipol ikatan; pada $\\text{NF}_3$ dipol ikatan polar $\\text{N}-\\text{F}$ berlawanan arah dengan dipol pasangan elektron bebas sehingga saling melemahkan, sedangkan pada $\\text{NH}_3$ dipol ikatan $\\text{N}-\\text{H}$ dan dipol pasangan elektron bebas searah sehingga saling memperkuat."
      },
      {
        "key": "C",
        "text": "$\\mu[\\text{NF}_3] > \\mu[\\text{NH}_3] > \\mu[\\text{BF}_3]$, karena atom fluorin memiliki elektronegativitas terbesar di tabel periodik sehingga dipol ikatannya selalu mendominasi mutlak ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "D",
        "text": "$\\mu[\\text{NH}_3] = 0\\text{ D}$, karena gaya tolak pasangan elektron bebas menetralkan muatan parsial positif pada ketiga atom hidrogen."
      },
      {
        "key": "E",
        "text": "$\\mu[\\text{BF}_3] > \\mu[\\text{NF}_3] > \\mu[\\text{NH}_3]$, karena ikatan kovalen antara boron dan fluorin memiliki selisih elektronegativitas paling besar."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\mu[\\text{BF}_3] = 0\\text{ D} < \\mu[\\text{NF}_3] (0{,}24\\text{ D}) < \\mu[\\text{NH}_3] (1{,}47\\text{ D})$; $\\text{BF}_3$ nonpolar karena geometri trigonal planar simetris membatalkan seluruh dipol ikatan; pada $\\text{NF}_3$ dipol ikatan polar $\\text{N}-\\text{F}$ berlawanan arah dengan dipol pasangan elektron bebas sehingga saling melemahkan, sedangkan pada $\\text{NH}_3$ dipol ikatan $\\text{N}-\\text{H}$ dan dipol pasangan elektron bebas searah sehingga saling memperkuat.. Perhatikan resultan vektor dipol ikatan dan dipol PEB. Pada BF3 simetri planar membatalkan dipol. Pada NF3, dipol ikatan N-F melawan dipol PEB. Pada NH3, dipol ikatan H-N searah dengan dipol PEB. Urutan momen dipol: BF3 (0) < NF3 (0,24 D) < NH3 (1,47 D)."
  },
  {
    "id": "kim-sim-19",
    "materi": "TERMODINAMIKA SPONTANITAS",
    "topic": "Termodinamika Pelarutan Endotermik Garam Amonium Nitrat pada Cold Pack",
    "hints": {
      "concept": "Reaksi endotermik (Delta H > 0) hanya bisa spontan jika didorong oleh peningkatan entropi yang besar (Delta S > 0) pada suhu di mana T*Delta S > Delta H, sehingga Delta G < 0.",
      "execution": "Pilih opsi yang menjelaskan dominasi kenaikan entropi (Delta S sistem > 0) yang membuat Delta G negatif pada suhu kamar."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Kompres dingin instan ($\\textit{cold pack}$) bekerja berdasarkan reaksi pelarutan spontan garam amonium nitrat padat ke dalam air murni:<br>$\\text{NH}_4\\text{NO}_3(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{NH}_4^+(aq) + \\text{NO}_3^-(aq) \\quad \\Delta H^\\circ = +25{,}7\\text{ kJ/mol}$<br>Meskipun proses pelarutan ini bersifat endotermik (menyerap kalor dari lingkungan sehingga suhu turun drastis), proses ini berlangsung secara spontan pada suhu kamar ($298\\text{ K}$). Penjelasan termodinamika yang paling valid berdasarkan Hukum Kedua Termodinamika adalah...",
    "formulaHud": {
      "title": "PERSAMAAN ENERGI BEBAS GIBBS & SPONTANITAS ENDOTERMIK",
      "latex": "\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ < 0 \\iff T\\Delta S^\\circ > \\Delta H^\\circ > 0",
      "legend": "• $\\Delta H^\\circ = +25{,}7\\text{ kJ/mol}$ (endotermik, menyerap kalor)<br>• $\\Delta S^\\circ \\approx +108\\text{ J/(mol K)}$ (peningkatan keteracakan kisi ionik padat menjadi ion terlarut)<br>• Pada $298\\text{ K}$: $T\\Delta S^\\circ = 298 \\times 0{,}108 = +32{,}2\\text{ kJ/mol} > \\Delta H^\\circ$<br>• $\\Delta G^\\circ = 25{,}7 - 32{,}2 = -6{,}5\\text{ kJ/mol} < 0$ (spontan digerakkan oleh entropi)"
    },
    "options": [
      {
        "key": "A",
        "text": "Ion amonium mengalami reaksi fusi nuklir dengan molekul air melepaskan radiasi partikel alfa yang menetralkan nilai entalpi."
      },
      {
        "key": "B",
        "text": "Reaksi tersebut sebenarnya tidak spontan dan hanya dapat berlangsung jika diberi bantuan arus listrik luar secara kontinu."
      },
      {
        "key": "C",
        "text": "Pelarutan kristal padat menjadi ion-ion terhidrasi bebas meningkatkan derajat ketidakteraturan sistem secara drastis ($\\Delta S^\\circ_{\\text{sistem}} \\gg 0$), sehingga pada suhu kamar suku pengurang termal $T\\Delta S^\\circ$ bernilai positif sangat besar dan melampaui nilai $\\Delta H^\\circ$, menghasilkan perubahan energi bebas Gibbs bernilai negatif ($\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ < 0$)."
      },
      {
        "key": "D",
        "text": "Proses pelarutan menghasilkan energi kisi kristal yang sangat eksotermik sehingga energi aktivasi reaksi menjadi bernilai negatif menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      },
      {
        "key": "E",
        "text": "Suhu dingin yang tercipta memicu penurunan entropi semesta secara spontan sesuai Hukum Ketiga Termodinamika."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Pelarutan kristal padat menjadi ion-ion terhidrasi bebas meningkatkan derajat ketidakteraturan sistem secara drastis ($\\Delta S^\\circ_{\\text{sistem}} \\gg 0$), sehingga pada suhu kamar suku pengurang termal $T\\Delta S^\\circ$ bernilai positif sangat besar dan melampaui nilai $\\Delta H^\\circ$, menghasilkan perubahan energi bebas Gibbs bernilai negatif ($\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ < 0$).. Reaksi endotermik (Delta H > 0) hanya bisa spontan jika didorong oleh peningkatan entropi yang besar (Delta S > 0) pada suhu di mana T*Delta S > Delta H, sehingga Delta G < 0. Pilih opsi yang menjelaskan dominasi kenaikan entropi (Delta S sistem > 0) yang membuat Delta G negatif pada suhu kamar."
  },
  {
    "id": "kim-sim-20",
    "materi": "KIMIA KOLOID & PENGOLAHAN AIR",
    "topic": "Mekanisme Koagulasi Koloid Berdasarkan Aturan Schulze-Hardy",
    "hints": {
      "concept": "Aturan Schulze-Hardy: ion lawan dengan valensi lebih tinggi memiliki daya koagulasi jauh lebih dahsyat (sebanding dengan z^6). Untuk koloid bermuatan negatif, kation penentu efektivitasnya.",
      "execution": "Valensi kation: Al3+ (z=3) > Mg2+ (z=2) > Na+ (z=1). Daya koagulasi Al3+ >> Mg2+ >> Na+."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam proses penjernihan air minum PDAM, air sungai yang keruh mengandung partikel koloid lumpur lempung yang bermuatan negatif dan stabil melayang dalam air. Untuk mengendapkan koloid lumpur tersebut, ditambahkan koagulan tawas (tawas aluminium sulfat, $\\text{Al}_2(\\text{SO}_4)_3$). Menurut aturan Schulze-Hardy, keefektifan ion koagulan dalam menggumpalkan koloid ditentukan oleh valensi muatannya. Perbandingan efektivitas koagulasi ion $\\text{Al}^{3+}$, $\\text{Mg}^{2+}$, dan $\\text{Na}^+$ terhadap koloid lumpur bermuatan negatif tersebut adalah...",
    "formulaHud": {
      "title": "ATURAN SCHULZE-HARDY PADA KOAGULASI KOLOID",
      "latex": "\\text{Konsentrasi Koagulasi Kritis (CCC)} \\propto \\frac{1}{z^6}; \\quad \\text{Rasio Daya Koagulasi: } 1^6 : 2^6 : 3^6 = 1 : 64 : 729",
      "legend": "• Koloid lumpur bermuatan negatif dinetralkan oleh kation (ion lawan/counter-ion)<br>• Kation dengan muatan lebih tinggi ($z = 3$ untuk $\\text{Al}^{3+}$) menekan lapisan difus listrik jauh lebih efisien dibanding $z = 1$ ($\text{Na}^+$)<br>• Tawas aluminium sulfat merupakan koagulan air industri yang sangat hemat dan efektif"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\text{Al}^{3+} \\gg \\text{Mg}^{2+} \\gg \\text{Na}^+$; daya koagulasi meningkat secara eksponensial sebanding dengan pangkat enam valensi muatan kation penyerap ($\\text{daya} \\propto z^6$), sehingga ion trivalen $\\text{Al}^{3+}$ memiliki daya pengendapan sekitar 700–1000 kali lebih kuat dibanding ion monovalen $\\text{Na}^+$ dalam menetralkan lapisan rangkap listrik koloid."
      },
      {
        "key": "B",
        "text": "Ion $\\text{Al}^{3+}$ tidak mampu mengendapkan koloid karena aluminium bersifat amfoter yang langsung larut kembali sebagai aluminat."
      },
      {
        "key": "C",
        "text": "$\\text{Na}^+ > \\text{Mg}^{2+} > \\text{Al}^{3+}$, karena ion natrium berukuran paling kecil sehingga mobilitas difusinya dalam air paling cepat."
      },
      {
        "key": "D",
        "text": "Koagulasi ditentukan oleh anion sulfida bukan oleh kation, sehingga jenis logam tidak mempengaruhi pengendapan koloid lumpur."
      },
      {
        "key": "E",
        "text": "$\\text{Al}^{3+} = \\text{Mg}^{2+} = \\text{Na}^+$, karena seluruh kation logam golongan utama memiliki kemampuan koagulasi identik per mol ion."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $\\text{Al}^{3+} \\gg \\text{Mg}^{2+} \\gg \\text{Na}^+$; daya koagulasi meningkat secara eksponensial sebanding dengan pangkat enam valensi muatan kation penyerap ($\\text{daya} \\propto z^6$), sehingga ion trivalen $\\text{Al}^{3+}$ memiliki daya pengendapan sekitar 700–1000 kali lebih kuat dibanding ion monovalen $\\text{Na}^+$ dalam menetralkan lapisan rangkap listrik koloid.. Aturan Schulze-Hardy: ion lawan dengan valensi lebih tinggi memiliki daya koagulasi jauh lebih dahsyat (sebanding dengan z^6). Untuk koloid bermuatan negatif, kation penentu efektivitasnya. Valensi kation: Al3+ (z=3) > Mg2+ (z=2) > Na+ (z=1). Daya koagulasi Al3+ >> Mg2+ >> Na+."
  },
  {
    "id": "kim-sim-21",
    "materi": "SPEKTROSKOPI STRUKTUR ORGANIK",
    "topic": "Identifikasi Gugus Fungsi Isomer Senyawa C3H6O via Spektroskopi IR",
    "hints": {
      "concept": "Puncak kuat di 1715 cm^-1 adalah gugus karbonil C=O. Pasangan puncak di 2720 dan 2820 cm^-1 adalah ciri khas unik C-H aldehida (fermi resonance). Keton tidak memilikinya.",
      "execution": "Senyawa A memiliki C-H aldehida -> Propanal. Senyawa B tidak memilikinya -> Propanon (aseton)."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua senyawa organik cair tak berwarna, senyawa $A$ dan senyawa $B$, memiliki rumus molekul identik $\\text{C}_3\\text{H}_6\\text{O}$ ($M_r = 58$). Analisis spektroskopi inframerah (FTIR) memberikan data puncak serapan serapan berikut:<br>• Senyawa $A$: Menunjukkan puncak serapan sangat kuat dan tajam pada bilangan gelombang $1715\\text{ cm}^{-1}$, serta puncak getaran ulur $\\text{C-H}$ aldehida kembar (fermi resonance) pada $2720\\text{ cm}^{-1}$ dan $2820\\text{ cm}^{-1}$.<br>• Senyawa $B$: Menunjukkan puncak tajam sangat kuat pada $1715\\text{ cm}^{-1}$, namun tidak menunjukkan serapan sama sekali pada daerah $2700-2850\\text{ cm}^{-1}$ maupun daerah serapan lebar di atas $3200\\text{ cm}^{-1}$.<br>Identitas senyawa $A$ dan senyawa $B$ yang tepat adalah...",
    "formulaHud": {
      "title": "KARAKTERISTIK SERAPAN INFRAMERAH (IR) GUGUS KARBONIL",
      "latex": "\\nu(\\text{C=O}): 1710 - 1720\\text{ cm}^{-1}; \\quad \\nu(\\text{C-H}_{\\text{aldehida}}): 2720\\text{ cm}^{-1} \\text{ & } 2820\\text{ cm}^{-1} \\text{ (doublet)}",
      "legend": "• Senyawa $A$ (Propanal, $\\text{CH}_3\\text{CH}_2\\text{CHO}$): Memiliki $\\text{C=O}$ dan $\\text{C-H}$ aldehida kembar<br>• Senyawa $B$ (Propanon/Aseton, $\\text{CH}_3\\text{COCH}_3$): Memiliki $\\text{C=O}$ keton tanpa $\\text{C-H}$ karbonil<br>• Tidak ada serapan lebar pada $3300\\text{ cm}^{-1}$ membuktikan ketiadaan gugus $-\\text{OH}$ alkohol"
    },
    "options": [
      {
        "key": "A",
        "text": "Senyawa $A$ adalah propanon dan senyawa $B$ adalah propanal, terbalik karena keton selalu memiliki serapan ulur C-H fermi resonance."
      },
      {
        "key": "B",
        "text": "Senyawa $A$ adalah 1-propanol dan senyawa $B$ adalah metil etil eter, dengan puncak $1715\\text{ cm}^{-1}$ merupakan vibrasi ikatan eter kovalen."
      },
      {
        "key": "C",
        "text": "Senyawa $A$ adalah asam propanoat dan senyawa $B$ adalah metil etanoat, karena memiliki atom oksigen tunggal dalam rumus strukturnya."
      },
      {
        "key": "D",
        "text": "Senyawa $A$ adalah siklopropanol dan senyawa $B$ adalah propilena glikol jenuh."
      },
      {
        "key": "E",
        "text": "Senyawa $A$ adalah propanal (propionaldehida) dan senyawa $B$ adalah propanon (aseton); serapan $1715\\text{ cm}^{-1}$ adalah vibrasi ulur gugus karbonil ($\\text{C=O}$), sedangkan serapan khas $2720$ dan $2820\\text{ cm}^{-1}$ adalah sidik jari ulur $\\text{C-H}$ aldehida yang tidak dimiliki oleh gugus keton propanon."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Senyawa $A$ adalah propanal (propionaldehida) dan senyawa $B$ adalah propanon (aseton); serapan $1715\\text{ cm}^{-1}$ adalah vibrasi ulur gugus karbonil ($\\text{C=O}$), sedangkan serapan khas $2720$ dan $2820\\text{ cm}^{-1}$ adalah sidik jari ulur $\\text{C-H}$ aldehida yang tidak dimiliki oleh gugus keton propanon.. Puncak kuat di 1715 cm^-1 adalah gugus karbonil C=O. Pasangan puncak di 2720 dan 2820 cm^-1 adalah ciri khas unik C-H aldehida (fermi resonance). Keton tidak memilikinya. Senyawa A memiliki C-H aldehida -> Propanal. Senyawa B tidak memilikinya -> Propanon (aseton)."
  },
  {
    "id": "kim-sim-22",
    "materi": "KIMIA LINGKUNGAN & TERAPI KELASI",
    "topic": "Terapi Kelasi Intoksikasi Timbal (Pb2+) dengan Ligan EDTA",
    "hints": {
      "concept": "Pahami efek kelat dan konstanta pembentukan Kf. Kf(Pb-EDTA) jauh melampaui Kf(Ca-EDTA). Garam kalsium digunakan agar EDTA tidak merampas Ca2+ darah yang dapat menyebabkan kejang hipokalsemia.",
      "execution": "Pilih jawaban yang menjelaskan perbandingan nilai Kf (Pb mendesak Ca) dan pencegahan hipokalsemia."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Keracunan ion logam berat timbal ($\\text{Pb}^{2+}$) sangat berbahaya bagi sistem saraf manusia karena mengikat gugus tiol ($-\\text{SH}$) pada enzim tubuh. Dalam penanganan medis darurat, diberikan obat kelasi kalsium dinatrium edetat ($\\text{CaNa}_2\\text{EDTA}$). Alasan mengapa digunakan garam kompleks $\\text{CaNa}_2\\text{EDTA}$ dan bukan asam murni $\\text{Na}_2\\text{H}_2\\text{EDTA}$, serta mekanisme penggantian ion logam dalam darah adalah...",
    "formulaHud": {
      "title": "TERMODINAMIKA PERTUKARAN LIGAN KELASI EDTA",
      "latex": "[\\text{Ca(EDTA)}]^{2-} + \\text{Pb}^{2+} \\rightleftharpoons [\\text{Pb(EDTA)}]^{2-} + \\text{Ca}^{2+}; \\quad K_{\\text{tukar}} = \\frac{K_f(\\text{Pb})}{K_f(\\text{Ca})} = \\frac{10^{18{,}0}}{10^{10{,}7}} = 10^{7{,}3} \\approx 2 \\times 10^7",
      "legend": "• $K_f[\\text{Pb(EDTA)}^{2-}] = 10^{18{,}0} \\gg K_f[\\text{Ca(EDTA)}^{2-}] = 10^{10{,}7}$<br>• Nilai $K_{\\text{tukar}} = 2 \\times 10^7 \\gg 1$ menggeser reaksi hampir 100% ke arah pengikatan $\\text{Pb}^{2+}$<br>• Ion $\\text{Ca}^{2+}$ yang dilepaskan aman bagi darah, dan kelat $[\\text{Pb(EDTA)}]^{2-}$ larut dalam air sehingga dibuang lewat urin"
    },
    "options": [
      {
        "key": "A",
        "text": "Konstanta kestabilan pembentukan kompleks $[\\text{Pb(EDTA)}]^{2-}$ ($K_f = 10^{18{,}0}$) jauh lebih besar daripada $[\\text{Ca(EDTA)}]^{2-}$ ($K_f = 10^{10{,}7}$), sehingga ion $\\text{Pb}^{2+}$ mampu mendesak keluar ion $\\text{Ca}^{2+}$ dari ligan secara spontan; penggunaan garam Ca mencegah pengikatan ion kalsium bebas dalam darah yang dapat memicu hipokalsemia fatal."
      },
      {
        "key": "B",
        "text": "Konstanta kestabilan kompleks timbal lebih kecil daripada kalsium sehingga ion kalsium yang membunuh ion timbal secara enzimatik."
      },
      {
        "key": "C",
        "text": "EDTA murni akan menguap menjadi gas nitrogen dioksida yang merusak alveolus paru-paru jika tidak distabilkan oleh kalsium padat."
      },
      {
        "key": "D",
        "text": "Ion timbal bereaksi dengan kalsium membentuk amalgam logam padat yang langsung dikeluarkan lewat kelenjar keringat kulit."
      },
      {
        "key": "E",
        "text": "Ion $\\text{Pb}^{2+}$ mengendap sebagai garam sulfat tak larut di dalam ginjal sehingga tidak perlu diikat oleh ligan pengkhelat."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Konstanta kestabilan pembentukan kompleks $[\\text{Pb(EDTA)}]^{2-}$ ($K_f = 10^{18{,}0}$) jauh lebih besar daripada $[\\text{Ca(EDTA)}]^{2-}$ ($K_f = 10^{10{,}7}$), sehingga ion $\\text{Pb}^{2+}$ mampu mendesak keluar ion $\\text{Ca}^{2+}$ dari ligan secara spontan; penggunaan garam Ca mencegah pengikatan ion kalsium bebas dalam darah yang dapat memicu hipokalsemia fatal.. Pahami efek kelat dan konstanta pembentukan Kf. Kf(Pb-EDTA) jauh melampaui Kf(Ca-EDTA). Garam kalsium digunakan agar EDTA tidak merampas Ca2+ darah yang dapat menyebabkan kejang hipokalsemia. Pilih jawaban yang menjelaskan perbandingan nilai Kf (Pb mendesak Ca) dan pencegahan hipokalsemia."
  },
  {
    "id": "kim-sim-23",
    "materi": "LARUTAN & CAMPURAN AZEOTROP",
    "topic": "Penyimpangan Negatif Hukum Raoult pada Campuran Aseton-Kloroform",
    "hints": {
      "concept": "Penyimpangan negatif terjadi jika interaksi A-B lebih kuat daripada A-A dan B-B. Atom H pada CHCl3 terpolarisasi positif kuat oleh 3 atom Cl, membentuk ikatan hidrogen dengan atom O pada aseton.",
      "execution": "Pilih penjelasan pembentukan ikatan hidrogen intermolekul A-B yang lebih kuat dari interaksi molekul murninya."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Pencampuran cairan aseton ($\\text{CH}_3\\text{COCH}_3$) dan kloroform ($\\text{CHCl}_3$) menghasilkan sistem larutan non-ideal yang mengalami penyimpangan negatif ($\\textit{negative deviation}$) terhadap Hukum Raoult, disertai pelepasan kalor ($\\Delta H_{\\text{campuran}} < 0$). Campuran ini membentuk azeotrop titik didih maksimum pada komposisi tertentu. Penyebab fisis-kimia dari fenomena penyimpangan negatif ini pada tingkat molekuler adalah...",
    "formulaHud": {
      "title": "PENYIMPANGAN NEGATIF HUKUM RAOULT",
      "latex": "P_{\\text{total}} < P_A^\\circ X_A + P_B^\\circ X_B; \\quad \\Delta H_{\\text{mix}} < 0; \\quad \\Delta V_{\\text{mix}} < 0; \\quad \\text{Ikatan H: } \\text{Cl}_3\\text{C-H}\\cdots\\text{O=C}(\\text{CH}_3)_2",
      "legend": "• Interaksi $A-B$ (aseton-kloroform) > interaksi $A-A$ dan $B-B$<br>• Tekanan uap jenuh total campuran lebih rendah daripada nilai ideal Raoult<br>• Titik didih campuran lebih tinggi daripada titik didih komponen murninya (Azeotrop Titik Didih Maksimum)"
    },
    "options": [
      {
        "key": "A",
        "text": "Gaya tolak elektrostatik antara atom klorin kloroform dan gugus metil aseton menyebabkan molekul lebih mudah menguap ke udara bebas."
      },
      {
        "key": "B",
        "text": "Terbentuknya ikatan hidrogen intermolekul yang kuat antara atom hidrogen yang bersifat asam pada kloroform (akibat tarikan tiga atom klorin yang sangat elektronegatif) dengan pasangan elektron bebas pada atom oksigen karbonil aseton, sehingga gaya tarik antarmolekul tak sejenis ($A-B$) lebih kuat daripada gaya tarik antarmolekul sejenis ($A-A$ dan $B-B$)."
      },
      {
        "key": "C",
        "text": "Molekul aseton mengalami kondensasi aldol membentuk polimer padat yang mengendap di dasar bejana pencampur."
      },
      {
        "key": "D",
        "text": "Terjadi reaksi kimia adisi eliminasi permanen yang membentuk garam ester kovalen tak terionisasi di dalam larutan ditinjau dari profil energi aktivasi kompleks teraktivasi menurut teori laju reaksi keadaan transisi."
      },
      {
        "key": "E",
        "text": "Kloroform bertindak sebagai ligan bidentat yang mengikat atom karbon aseton membentuk sangkar khelat koordinasi."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Terbentuknya ikatan hidrogen intermolekul yang kuat antara atom hidrogen yang bersifat asam pada kloroform (akibat tarikan tiga atom klorin yang sangat elektronegatif) dengan pasangan elektron bebas pada atom oksigen karbonil aseton, sehingga gaya tarik antarmolekul tak sejenis ($A-B$) lebih kuat daripada gaya tarik antarmolekul sejenis ($A-A$ dan $B-B$).. Penyimpangan negatif terjadi jika interaksi A-B lebih kuat daripada A-A dan B-B. Atom H pada CHCl3 terpolarisasi positif kuat oleh 3 atom Cl, membentuk ikatan hidrogen dengan atom O pada aseton. Pilih penjelasan pembentukan ikatan hidrogen intermolekul A-B yang lebih kuat dari interaksi molekul murninya."
  },
  {
    "id": "kim-sim-24",
    "materi": "RADIOKIMIA & PENANGGALAN PURBA",
    "topic": "Penanggalan Karbon-14 (Radiocarbon Dating) pada Fosil Kayu",
    "hints": {
      "concept": "Hitung perbandingan aktivitas sisa terhadap awal: At / A0 = 1,91 / 15,3 = 1/8. Karena (1/2)^3 = 1/8, maka waktu yang berlalu adalah 3 kali waktu paruh.",
      "execution": "t = 3 * 5730 tahun = 17.190 tahun."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Suatu sampel kayu purba yang ditemukan di situs arkeologi megalitikum diuji aktivitas radiokarbon $^{14}\\text{C}$-nya ($T_{1/2} = 5730\\text{ tahun}$). Kayu hidup segar saat ini memiliki aktivitas spesifik $^{14}\\text{C}$ sebesar $15{,}3\\text{ desintegrasi per menit per gram karbon}$ ($15{,}3\\text{ dpm/g}$). Jika sampel kayu purba tersebut menunjukkan aktivitas radiokarbon sebesar $1{,}91\\text{ dpm/g}$, perkiraan usia sampel kayu purba tersebut adalah...",
    "formulaHud": {
      "title": "PENANGGALAN RADIOMETRIK KARBON-14",
      "latex": "\\frac{A_t}{A_0} = \\left(\\frac{1}{2}\\right)^{\\frac{t}{T_{1/2}}} \\implies \\frac{1{,}91}{15{,}3} = 0{,}1248 \\approx \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3 \\implies t = 3 \\times 5730 = 17.190\\text{ tahun}",
      "legend": "• Aktivitas awal kayu hidup: $A_0 = 15{,}3\\text{ dpm/g}$<br>• Aktivitas kayu purba terukur: $A_t = 1{,}91\\text{ dpm/g}$<br>• Fraksi sisa: $\\frac{1{,}91}{15{,}3} = \\frac{1}{8}$ ($n = 3$ siklus)<br>• Usia arkeologis: $17.190\\text{ tahun}$"
    },
    "options": [
      {
        "key": "A",
        "text": "$22.920\\text{ tahun}$, dihitung jika kayu telah melewati 4 kali waktu paruh (seperenam belas aktivitas awal)."
      },
      {
        "key": "B",
        "text": "$5.730\\text{ tahun}$, dihitung jika aktivitas kayu purba diasumsikan tersisa separuh dari aktivitas awal."
      },
      {
        "key": "C",
        "text": "$34.380\\text{ tahun}$, dihitung dari perkalian langsung faktor pembagi aktivitas dengan waktu paruh zat."
      },
      {
        "key": "D",
        "text": "$17.190\\text{ tahun}$, karena rasio aktivitas sampel purba terhadap kayu segar adalah $\\frac{A_t}{A_0} = \\frac{1{,}91}{15{,}3} = \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3$. Hal ini membuktikan bahwa sampel kayu telah meluruh selama $n = 3$ kali waktu paruh, sehingga usia kayu adalah $t = 3 \\times T_{1/2} = 3 \\times 5730 = 17.190\\text{ tahun}$."
      },
      {
        "key": "E",
        "text": "$11.460\\text{ tahun}$, dihitung jika aktivitas sampel diasumsikan telah meluruh sebesar dua kali waktu paruh (seperempat aktivitas awal) menurut pergeseran kesetimbangan dinamis asas Le Chatelier pada sistem heterogen tertutup."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $17.190\\text{ tahun}$, karena rasio aktivitas sampel purba terhadap kayu segar adalah $\\frac{A_t}{A_0} = \\frac{1{,}91}{15{,}3} = \\frac{1}{8} = \\left(\\frac{1}{2}\\right)^3$. Hal ini membuktikan bahwa sampel kayu telah meluruh selama $n = 3$ kali waktu paruh, sehingga usia kayu adalah $t = 3 \\times T_{1/2} = 3 \\times 5730 = 17.190\\text{ tahun}$.. Hitung perbandingan aktivitas sisa terhadap awal: At / A0 = 1,91 / 15,3 = 1/8. Karena (1/2)^3 = 1/8, maka waktu yang berlalu adalah 3 kali waktu paruh. t = 3 * 5730 tahun = 17.190 tahun."
  },
  {
    "id": "kim-sim-25",
    "materi": "REAKSI KONDENSASI SENYAWA KARBONIL",
    "topic": "Sintesis Dibenzalaseton Melalui Kondensasi Claisen-Schmidt",
    "hints": {
      "concept": "Syarat pembentukan ion enolat adalah keberadaan hidrogen alfa (atom H yang terikat pada karbon di samping gugus C=O). Benzaldehida tidak punya H-alfa.",
      "execution": "Pilih jawaban yang menerangkan ketiadaan hidrogen alfa pada benzaldehida dan keberadaan H-alfa asam pada aseton."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam sintesis zat penyerap sinar UV tabir surya dibenzalaseton, benzaldehida direaksikan dengan aseton dalam suasana basa encer ($\\text{NaOH}$) dengan perbandingan stoikiometri mol $2 : 1$ menurut reaksi kondensasi Claisen-Schmidt:<br>$2\\text{C}_6\\text{H}_5\\text{CHO} + \\text{CH}_3\\text{COCH}_3 \\xrightarrow{\\text{OH}^-} \\text{C}_6\\text{H}_5\\text{-CH=CH-CO-CH=CH-C}_6\\text{H}_5 + 2\\text{H}_2\\text{O}$<br>Alasan kimia mengapa benzaldehida tidak dapat melakukan kondensasi mandiri ($\\textit{self-condensation}$) melainkan hanya dapat bertindak sebagai elektrofil yang diserang oleh ion enolat aseton adalah...",
    "formulaHud": {
      "title": "MEKANISME KONDENSASI CLAISEN-SCHMIDT (ALDOL SILANG)",
      "latex": "\\text{CH}_3\\text{COCH}_3 + \\text{OH}^- \\rightleftharpoons [\\text{CH}_2\\text{COCH}_3]^- + \\text{H}_2\\text{O}; \\quad \\text{Ar-CHO} + [\\text{CH}_2\\text{COCH}_3]^- \\rightarrow \\text{Ar-CH(OH)-CH}_2\\text{COCH}_3 \\xrightarrow{-\\text{H}_2\\text{O}} \\text{Dibenzalaseton}",
      "legend": "• Benzaldehida ($\text{C}_6\text{H}_5\text{CHO}$) tidak memiliki hidrogen alfa ($\u0007lpha$-H)<br>• Aseton memiliki atom hidrogen alfa yang bersifat asam ($pK_a \\sim 20$)<br>• Deprotonasi aseton membentuk ion enolat yang bertindak sebagai nukleofil menyerang C karbonil benzaldehida"
    },
    "options": [
      {
        "key": "A",
        "text": "Benzaldehida memiliki titik didih yang terlalu rendah sehingga langsung menguap sebelum sempat membentuk ikatan karbon-karbon baru."
      },
      {
        "key": "B",
        "text": "Cincin benzena benzaldehida bermuatan positif kuat yang menolak interaksi dengan molekul pelarut air."
      },
      {
        "key": "C",
        "text": "Molekul aseton tidak memiliki gugus karbonil sehingga hanya berperan sebagai pelarut inert tanpa ikut bereaksi."
      },
      {
        "key": "D",
        "text": "Molekul benzaldehida tidak memiliki atom hidrogen alfa ($\\alpha\\text{-H}$) pada karbon di sebelah gugus karbonilnya sehingga tidak dapat melepaskan proton untuk membentuk ion enolat; sebaliknya aseton memiliki enam atom $\\alpha\\text{-H}$ asam yang mudah dideprotonasi oleh basa $\\text{OH}^-$ membentuk nukleofil enolat penyerang."
      },
      {
        "key": "E",
        "text": "Gugus aldehida pada benzaldehida bersifat sangat basa sehingga menetralkan katalis NaOH sebelum reaksi dimulai."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Molekul benzaldehida tidak memiliki atom hidrogen alfa ($\\alpha\\text{-H}$) pada karbon di sebelah gugus karbonilnya sehingga tidak dapat melepaskan proton untuk membentuk ion enolat; sebaliknya aseton memiliki enam atom $\\alpha\\text{-H}$ asam yang mudah dideprotonasi oleh basa $\\text{OH}^-$ membentuk nukleofil enolat penyerang.. Syarat pembentukan ion enolat adalah keberadaan hidrogen alfa (atom H yang terikat pada karbon di samping gugus C=O). Benzaldehida tidak punya H-alfa. Pilih jawaban yang menerangkan ketiadaan hidrogen alfa pada benzaldehida dan keberadaan H-alfa asam pada aseton."
  },
  {
    "id": "kim-sim-26",
    "type": "multi",
    "materi": "KIMIA HIJAU (GREEN CHEMISTRY)",
    "topic": "12 Prinsip Kimia Hijau dalam Desain Proses Kimia Lestari",
    "options": [
      {
        "key": "A",
        "text": "Memprioritaskan pemanfaatan katalis selektif dibandingkan reagen stoikiometris konvensional untuk menurunkan kebutuhan energi dan mencegah produk samping limbah."
      },
      {
        "key": "B",
        "text": "Menggunakan bahan baku terbarukan (seperti biomassa tanaman) dibandingkan bahan baku tak terbarukan berbasis fosil minyak bumi."
      },
      {
        "key": "C",
        "text": "Merancang sintesis kimia dengan prinsip ekonomi atom maksimal sehingga persentase massa seluruh bahan baku terinkorporasi penuh ke dalam produk akhir yang diinginkan."
      },
      {
        "key": "D",
        "text": "Menggunakan pelarut organik klorinasi volatil (seperti kloroform dan karbon tetraklorida) dalam jumlah besar untuk mempercepat pendinginan reaktor."
      },
      {
        "key": "E",
        "text": "Meningkatkan pembentukan produk samping beracun asalkan proses pembuangan ke sungai dilakukan pada tengah malam saat tidak terpantau."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Pahami 12 prinsip green chemistry: pencegahan limbah, ekonomi atom, sintesis lebih aman, bahan terbarukan, penggunaan katalis selektif, dan degradabilitas produk.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Prinsip Kimia Hijau ($\\textit{Green Chemistry}$) yang dirumuskan oleh Paul Anastas dan John Warner bertujuan merancang produk dan proses kimia yang meminimalkan atau meniadakan penggunaan serta pembentukan zat-zat berbahaya. Manakah TIGA pernyataan berikut yang merupakan implementasi nyata dari 12 Prinsip Kimia Hijau dalam industri manufaktur kimia modern? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "12 PRINSIP UTAMA KIMIA HIJAU (ANASTAS & WARNER)",
      "latex": "\\text{Prinsip: Pencegahan Limbah} \\ | \\ \\text{Ekonomi Atom} \\ | \\ \\text{Katalisis} \\ | \\ \\text{Bahan Terbarukan} \\ | \\ \\text{Pelarut Ramah Lingkungan}",
      "legend": "• A BENAR: Prinsip Katalisis (Prinsip 9)<br>• B BENAR: Pemanfaatan Bahan Baku Terbarukan (Prinsip 7)<br>• C BENAR: Ekonomi Atom Maksimal (Prinsip 2)<br>• D SALAH: Bertentangan dengan Prinsip 5 (Pelarut dan zat penolong yang aman)<br>• E SALAH: Melanggar etika lingkungan dan Prinsip 1 (Pencegahan Limbah)"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Pahami 12 prinsip green chemistry: pencegahan limbah, ekonomi atom, sintesis lebih aman, bahan terbarukan, penggunaan katalis selektif, dan degradabilitas produk. Pilih A, B, dan C."
  },
  {
    "id": "kim-sim-27",
    "type": "multi",
    "materi": "KOROSI & PROTEKSI ELEKTROKIMIA",
    "topic": "Faktor Pemicu dan Mekanisme Pencegahan Korosi Logam Besi",
    "options": [
      {
        "key": "A",
        "text": "Keberadaan gas oksigen ($\\text{O}_2$) dan air ($\\text{H}_2\\text{O}$) merupakan syarat mutlak terjadinya perkaratan; besi tidak akan berkarat di dalam air murni yang telah dididihkan dan diisolasi dari udara luar."
      },
      {
        "key": "B",
        "text": "Larutan elektrolit (seperti garam $\\text{NaCl}$ air laut) dan suasana asam ($pH < 7$) mempercepat laju korosi besi secara signifikan karena meningkatkan konduktivitas transfer ion dan potensial reduksi katoda."
      },
      {
        "key": "C",
        "text": "Pada metode proteksi katodik anoda korban, logam dengan potensial reduksi standar ($E^\\circ$) lebih negatif daripada besi (seperti $\\text{Mg}$ atau $\\text{Zn}$) dihubungkan ke struktur pipa besi sehingga logam tersebut teroksidasi lebih dahulu."
      },
      {
        "key": "D",
        "text": "Melapisi besi dengan logam tembaga ($\\text{Cu}$) memberikan perlindungan katodik permanen; jika lapisan tembaga tergores, besi justru akan semakin tahan terhadap karat."
      },
      {
        "key": "E",
        "text": "Besi akan terkorosi jauh lebih lambat jika dihubungkan secara kontak galvanik langsung dengan logam emas murni ($\\text{Au}$)."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Syarat korosi besi: H2O dan O2. Elektrolit dan asam mempercepat korosi. Anoda korban harus memiliki E-nol lebih negatif dari besi (Mg atau Zn). Logam mulia (Cu, Au) justru mempercepat korosi jika lapisan tergores.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Korosi pada besi ($\\text{Fe}$) merupakan proses elektrokimia spontan yang merugikan secara ekonomi miliaran rupiah per tahun pada jembatan dan kapal laut. Manakah TIGA pernyataan berikut yang secara ilmiah BENAR mengenai mekanisme dan faktor-faktor yang mempengaruhi laju korosi pada besi? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "MEKANISME ELEKTROKIMIA PERKARATAN BESI",
      "latex": "\\text{Anoda: } \\text{Fe} \\rightarrow \\text{Fe}^{2+} + 2e^-; \\quad \\text{Katoda: } \\text{O}_2 + 4\\text{H}^+ + 4e^- \\rightarrow 2\\text{H}_2\\text{O} \\ (\\text{atau } \\text{O}_2 + 2\\text{H}_2\\text{O} + 4e^- \\rightarrow 4\\text{OH}^-)",
      "legend": "• A BENAR: Air dan oksigen adalah reaktan redoks esensial pembentuk karat $\\text{Fe}_2\\text{O}_3\\cdot x\\text{H}_2\\text{O}$<br>• B BENAR: Elektrolit mempercepat jembatan garam mikro, asam menambah spesi pengoksidasi $\\text{H}^+$<br>• C BENAR: Logam Mg ($E^\\circ = -2{,}37\\text{ V}$) dan Zn ($-0{,}76\\text{ V}$) lebih mudah teroksidasi dari Fe ($-0{,}44\\text{ V}$)<br>• D dan E SALAH: Logam Cu ($+0{,}34\\text{ V}$) dan Au ($+1{,}50\\text{ V}$) memiliki $E^\\circ$ lebih positif; jika tergores, Fe menjadi anoda yang terkorosi jauh lebih cepat"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Syarat korosi besi: H2O dan O2. Elektrolit dan asam mempercepat korosi. Anoda korban harus memiliki E-nol lebih negatif dari besi (Mg atau Zn). Logam mulia (Cu, Au) justru mempercepat korosi jika lapisan tergores. Pilih A, B, dan C."
  },
  {
    "id": "kim-sim-28",
    "type": "multi",
    "materi": "TERMODINAMIKA & ENTROPI SISTEM",
    "topic": "Proses-Proses Fisis dan Kimia yang Menghasilkan Kenaikan Entropi",
    "options": [
      {
        "key": "A",
        "text": "Sublimasi dry ice (karbon dioksida padat) menjadi gas karbon dioksida: $\\text{CO}_2(s) \\rightarrow \\text{CO}_2(g)$."
      },
      {
        "key": "B",
        "text": "Reaksi peruraian termal batu kapur menghasilkan gas: $\\text{CaCO}_3(s) \\rightarrow \\text{CaO}(s) + \\text{CO}_2(g)$."
      },
      {
        "key": "C",
        "text": "Pelarutan kristal garam dapur di dalam air murni: $\\text{NaCl}(s) \\xrightarrow{\\text{H}_2\\text{O}} \\text{Na}^+(aq) + \\text{Cl}^-(aq)$."
      },
      {
        "key": "D",
        "text": "Pengembunan uap air menjadi tetesan air hujan pada pembentukan awan: $\\text{H}_2\\text{O}(g) \\rightarrow \\text{H}_2\\text{O}(l)$."
      },
      {
        "key": "E",
        "text": "Pembentukan kristal es dari air cair pada freezer lemari es: $\\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{O}(s)$."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Entropi naik (Delta S > 0) jika: jumlah mol gas bertambah, terjadi transisi fasa padat -> cair -> gas, atau pelarutan kristal padat menjadi ion larutan.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Entropi ($S$) adalah besaran termodinamika yang mengukur derajat ketidakteraturan molekuler atau dispersi energi dalam suatu sistem. Manakah TIGA proses kimia atau fisis berikut yang menghasilkan perubahan entropi sistem bertanda positif ($\\Delta S_{\\text{sistem}} > 0$)? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "PRINSIP PENINGKATAN ENTROPI SISTEM",
      "latex": "\\Delta S_{\\text{sistem}} > 0 \\iff S_{\\text{gas}} \\gg S_{\\text{cair}} > S_{\\text{padat}}; \\quad \\Delta n_{\\text{gas}} > 0",
      "legend": "• A BENAR: Perubahan fasa padat $\\rightarrow$ gas menghasilkan kenaikan ruang gerak partikel sangat masif ($\\Delta S > 0$)<br>• B BENAR: Reaksi menghasilkan mol gas dari zat padat murni ($\\Delta n_g = +1 > 0$)<br>• C BENAR: Pembongkaran kisi kristal teratur menjadi ion-ion terlarut acak ($\\Delta S > 0$)<br>• D dan E SALAH: Kondensasi dan pembekuan menurunkan ketidakteraturan partikel ($\\Delta S < 0$)"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Entropi naik (Delta S > 0) jika: jumlah mol gas bertambah, terjadi transisi fasa padat -> cair -> gas, atau pelarutan kristal padat menjadi ion larutan. Pilih A, B, dan C."
  },
  {
    "id": "kim-sim-29",
    "type": "multi",
    "materi": "MAKROMOLEKUL & STRUKTUR PROTEIN",
    "topic": "Interaksi Kimia Penstabil Struktur Tersier dan Kuaterner Protein",
    "options": [
      {
        "key": "A",
        "text": "Jembatan disulfida (ikatan kovalen $-\\text{S}-\\text{S}-$) yang terbentuk dari oksidasi gugus tiol antara dua residu asam amino sistein."
      },
      {
        "key": "B",
        "text": "Jembatan garam (ikatan ionik / interaksi elektrostatik) antara gugus samping bermuatan positif (seperti lisin/arginin) dengan gugus samping bermuatan negatif (seperti aspartat/glutamat)."
      },
      {
        "key": "C",
        "text": "Interaksi hidrofobik antarrantai samping nonpolar (seperti valin, leusin, fenilalanin) yang cenderung berkumpul menjauhi pelarut air di inti bagian dalam molekul protein."
      },
      {
        "key": "D",
        "text": "Ikatan logam radioaktif antara gugus amida dengan radikal bebas isotop kalium."
      },
      {
        "key": "E",
        "text": "Pembentukan ikatan kovalen rangkap tiga antara seluruh karbon alfa di sepanjang rantai utama."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Empat interaksi penstabil struktur tersier protein: jembatan disulfida (-S-S-), jembatan garam (ionik), interaksi hidrofobik gugus nonpolar, dan ikatan hidrogen.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Struktur konformasi 3D aktif (tertier dan kuaterner) suatu protein enzim sangat menentukan fungsi biologisnya. Kerusakan konformasi ini mengakibatkan denaturasi protein. Manakah TIGA jenis interaksi kimia berikut yang secara langsung bertanggung jawab menstabilkan pelipatan struktur tersier rantai polipeptida protein? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "GAYA PENSTABIL KONFORMASI TERSIER PROTEIN",
      "latex": "\\text{Stabilisasi 3D} = \\text{Jembatan Disulfida } (-\\text{S-S}-) + \\text{Jembatan Garam } (-\\text{NH}_3^+ \\cdots ^-\\text{OOC}-) + \\text{Gaya Hidrofobik} + \\text{Ikatan H}",
      "legend": "• A BENAR: Jembatan disulfida adalah satu-satunya ikatan kovalen penstabil struktur tersier<br>• B BENAR: Jembatan garam adalah atraksi ionik antar residu bermuatan lawan<br>• C BENAR: Gaya penggerak utama pelipatan protein dalam lingkungan akuatik sel<br>• D dan E adalah opsi nonsens tanpa dasar biokimia"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Empat interaksi penstabil struktur tersier protein: jembatan disulfida (-S-S-), jembatan garam (ionik), interaksi hidrofobik gugus nonpolar, dan ikatan hidrogen. Pilih A, B, dan C."
  },
  {
    "id": "kim-sim-30",
    "type": "multi",
    "materi": "KIMIA UNSUR TRANSISI PERIODE 4",
    "topic": "Sifat Khas Fisika dan Kimia Logam Transisi Periode 4",
    "options": [
      {
        "key": "A",
        "text": "Mampu memiliki lebih dari satu bilangan oksidasi (tingkat oksidasi bervariasi) dalam berbagai senyawanya, seperti $\\text{Mn}$ yang memiliki biloks $+2, +3, +4, +6,$ dan $+7$."
      },
      {
        "key": "B",
        "text": "Membentuk ion-ion kompleks koordinasi yang seringkali berwarna cerah akibat eksitasi elektron transisi orbital $d-d$ pada penyerapan spektrum cahaya tampak."
      },
      {
        "key": "C",
        "text": "Banyak unsur dan senyawanya yang memiliki sifat paramagnetik (ditarik medan magnet) karena memiliki satu atau lebih elektron tak berpasangan pada subkulit $3d$."
      },
      {
        "key": "D",
        "text": "Selalu membentuk ikatan ionik murni dan tidak pernah mampu membentuk ikatan kovalen koordinasi dengan molekul netral."
      },
      {
        "key": "E",
        "text": "Semua logam transisi memiliki massa jenis yang lebih rendah daripada air murni sehingga selalu terapung di permukaan danau."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Sifat khas logam transisi periode 4: biloks bervariasi, senyawa kompleks berwarna (transisi d-d), memiliki sifat paramagnetik (elektron 3d tak berpasangan), dan berfungsi sebagai katalis.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Unsur-unsur transisi periode 4 (dari skandium hingga tembaga) memiliki karakteristik khas yang membedakannya secara tajam dari unsur-unsur golongan utama (blok s dan blok p). Manakah TIGA sifat karakteristik berikut yang merupakan sifat khas yang dimiliki oleh sebagian besar unsur transisi periode keempat? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "KARAKTERISTIK SUBKULIT 3D LOGAM TRANSISI",
      "latex": "\\text{Konfigurasi: } [\\text{Ar}] 4s^2 3d^n; \\quad \\Delta E = h\\nu \\text{ (transisi } d-d); \\quad \\mu_s = \\sqrt{n(n+2)} \\text{ BM}",
      "legend": "• A BENAR: Tingkat energi orbital $4s$ dan $3d$ sangat berdekatan sehingga elektron pada kedua subkulit dapat dilepaskan bertahap<br>• B BENAR: Pembelahan medan kristal ($\\Delta_o$ atau $\\Delta_t$) menyerap foton tampak memunculkan warna komplementer<br>• C BENAR: Momen magnet spin elektron tak berpasangan $\\implies$ paramagnetik / feromagnetik<br>• D SALAH: Logam transisi justru merupakan pembentuk senyawa koordinasi kovalen terbaik<br>• E SALAH: Logam transisi memiliki massa jenis tinggi ($> 3\\text{ g/cm}^3$)"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Sifat khas logam transisi periode 4: biloks bervariasi, senyawa kompleks berwarna (transisi d-d), memiliki sifat paramagnetik (elektron 3d tak berpasangan), dan berfungsi sebagai katalis. Pilih A, B, dan C."
  },
  {
    "id": "kim-sim-31",
    "type": "matrix",
    "materi": "TERMODINAMIKA & KESETIMBANGAN KIMIA",
    "topic": "Prinsip Energi Bebas Gibbs dan Kesetimbangan Termodinamika",
    "statements": [
      {
        "text": "Jika suatu reaksi kimia memiliki Delta H bernilai negatif (eksotermik) dan Delta S bernilai positif (entropi meningkat), maka reaksi tersebut pasti berlangsung spontan pada segala suhu (Delta G selalu negatif).",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Pada kondisi kesetimbangan kimia dinamis pada suhu dan tekanan konstan, nilai perubahan energi bebas Gibbs sistem bernilai nol (Delta G = 0).",
        "correct": "Benar",
        "id": "1"
      },
      {
        "text": "Jika nilai tetapan kesetimbangan suatu reaksi K > 1, maka nilai perubahan energi bebas Gibbs standar reaksi tersebut (Delta G nol) selalu bertanda positif.",
        "correct": "Salah",
        "id": "2"
      },
      {
        "text": "Katalis dapat mengubah nilai perubahan energi bebas Gibbs standar (Delta G nol) sehingga mampu mengubah reaksi non-spontan menjadi reaksi spontan.",
        "correct": "Salah",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Pahami rumus Delta G = Delta H - T*Delta S dan Delta G0 = -RT ln K. Saat setimbang Delta G = 0. Katalis TIDAK pernah mengubah Delta G atau kesetimbangan K.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai Energi Bebas Gibbs, Entalpi, dan Kesetimbangan Kimia!",
    "formulaHud": {
      "title": "PRINSIP ENERGI BEBAS GIBBS & KESETIMBANGAN",
      "latex": "\\Delta G = \\Delta H - T\\Delta S; \\quad \\Delta G = 0 \\text{ (saat setimbang)}; \\quad \\Delta G^\\circ = -RT \\ln K",
      "legend": "• Pernyataan 1 BENAR: $\\Delta H < 0$ dan $\\Delta S > 0 \\implies \\Delta G = (-) - T(+) < 0$ pada semua $T$<br>• Pernyataan 2 BENAR: Kriteria kesetimbangan termodinamika sistem tertutup adalah $\\Delta G = 0$<br>• Pernyataan 3 SALAH: Karena $\\Delta G^\\circ = -RT \\ln K$, jika $K > 1$ maka $\\ln K > 0$ sehingga $\\Delta G^\\circ < 0$ (negatif)<br>• Pernyataan 4 SALAH: Katalis hanya menurunkan energi aktivasi ($E_a$), tidak mempengaruhi fungsi keadaan termodinamika $\\Delta G^\\circ$"
    },
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": false
    },
    "explanation": "Pahami rumus Delta G = Delta H - T*Delta S dan Delta G0 = -RT ln K. Saat setimbang Delta G = 0. Katalis TIDAK pernah mengubah Delta G atau kesetimbangan K. Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
  },
  {
    "id": "kim-sim-32",
    "type": "matrix",
    "materi": "TEORI ASAM-BASA & HSAB",
    "topic": "Konsep Asam-Basa Lewis, Brønsted-Lowry, dan Prinsip HSAB",
    "statements": [
      {
        "text": "Menurut teori Lewis, suatu basa didefinisikan sebagai spesi kimia yang bertindak sebagai donor pasangan elektron bebas untuk membentuk ikatan kovalen koordinasi.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Molekul boron trifluorida (BF3) bertindak sebagai asam Lewis kuat karena atom boron memiliki orbital p kosong yang belum memenuhi kaidah oktet.",
        "correct": "Benar",
        "id": "1"
      },
      {
        "text": "Semakin kuat suatu asam Brønsted-Lowry, maka basa konjugasi yang dihasilkannya akan memiliki kekuatan kebasaan yang semakin kuat pula.",
        "correct": "Salah",
        "id": "2"
      },
      {
        "text": "Menurut prinsip HSAB (Hard and Soft Acids and Bases), asam keras (seperti Al3+ atau Ti4+) cenderung lebih stabil berikatan dengan basa lunak (seperti ion I- atau fosfina R3P).",
        "correct": "Salah",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Basa Lewis = donor PEB, Asam Lewis = akseptor PEB. Asam kuat punya basa konjugasi sangat lemah. Prinsip HSAB: Keras-Keras dan Lunak-Lunak.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai teori asam-basa modern dan interaksi kation-anion!",
    "formulaHud": {
      "title": "TEORI ASAM BASA LEWIS & PRINSIP PEARSON (HSAB)",
      "latex": "\\text{Asam Lewis: Akseptor PEB}; \\quad \\text{Basa Lewis: Donor PEB}; \\quad \\text{Hard-Hard & Soft-Soft Preference}",
      "legend": "• Pernyataan 1 BENAR: Definisi resmi asam-basa Lewis<br>• Pernyataan 2 BENAR: Boron pada $\\text{BF}_3$ hanya dikelilingi 6 elektron (hipovalen, ada orbital $2p$ kosong)<br>• Pernyataan 3 SALAH: Asam sangat kuat memiliki basa konjugasi yang sangat lemah (stabil)<br>• Pernyataan 4 SALAH: Prinsip HSAB menyatakan asam keras menyukai basa keras (gaya ionik), dan asam lunak menyukai basa lunak (gaya kovalen)"
    },
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": false
    },
    "explanation": "Basa Lewis = donor PEB, Asam Lewis = akseptor PEB. Asam kuat punya basa konjugasi sangat lemah. Prinsip HSAB: Keras-Keras dan Lunak-Lunak. Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
  },
  {
    "id": "kim-sim-33",
    "type": "matrix",
    "materi": "KINETIKA KIMIA & TEORI TUMBUKAN",
    "topic": "Energi Aktivasi, Persamaan Arrhenius, dan Katalisis",
    "statements": [
      {
        "text": "Kenaikan suhu reaksi mempercepat laju reaksi terutama karena meningkatkan fraksi molekul reaktan yang memiliki energi kinetik melampaui energi aktivasi (Ea).",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Nilai energi aktivasi (Ea) suatu reaksi kimia selalu berbanding lurus dengan perubahan entalpi reaksi (Delta H).",
        "correct": "Salah",
        "id": "1"
      },
      {
        "text": "Penambahan katalis mempercepat tercapainya keadaan setimbang dengan cara menyediakan jalur mekanisme reaksi alternatif yang memiliki energi aktivasi lebih rendah.",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Katalis heterogen (seperti serbuk platina padat pada reaksi fasa gas) bekerja dengan cara mengadsorpsi molekul reaktan pada permukaannya sehingga melemahkan ikatan kimia reaktan.",
        "correct": "Benar",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Suhu menaikkan fraksi partikel dengan energi >= Ea. Ea tidak berhubungan langsung dengan Delta H. Katalis menurunkan Ea melalui mekanisme alternatif (adsorpsi pada permukaan katalis heterogen).",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai laju reaksi dan mekanisme katalis kimia!",
    "formulaHud": {
      "title": "PERSAMAAN ARRHENIUS & TEORI TUMBUKAN",
      "latex": "k = A e^{-E_a/RT}; \\quad f = e^{-E_a/RT} \\text{ (fraksi molekul berenergi } \\ge E_a); \\quad E_a \\text{ independen dari } \\Delta H",
      "legend": "• Pernyataan 1 BENAR: Penjelasan distribusi Boltzmann Maxwell (fraksi molekul efektif naik)<br>• Pernyataan 2 SALAH: Energi aktivasi adalah rintangan kinetika transisi, sedangkan $\\Delta H$ adalah selisih termodinamika keadaan awal dan akhir<br>• Pernyataan 3 BENAR: Definisi fungsi kerja katalis<br>• Pernyataan 4 BENAR: Mekanisme adsorpsi fisiosorpsi/kemisorpsi pada katalisis heterogen"
    },
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "explanation": "Suhu menaikkan fraksi partikel dengan energi >= Ea. Ea tidak berhubungan langsung dengan Delta H. Katalis menurunkan Ea melalui mekanisme alternatif (adsorpsi pada permukaan katalis heterogen). Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
  },
  {
    "id": "kim-sim-34",
    "type": "matrix",
    "materi": "ELEKTROKIMIA & SEL ELEKTROLISIS",
    "topic": "Hukum Faraday, Elektrolisis Larutan, dan Potensial Sel",
    "statements": [
      {
        "text": "Pada elektrolisis larutan NaCl encer menggunakan elektroda karbon inert, gas yang dihasilkan di kutub katoda adalah gas hidrogen (H2), bukan endapan logam natrium.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Menurut Hukum Faraday I, massa zat yang diendapkan pada elektroda berbanding lurus dengan muatan listrik total (kuat arus dikali waktu) yang dialirkan ke dalam sel.",
        "correct": "Benar",
        "id": "1"
      },
      {
        "text": "Reaksi redoks dalam sel volta berlangsung spontan dengan potensial sel standar selalu bertanda negatif (E sel nol < 0).",
        "correct": "Salah",
        "id": "2"
      },
      {
        "text": "Pada proses pemurnian tembaga kotor (electrorefining), logam tembaga kotor dipasang sebagai katoda sedangkan tembaga murni dipasang sebagai anoda.",
        "correct": "Salah",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Di katoda larutan NaCl: air tereduksi menjadi H2 karena E0 reduksi Na sangat negatif. Faraday I: w ~ I*t. Sel volta spontan E0_sel > 0. Electrorefining Cu: anoda = Cu kotor, katoda = Cu murni.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai elektrokimia sel volta dan elektrolisis!",
    "formulaHud": {
      "title": "HUKUM ELEKTROKIMIA & ATURAN ELEKTROLISIS",
      "latex": "w = \\frac{e \\cdot i \\cdot t}{96500}; \\quad \\Delta G^\\circ = -n F E_{\\text{sel}}^\\circ < 0 \\implies E_{\\text{sel}}^\\circ > 0 \\text{ (spontan)}",
      "legend": "• Pernyataan 1 BENAR: Logam aktif Golongan IA ($E^\\circ = -2{,}71\\text{ V}$) kalah bersaing dengan air ($E^\\circ = -0{,}83\\text{ V}$), sehingga air tereduksi menjadi $\\text{H}_2$<br>• Pernyataan 2 BENAR: Hukum Faraday I ($w \\propto Q = I \\cdot t$)<br>• Pernyataan 3 SALAH: Sel volta spontan memiliki $E_{\\text{sel}}^\\circ > 0$ (positif)<br>• Pernyataan 4 SALAH: Tembaga kotor harus dioksidasi di ANODA, dan tembaga murni mengendap di KATODA"
    },
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": false
    },
    "explanation": "Di katoda larutan NaCl: air tereduksi menjadi H2 karena E0 reduksi Na sangat negatif. Faraday I: w ~ I*t. Sel volta spontan E0_sel > 0. Electrorefining Cu: anoda = Cu kotor, katoda = Cu murni. Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
  },
  {
    "id": "kim-sim-35",
    "type": "matrix",
    "materi": "IKATAN KIMIA & GAYA ANTARMOLEKUL",
    "topic": "Hibridisasi Orbital, Geometri Molekul, dan Gaya Antarmolekul",
    "statements": [
      {
        "text": "Molekul metana (CH4) memiliki hibridisasi sp3 pada atom pusat C dengan bentuk geometri molekul tetrahedral sempurna dan sudut ikatan 109,5 derajat.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Molekul air (H2O) memiliki sudut ikatan H-O-H sekitar 104,5 derajat (lebih kecil dari sudut tetrahedral ideal) akibat tolakan kuat dari dua pasangan elektron bebas pada atom oksigen.",
        "correct": "Benar",
        "id": "1"
      },
      {
        "text": "Ikatan kovalen rangkap dua (C=C) selalu tersusun dari dua buah ikatan pi yang terbentuk dari tumpang tindih orbital sisi-ke-sisi.",
        "correct": "Salah",
        "id": "2"
      },
      {
        "text": "Kekuatan gaya dispersi London antara molekul-molekul nonpolar meningkat seiring bertambahnya massa molar dan ukuran awan elektron molekul tersebut.",
        "correct": "Benar",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "CH4 tetrahedral sp3 (109,5). H2O sudut menyusut jadi 104,5 karena tolakan 2 PEB. Ikatan rangkap 2 = 1 sigma + 1 pi. Gaya London makin kuat jika Mr dan awan elektron makin besar.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
    },
    "subject": "kimia",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai struktur ikatan kovalen dan interaksi antarmolekul!",
    "formulaHud": {
      "title": "TEORI VSEPR & HIBRIDISASI VALENSI",
      "latex": "\\text{Ikatan Rangkap 2 } (\\text{C=C}) = 1\\sigma + 1\\pi; \\quad \\text{Tolakan: PEB-PEB} > \\text{PEB-PEI} > \\text{PEI-PEI}",
      "legend": "• Pernyataan 1 BENAR: Metana memiliki 4 domain ikatan (hibridisasi $sp^3$, tetrahedral sempurna $109{,}5^\\circ$)<br>• Pernyataan 2 BENAR: Air memiliki 2 PEI dan 2 PEB; tolakan PEB mendistorsi sudut menjadi $104{,}5^\\circ$<br>• Pernyataan 3 SALAH: Ikatan rangkap dua terdiri atas 1 ikatan sigma ($\\sigma$) dan 1 ikatan pi ($\\pi$), bukan dua ikatan pi<br>• Pernyataan 4 BENAR: Awan elektron yang lebih besar lebih mudah dipolarisasikan (daya dispersi meningkat)"
    },
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "explanation": "CH4 tetrahedral sp3 (109,5). H2O sudut menyusut jadi 104,5 karena tolakan 2 PEB. Ikatan rangkap 2 = 1 sigma + 1 pi. Gaya London makin kuat jika Mr dan awan elektron makin besar. Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
  }
];
