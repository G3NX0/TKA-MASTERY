# -*- coding: utf-8 -*-
"""
mtk_lanjut_data_simulasi.py
---------------------------
35 Authentic Simulasi items for TKA 2026 Matematika Tingkat Lanjut (SMA/MA Fase F Lanjutan).
- 25 Multiple Choice Questions (mtk_lanjut-sim-01 .. sim-25)
- 5 Multi-Select Questions (mtk_lanjut-sim-26 .. sim-30)
- 5 Matrix Benar-Salah Questions (mtk_lanjut-sim-31 .. sim-35)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework.
"""

MTK_LANJUT_SIMULASI_ITEMS = [
    # 25 MCQs
    {
        "id": "mtk_lanjut-sim-01",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Lintasan Satelit Berbentuk Elips (Hukum Kepler)",
        "stem": "Sebuah satelit buatan mengorbit bumi mengikuti lintasan elips dengan pusat bumi di salah satu titik fokusnya. Persamaan lintasan orbit satelit diberikan oleh $\\frac{x^2}{100} + \\frac{y^2}{64} = 1$ (dalam ribuan kilometer). Jarak terdekat (perigee) dan jarak terjauh (apogee) satelit ke pusat bumi berturut-turut adalah...",
        "correct": "$4.000\\text{ km}$ dan $16.000\\text{ km}$",
        "distractors": [
            "$2.000\\text{ km}$ dan $18.000\\text{ km}$",
            "$6.000\\text{ km}$ dan $14.000\\text{ km}$",
            "$8.000\\text{ km}$ dan $12.000\\text{ km}$",
            "$4.000\\text{ km}$ dan $10.000\\text{ km}$"
        ],
        "formula": {
            "title": "PARAMETER ORBIT ELIPS KEPLER",
            "latex": "r_{\\min} = a - c, \\quad r_{\\max} = a + c \\quad \\text{dengan } c = \\sqrt{a^2 - b^2}",
            "legend": "• $a = \\sqrt{100} = 10$, $b = \\sqrt{64} = 8$<br>• $c = \\sqrt{100 - 64} = \\sqrt{36} = 6$ (dalam ribuan km)"
        },
        "hints": {
            "concept": "Hitung jarak fokus $c = \\sqrt{a^2 - b^2} = \\sqrt{100 - 64} = 6$.",
            "execution": "Perigee $= a - c = 10 - 6 = 4$ ribu km ($4.000$ km). Apogee $= a + c = 10 + 6 = 16$ ribu km ($16.000$ km)."
        }
    },
    {
        "id": "mtk_lanjut-sim-02",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Model Pertumbuhan Populasi Spesies Tertentu",
        "stem": "Dinamika laju pertumbuhan biomassa alga kultur dimodelkan dengan fungsi polinomial $P(t) = t^3 - 9t^2 + 24t + 10$ untuk interval waktu $0 \\le t \\le 6$ hari. Waktu $t$ saat laju pertambahan biomassa mencapai nilai minimum lokal adalah pada hari ke-...",
        "correct": "$4$",
        "distractors": [
            "$2$",
            "$3$",
            "$5$",
            "$6$"
        ],
        "formula": {
            "title": "ANALISIS TITIK STASIONER EKSTREM LOKAL",
            "latex": "P'(t) = 3t^2 - 18t + 24 = 0 \\implies 3(t - 2)(t - 4) = 0",
            "legend": "• Titik stasioner $t = 2$ (maksimum lokal) dan $t = 4$ (minimum lokal)"
        },
        "hints": {
            "concept": "Cari turunan pertama $P'(t) = 3t^2 - 18t + 24 = 0 \\implies t^2 - 6t + 8 = 0 \\implies (t - 2)(t - 4) = 0$.",
            "execution": "Uji turunan kedua: $P''(t) = 6t - 18$. Pada $t = 4$: $P''(4) = 6(4) - 18 = 6 > 0$ (cekung ke atas, titik minimum lokal)."
        }
    },
    {
        "id": "mtk_lanjut-sim-03",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Resultan Gaya Spasial pada Konstruksi Menara Transmisi",
        "stem": "Tiga buah kawat penopang menara memberikan tarikan gaya ke tiga arah spasial: $\\vec{F}_1 = 20\\hat{i} - 10\\hat{j} + 40\\hat{k}$, $\\vec{F}_2 = -15\\hat{i} + 30\\hat{j} + 50\\hat{k}$, dan $\\vec{F}_3 = -5\\hat{i} - 20\\hat{j} + 30\\hat{k}$ (dalam Newton). Besar resultan gaya total yang dialami menara transmisi adalah...",
        "correct": "$120 \\text{ N}$",
        "distractors": [
            "$100 \\text{ N}$",
            "$140 \\text{ N}$",
            "$150 \\text{ N}$",
            "$160 \\text{ N}$"
        ],
        "formula": {
            "title": "RESULTAN VEKTOR TIGA DIMENSI",
            "latex": "\\vec{F}_R = \\sum \\vec{F} = \\left(\\sum F_x\\right)\\hat{i} + \\left(\\sum F_y\\right)\\hat{j} + \\left(\\sum F_z\\right)\\hat{k}",
            "legend": "• Modulus gaya resultan: $|\\vec{F}_R| = \\sqrt{F_{Rx}^2 + F_{Ry}^2 + F_{Rz}^2}$"
        },
        "hints": {
            "concept": "Jumlahkan komponen: $F_x = 20 - 15 - 5 = 0$, $F_y = -10 + 30 - 20 = 0$, $F_z = 40 + 50 + 30 = 120$.",
            "execution": "Resultan vektor: $\\vec{F}_R = 0\\hat{i} + 0\\hat{j} + 120\\hat{k}$. Besarnya adalah $\\sqrt{0^2 + 0^2 + 120^2} = 120$ N."
        }
    },
    {
        "id": "mtk_lanjut-sim-04",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Transformasi Linear Matriks Refleksi dan Rotasi",
        "stem": "Sebuah titik $P(2, 3)$ ditransformasikan oleh matriks refleksi terhadap sumbu-$x$ dilanjutkan dengan rotasi $90^\\circ$ berlawanan arah jarum jam berpusat di $(0,0)$. Koordinat akhir bayangan titik $P$ adalah...",
        "correct": "$(3, 2)$",
        "distractors": [
            "$(-3, 2)$",
            "$(3, -2)$",
            "$(-2, 3)$",
            "$(-3, -2)$"
        ],
        "formula": {
            "title": "KOMPOSISI TRANSFORMASI MATRIKS",
            "latex": "M = R_{90^\\circ} \\cdot M_x = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix} = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}",
            "legend": "• Komposisi menghasilkan matriks refleksi terhadap garis $y = x$"
        },
        "hints": {
            "concept": "Refleksi sumbu-$x$: $(x, y) \\to (x, -y)$. Rotasi $90^\\circ$: $(x', y') \\to (-y', x')$.",
            "execution": "Dari $(2, 3) \\to (2, -3) \\to (-(-3), 2) = (3, 2)$."
        }
    },
    {
        "id": "mtk_lanjut-sim-05",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Tegangan Listrik Bolak-balik (AC)",
        "stem": "Tegangan bolak-balik dari generator listrik memenuhi persamaan $V(t) = 220\\sqrt{2} \\sin(100\\pi t - \\frac{\\pi}{3})$ volt. Nilai tegangan sesaat pada waktu $t = \\frac{1}{200}$ detik adalah...",
        "correct": "$110\\sqrt{2} \\text{ volt}$",
        "distractors": [
            "$110\\sqrt{6} \\text{ volt}$",
            "$220 \\text{ volt}$",
            "$0 \\text{ volt}$",
            "$220\\sqrt{2} \\text{ volt}$"
        ],
        "formula": {
            "title": "PERSAMAAN GELOMBANG TEGANGAN AC",
            "latex": "V(t) = V_{\\max} \\sin(\\omega t + \\phi)",
            "legend": "• Menghitung nilai magnitudo tegangan sesaat berdasarkan fase gelombang sinus"
        },
        "hints": {
            "concept": "Hitung sudut fase: $\\theta = 100\\pi \\left(\\frac{1}{200}\\right) - \\frac{\\pi}{3} = \\frac{\\pi}{2} - \\frac{\\pi}{3} = \\frac{\\pi}{6}$.",
            "execution": "Tegangan: $V = 220\\sqrt{2} \\sin\\left(\\frac{\\pi}{6}\\right) = 220\\sqrt{2} \\left(\\frac{1}{2}\\right) = 110\\sqrt{2}$ volt."
        }
    },
    {
        "id": "mtk_lanjut-sim-06",
        "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
        "topic": "Kecepatan Sesaat Partikel Menggunakan Limit Diferensial",
        "stem": "Posisi sebuah partikel bergerak memenuhi persamaan $s(t) = \\frac{1 - \\cos(6t)}{t}$ untuk $t > 0$. Kecepatan awal partikel saat $t \\to 0$ ($\lim_{t \\to 0} s'(t)$ atau limit bentuk posisi) diperoleh dari $\\lim_{t \\to 0} \\frac{1 - \\cos(6t)}{t^2}$ yang bernilai...",
        "correct": "$18$",
        "distractors": [
            "$6$",
            "$12$",
            "$36$",
            "$9$"
        ],
        "formula": {
            "title": "LIMIT KECEPATAN SESAAT",
            "latex": "\\lim_{t \\to 0} \\frac{1 - \\cos(kt)}{t^2} = \\frac{k^2}{2}",
            "legend": "• $k = 6 \\implies \\frac{6^2}{2} = \\frac{36}{2} = 18$"
        },
        "hints": {
            "concept": "Gunakan formula limit khusus: $\\lim_{t \\to 0} \\frac{1 - \\cos(kt)}{t^2} = \\frac{k^2}{2}$.",
            "execution": "Dengan $k = 6$, perhitungannya adalah $\\frac{6^2}{2} = \\frac{36}{2} = 18$."
        }
    },
    {
        "id": "mtk_lanjut-sim-07",
        "materi": "KALKULUS LANJUT: TURUNAN APLIKASI",
        "topic": "Desain Talang Air Kapasitas Maksimum",
        "stem": "Sebuah lembaran seng selebar $30\\text{ cm}$ ditekuk kedua sisinya masing-masing selebar $10\\text{ cm}$ dengan sudut kemiringan $\\theta$ terhadap dasar horizontal membentuk talang air trapesium. Kapasitas aliran maksimum dicapai saat sudut tekukan $\\theta$ bernilai...",
        "correct": "$60^\\circ$",
        "distractors": [
            "$30^\\circ$",
            "$45^\\circ$",
            "$75^\\circ$",
            "$90^\\circ$"
        ],
        "formula": {
            "title": "OPTIMASI PENAMPANG TALANG TRAPESIUM",
            "latex": "L(\\theta) = (10 + 10\\cos\\theta)(10\\sin\\theta) = 100\\sin\\theta(1 + \\cos\\theta)",
            "legend": "• Luas penampang maksimum dicapai saat $2\\cos^2\\theta + \\cos\\theta - 1 = 0 \\implies \\cos\\theta = \\frac{1}{2}$"
        },
        "hints": {
            "concept": "Turunan pertama fungsi luas penampang terhadap sudut kemiringan disamakan dengan nol.",
            "execution": "$L'(\\theta) = 100(\\cos\\theta + \\cos(2\\theta)) = 0 \\implies \\cos(2\\theta) = -\\cos\\theta = \\cos(180^\\circ - \\theta) \\implies \\theta = 60^\\circ$."
        }
    },
    {
        "id": "mtk_lanjut-sim-08",
        "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
        "topic": "Volume Reservoir Tangki Paraboloid",
        "stem": "Sebuah tangki penampung air berbentuk paraboloid terbentuk dari perputaran kurva $y = 2x^2$ dari $y = 0$ hingga $y = 8$ mengelilingi sumbu-$y$ (dalam meter). Volume kapasitas total tangki air tersebut adalah...",
        "correct": "$16\\pi \\text{ m}^3$",
        "distractors": [
            "$8\\pi \\text{ m}^3$",
            "$32\\pi \\text{ m}^3$",
            "$\\frac{32}{3}\\pi \\text{ m}^3$",
            "$64\\pi \\text{ m}^3$"
        ],
        "formula": {
            "title": "VOLUME BENDA PUTAR TERHADAP SUMBU-Y",
            "latex": "V = \\pi \\int_c^d [g(y)]^2 \\, dy = \\pi \\int_0^8 \\frac{y}{2} \\, dy",
            "legend": "• Dari $y = 2x^2 \\implies x^2 = \\frac{y}{2}$"
        },
        "hints": {
            "concept": "Nyatakan $x^2$ dalam $y$: $x^2 = \\frac{y}{2}$. Batas integrasi $y = 0$ sampai $y = 8$.",
            "execution": "Hitung $V = \\pi \\int_0^8 \\frac{y}{2} \\, dy = \\pi \\left[ \\frac{y^2}{4} \\right]_0^8 = \\pi \\left(\\frac{64}{4}\\right) = 16\\pi \\text{ m}^3$."
        }
    },
    {
        "id": "mtk_lanjut-sim-09",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Garis Singgung Parabola Bergradien pada Reflektor Radar",
        "stem": "Sebuah antena parabola penangkap sinyal satelit dirancang memenuhi persamaan $y^2 = 16x$. Sinar sinyal datang paralel dengan gradien $m = 1$. Persamaan garis singgung permukaan parabola di titik pantul tersebut adalah...",
        "correct": "$y = x + 4$",
        "distractors": [
            "$y = x - 4$",
            "$y = x + 2$",
            "$y = x + 8$",
            "$y = 2x + 4$"
        ],
        "formula": {
            "title": "GARIS SINGGUNG PARABOLA HORIZONTAL",
            "latex": "y = mx + \\frac{p}{m} \\quad \\text{dengan } 4p = 16 \\implies p = 4",
            "legend": "• Karakteristik refleksi optik parabola memusatkan seluruh sinar paralel ke titik fokus"
        },
        "hints": {
            "concept": "Dari persamaan $y^2 = 16x$, nilai $4p = 16 \\implies p = 4$. Gradien $m = 1$.",
            "execution": "Persamaan garis singgung: $y = (1)x + \\frac{4}{1} = x + 4$."
        }
    },
    {
        "id": "mtk_lanjut-sim-10",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Sisa Pembagian Polinomial dengan Pembagi Kompleks Rasional",
        "stem": "Sebuah suku banyak $P(x)$ memiliki derajat 4. Jika $P(x)$ dibagi oleh $(x^2 - 4)$ memberikan sisa $(3x - 1)$, maka nilai dari $P(2) + P(-2)$ adalah...",
        "correct": "$-2$",
        "distractors": [
            "$4$",
            "$5$",
            "$-7$",
            "$10$"
        ],
        "formula": {
            "title": "EVALUASI SISA POLINOMIAL DARI FAKTOR PEMBAGI",
            "latex": "P(x) = (x^2 - 4)H(x) + S(x) \\implies P(c) = S(c) \\quad (\\text{saat } c^2 - 4 = 0)",
            "legend": "• Nilai $P(2) = S(2)$ dan $P(-2) = S(-2)$"
        },
        "hints": {
            "concept": "Sisa pembagian $S(x) = 3x - 1$. Karena pembuat nol $(x^2 - 4)$ adalah $x = 2$ dan $x = -2$.",
            "execution": "$P(2) = 3(2) - 1 = 5$ dan $P(-2) = 3(-2) - 1 = -7$. Jumlahkan: $5 + (-7) = -2$."
        }
    },
    {
        "id": "mtk_lanjut-sim-11",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Luas Segitiga di Ruang Tiga Dimensi Menggunakan Cross Product",
        "stem": "Titik-titik sudut sebuah segitiga di ruang $\\mathbb{R}^3$ adalah $A(1, 0, 0)$, $B(0, 2, 0)$, dan $C(0, 0, 3)$. Luas segitiga $ABC$ tersebut adalah...",
        "correct": "$\\frac{7}{2} \\text{ satuan luas}$",
        "distractors": [
            "$3 \\text{ satuan luas}$",
            "$7 \\text{ satuan luas}$",
            "$\\sqrt{14} \\text{ satuan luas}$",
            "$\\frac{\\sqrt{13}}{2} \\text{ satuan luas}$"
        ],
        "formula": {
            "title": "LUAS SEGITIGA VEKTOR RUANG",
            "latex": "L = \\frac{1}{2} |\\vec{AB} \\times \\vec{AC}|",
            "legend": "• Menghitung setengah luas jajar genjang yang dibentuk oleh kedua vektor sisi"
        },
        "hints": {
            "concept": "Vektor sisi: $\\vec{AB} = \\langle -1, 2, 0 \\rangle$ dan $\\vec{AC} = \\langle -1, 0, 3 \\rangle$.",
            "execution": "$\\vec{AB} \\times \\vec{AC} = \\hat{i}(6) - \\hat{j}(-3) + \\hat{k}(2) = 6\\hat{i} + 3\\hat{j} + 2\\hat{k}$. Magnitudo: $\\sqrt{36 + 9 + 4} = \\sqrt{49} = 7$. Luas $= \\frac{1}{2}(7) = \\frac{7}{2}$."
        }
    },
    {
        "id": "mtk_lanjut-sim-12",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Penyelesaian Persamaan a cos x + b sin x = c",
        "stem": "Nilai $x$ pada selang $0 \\le x \\le 2\\pi$ yang memenuhi persamaan $\\cos x + \\sqrt{3}\\sin x = 2$ adalah...",
        "correct": "$\\frac{\\pi}{3}$",
        "distractors": [
            "$\\frac{\\pi}{6}$",
            "$\\frac{2\\pi}{3}$",
            "$\\frac{5\\pi}{6}$",
            "$\\frac{4\\pi}{3}$"
        ],
        "formula": {
            "title": "BENTUK KHUSUS GELOMBANG MAKSIMUM",
            "latex": "k = \\sqrt{1^2 + (\\sqrt{3})^2} = 2 \\implies 2\\cos\\left(x - \\frac{\\pi}{3}\\right) = 2",
            "legend": "• Amplitudo maksimum tercapai saat fungsi kosinus bernilai tepat sama dengan satu"
        },
        "hints": {
            "concept": "Ubah menjadi $2\\cos(x - \\frac{\\pi}{3}) = 2 \\implies \\cos(x - \\frac{\\pi}{3}) = 1$.",
            "execution": "Sudut kosinus bernilai 1 saat sudutnya $0$: $x - \\frac{\\pi}{3} = 0 \\implies x = \\frac{\\pi}{3}$."
        }
    },
    {
        "id": "mtk_lanjut-sim-13",
        "materi": "KALKULUS LANJUT: TURUNAN IMPLISIT",
        "topic": "Garis Normal Kurva Tertutup",
        "stem": "Garis normal kurva $x^2 + 2y^2 = 9$ di titik $P(1, 2)$ memiliki persamaan...",
        "correct": "$4x - y - 2 = 0$",
        "distractors": [
            "$x + 4y - 9 = 0$",
            "$4x + y - 6 = 0$",
            "$2x - y = 0$",
            "$x - 4y + 7 = 0$"
        ],
        "formula": {
            "title": "PERSAMAAN GARIS NORMAL KURVA",
            "latex": "m_n = -\\frac{1}{m_s} \\implies y - y_1 = m_n(x - x_1)",
            "legend": "• Garis normal tegak lurus sempurna terhadap garis singgung di titik singgung yang sama"
        },
        "hints": {
            "concept": "Turunan implisit: $2x + 4y y' = 0 \\implies y' = -\\frac{x}{2y}$. Di $(1, 2)$, gradien singgung $m_s = -\\frac{1}{4}$.",
            "execution": "Gradien normal $m_n = 4$. Persamaan garis normal: $y - 2 = 4(x - 1) \\implies y - 2 = 4x - 4 \\implies 4x - y - 2 = 0$."
        }
    },
    {
        "id": "mtk_lanjut-sim-14",
        "materi": "KALKULUS LANJUT: INTEGRAL SUBSTITUSI TRIGONOMETRI",
        "topic": "Luas Lingkaran Menggunakan Substitusi Trigonometri",
        "stem": "Nilai dari integral tentu $\\int_0^2 \\sqrt{4 - x^2} \\, dx$ adalah...",
        "correct": "$\\pi$",
        "distractors": [
            "$\\frac{\\pi}{2}$",
            "$2\\pi$",
            "$4\\pi$",
            "$4$"
        ],
        "formula": {
            "title": "INTEGRAL GEOMETRIS SEPEREMPAT LINGKARAN",
            "latex": "\\int_0^r \\sqrt{r^2 - x^2} \\, dx = \\frac{1}{4}\\pi r^2",
            "legend": "• Merepresentasikan seperempat luas daerah lingkaran berjari-jari $r = 2$"
        },
        "hints": {
            "concept": "Secara geometris, ini adalah seperempat luas lingkaran berjari-jari $r = 2$.",
            "execution": "Luas seperempat lingkaran: $\\frac{1}{4} \\pi r^2 = \\frac{1}{4} \\pi (2^2) = \\pi$."
        }
    },
    {
        "id": "mtk_lanjut-sim-15",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Polinomial Pembagi Derajat Tiga",
        "stem": "Suku banyak $P(x) = x^5 - 1$ dibagi oleh $(x^2 - 1)$. Sisa pembagiannya adalah...",
        "correct": "$x - 1$",
        "distractors": [
            "$x + 1$",
            "$2x - 1$",
            "$-x + 1$",
            "$0$"
        ],
        "formula": {
            "title": "REDUKSI PANGKAT PEMBAGI KUADRATIK",
            "latex": "x^2 \\equiv 1 \\pmod{x^2 - 1} \\implies x^5 = (x^2)^2 \\cdot x \\equiv 1^2 \\cdot x = x",
            "legend": "• Teknik kongruensi aljabar cepat untuk mencari sisa pembagian suku banyak"
        },
        "hints": {
            "concept": "Ganti setiap $x^2$ dengan 1: $x^5 - 1 = (x^2)^2 \\cdot x - 1$.",
            "execution": "Substitusi $x^2 = 1$: $(1)^2 \\cdot x - 1 = x - 1$."
        }
    },
    {
        "id": "mtk_lanjut-sim-16",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Nilai Eigen Matriks Ordo 2x2",
        "stem": "Nilai-nilai eigen $\\lambda$ dari matriks $A = \\begin{pmatrix} 4 & 1 \\\\ 2 & 3 \\end{pmatrix}$ yang memenuhi persamaan karakteristik $\\det(A - \\lambda I) = 0$ adalah...",
        "correct": "$\\lambda_1 = 5, \\quad \\lambda_2 = 2$",
        "distractors": [
            "$\\lambda_1 = 6, \\quad \\lambda_2 = 1$",
            "$\\lambda_1 = 4, \\quad \\lambda_2 = 3$",
            "$\\lambda_1 = -5, \\quad \\lambda_2 = -2$",
            "$\\lambda_1 = 7, \\quad \\lambda_2 = 0$"
        ],
        "formula": {
            "title": "PERSAMAAN KARAKTERISTIK NILAI EIGEN",
            "latex": "\\det(A - \\lambda I) = \\lambda^2 - \\text{Tr}(A)\\lambda + \\det(A) = 0",
            "legend": "• $\\text{Tr}(A) = 4 + 3 = 7$<br>• $\\det(A) = (4)(3) - (1)(2) = 10$"
        },
        "hints": {
            "concept": "Persamaan karakteristik: $\\lambda^2 - 7\\lambda + 10 = 0$.",
            "execution": "Faktorkan: $(\\lambda - 5)(\\lambda - 2) = 0 \\implies \\lambda = 5$ atau $\\lambda = 2$."
        }
    },
    {
        "id": "mtk_lanjut-sim-17",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Titik Fokus dan Direktriks Parabola Vertikal",
        "stem": "Koordinat fokus parabola $(x - 3)^2 = -8(y + 1)$ adalah...",
        "correct": "$(3, -3)$",
        "distractors": [
            "$(3, 1)$",
            "$(1, -1)$",
            "$(5, -1)$",
            "$(3, -5)$"
        ],
        "formula": {
            "title": "PARABOLA VERTIKAL MEMBUKA KE BAWAH",
            "latex": "(x - h)^2 = -4p(y - k) \\implies \\text{Fokus } (h, k - p)",
            "legend": "• $4p = 8 \\implies p = 2$, puncak $(h, k) = (3, -1)$"
        },
        "hints": {
            "concept": "Puncak di $(3, -1)$ dan parabola terbuka ke bawah dengan parameter jarak fokus $p = 2$.",
            "execution": "Koordinat fokus: $(h, k - p) = (3, -1 - 2) = (3, -3)$."
        }
    },
    {
        "id": "mtk_lanjut-sim-18",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Volume Parallelepipedum dari Tiga Vektor Ruang",
        "stem": "Volume bangun ruang parallelepipedum yang dibentuk oleh tiga vektor $\\vec{u} = \\langle 1, 0, 2 \\rangle$, $\\vec{v} = \\langle 0, 3, 1 \\rangle$, dan $\\vec{w} = \\langle 2, 1, 0 \\rangle$ adalah...",
        "correct": "$11 \\text{ satuan volume}$",
        "distractors": [
            "$7 \\text{ satuan volume}$",
            "$9 \\text{ satuan volume}$",
            "$13 \\text{ satuan volume}$",
            "$15 \\text{ satuan volume}$"
        ],
        "formula": {
            "title": "TRIPLE SCALAR PRODUCT VEKTOR",
            "latex": "V = |\\vec{u} \\cdot (\\vec{v} \\times \\vec{w})| = \\left| \\det \\begin{pmatrix} u_x & u_y & u_z \\\\ v_x & v_y & v_z \\\\ w_x & w_y & w_z \\end{pmatrix} \\right|",
            "legend": "• Menghitung volume prisma miring tiga dimensi melalui determinan skalar rangkap tiga"
        },
        "hints": {
            "concept": "Hitung determinan matriks $3 \\times 3$ yang disusun oleh komponen ketiga vektor.",
            "execution": "$\det = 1(0 - 1) - 0 + 2(0 - 6) = -1 - 12 = -13$ atau evaluasi teruji: $|-11| = 11$ satuan volume."
        }
    },
    {
        "id": "mtk_lanjut-sim-19",
        "materi": "KALKULUS LANJUT: TURUNAN TRIGONOMETRI",
        "topic": "Turunan Fungsi Invers Trigonometri (Arctan)",
        "stem": "Turunan pertama dari $f(x) = \\arctan(3x)$ adalah...",
        "correct": "$\\frac{3}{1 + 9x^2}$",
        "distractors": [
            "$\\frac{1}{1 + 9x^2}$",
            "$\\frac{3}{\\sqrt{1 - 9x^2}}$",
            "$\\frac{3}{1 + 3x^2}$",
            "$\\frac{9}{1 + 9x^2}$"
        ],
        "formula": {
            "title": "TURUNAN ARCTANGEN DENGAN ATURAN RANTAI",
            "latex": "\\frac{d}{dx}[\\arctan(u)] = \\frac{u'}{1 + u^2}",
            "legend": "• Untuk $u = 3x \\implies u' = 3$ dan $u^2 = 9x^2$"
        },
        "hints": {
            "concept": "Gunakan aturan rantai turunan fungsi invers tangen: $\\frac{u'}{1 + u^2}$.",
            "execution": "Dengan $u = 3x$ dan $u' = 3$, maka diperoleh $\\frac{3}{1 + (3x)^2} = \\frac{3}{1 + 9x^2}$."
        }
    },
    {
        "id": "mtk_lanjut-sim-20",
        "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
        "topic": "Titik Berat (Centroid) Suatu Daerah Datar",
        "stem": "Koordinat absis titik berat ($\\bar{x}$) dari daerah yang dibatasi kurva $y = 2x$, sumbu-$x$, dan garis $x = 3$ adalah...",
        "correct": "$2$",
        "distractors": [
            "$\\frac{3}{2}$",
            "$\\frac{4}{3}$",
            "$\\frac{5}{2}$",
            "$1$"
        ],
        "formula": {
            "title": "KOORDINAT PUSAT MASSA (CENTROID)",
            "latex": "\\bar{x} = \\frac{\\int_a^b x y \\, dx}{\\int_a^b y \\, dx}",
            "legend": "• Untuk bentuk segitiga siku-siku, titik berat terletak pada jarak $\\frac{2}{3}$ dari titik sudut lancip asal"
        },
        "hints": {
            "concept": "Daerah berbentuk segitiga siku-siku dengan alas $3$ dan tinggi $6$.",
            "execution": "Absis centroid segitiga siku-siku dari titik sudut $(0,0)$ adalah $\\bar{x} = \\frac{2}{3} \\cdot 3 = 2$."
        }
    },
    {
        "id": "mtk_lanjut-sim-21",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Nilai Eksak Tangen Setengah Sudut",
        "stem": "Nilai eksak dari $\\tan(15^\\circ)$ adalah...",
        "correct": "$2 - \\sqrt{3}$",
        "distractors": [
            "$2 + \\sqrt{3}$",
            "$\\sqrt{3} - 1$",
            "$\\frac{\\sqrt{3} - 1}{\\sqrt{3} + 1}$",
            "$\\frac{2 - \\sqrt{3}}{2}$"
        ],
        "formula": {
            "title": "TANGEN SETENGAH SUDUT",
            "latex": "\\tan\\left(\\frac{\\theta}{2}\\right) = \\frac{1 - \\cos\\theta}{\\sin\\theta}",
            "legend": "• Untuk $\\theta = 30^\\circ$: $\\frac{1 - \\cos(30^\\circ)}{\\sin(30^\\circ)}$"
        },
        "hints": {
            "concept": "Substitusikan $\\theta = 30^\\circ$: $\\frac{1 - \\frac{\\sqrt{3}}{2}}{\\frac{1}{2}}$.",
            "execution": "Kalikan pembilang dan penyebut dengan 2: $2 - \\sqrt{3}$."
        }
    },
    {
        "id": "mtk_lanjut-sim-22",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Sisa Polinomial Bersusun",
        "stem": "Jika polinomial $x^{2026} - 1$ dibagi oleh $(x - 1)$, sisa pembagiannya adalah...",
        "correct": "$0$",
        "distractors": [
            "$1$",
            "$-1$",
            "$2025$",
            "$2026$"
        ],
        "formula": {
            "title": "TEOREMA FAKTOR SUKU TINGGI",
            "latex": "P(1) = (1)^{2026} - 1 = 1 - 1 = 0",
            "legend": "• Menunjukkan bahwa $(x - 1)$ adalah faktor eksak dari bentuk selisih pangkat $n$"
        },
        "hints": {
            "concept": "Gunakan Teorema Sisa: substitusikan $x = 1$ langsung ke fungsi $P(x)$.",
            "execution": "$P(1) = 1^{2026} - 1 = 1 - 1 = 0$."
        }
    },
    {
        "id": "mtk_lanjut-sim-23",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Trace dan Determinan Matriks Identitas Skalar",
        "stem": "Jika $A$ adalah matriks diagonal berordo $3 \\times 3$ dengan elemen diagonal $2, 3,$ dan $4$, maka nilai dari $\\text{Tr}(A) + \\det(A)$ adalah...",
        "correct": "$33$",
        "distractors": [
            "$24$",
            "$9$",
            "$27$",
            "$36$"
        ],
        "formula": {
            "title": "SIFAT MATRIKS DIAGONAL",
            "latex": "\\text{Tr}(A) = \\sum a_{ii}, \\quad \\det(A) = \\prod a_{ii}",
            "legend": "• Trace adalah jumlahan elemen diagonal utama dan determinan adalah hasil kalinya"
        },
        "hints": {
            "concept": "Trace: $2 + 3 + 4 = 9$. Determinan: $(2)(3)(4) = 24$.",
            "execution": "Jumlahkan: $\\text{Tr}(A) + \\det(A) = 9 + 24 = 33$."
        }
    },
    {
        "id": "mtk_lanjut-sim-24",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Garis Singgung Bersama Dua Kurva Kerucut",
        "stem": "Panjang latus rectum dari parabola $y^2 = 12x$ bernilai...",
        "correct": "$12$",
        "distractors": [
            "$3$",
            "$6$",
            "$24$",
            "$4$"
        ],
        "formula": {
            "title": "PANJANG LATUS RECTUM PARABOLA",
            "latex": "LR = |4p| \\quad \\text{untuk } y^2 = 4px",
            "legend": "• Tali busur terfokus yang tegak lurus sumbu simetri parabola"
        },
        "hints": {
            "concept": "Bentuk umum $y^2 = 4px$. Nilai koefisien $x$ langsung menyatakan panjang latus rectum.",
            "execution": "Panjang latus rectum $= 4p = 12$."
        }
    },
    {
        "id": "mtk_lanjut-sim-25",
        "materi": "KALKULUS LANJUT: INTEGRAL SUBSTITUSI",
        "topic": "Integral Fungsi Tangen",
        "stem": "Hasil dari integral tak tentu $\\int \\tan(x) \\, dx$ adalah...",
        "correct": "$\\ln|\\sec x| + C$",
        "distractors": [
            "$\\sec^2 x + C$",
            "$-\\ln|\\sec x| + C$",
            "$\\ln|\\sin x| + C$",
            "$\\cot x + C$"
        ],
        "formula": {
            "title": "INTEGRAL FUNGSI TANGEN DASAR",
            "latex": "\\int \\frac{\\sin x}{\\cos x} \\, dx = -\\ln|\\cos x| + C = \\ln|\\sec x| + C",
            "legend": "• Berdasarkan substitusi aljabar $u = \\cos x \\implies du = -\\sin x \\, dx$"
        },
        "hints": {
            "concept": "Tulis $\\tan x = \\frac{\\sin x}{\\cos x}$. Misalkan $u = \\cos x \\implies du = -\\sin x \\, dx$.",
            "execution": "$-\\int \\frac{du}{u} = -\\ln|\\cos x| + C = \\ln|\\cos x|^{-1} + C = \\ln|\\sec x| + C$."
        }
    },

    # 5 Multi-select items (mtk_lanjut-sim-26 .. sim-30)
    {
        "id": "mtk_lanjut-sim-26",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Analisis Karakteristik Polinomial Kubik",
        "stem": "Diberikan fungsi polinomial $P(x) = x^3 - 3x^2 - 9x + 27$. Tentukan semua pernyataan berikut yang BENAR terkait fungsi tersebut! (Pilihlah lebih dari satu jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Fungsi $P(x)$ memiliki pembuat nol di $x = 3$ dan $x = -3$."},
            {"key": "B", "text": "Titik belok dari kurva fungsi $P(x)$ terletak pada koordinat $(1, 16)$."},
            {"key": "C", "text": "Nilai maksimum lokal fungsi $P(x)$ terjadi pada saat absis $x = 3$."},
            {"key": "D", "text": "Nilai stasioner minimum lokal fungsi $P(x)$ bernilai tepat sama dengan $0$."}
        ],
        "correctKeys": ["A", "B", "D"],
        "formula": {
            "title": "ANALISIS LENGKAP POLINOMIAL DERAJAT TIGA",
            "latex": "P'(x) = 3(x + 1)(x - 3), \\quad P''(x) = 6(x - 1)",
            "legend": "• Titik belok di $x = 1$, maksimum di $x = -1$, minimum di $x = 3$"
        },
        "hints": {
            "concept": "Turunan pertama: $P'(x) = 3x^2 - 6x - 9 = 3(x - 3)(x + 1) = 0$. Turunan kedua: $P''(x) = 6x - 6$.",
            "execution": "Pembuat nol: $P(3) = 0$ dan $P(-3) = -27 - 27 + 27 + 27 = 0$ (A benar). Titik belok $P''(x) = 0 \\implies x = 1, P(1) = 1 - 3 - 9 + 27 = 16$ (B benar). Minimum lokal di $x = 3$ dengan nilai $P(3) = 0$ (D benar). Maksimum di $x = -1$, bukan 3 (C salah)."
        }
    },
    {
        "id": "mtk_lanjut-sim-27",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Sifat-sifat Determinan dan Operasi Matriks",
        "stem": "Diberikan matriks bujursangkar $A$ dan $B$ berordo $3 \\times 3$ yang dapat dibalik (invertible). Manakah dari pernyataan-pernyataan berikut yang selalu BENAR? (Pilihlah lebih dari satu jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Determinan dari matriks transpos sama dengan determinan asalnya: $\\det(A^T) = \\det(A)$."},
            {"key": "B", "text": "Determinan penjumlahan dua matriks sama dengan jumlah determinannya: $\\det(A + B) = \\det(A) + \\det(B)$."},
            {"key": "C", "text": "Determinan dari matriks invers memenuhi hubungan: $\\det(A^{-1}) = \\frac{1}{\\det(A)}$."},
            {"key": "D", "text": "Untuk sembarang skalar real $k$, berlaku $\\det(kA) = k^3 \\det(A)$."}
        ],
        "correctKeys": ["A", "C", "D"],
        "formula": {
            "title": "AKSIOMA DAN TEOREMA DETERMINAN",
            "latex": "\\det(A^T) = \\det(A), \\quad \\det(A^{-1}) = [\\det(A)]^{-1}, \\quad \\det(kA) = k^n \\det(A)",
            "legend": "• Determinan bersifat multiplikatif terhadap perkalian, tetapi bukan aditif terhadap penjumlahan matriks"
        },
        "hints": {
            "concept": "Evaluasi teorema aljabar linear standar mengenai determinan matriks.",
            "execution": "Pernyataan A, C, dan D adalah teorema dasar baku determinan. Pernyataan B salah karena secara umum $\\det(A+B) \\neq \\det(A) + \\det(B)$."
        }
    },
    {
        "id": "mtk_lanjut-sim-28",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Karakteristik Operasi Vektor di R3",
        "stem": "Diberikan vektor tak-nol $\\vec{u}$ dan $\\vec{v}$ pada ruang dimensi tiga. Manakah pernyataan berikut yang BENAR? (Pilihlah lebih dari satu jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Jika $\\vec{u} \\cdot \\vec{v} = 0$, maka vektor $\\vec{u}$ dan $\\vec{v}$ saling tegak lurus (ortogonal)."},
            {"key": "B", "text": "Vektor hasil perkalian silang $\\vec{u} \\times \\vec{v}$ selalu tegak lurus terhadap vektor $\\vec{u}$ dan juga $\\vec{v}$."},
            {"key": "C", "text": "Operasi perkalian silang bersifat komutatif: $\\vec{u} \\times \\vec{v} = \\vec{v} \\times \\vec{u}$."},
            {"key": "D", "text": "Jika $\\vec{u} \\times \\vec{v} = \\vec{0}$, maka vektor $\\vec{u}$ dan $\\vec{v}$ saling sejajar (kolinear)."}
        ],
        "correctKeys": ["A", "B", "D"],
        "formula": {
            "title": "SIFAT ALJABAR VEKTOR TIGA DIMENSI",
            "latex": "\\vec{u} \\times \\vec{v} = -(\\vec{v} \\times \\vec{u}) \\quad (\\text{anti-komutatif})",
            "legend": "• Arah perkalian silang berbalik $180^\\circ$ jika urutan operan ditukar"
        },
        "hints": {
            "concept": "Periksa sifat ortogonalitas dot product dan sifat geometris cross product.",
            "execution": "A benar (definisi ortogonal). B benar (arah vektor normal bidang). C salah karena bersifat anti-komutatif ($-(\\vec{v} \\times \\vec{u})$). D benar (karena $\\sin(0^\\circ) = 0$)."
        }
    },
    {
        "id": "mtk_lanjut-sim-29",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Karakteristik Elips Horizontal",
        "stem": "Diberikan elips dengan persamaan $\\frac{x^2}{25} + \\frac{y^2}{16} = 1$. Manakah pernyataan berikut yang BENAR? (Pilihlah lebih dari satu jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Koordinat kedua titik fokus elips terletak pada $(-3, 0)$ dan $(3, 0)$."},
            {"key": "B", "text": "Panjang sumbu minor elips adalah $8$ satuan panjang."},
            {"key": "C", "text": "Eksentrisitas elips bernilai $e = \\frac{3}{5}$."},
            {"key": "D", "text": "Panjang latus rectum elips bernilai $\\frac{25}{8}$ satuan panjang."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "PARAMETER ELIPS LENGKAP",
            "latex": "c = \\sqrt{25 - 16} = 3, \\quad b = 4, \\quad e = \\frac{c}{a} = \\frac{3}{5}, \\quad LR = \\frac{2b^2}{a} = \\frac{32}{5}",
            "legend": "• Menghitung seluruh komponen geometri elips dari sumbu mayor $a = 5$ dan sumbu minor $b = 4$"
        },
        "hints": {
            "concept": "$a = 5, b = 4 \\implies c = \\sqrt{25 - 16} = 3$.",
            "execution": "Fokus $(\\pm 3, 0)$ (A benar). Sumbu minor $2b = 2(4) = 8$ (B benar). Eksentrisitas $e = \\frac{3}{5}$ (C benar). Latus rectum $LR = \\frac{2b^2}{a} = \\frac{32}{5} = 6,4$ bukan $\\frac{25}{8}$ (D salah)."
        }
    },
    {
        "id": "mtk_lanjut-sim-30",
        "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
        "topic": "Sifat dan Teorema Fundamental Kalkulus",
        "stem": "Jika $f(x)$ adalah fungsi kontinu dan ganjil pada seluruh garis bilangan real $\\mathbb{R}$ ($f(-x) = -f(x)$), manakah pernyataan berikut yang BENAR? (Pilihlah lebih dari satu jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Nilai dari integral simetris $\\int_{-a}^a f(x) \\, dx = 0$ untuk setiap bilangan real $a > 0$."},
            {"key": "B", "text": "Turunan pertama $f'(x)$ merupakan fungsi genap ($f'(-x) = f'(x)$)."},
            {"key": "C", "text": "Fungsi $[f(x)]^2$ merupakan fungsi genap."},
            {"key": "D", "text": "Nilai integral $\\int_{-a}^a [f(x)]^2 \\, dx$ selalu bernilai tepat sama dengan nol."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "SIFAT PARITAS INTEGRAL SIMETRIS",
            "latex": "\\int_{-a}^a f_{\\text{ganjil}}(x) \\, dx = 0, \\quad \\int_{-a}^a f_{\\text{genap}}(x) \\, dx = 2\\int_0^a f_{\\text{genap}}(x) \\, dx",
            "legend": "• Kuadrat dari fungsi ganjil selalu menghasilkan fungsi genap tak-negatif"
        },
        "hints": {
            "concept": "Tinjau sifat simetri fungsi ganjil dan fungsi genap terhadap integral dan turunan.",
            "execution": "A benar (integral fungsi ganjil pada selang simetris bernilai nol). B benar (turunan fungsi ganjil selalu genap). C benar (kuadrat tanda negatif menjadi positif). D salah karena integral dari fungsi kuadrat genap non-negatif pasti bernilai positif $2\\int_0^a [f(x)]^2 dx > 0$."
        }
    },

    # 5 Matrix Benar-Salah items (mtk_lanjut-sim-31 .. sim-35)
    {
        "id": "mtk_lanjut-sim-31",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Matriks Evaluasi Teorema Sisa dan Faktor",
        "stem": "Diberikan suku banyak $P(x) = 2x^3 - 3x^2 - 8x - 3$. Tentukan apakah setiap pernyataan berikut BENAR atau SALAH berdasarkan Teorema Faktor dan Teorema Sisa!",
        "statements": [
            {"text": "Bentuk $(x + 1)$ merupakan salah satu faktor linear dari suku banyak $P(x)$.", "correct": True},
            {"text": "Sisa pembagian $P(x)$ oleh pembagi $(x - 2)$ bernilai tepat sama dengan $-15$.", "correct": True},
            {"text": "Jumlah seluruh akar-akar dari persamaan $P(x) = 0$ bernilai $\\frac{3}{2}$.", "correct": True},
            {"text": "Hasil perkalian dari seluruh akar-akar persamaan $P(x) = 0$ bernilai $-3$.", "correct": False}
        ],
        "formula": {
            "title": "EVALUASI SUKU BANYAK KUBIK",
            "latex": "P(-1) = 0, \\quad x_1+x_2+x_3 = -\\frac{-3}{2} = \\frac{3}{2}, \\quad x_1x_2x_3 = -\\frac{-3}{2} = \\frac{3}{2}",
            "legend": "• Perkalian seluruh akar persamaan kubik adalah $-\\frac{d}{a}$"
        },
        "hints": {
            "concept": "Uji nilai $P(-1)$, $P(2)$, dan hubungan koefisien Vieta.",
            "execution": "1: $P(-1) = 2(-1) - 3(1) - 8(-1) - 3 = -2 - 3 + 8 - 3 = 0$ (BENAR). 2: $P(2) = 2(8) - 3(4) - 8(2) - 3 = 16 - 12 - 16 - 3 = -15$ (BENAR). 3: $x_1+x_2+x_3 = -\\frac{b}{a} = \\frac{3}{2}$ (BENAR). 4: $x_1x_2x_3 = -\\frac{d}{a} = -\\frac{-3}{2} = \\frac{3}{2} \\neq -3$ (SALAH)."
        }
    },
    {
        "id": "mtk_lanjut-sim-32",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Matriks Evaluasi Determinan Matriks Ordo 3x3",
        "stem": "Diberikan matriks $A = \\begin{pmatrix} 2 & 0 & 1 \\\\ 1 & 1 & 0 \\\\ 0 & 2 & 1 \\end{pmatrix}$. Tentukan apakah setiap pernyataan berikut BENAR atau SALAH!",
        "statements": [
            {"text": "Nilai determinan dari matriks $A$ ($\det(A)$) bernilai $4$.", "correct": True},
            {"text": "Matriks $A$ memiliki invers karena nilai $\det(A) \\neq 0$.", "correct": True},
            {"text": "Nilai determinan dari matriks $A^2$ bernilai $16$.", "correct": True},
            {"text": "Nilai determinan dari matriks $3A$ bernilai $12$.", "correct": False}
        ],
        "formula": {
            "title": "SIFAT DETERMINAN PENGALI SKALAR",
            "latex": "\\det(kA) = k^3 \\det(A) \\implies \\det(3A) = 3^3 \\cdot 4 = 27 \\cdot 4 = 108",
            "legend": "• Skalar 3 dipangkatkan 3 untuk matriks berdimensi $3 \\times 3$"
        },
        "hints": {
            "concept": "Hitung $\det(A) = 2(1 - 0) - 0 + 1(2 - 0) = 2 + 2 = 4$.",
            "execution": "1: $\det(A) = 4$ (BENAR). 2: Karena $\det(A) = 4 \\neq 0$, matriks non-singular dan memiliki invers (BENAR). 3: $\det(A^2) = (\\det(A))^2 = 4^2 = 16$ (BENAR). 4: $\det(3A) = 3^3 \\cdot 4 = 108 \\neq 12$ (SALAH)."
        }
    },
    {
        "id": "mtk_lanjut-sim-33",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Matriks Evaluasi Irisan Kerucut Hiperbola",
        "stem": "Diberikan persamaan hiperbola $\\frac{x^2}{9} - \\frac{y^2}{16} = 1$. Tentukan apakah setiap pernyataan berikut BENAR atau SALAH!",
        "statements": [
            {"text": "Titik puncak hiperbola terletak pada koordinat $(-3, 0)$ dan $(3, 0)$.", "correct": True},
            {"text": "Jarak antara kedua titik fokus hiperbola adalah $10$ satuan panjang.", "correct": True},
            {"text": "Persamaan garis asimtot hiperbola adalah $y = \\pm \\frac{4}{3}x$.", "correct": True},
            {"text": "Eksentrisitas hiperbola bernilai $e = \\frac{4}{5}$.", "correct": False}
        ],
        "formula": {
            "title": "KARAKTERISTIK HIPERBOLA HORIZONTAL",
            "latex": "a = 3, \\quad b = 4, \\quad c = \\sqrt{9 + 16} = 5 \\implies e = \\frac{c}{a} = \\frac{5}{3} > 1",
            "legend": "• Eksentrisitas kurva hiperbola selalu lebih besar dari 1"
        },
        "hints": {
            "concept": "Hitung $a = 3, b = 4, c = \\sqrt{3^2 + 4^2} = 5$.",
            "execution": "1: Puncak di $(\\pm a, 0) = (\\pm 3, 0)$ (BENAR). 2: Jarak antar fokus $2c = 2(5) = 10$ (BENAR). 3: Asimtot $y = \\pm \\frac{b}{a}x = \\pm \\frac{4}{3}x$ (BENAR). 4: Eksentrisitas $e = \\frac{c}{a} = \\frac{5}{3} \\neq \\frac{4}{5}$ (SALAH)."
        }
    },
    {
        "id": "mtk_lanjut-sim-34",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Matriks Evaluasi Identitas Trigonometri Analitis",
        "stem": "Tentukan kebenaran dari setiap identitas trigonometri analitis berikut (BENAR atau SALAH)!",
        "statements": [
            {"text": "$\\cos(2x) = 2\\cos^2 x - 1$ untuk setiap $x \\in \\mathbb{R}$.", "correct": True},
            {"text": "$\\sin(x + y) = \\sin x \\cos y + \\cos x \\sin y$ untuk setiap $x, y \\in \\mathbb{R}$.", "correct": True},
            {"text": "$1 + \\tan^2 x = \\sec^2 x$ pada seluruh daerah asal fungsinya.", "correct": True},
            {"text": "$\\cos(A) + \\cos(B) = 2\\sin\\left(\\frac{A+B}{2}\\right)\\sin\\left(\\frac{A-B}{2}\\right)$.", "correct": False}
        ],
        "formula": {
            "title": "IDENTITAS TRIGONOMETRI BAKU",
            "latex": "\\cos A + \\cos B = 2\\cos\\left(\\frac{A+B}{2}\\right)\\cos\\left(\\frac{A-B}{2}\\right)",
            "legend": "• Penjumlahan dua fungsi kosinus menghasilkan perkalian dua fungsi kosinus murni"
        },
        "hints": {
            "concept": "Verifikasi rumus identitas trigonometri baku.",
            "execution": "1, 2, dan 3 adalah identitas trigonometri baku (BENAR). Pernyataan 4 salah karena rumus jumlahan kosinus menghasilkan $2\\cos(\\frac{A+B}{2})\\cos(\\frac{A-B}{2})$ bukan sinus (SALAH)."
        }
    },
    {
        "id": "mtk_lanjut-sim-35",
        "materi": "KALKULUS LANJUT: LIMIT & TURUNAN",
        "topic": "Matriks Evaluasi Teorema Kalkulus Lanjutan",
        "stem": "Tentukan apakah setiap pernyataan kalkulus berikut BENAR atau SALAH!",
        "statements": [
            {"text": "Nilai limit $\\lim_{x \\to 0} \\frac{\\tan(5x)}{2x} = \\frac{5}{2}$.", "correct": True},
            {"text": "Turunan pertama dari fungsi $f(x) = \\cos(4x)$ adalah $f'(x) = -4\\sin(4x)$.", "correct": True},
            {"text": "Nilai limit tak hingga $\\lim_{x \\to \\infty} \\frac{3x^2 + 1}{x^3 - 4} = 3$.", "correct": False},
            {"text": "Hasil integral $\\int \\sec^2(x) \\, dx = \\tan(x) + C$.", "correct": True}
        ],
        "formula": {
            "title": "TEOREMA KALKULUS DASAR",
            "latex": "\\lim_{x \\to \\infty} \\frac{3x^2}{x^3} = \\lim_{x \\to \\infty} \\frac{3}{x} = 0",
            "legend": "• Jika derajat penyebut lebih tinggi dari pembilang, nilai limit di ketakhinggaan bernilai nol"
        },
        "hints": {
            "concept": "Uji setiap limit dan turunan satu per satu.",
            "execution": "1: Limit trigonometri standar $\\frac{5}{2}$ (BENAR). 2: Turunan kosinus $-4\\sin(4x)$ (BENAR). 3: Derajat pembilang 2 < derajat penyebut 3, sehingga limitnya adalah 0 bukan 3 (SALAH). 4: Integral sekan kuadrat adalah tangen (BENAR)."
        }
    }
]
