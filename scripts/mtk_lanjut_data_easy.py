# -*- coding: utf-8 -*-
"""
mtk_lanjut_data_easy.py
-----------------------
25 Authentic Latihan Easy items for TKA 2026 Matematika Tingkat Lanjut (SMA/MA Fase F Lanjutan).
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework.
Topics: Polinomial, Matriks 3x3, Irisan Kerucut, Vektor R3, Trigonometri Lanjut, Limit & Turunan.
"""

MTK_LANJUT_EASY_ITEMS = [
    {
        "id": "mtk_lanjut-lat-e-01",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Teorema Sisa Pembagian Polinomial Linear",
        "stem": "Diketahui suku banyak $P(x) = 2x^3 - 5x^2 + 8x - 12$. Sisa pembagian suku banyak $P(x)$ oleh pembagi linear $(x - 3)$ berdasarkan Teorema Sisa adalah...",
        "correct": "$21$",
        "distractors": [
            "$15$",
            "$18$",
            "$24$",
            "$27$"
        ],
        "formula": {
            "title": "TEOREMA SISA POLINOMIAL LINEAR",
            "latex": "P(x) = (x - c) \\cdot H(x) + S \\implies S = P(c)",
            "legend": "• Sisa pembagian suku banyak $P(x)$ oleh pembagi $(x - c)$ tepat bernilai $P(c)$"
        },
        "hints": {
            "concept": "Menurut Teorema Sisa, sisa pembagian $P(x)$ oleh $(x - 3)$ diperoleh dengan menyubstitusikan $x = 3$ langsung ke fungsi $P(x)$.",
            "execution": "Hitung $P(3) = 2(3)^3 - 5(3)^2 + 8(3) - 12 = 2(27) - 5(9) + 24 - 12 = 54 - 45 + 12 = 21$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-02",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Teorema Faktor Polinomial Derajat Tiga",
        "stem": "Suku banyak $P(x) = x^3 + kx^2 - 4x - 12$ memiliki faktor linear $(x + 2)$. Nilai konstanta $k$ yang memenuhi persamaan tersebut adalah...",
        "correct": "$1$",
        "distractors": [
            "$-2$",
            "$0$",
            "$2$",
            "$3$"
        ],
        "formula": {
            "title": "TEOREMA FAKTOR POLINOMIAL",
            "latex": "(x - c) \\text{ faktor dari } P(x) \\iff P(c) = 0",
            "legend": "• Nilai fungsi suku banyak bernilai nol pada pembuat nol dari faktor linearnya"
        },
        "hints": {
            "concept": "Karena $(x + 2)$ adalah faktor, maka nilai $P(-2)$ harus tepat sama dengan nol.",
            "execution": "Substitusikan $x = -2$: $(-2)^3 + k(-2)^2 - 4(-2) - 12 = -8 + 4k + 8 - 12 = 4k - 12 = 0 \\implies 4k = 12 \\implies k = 3$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-03",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Jumlah Akar-akar Persamaan Kubik (Teorema Vieta)",
        "stem": "Akar-akar dari persamaan polinomial kubik $2x^3 - 6x^2 + 11x - 5 = 0$ adalah $x_1, x_2,$ dan $x_3$. Nilai dari hasil penjumlahan seluruh akar $(x_1 + x_2 + x_3)$ adalah...",
        "correct": "$3$",
        "distractors": [
            "$-3$",
            "$\\frac{11}{2}$",
            "$-\\frac{5}{2}$",
            "$\\frac{5}{2}$"
        ],
        "formula": {
            "title": "TEOREMA VIETA SUKU BANYAK DERAJAT TIGA",
            "latex": "ax^3 + bx^2 + cx + d = 0 \\implies x_1 + x_2 + x_3 = -\\frac{b}{a}",
            "legend": "• Jumlah akar tunggal ditentukan oleh perbandingan negatif koefisien derajat kedua terhadap koefisien utama"
        },
        "hints": {
            "concept": "Gunakan hubungan Vieta untuk jumlah akar persamaan kubik: $x_1 + x_2 + x_3 = -\\frac{b}{a}$.",
            "execution": "Dari persamaan, $a = 2, b = -6$. Maka $x_1 + x_2 + x_3 = -\\frac{-6}{2} = \\frac{6}{2} = 3$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-04",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Determinan Matriks Persegi Ordo 3x3 Metode Sarrus",
        "stem": "Diberikan matriks $A = \\begin{pmatrix} 1 & 2 & 0 \\\\ 0 & 3 & 4 \\\\ 2 & 1 & 5 \\end{pmatrix}$. Nilai determinan dari matriks $A$ ($\det(A)$) adalah...",
        "correct": "$23$",
        "distractors": [
            "$15$",
            "$19$",
            "$27$",
            "$31$"
        ],
        "formula": {
            "title": "DETERMINAN MATRIKS 3X3",
            "latex": "\\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})",
            "legend": "• Perhitungan determinan ordo 3 melalui metode ekspansi kofaktor baris pertama"
        },
        "hints": {
            "concept": "Ekspansi kofaktor sepanjang baris pertama: $\det(A) = 1(3\\cdot 5 - 4\\cdot 1) - 2(0\\cdot 5 - 4\\cdot 2) + 0$.",
            "execution": "Hitung: $1(15 - 4) - 2(0 - 8) + 0 = 1(11) - 2(-8) = 11 + 16 = 27$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-05",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Sifat Determinan Perkalian dan Skalar Matriks",
        "stem": "Jika $P$ dan $Q$ adalah matriks berordo $3 \\times 3$ dengan $\det(P) = 4$ dan $\det(Q) = -2$, maka nilai dari $\det(2 \\cdot P \\cdot Q)$ adalah...",
        "correct": "$-64$",
        "distractors": [
            "$-16$",
            "$-32$",
            "$32$",
            "$64$"
        ],
        "formula": {
            "title": "SIFAT DETERMINAN MATRIKS BERORDO n",
            "latex": "\\det(k \\cdot A \\cdot B) = k^n \\cdot \\det(A) \\cdot \\det(B) \\quad (\\text{untuk ordo } n \\times n)",
            "legend": "• Konstanta skalar $k$ keluar dari determinan dengan pangkat senilai ordo matriks $n$"
        },
        "hints": {
            "concept": "Karena ordo matriks adalah $3 \\times 3$ ($n = 3$), maka skalar 2 keluar menjadi $2^3 = 8$. Lalu kalikan dengan $\det(P)$ dan $\det(Q)$.",
            "execution": "Hitung: $\det(2PQ) = 2^3 \\cdot \\det(P) \\cdot \\det(Q) = 8 \\cdot 4 \\cdot (-2) = 32 \\cdot (-2) = -64$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-06",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Titik Puncak dan Fokus Parabola Horizontal",
        "stem": "Diberikan persamaan parabola $y^2 - 4y - 12x + 16 = 0$. Koordinat titik puncak dari parabola tersebut adalah...",
        "correct": "$(1, 2)$",
        "distractors": [
            "$(2, 1)$",
            "$(1, -2)$",
            "$(-1, 2)$",
            "$(4, 2)$"
        ],
        "formula": {
            "title": "BENTUK BAKU PARABOLA HORIZONTAL",
            "latex": "(y - k)^2 = 4p(x - h) \\implies \\text{Puncak } (h, k)",
            "legend": "• $h$: Absis puncak parabola<br>• $k$: Ordinat puncak parabola<br>• $p$: Jarak fokus"
        },
        "hints": {
            "concept": "Ubah persamaan kuadrat ke dalam bentuk kuadrat sempurna untuk variabel $y$: $(y - 2)^2 - 4 - 12x + 16 = 0$.",
            "execution": "$(y - 2)^2 + 12 - 12x = 0 \\implies (y - 2)^2 = 12x - 12 = 12(x - 1)$. Dari sini diperoleh puncak $(h, k) = (1, 2)$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-07",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Panjang Sumbu Mayor dan Minor Elips",
        "stem": "Persamaan elips diberikan oleh $\\frac{x^2}{25} + \\frac{y^2}{9} = 1$. Panjang sumbu mayor ($2a$) dan sumbu minor ($2b$) elips tersebut berturut-turut adalah...",
        "correct": "$10$ dan $6$",
        "distractors": [
            "$5$ dan $3$",
            "$25$ dan $9$",
            "$10$ dan $8$",
            "$8$ dan $6$"
        ],
        "formula": {
            "title": "DIMENSI SUMBU ELIPS HORIZONTAL",
            "latex": "\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1 \\implies \\text{Sumbu Mayor} = 2a, \\quad \\text{Sumbu Minor} = 2b",
            "legend": "• $a = \\sqrt{25} = 5$ (setengah sumbu panjang)<br>• $b = \\sqrt{9} = 3$ (setengah sumbu pendek)"
        },
        "hints": {
            "concept": "Nilai $a^2 = 25 \\implies a = 5$ dan $b^2 = 9 \\implies b = 3$.",
            "execution": "Panjang sumbu mayor adalah $2a = 2(5) = 10$, dan sumbu minor adalah $2b = 2(3) = 6$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-08",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Persamaan Asimtot Hiperbola Horizontal Berpusat di Asal",
        "stem": "Persamaan asimtot dari kurva hiperbola $\\frac{x^2}{16} - \\frac{y^2}{9} = 1$ adalah...",
        "correct": "$y = \\pm \\frac{3}{4}x$",
        "distractors": [
            "$y = \\pm \\frac{4}{3}x$",
            "$y = \\pm \\frac{9}{16}x$",
            "$y = \\pm \\frac{16}{9}x$",
            "$y = \\pm \\frac{3}{5}x$"
        ],
        "formula": {
            "title": "PERSAMAAN ASIMTOT HIPERBOLA",
            "latex": "\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1 \\implies y = \\pm \\frac{b}{a}x",
            "legend": "• Asimtot merupakan garis pemandu yang didekati kurva hiperbola saat menuju tak hingga"
        },
        "hints": {
            "concept": "Dari persamaan hiperbola, $a^2 = 16 \\implies a = 4$ dan $b^2 = 9 \\implies b = 3$.",
            "execution": "Rumus garis asimtot hiperbola horizontal adalah $y = \\pm \\frac{b}{a}x = \\pm \\frac{3}{4}x$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-09",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Perkalian Skalar (Dot Product) Dua Vektor di R3",
        "stem": "Diberikan dua vektor pada ruang tiga dimensi: $\\vec{u} = 2\\hat{i} - 3\\hat{j} + 4\\hat{k}$ dan $\\vec{v} = 5\\hat{i} + 2\\hat{j} - \\hat{k}$. Nilai perkalian skalar $\\vec{u} \\cdot \\vec{v}$ adalah...",
        "correct": "$0$",
        "distractors": [
            "$-4$",
            "$2$",
            "$6$",
            "$12$"
        ],
        "formula": {
            "title": "DOT PRODUCT VEKTOR TIGA DIMENSI",
            "latex": "\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z",
            "legend": "• Menghasilkan skalar; jika bernilai nol menandakan kedua vektor saling tegak lurus (ortogonal)"
        },
        "hints": {
            "concept": "Kalikan komponen-komponen yang seletak lalu jumlahkan seluruh hasilnya.",
            "execution": "$\\vec{u} \\cdot \\vec{v} = (2)(5) + (-3)(2) + (4)(-1) = 10 - 6 - 4 = 0$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-10",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Panjang Proyeksi Skalar Ortogonal",
        "stem": "Diketahui vektor $\\vec{a} = 3\\hat{i} - 4\\hat{j}$ dan $\\vec{b} = 6\\hat{i} + 8\\hat{j}$. Panjang proyeksi skalar ortogonal vektor $\\vec{a}$ pada vektor $\\vec{b}$ adalah...",
        "correct": "$-\\frac{7}{5}$",
        "distractors": [
            "$-2$",
            "$-1$",
            "$\\frac{7}{5}$",
            "$\\frac{14}{5}$"
        ],
        "formula": {
            "title": "PANJANG PROYEKSI SKALAR",
            "latex": "|\\vec{c}| = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|}",
            "legend": "• $|\\vec{b}| = \\sqrt{b_x^2 + b_y^2 + b_z^2}$ adalah modulus atau magnitudo vektor target"
        },
        "hints": {
            "concept": "Hitung perkalian dot $\\vec{a} \\cdot \\vec{b}$ lalu bagi dengan panjang vektor $\\vec{b}$.",
            "execution": "$\\vec{a} \\cdot \\vec{b} = 3(6) + (-4)(8) = 18 - 32 = -14$. Panjang $|\\vec{b}| = \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = 10$. Maka proyeksi skalarnya adalah $\\frac{-14}{10} = -\\frac{7}{5}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-11",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Identitas Sudut Ganda Sinus dan Kosinus",
        "stem": "Jika diketahui $\\sin \\alpha = \\frac{3}{5}$ dengan $\\alpha$ merupakan sudut lancip ($0 < \\alpha < \\frac{\\pi}{2}$), maka nilai dari $\\cos(2\\alpha)$ adalah...",
        "correct": "$\\frac{7}{25}$",
        "distractors": [
            "$\\frac{12}{25}$",
            "$\\frac{16}{25}$",
            "$\\frac{24}{25}$",
            "$-\\frac{7}{25}$"
        ],
        "formula": {
            "title": "IDENTITAS SUDUT GANDA KOSINUS",
            "latex": "\\cos(2\\alpha) = 1 - 2\\sin^2\\alpha = 2\\cos^2\\alpha - 1 = \\cos^2\\alpha - \\sin^2\\alpha",
            "legend": "• Memungkinkan konversi sudut ganda langsung dari nilai fungsi trigonometri sudut tunggal"
        },
        "hints": {
            "concept": "Gunakan bentuk identitas $\\cos(2\\alpha) = 1 - 2\\sin^2\\alpha$ karena nilai $\\sin\\alpha$ sudah diketahui langsung.",
            "execution": "Hitung: $\\cos(2\\alpha) = 1 - 2\\left(\\frac{3}{5}\\right)^2 = 1 - 2\\left(\\frac{9}{25}\\right) = 1 - \\frac{18}{25} = \\frac{7}{25}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-12",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Penjumlahan Sudut Tangen",
        "stem": "Diketahui $\\tan A = \\frac{1}{2}$ dan $\\tan B = \\frac{1}{3}$. Nilai dari $\\tan(A + B)$ adalah...",
        "correct": "$1$",
        "distractors": [
            "$\\frac{5}{6}$",
            "$\\frac{2}{3}$",
            "$\\frac{5}{7}$",
            "$\\sqrt{3}$"
        ],
        "formula": {
            "title": "RUMUS JUMLAH SUDUT TANGEN",
            "latex": "\\tan(A + B) = \\frac{\\tan A + \\tan B}{1 - \\tan A \\cdot \\tan B}",
            "legend": "• Konversi jumlahan sudut tangen menjadi rasio aljabar nilai tangen masing-masing sudut"
        },
        "hints": {
            "concept": "Substitusikan nilai $\\tan A = \\frac{1}{2}$ dan $\\tan B = \\frac{1}{3}$ ke dalam formula jumlahan tangen.",
            "execution": "$\\tan(A + B) = \\frac{\\frac{1}{2} + \\frac{1}{3}}{1 - (\\frac{1}{2})(\\frac{1}{3})} = \\frac{\\frac{5}{6}}{1 - \\frac{1}{6}} = \\frac{\\frac{5}{6}}{\\frac{5}{6}} = 1$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-13",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Konversi Bentuk a cos x + b sin x = k cos(x - alpha)",
        "stem": "Bentuk $f(x) = \\sqrt{3}\\cos x + \\sin x$ dapat dinyatakan dalam bentuk ekuivalen $k \\cos(x - \\alpha)$. Nilai konstanta amplitudo $k$ dan sudut fase $\\alpha$ (dalam radian) adalah...",
        "correct": "$k = 2, \\quad \\alpha = \\frac{\\pi}{6}$",
        "distractors": [
            "$k = 2, \\quad \\alpha = \\frac{\\pi}{3}$",
            "$k = 4, \\quad \\alpha = \\frac{\\pi}{6}$",
            "$k = \\sqrt{2}, \\quad \\alpha = \\frac{\\pi}{4}$",
            "$k = 2, \\quad \\alpha = \\frac{\\pi}{4}$"
        ],
        "formula": {
            "title": "TRANSFORMASI FUNGSI KOSINUS-SINUS",
            "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha) \\implies k = \\sqrt{a^2 + b^2}, \\quad \\tan\\alpha = \\frac{b}{a}",
            "legend": "• $k$: Modulus amplitudo gelombang gabungan<br>• $\\alpha$: Pergeseran fase sudut di kuadran bersesuaian"
        },
        "hints": {
            "concept": "Ambil $a = \\sqrt{3}$ dan $b = 1$. Hitung $k = \\sqrt{a^2 + b^2}$ dan $\\tan\\alpha = \\frac{b}{a}$.",
            "execution": "$k = \\sqrt{(\\sqrt{3})^2 + 1^2} = \\sqrt{3 + 1} = \\sqrt{4} = 2$. Karena $a > 0$ dan $b > 0$, $\\alpha$ di Kuadran I: $\\tan\\alpha = \\frac{1}{\\sqrt{3}} \\implies \\alpha = 30^\\circ = \\frac{\\pi}{6}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-14",
        "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
        "topic": "Limit Dasar Bentuk Tak Tentu Sinus",
        "stem": "Nilai dari limit trigonometri dasar $\\lim_{x \\to 0} \\frac{\\sin(6x)}{2x}$ adalah...",
        "correct": "$3$",
        "distractors": [
            "$1$",
            "$2$",
            "$6$",
            "$\\frac{1}{3}$"
        ],
        "formula": {
            "title": "TEOREMA LIMIT TRIGONOMETRI DASAR",
            "latex": "\\lim_{x \\to 0} \\frac{\\sin(ax)}{bx} = \\frac{a}{b}",
            "legend": "• Berlaku untuk fungsi sinus dan tangen saat variabel $x$ mendekati nilai nol"
        },
        "hints": {
            "concept": "Gunakan teorema limit trigonometri khusus: $\\lim_{x \\to 0} \\frac{\\sin(ax)}{bx} = \\frac{a}{b}$.",
            "execution": "Ambil $a = 6$ dan $b = 2$, maka nilainya adalah $\\frac{6}{2} = 3$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-15",
        "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
        "topic": "Limit Bentuk 1 - cos(kx) per x kuadrat",
        "stem": "Nilai limit fungsi trigonometri $\\lim_{x \\to 0} \\frac{1 - \\cos(4x)}{x^2}$ bernilai tepat sama dengan...",
        "correct": "$8$",
        "distractors": [
            "$2$",
            "$4$",
            "$16$",
            "$32$"
        ],
        "formula": {
            "title": "LIMIT IDENTITAS SUDUT KOSINUS",
            "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
            "legend": "• Hasil penjabaran identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$"
        },
        "hints": {
            "concept": "Berdasarkan formula standar limit: $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$.",
            "execution": "Untuk $k = 4$, hitung: $\\frac{4^2}{2} = \\frac{16}{2} = 8$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-16",
        "materi": "KALKULUS LANJUT: LIMIT TAK HINGGA",
        "topic": "Limit di Ketakhinggaan Fungsi Rasional Aljabar",
        "stem": "Nilai dari $\\lim_{x \\to \\infty} \\frac{4x^3 - 5x + 7}{2x^3 + 3x^2 - 1}$ adalah...",
        "correct": "$2$",
        "distractors": [
            "$0$",
            "$\\frac{4}{3}$",
            "$4$",
            "$\\infty$"
        ],
        "formula": {
            "title": "LIMIT ASIMTOTIK FUNGSI RASIONAL",
            "latex": "\\lim_{x \\to \\infty} \\frac{a_n x^n + \\dots}{b_m x^m + \\dots} = \\begin{cases} \\frac{a_n}{b_m}, & n = m \\\\ 0, & n < m \\\\ \\infty, & n > m \\end{cases}",
            "legend": "• Ditentukan oleh rasio koefisien pangkat tertinggi saat derajat pembilang sama dengan penyebut"
        },
        "hints": {
            "concept": "Karena derajat tertinggi pembilang dan penyebut sama-sama 3 ($n = m = 3$), bagi pembilang dan penyebut dengan $x^3$.",
            "execution": "Rasio koefisien pangkat tertinggi adalah $\\frac{4}{2} = 2$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-17",
        "materi": "KALKULUS LANJUT: LIMIT TAK HINGGA",
        "topic": "Limit Selisih Bentuk Akar Kuadrat di Ketakhinggaan",
        "stem": "Nilai dari limit aljabar $\\lim_{x \\to \\infty} \\left( \\sqrt{x^2 + 6x - 2} - \\sqrt{x^2 - 4x + 5} \\right)$ adalah...",
        "correct": "$5$",
        "distractors": [
            "$1$",
            "$2$",
            "$10$",
            "$\\infty$"
        ],
        "formula": {
            "title": "LIMIT SELISIH AKAR KUADRAT TAK HINGGA",
            "latex": "\\lim_{x \\to \\infty} \\left(\\sqrt{ax^2 + bx + c} - \\sqrt{ax^2 + px + q}\\right) = \\frac{b - p}{2\\sqrt{a}} \\quad (a > 0)",
            "legend": "• Menghitung nilai limit seketika tanpa perlu mengalikan sekawan panjang"
        },
        "hints": {
            "concept": "Gunakan rumus cepat limit selisih bentuk akar kuadrat: $L = \\frac{b - p}{2\\sqrt{a}}$.",
            "execution": "Dari soal, $a = 1, b = 6, p = -4$. Maka $L = \\frac{6 - (-4)}{2\\sqrt{1}} = \\frac{10}{2} = 5$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-18",
        "materi": "KALKULUS LANJUT: TURUNAN TRIGONOMETRI",
        "topic": "Turunan Pertama Fungsi Komposisi Sinus Kuadrat",
        "stem": "Turunan pertama dari fungsi $f(x) = \\sin^2(3x)$ terhadap variabel $x$ adalah...",
        "correct": "$3\\sin(6x)$",
        "distractors": [
            "$6\\sin(3x)$",
            "$2\\sin(3x)\\cos(3x)$",
            "$6\\cos(3x)$",
            "$3\\cos(6x)$"
        ],
        "formula": {
            "title": "ATURAN RANTAI TURUNAN TRIGONOMETRI",
            "latex": "\\frac{d}{dx}[\\sin^n(u)] = n\\sin^{n-1}(u) \\cdot \\cos(u) \\cdot u'",
            "legend": "• Mengombinasikan diferensiasi fungsi pangkat terluar, fungsi trigonometri, dan fungsi sudut terdalam"
        },
        "hints": {
            "concept": "Terapkan aturan rantai: turunkan pangkat 2 terlebih dahulu, lalu turunkan fungsi $\\sin$, lalu turunkan sudut $3x$.",
            "execution": "$f'(x) = 2\\sin(3x) \\cdot \\cos(3x) \\cdot 3 = 3 \\cdot (2\\sin(3x)\\cos(3x)) = 3\\sin(6x)$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-19",
        "materi": "KALKULUS LANJUT: TURUNAN TRIGONOMETRI",
        "topic": "Persamaan Garis Singgung Kurva Fungsi Trigonometri",
        "stem": "Gradien garis singgung kurva fungsi $y = \\tan(2x)$ di titik berabsis $x = \\frac{\\pi}{8}$ adalah...",
        "correct": "$4$",
        "distractors": [
            "$1$",
            "$2$",
            "$2\\sqrt{2}$",
            "$8$"
        ],
        "formula": {
            "title": "GRADIEN GARIS SINGGUNG KURVA",
            "latex": "m = f'(x_0) \\quad \\text{dengan} \\quad \\frac{d}{dx}[\\tan(kx)] = k\\sec^2(kx)",
            "legend": "• Nilai gradien $m$ adalah turunan pertama fungsi yang dievaluasi pada titik singgung"
        },
        "hints": {
            "concept": "Cari turunan pertama $y' = 2\\sec^2(2x)$, lalu evaluasi pada $x = \\frac{\\pi}{8}$.",
            "execution": "$y'\\left(\\frac{\\pi}{8}\\right) = 2\\sec^2\\left(2 \\cdot \\frac{\\pi}{8}\\right) = 2\\sec^2\\left(\\frac{\\pi}{4}\\right) = 2 \\cdot (\\sqrt{2})^2 = 2 \\cdot 2 = 4$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-20",
        "materi": "KALKULUS LANJUT: INTEGRAL SUBSTITUSI",
        "topic": "Integral Substitusi Aljabar Sederhana",
        "stem": "Hasil dari integral tak tentu $\\int 2x(x^2 + 5)^4 \\, dx$ adalah...",
        "correct": "$\\frac{1}{5}(x^2 + 5)^5 + C$",
        "distractors": [
            "$\\frac{1}{4}(x^2 + 5)^5 + C$",
            "$(x^2 + 5)^5 + C$",
            "$\\frac{2}{5}(x^2 + 5)^5 + C$",
            "$\\frac{1}{10}(x^2 + 5)^5 + C$"
        ],
        "formula": {
            "title": "INTEGRAL DENGAN TEKNIK SUBSTITUSI",
            "latex": "\\int f(g(x))g'(x) \\, dx = \\int f(u) \\, du \\quad \\text{dengan } u = g(x)",
            "legend": "• Menyederhanakan perkalian fungsi dengan turunan bagian dalamnya menjadi integral tunggal"
        },
        "hints": {
            "concept": "Misalkan $u = x^2 + 5$, maka $du = 2x \\, dx$. Bentuk integral berubah menjadi $\\int u^4 \\, du$.",
            "execution": "$\\int u^4 \\, du = \\frac{1}{5}u^5 + C = \\frac{1}{5}(x^2 + 5)^5 + C$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-21",
        "materi": "KALKULUS LANJUT: INTEGRAL PARSIAL",
        "topic": "Integral Parsial Fungsi Perkalian Aljabar dan Eksponensial",
        "stem": "Hasil dari $\\int x e^{2x} \\, dx$ menggunakan metode integral parsial adalah...",
        "correct": "$\\frac{1}{2}x e^{2x} - \\frac{1}{4}e^{2x} + C$",
        "distractors": [
            "$\\frac{1}{2}x e^{2x} + \\frac{1}{4}e^{2x} + C$",
            "$x e^{2x} - \\frac{1}{2}e^{2x} + C$",
            "$\\frac{1}{2}x e^{2x} - \\frac{1}{2}e^{2x} + C$",
            "$\\frac{1}{4}x e^{2x} - \\frac{1}{4}e^{2x} + C$"
        ],
        "formula": {
            "title": "FORMULA INTEGRAL PARSIAL",
            "latex": "\\int u \\, dv = u \\cdot v - \\int v \\, du",
            "legend": "• Pemilihan $u$ mengikuti urutan LIATE (Logaritma, Invers trigonometri, Aljabar, Trigonometri, Eksponensial)"
        },
        "hints": {
            "concept": "Pilih $u = x \\implies du = dx$ dan $dv = e^{2x} \\, dx \\implies v = \\frac{1}{2}e^{2x}$.",
            "execution": "$\\int x e^{2x} \\, dx = x\\left(\\frac{1}{2}e^{2x}\\right) - \\int \\frac{1}{2}e^{2x} \\, dx = \\frac{1}{2}x e^{2x} - \\frac{1}{4}e^{2x} + C$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-22",
        "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
        "topic": "Luas Daerah di Bawah Kurva Parabola dan Sumbu-X",
        "stem": "Luas daerah tertutup yang dibatasi oleh kurva parabola $y = 6x - x^2$ dan sumbu-$x$ adalah...",
        "correct": "$36 \\text{ satuan luas}$",
        "distractors": [
            "$18 \\text{ satuan luas}$",
            "$24 \\text{ satuan luas}$",
            "$48 \\text{ satuan luas}$",
            "$72 \\text{ satuan luas}$"
        ],
        "formula": {
            "title": "LUAS DAERAH KURVA PARABOLA",
            "latex": "L = \\int_0^6 (6x - x^2) \\, dx = \\frac{D\\sqrt{D}}{6a^2}",
            "legend": "• Dapat dihitung melalui integral tentu dari batas titik potong sumbu-$x$ atau rumus diskriminan Archimedes"
        },
        "hints": {
            "concept": "Titik potong sumbu-$x$: $6x - x^2 = 0 \\implies x(6 - x) = 0 \\implies x = 0$ dan $x = 6$.",
            "execution": "Hitung integral: $\\left[ 3x^2 - \\frac{1}{3}x^3 \\right]_0^6 = 3(36) - \\frac{1}{3}(216) = 108 - 72 = 36$ satuan luas."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-23",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Pembagian Polinomial dengan Skema Horner",
        "stem": "Jika suku banyak $P(x) = 3x^4 - 2x^2 + 5x - 7$ dibagi oleh $(x + 1)$, hasil bagi yang diperoleh adalah...",
        "correct": "$3x^3 - 3x^2 + x + 4$",
        "distractors": [
            "$3x^3 + 3x^2 + x + 4$",
            "$3x^3 - 3x^2 - x + 4$",
            "$3x^3 - 2x^2 + 5x + 4$",
            "$3x^3 - 3x^2 + 4x - 1$"
        ],
        "formula": {
            "title": "SKEMA PEMBAGIAN HORNER",
            "latex": "P(x) = (x - c)H(x) + S",
            "legend": "• Koefisien $H(x)$ diperoleh dari baris bawah proses sintesis Horner berurutan"
        },
        "hints": {
            "concept": "Tulis koefisien lengkap berderajat 4 ke 0: $[3, 0, -2, 5, -7]$ dengan pembagi $c = -1$.",
            "execution": "Horner: turunkan 3; $(-1)(3) = -3$; $0 + (-3) = -3$; $(-1)(-3) = 3$; $-2 + 3 = 1$; $(-1)(1) = -1$; $5 + (-1) = 4$. Hasil bagi berderajat 3: $3x^3 - 3x^2 + x + 4$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-24",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Invers Matriks 2x2 Dasar Lanjutan",
        "stem": "Invers dari matriks $M = \\begin{pmatrix} 4 & 7 \\\\ 1 & 2 \\end{pmatrix}$ adalah...",
        "correct": "$\\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$",
        "distractors": [
            "$\\begin{pmatrix} 2 & 7 \\\\ 1 & 4 \\end{pmatrix}$",
            "$\\begin{pmatrix} -2 & 7 \\\\ 1 & -4 \\end{pmatrix}$",
            "$\\begin{pmatrix} 4 & -7 \\\\ -1 & 2 \\end{pmatrix}$",
            "$\\begin{pmatrix} 1 & -7 \\\\ -2 & 4 \\end{pmatrix}$"
        ],
        "formula": {
            "title": "INVERS MATRIKS ORDO 2X2",
            "latex": "M^{-1} = \\frac{1}{\\det(M)} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}",
            "legend": "• Menukar elemen diagonal utama dan mengalikan elemen diagonal samping dengan negatif satu"
        },
        "hints": {
            "concept": "Hitung determinan: $\det(M) = (4)(2) - (7)(1) = 8 - 7 = 1$.",
            "execution": "Karena determinannya bernilai 1, matriks inversnya langsung adalah matriks adjoinnya: $\\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-e-25",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Vektor Satuan Searah Vektor Tertentu",
        "stem": "Vektor satuan yang searah dengan vektor $\\vec{w} = 2\\hat{i} - 2\\hat{j} + \\hat{k}$ adalah...",
        "correct": "$\\frac{2}{3}\\hat{i} - \\frac{2}{3}\\hat{j} + \\frac{1}{3}\\hat{k}$",
        "distractors": [
            "$\\frac{2}{9}\\hat{i} - \\frac{2}{9}\\hat{j} + \\frac{1}{9}\\hat{k}$",
            "$\\frac{1}{3}\\hat{i} - \\frac{1}{3}\\hat{j} + \\frac{1}{3}\\hat{k}$",
            "$2\\hat{i} - 2\\hat{j} + \\hat{k}$",
            "$\\frac{2}{\\sqrt{5}}\\hat{i} - \\frac{2}{\\sqrt{5}}\\hat{j} + \\frac{1}{\\sqrt{5}}\\hat{k}$"
        ],
        "formula": {
            "title": "VEKTOR SATUAN (UNIT VECTOR)",
            "latex": "\\hat{e}_w = \\frac{\\vec{w}}{|\\vec{w}|} = \\frac{w_x\\hat{i} + w_y\\hat{j} + w_z\\hat{k}}{\\sqrt{w_x^2 + w_y^2 + w_z^2}}",
            "legend": "• Memiliki besar tepat satu satuan panjang dan mempertahankan arah vektor asal"
        },
        "hints": {
            "concept": "Hitung panjang vektor $|\\vec{w}| = \\sqrt{2^2 + (-2)^2 + 1^2} = \\sqrt{4 + 4 + 1} = \\sqrt{9} = 3$.",
            "execution": "Bagi setiap komponen vektor dengan 3: $\\hat{e} = \\frac{2}{3}\\hat{i} - \\frac{2}{3}\\hat{j} + \\frac{1}{3}\\hat{k}$."
        }
    }
]
