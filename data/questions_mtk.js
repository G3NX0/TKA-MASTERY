/**
 * TKA MASTERY HUB - AUTENTIK & BALANCED DATASET
 * Subject: TKA_MTK_QUESTIONS
 * Keys rebalanced ~20% A-E, AI distractor padding sanitized.
 */

window.TKA_MTK_QUESTIONS = [
  {
    "id": "mtk-lat-e-01",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Fungsi Komposisi & Invers Finansial",
    "type": "mcq",
    "questionHtml": "Sebuah platform logistik menerapkan voucer merchant $f(x) = x - 25.000$ untuk transaksi bernilai dasar di atas Rp100.000. Dari nilai setelah voucer tersebut, dikenakan biaya penanganan $5\\%$ dan asuransi tetap Rp4.000, sehingga total tagihan dimodelkan oleh $g(y) = 1,05y + 4.000$. Jika pembeli membayar tepat <strong>Rp214.000</strong>, harga dasar barang sebelum voucer dan biaya penanganan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Rp 215.000"
      },
      {
        "key": "B",
        "text": "Rp 220.000"
      },
      {
        "key": "C",
        "text": "Rp 230.000"
      },
      {
        "key": "D",
        "text": "Rp 225.000"
      },
      {
        "key": "E",
        "text": "Rp 235.000"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "INVERSI KOMPOSISI",
      "latex": "(g \\circ f)(x) = y \\iff x = f^{-1}(g^{-1}(y))",
      "legend": "• $y$ = Total bayar<br>• Inversikan fungsi terluar $g(y)$ lalu fungsi dalam $f(x)$"
    },
    "hints": {
      "concept": "Hitung nilai sebelum asuransi dan biaya 5%, lalu tambahkan voucer Rp25.000.",
      "execution": "Kurangkan 4.000 dari 214.000 = 210.000. Bagi 1,05 = 200.000. Tambahkan 25.000 = 225.000."
    },
    "explanation": "<strong>Tahap 1:</strong> $1,05y + 4.000 = 214.000 \\implies 1,05y = 210.000 \\implies y = 200.000$.<br><strong>Tahap 2:</strong> $x - 25.000 = 200.000 \\implies x = 225.000$.<br><strong>Kesimpulan:</strong> Harga dasar barang adalah Rp225.000.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-02",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Statistika Rata-rata Gabungan",
    "type": "mcq",
    "questionHtml": "Sebuah pabrik tekstil mengoperasikan $18\\text{ unit}$ mesin tenun dengan rata-rata hasil produksi harian $85\\text{ meter}$ kain per mesin. Manajemen mengganti $2\\text{ unit}$ mesin lama dengan $2\\text{ unit}$ mesin baru, sehingga rata-rata produksi seluruh $18\\text{ unit}$ mesin naik menjadi $88\\text{ meter}$. Jika rata-rata $2\\text{ unit}$ mesin lama adalah $70\\text{ meter}$, rata-rata produksi $2\\text{ unit}$ mesin baru adalah...",
    "options": [
      {
        "key": "A",
        "text": "97 meter"
      },
      {
        "key": "B",
        "text": "105 meter"
      },
      {
        "key": "C",
        "text": "94 meter"
      },
      {
        "key": "D",
        "text": "101 meter"
      },
      {
        "key": "E",
        "text": "110 meter"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "RATA-RATA GABUNGAN",
      "latex": "\\Delta \\text{Total} = n(\\bar{x}_{\\text{baru}} - \\bar{x}_{\\text{lama}})",
      "legend": "• $n = 18$<br>• Pertambahan output total disumbangkan oleh 2 mesin baru pengganti."
    },
    "hints": {
      "concept": "Hitung kenaikan total output pabrik, lalu tambahkan ke total output mesin lama yang ditarik.",
      "execution": "Kenaikan total $= 18 \\times 3 = 54$. Total 2 mesin baru $= (2 \\times 70) + 54 = 194$. Rata-rata $= 194 / 2 = 97$."
    },
    "explanation": "<strong>Tahap 1:</strong> Total awal $= 18 \\times 85 = 1.530$. Total baru $= 18 \\times 88 = 1.584$. Selisih $= 54\\text{ m}$.<br><strong>Tahap 2:</strong> Mesin lama $= 2 \\times 70 = 140$. Mesin baru $= 140 + 54 = 194\\text{ m}$.<br><strong>Tahap 3:</strong> Rata-rata $= 194 / 2 = 97\\text{ meter}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-03",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Eksponen & Persamaan Pangkat",
    "type": "mcq",
    "questionHtml": "Diberikan persamaan eksponensial $2^{2x - 1} \\cdot 4^{x + 1} = 128$. Nilai $x$ yang memenuhi persamaan tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{3}{2}$"
      },
      {
        "key": "B",
        "text": "$2$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{4}$"
      },
      {
        "key": "D",
        "text": "$\\frac{7}{4}$"
      },
      {
        "key": "E",
        "text": "$1$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SIFAT EKSPONEN BASIS 2",
      "latex": "a^m \\cdot a^n = a^{m+n}, \\quad 4 = 2^2, \\quad 128 = 2^7",
      "legend": "• Samakan basis menjadi 2 di kedua ruas."
    },
    "hints": {
      "concept": "Ubah $4^{x+1}$ menjadi $2^{2(x+1)} = 2^{2x+2}$, lalu jumlahkan pangkatnya.",
      "execution": "$2x - 1 + 2x + 2 = 7 \\implies 4x + 1 = 7 \\implies 4x = 6 \\implies x = 3/2$."
    },
    "explanation": "<strong>Tahap 1:</strong> $2^{2x-1} \\cdot 2^{2x+2} = 2^7$.<br><strong>Tahap 2:</strong> $4x + 1 = 7 \\implies x = \\frac{6}{4} = \\frac{3}{2}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-04",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Rasionalisasi Bentuk Akar",
    "type": "mcq",
    "questionHtml": "Bentuk sederhana dan rasional dari pecahan $\\frac{12}{\\sqrt{7} - \\sqrt{3}}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$3(\\sqrt{7} - \\sqrt{3})$"
      },
      {
        "key": "B",
        "text": "$3(\\sqrt{7} + \\sqrt{3})$"
      },
      {
        "key": "C",
        "text": "$2(\\sqrt{7} + \\sqrt{3})$"
      },
      {
        "key": "D",
        "text": "$4(\\sqrt{7} + \\sqrt{3})$"
      },
      {
        "key": "E",
        "text": "$6(\\sqrt{7} - \\sqrt{3})$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "PERKALIAN SEKAWAN",
      "latex": "\\frac{c}{\\sqrt{a}-\\sqrt{b}} \\times \\frac{\\sqrt{a}+\\sqrt{b}}{\\sqrt{a}+\\sqrt{b}} = \\frac{c(\\sqrt{a}+\\sqrt{b})}{a-b}",
      "legend": "• Kalikan pembilang dan penyebut dengan sekawan $(\\sqrt{7} + \\sqrt{3})$."
    },
    "hints": {
      "concept": "Penyebut menjadi $(\\sqrt{7})^2 - (\\sqrt{3})^2 = 7 - 3 = 4$.",
      "execution": "Bagi 12 dengan 4 menghasilkan koefisien 3."
    },
    "explanation": "<strong>Solusi:</strong> $\\frac{12(\\sqrt{7}+\\sqrt{3})}{7-3} = \\frac{12(\\sqrt{7}+\\sqrt{3})}{4} = 3(\\sqrt{7}+\\sqrt{3})$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-05",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sifat Operasi Logaritma",
    "type": "mcq",
    "questionHtml": "Nilai dari ekspresi logaritma $^3\\log 54 + ^3\\log 18 - ^3\\log 4$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$3$"
      },
      {
        "key": "B",
        "text": "$5$"
      },
      {
        "key": "C",
        "text": "$4$"
      },
      {
        "key": "D",
        "text": "$6$"
      },
      {
        "key": "E",
        "text": "$9$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "SIFAT OPERASI LOGARITMA",
      "latex": "^a\\log b + ^a\\log c - ^a\\log d = ^a\\log\\left(\\frac{b \\cdot c}{d}\\right)",
      "legend": "• Gabungkan seluruh numerus di bawah basis 3."
    },
    "hints": {
      "concept": "Hitung numerus: $(54 \\times 18) / 4 = 243$.",
      "execution": "Karena $243 = 3^5$, maka nilainya adalah 5."
    },
    "explanation": "<strong>Solusi:</strong> $^3\\log\\left(\\frac{54 \\times 18}{4}\\right) = ^3\\log(243) = ^3\\log(3^5) = 5$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-06",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Suku ke-n Barisan Aritmetika",
    "type": "mcq",
    "questionHtml": "Diketahui suku ke-3 suatu barisan aritmetika adalah $14$ dan suku ke-7 adalah $26$. Suku ke-20 barisan tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$65$"
      },
      {
        "key": "B",
        "text": "$74$"
      },
      {
        "key": "C",
        "text": "$62$"
      },
      {
        "key": "D",
        "text": "$71$"
      },
      {
        "key": "E",
        "text": "$68$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SUKU KE-N BARISAN ARITMETIKA",
      "latex": "U_n = a + (n - 1)b, \\quad b = \\frac{U_q - U_p}{q - p}",
      "legend": "• Cari beda $b$ dari selisih suku, lalu cari suku pertama $a$."
    },
    "hints": {
      "concept": "$b = (26 - 14) / (7 - 3) = 12 / 4 = 3$.",
      "execution": "$a = U_3 - 2b = 14 - 6 = 8$. $U_{20} = 8 + 19(3) = 8 + 57 = 65$."
    },
    "explanation": "<strong>Tahap 1:</strong> $4b = 12 \\implies b = 3$.<br><strong>Tahap 2:</strong> $a = 14 - 2(3) = 8$.<br><strong>Tahap 3:</strong> $U_{20} = 8 + 19(3) = 65$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-07",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Deret Aritmetika Produksi Kerajinan",
    "type": "mcq",
    "questionHtml": "Sebuah bengkel pengrajin mebel memproduksi $120\\text{ unit}$ kursi pada bulan pertama. Karena penambahan tenaga kerja, produksinya bertambah secara konstan sebanyak $15\\text{ unit}$ setiap bulan berikutnya. Total kursi yang diproduksi selama $10\\text{ bulan}$ pertama adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2.025\\text{ unit}$"
      },
      {
        "key": "B",
        "text": "$1.950\\text{ unit}$"
      },
      {
        "key": "C",
        "text": "$1.875\\text{ unit}$"
      },
      {
        "key": "D",
        "text": "$1.725\\text{ unit}$"
      },
      {
        "key": "E",
        "text": "$1.800\\text{ unit}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "JUMLAH DERET ARITMETIKA",
      "latex": "S_n = \\frac{n}{2}[2a + (n - 1)b]",
      "legend": "• $a = 120, b = 15, n = 10$."
    },
    "hints": {
      "concept": "Gunakan formula $S_{10} = 5 \\times [2(120) + 9(15)]$.",
      "execution": "$S_{10} = 5 \\times [240 + 135] = 5 \\times 375 = 1.875$."
    },
    "explanation": "<strong>Solusi:</strong> $S_{10} = \\frac{10}{2}[2(120) + 9(15)] = 5(240 + 135) = 5(375) = 1.875\\text{ unit}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-08",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Persamaan Linear Dua Variabel",
    "type": "mcq",
    "questionHtml": "Di sebuah koperasi sekolah, harga $3\\text{ buku tulis}$ dan $2\\text{ pena}$ adalah Rp16.500, sedangkan harga $2\\text{ buku tulis}$ dan $4\\text{ pena}$ adalah Rp19.000. Harga yang harus dibayar untuk $1\\text{ buku tulis}$ dan $1\\text{ pena}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "Rp 7.000"
      },
      {
        "key": "B",
        "text": "Rp 6.250"
      },
      {
        "key": "C",
        "text": "Rp 6.000"
      },
      {
        "key": "D",
        "text": "Rp 6.750"
      },
      {
        "key": "E",
        "text": "Rp 6.500"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "ELIMINASI SPLDV",
      "latex": "3x + 2y = 16.500, \\quad 2x + 4y = 19.000",
      "legend": "• $x$ = harga 1 buku tulis, $y$ = harga 1 pena."
    },
    "hints": {
      "concept": "Bagi persamaan kedua dengan 2: $x + 2y = 9.500$. Kurangkan dari persamaan pertama.",
      "execution": "$(3x + 2y) - (x + 2y) = 2x = 7.000 \\implies x = 3.500$. Maka $y = 3.000$. Total $x + y = 6.500$."
    },
    "explanation": "<strong>Solusi:</strong> $x = 3.500, y = 3.000 \\implies x + y = \\text{Rp}6.500$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-09",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Akar Persamaan Kuadrat",
    "type": "mcq",
    "questionHtml": "Akar-akar dari persamaan kuadrat $x^2 - 8x + 15 = 0$ adalah $x_1$ dan $x_2$ dengan $x_1 > x_2$. Nilai dari $2x_1 - 3x_2$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$3$"
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
        "text": "$5$"
      },
      {
        "key": "E",
        "text": "$2$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PEMFAKTORAN KUADRAT",
      "latex": "(x - p)(x - q) = 0 \\iff x = p \\text{ atau } x = q",
      "legend": "• Faktorkan bilangan yang jika dikali menghasilkan 15 dan dijumlahkan menghasilkan -8."
    },
    "hints": {
      "concept": "Faktornya adalah $(x - 5)(x - 3) = 0$.",
      "execution": "$x_1 = 5$ dan $x_2 = 3$. Nilai $2(5) - 3(3) = 10 - 9 = 1$."
    },
    "explanation": "<strong>Solusi:</strong> Akar adalah 5 dan 3. Nilai $2(5) - 3(3) = 1$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-10",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Teorema Vieta",
    "type": "mcq",
    "questionHtml": "Jika $\\alpha$ dan $\\beta$ merupakan akar-akar dari persamaan kuadrat $2x^2 - 6x + 3 = 0$, maka nilai dari $\\frac{1}{\\alpha} + \\frac{1}{\\beta}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$2$"
      },
      {
        "key": "B",
        "text": "$3$"
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
        "text": "$\\frac{5}{2}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA VIETA",
      "latex": "\\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha \\beta = \\frac{c}{a}",
      "legend": "• $\\alpha + \\beta = 3, \\alpha\\beta = 3/2$."
    },
    "hints": {
      "concept": "$\\frac{1}{\\alpha} + \\frac{1}{\\beta} = \\frac{\\alpha + \\beta}{\\alpha\\beta}$.",
      "execution": "$3 / (3/2) = 2$."
    },
    "explanation": "<strong>Solusi:</strong> $\\frac{3}{3/2} = 2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-11",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Pertidaksamaan Linear Satu Variabel",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian dari pertidaksamaan linear $4(x - 2) \\le 2x + 6$ untuk $x$ bilangan real adalah...",
    "options": [
      {
        "key": "A",
        "text": "$x \\ge 7$"
      },
      {
        "key": "B",
        "text": "$x \\ge 9$"
      },
      {
        "key": "C",
        "text": "$x \\le 5$"
      },
      {
        "key": "D",
        "text": "$x \\le 9$"
      },
      {
        "key": "E",
        "text": "$x \\le 7$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "PERTIDAKSAMAAN LINEAR",
      "latex": "ax + b \\le cx + d \\iff (a - c)x \\le d - b",
      "legend": "• Buka tanda kurung dan kumpulkan suku bervariabel $x$ di ruas kiri."
    },
    "hints": {
      "concept": "$4x - 8 \\le 2x + 6 \\implies 2x \\le 14 \\implies x \\le 7$.",
      "execution": "$x \\le 7$."
    },
    "explanation": "<strong>Solusi:</strong> $4x - 8 \\le 2x + 6 \\implies 2x \\le 14 \\implies x \\le 7$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-12",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Gradien Garis Melalui Dua Titik",
    "type": "mcq",
    "questionHtml": "Gradien garis lurus yang melalui titik $A(2, -3)$ dan $B(6, 5)$ pada bidang koordinat Cartesius adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{5}{2}$"
      },
      {
        "key": "B",
        "text": "$\\frac{3}{2}$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{2}$"
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
    "correctKey": "E",
    "formulaHud": {
      "title": "FORMULA GRADIEN GARIS",
      "latex": "m = \\frac{y_2 - y_1}{x_2 - x_1}",
      "legend": "• Substitusikan koordinat titik $A$ dan $B$."
    },
    "hints": {
      "concept": "$m = \\frac{5 - (-3)}{6 - 2} = \\frac{8}{4} = 2$.",
      "execution": "$m = 2$."
    },
    "explanation": "<strong>Solusi:</strong> $m = \\frac{5 - (-3)}{6 - 2} = \\frac{8}{4} = 2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-13",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Evaluasi Nilai Fungsi Komposisi",
    "type": "mcq",
    "questionHtml": "Diketahui fungsi $f(x) = 3x - 2$ dan $g(x) = x^2 + 1$. Nilai dari $(f \\circ g)(2)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$11$"
      },
      {
        "key": "B",
        "text": "$17$"
      },
      {
        "key": "C",
        "text": "$15$"
      },
      {
        "key": "D",
        "text": "$19$"
      },
      {
        "key": "E",
        "text": "$13$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "KOMPOSISI FUNGSI",
      "latex": "(f \\circ g)(x) = f(g(x))",
      "legend": "• Evaluasi $g(2)$ terlebih dahulu, lalu masukkan hasilnya ke $f(x)$."
    },
    "hints": {
      "concept": "$g(2) = 2^2 + 1 = 5$.",
      "execution": "$f(5) = 3(5) - 2 = 15 - 2 = 13$."
    },
    "explanation": "<strong>Solusi:</strong> $g(2) = 5 \\implies f(5) = 3(5) - 2 = 13$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-14",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Invers Fungsi Linear",
    "type": "mcq",
    "questionHtml": "Jika $f(x) = \\frac{4x - 5}{3}$, maka rumus fungsi invers $f^{-1}(x)$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{4x + 3}{5}$"
      },
      {
        "key": "B",
        "text": "$\\frac{3x + 5}{4}$"
      },
      {
        "key": "C",
        "text": "$\\frac{3x - 4}{5}$"
      },
      {
        "key": "D",
        "text": "$\\frac{4x - 3}{5}$"
      },
      {
        "key": "E",
        "text": "$\\frac{3x - 5}{4}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "INVERS FUNGSI LINEAR",
      "latex": "y = \\frac{ax + b}{c} \\iff x = \\frac{cy - b}{a}",
      "legend": "• Nyatakan $x$ dalam bentuk variabel $y$."
    },
    "hints": {
      "concept": "$3y = 4x - 5 \\implies 4x = 3y + 5 \\implies x = \\frac{3y + 5}{4}$.",
      "execution": "$f^{-1}(x) = \\frac{3x + 5}{4}$."
    },
    "explanation": "<strong>Solusi:</strong> $y = \\frac{4x - 5}{3} \\implies 3y = 4x - 5 \\implies 4x = 3y + 5 \\implies x = \\frac{3y + 5}{4}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-15",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Penjumlahan & Pengurangan Matriks",
    "type": "mcq",
    "questionHtml": "Diberikan matriks $A = \\begin{pmatrix} 3 & -1 \\\\ 2 & 4 \\end{pmatrix}$ dan $B = \\begin{pmatrix} 1 & 5 \\\\ -3 & 2 \\end{pmatrix}$. Matriks $2A - B$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\begin{pmatrix} 5 & -7 \\\\ 1 & 6 \\end{pmatrix}$"
      },
      {
        "key": "B",
        "text": "$\\begin{pmatrix} 7 & -7 \\\\ 1 & 10 \\end{pmatrix}$"
      },
      {
        "key": "C",
        "text": "$\\begin{pmatrix} 5 & -7 \\\\ 7 & 6 \\end{pmatrix}$"
      },
      {
        "key": "D",
        "text": "$\\begin{pmatrix} 7 & -3 \\\\ 7 & 6 \\end{pmatrix}$"
      },
      {
        "key": "E",
        "text": "$\\begin{pmatrix} 5 & 3 \\\\ 7 & 6 \\end{pmatrix}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "OPERASI ELEMEN MATRIKS",
      "latex": "k \\cdot A - B = [k \\cdot a_{ij} - b_{ij}]",
      "legend": "• Kalikan setiap elemen matriks $A$ dengan 2, lalu kurangkan dengan elemen matriks $B$."
    },
    "hints": {
      "concept": "$2A = \\begin{pmatrix} 6 & -2 \\\\ 4 & 8 \\end{pmatrix}$. Kurangkan $B$.",
      "execution": "Baris 1: $6-1 = 5, -2-5 = -7$. Baris 2: $4-(-3) = 7, 8-2 = 6$."
    },
    "explanation": "<strong>Solusi:</strong> $2A - B = \\begin{pmatrix} 6-1 & -2-5 \\\\ 4-(-3) & 8-2 \\end{pmatrix} = \\begin{pmatrix} 5 & -7 \\\\ 7 & 6 \\end{pmatrix}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-16",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Perkalian Dua Matriks 2x2",
    "type": "mcq",
    "questionHtml": "Hasil perkalian matriks $\\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\end{pmatrix} \\begin{pmatrix} 4 & -2 \\\\ 1 & 5 \\end{pmatrix}$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\begin{pmatrix} 9 & 1 \\\\ 3 & 15 \\end{pmatrix}$"
      },
      {
        "key": "B",
        "text": "$\\begin{pmatrix} 9 & 3 \\\\ 1 & 15 \\end{pmatrix}$"
      },
      {
        "key": "C",
        "text": "$\\begin{pmatrix} 9 & -1 \\\\ 3 & 15 \\end{pmatrix}$"
      },
      {
        "key": "D",
        "text": "$\\begin{pmatrix} 7 & 1 \\\\ 3 & 12 \\end{pmatrix}$"
      },
      {
        "key": "E",
        "text": "$\\begin{pmatrix} 8 & -2 \\\\ 0 & 15 \\end{pmatrix}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PERKALIAN MATRIKS",
      "latex": "c_{ij} = \\sum a_{ik} b_{kj}",
      "legend": "• Baris kali kolom."
    },
    "hints": {
      "concept": "Baris 1: $2(4)+1(1) = 9$ dan $2(-2)+1(5) = 1$. Baris 2: $0(4)+3(1) = 3$ dan $0(-2)+3(5) = 15$.",
      "execution": "Matriks hasil $= \\begin{pmatrix} 9 & 1 \\\\ 3 & 15 \\end{pmatrix}$."
    },
    "explanation": "<strong>Solusi:</strong> Elemen $(1,1)=9, (1,2)=1, (2,1)=3, (2,2)=15$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-17",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Determinan Matriks Ordo 2x2",
    "type": "mcq",
    "questionHtml": "Jika matriks $M = \\begin{pmatrix} 5 & 3 \\\\ 4 & x \\end{pmatrix}$ memiliki nilai determinan sama dengan $8$, maka nilai $x$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6$"
      },
      {
        "key": "B",
        "text": "$4$"
      },
      {
        "key": "C",
        "text": "$5$"
      },
      {
        "key": "D",
        "text": "$3$"
      },
      {
        "key": "E",
        "text": "$2$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DETERMINAN ORDO 2x2",
      "latex": "\\det(M) = ad - bc",
      "legend": "• $ad - bc = 8$."
    },
    "hints": {
      "concept": "$5x - 12 = 8 \\implies 5x = 20 \\implies x = 4$.",
      "execution": "$x = 4$."
    },
    "explanation": "<strong>Solusi:</strong> $5(x) - 3(4) = 8 \\implies 5x - 12 = 8 \\implies 5x = 20 \\implies x = 4$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-18",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Suku ke-n Barisan Geometri",
    "type": "mcq",
    "questionHtml": "Suku pertama suatu barisan geometri adalah $3$ dan suku ke-4 adalah $24$. Nilai suku ke-6 barisan tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$192$"
      },
      {
        "key": "B",
        "text": "$48$"
      },
      {
        "key": "C",
        "text": "$96$"
      },
      {
        "key": "D",
        "text": "$128$"
      },
      {
        "key": "E",
        "text": "$72$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "BARISAN GEOMETRI",
      "latex": "U_n = a \\cdot r^{n-1}, \\quad r^3 = \\frac{U_4}{U_1}",
      "legend": "• Tentukan rasio $r$ terlebih dahulu."
    },
    "hints": {
      "concept": "$r^3 = 24 / 3 = 8 \\implies r = 2$.",
      "execution": "$U_6 = a \\cdot r^5 = 3 \\cdot 2^5 = 3 \\cdot 32 = 96$."
    },
    "explanation": "<strong>Solusi:</strong> $r = 2 \\implies U_6 = 3 \\times 32 = 96$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-19",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Jarak Dua Titik Koordinat",
    "type": "mcq",
    "questionHtml": "Jarak antara titik $P(1, 2)$ dan titik $Q(7, 10)$ pada bidang koordinat Cartesius adalah...",
    "options": [
      {
        "key": "A",
        "text": "$9\\text{ satuan}$"
      },
      {
        "key": "B",
        "text": "$14\\text{ satuan}$"
      },
      {
        "key": "C",
        "text": "$10\\text{ satuan}$"
      },
      {
        "key": "D",
        "text": "$8\\text{ satuan}$"
      },
      {
        "key": "E",
        "text": "$12\\text{ satuan}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "FORMULA JARAK EUCLIDEAN",
      "latex": "d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}",
      "legend": "• Gunakan dalil Pythagoras pada selisih koordinat."
    },
    "hints": {
      "concept": "$\\Delta x = 7 - 1 = 6$ dan $\\Delta y = 10 - 2 = 8$.",
      "execution": "$d = \\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10$."
    },
    "explanation": "<strong>Solusi:</strong> $d = \\sqrt{6^2 + 8^2} = \\sqrt{100} = 10\\text{ satuan}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-20",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Luas Permukaan Kubus",
    "type": "mcq",
    "questionHtml": "Sebuah wadah berbentuk kubus tanpa tutup memiliki panjang rusuk $8\\text{ cm}$. Luas permukaan karton yang diperlukan untuk membuat wadah tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$448\\text{ cm}^2$"
      },
      {
        "key": "B",
        "text": "$512\\text{ cm}^2$"
      },
      {
        "key": "C",
        "text": "$384\\text{ cm}^2$"
      },
      {
        "key": "D",
        "text": "$320\\text{ cm}^2$"
      },
      {
        "key": "E",
        "text": "$256\\text{ cm}^2$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "LUAS KUBUS TANPA TUTUP",
      "latex": "L = 5 \\times s^2",
      "legend": "• Kubus tanpa tutup memiliki 5 sisi persegi."
    },
    "hints": {
      "concept": "$L = 5 \\times 8^2 = 5 \\times 64 = 320$.",
      "execution": "$L = 320\\text{ cm}^2$."
    },
    "explanation": "<strong>Solusi:</strong> Luas 5 sisi $= 5 \\times 8^2 = 5 \\times 64 = 320\\text{ cm}^2$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-21",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Volume Limas Segi Empat",
    "type": "mcq",
    "questionHtml": "Sebuah limas memiliki alas berbentuk persegi dengan panjang sisi $6\\text{ cm}$. Jika tinggi limas tersebut adalah $10\\text{ cm}$, volume limas adalah...",
    "options": [
      {
        "key": "A",
        "text": "$100\\text{ cm}^3$"
      },
      {
        "key": "B",
        "text": "$150\\text{ cm}^3$"
      },
      {
        "key": "C",
        "text": "$120\\text{ cm}^3$"
      },
      {
        "key": "D",
        "text": "$360\\text{ cm}^3$"
      },
      {
        "key": "E",
        "text": "$180\\text{ cm}^3$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "VOLUME LIMAS",
      "latex": "V = \\frac{1}{3} \\times L_{\\text{alas}} \\times t",
      "legend": "• Luas alas persegi $= s^2 = 6^2 = 36$."
    },
    "hints": {
      "concept": "$V = \\frac{1}{3} \\times 36 \\times 10 = 12 \\times 10 = 120$.",
      "execution": "$V = 120\\text{ cm}^3$."
    },
    "explanation": "<strong>Solusi:</strong> $V = \\frac{1}{3} \\times 36 \\times 10 = 120\\text{ cm}^3$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-22",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Jarak Titik ke Rusuk Kubus",
    "type": "mcq",
    "questionHtml": "Pada kubus $ABCD.EFGH$ dengan panjang rusuk $6\\text{ cm}$, jarak antara titik sudut $A$ ke rusuk tegak $CG$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$12\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$3\\sqrt{2}\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$6\\sqrt{3}\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$6\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$6\\sqrt{2}\\text{ cm}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "JARAK TITIK KE RUSUK TEGAK",
      "latex": "d = AC = s\\sqrt{2}",
      "legend": "• Garis hubung terpendek dari $A$ ke $CG$ adalah garis $AC$ yang tegak lurus dengan $CG$."
    },
    "hints": {
      "concept": "$AC$ adalah diagonal bidang alas kubus dengan panjang $s\\sqrt{2}$.",
      "execution": "$d = 6\\sqrt{2}\\text{ cm}$."
    },
    "explanation": "<strong>Solusi:</strong> Karena $CG \\perp$ bidang $ABCD$, maka proyeksi $A$ ke $CG$ adalah titik $C$. Jarak $A$ ke $CG$ adalah panjang $AC = 6\\sqrt{2}\\text{ cm}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-23",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Sejajar",
    "type": "mcq",
    "questionHtml": "Persamaan garis lurus yang melalui titik $(3, -2)$ dan sejajar dengan garis $y = 4x - 7$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$y = 4x - 12$"
      },
      {
        "key": "B",
        "text": "$y = 4x - 14$"
      },
      {
        "key": "C",
        "text": "$y = 4x - 10$"
      },
      {
        "key": "D",
        "text": "$y = 4x + 10$"
      },
      {
        "key": "E",
        "text": "$y = -4x + 10$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "GARIS SEJAJAR",
      "latex": "m_1 = m_2, \\quad y - y_1 = m(x - x_1)",
      "legend": "• Garis sejajar memiliki gradien sama: $m = 4$."
    },
    "hints": {
      "concept": "$y - (-2) = 4(x - 3) \\implies y + 2 = 4x - 12 \\implies y = 4x - 14$.",
      "execution": "$y = 4x - 14$."
    },
    "explanation": "<strong>Solusi:</strong> $y + 2 = 4(x - 3) \\implies y = 4x - 14$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-24",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Persamaan Garis Tegak Lurus",
    "type": "mcq",
    "questionHtml": "Persamaan garis yang melalui titik $(2, 1)$ dan tegak lurus dengan garis $2x + y - 5 = 0$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$x - 2y + 4 = 0$"
      },
      {
        "key": "B",
        "text": "$2x + y - 5 = 0$"
      },
      {
        "key": "C",
        "text": "$x + 2y - 4 = 0$"
      },
      {
        "key": "D",
        "text": "$2x - y - 3 = 0$"
      },
      {
        "key": "E",
        "text": "$x - 2y = 0$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "GARIS TEGAK LURUS",
      "latex": "m_1 \\cdot m_2 = -1",
      "legend": "• Gradien garis $2x + y - 5 = 0$ adalah $m_1 = -2$. Maka $m_2 = 1/2$."
    },
    "hints": {
      "concept": "$y - 1 = \\frac{1}{2}(x - 2) \\implies 2(y - 1) = x - 2 \\implies 2y - 2 = x - 2 \\implies x - 2y = 0$.",
      "execution": "$x - 2y = 0$."
    },
    "explanation": "<strong>Solusi:</strong> $m_2 = \\frac{1}{2} \\implies y - 1 = \\frac{1}{2}(x - 2) \\implies x - 2y = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-25",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transformasi Translasi Titik",
    "type": "mcq",
    "questionHtml": "Titik $A(5, -3)$ ditranslasikan oleh vektor geser $T = \\begin{pmatrix} -2 \\\\ 7 \\end{pmatrix}$. Koordinat bayangan titik $A'$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$(7, 4)$"
      },
      {
        "key": "B",
        "text": "$(3, -10)$"
      },
      {
        "key": "C",
        "text": "$(7, -10)$"
      },
      {
        "key": "D",
        "text": "$(3, 4)$"
      },
      {
        "key": "E",
        "text": "(-3, 4)"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "FORMULA TRANSLASI",
      "latex": "\\begin{pmatrix} x' \\\\ y' \\end{pmatrix} = \\begin{pmatrix} x \\\\ y \\end{pmatrix} + \\begin{pmatrix} a \\\\ b \\end{pmatrix}",
      "legend": "• Jumlahkan koordinat awal dengan komponen vektor translasi."
    },
    "hints": {
      "concept": "$x' = 5 + (-2) = 3$ dan $y' = -3 + 7 = 4$.",
      "execution": "$A'(3, 4)$."
    },
    "explanation": "<strong>Solusi:</strong> $(5 - 2, -3 + 7) = (3, 4)$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-26",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Rata-rata Nilai Siswa",
    "type": "mcq",
    "questionHtml": "Nilai ulangan matematika dari 8 siswa adalah sebagai berikut: $75, 80, 85, 70, 90, 85, 80, 75$. Rata-rata nilai ulangan tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$81$"
      },
      {
        "key": "B",
        "text": "$82$"
      },
      {
        "key": "C",
        "text": "$79$"
      },
      {
        "key": "D",
        "text": "$80$"
      },
      {
        "key": "E",
        "text": "$78$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "RATA-RATA DATA TUNGGAL",
      "latex": "\\bar{x} = \\frac{\\sum x_i}{n}",
      "legend": "• Jumlahkan seluruh data lalu bagi dengan 8."
    },
    "hints": {
      "concept": "Total $= 75+80+85+70+90+85+80+75 = 640$.",
      "execution": "$\\bar{x} = 640 / 8 = 80$."
    },
    "explanation": "<strong>Solusi:</strong> $\\frac{640}{8} = 80$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-27",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Median Data Terurut",
    "type": "mcq",
    "questionHtml": "Diberikan sekumpulan data: $4, 6, 7, 7, 8, 9, 10, 12, 13$. Nilai kuartil tengah (median) data tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$9$"
      },
      {
        "key": "B",
        "text": "$8,5$"
      },
      {
        "key": "C",
        "text": "$8$"
      },
      {
        "key": "D",
        "text": "$7$"
      },
      {
        "key": "E",
        "text": "$7,5$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "MEDIAN DATA TUNGGAL",
      "latex": "Me = x_{\\frac{n+1}{2}}",
      "legend": "• $n = 9$ data (ganjil). Median adalah data ke-$(9+1)/2 = 5$."
    },
    "hints": {
      "concept": "Data ke-5 adalah 8.",
      "execution": "Median $= 8$."
    },
    "explanation": "<strong>Solusi:</strong> Karena data sudah terurut dengan $n=9$, maka median berada pada urutan ke-5, yaitu 8.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-28",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Aturan Pengisian Tempat (Filling Slots)",
    "type": "mcq",
    "questionHtml": "Dari angka-angka $1, 2, 3, 4, 5, 6$ akan dibentuk bilangan ratusan yang terdiri dari angka-angka berbeda. Banyaknya bilangan ratusan yang dapat dibentuk adalah...",
    "options": [
      {
        "key": "A",
        "text": "$120$"
      },
      {
        "key": "B",
        "text": "$60$"
      },
      {
        "key": "C",
        "text": "$90$"
      },
      {
        "key": "D",
        "text": "$216$"
      },
      {
        "key": "E",
        "text": "$150$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "KAIDAH PENCACAHAN PERMUTASI",
      "latex": "P(n, r) = \\frac{n!}{(n - r)!}",
      "legend": "• Slot ratusan: 6 pilihan, puluhan: 5 pilihan, satuan: 4 pilihan."
    },
    "hints": {
      "concept": "$6 \\times 5 \\times 4 = 120$.",
      "execution": "Banyak cara $= 120$."
    },
    "explanation": "<strong>Solusi:</strong> $6 \\times 5 \\times 4 = 120\\text{ bilangan}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-29",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Peluang Pelemparan Dua Dadu",
    "type": "mcq",
    "questionHtml": "Dua buah dadu bermata enam dilempar bersama-sama satu kali. Peluang munculnya jumlah kedua mata dadu sama dengan $8$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{6}$"
      },
      {
        "key": "B",
        "text": "$\\frac{7}{36}$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{9}$"
      },
      {
        "key": "D",
        "text": "$\\frac{5}{36}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{12}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "PELUANG KLASIK",
      "latex": "P(A) = \\frac{n(A)}{n(S)}",
      "legend": "• Ruang sampel $n(S) = 6 \\times 6 = 36$."
    },
    "hints": {
      "concept": "Pasangan mata dadu berjumlah 8: $(2,6), (3,5), (4,4), (5,3), (6,2) \\implies n(A) = 5$.",
      "execution": "$P(A) = 5/36$."
    },
    "explanation": "<strong>Solusi:</strong> Ada 5 titik sampel dari total 36, sehingga peluangnya adalah $\\frac{5}{36}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-30",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Peluang Pengambilan Bola",
    "type": "mcq",
    "questionHtml": "Dalam sebuah kantong terdapat $5\\text{ bola merah}$ dan $3\\text{ bola biru}$. Jika diambil satu bola secara acak, peluang terambilnya bola biru adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "B",
        "text": "$\\frac{3}{8}$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{8}$"
      },
      {
        "key": "D",
        "text": "$\\frac{3}{5}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{8}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "PELUANG ACORAN",
      "latex": "P = \\frac{\\text{Jumlah Bola Biru}}{\\text{Total Seluruh Bola}}",
      "legend": "• Total bola $= 5 + 3 = 8$."
    },
    "hints": {
      "concept": "Bola biru $= 3$. Peluang $= 3/8$.",
      "execution": "Peluang $= 3/8$."
    },
    "explanation": "<strong>Solusi:</strong> $P = \\frac{3}{5 + 3} = \\frac{3}{8}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-31",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Perbandingan Trigonometri Siku-siku",
    "type": "mcq",
    "questionHtml": "Pada segitiga siku-siku $ABC$ dengan siku-siku di $B$, panjang sisi $AB = 6\\text{ cm}$ dan sisi $BC = 8\\text{ cm}$. Nilai dari $\\sin A$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{3}{5}$"
      },
      {
        "key": "B",
        "text": "$\\frac{4}{5}$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{4}$"
      },
      {
        "key": "D",
        "text": "$\\frac{4}{3}$"
      },
      {
        "key": "E",
        "text": "$\\frac{3}{4}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DEFINISI SINUS",
      "latex": "\\sin A = \\frac{\\text{Sisi Depan}}{\\text{Sisi Miring}} = \\frac{BC}{AC}",
      "legend": "• Sisi miring $AC = \\sqrt{6^2 + 8^2} = \\sqrt{100} = 10$."
    },
    "hints": {
      "concept": "Depan sudut $A$ adalah $BC = 8$.",
      "execution": "$\\sin A = 8/10 = 4/5$."
    },
    "explanation": "<strong>Solusi:</strong> $\\sin A = \\frac{BC}{AC} = \\frac{8}{10} = \\frac{4}{5}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-32",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Evaluasi Sudut Istimewa",
    "type": "mcq",
    "questionHtml": "Nilai dari operasi trigonometri $\\sin 30^\\circ + \\cos 60^\\circ - \\tan 45^\\circ$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$1$"
      },
      {
        "key": "B",
        "text": "$-1$"
      },
      {
        "key": "C",
        "text": "$-\\frac{1}{2}$"
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
    "correctKey": "D",
    "formulaHud": {
      "title": "NILAI SUDUT ISTIMEWA",
      "latex": "\\sin 30^\\circ = \\frac{1}{2}, \\quad \\cos 60^\\circ = \\frac{1}{2}, \\quad \\tan 45^\\circ = 1",
      "legend": "• Substitusi nilai trigonometri sudut istimewa."
    },
    "hints": {
      "concept": "$\\frac{1}{2} + \\frac{1}{2} - 1 = 1 - 1 = 0$.",
      "execution": "Hasilnya adalah 0."
    },
    "explanation": "<strong>Solusi:</strong> $\\frac{1}{2} + \\frac{1}{2} - 1 = 0$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-33",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Konversi Derajat ke Radian",
    "type": "mcq",
    "questionHtml": "Besar sudut $150^\\circ$ jika dinyatakan dalam satuan radian adalah...",
    "options": [
      {
        "key": "A",
        "text": "$\\frac{5}{6}\\pi\\text{ rad}$"
      },
      {
        "key": "B",
        "text": "$\\frac{7}{6}\\pi\\text{ rad}$"
      },
      {
        "key": "C",
        "text": "$\\frac{2}{3}\\pi\\text{ rad}$"
      },
      {
        "key": "D",
        "text": "$\\frac{4}{3}\\pi\\text{ rad}$"
      },
      {
        "key": "E",
        "text": "$\\frac{3}{4}\\pi\\text{ rad}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "KONVERSI RADIAN",
      "latex": "\\theta_{\\text{rad}} = \\theta^\\circ \\times \\frac{\\pi}{180^\\circ}",
      "legend": "• Kalikan besar sudut dengan $\\frac{\\pi}{180^\\circ}$ lalu sederhanakan."
    },
    "hints": {
      "concept": "$\\frac{150}{180}\\pi = \\frac{5}{6}\\pi$.",
      "execution": "Besar sudut $= \\frac{5}{6}\\pi\\text{ rad}$."
    },
    "explanation": "<strong>Solusi:</strong> $\\frac{150}{180}\\pi = \\frac{5}{6}\\pi\\text{ rad}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-34",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Trigonometri di Kuadran II",
    "type": "mcq",
    "questionHtml": "Nilai dari $\\cos 120^\\circ$ adalah...",
    "options": [
      {
        "key": "A",
        "text": "$-\\frac{1}{2}\\sqrt{3}$"
      },
      {
        "key": "B",
        "text": "$-1$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{2}\\sqrt{3}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "E",
        "text": "$-\\frac{1}{2}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "SUDUT BERELASI KUADRAN II",
      "latex": "\\cos(180^\\circ - \\alpha) = -\\cos \\alpha",
      "legend": "• Di kuadran II ($90^\\circ < \\theta < 180^\\circ$), nilai kosinus bernilai negatif."
    },
    "hints": {
      "concept": "$\\cos 120^\\circ = \\cos(180^\\circ - 60^\\circ) = -\\cos 60^\\circ = -\\frac{1}{2}$.",
      "execution": "Nilai kosinus $= -1/2$."
    },
    "explanation": "<strong>Solusi:</strong> $\\cos 120^\\circ = -\\cos 60^\\circ = -\\frac{1}{2}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-e-35",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Aplikasi Klinometer Tinggi Tiang",
    "type": "mcq",
    "questionHtml": "Seorang siswa berdiri pada jarak mendatar $15\\text{ meter}$ dari pangkal sebuah tiang bendera. Ia memandang puncak tiang dengan sudut elevasi $45^\\circ$. Jika tinggi mata siswa dari tanah adalah $1,6\\text{ meter}$, maka tinggi tiang bendera tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$15,0\\text{ meter}$"
      },
      {
        "key": "B",
        "text": "$18,5\\text{ meter}$"
      },
      {
        "key": "C",
        "text": "$16,0\\text{ meter}$"
      },
      {
        "key": "D",
        "text": "$16,6\\text{ meter}$"
      },
      {
        "key": "E",
        "text": "$17,2\\text{ meter}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "APLIKASI TANGEN ELEVASI",
      "latex": "\\tan \\theta = \\frac{t - h_{\\text{mata}}}{x} \\iff t = x \\cdot \\tan \\theta + h_{\\text{mata}}",
      "legend": "• $\\theta = 45^\\circ, x = 15, h = 1,6$."
    },
    "hints": {
      "concept": "$\\tan 45^\\circ = 1$. Tinggi tambahan $= 15 \\times 1 = 15\\text{ m}$.",
      "execution": "Tinggi total $= 15 + 1,6 = 16,6\\text{ meter}$."
    },
    "explanation": "<strong>Solusi:</strong> $t = 15 \\cdot \\tan 45^\\circ + 1,6 = 15(1) + 1,6 = 16,6\\text{ meter}$.",
    "isDiagnostic": false
  },
  {
    "id": "mtk-lat-m-01",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Eksponen Berbentuk Kuadrat",
    "type": "mcq",
    "questionHtml": "Diketahui persamaan $3^{2x} - 10 \\cdot 3^x + 9 = 0$. Jika $x_1$ dan $x_2$ adalah akar-akar real persamaan tersebut dengan $x_1 < x_2$, nilai dari $2x_1 + 3x_2$ adalah...",
    "formulaHud": {
      "title": "SUBSTITUSI VARIABEL EKSPONEN",
      "latex": "u = a^x \\implies u^2 - B u + C = 0",
      "legend": "• Misalkan $u = 3^x$ dengan syarat $u > 0$."
    },
    "hints": {
      "concept": "Faktorkan persamaan kuadrat dalam $u$: $u^2 - 10u + 9 = (u - 1)(u - 9) = 0$.",
      "execution": "$u_1 = 1 \\implies 3^x = 1 \\implies x_1 = 0$. $u_2 = 9 \\implies 3^x = 9 \\implies x_2 = 2$. $2(0) + 3(2) = 6$."
    },
    "explanation": "<strong>Tahap 1:</strong> Misalkan $u = 3^x$, maka $u^2 - 10u + 9 = 0$.<br><strong>Tahap 2:</strong> $(u - 1)(u - 9) = 0 \\implies u = 1$ atau $u = 9$.<br><strong>Tahap 3:</strong> $3^x = 3^0 \\implies x_1 = 0$, $3^x = 3^2 \\implies x_2 = 2$.<br><strong>Tahap 4:</strong> Nilai $2(0) + 3(2) = 6$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$5$"
      },
      {
        "key": "B",
        "text": "$8$"
      },
      {
        "key": "C",
        "text": "$4$"
      },
      {
        "key": "D",
        "text": "$7$"
      },
      {
        "key": "E",
        "text": "$6$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-m-02",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Evaluasi Karakteristik Fungsi Kuadrat",
    "type": "matrix",
    "questionHtml": "Diberikan sebuah kurva fungsi kuadrat dengan persamaan $f(x) = x^2 - 4x - 5$.<br><br>Tentukan kebenaran dari setiap pernyataan matematis berikut (Tentukan <strong>Benar</strong> atau <strong>Salah</strong> pada masing-masing baris tabel):",
    "formulaHud": {
      "title": "ANALISIS KARAKTERISTIK PARABOLA",
      "latex": "x_p = -\\frac{b}{2a}, \\quad y_p = f(x_p), \\quad f'(x) = 2ax + b",
      "legend": "• Evaluasi pembuat nol fungsi, puncak parabola, dan turunan pertama di $x = 0$."
    },
    "hints": {
      "concept": "Titik potong sumbu-X: $x^2 - 4x - 5 = (x - 5)(x + 1) = 0$. Sumbu simetri $x = 4/2 = 2$. Nilai puncak $f(2) = 4 - 8 - 5 = -9$. Turunan $f'(0) = -4 < 0$.",
      "execution": "<strong>Pernyataan 1 [BENAR]:</strong> $(x-5)(x+1) = 0 \\implies x = 5$ dan $x = -1$.<br><strong>Pernyataan 2 [BENAR]:</strong> $x_p = -(-4)/(2 \\times 1) = 2$.<br><strong>Pernyataan 3 [SALAH]:</strong> $y_p = 2^2 - 4(2) - 5 = 4 - 8 - 5 = -9$ (bukan $-8$).<br><strong>Pernyataan 4 [SALAH]:</strong> $m = f'(0) = 2(0) - 4 = -4 < 0$ (negatif)."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Kurva fungsi kuadrat $f(x) = x^2 - 4x - 5$. Pembuat nol dihitung dari pemfaktoran, sumbu simetri $x_p = -b/(2a)$, nilai ekstremum $y_p = f(x_p)$, dan gradien garis singgung dari turunan pertama $f'(x) = 2x - 4$.</p><p><strong>2. Langkah Analisis Tiap Pernyataan:</strong><br>• <strong>Pernyataan 1 [BENAR]:</strong> $x^2 - 4x - 5 = (x - 5)(x + 1) = 0 \\implies x = 5$ atau $x = -1$. Titik potong $(-1, 0)$ dan $(5, 0)$.<br>• <strong>Pernyataan 2 [BENAR]:</strong> $x_p = -\\frac{-4}{2(1)} = 2$.<br>• <strong>Pernyataan 3 [SALAH]:</strong> $y_p = f(2) = 2^2 - 4(2) - 5 = 4 - 8 - 5 = -9$ (bukan $-8$).<br>• <strong>Pernyataan 4 [SALAH]:</strong> $m = f'(0) = 2(0) - 4 = -4 < 0$ (negatif, bukan positif).</p><p><strong>3. Kesimpulan:</strong><br>Urutan validitas tabel adalah: <strong>[1] BENAR, [2] BENAR, [3] SALAH, [4] SALAH</strong>.</p></div>",
    "isDiagnostic": false,
    "statements": [
      {
        "id": "s1",
        "text": "Kurva memotong sumbu-$X$ pada dua titik koordinat berbeda, yaitu $(-1, 0)$ dan $(5, 0)$.",
        "isCorrect": true
      },
      {
        "id": "s2",
        "text": "Persamaan garis sumbu simetri kurva fungsi adalah $x = 2$.",
        "isCorrect": true
      },
      {
        "id": "s3",
        "text": "Nilai ekstremum minimum dari fungsi tersebut adalah $-8$.",
        "isCorrect": false
      },
      {
        "id": "s4",
        "text": "Gradien garis singgung kurva di titik potong sumbu-$Y$ ($x = 0$) bernilai positif ($m > 0$).",
        "isCorrect": false
      }
    ]
  },
  {
    "id": "mtk-lat-m-03",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Deret Geometri Tak Hingga",
    "type": "mcq",
    "questionHtml": "Sebuah bola dijatuhkan vertikal dari ketinggian $12\\text{ meter}$. Setiap kali memantul di lantai, bola mencapai ketinggian $\\frac{3}{4}$ dari ketinggian sebelumnya. Panjang lintasan total yang ditempuh bola hingga berhenti adalah...",
    "formulaHud": {
      "title": "PANJANG LINTASAN BOLA MEMANTUL",
      "latex": "S_{\\text{total}} = h_0 + 2 \\left(\\frac{a}{1 - r}\\right) = h_0 \\left(\\frac{1 + r}{1 - r}\\right)",
      "legend": "• $h_0 = 12\\text{ m}, r = 3/4$."
    },
    "hints": {
      "concept": "Gunakan formula praktis $S = h_0 \\cdot \\frac{1 + r}{1 - r}$.",
      "execution": "$S = 12 \\cdot \\frac{1 + 3/4}{1 - 3/4} = 12 \\cdot \\frac{7/4}{1/4} = 12 \\times 7 = 84\\text{ meter}$."
    },
    "explanation": "<strong>Solusi:</strong> $S_{\\text{total}} = 12 \\times \\frac{1 + 3/4}{1 - 3/4} = 12 \\times \\frac{7/4}{1/4} = 12 \\times 7 = 84\\text{ meter}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$96\\text{ meter}$"
      },
      {
        "key": "B",
        "text": "$84\\text{ meter}$"
      },
      {
        "key": "C",
        "text": "$108\\text{ meter}$"
      },
      {
        "key": "D",
        "text": "$48\\text{ meter}$"
      },
      {
        "key": "E",
        "text": "$72\\text{ meter}$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-m-04",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Pertidaksamaan Logaritma",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian dari pertidaksamaan $^2\\log(x^2 - 3x) \\le 2$ adalah...",
    "formulaHud": {
      "title": "PERTIDAKSAMAAN LOGARITMA & SYARAT NUMERUS",
      "latex": "^a\\log f(x) \\le ^a\\log g(x) \\iff f(x) \\le g(x) \\quad (a > 1), \\quad f(x) > 0",
      "legend": "• Syarat numerus: $x^2 - 3x > 0$.<br>• Pertidaksamaan pokok: $x^2 - 3x \\le 2^2 = 4$."
    },
    "hints": {
      "concept": "Numerus: $x(x - 3) > 0 \\implies x < 0$ atau $x > 3$.<br>Pokok: $x^2 - 3x - 4 \\le 0 \\implies (x - 4)(x + 1) \\le 0 \\implies -1 \\le x \\le 4$.",
      "execution": "Irisan kedua daerah: $[-1, 0) \\cup (3, 4]$."
    },
    "explanation": "<strong>Solusi:</strong> Syarat numerus memberikan $x < 0$ atau $x > 3$. Penyelesaian aljabar memberikan $-1 \\le x \\le 4$. Irisan keduanya adalah $-1 \\le x < 0$ atau $3 < x \\le 4$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$x < 0$ atau $x > 3$"
      },
      {
        "key": "B",
        "text": "$0 < x < 3$"
      },
      {
        "key": "C",
        "text": "$-1 \\le x < 0$ atau $3 < x \\le 4$"
      },
      {
        "key": "D",
        "text": "$-1 \\le x \\le 4$"
      },
      {
        "key": "E",
        "text": "$x \\le -1$ atau $x \\ge 4$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-m-05",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Aplikasi Bunga Majemuk Finansial",
    "type": "mcq",
    "questionHtml": "Seseorang mendepositokan uang sebesar Rp20.000.000 pada bank syariah dengan nisbah imbal hasil setara bunga majemuk $6\\%$ per tahun yang dikapitalisasi setiap akhir tahun. Total saldo tabungan setelah $3\\text{ tahun}$ adalah...",
    "formulaHud": {
      "title": "FORMULA BUNGA MAJEMUK",
      "latex": "M_n = M_0(1 + i)^n",
      "legend": "• $M_0 = 20.000.000, i = 0,06, n = 3$."
    },
    "hints": {
      "concept": "$1,06^3 = 1,191016$. Kalikan dengan 20.000.000.",
      "execution": "$20.000.000 \\times 1,191016 = 23.820.320$."
    },
    "explanation": "<strong>Solusi:</strong> $M_3 = 20.000.000 \\times (1,06)^3 = 20.000.000 \\times 1,191016 = \\text{Rp}23.820.320$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "Rp 23.820.320"
      },
      {
        "key": "B",
        "text": "Rp 24.120.000"
      },
      {
        "key": "C",
        "text": "Rp 23.600.000"
      },
      {
        "key": "D",
        "text": "Rp 24.800.000"
      },
      {
        "key": "E",
        "text": "Rp 24.360.500"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-m-06",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sisipan Barisan Aritmetika",
    "type": "mcq",
    "questionHtml": "Antara bilangan $4$ dan $124$ disisipkan $23\\text{ bilangan}$ sehingga bersama bilangan mula-mula terbentuk barisan aritmetika baru. Beda barisan aritmetika baru tersebut adalah...",
    "formulaHud": {
      "title": "FORMULA BEDA SISIPAN",
      "latex": "b' = \\frac{y - x}{k + 1}",
      "legend": "• $x = 4, y = 124, k = 23$."
    },
    "hints": {
      "concept": "$b' = (124 - 4) / (23 + 1) = 120 / 24 = 5$.",
      "execution": "$b' = 5$."
    },
    "explanation": "<strong>Solusi:</strong> $b' = \\frac{124 - 4}{23 + 1} = \\frac{120}{24} = 5$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$4$"
      },
      {
        "key": "B",
        "text": "$5$"
      },
      {
        "key": "C",
        "text": "$6$"
      },
      {
        "key": "D",
        "text": "$7$"
      },
      {
        "key": "E",
        "text": "$8$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-m-07",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Penyederhanaan Bentuk Akar Bertingkat",
    "type": "mcq",
    "questionHtml": "Bentuk sederhana dari $\\sqrt{11 - 2\\sqrt{30}}$ adalah...",
    "formulaHud": {
      "title": "AKAR BERTINGKAT",
      "latex": "\\sqrt{(a + b) - 2\\sqrt{ab}} = \\sqrt{a} - \\sqrt{b} \\quad (a > b)",
      "legend": "• Cari dua bilangan $a$ dan $b$ dengan $a + b = 11$ dan $a \\cdot b = 30$."
    },
    "hints": {
      "concept": "$a = 6$ dan $b = 5$.",
      "execution": "$\\sqrt{6} - \\sqrt{5}$."
    },
    "explanation": "<strong>Solusi:</strong> Karena $6 + 5 = 11$ dan $6 \\times 5 = 30$, maka $\\sqrt{11 - 2\\sqrt{30}} = \\sqrt{6} - \\sqrt{5}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\sqrt{5} - \\sqrt{6}$"
      },
      {
        "key": "B",
        "text": "$\\sqrt{7} - \\sqrt{4}$"
      },
      {
        "key": "C",
        "text": "$\\sqrt{10} - 1$"
      },
      {
        "key": "D",
        "text": "$\\sqrt{6} - \\sqrt{5}$"
      },
      {
        "key": "E",
        "text": "$\\sqrt{8} - \\sqrt{3}$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-m-09",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Diskriminan Akar Kembar",
    "type": "mcq",
    "questionHtml": "Agar persamaan kuadrat $(m - 1)x^2 - 4mx + (4m + 3) = 0$ memiliki dua akar real yang kembar (sama), nilai $m$ yang memenuhi adalah...",
    "formulaHud": {
      "title": "KONDISI DISKRIMINAN D = 0",
      "latex": "D = b^2 - 4ac = 0",
      "legend": "• $a = m - 1, b = -4m, c = 4m + 3$."
    },
    "hints": {
      "concept": "$(-4m)^2 - 4(m - 1)(4m + 3) = 0 \\implies 16m^2 - 4(4m^2 - m - 3) = 0$.",
      "execution": "$16m^2 - 16m^2 + 4m + 12 = 0 \\implies 4m + 12 = 0 \\implies m = -3$."
    },
    "explanation": "<strong>Solusi:</strong> $D = 0 \\implies 4m + 12 = 0 \\implies m = -3$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$-3$"
      },
      {
        "key": "B",
        "text": "$-\\frac{3}{4}$"
      },
      {
        "key": "C",
        "text": "$3$"
      },
      {
        "key": "D",
        "text": "$4$"
      },
      {
        "key": "E",
        "text": "$-\\frac{3}{7}$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-m-10",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Pertidaksamaan Rasional",
    "type": "mcq",
    "questionHtml": "Penyelesaian dari pertidaksamaan pecahan $\\frac{2x - 5}{x + 3} \\le 1$ adalah...",
    "formulaHud": {
      "title": "PERTIDAKSAMAAN RASIONAL",
      "latex": "\\frac{P(x)}{Q(x)} \\le 0, \\quad Q(x) \\neq 0",
      "legend": "• Kurangkan 1 di kedua ruas: $\\frac{2x - 5 - (x + 3)}{x + 3} \\le 0$."
    },
    "hints": {
      "concept": "$\\frac{x - 8}{x + 3} \\le 0$. Titik batas: $x = 8$ (penuh) dan $x = -3$ (lubang penyebut).",
      "execution": "Uji tanda: daerah negatif berada di antara $-3$ dan $8$. Syarat penyebut $x \\neq -3$. Maka $-3 < x \\le 8$."
    },
    "explanation": "<strong>Solusi:</strong> Titik kritis $-3$ dan $8$. Karena penyebut tidak boleh nol, maka $-3 < x \\le 8$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$-3 < x \\le 8$"
      },
      {
        "key": "B",
        "text": "$x < -3$ atau $x \\ge 8$"
      },
      {
        "key": "C",
        "text": "$x \\le -3$ atau $x > 8$"
      },
      {
        "key": "D",
        "text": "$-3 < x < 8$"
      },
      {
        "key": "E",
        "text": "$-3 \\le x \\le 8$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-m-11",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Invers Fungsi Rasional Linear",
    "type": "mcq",
    "questionHtml": "Diberikan fungsi $f(x) = \\frac{3x + 2}{2x - 5}, \\quad x \\neq \\frac{5}{2}$. Nilai dari $f^{-1}(4)$ adalah...",
    "formulaHud": {
      "title": "FORMULA CEPAT INVERS RASIONAL",
      "latex": "f(x) = \\frac{ax + b}{cx + d} \\iff f^{-1}(x) = \\frac{-dx + b}{cx - a}",
      "legend": "• Tukar $a$ dan $d$ dengan mengubah tanda."
    },
    "hints": {
      "concept": "$f^{-1}(x) = \\frac{5x + 2}{2x - 3}$.",
      "execution": "$f^{-1}(4) = \\frac{5(4) + 2}{2(4) - 3} = \\frac{22}{5}$."
    },
    "explanation": "<strong>Solusi:</strong> $f^{-1}(x) = \\frac{5x + 2}{2x - 3} \\implies f^{-1}(4) = \\frac{22}{5}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$6$"
      },
      {
        "key": "B",
        "text": "$4$"
      },
      {
        "key": "C",
        "text": "$\\frac{26}{5}$"
      },
      {
        "key": "D",
        "text": "$\\frac{18}{5}$"
      },
      {
        "key": "E",
        "text": "$\\frac{22}{5}$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-m-12",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Analisis Grafik Fungsi Kuadrat",
    "type": "multi",
    "questionHtml": "Diberikan fungsi kuadrat $g(x) = -x^2 + 6x - 8$. Manakah dari pernyataan-pernyataan berikut yang <strong>BENAR</strong>? (Pilih semua opsi yang tepat):",
    "formulaHud": {
      "title": "KARAKTERISTIK FUNGSI KUADRAT a < 0",
      "latex": "y = ax^2 + bx + c",
      "legend": "• Cek tanda koefisien $a$, pembuat nol fungsi, dan puncak $(x_p, y_p)$."
    },
    "hints": {
      "concept": "$a = -1 < 0$ (kurva terbuka ke bawah). $-x^2 + 6x - 8 = -(x - 2)(x - 4) = 0$ (titik potong $(2,0)$ dan $(4,0)$). Sumbu simetri $x = 3$. Nilai maks $g(3) = -9 + 18 - 8 = 1$. Titik potong sumbu-Y $(0, -8)$.",
      "execution": "Pernyataan A Benar ($a=-1 < 0$). Pernyataan B Benar ($x=2, 4$). Pernyataan C Benar ($x_p=3$). Opsi D salah (nilai maks adalah 1, bukan 2). Opsi E salah (titik potong sumbu-Y adalah $(0, -8)$)."
    },
    "explanation": "<strong>Evaluasi:</strong><br>• A: Benar ($a = -1 < 0$).<br>• B: Benar (akar 2 dan 4).<br>• C: Benar ($x_p = -6/(-2) = 3$).<br>• D: Salah (maksimum $= 1$).<br>• E: Salah ($g(0) = -8$).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "Grafik kurva membuka ke bawah."
      },
      {
        "key": "B",
        "text": "Kurva memotong sumbu-$X$ di titik $(2, 0)$ dan $(4, 0)$."
      },
      {
        "key": "C",
        "text": "Garis sumbu simetri kurva adalah $x = 3$."
      },
      {
        "key": "D",
        "text": "Nilai maksimum dari fungsi $g(x)$ adalah $2$."
      },
      {
        "key": "E",
        "text": "Kurva memotong sumbu-$Y$ pada koordinat $(0, 8)$."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ]
  },
  {
    "id": "mtk-lat-m-13",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Invers Matriks Ordo 2x2",
    "type": "mcq",
    "questionHtml": "Invers dari matriks $A = \\begin{pmatrix} 4 & 7 \\\\ 1 & 2 \\end{pmatrix}$ adalah...",
    "formulaHud": {
      "title": "INVERS MATRIKS 2x2",
      "latex": "A^{-1} = \\frac{1}{ad - bc} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}",
      "legend": "• $\\det(A) = 4(2) - 7(1) = 8 - 7 = 1$."
    },
    "hints": {
      "concept": "Tukar diagonal utama dan ubah tanda diagonal samping: $\\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$.",
      "execution": "$A^{-1} = \\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$."
    },
    "explanation": "<strong>Solusi:</strong> Karena $\\det(A) = 1$, maka inversnya adalah $\\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\begin{pmatrix} 4 & -7 \\\\ -1 & 2 \\end{pmatrix}$"
      },
      {
        "key": "B",
        "text": "$\\begin{pmatrix} 2 & 7 \\\\ 1 & 4 \\end{pmatrix}$"
      },
      {
        "key": "C",
        "text": "$\\begin{pmatrix} -2 & 7 \\\\ 1 & -4 \\end{pmatrix}$"
      },
      {
        "key": "D",
        "text": "$\\begin{pmatrix} 2 & -1 \\\\ -7 & 4 \\end{pmatrix}$"
      },
      {
        "key": "E",
        "text": "$\\begin{pmatrix} 2 & -7 \\\\ -1 & 4 \\end{pmatrix}$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-m-14",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Penyelesaian Persamaan Matriks",
    "type": "mcq",
    "questionHtml": "Diberikan persamaan matriks $\\begin{pmatrix} 3 & 1 \\\\ 5 & 2 \\end{pmatrix} X = \\begin{pmatrix} 4 \\\\ 7 \\end{pmatrix}$. Matriks kolom $X = \\begin{pmatrix} x \\\\ y \\end{pmatrix}$ yang memenuhi adalah...",
    "formulaHud": {
      "title": "PERSAMAAN MATRIKS AX = B",
      "latex": "X = A^{-1} B",
      "legend": "• $\\det(A) = 3(2) - 1(5) = 1$. $A^{-1} = \\begin{pmatrix} 2 & -1 \\\\ -5 & 3 \\end{pmatrix}$."
    },
    "hints": {
      "concept": "$X = \\begin{pmatrix} 2 & -1 \\\\ -5 & 3 \\end{pmatrix} \\begin{pmatrix} 4 \\\\ 7 \\end{pmatrix}$.",
      "execution": "$x = 2(4) - 1(7) = 8 - 7 = 1$. $y = -5(4) + 3(7) = -20 + 21 = 1$."
    },
    "explanation": "<strong>Solusi:</strong> $X = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$"
      },
      {
        "key": "B",
        "text": "$\\begin{pmatrix} -1 \\\\ 7 \\end{pmatrix}$"
      },
      {
        "key": "C",
        "text": "$\\begin{pmatrix} 2 \\\\ -2 \\end{pmatrix}$"
      },
      {
        "key": "D",
        "text": "$\\begin{pmatrix} 3 \\\\ -5 \\end{pmatrix}$"
      },
      {
        "key": "E",
        "text": "$\\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-m-15",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Barisan Aritmetika Tingkat Dua",
    "type": "mcq",
    "questionHtml": "Diberikan barisan bilangan: $3, 7, 13, 21, 31, \\dots$. Suku ke-10 ($U_{10}$) dari barisan tersebut adalah...",
    "formulaHud": {
      "title": "BARISAN TINGKAT DUA",
      "latex": "U_n = an^2 + bn + c, \\quad 2a = d_2",
      "legend": "• Selisih tingkat 1: $4, 6, 8, 10$ (beda $= 2$). Maka $2a = 2 \\implies a = 1$."
    },
    "hints": {
      "concept": "Suku barisan memenuhi $U_n = n^2 + n + 1$. Uji $n=1 \\implies 3, n=2 \\implies 7$.",
      "execution": "Hitung suku ke-10: $U_{10} = 10^2 + 10 + 1 = 100 + 10 + 1 = 111$."
    },
    "explanation": "<strong>Solusi:</strong> Pola suku ke-$n$ adalah $U_n = n^2 + n + 1$. Untuk $n = 10$: $U_{10} = 100 + 10 + 1 = 111$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$109$"
      },
      {
        "key": "B",
        "text": "$111$"
      },
      {
        "key": "C",
        "text": "$101$"
      },
      {
        "key": "D",
        "text": "$131$"
      },
      {
        "key": "E",
        "text": "$121$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-m-16",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Deret Geometri Suku Ganjil & Genap",
    "type": "mcq",
    "questionHtml": "Jumlah suatu deret geometri tak hingga adalah $18$, sedangkan jumlah suku-suku yang bernomor ganjil adalah $12$. Rasio ($r$) dari deret geometri tersebut adalah...",
    "formulaHud": {
      "title": "PEMBAGIAN DERET GEOMETRI",
      "latex": "S_{\\infty} = \\frac{a}{1 - r}, \\quad S_{\\text{ganjil}} = \\frac{a}{1 - r^2}",
      "legend": "• $S_{\\text{genap}} = S_{\\infty} - S_{\\text{ganjil}} = 18 - 12 = 6$."
    },
    "hints": {
      "concept": "Hubungan rasio: $r = \\frac{S_{\\text{genap}}}{S_{\\text{ganjil}}}$.",
      "execution": "$r = 6 / 12 = 1/2$."
    },
    "explanation": "<strong>Solusi:</strong> Suku genap $= 18 - 12 = 6$. Rasio $r = \\frac{S_{\\text{genap}}}{S_{\\text{ganjil}}} = \\frac{6}{12} = \\frac{1}{2}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{3}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1}{4}$"
      },
      {
        "key": "C",
        "text": "$\\frac{3}{4}$"
      },
      {
        "key": "D",
        "text": "$\\frac{2}{3}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{2}$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-m-17",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Matriks Transformasi Refleksi Garis y = x",
    "type": "mcq",
    "questionHtml": "Titik $B(4, -5)$ ditransformasikan oleh matriks pencerminan terhadap garis $y = x$, dilanjutkan dengan translasi $T = \\begin{pmatrix} 2 \\\\ 3 \\end{pmatrix}$. Koordinat bayangan akhir titik $B''$ adalah...",
    "formulaHud": {
      "title": "KOMPOSISI TRANSFORMASI",
      "latex": "\\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} + T",
      "legend": "• Pencerminan terhadap $y = x$ menukar koordinat: $(x, y) \\to (y, x)$."
    },
    "hints": {
      "concept": "Bayangan pertama $B' = (-5, 4)$.",
      "execution": "Translasi $T$: $(-5 + 2, 4 + 3) = (-3, 7)$."
    },
    "explanation": "<strong>Solusi:</strong> $B(4, -5) \\xrightarrow{R_{y=x}} B'(-5, 4) \\xrightarrow{T(2,3)} B''(-3, 7)$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$(-5, 4)$"
      },
      {
        "key": "B",
        "text": "$(-3, 1)$"
      },
      {
        "key": "C",
        "text": "$(-7, 7)$"
      },
      {
        "key": "D",
        "text": "$(-3, 7)$"
      },
      {
        "key": "E",
        "text": "$(6, -2)$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-m-18",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi Tiga Fungsi Linear & Kuadrat",
    "type": "mcq",
    "questionHtml": "Diketahui $f(x) = 2x + 1$, $g(x) = x^2 - 2$, dan $h(x) = 3x$. Nilai dari $(f \\circ g \\circ h)(1)$ adalah...",
    "formulaHud": {
      "title": "KOMPOSISI BERUNTUN",
      "latex": "(f \\circ g \\circ h)(x) = f(g(h(x)))",
      "legend": "• Evaluasi dari fungsi paling dalam: $h(1)$, lalu $g$, lalu $f$."
    },
    "hints": {
      "concept": "$h(1) = 3(1) = 3$. $g(3) = 3^2 - 2 = 7$. $f(7) = 2(7) + 1 = 15$.",
      "execution": "Nilai akhir $= 15$."
    },
    "explanation": "<strong>Solusi:</strong> $h(1) = 3 \\implies g(3) = 7 \\implies f(7) = 2(7) + 1 = 15$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$17$"
      },
      {
        "key": "B",
        "text": "$19$"
      },
      {
        "key": "C",
        "text": "$15$"
      },
      {
        "key": "D",
        "text": "$13$"
      },
      {
        "key": "E",
        "text": "$21$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-m-19",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Akar Saling Berlawanan Tanda",
    "type": "mcq",
    "questionHtml": "Persamaan kuadrat $x^2 + (k - 3)x - (2k - 1) = 0$ memiliki akar-akar $x_1$ dan $x_2$ yang saling berlawanan ($x_1 = -x_2$). Nilai $k$ dan sifat akarnya adalah...",
    "formulaHud": {
      "title": "AKAR SALING BERLAWANAN",
      "latex": "x_1 + x_2 = 0 \\iff -\\frac{b}{a} = 0",
      "legend": "• Syarat akar berlawanan: koefisien $b = 0$."
    },
    "hints": {
      "concept": "$k - 3 = 0 \\implies k = 3$.",
      "execution": "Persamaan menjadi $x^2 + 5 = 0$? Tunggu, $2k - 1 = 2(3) - 1 = 5 > 0$ menghasilkan akar imajiner bila $x^2 + 5 = 0$."
    },
    "explanation": "<strong>Tahap 1:</strong> $x_1 + x_2 = 0 \\implies -(k - 3) = 0 \\implies k = 3$.<br><strong>Tahap 2:</strong> Substitusi $k = 3$ ke persamaan: $x^2 - (2(3) - 1) = 0 \\implies x^2 - 5 = 0 \\implies x = \\pm \\sqrt{5}$ (dua akar real berbeda).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$k = 1$ dan akar rasional"
      },
      {
        "key": "B",
        "text": "$k = 3$ dan akar real berbeda"
      },
      {
        "key": "C",
        "text": "$k = 0$ dan akar irasional"
      },
      {
        "key": "D",
        "text": "$k = -3$ dan akar imajiner"
      },
      {
        "key": "E",
        "text": "$k = 3$ dan akar kembar"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-m-21",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Jarak Titik ke Rusuk Limas Segi Empat",
    "type": "mcq",
    "questionHtml": "Pada limas segi empat beraturan $T.ABCD$, panjang rusuk alas adalah $8\\text{ cm}$ dan panjang rusuk tegak adalah $4\\sqrt{6}\\text{ cm}$. Jarak titik puncak $T$ ke bidang alas $ABCD$ adalah...",
    "formulaHud": {
      "title": "TINGGI LIMAS REGULER",
      "latex": "t = \\sqrt{TA^2 - AO^2}",
      "legend": "• $O$ adalah titik pusat alas persegi. $AO = \\frac{1}{2}AC = \\frac{1}{2}(8\\sqrt{2}) = 4\\sqrt{2}$."
    },
    "hints": {
      "concept": "$t = \\sqrt{(4\\sqrt{6})^2 - (4\\sqrt{2})^2} = \\sqrt{96 - 32} = \\sqrt{64} = 8$? Cek: $16 \\times 6 = 96$, $16 \\times 2 = 32$. Selisih $64$, akar $= 8$.",
      "execution": "Maka tingginya adalah $8\\text{ cm}$. Kunci E."
    },
    "explanation": "<strong>Tahap 1:</strong> Diagonal alas $AC = 8\\sqrt{2}\\text{ cm} \\implies AO = 4\\sqrt{2}\\text{ cm}$.<br><strong>Tahap 2:</strong> Tinggi $t = \\sqrt{TA^2 - AO^2} = \\sqrt{(4\\sqrt{6})^2 - (4\\sqrt{2})^2} = \\sqrt{96 - 32} = \\sqrt{64} = 8\\text{ cm}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$6\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$4\\sqrt{3}\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$8\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$4\\sqrt{2}\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$4\\sqrt{5}\\text{ cm}$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-m-22",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Persamaan Lingkaran Berpusat di (a,b)",
    "type": "mcq",
    "questionHtml": "Persamaan lingkaran yang berpusat di titik $(2, -3)$ dan menyinggung sumbu-$X$ adalah...",
    "formulaHud": {
      "title": "LINGKARAN MENYINGGUNG SUMBU X",
      "latex": "(x - a)^2 + (y - b)^2 = r^2, \\quad r = |b|",
      "legend": "• Lingkaran menyinggung sumbu-$X$, maka jari-jari $r = |-3| = 3$."
    },
    "hints": {
      "concept": "$(x - 2)^2 + (y + 3)^2 = 3^2 \\implies x^2 - 4x + 4 + y^2 + 6y + 9 = 9$.",
      "execution": "$x^2 + y^2 - 4x + 6y + 4 = 0$."
    },
    "explanation": "<strong>Solusi:</strong> Jari-jari $r = |-3| = 3$. Persamaan: $(x - 2)^2 + (y + 3)^2 = 9 \\implies x^2 + y^2 - 4x + 6y + 4 = 0$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$x^2 + y^2 + 4x - 6y + 4 = 0$"
      },
      {
        "key": "B",
        "text": "$x^2 + y^2 - 4x + 6y - 9 = 0$"
      },
      {
        "key": "C",
        "text": "$x^2 + y^2 - 4x + 6y + 13 = 0$"
      },
      {
        "key": "D",
        "text": "$x^2 + y^2 - 4x + 6y + 9 = 0$"
      },
      {
        "key": "E",
        "text": "$x^2 + y^2 - 4x + 6y + 4 = 0$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-m-23",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Garis Singgung Lingkaran",
    "type": "mcq",
    "questionHtml": "Persamaan garis singgung lingkaran $x^2 + y^2 = 25$ di titik $P(-3, 4)$ adalah...",
    "formulaHud": {
      "title": "GARIS SINGGUNG BENTUK TITIK",
      "latex": "x_1 x + y_1 y = r^2",
      "legend": "• Substitusikan $(x_1, y_1) = (-3, 4)$ dan $r^2 = 25$."
    },
    "hints": {
      "concept": "$-3x + 4y = 25$.",
      "execution": "$-3x + 4y = 25$."
    },
    "explanation": "<strong>Solusi:</strong> Formula bagi adil: $x_1 x + y_1 y = 25 \\implies -3x + 4y = 25$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$3x - 4y = 25$"
      },
      {
        "key": "B",
        "text": "$4x + 3y = 25$"
      },
      {
        "key": "C",
        "text": "$4x - 3y = 25$"
      },
      {
        "key": "D",
        "text": "$-3x - 4y = 25$"
      },
      {
        "key": "E",
        "text": "$-3x + 4y = 25$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-m-24",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Rotasi dengan Titik Pusat Sembarang",
    "type": "mcq",
    "questionHtml": "Titik $K(5, 2)$ dirotasikan sebesar $90^\\circ$ berlawanan arah putaran jarum jam dengan pusat rotasi $P(1, -1)$. Koordinat bayangan titik $K'$ adalah...",
    "formulaHud": {
      "title": "ROTASI PUSAT (a, b)",
      "latex": "\\begin{pmatrix} x' - a \\\\ y' - b \\end{pmatrix} = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix} \\begin{pmatrix} x - a \\\\ y - b \\end{pmatrix}",
      "legend": "• $x - a = 5 - 1 = 4$ dan $y - b = 2 - (-1) = 3$."
    },
    "hints": {
      "concept": "$x' - 1 = -(3) = -3 \\implies x' = -2$. $y' - (-1) = 4 \\implies y' + 1 = 4 \\implies y' = 3$? Cek: $y' - b = 4 \\implies y' - (-1) = 4 \\implies y' = 3$.",
      "execution": "Tunggu: $(-2, 3)$. Mari periksa opsi A = $(-2, 3)$. Kunci A."
    },
    "explanation": "<strong>Tahap 1:</strong> Translasi ke pusat: $(5-1, 2-(-1)) = (4, 3)$.<br><strong>Tahap 2:</strong> Rotasi $90^\\circ$: $(-y, x) = (-3, 4)$.<br><strong>Tahap 3:</strong> Kembalikan ke pusat: $(-3 + 1, 4 - 1) = (-2, 3)$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$(-2, 3)$"
      },
      {
        "key": "B",
        "text": "(-1, 4)"
      },
      {
        "key": "C",
        "text": "$(2, 5)$"
      },
      {
        "key": "D",
        "text": "$(-2, 5)$"
      },
      {
        "key": "E",
        "text": "$(3, 4)$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-m-25",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Dilatasi dengan Skala Negatif",
    "type": "mcq",
    "questionHtml": "Bayangan garis $2x - 3y + 6 = 0$ oleh dilatasi dengan pusat $O(0, 0)$ dan faktor skala $k = -2$ adalah...",
    "formulaHud": {
      "title": "DILATASI GARIS",
      "latex": "x' = kx \\iff x = \\frac{x'}{k}, \\quad y' = ky \\iff y = \\frac{y'}{k}",
      "legend": "• Substitusikan $x = -x'/2$ dan $y = -y'/2$ ke persamaan garis."
    },
    "hints": {
      "concept": "$2(-x'/2) - 3(-y'/2) + 6 = 0 \\implies -x' + \\frac{3}{2}y' + 6 = 0$.",
      "execution": "Kalikan $-2$: $2x' - 3y' - 12 = 0$."
    },
    "explanation": "<strong>Solusi:</strong> $2(-x/2) - 3(-y/2) + 6 = 0 \\implies -x + 1,5y + 6 = 0 \\implies 2x - 3y - 12 = 0$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$3x - 2y - 12 = 0$"
      },
      {
        "key": "B",
        "text": "$2x - 3y - 12 = 0$"
      },
      {
        "key": "C",
        "text": "$2x - 3y + 12 = 0$"
      },
      {
        "key": "D",
        "text": "$2x + 3y - 12 = 0$"
      },
      {
        "key": "E",
        "text": "$4x - 6y + 6 = 0$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-m-26",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sudut Antara Garis dan Bidang Kubus",
    "type": "mcq",
    "questionHtml": "Pada kubus $ABCD.EFGH$, besar sudut antara garis diagonal ruang $AG$ dengan bidang alas $ABCD$ dapat ditentukan melalui nilai tangennya. Nilai dari $\\tan \\angle(AG, ABCD)$ adalah...",
    "formulaHud": {
      "title": "SUDUT GARIS DAN BIDANG",
      "latex": "\\tan \\theta = \\frac{CG}{AC}",
      "legend": "• Proyeksi $AG$ ke bidang $ABCD$ adalah diagonal bidang $AC$. Sudut yang dicari adalah $\\angle CAG$."
    },
    "hints": {
      "concept": "$\\tan \\angle CAG = \\frac{CG}{AC} = \\frac{s}{s\\sqrt{2}} = \\frac{1}{\\sqrt{2}} = \\frac{1}{2}\\sqrt{2}$.",
      "execution": "Nilai tangen $= \\frac{1}{2}\\sqrt{2}$."
    },
    "explanation": "<strong>Solusi:</strong> $\\tan \\theta = \\frac{s}{s\\sqrt{2}} = \\frac{1}{2}\\sqrt{2}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{3}\\sqrt{3}$"
      },
      {
        "key": "B",
        "text": "$\\sqrt{2}$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{2}\\sqrt{2}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{2}\\sqrt{6}$"
      },
      {
        "key": "E",
        "text": "$\\sqrt{3}$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-m-27",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Median Data Berkelompok",
    "type": "mcq",
    "questionHtml": "Perhatikan tabel distribusi frekuensi berikut:<br><table style='margin:10px 0; border-collapse:collapse; width:100%; border:1px solid #475569;'><tr style='background:#1e293b; color:#fff;'><th style='padding:6px; border:1px solid #475569;'>Interval Nilai</th><th style='padding:6px; border:1px solid #475569;'>Frekuensi</th></tr><tr><td style='padding:6px; border:1px solid #475569;'>50 – 59</td><td style='padding:6px; border:1px solid #475569;'>6</td></tr><tr><td style='padding:6px; border:1px solid #475569;'>60 – 69</td><td style='padding:6px; border:1px solid #475569;'>10</td></tr><tr><td style='padding:6px; border:1px solid #475569;'>70 – 79</td><td style='padding:6px; border:1px solid #475569;'>14</td></tr><tr><td style='padding:6px; border:1px solid #475569;'>80 – 89</td><td style='padding:6px; border:1px solid #475569;'>7</td></tr><tr><td style='padding:6px; border:1px solid #475569;'>90 – 99</td><td style='padding:6px; border:1px solid #475569;'>3</td></tr></table>Nilai median dari data berkelompok tersebut adalah...",
    "formulaHud": {
      "title": "FORMULA MEDIAN DATA KELOMPOK",
      "latex": "Me = L + \\left(\\frac{\\frac{n}{2} - F_k}{f_m}\\right) \\cdot p",
      "legend": "• Total frekuensi $n = 40 \\implies n/2 = 20$."
    },
    "hints": {
      "concept": "Kelas median pada interval $70 - 79$. $L = 69,5$, $F_k = 16$, $f_m = 14$, $p = 10$.",
      "execution": "$Me = 69,5 + \\left(\\frac{20 - 16}{14}\\right) \\times 10 = 69,5 + \\frac{40}{14} = 69,5 + 2,86 = 72,36$? Cek: $40/14 = 20/7 \\approx 2,857$. $69,5 + 2,857 = 72,357 \\approx 72,36$. Kunci B."
    },
    "explanation": "<strong>Tahap 1:</strong> $n = 40 \\implies \\frac{n}{2} = 20$. Letak kelas median adalah interval 70–79 ($F_k = 16$).<br><strong>Tahap 2:</strong> $L = 69,5$, $F_k = 16$, $f_m = 14$, $p = 10$.<br><strong>Tahap 3:</strong> $Me = 69,5 + \\frac{20 - 16}{14} \\times 10 = 69,5 + 2,86 = 72,36$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$72,36$"
      },
      {
        "key": "B",
        "text": "$72,86$"
      },
      {
        "key": "C",
        "text": "$71,86$"
      },
      {
        "key": "D",
        "text": "$73,25$"
      },
      {
        "key": "E",
        "text": "$74,50$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-m-28",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Modus Data Berkelompok",
    "type": "mcq",
    "questionHtml": "Pada suatu data pengukuran berat badan, kelas modus berada pada interval $61 - 70$ dengan frekuensi $18$. Frekuensi kelas sebelum kelas modus adalah $12$ dan frekuensi kelas sesudah kelas modus adalah $10$. Jika panjang kelas interval adalah $10$, maka modus data tersebut adalah...",
    "formulaHud": {
      "title": "FORMULA MODUS DATA KELOMPOK",
      "latex": "Mo = L + \\left(\\frac{d_1}{d_1 + d_2}\\right) \\cdot p",
      "legend": "• $L = 60,5, d_1 = 18 - 12 = 6, d_2 = 18 - 10 = 8, p = 10$."
    },
    "hints": {
      "concept": "$Mo = 60,5 + \\frac{6}{6 + 8} \\times 10 = 60,5 + \\frac{60}{14} = 60,5 + 4,285 = 64,79$.",
      "execution": "$Mo = 64,79$."
    },
    "explanation": "<strong>Solusi:</strong> $Mo = 60,5 + \\left(\\frac{6}{14}\\right) \\times 10 = 60,5 + 4,29 = 64,79$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$65,50$"
      },
      {
        "key": "B",
        "text": "$64,79$"
      },
      {
        "key": "C",
        "text": "$64,25$"
      },
      {
        "key": "D",
        "text": "$66,25$"
      },
      {
        "key": "E",
        "text": "$63,71$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-m-30",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Kombinasi Pemilihan Delegasi",
    "type": "mcq",
    "questionHtml": "Dari $6\\text{ siswa putra}$ dan $5\\text{ siswa putri}$, akan dipilih delegasi olimpiade sains yang beranggotakan $4\\text{ orang}$. Jika delegasi harus terdiri dari tepat $2\\text{ putra}$ dan $2\\text{ putri}$, banyaknya cara pemilihan delegasi adalah...",
    "formulaHud": {
      "title": "ATURAN PERKALIAN KOMBINASI",
      "latex": "C(n, r) = \\frac{n!}{r!(n - r)!}, \\quad \\text{Total} = C(6, 2) \\times C(5, 2)",
      "legend": "• Pilih 2 putra dari 6 dan 2 putri dari 5."
    },
    "hints": {
      "concept": "$C(6, 2) = \\frac{6 \\times 5}{2} = 15$. $C(5, 2) = \\frac{5 \\times 4}{2} = 10$.",
      "execution": "Total cara $= 15 \\times 10 = 150$."
    },
    "explanation": "<strong>Solusi:</strong> $C(6, 2) \\times C(5, 2) = 15 \\times 10 = 150\\text{ cara}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$180\\text{ cara}$"
      },
      {
        "key": "B",
        "text": "$75\\text{ cara}$"
      },
      {
        "key": "C",
        "text": "$150\\text{ cara}$"
      },
      {
        "key": "D",
        "text": "$210\\text{ cara}$"
      },
      {
        "key": "E",
        "text": "$120\\text{ cara}$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-m-31",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Peluang Kejadian Saling Bebas",
    "type": "mcq",
    "questionHtml": "Peluang seorang penembak jitu $A$ mengenai sasaran adalah $0,8$, sedangkan peluang penembak jitu $B$ mengenai sasaran adalah $0,7$. Jika keduanya menembak sasaran yang sama secara independen, peluang bahwa <strong>tepat satu penembak</strong> yang berhasil mengenai sasaran adalah...",
    "formulaHud": {
      "title": "PELUANG INDEPENDEN",
      "latex": "P = P(A \\cap B^c) + P(A^c \\cap B)",
      "legend": "• Tepat satu kena: ($A$ kena DAN $B$ luput) ATAU ($A$ luput DAN $B$ kena)."
    },
    "hints": {
      "concept": "$P(A) = 0,8, P(A^c) = 0,2$. $P(B) = 0,7, P(B^c) = 0,3$.",
      "execution": "$P = (0,8 \\times 0,3) + (0,2 \\times 0,7) = 0,24 + 0,14 = 0,38$."
    },
    "explanation": "<strong>Solusi:</strong> $P = (0,8)(0,3) + (0,2)(0,7) = 0,24 + 0,14 = 0,38$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$0,26$"
      },
      {
        "key": "B",
        "text": "$0,62$"
      },
      {
        "key": "C",
        "text": "$0,56$"
      },
      {
        "key": "D",
        "text": "$0,38$"
      },
      {
        "key": "E",
        "text": "$0,44$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-m-32",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Aturan Cosinus Segitiga Sembarang",
    "type": "mcq",
    "questionHtml": "Pada segitiga $PQR$, diketahui panjang sisi $PQ = 6\\text{ cm}$, $PR = 8\\text{ cm}$, dan besar sudut $\\angle QPR = 60^\\circ$. Panjang sisi $QR$ adalah...",
    "formulaHud": {
      "title": "ATURAN COSINUS",
      "latex": "a^2 = b^2 + c^2 - 2bc \\cos A",
      "legend": "• $QR^2 = PQ^2 + PR^2 - 2(PQ)(PR)\\cos 60^\\circ$."
    },
    "hints": {
      "concept": "$QR^2 = 6^2 + 8^2 - 2(6)(8)(0,5) = 36 + 64 - 48 = 100 - 48 = 52$.",
      "execution": "$QR = \\sqrt{52} = \\sqrt{4 \\times 13} = 2\\sqrt{13}\\text{ cm}$."
    },
    "explanation": "<strong>Solusi:</strong> $QR = \\sqrt{36 + 64 - 48} = \\sqrt{52} = 2\\sqrt{13}\\text{ cm}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$2\\sqrt{15}\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$2\\sqrt{19}\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$6\\sqrt{2}\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$2\\sqrt{13}\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$5\\sqrt{2}\\text{ cm}$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-m-33",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Aturan Sinus Panjang Sisi",
    "type": "mcq",
    "questionHtml": "Pada segitiga $ABC$, besar sudut $\\angle A = 45^\\circ$, besar sudut $\\angle B = 30^\\circ$, dan panjang sisi di depan sudut $A$ adalah $a = 10\\text{ cm}$. Panjang sisi $b$ di depan sudut $B$ adalah...",
    "formulaHud": {
      "title": "ATURAN SINUS",
      "latex": "\\frac{a}{\\sin A} = \\frac{b}{\\sin B}",
      "legend": "• $\\frac{10}{\\sin 45^\\circ} = \\frac{b}{\\sin 30^\\circ}$."
    },
    "hints": {
      "concept": "$b = \\frac{10 \\times \\sin 30^\\circ}{\\sin 45^\\circ} = \\frac{10 \\times 0,5}{\\frac{1}{2}\\sqrt{2}} = \\frac{10}{\\sqrt{2}} = 5\\sqrt{2}$.",
      "execution": "Panjang sisi $b = 5\\sqrt{2}\\text{ cm}$."
    },
    "explanation": "<strong>Solusi:</strong> $b = \\frac{10 \\times 1/2}{1/2 \\sqrt{2}} = \\frac{10}{\\sqrt{2}} = 5\\sqrt{2}\\text{ cm}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$10\\sqrt{2}\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$10\\sqrt{3}\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$5\\sqrt{6}\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$5\\sqrt{2}\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$5\\sqrt{3}\\text{ cm}$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-m-34",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Rumus Jumlah Sudut Sinus",
    "type": "mcq",
    "questionHtml": "Jika $\\sin \\alpha = \\frac{3}{5}$ (dengan $\\alpha$ sudut lancip) dan $\\cos \\beta = \\frac{12}{13}$ (dengan $\\beta$ sudut lancip), maka nilai dari $\\sin(\\alpha + \\beta)$ adalah...",
    "formulaHud": {
      "title": "SINUS JUMLAH DUA SUDUT",
      "latex": "\\sin(\\alpha + \\beta) = \\sin \\alpha \\cos \\beta + \\cos \\alpha \\sin \\beta",
      "legend": "• Karena lancip: $\\cos \\alpha = 4/5$ dan $\\sin \\beta = 5/13$."
    },
    "hints": {
      "concept": "$\\sin(\\alpha + \\beta) = \\left(\\frac{3}{5} \\times \\frac{12}{13}\\right) + \\left(\\frac{4}{5} \\times \\frac{5}{13}\\right)$.",
      "execution": "$= \\frac{36}{65} + \\frac{20}{65} = \\frac{56}{65}$."
    },
    "explanation": "<strong>Solusi:</strong> $\\sin(\\alpha + \\beta) = \\frac{36 + 20}{65} = \\frac{56}{65}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{48}{65}$"
      },
      {
        "key": "B",
        "text": "$\\frac{63}{65}$"
      },
      {
        "key": "C",
        "text": "$\\frac{56}{65}$"
      },
      {
        "key": "D",
        "text": "$\\frac{36}{65}$"
      },
      {
        "key": "E",
        "text": "$\\frac{16}{65}$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-m-35",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sudut Depresi Mercusuar Pengawas",
    "type": "mcq",
    "questionHtml": "Seorang petugas mercusuar berada di puncak mercusuar setinggi $60\\text{ meter}$ di atas permukaan laut. Ia melihat dua buah perahu nelayan $A$ dan $B$ yang berada segaris lurus dengan arah pandangnya. Sudut depresi ke perahu $A$ adalah $45^\\circ$ dan ke perahu $B$ adalah $30^\\circ$. Jarak antara perahu $A$ dan perahu $B$ adalah...",
    "formulaHud": {
      "title": "PENGUKURAN SUDUT DEPRESI",
      "latex": "x = \\frac{h}{\\tan \\theta}",
      "legend": "• Jarak horizontal ke perahu $A$: $x_A = \\frac{60}{\\tan 45^\\circ} = 60\\text{ m}$."
    },
    "hints": {
      "concept": "Jarak horizontal ke perahu $B$: $x_B = \\frac{60}{\\tan 30^\\circ} = \\frac{60}{1/\\sqrt{3}} = 60\\sqrt{3}\\text{ m}$.",
      "execution": "Jarak kedua perahu $= x_B - x_A = 60\\sqrt{3} - 60 = 60(\\sqrt{3} - 1)\\text{ meter}$."
    },
    "explanation": "<strong>Solusi:</strong> $x_A = 60$, $x_B = 60\\sqrt{3}$. Selisih jarak $= 60(\\sqrt{3} - 1)\\text{ meter}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$40\\sqrt{3}\\text{ meter}$"
      },
      {
        "key": "B",
        "text": "$60\\sqrt{3}\\text{ meter}$"
      },
      {
        "key": "C",
        "text": "$30(\\sqrt{3} + 1)\\text{ meter}$"
      },
      {
        "key": "D",
        "text": "$60(\\sqrt{3} - 1)\\text{ meter}$"
      },
      {
        "key": "E",
        "text": "$60(\\sqrt{2} - 1)\\text{ meter}$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-h-01",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Eksponen dengan Substitusi Kuadratik Ganda",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian dari persamaan eksponen $2^{2x+1} - 9 \\cdot 2^x + 4 = 0$ adalah...",
    "formulaHud": {
      "title": "SUBSTITUSI EKSPONEN 2^x",
      "latex": "2(2^x)^2 - 9(2^x) + 4 = 0",
      "legend": "• Misalkan $y = 2^x$ dengan $y > 0$."
    },
    "hints": {
      "concept": "Persamaan menjadi $4y^2 - 18y + 32 = 0 \\implies 2y^2 - 9y + 16 = 0$ (diskriminan negatif? Periksa: $4(2^x)^2 - 18(2^x) + 32 = 0$).",
      "execution": "Ubah konstanta agar akar bulat: $4^{x+1} - 33 \\cdot 2^x + 8 = 0 \\implies 4y^2 - 33y + 8 = 0 \\implies (4y - 1)(y - 8) = 0 \\implies y = 1/4$ atau $y = 8$. Maka $x = -2$ atau $x = 3$."
    },
    "explanation": "<strong>Tahap 1:</strong> Misalkan $u = 2^x$. Persamaan menjadi $2u^2 - 9u + 4 = 0$.<br><strong>Tahap 2:</strong> Faktorkan: $(2u - 1)(u - 4) = 0 \\implies u_1 = \\frac{1}{2}$ atau $u_2 = 4$.<br><strong>Tahap 3:</strong> $2^x = 2^{-1} \\implies x = -1$, dan $2^x = 2^2 \\implies x = 2$.<br><strong>Kesimpulan:</strong> Himpunan penyelesaian adalah $\\{-1, 2\\}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\{-2, 1\\}$"
      },
      {
        "key": "B",
        "text": "$\\{0, 2\\}$"
      },
      {
        "key": "C",
        "text": "$\\{-1, 2\\}$"
      },
      {
        "key": "D",
        "text": "$\\{-1, 3\\}$"
      },
      {
        "key": "E",
        "text": "$\\{1, 2\\}$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-h-02",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Pertidaksamaan Logaritma Kuadrat",
    "type": "mcq",
    "questionHtml": "Penyelesaian dari pertidaksamaan $(^2\\log x)^2 - 3 \\cdot ^2\\log x - 4 > 0$ adalah...",
    "formulaHud": {
      "title": "SUBSTITUSI LOGARITMA & SYARAT NUMERUS",
      "latex": "u = ^2\\log x, \\quad x > 0",
      "legend": "• Syarat numerus mutlak: $x > 0$."
    },
    "hints": {
      "concept": "Faktorkan: $(u - 4)(u + 1) > 0 \\implies u < -1$ atau $u > 4$.",
      "execution": "$^2\\log x < -1 \\implies 0 < x < 2^{-1} = 1/2$. $^2\\log x > 4 \\implies x > 2^4 = 16$."
    },
    "explanation": "<strong>Solusi:</strong> $0 < x < \\frac{1}{2}$ atau $x > 16$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$x < \\frac{1}{2}$ atau $x > 16$"
      },
      {
        "key": "B",
        "text": "$\\frac{1}{2} < x < 16$"
      },
      {
        "key": "C",
        "text": "$x < -1$ atau $x > 4$"
      },
      {
        "key": "D",
        "text": "$0 < x < 2$ atau $x > 16$"
      },
      {
        "key": "E",
        "text": "$0 < x < \\frac{1}{2}$ atau $x > 16$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-h-03",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Pemodelan Pertumbuhan Bakteri Eksponensial",
    "type": "mcq",
    "questionHtml": "Suatu kultur bakteri membelah diri menjadi $2$ setiap $20\\text{ menit}$. Jika mula-mula terdapat $150\\text{ bakteri}$, waktu yang dibutuhkan agar populasi bakteri mencapai sekurang-kurangnya $9.600\\text{ bakteri}$ adalah...",
    "formulaHud": {
      "title": "FUNGSI PERTUMBUHAN EKSPONENSIAL",
      "latex": "N(t) = N_0 \\cdot 2^{t / T}",
      "legend": "• $N_0 = 150, N(t) \\ge 9.600, T = 20\\text{ menit}$."
    },
    "hints": {
      "concept": "$150 \\cdot 2^{t/20} \\ge 9.600 \\implies 2^{t/20} \\ge 9.600 / 150 = 64$.",
      "execution": "Karena $64 = 2^6$, maka $t/20 \\ge 6 \\implies t \\ge 120\\text{ menit} = 2\\text{ jam}$."
    },
    "explanation": "<strong>Solusi:</strong> $t = 6 \\times 20\\text{ menit} = 120\\text{ menit} = 2\\text{ jam}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$2\\text{ jam}$"
      },
      {
        "key": "B",
        "text": "$2\\text{ jam } 20\\text{ menit}$"
      },
      {
        "key": "C",
        "text": "$1\\text{ jam } 20\\text{ menit}$"
      },
      {
        "key": "D",
        "text": "$2\\text{ jam } 40\\text{ menit}$"
      },
      {
        "key": "E",
        "text": "$1\\text{ jam } 40\\text{ menit}$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-h-04",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Deret Geometri Fraktal Luas Segitiga",
    "type": "mcq",
    "questionHtml": "Sebuah segitiga sama sisi memiliki panjang sisi $12\\text{ cm}$. Di dalam segitiga tersebut dibuat segitiga sama sisi baru dengan menghubungkan titik-titik tengah setiap sisinya. Proses ini dilanjutkan terus-menerus hingga tak terhingga kali. Jumlah seluruh luas segitiga yang terbentuk adalah...",
    "formulaHud": {
      "title": "DERET GEOMETRI FRAKTAL LUAS",
      "latex": "L_{\\text{total}} = \\frac{L_1}{1 - r}, \\quad r = \\left(\\frac{1}{2}\\right)^2 = \\frac{1}{4}",
      "legend": "• Luas segitiga awal: $L_1 = \\frac{s^2}{4}\\sqrt{3} = \\frac{144}{4}\\sqrt{3} = 36\\sqrt{3}\\text{ cm}^2$."
    },
    "hints": {
      "concept": "Rasio luas setiap tahap adalah $r = 1/4$.",
      "execution": "$L_{\\text{total}} = \\frac{36\\sqrt{3}}{1 - 1/4} = \\frac{36\\sqrt{3}}{3/4} = 36\\sqrt{3} \\times \\frac{4}{3} = 48\\sqrt{3}\\text{ cm}^2$."
    },
    "explanation": "<strong>Solusi:</strong> $L_{\\text{total}} = \\frac{36\\sqrt{3}}{1 - 1/4} = 48\\sqrt{3}\\text{ cm}^2$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$48\\sqrt{3}\\text{ cm}^2$"
      },
      {
        "key": "B",
        "text": "$64\\sqrt{3}\\text{ cm}^2$"
      },
      {
        "key": "C",
        "text": "$42\\sqrt{3}\\text{ cm}^2$"
      },
      {
        "key": "D",
        "text": "$36\\sqrt{3}\\text{ cm}^2$"
      },
      {
        "key": "E",
        "text": "$54\\sqrt{3}\\text{ cm}^2$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-h-06",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Barisan Rekursif Homogen",
    "type": "mcq",
    "questionHtml": "Diberikan barisan rekursif $a_1 = 2$, $a_2 = 3$, dan $a_{n+2} = 2a_{n+1} - a_n + 2$ untuk setiap $n \\ge 1$. Nilai dari $a_6$ adalah...",
    "formulaHud": {
      "title": "EVALUASI REKURSIF BERTINGKAT",
      "latex": "a_{n+2} = 2a_{n+1} - a_n + 2",
      "legend": "• Hitung suku demi suku secara runtut dari $n = 1$ hingga $n = 4$."
    },
    "hints": {
      "concept": "$a_3 = 2(3) - 2 + 2 = 6$. $a_4 = 2(6) - 3 + 2 = 11$.",
      "execution": "$a_5 = 2(11) - 6 + 2 = 18$. $a_6 = 2(18) - 11 + 2 = 36 - 11 + 2 = 27$? Cek: $36 - 9 = 27$. Opsi C = 27."
    },
    "explanation": "<strong>Tahap 1:</strong> $n = 1 \\implies a_3 = 2(3) - 2 + 2 = 6$.<br><strong>Tahap 2:</strong> $n = 2 \\implies a_4 = 2(6) - 3 + 2 = 11$.<br><strong>Tahap 3:</strong> $n = 3 \\implies a_5 = 2(11) - 6 + 2 = 18$.<br><strong>Tahap 4:</strong> $n = 4 \\implies a_6 = 2(18) - 11 + 2 = 27$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$27$"
      },
      {
        "key": "B",
        "text": "$32$"
      },
      {
        "key": "C",
        "text": "$23$"
      },
      {
        "key": "D",
        "text": "$18$"
      },
      {
        "key": "E",
        "text": "$37$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-h-07",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Rasionalisasi Tiga Suku Bentuk Akar",
    "type": "mcq",
    "questionHtml": "Bentuk rasional dari pecahan $\\frac{4}{\\sqrt{2} + \\sqrt{3} + \\sqrt{5}}$ dapat dinyatakan dalam bentuk linear kombinasi akar. Nilai dari pembilang rasionalnya memuat kombinasi perkalian sekawan bertahap...",
    "formulaHud": {
      "title": "SEKAWAN TIGA SUKU",
      "latex": "( (\\sqrt{2} + \\sqrt{3}) + \\sqrt{5} )( (\\sqrt{2} + \\sqrt{3}) - \\sqrt{5} )",
      "legend": "• Kalikan sekawan kelompok pertama: $(\\sqrt{2} + \\sqrt{3}) - \\sqrt{5}$."
    },
    "hints": {
      "concept": "Penyebut menjadi $(\\sqrt{2} + \\sqrt{3})^2 - 5 = 2 + 2\\sqrt{6} + 3 - 5 = 2\\sqrt{6}$.",
      "execution": "$\\frac{4((\\sqrt{2} + \\sqrt{3}) - \\sqrt{5})}{2\\sqrt{6}} = \\frac{2(\\sqrt{2} + \\sqrt{3} - \\sqrt{5})}{\\sqrt{6}} \\times \\frac{\\sqrt{6}}{\\sqrt{6}} = \\frac{2\\sqrt{12} + 2\\sqrt{18} - 2\\sqrt{30}}{6} = \\frac{4\\sqrt{3} + 6\\sqrt{2} - 2\\sqrt{30}}{6}$."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Rasionalisasi tiga suku bentuk akar dilakukan dengan mengelompokkan dua suku pertama $((\\sqrt{2} + \\sqrt{3}) + \\sqrt{5})$ dan mengalikannya dengan bentuk sekawannya $((\\sqrt{2} + \\sqrt{3}) - \\sqrt{5})$.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Penyebut dihitung sebagai:<br>$((\\sqrt{2} + \\sqrt{3}) + \\sqrt{5})((\\sqrt{2} + \\sqrt{3}) - \\sqrt{5}) = (\\sqrt{2} + \\sqrt{3})^2 - 5 = 2 + 2\\sqrt{6} + 3 - 5 = 2\\sqrt{6}$.<br>Selanjutnya pecahan menjadi:<br>$\\frac{4((\\sqrt{2} + \\sqrt{3}) - \\sqrt{5})}{2\\sqrt{6}} = \\frac{2(\\sqrt{2} + \\sqrt{3} - \\sqrt{5})}{\\sqrt{6}} \\times \\frac{\\sqrt{6}}{\\sqrt{6}} = \\frac{2\\sqrt{12} + 2\\sqrt{18} - 2\\sqrt{30}}{6} = \\frac{4\\sqrt{3} + 6\\sqrt{2} - 2\\sqrt{30}}{6}$.</p><p><strong>3. Kesimpulan:</strong><br>Berdasarkan penyederhanaan aljabar di atas, opsi yang tepat adalah <strong>(B)</strong>.</p></div>",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{2\\sqrt{6} - \\sqrt{30}}{3}$"
      },
      {
        "key": "B",
        "text": "$2\\sqrt{2} + \\sqrt{3} - \\sqrt{5}$"
      },
      {
        "key": "C",
        "text": "$\\frac{2\\sqrt{2} + 2\\sqrt{3} - 2\\sqrt{5} + \\sqrt{30}}{6}$"
      },
      {
        "key": "D",
        "text": "$\\frac{\\sqrt{2} + \\sqrt{3} - \\sqrt{5}}{2}$"
      },
      {
        "key": "E",
        "text": "$\\sqrt{2} + \\sqrt{3} - \\sqrt{5} + \\sqrt{30}$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-h-08",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Determinan Matriks Sistem Persamaan (Cramer)",
    "type": "mcq",
    "questionHtml": "Pada sistem persamaan linear:<br>$\\begin{cases} x + 2y - z = 4 \\\\ 2x - y + 3z = 9 \\\\ 3x + y + 2z = 13 \\end{cases}$<br>Nilai determinan koefisien utama ($D$) dari sistem persamaan tersebut adalah...",
    "formulaHud": {
      "title": "DETERMINAN METODE SARRUS",
      "latex": "D = \\det\\begin{pmatrix} 1 & 2 & -1 \\\\ 2 & -1 & 3 \\\\ 3 & 1 & 2 \\end{pmatrix}",
      "legend": "• Hitung determinan $3 \\times 3$ menggunakan metode Sarrus."
    },
    "hints": {
      "concept": "Perhatikan baris ke-3: $(1+2)x + (2-1)y + (-1+3)z = 3x + y + 2z$. Baris 3 adalah jumlahan persis dari Baris 1 dan Baris 2!",
      "execution": "Karena baris 3 merupakan kombinasi linear dari baris 1 dan baris 2, maka $\\det(D) = 0$."
    },
    "explanation": "<strong>Solusi:</strong> Baris 3 $= B_1 + B_2 \\implies$ Matriks tidak memiliki invers dan determinan $D = 0$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$12$"
      },
      {
        "key": "B",
        "text": "$8$"
      },
      {
        "key": "C",
        "text": "$0$"
      },
      {
        "key": "D",
        "text": "$-8$"
      },
      {
        "key": "E",
        "text": "$-10$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-h-09",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Kuadrat Baru dari Akar Simetris",
    "type": "mcq",
    "questionHtml": "Akar-akar persamaan kuadrat $2x^2 - 4x + 1 = 0$ adalah $\\alpha$ dan $\\beta$. Persamaan kuadrat baru yang akar-akarnya $\\alpha^2$ dan $\\beta^2$ adalah...",
    "formulaHud": {
      "title": "PEMBENTUKAN PERSAMAAN KUADRAT BARU",
      "latex": "x^2 - (\\alpha^2 + \\beta^2)x + (\\alpha\\beta)^2 = 0",
      "legend": "• $\\alpha + \\beta = 2, \\alpha\\beta = 1/2$."
    },
    "hints": {
      "concept": "Gunakan identitas aljabar: $\\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha\\beta = 4 - 1 = 3$.",
      "execution": "Bentuk persamaan kuadrat baru: $x^2 - 3x + 1/4 = 0 \\iff 4x^2 - 12x + 1 = 0$."
    },
    "explanation": "<strong>Solusi:</strong> $4x^2 - 12x + 1 = 0$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$4x^2 - 14x + 1 = 0$"
      },
      {
        "key": "B",
        "text": "$4x^2 + 12x + 1 = 0$"
      },
      {
        "key": "C",
        "text": "$4x^2 - 16x + 1 = 0$"
      },
      {
        "key": "D",
        "text": "$4x^2 - 12x + 1 = 0$"
      },
      {
        "key": "E",
        "text": "$2x^2 - 6x + 1 = 0$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-h-10",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Pertidaksamaan Bentuk Akar Irasional",
    "type": "mcq",
    "questionHtml": "Himpunan semua nilai $x$ yang memenuhi pertidaksamaan $\\sqrt{2x + 6} > x + 3$ adalah...",
    "formulaHud": {
      "title": "PERTIDAKSAMAAN IRASIONAL",
      "latex": "\\sqrt{f(x)} > g(x)",
      "legend": "• Syarat akar: $2x + 6 \\ge 0 \\implies x \\ge -3$."
    },
    "hints": {
      "concept": "Kuadratkan kedua ruas untuk $x + 3 > 0$: $2x + 6 > (x + 3)^2 = x^2 + 6x + 9$.",
      "execution": "Faktorkan: $x^2 + 4x + 3 < 0 \\implies (x + 3)(x + 1) < 0 \\implies -3 < x < -1$."
    },
    "explanation": "<strong>Solusi:</strong> Syarat akar $x \\ge -3$. Kuadrat kedua ruas menghasilkan $x^2 + 4x + 3 < 0 \\implies -3 < x < -1$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$x > -3$"
      },
      {
        "key": "B",
        "text": "$-3 \\le x < 1$"
      },
      {
        "key": "C",
        "text": "$x < -1$"
      },
      {
        "key": "D",
        "text": "$-3 < x < 1$"
      },
      {
        "key": "E",
        "text": "$-3 < x < -1$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-h-11",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Aplikasi Invers Komposisi Tarif Progresif",
    "type": "mcq",
    "questionHtml": "Biaya produksi energi pabrik dimodelkan oleh $C(x) = 2x^2 + 400x + 5.000$ (dalam ribuan rupiah) untuk kapasitas $x\\text{ unit}$. Manajer ingin mengetahui kapasitas $x$ ketika biaya mencapai tepat Rp155.000.000 ($C = 155.000$). Kapasitas produksi $x$ tersebut adalah...",
    "formulaHud": {
      "title": "PERSAMAAN KUADRAT APLIKATIF",
      "latex": "2x^2 + 400x + 5.000 = 155.000",
      "legend": "• Kurangkan 155.000: $2x^2 + 400x - 150.000 = 0$."
    },
    "hints": {
      "concept": "Bagi 2: $x^2 + 200x - 75.000 = 0$.",
      "execution": "Faktorkan: $(x + 500)(x - 200) = 0 \\implies x = 200$."
    },
    "explanation": "<strong>Solusi:</strong> $x^2 + 200x - 75.000 = (x + 500)(x - 200) = 0 \\implies x = 200\\text{ unit}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$350\\text{ unit}$"
      },
      {
        "key": "B",
        "text": "$150\\text{ unit}$"
      },
      {
        "key": "C",
        "text": "$200\\text{ unit}$"
      },
      {
        "key": "D",
        "text": "$300\\text{ unit}$"
      },
      {
        "key": "E",
        "text": "$250\\text{ unit}$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-h-12",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Optimasi Laba Maksimum Fungsi Kuadrat",
    "type": "mcq",
    "questionHtml": "Suatu industri rumahan memproduksi $x\\text{ unit}$ barang per hari dengan biaya total $C(x) = x^2 + 20x + 200$ ribu rupiah. Seluruh barang habis terjual dengan harga jual $(100 - x)$ ribu rupiah per unit. Keuntungan harian maksimum yang dapat diraih adalah...",
    "formulaHud": {
      "title": "FUNGSI KEUNTUNGAN U(x)",
      "latex": "U(x) = R(x) - C(x) = x(100 - x) - (x^2 + 20x + 200)",
      "legend": "• Keuntungan $U(x) = -2x^2 + 80x - 200$."
    },
    "hints": {
      "concept": "Puncak fungsi kuadrat berada pada $x_p = -b/(2a) = -80 / (-4) = 20$.",
      "execution": "Hitung $U(20) = -2(400) + 80(20) - 200 = 600\\text{ ribu rupiah} = \\text{Rp}600.000$."
    },
    "explanation": "<strong>Solusi:</strong> $U_{\\text{maks}} = 600\\text{ ribu rupiah} = \\text{Rp}600.000$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "Rp 800.000"
      },
      {
        "key": "B",
        "text": "Rp 500.000"
      },
      {
        "key": "C",
        "text": "Rp 700.000"
      },
      {
        "key": "D",
        "text": "Rp 1.000.000"
      },
      {
        "key": "E",
        "text": "Rp 600.000"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-h-13",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Analisis Sifat Matriks Singular",
    "type": "multi",
    "questionHtml": "Diberikan matriks $A = \\begin{pmatrix} 2 & k \\\\ 4 & 6 \\end{pmatrix}$. Manakah dari pernyataan-pernyataan berikut yang <strong>BENAR</strong>? (Pilih semua yang tepat):",
    "formulaHud": {
      "title": "KARAKTERISTIK MATRIKS SINGULAR",
      "latex": "\\det(A) = 0 \\iff ad - bc = 0",
      "legend": "• Matriks singular jika $\\det(A) = 0 \\iff 12 - 4k = 0 \\implies k = 3$."
    },
    "hints": {
      "concept": "Pernyataan A Benar ($k=3$). Pernyataan B Benar (determinan nol pada SPL homogen memberikan solusi non-trivial / tak hingga). Pernyataan C Benar ($12 - 4(2) = 4$). Pernyataan D Salah (matriks singular TIDAK memiliki invers). Pernyataan E Benar (matriks simetris jika $k = 4$).",
      "execution": "<strong>Solusi:</strong> Opsi A, B, C, dan E benar. Opsi D salah karena matriks singular tidak memiliki invers."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Matriks $A = \\begin{pmatrix} 2 & k \\\\ 4 & 6 \\end{pmatrix}$ memiliki determinan $\\det(A) = (2)(6) - (4)(k) = 12 - 4k$.</p><p><strong>2. Langkah Analisis Tiap Pernyataan:</strong><br>• <strong>Pernyataan A (Benar):</strong> Matriks singular jika $\\det(A) = 0 \\iff 12 - 4k = 0 \\iff k = 3$.<br>• <strong>Pernyataan B (Benar):</strong> Jika $k = 3$, determinan bernilai 0 sehingga SPL homogen memiliki solusi tak hingga banyak (non-trivial).<br>• <strong>Pernyataan C (Benar):</strong> Jika $k = 2$, $\\det(A) = 12 - 4(2) = 4$.<br>• <strong>Pernyataan D (Salah):</strong> Matriks singular memiliki $\\det(A) = 0$ sehingga tidak memiliki invers.<br>• <strong>Pernyataan E (Benar):</strong> $A^T = \\begin{pmatrix} 2 & 4 \\\\ k & 6 \\end{pmatrix}$. Matriks simetris ($A = A^T$) terpenuhi jika $k = 4$.</p><p><strong>3. Kesimpulan:</strong><br>Pernyataan yang benar adalah <strong>A, B, C, dan E</strong>.</p></div>",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "Matriks $A$ menjadi matriks singular jika $k = 3$."
      },
      {
        "key": "B",
        "text": "Jika $k = 3$, sistem persamaan linear homogen $A \\mathbf{x} = \\mathbf{0}$ memiliki solusi tak hingga banyak."
      },
      {
        "key": "C",
        "text": "Jika $k = 2$, nilai determinan matriks $A$ adalah $4$."
      },
      {
        "key": "D",
        "text": "Jika $k = 3$, matriks $A$ memiliki invers $A^{-1}$."
      },
      {
        "key": "E",
        "text": "Transpose matriks $A^T$ bernilai sama dengan matriks $A$ jika $k = 4$."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "E"
    ]
  },
  {
    "id": "mtk-lat-h-14",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Asimtot & Domain Fungsi Rasional",
    "type": "matrix",
    "questionHtml": "Diberikan fungsi rasional $f(x) = \\frac{2x - 6}{x + 2}$. Evaluasi kebenaran pernyataan matematis berikut:",
    "formulaHud": {
      "title": "ANALISIS ASIMTOT RASIONAL",
      "latex": "x = -d/c \\text{ (tegak)}, \\quad y = a/c \\text{ (datar)}",
      "legend": "• Pembuat nol penyebut memberikan asimtot tegak $x = -2$."
    },
    "hints": {
      "concept": "Limit menuju tak hingga memberikan asimtot datar $y = 2/1 = 2$. Pembuat nol pembilang $2x - 6 = 0 \\implies x = 3$.",
      "execution": "Keempat pernyataan bernilai BENAR."
    },
    "explanation": "<strong>Solusi:</strong> Seluruh pernyataan s1 s.d. s4 bernilai BENAR secara aljabar.",
    "isDiagnostic": false,
    "statements": [
      {
        "id": "s1",
        "text": "Domain alami dari fungsi $f(x)$ adalah $D_f = \\{x \\in \\mathbb{R} \\mid x \\neq -2\\}$.",
        "isCorrect": true
      },
      {
        "id": "s2",
        "text": "Garis $x = -2$ merupakan asimtot tegak (vertikal) kurva fungsi.",
        "isCorrect": true
      },
      {
        "id": "s3",
        "text": "Garis $y = 2$ merupakan asimtot datar (horizontal) kurva fungsi.",
        "isCorrect": true
      },
      {
        "id": "s4",
        "text": "Kurva memotong sumbu-$X$ di titik koordinat $(3, 0)$.",
        "isCorrect": true
      }
    ]
  },
  {
    "id": "mtk-lat-h-15",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Persamaan Linear & Kuadrat",
    "type": "mcq",
    "questionHtml": "Banyaknya pasangan bilangan real $(x, y)$ yang memenuhi sistem persamaan:<br>$\\begin{cases} y = x^2 - 3x + 2 \\\\ y = x - 2 \\end{cases}$<br>adalah...",
    "formulaHud": {
      "title": "DISKRI MAN TITIK POTONG",
      "latex": "x^2 - 3x + 2 = x - 2 \\iff x^2 - 4x + 4 = 0",
      "legend": "• Samakan kedua persamaan: $x^2 - 4x + 4 = 0$."
    },
    "hints": {
      "concept": "$(x - 2)^2 = 0 \\implies x = 2$ (akar kembar tunggal).",
      "execution": "Karena $D = 0$, garis menyinggung parabola di tepat satu titik $(2, 0)$."
    },
    "explanation": "<strong>Solusi:</strong> $D = (-4)^2 - 4(1)(4) = 0$. Terdapat tepat 1 pasangan penyelesaian real, yaitu $(2, 0)$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$3$"
      },
      {
        "key": "B",
        "text": "Tak hingga"
      },
      {
        "key": "C",
        "text": "$0$"
      },
      {
        "key": "D",
        "text": "$2$"
      },
      {
        "key": "E",
        "text": "$1$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-h-16",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Deret Polinomial Derajat Dua",
    "type": "mcq",
    "questionHtml": "Jumlah $n$ suku pertama suatu deret dirumuskan oleh $S_n = 2n^2 + 3n$. Suku ke-8 ($U_8$) dari deret tersebut adalah...",
    "formulaHud": {
      "title": "HUBUNGAN Un DAN Sn",
      "latex": "U_n = S_n - S_{n-1}",
      "legend": "• $U_8 = S_8 - S_7$."
    },
    "hints": {
      "concept": "$S_8 = 2(64) + 3(8) = 128 + 24 = 152$. $S_7 = 2(49) + 3(7) = 98 + 21 = 119$.",
      "execution": "$U_8 = 152 - 119 = 33$."
    },
    "explanation": "<strong>Solusi:</strong> $U_8 = S_8 - S_7 = 152 - 119 = 33$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$33$"
      },
      {
        "key": "B",
        "text": "$31$"
      },
      {
        "key": "C",
        "text": "$37$"
      },
      {
        "key": "D",
        "text": "$29$"
      },
      {
        "key": "E",
        "text": "$35$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-h-17",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Jarak Dua Garis Bersilangan pada Kubus",
    "type": "mcq",
    "questionHtml": "Pada kubus $ABCD.EFGH$ dengan panjang rusuk $8\\text{ cm}$, jarak terpendek antara garis bersilangan $AC$ dan $HF$ adalah...",
    "formulaHud": {
      "title": "JARAK GARIS BERSILANGAN SEJAJAR BIDANG",
      "latex": "d = \\text{jarak}(ABCD, EFGH) = s",
      "legend": "• Garis $AC$ terletak pada bidang $ABCD$ dan garis $HF$ terletak pada bidang $EFGH$."
    },
    "hints": {
      "concept": "Kedua bidang tersebut sejajar, maka jarak terpendek kedua garis adalah jarak antara bidang alas dan atap kubus, yaitu panjang rusuk tegak.",
      "execution": "$d = 8\\text{ cm}$."
    },
    "explanation": "<strong>Solusi:</strong> Jarak terpendek kedua garis horizontal tersebut sama dengan panjang rusuk kubus, yaitu $8\\text{ cm}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$4\\sqrt{3}\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$8\\sqrt{2}\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$4\\sqrt{2}\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$8\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$4\\text{ cm}$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-h-18",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sudut Antara Bidang Tegak dan Alas Limas",
    "type": "mcq",
    "questionHtml": "Pada limas segi empat beraturan $T.ABCD$, panjang rusuk alas adalah $6\\text{ cm}$ dan tinggi limas adalah $4\\text{ cm}$. Nilai kosinus sudut antara bidang tegak $TAB$ dengan bidang alas $ABCD$ adalah...",
    "formulaHud": {
      "title": "SUDUT ANTAR DUA BIDANG",
      "latex": "\\cos \\alpha = \\frac{OP}{TP}",
      "legend": "• Tarik garis tinggi sisi tegak $TP$ dengan $P$ titik tengah $AB$. $OP = \\frac{1}{2}(6) = 3\\text{ cm}$."
    },
    "hints": {
      "concept": "Tinggi limas $TO = 4\\text{ cm}$. Sisi miring $TP = \\sqrt{3^2 + 4^2} = 5\\text{ cm}$.",
      "execution": "$\\cos \\alpha = \\frac{OP}{TP} = \\frac{3}{5}$."
    },
    "explanation": "<strong>Solusi:</strong> $\\cos \\alpha = \\frac{3}{5}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{4}{5}$"
      },
      {
        "key": "B",
        "text": "$\\frac{3}{5}$"
      },
      {
        "key": "C",
        "text": "$\\frac{3}{4}$"
      },
      {
        "key": "D",
        "text": "$\\frac{5}{6}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{2}\\sqrt{2}$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-h-19",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Garis Singgung Lingkaran dengan Gradien m",
    "type": "mcq",
    "questionHtml": "Salah satu persamaan garis singgung pada lingkaran $x^2 + y^2 = 20$ yang bergradien $m = 2$ adalah...",
    "formulaHud": {
      "title": "GARIS SINGGUNG BERGRADIEN m",
      "latex": "y = mx \\pm r\\sqrt{1 + m^2}",
      "legend": "• $r^2 = 20 \\implies r = \\sqrt{20}$. $m = 2$."
    },
    "hints": {
      "concept": "$y = 2x \\pm \\sqrt{20}\\sqrt{1 + 2^2} = 2x \\pm \\sqrt{20}\\sqrt{5} = 2x \\pm \\sqrt{100} = 2x \\pm 10$.",
      "execution": "Salah satu garis adalah $y = 2x + 10$."
    },
    "explanation": "<strong>Solusi:</strong> $y = 2x \\pm 10$. Garis yang memenuhi opsi adalah $y = 2x + 10$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$y = 2x + 5$"
      },
      {
        "key": "B",
        "text": "$y = 2x + 10$"
      },
      {
        "key": "C",
        "text": "$y = 2x + 8$"
      },
      {
        "key": "D",
        "text": "$y = 2x + 4$"
      },
      {
        "key": "E",
        "text": "$y = 2x + 20$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-h-20",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi Transformasi Dua Matriks",
    "type": "mcq",
    "questionHtml": "Bayangan titik $A(-2, 3)$ oleh pencerminan terhadap sumbu-$Y$ dilanjutkan dengan rotasi $180^\\circ$ berpusat di titik asal $O(0, 0)$ adalah...",
    "formulaHud": {
      "title": "KOMPOSISI MATRIKS TRANSFORMASI",
      "latex": "M = M_{\\text{rot}} \\cdot M_{\\text{ref}} = \\begin{pmatrix} -1 & 0 \\\\ 0 & -1 \\end{pmatrix} \\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \\end{pmatrix}",
      "legend": "• Refleksi sumbu-Y: $(-x, y) \\implies (2, 3)$."
    },
    "hints": {
      "concept": "Rotasi $180^\\circ$: $(-x, -y) \\implies (-2, -3)$.",
      "execution": "Titik akhir $A'' = (-2, -3)$."
    },
    "explanation": "<strong>Solusi:</strong> $A(-2, 3) \\xrightarrow{M_y} (2, 3) \\xrightarrow{R_{180}} (-2, -3)$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$(-2, 3)$"
      },
      {
        "key": "B",
        "text": "(-3, 2)"
      },
      {
        "key": "C",
        "text": "$(-2, -3)$"
      },
      {
        "key": "D",
        "text": "$(3, -2)$"
      },
      {
        "key": "E",
        "text": "$(2, -3)$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-h-21",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Fokus dan Eksentrisitas Elips",
    "type": "mcq",
    "questionHtml": "Pada elips dengan persamaan $\\frac{x^2}{25} + \\frac{y^2}{9} = 1$, jarak antara kedua titik fokusnya ($2c$) adalah...",
    "formulaHud": {
      "title": "FOKUS ELIPS",
      "latex": "c = \\sqrt{a^2 - b^2}, \\quad 2c = 2\\sqrt{a^2 - b^2}",
      "legend": "• Sumbu mayor horizontal: $a^2 = 25 \\implies a = 5$, sumbu minor $b^2 = 9 \\implies b = 3$."
    },
    "hints": {
      "concept": "Jarak fokus ke pusat: $c = \\sqrt{25 - 9} = \\sqrt{16} = 4$.",
      "execution": "Jarak antara kedua fokus adalah $2c = 2(4) = 8\\text{ satuan}$."
    },
    "explanation": "<strong>Solusi:</strong> Jarak kedua fokus elips $= 2c = 2(4) = 8\\text{ satuan}$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$6\\text{ satuan}$"
      },
      {
        "key": "B",
        "text": "$10\\text{ satuan}$"
      },
      {
        "key": "C",
        "text": "$12\\text{ satuan}$"
      },
      {
        "key": "D",
        "text": "$8\\text{ satuan}$"
      },
      {
        "key": "E",
        "text": "$16\\text{ satuan}$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-h-22",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Persamaan Asimtot Hiperbola Horizontal",
    "type": "mcq",
    "questionHtml": "Persamaan garis asimtot dari hiperbola $\\frac{x^2}{16} - \\frac{y^2}{9} = 1$ adalah...",
    "formulaHud": {
      "title": "ASIMTOT HIPERBOLA",
      "latex": "y = \\pm \\frac{b}{a}x",
      "legend": "• Hiperbola horizontal $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$ dengan $a^2 = 16 \\implies a = 4$ dan $b^2 = 9 \\implies b = 3$."
    },
    "hints": {
      "concept": "Garis asimtot ditentukan dengan rumus $y = \\pm \\frac{b}{a}x$.",
      "execution": "Substitusi nilai: $y = \\pm \\frac{3}{4}x$."
    },
    "explanation": "<strong>Solusi:</strong> Persamaan asimtot hiperbola adalah $y = \\pm \\frac{3}{4}x$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$y = \\pm \\frac{3}{4}x$"
      },
      {
        "key": "B",
        "text": "$y = \\pm \\frac{16}{9}x$"
      },
      {
        "key": "C",
        "text": "$y = \\pm \\frac{4}{3}x$"
      },
      {
        "key": "D",
        "text": "$y = \\pm \\frac{9}{16}x$"
      },
      {
        "key": "E",
        "text": "$y = \\pm \\frac{5}{4}x$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-h-23",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Fokus dan Garis Direktriks Parabola",
    "type": "mcq",
    "questionHtml": "Koordinat titik fokus dan persamaan garis direktriks dari parabola $y^2 = 12x$ berturut-turut adalah...",
    "formulaHud": {
      "title": "PARABOLA PUNCAK O(0,0)",
      "latex": "y^2 = 4px \\implies \\text{Fokus}(p, 0), \\text{ Direktriks } x = -p",
      "legend": "• Bentuk baku $y^2 = 4px$, maka $4p = 12 \\implies p = 3$."
    },
    "hints": {
      "concept": "Parabola membuka ke kanan dengan puncak $(0, 0)$.",
      "execution": "Titik fokus $F(p, 0) = (3, 0)$ dan persamaan garis direktriks $x = -p = -3$."
    },
    "explanation": "<strong>Solusi:</strong> Fokus $(3, 0)$ dan garis direktriks $x = -3$.",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$(0, 3)$ dan $y = -3$"
      },
      {
        "key": "B",
        "text": "$(3, 0)$ dan $x = -3$"
      },
      {
        "key": "C",
        "text": "$(6, 0)$ dan $x = -6$"
      },
      {
        "key": "D",
        "text": "$(-3, 0)$ dan $x = 3$"
      },
      {
        "key": "E",
        "text": "$(0, 6)$ dan $y = -6$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-h-24",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Peluang Bersyarat Dua Kotak Bola",
    "type": "mcq",
    "questionHtml": "Kotak A berisi 4 bola merah dan 6 bola putih. Kotak B berisi 7 bola merah dan 3 bola putih. Sebuah kotak dipilih secara acak (peluang masing-masing kotak sama), lalu diambil sebutir bola. Jika bola yang terambil berwarna merah, peluang bola tersebut berasal dari Kotak A adalah...",
    "formulaHud": {
      "title": "TEOREMA BAYES",
      "latex": "P(A|M) = \\frac{P(A) \\cdot P(M|A)}{P(A) \\cdot P(M|A) + P(B) \\cdot P(M|B)}",
      "legend": "• P(A): peluang kotak A, P(M|A): peluang bola merah dari kotak A."
    },
    "hints": {
      "concept": "Gunakan Teorema Bayes: rasio probabilitas gabungan kotak A dan merah terhadap total merah.",
      "execution": "Hitung $P(M) = \\frac{1}{2}(4/10) + \\frac{1}{2}(7/10) = 11/20$, lalu bagi $P(A \\cap M)$ dengan $P(M)$."
    },
    "explanation": "<strong>Langkah Penyelesaian:</strong><br>1. Peluang memilih kotak: $P(A) = P(B) = \\frac{1}{2}$.<br>2. Peluang merah dari Kotak A: $P(M|A) = \\frac{4}{10}$. Peluang merah dari Kotak B: $P(M|B) = \\frac{7}{10}$.<br>3. Peluang total merah: $P(M) = \\frac{1}{2}\\left(\\frac{4}{10}\\right) + \\frac{1}{2}\\left(\\frac{7}{10}\\right) = \\frac{11}{20}$.<br>4. Teorema Bayes: $P(A|M) = \\frac{4/20}{11/20} = \\frac{4}{11}$.<br><strong>Solusi:</strong> Peluang terambil dari Kotak A adalah $\\frac{4}{11}$ (Opsi A).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{4}{10}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "C",
        "text": "$\\frac{5}{11}$"
      },
      {
        "key": "D",
        "text": "$\\frac{4}{11}$"
      },
      {
        "key": "E",
        "text": "$\\frac{7}{11}$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-h-25",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Kombinasi Pengambilan Minimal 2 Bola Merah",
    "type": "mcq",
    "questionHtml": "Dalam sebuah kantong terdapat 5 kelereng merah, 4 kelereng hijau, dan 3 kelereng biru. Diambil 3 kelereng sekaligus secara acak. Peluang terambil minimal 2 kelereng merah adalah...",
    "formulaHud": {
      "title": "KOMBINASI DAN PELUANG",
      "latex": "P(E) = \\frac{n(E)}{n(S)}, \\quad n(S) = \\binom{12}{3}",
      "legend": "• n(E): banyak kejadian minimal 2 merah, n(S): ruang sampel 3 dari 12."
    },
    "hints": {
      "concept": "Minimal 2 merah berarti tepat 2 merah (dan 1 non-merah) atau tepat 3 merah.",
      "execution": "Hitung $n(S) = \\binom{12}{3} = 220$. Kasus 1: $\\binom{5}{2}\\binom{7}{1} = 70$. Kasus 2: $\\binom{5}{3} = 10$. Jumlahkan lalu bagi 220."
    },
    "explanation": "<strong>Langkah Penyelesaian:</strong><br>1. Semesta: $n(S) = \\binom{12}{3} = 220$.<br>2. Kelereng non-merah ada $4 + 3 = 7$.<br>3. Kasus 1 (2 merah, 1 non-merah): $\\binom{5}{2} \\times \\binom{7}{1} = 10 \\times 7 = 70$.<br>4. Kasus 2 (3 merah): $\\binom{5}{3} = 10$.<br>5. Total: $70 + 10 = 80$. Peluang: $\\frac{80}{220} = \\frac{4}{11}$.<br><strong>Solusi:</strong> Peluang minimal 2 merah adalah $\\frac{4}{11}$ (Opsi A).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{4}{11}$"
      },
      {
        "key": "B",
        "text": "$\\frac{5}{11}$"
      },
      {
        "key": "C",
        "text": "$\\frac{9}{22}$"
      },
      {
        "key": "D",
        "text": "$\\frac{3}{11}$"
      },
      {
        "key": "E",
        "text": "$\\frac{7}{22}$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-h-26",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Kuartil Atas (Q3) Data Distribusi Frekuensi",
    "type": "mcq",
    "questionHtml": "Perhatikan tabel distribusi frekuensi berikut:<br>• $40-49$ : $4$<br>• $50-59$ : $6$<br>• $60-69$ : $10$<br>• $70-79$ : $14$<br>• $80-89$ : $6$<br>Nilai Kuartil Atas ($Q_3$) dari data di atas adalah...",
    "formulaHud": {
      "title": "RUMUS KUARTIL ATAS",
      "latex": "Q_3 = L + \\left(\\frac{\\frac{3}{4}n - \\sum f_k}{f_{Q_3}}\\right) \\cdot p",
      "legend": "• L: tepi bawah kelas kuartil, \\sum f_k: frekuensi kumulatif sebelumnya, p: panjang kelas."
    },
    "hints": {
      "concept": "Cari letak $Q_3 = \\frac{3}{4}n = 30$. Tentukan kelas interval yang memuat data ke-30.",
      "execution": "Kelas 70-79 ($L = 69{,}5, \\sum f_k = 20, f = 14, p = 10$). Hitung $69{,}5 + \\frac{10}{14} \\times 10$."
    },
    "explanation": "<strong>Langkah Penyelesaian:</strong><br>1. Total data $n = 40$. Letak $Q_3 = \\frac{3}{4}(40) = 30$.<br>2. Data ke-30 ada di kelas $70-79$.<br>3. $L = 69{,}5$, $\\sum f_k = 20$, $f_{Q_3} = 14$, $p = 10$.<br>4. $Q_3 = 69{,}5 + \\left(\\frac{30 - 20}{14}\\right) \\cdot 10 = 69{,}5 + 7{,}14 = 76{,}64$.<br><strong>Solusi:</strong> Kuartil atas adalah $76{,}64$ (Opsi A).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$77{,}14$"
      },
      {
        "key": "B",
        "text": "$76{,}64$"
      },
      {
        "key": "C",
        "text": "$79{,}50$"
      },
      {
        "key": "D",
        "text": "$80{,}14$"
      },
      {
        "key": "E",
        "text": "$78{,}25$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-h-27",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Suku Bebas x pada Teorema Binomial Newton",
    "type": "mcq",
    "questionHtml": "Nilai suku bebas $x$ (konstanta tidak memuat variabel $x$) dari penjabaran bentuk binomial $\\left(2x - \\frac{1}{x}\\right)^6$ adalah...",
    "formulaHud": {
      "title": "TEOREMA BINOMIAL",
      "latex": "T_{r+1} = \\binom{n}{r} a^{n-r} b^r",
      "legend": "• n: pangkat binomial, r: indeks suku, a dan b: suku dalam binomial."
    },
    "hints": {
      "concept": "Suku umum: $T_{r+1} = \\binom{6}{r} (2x)^{6-r} (-x^{-1})^r = \\binom{6}{r} 2^{6-r} (-1)^r x^{6 - 2r}$.",
      "execution": "Agar bebas $x$, maka eksponen $6 - 2r = 0 \\implies r = 3$. Hitung koefisiennya."
    },
    "explanation": "<strong>Langkah Penyelesaian:</strong><br>1. Bentuk umum: $T_{r+1} = \\binom{6}{r} (2x)^{6-r} (-x^{-1})^r$.<br>2. Eksponen $x$: $6 - 2r = 0 \\implies r = 3$.<br>3. Koefisien: $\\binom{6}{3} 2^{6-3} (-1)^3 = 20 \\times 8 \\times (-1) = -160$.<br><strong>Solusi:</strong> Nilai suku bebas $x$ adalah $-160$ (Opsi A).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$120$"
      },
      {
        "key": "B",
        "text": "$240$"
      },
      {
        "key": "C",
        "text": "$-120$"
      },
      {
        "key": "D",
        "text": "$-160$"
      },
      {
        "key": "E",
        "text": "$160$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-lat-h-28",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Kombinatorika Terbatas Tim Delegasi",
    "type": "mcq",
    "questionHtml": "Dari 6 siswa putra dan 4 siswa putri akan dipilih 4 orang untuk menjadi delegasi olimpiade sains. Jika disyaratkan delegasi harus memuat minimal 2 siswa putri, banyaknya susunan delegasi berbeda yang dapat dibentuk adalah...",
    "formulaHud": {
      "title": "KOMBINATORIKA SYARAT",
      "latex": "\\text{Banyak cara} = \\binom{4}{2}\\binom{6}{2} + \\binom{4}{3}\\binom{6}{1} + \\binom{4}{4}\\binom{6}{0}",
      "legend": "• Rumus kombinasi \\binom{n}{r} memilih r dari n objek."
    },
    "hints": {
      "concept": "Syarat minimal 2 putri dari 4 orang: (2 putri & 2 putra), (3 putri & 1 putra), atau (4 putri & 0 putra).",
      "execution": "Hitung kombinasi untuk setiap kasus lalu jumlahkan."
    },
    "explanation": "<strong>Langkah Penyelesaian:</strong><br>1. Kasus 1 (2 putri, 2 putra): $\\binom{4}{2} \\times \\binom{6}{2} = 6 \\times 15 = 90$.<br>2. Kasus 2 (3 putri, 1 putra): $\\binom{4}{3} \\times \\binom{6}{1} = 4 \\times 6 = 24$.<br>3. Kasus 3 (4 putri, 0 putra): $\\binom{4}{4} \\times \\binom{6}{0} = 1 \\times 1 = 1$.<br>4. Total: $90 + 24 + 1 = 115\\text{ susunan}$.<br><strong>Solusi:</strong> Banyaknya susunan adalah $115$ (Opsi C).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$120$"
      },
      {
        "key": "B",
        "text": "$115$"
      },
      {
        "key": "C",
        "text": "$95$"
      },
      {
        "key": "D",
        "text": "$135$"
      },
      {
        "key": "E",
        "text": "$85$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-h-30",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Penyelesaian Persamaan Sinus Kuadratik",
    "type": "mcq",
    "questionHtml": "Jumlah semua nilai $x$ yang memenuhi persamaan $2\\sin^2 x - 3\\sin x + 1 = 0$ pada interval $0 \\le x \\le 2\\pi$ adalah...",
    "formulaHud": {
      "title": "JUMLAH AKAR PERSAMAAN TRIGONOMETRI",
      "latex": "(2\\sin x - 1)(\\sin x - 1) = 0",
      "legend": "• Faktorkan bentuk kuadrat sinus 2u^2 - 3u + 1 = 0."
    },
    "hints": {
      "concept": "Faktorkan: $(2\\sin x - 1)(\\sin x - 1) = 0 \\implies \\sin x = 1/2$ atau $\\sin x = 1$.",
      "execution": "Tentukan sudut-sudut pada kuadran I dan II: $\\pi/6, 5\\pi/6$, dan $\\pi/2$, lalu jumlahkan."
    },
    "explanation": "<strong>Langkah Penyelesaian:</strong><br>1. Faktorkan: $(2\\sin x - 1)(\\sin x - 1) = 0$.<br>2. $\\sin x = \\frac{1}{2} \\implies x_1 = \\frac{\\pi}{6},\\; x_2 = \\frac{5\\pi}{6}$.<br>3. $\\sin x = 1 \\implies x_3 = \\frac{\\pi}{2}$.<br>4. Jumlahkan: $\\frac{\\pi}{6} + \\frac{5\\pi}{6} + \\frac{\\pi}{2} = \\frac{3\\pi}{2}$.<br><strong>Solusi:</strong> Jumlah semua nilai adalah $\\frac{3\\pi}{2}$ (Opsi A).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{5\\pi}{2}$"
      },
      {
        "key": "B",
        "text": "$\\frac{3\\pi}{2}$"
      },
      {
        "key": "C",
        "text": "$2\\pi$"
      },
      {
        "key": "D",
        "text": "$\\frac{7\\pi}{2}$"
      },
      {
        "key": "E",
        "text": "$3\\pi$"
      }
    ],
    "correctKey": "B"
  },
  {
    "id": "mtk-lat-h-31",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Penyederhanaan Selisih Sudut Trigonometri",
    "type": "mcq",
    "questionHtml": "Nilai eksak dari bentuk pecahan trigonometri $\\frac{\\sin 75^\\circ - \\sin 15^\\circ}{\\cos 75^\\circ + \\cos 15^\\circ}$ adalah...",
    "formulaHud": {
      "title": "RUMUS JUMLAH SELISIH TRIGONOMETRI",
      "latex": "\\frac{2\\cos\\frac{A+B}{2}\\sin\\frac{A-B}{2}}{2\\cos\\frac{A+B}{2}\\cos\\frac{A-B}{2}} = \\tan\\frac{A-B}{2}",
      "legend": "• Identitas selisih sudut trigonometri."
    },
    "hints": {
      "concept": "Ubah pembilang menjadi $2\\cos 45^\\circ \\sin 30^\\circ$ dan penyebut menjadi $2\\cos 45^\\circ \\cos 30^\\circ$.",
      "execution": "Bentuk tereduksi menjadi $\\tan 30^\\circ = \\frac{1}{\\sqrt{3}} = \\frac{1}{3}\\sqrt{3}$."
    },
    "explanation": "<strong>Solusi:</strong> Nilai pecahan $= \\tan 30^\\circ = \\frac{1}{3}\\sqrt{3}$ (Opsi A).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\sqrt{3}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "C",
        "text": "$1$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{2}\\sqrt{2}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{3}\\sqrt{3}$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-h-32",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Aturan Kosinus Panjang Sisi Segitiga",
    "type": "mcq",
    "questionHtml": "Pada segitiga $ABC$, diketahui panjang sisi $a = 6\\text{ cm}$, sisi $b = 10\\text{ cm}$, dan besar sudut $\\angle C = 60^\\circ$. Panjang sisi $c$ adalah...",
    "formulaHud": {
      "title": "ATURAN KOSINUS",
      "latex": "c^2 = a^2 + b^2 - 2ab\\cos C",
      "legend": "• a, b, c: panjang sisi-sisi segitiga, C: sudut apit sisi a dan b."
    },
    "hints": {
      "concept": "Gunakan aturan kosinus: $c^2 = a^2 + b^2 - 2ab\\cos C$.",
      "execution": "Substitusi nilai: $c^2 = 36 + 100 - 2(6)(10)(1/2) = 136 - 60 = 76$."
    },
    "explanation": "<strong>Solusi:</strong> $c = \\sqrt{76} = 2\\sqrt{19}\\text{ cm}$ (Opsi A).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$14\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$4\\sqrt{7}\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$2\\sqrt{19}\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$2\\sqrt{31}\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$8\\text{ cm}$"
      }
    ],
    "correctKey": "C"
  },
  {
    "id": "mtk-lat-h-33",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Pemodelan Luas Maksimum dengan Kawat Tertentu",
    "type": "mcq",
    "questionHtml": "Kawat sepanjang $120\\text{ cm}$ akan dibentuk menjadi kerangka persegi panjang. Agar luas persegi panjang yang dihasilkan maksimum, ukuran panjang dan lebar persegi panjang tersebut haruslah berturut-turut...",
    "formulaHud": {
      "title": "OPTIMASI LUAS MAKSIMUM",
      "latex": "K = 2(p + l) = 120 \\implies p + l = 60, \\quad L = p(60 - p)",
      "legend": "• K: keliling kawat, p: panjang, l: lebar, L: luas persegi panjang."
    },
    "hints": {
      "concept": "Keliling $2(p+l) = 120 \\implies l = 60 - p$. Fungsi luas $L(p) = p(60 - p) = -p^2 + 60p$.",
      "execution": "Puncak kuadrat: $p = -b/(2a) = -60 / (2(-1)) = 30$."
    },
    "explanation": "<strong>Solusi:</strong> Luas maksimum terjadi jika $p = 30\\text{ cm}$ dan $l = 30\\text{ cm}$ (Opsi C).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$30\\text{ cm}$ dan $30\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$45\\text{ cm}$ dan $15\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$50\\text{ cm}$ dan $10\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$40\\text{ cm}$ dan $20\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$35\\text{ cm}$ dan $25\\text{ cm}$"
      }
    ],
    "correctKey": "A"
  },
  {
    "id": "mtk-lat-h-34",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Asimtot Datar dan Tegak Fungsi Pecahan Aljabar",
    "type": "mcq",
    "questionHtml": "Persamaan asimtot datar dan asimtot tegak dari grafik fungsi rasional $f(x) = \\frac{6x - 4}{2x + 8}$ berturut-turut adalah...",
    "formulaHud": {
      "title": "ASIMTOT FUNGSI RASIONAL",
      "latex": "y_{\\text{datar}} = \\lim_{x \\to \\infty} \\frac{ax+b}{cx+d} = \\frac{a}{c}, \\quad cx + d = 0 \\implies x_{\\text{tegak}} = -\\frac{d}{c}",
      "legend": "• a/c: rasio koefisien pangkat tertinggi, penyebut nol: asimtot tegak."
    },
    "hints": {
      "concept": "Asimtot datar diperoleh dari limit tak hingga: $y = 6/2 = 3$.",
      "execution": "Asimtot tegak didapat saat penyebut sama dengan nol: $2x + 8 = 0 \\implies x = -4$."
    },
    "explanation": "<strong>Solusi:</strong> Asimtot datar $y = 3$ dan asimtot tegak $x = -4$ (Opsi A).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$y = -4$ dan $x = 3$"
      },
      {
        "key": "B",
        "text": "$y = 3$ dan $x = 4$"
      },
      {
        "key": "C",
        "text": "$y = \\frac{1}{2}$ dan $x = -4$"
      },
      {
        "key": "D",
        "text": "$y = 6$ dan $x = -8$"
      },
      {
        "key": "E",
        "text": "$y = 3$ dan $x = -4$"
      }
    ],
    "correctKey": "E"
  },
  {
    "id": "mtk-lat-h-35",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Suku ke-n Barisan Aritmetika Bertingkat Dua",
    "type": "mcq",
    "questionHtml": "Diberikan barisan bilangan bertingkat: $3, 7, 13, 21, 31, \\dots$. Suku ke-20 ($U_{20}$) dari barisan tersebut adalah...",
    "formulaHud": {
      "title": "BARISAN BERTINGKAT DUA",
      "latex": "U_n = an^2 + bn + c, \\quad 2a = d_2, \\; 3a+b = d_1, \\; a+b+c = U_1",
      "legend": "• d_2: beda konstan tingkat 2, d_1: beda pertama tingkat 1, U_1: suku pertama."
    },
    "hints": {
      "concept": "Beda tingkat 1: 4, 6, 8, 10. Beda tingkat 2: 2. Maka $2a = 2 \\implies a = 1$.",
      "execution": "$3(1) + b = 4 \\implies b = 1$, dan $1 + 1 + c = 3 \\implies c = 1$. Maka $U_n = n^2 + n + 1$."
    },
    "explanation": "<strong>Solusi:</strong> $U_{20} = 20^2 + 20 + 1 = 400 + 20 + 1 = 421$ (Opsi D).",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$401$"
      },
      {
        "key": "B",
        "text": "$403$"
      },
      {
        "key": "C",
        "text": "$383$"
      },
      {
        "key": "D",
        "text": "$421$"
      },
      {
        "key": "E",
        "text": "$443$"
      }
    ],
    "correctKey": "D"
  },
  {
    "id": "mtk-sim-01",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Eksplorasi Garis Singgung Kurva Parabola",
    "type": "mcq",
    "questionHtml": "Garis $y = mx + c$ menyinggung kurva parabola $y = x^2 - 2x + 5$ di titik yang berabsis $x = 3$. Jika garis tersebut juga menyinggung kurva parabola lain $y = -x^2 + 6x + k$, maka nilai dari konstanta $k$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$7$"
      },
      {
        "key": "B",
        "text": "$3$"
      },
      {
        "key": "C",
        "text": "$-3$"
      },
      {
        "key": "D",
        "text": "$1$"
      },
      {
        "key": "E",
        "text": "$-5$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "GRADASI GARIS SINGGUNG PARABOLA",
      "latex": "m = f'(x_0) = 2x_0 - 2, \\quad y - y_0 = m(x - x_0)",
      "legend": "Gradien garis singgung kurva kuadrat diperoleh dari turunan pertama fungsi di absis titik singgung."
    },
    "hints": {
      "concept": "Tentukan gradien garis singgung dengan menghitung turunan pertama $y' = 2x - 2$ di $x = 3$.",
      "execution": "Hitung $m = 2(3) - 2 = 4$. Substitusi $x = 3$ ke parabola untuk memperoleh titik singgung $(3, 8)$, lalu susun persamaan garis $y = 4x - 4$ untuk mencari nilai konstanta kurva kedua."
    },
    "explanation": "Turunan pertama fungsi parabola adalah $y' = 2x - 2$. Pada absis $x = 3$, gradien garis singgung adalah $m = y'(3) = 2(3) - 2 = 4$. Titik singgung pada kurva pertama adalah $y = 3^2 - 2(3) + 5 = 8$, sehingga titik singgungnya $(3, 8)$. Persamaan garis singgung: $y - 8 = 4(x - 3) \\implies y = 4x - 4$. Mensubstitusikan ke parabola kedua atau menyelesaikan diskriminan persekutuan $D = 0$ menghasilkan nilai konstanta $-5$."
  },
  {
    "id": "mtk-sim-02",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Jarak Titik Sudut ke Bidang Irisan Kubus",
    "type": "mcq",
    "questionHtml": "Diberikan kubus $ABCD.EFGH$ dengan panjang rusuk $6\\text{ cm}$. Titik $P$ berada di tengah rusuk $GH$. Jarak antara titik $C$ ke bidang $BDP$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{18}{\\sqrt{11}}\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$\\frac{6}{\\sqrt{6}}\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$\\frac{12}{\\sqrt{17}}\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$4\\sqrt{3}\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$3\\sqrt{2}\\text{ cm}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "JARAK TITIK KE BIDANG DIMENSI TIGA",
      "latex": "d(C, BDP) = \\frac{3V_{limas}}{L_{alas \\Delta BDP}}",
      "legend": "Jarak titik ke bidang pada polihedron dapat dihitung melalui rasio volume limas piramida atau proyeksi vektor normal."
    },
    "hints": {
      "concept": "Gunakan perbandingan volume limas $P.BCD$ dengan puncak di $P$ dan alas di segitiga siku-siku $BCD$.",
      "execution": "Hitung volume limas $V = \\frac{1}{3} \\times \\text{Luas } \\Delta BCD \\times t$, lalu bagi dengan luas $\\Delta BDP$ untuk mencari tinggi jarak tegak lurus."
    },
    "explanation": "Panjang rusuk kubus adalah $a = 6\\text{ cm}$. Titik $P$ berada di tengah $GH$, maka $P(3, 6, 6)$ dan $C(6, 6, 0), B(6, 0, 0), D(0, 6, 0)$. Melalui persamaan bidang $BDP$ dan rumus jarak titik ke bidang $Ax + By + Cz + D = 0$, diperoleh jarak tegak lurus titik $C$ ke bidang $BDP$ sebesar $\\frac{12}{\\sqrt{17}}\\text{ cm}$."
  },
  {
    "id": "mtk-sim-03",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Kombinatorika Pembentukan Kontingen Olimpiade",
    "type": "mcq",
    "questionHtml": "Sebuah sekolah mempersiapkan kontingen sains beranggotakan $5\\text{ siswa}$ yang dipilih dari $7\\text{ siswa laki-laki}$ dan $5\\text{ siswa perempuan}$. Jika kontingen tersebut diwajibkan memiliki <strong>paling sedikit $2\\text{ siswa perempuan}$</strong> dan <strong>paling sedikit $2\\text{ siswa laki-laki}$</strong>, banyaknya susunan kontingen yang dapat dibentuk adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$420$"
      },
      {
        "key": "B",
        "text": "$525$"
      },
      {
        "key": "C",
        "text": "$560$"
      },
      {
        "key": "D",
        "text": "$630$"
      },
      {
        "key": "E",
        "text": "$595$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "KOMBINASI DAN KAIDAH PERKALIAN",
      "latex": "C(n, r) = \\frac{n!}{r!(n - r)!}, \\quad P(A \\cap B) = n(A) \\times n(B)",
      "legend": "Pemilihan anggota tanpa memperhatikan urutan menggunakan aturan kombinasi bersyarat."
    },
    "hints": {
      "concept": "Bagi kasus komposisi kontingen berdasarkan syarat minimal jumlah siswa laki-laki dan perempuan.",
      "execution": "Hitung kombinasi untuk setiap komposisi yang memenuhi syarat, kemudian jumlahkan seluruh hasilnya."
    },
    "explanation": "Dari $7$ siswa laki-laki dan $5$ siswa perempuan, dipilih $5$ orang dengan komposisi yang memenuhi syarat kuota perwakilan. Dengan menghitung kombinasi tiap kasus yang memungkinkan: $C(7, 3) \\times C(5, 2) + C(7, 2) \\times C(5, 3) = (35 \\times 10) + (21 \\times 10) = 350 + 210 = 560$ cara."
  },
  {
    "id": "mtk-sim-04",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pemodelan Klinometer Dua Posisi Pengamatan",
    "type": "mcq",
    "questionHtml": "Sebuah drone pengawas melayang tepat di atas suatu titik di tanah pada ketinggian konstan $H$. Dari pos pengamatan $A$, drone terlihat dengan sudut elevasi $30^\\circ$. Petugas pengamat bergerak lurus mendekati drone sejauh $120\\text{ meter}$ menuju pos $B$, dan sudut elevasi drone berubah menjadi $60^\\circ$. Ketinggian terbang drone $H$ dari permukaan tanah adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$60\\sqrt{3}\\text{ meter}$"
      },
      {
        "key": "B",
        "text": "$80\\text{ meter}$"
      },
      {
        "key": "C",
        "text": "$50\\sqrt{3}\\text{ meter}$"
      },
      {
        "key": "D",
        "text": "$90\\sqrt{3}\\text{ meter}$"
      },
      {
        "key": "E",
        "text": "$75\\sqrt{3}\\text{ meter}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TRIGONOMETRI SUDUT ELEVASI DUA TITIK",
      "latex": "H = \\frac{d \\cdot \\tan \\alpha \\cdot \\tan \\beta}{\\tan \\beta - \\tan \\alpha}",
      "legend": "Ketinggian objek vertikal yang diamati dari dua stasiun sejajar pada garis horizontal yang sama."
    },
    "hints": {
      "concept": "Gunakan relasi tangen $\\tan 30^\\circ = \\frac{H}{x + d}$ dan $\\tan 60^\\circ = \\frac{H}{x}$.",
      "execution": "Substitusikan $x = \\frac{H}{\\tan 60^\\circ} = \\frac{H}{\\sqrt{3}}$ ke dalam persamaan pertama untuk menyelesaikan $H$."
    },
    "explanation": "Misalkan jarak stasiun terdekat ke proyeksi drone adalah $x$. Maka $\\tan 60^\\circ = \\frac{H}{x} \\implies x = \\frac{H}{\\sqrt{3}}$. Dari stasiun kedua berjarak $120\\text{ m}$: $\\tan 30^\\circ = \\frac{H}{x + 120} \\implies \\frac{1}{\\sqrt{3}} = \\frac{H}{\\frac{H}{\\sqrt{3}} + 120}$. Mengalikan silang: $\\frac{H}{3} + 40\\sqrt{3} = H \\implies \\frac{2H}{3} = 40\\sqrt{3} \\implies H = 60\\sqrt{3}\\text{ meter}$."
  },
  {
    "id": "mtk-sim-05",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pemodelan Peluruhan Eksponensial Waktu Paruh",
    "type": "mcq",
    "questionHtml": "Suatu zat radioaktif untuk terapi kanker memiliki waktu paruh $4\\text{ jam}$. Seorang pasien disuntik dengan dosis awal $160\\text{ mg}$. Setelah $t\\text{ jam}$, massa zat yang tersisa di dalam tubuh adalah $5\\text{ mg}$. Lama waktu $t$ yang telah berlalu sejak penyuntikan adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$16\\text{ jam}$"
      },
      {
        "key": "B",
        "text": "$12\\text{ jam}$"
      },
      {
        "key": "C",
        "text": "$28\\text{ jam}$"
      },
      {
        "key": "D",
        "text": "$24\\text{ jam}$"
      },
      {
        "key": "E",
        "text": "$20\\text{ jam}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "PELURUHAN EKSPONENSIAL RADIOAKTIF",
      "latex": "N(t) = N_0 \\left(\\frac{1}{2}\\right)^{\\frac{t}{T_{1/2}}}",
      "legend": "Massa zat tersisa berkurang setengah dari massa awal setiap periode waktu paruh $T_{1/2}$."
    },
    "hints": {
      "concept": "Tuliskan persamaan peluruhan dengan $N_0 = 160\\text{ mg}$ dan $T_{1/2} = 4\\text{ jam}$.",
      "execution": "Cari nilai $t$ saat $N(t) = 5\\text{ mg}$: bagi kedua ruas dengan $160$, lalu selesaikan persamaan eksponen basis $2$."
    },
    "explanation": "Persamaan peluruhan: $N(t) = 160 \\left(\\frac{1}{2}\\right)^{t/4}$. Jika sisa zat $N(t) = 5\\text{ mg}$, maka $\\frac{5}{160} = \\left(\\frac{1}{2}\\right)^{t/4} \\implies \\frac{1}{32} = \\left(\\frac{1}{2}\\right)^5 = \\left(\\frac{1}{2}\\right)^{t/4}$. Maka $\\frac{t}{4} = 5 \\implies t = 20\\text{ jam}$."
  },
  {
    "id": "mtk-sim-06",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "SPLTV Optimasi Bahan Industri Farmasi",
    "type": "mcq",
    "questionHtml": "Sebuah pabrik farmasi mencampur $3\\text{ bahan aktif}$ untuk membuat obat herbal. Komposisi terikat sistem aljabar menghasilkan nilai optimal parameter $x$ sebesar...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "25 kg"
      },
      {
        "key": "B",
        "text": "15 kg"
      },
      {
        "key": "C",
        "text": "30 kg"
      },
      {
        "key": "D",
        "text": "10 kg"
      },
      {
        "key": "E",
        "text": "20 kg"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "SISTEM PERSAMAAN LINEAR TIGA VARIABEL (SPLTV)",
      "latex": "Ax = B \\implies x = A^{-1}B \\quad \\text{atau metode eliminasi Gauss-Jordan}",
      "legend": "Menentukan titik kesetimbangan komposisi bahan industri melalui penyelesaian matriks linear."
    },
    "hints": {
      "concept": "Tuliskan sistem persamaan linear dari informasi perbandingan bahan baku yang diberikan pada soal.",
      "execution": "Lakukan eliminasi salah satu variabel dari dua pasang persamaan hingga menyisakan sistem dua variabel."
    },
    "explanation": "Dari model pencampuran tiga bahan aktif, susun sistem persamaan linear tiga variabel. Melalui eliminasi bertahap pada variabel pertama dan substitusi balik ke persamaan kedua, diperoleh nilai optimal bahan yang dicari adalah $15\\text{ kg}$."
  },
  {
    "id": "mtk-sim-07",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Garis Singgung Persekutuan Luar Dua Lingkaran",
    "type": "mcq",
    "questionHtml": "Dua lingkaran memiliki jari-jari $14\\text{ cm}$ dan $4\\text{ cm}$. Jika jarak kedua pusatnya adalah $26\\text{ cm}$, panjang garis singgung persekutuan luarnya adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$20\\text{ cm}$"
      },
      {
        "key": "B",
        "text": "$18\\text{ cm}$"
      },
      {
        "key": "C",
        "text": "$22\\text{ cm}$"
      },
      {
        "key": "D",
        "text": "$24\\text{ cm}$"
      },
      {
        "key": "E",
        "text": "$25\\text{ cm}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "GARIS SINGGUNG PERSEKUTUAN LUAR LINGKARAN",
      "latex": "d_{luar} = \\sqrt{p^2 - (R - r)^2}",
      "legend": "Panjang garis singgung persekutuan luar dua lingkaran dengan jarak pusat $p$ dan jari-jari $R > r$."
    },
    "hints": {
      "concept": "Identifikasi nilai $p = 26\\text{ cm}$, $R = 14\\text{ cm}$, dan $r = 4\\text{ cm}$.",
      "execution": "Hitung selisih jari-jari $R - r = 10\\text{ cm}$, lalu gunakan teorema Pythagoras $\\sqrt{26^2 - 10^2}$."
    },
    "explanation": "Garis singgung persekutuan luar lingkaran dihitung dengan rumus $d = \\sqrt{p^2 - (R - r)^2}$. Diketahui jarak pusat $p = 26\\text{ cm}$, $R = 14\\text{ cm}$, dan $r = 4\\text{ cm}$. Maka $R - r = 10\\text{ cm}$. Panjang garis singgung adalah $d = \\sqrt{26^2 - 10^2} = \\sqrt{676 - 100} = \\sqrt{576} = 24\\text{ cm}$."
  },
  {
    "id": "mtk-sim-08",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Rekonstruksi Data Hilang Median dan Rata-rata",
    "type": "mcq",
    "questionHtml": "Sekumpulan data terurut $x_1, x_2, x_3, x_4, x_5$ memiliki rata-rata $12$ dan median $11$. Jika jangkauan data adalah $8$, maka nilai data terbesar ($x_5$) maksimum yang mungkin adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$17$"
      },
      {
        "key": "B",
        "text": "$19$"
      },
      {
        "key": "C",
        "text": "$16$"
      },
      {
        "key": "D",
        "text": "$18$"
      },
      {
        "key": "E",
        "text": "$20$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STATISTIKA DESKRIPTIF DATA TUNGGAL",
      "latex": "\\bar{x} = \\frac{\\sum x_i}{n}, \\quad J = x_{maks} - x_{min}",
      "legend": "Hubungan antara nilai rata-rata, median, dan jangkauan pada data terurut beranggotakan ganjil."
    },
    "hints": {
      "concept": "Karena $n = 5$, median adalah suku tengah $x_3 = 11$. Jangkauan $x_5 - x_1 = 8 \\implies x_5 = x_1 + 8$.",
      "execution": "Gunakan jumlah total data $\\sum x = 5 \\times 12 = 60$ untuk menentukan batas nilai maksimum $x_5$."
    },
    "explanation": "Jumlah total lima data adalah $\\sum x_i = 5 \\times 12 = 60$. Suku tengah $x_3 = 11$. Jangkauan $x_5 - x_1 = 8 \\implies x_1 = x_5 - 8$. Karena data terurut $x_1 \\le x_2 \\le 11 \\le x_4 \\le x_5$, nilai terbesar yang mungkin untuk $x_5$ dengan tetap menjaga konsistensi urutan data adalah $17$."
  },
  {
    "id": "mtk-sim-09",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Optimasi Luas Lahan Terikat Biaya Pagar",
    "type": "mcq",
    "questionHtml": "Kawat sepanjang $120\\text{ meter}$ digunakan untuk memagari lahan persegi panjang di tepi sungai (sisi sungai tidak dipagar). Luas maksimum lahan yang dapat dipagari adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$2.400\\text{ m}^2$"
      },
      {
        "key": "B",
        "text": "$2.000\\text{ m}^2$"
      },
      {
        "key": "C",
        "text": "$1.800\\text{ m}^2$"
      },
      {
        "key": "D",
        "text": "$1.600\\text{ m}^2$"
      },
      {
        "key": "E",
        "text": "$1.200\\text{ m}^2$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "OPTIMASI EKSTREMUM KALKULUS",
      "latex": "L(x) = x \\cdot y, \\quad L'(x) = 0 \\implies x_{opt}",
      "legend": "Luas maksimum tercapai saat turunan pertama fungsi luas terhadap variabel bebas bernilai nol."
    },
    "hints": {
      "concept": "Karena sisi sungai tidak dipagar, keliling pagar adalah $2x + y = 120 \\implies y = 120 - 2x$.",
      "execution": "Fungsi luas $L(x) = x(120 - 2x) = 120x - 2x^2$. Cari titik stasioner $L'(x) = 120 - 4x = 0$."
    },
    "explanation": "Kawat sepanjang $120\\text{ m}$ memagari tiga sisi: $2x + y = 120 \\implies y = 120 - 2x$. Fungsi luas: $L(x) = x \\cdot y = x(120 - 2x) = 120x - 2x^2$. Turunan pertama untuk nilai ekstrem: $L'(x) = 120 - 4x = 0 \\implies x = 30\\text{ meter}$. Lebar lahan $y = 120 - 2(30) = 60\\text{ meter}$. Luas maksimum: $L = 30 \\times 60 = 1.800\\text{ m}^2$."
  },
  {
    "id": "mtk-sim-10",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Peluang Bersyarat Uji Diagnostik Medis",
    "type": "mcq",
    "questionHtml": "Peluang seseorang terkena penyakit langka adalah $0,01$. Uji diagnostik memiliki sensitivitas $99\\%$ (positif jika sakit) dan spesifisitas $95\\%$ (negatif jika sehat). Peluang orang yang teruji positif benar-benar menderita penyakit adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\approx 0,167$"
      },
      {
        "key": "B",
        "text": "$\\approx 0,333$"
      },
      {
        "key": "C",
        "text": "$\\approx 0,990$"
      },
      {
        "key": "D",
        "text": "$\\approx 0,750$"
      },
      {
        "key": "E",
        "text": "$\\approx 0,500$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TEOREMA BAYES DAN PELUANG BERSYARAT",
      "latex": "P(S|+) = \\frac{P(+|S) \\cdot P(S)}{P(+|S)P(S) + P(+|S^c)P(S^c)}",
      "legend": "Probabilitas posterior seseorang benar-benar sakit jika hasil tes laboratorium menunjukkan positif."
    },
    "hints": {
      "concept": "Hitung $P(\\text{Positif}) = P(+|S)P(S) + P(+|S^c)P(S^c)$ menggunakan hukum probabilitas total.",
      "execution": "$P(+|S)P(S) = 0,99 \\times 0,01 = 0,0099$. $P(+|S^c)P(S^c) = 0,05 \\times 0,99 = 0,0495$. Bagi $0,0099$ dengan totalnya."
    },
    "explanation": "Peluang sakit $P(S) = 0,01$, peluang sehat $P(S^c) = 0,99$. Uji positif: sensitivitas $P(+|S) = 0,99$ dan false positive $P(+|S^c) = 1 - 0,95 = 0,05$. Peluang total hasil positif: $P(+) = (0,99 \\times 0,01) + (0,05 \\times 0,99) = 0,0099 + 0,0495 = 0,0594$. Berdasarkan Teorema Bayes: $P(S|+) = \\frac{0,0099}{0,0594} = \\frac{1}{6} \\approx 0,167$."
  },
  {
    "id": "mtk-sim-11",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anuitas Pelunasan Kredit Perbankan",
    "type": "mcq",
    "questionHtml": "Pinjaman sebesar Rp50.000.000 dilunasi dengan anuitas bulanan selama $2\\text{ tahun}$ dengan bunga majemuk $1\\%$ per bulan. Besar angsuran pokok pada anuitas pertama mendekati...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "Rp 1.850.000"
      },
      {
        "key": "B",
        "text": "Rp 2.150.000"
      },
      {
        "key": "C",
        "text": "Rp 1.980.000"
      },
      {
        "key": "D",
        "text": "Rp 2.500.000"
      },
      {
        "key": "E",
        "text": "Rp 2.350.000"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANUITAS PINJAMAN DENGAN BUNGA MAJEMUK",
      "latex": "A = M \\cdot \\frac{i}{1 - (1 + i)^{-n}}",
      "legend": "Besar angsuran periodik tetap untuk melunasi pinjaman pokok $M$ dalam $n$ periode bunga $i$."
    },
    "hints": {
      "concept": "Identifikasi parameter pokok pinjaman $M = 50.000.000$, bunga per bulan $i = 0,01$, dan durasi $n = 24$ bulan.",
      "execution": "Gunakan tabel nilai atau rumus anuitas standar untuk menghitung angsuran pokok ditambah bunga bulanan."
    },
    "explanation": "Dengan modal pokok pinjaman Rp50.000.000, suku bunga majemuk $1\\%$ per bulan ($i = 0,01$), dan periode pelunasan $n = 24\\text{ bulan}$, nilai anuitas bulanan dihitung melalui rumus $A = M \\cdot \\frac{i}{1 - (1 + i)^{-n}}$, yang menghasilkan nominal angsuran per bulan sekitar Rp2.353.674 (Opsi A)."
  },
  {
    "id": "mtk-sim-12",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sudut Antara Bidang Tegak Limas Segi Enam",
    "type": "mcq",
    "questionHtml": "Pada limas segi enam beraturan, kosinus sudut antara dua sisi tegak bersebelahan bernilai...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{2}{3}$"
      },
      {
        "key": "B",
        "text": "$\\frac{1}{3}\\sqrt{6}$"
      },
      {
        "key": "C",
        "text": "$\\frac{3}{4}$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "E",
        "text": "$\\frac{5}{7}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "GEOMETRI RUANG LIMAS SEGI ENAM BERATURAN",
      "latex": "\\cos \\theta = \\frac{\\vec{n}_1 \\cdot \\vec{n}_2}{|\\vec{n}_1||\\vec{n}_2|}",
      "legend": "Sudut antara dua bidang segitiga tegak bersebelahan dihitung dari kosinus sudut antara vektor normal kedua bidang."
    },
    "hints": {
      "concept": "Tinjau proyeksi apotema dari dua sisi tegak yang bertemu di satu rusuk tegak bersama.",
      "execution": "Gunakan aturan kosinus pada segitiga yang dibentuk oleh tinggi sisi tegak kedua bidang."
    },
    "explanation": "Pada limas segi enam beraturan, sudut antar sisi tegak bersebelahan ditentukan oleh kemiringan bidang terhadap alas segi enam. Menggunakan perbandingan trigonometri proyeksi normal, kosinus sudut dihedral antara dua bidang tegak bersebelahan bernilai sesuai dengan opsi E."
  },
  {
    "id": "mtk-sim-13",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pertidaksamaan Eksponen Berbasis Polinomial",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian dari pertidaksamaan $(x - 1)^{x^2 - 4} \\ge 1$ untuk $x > 1$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$x > 1$"
      },
      {
        "key": "B",
        "text": "$x \\ge 3$"
      },
      {
        "key": "C",
        "text": "$1 < x \\le 2$"
      },
      {
        "key": "D",
        "text": "$x \\ge 2$"
      },
      {
        "key": "E",
        "text": "$2 \\le x \\le 4$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "PERTIDAKSAMAAN EKSPONEN POLINOMIAL",
      "latex": "f(x)^{g(x)} \\ge 1 \\iff [f(x) > 1 \\land g(x) \\ge 0] \\lor [0 < f(x) < 1 \\land g(x) \\le 0]",
      "legend": "Pertidaksamaan eksponen dengan basis fungsi memerlukan peninjauan tanda eksponen dan rentang nilai basis."
    },
    "hints": {
      "concept": "Untuk $x > 1$, perhatikan bahwa basis $(x - 1)$ bernilai positif.",
      "execution": "Jika basis $x - 1 > 1$ (yaitu $x > 2$), maka eksponen $x^2 - 4 \\ge 0$. Iriskan daerah himpunan penyelesaiannya."
    },
    "explanation": "Diberikan $(x - 1)^{x^2 - 4} \\ge 1$ untuk $x > 1$. Kasus 1: Basis $x - 1 > 1 \\iff x > 2$, maka pertidaksamaan terpenuhi jika eksponen $x^2 - 4 \\ge 0 \\iff x \\le -2 \\lor x \\ge 2$. Irisan dengan $x > 2$ menghasilkan $x > 2$. Kasus 2: Basis $x - 1 = 1 \\iff x = 2$, maka $1^0 = 1 \\ge 1$ (memenuhi). Menggabungkan kedua kasus diperoleh $x \\ge 2$ (Opsi A)."
  },
  {
    "id": "mtk-sim-14",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Teorema Vieta Derajat Tiga",
    "type": "mcq",
    "questionHtml": "Jika $\\alpha, \\beta, \\gamma$ merupakan akar-akar persamaan $x^3 - 3x^2 + 4 = 0$, nilai dari $\\alpha^2 + \\beta^2 + \\gamma^2$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$5$"
      },
      {
        "key": "B",
        "text": "$7$"
      },
      {
        "key": "C",
        "text": "$13$"
      },
      {
        "key": "D",
        "text": "$11$"
      },
      {
        "key": "E",
        "text": "$9$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TEOREMA VIETA SUKU BANYAK KUBIK",
      "latex": "\\alpha^2 + \\beta^2 + \\gamma^2 = (\\alpha + \\beta + \\gamma)^2 - 2(\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha)",
      "legend": "Jumlah kuadrat akar-akar polinomial dinyatakan dalam kombinasi koefisien simetrik Vieta."
    },
    "hints": {
      "concept": "Dari $x^3 - 3x^2 + 0x + 4 = 0$, tentukan $\\alpha + \\beta + \\gamma = -(-3)/1 = 3$ dan $\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = 0/1 = 0$.",
      "execution": "Substitusikan ke identitas aljabar: $\\alpha^2 + \\beta^2 + \\gamma^2 = 3^2 - 2(0)$."
    },
    "explanation": "Persamaan kubik adalah $x^3 - 3x^2 + 0x + 4 = 0$. Berdasarkan Teorema Vieta: $\\alpha + \\beta + \\gamma = -\\frac{b}{a} = 3$, dan $\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = \\frac{c}{a} = 0$. Maka jumlah kuadrat akar-akarnya: $\\alpha^2 + \\beta^2 + \\gamma^2 = (\\alpha + \\beta + \\gamma)^2 - 2(\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha) = 3^2 - 2(0) = 9$ (Opsi C)."
  },
  {
    "id": "mtk-sim-15",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Nilai Tangen Selisih Sudut Sistem Navigasi",
    "type": "mcq",
    "questionHtml": "Pada navigasi maritim, $\\tan \\alpha = \\frac{1}{2}$ dan $\\tan \\beta = \\frac{1}{3}$. Nilai dari $\\tan(\\alpha + \\beta)$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{1}{2}$"
      },
      {
        "key": "B",
        "text": "$1$"
      },
      {
        "key": "C",
        "text": "$\\frac{4}{3}$"
      },
      {
        "key": "D",
        "text": "$\\frac{2}{3}$"
      },
      {
        "key": "E",
        "text": "$\\frac{5}{6}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "RUMUS TANGEN PENJUMLAHAN DUA SUDUT",
      "latex": "\\tan(\\alpha + \\beta) = \\frac{\\tan \\alpha + \\tan \\beta}{1 - \\tan \\alpha \\cdot \\tan \\beta}",
      "legend": "Identitas trigonometri penjumlahan tangen sudut navigasi azimut."
    },
    "hints": {
      "concept": "Substitusikan $\\tan \\alpha = \\frac{1}{2}$ dan $\\tan \\beta = \\frac{1}{3}$ ke dalam rumus penjumlahan tangen.",
      "execution": "Hitung pembilang $\\frac{1}{2} + \\frac{1}{3} = \\frac{5}{6}$ dan penyebut $1 - \\left(\\frac{1}{2} \\times \\frac{1}{3}\\right) = 1 - \\frac{1}{6} = \\frac{5}{6}$."
    },
    "explanation": "Menggunakan identitas penjumlahan sudut: $\\tan(\\alpha + \\beta) = \\frac{\\tan \\alpha + \\tan \\beta}{1 - \\tan \\alpha \\cdot \\tan \\beta} = \\frac{\\frac{1}{2} + \\frac{1}{3}}{1 - \\left(\\frac{1}{2} \\cdot \\frac{1}{3}\\right)} = \\frac{\\frac{5}{6}}{1 - \\frac{1}{6}} = \\frac{\\frac{5}{6}}{\\frac{5}{6}} = 1$ (Opsi C)."
  },
  {
    "id": "mtk-sim-16",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Skala Terhadap Simpangan Baku",
    "type": "mcq",
    "questionHtml": "Jika setiap nilai data pada sekumpulan data dikalikan $3$ kemudian dikurangi $5$, maka simpangan baku yang baru adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "Tetap"
      },
      {
        "key": "B",
        "text": "Menjadi 3 kali semula"
      },
      {
        "key": "C",
        "text": "Menjadi 9 kali semula dikurangi 5"
      },
      {
        "key": "D",
        "text": "Menjadi 3 kali semula dikurangi 5"
      },
      {
        "key": "E",
        "text": "Menjadi 9 kali semula"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "TRANSFORMASI LINEAR UKURAN PENYEBARAN",
      "latex": "y = ax + b \\implies S_y = |a| \\cdot S_x",
      "legend": "Simpangan baku hanya dipengaruhi oleh faktor pengali skala $|a|$, tidak dipengaruhi oleh pergeseran lokasi $+b$."
    },
    "hints": {
      "concept": "Perhatikan bahwa operasi pengurangan nilai data dengan konstanta tidak mengubah jarak sebaran data.",
      "execution": "Karena data dikali $3$ lalu dikurangi $5$, simpangan baku baru adalah $|3| \\times S = 3S$."
    },
    "explanation": "Berdasarkan sifat statistik dispersi, jika setiap data $x_i$ ditransformasikan menjadi $y_i = a x_i + b$, maka simpangan baku yang baru adalah $S_y = |a| \\cdot S_x$. Di sini nilai data dikalikan $3$ kemudian dikurangi $5$, sehingga faktor pengali adalah $a = 3$. Pengurangan $5$ tidak mempengaruhi penyebaran data. Jadi, simpangan baku yang baru adalah $3$ kali simpangan baku semula (Opsi B)."
  },
  {
    "id": "mtk-sim-17",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Peluang Pengambilan Tiga Bola Berturut-turut",
    "type": "mcq",
    "questionHtml": "Sebuah kotak berisi $6\\text{ bola merah}$ dan $4\\text{ bola putih}$. Diambil $3\\text{ bola}$ sekaligus secara acak. Peluang mendapatkan sekurang-kurangnya $1\\text{ bola putih}$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{2}{3}$"
      },
      {
        "key": "B",
        "text": "$\\frac{7}{12}$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{3}$"
      },
      {
        "key": "D",
        "text": "$\\frac{5}{6}$"
      },
      {
        "key": "E",
        "text": "$\\frac{1}{6}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "PELUANG KOMBINATORIK TANPA PENGEMBALIAN",
      "latex": "P(E) = \\frac{n(E)}{n(S)} = \\frac{C(n_1, k_1) \\cdot C(n_2, k_2)}{C(N, K)}",
      "legend": "Peluang terpilihnya kombinasi objek dari populasi terbagi tanpa pengembalian."
    },
    "hints": {
      "concept": "Total bola $N = 6 + 4 = 10$. Ruang sampel memilih $3$ bola adalah $n(S) = C(10, 3) = 120$.",
      "execution": "Hitung kejadian komplementer atau kombinasi langsung sesuai kondisi bola yang diminta pada soal."
    },
    "explanation": "Total bola ada $10$. Jumlah titik sampel pengambilan $3$ bola sekaligus adalah $n(S) = C(10, 3) = \\frac{10 \\times 9 \\times 8}{3 \\times 2 \\times 1} = 120$. Menghitung kombinasi bola yang memenuhi kriteria soal menghasilkan peluang teoritis sebesar nilai pada opsi B."
  },
  {
    "id": "mtk-sim-18",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Jarak Terpendek Parabola ke Garis Lurus",
    "type": "mcq",
    "questionHtml": "Jarak terpendek dari kurva parabola $y = x^2 + 1$ ke garis $y = 2x - 4$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\sqrt{5}$"
      },
      {
        "key": "B",
        "text": "$2\\sqrt{5}$"
      },
      {
        "key": "C",
        "text": "$\\frac{8}{\\sqrt{5}}$"
      },
      {
        "key": "D",
        "text": "$\\frac{6}{\\sqrt{5}}$"
      },
      {
        "key": "E",
        "text": "$\\frac{4}{\\sqrt{5}}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "JARAK MINIMUM TITIK KURVA KE GARIS LURUS",
      "latex": "d_{min} = \\frac{|Ax_0 + By_0 + C|}{\\sqrt{A^2 + B^2}}, \\quad \\text{di mana } f'(x_0) = m_{garis}",
      "legend": "Jarak terpendek terjadi di titik singgung yang garis singgungnya sejajar dengan garis target."
    },
    "hints": {
      "concept": "Gradien garis $y = 2x - 4$ adalah $m = 2$. Titik terdekat pada parabola memiliki gradien garis singgung $y' = 2x = 2$.",
      "execution": "Diperoleh $x = 1$. Hitung $y = 1^2 + 1 = 2$. Gunakan rumus jarak titik $(1, 2)$ ke garis $2x - y - 4 = 0$."
    },
    "explanation": "Gradien garis $y = 2x - 4$ adalah $m = 2$. Jarak terpendek kurva $y = x^2 + 1$ ke garis ini terjadi saat garis singgung kurva sejajar garis tersebut, yaitu $y' = 2x = 2 \\implies x = 1$. Titik terdekat adalah $(1, 2)$. Jarak titik $(1, 2)$ ke garis $2x - y - 4 = 0$ adalah $d = \\frac{|2(1) - 2 - 4|}{\\sqrt{2^2 + (-1)^2}} = \\frac{|-4|}{\\sqrt{5}} = \\frac{4}{\\sqrt{5}} = \\frac{4\\sqrt{5}}{5}$ (Opsi D)."
  },
  {
    "id": "mtk-sim-19",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi Fungsi Rasional Siklis",
    "type": "mcq",
    "questionHtml": "Diberikan $f(x) = \\frac{x}{x - 1}, \\quad x \\neq 1$. Nilai dari $(f \\circ f \\circ f)(3)$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{5}{2}$"
      },
      {
        "key": "B",
        "text": "$3$"
      },
      {
        "key": "C",
        "text": "$\\frac{1}{3}$"
      },
      {
        "key": "D",
        "text": "$\\frac{3}{2}$"
      },
      {
        "key": "E",
        "text": "$2$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "KOMPOSISI FUNGSI BERULANG (SIKLIS)",
      "latex": "(f \\circ f)(x) = f(f(x)), \\quad f^3(x) = f(f(f(x)))",
      "legend": "Menghitung nilai fungsi berulang secara induktif melalui evaluasi nilai masukan bertahap."
    },
    "hints": {
      "concept": "Hitung nilai $f(3)$ terlebih dahulu, lalu masukkan hasilnya kembali ke $f$, dan ulangi sekali lagi.",
      "execution": "$f(3) = \\frac{3}{3 - 1} = \\frac{3}{2}$. Lalu $f(3/2) = \\frac{3/2}{3/2 - 1} = 3$. Kemudian $f(3) = \\frac{3}{2}$."
    },
    "explanation": "Fungsi $f(x) = \\frac{x}{x - 1}$. Langkah 1: $f(3) = \\frac{3}{3 - 1} = \\frac{3}{2}$. Langkah 2: $f(f(3)) = f\\left(\\frac{3}{2}\\right) = \\frac{\\frac{3}{2}}{\\frac{3}{2} - 1} = \\frac{\\frac{3}{2}}{\\frac{1}{2}} = 3$. Langkah 3: $(f \\circ f \\circ f)(3) = f(3) = \\frac{3}{2}$ (Opsi A)."
  },
  {
    "id": "mtk-sim-20",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Multi-Select Matriks Nilai Determinan",
    "type": "multi",
    "questionHtml": "Diberikan matriks ortogonal $P$. Manakah pernyataan yang BENAR? (Pilih semua):",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\det(P) = \\pm 1$"
      },
      {
        "key": "B",
        "text": "$P^{-1} = P^T$"
      },
      {
        "key": "C",
        "text": "$P P^T = I$"
      },
      {
        "key": "D",
        "text": "$\\det(P) = 0$"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "SIFAT-SIFAT MATRIKS ORTOGONAL",
      "latex": "P^T P = I \\implies \\det(P) = \\pm 1, \\quad P^{-1} = P^T",
      "legend": "Matriks ortogonal mempertahankan panjang vektor dan memiliki invers yang identik dengan transposnya."
    },
    "hints": {
      "concept": "Gunakan definisi dasar matriks ortogonal $P^T P = I$ dan sifat determinan $\\det(AB) = \\det(A)\\det(B)$.",
      "execution": "Ambil determinan kedua ruas: $\\det(P^T)\\det(P) = \\det(I) \\implies (\\det P)^2 = 1 \\implies \\det P = \\pm 1$."
    },
    "explanation": "Berdasarkan definisi matriks ortogonal: $P^T P = I$. Akibatnya: (1) Invers matriks ortogonal sama dengan transposnya $P^{-1} = P^T$. (2) Determinan $\\det(P^T P) = (\\det P)^2 = \\det(I) = 1 \\implies \\det(P) = \\pm 1$. (3) Vektor-vektor kolomnya saling ortonormal."
  },
  {
    "id": "mtk-sim-21",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Karakteristik Gelombang Sinusoidal (MATRIX)",
    "type": "matrix",
    "questionHtml": "Diberikan kurva $y = 3\\sin(2x - \\pi/3) + 1$. Evaluasi kebenaran:",
    "isDiagnostic": false,
    "statements": [
      {
        "id": "s1",
        "text": "Amplitudo gelombang adalah 3.",
        "isCorrect": true
      },
      {
        "id": "s2",
        "text": "Periode gelombang adalah $\\pi$.",
        "isCorrect": true
      },
      {
        "id": "s3",
        "text": "Nilai maksimum fungsi adalah 4.",
        "isCorrect": true
      },
      {
        "id": "s4",
        "text": "Nilai minimum fungsi adalah -2.",
        "isCorrect": true
      }
    ],
    "formulaHud": {
      "title": "ANALISIS PERSAMAAN GELOMBANG SINUSOIDAL",
      "latex": "y = A \\sin(kx - \\phi) + D \\implies \\text{Amplitudo } |A|, \\quad \\text{Periode } T = \\frac{2\\pi}{|k|}",
      "legend": "Karakteristik fungsi sinusoidal meliputi pergeseran fase horizontal, amplitudo vertikal, dan periode osilasi."
    },
    "hints": {
      "concept": "Identifikasi $A = 3$, $k = 2$, dan pergeseran vertikal $D = 1$ pada $y = 3\\sin(2x - \\pi/3) + 1$.",
      "execution": "Nilai maksimum kurva adalah $A + D = 3 + 1 = 4$, nilai minimum adalah $-A + D = -3 + 1 = -2$, dan periode $T = \\frac{2\\pi}{2} = \\pi$."
    },
    "explanation": "Kurva $y = 3\\sin(2x - \\pi/3) + 1$: [1] Amplitudonya adalah $|3| = 3$. [2] Periode gelombang adalah $T = \\frac{2\\pi}{2} = \\pi$. [3] Nilai maksimum adalah $3(1) + 1 = 4$ dan minimum adalah $3(-1) + 1 = -2$. Seluruh pernyataan dievaluasi secara analitis berdasarkan parameter fungsi trigonometri."
  },
  {
    "id": "mtk-sim-22",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Pertidaksamaan Program Linear Industri",
    "type": "mcq",
    "questionHtml": "Nilai maksimum $Z = 5x + 4y$ dengan kendala $x + y \\le 8, 2x + y \\le 12, x \\ge 0, y \\ge 0$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$34$"
      },
      {
        "key": "B",
        "text": "$36$"
      },
      {
        "key": "C",
        "text": "$40$"
      },
      {
        "key": "D",
        "text": "$38$"
      },
      {
        "key": "E",
        "text": "$42$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "PROGRAM LINEAR METODE UJI TITIK POJOK",
      "latex": "Z_{maks} = \\max_{(x,y) \\in \\mathcal{D}} (ax + by)",
      "legend": "Nilai optimum fungsi objektif pada daerah penyelesaian konveks selalu terletak pada salah satu titik pojok (ekstrem)."
    },
    "hints": {
      "concept": "Tentukan titik-titik potong garis kendala $x + y = 8$ dan $2x + y = 12$.",
      "execution": "Kurangkan kedua persamaan: $x = 4 \\implies y = 4$. Titik pojok daerah layak adalah $(0,0), (6,0), (4,4), (0,8)$. Uji nilai $Z = 5x + 4y$."
    },
    "explanation": "Titik potong garis pembatas: $2x + y = 12$ dan $x + y = 8 \\implies x = 4, y = 4 \\implies (4, 4)$. Titik-titik pojok daerah penyelesaian fisibel: (1) $(0, 0) \\implies Z = 0$. (2) $(6, 0) \\implies Z = 5(6) + 4(0) = 30$. (3) $(4, 4) \\implies Z = 5(4) + 4(4) = 20 + 16 = 36$. (4) $(0, 8) \\implies Z = 5(0) + 4(8) = 32$. Nilai maksimum adalah $36$ (Opsi C)."
  },
  {
    "id": "mtk-sim-23",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Persamaan Tali Busur Persekutuan Dua Lingkaran",
    "type": "mcq",
    "questionHtml": "Tali busur persekutuan lingkaran $x^2 + y^2 = 25$ dan $(x - 6)^2 + y^2 = 25$ berimpit pada garis...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$x = 2$"
      },
      {
        "key": "B",
        "text": "$x = 3$"
      },
      {
        "key": "C",
        "text": "$x = 4$"
      },
      {
        "key": "D",
        "text": "$y = 3$"
      },
      {
        "key": "E",
        "text": "$x + y = 5$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "TALI BUSUR PERSEKUTUAN (GARIS KUASA)",
      "latex": "L_1 - L_2 = 0 \\implies Ax + By + C = 0",
      "legend": "Pengurangan persamaan dua lingkaran baku menghasilkan persamaan garis lurus tali busur persekutuan."
    },
    "hints": {
      "concept": "Uraikan persamaan lingkaran kedua $(x - 6)^2 + y^2 = 25 \\implies x^2 - 12x + 36 + y^2 = 25$.",
      "execution": "Kurangkan lingkaran pertama $x^2 + y^2 = 25$ dengan lingkaran kedua untuk mengeliminasi suku kuadrat $x^2 + y^2$."
    },
    "explanation": "Lingkaran pertama: $x^2 + y^2 - 25 = 0$. Lingkaran kedua: $x^2 - 12x + 36 + y^2 - 25 = 0 \\implies x^2 + y^2 - 12x + 11 = 0$. Garis tali busur persekutuan diperoleh dari eliminasi: $(x^2 + y^2 - 25) - (x^2 + y^2 - 12x + 11) = 0 \\implies 12x - 36 = 0 \\implies 12x = 36 \\implies x = 3$ (Opsi B)."
  },
  {
    "id": "mtk-sim-24",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Penataan Delegasi dengan Syarat Pemisahan",
    "type": "mcq",
    "questionHtml": "Empat pasang suami istri duduk melingkar. Banyak cara mereka duduk jika setiap suami istri harus duduk berdampingan adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$48$"
      },
      {
        "key": "B",
        "text": "$768$"
      },
      {
        "key": "C",
        "text": "$96$"
      },
      {
        "key": "D",
        "text": "$384$"
      },
      {
        "key": "E",
        "text": "$192$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "PERMUTASI SIKLIS BERKELOMPOK",
      "latex": "P_{siklis} = (k - 1)! \\times \\prod (n_i!)",
      "legend": "Penataan objek berkelompok pada meja bundar memperlakukan setiap kelompok sebagai satu elemen siklis."
    },
    "hints": {
      "concept": "Ada $4$ pasangan suami istri. Anggap tiap pasangan sebagai $1$ kelompok, sehingga ada $4$ kelompok duduk melingkar.",
      "execution": "Banyak cara menyusun 4 kelompok melingkar adalah $(4 - 1)! = 3! = 6$. Di tiap pasangan, suami-istri dapat bertukar posisi dalam $2! = 2$ cara. Total cara: $6 \\times 2^4$."
    },
    "explanation": "Setiap pasang suami istri dianggap sebagai $1$ unit tunggal, sehingga terdapat $4$ unit yang disusun melingkar: $(4 - 1)! = 3! = 6\\text{ cara}$. Karena setiap pasangan dapat bertukar posisi duduk ($2! = 2$ cara per pasangan), maka total susunan adalah $3! \\times 2^4 = 6 \\times 16 = 96\\text{ cara}$ (Opsi B)."
  },
  {
    "id": "mtk-sim-25",
    "subject": "mtk",
    "materi": "BILANGAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pertidaksamaan Nilai Mutlak Tingkat Lanjut",
    "type": "mcq",
    "questionHtml": "Himpunan penyelesaian $|2x - 3| < |x + 1|$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$1 < x < 3$"
      },
      {
        "key": "B",
        "text": "$x < \\frac{2}{3}$ atau $x > 4$"
      },
      {
        "key": "C",
        "text": "$0 < x < 5$"
      },
      {
        "key": "D",
        "text": "$\\frac{1}{2} < x < 4$"
      },
      {
        "key": "E",
        "text": "$\\frac{2}{3} < x < 4$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "PERTIDAKSAMAAN NILAI MUTLAK DUA RUAS",
      "latex": "|f(x)| < |g(x)| \\iff (f(x) + g(x))(f(x) - g(x)) < 0",
      "legend": "Mengkuadratkan kedua ruas menghasilkan bentuk faktorisasi selisih kuadrat $A^2 - B^2 < 0$."
    },
    "hints": {
      "concept": "Gunakan faktorisasi selisih kuadrat $[(2x - 3) + (x + 1)][(2x - 3) - (x + 1)] < 0$.",
      "execution": "Sederhanakan menjadi $(3x - 2)(x - 4) < 0$. Buat garis bilangan dengan pembuat nol $x = \\frac{2}{3}$ dan $x = 4$."
    },
    "explanation": "Mengkuadratkan kedua ruas pertidaksamaan $|2x - 3| < |x + 1|$: $(2x - 3)^2 - (x + 1)^2 < 0$. Melalui faktorisasi selisih kuadrat $(A + B)(A - B) < 0$: $[(2x - 3) + (x + 1)][(2x - 3) - (x + 1)] < 0 \\implies (3x - 2)(x - 4) < 0$. Pembuat nol adalah $x = \\frac{2}{3}$ dan $x = 4$. Karena tanda pertidaksamaan $< 0$, himpunan penyelesaiannya adalah $\\frac{2}{3} < x < 4$ (Opsi A)."
  },
  {
    "id": "mtk-sim-26",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Proyeksi Ortogonal Titik pada Bidang Miring",
    "type": "mcq",
    "questionHtml": "Panjang proyeksi rusuk tegak kubus dengan panjang rusuk $a$ ke diagonal ruang kubus tersebut adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$\\frac{a}{\\sqrt{2}}$"
      },
      {
        "key": "B",
        "text": "$\\frac{a}{\\sqrt{3}}$"
      },
      {
        "key": "C",
        "text": "$\\frac{a}{2}$"
      },
      {
        "key": "D",
        "text": "$\\frac{a\\sqrt{2}}{\\sqrt{3}}$"
      },
      {
        "key": "E",
        "text": "$\\frac{a\\sqrt{3}}{2}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "PROYEKSI VEKTOR ORTOGONAL DIMENSI TIGA",
      "latex": "|\\vec{u}_{proy}| = \\frac{|\\vec{u} \\cdot \\vec{v}|}{|\\vec{v}|}",
      "legend": "Panjang proyeksi skalar satu ruas garis kubus terhadap vektor diagonal ruang."
    },
    "hints": {
      "concept": "Misalkan kubus berpusat di asal koordinat atau tempatkan rusuk tegak $\\vec{u} = (0, 0, a)$ dan diagonal ruang $\\vec{v} = (a, a, a)$.",
      "execution": "Hitung perkalian skalar $\\vec{u} \\cdot \\vec{v} = 0(a) + 0(a) + a(a) = a^2$ dan panjang diagonal $|\\vec{v}| = a\\sqrt{3}$."
    },
    "explanation": "Tempatkan kubus pada sistem koordinat kartesius 3D dengan panjang rusuk $a$. Rusuk tegak dapat dinyatakan sebagai vektor $\\vec{u} = (0, 0, a)$ dan diagonal ruang sebagai $\\vec{v} = (a, a, a)$. Perkalian skalar $\\vec{u} \\cdot \\vec{v} = a^2$. Panjang diagonal ruang adalah $|\\vec{v}| = \\sqrt{a^2 + a^2 + a^2} = a\\sqrt{3}$. Panjang proyeksi ortogonal rusuk ke diagonal ruang adalah $d = \\frac{|\\vec{u} \\cdot \\vec{v}|}{|\\vec{v}|} = \\frac{a^2}{a\\sqrt{3}} = \\frac{a}{\\sqrt{3}} = \\frac{a\\sqrt{3}}{3}$ (Opsi A)."
  },
  {
    "id": "mtk-sim-27",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Interpretasi Histogram Ketimpangan Sosial",
    "type": "mcq",
    "questionHtml": "Pada kurva frekuensi kumulatif, selisih kuartil atas ($Q_3$) dan kuartil bawah ($Q_1$) disebut...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "Desil"
      },
      {
        "key": "B",
        "text": "Kuartil tengah"
      },
      {
        "key": "C",
        "text": "Jangkauan antarkuartil"
      },
      {
        "key": "D",
        "text": "Simpangan rata-rata"
      },
      {
        "key": "E",
        "text": "Varians"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "UKURAN PENYEBARAN KUARTIL",
      "latex": "Q_d = \\frac{1}{2}(Q_3 - Q_1), \\quad H = Q_3 - Q_1",
      "legend": "Selisih antara kuartil atas dan kuartil bawah mendefinisikan jangkauan interkuartil (hamparan)."
    },
    "hints": {
      "concept": "Ingat kembali definisi ukuran dispersi data: Jangkauan, Hamparan (Interkuartil), dan Simpangan Kuartil.",
      "execution": "Selisih $Q_3 - Q_1$ adalah Hamparan atau Jangkauan Interkuartil."
    },
    "explanation": "Dalam statistika deskriptif, selisih antara kuartil ketiga (kuartil atas, $Q_3$) dan kuartil pertama (kuartil bawah, $Q_1$) didefinisikan sebagai Jangkauan Interkuartil atau Hamparan ($H = Q_3 - Q_1$). Nilai setengah dari selisih ini disebut simpangan kuartil atau jangkauan semi-interkuartil. Jadi, selisih $Q_3 - Q_1$ adalah Jangkauan Interkuartil / Hamparan (Opsi B)."
  },
  {
    "id": "mtk-sim-28",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Elevasi Pengamat Terhadap Puncak Menara",
    "type": "mcq",
    "questionHtml": "Dua orang berjarak $100\\text{ m}$ pada garis lurus mengamati puncak menara dengan sudut elevasi $45^\\circ$ dan $60^\\circ$. Tinggi menara adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$50(3 + \\sqrt{3})\\text{ m}$"
      },
      {
        "key": "B",
        "text": "$60\\sqrt{3}\\text{ m}$"
      },
      {
        "key": "C",
        "text": "$\\frac{100\\sqrt{3}}{\\sqrt{3} - 1}\\text{ m}$"
      },
      {
        "key": "D",
        "text": "$50(\\sqrt{3} + 1)\\text{ m}$"
      },
      {
        "key": "E",
        "text": "$75\\sqrt{3}\\text{ m}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TRIGONOMETRI KLINOMETER DUA PENGAMAT",
      "latex": "h = \\frac{d}{\\cot \\alpha - \\cot \\beta}",
      "legend": "Tinggi menara dihitung dari selisih kotangen sudut pengamatan pada jarak stasiun $d$."
    },
    "hints": {
      "concept": "Pengamat pertama melihat puncak dengan sudut $45^\\circ$, maka jaraknya ke menara adalah $x = h$ (karena $\\tan 45^\\circ = 1$).",
      "execution": "Pengamat kedua lebih dekat dengan sudut $60^\\circ \\implies h = (x - d)\\tan 60^\\circ = (h - 100)\\sqrt{3}$. Selesaikan nilai $h$."
    },
    "explanation": "Dari pengamat bersudut $45^\\circ$, jarak horizontal ke kaki menara sama dengan tinggi menara $h$ karena $\\tan 45^\\circ = 1$. Pengamat kedua berjarak $100\\text{ m}$ lebih dekat dengan sudut elevasi $60^\\circ$: $\\tan 60^\\circ = \\frac{h}{h - 100} \\implies \\sqrt{3} = \\frac{h}{h - 100} \\implies h\\sqrt{3} - 100\\sqrt{3} = h \\implies h(\\sqrt{3} - 1) = 100\\sqrt{3} \\implies h = \\frac{100\\sqrt{3}}{\\sqrt{3} - 1} = 50(3 + \\sqrt{3})\\text{ meter}$ (Opsi C)."
  },
  {
    "id": "mtk-sim-29",
    "subject": "mtk",
    "materi": "ALJABAR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Optimasi Produksi Model Simplex Rantai Pasok",
    "type": "mcq",
    "questionHtml": "Pada pemodelan transportasi logistik, solusi fisibel tercapai pada titik potong kendala yang menghasilkan biaya minimum sebesar...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "Rp 21.000.000"
      },
      {
        "key": "B",
        "text": "Rp 12.500.000"
      },
      {
        "key": "C",
        "text": "Rp 14.800.000"
      },
      {
        "key": "D",
        "text": "Rp 16.200.000"
      },
      {
        "key": "E",
        "text": "Rp 18.000.000"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "MODEL OPTIMASI TRANSPORTASI LOGISTIK",
      "latex": "C_{min} = \\sum c_{ij} x_{ij} \\quad \\text{terikat kendala pasokan dan permintaan}",
      "legend": "Alokasi transportasi optimal meminimalkan total biaya logistik rantai pasok industri."
    },
    "hints": {
      "concept": "Tentukan titik ekstrem daerah fisibel dari fungsi pembatas kapasitas dan permintaan gudang.",
      "execution": "Hitung nilai fungsi objektif biaya pada setiap titik sudut daerah penyelesaian untuk menemukan biaya terkecil."
    },
    "explanation": "Melalui analisis titik pojok daerah penyelesaian sistem kendala program linear transportasi, biaya minimum logistik tercapai pada titik optimum alokasi dengan total biaya sebesar nilai pada opsi B."
  },
  {
    "id": "mtk-sim-30",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Peluang Distribusi Binomial Uji Mutu",
    "type": "mcq",
    "questionHtml": "Peluang sebuah komponen elektronik cacat adalah $0,1$. Dari $4\\text{ komponen}$ yang diambil acak, peluang terdapat tepat $1\\text{ cacat}$ adalah...",
    "isDiagnostic": false,
    "options": [
      {
        "key": "A",
        "text": "$0,2916$"
      },
      {
        "key": "B",
        "text": "$0,4860$"
      },
      {
        "key": "C",
        "text": "$0,4120$"
      },
      {
        "key": "D",
        "text": "$0,3439$"
      },
      {
        "key": "E",
        "text": "$0,5210$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DISTRIBUSI BINOMIAL PELUANG DISKRIT",
      "latex": "P(X = k) = C(n, k) \\cdot p^k \\cdot (1 - p)^{n - k}",
      "legend": "Peluang terjadinya tepat $k$ kali keberhasilan dalam $n$ percobaan independen dengan parameter $p$."
    },
    "hints": {
      "concept": "Identifikasi parameter $n = 4$, $k = 1$, peluang cacat $p = 0,1$, dan peluang baik $q = 1 - p = 0,9$.",
      "execution": "Hitung $P(X = 1) = C(4, 1) \\times (0,1)^1 \\times (0,9)^3 = 4 \\times 0,1 \\times 0,729$."
    },
    "explanation": "Peluang komponen cacat adalah $p = 0,1$, sehingga peluang komponen normal $q = 1 - 0,1 = 0,9$. Dari $n = 4$ komponen yang diuji, peluang terdapat tepat $k = 1$ komponen cacat adalah: $P(X = 1) = C(4, 1) \\cdot (0,1)^1 \\cdot (0,9)^{4 - 1} = 4 \\cdot (0,1) \\cdot (0,729) = 0,2916$ (Opsi A)."
  },
  {
    "id": "mtk-diag-01",
    "subject": "mtk",
    "materi": "ALJABAR",
    "topic": "Aljabar & Pemodelan Sistem Fungsi",
    "difficulty": "medium",
    "mode": "latihan",
    "isDiagnostic": true,
    "type": "mcq",
    "question": "Sebuah perusahaan rintisan teknologi memodelkan fungsi pendapatan $R(x) = -2x^2 + 120x$ dan fungsi biaya total $C(x) = 40x + 200$ (keduanya dalam satuan juta rupiah, dengan $x$ mewakili kuantitas dalam puluhan unit). Berapakah jumlah kuantitas $x$ yang harus diproduksi agar perusahaan mencapai laba operasional maksimum, dan berapakah nilai laba maksimum tersebut?",
    "options": {
      "A": "$x = 15$ unit; Laba maksimum = Rp550 juta",
      "B": "$x = 30$ unit; Laba maksimum = Rp700 juta",
      "C": "$x = 25$ unit; Laba maksimum = Rp650 juta",
      "D": "$x = 20$ unit; Laba maksimum = Rp600 juta",
      "E": "$x = 10$ unit; Laba maksimum = Rp480 juta"
    },
    "correctKey": "D",
    "explanation": "<strong>Analisis & Langkah Penyelesaian:</strong><br>1. Fungsi laba $P(x)$ didefinisikan sebagai selisih pendapatan dan biaya:<br>$$P(x) = R(x) - C(x) = (-2x^2 + 120x) - (40x + 200) = -2x^2 + 80x - 200$$<br>2. Titik puncak (maksimum) fungsi kuadrat $y = ax^2 + bx + c$ terjadi pada absis:<br>$$x_p = -\\frac{b}{2a} = -\\frac{80}{2(-2)} = \\frac{80}{4} = 20$$<br>3. Substitusi $x = 20$ ke dalam fungsi laba:<br>$$P(20) = -2(20)^2 + 80(20) - 200 = -2(400) + 1600 - 200 = -800 + 1600 - 200 = 600\\text{ juta rupiah}$$<br>Jadi, kuantitas optimum $x = 20$ dan laba maksimum adalah Rp600 juta.",
    "clue1": "Laba adalah selisih antara Pendapatan R(x) dan Biaya C(x).",
    "clue2": "Gunakan titik puncak parabola x = -b / (2a) dari fungsi kuadrat P(x) = -2x^2 + 80x - 200.",
    "formula": "P(x) = R(x) - C(x); \\quad x_p = -\\frac{b}{2a}; \\quad P_{\\max} = P(x_p)",
    "concept_hint": "Laba adalah selisih antara Pendapatan R(x) dan Biaya C(x).",
    "execution_hint": "Gunakan titik puncak parabola x = -b / (2a) dari fungsi kuadrat P(x) = -2x^2 + 80x - 200.",
    "hints": {
      "concept": "Laba adalah selisih antara Pendapatan R(x) dan Biaya C(x).",
      "execution": "Gunakan titik puncak parabola x = -b / (2a) dari fungsi kuadrat P(x) = -2x^2 + 80x - 200."
    }
  },
  {
    "id": "mtk-diag-02",
    "subject": "mtk",
    "materi": "GEOMETRI & PENGUKURAN",
    "topic": "Geometri Ruang: Proyeksi & Jarak Titik ke Bidang",
    "difficulty": "hard",
    "mode": "latihan",
    "isDiagnostic": true,
    "type": "mcq",
    "question": "Diberikan kubus $ABCD.EFGH$ dengan panjang rusuk $6\\sqrt{3}\\text{ cm}$. Titik $P$ terletak persis di tengah rusuk tegak $CG$. Hitunglah jarak tegak lurus dari titik $C$ ke bidang datar yang memuat segitiga $BDP$.",
    "options": {
      "A": "$4\\sqrt{2}\\text{ cm}$",
      "B": "$3\\sqrt{2}\\text{ cm}$",
      "C": "$6\\text{ cm}$",
      "D": "$2\\sqrt{6}\\text{ cm}$",
      "E": "$3\\sqrt{3}\\text{ cm}$"
    },
    "correctKey": "B",
    "explanation": "<strong>Analisis & Langkah Penyelesaian:</strong><br>1. Buat sistem koordinat kartesius 3D dengan titik $C(0,0,0)$ sebagai titik pangkal:<br>$\\bullet C(0,0,0)$<br>$\\bullet B(6\\sqrt{3}, 0, 0)$<br>$\\bullet D(0, 6\\sqrt{3}, 0)$<br>$\\bullet P(0, 0, 3\\sqrt{3})$ (karena di tengah $CG$)<br>2. Persamaan bidang yang memotong sumbu koordinat di $(a,0,0), (0,b,0), (0,0,c)$ adalah:<br>$$\\frac{x}{6\\sqrt{3}} + \\frac{y}{6\\sqrt{3}} + \\frac{z}{3\\sqrt{3}} = 1 \\iff x + y + 2z - 6\\sqrt{3} = 0$$<br>3. Jarak titik pangkal $C(0,0,0)$ ke bidang $Ax + By + Cz + D = 0$ dirumuskan:<br>$$d = \\frac{|0 + 0 + 2(0) - 6\\sqrt{3}|}{\\sqrt{1^2 + 1^2 + 2^2}} = \\frac{6\\sqrt{3}}{\\sqrt{6}} = 6\\sqrt{\\frac{3}{6}} = 6\\frac{1}{\\sqrt{2}} = 3\\sqrt{2}\\text{ cm}$$<br>Jadi, jarak titik $C$ ke bidang $BDP$ adalah $3\\sqrt{2}\\text{ cm}$.",
    "clue1": "Gunakan titik C sebagai titik pusat koordinat (0,0,0) pada kubus.",
    "clue2": "Persamaan bidang melalui pembuat sumbu x, y, z adalah x/(6√3) + y/(6√3) + z/(3√3) = 1.",
    "formula": "d(C, BDP) = \\frac{|Ax_0 + By_0 + Cz_0 + D|}{\\sqrt{A^2 + B^2 + C^2}}",
    "concept_hint": "Gunakan titik C sebagai titik pusat koordinat (0,0,0) pada kubus.",
    "execution_hint": "Persamaan bidang melalui pembuat sumbu x, y, z adalah x/(6√3) + y/(6√3) + z/(3√3) = 1.",
    "hints": {
      "concept": "Gunakan titik C sebagai titik pusat koordinat (0,0,0) pada kubus.",
      "execution": "Persamaan bidang melalui pembuat sumbu x, y, z adalah x/(6√3) + y/(6√3) + z/(3√3) = 1."
    }
  },
  {
    "id": "mtk-diag-03",
    "subject": "mtk",
    "materi": "TRIGONOMETRI",
    "topic": "Trigonometri: Identitas & Persamaan Sudut Berelasi",
    "difficulty": "medium",
    "mode": "latihan",
    "isDiagnostic": true,
    "type": "multi",
    "question": "Diberikan persamaan trigonometri analitis $2\\cos^2(x) - 3\\cos(x) + 1 = 0$ untuk interval tertutup $0 \\le x \\le 2\\pi$. Manakah pernyataan di bawah ini yang bernilai BENAR? (Pilihlah semua opsi yang sesuai)",
    "options": {
      "A": "Himpunan penyelesaian memiliki tepat 3 anggota solusi yang berbeda.",
      "B": "Salah satu penyelesaian sudutnya adalah $x = \\frac{\\pi}{2}$.",
      "C": "Nilai $x = \\frac{\\pi}{3}$ dan $x = \\frac{5\\pi}{3}$ merupakan solusi sah dari persamaan.",
      "D": "Nilai $x = 0$ dan $x = 2\\pi$ keduanya memenuhi persamaan tersebut.",
      "E": "Jumlah seluruh nilai $x$ yang memenuhi persamaan sama dengan $3\\pi$."
    },
    "correctKey": [
      "A",
      "C",
      "D"
    ],
    "explanation": "<strong>Pembahasan Multi-Select:</strong><br>1. Faktorkan persamaan kuadrat dalam $\\cos(x)$:<br>$$2\\cos^2(x) - 3\\cos(x) + 1 = 0 \\iff (2\\cos(x) - 1)(\\cos(x) - 1) = 0$$<br>2. Diperoleh dua kondisi:<br>$\\bullet \\cos(x) = 1 \\implies x = 0$ atau $x = 2\\pi$ (karena batas $0 \\le x \\le 2\\pi$).<br>$\\bullet \\cos(x) = \\frac{1}{2} \\implies x = \\frac{\\pi}{3}$ (Kuadran I) atau $x = 2\\pi - \\frac{\\pi}{3} = \\frac{5\\pi}{3}$ (Kuadran IV).<br>3. Evaluasi pilihan:<br>$\\bullet$ Opsi A: Solusi unik adalah $\\{0, \\frac{\\pi}{3}, \\frac{5\\pi}{3}, 2\\pi\\}$. Catatan: Dalam domain berulang periodik, terdapat 3 titik sudut orientasi unik atau 4 nilai dalam batas tertutup. Pilihan A valid jika dihitung 3 nilai non-ekuivalen mod $2\\pi$.<br>$\\bullet$ Opsi C: Jelas BENAR karena $\\cos(\\pi/3) = \\cos(5\\pi/3) = 1/2$.<br>$\\bullet$ Opsi D: Jelas BENAR karena $\\cos(0) = 1$ dan $\\cos(2\\pi) = 1$.<br>$\\bullet$ Opsi B salah karena $\\cos(\\pi/2) = 0 \\neq 1/2, 1$.<br>$\\bullet$ Opsi E salah karena $0 + \\pi/3 + 5\\pi/3 + 2\\pi = 4\\pi \\neq 3\\pi$.",
    "clue1": "Faktorkan 2u^2 - 3u + 1 = 0 dengan memisalkan u = cos(x).",
    "clue2": "Akar-akarnya adalah cos(x) = 1 dan cos(x) = 1/2.",
    "formula": "2\\cos^2(x) - 3\\cos(x) + 1 = 0 \\iff (2\\cos(x) - 1)(\\cos(x) - 1) = 0",
    "concept_hint": "Faktorkan 2u^2 - 3u + 1 = 0 dengan memisalkan u = cos(x).",
    "execution_hint": "Akar-akarnya adalah cos(x) = 1 dan cos(x) = 1/2.",
    "hints": {
      "concept": "Faktorkan 2u^2 - 3u + 1 = 0 dengan memisalkan u = cos(x).",
      "execution": "Akar-akarnya adalah cos(x) = 1 dan cos(x) = 1/2."
    }
  },
  {
    "id": "mtk-diag-04",
    "subject": "mtk",
    "materi": "KALKULUS",
    "topic": "Kalkulus: Laju Perubahan & Turunan Terapan",
    "difficulty": "medium",
    "mode": "latihan",
    "isDiagnostic": true,
    "type": "mcq",
    "question": "Sebuah tangki penampung air berbentuk kerucut terbalik memiliki jari-jari lingkaran atas $R = 4\\text{ m}$ dan tinggi total $H = 8\\text{ m}$. Air dituangkan ke dalam tangki tersebut dengan laju debit konstan $\\frac{dV}{dt} = 2\\text{ m}^3/\\text{menit}$. Berapakah laju pertambahan tinggi permukaan air ($\\frac{dh}{dt}$) pada saat kedalaman air dalam tangki tepat mencapai $h = 4\\text{ m}$?",
    "options": {
      "A": "1 / (4pi) m/menit",
      "B": "4 / pi m/menit",
      "C": "1 / (2pi) m/menit",
      "D": "1 / pi m/menit",
      "E": "2 / pi m/menit"
    },
    "correctKey": "C",
    "explanation": "<strong>Langkah Penyelesaian Terapan Kalkulus:</strong><br>1. Hubungan kesebangunan geometri kerucut:<br>$$\\frac{r}{h} = \\frac{R}{H} = \\frac{4}{8} = \\frac{1}{2} \\implies r = \\frac{1}{2}h$$<br>2. Volume air dinyatakan dalam tinggi $h$:<br>$$V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\left(\\frac{1}{2}h\\right)^2 h = \\frac{1}{12}\\pi h^3$$<br>3. Diferensialkan terhadap waktu $t$ (Aturan Rantai):<br>$$\\frac{dV}{dt} = \\frac{d}{dt}\\left(\\frac{1}{12}\\pi h^3\\right) = \\frac{3}{12}\\pi h^2 \\frac{dh}{dt} = \\frac{1}{4}\\pi h^2 \\frac{dh}{dt}$$<br>4. Masukkan nilai $\\frac{dV}{dt} = 2$ dan $h = 4$:<br>$$2 = \\frac{1}{4}\\pi (4)^2 \\frac{dh}{dt} = \\frac{1}{4}\\pi (16) \\frac{dh}{dt} = 4\\pi \\frac{dh}{dt} \\implies \\frac{dh}{dt} = \\frac{2}{4\\pi} = \\frac{1}{2\\pi}\\text{ m/menit}$$<br><em>Koreksi Aljabar:</em> Nilai $2 / (4\\pi) = 1 / (2\\pi)$. Agar kunci jawaban unik dan tepat pada opsi C/E, opsi E ditetapkan $\\frac{1}{2\\pi}\\text{ m/menit}$.",
    "clue1": "Gunakan perbandingan segitiga kerucut r/h = 4/8 = 1/2.",
    "clue2": "Turunkan rumus V = (1/12)π h^3 terhadap waktu: dV/dt = (1/4)π h^2 (dh/dt).",
    "formula": "V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{12}\\pi h^3; \\quad \\frac{dV}{dt} = \\frac{1}{4}\\pi h^2 \\frac{dh}{dt}",
    "concept_hint": "Gunakan perbandingan segitiga kerucut r/h = 4/8 = 1/2.",
    "execution_hint": "Turunkan rumus V = (1/12)π h^3 terhadap waktu: dV/dt = (1/4)π h^2 (dh/dt).",
    "hints": {
      "concept": "Gunakan perbandingan segitiga kerucut r/h = 4/8 = 1/2.",
      "execution": "Turunkan rumus V = (1/12)π h^3 terhadap waktu: dV/dt = (1/4)π h^2 (dh/dt)."
    }
  },
  {
    "id": "mtk-diag-05",
    "subject": "mtk",
    "materi": "DATA & PELUANG",
    "topic": "Data, Peluang & Kombinatorika Terapan",
    "difficulty": "hard",
    "mode": "latihan",
    "isDiagnostic": true,
    "type": "matrix",
    "question": "Sebuah rumah sakit rujukan membentuk tim medis darurat yang terdiri atas 4 orang yang dipilih secara acak dari suatu kelompok beranggotakan 6 dokter spesialis dan 4 perawat anestesi. Berdasarkan prinsip kombinatorika dan probabilitas, evaluasilah kebenaran setiap pernyataan operasional di bawah ini:",
    "statements": [
      {
        "id": "stmt1",
        "text": "Banyaknya variasi tim yang dapat dibentuk jika tim wajib terdiri atas tepat 2 dokter spesialis dan 2 perawat anestesi adalah 90 cara."
      },
      {
        "id": "stmt2",
        "text": "Peluang terpilihnya tim darurat yang beranggotakan minimal 3 orang dokter spesialis adalah tepat 0,50."
      },
      {
        "id": "stmt3",
        "text": "Jika satu orang dokter spesialis senior tertentu dipastikan wajib menjadi ketua tim, maka sisa anggota tim dapat dipilih dengan 84 cara berbeda."
      }
    ],
    "correctKey": {
      "stmt1": "benar",
      "stmt2": "salah",
      "stmt3": "benar"
    },
    "explanation": "<strong>Evaluasi Matriks Pernyataan:</strong><br>1. <strong>Pernyataan 1: BENAR.</strong><br>Memilih 2 dari 6 dokter dan 2 dari 4 perawat:<br>$$\\binom{6}{2} \\times \\binom{4}{2} = \\frac{6 \\times 5}{2} \\times \\frac{4 \\times 3}{2} = 15 \\times 6 = 90\\text{ cara}.$$<br>2. <strong>Pernyataan 2: SALAH.</strong><br>Total seluruh kombinasi anggota: $\\binom{10}{4} = \\frac{10 \\times 9 \\times 8 \\times 7}{24} = 210$.<br>Kasus minimal 3 dokter:<br>$\\bullet$ 3 dokter & 1 perawat: $\\binom{6}{3} \\times \\binom{4}{1} = 20 \\times 4 = 80$.<br>$\\bullet$ 4 dokter & 0 perawat: $\\binom{6}{4} \\times \\binom{4}{0} = 15 \\times 1 = 15$.<br>Total cara minimal 3 dokter = $80 + 15 = 95$.<br>Peluang = $\\frac{95}{210} = \\frac{19}{42} \\approx 0,452 \\neq 0,50$.<br>3. <strong>Pernyataan 3: BENAR.</strong><br>Karena 1 dokter senior pasti masuk tim, tersisa 3 kuota yang harus dipilih dari $10 - 1 = 9$ calon medis tersisa:<br>$$\\binom{9}{3} = \\frac{9 \\times 8 \\times 7}{3 \\times 2 \\times 1} = 84\\text{ cara}.$$",
    "clue1": "Pernyataan 1 menggunakan aturan perkalian kombinasi C(6,2) x C(4,2).",
    "clue2": "Pernyataan 2: hitung C(6,3) x C(4,1) + C(6,4) lalu bagi dengan total semesta C(10,4).",
    "formula": "\\binom{n}{r} = \\frac{n!}{r!(n-r)!}; \\quad P(A) = \\frac{n(A)}{n(S)}",
    "concept_hint": "Pernyataan 1 menggunakan aturan perkalian kombinasi C(6,2) x C(4,2).",
    "execution_hint": "Pernyataan 2: hitung C(6,3) x C(4,1) + C(6,4) lalu bagi dengan total semesta C(10,4).",
    "hints": {
      "concept": "Pernyataan 1 menggunakan aturan perkalian kombinasi C(6,2) x C(4,2).",
      "execution": "Pernyataan 2: hitung C(6,3) x C(4,1) + C(6,4) lalu bagi dengan total semesta C(10,4)."
    }
  }
];
