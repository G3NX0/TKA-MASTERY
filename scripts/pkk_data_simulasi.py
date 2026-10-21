# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Produk Kreatif dan Kewirausahaan (PKK SMK/MAK)
Dataset: Simulasi CBT HOTS (35 Authentic Questions, pkk-sim-01 to 35)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
Composition:
  - 25 Authentic Single MCQ HOTS (pkk-sim-01 to 25)
  - 5 Complex Multi-select HOTS (pkk-sim-26 to 30)
  - 5 Matrix Benar-Salah HOTS (pkk-sim-31 to 35)
"""

PKK_SIMULASI_ITEMS = [
    {
        "id": "pkk-sim-01",
        "materi": "VALIDASI BISNIS & METODOLOGI LEAN",
        "topic": "Siklus Build-Measure-Learn & Keputusan Pivot",
        "stem": "Sebuah startup agritech siswa SMK meluncurkan aplikasi pencatatan inventaris pupuk bagi kelompok tani (Build). Setelah 3 bulan uji pasar (Measure), data analitik menunjukkan bahwa fitur inventaris jarang digunakan, namun 85% petani aktif menggunakan fitur forum konsultasi hama tanaman via foto dan bersedia membayar langganan untuk rekomendasi pestisida terpercaya (Learn). Menurut metodologi Lean Startup (Eric Ries), langkah strategis wirausaha yang paling tepat dieksekusi adalah...",
        "correct": "Melakukan 'Zoom-In Pivot', yaitu merombak haluan bisnis dengan memfokuskan produk utama sepenuhnya pada fitur konsultasi hama (yang semula hanya fitur minor) karena telah tervalidasi memiliki Product-Market Fit nyata.",
        "distractors": [
            "Melakukan 'Persevere Buta', yaitu memaksakan petani menggunakan fitur inventaris pupuk dengan ancaman pemblokiran akun secara sepihak.",
            "Menutup seluruh operasional rintisan dan membuang server aplikasi ke tempat pembuangan akhir sampah elektronik.",
            "Membayar influencer media sosial kota metropolitan seharga puluhan juta rupiah untuk mengiklankan fitur inventaris yang tidak disukai petani.",
            "Mengganti seluruh bahasa antarmuka aplikasi menjadi bahasa pemrograman assembly agar terlihat canggih di mata dewan juri lomba."
        ],
        "formula": {
            "title": "SIKLUS FEEDBACK LEAN STARTUP (ERIC RIES)",
            "latex": "\\text{Ideas} \\xrightarrow{\\text{Build}} \\text{Product/MVP} \\xrightarrow{\\text{Measure}} \\text{Data} \\xrightarrow{\\text{Learn}} \\text{Pivot or Persevere}",
            "legend": "• Zoom-In Pivot: Fitur minor yang sangat diminati diangkat menjadi keseluruhan produk inti baru<br>• Validated Learning: Keputusan arah bisnis didasarkan pada data perilaku nyata konsumen, bukan asumsi pribadi pendiri"
        },
        "hints": {
            "concept": "Saat data menunjukkan satu fitur minor sangat disukai dan memecahkan masalah nyata pengguna, startup melakukan Zoom-In Pivot.",
            "execution": "Zoom-In Pivot pada fitur konsultasi hama tanaman."
        }
    },
    {
        "id": "pkk-lat-sim-02",
        "id": "pkk-sim-02",
        "materi": "ANALISIS AKUNTANSI BIAYA STANDAR",
        "topic": "Analisis Varians Biaya Bahan Baku (Price & Quantity Variance)",
        "stem": "Standar biaya bahan baku pembuatan 1 unit meja besi lipat di Teaching Factory SMK adalah 4 meter besi hollow seharga Rp15.000 per meter (Standar = Rp60.000/unit). Dalam realisasi produksi 100 unit meja, bagian pengadaan membeli 450 meter besi hollow dengan harga aktual Rp16.000 per meter akibat kenaikan harga pasar. Nilai Selisih Harga Bahan Baku (Material Price Variance / MPV) dan sifat varians tersebut adalah...",
        "correct": "Rp450.000 Tidak Menguntungkan (Unfavorable), karena harga aktual Rp16.000 lebih mahal Rp1.000 dari harga standar untuk seluruh 450 meter bahan yang dibeli.",
        "distractors": [
            "Rp500.000 Menguntungkan (Favorable), karena unit produksi berhasil membuat 100 unit meja tanpa ada siswa yang terluka.",
            "Rp750.000 Tidak Menguntungkan, dihitung dari total selisih kuantitas bahan yang dibeli bendahara sekolah.",
            "Rp1.000.000 Menguntungkan, karena kenaikan harga bahan baku otomatis meningkatkan nilai jual aset sekolah di mata publik.",
            "Rp0 (Impas), karena seluruh kelebihan harga bahan baku otomatis ditanggung oleh dana bantuan operasional sekolah."
        ],
        "formula": {
            "title": "FORMULA MATERIAL PRICE VARIANCE (MPV)",
            "latex": "MPV = (AP - SP) \\times AQ = (16.000 - 15.000) \\times 450 = +1.000 \\times 450 = +\\text{Rp}450.000 \\text{ (Unfavorable)}",
            "legend": "• $AP = \\text{Harga Aktual} = \\text{Rp}16.000$<br>• $SP = \\text{Harga Standar} = \\text{Rp}15.000$<br>• $AQ = \\text{Kuantitas Aktual Dibeli} = 450$ meter<br>• $AP > SP \\implies$ Selisih merugikan / Unfavorable (biaya riil membengkak)"
        },
        "hints": {
            "concept": "MPV = (Actual Price - Standard Price) x Actual Quantity = (16.000 - 15.000) x 450 = Rp450.000 Unfavorable (Tidak Menguntungkan).",
            "execution": "Rp450.000 Tidak Menguntungkan (Unfavorable)."
        }
    },
    {
        "id": "pkk-sim-03",
        "materi": "MANAJEMEN OPERASIONAL TEORI KENDALA",
        "topic": "Theory of Constraints (TOC) & Drum-Buffer-Rope",
        "stem": "Sebuah lini perakitan lampu LED pintar di SMK memiliki empat stasiun kerja berurutan: Stasiun 1 (Pencetakan Casing, kapasitas 60 unit/jam), Stasiun 2 (Penyolderan LED & Komponen, kapasitas 25 unit/jam), Stasiun 3 (Pengujian Kelistrikan & Sensor, kapasitas 40 unit/jam), dan Stasiun 4 (Pengemasan & Box, kapasitas 50 unit/jam). Menurut Theory of Constraints (Eliyahu Goldratt), kapasitas keluaran (throughput) maksimum seluruh pabrik dan stasiun yang menjadi kendala (bottleneck) adalah...",
        "correct": "Throughput maksimum adalah 25 unit/jam yang dibatasi mutlak oleh Stasiun 2 (Penyolderan) sebagai stasiun bottleneck (kendala utama sistem).",
        "distractors": [
            "Throughput maksimum adalah 60 unit/jam yang ditentukan oleh kecepatan tercepat mesin Stasiun 1.",
            "Throughput maksimum adalah 175 unit/jam, yang diperoleh dari penjumlahan seluruh kapasitas keempat stasiun kerja.",
            "Throughput maksimum adalah 43,75 unit/jam, yang dihitung dari rata-rata aritmatika seluruh stasiun kerja bengkel.",
            "Throughput sistem tidak terbatas, karena siswa dapat dipaksa bekerja 24 jam nonstop tanpa henti."
        ],
        "formula": {
            "title": "PRINSIP THEORY OF CONSTRAINTS (TOC)",
            "latex": "\\text{System Throughput} = \\min(\\text{Capacity}_1, \\text{Capacity}_2, \\dots, \\text{Capacity}_n) = \\min(60, 25, 40, 50) = 25 \\text{ unit/jam}",
            "legend": "• Bottleneck Station: Titik dengan kapasitas terendah yang menentukan kecepatan alur seluruh pabrik (Stasiun 2 = 25 unit/jam)<br>• 5 Focusing Steps TOC: (1) Identify bottleneck, (2) Exploit bottleneck, (3) Subordinate everything else, (4) Elevate bottleneck, (5) Prevent inertia"
        },
        "hints": {
            "concept": "Kecepatan maksimal seluruh rantai produksi selalu ditentukan oleh stasiun terlambat/paling lambat (bottleneck). Stasiun 2 memiliki kapasitas terendah (25 unit/jam).",
            "execution": "25 unit/jam dibatasi oleh Stasiun 2 (Penyolderan)."
        }
    },
    {
        "id": "pkk-sim-04",
        "materi": "HAK KEKAYAAN INTELEKTUAL & HUKUM BISNIS",
        "topic": "Sengketa Merek Dagang: Prinsip First to File (UU No. 20/2016)",
        "stem": "Sebuah unit wirausaha tata boga SMK di Kota Bandung telah menjual keripik tempe dengan merek 'KRIUK-JUARA' sejak tahun 2021 secara lokal namun belum pernah mendaftarkannya ke Ditjen KI. Pada awal tahun 2024, seorang pengusaha dari Jakarta mendaftarkan merek 'KRIUK-JUARA' untuk kelas barang kripik tempe yang sama ke Ditjen KI dan sertifikat mereknya resmi terbit. Berdasarkan Undang-Undang No. 20 Tahun 2016 tentang Merek dan Indikasi Geografis, status hak atas merek tersebut adalah...",
        "correct": "Pengusaha Jakarta sah sebagai pemilik hak eksklusif merek karena Indonesia menganut sistem konstitutif (First to File Principle), sehingga unit SMK dilarang menggunakan merek tersebut di pasaran komersial tanpa izin pemegang sertifikat.",
        "distractors": [
            "Unit SMK otomatis menjadi pemilik sah merek karena mereka yang pertama kali memakainya di dapur sekolah (Declarative Principle).",
            "Kedua belah pihak wajib menggabungkan perusahaannya menjadi badan usaha milik daerah tingkat provinsi Jawa Barat.",
            "Ditjen KI akan membatalkan sertifikat pengusaha Jakarta secara sepihak dan menyita seluruh keuntungan usahanya.",
            "Merek tersebut otomatis menjadi milik umum (domain publik) dan siapapun bebas menggunakannya tanpa royalti."
        ],
        "formula": {
            "title": "PRINSIP FIRST TO FILE UU MEREK NO. 20 TAHUN 2016",
            "latex": "\\text{Hak Eksklusif Merek} \\iff \\text{Pendaftaran Resmi di DJKI (Sistem Konstitutif/First to File)} \\neq \\text{Pemakai Pertama}",
            "legend": "• First to File: Hak eksklusif diberikan kepada pihak yang pertama kali mengajukan permohonan pendaftaran resmi dan disetujui DJKI<br>• Pelajaran Krusial Bisnis: Pelaku usaha/UMKM wajib segera mendaftarkan mereknya sejak awal berdiri sebelum diserobot pihak lain"
        },
        "hints": {
            "concept": "Indonesia menganut asas First to File (bukan First to Use). Hak eksklusif merek lahir dari pendaftaran resmi di DJKI, bukan dari siapa yang memakai duluan di lapangan.",
            "execution": "Pengusaha Jakarta pemilik sah karena sistem First to File (konstitutif)."
        }
    },
    {
        "id": "pkk-sim-05",
        "materi": "STRATEGI PENETAPAN HARGA KONTEMPORER",
        "topic": "Price Bundling Strategy (Pure vs Mixed Bundling)",
        "stem": "Sebuah unit bisnis digital siswa SMK meluncurkan tiga layanan: Jasa Desain Logo (dijual mandiri Rp200.000), Jasa Pembuatan Website Portofolio (dijual mandiri Rp500.000), dan Layanan Domain-Hosting 1 Tahun (dijual mandiri Rp300.000). Untuk mendongkrak omzet dan menangkap surplus konsumen, mereka menawarkan paket hemat 'Branding Lengkap' seharga Rp800.000 yang mencakup ketiga layanan sekaligus, di samping tetap membolehkan konsumen membeli masing-masing layanan secara terpisah. Strategi penetapan harga ini disebut...",
        "correct": "Mixed Bundling (Penjualan Bundel Campuran), di mana produk ditawarkan baik secara terpisah (ala carte) dengan harga individual maupun dalam satu paket bundel gabungan dengan potongan harga menarik.",
        "distractors": [
            "Pure Bundling Murni, di mana konsumen dipaksa secara mutlak membeli seluruh paket dan dilarang keras membeli satu layanan saja.",
            "Predatory Pricing Ekstrem, yang bertujuan membunuh seluruh penyedia jasa internet di wilayah kabupaten secara ilegal.",
            "Loss Leader Pricing, di mana siswa sengaja merugi Rp5.000.000 pada setiap desain website yang dikerjakan.",
            "Freemium Monopoli, di mana seluruh fitur website disembunyikan di balik pembayaran uang tebusan kripto."
        ],
        "formula": {
            "title": "TAKSONOMI STRATEGI BUNDLING HARGA",
            "latex": "\\text{Mixed Bundling: } P_{\\text{Bundle}} < \\sum P_{\\text{Individual}} \\quad (\\text{Rp}800.000 < \\text{Rp}1.000.000) \\quad \\& \\quad \\text{Individual Sales Allowed}",
            "legend": "• Pure Bundling: Hanya dijual dalam paket; tidak dijual terpisah sama sekali<br>• Mixed Bundling: Dijual terpisah (ala carte) DAN dijual dalam paket terdiskon (meningkatkan volume penjualan dan utilitas konsumen)"
        },
        "hints": {
            "concept": "Ketika produk dijual terpisah tetapi juga ditawarkan dalam paket terdiskon bersama, strateginya adalah Mixed Bundling.",
            "execution": "Mixed Bundling (Penjualan Bundel Campuran)."
        }
    },
    {
        "id": "pkk-sim-06",
        "materi": "MANAJEMEN PERSEDIAAN RITEL",
        "topic": "Gross Margin Return on Investment (GMROI)",
        "stem": "Koperasi ritel siswa SMK menjual helm retro dengan data kinerja tahunan: Total Penjualan Kotor = Rp50.000.000, Total Harga Pokok Penjualan (HPP) = Rp35.000.000, dan Biaya Rata-Rata Persediaan Barang di Etalase (Average Inventory Cost) = Rp10.000.000. Berapakah nilai Gross Margin Return on Investment (GMROI) dari lini produk helm retro tersebut dan apa maknanya?",
        "correct": "1,50 (atau 150%), yang bermakna bahwa setiap Rp1 modal uang kas yang tertanam di persediaan helm mampu menghasilkan laba kotor sebesar Rp1,50 per tahun.",
        "distractors": [
            "5,00 (atau 500%), dihitung dengan membagi penjualan kotor langsung dengan biaya persediaan tanpa memperhitungkan HPP.",
            "0,20 (atau 20%), yang menunjukkan bahwa koperasi mengalami kerugian persediaan sebesar 80% dari modal awal.",
            "3,50 (atau 350%), yang merupakan perputaran persediaan berdasarkan harga pokok barang.",
            "0,70 (atau 70%), dihitung dari rasio harga pokok penjualan terhadap total penjualan kotor tahunan."
        ],
        "formula": {
            "title": "FORMULA GROSS MARGIN RETURN ON INVESTMENT (GMROI)",
            "latex": "GMROI = \\frac{\\text{Gross Profit}}{\\text{Average Inventory Cost}} = \\frac{\\text{Sales} - \\text{COGS}}{\\text{Average Inventory Cost}} = \\frac{50.000.000 - 35.000.000}{10.000.000} = \\frac{15.000.000}{10.000.000} = 1{,}50",
            "legend": "• Gross Profit: Rp15.000.000<br>• GMROI > 1,0 menunjukkan persediaan menghasilkan keuntungan melebihi modal yang terikat di barang stok<br>• Standar Ritel: GMROI 1,5 - 2,5 adalah target sehat bagi toko ritel produktif"
        },
        "hints": {
            "concept": "GMROI = Laba Kotor / Biaya Rata-Rata Persediaan. Laba Kotor = 50jt - 35jt = 15jt. GMROI = 15jt / 10jt = 1,50 (150%).",
            "execution": "1,50 (atau 150%)."
        }
    },
    {
        "id": "pkk-sim-07",
        "materi": "EVALUASI SENSORIS & MUTU PANGAN",
        "topic": "Pengujian Organoleptik Skala Hedonik pada Pangan",
        "stem": "Dalam pengembangan produk nugget ikan lele substitusi daun kelor oleh siswa SMK Agribisnis Pengolahan Hasil Perikanan, tim melakukan uji penerimaan konsumen terhadap 30 panelis agak terlatih menggunakan lembar evaluasi Skala Hedonik 7 poin (skor 1 = Sangat Tidak Suka s.d. skor 7 = Sangat Suka) untuk parameter Rasa, Aroma, Warna, dan Tekstur. Fungsi esensial dari penerapan uji hedonik tersebut dalam tahapan perancangan produk massal adalah...",
        "correct": "Mengukur secara kuantitatif tingkat kesukaan dan penerimaan subjektif konsumen potensial terhadap karakteristik sensori produk guna menentukan formulasi resep terbaik sebelum diproduksi secara komersial.",
        "distractors": [
            "Menghitung kadar racun arsenik dan zat kimia berbahaya di dalam laboratorium toksikologi forensik.",
            "Menentukan nilai pajak pertambahan nilai yang harus disetorkan ke kantor pelayanan pajak pratama.",
            "Memaksa panelis menandatangani surat perjanjian pembelian saham perusahaan sebanyak 100 lembar.",
            "Mengganti seluruh komposisi daging ikan lele dengan tepung tapioka tanpa memberitahukan kepada konsumen."
        ],
        "formula": {
            "title": "PRINSIP UJI SENSORIK HEDONIK (SNI 01-2346)",
            "latex": "\\overline{X}_{\\text{Hedonik}} = \\frac{\\sum (f_i \\times S_i)}{N} \\ge 5{,}0 \\text{ (Kriteria Diterima Pasar: Rata-Rata 'Agak Suka' s.d. 'Sangat Suka')}",
            "legend": "• Skala Hedonik: 1 (Sangat Tidak Suka), 2 (Tidak Suka), 3 (Agak Tidak Suka), 4 (Netral), 5 (Agak Suka), 6 (Suka), 7 (Sangat Suka)<br>• Analisis: Digunakan ANOVA dan uji lanjut Duncan/Tukey untuk menguji signifikansi perbedaan antar formulasi perlakuan"
        },
        "hints": {
            "concept": "Uji hedonik adalah uji organoleptik berbasis respon afektif (tingkat kesukaan) konsumen terhadap parameter rasa, aroma, tekstur, dan warna sebelum komersialisasi.",
            "execution": "Mengukur tingkat kesukaan dan penerimaan sensori konsumen untuk optimasi formulasi resep."
        }
    },
    {
        "id": "pkk-sim-08",
        "materi": "MANAJEMEN KEUANGAN & MODAL KERJA",
        "topic": "Siklus Konversi Kas (Cash Conversion Cycle - CCC)",
        "stem": "Unit produksi garmen SMK memiliki metrik manajemen operasional kas: Rata-Rata Umur Persediaan (Days Inventory Outstanding / DIO) = 45 hari, Rata-Rata Periode Pengumpulan Piutang (Days Sales Outstanding / DSO) = 30 hari, dan Rata-Rata Periode Pembayaran Utang Bahan ke Supplier (Days Payable Outstanding / DPO) = 25 hari. Berapakah durasi Siklus Konversi Kas (Cash Conversion Cycle / CCC) dari usaha garmen tersebut?",
        "correct": "50 hari, dihitung dari DIO (45 hari) + DSO (30 hari) - DPO (25 hari), yang menunjukkan rentang waktu di mana uang kas perusahaan terikat dalam modal kerja sejak pembelian bahan hingga kas piutang diterima.",
        "distractors": [
            "100 hari, yang diperoleh dari penjumlahan seluruh hari operasional tanpa memperhitungkan fasilitas tempo utang supplier.",
            "10 hari, karena periode pembayaran utang langsung dikurangkan dari piutang dagang tanpa memperhitungkan stok gudang.",
            "20 hari, dihitung dari selisih antara umur persediaan dengan periode pembayaran utang dagang.",
            "75 hari, dihitung dengan mengabaikan seluruh kebijakan kredit dari pemasok kain tekstil."
        ],
        "formula": {
            "title": "FORMULA CASH CONVERSION CYCLE (CCC)",
            "latex": "CCC = DIO + DSO - DPO = 45 + 30 - 25 = 50 \\text{ hari}",
            "legend": "• DIO (Days Inventory Outstanding): Rata-rata hari bahan tersimpan hingga terjual = 45 hari<br>• DSO (Days Sales Outstanding): Rata-rata hari piutang tertagih menjadi uang tunai = 30 hari<br>• DPO (Days Payable Outstanding): Rata-rata hari tempo pembayaran kepada pemasok = 25 hari<br>• Strategi Optimasi: Perkecil DIO dan DSO, serta perpanjang DPO yang sehat untuk memperpendek CCC"
        },
        "hints": {
            "concept": "Cash Conversion Cycle (CCC) = DIO + DSO - DPO. CCC = 45 + 30 - 25 = 50 hari.",
            "execution": "50 hari (rentang kas terikat modal kerja operasional)."
        }
    },
    {
        "id": "pkk-sim-09",
        "materi": "ANALISIS KINERJA KEUANGAN (DUPONT)",
        "topic": "Analisis DuPont 3-Faktor: Return on Equity (ROE)",
        "stem": "Sebuah perseroan terbatas rintisan alumni SMK dievaluasi menggunakan analisis DuPont 3-langkah untuk membedah kinerja Return on Equity (ROE). Perusahaan mencatat: Net Profit Margin (NPM) = 10%, Asset Turnover (ATO) = 1,5 kali, dan Financial Leverage Multiplier (Equity Multiplier) = 2,0 kali. Berapakah nilai Return on Equity (ROE) perusahaan dan faktor mana yang paling berkontribusi mendorong pengembalian ekuitas tersebut?",
        "correct": "ROE = 30%, dihasilkan dari efisiensi margin laba (10%), kecepatan perputaran aset (1,5x), dan pemanfaatan struktur modal terungkit (leverage 2,0x) yang bekerja secara simultan.",
        "distractors": [
            "ROE = 13,5%, dihitung dari penjumlahan ketiga indikator keuangan tanpa menerapkan prinsip perkalian faktor.",
            "ROE = 3,0%, dihitung dari pembagian rasio profit margin dengan equity multiplier.",
            "ROE = 7,5%, karena perputaran aset memotong nilai keuntungan bersih menjadi separuhnya.",
            "ROE = 300%, karena ekuitas perusahaan dihitung menggunakan kurs mata uang euro seratus tahun lalu."
        ],
        "formula": {
            "title": "FORMULA SISTEM ANALISIS DUPONT (ROE)",
            "latex": "ROE = \\text{Net Profit Margin} \\times \\text{Asset Turnover} \\times \\text{Equity Multiplier} = 0{,}10 \\times 1{,}5 \\times 2{,}0 = 0{,}30 \\text{ (30\\%)}",
            "legend": "• Margin (10%): Kemampuan menghasilkan laba dari setiap rupiah omzet penjualan (Profitabilitas Operasional)<br>• Asset Turnover (1,5x): Efisiensi penggunaan seluruh aset untuk menghasilkan omzet (Efisiensi Aset)<br>• Equity Multiplier (2,0x): Rasio total aset terhadap ekuitas sendiri (Financial Leverage / Daya Ungkit Utang)"
        },
        "hints": {
            "concept": "Analisis DuPont: ROE = NPM x Asset Turnover x Equity Multiplier. ROE = 0,10 x 1,5 x 2,0 = 0,30 = 30%.",
            "execution": "ROE = 30%."
        }
    },
    {
        "id": "pkk-sim-10",
        "materi": "SISTEM PRODUKSI RAMPING (LEAN)",
        "topic": "Value Stream Mapping (VSM) & Takt Time",
        "stem": "Dalam perakitan panel saklar pintar di bengkel SMK, permintaan harian pelanggan adalah 120 unit. Waktu kerja efektif yang tersedia bagi operator dalam satu hari adalah 8 jam kerja (480 menit), dikurangi total istirahat terencana 60 menit (waktu kerja bersih 420 menit atau 25.200 detik). Berapakah Takt Time (ritme detak produksi) yang wajib dipertahankan oleh lini perakitan agar pesanan pelanggan terpenuhi tepat waktu tanpa kelebihan produksi?",
        "correct": "210 detik per unit (atau 3,5 menit per unit), dihitung dari waktu kerja bersih 25.200 detik dibagi dengan permintaan pelanggan 120 unit.",
        "distractors": [
            "240 detik per unit, dihitung dari total waktu 8 jam penuh tanpa mengurangkan waktu istirahat operator bengkel.",
            "60 detik per unit, agar siswa bekerja terburu-buru hingga tingkat produk cacat meningkat tajam.",
            "1.200 detik per unit, karena siswa diperbolehkan bersantai menonton video di jam kerja praktik.",
            "30 detik per unit, dihitung dari selisih antara waktu istirahat dengan jumlah saklar listrik."
        ],
        "formula": {
            "title": "FORMULA TAKT TIME PRODUKSI LEAN",
            "latex": "\\text{Takt Time} = \\frac{\\text{Net Available Operating Time per Day}}{\\text{Customer Demand per Day}} = \\frac{25.200 \\text{ detik}}{120 \\text{ unit}} = 210 \\text{ detik/unit}",
            "legend": "• Waktu Bersih: $(480 - 60) \\times 60 = 420 \\times 60 = 25.200$ detik<br>• Permintaan: 120 unit per hari<br>• Takt Time = 210 detik (Setiap 210 detik, 1 unit saklar jadi harus selesai keluar dari lini perakitan)"
        },
        "hints": {
            "concept": "Takt Time = Waktu Kerja Efektif Bersih / Kebutuhan Konsumen = (420 menit x 60 detik) / 120 unit = 25.200 / 120 = 210 detik/unit.",
            "execution": "210 detik per unit (atau 3,5 menit per unit)."
        }
    },
    {
        "id": "pkk-sim-11",
        "materi": "MANAJEMEN KEUANGAN & PEMBIAYAAN",
        "topic": "Anjak Piutang (Factoring) dengan Recourse vs Without Recourse",
        "stem": "Unit produksi furnitur SMK memiliki piutang dagang sebesar Rp100.000.000 dari pembeli hotel berbintang dengan termin pembayaran 90 hari. Untuk mempercepat arus kas guna membeli kayu jati gelondongan, unit usaha mengalihkan (menjual) piutang tersebut ke lembaga anjak piutang (Factoring Company) dengan skema 'With Recourse'. Konsekuensi finansial dan yuridis dari klausul 'With Recourse' tersebut adalah...",
        "correct": "Jika pihak hotel pembeli mengalami gagal bayar (wanprestasi) saat jatuh tempo 90 hari, maka unit usaha SMK tetap memikul risiko kerugian penuh dan wajib mengembalikan uang talangan kepada lembaga anjak piutang.",
        "distractors": [
            "Lembaga anjak piutang menanggung 100% risiko kredit macet tanpa hak menuntut pengembalian uang kepada unit usaha SMK.",
            "Hotel berbintang otomatis menjadi milik sekolah sebagai aset tetap sitaan tanpa proses pengadilan.",
            "Lembaga anjak piutang wajib membagikan separuh sahamnya kepada guru pembimbing kewirausahaan sekolah.",
            "Seluruh utang piutang otomatis dihapuskan oleh menteri keuangan atas nama keadilan sosial."
        ],
        "formula": {
            "title": "DIKOTOMI SKEMA ANJAK PIUTANG (FACTORING)",
            "latex": "\\text{With Recourse} \\implies \\text{Credit Risk Retained by Seller (SMK)}; \\quad \\text{Without Recourse} \\implies \\text{Credit Risk Absorbed by Factor}",
            "legend": "• With Recourse: Biaya diskonto/fee lebih murah, tetapi penjual piutang menjamin pelunasan bila debitur wanprestasi<br>• Without Recourse (Non-recourse): Biaya fee lebih mahal, risiko debitur macet beralih sepenuhnya ke perusahaan anjak piutang"
        },
        "hints": {
            "concept": "Dalam anjak piutang With Recourse, risiko kredit macet tetap berada pada penjual piutang (jika debitur gagal bayar, penjual wajib mengganti).",
            "execution": "Unit SMK tetap menanggung risiko gagal bayar (With Recourse)."
        }
    },
    {
        "id": "pkk-sim-12",
        "materi": "SERTIFIKASI PRODUK & STANDAR MUTU",
        "topic": "Sistem Jaminan Produk Halal (SJPH) & Titik Kritis Bahan",
        "stem": "Dalam proses pengajuan sertifikasi halal reguler produk kue bolu gulung ke BPJPH, auditor Lembaga Pemeriksa Halal (LPH) memeriksa dokumen daftar bahan baku. Titik kritis kehalalan (Critical Halal Point) yang wajib dibuktikan dengan sertifikat halal yang valid dan dokumen spesifikasi teknis dari produsen bahan tambahan pangan adalah...",
        "correct": "Bahan pengemulsi nabati/hewani (Emulsifier seperti mono- dan digliserida), gelatin pembentuk gel, dan perisa rum sintetis yang berpotensi mengandung alkohol turunan khamr.",
        "distractors": [
            "Air mineral murni dari sumur bor yang telah dimasak mendidih pada suhu seratus derajat celcius.",
            "Tepung terigu curah yang digiling dari biji gandum mentah di ladang pertanian organik.",
            "Gula pasir tebu kristal putih yang diperoleh langsung dari petani tebu lokal.",
            "Loyang aluminium cetakan kue yang dicuci bersih menggunakan deterjen pencuci piring."
        ],
        "formula": {
            "title": "TITIK KRITIS BAHAN SISTEM JAMINAN PRODUK HALAL (HAS 23000)",
            "latex": "\\text{Bahan Kritis} = \\text{Turunan Lemak Hewani (E471)} + \\text{Gelatin (Porcine/Bovine)} + \\text{Flavor/Pelarut Alkohol Turunan}",
            "legend": "• Bahan Non-Kritis (Positive List): Air, garam, gula murni, sayuran segar, buah murni<br>• Bahan Kritis (Wajib Bersertifikat): Emulsifier, enzim pengembang, gelatin, flavor, seasoning, shortening"
        },
        "hints": {
            "concept": "Titik kritis bahan halal pada produk reroti/kue adalah pengemulsi (emulsifier berbasis lemak hewani/nabati), gelatin, dan flavor berpelarut alkohol.",
            "execution": "Emulsifier lemak, gelatin, dan perisa beralkohol (titik kritis kehalalan)."
        }
    },
    {
        "id": "pkk-sim-13",
        "materi": "STRATEGI PERTUMBUHAN USAHA (GROWTH)",
        "topic": "Framework Metrik Pirate AARRR pada Startup",
        "stem": "Sebuah aplikasi bursa kerja khusus lulusan SMK menerapkan kerangka analitik Pirate Metrics (AARRR: Acquisition, Activation, Retention, Referral, Revenue). Jika data menunjukkan 2.000 alumni mengunduh aplikasi (Acquisition), 1.200 di antaranya melengkapi profil curriculum vitae pada hari pertama (Activation), dan 300 di antaranya merekomendasikan tautan kode undangan kepada teman sekelasnya hingga mendaftar baru, maka metrik AARRR yang terefleksikan pada aktivitas terakhir tersebut adalah...",
        "correct": "Referral (Advokasi / Rujukan Pengguna), yaitu fase di mana pengguna yang puas secara sukarela membagikan dan mengajak pengguna baru ke dalam platform.",
        "distractors": [
            "Revenue (Pendapatan), karena setiap kode undangan otomatis dipotong saldo kasir bank Indonesia.",
            "Retention (Retensi), karena pengguna tersebut tetap membuka aplikasi selama sepuluh jam tanpa tidur.",
            "Acquisition (Akuisisi), karena tautan kode referral dibuat oleh algoritma peladen komputer.",
            "Dissolution (Pembubaran), karena sistem membatasi pendaftaran hanya untuk satu rumpun kejuruan saja."
        ],
        "formula": {
            "title": "KERANGKA KERJA STARTUP METRICS AARRR (DAVE MCCLURE)",
            "latex": "\\text{Acquisition (Tahu/Daftar)} \\rightarrow \\text{Activation (Aha-Moment)} \\rightarrow \\text{Retention (Kembali Pakai)} \\rightarrow \\mathbf{Referral} \\rightarrow \\text{Revenue}",
            "legend": "• Acquisition: Pengguna datang dari kanal pemasaran<br>• Activation: Pengguna merasakan manfaat awal produk (profil lengkap)<br>• Retention: Pengguna kembali menggunakan produk secara berkala<br>• Referral: Pengguna mengajak orang lain (viral coefficient / K-factor)<br>• Revenue: Pengguna membayar transaksi/berlangganan"
        },
        "hints": {
            "concept": "Aktivitas membagikan tautan/kode undangan kepada teman sehingga terjadi pendaftaran baru merupakan tahap Referral (Rujukan).",
            "execution": "Referral (Rujukan / Word-of-Mouth)."
        }
    },
    {
        "id": "pkk-sim-14",
        "materi": "KESELAMATAN & KESEHATAN KERJA (K3LH)",
        "topic": "Hirarki Pengendalian Bahaya (Hierarchy of Controls)",
        "stem": "Di bengkel bodi dan pengecatan otomotif SMK, proses pembersihan cat mobil lama menggunakan cairan pelarut kimia berbasis benzena yang sangat beracun dan bersifat karsinogenik. Guru pembimbing bersama tim K3 memutuskan untuk mengganti cairan benzena tersebut dengan larutan pembersih nabati berbasis minyak kulit jeruk (d-Limonene) yang tidak beracun dan ramah lingkungan. Berdasarkan Hirarki Pengendalian Bahaya K3, tindakan tersebut berada pada level pengendalian...",
        "correct": "Substitusi (Substitution), yaitu mengganti bahan, peralatan, atau proses yang berbahaya dengan bahan atau proses yang memiliki tingkat bahaya jauh lebih rendah atau tidak berbahaya sama sekali.",
        "distractors": [
            "Penggunaan Alat Pelindung Diri (APD), karena siswa diwajibkan membeli masker respirator karbon aktif dengan uang sendiri.",
            "Pengendalian Administratif, karena guru hanya menempelkan stiker gambar tengkorak bahaya racun di pintu lemari.",
            "Rekayasa Teknik (Engineering Control), karena cairan kimia diaduk menggunakan sendok makan berbahan plastik.",
            "Eliminasi Total, karena mobil konsumen langsung dibakar hingga seluruh cat mengelupas dengan sendirinya."
        ],
        "formula": {
            "title": "HIRARKI PENGENDALIAN BAHAYA K3 (ISO 45001 / OSHA)",
            "latex": "\\text{Eliminasi (Paling Efektif)} \\longrightarrow \\mathbf{Substitusi} \\longrightarrow \\text{Rekayasa Teknik} \\longrightarrow \\text{Administratif} \\longrightarrow \\text{APD (Paling Lemah)}",
            "legend": "• Eliminasi: Menghilangkan sumber bahaya secara fisik total<br>• Substitusi: Mengganti bahan beracun (benzena) dengan bahan aman (d-Limonene)<br>• Rekayasa Teknik: Memasang exhaust ventilation hood dan spray booth tertutup<br>• Administratif: SOP waktu kerja dan rotasi operator<br>• APD: Respirator kimia, sarung tangan nitril, kacamata goggle"
        },
        "hints": {
            "concept": "Mengganti bahan beracun berbahaya dengan alternatif yang lebih aman merupakan tindakan pada tingkat Substitusi (Hierarchy of Controls).",
            "execution": "Substitusi (Substitution)."
        }
    },
    {
        "id": "pkk-sim-15",
        "materi": "HAK KEKAYAAN INTELEKTUAL & HUKUM",
        "topic": "Perlindungan Rahasia Dagang (UU No. 30/2000)",
        "stem": "Unit produksi pengolahan pangan SMK memiliki formula bumbu rempah rahasia untuk produk ayam goreng krispi yang tidak pernah didaftarkan patennya agar resep tersebut tidak dipublikasikan ke dokumen terbuka. Agar formula resep tersebut sah dan terlindungi secara hukum sebagai 'Rahasia Dagang' berdasarkan Undang-Undang No. 30 Tahun 2000, tiga syarat kumulatif yang wajib dipenuhi adalah...",
        "correct": "Informasi tersebut bersifat rahasia (hanya diketahui pihak tertentu), memiliki nilai ekonomi komersial nyata, dan dijaga kerahasiaannya melalui langkah-langkah yang layak (seperti penyimpanan terkunci, akses terbatas, dan klausul NDA).",
        "distractors": [
            "Informasi harus diumumkan di surat kabar nasional, ditempel di mading sekolah, dan dibagikan ke seluruh wali murid.",
            "Pemilik resep wajib memiliki gelar doktor di bidang kimia pangan dan memegang paspor Uni Eropa.",
            "Formula resep harus diuji coba pada hewan mamalia laut di bawah pengawasan dinas kelautan.",
            "Resep wajib dibeli oleh pemerintah daerah dengan harga minimal satu miliar rupiah secara tunai."
        ],
        "formula": {
            "title": "3 SYARAT KUALIFIKASI RAHASIA DAGANG (UU 30/2000 PASAL 3)",
            "latex": "\\text{Rahasia Dagang Sah} \\iff \\text{Bersifat Rahasia} \\wedge \\text{Bernilai Ekonomi} \\wedge \\text{Dijaga dengan Upaya Layak (NDA \& SOP)}",
            "legend": "• Berbeda dengan Paten: Paten mensyaratkan keterbukaan publik (disclosure) dengan masa perlindungan 20 tahun; Rahasia Dagang tidak dipublikasikan dan masa perlindungannya tanpa batas waktu selama kerahasiaan terjaga"
        },
        "hints": {
            "concept": "Syarat Rahasia Dagang menurut UU 30/2000: (1) Bersifat rahasia, (2) Memiliki nilai ekonomi, (3) Dijaga kerahasiaannya melalui upaya yang layak.",
            "execution": "Bersifat rahasia, memiliki nilai ekonomi, dan dijaga kerahasiaannya dengan upaya layak."
        }
    },
    {
        "id": "pkk-sim-16",
        "materi": "MANAJEMEN OPERASIONAL JUST-IN-TIME",
        "topic": "Sistem Tarik Kanban (Pull System) vs Push System",
        "stem": "Dalam transformasi bengkel manufaktur SMK menuju sistem Just-In-Time (JIT), kepala bengkel mengganti sistem produksi terjadwal berbasis ramalan (Push System) dengan sistem Kanban (Pull System). Prinsip kerja utama dari alur produksi berbasis kartu Kanban tersebut adalah...",
        "correct": "Stasiun kerja di hilir hanya menarik dan memicu produksi komponen dari stasiun kerja di hulu persis saat ada permintaan nyata, sehingga meniadakan penumpukan barang dalam proses (Work-in-Process / WIP).",
        "distractors": [
            "Stasiun kerja hulu memproduksi barang sebanyak-banyaknya tanpa mempedulikan apakah stasiun hilir siap menerimanya atau tidak.",
            "Setiap siswa diwajibkan membawa kartu debit perbankan untuk menggesek mesin absensi sebelum menyalakan bor listrik.",
            "Seluruh proses perakitan dihentikan secara permanen dan sekolah hanya mengimpor barang jadi dari luar negeri.",
            "Mesin pabrik diprogram untuk membuang separuh komponen ke bak sampah setiap lima menit sekali."
        ],
        "formula": {
            "title": "MEKANISME PULL SYSTEM DENGAN KANBAN (TOYOTA JIT)",
            "latex": "\\text{Customer Demand} \\longrightarrow \\text{Downstream Station} \\xrightarrow{\\text{Withdrawal Kanban}} \\text{Upstream Station} \\xrightarrow{\\text{Production Kanban}} \\text{Zero Idle WIP}",
            "legend": "• Push System: Berdasarkan peramalan kuota (MRP), risiko overproduction dan WIP menumpuk di lantai pabrik<br>• Pull System (Kanban): Berdasarkan konsumsi riil downstream; produksi hanya berjalan jika ada sinyal kartu Kanban"
        },
        "hints": {
            "concept": "Sistem Tarik (Pull System) dengan Kanban: stasiun kerja hilir menarik komponen dari hulu hanya ketika dibutuhkan, mencegah penumpukan WIP.",
            "execution": "Stasiun hilir menarik komponen dari hulu sesuai kebutuhan nyata (meniadakan tumpukan WIP)."
        }
    },
    {
        "id": "pkk-sim-17",
        "materi": "LEGALITAS BADAN USAHA KONTEMPORER",
        "topic": "Pendirian Perseroan Perorangan (UU Cipta Kerja)",
        "stem": "Dua siswa SMK yang baru lulus ingin mendirikan badan usaha berbadan hukum resmi untuk usaha konsultan jaringan komputer mereka. Berdasarkan UU Cipta Kerja dan PP No. 8 Tahun 2021, pemerintah memperkenalkan bentuk badan usaha 'Perseroan Perorangan untuk Usaha Mikro dan Kecil'. Karakteristik utama dari Perseroan Perorangan yang sangat menguntungkan bagi wirausahawan pemula adalah...",
        "correct": "Dapat didirikan oleh 1 orang WNI tanpa akta notaris (cukup pendaftaran elektronik di Kemenkumham), memiliki status badan hukum resmi, dan adanya pemisahan tanggung jawab kekayaan pribadi dengan kekayaan perusahaan (tanggung jawab terbatas).",
        "distractors": [
            "Wajib memiliki modal disetor minimal Rp50 Miliar tunai di brankas kantor kementerian investasi.",
            "Harus didirikan minimal oleh 20 orang anggota keluarga sedarah dengan persetujuan kepala desa.",
            "Pemilik usaha memikul tanggung jawab hukum dan utang piutang tanpa batas hingga ke seluruh harta warisan orang tua.",
            "Dilarang membuka rekening bank atas nama badan usaha dan tidak berhak mendapatkan Nomor Induk Berusaha."
        ],
        "formula": {
            "title": "KARAKTERISTIK PERSEROAN PERORANGAN (PP 8/2021)",
            "latex": "\\text{PT Perorangan} = \\text{1 Orang Pendiri (WNI)} + \\text{Badan Hukum Resmi (Kemenkumham)} + \\text{Limited Liability} + \\text{Biaya PNBP Murah (Rp50.000)}",
            "legend": "• Syarat: Kriteria Usaha Mikro dan Kecil (Modal usaha $\\le$ Rp5 Miliar di luar tanah & bangunan)<br>• Keunggulan: Tanggung jawab pemegang saham terbatas sebesar modal yang disetor (kekayaan pribadi aman dari sitaan utang usaha)"
        },
        "hints": {
            "concept": "PT Perorangan (UU Cipta Kerja): didirikan oleh 1 orang, tanpa akta notaris (cukup SK Kemenkumham online), berstatus badan hukum, dan tanggung jawab terbatas.",
            "execution": "Dapat didirikan 1 orang tanpa akta notaris, berbadan hukum, dan tanggung jawab terbatas."
        }
    },
    {
        "id": "pkk-sim-18",
        "materi": "PERLINDUNGAN KONSUMEN & ETIKA BISNIS",
        "topic": "Tanggung Jawab Produk Cacat (UU Perlindungan Konsumen No. 8/1999)",
        "stem": "Sebuah unit Teaching Factory SMK menjual lampu pemanas penetas telur otomatis. Akibat cacat desain pada rangkaian pengatur suhu, alat tersebut mengalami panas berlebih (overheat) hingga meledak dan menghanguskan kandang serta 200 butir telur milik peternak pembeli. Berdasarkan UU No. 8 Tahun 1999 tentang Perlindungan Konsumen (UUPK Pasal 19), tanggung jawab pelaku usaha atas kerugian konsumen tersebut adalah...",
        "correct": "Wajib memberikan ganti rugi berupa pengembalian uang atau penggantian barang yang sejenis atau setara nilainya, atau perawatan kesehatan/santunan, dalam tenggang waktu 7 hari setelah tanggal transaksi/insiden.",
        "distractors": [
            "Bebas dari segala tuntutan hukum karena sekolah berstatus lembaga pendidikan yang kebal terhadap hukum perdata dan pidana.",
            "Cukup meminta maaf secara lisan melalui pengeras suara upacara bendera hari Senin.",
            "Menuntut peternak balik ke kepolisian karena peternak dianggap tidak mampu mendinginkan ruangan kandang.",
            "Mengganti kerugian peternak dengan selembar kupon undian berhadiah kaos sablon sekolah."
        ],
        "formula": {
            "title": "TANGGUNG JAWAB PELAKU USAHA (UU NO. 8 TAHUN 1999 PASAL 19)",
            "latex": "\\text{Strict Product Liability} \\implies \\text{Ganti Rugi Kerusakan/Pencemaran/Kerugian Finansial Konsumen} \\le 7 \\text{ Hari}",
            "legend": "• Pasal 19 UUPK: Pelaku usaha bertanggung jawab memberi ganti rugi atas kerusakan, pencemaran, dan/atau kerugian konsumen akibat mengkonsumsi barang yang dihasilkan atau diperdagangkan<br>• Ganti rugi tidak menghapuskan kemungkinan tuntutan pidana bila ada unsur kelalaian fatal"
        },
        "hints": {
            "concept": "Pasal 19 UU No. 8/1999 mewajibkan pelaku usaha mengganti rugi kerusakan/kerugian konsumen (uang kembali atau penggantian barang setara) maksimal 7 hari.",
            "execution": "Wajib memberikan ganti rugi penggantian barang atau uang dalam batas 7 hari."
        }
    },
    {
        "id": "pkk-sim-19",
        "materi": "PEMASARAN HIJAU & ESG",
        "topic": "Green Marketing vs Praktik Greenwashing",
        "stem": "Sebuah jenama tas kain buatan unit kriya SMK memasang klaim mencolok pada label kemasannya: '100% Ramah Lingkungan & Menyelamatkan Bumi dari Krisis Iklim'. Namun saat ditelusuri dalam audit rantai pasok, kain tas tersebut terbuat dari serat sintetis nilon berbasis minyak bumi, proses pewarnaan membuang limbah logam berat tanpa instalasi pengolahan air limbah (IPAL), dan tidak ada sertifikasi ekolabel resmi dari lembaga berwenang. Praktik pemasaran yang menyesatkan konsumen tersebut dikategorikan sebagai...",
        "correct": "Greenwashing, yaitu tindakan memberikan klaim menyesatkan atau tidak berdasar mengenai manfaat ramah lingkungan dari suatu produk guna membangun citra palsu yang peduli lingkungan.",
        "distractors": [
            "Carbon Neutral Certification, yaitu standar internasional pengakuan perusahaan yang telah mencapai emisi nol bersih secara saintifik.",
            "Circular Economy Champion, yaitu penghargaan tertinggi bagi industri yang berhasil mendaur ulang seluruh limbah produksinya.",
            "Organic Fair Trade, yaitu sistem sertifikasi keadilan upah bagi para petani kapas dan pekerja tekstil perempuan.",
            "Life Cycle Sustainability, yaitu pelaporan transparansi dampak ekologis produk secara terbuka kepada publik."
        ],
        "formula": {
            "title": "DOSA-DOSA GREENWASHING (TERRACHOICE FRAMEWORK)",
            "latex": "\\text{Greenwashing} = \\text{Klaim Hijau Kosong (No Proof)} + \\text{Ketidakjelasan (Vagueness)} + \\text{Pelabelan Palsu (False Labels)}",
            "legend": "• Sin of the Hidden Trade-off, Sin of No Proof, Sin of Vagueness, Sin of Worshiping False Labels<br>• Dampak: Kehilangan kepercayaan konsumen, boikot pasar, potensi sanksi hukum klaim iklan menyesatkan (UU Perlindungan Konsumen)"
        },
        "hints": {
            "concept": "Klaim palsu ramah lingkungan tanpa bukti ilmiah dan audit independen dinamakan Greenwashing.",
            "execution": "Greenwashing (klaim ramah lingkungan palsu / manipulatif)."
        }
    },
    {
        "id": "pkk-sim-20",
        "materi": "ANALISIS KELAYAKAN FINANSIAL",
        "topic": "Profitability Index (Benefit-Cost Ratio Modal)",
        "stem": "Sebuah usulan ekspansi bengkel servis AC mobil siswa SMK membutuhkan investasi awal kas sebesar Rp50.000.000. Dari analisis arus kas masa depan yang telah didiskontokan dengan suku bunga 12%, diperoleh total Present Value (PV) arus kas masuk bersih sebesar Rp65.000.000. Berapakah nilai Indeks Kemampulabaan (Profitability Index / PI) dari usulan proyek tersebut dan apa kesimpulannya?",
        "correct": "PI = 1,30, yang menunjukkan proyek sangat layak diterima (karena PI > 1,0), di mana setiap Rp1 investasi awal menghasilkan nilai tunai arus kas masuk sebesar Rp1,30.",
        "distractors": [
            "PI = 0,77, yang menunjukkan proyek harus segera ditolak karena nilai investasi awal lebih kecil daripada arus kas masuk.",
            "PI = 0,30, dihitung dari selisih antara keuntungan bersih dengan biaya sewa gedung laboratorium.",
            "PI = 15,0, dihitung dari selisih nominal kas masuk dikalikan dengan faktor penyusutan mesin pompa vakum.",
            "PI = -1,30, karena nilai uang di masa depan selalu bertanda minus dalam standar perbankan nasional."
        ],
        "formula": {
            "title": "FORMULA PROFITABILITY INDEX (PI)",
            "latex": "PI = \\frac{\\text{PV of Future Cash Inflows}}{\\text{Initial Investment Outlay}} = \\frac{\\text{Rp}65.000.000}{\\text{Rp}50.000.000} = 1{,}30",
            "legend": "• Kriteria Keputusan: PI > 1,0 (Diterima / Feasible); PI = 1,0 (Indifferent); PI < 1,0 (Ditolak / Unfeasible)<br>• PI = 1,30 identik dengan NPV positif sebesar Rp15.000.000"
        },
        "hints": {
            "concept": "Profitability Index (PI) = PV of Cash Inflows / Initial Outlay. PI = 65jt / 50jt = 1,30. Nilai PI > 1,0 menandakan proyek layak diterima.",
            "execution": "PI = 1,30 (layak diterima, PI > 1,0)."
        }
    },
    {
        "id": "pkk-sim-21",
        "materi": "PERJANJIAN LISENSI MEREK",
        "topic": "Klausul Pembayaran Royalti Merek & Pengendalian Kualitas",
        "stem": "Dalam perjanjian pemberian lisensi merek sepatu lokal karya siswa SMK kepada mitra pabrikan sepatu di Jawa Timur, dicantumkan klausul bahwa mitra pabrikan berhak memproduksi dan menjual sepatu dengan merek tersebut dengan kewajiban membayar royalti 8% dari omzet penjualan kotor setiap kuartal. Di samping itu, pemilik lisensi (SMK) berhak melakukan inspeksi berkala terhadap bahan baku dan standar jahitan di pabrik mitra. Tujuan yuridis utama dari pencantuman klausul pengendalian mutu (Quality Control Clause) tersebut adalah...",
        "correct": "Mencegah terjadinya degradasi reputasi dan nilai ekuitas merek (Brand Dilution) akibat produk berkualitas rendah yang dibuat oleh penerima lisensi, sekaligus memenuhi kewajiban undang-undang untuk menjaga standar kualitas merek terdaftar.",
        "distractors": [
            "Memungkinkan siswa SMK menyita seluruh mesin pemotong kulit milik pabrikan mitra tanpa ganti rugi.",
            "Menghapus kewajiban pembayaran pajak penghasilan atas royalti merek bagi kedua belah pihak.",
            "Memaksa pabrikan mitra mempekerjakan seluruh warga desa sekitar pabrik sebagai direktur operasional.",
            "Mengganti nama kepemilikan pabrik mitra menjadi kantor cabang dinas pendidikan provinsi."
        ],
        "formula": {
            "title": "PRINSIP LISENSI MEREK & KONTROL MUTU (UU 20/2016)",
            "latex": "\\text{Lisensi Merek Sah} \\implies \\text{Royalty Agreement} + \\mathbf{Quality\\ Control\\ Mandate} \\implies \\text{Preservation of Brand Equity}",
            "legend": "• Perlindungan Brand Equity: Lisensi tanpa kendali mutu (naked licensing) dapat menyebabkan merek kehilangan daya pembeda dan reputasi pasar<br>• Aspek UU: Pemilik merek terdaftar berhak memberikan lisensi dan tetap bertanggung jawab atas jaminan standar mutu produk berlisensi"
        },
        "hints": {
            "concept": "Quality Control Clause dalam kontrak lisensi merek bertujuan melindungi reputasi dan ekuitas merek dari penurunan kualitas oleh penerima lisensi.",
            "execution": "Mencegah degradasi reputasi dan menjaga ekuitas merek (Quality Control Clause)."
        }
    },
    {
        "id": "pkk-sim-22",
        "materi": "MANAJEMEN KUALITAS & TAGUCHI",
        "topic": "Design of Experiments (DOE) & Fungsi Kerugian Taguchi",
        "stem": "Dalam merancang cetakan injeksi plastik untuk bodi stopkontak listrik, tim engineering Teaching Factory SMK menerapkan prinsip Mutu Taguchi (Taguchi Quality Loss Function): $L(y) = k(y - m)^2$. Di mana $m$ adalah nilai target dimensi nominal (50,00 mm) dan $y$ adalah dimensi aktual produk. Filosofi revolusioner Taguchi mengenai kerugian mutu (Quality Loss) yang membedakannya dari pendekatan toleransi tradisional adalah...",
        "correct": "Kerugian mutu bagi masyarakat/konsumen mulai timbul seketika begitu nilai karakteristik produk menyimpang dari target nominal ($m$), meskipun deviasi tersebut masih berada di dalam rentang batas toleransi spesifikasi teknis yang diizinkan.",
        "distractors": [
            "Kerugian mutu bernilai nol rupiah selama produk tidak meledak di tangan konsumen saat pertama kali dicolokkan ke listrik.",
            "Produk yang berada di batas toleransi terluar dianggap memiliki mutu yang sama persis sempurnanya dengan produk yang tepat di target nominal.",
            "Biaya kerugian mutu hanya ditanggung oleh petugas quality control yang bertugas memeriksa barang di pintu keluar gudang.",
            "Kerugian mutu dihitung semata-mata dari selisih harga jual produk di pasar tradisional dengan pasar modern."
        ],
        "formula": {
            "title": "FUNGSI KERUGIAN MUTU TAGUCHI (QUALITY LOSS FUNCTION)",
            "latex": "L(y) = k(y - m)^2 \\quad \\text{vs} \\quad \\text{Traditional Goalpost: } \\text{Loss} = 0 \\iff LSL \\le y \\le USL",
            "legend": "• Pendekatan Tradisional (Goalpost): Mutu dianggap baik biner (tanpa rugi) selama berada di antara LSL dan USL<br>• Filosofi Taguchi: Penyimpangan sekecil apa pun dari titik target ($m$) menimbulkan kerugian (loss to society) berbentuk fungsi kuadratik parabolik"
        },
        "hints": {
            "concept": "Filosofi Taguchi memandang bahwa setiap penyimpangan dari target nominal (meski masih dalam toleransi) sudah menimbulkan kerugian mutu secara kuadratik bagi konsumen.",
            "execution": "Kerugian timbul begitu menyimpang dari target nominal (filosofi kuadratik Taguchi)."
        }
    },
    {
        "id": "pkk-sim-23",
        "materi": "VALUASI STARTUP METODE SCORECARD",
        "topic": "Valuasi Startup Pre-Revenue: Scorecard Valuation Method",
        "stem": "Sebuah tim startup IoT pertanian siswa SMK melakukan valuasi pre-revenue menggunakan metode Scorecard Valuation (Payne Method). Rata-rata valuasi startup serupa di wilayah tersebut adalah Rp1.000.000.000. Berdasarkan penilaian faktor tertimbang (Kekuatan Tim Pendiri bobot 30% skor 120%, Ukuran Peluang Pasar bobot 25% skor 110%, Kesiapan Produk/Teknologi bobot 15% skor 100%, Iklim Persaingan bobot 10% skor 90%, dan Kemitraan Strategis bobot 20% skor 105%), total faktor penyesuaian tertimbang adalah 1,105 (110,5%). Berapakah nilai valuasi pra-investasi (Pre-Money Valuation) startup tersebut?",
        "correct": "Rp1.105.000.000, dihitung dari perkalian rata-rata valuasi pembanding (Rp1.000.000.000) dengan total faktor penyesuaian tertimbang (1,105).",
        "distractors": [
            "Rp895.000.000, dihitung dengan mengurangi valuasi rata-rata dengan persentase penyesuaian pasar modal.",
            "Rp2.105.000.000, yang diperoleh dengan menambahkan omzet target lima tahun ke depan secara spekulatif.",
            "Rp500.000.000, karena valuasi startup siswa sekolah diatur memiliki batas atas tetap oleh dinas pendidikan.",
            "Rp110.500.000, dihitung dari pembagian valuasi rata-rata dengan jumlah anggota tim pendiri."
        ],
        "formula": {
            "title": "METODE SCORECARD VALUATION (BILL PAYNE METHOD)",
            "latex": "\\text{Valuasi Pre-Money} = \\text{Base Benchmark Valuation} \\times \\sum (W_i \\times S_i) = 1.000.000.000 \\times 1{,}105 = \\text{Rp}1.105.000.000",
            "legend": "• Faktor Tertimbang: Tim (0,30x1,2 = 0,36) + Pasar (0,25x1,1 = 0,275) + Produk (0,15x1,0 = 0,15) + Kompetisi (0,10x0,9 = 0,09) + Mitra (0,20x1,05 = 0,21) = 1,085 + ... = 1,105<br>• Aplikasi: Standar de facto valuasi angel investor untuk startup teknologi yang belum memiliki laporan laba rugi komersial (pre-revenue)"
        },
        "hints": {
            "concept": "Scorecard Valuation = Rata-Rata Valuasi Pasar x Total Faktor Penyesuaian Tertimbang = 1.000.000.000 x 1,105 = Rp1.105.000.000.",
            "execution": "Rp1.105.000.000."
        }
    },
    {
        "id": "pkk-sim-24",
        "materi": "DESAIN PRODUK & KANSEI ENGINEERING",
        "topic": "Penerapan Kansei Engineering pada Produk Kriya Kreatif",
        "stem": "Dalam mendesain perabot meja kerja minimalis berbahan kayu jati Belanda daur ulang, siswa SMK mengidentifikasi respons emosional dan psikologis pengguna terhadap kata sifat seperti 'hangat', 'lapang', 'tenang', dan 'kokoh', lalu menerjemahkannya secara matematis ke dalam parameter fisik desain (seperti sudut kelengkungan kurva tepi meja $R=15\\text{ mm}$, warna finishing natural matte, dan ketebalan papan $30\\text{ mm}$). Metodologi rekayasa desain yang menjembatani perasaan emosional konsumen dengan spesifikasi teknis produk ini disebut...",
        "correct": "Kansei Engineering (Rekayasa Sensori Emosional), yaitu pendekatan teknologi desain ergonomis yang menerjemahkan citra rasa psikologis (emosi) konsumen menjadi parameter desain fisik produk nyata.",
        "distractors": [
            "Reverse Engineering Tradisional, yaitu membongkar produk kompetitor secara sembunyi-sembunyi untuk meniru ukuran bautnya.",
            "Brute Force Fabrication, yaitu memotong kayu secara acak tanpa pengukuran gambar teknik kerja.",
            "Destructive Strength Testing, yaitu membanting meja dari lantai tiga sekolah untuk menguji kekuatannya.",
            "Arbitrary Styling Method, yaitu mengecat meja dengan warna-warni kontras tanpa mempedulikan kenyamanan pengguna."
        ],
        "formula": {
            "title": "METODOLOGI KANSEI ENGINEERING (MITSUO NAGAMACHI)",
            "latex": "\\text{Emotional Feelings (Kansei Words)} \\xrightarrow{\\text{Kuantifikasi Semantik \& Regresi}} \\text{Spesifikasi Fisik Produk (Properties)}",
            "legend": "• Kansei Type I (Category Classification): Menghubungkan kata sensori (Kansei words) dengan sub-fitur produk fisik<br>• Kansei Type II (Computer-aided / AI): Penggunaan model jaringan saraf/matematis untuk memprediksi respon afektif pelanggan"
        },
        "hints": {
            "concept": "Metodologi yang menerjemahkan perasaan emosional/psikologis konsumen menjadi parameter spesifikasi teknis fisik desain disebut Kansei Engineering.",
            "execution": "Kansei Engineering (Rekayasa Sensori Emosional)."
        }
    },
    {
        "id": "pkk-sim-25",
        "materi": "PERPAJAKAN TRANSAKSI DIGITAL",
        "topic": "Kewajiban Perpajakan Marketplace & PMSE (PPN Digital)",
        "stem": "Sebuah unit bisnis digital siswa SMK menjual produk kerajinan tangan melalui platform e-commerce lokapasar (marketplace) nasional. Berdasarkan ketentuan perpajakan transaksi Perdagangan Melalui Sistem Elektronik (PMSE) di Indonesia, pemungutan dan penyetoran Pajak Pertambahan Nilai (PPN) atas biaya jasa layanan platform yang dikenakan marketplace kepada penjual dilakukan dengan mekanisme...",
        "correct": "Pihak penyelenggara marketplace bertindak sebagai Pemungut PPN PMSE yang ditunjuk oleh Menteri Keuangan untuk memungut, menyetorkan, dan melaporkan PPN atas biaya komisi layanan transaksi secara terpusat.",
        "distractors": [
            "Siswa penjual wajib datang setiap hari ke kantor pajak membawa uang tunai receh untuk membayar PPN transaksi.",
            "Seluruh transaksi di marketplace bebas pajak secara mutlak karena server komputer berada di awan (cloud).",
            "Pembeli barang diwajibkan mengirimkan bukti lapor SPT tahunan kepada kurir paket sebelum barang diserahkan.",
            "Pajak pertambahan nilai diganti dengan sumbangan wajib beras untuk lumbung pangan desa."
        ],
        "formula": {
            "title": "MEKANISME PPN PMSE (PMK NO. 60/PMK.03/2022)",
            "latex": "\\text{Platform Marketplace (Pemungut Ditunjuk)} \\xrightarrow{\\text{Pungut PPN (11\\% / 12\\%)}} \\text{Kas Negara via DJP Elektronik}",
            "legend": "• Dasar Hukum: Penunjukan PMSE sebagai Pemungut PPN oleh Dirjen Pajak<br>• Objek: Penyerahan BKP Tidak Berwujud dan/atau JKP dari luar maupun dalam negeri melalui sistem elektronik<br>• Tanggung Jawab: Pelaku usaha mikro tidak terbebani administrasi pelaporan PPN platform karena dipungut otomatis di sistem"
        },
        "hints": {
            "concept": "Dalam regulasi PMSE Indonesia, penyelenggara marketplace ditunjuk resmi sebagai Pemungut PPN yang memotong dan menyetor PPN jasa secara terpusat.",
            "execution": "Marketplace bertindak sebagai Pemungut PPN PMSE resmi yang memungut dan menyetor terpusat."
        }
    },

    # -------------------------------------------------------------
    # 5 COMPLEX MULTI-SELECT ITEMS (pkk-sim-26 to pkk-sim-30)
    # -------------------------------------------------------------
    {
        "id": "pkk-sim-26",
        "type": "multi",
        "materi": "INDIKATOR KESEHATAN MODEL BISNIS",
        "topic": "Metrik Keberlanjutan Startup & Unit Economics",
        "stem": "Dalam mengevaluasi keberlanjutan dan kelayakan ekspansi unit usaha rintisan (startup) siswa SMK, tim penilai bisnis mengkaji serangkaian metrik finansial dan operasional. Manakah TIGA pernyataan berikut yang merupakan indikator kesehatan bisnis rintisan (Healthy Unit Economics) yang terverifikasi? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Rasio Customer Lifetime Value terhadap Customer Acquisition Cost (LTV : CAC) bernilai lebih besar atau sama dengan 3 : 1."},
            {"key": "B", "text": "Gross Margin Return on Investment (GMROI) berada di atas angka 1,0, yang membuktikan persediaan menghasilkan laba melebihi biaya perolehannya."},
            {"key": "C", "text": "Churn Rate (tingkat pembatalan langganan pelanggan bulanan) bernilai 90% per bulan sebagai bukti perputaran pelanggan yang sangat cepat."},
            {"key": "D", "text": "Cash Conversion Cycle (CCC) bernilai lebih pendek atau negatif, yang menandakan usaha sangat efisien dalam mengelola modal kerja."},
            {"key": "E", "text": "Biaya Tetap (Fixed Cost) sengaja dinaikkan hingga 500% dari total omzet untuk mempercepat pengembalian modal investasi."}
        ],
        "correctAnswer": ["A", "B", "D"],
        "formula": {
            "title": "TRIAD INDIKATOR KESEHATAN UNIT ECONOMICS",
            "latex": "\\text{Sehat: } (\\text{LTV:CAC} \\ge 3:1) \\wedge (\\text{GMROI} > 1{,}0) \\wedge (\\text{CCC Minimized})",
            "legend": "• LTV:CAC >= 3:1 menjamin pengembalian biaya promosi<br>• GMROI > 1,0 membuktikan keuntungan stok dagangan<br>• Short/Negative CCC memastikan modal kerja tidak tersandera<br>• Pilihan C salah (Churn 90% berarti bisnis bocor dan mendekati kolaps); Pilihan E salah (FC bengkak memperbesar kerugian)"
        },
        "hints": {
            "concept": "Bisnis sehat memiliki LTV:CAC >= 3:1, GMROI > 1,0, dan CCC yang pendek/efisien. Churn 90% dan FC membengkak adalah tanda kegagalan.",
            "execution": "Pilih A, B, dan D."
        }
    },
    {
        "id": "pkk-sim-27",
        "type": "multi",
        "materi": "PENETAPAN BIAYA PRODUKSI (HPP)",
        "topic": "Unsur Harga Pokok Produksi Metode Full Costing",
        "stem": "Dalam menyusun Harga Pokok Produksi (HPP) pembuatan prototipe lampu meja pintar berbasis kayu sonokeling dan modul sensor otomatis, tim wirausaha SMK menggunakan metode Full Costing. Manakah TIGA komponen di bawah ini yang wajib dimasukkan ke dalam perhitungan Harga Pokok Produksi (HPP) Full Costing? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Biaya Bahan Baku Langsung (kayu sonokeling, modul mikrokontroler, dan kabel instalasi)."},
            {"key": "B", "text": "Biaya Tenaga Kerja Langsung (upah teknisi siswa yang merakit komponen lampu)."},
            {"key": "C", "text": "Biaya Overhead Pabrik Tetap (penyusutan mesin gergaji listrik dan sewa ruang bengkel praktik)."},
            {"key": "D", "text": "Biaya Komisi Pemasaran dan Iklan Brosur yang dibagikan kepada calon pembeli di pameran."},
            {"key": "E", "text": "Biaya Pajak Penghasilan Orang Pribadi pemilik usaha rintisan pada akhir tahun pajak."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "STRUKTUR BIAYA FULL COSTING",
            "latex": "\\text{HPP}_{\\text{Full Costing}} = \\text{BBB} + \\text{BTKL} + \\text{BOP Variabel} + \\text{BOP Tetap}",
            "legend": "• A, B, C adalah unsur biaya produksi pabrikasi (Product Costs)<br>• D (Biaya Pemasaran) dan E (Pajak Pribadi) adalah biaya komersial non-produksi (Period Costs) yang masuk ke Laporan Laba Rugi di bawah Laba Kotor"
        },
        "hints": {
            "concept": "HPP Full Costing hanya mencakup biaya produksi: Bahan Baku Langsung (A), Tenaga Kerja Langsung (B), dan Overhead Pabrik (C). Komisi iklan dan pajak bukan biaya produksi.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "pkk-sim-28",
        "type": "multi",
        "materi": "HAK KEKAYAAN INTELEKTUAL (PATEN)",
        "topic": "Syarat Substantif Paten (UU No. 13 Tahun 2016)",
        "stem": "Siswa SMK berencana mengajukan permohonan Paten atas alat penjernih air limbah bengkel berbasis membran karbon aktif berpemanas induksi. Berdasarkan UU No. 13 Tahun 2016 tentang Paten, manakah TIGA syarat substantif kumulatif yang wajib dipenuhi agar invensi teknologi tersebut dapat diberi Paten oleh Ditjen KI? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Mengandung Kebaruan (Novelty), yaitu pada tanggal penerimaan permohonan, invensi tersebut belum pernah diumumkan di media cetak/elektronik di negara manapun di dunia."},
            {"key": "B", "text": "Mengandung Langkah Inventif (Inventive Step), yaitu invensi tersebut tidak dapat diduga sebelumnya oleh seseorang yang memiliki keahlian biasa di bidang teknik terkait."},
            {"key": "C", "text": "Dapat Diterapkan dalam Industri (Industrial Applicability), yaitu invensi dapat diproduksi atau digunakan dalam berbagai jenis industri secara nyata dan konsisten."},
            {"key": "D", "text": "Harus sudah terjual minimal 1.000 unit di pasar ritel modern dan menghasilkan omzet satu miliar rupiah sebelum didaftarkan."},
            {"key": "E", "text": "Penciptanya wajib menandatangani surat pelepasan kewarganegaraan Republik Indonesia kepada lembaga paten dunia."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "3 SYARAT SUBSTANTIF PATEN (UU PATEN PASAL 3-5)",
            "latex": "\\text{Paten Diberikan} \\iff \\text{Kebaruan (Novelty)} \\wedge \\text{Langkah Inventif (Non-Obviousness)} \\wedge \\text{Dapat Diterapkan di Industri}",
            "legend": "• Novelty: Belum pernah dipublikasikan di dunia (prior art search)<br>• Inventive Step: Memiliki lompatan teknologi bagi orang yang ahli di bidangnya (person having ordinary skill in the art)<br>• Industrial Applicability: Dapat dibuat/digunakan berulang dalam industri"
        },
        "hints": {
            "concept": "Tiga syarat paten mutlak: Novelty (Kebaruan), Inventive Step (Langkah Inventif), dan Industrial Applicability (Dapat diterapkan di industri).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "pkk-sim-29",
        "type": "multi",
        "materi": "SISTEM MANAJEMEN KUALITAS (LEAN & 5S)",
        "topic": "Prinsip Kerja Kaizen 5S/5R di Area Kerja Industri",
        "stem": "Dalam implementasi budaya kerja industri Kaizen dan 5S/5R (Seiri, Seiton, Seiso, Seiketsu, Shitsuke) di bengkel pengelasan dan perakitan SMK, manakah TIGA tindakan operasional yang mencerminkan penerapan 5S/5R yang tepat? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Memasang papan bayangan alat (Tool Shadow Board) dengan penandaan visual presisi agar setiap tang dan palu memiliki posisi tetap yang mudah diawasi (Seiton / Rapi)."},
            {"key": "B", "text": "Memberikan tanda label merah (Red Tagging) pada perkakas rusak dan material sisa yang tidak terpakai untuk segera disingkirkan dari area kerja (Seiri / Ringkas)."},
            {"key": "C", "text": "Menyusun Standar Operasional Prosedur (SOP) visual dan jadwal audit kepatuhan kebersihan harian yang ditaati secara berkesinambungan (Seiketsu & Shitsuke / Rawat & Rajin)."},
            {"key": "D", "text": "Menimbun seluruh plat besi berkarat di kolong meja perakitan agar bengkel terlihat luas dari pintu gerbang luar."},
            {"key": "E", "text": "Menghentikan seluruh pemeliharaan preventif mesin las agar tidak membuang anggaran oli pelumas."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "IMPLEMENTASI 5S KONTEMPORER DI BENGKEL",
            "latex": "\\text{5S} = \\text{Red Tagging (Sort)} + \\text{Shadow Board (Set in Order)} + \\text{Cleaning as Inspection (Shine)} + \\text{Standard Audit (Standardize)}",
            "legend": "• Tool Shadow Board = Seiton (Set in order)<br>• Red Tagging = Seiri (Sort/Ringkas)<br>• Visual SOP & Daily Audit = Seiketsu & Shitsuke (Rawat & Rajin)<br>• D dan E adalah bentuk pelanggaran berat tata kelola bengkel industri"
        },
        "hints": {
            "concept": "Tindakan 5S sejati: Red Tagging untuk memilah (B), Shadow Board untuk menata (A), dan Standar SOP Audit harian (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "pkk-sim-30",
        "type": "multi",
        "materi": "HAK DAN KEWAJIBAN KONSUMEN & PELAKU USAHA",
        "topic": "Kewajiban Pelaku Usaha (UU No. 8 Tahun 1999)",
        "stem": "Berdasarkan Undang-Undang No. 8 Tahun 1999 tentang Perlindungan Konsumen (Pasal 7), manakah TIGA kewajiban utama yang wajib dipatuhi oleh unit wirausaha siswa SMK selaku pelaku usaha komersial? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Beriktikad baik dalam melakukan kegiatan usahanya dan memberikan informasi yang benar, jelas, serta jujur mengenai kondisi dan jaminan barang/jasa."},
            {"key": "B", "text": "Memperlakukan atau melayani konsumen secara benar dan jujur serta tidak diskriminatif berdasarkan suku, agama, ras, atau status sosial."},
            {"key": "C", "text": "Memberikan kompensasi, ganti rugi, dan/atau penggantian apabila barang dan/atau jasa yang diterima atau dimanfaatkan tidak sesuai dengan perjanjian."},
            {"key": "D", "text": "Menyembunyikan cacat tersembunyi produk agar barang lekas laku sebelum tanggal kedaluwarsa terlewati."},
            {"key": "E", "text": "Membuat klausul baku sepihak di struk kasir yang menyatakan 'Barang yang sudah dibeli tidak dapat ditukar atau dikembalikan dalam kondisi apapun'."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "PASAL 7 UU NO. 8 TAHUN 1999 (KEWAJIBAN PELAKU USAHA)",
            "latex": "\\text{Kewajiban Pokok} = \\text{Iktikad Baik \& Kejujuran Info} + \\text{Layanan Non-Diskriminatif} + \\text{Ganti Rugi Produk Tidak Sesuai}",
            "legend": "• Pasal 7 Huruf a, b, c, g UUPK: Kewajiban pelaku usaha menjamin mutu, kejujuran info, dan ganti rugi cacat<br>• Catatan: Pilihan E dilarang keras oleh Pasal 18 UUPK (Larangan Klausula Baku pengalihan tanggung jawab)"
        },
        "hints": {
            "concept": "Kewajiban pelaku usaha menurut Pasal 7 UU Perlindungan Konsumen: iktikad baik & jujur (A), melayani tanpa diskriminasi (B), serta memberi ganti rugi jika barang tidak sesuai (C). Klausul sepihak (E) dilarang.",
            "execution": "Pilih A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH ITEMS (pkk-sim-31 to pkk-sim-35)
    # -------------------------------------------------------------
    {
        "id": "pkk-sim-31",
        "type": "matrix",
        "materi": "EVALUASI TITIK IMPAS & KEUANGAN",
        "topic": "Prinsip Analisis Break-Even Point (BEP)",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai konsep Titik Impas (Break-Even Point) dan Margin Kontribusi dalam pengelolaan keuangan wirausaha SMK!",
        "statements": [
            {
                "text": "Titik Impas (BEP) adalah kondisi di mana total pendapatan usaha sama persis dengan total biaya operasional, sehingga usaha membukukan laba bersih nol rupiah.",
                "correct": True
            },
            {
                "text": "Jika biaya variabel per unit diturunkan sementara harga jual dan biaya tetap tidak berubah, maka jumlah unit penjualan untuk mencapai titik impas akan semakin mengecil.",
                "correct": True
            },
            {
                "text": "Margin Kontribusi per unit dihitung dari pengurangan antara Biaya Tetap (Fixed Cost) dengan Biaya Variabel per unit.",
                "correct": False
            },
            {
                "text": "Margin of Safety (Batas Keamanan) menunjukkan persentase seberapa besar penjualan boleh turun sebelum usaha mulai menderita kerugian.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP MATEMATIS BREAK-EVEN POINT",
            "latex": "\\text{BEP}_{\\text{unit}} = \\frac{FC}{P - VC}; \\quad \\text{Margin Kontribusi} = P - VC; \\quad \\text{Margin of Safety} = \\frac{\\text{Aktual} - \\text{BEP}}{\\text{Aktual}}",
            "legend": "• Pernyataan 1 BENAR: Definisi BEP (Total Revenue = Total Cost, Profit = 0)<br>• Pernyataan 2 BENAR: VC turun -> Margin kontribusi naik -> BEP unit mengecil (impas lebih cepat tercapai)<br>• Pernyataan 3 SALAH: Margin Kontribusi = Harga Jual (P) - Biaya Variabel (VC), bukan FC - VC<br>• Pernyataan 4 BENAR: Definisi Margin of Safety (MoS)"
        },
        "hints": {
            "concept": "Pahami rumus BEP unit = FC / (P - VC), rumus margin kontribusi = P - VC, dan konsep Margin of Safety.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    },
    {
        "id": "pkk-sim-32",
        "type": "matrix",
        "materi": "HAK KEKAYAAN INTELEKTUAL (HAKI)",
        "topic": "Komparasi Domain Perlindungan HAKI di Indonesia",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut terkait rezim perlindungan Hak Kekayaan Intelektual (HAKI) di wilayah Republik Indonesia!",
        "statements": [
            {
                "text": "Paten melindungi invensi teknologi baru yang memiliki langkah inventif dan dapat diterapkan dalam industri selama jangka waktu 20 tahun sejak tanggal penerimaan.",
                "correct": True
            },
            {
                "text": "Merek terdaftar dilindungi selama jangka waktu 10 tahun sejak tanggal penerimaan dan masa perlindungannya dapat diperpanjang tanpa batas untuk jangka waktu yang sama.",
                "correct": True
            },
            {
                "text": "Hak Cipta atas program komputer (software aplikasi) menganut sistem First to File dan wajib memperoleh sertifikat pendaftaran sebelum karya tersebut dapat dilindungi.",
                "correct": False
            },
            {
                "text": "Desain Industri melindungi bentuk 3D, konfigurasi, atau komposisi garis dan warna yang memberikan kesan estetis pada suatu komoditas industri selama 10 tahun.",
                "correct": True
            }
        ],
        "formula": {
            "title": "MATRIKS KOMPARASI REZIM HAKI INDONESIA",
            "latex": "\\begin{aligned} \\text{Paten} &: 20 \\text{ Tahun (Invensi Teknologi)} \\\\ \\text{Merek} &: 10 \\text{ Tahun (Dapat Diperpanjang)} \\\\ \\text{Hak Cipta} &: \\text{Deklaratif Otomatis (Seumur Hidup Pencipta } + 70 \\text{ Tahun / } 50 \\text{ Tahun Program)} \\\\ \\text{Desain Industri} &: 10 \\text{ Tahun (Estetika Rupa Produk)} \\end{aligned}",
            "legend": "• Pernyataan 1 BENAR (UU No. 13/2016 Pasal 22)<br>• Pernyataan 2 BENAR (UU No. 20/2016 Pasal 35)<br>• Pernyataan 3 SALAH: Hak Cipta menganut sistem deklaratif (perlindungan otomatis lahir saat ciptaan diwujudkan dalam bentuk nyata, pencatatan di DJKI hanya alat bukti pembuktian)<br>• Pernyataan 4 BENAR (UU No. 31/2000)"
        },
        "hints": {
            "concept": "Paten 20 th (Benar), Merek 10 th dapat diperpanjang (Benar), Hak Cipta deklaratif otomatis bukan konstitutif First to File (Salah), Desain Industri 10 th estetis (Benar).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    },
    {
        "id": "pkk-sim-33",
        "type": "matrix",
        "materi": "LAPORAN KEUANGAN & LIKUIDITAS",
        "topic": "Prinsip Arus Kas dan Solvabilitas Keuangan Bisnis",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai analisis laporan keuangan dan likuiditas usaha rintisan kejuruan!",
        "statements": [
            {
                "text": "Sebuah usaha dapat membukukan laba bersih positif yang tinggi di laporan laba rugi tetapi pada saat yang sama mengalami kebangkrutan likuiditas (arus kas negatif) akibat piutang macet.",
                "correct": True
            },
            {
                "text": "Beban penyusutan (depresiasi) mesin bengkel merupakan pengeluaran kas riil yang langsung memotong saldo uang tunai di buku tabungan bank.",
                "correct": False
            },
            {
                "text": "Rasio Cepat (Quick Ratio / Acid-Test Ratio) tidak memasukkan persediaan barang dagang ke dalam perhitungannya karena persediaan membutuhkan waktu lebih lama untuk diuangkan.",
                "correct": True
            },
            {
                "text": "Arus kas dari aktivitas pendanaan mencakup penerimaan uang tunai dari penjualan jasa harian kepada konsumen di kasir.",
                "correct": False
            }
        ],
        "formula": {
            "title": "PRINSIP AKUNTANSI KEUANGAN KONTEMPORER",
            "latex": "\\text{Quick Ratio} = \\frac{\\text{Kas} + \\text{Bank} + \\text{Piutang}}{\\text{Utang Lancar}}; \\quad \\text{Depreciation} = \\text{Non-Cash Expense}",
            "legend": "• Pernyataan 1 BENAR: Fenomena 'profitable on paper, broke in cash'<br>• Pernyataan 2 SALAH: Depresiasi adalah beban non-kas (non-cash expense) yang tidak melibatkan pengeluaran uang fisik<br>• Pernyataan 3 BENAR: Quick Ratio mengeluarkan persediaan (karena persediaan kurang likuid)<br>• Pernyataan 4 SALAH: Penjualan jasa harian masuk Arus Kas Operasi, bukan Pendanaan"
        },
        "hints": {
            "concept": "Laba tidak sama dengan kas (Benar), Depresiasi adalah beban non-kas bukan kas fisik (Salah), Quick Ratio mengecualikan persediaan (Benar), Penjualan harian = operasi bukan pendanaan (Salah).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "pkk-sim-34",
        "type": "matrix",
        "materi": "MANAJEMEN KUALITAS & STATISTIK (SPC)",
        "topic": "Pengendalian Kualitas Statistik & Metrik Six Sigma",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai pengendalian proses statistik dan manajemen kualitas industri manufaktur modern!",
        "statements": [
            {
                "text": "Tingkat kualitas Six Sigma secara matematis setara dengan toleransi maksimal 3,4 cacat per satu juta peluang (3.4 DPMO).",
                "correct": True
            },
            {
                "text": "Batas kendali statistik (UCL dan LCL) pada peta kendali dihitung dari variabilitas data proses aktual, bukan dari batas toleransi spesifikasi desain teknik (USL dan LSL).",
                "correct": True
            },
            {
                "text": "Diagram Pareto didasarkan pada prinsip aturan 80/20, yaitu 80% cacat produk umumnya disebabkan oleh 20% jenis masalah yang paling vital.",
                "correct": True
            },
            {
                "text": "Jika indeks kapabilitas proses ($C_p$) bernilai 0,5, maka lini produksi dinyatakan sangat kapabel dan mampu menghasilkan produk bebas cacat 100%.",
                "correct": False
            }
        ],
        "formula": {
            "title": "METRIK SIX SIGMA & KAPABILITAS PROSES",
            "latex": "\\text{Six Sigma} = 3{,}4 \\text{ DPMO}; \\quad C_p = \\frac{\\text{USL} - \\text{LSL}}{6\\sigma} \\ge 1{,}33 \\text{ (Standar Kapabel Minimal Industri)}",
            "legend": "• Pernyataan 1 BENAR: Standar Six Sigma dengan pergeseran 1,5-sigma shift menghasilkan 3,4 DPMO<br>• Pernyataan 2 BENAR: UCL/LCL = Voice of the Process (grafik kendali); USL/LSL = Voice of the Customer (desain teknik)<br>• Pernyataan 3 BENAR: Kaidah vital few and trivial many (Vilfredo Pareto)<br>• Pernyataan 4 SALAH: Cp = 0,5 berarti proses tidak kapabel (variasi proses jauh melampaui lebar toleransi desain)"
        },
        "hints": {
            "concept": "Six Sigma = 3,4 DPMO (Benar), UCL/LCL dari data proses bukan toleransi USL/LSL (Benar), Pareto 80/20 (Benar), Cp = 0,5 berarti sangat tidak kapabel karena minimal industri 1,33 (Salah).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "pkk-sim-35",
        "type": "matrix",
        "materi": "KESELAMATAN KERJA & KETENAGAKERJAAN",
        "topic": "Standar K3 Bengkel & Hubungan Industrial Ketenagakerjaan",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut terkait norma Keselamatan dan Kesehatan Kerja (K3) serta regulasi ketenagakerjaan di lingkungan industri!",
        "statements": [
            {
                "text": "Alat Pemadam Api Ringan (APAR) jenis serbuk kimia kering (Dry Chemical Powder) cocok digunakan untuk memadamkan kebakaran Kelas A, B, dan C sekaligus.",
                "correct": True
            },
            {
                "text": "Dalam hirarki pengendalian bahaya K3 (Hierarchy of Controls), penyediaan Alat Pelindung Diri (APD) merupakan garis pertahanan pertama yang paling efektif mengeliminasi bahaya.",
                "correct": False
            },
            {
                "text": "Kecelakaan kerja yang terjadi pada saat pekerja dalam perjalanan resmi dari rumah menuju tempat kerja bengkel diakui dan dijamin oleh program JKK BPJS Ketenagakerjaan.",
                "correct": True
            },
            {
                "text": "Pengusaha yang mempekerjakan karyawan dengan status Perjanjian Kerja Waktu Tertentu (PKWT) dilarang mensyaratkan adanya masa percobaan kerja (probation).",
                "correct": True
            }
        ],
        "formula": {
            "title": "NORMA K3 & KETENAGAKERJAAN REPUBLIK INDONESIA",
            "latex": "\\text{APAR Multipurpose (ABC)} \\wedge \\text{APD = Garis Pertahanan Terakhir (Least Effective)} \\wedge \\text{PKWT No Probation}",
            "legend": "• Pernyataan 1 BENAR: Dry powder efektif untuk Kelas A (benda padat), B (cairan mudah terbakar), dan C (instalasi listrik)<br>• Pernyataan 2 SALAH: APD adalah garis pertahanan terakhir (paling lemah/least effective), yang paling efektif adalah Eliminasi<br>• Pernyataan 3 BENAR: Ruang lingkup JKK BPJS Ketenagakerjaan mencakup kecelakaan lalu lintas rute berangkat/pulang kerja yang wajar<br>• Pernyataan 4 BENAR: Pasal 58 UU Ketenagakerjaan melarang masa percobaan pada PKWT (bila disyaratkan, klausul tersebut batal demi hukum)"
        },
        "hints": {
            "concept": "APAR powder serbaguna ABC (Benar), APD adalah garis pertahanan terakhir paling lemah bukan pertama (Salah), JKK menjamin perjalanan rumah-kerja (Benar), PKWT dilarang masa probation (Benar).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    }
]
