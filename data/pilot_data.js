/**
 * TKA MASTERY HUB — SEED PILOT DATA (SPRINT 1)
 * Mencakup:
 * - 20 Soal Matematika Wajib (Variasi Easy, Medium, Hard + Full KaTeX + 2-Stage Clues)
 * - Sample Pilot Bahasa Indonesia & Bahasa Inggris agar seluruh Tab Navigasi hidup 100%.
 * Seluruh kalkulasi matematis telah diverifikasi secara analitis & bebas draf internal.
 */

window.TKA_PILOT_DATA = [
  // =========================================================================
  // MATEMATIKA WAJIB — EASY (7 SOAL)
  // =========================================================================
  {
    id: "mtk-lat-e-01",
    subject: "mtk",
    mode: "latihan",
    difficulty: "easy",
    topic: "Fungsi Komposisi & Invers",
    questionHtml: "Sebuah toko buku daring menerapkan fungsi potongan harga member $f(x) = x - 15.000$ untuk setiap pembelian di atas Rp100.000, di mana $x$ adalah harga awal buku. Setelah dipotong, platform mengenakan pajak layanan sehingga total bayar dimodelkan oleh $g(y) = 1,05y + 3.000$. Jika seorang siswa membayar total $\\text{Rp}171.000$, berapakah harga awal buku tersebut sebelum diskon?",
    options: [
      { key: "A", text: "Rp 160.000" },
      { key: "B", text: "Rp 165.000" },
      { key: "C", text: "Rp 175.000" },
      { key: "D", text: "Rp 180.000" },
      { key: "E", text: "Rp 185.000" }
    ],
    correctKey: "C",
    formulaHud: "(g \\circ f)(x) = g(f(x)) \\iff y = \\frac{g(y) - c}{m}",
    hints: {
      concept: "Gunakan prinsip invers dari belakang: cari terlebih dahulu nilai $y$ (harga setelah diskon) dari persamaan $g(y) = 171.000$.",
      execution: "$1,05y + 3.000 = 171.000 \\implies 1,05y = 168.000 \\implies y = 160.000$."
    },
    explanation: "Langkah 1: Cari harga setelah diskon ($y$) dari $1,05y + 3.000 = 171.000$, diperoleh $1,05y = 168.000 \\implies y = 160.000$. Langkah 2: Substitusi ke fungsi diskon $f(x) = x - 15.000 = 160.000 \\implies x = 175.000$. Jawaban: C."
  },
  {
    id: "mtk-lat-e-02",
    subject: "mtk",
    mode: "latihan",
    difficulty: "easy",
    topic: "Eksponen & Logaritma",
    questionHtml: "Jika diketahui $3^{2x - 1} = 27^{x - 2}$, maka nilai dari $x^2 - 2x$ adalah...",
    options: [
      { key: "A", text: "8" },
      { key: "B", text: "15" },
      { key: "C", text: "24" },
      { key: "D", text: "35" },
      { key: "E", text: "48" }
    ],
    correctKey: "B",
    formulaHud: "a^{f(x)} = a^{g(x)} \\implies f(x) = g(x), \\quad 27 = 3^3",
    hints: {
      concept: "Samakan basis eksponen di kedua ruas menjadi basis $3$, lalu samakan pangkatnya.",
      execution: "$3^{2x - 1} = (3^3)^{x - 2} = 3^{3x - 6} \\implies 2x - 1 = 3x - 6$."
    },
    explanation: "Samakan pangkat: $2x - 1 = 3x - 6 \\implies x = 5$. Maka nilai $x^2 - 2x = 5^2 - 2(5) = 25 - 10 = 15$. Jawaban: B."
  },
  {
    id: "mtk-lat-e-03",
    subject: "mtk",
    mode: "latihan",
    difficulty: "easy",
    topic: "Barisan & Deret Aritmetika",
    questionHtml: "Seorang teknisi jaringan memasang kabel serat optik. Pada hari pertama ia menarik $18\\text{ meter}$ kabel, hari kedua $25\\text{ meter}$, hari ketiga $32\\text{ meter}$, dan seterusnya bertambah secara tetap setiap hari. Berapakah panjang kabel yang dipasang tepat pada hari ke-12?",
    options: [
      { key: "A", text: "88 meter" },
      { key: "B", text: "92 meter" },
      { key: "C", text: "95 meter" },
      { key: "D", text: "102 meter" },
      { key: "E", text: "105 meter" }
    ],
    correctKey: "C",
    formulaHud: "U_n = a + (n - 1)b",
    hints: {
      concept: "Identifikasi suku pertama ($a$) dan selisih tetap/beda ($b$) dari barisan aritmetika.",
      execution: "Diketahui $a = 18$ dan $b = 25 - 18 = 7$. Substitusikan $n = 12$ ke rumus $U_{12}$."
    },
    explanation: "$U_{12} = 18 + (12 - 1) \\times 7 = 18 + 11 \\times 7 = 18 + 77 = 95\\text{ meter}$. Jawaban: C."
  },
  {
    id: "mtk-lat-e-04",
    subject: "mtk",
    mode: "latihan",
    difficulty: "easy",
    topic: "Sistem Persamaan Linear",
    questionHtml: "Harga $2\\text{ lisensi}$ server tipe A dan $3\\text{ lisensi}$ tipe B adalah $\\text{Rp}1.350.000$. Sedangkan harga $3\\text{ lisensi}$ tipe A dan $1\\text{ lisensi}$ tipe B adalah $\\text{Rp}975.000$. Berapakah harga $1\\text{ lisensi}$ tipe A dan $2\\text{ lisensi}$ tipe B?",
    options: [
      { key: "A", text: "Rp 750.000" },
      { key: "B", text: "Rp 825.000" },
      { key: "C", text: "Rp 850.000" },
      { key: "D", text: "Rp 900.000" },
      { key: "E", text: "Rp 925.000" }
    ],
    correctKey: "B",
    formulaHud: "\\begin{cases} 2A + 3B = 1.350.000 \\\\ 3A + B = 975.000 \\end{cases}",
    hints: {
      concept: "Gunakan metode eliminasi dengan mengalikan persamaan kedua dengan 3 untuk mengeliminasi variabel $B$.",
      execution: "$(9A + 3B) - (2A + 3B) = 2.925.000 - 1.350.000 \\implies 7A = 1.575.000$."
    },
    explanation: "Dari $7A = 1.575.000$ diperoleh $A = 225.000$. Substitusi ke $3(225.000) + B = 975.000 \\implies B = 300.000$. Maka $A + 2B = 225.000 + 600.000 = \\text{Rp}825.000$. Jawaban: B."
  },
  {
    id: "mtk-lat-e-05",
    subject: "mtk",
    mode: "latihan",
    difficulty: "easy",
    topic: "Statistika Deskriptif",
    questionHtml: "Rata-rata nilai ujian matematika dari $8\\text{ siswa}$ adalah $76$. Ketika nilai dari $2\\text{ siswa}$ susulan digabungkan, rata-rata keseluruhannya naik menjadi $78,5$. Berapakah rata-rata nilai dari kedua siswa susulan tersebut?",
    options: [
      { key: "A", text: "84,0" },
      { key: "B", text: "86,5" },
      { key: "C", text: "88,5" },
      { key: "D", text: "90,0" },
      { key: "E", text: "91,5" }
    ],
    correctKey: "C",
    formulaHud: "\\bar{x}_{\\text{gab}} = \\frac{n_1 \\bar{x}_1 + n_2 \\bar{x}_2}{n_1 + n_2}",
    hints: {
      concept: "Hitung selisih antara total nilai 10 siswa dengan total nilai 8 siswa mula-mula.",
      execution: "Total 8 siswa $= 8 \\times 76 = 608$. Total 10 siswa $= 10 \\times 78,5 = 785$."
    },
    explanation: "Jumlah nilai 2 siswa susulan $= 785 - 608 = 177$. Rata-rata kedua siswa tersebut $= \\frac{177}{2} = 88,5$. Jawaban: C."
  },
  {
    id: "mtk-lat-e-06",
    subject: "mtk",
    mode: "latihan",
    difficulty: "easy",
    topic: "Limit Fungsi Aljabar",
    questionHtml: "Nilai dari $\\lim_{x \\to 4} \\frac{x^2 - 2x - 8}{x - 4}$ adalah...",
    options: [
      { key: "A", text: "2" },
      { key: "B", text: "4" },
      { key: "C", text: "6" },
      { key: "D", text: "8" },
      { key: "E", text: "10" }
    ],
    correctKey: "C",
    formulaHud: "\\lim_{x \\to a} \\frac{(x - a)(x - b)}{x - a} = a - b",
    hints: {
      concept: "Substitusi langsung menghasilkan bentuk tak tentu $\\frac{0}{0}$. Faktorkan pembilang kuadratnya.",
      execution: "$x^2 - 2x - 8 = (x - 4)(x + 2)$. Coret faktor $(x - 4)$."
    },
    explanation: "$\\lim_{x \\to 4} \\frac{(x - 4)(x + 2)}{x - 4} = \\lim_{x \\to 4} (x + 2) = 4 + 2 = 6$. Jawaban: C."
  },
  {
    id: "mtk-lat-e-07",
    subject: "mtk",
    mode: "latihan",
    difficulty: "easy",
    topic: "Matriks & Determinan",
    questionHtml: "Diketahui matriks $A = \\begin{pmatrix} 2x & 3 \\\\ 4 & x+1 \\end{pmatrix}$. Jika matriks $A$ merupakan matriks singular (tidak memiliki invers) untuk $x > 0$, maka nilai $x$ adalah...",
    options: [
      { key: "A", text: "1" },
      { key: "B", text: "2" },
      { key: "C", text: "3" },
      { key: "D", text: "4" },
      { key: "E", text: "6" }
    ],
    correctKey: "B",
    formulaHud: "\\det(A) = ad - bc = 0",
    hints: {
      concept: "Matriks singular memiliki determinan sama dengan nol ($ad - bc = 0$).",
      execution: "$2x(x + 1) - 3(4) = 0 \\implies 2x^2 + 2x - 12 = 0 \\implies x^2 + x - 6 = 0$."
    },
    explanation: "Faktorkan persamaan kuadrat: $(x + 3)(x - 2) = 0$. Karena syarat $x > 0$, maka dipilih $x = 2$. Jawaban: B."
  },

  // =========================================================================
  // MATEMATIKA WAJIB — MEDIUM (7 SOAL)
  // =========================================================================
  {
    id: "mtk-lat-m-08",
    subject: "mtk",
    mode: "latihan",
    difficulty: "medium",
    topic: "Persamaan & Fungsi Kuadrat",
    questionHtml: "Kurva parabola $y = x^2 - (2k - 1)x + k^2 - 3$ menyinggung sumbu-$X$ di satu titik untuk $k > 0$. Tentukan koordinat titik puncak parabola tersebut!",
    options: [
      { key: "A", text: "(11/4, 0)" },
      { key: "B", text: "(13/4, 0)" },
      { key: "C", text: "(7/2, 0)" },
      { key: "D", text: "(9/2, 0)" },
      { key: "E", text: "(15/4, 0)" }
    ],
    correctKey: "A",
    formulaHud: "D = b^2 - 4ac = 0, \\quad x_p = -\\frac{b}{2a}",
    hints: {
      concept: "Syarat kurva menyinggung sumbu-$X$ adalah diskriminan $D = 0$, dan ordinat puncak pasti $y_p = 0$.",
      execution: "$D = [-(2k - 1)]^2 - 4(1)(k^2 - 3) = 0 \\implies (4k^2 - 4k + 1) - 4k^2 + 12 = 0$."
    },
    explanation: "Syarat menyinggung sumbu-$X$ adalah $D = 0$. Maka: $[-(2k - 1)]^2 - 4(1)(k^2 - 3) = 0 \\implies (4k^2 - 4k + 1) - 4k^2 + 12 = 0 \\implies 13 - 4k = 0 \\implies k = \\frac{13}{4}$. Absis titik puncak adalah $x_p = -\\frac{b}{2a} = \\frac{2k - 1}{2} = \\frac{2(13/4) - 1}{2} = \\frac{13/2 - 1}{2} = \\frac{11}{4}$, dan ordinat $y_p = 0$. Titik puncak adalah $(11/4, 0)$. Jawaban: A."
  },
  {
    id: "mtk-lat-m-09",
    subject: "mtk",
    mode: "latihan",
    difficulty: "medium",
    topic: "Deret Geometri Tak Hingga",
    questionHtml: "Sebuah bola elastis dijatuhkan secara vertikal dari ketinggian $16\\text{ meter}$. Setiap kali memantul di lantai, bola mencapai ketinggian $\\frac{3}{4}$ dari ketinggian sebelumnya. Berapakah total panjang lintasan seluruhnya yang ditempuh bola sampai berhenti?",
    options: [
      { key: "A", text: "64 meter" },
      { key: "B", text: "96 meter" },
      { key: "C", text: "112 meter" },
      { key: "D", text: "120 meter" },
      { key: "E", text: "128 meter" }
    ],
    correctKey: "C",
    formulaHud: "L_{\\text{total}} = h_0 \\left( \\frac{q + p}{q - p} \\right) \\text{ untuk } r = \\frac{p}{q}",
    hints: {
      concept: "Lintasan turun pertama hanya terjadi sekali ($h_0$), sedangkan pantulan naik dan turun berikutnya terjadi dua kali lipat deret geometri tak hingga.",
      execution: "$h_0 = 16$, rasio $r = \\frac{3}{4}$. Gunakan rumus cepat $L = 16 \\times \\frac{4 + 3}{4 - 3}$."
    },
    explanation: "$L_{\\text{total}} = 2 S_\\infty - h_0 = 2 \\left( \\frac{16}{1 - 3/4} \\right) - 16 = 2(64) - 16 = 128 - 16 = 112\\text{ meter}$. Jawaban: C."
  },
  {
    id: "mtk-lat-m-10",
    subject: "mtk",
    mode: "latihan",
    difficulty: "medium",
    topic: "Turunan Fungsi & Optimasi",
    questionHtml: "Biaya operasional harian sebuah mesin CNC untuk memproduksi $x$ unit komponen dirumuskan dengan $B(x) = \\left(2x^2 - 80x + 1.500\\right)$ ribu rupiah. Agar biaya operasional total minimum, berapa unit komponen yang harus diproduksi per hari dan berapakah biaya minimum tersebut?",
    options: [
      { key: "A", text: "20 unit dan Rp 700.000" },
      { key: "B", text: "20 unit dan Rp 800.000" },
      { key: "C", text: "40 unit dan Rp 650.000" },
      { key: "D", text: "40 unit dan Rp 700.000" },
      { key: "E", text: "25 unit dan Rp 750.000" }
    ],
    correctKey: "A",
    formulaHud: "B'(x) = 0 \\implies 4x - 80 = 0",
    hints: {
      concept: "Nilai stasioner (minimum) dicapai saat turunan pertama fungsi biaya sama dengan nol ($B'(x) = 0$).",
      execution: "$B'(x) = 4x - 80 = 0 \\implies x = 20\\text{ unit}$. Substitusikan $x = 20$ ke $B(x)$."
    },
    explanation: "Saat $x = 20$, nilai $B(20) = 2(20)^2 - 80(20) + 1.500 = 800 - 1.600 + 1.500 = 700\\text{ ribu rupiah}$ ($\\text{Rp}700.000$). Jawaban: A."
  },
  {
    id: "mtk-lat-m-11",
    subject: "mtk",
    mode: "latihan",
    difficulty: "medium",
    topic: "Trigonometri Terapan",
    questionHtml: "Seorang pengamat melihat puncak menara pemancar dengan sudut elevasi $30^\\circ$. Setelah ia berjalan maju mendekati menara sejauh $40\\text{ meter}$ pada tanah mendatar, sudut elevasinya berubah menjadi $60^\\circ$. Jika tinggi mata pengamat dari tanah adalah $1,6\\text{ meter}$, berapakah tinggi total menara tersebut?",
    options: [
      { key: "A", text: "(20√3 + 1,6) meter" },
      { key: "B", text: "(30√3 + 1,6) meter" },
      { key: "C", text: "(40√3 + 1,6) meter" },
      { key: "D", text: "(20 + 1,6) meter" },
      { key: "E", text: "(40 + 1,6) meter" }
    ],
    correctKey: "A",
    formulaHud: "\\tan \\theta = \\frac{h}{x}, \\quad h = \\frac{d}{\\cot 30^\\circ - \\cot 60^\\circ}",
    hints: {
      concept: "Misalkan jarak akhir ke menara adalah $x$ dan tinggi menara di atas mata pengamat adalah $h$. Gunakan perbandingan $\\tan 60^\\circ$ dan $\\tan 30^\\circ$.",
      execution: "$h = x\\sqrt{3}$ dan $\\tan 30^\\circ = \\frac{h}{x + 40} = \\frac{1}{\\sqrt{3}} \\implies x + 40 = h\\sqrt{3} = 3x$."
    },
    explanation: "Dari $3x = x + 40 \\implies 2x = 40 \\implies x = 20\\text{ m}$. Maka $h = 20\\sqrt{3}\\text{ m}$. Tinggi menara dari tanah adalah $H = (20\\sqrt{3} + 1,6)\\text{ meter}$. Jawaban: A."
  },
  {
    id: "mtk-lat-m-12",
    subject: "mtk",
    mode: "latihan",
    difficulty: "medium",
    topic: "Kaidah Pencacahan & Peluang",
    questionHtml: "Dari sebuah tim riset yang terdiri atas $6\\text{ programmer backend}$ dan $4\\text{ desainer UI/UX}$, akan dipilih $3\\text{ orang}$ untuk mewakili presentasi produk. Berapakah peluang terpilihnya tim yang memuat paling sedikit $2\\text{ programmer backend}$?",
    options: [
      { key: "A", text: "1/2" },
      { key: "B", text: "2/3" },
      { key: "C", text: "3/4" },
      { key: "D", text: "5/6" },
      { key: "E", text: "7/12" }
    ],
    correctKey: "B",
    formulaHud: "C(n, r) = \\frac{n!}{r!(n-r)!}, \\quad P(A) = \\frac{n(A)}{n(S)}",
    hints: {
      concept: "Kejadian 'paling sedikit 2 backend' terdiri dari dua kasus saling lepas: (2 Backend & 1 UI/UX) ATAU (3 Backend & 0 UI/UX).",
      execution: "Ruang sampel $n(S) = C(10, 3) = \\frac{10 \\times 9 \\times 8}{6} = 120$."
    },
    explanation: "Kasus 1 (2B, 1U): $C(6,2) \\times C(4,1) = 15 \\times 4 = 60$. Kasus 2 (3B, 0U): $C(6,3) \\times C(4,0) = 20 \\times 1 = 20$. Total $n(A) = 60 + 20 = 80$. Peluang $= \\frac{80}{120} = \\frac{2}{3}$. Jawaban: B."
  },
  {
    id: "mtk-lat-m-13",
    subject: "mtk",
    mode: "latihan",
    difficulty: "medium",
    topic: "Integral Tentu",
    questionHtml: "Diketahui nilai $\\int_{1}^{3} (3x^2 - 2kx + 4)\\,dx = 22$. Maka nilai dari $4k$ adalah...",
    options: [
      { key: "A", text: "6" },
      { key: "B", text: "8" },
      { key: "C", text: "12" },
      { key: "D", text: "16" },
      { key: "E", text: "20" }
    ],
    correctKey: "A",
    formulaHud: "\\int_{a}^{b} f(x)\\,dx = [F(x)]_{a}^{b} = F(b) - F(a)",
    hints: {
      concept: "Integralkan masing-masing suku terhadap $x$, lalu substitusikan batas atas $x = 3$ dikurangi batas bawah $x = 1$.",
      execution: "$[x^3 - kx^2 + 4x]_1^3 = (27 - 9k + 12) - (1 - k + 4) = 22$."
    },
    explanation: "$(39 - 9k) - (5 - k) = 22 \\implies 34 - 8k = 22 \\implies 8k = 12 \\implies 4k = 6$. Jawaban: A."
  },
  {
    id: "mtk-lat-m-14",
    subject: "mtk",
    mode: "latihan",
    difficulty: "medium",
    topic: "Program Linear",
    questionHtml: "Seorang pedagang meracik dua jenis paket parfum non-alkohol: Paket Reguler membutuhkan $10\\text{ ml}$ bibit A dan $20\\text{ ml}$ bibit B, sedangkan Paket Eksklusif membutuhkan $30\\text{ ml}$ bibit A dan $10\\text{ ml}$ bibit B. Stok tersedia adalah $300\\text{ ml}$ bibit A dan $200\\text{ ml}$ bibit B. Jika laba Paket Reguler $\\text{Rp}40.000$ dan Paket Eksklusif $\\text{Rp}75.000$, berapakah laba maksimum yang dapat diperoleh?",
    options: [
      { key: "A", text: "Rp 600.000" },
      { key: "B", text: "Rp 680.000" },
      { key: "C", text: "Rp 750.000" },
      { key: "D", text: "Rp 790.000" },
      { key: "E", text: "Rp 840.000" }
    ],
    correctKey: "E",
    formulaHud: "\\begin{cases} x + 3y \\le 30 \\\\ 2x + y \\le 20 \\\\ x, y \\ge 0 \\end{cases} \\quad Z = 40.000x + 75.000y",
    hints: {
      concept: "Sederhanakan sistem pertidaksamaan kendala, lalu cari titik potong kedua garis batas untuk diuji ke fungsi objektif $Z$.",
      execution: "Eliminasi $x + 3y = 30$ dan $2x + y = 20 \\implies 5y = 40 \\implies y = 8$ dan $x = 6$."
    },
    explanation: "Model matematika: $x + 3y \\le 30$ dan $2x + y \\le 20$ dengan $x, y \\ge 0$. Titik potong kedua garis kendala: kalikan persamaan pertama dengan 2: $2x + 6y = 60$. Kurangkan dengan $2x + y = 20 \\implies 5y = 40 \\implies y = 8$, sehingga $x = 6$. Uji seluruh titik pojok daerah penyelesaian ke $Z(x,y) = 40.000x + 75.000y$: (1) Titik $(10, 0) \\implies \\text{Rp}400.000$; (2) Titik $(0, 10) \\implies \\text{Rp}750.000$; (3) Titik $(6, 8) \\implies 40.000(6) + 75.000(8) = 240.000 + 600.000 = \\text{Rp}840.000$. Maka laba maksimumnya adalah $\\text{Rp}840.000$. Jawaban: E."
  },

  // =========================================================================
  // MATEMATIKA WAJIB — HARD (6 SOAL)
  // =========================================================================
  {
    id: "mtk-lat-h-15",
    subject: "mtk",
    mode: "latihan",
    difficulty: "hard",
    topic: "Dimensi Tiga (Geometri Ruang)",
    questionHtml: "Diketahui kubus $ABCD.EFGH$ dengan panjang rusuk $12\\text{ cm}$. Titik $P$ terletak tepat di tengah rusuk $CG$. Berapakah jarak dari titik $E$ ke garis $BP$?",
    options: [
      { key: "A", text: "6√5 cm" },
      { key: "B", text: "36/5 √5 cm" },
      { key: "C", text: "8√3 cm" },
      { key: "D", text: "42/5 √5 cm" },
      { key: "E", text: "9√2 cm" }
    ],
    correctKey: "B",
    formulaHud: "d(E, BP) = EB \\sin B, \\quad \\cos B = \\frac{EB^2 + BP^2 - EP^2}{2 \\cdot EB \\cdot BP}",
    hints: {
      concept: "Bentuk segitiga $EBP$ dengan menghitung panjang ketiga sisinya menggunakan Teorema Pythagoras pada kubus.",
      execution: "$BP = \\sqrt{12^2 + 6^2} = 6\\sqrt{5}\\text{ cm}$, $EB = 12\\sqrt{2}\\text{ cm}$, dan $EP = \\sqrt{EG^2 + GP^2} = \\sqrt{(12\\sqrt{2})^2 + 6^2} = 18\\text{ cm}$."
    },
    explanation: "Pada $\\triangle EBP$: $EB = 12\\sqrt{2}\\text{ cm}$, $BP = 6\\sqrt{5}\\text{ cm}$, dan $EP = 18\\text{ cm}$. Dengan aturan cosinus pada sudut $B$: $\\cos B = \\frac{EB^2 + BP^2 - EP^2}{2 \\cdot EB \\cdot BP} = \\frac{288 + 180 - 324}{2 \\cdot 12\\sqrt{2} \\cdot 6\\sqrt{5}} = \\frac{144}{144\\sqrt{10}} = \\frac{1}{\\sqrt{10}}$. Maka $\\sin B = \\sqrt{1 - \\frac{1}{10}} = \\frac{3}{\\sqrt{10}}$. Jarak titik $E$ ke garis $BP$ adalah $EB \\cdot \\sin B = 12\\sqrt{2} \\cdot \\frac{3}{\\sqrt{10}} = \\frac{36}{\\sqrt{5}} = \\frac{36}{5}\\sqrt{5}\\text{ cm}$. Jawaban: B."
  },
  {
    id: "mtk-lat-h-16",
    subject: "mtk",
    mode: "latihan",
    difficulty: "hard",
    topic: "Aplikasi Turunan & Geometri Minimum",
    questionHtml: "Sebuah kemasan tabung tertutup akan dibuat dari lembaran aluminium dengan volume tetap sebesar $128\\pi\\text{ cm}^3$. Agar luas permukaan aluminium yang digunakan seminimum mungkin, berapakah tinggi tabung tersebut?",
    options: [
      { key: "A", text: "4 cm" },
      { key: "B", text: "6 cm" },
      { key: "C", text: "8 cm" },
      { key: "D", text: "10 cm" },
      { key: "E", text: "12 cm" }
    ],
    correctKey: "C",
    formulaHud: "V = \\pi r^2 t = 128\\pi, \\quad L(r) = 2\\pi r^2 + \\frac{2V}{r}, \\quad L'(r) = 0",
    hints: {
      concept: "Tabung tertutup memiliki luas permukaan minimum ketika tingginya tepat sama dengan diameter alasnya ($t = 2r$).",
      execution: "Dari $V = \\pi r^2 t = 128\\pi \\implies t = \\frac{128}{r^2}$. Substitusi ke $L(r) = 2\\pi r^2 + \\frac{256\\pi}{r}$."
    },
    explanation: "Turunkan $L'(r) = 4\\pi r - \\frac{256\\pi}{r^2} = 0 \\implies r^3 = 64 \\implies r = 4\\text{ cm}$. Maka tinggi tabung $t = \\frac{128}{4^2} = \\frac{128}{16} = 8\\text{ cm}$. Jawaban: C."
  },
  {
    id: "mtk-lat-h-17",
    subject: "mtk",
    mode: "latihan",
    difficulty: "hard",
    topic: "Sistem Persamaan Eksponen & Logaritma",
    questionHtml: "Jika $(x, y)$ memenuhi persamaan $^2\\log x + ^2\\log y = 5$ dan $(^2\\log x)^2 - (^2\\log y)^2 = 15$, dengan $x > y > 0$, maka nilai dari $x - 2y$ adalah...",
    options: [
      { key: "A", text: "8" },
      { key: "B", text: "12" },
      { key: "C", text: "14" },
      { key: "D", text: "16" },
      { key: "E", text: "20" }
    ],
    correctKey: "B",
    formulaHud: "a^2 - b^2 = (a + b)(a - b)",
    hints: {
      concept: "Misalkan $a = \\,^2\\log x$ dan $b = \\,^2\\log y$. Faktorkan bentuk selisih kuadrat $a^2 - b^2 = 15$.",
      execution: "$(a + b)(a - b) = 15 \\implies 5(a - b) = 15 \\implies a - b = 3$."
    },
    explanation: "Dari $a + b = 5$ dan $a - b = 3$, dijumlahkan menghasilkan $2a = 8 \\implies a = 4$ dan $b = 1$. Maka $x = 2^4 = 16$ dan $y = 2^1 = 2$. Nilai $x - 2y = 16 - 2(2) = 12$. Jawaban: B."
  },
  {
    id: "mtk-lat-h-18",
    subject: "mtk",
    mode: "latihan",
    difficulty: "hard",
    topic: "Transformasi Geometri",
    questionHtml: "Garis $g: 2x - 3y + 6 = 0$ dicerminkan terhadap garis $y = x$, kemudian dilanjutkan dengan rotasi sejauh $90^\\circ$ berlawanan arah jarum jam dengan pusat $O(0,0)$. Persamaan bayangan akhir garis $g$ adalah...",
    options: [
      { key: "A", text: "2x + 3y - 6 = 0" },
      { key: "B", text: "2x + 3y + 6 = 0" },
      { key: "C", text: "3x - 2y + 6 = 0" },
      { key: "D", text: "3x + 2y - 6 = 0" },
      { key: "E", text: "2x - 3y - 6 = 0" }
    ],
    correctKey: "A",
    formulaHud: "M_{y=x} = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}, \\quad R_{90^\\circ} = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}",
    hints: {
      concept: "Cari matriks komposisi transformasi $T = R_{90^\\circ} \\cdot M_{y=x}$, lalu nyatakan $(x, y)$ dalam $(x', y')$.",
      execution: "Refleksi $y=x$ mengubah $(x,y) \\to (y,x)$. Rotasi $+90^\\circ$ mengubah $(y,x) \\to (-x, y)$. Jadi $x' = -x$ dan $y' = y$."
    },
    explanation: "Dari $x' = -x \\implies x = -x'$ dan $y' = y \\implies y = y'$. Substitusikan ke persamaan awal: $2(-x') - 3(y') + 6 = 0 \\implies -2x' - 3y' + 6 = 0 \\implies 2x + 3y - 6 = 0$. Jawaban: A."
  },
  {
    id: "mtk-lat-h-19",
    subject: "mtk",
    mode: "latihan",
    difficulty: "hard",
    topic: "Limit Trigonometri",
    questionHtml: "Nilai dari $\\lim_{x \\to 0} \\frac{1 - \\cos 4x}{x \\sin 2x}$ adalah...",
    options: [
      { key: "A", text: "2" },
      { key: "B", text: "4" },
      { key: "C", text: "6" },
      { key: "D", text: "8" },
      { key: "E", text: "16" }
    ],
    correctKey: "B",
    formulaHud: "1 - \\cos 2\\alpha = 2 \\sin^2 \\alpha, \\quad \\lim_{x \\to 0} \\frac{\\sin ax}{bx} = \\frac{a}{b}",
    hints: {
      concept: "Ubah bentuk $1 - \\cos 4x$ menggunakan identitas sudut rangkap kosinus menjadi $2 \\sin^2 2x$.",
      execution: "$\\lim_{x \\to 0} \\frac{2 \\sin^2 2x}{x \\sin 2x} = \\lim_{x \\to 0} \\frac{2 \\sin 2x}{x}$."
    },
    explanation: "$\\lim_{x \\to 0} \\frac{2 \\sin 2x}{x} = 2 \\times \\frac{2}{1} = 4$. Jawaban: B."
  },
  {
    id: "mtk-lat-h-20",
    subject: "mtk",
    mode: "latihan",
    difficulty: "hard",
    topic: "Peluang Bersyarat & Teorema Bayes",
    questionHtml: "Sebuah pabrik semikonduktor memiliki dua lini mesin. Mesin A memproduksi $60\\%$ total chip dengan tingkat cacat $2\\%$, sedangkan Mesin B memproduksi $40\\%$ sisanya dengan tingkat cacat $5\\%$. Jika satu chip diambil secara acak dan ternyata cacat, berapakah peluang chip tersebut berasal dari Mesin B?",
    options: [
      { key: "A", text: "3/8" },
      { key: "B", text: "1/2" },
      { key: "C", text: "5/8" },
      { key: "D", text: "3/5" },
      { key: "E", text: "5/7" }
    ],
    correctKey: "C",
    formulaHud: "P(B \\mid C) = \\frac{P(B) \\cdot P(C \\mid B)}{P(A) \\cdot P(C \\mid A) + P(B) \\cdot P(C \\mid B)}",
    hints: {
      concept: "Gunakan Teorema Bayes: bagi peluang irisan (Mesin B dan Cacat) dengan peluang total seluruh produk cacat.",
      execution: "$P(A \\cap C) = 0,60 \\times 0,02 = 0,012$. Sedangkan $P(B \\cap C) = 0,40 \\times 0,05 = 0,020$."
    },
    explanation: "Peluang total cacat $P(C) = 0,012 + 0,020 = 0,032$. Maka $P(B \\mid C) = \\frac{0,020}{0,032} = \\frac{20}{32} = \\frac{5}{8}$. Jawaban: C."
  },

  // =========================================================================
  // PILOT SAMPLE: BAHASA INDONESIA & BAHASA INGGRIS (VALIDASI MULTI-TAB)
  // =========================================================================
  {
    id: "ind-lat-m-01",
    subject: "ind",
    mode: "latihan",
    difficulty: "medium",
    topic: "Penalaran Kritis & Ide Pokok Wacana",
    questionHtml: "Transformasi pembayaran digital melalui standar QRIS di tingkat pelaku usaha mikro tidak sekadar mempercepat transaksi kasir, tetapi juga membangun rekam jejak finansial formal yang sebelumnya tidak tercatat oleh perbankan. Namun, literasi keamanan siber yang timpang membuat sebagian pedagang rentan terhadap rekayasa sosial.<br><br>Manakah simpulan yang paling tepat berdasarkan paragraf di atas?",
    options: [
      { key: "A", text: "Seluruh pedagang mikro kini telah mendapatkan kredit perbankan berkat QRIS." },
      { key: "B", text: "Adopsi pembayaran digital membawa manfaat inklusi pencatatan keuangan, namun harus diimbangi penguatan literasi keamanan siber." },
      { key: "C", text: "Rekayasa sosial hanya menyerang pedagang yang menolak menggunakan uang tunai." },
      { key: "D", text: "Kecepatan transaksi kasir adalah satu-satunya alasan penggunaan QRIS." },
      { key: "E", text: "Perbankan wajib menghapus sistem QRIS karena rawan kejahatan siber." }
    ],
    correctKey: "B",
    formulaHud: "\\text{Simpulan Valid} = \\text{Premis Utama (Dampak Positif)} + \\text{Premis Kontras (Tantangan)}",
    hints: {
      concept: "Perhatikan konjungsi pertentangan 'Namun' yang menghubungkan manfaat inklusi finansial dengan risiko literasi keamanan.",
      execution: "Eliminasi opsi yang menggunakan kata ekstrem seperti 'Seluruh', 'Satu-satunya', atau 'Wajib menghapus'."
    },
    explanation: "Wacana menyoroti dua sisi: manfaat pencatatan finansial formal dan kerentanan akibat literasi siber yang timpang. Opsi B merangkum kedua premis secara akurat tanpa generalisasi berlebihan. Jawaban: B."
  },
  {
    id: "eng-lat-m-01",
    subject: "eng",
    mode: "latihan",
    difficulty: "medium",
    topic: "Reading Comprehension & Inference",
    questionHtml: "<em>While large language models excel at recognizing statistical patterns across massive corpora, treating their fluent outputs as infallible factual databases remains a critical epistemological error among novice researchers.</em><br><br>What can be reasonably inferred from the statement above?",
    options: [
      { key: "A", text: "Novice researchers never use large language models for academic work." },
      { key: "B", text: "Linguistic fluency in AI-generated text does not guarantee factual accuracy." },
      { key: "C", text: "Statistical pattern recognition is completely useless in modern computing." },
      { key: "D", text: "Large language models are designed exclusively to replace peer-reviewed journals." },
      { key: "E", text: "Experienced researchers rely solely on AI outputs without verification." }
    ],
    correctKey: "B",
    formulaHud: "\\text{Contrastive Clause: } \\text{While } X \\text{ (fluency/pattern)}, Y \\text{ (not infallible truth)}",
    hints: {
      concept: "Fokus pada kontras antara 'fluent outputs' (kelancaran bahasa) dan 'infallible factual databases' (basis data fakta tanpa celah).",
      execution: "Frasa 'critical epistemological error' menunjukkan bahwa menganggap output yang terdengar fasih pasti benar adalah sebuah kesalahan."
    },
    explanation: "Kalimat tersebut menegaskan bahwa meskipun model bahasa menghasilkan teks yang fasih secara statistik, menganggapnya selalu akurat secara faktual adalah kesalahan. Maka inferensi yang tepat adalah kelancaran bahasa tidak menjamin kebenaran fakta (B)."
  }
];
