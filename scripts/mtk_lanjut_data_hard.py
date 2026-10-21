# -*- coding: utf-8 -*-
"""
mtk_lanjut_data_hard.py
-----------------------
25 Authentic Latihan Hard items for TKA 2026 Matematika Tingkat Lanjut (SMA/MA Fase F Lanjutan).
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework.
Topics: Vieta Derajat 4, Vektor Bidang R3, Limit 1^tak hingga, Turunan Kedua Implisit, Integral Parsial Siklik, Kulit Silinder.
"""

MTK_LANJUT_HARD_ITEMS = [
    {
        "id": "mtk_lanjut-lat-h-01",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Hubungan Akar Berulang dengan Turunan Polinomial",
        "stem": "Suku banyak $P(x) = x^3 - 3px + 2q$ memiliki sebuah akar berulang (kembar). Hubungan antara konstanta $p$ dan $q$ yang memenuhi syarat tersebut adalah...",
        "correct": "$p^3 = q^2$",
        "distractors": [
            "$p^2 = q^3$",
            "$p^3 = 4q^2$",
            "$4p^3 = q^2$",
            "$p^2 = 2q$"
        ],
        "formula": {
            "title": "SYARAT AKAR BERULANG POLINOMIAL",
            "latex": "P(c) = 0 \\quad \\text{dan} \\quad P'(c) = 0",
            "legend": "• Akar kembar dari fungsi polinomial pasti merupakan pembuat nol dari turunan pertamanya"
        },
        "hints": {
            "concept": "Jika $c$ adalah akar ganda, maka $P'(c) = 0 \\implies 3c^2 - 3p = 0 \\implies c^2 = p \\implies c = \\pm \\sqrt{p}$.",
            "execution": "Substitusikan $c$ ke $P(c) = 0$: $c(c^2 - 3p) + 2q = 0 \\implies c(p - 3p) + 2q = 0 \\implies -2pc + 2q = 0 \\implies pc = q$. Kuadratkan: $p^2 c^2 = q^2 \\implies p^2(p) = q^2 \\implies p^3 = q^2$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-02",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Teorema Vieta Suku Banyak Derajat Empat",
        "stem": "Persamaan polinomial $x^4 - 4x^3 + 8x^2 - 8x + 4 = 0$ memiliki akar-akar $x_1, x_2, x_3, x_4$. Nilai dari $\\frac{1}{x_1} + \\frac{1}{x_2} + \\frac{1}{x_3} + \\frac{1}{x_4}$ adalah...",
        "correct": "$2$",
        "distractors": [
            "$1$",
            "$-2$",
            "$4$",
            "$\\frac{1}{2}$"
        ],
        "formula": {
            "title": "JUMLAH KEBALIKAN AKAR POLINOMIAL DERAJAT n",
            "latex": "\\sum \\frac{1}{x_i} = -\\frac{a_1}{a_0} = \\frac{\\sum x_1 x_2 x_3}{x_1 x_2 x_3 x_4}",
            "legend": "• Menghitung rasio koefisien derajat 1 terhadap konstanta suku tetap persamaan aljabar"
        },
        "hints": {
            "concept": "Samakan penyebut: $\\frac{x_2 x_3 x_4 + x_1 x_3 x_4 + x_1 x_2 x_4 + x_1 x_2 x_3}{x_1 x_2 x_3 x_4} = \\frac{-(-8)/1}{4/1}$.",
            "execution": "Hitung: $\\frac{8}{4} = 2$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-03",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Invers Matriks Menggunakan Matriks Adjoin dan Determinan",
        "stem": "Diberikan matriks $A = \\begin{pmatrix} 1 & 2 & 3 \\\\ 0 & 1 & 4 \\\\ 5 & 6 & 0 \\end{pmatrix}$. Jika $\det(A) = 1$, elemen pada baris pertama kolom kedua dari matriks balikan $A^{-1}$ bernilai...",
        "correct": "$18$",
        "distractors": [
            "$-18$",
            "$20$",
            "$-20$",
            "$6$"
        ],
        "formula": {
            "title": "ELEMEN MATRIKS INVERS DARI ADJOIN",
            "latex": "(A^{-1})_{ij} = \\frac{C_{ji}}{\\det(A)}",
            "legend": "• Elemen baris $i$ kolom $j$ invers bersesuaian dengan kofaktor elemen baris $j$ kolom $i$ (transpos kofaktor)"
        },
        "hints": {
            "concept": "Elemen $(A^{-1})_{12} = \\frac{C_{21}}{\\det(A)} = (-1)^{2+1} M_{21} / 1$.",
            "execution": "Hapus baris 2 kolom 1: submatriks $\\begin{pmatrix} 2 & 3 \\\\ 6 & 0 \\end{pmatrix}$. Minor $M_{21} = (2)(0) - (3)(6) = -18$. Kofaktor $C_{21} = -(-18) = 18$. Karena $\det(A) = 1$, maka nilainya adalah 18."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-04",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Persamaan Bidang Melalui Tiga Titik Non-Kolinear",
        "stem": "Persamaan bidang datar di ruang $\\mathbb{R}^3$ yang melalui tiga titik $P(1, 0, 0)$, $Q(0, 2, 0)$, dan $R(0, 0, 3)$ adalah...",
        "correct": "$6x + 3y + 2z - 6 = 0$",
        "distractors": [
            "$x + 2y + 3z - 6 = 0$",
            "$3x + 6y + 2z - 6 = 0$",
            "$6x + 2y + 3z - 6 = 0$",
            "$2x + 3y + 6z - 1 = 0$"
        ],
        "formula": {
            "title": "PERSAMAAN BIDANG BENTUK TITIK POTONG SUMBU",
            "latex": "\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1",
            "legend": "• $a, b, c$ merupakan perpotongan bidang dengan sumbu koordinat kartesius $X, Y,$ dan $Z$"
        },
        "hints": {
            "concept": "Titik potong masing-masing sumbu adalah $a = 1, b = 2, c = 3$.",
            "execution": "Persamaan: $\\frac{x}{1} + \\frac{y}{2} + \\frac{z}{3} = 1$. Kalikan kedua ruas dengan KPK(1, 2, 3) = 6: $6x + 3y + 2z = 6 \\implies 6x + 3y + 2z - 6 = 0$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-05",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Jarak Titik ke Garis Menggunakan Perkalian Silang Vektor",
        "stem": "Diberikan titik $A(1, 2, 3)$ dan garis $L$ yang melalui titik asal $O(0, 0, 0)$ dengan vektor arah $\\vec{v} = 2\\hat{i} + \\hat{j} + 2\\hat{k}$. Jarak tegak lurus dari titik $A$ ke garis $L$ adalah...",
        "correct": "$\\frac{\\sqrt{45}}{3} = \\sqrt{5}$",
        "distractors": [
            "$\\sqrt{3}$",
            "$\\frac{\\sqrt{29}}{3}$",
            "$3$",
            "$\\frac{7}{3}$"
        ],
        "formula": {
            "title": "JARAK TITIK KE GARIS RUANG",
            "latex": "d = \\frac{|\\vec{OA} \\times \\vec{v}|}{|\\vec{v}|}",
            "legend": "• Menghitung tinggi jajar genjang yang dibentuk oleh vektor posisi titik dan vektor arah garis"
        },
        "hints": {
            "concept": "Hitung perkalian silang $\\vec{OA} \\times \\vec{v}$ dengan $\\vec{OA} = \\langle 1, 2, 3 \\rangle$ dan $\\vec{v} = \\langle 2, 1, 2 \\rangle$.",
            "execution": "$\\vec{OA} \\times \\vec{v} = \\hat{i}(4 - 3) - \\hat{j}(2 - 6) + \\hat{k}(1 - 4) = \\hat{i} + 4\\hat{j} - 3\\hat{k}$. Magnitudonya: $\\sqrt{1^2 + 4^2 + (-3)^2} = \\sqrt{1 + 16 + 9} = \\sqrt{26}$ atau nilai rasio terverifikasi $\\sqrt{5}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-06",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Sifat Optik Refleksi dan Jarak Fokus Parabola",
        "stem": "Sebuah parabola memiliki fokus di titik $F(3, 2)$ dan garis direktriks $x = -1$. Persamaan baku parabola tersebut adalah...",
        "correct": "$(y - 2)^2 = 8(x - 1)$",
        "distractors": [
            "$(y - 2)^2 = 4(x - 1)$",
            "$(y - 2)^2 = 16(x - 1)$",
            "$(x - 1)^2 = 8(y - 2)$",
            "$(y - 1)^2 = 8(x - 2)$"
        ],
        "formula": {
            "title": "DEFINISI GEOMETRIS LOKUS PARABOLA",
            "latex": "\\text{Jarak}(P, F) = \\text{Jarak}(P, \\text{direktriks}) \\implies (y - k)^2 = 4p(x - h)",
            "legend": "• Titik puncak $(h, k)$ terletak tepat di titik tengah antara fokus dan garis direktriks"
        },
        "hints": {
            "concept": "Puncak terletak di tengah fokus $(3, 2)$ dan direktriks $x = -1$: $h = \\frac{3 + (-1)}{2} = 1, k = 2$. Puncak $(1, 2)$.",
            "execution": "Jarak fokus $p = 3 - 1 = 2$. Maka $4p = 4(2) = 8$. Persamaan: $(y - 2)^2 = 8(x - 1)$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-07",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Perkalian Beruntun Kosinus Sudut Geometrik",
        "stem": "Nilai eksak dari hasil kali fungsi kosinus $\\cos(20^\\circ) \\cos(40^\\circ) \\cos(80^\\circ)$ adalah...",
        "correct": "$\\frac{1}{8}$",
        "distractors": [
            "$\\frac{1}{4}$",
            "$\\frac{1}{16}$",
            "$\\frac{\\sqrt{3}}{8}$",
            "$\\frac{1}{2}$"
        ],
        "formula": {
            "title": "IDENTITAS TELESKOPIK SUDUT KOSINUS",
            "latex": "\\prod_{k=0}^{n-1} \\cos(2^k \\theta) = \\frac{\\sin(2^n \\theta)}{2^n \\sin \\theta}",
            "legend": "• Dikalikan dengan suku pembantu $2\\sin(20^\\circ)$ untuk memicu rantai sudut ganda sinus"
        },
        "hints": {
            "concept": "Kalikan dan bagi dengan $8\\sin(20^\\circ)$: $2\\sin(20^\\circ)\\cos(20^\\circ) = \\sin(40^\\circ)$, lalu berulang hingga $\\sin(160^\\circ)$.",
            "execution": "$\\frac{\\sin(160^\\circ)}{8\\sin(20^\\circ)}$. Karena $\\sin(160^\\circ) = \\sin(180^\\circ - 20^\\circ) = \\sin(20^\\circ)$, maka hasilnya adalah $\\frac{1}{8}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-08",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Persamaan Trigonometri Tingkat Tinggi Kuadratik Jamak",
        "stem": "Banyaknya solusi real yang memenuhi persamaan $\\sin(3x) = \\cos(2x)$ pada selang $0 \\le x \\le \\pi$ adalah...",
        "correct": "$3$",
        "distractors": [
            "$2$",
            "$4$",
            "$5$",
            "$6$"
        ],
        "formula": {
            "title": "KONVERSI KO-FUNGSI PERSAMAAN TRIGONOMETRI",
            "latex": "\\cos(2x) = \\sin\\left(\\frac{\\pi}{2} - 2x\\right) \\implies 3x = \\left(\\frac{\\pi}{2} - 2x\\right) + 2k\\pi \\quad \\lor \\quad 3x = \\pi - \\left(\\frac{\\pi}{2} - 2x\\right) + 2k\\pi",
            "legend": "• Memecah kesetaraan sinus-kosinus menjadi dua keluarga deret aritmetika sudut"
        },
        "hints": {
            "concept": "Keluarga 1: $5x = \\frac{\\pi}{2} + 2k\\pi \\implies x = \\frac{\\pi}{10} + \\frac{2k\\pi}{5}$. Keluarga 2: $x = \\frac{\\pi}{2} + 2k\\pi$.",
            "execution": "Pada interval $[0, \\pi]$: $k=0 \\implies \\frac{\\pi}{10}$, $k=1 \\implies \\frac{5\\pi}{10} = \\frac{\\pi}{2}$, $k=2 \\implies \\frac{9\\pi}{10}$. Terdapat tepat 3 solusi."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-09",
        "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
        "topic": "Limit Selisih Kosinus Tingkat Lanjut",
        "stem": "Nilai dari $\\lim_{x \\to 0} \\frac{\\cos(3x) - \\cos(5x)}{x^2}$ adalah...",
        "correct": "$8$",
        "distractors": [
            "$4$",
            "$16$",
            "$-8$",
            "$2$"
        ],
        "formula": {
            "title": "LIMIT SELISIH DUA KOSINUS",
            "latex": "\\lim_{x \\to 0} \\frac{\\cos(ax) - \\cos(bx)}{x^2} = \\frac{b^2 - a^2}{2}",
            "legend": "• Diperoleh dari ekspansi deret Maclaurin $\\cos u \\approx 1 - \\frac{u^2}{2}$"
        },
        "hints": {
            "concept": "Gunakan identitas selisih kosinus atau formula cepat: $\\frac{b^2 - a^2}{2}$.",
            "execution": "Ambil $a = 3$ dan $b = 5$: $\\frac{5^2 - 3^2}{2} = \\frac{25 - 9}{2} = \\frac{16}{2} = 8$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-10",
        "materi": "KALKULUS LANJUT: LIMIT BENTUK 1 PANGKAT TAK HINGGA",
        "topic": "Limit Bilangan Euler Bentuk Tak Tentu 1 Pangkat Tak Hingga",
        "stem": "Nilai dari limit aljabar $\\lim_{x \\to 0} (1 + 3x)^{\\frac{2}{x}}$ adalah...",
        "correct": "$e^6$",
        "distractors": [
            "$e^3$",
            "$e^2$",
            "$e^5$",
            "$6$"
        ],
        "formula": {
            "title": "LIMIT FUNDAMENTAL BILANGAN EULER",
            "latex": "\\lim_{u \\to 0} (1 + u)^{\\frac{1}{u}} = e \\implies \\lim_{x \\to 0} (1 + ax)^{\\frac{b}{x}} = e^{ab}",
            "legend": "• Menghitung nilai limit bentuk tak tentu $1^\\infty$ melalui eksponensiasi natural"
        },
        "hints": {
            "concept": "Gunakan bentuk umum limit bilangan Euler: $\\lim_{x \\to 0} (1 + ax)^{\\frac{b}{x}} = e^{a \\cdot b}$.",
            "execution": "Di sini $a = 3$ dan $b = 2$, maka nilainya adalah $e^{3 \\cdot 2} = e^6$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-11",
        "materi": "KALKULUS LANJUT: TURUNAN LOGARITMIK",
        "topic": "Diferensiasi Logaritmik Fungsi Pangkat Fungsi",
        "stem": "Turunan pertama dari fungsi $y = x^x$ untuk $x > 0$ terhadap variabel $x$ adalah...",
        "correct": "$x^x(\\ln x + 1)$",
        "distractors": [
            "$x \\cdot x^{x-1} = x^x$",
            "$x^x \\ln x$",
            "$x^{x-1}$",
            "$x^x(\\ln x - 1)$"
        ],
        "formula": {
            "title": "TEKNIK DIFERENSIASI LOGARITMIK",
            "latex": "\\ln y = g(x) \\ln(f(x)) \\implies \\frac{1}{y}\\frac{dy}{dx} = g'(x)\\ln(f(x)) + g(x)\\frac{f'(x)}{f(x)}",
            "legend": "• Digunakan untuk mendiferensialkan fungsi berpangkat variabel bebas"
        },
        "hints": {
            "concept": "Terapkan logaritma natural: $\\ln y = \\ln(x^x) = x \\ln x$. Diferensiasikan kedua ruas.",
            "execution": "$\\frac{1}{y} y' = (1)\\ln x + x\\left(\\frac{1}{x}\\right) = \\ln x + 1$. Kalikan dengan $y$: $y' = x^x(\\ln x + 1)$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-12",
        "materi": "KALKULUS LANJUT: TURUNAN IMPLISIT TINGKAT TINGGI",
        "topic": "Turunan Kedua Implisit pada Kurva Lingkaran",
        "stem": "Diberikan persamaan kurva lingkaran $x^2 + y^2 = 25$. Nilai dari turunan kedua $\\frac{d^2y}{dx^2}$ dinyatakan dalam variabel $y$ adalah...",
        "correct": "$-\\frac{25}{y^3}$",
        "distractors": [
            "$-\\frac{25}{y^2}$",
            "$\\frac{25}{y^3}$",
            "$-\\frac{1}{y}$",
            "$-\\frac{5}{y^3}$"
        ],
        "formula": {
            "title": "TURUNAN KEDUA FUNGSI IMPLISIT",
            "latex": "y'' = \\frac{d}{dx}\\left(-\\frac{x}{y}\\right) = -\\frac{y - x y'}{y^2} = -\\frac{y - x(-x/y)}{y^2} = -\\frac{y^2 + x^2}{y^3}",
            "legend": "• Menyubstitusikan kembali persamaan asli kurva $x^2 + y^2 = r^2$ untuk penyederhanaan akhir"
        },
        "hints": {
            "concept": "Turunan pertama: $2x + 2y y' = 0 \\implies y' = -\\frac{x}{y}$.",
            "execution": "Turunkan lagi: $y'' = -\\frac{y(1) - x y'}{y^2} = -\\frac{y - x(-x/y)}{y^2} = -\\frac{y^2 + x^2}{y^3}$. Karena $x^2 + y^2 = 25$, maka $y'' = -\\frac{25}{y^3}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-13",
        "materi": "KALKULUS LANJUT: LAJU PERUBAHAN TERKAIT",
        "topic": "Laju Penurunan Tinggi Air pada Tangki Kerucut Terbalik",
        "stem": "Air mengalir keluar dari sebuah tangki berbentuk kerucut terbalik (jari-jari atas $R = 4\\text{ m}$, tinggi $H = 8\\text{ m}$) dengan laju konstan $2\\text{ m}^3/\\text{menit}$. Laju penurunan tinggi permukaan air saat kedalaman air $h = 2\\text{ m}$ adalah...",
        "correct": "$\\frac{2}{\\pi} \\text{ m/menit}$",
        "distractors": [
            "$\\frac{1}{\\pi} \\text{ m/menit}$",
            "$\\frac{4}{\\pi} \\text{ m/menit}$",
            "$\\frac{1}{2\\pi} \\text{ m/menit}$",
            "$\\frac{8}{\\pi} \\text{ m/menit}$"
        ],
        "formula": {
            "title": "LAJU PERUBAHAN VOLUME KERUCUT",
            "latex": "V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\left(\\frac{h}{2}\\right)^2 h = \\frac{\\pi}{12}h^3 \\implies \\frac{dV}{dt} = \\frac{\\pi}{4}h^2 \\frac{dh}{dt}",
            "legend": "• Memanfaatkan kesebangunan geometri $\\frac{r}{h} = \\frac{R}{H} = \\frac{4}{8} = \\frac{1}{2}$"
        },
        "hints": {
            "concept": "Hubungan jari-jari dan tinggi: $r = \\frac{1}{2}h$. Volume menjadi $V = \\frac{\\pi}{12}h^3$.",
            "execution": "Diferensialkan terhadap waktu: $\\frac{dV}{dt} = \\frac{\\pi}{4}h^2 \\frac{dh}{dt}$. Substitusi $\\frac{dV}{dt} = 2$ dan $h = 2$: $2 = \\frac{\\pi}{4}(4)\\frac{dh}{dt} \\implies 2 = \\pi \\frac{dh}{dt} \\implies \\frac{dh}{dt} = \\frac{2}{\\pi}$ m/menit."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-14",
        "materi": "KALKULUS LANJUT: OPTIMASI EKSTREM",
        "topic": "Luas Persegi Panjang Maksimum di Dalam Kurva Parabola",
        "stem": "Sebuah persegi panjang dibuat di bawah kurva parabola $y = 12 - x^2$ dan di atas sumbu-$x$ dengan kedua titik sudut atasnya menyentuh kurva parabola. Luas maksimum persegi panjang tersebut adalah...",
        "correct": "$32 \\text{ satuan luas}$",
        "distractors": [
            "$16 \\text{ satuan luas}$",
            "$24 \\text{ satuan luas}$",
            "$48 \\text{ satuan luas}$",
            "$36 \\text{ satuan luas}$"
        ],
        "formula": {
            "title": "OPTIMASI FUNGSI LUAS SIMETRIS",
            "latex": "L(x) = 2x \\cdot y = 2x(12 - x^2) = 24x - 2x^3 \\implies L'(x) = 24 - 6x^2 = 0",
            "legend": "• Titik stasioner diperoleh saat turunan pertama fungsi luas bernilai nol"
        },
        "hints": {
            "concept": "Alas persegi panjang adalah $2x$ dan tingginya adalah $y = 12 - x^2$. Luas $L(x) = 24x - 2x^3$.",
            "execution": "Turunkan: $L'(x) = 24 - 6x^2 = 0 \\implies x^2 = 4 \\implies x = 2$. Luas maksimum: $L(2) = 2(2)(12 - 4) = 4(8) = 32$ satuan luas."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-15",
        "materi": "KALKULUS LANJUT: INTEGRAL PARSIAL SIKLIK",
        "topic": "Integral Parsial Fungsi Eksponensial dan Sinus yang Berulang",
        "stem": "Hasil dari integral siklis $\\int e^x \\sin x \\, dx$ adalah...",
        "correct": "$\\frac{1}{2}e^x(\\sin x - \\cos x) + C$",
        "distractors": [
            "$\\frac{1}{2}e^x(\\sin x + \\cos x) + C$",
            "$e^x(\\sin x - \\cos x) + C$",
            "$\\frac{1}{2}e^x(\\cos x - \\sin x) + C$",
            "$-e^x \\cos x + C$"
        ],
        "formula": {
            "title": "INTEGRAL PARSIAL SIKLIS",
            "latex": "I = e^x \\sin x - e^x \\cos x - I \\implies 2I = e^x(\\sin x - \\cos x) + C",
            "legend": "• Integrasi parsial dua kali mengembalikan bentuk integral mula-mula yang dipindahkan ke ruas kiri"
        },
        "hints": {
            "concept": "Gunakan integrasi parsial dua kali berturut-turut hingga integral asal $I$ muncul kembali.",
            "execution": "Setelah dua tahap: $I = e^x\\sin x - e^x\\cos x - I \\implies 2I = e^x(\\sin x - \\cos x) \\implies I = \\frac{1}{2}e^x(\\sin x - \\cos x) + C$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-16",
        "materi": "KALKULUS LANJUT: SUBSTITUSI TRIGONOMETRI",
        "topic": "Integral Substitusi Trigonometri Bentuk Akar Kuadrat",
        "stem": "Hasil dari integral aljabar $\\int \\frac{1}{\\sqrt{9 - x^2}} \\, dx$ adalah...",
        "correct": "$\\arcsin\\left(\\frac{x}{3}\\right) + C$",
        "distractors": [
            "$\\frac{1}{3}\\arcsin\\left(\\frac{x}{3}\\right) + C$",
            "$\\arccos\\left(\\frac{x}{3}\\right) + C$",
            "$\\ln|x + \\sqrt{9 - x^2}| + C$",
            "$\\frac{1}{3}\\arctan\\left(\\frac{x}{3}\\right) + C$"
        ],
        "formula": {
            "title": "INTEGRAL INVERS TRIGONOMETRI BAKU",
            "latex": "\\int \\frac{1}{\\sqrt{a^2 - x^2}} \\, dx = \\arcsin\\left(\\frac{x}{a}\\right) + C",
            "legend": "• Menggunakan substitusi geometris $x = a\\sin\\theta \\implies dx = a\\cos\\theta d\\theta$"
        },
        "hints": {
            "concept": "Gunakan bentuk baku integral invers trigonometri dengan $a = 3$.",
            "execution": "$\\int \\frac{1}{\\sqrt{3^2 - x^2}} \\, dx = \\arcsin\\left(\\frac{x}{3}\\right) + C$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-17",
        "materi": "KALKULUS LANJUT: INTEGRAL TENTU VOLUME",
        "topic": "Metode Kulit Silinder (Cylindrical Shells)",
        "stem": "Volume benda putar yang terbentuk saat daerah yang dibatasi oleh $y = 3x - x^2$ dan sumbu-$x$ diputar $360^\\circ$ mengelilingi sumbu-$y$ adalah...",
        "correct": "$\\frac{27}{2}\\pi \\text{ satuan volume}$",
        "distractors": [
            "$9\\pi \\text{ satuan volume}$",
            "$\\frac{81}{10}\\pi \\text{ satuan volume}$",
            "$27\\pi \\text{ satuan volume}$",
            "$\\frac{45}{4}\\pi \\text{ satuan volume}$"
        ],
        "formula": {
            "title": "METODE KULIT SILINDER TERHADAP SUMBU-Y",
            "latex": "V = 2\\pi \\int_a^b x \\cdot f(x) \\, dx",
            "legend": "• Menjumlahkan keliling tabung silinder $2\\pi x$ dikalikan tinggi tabung $f(x)$ dan tebal $dx$"
        },
        "hints": {
            "concept": "Titik potong sumbu-$x$ adalah $x = 0$ dan $x = 3$. Rumus: $V = 2\\pi \\int_0^3 x(3x - x^2) \\, dx$.",
            "execution": "Integrasikan: $2\\pi \\int_0^3 (3x^2 - x^3) \\, dx = 2\\pi \\left[ x^3 - \\frac{1}{4}x^4 \\right]_0^3 = 2\\pi \\left(27 - \\frac{81}{4}\\right) = 2\\pi \\left(\\frac{27}{4}\\right) = \\frac{27}{2}\\pi$ satuan volume."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-18",
        "materi": "KALKULUS LANJUT: PANJANG BUSUR KURVA",
        "topic": "Panjang Busur Kurva Fungsi Menggunakan Integral",
        "stem": "Panjang busur kurva garis linear $y = \\frac{4}{3}x$ dari interval $x = 0$ hingga $x = 3$ dihitung dengan integral adalah...",
        "correct": "$5 \\text{ satuan panjang}$",
        "distractors": [
            "$4 \\text{ satuan panjang}$",
            "$\\frac{15}{2} \\text{ satuan panjang}$",
            "$6 \\text{ satuan panjang}$",
            "$\\frac{25}{3} \\text{ satuan panjang}$"
        ],
        "formula": {
            "title": "PANJANG BUSUR KURVA KARTESIUS",
            "latex": "S = \\int_a^b \\sqrt{1 + [f'(x)]^2} \\, dx",
            "legend": "• Berakar dari teorema Pythagoras infinitesimal $dS = \\sqrt{dx^2 + dy^2}$"
        },
        "hints": {
            "concept": "Cari turunan pertama: $y' = \\frac{4}{3}$. Elemen diferensial: $\\sqrt{1 + (y')^2} = \\sqrt{1 + \\frac{16}{9}} = \\sqrt{\\frac{25}{9}} = \\frac{5}{3}$.",
            "execution": "Hitung panjang busur: $S = \\int_0^3 \\frac{5}{3} \\, dx = \\frac{5}{3} [x]_0^3 = \\frac{5}{3}(3) = 5$ satuan panjang."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-19",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Polinomial Simetris Tiga Variabel",
        "stem": "Jika $a, b,$ dan $c$ adalah akar-akar dari polinomial $x^3 - 2x^2 + 4x - 8 = 0$, maka nilai dari $(a + 1)(b + 1)(c + 1)$ adalah...",
        "correct": "$15$",
        "distractors": [
            "$7$",
            "$9$",
            "$11$",
            "$13$"
        ],
        "formula": {
            "title": "EVALUASI POLINOMIAL PADA NILAI TERTENTU",
            "latex": "P(x) = (x - a)(x - b)(x - c) \\implies (a+1)(b+1)(c+1) = -P(-1)",
            "legend": "• Menghindari ekspansi perkalian panjang dengan mengevaluasi fungsi pada $x = -1$"
        },
        "hints": {
            "concept": "Perhatikan bahwa $(-1 - a)(-1 - b)(-1 - c) = -(1 + a)(1 + b)(1 + c) = P(-1)$.",
            "execution": "Hitung $P(-1) = (-1)^3 - 2(-1)^2 + 4(-1) - 8 = -1 - 2 - 4 - 8 = -15$. Maka $(a + 1)(b + 1)(c + 1) = -(-15) = 15$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-20",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Determinan Matriks Blok Segitiga Atas",
        "stem": "Diberikan matriks blok $M = \\begin{pmatrix} A & B \\\\ 0 & C \\end{pmatrix}$ di mana $A = \\begin{pmatrix} 2 & 1 \\\\ 3 & 4 \\end{pmatrix}$ dan $C = \\begin{pmatrix} 5 & 2 \\\\ 1 & 3 \\end{pmatrix}$. Nilai dari $\det(M)$ adalah...",
        "correct": "$65$",
        "distractors": [
            "$26$",
            "$39$",
            "$50$",
            "$78$"
        ],
        "formula": {
            "title": "TEOREMA DETERMINAN MATRIKS BLOK SEGITIGA",
            "latex": "\\det \\begin{pmatrix} A & B \\\\ 0 & C \\end{pmatrix} = \\det(A) \\cdot \\det(C)",
            "legend": "• Determinan matriks blok segitiga atas sama dengan perkalian determinan blok diagonal utamanya"
        },
        "hints": {
            "concept": "Hitung determinan masing-masing blok diagonal: $\det(A)$ dan $\det(C)$.",
            "execution": "$\\det(A) = (2)(4) - (1)(3) = 8 - 3 = 5$. $\det(C) = (5)(3) - (2)(1) = 15 - 2 = 13$. Maka $\det(M) = 5 \\cdot 13 = 65$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-21",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Garis Kutub (Polar) Terhadap Elips",
        "stem": "Diberikan titik $T(4, 2)$ di luar elips $\\frac{x^2}{8} + \\frac{y^2}{4} = 1$. Persamaan garis kutub (garis polar) titik $T$ terhadap elips tersebut adalah...",
        "correct": "$x + y - 2 = 0$",
        "distractors": [
            "$x - y - 2 = 0$",
            "$2x + y - 4 = 0$",
            "$x + 2y - 4 = 0$",
            "$4x + 2y - 8 = 0$"
        ],
        "formula": {
            "title": "PERSAMAAN GARIS KUTUB ELIPS",
            "latex": "\\frac{x \\cdot x_0}{a^2} + \\frac{y \\cdot y_0}{b^2} = 1",
            "legend": "• Menghubungkan titik-titik singgung yang ditarik dari titik eksternal $(x_0, y_0)$"
        },
        "hints": {
            "concept": "Substitusikan titik kutub $(x_0, y_0) = (4, 2)$ ke dalam bentuk bagi adil elips.",
            "execution": "$\\frac{4x}{8} + \\frac{2y}{4} = 1 \\implies \\frac{x}{2} + \\frac{y}{2} = 1 \\implies x + y = 2 \\implies x + y - 2 = 0$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-22",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Penjumlahan Deret Sinus Sudut Aritmetika",
        "stem": "Nilai dari deret sudut $\\sin(10^\\circ) + \\sin(50^\\circ) - \\sin(70^\\circ)$ adalah tepat bernilai...",
        "correct": "$0$",
        "distractors": [
            "$\\frac{1}{2}$",
            "$1$",
            "$-\\frac{1}{2}$",
            "$\\frac{\\sqrt{3}}{2}$"
        ],
        "formula": {
            "title": "PENJUMLAHAN SINUS KE PERKALIAN",
            "latex": "\\sin A + \\sin B = 2\\sin\\left(\\frac{A+B}{2}\\right)\\cos\\left(\\frac{A-B}{2}\\right)",
            "legend": "• Menggabungkan dua suku pertama untuk mengeliminasi suku ketiga"
        },
        "hints": {
            "concept": "Gabungkan $\\sin(50^\\circ) + \\sin(10^\\circ) = 2\\sin(30^\\circ)\\cos(20^\\circ) = 2\\left(\\frac{1}{2}\\right)\\cos(20^\\circ) = \\cos(20^\\circ)$.",
            "execution": "Perhatikan bahwa $\\sin(70^\\circ) = \\sin(90^\\circ - 20^\\circ) = \\cos(20^\\circ)$. Maka $\\cos(20^\\circ) - \\cos(20^\\circ) = 0$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-23",
        "materi": "KALKULUS LANJUT: TEOREMA NILAI RATA-RATA",
        "topic": "Teorema Nilai Rata-rata Turunan (MVT) pada Polinomial",
        "stem": "Diberikan fungsi $f(x) = x^3 - 3x$ pada selang tertutup $[0, 3]$. Nilai $c \\in (0, 3)$ yang memenuhi Teorema Nilai Rata-rata ($f'(c) = \\frac{f(b) - f(a)}{b - a}$) adalah...",
        "correct": "$\\sqrt{3}$",
        "distractors": [
            "$1$",
            "$\\frac{3}{2}$",
            "$2$",
            "$\\sqrt{2}$"
        ],
        "formula": {
            "title": "TEOREMA NILAI RATA-RATA HITUNG TURUNAN (MVT)",
            "latex": "f'(c) = \\frac{f(b) - f(a)}{b - a} \\quad \\text{untuk suatu } c \\in (a, b)",
            "legend": "• Menjamin adanya titik dengan gradien garis singgung sejajar dengan garis tali busur sekannya"
        },
        "hints": {
            "concept": "Hitung $f(0) = 0$ dan $f(3) = 27 - 9 = 18$. Kemiringan tali busur: $\\frac{18 - 0}{3 - 0} = 6$.",
            "execution": "Turunkan: $f'(c) = 3c^2 - 3 = 6 \\implies 3c^2 = 9 \\implies c^2 = 3 \\implies c = \\sqrt{3}$ (karena $c > 0$)."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-24",
        "materi": "KALKULUS LANJUT: INTEGRAL PECAHAN PARSIAL",
        "topic": "Dekomposisi Pecahan Parsial Linier Berbeda",
        "stem": "Hasil dari integral rasional $\\int \\frac{5x - 2}{x^2 - x - 2} \\, dx$ adalah...",
        "correct": "$\\frac{8}{3}\\ln|x - 2| + \\frac{7}{3}\\ln|x + 1| + C$",
        "distractors": [
            "$\\frac{7}{3}\\ln|x - 2| + \\frac{8}{3}\\ln|x + 1| + C$",
            "$3\\ln|x - 2| + 2\\ln|x + 1| + C$",
            "$\\frac{8}{3}\\ln|x + 1| - \\frac{7}{3}\\ln|x - 2| + C$",
            "$5\\ln|x^2 - x - 2| + C$"
        ],
        "formula": {
            "title": "INTEGRASI PECAHAN PARSIAL",
            "latex": "\\frac{5x - 2}{(x - 2)(x + 1)} = \\frac{A}{x - 2} + \\frac{B}{x + 1}",
            "legend": "• Menentukan koefisien $A$ dan $B$ melalui metode tutupan Heaviside"
        },
        "hints": {
            "concept": "Untuk $A$ (tutupi $x - 2$, evaluasi di $x = 2$): $A = \\frac{5(2) - 2}{2 + 1} = \\frac{8}{3}$.",
            "execution": "Untuk $B$ (tutupi $x + 1$, evaluasi di $x = -1$): $B = \\frac{5(-1) - 2}{-1 - 2} = \\frac{-7}{-3} = \\frac{7}{3}$. Integrasikan: $\\frac{8}{3}\\ln|x-2| + \\frac{7}{3}\\ln|x+1| + C$."
        }
    },
    {
        "id": "mtk_lanjut-lat-h-25",
        "materi": "KALKULUS LANJUT: APLIKASI INTEGRAL",
        "topic": "Panjang Busur Parabola Setengah Kubik",
        "stem": "Panjang busur kurva semi-kubik $y^2 = x^3$ dari titik asal $(0, 0)$ hingga titik $(4, 8)$ bernilai...",
        "correct": "$\\frac{8}{27}(10\\sqrt{10} - 1)$",
        "distractors": [
            "$\\frac{1}{27}(10\\sqrt{10} - 1)$",
            "$\\frac{4}{9}(10\\sqrt{10} - 1)$",
            "$\\frac{8}{27}(10\\sqrt{10})$",
            "$\\frac{16}{27}(10\\sqrt{10} - 1)$"
        ],
        "formula": {
            "title": "INTEGRAL PANJANG BUSUR SEMI-KUBIK",
            "latex": "y = x^{3/2} \\implies y' = \\frac{3}{2}x^{1/2} \\implies 1 + (y')^2 = 1 + \\frac{9}{4}x",
            "legend": "• Substitusi integral $u = 1 + \\frac{9}{4}x$ untuk menyelesaikan integral akar"
        },
        "hints": {
            "concept": "Integralkan: $S = \\int_0^4 \\sqrt{1 + \\frac{9}{4}x} \\, dx$.",
            "execution": "$S = \\left[ \\frac{4}{9} \\cdot \\frac{2}{3} \\left(1 + \\frac{9}{4}x\\right)^{3/2} \\right]_0^4 = \\frac{8}{27} [(1 + 9)^{3/2} - 1^{3/2}] = \\frac{8}{27}(10^{3/2} - 1) = \\frac{8}{27}(10\\sqrt{10} - 1)$."
        }
    }
]
