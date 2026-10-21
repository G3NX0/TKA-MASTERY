# -*- coding: utf-8 -*-
"""
ekonomi_data_hard.py
--------------------
25 Authentic HOTS Hard Practice Questions for TKA 2026 Ekonomi (SMA/MA Soshum).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: eko-lat-h-01 .. eko-lat-h-25
"""

EKONOMI_HARD_ITEMS = [
    {
        "id": "eko-lat-h-01",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Keseimbangan Simultan Pasar Barang dan Pasar Uang (Model IS-LM)",
        "stem": "Dalam suatu perekonomian tertutup diketahui:\n- Pasar Barang (Kurva IS): $Y = 1.200 - 2.000r$\n- Pasar Uang (Kurva LM): $Y = 400 + 2.000r$\ndi mana $Y$ adalah pendapatan nasional riil dan $r$ adalah tingkat suku bunga riil. Jika pemerintah menjalankan kebijakan fiskal ekspansif yang menggeser kurva IS ke kanan menjadi $Y = 1.400 - 2.000r$ sementara bank sentral mempertahankan jumlah uang beredar konstan (kurva LM tetap), tingkat suku bunga keseimbangan ($r^*$) dan pendapatan nasional keseimbangan ($Y^*$) yang baru serta dampaknya terhadap investasi swasta (_crowding-out effect_) adalah...",
        "correct": "$r^* = 25\\% \\ (0,25)$, $Y^* = 900$, dan terjadi sebagian efek perdesakan investasi swasta (_partial crowding-out_) akibat kenaikan suku bunga dari $20\\%$ menjadi $25\\%$.",
        "distractors": [
            "$r^* = 20\\% \\ (0,20)$, $Y^* = 800$, dan tidak terjadi crowding-out karena pasar uang mampu menyerap seluruh belanja pemerintah.",
            "$r^* = 30\\% \\ (0,30)$, $Y^* = 1.000$, dan terjadi fenomena crowding-out total yang membuat pendapatan riil tidak bertambah.",
            "$r^* = 15\\% \\ (0,15)$, $Y^* = 700$, dan suku bunga turun merangsang lonjakan tajam investasi riil swasta domestik.",
            "$r^* = 25\\% \\ (0,25)$, $Y^* = 1.400$, dan seluruh kenaikan belanja pemerintah dikonversi menjadi pendapatan tanpa hambatan likuiditas."
        ],
        "formula": {
            "title": "KESEIMBANGAN SIMULTAN PASAR IS-LM",
            "latex": "\\begin{aligned} \\text{Awal:} & \\quad 1.200 - 2.000r = 400 + 2.000r \\implies 4.000r = 800 \\implies r_0 = 0,20 \\ (20\\%), \\ Y_0 = 800 \\\\ \\text{Setelah Fiskal Ekspansif:} & \\quad 1.400 - 2.000r = 400 + 2.000r \\implies 4.000r = 1.000 \\implies \\mathbf{r^* = 0,25 \\ (25\\%)} \\\\ Y^* & = 400 + 2.000(0,25) = 400 + 500 = \\mathbf{900} \\\\ \\text{Efek Crowding-out:} & \\quad \\text{Jika suku bunga tetap 20\\%, } Y = 1.400 - 2.000(0,20) = 1.000. \\\\ & \\quad \\text{Kenaikan suku bunga memangkas potensi } Y \\text{ dari } 1.000 \\text{ menjadi } 900 \\text{ (-100 output)}. \\end{aligned}",
            "legend": "• Kurva IS (Investasi-Tabungan): Hubungan negatif antara suku bunga dan output riil di pasar barang<br>• Kurva LM (Likuiditas-Uang): Hubungan positif antara suku bunga dan output riil di pasar uang<br>• Crowding-out: Kenaikan belanja pemerintah menaikkan suku bunga, sehingga menekan investasi swasta"
        },
        "hints": {
            "concept": "Samakan persamaan IS baru dengan LM untuk mencari suku bunga baru r*, lalu substitusikan r* ke dalam salah satu persamaan untuk mencari Y*.",
            "execution": "1.400 - 2.000r = 400 + 2.000r -> 4.000r = 1.000 -> r = 0,25 (25%). Y = 400 + 2.000(0,25) = 900. Kenaikan r menyebabkan crowding out."
        }
    },
    {
        "id": "eko-lat-h-02",
        "materi": "STRUKTUR PASAR",
        "topic": "Keseimbangan Duopoli Model Cournot (Cournot Duopoly Equilibrium)",
        "stem": "Dua perusahaan farmasi identik ($A$ dan $B$) membentuk pasar duopoli non-kolusif untuk memproduksi serum vaksin dengan fungsi permintaan pasar $P = 150 - (Q_A + Q_B)$. Kedua perusahaan memiliki struktur biaya marjinal konstan yang sama tanpa biaya tetap, yaitu $MC_A = MC_B = 30$. Berdasarkan Model Keseimbangan Cournot, kuantitas output optimal masing-masing perusahaan ($Q_A^*, Q_B^*$), harga pasar ($P^*$), dan perbandingannya dengan hasil monopoli murni adalah...",
        "correct": "$Q_A^* = Q_B^* = 40$ unit (total output $Q = 80$ unit), harga pasar $P^* = \\text{Rp } 70,-$, di mana total output duopoli lebih banyak dan harga lebih murah dibandingkan monopoli murni ($Q_{\\text{mono}} = 60, P_{\\text{mono}} = 90$).",
        "distractors": [
            "$Q_A^* = Q_B^* = 60$ unit (total output $Q = 120$ unit), harga pasar $P^* = \\text{Rp } 30,-$, sama persis dengan kondisi persaingan sempurna.",
            "$Q_A^* = Q_B^* = 30$ unit (total output $Q = 60$ unit), harga pasar $P^* = \\text{Rp } 90,-$, sama persis dengan kartel monopoli gabungan.",
            "$Q_A^* = 50$ unit, $Q_B^* = 25$ unit, harga pasar $P^* = \\text{Rp } 75,-$, karena perusahaan A bertindak sebagai pemimpin pasar Stackelberg.",
            "$Q_A^* = Q_B^* = 20$ unit (total output $Q = 40$ unit), harga pasar $P^* = \\text{Rp } 110,-$, dengan deadweight loss melebihi monopoli absolut."
        ],
        "formula": {
            "title": "PENURUNAN KESEIMBANGAN NASH-COURNOT",
            "latex": "\\begin{aligned} TR_A & = P \\cdot Q_A = (150 - Q_A - Q_B)Q_A = 150Q_A - Q_A^2 - Q_A Q_B \\\\ MR_A & = 150 - 2Q_A - Q_B = MC = 30 \\implies 2Q_A = 120 - Q_B \\implies Q_A = 60 - 0,5Q_B \\\\ \\text{Simetris: } & \\quad Q_B = 60 - 0,5Q_A \\implies Q_A = 60 - 0,5(60 - 0,5Q_A) = 30 + 0,25Q_A \\\\ 0,75Q_A & = 30 \\implies \\mathbf{Q_A^* = 40}, \\ \\mathbf{Q_B^* = 40} \\implies Q_{\\text{total}} = 80 \\\\ \\mathbf{P^*} & = 150 - 80 = \\mathbf{70} \\end{aligned}",
            "legend": "• Fungsi Reaksi Cournot: $Q_i = \\frac{a - c}{2b} - \\frac{1}{2}Q_j$<br>• Keseimbangan Cournot: Output industri $Q = \\frac{N}{N+1} \\left(\\frac{a - c}{b}\\right) = \\frac{2}{3}(120) = 80$"
        },
        "hints": {
            "concept": "Tentukan TR_A dan turunkan ke MR_A. Samakan MR_A = MC untuk mencari fungsi reaksi Q_A terhadap Q_B. Karena simetris, Q_A = Q_B.",
            "execution": "MR_A = 150 - 2Q_A - Q_B = 30 -> 2Q_A + Q_B = 120. Karena Q_A = Q_B -> 3Q_A = 120 -> Q_A = 40, Q_B = 40. P = 150 - 80 = 70."
        }
    },
    {
        "id": "eko-lat-h-03",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Model Pertumbuhan Ekonomi Neoklasik Solow-Swan (Steady-State Capital)",
        "stem": "Dalam model pertumbuhan ekonomi Solow-Swan, fungsi produksi per kapita suatu negara dirumuskan sebagai $y = k^{0,5}$ (atau $y = \\sqrt{k}$), di mana $y$ adalah output per pekerja dan $k$ adalah rasio modal per pekerja. Negara tersebut memiliki tingkat tabungan investasi $s = 30\\% \\ (0,3)$, tingkat penyusutan modal $\\delta = 3\\% \\ (0,03)$, dan laju pertumbuhan angkatan kerja $n = 2\\% \\ (0,02)$ per tahun. Rasio modal per pekerja pada kondisi kondisi mapan (_Steady-State Capital per Worker_ / $k^*$) dan output per pekerja mapan ($y^*$) adalah...",
        "correct": "$k^* = 36$ unit modal per pekerja dan $y^* = 6$ unit output per pekerja.",
        "distractors": [
            "$k^* = 25$ unit modal per pekerja dan $y^* = 5$ unit output per pekerja.",
            "$k^* = 49$ unit modal per pekerja dan $y^* = 7$ unit output per pekerja.",
            "$k^* = 16$ unit modal per pekerja dan $y^* = 4$ unit output per pekerja.",
            "$k^* = 64$ unit modal per pekerja dan $y^* = 8$ unit output per pekerja."
        ],
        "formula": {
            "title": "KONDISI STEADY-STATE PERTUMBUHAN EKONOMI SOLOW",
            "latex": "\\begin{aligned} \\Delta k & = s \\cdot f(k) - (\\delta + n)k = 0 \\implies s \\cdot \\sqrt{k} = (\\delta + n)k \\\\ 0,3 \\sqrt{k} & = (0,03 + 0,02)k = 0,05 k \\\\ \\frac{\\sqrt{k}}{k} & = \\frac{0,05}{0,3} \\implies \\frac{1}{\\sqrt{k}} = \\frac{1}{6} \\implies \\sqrt{k} = 6 \\implies \\mathbf{k^* = 36} \\\\ \\mathbf{y^*} & = f(k^*) = \\sqrt{36} = \\mathbf{6} \\end{aligned}",
            "legend": "• Kondisi Mapan (Steady State): Titik di mana investasi bruto per kapita ($s \\cdot y$) tepat mengimbangi pelemahan modal akibat depresiasi dan pertumbuhan pekerja ($(\\delta + n)k$)"
        },
        "hints": {
            "concept": "Pada kondisi steady-state, investasi baru = investasi penggantian: s . f(k) = (delta + n)k. Masukkan nilai s = 0,3 dan delta + n = 0,05.",
            "execution": "0,3 * sqrt(k) = 0,05 * k -> sqrt(k) / k = 0,05 / 0,3 = 1/6 -> sqrt(k) = 6 -> k* = 36. Output y* = sqrt(36) = 6."
        }
    },
    {
        "id": "eko-lat-h-04",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Efektivitas Kebijakan Makro dalam Model Mundell-Fleming (Kurs Mengambang)",
        "stem": "Berdasarkan Model Mundell-Fleming untuk perekonomian terbuka kecil dengan mobilitas modal internasional sempurna (_perfect capital mobility_) di bawah sistem nilai tukar mengambang bebas (_floating exchange rate_), analisis komparatif mengenai efektivitas kebijakan moneter dan fiskal dalam meningkatkan output pendapatan riil ($Y$) adalah...",
        "correct": "Kebijakan moneter sangat efektif (menurunkan suku bunga memicu aliran modal keluar, mendepresiasi mata uang, lalu mendongkrak ekspor neto), sedangkan kebijakan fiskal sama sekali tidak efektif karena dorongan belanja negara dieliminasi sepenuhnya oleh apresiasi nilai tukar (_crowding-out nilai tukar_ $100\\%$).",
        "distractors": [
            "Kebijakan fiskal sangat efektif menaikkan output riil sementara kebijakan moneter mandul karena likuiditas terperangkap di pasar uang.",
            "Kedua kebijakan sama-sama sangat efektif melipatgandakan output riil karena suku bunga domestik terisolasi dari suku bunga global.",
            "Kedua kebijakan sama sekali tidak efektif karena mobilitas modal sempurna melumpuhkan seluruh instrumen transmisi pemerintah dan bank sentral.",
            "Kebijakan fiskal hanya efektif jika pemerintah mencetak surat utang dalam mata uang emas murni secara tertutup."
        ],
        "formula": {
            "title": "TRIPLIKASI MODEL MUNDELL-FLEMING (FLOATING EXCHANGE RATE)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Moneter Ekspansif:}} & \\quad M \\uparrow \\implies LM^* \\text{ geser kanan} \\implies r < r^* \\implies \\text{Capital Outflow} \\implies e \\downarrow \\implies NX \\uparrow \\implies \\mathbf{Y \\uparrow \\text{ (Sangat Efektif!)}} \\\\ \\mathbf{\\text{Fiskal Ekspansif:}} & \\quad G \\uparrow \\implies IS^* \\text{ geser kanan} \\implies r > r^* \\implies \\text{Capital Inflow} \\implies e \\uparrow \\implies NX \\downarrow \\implies \\mathbf{Y \\text{ Tetap (Mandul!)}} \\end{aligned}",
            "legend": "• $e$: Nilai tukar nominal (kurs)<br>• $NX$: Ekspor neto ($X - M$)<br>• Pada kurs mengambang bebas, transmisi kebijakan moneter beroperasi melalui depresiasi kurs valuta"
        },
        "hints": {
            "concept": "Dalam Mundell-Fleming kurs mengambang + modal bebas sempurna: Kebijakan moneter berkuasa (ekspansi moneter depresiasi kurs -> NX naik -> Y naik). Kebijakan fiskal mandul karena apresiasi kurs mengeliminasi NX.",
            "execution": "Pilih: Kebijakan moneter sangat efektif, kebijakan fiskal tidak efektif (crowding out nilai tukar 100%)."
        }
    },
    {
        "id": "eko-lat-h-05",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Penetapan Suku Bunga Acuan Berdasarkan Aturan Taylor (Taylor Rule)",
        "stem": "Bank Sentral menerapkan kaidah kebijakan moneter Aturan Taylor (Taylor Rule) standar untuk menetapkan target suku bunga nominal acuan ($i^*$) dengan persamaan:\n$$i^* = r_n + \\pi + 0,5(\\pi - \\pi^*) + 0,5(y - \\bar{y})$$\ndi mana suku bunga riil netral adalah $r_n = 2\\%$, target inflasi bank sentral adalah $\\pi^* = 3\\%$, tingkat inflasi aktual saat ini adalah $\\pi = 5\\%$, dan kesenjangan output (_output gap_) adalah $(y - \\bar{y}) = +2\\%$ (perekonomian mengalami _overheating_ di atas kapasitas potensial). Target suku bunga nominal acuan yang wajib ditetapkan oleh Bank Sentral adalah...",
        "correct": "$i^* = 9,0\\%$, sebagai respon kontraktif untuk menekan inflasi yang melampaui target dan mendinginkan kesenjangan output positif.",
        "distractors": [
            "$i^* = 7,0\\%$, hasil kalkulasi penjumlahan suku bunga riil netral dengan tingkat inflasi aktual murni.",
            "$i^* = 8,0\\%$, hasil perhitungan tanpa memperhitungkan bobot reaksi terhadap kesenjangan output agregat.",
            "$i^* = 10,5\\%$, hasil penerapan koefisien pengetatan moneter ganda pada instrumen giro wajib minimum.",
            "$i^* = 5,5\\%$, hasil pelonggaran moneter agresif untuk menstimulasi kredit perbankan komersial."
        ],
        "formula": {
            "title": "FORMULA ATURAN TAYLOR (TAYLOR RULE 1993)",
            "latex": "\\begin{aligned} i^* & = r_n + \\pi + 0,5(\\pi - \\pi^*) + 0,5(y - \\bar{y}) \\\\ & = 2\\% + 5\\% + 0,5(5\\% - 3\\%) + 0,5(2\\%) \\\\ & = 7\\% + 0,5(2\\%) + 0,5(2\\%) \\\\ & = 7\\% + 1\\% + 1\\% = \\mathbf{9,0\\%} \\end{aligned}",
            "legend": "• Prinsip Taylor (Taylor Principle): Koefisien respon inflasi terhadap suku bunga nominal harus lebih dari 1 ($1 + 0,5 = 1,5$) agar suku bunga riil meningkat saat inflasi naik, sehingga mampu meredam laju inflasi"
        },
        "hints": {
            "concept": "Taylor Rule: i* = r_n + pi + 0,5(pi - pi*) + 0,5(output gap). Masukkan r_n = 2, pi = 5, pi* = 3, output gap = 2.",
            "execution": "i* = 2 + 5 + 0,5(5 - 3) + 0,5(2) = 7 + 1 + 1 = 9,0%."
        }
    },
    {
        "id": "eko-lat-h-06",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Maksimisasi Utilitas Cobb-Douglas dengan Metode Lagrange (Lagrangian Multiplier)",
        "stem": "Seorang konsumen memiliki fungsi utilitas terhadap barang $X$ dan barang $Y$ berbentuk Cobb-Douglas: $U(X, Y) = X^{0,6} Y^{0,4}$. Konsumen tersebut memiliki anggaran pendapatan sebesar $I = \\text{Rp } 1.000.000,-$, sedangkan harga pasar barang $X$ adalah $P_X = \\text{Rp } 20.000,-$ dan harga barang $Y$ adalah $P_Y = \\text{Rp } 10.000,-$. Kombinasi kuantitas konsumsi optimal ($X^*, Y^*$) yang memaksimumkan kepuasan konsumen tersebut adalah...",
        "correct": "$X^* = 30$ unit dan $Y^* = 40$ unit, di mana konsumen membelanjakan $60\\%$ anggarannya untuk barang $X$ (Rp 600.000,-) dan $40\\%$ untuk barang $Y$ (Rp 400.000,-).",
        "distractors": [
            "$X^* = 25$ unit dan $Y^* = 50$ unit, dengan membagi total anggaran belanja secara seimbang rata lima puluh persen.",
            "$X^* = 40$ unit dan $Y^* = 20$ unit, yang memprioritaskan konsumsi barang bernilai ekonomi lebih tinggi.",
            "$X^* = 50$ unit dan $Y^* = 0$ unit, di mana konsumen menghabiskan seluruh pendapatan hanya pada barang kebutuhan primer.",
            "$X^* = 20$ unit dan $Y^* = 60$ unit, hasil estimasi titik potong garis anggaran tanpa mempertimbangkan proporsi elastisitas utilitas."
        ],
        "formula": {
            "title": "SIFAT KHUSUS FUNGSI UTILITAS COBB-DOUGLAS",
            "latex": "\\begin{aligned} U = X^\\alpha Y^\\beta & \\implies \\text{Porsi Anggaran Belanja Barang } X = \\frac{\\alpha}{\\alpha + \\beta} \\cdot I \\\\ \\text{Belanja } X & = \\frac{0,6}{0,6 + 0,4} \\times 1.000.000 = \\text{Rp } 600.000 \\implies \\mathbf{X^* = \\frac{600.000}{20.000} = 30 \\text{ unit}} \\\\ \\text{Belanja } Y & = \\frac{0,4}{0,6 + 0,4} \\times 1.000.000 = \\text{Rp } 400.000 \\implies \\mathbf{Y^* = \\frac{400.000}{10.000} = 40 \\text{ unit}} \\end{aligned}",
            "legend": "• Fungsi Permintaan Marshallian Cobb-Douglas: $X^* = \\frac{\\alpha I}{(\\alpha+\\beta)P_X}$ dan $Y^* = \\frac{\\beta I}{(\\alpha+\\beta)P_Y}$<br>• Bukti Anggaran: $30(20.000) + 40(10.000) = 600.000 + 400.000 = 1.000.000$ (Habis terpakai)"
        },
        "hints": {
            "concept": "Pada utilitas Cobb-Douglas U = X^a Y^b, proporsi pengeluaran untuk X adalah a/(a+b) dari pendapatan I, dan untuk Y adalah b/(a+b) dari I.",
            "execution": "Pengeluaran X = 0,6 * 1.000.000 = 600.000 -> X* = 600.000 / 20.000 = 30 unit. Pengeluaran Y = 0,4 * 1.000.000 = 400.000 -> Y* = 400.000 / 10.000 = 40 unit."
        }
    },
    {
        "id": "eko-lat-h-07",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Insidensi Pajak (Tax Incidence) dan Beban Hilang Bobot Mati (Deadweight Loss)",
        "stem": "Fungsi permintaan dan penawaran suatu produk kebutuhan pokok dirumuskan sebagai:\n- Permintaan: $P = 100 - 2Q$\n- Penawaran: $P = 20 + 2Q$\nPemerintah mengenakan pajak spesifik sebesar $t = \\text{Rp } 20,-$ per unit barang. Besarnya beban pajak yang ditanggung oleh konsumen ($T_k$), produsen ($T_p$), dan Beban Hilang Bobot Mati (Deadweight Loss / DWL) akibat intervensi pajak tersebut adalah...",
        "correct": "$T_k = \\text{Rp } 10,-$ per unit, $T_p = \\text{Rp } 10,-$ per unit, dan $\\text{DWL} = \\text{Rp } 50,-$.",
        "distractors": [
            "$T_k = \\text{Rp } 20,-$ per unit, $T_p = \\text{Rp } 0,-$ per unit, dan $\\text{DWL} = \\text{Rp } 100,-$.",
            "$T_k = \\text{Rp } 15,-$ per unit, $T_p = \\text{Rp } 5,-$ per unit, dan $\\text{DWL} = \\text{Rp } 75,-$.",
            "$T_k = \\text{Rp } 5,-$ per unit, $T_p = \\text{Rp } 15,-$ per unit, dan $\\text{DWL} = \\text{Rp } 25,-$.",
            "$T_k = \\text{Rp } 10,-$ per unit, $T_p = \\text{Rp } 10,-$ per unit, dan $\\text{DWL} = \\text{Rp } 0,-$ karena pasar menyerap pajak secara efisien."
        ],
        "formula": {
            "title": "KALKULASI INSIDENSI PAJAK DAN DEADWEIGHT LOSS (DWL)",
            "latex": "\\begin{aligned} \\text{Ekuilibrium Awal:} & \\quad 100 - 2Q = 20 + 2Q \\implies 4Q = 80 \\implies Q_0 = 20, \\ P_0 = 60 \\\\ \\text{Penawaran Baru:} & \\quad P_s' = 20 + 2Q + 20 = 40 + 2Q \\\\ \\text{Ekuilibrium Pajak:} & \\quad 100 - 2Q = 40 + 2Q \\implies 4Q = 60 \\implies Q_t = 15, \\ P_t = 70 \\\\ \\text{Insidensi Pajak:} & \\quad T_k = P_t - P_0 = 70 - 60 = \\mathbf{10}, \\quad T_p = t - T_k = 20 - 10 = \\mathbf{10} \\\\ \\mathbf{\\text{Deadweight Loss (DWL):}} & \\quad \\frac{1}{2} \\times t \\times (Q_0 - Q_t) = \\frac{1}{2} \\times 20 \\times (20 - 15) = 10 \\times 5 = \\mathbf{50} \\end{aligned}",
            "legend": "• Kemiringan Permintaan dan Penawaran sama besar ($|-2| = 2$), sehingga beban pajak terbagi merata 50:50 antara konsumen dan produsen<br>• DWL: Kerugian surplus total masyarakat (segitiga Harberger) yang tidak diterima oleh pihak mana pun"
        },
        "hints": {
            "concept": "Cari keseimbangan awal (Q0, P0), lalu tentukan fungsi penawaran baru setelah pajak Ps' = Ps + t. Cari ekuilibrium baru (Qt, Pt). Beban konsumen = Pt - P0. DWL = 0,5 * t * (Q0 - Qt).",
            "execution": "Q0 = 20, P0 = 60. Ps' = 40 + 2Q -> 100 - 2Q = 40 + 2Q -> Qt = 15, Pt = 70. Tk = 70 - 60 = 10, Tp = 10. DWL = 0,5 * 20 * (20 - 15) = 50."
        }
    },
    {
        "id": "eko-lat-h-08",
        "materi": "STRUKTUR PASAR",
        "topic": "Diskriminasi Harga Derajat Ketiga (Third-Degree Price Discrimination)",
        "stem": "Sebuah maskapai penerbangan memiliki monopoli rute dan melayani dua segmen penumpang yang terpisah secara sempurna:\n- Pasar 1 (Penumpang Bisnis): $P_1 = 200 - Q_1$\n- Pasar 2 (Wisatawan): $P_2 = 140 - Q_2$\nBiaya marjinal penyediaan kursi adalah konstan $MC = 20$ tanpa biaya tetap. Jika maskapai menerapkan diskriminasi harga derajat ketiga untuk memaksimumkan total keuntungan, harga tiket pada Pasar Bisnis ($P_1^*$), Pasar Wisatawan ($P_2^*$), dan perbandingannya adalah...",
        "correct": "$P_1^* = \\text{Rp } 110,-$ dan $P_2^* = \\text{Rp } 80,-$, di mana harga lebih mahal dikenakan pada Pasar 1 karena penumpang bisnis memiliki elastisitas permintaan yang lebih inelastis dibandingkan wisatawan.",
        "distractors": [
            "$P_1^* = \\text{Rp } 100,-$ dan $P_2^* = \\text{Rp } 100,-$, karena hukum satu harga (Law of One Price) melarang disparitas tarif antar konsumen.",
            "$P_1^* = \\text{Rp } 80,-$ dan $P_2^* = \\text{Rp } 110,-$, karena wisatawan mengonsumsi fasilitas hiburan tambahan di kabin pesawat.",
            "$P_1^* = \\text{Rp } 140,-$ dan $P_2^* = \\text{Rp } 60,-$, hasil penetapan tarif batas atas oleh kementerian perhubungan.",
            "$P_1^* = \\text{Rp } 180,-$ dan $P_2^* = \\text{Rp } 120,-$, dengan kuantitas kursi dibatasi separuh kapasitas penerbangan komersial."
        ],
        "formula": {
            "title": "SYARAT LABA DISKRIMINASI HARGA DERAJAT TIGA",
            "latex": "\\begin{aligned} MR_1 = MC & \\implies 200 - 2Q_1 = 20 \\implies 2Q_1 = 180 \\implies Q_1^* = 90 \\\\ & \\implies \\mathbf{P_1^* = 200 - 90 = 110} \\\\ MR_2 = MC & \\implies 140 - 2Q_2 = 20 \\implies 2Q_2 = 120 \\implies Q_2^* = 60 \\\\ & \\implies \\mathbf{P_2^* = 140 - 60 = 80} \\\\ \\text{Aturan Ramsey-Lerner:} & \\quad \\frac{P_1}{P_2} = \\frac{1 - 1/|E_2|}{1 - 1/|E_1|} \\implies \\text{Pasar lebih inelastis dikenakan harga lebih tinggi} \\end{aligned}",
            "legend": "• Prasyarat Diskriminasi Harga: Kekuatan monopoli, pemisahan pasar yang efektif (tidak ada arbitrase/reselling), dan elastisitas permintaan yang berbeda di tiap pasar"
        },
        "hints": {
            "concept": "Samakan MR tiap pasar dengan MC: MR1 = MC dan MR2 = MC. Dari situ cari Q1 dan Q2, lalu substitusikan ke P1 dan P2.",
            "execution": "200 - 2Q1 = 20 -> Q1 = 90 -> P1 = 110. 140 - 2Q2 = 20 -> Q2 = 60 -> P2 = 80."
        }
    },
    {
        "id": "eko-lat-h-09",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Eksternalitas Negatif Produksi dan Tarif Pajak Korektif Pigouvian",
        "stem": "Sebuah pabrik pulp dan kertas beroperasi di tepi sungai dengan fungsi biaya marjinal privat $MPC = 40 + 2Q$ dan menghadapi permintaan pasar $P = 160 - Q$. Proses produksi tersebut membuang limbah cair ke sungai yang merugikan masyarakat nelayan sekitar dengan biaya kerusakan marjinal eksternal $MEC = Q$. Agar tercapai tingkat alokasi produksi yang efisien secara sosial ($MSC = MSB$), kebijakan pajak korektif Pigouvian per unit output ($t^*$) yang wajib dikenakan pemerintah kepada pabrik tersebut adalah...",
        "correct": "$t^* = \\text{Rp } 30,-$ per unit barang, yang akan menurunkan output dari ekuilibrium pasar bebas $Q_m = 40$ unit menjadi tingkat output optimum sosial $Q^* = 30$ unit.",
        "distractors": [
            "$t^* = \\text{Rp } 40,-$ per unit barang, yang akan menghentikan seluruh aktivitas operasional pabrik kertas.",
            "$t^* = \\text{Rp } 20,-$ per unit barang, hasil perhitungan dari biaya marjinal privat awal produsen.",
            "$t^* = \\text{Rp } 10,-$ per unit barang, yang membiarkan sebagian besar limbah tetap mencemari perairan umum.",
            "$t^* = \\text{Rp } 50,-$ per unit barang, hasil pembebanan denda administratif tetap tanpa menghitung ekuilibrium."
        ],
        "formula": {
            "title": "PENENTUAN PAJAK PIGOUVIAN INTERNALISASI EKSTERNALITAS",
            "latex": "\\begin{aligned} \\text{Pasar Bebas (Privat):} & \\quad MPC = P \\implies 40 + 2Q = 160 - Q \\implies 3Q = 120 \\implies Q_m = 40 \\\\ \\text{Optimum Sosial:} & \\quad MSC = MPC + MEC = (40 + 2Q) + Q = 40 + 3Q \\\\ MSC = MSB & \\implies 40 + 3Q = 160 - Q \\implies 4Q = 120 \\implies \\mathbf{Q^* = 30} \\\\ \\mathbf{\\text{Pajak Pigouvian:}} & \\quad \\mathbf{t^* = MEC(Q^*) = 30} \\\\ \\text{Cek Biaya Pajak:} & \\quad MPC' = MPC + t^* = (40 + 2Q) + 30 = 70 + 2Q \\\\ 70 + 2Q & = 160 - Q \\implies 3Q = 90 \\implies Q = 30 \\text{ (Tepat tercapai!)} \\end{aligned}",
            "legend": "• Eksternalitas Negatif: Menimbulkan over-produksi di pasar bebas ($Q_m > Q^*$) dan inefisiensi sosial (DWL)<br>• Pajak Pigouvian menginternalisasi biaya eksternal sehingga keputusan privat produsen selaras dengan optimum sosial"
        },
        "hints": {
            "concept": "Tentukan MSC = MPC + MEC. Samakan MSC = MSB (di mana MSB = P) untuk memperoleh Q optimum sosial Q*. Tarif pajak Pigouvian t* = MEC(Q*).",
            "execution": "MSC = 40 + 2Q + Q = 40 + 3Q. 40 + 3Q = 160 - Q -> 4Q = 120 -> Q* = 30. Pajak t* = MEC(30) = 30."
        }
    },
    {
        "id": "eko-lat-h-10",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Hipotesis Pendapatan Permanen Friedman vs Pendapatan Sementara",
        "stem": "Dalam Teori Konsumsi Hipotesis Pendapatan Permanen (Permanent Income Hypothesis) yang dikembangkan oleh Milton Friedman, total pendapatan konsumen dibagi menjadi Pendapatan Permanen ($Y_p$) dan Pendapatan Sementara/Transitori ($Y_t$). Respon perilaku konsumsi masyarakat terhadap stimulus bantuan tunai langsung (BLT) pemerintah yang bersifat sementara (_one-off transfer_) menurut teori ini adalah...",
        "correct": "Kecenderungan mengonsumsi marjinal dari pendapatan sementara ($MPC_t$) mendekati nol, karena konsumen yang rasional akan menabung sebagian besar dana BLT tersebut untuk meratakan pola konsumsi sepanjang hidupnya (_consumption smoothing_), sehingga dampak pengganda konsumsinya sangat kecil.",
        "distractors": [
            "Seluruh dana BLT akan langsung dihabiskan untuk konsumsi primer dengan nilai $MPC_t$ sama persis dengan satu.",
            "Konsumen akan meminjam uang lebih banyak di perbankan karena menganggap dana BLT sebagai kenaikan pendapatan tetap.",
            "Tingkat konsumsi masyarakat akan anjlok drastis karena timbul ketakutan terhadap lonjakan tarif pajak masa depan.",
            "Perekonomian akan mengalami perangkap likuiditas di mana fungsi konsumsi berubah menjadi garis melengkung ke bawah."
        ],
        "formula": {
            "title": "HIPOTESIS PENDAPATAN PERMANEN (PIH - MILTON FRIEDMAN)",
            "latex": "\\begin{aligned} Y & = Y_p + Y_t \\quad \\text{dan} \\quad C = C_p + C_t \\\\ C & = \\alpha Y_p \\implies MPC_{\\text{permanen}} \\approx 0,8 - 0,9 \\\\ C_t & \\approx 0 \\implies \\mathbf{MPC_{\\text{transitori}} \\approx 0} \\quad (\\text{Sebagian besar ditabung: } \\Delta S \\approx \\Delta Y_t) \\end{aligned}",
            "legend": "• Consumption Smoothing: Konsumen lebih menyukai pola konsumsi yang stabil sepanjang waktu daripada konsumsi yang berfluktuasi tajam mengikuti volatilitas pendapatan jangka pendek"
        },
        "hints": {
            "concept": "Friedman menyatakan konsumsi didorong pendapatan permanen. Pendapatan transitori (sementara seperti BLT) memiliki MPC mendekati nol karena mayoritas ditabung.",
            "execution": "Pilih opsi: MPC transitori mendekati nol karena konsumen menabung untuk consumption smoothing."
        }
    },
    {
        "id": "eko-lat-h-11",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Model Permintaan Uang Transaksi Persediaan Baumol-Tobin",
        "stem": "Berdasarkan Model Persediaan Baumol-Tobin untuk permintaan uang transaksi, seorang pengusaha membutuhkan pengeluaran dana transaksi riil sebesar $Y = \\text{Rp } 400.000.000,-$ per tahun secara merata. Biaya tetap setiap kali melakukan penarikan dana tunai dari bank (ongkos pergi ke bank dan biaya administrasi) adalah $F = \\text{Rp } 50.000,-$ per transaksi, sedangkan tingkat suku bunga pasar uang adalah $r = 10\\% \\ (0,10)$ per tahun. Jumlah penarikan tunai optimal setiap kali transaksi ($C^*$) dan rata-rata saldo uang kas yang dipegang ($M^*$) adalah...",
        "correct": "Penarikan kas optimal sebesar $C^* = \\text{Rp } 20.000.000,-$ per transaksi dan saldo kas rata-rata yang disimpan dalam dompet adalah $M^* = \\text{Rp } 10.000.000,-$.",
        "distractors": [
            "Penarikan $C^* = \\text{Rp } 40.000.000,-$ dan rata-rata saldo $M^* = \\text{Rp } 20.000.000,-$.",
            "Penarikan $C^* = \\text{Rp } 10.000.000,-$ dan rata-rata saldo $M^* = \\text{Rp } 5.000.000,-$.",
            "Penarikan $C^* = \\text{Rp } 30.000.000,-$ dan rata-rata saldo $M^* = \\text{Rp } 15.000.000,-$.",
            "Penarikan $C^* = \\text{Rp } 50.000.000,-$ dan rata-rata saldo $M^* = \\text{Rp } 25.000.000,-$."
        ],
        "formula": {
            "title": "MODEL PERMINTAAN UANG BAUMOL-TOBIN",
            "latex": "\\begin{aligned} \\text{Total Biaya Kas (TC)} & = \\frac{Y}{C} F + \\frac{C}{2} r \\\\ \\frac{d(TC)}{dC} = 0 & \\implies -\\frac{YF}{C^2} + \\frac{r}{2} = 0 \\implies C^2 = \\frac{2FY}{r} \\implies \\mathbf{C^* = \\sqrt{\\frac{2FY}{r}}} \\\\ C^* & = \\sqrt{\\frac{2 \\times 50.000 \\times 400.000.000}{0,10}} = \\sqrt{\\frac{4 \\times 10^{13}}{0,10}} = \\sqrt{4 \\times 10^{14}} = \\mathbf{20.000.000} \\\\ \\mathbf{M^*} & = \\frac{C^*}{2} = \\frac{20.000.000}{2} = \\mathbf{10.000.000} \\end{aligned}",
            "legend": "• $Y$: Kebutuhan pengeluaran total tahunan (Rp 400 Juta)<br>• $F$: Biaya tetap per penarikan (Rp 50.000,-)<br>• $r$: Biaya peluang suku bunga ($10\\%$)<br>• $M^*$: Saldo kas rata-rata yang disimpan dalam dompet"
        },
        "hints": {
            "concept": "Formula Baumol-Tobin: C* = sqrt(2FY / r) dan rata-rata saldo kas M* = C* / 2.",
            "execution": "C* = sqrt(2 * 50.000 * 400 jt / 0,10) = sqrt(4 * 10^14) = 20.000.000. Rata-rata saldo M* = 20 jt / 2 = 10.000.000."
        }
    },
    {
        "id": "eko-lat-h-12",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Paritas Suku Bunga Tak Terlindungi (Uncovered Interest Rate Parity / UIP)",
        "stem": "Investor keuangan global mempertimbangkan penempatan dana antara instrumen Surat Berharga Negara (SBN) di Indonesia dan US Treasury Bill di Amerika Serikat. Diketahui:\n- Suku bunga nominal SBN Indonesia: $i_{\\text{IDR}} = 6,5\\%$ per tahun\n- Suku bunga nominal US Treasury: $i_{\\text{USD}} = 4,0\\%$ per tahun\nBerdasarkan kondisi Paritas Suku Bunga Tak Terlindungi (Uncovered Interest Rate Parity / UIP), pasar valuta asing memprediksikan bahwa nilai tukar Rupiah terhadap Dolar AS selama satu tahun ke depan akan mengalami...",
        "correct": "Depresiasi (pelemahan) sebesar $2,5\\%$, yang mengeliminasi selisih keuntungan bunga domestik sehingga imbal hasil yang diharapkan antar kedua negara menjadi seimbang.",
        "distractors": [
            "Apresiasi (penguatan) sebesar $2,5\\%$, karena suku bunga Indonesia lebih tinggi menarik arus modal masuk permanen.",
            "Depresiasi sebesar $10,5\\%$, hasil penjumlahan suku bunga nominal kedua negara dalam neraca modal.",
            "Apresiasi sebesar $6,5\\%$, sebanding dengan imbal hasil kupon obligasi pemerintah Indonesia.",
            "Stabilitas mutlak $0\\%$, karena pasar valuta asing selalu berada dalam kondisi nilai tukar riil konstan."
        ],
        "formula": {
            "title": "PARITAS SUKU BUNGA TAK TERLINDUNGI (UIP)",
            "latex": "\\begin{aligned} i_{\\text{domestik}} & \\approx i_{\\text{asing}} + \\frac{E^e - E}{E} = i_{\\text{asing}} + \\%\\Delta E^e \\\\ 6,5\\% & = 4,0\\% + \\%\\Delta E^e \\implies \\mathbf{\\%\\Delta E^e = 6,5\\% - 4,0\\% = +2,5\\%} \\end{aligned}",
            "legend": "• Tanda positif ($+2,5\\%$) menandakan ekspektasi pelemahan/depresiasi nilai tukar mata uang domestik (Rupiah butuh lebih banyak unit per 1 USD)<br>• Mekanisme UIP: Jika Rupiah tidak terdepresiasi sebesar 2,5%, investor akan melakukan arbitrase tanpa batas"
        },
        "hints": {
            "concept": "Formula UIP: i_dom = i_asing + %Ekspektasi Depresiasi. Selisih suku bunga = 6,5% - 4,0% = 2,5% depresiasi rupiah.",
            "execution": "Pilih: Depresiasi (pelemahan) sebesar 2,5%."
        }
    },
    {
        "id": "eko-lat-h-13",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Rekonsiliasi Bank 4 Kolom dan Koreksi Saldo Kas yang Benar",
        "stem": "Pada tanggal 31 Desember 2024, saldo akun Kas menurut catatan buku besar PT Barata adalah Rp 85.000.000,- sedangkan saldo menurut Rekening Koran Bank adalah Rp 94.000.000,-. Setelah diteliti ditemukan beberapa data penyebab perbedaan:\n1. Setoran dalam perjalanan (_Deposit in Transit_) sebesar Rp 18.000.000,- belum dicatat bank.\n2. Cek yang masih beredar (_Outstanding Checks_) sebesar Rp 19.000.000,- belum diuangkan pemegangnya.\n3. Bank telah menagihkan piutang wesel perusahaan sebesar Rp 12.000.000,- ditambah pendapatan bunga Rp 600.000,- dikurangi biaya penagihan Rp 100.000,- (belum dicatat perusahaan).\n4. Beban administrasi bank Rp 150.000,- dan pendapatan jasa giro bank Rp 650.000,- belum dicatat perusahaan.\n5. Cek pelanggan sebesar Rp 5.000.000,- ditolak bank karena dana tidak cukup (Cek Kosong / _Non-Sufficient Funds_).\nBerdasarkan data rekonsiliasi tersebut, saldo kas yang benar (_Correct Adjusted Cash Balance_) per 31 Desember 2024 adalah...",
        "correct": "Rp 93.000.000,-, di mana saldo menurut rekening koran dan pembukuan perusahaan setelah penyesuaian seimbang tepat pada nilai yang sama.",
        "distractors": [
            "Rp 85.000.000,-, sesuai dengan saldo pembukuan awal kas perusahaan sebelum penyesuaian.",
            "Rp 94.000.000,-, sesuai dengan saldo mutlak rekening koran yang diterbitkan oleh pihak perbankan.",
            "Rp 87.000.000,-, hasil rekonsiliasi sisi bank tanpa memperhitungkan koreksi wesel tagih.",
            "Rp 102.000.000,-, hasil penjumlahan seluruh setoran tanpa mengurangkan cek kosong dan beban administrasi."
        ],
        "formula": {
            "title": "REKONSILIASI SALDO KAS BENAR DUA SISI",
            "latex": "\\begin{aligned} \\mathbf{\\text{Sisi Bank:}} & \\quad 94.000.000 + 18.000.000 \\text{ (DIT)} - 19.000.000 \\text{ (OC)} = \\mathbf{93.000.000} \\\\ \\mathbf{\\text{Sisi Perusahaan:}} & \\quad 85.000.000 + 12.500.000 \\text{ (Wesel Bersih)} + 500.000 \\text{ (Giro Bersih)} - 5.000.000 \\text{ (NSF)} = \\mathbf{93.000.000} \\end{aligned}",
            "legend": "• DIT (Deposit in Transit): Menambah saldo bank<br>• Outstanding Checks: Mengurangi saldo bank<br>• Penerimaan Wesel & Jasa Giro: Menambah saldo buku perusahaan<br>• Cek Kosong (NSF) & Beban Bank: Mengurangi saldo buku perusahaan"
        },
        "hints": {
            "concept": "Sisi bank: Saldo koran + Deposit in transit - Outstanding check = 94 + 18 - 19 = 93 jt. Sisi buku: Saldo buku + Penerimaan wesel bersih + Jasa giro bersih - Cek kosong = 85 + 12,5 + 0,5 - 5 = 93 jt.",
            "execution": "Pilih: Rp 93.000.000,-."
        }
    },
    {
        "id": "eko-lat-h-14",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Penilaian Persediaan FIFO vs Rata-Rata Tertimbang dalam Periode Inflasi",
        "stem": "Dalam periode perekonomian yang sedang mengalami inflasi harga persediaan secara konsisten meningkat, dampak komparatif penggunaan metode First-In, First-Out (FIFO) dibandingkan metode Rata-Rata Tertimbang (Weighted Average) terhadap nilai Persediaan Akhir di Neraca, Harga Pokok Penjualan (HPP), dan Beban Pajak Penghasilan (PPh) perusahaan adalah...",
        "correct": "Metode FIFO menghasilkan nilai Persediaan Akhir lebih tinggi, HPP lebih rendah, laba kotor lebih tinggi, dan konsekuensinya beban pajak penghasilan (PPh) menjadi lebih besar dibandingkan metode Rata-Rata Tertimbang.",
        "distractors": [
            "Metode FIFO menghasilkan nilai Persediaan Akhir lebih rendah dan beban pajak penghasilan yang jauh lebih kecil.",
            "Kedua metode menghasilkan HPP dan laba bersih yang identik karena standar akuntansi IFRS mewajibkan pembulatan nilai wajar.",
            "Metode FIFO menghasilkan HPP lebih tinggi sehingga dividen yang dibagikan kepada pemegang saham menjadi berkurang.",
            "Metode Weighted Average menghasilkan nilai laba kotor tertinggi karena menggunakan harga pembelian paling mutakhir."
        ],
        "formula": {
            "title": "KOMPARASI METODE PERSEDIAAN SAAT TREN HARGA NAIK (INFLASI)",
            "latex": "\\begin{array}{|l|c|c|} \\hline \\text{Indikator Keuangan} & \\text{FIFO (First-In, First-Out)} & \\text{Weighted Average} \\\\ \\hline \\text{Harga Pokok Penjualan (HPP)} & \\mathbf{\\text{Lebih Rendah (Ambil stok lama murah)}} & \\text{Sedang} \\\\ \\text{Laba Kotor \\& Laba Bersih} & \\mathbf{\\text{Lebih Tinggi}} & \\text{Sedang} \\\\ \\text{Nilai Persediaan Akhir} & \\mathbf{\\text{Lebih Tinggi (Tersisa stok baru mahal)}} & \\text{Sedang} \\\\ \\text{Beban Pajak Penghasilan (PPh)} & \\mathbf{\\text{Lebih Besar (Karena Laba Tinggi)}} & \\text{Lebih Rendah} \\\\ \\hline \\end{array}",
            "legend": "• FIFO mencerminkan arus fisik barang aktual dan menyajikan nilai persediaan di neraca mendekati harga pasar terkini"
        },
        "hints": {
            "concept": "Saat harga naik: FIFO mengeluarkan barang lama yang murah untuk HPP -> HPP rendah -> Laba tinggi -> Pajak tinggi -> Nilai stok akhir tinggi (barang baru yang mahal).",
            "execution": "Pilih opsi: Nilai Persediaan Akhir lebih tinggi, HPP lebih rendah, dan beban pajak penghasilan lebih besar."
        }
    },
    {
        "id": "eko-lat-h-15",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Amortisasi Diskonto Obligasi Menggunakan Metode Bunga Efektif",
        "stem": "Pada tanggal 1 Januari 2024, PT Megantara menerbitkan obligasi 5 tahun bernilai nominal Rp 100.000.000,- dengan suku bunga kupon tahunan $8\\%$ yang dibayarkan setiap tanggal 31 Desember. Pada saat diterbitkan, suku bunga pasar efektif adalah $10\\%$, sehingga obligasi diterbitkan pada harga diskonto Rp 92.418.000,-. Beban bunga obligasi (_Interest Expense_) yang diakui pada Laporan Laba Rugi untuk tahun pertama yang berakhir pada 31 Desember 2024 menggunakan metode bunga efektif adalah...",
        "correct": "Rp 9.241.800,-, terdiri atas pembayaran kupon tunai Rp 8.000.000,- dan amortisasi diskonto obligasi penambah nilai tercatat sebesar Rp 1.241.800,-.",
        "distractors": [
            "Rp 8.000.000,-, tepat sebesar kas bunga kupon nominal yang dibayarkan kepada investor obligasi.",
            "Rp 10.000.000,-, hasil perkalian suku bunga efektif pasar dengan nilai nominal penuh obligasi.",
            "Rp 1.516.400,-, hasil pembagian garis lurus total diskonto obligasi selama lima tahun masa edar.",
            "Rp 8.758.200,-, hasil pengurangan nilai kupon kas dengan selisih diskonto periode berjalan."
        ],
        "formula": {
            "title": "AMORTISASI METODE BUNGA EFEKTIF (EFFECTIVE INTEREST METHOD)",
            "latex": "\\begin{aligned} \\text{Kas Kupon Dibayar} & = \\text{Nominal} \\times \\text{Bunga Kupon} = 100.000.000 \\times 8\\% = \\mathbf{8.000.000} \\\\ \\mathbf{\\text{Beban Bunga Efektif}} & = \\text{Nilai Tercatat Awal} \\times \\text{Bunga Pasar} \\\\ & = 92.418.000 \\times 10\\% = \\mathbf{9.241.800} \\\\ \\text{Amortisasi Diskonto} & = \\text{Beban Bunga} - \\text{Kas Kupon} = 9.241.800 - 8.000.000 = \\mathbf{1.241.800} \\\\ \\text{Nilai Buku Baru (31 Des)} & = 92.418.000 + 1.241.800 = 93.659.800 \\end{aligned}",
            "legend": "• Nilai tercatat obligasi berdiskonto akan terus merangkak naik setiap tahun hingga mencapai nilai nominal Rp 100 Juta saat jatuh tempo"
        },
        "hints": {
            "concept": "Beban bunga efektif = Nilai tercatat awal obligasi x Suku bunga pasar = 92.418.000 x 10% = 9.241.800. Kas kupon = 8% x 100 jt = 8.000.000.",
            "execution": "Pilih: Rp 9.241.800,-."
        }
    },
    {
        "id": "eko-lat-h-16",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Teori Upah Efisiensi (Efficiency Wage Theory) dan Kekakuan Upah Riil",
        "stem": "Dalam ilmu makroekonomi modern, Teori Upah Efisiensi (Efficiency Wage Theory) menjelaskan mengapa upah riil di pasar tenaga kerja cenderung bertahan kaku di atas tingkat kliring keseimbangan pasar bebas ($w > w_{\\text{ekuilibrium}}$) meskipun terdapat banyak pengangguran yang bersedia bekerja dengan upah lebih rendah. Rasionalitas ekonomi yang melandasi keputusan pengusaha membayar upah di atas ekuilibrium adalah...",
        "correct": "Tingkat upah yang tinggi memacu produktivitas pekerja, mengurangi tingkat perputaran tenaga kerja (_labor turnover_), menekan biaya rekrutmen dan pelatihan, memitigasi risiko kelalaian kerja (_shirking_), serta menarik pelamar kerja berkualitas tinggi (mengatasi _adverse selection_).",
        "distractors": [
            "Pengusaha diwajibkan oleh undang-undang antimonopoli internasional untuk membagi seluruh dividen kepada buruh harian.",
            "Serikat buruh menggunakan ancaman boikot fisik sehingga mekanika penawaran tenaga kerja tidak berlaku sama sekali.",
            "Pemerintah memberikan subsidi tunai langsung kepada pengusaha sebesar selisih upah minimum dan upah pasar.",
            "Tingkat inflasi yang tinggi secara otomatis melipatgandakan daya beli riil upah tanpa campur tangan manajemen."
        ],
        "formula": {
            "title": "RASIONALITAS TEORI UPAH EFISIENSI (SHAPIRO-STIGLITZ MODEL)",
            "latex": "\\text{Upah Efisiensi } (w^*) \\implies \\begin{cases} \\text{Worker Effort} \\uparrow & \\implies \\text{Pekerja enggan lalai karena takut kehilangan upah tinggi} \\\\ \\text{Labor Turnover} \\downarrow & \\implies \\text{Menghemat biaya penarikan \\& orientasi karyawan baru} \\\\ \\text{Worker Health} \\uparrow & \\implies \\text{Nutrisi dan kebugaran buruh meningkat} \\\\ \\text{Selection Bias} \\downarrow & \\implies \\text{Hanya talenta berkemampuan terbaik yang melamar} \\end{cases}",
            "legend": "• Implikasi Makro: Upah riil tidak turun ke titik kliring pasar, menciptakan Pengangguran Riil Struktural permanen"
        },
        "hints": {
            "concept": "Upah efisiensi: perusahaan membayar di atas pasar untuk meningkatkan produktivitas, mengurangi perputaran kerja, mencegah shirking, dan menarik pekerja terbaik.",
            "execution": "Pilih opsi: Tingkat upah tinggi memacu produktivitas, menekan labor turnover, memitigasi kelalaian, dan menarik pelamar berkualitas."
        }
    },
    {
        "id": "eko-lat-h-17",
        "materi": "STRUKTUR PASAR",
        "topic": "Teori Permainan (Game Theory) dan Keseimbangan Nash Dilema Tahanan Oligopoli",
        "stem": "Dua perusahaan penyedia layanan telekomunikasi (Alpha dan Beta) menghadapi matriks imbalan (payoff) laba bersih tahunan (dalam Miliar Rupiah) berdasarkan strategi penetapan harga:\n- Alpha Harga Tinggi, Beta Harga Tinggi: (100, 100)\n- Alpha Harga Rendah, Beta Harga Tinggi: (140, 30)\n- Alpha Harga Tinggi, Beta Harga Rendah: (30, 140)\n- Alpha Harga Rendah, Beta Harga Rendah: (60, 60)\nJika kedua perusahaan tidak diperkenankan melakukan kolusi resmi (kartel dilarang oleh KPPU), strategi dominan masing-masing perusahaan dan Keseimbangan Nash (Nash Equilibrium) yang terbentuk adalah...",
        "correct": "Kedua perusahaan memiliki strategi dominan memilih Harga Rendah, dan Keseimbangan Nash tercapai pada kondisi (Harga Rendah, Harga Rendah) dengan laba masing-masing sebesar Rp 60 Miliar, mencerminkan fenomena Dilema Tahanan (_Prisoner's Dilemma_).",
        "distractors": [
            "Kedua perusahaan memilih Harga Tinggi secara diam-diam sehingga Keseimbangan Nash menghasilkan laba optimal Rp 100 Miliar.",
            "Perusahaan Alpha memilih Harga Rendah sedangkan Beta memilih Harga Tinggi sehingga Keseimbangan Nash tidak pernah stabil.",
            "Tidak ada strategi dominan bagi kedua perusahaan sehingga keseimbangan hanya dapat dicapai melalui undian probabilitas acak.",
            "Keseimbangan Nash tercapai saat kedua perusahaan menghentikan perang tarif dan menyerahkan pangsa pasar kepada BUMN."
        ],
        "formula": {
            "title": "IDENTIFIKASI KESEIMBANGAN NASH DILEMA TAHANAN",
            "latex": "\\begin{aligned} \\text{Jika Beta Harga Tinggi:} & \\quad \\text{Alpha pilih Rendah (140 > 100)} \\\\ \\text{Jika Beta Harga Rendah:} & \\quad \\text{Alpha pilih Rendah (60 > 30)} \\implies \\mathbf{\\text{Strategi Dominan Alpha: Rendah}} \\\\ \\text{Secara Simetris:} & \\quad \\mathbf{\\text{Strategi Dominan Beta: Rendah}} \\\\ \\mathbf{\\text{Keseimbangan Nash:}} & \\quad \\mathbf{(\\text{Rendah}, \\text{Rendah}) \\implies (60, 60)} \\end{aligned}",
            "legend": "• Sub-Optimalitas Sosial: Titik ekuilibrium non-kooperatif (60, 60) lebih buruk bagi kedua belah pihak dibanding hasil kerja sama kooperatif (100, 100)"
        },
        "hints": {
            "concept": "Cari respon terbaik untuk tiap kemungkinan langkah lawan. Keduanya punya strategi dominan memilih Harga Rendah, menghasilkan Nash Equilibrium (Rendah, Rendah) dengan laba (60, 60).",
            "execution": "Pilih: Kedua perusahaan memilih Harga Rendah, Nash Equilibrium (Rendah, Rendah) laba Rp 60 Miliar."
        }
    },
    {
        "id": "eko-lat-h-18",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Kegagalan Pasar Akibat Asimetri Informasi: Adverse Selection vs Moral Hazard",
        "stem": "Dalam ekonomi informasi (Information Economics), asimetri informasi antara pihak yang bertransaksi dapat menimbulkan kegagalan pasar melalui dua fenomena utama: _Adverse Selection_ dan _Moral Hazard_. Perbedaan fundamental antara kedua fenomena tersebut ditinjau dari dimensi waktu terjadinya kesepakatan kontrak adalah...",
        "correct": "_Adverse Selection_ terjadi SEBELUM kontrak ditandatangani (_hidden characteristics_), di mana pembeli/penjual memiliki informasi privat tersembunyi mengenai kualitas barang atau profil risiko; sedangkan _Moral Hazard_ terjadi SETELAH kontrak disepakati (_hidden action_), di mana perilaku pihak yang diasuransikan berubah menjadi lebih ceroboh karena risikonya ditanggung pihak lain.",
        "distractors": [
            "_Adverse Selection_ terjadi setelah klaim asuransi cair, sedangkan _Moral Hazard_ terjadi saat pendaftaran polis pertama kali.",
            "_Adverse Selection_ hanya dialami oleh lembaga perbankan negara, sedangkan _Moral Hazard_ murni fenomena di pasar modal swasta.",
            "_Adverse Selection_ terjadi saat suku bunga acuan dipangkas, sedangkan _Moral Hazard_ terjadi saat bank sentral menaikkan giro wajib minimum.",
            "Kedua fenomena terjadi serentak sebelum penandatanganan akad dan hanya dapat diatasi dengan pembubaran perusahaan asuransi."
        ],
        "formula": {
            "title": "TAKSONOMI ASIMETRI INFORMASI (GEORGE AKERLOF & JOSEPH STIGLITZ)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Adverse Selection (Pra-Kontrak):}} & \\quad \\text{Informasi Tersembunyi (Hidden Information)} \\\\ & \\implies \\text{Barang berkualitas buruk mendesak keluar barang bagus (Pasar Lemon)} \\\\ \\mathbf{\\text{Moral Hazard (Pasca-Kontrak):}} & \\quad \\text{Tindakan Tersembunyi (Hidden Action)} \\\\ & \\implies \\text{Perilaku berisiko meningkat setelah terlindungi jaminan/asuransi} \\end{aligned}",
            "legend": "• Solusi Adverse Selection: Screening (Penyaringan oleh pihak tak berinformasi) & Signaling (Pemberian sinyal kualitas oleh pemilik informasi seperti garansi/ijazah)<br>• Solusi Moral Hazard: Deductible (pembagian risiko beban sendiri), co-payment, dan pemantauan berkala"
        },
        "hints": {
            "concept": "Adverse Selection = sebelum transaksi (hidden information/characteristics), Moral Hazard = setelah transaksi/kontrak (hidden action/perilaku ceroboh).",
            "execution": "Pilih opsi: Adverse Selection sebelum kontrak (hidden characteristics), Moral Hazard setelah kontrak disepakati (hidden action)."
        }
    },
    {
        "id": "eko-lat-h-19",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Teorema Angka Pengganda Anggaran Berimbang (Balanced Budget Multiplier)",
        "stem": "Pemerintah memutuskan untuk meningkatkan belanja pengeluaran barang dan jasa publik sebesar $\\Delta G = \\text{Rp } 100 \\text{ Triliun}$ untuk program perbaikan sanitasi nasional. Pada saat yang bersamaan, pemerintah menaikkan penerimaan pajak lump-sum sebesar $\\Delta T = \\text{Rp } 100 \\text{ Triliun}$ sehingga anggaran negara tetap berimbang (defisit anggaran nol, $\\Delta G = \\Delta T$). Jika kecenderungan mengonsumsi marjinal masyarakat adalah $MPC = 0,75$, dampak akhir kebijakan tersebut terhadap pendapatan nasional keseimbangan ($\\Delta Y$) adalah...",
        "correct": "Pendapatan nasional bertambah tepat sebesar $\\Delta Y = \\text{Rp } 100 \\text{ Triliun}$, karena nilai angka pengganda anggaran berimbang (_Balanced Budget Multiplier_) selalu bernilai tepat sama dengan satu ($k_{bb} = 1$).",
        "distractors": [
            "Pendapatan nasional tidak berubah sama sekali ($\\Delta Y = 0$) karena kenaikan belanja negara dihapus tuntas oleh kenaikan pajak.",
            "Pendapatan nasional meningkat sebesar $\\Delta Y = \\text{Rp } 400 \\text{ Triliun}$, mengikuti multiplier belanja pemerintah murni.",
            "Pendapatan nasional justru merosot sebesar $\\Delta Y = -\\text{Rp } 100 \\text{ Triliun}$ akibat kontraksi konsumsi masyarakat berpendapatan rendah.",
            "Pendapatan nasional meningkat sebesar $\\Delta Y = \\text{Rp } 75 \\text{ Triliun}$, tepat sebesar proporsi koefisien MPC belanja."
        ],
        "formula": {
            "title": "PENURUNAN MULTIPLIER ANGGARAN BERIMBANG (BALANCED BUDGET MULTIPLIER)",
            "latex": "\\begin{aligned} \\Delta Y & = k_G \\cdot \\Delta G + k_T \\cdot \\Delta T \\\\ & = \\left( \\frac{1}{1 - MPC} \\right) \\Delta G + \\left( \\frac{-MPC}{1 - MPC} \\right) \\Delta T \\\\ \\text{Karena } \\Delta G = \\Delta T: & \\quad \\Delta Y = \\left( \\frac{1 - MPC}{1 - MPC} \\right) \\Delta G = 1 \\cdot \\Delta G \\implies \\mathbf{k_{bb} = 1} \\\\ \\mathbf{\\Delta Y} & = 1 \\times 100 \\text{ Triliun} = \\mathbf{100 \\text{ Triliun}} \\end{aligned}",
            "legend": "• Mengapa k = 1? Karena seluruh belanja pemerintah Rp 100 T langsung menjadi pendapatan masyarakat pada putaran pertama, sedangkan kenaikan pajak Rp 100 T hanya memotong konsumsi sebesar MPC x Rp 100 T (Rp 75 T), sisanya memotong tabungan yang merupakan kebocoran (leakage)"
        },
        "hints": {
            "concept": "Teorema Balanced Budget Multiplier: k_bb = k_G + k_T = 1/(1-MPC) - MPC/(1-MPC) = (1-MPC)/(1-MPC) = 1. Jadi Delta Y = 1 x Delta G = 100 Triliun.",
            "execution": "Pilih: Pendapatan nasional bertambah tepat sebesar Rp 100 Triliun (k_bb = 1)."
        }
    },
    {
        "id": "eko-lat-h-20",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Kurva Phillips Ekspektasi dan Tingkat Pengangguran Alami (NAIRU)",
        "stem": "Dalam teori makroekonomi aliran Monetaris dan Ekspektasi Rasional (Milton Friedman dan Edmund Phelps), Kurva Phillips yang menggambarkan hubungan antara tingkat inflasi dan tingkat pengangguran dalam jangka panjang (Long-Run Phillips Curve / LRPC) berbentuk...",
        "correct": "Garis lurus vertikal sempurna tepat pada Tingkat Pengangguran Alami (Non-Accelerating Inflation Rate of Unemployment / NAIRU), yang menegaskan bahwa dalam jangka panjang tidak ada pertukaran (_trade-off_) permanen antara inflasi dan pengangguran.",
        "distractors": [
            "Kurva melengkung menurun dari kiri atas ke kanan bawah secara permanen di segala horizon waktu.",
            "Garis lurus horizontal sempurna pada tingkat suku bunga netral bank sentral.",
            "Kurva berbentuk huruf U terbalik di mana inflasi tinggi selalu berhasil menghapus seluruh pengangguran terbuka.",
            "Garis diagonal positif bergerak selaras dengan laju pertumbuhan Produk Domestik Bruto riil."
        ],
        "formula": {
            "title": "KURVA PHILLIPS DENGAN EXPECTATIONS-AUGMENTED",
            "latex": "\\begin{aligned} \\pi & = \\pi^e - \\beta(u - u_n) + v \\\\ \\text{Jangka Pendek (SR):} & \\quad \\pi^e \\text{ kaku} \\implies \\text{Ada Trade-off antara } \\pi \\text{ dan } u \\\\ \\text{Jangka Panjang (LR):} & \\quad \\pi^e = \\pi \\implies 0 = -\\beta(u - u_n) \\implies \\mathbf{u = u_n \\text{ (NAIRU Vertikal)}} \\end{aligned}",
            "legend": "• $u_n$: Natural Rate of Unemployment (NAIRU)<br>• Usaha pemerintah memacu stimulus moneter untuk menekan $u < u_n$ dalam jangka panjang hanya akan memicu akselerasi inflasi spiral tanpa menurunkan pengangguran"
        },
        "hints": {
            "concept": "Jangka panjang Kurva Phillips berbentuk vertikal di tingkat pengangguran alami (NAIRU). Tidak ada trade-off permanen antara inflasi dan pengangguran.",
            "execution": "Pilih: Garis lurus vertikal sempurna pada tingkat pengangguran alami (NAIRU)."
        }
    },
    {
        "id": "eko-lat-h-21",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Akuntansi Persekutuan Firma: Pembagian Laba Bersih Multi-Kriteria",
        "stem": "Firma \"Bintang Tiga\" beranggotakan Sekutu Arya dan Sekutu Bayu dengan modal awal masing-masing Rp 60.000.000,- dan Rp 40.000.000,-. Perjanjian persekutuan menetapkan pembagian laba bersih tahunan berdasarkan ketentuan:\n1. Bunga modal diberikan sebesar $10\\%$ per tahun atas modal awal masing-masing sekutu.\n2. Tunjangan gaji tahunan untuk Sekutu Arya (aktif mengelola firma) sebesar Rp 20.000.000,-.\n3. Sisa laba/rugi dibagi rata ($50\\% : 50\\%$) antara kedua sekutu.\nJika selama tahun 2024 firma memperoleh laba bersih sebesar Rp 40.000.000,-, bagian laba bersih akhir yang diterima oleh Sekutu Arya dan Sekutu Bayu adalah...",
        "correct": "Sekutu Arya menerima Rp 31.000.000,- dan Sekutu Bayu menerima Rp 9.000.000,-.",
        "distractors": [
            "Sekutu Arya menerima Rp 24.000.000,- dan Sekutu Bayu menerima Rp 16.000.000,-.",
            "Sekutu Arya menerima Rp 20.000.000,- dan Sekutu Bayu menerima Rp 20.000.000,-.",
            "Sekutu Arya menerima Rp 26.000.000,- dan Sekutu Bayu menerima Rp 14.000.000,-.",
            "Sekutu Arya menerima Rp 35.000.000,- dan Sekutu Bayu menerima Rp 5.000.000,-."
        ],
        "formula": {
            "title": "KALKULASI ALOKASI LABA BERSIH PERSEKUTUAN FIRMA",
            "latex": "\\begin{aligned} \\text{Total Laba Bersih} & = \\text{Rp } 40.000.000 \\\\ \\text{Bunga Modal (10\\%):} & \\quad \\text{Arya} = 6.000.000; \\quad \\text{Bayu} = 4.000.000 \\quad (\\text{Total } = 10.000.000) \\\\ \\text{Tunjangan Gaji:} & \\quad \\text{Arya} = 20.000.000 \\quad (\\text{Total } = 20.000.000) \\\\ \\text{Sisa Laba Dibagi Rata:} & \\quad 40.000.000 - (10.000.000 + 20.000.000) = \\mathbf{10.000.000} \\\\ \\text{Alokasi Sisa (50\\% : 50\\%):} & \\quad \\text{Arya} = 5.000.000; \\quad \\text{Bayu} = 5.000.000 \\\\ \\mathbf{\\text{Total Laba Arya:}} & \\quad 6.000.000 + 20.000.000 + 5.000.000 = \\mathbf{31.000.000} \\\\ \\mathbf{\\text{Total Laba Bayu:}} & \\quad 4.000.000 + 5.000.000 = \\mathbf{9.000.000} \\end{aligned}",
            "legend": "• Cek Total: Rp 31 Juta + Rp 9 Juta = Rp 40 Juta (Sesuai laba bersih)"
        },
        "hints": {
            "concept": "Hitung bunga modal: Arya = 10% x 60 jt = 6 jt, Bayu = 10% x 40 jt = 4 jt. Gaji: Arya = 20 jt. Sisa laba = 40 jt - (6+4+20) jt = 10 jt. Sisa dibagi 50:50 = 5 jt tiap sekutu.",
            "execution": "Arya = 6 + 20 + 5 = 31 jt. Bayu = 4 + 5 = 9 jt. Total = 40 jt."
        }
    },
    {
        "id": "eko-lat-h-22",
        "materi": "BADAN USAHA & KOPERASI",
        "topic": "Penganggaran Modal (Capital Budgeting): Analisis Kelayakan Proyek NPV",
        "stem": "Sebuah BUMN merencanakan proyek investasi instalasi pembangkit listrik tenaga surya (PLTS) dengan pengeluaran modal awal (_Initial Outlay_) sebesar Rp 100 Miliar. Proyek tersebut diproyeksikan menghasilkan arus kas bersih masuk (_Net Cash Inflow_) sebesar Rp 41 Miliar per tahun selama 3 tahun berturut-turut. Jika tingkat diskonto biaya modal perusahaan adalah $k = 10\\%$ per tahun (Faktor Diskonto Kumulatif Anuitas 3 tahun = 2,4869), nilai Net Present Value (NPV) proyek tersebut dan keputusan kelayakannya adalah...",
        "correct": "$\\text{NPV} = +\\text{Rp } 1,9629 \\text{ Miliar}$ (atau $+\\text{Rp } 1.962.900.000,-$), sehingga proyek investasi dinyatakan **Layak Diterima** karena $\\text{NPV} > 0$.",
        "distractors": [
            "$\\text{NPV} = -\\text{Rp } 5,4200 \\text{ Miliar}$, sehingga proyek dinyatakan ditolak karena merugikan keuangan negara.",
            "$\\text{NPV} = +\\text{Rp } 23,0000 \\text{ Miliar}$, dihitung dari akumulasi kas masuk bruto tanpa memperhitungkan faktor nilai waktu uang.",
            "$\\text{NPV} = 0$, sehingga proyek berada dalam posisi titik impas tanpa nilai tambah ekonomi.",
            "$\\text{NPV} = +\\text{Rp } 9,4500 \\text{ Miliar}$, hasil pemotongan diskonto suku bunga majemuk flat lima persen."
        ],
        "formula": {
            "title": "FORMULA NET PRESENT VALUE (NPV) ANUITAS KAS",
            "latex": "\\begin{aligned} PV_{\\text{arus kas}} & = \\text{Arus Kas Tahunan} \\times \\text{PVIFA}_{10\\%, 3} \\\\ & = 41 \\times 2,4869 = \\mathbf{101,9629 \\text{ Miliar}} \\\\ \\mathbf{\\text{NPV}} & = PV_{\\text{arus kas}} - \\text{Investasi Awal} \\\\ & = 101,9629 - 100 = \\mathbf{+1,9629 \\text{ Miliar}} \\end{aligned}",
            "legend": "• Kaidah Keputusan NPV: Jika $NPV > 0$, proyek mampu menghasilkan imbal hasil di atas biaya modal dan menambah nilai ekonomi perusahaan"
        },
        "hints": {
            "concept": "NPV = Total PV Arus Kas Masuk - Investasi Awal. Jika NPV > 0 maka proyek layak diterima.",
            "execution": "Pilih opsi kelayakan: Proyek layak diterima karena NPV bernilai positif."
        }
    },
    {
        "id": "eko-lat-h-23",
        "materi": "LEMBAGA KEUANGAN & PASAR MODAL",
        "topic": "Teori Struktur Modal Modigliani-Miller dengan Pajak Perusahaan",
        "stem": "Berdasarkan Teori Struktur Modal Modigliani-Miller (MM Proposisi I) dengan memperhitungkan adanya Pajak Penghasilan Badan (_Corporate Taxes_), perbandingan nilai perusahaan yang memiliki utang obligasi (_Levered Firm_ / $V_L$) terhadap nilai perusahaan sejenis yang sepenuhnya didanai oleh ekuitas saham murni (_Unlevered Firm_ / $V_U$) adalah...",
        "correct": "$V_L = V_U + T_c \\cdot D$, di mana nilai perusahaan yang berutang lebih tinggi tepat sebesar nilai kini penghematan pajak bunga pinjaman (_Tax Shield of Debt_), karena beban bunga utang dapat mengurangi penghasilan kena pajak perusahaan (_tax deductible_).",
        "distractors": [
            "$V_L = V_U - T_c \\cdot D$, di mana penggunaan utang selalu menurunkan nilai perusahaan akibat ancaman kebangkrutan seketika.",
            "$V_L = V_U$, di mana struktur modal tidak memiliki pengaruh sedikit pun terhadap nilai pasar perusahaan dalam segala kondisi.",
            "$V_L = V_U / (1 - T_c)$, di mana nilai perusahaan berbanding terbalik secara geometris dengan tarif pajak dividen.",
            "$V_L = D \\times (1 + k_e)$, di mana nilai perusahaan ditentukan secara independen oleh ekspektasi pengembalian modal saham."
        ],
        "formula": {
            "title": "TEORI MODIGLIANI-MILLER DENGAN PAJAK BADAN (1963)",
            "latex": "\\begin{aligned} V_L & = V_U + T_c \\cdot D \\\\ \\text{di mana:} & \\quad V_L = \\text{Nilai Perusahaan Berutang (Levered)} \\\\ & \\quad V_U = \\text{Nilai Perusahaan Tanpa Utang (Unlevered)} \\\\ & \\quad T_c = \\text{Tarif Pajak PPh Badan (Corporate Tax Rate)} \\\\ & \\quad D = \\text{Total Nilai Nominal Utang (Debt)} \\\\ & \\quad T_c \\cdot D = \\text{Present Value of Interest Tax Shield} \\end{aligned}",
            "legend": "• Bunga utang bersifat tax-deductible (mengurangi beban pajak laba), sedangkan dividen saham dibayarkan setelah laba dipotong pajak"
        },
        "hints": {
            "concept": "MM dengan pajak: Nilai perusahaan berutang VL = VU + Tc . D karena ada penghematan pajak dari bunga utang (tax shield of debt).",
            "execution": "Pilih: VL = VU + Tc . D (nilai perusahaan lebih tinggi sebesar tax shield of debt)."
        }
    },
    {
        "id": "eko-lat-h-24",
        "materi": "BADAN USAHA & KOPERASI",
        "topic": "Perhitungan Biaya Modal Rata-Rata Tertimbang (WACC)",
        "stem": "PT Nusantara Mandiri memiliki struktur permodalan optimal yang terdiri atas $40\\%$ utang jangka panjang (obligasi) dan $60\\%$ ekuitas saham biasa. Biaya utang sebelum pajak adalah $r_d = 10\\%$, biaya modal saham biasa adalah $r_e = 15\\%$, dan perusahaan dikenakan tarif Pajak Penghasilan Badan sebesar $T_c = 25\\%$. Biaya Modal Rata-Rata Tertimbang (Weighted Average Cost of Capital / WACC) perusahaan tersebut adalah...",
        "correct": "$\\text{WACC} = 12,0\\%$, dihitung dari pembobotan biaya modal setelah pajak: $0,40 \\times 10\\%(1 - 0,25) + 0,60 \\times 15\\% = 0,40(7,5\\%) + 0,60(15\\%) = 3,0\\% + 9,0\\%$.",
        "distractors": [
            "$\\text{WACC} = 13,0\\%$, hasil perhitungan tanpa mengurangkan perisai pajak bunga atas utang.",
            "$\\text{WACC} = 12,5\\%$, hasil pembagian rata aritmatika sederhana antara biaya utang dan saham.",
            "$\\text{WACC} = 10,0\\%$, hasil kesalahan pembobotan yang didominasi oleh instrumen utang komersial.",
            "$\\text{WACC} = 14,25\\%$, hasil penambahan tarif pajak badan ke dalam beban modal saham."
        ],
        "formula": {
            "title": "FORMULA BIAYA MODAL RATA-RATA TERTIMBANG (WACC)",
            "latex": "\\begin{aligned} \\text{WACC} & = w_d \\cdot r_d(1 - T_c) + w_e \\cdot r_e \\\\ & = 0,40 \\times 10\\% \\times (1 - 0,25) + 0,60 \\times 15\\% \\\\ & = 0,40 \\times 7,5\\% + 0,60 \\times 15\\% \\\\ & = 3,0\\% + 9,0\\% = \\mathbf{12,0\\%} \\end{aligned}",
            "legend": "• $w_d, w_e$: Bobot proporsi utang dan ekuitas modal dalam neraca keuangan<br>• $r_d(1 - T_c)$: Biaya utang setelah penyesuaian perisai pajak (_after-tax cost of debt_)"
        },
        "hints": {
            "concept": "WACC = w_d . r_d(1 - T_c) + w_e . r_e. Utang setelah pajak = 10% x (1 - 0,25) = 7,5%. Bobot utang = 0,40 x 7,5% = 3%. Saham = 0,60 x 15% = 9%. Total = 12,0%.",
            "execution": "Pilih: WACC = 12,0%."
        }
    },
    {
        "id": "eko-lat-h-25",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Indeks Pembangunan Manusia (IPM / HDI) Metode Baru BPS-UNDP",
        "stem": "Sejak tahun 2014, Badan Pusat Statistik (BPS) mengadopsi metode baru penghitungan Indeks Pembangunan Manusia (IPM / HDI) sesuai standar UNDP. Tiga dimensi dasar pembentuk IPM metode baru beserta indikator ukuran kompositnya adalah...",
        "correct": "1. Dimensi Kesehatan: Umur Harapan Hidup saat Lahir (UHH);\n2. Dimensi Pendidikan: Harapan Lama Sekolah (HLS) dan Rata-rata Lama Sekolah (RLS);\n3. Dimensi Standar Hidup Layak: Pengeluaran Riil per Kapita yang Disesuaikan (daya beli PPP);\ndengan penggabungan menggunakan rata-rata geometrik.",
        "distractors": [
            "Tingkat pendapatan per kapita nominal, angka kelahiran kasar, dan rasio kepemilikan kendaraan bermotor per rumah tangga.",
            "Tingkat inflasi tahunan, cadangan devisa bank sentral, dan angka melek huruf penduduk dewasa.",
            "Penerimaan pajak daerah, panjang jalan tol beraspal, dan rasio tempat tidur rumah sakit per kapita.",
            "Jumlah universitas terakreditasi unggul, rasio elektrifikasi desa, dan volume ekspor non-migas nasional."
        ],
        "formula": {
            "title": "FORMULASI IPM METODE BARU (BPS-UNDP)",
            "latex": "\\begin{aligned} \\mathbf{\\text{IPM}} & = \\sqrt[3]{I_{\\text{Kesehatan}} \\times I_{\\text{Pendidikan}} \\times I_{\\text{Pengeluaran}}} \\\\ I_{\\text{Pendidikan}} & = \\frac{I_{\\text{HLS}} + I_{\\text{RLS}}}{2} \\\\ \\text{Metode Agregasi:} & \\quad \\text{Rata-rata Geometrik (Menggantikan rata-rata aritmatik lama)} \\end{aligned}",
            "legend": "• Keunggulan Rata-Rata Geometrik: Capaian tinggi pada satu dimensi tidak dapat lagi menutupi secara sempurna capaian rendah pada dimensi lain (mencegah kompensasi semu)"
        },
        "hints": {
            "concept": "Tiga dimensi IPM metode baru: Umur Harapan Hidup (Kesehatan), Harapan Lama Sekolah & Rata-rata Lama Sekolah (Pendidikan), dan Pengeluaran Riil per Kapita Disesuaikan (Standar Hidup Layak) dengan rata-rata geometrik.",
            "execution": "Pilih opsi: UHH (kesehatan), HLS & RLS (pendidikan), dan Pengeluaran riil per kapita disesuaikan (standar hidup layak) via rata-rata geometrik."
        }
    }
]
