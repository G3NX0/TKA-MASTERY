# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Ekonomi (SMA/MA)
Dataset: Latihan Tingkat Medium (25 Authentic Questions, eko-lat-m-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

EKONOMI_MEDIUM_ITEMS = [
    {
        "id": "eko-lat-m-01",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Pengaruh Pajak Spesifik Terhadap Titik Keseimbangan Pasar",
        "stem": "Diketahui fungsi permintaan suatu barang adalah $Q_d = 100 - 2P$ dan fungsi penawaran sebelum pajak adalah $Q_s = -20 + 2P$. Pemerintah mengenakan pajak spesifik sebesar $t = 6$ per unit barang yang dijual. Titik harga dan kuantitas keseimbangan pasar yang baru setelah pajak ($P_e', Q_e'$) adalah...",
        "correct": "$P_e' = 33$ dan $Q_e' = 34$, di mana harga naik dari $P_e = 30$ dan kuantitas turun dari $Q_e = 40$.",
        "distractors": [
            "$P_e' = 36$ dan $Q_e' = 28$, akibat pembebanan seluruh pajak langsung ke konsumen tanpa pergeseran.",
            "$P_e' = 27$ dan $Q_e' = 46$, karena produsen menanggung subsidi harga di pasar persaingan.",
            "$P_e' = 30$ dan $Q_e' = 40$, karena pajak spesifik tidak mengubah titik potong kurva penawaran.",
            "$P_e' = 35$ dan $Q_e' = 30$, hasil perhitungan kesalahan inversi gradien fungsi penawaran."
        ],
        "formula": {
            "title": "KESEIMBANGAN PASAR SETELAH PAJAK SPESIFIK",
            "latex": "\\begin{aligned} Q_s' & = -20 + 2(P - 6) = -20 + 2P - 12 = -32 + 2P \\\\ Q_d = Q_s' & \\implies 100 - 2P = -32 + 2P \\implies 4P = 132 \\implies \\mathbf{P_e' = 33} \\\\ Q_e' & = 100 - 2(33) = 100 - 66 = \\mathbf{34} \\end{aligned}",
            "legend": "• Beban Pajak Konsumen ($t_k$): $P_e' - P_e = 33 - 30 = 3$ per unit<br>• Beban Pajak Produsen ($t_p$): $t - t_k = 6 - 3 = 3$ per unit<br>• Total Penerimaan Pajak Pemerintah: $T = t \\times Q_e' = 6 \\times 34 = 204$"
        },
        "hints": {
            "concept": "Pajak spesifik t menggeser kurva penawaran: ganti P dengan (P - t) pada fungsi Qs. Samakan Qd = Qs'.",
            "execution": "Qs' = -20 + 2(P - 6) = -32 + 2P. 100 - 2P = -32 + 2P -> 4P = 132 -> P = 33, Q = 100 - 2(33) = 34."
        }
    },
    {
        "id": "eko-lat-m-02",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Perhitungan Pendapatan Nasional Pendekatan Pengeluaran",
        "stem": "Data makroekonomi suatu negara dalam satu tahun anggaran menunjukkan:\n- Pengeluaran Konsumsi Rumah Tangga ($C$) = Rp 450 Triliun\n- Investasi Domestik Bruto Swasta ($I$) = Rp 180 Triliun\n- Pengeluaran Konsumsi & Belanja Pemerintah ($G$) = Rp 220 Triliun\n- Nilai Ekspor Barang & Jasa ($X$) = Rp 110 Triliun\n- Nilai Impor Barang & Jasa ($M$) = Rp 90 Triliun\n- Pembayaran Sewa Tanah ($r$) = Rp 85 Triliun\n- Pembayaran Upah Gaji ($w$) = Rp 240 Triliun\nBerdasarkan data tersebut, besarnya Produk Domestik Bruto (PDB) jika dihitung menggunakan Pendekatan Pengeluaran adalah...",
        "correct": "Rp 870 Triliun, dihitung dari formula $Y = C + I + G + (X - M) = 450 + 180 + 220 + (110 - 90) = 870$ Triliun.",
        "distractors": [
            "Rp 1.195 Triliun, hasil penjumlahan seluruh variabel data secara membabi buta termasuk sewa dan upah.",
            "Rp 850 Triliun, hasil perhitungan tanpa memperhitungkan neraca perdagangan ekspor neto.",
            "Rp 890 Triliun, hasil kesalahan menambahkan nilai impor dan mengurangkan nilai ekspor.",
            "Rp 630 Triliun, hasil penjumlahan sewa tanah dan upah gaji pada pendekatan pendapatan."
        ],
        "formula": {
            "title": "PENDEKATAN PENGELUARAN PENDAPATAN NASIONAL",
            "latex": "Y = C + I + G + (X - M) = 450 + 180 + 220 + (110 - 90) = 850 + 20 = 870 \\text{ Triliun}",
            "legend": "• Komponen Pengeluaran: Konsumsi Rumah Tangga ($C$), Investasi ($I$), Belanja Pemerintah ($G$), Ekspor Bersih ($X - M$)<br>• Data sewa ($r$) dan upah ($w$) adalah pengecoh milik Pendekatan Pendapatan ($Y = r + w + i + p$)"
        },
        "hints": {
            "concept": "Gunakan formula pendekatan pengeluaran: Y = C + I + G + (X - M). Abaikan sewa dan upah.",
            "execution": "Y = 450 + 180 + 220 + (110 - 90) = 850 + 20 = 870 Triliun."
        }
    },
    {
        "id": "eko-lat-m-03",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Keseimbangan Konsumen Pendekatan Ordinal (Indifference Curve & Budget Line)",
        "stem": "Dalam teori perilaku konsumen pendekatan ordinal, seorang konsumen mengalokasikan anggarannya untuk mengonsumsi barang $X$ dan barang $Y$. Kondisi ekuilibrium kepuasan maksimum konsumen (Consumer Equilibrium) tercapai pada saat...",
        "correct": "Kurva Indiferen (Indifference Curve) bersinggungan tepat dengan Garis Anggaran (Budget Line), di mana Tingkat Substitusi Marjinal sama dengan rasio harga kedua barang ($MRS_{xy} = \\frac{P_x}{P_y}$).",
        "distractors": [
            "Kurva Indiferen memotong tegak lurus Garis Anggaran pada titik batas sumbu horizontal barang X.",
            "Total Utility dari barang X sama persis dengan Total Utility dari barang Y tanpa mempedulikan harga pasar.",
            "Seluruh pendapatan konsumen dihabiskan hanya untuk membeli satu jenis barang yang memiliki harga termurah.",
            "Kurva Indiferen berada di posisi paling bawah mendekati titik origin nol sumbu koordinat."
        ],
        "formula": {
            "title": "KONDISI KESEIMBANGAN KONSUMEN PENDEKATAN ORDINAL",
            "latex": "\\text{Slope Kurva Indiferen} = \\text{Slope Garis Anggaran} \\implies MRS_{xy} = \\frac{MU_x}{MU_y} = \\frac{P_x}{P_y}",
            "legend": "• Indifference Curve: Menggambarkan kombinasi konsumsi dua barang yang memberikan kepuasan sama<br>• Budget Line: Batas kemampuan finansial ($I = P_x \\cdot X + P_y \\cdot Y$)<br>• Titik Singgung: Titik kepuasan tertinggi yang dapat dijangkau oleh anggaran yang tersedia"
        },
        "hints": {
            "concept": "Keseimbangan konsumen ordinal tercapai saat Indifference Curve bersinggungan dengan Budget Line: MRSxy = Px / Py.",
            "execution": "Pilih: Kurva Indiferen bersinggungan dengan Garis Anggaran di mana MRSxy = Px / Py."
        }
    },
    {
        "id": "eko-lat-m-04",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Hubungan Kurva Biaya Marjinal (MC) dan Biaya Rata-Rata (AC)",
        "stem": "Dalam teori biaya produksi jangka pendek, kurva Biaya Marjinal (Marginal Cost / $MC$) memiliki hubungan geometris dan matematis yang unik dengan kurva Biaya Total Rata-Rata (Average Cost / $AC$). Hubungan yang benar antara kedua kurva tersebut adalah...",
        "correct": "Kurva $MC$ memotong kurva $AC$ tepat pada titik minimum kurva $AC$; ketika $MC < AC$, kurva $AC$ sedang menurun, dan ketika $MC > AC$, kurva $AC$ sedang meningkat.",
        "distractors": [
            "Kurva $MC$ selalu berada di atas kurva $AC$ di seluruh rentang jumlah output produksi barang.",
            "Kurva $MC$ memotong kurva $AC$ tepat pada titik maksimum kurva $AC$ saat terjadi kelebihan kapasitas.",
            "Kurva $MC$ berbentuk garis lurus horizontal sedangkan kurva $AC$ berbentuk garis lurus vertikal.",
            "Kurva $MC$ memotong kurva $AC$ tepat pada titik potong sumbu vertikal biaya awal nol."
        ],
        "formula": {
            "title": "HUBUNGAN MATEMATIS BIAYA MARJINAL (MC) DAN AVERAGE COST (AC)",
            "latex": "\\begin{aligned} MC < AC & \\implies \\frac{d(AC)}{dQ} < 0 \\implies AC \\text{ Menurun} \\\\ \\mathbf{MC = AC} & \\implies \\frac{d(AC)}{dQ} = 0 \\implies \\mathbf{AC \\text{ Minimum}} \\\\ MC > AC & \\implies \\frac{d(AC)}{dQ} > 0 \\implies AC \\text{ Meningkat} \\end{aligned}",
            "legend": "• Analog Nilai Ujian: Jika nilai ujian terakhir ($MC$) di bawah rata-rata ($AC$), maka nilai rata-rata akan turun; jika di atasnya, rata-rata naik"
        },
        "hints": {
            "concept": "Kurva MC memotong kurva AC tepat di titik minimum AC. Saat MC < AC maka AC turun, saat MC > AC maka AC naik.",
            "execution": "Pilih opsi yang menjelaskan kurva MC memotong AC tepat di titik minimum AC."
        }
    },
    {
        "id": "eko-lat-m-05",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Persamaan Pertukaran Teori Kuantitas Uang Irving Fisher",
        "stem": "Berdasarkan Teori Kuantitas Uang yang dirumuskan oleh Irving Fisher ($M \\cdot V = P \\cdot T$), dalam suatu perekonomian jumlah uang yang beredar adalah $M = \\text{Rp } 200 \\text{ Triliun}$, kecepatan perputaran uang adalah $V = 8$ kali per tahun, dan volume total transaksi barang dan jasa adalah $T = 400 \\text{ Juta unit}$. Jika kecepatan perputaran uang ($V$) dan volume transaksi ($T$) diasumsikan konstan, dampak terhadap tingkat harga ($P$) jika Bank Sentral menggandakan jumlah uang beredar ($M$) menjadi Rp 400 Triliun adalah...",
        "correct": "Tingkat harga ($P$) naik proporsional dua kali lipat dari Rp 4.000.000,- menjadi Rp 8.000.000,- per unit barang.",
        "distractors": [
            "Tingkat harga ($P$) tetap stabil tidak berubah karena transaksi riil mengimbangi peredaran uang.",
            "Tingkat harga ($P$) turun menjadi setengahnya karena daya beli uang mengalami apresiasi nilai.",
            "Tingkat harga ($P$) melonjak sepuluh kali lipat akibat fenomena hiperinflasi tak terkendali.",
            "Volume transaksi barang ($T$) otomatis berlipat ganda menjadi 800 juta unit tanpa kenaikan harga."
        ],
        "formula": {
            "title": "TEORI KUANTITAS UANG IRVING FISHER (EQUATION OF EXCHANGE)",
            "latex": "M \\cdot V = P \\cdot T \\implies P = \\frac{M \\cdot V}{T} = \\frac{200 \\times 8}{400} = 4 \\implies \\text{Jika } M' = 400 \\implies P' = \\frac{400 \\times 8}{400} = 8",
            "legend": "• $M$: Jumlah Uang Beredar (Money Supply)<br>• $V$: Kecepatan Perputaran Uang (Velocity of Money)<br>• $P$: Tingkat Harga Umum (Price Level)<br>• $T$: Volume Transaksi Barang & Jasa<br>• Asumsi Fisher: $V$ dan $T$ relatif konstan dalam jangka pendek, sehingga \\%\\Delta M = \\%\\Delta P$"
        },
        "hints": {
            "concept": "Dalam persamaan M . V = P . T, jika V dan T konstan, perubahan M berbanding lurus proporsional dengan perubahan P.",
            "execution": "P awal = (200 * 8) / 400 = 4 juta. Jika M naik 2x lipat jadi 400, maka P juga naik 2x lipat jadi 8 juta."
        }
    },
    {
        "id": "eko-lat-m-06",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Pengganda Uang (Money Multiplier) dan Giro Wajib Minimum (GWM)",
        "stem": "Bank sentral menetapkan Giro Wajib Minimum (GWM / Reserve Requirement Ratio) sebesar $8\\%$. Jika seorang nasabah menyetorkan dana awal sebesar Rp 50.000.000,- sebagai giro tunai ke dalam sistem perbankan dan diasumsikan masyarakat tidak memegang uang kartal (seluruh uang beredar dalam bentuk simpanan bank), jumlah penciptaan uang giral maksimum (Money Multiplier Effect) yang dapat terbentuk di dalam sistem perekonomian adalah...",
        "correct": "Rp 625.000.000,-, dihitung dari formula angka pengganda uang $M = \\frac{1}{\\text{GWM}} \\times \\text{Setoran Awal} = \\frac{1}{0,08} \\times 50.000.000 = 12,5 \\times 50.000.000$.",
        "distractors": [
            "Rp 400.000.000,-, hasil perkalian setoran awal dengan suku bunga acuan moneter nasional.",
            "Rp 54.000.000,-, hasil penambahan setoran awal dengan margin bunga sebesar delapan persen.",
            "Rp 500.000.000,-, hasil perhitungan angka pengganda dengan pembulatan rasio sepuluh persen.",
            "Rp 50.000.000,-, karena bank komersial dilarang meminjamkan dana simpanan kepada nasabah lain."
        ],
        "formula": {
            "title": "FORMULA ANGKA PENGGANDA UANG SEDERHANA",
            "latex": "\\text{Multiplier (} m \\text{)} = \\frac{1}{RR} = \\frac{1}{0,08} = 12,5 \\implies \\Delta M = m \\times \\text{Deposit Awal} = 12,5 \\times 50.000.000 = 625.000.000",
            "legend": "• $RR$ (Reserve Requirement): Giro Wajib Minimum yang wajib disimpan bank di rekening Bank Indonesia<br>• Penciptaan Uang Giral: Terjadi melalui rantai penyaluran kredit dan penyimpanan kembali di sistem perbankan komersial"
        },
        "hints": {
            "concept": "Angka pengganda uang sederhana m = 1 / GWM. m = 1 / 0.08 = 12.5. Total uang = 12.5 * 50 juta = 625 juta.",
            "execution": "Pilih: Rp 625.000.000,-."
        }
    },
    {
        "id": "eko-lat-m-07",
        "materi": "STRUKTUR PASAR",
        "topic": "Penentuan Laba Maksimum Monopoli dan Deadweight Loss",
        "stem": "Sebuah perusahaan monopoli menghadapi fungsi permintaan pasar $P = 100 - Q$ dan memiliki fungsi biaya total $TC = 20Q + Q^2$. Untuk memaksimumkan laba perusahaan (kondisi $MR = MC$), tingkat kuantitas output ($Q$), harga jual keseimbangan ($P$), dan laba maksimum ($\\pi$) yang diperoleh perusahaan monopoli tersebut adalah...",
        "correct": "$Q = 20$ unit, $P = \\text{Rp } 80,-$, dan laba maksimum $\\pi = \\text{Rp } 800,-$.",
        "distractors": [
            "$Q = 40$ unit, $P = \\text{Rp } 60,-$, dan laba maksimum $\\pi = \\text{Rp } 600,-$.",
            "$Q = 30$ unit, $P = \\text{Rp } 70,-$, dan laba maksimum $\\pi = \\text{Rp } 900,-$.",
            "$Q = 25$ unit, $P = \\text{Rp } 75,-$, dan laba maksimum $\\pi = \\text{Rp } 750,-$.",
            "$Q = 15$ unit, $P = \\text{Rp } 85,-$, dan laba maksimum $\\pi = \\text{Rp } 525,-$."
        ],
        "formula": {
            "title": "KESEIMBANGAN LABA MAKSIMUM PERUSAHAAN MONOPOLI",
            "latex": "\\begin{aligned} TR & = P \\cdot Q = (100 - Q)Q = 100Q - Q^2 \\\\ MR & = \\frac{d(TR)}{dQ} = 100 - 2Q \\\\ MC & = \\frac{d(TC)}{dQ} = 20 + 2Q \\\\ MR = MC & \\implies 100 - 2Q = 20 + 2Q \\implies 4Q = 80 \\implies \\mathbf{Q = 20} \\\\ P & = 100 - 20 = \\mathbf{\\text{Rp } 80,-} \\\\ \\pi & = TR - TC = (80 \\times 20) - (20(20) + 20^2) = 1.600 - (400 + 400) = \\mathbf{\\text{Rp } 800,-} \\end{aligned}",
            "legend": "• Syarat Laba Maksimum: $MR = MC$<br>• Harga Monopoli ($P$) selalu di atas $MC$ ($P > MC$) yang menimbulkan kerugian bobot mati (Deadweight Loss / DWL)"
        },
        "hints": {
            "concept": "Laba maksimum tercapai saat MR = MC. Turunkan TR untuk memperoleh MR, turunkan TC untuk memperoleh MC, lalu samakan untuk mencari Q, P, dan laba.",
            "execution": "MR = 100 - 2Q, MC = 20 + 2Q. 100 - 2Q = 20 + 2Q -> 4Q = 80 -> Q = 20. P = 100 - 20 = 80. Laba = TR - TC = 1.600 - 800 = 800."
        }
    },
    {
        "id": "eko-lat-m-08",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Jurnal Penyesuaian Beban Penyusutan Aset Tetap Metode Garis Lurus",
        "stem": "Pada tanggal 1 Januari 2024, perusahaan membeli peralatan operasional seharga Rp 60.000.000,- dengan estimasi masa manfaat 5 tahun dan nilai residu (sisa) diperkirakan sebesar Rp 10.000.000,-. Penyusutan dihitung menggunakan metode garis lurus. Jurnal penyesuaian (AJP) yang wajib dibuat pada tanggal 31 Desember 2024 adalah...",
        "correct": "Beban Penyusutan Peralatan (Debit) Rp 10.000.000,- dan Akumulasi Penyusutan Peralatan (Kredit) Rp 10.000.000,-.",
        "distractors": [
            "Akumulasi Penyusutan Peralatan (Debit) Rp 10.000.000,- dan Peralatan (Kredit) Rp 10.000.000,-.",
            "Beban Penyusutan Peralatan (Debit) Rp 12.000.000,- dan Kas (Kredit) Rp 12.000.000,-.",
            "Peralatan (Debit) Rp 50.000.000,- dan Beban Penyusutan Peralatan (Kredit) Rp 50.000.000,-.",
            "Beban Operasional (Debit) Rp 60.000.000,- dan Modal Usaha (Kredit) Rp 60.000.000,-."
        ],
        "formula": {
            "title": "PENYUSUTAN METODE GARIS LURUS (STRAIGHT-LINE METHOD)",
            "latex": "\\text{Beban Penyusutan per Tahun} = \\frac{\\text{Harga Perolehan} - \\text{Nilai Residu}}{\\text{Umur Ekonomis}} = \\frac{60.000.000 - 10.000.000}{5} = \\text{Rp } 10.000.000,-",
            "legend": "• Akun Akumulasi Penyusutan: Merupakan akun kontra-aset (contra-asset account) yang bersaldo normal Kredit<br>• Nilai Buku Bersih (Book Value) per 31 Des: Rp 60 Juta - Rp 10 Juta = Rp 50 Juta"
        },
        "hints": {
            "concept": "Penyusutan = (Harga Perolehan - Nilai Sisa) / Umur = (60 jt - 10 jt) / 5 = 10 jt. Jurnal: Beban Penyusutan (D) dan Akumulasi Penyusutan (K).",
            "execution": "Pilih: Beban Penyusutan Peralatan (Debit) Rp 10.000.000,- dan Akumulasi Penyusutan Peralatan (Kredit) Rp 10.000.000,-."
        }
    },
    {
        "id": "eko-lat-m-09",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Teori Keunggulan Komparatif David Ricardo dan Dasar Tukar Internasional",
        "stem": "Diberikan tabel produktivitas satu orang tenaga kerja per hari di dua negara:\n- Indonesia: 10 meter kain ATAU 5 unit sepatu (Dasar Tukar Domestik: 1 sepatu = 2 meter kain)\n- Vietnam: 6 meter kain ATAU 6 unit sepatu (Dasar Tukar Domestik: 1 sepatu = 1 meter kain)\nBerdasarkan Teori Keunggulan Komparatif David Ricardo, pola spesialisasi dan Dasar Tukar Internasional (DTI) yang menguntungkan kedua negara adalah...",
        "correct": "Indonesia berspesialisasi memproduksi kain (biaya peluang sepatu lebih mahal: 2 kain > 1 kain) dan Vietnam berspesialisasi memproduksi sepatu, dengan rentang DTI yang saling menguntungkan: $1 \\text{ unit sepatu bernilai antara } 1 \\text{ s.d. } 2 \\text{ meter kain}$.",
        "distractors": [
            "Indonesia dan Vietnam tidak dapat melakukan perdagangan karena Vietnam memiliki keunggulan mutlak di semua bidang.",
            "Indonesia berspesialisasi memproduksi sepatu dan Vietnam berspesialisasi memproduksi kain, dengan nilai tukar 1 sepatu = 3 meter kain.",
            "Kedua negara berspesialisasi memproduksi kain secara serentak dan menghentikan seluruh produksi sepatu.",
            "Vietnam berspesialisasi memproduksi kain dengan syarat Indonesia membayar bea tarif impor sebesar seratus persen."
        ],
        "formula": {
            "title": "TEORI KEUNGGULAN KOMPARATIF DAVID RICARDO",
            "latex": "\\begin{aligned} \\text{Biaya Peluang 1 Sepatu di Indonesia:} & \\quad \\frac{10}{5} = 2 \\text{ Kain} \\\\ \\text{Biaya Peluang 1 Sepatu di Vietnam:} & \\quad \\frac{6}{6} = 1 \\text{ Kain (Lebih Murah!)} \\implies \\text{Vietnam Spesialisasi Sepatu} \\\\ \\text{Rentang DTI Saling Menguntungkan:} & \\quad 1 \\text{ Kain} < 1 \\text{ Sepatu} < 2 \\text{ Kain} \\end{aligned}",
            "legend": "• Keunggulan Komparatif dicapai pada barang dengan biaya peluang (opportunity cost) terkecil"
        },
        "hints": {
            "concept": "Biaya peluang 1 sepatu di Vietnam adalah 1 kain (lebih murah dari Indo yang 2 kain). Vietnam spesialisasi sepatu, Indonesia spesialisasi kain. Rentang DTI: 1 sepatu = 1 s.d. 2 kain.",
            "execution": "Pilih: Indonesia spesialisasi kain, Vietnam spesialisasi sepatu, rentang DTI: 1 sepatu di antara 1 s.d. 2 meter kain."
        }
    },
    {
        "id": "eko-lat-m-10",
        "materi": "BADAN USAHA & KOPERASI",
        "topic": "Kalkulasi Pembagian Sisa Hasil Usaha (SHU) Anggota",
        "stem": "Koperasi Simpan Pinjam \"Makmur Sejahtera\" memperoleh SHU tahun berjalan sebesar Rp 80.000.000,-. Berdasarkan Anggaran Dasar/Anggaran Rumah Tangga (AD/ART), alokasi SHU ditetapkan:\n- Jasa Modal = $25\\%$\n- Jasa Anggota (Pinjaman) = $30\\%$\nTotal simpanan seluruh anggota adalah Rp 200.000.000,- dan total akumulasi pinjaman anggota adalah Rp 300.000.000,-. Pak Budi seorang anggota memiliki total simpanan (pokok + wajib) sebesar Rp 10.000.000,- dan telah meminjam dana sebesar Rp 15.000.000,- selama tahun berjalan. Total SHU yang diterima Pak Budi adalah...",
        "correct": "Rp 2.200.000,-, terdiri atas Jasa Modal Rp 1.000.000,- dan Jasa Pinjaman Rp 1.200.000,-.",
        "distractors": [
            "Rp 1.800.000,-, hasil perhitungan jasa modal tanpa memperhitungkan kontribusi jasa pinjaman.",
            "Rp 2.500.000,-, hasil pembagian SHU sama rata berdasarkan persentase simpanan murni.",
            "Rp 3.100.000,-, hasil kesalahan perkalian rasio simpanan terhadap total laba kotor koperasi.",
            "Rp 1.500.000,-, hasil potongan pajak bunga simpanan anggota perorangan."
        ],
        "formula": {
            "title": "KALKULASI RINCIAN SHU PAK BUDI",
            "latex": "\\begin{aligned} \\text{Total Bagian SHU Modal} & = 25\\% \\times 80.000.000 = \\text{Rp } 20.000.000 \\\\ \\text{Total Bagian SHU Pinjaman} & = 30\\% \\times 80.000.000 = \\text{Rp } 24.000.000 \\\\ \\text{Jasa Modal Budi} & = \\frac{10.000.000}{200.000.000} \\times 20.000.000 = \\mathbf{1.000.000} \\\\ \\text{Jasa Pinjaman Budi} & = \\frac{15.000.000}{300.000.000} \\times 24.000.000 = \\mathbf{1.200.000} \\\\ \\text{Total SHU Budi} & = 1.000.000 + 1.200.000 = \\mathbf{2.200.000} \\end{aligned}",
            "legend": "• Rasio Simpanan Budi: $10/200 = 5\\% \\implies 5\\% \\times 20 \\text{ Jt} = 1 \\text{ Jt}$<br>• Rasio Pinjaman Budi: $15/300 = 5\\% \\implies 5\\% \\times 24 \\text{ Jt} = 1,2 \\text{ Jt}$"
        },
        "hints": {
            "concept": "Jasa modal Budi = (10/200) * (25% * 80jt) = 0.05 * 20jt = 1.000.000. Jasa pinjaman = (15/300) * (30% * 80jt) = 0.05 * 24jt = 1.200.000. Total = 2.200.000.",
            "execution": "Pilih: Rp 2.200.000,-."
        }
    },
    {
        "id": "eko-lat-m-11",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Kalkulasi Laju Inflasi Berdasarkan Indeks Harga Konsumen (IHK)",
        "stem": "Data Badan Pusat Statistik (BPS) mencatat Indeks Harga Konsumen (IHK) suatu kota pada akhir bulan Desember 2023 adalah $112,50$ dan pada akhir bulan Desember 2024 naik menjadi $118,125$. Laju inflasi tahunan kota tersebut pada tahun 2024 serta tingkat keparahannya adalah...",
        "correct": "$5,0\\%$, tergolong ke dalam kategori Inflasi Ringan (di bawah $10\\%$ per tahun).",
        "distractors": [
            "$5,625\\%$, tergolong ke dalam kategori Inflasi Sedang (antara $10\\%$ sampai $30\\%$ per tahun).",
            "$8,0\\%$, tergolong ke dalam kategori Inflasi Berat (antara $30\\%$ sampai $100\\%$ per tahun).",
            "$12,5\\%$, tergolong ke dalam kategori Hiperinflasi (di atas $100\\%$ per tahun).",
            "$3,2\\%$, tergolong ke dalam kategori Deflasi Negatif berkesinambungan."
        ],
        "formula": {
            "title": "FORMULA KALKULASI LAJU INFLASI",
            "latex": "\\text{Laju Inflasi}_t = \\frac{\\text{IHK}_t - \\text{IHK}_{t-1}}{\\text{IHK}_{t-1}} \\times 100\\% = \\frac{118,125 - 112,50}{112,50} \\times 100\\% = \\frac{5,625}{112,50} \\times 100\\% = \\mathbf{5,0\\%}",
            "legend": "• Tingkat Keparahan Inflasi: Ringan (< 10%), Sedang (10% - 30%), Berat (30% - 100%), Hiperinflasi (> 100%)"
        },
        "hints": {
            "concept": "Laju inflasi = ((IHK_t - IHK_t-1) / IHK_t-1) * 100%. (118.125 - 112.5) / 112.5 = 5.625 / 112.5 = 0.05 = 5.0%. Inflasi di bawah 10% adalah inflasi ringan.",
            "execution": "Pilih: 5,0%, tergolong ke dalam kategori Inflasi Ringan."
        }
    },
    {
        "id": "eko-lat-m-12",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Kalkulasi Koefisien Elastisitas Titik Menggunakan Turunan Parsial",
        "stem": "Fungsi permintaan sebuah produk barang elektronik dirumuskan sebagai $Q_d = 200 - 4P^2$. Pada tingkat harga pasar $P = 5$, nilai koefisien elastisitas harga permintaan titik (Point Elasticity of Demand) serta sifat elastisitasnya adalah...",
        "correct": "$E_d = -2,0$ (Elastis, karena $|E_d| = 2 > 1$), di mana kenaikan harga sebesar $1\\%$ akan menurunkan jumlah permintaan barang sebesar $2\\%$.",
        "distractors": [
            "$E_d = -0,5$ (Inelastis, karena $|E_d| < 1$), di mana persentase perubahan kuantitas lebih kecil dari persentase harga.",
            "$E_d = -1,0$ (Elastis Uniter), di mana persentase perubahan harga dan kuantitas sama persis.",
            "$E_d = -4,0$ (Elastis Sempurna), di mana permintaan barang sangat rentan terhadap perubahan substitusi.",
            "$E_d = 0$ (Inelastis Sempurna), di mana kurva permintaan berbentuk garis tegak lurus."
        ],
        "formula": {
            "title": "FORMULA ELASTISITAS TITIK DENGAN TURUNAN",
            "latex": "\\begin{aligned} Q_d(5) & = 200 - 4(5^2) = 200 - 100 = 100 \\\\ \\frac{dQ}{dP} & = -8P \\implies \\left. \\frac{dQ}{dP} \\right|_{P=5} = -8(5) = -40 \\\\ E_d & = \\frac{dQ}{dP} \\times \\frac{P}{Q} = -40 \\times \\frac{5}{100} = \\frac{-200}{100} = \\mathbf{-2,0} \\implies |E_d| = 2 > 1 \\text{ (Elastis)} \\end{aligned}",
            "legend": "• Tanda negatif menunjukkan arah hubungan terbalik antara harga dan kuantitas sesuai hukum permintaan"
        },
        "hints": {
            "concept": "Pada P = 5, Q = 200 - 4(25) = 100. Turunan dQ/dP = -8P = -40. Ed = (dQ/dP) * (P/Q) = -40 * (5/100) = -2.0. Nilai mutlak 2 > 1 berarti Elastis.",
            "execution": "Pilih: Ed = -2,0 (Elastis, karena |Ed| > 1)."
        }
    },
    {
        "id": "eko-lat-m-13",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Keseimbangan Produsen Meminimalkan Biaya (Isoquant & Isocost)",
        "stem": "Dalam teori produksi jangka panjang, seorang produsen mengombinasikan faktor produksi tenaga kerja ($L$) dengan upah $w = \\text{Rp } 50.000,-$ per jam dan modal ($K$) dengan harga sewa $r = \\text{Rp } 100.000,-$ per jam. Keseimbangan produsen yang meminimalkan biaya produksi (Least Cost Combination) untuk menghasilkan sejumlah output tertentu tercapai pada saat...",
        "correct": "Tingkat Substitusi Teknis Marjinal sama dengan rasio harga input ($MRTS_{LK} = \\frac{w}{r} = \\frac{50.000}{100.000} = 0,5$), yang ditandai dengan bersinggungannya kurva Isoquant dengan kurva Isocost.",
        "distractors": [
            "Kurva Isoquant memotong tegak lurus kurva Isocost pada titik di mana Marginal Product tenaga kerja sama dengan nol.",
            "Produsen menggunakan tenaga kerja dua kali lebih banyak daripada modal tanpa memperhitungkan upah marjinal.",
            "Total Cost yang dikeluarkan perusahaan sama persis dengan Total Revenue dari penjualan barang di pasar bebas.",
            "Kurva Isocost bergeser ke kanan atas menjauhi kurva Isoquant sehingga timbul laba monopoli."
        ],
        "formula": {
            "title": "KONDISI KESEIMBANGAN PRODUSEN (LEAST COST COMBINATION)",
            "latex": "MRTS_{LK} = \\frac{MP_L}{MP_K} = \\frac{w}{r} \\implies \\frac{MP_L}{w} = \\frac{MP_K}{r}",
            "legend": "• Isoquant: Menggambarkan kombinasi input $L$ dan $K$ yang menghasilkan kuantitas output yang sama<br>• Isocost: Batas kemampuan anggaran total biaya produsen ($TC = wL + rK$)<br>• Slope Isocost: $-w / r$"
        },
        "hints": {
            "concept": "Keseimbangan produsen (Least Cost Combination) tercapai saat kurva Isoquant bersinggungan dengan Isocost: MRTS_LK = w / r = 50.000 / 100.000 = 0,5.",
            "execution": "Pilih opsi: MRTS_LK = w / r = 0,5, ditandai persinggungan Isoquant dan Isocost."
        }
    },
    {
        "id": "eko-lat-m-14",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Angka Pengganda Pengeluaran Pemerintah (Government Spending Multiplier)",
        "stem": "Dalam perekonomian tertutup sederhana, fungsi konsumsi masyarakat dirumuskan sebagai $C = 100 + 0,8Y_d$, di mana kecenderungan mengonsumsi marjinal adalah $MPC = 0,8$. Jika pemerintah menambah anggaran pengeluaran belanja negara ($\\Delta G$) sebesar Rp 50 Triliun untuk membangun jalan tol, pertambahan total pendapatan nasional ($\\Delta Y$) yang tercipta melalui proses efek pengganda (multiplier effect) adalah...",
        "correct": "Rp 250 Triliun, dihitung dari formula angka pengganda belanja pemerintah $k_G = \\frac{1}{1 - MPC} = \\frac{1}{1 - 0,8} = 5$, sehingga $\\Delta Y = 5 \\times 50 = 250$ Triliun.",
        "distractors": [
            "Rp 50 Triliun, karena pendapatan nasional hanya bertambah tepat sebesar nilai suntikan dana pemerintah.",
            "Rp 200 Triliun, hasil perkalian nilai pengeluaran pemerintah dengan koefisien MPC masyarakat.",
            "Rp 40 Triliun, karena sebagian dana mengalami kebocoran melalui tabungan dan pajak.",
            "Rp 500 Triliun, hasil asumsi angka pengganda pajak lump-sum berbobot sepuluh kali lipat."
        ],
        "formula": {
            "title": "FORMULA ANGKA PENGGANDA BELANJA PEMERINTAH",
            "latex": "k_G = \\frac{1}{1 - MPC} = \\frac{1}{MPS} = \\frac{1}{0,2} = 5 \\implies \\Delta Y = k_G \\cdot \\Delta G = 5 \\times 50 = \\mathbf{250 \\text{ Triliun}}",
            "legend": "• $MPC$: Marginal Propensity to Consume ($0,8$)<br>• $MPS$: Marginal Propensity to Save ($1 - MPC = 0,2$)<br>• Efek Multiplier: Setiap Rp 1 belanja pemerintah merangsang rantai konsumsi berulang di masyarakat sebesar Rp 5"
        },
        "hints": {
            "concept": "Multiplier belanja k_G = 1 / (1 - MPC) = 1 / (1 - 0.8) = 1 / 0.2 = 5. Delta Y = 5 * 50 = 250 Triliun.",
            "execution": "Pilih: Rp 250 Triliun."
        }
    },
    {
        "id": "eko-lat-m-15",
        "materi": "LEMBAGA KEUANGAN & PASAR MODAL",
        "topic": "Komparasi Hak Pemegang Saham Biasa vs Saham Preferen",
        "stem": "Di bursa efek pasar modal, instrumen ekuitas diterbitkan dalam bentuk Saham Biasa (Common Stock) dan Saham Preferen (Preferred Stock). Keistimewaan hak finansial yang dimiliki oleh pemegang Saham Preferen dibandingkan pemegang Saham Biasa adalah...",
        "correct": "Mendapatkan prioritas utama dalam pembagian dividen dengan tingkat dividen tetap (fixed dividend) dan memperoleh klaim aset terlebih dahulu jika perusahaan mengalami likuidasi/pailit, namun umumnya tidak memiliki hak suara dalam Rapat Umum Pemegang Saham (RUPS).",
        "distractors": [
            "Memiliki hak suara ganda dalam RUPS untuk memilih jajaran dewan direksi dan komisaris perusahaan.",
            "Bebas dari segala kewajiban hukum dan dapat menuntut pengembalian modal pokok setiap saat seperti deposito.",
            "Dijamin memperoleh imbalan bunga kupon bulanan tetap yang ditanggung sepenuhnya oleh Bank Indonesia.",
            "Dapat menukarkan sahamnya menjadi mata uang emas batangan langsung di kantor Otoritas Jasa Keuangan."
        ],
        "formula": {
            "title": "KOMPARASI SAHAM BIASA VS SAHAM PREFEREN",
            "latex": "\\begin{array}{|l|c|c|} \\hline \\text{Karakteristik} & \\text{Saham Biasa (Common)} & \\text{Saham Preferen (Preferred)} \\\\ \\hline \\text{Hak Suara di RUPS} & \\text{Ya (1 Saham = 1 Suara)} & \\text{Umumnya Tidak Memiliki Hak Suara} \\\\ \\text{Dividen} & \\text{Bervariasi (Tergantung Laba)} & \\mathbf{\\text{Tetap \\& Diprioritaskan Terlebih Dahulu}} \\\\ \\text{Klaim Aset Saat Likuidasi} & \\text{Paling Terakhir (Residual Claim)} & \\mathbf{\\text{Diprioritaskan Sebelum Saham Biasa}} \\\\ \\hline \\end{array}",
            "legend": "• Saham Preferen merupakan instrumen hibrida yang memadukan karakteristik obligasi (pembayaran tetap) dan saham (ekuitas)"
        },
        "hints": {
            "concept": "Saham preferen: dividen tetap dan prioritas klaim aset saat likuidasi, tetapi umumnya tidak punya hak suara di RUPS.",
            "execution": "Pilih opsi yang menjelaskan prioritas pembagian dividen tetap dan klaim aset saat likuidasi namun tanpa hak suara."
        }
    },
    {
        "id": "eko-lat-m-16",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Jurnal Penyesuaian Pendapatan Diterima di Muka Pendekatan Neraca",
        "stem": "Pada tanggal 1 Agustus 2024, sebuah perusahaan jasa menerima pembayaran uang sewa gedung sebesar Rp 36.000.000,- untuk masa sewa 2 tahun ke depan dan dicatat pada akun `Sewa Diterima di Muka` (pendekatan neraca / utang). Pada penutupan buku per 31 Desember 2024, ayat jurnal penyesuaian (AJP) yang benar adalah...",
        "correct": "Sewa Diterima di Muka (Debit) Rp 7.500.000,- dan Pendapatan Sewa (Kredit) Rp 7.500.000,-.",
        "distractors": [
            "Pendapatan Sewa (Debit) Rp 7.500.000,- dan Sewa Diterima di Muka (Kredit) Rp 7.500.000,-.",
            "Kas (Debit) Rp 36.000.000,- dan Pendapatan Sewa (Kredit) Rp 36.000.000,-.",
            "Sewa Diterima di Muka (Debit) Rp 28.500.000,- dan Pendapatan Sewa (Kredit) Rp 28.500.000,-.",
            "Beban Sewa (Debit) Rp 7.500.000,- dan Kas (Kredit) Rp 7.500.000,-."
        ],
        "formula": {
            "title": "KALKULASI PENYESUAIAN PENDAPATAN DITERIMA DI MUKA",
            "latex": "\\begin{aligned} \\text{Masa Sewa Berjalan (1 Agt s.d. 31 Des 2024)} & = 5 \\text{ Bulan} \\\\ \\text{Total Durasi Sewa (2 Tahun)} & = 24 \\text{ Bulan} \\\\ \\text{Pendapatan yang Sudah Terealisasi (Hak Periode Ini)} & = \\frac{5}{24} \\times 36.000.000 = \\mathbf{7.500.000} \\\\ \\text{Jurnal: Liabilitas Berkurang (Debit), } & \\text{Pendapatan Diakui (Kredit)} \\end{aligned}",
            "legend": "• Pendekatan Neraca: Dicatat awalnya di kewajiban, maka AJP menyesuaikan porsi yang TELAH menjadi pendapatan (5 bulan = Rp 7.500.000,-)"
        },
        "hints": {
            "concept": "Dari 1 Agustus ke 31 Desember = 5 bulan berjalan. Total sewa 2 tahun = 24 bulan. Hak pendapatan yang sudah terealisasi = (5/24) * 36 jt = 7,5 jt. Debet Sewa Diterima di Muka, Kredit Pendapatan Sewa.",
            "execution": "Pilih: Sewa Diterima di Muka (Debit) Rp 7.500.000,- dan Pendapatan Sewa (Kredit) Rp 7.500.000,-."
        }
    },
    {
        "id": "eko-lat-m-17",
        "materi": "STRUKTUR PASAR",
        "topic": "Pasar Oligopoli dan Model Kurva Permintaan Patah (Kinked Demand Curve)",
        "stem": "Dalam pasar oligopoli non-kolusif, Paul Sweezy merumuskan model Kurva Permintaan Patah (Kinked Demand Curve) untuk menjelaskan fenomena kekakuan harga (Price Rigidity). Asumsi perilaku saling ketergantungan antar produsen oligopoli dalam model Sweezy adalah...",
        "correct": "Jika salah satu perusahaan menaikkan harga, perusahaan pesaing tidak akan mengikuti (sehingga kurva di atas harga pasar bersifat elastis), namun jika perusahaan menurunkan harga, seluruh pesaing akan ikut menurunkan harga agar tidak kehilangan pangsa pasar (kurva di bawah harga pasar bersifat inelastis).",
        "distractors": [
            "Jika perusahaan menaikkan harga, pesaing akan menaikkan harga dua kali lipat lebih tinggi untuk membentuk kartel monopoli.",
            "Seluruh perusahaan di pasar oligopoli sepakat untuk tidak memproduksi barang selama harga belum disetujui pemerintah.",
            "Perusahaan yang memiliki biaya produksi terendah akan membagikan teknologinya secara gratis kepada perusahaan lain.",
            "Kurva permintaan oligopoli selalu berbentuk garis lurus horizontal seperti halnya pasar persaingan sempurna."
        ],
        "formula": {
            "title": "MODEL KURVA PERMINTAAN PATAH SWEEZY (KINKED DEMAND)",
            "latex": "\\begin{cases} P > P_0 : & \\text{Pesaing Tidak Mengikuti} \\implies \\text{Permintaan Elastis (Kehilangan Konsumen)} \\\\ P < P_0 : & \\text{Pesaing Ikut Menurunkan Harga} \\implies \\text{Permintaan Inelastis (Perang Harga)} \\end{cases}",
            "legend": "• Disparitas Kurva MR: Kurva Marginal Revenue mengalami diskontinuitas (terputus vertikal) tepat pada tingkat output keseimbangan<br>• Implikasi: Pergeseran biaya marjinal ($MC$) di area terputus tidak akan mengubah harga pasar (kekakuan harga)"
        },
        "hints": {
            "concept": "Asumsi Sweezy: Naik harga tidak diikuti (elastis), turun harga diikuti semua pesaing (inelastis). Akibatnya harga cenderung kaku (rigid).",
            "execution": "Pilih opsi: Jika menaikkan harga pesaing tidak mengikuti (elastis), jika menurunkan harga pesaing ikut menurunkan harga (inelastis)."
        }
    },
    {
        "id": "eko-lat-m-18",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Dampak Depresiasi Nilai Tukar dan Efek Kurva J (J-Curve Effect)",
        "stem": "Ketika nilai tukar rupiah mengalami depresiasi (pelemahan) terhadap dolar AS, secara teoritis harga barang ekspor Indonesia menjadi lebih murah di pasar global dan barang impor menjadi lebih mahal. Namun, dalam jangka sangat pendek, neraca perdagangan Indonesia sering kali justru memburuk terlebih dahulu sebelum akhirnya membaik di jangka panjang. Fenomena pergerakan neraca perdagangan ini dikenal sebagai...",
        "correct": "Efek Kurva J (J-Curve Effect), yang terjadi karena volume ekspor dan impor bersifat kaku (inelastic) dalam jangka pendek akibat kontrak dagang lama yang masih berjalan, sehingga nilai tagihan impor melonjak sebelum volume perdagangan mampu menyesuaikan diri.",
        "distractors": [
            "Kondisi Marshall-Lerner Negatif, yaitu kondisi di mana jumlah elastisitas ekspor dan impor selalu lebih besar dari sepuluh.",
            "Fenomena Dutch Disease, yaitu apresiasi mata uang akibat penemuan ladang minyak raksasa secara tiba-tiba.",
            "Perangkap Likuiditas (Liquidity Trap), yaitu kondisi suku bunga nol di mana kebijakan moneter kehilangan efektivitasnya.",
            "Krisis Neraca Modal, yaitu penarikan seluruh investasi asing portofolio dari pasar saham dalam satu hari perdagangan."
        ],
        "formula": {
            "title": "DINAMIKA EFEK KURVA J (J-CURVE EFFECT)",
            "latex": "\\text{Depresiasi Mata Uang} \\implies \\begin{cases} \\text{Jangka Pendek (Kontrak Kaku):} & \\text{Neraca Dagang Memburuk (Defisit Melebar)} \\\\ \\text{Jangka Panjang (Volume Responsif):} & |E_x + E_m| > 1 \\implies \\text{Neraca Dagang Membaik (Surplus)} \\end{cases}",
            "legend": "• Bentuk Kurva: Menukik turun terlebih dahulu lalu melesat naik tajam membentuk huruf 'J'<br>• Prasyarat Pemulihan Jangka Panjang: Terpenuhinya Kondisi Marshall-Lerner ($|E_x + E_m| > 1$)"
        },
        "hints": {
            "concept": "Depresiasi mata uang membuat neraca dagang memburuk dulu di jangka pendek baru membaik di jangka panjang, membentuk pola huruf J (J-Curve Effect).",
            "execution": "Pilih: Efek Kurva J (J-Curve Effect)."
        }
    },
    {
        "id": "eko-lat-m-19",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Batas Kemungkinan Produksi (PPF) dan Increasing Opportunity Costs",
        "stem": "Kurva Batas Kemungkinan Produksi (Production Possibility Frontier / PPF) yang berbentuk cekung ke arah titik origin (titik nol) mencerminkan salah satu hukum fundamental ekonomi, yaitu...",
        "correct": "Hukum Peningkatan Biaya Peluang (The Law of Increasing Opportunity Costs), yang menyatakan bahwa untuk memproduksi unit tambahan suatu barang, masyarakat harus mengorbankan kuantitas barang lain dalam jumlah yang semakin lama semakin besar karena sumber daya tidak dapat dialihkan secara sempurna.",
        "distractors": [
            "Hukum Biaya Tetap Konstan, di mana setiap penambahan barang selalu menuntut pengorbanan barang lain yang sama persis ukurannya.",
            "Kondisi inefisiensi produksi di mana perekonomian beroperasi di bawah kapasitas penuh tenaga kerja.",
            "Kemustahilan komputasi dalam membagi sumber daya antara barang konsumsi publik dan barang modal swasta.",
            "Keberadaan inflasi harga barang yang menyebabkan seluruh biaya bahan baku menjadi dua kali lipat lebih mahal."
        ],
        "formula": {
            "title": "KURVA BATAS KEMUNGKINAN PRODUKSI (PPF)",
            "latex": "\\text{Slope PPF} = MRT = -\\frac{\\Delta Y}{\\Delta X} \\implies \\text{Semakin ke Kanan Bawah, Slope } |MRT| \\uparrow \\implies \\text{Cekung (Concave)}",
            "legend": "• Titik di DALAM Kurva: Tidak efisien (ada pengangguran sumber daya)<br>• Titik pada SEPANJANG Kurva: Efisien secara produktif<br>• Titik di LUAR Kurva: Mustahil dicapai dengan teknologi dan sumber daya saat ini (hanya bisa dicapai lewat pertumbuhan ekonomi)"
        },
        "hints": {
            "concept": "Bentuk PPF cekung (concave) ke titik nol mencerminkan The Law of Increasing Opportunity Costs (biaya peluang yang semakin meningkat).",
            "execution": "Pilih: Hukum Peningkatan Biaya Peluang (The Law of Increasing Opportunity Costs)."
        }
    },
    {
        "id": "eko-lat-m-20",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Perhitungan Harga Pokok Penjualan (HPP) Perusahaan Dagang",
        "stem": "Data pembukuan sebuah toko distributor barang dagangan selama bulan Desember mencatat:\n- Persediaan Awal Barang Dagangan = Rp 35.000.000,-\n- Pembelian Barang Dagangan Bruto = Rp 120.000.000,-\n- Beban Angkut Pembelian = Rp 5.000.000,-\n- Retur Pembelian dan Pengurangan Harga = Rp 4.000.000,-\n- Potongan Pembelian Tunai = Rp 1.000.000,-\n- Persediaan Akhir Barang Dagangan = Rp 40.000.000,-\nBesarnya Harga Pokok Penjualan (HPP) toko tersebut untuk bulan Desember adalah...",
        "correct": "Rp 115.000.000,-, dihitung dari formula $\\text{HPP} = \\text{Persediaan Awal} + \\text{Pembelian Bersih} - \\text{Persediaan Akhir} = 35 + (120 + 5 - 4 - 1) - 40 = 35 + 120 - 40 = 115$ Juta.",
        "distractors": [
            "Rp 125.000.000,-, hasil perhitungan tanpa mengurangkan retur dan potongan pembelian.",
            "Rp 110.000.000,-, hasil kesalahan mengurangkan beban angkut dari total pembelian barang.",
            "Rp 155.000.000,-, hasil penjumlahan barang tersedia untuk dijual tanpa mengurangkan persediaan akhir.",
            "Rp 95.000.000,-, hasil pengurangan persediaan awal dan akhir dari total pembelian bruto."
        ],
        "formula": {
            "title": "FORMULA HARGA POKOK PENJUALAN (HPP)",
            "latex": "\\begin{aligned} \\text{Pembelian Bersih} & = \\text{Pembelian} + \\text{Beban Angkut} - (\\text{Retur} + \\text{Potongan}) \\\\ & = 120 + 5 - (4 + 1) = \\mathbf{120 \\text{ Juta}} \\\\ \\text{Barang Tersedia untuk Dijual (BTUD)} & = \\text{Persediaan Awal} + \\text{Pembelian Bersih} = 35 + 120 = \\mathbf{155 \\text{ Juta}} \\\\ \\mathbf{\\text{HPP}} & = \\text{BTUD} - \\text{Persediaan Akhir} = 155 - 40 = \\mathbf{115 \\text{ Juta}} \\end{aligned}",
            "legend": "• Laba Kotor = Penjualan Bersih - HPP"
        },
        "hints": {
            "concept": "Pembelian bersih = 120 + 5 - (4 + 1) = 120 jt. Barang tersedia = 35 + 120 = 155 jt. HPP = 155 - 40 = 115 jt.",
            "execution": "Pilih: Rp 115.000.000,-."
        }
    },
    {
        "id": "eko-lat-m-21",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Fungsi Konsumsi, Tabungan, dan Tingkat Pendapatan Break-Even",
        "stem": "Dalam suatu perekonomian, fungsi konsumsi masyarakat dirumuskan sebagai $C = 60 + 0,75Y$, di mana $Y$ adalah pendapatan nasional dalam triliun rupiah. Tingkat pendapatan nasional pada saat terjadi keseimbangan titik impas konsumsi (Break-Even Income / tabungan $S = 0$) adalah...",
        "correct": "$Y = 240$ Triliun, dihitung dari kondisi $Y = C \\implies Y = 60 + 0,75Y \\implies 0,25Y = 60 \\implies Y = \\frac{60}{0,25} = 240$.",
        "distractors": [
            "$Y = 180$ Triliun, hasil perkalian konsumsi otonom dengan koefisien kemiringan marginal MPC.",
            "$Y = 300$ Triliun, hasil penambahan fungsi tabungan dengan pendapatan disposabel penuh.",
            "$Y = 60$ Triliun, yaitu nilai konsumsi otonom saat pendapatan nasional bernilai nol.",
            "$Y = 480$ Triliun, hasil perhitungan dengan membagi konsumsi otonom dengan angka pengganda pajak dua."
        ],
        "formula": {
            "title": "KONDISI TITIK IMPAS PENDAPATAN (BREAK-EVEN INCOME)",
            "latex": "\\begin{aligned} Y & = C + S \\implies \\text{Titik Impas saat } S = 0 \\implies Y = C \\\\ Y & = 60 + 0,75Y \\implies Y - 0,75Y = 60 \\implies 0,25Y = 60 \\implies \\mathbf{Y = 240 \\text{ Triliun}} \\\\ \\text{Fungsi Tabungan:} & \\quad S = -60 + 0,25Y \\implies S(240) = -60 + 0,25(240) = -60 + 60 = 0 \\end{aligned}",
            "legend": "• Break-Even Income: Titik di mana seluruh pendapatan nasional habis digunakan untuk belanja konsumsi tanpa menabung"
        },
        "hints": {
            "concept": "Titik impas terjadi saat S = 0 atau Y = C. Y = 60 + 0.75Y -> 0.25Y = 60 -> Y = 60 / 0.25 = 240 Triliun.",
            "execution": "Pilih: Y = 240 Triliun."
        }
    },
    {
        "id": "eko-lat-m-22",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Landasan Konstitusional Sistem Ekonomi Demokrasi Pancasila",
        "stem": "Pasal 33 Undang-Undang Dasar Negara Republik Indonesia Tahun 1945 menjadi landasan konstitusional sistem ekonomi Demokrasi Pancasila. Makna yuridis dan filosofis dari Ayat (2) dan Ayat (3) Pasal 33 UUD 1945 adalah...",
        "correct": "Cabang-cabang produksi yang penting bagi negara dan menguasai hajat hidup orang banyak, serta bumi, air, dan kekayaan alam yang terkandung di dalamnya dikuasai oleh negara dan dipergunakan untuk sebesar-besar kemakmuran rakyat.",
        "distractors": [
            "Pemerintah memberikan kebebasan mutlak kepada konglomerat swasta untuk mengeksploitasi seluruh sumber daya mineral tanpa izin.",
            "Seluruh perusahaan milik negara wajib diprivatisasi penuh kepada investor asing demi melunasi utang luar negeri.",
            "Masyarakat dilarang memiliki modal tabungan pribadi dan seluruh kepemilikan tanah wajib diserahkan kepada koperasi desa.",
            "Sistem pasar bebas kapitalis diterapkan secara murni tanpa ada intervensi regulasi harga sedikit pun dari pemerintah."
        ],
        "formula": {
            "title": "LANDASAN PASAL 33 UUD 1945 (SISTEM EKONOMI INDONESIA)",
            "latex": "\\begin{aligned} \\text{Ayat 1:} & \\quad \\text{Perekonomian disusun sebagai usaha bersama berdasar asas kekeluargaan (Koperasi)} \\\\ \\mathbf{\\text{Ayat 2:}} & \\quad \\mathbf{\\text{Cabang produksi penting \\& kuasai hajat hidup orang banyak dikuasai negara (BUMN)}} \\\\ \\mathbf{\\text{Ayat 3:}} & \\quad \\mathbf{\\text{Bumi, air, kekayaan alam dikuasai negara untuk kemakmuran rakyat}} \\end{aligned}",
            "legend": "• Prinsip: Menghindari sistem free-fight liberalism (penindasan kapitalis), etatisme (pemerintah monopoli kaku), dan monopoli swasta yang merugikan rakyat"
        },
        "hints": {
            "concept": "Ayat 2 & 3 Pasal 33: cabang produksi penting dan bumi, air, kekayaan alam dikuasai negara untuk sebesar-besar kemakmuran rakyat.",
            "execution": "Pilih opsi: Cabang-cabang produksi penting dan kekayaan alam dikuasai oleh negara untuk sebesar-besar kemakmuran rakyat."
        }
    },
    {
        "id": "eko-lat-m-23",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Perbedaan Demand-Pull Inflation vs Cost-Push Inflation",
        "stem": "Inflasi dapat dipicu oleh sisi permintaan agregat maupun sisi penawaran agregat. Peristiwa kenaikan harga barang dan jasa secara luas yang dipicu oleh kenaikan drastis harga bahan bakar minyak (BBM) dunia dan lonjakan upah minimum tenaga kerja diklasifikasikan sebagai...",
        "correct": "Cost-Push Inflation (Inflasi Dorongan Biaya), yang ditandai dengan pergeseran kurva penawaran agregat ($AS$) ke kiri atas, menyebabkan tingkat harga umum naik dan output riil PDB menurun (berisiko memicu stagflasi).",
        "distractors": [
            "Demand-Pull Inflation, yang ditandai dengan pergeseran kurva permintaan agregat ke kanan atas akibat lonjakan daya beli.",
            "Hyperinflation Eksponensial, yang dipicu oleh pencetakan uang kertas secara ugal-ugalan oleh bank sentral.",
            "Imported Deflation, yang menyebabkan penurunan harga barang komoditas impor di pasar dalam negeri.",
            "Structural Deflation, yang terjadi saat penawaran barang melimpah ruah akibat panen raya serentak."
        ],
        "formula": {
            "title": "KOMPARASI PENYEBAB UTAMA INFLASI MAKRO",
            "latex": "\\begin{aligned} \\text{Demand-Pull Inflation:} & \\quad AD \\uparrow \\implies \\text{Kurva } AD \\text{ geser kanan} \\implies P \\uparrow, \\ Y \\uparrow \\\\ \\mathbf{\\text{Cost-Push Inflation:}} & \\quad \\text{Biaya Input} \\uparrow \\implies \\text{Kurva } AS \\text{ geser kiri} \\implies \\mathbf{P \\uparrow, \\ Y \\downarrow \\ (\\text{Stagflasi})} \\end{aligned}",
            "legend": "• Cost-Push dipicu oleh: Kenaikan harga BBM, kenaikan UMR mendadak, depresiasi kurs rupiah yang menaikkan biaya bahan baku impor"
        },
        "hints": {
            "concept": "Kenaikan harga akibat lonjakan biaya bahan baku/BBM/upah adalah Cost-Push Inflation (pergeseran AS ke kiri).",
            "execution": "Pilih: Cost-Push Inflation (Inflasi Dorongan Biaya)."
        }
    },
    {
        "id": "eko-lat-m-24",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Jenis-Jenis Pengangguran: Struktural vs Friksional",
        "stem": "Perkembangan pesat teknologi kecerdasan buatan dan otomasi industri menyebabkan banyak buruh pabrik perakitan konvensional kehilangan pekerjaan karena keahlian manual yang mereka miliki tidak lagi sesuai dengan kualifikasi pemeliharaan robotik yang dicari perusahaan modern. Jenis pengangguran yang dialami oleh para buruh tersebut diklasifikasikan sebagai...",
        "correct": "Pengangguran Struktural (Structural Unemployment), yang terjadi akibat adanya ketidakcocokan mendasar (mismatch) antara keterampilan tenaga kerja yang tersedia dan keahlian yang dibutuhkan oleh lowongan kerja baru.",
        "distractors": [
            "Pengangguran Friksional, yaitu pengangguran sementara yang terjadi karena pekerja sedang dalam proses berpindah tempat kerja.",
            "Pengangguran Musiman, yaitu pengangguran yang timbul akibat pergantian musim tanam atau musim liburan pariwisata.",
            "Pengangguran Siklikal (Konjungtur), yaitu pengangguran akibat penurunan permintaan agregat saat resesi ekonomi.",
            "Pengangguran Sukarela (Voluntary), yaitu orang yang memilih menganggur karena sudah merasa kaya secara finansial."
        ],
        "formula": {
            "title": "TAKSONOMI PENGANGGURAN (UNEMPLOYMENT)",
            "latex": "\\begin{aligned} \\text{Friksional:} & \\quad \\text{Transisi normal antar pekerjaan (pencarian kerja pertama)} \\\\ \\mathbf{\\text{Struktural:}} & \\quad \\mathbf{\\text{Perubahan struktur ekonomi/teknologi} \\implies \\text{Skill Mismatch}} \\\\ \\text{Siklikal:} & \\quad \\text{Resesi ekonomi makro (Penurunan kegiatan bisnis global)} \\\\ \\text{Musiman:} & \\quad \\text{Fluktuasi musim kalender (Petani di luar musim panen)} \\end{aligned}",
            "legend": "• Solusi Pengangguran Struktural: Pelatihan ulang keterampilan (reskilling & upskilling) dan pendidikan vokasi adaptif"
        },
        "hints": {
            "concept": "Pengangguran akibat perubahan struktur teknologi/ekonomi di mana skill lama tidak cocok dengan kebutuhan baru disebut Pengangguran Struktural.",
            "execution": "Pilih: Pengangguran Struktural (Structural Unemployment)."
        }
    },
    {
        "id": "eko-lat-m-25",
        "materi": "LEMBAGA KEUANGAN & PASAR MODAL",
        "topic": "Prinsip Akad Perbankan Syariah: Mudharabah vs Murabahah",
        "stem": "Dalam sistem perbankan syariah yang beroperasi bebas riba, bank menyalurkan pembiayaan modal kerja kepada pengusaha menggunakan akad _Mudharabah_. Karakteristik utama dari pembiayaan berbasis akad _Mudharabah_ adalah...",
        "correct": "Akad kerja sama kemitraan di mana bank syariah menyediakan $100\\%$ modal usaha (Shahibul Maal) dan nasabah bertindak sebagai pengelola usaha (Mudharib), dengan keuntungan dibagi berdasarkan nisbah bagi hasil yang disepakati bersama di awal, sedangkan kerugian finansial ditanggung oleh bank pemilik modal selama bukan akibat kelalaian nasabah.",
        "distractors": [
            "Akad jual beli barang di mana bank menetapkan harga perolehan ditambah margin keuntungan tetap yang dicicil nasabah.",
            "Akad pinjaman berbunga tetap dengan jaminan surat tanah yang akan disita bank jika angsuran bulanan macet.",
            "Akad sewa-menyewa murni tanpa ada opsi pemindahan hak kepemilikan barang di akhir periode pembiayaan.",
            "Akad penitipan dana murni di mana nasabah sewaktu-waktu dapat menarik uangnya tanpa mendapatkan bagi hasil."
        ],
        "formula": {
            "title": "KOMPARASI AKAD UTAMA PERBANKAN SYARIAH",
            "latex": "\\begin{aligned} \\mathbf{\\text{Mudharabah:}} & \\quad \\mathbf{\\text{Kemitraan Modal 100\\% Bank + Tenaga Nasabah} \\implies \\text{Bagi Hasil Nisbah (Profit/Loss Sharing)}} \\\\ \\text{Musyarakah:} & \\quad \\text{Penyertaan modal bersama (Bank \\& Nasabah urun modal)} \\\\ \\text{Murabahah:} & \\quad \\text{Jual Beli: Harga Pokok + Margin Keuntungan Transparan} \\\\ \\text{Ijarah:} & \\quad \\text{Sewa Menyewa manfaat barang/jasa} \\end{aligned}",
            "legend": "• Prinsip Syariah: Adil, transparan, halal, tanpa riba (bunga), tanpa gharar (ketidakjelasan), tanpa maysir (judi)"
        },
        "hints": {
            "concept": "Mudharabah adalah kemitraan bagi hasil di mana 100% modal dari bank dan nasabah sebagai pengelola.",
            "execution": "Pilih opsi: Kerja sama kemitraan di mana bank menyediakan 100% modal dan keuntungan dibagi sesuai nisbah."
        }
    }
]
