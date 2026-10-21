/**
 * TKA MASTERY HUB — QUESTIONS_MTK_LANJUT.JS (135 SOAL AUTENTIK)
 */
window.TKA_MTK_LANJUT_QUESTIONS = [
  {
    "id": "mtk_lanjut-lat-e-01",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(5x)}{5x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{25}{10}$"
      },
      {
        "key": "B",
        "text": "$\\frac{27}{10}$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{5}$"
      },
      {
        "key": "D",
        "text": "$\\frac{25}{14}$"
      },
      {
        "key": "E",
        "text": "$\\frac{25}{5}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{5}$ lalu hitung limit standar $\\frac{5^2}{2} = \\frac{25}{10}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(5x)}{5x^2} = \\frac{1}{5} \\cdot \\frac{5^2}{2} = \\frac{25}{10}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-02",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(6x)}{7x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{36}{14}$"
      },
      {
        "key": "B",
        "text": "$\\frac{38}{14}$"
      },
      {
        "key": "C",
        "text": "$\\frac{6}{7}$"
      },
      {
        "key": "D",
        "text": "$\\frac{36}{18}$"
      },
      {
        "key": "E",
        "text": "$\\frac{36}{7}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{7}$ lalu hitung limit standar $\\frac{6^2}{2} = \\frac{36}{14}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(6x)}{7x^2} = \\frac{1}{7} \\cdot \\frac{6^2}{2} = \\frac{36}{14}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-03",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 4 & 0 & 2 \\\\ 1 & 3 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-0.5$"
      },
      {
        "key": "B",
        "text": "$1.0$"
      },
      {
        "key": "C",
        "text": "$2.2$"
      },
      {
        "key": "D",
        "text": "$3.0$"
      },
      {
        "key": "E",
        "text": "$4.5$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 1.0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-04",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 5 & 0 & 2 \\\\ 1 & 4 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-0.65$"
      },
      {
        "key": "B",
        "text": "$0.85$"
      },
      {
        "key": "C",
        "text": "$2.05$"
      },
      {
        "key": "D",
        "text": "$2.85$"
      },
      {
        "key": "E",
        "text": "$4.35$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.85$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-05",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{52} + \\frac{y^2}{32} = 1$ yang sejajar dengan garis linear $y = 2x + 5$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 15.5$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 18.7$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 15.5$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 15.5$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 31.0$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 15.5$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-06",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{60} + \\frac{y^2}{38} = 1$ yang sejajar dengan garis linear $y = 2x + 6$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 16.7$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 19.9$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 16.7$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 16.7$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 33.4$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 16.7$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-07",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-08",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-09",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (21, -2, 13)$ dan $\\vec{v} = (2, 9, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6$"
      },
      {
        "key": "B",
        "text": "$9$"
      },
      {
        "key": "C",
        "text": "$11$"
      },
      {
        "key": "D",
        "text": "$15$"
      },
      {
        "key": "E",
        "text": "$20$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 42 + (-18) + (-13) = 11."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (21)(2) + (-2)(9) + (13)(-1) = 42 - 18 - 13 = 11$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-10",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(14x)}{23x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{196}{46}$"
      },
      {
        "key": "B",
        "text": "$\\frac{198}{46}$"
      },
      {
        "key": "C",
        "text": "$\\frac{14}{23}$"
      },
      {
        "key": "D",
        "text": "$\\frac{196}{50}$"
      },
      {
        "key": "E",
        "text": "$\\frac{196}{23}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{23}$ lalu hitung limit standar $\\frac{14^2}{2} = \\frac{196}{46}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(14x)}{23x^2} = \\frac{1}{23} \\cdot \\frac{14^2}{2} = \\frac{196}{46}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-11",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(15x)}{25x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{225}{50}$"
      },
      {
        "key": "B",
        "text": "$\\frac{227}{50}$"
      },
      {
        "key": "C",
        "text": "$\\frac{15}{25}$"
      },
      {
        "key": "D",
        "text": "$\\frac{225}{54}$"
      },
      {
        "key": "E",
        "text": "$\\frac{225}{25}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{25}$ lalu hitung limit standar $\\frac{15^2}{2} = \\frac{225}{50}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(15x)}{25x^2} = \\frac{1}{25} \\cdot \\frac{15^2}{2} = \\frac{225}{50}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-12",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Integral Substitusi Parsial & Luas Daerah Tertutup",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(16x)}{27x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{256}{54}$"
      },
      {
        "key": "B",
        "text": "$\\frac{258}{54}$"
      },
      {
        "key": "C",
        "text": "$\\frac{16}{27}$"
      },
      {
        "key": "D",
        "text": "$\\frac{256}{58}$"
      },
      {
        "key": "E",
        "text": "$\\frac{256}{27}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "INTEGRAL PARSIAL",
      "latex": "\\int u \\, dv = uv - \\int v \\, du",
      "legend": "• Pilihlah $u$ menurut kaidah LIATE<br>• Luas antara kurva $L = \\int_a^b (y_\\\\atas}} - y_\\\\bawah}}) \\, dx$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{27}$ lalu hitung limit standar $\\frac{16^2}{2} = \\frac{256}{54}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(16x)}{27x^2} = \\frac{1}{27} \\cdot \\frac{16^2}{2} = \\frac{256}{54}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-13",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(17x)}{29x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{289}{58}$"
      },
      {
        "key": "B",
        "text": "$\\frac{291}{58}$"
      },
      {
        "key": "C",
        "text": "$\\frac{17}{29}$"
      },
      {
        "key": "D",
        "text": "$\\frac{289}{62}$"
      },
      {
        "key": "E",
        "text": "$\\frac{289}{29}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{29}$ lalu hitung limit standar $\\frac{17^2}{2} = \\frac{289}{58}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(17x)}{29x^2} = \\frac{1}{29} \\cdot \\frac{17^2}{2} = \\frac{289}{58}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-14",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(18x)}{31x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{324}{62}$"
      },
      {
        "key": "B",
        "text": "$\\frac{326}{62}$"
      },
      {
        "key": "C",
        "text": "$\\frac{18}{31}$"
      },
      {
        "key": "D",
        "text": "$\\frac{324}{66}$"
      },
      {
        "key": "E",
        "text": "$\\frac{324}{31}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{31}$ lalu hitung limit standar $\\frac{18^2}{2} = \\frac{324}{62}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(18x)}{31x^2} = \\frac{1}{31} \\cdot \\frac{18^2}{2} = \\frac{324}{62}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-15",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 16 & 0 & 2 \\\\ 1 & 15 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.2$"
      },
      {
        "key": "B",
        "text": "$0.3$"
      },
      {
        "key": "C",
        "text": "$1.5$"
      },
      {
        "key": "D",
        "text": "$2.3$"
      },
      {
        "key": "E",
        "text": "$3.8$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.3$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-16",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 17 & 0 & 2 \\\\ 1 & 16 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.22$"
      },
      {
        "key": "B",
        "text": "$0.28$"
      },
      {
        "key": "C",
        "text": "$1.48$"
      },
      {
        "key": "D",
        "text": "$2.2800000000000002$"
      },
      {
        "key": "E",
        "text": "$3.7800000000000002$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.28$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-17",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{148} + \\frac{y^2}{104} = 1$ yang sejajar dengan garis linear $y = 2x + 17$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 26.4$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 29.6$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 26.4$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 26.4$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 52.8$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 26.4$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-18",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{156} + \\frac{y^2}{110} = 1$ yang sejajar dengan garis linear $y = 2x + 18$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 27.1$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 30.3$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 27.1$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 27.1$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 54.2$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 27.1$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-19",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-20",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-21",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (45, -2, 25)$ dan $\\vec{v} = (2, 21, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18$"
      },
      {
        "key": "B",
        "text": "$21$"
      },
      {
        "key": "C",
        "text": "$23$"
      },
      {
        "key": "D",
        "text": "$27$"
      },
      {
        "key": "E",
        "text": "$32$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 90 + (-42) + (-25) = 23."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (45)(2) + (-2)(21) + (25)(-1) = 90 - 42 - 25 = 23$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-22",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(26x)}{47x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{676}{94}$"
      },
      {
        "key": "B",
        "text": "$\\frac{678}{94}$"
      },
      {
        "key": "C",
        "text": "$\\frac{26}{47}$"
      },
      {
        "key": "D",
        "text": "$\\frac{676}{98}$"
      },
      {
        "key": "E",
        "text": "$\\frac{676}{47}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{47}$ lalu hitung limit standar $\\frac{26^2}{2} = \\frac{676}{94}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(26x)}{47x^2} = \\frac{1}{47} \\cdot \\frac{26^2}{2} = \\frac{676}{94}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-23",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(27x)}{49x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{729}{98}$"
      },
      {
        "key": "B",
        "text": "$\\frac{731}{98}$"
      },
      {
        "key": "C",
        "text": "$\\frac{27}{49}$"
      },
      {
        "key": "D",
        "text": "$\\frac{729}{102}$"
      },
      {
        "key": "E",
        "text": "$\\frac{729}{49}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{49}$ lalu hitung limit standar $\\frac{27^2}{2} = \\frac{729}{98}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(27x)}{49x^2} = \\frac{1}{49} \\cdot \\frac{27^2}{2} = \\frac{729}{98}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-24",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Integral Substitusi Parsial & Luas Daerah Tertutup",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(28x)}{51x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{784}{102}$"
      },
      {
        "key": "B",
        "text": "$\\frac{786}{102}$"
      },
      {
        "key": "C",
        "text": "$\\frac{28}{51}$"
      },
      {
        "key": "D",
        "text": "$\\frac{784}{106}$"
      },
      {
        "key": "E",
        "text": "$\\frac{784}{51}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "INTEGRAL PARSIAL",
      "latex": "\\int u \\, dv = uv - \\int v \\, du",
      "legend": "• Pilihlah $u$ menurut kaidah LIATE<br>• Luas antara kurva $L = \\int_a^b (y_\\\\atas}} - y_\\\\bawah}}) \\, dx$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{51}$ lalu hitung limit standar $\\frac{28^2}{2} = \\frac{784}{102}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(28x)}{51x^2} = \\frac{1}{51} \\cdot \\frac{28^2}{2} = \\frac{784}{102}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-25",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(29x)}{53x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{841}{106}$"
      },
      {
        "key": "B",
        "text": "$\\frac{843}{106}$"
      },
      {
        "key": "C",
        "text": "$\\frac{29}{53}$"
      },
      {
        "key": "D",
        "text": "$\\frac{841}{110}$"
      },
      {
        "key": "E",
        "text": "$\\frac{841}{53}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{53}$ lalu hitung limit standar $\\frac{29^2}{2} = \\frac{841}{106}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(29x)}{53x^2} = \\frac{1}{53} \\cdot \\frac{29^2}{2} = \\frac{841}{106}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-26",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(30x)}{55x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{900}{110}$"
      },
      {
        "key": "B",
        "text": "$\\frac{902}{110}$"
      },
      {
        "key": "C",
        "text": "$\\frac{30}{55}$"
      },
      {
        "key": "D",
        "text": "$\\frac{900}{114}$"
      },
      {
        "key": "E",
        "text": "$\\frac{900}{55}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{55}$ lalu hitung limit standar $\\frac{30^2}{2} = \\frac{900}{110}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(30x)}{55x^2} = \\frac{1}{55} \\cdot \\frac{30^2}{2} = \\frac{900}{110}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-27",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 28 & 0 & 2 \\\\ 1 & 27 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.33$"
      },
      {
        "key": "B",
        "text": "$0.17$"
      },
      {
        "key": "C",
        "text": "$1.3699999999999999$"
      },
      {
        "key": "D",
        "text": "$2.17$"
      },
      {
        "key": "E",
        "text": "$3.67$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.17$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-28",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 29 & 0 & 2 \\\\ 1 & 28 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.33$"
      },
      {
        "key": "B",
        "text": "$0.17$"
      },
      {
        "key": "C",
        "text": "$1.3699999999999999$"
      },
      {
        "key": "D",
        "text": "$2.17$"
      },
      {
        "key": "E",
        "text": "$3.67$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.17$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-29",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{244} + \\frac{y^2}{176} = 1$ yang sejajar dengan garis linear $y = 2x + 29$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 33.9$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 37.1$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 33.9$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 33.9$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 67.8$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 33.9$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-30",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{252} + \\frac{y^2}{182} = 1$ yang sejajar dengan garis linear $y = 2x + 30$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 34.5$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 37.7$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 34.5$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 34.5$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 69.0$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 34.5$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-31",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-32",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-33",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (69, -2, 37)$ dan $\\vec{v} = (2, 33, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$30$"
      },
      {
        "key": "B",
        "text": "$33$"
      },
      {
        "key": "C",
        "text": "$35$"
      },
      {
        "key": "D",
        "text": "$39$"
      },
      {
        "key": "E",
        "text": "$44$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 138 + (-66) + (-37) = 35."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (69)(2) + (-2)(33) + (37)(-1) = 138 - 66 - 37 = 35$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-34",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(38x)}{71x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1444}{142}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1446}{142}$"
      },
      {
        "key": "C",
        "text": "$\\frac{38}{71}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1444}{146}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1444}{71}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{71}$ lalu hitung limit standar $\\frac{38^2}{2} = \\frac{1444}{142}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(38x)}{71x^2} = \\frac{1}{71} \\cdot \\frac{38^2}{2} = \\frac{1444}{142}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-e-35",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(39x)}{73x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1521}{146}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1523}{146}$"
      },
      {
        "key": "C",
        "text": "$\\frac{39}{73}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1521}{150}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1521}{73}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{73}$ lalu hitung limit standar $\\frac{39^2}{2} = \\frac{1521}{146}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(39x)}{73x^2} = \\frac{1}{73} \\cdot \\frac{39^2}{2} = \\frac{1521}{146}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-01",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(5x)}{5x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{25}{10}$"
      },
      {
        "key": "B",
        "text": "$\\frac{27}{10}$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{5}$"
      },
      {
        "key": "D",
        "text": "$\\frac{25}{14}$"
      },
      {
        "key": "E",
        "text": "$\\frac{25}{5}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{5}$ lalu hitung limit standar $\\frac{5^2}{2} = \\frac{25}{10}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(5x)}{5x^2} = \\frac{1}{5} \\cdot \\frac{5^2}{2} = \\frac{25}{10}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-02",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(6x)}{7x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{36}{14}$"
      },
      {
        "key": "B",
        "text": "$\\frac{38}{14}$"
      },
      {
        "key": "C",
        "text": "$\\frac{6}{7}$"
      },
      {
        "key": "D",
        "text": "$\\frac{36}{18}$"
      },
      {
        "key": "E",
        "text": "$\\frac{36}{7}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{7}$ lalu hitung limit standar $\\frac{6^2}{2} = \\frac{36}{14}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(6x)}{7x^2} = \\frac{1}{7} \\cdot \\frac{6^2}{2} = \\frac{36}{14}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-03",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 4 & 0 & 2 \\\\ 1 & 3 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-0.5$"
      },
      {
        "key": "B",
        "text": "$1.0$"
      },
      {
        "key": "C",
        "text": "$2.2$"
      },
      {
        "key": "D",
        "text": "$3.0$"
      },
      {
        "key": "E",
        "text": "$4.5$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 1.0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-04",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 5 & 0 & 2 \\\\ 1 & 4 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-0.65$"
      },
      {
        "key": "B",
        "text": "$0.85$"
      },
      {
        "key": "C",
        "text": "$2.05$"
      },
      {
        "key": "D",
        "text": "$2.85$"
      },
      {
        "key": "E",
        "text": "$4.35$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.85$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-05",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{52} + \\frac{y^2}{32} = 1$ yang sejajar dengan garis linear $y = 2x + 5$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 15.5$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 18.7$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 15.5$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 15.5$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 31.0$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 15.5$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-06",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{60} + \\frac{y^2}{38} = 1$ yang sejajar dengan garis linear $y = 2x + 6$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 16.7$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 19.9$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 16.7$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 16.7$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 33.4$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 16.7$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-07",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-08",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-09",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (21, -2, 13)$ dan $\\vec{v} = (2, 9, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6$"
      },
      {
        "key": "B",
        "text": "$9$"
      },
      {
        "key": "C",
        "text": "$11$"
      },
      {
        "key": "D",
        "text": "$15$"
      },
      {
        "key": "E",
        "text": "$20$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 42 + (-18) + (-13) = 11."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (21)(2) + (-2)(9) + (13)(-1) = 42 - 18 - 13 = 11$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-10",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(14x)}{23x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{196}{46}$"
      },
      {
        "key": "B",
        "text": "$\\frac{198}{46}$"
      },
      {
        "key": "C",
        "text": "$\\frac{14}{23}$"
      },
      {
        "key": "D",
        "text": "$\\frac{196}{50}$"
      },
      {
        "key": "E",
        "text": "$\\frac{196}{23}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{23}$ lalu hitung limit standar $\\frac{14^2}{2} = \\frac{196}{46}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(14x)}{23x^2} = \\frac{1}{23} \\cdot \\frac{14^2}{2} = \\frac{196}{46}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-11",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(15x)}{25x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{225}{50}$"
      },
      {
        "key": "B",
        "text": "$\\frac{227}{50}$"
      },
      {
        "key": "C",
        "text": "$\\frac{15}{25}$"
      },
      {
        "key": "D",
        "text": "$\\frac{225}{54}$"
      },
      {
        "key": "E",
        "text": "$\\frac{225}{25}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{25}$ lalu hitung limit standar $\\frac{15^2}{2} = \\frac{225}{50}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(15x)}{25x^2} = \\frac{1}{25} \\cdot \\frac{15^2}{2} = \\frac{225}{50}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-12",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Integral Substitusi Parsial & Luas Daerah Tertutup",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(16x)}{27x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{256}{54}$"
      },
      {
        "key": "B",
        "text": "$\\frac{258}{54}$"
      },
      {
        "key": "C",
        "text": "$\\frac{16}{27}$"
      },
      {
        "key": "D",
        "text": "$\\frac{256}{58}$"
      },
      {
        "key": "E",
        "text": "$\\frac{256}{27}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "INTEGRAL PARSIAL",
      "latex": "\\int u \\, dv = uv - \\int v \\, du",
      "legend": "• Pilihlah $u$ menurut kaidah LIATE<br>• Luas antara kurva $L = \\int_a^b (y_\\\\atas}} - y_\\\\bawah}}) \\, dx$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{27}$ lalu hitung limit standar $\\frac{16^2}{2} = \\frac{256}{54}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(16x)}{27x^2} = \\frac{1}{27} \\cdot \\frac{16^2}{2} = \\frac{256}{54}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-13",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(17x)}{29x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{289}{58}$"
      },
      {
        "key": "B",
        "text": "$\\frac{291}{58}$"
      },
      {
        "key": "C",
        "text": "$\\frac{17}{29}$"
      },
      {
        "key": "D",
        "text": "$\\frac{289}{62}$"
      },
      {
        "key": "E",
        "text": "$\\frac{289}{29}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{29}$ lalu hitung limit standar $\\frac{17^2}{2} = \\frac{289}{58}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(17x)}{29x^2} = \\frac{1}{29} \\cdot \\frac{17^2}{2} = \\frac{289}{58}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-14",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(18x)}{31x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{324}{62}$"
      },
      {
        "key": "B",
        "text": "$\\frac{326}{62}$"
      },
      {
        "key": "C",
        "text": "$\\frac{18}{31}$"
      },
      {
        "key": "D",
        "text": "$\\frac{324}{66}$"
      },
      {
        "key": "E",
        "text": "$\\frac{324}{31}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{31}$ lalu hitung limit standar $\\frac{18^2}{2} = \\frac{324}{62}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(18x)}{31x^2} = \\frac{1}{31} \\cdot \\frac{18^2}{2} = \\frac{324}{62}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-15",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 16 & 0 & 2 \\\\ 1 & 15 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.2$"
      },
      {
        "key": "B",
        "text": "$0.3$"
      },
      {
        "key": "C",
        "text": "$1.5$"
      },
      {
        "key": "D",
        "text": "$2.3$"
      },
      {
        "key": "E",
        "text": "$3.8$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.3$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-16",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 17 & 0 & 2 \\\\ 1 & 16 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.22$"
      },
      {
        "key": "B",
        "text": "$0.28$"
      },
      {
        "key": "C",
        "text": "$1.48$"
      },
      {
        "key": "D",
        "text": "$2.2800000000000002$"
      },
      {
        "key": "E",
        "text": "$3.7800000000000002$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.28$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-17",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{148} + \\frac{y^2}{104} = 1$ yang sejajar dengan garis linear $y = 2x + 17$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 26.4$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 29.6$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 26.4$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 26.4$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 52.8$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 26.4$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-18",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{156} + \\frac{y^2}{110} = 1$ yang sejajar dengan garis linear $y = 2x + 18$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 27.1$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 30.3$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 27.1$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 27.1$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 54.2$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 27.1$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-19",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-20",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-21",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (45, -2, 25)$ dan $\\vec{v} = (2, 21, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18$"
      },
      {
        "key": "B",
        "text": "$21$"
      },
      {
        "key": "C",
        "text": "$23$"
      },
      {
        "key": "D",
        "text": "$27$"
      },
      {
        "key": "E",
        "text": "$32$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 90 + (-42) + (-25) = 23."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (45)(2) + (-2)(21) + (25)(-1) = 90 - 42 - 25 = 23$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-22",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(26x)}{47x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{676}{94}$"
      },
      {
        "key": "B",
        "text": "$\\frac{678}{94}$"
      },
      {
        "key": "C",
        "text": "$\\frac{26}{47}$"
      },
      {
        "key": "D",
        "text": "$\\frac{676}{98}$"
      },
      {
        "key": "E",
        "text": "$\\frac{676}{47}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{47}$ lalu hitung limit standar $\\frac{26^2}{2} = \\frac{676}{94}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(26x)}{47x^2} = \\frac{1}{47} \\cdot \\frac{26^2}{2} = \\frac{676}{94}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-23",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(27x)}{49x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{729}{98}$"
      },
      {
        "key": "B",
        "text": "$\\frac{731}{98}$"
      },
      {
        "key": "C",
        "text": "$\\frac{27}{49}$"
      },
      {
        "key": "D",
        "text": "$\\frac{729}{102}$"
      },
      {
        "key": "E",
        "text": "$\\frac{729}{49}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{49}$ lalu hitung limit standar $\\frac{27^2}{2} = \\frac{729}{98}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(27x)}{49x^2} = \\frac{1}{49} \\cdot \\frac{27^2}{2} = \\frac{729}{98}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-24",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Integral Substitusi Parsial & Luas Daerah Tertutup",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(28x)}{51x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{784}{102}$"
      },
      {
        "key": "B",
        "text": "$\\frac{786}{102}$"
      },
      {
        "key": "C",
        "text": "$\\frac{28}{51}$"
      },
      {
        "key": "D",
        "text": "$\\frac{784}{106}$"
      },
      {
        "key": "E",
        "text": "$\\frac{784}{51}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "INTEGRAL PARSIAL",
      "latex": "\\int u \\, dv = uv - \\int v \\, du",
      "legend": "• Pilihlah $u$ menurut kaidah LIATE<br>• Luas antara kurva $L = \\int_a^b (y_\\\\atas}} - y_\\\\bawah}}) \\, dx$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{51}$ lalu hitung limit standar $\\frac{28^2}{2} = \\frac{784}{102}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(28x)}{51x^2} = \\frac{1}{51} \\cdot \\frac{28^2}{2} = \\frac{784}{102}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-25",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(29x)}{53x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{841}{106}$"
      },
      {
        "key": "B",
        "text": "$\\frac{843}{106}$"
      },
      {
        "key": "C",
        "text": "$\\frac{29}{53}$"
      },
      {
        "key": "D",
        "text": "$\\frac{841}{110}$"
      },
      {
        "key": "E",
        "text": "$\\frac{841}{53}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{53}$ lalu hitung limit standar $\\frac{29^2}{2} = \\frac{841}{106}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(29x)}{53x^2} = \\frac{1}{53} \\cdot \\frac{29^2}{2} = \\frac{841}{106}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-26",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(30x)}{55x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{900}{110}$"
      },
      {
        "key": "B",
        "text": "$\\frac{902}{110}$"
      },
      {
        "key": "C",
        "text": "$\\frac{30}{55}$"
      },
      {
        "key": "D",
        "text": "$\\frac{900}{114}$"
      },
      {
        "key": "E",
        "text": "$\\frac{900}{55}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{55}$ lalu hitung limit standar $\\frac{30^2}{2} = \\frac{900}{110}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(30x)}{55x^2} = \\frac{1}{55} \\cdot \\frac{30^2}{2} = \\frac{900}{110}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-27",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 28 & 0 & 2 \\\\ 1 & 27 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.33$"
      },
      {
        "key": "B",
        "text": "$0.17$"
      },
      {
        "key": "C",
        "text": "$1.3699999999999999$"
      },
      {
        "key": "D",
        "text": "$2.17$"
      },
      {
        "key": "E",
        "text": "$3.67$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.17$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-28",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 29 & 0 & 2 \\\\ 1 & 28 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.33$"
      },
      {
        "key": "B",
        "text": "$0.17$"
      },
      {
        "key": "C",
        "text": "$1.3699999999999999$"
      },
      {
        "key": "D",
        "text": "$2.17$"
      },
      {
        "key": "E",
        "text": "$3.67$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.17$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-29",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{244} + \\frac{y^2}{176} = 1$ yang sejajar dengan garis linear $y = 2x + 29$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 33.9$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 37.1$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 33.9$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 33.9$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 67.8$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 33.9$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-30",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{252} + \\frac{y^2}{182} = 1$ yang sejajar dengan garis linear $y = 2x + 30$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 34.5$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 37.7$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 34.5$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 34.5$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 69.0$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 34.5$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-31",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-32",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-33",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (69, -2, 37)$ dan $\\vec{v} = (2, 33, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$30$"
      },
      {
        "key": "B",
        "text": "$33$"
      },
      {
        "key": "C",
        "text": "$35$"
      },
      {
        "key": "D",
        "text": "$39$"
      },
      {
        "key": "E",
        "text": "$44$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 138 + (-66) + (-37) = 35."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (69)(2) + (-2)(33) + (37)(-1) = 138 - 66 - 37 = 35$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-34",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(38x)}{71x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1444}{142}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1446}{142}$"
      },
      {
        "key": "C",
        "text": "$\\frac{38}{71}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1444}{146}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1444}{71}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{71}$ lalu hitung limit standar $\\frac{38^2}{2} = \\frac{1444}{142}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(38x)}{71x^2} = \\frac{1}{71} \\cdot \\frac{38^2}{2} = \\frac{1444}{142}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-m-35",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(39x)}{73x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1521}{146}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1523}{146}$"
      },
      {
        "key": "C",
        "text": "$\\frac{39}{73}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1521}{150}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1521}{73}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{73}$ lalu hitung limit standar $\\frac{39^2}{2} = \\frac{1521}{146}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(39x)}{73x^2} = \\frac{1}{73} \\cdot \\frac{39^2}{2} = \\frac{1521}{146}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-01",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(5x)}{5x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{25}{10}$"
      },
      {
        "key": "B",
        "text": "$\\frac{27}{10}$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{5}$"
      },
      {
        "key": "D",
        "text": "$\\frac{25}{14}$"
      },
      {
        "key": "E",
        "text": "$\\frac{25}{5}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{5}$ lalu hitung limit standar $\\frac{5^2}{2} = \\frac{25}{10}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(5x)}{5x^2} = \\frac{1}{5} \\cdot \\frac{5^2}{2} = \\frac{25}{10}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-02",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(6x)}{7x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{36}{14}$"
      },
      {
        "key": "B",
        "text": "$\\frac{38}{14}$"
      },
      {
        "key": "C",
        "text": "$\\frac{6}{7}$"
      },
      {
        "key": "D",
        "text": "$\\frac{36}{18}$"
      },
      {
        "key": "E",
        "text": "$\\frac{36}{7}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{7}$ lalu hitung limit standar $\\frac{6^2}{2} = \\frac{36}{14}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(6x)}{7x^2} = \\frac{1}{7} \\cdot \\frac{6^2}{2} = \\frac{36}{14}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-03",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 4 & 0 & 2 \\\\ 1 & 3 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-0.5$"
      },
      {
        "key": "B",
        "text": "$1.0$"
      },
      {
        "key": "C",
        "text": "$2.2$"
      },
      {
        "key": "D",
        "text": "$3.0$"
      },
      {
        "key": "E",
        "text": "$4.5$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 1.0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-04",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 5 & 0 & 2 \\\\ 1 & 4 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-0.65$"
      },
      {
        "key": "B",
        "text": "$0.85$"
      },
      {
        "key": "C",
        "text": "$2.05$"
      },
      {
        "key": "D",
        "text": "$2.85$"
      },
      {
        "key": "E",
        "text": "$4.35$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.85$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-05",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{52} + \\frac{y^2}{32} = 1$ yang sejajar dengan garis linear $y = 2x + 5$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 15.5$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 18.7$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 15.5$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 15.5$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 31.0$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 15.5$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-06",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{60} + \\frac{y^2}{38} = 1$ yang sejajar dengan garis linear $y = 2x + 6$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 16.7$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 19.9$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 16.7$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 16.7$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 33.4$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 16.7$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-07",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-08",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-09",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (21, -2, 13)$ dan $\\vec{v} = (2, 9, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6$"
      },
      {
        "key": "B",
        "text": "$9$"
      },
      {
        "key": "C",
        "text": "$11$"
      },
      {
        "key": "D",
        "text": "$15$"
      },
      {
        "key": "E",
        "text": "$20$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 42 + (-18) + (-13) = 11."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (21)(2) + (-2)(9) + (13)(-1) = 42 - 18 - 13 = 11$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-10",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(14x)}{23x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{196}{46}$"
      },
      {
        "key": "B",
        "text": "$\\frac{198}{46}$"
      },
      {
        "key": "C",
        "text": "$\\frac{14}{23}$"
      },
      {
        "key": "D",
        "text": "$\\frac{196}{50}$"
      },
      {
        "key": "E",
        "text": "$\\frac{196}{23}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{23}$ lalu hitung limit standar $\\frac{14^2}{2} = \\frac{196}{46}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(14x)}{23x^2} = \\frac{1}{23} \\cdot \\frac{14^2}{2} = \\frac{196}{46}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-11",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(15x)}{25x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{225}{50}$"
      },
      {
        "key": "B",
        "text": "$\\frac{227}{50}$"
      },
      {
        "key": "C",
        "text": "$\\frac{15}{25}$"
      },
      {
        "key": "D",
        "text": "$\\frac{225}{54}$"
      },
      {
        "key": "E",
        "text": "$\\frac{225}{25}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{25}$ lalu hitung limit standar $\\frac{15^2}{2} = \\frac{225}{50}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(15x)}{25x^2} = \\frac{1}{25} \\cdot \\frac{15^2}{2} = \\frac{225}{50}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-12",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Integral Substitusi Parsial & Luas Daerah Tertutup",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(16x)}{27x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{256}{54}$"
      },
      {
        "key": "B",
        "text": "$\\frac{258}{54}$"
      },
      {
        "key": "C",
        "text": "$\\frac{16}{27}$"
      },
      {
        "key": "D",
        "text": "$\\frac{256}{58}$"
      },
      {
        "key": "E",
        "text": "$\\frac{256}{27}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "INTEGRAL PARSIAL",
      "latex": "\\int u \\, dv = uv - \\int v \\, du",
      "legend": "• Pilihlah $u$ menurut kaidah LIATE<br>• Luas antara kurva $L = \\int_a^b (y_\\\\atas}} - y_\\\\bawah}}) \\, dx$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{27}$ lalu hitung limit standar $\\frac{16^2}{2} = \\frac{256}{54}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(16x)}{27x^2} = \\frac{1}{27} \\cdot \\frac{16^2}{2} = \\frac{256}{54}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-13",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(17x)}{29x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{289}{58}$"
      },
      {
        "key": "B",
        "text": "$\\frac{291}{58}$"
      },
      {
        "key": "C",
        "text": "$\\frac{17}{29}$"
      },
      {
        "key": "D",
        "text": "$\\frac{289}{62}$"
      },
      {
        "key": "E",
        "text": "$\\frac{289}{29}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{29}$ lalu hitung limit standar $\\frac{17^2}{2} = \\frac{289}{58}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(17x)}{29x^2} = \\frac{1}{29} \\cdot \\frac{17^2}{2} = \\frac{289}{58}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-14",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(18x)}{31x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{324}{62}$"
      },
      {
        "key": "B",
        "text": "$\\frac{326}{62}$"
      },
      {
        "key": "C",
        "text": "$\\frac{18}{31}$"
      },
      {
        "key": "D",
        "text": "$\\frac{324}{66}$"
      },
      {
        "key": "E",
        "text": "$\\frac{324}{31}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{31}$ lalu hitung limit standar $\\frac{18^2}{2} = \\frac{324}{62}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(18x)}{31x^2} = \\frac{1}{31} \\cdot \\frac{18^2}{2} = \\frac{324}{62}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-15",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 16 & 0 & 2 \\\\ 1 & 15 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.2$"
      },
      {
        "key": "B",
        "text": "$0.3$"
      },
      {
        "key": "C",
        "text": "$1.5$"
      },
      {
        "key": "D",
        "text": "$2.3$"
      },
      {
        "key": "E",
        "text": "$3.8$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.3$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-16",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 17 & 0 & 2 \\\\ 1 & 16 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.22$"
      },
      {
        "key": "B",
        "text": "$0.28$"
      },
      {
        "key": "C",
        "text": "$1.48$"
      },
      {
        "key": "D",
        "text": "$2.2800000000000002$"
      },
      {
        "key": "E",
        "text": "$3.7800000000000002$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.28$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-17",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{148} + \\frac{y^2}{104} = 1$ yang sejajar dengan garis linear $y = 2x + 17$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 26.4$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 29.6$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 26.4$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 26.4$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 52.8$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 26.4$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-18",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{156} + \\frac{y^2}{110} = 1$ yang sejajar dengan garis linear $y = 2x + 18$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 27.1$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 30.3$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 27.1$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 27.1$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 54.2$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 27.1$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-19",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-20",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-21",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (45, -2, 25)$ dan $\\vec{v} = (2, 21, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18$"
      },
      {
        "key": "B",
        "text": "$21$"
      },
      {
        "key": "C",
        "text": "$23$"
      },
      {
        "key": "D",
        "text": "$27$"
      },
      {
        "key": "E",
        "text": "$32$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 90 + (-42) + (-25) = 23."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (45)(2) + (-2)(21) + (25)(-1) = 90 - 42 - 25 = 23$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-22",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(26x)}{47x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{676}{94}$"
      },
      {
        "key": "B",
        "text": "$\\frac{678}{94}$"
      },
      {
        "key": "C",
        "text": "$\\frac{26}{47}$"
      },
      {
        "key": "D",
        "text": "$\\frac{676}{98}$"
      },
      {
        "key": "E",
        "text": "$\\frac{676}{47}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{47}$ lalu hitung limit standar $\\frac{26^2}{2} = \\frac{676}{94}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(26x)}{47x^2} = \\frac{1}{47} \\cdot \\frac{26^2}{2} = \\frac{676}{94}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-23",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(27x)}{49x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{729}{98}$"
      },
      {
        "key": "B",
        "text": "$\\frac{731}{98}$"
      },
      {
        "key": "C",
        "text": "$\\frac{27}{49}$"
      },
      {
        "key": "D",
        "text": "$\\frac{729}{102}$"
      },
      {
        "key": "E",
        "text": "$\\frac{729}{49}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{49}$ lalu hitung limit standar $\\frac{27^2}{2} = \\frac{729}{98}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(27x)}{49x^2} = \\frac{1}{49} \\cdot \\frac{27^2}{2} = \\frac{729}{98}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-24",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Integral Substitusi Parsial & Luas Daerah Tertutup",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(28x)}{51x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{784}{102}$"
      },
      {
        "key": "B",
        "text": "$\\frac{786}{102}$"
      },
      {
        "key": "C",
        "text": "$\\frac{28}{51}$"
      },
      {
        "key": "D",
        "text": "$\\frac{784}{106}$"
      },
      {
        "key": "E",
        "text": "$\\frac{784}{51}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "INTEGRAL PARSIAL",
      "latex": "\\int u \\, dv = uv - \\int v \\, du",
      "legend": "• Pilihlah $u$ menurut kaidah LIATE<br>• Luas antara kurva $L = \\int_a^b (y_\\\\atas}} - y_\\\\bawah}}) \\, dx$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{51}$ lalu hitung limit standar $\\frac{28^2}{2} = \\frac{784}{102}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(28x)}{51x^2} = \\frac{1}{51} \\cdot \\frac{28^2}{2} = \\frac{784}{102}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-25",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(29x)}{53x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{841}{106}$"
      },
      {
        "key": "B",
        "text": "$\\frac{843}{106}$"
      },
      {
        "key": "C",
        "text": "$\\frac{29}{53}$"
      },
      {
        "key": "D",
        "text": "$\\frac{841}{110}$"
      },
      {
        "key": "E",
        "text": "$\\frac{841}{53}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA SISA POLINOMIAL",
      "latex": "P(x) = Q(x)H(x) + S(x)",
      "legend": "• $P(x)$: Suku banyak<br>• $H(x)$: Hasil bagi<br>• $S(x)$: Sisa derajat $< \\deg(Q)"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{53}$ lalu hitung limit standar $\\frac{29^2}{2} = \\frac{841}{106}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(29x)}{53x^2} = \\frac{1}{53} \\cdot \\frac{29^2}{2} = \\frac{841}{106}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-26",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(30x)}{55x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{900}{110}$"
      },
      {
        "key": "B",
        "text": "$\\frac{902}{110}$"
      },
      {
        "key": "C",
        "text": "$\\frac{30}{55}$"
      },
      {
        "key": "D",
        "text": "$\\frac{900}{114}$"
      },
      {
        "key": "E",
        "text": "$\\frac{900}{55}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA DERAJAT TIGA",
      "latex": "x_1 + x_2 + x_3 = -\\frac{b}{a}, \\quad x_1 x_2 + x_2 x_3 + x_1 x_3 = \\frac{c}{a}",
      "legend": "• $ax^3 + bx^2 + cx + d = 0$<br>• Hasil kali tiga akar $x_1 x_2 x_3 = -\\frac{d}{a}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{55}$ lalu hitung limit standar $\\frac{30^2}{2} = \\frac{900}{110}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(30x)}{55x^2} = \\frac{1}{55} \\cdot \\frac{30^2}{2} = \\frac{900}{110}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-27",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 28 & 0 & 2 \\\\ 1 & 27 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.33$"
      },
      {
        "key": "B",
        "text": "$0.17$"
      },
      {
        "key": "C",
        "text": "$1.3699999999999999$"
      },
      {
        "key": "D",
        "text": "$2.17$"
      },
      {
        "key": "E",
        "text": "$3.67$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS / EKSPANSI KOFAKTOR",
      "latex": "\\det(A) = a_{11}C_{11} + a_{12}C_{12} + a_{13}C_{13}",
      "legend": "• $C_{ij} = (-1)^{i+j} M_{ij}$ (Kofaktor)<br>• $A^{-1} =\\\\1}{\\det(A)}\\\\Adj}(A)$"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.17$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-28",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 29 & 0 & 2 \\\\ 1 & 28 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.33$"
      },
      {
        "key": "B",
        "text": "$0.17$"
      },
      {
        "key": "C",
        "text": "$1.3699999999999999$"
      },
      {
        "key": "D",
        "text": "$2.17$"
      },
      {
        "key": "E",
        "text": "$3.67$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ATURAN CRAMER SISTEM LINEAR",
      "latex": "x = \\frac{\\det(A_x)}{\\det(A)}, \\quad y = \\frac{\\det(A_y)}{\\det(A)}, \\quad z = \\frac{\\det(A_z)}{\\det(A)}",
      "legend": "• $\\det(A)\\\\0$<br>• $A_k$ mengganti kolom ke-$k$ dengan vektor konstanta"
    },
    "hints": {
      "concept": "Matriks singular memenuhi kondisi mutlak $\\det(M) = 0$.",
      "execution": "Lakukan ekspansi kofaktor sepanjang baris pertama yang memiliki elemen 0 untuk eliminasi cepat."
    },
    "explanation": "Syarat matriks singular adalah $\\det(M) = 0$. Ekspansi baris pertama menghasilkan determinan nol jika $k = 0.17$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-29",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{244} + \\frac{y^2}{176} = 1$ yang sejajar dengan garis linear $y = 2x + 29$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 33.9$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 37.1$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 33.9$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 33.9$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 67.8$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARIS SINGGUNG PARABOLA BERGRADISIEN $m$",
      "latex": "y - k = m(x - h) + \\frac{p}{m}",
      "legend": "• Parabola $(y-k)^2 = 4p(x-h)$<br>• $p$: Jarak fokus ke puncak"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 33.9$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-30",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{252} + \\frac{y^2}{182} = 1$ yang sejajar dengan garis linear $y = 2x + 30$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 34.5$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 37.7$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 34.5$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 34.5$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 69.0$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA HORIZONTAL",
      "latex": "\\frac{(x-h)^2}{a^2} - \\frac{(y-k)^2}{b^2} = 1 \\implies y - k = \\pm \\frac{b}{a}(x - h)",
      "legend": "• Pusat $(h,k)$<br>• Asimtot garis pemandu hiperbola"
    },
    "hints": {
      "concept": "Garis sejajar memiliki gradien identik ($m_1 = m_2 = 2$).",
      "execution": "Substitusikan gradien $m=2$, $a^2$, dan $b^2$ ke formula garis singgung elips."
    },
    "explanation": "Gradien garis singgung $m = 2$. Rumus garis singgung elips bergradien $m$ adalah $y = mx \\pm \\sqrt{a^2 m^2 + b^2}$. Diperoleh $y = 2x \\pm 34.5$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-31",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IDENTITAS SUDUT GANDA KOSINUS",
      "latex": "\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta",
      "legend": "• $\\sin(\\\\ = 2\\si\\\\\co\\\\<br>• \\\\\\\\ =\\\\2\ta\\\\{1 -\\\\\\\\$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-32",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "BENTUK KHUSUS SINUS-KOSINUS",
      "latex": "a\\cos x + b\\sin x = k\\cos(x - \\alpha)",
      "legend": "• $k = \\sqrt{a^2 + b^2}$<br>• \\\\u0007lpha =\\\\b}{a}$ dengan syarat $|c| \\leq k$"
    },
    "hints": {
      "concept": "Misalkan $p = \\cos x$ dan selesaikan sebagai persamaan kuadrat aljabar murni.",
      "execution": "Akar-akar kuadrat adalah $p = 1$ dan $p = 1/2$. Tentukan sudut kuadran I dan IV."
    },
    "explanation": "Faktorisasi: $(2\\cos x - 1)(\\cos x - 1) = 0 \\implies \\cos x = \\frac{1}{2}$ atau $\\cos x = 1$. Pada interval $[0, 2\\pi]$, nilai $x$ adalah $0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-33",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (69, -2, 37)$ dan $\\vec{v} = (2, 33, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$30$"
      },
      {
        "key": "B",
        "text": "$33$"
      },
      {
        "key": "C",
        "text": "$35$"
      },
      {
        "key": "D",
        "text": "$39$"
      },
      {
        "key": "E",
        "text": "$44$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL",
      "latex": "\\vec{p} = \\left(\\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\right)\\vec{v}",
      "legend": "• Panjang proyeksi skalar: $|\u000bec{p}| =\\\\|\u000bec{u} \\cdot \u000bec{v}|}{|\u000bec{v}|}$<br>• Vektor ortogonal searah $\u000bec{v}$"
    },
    "hints": {
      "concept": "Dot product dua vektor $\\vec{u} \\cdot \\vec{v} = u_x v_x + u_y v_y + u_z v_z$.",
      "execution": "Kalikan komponen yang bersesuaian: 138 + (-66) + (-37) = 35."
    },
    "explanation": "Perkalian skalar $\\vec{u} \\cdot \\vec{v} = (69)(2) + (-2)(33) + (37)(-1) = 138 - 66 - 37 = 35$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-34",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(38x)}{71x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1444}{142}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1446}{142}$"
      },
      {
        "key": "C",
        "text": "$\\frac{38}{71}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1444}{146}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1444}{71}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIMIT TRIGONOMETRI KHUSUS",
      "latex": "\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}",
      "legend": "• Subtitusi identitas $1 - \\cos(kx) = 2\\sin^2\\\\kx}{2})$<br>• Gunakan sifat $\\lim_{u\\\\0\\\\\\sin u}{u}=1$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{71}$ lalu hitung limit standar $\\frac{38^2}{2} = \\frac{1444}{142}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(38x)}{71x^2} = \\frac{1}{71} \\cdot \\frac{38^2}{2} = \\frac{1444}{142}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-lat-h-35",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(39x)}{73x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1521}{146}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1523}{146}$"
      },
      {
        "key": "C",
        "text": "$\\frac{39}{73}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1521}{150}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1521}{73}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DIFERENSIASI IMPLISIT",
      "latex": "\\frac{d}{dx}[f(x, y)] = 0 \\implies \\frac{\\partial f}{\\partial x} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dx} = 0",
      "legend": "• Anggap $y$ sebagai fungsi terselubung terhadap $x$<br>• Turunan $y^n\\\\n y^{n-1}\\\\dy}{dx}$"
    },
    "hints": {
      "concept": "Gunakan identitas sudut ganda $1 - \\cos(kx) = 2\\sin^2\\left(\\frac{kx}{2}\\right)$.",
      "execution": "Faktorkan koefisien $\\frac{1}{73}$ lalu hitung limit standar $\\frac{39^2}{2} = \\frac{1521}{146}$."
    },
    "explanation": "Berdasarkan formula $\\lim_{x \\to 0} \\frac{1 - \\cos(kx)}{x^2} = \\frac{k^2}{2}$, maka $\\lim_{x \\to 0} \\frac{1 - \\cos(39x)}{73x^2} = \\frac{1}{73} \\cdot \\frac{39^2}{2} = \\frac{1521}{146}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-01",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(5x)}{5x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{25}{10}$"
      },
      {
        "key": "B",
        "text": "$\\frac{27}{10}$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{5}$"
      },
      {
        "key": "D",
        "text": "$\\frac{25}{14}$"
      },
      {
        "key": "E",
        "text": "$\\frac{25}{5}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-02",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(6x)}{7x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{36}{14}$"
      },
      {
        "key": "B",
        "text": "$\\frac{38}{14}$"
      },
      {
        "key": "C",
        "text": "$\\frac{6}{7}$"
      },
      {
        "key": "D",
        "text": "$\\frac{36}{18}$"
      },
      {
        "key": "E",
        "text": "$\\frac{36}{7}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-03",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 4 & 0 & 2 \\\\ 1 & 3 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-0.5$"
      },
      {
        "key": "B",
        "text": "$1.0$"
      },
      {
        "key": "C",
        "text": "$2.2$"
      },
      {
        "key": "D",
        "text": "$3.0$"
      },
      {
        "key": "E",
        "text": "$4.5$"
      }
    ],
    "correctKey": "B",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-04",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 5 & 0 & 2 \\\\ 1 & 4 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-0.65$"
      },
      {
        "key": "B",
        "text": "$0.85$"
      },
      {
        "key": "C",
        "text": "$2.05$"
      },
      {
        "key": "D",
        "text": "$2.85$"
      },
      {
        "key": "E",
        "text": "$4.35$"
      }
    ],
    "correctKey": "B",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-05",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{52} + \\frac{y^2}{32} = 1$ yang sejajar dengan garis linear $y = 2x + 5$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 15.5$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 18.7$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 15.5$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 15.5$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 31.0$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-06",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{60} + \\frac{y^2}{38} = 1$ yang sejajar dengan garis linear $y = 2x + 6$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 16.7$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 19.9$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 16.7$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 16.7$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 33.4$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-07",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-08",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-09",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (21, -2, 13)$ dan $\\vec{v} = (2, 9, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6$"
      },
      {
        "key": "B",
        "text": "$9$"
      },
      {
        "key": "C",
        "text": "$11$"
      },
      {
        "key": "D",
        "text": "$15$"
      },
      {
        "key": "E",
        "text": "$20$"
      }
    ],
    "correctKey": "C",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-10",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(14x)}{23x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{196}{46}$"
      },
      {
        "key": "B",
        "text": "$\\frac{198}{46}$"
      },
      {
        "key": "C",
        "text": "$\\frac{14}{23}$"
      },
      {
        "key": "D",
        "text": "$\\frac{196}{50}$"
      },
      {
        "key": "E",
        "text": "$\\frac{196}{23}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-11",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(15x)}{25x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{225}{50}$"
      },
      {
        "key": "B",
        "text": "$\\frac{227}{50}$"
      },
      {
        "key": "C",
        "text": "$\\frac{15}{25}$"
      },
      {
        "key": "D",
        "text": "$\\frac{225}{54}$"
      },
      {
        "key": "E",
        "text": "$\\frac{225}{25}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-12",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Integral Substitusi Parsial & Luas Daerah Tertutup",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(16x)}{27x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{256}{54}$"
      },
      {
        "key": "B",
        "text": "$\\frac{258}{54}$"
      },
      {
        "key": "C",
        "text": "$\\frac{16}{27}$"
      },
      {
        "key": "D",
        "text": "$\\frac{256}{58}$"
      },
      {
        "key": "E",
        "text": "$\\frac{256}{27}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-13",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(17x)}{29x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{289}{58}$"
      },
      {
        "key": "B",
        "text": "$\\frac{291}{58}$"
      },
      {
        "key": "C",
        "text": "$\\frac{17}{29}$"
      },
      {
        "key": "D",
        "text": "$\\frac{289}{62}$"
      },
      {
        "key": "E",
        "text": "$\\frac{289}{29}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-14",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(18x)}{31x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{324}{62}$"
      },
      {
        "key": "B",
        "text": "$\\frac{326}{62}$"
      },
      {
        "key": "C",
        "text": "$\\frac{18}{31}$"
      },
      {
        "key": "D",
        "text": "$\\frac{324}{66}$"
      },
      {
        "key": "E",
        "text": "$\\frac{324}{31}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-15",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 16 & 0 & 2 \\\\ 1 & 15 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.2$"
      },
      {
        "key": "B",
        "text": "$0.3$"
      },
      {
        "key": "C",
        "text": "$1.5$"
      },
      {
        "key": "D",
        "text": "$2.3$"
      },
      {
        "key": "E",
        "text": "$3.8$"
      }
    ],
    "correctKey": "B",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-16",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 17 & 0 & 2 \\\\ 1 & 16 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.22$"
      },
      {
        "key": "B",
        "text": "$0.28$"
      },
      {
        "key": "C",
        "text": "$1.48$"
      },
      {
        "key": "D",
        "text": "$2.2800000000000002$"
      },
      {
        "key": "E",
        "text": "$3.7800000000000002$"
      }
    ],
    "correctKey": "B",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-17",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{148} + \\frac{y^2}{104} = 1$ yang sejajar dengan garis linear $y = 2x + 17$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 26.4$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 29.6$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 26.4$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 26.4$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 52.8$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-18",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{156} + \\frac{y^2}{110} = 1$ yang sejajar dengan garis linear $y = 2x + 18$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 27.1$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 30.3$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 27.1$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 27.1$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 54.2$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-19",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Rumus Jumlah & Selisih Sudut Serta Sudut Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-20",
    "subject": "mtk_lanjut",
    "materi": "TRIGONOMETRI LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Trigonometri $a\\cos x + b\\sin x = c$",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian persamaan trigonometri kuadratis $2\\cos^2 x - 3\\cos x + 1 = 0$ pada interval tertutup $0 \\leq x \\leq 2\\pi$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$"
      },
      {
        "key": "B",
        "text": "$\\{\\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "C",
        "text": "$\\{0, \\frac{\\pi}{2}, \\frac{3\\pi}{2}, 2\\pi\\}$"
      },
      {
        "key": "D",
        "text": "$\\{\\frac{\\pi}{3}, \\pi, \\frac{5\\pi}{3}\\}$"
      },
      {
        "key": "E",
        "text": "$\\{0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi\\}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-21",
    "subject": "mtk_lanjut",
    "materi": "VEKTOR RUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Proyeksi Vektor Ortogonal & Skalar",
    "type": "mcq",
    "questionHtml": "Diberikan dua vektor posisi pada ruang dimensi tiga: $\\vec{u} = (45, -2, 25)$ dan $\\vec{v} = (2, 21, -1)$. Jika panjang proyeksi skalar ortogonal vektor $\\vec{u}$ pada arah $\\vec{v}$ bernilai riil tertentu, besar hasil kali skalar (dot product) $\\vec{u} \\cdot \\vec{v}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18$"
      },
      {
        "key": "B",
        "text": "$21$"
      },
      {
        "key": "C",
        "text": "$23$"
      },
      {
        "key": "D",
        "text": "$27$"
      },
      {
        "key": "E",
        "text": "$32$"
      }
    ],
    "correctKey": "C",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-22",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Limit Fungsi Trigonometri Lanjutan",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(26x)}{47x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{676}{94}$"
      },
      {
        "key": "B",
        "text": "$\\frac{678}{94}$"
      },
      {
        "key": "C",
        "text": "$\\frac{26}{47}$"
      },
      {
        "key": "D",
        "text": "$\\frac{676}{98}$"
      },
      {
        "key": "E",
        "text": "$\\frac{676}{47}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-23",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Turunan Fungsi Implisit & Aturan Rantai",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(27x)}{49x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{729}{98}$"
      },
      {
        "key": "B",
        "text": "$\\frac{731}{98}$"
      },
      {
        "key": "C",
        "text": "$\\frac{27}{49}$"
      },
      {
        "key": "D",
        "text": "$\\frac{729}{102}$"
      },
      {
        "key": "E",
        "text": "$\\frac{729}{49}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-24",
    "subject": "mtk_lanjut",
    "materi": "KALKULUS LANJUT",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Integral Substitusi Parsial & Luas Daerah Tertutup",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(28x)}{51x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{784}{102}$"
      },
      {
        "key": "B",
        "text": "$\\frac{786}{102}$"
      },
      {
        "key": "C",
        "text": "$\\frac{28}{51}$"
      },
      {
        "key": "D",
        "text": "$\\frac{784}{106}$"
      },
      {
        "key": "E",
        "text": "$\\frac{784}{51}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-25",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Teorema Sisa & Pembagian Horner",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(29x)}{53x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{841}{106}$"
      },
      {
        "key": "B",
        "text": "$\\frac{843}{106}$"
      },
      {
        "key": "C",
        "text": "$\\frac{29}{53}$"
      },
      {
        "key": "D",
        "text": "$\\frac{841}{110}$"
      },
      {
        "key": "E",
        "text": "$\\frac{841}{53}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-26",
    "subject": "mtk_lanjut",
    "materi": "POLINOMIAL & SUKU BANYAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Teorema Vieta Akar Polinomial",
    "type": "mcq",
    "questionHtml": "Nilai limit trigonometri tak tentu $\\lim_{x \\to 0} \\frac{1 - \\cos(30x)}{55x^2}$ setara dengan rasio bilangan rasional...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{900}{110}$"
      },
      {
        "key": "B",
        "text": "$\\frac{902}{110}$"
      },
      {
        "key": "C",
        "text": "$\\frac{30}{55}$"
      },
      {
        "key": "D",
        "text": "$\\frac{900}{114}$"
      },
      {
        "key": "E",
        "text": "$\\frac{900}{55}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-27",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Invers & Determinan Matriks 3x3",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 28 & 0 & 2 \\\\ 1 & 27 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.33$"
      },
      {
        "key": "B",
        "text": "$0.17$"
      },
      {
        "key": "C",
        "text": "$1.3699999999999999$"
      },
      {
        "key": "D",
        "text": "$2.17$"
      },
      {
        "key": "E",
        "text": "$3.67$"
      }
    ],
    "correctKey": "B",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-28",
    "subject": "mtk_lanjut",
    "materi": "MATRIKS & DETERMINAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Persamaan Linear Aturan Cramer",
    "type": "mcq",
    "questionHtml": "Diberikan matriks singular berordo $3 \\times 3$, $M = \\begin{pmatrix} 29 & 0 & 2 \\\\ 1 & 28 & -1 \\\\ 3 & 1 & k \\end{pmatrix}$. Agar matriks $M$ tidak memiliki invers (determinan bernilai nol), nilai konstanta $k$ yang memenuhi adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-1.33$"
      },
      {
        "key": "B",
        "text": "$0.17$"
      },
      {
        "key": "C",
        "text": "$1.3699999999999999$"
      },
      {
        "key": "D",
        "text": "$2.17$"
      },
      {
        "key": "E",
        "text": "$3.67$"
      }
    ],
    "correctKey": "B",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-29",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Parabola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{244} + \\frac{y^2}{176} = 1$ yang sejajar dengan garis linear $y = 2x + 29$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 33.9$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 37.1$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 33.9$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 33.9$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 67.8$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "mtk_lanjut-sim-30",
    "subject": "mtk_lanjut",
    "materi": "GEOMETRI ANALITIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Garis Singgung Elips & Asimtot Hiperbola",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung elips $\\frac{x^2}{252} + \\frac{y^2}{182} = 1$ yang sejajar dengan garis linear $y = 2x + 30$ memiliki persamaan...",
    "options": [
      {
        "key": "A",
        "text": "$y = 2x \\pm 34.5$"
      },
      {
        "key": "B",
        "text": "$y = 2x \\pm 37.7$"
      },
      {
        "key": "C",
        "text": "$y = -2x \\pm 34.5$"
      },
      {
        "key": "D",
        "text": "$y = \\frac{1}{2}x \\pm 34.5$"
      },
      {
        "key": "E",
        "text": "$y = 2x \\pm 69.0$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  }
];
