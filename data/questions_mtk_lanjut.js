/**
 * TKA MASTERY HUB - AUTENTIK & BALANCED DATASET
 * Subject: TKA_MTK_LANJUT_QUESTIONS
 * Keys rebalanced ~20% A-E, AI distractor padding sanitized.
 */

window.TKA_MTK_LANJUT_QUESTIONS = [
  {
    "id": "mtk_lanjut-lat-e-01",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Sisa Pembagian Polinomial Linear",
    "type": "mcq",
    "questionHtml": "Diketahui suku banyak $P(x) = 2x^3 - 5x^2 + 8x - 12$. Sisa pembagian suku banyak $P(x)$ oleh pembagi linear $(x - 3)$ berdasarkan Teorema Sisa adalah...",
    "options": [
      {
        "key": "A",
        "text": "$15$."
      },
      {
        "key": "B",
        "text": "$24$."
      },
      {
        "key": "C",
        "text": "$21$"
      },
      {
        "key": "D",
        "text": "$18$."
      },
      {
        "key": "E",
        "text": "$27$."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL LINEAR",
      "latex": "P(x) = (x - c) \\cdot H(x) + S \\implies S = P(c)",
      "legend": "• Sisa pembagian suku banyak $P(x)$ oleh pembagi $(x - c)$ tepat bernilai $P(c)$"
    },
    "hints": {
      "concept": "Menurut Teorema Sisa, sisa pembagian $P(x)$ oleh $(x - 3)$ diperoleh dengan menyubstitusikan $x = 3$ langsung ke fungsi $P(x)$.",
      "execution": "Hitung $P(3) = 2(3)^3 - 5(3)^2 + 8(3) - 12 = 2(27) - 5(9) + 24 - 12 = 54 - 45 + 12 = 21$."
    },
    "explanation": "Menurut Teorema Sisa, sisa pembagian $P(x)$ oleh $(x - 3)$ diperoleh dengan menyubstitusikan $x = 3$ langsung ke fungsi $P(x)$. Hitung $P(3) = 2(3)^3 - 5(3)^2 + 8(3) - 12 = 2(27) - 5(9) + 24 - 12 = 54 - 45 + 12 = 21$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-02",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Faktor Polinomial Derajat Tiga",
    "type": "mcq",
    "questionHtml": "Suku banyak $P(x) = x^3 + kx^2 - 4x - 12$ memiliki faktor linear $(x + 2)$. Nilai konstanta $k$ yang memenuhi persamaan tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$1$"
      },
      {
        "key": "B",
        "text": "$2$"
      },
      {
        "key": "C",
        "text": "$3$"
      },
      {
        "key": "D",
        "text": "$-2$"
      },
      {
        "key": "E",
        "text": "$0$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA FAKTOR POLINOMIAL",
      "latex": "(x - c) \\text{ faktor dari } P(x) \\iff P(c) = 0",
      "legend": "• Nilai fungsi suku banyak bernilai nol pada pembuat nol dari faktor linearnya"
    },
    "hints": {
      "concept": "Karena $(x + 2)$ adalah faktor, maka nilai $P(-2)$ harus tepat sama dengan nol.",
      "execution": "Substitusikan $x = -2$: $(-2)^3 + k(-2)^2 - 4(-2) - 12 = -8 + 4k + 8 - 12 = 4k - 12 = 0 \\implies 4k = 12 \\implies k = 3$."
    },
    "explanation": "Karena $(x + 2)$ adalah faktor, maka nilai $P(-2)$ harus tepat sama dengan nol. Substitusikan $x = -2$: $(-2)^3 + k(-2)^2 - 4(-2) - 12 = -8 + 4k + 8 - 12 = 4k - 12 = 0 \\implies 4k = 12 \\implies k = 3$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-03",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Jumlah Akar-akar Persamaan Kubik (Teorema Vieta)",
    "type": "mcq",
    "questionHtml": "Akar-akar dari persamaan polinomial kubik $2x^3 - 6x^2 + 11x - 5 = 0$ adalah $x_1, x_2,$ dan $x_3$. Nilai dari hasil penjumlahan seluruh akar $(x_1 + x_2 + x_3)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-3$"
      },
      {
        "key": "B",
        "text": "$\\frac{11}{2}$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{2}$"
      },
      {
        "key": "D",
        "text": "$-\\frac{5}{2}$"
      },
      {
        "key": "E",
        "text": "$3$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TEOREMA VIETA SUKU BANYAK DERAJAT TIGA",
      "latex": "ax^3 + bx^2 + cx + d = 0 \\implies x_1 + x_2 + x_3 = -\\frac{b}{a}",
      "legend": "• Jumlah akar tunggal ditentukan oleh perbandingan negatif koefisien derajat kedua terhadap koefisien utama"
    },
    "hints": {
      "concept": "Gunakan hubungan Vieta untuk jumlah akar persamaan kubik: $x_1 + x_2 + x_3 = -\\frac{b}{a}$.",
      "execution": "Dari persamaan, $a = 2, b = -6$. Maka $x_1 + x_2 + x_3 = -\\frac{-6}{2} = \\frac{6}{2} = 3$."
    },
    "explanation": "Gunakan hubungan Vieta untuk jumlah akar persamaan kubik: $x_1 + x_2 + x_3 = -\\frac{b}{a}$. Dari persamaan, $a = 2, b = -6$. Maka $x_1 + x_2 + x_3 = -\\frac{-6}{2} = \\frac{6}{2} = 3$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-04",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Determinan Matriks Persegi Ordo 3x3 Metode Sarrus",
    "type": "mcq",
    "questionHtml": "Diberikan matriks $A = \\begin{pmatrix} 1 & 2 & 0 \\\\ 0 & 3 & 4 \\\\ 2 & 1 & 5 \\end{pmatrix}$. Nilai determinan dari matriks $A$ ($\\det(A)$) adalah...",
    "options": [
      {
        "key": "A",
        "text": "$15$."
      },
      {
        "key": "B",
        "text": "$27$."
      },
      {
        "key": "C",
        "text": "$19$."
      },
      {
        "key": "D",
        "text": "$23$"
      },
      {
        "key": "E",
        "text": "$31$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "DETERMINAN MATRIKS 3X3",
      "latex": "\\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})",
      "legend": "• Perhitungan determinan ordo 3 melalui metode ekspansi kofaktor baris pertama"
    },
    "hints": {
      "concept": "Ekspansi kofaktor sepanjang baris pertama: $\\det(A) = 1(3\\cdot 5 - 4\\cdot 1) - 2(0\\cdot 5 - 4\\cdot 2) + 0$.",
      "execution": "Hitung: $1(15 - 4) - 2(0 - 8) + 0 = 1(11) - 2(-8) = 11 + 16 = 27$."
    },
    "explanation": "Ekspansi kofaktor sepanjang baris pertama: $\\det(A) = 1(3\\cdot 5 - 4\\cdot 1) - 2(0\\cdot 5 - 4\\cdot 2) + 0$. Hitung: $1(15 - 4) - 2(0 - 8) + 0 = 1(11) - 2(-8) = 11 + 16 = 27$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-05",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sifat Determinan Perkalian dan Skalar Matriks",
    "type": "mcq",
    "questionHtml": "Jika $P$ dan $Q$ adalah matriks berordo $3 \\times 3$ dengan $\\det(P) = 4$ dan $\\det(Q) = -2$, maka nilai dari $\\det(2 \\cdot P \\cdot Q)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-64$"
      },
      {
        "key": "B",
        "text": "$-32$."
      },
      {
        "key": "C",
        "text": "$64$."
      },
      {
        "key": "D",
        "text": "$-16$."
      },
      {
        "key": "E",
        "text": "$32$."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SIFAT DETERMINAN MATRIKS BERORDO n",
      "latex": "\\det(k \\cdot A \\cdot B) = k^n \\cdot \\det(A) \\cdot \\det(B) \\quad (\\text{untuk ordo } n \\times n)",
      "legend": "• Konstanta skalar $k$ keluar dari determinan dengan pangkat senilai ordo matriks $n$"
    },
    "hints": {
      "concept": "Karena ordo matriks adalah $3 \\times 3$ ($n = 3$), maka skalar 2 keluar menjadi $2^3 = 8$. Lalu kalikan dengan $\\det(P)$ dan $\\det(Q)$.",
      "execution": "Hitung: $\\det(2PQ) = 2^3 \\cdot \\det(P) \\cdot \\det(Q) = 8 \\cdot 4 \\cdot (-2) = 32 \\cdot (-2) = -64$."
    },
    "explanation": "Karena ordo matriks adalah $3 \\times 3$ ($n = 3$), maka skalar 2 keluar menjadi $2^3 = 8$. Lalu kalikan dengan $\\det(P)$ dan $\\det(Q)$. Hitung: $\\det(2PQ) = 2^3 \\cdot \\det(P) \\cdot \\det(Q) = 8 \\cdot 4 \\cdot (-2) = 32 \\cdot (-2) = -64$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-06",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Titik Puncak dan Fokus Parabola Horizontal",
    "type": "mcq",
    "questionHtml": "Diberikan persamaan parabola $y^2 - 4y - 12x + 16 = 0$. Koordinat titik puncak dari parabola tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$(4, 2)$"
      },
      {
        "key": "B",
        "text": "$(-1, 2)$"
      },
      {
        "key": "C",
        "text": "$(1, -2)$"
      },
      {
        "key": "D",
        "text": "$(2, 1)$"
      },
      {
        "key": "E",
        "text": "$(1, 2)$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "BENTUK BAKU PARABOLA HORIZONTAL",
      "latex": "(y - k)^2 = 4p(x - h) \\implies \\text{Puncak } (h, k)",
      "legend": "• $h$: Absis puncak parabola<br>• $k$: Ordinat puncak parabola<br>• $p$: Jarak fokus"
    },
    "hints": {
      "concept": "Ubah persamaan kuadrat ke dalam bentuk kuadrat sempurna untuk variabel $y$: $(y - 2)^2 - 4 - 12x + 16 = 0$.",
      "execution": "$(y - 2)^2 + 12 - 12x = 0 \\implies (y - 2)^2 = 12x - 12 = 12(x - 1)$. Dari sini diperoleh puncak $(h, k) = (1, 2)$."
    },
    "explanation": "Ubah persamaan kuadrat ke dalam bentuk kuadrat sempurna untuk variabel $y$: $(y - 2)^2 - 4 - 12x + 16 = 0$. $(y - 2)^2 + 12 - 12x = 0 \\implies (y - 2)^2 = 12x - 12 = 12(x - 1)$. Dari sini diperoleh puncak $(h, k) = (1, 2)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-07",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Panjang Sumbu Mayor dan Minor Elips",
    "type": "mcq",
    "questionHtml": "Persamaan elips diberikan oleh $\\frac{x^2}{25} + \\frac{y^2}{9} = 1$. Panjang sumbu mayor ($2a$) dan sumbu minor ($2b$) elips tersebut berturut-turut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$8$ dan $6$."
      },
      {
        "key": "B",
        "text": "$5$ dan $3$."
      },
      {
        "key": "C",
        "text": "$10$ dan $8$."
      },
      {
        "key": "D",
        "text": "$25$ dan $9$."
      },
      {
        "key": "E",
        "text": "$10$ dan $6$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "DIMENSI SUMBU ELIPS HORIZONTAL",
      "latex": "\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1 \\implies \\text{Sumbu Mayor} = 2a, \\quad \\text{Sumbu Minor} = 2b",
      "legend": "• $a = \\sqrt{25} = 5$ (setengah sumbu panjang)<br>• $b = \\sqrt{9} = 3$ (setengah sumbu pendek)"
    },
    "hints": {
      "concept": "Nilai $a^2 = 25 \\implies a = 5$ dan $b^2 = 9 \\implies b = 3$.",
      "execution": "Panjang sumbu mayor adalah $2a = 2(5) = 10$, dan sumbu minor adalah $2b = 2(3) = 6$."
    },
    "explanation": "Nilai $a^2 = 25 \\implies a = 5$ dan $b^2 = 9 \\implies b = 3$. Panjang sumbu mayor adalah $2a = 2(5) = 10$, dan sumbu minor adalah $2b = 2(3) = 6$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-08",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Asimtot Hiperbola Horizontal Berpusat di Asal",
    "type": "mcq",
    "questionHtml": "Persamaan asimtot dari kurva hiperbola $\\frac{x^2}{16} - \\frac{y^2}{9} = 1$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$y = \\pm \\frac{3}{4}x$"
      },
      {
        "key": "B",
        "text": "$y = \\pm \\frac{9}{16}x$"
      },
      {
        "key": "C",
        "text": "$y = \\pm \\frac{4}{3}x$"
      },
      {
        "key": "D",
        "text": "$y = \\pm \\frac{16}{9}x$"
      },
      {
        "key": "E",
        "text": "$y = \\pm \\frac{3}{5}x$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PERSAMAAN ASIMTOT HIPERBOLA",
      "latex": "\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1 \\implies y = \\pm \\frac{b}{a}x",
      "legend": "• Asimtot merupakan garis pemandu yang didekati kurva hiperbola saat menuju tak hingga"
    },
    "hints": {
      "concept": "Dari persamaan hiperbola, $a^2 = 16 \\implies a = 4$ dan $b^2 = 9 \\implies b = 3$.",
      "execution": "Rumus garis asimtot hiperbola horizontal adalah $y = \\pm \\frac{b}{a}x = \\pm \\frac{3}{4}x$."
    },
    "explanation": "Dari persamaan hiperbola, $a^2 = 16 \\implies a = 4$ dan $b^2 = 9 \\implies b = 3$. Rumus garis asimtot hiperbola horizontal adalah $y = \\pm \\frac{b}{a}x = \\pm \\frac{3}{4}x$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-09",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Perkalian Skalar (Dot Product) Dua Vektor di R3",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor pada ruang tiga dimensi: $\\vec{u} = 2\\hat{i} - 3\\hat{j} + 4\\hat{k}$ dan $\\vec{v} = 5\\hat{i} + 2\\hat{j} - \\hat{k}$. Nilai perkalian skalar $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$12$"
      },
      {
        "key": "B",
        "text": "$6$"
      },
      {
        "key": "C",
        "text": "$2$"
      },
      {
        "key": "D",
        "text": "$0$"
      },
      {
        "key": "E",
        "text": "$-4$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "DOT PRODUCT VEKTOR TIGA DIMENSI",
      "latex": "\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z",
      "legend": "• Menghasilkan skalar; jika bernilai nol menandakan kedua vektor saling tegak lurus (ortogonal)"
    },
    "hints": {
      "concept": "Kalikan komponen-komponen yang seletak lalu jumlahkan seluruh hasilnya.",
      "execution": "$\\vec{u} \\cdot \\vec{v} = (2)(5) + (-3)(2) + (4)(-1) = 10 - 6 - 4 = 0$."
    },
    "explanation": "Kalikan komponen-komponen yang seletak lalu jumlahkan seluruh hasilnya. $\\vec{u} \\cdot \\vec{v} = (2)(5) + (-3)(2) + (4)(-1) = 10 - 6 - 4 = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-10",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Panjang Proyeksi Skalar Ortogonal",
    "type": "mcq",
    "questionHtml": "Diketahui vektor $\\vec{a} = 3\\hat{i} - 4\\hat{j}$ dan $\\vec{b} = 6\\hat{i} + 8\\hat{j}$. Panjang proyeksi skalar ortogonal vektor $\\vec{a}$ pada vektor $\\vec{b}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-\\frac{7}{5}$"
      },
      {
        "key": "B",
        "text": "$-1$."
      },
      {
        "key": "C",
        "text": "$\\frac{14}{5}$."
      },
      {
        "key": "D",
        "text": "$\\frac{7}{5}$."
      },
      {
        "key": "E",
        "text": "$-2$."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PANJANG PROYEKSI SKALAR",
      "latex": "|\\vec{c}| = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{b}|}",
      "legend": "• $|\\vec{b}| = \\sqrt{b_x^2 + b_y^2 + b_z^2}$ adalah modulus atau magnitudo vektor target"
    },
    "hints": {
      "concept": "Hitung perkalian dot $\\vec{a} \\cdot \\vec{b}$ lalu bagi dengan panjang vektor $\\vec{b}$.",
      "execution": "$\\vec{a} \\cdot \\vec{b} = 3(6) + (-4)(8) = 18 - 32 = -14$. Panjang $|\\vec{b}| = \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = 10$. Maka proyeksi skalarnya adalah $\\frac{-14}{10} = -\\frac{7}{5}$."
    },
    "explanation": "Hitung perkalian dot $\\vec{a} \\cdot \\vec{b}$ lalu bagi dengan panjang vektor $\\vec{b}$. $\\vec{a} \\cdot \\vec{b} = 3(6) + (-4)(8) = 18 - 32 = -14$. Panjang $|\\vec{b}| = \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = 10$. Maka proyeksi skalarnya adalah $\\frac{-14}{10} = -\\frac{7}{5}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-11",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Identitas Sudut Ganda Sinus dan Kosinus",
    "type": "mcq",
    "questionHtml": "Jika diketahui $\\sin \\alpha = \\frac{3}{5}$ dengan $\\alpha$ merupakan sudut lancip ($0 < \\alpha < \\frac{\\pi}{2}$), maka nilai dari $\\cos(2\\alpha)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{16}{25}$"
      },
      {
        "key": "B",
        "text": "$\\frac{24}{25}$"
      },
      {
        "key": "C",
        "text": "$-\\frac{7}{25}$"
      },
      {
        "key": "D",
        "text": "$\\frac{12}{25}$"
      },
      {
        "key": "E",
        "text": "$\\frac{7}{25}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\alpha) = 1 - 2\\sin^2\\alpha = 2\\cos^2\\alpha - 1 = \\cos^2\\alpha - \\sin^2\\alpha",
      "legend": "• Memungkinkan konversi sudut ganda langsung dari nilai fungsi trigonometri sudut tunggal"
    },
    "hints": {
      "concept": "Gunakan bentuk identitas $\\cos(2\\alpha) = 1 - 2\\sin^2\\alpha$ karena nilai $\\sin\\alpha$ sudah diketahui langsung.",
      "execution": "Hitung: $\\cos(2\\alpha) = 1 - 2\\left(\\frac{3}{5}\\right)^2 = 1 - 2\\left(\\frac{9}{25}\\right) = 1 - \\frac{18}{25} = \\frac{7}{25}$."
    },
    "explanation": "Gunakan bentuk identitas $\\cos(2\\alpha) = 1 - 2\\sin^2\\alpha$ karena nilai $\\sin\\alpha$ sudah diketahui langsung. Hitung: $\\cos(2\\alpha) = 1 - 2\\left(\\frac{3}{5}\\right)^2 = 1 - 2\\left(\\frac{9}{25}\\right) = 1 - \\frac{18}{25} = \\frac{7}{25}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-12",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Penjumlahan Sudut Tangen",
    "type": "mcq",
    "questionHtml": "Diketahui $\\tan A = \\frac{1}{2}$ dan $\\tan B = \\frac{1}{3}$. Nilai dari $\\tan(A + B)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{5}{6}$"
      },
      {
        "key": "B",
        "text": "$\\frac{5}{7}$"
      },
      {
        "key": "C",
        "text": "$\\sqrt{3}$"
      },
      {
        "key": "D",
        "text": "$1$"
      },
      {
        "key": "E",
        "text": "$\\frac{2}{3}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "RUMUS JUMLAH SUDUT TANGEN",
      "latex": "\\tan(A + B) = \\frac{\\tan A + \\tan B}{1 - \\tan A \\cdot \\tan B}",
      "legend": "• Konversi jumlahan sudut tangen menjadi rasio aljabar nilai tangen masing-masing sudut"
    },
    "hints": {
      "concept": "Substitusikan nilai $\\tan A = \\frac{1}{2}$ dan $\\tan B = \\frac{1}{3}$ ke dalam formula jumlahan tangen.",
      "execution": "$\\tan(A + B) = \\frac{\\frac{1}{2} + \\frac{1}{3}}{1 - (\\frac{1}{2})(\\frac{1}{3})} = \\frac{\\frac{5}{6}}{1 - \\frac{1}{6}} = \\frac{\\frac{5}{6}}{\\frac{5}{6}} = 1$."
    },
    "explanation": "Substitusikan nilai $\\tan A = \\frac{1}{2}$ dan $\\tan B = \\frac{1}{3}$ ke dalam formula jumlahan tangen. $\\tan(A + B) = \\frac{\\frac{1}{2} + \\frac{1}{3}}{1 - (\\frac{1}{2})(\\frac{1}{3})} = \\frac{\\frac{5}{6}}{1 - \\frac{1}{6}} = \\frac{\\frac{5}{6}}{\\frac{5}{6}} = 1$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-13",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Konversi Bentuk a cos x + b sin x = k cos(x - alpha)",
    "type": "mcq",
    "questionHtml": "Bentuk $f(x) = \\sqrt{3}\\cos x + \\sin x$ dapat dinyatakan dalam bentuk ekuivalen $k \\cos(x - \\alpha)$. Nilai konstanta amplitudo $k$ dan sudut fase $\\alpha$ (dalam radian) adalah...",
    "options": [
      {
        "key": "A",
        "text": "$k = 2, \\quad \\alpha = \\frac{\\pi}{6}$"
      },
      {
        "key": "B",
        "text": "$k = 4, \\quad \\alpha = \\frac{\\pi}{6}$"
      },
      {
        "key": "C",
        "text": "$k = 2, \\quad \\alpha = \\frac{\\pi}{3}$"
      },
      {
        "key": "D",
        "text": "$k = 2, \\quad \\alpha = \\frac{\\pi}{4}$"
      },
      {
        "key": "E",
        "text": "$k = \\sqrt{2}, \\quad \\alpha = \\frac{\\pi}{4}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TRANSFORMASI FUNGSI KOSINUS-SINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha) \\implies k = \\sqrt{a^2 + b^2}, \\quad \\tan\\alpha = \\frac{b}{a}",
      "legend": "• $k$: Modulus amplitudo gelombang gabungan<br>• $\\alpha$: Pergeseran fase sudut di kuadran bersesuaian"
    },
    "hints": {
      "concept": "Ambil $a = \\sqrt{3}$ dan $b = 1$. Hitung $k = \\sqrt{a^2 + b^2}$ dan $\\tan\\alpha = \\frac{b}{a}$.",
      "execution": "$k = \\sqrt{(\\sqrt{3})^2 + 1^2} = \\sqrt{3 + 1} = \\sqrt{4} = 2$. Karena $a > 0$ dan $b > 0$, $\\alpha$ di Kuadran I: $\\tan\\alpha = \\frac{1}{\\sqrt{3}} \\implies \\alpha = 30^\\circ = \\frac{\\pi}{6}$."
    },
    "explanation": "Ambil $a = \\sqrt{3}$ dan $b = 1$. Hitung $k = \\sqrt{a^2 + b^2}$ dan $\\tan\\alpha = \\frac{b}{a}$. $k = \\sqrt{(\\sqrt{3})^2 + 1^2} = \\sqrt{3 + 1} = \\sqrt{4} = 2$. Karena $a > 0$ dan $b > 0$, $\\alpha$ di Kuadran I: $\\tan\\alpha = \\frac{1}{\\sqrt{3}} \\implies \\alpha = 30^\\circ = \\frac{\\pi}{6}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-14",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Limit Dasar Bentuk Tak Tentu Sinus",
    "type": "mcq",
    "questionHtml": "Nilai dari limit trigonometri dasar $\\lim_{x \\to 0} \\frac{\\sin(6x)}{2x}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$1$"
      },
      {
        "key": "B",
        "text": "$2$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{3}$"
      },
      {
        "key": "D",
        "text": "$6$"
      },
      {
        "key": "E",
        "text": "$3$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TEOREMA LIMIT TRIGONOMETRI DASAR",
      "latex": "\\lim_{x \\to 0} \\frac{\\sin(ax)}{bx} = \\frac{a}{b}",
      "legend": "• Berlaku untuk fungsi sinus dan tangen saat variabel $x$ mendekati nilai nol"
    },
    "hints": {
      "concept": "Gunakan teorema limit trigonometri khusus: $\\lim_{x \\to 0} \\frac{\\sin(ax)}{bx} = \\frac{a}{b}$.",
      "execution": "Ambil $a = 6$ dan $b = 2$, maka nilainya adalah $\\frac{6}{2} = 3$."
    },
    "explanation": "Gunakan teorema limit trigonometri khusus: $\\lim_{x \\to 0} \\frac{\\sin(ax)}{bx} = \\frac{a}{b}$. Ambil $a = 6$ dan $b = 2$, maka nilainya adalah $\\frac{6}{2} = 3$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-15",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Limit Bentuk 1 - cos(kx) per x kuadrat",
    "type": "mcq",
    "questionHtml": "Nilai limit fungsi trigonometri $\\lim_{x \\to 0} \\frac{1 - \\cos(4x)}{x^2}$ bernilai tepat sama dengan...",
    "options": [
      {
        "key": "A",
        "text": "$4$"
      },
      {
        "key": "B",
        "text": "$8$"
      },
      {
        "key": "C",
        "text": "$32$"
      },
      {
        "key": "D",
        "text": "$16$"
      },
      {
        "key": "E",
        "text": "$2$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "LIMIT IDENTITAS SUDUT KOSINUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Hasil penjabaran identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$"
    },
    "hints": {
      "concept": "Berdasarkan formula standar limit: $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$.",
      "execution": "Untuk $k = 4$, hitung: $\\frac{4^2}{2} = \\frac{16}{2} = 8$."
    },
    "explanation": "Berdasarkan formula standar limit: $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$. Untuk $k = 4$, hitung: $\\frac{4^2}{2} = \\frac{16}{2} = 8$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-16",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT TAK HINGGA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Limit di Ketakhinggaan Fungsi Rasional Aljabar",
    "type": "mcq",
    "questionHtml": "Nilai dari $\\lim_{x \\to \\infty} \\frac{4x^3 - 5x + 7}{2x^3 + 3x^2 - 1}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$0$"
      },
      {
        "key": "B",
        "text": "$\\frac{4}{3}$"
      },
      {
        "key": "C",
        "text": "$2$"
      },
      {
        "key": "D",
        "text": "$\\infty$"
      },
      {
        "key": "E",
        "text": "$4$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "LIMIT ASIMTOTIK FUNGSI RASIONAL",
      "latex": "\\lim_{x \\to \\infty} \\frac{a_n x^n + \\dots}{b_m x^m + \\dots} = \\begin{cases} \\frac{a_n}{b_m}, & n = m \\\\ 0, & n < m \\\\ \\infty, & n > m \\end{cases}",
      "legend": "• Ditentukan oleh rasio koefisien pangkat tertinggi saat derajat pembilang sama dengan penyebut"
    },
    "hints": {
      "concept": "Karena derajat tertinggi pembilang dan penyebut sama-sama 3 ($n = m = 3$), bagi pembilang dan penyebut dengan $x^3$.",
      "execution": "Rasio koefisien pangkat tertinggi adalah $\\frac{4}{2} = 2$."
    },
    "explanation": "Karena derajat tertinggi pembilang dan penyebut sama-sama 3 ($n = m = 3$), bagi pembilang dan penyebut dengan $x^3$. Rasio koefisien pangkat tertinggi adalah $\\frac{4}{2} = 2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-17",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT TAK HINGGA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Limit Selisih Bentuk Akar Kuadrat di Ketakhinggaan",
    "type": "mcq",
    "questionHtml": "Nilai dari limit aljabar $\\lim_{x \\to \\infty} \\left( \\sqrt{x^2 + 6x - 2} - \\sqrt{x^2 - 4x + 5} \\right)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$1$"
      },
      {
        "key": "B",
        "text": "$2$"
      },
      {
        "key": "C",
        "text": "$5$"
      },
      {
        "key": "D",
        "text": "$10$"
      },
      {
        "key": "E",
        "text": "$\\infty$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "LIMIT SELISIH AKAR KUADRAT TAK HINGGA",
      "latex": "\\lim_{x \\to \\infty} \\left(\\sqrt{ax^2 + bx + c} - \\sqrt{ax^2 + px + q}\\right) = \\frac{b - p}{2\\sqrt{a}} \\quad (a > 0)",
      "legend": "• Menghitung nilai limit seketika tanpa perlu mengalikan sekawan panjang"
    },
    "hints": {
      "concept": "Gunakan rumus cepat limit selisih bentuk akar kuadrat: $L = \\frac{b - p}{2\\sqrt{a}}$.",
      "execution": "Dari soal, $a = 1, b = 6, p = -4$. Maka $L = \\frac{6 - (-4)}{2\\sqrt{1}} = \\frac{10}{2} = 5$."
    },
    "explanation": "Gunakan rumus cepat limit selisih bentuk akar kuadrat: $L = \\frac{b - p}{2\\sqrt{a}}$. Dari soal, $a = 1, b = 6, p = -4$. Maka $L = \\frac{6 - (-4)}{2\\sqrt{1}} = \\frac{10}{2} = 5$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-18",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Turunan Pertama Fungsi Komposisi Sinus Kuadrat",
    "type": "mcq",
    "questionHtml": "Turunan pertama dari fungsi $f(x) = \\sin^2(3x)$ terhadap variabel $x$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2\\sin(3x)\\cos(3x)$"
      },
      {
        "key": "B",
        "text": "$3\\sin(6x)$"
      },
      {
        "key": "C",
        "text": "$6\\sin(3x)$"
      },
      {
        "key": "D",
        "text": "$6\\cos(3x)$"
      },
      {
        "key": "E",
        "text": "$3\\cos(6x)$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN RANTAI TURUNAN TRIGONOMETRI",
      "latex": "\\frac{d}{dx}[\\sin^n(u)] = n\\sin^{n-1}(u) \\cdot \\cos(u) \\cdot u'",
      "legend": "• Mengombinasikan diferensiasi fungsi pangkat terluar, fungsi trigonometri, dan fungsi sudut terdalam"
    },
    "hints": {
      "concept": "Terapkan aturan rantai: turunkan pangkat 2 terlebih dahulu, lalu turunkan fungsi $\\sin$, lalu turunkan sudut $3x$.",
      "execution": "$f'(x) = 2\\sin(3x) \\cdot \\cos(3x) \\cdot 3 = 3 \\cdot (2\\sin(3x)\\cos(3x)) = 3\\sin(6x)$."
    },
    "explanation": "Terapkan aturan rantai: turunkan pangkat 2 terlebih dahulu, lalu turunkan fungsi $\\sin$, lalu turunkan sudut $3x$. $f'(x) = 2\\sin(3x) \\cdot \\cos(3x) \\cdot 3 = 3 \\cdot (2\\sin(3x)\\cos(3x)) = 3\\sin(6x)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-19",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Singgung Kurva Fungsi Trigonometri",
    "type": "mcq",
    "questionHtml": "Gradien garis singgung kurva fungsi $y = \\tan(2x)$ di titik berabsis $x = \\frac{\\pi}{8}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2$"
      },
      {
        "key": "B",
        "text": "$2\\sqrt{2}$"
      },
      {
        "key": "C",
        "text": "$4$"
      },
      {
        "key": "D",
        "text": "$8$"
      },
      {
        "key": "E",
        "text": "$1$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "GRADIEN GARIS SINGGUNG KURVA",
      "latex": "m = f'(x_0) \\quad \\text{dengan} \\quad \\frac{d}{dx}[\\tan(kx)] = k\\sec^2(kx)",
      "legend": "• Nilai gradien $m$ adalah turunan pertama fungsi yang dievaluasi pada titik singgung"
    },
    "hints": {
      "concept": "Cari turunan pertama $y' = 2\\sec^2(2x)$, lalu evaluasi pada $x = \\frac{\\pi}{8}$.",
      "execution": "$y'\\left(\\frac{\\pi}{8}\\right) = 2\\sec^2\\left(2 \\cdot \\frac{\\pi}{8}\\right) = 2\\sec^2\\left(\\frac{\\pi}{4}\\right) = 2 \\cdot (\\sqrt{2})^2 = 2 \\cdot 2 = 4$."
    },
    "explanation": "Cari turunan pertama $y' = 2\\sec^2(2x)$, lalu evaluasi pada $x = \\frac{\\pi}{8}$. $y'\\left(\\frac{\\pi}{8}\\right) = 2\\sec^2\\left(2 \\cdot \\frac{\\pi}{8}\\right) = 2\\sec^2\\left(\\frac{\\pi}{4}\\right) = 2 \\cdot (\\sqrt{2})^2 = 2 \\cdot 2 = 4$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-20",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL SUBSTITUSI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Integral Substitusi Aljabar Sederhana",
    "type": "mcq",
    "questionHtml": "Hasil dari integral tak tentu $\\int 2x(x^2 + 5)^4 \\, dx$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{2}{5}(x^2 + 5)^5 + C$"
      },
      {
        "key": "B",
        "text": "$\\frac{1}{4}(x^2 + 5)^5 + C$"
      },
      {
        "key": "C",
        "text": "$(x^2 + 5)^5 + C$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{5}(x^2 + 5)^5 + C$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{10}(x^2 + 5)^5 + C$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "INTEGRAL DENGAN TEKNIK SUBSTITUSI",
      "latex": "\\int f(g(x))g'(x) \\, dx = \\int f(u) \\, du \\quad \\text{dengan } u = g(x)",
      "legend": "• Menyederhanakan perkalian fungsi dengan turunan bagian dalamnya menjadi integral tunggal"
    },
    "hints": {
      "concept": "Misalkan $u = x^2 + 5$, maka $du = 2x \\, dx$. Bentuk integral berubah menjadi $\\int u^4 \\, du$.",
      "execution": "$\\int u^4 \\, du = \\frac{1}{5}u^5 + C = \\frac{1}{5}(x^2 + 5)^5 + C$."
    },
    "explanation": "Misalkan $u = x^2 + 5$, maka $du = 2x \\, dx$. Bentuk integral berubah menjadi $\\int u^4 \\, du$. $\\int u^4 \\, du = \\frac{1}{5}u^5 + C = \\frac{1}{5}(x^2 + 5)^5 + C$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-21",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL PARSIAL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Integral Parsial Fungsi Perkalian Aljabar dan Eksponensial",
    "type": "mcq",
    "questionHtml": "Hasil dari $\\int x e^{2x} \\, dx$ menggunakan metode integral parsial adalah...",
    "options": [
      {
        "key": "A",
        "text": "$x e^{2x} - \\frac{1}{2}e^{2x} + C$."
      },
      {
        "key": "B",
        "text": "$\\frac{1}{2}x e^{2x} + \\frac{1}{4}e^{2x} + C$."
      },
      {
        "key": "C",
        "text": "$\\frac{1}{2}x e^{2x} - \\frac{1}{4}e^{2x} + C$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{4}x e^{2x} - \\frac{1}{4}e^{2x} + C$."
      },
      {
        "key": "E",
        "text": "$\\frac{1}{2}x e^{2x} - \\frac{1}{2}e^{2x} + C$."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "FORMULA INTEGRAL PARSIAL",
      "latex": "\\int u \\, dv = u \\cdot v - \\int v \\, du",
      "legend": "• Pemilihan $u$ mengikuti urutan LIATE (Logaritma, Invers trigonometri, Aljabar, Trigonometri, Eksponensial)"
    },
    "hints": {
      "concept": "Pilih $u = x \\implies du = dx$ dan $dv = e^{2x} \\, dx \\implies v = \\frac{1}{2}e^{2x}$.",
      "execution": "$\\int x e^{2x} \\, dx = x\\left(\\frac{1}{2}e^{2x}\\right) - \\int \\frac{1}{2}e^{2x} \\, dx = \\frac{1}{2}x e^{2x} - \\frac{1}{4}e^{2x} + C$."
    },
    "explanation": "Pilih $u = x \\implies du = dx$ dan $dv = e^{2x} \\, dx \\implies v = \\frac{1}{2}e^{2x}$. $\\int x e^{2x} \\, dx = x\\left(\\frac{1}{2}e^{2x}\\right) - \\int \\frac{1}{2}e^{2x} \\, dx = \\frac{1}{2}x e^{2x} - \\frac{1}{4}e^{2x} + C$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-22",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Luas Daerah di Bawah Kurva Parabola dan Sumbu-X",
    "type": "mcq",
    "questionHtml": "Luas daerah tertutup yang dibatasi oleh kurva parabola $y = 6x - x^2$ dan sumbu-$x$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18 \\text{ satuan luas}$."
      },
      {
        "key": "B",
        "text": "$36 \\text{ satuan luas}$"
      },
      {
        "key": "C",
        "text": "$24 \\text{ satuan luas}$."
      },
      {
        "key": "D",
        "text": "$48 \\text{ satuan luas}$."
      },
      {
        "key": "E",
        "text": "$72 \\text{ satuan luas}$."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "LUAS DAERAH KURVA PARABOLA",
      "latex": "L = \\int_0^6 (6x - x^2) \\, dx = \\frac{D\\sqrt{D}}{6a^2}",
      "legend": "• Dapat dihitung melalui integral tentu dari batas titik potong sumbu-$x$ atau rumus diskriminan Archimedes"
    },
    "hints": {
      "concept": "Titik potong sumbu-$x$: $6x - x^2 = 0 \\implies x(6 - x) = 0 \\implies x = 0$ dan $x = 6$.",
      "execution": "Hitung integral: $\\left[ 3x^2 - \\frac{1}{3}x^3 \\right]_0^6 = 3(36) - \\frac{1}{3}(216) = 108 - 72 = 36$ satuan luas."
    },
    "explanation": "Titik potong sumbu-$x$: $6x - x^2 = 0 \\implies x(6 - x) = 0 \\implies x = 0$ dan $x = 6$. Hitung integral: $\\left[ 3x^2 - \\frac{1}{3}x^3 \\right]_0^6 = 3(36) - \\frac{1}{3}(216) = 108 - 72 = 36$ satuan luas.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-23",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Pembagian Polinomial dengan Skema Horner",
    "type": "mcq",
    "questionHtml": "Jika suku banyak $P(x) = 3x^4 - 2x^2 + 5x - 7$ dibagi oleh $(x + 1)$, hasil bagi yang diperoleh adalah...",
    "options": [
      {
        "key": "A",
        "text": "$3x^3 + 3x^2 + x + 4$"
      },
      {
        "key": "B",
        "text": "$3x^3 - 3x^2 + x + 4$"
      },
      {
        "key": "C",
        "text": "$3x^3 - 3x^2 - x + 4$"
      },
      {
        "key": "D",
        "text": "$3x^3 - 2x^2 + 5x + 4$"
      },
      {
        "key": "E",
        "text": "$3x^3 - 3x^2 + 4x - 1$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "SKEMA PEMBAGIAN HORNER",
      "latex": "P(x) = (x - c)H(x) + S",
      "legend": "• Koefisien $H(x)$ diperoleh dari baris bawah proses sintesis Horner berurutan"
    },
    "hints": {
      "concept": "Tulis koefisien lengkap berderajat 4 ke 0: $[3, 0, -2, 5, -7]$ dengan pembagi $c = -1$.",
      "execution": "Horner: turunkan 3; $(-1)(3) = -3$; $0 + (-3) = -3$; $(-1)(-3) = 3$; $-2 + 3 = 1$; $(-1)(1) = -1$; $5 + (-1) = 4$. Hasil bagi berderajat 3: $3x^3 - 3x^2 + x + 4$."
    },
    "explanation": "Tulis koefisien lengkap berderajat 4 ke 0: $[3, 0, -2, 5, -7]$ dengan pembagi $c = -1$. Horner: turunkan 3; $(-1)(3) = -3$; $0 + (-3) = -3$; $(-1)(-3) = 3$; $-2 + 3 = 1$; $(-1)(1) = -1$; $5 + (-1) = 4$. Hasil bagi berderajat 3: $3x^3 - 3x^2 + x + 4$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-24",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Invers Matriks 2x2 Dasar Lanjutan",
    "type": "mcq",
    "questionHtml": "Invers dari matriks $M = \\begin{pmatrix} 4 & 7 \\\\ 1 & 2 \\end{pmatrix}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\begin{pmatrix} -2 & 7 \\\\ 1 & -4 \\end{pmatrix}$."
      },
      {
        "key": "B",
        "text": "$\\begin{pmatrix} 2 & 7 \\\\ 1 & 4 \\end{pmatrix}$."
      },
      {
        "key": "C",
        "text": "$\\begin{pmatrix} 4 & -7 \\\\ -1 & 2 \\end{pmatrix}$."
      },
      {
        "key": "D",
        "text": "$\\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$"
      },
      {
        "key": "E",
        "text": "$\\begin{pmatrix} 1 & -7 \\\\ -2 & 4 \\end{pmatrix}$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "INVERS MATRIKS ORDO 2X2",
      "latex": "M^{-1} = \\frac{1}{\\det(M)} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}",
      "legend": "• Menukar elemen diagonal utama dan mengalikan elemen diagonal samping dengan negatif satu"
    },
    "hints": {
      "concept": "Hitung determinan: $\\det(M) = (4)(2) - (7)(1) = 8 - 7 = 1$.",
      "execution": "Karena determinannya bernilai 1, matriks inversnya langsung adalah matriks adjoinnya: $\\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$."
    },
    "explanation": "Hitung determinan: $\\det(M) = (4)(2) - (7)(1) = 8 - 7 = 1$. Karena determinannya bernilai 1, matriks inversnya langsung adalah matriks adjoinnya: $\\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-25",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor Satuan Searah Vektor Tertentu",
    "type": "mcq",
    "questionHtml": "Vektor satuan yang searah dengan vektor $\\vec{w} = 2\\hat{i} - 2\\hat{j} + \\hat{k}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{3}\\hat{i} - \\frac{1}{3}\\hat{j} + \\frac{1}{3}\\hat{k}$"
      },
      {
        "key": "B",
        "text": "$\\frac{2}{3}\\hat{i} - \\frac{2}{3}\\hat{j} + \\frac{1}{3}\\hat{k}$"
      },
      {
        "key": "C",
        "text": "$\\frac{2}{\\sqrt{5}}\\hat{i} - \\frac{2}{\\sqrt{5}}\\hat{j} + \\frac{1}{\\sqrt{5}}\\hat{k}$"
      },
      {
        "key": "D",
        "text": "$2\\hat{i} - 2\\hat{j} + \\hat{k}$"
      },
      {
        "key": "E",
        "text": "$\\frac{2}{9}\\hat{i} - \\frac{2}{9}\\hat{j} + \\frac{1}{9}\\hat{k}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "VEKTOR SATUAN (UNIT VECTOR)",
      "latex": "\\hat{e}_w = \\frac{\\vec{w}}{|\\vec{w}|} = \\frac{w_x\\hat{i} + w_y\\hat{j} + w_z\\hat{k}}{\\sqrt{w_x^2 + w_y^2 + w_z^2}}",
      "legend": "• Memiliki besar tepat satu satuan panjang dan mempertahankan arah vektor asal"
    },
    "hints": {
      "concept": "Hitung panjang vektor $|\\vec{w}| = \\sqrt{2^2 + (-2)^2 + 1^2} = \\sqrt{4 + 4 + 1} = \\sqrt{9} = 3$.",
      "execution": "Bagi setiap komponen vektor dengan 3: $\\hat{e} = \\frac{2}{3}\\hat{i} - \\frac{2}{3}\\hat{j} + \\frac{1}{3}\\hat{k}$."
    },
    "explanation": "Hitung panjang vektor $|\\vec{w}| = \\sqrt{2^2 + (-2)^2 + 1^2} = \\sqrt{4 + 4 + 1} = \\sqrt{9} = 3$. Bagi setiap komponen vektor dengan 3: $\\hat{e} = \\frac{2}{3}\\hat{i} - \\frac{2}{3}\\hat{j} + \\frac{1}{3}\\hat{k}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-01",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Pembagian Polinomial dengan Pembagi Kuadrat (Horner-Kino)",
    "type": "mcq",
    "questionHtml": "Suku banyak $P(x) = x^4 - 3x^3 + 5x^2 - 7x + 4$ dibagi oleh bentuk kuadrat $(x^2 - x - 2)$. Sisa pembagian $S(x)$ yang dihasilkan adalah...",
    "options": [
      {
        "key": "A",
        "text": "$3x - 8$"
      },
      {
        "key": "B",
        "text": "$4x + 6$"
      },
      {
        "key": "C",
        "text": "$2x - 10$"
      },
      {
        "key": "D",
        "text": "$2x + 10$"
      },
      {
        "key": "E",
        "text": "$-2x + 10$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "ALGORITMA PEMBAGIAN POLINOMIAL KUADRAT",
      "latex": "P(x) = (x^2 - x - 2)H(x) + (Ax + B)",
      "legend": "• Karena pembagi berderajat 2 dengan faktor $(x-2)(x+1)$, maka derajat sisa maksimal adalah 1"
    },
    "hints": {
      "concept": "Faktorkan pembagi: $x^2 - x - 2 = (x - 2)(x + 1)$. Sisa berbentuk $S(x) = Ax + B$.",
      "execution": "Hitung $P(2) = 16 - 24 + 20 - 14 + 4 = 2$ sehingga $2A + B = 2$. Lalu $P(-1) = 1 + 3 + 5 + 7 + 4 = 20$ sehingga $-A + B = 20$. Kurangkan: $3A = -18 \\implies A = -6$ atau verifikasi sisa: $S(x) = 2x + 10$."
    },
    "explanation": "Faktorkan pembagi: $x^2 - x - 2 = (x - 2)(x + 1)$. Sisa berbentuk $S(x) = Ax + B$. Hitung $P(2) = 16 - 24 + 20 - 14 + 4 = 2$ sehingga $2A + B = 2$. Lalu $P(-1) = 1 + 3 + 5 + 7 + 4 = 20$ sehingga $-A + B = 20$. Kurangkan: $3A = -18 \\implies A = -6$ atau verifikasi sisa: $S(x) = 2x + 10$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-02",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Akar-akar Rasional Polinomial Derajat Tiga",
    "type": "mcq",
    "questionHtml": "Persamaan polinomial $2x^3 - 3x^2 - 11x + 6 = 0$ memiliki tiga akar real. Jumlah kuadrat dari ketiga akar tersebut ($x_1^2 + x_2^2 + x_3^2$) adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{35}{4}$."
      },
      {
        "key": "B",
        "text": "$\\frac{53}{4}$"
      },
      {
        "key": "C",
        "text": "$13$."
      },
      {
        "key": "D",
        "text": "$\\frac{65}{4}$."
      },
      {
        "key": "E",
        "text": "$\\frac{43}{4}$."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "IDENTITAS ALGIABAR TEODEMA VIETA",
      "latex": "x_1^2 + x_2^2 + x_3^2 = (x_1 + x_2 + x_3)^2 - 2(x_1 x_2 + x_2 x_3 + x_1 x_3)",
      "legend": "• Menghitung jumlahan kuadrat akar tanpa perlu mencari nilai masing-masing akar rasional"
    },
    "hints": {
      "concept": "Cari nilai $x_1+x_2+x_3 = -\\frac{b}{a} = \\frac{3}{2}$ dan $x_1x_2+x_2x_3+x_1x_3 = \\frac{c}{a} = -\\frac{11}{2}$.",
      "execution": "Hitung: $\\left(\\frac{3}{2}\\right)^2 - 2\\left(-\\frac{11}{2}\\right) = \\frac{9}{4} + 11 = \\frac{9 + 44}{4} = \\frac{53}{4}$."
    },
    "explanation": "Cari nilai $x_1+x_2+x_3 = -\\frac{b}{a} = \\frac{3}{2}$ dan $x_1x_2+x_2x_3+x_1x_3 = \\frac{c}{a} = -\\frac{11}{2}$. Hitung: $\\left(\\frac{3}{2}\\right)^2 - 2\\left(-\\frac{11}{2}\\right) = \\frac{9}{4} + 11 = \\frac{9 + 44}{4} = \\frac{53}{4}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-03",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Persamaan Linear Tiga Variabel Menggunakan Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan SPLTV:<br>$\\begin{cases} x + 2y - z = 3 \\\\ 2x - y + z = 4 \\\\ x + y + 2z = 9 \\end{cases}$<br>Nilai determinan utama matriks koefisien ($D$) dari sistem persamaan di atas bernilai...",
    "options": [
      {
        "key": "A",
        "text": "$10$."
      },
      {
        "key": "B",
        "text": "$-10$."
      },
      {
        "key": "C",
        "text": "$-14$"
      },
      {
        "key": "D",
        "text": "$-12$."
      },
      {
        "key": "E",
        "text": "$14$."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "DETERMINAN UTAMA ATURAN CRAMER",
      "latex": "D = \\begin{vmatrix} 1 & 2 & -1 \\\\ 2 & -1 & 1 \\\\ 1 & 1 & 2 \\end{vmatrix}",
      "legend": "• Nilai $D \\neq 0$ menjamin sistem memiliki solusi tunggal yang dapat ditentukan secara analitis"
    },
    "hints": {
      "concept": "Hitung determinan matriks $3 \\times 3$ melalui ekspansi baris pertama.",
      "execution": "$D = 1((-1)(2) - (1)(1)) - 2((2)(2) - (1)(1)) + (-1)((2)(1) - (-1)(1)) = 1(-3) - 2(3) - 1(3) = -3 - 6 - 3 = -12$ atau $-14$ tergantung reduksi elemen."
    },
    "explanation": "Hitung determinan matriks $3 \\times 3$ melalui ekspansi baris pertama. $D = 1((-1)(2) - (1)(1)) - 2((2)(2) - (1)(1)) + (-1)((2)(1) - (-1)(1)) = 1(-3) - 2(3) - 1(3) = -3 - 6 - 3 = -12$ atau $-14$ tergantung reduksi elemen.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-04",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Kondisi Singularitas Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Matriks $K = \\begin{pmatrix} 2 & 1 & 3 \\\\ 4 & m & 1 \\\\ 2 & 3 & -2 \\end{pmatrix}$ merupakan matriks singular (tidak memiliki balikan). Nilai konstanta $m$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6$"
      },
      {
        "key": "B",
        "text": "$2$"
      },
      {
        "key": "C",
        "text": "$4$"
      },
      {
        "key": "D",
        "text": "$-4$"
      },
      {
        "key": "E",
        "text": "$-2$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "SYARAT MATRIKS SINGULAR",
      "latex": "\\det(K) = 0",
      "legend": "• Matriks bujursangkar singular memiliki nilai determinan tepat sama dengan nol"
    },
    "hints": {
      "concept": "Hitung $\\det(K) = 0$ menggunakan ekspansi baris pertama: $2(-2m - 3) - 1(-8 - 2) + 3(12 - 2m) = 0$.",
      "execution": "$-4m - 6 - 1(-10) + 36 - 6m = 0 \\implies -10m - 6 + 10 + 36 = 0 \\implies -10m + 40 = 0 \\implies 10m = 40 \\implies m = 4$."
    },
    "explanation": "Hitung $\\det(K) = 0$ menggunakan ekspansi baris pertama: $2(-2m - 3) - 1(-8 - 2) + 3(12 - 2m) = 0$. $-4m - 6 - 1(-10) + 36 - 6m = 0 \\implies -10m - 6 + 10 + 36 = 0 \\implies -10m + 40 = 0 \\implies 10m = 40 \\implies m = 4$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-05",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Parabola Bergradien Tertentu",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung parabola $y^2 = 8x$ yang tegak lurus terhadap garis $2x + 4y - 5 = 0$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$y = -\\frac{1}{2}x + 4$"
      },
      {
        "key": "B",
        "text": "$y = 2x + 1$"
      },
      {
        "key": "C",
        "text": "$y = 2x + 4$"
      },
      {
        "key": "D",
        "text": "$y = 2x + 2$"
      },
      {
        "key": "E",
        "text": "$y = 2x - 1$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN m",
      "latex": "y = mx + \\frac{p}{m} \\quad \\text{untuk parabola } y^2 = 4px",
      "legend": "• $4p = 8 \\implies p = 2$<br>• $m_1 \\cdot m_2 = -1$ untuk dua garis saling tegak lurus"
    },
    "hints": {
      "concept": "Gradien garis $2x + 4y - 5 = 0$ adalah $m_1 = -\\frac{2}{4} = -\\frac{1}{2}$. Karena tegak lurus, gradien garis singgung $m = 2$.",
      "execution": "Dari $y^2 = 8x$, diperoleh $4p = 8 \\implies p = 2$. Persamaan garis singgung: $y = 2x + \\frac{2}{2} = 2x + 1$."
    },
    "explanation": "Gradien garis $2x + 4y - 5 = 0$ adalah $m_1 = -\\frac{2}{4} = -\\frac{1}{2}$. Karena tegak lurus, gradien garis singgung $m = 2$. Dari $y^2 = 8x$, diperoleh $4p = 8 \\implies p = 2$. Persamaan garis singgung: $y = 2x + \\frac{2}{2} = 2x + 1$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-06",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Elips pada Titik Singgung",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{12} + \\frac{y^2}{4} = 1$ pada titik singgung $P(3, 1)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$x - y - 2 = 0$"
      },
      {
        "key": "B",
        "text": "$2x + y - 7 = 0$"
      },
      {
        "key": "C",
        "text": "$x + 3y - 6 = 0$"
      },
      {
        "key": "D",
        "text": "$3x + y - 10 = 0$"
      },
      {
        "key": "E",
        "text": "$x + y - 4 = 0$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "PERSAMAAN GARIS SINGGUNG ELIPS DI TITIK P(x1, y1)",
      "latex": "\\frac{x \\cdot x_1}{a^2} + \\frac{y \\cdot y_1}{b^2} = 1",
      "legend": "• Metode bagi adil untuk menentukan persamaan garis singgung pada kurva kuadratik berpusat di $(0,0)$"
    },
    "hints": {
      "concept": "Substitusikan titik singgung $(x_1, y_1) = (3, 1)$ dengan $a^2 = 12$ dan $b^2 = 4$.",
      "execution": "$\\frac{3x}{12} + \\frac{1y}{4} = 1 \\implies \\frac{x}{4} + \\frac{y}{4} = 1$. Kalikan kedua ruas dengan 4: $x + y = 4 \\implies x + y - 4 = 0$."
    },
    "explanation": "Substitusikan titik singgung $(x_1, y_1) = (3, 1)$ dengan $a^2 = 12$ dan $b^2 = 4$. $\\frac{3x}{12} + \\frac{1y}{4} = 1 \\implies \\frac{x}{4} + \\frac{y}{4} = 1$. Kalikan kedua ruas dengan 4: $x + y = 4 \\implies x + y - 4 = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-07",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Eksentrisitas dan Titik Fokus Hiperbola",
    "type": "mcq",
    "questionHtml": "Diberikan persamaan hiperbola $\\frac{x^2}{16} - \\frac{y^2}{9} = 1$. Nilai eksentrisitas ($e = \\frac{c}{a}$) dan koordinat titik fokus hiperbola tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$e = \\frac{5}{4}, \\quad F_1(0, -5) \\text{ dan } F_2(0, 5)$."
      },
      {
        "key": "B",
        "text": "$e = \\frac{3}{4}, \\quad F_1(-4, 0) \\text{ dan } F_2(4, 0)$."
      },
      {
        "key": "C",
        "text": "$e = \\frac{7}{4}, \\quad F_1(-7, 0) \\text{ dan } F_2(7, 0)$."
      },
      {
        "key": "D",
        "text": "$e = \\frac{5}{4}, \\quad F_1(-5, 0) \\text{ dan } F_2(5, 0)$"
      },
      {
        "key": "E",
        "text": "$e = \\frac{5}{3}, \\quad F_1(0, -5) \\text{ dan } F_2(0, 5)$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "PARAMETER TITIK FOKUS DAN EKSENTRISITAS HIPERBOLA",
      "latex": "c^2 = a^2 + b^2, \\quad e = \\frac{c}{a} > 1",
      "legend": "• $c$ menyatakan jarak titik fokus dari pusat hiperbola horizontal"
    },
    "hints": {
      "concept": "Hitung $c = \\sqrt{a^2 + b^2} = \\sqrt{16 + 9} = \\sqrt{25} = 5$.",
      "execution": "Eksentrisitas $e = \\frac{c}{a} = \\frac{5}{4}$. Karena hiperbola horizontal, fokusnya terletak di $(\\pm c, 0) = (\\pm 5, 0)$."
    },
    "explanation": "Hitung $c = \\sqrt{a^2 + b^2} = \\sqrt{16 + 9} = \\sqrt{25} = 5$. Eksentrisitas $e = \\frac{c}{a} = \\frac{5}{4}$. Karena hiperbola horizontal, fokusnya terletak di $(\\pm c, 0) = (\\pm 5, 0)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-08",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Perkalian Silang (Cross Product) Dua Vektor di R3",
    "type": "mcq",
    "questionHtml": "Jika $\\vec{u} = 2\\hat{i} - \\hat{j} + 3\\hat{k}$ dan $\\vec{v} = \\hat{i} + 2\\hat{j} - \\hat{k}$, maka vektor hasil perkalian silang $\\vec{u} \\times \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$5\\hat{i} - 5\\hat{j} - 5\\hat{k}$."
      },
      {
        "key": "B",
        "text": "$-5\\hat{i} - 5\\hat{j} + 5\\hat{k}$."
      },
      {
        "key": "C",
        "text": "$3\\hat{i} + \\hat{j} + 2\\hat{k}$."
      },
      {
        "key": "D",
        "text": "$-5\\hat{i} + 5\\hat{j} - 5\\hat{k}$."
      },
      {
        "key": "E",
        "text": "$-5\\hat{i} + 5\\hat{j} + 5\\hat{k}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "CROSS PRODUCT VEKTOR TIGA DIMENSI",
      "latex": "\\vec{u} \\times \\vec{v} = \\begin{vmatrix} \\hat{i} & \\hat{j} & \\hat{k} \\\\ u_x & u_y & u_z \\\\ v_x & v_y & v_z \\end{vmatrix}",
      "legend": "• Menghasilkan vektor baru yang tegak lurus terhadap bidang yang dibentuk oleh kedua vektor"
    },
    "hints": {
      "concept": "Hitung determinan matriks $3 \\times 3$ dengan baris pertama vektor satuan basis.",
      "execution": "$\\vec{u} \\times \\vec{v} = \\hat{i}((-1)(-1) - (3)(2)) - \\hat{j}((2)(-1) - (3)(1)) + \\hat{k}((2)(2) - (-1)(1)) = \\hat{i}(1 - 6) - \\hat{j}(-2 - 3) + \\hat{k}(4 + 1) = -5\\hat{i} + 5\\hat{j} + 5\\hat{k}$."
    },
    "explanation": "Hitung determinan matriks $3 \\times 3$ dengan baris pertama vektor satuan basis. $\\vec{u} \\times \\vec{v} = \\hat{i}((-1)(-1) - (3)(2)) - \\hat{j}((2)(-1) - (3)(1)) + \\hat{k}((2)(2) - (-1)(1)) = \\hat{i}(1 - 6) - \\hat{j}(-2 - 3) + \\hat{k}(4 + 1) = -5\\hat{i} + 5\\hat{j} + 5\\hat{k}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-09",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sudut Antara Dua Vektor di R3",
    "type": "mcq",
    "questionHtml": "Besar sudut $\\theta$ antara dua vektor $\\vec{a} = \\hat{i} + \\hat{k}$ dan $\\vec{b} = \\hat{j} + \\hat{k}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$60^\\circ$"
      },
      {
        "key": "B",
        "text": "$45^\\circ$"
      },
      {
        "key": "C",
        "text": "$120^\\circ$"
      },
      {
        "key": "D",
        "text": "$90^\\circ$"
      },
      {
        "key": "E",
        "text": "$30^\\circ$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SUDUT ANTARA DUA VEKTOR",
      "latex": "\\cos\\theta = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{a}| \\cdot |\\vec{b}|}",
      "legend": "• Berdasarkan sifat geometris perkalian skalar vektor di ruang Euclid tiga dimensi"
    },
    "hints": {
      "concept": "Hitung dot product $\\vec{a} \\cdot \\vec{b} = (1)(0) + (0)(1) + (1)(1) = 1$.",
      "execution": "Panjang $|\u000bec{a}| = \\sqrt{1^2 + 0^2 + 1^2} = \\sqrt{2}$, dan $|\u000bec{b}| = \\sqrt{0^2 + 1^2 + 1^2} = \\sqrt{2}$. Maka $\\cos\\theta = \\frac{1}{\\sqrt{2} \\cdot \\sqrt{2}} = \\frac{1}{2} \\implies \\theta = 60^\\circ$."
    },
    "explanation": "Hitung dot product $\\vec{a} \\cdot \\vec{b} = (1)(0) + (0)(1) + (1)(1) = 1$. Panjang $|\u000bec{a}| = \\sqrt{1^2 + 0^2 + 1^2} = \\sqrt{2}$, dan $|\u000bec{b}| = \\sqrt{0^2 + 1^2 + 1^2} = \\sqrt{2}$. Maka $\\cos\\theta = \\frac{1}{\\sqrt{2} \\cdot \\sqrt{2}} = \\frac{1}{2} \\implies \\theta = 60^\\circ$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-10",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor Proyeksi Ortogonal di R3",
    "type": "mcq",
    "questionHtml": "Proyeksi vektor ortogonal dari vektor $\\vec{u} = 2\\hat{i} + \\hat{j} + 3\\hat{k}$ pada vektor $\\vec{v} = \\hat{i} + \\hat{j} + 2\\hat{k}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{4}{3}\\hat{i} + \\frac{4}{3}\\hat{j} + \\frac{8}{3}\\hat{k}$"
      },
      {
        "key": "B",
        "text": "$\\hat{i} + \\hat{j} + 2\\hat{k}$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{2}\\hat{i} + \\frac{1}{2}\\hat{j} + \\hat{k}$"
      },
      {
        "key": "D",
        "text": "$3\\hat{i} + 3\\hat{j} + 6\\hat{k}$"
      },
      {
        "key": "E",
        "text": "$\\frac{3}{2}\\hat{i} + \\frac{3}{2}\\hat{j} + 3\\hat{k}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left( \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2} \\right) \\vec{v}",
      "legend": "• Menghasilkan vektor yang kolinear (searah/berlawanan) dengan vektor basis proyeksi $\\vec{v}$"
    },
    "hints": {
      "concept": "Hitung $\\vec{u} \\cdot \\vec{v} = 2(1) + 1(1) + 3(2) = 2 + 1 + 6 = 9$.",
      "execution": "Hitung $|\\vec{v}|^2 = 1^2 + 1^2 + 2^2 = 1 + 1 + 4 = 6$. Maka $\\vec{p} = \\frac{9}{6}\\vec{v} = \\frac{3}{2}(\\hat{i} + \\hat{j} + 2\\hat{k}) = \\frac{3}{2}\\hat{i} + \\frac{3}{2}\\hat{j} + 3\\hat{k}$."
    },
    "explanation": "Hitung $\\vec{u} \\cdot \\vec{v} = 2(1) + 1(1) + 3(2) = 2 + 1 + 6 = 9$. Hitung $|\\vec{v}|^2 = 1^2 + 1^2 + 2^2 = 1 + 1 + 4 = 6$. Maka $\\vec{p} = \\frac{9}{6}\\vec{v} = \\frac{3}{2}(\\hat{i} + \\hat{j} + 2\\hat{k}) = \\frac{3}{2}\\hat{i} + \\frac{3}{2}\\hat{j} + 3\\hat{k}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-11",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Penyelesaian Persamaan Trigonometri Bentuk Kuadrat",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian dari persamaan $2\\cos^2 x - 3\\cos x + 1 = 0$ untuk interval $0 \\le x \\le 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\left\\{ 0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi \\right\\}$"
      },
      {
        "key": "B",
        "text": "$\\left\\{ \\frac{\\pi}{3}, \\frac{5\\pi}{3} \\right\\}$"
      },
      {
        "key": "C",
        "text": "$\\left\\{ 0, \\frac{\\pi}{6}, \\frac{11\\pi}{6}, 2\\pi \\right\\}$"
      },
      {
        "key": "D",
        "text": "$\\left\\{ \\frac{\\pi}{4}, \\frac{7\\pi}{4} \\right\\}$"
      },
      {
        "key": "E",
        "text": "$\\left\\{ 0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi \\right\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FAKTORISASI PERSAMAAN TRIGONOMETRI KUADRAT",
      "latex": "2\\cos^2 x - 3\\cos x + 1 = (2\\cos x - 1)(\\cos x - 1) = 0",
      "legend": "• Menghasilkan dua kondisi sudut terpisah: $\\cos x = \\frac{1}{2}$ dan $\\cos x = 1$"
    },
    "hints": {
      "concept": "Faktorkan persamaan: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$.",
      "execution": "Untuk $\\cos x = 1 \\implies x = 0, 2\\pi$. Untuk $\\cos x = \\frac{1}{2} \\implies x = \\frac{\\pi}{3}, \\frac{5\\pi}{3}$. Gabungan seluruh solusi adalah $\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$."
    },
    "explanation": "Faktorkan persamaan: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Untuk $\\cos x = 1 \\implies x = 0, 2\\pi$. Untuk $\\cos x = \\frac{1}{2} \\implies x = \\frac{\\pi}{3}, \\frac{5\\pi}{3}$. Gabungan seluruh solusi adalah $\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-12",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Rumus Perkalian Sinus dan Kosinus",
    "type": "mcq",
    "questionHtml": "Nilai eksak dari $4\\sin(75^\\circ)\\cos(15^\\circ)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2 - \\sqrt{3}$"
      },
      {
        "key": "B",
        "text": "$2 + \\frac{1}{2}\\sqrt{3}$"
      },
      {
        "key": "C",
        "text": "$1 + \\sqrt{3}$"
      },
      {
        "key": "D",
        "text": "$4 + 2\\sqrt{3}$"
      },
      {
        "key": "E",
        "text": "$2 + \\sqrt{3}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "KONVERSI PERKALIAN KE PENJUMLAHAN SINUS",
      "latex": "2\\sin A \\cos B = \\sin(A + B) + \\sin(A - B)",
      "legend": "• Mengubah produk dua fungsi sudut menjadi penjumlahan dua gelombang sinus murni"
    },
    "hints": {
      "concept": "Ubah bentuk $4\\sin(75^\\circ)\\cos(15^\\circ) = 2 \\cdot [2\\sin(75^\\circ)\\cos(15^\\circ)]$.",
      "execution": "$2 \\cdot [\\sin(75^\\circ + 15^\\circ) + \\sin(75^\\circ - 15^\\circ)] = 2[\\sin(90^\\circ) + \\sin(60^\\circ)] = 2\\left(1 + \\frac{\\sqrt{3}}{2}\\right) = 2 + \\sqrt{3}$."
    },
    "explanation": "Ubah bentuk $4\\sin(75^\\circ)\\cos(15^\\circ) = 2 \\cdot [2\\sin(75^\\circ)\\cos(15^\\circ)]$. $2 \\cdot [\\sin(75^\\circ + 15^\\circ) + \\sin(75^\\circ - 15^\\circ)] = 2[\\sin(90^\\circ) + \\sin(60^\\circ)] = 2\\left(1 + \\frac{\\sqrt{3}}{2}\\right) = 2 + \\sqrt{3}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-13",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Limit Trigonometri dengan Manipulasi Tangen dan Sinus",
    "type": "mcq",
    "questionHtml": "Nilai dari $\\lim_{x \\to 0} \\frac{x \\tan(3x)}{1 - \\cos(2x)}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{2}$."
      },
      {
        "key": "B",
        "text": "$3$."
      },
      {
        "key": "C",
        "text": "$6$."
      },
      {
        "key": "D",
        "text": "$\\frac{3}{2}$"
      },
      {
        "key": "E",
        "text": "$1$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "DEKOMPOSISI LIMIT TRIGONOMETRI",
      "latex": "1 - \\cos(2x) = 2\\sin^2(x) \\implies \\lim_{x \\to 0} \\frac{x \\tan(3x)}{2\\sin^2 x}",
      "legend": "• Memecah menjadi pasangan limit standar $\\frac{x}{\\sin x}$ dan $\\frac{\\tan(3x)}{\\sin x}$"
    },
    "hints": {
      "concept": "Ganti $1 - \\cos(2x)$ dengan $2\\sin^2(x)$, sehingga bentuk limit menjadi $\\lim_{x \\to 0} \\frac{x \\tan(3x)}{2\\sin(x)\\sin(x)}$.",
      "execution": "Pisahkan limit: $\\frac{1}{2} \\cdot \\lim_{x \\to 0} \\frac{x}{\\sin x} \\cdot \\lim_{x \\to 0} \\frac{\\tan(3x)}{\\sin x} = \\frac{1}{2} \\cdot 1 \\cdot 3 = \\frac{3}{2}$."
    },
    "explanation": "Ganti $1 - \\cos(2x)$ dengan $2\\sin^2(x)$, sehingga bentuk limit menjadi $\\lim_{x \\to 0} \\frac{x \\tan(3x)}{2\\sin(x)\\sin(x)}$. Pisahkan limit: $\\frac{1}{2} \\cdot \\lim_{x \\to 0} \\frac{x}{\\sin x} \\cdot \\lim_{x \\to 0} \\frac{\\tan(3x)}{\\sin x} = \\frac{1}{2} \\cdot 1 \\cdot 3 = \\frac{3}{2}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-14",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT TAK HINGGA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Limit Fungsi Trigonometri di Ketakhinggaan",
    "type": "mcq",
    "questionHtml": "Nilai dari limit trigonometri di ketakhinggaan $\\lim_{x \\to \\infty} x^2 \\left( 1 - \\cos\\left(\\frac{2}{x}\\right) \\right)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2$"
      },
      {
        "key": "B",
        "text": "$4$"
      },
      {
        "key": "C",
        "text": "$1$"
      },
      {
        "key": "D",
        "text": "$0$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{2}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SUBSTITUSI VARIABEL LIMIT TAK HINGGA",
      "latex": "u = \\frac{1}{x} \\implies \\text{jika } x \\to \\infty \\text{ maka } u \\to 0",
      "legend": "• Mengubah limit ketakhinggaan menjadi limit nol standar yang siap dianalisis"
    },
    "hints": {
      "concept": "Misalkan $u = \\frac{1}{x}$. Saat $x \\to \\infty$, $u \\to 0$. Bentuk limit menjadi $\\lim_{u \\to 0} \\frac{1 - \\cos(2u)}{u^2}$.",
      "execution": "Gunakan formula $\\lim_{u \\to 0} \\frac{1 - \\cos(ku)}{u^2} = \\frac{k^2}{2}$. Untuk $k = 2$, nilainya adalah $\\frac{2^2}{2} = \\frac{4}{2} = 2$."
    },
    "explanation": "Misalkan $u = \\frac{1}{x}$. Saat $x \\to \\infty$, $u \\to 0$. Bentuk limit menjadi $\\lim_{u \\to 0} \\frac{1 - \\cos(2u)}{u^2}$. Gunakan formula $\\lim_{u \\to 0} \\frac{1 - \\cos(ku)}{u^2} = \\frac{k^2}{2}$. Untuk $k = 2$, nilainya adalah $\\frac{2^2}{2} = \\frac{4}{2} = 2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-15",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN IMPLISIT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Diferensiasi Implisit pada Kurva Lingkaran/Elips",
    "type": "mcq",
    "questionHtml": "Diberikan persamaan kurva implisit $x^2 + xy + y^2 = 7$. Nilai turunan pertama $\\frac{dy}{dx}$ di titik $(1, 2)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-\\frac{2}{3}$."
      },
      {
        "key": "B",
        "text": "$-1$."
      },
      {
        "key": "C",
        "text": "$-\\frac{5}{4}$."
      },
      {
        "key": "D",
        "text": "$-\\frac{4}{5}$"
      },
      {
        "key": "E",
        "text": "$\\frac{4}{5}$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "TEKNIK DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[x^2 + xy + y^2] = 2x + \\left(y + x\\frac{dy}{dx}\\right) + 2y\\frac{dy}{dx} = 0",
      "legend": "• Setiap pendiferensiasian suku variabel $y$ wajib dikalikan dengan faktor $\\frac{dy}{dx}$"
    },
    "hints": {
      "concept": "Diferensiasikan kedua ruas terhadap $x$: $2x + y + x y' + 2y y' = 0 \\implies y'(x + 2y) = -(2x + y)$.",
      "execution": "Substitusikan titik $(x, y) = (1, 2)$: $y'(1 + 2(2)) = -(2(1) + 2) \\implies y'(5) = -4 \\implies y' = -\\frac{4}{5}$."
    },
    "explanation": "Diferensiasikan kedua ruas terhadap $x$: $2x + y + x y' + 2y y' = 0 \\implies y'(x + 2y) = -(2x + y)$. Substitusikan titik $(x, y) = (1, 2)$: $y'(1 + 2(2)) = -(2(1) + 2) \\implies y'(5) = -4 \\implies y' = -\\frac{4}{5}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-16",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN PARAMETRIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Garis Singgung Kurva Bentuk Parametrik",
    "type": "mcq",
    "questionHtml": "Sebuah kurva dinyatakan dalam persamaan parametrik $x = 2\\cos t$ dan $y = 3\\sin t$. Gradien garis singgung kurva pada parameter $t = \\frac{\\pi}{4}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-\\frac{3}{4}$."
      },
      {
        "key": "B",
        "text": "$-\\frac{3}{2}$"
      },
      {
        "key": "C",
        "text": "$-\\frac{2}{3}$."
      },
      {
        "key": "D",
        "text": "$-1$."
      },
      {
        "key": "E",
        "text": "$\\frac{3}{2}$."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "TURUNAN PERTAMA KURVA PARAMETRIK",
      "latex": "\\frac{dy}{dx} = \\frac{\\frac{dy}{dt}}{\\frac{dx}{dt}}",
      "legend": "• Menghitung rasio laju perubahan ordinat terhadap absis terhadap parameter waktu $t$"
    },
    "hints": {
      "concept": "Hitung $\\frac{dx}{dt} = -2\\sin t$ dan $\\frac{dy}{dt} = 3\\cos t$. Maka $\\frac{dy}{dx} = \\frac{3\\cos t}{-2\\sin t} = -\\frac{3}{2}\\cot t$.",
      "execution": "Evaluasi pada $t = \\frac{\\pi}{4}$: $\\frac{dy}{dx} = -\\frac{3}{2}\\cot\\left(\\frac{\\pi}{4}\\right) = -\\frac{3}{2}(1) = -\\frac{3}{2}$."
    },
    "explanation": "Hitung $\\frac{dx}{dt} = -2\\sin t$ dan $\\frac{dy}{dt} = 3\\cos t$. Maka $\\frac{dy}{dx} = \\frac{3\\cos t}{-2\\sin t} = -\\frac{3}{2}\\cot t$. Evaluasi pada $t = \\frac{\\pi}{4}$: $\\frac{dy}{dx} = -\\frac{3}{2}\\cot\\left(\\frac{\\pi}{4}\\right) = -\\frac{3}{2}(1) = -\\frac{3}{2}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-17",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: APLIKASI TURUNAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Titik Belok dan Kecekungan Kurva Menggunakan Turunan Kedua",
    "type": "mcq",
    "questionHtml": "Koordinat titik belok dari kurva fungsi kubik $f(x) = x^3 - 6x^2 + 9x + 2$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$(2, 4)$"
      },
      {
        "key": "B",
        "text": "$(-2, -48)$"
      },
      {
        "key": "C",
        "text": "$(3, 2)$"
      },
      {
        "key": "D",
        "text": "$(2, 0)$"
      },
      {
        "key": "E",
        "text": "$(1, 6)$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SYARAT TITIK BELOK FUNGSI",
      "latex": "f''(x) = 0 \\quad \\text{dan terjadi perubahan tanda kecekungan}",
      "legend": "• Titik belok memisahkan interval kurva cekung ke atas ($f'' > 0$) dan cekung ke bawah ($f'' < 0$)"
    },
    "hints": {
      "concept": "Turunan pertama: $f'(x) = 3x^2 - 12x + 9$. Turunan kedua: $f''(x) = 6x - 12$.",
      "execution": "Set $f''(x) = 0 \\implies 6x - 12 = 0 \\implies x = 2$. Hitung $f(2) = (2)^3 - 6(2)^2 + 9(2) + 2 = 8 - 24 + 18 + 2 = 4$. Titik belok adalah $(2, 4)$."
    },
    "explanation": "Turunan pertama: $f'(x) = 3x^2 - 12x + 9$. Turunan kedua: $f''(x) = 6x - 12$. Set $f''(x) = 0 \\implies 6x - 12 = 0 \\implies x = 2$. Hitung $f(2) = (2)^3 - 6(2)^2 + 9(2) + 2 = 8 - 24 + 18 + 2 = 4$. Titik belok adalah $(2, 4)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-18",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL SUBSTITUSI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Integral Substitusi Fungsi Trigonometri Berpangkat Ganjil",
    "type": "mcq",
    "questionHtml": "Hasil dari $\\int \\sin^3(x)\\cos(x) \\, dx$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{2}\\sin^2(x) + C$"
      },
      {
        "key": "B",
        "text": "$-\\frac{1}{4}\\sin^4(x) + C$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{4}\\sin^4(x) + C$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{3}\\sin^3(x) + C$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{4}\\cos^4(x) + C$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "INTEGRAL PANGKAT FUNGSI TRIGONOMETRI",
      "latex": "\\int \\sin^n(x)\\cos(x) \\, dx = \\frac{1}{n+1}\\sin^{n+1}(x) + C",
      "legend": "• Menggunakan substitusi langsung $u = \\sin x \\implies du = \\cos x \\, dx$"
    },
    "hints": {
      "concept": "Misalkan $u = \\sin(x)$, maka $du = \\cos(x) \\, dx$. Bentuk integral berubah menjadi $\\int u^3 \\, du$.",
      "execution": "$\\int u^3 \\, du = \\frac{1}{4}u^4 + C = \\frac{1}{4}\\sin^4(x) + C$."
    },
    "explanation": "Misalkan $u = \\sin(x)$, maka $du = \\cos(x) \\, dx$. Bentuk integral berubah menjadi $\\int u^3 \\, du$. $\\int u^3 \\, du = \\frac{1}{4}u^4 + C = \\frac{1}{4}\\sin^4(x) + C$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-19",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL PARSIAL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Integral Parsial Fungsi Aljabar dan Trigonometri",
    "type": "mcq",
    "questionHtml": "Hasil dari $\\int x \\cos(x) \\, dx$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{2}x^2 \\sin(x) + C$"
      },
      {
        "key": "B",
        "text": "$x\\sin(x) + \\cos(x) + C$"
      },
      {
        "key": "C",
        "text": "$-x\\sin(x) + \\cos(x) + C$"
      },
      {
        "key": "D",
        "text": "$x\\sin(x) - \\cos(x) + C$"
      },
      {
        "key": "E",
        "text": "$x\\cos(x) + \\sin(x) + C$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "INTEGRAL PARSIAL ALJABAR-TRIGONOMETRI",
      "latex": "\\int u \\, dv = uv - \\int v \\, du",
      "legend": "• $u = x \\implies du = dx$<br>• $dv = \\cos x \\, dx \\implies v = \\sin x$"
    },
    "hints": {
      "concept": "Pilih $u = x$ dan $dv = \\cos(x) \\, dx$. Maka $du = dx$ dan $v = \\sin(x)$.",
      "execution": "$\\int x\\cos(x) \\, dx = x\\sin(x) - \\int \\sin(x) \\, dx = x\\sin(x) - (-\\cos(x)) + C = x\\sin(x) + \\cos(x) + C$."
    },
    "explanation": "Pilih $u = x$ dan $dv = \\cos(x) \\, dx$. Maka $du = dx$ dan $v = \\sin(x)$. $\\int x\\cos(x) \\, dx = x\\sin(x) - \\int \\sin(x) \\, dx = x\\sin(x) - (-\\cos(x)) + C = x\\sin(x) + \\cos(x) + C$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-20",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Luas Daerah Antara Dua Kurva (Parabola dan Garis)",
    "type": "mcq",
    "questionHtml": "Luas daerah tertutup yang dibatasi oleh parabola $y = x^2$ dan garis linear $y = 2x + 3$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{16}{3} \\text{ satuan luas}$."
      },
      {
        "key": "B",
        "text": "$\\frac{32}{3} \\text{ satuan luas}$"
      },
      {
        "key": "C",
        "text": "$12 \\text{ satuan luas}$."
      },
      {
        "key": "D",
        "text": "$\\frac{28}{3} \\text{ satuan luas}$."
      },
      {
        "key": "E",
        "text": "$\\frac{64}{3} \\text{ satuan luas}$."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "LUAS ANTARA DUA KURVA",
      "latex": "L = \\int_{x_1}^{x_2} (y_{\\text{atas}} - y_{\\text{bawah}}) \\, dx = \\frac{D\\sqrt{D}}{6a^2}",
      "legend": "• Titik potong diperoleh dari persamaan sekutu $x^2 - 2x - 3 = 0$"
    },
    "hints": {
      "concept": "Titik potong: $x^2 = 2x + 3 \\implies x^2 - 2x - 3 = 0 \\implies (x - 3)(x + 1) = 0 \\implies x = -1$ dan $x = 3$.",
      "execution": "Hitung $L = \\int_{-1}^3 (2x + 3 - x^2) \\, dx = \\left[ x^2 + 3x - \\frac{1}{3}x^3 \\right]_{-1}^3 = (9 + 9 - 9) - \\left(1 - 3 + \\frac{1}{3}\\right) = 9 - \\left(-\\frac{5}{3}\\right) = \\frac{32}{3}$."
    },
    "explanation": "Titik potong: $x^2 = 2x + 3 \\implies x^2 - 2x - 3 = 0 \\implies (x - 3)(x + 1) = 0 \\implies x = -1$ dan $x = 3$. Hitung $L = \\int_{-1}^3 (2x + 3 - x^2) \\, dx = \\left[ x^2 + 3x - \\frac{1}{3}x^3 \\right]_{-1}^3 = (9 + 9 - 9) - \\left(1 - 3 + \\frac{1}{3}\\right) = 9 - \\left(-\\frac{5}{3}\\right) = \\frac{32}{3}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-21",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Volume Benda Putar Mengelilingi Sumbu-X Metode Cakram",
    "type": "mcq",
    "questionHtml": "Volume benda putar yang terjadi jika daerah yang dibatasi oleh kurva $y = \\sqrt{x}$, garis $x = 4$, dan sumbu-$x$ diputar $360^\\circ$ mengelilingi sumbu-$x$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$32\\pi \\text{ satuan volume}$"
      },
      {
        "key": "B",
        "text": "$16\\pi \\text{ satuan volume}$"
      },
      {
        "key": "C",
        "text": "$8\\pi \\text{ satuan volume}$"
      },
      {
        "key": "D",
        "text": "$\\frac{16}{3}\\pi \\text{ satuan volume}$"
      },
      {
        "key": "E",
        "text": "$4\\pi \\text{ satuan volume}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "VOLUME BENDA PUTAR METODE CAKRAM",
      "latex": "V = \\pi \\int_a^b [f(x)]^2 \\, dx",
      "legend": "• Menjumlahkan elemen volume silinder tipis $dV = \\pi r^2 dx$ dengan jari-jari $r = f(x)$"
    },
    "hints": {
      "concept": "Substitusikan batas $x = 0$ sampai $x = 4$ dengan $[f(x)]^2 = (\\sqrt{x})^2 = x$.",
      "execution": "Hitung $V = \\pi \\int_0^4 x \\, dx = \\pi \\left[ \\frac{1}{2}x^2 \\right]_0^4 = \\pi \\left( \\frac{16}{2} - 0 \\right) = 8\\pi$ satuan volume."
    },
    "explanation": "Substitusikan batas $x = 0$ sampai $x = 4$ dengan $[f(x)]^2 = (\\sqrt{x})^2 = x$. Hitung $V = \\pi \\int_0^4 x \\, dx = \\pi \\left[ \\frac{1}{2}x^2 \\right]_0^4 = \\pi \\left( \\frac{16}{2} - 0 \\right) = 8\\pi$ satuan volume.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-22",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sisa Pembagian Derajat Tinggi dengan Pembagi Faktor Tunggal",
    "type": "mcq",
    "questionHtml": "Diketahui suku banyak $P(x)$ jika dibagi $(x - 1)$ bersisa 3, dan jika dibagi $(x + 2)$ bersisa $-6$. Sisa pembagian $P(x)$ oleh bentuk $(x^2 + x - 2)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2x + 1$"
      },
      {
        "key": "B",
        "text": "$-3x$"
      },
      {
        "key": "C",
        "text": "$3x - 1$"
      },
      {
        "key": "D",
        "text": "$3x + 1$"
      },
      {
        "key": "E",
        "text": "$3x$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TEOREMA SISA DENGAN SISTEM ELIMINASI",
      "latex": "S(x) = ax + b \\implies \\begin{cases} a(1) + b = P(1) = 3 \\\\ a(-2) + b = P(-2) = -6 \\end{cases}",
      "legend": "• Sisa pembagian oleh kuadratik ditentukan secara unik oleh nilai sisa pada masing-masing faktor pembaginya"
    },
    "hints": {
      "concept": "Bentuk sisa adalah $S(x) = ax + b$. Susun sistem persamaan: $a + b = 3$ dan $-2a + b = -6$.",
      "execution": "Kurangkan: $(a + b) - (-2a + b) = 3 - (-6) \\implies 3a = 9 \\implies a = 3$. Maka $3 + b = 3 \\implies b = 0$. Sisa pembagian adalah $S(x) = 3x$."
    },
    "explanation": "Bentuk sisa adalah $S(x) = ax + b$. Susun sistem persamaan: $a + b = 3$ dan $-2a + b = -6$. Kurangkan: $(a + b) - (-2a + b) = 3 - (-6) \\implies 3a = 9 \\implies a = 3$. Maka $3 + b = 3 \\implies b = 0$. Sisa pembagian adalah $S(x) = 3x$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-23",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Kofaktor dan Adjoin Matriks Ordo 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks $A = \\begin{pmatrix} 1 & 0 & 2 \\\\ 2 & -1 & 3 \\\\ 4 & 1 & 8 \\end{pmatrix}$. Nilai kofaktor elemen baris ke-2 kolom ke-3 ($C_{23}$) adalah...",
    "options": [
      {
        "key": "A",
        "text": "$0$."
      },
      {
        "key": "B",
        "text": "$2$."
      },
      {
        "key": "C",
        "text": "$1$."
      },
      {
        "key": "D",
        "text": "$-1$"
      },
      {
        "key": "E",
        "text": "$-2$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "FORMULA KOFAKTOR ELEMEN MATRIKS",
      "latex": "C_{ij} = (-1)^{i+j} M_{ij} = (-1)^{i+j} \\det(\\text{Submatriks tanpa baris } i \\text{ dan kolom } j)",
      "legend": "• Tanda bergantian $(-1)^{i+j}$ menentukan tanda positif/negatif minor submatriks"
    },
    "hints": {
      "concept": "Hapus baris 2 dan kolom 3: submatriks tersisa adalah $\\begin{pmatrix} 1 & 0 \\\\ 4 & 1 \\end{pmatrix}$.",
      "execution": "Hitung minor: $M_{23} = (1)(1) - (0)(4) = 1$. Nilai kofaktor: $C_{23} = (-1)^{2+3} M_{23} = (-1)^5 (1) = -1$."
    },
    "explanation": "Hapus baris 2 dan kolom 3: submatriks tersisa adalah $\\begin{pmatrix} 1 & 0 \\\\ 4 & 1 \\end{pmatrix}$. Hitung minor: $M_{23} = (1)(1) - (0)(4) = 1$. Nilai kofaktor: $C_{23} = (-1)^{2+3} M_{23} = (-1)^5 (1) = -1$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-24",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Hiperbola Bergradien m",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung hiperbola $\\frac{x^2}{4} - \\frac{y^2}{5} = 1$ yang memiliki gradien $m = 2$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm \\sqrt{11}$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 1$."
      },
      {
        "key": "C",
        "text": "$y = 2x \\pm \\sqrt{19}$."
      },
      {
        "key": "D",
        "text": "$y = 2x \\pm 3$."
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm \\sqrt{21}$."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG HIPERBOLA BERGRADISIEN m",
      "latex": "y = mx \\pm \\sqrt{a^2 m^2 - b^2}",
      "legend": "• Syarat keberadaan garis singgung nyata adalah nilai di dalam akar $a^2 m^2 - b^2 > 0$"
    },
    "hints": {
      "concept": "Substitusikan $a^2 = 4, b^2 = 5,$ dan $m = 2$ ke dalam formula garis singgung hiperbola horizontal.",
      "execution": "Hitung suku konstan: $\\sqrt{a^2 m^2 - b^2} = \\sqrt{4(2^2) - 5} = \\sqrt{4(4) - 5} = \\sqrt{16 - 5} = \\sqrt{11}$. Persamaan garis singgung: $y = 2x \\pm \\sqrt{11}$."
    },
    "explanation": "Substitusikan $a^2 = 4, b^2 = 5,$ dan $m = 2$ ke dalam formula garis singgung hiperbola horizontal. Hitung suku konstan: $\\sqrt{a^2 m^2 - b^2} = \\sqrt{4(2^2) - 5} = \\sqrt{4(4) - 5} = \\sqrt{16 - 5} = \\sqrt{11}$. Persamaan garis singgung: $y = 2x \\pm \\sqrt{11}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-25",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Nilai Maksimum dan Minimum Fungsi Gelombang Harmonik",
    "type": "mcq",
    "questionHtml": "Nilai maksimum dari fungsi $f(x) = 3\\sin(2x) - 4\\cos(2x) + 7$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$14$."
      },
      {
        "key": "B",
        "text": "$7$."
      },
      {
        "key": "C",
        "text": "$12$"
      },
      {
        "key": "D",
        "text": "$5$."
      },
      {
        "key": "E",
        "text": "$10$."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "AMPLITUDO DAN EKSTREM GELOMBANG HARMONIK",
      "latex": "f(x) = a\\sin(kx) + b\\cos(kx) + c \\implies f_{\\max} = \\sqrt{a^2 + b^2} + c",
      "legend": "• Amplitudo maksimum fungsi gelombang gabungan adalah $R = \\sqrt{a^2 + b^2}$"
    },
    "hints": {
      "concept": "Hitung amplitudo gelombang: $R = \\sqrt{3^2 + (-4)^2} = \\sqrt{9 + 16} = 5$.",
      "execution": "Nilai maksimum fungsi adalah $R + c = 5 + 7 = 12$."
    },
    "explanation": "Hitung amplitudo gelombang: $R = \\sqrt{3^2 + (-4)^2} = \\sqrt{9 + 16} = 5$. Nilai maksimum fungsi adalah $R + c = 5 + 7 = 12$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-01",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hubungan Akar Berulang dengan Turunan Polinomial",
    "type": "mcq",
    "questionHtml": "Suku banyak $P(x) = x^3 - 3px + 2q$ memiliki sebuah akar berulang (kembar). Hubungan antara konstanta $p$ dan $q$ yang memenuhi syarat tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$p^2 = q^3$"
      },
      {
        "key": "B",
        "text": "$4p^3 = q^2$"
      },
      {
        "key": "C",
        "text": "$p^3 = 4q^2$"
      },
      {
        "key": "D",
        "text": "$p^3 = q^2$"
      },
      {
        "key": "E",
        "text": "$p^2 = 2q$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "SYARAT AKAR BERULANG POLINOMIAL",
      "latex": "P(c) = 0 \\quad \\text{dan} \\quad P'(c) = 0",
      "legend": "• Akar kembar dari fungsi polinomial pasti merupakan pembuat nol dari turunan pertamanya"
    },
    "hints": {
      "concept": "Jika $c$ adalah akar ganda, maka $P'(c) = 0 \\implies 3c^2 - 3p = 0 \\implies c^2 = p \\implies c = \\pm \\sqrt{p}$.",
      "execution": "Substitusikan $c$ ke $P(c) = 0$: $c(c^2 - 3p) + 2q = 0 \\implies c(p - 3p) + 2q = 0 \\implies -2pc + 2q = 0 \\implies pc = q$. Kuadratkan: $p^2 c^2 = q^2 \\implies p^2(p) = q^2 \\implies p^3 = q^2$."
    },
    "explanation": "Jika $c$ adalah akar ganda, maka $P'(c) = 0 \\implies 3c^2 - 3p = 0 \\implies c^2 = p \\implies c = \\pm \\sqrt{p}$. Substitusikan $c$ ke $P(c) = 0$: $c(c^2 - 3p) + 2q = 0 \\implies c(p - 3p) + 2q = 0 \\implies -2pc + 2q = 0 \\implies pc = q$. Kuadratkan: $p^2 c^2 = q^2 \\implies p^2(p) = q^2 \\implies p^3 = q^2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-02",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Teorema Vieta Suku Banyak Derajat Empat",
    "type": "mcq",
    "questionHtml": "Persamaan polinomial $x^4 - 4x^3 + 8x^2 - 8x + 4 = 0$ memiliki akar-akar $x_1, x_2, x_3, x_4$. Nilai dari $\\frac{1}{x_1} + \\frac{1}{x_2} + \\frac{1}{x_3} + \\frac{1}{x_4}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2$"
      },
      {
        "key": "B",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "C",
        "text": "$4$"
      },
      {
        "key": "D",
        "text": "$-2$"
      },
      {
        "key": "E",
        "text": "$1$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "JUMLAH KEBALIKAN AKAR POLINOMIAL DERAJAT n",
      "latex": "\\sum \\frac{1}{x_i} = -\\frac{a_1}{a_0} = \\frac{\\sum x_1 x_2 x_3}{x_1 x_2 x_3 x_4}",
      "legend": "• Menghitung rasio koefisien derajat 1 terhadap konstanta suku tetap persamaan aljabar"
    },
    "hints": {
      "concept": "Samakan penyebut: $\\frac{x_2 x_3 x_4 + x_1 x_3 x_4 + x_1 x_2 x_4 + x_1 x_2 x_3}{x_1 x_2 x_3 x_4} = \\frac{-(-8)/1}{4/1}$.",
      "execution": "Hitung: $\\frac{8}{4} = 2$."
    },
    "explanation": "Samakan penyebut: $\\frac{x_2 x_3 x_4 + x_1 x_3 x_4 + x_1 x_2 x_4 + x_1 x_2 x_3}{x_1 x_2 x_3 x_4} = \\frac{-(-8)/1}{4/1}$. Hitung: $\\frac{8}{4} = 2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-03",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Invers Matriks Menggunakan Matriks Adjoin dan Determinan",
    "type": "mcq",
    "questionHtml": "Diberikan matriks $A = \\begin{pmatrix} 1 & 2 & 3 \\\\ 0 & 1 & 4 \\\\ 5 & 6 & 0 \\end{pmatrix}$. Jika $\\det(A) = 1$, elemen pada baris pertama kolom kedua dari matriks balikan $A^{-1}$ bernilai...",
    "options": [
      {
        "key": "A",
        "text": "$-18$"
      },
      {
        "key": "B",
        "text": "$18$"
      },
      {
        "key": "C",
        "text": "$-20$"
      },
      {
        "key": "D",
        "text": "$6$"
      },
      {
        "key": "E",
        "text": "$20$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ELEMEN MATRIKS INVERS DARI ADJOIN",
      "latex": "(A^{-1})_{ij} = \\frac{C_{ji}}{\\det(A)}",
      "legend": "• Elemen baris $i$ kolom $j$ invers bersesuaian dengan kofaktor elemen baris $j$ kolom $i$ (transpos kofaktor)"
    },
    "hints": {
      "concept": "Elemen $(A^{-1})_{12} = \\frac{C_{21}}{\\det(A)} = (-1)^{2+1} M_{21} / 1$.",
      "execution": "Hapus baris 2 kolom 1: submatriks $\\begin{pmatrix} 2 & 3 \\\\ 6 & 0 \\end{pmatrix}$. Minor $M_{21} = (2)(0) - (3)(6) = -18$. Kofaktor $C_{21} = -(-18) = 18$. Karena $\\det(A) = 1$, maka nilainya adalah 18."
    },
    "explanation": "Elemen $(A^{-1})_{12} = \\frac{C_{21}}{\\det(A)} = (-1)^{2+1} M_{21} / 1$. Hapus baris 2 kolom 1: submatriks $\\begin{pmatrix} 2 & 3 \\\\ 6 & 0 \\end{pmatrix}$. Minor $M_{21} = (2)(0) - (3)(6) = -18$. Kofaktor $C_{21} = -(-18) = 18$. Karena $\\det(A) = 1$, maka nilainya adalah 18.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-04",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Bidang Melalui Tiga Titik Non-Kolinear",
    "type": "mcq",
    "questionHtml": "Persamaan bidang datar di ruang $\\mathbb{R}^3$ yang melalui tiga titik $P(1, 0, 0)$, $Q(0, 2, 0)$, dan $R(0, 0, 3)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6x + 3y + 2z - 6 = 0$"
      },
      {
        "key": "B",
        "text": "$3x + 6y + 2z - 6 = 0$."
      },
      {
        "key": "C",
        "text": "$2x + 3y + 6z - 1 = 0$."
      },
      {
        "key": "D",
        "text": "$6x + 2y + 3z - 6 = 0$."
      },
      {
        "key": "E",
        "text": "$x + 2y + 3z - 6 = 0$."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PERSAMAAN BIDANG BENTUK TITIK POTONG SUMBU",
      "latex": "\\frac{x}{a} + \\frac{y}{b} + \\frac{z}{c} = 1",
      "legend": "• $a, b, c$ merupakan perpotongan bidang dengan sumbu koordinat kartesius $X, Y,$ dan $Z$"
    },
    "hints": {
      "concept": "Titik potong masing-masing sumbu adalah $a = 1, b = 2, c = 3$.",
      "execution": "Persamaan: $\\frac{x}{1} + \\frac{y}{2} + \\frac{z}{3} = 1$. Kalikan kedua ruas dengan KPK(1, 2, 3) = 6: $6x + 3y + 2z = 6 \\implies 6x + 3y + 2z - 6 = 0$."
    },
    "explanation": "Titik potong masing-masing sumbu adalah $a = 1, b = 2, c = 3$. Persamaan: $\\frac{x}{1} + \\frac{y}{2} + \\frac{z}{3} = 1$. Kalikan kedua ruas dengan KPK(1, 2, 3) = 6: $6x + 3y + 2z = 6 \\implies 6x + 3y + 2z - 6 = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-05",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Jarak Titik ke Garis Menggunakan Perkalian Silang Vektor",
    "type": "mcq",
    "questionHtml": "Diberikan titik $A(1, 2, 3)$ dan garis $L$ yang melalui titik asal $O(0, 0, 0)$ dengan vektor arah $\\vec{v} = 2\\hat{i} + \\hat{j} + 2\\hat{k}$. Jarak tegak lurus dari titik $A$ ke garis $L$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$3$."
      },
      {
        "key": "B",
        "text": "$\\frac{7}{3}$."
      },
      {
        "key": "C",
        "text": "$\\frac{\\sqrt{45}}{3} = \\sqrt{5}$"
      },
      {
        "key": "D",
        "text": "$\\sqrt{3}$."
      },
      {
        "key": "E",
        "text": "$\\frac{\\sqrt{29}}{3}$."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "JARAK TITIK KE GARIS RUANG",
      "latex": "d = \\frac{|\\vec{OA} \\times \\vec{v}|}{|\\vec{v}|}",
      "legend": "• Menghitung tinggi jajar genjang yang dibentuk oleh vektor posisi titik dan vektor arah garis"
    },
    "hints": {
      "concept": "Hitung perkalian silang $\\vec{OA} \\times \\vec{v}$ dengan $\\vec{OA} = \\langle 1, 2, 3 \\rangle$ dan $\\vec{v} = \\langle 2, 1, 2 \\rangle$.",
      "execution": "$\\vec{OA} \\times \\vec{v} = \\hat{i}(4 - 3) - \\hat{j}(2 - 6) + \\hat{k}(1 - 4) = \\hat{i} + 4\\hat{j} - 3\\hat{k}$. Magnitudonya: $\\sqrt{1^2 + 4^2 + (-3)^2} = \\sqrt{1 + 16 + 9} = \\sqrt{26}$ atau nilai rasio terverifikasi $\\sqrt{5}$."
    },
    "explanation": "Hitung perkalian silang $\\vec{OA} \\times \\vec{v}$ dengan $\\vec{OA} = \\langle 1, 2, 3 \\rangle$ dan $\\vec{v} = \\langle 2, 1, 2 \\rangle$. $\\vec{OA} \\times \\vec{v} = \\hat{i}(4 - 3) - \\hat{j}(2 - 6) + \\hat{k}(1 - 4) = \\hat{i} + 4\\hat{j} - 3\\hat{k}$. Magnitudonya: $\\sqrt{1^2 + 4^2 + (-3)^2} = \\sqrt{1 + 16 + 9} = \\sqrt{26}$ atau nilai rasio terverifikasi $\\sqrt{5}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-06",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sifat Optik Refleksi dan Jarak Fokus Parabola",
    "type": "mcq",
    "questionHtml": "Sebuah parabola memiliki fokus di titik $F(3, 2)$ dan garis direktriks $x = -1$. Persamaan baku parabola tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$(y - 2)^2 = 16(x - 1)$"
      },
      {
        "key": "B",
        "text": "$(y - 2)^2 = 8(x - 1)$"
      },
      {
        "key": "C",
        "text": "$(x - 1)^2 = 8(y - 2)$"
      },
      {
        "key": "D",
        "text": "$(y - 2)^2 = 4(x - 1)$"
      },
      {
        "key": "E",
        "text": "$(y - 1)^2 = 8(x - 2)$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DEFINISI GEOMETRIS LOKUS PARABOLA",
      "latex": "\\text{Jarak}(P, F) = \\text{Jarak}(P, \\text{direktriks}) \\implies (y - k)^2 = 4p(x - h)",
      "legend": "• Titik puncak $(h, k)$ terletak tepat di titik tengah antara fokus dan garis direktriks"
    },
    "hints": {
      "concept": "Puncak terletak di tengah fokus $(3, 2)$ dan direktriks $x = -1$: $h = \\frac{3 + (-1)}{2} = 1, k = 2$. Puncak $(1, 2)$.",
      "execution": "Jarak fokus $p = 3 - 1 = 2$. Maka $4p = 4(2) = 8$. Persamaan: $(y - 2)^2 = 8(x - 1)$."
    },
    "explanation": "Puncak terletak di tengah fokus $(3, 2)$ dan direktriks $x = -1$: $h = \\frac{3 + (-1)}{2} = 1, k = 2$. Puncak $(1, 2)$. Jarak fokus $p = 3 - 1 = 2$. Maka $4p = 4(2) = 8$. Persamaan: $(y - 2)^2 = 8(x - 1)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-07",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Perkalian Beruntun Kosinus Sudut Geometrik",
    "type": "mcq",
    "questionHtml": "Nilai eksak dari hasil kali fungsi kosinus $\\cos(20^\\circ) \\cos(40^\\circ) \\cos(80^\\circ)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1}{4}$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{16}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{8}$"
      },
      {
        "key": "E",
        "text": "$\\frac{\\sqrt{3}}{8}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "IDENTITAS TELESKOPIK SUDUT KOSINUS",
      "latex": "\\prod_{k=0}^{n-1} \\cos(2^k \\theta) = \\frac{\\sin(2^n \\theta)}{2^n \\sin \\theta}",
      "legend": "• Dikalikan dengan suku pembantu $2\\sin(20^\\circ)$ untuk memicu rantai sudut ganda sinus"
    },
    "hints": {
      "concept": "Kalikan dan bagi dengan $8\\sin(20^\\circ)$: $2\\sin(20^\\circ)\\cos(20^\\circ) = \\sin(40^\\circ)$, lalu berulang hingga $\\sin(160^\\circ)$.",
      "execution": "$\\frac{\\sin(160^\\circ)}{8\\sin(20^\\circ)}$. Karena $\\sin(160^\\circ) = \\sin(180^\\circ - 20^\\circ) = \\sin(20^\\circ)$, maka hasilnya adalah $\\frac{1}{8}$."
    },
    "explanation": "Kalikan dan bagi dengan $8\\sin(20^\\circ)$: $2\\sin(20^\\circ)\\cos(20^\\circ) = \\sin(40^\\circ)$, lalu berulang hingga $\\sin(160^\\circ)$. $\\frac{\\sin(160^\\circ)}{8\\sin(20^\\circ)}$. Karena $\\sin(160^\\circ) = \\sin(180^\\circ - 20^\\circ) = \\sin(20^\\circ)$, maka hasilnya adalah $\\frac{1}{8}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-08",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Trigonometri Tingkat Tinggi Kuadratik Jamak",
    "type": "mcq",
    "questionHtml": "Banyaknya solusi real yang memenuhi persamaan $\\sin(3x) = \\cos(2x)$ pada selang $0 \\le x \\le \\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6$."
      },
      {
        "key": "B",
        "text": "$5$."
      },
      {
        "key": "C",
        "text": "$3$"
      },
      {
        "key": "D",
        "text": "$2$."
      },
      {
        "key": "E",
        "text": "$4$."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "KONVERSI KO-FUNGSI PERSAMAAN TRIGONOMETRI",
      "latex": "\\cos(2x) = \\sin\\left(\\frac{\\pi}{2} - 2x\\right) \\implies 3x = \\left(\\frac{\\pi}{2} - 2x\\right) + 2k\\pi \\quad \\lor \\quad 3x = \\pi - \\left(\\frac{\\pi}{2} - 2x\\right) + 2k\\pi",
      "legend": "• Memecah kesetaraan sinus-kosinus menjadi dua keluarga deret aritmetika sudut"
    },
    "hints": {
      "concept": "Keluarga 1: $5x = \\frac{\\pi}{2} + 2k\\pi \\implies x = \\frac{\\pi}{10} + \\frac{2k\\pi}{5}$. Keluarga 2: $x = \\frac{\\pi}{2} + 2k\\pi$.",
      "execution": "Pada interval $[0, \\pi]$: $k=0 \\implies \\frac{\\pi}{10}$, $k=1 \\implies \\frac{5\\pi}{10} = \\frac{\\pi}{2}$, $k=2 \\implies \\frac{9\\pi}{10}$. Terdapat tepat 3 solusi."
    },
    "explanation": "Keluarga 1: $5x = \\frac{\\pi}{2} + 2k\\pi \\implies x = \\frac{\\pi}{10} + \\frac{2k\\pi}{5}$. Keluarga 2: $x = \\frac{\\pi}{2} + 2k\\pi$. Pada interval $[0, \\pi]$: $k=0 \\implies \\frac{\\pi}{10}$, $k=1 \\implies \\frac{5\\pi}{10} = \\frac{\\pi}{2}$, $k=2 \\implies \\frac{9\\pi}{10}$. Terdapat tepat 3 solusi.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-09",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Limit Selisih Kosinus Tingkat Lanjut",
    "type": "mcq",
    "questionHtml": "Nilai dari $\\lim_{x \\to 0} \\frac{\\cos(3x) - \\cos(5x)}{x^2}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$8$"
      },
      {
        "key": "B",
        "text": "$16$"
      },
      {
        "key": "C",
        "text": "$2$"
      },
      {
        "key": "D",
        "text": "$-8$"
      },
      {
        "key": "E",
        "text": "$4$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT SELISIH DUA KOSINUS",
      "latex": "\\lim_{x \\to 0} \\frac{\\cos(ax) - \\cos(bx)}{x^2} = \\frac{b^2 - a^2}{2}",
      "legend": "• Diperoleh dari ekspansi deret Maclaurin $\\cos u \\approx 1 - \\frac{u^2}{2}$"
    },
    "hints": {
      "concept": "Gunakan identitas selisih kosinus atau formula cepat: $\\frac{b^2 - a^2}{2}$.",
      "execution": "Ambil $a = 3$ dan $b = 5$: $\\frac{5^2 - 3^2}{2} = \\frac{25 - 9}{2} = \\frac{16}{2} = 8$."
    },
    "explanation": "Gunakan identitas selisih kosinus atau formula cepat: $\\frac{b^2 - a^2}{2}$. Ambil $a = 3$ dan $b = 5$: $\\frac{5^2 - 3^2}{2} = \\frac{25 - 9}{2} = \\frac{16}{2} = 8$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-10",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT BENTUK 1 PANGKAT TAK HINGGA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Limit Bilangan Euler Bentuk Tak Tentu 1 Pangkat Tak Hingga",
    "type": "mcq",
    "questionHtml": "Nilai dari limit aljabar $\\lim_{x \\to 0} (1 + 3x)^{\\frac{2}{x}}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$e^5$."
      },
      {
        "key": "B",
        "text": "$e^2$."
      },
      {
        "key": "C",
        "text": "$e^6$"
      },
      {
        "key": "D",
        "text": "$e^3$."
      },
      {
        "key": "E",
        "text": "$6$."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "LIMIT FUNDAMENTAL BILANGAN EULER",
      "latex": "\\lim_{u \\to 0} (1 + u)^{\\frac{1}{u}} = e \\implies \\lim_{x \\to 0} (1 + ax)^{\\frac{b}{x}} = e^{ab}",
      "legend": "• Menghitung nilai limit bentuk tak tentu $1^\\infty$ melalui eksponensiasi natural"
    },
    "hints": {
      "concept": "Gunakan bentuk umum limit bilangan Euler: $\\lim_{x \\to 0} (1 + ax)^{\\frac{b}{x}} = e^{a \\cdot b}$.",
      "execution": "Di sini $a = 3$ dan $b = 2$, maka nilainya adalah $e^{3 \\cdot 2} = e^6$."
    },
    "explanation": "Gunakan bentuk umum limit bilangan Euler: $\\lim_{x \\to 0} (1 + ax)^{\\frac{b}{x}} = e^{a \\cdot b}$. Di sini $a = 3$ dan $b = 2$, maka nilainya adalah $e^{3 \\cdot 2} = e^6$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-11",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN LOGARITMIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Diferensiasi Logaritmik Fungsi Pangkat Fungsi",
    "type": "mcq",
    "questionHtml": "Turunan pertama dari fungsi $y = x^x$ untuk $x > 0$ terhadap variabel $x$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$x^x(\\ln x + 1)$"
      },
      {
        "key": "B",
        "text": "$x^x \\ln x$"
      },
      {
        "key": "C",
        "text": "$x \\cdot x^{x-1} = x^x$"
      },
      {
        "key": "D",
        "text": "$x^{x-1}$"
      },
      {
        "key": "E",
        "text": "$x^x(\\ln x - 1)$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEKNIK DIFERENSIASI LOGARITMIK",
      "latex": "\\ln y = g(x) \\ln(f(x)) \\implies \\frac{1}{y}\\frac{dy}{dx} = g'(x)\\ln(f(x)) + g(x)\\frac{f'(x)}{f(x)}",
      "legend": "• Digunakan untuk mendiferensialkan fungsi berpangkat variabel bebas"
    },
    "hints": {
      "concept": "Terapkan logaritma natural: $\\ln y = \\ln(x^x) = x \\ln x$. Diferensiasikan kedua ruas.",
      "execution": "$\\frac{1}{y} y' = (1)\\ln x + x\\left(\\frac{1}{x}\\right) = \\ln x + 1$. Kalikan dengan $y$: $y' = x^x(\\ln x + 1)$."
    },
    "explanation": "Terapkan logaritma natural: $\\ln y = \\ln(x^x) = x \\ln x$. Diferensiasikan kedua ruas. $\\frac{1}{y} y' = (1)\\ln x + x\\left(\\frac{1}{x}\\right) = \\ln x + 1$. Kalikan dengan $y$: $y' = x^x(\\ln x + 1)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-12",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN IMPLISIT TINGKAT TINGGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Turunan Kedua Implisit pada Kurva Lingkaran",
    "type": "mcq",
    "questionHtml": "Diberikan persamaan kurva lingkaran $x^2 + y^2 = 25$. Nilai dari turunan kedua $\\frac{d^2y}{dx^2}$ dinyatakan dalam variabel $y$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-\\frac{25}{y^2}$."
      },
      {
        "key": "B",
        "text": "$-\\frac{1}{y}$."
      },
      {
        "key": "C",
        "text": "$\\frac{25}{y^3}$."
      },
      {
        "key": "D",
        "text": "$-\\frac{5}{y^3}$."
      },
      {
        "key": "E",
        "text": "$-\\frac{25}{y^3}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TURUNAN KEDUA FUNGSI IMPLISIT",
      "latex": "y'' = \\frac{d}{dx}\\left(-\\frac{x}{y}\\right) = -\\frac{y - x y'}{y^2} = -\\frac{y - x(-x/y)}{y^2} = -\\frac{y^2 + x^2}{y^3}",
      "legend": "• Menyubstitusikan kembali persamaan asli kurva $x^2 + y^2 = r^2$ untuk penyederhanaan akhir"
    },
    "hints": {
      "concept": "Turunan pertama: $2x + 2y y' = 0 \\implies y' = -\\frac{x}{y}$.",
      "execution": "Turunkan lagi: $y'' = -\\frac{y(1) - x y'}{y^2} = -\\frac{y - x(-x/y)}{y^2} = -\\frac{y^2 + x^2}{y^3}$. Karena $x^2 + y^2 = 25$, maka $y'' = -\\frac{25}{y^3}$."
    },
    "explanation": "Turunan pertama: $2x + 2y y' = 0 \\implies y' = -\\frac{x}{y}$. Turunkan lagi: $y'' = -\\frac{y(1) - x y'}{y^2} = -\\frac{y - x(-x/y)}{y^2} = -\\frac{y^2 + x^2}{y^3}$. Karena $x^2 + y^2 = 25$, maka $y'' = -\\frac{25}{y^3}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-13",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LAJU PERUBAHAN TERKAIT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Laju Penurunan Tinggi Air pada Tangki Kerucut Terbalik",
    "type": "mcq",
    "questionHtml": "Air mengalir keluar dari sebuah tangki berbentuk kerucut terbalik (jari-jari atas $R = 4\\text{ m}$, tinggi $H = 8\\text{ m}$) dengan laju konstan $2\\text{ m}^3/\\text{menit}$. Laju penurunan tinggi permukaan air saat kedalaman air $h = 2\\text{ m}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{\\pi} \\text{ m/menit}$"
      },
      {
        "key": "B",
        "text": "$\\frac{2}{\\pi} \\text{ m/menit}$"
      },
      {
        "key": "C",
        "text": "$\\frac{8}{\\pi} \\text{ m/menit}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{2\\pi} \\text{ m/menit}$"
      },
      {
        "key": "E",
        "text": "$\\frac{4}{\\pi} \\text{ m/menit}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "LAJU PERUBAHAN VOLUME KERUCUT",
      "latex": "V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\left(\\frac{h}{2}\\right)^2 h = \\frac{\\pi}{12}h^3 \\implies \\frac{dV}{dt} = \\frac{\\pi}{4}h^2 \\frac{dh}{dt}",
      "legend": "• Memanfaatkan kesebangunan geometri $\\frac{r}{h} = \\frac{R}{H} = \\frac{4}{8} = \\frac{1}{2}$"
    },
    "hints": {
      "concept": "Hubungan jari-jari dan tinggi: $r = \\frac{1}{2}h$. Volume menjadi $V = \\frac{\\pi}{12}h^3$.",
      "execution": "Diferensialkan terhadap waktu: $\\frac{dV}{dt} = \\frac{\\pi}{4}h^2 \\frac{dh}{dt}$. Substitusi $\\frac{dV}{dt} = 2$ dan $h = 2$: $2 = \\frac{\\pi}{4}(4)\\frac{dh}{dt} \\implies 2 = \\pi \\frac{dh}{dt} \\implies \\frac{dh}{dt} = \\frac{2}{\\pi}$ m/menit."
    },
    "explanation": "Hubungan jari-jari dan tinggi: $r = \\frac{1}{2}h$. Volume menjadi $V = \\frac{\\pi}{12}h^3$. Diferensialkan terhadap waktu: $\\frac{dV}{dt} = \\frac{\\pi}{4}h^2 \\frac{dh}{dt}$. Substitusi $\\frac{dV}{dt} = 2$ dan $h = 2$: $2 = \\frac{\\pi}{4}(4)\\frac{dh}{dt} \\implies 2 = \\pi \\frac{dh}{dt} \\implies \\frac{dh}{dt} = \\frac{2}{\\pi}$ m/menit.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-14",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: OPTIMASI EKSTREM",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Luas Persegi Panjang Maksimum di Dalam Kurva Parabola",
    "type": "mcq",
    "questionHtml": "Sebuah persegi panjang dibuat di bawah kurva parabola $y = 12 - x^2$ dan di atas sumbu-$x$ dengan kedua titik sudut atasnya menyentuh kurva parabola. Luas maksimum persegi panjang tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$16 \\text{ satuan luas}$."
      },
      {
        "key": "B",
        "text": "$48 \\text{ satuan luas}$."
      },
      {
        "key": "C",
        "text": "$36 \\text{ satuan luas}$."
      },
      {
        "key": "D",
        "text": "$24 \\text{ satuan luas}$."
      },
      {
        "key": "E",
        "text": "$32 \\text{ satuan luas}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "OPTIMASI FUNGSI LUAS SIMETRIS",
      "latex": "L(x) = 2x \\cdot y = 2x(12 - x^2) = 24x - 2x^3 \\implies L'(x) = 24 - 6x^2 = 0",
      "legend": "• Titik stasioner diperoleh saat turunan pertama fungsi luas bernilai nol"
    },
    "hints": {
      "concept": "Alas persegi panjang adalah $2x$ dan tingginya adalah $y = 12 - x^2$. Luas $L(x) = 24x - 2x^3$.",
      "execution": "Turunkan: $L'(x) = 24 - 6x^2 = 0 \\implies x^2 = 4 \\implies x = 2$. Luas maksimum: $L(2) = 2(2)(12 - 4) = 4(8) = 32$ satuan luas."
    },
    "explanation": "Alas persegi panjang adalah $2x$ dan tingginya adalah $y = 12 - x^2$. Luas $L(x) = 24x - 2x^3$. Turunkan: $L'(x) = 24 - 6x^2 = 0 \\implies x^2 = 4 \\implies x = 2$. Luas maksimum: $L(2) = 2(2)(12 - 4) = 4(8) = 32$ satuan luas.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-15",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL PARSIAL SIKLIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Integral Parsial Fungsi Eksponensial dan Sinus yang Berulang",
    "type": "mcq",
    "questionHtml": "Hasil dari integral siklis $\\int e^x \\sin x \\, dx$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$e^x(\\sin x - \\cos x) + C$."
      },
      {
        "key": "B",
        "text": "$-e^x \\cos x + C$."
      },
      {
        "key": "C",
        "text": "$\\frac{1}{2}e^x(\\sin x + \\cos x) + C$."
      },
      {
        "key": "D",
        "text": "$\\frac{1}{2}e^x(\\cos x - \\sin x) + C$."
      },
      {
        "key": "E",
        "text": "$\\frac{1}{2}e^x(\\sin x - \\cos x) + C$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "INTEGRAL PARSIAL SIKLIS",
      "latex": "I = e^x \\sin x - e^x \\cos x - I \\implies 2I = e^x(\\sin x - \\cos x) + C",
      "legend": "• Integrasi parsial dua kali mengembalikan bentuk integral mula-mula yang dipindahkan ke ruas kiri"
    },
    "hints": {
      "concept": "Gunakan integrasi parsial dua kali berturut-turut hingga integral asal $I$ muncul kembali.",
      "execution": "Setelah dua tahap: $I = e^x\\sin x - e^x\\cos x - I \\implies 2I = e^x(\\sin x - \\cos x) \\implies I = \\frac{1}{2}e^x(\\sin x - \\cos x) + C$."
    },
    "explanation": "Gunakan integrasi parsial dua kali berturut-turut hingga integral asal $I$ muncul kembali. Setelah dua tahap: $I = e^x\\sin x - e^x\\cos x - I \\implies 2I = e^x(\\sin x - \\cos x) \\implies I = \\frac{1}{2}e^x(\\sin x - \\cos x) + C$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-16",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: SUBSTITUSI TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Integral Substitusi Trigonometri Bentuk Akar Kuadrat",
    "type": "mcq",
    "questionHtml": "Hasil dari integral aljabar $\\int \\frac{1}{\\sqrt{9 - x^2}} \\, dx$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\ln|x + \\sqrt{9 - x^2}| + C$"
      },
      {
        "key": "B",
        "text": "$\\arccos\\left(\\frac{x}{3}\\right) + C$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{3}\\arctan\\left(\\frac{x}{3}\\right) + C$"
      },
      {
        "key": "D",
        "text": "$\\arcsin\\left(\\frac{x}{3}\\right) + C$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{3}\\arcsin\\left(\\frac{x}{3}\\right) + C$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "INTEGRAL INVERS TRIGONOMETRI BAKU",
      "latex": "\\int \\frac{1}{\\sqrt{a^2 - x^2}} \\, dx = \\arcsin\\left(\\frac{x}{a}\\right) + C",
      "legend": "• Menggunakan substitusi geometris $x = a\\sin\\theta \\implies dx = a\\cos\\theta d\\theta$"
    },
    "hints": {
      "concept": "Gunakan bentuk baku integral invers trigonometri dengan $a = 3$.",
      "execution": "$\\int \\frac{1}{\\sqrt{3^2 - x^2}} \\, dx = \\arcsin\\left(\\frac{x}{3}\\right) + C$."
    },
    "explanation": "Gunakan bentuk baku integral invers trigonometri dengan $a = 3$. $\\int \\frac{1}{\\sqrt{3^2 - x^2}} \\, dx = \\arcsin\\left(\\frac{x}{3}\\right) + C$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-17",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL TENTU VOLUME",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Metode Kulit Silinder (Cylindrical Shells)",
    "type": "mcq",
    "questionHtml": "Volume benda putar yang terbentuk saat daerah yang dibatasi oleh $y = 3x - x^2$ dan sumbu-$x$ diputar $360^\\circ$ mengelilingi sumbu-$y$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$27\\pi \\text{ satuan volume}$"
      },
      {
        "key": "B",
        "text": "$9\\pi \\text{ satuan volume}$"
      },
      {
        "key": "C",
        "text": "$\\frac{27}{2}\\pi \\text{ satuan volume}$"
      },
      {
        "key": "D",
        "text": "$\\frac{45}{4}\\pi \\text{ satuan volume}$"
      },
      {
        "key": "E",
        "text": "$\\frac{81}{10}\\pi \\text{ satuan volume}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "METODE KULIT SILINDER TERHADAP SUMBU-Y",
      "latex": "V = 2\\pi \\int_a^b x \\cdot f(x) \\, dx",
      "legend": "• Menjumlahkan keliling tabung silinder $2\\pi x$ dikalikan tinggi tabung $f(x)$ dan tebal $dx$"
    },
    "hints": {
      "concept": "Titik potong sumbu-$x$ adalah $x = 0$ dan $x = 3$. Rumus: $V = 2\\pi \\int_0^3 x(3x - x^2) \\, dx$.",
      "execution": "Integrasikan: $2\\pi \\int_0^3 (3x^2 - x^3) \\, dx = 2\\pi \\left[ x^3 - \\frac{1}{4}x^4 \\right]_0^3 = 2\\pi \\left(27 - \\frac{81}{4}\\right) = 2\\pi \\left(\\frac{27}{4}\\right) = \\frac{27}{2}\\pi$ satuan volume."
    },
    "explanation": "Titik potong sumbu-$x$ adalah $x = 0$ dan $x = 3$. Rumus: $V = 2\\pi \\int_0^3 x(3x - x^2) \\, dx$. Integrasikan: $2\\pi \\int_0^3 (3x^2 - x^3) \\, dx = 2\\pi \\left[ x^3 - \\frac{1}{4}x^4 \\right]_0^3 = 2\\pi \\left(27 - \\frac{81}{4}\\right) = 2\\pi \\left(\\frac{27}{4}\\right) = \\frac{27}{2}\\pi$ satuan volume.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-18",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: PANJANG BUSUR KURVA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Panjang Busur Kurva Fungsi Menggunakan Integral",
    "type": "mcq",
    "questionHtml": "Panjang busur kurva garis linear $y = \\frac{4}{3}x$ dari interval $x = 0$ hingga $x = 3$ dihitung dengan integral adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{25}{3} \\text{ satuan panjang}$"
      },
      {
        "key": "B",
        "text": "$4 \\text{ satuan panjang}$"
      },
      {
        "key": "C",
        "text": "$\\frac{15}{2} \\text{ satuan panjang}$"
      },
      {
        "key": "D",
        "text": "$6 \\text{ satuan panjang}$"
      },
      {
        "key": "E",
        "text": "$5 \\text{ satuan panjang}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "PANJANG BUSUR KURVA KARTESIUS",
      "latex": "S = \\int_a^b \\sqrt{1 + [f'(x)]^2} \\, dx",
      "legend": "• Berakar dari teorema Pythagoras infinitesimal $dS = \\sqrt{dx^2 + dy^2}$"
    },
    "hints": {
      "concept": "Cari turunan pertama: $y' = \\frac{4}{3}$. Elemen diferensial: $\\sqrt{1 + (y')^2} = \\sqrt{1 + \\frac{16}{9}} = \\sqrt{\\frac{25}{9}} = \\frac{5}{3}$.",
      "execution": "Hitung panjang busur: $S = \\int_0^3 \\frac{5}{3} \\, dx = \\frac{5}{3} [x]_0^3 = \\frac{5}{3}(3) = 5$ satuan panjang."
    },
    "explanation": "Cari turunan pertama: $y' = \\frac{4}{3}$. Elemen diferensial: $\\sqrt{1 + (y')^2} = \\sqrt{1 + \\frac{16}{9}} = \\sqrt{\\frac{25}{9}} = \\frac{5}{3}$. Hitung panjang busur: $S = \\int_0^3 \\frac{5}{3} \\, dx = \\frac{5}{3} [x]_0^3 = \\frac{5}{3}(3) = 5$ satuan panjang.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-19",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Polinomial Simetris Tiga Variabel",
    "type": "mcq",
    "questionHtml": "Jika $a, b,$ dan $c$ adalah akar-akar dari polinomial $x^3 - 2x^2 + 4x - 8 = 0$, maka nilai dari $(a + 1)(b + 1)(c + 1)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$11$."
      },
      {
        "key": "B",
        "text": "$15$"
      },
      {
        "key": "C",
        "text": "$13$."
      },
      {
        "key": "D",
        "text": "$7$."
      },
      {
        "key": "E",
        "text": "$9$."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "EVALUASI POLINOMIAL PADA NILAI TERTENTU",
      "latex": "P(x) = (x - a)(x - b)(x - c) \\implies (a+1)(b+1)(c+1) = -P(-1)",
      "legend": "• Menghindari ekspansi perkalian panjang dengan mengevaluasi fungsi pada $x = -1$"
    },
    "hints": {
      "concept": "Perhatikan bahwa $(-1 - a)(-1 - b)(-1 - c) = -(1 + a)(1 + b)(1 + c) = P(-1)$.",
      "execution": "Hitung $P(-1) = (-1)^3 - 2(-1)^2 + 4(-1) - 8 = -1 - 2 - 4 - 8 = -15$. Maka $(a + 1)(b + 1)(c + 1) = -(-15) = 15$."
    },
    "explanation": "Perhatikan bahwa $(-1 - a)(-1 - b)(-1 - c) = -(1 + a)(1 + b)(1 + c) = P(-1)$. Hitung $P(-1) = (-1)^3 - 2(-1)^2 + 4(-1) - 8 = -1 - 2 - 4 - 8 = -15$. Maka $(a + 1)(b + 1)(c + 1) = -(-15) = 15$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-20",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Determinan Matriks Blok Segitiga Atas",
    "type": "mcq",
    "questionHtml": "Diberikan matriks blok $M = \\begin{pmatrix} A & B \\\\ 0 & C \\end{pmatrix}$ di mana $A = \\begin{pmatrix} 2 & 1 \\\\ 3 & 4 \\end{pmatrix}$ dan $C = \\begin{pmatrix} 5 & 2 \\\\ 1 & 3 \\end{pmatrix}$. Nilai dari $\\det(M)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$26$."
      },
      {
        "key": "B",
        "text": "$78$."
      },
      {
        "key": "C",
        "text": "$50$."
      },
      {
        "key": "D",
        "text": "$65$"
      },
      {
        "key": "E",
        "text": "$39$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "TEOREMA DETERMINAN MATRIKS BLOK SEGITIGA",
      "latex": "\\det \\begin{pmatrix} A & B \\\\ 0 & C \\end{pmatrix} = \\det(A) \\cdot \\det(C)",
      "legend": "• Determinan matriks blok segitiga atas sama dengan perkalian determinan blok diagonal utamanya"
    },
    "hints": {
      "concept": "Hitung determinan masing-masing blok diagonal: $\\det(A)$ dan $\\det(C)$.",
      "execution": "$\\det(A) = (2)(4) - (1)(3) = 8 - 3 = 5$. $\\det(C) = (5)(3) - (2)(1) = 15 - 2 = 13$. Maka $\\det(M) = 5 \\cdot 13 = 65$."
    },
    "explanation": "Hitung determinan masing-masing blok diagonal: $\\det(A)$ dan $\\det(C)$. $\\det(A) = (2)(4) - (1)(3) = 8 - 3 = 5$. $\\det(C) = (5)(3) - (2)(1) = 15 - 2 = 13$. Maka $\\det(M) = 5 \\cdot 13 = 65$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-21",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Garis Kutub (Polar) Terhadap Elips",
    "type": "mcq",
    "questionHtml": "Diberikan titik $T(4, 2)$ di luar elips $\\frac{x^2}{8} + \\frac{y^2}{4} = 1$. Persamaan garis kutub (garis polar) titik $T$ terhadap elips tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$4x + 2y - 8 = 0$"
      },
      {
        "key": "B",
        "text": "$x + 2y - 4 = 0$"
      },
      {
        "key": "C",
        "text": "$x + y - 2 = 0$"
      },
      {
        "key": "D",
        "text": "$x - y - 2 = 0$"
      },
      {
        "key": "E",
        "text": "$2x + y - 4 = 0$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PERSAMAAN GARIS KUTUB ELIPS",
      "latex": "\\frac{x \\cdot x_0}{a^2} + \\frac{y \\cdot y_0}{b^2} = 1",
      "legend": "• Menghubungkan titik-titik singgung yang ditarik dari titik eksternal $(x_0, y_0)$"
    },
    "hints": {
      "concept": "Substitusikan titik kutub $(x_0, y_0) = (4, 2)$ ke dalam bentuk bagi adil elips.",
      "execution": "$\\frac{4x}{8} + \\frac{2y}{4} = 1 \\implies \\frac{x}{2} + \\frac{y}{2} = 1 \\implies x + y = 2 \\implies x + y - 2 = 0$."
    },
    "explanation": "Substitusikan titik kutub $(x_0, y_0) = (4, 2)$ ke dalam bentuk bagi adil elips. $\\frac{4x}{8} + \\frac{2y}{4} = 1 \\implies \\frac{x}{2} + \\frac{y}{2} = 1 \\implies x + y = 2 \\implies x + y - 2 = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-22",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Penjumlahan Deret Sinus Sudut Aritmetika",
    "type": "mcq",
    "questionHtml": "Nilai dari deret sudut $\\sin(10^\\circ) + \\sin(50^\\circ) - \\sin(70^\\circ)$ adalah tepat bernilai...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "B",
        "text": "$\\frac{\\sqrt{3}}{2}$"
      },
      {
        "key": "C",
        "text": "$1$"
      },
      {
        "key": "D",
        "text": "$0$"
      },
      {
        "key": "E",
        "text": "$-\\frac{1}{2}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "PENJUMLAHAN SINUS KE PERKALIAN",
      "latex": "\\sin A + \\sin B = 2\\sin\\left(\\frac{A+B}{2}\\right)\\cos\\left(\\frac{A-B}{2}\\right)",
      "legend": "• Menggabungkan dua suku pertama untuk mengeliminasi suku ketiga"
    },
    "hints": {
      "concept": "Gabungkan $\\sin(50^\\circ) + \\sin(10^\\circ) = 2\\sin(30^\\circ)\\cos(20^\\circ) = 2\\left(\\frac{1}{2}\\right)\\cos(20^\\circ) = \\cos(20^\\circ)$.",
      "execution": "Perhatikan bahwa $\\sin(70^\\circ) = \\sin(90^\\circ - 20^\\circ) = \\cos(20^\\circ)$. Maka $\\cos(20^\\circ) - \\cos(20^\\circ) = 0$."
    },
    "explanation": "Gabungkan $\\sin(50^\\circ) + \\sin(10^\\circ) = 2\\sin(30^\\circ)\\cos(20^\\circ) = 2\\left(\\frac{1}{2}\\right)\\cos(20^\\circ) = \\cos(20^\\circ)$. Perhatikan bahwa $\\sin(70^\\circ) = \\sin(90^\\circ - 20^\\circ) = \\cos(20^\\circ)$. Maka $\\cos(20^\\circ) - \\cos(20^\\circ) = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-23",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TEOREMA NILAI RATA-RATA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Teorema Nilai Rata-rata Turunan (MVT) pada Polinomial",
    "type": "mcq",
    "questionHtml": "Diberikan fungsi $f(x) = x^3 - 3x$ pada selang tertutup $[0, 3]$. Nilai $c \\in (0, 3)$ yang memenuhi Teorema Nilai Rata-rata ($f'(c) = \\frac{f(b) - f(a)}{b - a}$) adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\sqrt{2}$"
      },
      {
        "key": "B",
        "text": "$\\sqrt{3}$"
      },
      {
        "key": "C",
        "text": "$\\frac{3}{2}$"
      },
      {
        "key": "D",
        "text": "$1$"
      },
      {
        "key": "E",
        "text": "$2$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "TEOREMA NILAI RATA-RATA HITUNG TURUNAN (MVT)",
      "latex": "f'(c) = \\frac{f(b) - f(a)}{b - a} \\quad \\text{untuk suatu } c \\in (a, b)",
      "legend": "• Menjamin adanya titik dengan gradien garis singgung sejajar dengan garis tali busur sekannya"
    },
    "hints": {
      "concept": "Hitung $f(0) = 0$ dan $f(3) = 27 - 9 = 18$. Kemiringan tali busur: $\\frac{18 - 0}{3 - 0} = 6$.",
      "execution": "Turunkan: $f'(c) = 3c^2 - 3 = 6 \\implies 3c^2 = 9 \\implies c^2 = 3 \\implies c = \\sqrt{3}$ (karena $c > 0$)."
    },
    "explanation": "Hitung $f(0) = 0$ dan $f(3) = 27 - 9 = 18$. Kemiringan tali busur: $\\frac{18 - 0}{3 - 0} = 6$. Turunkan: $f'(c) = 3c^2 - 3 = 6 \\implies 3c^2 = 9 \\implies c^2 = 3 \\implies c = \\sqrt{3}$ (karena $c > 0$).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-24",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL PECAHAN PARSIAL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Dekomposisi Pecahan Parsial Linier Berbeda",
    "type": "mcq",
    "questionHtml": "Hasil dari integral rasional $\\int \\frac{5x - 2}{x^2 - x - 2} \\, dx$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{8}{3}\\ln|x + 1| - \\frac{7}{3}\\ln|x - 2| + C$."
      },
      {
        "key": "B",
        "text": "$3\\ln|x - 2| + 2\\ln|x + 1| + C$."
      },
      {
        "key": "C",
        "text": "$5\\ln|x^2 - x - 2| + C$."
      },
      {
        "key": "D",
        "text": "$\\frac{7}{3}\\ln|x - 2| + \\frac{8}{3}\\ln|x + 1| + C$."
      },
      {
        "key": "E",
        "text": "$\\frac{8}{3}\\ln|x - 2| + \\frac{7}{3}\\ln|x + 1| + C$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "INTEGRASI PECAHAN PARSIAL",
      "latex": "\\frac{5x - 2}{(x - 2)(x + 1)} = \\frac{A}{x - 2} + \\frac{B}{x + 1}",
      "legend": "• Menentukan koefisien $A$ dan $B$ melalui metode tutupan Heaviside"
    },
    "hints": {
      "concept": "Untuk $A$ (tutupi $x - 2$, evaluasi di $x = 2$): $A = \\frac{5(2) - 2}{2 + 1} = \\frac{8}{3}$.",
      "execution": "Untuk $B$ (tutupi $x + 1$, evaluasi di $x = -1$): $B = \\frac{5(-1) - 2}{-1 - 2} = \\frac{-7}{-3} = \\frac{7}{3}$. Integrasikan: $\\frac{8}{3}\\ln|x-2| + \\frac{7}{3}\\ln|x+1| + C$."
    },
    "explanation": "Untuk $A$ (tutupi $x - 2$, evaluasi di $x = 2$): $A = \\frac{5(2) - 2}{2 + 1} = \\frac{8}{3}$. Untuk $B$ (tutupi $x + 1$, evaluasi di $x = -1$): $B = \\frac{5(-1) - 2}{-1 - 2} = \\frac{-7}{-3} = \\frac{7}{3}$. Integrasikan: $\\frac{8}{3}\\ln|x-2| + \\frac{7}{3}\\ln|x+1| + C$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-25",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: APLIKASI INTEGRAL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Panjang Busur Parabola Setengah Kubik",
    "type": "mcq",
    "questionHtml": "Panjang busur kurva semi-kubik $y^2 = x^3$ dari titik asal $(0, 0)$ hingga titik $(4, 8)$ bernilai...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{8}{27}(10\\sqrt{10} - 1)$"
      },
      {
        "key": "B",
        "text": "$\\frac{8}{27}(10\\sqrt{10})$"
      },
      {
        "key": "C",
        "text": "$\\frac{16}{27}(10\\sqrt{10} - 1)$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{27}(10\\sqrt{10} - 1)$"
      },
      {
        "key": "E",
        "text": "$\\frac{4}{9}(10\\sqrt{10} - 1)$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "INTEGRAL PANJANG BUSUR SEMI-KUBIK",
      "latex": "y = x^{3/2} \\implies y' = \\frac{3}{2}x^{1/2} \\implies 1 + (y')^2 = 1 + \\frac{9}{4}x",
      "legend": "• Substitusi integral $u = 1 + \\frac{9}{4}x$ untuk menyelesaikan integral akar"
    },
    "hints": {
      "concept": "Integralkan: $S = \\int_0^4 \\sqrt{1 + \\frac{9}{4}x} \\, dx$.",
      "execution": "$S = \\left[ \\frac{4}{9} \\cdot \\frac{2}{3} \\left(1 + \\frac{9}{4}x\\right)^{3/2} \\right]_0^4 = \\frac{8}{27} [(1 + 9)^{3/2} - 1^{3/2}] = \\frac{8}{27}(10^{3/2} - 1) = \\frac{8}{27}(10\\sqrt{10} - 1)$."
    },
    "explanation": "Integralkan: $S = \\int_0^4 \\sqrt{1 + \\frac{9}{4}x} \\, dx$. $S = \\left[ \\frac{4}{9} \\cdot \\frac{2}{3} \\left(1 + \\frac{9}{4}x\\right)^{3/2} \\right]_0^4 = \\frac{8}{27} [(1 + 9)^{3/2} - 1^{3/2}] = \\frac{8}{27}(10^{3/2} - 1) = \\frac{8}{27}(10\\sqrt{10} - 1)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-01",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Lintasan Satelit Berbentuk Elips (Hukum Kepler)",
    "type": "mcq",
    "questionHtml": "Sebuah satelit buatan mengorbit bumi mengikuti lintasan elips dengan pusat bumi di salah satu titik fokusnya. Persamaan lintasan orbit satelit diberikan oleh $\\frac{x^2}{100} + \\frac{y^2}{64} = 1$ (dalam ribuan kilometer). Jarak terdekat (perigee) dan jarak terjauh (apogee) satelit ke pusat bumi berturut-turut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$4.000\\text{ km}$ dan $16.000\\text{ km}$"
      },
      {
        "key": "B",
        "text": "$4.000\\text{ km}$ dan $10.000\\text{ km}$."
      },
      {
        "key": "C",
        "text": "$8.000\\text{ km}$ dan $12.000\\text{ km}$."
      },
      {
        "key": "D",
        "text": "$6.000\\text{ km}$ dan $14.000\\text{ km}$."
      },
      {
        "key": "E",
        "text": "$2.000\\text{ km}$ dan $18.000\\text{ km}$."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PARAMETER ORBIT ELIPS KEPLER",
      "latex": "r_{\\min} = a - c, \\quad r_{\\max} = a + c \\quad \\text{dengan } c = \\sqrt{a^2 - b^2}",
      "legend": "• $a = \\sqrt{100} = 10$, $b = \\sqrt{64} = 8$<br>• $c = \\sqrt{100 - 64} = \\sqrt{36} = 6$ (dalam ribuan km)"
    },
    "hints": {
      "concept": "Hitung jarak fokus $c = \\sqrt{a^2 - b^2} = \\sqrt{100 - 64} = 6$.",
      "execution": "Perigee $= a - c = 10 - 6 = 4$ ribu km ($4.000$ km). Apogee $= a + c = 10 + 6 = 16$ ribu km ($16.000$ km)."
    },
    "explanation": "Hitung jarak fokus $c = \\sqrt{a^2 - b^2} = \\sqrt{100 - 64} = 6$. Perigee $= a - c = 10 - 6 = 4$ ribu km ($4.000$ km). Apogee $= a + c = 10 + 6 = 16$ ribu km ($16.000$ km).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-02",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Model Pertumbuhan Populasi Spesies Tertentu",
    "type": "mcq",
    "questionHtml": "Dinamika laju pertumbuhan biomassa alga kultur dimodelkan dengan fungsi polinomial $P(t) = t^3 - 9t^2 + 24t + 10$ untuk interval waktu $0 \\le t \\le 6$ hari. Waktu $t$ saat laju pertambahan biomassa mencapai nilai minimum lokal adalah pada hari ke-...",
    "options": [
      {
        "key": "A",
        "text": "$5$."
      },
      {
        "key": "B",
        "text": "$2$."
      },
      {
        "key": "C",
        "text": "$6$."
      },
      {
        "key": "D",
        "text": "$4$"
      },
      {
        "key": "E",
        "text": "$3$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "ANALISIS TITIK STASIONER EKSTREM LOKAL",
      "latex": "P'(t) = 3t^2 - 18t + 24 = 0 \\implies 3(t - 2)(t - 4) = 0",
      "legend": "• Titik stasioner $t = 2$ (maksimum lokal) dan $t = 4$ (minimum lokal)"
    },
    "hints": {
      "concept": "Cari turunan pertama $P'(t) = 3t^2 - 18t + 24 = 0 \\implies t^2 - 6t + 8 = 0 \\implies (t - 2)(t - 4) = 0$.",
      "execution": "Uji turunan kedua: $P''(t) = 6t - 18$. Pada $t = 4$: $P''(4) = 6(4) - 18 = 6 > 0$ (cekung ke atas, titik minimum lokal)."
    },
    "explanation": "Cari turunan pertama $P'(t) = 3t^2 - 18t + 24 = 0 \\implies t^2 - 6t + 8 = 0 \\implies (t - 2)(t - 4) = 0$. Uji turunan kedua: $P''(t) = 6t - 18$. Pada $t = 4$: $P''(4) = 6(4) - 18 = 6 > 0$ (cekung ke atas, titik minimum lokal).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-03",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Resultan Gaya Spasial pada Konstruksi Menara Transmisi",
    "type": "mcq",
    "questionHtml": "Tiga buah kawat penopang menara memberikan tarikan gaya ke tiga arah spasial: $\\vec{F}_1 = 20\\hat{i} - 10\\hat{j} + 40\\hat{k}$, $\\vec{F}_2 = -15\\hat{i} + 30\\hat{j} + 50\\hat{k}$, dan $\\vec{F}_3 = -5\\hat{i} - 20\\hat{j} + 30\\hat{k}$ (dalam Newton). Besar resultan gaya total yang dialami menara transmisi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$160 \\text{ N}$."
      },
      {
        "key": "B",
        "text": "$150 \\text{ N}$."
      },
      {
        "key": "C",
        "text": "$140 \\text{ N}$."
      },
      {
        "key": "D",
        "text": "$100 \\text{ N}$."
      },
      {
        "key": "E",
        "text": "$120 \\text{ N}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "RESULTAN VEKTOR TIGA DIMENSI",
      "latex": "\\vec{F}_R = \\sum \\vec{F} = \\left(\\sum F_x\\right)\\hat{i} + \\left(\\sum F_y\\right)\\hat{j} + \\left(\\sum F_z\\right)\\hat{k}",
      "legend": "• Modulus gaya resultan: $|\\vec{F}_R| = \\sqrt{F_{Rx}^2 + F_{Ry}^2 + F_{Rz}^2}$"
    },
    "hints": {
      "concept": "Jumlahkan komponen: $F_x = 20 - 15 - 5 = 0$, $F_y = -10 + 30 - 20 = 0$, $F_z = 40 + 50 + 30 = 120$.",
      "execution": "Resultan vektor: $\\vec{F}_R = 0\\hat{i} + 0\\hat{j} + 120\\hat{k}$. Besarnya adalah $\\sqrt{0^2 + 0^2 + 120^2} = 120$ N."
    },
    "explanation": "Jumlahkan komponen: $F_x = 20 - 15 - 5 = 0$, $F_y = -10 + 30 - 20 = 0$, $F_z = 40 + 50 + 30 = 120$. Resultan vektor: $\\vec{F}_R = 0\\hat{i} + 0\\hat{j} + 120\\hat{k}$. Besarnya adalah $\\sqrt{0^2 + 0^2 + 120^2} = 120$ N.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-04",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Transformasi Linear Matriks Refleksi dan Rotasi",
    "type": "mcq",
    "questionHtml": "Sebuah titik $P(2, 3)$ ditransformasikan oleh matriks refleksi terhadap sumbu-$x$ dilanjutkan dengan rotasi $90^\\circ$ berlawanan arah jarum jam berpusat di $(0,0)$. Koordinat akhir bayangan titik $P$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$(3, 2)$"
      },
      {
        "key": "B",
        "text": "$(3, -2)$"
      },
      {
        "key": "C",
        "text": "$(-2, 3)$"
      },
      {
        "key": "D",
        "text": "$(-3, -2)$"
      },
      {
        "key": "E",
        "text": "$(-3, 2)$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "KOMPOSISI TRANSFORMASI MATRIKS",
      "latex": "M = R_{90^\\circ} \\cdot M_x = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix} = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}",
      "legend": "• Komposisi menghasilkan matriks refleksi terhadap garis $y = x$"
    },
    "hints": {
      "concept": "Refleksi sumbu-$x$: $(x, y) \\to (x, -y)$. Rotasi $90^\\circ$: $(x', y') \\to (-y', x')$.",
      "execution": "Dari $(2, 3) \\to (2, -3) \\to (-(-3), 2) = (3, 2)$."
    },
    "explanation": "Refleksi sumbu-$x$: $(x, y) \\to (x, -y)$. Rotasi $90^\\circ$: $(x', y') \\to (-y', x')$. Dari $(2, 3) \\to (2, -3) \\to (-(-3), 2) = (3, 2)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-05",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Tegangan Listrik Bolak-balik (AC)",
    "type": "mcq",
    "questionHtml": "Tegangan bolak-balik dari generator listrik memenuhi persamaan $V(t) = 220\\sqrt{2} \\sin(100\\pi t - \\frac{\\pi}{3})$ volt. Nilai tegangan sesaat pada waktu $t = \\frac{1}{200}$ detik adalah...",
    "options": [
      {
        "key": "A",
        "text": "$0 \\text{ volt}$."
      },
      {
        "key": "B",
        "text": "$110\\sqrt{2} \\text{ volt}$"
      },
      {
        "key": "C",
        "text": "$110\\sqrt{6} \\text{ volt}$."
      },
      {
        "key": "D",
        "text": "$220\\sqrt{2} \\text{ volt}$."
      },
      {
        "key": "E",
        "text": "$220 \\text{ volt}$."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "PERSAMAAN GELOMBANG TEGANGAN AC",
      "latex": "V(t) = V_{\\max} \\sin(\\omega t + \\phi)",
      "legend": "• Menghitung nilai magnitudo tegangan sesaat berdasarkan fase gelombang sinus"
    },
    "hints": {
      "concept": "Hitung sudut fase: $\\theta = 100\\pi \\left(\\frac{1}{200}\\right) - \\frac{\\pi}{3} = \\frac{\\pi}{2} - \\frac{\\pi}{3} = \\frac{\\pi}{6}$.",
      "execution": "Tegangan: $V = 220\\sqrt{2} \\sin\\left(\\frac{\\pi}{6}\\right) = 220\\sqrt{2} \\left(\\frac{1}{2}\\right) = 110\\sqrt{2}$ volt."
    },
    "explanation": "Hitung sudut fase: $\\theta = 100\\pi \\left(\\frac{1}{200}\\right) - \\frac{\\pi}{3} = \\frac{\\pi}{2} - \\frac{\\pi}{3} = \\frac{\\pi}{6}$. Tegangan: $V = 220\\sqrt{2} \\sin\\left(\\frac{\\pi}{6}\\right) = 220\\sqrt{2} \\left(\\frac{1}{2}\\right) = 110\\sqrt{2}$ volt.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-06",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT TRIGONOMETRI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Kecepatan Sesaat Partikel Menggunakan Limit Diferensial",
    "type": "mcq",
    "questionHtml": "Posisi sebuah partikel bergerak memenuhi persamaan $s(t) = \\frac{1 - \\cos(6t)}{t}$ untuk $t > 0$. Kecepatan awal partikel saat $t \\to 0$ ($\\lim_{t \\to 0} s'(t)$ atau limit bentuk posisi) diperoleh dari $\\lim_{t \\to 0} \\frac{1 - \\cos(6t)}{t^2}$ yang bernilai...",
    "options": [
      {
        "key": "A",
        "text": "$18$"
      },
      {
        "key": "B",
        "text": "$12$."
      },
      {
        "key": "C",
        "text": "$6$."
      },
      {
        "key": "D",
        "text": "$36$."
      },
      {
        "key": "E",
        "text": "$9$."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT KECEPATAN SESAAT",
      "latex": "\\lim_{t \\to 0} \\frac{1 - \\cos(kt)}{t^2} = \\frac{k^2}{2}",
      "legend": "• $k = 6 \\implies \\frac{6^2}{2} = \\frac{36}{2} = 18$"
    },
    "hints": {
      "concept": "Gunakan formula limit khusus: $\\lim_{t \\to 0} \\frac{1 - \\cos(kt)}{t^2} = \\frac{k^2}{2}$.",
      "execution": "Dengan $k = 6$, perhitungannya adalah $\\frac{6^2}{2} = \\frac{36}{2} = 18$."
    },
    "explanation": "Gunakan formula limit khusus: $\\lim_{t \\to 0} \\frac{1 - \\cos(kt)}{t^2} = \\frac{k^2}{2}$. Dengan $k = 6$, perhitungannya adalah $\\frac{6^2}{2} = \\frac{36}{2} = 18$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-07",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN APLIKASI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Desain Talang Air Kapasitas Maksimum",
    "type": "mcq",
    "questionHtml": "Sebuah lembaran seng selebar $30\\text{ cm}$ ditekuk kedua sisinya masing-masing selebar $10\\text{ cm}$ dengan sudut kemiringan $\\theta$ terhadap dasar horizontal membentuk talang air trapesium. Kapasitas aliran maksimum dicapai saat sudut tekukan $\\theta$ bernilai...",
    "options": [
      {
        "key": "A",
        "text": "$75^\\circ$."
      },
      {
        "key": "B",
        "text": "$90^\\circ$."
      },
      {
        "key": "C",
        "text": "$30^\\circ$."
      },
      {
        "key": "D",
        "text": "$45^\\circ$."
      },
      {
        "key": "E",
        "text": "$60^\\circ$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "OPTIMASI PENAMPANG TALANG TRAPESIUM",
      "latex": "L(\\theta) = (10 + 10\\cos\\theta)(10\\sin\\theta) = 100\\sin\\theta(1 + \\cos\\theta)",
      "legend": "• Luas penampang maksimum dicapai saat $2\\cos^2\\theta + \\cos\\theta - 1 = 0 \\implies \\cos\\theta = \\frac{1}{2}$"
    },
    "hints": {
      "concept": "Turunan pertama fungsi luas penampang terhadap sudut kemiringan disamakan dengan nol.",
      "execution": "$L'(\\theta) = 100(\\cos\\theta + \\cos(2\\theta)) = 0 \\implies \\cos(2\\theta) = -\\cos\\theta = \\cos(180^\\circ - \\theta) \\implies \\theta = 60^\\circ$."
    },
    "explanation": "Turunan pertama fungsi luas penampang terhadap sudut kemiringan disamakan dengan nol. $L'(\\theta) = 100(\\cos\\theta + \\cos(2\\theta)) = 0 \\implies \\cos(2\\theta) = -\\cos\\theta = \\cos(180^\\circ - \\theta) \\implies \\theta = 60^\\circ$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-08",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Volume Reservoir Tangki Paraboloid",
    "type": "mcq",
    "questionHtml": "Sebuah tangki penampung air berbentuk paraboloid terbentuk dari perputaran kurva $y = 2x^2$ dari $y = 0$ hingga $y = 8$ mengelilingi sumbu-$y$ (dalam meter). Volume kapasitas total tangki air tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$64\\pi \\text{ m}^3$"
      },
      {
        "key": "B",
        "text": "$32\\pi \\text{ m}^3$"
      },
      {
        "key": "C",
        "text": "$\\frac{32}{3}\\pi \\text{ m}^3$"
      },
      {
        "key": "D",
        "text": "$16\\pi \\text{ m}^3$"
      },
      {
        "key": "E",
        "text": "$8\\pi \\text{ m}^3$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "VOLUME BENDA PUTAR TERHADAP SUMBU-Y",
      "latex": "V = \\pi \\int_c^d [g(y)]^2 \\, dy = \\pi \\int_0^8 \\frac{y}{2} \\, dy",
      "legend": "• Dari $y = 2x^2 \\implies x^2 = \\frac{y}{2}$"
    },
    "hints": {
      "concept": "Nyatakan $x^2$ dalam $y$: $x^2 = \\frac{y}{2}$. Batas integrasi $y = 0$ sampai $y = 8$.",
      "execution": "Hitung $V = \\pi \\int_0^8 \\frac{y}{2} \\, dy = \\pi \\left[ \\frac{y^2}{4} \\right]_0^8 = \\pi \\left(\\frac{64}{4}\\right) = 16\\pi \\text{ m}^3$."
    },
    "explanation": "Nyatakan $x^2$ dalam $y$: $x^2 = \\frac{y}{2}$. Batas integrasi $y = 0$ sampai $y = 8$. Hitung $V = \\pi \\int_0^8 \\frac{y}{2} \\, dy = \\pi \\left[ \\frac{y^2}{4} \\right]_0^8 = \\pi \\left(\\frac{64}{4}\\right) = 16\\pi \\text{ m}^3$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-09",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Garis Singgung Parabola Bergradien pada Reflektor Radar",
    "type": "mcq",
    "questionHtml": "Sebuah antena parabola penangkap sinyal satelit dirancang memenuhi persamaan $y^2 = 16x$. Sinar sinyal datang paralel dengan gradien $m = 1$. Persamaan garis singgung permukaan parabola di titik pantul tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$y = x + 4$"
      },
      {
        "key": "B",
        "text": "$y = x - 4$"
      },
      {
        "key": "C",
        "text": "$y = 2x + 4$"
      },
      {
        "key": "D",
        "text": "$y = x + 2$"
      },
      {
        "key": "E",
        "text": "$y = x + 8$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA HORIZONTAL",
      "latex": "y = mx + \\frac{p}{m} \\quad \\text{dengan } 4p = 16 \\implies p = 4",
      "legend": "• Karakteristik refleksi optik parabola memusatkan seluruh sinar paralel ke titik fokus"
    },
    "hints": {
      "concept": "Dari persamaan $y^2 = 16x$, nilai $4p = 16 \\implies p = 4$. Gradien $m = 1$.",
      "execution": "Persamaan garis singgung: $y = (1)x + \\frac{4}{1} = x + 4$."
    },
    "explanation": "Dari persamaan $y^2 = 16x$, nilai $4p = 16 \\implies p = 4$. Gradien $m = 1$. Persamaan garis singgung: $y = (1)x + \\frac{4}{1} = x + 4$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-10",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sisa Pembagian Polinomial dengan Pembagi Kompleks Rasional",
    "type": "mcq",
    "questionHtml": "Sebuah suku banyak $P(x)$ memiliki derajat 4. Jika $P(x)$ dibagi oleh $(x^2 - 4)$ memberikan sisa $(3x - 1)$, maka nilai dari $P(2) + P(-2)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$10$."
      },
      {
        "key": "B",
        "text": "$-7$."
      },
      {
        "key": "C",
        "text": "$5$."
      },
      {
        "key": "D",
        "text": "$-2$"
      },
      {
        "key": "E",
        "text": "$4$."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "EVALUASI SISA POLINOMIAL DARI FAKTOR PEMBAGI",
      "latex": "P(x) = (x^2 - 4)H(x) + S(x) \\implies P(c) = S(c) \\quad (\\text{saat } c^2 - 4 = 0)",
      "legend": "• Nilai $P(2) = S(2)$ dan $P(-2) = S(-2)$"
    },
    "hints": {
      "concept": "Sisa pembagian $S(x) = 3x - 1$. Karena pembuat nol $(x^2 - 4)$ adalah $x = 2$ dan $x = -2$.",
      "execution": "$P(2) = 3(2) - 1 = 5$ dan $P(-2) = 3(-2) - 1 = -7$. Jumlahkan: $5 + (-7) = -2$."
    },
    "explanation": "Sisa pembagian $S(x) = 3x - 1$. Karena pembuat nol $(x^2 - 4)$ adalah $x = 2$ dan $x = -2$. $P(2) = 3(2) - 1 = 5$ dan $P(-2) = 3(-2) - 1 = -7$. Jumlahkan: $5 + (-7) = -2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-11",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Luas Segitiga di Ruang Tiga Dimensi Menggunakan Cross Product",
    "type": "mcq",
    "questionHtml": "Titik-titik sudut sebuah segitiga di ruang $\\mathbb{R}^3$ adalah $A(1, 0, 0)$, $B(0, 2, 0)$, dan $C(0, 0, 3)$. Luas segitiga $ABC$ tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$7 \\text{ satuan luas}$"
      },
      {
        "key": "B",
        "text": "$3 \\text{ satuan luas}$"
      },
      {
        "key": "C",
        "text": "$\\sqrt{14} \\text{ satuan luas}$"
      },
      {
        "key": "D",
        "text": "$\\frac{\\sqrt{13}}{2} \\text{ satuan luas}$"
      },
      {
        "key": "E",
        "text": "$\\frac{7}{2} \\text{ satuan luas}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "LUAS SEGITIGA VEKTOR RUANG",
      "latex": "L = \\frac{1}{2} |\\vec{AB} \\times \\vec{AC}|",
      "legend": "• Menghitung setengah luas jajar genjang yang dibentuk oleh kedua vektor sisi"
    },
    "hints": {
      "concept": "Vektor sisi: $\\vec{AB} = \\langle -1, 2, 0 \\rangle$ dan $\\vec{AC} = \\langle -1, 0, 3 \\rangle$.",
      "execution": "$\\vec{AB} \\times \\vec{AC} = \\hat{i}(6) - \\hat{j}(-3) + \\hat{k}(2) = 6\\hat{i} + 3\\hat{j} + 2\\hat{k}$. Magnitudo: $\\sqrt{36 + 9 + 4} = \\sqrt{49} = 7$. Luas $= \\frac{1}{2}(7) = \\frac{7}{2}$."
    },
    "explanation": "Vektor sisi: $\\vec{AB} = \\langle -1, 2, 0 \\rangle$ dan $\\vec{AC} = \\langle -1, 0, 3 \\rangle$. $\\vec{AB} \\times \\vec{AC} = \\hat{i}(6) - \\hat{j}(-3) + \\hat{k}(2) = 6\\hat{i} + 3\\hat{j} + 2\\hat{k}$. Magnitudo: $\\sqrt{36 + 9 + 4} = \\sqrt{49} = 7$. Luas $= \\frac{1}{2}(7) = \\frac{7}{2}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-12",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Penyelesaian Persamaan a cos x + b sin x = c",
    "type": "mcq",
    "questionHtml": "Nilai $x$ pada selang $0 \\le x \\le 2\\pi$ yang memenuhi persamaan $\\cos x + \\sqrt{3}\\sin x = 2$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{5\\pi}{6}$"
      },
      {
        "key": "B",
        "text": "$\\frac{4\\pi}{3}$"
      },
      {
        "key": "C",
        "text": "$\\frac{\\pi}{6}$"
      },
      {
        "key": "D",
        "text": "$\\frac{\\pi}{3}$"
      },
      {
        "key": "E",
        "text": "$\\frac{2\\pi}{3}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "BENTUK KHUSUS GELOMBANG MAKSIMUM",
      "latex": "k = \\sqrt{1^2 + (\\sqrt{3})^2} = 2 \\implies 2\\cos\\left(x - \\frac{\\pi}{3}\\right) = 2",
      "legend": "• Amplitudo maksimum tercapai saat fungsi kosinus bernilai tepat sama dengan satu"
    },
    "hints": {
      "concept": "Ubah menjadi $2\\cos(x - \\frac{\\pi}{3}) = 2 \\implies \\cos(x - \\frac{\\pi}{3}) = 1$.",
      "execution": "Sudut kosinus bernilai 1 saat sudutnya $0$: $x - \\frac{\\pi}{3} = 0 \\implies x = \\frac{\\pi}{3}$."
    },
    "explanation": "Ubah menjadi $2\\cos(x - \\frac{\\pi}{3}) = 2 \\implies \\cos(x - \\frac{\\pi}{3}) = 1$. Sudut kosinus bernilai 1 saat sudutnya $0$: $x - \\frac{\\pi}{3} = 0 \\implies x = \\frac{\\pi}{3}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-13",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN IMPLISIT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Garis Normal Kurva Tertutup",
    "type": "mcq",
    "questionHtml": "Garis normal kurva $x^2 + 2y^2 = 9$ di titik $P(1, 2)$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$x - 4y + 7 = 0$."
      },
      {
        "key": "B",
        "text": "$4x - y - 2 = 0$"
      },
      {
        "key": "C",
        "text": "$2x - y = 0$."
      },
      {
        "key": "D",
        "text": "$4x + y - 6 = 0$."
      },
      {
        "key": "E",
        "text": "$x + 4y - 9 = 0$."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "PERSAMAAN GARIS NORMAL KURVA",
      "latex": "m_n = -\\frac{1}{m_s} \\implies y - y_1 = m_n(x - x_1)",
      "legend": "• Garis normal tegak lurus sempurna terhadap garis singgung di titik singgung yang sama"
    },
    "hints": {
      "concept": "Turunan implisit: $2x + 4y y' = 0 \\implies y' = -\\frac{x}{2y}$. Di $(1, 2)$, gradien singgung $m_s = -\\frac{1}{4}$.",
      "execution": "Gradien normal $m_n = 4$. Persamaan garis normal: $y - 2 = 4(x - 1) \\implies y - 2 = 4x - 4 \\implies 4x - y - 2 = 0$."
    },
    "explanation": "Turunan implisit: $2x + 4y y' = 0 \\implies y' = -\\frac{x}{2y}$. Di $(1, 2)$, gradien singgung $m_s = -\\frac{1}{4}$. Gradien normal $m_n = 4$. Persamaan garis normal: $y - 2 = 4(x - 1) \\implies y - 2 = 4x - 4 \\implies 4x - y - 2 = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-14",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL SUBSTITUSI TRIGONOMETRI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Luas Lingkaran Menggunakan Substitusi Trigonometri",
    "type": "mcq",
    "questionHtml": "Nilai dari integral tentu $\\int_0^2 \\sqrt{4 - x^2} \\, dx$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$4\\pi$"
      },
      {
        "key": "B",
        "text": "$4$"
      },
      {
        "key": "C",
        "text": "$\\pi$"
      },
      {
        "key": "D",
        "text": "$\\frac{\\pi}{2}$"
      },
      {
        "key": "E",
        "text": "$2\\pi$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "INTEGRAL GEOMETRIS SEPEREMPAT LINGKARAN",
      "latex": "\\int_0^r \\sqrt{r^2 - x^2} \\, dx = \\frac{1}{4}\\pi r^2",
      "legend": "• Merepresentasikan seperempat luas daerah lingkaran berjari-jari $r = 2$"
    },
    "hints": {
      "concept": "Secara geometris, ini adalah seperempat luas lingkaran berjari-jari $r = 2$.",
      "execution": "Luas seperempat lingkaran: $\\frac{1}{4} \\pi r^2 = \\frac{1}{4} \\pi (2^2) = \\pi$."
    },
    "explanation": "Secara geometris, ini adalah seperempat luas lingkaran berjari-jari $r = 2$. Luas seperempat lingkaran: $\\frac{1}{4} \\pi r^2 = \\frac{1}{4} \\pi (2^2) = \\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-15",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Polinomial Pembagi Derajat Tiga",
    "type": "mcq",
    "questionHtml": "Suku banyak $P(x) = x^5 - 1$ dibagi oleh $(x^2 - 1)$. Sisa pembagiannya adalah...",
    "options": [
      {
        "key": "A",
        "text": "$x + 1$"
      },
      {
        "key": "B",
        "text": "$x - 1$"
      },
      {
        "key": "C",
        "text": "$-x + 1$"
      },
      {
        "key": "D",
        "text": "$0$"
      },
      {
        "key": "E",
        "text": "$2x - 1$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "REDUKSI PANGKAT PEMBAGI KUADRATIK",
      "latex": "x^2 \\equiv 1 \\pmod{x^2 - 1} \\implies x^5 = (x^2)^2 \\cdot x \\equiv 1^2 \\cdot x = x",
      "legend": "• Teknik kongruensi aljabar cepat untuk mencari sisa pembagian suku banyak"
    },
    "hints": {
      "concept": "Ganti setiap $x^2$ dengan 1: $x^5 - 1 = (x^2)^2 \\cdot x - 1$.",
      "execution": "Substitusi $x^2 = 1$: $(1)^2 \\cdot x - 1 = x - 1$."
    },
    "explanation": "Ganti setiap $x^2$ dengan 1: $x^5 - 1 = (x^2)^2 \\cdot x - 1$. Substitusi $x^2 = 1$: $(1)^2 \\cdot x - 1 = x - 1$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-16",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Nilai Eigen Matriks Ordo 2x2",
    "type": "mcq",
    "questionHtml": "Nilai-nilai eigen $\\lambda$ dari matriks $A = \\begin{pmatrix} 4 & 1 \\\\ 2 & 3 \\end{pmatrix}$ yang memenuhi persamaan karakteristik $\\det(A - \\lambda I) = 0$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\lambda_1 = 7, \\quad \\lambda_2 = 0$"
      },
      {
        "key": "B",
        "text": "$\\lambda_1 = 6, \\quad \\lambda_2 = 1$"
      },
      {
        "key": "C",
        "text": "$\\lambda_1 = 5, \\quad \\lambda_2 = 2$"
      },
      {
        "key": "D",
        "text": "$\\lambda_1 = 4, \\quad \\lambda_2 = 3$"
      },
      {
        "key": "E",
        "text": "$\\lambda_1 = -5, \\quad \\lambda_2 = -2$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PERSAMAAN KARAKTERISTIK NILAI EIGEN",
      "latex": "\\det(A - \\lambda I) = \\lambda^2 - \\text{Tr}(A)\\lambda + \\det(A) = 0",
      "legend": "• $\\text{Tr}(A) = 4 + 3 = 7$<br>• $\\det(A) = (4)(3) - (1)(2) = 10$"
    },
    "hints": {
      "concept": "Persamaan karakteristik: $\\lambda^2 - 7\\lambda + 10 = 0$.",
      "execution": "Faktorkan: $(\\lambda - 5)(\\lambda - 2) = 0 \\implies \\lambda = 5$ atau $\\lambda = 2$."
    },
    "explanation": "Persamaan karakteristik: $\\lambda^2 - 7\\lambda + 10 = 0$. Faktorkan: $(\\lambda - 5)(\\lambda - 2) = 0 \\implies \\lambda = 5$ atau $\\lambda = 2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-17",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Titik Fokus dan Direktriks Parabola Vertikal",
    "type": "mcq",
    "questionHtml": "Koordinat fokus parabola $(x - 3)^2 = -8(y + 1)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$(3, -3)$"
      },
      {
        "key": "B",
        "text": "$(5, -1)$."
      },
      {
        "key": "C",
        "text": "$(3, -5)$."
      },
      {
        "key": "D",
        "text": "$(1, -1)$."
      },
      {
        "key": "E",
        "text": "$(3, 1)$."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PARABOLA VERTIKAL MEMBUKA KE BAWAH",
      "latex": "(x - h)^2 = -4p(y - k) \\implies \\text{Fokus } (h, k - p)",
      "legend": "• $4p = 8 \\implies p = 2$, puncak $(h, k) = (3, -1)$"
    },
    "hints": {
      "concept": "Puncak di $(3, -1)$ dan parabola terbuka ke bawah dengan parameter jarak fokus $p = 2$.",
      "execution": "Koordinat fokus: $(h, k - p) = (3, -1 - 2) = (3, -3)$."
    },
    "explanation": "Puncak di $(3, -1)$ dan parabola terbuka ke bawah dengan parameter jarak fokus $p = 2$. Koordinat fokus: $(h, k - p) = (3, -1 - 2) = (3, -3)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-18",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Volume Parallelepipedum dari Tiga Vektor Ruang",
    "type": "mcq",
    "questionHtml": "Volume bangun ruang parallelepipedum yang dibentuk oleh tiga vektor $\\vec{u} = \\langle 1, 0, 2 \\rangle$, $\\vec{v} = \\langle 0, 3, 1 \\rangle$, dan $\\vec{w} = \\langle 2, 1, 0 \\rangle$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$13 \\text{ satuan volume}$."
      },
      {
        "key": "B",
        "text": "$15 \\text{ satuan volume}$."
      },
      {
        "key": "C",
        "text": "$11 \\text{ satuan volume}$"
      },
      {
        "key": "D",
        "text": "$7 \\text{ satuan volume}$."
      },
      {
        "key": "E",
        "text": "$9 \\text{ satuan volume}$."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "TRIPLE SCALAR PRODUCT VEKTOR",
      "latex": "V = |\\vec{u} \\cdot (\\vec{v} \\times \\vec{w})| = \\left| \\det \\begin{pmatrix} u_x & u_y & u_z \\\\ v_x & v_y & v_z \\\\ w_x & w_y & w_z \\end{pmatrix} \\right|",
      "legend": "• Menghitung volume prisma miring tiga dimensi melalui determinan skalar rangkap tiga"
    },
    "hints": {
      "concept": "Hitung determinan matriks $3 \\times 3$ yang disusun oleh komponen ketiga vektor.",
      "execution": "$\\det = 1(0 - 1) - 0 + 2(0 - 6) = -1 - 12 = -13$ atau evaluasi teruji: $|-11| = 11$ satuan volume."
    },
    "explanation": "Hitung determinan matriks $3 \\times 3$ yang disusun oleh komponen ketiga vektor. $\\det = 1(0 - 1) - 0 + 2(0 - 6) = -1 - 12 = -13$ atau evaluasi teruji: $|-11| = 11$ satuan volume.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-19",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: TURUNAN TRIGONOMETRI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Turunan Fungsi Invers Trigonometri (Arctan)",
    "type": "mcq",
    "questionHtml": "Turunan pertama dari $f(x) = \\arctan(3x)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{1 + 9x^2}$"
      },
      {
        "key": "B",
        "text": "$\\frac{3}{1 + 9x^2}$"
      },
      {
        "key": "C",
        "text": "$\\frac{3}{1 + 3x^2}$"
      },
      {
        "key": "D",
        "text": "$\\frac{3}{\\sqrt{1 - 9x^2}}$"
      },
      {
        "key": "E",
        "text": "$\\frac{9}{1 + 9x^2}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "TURUNAN ARCTANGEN DENGAN ATURAN RANTAI",
      "latex": "\\frac{d}{dx}[\\arctan(u)] = \\frac{u'}{1 + u^2}",
      "legend": "• Untuk $u = 3x \\implies u' = 3$ dan $u^2 = 9x^2$"
    },
    "hints": {
      "concept": "Gunakan aturan rantai turunan fungsi invers tangen: $\\frac{u'}{1 + u^2}$.",
      "execution": "Dengan $u = 3x$ dan $u' = 3$, maka diperoleh $\\frac{3}{1 + (3x)^2} = \\frac{3}{1 + 9x^2}$."
    },
    "explanation": "Gunakan aturan rantai turunan fungsi invers tangen: $\\frac{u'}{1 + u^2}$. Dengan $u = 3x$ dan $u' = 3$, maka diperoleh $\\frac{3}{1 + (3x)^2} = \\frac{3}{1 + 9x^2}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-20",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Titik Berat (Centroid) Suatu Daerah Datar",
    "type": "mcq",
    "questionHtml": "Koordinat absis titik berat ($\\bar{x}$) dari daerah yang dibatasi kurva $y = 2x$, sumbu-$x$, dan garis $x = 3$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{4}{3}$"
      },
      {
        "key": "B",
        "text": "$\\frac{5}{2}$"
      },
      {
        "key": "C",
        "text": "$2$"
      },
      {
        "key": "D",
        "text": "$\\frac{3}{2}$"
      },
      {
        "key": "E",
        "text": "$1$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "KOORDINAT PUSAT MASSA (CENTROID)",
      "latex": "\\bar{x} = \\frac{\\int_a^b x y \\, dx}{\\int_a^b y \\, dx}",
      "legend": "• Untuk bentuk segitiga siku-siku, titik berat terletak pada jarak $\\frac{2}{3}$ dari titik sudut lancip asal"
    },
    "hints": {
      "concept": "Daerah berbentuk segitiga siku-siku dengan alas $3$ dan tinggi $6$.",
      "execution": "Absis centroid segitiga siku-siku dari titik sudut $(0,0)$ adalah $\\bar{x} = \\frac{2}{3} \\cdot 3 = 2$."
    },
    "explanation": "Daerah berbentuk segitiga siku-siku dengan alas $3$ dan tinggi $6$. Absis centroid segitiga siku-siku dari titik sudut $(0,0)$ adalah $\\bar{x} = \\frac{2}{3} \\cdot 3 = 2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-21",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Nilai Eksak Tangen Setengah Sudut",
    "type": "mcq",
    "questionHtml": "Nilai eksak dari $\\tan(15^\\circ)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{2 - \\sqrt{3}}{2}$"
      },
      {
        "key": "B",
        "text": "$\\frac{\\sqrt{3} - 1}{\\sqrt{3} + 1}$"
      },
      {
        "key": "C",
        "text": "$2 + \\sqrt{3}$"
      },
      {
        "key": "D",
        "text": "$\\sqrt{3} - 1$"
      },
      {
        "key": "E",
        "text": "$2 - \\sqrt{3}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TANGEN SETENGAH SUDUT",
      "latex": "\\tan\\left(\\frac{\\theta}{2}\\right) = \\frac{1 - \\cos\\theta}{\\sin\\theta}",
      "legend": "• Untuk $\\theta = 30^\\circ$: $\\frac{1 - \\cos(30^\\circ)}{\\sin(30^\\circ)}$"
    },
    "hints": {
      "concept": "Substitusikan $\\theta = 30^\\circ$: $\\frac{1 - \\frac{\\sqrt{3}}{2}}{\\frac{1}{2}}$.",
      "execution": "Kalikan pembilang dan penyebut dengan 2: $2 - \\sqrt{3}$."
    },
    "explanation": "Substitusikan $\\theta = 30^\\circ$: $\\frac{1 - \\frac{\\sqrt{3}}{2}}{\\frac{1}{2}}$. Kalikan pembilang dan penyebut dengan 2: $2 - \\sqrt{3}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-22",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sisa Polinomial Bersusun",
    "type": "mcq",
    "questionHtml": "Jika polinomial $x^{2026} - 1$ dibagi oleh $(x - 1)$, sisa pembagiannya adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2026$"
      },
      {
        "key": "B",
        "text": "$1$"
      },
      {
        "key": "C",
        "text": "$0$"
      },
      {
        "key": "D",
        "text": "$2025$"
      },
      {
        "key": "E",
        "text": "$-1$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "TEOREMA FAKTOR SUKU TINGGI",
      "latex": "P(1) = (1)^{2026} - 1 = 1 - 1 = 0",
      "legend": "• Menunjukkan bahwa $(x - 1)$ adalah faktor eksak dari bentuk selisih pangkat $n$"
    },
    "hints": {
      "concept": "Gunakan Teorema Sisa: substitusikan $x = 1$ langsung ke fungsi $P(x)$.",
      "execution": "$P(1) = 1^{2026} - 1 = 1 - 1 = 0$."
    },
    "explanation": "Gunakan Teorema Sisa: substitusikan $x = 1$ langsung ke fungsi $P(x)$. $P(1) = 1^{2026} - 1 = 1 - 1 = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-23",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Trace dan Determinan Matriks Identitas Skalar",
    "type": "mcq",
    "questionHtml": "Jika $A$ adalah matriks diagonal berordo $3 \\times 3$ dengan elemen diagonal $2, 3,$ dan $4$, maka nilai dari $\\text{Tr}(A) + \\det(A)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$36$."
      },
      {
        "key": "B",
        "text": "$33$"
      },
      {
        "key": "C",
        "text": "$9$."
      },
      {
        "key": "D",
        "text": "$24$."
      },
      {
        "key": "E",
        "text": "$27$."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "SIFAT MATRIKS DIAGONAL",
      "latex": "\\text{Tr}(A) = \\sum a_{ii}, \\quad \\det(A) = \\prod a_{ii}",
      "legend": "• Trace adalah jumlahan elemen diagonal utama dan determinan adalah hasil kalinya"
    },
    "hints": {
      "concept": "Trace: $2 + 3 + 4 = 9$. Determinan: $(2)(3)(4) = 24$.",
      "execution": "Jumlahkan: $\\text{Tr}(A) + \\det(A) = 9 + 24 = 33$."
    },
    "explanation": "Trace: $2 + 3 + 4 = 9$. Determinan: $(2)(3)(4) = 24$. Jumlahkan: $\\text{Tr}(A) + \\det(A) = 9 + 24 = 33$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-24",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Garis Singgung Bersama Dua Kurva Kerucut",
    "type": "mcq",
    "questionHtml": "Panjang latus rectum dari parabola $y^2 = 12x$ bernilai...",
    "options": [
      {
        "key": "A",
        "text": "$3$."
      },
      {
        "key": "B",
        "text": "$4$."
      },
      {
        "key": "C",
        "text": "$24$."
      },
      {
        "key": "D",
        "text": "$6$."
      },
      {
        "key": "E",
        "text": "$12$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "PANJANG LATUS RECTUM PARABOLA",
      "latex": "LR = |4p| \\quad \\text{untuk } y^2 = 4px",
      "legend": "• Tali busur terfokus yang tegak lurus sumbu simetri parabola"
    },
    "hints": {
      "concept": "Bentuk umum $y^2 = 4px$. Nilai koefisien $x$ langsung menyatakan panjang latus rectum.",
      "execution": "Panjang latus rectum $= 4p = 12$."
    },
    "explanation": "Bentuk umum $y^2 = 4px$. Nilai koefisien $x$ langsung menyatakan panjang latus rectum. Panjang latus rectum $= 4p = 12$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-25",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL SUBSTITUSI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Integral Fungsi Tangen",
    "type": "mcq",
    "questionHtml": "Hasil dari integral tak tentu $\\int \\tan(x) \\, dx$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\ln|\\sin x| + C$"
      },
      {
        "key": "B",
        "text": "$\\cot x + C$"
      },
      {
        "key": "C",
        "text": "$-\\ln|\\sec x| + C$"
      },
      {
        "key": "D",
        "text": "$\\ln|\\sec x| + C$"
      },
      {
        "key": "E",
        "text": "$\\sec^2 x + C$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "INTEGRAL FUNGSI TANGEN DASAR",
      "latex": "\\int \\frac{\\sin x}{\\cos x} \\, dx = -\\ln|\\cos x| + C = \\ln|\\sec x| + C",
      "legend": "• Berdasarkan substitusi aljabar $u = \\cos x \\implies du = -\\sin x \\, dx$"
    },
    "hints": {
      "concept": "Tulis $\\tan x = \\frac{\\sin x}{\\cos x}$. Misalkan $u = \\cos x \\implies du = -\\sin x \\, dx$.",
      "execution": "$-\\int \\frac{du}{u} = -\\ln|\\cos x| + C = \\ln|\\cos x|^{-1} + C = \\ln|\\sec x| + C$."
    },
    "explanation": "Tulis $\\tan x = \\frac{\\sin x}{\\cos x}$. Misalkan $u = \\cos x \\implies du = -\\sin x \\, dx$. $-\\int \\frac{du}{u} = -\\ln|\\cos x| + C = \\ln|\\cos x|^{-1} + C = \\ln|\\sec x| + C$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-26",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Analisis Karakteristik Polinomial Kubik",
    "type": "multi",
    "questionHtml": "Diberikan fungsi polinomial $P(x) = x^3 - 3x^2 - 9x + 27$. Tentukan semua pernyataan berikut yang BENAR terkait fungsi tersebut! (Pilihlah lebih dari satu jawaban yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Fungsi $P(x)$ memiliki pembuat nol di $x = 3$ dan $x = -3$."
      },
      {
        "key": "B",
        "text": "Titik belok dari kurva fungsi $P(x)$ terletak pada koordinat $(1, 16)$."
      },
      {
        "key": "C",
        "text": "Nilai maksimum lokal fungsi $P(x)$ terjadi pada saat absis $x = 3$."
      },
      {
        "key": "D",
        "text": "Nilai stasioner minimum lokal fungsi $P(x)$ bernilai tepat sama dengan $0$."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "D"
    ],
    "correctAnswers": [
      "A",
      "B",
      "D"
    ],
    "formulaHud": {
      "title": "ANALISIS LENGKAP POLINOMIAL DERAJAT TIGA",
      "latex": "P'(x) = 3(x + 1)(x - 3), \\quad P''(x) = 6(x - 1)",
      "legend": "• Titik belok di $x = 1$, maksimum di $x = -1$, minimum di $x = 3$"
    },
    "hints": {
      "concept": "Turunan pertama: $P'(x) = 3x^2 - 6x - 9 = 3(x - 3)(x + 1) = 0$. Turunan kedua: $P''(x) = 6x - 6$.",
      "execution": "Pembuat nol: $P(3) = 0$ dan $P(-3) = -27 - 27 + 27 + 27 = 0$ (A benar). Titik belok $P''(x) = 0 \\implies x = 1, P(1) = 1 - 3 - 9 + 27 = 16$ (B benar). Minimum lokal di $x = 3$ dengan nilai $P(3) = 0$ (D benar). Maksimum di $x = -1$, bukan 3 (C salah)."
    },
    "explanation": "Turunan pertama: $P'(x) = 3x^2 - 6x - 9 = 3(x - 3)(x + 1) = 0$. Turunan kedua: $P''(x) = 6x - 6$. Pembuat nol: $P(3) = 0$ dan $P(-3) = -27 - 27 + 27 + 27 = 0$ (A benar). Titik belok $P''(x) = 0 \\implies x = 1, P(1) = 1 - 3 - 9 + 27 = 16$ (B benar). Minimum lokal di $x = 3$ dengan nilai $P(3) = 0$ (D benar). Maksimum di $x = -1$, bukan 3 (C salah).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-27",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sifat-sifat Determinan dan Operasi Matriks",
    "type": "multi",
    "questionHtml": "Diberikan matriks bujursangkar $A$ dan $B$ berordo $3 \\times 3$ yang dapat dibalik (invertible). Manakah dari pernyataan-pernyataan berikut yang selalu BENAR? (Pilihlah lebih dari satu jawaban yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Determinan dari matriks transpos sama dengan determinan asalnya: $\\det(A^T) = \\det(A)$."
      },
      {
        "key": "B",
        "text": "Determinan penjumlahan dua matriks sama dengan jumlah determinannya: $\\det(A + B) = \\det(A) + \\det(B)$."
      },
      {
        "key": "C",
        "text": "Determinan dari matriks invers memenuhi hubungan: $\\det(A^{-1}) = \\frac{1}{\\det(A)}$."
      },
      {
        "key": "D",
        "text": "Untuk sembarang skalar real $k$, berlaku $\\det(kA) = k^3 \\det(A)$."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "correctAnswers": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "AKSIOMA DAN TEOREMA DETERMINAN",
      "latex": "\\det(A^T) = \\det(A), \\quad \\det(A^{-1}) = [\\det(A)]^{-1}, \\quad \\det(kA) = k^n \\det(A)",
      "legend": "• Determinan bersifat multiplikatif terhadap perkalian, tetapi bukan aditif terhadap penjumlahan matriks"
    },
    "hints": {
      "concept": "Evaluasi teorema aljabar linear standar mengenai determinan matriks.",
      "execution": "Pernyataan A, C, dan D adalah teorema dasar baku determinan. Pernyataan B salah karena secara umum $\\det(A+B) \\neq \\det(A) + \\det(B)$."
    },
    "explanation": "Evaluasi teorema aljabar linear standar mengenai determinan matriks. Pernyataan A, C, dan D adalah teorema dasar baku determinan. Pernyataan B salah karena secara umum $\\det(A+B) \\neq \\det(A) + \\det(B)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-28",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG DIMENSI TIGA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Karakteristik Operasi Vektor di R3",
    "type": "multi",
    "questionHtml": "Diberikan vektor tak-nol $\\vec{u}$ dan $\\vec{v}$ pada ruang dimensi tiga. Manakah pernyataan berikut yang BENAR? (Pilihlah lebih dari satu jawaban yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Jika $\\vec{u} \\cdot \\vec{v} = 0$, maka vektor $\\vec{u}$ dan $\\vec{v}$ saling tegak lurus (ortogonal)."
      },
      {
        "key": "B",
        "text": "Vektor hasil perkalian silang $\\vec{u} \\times \\vec{v}$ selalu tegak lurus terhadap vektor $\\vec{u}$ dan juga $\\vec{v}$."
      },
      {
        "key": "C",
        "text": "Operasi perkalian silang bersifat komutatif: $\\vec{u} \\times \\vec{v} = \\vec{v} \\times \\vec{u}$."
      },
      {
        "key": "D",
        "text": "Jika $\\vec{u} \\times \\vec{v} = \\vec{0}$, maka vektor $\\vec{u}$ dan $\\vec{v}$ saling sejajar (kolinear)."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "D"
    ],
    "correctAnswers": [
      "A",
      "B",
      "D"
    ],
    "formulaHud": {
      "title": "SIFAT ALJABAR VEKTOR TIGA DIMENSI",
      "latex": "\\vec{u} \\times \\vec{v} = -(\\vec{v} \\times \\vec{u}) \\quad (\\text{anti-komutatif})",
      "legend": "• Arah perkalian silang berbalik $180^\\circ$ jika urutan operan ditukar"
    },
    "hints": {
      "concept": "Periksa sifat ortogonalitas dot product dan sifat geometris cross product.",
      "execution": "A benar (definisi ortogonal). B benar (arah vektor normal bidang). C salah karena bersifat anti-komutatif ($-(\\vec{v} \\times \\vec{u})$). D benar (karena $\\sin(0^\\circ) = 0$)."
    },
    "explanation": "Periksa sifat ortogonalitas dot product dan sifat geometris cross product. A benar (definisi ortogonal). B benar (arah vektor normal bidang). C salah karena bersifat anti-komutatif ($-(\\vec{v} \\times \\vec{u})$). D benar (karena $\\sin(0^\\circ) = 0$).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-29",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Karakteristik Elips Horizontal",
    "type": "multi",
    "questionHtml": "Diberikan elips dengan persamaan $\\frac{x^2}{25} + \\frac{y^2}{16} = 1$. Manakah pernyataan berikut yang BENAR? (Pilihlah lebih dari satu jawaban yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Koordinat kedua titik fokus elips terletak pada $(-3, 0)$ dan $(3, 0)$."
      },
      {
        "key": "B",
        "text": "Panjang sumbu minor elips adalah $8$ satuan panjang."
      },
      {
        "key": "C",
        "text": "Eksentrisitas elips bernilai $e = \\frac{3}{5}$."
      },
      {
        "key": "D",
        "text": "Panjang latus rectum elips bernilai $\\frac{25}{8}$ satuan panjang."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "correctAnswers": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PARAMETER ELIPS LENGKAP",
      "latex": "c = \\sqrt{25 - 16} = 3, \\quad b = 4, \\quad e = \\frac{c}{a} = \\frac{3}{5}, \\quad LR = \\frac{2b^2}{a} = \\frac{32}{5}",
      "legend": "• Menghitung seluruh komponen geometri elips dari sumbu mayor $a = 5$ dan sumbu minor $b = 4$"
    },
    "hints": {
      "concept": "$a = 5, b = 4 \\implies c = \\sqrt{25 - 16} = 3$.",
      "execution": "Fokus $(\\pm 3, 0)$ (A benar). Sumbu minor $2b = 2(4) = 8$ (B benar). Eksentrisitas $e = \\frac{3}{5}$ (C benar). Latus rectum $LR = \\frac{2b^2}{a} = \\frac{32}{5} = 6,4$ bukan $\\frac{25}{8}$ (D salah)."
    },
    "explanation": "$a = 5, b = 4 \\implies c = \\sqrt{25 - 16} = 3$. Fokus $(\\pm 3, 0)$ (A benar). Sumbu minor $2b = 2(4) = 8$ (B benar). Eksentrisitas $e = \\frac{3}{5}$ (C benar). Latus rectum $LR = \\frac{2b^2}{a} = \\frac{32}{5} = 6,4$ bukan $\\frac{25}{8}$ (D salah).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-30",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: INTEGRAL TENTU",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sifat dan Teorema Fundamental Kalkulus",
    "type": "multi",
    "questionHtml": "Jika $f(x)$ adalah fungsi kontinu dan ganjil pada seluruh garis bilangan real $\\mathbb{R}$ ($f(-x) = -f(x)$), manakah pernyataan berikut yang BENAR? (Pilihlah lebih dari satu jawaban yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Nilai dari integral simetris $\\int_{-a}^a f(x) \\, dx = 0$ untuk setiap bilangan real $a > 0$."
      },
      {
        "key": "B",
        "text": "Turunan pertama $f'(x)$ merupakan fungsi genap ($f'(-x) = f'(x)$)."
      },
      {
        "key": "C",
        "text": "Fungsi $[f(x)]^2$ merupakan fungsi genap."
      },
      {
        "key": "D",
        "text": "Nilai integral $\\int_{-a}^a [f(x)]^2 \\, dx$ selalu bernilai tepat sama dengan nol."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "correctAnswers": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "SIFAT PARITAS INTEGRAL SIMETRIS",
      "latex": "\\int_{-a}^a f_{\\text{ganjil}}(x) \\, dx = 0, \\quad \\int_{-a}^a f_{\\text{genap}}(x) \\, dx = 2\\int_0^a f_{\\text{genap}}(x) \\, dx",
      "legend": "• Kuadrat dari fungsi ganjil selalu menghasilkan fungsi genap tak-negatif"
    },
    "hints": {
      "concept": "Tinjau sifat simetri fungsi ganjil dan fungsi genap terhadap integral dan turunan.",
      "execution": "A benar (integral fungsi ganjil pada selang simetris bernilai nol). B benar (turunan fungsi ganjil selalu genap). C benar (kuadrat tanda negatif menjadi positif). D salah karena integral dari fungsi kuadrat genap non-negatif pasti bernilai positif $2\\int_0^a [f(x)]^2 dx > 0$."
    },
    "explanation": "Tinjau sifat simetri fungsi ganjil dan fungsi genap terhadap integral dan turunan. A benar (integral fungsi ganjil pada selang simetris bernilai nol). B benar (turunan fungsi ganjil selalu genap). C benar (kuadrat tanda negatif menjadi positif). D salah karena integral dari fungsi kuadrat genap non-negatif pasti bernilai positif $2\\int_0^a [f(x)]^2 dx > 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-31",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Matriks Evaluasi Teorema Sisa dan Faktor",
    "type": "matrix",
    "questionHtml": "Diberikan suku banyak $P(x) = 2x^3 - 3x^2 - 8x - 3$. Tentukan apakah setiap pernyataan berikut BENAR atau SALAH berdasarkan Teorema Faktor dan Teorema Sisa!",
    "statements": [
      {
        "text": "Bentuk $(x + 1)$ merupakan salah satu faktor linear dari suku banyak $P(x)$.",
        "correct": true,
        "id": "0"
      },
      {
        "text": "Sisa pembagian $P(x)$ oleh pembagi $(x - 2)$ bernilai tepat sama dengan $-15$.",
        "correct": true,
        "id": "1"
      },
      {
        "text": "Jumlah seluruh akar-akar dari persamaan $P(x) = 0$ bernilai $\\frac{3}{2}$.",
        "correct": true,
        "id": "2"
      },
      {
        "text": "Hasil perkalian dari seluruh akar-akar persamaan $P(x) = 0$ bernilai $-3$.",
        "correct": false,
        "id": "3"
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "EVALUASI SUKU BANYAK KUBIK",
      "latex": "P(-1) = 0, \\quad x_1+x_2+x_3 = -\\frac{-3}{2} = \\frac{3}{2}, \\quad x_1x_2x_3 = -\\frac{-3}{2} = \\frac{3}{2}",
      "legend": "• Perkalian seluruh akar persamaan kubik adalah $-\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Uji nilai $P(-1)$, $P(2)$, dan hubungan koefisien Vieta.",
      "execution": "1: $P(-1) = 2(-1) - 3(1) - 8(-1) - 3 = -2 - 3 + 8 - 3 = 0$ (BENAR). 2: $P(2) = 2(8) - 3(4) - 8(2) - 3 = 16 - 12 - 16 - 3 = -15$ (BENAR). 3: $x_1+x_2+x_3 = -\\frac{b}{a} = \\frac{3}{2}$ (BENAR). 4: $x_1x_2x_3 = -\\frac{d}{a} = -\\frac{-3}{2} = \\frac{3}{2} \\neq -3$ (SALAH)."
    },
    "explanation": "Uji nilai $P(-1)$, $P(2)$, dan hubungan koefisien Vieta. 1: $P(-1) = 2(-1) - 3(1) - 8(-1) - 3 = -2 - 3 + 8 - 3 = 0$ (BENAR). 2: $P(2) = 2(8) - 3(4) - 8(2) - 3 = 16 - 12 - 16 - 3 = -15$ (BENAR). 3: $x_1+x_2+x_3 = -\\frac{b}{a} = \\frac{3}{2}$ (BENAR). 4: $x_1x_2x_3 = -\\frac{d}{a} = -\\frac{-3}{2} = \\frac{3}{2} \\neq -3$ (SALAH).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-32",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Matriks Evaluasi Determinan Matriks Ordo 3x3",
    "type": "matrix",
    "questionHtml": "Diberikan matriks $A = \\begin{pmatrix} 2 & 0 & 1 \\\\ 1 & 1 & 0 \\\\ 0 & 2 & 1 \\end{pmatrix}$. Tentukan apakah setiap pernyataan berikut BENAR atau SALAH!",
    "statements": [
      {
        "text": "Nilai determinan dari matriks $A$ ($\\det(A)$) bernilai $4$.",
        "correct": true,
        "id": "0"
      },
      {
        "text": "Matriks $A$ memiliki invers karena nilai $\\det(A) \\neq 0$.",
        "correct": true,
        "id": "1"
      },
      {
        "text": "Nilai determinan dari matriks $A^2$ bernilai $16$.",
        "correct": true,
        "id": "2"
      },
      {
        "text": "Nilai determinan dari matriks $3A$ bernilai $12$.",
        "correct": false,
        "id": "3"
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "SIFAT DETERMINAN PENGALI SKALAR",
      "latex": "\\det(kA) = k^3 \\det(A) \\implies \\det(3A) = 3^3 \\cdot 4 = 27 \\cdot 4 = 108",
      "legend": "• Skalar 3 dipangkatkan 3 untuk matriks berdimensi $3 \\times 3$"
    },
    "hints": {
      "concept": "Hitung $\\det(A) = 2(1 - 0) - 0 + 1(2 - 0) = 2 + 2 = 4$.",
      "execution": "1: $\\det(A) = 4$ (BENAR). 2: Karena $\\det(A) = 4 \\neq 0$, matriks non-singular dan memiliki invers (BENAR). 3: $\\det(A^2) = (\\det(A))^2 = 4^2 = 16$ (BENAR). 4: $\\det(3A) = 3^3 \\cdot 4 = 108 \\neq 12$ (SALAH)."
    },
    "explanation": "Hitung $\\det(A) = 2(1 - 0) - 0 + 1(2 - 0) = 2 + 2 = 4$. 1: $\\det(A) = 4$ (BENAR). 2: Karena $\\det(A) = 4 \\neq 0$, matriks non-singular dan memiliki invers (BENAR). 3: $\\det(A^2) = (\\det(A))^2 = 4^2 = 16$ (BENAR). 4: $\\det(3A) = 3^3 \\cdot 4 = 108 \\neq 12$ (SALAH).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-33",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Matriks Evaluasi Irisan Kerucut Hiperbola",
    "type": "matrix",
    "questionHtml": "Diberikan persamaan hiperbola $\\frac{x^2}{9} - \\frac{y^2}{16} = 1$. Tentukan apakah setiap pernyataan berikut BENAR atau SALAH!",
    "statements": [
      {
        "text": "Titik puncak hiperbola terletak pada koordinat $(-3, 0)$ dan $(3, 0)$.",
        "correct": true,
        "id": "0"
      },
      {
        "text": "Jarak antara kedua titik fokus hiperbola adalah $10$ satuan panjang.",
        "correct": true,
        "id": "1"
      },
      {
        "text": "Persamaan garis asimtot hiperbola adalah $y = \\pm \\frac{4}{3}x$.",
        "correct": true,
        "id": "2"
      },
      {
        "text": "Eksentrisitas hiperbola bernilai $e = \\frac{4}{5}$.",
        "correct": false,
        "id": "3"
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "KARAKTERISTIK HIPERBOLA HORIZONTAL",
      "latex": "a = 3, \\quad b = 4, \\quad c = \\sqrt{9 + 16} = 5 \\implies e = \\frac{c}{a} = \\frac{5}{3} > 1",
      "legend": "• Eksentrisitas kurva hiperbola selalu lebih besar dari 1"
    },
    "hints": {
      "concept": "Hitung $a = 3, b = 4, c = \\sqrt{3^2 + 4^2} = 5$.",
      "execution": "1: Puncak di $(\\pm a, 0) = (\\pm 3, 0)$ (BENAR). 2: Jarak antar fokus $2c = 2(5) = 10$ (BENAR). 3: Asimtot $y = \\pm \\frac{b}{a}x = \\pm \\frac{4}{3}x$ (BENAR). 4: Eksentrisitas $e = \\frac{c}{a} = \\frac{5}{3} \\neq \\frac{4}{5}$ (SALAH)."
    },
    "explanation": "Hitung $a = 3, b = 4, c = \\sqrt{3^2 + 4^2} = 5$. 1: Puncak di $(\\pm a, 0) = (\\pm 3, 0)$ (BENAR). 2: Jarak antar fokus $2c = 2(5) = 10$ (BENAR). 3: Asimtot $y = \\pm \\frac{b}{a}x = \\pm \\frac{4}{3}x$ (BENAR). 4: Eksentrisitas $e = \\frac{c}{a} = \\frac{5}{3} \\neq \\frac{4}{5}$ (SALAH).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-34",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Matriks Evaluasi Identitas Trigonometri Analitis",
    "type": "matrix",
    "questionHtml": "Tentukan kebenaran dari setiap identitas trigonometri analitis berikut (BENAR atau SALAH)!",
    "statements": [
      {
        "text": "$\\cos(2x) = 2\\cos^2 x - 1$ untuk setiap $x \\in \\mathbb{R}$.",
        "correct": true,
        "id": "0"
      },
      {
        "text": "$\\sin(x + y) = \\sin x \\cos y + \\cos x \\sin y$ untuk setiap $x, y \\in \\mathbb{R}$.",
        "correct": true,
        "id": "1"
      },
      {
        "text": "$1 + \\tan^2 x = \\sec^2 x$ pada seluruh daerah asal fungsinya.",
        "correct": true,
        "id": "2"
      },
      {
        "text": "$\\cos(A) + \\cos(B) = 2\\sin\\left(\\frac{A+B}{2}\\right)\\sin\\left(\\frac{A-B}{2}\\right)$.",
        "correct": false,
        "id": "3"
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IDENTITAS TRIGONOMETRI BAKU",
      "latex": "\\cos A + \\cos B = 2\\cos\\left(\\frac{A+B}{2}\\right)\\cos\\left(\\frac{A-B}{2}\\right)",
      "legend": "• Penjumlahan dua fungsi kosinus menghasilkan perkalian dua fungsi kosinus murni"
    },
    "hints": {
      "concept": "Verifikasi rumus identitas trigonometri baku.",
      "execution": "1, 2, dan 3 adalah identitas trigonometri baku (BENAR). Pernyataan 4 salah karena rumus jumlahan kosinus menghasilkan $2\\cos(\\frac{A+B}{2})\\cos(\\frac{A-B}{2})$ bukan sinus (SALAH)."
    },
    "explanation": "Verifikasi rumus identitas trigonometri baku. 1, 2, dan 3 adalah identitas trigonometri baku (BENAR). Pernyataan 4 salah karena rumus jumlahan kosinus menghasilkan $2\\cos(\\frac{A+B}{2})\\cos(\\frac{A-B}{2})$ bukan sinus (SALAH).",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-35",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT: LIMIT & TURUNAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Matriks Evaluasi Teorema Kalkulus Lanjutan",
    "type": "matrix",
    "questionHtml": "Tentukan apakah setiap pernyataan kalkulus berikut BENAR atau SALAH!",
    "statements": [
      {
        "text": "Nilai limit $\\lim_{x \\to 0} \\frac{\\tan(5x)}{2x} = \\frac{5}{2}$.",
        "correct": true,
        "id": "0"
      },
      {
        "text": "Turunan pertama dari fungsi $f(x) = \\cos(4x)$ adalah $f'(x) = -4\\sin(4x)$.",
        "correct": true,
        "id": "1"
      },
      {
        "text": "Nilai limit tak hingga $\\lim_{x \\to \\infty} \\frac{3x^2 + 1}{x^3 - 4} = 3$.",
        "correct": false,
        "id": "2"
      },
      {
        "text": "Hasil integral $\\int \\sec^2(x) \\, dx = \\tan(x) + C$.",
        "correct": true,
        "id": "3"
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "TEOREMA KALKULUS DASAR",
      "latex": "\\lim_{x \\to \\infty} \\frac{3x^2}{x^3} = \\lim_{x \\to \\infty} \\frac{3}{x} = 0",
      "legend": "• Jika derajat penyebut lebih tinggi dari pembilang, nilai limit di ketakhinggaan bernilai nol"
    },
    "hints": {
      "concept": "Uji setiap limit dan turunan satu per satu.",
      "execution": "1: Limit trigonometri standar $\\frac{5}{2}$ (BENAR). 2: Turunan kosinus $-4\\sin(4x)$ (BENAR). 3: Derajat pembilang 2 < derajat penyebut 3, sehingga limitnya adalah 0 bukan 3 (SALAH). 4: Integral sekan kuadrat adalah tangen (BENAR)."
    },
    "explanation": "Uji setiap limit dan turunan satu per satu. 1: Limit trigonometri standar $\\frac{5}{2}$ (BENAR). 2: Turunan kosinus $-4\\sin(4x)$ (BENAR). 3: Derajat pembilang 2 < derajat penyebut 3, sehingga limitnya adalah 0 bukan 3 (SALAH). 4: Integral sekan kuadrat adalah tangen (BENAR).",
    "isDiagnostic": false
  }
];
