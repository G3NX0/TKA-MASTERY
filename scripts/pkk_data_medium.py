# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Produk Kreatif dan Kewirausahaan (PKK SMK/MAK)
Dataset: Medium Practice (25 Authentic Questions, pkk-lat-m-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

PKK_MEDIUM_ITEMS = [
    {
        "id": "pkk-lat-m-01",
        "materi": "ANALISIS KEUANGAN & BEP",
        "topic": "Perhitungan Titik Impas Rupiah (BEP Nominal)",
        "stem": "Sebuah usaha sablon digital siswa SMK memproduksi kaos sablon custom dengan biaya tetap (Fixed Cost) operasional sebesar Rp6.000.000 per bulan. Biaya variabel (Variable Cost) per lembar kaos adalah Rp40.000, dan kaos dijual dengan harga (P) Rp100.000 per lembar. Berdasarkan rasio margin kontribusi, nilai penjualan minimal (BEP Rupiah) yang harus dicapai agar usaha tidak mengalami kerugian adalah...",
        "correct": "Rp10.000.000, dihitung dari rasio margin kontribusi 60% (Margin Kontribusi Rp60.000 / Harga Rp100.000), sehingga Rp6.000.000 dibagi 0,6 menghasilkan omzet impas tepat Rp10.000.000.",
        "distractors": [
            "Rp6.000.000, karena nilai impas omzet selalu identik secara mutlak dengan total pengeluaran biaya tetap gedung tanpa memperhitungkan biaya bahan kain.",
            "Rp15.000.000, karena laba kotor harus dikalikan 250% untuk menutupi risiko penyusutan mesin cetak sablon digital di laboratorium sekolah.",
            "Rp4.000.000, karena biaya variabel per lembar kaos menjadi pengurang langsung terhadap nilai seluruh aset lancar di neraca saldo.",
            "Rp24.000.000, karena omzet impas dihitung dengan mengalikan harga jual kaos dengan total biaya tetap bulanan secara langsung."
        ],
        "formula": {
            "title": "FORMULA TITIK IMPAS NOMINAL (BEP RUPIAH)",
            "latex": "\\text{BEP}_{Rp} = \\frac{FC}{1 - \\frac{VC}{P}} = \\frac{FC}{\\text{Contribution Margin Ratio}}",
            "legend": "• $FC = \\text{Rp}6.000.000$<br>• $VC = \\text{Rp}40.000$, $P = \\text{Rp}100.000$<br>• Rasio Margin Kontribusi $= \\frac{100.000 - 40.000}{100.000} = 0{,}60$ (60%)<br>• $\\text{BEP}_{Rp} = \\frac{6.000.000}{0{,}6} = \\text{Rp}10.000.000$ (setara 100 unit kaos)"
        },
        "hints": {
            "concept": "BEP Rupiah dihitung dengan membagi Biaya Tetap (FC) dengan Rasio Margin Kontribusi (1 - VC/P).",
            "execution": "Margin kontribusi = 100rb - 40rb = 60rb (60%). BEP Rp = 6jt / 0,6 = Rp10.000.000."
        }
    },
    {
        "id": "pkk-lat-m-02",
        "materi": "VALUE PROPOSITION DESIGN",
        "topic": "Value Proposition Canvas: Pains vs Pain Relievers",
        "stem": "Dalam merancang Value Proposition Canvas untuk usaha perbaikan sepeda motor keliling, tim wirausaha SMK menemukan keluhan utama pelanggan (Customer Pains): 'Konsumen sangat kesal menunggu antrean bengkel hingga 3 jam dan sering merasa dicurangi mengenai harga onderdil yang tidak transparan'. Solusi yang tepat pada sisi Value Map untuk meredakan keluhan tersebut (Pain Relievers) adalah...",
        "correct": "Menyediakan fitur pemesanan waktu servis presisi via WhatsApp disertai katalog digital daftar harga resmi onderdil dan estimasi biaya sebelum pengerjaan dimulai.",
        "distractors": [
            "Menyediakan ruang tunggu mewah ber-AC dengan televisi kabel di kantor pusat bengkel yang berjarak 20 kilometer dari rumah pelanggan.",
            "Memberikan suvenir gantungan kunci berbahan karet sintetis tanpa memberikan rincian nota pembelian onderdil.",
            "Menaikkan tarif jasa montir sebesar 50% untuk menyeleksi konsumen dari kalangan ekonomi menengah ke atas.",
            "Mengganti seluruh mekanik motor bensin dengan montir spesialis pesawat terbang komersial bermesin jet ganda."
        ],
        "formula": {
            "title": "ARSITEKTUR VALUE PROPOSITION CANVAS (OSTERWALDER)",
            "latex": "\\text{Product-Market Fit} \\iff \\text{Pain Relievers} \\cap \\text{Customer Pains} \\neq \\emptyset \\quad \\& \\quad \\text{Gain Creators} \\cap \\text{Customer Gains} \\neq \\emptyset",
            "legend": "• Customer Pains: Masalah, hambatan, ketakutan, dan frustrasi yang dialami pelanggan<br>• Pain Relievers: Fitur spesifik produk/layanan yang secara langsung mengeliminasi masalah pelanggan tersebut<br>• Fit: Keselarasan presisi antara apa yang ditawarkan dengan apa yang dirasakan konsumen"
        },
        "hints": {
            "concept": "Pain Relievers pada Value Map harus secara spesifik menjawab Customer Pains (antre lama dan ketidaktransparanan harga).",
            "execution": "Pilih opsi yang menawarkan solusi waktu servis terjadwal dan transparansi katalog harga onderdil."
        }
    },
    {
        "id": "pkk-lat-m-03",
        "materi": "MANAJEMEN PERSEDIAAN",
        "topic": "Economic Order Quantity (EOQ) Bahan Baku",
        "stem": "Unit produksi pengelasan SMK membutuhkan 1.200 batang besi hollow per tahun untuk memproduksi pagar minimalis. Biaya pemesanan setiap kali pesan adalah Rp60.000 (ongkos kirim dan administrasi), sedangkan biaya penyimpanan di gudang adalah Rp4.000 per batang per tahun. Berapakah jumlah pemesanan paling ekonomis (Economic Order Quantity / EOQ) yang meminimalkan total biaya persediaan?",
        "correct": "190 batang per pemesanan (dibulatkan dari $\\sqrt{36.000} \\approx 189{,}74$), yang menghasilkan titik keseimbangan optimal antara biaya pesan dan biaya simpan gudang.",
        "distractors": [
            "600 batang per pemesanan, dengan asumsi memesan dua kali setahun untuk menghabiskan seluruh sisa anggaran kas sekaligus.",
            "1.200 batang sekaligus di awal tahun, agar gudang sekolah penuh sesak meskipun risiko karat dan biaya simpan membengkak.",
            "50 batang per pemesanan, agar guru pembimbing sering melakukan perjalanan dinas keluar sekolah untuk mengambil nota kuitansi.",
            "300 batang per pemesanan, dihitung dari total kebutuhan dibagi dengan jumlah bulan dalam satu tahun kalender."
        ],
        "formula": {
            "title": "FORMULA ECONOMIC ORDER QUANTITY (EOQ)",
            "latex": "EOQ = \\sqrt{\\frac{2 \\times D \\times S}{H}} = \\sqrt{\\frac{2 \\times 1.200 \\times 60.000}{4.000}} = \\sqrt{36.000} \\approx 189{,}74 \\text{ unit}",
            "legend": "• $D = \\text{Permintaan tahunan (Demand)} = 1.200$ batang<br>• $S = \\text{Biaya pesan per order (Setup/Order Cost)} = \\text{Rp}60.000$<br>• $H = \\text{Biaya simpan per unit/tahun (Holding Cost)} = \\text{Rp}4.000$"
        },
        "hints": {
            "concept": "Gunakan rumus EOQ = sqrt( (2 * D * S) / H ).",
            "execution": "2 * 1200 * 60.000 / 4000 = 144.000.000 / 4000 = 36.000. Akar dari 36.000 = 189,74 ≈ 190 batang."
        }
    },
    {
        "id": "pkk-lat-m-04",
        "materi": "MANAJEMEN PERSEDIAAN",
        "topic": "Titik Pemesanan Kembali (Reorder Point - ROP)",
        "stem": "Sebuah usaha roti kering siswa tata boga SMK menggunakan rata-rata 15 kg mentega per hari. Waktu tunggu pengiriman dari distributor (Lead Time) adalah 4 hari kerja. Untuk mengantisipasi lonjakan pesanan mendadak atau keterlambatan kurir, tim menetapkan persediaan pengaman (Safety Stock) sebesar 20 kg. Tim produksi harus melakukan pemesanan kembali (Reorder Point / ROP) saat stok mentega di gudang tersisa...",
        "correct": "80 kg, dihitung dari kebutuhan selama waktu tunggu (15 kg/hari x 4 hari = 60 kg) ditambah dengan persediaan pengaman (Safety Stock 20 kg).",
        "distractors": [
            "60 kg, karena persediaan pengaman tidak boleh dihitung ke dalam ambang batas pemesanan operasional harian.",
            "20 kg, yaitu saat stok gudang hanya menyisakan cadangan pengaman darurat persis sebelum habis total.",
            "100 kg, dihitung dengan menjumlahkan seluruh kebutuhan mentega selama satu bulan kalender kerja.",
            "39 kg, hasil perkalian waktu tunggu dengan faktor kelembapan udara ruangan dapur pengolahan roti."
        ],
        "formula": {
            "title": "PERHITUNGAN REORDER POINT (ROP)",
            "latex": "\\text{ROP} = (d \\times L) + \\text{SS}",
            "legend": "• $d = \\text{Penggunaan rata-rata per hari} = 15$ kg<br>• $L = \\text{Waktu tunggu pengiriman (Lead Time)} = 4$ hari<br>• $\\text{SS} = \\text{Persediaan pengaman (Safety Stock)} = 20$ kg<br>• $\\text{ROP} = (15 \\times 4) + 20 = 60 + 20 = 80$ kg"
        },
        "hints": {
            "concept": "Reorder Point (ROP) = (Kebutuhan Harian x Lead Time) + Safety Stock.",
            "execution": "ROP = (15 x 4) + 20 = 60 + 20 = 80 kg."
        }
    },
    {
        "id": "pkk-lat-m-05",
        "materi": "PEMASARAN DIGITAL & METRIK USAHA",
        "topic": "Efisiensi Pemasaran: Rasio LTV terhadap CAC",
        "stem": "Sebuah rintisan software akuntansi berbasis SaaS hasil karya siswa SMK menghabiskan biaya pemasaran digital sebesar Rp15.000.000 dalam sebulan dan berhasil memperoleh 50 pelanggan berbayar baru. Berdasarkan data historis retensi, rata-rata satu pelanggan berlangganan selama 12 bulan dengan kontribusi margin keuntungan bersih Rp100.000 per bulan. Evaluasi kesehatan akuisisi pelanggan (LTV : CAC) bisnis tersebut adalah...",
        "correct": "Sehat dan layak ekspansi, karena CAC sebesar Rp300.000 menghasilkan LTV sebesar Rp1.200.000 sehingga rasio LTV : CAC mencapai 4 : 1 (melampaui ambang batas sehat industri startup yaitu minimal 3 : 1).",
        "distractors": [
            "Sangat berbahaya dan mendekati bangkrut, karena biaya pemasaran Rp15.000.000 langsung mengurangi modal dasar perseroan tanpa sisa kas.",
            "Tidak efisien, karena rasio LTV terhadap CAC bernilai 1 : 4 sehingga perusahaan merugi Rp900.000 pada setiap pelanggan yang didapat.",
            "Netral, karena biaya akuisisi pelanggan tidak memiliki korelasi statistik dengan pendapatan berulang bulanan (MRR).",
            "Ilegal, karena usaha siswa SMK dilarang menggunakan strategi iklan berbayar di platform media sosial digital."
        ],
        "formula": {
            "title": "METRIK AKUISISI PELANGGAN (CAC & LTV)",
            "latex": "\\text{CAC} = \\frac{\\text{Total Marketing Cost}}{\\text{New Customers}} = \\frac{15.000.000}{50} = \\text{Rp}300.000; \\quad \\text{LTV} = 12 \\times 100.000 = \\text{Rp}1.200.000",
            "legend": "• $\\text{Rasio LTV : CAC} = \\frac{1.200.000}{300.000} = 4 : 1$<br>• Benchmark Industri: < 1:1 (Pasti Bangkrut), 1:1 - 2:1 (Kurang Efisien), 3:1 - 5:1 (Sangat Sehat & Optimal), > 5:1 (Terlalu Sedikit Beriklan)"
        },
        "hints": {
            "concept": "CAC = Total Biaya Iklan / Jumlah Pelanggan Baru. LTV = Masa Langganan x Margin per Bulan. Rasio sehat minimal 3:1.",
            "execution": "CAC = 15jt / 50 = 300rb. LTV = 12 x 100rb = 1,2jt. Rasio = 1,2jt / 300rb = 4:1 (Sehat)."
        }
    },
    {
        "id": "pkk-lat-m-06",
        "materi": "HAK KEKAYAAN INTELEKTUAL (HAKI)",
        "topic": "Paten vs Desain Industri vs Hak Cipta",
        "stem": "Siswa SMK Jurusan Teknik Kendaraan Ringan berhasil memodifikasi mekanisme tuas dongkrak hidrolik mobil dengan formula sistem katup baru yang melipatgandakan daya angkat beban hingga 300% melalui prinsip mekanika fluida terbaru. Jenis perlindungan Hak Kekayaan Intelektual (HAKI) yang wajib diajukan ke Ditjen KI untuk melindungi solusi teknis operasional penemuan tersebut adalah...",
        "correct": "Paten (atau Paten Sederhana), karena objek perlindungan merupakan invasi/inovasi di bidang teknologi yang berupa proses, produk mekanis, atau pengembangan sistem teknis baru.",
        "distractors": [
            "Hak Cipta, karena dongkrak hidrolik memiliki kesamaan fungsi estetika dengan lukisan kanvas pemandangan alam.",
            "Desain Industri, karena yang dilindungi semata-mata adalah warna cat oranye pada bodi luar tabung dongkrak.",
            "Merek Dagang, karena penemuan katup tersebut secara otomatis menjadi logo huruf timbul yang ditempel di kaca belakang mobil.",
            "Indikasi Geografis, karena bahan baku besi dongkrak ditambang dari daerah pegunungan kapur Jawa Timur."
        ],
        "formula": {
            "title": "KLASIFIKASI OBJEK PERLINDUNGAN HAKI (UU RI)",
            "latex": "\\text{Paten} = \\text{Invensi Teknologi (Fungsi/Cara Kerja)}; \\quad \\text{Desain Industri} = \\text{Kreasi Estetika/Bentuk 2D/3D}",
            "legend": "• Paten (UU No. 13/2016): Solusi teknis atas masalah spesifik (kebaruan, langkah inventif, dapat diterapkan di industri)<br>• Desain Industri (UU No. 31/2000): Penampilan visual luar (bentuk, konfigurasi, komposisi garis/warna)<br>• Hak Cipta (UU No. 28/2014): Karya cipta seni, sastra, dan ilmu pengetahuan (termasuk program komputer)"
        },
        "hints": {
            "concept": "Inovasi pada cara kerja, sistem mekanis, atau teknologi fungsional (mekanisme katup daya angkat) dilindungi oleh Paten.",
            "execution": "Paten (atau Paten Sederhana) untuk invensi teknologi fungsional."
        }
    },
    {
        "id": "pkk-lat-m-07",
        "materi": "LAPORAN KEUANGAN & ARUS KAS",
        "topic": "Klasifikasi Aktivitas Laporan Arus Kas (Operating vs Investing vs Financing)",
        "stem": "Dalam pembukuan usaha bengkel permesinan CNC SMK, bendahara mencatat tiga transaksi dalam satu minggu: (1) Penerimaan uang tunai dari pelanggan atas jasa bubut baut roda, (2) Pembelian satu unit mesin gerinda duduk baru untuk inventaris bengkel, dan (3) Penarikan pinjaman modal kerja dari koperasi sekolah. Berdasarkan Standar Akuntansi Keuangan, klasifikasi ketiga arus kas tersebut secara berurutan adalah...",
        "correct": "Arus Kas Aktivitas Operasi (Operating), Arus Kas Aktivitas Investasi (Investing), dan Arus Kas Aktivitas Pendanaan (Financing).",
        "distractors": [
            "Arus Kas Aktivitas Investasi, Arus Kas Aktivitas Operasi, dan Arus Kas Aktivitas Sosial Kemanusiaan.",
            "Arus Kas Aktivitas Pendanaan, Arus Kas Aktivitas Penjualan Aset, dan Arus Kas Aktivitas Beban Pajak Daerah.",
            "Arus Kas Beban Pokok Penjualan, Arus Kas Modal Disetor, dan Arus Kas Piutang Tak Tertagih.",
            "Arus Kas Kasir Depan, Arus Kas Kasir Belakang, dan Arus Kas Gudang Logistik Sentral."
        ],
        "formula": {
            "title": "TAKSONOMI ARUS KAS (STATEMENT OF CASH FLOWS)",
            "latex": "\\Delta \\text{Cash} = \\text{Cash Flow Operasi} + \\text{Cash Flow Investasi} + \\text{Cash Flow Pendanaan}",
            "legend": "• Operasi (Operating): Transaksi operasional rutin (penjualan jasa, beli bahan, bayar gaji, listrik)<br>• Investasi (Investing): Pembelian/penjualan aset tetap jangka panjang (mesin, alat, tanah, gedung)<br>• Pendanaan (Financing): Transaksi modal dan utang jangka panjang (pinjaman bank/koperasi, setoran modal pemegang saham)"
        },
        "hints": {
            "concept": "(1) Jasa bubut = operasi harian; (2) Pembelian mesin gerinda = investasi aset tetap; (3) Pinjaman modal koperasi = pendanaan modal usaha.",
            "execution": "Operasi, Investasi, dan Pendanaan."
        }
    },
    {
        "id": "pkk-lat-m-08",
        "materi": "ANALISIS RASIO KEUANGAN",
        "topic": "Rasio Likuiditas: Perhitungan Current Ratio",
        "stem": "Neraca keuangan unit usaha katering siswa SMK pada akhir semester mencatat posisi keuangan sebagai berikut: Kas dan Bank = Rp4.000.000, Piutang Usaha = Rp2.000.000, Persediaan Bahan Makanan = Rp6.000.000, dan Utang Usaha yang segera jatuh tempo dalam 30 hari = Rp6.000.000. Berapakah nilai Rasio Lancar (Current Ratio) usaha tersebut dan apa interpretasinya?",
        "correct": "2,0 (atau 200%), yang berarti usaha dalam kondisi likuiditas sangat aman karena setiap Rp1 utang jangka pendek dijamin oleh Rp2 aset lancar.",
        "distractors": [
            "0,67 (atau 67%), yang berarti usaha menghadapi ancaman kebangkrutan seketika karena persediaan tidak dapat dihitung sebagai aset.",
            "1,0 (atau 100%), yang berarti seluruh kas bank harus segera disita oleh pihak sekolah untuk kas dana bos.",
            "4,0 (atau 400%), dihitung dengan mengabaikan seluruh utang dagang yang belum dibayar kepada pemasok beras.",
            "0,5 (atau 50%), yang menunjukkan bahwa kas bank tidak cukup untuk membayar biaya bahan baku satu semester."
        ],
        "formula": {
            "title": "FORMULA RASIO LANCAR (CURRENT RATIO)",
            "latex": "\\text{Current Ratio} = \\frac{\\text{Current Assets}}{\\text{Current Liabilities}} = \\frac{\\text{Kas} + \\text{Piutang} + \\text{Persediaan}}{\\text{Utang Lancar}}",
            "legend": "• $\\text{Aset Lancar} = 4.000.000 + 2.000.000 + 6.000.000 = \\text{Rp}12.000.000$<br>• $\\text{Utang Lancar} = \\text{Rp}6.000.000$<br>• $\\text{Current Ratio} = \\frac{12.000.000}{6.000.000} = 2{,}0$ (200%)"
        },
        "hints": {
            "concept": "Current Ratio = Total Aset Lancar / Total Utang Lancar.",
            "execution": "Aset Lancar = 4jt + 2jt + 6jt = 12jt. Utang Lancar = 6jt. Current Ratio = 12jt / 6jt = 2,0."
        }
    },
    {
        "id": "pkk-lat-m-09",
        "materi": "PENETAPAN BIAYA PRODUKSI (HPP)",
        "topic": "Metode Full Costing vs Variable Costing",
        "stem": "Dalam menghitung Harga Pokok Produksi (HPP) pembuatan meja belajar kayu lipat, tim wirausaha SMK memasukkan unsur: Biaya Bahan Baku Utama, Biaya Tenaga Kerja Langsung, Biaya Overhead Pabrik Variabel, dan Biaya Overhead Pabrik Tetap (seperti penyusutan mesin gergaji listrik). Pendekatan penentuan harga pokok yang memasukkan seluruh unsur biaya overhead tetap dan variabel ini disebut...",
        "correct": "Metode Biaya Penuh (Full Costing), yaitu metode penentuan HPP yang membebankan seluruh unsur biaya produksi baik yang berperilaku tetap maupun variabel ke dalam harga pokok produk.",
        "distractors": [
            "Metode Biaya Variabel (Variable Costing), yang hanya memasukkan biaya produksi yang berubah sebanding dengan volume output dan mengabaikan overhead tetap.",
            "Metode Biaya Peluang (Opportunity Costing), yang menghitung potensi pendapatan siswa jika mereka bekerja paruh waktu di tempat pencucian mobil.",
            "Metode Biaya Hangus (Sunk Costing), yang hanya memperhitungkan biaya pembelian kayu yang sudah lapuk dan dimakan rayap.",
            "Metode Biaya Marginal Acak, yang menentukan biaya produksi berdasarkan tebakan harga pasaran di lokapasar online."
        ],
        "formula": {
            "title": "PERBANDINGAN STRUKTUR HARGA POKOK PRODUKSI",
            "latex": "\\text{HPP}_{\\text{Full Costing}} = \\text{BBB} + \\text{BTKL} + \\text{BOP Variabel} + \\text{BOP Tetap}",
            "legend": "• Full Costing (Absorption Costing): Wajib untuk pelaporan keuangan eksternal (SAK/Fiskal)<br>• Variable Costing (Direct Costing): BBB + BTKL + BOP Variabel (khusus untuk pengambilan keputusan manajerial internal)<br>• BOP Tetap: Penyusutan gedung bengkel, asuransi mesin, gaji mandor tetap"
        },
        "hints": {
            "concept": "Metode penentuan harga pokok produksi yang memperhitungkan seluruh biaya (variabel + tetap) disebut Full Costing.",
            "execution": "Full Costing (Biaya Penuh)."
        }
    },
    {
        "id": "pkk-lat-m-10",
        "materi": "STRATEGI PENETAPAN HARGA (PRICING)",
        "topic": "Penetration Pricing vs Price Skimming",
        "stem": "Sebuah rintisan usaha minuman teh herbal kemasan botol karya siswa SMK Agribisnis memasuki pasar lokal yang sudah didominasi oleh merek-merek multinasional besar. Untuk menarik perhatian konsumen dengan cepat dan merebut pangsa pasar perdana, tim menetapkan harga jual Rp3.000 per botol (jauh di bawah harga pasar pesaing Rp6.000), dengan rencana menaikkan harga secara bertahap setelah memiliki basis pelanggan loyal. Strategi penetapan harga ini disebut...",
        "correct": "Penetration Pricing (Harga Penetrasi Pasar), yaitu strategi menetapkan harga awal yang relatif rendah untuk menembus pasar secara cepat dan membangun loyalitas volume konsumen.",
        "distractors": [
            "Price Skimming (Penyaringan Harga), yaitu menetapkan harga awal setinggi mungkin untuk memeras surplus konsumen kelas atas sebelum menurunkan harga.",
            "Prestige Pricing (Harga Gengsi), yaitu sengaja menetapkan harga mahal agar produk dipandang sebagai barang mewah oleh kolektor barang antik.",
            "Cost-Plus Pricing Murni, yaitu menambahkan persentase keuntungan kaku tanpa mempedulikan reaksi kompetitor di pasar ritel.",
            "Dynamic Pricing Algoritmik, yaitu mengubah harga botol setiap 5 detik sesuai dengan pergerakan indeks saham gabungan."
        ],
        "formula": {
            "title": "DIKOTOMI STRATEGI HARGA PRODUK BARU",
            "latex": "\\text{Penetrasi: } P_{\\text{awal}} < P_{\\text{pasar}} \\implies \\text{Volume \& Share} \\quad \\text{vs} \\quad \\text{Skimming: } P_{\\text{awal}} \\gg P_{\\text{pasar}} \\implies \\text{Margin Maksimal}",
            "legend": "• Penetration Pricing: Cocok untuk pasar elastis terhadap harga dan persaingan ketat (makanan, minuman, jasa ritel)<br>• Price Skimming: Cocok untuk produk inovasi teknologi tinggi yang tidak memiliki pesaing langsung (gadget unik)"
        },
        "hints": {
            "concept": "Memasang harga murah di awal untuk menerobos pasar dan membangun basis konsumen disebut Penetration Pricing.",
            "execution": "Penetration Pricing (Harga Penetrasi Pasar)."
        }
    },
    {
        "id": "pkk-lat-m-11",
        "materi": "SIKLUS HIDUP PRODUK (PLC)",
        "topic": "Tahap Kematangan (Maturity Stage) dan Strategi Modifikasi",
        "stem": "Penjualan casing smartphone berbahan resin akrilik produksi siswa SMK kriya berada pada kondisi: volume penjualan mencapai puncak tertinggi, tingkat pertumbuhan penjualan mulai mendatar (stagnan), persaingan dari perajin lain sangat ketat, dan margin laba mulai tertekan. Berdasarkan kurva Siklus Hidup Produk (Product Life Cycle), produk tersebut berada pada tahap...",
        "correct": "Tahap Kedewasaan / Kematangan (Maturity Stage), yang menuntut strategi modifikasi fitur produk, diferensiasi desain, atau eksplorasi segmen pasar baru agar tidak jatuh ke tahap penurunan (decline).",
        "distractors": [
            "Tahap Perkenalan (Introduction Stage), di mana konsumen belum mengetahui keberadaan produk dan biaya promosi masih sangat besar.",
            "Tahap Pertumbuhan (Growth Stage), di mana penjualan melonjak drastis secara eksponensial tanpa adanya persaingan yang berarti.",
            "Tahap Penurunan (Decline Stage), di mana penjualan telah anjlok mendekati nol dan produk harus segera ditarik dari peredaran.",
            "Tahap Konsepsi Awal, di mana siswa baru mulai menggambar sketsa manual di atas kertas kalkir."
        ],
        "formula": {
            "title": "4 FASE PRODUCT LIFE CYCLE (PLC)",
            "latex": "\\text{Introduction} \\longrightarrow \\text{Growth} \\longrightarrow \\text{Maturity (Puncak Volume \& Kompetisi)} \\longrightarrow \\text{Decline}",
            "legend": "• Maturity Characteristics: Pertumbuhan melambat, saturasi pasar, perang harga antar kompetitor<br>• Solusi Strategis di Tahap Maturity: Rejuvenasi produk, penambahan varian/fitur, bundling promosi, rebranding"
        },
        "hints": {
            "concept": "Penjualan di puncak, pertumbuhan melambat, dan persaingan sangat ketat merupakan karakteristik tahap Maturity (Kedewasaan/Kematangan).",
            "execution": "Tahap Kedewasaan / Kematangan (Maturity Stage)."
        }
    },
    {
        "id": "pkk-lat-m-12",
        "materi": "SALURAN DISTRIBUSI",
        "topic": "Tingkat Saluran Distribusi (Zero-Level vs One-Level Channel)",
        "stem": "Unit produksi pengolahan hasil pertanian SMK memproduksi selai stroberi organik. Untuk memperluas jangkauan tanpa harus membuka gerai fisik sendiri di setiap kecamatan, tim wirausaha menjual produknya ke jaringan minimarket modern lokal, yang selanjutnya menjual langsung kepada konsumen akhir di kasir toko. Struktur saluran pemasaran yang diterapkan oleh unit usaha ini adalah...",
        "correct": "Saluran Tingkat Satu (One-Level Channel / Indirect Distribution), di mana alur produk mengalir dari Produsen $\\rightarrow$ Pengecer (Retailer) $\\rightarrow$ Konsumen Akhir.",
        "distractors": [
            "Saluran Tingkat Nol (Zero-Level Channel / Direct Marketing), di mana produsen menjual langsung dari dapur ke tangan konsumen tanpa perantara sama sekali.",
            "Saluran Tingkat Dua (Two-Level Channel), di mana barang harus melewati Pedagang Besar (Wholesaler) dan Agen Tunggal Pemegang Merek sebelum sampai ke toko.",
            "Saluran Sirkular Gelap, di mana barang diselundupkan melewati batas perairan internasional tanpa dokumen karantina.",
            "Saluran Multi-Level Marketing (MLM), di mana konsumen diwajibkan merekrut sepuluh anggota keluarga untuk memperoleh potongan harga."
        ],
        "formula": {
            "title": "ARSITEKTUR SALURAN DISTRIBUSI KONTEMPORER",
            "latex": "\\text{Produsen} \\xrightarrow{\\text{Tingkat Satu}} \\text{Pengecer (Retailer)} \\xrightarrow{} \\text{Konsumen Akhir}",
            "legend": "• Zero-Level: Produsen $\\rightarrow$ Konsumen (Direct D2C, Toko Sendiri, Website Resmi)<br>• One-Level: Produsen $\\rightarrow$ Retailer $\\rightarrow$ Konsumen (Minimarket, Toko Ritel)<br>• Two-Level: Produsen $\\rightarrow$ Wholesaler/Distributor $\\rightarrow$ Retailer $\\rightarrow$ Konsumen"
        },
        "hints": {
            "concept": "Produsen menjual ke perantara tunggal (minimarket/pengecer), lalu pengecer menjual ke konsumen = Saluran Tingkat Satu (One-Level Channel).",
            "execution": "Saluran Tingkat Satu (One-Level Channel)."
        }
    },
    {
        "id": "pkk-lat-m-13",
        "materi": "REGULASI PERIZINAN USAHA",
        "topic": "Perizinan Berusaha Berbasis Risiko (OSS-RBA)",
        "stem": "Sesuai PP No. 5 Tahun 2021 tentang Penyelenggaraan Perizinan Berusaha Berbasis Risiko melalui sistem Online Single Submission (OSS-RBA), sebuah unit usaha konveksi pakaian kasual siswa SMK yang tergolong dalam Tingkat Risiko Rendah (Low Risk) cukup memiliki dokumen legalitas operasional utama berupa...",
        "correct": "Nomor Induk Berusaha (NIB), yang berlaku sebagai legalitas identitas pelaku usaha, Tanda Daftar Perusahaan (TDP), Angka Pengenal Impor (API), dan bukti pemenuhan izin edar dasar.",
        "distractors": [
            "Analisis Mengenai Dampak Lingkungan (AMDAL) komprehensif skala reaktor nuklir industri berat.",
            "Surat Keputusan Izin Ekspor Logam Mulia dari Dewan Keamanan Perserikatan Bangsa-Bangsa.",
            "Izin Penggunaan Senjata Api Otomatis dari Markas Besar Kepolisian Daerah Khusus Ibu Kota.",
            "Sertifikat Kelayakan Terbang Pesawat Ruang Angkasa Berawak dari Badan Antariksa Internasional."
        ],
        "formula": {
            "title": "HIRARKI PERIZINAN BERBASIS RISIKO (PP 5/2021 OSS-RBA)",
            "latex": "\\text{Risiko Rendah} \\implies \\text{NIB}; \\quad \\text{Menengah Rendah} \\implies \\text{NIB} + \\text{Sertifikat Standar (Self-declare)}",
            "legend": "• Rendah (Low): Cukup NIB (otomatis berlaku sebagai izin usaha legal tanpa verifikasi lapangan rumit)<br>• Menengah Rendah: NIB + Sertifikat Standar Pernyataan Mandiri<br>• Menengah Tinggi: NIB + Sertifikat Standar Terverifikasi<br>• Tinggi (High): NIB + Izin Resmi (wajib verifikasi teknis/lapangan mendalam)"
        },
        "hints": {
            "concept": "Untuk skala mikro/kecil dengan tingkat risiko rendah dalam OSS RBA, dokumen legalitas operasional tunggal yang wajib dan cukup adalah NIB.",
            "execution": "Nomor Induk Berusaha (NIB)."
        }
    },
    {
        "id": "pkk-lat-m-14",
        "materi": "PENGUJIAN & VALIDASI PRODUK",
        "topic": "Metode Pengujian: Alpha Testing vs Beta Testing",
        "stem": "Sebuah aplikasi kasir berbasis web buatan siswa Rekayasa Perangkat Lunak SMK diuji coba dalam dua tahapan: Tahap I diuji oleh tim internal siswa dan guru pembimbing di lab sekolah untuk melacak bug sintaks dan kegagalan basis data; Tahap II diuji langsung oleh 5 pemilik toko kelontong di sekitar sekolah dalam kondisi transaksi riil selama dua minggu. Istilah pengujian Tahap I dan Tahap II tersebut secara berurutan adalah...",
        "correct": "Alpha Testing (Pengujian Internal di Laboratorium Pengembang) dan Beta Testing (Pengujian Eksternal oleh Pengguna Nyata di Lingkungan Sebenarnya).",
        "distractors": [
            "Beta Testing dan Gamma Testing, karena pengujian perangkat lunak di sekolah tidak pernah memerlukan peran pengembang internal.",
            "Stress Testing dan Penetration Testing, yang bertujuan membobol kata sandi rekening bank milik pemilik toko kelontong.",
            "Unit Testing dan Code Refactoring, karena pemilik toko kelontong bertugas membaca baris kode pemrograman PHP secara manual.",
            "Black Box Testing dan White Box Testing, karena kedua istilah tersebut hanya merujuk pada warna casing komputer jinjing."
        ],
        "formula": {
            "title": "TAHAPAN TESTING VALIDASI PRODUK PERANGKAT LUNAK",
            "latex": "\\text{Pengembangan} \\longrightarrow \\text{Alpha Test (Internal Lab)} \\longrightarrow \\text{Beta Test (Real End-User Field)} \\longrightarrow \\text{Release (GA)}",
            "legend": "• Alpha Test: Dilakukan oleh developer/karyawan internal dalam lingkungan terkontrol (white-box / simulated environment)<br>• Beta Test: Dilakukan oleh kelompok pengguna target (external users) di lingkungan operasional nyata untuk mendapatkan feedback objektif"
        },
        "hints": {
            "concept": "Pengujian internal di lingkungan pengembang = Alpha Test. Pengujian langsung oleh pengguna riil di lapangan = Beta Test.",
            "execution": "Alpha Testing dan Beta Testing."
        }
    },
    {
        "id": "pkk-lat-m-15",
        "materi": "MANAJEMEN MUTU & PRODUKSI",
        "topic": "Budaya Kerja Industri: Kaizen dan Konsep 5S/5R",
        "stem": "Di bengkel manufaktur pemesinan SMK, seorang teknisi menemukan tumpukan perkakas kunci inggris yang bercampur dengan sampah bram besi, lantai licin akibat tumpahan oli mesin, dan perkakas ukur presisi (mikrometer) yang diletakkan sembarangan hingga sering hilang. Langkah awal yang paling fundamental menurut prinsip 5S/5R (Seiri / Ringkas) untuk menata bengkel tersebut adalah...",
        "correct": "Memilah secara tegas antara barang yang masih diperlukan dan barang yang sudah tidak berguna/rusak, kemudian membuang atau menyingkirkan barang yang tidak diperlukan dari area kerja.",
        "distractors": [
            "Mengecat seluruh lantai bengkel dengan warna perak berkilau tanpa menyingkirkan bram besi yang berserakan.",
            "Menempelkan poster peringatan keselamatan kerja berukuran raksasa di atas tumpahan oli licin agar tidak terlihat oleh pengawas.",
            "Menutup bengkel secara permanen dan memindahkan seluruh aktivitas praktik kerja lapangan ke aula olahraga sekolah.",
            "Meminta seluruh siswa membeli mikrometer baru masing-masing dengan menggunakan uang saku pribadi."
        ],
        "formula": {
            "title": "PRINSIP BUDAYA KERJA 5S / 5R (LEAN WORKPLACE)",
            "latex": "\\text{Seiri (Ringkas)} \\rightarrow \\text{Seiton (Rapi)} \\rightarrow \\text{Seiso (Resik)} \\rightarrow \\text{Seiketsu (Rawat)} \\rightarrow \\text{Shitsuke (Rajin)}",
            "legend": "• Seiri (Ringkas/Sort): Pilah barang berguna vs tidak berguna, singkirkan red tag items<br>• Seiton (Rapi/Set in order): Tempatkan barang sesuai tempatnya dengan label jelas<br>• Seiso (Resik/Shine): Bersihkan area kerja dan peralatan dari debu/oli<br>• Seiketsu (Rawat/Standardize): Buat SOP kebersihan dan kerapian berkala<br>• Shitsuke (Rajin/Sustain): Disiplin mematuhi standar kerja setiap hari"
        },
        "hints": {
            "concept": "Langkah pertama 5S/5R adalah Seiri (Ringkas): memilah antara barang yang berguna dan tidak berguna, lalu membuang barang yang tidak terpakai.",
            "execution": "Memilah dan menyingkirkan barang yang tidak diperlukan (Seiri / Ringkas)."
        }
    },
    {
        "id": "pkk-lat-m-16",
        "materi": "EVALUASI INVESTASI USAHA",
        "topic": "Return on Investment (ROI) dan Payback Period",
        "stem": "Unit wirausaha siswa SMK membeli mesin sablon mug otomatis seharga Rp12.000.000. Dari operasional mesin tersebut, diperoleh laba bersih tunai rata-rata sebesar Rp1.500.000 per bulan secara konstan. Berapakah jangka waktu pengembalian modal investasi (Payback Period) dari pembelian mesin tersebut?",
        "correct": "8 bulan, dihitung dari total nilai investasi awal sebesar Rp12.000.000 dibagi dengan arus kas laba bersih bulanan sebesar Rp1.500.000.",
        "distractors": [
            "12 bulan, karena periode pengembalian modal bisnis diatur secara resmi harus selalu genap satu tahun pajak.",
            "18 bulan, karena nilai mesin akan terdepresiasi sebesar 50% setiap kali dialiri arus listrik bolak-balik.",
            "4 bulan, dengan asumsi separuh laba bersih berasal dari sumbangan sukarela orang tua murid.",
            "24 bulan, dihitung dengan menjumlahkan seluruh bunga bank yang diasumsikan pada suku bunga majemuk darurat."
        ],
        "formula": {
            "title": "PERHITUNGAN PAYBACK PERIOD SEDERHANA",
            "latex": "\\text{Payback Period} = \\frac{\\text{Initial Investment}}{\\text{Annual/Monthly Cash Inflow}} = \\frac{\\text{Rp}12.000.000}{\\text{Rp}1.500.000/\\text{bulan}} = 8 \\text{ bulan}",
            "legend": "• Investasi Awal: Rp12.000.000<br>• Arus Kas Masuk Bersih: Rp1.500.000 per bulan<br>• Hasil: Modal kembali penuh pada bulan ke-8 pemakaian alat"
        },
        "hints": {
            "concept": "Payback Period = Nilai Investasi Awal / Arus Kas Bersih per Periode.",
            "execution": "12.000.000 / 1.500.000 = 8 bulan."
        }
    },
    {
        "id": "pkk-lat-m-17",
        "materi": "MODEL BISNIS & STRATEGI PENJUALAN",
        "topic": "Perbedaan Pemasaran B2B vs B2C",
        "stem": "Sebuah unit produksi siswa SMK Jurusan Teknik Pengelasan membuat dua jenis penawaran: (1) Menjual pagar tralis minimalis langsung kepada pemilik rumah perorangan, dan (2) Mengikuti tender pengadaan 500 unit rangka besi troli barang untuk pabrik perakitan otomotif. Karakteristik utama dari transaksi nomor (2) sebagai model B2B (Business-to-Business) dibandingkan B2C adalah...",
        "correct": "Keputusan pembelian melibatkan banyak pemangku kepentingan (buying center), proses evaluasi rasional berbasis spesifikasi teknis dan legalitas faktur, serta volume transaksi yang besar dengan kontrak jangka panjang.",
        "distractors": [
            "Keputusan pembelian bersifat sangat emosional dan impulsif dipicu oleh warna kemasan kardus yang mencolok.",
            "Pembayaran selalu dilakukan secara tunai di kasir minimarket tanpa adanya bukti faktur pajak resmi.",
            "Siklus transaksi berlangsung sangat instan dalam hitungan detik layaknya membeli makanan ringan di pinggir jalan.",
            "Harga jual produk tidak boleh dinegosiasikan dan wajib mencantumkan label diskon coret sebesar 90%."
        ],
        "formula": {
            "title": "PERBANDINGAN SEGMENTASI B2B VS B2C",
            "latex": "\\text{B2B: } \\text{Rational} \\times \\text{Multi-stakeholder} \\times \\text{High Value} \\quad \\text{vs} \\quad \\text{B2C: } \\text{Emotional} \\times \\text{Individual} \\times \\text{High Volume}",
            "legend": "• B2B (Business-to-Business): Motivasi profit/efisiensi operasional, spesifikasi teknis ketat, SLA/garansi pabrik<br>• B2C (Business-to-Consumer): Motivasi pemenuhan kebutuhan personal, pengaruh tren/gaya hidup, proses beli cepat"
        },
        "hints": {
            "concept": "Model B2B bercirikan keputusan rasional multi-pihak, evaluasi spesifikasi ketat, volume besar, dan kontrak formal jangka panjang.",
            "execution": "Pilih opsi yang menjelaskan keputusan rasional berbasis spesifikasi teknis dan legalitas formal."
        }
    },
    {
        "id": "pkk-lat-m-18",
        "materi": "LAPORAN LABA RUGI (INCOME STATEMENT)",
        "topic": "Laba Kotor vs Laba Operasional vs Laba Bersih",
        "stem": "Dalam Laporan Laba Rugi usaha perakitan drone pertanian siswa SMK tercatat: Pendapatan Penjualan = Rp50.000.000, Harga Pokok Penjualan (HPP) = Rp30.000.000, Beban Operasional Penjualan & Administrasi = Rp8.000.000, dan Beban Pajak Penghasilan (PPh) Final UMKM = Rp250.000. Berapakah nilai Laba Operasional (Operating Profit / EBIT) dari usaha tersebut?",
        "correct": "Rp12.000.000, diperoleh dari Laba Kotor (Penjualan Rp50.000.000 dikurangi HPP Rp30.000.000 = Rp20.000.000), kemudian dikurangi Beban Operasional sebesar Rp8.000.000.",
        "distractors": [
            "Rp20.000.000, karena nilai tersebut merupakan Laba Kotor yang belum dipotong oleh beban gaji dan sewa bengkel.",
            "Rp11.750.000, karena nilai tersebut merupakan Laba Bersih Setelah Pajak (EAT) yang telah memperhitungkan PPh Final.",
            "Rp50.000.000, karena omzet bruto penjualan langsung diakui sebagai keuntungan bersih operasional di rekening bank.",
            "Rp8.000.000, karena beban penjualan otomatis menjadi batas maksimal keuntungan yang boleh diambil oleh unit siswa."
        ],
        "formula": {
            "title": "STRUKTUR TINGKATAN LABA DALAM INCOME STATEMENT",
            "latex": "\\begin{aligned} \\text{Laba Kotor} &= \\text{Penjualan} - \\text{HPP} = 50.000.000 - 30.000.000 = \\text{Rp}20.000.000 \\\\ \\text{Laba Operasional (EBIT)} &= \\text{Laba Kotor} - \\text{Beban Operasional} = 20.000.000 - 8.000.000 = \\text{Rp}12.000.000 \\\\ \\text{Laba Bersih} &= \\text{Laba Operasi} - \\text{Pajak} = 12.000.000 - 250.000 = \\text{Rp}11.750.000 \\end{aligned}",
            "legend": "• Gross Profit: Keuntungan murni dari selisih jual dengan biaya produksi fisik barang<br>• Operating Profit (EBIT): Keuntungan murni dari aktivitas bisnis inti setelah membiayai operasional kantor/penjualan<br>• Net Profit: Sisa laba final setelah bunga pinjaman dan kewajiban pajak negara"
        },
        "hints": {
            "concept": "Laba Operasional = Laba Kotor - Beban Operasional. Laba Kotor = Penjualan - HPP.",
            "execution": "Laba Kotor = 50jt - 30jt = 20jt. Laba Operasi = 20jt - 8jt = Rp12.000.000."
        }
    },
    {
        "id": "pkk-lat-m-19",
        "materi": "PEMASARAN DIGITAL (DIGITAL MARKETING)",
        "topic": "Funnel AIDA dan Perhitungan Conversion Rate (CR)",
        "stem": "Sebuah kampanye iklan digital di media sosial untuk mempromosikan produk lampu hias ukir pipa PVC buatan siswa SMK menghasilkan 10.000 impresi tayangan iklan. Dari impresi tersebut, sebanyak 500 pengguna mengeklik tautan menuju landing page (Click-Through), dan 25 orang di antaranya melakukan transfer pembayaran pembelian produk di formulir kasir. Berapakah nilai Tingkat Konversi Penjualan (Sales Conversion Rate) dari pengunjung landing page menjadi pembeli?",
        "correct": "5,0%, dihitung dari jumlah pembeli nyata (25 orang) dibagi dengan total pengunjung landing page (500 orang) dikalikan 100%.",
        "distractors": [
            "0,25%, dihitung secara keliru dari jumlah pembeli dibagi dengan total impresi tayangan iklan awal.",
            "20,0%, dihitung dari rasio jumlah klik tautan terhadap harga jual satu unit lampu hias pipa.",
            "50,0%, karena setiap dua orang yang membaca iklan diyakini pasti akan membeli satu lusin lampu hias.",
            "2,5%, dihitung dari selisih antara klik tautan dengan jumlah pengikut akun media sosial sekolah."
        ],
        "formula": {
            "title": "FORMULA TINGKAT KONVERSI (CONVERSION RATE)",
            "latex": "\\text{Conversion Rate (Landing Page)} = \\frac{\\text{Total Conversions / Buyers}}{\\text{Total Visitors / Clicks}} \\times 100\\% = \\frac{25}{500} \\times 100\\% = 5{,}0\\%",
            "legend": "• Funnel: Impresi (10.000) $\\xrightarrow{\\text{CTR 5\\%}}$ Klik Landing Page (500) $\\xrightarrow{\\text{CR 5\\%}}$ Pembeli (25)<br>• Standar Industri E-Commerce: Rata-rata conversion rate website berkisar 1% - 3%. Capaian 5% tergolong sangat efektif"
        },
        "hints": {
            "concept": "Conversion Rate dihitung dari (Pembeli / Pengunjung Website) x 100%.",
            "execution": "25 / 500 * 100% = 5,0%."
        }
    },
    {
        "id": "pkk-lat-m-20",
        "materi": "MANAJEMEN KEUANGAN & PIUTANG",
        "topic": "Manajemen Umur Piutang (Aging Schedule)",
        "stem": "Dalam rekapitulasi daftar piutang dagang usaha kriya kulit siswa SMK sebesar Rp10.000.000, ditemukan bahwa Rp2.000.000 di antaranya telah menunggak melebihi 90 hari melewati batas jatuh tempo (overdue). Tindakan manajerial pengendalian kredit yang paling bijak dan terstruktur untuk menanggulangi situasi tersebut adalah...",
        "correct": "Menghentikan fasilitas penjualan kredit baru kepada pelanggan yang menunggak tersebut, membentuk cadangan kerugian piutang tak tertagih, dan mengirimkan surat penagihan berjenjang.",
        "distractors": [
            "Menghapus seluruh piutang secara diam-diam dari catatan buku kas tanpa memberitahu guru pembimbing usaha.",
            "Menambah plafon kredit menjadi Rp20.000.000 kepada debitur macet tersebut agar mereka terdorong membeli lebih banyak barang.",
            "Menyita sertifikat rumah milik orang tua siswa yang bertugas mencatat buku penjualan harian.",
            "Melaporkan penunggak utang langsung ke pengadilan arbitrase internasional di Den Haag Belanda."
        ],
        "formula": {
            "title": "PRINSIP AGING OF ACCOUNTS RECEIVABLE",
            "latex": "\\text{Penyisihan Piutang Tak Tertagih} = \\sum (\\text{Saldo Piutang}_{i} \\times \\% \\text{Estimasi Gagal Bayar}_{i})",
            "legend": "• Klasifikasi: Belum Jatuh Tempo (1-30 hari: risiko rendah) $\\rightarrow$ Lewat 31-60 hari $\\rightarrow$ Lewat 61-90 hari $\\rightarrow$ Lewat >90 hari (risiko macet tinggi)<br>• Tindakan Mitigasi: Stop kredit baru, restrukturisasi jadwal cicilan, bentuk allowance for doubtful accounts"
        },
        "hints": {
            "concept": "Piutang menunggak >90 hari berisiko macet tinggi. Kebijakan pengendalian: stop kredit tambahan, cadangkan kerugian piutang, dan lakukan penagihan bertahap.",
            "execution": "Stop kredit baru, cadangkan piutang tak tertagih, dan kirim surat peringatan/penagihan."
        }
    },
    {
        "id": "pkk-lat-m-21",
        "materi": "HAK KEKAYAAN INTELEKTUAL & HUKUM",
        "topic": "Perjanjian Kerahasiaan (Non-Disclosure Agreement - NDA)",
        "stem": "Sebelum mempresentasikan prototipe inovasi alat sensor hemat pakan ikan otomatis kepada calon investor dan mitra bengkel fabrikasi, tim rintisan siswa SMK mewajibkan seluruh pihak menandatangani dokumen Non-Disclosure Agreement (NDA). Fungsi esensial dari penandatanganan perjanjian NDA tersebut adalah...",
        "correct": "Melindungi kerahasiaan informasi teknis, rahasia dagang, dan skema bisnis agar tidak dibocorkan, ditiru, atau dimanfaatkan oleh pihak mitra tanpa izin sah tertulis.",
        "distractors": [
            "Memaksa investor menyerahkan seluruh kepemilikan saham perusahaannya kepada kas koperasi sekolah secara cuma-cuma.",
            "Memberikan hak istimewa kepada mitra bengkel untuk menjual alat tersebut secara bebas tanpa membayar royalti.",
            "Menjamin bahwa siswa pembuat alat akan otomatis lulus ujian sekolah tanpa perlu mengikuti asesmen akhir.",
            "Mengganti akta kelahiran seluruh anggota tim rintisan menjadi warga negara asing pemegang paspor diplomatik."
        ],
        "formula": {
            "title": "PRINSIP PROTEKSI INFORMASI RAHASIA BISNIS (NDA)",
            "latex": "\\text{Klausul NDA} \\implies \\text{Definisi Rahasia} + \\text{Kewajiban Menjaga} + \\text{Durasi Kerahasiaan} + \\text{Ganti Rugi Pelanggaran}",
            "legend": "• NDA (Non-Disclosure Agreement): Kontrak hukum mengikat pencegah kebocoran rahasia industri<br>• Urgensi sebelum Paten: Mencegah penemuan kehilangan status 'kebaruan' (novelty) akibat publikasi prematur sebelum pendaftaran resmi"
        },
        "hints": {
            "concept": "NDA (Non-Disclosure Agreement) adalah perjanjian hukum untuk mengunci dan menjaga kerahasiaan informasi/rahasia dagang dari pembocoran sepihak.",
            "execution": "Melindungi kerahasiaan informasi teknis dan rahasia bisnis agar tidak ditiru tanpa izin."
        }
    },
    {
        "id": "pkk-lat-m-22",
        "materi": "MANAJEMEN OPERASIONAL & LEAN",
        "topic": "7 Pemborosan Industri (7 Wastes / Muda)",
        "stem": "Di bengkel perakitan instalasi listrik SMK, siswa meletakkan rak komponen saklar dan kabel sejauh 40 meter dari meja kerja utama, sehingga setiap kali merakit satu panel, siswa harus berjalan bolak-balik sebanyak 15 kali. Dalam filosofi Lean Manufacturing (Toyota Production System), aktivitas yang tidak memberikan nilai tambah (Non-Value Added) tersebut diklasifikasikan sebagai pemborosan...",
        "correct": "Waste of Motion (Pemborosan Gerakan), yaitu gerakan fisik pekerja yang tidak ergonomis atau tidak perlu karena tata letak (layout) area kerja yang buruk.",
        "distractors": [
            "Waste of Overproduction (Pemborosan Produksi Berlebih), karena siswa merakit terlalu banyak panel listrik melebihi jumlah pesanan pelanggan.",
            "Waste of Defect (Pemborosan Cacat Produk), karena saklar listrik meledak akibat korsleting tegangan tinggi.",
            "Waste of Overprocessing (Pemborosan Proses Berlebih), karena permukaan panel dipoles menggunakan serbuk intan berlian.",
            "Waste of Waiting (Pemborosan Menunggu), karena seluruh pasokan listrik PLN di kota tersebut padam selama seminggu."
        ],
        "formula": {
            "title": "7 PEMBOROSAN MANUFAKTUR (TIMWOOD)",
            "latex": "\\text{Muda} = \\text{Transport} + \\text{Inventory} + \\text{Motion} + \\text{Waiting} + \\text{Overproduction} + \\text{Overprocessing} + \\text{Defects}",
            "legend": "• Motion: Gerakan tubuh operator yang sia-sia (membungkuk, mencari alat, berjalan jauh akibat layout buruk)<br>• Transportation: Pemindahan bahan/produk antar lokasi yang tidak perlu<br>• Solusi Motion: Terapkan prinsip ekonomi gerakan (Motion Economy) dan dekatkan wadah komponen ke jangkauan tangan"
        },
        "hints": {
            "concept": "Gerakan fisik pekerja yang bolak-balik karena layout bengkel yang tidak teratur adalah contoh nyata Waste of Motion (Pemborosan Gerakan).",
            "execution": "Waste of Motion (Pemborosan Gerakan)."
        }
    },
    {
        "id": "pkk-lat-m-23",
        "materi": "STANDARISASI & MUTU PRODUK",
        "topic": "Standar Nasional Indonesia (SNI Wajib vs Sukarela)",
        "stem": "Unit produksi pengelasan helm sepeda motor siswa SMK berniat memasarkan produk pelindung kepala ke jaringan ritel nasional. Pemerintah Indonesia melalui Kementerian Perindustrian menetapkan bahwa produk helm pengendara kendaraan bermotor wajib memiliki tanda SNI (Standar Nasional Indonesia). Konsekuensi hukum dan operasional dari status 'SNI Wajib' tersebut adalah...",
        "correct": "Produk helm dilarang keras diperjualbelikan atau diedarkan di wilayah Republik Indonesia jika belum lulus uji laboratorium terakreditasi dan belum memiliki Sertifikat Produk Penggunaan Tanda SNI (SPPT SNI).",
        "distractors": [
            "Pemberian tanda SNI hanya bersifat anjuran sukarela pemanis stiker tanpa ada konsekuensi penarikan barang dari pasaran.",
            "Helm yang tidak ber-SNI tetap boleh dijual bebas asalkan diberi tulisan 'Hanya untuk dipakai di jalan desa'.",
            "Pabrik helm otomatis dibebaskan dari kewajiban membayar pajak penghasilan selama sepuluh tahun masa berlakunya sertifikat.",
            "Siswa SMK yang memproduksi helm secara otomatis diangkat menjadi pegawai negeri sipil di Badan Standardisasi Nasional."
        ],
        "formula": {
            "title": "REGULASI STANDARISASI PRODUK (BSN & KEMENPERIN)",
            "latex": "\\text{SNI Wajib} \\implies \\text{Uji Lab Terakreditasi} + \\text{Audit Audit Sistem Mutu (ISO 9001)} \\longrightarrow \\text{SPPT SNI}",
            "legend": "• SNI Wajib diberlakukan untuk produk yang menyangkut keselamatan, keamanan, dan kesehatan publik (K3L)<br>• Pelanggaran SNI Wajib: Sanksi pidana kurungan, denda miliaran rupiah, dan penyitaan produk dari etalase pasar (UU No. 20/2014)"
        },
        "hints": {
            "concept": "SNI Wajib berlaku mutlak demi keselamatan konsumen; produk tanpa sertifikat SNI dilarang beredar dan dikenai sanksi penarikan.",
            "execution": "Dilarang diperjualbelikan di wilayah RI tanpa SPPT SNI."
        }
    },
    {
        "id": "pkk-lat-m-24",
        "materi": "PEMASARAN DIGITAL (DIGITAL MARKETING)",
        "topic": "Return on Ad Spend (ROAS) Iklan Online",
        "stem": "Untuk mempromosikan produk sepatu kulit buatan siswa SMK di platform iklan media sosial, tim wirausaha menggelontorkan anggaran iklan sebesar Rp2.000.000. Dari kampanye tersebut, tercipta omzet penjualan produk secara langsung sebesar Rp10.000.000. Berapakah nilai Return on Ad Spend (ROAS) dari kampanye periklanan tersebut dan bagaimana efektivitasnya?",
        "correct": "5,0x (atau 500%), yang berarti setiap Rp1 uang yang dibelanjakan untuk iklan berhasil mendatangkan omzet penjualan kotor sebesar Rp5.",
        "distractors": [
            "0,2x (atau 20%), yang menunjukkan bahwa usaha mengalami kerugian iklan karena biaya promosi lebih mahal daripada harga sepasang sepatu.",
            "2,0x (atau 200%), dihitung dengan mengurangi omzet penjualan dengan biaya pokok bahan baku kulit samak.",
            "8,0x (atau 800%), dihitung dari selisih antara pendapatan kotor dengan modal kerja awal yang disetor guru pembimbing.",
            "12,0x (atau 1.200%), karena seluruh penonton video iklan diasumsikan akan menjadi pelanggan seumur hidup."
        ],
        "formula": {
            "title": "FORMULA RETURN ON AD SPEND (ROAS)",
            "latex": "\\text{ROAS} = \\frac{\\text{Revenue Generated from Ads}}{\\text{Total Ad Spend}} = \\frac{\\text{Rp}10.000.000}{\\text{Rp}2.000.000} = 5{,}0\\text{x}",
            "legend": "• Formula: Pendapatan Iklan / Biaya Iklan<br>• Interpretasi: 5,0x artinya menghasilkan 5 kali lipat dari biaya iklan yang dikeluarkan<br>• Efektivitas: Sangat baik jika margin kotor produk di atas 20% (karena Break-Even ROAS = 1 / Gross Margin)"
        },
        "hints": {
            "concept": "ROAS = Pendapatan dari Iklan / Biaya Iklan.",
            "execution": "10.000.000 / 2.000.000 = 5,0x (atau 500%)."
        }
    },
    {
        "id": "pkk-lat-m-25",
        "materi": "MANAJEMEN OPERASIONAL & KAPASITAS",
        "topic": "Kapasitas Desain vs Kapasitas Efektif vs Utilisasi",
        "stem": "Mesin jahit otomatis di pabrik garmen siswa SMK dirancang oleh pabrik pembuatnya untuk mampu menjahit maksimal 1.000 kemeja per minggu dalam kondisi ideal tanpa henti (Kapasitas Desain). Namun dengan memperhitungkan waktu perawatan mesin terjadwal, istirahat operator, dan pergantian benang, manajemen menetapkan target realistis sebesar 800 kemeja per minggu (Kapasitas Efektif). Jika dalam praktiknya mesin menghasilkan 720 kemeja dalam seminggu, berapakah Tingkat Utilisasi (Utilization Rate) dari mesin tersebut?",
        "correct": "72%, dihitung dari output aktual (720 unit) dibagi dengan kapasitas desain maksimum mesin (1.000 unit) dikalikan 100%.",
        "distractors": [
            "90%, karena angka tersebut merupakan Tingkat Efisiensi (Efficiency Rate) yang dihitung dari output aktual dibagi kapasitas efektif.",
            "80%, karena kapasitas efektif otomatis menjadi batas mati utilisasi seluruh mesin pabrik garmen tekstil.",
            "50%, dihitung dari selisih antara kapasitas desain dengan jumlah kemeja yang ditolak oleh bagian quality control.",
            "100%, dengan asumsi seluruh mesin jahit beroperasi secara otomatis tanpa bantuan tenaga manusia sama sekali."
        ],
        "formula": {
            "title": "FORMULA PENGUKURAN KINERJA KAPASITAS OPERASIONAL",
            "latex": "\\text{Utilisasi} = \\frac{\\text{Output Aktual}}{\\text{Kapasitas Desain}} \\times 100\\% = \\frac{720}{1.000} \\times 100\\% = 72\\%",
            "legend": "• Utilisasi (Utilization): Output Aktual / Kapasitas Desain = 720 / 1.000 = 72%<br>• Efisiensi (Efficiency): Output Aktual / Kapasitas Efektif = 720 / 800 = 90%<br>• Analisis: Efisiensi tinggi (90%) menunjukkan pengelolaan kapasitas efektif sudah baik, tetapi masih ada gap 28% dari kapasitas teoretis mesin"
        },
        "hints": {
            "concept": "Tingkat Utilisasi dihitung dari Output Aktual dibagi Kapasitas Desain. (Catatan: Output Aktual dibagi Kapasitas Efektif disebut Tingkat Efisiensi).",
            "execution": "Utilisasi = 720 / 1000 * 100% = 72%."
        }
    }
]
