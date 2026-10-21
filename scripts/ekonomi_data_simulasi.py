# -*- coding: utf-8 -*-
"""
ekonomi_data_simulasi.py
------------------------
35 Authentic HOTS Simulation Questions for TKA 2026 Ekonomi (SMA/MA Soshum).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: eko-sim-01 .. eko-sim-35
Breakdown:
- 25 Single MCQ HOTS (eko-sim-01 .. eko-sim-25)
- 5 Multi-select HOTS (eko-sim-26 .. eko-sim-30)
- 5 Matrix Benar-Salah HOTS (eko-sim-31 .. eko-sim-35)
"""

EKONOMI_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 SINGLE MCQ HOTS (eko-sim-01 to eko-sim-25)
    # -------------------------------------------------------------
    {
        "id": "eko-sim-01",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Analisis Biaya Peluang Eksplisit dan Implisit Pengusaha",
        "stem": "Seorang manajer senior dengan gaji Rp 30.000.000,- per bulan memutuskan mengundurkan diri untuk membuka usaha kedai kopi sendiri. Ia menggunakan tabungan pribadinya sebesar Rp 200.000.000,- yang sebelumnya memberikan bunga deposito 6% per tahun. Pada tahun pertama, kedai kopi tersebut membukukan pendapatan total Rp 600.000.000,- dengan pengeluaran operasional eksplisit (bahan baku, gaji karyawan, sekeliling sewa) sebesar Rp 220.000.000,-. Besarnya Laba Akuntansi (_Accounting Profit_) dan Laba Ekonomi (_Economic Profit_) usaha kedai kopi tersebut selama tahun pertama adalah...",
        "correct": "Laba Akuntansi sebesar Rp 380.000.000,- dan Laba Ekonomi sebesar Rp 8.000.000,-.",
        "distractors": [
            "Laba Akuntansi sebesar Rp 380.000.000,- dan Laba Ekonomi sebesar Rp 380.000.000,-.",
            "Laba Akuntansi sebesar Rp 220.000.000,- dan Laba Ekonomi sebesar -Rp 152.000.000,- (Rugi Ekonomi).",
            "Laba Akuntansi sebesar Rp 600.000.000,- dan Laba Ekonomi sebesar Rp 228.000.000,-.",
            "Laba Akuntansi sebesar Rp 368.000.000,- dan Laba Ekonomi sebesar Rp 20.000.000,-."
        ],
        "formula": {
            "title": "KOMPARASI LABA AKUNTANSI VS LABA EKONOMI",
            "latex": "\\begin{aligned} \\text{Laba Akuntansi} & = TR - \\text{Biaya Eksplisit} = 600.000.000 - 220.000.000 = \\mathbf{380.000.000} \\\\ \\text{Biaya Implisit} & = \\text{Gaji yang Dilepas (12 } \\times 30 \\text{ Jt)} + \\text{Bunga Deposito (6\\% } \\times 200 \\text{ Jt)} \\\\ & = 360.000.000 + 12.000.000 = \\mathbf{372.000.000} \\\\ \\mathbf{\\text{Laba Ekonomi}} & = \\text{Laba Akuntansi} - \\text{Biaya Implisit} = 380.000.000 - 372.000.000 = \\mathbf{8.000.000} \\end{aligned}",
            "legend": "• Laba Akuntansi murni memperhitungkan aliran kas keluar (biaya eksplisit)<br>• Laba Ekonomi memperhitungkan seluruh biaya peluang (eksplisit + implisit); jika laba ekonomi > 0, keputusan beralih usaha bernilai tambah positif"
        },
        "hints": {
            "concept": "Laba akuntansi = TR - Biaya eksplisit = 600 jt - 220 jt = 380 jt. Biaya implisit = Gaji setahun (360 jt) + Bunga deposito (12 jt) = 372 jt. Laba ekonomi = 380 jt - 372 jt = 8 jt.",
            "execution": "Pilih: Laba Akuntansi Rp 380.000.000,- dan Laba Ekonomi Rp 8.000.000,-."
        }
    },
    {
        "id": "eko-sim-02",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Kalkulasi Koefisien Elastisitas Silang Permintaan (Cross Elasticity)",
        "stem": "Ketika harga gas elpiji tabung 12 kg naik dari Rp 200.000,- menjadi Rp 250.000,- (kenaikan harga $25\\%$), permintaan rumah tangga terhadap kompor listrik induksi melonjak dari 10.000 unit menjadi 15.000 unit per bulan (kenaikan kuantitas $50\\%$). Nilai koefisien elastisitas silang permintaan ($E_c$) kompor listrik terhadap harga gas elpiji serta hubungan ekonomis antara kedua barang tersebut adalah...",
        "correct": "$E_c = +2,0$ (bernilai positif), menunjukkan bahwa kompor listrik induksi dan gas elpiji memiliki hubungan sebagai barang substitusi (saling menggantikan).",
        "distractors": [
            "$E_c = -2,0$ (bernilai negatif), menunjukkan bahwa kedua barang tersebut merupakan barang komplementer (saling melengkapi).",
            "$E_c = +0,5$, menunjukkan bahwa hubungan substitusi antara kedua produk sangat lemah dan mendekati netral.",
            "$E_c = 0$, menunjukkan bahwa kompor listrik dan gas elpiji merupakan barang independen yang tidak berhubungan.",
            "$E_c = -0,5$, menunjukkan bahwa kenaikan harga elpiji memangkas daya beli konsumsi kompor listrik."
        ],
        "formula": {
            "title": "FORMULA KOEFISIEN ELASTISITAS SILANG (CROSS PRICE ELASTICITY)",
            "latex": "\\begin{aligned} E_c & = \\frac{\\%\\Delta Q_{\\text{kompor}}}{\\%\\Delta P_{\\text{gas}}} = \\frac{(15.000 - 10.000)/10.000}{(250.000 - 200.000)/200.000} = \\frac{+50\\%}{+25\\%} = \\mathbf{+2,0} \\\\ E_c > 0 & \\implies \\mathbf{\\text{Barang Substitusi}}, \\quad E_c < 0 \\implies \\text{Barang Komplementer}, \\quad E_c = 0 \\implies \\text{Independen} \\end{aligned}",
            "legend": "• Nilai positif (+2,0) menandakan kenaikan harga gas memicu peralihan konsumen ke kompor listrik"
        },
        "hints": {
            "concept": "Elastisitas silang E_c = %Delta Q / %Delta P = +50% / +25% = +2,0. Tanda positif menandakan barang substitusi.",
            "execution": "Pilih: Ec = +2,0 (positif), barang substitusi."
        }
    },
    {
        "id": "eko-sim-03",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Keseimbangan Pasar Setelah Subsidi Spesifik Pemerintah",
        "stem": "Fungsi permintaan dan penawaran beras premium di pasar lokal adalah:\n- Permintaan: $P = 120 - 2Q$\n- Penawaran: $P = 20 + 3Q$\nPemerintah memberikan subsidi spesifik sebesar $s = \\text{Rp } 10,-$ per kg beras kepada para petani produsen. Tingkat harga ($P_s$) dan kuantitas ($Q_s$) keseimbangan pasar setelah subsidi, serta total pengeluaran subsidi yang ditanggung kas pemerintah adalah...",
        "correct": "$Q_s = 22$ unit, $P_s = \\text{Rp } 76,-$, dan total pengeluaran subsidi pemerintah adalah Rp 220,-.",
        "distractors": [
            "$Q_s = 20$ unit, $P_s = \\text{Rp } 80,-$, dan total pengeluaran subsidi pemerintah adalah Rp 200,-.",
            "$Q_s = 25$ unit, $P_s = \\text{Rp } 70,-$, dan total pengeluaran subsidi pemerintah adalah Rp 250,-.",
            "$Q_s = 18$ unit, $P_s = \\text{Rp } 84,-$, dan total pengeluaran subsidi pemerintah adalah Rp 180,-.",
            "$Q_s = 24$ unit, $P_s = \\text{Rp } 72,-$, dan total pengeluaran subsidi pemerintah adalah Rp 240,-."
        ],
        "formula": {
            "title": "EVALUASI KESEIMBANGAN PASAR SETELAH SUBSIDI",
            "latex": "\\begin{aligned} \\text{Ekuilibrium Awal:} & \\quad 120 - 2Q = 20 + 3Q \\implies 5Q = 100 \\implies Q_0 = 20, \\ P_0 = 80 \\\\ \\text{Penawaran Baru:} & \\quad P_s' = 20 + 3Q - 10 = 10 + 3Q \\\\ \\text{Ekuilibrium Subsidi:} & \\quad 120 - 2Q = 10 + 3Q \\implies 5Q = 110 \\implies \\mathbf{Q_s = 22} \\\\ \\mathbf{P_s} & = 120 - 2(22) = 120 - 44 = \\mathbf{76} \\\\ \\mathbf{\\text{Total Subsidi}} & = s \\times Q_s = 10 \\times 22 = \\mathbf{220} \\end{aligned}",
            "legend": "• Subsidi menurunkan harga beli konsumen ($P_s < P_0$) dan menaikkan kuantitas barang yang diperdagangkan ($Q_s > Q_0$)"
        },
        "hints": {
            "concept": "Fungsi penawaran baru setelah subsidi: Ps' = Ps - s = (20 + 3Q) - 10 = 10 + 3Q. Samakan dengan permintaan Pd = 120 - 2Q.",
            "execution": "120 - 2Q = 10 + 3Q -> 5Q = 110 -> Qs = 22. Ps = 120 - 2(22) = 76. Total Subsidi = 10 * 22 = 220."
        }
    },
    {
        "id": "eko-sim-04",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Penurunan Kurva Konsumsi Pendapatan (ICC) dan Kurva Engel",
        "stem": "Dalam analisis perilaku konsumen pendekatan ordinal, jika pendapatan nominal konsumen ($I$) terus ditingkatkan sementara harga barang $X$ dan $Y$ tetap, titik-titik keseimbangan kepuasan maksimum yang baru akan dihubungkan membentuk sebuah kurva. Kurva yang menghubungkan titik-titik persinggungan antara kurva indiferensi dan garis anggaran akibat perubahan pendapatan tersebut dikenal sebagai...",
        "correct": "Kurva Konsumsi Pendapatan (Income Consumption Curve / ICC), yang jika ditransformasikan ke diagram hubungan antara tingkat pendapatan dan jumlah pembelian barang $X$ akan menghasilkan Kurva Engel.",
        "distractors": [
            "Kurva Konsumsi Harga (Price Consumption Curve / PCC), yang kemudian diturunkan menjadi Kurva Permintaan Individu.",
            "Kurva Kemungkinan Produksi (PPF), yang menunjukkan batas pertukaran teknologi dan sumber daya fisik.",
            "Kurva Isocost, yang menggambarkan kombinasi anggaran biaya faktor produksi modal dan tenaga kerja.",
            "Kurva Batas Kemakmuran Sosial (Social Welfare Function), yang menghubungkan titik-titik pareto optimal."
        ],
        "formula": {
            "title": "HUBUNGAN KURVA ICC DAN KURVA ENGEL",
            "latex": "\\begin{aligned} \\text{Pergeseran Garis Anggaran (Pendapatan } I \\uparrow) & \\implies \\text{Lokus Keseimbangan Baru} \\equiv \\mathbf{\\text{ICC (Income Consumption Curve)}} \\\\ \\text{Transformasi Diagram } (Y \\to I): & \\quad \\mathbf{\\text{Kurva Engel}} \\implies \\begin{cases} \\text{Kemiringan Positif } (\\Delta Q / \\Delta I > 0): & \\text{Barang Normal} \\\\ \\text{Kemiringan Negatif } (\\Delta Q / \\Delta I < 0): & \\text{Barang Inferior} \\end{cases} \\end{aligned}",
            "legend": "• PCC (Price Consumption Curve) diturunkan dari perubahan harga ($P$), menghasilkan Kurva Permintaan<br>• ICC diturunkan dari perubahan pendapatan ($I$), menghasilkan Kurva Engel"
        },
        "hints": {
            "concept": "Kurva yang menghubungkan titik keseimbangan saat pendapatan berubah adalah ICC (Income Consumption Curve), yang ditransformasikan menjadi Kurva Engel.",
            "execution": "Pilih: Kurva Konsumsi Pendapatan (Income Consumption Curve / ICC) dan Kurva Engel."
        }
    },
    {
        "id": "eko-sim-05",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Tiga Tahap Fungsi Produksi Klasik (The Law of Diminishing Returns)",
        "stem": "Dalam teori produksi satu input variabel tenaga kerja ($L$), kurva Produksi Total ($TP$), Produksi Rata-rata ($AP$), dan Produksi Marjinal ($MP$) membagi proses produksi ke dalam Tiga Tahap Produksi. Produsen rasional akan memilih beroperasi pada tahap...",
        "correct": "Tahap II (Tahap Rasional), yang dimulai dari titik saat $AP$ mencapai nilai maksimum ($MP = AP$) hingga saat $MP = 0$ (saat $TP$ mencapai nilai maksimum), di mana elastisitas output berada pada rentang $0 \\le E_p \\le 1$.",
        "distractors": [
            "Tahap I (Tahap Irasional), karena pada tahap ini nilai produksi marjinal $MP$ masih terus mengalami kenaikan tajam di atas nilai rata-rata.",
            "Tahap III (Tahap Irasional), karena penambahan tenaga kerja telah menghasilkan nilai $MP$ negatif yang menghemat beban upah buruh.",
            "Tepat pada titik awal saat jumlah tenaga kerja pertama kali dimasukkan ke dalam pabrik tanpa modal pendamping.",
            "Tahap di mana kurva AP bernilai negatif dan kurva TP berbentuk garis lurus vertikal sejajar sumbu tegak."
        ],
        "formula": {
            "title": "KARAKTERISTIK TIGA TAHAP PRODUKSI FUNGSI VARIABEL",
            "latex": "\\begin{array}{|l|c|c|l|} \\hline \\text{Tahap} & \\text{Batas Input } L & \\text{Sifat Marjinal } MP & \\text{Keterangan Ekonomi} \\\\ \\hline \\text{Tahap I} & 0 \\le L < L(AP_{\\max}) & MP > AP, \\ E_p > 1 & \\text{Irasional (Kapasitas mesin belum optimal)} \\\\ \\mathbf{\\text{Tahap II}} & \\mathbf{AP_{\\max} \\le L \\le TP_{\\max}} & \\mathbf{0 \\le MP \\le AP, \\ 0 \\le E_p \\le 1} & \\mathbf{\\text{Rasional (Area Operasi Produsen)}} \\\\ \\text{Tahap III} & L > L(TP_{\\max}) & MP < 0, \\ E_p < 0 & \\text{Irasional (Kelebihan buruh, TP turun)} \\\\ \\hline \\end{array}",
            "legend": "• Pada Tahap II, produsen menyeimbangkan pemanfaatan modal tetap dan efisiensi penambahan tenaga kerja variabel"
        },
        "hints": {
            "concept": "Produsen rasional selalu beroperasi di Tahap II (dari AP maks / MP=AP sampai TP maks / MP=0, di mana 0 <= Ep <= 1).",
            "execution": "Pilih: Tahap II (Tahap Rasional), dari AP maksimum (MP = AP) hingga MP = 0 (TP maksimum)."
        }
    },
    {
        "id": "eko-sim-06",
        "materi": "STRUKTUR PASAR",
        "topic": "Titik Tutup Usaha (Shut-Down Point) Perusahaan Persaingan Sempurna",
        "stem": "Dalam jangka pendek, sebuah perusahaan di pasar persaingan sempurna tetap rasional untuk melanjutkan aktivitas produksinya meskipun sedang mengalami kerugian finansial, selama tingkat harga pasar ($P$) memenuhi kondisi...",
        "correct": "$P \\ge AVC_{\\min}$ (harga pasar masih mampu menutup seluruh Biaya Variabel Rata-rata minimum), sehingga pendapatan penjualan masih dapat memberikan kontribusi untuk menutup sebagian Biaya Tetap ($FC$).",
        "distractors": [
            "$P < AVC_{\\min}$, karena perusahaan dapat meminjam dana darurat kepada bank tanpa batas waktu.",
            "$P = ATC_{\\min}$, di mana perusahaan memperoleh laba supernormal sepuluh persen di atas biaya total.",
            "$P = MC$ pada saat kurva biaya marjinal berada tepat di bawah titik nol absolut.",
            "$P < AFC$, karena biaya tetap tidak perlu dibayar jika perusahaan beroperasi di bawah kapasitas normal."
        ],
        "formula": {
            "title": "KRITERIA KEPUTUSAN OPERASIONAL JANGKA PENDEK",
            "latex": "\\begin{cases} P > ATC_{\\min} & \\implies \\text{Laba Supernormal (Economic Profit > 0)} \\\\ P = ATC_{\\min} & \\implies \\text{Titik Impas (Break-Even Point, Laba Normal)} \\\\ AVC_{\\min} \\le P < ATC_{\\min} & \\implies \\mathbf{\\text{Rugi, tapi Terus Beroperasi (Tutup Sebagian FC)}} \\\\ \\mathbf{P < AVC_{\\min}} & \\implies \\mathbf{\\text{Tutup Usaha Seketika (Shut-Down Point)}} \\end{cases}",
            "legend": "• Jika tutup saat $P < AVC$, kerugian perusahaan hanya sebesar $FC$<br>• Jika memaksakan operasi saat $P < AVC$, kerugian perusahaan $= FC + \\text{sebagian } VC$ (lebih besar dari modal tetap!)"
        },
        "hints": {
            "concept": "Perusahaan tetap beroperasi jangka pendek meski rugi asalkan harga P masih di atas AVC minimum (P >= AVC_min). Titik P = AVC_min adalah Titik Tutup Usaha (Shut-down Point).",
            "execution": "Pilih opsi: P >= AVC_min (harga masih menutup seluruh Biaya Variabel Rata-rata minimum)."
        }
    },
    {
        "id": "eko-sim-07",
        "materi": "STRUKTUR PASAR",
        "topic": "Pengukuran Derajat Kekuatan Monopoli dengan Indeks Lerner",
        "stem": "Sebuah perusahaan manufaktur obat mematok harga jual produk patennya sebesar $P = \\text{Rp } 100.000,-$ per botol dengan biaya marjinal produksi konstan sebesar $MC = \\text{Rp } 25.000,-$. Berdasarkan Indeks Lerner ($L = \\frac{P - MC}{P}$), derajat kekuatan monopoli perusahaan tersebut serta elastisitas harga permintaannya adalah...",
        "correct": "$L = 0,75$ (menunjukkan kekuatan monopoli yang sangat tinggi), dengan elastisitas harga permintaan $|E_d| = 1,33$.",
        "distractors": [
            "$L = 0,25$, dengan elastisitas harga permintaan $|E_d| = 4,00$.",
            "$L = 0,50$, dengan elastisitas harga permintaan $|E_d| = 2,00$.",
            "$L = 1,00$, dengan elastisitas harga permintaan $|E_d| = 1,00$ (elastis uniter).",
            "$L = 0$, yang menunjukkan bahwa perusahaan tidak memiliki kekuatan monopoli sama sekali."
        ],
        "formula": {
            "title": "FORMULA INDEKS LERNER KEKUATAN MONOPOLI",
            "latex": "\\begin{aligned} L & = \\frac{P - MC}{P} = \\frac{100.000 - 25.000}{100.000} = \\frac{75.000}{100.000} = \\mathbf{0,75} \\\\ \\text{Hubungan Elastisitas:} & \\quad L = \\frac{1}{|E_d|} \\implies |E_d| = \\frac{1}{L} = \\frac{1}{0,75} = \\frac{4}{3} \\approx \\mathbf{1,33} \\end{aligned}",
            "legend": "• Rentang Indeks Lerner: $0 \\le L \\le 1$<br>• Pasar Persaingan Sempurna ($P = MC$) memiliki $L = 0$<br>• Semakin mendekati 1, semakin besar mark-up harga di atas biaya marjinal (daya monopoli semakin kuat)"
        },
        "hints": {
            "concept": "Indeks Lerner L = (P - MC) / P = (100 - 25) / 100 = 75/100 = 0,75. Hubungan elastisitas L = 1 / |Ed| -> |Ed| = 1 / 0,75 = 1,33.",
            "execution": "Pilih: L = 0,75 dengan elastisitas |Ed| = 1,33."
        }
    },
    {
        "id": "eko-sim-08",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Penghitungan PDB Menggunakan Pendekatan Nilai Tambah (Value Added)",
        "stem": "Dalam suatu rantai industri garmen, tercatat aliran transaksi sebagai berikut:\n1. Petani kapas menjual kapas mentah ke pabrik pemintalan benang seharga Rp 40.000.000,-\n2. Pabrik pemintalan memproses kapas menjadi benang dan menjualnya ke pabrik tekstil seharga Rp 70.000.000,-\n3. Pabrik tekstil menenun benang menjadi kain dan menjualnya ke industri garmen seharga Rp 120.000.000,-\n4. Industri garmen menjahit kain menjadi pakaian jadi dan menjualnya ke butik ritel seharga Rp 190.000.000,-\n5. Butik ritel menjual pakaian jadi kepada konsumen akhir seharga Rp 260.000.000,-\nBesarnya kontribusi nilai tambah bruto rantai industri tersebut terhadap Produk Domestik Bruto (PDB) negara adalah...",
        "correct": "Rp 260.000.000,-, tepat sama dengan nilai barang akhir konsumsi, sehingga terhindar dari kesalahan perhitungan ganda (_double counting_).",
        "distractors": [
            "Rp 680.000.000,-, hasil penjumlahan seluruh nilai transaksi bruto dari petani hingga butik ritel.",
            "Rp 420.000.000,-, hasil selisih nilai penjualan butik dengan biaya kapas awal petani.",
            "Rp 220.000.000,-, hasil pengurangan nilai kain tekstil dari total omzet pakaian jadi.",
            "Rp 190.000.000,-, sesuai dengan nilai penyerahan barang dari pabrik garmen ke pihak ritel."
        ],
        "formula": {
            "title": "PENDEKATAN NILAI TAMBAH (VALUE ADDED APPROACH)",
            "latex": "\\begin{aligned} \\text{Nilai Tambah 1 (Kapas):} & \\quad 40.000.000 - 0 = 40.000.000 \\\\ \\text{Nilai Tambah 2 (Benang):} & \\quad 70.000.000 - 40.000.000 = 30.000.000 \\\\ \\text{Nilai Tambah 3 (Kain):} & \\quad 120.000.000 - 70.000.000 = 50.000.000 \\\\ \\text{Nilai Tambah 4 (Pakaian):} & \\quad 190.000.000 - 120.000.000 = 70.000.000 \\\\ \\text{Nilai Tambah 5 (Ritel):} & \\quad 260.000.000 - 190.000.000 = 70.000.000 \\\\ \\mathbf{\\sum \\text{Nilai Tambah (PDB)}} & = 40 + 30 + 50 + 70 + 70 = \\mathbf{260.000.000} \\end{aligned}",
            "legend": "• Pendekatan Nilai Tambah secara matematis identik dengan Pendekatan Pengeluaran Barang Akhir ($C = 260 \\text{ Juta}$)"
        },
        "hints": {
            "concept": "PDB pendekatan produksi dihitung dari penjumlahan seluruh nilai tambah di setiap tahapan, yang nilainya tepat sama dengan harga jual barang akhir kepada konsumen = 260 juta.",
            "execution": "Pilih: Rp 260.000.000,- (sama dengan nilai barang akhir)."
        }
    },
    {
        "id": "eko-sim-09",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Penghitungan Pertumbuhan Ekonomi Riil Menggunakan Deflator PDB",
        "stem": "Data perekonomian suatu negara mencatat:\n- PDB Nominal Tahun 2023 = Rp 2.000 Triliun (dengan Deflator PDB = 100 sebagai tahun dasar)\n- PDB Nominal Tahun 2024 = Rp 2.420 Triliun\n- Deflator PDB Tahun 2024 = 110\nLaju pertumbuhan ekonomi riil negara tersebut pada tahun 2024 adalah...",
        "correct": "$10,0\\%$, dihitung dari kenaikan PDB Riil dari Rp 2.000 Triliun menjadi Rp 2.200 Triliun.",
        "distractors": [
            "$21,0\\%$, hasil perhitungan kenaikan PDB nominal tanpa memperhitungkan deflator inflasi.",
            "$11,0\\%$, hasil pengurangan tingkat inflasi deflator langsung dari persentase nominal.",
            "$12,0\\%$, hasil pembagian langsung rasio deflator terhadap PDB nominal tahun berjalan.",
            "$5,0\\%$, hasil koreksi deflator menggunakan indeks harga produsen industri berat."
        ],
        "formula": {
            "title": "KALKULASI PDB RIIL DAN PERTUMBUHAN EKONOMI",
            "latex": "\\begin{aligned} \\text{PDB Riil}_{2023} & = \\frac{\\text{PDB Nominal}_{2023}}{\\text{Deflator}_{2023}} \\times 100 = \\frac{2.000}{100} \\times 100 = \\mathbf{2.000 \\text{ Triliun}} \\\\ \\text{PDB Riil}_{2024} & = \\frac{\\text{PDB Nominal}_{2024}}{\\text{Deflator}_{2024}} \\times 100 = \\frac{2.420}{110} \\times 100 = \\mathbf{2.200 \\text{ Triliun}} \\\\ \\mathbf{\\text{Laju Pertumbuhan}} & = \\frac{2.200 - 2.000}{2.000} \\times 100\\% = \\frac{200}{2.000} \\times 100\\% = \\mathbf{10,0\\%} \\end{aligned}",
            "legend": "• PDB Riil mencerminkan kuantitas fisik output riil barang dan jasa tanpa pengaruh distorsi kenaikan harga (inflasi)"
        },
        "hints": {
            "concept": "PDB Riil 2024 = (PDB Nominal / Deflator) * 100 = (2.420 / 110) * 100 = 2.200 Triliun. Pertumbuhan riil = (2.200 - 2.000) / 2.000 = 10,0%.",
            "execution": "Pilih: 10,0%."
        }
    },
    {
        "id": "eko-sim-10",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Multiplier Pajak Lump-Sum vs Pengganda Belanja Pemerintah",
        "stem": "Dalam model perekonomian tertutup tiga sektor dengan fungsi konsumsi $C = 150 + 0,8Y_d$, pemerintah berencana meningkatkan pendapatan nasional keseimbangan sebesar $\\Delta Y = \\text{Rp } 200 \\text{ Triliun}$. Jika pemerintah memilih menggunakan instrumen penurunan pajak lump-sum ($\\Delta T$), besarnya pemotongan pajak yang harus dilakukan adalah...",
        "correct": "Pemotongan pajak sebesar $\\Delta T = -\\text{Rp } 50 \\text{ Triliun}$, karena angka pengganda pajak bernilai $k_T = -\\frac{MPC}{1 - MPC} = -\\frac{0,8}{0,2} = -4$.",
        "distractors": [
            "Pemotongan pajak sebesar $\\Delta T = -\\text{Rp } 40 \\text{ Triliun}$, mengikuti koefisien belanja pemerintah lima kali lipat.",
            "Pemotongan pajak sebesar $\\Delta T = -\\text{Rp } 200 \\text{ Triliun}$, agar nilainya sama persis dengan target kenaikan pendapatan nasional.",
            "Kenaikan pajak sebesar $\\Delta T = +\\text{Rp } 50 \\text{ Triliun}$, untuk memperkuat kas perbendaharaan negara.",
            "Pemotongan pajak sebesar $\\Delta T = -\\text{Rp } 25 \\text{ Triliun}$, hasil estimasi separuh angka pengganda investasi."
        ],
        "formula": {
            "title": "FORMULA ANGKA PENGGANDA PAJAK (TAX MULTIPLIER)",
            "latex": "\\begin{aligned} k_T & = -\\frac{MPC}{1 - MPC} = -\\frac{0,8}{0,2} = -4 \\\\ \\Delta Y & = k_T \\cdot \\Delta T \\implies 200 = -4 \\cdot \\Delta T \\implies \\mathbf{\\Delta T = -50 \\text{ Triliun}} \\end{aligned}",
            "legend": "• Multiplier Pajak selalu lebih kecil 1 poin secara absolut dibanding multiplier belanja: $|k_T| = |k_G| - 1 = 5 - 1 = 4$<br>• Tanda negatif menunjukkan arah berlawanan: Penurunan pajak memicu kenaikan pendapatan nasional"
        },
        "hints": {
            "concept": "Multiplier pajak k_T = -MPC / (1 - MPC) = -0,8 / 0,2 = -4. Delta Y = k_T * Delta T -> 200 = -4 * Delta T -> Delta T = -50 Triliun.",
            "execution": "Pilih: Pemotongan pajak sebesar Delta T = -Rp 50 Triliun."
        }
    },
    {
        "id": "eko-sim-11",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Instrumen Kebijakan Moneter Kualitatif Bank Sentral (Moral Suasion)",
        "stem": "Selain menggunakan instrumen moneter kuantitatif (seperti Operasi Pasar Terbuka, Fasilitas Diskonto, dan GWM), Bank Indonesia secara aktif menerapkan instrumen moneter kualitatif berupa Himbauan Moral (_Moral Suasion_). Penerapan himbauan moral oleh Bank Indonesia dalam prakteknya berwujud...",
        "correct": "Pertemuan berkala dan komunikasi persuasif pimpinan bank sentral dengan direksi bank-bank umum agar secara sukarela menyelaraskan penyaluran kredit dan suku bunga perbankan dengan target stabilitas moneter nasional tanpa adanya paksaan sanksi hukum langsung.",
        "distractors": [
            "Penerbitan surat perintah penutupan paksa operasional kantor cabang bank yang menolak menurunkan bunga deposito.",
            "Penyitaan seluruh sertifikat deposito berjangka milik nasabah korporasi swasta untuk dijadikan cadangan devisa negara.",
            "Penetapan kuota impor bahan pangan pokok melalui lelang terbuka kementerian perdagangan.",
            "Pemberian subsidi bunga kredit usaha mikro secara langsung yang ditransfer dari rekening kas negara APBN."
        ],
        "formula": {
            "title": "KLASIFIKASI INSTRUMEN KEBIJAKAN MONETER BANK SENTRAL",
            "latex": "\\begin{cases} \\mathbf{\\text{Kuantitatif:}} & \\text{Operasi Pasar Terbuka (SBN), Fasilitas Diskonto (BI-Rate), GWM} \\\\ \\mathbf{\\text{Kualitatif:}} & \\begin{aligned} & \\text{1. Himbauan Moral (Moral Suasion / Persuasive Communication)} \\\\ & \\text{2. Pengawasan Kredit Selektif (Selective Credit Control / LTV / DTI)} \\end{aligned} \\end{cases}",
            "legend": "• Moral Suasion efektif membangun transparansi ekspektasi pasar dan memandu sinyal transmisi moneter perbankan"
        },
        "hints": {
            "concept": "Himbauan moral (Moral Suasion) adalah ajakan/himbauan persuasif bank sentral kepada pimpinan bank umum untuk menyelaraskan kebijakan kredit dengan target moneter tanpa sanksi formal.",
            "execution": "Pilih opsi yang menjelaskan komunikasi persuasif pimpinan bank sentral dengan direksi bank-bank umum secara sukarela."
        }
    },
    {
        "id": "eko-sim-12",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Dampak Kebijakan Tarif Impor terhadap Kesejahteraan Ekonomi (Surplus Analisis)",
        "stem": "Pemerintah memberlakukan tarif bea masuk sebesar Rp 2.000,- per kg atas impor daging sapi untuk melindungi peternak domestik. Dampak kebijakan proteksi tarif impor tersebut terhadap diagram surplus ekonomi di pasar dalam negeri adalah...",
        "correct": "Surplus konsumen berkurang, surplus produsen domestik bertambah, pemerintah memperoleh penerimaan bea masuk, dan tercipta kerugian bobot mati masyarakat (Deadweight Loss) yang terdiri atas distorsi produksi dan distorsi konsumsi.",
        "distractors": [
            "Surplus konsumen bertambah pesat karena kualitas daging sapi lokal meningkat dua kali lipat.",
            "Surplus produsen domestik menyusut karena harga jual daging sapi di pasar domestik menjadi lebih murah.",
            "Seluruh surplus ekonomi masyarakat musnah tanpa ada penerimaan pajak bea masuk yang masuk ke kas negara.",
            "Perekonomian mencapai efisiensi alokatif optimal dengan hilangnya seluruh beban subsidi pemerintah."
        ],
        "formula": {
            "title": "DAMPAK KESEJAHTERAAN DARI TARIF IMPOR (WELFARE ANALYSIS)",
            "latex": "\\begin{aligned} \\Delta CS & = -(a + b + c + d) \\quad (\\text{Konsumen Rugi Besar}) \\\\ \\Delta PS & = +a \\quad (\\text{Produsen Domestik Untung}) \\\\ \\text{Penerimaan Bea Masuk} & = +c = \\text{Tarif} \\times \\text{Volume Impor Baru} \\\\ \\mathbf{\\text{Net Welfare Loss (DWL)}} & = -(b + d) \\end{aligned}",
            "legend": "• $b$: Kerugian inefisiensi produksi domestik (biaya marjinal lokal > harga dunia)<br>• $d$: Kerugian distorsi konsumsi (konsumen terpaksa mengurangi konsumsi daging)"
        },
        "hints": {
            "concept": "Tarif impor menaikkan harga domestik: Surplus konsumen berkurang (-), Surplus produsen bertambah (+), Pemerintah dapat kas bea masuk (+), Timbul DWL berupa segitiga distorsi produksi dan konsumsi.",
            "execution": "Pilih: Surplus konsumen berkurang, surplus produsen bertambah, kas bea masuk bertambah, dan timbul deadweight loss."
        }
    },
    {
        "id": "eko-sim-13",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Penggunaan Jurnal Khusus (Special Journals) Perusahaan Dagang",
        "stem": "Dalam siklus akuntansi perusahaan dagang yang memiliki frekuensi transaksi tinggi, transaksi transaksi berikut wajib dicatat ke dalam **Jurnal Khusus Pengeluaran Kas (Cash Payment Journal)**, KECUALI...",
        "correct": "Transaksi pengembalian barang dagangan yang rusak kepada pemasok (vendor) atas pembelian barang secara kredit minggu lalu.",
        "distractors": [
            "Pembayaran utang dagang kepada pemasok dengan memanfaatkan syarat potongan tunai 2/10, n/30.",
            "Pembayaran gaji karyawan toko bulanan secara tunai melalui transfer rekening kas bank perusahaan.",
            "Pembelian perlengkapan kantor operasional secara tunai dari toko alat tulis terdekat.",
            "Pengambilan uang tunai dari kas perusahaan oleh pemilik untuk keperluan pribadi (Prive)."
        ],
        "formula": {
            "title": "FUNGSI DAN KLASIFIKASI JURNAL KHUSUS",
            "latex": "\\begin{cases} \\text{Jurnal Pembelian (PJ):} & \\text{Pembelian barang dagangan secara KREDIT} \\\\ \\text{Jurnal Penjualan (SJ):} & \\text{Penjualan barang dagangan secara KREDIT} \\\\ \\text{Jurnal Penerimaan Kas (CRJ):} & \\text{Seluruh transaksi yang MENERIMA UANG KAS} \\\\ \\mathbf{\\text{Jurnal Pengeluaran Kas (CDJ):}} & \\mathbf{\\text{Seluruh transaksi yang MENGELUARKAN UANG KAS}} \\\\ \\mathbf{\\text{Jurnal Umum (GJ):}} & \\mathbf{\\text{Retur Pembelian/Penjualan Kredit, AJP, Penutup, Pembalik}} \\end{cases}",
            "legend": "• Retur pembelian barang dagangan secara kredit dicatat pada Jurnal Umum (Debet: Utang Dagang, Kredit: Retur Pembelian) karena tidak ada arus kas keluar"
        },
        "hints": {
            "concept": "Jurnal pengeluaran kas hanya mencatat transaksi yang mengeluarkan uang kas. Retur pembelian kredit tidak mengeluarkan kas, melainkan dicatat di Jurnal Umum.",
            "execution": "Pilih opsi: Pengembalian barang dagangan atas pembelian secara kredit (Retur pembelian kredit)."
        }
    },
    {
        "id": "eko-sim-14",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Tujuan dan Ayat Jurnal Penutup (Closing Entries) Akhir Periode",
        "stem": "Pada akhir periode akuntansi, perusahaan wajib membuat ayat jurnal penutup (closing entries). Tujuan utama pembuatan jurnal penutup serta kelompok akun yang harus ditutup saldonya menjadi nol adalah...",
        "correct": "Menolkan saldo seluruh Akun Nominal (Pendapatan dan Beban) serta akun Prive/Dividen, lalu memindahkan saldo laba/rugi bersih periode berjalan ke akun Modal/Laba Ditahan di Neraca.",
        "distractors": [
            "Menolkan saldo seluruh Akun Riil (Aset, Liabilitas, dan Ekuitas) agar neraca awal tahun depan bersih.",
            "Menghapus seluruh piutang dagang pelanggan yang belum tertagih sampai tanggal neraca.",
            "Mengganti seluruh nilai wajar gedung kantor dengan nilai perolehan historis amortisasi.",
            "Memindahkan seluruh saldo kas bank perusahaan ke rekening kas negara kementerian keuangan."
        ],
        "formula": {
            "title": "LANGKAH-LANGKAH JURNAL PENUTUP (CLOSING ENTRIES)",
            "latex": "\\begin{aligned} \\text{1. Tutup Akun Pendapatan:} & \\quad \\text{Debit: Pendapatan, } \\text{Kredit: Ikhtisar Laba Rugi} \\\\ \\text{2. Tutup Akun Beban:} & \\quad \\text{Debit: Ikhtisar Laba Rugi, } \\text{Kredit: Beban-Beban} \\\\ \\text{3. Tutup Saldo Laba/Rugi:} & \\quad \\text{Debit: Ikhtisar Laba Rugi, } \\text{Kredit: Modal (Jika Laba)} \\\\ \\text{4. Tutup Akun Prive:} & \\quad \\text{Debit: Modal, } \\text{Kredit: Prive} \\end{aligned}",
            "legend": "• Akun Nominal (Temporary Accounts) ditutup agar tidak mencampuri perhitungan laba periode berikutnya<br>• Akun Riil (Permanent Accounts) saldonya terbawa terus ke neraca periode baru"
        },
        "hints": {
            "concept": "Jurnal penutup menolkan akun-akun nominal (pendapatan, beban, ikhtisar laba rugi, prive) dan memindahkan saldo laba/rugi ke modal.",
            "execution": "Pilih opsi: Menolkan saldo seluruh Akun Nominal (Pendapatan dan Beban) serta akun Prive, dan memindahkan saldo ke akun Modal."
        }
    },
    {
        "id": "eko-sim-15",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Logika Pembuatan Ayat Jurnal Pembalik (Reversing Entries)",
        "stem": "Pada awal periode akuntansi baru (tanggal 2 Januari), bagian akuntansi perusahaan menyusun ayat jurnal pembalik (reversing entries). Karakteristik akun yang WAJIB dibuatkan jurnal pembalik adalah...",
        "correct": "Akun penyesuaian akhir periode yang memunculkan akun riil baru dari transaksi akrual, seperti Beban yang Masih Harus Dibayar (Utang Beban) dan Pendapatan yang Masih Harus Diterima (Piutang Pendapatan).",
        "distractors": [
            "Ayat jurnal penyesuaian untuk penyusutan aset tetap dan amortisasi hak paten tak berwujud.",
            "Seluruh transaksi penyetoran modal awal tunai pemegang saham baru.",
            "Penyesuaian persediaan akhir barang dagangan menggunakan pendekatan ikhtisar laba rugi.",
            "Pelunasan utang obligasi jangka panjang yang telah jatuh tempo di bank kustodian."
        ],
        "formula": {
            "title": "ATURAN JURNAL PEMBALIK (REVERSING ENTRIES)",
            "latex": "\\begin{cases} \\mathbf{\\text{Wajib Dibalik:}} & \\begin{aligned} & \\text{1. Beban akrual (Beban yang masih harus dibayar / Utang beban)} \\\\ & \\text{2. Pendapatan akrual (Piutang pendapatan)} \\\\ & \\text{3. Beban dibayar dimuka (dicatat pendekatan BEBAN)} \\\\ & \\text{4. Pendapatan diterima dimuka (dicatat pendekatan PENDAPATAN)} \\end{aligned} \\\\ \\mathbf{\\text{Tidak Boleh Dibalik:}} & \\text{Beban Penyusutan, Amortisasi, Beban Kerugian Piutang} \\end{cases}",
            "legend": "• Tujuan Jurnal Pembalik: Menyederhanakan proses pencatatan transaksi rutin di periode berjalan berikutnya agar terhindar dari pencatatan ganda"
        },
        "hints": {
            "concept": "Jurnal pembalik dibuat untuk beban yang masih harus dibayar (utang beban) dan pendapatan yang masih harus diterima (piutang pendapatan). Penyusutan dan amortisasi TIDAK pernah dibalik.",
            "execution": "Pilih: Beban yang Masih Harus Dibayar dan Pendapatan yang Masih Harus Diterima."
        }
    },
    {
        "id": "eko-sim-16",
        "materi": "LEMBAGA KEUANGAN & PASAR MODAL",
        "topic": "Rasio Kecukupan Modal Bank (Capital Adequacy Ratio / CAR)",
        "stem": "Otoritas Jasa Keuangan (OJK) dan regulasi Basel mewajibkan perbankan komersial mempertahankan Rasio Kecukupan Modal (Capital Adequacy Ratio / CAR) minimal di atas batas ketentuan (di Indonesia minimal 8% s.d. 14% tergantung profil risiko). Formula perhitungan CAR dan fungsi ekonomisnya adalah...",
        "correct": "$\\text{CAR} = \\frac{\\text{Modal Bank (Tier 1 + Tier 2)}}{\\text{Aktiva Tertimbang Menurut Risiko (ATMR)}} \\times 100\\%$, yang berfungsi sebagai bantalan penyerap kerugian kredit bermasalah agar dana simpanan nasabah penyimpan tetap aman.",
        "distractors": [
            "$\\text{CAR} = \\frac{\\text{Kredit yang Disalurkan}}{\\text{Total Dana Pihak Ketiga}} \\times 100\\%$, yang berfungsi mengukur likuiditas pinjaman debitur.",
            "$\\text{CAR} = \\frac{\\text{Laba Bersih}}{\\text{Total Aset Bank}} \\times 100\\%$, yang berfungsi mengukur profitabilitas modal pemegang saham.",
            "$\\text{CAR} = \\frac{\\text{Kredit Macet (NPL)}}{\\text{Total Kredit}} \\times 100\\%$, yang berfungsi menghitung rasio kebangkrutan perbankan.",
            "$\\text{CAR} = \\frac{\\text{Cadangan Giro Wajib}}{\\text{Kas Fisik di Brankas}} \\times 100\\%$, yang berfungsi menghitung rasio uang kartal."
        ],
        "formula": {
            "title": "FORMULA CAPITAL ADEQUACY RATIO (CAR / KPMM)",
            "latex": "\\begin{aligned} \\text{CAR} & = \\frac{\\text{Modal Inti (Tier 1) + Modal Pelengkap (Tier 2)}}{\\text{ATMR (Aktiva Tertimbang Menurut Risiko)}} \\times 100\\% \\ge 8\\% \\\\ \\text{ATMR} & = \\sum (\\text{Nilai Aset}_i \\times \\text{Bobot Risiko}_i) \\end{aligned}",
            "legend": "• Kas dan SBN memiliki bobot risiko 0% (bebas risiko)<br>• Kredit komersial memiliki bobot risiko 100%<br>• CAR tinggi = Ketahanan bank terhadap guncangan krisis finansial sangat kuat"
        },
        "hints": {
            "concept": "CAR = (Modal Bank / ATMR) x 100%. Fungsinya sebagai penyerap potensi kerugian kredit agar dana nasabah terlindungi.",
            "execution": "Pilih: CAR = Modal Bank / ATMR x 100%."
        }
    },
    {
        "id": "eko-sim-17",
        "materi": "LEMBAGA KEUANGAN & PASAR MODAL",
        "topic": "Valuasi Saham: Price to Earnings Ratio (PER) dan Earning Per Share (EPS)",
        "stem": "PT Surya Kencana memiliki 100.000.000 lembar saham biasa yang beredar di Bursa Efek Indonesia. Pada tahun 2024, perusahaan berhasil membukukan laba bersih setelah pajak sebesar Rp 50.000.000.000,- (Rp 50 Miliar). Jika saat ini saham perusahaan diperdagangkan pada harga pasar Rp 7.500,- per lembar, nilai Laba per Lembar Saham (Earnings Per Share / EPS) dan Rasio Harga terhadap Laba (Price to Earnings Ratio / PER) adalah...",
        "correct": "$\\text{EPS} = \\text{Rp } 500,-$ per lembar saham dan $\\text{PER} = 15 \\text{ kali}$.",
        "distractors": [
            "$\\text{EPS} = \\text{Rp } 50,-$ per lembar saham dan $\\text{PER} = 150 \\text{ kali}$.",
            "$\\text{EPS} = \\text{Rp } 750,-$ per lembar saham dan $\\text{PER} = 10 \\text{ kali}$.",
            "$\\text{EPS} = \\text{Rp } 500,-$ per lembar saham dan $\\text{PER} = 25 \\text{ kali}$.",
            "$\\text{EPS} = \\text{Rp } 250,-$ per lembar saham dan $\\text{PER} = 30 \\text{ kali}$."
        ],
        "formula": {
            "title": "FORMULA VALUASI EPS DAN PRICE TO EARNINGS RATIO",
            "latex": "\\begin{aligned} \\mathbf{\\text{EPS}} & = \\frac{\\text{Laba Bersih Setelah Pajak}}{\\text{Jumlah Saham Beredar}} = \\frac{50.000.000.000}{100.000.000} = \\mathbf{\\text{Rp } 500,-} \\\\ \\mathbf{\\text{PER}} & = \\frac{\\text{Harga Pasar per Saham}}{\\text{EPS}} = \\frac{7.500}{500} = \\mathbf{15 \\text{ kali}} \\end{aligned}",
            "legend": "• PER 15 kali bermakna: Investor bersedia membayar Rp 15 untuk setiap Rp 1 laba bersih yang dihasilkan perusahaan, atau butuh 15 tahun laba konstan untuk balik modal investasi murni"
        },
        "hints": {
            "concept": "EPS = Laba Bersih / Jumlah Saham = 50 Miliar / 100 Juta = 500 per lembar. PER = Harga Saham / EPS = 7.500 / 500 = 15 kali.",
            "execution": "Pilih: EPS = Rp 500,- dan PER = 15 kali."
        }
    },
    {
        "id": "eko-sim-18",
        "materi": "BADAN USAHA & KOPERASI",
        "topic": "Klasifikasi Modal Koperasi menurut UU No. 25 Tahun 1992",
        "stem": "Berdasarkan Undang-Undang Republik Indonesia Nomor 25 Tahun 1992 tentang Perkoperasian, permodalan koperasi terdiri atas Modal Sendiri dan Modal Pinjaman. Yang termasuk ke dalam kelompok **Modal Sendiri Koperasi** adalah...",
        "correct": "Simpanan Pokok, Simpanan Wajib, Dana Cadangan, dan Hibah.",
        "distractors": [
            "Simpanan Pokok, Simpanan Sukarela, Pinjaman Bank Komersial, dan Obligasi.",
            "Simpanan Wajib, Simpanan Sukarela, Modal Penyertaan BUMN, dan Kredit Usaha Rakyat.",
            "Simpanan Pokok, Modal Pinjaman Anggota, Dana Pensiun, dan Surat Utang Luar Negeri.",
            "Simpanan Sukarela, Deposito Anggota, Hibah Pemerintah Asing, dan Fasilitas Diskonto."
        ],
        "formula": {
            "title": "STRUKTUR PERMODALAN KOPERASI (UU NO. 25 TAHUN 1992)",
            "latex": "\\begin{cases} \\mathbf{\\text{Modal Sendiri:}} & \\mathbf{\\text{1. Simpanan Pokok, 2. Simpanan Wajib, 3. Dana Cadangan, 4. Hibah}} \\\\ \\text{Modal Pinjaman:} & \\text{1. Anggota (Simpanan Sukarela/Wajib Khusus), 2. Koperasi Lain, 3. Bank, 4. Obligasi} \\end{cases}",
            "legend": "• Simpanan Pokok & Wajib tidak dapat diambil selama menjadi anggota<br>• Simpanan Sukarela diperlakukan sebagai Modal Pinjaman karena sewaktu-waktu dapat ditarik oleh anggota"
        },
        "hints": {
            "concept": "Pasal 41 UU No. 25/1992: Modal Sendiri Koperasi terdiri dari: Simpanan Pokok, Simpanan Wajib, Dana Cadangan, dan Hibah. Simpanan sukarela masuk modal pinjaman.",
            "execution": "Pilih: Simpanan Pokok, Simpanan Wajib, Dana Cadangan, dan Hibah."
        }
    },
    {
        "id": "eko-sim-19",
        "materi": "BADAN USAHA & KOPERASI",
        "topic": "Empat Fungsi Fundamental Manajemen (POAC George Terry)",
        "stem": "Seorang direktur utama membagi tugas operasional kepada staf, menetapkan struktur organisasi garis dan staf, serta mendelegasikan wewenang penanggung jawab proyek kepada para manajer divisi. Tindakan direktur utama tersebut mencerminkan pelaksanaan fungsi manajemen...",
        "correct": "Organizing (Pengorganisasian), yaitu proses pengelompokan aktivitas kerja, pengalokasian sumber daya organisasi, dan penetapan wewenang serta tanggung jawab struktural.",
        "distractors": [
            "Planning (Perencanaan), yaitu penetapan tujuan jangka panjang dan strategi pencapaian target target perusahaan.",
            "Actuating (Penggerakan), yaitu pemberian motivasi, bimbingan, dan komunikasi persuasif kepada karyawan di lapangan.",
            "Controlling (Pengawasan), yaitu pengukuran kinerja aktual dibandingkan standar dan tindakan koreksi penyimpangan.",
            "Innovating (Inovasi), yaitu penciptaan teknologi mutakhir yang belum pernah diproduksi sebelumnya."
        ],
        "formula": {
            "title": "FUNGSI MANAJEMEN FUNDAMENTAL (POAC)",
            "latex": "\\text{POAC} \\equiv \\begin{cases} \\text{Planning (P):} & \\text{Menentukan Sasaran \\& Cara Mencapainya (What, How, When)} \\\\ \\mathbf{\\text{Organizing (O):}} & \\mathbf{\\text{Membagi Pekerjaan, Struktur Organisasi, Pendelegasian Wewenang}} \\\\ \\text{Actuating (A):} & \\text{Menggerakkan, Mengarahkan, \\& Memotivasi SDM (Leadership)} \\\\ \\text{Controlling (C):} & \\text{Mengevaluasi Kinerja vs Target \\& Mengoreksi Deviasi} \\end{cases}",
            "legend": "• Pelaksanaan POAC yang harmonis menjamin efektivitas dan efisiensi pencapaian tujuan korporasi"
        },
        "hints": {
            "concept": "Membagi tugas, menyusun struktur organisasi, dan mendelegasikan wewenang adalah esensi fungsi Organizing (Pengorganisasian).",
            "execution": "Pilih: Organizing (Pengorganisasian)."
        }
    },
    {
        "id": "eko-sim-20",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Infrastruktur Sistem Pembayaran Nasional: BI-FAST vs RTGS",
        "stem": "Bank Indonesia menyediakan berbagai infrastruktur sistem pembayaran non-tunai. Karakteristik komparatif antara layanan **BI-FAST** dan **Bank Indonesia Real Time Gross Settlement (BI-RTGS)** yang benar adalah...",
        "correct": "BI-FAST melayani transaksi ritel nasabah bernilai rendah hingga maksimal Rp 250.000.000,- yang beroperasi selama 24 jam sehari 7 hari seminggu (24/7) secara real-time; sedangkan BI-RTGS melayani transfer dana bernilai besar (_high-value payments_ di atas Rp 100 Juta) dan transaksi antarbank yang penyelesaiannya seketika per transaksi pada jam operasional kerja.",
        "distractors": [
            "BI-FAST khusus digunakan untuk transaksi valuta asing internasional sedangkan RTGS hanya untuk mata uang lokal pecahan kecil.",
            "BI-FAST hanya beroperasi pada hari kerja perbankan sedangkan RTGS beroperasi 24 jam tanpa henti di akhir pekan.",
            "BI-FAST membebankan biaya transfer jutaan rupiah sedangkan RTGS bebas biaya administrasi untuk masyarakat umum.",
            "Kedua sistem pembayaran tersebut telah dihapuskan dan digantikan sepenuhnya oleh mata uang kripto tak terdaftar."
        ],
        "formula": {
            "title": "TAKSONOMI SISTEM PEMBAYARAN BANK INDONESIA",
            "latex": "\\begin{array}{|l|c|c|} \\hline \\text{Fitur} & \\text{BI-FAST} & \\text{BI-RTGS} \\\\ \\hline \\text{Segmen Transaksi} & \\mathbf{\\text{Ritel (Nasabah Umum)}} & \\mathbf{\\text{Nilai Besar (High-Value) \\& Antarbank}} \\\\ \\text{Batas Maksimal} & \\text{Rp 250 Juta per transaksi} & \\text{Di atas Rp 100 Juta} \\\\ \\text{Waktu Operasional} & \\mathbf{\\text{24 Jam / 7 Hari (Nonstop)}} & \\text{Jam Kerja Sistem Bank Sentral} \\\\ \\text{Kecepatan} & \\text{Real-time End-to-End} & \\text{Real-time Gross Settlement} \\\\ \\hline \\end{array}",
            "legend": "• BI-FAST memperluas inklusi keuangan digital dan mempercepat sirkulasi moneter ritel"
        },
        "hints": {
            "concept": "BI-FAST: ritel (maksimal 250 juta), operasional 24/7 real-time. BI-RTGS: nilai besar (high value, di atas 100 juta), jam kerja bank sentral.",
            "execution": "Pilih opsi yang menjelaskan BI-FAST melayani ritel 24/7 hingga 250 juta, dan RTGS melayani nilai besar seketika saat jam kerja."
        }
    },
    {
        "id": "eko-sim-21",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Komponen Transaksi Finansial Neraca Pembayaran: FDI vs Portofolio",
        "stem": "Dalam Neraca Pembayaran Internasional (Balance of Payments / BOP), aliran masuk modal asing dicatat pada Transaksi Finansial. Perbedaan konseptual antara Investasi Langsung (Foreign Direct Investment / FDI) dan Investasi Portofolio (Portfolio Investment) adalah...",
        "correct": "FDI melibatkan pendirian pabrik fisik, pengadaan aset riil, dan kepemilikan saham jangka panjang dengan kendali manajemen aktif (_lasting interest_ minimal 10%); sedangkan Investasi Portofolio berupa pembelian aset keuangan likuid (saham publik dan obligasi) bermotif imbal hasil jangka pendek tanpa kendali manajemen aktif.",
        "distractors": [
            "FDI hanya dilakukan oleh bank sentral negara sedangkan portofolio murni transaksi antar warga negara miskin.",
            "FDI dicatat di Neraca Berjalan sedangkan Investasi Portofolio dicatat di pos Kesalahan dan Kelalaian Bersih.",
            "FDI memiliki likuiditas harian sangat tinggi sehingga modalnya dapat ditarik sewaktu-waktu dalam hitungan detik.",
            "Investasi Portofolio dilarang diperdagangkan di pasar bursa efek internasional menurut konvensi IMF."
        ],
        "formula": {
            "title": "KOMPARASI TRANSAKSI FINANSIAL (BOP IMF MANUAL)",
            "latex": "\\begin{aligned} \\mathbf{\\text{FDI (Direct Investment):}} & \\quad \\text{Pabrik riil, kendali manajemen } \\ge 10\\%, \\text{ modal tahan lama (Sticky Capital)} \\\\ \\mathbf{\\text{Portofolio:}} & \\quad \\text{Saham/Obligasi bursa, kendali } < 10\\%, \\text{ modal sangat likuid (Hot Money)} \\end{aligned}",
            "legend": "• Risiko 'Hot Money' Portofolio: Rentan mengalami pembalikan arus modal tiba-tiba (sudden stop/capital flight) saat terjadi guncangan sentimen global"
        },
        "hints": {
            "concept": "FDI = modal fisik/pabrik riil jangka panjang dengan kontrol manajemen. Investasi Portofolio = instrumen keuangan saham/obligasi likuid tanpa kendali manajemen (hot money).",
            "execution": "Pilih: FDI aset riil dan kendali manajemen aktif, Portofolio aset keuangan likuid jangka pendek tanpa kendali manajemen."
        }
    },
    {
        "id": "eko-sim-22",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Penghitungan Pajak Penghasilan Orang Pribadi (PPh Pasal 21 Progresif)",
        "stem": "Pak Ahmad seorang karyawan swasta belum menikah dan tidak memiliki tanggungan (status PTKP TK/0 = Rp 54.000.000,- per tahun). Selama tahun 2024, ia menerima penghasilan bruto disetahunkan setelah dikurangi biaya jabatan dan iuran pensiun sehingga Penghasilan Neto adalah Rp 114.000.000,-. Berdasarkan tarif progresif PPh Orang Pribadi UU Harmonisasi Peraturan Perpajakan (HPP):\n- Lapisan I: $0 - \\text{Rp } 60.000.000,-$ dikenakan tarif $5\\%$\n- Lapisan II: di atas $\\text{Rp } 60.000.000,-$ s.d. $\\text{Rp } 250.000.000,-$ dikenakan tarif $15\\%$\nBesarnya Pajak Penghasilan (PPh Pasal 21) terutang yang wajib dibayar Pak Ahmad untuk tahun 2024 adalah...",
        "correct": "Rp 3.000.000,- per tahun, dihitung dari tarif 5% atas Penghasilan Kena Pajak (PKP) sebesar Rp 60.000.000,-.",
        "distractors": [
            "Rp 5.700.000,-, hasil perkalian tarif flat lima persen terhadap seluruh penghasilan neto tahunan.",
            "Rp 9.000.000,-, hasil perhitungan lapisan kedua tanpa memperhitungkan batas dasar lapisan awal.",
            "Rp 4.500.000,-, hasil penerapan tarif rata-rata efektif PPh badan.",
            "Rp 1.500.000,-, hasil pemotongan diskon pajak investasi reksadana syariah."
        ],
        "formula": {
            "title": "KALKULASI PPH PASAL 21 UU HPP (STATUS TK/0)",
            "latex": "\\begin{aligned} \\text{Penghasilan Kena Pajak (PKP)} & = \\text{Penghasilan Neto} - \\text{PTKP (TK/0)} \\\\ & = 114.000.000 - 54.000.000 = \\mathbf{60.000.000} \\\\ \\mathbf{\\text{Pajak Terutang (Lapisan I):}} & = 5\\% \\times 60.000.000 = \\mathbf{3.000.000} \\end{aligned}",
            "legend": "• Karena PKP tepat Rp 60 Juta, seluruh pajak terutang masuk dalam Lapisan I (Tarif 5%) tanpa menyentuh Lapisan II (15%)"
        },
        "hints": {
            "concept": "PKP = Penghasilan Neto - PTKP = 114 jt - 54 jt = 60 jt. Karena tepat 60 jt, seluruhnya kena tarif lapisan 1 yaitu 5%. PPh = 5% x 60 jt = 3.000.000.",
            "execution": "Pilih: Rp 3.000.000,- per tahun."
        }
    },
    {
        "id": "eko-sim-23",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Struktur Belanja Transfer ke Daerah (TKD) dalam APBN",
        "stem": "Dalam struktur Anggaran Pendapatan dan Belanja Negara (APBN) Indonesia, pemerintah pusat mengalokasikan pos Transfer ke Daerah (TKD) untuk mendanai desentralisasi fiskal. Dana transfer yang dialokasikan kepada seluruh daerah dengan tujuan utama untuk mengurangi ketimpangan kemampuan keuangan antar daerah dalam rangka pendanaan kebutuhan operasional daerah tanpa ikatan penggunaannya (_block grant_) adalah...",
        "correct": "Dana Alokasi Umum (DAU), yang bersifat _block grant_ (bebas digunakan daerah sesuai prioritas otonomi) dan dialokasikan dengan formula celah fiskal (_fiscal gap_).",
        "distractors": [
            "Dana Alokasi Khusus (DAK) Fisik, yang bersifat _specific grant_ untuk mendanai sarana prasarana fisik pendidikan dan kesehatan.",
            "Dana Bagi Hasil (DBH), yang dibagikan berdasarkan persentase daerah penghasil sumber daya alam migas dan pertambangan.",
            "Dana Otonomi Khusus, yang hanya dialokasikan kepada seluruh provinsi di pulau Jawa secara merata.",
            "Dana Darurat Bencana, yang dialokasikan hanya saat terjadi letusan gunung berapi berskala nasional."
        ],
        "formula": {
            "title": "KLASIFIKASI DANA TRANSFER KE DAERAH (TKD - UU HKPD)",
            "latex": "\\begin{cases} \\mathbf{\\text{Dana Alokasi Umum (DAU):}} & \\mathbf{\\text{Block Grant, Pemerataan celah fiskal antar daerah}} \\\\ \\text{Dana Alokasi Khusus (DAK):} & \\text{Specific Grant (Tujuan khusus prioritas nasional: sekolah, RS)} \\\\ \\text{Dana Bagi Hasil (DBH):} & \\text{Bagi hasil pajak (PPh/PBB) \\& SDA penghasil} \\\\ \\text{Dana Desa:} & \\text{Pemberdayaan dan pembangunan ekonomi desa} \\end{cases}",
            "legend": "• DAU menjadi tulang punggung pembiayaan pelayanan publik dasar di kabupaten/kota"
        },
        "hints": {
            "concept": "DAU (Dana Alokasi Umum) bersifat block grant untuk mengurangi ketimpangan fiskal antar daerah. DAK bersifat spesifik grant.",
            "execution": "Pilih: Dana Alokasi Umum (DAU)."
        }
    },
    {
        "id": "eko-sim-24",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Analisis Kurva Lorenz dan Koefisien Gini Ketimpangan Distribusi Pendapatan",
        "stem": "Sebuah laporan riset sosial memaparkan dua kurva Lorenz distribusi pendapatan untuk Negara Andromeda dan Negara Bima. Kurva Lorenz Negara Andromeda melengkung jauh menjauhi garis diagonal kemerataan sempurna dengan Koefisien Gini $G = 0,52$, sedangkan Kurva Lorenz Negara Bima berada sangat dekat dengan garis diagonal dengan Koefisien Gini $G = 0,26$. Kesimpulan analisis komparatif mengenai distribusi pendapatan di kedua negara tersebut adalah...",
        "correct": "Negara Andromeda mengalami ketimpangan distribusi pendapatan yang parah/tinggi ($G > 0,5$), sedangkan Negara Bima memiliki tingkat pemerataan pendapatan yang relatif merata dan berkeadilan ($G < 0,3$).",
        "distractors": [
            "Negara Andromeda memiliki pemerataan sempurna di mana seluruh warga negaranya berpendapatan identik.",
            "Negara Bima mengalami krisis kemiskinan ekstrem akibat konsentrasi kekayaan pada satu persen oligarki elit.",
            "Kedua negara memiliki struktur pemerataan yang serupa karena selisih nilai Gini tidak memiliki signifikansi statistik.",
            "Negara Bima mengalami kebangkrutan fiskal karena Koefisien Gini di bawah nol koma tiga menandakan deflasi."
        ],
        "formula": {
            "title": "INTERPRETASI ANGKA KOEFISIEN GINI (WORLD BANK STANDARD)",
            "latex": "\\begin{aligned} \\text{Koefisien Gini } (G) & = \\frac{\\text{Luas Area Antara Diagonal \\& Kurva Lorenz}}{\\text{Total Luas Segitiga di Bawah Diagonal}} \\\\ G < 0,3 & \\implies \\mathbf{\\text{Ketimpangan Rendah (Relatif Merata)}} \\\\ 0,3 \\le G \\le 0,5 & \\implies \\text{Ketimpangan Sedang} \\\\ G > 0,5 & \\implies \\mathbf{\\text{Ketimpangan Tinggi (Sangat Timpang)}} \\end{aligned}",
            "legend": "• Semakin melengkung kurva Lorenz ke bawah, semakin luas area ketimpangan dan semakin mendekati 1 nilai Koefisien Gini"
        },
        "hints": {
            "concept": "Gini = 0 merata sempurna, Gini = 1 timpang sempurna. Gini 0,52 = ketimpangan tinggi. Gini 0,26 = ketimpangan rendah (relatif merata).",
            "execution": "Pilih: Negara Andromeda mengalami ketimpangan tinggi (G > 0,5), Negara Bima relatif merata (G < 0,3)."
        }
    },
    {
        "id": "eko-sim-25",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Diagram Alir Lingkar Kegiatan Ekonomi 4 Sektor (Circular Flow Diagram)",
        "stem": "Dalam model diagram alir lingkar kegiatan ekonomi empat sektor (_Circular Flow Diagram_), aliran faktor produksi (seperti tanah, tenaga kerja, modal, dan kewirausahaan) bergerak dari...",
        "correct": "Rumah Tangga Konsumen (RTK) menuju Rumah Tangga Produsen (RTP) melalui Pasar Input (Pasar Faktor Produksi), dan sebagai imbalannya RTP memberikan aliran balas jasa berupa sewa, upah, bunga, dan laba.",
        "distractors": [
            "Rumah Tangga Produsen (RTP) menuju Rumah Tangga Konsumen (RTK) melalui Pasar Output barang jadi.",
            "Pemerintah menuju Masyarakat Luar Negeri melalui jalur perdagangan valuta asing pasar gelap.",
            "Rumah Tangga Konsumen langsung ke Bank Sentral tanpa melalui pasar faktor produksi.",
            "Masyarakat Luar Negeri menuju RTK dalam bentuk subsidi bahan bakar minyak gratis."
        ],
        "formula": {
            "title": "ALIRAN PASAR FAKTOR PRODUKSI (CIRCULAR FLOW)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Pasar Input:}} & \\quad \\text{RTK (Pemilik Faktor)} \\xrightarrow{\\text{Faktor Produksi: } L, K, T} \\text{RTP (Pengguna)} \\\\ & \\quad \\text{RTP} \\xrightarrow{\\text{Balas Jasa: Sewa, Upah, Bunga, Laba}} \\text{RTK} \\\\ \\mathbf{\\text{Pasar Output:}} & \\quad \\text{RTP} \\xrightarrow{\\text{Barang \\& Jasa Konsumsi}} \\text{RTK} \\\\ & \\quad \\text{RTK} \\xrightarrow{\\text{Uang Belanja Konsumsi}} \\text{RTP} \\end{aligned}",
            "legend": "• Empat Pelaku: RTK (Konsumen), RTP (Produsen), RTN (Pemerintah/Negara), RTLN (Luar Negeri)"
        },
        "hints": {
            "concept": "RTK adalah pemilik faktor produksi (tanah, tenaga kerja, modal, keahlian) yang diserahkan ke RTP lewat Pasar Faktor Produksi (Pasar Input).",
            "execution": "Pilih: Dari RTK menuju RTP melalui Pasar Input dengan balas jasa sewa, upah, bunga, dan laba."
        }
    },

    # -------------------------------------------------------------
    # 5 MULTI-SELECT HOTS (eko-sim-26 to eko-sim-30)
    # -------------------------------------------------------------
    {
        "id": "eko-sim-26",
        "materi": "STRUKTUR PASAR",
        "topic": "Karakteristik Fundamental Pasar Persaingan Sempurna",
        "stem": "Pasar persaingan sempurna merupakan model teoretis struktur pasar dengan tingkat efisiensi alokatif dan produktif tertinggi. Manakah TIGA karakteristik utama berikut yang BENAR mengenai pasar persaingan sempurna? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Jumlah penjual dan pembeli sangat banyak di pasar, sehingga masing-masing pelaku tidak memiliki kekuatan pasar untuk mempengaruhi harga (Price Taker)."},
            {"key": "B", "text": "Barang yang diperdagangkan bersifat homogen sempurna (identik dan standardized) sehingga konsumen tidak membedakan asal produsen produk tersebut."},
            {"key": "C", "text": "Terdapat kebebasan penuh untuk keluar-masuk pasar (Free Entry and Free Exit) tanpa adanya hambatan legal, teknologi, maupun finansial bagi perusahaan baru."},
            {"key": "D", "text": "Setiap produsen gencar melakukan promosi iklan perang diskon di televisi untuk membedakan produknya dari pesaing."},
            {"key": "E", "text": "Dalam jangka panjang setiap perusahaan memperoleh laba supernormal monopoli yang dilindungi oleh hak paten negara."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "ASUMSI KLASIK PASAR PERSAINGAN SEMPURNA",
            "latex": "\\begin{cases} \\mathbf{\\text{A. Price Taker:}} & \\text{Kurva permintaan individual horizontal } (P = AR = MR) \\\\ \\mathbf{\\text{B. Homogenitas:}} & \\text{Substitusi sempurna antar produk, elastisitas tak terhingga} \\\\ \\mathbf{\\text{C. Free Entry/Exit:}} & \\text{Mendorong laba ekonomi jangka panjang menjadi nol (Laba Normal)} \\end{cases}",
            "legend": "• A, B, C BENAR: Karakteristik mutlak persaingan sempurna<br>• D SALAH: Iklan tidak diperlukan karena produk homogen<br>• E SALAH: Jangka panjang hanya laba normal ($P = ATC$)"
        },
        "hints": {
            "concept": "Ciri persaingan sempurna: Price taker (A), Produk homogen (B), Bebas keluar masuk / Free entry exit (C). Tidak ada iklan produk dan tidak ada laba supernormal jangka panjang.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "eko-sim-27",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Instrumen Operasi Moneter Kuantitatif Kontraktif Bank Sentral",
        "stem": "Ketika tingkat inflasi melampaui batas toleransi target, Bank Indonesia akan menjalankan kebijakan moneter kontraktif (_tight money policy_) untuk menyerap kelebihan likuiditas di masyarakat. Manakah TIGA instrumen kuantitatif berikut yang diterapkan oleh Bank Sentral? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Menjual Surat Berharga Negara (SBN) atau Sertifikat Bank Indonesia (SBI) kepada perbankan komersial melalui operasi pasar terbuka."},
            {"key": "B", "text": "Menaikkan suku bunga kebijakan acuan (BI-Rate) pada fasilitas diskonto untuk membatasi pinjaman likuiditas bank umum."},
            {"key": "C", "text": "Menaikkan rasio Giro Wajib Minimum (GWM) yang wajib dipelihara bank umum di rekening giro Bank Indonesia."},
            {"key": "D", "text": "Membeli kembali obligasi pemerintah dari masyarakat umum dalam jumlah masif untuk menggandakan peredaran uang kartal."},
            {"key": "E", "text": "Menurunkan suku bunga simpanan tabungan perbankan menjadi nol persen agar masyarakat gemar berbelanja barang konsumsi."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "TRANSMISI KEBIJAKAN MONETER KONTRAKTIF (TIGHT MONEY POLICY)",
            "latex": "\\begin{aligned} \\text{Instrumen:} & \\quad \\mathbf{\\text{Jual SBN (OPT)}} + \\mathbf{\\text{Naikkan BI-Rate}} + \\mathbf{\\text{Naikkan GWM}} \\\\ & \\implies \\text{Likuiditas Bank } \\downarrow \\implies M_s \\downarrow \\implies \\text{Kredit } \\downarrow \\implies AD \\downarrow \\implies \\mathbf{\\text{Inflasi Reda}} \\end{aligned}",
            "legend": "• A, B, C BENAR: Kombinasi instrumen peredam inflasi<br>• D dan E SALAH: Itu adalah kebijakan moneter ekspansif (easy money policy)"
        },
        "hints": {
            "concept": "Moneter kontraktif: Jual SBN (A), Naikkan suku bunga acuan (B), Naikkan GWM (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "eko-sim-28",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Kaidah Dasar Akuntansi Berbasis Akrual (Accrual Basis Accounting)",
        "stem": "Standar Akuntansi Keuangan (SAK) mewajibkan penyusunan laporan keuangan menggunakan basis akrual (_accrual basis_) bukan basis kas (_cash basis_). Manakah TIGA prinsip perlakuan akuntansi berikut yang BENAR mengenai basis akrual? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Pendapatan diakui dan dicatat pada saat timbulnya hak atas penyerahan barang/jasa kepada pelanggan, terlepas dari apakah kas pembayarannya sudah diterima atau belum."},
            {"key": "B", "text": "Beban operasional diakui dan dicatat pada saat terjadinya pemanfaatan sumber daya atau jasa, terlepas dari apakah kas telah dibayarkan tunai atau belum."},
            {"key": "C", "text": "Menerapkan prinsip pencocokan (_matching principle_) antara beban yang dikeluarkan dan pendapatan yang dihasilkan pada periode pelaporan yang sama."},
            {"key": "D", "text": "Pendapatan penjualan hanya boleh dicatat ke dalam buku jurnal ketika kas tunai fisik sudah masuk ke dalam brankas perusahaan."},
            {"key": "E", "text": "Perusahaan tidak perlu membuat ayat jurnal penyesuaian (AJP) pada akhir tahun karena seluruh kas telah terealisasi sempurna."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "PRINSIP ACCRUAL BASIS VS CASH BASIS",
            "latex": "\\begin{cases} \\mathbf{\\text{Pendapatan:}} & \\text{Diakui saat hak timbul (Barang/Jasa diserahkan) } \\implies \\text{Piutang (AR)} \\\\ \\mathbf{\\text{Beban:}} & \\text{Diakui saat manfaat dinikmati } \\implies \\text{Utang Beban (AP)} \\\\ \\mathbf{\\text{Matching:}} & \\text{Beban dikaitkan langsung dengan pendapatan yang dihasilkannya} \\end{cases}",
            "legend": "• A, B, C BENAR: Fondasi kerangka konseptual akuntansi modern SAK/IFRS<br>• D adalah definisi Cash Basis<br>• E SALAH: Basis akrual justru mewajibkan adanya jurnal penyesuaian (AJP)"
        },
        "hints": {
            "concept": "Basis akrual mengakui pendapatan saat hak timbul (A), beban saat terjadi pemanfaatan (B), dan menerapkan matching principle (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "eko-sim-29",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Dampak Intervensi Kebijakan Harga Batas Atas (Ceiling Price)",
        "stem": "Pemerintah menetapkan Kebijakan Harga Eceran Tertinggi (HET / Ceiling Price) untuk komoditas minyak goreng di bawah tingkat harga keseimbangan pasar bebas demi melindungi daya beli masyarakat berpenghasilan rendah. Manakah TIGA konsekuensi ekonomis berikut yang timbul akibat kebijakan tersebut? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Terjadi kelebihan permintaan (Shortage / Excess Demand) di mana jumlah barang yang ingin dibeli masyarakat melampaui jumlah barang yang bersedia dijual oleh produsen."},
            {"key": "B", "text": "Memicu timbulnya pasar gelap (_black market_) di mana barang dijual secara sembunyi-sembunyi dengan harga di atas ketentuan resmi pemerintah."},
            {"key": "C", "text": "Menimbulkan kerugian bobot mati masyarakat (_Deadweight Loss_) karena total kuantitas transaksi yang terealisasi di pasar menjadi lebih sedikit dibanding titik optimum pasar."},
            {"key": "D", "text": "Produsen berlomba-lomba menambah kapasitas pabrik dan meningkatkan volume penawaran barang hingga melimpah ruah di etalase toko."},
            {"key": "E", "text": "Seluruh konsumen dijamin mendapatkan barang dalam jumlah berlebih tanpa perlu mengantre di pasar."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "ANALISIS PASAR ATAS CEILING PRICE ($P_c < P_e$)",
            "latex": "\\begin{aligned} P_c < P_e & \\implies Q_d > Q_s \\implies \\mathbf{\\text{Shortage / Kelangkaan Fisik}} \\\\ \\text{Dampak Lanjutan:} & \\implies \\mathbf{\\text{Antrean Kupon / Black Market}} + \\mathbf{\\text{Deadweight Loss (DWL)}} \\end{aligned}",
            "legend": "• A, B, C BENAR: Dampak umum dari batas harga atas di bawah ekuilibrium<br>• D dan E SALAH: Produsen justru memangkas penawaran ($Q_s$ turun) sehingga timbul antrean dan kelangkaan"
        },
        "hints": {
            "concept": "Ceiling price di bawah ekuilibrium memicu: Shortage / kelangkaan (A), Munculnya pasar gelap (B), dan Terciptanya Deadweight Loss (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "eko-sim-30",
        "materi": "BADAN USAHA & KOPERASI",
        "topic": "Prinsip-Prinsip Koperasi menurut Standar Internasional dan UU No. 25/1992",
        "stem": "Koperasi merupakan badan usaha yang beranggotakan orang-seorang atau badan hukum koperasi dengan melandaskan kegiatannya berdasarkan prinsip koperasi sekaligus gerakan ekonomi rakyat yang berdasar atas asas kekeluargaan. Manakah TIGA prinsip koperasi berikut yang BENAR menurut UU No. 25 Tahun 1992? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Keanggotaan koperasi bersifat sukarela dan terbuka tanpa diskriminasi latar belakang sosial politik."},
            {"key": "B", "text": "Pengelolaan koperasi dilakukan secara demokratis dengan prinsip satu anggota satu suara (_one man one vote_) dalam Rapat Anggota, terlepas dari besar kecilnya simpanan modal."},
            {"key": "C", "text": "Pembagian Sisa Hasil Usaha (SHU) dilakukan secara adil sebanding dengan besarnya jasa usaha yang disumbangkan oleh masing-masing anggota."},
            {"key": "D", "text": "Hak suara dalam Rapat Anggota ditentukan oleh persentase kepemilikan modal saham seperti halnya Perseroan Terbatas (PT)."},
            {"key": "E", "text": "Seluruh keuntungan koperasi wajib diserahkan kepada kas daerah pemerintah kabupaten setempat."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "PRINSIP KOPERASI INDONESIA (PASAL 5 UU NO. 25 TAHUN 1992)",
            "latex": "\\text{Prinsip Koperasi} \\equiv \\begin{cases} \\mathbf{\\text{1. Keanggotaan sukarela \\& terbuka}} \\\\ \\mathbf{\\text{2. Pengelolaan demokratis (1 Anggota = 1 Suara)}} \\\\ \\mathbf{\\text{3. Pembagian SHU sebanding jasa usaha}} \\\\ \\text{4. Pemberian balas jasa terbatas terhadap modal} \\\\ \\text{5. Kemandirian, Pendidikan perkoperasian, Kerjasama antar koperasi} \\end{cases}",
            "legend": "• A, B, C BENAR: Ciri khas demokrasi ekonomi koperasi<br>• D adalah prinsip Perseroan Terbatas (kapitalis)<br>• E SALAH: SHU adalah hak milik anggota koperasi"
        },
        "hints": {
            "concept": "Prinsip koperasi: Keanggotaan sukarela dan terbuka (A), Pengelolaan demokratis one man one vote (B), Pembagian SHU sebanding jasa usaha anggota (C).",
            "execution": "Pilih A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH HOTS (eko-sim-31 to eko-sim-35)
    # -------------------------------------------------------------
    {
        "id": "eko-sim-31",
        "type": "matrix",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Pendekatan Kardinal dan Ordinal dalam Teori Perilaku Konsumen",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai teori perilaku konsumen!",
        "statements": [
            {
                "text": "Dalam pendekatan kardinal, kepuasan konsumen dianggap dapat diukur secara kuantitatif dalam satuan angka pasti yang disebut 'util'.",
                "correct": True
            },
            {
                "text": "Dua kurva indiferensi yang berbeda untuk seorang konsumen yang rasional dapat saling berpotongan di satu titik kepuasan.",
                "correct": False
            },
            {
                "text": "Kemiringan (slope) dari kurva indiferensi mencerminkan Tingkat Substitusi Marjinal (Marginal Rate of Substitution / MRS) antara dua barang.",
                "correct": True
            },
            {
                "text": "Garis Anggaran (Budget Line) akan berotasi memutar ke luar pada satu sumbu jika terjadi penurunan harga pada barang di sumbu tersebut sementara pendapatan tetap.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP TEORI PERILAKU KONSUMEN",
            "latex": "\\text{Kardinal: Kuatitatif (Util)}, \\quad \\text{Ordinal: Kurva Indiferensi (Tidak Berpotongan)}, \\quad \\text{Slope IC} = -\\text{MRS}_{xy}, \\quad \\text{Budget Line Rotate}",
            "legend": "• Pernyataan 1 BENAR: Asumsi dasar pendekatan kardinal Gossen<br>• Pernyataan 2 SALAH: Kurva indiferensi tidak boleh berpotongan karena melanggar aksioma transitivitas preferensi ($A \\succ B$ dan $B \\succ C \\implies A \\succ C$)<br>• Pernyataan 3 BENAR: Definisi baku kemiringan kurva indiferen ($MRS_{xy} = MU_x / MU_y$)<br>• Pernyataan 4 BENAR: Perubahan harga satu barang menyebabkan garis anggaran berotasi"
        },
        "hints": {
            "concept": "Kardinal mengukur dalam satuan util. Kurva indiferensi TIDAK BOLEH saling berpotongan. Slope kurva indiferensi adalah MRS. Budget line berotasi jika harga salah satu barang berubah.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "eko-sim-32",
        "type": "matrix",
        "materi": "STRUKTUR PASAR",
        "topic": "Struktur Pasar: Persaingan Sempurna, Monopoli, dan Oligopoli",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai struktur pasar dan penentuan output!",
        "statements": [
            {
                "text": "Perusahaan monopoli selalu dapat menetapkan harga jual setinggi mungkin tanpa batas karena tidak memiliki pesaing sama sekali di pasar.",
                "correct": False
            },
            {
                "text": "Dalam jangka panjang, perusahaan di pasar persaingan monopolistik hanya memperoleh laba normal karena tidak ada hambatan masuk bagi pesaing baru.",
                "correct": True
            },
            {
                "text": "Diskriminasi harga derajat pertama (first-degree price discrimination) menyerap seluruh surplus konsumen menjadi surplus produsen.",
                "correct": True
            },
            {
                "text": "Pada pasar persaingan sempurna, kurva biaya marjinal (MC) di atas titik AVC minimum merupakan kurva penawaran jangka pendek perusahaan.",
                "correct": True
            }
        ],
        "formula": {
            "title": "EVALUASI STRUKTUR PASAR DAN PENAWARAN",
            "latex": "\\text{Monopolis dibatasi Kurva Permintaan}, \\quad \\text{Monopolistik Jangka Panjang } \\implies \\text{Laba Normal}, \\quad \\text{Diskriminasi Derajat 1: } CS = 0, \\quad \\text{Penawaran PPS: } MC \\ge AVC_{\\min}",
            "legend": "• Pernyataan 1 SALAH: Monopolis tetap dibatasi oleh kurva permintaan konsumen; jika harga dipatok terlalu tinggi konsumen tidak akan membeli<br>• Pernyataan 2 BENAR: Masuknya pendatang baru menggeser kurva permintaan ke kiri hingga bersinggungan dengan AC ($P = AC$)<br>• Pernyataan 3 BENAR: Diskriminasi derajat 1 mengenakan harga setinggi kerelaan membayar (willingness to pay) tiap individu sehingga $CS = 0$<br>• Pernyataan 4 BENAR: Definisi baku kurva penawaran jangka pendek persaingan sempurna"
        },
        "hints": {
            "concept": "Monopoli dibatasi kurva permintaan pasar. Pasar monopolistik jangka panjang menghasilkan laba normal. Diskriminasi derajat 1 menyerap seluruh surplus konsumen. Kurva MC di atas AVC minimum adalah kurva penawaran PPS.",
            "execution": "Pernyataan 1: Salah; Pernyataan 2: Benar; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "eko-sim-33",
        "type": "matrix",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Indikator Makroekonomi: PDB, Pendapatan Per Kapita, dan Ketenagakerjaan",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai indikator ekonomi makro!",
        "statements": [
            {
                "text": "Produk Nasional Bruto (PNB) Indonesia akan bernilai lebih besar daripada Produk Domestik Bruto (PDB) jika pendapatan neto faktor luar negeri bernilai negatif.",
                "correct": False
            },
            {
                "text": "Pendapatan Disposabel (Disposable Income) adalah pendapatan personal yang siap dibelanjakan setelah dikurangi dengan pajak langsung seperti PPh.",
                "correct": True
            },
            {
                "text": "Seseorang yang sedang aktif mencari pekerjaan pertama kali setelah lulus kuliah dikategorikan ke dalam kelompok pengangguran friksional.",
                "correct": True
            },
            {
                "text": "Tingkat Partisipasi Angkatan Kerja (TPAK) dihitung dengan membagi jumlah pengangguran dengan total seluruh penduduk di suatu negara.",
                "correct": False
            }
        ],
        "formula": {
            "title": "KONSEP INDIKATOR MAKROEKONOMI",
            "latex": "\\text{PNB} = \\text{PDB} + \\text{FPNLN}, \\quad DI = PI - \\text{Pajak Langsung}, \\quad \\text{TPAK} = \\frac{\\text{Angkatan Kerja}}{\\text{Usia Kerja (15+)}} \\times 100\\%",
            "legend": "• Pernyataan 1 SALAH: Jika FPNLN negatif, maka PNB < PDB (kondisi umum negara berkembang)<br>• Pernyataan 2 BENAR: Definisi baku Disposable Income ($Y_d = C + S$)<br>• Pernyataan 3 BENAR: Fresh graduate yang mencari kerja adalah pengangguran friksional<br>• Pernyataan 4 SALAH: TPAK = (Angkatan Kerja / Penduduk Usia Kerja 15 Tahun ke Atas) x 100%"
        },
        "hints": {
            "concept": "PNB = PDB + FPNLN, jika FPNLN negatif maka PNB lebih kecil dari PDB. Disposable Income = PI - Pajak Langsung. Fresh graduate mencari kerja = pengangguran friksional. TPAK = Angkatan kerja / Penduduk usia kerja.",
            "execution": "Pernyataan 1: Salah; Pernyataan 2: Benar; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "eko-sim-34",
        "type": "matrix",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Siklus Akuntansi: Persamaan Dasar, Saldo Normal, dan Laporan Keuangan",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai siklus dan prinsip dasar akuntansi!",
        "statements": [
            {
                "text": "Akun Beban dan akun Prive memiliki saldo normal di sebelah Debit, sehingga penambahan pada kedua akun tersebut dicatat di sisi Debit.",
                "correct": True
            },
            {
                "text": "Pembelian perlengkapan kantor secara kredit akan menyebabkan Aset (Perlengkapan) bertambah dan Ekuitas (Modal) berkurang.",
                "correct": False
            },
            {
                "text": "Laporan Posisi Keuangan (Neraca) menyajikan informasi mengenai kinerja operasional pendapatan dan beban perusahaan selama satu periode berjalan.",
                "correct": False
            },
            {
                "text": "Keseimbangan jumlah debit dan kredit pada Neraca Saldo (Trial Balance) belum tentu menjamin pembukuan bebas dari kesalahan pencatatan transaksi.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PERSAMAAN DASAR AKUNTANSI DAN SALDO NORMAL",
            "latex": "\\text{Aset} + \\text{Beban} + \\text{Prive} = \\text{Liabilitas} + \\text{Ekuitas} + \\text{Pendapatan} \\quad (\\text{Kiri: Debit}, \\text{ Kanan: Kredit})",
            "legend": "• Pernyataan 1 BENAR: Saldo normal Beban dan Prive adalah Debit<br>• Pernyataan 2 SALAH: Beli perlengkapan kredit menambah Aset (Perlengkapan) dan menambah Liabilitas (Utang Usaha), modal tidak berubah<br>• Pernyataan 3 SALAH: Pendapatan dan beban disajikan di Laporan Laba Rugi, bukan Neraca<br>• Pernyataan 4 BENAR: Neraca saldo seimbang bisa saja mengandung kesalahan transaksi terlewat, salah akun, atau kesalahan kompensasi"
        },
        "hints": {
            "concept": "Beban dan prive bersaldo normal Debit. Beli kredit menambah aset dan utang (bukan mengurangi modal). Laba rugi menyajikan pendapatan dan beban (neraca menyajikan aset, utang, modal). Neraca saldo seimbang belum tentu benar (bisa ada omisi/salah akun).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    },
    {
        "id": "eko-sim-35",
        "type": "matrix",
        "materi": "LEMBAGA KEUANGAN & PASAR MODAL",
        "topic": "Lembaga Regulasi Keuangan: Bank Indonesia, OJK, dan LPS",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai tugas dan wewenang lembaga pengatur stabilitas sistem keuangan di Indonesia!",
        "statements": [
            {
                "text": "Bank Indonesia bertugas merumuskan dan melaksanakan kebijakan moneter, mengatur kelancaran sistem pembayaran, serta mengelola stabilitas makroprudensial.",
                "correct": True
            },
            {
                "text": "Otoritas Jasa Keuangan (OJK) bertugas melakukan pengawasan mikroprudensial terhadap operasional lembaga perbankan, pasar modal, dan industri keuangan non-bank.",
                "correct": True
            },
            {
                "text": "Lembaga Penjamin Simpanan (LPS) menjamin seluruh simpanan nasabah di bank tanpa batas nominal maksimal meskipun suku bunga simpanan melebihi batas penjaminan.",
                "correct": False
            },
            {
                "text": "Komite Stabilitas Sistem Keuangan (KSSK) terdiri atas Kementerian Keuangan, Bank Indonesia, OJK, dan LPS untuk mengkoordinasikan pencegahan dan penanganan krisis.",
                "correct": True
            }
        ],
        "formula": {
            "title": "STRUKTUR DAN FUNGSI JARING PENGAWAS KEUANGAN (KSSK)",
            "latex": "\\text{KSSK} = \\begin{cases} \\text{Kemenkeu:} & \\text{Kebijakan Fiskal} \\\\ \\text{Bank Indonesia:} & \\text{Moneter, Sistem Pembayaran, Makroprudensial} \\\\ \\text{OJK:} & \\text{Pengawasan Mikroprudensial Bank, Pasar Modal, IKNB} \\\\ \\text{LPS:} & \\text{Penjamin Simpanan Nasabah (Maks Rp 2 Miliar, Syarat 3T)} \\end{cases}",
            "legend": "• Pernyataan 1 BENAR: Tugas pokok Bank Indonesia UU No. 23/1999 jo UU P2SK<br>• Pernyataan 2 BENAR: Wewenang OJK UU No. 21/2011<br>• Pernyataan 3 SALAH: LPS hanya menjamin simpanan maksimal Rp 2 Miliar per nasabah per bank dengan memenuhi syarat 3T (Tercatat, Tidak melebihi suku bunga LPS, Tidak merugikan bank)<br>• Pernyataan 4 BENAR: Empat pilar anggota KSSK"
        },
        "hints": {
            "concept": "BI = moneter, sistem pembayaran, makroprudensial. OJK = pengawasan mikroprudensial bank & non-bank. LPS = penjaminan simpanan maks 2 miliar dengan syarat 3T (bukan tanpa batas). KSSK = Kemenkeu, BI, OJK, LPS.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    }
]
