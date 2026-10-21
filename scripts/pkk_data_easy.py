# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Produk Kreatif dan Kewirausahaan (PKK SMK/MAK)
Dataset: Easy Practice (25 Authentic Questions, pkk-lat-e-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

PKK_EASY_ITEMS = [
    {
        "id": "pkk-lat-e-01",
        "materi": "ANALISIS PELUANG USAHA & SWOT",
        "topic": "Matriks SWOT: Strategi ST (Strengths-Threats)",
        "stem": "Sebuah unit produksi siswa SMK memiliki keunggulan internal berupa keterampilan teknis tinggi dalam merancang aplikasi mobile custom (Strength), namun menghadapi ancaman persaingan ketat dari studio software house besar yang memiliki modal promosi masif (Threat). Berdasarkan matriks analisis SWOT, strategi bisnis yang paling tepat diterapkan adalah...",
        "correct": "Strategi ST (Strengths-Threats), yaitu memanfaatkan keahlian teknis internal untuk menciptakan produk spesifik bagi ceruk pasar (niche market) lokal yang belum terlayani oleh studio pengembang besar.",
        "distractors": [
            "Strategi SO (Strengths-Opportunities), yaitu melakukan perang tarif banting harga gila-gilaan dengan studio besar tanpa menghitung biaya operasional.",
            "Strategi WO (Weaknesses-Opportunities), yaitu menutup unit produksi dan menjual seluruh komputer lab ke pasar barang bekas secara mendadak.",
            "Strategi WT (Weaknesses-Threats), yaitu menghentikan seluruh aktivitas riset dan membiarkan produk terbengkalai tanpa pembaruan fitur apa pun.",
            "Strategi Defensif Pasif, yaitu menaikkan harga aplikasi hingga sepuluh kali lipat tanpa menambahkan nilai fungsional produk."
        ],
        "formula": {
            "title": "MATRIKS STRATEGI SWOT KONTEMPORER",
            "latex": "\\text{Strategi ST} = \\text{Strengths (Internal)} \\times \\text{Threats (Eksternal)} \\implies \\text{Mitigasi Ancaman via Keunggulan Unik}",
            "legend": "• SO (Aggressive): Memanfaatkan kekuatan untuk merebut peluang<br>• ST (Diversification): Menggunakan keunggulan unik untuk menangkal ancaman pasar<br>• WO (Turnaround): Meminimalkan kelemahan internal untuk menangkap peluang<br>• WT (Defensive): Meminimalkan kelemahan untuk bertahan dari ancaman"
        },
        "hints": {
            "concept": "Strategi ST mengombinasikan kekuatan internal (keahlian teknis) untuk mengatasi ancaman eksternal (persaingan studio besar) dengan membidik ceruk pasar (niche market).",
            "execution": "Pilih strategi ST yang fokus pada pemanfaatan keahlian unik untuk menembus pasar khusus (niche market)."
        }
    },
    {
        "id": "pkk-lat-e-02",
        "materi": "BUSINESS MODEL CANVAS (BMC)",
        "topic": "9 Blok BMC: Value Proposition vs Customer Segment",
        "stem": "Dalam perancangan Business Model Canvas (BMC) untuk usaha rintisan jasa servis laptop panggilan, tim wirausaha SMK menuliskan: 'Layanan perbaikan laptop di tempat konsumen dalam waktu 2 jam dengan transparansi harga dan garansi 30 hari'. Pernyataan keunggulan solusi tersebut wajib diletakkan pada blok...",
        "correct": "Value Propositions, karena mendefinisikan gabungan nilai keunggulan unik, manfaat solusi, dan pemecahan masalah yang ditawarkan kepada konsumen.",
        "distractors": [
            "Customer Segments, karena menjelaskan karakteristik demografis dan profesi dari pelanggan yang memiliki laptop rusak.",
            "Channels, karena menjabarkan armada sepeda motor yang digunakan teknisi untuk mendatangi rumah konsumen.",
            "Cost Structure, karena menghitung biaya pembelian obeng dan pasta pendingin prosesor laptop.",
            "Key Partnerships, karena menyebutkan toko suku cadang elektronik tempat membeli motherboard cadangan."
        ],
        "formula": {
            "title": "ARSITEKTUR 9 BLOK BUSINESS MODEL CANVAS (OSTERWALDER)",
            "latex": "\\text{Value Proposition} = f(\\text{Pains Relieved}, \\text{Gains Created}) \\iff \\text{Solusi Unik untuk Target Segmen}",
            "legend": "• Value Proposition: Nilai/alasan utama mengapa konsumen memilih produk Anda<br>• Customer Segments: Kelompok konsumen spesifik yang dilayani<br>• Channels: Sarana komunikasi dan distribusi produk kepada pelanggan"
        },
        "hints": {
            "concept": "Value Proposition adalah blok di tengah BMC yang menjelaskan tawaran nilai, keunikan, dan manfaat utama produk/jasa bagi konsumen.",
            "execution": "Janji layanan cepat 2 jam dan garansi transparan adalah penawaran nilai (Value Proposition)."
        }
    },
    {
        "id": "pkk-lat-e-03",
        "materi": "DESAIN & PROTOTYPING PRODUK",
        "topic": "Konsep Minimum Viable Product (MVP)",
        "stem": "Sebuah tim startup siswa SMK ingin meluncurkan platform marketplace barang bekas antar-pelajar sekolah. Sebelum menginvestasikan dana puluhan juta rupiah untuk membangun aplikasi kompleks dengan fitur lengkap, mereka meluncurkan situs web sederhana satu halaman berbasis form daring untuk menguji minat nyata pengguna. Konsep pengembangan produk awal ini dinamakan...",
        "correct": "Minimum Viable Product (MVP), yaitu versi produk paling sederhana yang memiliki fitur esensial minimum untuk memvalidasi hipotesis pasar dengan usaha dan sumber daya terkecil.",
        "distractors": [
            "Final Mass Production, yaitu pelepasan produk matang berskala penuh yang sudah siap dipasarkan ke seluruh dunia tanpa perlu perbaikan lagi.",
            "Mockup Statis 3 Dimensi, yaitu patung tanah liat yang tidak memiliki fungsi operasional sama sekali di layar komputer.",
            "Reverse Engineering, yaitu proses membongkar kode sumber aplikasi kompetitor untuk dijiplak secara ilegal.",
            "End of Life (EOL), yaitu penarikan resmi suatu produk teknologi dari pasaran karena sudah kedaluwarsa."
        ],
        "formula": {
            "title": "SIKLUS LEAN STARTUP: BUILD-MEASURE-LEARN",
            "latex": "\\text{Ide Bisnis} \\xrightarrow{\\text{Build}} \\text{MVP} \\xrightarrow{\\text{Measure}} \\text{Validasi Data} \\xrightarrow{\\text{Learn}} \\text{Pivot / Persevere}",
            "legend": "• MVP: Versi produk awal yang cukup untuk memancing early adopters dan feedback riil<br>• Tujuan: Meminimalkan risiko kerugian modal besar pada ide bisnis yang belum tentu diminati pasar<br>• Fitur: Fokus pada solusi masalah utama (core value) tanpa fitur mewah pelengkap"
        },
        "hints": {
            "concept": "MVP (Minimum Viable Product) adalah produk dengan fitur minimal yang cukup untuk menguji respons pasar nyata dan mengumpulkan umpan balik konsumen.",
            "execution": "Versi awal paling sederhana untuk validasi pasar disebut Minimum Viable Product (MVP)."
        }
    },
    {
        "id": "pkk-lat-e-04",
        "materi": "BIAYA PRODUKSI & PENETAPAN HARGA",
        "topic": "Kalkulasi Break-Even Point (BEP) Unit",
        "stem": "Unit produksi SMK memproduksi lampu hias meja dari limbah kayu dengan rincian biaya: Biaya Tetap (sewa bengkel dan penyusutan alat) sebesar Rp3.000.000 per bulan, Biaya Variabel per unit sebesar Rp50.000, dan produk dijual dengan harga Rp100.000 per unit. Berapakah jumlah unit lampu hias yang harus terjual dalam sebulan agar usaha tersebut mencapai titik impas (Break-Even Point)?",
        "correct": "60 unit, yang diperoleh dari pembagian Biaya Tetap dengan Margin Kontribusi per unit (Rp3.000.000 / (Rp100.000 - Rp50.000) = Rp3.000.000 / Rp50.000 = 60).",
        "distractors": [
            "30 unit, yang merupakan hasil pembagian biaya tetap langsung dengan harga jual tanpa dikurangi biaya variabel bahan baku.",
            "100 unit, yang merupakan hasil penaksiran acak berdasarkan target jumlah siswa di satu jurusan SMK.",
            "50 unit, yang hanya memperhitungkan biaya variabel tanpa mengalokasikan pengembalian biaya sewa bengkel.",
            "120 unit, yang merupakan perhitungan target omzet penjualan kotor dua kali lipat modal pinjaman bank."
        ],
        "formula": {
            "title": "FORMULA BREAK-EVEN POINT (BEP UNIT)",
            "latex": "\\text{BEP}_{\\text{unit}} = \\frac{\\text{Fixed Cost}}{P - \\text{Variable Cost}} = \\frac{3.000.000}{100.000 - 50.000} = \\frac{3.000.000}{50.000} = 60\\,\\text{unit}",
            "legend": "• Fixed Cost (FC): Rp3.000.000 (tetap berapapun jumlah produksi)<br>• Price (P): Rp100.000 (harga jual per unit)<br>• Variable Cost (VC): Rp50.000 (biaya per unit produk)<br>• Margin Kontribusi: $P - VC = 50.000$"
        },
        "hints": {
            "concept": "BEP Unit = Total Biaya Tetap / (Harga Jual - Biaya Variabel per unit).",
            "execution": "Rp3.000.000 / (Rp100.000 - Rp50.000) = Rp3.000.000 / Rp50.000 = 60 unit."
        }
    },
    {
        "id": "pkk-lat-e-05",
        "materi": "PEMASARAN & DIGITAL MARKETING",
        "topic": "Digital Marketing: Model AIDA Funnel",
        "stem": "Dalam merancang kampanye iklan media sosial TikTok untuk produk minuman boba herbal buatan siswa SMK, tim pemasaran membuat video 15 detik dengan 3 detik pertama menampilkan adegan dramatis es batu jatuh ke sirup warna-warni yang menggiurkan dengan suara jernih. Tahapan respon konsumen dalam model pemasaran AIDA yang disasar pada 3 detik pertama tersebut adalah...",
        "correct": "Attention (Kesadaran/Perhatian), yaitu memikat pandangan dan menghentikan jempol audiens yang sedang menggulir layar (hooking) agar memperhatikan pesan promosi.",
        "distractors": [
            "Action (Tindakan Pembelian), yaitu proses ketika konsumen langsung mentransfer uang ke rekening penjual dalam sekejap mata.",
            "Desire (Keinginan Kuat), yaitu tahapan konsumen membandingkan kandungan gizi minuman boba herbal dengan merek lain.",
            "Interest (Ketertarikan Mendalam), yaitu sesi konsumen membaca seluruh artikel ilmiah tentang khasiat tanaman herbal di website resmi.",
            "After-Sales Service, yaitu pemberian kupon perbaikan blender gratis bagi konsumen yang membeli seratus gelas boba."
        ],
        "formula": {
            "title": "MARKETING FUNNEL AIDA (E. ST. ELMO LEWIS)",
            "latex": "\\text{Customer Journey} = \\text{Attention (Hook)} \\longrightarrow \\text{Interest (Story)} \\longrightarrow \\text{Desire (Proof/Offer)} \\longrightarrow \\text{Action (CTA)}",
            "legend": "• Attention (0-3 detik): Menarik atensi visual/suara spontan di feed media sosial<br>• Interest: Membangkitkan rasa penasaran terhadap solusi masalah<br>• Desire: Menciptakan dorongan emosional ingin memiliki produk<br>• Action: Mendorong klik tombol 'Beli Sekarang' atau 'Kunjungi Profil'"
        },
        "hints": {
            "concept": "Huruf 'A' pertama dalam AIDA adalah Attention (Perhatian)—tahapan menangkap perhatian awal pengguna media sosial dalam detik-detik pertama.",
            "execution": "Adegan hook 3 detik pertama bertujuan merebut Attention (perhatian) audiens."
        }
    },
    {
        "id": "pkk-lat-e-06",
        "materi": "HAKI & ASPEK LEGALITAS",
        "topic": "Perizinan Berusaha: Nomor Induk Berusaha (NIB) via OSS",
        "stem": "Seorang wirausahawan muda lulusan SMK mendirikan unit usaha mikro di bidang pembuatan roti rumahan. Untuk melegalkan usahanya agar dapat membuka rekening bank perusahaan dan mengajukan sertifikasi halal, dokumen identitas legalitas tunggal pertama yang wajib diurus secara daring melalui sistem Online Single Submission (OSS) adalah...",
        "correct": "Nomor Induk Berusaha (NIB), yang berfungsi sebagai identitas pelaku usaha, Tanda Daftar Perusahaan (TDP), Angka Pengenal Impor (API), dan akses kepabeanan.",
        "distractors": [
            "Surat Izin Mengemudi (SIM B2 Umum), yang diterbitkan oleh kepolisian untuk pengemudi kendaraan alat berat pengangkut gandum.",
            "Izin Mendirikan Bangunan (IMB) gedung pencakar langit berlantai lima puluh dari kementerian pekerjaan umum.",
            "Paspor Diplomatik Internasional, untuk melakukan perjalanan dinas kepresidenan antar benua secara gratis.",
            "Surat Bebas Narkoba dari dinas perhubungan yang diperbarui setiap dua jam sekali."
        ],
        "formula": {
            "title": "LEGALITAS USAHA MIKRO KECIL (UU CIPTA KERJA / PP 5/2021)",
            "latex": "\\text{Legalitas Tunggal UMK} = \\text{NIB (Online Single Submission / OSS Berbasis Risiko)}",
            "legend": "• NIB: 13 digit angka pengenal identitas resmi pelaku usaha di seluruh Indonesia<br>• Fungsi Integratif: Menggantikan TDP, SIUP, dan IUI untuk kategori risiko rendah<br>• Syarat Wajib: Diperlukan untuk sertifikasi Halal (BPJPH), P-IRT, dan pengajuan kredit KUR"
        },
        "hints": {
            "concept": "NIB (Nomor Induk Berusaha) adalah pintu gerbang legalitas resmi usaha di Indonesia yang diurus via portal OSS (Online Single Submission).",
            "execution": "Dokumen perizinan tunggal terintegrasi untuk wirausaha adalah Nomor Induk Berusaha (NIB)."
        }
    },
    {
        "id": "pkk-lat-e-07",
        "materi": "PENGELOLAAN KEUANGAN & LABA RUGI",
        "topic": "Struktur Laporan Laba Rugi: Laba Kotor vs Laba Bersih",
        "stem": "Dalam laporan keuangan bulanan bengkel las SMK, tercatat Total Penjualan Jasa sebesar Rp20.000.000, Harga Pokok Penjualan/Produksi (biaya kawat las, pelat besi, dan listrik las) sebesar Rp12.000.000, dan Beban Operasional (gaji penjaga toko dan biaya kuota internet pemasaran) sebesar Rp3.000.000. Berapakah nilai Laba Bersih Operasional bengkel las tersebut?",
        "correct": "Rp5.000.000, yang dihitung dari Penjualan dikurangi HPP menghasilkan Laba Kotor Rp8.000.000, kemudian dikurangi Beban Operasional Rp3.000.000 menghasilkan Laba Bersih Rp5.000.000.",
        "distractors": [
            "Rp8.000.000, yang hanya merupakan nilai Laba Kotor tanpa memperhitungkan pemotongan beban operasional kantor.",
            "Rp17.000.000, yang merupakan hasil pengurangan total penjualan dengan biaya pulsa kuota internet saja.",
            "Rp2.000.000, yang dihitung dari pembagian laba kotor dengan jumlah teknisi bengkel las secara sembarangan.",
            "Rp15.000.000, yang merupakan akumulasi seluruh uang kas yang ada di dalam dompet kasir bengkel."
        ],
        "formula": {
            "title": "STRUKTUR LAPORAN LABA RUGI (INCOME STATEMENT)",
            "latex": "\\begin{aligned} \\text{Laba Kotor} &= \\text{Pendapatan Penjualan} - \\text{HPP} = 20\\,\\text{jt} - 12\\,\\text{jt} = 8\\,\\text{jt} \\\\ \\text{Laba Bersih} &= \\text{Laba Kotor} - \\text{Beban Operasional} = 8\\,\\text{jt} - 3\\,\\text{jt} = 5\\,\\text{jt} \\end{aligned}",
            "legend": "• Pendapatan: Total penerimaan kotor dari pelanggan<br>• HPP: Biaya langsung bahan baku & tenaga kerja produksi<br>• Beban Operasional: Biaya administrasi, promosi, dan utilitas kantor"
        },
        "hints": {
            "concept": "Laba Bersih = Pendapatan Penjualan - HPP - Beban Operasional. Laba Kotor = Penjualan - HPP.",
            "execution": "Laba Kotor = 20 jt - 12 jt = 8 jt. Laba Bersih = 8 jt - 3 jt = 5 juta rupiah."
        }
    },
    {
        "id": "pkk-lat-e-08",
        "materi": "PRODUKSI MASSAL & PENGENDALIAN MUTU",
        "topic": "Budaya Kerja 5S / 5R di Ruang Kerja",
        "stem": "Dalam laboratorium perakitan instalasi listrik SMK, instruktur membiasakan siswa melakukan kegiatan memilah dan memisahkan peralatan kerja yang masih terpakai dengan perkakas yang sudah rusak atau tidak diperlukan lagi, kemudian membuang barang yang tidak berguna dari area meja kerja. Prinsip 5S/5R yang sedang diterapkan tersebut adalah...",
        "correct": "Seiri (Ringkas), yaitu memisahkan barang yang diperlukan dengan yang tidak diperlukan dan menyingkirkan barang yang tidak terpakai dari tempat kerja.",
        "distractors": [
            "Seiton (Rapi), yaitu menata dan melabeli tempat penyimpanan peralatan kerja agar mudah diambil saat dibutuhkan.",
            "Seiso (Resik), yaitu membersihkan meja kerja, mesin, dan lantai dari kotoran debu, sisa potongan kabel, dan oli.",
            "Seiketsu (Rawat), yaitu menjaga standardisasi kebersihan dan kerapian tempat kerja secara konsisten.",
            "Shitsuke (Rajin), yaitu mendisiplinkan diri untuk mematuhi seluruh standar kerja K3 secara terus-menerus."
        ],
        "formula": {
            "title": "PRINSIP BUDAYA KERJA 5S / 5R (KAIZEN JEPANG)",
            "latex": "\\text{5S Kaizen} = \\text{Seiri (Ringkas)} \\rightarrow \\text{Seiton (Rapi)} \\rightarrow \\text{Seiso (Resik)} \\rightarrow \\text{Seiketsu (Rawat)} \\rightarrow \\text{Shitsuke (Rajin)}",
            "legend": "• Seiri (Sort / Ringkas): Pilah barang berguna vs tidak berguna, buang sampah/limbah kerja<br>• Seiton (Set in order / Rapi): Tempatkan barang sesuai denah bayangan perkakas<br>• Seiso (Shine / Resik): Bersihkan ruang kerja dari kotoran<br>• Manfaat: Mengeliminasi pemborosan waktu (muda) mencari alat kerja"
        },
        "hints": {
            "concept": "5R: Ringkas (Seiri), Rapi (Seiton), Resik (Seiso), Rawat (Seiketsu), Rajin (Shitsuke). Memilah dan membuang barang yang tak berguna adalah prinsip Ringkas (Seiri).",
            "execution": "Memilah dan menyingkirkan barang yang tidak diperlukan adalah Seiri (Ringkas)."
        }
    },
    {
        "id": "pkk-lat-e-09",
        "materi": "K3LH & KESELAMATAN WIRAUSAHA",
        "topic": "Penggunaan Alat Pelindung Diri (APD) Bengkel Mekanik",
        "stem": "Seorang siswa wirausaha di unit produksi perbengkelan bubut sedang membubut poros besi baja dengan kecepatan putaran spindel 800 RPM. Percikan gram serpihan logam besi panas beterbangan di sekitar mesin. Alat Pelindung Diri (APD) utama yang wajib dikenakan untuk mencegah luka fatal pada indra penglihatan siswa adalah...",
        "correct": "Kacamata pelindung keselamatan (Safety Goggles / Face Shield), yang memiliki pelindung benturan samping dan lensa polikarbonat tahan impak serpihan logam panas.",
        "distractors": [
            "Kacamata hitam gaya santai berbahan kaca tipis tanpa pelindung samping yang rentan pecah saat tertimpa partikel besi.",
            "Topi koboi jerami pelindung terik matahari ladang pertanian.",
            "Masker kain tipis yang dipasang menutupi kedua kelopak mata saat mesin bubut sedang berputar kencang.",
            "Sarung tangan wol rajut longgar dengan benang terurai yang berisiko tinggi terbelit oleh putaran poros spindel mesin."
        ],
        "formula": {
            "title": "STANDAR APD PERMESINAN (PERMENAKER NO. 08/2010)",
            "latex": "\\text{Hazard: Flying Chips } (v > 20\\,\\text{m/s}) \\implies \\text{Safety Goggles ANSI Z87.1 / EN166}",
            "legend": "• Safety Glasses/Goggles: Menahan impak partikel kecepatan tinggi dan tahan panas percikan gram logam<br>• Pantangan Mutlak Membubut: DILARANG menggunakan sarung tangan longgar (risiko tangan tertarik ke spindel putar)<br>• Rambut & Baju: Rambut panjang diikat rapi dan baju werpack terkancing rapat"
        },
        "hints": {
            "concept": "Serpihan gram logam panas dari mesin bubut dapat menyebabkan kebutaan permanen. APD wajib untuk mata adalah Safety Goggles atau Face Shield berstandar impak tinggi.",
            "execution": "Kacamata safety (Safety Goggles/Face Shield) berbahan polikarbonat tahan benturan."
        }
    },
    {
        "id": "pkk-lat-e-10",
        "materi": "BIAYA PRODUKSI & PENETAPAN HARGA",
        "topic": "Metode Cost-Plus Pricing",
        "stem": "Unit wirausaha tata boga SMK membuat kue kering toples dengan Harga Pokok Produksi (HPP) total sebesar Rp40.000 per toples. Manajemen unit usaha menetapkan persentase margin keuntungan (markup) yang diinginkan sebesar 25% dari HPP. Berdasarkan metode penetapan harga Cost-Plus Pricing, harga jual per toples kue kering tersebut adalah...",
        "correct": "Rp50.000, yang dihitung dari HPP Rp40.000 ditambah margin laba 25% (25% x Rp40.000 = Rp10.000, sehingga Rp40.000 + Rp10.000 = Rp50.000).",
        "distractors": [
            "Rp42.500, yang hanya menambahkan nominal angka 25 langsung ke nilai ratusan per toples kue kering.",
            "Rp65.000, yang merupakan penaksiran markup keuntungan sebesar seratus persen di luar formula keuangan.",
            "Rp30.000, yang menyebabkan unit wirausaha mengalami kerugian finansial di bawah biaya pokok produksi.",
            "Rp100.000, yang merupakan harga patokan toples kristal impor berlapis emas di pusat perbelanjaan mewah."
        ],
        "formula": {
            "title": "FORMULA COST-PLUS PRICING",
            "latex": "P = \\text{HPP} + (\\text{Markup} \\times \\text{HPP}) = 40.000 + (0.25 \\times 40.000) = 40.000 + 10.000 = \\text{Rp}50.000",
            "legend": "• HPP: Biaya pokok per unit produk (bahan baku, tenaga kerja, overhead pabrik)<br>• Markup (%): Persentase keuntungan yang ditargetkan pengusaha<br>• Kelebihan: Menjamin seluruh biaya tertutupi dan kepastian margin laba"
        },
        "hints": {
            "concept": "Cost-Plus Pricing: Harga Jual = HPP + (Markup % x HPP).",
            "execution": "Laba = 25% x Rp40.000 = Rp10.000. Harga jual = Rp40.000 + Rp10.000 = Rp50.000."
        }
    },
    {
        "id": "pkk-lat-e-11",
        "materi": "HAKI & ASPEK LEGALITAS",
        "topic": "Sertifikasi P-IRT untuk Produk Industri Rumah Tangga",
        "stem": "Siswa SMK jurusan Agribisnis Pengolahan Hasil Pertanian memproduksi keripik pisang aneka rasa dalam kemasan standing pouch. Untuk dapat mendistribusikan produk camilan tersebut secara legal ke jaringan minimarket modern lokal, izin edar pangan tingkat rumah tangga yang wajib diajukan ke Dinas Kesehatan kabupaten/kota adalah...",
        "correct": "Sertifikat Produksi Pangan Industri Rumah Tangga (SPP-IRT / P-IRT), yang menjamin bahwa olahan pangan telah memenuhi standar keamanan pangan industri rumahan.",
        "distractors": [
            "Izin Edar Alat Kesehatan Radiologi Nuklir dari kementerian energi dan sumber daya mineral.",
            "Sertifikat Kelayakan Terbang Pesawat Penumpang dari kementerian perhubungan udara.",
            "Izin Penggunaan Senjata Api dari markas besar kepolisian republik Indonesia.",
            "Surat Pernyataan Bebas Pajak Penghasilan selama sepuluh abad dari bank pembangunan Asia."
        ],
        "formula": {
            "title": "IZIN EDAR PRODUK PANGAN OLAHAN (BPOM NO. 22/2018)",
            "latex": "\\text{Usaha Pangan Skala Rumah Tangga} \\implies \\text{SPP-PIRT (Dinas Kesehatan via OSS)}",
            "legend": "• P-IRT: Izin edar untuk produk pangan olahan kering risiko rendah/sedang skala UMKM rumahan<br>• BPOM MD: Untuk industri besar/olahan susu/daging/berisiko tinggi (diproduksi di dalam negeri)<br>• Syarat P-IRT: Mengikuti Penyuluhan Keamanan Pangan (PKP) dan lolos inspeksi higienitas dapur"
        },
        "hints": {
            "concept": "Produk makanan kering skala mikro/kecil seperti keripik pisang memerlukan izin edar P-IRT (Pangan Industri Rumah Tangga) dari Dinas Kesehatan setempat.",
            "execution": "P-IRT adalah sertifikat resmi untuk produk pangan industri rumah tangga."
        }
    },
    {
        "id": "pkk-lat-e-12",
        "materi": "ANALISIS PELUANG USAHA & SWOT",
        "topic": "Identifikasi Masalah Pasar (Customer Pain Points)",
        "stem": "Sekelompok siswa SMK mengamati bahwa para ibu rumah tangga di perumahan sekitar sekolah sering mengeluh kesulitan memotong bawang merah karena mata terasa sangat perih dan memakan waktu lama saat menyiapkan sarapan pagi. Kondisi ketidaknyamanan konsumen tersebut dalam analisis peluang bisnis dikategorikan sebagai...",
        "correct": "Customer Pain Point, yaitu masalah, hambatan, atau frustrasi spesifik yang dialami calon pelanggan yang membuka peluang bagi terciptanya produk solusi yang bernilai jual.",
        "distractors": [
            "Customer Lifetime Value, yaitu total nominal keuntungan finansial yang disetorkan konsumen ke bank selama sepuluh tahun berturut-turut.",
            "Brand Advocacy, yaitu tindakan ibu rumah tangga menyebarkan brosur promosi di arisan tanpa dibayar.",
            "Price Skimming, yaitu kebijakan mematok harga sayuran setinggi langit saat musim panen bawang.",
            "Break-Even Time, yaitu durasi waktu yang dibutuhkan bawang merah untuk bertunas di dalam lemari es."
        ],
        "formula": {
            "title": "CUSTOMER DISCOVERY: PAIN POINTS & VALUE CREATION",
            "latex": "\\text{Inovasi Wirausaha Berhasil} = \\text{Validasi Masalah Nyata (Pain Points)} \\times \\text{Solusi Praktis Terjangkau}",
            "legend": "• Pain Points: Masalah fungsional, finansial, atau proses yang menyulitkan konsumen<br>• Peluang Produk: Alat pengiris bawang putar mekanik manual cepat tanpa perih<br>• Fondasi: 'Sell the problem you solve, not the product you build'"
        },
        "hints": {
            "concept": "Keluhan, kerepotan, atau rasa frustrasi yang dialami konsumen adalah Customer Pain Point (titik sakit konsumen) yang memicu ide inovasi bisnis.",
            "execution": "Ketidaknyamanan mata perih saat mengiris bawang adalah Customer Pain Point."
        }
    },
    {
        "id": "pkk-lat-e-13",
        "materi": "PEMASARAN & DIGITAL MARKETING",
        "topic": "Metrik Pemasaran Digital: ROAS (Return on Ad Spend)",
        "stem": "Sebuah toko daring unit produksi busana SMK mengeluarkan biaya iklan berbayar di Instagram Ads sebesar Rp1.000.000 selama seminggu. Dari penayangan iklan tersebut, mereka berhasil membukukan total pendapatan penjualan baju sebesar Rp4.000.000. Berapakah nilai Return on Ad Spend (ROAS) kampanye iklan tersebut?",
        "correct": "4x (atau 400%), yang dihitung dari total pendapatan penjualan dibagi dengan total biaya belanja iklan (Rp4.000.000 / Rp1.000.000 = 4).",
        "distractors": [
            "1x, yang berarti unit usaha mengalami kerugian finansial karena uang iklan hilang tanpa sisa penjualan.",
            "0.25x, yang dihitung dari pembagian terbalik biaya iklan dengan pendapatan kotor penjualan baju.",
            "40x, yang merupakan estimasi berlebihan tanpa dasar perhitungan matematis akuntansi periklanan.",
            "10x, yang merupakan jumlah klik yang dilakukan oleh staf admin toko daring sendiri."
        ],
        "formula": {
            "title": "METRIK DIGITAL MARKETING: FORMULA ROAS",
            "latex": "\\text{ROAS} = \\frac{\\text{Total Pendapatan Iklan (Revenue)}}{\\text{Total Belanja Iklan (Ad Spend)}} = \\frac{4.000.000}{1.000.000} = 4\\text{x (atau } 400\\%)",
            "legend": "• ROAS > 1: Pendapatan melebihi biaya belanja iklan (positif)<br>• ROAS = 1: Pendapatan impas tepat setara biaya belanja iklan<br>• Benchmark E-Commerce: ROAS 3x - 5x umumnya dibutuhkan untuk menutup HPP dan biaya operasional"
        },
        "hints": {
            "concept": "ROAS (Return on Ad Spend) mengukur efektivitas belanja iklan: Pendapatan Iklan / Biaya Iklan.",
            "execution": "Rp4.000.000 / Rp1.000.000 = 4x (atau 400%)."
        }
    },
    {
        "id": "pkk-lat-e-14",
        "materi": "PRODUKSI MASSAL & PENGENDALIAN MUTU",
        "topic": "Metode Persediaan FIFO (First In First Out)",
        "stem": "Gudang penyimpanan bahan baku toko roti wirausaha SMK menerapkan sistem manajemen pergudangan di mana stok tepung terigu, ragi instan, dan telur ayam yang dibeli dan masuk gudang paling awal wajib dikeluarkan dan digunakan terlebih dahulu untuk proses produksi roti hari ini. Metode perputaran arus barang persediaan ini disebut...",
        "correct": "FIFO (First In First Out), yaitu barang persediaan yang pertama kali masuk ke gudang merupakan barang yang pertama kali harus dikeluarkan untuk menjaga kesegaran bahan dan mencegah kerusakan kedaluwarsa.",
        "distractors": [
            "LIFO (Last In First Out), di mana tepung terigu yang baru dibeli kemarin sore wajib digunakan duluan sementara stok lama dibiarkan membusuk di sudut gudang.",
            "Average Costing, di mana seluruh karung tepung terigu ditenggelamkan ke dalam bak air untuk dihitung massa jenis rata-ratanya.",
            "Just In Time Ekstrem, di mana koki roti hanya boleh membeli tepung setelah adonan dimasukkan ke dalam loyang pemanggang oven.",
            "Random Shuffling, di mana karung bahan baku dilemparkan secara acak ke seluruh penjuru ruangan setiap pagi."
        ],
        "formula": {
            "title": "SISTEM MANAJEMEN INVENTORY FIFO (PSAK NO. 14)",
            "latex": "\\text{FIFO Method} \\implies \\text{Bahan Masuk Awal} \\xrightarrow{\\text{Prioritas Produksi}} \\text{Keluar Awal} \\implies \\text{Risiko Expired} \\approx 0",
            "legend": "• FIFO (First In First Out): Mutlak diterapkan pada produk makanan, farmasi, dan barang rentan basi<br>• Keuntungan: Menjaga kualitas bahan segar, rotasi stok teratur, dan mencegah penumpukan barang basi<br>• FEFO (First Expired First Out): Varian berbasis tanggal kedaluwarsa terdekat"
        },
        "hints": {
            "concept": "Barang yang pertama kali masuk harus pertama kali keluar untuk mencegah kedaluwarsa pada bahan makanan basah/baku: FIFO (First In First Out).",
            "execution": "Barang pertama masuk digunakan pertama kali adalah metode FIFO."
        }
    },
    {
        "id": "pkk-lat-e-15",
        "materi": "BUSINESS MODEL CANVAS (BMC)",
        "topic": "9 Blok BMC: Revenue Streams (Arus Pendapatan)",
        "stem": "Sebuah tim siswa SMK merancang model bisnis game edukasi sejarah untuk anak-anak sekolah dasar. Model monetisasi yang mereka tetapkan terdiri dari dua cara: pembelian aplikasi berbayar sekali beli di awal sebesar Rp25.000 dan penjualan paket kostum karakter digital tambahan di dalam game (in-app purchase). Sumber pemasukan keuangan ini dalam 9 blok BMC dicatat pada bagian...",
        "correct": "Revenue Streams, karena mencatat representasi uang tunai yang dihasilkan perusahaan dari masing-masing segmen pelanggan melalui mekanisme penetapan harga tertentu.",
        "distractors": [
            "Cost Structure, karena mendata seluruh tagihan listrik server dan gaji bulanan animator 3D.",
            "Key Activities, karena menjabarkan jadwal kerja para programmer mengetik kode bahasa pemrograman.",
            "Key Resources, karena mencatat jumlah unit komputer PC gaming yang ada di laboratorium sekolah.",
            "Customer Relationships, karena menjelaskan cara admin menyapa pelanggan di media sosial."
        ],
        "formula": {
            "title": "BLOK BMC: REVENUE STREAMS (ARUS PENDAPATAN)",
            "latex": "\\text{Revenue Streams} = \\sum (\\text{Volume Transaksi} \\times \\text{Harga Satuan}) + \\text{Recurring / In-App}",
            "legend": "• Revenue Streams: Aliran uang masuk dari nilai yang berhasil dihantarkan ke konsumen<br>• Model Monetisasi: Penjualan aset, biaya langganan, sewa, lisensi, in-app purchase, iklan<br>• Pertanyaan Kunci: 'Berapa konsumen bersedia membayar dan bagaimana cara mereka membayar?'"
        },
        "hints": {
            "concept": "Revenue Streams adalah blok BMC yang merinci semua sumber aliran pemasukan pendapatan kas dari konsumen.",
            "execution": "Pembelian aplikasi dan in-app purchase dicatat di blok Revenue Streams."
        }
    },
    {
        "id": "pkk-lat-e-16",
        "materi": "HAKI & ASPEK LEGALITAS",
        "topic": "Bentuk Badan Usaha: PT Perorangan untuk Usaha Mikro Kecil",
        "stem": "Pemerintah Indonesia melalui UU Cipta Kerja memberikan kemudahan bagi wirausahawan pemula lulusan SMK untuk mendirikan badan hukum berstatus Perseroan Terbatas yang didirikan oleh 1 orang pendiri saja tanpa kewajiban memiliki partner sekutu dan tanpa syarat besaran modal dasar minimum. Bentuk badan usaha modern ini dikenal sebagai...",
        "correct": "PT Perorangan (Perseroan Perorangan), yang diperuntukkan khusus bagi Usaha Mikro dan Kecil (UMK) dengan status badan hukum terpisah yang melindungi aset pribadi pendiri.",
        "distractors": [
            "Firma Kongsi Dagang, di mana seluruh sekutu bertanggung jawab secara pribadi dengan harta kekayaan keluarga tanpa batas perlindungan hukum.",
            "Badan Usaha Milik Negara (BUMN) Persero Terbuka, yang seluruh sahamnya wajib dimiliki oleh presiden republik Indonesia secara pribadi.",
            "Koperasi Multinasional Asing, yang izin operasionalnya harus disahkan oleh sidang umum perserikatan bangsa-bangsa di New York.",
            "Yayasan Amal Nirlaba Tertutup, yang dilarang keras menjual barang dagangan atau mencari laba komersial sama sekali."
        ],
        "formula": {
            "title": "PERSEROAN PERORANGAN (PP NO. 8 TAHUN 2021)",
            "latex": "\\text{PT Perorangan} = \\text{1 Pendiri (WNI } \\ge 17\\,\\text{th)} + \\text{Badan Hukum Terpisah} + \\text{Kriteria UMK}",
            "legend": "• Keunggulan Utama: Pemisahan kekayaan pribadi dengan kekayaan usaha (tanggung jawab terbatas)<br>• Prosedur Cepat: Pendaftaran elektronik di Kemenkumham tanpa perlu akta notaris mahal<br>• Kriteria Modal UMK: Modal usaha maksimal Rp1 Miliar (mikro) atau hingga Rp5 Miliar (kecil)"
        },
        "hints": {
            "concept": "PT Perorangan adalah inovasi hukum bisnis Indonesia untuk UMK yang memungkinkan 1 orang mendirikan PT berbadan hukum resmi tanpa modal minimum.",
            "execution": "Badan hukum untuk 1 orang pendiri UMK adalah PT Perorangan (Perseroan Perorangan)."
        }
    },
    {
        "id": "pkk-lat-e-17",
        "materi": "BIAYA PRODUKSI & PENETAPAN HARGA",
        "topic": "Perhitungan Harga Pokok Produksi (HPP)",
        "stem": "Dalam satu sesi produksi sabun cuci piring cair sebanyak 200 botol, unit produksi kimia industri SMK mengeluarkan biaya: Bahan Baku (surfaktan dan pewangi) Rp800.000, Botol kemasan dan label stiker Rp400.000, dan Upah tenaga kerja produksi siswa Rp400.000. Berapakah Harga Pokok Produksi (HPP) per botol sabun cuci piring tersebut?",
        "correct": "Rp8.000 per botol, yang dihitung dari total biaya produksi dibagi dengan jumlah produk yang dihasilkan (Rp1.600.000 / 200 botol = Rp8.000).",
        "distractors": [
            "Rp4.000 per botol, yang hanya menghitung biaya bahan baku kimia surfaktan tanpa memperhitungkan botol dan upah kerja.",
            "Rp16.000 per botol, yang dihitung dari pengalian biaya kemasan botol dengan persentase laba kotor toko kelontong.",
            "Rp2.000 per botol, yang didapat dari pembagian biaya upah kerja siswa dengan total jumlah botol tanpa biaya bahan.",
            "Rp80.000 per botol, yang merupakan kekeliruan perhitungan peletakan titik desimal pada kalkulator kasir."
        ],
        "formula": {
            "title": "FORMULA HARGA POKOK PRODUKSI (HPP PER UNIT)",
            "latex": "\\text{HPP per Unit} = \\frac{\\text{Total Biaya Produksi (Bahan + Kemasan + Tenaga Kerja)}}{\\text{Jumlah Unit Dihasilkan (Q)}} = \\frac{1.600.000}{200} = \\text{Rp}8.000",
            "legend": "• Total Biaya = Rp800.000 + Rp400.000 + Rp400.000 = Rp1.600.000<br>• Output Produksi = 200 botol<br>• HPP: Nilai dasar untuk menentukan harga jual aman di atas titik modal"
        },
        "hints": {
            "concept": "HPP per unit = Total Biaya Produksi / Jumlah Produk yang dihasilkan.",
            "execution": "Total Biaya = 800rb + 400rb + 400rb = 1.600.000. HPP = 1.600.000 / 200 = Rp8.000 per botol."
        }
    },
    {
        "id": "pkk-lat-e-18",
        "materi": "DESAIN & PROTOTYPING PRODUK",
        "topic": "Tahapan Prototyping: Mockup vs Functional Prototype",
        "stem": "Tim siswa SMK jurusan Teknik Pemesinan merancang inovasi alat perajang rumput pakan ternak otomatis. Pada tahap awal, mereka membuat model skala 1:5 dari bahan karton dan plastik akrilik untuk mempresentasikan bentuk fisik, proporsi rangka, dan letak tombol kepada calon investor tanpa motor mesin penggerak yang menyala. Model representasi fisik visual awal tersebut disebut...",
        "correct": "Mockup (Desain Model Visual), yaitu representasi visual berdimensi nyata yang menampilkan tampilan fisik, gaya, dan proporsi produk tanpa dilengkapi fungsi mekanis operasional kerja yang sesungguhnya.",
        "distractors": [
            "Functional Working Prototype, yaitu mesin nyata berskala 1:1 yang sudah dipasangi pisau baja tajam dan mesin diesel menyala di kandang sapi.",
            "Mass Production Tooling, yaitu cetakan baja hidrolik pabrik yang memproduksi 100.000 unit mesin pemotong rumput per hari.",
            "Product Recall, yaitu penarikan mesin dari tangan petani karena motor mesin terbukti mengeluarkan asap tebal beracun.",
            "Buku Manual Reparasi, yaitu lembaran kertas fotokopi petunjuk pembongkaran baut karburator mesin traktor."
        ],
        "formula": {
            "title": "SPEKTRUM EVOLUSI PROTOTYPE PRODUK",
            "latex": "\\text{Sketsa Ide 2D} \\longrightarrow \\text{Mockup Visual (Estetika & Skala)} \\longrightarrow \\text{Working Prototype (Fungsional)} \\longrightarrow \\text{MVP}",
            "legend": "• Mockup: Model skala non-fungsional untuk validasi bentuk ergonomis, estetika, dan pitch investor<br>• Working Prototype: Model fungsional untuk uji kekuatan beban, getaran, dan keandalan mekanis<br>• Biaya Efisien: Mockup karton/akrilik mempermudah revisi dimensi sebelum pembubutan logam mahal"
        },
        "hints": {
            "concept": "Model fisik untuk melihat wujud estetika dan proporsi tanpa fungsi mesin yang bekerja disebut Mockup (skala visual).",
            "execution": "Model fisik representasi bentuk tanpa mesin operasional adalah Mockup."
        }
    },
    {
        "id": "pkk-lat-e-19",
        "materi": "PENGELOLAAN KEUANGAN & LABA RUGI",
        "topic": "Persamaan Dasar Akuntansi (Neraca)",
        "stem": "Dalam pembukuan keuangan dasar unit usaha wirausaha sekolah, persamaan matematika neraca yang wajib selalu berada dalam kondisi seimbang (balance) antara sisi kiri dan sisi kanan adalah...",
        "correct": "Aset (Aktiva) = Liabilitas (Kewajiban/Utang) + Ekuitas (Modal Sendiri).",
        "distractors": [
            "Aset (Aktiva) = Pendapatan Penjualan dikalikan dengan Biaya Promosi Iklan Media Sosial.",
            "Modal Sendiri = Utang Usaha dibagi dengan Jumlah Seluruh Karyawan Toko.",
            "Laba Bersih = Seluruh Uang Kas yang dipinjam dari rentenir tanpa batas waktu pengembalian.",
            "Kewajiban = Aset Kas ditambah dengan Kerugian Piutang Tak Tertagih secara eksponensial."
        ],
        "formula": {
            "title": "PERSAMAAN DASAR AKUNTANSI KEUANGAN",
            "latex": "\\text{Aset (Assets)} = \\text{Liabilitas (Liabilities)} + \\text{Ekuitas (Equity)}",
            "legend": "• Aset: Sumber daya ekonomi yang dikuasai usaha (Kas, Piutang, Perlengkapan, Mesin)<br>• Liabilitas: Klaim pihak luar berupa utang dagang atau pinjaman bank<br>• Ekuitas: Hak residual pemilik usaha atas aset setelah dikurangi seluruh kewajiban"
        },
        "hints": {
            "concept": "Persamaan dasar akuntansi neraca adalah: Aset = Kewajiban (Liabilitas) + Modal (Ekuitas).",
            "execution": "Aset = Liabilitas + Ekuitas."
        }
    },
    {
        "id": "pkk-lat-e-20",
        "materi": "PEMASARAN & DIGITAL MARKETING",
        "topic": "Perbedaan Pemasaran Organik vs Berbayar (Paid Ads)",
        "stem": "Sebuah usaha sablon kaos siswa SMK ingin mempromosikan layanannya di media sosial tanpa mengeluarkan modal uang sepeser pun untuk beriklan, melainkan dengan memproduksi video tutorial proses menyablon yang menarik, memanfaatkan tagar (#) yang relevan, dan mengajak pengikut berinteraksi di kolom komentar. Strategi pemasaran ini dikenal sebagai...",
        "correct": "Pemasaran Organik (Organic Marketing), yaitu strategi menarik calon konsumen secara alami mengandalkan konten berkualitas, konsistensi algoritma platform, dan interaksi komunitas tanpa membayar biaya penayangan iklan berbayar.",
        "distractors": [
            "Pay-Per-Click (PPC) Advertising, yaitu kampanye iklan di mana pemilik akun membayar setiap kali tombol tautan iklan diklik oleh pengguna internet.",
            "Influencer Endorsement Mahal, yaitu membayar artis papan atas senilai ratusan juta rupiah untuk memegang kaos di acara gala premiere.",
            "Spamming Ilegal, yaitu mengirimkan ribuan pesan promosi otomatis yang mengganggu ke nomor WhatsApp pribadi orang asing setiap menit.",
            "Pemasaran Billboard Raksasa, yaitu menyewa papan reklame lampu LED di bundaran jalan protokol kota metropolitan."
        ],
        "formula": {
            "title": "STRATEGI PEMASARAN KONTEN MEDIA SOSIAL",
            "latex": "\\text{Pertumbuhan Organik} = f(\\text{Kualitas Konten}, \\text{Relevansi Algoritma}, \\text{Engagement Rate}) \\iff \\text{Biaya Iklan} = 0",
            "legend": "• Organik: Membangun kepercayaan jangka panjang dan komunitas loyal (biaya tunai nol, butuh waktu & kreativitas)<br>• Paid Ads: Mendatangkan konversi cepat dengan biaya per klik/impresi<br>• Kombinasi Ideal: Konten organik untuk membangun relasi, paid ads untuk akselerasi promosi musiman"
        },
        "hints": {
            "concept": "Pemasaran tanpa membayar biaya pasang iklan yang mengandalkan konten bermutu dan interaksi sosial disebut Pemasaran Organik (Organic Marketing).",
            "execution": "Pemasaran berbasis konten alami tanpa biaya penayangan iklan adalah Pemasaran Organik."
        }
    },
    {
        "id": "pkk-lat-e-21",
        "materi": "ANALISIS PELUANG USAHA & SWOT",
        "topic": "Analisis Peluang: Metode Amati, Tiru, Modifikasi (ATM)",
        "stem": "Seorang siswa SMK melihat kesuksesan gerobak minuman kopi susu gula aren yang sedang viral di kotanya. Alih-alih menjiplak persis produk tersebut, siswa tersebut menambahkan inovasi berupa ekstrak rempah kayu manis lokal dan kemasan botol ramah lingkungan dengan harga lebih terjangkau. Pendekatan penciptaan inovasi usaha ini menerapkan prinsip...",
        "correct": "Amati, Tiru, dan Modifikasi (ATM), di mana pengusaha mempelajari formula sukses bisnis yang sudah ada di pasar, lalu memberikan nilai tambah diferensiasi baru yang unik untuk memenangkan kompetisi pasar.",
        "distractors": [
            "Plagiarisme Murni Ilegal, yaitu meniru seluruh nama merek, logo, dan resep kompetitor secara diam-diam tanpa izin.",
            "Monopoli Dagang Tertutup, yaitu menyuap aparat penegak hukum untuk menutup seluruh gerai kopi lain di wilayah kecamatan.",
            "Price Dumping Kriminal, yaitu menjual produk dengan harga rugi total untuk menghancurkan ekonomi keluarga petani kopi.",
            "Spekulasi Saham Valas, yaitu bertaruh pada pergerakan mata uang asing tanpa memproduksi minuman kopi fisik."
        ],
        "formula": {
            "title": "PRINSIP INOVASI NILAI: TEKNIK ATM",
            "latex": "\\text{Inovasi ATM} = \\text{Amati (Benchmarking)} + \\text{Tiru (Best Practice)} + \\text{Modifikasi (Value-Added Differentiation)}",
            "legend": "• Amati: Menganalisis kelebihan produk kompetitor dan respons konsumen<br>• Tiru: Mengadopsi pola dasar operasional yang terbukti berhasil<br>• Modifikasi: Memberikan keunikan baru (rasa rempah, kemasan ramah lingkungan, pelayanan prima)"
        },
        "hints": {
            "concept": "Teknik ATM (Amati, Tiru, Modifikasi) mempelajari keunggulan kompetitor lalu menambahkan modifikasi nilai pembeda (diferensiasi).",
            "execution": "Mempelajari kesuksesan kompetitor dan memberi nilai tambah baru menerapkan prinsip ATM."
        }
    },
    {
        "id": "pkk-lat-e-22",
        "materi": "K3LH & KESELAMATAN WIRAUSAHA",
        "topic": "Penataan Ruang Produksi & Ergonomi Angkat Beban Manual",
        "stem": "Dalam operasional gudang bahan baku unit usaha SMK, staf gudang sering mengangkat karung beras seberat 25 kg dari lantai ke atas truk pengangkut. Menurut standar ergonomi keselamatan kerja K3LH, teknik manual lifting yang benar untuk mencegah cedera saraf tulang pinggang (Herniated Nucleus Pulposus / HNP) adalah...",
        "correct": "Menekuk kedua lutut dalam posisi jongkok stabil, menjaga punggung tetap tegak lurus, memegang karung dekat dengan dada, lalu mengangkat beban bertumpu pada kekuatan otot paha kaki, bukan membungkukkan pinggang.",
        "distractors": [
            "Menjaga kedua kaki tetap lurus kaku dan membungkukkan punggung sejajar lantai lalu menyentak beban sekuat tenaga ke atas.",
            "Mengangkat karung beras sambil memutar pinggang 90 derajat secara mendadak ke arah kanan sambil tertawa terbahak-bahak.",
            "Melemparkan karung beras ke udara menggunakan kepala tanpa memegang dengan kedua tangan sama sekali.",
            "Menahan karung beras di ujung jari tangan sambil berjalan jinjit di atas tumpukan lantai berminyak licin."
        ],
        "formula": {
            "title": "STANDAR ERGONOMI MANUAL HANDLING (OSHA / NIOSH)",
            "latex": "\\text{Lifting Posture}: \\quad \\text{Power from Legs (Quadriceps)} \\gg \\text{Back Bending (Spinal Stress)}",
            "legend": "• Posisi Benar: Tekuk lutut (squat), punggung lurus, beban didekap dekat titik berat tubuh (CoG)<br>• Bahaya Membungkuk: Beban pada cakram tulang belakang L5-S1 melonjak hingga 10x lipat berat beban<br>• Batas Angkat Manual Aman: Pria dewasa 20-25 kg, wanita 12-15 kg"
        },
        "hints": {
            "concept": "Teknik mengangkat beban berat manual handling: tekuk lutut (jongkok), punggung tetap lurus, gunakan kekuatan paha kaki, bukan membungkukkan punggung.",
            "execution": "Menekuk lutut (jongkok), punggung tegak lurus, dan bertumpu pada otot paha kaki."
        }
    },
    {
        "id": "pkk-lat-e-23",
        "materi": "PRODUKSI MASSAL & PENGENDALIAN MUTU",
        "topic": "Siklus Manajemen Kualitas PDCA (Deming Cycle)",
        "stem": "Dalam menjaga konsistensi mutu produk keramik hias di unit wirausaha kriya SMK, instruktur menerapkan siklus kendali mutu berkesinambungan (Continuous Improvement): merencanakan perbaikan formula tanah liat, melaksanakan uji coba pembakaran, memeriksa persentase keramik yang retak, lalu menstandardisasi prosedur baru jika berhasil. Siklus manajemen mutu ini dikenal sebagai...",
        "correct": "Siklus PDCA (Plan - Do - Check - Act / Deming Cycle), yaitu metodologi manajemen berulang empat langkah untuk pengendalian kualitas dan perbaikan proses kerja secara berkelanjutan.",
        "distractors": [
            "Siklus SWOT Kriminal, di mana pengusaha mencari kelemahan aparat penegak hukum untuk menghindari pembayaran pajak.",
            "Metode Piramida Keuangan Cepat, yaitu skema penggandaan uang fiktif melalui arisan berantai ilegal.",
            "Sistem Lotere Acak, di mana kualitas produk ditentukan murni oleh pelemparan dadu bermata enam di awal shift kerja.",
            "Siklus E-Commerce Dropping, di mana pesanan barang dikirim ke alamat acak tanpa pesanan pembeli."
        ],
        "formula": {
            "title": "SIKLUS KONTROL MUTU TOTAL: PDCA (W. EDWARDS DEMING)",
            "latex": "\\text{Plan (Rencana Target)} \\longrightarrow \\text{Do (Uji Coba Skala Kecil)} \\longrightarrow \\text{Check (Audit Hasil Data)} \\longrightarrow \\text{Act (Standardisasi SOP)}",
            "legend": "• Plan: Identifikasi masalah mutu dan rumuskan hipotesis tindakan perbaikan<br>• Do: Jalankan rencana perbaikan pada lini percontohan terbatas<br>• Check: Ukur efektivitas, bandingkan hasil cacat produk sebelum vs sesudah<br>• Act: Jadikan SOP baku bila sukses, atau ulangi siklus bila gagal"
        },
        "hints": {
            "concept": "Siklus Plan-Do-Check-Act (PDCA) atau Deming Cycle adalah metodologi perbaikan kualitas berkelanjutan (continuous improvement).",
            "execution": "Metodologi 4 langkah Plan-Do-Check-Act disebut Siklus PDCA."
        }
    },
    {
        "id": "pkk-lat-e-24",
        "materi": "HAKI & ASPEK LEGALITAS",
        "topic": "Sertifikasi Halal Produk Makanan UMKM (BPJPH)",
        "stem": "Berdasarkan regulasi jaminan produk halal di Indonesia (UU No. 33 Tahun 2014), seluruh produk makanan dan minuman yang diperjualbelikan di wilayah Indonesia wajib bersertifikat halal. Badan pemerintah resmi di bawah Kementerian Agama yang berwenang menerbitkan sertifikat halal bagi produk UMKM adalah...",
        "correct": "Badan Penyelenggara Jaminan Produk Halal (BPJPH), yang bekerja sama dengan Lembaga Pemeriksa Halal (LPH) dan Komisi Fatwa Majelis Ulama Indonesia (MUI).",
        "distractors": [
            "Badan Narkotika Nasional (BNN), yang bertugas memberantas peredaran zat psikotropika ilegal di tempat hiburan malam.",
            "Komisi Pemberantasan Korupsi (KPK), yang bertugas melakukan operasi tangkap tangan tindak pidana korupsi pejabat negara.",
            "Badan Meteorologi, Klimatologi, dan Geofisika (BMKG), yang bertugas memprediksi potensi gempa bumi dan tsunami samudera.",
            "Otoritas Jasa Keuangan (OJK), yang mengawasi perdagangan saham dan operasional perbankan di pasar modal."
        ],
        "formula": {
            "title": "EKOSISTEM JAMINAN PRODUK HALAL (JPH INDONESIA)",
            "latex": "\\text{Pendaftaran UMK} \\xrightarrow{\\text{BPJPH}} \\text{Pemeriksaan Bahan (LPH)} \\xrightarrow{\\text{Sidang Fatwa (MUI)}} \\text{Penerbitan Sertifikat (BPJPH)}",
            "legend": "• BPJPH (Kemenag): Regulator administratif & penerbit sertifikat halal resmi negara<br>• LPH (LPPOM MUI, Sucofindo, dll): Auditor teknis penguji kandungan bahan di laboratorium<br>• Komisi Fatwa MUI: Penetap kehalalan produk secara syariat Islam"
        },
        "hints": {
            "concept": "Lembaga pemerintah penerbit sertifikat halal resmi di Indonesia sejak UU JPH adalah BPJPH (Badan Penyelenggara Jaminan Produk Halal) Kemenag.",
            "execution": "Badan Penyelenggara Jaminan Produk Halal (BPJPH)."
        }
    },
    {
        "id": "pkk-lat-e-25",
        "materi": "PENGELOLAAN KEUANGAN & LABA RUGI",
        "topic": "Arus Kas (Cash Flow): Kas Masuk vs Kas Keluar",
        "stem": "Sebuah usaha sabun herbal siswa SMK membukukan penjualan yang sangat laris secara kredit dengan nilai faktur piutang Rp30.000.000 dalam sebulan. Namun pada akhir bulan, mereka tidak mampu membayar tagihan listrik bengkel dan upah pekerja sebesar Rp5.000.000 karena uang kas fisik di dompet kasir hanya tersisa Rp200.000. Masalah krusial yang dialami usaha tersebut adalah...",
        "correct": "Krisis Arus Kas (Cash Flow Deficit / Insolvensi Jangka Pendek), di mana usaha menghasilkan laba akuntansi di atas kertas tetapi kekurangan likuiditas uang kas nyata akibat piutang dagang yang belum tertagih.",
        "distractors": [
            "Peningkatan Nilai Ekuitas Saham, di mana perusahaan secara otomatis memenuhi syarat penawaran umum perdana di bursa efek London.",
            "Kebakaran Modal Permanen, di mana seluruh uang kas kertas di kasir terbakar oleh aliran listrik tegangan tinggi.",
            "Penipuan Pajak Berkelanjutan, di mana desainer sengaja menyembunyikan uang di dalam brankas besi dasar laut.",
            "Inflasi Moneter Global, yang menyebabkan seluruh nilai mata uang di dunia diturunkan menjadi pecahan tembaga."
        ],
        "formula": {
            "title": "PRINSIP CASH FLOW: PROFIT $\\neq$ CASH",
            "latex": "\\text{Net Operating Cash Flow} = \\text{Penerimaan Kas Nyata} - \\text{Pengeluaran Kas Nyata} < 0 \\implies \\text{Insolvency Risk}",
            "legend": "• 'Revenue is vanity, Profit is sanity, but Cash is king'<br>• Piutang Dagang Belum Cair: Penjualan kredit tercatat sebagai laba di laporan laba rugi, namun kas riil nol<br>• Solusi: Batasi tempo piutang maksimal 7 hari, tawarkan diskon pelunasan tunai (misal 2/10 n/30)"
        },
        "hints": {
            "concept": "Laba di atas kertas (omzet piutang) berbeda dengan kas riil. Bila piutang belum tertagih sementara tagihan harus dibayar, usaha mengalami krisis arus kas (cash flow crisis / kekurangan likuiditas).",
            "execution": "Krisis Arus Kas (Cash Flow Deficit) akibat tingginya piutang yang belum tertagih."
        }
    }
]
