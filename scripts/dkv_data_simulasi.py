# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Desain Komunikasi Visual (DKV / Rekayasa Desain SMK/MAK)
Dataset: CBT Simulation (35 Authentic HOTS Items, tekd-sim-01 to 35)
Includes: 25 MCQ HOTS, 5 Complex Multi-select, 5 Matrix Benar-Salah
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

DKV_SIMULASI_ITEMS = [
    # 25 MCQ HOTS ITEMS (tekd-sim-01 to tekd-sim-25)
    {
        "id": "tekd-sim-01",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Finishing Khusus: Spot UV vs Hot Stamping Foil",
        "stem": "Dalam proyek pencetakan cover buku eksklusif bertema monokrom, desainer merancang agar seluruh permukaan cover dilapisi laminasi Doff (Matte) yang lembut dan tidak memantulkan cahaya. Namun, khusus pada teks judul dan logo utama diberikan efek lapisan cairan mengkilap transparan yang menonjol licin saat terkena cahaya. Teknik finishing pre-press yang diterapkan adalah...",
        "correct": "Spot UV Varnish di atas laminasi Doff, di mana cairan pernis polimer khusus disinari lampu ultraviolet selektif hanya pada area judul dan logo untuk menciptakan kontras tekstur kilap vs redup yang mewah.",
        "distractors": [
            "Hot Stamping Gold Foil, yang menempelkan lembaran logam emas berkilau menggunakan plat pemanas tembaga bertekanan hidrolik.",
            "Blind Debossing, yang menekan kertas ke arah dalam secara mekanis tanpa menambahkan bahan pelapis kimia apa pun.",
            "Laminasi Glossy penuh pada seluruh permukaan kertas yang menghilangkan seluruh efek redup matte cover buku.",
            "Sablon pasta karet timbul berwarna putih solid yang menutupi seluruh huruf judul dengan lapisan tebal 2 milimeter."
        ],
        "formula": {
            "title": "TEKNIK FINISHING CETAK: SPOT UV",
            "latex": "\\text{Cover Kontras Taktil} = \\text{Laminasi Doff (Base)} + \\text{Spot UV Film (Target Area)}",
            "legend": "• Base Doff: Menghilangkan silau dan melindungi tinta dasar dari goresan<br>• Spot UV: Memantulkan cahaya tinggi selektif (high gloss) pada elemen kunci<br>• Film Pisah: Membutuhkan file master warna hitam solid $K=100\\%$ pada layer khusus 'UV'"
        },
        "hints": {
            "concept": "Spot UV adalah pemberian pernis mengkilap pada bagian/area tertentu (spot) saja di atas lapisan doff untuk memunculkan efek kontras kilap yang elegan.",
            "execution": "Pilih Spot UV Varnish di atas laminasi doff."
        }
    },
    {
        "id": "tekd-sim-02",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Filter Lensa: Circular Polarizer (CPL) untuk Pantulan",
        "stem": "Seorang fotografer komersial ditugaskan memotret interior mobil mewah baru dari luar kaca jendela mobil dan model di tepi danau jernih. Tanpa filter, permukaan kaca mobil dan air danau memantulkan kilauan silau matahari yang menutupi jok kulit mobil dan dasar bebatuan danau. Filter optis kamera yang wajib dipasang di depan lensa untuk menghilangkan pantulan polarisasi silau tersebut adalah...",
        "correct": "Filter Circular Polarizer (CPL), yang dapat diputar sudutnya untuk memblokir gelombang pantulan cahaya terpolarisasi dari permukaan air dan kaca non-logam sehingga objek di baliknya terlihat jernih transparan.",
        "distractors": [
            "Filter Neutral Density (ND 1000) pekat, yang hanya menggelapkan seluruh bidang gambar secara merata tanpa mempengaruhi pantulan silau.",
            "Filter Ultraviolet (UV) bening biasa, yang hanya berfungsi sebagai kaca pelindung fisik lensa dari goresan debu kasar.",
            "Filter Star 8-Point Cross, yang mengubah setiap titik pantulan cahaya menjadi kilauan bintang delapan arah yang menyilaukan mata.",
            "Filter Infrared (IR), yang memblokir seluruh spektrum cahaya tampak dan hanya merekam pantulan panas radiasi daun pohon."
        ],
        "formula": {
            "title": "POLARISASI CAHAYA & SUDUT BREWSTER (FILTER CPL)",
            "latex": "\\theta_B = \\arctan(n) \\implies \\text{CPL Filter Rotates } \\theta_{\\text{pol}} \\implies \\text{Glare Reflection Suppressed by } 99\\%",
            "legend": "• Glare Permukaan Non-Logam: Bersifat terpolarisasi linear sebagian<br>• Filter CPL: Memiliki kisi polarisasi putar yang menyeleksi orientasi gelombang foton<br>• Efek Sekunder: Meningkatkan saturasi warna biru langit dan dedaunan hijau"
        },
        "hints": {
            "concept": "Filter CPL (Circular Polarizer) khusus digunakan untuk menghilangkan pantulan pada permukaan kaca dan air serta memekatkan langit biru.",
            "execution": "Filter Circular Polarizer (CPL) memutar sudut polarisasi untuk menembus pantulan kaca/air."
        }
    },
    {
        "id": "tekd-sim-03",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Tipografi OpenType: Ligatur Standar vs Discretionary",
        "stem": "Dalam teks buku sastra berbahasa Inggris, huruf kecil 'f' dan 'i' yang berdampingan sering kali saling bertabrakan secara janggal di mana titik pada huruf 'i' menabrak ujung melengkung huruf 'f'. Fitur tipografi digital profesional yang secara cerdas menggabungkan dua karakter huruf bertabrakan tersebut menjadi satu glif sambung terpadu yang estetis adalah...",
        "correct": "Ligature (Standard Ligatures 'fi', 'fl'), yang meleburkan titik 'i' ke dalam kurva ujung atas huruf 'f' untuk meningkatkan keindahan aliran visual dan keterbacaan teks.",
        "distractors": [
            "Discretionary Hyphenation, yang memotong huruf 'f' menjadi tanda strip pemenggalan suku kata bahasa asing.",
            "All Caps Transformation, yang mengubah seluruh huruf 'fi' menjadi huruf kapital besar balok berukuran 36 pt.",
            "Vertical Baseline Shift, yang menaikkan huruf 'i' setinggi 5 sentimeter di atas huruf 'f'.",
            "Monospace Spacing, yang memisahkan huruf 'f' dan 'i' sejauh 10 spasi kosong menggunakan tombol spasi keyboard."
        ],
        "formula": {
            "title": "TIPOGRAFI OPEN_TYPE: STANDAR LIGATUR",
            "latex": "\\text{Karakter 'f'} + \\text{Karakter 'i'} \\xrightarrow{\\text{OpenType Ligature}} \\text{Glif Tunggal '\\fi' (Harmoni Sempurna)}",
            "legend": "• Standard Ligatures: fi, fl, ff, ffi, ffl (Mengatasi tabrakan fisik kait dan titik huruf)<br>• Discretionary Ligatures: st, ct (Dekoratif/historis)<br>• Legibility Benefit: Menghilangkan gangguan visual benturan titik i pada badan kait f"
        },
        "hints": {
            "concept": "Ligatur (ligature) adalah glif khusus yang menggabungkan dua huruf yang rawan bertabrakan seperti 'f' dan 'i' menjadi satu kesatuan glif 'fi'.",
            "execution": "Pilih Standard Ligatures ('fi', 'fl')."
        }
    },
    {
        "id": "tekd-sim-04",
        "materi": "DESAIN MEDIA & KEMASAN",
        "topic": "Standar Barcode EAN-13 & Quiet Zone",
        "stem": "Sebuah kemasan snack biskuit ditolak oleh sistem pemindai barcode otomatis di kasir supermarket modern karena sensor kasir berulang kali gagal membaca kode batang EAN-13 yang tercetak pada kemasan. Setelah diaudit oleh desainer kemasan, kesalahan fatal yang dilakukan desainer pada area barcode tersebut adalah...",
        "correct": "Menempatkan elemen ilustrasi grafik terlalu mepet dan tidak menyisakan ruang kosong putih di sisi kiri dan kanan batang barcode (melanggar batas minimal Quiet Zone sebesar 3.63 mm).",
        "distractors": [
            "Mencetak garis batang barcode menggunakan tinta hitam pekat di atas latar belakang kotak putih bersih.",
            "Menggunakan angka berjumlah 13 digit lengkap yang telah terdaftar secara legal di lembaga GS1 Indonesia.",
            "Meletakkan barcode di bagian panel belakang kemasan biskuit yang permukaannya rata tanpa kerutan.",
            "Mencetak barcode dengan orientasi tegak lurus searah dengan arah jalannya silinder mesin rotogravure."
        ],
        "formula": {
            "title": "STANDAR BARCODE GS1 EAN-13 PRE-PRESS",
            "latex": "\\text{Lebar Minimum Quiet Zone} \\ge 3.63\\,\\text{mm (Kiri)} \\land \\ge 2.31\\,\\text{mm (Kanan)} \\implies \\text{Scanner Error} = 0",
            "legend": "• Quiet Zone: Ruang kosong tanpa grafis di kedua sisi batas garis barcode<br>• Warna Kontras: Garis wajib gelap pekat (Black/Dark Blue) di atas latar terang (White/Yellow)<br>• Pantangan: Dilarang garis merah di atas putih (karena sensor pemindai menggunakan sinar laser merah)"
        },
        "hints": {
            "concept": "Sensor laser barcode kasir membutuhkan zona hening (Quiet Zone)—area kosong bersih di kiri dan kanan kode batang—untuk menandai awal dan akhir pembacaan.",
            "execution": "Mengabaikan batas Quiet Zone (margin putih kiri-kanan) membuat pemindai gagal membaca barcode."
        }
    },
    {
        "id": "tekd-sim-05",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Etika Generative AI & Hak Cipta Prompting",
        "stem": "Seorang desainer menggunakan model Generative AI untuk menghasilkan ilustrasi poster hanya dengan memasukkan prompt teks singkat: 'pemandangan kota cyberpunk gaya lukisan seniman X'. Desainer kemudian mendaftarkan hasil murni gambar keluaran AI tersebut ke Direktorat Jenderal Kekayaan Intelektual (DJKI) sebagai karya cipta pribadinya. Berdasarkan konsensus etika profesi desain dan perkembangan yurisprudensi hak cipta internasional, status pendaftaran tersebut adalah...",
        "correct": "Ditolak atau tidak memenuhi syarat hak cipta, karena karya yang dihasilkan murni oleh kecerdasan buatan tanpa campur tangan kreativitas manusia (human authorship) yang substansial tidak diakui sebagai subjek perlindungan hak cipta.",
        "distractors": [
            "Diterima secara penuh dan model kecerdasan buatan tersebut secara hukum dipenjara selama lima tahun di lembaga pemasyarakatan.",
            "Hak cipta diberikan 100% kepada perusahaan penyedia listrik yang menyalakan server komputer AI di luar negeri.",
            "Desainer otomatis diangkat menjadi menteri ekonomi kreatif karena berhasil mengetik kalimat prompt sepuluh kata.",
            "Pemerintah memberikan medali penghargaan emas atas penemuan teknologi lukisan manual tertua di dunia."
        ],
        "formula": {
            "title": "DOKTRIN HUMAN AUTHORSHIP HAK CIPTA",
            "latex": "\\text{Perlindungan Hak Cipta} \\iff \\text{Karya Memuat Kreativitas Nyata Manusia (Human Authorship} > 0)",
            "legend": "• Output Murni AI: Tidak memiliki subjek hukum pencipta manusia $\\implies$ Masuk domain publik<br>• Assisted AI: AI sebagai alat bantu teknis, tetapi desainer melakukan kurasi, komposisi, modifikasi substansial<br>• Etika: Wajib transparansi atribusi dan menghormati hak gaya seniman yang diprompt"
        },
        "hints": {
            "concept": "Hukum hak cipta internasional dan nasional mensyaratkan adanya 'kreativitas manusia' (Human Authorship). Output murni ketikan prompt AI tidak memiliki hak cipta.",
            "execution": "Karya murni AI tanpa kreativitas manusia yang substansial tidak diakui sebagai ciptaan yang dilindungi hak cipta."
        }
    },
    {
        "id": "tekd-sim-06",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Keseimbangan Asimetris vs Simetris Dinamis",
        "stem": "Dalam mendesain poster konser musik jazz kontemporer, seorang desainer menempatkan satu foto siluet pemain saksofon berukuran besar berwarna gelap di area kanan bawah kanvas. Di area kiri atas yang luas, ia hanya menempatkan beberapa baris tipografi judul berukuran sedang dengan warna kuning cerah dan ruang negatif yang lapang. Komposisi ini tetap terasa stabil dan memikat secara visual karena menerapkan...",
        "correct": "Keseimbangan Asimetris (Asymmetrical Balance), di mana bobot visual objek besar di satu sisi diimbangi oleh intensitas warna cerah dan daya tarik tipografi di sisi lain tanpa pencerminan bentuk identik.",
        "distractors": [
            "Keseimbangan Simetris Formal, di mana sisi kiri dan sisi kanan kanvas merupakan cerminan bayangan kembar identik 100 persen.",
            "Keseimbangan Radial, di mana seluruh elemen berputar memancar keluar dari satu titik pusat roda lingkaran.",
            "Komposisi Acak Tanpa Prinsip, di mana elemen desain disebarkan secara sembarangan tanpa memikirkan bobot visual.",
            "Nirmana Trimatra Kinetik, di mana kanvas kertas berputar 360 derajat di dinding pameran menggunakan motor dinamo listrik."
        ],
        "formula": {
            "title": "PRINSIP KESEIMBANGAN ASIMETRIS (VISUAL WEIGHT)",
            "latex": "\\sum (\\text{Visual Weight} \\times \\text{Distance})_{\\text{Kiri}} = \\sum (\\text{Visual Weight} \\times \\text{Distance})_{\\text{Kanan}}",
            "legend": "• Bobot Visual (Visual Weight): Dipengaruhi oleh ukuran, kegelapan warna, saturasi, dan kontras<br>• Asimetris: Dinamis, modern, tidak kaku, memancing eksplorasi visual mata<br>• Simetris: Formal, stabil, agung, terkesan statis/tradisional"
        },
        "hints": {
            "concept": "Keseimbangan asimetris menyeimbangkan elemen yang berbeda ukuran/bentuk melalui perbedaan warna, kontras, atau posisi tuas visual (optical lever).",
            "execution": "Objek besar gelap diimbangi warna cerah dan tipografi di sisi lain merupakan Keseimbangan Asimetris."
        }
    },
    {
        "id": "tekd-sim-07",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Kalibrasi Monitor Desain Hardware Calibration (Colorimeter / Spyder)",
        "stem": "Sebuah agensi branding sering mengalami perselisihan dengan klien karena warna desain kemasan yang disetujui di monitor laptop desainer terlihat sangat berbeda jauh (kemilau biru pucat) ketika dibuka di layar klien dan dicetak di percetakan. Langkah standardisasi studio DKV yang paling tepat dan profesional untuk menjamin konsistensi penilaian warna visual adalah...",
        "correct": "Melakukan kalibrasi perangkat keras (Hardware Calibration) secara berkala pada monitor grafis IPS dengan alat Colorimeter/Spektrofotometer eksternal untuk mengunci titik putih D65 (6500K), Gamma 2.2, dan kecerahan $120\\,\\text{cd/m}^2$.",
        "distractors": [
            "Menyalakan mode hemat daya baterai dan mematikan lampu monitor hingga tingkat kecerahan nol persen.",
            "Mengganti kaca meja kerja desainer dengan marmer hitam agar bayangan keyboard tidak memantul ke layar.",
            "Menyetel kecerahan monitor ke tingkat maksimal 1000 nits dan memilih profil warna bioskop 'Vivid Dynamic'.",
            "Mengharuskan klien membeli laptop dengan merk dan tahun pembuatan yang sama persis dengan milik desainer."
        ],
        "formula": {
            "title": "STANDAR KALIBRASI MONITOR GRAFIS (ISO 3664 / 12646)",
            "latex": "\\text{Target Kalibrasi}: \\quad T_{\\text{White Point}} = 6500\\,\\text{K (D65)}, \\quad \\gamma = 2.2, \\quad L = 100-120\\,\\text{cd/m}^2, \\quad \\Delta E < 1.5",
            "legend": "• Colorimeter Hardware: Mengukur emisi spektrum warna fisik layar secara objektif<br>• ICC Profile Display: Memetakan deviasi monitor ke kartu grafis (LUT kalibrasi)<br>• Konsistensi: Menghilangkan bias visual mata manusia yang mudah beradaptasi dengan pencahayaan ruangan"
        },
        "hints": {
            "concept": "Mata manusia mudah tertipu cahaya ruangan. Solusi mutlak untuk studio desain adalah kalibrasi berkala menggunakan alat ukur fisik (colorimeter/spectrophotometer).",
            "execution": "Hardware calibration monitor ke standar D65, Gamma 2.2, dan $120\\,\\text{cd/m}^2$ menggunakan colorimeter eksternal."
        }
    },
    {
        "id": "tekd-sim-08",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Ergonomi Postur Duduk: Sudut 90 Derajat & Sandaran Lumbal",
        "stem": "Berdasarkan standar ergonomi K3LH perkantoran industri kreatif untuk operator komputer grafis yang bekerja selama 8 jam sehari, penataan kursi kerja dan postur tubuh yang benar untuk mencegah kelainan tulang belakang (Low Back Pain) adalah...",
        "correct": "Ketinggian kursi diatur agar telapak kaki menapak rata di lantai dengan sudut lutut 90 derajat, siku lengan bertumpu sejajar meja dengan sudut 90 derajat, serta sandaran kursi menopang kurva lekukan pinggang bawah (lumbar support).",
        "distractors": [
            "Kursi diatur setinggi mungkin hingga kedua kaki menggantung bebas di udara dan punggung membungkuk ke depan menempel meja.",
            "Bekerja sambil berbaring telentang di lantai tanpa bantal penyangga kepala selama 8 jam nonstop.",
            "Mengunci posisi lutut pada sudut 180 derajat lurus ke atas dan memegang mouse menggunakan kedua ibu jari kaki.",
            "Mencondongkan leher ke depan sejauh 15 sentimeter dengan pandangan mata menengadah ke langit-langit atap ruangan."
        ],
        "formula": {
            "title": "POSTUR KERJA KOMPUTER ERGONOMIS (OSHA / KEMENKES)",
            "latex": "\\theta_{\\text{lutut}} \\approx 90^\\circ, \\quad \\theta_{\\text{siku}} \\approx 90^\\circ, \\quad \\theta_{\\text{pinggul}} \\approx 90-100^\\circ, \\quad \\text{Jarak Monitor} = 50-70\\,\\text{cm}",
            "legend": "• Lumbar Support: Menjaga kurva lordosis alami tulang belakang bawah<br>• Sudut Pandang Layar: $15-20^\\circ$ di bawah garis lurus horizontal mata (mencegah nyeri leher)<br>• Kaki Menapak: Mencegah penyumbatan aliran darah pada pembuluh vena paha bawah"
        },
        "hints": {
            "concept": "Prinsip postur ergonomis komputer: Aturan 90 derajat (lutut, siku, pinggul), kaki menapak lantai, dan lumbar support menyangga pinggang.",
            "execution": "Kaki menapak rata (lutut 90°), siku 90°, dan sandaran menopang pinggang (lumbar support)."
        }
    },
    {
        "id": "tekd-sim-09",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Bracketing & High Dynamic Range (HDR) Fotografi Arsitektur",
        "stem": "Seorang fotografer arsitektur memotret ruang tamu vila mewah dengan dinding kaca besar yang menghadap langsung ke arah matahari sore yang sangat terik. Foto tunggal selalu menghasilkan ruangan tamu yang gelap gulita atau pemandangan luar jendela yang putih silau terbakar. Teknik pemotretan profesional yang paling tepat untuk mengatasi masalah kontras ekstrem tersebut adalah...",
        "correct": "Exposure Bracketing (mengambil minimal 3 foto berturut-turut pada tripod dengan eksposur underexposed, normal, dan overexposed), lalu menggabungkannya melalui teknik High Dynamic Range (HDR) blending.",
        "distractors": [
            "Menaikkan nilai ISO kamera ke 51.200 dan memotret sambil berlari cepat mengelilingi ruangan tanpa tripod.",
            "Menutup seluruh jendela kaca vila dengan cat pilox semprot berwarna hitam legam agar tidak ada cahaya luar yang masuk.",
            "Memotret menggunakan lampu kilat (flash) bodi internal kamera yang diarahkan tegak lurus langsung ke kaca jendela.",
            "Mengganti lensa kamera dengan lensa teropong bintang berjarak fokus 1000 milimeter."
        ],
        "formula": {
            "title": "TEKNIK EXPOSURE BRACKETING & HDR",
            "latex": "\\text{Dynamic Range Scene} > \\text{Dynamic Range Sensor} \\implies \\text{Merge}(\\text{EV}_{-2}, \\text{EV}_0, \\text{EV}_{+2}) \\xrightarrow{\\text{Tone Map}} \\text{HDR Output}",
            "legend": "• $EV_{-2}$ (Underexposed): Menyelamatkan detail terik matahari dan awan di luar jendela<br>• $EV_0$ (Normal): Menangkap midtone ruangan secara seimbang<br>• $EV_{+2}$ (Overexposed): Menyelamatkan detail bayangan gelap furnitur interior"
        },
        "hints": {
            "concept": "Ketika kontras ruangan melampaui kemampuan sensor, fotografer mengambil multiple exposure (bracketing: gelap, sedang, terang) lalu menggabungkannya menjadi foto HDR.",
            "execution": "Exposure bracketing (under, normal, over) digabung dengan teknik HDR blending."
        }
    },
    {
        "id": "tekd-sim-10",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Pelanggaran Merek: Praktik 'Passing Off'",
        "stem": "Sebuah warung kopi lokal membuat logo lingkaran hijau dengan tipografi melingkar dan gambar siluet putri duyung berekor dua yang nyaris identik dengan waralaba kopi global ternama, kemudian memasang plang toko tersebut di tepi jalan raya utama untuk mengecoh konsumen agar mengira gerainya adalah cabang resmi waralaba tersebut. Praktik persaingan curang dalam hukum HAKI ini dikenal sebagai...",
        "correct": "Passing Off, yaitu tindakan memperdagangkan barang atau jasa dengan cara sedemikian rupa sehingga menyesatkan masyarakat umum bahwa barang atau jasa tersebut berkaitan, berafiliasi, atau merupakan produk dari pemilik reputasi merek terkenal lain.",
        "distractors": [
            "Reverse Engineering, yaitu proses membongkar mesin pembuat kopi untuk mempelajari susunan roda gigi mekanik di dalamnya.",
            "Fair Use Doktrin, yaitu penggunaan sebagian kecil kutipan berita untuk tujuan ulasan kritis dan pendidikan nirlaba.",
            "Public Domain Dedication, yaitu pelepasan sukarela hak cipta oleh pemilik karya kepada seluruh masyarakat dunia.",
            "Trade Secret Licensing, yaitu perjanjian rahasia resep pembuatan sirup karamel antara dua pemilik perkebunan tebu."
        ],
        "formula": {
            "title": "DOKTRIN TORT OF PASSING OFF (PERSAINGAN CURANG)",
            "latex": "\\text{Passing Off Elements} = \\text{Goodwill (Reputasi Korban)} + \\text{Misrepresentation (Penyesatan)} + \\text{Damage (Kerugian)}",
            "legend": "• Goodwill: Nama besar dan reputasi yang telah melekat di benak konsumen<br>• Misrepresentation: Desain visual mengecoh publik seolah ada keterikatan resmi<br>• Konsekuensi: Tuntutan ganti rugi perdata dan penutupan paksa gerai toko"
        },
        "hints": {
            "concept": "Passing Off adalah penyesatan dagang di mana pelaku meniru identitas merek terkenal agar konsumen mengira produknya adalah barang dari pemilik merek terkenal tersebut.",
            "execution": "Praktik mengecoh konsumen seolah gerai tersebut adalah cabang resmi merek terkenal disebut Passing Off."
        }
    },
    {
        "id": "tekd-sim-11",
        "materi": "DESAIN MEDIA & KEMASAN",
        "topic": "Sertifikasi Food Grade Kemasan (BPA Free & Regulasi BPOM)",
        "stem": "Dalam perancangan kemasan fleksibel untuk produk bubur bayi instan yang akan diseduh dengan air mendidih bersuhu $100^\\circ\\text{C}$, desainer kemasan wajib memastikan bahwa material kemasan memiliki sertifikasi Food Grade dan bebas dari zat berbahaya seperti Bisphenol A (BPA) serta ftalat. Bahaya utama yang dicegah dari regulasi kemasan pangan ini adalah...",
        "correct": "Migrasi zat kimia beracun dari lapisan kemasan plastik ke dalam produk makanan bayi akibat pemanasan suhu tinggi, yang dapat memicu gangguan sistem endokrin dan kesehatan anak.",
        "distractors": [
            "Perubahan warna tinta barcode kemasan dari warna hitam menjadi warna pelangi menyala saat terkena air panas.",
            "Peningkatan berat jenis bubur bayi menjadi seberat logam timbal saat terkena paparan cahaya lampu dapur.",
            "Timbulnya gelombang suara ultrasonik dari dalam kantong kemasan yang dapat mengagetkan orang tua bayi.",
            "Larangan dari kementerian perdagangan untuk mencantumkan gambar foto bayi pada label kemasan makanan."
        ],
        "formula": {
            "title": "STANDAR REGULASI KEMASAN PANGAN (BPOM NO. 20/2019)",
            "latex": "\\text{Zat Migrasi Kimia} \\le \\text{Batas Maksimal Migrasi Spesifik (SML)} \\implies \\text{Sertifikasi Food Grade Aman}",
            "legend": "• Bahan Rekomendasi: Aluminium Foil barrier tinggi berlapis LLDPE Food Grade<br>• Pantangan: Plastik daur ulang non-food grade dan pelarut tinta cetak non-kering<br>• BPA Free: Mencegah kerusakan hormon perkembangan kelenjar tiroid pada bayi"
        },
        "hints": {
            "concept": "Standar kemasan Food Grade (bebas BPA) bertujuan mencegah migrasi zat kimia beracun dari wadah plastik ke dalam makanan saat terkena suhu panas.",
            "execution": "Mencegah migrasi zat kimia beracun ke dalam makanan akibat panas tinggi."
        }
    },
    {
        "id": "tekd-sim-12",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Sistem Grid Modular vs Grid Kolom Editorial",
        "stem": "Dalam perancangan katalog pameran seni rupa kontemporer setebal 200 halaman yang memuat ratusan karya lukisan berbagai ukuran dimensi, desainer menyusun tata letak menggunakan Grid Modular (modular grid) yang membagi halaman ke dalam matriks kolom vertikal dan modul baris horizontal (spatial zones). Keunggulan fungsional utama sistem grid modular dibanding grid kolom sederhana adalah...",
        "correct": "Memberikan fleksibilitas tinggi dalam mengelompokkan beberapa modul bidang menjadi zona spasial multifungsi untuk memuat berbagai proporsi foto karya seni secara harmonis dan konsisten.",
        "distractors": [
            "Memaksa seluruh foto lukisan dicetak dalam bentuk lingkaran bulat kecil berdiameter 1 sentimeter tanpa variasi.",
            "Menghapus seluruh batas margin halaman sehingga teks dan gambar dicetak menabrak tepi kertas buku.",
            "Membuat file digital katalog otomatis terkunci dan tidak dapat diubah oleh desainer grafis mana pun.",
            "Mengurangi biaya pembelian kertas buku di pabrik kertas sebesar sembilan puluh persen secara instan."
        ],
        "formula": {
            "title": "ARSITEKTUR GRID EDITORIAL: MODULAR GRID",
            "latex": "\\text{Bidang Kanvas} = \\sum_{i=1}^m \\sum_{j=1}^n \\text{Modul}_{i,j} + \\text{Gutters} \\implies \\text{Zona Spasial Dinamis}",
            "legend": "• Modul: Unit ruang terkecil persilangan kolom dan baris horisontal (flowlines)<br>• Spatial Zones: Gabungan beberapa modul untuk gambar horizontal, vertikal, atau teks narasi<br>• Manfaat: Struktur disiplin ketat sekaligus sangat fleksibel untuk layout multi-halaman kompleks"
        },
        "hints": {
            "concept": "Grid modular membagi halaman menjadi matriks kotak-kotak (modul) yang dapat digabungkan menjadi berbagai ukuran bidang (spatial zones) yang fleksibel.",
            "execution": "Memberikan fleksibilitas pengelompokan modul menjadi zona spasial harmonis untuk berbagai variasi ukuran gambar."
        }
    },
    {
        "id": "tekd-sim-13",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Teknologi Computer-to-Plate (CtP) vs Computer-to-Film (CtF)",
        "stem": "Industri percetakan modern telah sepenuhnya meninggalkan teknologi Computer-to-Film (CtF) dan beralih menggunakan sistem Computer-to-Plate (CtP) thermal laser. Keuntungan teknis paling mutlak dari penggunaan teknologi CtP dalam pembuatan plat cetak offset adalah...",
        "correct": "Menghilangkan tahapan pembuatan film perantara dan penyinaran manual vakum, sehingga registrasi warna jauh lebih presisi, titik raster halftone lebih tajam (generasi pertama), serta meniadakan limbah kimia perak nitrat pemroses film.",
        "distractors": [
            "Memungkinkan mesin cetak bekerja tanpa menggunakan plat aluminium dan tanpa menggunakan tinta cetak sama sekali.",
            "Membuat kertas majalah yang dicetak otomatis berubah menjadi layar sentuh digital interaktif.",
            "Menaikkan suhu ruangan percetakan hingga 500 derajat Celsius untuk mengeringkan pakaian karyawan pabrik.",
            "Mengharuskan operator mencetak seluruh halaman majalah menggunakan kuas lukis cat air satu per satu."
        ],
        "formula": {
            "title": "EVOLUSI PRE-PRESS: CTF VS CTP",
            "latex": "\\text{File Digital} \\xrightarrow{\\text{CtP Laser}} \\text{Plat Aluminium} \\quad (\\text{Bypass Film, } \\Delta \\text{Dot Loss} \\approx 0)",
            "legend": "• CtF Lama: File $\\rightarrow$ Film Negatif $\\rightarrow$ Kontak Vakum Lampu UV $\\rightarrow$ Plat (Banyak deviasi mikro & limbah kimia)<br>• CtP Modern: Laser infra-merah langsung mengekspos lapisan polimer plat logam<br>• Keuntungan: Registrasi 4 warna super akurat, waktu setup mesin cetak (makeready) berkurang 50%"
        },
        "hints": {
            "concept": "CtP (Computer to Plate) mengekspos laser langsung ke plat aluminium tanpa melalui film plastik. Hasilnya jauh lebih presisi, tajam, cepat, dan ramah lingkungan.",
            "execution": "Menghilangkan film perantara, registrasi warna lebih presisi, dan meniadakan limbah kimia perak nitrat."
        }
    },
    {
        "id": "tekd-sim-14",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Tipologi Lisensi Font Komersial: Desktop vs Webfont vs App",
        "stem": "Sebuah perusahaan rintisan (startup) membeli lisensi font seharga $50 untuk 1 pengguna komputer (Desktop License) bagi desainer grafisnya. Tanpa membaca berkas perjanjian lisensi pengguna akhir (EULA), tim IT langsung mengunggah file font `.otf` tersebut ke server web publik agar digunakan pada situs web perusahaan dan disematkan (embedded) ke dalam aplikasi Android mereka. Konsekuensi pelanggaran lisensi tersebut adalah...",
        "correct": "Melanggar ketentuan EULA font, karena Desktop License hanya mengizinkan penggunaan instalasi lokal pada perangkat komputer untuk media statis/cetak; penggunaan pada situs web memerlukan Webfont License (berdasarkan pageviews) dan aplikasi memerlukan App/Server Embedding License.",
        "distractors": [
            "Tidak terjadi pelanggaran apa pun karena setiap font yang telah dibeli sekali otomatis menjadi hak milik mutlak pembeli selamanya tanpa batasan media.",
            "Sistem operasi Android akan secara otomatis menghapus seluruh nomor kontak telepon pengguna yang mengunduh aplikasi startup tersebut.",
            "Desainer font berhak menyita seluruh gedung kantor startup dan menjualnya di balai lelang negara.",
            "Startup hanya perlu mengirimkan sepucuk surat permohonan maaf tanpa ada kewajiban hukum membayar lisensi tambahan."
        ],
        "formula": {
            "title": "TAKSONOMI LISENSI TIPOGRAFI DIGITAL (EULA)",
            "latex": "\\text{Font EULA} = \\begin{cases} \\text{Desktop: Instalasi PC, desain cetak/raster statis} \\\\ \\text{Webfont: Self-hosting web via @font-face (Trafik Pageviews)} \\\\ \\text{App/Server: Binary embedding kode APK/iOS / SaaS dynamic} \\end{cases}",
            "legend": "• Pelanggaran Hak Cipta Font: Rentan dituntut audit hak cipta oleh font foundry internasional dengan denda ganti rugi besar<br>• Solusi Legal: Beli paket lisensi multi-platform lengkap atau beralih ke font open-source berlisensi SIL Open Font License (OFL)"
        },
        "hints": {
            "concept": "Lisensi font Desktop berbeda dengan Webfont atau App Embedding. Desktop hanya untuk instalasi lokal komputer. Menyematkan ke server web/aplikasi tanpa lisensi tepat melanggar EULA hak cipta.",
            "execution": "Desktop License hanya untuk instalasi lokal komputer; web dan aplikasi butuh Webfont dan App/Embedding License khusus."
        }
    },
    {
        "id": "tekd-sim-15",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Irama Visual (Rhythm) & Pengulangan Bergradasi",
        "stem": "Dalam merancang sampul buku panduan festival tari kontemporer, desainer menata serangkaian bentuk garis kurva berulang yang semakin ke kanan semakin membesar ukurannya, semakin rapat jarak spasinya, dan semakin pekat kepekatan warnanya. Kesan visual yang berhasil dibangkitkan oleh prinsip penataan bentuk rupa tersebut adalah...",
        "correct": "Irama Bergradasi (Progressive Rhythm), yang menciptakan ilusi dinamika pergerakan visual yang semakin cepat, bertenaga, dan memuncak (klimaks visual) melintasi kanvas.",
        "distractors": [
            "Irama Statis Monoton, di mana bentuk dan jarak selalu diulang dalam bentuk yang sama kaku tanpa ada perubahan apa pun.",
            "Kekacauan Visual (Visual Chaos), di mana tidak ditemukan pola hubungan logis antarelemen rupa.",
            "Tekstur Taktil Nyata, di mana kertas sampul buku otomatis bergetar mengeluarkan nada musik saat dibuka pembaca.",
            "Proporsi Kerdil, di mana seluruh elemen visual menyusut hingga tidak dapat dilihat tanpa mikroskop optik."
        ],
        "formula": {
            "title": "VARIASI IRAMA NIRMANA (RHYTHM)",
            "latex": "\\text{Rhythm} = f(\\Delta \\text{Ukuran}, \\Delta \\text{Jarak}, \\Delta \\text{Tone}) \\implies \\text{Irama Progresif (Dinamika Klimaks)}",
            "legend": "• Regular/Statis: Ukuran & interval sama $\\implies$ Tenang, teratur, stabil<br>• Alternating: Pola selang-seling (A-B-A-B) $\\implies$ Berirama terduga<br>• Progressive: Perubahan bertahap secara matematis $\\implies$ Dinamis, melaju kencang menuju titik klimaks"
        },
        "hints": {
            "concept": "Pengulangan dengan perubahan bertahap (makin besar, makin rapat, makin pekat) disebut Progressive Rhythm (Irama Bergradasi).",
            "execution": "Menciptakan kesan pergerakan yang semakin memuncak (Progressive Rhythm)."
        }
    },
    {
        "id": "tekd-sim-16",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Fotografi Makro & Kedalaman Bidang Sempit Ekstrem (Focus Stacking)",
        "stem": "Seorang fotografer mengabadikan mata serangga kecil menggunakan lensa makro 100mm dengan rasio perbesaran 1:1 dan bukaan f/2.8. Hasil foto memperlihatkan bahwa hanya ujung satu helai bulu mata serangga yang fokus, sedangkan sisa bagian mata lainnya kabur buram karena kedalaman bidang (DoF) makro yang sangat tipis (kurang dari 1 mm). Teknik digital fotografi mutakhir untuk membuat seluruh kepala serangga fokus tajam dari depan hingga belakang adalah...",
        "correct": "Focus Stacking, yaitu memotret puluhan foto berturut-turut dengan menggeser titik fokus milimeter demi milimeter menggunakan rel makro, lalu menggabungkan seluruh area tajamnya menggunakan software pengolah gambar.",
        "distractors": [
            "Menutup diafragma lensa hingga f/128 dan menaikkan ISO kamera hingga noise butiran merusak foto.",
            "Menyorot mata serangga menggunakan lampu laser pemotong besi berkekuatan 10.000 Watt dari jarak 1 cm.",
            "Memotong lensa kamera menjadi tiga bagian lalu menempelkannya kembali menggunakan lem kayu.",
            "Mengguncang kamera sekuat tenaga saat tombol rana ditekan untuk menyebarkan titik fokus secara acak."
        ],
        "formula": {
            "title": "TEKNIK FOCUS STACKING FOTOGRAFI MAKRO",
            "latex": "\\text{DoF}_{\\text{makro}} \\approx \\frac{2 N c (m+1)}{m^2} \\xrightarrow{m=1} < 0.5\\,\\text{mm} \\implies \\text{Solusi: Merge } \\sum_{i=1}^n \\text{Sharp Slices}_i",
            "legend": "• Pada perbesaran tinggi ($m=1:1$), DoF anjlok ekstrem bahkan pada f/8<br>• Difraksi Optis: Menutup diafragma terlalu kecil ($> f/16$) membuat foto menjadi buram akibat difraksi cahaya<br>• Focus Stacking: Menghasilkan ketajaman ultra-panjang tanpa degradasi difraksi"
        },
        "hints": {
            "concept": "Lensa makro perbesaran tinggi memiliki DoF sangat tipis. Focus Stacking memotret irisan-irisan fokus berbeda lalu menggabungkan bagian tajamnya.",
            "execution": "Teknik Focus Stacking dengan rel makro untuk menggabungkan irisan area tajam."
        }
    },
    {
        "id": "tekd-sim-17",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Pembuatan File Finishing Khusus (Emboss & Die-Cut)",
        "stem": "Dalam mempersiapkan dokumen artwork kartu nama eksekutif yang memuat finishing Emboss (timbul fisik ke atas) dan Die-Cut (potongan sudut melengkung), cara penyiapan layer artwork yang benar pada file Adobe Illustrator sebelum dikirim ke percetakan adalah...",
        "correct": "Memisahkan artwork cetak CMYK, jalur pisau Die-Cut, dan area Emboss ke dalam layer-layer terpisah yang berbeda, dengan garis Die-Cut dan bentuk Emboss menggunakan Spot Color khusus bertipe Technical/No-Print.",
        "distractors": [
            "Menggabungkan seluruh elemen cetak, garis pisau potong, dan emboss menjadi satu gambar bitmap JPEG 72 PPI tunggal yang di-flatten.",
            "Mencetak garis pisau potong menggunakan tinta warna kuning terang transparan di atas teks nama kartu nama.",
            "Menggambar garis potong menggunakan pulpen tinta basah langsung di atas layar monitor komputer percetakan.",
            "Menghapus seluruh teks kartu nama dan membiarkan lembaran kanvas kosong melompong tanpa data vektor."
        ],
        "formula": {
            "title": "MANAJEMEN LAYER PRE-PRESS FINISHING KHUSUS",
            "latex": "\\text{Master File} = \\text{Layer CMYK (Grafis)} + \\text{Layer Die-Cut (Spot 'Cutter')} + \\text{Layer Emboss (Spot 'Emboss')}",
            "legend": "• Spot Color Teknis: Diberi nama 'DieCut' atau 'Emboss' dengan atribut non-printing / overprint<br>• Layer Terpisah: Memudahkan operator membuat plat film pisau pond baja dan klise tembaga emboss<br>• Posisi Pas: Seluruh layer berada pada koordinat $X, Y$ registrasi yang identik"
        },
        "hints": {
            "concept": "Finishing khusus (pond pisau potong, emboss, hotprint) wajib diletakkan pada layer terpisah dengan warna Spot Color teknis tersendiri dan registrasi presisi.",
            "execution": "Pisahkan ke dalam layer tersendiri (CMYK, Die-Cut, Emboss) menggunakan Spot Color khusus."
        }
    },
    {
        "id": "tekd-sim-18",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Psikologi Warna Korporat & Asosiasi Budaya",
        "stem": "Sebuah rumah sakit swasta dan penyedia asuransi kesehatan ingin merancang identitas korporat baru yang menanamkan rasa ketenangan, kebersihan, kepercayaan ilmiah, dan rasa aman bagi pasien. Berdasarkan psikologi warna komunikasi visual dan konteks medis modern, kombinasi palet warna primer yang paling efektif adalah...",
        "correct": "Biru laut (membangun kepercayaan, kestabilan, profesionalisme) dipadukan dengan Hijau toska/sage (kesehatan, pemulihan, ketenangan jiwa) dan Putih steril (kebersihan higienis).",
        "distractors": [
            "Merah darah menyala dikombinasikan dengan Kuning peringatan dan Hitam pekat pejal untuk memicu kepanikan darurat pasien.",
            "Cokelat tanah berlumpur gelap dipadukan dengan Abu-abu kusam untuk memberikan kesan gedung kuno yang lapuk.",
            "Jingga menyengat dipadukan dengan Merah muda fluorescent untuk membangkitkan nafsu makan makanan pedas.",
            "Ungu gelap pekat dipadukan dengan Hitam arang untuk membangun suasana ritual pemakaman mistis abad pertengahan."
        ],
        "formula": {
            "title": "PSIKOLOGI WARNA BIDANG KESEHATAN (HEALTHCARE VISUALS)",
            "latex": "\\text{Healthcare Trust} = \\text{Blue (Kepercayaan/Sains)} + \\text{Teal/Green (Penyembuhan/Alami)} + \\text{White (Higienis/Steril)}",
            "legend": "• Biru: Menurunkan detak jantung, meredakan kecemasan, asosiasi kredibilitas dokter<br>• Hijau/Teal: Menyejukkan mata, regenerasi sel, pemulihan kesehatan<br>• Merah pada Medis: Dihindari pada brand identity utama karena diasosiasikan dengan darah, bahaya, dan ambulans darurat"
        },
        "hints": {
            "concept": "Sektor medis membutuhkan warna yang menenangkan dan membangun kepercayaan: Biru (kredibilitas/sains), Hijau/Toska (penyembuhan), dan Putih (steril/bersih).",
            "execution": "Biru laut, hijau toska, dan putih steril adalah palet baku industri kesehatan."
        }
    },
    {
        "id": "tekd-sim-19",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Bahaya Kebakaran Studio Percetakan & Alat APAR",
        "stem": "Di ruang penyimpanan bahan kimia dan kertas studio percetakan DKV, terdapat tumpukan pelarut organik thinner, tinta cair, dan ribuan rim kertas yang sangat mudah tersulut api. Berdasarkan klasifikasi kebakaran (NFPA) dan K3LH, jenis Alat Pemadam Api Ringan (APAR) yang paling tepat disediakan di ruangan tersebut untuk memadamkan kebakaran Kelas A (benda padat kertas) dan Kelas B (cairan pelarut mudah terbakar) adalah...",
        "correct": "APAR Serbuk Kimia Kering (Dry Chemical Powder ABC) atau APAR Busa (Foam AFFF), yang mampu menyelimuti permukaan bahan terbakar dan memutus pasokan oksigen.",
        "distractors": [
            "Menyemprotkan bensin murni menggunakan selang air bertekanan tinggi ke arah kobaran api.",
            "APAR berisi air murni bertekanan tinggi yang disemprotkan langsung ke dalam wadah thinner yang sedang mendidih terbakar.",
            "Melemparkan tumpukan kertas koran kering tambahan ke atas api agar kobaran api kelelahan membakar kertas.",
            "Meniup api menggunakan kipas angin meja bertenaga baterai kecil dari jarak lima sentimeter."
        ],
        "formula": {
            "title": "KLASIFIKASI KEBAKARAN & APAR (PERMENAKER NO. 04/1980)",
            "latex": "\\text{Bahan Cetak} \\implies \\text{Kelas A (Kertas/Karton)} + \\text{Kelas B (Pelarut/Tinta)} \\implies \\text{APAR Powder ABC / Busa AFFF}",
            "legend": "• Kelas A: Bahan padat mudah terbakar (kertas, kayu, kain)<br>• Kelas B: Cairan/gas mudah menyala (thinner, alkohol, bensin, minyak)<br>• Bahaya Air pada Kelas B: Air membuat pelarut mengapung dan menyebarkan kobaran api ke mana-mana"
        },
        "hints": {
            "concept": "Percetakan memiliki risiko kebakaran kelas A (kertas) dan kelas B (cairan pelarut kimia). Menggunakan air pada pelarut kimia berbahaya. APAR Dry Powder ABC atau Busa Foam adalah standar yang tepat.",
            "execution": "APAR Dry Chemical Powder ABC atau Busa Foam AFFF."
        }
    },
    {
        "id": "tekd-sim-20",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Perhitungan Ukuran Teks Signage Lingkungan (Viewing Distance)",
        "stem": "Sebuah rumah sakit membutuhkan papan petunjuk arah gawat darurat (signage wayfinding) yang harus dapat dibaca dengan jelas oleh pengemudi ambulans dari jarak pandang 30 meter. Berdasarkan aturan praktis tipografi lingkungan (Environmental Graphic Design: 1 inci tinggi huruf per 30 kaki / sekitar 10 meter jarak pandang), berapakah tinggi huruf kapital minimal yang harus dirancang oleh desainer?",
        "correct": "Minimal 3 inci (sekitar 7.6 cm atau 75-80 mm), agar pesan teks terbaca secara instan dan akurat dari jarak 30 meter dalam kondisi kritis.",
        "distractors": [
            "Cukup 5 milimeter (ukuran font teks buku 14 pt), karena mata manusia memiliki kemampuan melihat mikro dari jarak satu kilometer.",
            "Minimal 5 meter per huruf, sehingga papan petunjuk arah membutuhkan tiang baja setinggi menara pemancar radio.",
            "Setengah milimeter, yang dicetak menggunakan tinta rahasia yang hanya terlihat melalui kacamata khusus inframerah.",
            "Tinggi huruf tidak berpengaruh sama sekali terhadap jarak baca asalkan huruf diwarnai hijau neon."
        ],
        "formula": {
            "title": "RUMUS KETERBACAAN SIGNAGE TIPOGRAFI LINGKUNGAN",
            "latex": "H_{\\text{huruf}} = \\frac{D_{\\text{viewing}}}{10\\,\\text{meter}} \\times 2.54\\,\\text{cm} \\implies \\frac{30}{10} \\times 2.54 = 7.62\\,\\text{cm} \\ (\\approx 3\\,\\text{inci})",
            "legend": "• Rasio Standar EGD: Setiap 1 inci ($2.54$ cm) tinggi huruf kapital efektif untuk jarak baca $30$ kaki ($9-10$ meter)<br>• Pada 30 meter: Butuh minimal $3\\,\\text{inci} \\approx 7.6\\,\\text{cm}$<br>• Kecepatan Bergerak: Jika dibaca saat kendaraan melaju, tinggi huruf ditambah faktor pengali $1.5\\times$"
        },
        "hints": {
            "concept": "Kaidah Environmental Graphic Design: setiap 10 meter jarak baca membutuhkan tinggi huruf minimal 1 inci (~2.5 cm).",
            "execution": "Untuk jarak 30 meter: $3 \\times 2.54\\text{ cm} \\approx 7.6\\text{ cm}$ (3 inci)."
        }
    },
    {
        "id": "tekd-sim-21",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Gestalt Law of Continuity & Alur Pandang (Eye Flow)",
        "stem": "Dalam perancangan infografis linimasa sejarah kemerdekaan Indonesia pada poster lipat panjang, desainer menggambar pita merah putih bergelombang yang meliuk-liuk dari sudut kiri atas halaman, melewati kolom-kolom teks, hingga berakhir di sudut kanan bawah. Pandangan mata pembaca secara alami terdorong mengikuti alur liukan pita tersebut dari awal hingga akhir. Prinsip persepsi Gestalt yang mendasari desain tersebut adalah...",
        "correct": "Law of Continuity (Prinsip Kelangsungan Garis), di mana mata manusia cenderung mengikuti jalur, garis, atau kurva yang mengalir berkesinambungan secara mulus dibandingkan memutus perhatian pada sudut tajam.",
        "distractors": [
            "Law of Proximity, di mana teks tahun kemerdekaan dianggap bersaudara kandung dengan gambar bendera negara lain.",
            "Law of Similarity, di mana seluruh foto tokoh pejuang kemerdekaan wajib diedit memiliki bentuk kumis yang sama persis.",
            "Law of Symmetry, di mana separuh poster harus dicelupkan ke dalam air raksa agar memantulkan bayangan cermin.",
            "Law of Synchrony, di mana kertas poster mengeluarkan aroma wangi bunga melati secara serempak di setiap jam kantor."
        ],
        "formula": {
            "title": "GESTALT LAW OF CONTINUITY (KONTINUITAS)",
            "latex": "\\frac{d\\mathbf{C}}{ds} \\text{ Mulus / Smooth} \\implies \\text{Mata Memprioritaskan Alur Kontinu Melintasi Interupsi Elemen}",
            "legend": "• Continuity: Elemen yang tersusun dalam garis/kurva dilihat sebagai entitas yang saling terhubung erat<br>• Visual Path: Digunakan desainer untuk menuntun alur baca (eye tracking navigation)<br>• Aplikasi: Garis linimasa (timeline), grafik tren pasar, panah penunjuk arah"
        },
        "hints": {
            "concept": "Law of Continuity menyatakan bahwa mata terdorong mengikuti garis atau alur kurva yang mengalir berkesinambungan tanpa henti.",
            "execution": "Liukan pita penuntun urutan membaca menerapkan Law of Continuity."
        }
    },
    {
        "id": "tekd-sim-22",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Preflight Audit File Cetak (Checklist Pra-Cetak)",
        "stem": "Sebelum mengirimkan file PDF kemasan produk pangan ke industri percetakan rotogravure komersial, seorang staf prepress menjalankan proses otomatis 'Preflight Inspection'. Masalah kritis yang terdeteksi dan wajib segera diperbaiki oleh desainer pada tahapan preflight tersebut adalah...",
        "correct": "Ditemukan gambar foto beresolusi rendah (72 PPI), model warna masih ada yang berformat RGB, font teks belum di-convert to curves (outline) atau belum ter-embed, dan tidak adanya lebihan garis bleed 3 mm.",
        "distractors": [
            "Ditemukan bahwa teks deskripsi produk ditulis menggunakan bahasa Indonesia baku yang sesuai dengan pedoman umum ejaan bahasa Indonesia.",
            "Ditemukan bahwa berat file dokumen PDF berada di atas 5 Kilobyte sehingga melanggar aturan ukuran file pesan instan WhatsApp.",
            "Ditemukan bahwa nama desainer yang tercantum di file tidak memiliki gelar bangsawan kerajaan eropa kuno.",
            "Ditemukan bahwa warna plat cetak hitam menggunakan tinta hitam padahal seharusnya menggunakan air teh manis."
        ],
        "formula": {
            "title": "CHECKLIST PREFLIGHT INSPECTION ISO PRE-PRESS",
            "latex": "\\text{Pass Preflight} \\iff (\\text{DPI} \\ge 300) \\land (\\text{Color} = \\text{CMYK/Spot}) \\land (\\text{Bleed} \\ge 3\\,\\text{mm}) \\land (\\text{Fonts Embedded})",
            "legend": "• Preflight: Verifikasi otomatis kelaikan file sebelum proses pembuatan plat cetak (RIP)<br>• Resolusi Rendah: Foto tampak buram/pecah pada cetakan fisik<br>• RGB Tercampur: Pergeseran warna parah saat konversi otomatis di mesin"
        },
        "hints": {
            "concept": "Preflight memeriksa kesalahan teknis cetak: resolusi < 300 DPI, gambar masih RGB, font belum embedded/outline, dan bleed kurang.",
            "execution": "Checklist preflight mencakup DPI rendah, profil RGB, font missing/belum outline, dan ketiadaan bleed."
        }
    },
    {
        "id": "tekd-sim-23",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Penggunaan Grey Card 18% untuk Kalibrasi Eksposur",
        "stem": "Saat memotret subjek berkulit gelap yang mengenakan jas tuksedo hitam pekat di depan latar belakang panggung hitam pekat, lightmeter internal kamera DSLR (reflective light meter) tertipu dan menghasilkan foto yang overexposed abu-abu pudar (jas hitam menjadi abu-abu kusam). Alat bantu standar fotografi yang wajib diletakkan di depan subjek untuk mengunci eksposur dan white balance yang akurat adalah...",
        "correct": "Grey Card dengan standar pantulan 18% netral (18% Reflectance Middle Gray), yang menjadi acuan standar kalibrasi lightmeter kamera untuk membaca pencahayaan netral tanpa terpengaruh warna gelap objek.",
        "distractors": [
            "Kaca cermin rias pengantin yang memantulkan sinar lampu studio 100% tegak lurus ke arah sensor kamera.",
            "Kain spanduk merah darah selebar 10 meter untuk menaikkan saturasi warna kulit model secara digital.",
            "Lensa pembesar kacamata baca plus lima yang ditempelkan di depan lampu flash bodi kamera.",
            "Batu bata merah yang dicelupkan ke dalam ember cat putih minyak sebelum pemotretan dimulai."
        ],
        "formula": {
            "title": "STANDAR LIGHTMETER INTERNAL: 18% NEUTRAL GRAY",
            "latex": "\\text{Kamera Reflective Meter Mengasumsikan Seluruh Dunia} = 18\\% \\text{ Gray} \\implies \\text{Objek Serba Hitam Diterangkan Menjadi Abu-abu}",
            "legend": "• Kelemahan Kamera: Menganggap adegan serba hitam/putih sebagai abu-abu 18% $\\implies$ salah ukur<br>• 18% Grey Card: Menghasilkan pembacaan eksposur akurat mutlak (zone V dalam Ansel Adams Zone System)<br>• Dual Fungsi: Sekaligus untuk penetapan White Balance manual di studio"
        },
        "hints": {
            "concept": "Lightmeter kamera selalu berasumsi dunia adalah abu-abu 18%. Objek serba hitam diterangkan jadi abu-abu. Grey Card 18% mengunci eksposur yang tepat.",
            "execution": "Kartu abu-abu netral 18% (18% Grey Card) adalah standar kalibrasi eksposur akurat."
        }
    },
    {
        "id": "tekd-sim-24",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Hak Cipta: Ciptaan yang Tidak Dilindungi (Pasal 65 UU Hak Cipta)",
        "stem": "Seorang desainer grafis diminta membuat ulang buku kumpulan Undang-Undang Perlindungan Konsumen dan naskah pidato kenegaraan presiden republik Indonesia dengan layout tipografi editorial yang sangat indah. Apakah teks undang-undang dan pidato resmi pejabat lembaga negara tersebut dapat diklaim hak ciptanya oleh seseorang dan dilarang untuk diperbanyak secara hukum?",
        "correct": "Tidak dapat, karena berdasarkan Pasal 65 UU No. 28 Tahun 2014, hasil karya berupa peraturan perundang-undangan, pidato kenegaraan, putusan pengadilan, dan kitab suci tidak memiliki hak cipta dan merupakan milik publik terbuka.",
        "distractors": [
            "Dapat diklaim hak ciptanya oleh siapapun yang mencetak naskah tersebut untuk pertama kali di atas kertas folio bergaris.",
            "Hak cipta undang-undang otomatis dimiliki oleh pemilik perusahaan percetakan swasta terbesar di ibu kota.",
            "Seluruh teks undang-undang menjadi hak cipta eksklusif milik keluarga mantan presiden selama 1000 tahun.",
            "Dapat diklaim oleh desainer grafis yang membuat tata letak huruf dan nomor halaman buku kumpulan hukum tersebut."
        ],
        "formula": {
            "title": "KARYA YANG TIDAK MEMILIKI HAK CIPTA (PASAL 65 UU 28/2014)",
            "latex": "\\text{Domain Publik Statis} = \\{ \\text{UU}, \\text{Pidato Pejabat}, \\text{Putusan Hakim}, \\text{Kitab Suci} \\} \\implies \\text{Hak Cipta} = \\emptyset",
            "legend": "• Akses Bebas: Menjamin keterbukaan informasi hukum dan demokrasi bagi seluruh rakyat<br>• Catatan DKV: Tata letak (layout) dan ilustrasi cover baru dapat dilindungi hak ciptanya, tetapi isi teks UU tetap publik<br>• Siapapun bebas mencetak ulang, mengutip, dan mendistribusikannya"
        },
        "hints": {
            "concept": "Pasal 65 UU Hak Cipta menegaskan bahwa peraturan perundang-undangan, pidato resmi pejabat negara, dan putusan pengadilan tidak memiliki hak cipta.",
            "execution": "Peraturan perundang-undangan dan pidato kenegaraan tidak memiliki hak cipta (milik publik)."
        }
    },
    {
        "id": "tekd-sim-25",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Prinsip Desain Inklusif & Keterbacaan Warna Buta Warna (Color Blindness)",
        "stem": "Dalam mendesain infografis peta jalur kereta commuter line perkotaan metropolitan, desainer menyadari bahwa sekitar 8% populasi pria menderita buta warna merah-hijau (Deuteranopia / Protanopia). Pendekatan desain komunikasi visual inklusif yang paling tepat diterapkan agar peta jalur kereta tetap dapat dipahami dengan mudah oleh penumpang dengan buta warna adalah...",
        "correct": "Menerapkan pengkodean ganda (Dual Coding / Multi-modal Cueing), di mana selain membedakan jalur dengan warna kontras aman, setiap jalur juga dibedakan dengan bentuk garis unik (putus-putus, garis ganda, solid) dan penambahan simbol ikon atau huruf kode jalur spesifik.",
        "distractors": [
            "Hanya menggunakan satu warna merah terang untuk seluruh 20 rute jalur kereta tanpa memberikan nomor atau nama stasiun.",
            "Menghapus seluruh peta visual stasiun dan mewajibkan penumpang menghafal seluruh nama stasiun sebelum masuk ke peron.",
            "Melarang penderita buta warna menaiki angkutan umum kereta commuter line sesuai instruksi dinas perhubungan.",
            "Mengganti seluruh peta cetak stasiun dengan rekaman suara sirene kebakaran yang berbunyi terus-menerus."
        ],
        "formula": {
            "title": "PRINSIP DESAIN INKLUSIF: DUAL CODING THEORY",
            "latex": "\\text{Aksesibilitas Navigasi} = \\text{Warna (Color Token)} + \\text{Bentuk/Pola (Pattern Cue)} + \\text{Ikonografi/Teks (Semantic Label)}",
            "legend": "• Jangan Mengandalkan Warna Saja: Prinsip fundamental WCAG Success Criterion 1.4.1 (Use of Color)<br>• Deuteranopia/Protanopia: Merah dan hijau tampak sebagai nuansa cokelat kekuningan yang serupa<br>• Garis Bertekstur & Simbol: Memastikan informasi 100% tersampaikan tanpa hambatan fisiologis mata"
        },
        "hints": {
            "concept": "Desain inklusif melarang penggunaan warna sebagai satu-satunya indikator (WCAG 1.4.1). Wajib menambahkan pola garis unik, ikon, atau label teks (dual coding).",
            "execution": "Dual coding: bedakan dengan pola garis (putus-putus, solid), ikon, dan simbol huruf di samping warna."
        }
    },

    # 5 COMPLEX MULTI-SELECT ITEMS (tekd-sim-26 to tekd-sim-30)
    {
        "id": "tekd-sim-26",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Faktor Kritis Pre-Press Cetak Offset Separasi 4 Warna",
        "type": "multi",
        "stem": "Seorang desainer grafis sedang mengaudit master file katalog majalah seni sebelum dikirim ke mesin cetak Computer-to-Plate (CtP) percetakan offset. Manakah dari pernyataan-pernyataan teknis berikut yang BENAR terkait persiapan file siap cetak (print-ready artwork)? (Pilihlah lebih dari satu jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Seluruh gambar bitmap yang digunakan wajib memiliki resolusi efektif minimal 300 DPI pada skala ukuran cetak aktual 1:1."},
            {"key": "B", "text": "Area lebihan batas potong (bleed) minimal 3 mm wajib ditambahkan pada setiap tepi halaman yang memuat gambar latar hingga ke pinggir kertas."},
            {"key": "C", "text": "Teks berukuran kecil (8 pt) berwarna hitam wajib diatur dengan perintah Knockout dan menggunakan campuran formula empat tinta C=100%, M=100%, Y=100%, K=100%."},
            {"key": "D", "text": "Seluruh font tipografi yang digunakan wajib disematkan (embedded) atau dikonversi menjadi kurva vektor (Create Outlines / Convert to Curves) untuk mencegah substitusi font sistem."},
            {"key": "E", "text": "Ruang warna dokumen wajib diatur pada mode sRGB 8-bit untuk memastikan mesin cetak menghasilkan saturasi warna neon menyala."}
        ],
        "correctKeys": ["A", "B", "D"],
        "formula": {
            "title": "CHECKLIST EMAS ARTIKEL SIAP CETAK (PRE-PRESS ISO 12647)",
            "latex": "\\text{Valid Print File} = (\\text{DPI} \\ge 300) \\land (\\text{Bleed} \\ge 3\\,\\text{mm}) \\land (\\text{Fonts Outlined}) \\land (\\text{Text } K=100 \\text{ Overprint})",
            "legend": "• A Benar: 300 DPI standar wajib ketajaman raster offset<br>• B Benar: Bleed 3 mm mencegah celah putih pergeseran pisau guillotine<br>• C Salah: Teks hitam wajib K=100% tunggal dengan OVERPRINT (bukan Rich Black 400% Knockout)<br>• D Benar: Outline font mencegah 'missing font error' di komputer percetakan<br>• E Salah: Cetak wajib CMYK/Spot, bukan sRGB layar"
        },
        "hints": {
            "concept": "Syarat mutlak cetak offset komersial: 300 DPI, Bleed 3 mm, dan Outline font. Teks kecil tidak boleh 4 warna dan ruang warna harus CMYK.",
            "execution": "Pernyataan A, B, dan D adalah kaidah baku pre-press yang benar."
        }
    },
    {
        "id": "tekd-sim-27",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Prinsip Anatomi & Keterbacaan Tipografi",
        "type": "multi",
        "stem": "Dalam perancangan tipografi antarmuka digital dan media cetak, pemahaman mendalam tentang anatomi huruf sangat krusial. Manakah dari pernyataan-pernyataan berikut yang TEPAT mengenai fungsi dan anatomi tipografi? (Pilihlah lebih dari satu jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Kerning mengatur jarak ruang optis secara individual antara sepasang karakter huruf spesifik, sedangkan tracking mengatur spasi seragam pada seluruh kata atau kalimat."},
            {"key": "B", "text": "Font dengan proporsi x-height yang tinggi (seperti Helvetica) umumnya memiliki tingkat keterbacaan (readability) yang lebih baik pada ukuran kecil di layar digital dibandingkan font dengan x-height rendah."},
            {"key": "C", "text": "Leading adalah jarak vertikal yang diukur dari garis atas huruf kapital (cap height) ke garis bawah huruf berkaki (descender line)."},
            {"key": "D", "text": "Huruf berkaki (Serif) memiliki kait ujung yang membantu memandu mata pembaca bergerak horizontal sepanjang baris teks panjang di media cetak."},
            {"key": "E", "text": "Discretionary ligatures adalah fitur yang mewajibkan seluruh huruf vokal dihapus dari penulisan judul majalah."}
        ],
        "correctKeys": ["A", "B", "D"],
        "formula": {
            "title": "ANATOMI TIPOGRAFI DIGITAL",
            "latex": "\\text{Leading} = \\text{Jarak Baseline ke Baseline}; \\quad \\text{Kerning} \\ne \\text{Tracking}; \\quad \\text{Large X-Height} \\implies \\text{Better Legibility}",
            "legend": "• A Benar: Definisi tepat kerning (pasangan) vs tracking (blok global)<br>• B Benar: X-height besar membuat badan huruf kecil terlihat lebih jelas di layar kecil<br>• C Salah: Leading diukur dari Baseline ke Baseline baris berikutnya (bukan dari cap height ke descender)<br>• D Benar: Serif berfungsi sebagai pemandu kontinuitas horizontal membaca buku<br>• E Salah: Ligatur menggabungkan karakter bertabrakan seperti fi/fl, bukan menghapus vokal"
        },
        "hints": {
            "concept": "Kerning = pasangan huruf; X-height besar = mudah dibaca di ukuran kecil; Serif = memandu mata di media cetak. Leading diukur dari baseline ke baseline.",
            "execution": "Pernyataan A, B, dan D tepat secara kaidah anatomi tipografi."
        }
    },
    {
        "id": "tekd-sim-28",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Segitiga Eksposur & Karakteristik Lensa",
        "type": "multi",
        "stem": "Seorang fotografer studio sedang melakukan pengaturan kamera untuk pemotretan produk kosmetik mewah. Manakah dari prinsip-prinsip segitiga eksposur dan optika fotografi berikut yang BENAR? (Pilihlah lebih dari satu jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Membuka diafragma lensa ke angka f-stop kecil (misal f/1.8 atau f/2.8) akan menghasilkan kedalaman bidang yang sempit (shallow depth of field) dengan latar belakang bokeh halus."},
            {"key": "B", "text": "Menaikkan nilai ISO kamera dari 100 menjadi 12.800 akan meningkatkan sensitivitas sensor terhadap cahaya sekaligus memicu munculnya noise butiran digital dan penurunan dynamic range."},
            {"key": "C", "text": "Menggunakan shutter speed lambat (misal 1/2 detik) tanpa tripod akan membekukan gerakan cipratan air secara tajam tanpa buram."},
            {"key": "D", "text": "Hukum Kuadrat Terbalik (Inverse Square Law) menyatakan bahwa melipatgandakan jarak lampu studio dari 2 meter menjadi 4 meter akan memangkas intensitas cahaya menjadi 1/4 (turun 2 stop penuh)."},
            {"key": "E", "text": "Lensa sudut lebar (wide-angle 16mm) dari jarak 30 cm sangat direkomendasikan untuk potret wajah close-up karena memberikan bentuk hidung yang paling kecil dan ramping."}
        ],
        "correctKeys": ["A", "B", "D"],
        "formula": {
            "title": "PRINSIP INTI SEGITIGA EKSPOSUR & OPTIKA",
            "latex": "\\text{Eksposur} = f(A, S, \\text{ISO}); \\quad \\text{Bukaan Besar (f/1.8)} \\implies \\text{DoF Sempit}; \\quad I \\propto \\frac{1}{d^2}",
            "legend": "• A Benar: Bukaan besar (f kecil) menghasilkan DoF sempit / bokeh<br>• B Benar: ISO tinggi menguatkan sinyal analog sensor beserta noise butirannya<br>• C Salah: Shutter lambat 1/2 detik memicu motion blur hebat dan goyangan tangan (camera shake)<br>• D Benar: Jarak mundur 2x lipat memotong intensitas cahaya menjadi 1/4 (2 stop)<br>• E Salah: Lensa ultra-wide jarak dekat memicu distorsi barel yang membuat hidung tampak bengkak besar"
        },
        "hints": {
            "concept": "Bukaan diafragma besar (f-stop kecil) = bokeh (A benar). ISO tinggi = banyak noise (B benar). Inverse Square Law jarak 2x = cahaya 1/4 (D benar).",
            "execution": "Pernyataan A, B, dan D valid secara fisika dan optika kamera."
        }
    },
    {
        "id": "tekd-sim-29",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Hukum Kekayaan Intelektual Terkait DKV di Indonesia",
        "type": "multi",
        "stem": "Dalam dunia profesional Desain Komunikasi Visual di Indonesia, pemahaman regulasi Hak Atas Kekayaan Intelektual (HAKI) sangat penting untuk melindungi karya dan menghindari gugatan hukum. Manakah dari pernyataan hukum berikut yang BENAR? (Pilihlah lebih dari satu jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Hak cipta atas karya seni rupa, ilustrasi, dan desain grafis timbul secara otomatis berdasarkan prinsip deklaratif seketika setelah karya tersebut diwujudkan dalam bentuk nyata tanpa keharusan pendaftaran."},
            {"key": "B", "text": "Perlindungan hukum merek dagang di Indonesia menganut sistem 'First to File', di mana pihak yang pertama kali mengajukan pendaftaran secara sah ke DJKI yang berhak atas merek tersebut."},
            {"key": "C", "text": "Hak moral pencipta dapat dialihkan atau dijual secara permanen kepada perusahaan pembeli hak cipta bersamaan dengan pengalihan hak ekonomi."},
            {"key": "D", "text": "Bentuk fisik kemasan 3 dimensi yang memiliki nilai estetika dan kebaruan dapat didaftarkan sebagai Desain Industri dengan masa perlindungan 10 tahun."},
            {"key": "E", "text": "Setiap karya visual yang diunggah ke internet secara otomatis menjadi Domain Publik bebas royalti yang boleh digunakan oleh siapa pun untuk tujuan komersial tanpa izin."}
        ],
        "correctKeys": ["A", "B", "D"],
        "formula": {
            "title": "REGULASI HAKI INDONESIA (UU 28/2014, UU 20/2016, UU 31/2000)",
            "latex": "\\text{Hak Cipta: Deklaratif (Otomatis)}, \\quad \\text{Merek: Konstitutif (First to File)}, \\quad \\text{Hak Moral: Abadi/Non-transferable}",
            "legend": "• A Benar: Hak cipta otomatis lahir saat diwujudkan dalam bentuk konkret<br>• B Benar: Hak merek di Indonesia didasarkan pada siapa pendaftar pertama (First to File)<br>• C Salah: Hak moral tidak dapat dialihkan atau dijual (Pasal 5 ayat 2 UU Hak Cipta)<br>• D Benar: Kemasan 3D estetik dilindungi di bawah rezim Desain Industri selama 10 tahun<br>• E Salah: Mengunggah ke internet tidak menghapus hak cipta penciptanya"
        },
        "hints": {
            "concept": "Hak cipta menganut asas deklaratif otomatis; Merek menganut sistem First to File; Kemasan 3D dilindungi Desain Industri. Hak moral abadi tidak bisa dijual.",
            "execution": "Pernyataan A, B, dan D sesuai dengan peraturan perundang-undangan HAKI di Indonesia."
        }
    },
    {
        "id": "tekd-sim-30",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Hukum Persepsi Gestalt dalam Komposisi Visual",
        "type": "multi",
        "stem": "Prinsip psikologi persepsi visual Gestalt merupakan fondasi fundamental dalam tata letak, branding, dan UI/UX modern. Manakah dari pernyataan-pernyataan berikut yang TEPAT mengenai implementasi prinsip Gestalt? (Pilihlah lebih dari satu jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Law of Proximity menyatakan bahwa objek-objek grafis yang letaknya saling berdekatan akan dipersepsikan oleh otak sebagai satu kelompok kesatuan yang saling berkaitan."},
            {"key": "B", "text": "Law of Closure menjelaskan mengapa mata manusia dapat mengenali figur panda utuh pada logo WWF meskipun garis luar penutup tubuhnya tidak digambar secara lengkap."},
            {"key": "C", "text": "Law of Similarity menyatakan bahwa elemen-elemen yang memiliki kesamaan bentuk, warna, atau ukuran akan dipersepsikan memiliki makna atau fungsi yang serupa."},
            {"key": "D", "text": "Figure-Ground Organization menyatakan bahwa mata manusia hanya dapat melihat objek warna merah terang dan selalu menolak objek yang berwarna biru."},
            {"key": "E", "text": "Law of Common Fate menyatakan bahwa seluruh objek yang diam di sudut kanvas wajib dicetak menggunakan tinta foil emas panas."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "PRINSIP PSIKOLOGI VISUAL GESTALT",
            "latex": "\\text{Gestalt}: \\text{The Whole is Other than the Sum of its Parts} \\implies \\text{Proximity} \\cup \\text{Closure} \\cup \\text{Similarity}",
            "legend": "• A Benar: Proximity = kedekatan spasial membentuk kesatuan kelompok (fondasi form design UI)<br>• B Benar: Closure = kecenderungan mental menutup celah bentuk yang terputus (logo WWF)<br>• C Benar: Similarity = elemen berkarakter visual sama dianggap satu kategori fungsi<br>• D Salah: Figure-Ground membedakan figur fokus vs latar belakang, bukan menolak warna biru<br>• E Salah: Common Fate berlaku pada elemen yang bergerak kinetik searah, bukan objek diam bertinta emas"
        },
        "hints": {
            "concept": "Proximity (kedekatan), Closure (penutupan celah), dan Similarity (kesamaan bentuk/warna) adalah prinsip utama Gestalt yang didefinisikan dengan benar.",
            "execution": "Pernyataan A, B, dan C benar secara teori psikologi Gestalt."
        }
    },

    # 5 MATRIX BENAR-SALAH (B/S) ITEMS (tekd-sim-31 to tekd-sim-35)
    {
        "id": "tekd-sim-31",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Matriks Fakta Model Warna & Reproduksi Grafis",
        "type": "matrix",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan teknis mengenai model warna dan reproduksi grafis pre-press berikut ini:",
        "statements": [
            {
                "id": "s1",
                "text": "Model warna RGB merupakan sistem warna aditif (additive color) berbasis perpaduan cahaya yang digunakan pada perangkat layar digital monitor dan smartphone.",
                "correct": True
            },
            {
                "id": "s2",
                "text": "Gamut warna ruang warna CMYK jauh lebih luas daripada Adobe RGB 1998 sehingga seluruh warna neon layar digital dapat dicetak persis dengan tinta offset standar.",
                "correct": False
            },
            {
                "id": "s3",
                "text": "Teknik Rich Black (misal C=40, M=30, Y=30, K=100) menghasilkan warna hitam yang lebih pekat dan mewah pada bidang blok latar luas dibandingkan hanya menggunakan K=100% tunggal.",
                "correct": True
            },
            {
                "id": "s4",
                "text": "Warna Spot Color (seperti Pantone Matching System - PMS) merupakan tinta khusus hasil campuran formula pabrik yang menjamin konsistensi warna brand di berbagai percetakan.",
                "correct": True
            }
        ],
        "formula": {
            "title": "MATRIKS MODEL WARNA FISIK & DIGITAL",
            "latex": "\\text{Gamut}(\\text{CMYK}) \\subset \\text{Gamut}(\\text{sRGB}) \\subset \\text{Gamut}(\\text{Adobe RGB})",
            "legend": "• s1 Benar: RGB aditif dari emisi cahaya layar monitor<br>• s2 Salah: Gamut CMYK justru lebih sempit (warna neon out-of-gamut)<br>• s3 Benar: Rich black memberi kepekatan optis tinggi pada blok besar<br>• s4 Benar: Pantone adalah tinta khusus premixed standar industri"
        },
        "hints": {
            "concept": "RGB adalah aditif layar (Benar). Gamut CMYK lebih sempit dari RGB, bukan lebih luas (Salah). Rich black menghasilkan hitam pekat pada bidang luas (Benar). Pantone adalah spot color baku pabrik (Benar).",
            "execution": "s1: Benar, s2: Salah, s3: Benar, s4: Benar."
        }
    },
    {
        "id": "tekd-sim-32",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Matriks Klasifikasi & Istilah Tipografi",
        "type": "matrix",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan mengenai klasifikasi dan penerapan tipografi berikut ini:",
        "statements": [
            {
                "id": "s1",
                "text": "Font berkaki tebal dan kaku menyerupai balok persegi panjang (seperti Rockwell atau Clarendon) diklasifikasikan ke dalam kelompok Slab Serif (Egyptian).",
                "correct": True
            },
            {
                "id": "s2",
                "text": "X-Height diukur dari puncak huruf kapital tertinggi hingga batas terbawah huruf berkaki descender seperti 'p' dan 'q'.",
                "correct": False
            },
            {
                "id": "s3",
                "text": "Fenomena 'Rivers of White' terjadi ketika teks justified pada kolom sempit memunculkan celah-celah spasi putih vertikal yang mengganggu alur membaca.",
                "correct": True
            },
            {
                "id": "s4",
                "text": "Tabular Figures menghasilkan angka dengan lebar karakter yang bervariasi mengikuti bentuk masing-masing angka sehingga sangat cocok untuk penulisan judul headline puisi.",
                "correct": False
            }
        ],
        "formula": {
            "title": "MATRIKS TAKSONOMI TIPOGRAFI",
            "latex": "\\text{Slab Serif} = \\text{Thick Block Serifs}; \\quad \\text{X-Height} = \\text{Baseline to Meanline (x, o, a)}; \\quad \\text{Tabular} = \\text{Monospaced Width}",
            "legend": "• s1 Benar: Slab Serif bercirikan kait tebal geometris (Rockwell, Clarendon)<br>• s2 Salah: X-height hanya mengukur tinggi huruf kecil tanpa ascender/descender (dari baseline ke meanline)<br>• s3 Benar: Rivers of white adalah cacat tipografi khas paragraf justified di kolom sempit<br>• s4 Salah: Tabular figures berlebar sama rata (monospaced) untuk tabel keuangan, bukan variatif untuk puisi"
        },
        "hints": {
            "concept": "Slab serif berkaki balok tebal (Benar). X-height hanya tinggi badan huruf kecil x, bukan dari kapital ke descender (Salah). Rivers of white = celah putih justified (Benar). Tabular figures berjarak sama rata untuk tabel, bukan variasi bervariasi (Salah).",
            "execution": "s1: Benar, s2: Salah, s3: Benar, s4: Salah."
        }
    },
    {
        "id": "tekd-sim-33",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Matriks Pengaturan Kamera & Teori Pencahayaan",
        "type": "matrix",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan mengenai teknis fotografi dan pencahayaan studio berikut ini:",
        "statements": [
            {
                "id": "s1",
                "text": "Semakin besar angka f-number (misal f/22), semakin sempit bukaan bilah diafragma lensa dan semakin lebar kedalaman bidang (Depth of Field) yang dihasilkan.",
                "correct": True
            },
            {
                "id": "s2",
                "text": "Pengaturan Shutter Speed 1/2000 detik dirancang khusus untuk menciptakan efek garis jejak gerak lampu mobil (light trails) yang panjang dan kabur pada malam hari.",
                "correct": False
            },
            {
                "id": "s3",
                "text": "Lampu Back Light pada skema Three-Point Lighting berfungsi memisahkan siluet model dari latar belakang dengan menghasilkan garis kilau cahaya (rim light) di kepala dan bahu.",
                "correct": True
            },
            {
                "id": "s4",
                "text": "Suhu warna lampu lilin dan lampu pijar rumah tangga (Tungsten) bernilai sekitar 3200 Kelvin dan menghasilkan spektrum warna bernuansa kuning-jingga hangat.",
                "correct": True
            }
        ],
        "formula": {
            "title": "MATRIKS HUBUNGAN PARAMETER FOTOGRAFI",
            "latex": "\\text{Angka } f\\text{-stop} \\uparrow \\implies \\text{Bukaan } \\downarrow \\implies \\text{DoF} \\uparrow; \\quad T_{\\text{Tungsten}} \\approx 3200\\,\\text{K} \\implies \\text{Warm Light}",
            "legend": "• s1 Benar: f/22 bukaan sangat kecil, menghasilkan DoF tajam luas dari depan sampai belakang<br>• s2 Salah: 1/2000s untuk membekukan gerakan cepat (freeze action); light trails butuh shutter lambat (1-10 detik)<br>• s3 Benar: Back light menciptakan rim light pemisah objek dari background<br>• s4 Benar: Tungsten bersuhu sekitar 3200K dengan rona hangat"
        },
        "hints": {
            "concept": "f/22 = bukaan kecil, DoF lebar (Benar). 1/2000 detik membekukan aksi cepat, bukan light trail berbayang (Salah). Back light = rim light pemisah latar (Benar). Tungsten = 3200K rona jingga/kuning (Benar).",
            "execution": "s1: Benar, s2: Salah, s3: Benar, s4: Benar."
        }
    },
    {
        "id": "tekd-sim-34",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Matriks Perlindungan Kekayaan Intelektual DKV",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan terkait etika profesi desainer dan perlindungan hukum HAKI di Indonesia berikut ini:",
        "statements": [
            {
                "id": "s1",
                "text": "Hak Cipta di Indonesia melindungi ide, gagasan murni, dan konsep abstrak yang masih ada di dalam pikiran desainer sebelum dituangkan ke dalam wujud nyata.",
                "correct": False
            },
            {
                "id": "s2",
                "text": "Karya yang berlisensi Creative Commons 'CC0' (Public Domain Dedication) dapat digunakan secara bebas untuk proyek komersial maupun non-komersial tanpa kewajiban mencantumkan nama pencipta.",
                "correct": True
            },
            {
                "id": "s3",
                "text": "Pendaftaran Merek Dagang di DJKI memberikan hak eksklusif perlindungan hukum selama 10 tahun dan dapat diperpanjang untuk jangka waktu yang sama secara terus-menerus.",
                "correct": True
            },
            {
                "id": "s4",
                "text": "Memodifikasi dan mengubah komposisi desain logo orang lain sebesar 20% otomatis menghilangkan segala bentuk tuntutan hukum plagiarisme dan pelanggaran hak cipta.",
                "correct": False
            }
        ],
        "formula": {
            "title": "MATRIKS PRINSIP HUKUM HAKI (UU HAK CIPTA & MEREK)",
            "latex": "\\text{Ide Murni} \\notin \\text{Objek Hak Cipta (Idea-Expression Dichotomy)}; \\quad \\text{Merek} = 10\\,\\text{Tahun (Renewable)}",
            "legend": "• s1 Salah: Hak cipta hanya melindungi EKSPRESI nyata karya, bukan ide/gagasan abstrak (Idea-Expression Dichotomy)<br>• s2 Benar: CC0 adalah pelepasan hak ke domain publik penuh tanpa syarat atribusi<br>• s3 Benar: Masa berlaku merek dagang adalah 10 tahun dan dapat diperpanjang tanpa batas masa<br>• s4 Salah: Mitos 'modifikasi 20%' tidak dikenal dalam hukum; jika ada substansi yang menjiplak tetap dianggap pelanggaran"
        },
        "hints": {
            "concept": "Hak cipta tidak melindungi ide murni, melainkan wujud nyata ciptaan (Salah). CC0 = public domain bebas atribusi (Benar). Perlindungan merek 10 tahun dan bisa diperpanjang (Benar). Aturan modifikasi 20% adalah mitos ilegal (Salah).",
            "execution": "s1: Salah, s2: Benar, s3: Benar, s4: Salah."
        }
    },
    {
        "id": "tekd-sim-35",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Matriks Keselamatan, Kesehatan Kerja & Lingkungan Hidup (K3LH)",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan mengenai standar K3LH dan ergonomi dalam aktivitas kerja studio DKV berikut ini:",
        "statements": [
            {
                "id": "s1",
                "text": "Aturan 20-20-20 menganjurkan agar setiap bekerja menatap monitor selama 20 menit, alihkan pandangan melihat objek berjarak minimal 20 kaki (sekitar 6 meter) selama minimal 20 detik untuk mengistirahatkan otot fokus mata.",
                "correct": True
            },
            {
                "id": "s2",
                "text": "Monitor komputer grafis sebaiknya diletakkan menghadap langsung membelakangi jendela kaca terbuka yang terpapar terik matahari tanpa tirai untuk menghemat pemakaian listrik lampu studio.",
                "correct": False
            },
            {
                "id": "s3",
                "text": "Sistem ventilasi hisap lokal (Local Exhaust Ventilation - LEV) wajib dipasang di ruang percetakan untuk menyedot uap beracun pelarut kimia dan tinta sebelum terhirup oleh sistem pernapasan pekerja.",
                "correct": True
            },
            {
                "id": "s4",
                "text": "Limbah cair pelarut kimia sisa pencucian silinder mesin cetak offset boleh dibuang langsung ke selokan air perumahan warga karena dapat menyuburkan lumut parit.",
                "correct": False
            }
        ],
        "formula": {
            "title": "MATRIKS STANDAR K3LH & ERGONOMI STUDIO DKV",
            "latex": "\\text{20-20-20 Rule} \\implies \\text{CVS Prevention}; \\quad \\text{Solvent} \\in \\text{Limbah B3} \\implies \\text{Dilarang Buang ke Drainase}",
            "legend": "• s1 Benar: 20-20-20 merelaksasi otot akomodasi mata siliaris<br>• s2 Salah: Membelakangi jendela terbuka memicu silau ekstrem (glare) dan hilangnya akurasi kontras warna layar<br>• s3 Benar: LEV menangkap uap kimia VOC di sumber penguapan mesin cetak<br>• s4 Salah: Pelarut cetak adalah limbah B3 beracun, dilarang keras dibuang ke selokan"
        },
        "hints": {
            "concept": "Aturan 20-20-20 cegah ketegangan mata (Benar). Monitor jangan membelakangi jendela karena silau glare (Salah). LEV hisap uap kimia berbahaya di sumbernya (Benar). Pelarut tinta adalah B3 dilarang dibuang ke parit umum (Salah).",
            "execution": "s1: Benar, s2: Salah, s3: Benar, s4: Salah."
        }
    }
]
