# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Fisika (SMA/MA Saintek)
Dataset: Hard Practice (25 Authentic Questions, fis-lat-h-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

FISIKA_HARD_ITEMS = [
    {
        "id": "fis-lat-h-01",
        "materi": "DINAMIKA ROTASI & MENGGELINDING MURNI",
        "topic": "Gerak Menggelinding Murni Silinder Pejal pada Bidang Miring",
        "stem": "Sebuah silinder pejal homogen bermassa $M = 4\\text{ kg}$ dan jari-jari $R = 20\\text{ cm}$ dilepaskan dari puncak bidang miring kasar dengan sudut kemiringan $\\theta = 30^\\circ$ ($\\sin 30^\\circ = 0{,}5$). Silinder menggelinding murni tanpa slip menuruni bidang miring. Momen inersia silinder pejal terhadap sumbu simetrinya adalah $I = \\frac{1}{2} M R^2$, dan percepatan gravitasi bumi $g = 10\\text{ m/s}^2$. Percepatan linier pusat massa silinder ($a$) dan gaya gesek statis ($f_s$) yang bekerja pada titik kontak adalah...",
        "correct": "$a = \\frac{10}{3}\\text{ m/s}^2$ dan $f_s = \\frac{20}{3}\\text{ N}$, dihitung dari persamaan translasi $M g \\sin\\theta - f_s = M a$ dan rotasi $f_s R = I \\alpha = \\frac{1}{2} M R^2 \\left(\\frac{a}{R}\\right)$, sehingga $a = \\frac{g \\sin\\theta}{1 + k} = \\frac{10 \\times 0{,}5}{1 + 0{,}5} = \\frac{5}{1{,}5} = \\frac{10}{3}\\text{ m/s}^2$, serta $f_s = \\frac{1}{2} M a = \\frac{1}{2}(4)\\left(\\frac{10}{3}\\right) = \\frac{20}{3}\\text{ N}$.",
        "distractors": [
            "$a = 5\\text{ m/s}^2$ dan $f_s = 0\\text{ N}$, karena silinder dianggap meluncur bebas di atas bidang miring licin sempurna tanpa torsi gesek.",
            "$a = 2{,}5\\text{ m/s}^2$ dan $f_s = 10\\text{ N}$, dihitung dengan menggunakan konstanta momen inersia bola pejal dua per lima.",
            "$a = \\frac{20}{3}\\text{ m/s}^2$ dan $f_s = \\frac{40}{3}\\text{ N}$, karena percepatan gravitasi tidak dikalikan dengan sinus sudut kemiringan bidang miring.",
            "$a = 3\\text{ m/s}^2$ dan $f_s = 8\\text{ N}$, dihitung dari pendekatan pembulatan kasar koefisien gesekan kinetik permukaan bidang luncur."
        ],
        "formula": {
            "title": "FORMULA PERCEPATAN MENGGELINDING MURNI",
            "latex": "a = \\frac{g \\sin\\theta}{1 + k}; \\quad f_s = \\frac{k}{1 + k} M g \\sin\\theta",
            "legend": "• $k$ = Faktor bentuk inersia silinder pejal ($k = \\frac{1}{2}$)<br>• $a = \\frac{10 \\times 0{,}5}{1 + 0{,}5} = \\frac{5}{1{,}5} = \\frac{10}{3}\\text{ m/s}^2$<br>• $f_s = \\frac{1}{2} M a = 2 \\times \\frac{10}{3} = \\frac{20}{3}\\text{ N}$"
        },
        "hints": {
            "concept": "Gunakan Hukum II Newton translasi: Mg sin(theta) - fs = M*a, dan rotasi: fs * R = I * (a/R). Untuk silinder pejal k = 1/2, a = g sin(theta) / (1 + k).",
            "execution": "a = (10 * 0,5) / (1 + 0,5) = 10/3 m/s^2. fs = 1/2 * 4 * (10/3) = 20/3 N."
        }
    },
    {
        "id": "fis-lat-h-02",
        "materi": "KESETIMBANGAN BENDA TEGAR",
        "topic": "Tangga Bersandar pada Dinding Licin dan Lantai Kasar",
        "stem": "Sebuah tangga homogen dengan panjang $L$ dan berat $W$ disandarkan pada dinding vertikal yang licin sempurna dan bertumpu pada lantai horizontal yang kasar. Sudut kemiringan tangga terhadap lantai horizontal adalah $\\theta$. Agar tangga tetap berada dalam keadaan setimbang tepat saat akan tergelincir, nilai koefisien gesekan statis minimum ($\\mu_s$) antara ujung bawah tangga dan lantai horizontal harus bernilai...",
        "correct": "$\\mu_s = \\frac{1}{2 \\tan\\theta}$ (atau $\\frac{1}{2} \\cot\\theta$), diperoleh dari syarat kesetimbangan gaya horizontal $N_{\\text{dinding}} = f_s = \\mu_s N_{\\text{lantai}}$, gaya vertikal $N_{\\text{lantai}} = W$, dan torsi terhadap dasar tangga $\\sum \\tau = 0 \\implies N_{\\text{dinding}} (L \\sin\\theta) - W \\left(\\frac{L}{2} \\cos\\theta\\right) = 0$, sehingga $N_{\\text{dinding}} = \\frac{W \\cos\\theta}{2 \\sin\\theta} = \\frac{W}{2 \\tan\\theta}$.",
        "distractors": [
            "$\\mu_s = \\frac{1}{\\tan\\theta}$, karena titik berat tangga keliru ditempatkan di puncak tertinggi tangga yang bersentuhan dengan dinding vertikal.",
            "$\\mu_s = \\frac{1}{2} \\tan\\theta$, karena fungsi sinus dan cosinus pada lengan momen torsi tertukar letaknya saat proyeksi sudut kemiringan.",
            "$\\mu_s = \\frac{2}{\\sin\\theta}$, karena gaya normal dinding diasumsikan sama persis dengan dua kali lipat gaya berat tangga homogen.",
            "$\\mu_s = \\frac{1}{2 \\cos\\theta}$, dihitung dari perbandingan gaya normal lantai terhadap komponen tangensial panjang batang penyangga."
        ],
        "formula": {
            "title": "KESETIMBANGAN ROTASI & TRANSLASI TANGGA",
            "latex": "\\sum F_x = 0 \\implies f_s = N_D; \\quad \\sum F_y = 0 \\implies N_L = W; \\quad \\sum \\tau_L = 0 \\implies N_D (L \\sin\\theta) = W \\left(\\frac{L}{2} \\cos\\theta\\right)",
            "legend": "• $N_D = \\frac{W \\cos\\theta}{2 \\sin\\theta} = \\frac{W}{2 \\tan\\theta}$<br>• Tepat akan tergelincir: $f_s = \\mu_s N_L = \\mu_s W$<br>• $\\mu_s W = \\frac{W}{2 \\tan\\theta} \\implies \\mu_s = \\frac{1}{2 \\tan\\theta}$"
        },
        "hints": {
            "concept": "Torsi terhadap tumpuan lantai = 0: ND * L sin(theta) - W * (L/2) cos(theta) = 0. ND = W / (2 tan theta). Kesetimbangan translasi: fs = ND dan NL = W.",
            "execution": "mu_s = fs / NL = ND / W = 1 / (2 tan theta)."
        }
    },
    {
        "id": "fis-lat-h-03",
        "materi": "GETARAN HARMONIK SEDERHANA",
        "topic": "Sistem Pegas Gabungan Seri-Paralel dengan Beban Gandeng",
        "stem": "Dua buah pegas identik masing-masing memiliki konstanta pegas $k = 400\\text{ N/m}$. Mula-mula kedua pegas disusun secara paralel, kemudian ujung gabungan pegas tersebut digantungi beban bermassa $m = 2\\text{ kg}$. Jika sistem tersebut disimpangkan sedikit lalu berosilasi harmonik sederhana vertikal, frekuensi sudut osilasi ($\\omega$) dan periode getarannya ($T$) berturut-turut adalah...",
        "correct": "$\\omega = 20\\text{ rad/s}$ dan $T = \\frac{\\pi}{10}\\text{ s}$ (sekitar $0{,}314\\text{ s}$), karena konstanta pegas pengganti paralel adalah $k_p = k_1 + k_2 = 400 + 400 = 800\\text{ N/m}$, sehingga frekuensi sudut $\\omega = \\sqrt{\\frac{k_p}{m}} = \\sqrt{\\frac{800}{2}} = \\sqrt{400} = 20\\text{ rad/s}$, dan periode $T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{20} = \\frac{\\pi}{10}\\text{ s}$.",
        "distractors": [
            "$\\omega = 10\\text{ rad/s}$ dan $T = \\frac{\\pi}{5}\\text{ s}$, karena kedua pegas keliru dihitung menggunakan formula susunan seri $k_s = 200\\text{ N/m}$.",
            "$\\omega = 40\\text{ rad/s}$ dan $T = \\frac{\\pi}{20}\\text{ s}$, dihitung dari penggandaan kuadrat frekuensi getaran alami pegas.",
            "$\\omega = 14{,}14\\text{ rad/s}$ dan $T = \\frac{\\pi}{7}\\text{ s}$, karena hanya memperhitungkan konstanta satu pegas tunggal tanpa paralel.",
            "$\\omega = 5\\text{ rad/s}$ dan $T = \\frac{2\\pi}{5}\\text{ s}$, dihitung dari rasio massa beban dibagi konstanta pegas dalam akar."
        ],
        "formula": {
            "title": "FREKUENSI SUDUT PEGAS PARALEL",
            "latex": "k_p = k_1 + k_2 = 2k = 800\\text{ N/m}; \\quad \\omega = \\sqrt{\\frac{k_p}{m}} = \\sqrt{\\frac{800}{2}} = 20\\text{ rad/s}; \\quad T = \\frac{2\\pi}{\\omega} = \\frac{\\pi}{10}\\text{ s}",
            "legend": "• $k_p$ = Konstanta ekuivalen pegas paralel ($400 + 400 = 800\\text{ N/m}$)<br>• $m = 2\\text{ kg}$<br>• $\\omega = 20\\text{ rad/s}$"
        },
        "hints": {
            "concept": "Pegas paralel: kp = k1 + k2 = 400 + 400 = 800 N/m. Frekuensi sudut omega = sqrt(kp / m). Periode T = 2pi / omega.",
            "execution": "omega = sqrt(800 / 2) = sqrt(400) = 20 rad/s. T = 2pi / 20 = pi / 10 s."
        }
    },
    {
        "id": "fis-lat-h-04",
        "materi": "FLUIDA DINAMIS (TEOREMA TORRICELLI & KONTINUITAS)",
        "topic": "Laju Aliran Efleks dengan Luas Tangki Terbatas",
        "stem": "Sebuah tangki silinder terbuka berisi air memiliki luas penampang $A_1 = 1\\text{ m}^2$. Di dasar tangki terdapat lubang kebocoran kecil berpenampang $A_2 = 10\\text{ cm}^2 = 10^{-3}\\text{ m}^2$. Pada saat ketinggian permukaan air dari dasar lubang adalah $h = 5\\text{ meter}$, laju semburan air yang keluar dari lubang dasar ($v_2$) dengan memperhitungkan turunnya permukaan air di tangki ($g = 10\\text{ m/s}^2$) adalah...",
        "correct": "$v_2 = 10\\text{ m/s}$ (tepatnya $\\sqrt{\\frac{2gh}{1 - (A_2/A_1)^2}} = \\sqrt{\\frac{100}{1 - 10^{-6}}} \\approx 10\\text{ m/s}$), karena rasio luas penampang $(A_2/A_1)^2 = 10^{-6}$ sangat kecil mendekati nol, sehingga kecepatan semburan sangat akurat didekati dengan teorema Torricelli standar $v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 5} = \\sqrt{100} = 10\\text{ m/s}$.",
        "distractors": [
            "$v_2 = 5\\text{ m/s}$, karena rumus Torricelli keliru tidak menyertakan angka 2 di dalam tanda akar kuadrat gravitasi tinggi.",
            "$v_2 = 14{,}14\\text{ m/s}$, dihitung dari perkalian percepatan gravitasi dengan kuadrat ketinggian air dalam tangki penampung.",
            "$v_2 = 20\\text{ m/s}$, dihitung dari penggandaan tinggi tangki sebelum dimasukkan ke dalam akar kuadrat fluida Bernoulli.",
            "$v_2 = 1\\text{ m/s}$, karena kecepatan semburan keliru dihitung dari pembagian volume air dengan luas penampang tangki atas."
        ],
        "formula": {
            "title": "TEOREMA TORRICELLI TERKOREKSI PERSAMAAN BERNOULLI",
            "latex": "v_2 = \\sqrt{\\frac{2gh}{1 - \\left(\\frac{A_2}{A_1}\\right)^2}} \\approx \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 5} = 10\\text{ m/s}",
            "legend": "• $h = 5\\text{ m}$, $g = 10\\text{ m/s}^2$<br>• Koreksi kontinuitas bernilai $\\approx 1 - 10^{-6} \\approx 1$<br>• $v_2 = 10\\text{ m/s}$"
        },
        "hints": {
            "concept": "Gunakan persamaan Bernoulli antara permukaan atas tangki dan lubang dasar. Jika A2 << A1, kecepatan efleks v2 = sqrt(2gh).",
            "execution": "v2 = sqrt(2 * 10 * 5) = sqrt(100) = 10 m/s."
        }
    },
    {
        "id": "fis-lat-h-05",
        "materi": "TERMODINAMIKA (MESIN PENDINGIN / REFRIGERATOR CARNOT)",
        "topic": "Koefisien Kinerja (COP) dan Daya Listrik Refrigerator",
        "stem": "Sebuah lemari es (refrigerator) beroperasi dengan siklus Carnot terbalik antara reservoir suhu rendah $T_C = -3^\\circ\\text{C}$ dan reservoir suhu tinggi $T_H = 27^\\circ\\text{C}$. Jika lemari es tersebut menyerap kalor sebesar $Q_C = 1.350\\text{ Joule}$ dari dalam ruang pendingin setiap detiknya, daya listrik masukan ($P$) yang dibutuhkan untuk menggerakkan kompresor refrigerator tersebut adalah...",
        "correct": "$P = 150\\text{ Watt}$, karena dalam skala Kelvin $T_C = 270\\text{ K}$ dan $T_H = 300\\text{ K}$, sehingga koefisien performa pendingin adalah $K_P = \\frac{T_C}{T_H - T_C} = \\frac{270}{300 - 270} = \\frac{270}{30} = 9$. Usaha per detik yang dibutuhkan kompresor adalah $W = \\frac{Q_C}{K_P} = \\frac{1.350}{9} = 150\\text{ Joule}$, yang setara dengan daya $150\\text{ Watt}$.",
        "distractors": [
            "$P = 135\\text{ Watt}$, karena suhu reservoir dihitung langsung menggunakan satuan derajat Celsius tanpa konversi ke Kelvin.",
            "$P = 300\\text{ Watt}$, dihitung dari efisiensi mesin pemanas Carnot standar dikalikan dengan total kalor serap reservoir.",
            "$P = 1.500\\text{ Watt}$, karena kalor yang diserap tertukar dengan kalor buangan yang dilepaskan ke lingkungan luar.",
            "$P = 450\\text{ Watt}$, dihitung dari pembagian kalor serap dengan selisih suhu reservoir dalam satuan Celsius."
        ],
        "formula": {
            "title": "KOEFISIEN PERFORMA (COP) REFRIGERATOR CARNOT",
            "latex": "K_P = \\frac{T_C}{T_H - T_C} = \\frac{270}{300 - 270} = 9; \\quad W = \\frac{Q_C}{K_P} = \\frac{1.350\\text{ J}}{9} = 150\\text{ J} \\implies P = 150\\text{ W}",
            "legend": "• $T_C = -3 + 273 = 270\\text{ K}$<br>• $T_H = 27 + 273 = 300\\text{ K}$<br>• $K_P = 9$<br>• Daya $P = \\frac{W}{t} = 150\\text{ Watt}$"
        },
        "hints": {
            "concept": "Konversi suhu ke Kelvin: Tc = 270 K, Th = 300 K. COP KP = Tc / (Th - Tc) = 270 / 30 = 9. Daya P = W / t = Qc / KP.",
            "execution": "KP = 9. P = 1.350 / 9 = 150 Watt."
        }
    },
    {
        "id": "fis-lat-h-06",
        "materi": "HUKUM II TERMODINAMIKA & ENTROPI",
        "topic": "Perubahan Entropi Sistem pada Proses Pencairan Es",
        "stem": "Sebongkah es bermassa $m = 500\\text{ gram}$ pada suhu $0^\\circ\\text{C}$ ditaruh dalam ruangan bersuhu konstan $27^\\circ\\text{C}$ hingga seluruhnya mencair menjadi air pada suhu $0^\\circ\\text{C}$. Diketahui kalor lebur es adalah $L_f = 334.000\\text{ J/kg} = 334\\text{ J/g}$. Perubahan entropi dari es tersebut ($\\Delta S_{\\text{es}}$) selama proses peleburan berlangsung adalah...",
        "correct": "$\\Delta S_{\\text{es}} = +611{,}7\\text{ J/K}$, karena proses peleburan terjadi secara isotermal pada suhu $T = 0^\\circ\\text{C} = 273\\text{ K}$ dengan menyerap kalor sebesar $Q = m L_f = 0{,}5\\text{ kg} \\times 334.000\\text{ J/kg} = 167.000\\text{ J}$, sehingga perubahan entropi es adalah $\\Delta S_{\\text{es}} = \\frac{Q}{T} = \\frac{167.000}{273} \\approx +611{,}72\\text{ J/K}$.",
        "distractors": [
            "$\\Delta S_{\\text{es}} = +556{,}7\\text{ J/K}$, karena suhu peleburan keliru dibagi dengan suhu ruangan 300 Kelvin, bukan suhu titik lebur es.",
            "$\\Delta S_{\\text{es}} = 0\\text{ J/K}$, karena suhu es tidak berubah selama fase mencair sehingga diasumsikan tidak ada perubahan entropi.",
            "$\\Delta S_{\\text{es}} = -611{,}7\\text{ J/K}$, karena es dianggap melepaskan kalor pembekuan ke lingkungan sekitarnya.",
            "$\\Delta S_{\\text{es}} = +167\\text{ J/K}$, dihitung dari kalor lebur dibagi dengan massa es tanpa memperhitungkan variabel suhu absolut termodinamika."
        ],
        "formula": {
            "title": "FORMULA PERUBAHAN ENTROPI ISOTERMAL",
            "latex": "Q = m L_f = 0{,}5 \\times 334.000 = 167.000\\text{ J}; \\quad \\Delta S = \\frac{Q}{T_{\\text{lebur}}} = \\frac{167.000}{273} \\approx +611{,}72\\text{ J/K}",
            "legend": "• $T_{\\text{lebur}} = 0^\\circ\\text{C} = 273\\text{ K}$ (suhu saat fase peleburan es berlangsung)<br>• Nilai $\\Delta S > 0$ menandakan penyerapan kalor meningkatkan ketidakteraturan sistem partikel es"
        },
        "hints": {
            "concept": "Peleburan es berlangsung pada T = 273 K. Kalor yang diserap Q = m * Lf = 0,5 * 334.000 = 167.000 J. Delta S = Q / T.",
            "execution": "Delta S = 167.000 / 273 = +611,7 J/K."
        }
    },
    {
        "id": "fis-lat-h-07",
        "materi": "GELOMBANG BUNYI (EFEK DOPPLER MULTIDIMENSI / ANGIN)",
        "topic": "Efek Doppler dengan Pergerakan Medium Angin",
        "stem": "Sebuah mobil pemadam kebakaran bergerak dengan kecepatan $v_s = 20\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 700\\text{ Hz}$. Seorang pengamat diam di pinggir jalan berada di depan mobil tersebut. Udara berhembus kencang searah gerak mobil pemadam (dari sumber ke arah pengamat) dengan kecepatan angin $v_w = 10\\text{ m/s}$. Jika cepat rambat bunyi di udara tenang adalah $v = 340\\text{ m/s}$, frekuensi bunyi sirine yang didengar oleh pengamat ($f_p$) adalah...",
        "correct": "$f_p = 742{,}4\\text{ Hz}$, karena hembusan angin searah rambatan bunyi meningkatkan cepat rambat efektif bunyi menjadi $v' = v + v_w = 340 + 10 = 350\\text{ m/s}$, dan pengamat diam ($v_p = 0$) didekati sumber ($v_s = 20\\text{ m/s}$), sehingga frekuensi terdengar adalah $f_p = \\left(\\frac{v' - v_p}{v' - v_s}\\right) f_s = \\left(\\frac{350}{350 - 20}\\right) 700 = \\left(\\frac{350}{330}\\right) 700 \\approx 742{,}42\\text{ Hz}$.",
        "distractors": [
            "$f_p = 743{,}75\\text{ Hz}$, dihitung dengan mengabaikan pengaruh kecepatan angin ($v_w = 0$) pada persamaan Efek Doppler standar.",
            "$f_p = 660{,}0\\text{ Hz}$, karena tanda kecepatan sumber dan arah angin keliru dioperasikan sebagai menjauhi pengamat di jalan.",
            "$f_p = 720{,}0\\text{ Hz}$, dihitung dari penambahan selisih kelajuan mobil dengan kecepatan angin terhadap frekuensi asli sirine.",
            "$f_p = 800{,}0\\text{ Hz}$, dihitung dari perbandingan kecepatan bunyi di udara tenang dibagi selisih kelajuan sumber."
        ],
        "formula": {
            "title": "EFEK DOPPLER DENGAN PENGARUH KECEPATAN ANGIN",
            "latex": "f_p = \\left(\\frac{(v \\pm v_w) \\pm v_p}{(v \\pm v_w) \\mp v_s}\\right) f_s = \\left(\\frac{340 + 10 - 0}{340 + 10 - 20}\\right) 700 = \\left(\\frac{350}{330}\\right) 700 \\approx 742{,}42\\text{ Hz}",
            "legend": "• Angin bertiup dari sumber ke pendengar $\\implies v' = v + v_w = 350\\text{ m/s}$<br>• Pendengar diam: $v_p = 0$<br>• Sumber mendekati pendengar: penyebut bertanda minus ($v' - v_s = 330\\text{ m/s}$)"
        },
        "hints": {
            "concept": "Jika ada angin bertiup dari sumber ke pendengar, cepat rambat bunyi efektif menjadi (v + vw) = 340 + 10 = 350 m/s. Gunakan rumus Doppler biasa dengan v efektif.",
            "execution": "fp = (350 / (350 - 20)) * 700 = (350 / 330) * 700 = 742,4 Hz."
        }
    },
    {
        "id": "fis-lat-h-08",
        "materi": "GELOMBANG MEKANIK STASIONER",
        "topic": "Letak Simpul dan Perut Gelombang Stasioner Ujung Terikat",
        "stem": "Sebuah tali elastis sepanjang $L = 2\\text{ meter}$ salah satu ujungnya diikat kuat pada dinding tetap dan ujung lainnya digetarkan harmonik sehingga terbentuk gelombang stasioner dengan 4 gelung (pola nada atas ketiga / 4 perut). Persamaan gelombang stasioner tersebut memiliki panjang gelombang $\\lambda = 1\\text{ meter}$. Jarak simpul ke-3 ($x_{s3}$) dan perut ke-2 ($x_{p2}$) diukur dari ujung pemantul terikat berturut-turut adalah...",
        "correct": "$x_{s3} = 1{,}0\\text{ meter}$ dan $x_{p2} = 0{,}375\\text{ meter}$ (atau $\\frac{3}{8}\\text{ m}$), karena pada ujung terikat letak simpul ke-$n$ adalah $x_{sn} = (n - 1)\\frac{\\lambda}{2}$ sehingga $x_{s3} = (3 - 1)\\frac{1}{2} = 1{,}0\\text{ m}$, sedangkan letak perut ke-$n$ adalah $x_{pn} = (2n - 1)\\frac{\\lambda}{4}$ sehingga $x_{p2} = (2(2) - 1)\\frac{1}{4} = \\frac{3}{4}\\lambda = 0{,}75\\text{ m}$ jika $n=2$ rumus $(2n-1)/4$ menghasilkan $\\frac{3}{4}(1) \\times 0{,}5$... tepatnya $x_{p2} = (2(2)-1)\\frac{\\lambda}{4} = \\frac{3}{4}(0{,}5)$ jika $\\lambda = 1\\text{ m}$, $x_{p2} = \\frac{3}{4}(1) = 0{,}75\\text{ m}$... mari periksa: $x_{s1} = 0$, $x_{p1} = \\lambda/4 = 0{,}25\\text{ m}$, $x_{s2} = \\lambda/2 = 0{,}5\\text{ m}$, $x_{p2} = 3\\lambda/4 = 0{,}75\\text{ m}$, $x_{s3} = \\lambda = 1{,}0\\text{ m}$.",
        "distractors": [
            "$x_{s3} = 0{,}75\\text{ meter}$ dan $x_{p2} = 0{,}5\\text{ meter}$, karena formula letak simpul dan perut tertukar antara ujung terikat dan ujung bebas.",
            "$x_{s3} = 1{,}5\\text{ meter}$ dan $x_{p2} = 1{,}0\\text{ meter}$, dihitung dengan mengalikan nomor simpul langsung dengan panjang gelombang.",
            "$x_{s3} = 0{,}5\\text{ meter}$ dan $x_{p2} = 0{,}25\\text{ meter}$, karena hanya memperhitungkan separuh dari panjang gelombang yang sebenarnya.",
            "$x_{s3} = 2{,}0\\text{ meter}$ dan $x_{p2} = 1{,}25\\text{ meter}$, dihitung dari ujung sumber getaran bukan dari ujung pemantul terikat."
        ],
        "formula": {
            "title": "FORMULA GELOMBANG STASIONER UJUNG TERIKAT",
            "latex": "x_{sn} = (n - 1)\\frac{\\lambda}{2} \\implies x_{s3} = (3 - 1)\\frac{1}{2} = 1{,}0\\text{ m}; \\quad x_{pn} = (2n - 1)\\frac{\\lambda}{4} \\implies x_{p2} = (4 - 1)\\frac{1}{4} = 0{,}75\\text{ m}",
            "legend": "• Ujung terikat selalu dimulai dari Simpul 1 di $x = 0$<br>• $x_{s1} = 0$, $x_{s2} = 0{,}5\\text{ m}$, $x_{s3} = 1{,}0\\text{ m}$<br>• $x_{p1} = 0{,}25\\text{ m}$, $x_{p2} = 0{,}75\\text{ m}$"
        },
        "hints": {
            "concept": "Pada ujung terikat, pemantul adalah simpul: xs_n = (n - 1) * lambda/2, dan xp_n = (2n - 1) * lambda/4.",
            "execution": "xs3 = (3 - 1) * 1 / 2 = 1,0 m. xp2 = (2*2 - 1) * 1 / 4 = 3/4 = 0,75 m."
        }
    },
    {
        "id": "fis-lat-h-09",
        "materi": "OPTIKA FISIS & INSTRUMEN (DAYA URAI RAYLEIGH)",
        "topic": "Kriteria Rayleigh dan Diameter Apertur Teleskop",
        "stem": "Sebuah teleskop luar angkasa digunakan untuk memisahkan bayangan dua bintang kembar yang terpisah dengan jarak sudut $\\theta_R = 2{,}44 \\times 10^{-6}\\text{ radian}$. Pengamatan dilakukan menggunakan cahaya tampak dengan panjang gelombang rata-rata $\\lambda = 500\\text{ nm} = 5 \\times 10^{-7}\\text{ meter}$. Berdasarkan Kriteria Rayleigh untuk difraksi apertur melingkar, diameter minimum lensa objektif teleskop ($D$) agar kedua bintang tersebut dapat dibedakan secara terpisah adalah...",
        "correct": "$D = 0{,}25\\text{ meter}$ (atau $25\\text{ cm}$), dihitung dari Kriteria Rayleigh $\\theta_R = 1{,}22 \\frac{\\lambda}{D}$, sehingga diameter objektif minimum adalah $D = \\frac{1{,}22 \\lambda}{\\theta_R} = \\frac{1{,}22 \\times (5 \\times 10^{-7}\\text{ m})}{2{,}44 \\times 10^{-6}\\text{ rad}} = \\frac{6{,}1 \\times 10^{-7}}{2{,}44 \\times 10^{-6}} = 0{,}25\\text{ m}$.",
        "distractors": [
            "$D = 0{,}50\\text{ meter}$, karena faktor difraksi Airy 1,22 keliru digandakan menjadi 2,44 saat perhitungan fraksi sudut.",
            "$D = 0{,}10\\text{ meter}$, dihitung tanpa mengikutsertakan tetapan difraksi lubang lingkaran Kriteria Rayleigh.",
            "$D = 1{,}22\\text{ meter}$, karena tetapan Rayleigh langsung dijadikan nilai diameter fisik cermin objektif teleskop.",
            "$D = 0{,}05\\text{ meter}$, dihitung dari perbandingan panjang gelombang terhadap sudut pemisahan tanpa pembagian eksponen."
        ],
        "formula": {
            "title": "KRITERIA DAYA URAI RAYLEIGH (APERTUR MELINGKAR)",
            "latex": "\\theta_R = 1{,}22 \\frac{\\lambda}{D} \\implies D = \\frac{1{,}22 \\lambda}{\\theta_R} = \\frac{1{,}22 \\times (5 \\times 10^{-7})}{2{,}44 \\times 10^{-6}} = \\frac{1{,}22}{2{,}44} \\times 0{,}5 = 0{,}5 \\times 0{,}5 = 0{,}25\\text{ m}",
            "legend": "• $\\theta_R = 2{,}44 \\times 10^{-6}\\text{ rad}$<br>• $\\lambda = 5 \\times 10^{-7}\\text{ m}$<br>• Angka $1{,}22$ berasal dari nol pertama fungsi Bessel orde satu ($J_1(x)$)<br>• $D = 0{,}25\\text{ m} = 25\\text{ cm}$"
        },
        "hints": {
            "concept": "Daya urai sudut apertur melingkar memenuhi kriteria Rayleigh: theta = 1,22 * lambda / D. Maka D = 1,22 * lambda / theta.",
            "execution": "D = (1,22 * 5e-7) / 2,44e-6 = 6,1e-7 / 2,44e-6 = 0,25 m = 25 cm."
        }
    },
    {
        "id": "fis-lat-h-10",
        "materi": "MEDAN MAGNET & INDUKTANSI DIRI",
        "topic": "Energi Magnetik dalam Solenoida Berinti Feromagnetik",
        "stem": "Sebuah solenoida ideal memiliki panjang $l = 40\\text{ cm} = 0{,}4\\text{ m}$, luas penampang $A = 20\\text{ cm}^2 = 2 \\times 10^{-3}\\text{ m}^2$, dan terdiri atas $N = 1.000\\text{ lilitan}$. Bagian dalam solenoida diisi bahan feromagnetik dengan permeabilitas relatif $\\mu_r = 500$ (diketahui $\\mu_0 = 4\\pi \\times 10^{-7}\\text{ Wb/(A}\\cdot\\text{m)}$). Jika solenoida dialiri arus listrik konstan $I = 2\\text{ Ampere}$, energi magnetik ($W_m$) yang tersimpan di dalam medan magnetik solenoida tersebut adalah...",
        "correct": "$W_m = 2\\pi \\times 10^{-1}\\text{ Joule} \\approx 0{,}628\\text{ Joule}$, karena induktansi diri solenoida berinti bahan adalah $L = \\frac{\\mu_r \\mu_0 N^2 A}{l} = \\frac{500 \\times (4\\pi \\times 10^{-7}) \\times (10^3)^2 \\times (2 \\times 10^{-3})}{0{,}4} = \\frac{500 \\times 4\\pi \\times 10^{-7} \\times 10^6 \\times 2 \\times 10^{-3}}{0{,}4} = \\frac{4\\pi \\times 10^{-1}}{0{,}4} = \\pi \\times 10^{-1}\\text{ H} = 0{,}1\\pi\\text{ H}$. Energi tersimpan adalah $W_m = \\frac{1}{2} L I^2 = \\frac{1}{2} (0{,}1\\pi) (2^2) = 0{,}2\\pi\\text{ J} \\approx 0{,}628\\text{ J}$.",
        "distractors": [
            "$W_m = 1{,}256 \\times 10^{-3}\\text{ Joule}$, karena pengaruh penguatan medan oleh permeabilitas relatif inti feromagnetik tidak diikutsertakan.",
            "$W_m = 6{,}28\\text{ Joule}$, karena luas penampang solenoida tidak dikonversi dari satuan sentimeter kuadrat ke meter kuadrat.",
            "$W_m = 3{,}14\\text{ Joule}$, dihitung dari perkalian induktansi diri dengan arus tanpa faktor pembagian satu per dua.",
            "$W_m = 0{,}02\\pi\\text{ Joule}$, dihitung dari asumsi jumlah lilitan hanya bernilai pangkat satu dalam rumus induktansi diri."
        ],
        "formula": {
            "title": "INDUKTANSI DIRI & ENERGI MEDAN MAGNETIK SOLENOIDA",
            "latex": "L = \\frac{\\mu_r \\mu_0 N^2 A}{l} = \\frac{500 \\times (4\\pi \\times 10^{-7}) \\times 10^6 \\times (2 \\times 10^{-3})}{0{,}4} = 0{,}1\\pi\\text{ H}; \\quad W_m = \\frac{1}{2} L I^2 = \\frac{1}{2}(0{,}1\\pi)(4) = 0{,}2\\pi\\text{ J} \\approx 0{,}628\\text{ J}",
            "legend": "• $\\mu = \\mu_r \\mu_0 = 500 \\times 4\\pi \\times 10^{-7}$<br>• $L = 0{,}1\\pi\\text{ Henry} \\approx 0{,}314\\text{ H}$<br>• $W_m = \\frac{1}{2} L I^2 = 0{,}2\\pi\\text{ J} \\approx 0{,}628\\text{ Joule}$"
        },
        "hints": {
            "concept": "L = mu_r * mu_0 * N^2 * A / l. Energi magnetik Wm = 1/2 * L * I^2.",
            "execution": "L = 500 * 4pi*1e-7 * 1e6 * 2e-3 / 0,4 = 0,1pi H. Wm = 1/2 * 0,1pi * 2^2 = 0,2pi J = 0,628 J."
        }
    },
    {
        "id": "fis-lat-h-11",
        "materi": "INDUKSI ELEKTROMAGNETIK",
        "topic": "Gaya Gerak Listrik (GGL) Batang Berputar dalam Medan Magnet",
        "stem": "Sebuah kawat tembaga lurus dengan panjang $L = 50\\text{ cm} = 0{,}5\\text{ m}$ diputar dengan salah satu ujungnya sebagai poros pada frekuensi putaran konstan $n = 600\\text{ rpm}$ di dalam bidang yang tegak lurus terhadap medan magnetik homogen $B = 0{,}4\\text{ Tesla}$. Beda potensial atau GGL induksi ($\\varepsilon$) yang dibangkitkan antara kedua ujung kawat tersebut adalah...",
        "correct": "$\\varepsilon = 3{,}14\\text{ Volt}$ (atau $\\pi\\text{ Volt}$), karena kecepatan sudut putaran adalah $\\omega = 600 \\times \\frac{2\\pi}{60} = 20\\pi\\text{ rad/s}$, sehingga luas sapuan lingkaran per detik memicu GGL induksi $\\varepsilon = \\frac{1}{2} B \\omega L^2 = \\frac{1}{2} (0{,}4) (20\\pi) (0{,}5)^2 = 0{,}2 \\times 20\\pi \\times 0{,}25 = \\pi\\text{ Volt} \\approx 3{,}14\\text{ Volt}$.",
        "distractors": [
            "$\\varepsilon = 6{,}28\\text{ Volt}$ (atau $2\\pi\\text{ Volt}$), karena formula GGL batang berputar keliru tidak dibagi dua ($BL^2\\omega$).",
            "$\\varepsilon = 1{,}57\\text{ Volt}$ (atau $0{,}5\\pi\\text{ Volt}$), dihitung dari kesalahan memasukkan panjang batang menjadi nilai jari-jari kuadrat.",
            "$\\varepsilon = 120\\text{ Volt}$, karena frekuensi sudut langsung menggunakan satuan rpm tanpa konversi ke radian per sekon.",
            "$\\varepsilon = 0{,}5\\text{ Volt}$, dihitung dari rumus batang bergerak translasi lurus ($BLv$) dengan kecepatan ujung poros pusat."
        ],
        "formula": {
            "title": "GGL INDUKSI BATANG KONDUKTOR BERPUTAR",
            "latex": "\\omega = \\frac{600 \\times 2\\pi}{60} = 20\\pi\\text{ rad/s}; \\quad \\varepsilon = \\frac{1}{2} B \\omega L^2 = \\frac{1}{2} (0{,}4)(20\\pi)(0{,}5)^2 = \\pi\\text{ Volt} \\approx 3{,}14\\text{ V}",
            "legend": "• Kecepatan linier rata-rata kawat yang berputar dari poros ke ujung adalah $\\bar{v} = \\frac{0 + \\omega L}{2} = \\frac{1}{2} \\omega L$<br>• $\\varepsilon = B L \\bar{v} = \\frac{1}{2} B \\omega L^2 = \\pi\\text{ V}$"
        },
        "hints": {
            "concept": "Konversi rpm ke rad/s: omega = 600 * 2pi / 60 = 20pi rad/s. GGL batang berputar: epsilon = 1/2 * B * omega * L^2.",
            "execution": "epsilon = 0,5 * 0,4 * 20pi * (0,5)^2 = 4pi * 0,25 = pi Volt = 3,14 V."
        }
    },
    {
        "id": "fis-lat-h-12",
        "materi": "RANGKAIAN ARUS BOLAK-BALIK (RLC)",
        "topic": "Resonansi RLC Seri, Faktor Daya, dan Daya Nyata Disipasi",
        "stem": "Sebuah rangkaian RLC seri dihubungkan dengan sumber tegangan bolak-balik $V(t) = 100\\sqrt{2} \\sin(1.000t)\\text{ Volt}$. Rangkaian terdiri atas resistor $R = 30\\,\\Omega$, induktor $L = 80\\text{ mH} = 0{,}08\\text{ H}$, dan kapasitor $C = 25\\,\\mu\\text{F} = 25 \\times 10^{-6}\\text{ F}$. Reaktansi induktif ($X_L$), reaktansi kapasitif ($X_C$), faktor daya ($\\cos\\phi$), dan daya rata-rata disipasi pada resistor ($P_{\\text{nyata}}$) adalah...",
        "correct": "$X_L = 80\\,\\Omega$, $X_C = 40\\,\\Omega$, $\\cos\\phi = 0{,}6$, dan $P_{\\text{nyata}} = 120\\text{ Watt}$, karena $X_L = \\omega L = 1.000 \\times 0{,}08 = 80\\,\\Omega$, $X_C = \\frac{1}{\\omega C} = \\frac{1}{1.000 \\times 25 \\times 10^{-6}} = 40\\,\\Omega$. Impedansi $Z = \\sqrt{R^2 + (X_L - X_C)^2} = \\sqrt{30^2 + (80 - 40)^2} = \\sqrt{900 + 1.600} = 50\\,\\Omega$. Arus efektif $I_{\\text{ef}} = \\frac{V_{\\text{ef}}}{Z} = \\frac{100}{50} = 2\\text{ A}$. Faktor daya $\\cos\\phi = \\frac{R}{Z} = \\frac{30}{50} = 0{,}6$, dan daya nyata $P = I_{\\text{ef}}^2 R = 2^2 \\times 30 = 120\\text{ Watt}$.",
        "distractors": [
            "$X_L = 80\\,\\Omega$, $X_C = 40\\,\\Omega$, $\\cos\\phi = 1{,}0$, dan $P_{\\text{nyata}} = 200\\text{ Watt}$, karena rangkaian diasumsikan mengalami resonansi murni padahal reaktansinya tidak saling meniadakan.",
            "$X_L = 40\\,\\Omega$, $X_C = 80\\,\\Omega$, $\\cos\\phi = 0{,}8$, dan $P_{\\text{nyata}} = 160\\text{ Watt}$, karena formula reaktansi induktif dan kapasitif tertukar perhitungannya.",
            "$X_L = 80\\,\\Omega$, $X_C = 40\\,\\Omega$, $\\cos\\phi = 0{,}5$, dan $P_{\\text{nyata}} = 100\\text{ Watt}$, dihitung dari rasio tegangan puncak bukan tegangan efektif RMS.",
            "$X_L = 100\\,\\Omega$, $X_C = 50\\,\\Omega$, $\\cos\\phi = 0{,}6$, dan $P_{\\text{nyata}} = 60\\text{ Watt}$, dihitung dari perkalian impedansi terhadap frekuensi sumber jala-jala listrik."
        ],
        "formula": {
            "title": "IMPEDANSI & DISIPASI DAYA RLC SERI",
            "latex": "X_L = \\omega L = 80\\,\\Omega; \\quad X_C = \\frac{1}{\\omega C} = 40\\,\\Omega; \\quad Z = \\sqrt{30^2 + 40^2} = 50\\,\\Omega; \\quad \\cos\\phi = \\frac{30}{50} = 0{,}6; \\quad P = I_{\\text{ef}}^2 R = 2^2 \\times 30 = 120\\text{ W}",
            "legend": "• $V_{\\text{ef}} = \\frac{V_{\\max}}{\\sqrt{2}} = 100\\text{ V}$<br>• $I_{\\text{ef}} = \\frac{100}{50} = 2\\text{ A}$<br>• $P_{\\text{nyata}} = V_{\\text{ef}} I_{\\text{ef}} \\cos\\phi = 100 \\times 2 \\times 0{,}6 = 120\\text{ Watt}$"
        },
        "hints": {
            "concept": "Hitung XL = omega * L dan XC = 1 / (omega * C). Impedansi Z = sqrt(R^2 + (XL - XC)^2). I_ef = V_ef / Z. cos(phi) = R / Z. P = I_ef^2 * R.",
            "execution": "XL = 80 ohm, XC = 40 ohm, Z = 50 ohm. I_ef = 100/50 = 2 A. cos(phi) = 30/50 = 0,6. P = 2^2 * 30 = 120 W."
        }
    },
    {
        "id": "fis-lat-h-13",
        "materi": "RADIASI BENDA HITAM & PERGESERAN WIEN",
        "topic": "Perbandingan Daya Radiasi Bintang Berdasarkan Suhu & Radius",
        "stem": "Dua buah bintang $A$ dan $B$ diamati memancarkan radiasi termal benda hitam ideal. Puncak spektrum emisi radiasi bintang $A$ berada pada panjang gelombang $\\lambda_A = 400\\text{ nm}$, sedangkan bintang $B$ berada pada panjang gelombang $\\lambda_B = 800\\text{ nm}$. Jika radius bintang $A$ adalah dua kali radius bintang $B$ ($R_A = 2 R_B$), perbandingan daya total radiasi yang dipancarkan bintang $A$ terhadap bintang $B$ ($\\frac{P_A}{P_B}$) menurut Hukum Stefan-Boltzmann dan Hukum Pergeseran Wien adalah...",
        "correct": "$\\frac{P_A}{P_B} = 64 : 1$, karena menurut Hukum Pergeseran Wien $\\lambda_{\\max} T = C$, rasio suhu kedua bintang adalah $\\frac{T_A}{T_B} = \\frac{\\lambda_B}{\\lambda_A} = \\frac{800}{400} = 2$. Daya radiasi total bola bintang berbanding lurus dengan luas permukaan dan suhu pangkat empat ($P = \\sigma A T^4 = 4\\pi R^2 \\sigma T^4$), sehingga $\\frac{P_A}{P_B} = \\left(\\frac{R_A}{R_B}\\right)^2 \\left(\\frac{T_A}{T_B}\\right)^4 = (2)^2 \\times (2)^4 = 4 \\times 16 = 64$.",
        "distractors": [
            "$\\frac{P_A}{P_B} = 16 : 1$, karena hanya memperhitungkan rasio suhu pangkat empat tanpa mengalikan rasio kuadrat radius bintang.",
            "$\\frac{P_A}{P_B} = 32 : 1$, dihitung dari asumsi radiasi berbanding lurus dengan pangkat lima suhu permukaan benda.",
            "$\\frac{P_A}{P_B} = 8 : 1$, karena suhu permukaan bintang dianggap berbanding lurus linier terhadap panjang gelombang puncak.",
            "$\\frac{P_A}{P_B} = 4 : 1$, karena mengabaikan variabel suhu dan hanya memperhitungkan faktor luas permukaan bola bintang."
        ],
        "formula": {
            "title": "HUKUM WIEN & DAYA RADIASI STEFAN-BOLTZMANN",
            "latex": "\\frac{T_A}{T_B} = \\frac{\\lambda_B}{\\lambda_A} = 2; \\quad \\frac{P_A}{P_B} = \\left(\\frac{R_A}{R_B}\\right)^2 \\left(\\frac{T_A}{T_B}\\right)^4 = 2^2 \\times 2^4 = 4 \\times 16 = 64",
            "legend": "• $\\lambda_A = 400\\text{ nm} \\implies T_A = 2 T_B$<br>• Luas permukaan bintang $A_{\\text{bola}} = 4\\pi R^2$<br>• Daya total $P = \\sigma (4\\pi R^2) T^4 \\implies P_A / P_B = 64$"
        },
        "hints": {
            "concept": "Hukum Wien: T berbanding terbalik dengan lambda_max, sehingga TA/TB = lambda_B/lambda_A = 800/400 = 2. Daya Stefan-Boltzmann: P sebanding dengan R^2 * T^4.",
            "execution": "PA / PB = (RA/RB)^2 * (TA/TB)^4 = (2)^2 * (2)^4 = 4 * 16 = 64."
        }
    },
    {
        "id": "fis-lat-h-14",
        "materi": "FISIKA KUANTUM (EFEK FOTOLISTRIK)",
        "topic": "Penentuan Fungsi Kerja Logam dan Potensial Henti",
        "stem": "Permukaan sebuah pelat logam disinari dengan foton monokromatik berenergi $E = 4{,}5\\text{ eV}$. Diketahui fungsi kerja logam tersebut adalah $W_0 = 2{,}5\\text{ eV}$ dan muatan elementer elektron $e = 1{,}6 \\times 10^{-19}\\text{ Coulomb}$. Energi kinetik maksimum fotoelektron yang terlepas ($E_{k,\\max}$) dan besar potensial henti ($V_0$) yang diperlukan untuk menghentikan seluruh arus fotolistrik tersebut adalah...",
        "correct": "$E_{k,\\max} = 2{,}0\\text{ eV}$ dan $V_0 = 2{,}0\\text{ Volt}$, karena menurut persamaan fotolistrik Einstein, energi kinetik maksimum fotoelektron adalah $E_{k,\\max} = hf - W_0 = 4{,}5\\text{ eV} - 2{,}5\\text{ eV} = 2{,}0\\text{ eV}$. Potensial henti memenuhi hubungan $e V_0 = E_{k,\\max}$, sehingga $V_0 = \\frac{2{,}0\\text{ eV}}{e} = 2{,}0\\text{ Volt}$.",
        "distractors": [
            "$E_{k,\\max} = 7{,}0\\text{ eV}$ dan $V_0 = 7{,}0\\text{ Volt}$, karena energi foton datang keliru dijumlahkan dengan fungsi kerja logam emiter.",
            "$E_{k,\\max} = 1{,}8\\text{ eV}$ dan $V_0 = 1{,}8\\text{ Volt}$, dihitung dari efisiensi kuantum pelepasan elektron emisi termionik.",
            "$E_{k,\\max} = 2{,}5\\text{ eV}$ dan $V_0 = 2{,}5\\text{ Volt}$, karena menyamakan energi kinetik maksimum dengan nilai fungsi kerja logam.",
            "$E_{k,\\max} = 0{,}5\\text{ eV}$ dan $V_0 = 0{,}5\\text{ Volt}$, dihitung dari kuadrat rasio fungsi kerja terhadap energi foton sinar datang."
        ],
        "formula": {
            "title": "PERSAMAAN EFEK FOTOLISTRIK EINSTEIN",
            "latex": "E_{k,\\max} = hf - W_0 = 4{,}5\\text{ eV} - 2{,}5\\text{ eV} = 2{,}0\\text{ eV}; \\quad e V_0 = E_{k,\\max} \\implies V_0 = 2{,}0\\text{ Volt}",
            "legend": "• $E_{k,\\max}$ adalah energi kinetik fotoelektron tercepat<br>• $V_0$ adalah tegangan pembalik (retarding potential) untuk memutus arus elektron anoda"
        },
        "hints": {
            "concept": "Gunakan persamaan Einstein: Ek_max = E_foton - W0. Hubungan potensial henti: e * V0 = Ek_max.",
            "execution": "Ek_max = 4,5 eV - 2,5 eV = 2,0 eV. V0 = 2,0 V."
        }
    },
    {
        "id": "fis-lat-h-15",
        "materi": "FISIKA KUANTUM (EFEK COMPTON)",
        "topic": "Pergeseran Panjang Gelombang Hamburan Hamburan Compton",
        "stem": "Sebuah foton sinar-X memiliki panjang gelombang datang $\\lambda = 0{,}0200\\text{ nm}$ ($2{,}00 \\times 10^{-11}\\text{ m}$). Foton tersebut menumbuk elektron diam dan dihamburkan dengan sudut hamburan $\\theta = 60^\\circ$ ($\\cos 60^\\circ = 0{,}5$). Jika panjang gelombang Compton elektron adalah $\\lambda_C = \\frac{h}{m_e c} = 0{,}00243\\text{ nm} = 2{,}43 \\times 10^{-12}\\text{ m}$, panjang gelombang foton hambur ($\\lambda'$) setelah tumbukan adalah...",
        "correct": "$\\lambda' = 0{,}0212\\text{ nm}$ (atau $2{,}1215 \\times 10^{-11}\\text{ m}$), karena pergeseran Compton adalah $\\Delta\\lambda = \\lambda' - \\lambda = \\lambda_C (1 - \\cos\\theta) = 0{,}00243\\text{ nm} \\times (1 - 0{,}5) = 0{,}001215\\text{ nm}$, sehingga panjang gelombang foton terhambur bertambah panjang menjadi $\\lambda' = \\lambda + \\Delta\\lambda = 0{,}0200 + 0{,}001215 = 0{,}021215\\text{ nm} \\approx 0{,}0212\\text{ nm}$.",
        "distractors": [
            "$\\lambda' = 0{,}0188\\text{ nm}$, karena panjang gelombang foton dihamburkan keliru dikurangi akibat salah asumsi bahwa foton menyerap energi dari elektron.",
            "$\\lambda' = 0{,}0224\\text{ nm}$, dihitung dari sudut hamburan sembilan puluh derajat dengan nilai sinus satu.",
            "$\\lambda' = 0{,}0243\\text{ nm}$, karena langsung menambahkan konstanta panjang gelombang Compton utuh tanpa faktor sudut.",
            "$\\lambda' = 0{,}0100\\text{ nm}$, dihitung dari pembagian panjang gelombang foton datang dengan nilai cosinus sudut hambur."
        ],
        "formula": {
            "title": "FORMULA HAMBURAN COMPTON",
            "latex": "\\Delta\\lambda = \\lambda' - \\lambda = \\frac{h}{m_e c}(1 - \\cos\\theta) = 0{,}00243 \\times (1 - 0{,}5) = 0{,}001215\\text{ nm}; \\quad \\lambda' = 0{,}0200 + 0{,}001215 = 0{,}021215\\text{ nm}",
            "legend": "• $\\lambda_C = \\frac{h}{m_e c} \\approx 2{,}43 \\times 10^{-12}\\text{ m}$ (Panjang gelombang Compton)<br>• Foton kehilangan energi kinetik yang diserahkan ke elektron recoil, sehingga frekuensinya turun dan panjang gelombangnya selalu bertambah ($\\lambda' > \\lambda$)"
        },
        "hints": {
            "concept": "Rumus hamburan Compton: lambda' - lambda = (h / (me * c)) * (1 - cos theta). Delta_lambda = lambda_C * (1 - cos 60).",
            "execution": "Delta_lambda = 0,00243 * (1 - 0,5) = 0,001215 nm. lambda' = 0,0200 + 0,001215 = 0,0212 nm."
        }
    },
    {
        "id": "fis-lat-h-16",
        "materi": "STRUKTUR ATOM (MODEL BOHR)",
        "topic": "Transisi Elektron dan Foton Deret Balmer",
        "stem": "Dalam model atom Bohr untuk hidrogen, sebuah elektron melakukan transisi eksitasi dari tingkat energi $n = 2$ ke tingkat energi $n = 4$ akibat menyerap sebutir foton. Jika energi dasar atom hidrogen pada $n = 1$ adalah $E_1 = -13{,}6\\text{ eV}$, energi foton yang diserap ($E_{\\text{foton}}$) dan panjang gelombangnya ($\\lambda$) adalah... (Gunakan $hc = 1.240\\text{ eV}\\cdot\\text{nm}$)",
        "correct": "$E_{\\text{foton}} = 2{,}55\\text{ eV}$ dan $\\lambda \\approx 486\\text{ nm}$, karena tingkat energi $E_2 = \\frac{-13{,}6}{2^2} = -3{,}4\\text{ eV}$ dan $E_4 = \\frac{-13{,}6}{4^2} = -0{,}85\\text{ eV}$, sehingga selisih energi yang diserap foton adalah $\\Delta E = E_4 - E_2 = -0{,}85 - (-3{,}4) = 2{,}55\\text{ eV}$. Panjang gelombang foton adalah $\\lambda = \\frac{hc}{\\Delta E} = \\frac{1.240\\text{ eV}\\cdot\\text{nm}}{2{,}55\\text{ eV}} \\approx 486{,}27\\text{ nm}$ (garis biru-kehijauan $H_\\beta$ deret Balmer).",
        "distractors": [
            "$E_{\\text{foton}} = 3{,}40\\text{ eV}$ dan $\\lambda \\approx 365\\text{ nm}$, dihitung dari transisi elektron langsung dari tak hingga menuju lintasan kedua.",
            "$E_{\\text{foton}} = 10{,}2\\text{ eV}$ dan $\\lambda \\approx 121\\text{ nm}$, karena merupakan transisi eksitasi dari kulit dasar n = 1 ke n = 2 pada deret Lyman.",
            "$E_{\\text{foton}} = 1{,}89\\text{ eV}$ dan $\\lambda \\approx 656\\text{ nm}$, karena merupakan transisi dari n = 3 ke n = 2 (garis merah H-alfa).",
            "$E_{\\text{foton}} = 0{,}85\\text{ eV}$ dan $\\lambda \\approx 1.458\\text{ nm}$, dihitung dari nilai mutlak energi orbital n = 4 atom hidrogen."
        ],
        "formula": {
            "title": "ENERGI TRANSISI ELEKTRON MODEL BOHR",
            "latex": "E_n = -\\frac{13{,}6\\text{ eV}}{n^2}; \\quad \\Delta E = E_4 - E_2 = -0{,}85 - (-3{,}40) = 2{,}55\\text{ eV}; \\quad \\lambda = \\frac{hc}{\\Delta E} = \\frac{1.240}{2{,}55} \\approx 486{,}3\\text{ nm}",
            "legend": "• $E_2 = -3{,}40\\text{ eV}$, $E_4 = -0{,}85\\text{ eV}$<br>• Transisi $n=2 \\to n=4$ menyerap foton garis $H_\\beta$ deret Balmer pada spektrum cahaya tampak"
        },
        "hints": {
            "concept": "En = -13,6 / n^2 eV. Hitung E2 = -13,6/4 = -3,4 eV dan E4 = -13,6/16 = -0,85 eV. Delta E = E4 - E2. lambda = hc / Delta E.",
            "execution": "Delta E = -0,85 - (-3,4) = 2,55 eV. lambda = 1.240 / 2,55 = 486 nm."
        }
    },
    {
        "id": "fis-lat-h-17",
        "materi": "RELATIVITAS KHUSUS (DILATASI WAKTU)",
        "topic": "Peluruhan Muon Kosmik di Atmosfer Bumi",
        "stem": "Partikel muon tercipta di lapisan atas atmosfer bumi pada ketinggian $h = 9\\text{ km}$ di atas permukaan laut. Muon bergerak lurus menuju permukaan bumi dengan kecepatan relativistik $v = 0{,}98c$ (faktor Lorentz $\\gamma \\approx 5{,}0$). Waktu hidup rata-rata partikel muon pada kerangka diamnya adalah $\\Delta t_0 = 2{,}2\\,\\mu\\text{s} = 2{,}2 \\times 10^{-6}\\text{ sekon}$. Ditinjau dari kerangka acuan pengamat di bumi, waktu hidup muon ($\\Delta t$) dan jarak yang mampu ditempuhnya sebelum meluruh ($s$) adalah... ($c = 3 \\times 10^8\\text{ m/s}$)",
        "correct": "$\\Delta t = 11\\,\\mu\\text{s}$ dan $s = 3{,}234\\text{ km}$ (sehingga sebagian muon mampu mencapai detektor di permukaan laut melalui efek relativistik), karena waktu hidup menurut pengamat bumi mengalami dilatasi waktu $\\Delta t = \\gamma \\Delta t_0 = 5{,}0 \\times 2{,}2\\,\\mu\\text{s} = 11\\,\\mu\\text{s} = 1{,}1 \\times 10^{-5}\\text{ s}$. Jarak tempuh dalam kerangka bumi adalah $s = v \\Delta t = (0{,}98 \\times 3 \\times 10^8\\text{ m/s}) \\times (1{,}1 \\times 10^{-5}\\text{ s}) = 2{,}94 \\times 10^8 \\times 1{,}1 \\times 10^{-5} \\approx 3.234\\text{ meter} = 3{,}234\\text{ km}$.",
        "distractors": [
            "$\\Delta t = 2{,}2\\,\\mu\\text{s}$ dan $s = 0{,}647\\text{ km}$, dihitung dengan mengabaikan dilatasi waktu relativistik mekanika klasik Einstein.",
            "$\\Delta t = 0{,}44\\,\\mu\\text{s}$ dan $s = 0{,}129\\text{ km}$, karena waktu hidup muon keliru dibagi dengan faktor Lorentz.",
            "$\\Delta t = 22\\,\\mu\\text{s}$ dan $s = 6{,}468\\text{ km}$, dihitung dari asumsi faktor Lorentz sebesar sepuluh.",
            "$\\Delta t = 55\\,\\mu\\text{s}$ dan $s = 16{,}17\\text{ km}$, dihitung dari pemangkatan kuadrat rasio kecepatan partikel muon."
        ],
        "formula": {
            "title": "DILATASI WAKTU RELATIVISTIK EINSTEIN",
            "latex": "\\Delta t = \\gamma \\Delta t_0 = \\frac{\\Delta t_0}{\\sqrt{1 - (v/c)^2}} = 5{,}0 \\times 2{,}2\\,\\mu\\text{s} = 11\\,\\mu\\text{s}; \\quad s = v \\Delta t = (0{,}98c) \\times 11\\,\\mu\\text{s} = 3.234\\text{ m}",
            "legend": "• Tanpa efek relativitas khusus, muon hanya menempuh $s_{\\text{klasik}} = 0{,}98c \\times 2{,}2\\,\\mu\\text{s} \\approx 647\\text{ m}$ dan tidak akan pernah mencapai bumi<br>• Dilatasi waktu membuktikan kebenaran teori relativitas khusus Einstein"
        },
        "hints": {
            "concept": "Dilatasi waktu: Delta_t = gamma * Delta_t0 = 5 * 2,2 mikrodetik = 11 mikrodetik. Jarak tempuh di bumi: s = v * Delta_t = 0,98 * 3e8 * 11e-6 m.",
            "execution": "Delta_t = 11 mikrosekon. s = 2,94e8 * 1,1e-5 = 3.234 m = 3,234 km."
        }
    },
    {
        "id": "fis-lat-h-18",
        "materi": "RELATIVITAS KHUSUS (ENERGI & MOMENTUM)",
        "topic": "Relasi Kecepatan saat Energi Kinetik Sama dengan Energi Diam",
        "stem": "Sebuah partikel subatomik bermassa diam $m_0$ dipercepat hingga memiliki energi kinetik relativistik yang besarnya tepat sama dengan energi diamnya ($E_k = E_0 = m_0 c^2$). Kecepatan gerak partikel ($v$) dan momentum relativistiknya ($p$) dinyatakan dalam konstanta $m_0$ dan $c$ berturut-turut adalah...",
        "correct": "$v = \\frac{1}{2}\\sqrt{3}\\,c \\approx 0{,}866c$ dan $p = \\sqrt{3}\\,m_0 c$, karena energi total partikel adalah $E = E_k + E_0 = 2 E_0 = 2 m_0 c^2$. Karena $E = \\gamma E_0$, maka faktor Lorentz bernilai $\\gamma = 2 \\implies \\frac{1}{\\sqrt{1 - (v/c)^2}} = 2 \\implies 1 - (v/c)^2 = \\frac{1}{4} \\implies (v/c)^2 = \\frac{3}{4} \\implies v = \\frac{\\sqrt{3}}{2}c$. Dari relasi $E^2 = p^2 c^2 + E_0^2$, kita dapatkan $(2 E_0)^2 = p^2 c^2 + E_0^2 \\implies 4 E_0^2 - E_0^2 = p^2 c^2 \\implies p^2 c^2 = 3 E_0^2 \\implies p = \\sqrt{3}\\frac{E_0}{c} = \\sqrt{3} m_0 c$.",
        "distractors": [
            "$v = 0{,}5c$ dan $p = m_0 c$, karena kecepatan diasumsikan berbanding lurus linier dengan setengah faktor energi kinetik.",
            "$v = \\frac{1}{\\sqrt{2}}c \\approx 0{,}707c$ dan $p = 2 m_0 c$, dihitung dari persamaan mekanika Newtonian non-relativistik.",
            "$v = 0{,}98c$ dan $p = 3 m_0 c$, dihitung dari perkiraan kasar kecepatan tanpa penyelesaian aljabar Lorentz.",
            "$v = c$ dan $p = \\infty$, karena berasumsi partikel bermassa diam dapat dipercepat hingga mencapai kecepatan cahaya."
        ],
        "formula": {
            "title": "RELASI ENERGI-MOMENTUM RELATIVISTIK",
            "latex": "E = E_k + E_0 = 2 E_0 \\implies \\gamma = 2; \\quad v = c\\sqrt{1 - \\frac{1}{\\gamma^2}} = c\\sqrt{1 - \\frac{1}{4}} = \\frac{\\sqrt{3}}{2}c; \\quad p = \\frac{\\sqrt{E^2 - E_0^2}}{c} = \\sqrt{3} m_0 c",
            "legend": "• $\\gamma = 2$<br>• $v = \\frac{\\sqrt{3}}{2}c \\approx 0{,}866c$<br>• $p = \\sqrt{3} m_0 c \\approx 1{,}732 m_0 c$"
        },
        "hints": {
            "concept": "E = Ek + E0 = 2 E0, jadi gamma = 2. gamma = 1 / sqrt(1 - (v/c)^2) = 2 -> v = sqrt(3)/2 c. Momentum relativistik p = sqrt(E^2 - E0^2)/c = sqrt(4 - 1) E0/c = sqrt(3) m0 c.",
            "execution": "v = (sqrt(3)/2) * c = 0,866c. p = sqrt(3) * m0 * c."
        }
    },
    {
        "id": "fis-lat-h-19",
        "materi": "FISIKA INTI & RADIOAKTIVITAS",
        "topic": "Hukum Peluruhan Eksponensial dan Aktivitas Radiasi",
        "stem": "Suatu sampel zat radioaktif memiliki waktu paruh $T_{1/2} = 8\\text{ hari}$. Mula-mula sampel tersebut memiliki aktivitas radiasi $A_0 = 160\\text{ mCi}$ (miliCurie). Aktivitas radiasi sampel tersebut setelah meluruh selama 24 hari ($A_t$) dan persentase inti induk yang telah meluruh adalah...",
        "correct": "$A_t = 20\\text{ mCi}$ dan inti yang telah meluruh sebesar $87{,}5\\%$, karena jumlah periode waktu paruh yang terlewati adalah $n = \\frac{t}{T_{1/2}} = \\frac{24}{8} = 3$. Aktivitas radiasi yang tersisa adalah $A_t = A_0 \\left(\\frac{1}{2}\\right)^n = 160 \\times \\left(\\frac{1}{2}\\right)^3 = 160 \\times \\frac{1}{8} = 20\\text{ mCi}$. Bagian yang tersisa adalah $\\frac{1}{8} = 12{,}5\\%$, sehingga fraksi inti induk yang telah meluruh menjadi inti anak adalah $100\\% - 12{,}5\\% = 87{,}5\\%$.",
        "distractors": [
            "$A_t = 40\\text{ mCi}$ dan inti yang telah meluruh sebesar $75{,}0\\%$, karena hanya memperhitungkan 2 kali periode waktu paruh peluruhan.",
            "$A_t = 20\\text{ mCi}$ dan inti yang telah meluruh sebesar $12{,}5\\%$, karena tertukar antara persentase inti sisa dengan persentase inti yang meluruh.",
            "$A_t = 10\\text{ mCi}$ dan inti yang telah meluruh sebesar $93{,}75\\%$, dihitung dari 4 kali waktu paruh peluruhan zat radioaktif.",
            "$A_t = 53{,}3\\text{ mCi}$ dan inti yang telah meluruh sebesar $66{,}7\\%$, dihitung dari pengurangan linier bukan peluruhan eksponensial."
        ],
        "formula": {
            "title": "HUKUM PELURUHAN RADIOAKTIF",
            "latex": "n = \\frac{t}{T_{1/2}} = \\frac{24}{8} = 3; \\quad A_t = A_0 \\left(\\frac{1}{2}\\right)^3 = \\frac{160}{8} = 20\\text{ mCi}; \\quad \\%_{\\text{meluruh}} = (1 - 2^{-n}) \\times 100\\% = 87{,}5\\%",
            "legend": "• $A_t$ = Aktivitas radiasi sisa pada waktu $t$<br>• Inti meluruh = $100\\% - \\%_{\\text{sisa}} = 100\\% - 12{,}5\\% = 87{,}5\\%$"
        },
        "hints": {
            "concept": "Jumlah waktu paruh n = 24 / 8 = 3. Sisa aktivitas A = A0 * (1/2)^3 = 160 / 8 = 20 mCi. Persentase meluruh = (1 - 1/8) * 100% = 87,5%.",
            "execution": "A = 20 mCi. Persentase meluruh = 87,5%."
        }
    },
    {
        "id": "fis-lat-h-20",
        "materi": "FISIKA INTI & ENERGI REAKSI FISI",
        "topic": "Defek Massa dan Energi Reaksi Pembelahan Inti Nuklir",
        "stem": "Dalam sebuah reaktor nuklir, terjadi reaksi fisi inti Uranium-235 yang ditembak oleh neutron termal sesuai persamaan reaksi berikut:<br>$$\\text{n} + {}_{92}^{235}\\text{U} \\to {}_{56}^{141}\\text{Ba} + {}_{36}^{92}\\text{Kr} + 3\\,\\text{n} + Q$$<br>Diketahui massa masing-masing partikel:<br>• Massa ${}_{92}^{235}\\text{U} = 235{,}0439\\text{ sma}$<br>• Massa neutron $\\text{n} = 1{,}0087\\text{ sma}$<br>• Massa ${}_{56}^{141}\\text{Ba} = 140{,}9144\\text{ sma}$<br>• Massa ${}_{36}^{92}\\text{Kr} = 91{,}9262\\text{ sma}$<br>Jika $1\\text{ sma} \\approx 931{,}5\\text{ MeV}$, energi ($Q$) yang dibebaskan dalam setiap satu reaksi fisi uranium tersebut adalah...",
        "correct": "$Q \\approx 173{,}26\\text{ MeV}$, karena massa pereaksi (reaktan) adalah $m_{\\text{reaktan}} = m_U + m_n = 235{,}0439 + 1{,}0087 = 236{,}0526\\text{ sma}$. Massa produk adalah $m_{\\text{produk}} = m_{\\text{Ba}} + m_{\\text{Kr}} + 3 m_n = 140{,}9144 + 91{,}9262 + 3(1{,}0087) = 232{,}8406 + 3{,}0261 = 235{,}8667\\text{ sma}$. Defek massa reaksi adalah $\\Delta m = 236{,}0526 - 235{,}8667 = 0{,}1859\\text{ sma}$. Energi yang dibebaskan adalah $Q = \\Delta m \\times 931{,}5\\text{ MeV} = 0{,}1859 \\times 931{,}5 \\approx 173{,}17\\text{ MeV}$ (dalam rentang nilai standar fisi nuklir $\\approx 173 - 200\\text{ MeV}$).",
        "distractors": [
            "$Q \\approx 192{,}8\\text{ MeV}$, dihitung tanpa memperhitungkan massa 3 neutron hasil fisi di ruas kanan reaksi produk.",
            "$Q \\approx 931{,}5\\text{ MeV}$, karena menyamakan energi reaksi dengan tetapan konversi massa satu satuan massa atom.",
            "$Q \\approx 86{,}5\\text{ MeV}$, karena defek massa keliru dibagi dua saat perhitungan kesetaraan energi Einstein.",
            "$Q \\approx 12{,}4\\text{ MeV}$, dihitung dari selisih energi ikat per nukleon tanpa mengalikan jumlah total nukleon isotop uranium."
        ],
        "formula": {
            "title": "ENERGI REAKSI FISI NUKLIR (DEFEK MASSA)",
            "latex": "\\Delta m = [m_U + m_n] - [m_{\\text{Ba}} + m_{\\text{Kr}} + 3m_n] = m_U - m_{\\text{Ba}} - m_{\\text{Kr}} - 2m_n = 235{,}0439 - 140{,}9144 - 91{,}9262 - 2(1{,}0087) = 0{,}1859\\text{ sma}; \\quad Q = 0{,}1859 \\times 931{,}5 \\approx 173{,}17\\text{ MeV}",
            "legend": "• $\\Delta m$ positif $\\implies$ Reaksi bersifat eksotermik (membebaskan energi raksasa)<br>• Reaksi fisi berantai menghasilkan sumber daya pembangkit listrik tenaga nuklir (PLTN)"
        },
        "hints": {
            "concept": "Delta_m = massa sebelum reaksi - massa sesudah reaksi. Q = Delta_m * 931,5 MeV.",
            "execution": "Delta_m = 235,0439 + 1,0087 - (140,9144 + 91,9262 + 3*1,0087) = 0,1859 sma. Q = 0,1859 * 931,5 = 173,2 MeV."
        }
    },
    {
        "id": "fis-lat-h-21",
        "materi": "ELEKTROMAGNETISME (SELEKTOR KECEPATAN / WIEN FILTER)",
        "topic": "Gerak Lurus Muatan dalam Medan Silang E dan B",
        "stem": "Dalam sebuah alat spektrometer massa, partikel bermuatan $q = +3{,}2 \\times 10^{-19}\\text{ C}$ dilewatkan melalui pemilih kecepatan (velocity selector). Di dalam ruang tersebut bekerja medan listrik homogen $E = 2{,}4 \\times 10^4\\text{ V/m}$ dan medan magnetik homogen $B = 0{,}12\\text{ Tesla}$ yang saling tegak lurus satu sama lain dan tegak lurus arah datang partikel. Agar partikel dapat melintas lurus tanpa mengalami pembelokan sedikit pun, kelajuan partikel ($v$) tersebut harus bernilai...",
        "correct": "$v = 2{,}0 \\times 10^5\\text{ m/s}$, karena syarat lintasan lurus adalah gaya Lorentz listrik dan gaya Lorentz magnet saling meniadakan ($F_E = F_B \\implies q E = q v B$), sehingga kelajuan partikel harus tepat memenuhi perbandingan $v = \\frac{E}{B} = \\frac{2{,}4 \\times 10^4\\text{ V/m}}{0{,}12\\text{ T}} = 2{,}0 \\times 10^5\\text{ m/s}$.",
        "distractors": [
            "$v = 5{,}0 \\times 10^{-6}\\text{ m/s}$, karena formula rasio medan keliru dibalik menjadi medan magnet dibagi medan listrik ($B/E$).",
            "$v = 2{,}88 \\times 10^3\\text{ m/s}$, dihitung dari hasil perkalian langsung antara kuat medan listrik dengan medan magnet.",
            "$v = 1{,}0 \\times 10^6\\text{ m/s}$, dihitung dari pendekatan kecepatan elektron bebas pada tabung sinar katoda.",
            "$v = 3{,}0 \\times 10^8\\text{ m/s}$, karena partikel bermuatan diasumsikan otomatis merambat dengan kelajuan cahaya di ruang hampa."
        ],
        "formula": {
            "title": "PRINSIP PEMILIH KECEPATAN (VELOCITY SELECTOR)",
            "latex": "\\sum F = F_E - F_B = 0 \\implies qE = qvB \\implies v = \\frac{E}{B} = \\frac{2{,}4 \\times 10^4}{0{,}12} = 2{,}0 \\times 10^5\\text{ m/s}",
            "legend": "• $F_E = qE$ (Gaya Coulomb listrik)<br>• $F_B = qvB$ (Gaya Lorentz magnetik)<br>• Kelajuan $v = E/B$ tidak bergantung pada massa partikel maupun besar muatan partikel"
        },
        "hints": {
            "concept": "Lintasan lurus terjadi saat gaya listrik sama dengan gaya magnet: q * E = q * v * B. Maka v = E / B.",
            "execution": "v = 2,4e4 / 0,12 = 2,0 x 10^5 m/s."
        }
    },
    {
        "id": "fis-lat-h-22",
        "materi": "ELEKTROSTATIKA (ENERGI POTENSIAL SISTEM MUATAN)",
        "topic": "Energi Potensial Tiga Muatan di Segitiga Sama Sisi",
        "stem": "Tiga buah muatan titik identik masing-masing sebesar $q_1 = q_2 = q_3 = +2\\,\\mu\\text{C} = 2 \\times 10^{-6}\\text{ C}$ ditempatkan pada ketiga titik sudut sebuah segitiga sama sisi yang memiliki panjang sisi $s = 30\\text{ cm} = 0{,}3\\text{ meter}$. Diketahui konstanta Coulomb $k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2$. Total energi potensial elektrostatik ($U_{\\text{total}}$) yang tersimpan dalam sistem tiga muatan tersebut adalah...",
        "correct": "$U_{\\text{total}} = 0{,}36\\text{ Joule}$, karena energi potensial total sistem adalah penjumlahan skalar dari energi potensial ketiga pasangan muatan: $U = U_{12} + U_{13} + U_{23} = 3 \\left(\\frac{k q^2}{s}\\right) = 3 \\times \\frac{(9 \\times 10^9) \\times (2 \\times 10^{-6})^2}{0{,}3} = 3 \\times \\frac{9 \\times 10^9 \\times 4 \\times 10^{-12}}{0{,}3} = 3 \\times \\frac{0{,}036}{0{,}3} = 3 \\times 0{,}12 = 0{,}36\\text{ Joule}$.",
        "distractors": [
            "$U_{\\text{total}} = 0{,}12\\text{ Joule}$, karena hanya memperhitungkan interaksi satu pasang muatan tunggal dalam sistem.",
            "$U_{\\text{total}} = 0{,}72\\text{ Joule}$, dihitung dari penggandaan pasangan muatan dengan menghitung interaksi timbal balik dua kali.",
            "$U_{\\text{total}} = 0\\text{ Joule}$, karena keliru menganggap energi potensial sebagai besaran vektor yang saling meniadakan di pusat segitiga.",
            "$U_{\\text{total}} = 1{,}08\\text{ Joule}$, dihitung dari perkalian tiga pasang muatan dengan kuadrat jarak sisi pemisah segitiga."
        ],
        "formula": {
            "title": "ENERGI POTENSIAL ELEKTROSTATIK SISTEM DISKRIT",
            "latex": "U_{\\text{total}} = \\sum_{i < j} \\frac{k q_i q_j}{r_{ij}} = 3 \\times \\frac{k q^2}{s} = 3 \\times \\frac{9 \\times 10^9 \\times (2 \\times 10^{-6})^2}{0{,}3} = 3 \\times 0{,}12 = 0{,}36\\text{ J}",
            "legend": "• Energi potensial adalah besaran skalar (bukan vektor)<br>• Terdapat 3 pasangan muatan pada segitiga: $(1,2)$, $(1,3)$, dan $(2,3)$<br>• $U_{\\text{total}} = 0{,}36\\text{ Joule}$"
        },
        "hints": {
            "concept": "Energi potensial elektrostatik sistem adalah jumlah skalar energi setiap pasangan: U_total = U12 + U23 + U13 = 3 * (k * q^2 / s).",
            "execution": "U_total = 3 * (9e9 * (2e-6)^2 / 0,3) = 3 * (0,036 / 0,3) = 3 * 0,12 = 0,36 J."
        }
    },
    {
        "id": "fis-lat-h-23",
        "materi": "KAPASITOR & BAHAN DIELEKTRIK",
        "topic": "Kapasitor Keping Sejajar dengan Dua Lapisan Dielektrik Seri",
        "stem": "Sebuah kapasitor keping sejajar dengan luas keping $A$ dan jarak antar keping $d$ mula-mula memiliki kapasitansi ruang hampa $C_0 = 12\\,\\mu\\text{F}$. Ruang di antara kedua keping kemudian diisi penuh oleh dua lapisan bahan dielektrik yang masing-masing memiliki ketebalan separuh jarak antar keping ($d_1 = d_2 = \\frac{1}{2}d$). Lapisan pertama memiliki konstanta dielektrik $\\kappa_1 = 2$ dan lapisan kedua $\\kappa_2 = 6$. Nilai kapasitas kapasitor setelah disisipi kedua dielektrik tersebut ($C_{\\text{gab}}$) adalah...",
        "correct": "$C_{\\text{gab}} = 36\\,\\mu\\text{F}$, karena susunan dielektrik berlapis tegak lurus garis medan membentuk dua kapasitor yang terhubung secara seri dengan jarak keping masing-masing $\\frac{1}{2}d$. Kapasitansi masing-masing adalah $C_1 = \\kappa_1 \\left(\\frac{\\varepsilon_0 A}{d/2}\\right) = 2 \\kappa_1 C_0 = 2(2)(12) = 48\\,\\mu\\text{F}$, dan $C_2 = 2 \\kappa_2 C_0 = 2(6)(12) = 144\\,\\mu\\text{F}$. Kapasitansi gabungan seri adalah $C_{\\text{gab}} = \\frac{C_1 C_2}{C_1 + C_2} = \\frac{48 \\times 144}{48 + 144} = \\frac{6.912}{192} = 36\\,\\mu\\text{F}$.",
        "distractors": [
            "$C_{\\text{gab}} = 48\\,\\mu\\text{F}$, dihitung dari rata-rata aritmetika konstanta dielektrik dikalikan dengan kapasitansi awal.",
            "$C_{\\text{gab}} = 96\\,\\mu\\text{F}$, karena kedua lapisan dielektrik keliru dihitung sebagai susunan kapasitor paralel.",
            "$C_{\\text{gab}} = 24\\,\\mu\\text{F}$, dihitung tanpa memperhitungkan reduksi separuh ketebalan keping masing-masing dielektrik.",
            "$C_{\\text{gab}} = 18\\,\\mu\\text{F}$, dihitung dari perkalian terbalik konstanta dielektrik terhadap permitivitas ruang hampa."
        ],
        "formula": {
            "title": "KAPASITANSI GABUNGAN DIELEKTRIK BERLAPIS (SERI)",
            "latex": "C_1 = 2\\kappa_1 C_0 = 48\\,\\mu\\text{F}; \\quad C_2 = 2\\kappa_2 C_0 = 144\\,\\mu\\text{F}; \\quad \\frac{1}{C_{\\text{gab}}} = \\frac{1}{C_1} + \\frac{1}{C_2} \\implies C_{\\text{gab}} = \\frac{48 \\times 144}{192} = 36\\,\\mu\\text{F}",
            "legend": "• Tebal masing-masing lapisan $d/2 \\implies$ kapasitansi dasar menjadi $2 C_0$<br>• Dielektrik tersusun seri: $\\kappa_{\\text{eff}} = \\frac{2 \\kappa_1 \\kappa_2}{\\kappa_1 + \\kappa_2} = \\frac{2 \\times 2 \\times 6}{2 + 6} = \\frac{24}{8} = 3$<br>• $C_{\\text{gab}} = \\kappa_{\\text{eff}} C_0 = 3 \\times 12 = 36\\,\\mu\\text{F}$"
        },
        "hints": {
            "concept": "Dua lapisan dielektrik yang membagi jarak d menjadi d/2 tersusun seri. Konstanta dielektrik efektif seri: kappa_eff = 2*k1*k2 / (k1 + k2). C_gab = kappa_eff * C0.",
            "execution": "kappa_eff = 2 * 2 * 6 / (2 + 6) = 24 / 8 = 3. C_gab = 3 * 12 mikrofarad = 36 mikrofarad."
        }
    },
    {
        "id": "fis-lat-h-24",
        "materi": "FISIKA MODERN (DIFRAKSI SINAR-X / HUKUM BRAGG)",
        "topic": "Hukum Difraksi Bragg pada Kisi Kristal Padat",
        "stem": "Berkas sinar-X monokromatik dengan panjang gelombang $\\lambda = 0{,}15\\text{ nm}$ ($1{,}5 \\times 10^{-10}\\text{ m}$) dijatuhkan pada permukaan kristal garam dapur (NaCl) yang memiliki jarak antarbidang kisi atom $d = 0{,}30\\text{ nm}$. Berdasarkan Hukum Difraksi Bragg ($2d \\sin\\theta = n\\lambda$), sudut berkas gelombang terhadap bidang kisi kristal (sudut Bragg $\\theta$) yang menghasilkan puncak difraksi interferensi konstruktif orde pertama ($n = 1$) adalah...",
        "correct": "$\\theta = 14{,}48^\\circ$ (karena $\\sin\\theta = 0{,}25$), dihitung dari persamaan Bragg $2d \\sin\\theta = n\\lambda$, sehingga $\\sin\\theta = \\frac{n\\lambda}{2d} = \\frac{1 \\times 0{,}15\\text{ nm}}{2 \\times 0{,}30\\text{ nm}} = \\frac{0{,}15}{0{,}60} = 0{,}25$, yang bersesuaian dengan sudut $\\theta = \\arcsin(0{,}25) \\approx 14{,}48^\\circ$.",
        "distractors": [
            "$\\theta = 30{,}0^\\circ$, karena angka 2 di depan jarak antarbidang kristal pada Hukum Bragg diabaikan ($\\sin\\theta = \\lambda/d = 0{,}5$).",
            "$\\theta = 60{,}0^\\circ$, karena keliru menggunakan nilai fungsi cosinus dari perbandingan panjang gelombang.",
            "$\\theta = 45{,}0^\\circ$, dihitung dari asumsi bahwa difraksi kisi kristal selalu simetris pada sudut separuh siku-siku.",
            "$\\theta = 7{,}24^\\circ$, dihitung dari pembagian sudut Bragg dengan orde difraksi kuantum kedua."
        ],
        "formula": {
            "title": "HUKUM DIFRAKSI BRAGG PADA KRISTAL",
            "latex": "2d \\sin\\theta = n\\lambda \\implies \\sin\\theta = \\frac{n\\lambda}{2d} = \\frac{1 \\times 0{,}15}{2 \\times 0{,}30} = 0{,}25 \\implies \\theta = \\arcsin(0{,}25) \\approx 14{,}48^\\circ",
            "legend": "• $d = 0{,}30\\text{ nm}$ (jarak antarbidang kristal)<br>• $\\theta$ diukur terhadap bidang pantul kisi kristal (bukan terhadap garis normal permukaan)"
        },
        "hints": {
            "concept": "Hukum Bragg: 2 * d * sin(theta) = n * lambda. Untuk n = 1: sin(theta) = lambda / (2d).",
            "execution": "sin(theta) = 0,15 / (2 * 0,30) = 0,15 / 0,60 = 0,25. theta = arcsin(0,25) = 14,48 derajat."
        }
    },
    {
        "id": "fis-lat-h-25",
        "materi": "TERMODINAMIKA GAS IDEAL (PROSES ADIABATIK)",
        "topic": "Tekanan dan Volume pada Pemuaian Adiabatik Gas Diatomik",
        "stem": "Sejumlah gas ideal diatomik (tetapan Laplace $\\gamma = 1{,}4 = \\frac{7}{5}$) mula-mula berada pada tekanan $P_1 = 3{,}2 \\times 10^5\\text{ Pa}$ dan volume $V_1 = 1\\text{ liter}$. Gas tersebut mengalami ekspansi adiabatik kuasistatik hingga volumenya membesar menjadi $V_2 = 32\\text{ liter}$. Mengingat relasi pemangkatan $32^{1{,}4} = (2^5)^{7/5} = 2^7 = 128$, besar tekanan akhir gas ($P_2$) setelah proses ekspansi adiabatik tersebut adalah...",
        "correct": "$P_2 = 2{,}5 \\times 10^3\\text{ Pa}$ (atau $2.500\\text{ Pa}$), karena pada proses adiabatik berlaku hukum Poisson $P_1 V_1^\\gamma = P_2 V_2^\\gamma$, sehingga $P_2 = P_1 \\left(\\frac{V_1}{V_2}\\right)^\\gamma = (3{,}2 \\times 10^5\\text{ Pa}) \\times \\left(\\frac{1}{32}\\right)^{1{,}4} = \\frac{3{,}2 \\times 10^5}{128} = 2.500\\text{ Pa} = 2{,}5 \\times 10^3\\text{ Pa}$.",
        "distractors": [
            "$P_2 = 1{,}0 \\times 10^4\\text{ Pa}$, karena gas keliru dihitung memuai secara isotermal menurut hukum Boyle ($P_1 V_1 = P_2 V_2$).",
            "$P_2 = 5{,}0 \\times 10^3\\text{ Pa}$, dihitung dengan menggunakan tetapan gas monoatomik gamma lima per tiga.",
            "$P_2 = 1{,}28 \\times 10^5\\text{ Pa}$, dihitung dari perkalian tekanan awal dengan faktor pemuaian volume gas.",
            "$P_2 = 8{,}0 \\times 10^2\\text{ Pa}$, dihitung dari pembagian tekanan gas terhadap kuadrat perubahan volume adiabatik."
        ],
        "formula": {
            "title": "PERSAMAAN PROSES ADIABATIK (HUKUM POISSON)",
            "latex": "P_1 V_1^\\gamma = P_2 V_2^\\gamma \\implies P_2 = P_1 \\left(\\frac{V_1}{V_2}\\right)^\\gamma = 3{,}2 \\times 10^5 \\times \\left(\\frac{1}{32}\\right)^{7/5} = \\frac{320.000}{128} = 2.500\\text{ Pa}",
            "legend": "• $\\gamma = \\frac{C_p}{C_v} = 1{,}4 = \\frac{7}{5}$ (Gas diatomik)<br>• $32^{7/5} = (2^5)^{7/5} = 2^7 = 128$<br>• Pada ekspansi adiabatik, tekanan gas turun drastis jauh lebih cepat daripada proses isotermal"
        },
        "hints": {
            "concept": "Proses adiabatik memenuhi P1 * V1^gamma = P2 * V2^gamma. P2 = P1 * (V1 / V2)^gamma. Hitung (1/32)^1,4 = 1 / 128.",
            "execution": "P2 = 3,2e5 / 128 = 2.500 Pa = 2,5 x 10^3 Pa."
        }
    }
]
