# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Ekonomi (SMA/MA)
Dataset: Latihan Tingkat Easy (25 Authentic Questions, eko-lat-e-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

EKONOMI_EASY_ITEMS = [
    {
        "id": "eko-lat-e-01",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Konsep Biaya Peluang (Opportunity Cost)",
        "stem": "Seorang lulusan SMA berprestasi memiliki tiga pilihan setelah lulus: (1) Bekerja sebagai staf administrasi dengan gaji Rp 3.500.000,- per bulan; (2) Menjadi pramuniaga toko dengan gaji Rp 3.200.000,- per bulan; atau (3) Melanjutkan kuliah sarjana dengan biaya pendidikan Rp 1.500.000,- per bulan. Jika ia memutuskan untuk melanjutkan kuliah sarjana, besar biaya peluang (opportunity cost) yang dikorbankannya per bulan adalah...",
        "correct": "Rp 3.500.000,- per bulan, yaitu nilai alternatif terbaik tertinggi yang dikorbankan (gaji sebagai staf administrasi).",
        "distractors": [
            "Rp 6.700.000,- per bulan, hasil penjumlahan seluruh alternatif gaji pekerjaan yang tidak dipilih.",
            "Rp 1.500.000,- per bulan, yaitu biaya eksplisit yang dikeluarkan secara langsung untuk membayar kuliah.",
            "Rp 5.000.000,- per bulan, hasil penambahan biaya kuliah dengan gaji staf administrasi.",
            "Rp 3.200.000,- per bulan, yaitu alternatif pekerjaan dengan nilai nominal gaji terendah."
        ],
        "formula": {
            "title": "KONSEP BIAYA PELUANG (OPPORTUNITY COST)",
            "latex": "\\text{Biaya Peluang} = \\max\\big(\\text{Nilai Alternatif Terbaik yang Dikorbankan}\\big)",
            "legend": "• Biaya Peluang BUKAN penjumlahan seluruh alternatif, melainkan SATU alternatif terbaik yang ditinggalkan<br>• Biaya Implisit: Pendapatan yang hilang karena memilih kuliah (Rp 3.500.000,-)<br>• Biaya Eksplisit: Uang tunai yang dibayarkan untuk SPP kuliah (Rp 1.500.000,-)"
        },
        "hints": {
            "concept": "Biaya peluang adalah nilai kesempatan terbaik yang hilang/dikorbankan karena mengambil suatu keputusan.",
            "execution": "Pilih: Rp 3.500.000,- per bulan (alternatif terbaik yang dikorbankan)."
        }
    },
    {
        "id": "eko-lat-e-02",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Hukum Permintaan dan Asumsi Ceteris Paribus",
        "stem": "Hukum permintaan menyatakan bahwa jika harga suatu barang mengalami kenaikan, jumlah barang yang diminta oleh konsumen akan mengalami penurunan, dan sebaliknya, dengan asumsi _ceteris paribus_. Makna paling tepat dari istilah asumsi _ceteris paribus_ dalam hukum ekonomi tersebut adalah...",
        "correct": "Faktor-faktor lain di luar harga barang itu sendiri (seperti pendapatan konsumen, selera, harga barang lain, dan ekspektasi masa depan) dianggap konstan atau tidak berubah.",
        "distractors": [
            "Seluruh produsen di pasar sepakat untuk memproduksi barang dalam jumlah kuantitas yang sama besar.",
            "Pemerintah menetapkan batas harga minimum dan harga maksimum secara serentak di pasar komoditas.",
            "Permintaan konsumen bersifat inelastis sempurna sehingga kuantitas tidak terpengaruh oleh harga.",
            "Tingkat inflasi dan nilai tukar valuta asing berada pada titik ekuilibrium nol secara permanen."
        ],
        "formula": {
            "title": "HUKUM PERMINTAAN & ASUMSI CETERIS PARIBUS",
            "latex": "P \\uparrow \\implies Q_d \\downarrow \\quad \\text{dan} \\quad P \\downarrow \\implies Q_d \\uparrow, \\quad \\text{Asumsi: } \\text{Ceteris Paribus}",
            "legend": "• $P$: Harga barang itu sendiri (Price)<br>• $Q_d$: Kuantitas barang yang diminta (Quantity Demanded)<br>• Ceteris Paribus: Variabel lain ($Y$, Selera, $P_{\\text{substitusi}}$, Populasi) bernilai tetap"
        },
        "hints": {
            "concept": "Ceteris paribus artinya \"faktor-faktor lain dianggap tetap/konstan\".",
            "execution": "Pilih: Faktor-faktor lain di luar harga barang itu sendiri dianggap konstan atau tidak berubah."
        }
    },
    {
        "id": "eko-lat-e-03",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Perbedaan Produk Domestik Bruto (PDB) vs Produk Nasional Bruto (PNB)",
        "stem": "Dalam perhitungan pendapatan nasional, Produk Domestik Bruto (PDB / GDP) dan Produk Nasional Bruto (PNB / GNP) mengukur kinerja perekonomian dari sudut pandang yang berbeda. Hubungan matematis yang tepat antara PDB dan PNB adalah...",
        "correct": "$\\text{PNB} = \\text{PDB} + \\text{Pendapatan Neto Faktor Luar Negeri (FPNLN)}$, di mana FPNLN adalah selisih pendapatan warga negara di luar negeri dikurangi pendapatan warga negara asing di dalam negeri.",
        "distractors": [
            "$\\text{PNB} = \\text{PDB} - \\text{Pajak Tidak Langsung} + \\text{Subsidi Pemerintah}$, tanpa memperhitungkan faktor warga negara.",
            "$\\text{PNB} = \\text{PDB} \\times \\text{Indeks Harga Konsumen (IHK)}$, untuk mengeliminasi dampak inflasi tahunan.",
            "$\\text{PNB} = \\text{PDB} + \\text{Penyusutan Barang Modal (Depresiasi)}$, untuk menghitung produk neto.",
            "$\\text{PNB} = \\text{PDB} / \\text{Jumlah Penduduk Total}$, yang mencerminkan pendapatan per kapita riil."
        ],
        "formula": {
            "title": "RELASI AGREGAT PENDAPATAN NASIONAL",
            "latex": "\\text{PNB} = \\text{PDB} + \\text{FPNLN}, \\quad \\text{FPNLN} = \\text{Pendapatan WNI di Luar Negeri} - \\text{Pendapatan WNA di Indonesia}",
            "legend": "• PDB (GDP): Berbasis teritorial/wilayah geografi domestik suatu negara<br>• PNB (GNP): Berbasis kewarganegaraan (nasionalitas) faktor produksi<br>• Negara Berkembang umumnya memiliki PDB > PNB (FPNLN bernilai negatif)"
        },
        "hints": {
            "concept": "PNB = PDB + Pendapatan Neto Faktor Produksi Luar Negeri (FPNLN).",
            "execution": "Pilih: PNB = PDB + Pendapatan Neto Faktor Luar Negeri (FPNLN)."
        }
    },
    {
        "id": "eko-lat-e-04",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Instrumen Operasi Pasar Terbuka (Open Market Operations)",
        "stem": "Ketika tingkat inflasi di dalam negeri mengalami kenaikan yang tidak terkendali, Bank Indonesia selaku bank sentral dapat menerapkan kebijakan moneter kontraktif (tight money policy). Langkah operasional yang dilakukan Bank Sentral melalui instrumen Operasi Pasar Terbuka (OPT) adalah...",
        "correct": "Menjual Surat Berharga Negara (SBN) atau Sertifikat Bank Indonesia (SBI) ke pasar uang perbankan untuk menyerap kelebihan likuiditas dan mengurangi jumlah uang yang beredar di masyarakat.",
        "distractors": [
            "Membeli obligasi pemerintah dari masyarakat umum secara besar-besaran untuk menyuntikkan uang tunai ke perbankan.",
            "Menurunkan suku bunga acuan BI-Rate agar perbankan lebih mudah menyalurkan kredit pinjaman konsumsi.",
            "Menurunkan rasio Giro Wajib Minimum (GWM) perbankan komersial agar kapasitas cadangan dana bank meningkat.",
            "Menghapus pungutan pajak penghasilan karyawan untuk meningkatkan daya beli konsumsi rumah tangga."
        ],
        "formula": {
            "title": "TRANSMISI INSTRUMEN OPERASI PASAR TERBUKA (OPT)",
            "latex": "\\text{Inflasi Tinggi} \\implies \\text{Bank Sentral JUAL Surat Berharga (SBN/SBI)} \\to \\text{Uang Masuk ke BI} \\to \\text{JUB} \\downarrow \\to \\text{Inflasi Terkendali}",
            "legend": "• Kebijakan Kontraktif (Meredam Inflasi): Jual SBN, Naikkan BI-Rate, Naikkan GWM, Perketat kredit<br>• Kebijakan Ekspansif (Mengatasi Resesi): Beli SBN, Turunkan BI-Rate, Turunkan GWM, Longgarkan kredit"
        },
        "hints": {
            "concept": "Mengatasi inflasi butuh mengurangi uang beredar. BI menjual SBN/SBI agar uang ditarik dari perbankan ke Bank Indonesia.",
            "execution": "Pilih: Menjual Surat Berharga Negara (SBN) atau SBI ke pasar uang."
        }
    },
    {
        "id": "eko-lat-e-05",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Persamaan Dasar Akuntansi dan Keseimbangan Neraca",
        "stem": "Dalam sistem pembukuan berpasangan (double-entry bookkeeping), persamaan dasar akuntansi menjadi fondasi seluruh pencatatan transaksi keuangan perusahaan. Rumusan persamaan dasar akuntansi yang benar adalah...",
        "correct": "$\\text{Aset (Harta)} = \\text{Liabilitas (Utang)} + \\text{Ekuitas (Modal)}$, yang mencerminkan bahwa seluruh kekayaan perusahaan didanai oleh klaim kreditur dan hak pemilik modal.",
        "distractors": [
            "$\\text{Aset} = \\text{Ekuitas} - \\text{Liabilitas} + \\text{Beban Operasional}$, yang mengabaikan hak klaim kreditur luar.",
            "$\\text{Aset} + \\text{Liabilitas} = \\text{Ekuitas} - \\text{Prive Pemilik}$, yang membalik posisi pasiva.",
            "$\\text{Liabilitas} = \\text{Aset} + \\text{Ekuitas}$, yang mengasumsikan utang menampung seluruh kekayaan perusahaan.",
            "$\\text{Pendapatan} = \\text{Aset} - \\text{Beban}$, yang hanya mengukur laba kotor periode berjalan."
        ],
        "formula": {
            "title": "PERSAMAAN DASAR AKUNTANSI PERUSAHAAN",
            "latex": "\\text{Aset} = \\text{Liabilitas} + \\text{Ekuitas} + (\\text{Pendapatan} - \\text{Beban} - \\text{Prive})",
            "legend": "• Sisi Kiri (Aktiva/Aset): Kas, Piutang, Perlengkapan, Peralatan, Gedung<br>• Sisi Kanan (Pasiva): Utang Usaha, Utang Bank, Modal Saham, Laba Ditahan<br>• Posisi Debit Normal: Aset dan Beban bertambah di Debit<br>• Posisi Kredit Normal: Liabilitas, Ekuitas, dan Pendapatan bertambah di Kredit"
        },
        "hints": {
            "concept": "Persamaan dasar akuntansi baku: Aset = Liabilitas + Ekuitas (Harta = Utang + Modal).",
            "execution": "Pilih: Aset = Liabilitas + Ekuitas."
        }
    },
    {
        "id": "eko-lat-e-06",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Hukum Gossen I tentang Nilai Guna Marjinal yang Semakin Menurun",
        "stem": "Ketika seseorang yang sangat haus meminum segelas air dingin pertama, ia merasakan kepuasan yang sangat tinggi. Pada gelas kedua kepuasannya masih bertambah, namun pada gelas ketiga, keempat, dan seterusnya, tambahan kepuasan dari tiap gelas tambahan semakin berkurang hingga akhirnya mencapai titik jenuh. Gejala psikologis konsumsi ini dirumuskan dalam...",
        "correct": "Hukum Gossen I (The Law of Diminishing Marginal Utility), yang menyatakan bahwa jika konsumsi satu jenis barang dilakukan secara terus-menerus, tambahan kepuasan (Marginal Utility) yang diperoleh akan semakin menurun.",
        "distractors": [
            "Hukum Gossen II, yang mengatur pengalokasian pendapatan untuk berbagai jenis barang guna mencapai kepuasan yang sama.",
            "Hukum Penawaran Say, yang menyatakan bahwa setiap penawaran barang akan otomatis menciptakan permintaannya sendiri.",
            "Hukum Hasil Lebih yang Semakin Berkurang (The Law of Diminishing Returns), yang berlaku pada fungsi produksi input produsen.",
            "Hukum Permintaan Keynes, yang menyatakan konsumsi agregat bergantung pada pendapatan disposabel absolut."
        ],
        "formula": {
            "title": "HUKUM GOSSEN I (DIMINISHING MARGINAL UTILITY)",
            "latex": "MU = \\frac{\\Delta TU}{\\Delta Q}, \\quad Q \\uparrow \\implies MU \\downarrow \\quad (\\text{Saat } MU = 0 \\implies TU \\text{ Maksimum})",
            "legend": "• $TU$ (Total Utility): Total kepuasan yang dinikmati konsumen<br>• $MU$ (Marginal Utility): Tambahan kepuasan per unit tambahan konsumsi barang<br>• Titik Kepuasan Maksimum: Dicapai saat $MU = 0$; jika konsumsi ditambah lagi maka $MU < 0$ (disutility)"
        },
        "hints": {
            "concept": "Konsumsi terus menerus atas 1 jenis barang menghasilkan tambahan kepuasan (MU) yang semakin berkurang adalah Hukum Gossen I.",
            "execution": "Pilih: Hukum Gossen I (The Law of Diminishing Marginal Utility)."
        }
    },
    {
        "id": "eko-lat-e-07",
        "materi": "STRUKTUR PASAR",
        "topic": "Ciri Khas Pasar Persaingan Sempurna (Perfect Competition)",
        "stem": "Dalam teori ekonomi mikro, Pasar Persaingan Sempurna (PPS) merupakan struktur pasar yang paling efisien secara alokatif. Salah satu ciri utama yang membedakan produsen di pasar persaingan sempurna dengan pasar monopoli adalah...",
        "correct": "Produsen bertindak sebagai penerima harga (Price Taker), di mana harga ditentukan sepenuhnya oleh mekanisme kekuatan pasar sehingga kurva permintaan yang dihadapi perusahaan berbentuk horizontal elastis sempurna ($P = AR = MR$).",
        "distractors": [
            "Produsen memiliki hak paten legal untuk menentukan harga jual setinggi-tingginya secara sepihak (Price Maker).",
            "Barang yang diperjualbelikan memiliki diferensiasi produk yang sangat unik dan didukung promosi iklan gencar.",
            "Terdapat hambatan masuk pasar yang sangat tinggi (barrier to entry) berupa modal teknologi raksasa.",
            "Hanya terdapat segelintir perusahaan raksasa yang saling mengawasi reaksi penetapan harga pesaing."
        ],
        "formula": {
            "title": "STRUKTUR KURVA PASAR PERSAINGAN SEMPURNA",
            "latex": "P = \\text{Market Price} \\implies D = AR = MR = P \\quad (\\text{Horizontal Elastis Sempurna})",
            "legend": "• Ciri Pasar Persaingan Sempurna: Banyak penjual & pembeli, produk homogen, bebas keluar-masuk (free entry/exit), informasi sempurna<br>• Laba Maksimum Produsen: Dicapai pada saat $MR = MC = P$<br>• Jangka Panjang: Hanya memperoleh laba normal (normal profit, $P = AC_{\\min}$)"
        },
        "hints": {
            "concept": "Di PPS, produsen adalah price taker (penerima harga), kurva permintaan horizontal elastis sempurna P = AR = MR.",
            "execution": "Pilih: Produsen bertindak sebagai penerima harga (Price Taker) dengan kurva permintaan horizontal."
        }
    },
    {
        "id": "eko-lat-e-08",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Teori Keunggulan Mutlak Adam Smith (Absolute Advantage)",
        "stem": "Dalam perdagangan internasional, Adam Smith dalam karyanya _The Wealth of Nations_ (1776) merumuskan Teori Keunggulan Mutlak (Absolute Advantage). Suatu negara dinyatakan memiliki keunggulan mutlak dibandingkan negara lain dalam memproduksi suatu komoditas jika...",
        "correct": "Negara tersebut mampu memproduksi komoditas tersebut dengan biaya absolut yang lebih rendah atau menggunakan sumber daya/tenaga kerja yang lebih sedikit per unit output dibandingkan negara mitra.",
        "distractors": [
            "Negara tersebut memiliki biaya peluang (opportunity cost) yang lebih rendah dalam memproduksi barang tersebut.",
            "Negara tersebut mengenakan tarif bea masuk paling tinggi untuk memblokir barang impor dari luar negeri.",
            "Negara tersebut memiliki jumlah cadangan emas batangan terbesar di brankas bank sentralnya.",
            "Negara tersebut menguasai seluruh hak distribusi dagang secara monopoli di pasar modal dunia."
        ],
        "formula": {
            "title": "TEORI KEUNGGULAN MUTLAK ADAM SMITH",
            "latex": "\\text{Keunggulan Mutlak} \\iff \\text{Output per Jam Kerja } (O_A > O_B) \\quad \\lor \\quad \\text{Biaya Tenaga Kerja } (L_A < L_B)",
            "legend": "• Adam Smith (Absolute Advantage): Spesialisasi pada barang yang diproduksi lebih efisien secara mutlak<br>• David Ricardo (Comparative Advantage): Spesialisasi pada barang dengan biaya peluang (opportunity cost) terendah"
        },
        "hints": {
            "concept": "Keunggulan mutlak Adam Smith berbasis keunggulan produksi langsung (biaya absolut lebih murah / output lebih banyak per unit input).",
            "execution": "Pilih: Mampu memproduksi dengan biaya absolut lebih rendah atau sumber daya lebih sedikit."
        }
    },
    {
        "id": "eko-lat-e-09",
        "materi": "BADAN USAHA & KOPERASI",
        "topic": "Prinsip Pembagian Sisa Hasil Usaha (SHU) Koperasi",
        "stem": "Berdasarkan Undang-Undang No. 25 Tahun 1992 tentang Perkoperasian, Sisa Hasil Usaha (SHU) koperasi yang dibagikan kepada anggota tidak dihitung semata-mata berdasarkan besarnya modal yang disetor, melainkan dialokasikan berdasarkan...",
        "correct": "Jasa usaha transaksi yang dilakukan oleh masing-masing anggota (Jasa Anggota) dan besarnya simpanan modal yang disetor anggota pada koperasi (Jasa Modal).",
        "distractors": [
            "Tingkat jabatan struktural dan lamanya masa keanggotaan pengurus di dewan pembina koperasi.",
            "Tingkat pendidikan formal tertinggi dan jumlah anggota keluarga yang tercantum di kartu keluarga.",
            "Jumlah pinjaman dana macet yang belum dilunasi oleh anggota kepada kas operasional koperasi.",
            "Dibagikan sama rata secara mutlak kepada seluruh anggota tanpa mempedulikan transaksi dan simpanan."
        ],
        "formula": {
            "title": "FORMULA PEMBAGIAN SHU ANGGOTA KOPERASI",
            "latex": "\\text{SHU Anggota}_i = \\text{Jasa Modal (JM)}_i + \\text{Jasa Usaha (JU)}_i = \\left( \\frac{\\text{Simpanan}_i}{\\sum \\text{Simpanan}} \\times \\text{SHU}_{\\text{Modal}} \\right) + \\left( \\frac{\\text{Transaksi}_i}{\\sum \\text{Transaksi}} \\times \\text{SHU}_{\\text{Usaha}} \\right)",
            "legend": "• Jasa Modal: Imbalan atas partisipasi modal (Simpanan Pokok + Simpanan Wajib)<br>• Jasa Usaha: Imbalan atas keaktifan bertransaksi (belanja di toko koperasi atau meminjam di unit simpan pinjam)"
        },
        "hints": {
            "concept": "SHU anggota koperasi dibagi berdasarkan dua pilar: Jasa Modal (simpanan) dan Jasa Anggota/Usaha (aktivitas transaksi).",
            "execution": "Pilih: Jasa usaha transaksi anggota dan besarnya simpanan modal anggota."
        }
    },
    {
        "id": "eko-lat-e-10",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Mekanisme Debit dan Kredit Penyetoran Modal Awal",
        "stem": "Tuan Ahmad menyetorkan uang tunai sebesar Rp 50.000.000,- dan sebuah kendaraan operasional senilai Rp 120.000.000,- sebagai modal awal pendirian usaha bengkel motor miliknya. Pencatatan ayat jurnal umum yang benar untuk transaksi tersebut adalah...",
        "correct": "Kas (Debit) Rp 50.000.000,-; Kendaraan (Debit) Rp 120.000.000,-; dan Modal Ahmad (Kredit) Rp 170.000.000,-.",
        "distractors": [
            "Modal Ahmad (Debit) Rp 170.000.000,-; Kas (Kredit) Rp 50.000.000,-; dan Kendaraan (Kredit) Rp 120.000.000,-.",
            "Kas (Debit) Rp 50.000.000,-; Pendapatan Jasa (Kredit) Rp 50.000.000,-; dan Kendaraan tidak dicatat.",
            "Beban Modal (Debit) Rp 170.000.000,- dan Utang Usaha (Kredit) Rp 170.000.000,-.",
            "Prive Ahmad (Debit) Rp 170.000.000,- dan Kas (Kredit) Rp 170.000.000,-."
        ],
        "formula": {
            "title": "ATURAN DEBIT DAN KREDIT AKUNTANSI KEUANGAN",
            "latex": "\\begin{aligned} \\text{Aset Bertambah} & \\implies \\text{DEBIT (Kas: 50 Jt, Kendaraan: 120 Jt)} \\\\ \\text{Ekuitas Bertambah} & \\implies \\text{KREDIT (Modal Ahmad: 170 Jt)} \\end{aligned}",
            "legend": "• Prinsip Double-Entry: Total nilai Debit (170 Juta) harus sama persis dengan total nilai Kredit (170 Juta)"
        },
        "hints": {
            "concept": "Kas dan Kendaraan adalah aset (bertambah di Debit). Modal adalah ekuitas (bertambah di Kredit).",
            "execution": "Pilih: Kas (Debit) 50 Jt, Kendaraan (Debit) 120 Jt, Modal Ahmad (Kredit) 170 Jt."
        }
    },
    {
        "id": "eko-lat-e-11",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Tiga Masalah Pokok Ekonomi Modern (What, How, For Whom)",
        "stem": "Masalah ekonomi klasik berfokus pada produksi, distribusi, dan konsumsi. Sementara itu, dalam ekonomi modern, permasalahan pokok yang dihadapi masyarakat dirumuskan ke dalam tiga pertanyaan mendasar, yaitu...",
        "correct": "Barang apa yang akan diproduksi dan berapa banyak (_What_), bagaimana cara memproduksi barang tersebut (_How_), dan untuk siapa barang tersebut diproduksi (_For Whom_).",
        "distractors": [
            "Kapan barang diproduksi (_When_), di mana lokasi pabrik dibangun (_Where_), dan siapa nama pemilik perusahaan (_Who_).",
            "Berapa harga jual barang di pasar (_How Much_), bagaimana cara mengiklankannya (_How to Sell_), dan mengapa barang dibuat (_Why_).",
            "Apakah barang harus diekspor (_Export_), berapa nilai kurs mata uang (_Exchange Rate_), dan bagaimana cara memungut pajak (_Tax_).",
            "Berapa jumlah pegawai yang dibutuhkan (_Labor_), bagaimana cara mendapatkan pinjaman bank (_Loan_), dan berapa lama masa sewa (_Lease_)."
        ],
        "formula": {
            "title": "TIGA MASALAH POKOK EKONOMI MODERN",
            "latex": "\\text{Masalah Ekonomi Modern} \\equiv \\begin{cases} \\mathbf{\\text{What:}} & \\text{Komoditas apa yang diproduksi \\& berapa kuantitasnya} \\\\ \\mathbf{\\text{How:}} & \\text{Teknologi/kombinasi faktor produksi (Padat Karya vs Padat Modal)} \\\\ \\mathbf{\\text{For Whom:}} & \\text{Target segmen pasar \\& distribusi pendapatan masyarakat} \\end{cases}",
            "legend": "• Masalah Pokok Klasik: Produksi, Distribusi, Konsumsi<br>• Masalah Pokok Modern: What, How, For Whom (dipelopori oleh Paul A. Samuelson)"
        },
        "hints": {
            "concept": "Tiga masalah pokok ekonomi modern adalah What, How, dan For Whom.",
            "execution": "Pilih: Barang apa yang diproduksi (What), bagaimana memproduksinya (How), dan untuk siapa diproduksi (For Whom)."
        }
    },
    {
        "id": "eko-lat-e-12",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Karakteristik Kurva Permintaan Inelastis Sempurna",
        "stem": "Obat-obatan penyelamat nyawa pasien darurat (seperti insulin bagi penderita diabetes akut) memiliki sifat di mana berapapun kenaikan harga yang ditetapkan, kuantitas barang yang dibutuhkan dan dibeli oleh konsumen tetap sama persis. Koefisien elastisitas harga permintaan ($E_d$) serta bentuk kurva permintaan komoditas tersebut adalah...",
        "correct": "$E_d = 0$ (Inelastis Sempurna), dengan bentuk kurva permintaan berupa garis lurus vertikal tegak lurus terhadap sumbu horizontal kuantitas.",
        "distractors": [
            "$E_d = 1$ (Elastis Uniter), dengan bentuk kurva berupa kurva hiperbola persegi simetris.",
            "$E_d = \\infty$ (Elastis Sempurna), dengan bentuk kurva berupa garis horizontal mendatar sejajar sumbu kuantitas.",
            "$E_d > 1$ (Elastis), dengan kurva permintaan yang berbentuk sangat landai mendekati sumbu horizontal.",
            "$E_d < 1$ (Inelastis), dengan kurva permintaan yang memotong sumbu vertikal pada titik harga negatif."
        ],
        "formula": {
            "title": "KLASIFIKASI KOEFISIEN ELASTISITAS PERMINTAAN HARGA",
            "latex": "\\begin{aligned} E_d = 0 & \\implies \\text{Inelastis Sempurna (Kurva Vertikal Tegak)} \\\\ E_d < 1 & \\implies \\text{Inelastis (Curam, misal beras/kebutuhan pokok)} \\\\ E_d = 1 & \\implies \\text{Unitary Elastic (Uniter)} \\\\ E_d > 1 & \\implies \\text{Elastis (Landai, misal barang mewah)} \\\\ E_d = \\infty & \\implies \\text{Elastis Sempurna (Garis Horizontal Mendatar)} \\end{aligned}",
            "legend": "• Formula: $E_d = |\\%\\Delta Q / \\%\\Delta P|$<br>• Pada $E_d = 0$, $\%\\Delta Q = 0$ berapapun $\%\\Delta P$"
        },
        "hints": {
            "concept": "Kuantitas tidak berubah sama sekali terhadap perubahan harga berarti inelastis sempurna: Ed = 0, kurva vertikal tegak.",
            "execution": "Pilih: Ed = 0 (Inelastis Sempurna) dengan kurva garis vertikal."
        }
    },
    {
        "id": "eko-lat-e-13",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Konsep Pendapatan Disposabel (Disposable Income)",
        "stem": "Dalam rantai perhitungan pendapatan nasional menuju daya beli riil individu, Pendapatan Disposabel (Disposable Income / DI) adalah bagian pendapatan yang siap dibelanjakan untuk konsumsi atau ditabung. Formula untuk memperoleh Disposable Income dari Pendapatan Perseorangan (Personal Income / PI) adalah...",
        "correct": "$\\text{DI} = \\text{Personal Income (PI)} - \\text{Pajak Langsung (Direct Tax)}$, di mana pajak langsung contohnya adalah Pajak Penghasilan (PPh).",
        "distractors": [
            "$\\text{DI} = \\text{Personal Income} + \\text{Pajak Pertambahan Nilai (PPN)} - \\text{Subsidi}$.",
            "$\\text{DI} = \\text{Net National Income (NNI)} - \\text{Penyusutan Barang Modal}$.",
            "$\\text{DI} = \\text{Gross National Product} - \\text{Iuran Jaminan Sosial} - \\text{Laba Ditahan}$.",
            "$\\text{DI} = \\text{Personal Income} \\times \\text{Tingkat Bunga Tabungan Bank}$."
        ],
        "formula": {
            "title": "RANGKAIAN AGREGAT PENDAPATAN NASIONAL",
            "latex": "\\begin{aligned} \\text{GNP} - \\text{Penyusutan} & = \\text{NNP} \\\\ \\text{NNP} - \\text{Pajak Tak Langsung} + \\text{Subsidi} & = \\text{NNI} \\\\ \\text{NNI} - \\text{Laba Ditahan} - \\text{Asuransi} + \\text{Transfer Payment} & = \\text{PI} \\\\ \\mathbf{\\text{PI} - \\text{Pajak Langsung}} & = \\mathbf{\\text{DI}} \\implies \\text{DI} = C + S \\end{aligned}",
            "legend": "• Pajak Langsung: Pajak yang bebannya tidak dapat dialihkan ke pihak lain (misal PPh)<br>• DI dialokasikan menjadi dua komponen: Konsumsi ($C$) dan Tabungan ($S$)"
        },
        "hints": {
            "concept": "Disposable Income (DI) = Personal Income (PI) - Pajak Langsung (PPh).",
            "execution": "Pilih: DI = Personal Income (PI) - Pajak Langsung (Direct Tax)."
        }
    },
    {
        "id": "eko-lat-e-14",
        "materi": "KEBIJAKAN MONETER & FISKAL",
        "topic": "Instrumen Kebijakan Fiskal Kontraktif untuk Meredam Inflasi",
        "stem": "Pemerintah bersama Kementerian Keuangan bertanggung jawab mengendalikan perekonomian makro melalui kebijakan fiskal (anggaran belanja dan perpajakan). Jika perekonomian mengalami tekanan inflasi yang sangat tinggi akibat lonjakan permintaan agregat, paket kebijakan fiskal yang tepat dijalankan oleh pemerintah adalah...",
        "correct": "Kebijakan Fiskal Kontraktif, yaitu menaikkan tarif pajak dan memangkas pengeluaran/belanja negara untuk menyerap kelebihan daya beli masyarakat.",
        "distractors": [
            "Kebijakan Fiskal Ekspansif, yaitu menurunkan tarif pajak dan melipatgandakan anggaran belanja proyek infrastruktur publik.",
            "Kebijakan Moneter Diskonto, yaitu menurunkan tingkat suku bunga pinjaman bank sentral kepada bank komersial.",
            "Mencetak uang kertas baru dalam jumlah masif untuk membagikan bantuan langsung tunai kepada seluruh warga.",
            "Menghapus seluruh bea ekspor komoditas mentah ke luar negeri tanpa memungut pajak pertambahan nilai."
        ],
        "formula": {
            "title": "KEBIJAKAN FISKAL KONTRAKTIF (ANTI-INFLASI)",
            "latex": "\\text{Inflasi Tinggi} \\implies T \\uparrow \\text{ (Pajak Naik)} \\quad \\land \\quad G \\downarrow \\text{ (Belanja Turun)} \\implies Y_d \\downarrow \\implies AD \\downarrow",
            "legend": "• Kebijakan Fiskal Ekspansif ($T \\downarrow, G \\uparrow$): Digunakan saat deflasi, pengangguran tinggi, atau resesi ekonomi<br>• Kebijakan Fiskal Kontraktif ($T \\uparrow, G \\downarrow$): Digunakan saat ekonomi _overheating_ dan inflasi tinggi"
        },
        "hints": {
            "concept": "Meredam inflasi via fiskal: kurangi pengeluaran belanja pemerintah (G turun) dan naikkan tarif pajak (T naik).",
            "execution": "Pilih: Kebijakan Fiskal Kontraktif, menaikkan tarif pajak dan memangkas pengeluaran negara."
        }
    },
    {
        "id": "eko-lat-e-15",
        "materi": "LEMBAGA KEUANGAN & PASAR MODAL",
        "topic": "Tugas dan Wewenang Otoritas Jasa Keuangan (OJK)",
        "stem": "Berdasarkan Undang-Undang No. 21 Tahun 2011, Otoritas Jasa Keuangan (OJK) dibentuk sebagai lembaga independen yang berwenang mengatur dan mengawasi sektor jasa keuangan di Indonesia. Lembaga-lembaga yang berada di bawah lingkup pengaturan dan pengawasan OJK adalah...",
        "correct": "Sektor Perbankan, Pasar Modal, serta Perasuransian, Dana Pensiun, Lembaga Pembiayaan, dan Lembaga Jasa Keuangan Lainnya (IKNB).",
        "distractors": [
            "Khusus mencetak dan mengedarkan uang rupiah fisik serta mengatur kebijakan nilai tukar valuta asing secara eksklusif.",
            "Mengelola penerimaan perpajakan negara dan menyusun Anggaran Pendapatan dan Belanja Negara (APBN).",
            "Mengawasi persaingan usaha tidak sehat antar perusahaan ritel di bawah komisi anti-monopoli.",
            "Mengadili sengketa tindak pidana korupsi pejabat negara di lembaga peradilan tindak pidana khusus."
        ],
        "formula": {
            "title": "PEMBAGIAN WEWENANG OTORITAS MONETER & JASA KEUANGAN",
            "latex": "\\begin{aligned} \\text{Bank Indonesia (BI):} & \\quad \\text{Kebijakan Moneter, Sistem Pembayaran, Stabilitas Makroprudensial} \\\\ \\text{Otoritas Jasa Keuangan (OJK):} & \\quad \\text{Pengaturan \\& Pengawasan Mikroprudensial (Bank, Pasar Modal, IKNB, Fintech)} \\\\ \\text{Kementerian Keuangan (Kemenkeu):} & \\quad \\text{Kebijakan Fiskal, Pengelolaan Kas Negara (APBN), Perpajakan} \\end{aligned}",
            "legend": "• OJK bertugas memastikan seluruh kegiatan jasa keuangan terselenggara secara teratur, adil, transparan, dan akuntabel serta melindungi kepentingan konsumen"
        },
        "hints": {
            "concept": "OJK mengatur dan mengawasi mikroprudensial: perbankan, pasar modal, dan industri keuangan non-bank (IKNB).",
            "execution": "Pilih: Sektor Perbankan, Pasar Modal, Perasuransian, Dana Pensiun, dan Lembaga Pembiayaan (IKNB)."
        }
    },
    {
        "id": "eko-lat-e-16",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Dampak Kebijakan Penetapan Harga Maksimum (Ceiling Price)",
        "stem": "Untuk melindungi konsumen berpendapatan rendah dari lonjakan harga bahan pokok saat hari raya, pemerintah menetapkan Harga Eceran Tertinggi (HET / Ceiling Price) yang berada di bawah tingkat harga keseimbangan pasar bebas ($P_{\\text{ceiling}} < P_e$). Dampak ekonomis langsung yang akan timbul di pasar akibat kebijakan tersebut adalah...",
        "correct": "Terjadi kelebihan permintaan (Shortage / Excess Demand), karena pada harga murah jumlah barang yang diminta konsumen meningkat drastis sementara produsen enggan menambah jumlah penawaran barang.",
        "distractors": [
            "Terjadi kelebihan penawaran (Surplus / Excess Supply), sehingga barang menumpuk tak terjual di gudang pedagang.",
            "Produsen memperoleh laba super-normal yang luar biasa besar karena volume penjualan meningkat tak terbatas.",
            "Kurva permintaan bergeser ke kiri bawah secara permanen dan kurva penawaran menjadi vertikal tegak.",
            "Harga pasar seketika melonjak menjadi dua kali lipat dari harga keseimbangan awal tanpa ada intervensi."
        ],
        "formula": {
            "title": "ANALISIS PASAR PENETAPAN HARGA MAKSIMUM (PRICE CEILING)",
            "latex": "P_{\\text{ceiling}} < P_e \\implies Q_d > Q_s \\implies \\text{Shortage (Kekurangan Pasokan / Excess Demand)}",
            "legend": "• Dampak Sampingan Price Ceiling: Antrean panjang, pasar gelap (black market), penjatahan kupon (rationing)<br>• Kebijakan Sebaliknya: Harga Dasar (Floor Price, $P_{\\text{floor}} > P_e$) melindungi produsen/petani, memicu Surplus/Excess Supply"
        },
        "hints": {
            "concept": "Harga maksimum di bawah ekuilibrium membuat harga murah: konsumen minta banyak (Qd naik), penjual tawarkan sedikit (Qs turun) -> Terjadi Shortage (Kelebihan Permintaan).",
            "execution": "Pilih: Terjadi kelebihan permintaan (Shortage / Excess Demand)."
        }
    },
    {
        "id": "eko-lat-e-17",
        "materi": "PERILAKU KONSUMEN & PRODUSEN",
        "topic": "Empat Faktor Produksi dan Balas Jasanya",
        "stem": "Dalam arus lingkaran kegiatan ekonomi (Circular Flow Diagram), rumah tangga konsumen (RTK) menyerahkan faktor-faktor produksi kepada rumah tangga produsen (RTP). Balas jasa pendapatan yang diterima oleh pemilik faktor produksi modal (Capital) dan kewirausahaan (Entrepreneurship) secara berturut-turut adalah...",
        "correct": "Bunga modal (Interest) dan Laba/Keuntungan usaha (Profit).",
        "distractors": [
            "Sewa tanah (Rent) dan Upah tenaga kerja (Wage).",
            "Upah tenaga kerja (Wage) dan Bunga modal (Interest).",
            "Laba usaha (Profit) dan Pajak penghasilan (Tax).",
            "Sewa tanah (Rent) dan Subsidi pemerintah (Subsidy)."
        ],
        "formula": {
            "title": "FAKTOR PRODUKSI DAN BALAS JASA PENDAPATAN (CIRCULAR FLOW)",
            "latex": "\\begin{array}{|l|l|} \\hline \\text{Faktor Produksi} & \\text{Balas Jasa Pendapatan} \\\\ \\hline \\text{Sumber Daya Alam (Tanah)} & \\text{Sewa (Rent)} \\\\ \\text{Tenaga Kerja (Labor)} & \\text{Upah/Gaji (Wage)} \\\\ \\mathbf{\\text{Modal (Capital)}} & \\mathbf{\\text{Bunga (Interest)}} \\\\ \\mathbf{\\text{Kewirausahaan (Skill)}} & \\mathbf{\\text{Laba/Keuntungan (Profit)}} \\\\ \\hline \\end{array}",
            "legend": "• Pendekatan Pendapatan dalam Pendapatan Nasional: $Y = r + w + i + p$"
        },
        "hints": {
            "concept": "Modal mendapat bunga (interest), kewirausahaan/keahlian mendapat laba (profit).",
            "execution": "Pilih: Bunga modal (Interest) dan Laba/Keuntungan usaha (Profit)."
        }
    },
    {
        "id": "eko-lat-e-18",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Komponen Utama Neraca Berjalan (Current Account)",
        "stem": "Neraca Pembayaran Internasional (Balance of Payments) mencatat seluruh transaksi ekonomi antar penduduk suatu negara dengan negara lain. Transaksi-transaksi ekonomi yang dicatat di dalam Neraca Berjalan (Current Account) meliputi...",
        "correct": "Neraca perdagangan barang (ekspor dan impor barang), neraca jasa (transportasi dan pariwisata), pendapatan primer (gaji TKI dan dividen investasi), serta pendapatan sekunder (hibah dan kiriman uang remitansi).",
        "distractors": [
            "Investasi langsung asing (FDI), investasi portofolio saham/obligasi, dan pinjaman utang luar negeri.",
            "Perubahan cadangan devisa emas bank sentral dan transaksi derivatif keuangan berjangka.",
            "Penerimaan pajak bumi dan bangunan serta retribusi daerah di dalam negeri.",
            "Pembelian surat utang negara oleh investor domestik pada pasar modal lokal."
        ],
        "formula": {
            "title": "STRUKTUR NERACA PEMBAYARAN INTERNASIONAL (BOP)",
            "latex": "\\text{Neraca Pembayaran} = \\mathbf{\\text{Neraca Berjalan}} + \\text{Neraca Modal} + \\text{Neraca Finansial} + \\text{Cadangan Devisa}",
            "legend": "• Neraca Berjalan: Ekspor-Impor Barang, Jasa, Pendapatan Primer, Pendapatan Sekunder<br>• Neraca Finansial: Penanaman Modal Asing Langsung (FDI), Portofolio Saham/Obligasi, Pinjaman Komersial"
        },
        "hints": {
            "concept": "Neraca Berjalan mencakup: perdagangan barang (ekspor/impor), jasa, pendapatan primer, dan transfer pendapatan sekunder.",
            "execution": "Pilih: Neraca perdagangan barang, neraca jasa, pendapatan primer, dan pendapatan sekunder."
        }
    },
    {
        "id": "eko-lat-e-19",
        "materi": "BADAN USAHA & KOPERASI",
        "topic": "Karakteristik Yuridis Perseroan Terbatas (PT)",
        "stem": "Bentuk badan usaha berbadan hukum Perseroan Terbatas (PT) sangat diminati dalam dunia bisnis modern. Keunggulan yuridis paling mendasar yang dimiliki oleh pemilik saham pada sebuah Perseroan Terbatas adalah...",
        "correct": "Tanggung jawab pemilik modal bersifat terbatas (Limited Liability), di mana risiko kerugian yang ditanggung pemegang saham hanya sebesar nilai nominal saham yang disetorkan dan tidak melibatkan harta kekayaan pribadi.",
        "distractors": [
            "Seluruh utang perusahaan wajib dilunasi menggunakan rumah dan tabungan pribadi para pemegang saham tanpa batas.",
            "Perusahaan tidak diwajibkan membayar pajak badan usaha kepada pemerintah pusat sama sekali.",
            "Masa operasional perusahaan otomatis berakhir dan dibubarkan apabila salah satu pemegang saham meninggal dunia.",
            "Setiap pemegang saham memiliki hak mutlak untuk memimpin operasional harian perusahaan tanpa persetujuan direksi."
        ],
        "formula": {
            "title": "KOMPARASI BENTUK BADAN USAHA SWASTA (BUMS)",
            "latex": "\\begin{aligned} \\text{Perusahaan Perseorangan:} & \\quad \\text{Tanggung Jawab Tidak Terbatas (Harta Pribadi Terancam)} \\\\ \\text{Firma (Fa) / CV (Sekutu Aktif):} & \\quad \\text{Tanggung Jawab Solider Tidak Terbatas} \\\\ \\mathbf{\\text{Perseroan Terbatas (PT):}} & \\quad \\mathbf{\\text{Tanggung Jawab Terbatas (Limited Liability) Sebesar Saham Disetor}} \\end{aligned}",
            "legend": "• PT merupakan badan hukum mandiri (separate legal entity) yang terpisah dari pemiliknya<br>• Kontinuitas usaha terjamin meskipun terjadi pergantian kepemilikan saham"
        },
        "hints": {
            "concept": "Ciri khas PT: Tanggung jawab pemegang saham terbatas (limited liability) sebatas modal saham yang disetor.",
            "execution": "Pilih: Tanggung jawab pemilik modal bersifat terbatas sebatas modal yang disetorkan."
        }
    },
    {
        "id": "eko-lat-e-20",
        "materi": "AKUNTANSI KEUANGAN",
        "topic": "Klasifikasi Akun Beban Dibayar di Muka pada Neraca",
        "stem": "Pada tanggal 1 September, perusahaan membayar uang sewa kantor sebesar Rp 24.000.000,- untuk masa sewa 1 tahun ke depan. Pada saat pembayaran dicatat menggunakan pendekatan neraca (harta), akun yang didebit adalah `Sewa Dibayar di Muka`. Dalam laporan posisi keuangan (neraca), akun `Sewa Dibayar di Muka` tersebut diklasifikasikan sebagai...",
        "correct": "Aset Lancar (Current Assets), karena perusahaan memiliki hak ekonomis atas manfaat ruangan kantor di masa depan yang akan habis digunakan dalam periode kurang dari satu tahun.",
        "distractors": [
            "Beban Operasional Penjualan, karena uang tunai sudah keluar dari rekening bank perusahaan.",
            "Liabilitas Jangka Pendek (Utang Lancar), karena perusahaan berutang ruangan kepada pemilik gedung.",
            "Ekuitas Modal Pemilik, karena sewa kantor menambah nilai investasi jangka panjang perusahaan.",
            "Aset Tetap Berwujud, setara dengan kepemilikan hak milik tanah dan bangunan permanen."
        ],
        "formula": {
            "title": "KLASIFIKASI BEBAN DIBAYAR DI MUKA (PREPAID EXPENSES)",
            "latex": "\\text{Kas Keluar di Awal} \\implies \\text{Timbul Hak/Klaim Manfaat Jasa Masa Depan} \\implies \\text{Aset Lancar (Harta)}",
            "legend": "• Transisi Penyesuaian (AJP): Seiring berjalannya waktu, porsi sewa yang telah terlewati masa pakainya akan diakui sebagai Beban Sewa (Expense), dan sisa saldo tetap sebagai Aset Lancar"
        },
        "hints": {
            "concept": "Sewa dibayar di muka adalah hak ekonomis yang dinikmati di masa depan, diklasifikasikan sebagai Aset Lancar (Current Assets).",
            "execution": "Pilih: Aset Lancar (Current Assets)."
        }
    },
    {
        "id": "eko-lat-e-21",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Tiga Motif Memegang Uang Menurut John Maynard Keynes",
        "stem": "Dalam Teori Preferensi Likuiditas (Liquidity Preference Theory) yang dikemukakan oleh John Maynard Keynes, masyarakat memiliki tiga motif mendasar dalam menahan uang tunai likuid. Ketiga motif tersebut adalah...",
        "correct": "Motif Transaksi (Transaction Motive), Motif Berjaga-jaga (Precautionary Motive), dan Motif Spekulasi (Speculative Motive).",
        "distractors": [
            "Motif Menabung, Motif Konsumsi, dan Motif Menghindari Pajak.",
            "Motif Investasi Fisik, Motif Perdagangan Saham, dan Motif Pembayaran Dividen.",
            "Motif Kedermawanan Sosial, Motif Pinjaman Bank, dan Motif Belanja Hiburan.",
            "Motif Ekspor Barang, Motif Impor Bahan Baku, dan Motif Arbitrase Valuta."
        ],
        "formula": {
            "title": "TEORI PREFERENSI LIKUIDITAS KEYNES (PERMINTAAN UANG)",
            "latex": "M_d = L_1(Y) + L_2(r) = \\underbrace{M_t + M_p}_{f(Y) \\text{ (Transaksi \\& Berjaga-jaga)}} + \\underbrace{M_s}_{f(r) \\text{ (Spekulasi, Suku Bunga)}}",
            "legend": "• Motif Transaksi & Berjaga-jaga ($L_1$): Dipengaruhi secara positif oleh tingkat pendapatan nasional ($Y$)<br>• Motif Spekulasi ($L_2$): Dipengaruhi secara negatif oleh tingkat suku bunga ($r$) pasar modal obligasi"
        },
        "hints": {
            "concept": "Tiga motif memegang uang Keynes: Transaksi, Berjaga-jaga, dan Spekulasi.",
            "execution": "Pilih: Motif Transaksi, Motif Berjaga-jaga, dan Motif Spekulasi."
        }
    },
    {
        "id": "eko-lat-e-22",
        "materi": "MEKANISME PASAR & ELASTISITAS",
        "topic": "Interpretasi Nilai Koefisien Elastisitas Silang (Cross Elasticity)",
        "stem": "Hasil perhitungan koefisien elastisitas silang antara komoditas teh ($X$) dan kopi ($Y$) menunjukkan nilai positif sebesar $E_{xy} = +1,8$. Berdasarkan nilai koefisien elastisitas silang tersebut, hubungan fungsional antara komoditas teh dan kopi adalah...",
        "correct": "Barang Substitusi (Saling Menggantikan), artinya jika harga kopi mengalami kenaikan, permintaan terhadap teh akan meningkat karena konsumen beralih mengonsumsi teh.",
        "distractors": [
            "Barang Komplementer (Saling Melengkapi), artinya kenaikan harga kopi akan menyebabkan permintaan terhadap teh menurun drastis.",
            "Barang Netral (Independen), artinya perubahan harga kopi sama sekali tidak memengaruhi kuantitas konsumsi teh.",
            "Barang Inferior, artinya konsumsi teh akan ditinggalkan ketika pendapatan konsumen mengalami peningkatan.",
            "Barang Giffen, artinya kenaikan harga teh akan menyebabkan masyarakat miskin membeli teh lebih banyak."
        ],
        "formula": {
            "title": "INTERPRETASI KOEFISIEN ELASTISITAS SILANG (CROSS ELASTICITY)",
            "latex": "E_{xy} = \\frac{\\% \\Delta Q_x}{\\% \\Delta P_y} \\implies \\begin{cases} E_{xy} > 0 & \\implies \\text{Barang Substitusi (Saling Menggantikan)} \\\\ E_{xy} < 0 & \\implies \\text{Barang Komplementer (Saling Melengkapi)} \\\\ E_{xy} = 0 & \\implies \\text{Barang Netral / Independen} \\end{cases}",
            "legend": "• Contoh Substitusi ($E_{xy} > 0$): Teh & Kopi, Mentega & Margarin<br>• Contoh Komplementer ($E_{xy} < 0$): Kopi & Gula, Mobil & Bensin"
        },
        "hints": {
            "concept": "Elastisitas silang positif (Exy > 0) menandakan kedua barang bersifat substitusi (saling menggantikan).",
            "execution": "Pilih: Barang Substitusi (Saling Menggantikan)."
        }
    },
    {
        "id": "eko-lat-e-23",
        "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
        "topic": "Analisis Ketimpangan Distribusi Pendapatan dengan Koefisien Gini",
        "stem": "Untuk mengukur derajat ketimpangan distribusi pendapatan masyarakat dalam suatu negara, para ekonom menggunakan indikator Koefisien Gini (Gini Ratio) yang diturunkan dari Kurva Lorenz. Karakteristik nilai Koefisien Gini yang menunjukkan tingkat distribusi pendapatan paling merata sempurna adalah...",
        "correct": "Nilai Koefisien Gini mendekati angka 0 (nol), di mana Kurva Lorenz berimpit sempurna dengan garis diagonal pemerataan sempurna.",
        "distractors": [
            "Nilai Koefisien Gini mendekati angka 1 (satu), di mana seluruh pendapatan nasional dinikmati hanya oleh satu orang terkaya.",
            "Nilai Koefisien Gini bernilai negatif minus satu ($-1$), yang mencerminkan deflasi ekonomi berkepanjangan.",
            "Nilai Koefisien Gini bernilai sama dengan 100, yang menandakan pertumbuhan ekonomi tercepat di dunia.",
            "Nilai Koefisien Gini berada di atas angka 2,5 sesuai standar toleransi inflasi Bank Dunia."
        ],
        "formula": {
            "title": "RENTANG NILAI KOEFISIEN GINI (GINI RATIO)",
            "latex": "0 \\le G \\le 1, \\quad \\begin{cases} G = 0 & \\implies \\text{Merata Sempurna (Perfect Equality)} \\\\ G < 0,4 & \\implies \\text{Ketimpangan Rendah} \\\\ 0,4 \\le G \\le 0,5 & \\implies \\text{Ketimpangan Sedang} \\\\ G > 0,5 & \\implies \\text{Ketimpangan Tinggi} \\\\ G = 1 & \\implies \\text{Timpang Sempurna (Perfect Inequality)} \\end{cases}",
            "legend": "• Formula Geometri: $G = A / (A + B)$, di mana $A$ adalah luas area antara garis diagonal dan Kurva Lorenz"
        },
        "hints": {
            "concept": "Koefisien Gini berkisar 0 sampai 1. Mendekati 0 berarti semakin merata sempurna. Mendekati 1 berarti semakin timpang.",
            "execution": "Pilih: Nilai Koefisien Gini mendekati 0 (nol), kurva berimpit dengan garis diagonal pemerataan."
        }
    },
    {
        "id": "eko-lat-e-24",
        "materi": "EKONOMI INTERNASIONAL",
        "topic": "Instrumen Proteksi Perdagangan: Kebijakan Kuota Impor",
        "stem": "Dalam perdagangan internasional, pemerintah dapat menerapkan kebijakan hambatan non-tarif berupa Kuota Impor. Tujuan utama pemerintah memberlakukan kuota impor terhadap suatu komoditas tertentu adalah...",
        "correct": "Membatasi jumlah fisik maksimum barang impor yang boleh masuk ke dalam negeri selama periode tertentu untuk melindungi produsen domestik dari serbuan produk luar negeri.",
        "distractors": [
            "Mengenakan tarif pajak persentase ad-valorem sebesar-besarnya untuk menambah penerimaan kas kasir bea cukai.",
            "Menjual barang ke pasar luar negeri dengan harga yang jauh lebih murah daripada harga jual di pasar domestik.",
            "Menghapus seluruh perizinan impor agar harga barang di pasar dalam negeri turun hingga titik terendah.",
            "Memaksa negara mitra dagang untuk menukarkan seluruh mata uang asingnya menjadi surat utang negara."
        ],
        "formula": {
            "title": "KEBIJAKAN HAMBATAN PERDAGANGAN INTERNASIONAL",
            "latex": "\\begin{aligned} \\text{Tarif (Hambatan Tarif):} & \\quad \\text{Pungutan bea masuk per unit / ad-valorem (Menaikkan harga barang impor)} \\\\ \\mathbf{\\text{Kuota Impor (Hambatan Non-Tarif):}} & \\quad \\mathbf{\\text{Pembatasan kuantitas fisik maksimum impor (Melindungi kuota produsen lokal)}} \\\\ \\text{Dumping:} & \\quad \\text{Harga jual ekspor lebih murah dibanding harga domestik} \\end{aligned}",
            "legend": "• Dampak Kuota: Kuantitas impor terkendali, harga domestik terlindungi, devisa keluar berkurang"
        },
        "hints": {
            "concept": "Kuota impor adalah pembatasan kuantitas fisik maksimum barang yang boleh diimpor untuk melindungi industri dalam negeri.",
            "execution": "Pilih: Membatasi jumlah fisik maksimum barang impor yang boleh masuk selama periode tertentu."
        }
    },
    {
        "id": "eko-lat-e-25",
        "materi": "KONSEP DASAR ILMU EKONOMI",
        "topic": "Ciri-Ciri Sistem Ekonomi Komando / Terpusat (Sosialis)",
        "stem": "Sistem ekonomi di dunia diklasifikasikan ke dalam sistem ekonomi tradisional, pasar bebas (kapitalis), komando (terpusat/sosialis), dan campuran. Ciri yang paling menonjol dari Sistem Ekonomi Komando adalah...",
        "correct": "Seluruh sumber daya dan faktor produksi strategis dikuasai sepenuhnya oleh negara/pemerintah pusat, sehingga hak milik individu tidak diakui dan kebebasan berusaha sangat dibatasi.",
        "distractors": [
            "Pemerintah sama sekali tidak ikut campur dalam perekonomian dan menyerahkan seluruhnya pada mekanisme pasar bebas.",
            "Harga komoditas terbentuk murni berdasarkan interaksi hukum permintaan dan penawaran di bursa efek.",
            "Masyarakat bebas memiliki modal produksi tanpa batas dan persaingan antar pengusaha berlangsung sangat ketat.",
            "Teknologi yang digunakan bersifat sangat sederhana dan sistem barter barang menjadi alat tukar utama masyarakat."
        ],
        "formula": {
            "title": "KOMPARASI SISTEM EKONOMI DUNIA",
            "latex": "\\begin{aligned} \\text{Pasar Bebas (Kapitalis):} & \\quad \\text{Mekanisme Pasar (Adam Smith), Hak Milik Swasta Penuh, Peran Negara Minimal} \\\\ \\mathbf{\\text{Komando (Sosialis):}} & \\quad \\mathbf{\\text{Direncanakan Pusat oleh Negara (Karl Marx), Hak Milik Pribadi Ditiadakan}} \\\\ \\text{Campuran / Pancasila:} & \\quad \\text{Sinergi Pasar \\& Intervensi Negara demi Kesejahteraan Bersama (Pasal 33 UUD 1945)} \\end{aligned}",
            "legend": "• Kelemahan Sistem Komando: Inisiatif dan daya kreasi individu mati, rentan inefisiensi birokrasi, variasi produk terbatas"
        },
        "hints": {
            "concept": "Sistem ekonomi komando: peran pemerintah dominan dan menguasai seluruh faktor produksi, hak milik swasta dibatasi.",
            "execution": "Pilih: Seluruh sumber daya dan faktor produksi dikuasai penuh oleh negara, hak milik individu tidak diakui."
        }
    }
]
