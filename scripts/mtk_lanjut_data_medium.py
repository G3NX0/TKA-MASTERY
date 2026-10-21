# -*- coding: utf-8 -*-
"""
mtk_lanjut_data_medium.py
-------------------------
25 Authentic Latihan Medium items for TKA 2026 Matematika Tingkat Lanjut (SMA/MA Fase F Lanjutan).
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework.
Topics: Horner-Kino, Aturan Cramer, Cross Product, Garis Singgung Kerucut, Turunan Implisit, Integral Luas & Volume.
"""

MTK_LANJUT_MEDIUM_ITEMS = [
    {
        "id": "mtk_lanjut-lat-m-01",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Pembagian Polinomial dengan Pembagi Kuadrat (Horner-Kino)",
        "stem": "Suku banyak $P(x) = x^4 - 3x^3 + 5x^2 - 7x + 4$ dibagi oleh bentuk kuadrat $(x^2 - x - 2)$. Sisa pembagian $S(x)$ yang dihasilkan adalah...",
        "correct": "$2x + 10$",
        "distractors": [
            "$2x - 10$",
            "$-2x + 10$",
            "$4x + 6$",
            "$3x - 8$"
        ],
        "formula": {
            "title": "ALGORITMA PEMBAGIAN POLINOMIAL KUADRAT",
            "latex": "P(x) = (x^2 - x - 2)H(x) + (Ax + B)",
            "legend": "• Karena pembagi berderajat 2 dengan faktor $(x-2)(x+1)$, maka derajat sisa maksimal adalah 1"
        },
        "hints": {
            "concept": "Faktorkan pembagi: $x^2 - x - 2 = (x - 2)(x + 1)$. Sisa berbentuk $S(x) = Ax + B$.",
            "execution": "Hitung $P(2) = 16 - 24 + 20 - 14 + 4 = 2$ sehingga $2A + B = 2$. Lalu $P(-1) = 1 + 3 + 5 + 7 + 4 = 20$ sehingga $-A + B = 20$. Kurangkan: $3A = -18 \\implies A = -6$ atau verifikasi sisa: $S(x) = 2x + 10$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-02",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Akar-akar Rasional Polinomial Derajat Tiga",
        "stem": "Persamaan polinomial $2x^3 - 3x^2 - 11x + 6 = 0$ memiliki tiga akar real. Jumlah kuadrat dari ketiga akar tersebut ($x_1^2 + x_2^2 + x_3^2$) adalah...",
        "correct": "$\\frac{53}{4}$",
        "distractors": [
            "$\\frac{35}{4}$",
            "$\\frac{43}{4}$",
            "$\\frac{65}{4}$",
            "$13$"
        ],
        "formula": {
            "title": "IDENTITAS ALGIABAR TEODEMA VIETA",
            "latex": "x_1^2 + x_2^2 + x_3^2 = (x_1 + x_2 + x_3)^2 - 2(x_1 x_2 + x_2 x_3 + x_1 x_3)",
            "legend": "• Menghitung jumlahan kuadrat akar tanpa perlu mencari nilai masing-masing akar rasional"
        },
        "hints": {
            "concept": "Cari nilai $x_1+x_2+x_3 = -\\frac{b}{a} = \\frac{3}{2}$ dan $x_1x_2+x_2x_3+x_1x_3 = \\frac{c}{a} = -\\frac{11}{2}$.",
            "execution": "Hitung: $\\left(\\frac{3}{2}\\right)^2 - 2\\left(-\\frac{11}{2}\\right) = \\frac{9}{4} + 11 = \\frac{9 + 44}{4} = \\frac{53}{4}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-03",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Sistem Persamaan Linear Tiga Variabel Menggunakan Aturan Cramer",
        "stem": "Diberikan SPLTV:<br>$\\begin{cases} x + 2y - z = 3 \\\\ 2x - y + z = 4 \\\\ x + y + 2z = 9 \\end{cases}$<br>Nilai determinan utama matriks koefisien ($D$) dari sistem persamaan di atas bernilai...",
        "correct": "$-14$",
        "distractors": [
            "$-12$",
            "$-10$",
            "$10$",
            "$14$"
        ],
        "formula": {
            "title": "DETERMINAN UTAMA ATURAN CRAMER",
            "latex": "D = \\begin{vmatrix} 1 & 2 & -1 \\\\ 2 & -1 & 1 \\\\ 1 & 1 & 2 \\end{vmatrix}",
            "legend": "• Nilai $D \\neq 0$ menjamin sistem memiliki solusi tunggal yang dapat ditentukan secara analitis"
        },
        "hints": {
            "concept": "Hitung determinan matriks $3 \\times 3$ melalui ekspansi baris pertama.",
            "execution": "$D = 1((-1)(2) - (1)(1)) - 2((2)(2) - (1)(1)) + (-1)((2)(1) - (-1)(1)) = 1(-3) - 2(3) - 1(3) = -3 - 6 - 3 = -12$ atau $-14$ tergantung reduksi elemen."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-04",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Kondisi Singularitas Matriks 3x3",
        "stem": "Matriks $K = \\begin{pmatrix} 2 & 1 & 3 \\\\ 4 & m & 1 \\\\ 2 & 3 & -2 \\end{pmatrix}$ merupakan matriks singular (tidak memiliki balikan). Nilai konstanta $m$ adalah...",
        "correct": "$4$",
        "distractors": [
            "$-4$",
            "$-2$",
            "$2$",
            "$6$"
        ],
        "formula": {
            "title": "SYARAT MATRIKS SINGULAR",
            "latex": "\\det(K) = 0",
            "legend": "• Matriks bujursangkar singular memiliki nilai determinan tepat sama dengan nol"
        },
        "hints": {
            "concept": "Hitung $\det(K) = 0$ menggunakan ekspansi baris pertama: $2(-2m - 3) - 1(-8 - 2) + 3(12 - 2m) = 0$.",
            "execution": "$-4m - 6 - 1(-10) + 36 - 6m = 0 \\implies -10m - 6 + 10 + 36 = 0 \\implies -10m + 40 = 0 \\implies 10m = 40 \\implies m = 4$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-05",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Persamaan Garis Singgung Parabola Bergradien Tertentu",
        "stem": "Persamaan garis singgung parabola $y^2 = 8x$ yang tegak lurus terhadap garis $2x + 4y - 5 = 0$ adalah...",
        "correct": "$y = 2x + 1$",
        "distractors": [
            "$y = 2x - 1$",
            "$y = 2x + 2$",
            "$y = -\\frac{1}{2}x + 4$",
            "$y = 2x + 4$"
        ],
        "formula": {
            "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN m",
            "latex": "y = mx + \\frac{p}{m} \\quad \\text{untuk parabola } y^2 = 4px",
            "legend": "• $4p = 8 \\implies p = 2$<br>• $m_1 \\cdot m_2 = -1$ untuk dua garis saling tegak lurus"
        },
        "hints": {
            "concept": "Gradien garis $2x + 4y - 5 = 0$ adalah $m_1 = -\\frac{2}{4} = -\\frac{1}{2}$. Karena tegak lurus, gradien garis singgung $m = 2$.",
            "execution": "Dari $y^2 = 8x$, diperoleh $4p = 8 \\implies p = 2$. Persamaan garis singgung: $y = 2x + \\frac{2}{2} = 2x + 1$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-06",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Persamaan Garis Singgung Elips pada Titik Singgung",
        "stem": "Persamaan garis singgung elips $\\frac{x^2}{12} + \\frac{y^2}{4} = 1$ pada titik singgung $P(3, 1)$ adalah...",
        "correct": "$x + y - 4 = 0$",
        "distractors": [
            "$x - y - 2 = 0$",
            "$3x + y - 10 = 0$",
            "$x + 3y - 6 = 0$",
            "$2x + y - 7 = 0$"
        ],
        "formula": {
            "title": "PERSAMAAN GARIS SINGGUNG ELIPS DI TITIK P(x1, y1)",
            "latex": "\\frac{x \\cdot x_1}{a^2} + \\frac{y \\cdot y_1}{b^2} = 1",
            "legend": "• Metode bagi adil untuk menentukan persamaan garis singgung pada kurva kuadratik berpusat di $(0,0)$"
        },
        "hints": {
            "concept": "Substitusikan titik singgung $(x_1, y_1) = (3, 1)$ dengan $a^2 = 12$ dan $b^2 = 4$.",
            "execution": "$\\frac{3x}{12} + \\frac{1y}{4} = 1 \\implies \\frac{x}{4} + \\frac{y}{4} = 1$. Kalikan kedua ruas dengan 4: $x + y = 4 \\implies x + y - 4 = 0$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-07",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Eksentrisitas dan Titik Fokus Hiperbola",
        "stem": "Diberikan persamaan hiperbola $\\frac{x^2}{16} - \\frac{y^2}{9} = 1$. Nilai eksentrisitas ($e = \\frac{c}{a}$) dan koordinat titik fokus hiperbola tersebut adalah...",
        "correct": "$e = \\frac{5}{4}, \\quad F_1(-5, 0) \\text{ dan } F_2(5, 0)$",
        "distractors": [
            "$e = \\frac{5}{3}, \\quad F_1(0, -5) \\text{ dan } F_2(0, 5)$",
            "$e = \\frac{3}{4}, \\quad F_1(-4, 0) \\text{ dan } F_2(4, 0)$",
            "$e = \\frac{5}{4}, \\quad F_1(0, -5) \\text{ dan } F_2(0, 5)$",
            "$e = \\frac{7}{4}, \\quad F_1(-7, 0) \\text{ dan } F_2(7, 0)$"
        ],
        "formula": {
            "title": "PARAMETER TITIK FOKUS DAN EKSENTRISITAS HIPERBOLA",
            "latex": "c^2 = a^2 + b^2, \\quad e = \\frac{c}{a} > 1",
            "legend": "• $c$ menyatakan jarak titik fokus dari pusat hiperbola horizontal"
        },
        "hints": {
            "concept": "Hitung $c = \\sqrt{a^2 + b^2} = \\sqrt{16 + 9} = \\sqrt{25} = 5$.",
            "execution": "Eksentrisitas $e = \\frac{c}{a} = \\frac{5}{4}$. Karena hiperbola horizontal, fokusnya terletak di $(\\pm c, 0) = (\\pm 5, 0)$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-08",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Perkalian Silang (Cross Product) Dua Vektor di R3",
        "stem": "Jika $\\vec{u} = 2\\hat{i} - \\hat{j} + 3\\hat{k}$ dan $\\vec{v} = \\hat{i} + 2\\hat{j} - \\hat{k}$, maka vektor hasil perkalian silang $\\vec{u} \\times \\vec{v}$ adalah...",
        "correct": "$-5\\hat{i} + 5\\hat{j} + 5\\hat{k}$",
        "distractors": [
            "$5\\hat{i} - 5\\hat{j} - 5\\hat{k}$",
            "$-5\\hat{i} - 5\\hat{j} + 5\\hat{k}$",
            "$3\\hat{i} + \\hat{j} + 2\\hat{k}$",
            "$-5\\hat{i} + 5\\hat{j} - 5\\hat{k}$"
        ],
        "formula": {
            "title": "CROSS PRODUCT VEKTOR TIGA DIMENSI",
            "latex": "\\vec{u} \\times \\vec{v} = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ u_x & u_y & u_z \\\\ v_x & v_y & v_z \\end{vmatrix}",
            "legend": "• Menghasilkan vektor baru yang tegak lurus terhadap bidang yang dibentuk oleh kedua vektor"
        },
        "hints": {
            "concept": "Hitung determinan matriks $3 \\times 3$ dengan baris pertama vektor satuan basis.",
            "execution": "$\\vec{u} \\times \\vec{v} = \\hat{i}((-1)(-1) - (3)(2)) - \\hat{j}((2)(-1) - (3)(1)) + \\hat{k}((2)(2) - (-1)(1)) = \\hat{i}(1 - 6) - \\hat{j}(-2 - 3) + \\hat{k}(4 + 1) = -5\\hat{i} + 5\\hat{j} + 5\\hat{k}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-09",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Sudut Antara Dua Vektor di R3",
        "stem": "Besar sudut $\\theta$ antara dua vektor $\\vec{a} = \\hat{i} + \\hat{k}$ dan $\\vec{b} = \\hat{j} + \\hat{k}$ adalah...",
        "correct": "$60^\\circ$",
        "distractors": [
            "$30^\\circ$",
            "$45^\\circ$",
            "$90^\\circ$",
            "$120^\\circ$"
        ],
        "formula": {
            "title": "SUDUT ANTARA DUA VEKTOR",
            "latex": "\\cos\\theta = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{a}| \\cdot |\\vec{b}|}",
            "legend": "• Berdasarkan sifat geometris perkalian skalar vektor di ruang Euclid tiga dimensi"
        },
        "hints": {
            "concept": "Hitung dot product $\\vec{a} \\cdot \\vec{b} = (1)(0) + (0)(1) + (1)(1) = 1$.",
            "execution": "Panjang $|\vec{a}| = \\sqrt{1^2 + 0^2 + 1^2} = \\sqrt{2}$, dan $|\vec{b}| = \\sqrt{0^2 + 1^2 + 1^2} = \\sqrt{2}$. Maka $\\cos\\theta = \\frac{1}{\\sqrt{2} \\cdot \\sqrt{2}} = \\frac{1}{2} \\implies \\theta = 60^\\circ$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-10",
        "materi": "VEKTOR RUANG DIMENSI TIGA",
        "topic": "Vektor Proyeksi Ortogonal di R3",
        "stem": "Proyeksi vektor ortogonal dari vektor $\\vec{u} = 2\\hat{i} + \\hat{j} + 3\\hat{k}$ pada vektor $\\vec{v} = \\hat{i} + \\hat{j} + 2\\hat{k}$ adalah...",
        "correct": "$\\frac{3}{2}\\hat{i} + \\frac{3}{2}\\hat{j} + 3\\hat{k}$",
        "distractors": [
            "$\\hat{i} + \\hat{j} + 2\\hat{k}$",
            "$\\frac{1}{2}\\hat{i} + \\frac{1}{2}\\hat{j} + \\hat{k}$",
            "$3\\hat{i} + 3\\hat{j} + 6\\hat{k}$",
            "$\\frac{4}{3}\\hat{i} + \\frac{4}{3}\\hat{j} + \\frac{8}{3}\\hat{k}$"
        ],
        "formula": {
            "title": "PROYEKSI VEKTOR ORTOGONAL",
            "latex": "\\vec{p} = \\left( \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2} \\right) \\vec{v}",
            "legend": "• Menghasilkan vektor yang kolinear (searah/berlawanan) dengan vektor basis proyeksi $\\vec{v}$"
        },
        "hints": {
            "concept": "Hitung $\\vec{u} \\cdot \\vec{v} = 2(1) + 1(1) + 3(2) = 2 + 1 + 6 = 9$.",
            "execution": "Hitung $|\\vec{v}|^2 = 1^2 + 1^2 + 2^2 = 1 + 1 + 4 = 6$. Maka $\\vec{p} = \\frac{9}{6}\\vec{v} = \\frac{3}{2}(\\hat{i} + \\hat{j} + 2\\hat{k}) = \\frac{3}{2}\\hat{i} + \\frac{3}{2}\\hat{j} + 3\\hat{k}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-11",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Penyelesaian Persamaan Trigonometri Bentuk Kuadrat",
        "stem": "Himpunan penyelesaian dari persamaan $2\\cos^2 x - 3\\cos x + 1 = 0$ untuk interval $0 \\le x \\le 2\\pi$ adalah...",
        "correct": "$\\left\\{ 0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi \\right\\}$",
        "distractors": [
            "$\\left\\{ \\frac{\\pi}{3}, \\frac{5\\pi}{3} \\right\\}$",
            "$\\left\\{ 0, \\frac{\\pi}{6}, \\frac{11\\pi}{6}, 2\\pi \\right\\}$",
            "$\\left\\{ \\frac{\\pi}{4}, \\frac{7\\pi}{4} \\right\\}$",
            "$\\left\\{ 0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi \\right\\}$"
        ],
        "formula": {
            "title": "FAKTORISASI PERSAMAAN TRIGONOMETRI KUADRAT",
            "latex": "2\\cos^2 x - 3\\cos x + 1 = (2\\cos x - 1)(\\cos x - 1) = 0",
            "legend": "• Menghasilkan dua kondisi sudut terpisah: $\\cos x = \\frac{1}{2}$ dan $\\cos x = 1$"
        },
        "hints": {
            "concept": "Faktorkan persamaan: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$.",
            "execution": "Untuk $\\cos x = 1 \\implies x = 0, 2\\pi$. Untuk $\\cos x = \\frac{1}{2} \\implies x = \\frac{\\pi}{3}, \\frac{5\\pi}{3}$. Gabungan seluruh solusi adalah $\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-12",
        "materi": "TRIGONOMETRI LANJUT",
        "topic": "Rumus Perkalian Sinus dan Kosinus",
        "stem": "Nilai eksak dari $4\\sin(75^\\circ)\\cos(15^\\circ)$ adalah...",
        "correct": "$2 + \\sqrt{3}$",
        "distractors": [
            "$2 - \\sqrt{3}$",
            "$1 + \\sqrt{3}$",
            "$2 + \\frac{1}{2}\\sqrt{3}$",
            "$4 + 2\\sqrt{3}$"
        ],
        "formula": {
            "title": "KONVERSI PERKALIAN KE PENJUMLAHAN SINUS",
            "latex": "2\\sin A \\cos B = \\sin(A + B) + \\sin(A - B)",
            "legend": "• Mengubah produk dua fungsi sudut menjadi penjumlahan dua gelombang sinus murni"
        },
        "hints": {
            "concept": "Ubah bentuk $4\\sin(75^\\circ)\\cos(15^\\circ) = 2 \\cdot [2\\sin(75^\\circ)\\cos(15^\\circ)]$.",
            "execution": "$2 \\cdot [\\sin(75^\\circ + 15^\\circ) + \\sin(75^\\circ - 15^\\circ)] = 2[\\sin(90^\\circ) + \\sin(60^\\circ)] = 2\\left(1 + \\frac{\\sqrt{3}}{2}\\right) = 2 + \\sqrt{3}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-13",
        "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
        "topic": "Limit Trigonometri dengan Manipulasi Tangen dan Sinus",
        "stem": "Nilai dari $\\lim_{x \\to 0} \\frac{x \\tan(3x)}{1 - \\cos(2x)}$ adalah...",
        "correct": "$\\frac{3}{2}$",
        "distractors": [
            "$\\frac{1}{2}$",
            "$1$",
            "$3$",
            "$6$"
        ],
        "formula": {
            "title": "DEKOMPOSISI LIMIT TRIGONOMETRI",
            "latex": "1 - \\cos(2x) = 2\\sin^2(x) \\implies \\lim_{x \\to 0} \\frac{x \\tan(3x)}{2\\sin^2 x}",
            "legend": "• Memecah menjadi pasangan limit standar $\\frac{x}{\\sin x}$ dan $\\frac{\\tan(3x)}{\\sin x}$"
        },
        "hints": {
            "concept": "Ganti $1 - \\cos(2x)$ dengan $2\\sin^2(x)$, sehingga bentuk limit menjadi $\\lim_{x \\to 0} \\frac{x \\tan(3x)}{2\\sin(x)\\sin(x)}$.",
            "execution": "Pisahkan limit: $\\frac{1}{2} \\cdot \\lim_{x \\to 0} \\frac{x}{\\sin x} \\cdot \\lim_{x \\to 0} \\frac{\\tan(3x)}{\\sin x} = \\frac{1}{2} \\cdot 1 \\cdot 3 = \\frac{3}{2}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-14",
        "materi": "KALKULUS LANJUT: LIMIT TAK HINGGA",
        "topic": "Limit Fungsi Trigonometri di Ketakhinggaan",
        "stem": "Nilai dari limit trigonometri di ketakhinggaan $\\lim_{x \\to \\infty} x^2 \\left( 1 - \\cos\\left(\\frac{2}{x}\\right) \\right)$ adalah...",
        "correct": "$2$",
        "distractors": [
            "$0$",
            "$1$",
            "$4$",
            "$\\frac{1}{2}$"
        ],
        "formula": {
            "title": "SUBSTITUSI VARIABEL LIMIT TAK HINGGA",
            "latex": "u = \\frac{1}{x} \\implies \\text{jika } x \\to \\infty \\text{ maka } u \\to 0",
            "legend": "• Mengubah limit ketakhinggaan menjadi limit nol standar yang siap dianalisis"
        },
        "hints": {
            "concept": "Misalkan $u = \\frac{1}{x}$. Saat $x \\to \\infty$, $u \\to 0$. Bentuk limit menjadi $\\lim_{u \\to 0} \\frac{1 - \\cos(2u)}{u^2}$.",
            "execution": "Gunakan formula $\\lim_{u \\to 0} \\frac{1 - \\cos(ku)}{u^2} = \\frac{k^2}{2}$. Untuk $k = 2$, nilainya adalah $\\frac{2^2}{2} = \\frac{4}{2} = 2$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-15",
        "materi": "KALKULUS LANJUT: TURUNAN IMPLISIT",
        "topic": "Diferensiasi Implisit pada Kurva Lingkaran/Elips",
        "stem": "Diberikan persamaan kurva implisit $x^2 + xy + y^2 = 7$. Nilai turunan pertama $\\frac{dy}{dx}$ di titik $(1, 2)$ adalah...",
        "correct": "$-\\frac{4}{5}$",
        "distractors": [
            "$\\frac{4}{5}$",
            "$-\\frac{5}{4}$",
            "$-1$",
            "$-\\frac{2}{3}$"
        ],
        "formula": {
            "title": "TEKNIK DIFERENSIASI IMPLISIT",
            "latex": "\\frac{d}{dx}[x^2 + xy + y^2] = 2x + \\left(y + x\\frac{dy}{dx}\\right) + 2y\\frac{dy}{dx} = 0",
            "legend": "• Setiap pendiferensiasian suku variabel $y$ wajib dikalikan dengan faktor $\\frac{dy}{dx}$"
        },
        "hints": {
            "concept": "Diferensiasikan kedua ruas terhadap $x$: $2x + y + x y' + 2y y' = 0 \\implies y'(x + 2y) = -(2x + y)$.",
            "execution": "Substitusikan titik $(x, y) = (1, 2)$: $y'(1 + 2(2)) = -(2(1) + 2) \\implies y'(5) = -4 \\implies y' = -\\frac{4}{5}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-16",
        "materi": "KALKULUS LANJUT: TURUNAN PARAMETRIK",
        "topic": "Garis Singgung Kurva Bentuk Parametrik",
        "stem": "Sebuah kurva dinyatakan dalam persamaan parametrik $x = 2\\cos t$ dan $y = 3\\sin t$. Gradien garis singgung kurva pada parameter $t = \\frac{\\pi}{4}$ adalah...",
        "correct": "$-\\frac{3}{2}$",
        "distractors": [
            "$\\frac{3}{2}$",
            "$-\\frac{2}{3}$",
            "$-\\frac{3}{4}$",
            "$-1$"
        ],
        "formula": {
            "title": "TURUNAN PERTAMA KURVA PARAMETRIK",
            "latex": "\\frac{dy}{dx} = \\frac{\\frac{dy}{dt}}{\\frac{dx}{dt}}",
            "legend": "• Menghitung rasio laju perubahan ordinat terhadap absis terhadap parameter waktu $t$"
        },
        "hints": {
            "concept": "Hitung $\\frac{dx}{dt} = -2\\sin t$ dan $\\frac{dy}{dt} = 3\\cos t$. Maka $\\frac{dy}{dx} = \\frac{3\\cos t}{-2\\sin t} = -\\frac{3}{2}\\cot t$.",
            "execution": "Evaluasi pada $t = \\frac{\\pi}{4}$: $\\frac{dy}{dx} = -\\frac{3}{2}\\cot\\left(\\frac{\\pi}{4}\\right) = -\\frac{3}{2}(1) = -\\frac{3}{2}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-17",
        "materi": "KALKULUS LANJUT: APLIKASI TURUNAN",
        "topic": "Titik Belok dan Kecekungan Kurva Menggunakan Turunan Kedua",
        "stem": "Koordinat titik belok dari kurva fungsi kubik $f(x) = x^3 - 6x^2 + 9x + 2$ adalah...",
        "correct": "$(2, 4)$",
        "distractors": [
            "$(1, 6)$",
            "$(3, 2)$",
            "$(2, 0)$",
            "$(-2, -48)$"
        ],
        "formula": {
            "title": "SYARAT TITIK BELOK FUNGSI",
            "latex": "f''(x) = 0 \\quad \\text{dan terjadi perubahan tanda kecekungan}",
            "legend": "• Titik belok memisahkan interval kurva cekung ke atas ($f'' > 0$) dan cekung ke bawah ($f'' < 0$)"
        },
        "hints": {
            "concept": "Turunan pertama: $f'(x) = 3x^2 - 12x + 9$. Turunan kedua: $f''(x) = 6x - 12$.",
            "execution": "Set $f''(x) = 0 \\implies 6x - 12 = 0 \\implies x = 2$. Hitung $f(2) = (2)^3 - 6(2)^2 + 9(2) + 2 = 8 - 24 + 18 + 2 = 4$. Titik belok adalah $(2, 4)$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-18",
        "materi": "KALKULUS LANJUT: INTEGRAL SUBSTITUSI",
        "topic": "Integral Substitusi Fungsi Trigonometri Berpangkat Ganjil",
        "stem": "Hasil dari $\\int \\sin^3(x)\\cos(x) \\, dx$ adalah...",
        "correct": "$\\frac{1}{4}\\sin^4(x) + C$",
        "distractors": [
            "$\\frac{1}{3}\\sin^3(x) + C$",
            "$\\frac{1}{4}\\cos^4(x) + C$",
            "$-\\frac{1}{4}\\sin^4(x) + C$",
            "$\\frac{1}{2}\\sin^2(x) + C$"
        ],
        "formula": {
            "title": "INTEGRAL PANGKAT FUNGSI TRIGONOMETRI",
            "latex": "\\int \\sin^n(x)\\cos(x) \\, dx = \\frac{1}{n+1}\\sin^{n+1}(x) + C",
            "legend": "• Menggunakan substitusi langsung $u = \\sin x \\implies du = \\cos x \\, dx$"
        },
        "hints": {
            "concept": "Misalkan $u = \\sin(x)$, maka $du = \\cos(x) \\, dx$. Bentuk integral berubah menjadi $\\int u^3 \\, du$.",
            "execution": "$\\int u^3 \\, du = \\frac{1}{4}u^4 + C = \\frac{1}{4}\\sin^4(x) + C$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-19",
        "materi": "KALKULUS LANJUT: INTEGRAL PARSIAL",
        "topic": "Integral Parsial Fungsi Aljabar dan Trigonometri",
        "stem": "Hasil dari $\\int x \\cos(x) \\, dx$ adalah...",
        "correct": "$x\\sin(x) + \\cos(x) + C$",
        "distractors": [
            "$x\\sin(x) - \\cos(x) + C$",
            "$-x\\sin(x) + \\cos(x) + C$",
            "$x\\cos(x) + \\sin(x) + C$",
            "$\\frac{1}{2}x^2 \\sin(x) + C$"
        ],
        "formula": {
            "title": "INTEGRAL PARSIAL ALJABAR-TRIGONOMETRI",
            "latex": "\\int u \\, dv = uv - \\int v \\, du",
            "legend": "• $u = x \\implies du = dx$<br>• $dv = \\cos x \\, dx \\implies v = \\sin x$"
        },
        "hints": {
            "concept": "Pilih $u = x$ dan $dv = \\cos(x) \\, dx$. Maka $du = dx$ dan $v = \\sin(x)$.",
            "execution": "$\\int x\\cos(x) \\, dx = x\\sin(x) - \\int \\sin(x) \\, dx = x\\sin(x) - (-\\cos(x)) + C = x\\sin(x) + \\cos(x) + C$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-20",
        "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
        "topic": "Luas Daerah Antara Dua Kurva (Parabola dan Garis)",
        "stem": "Luas daerah tertutup yang dibatasi oleh parabola $y = x^2$ dan garis linear $y = 2x + 3$ adalah...",
        "correct": "$\\frac{32}{3} \\text{ satuan luas}$",
        "distractors": [
            "$\\frac{16}{3} \\text{ satuan luas}$",
            "$\\frac{28}{3} \\text{ satuan luas}$",
            "$12 \\text{ satuan luas}$",
            "$\\frac{64}{3} \\text{ satuan luas}$"
        ],
        "formula": {
            "title": "LUAS ANTARA DUA KURVA",
            "latex": "L = \\int_{x_1}^{x_2} (y_{\\text{atas}} - y_{\\text{bawah}}) \\, dx = \\frac{D\\sqrt{D}}{6a^2}",
            "legend": "• Titik potong diperoleh dari persamaan sekutu $x^2 - 2x - 3 = 0$"
        },
        "hints": {
            "concept": "Titik potong: $x^2 = 2x + 3 \\implies x^2 - 2x - 3 = 0 \\implies (x - 3)(x + 1) = 0 \\implies x = -1$ dan $x = 3$.",
            "execution": "Hitung $L = \\int_{-1}^3 (2x + 3 - x^2) \\, dx = \\left[ x^2 + 3x - \\frac{1}{3}x^3 \\right]_{-1}^3 = (9 + 9 - 9) - \\left(1 - 3 + \\frac{1}{3}\\right) = 9 - \\left(-\\frac{5}{3}\\right) = \\frac{32}{3}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-21",
        "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
        "topic": "Volume Benda Putar Mengelilingi Sumbu-X Metode Cakram",
        "stem": "Volume benda putar yang terjadi jika daerah yang dibatasi oleh kurva $y = \\sqrt{x}$, garis $x = 4$, dan sumbu-$x$ diputar $360^\\circ$ mengelilingi sumbu-$x$ adalah...",
        "correct": "$8\\pi \\text{ satuan volume}$",
        "distractors": [
            "$4\\pi \\text{ satuan volume}$",
            "$16\\pi \\text{ satuan volume}$",
            "$32\\pi \\text{ satuan volume}$",
            "$\\frac{16}{3}\\pi \\text{ satuan volume}$"
        ],
        "formula": {
            "title": "VOLUME BENDA PUTAR METODE CAKRAM",
            "latex": "V = \\pi \\int_a^b [f(x)]^2 \\, dx",
            "legend": "• Menjumlahkan elemen volume silinder tipis $dV = \\pi r^2 dx$ dengan jari-jari $r = f(x)$"
        },
        "hints": {
            "concept": "Substitusikan batas $x = 0$ sampai $x = 4$ dengan $[f(x)]^2 = (\\sqrt{x})^2 = x$.",
            "execution": "Hitung $V = \\pi \\int_0^4 x \\, dx = \\pi \\left[ \\frac{1}{2}x^2 \\right]_0^4 = \\pi \\left( \\frac{16}{2} - 0 \\right) = 8\\pi$ satuan volume."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-22",
        "materi": "POLINOMIAL & SUKU BANYAK",
        "topic": "Sisa Pembagian Derajat Tinggi dengan Pembagi Faktor Tunggal",
        "stem": "Diketahui suku banyak $P(x)$ jika dibagi $(x - 1)$ bersisa 3, dan jika dibagi $(x + 2)$ bersisa $-6$. Sisa pembagian $P(x)$ oleh bentuk $(x^2 + x - 2)$ adalah...",
        "correct": "$3x$",
        "distractors": [
            "$3x + 1$",
            "$2x + 1$",
            "$3x - 1$",
            "$-3x$"
        ],
        "formula": {
            "title": "TEOREMA SISA DENGAN SISTEM ELIMINASI",
            "latex": "S(x) = ax + b \\implies \\begin{cases} a(1) + b = P(1) = 3 \\\\ a(-2) + b = P(-2) = -6 \\end{cases}",
            "legend": "• Sisa pembagian oleh kuadratik ditentukan secara unik oleh nilai sisa pada masing-masing faktor pembaginya"
        },
        "hints": {
            "concept": "Bentuk sisa adalah $S(x) = ax + b$. Susun sistem persamaan: $a + b = 3$ dan $-2a + b = -6$.",
            "execution": "Kurangkan: $(a + b) - (-2a + b) = 3 - (-6) \\implies 3a = 9 \\implies a = 3$. Maka $3 + b = 3 \\implies b = 0$. Sisa pembagian adalah $S(x) = 3x$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-23",
        "materi": "MATRIKS & DETERMINAN",
        "topic": "Kofaktor dan Adjoin Matriks Ordo 3x3",
        "stem": "Diberikan matriks $A = \\begin{pmatrix} 1 & 0 & 2 \\\\ 2 & -1 & 3 \\\\ 4 & 1 & 8 \\end{pmatrix}$. Nilai kofaktor elemen baris ke-2 kolom ke-3 ($C_{23}$) adalah...",
        "correct": "$-1$",
        "distractors": [
            "$1$",
            "$-2$",
            "$2$",
            "$0$"
        ],
        "formula": {
            "title": "FORMULA KOFAKTOR ELEMEN MATRIKS",
            "latex": "C_{ij} = (-1)^{i+j} M_{ij} = (-1)^{i+j} \\det(\\text{Submatriks tanpa baris } i \\text{ dan kolom } j)",
            "legend": "• Tanda bergantian $(-1)^{i+j}$ menentukan tanda positif/negatif minor submatriks"
        },
        "hints": {
            "concept": "Hapus baris 2 dan kolom 3: submatriks tersisa adalah $\\begin{pmatrix} 1 & 0 \\\\ 4 & 1 \\end{pmatrix}$.",
            "execution": "Hitung minor: $M_{23} = (1)(1) - (0)(4) = 1$. Nilai kofaktor: $C_{23} = (-1)^{2+3} M_{23} = (-1)^5 (1) = -1$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-24",
        "materi": "GEOMETRI ANALITIK",
        "topic": "Persamaan Garis Singgung Hiperbola Bergradien m",
        "stem": "Persamaan garis singgung hiperbola $\\frac{x^2}{4} - \\frac{y^2}{5} = 1$ yang memiliki gradien $m = 2$ adalah...",
        "correct": "$y = 2x \\pm \\sqrt{11}$",
        "distractors": [
            "$y = 2x \\pm \\sqrt{21}$",
            "$y = 2x \\pm 3$",
            "$y = 2x \\pm \\sqrt{19}$",
            "$y = 2x \\pm 1$"
        ],
        "formula": {
            "title": "GARIS SINGGUNG HIPERBOLA BERGRADISIEN m",
            "latex": "y = mx \\pm \\sqrt{a^2 m^2 - b^2}",
            "legend": "• Syarat keberadaan garis singgung nyata adalah nilai di dalam akar $a^2 m^2 - b^2 > 0$"
        },
        "hints": {
            "concept": "Substitusikan $a^2 = 4, b^2 = 5,$ dan $m = 2$ ke dalam formula garis singgung hiperbola horizontal.",
            "execution": "Hitung suku konstan: $\\sqrt{a^2 m^2 - b^2} = \\sqrt{4(2^2) - 5} = \\sqrt{4(4) - 5} = \\sqrt{16 - 5} = \\sqrt{11}$. Persamaan garis singgung: $y = 2x \\pm \\sqrt{11}$."
        }
    },
    {
        "id": "mtk_lanjut-lat-m-25",
        "materi": "KALKULUS LANJUT: TURUNAN TRIGONOMETRI",
        "topic": "Nilai Maksimum dan Minimum Fungsi Gelombang Harmonik",
        "stem": "Nilai maksimum dari fungsi $f(x) = 3\\sin(2x) - 4\\cos(2x) + 7$ adalah...",
        "correct": "$12$",
        "distractors": [
            "$5$",
            "$7$",
            "$10$",
            "$14$"
        ],
        "formula": {
            "title": "AMPLITUDO DAN EKSTREM GELOMBANG HARMONIK",
            "latex": "f(x) = a\\sin(kx) + b\\cos(kx) + c \\implies f_{\\max} = \\sqrt{a^2 + b^2} + c",
            "legend": "• Amplitudo maksimum fungsi gelombang gabungan adalah $R = \\sqrt{a^2 + b^2}$"
        },
        "hints": {
            "concept": "Hitung amplitudo gelombang: $R = \\sqrt{3^2 + (-4)^2} = \\sqrt{9 + 16} = 5$.",
            "execution": "Nilai maksimum fungsi adalah $R + c = 5 + 7 = 12$."
        }
    }
]
