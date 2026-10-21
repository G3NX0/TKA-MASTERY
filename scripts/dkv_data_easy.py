# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Desain Komunikasi Visual (DKV / Rekayasa Desain SMK/MAK)
Dataset: Easy Practice (25 Authentic Questions, tekd-lat-e-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

DKV_EASY_ITEMS = [
    {
        "id": "tekd-lat-e-01",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Gestalt Figure-Ground & Negative Space",
        "stem": "Seorang desainer grafis merancang poster minimalis untuk pameran seni kontemporer. Di tengah kanvas putih, ia menempatkan siluet pohon hitam tunggal, di mana celah antara cabang-cabangnya secara visual membentuk siluet dua wajah manusia yang sedang berhadapan. Prinsip psikologi visual Gestalt yang dimanfaatkan dalam karya tersebut adalah...",
        "correct": "Figure-Ground Organization, di mana mata audiens secara dinamis membedakan objek utama (figure) dengan latar belakang ruang negatif (ground) yang membentuk persepsi ganda bermakna.",
        "distractors": [
            "Proximity (kedekatan spasial), di mana elemen-elemen grafis yang saling berdekatan selalu dikelompokkan oleh otak sebagai satu kesatuan unit fungsional yang homogen.",
            "Similarity (kesamaan bentuk), di mana elemen dengan warna dan tekstur identik dianggap memiliki fungsi yang setara dalam tata letak komposisi poster.",
            "Continuity (kelangsungan garis), di mana mata dipaksa mengikuti arah garis lurus dari sudut kiri bawah kanvas menuju sudut kanan atas secara konstan.",
            "Closure (penutupan bentuk), di mana ruang kosong secara otomatis diisi oleh otak untuk melengkapi bentuk geometris lingkaran yang terputus sebagian."
        ],
        "formula": {
            "title": "PRINSIP GESTALT FIGURE-GROUND",
            "latex": "\\text{Persepsi Visual} = \\text{Figure (Fokus)} \\iff \\text{Ground (Ruang Negatif)}",
            "legend": "• Figure: Objek dominan yang ditangkap mata<br>• Ground: Bidang latar/ruang sisa yang dapat membentuk siluet kedua<br>• Negative Space: Elemen aktif pembentuk makna ganda"
        },
        "hints": {
            "concept": "Figure-Ground menyatakan bahwa sistem visual manusia memisahkan bidang pandang menjadi figur utama dan latar belakang; desainer ulung memanfaatkan ilusi ini untuk menciptakan gambar ganda.",
            "execution": "Cabang pohon (figure hitam) dan celah putih (ground) bergantian ditangkap persepsi sebagai pohon dan wajah berhadapan."
        }
    },
    {
        "id": "tekd-lat-e-02",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Klasifikasi Font Serif vs Sans Serif",
        "stem": "Dalam proyek perancangan majalah sastra dan novel cetak setebal 400 halaman, tim desain memilih jenis huruf Georgia untuk teks paragraf utama (body text). Pertimbangan ergonomis visual yang paling tepat mendasari pemilihan font berkaki (Serif) untuk media cetak panjang adalah...",
        "correct": "Kaki kait (serif) membentuk garis horizontal maya pada dasar huruf yang memandu mata pembaca meluncur lancar dari kiri ke kanan sepanjang baris teks yang padat.",
        "distractors": [
            "Font serif menggunakan memori file digital yang jauh lebih kecil saat dikirim ke mesin cetak rotogravure.",
            "Bentuk font berkaki memberikan kesan visual yang sangat modern, futuristik, dan minimalis pada tampilan layar smartphone.",
            "Font serif memiliki ketebalan stroke yang seragam sehingga tidak memerlukan proses rasterisasi saat dicetak pada kertas koran.",
            "Kaki pada font serif berfungsi menyerap kelebihan tinta cair agar tidak meluber ke luar batas margin halaman."
        ],
        "formula": {
            "title": "ERGONOMI TIPOGRAFI CETAK",
            "latex": "\\text{Legibility} + \\text{Readability} \\implies \\text{Serif Guides Eye Flow on Print Media}",
            "legend": "• Serif: Kait/ekstensi ujung stroke penuntun horizontal eye tracking<br>• Sans Serif: Tanpa kait, optimal untuk layar resolusi rendah & signage<br>• Readability: Kenyamanan membaca blok teks panjang"
        },
        "hints": {
            "concept": "Serif pada tipografi cetak konvensional mempermudah kontinuitas visual (eye tracking) dengan menyatukan huruf-huruf menjadi kesatuan kata dan garis lurus horizontal.",
            "execution": "Cari jawaban yang menjelaskan keterbacaan (readability) berbasis garis pandu horizontal untuk mata pembaca majalah/buku."
        }
    },
    {
        "id": "tekd-lat-e-03",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Sistem Warna RGB vs CMYK",
        "stem": "Seorang desainer grafis pemula menyelesaikan poster promosi di Adobe Photoshop menggunakan ruang warna RGB dengan warna latar hijau neon menyala (#00FF00). Ketika dicetak menggunakan mesin cetak digital offset CMYK, hasil cetak berubah drastis menjadi hijau tua kusam. Penyebab utama penurunan saturasi warna tersebut adalah...",
        "correct": "Gamut warna ruang warna subtraktif CMYK lebih sempit daripada aditif RGB, sehingga warna hijau neon di luar gamut terpotong (clipped/out of gamut) dan dikonversi ke warna cetak terdekat yang lebih redup.",
        "distractors": [
            "Mesin cetak digital offset kehabisan pasokan tinta hitam (Key/Black) sehingga tidak mampu mengikat pigmen warna sekunder.",
            "Resolusi kanvas desain awal terlalu tinggi sehingga molekul tinta printer tidak mampu menembus serat kertas art paper.",
            "Desainer lupa menambahkan garis batas potong (bleed) sebesar 3 mm pada keempat sisi dokumen poster cetak.",
            "Penggunaan format file PNG membuat seluruh informasi lapisan warna (color layer) terhapus secara otomatis sebelum proses rasterisasi."
        ],
        "formula": {
            "title": "GAMUT WARNA RGB VS CMYK",
            "latex": "\\text{Gamut}(\\text{CMYK}) \\subset \\text{Gamut}(\\text{RGB}) \\implies \\Delta E_{\\text{out-of-gamut}} > 0",
            "legend": "• RGB (Additive): $0-255$, sumber cahaya layar monitor<br>• CMYK (Subtractive): $0-100\\%$, pantulan cahaya pigmen tinta<br>• Out of Gamut: Warna layar yang mustahil diproduksi tinta standar"
        },
        "hints": {
            "concept": "RGB berbasis emisi cahaya (layar) memiliki gamut jauh lebih luas dari CMYK yang berbasis penyerapan cahaya oleh pigmen tinta fisik.",
            "execution": "Warna neon menyala berada di luar jangkauan (out of gamut) CMYK, sehingga warna terpaksa dipadatkan ke warna printable terdekat."
        }
    },
    {
        "id": "tekd-lat-e-04",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Exposure Triangle: Shutter Speed",
        "stem": "Seorang fotografer komersial ditugaskan memotret produk minuman bersoda di studio. Klien menginginkan foto percikan air soda yang menyembur keluar dari kaleng terlihat sangat tajam dan membeku tanpa ada jejak kabur gerak (motion blur). Pengaturan Shutter Speed kamera yang wajib dipilih adalah...",
        "correct": "Shutter speed tinggi, minimal 1/1000 hingga 1/2000 detik, untuk membekukan pergerakan cepat tetesan air percikan soda dalam fraksi waktu sangat singkat.",
        "distractors": [
            "Shutter speed lambat, sekitar 1/4 hingga 1/2 detik, agar sensor menangkap seluruh jejak lintasan gerak gelembung air secara artistik.",
            "Mengunci shutter speed pada mode Bulb (B) selama 10 detik dengan bukaan diafragma lensa terbuka maksimal di f/1.4.",
            "Menurunkan nilai ISO ke level terendah 50 tanpa memperhatikan kecepatan tirai rana (shutter curtain) kamera.",
            "Menggunakan shutter speed 1/30 detik dengan mengaktifkan fitur Optical Image Stabilization pada bodi kamera."
        ],
        "formula": {
            "title": "SEGITIGA EKSPOSUR - SHUTTER SPEED",
            "latex": "t_{\\text{shutter}} \\le \\frac{1}{1000}\\,\\text{s} \\implies \\text{Motion Blur} \\approx 0",
            "legend": "• Fast Shutter ($\\ge 1/1000$s): Freeze action (tetesan air, olahraga)<br>• Slow Shutter ($< 1/60$s): Motion blur, panning, light trails<br>• Rule of Thumb: Minimal $1/\\text{focal length}$ tanpa tripod"
        },
        "hints": {
            "concept": "Kecepatan rana (shutter speed) mengontrol durasi sensor kamera terpapar cahaya. Semakin singkat durasi rana terbuka, semakin tajam aksi cepat dibekukan.",
            "execution": "Untuk membekukan cipratan cairan (splash photography), dibutuhkan rana berkecepatan tinggi ($\ge 1/1000$ s)."
        }
    },
    {
        "id": "tekd-lat-e-05",
        "materi": "KOMPUTER GRAFIS & VEKTOR",
        "topic": "Vektor vs Bitmap/Raster",
        "stem": "Sebuah agensi periklanan merancang master logo untuk perusahaan telekomunikasi multinasional yang nantinya akan diaplikasikan pada berbagai media, mulai dari kartu nama ukuran 9x5 cm hingga papan reklame billboard ukuran 12x4 meter. Alasan utama logo wajib dibuat dalam format grafis berbasis vektor adalah...",
        "correct": "Grafis vektor disusun oleh koordinat matematis dan kurva Bézier sehingga dapat diperbesar hingga ukuran billboard raksasa tanpa penurunan ketajaman atau pecah piksel (resolution independent).",
        "distractors": [
            "Grafis vektor memiliki jumlah variasi spektrum warna gradasi fotorealistik yang jauh melampaui kemampuan file foto JPEG resolusi ultra-HD.",
            "File vektor secara otomatis mengubah warna font menjadi CMYK saat dibuka di perangkat mobile apa pun tanpa software desain.",
            "Format vektor dapat langsung dicetak oleh mesin offset tanpa memerlukan tahapan raster image processor (RIP).",
            "File vektor memiliki ukuran data yang selalu di bawah 10 Kilobyte terlepas dari seberapa rumit ribuan objek ilustrasi di dalamnya."
        ],
        "formula": {
            "title": "KARAKTERISTIK VEKTOR MATEMATIS",
            "latex": "\\mathbf{B}(t) = (1-t)^3 \\mathbf{P}_0 + 3(1-t)^2 t \\mathbf{P}_1 + 3(1-t) t^2 \\mathbf{P}_2 + t^3 \\mathbf{P}_3",
            "legend": "• Kurva Bézier: Dihitung secara matematis dari titik jangkar (anchor point)<br>• Vektor: Resolusi independen (skalabilitas tak terbatas tanpa pecah)<br>• Raster: Resolusi dependen (berbasis matriks grid piksel terbatas)"
        },
        "hints": {
            "concept": "Vektor tidak tersusun atas kotak-kotak piksel mati, melainkan formula kurva matematis yang dihitung ulang setiap kali diperbesar.",
            "execution": "Keunggulan utama vektor untuk logo adalah ketajaman yang konsisten dari kartu nama mikro hingga billboard makro (resolution independence)."
        }
    },
    {
        "id": "tekd-lat-e-06",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Aturan 20-20-20 & Ergonomi Workstation",
        "stem": "Seorang desainer grafis sering mengalami Computer Vision Syndrome (CVS) berupa mata perih, kering, dan sakit kepala setelah menatap layar monitor 4K selama 8 jam tanpa henti. Berdasarkan standar K3LH industri kreatif, penerapan aturan '20-20-20' yang tepat untuk mencegah kelelahan mata tersebut adalah...",
        "correct": "Setiap bekerja menatap monitor selama 20 menit, alihkan pandangan melihat objek yang berjarak minimal 20 kaki (sekitar 6 meter) selama minimal 20 detik.",
        "distractors": [
            "Mengistirahatkan mata selama 20 menit penuh setiap kali selesai mendesain selama 20 detik pada tingkat kecerahan layar 20 persen.",
            "Mengedipkan mata sebanyak 20 kali dalam durasi 20 detik sambil menyemprotkan cairan pembersih layar monitor setiap 20 menit sekali.",
            "Menjauhkan jarak mata dari permukaan layar komputer grafis sejauh 20 sentimeter dan memutar kursi kerja sebesar 20 derajat.",
            "Menatap lampu ultraviolet meja kerja berdaya 20 Watt selama 20 detik setiap kali pergantian sesi rendering grafis 3D."
        ],
        "formula": {
            "title": "STANDAR K3LH 20-20-20 RULE",
            "latex": "t_{\\text{work}} = 20\\,\\text{min} \\implies d_{\\text{focus}} \\ge 20\\,\\text{feet} \\ (\\approx 6\\,\\text{m}), \\quad t_{\\text{rest}} \\ge 20\\,\\text{s}",
            "legend": "• Otot Siliaris: Berelaksasi saat melihat jarak jauh ($\ge 6$ m)<br>• CVS (Computer Vision Syndrome): Akibat kontraksi akomodasi lensa mata terus-menerus<br>• Blinking: Meningkat dari 5-7 kali/menit menjadi normal 15-20 kali/menit"
        },
        "hints": {
            "concept": "Aturan 20-20-20 direkomendasikan dokter mata dan ergonomi kerja: 20 menit kerja, lihat 20 kaki (6 meter), selama 20 detik.",
            "execution": "Tujuannya merelaksasi otot fokus mata (otot siliaris) yang tegang karena terus mengakomodasi jarak dekat layar."
        }
    },
    {
        "id": "tekd-lat-e-07",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Hak Moral vs Hak Ekonomi UU Hak Cipta",
        "stem": "Sebuah perusahaan minuman membeli desain ilustrasi kemasan dari seorang desainer grafis lepas seharga Rp10.000.000 dengan perjanjian pengalihan hak komersial. Setahun kemudian, perusahaan tersebut mengubah warna ilustrasi tanpa izin desainer dan menghapus nama desainer dari katalog karya resmi. Ditinjau dari UU No. 28 Tahun 2014 tentang Hak Cipta, tindakan perusahaan tersebut melanggar...",
        "correct": "Hak Moral pencipta, karena hak moral melekat secara abadi pada diri pencipta untuk dicantumkan namanya dan tidak boleh diubah atau dirusak integritas karyanya meskipun hak ekonomi telah dialihkan.",
        "distractors": [
            "Hak Desain Tata Letak Sirkuit Terpadu, karena ilustrasi kemasan tergolong komponen semikonduktor visual berlisensi terbuka.",
            "Hak Paten Sederhana, karena perusahaan belum membayar royalti perpanjangan masa perlindungan invasi teknologi 10 tahunan.",
            "Hak Merek Dagang Kolektif, karena kemasan minuman tidak boleh menggunakan warna selain warna primer yang telah disepakati kementerian perindustrian.",
            "Ketentuan Lisensi Domain Publik, karena seluruh karya seni yang dibuat oleh pekerja lepas otomatis menjadi milik bersama masyarakat."
        ],
        "formula": {
            "title": "HAK CIPTA: MORAL VS EKONOMI (UU 28/2014)",
            "latex": "\\text{Hak Cipta} = \\text{Hak Moral (Abadi, Non-transferable)} + \\text{Hak Ekonomi (Lisensi, Transferable)}",
            "legend": "• Hak Moral: Hak diatribusikan nama pencipta & perlindungan integritas ciptaan<br>• Hak Ekonomi: Hak menggandakan, menerbitkan, dan memperoleh royalti finansial<br>• Status: Hak ekonomi dapat dijual/dialihkan, hak moral tetap melekat"
        },
        "hints": {
            "concept": "Hak Moral (Pasal 5 UU Hak Cipta) meliputi hak mencantumkan nama dan menjaga keutuhan karya. Hak ini abadi dan tidak dapat dilepaskan.",
            "execution": "Pengalihan hak komersial hanya mencakup Hak Ekonomi, bukan Hak Moral sang desainer."
        }
    },
    {
        "id": "tekd-lat-e-08",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Anatomi Huruf: Kerning, Tracking & Leading",
        "stem": "Dalam mendesain judul tajuk utama (headline) sebuah poster film laga, huruf 'A' dan 'V' yang berdampingan terlihat memiliki celah kosong yang terlalu renggang sehingga tampak terpisah secara janggal. Parameter tipografi digital yang wajib disesuaikan untuk merapatkan jarak spasial antar pasangan dua huruf spesifik tersebut adalah...",
        "correct": "Kerning, yaitu penyesuaian jarak ruang optis secara individual antara dua karakter huruf yang berdampingan agar tampak harmonis dan seimbang.",
        "distractors": [
            "Leading, yaitu penyesuaian jarak vertikal antara garis dasar (baseline) baris teks atas dan baris teks di bawahnya.",
            "Tracking, yaitu penambahan atau pengurangan jarak horizontal secara seragam pada seluruh blok kata atau kalimat sekaligus.",
            "Baseline Shift, yaitu pergeseran posisi vertikal satu huruf ke atas atau ke bawah relatif terhadap garis dasar normal.",
            "X-Height, yaitu tinggi badan rata-rata huruf kecil seperti 'x', 'a', dan 'o' diukur dari batas garis dasar (baseline)."
        ],
        "formula": {
            "title": "ANATOMI TIPOGRAFI MIKRO",
            "latex": "\\text{Spasial Huruf}: \\quad \\text{Kerning (Pair-specific)} \\neq \\text{Tracking (Global Block)} \\neq \\text{Leading (Vertical Line-height)}",
            "legend": "• Kerning: Jarak antar 2 huruf spesifik (misal: AV, To, WA)<br>• Tracking: Spasi seragam seluruh teks dalam 1 paragraf/kata<br>• Leading: Jarak vertikal antar baris dari baseline ke baseline"
        },
        "hints": {
            "concept": "Kerning khusus mengatur jarak antar sepasang karakter spesifik, sedangkan tracking mengatur spasi keseluruhan kata/paragraf.",
            "execution": "Celah janggal antara dua karakter tunggal 'A' dan 'V' diselesaikan dengan optical/manual kerning."
        }
    },
    {
        "id": "tekd-lat-e-09",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Standar Resolusi Cetak DPI vs Resolusi Layar PPI",
        "stem": "Sebuah brosur pameran produk otomotif dirancang untuk dicetak pada kertas Art Paper 150 GSM menggunakan mesin cetak separasi offset 4 warna. Standar resolusi gambar bitmap minimum yang wajib disiapkan oleh desainer grafis agar hasil cetak foto mobil tidak tampak buram atau berpiksel adalah...",
        "correct": "300 DPI (dots per inch) pada ukuran cetak aktual 1:1, sesuai dengan standar resolusi separasi raster offset industri percetakan berkualitas tinggi.",
        "distractors": [
            "72 DPI, karena ukuran ini merupakan standar emas yang sudah mencukupi untuk seluruh kebutuhan tampilan monitor dan cetak masal.",
            "150 DPI, karena kerapatan titik tersebut sudah melampaui batas kemampuan mata manusia untuk membedakan detail pada jarak 20 meter.",
            "600 DPI, karena mesin cetak offset konvensional otomatis merusak plat cetak jika resolusi gambar di bawah nilai tersebut.",
            "1200 DPI, agar file desain berukuran gigabyte sehingga menghasilkan ketebalan lapisan laminasi glossy yang optimal."
        ],
        "formula": {
            "title": "STANDAR RESOLUSI PRE-PRESS OFFSET",
            "latex": "\\text{Resolusi Cetak (DPI)} = 2 \\times \\text{LPI (Lines per Inch)} \\implies 2 \\times 150\\,\\text{LPI} = 300\\,\\text{DPI}",
            "legend": "• 72/96 PPI: Standar resolusi layar digital konvensional<br>• 300 DPI: Standar industri cetak commercial art paper / offset<br>• Dimensi Piksel: $\\text{Lebar Pixel} = \\text{Inci} \\times 300$"
        },
        "hints": {
            "concept": "Standar cetak offset komersial membutuhkan 300 DPI pada skala aktual agar separasi raster halftone tidak pecah.",
            "execution": "300 DPI adalah angka baku industri grafis pra-cetak (pre-press)."
        }
    },
    {
        "id": "tekd-lat-e-10",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Hierarki Visual & Aturan Sepertiga (Rule of Thirds)",
        "stem": "Dalam mendesain antarmuka landing page situs web portofolio, desainer membagi bidang kanvas layar dengan dua garis vertikal dan dua garis horizontal berjarak sama sehingga menghasilkan 9 kotak proporsional. Berdasarkan aturan komposisi Rule of Thirds, area yang paling efektif untuk menempatkan tombol Call to Action (CTA) agar segera memicu respons klik pengguna adalah...",
        "correct": "Pada salah satu dari empat titik temu perpotongan garis (power points / intersection points), karena titik tersebut merupakan area alami tangkapan fokus pertama mata manusia.",
        "distractors": [
            "Tepat menempel di sudut kiri paling bawah halaman agar pengguna harus menggulir (scroll) hingga akhir konten web.",
            "Di tengah-tengah persis kotak paling atas di luar batas pandang layar pertama (above the fold).",
            "Disebar secara acak di dalam seluruh 9 kotak secara bersamaan untuk memberikan variasi opsi visual kepada pengunjung.",
            "Di area margin terluar kanvas yang tidak terjangkau oleh batas kursor mouse pengguna."
        ],
        "formula": {
            "title": "RULE OF THIRDS INTERSECTION POINTS",
            "latex": "(x_i, y_j) \\in \\left\\{ \\frac{1}{3}W, \\frac{2}{3}W \\right\\} \\times \\left\\{ \\frac{1}{3}H, \\frac{2}{3}H \\right\\}",
            "legend": "• 4 Intersection Points: Titik kekuatan visual utama (power points)<br>• Asymmetry Balance: Menghindari kekakuan komposisi tepat di pusat dead-center<br>• CTA Placement: Efektif menarik perhatian spontan mata"
        },
        "hints": {
            "concept": "Rule of Thirds menempatkan objek fokus di titik perpotongan (intersection point) sepertiga bidang kanvas.",
            "execution": "Perpotongan garis 1/3 dan 2/3 kanvas adalah titik alami fokus pertama pandangan mata."
        }
    },
    {
        "id": "tekd-lat-e-11",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Depth of Field (Aperture / Diafragma)",
        "stem": "Seorang fotografer memotret model perhiasan cincin emas di atas meja marmer. Ia menginginkan detail cincin tampak sangat tajam dan fokus, sementara latar belakang ruangan di belakangnya menjadi buram halus (bokeh estetik). Pengaturan nilai bukaan diafragma lensa (aperture/f-number) yang wajib diterapkan adalah...",
        "correct": "Bukaan diafragma besar dengan angka f-stop kecil, seperti f/1.8 atau f/2.8, untuk menghasilkan kedalaman bidang sempit (shallow depth of field) dengan efek bokeh dramatis.",
        "distractors": [
            "Bukaan diafragma kecil dengan angka f-stop besar, seperti f/16 atau f/22, untuk membuat seluruh latar belakang sama tajamnya dengan objek cincin.",
            "Menutup bilah diafragma lensa sepenuhnya ke f/32 dan menaikkan ISO kamera hingga batas noise maksimum ISO 25.600.",
            "Memilih lensa sudut lebar (wide-angle 10mm) dengan bukaan f/11 yang diarahkan dari jarak 5 meter dari posisi meja.",
            "Mengganti sensor kamera dengan sensor mikro tanpa menggunakan lensa optik apa pun."
        ],
        "formula": {
            "title": "APERTURE & DEPTH OF FIELD",
            "latex": "\\text{Nilai } f\\text{-stop} \\downarrow (\\text{Bukaan } \\uparrow) \\implies \\text{Depth of Field (DoF)} \\downarrow (\\text{Bokeh Maksimal})",
            "legend": "• f/1.4 - f/2.8: Bukaan besar $\\implies$ DoF sempit (latar belakang blur/bokeh)<br>• f/8 - f/11: Sweet spot ketajaman lensa<br>• f/16 - f/22: Bukaan kecil $\\implies$ DoF lebar (lanskap tajam depan-belakang)"
        },
        "hints": {
            "concept": "Angka f-number berbanding terbalik dengan bukaan diafragma: angka kecil = bukaan lebar = depth of field sempit = bokeh latar.",
            "execution": "f/1.8 atau f/2.8 membuka diafragma lebar-lebar sehingga latar belakang menjadi buram lembut."
        }
    },
    {
        "id": "tekd-lat-e-12",
        "materi": "DESAIN MEDIA & KEMASAN",
        "topic": "Anatomi Dieline Kemasan (Crease vs Cut Line)",
        "stem": "Dalam pembuatan layout cetak kemasan kotak kosmetik lipstik (dieline packaging), desainer menggunakan warna garis khusus untuk membedakan instruksi mesin pond/finishing. Garis lurus tegas warna merah (Cyan/Magenta solid) dan garis putus-putus warna hijau pada file master cetak umumnya berturut-turut merepresentasikan...",
        "correct": "Garis potong pisau pond (cut line) untuk memotong pola lembaran karton, dan garis tekuk/lipatan (crease/fold line) untuk memudahkan pelipatan kotak kemasan.",
        "distractors": [
            "Garis batas area penempelan lem perekat karton, dan garis batas tanggal kedaluwarsa produk kosmetik.",
            "Garis batas toleransi radiasi ultraviolet mesin cetak, dan garis indikator arah tiupan angin ruang pengering kertas.",
            "Garis tempat pencetakan barcode produk komersial, dan garis batas penulisan teks komposisi bahan kimia.",
            "Garis batas potong pisau guillotine potong lurus, dan garis cetak warna perak foil panas (hot stamping)."
        ],
        "formula": {
            "title": "STANDAR DIELINE PACKAGING DESIGN",
            "latex": "\\text{Dieline} = \\text{Cut Line (Solid/Garis Potong)} + \\text{Crease Line (Dashed/Garis Lipat)} + \\text{Bleed}",
            "legend": "• Solid Line: Pisau potong menembus kertas karton<br>• Dashed Line: Pisau tumpul/roda penekan pembentuk alur lipatan<br>• Spot Color: Menggunakan tinta khusus (misal: Die-Cut) bertipe Technical"
        },
        "hints": {
            "concept": "Dieline kemasan membedakan garis potong fisik (solid cut) dan garis lipat yang tidak tembus kertas (crease/perforasi bergaris putus-putus).",
            "execution": "Garis tegas = potong (cut); garis putus-putus = lipat (crease/fold)."
        }
    },
    {
        "id": "tekd-lat-e-13",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Fungsi Bleed & Trim Mark pada File Cetak",
        "stem": "Ketika mempersiapkan dokumen majalah ukuran A4 untuk dikirim ke percetakan, desainer grafis menambahkan bidang lebihan gambar seluas 3 mm di luar garis batas potong halaman (trim line). Fungsi vital dari penambahan area bleed tersebut adalah...",
        "correct": "Mencegah munculnya garis putih tipis di tepi kertas majalah apabila terjadi pergeseran mekanis pisau mesin potong (guillotine) saat memotong tumpukan kertas.",
        "distractors": [
            "Mempercepat waktu penyerapan tinta cetak Cyan dan Magenta ke dalam pori-pori kertas HVS.",
            "Menyediakan ruang kosong khusus bagi operator percetakan untuk membubuhkan tanda tangan serah terima dokumen.",
            "Memastikan nomor halaman (folio) tercetak tepat di tengah-tengah punggung jilid kawat majalah.",
            "Mengurangi beban kompresi file PDF cetak saat dikirim melalui surat elektronik."
        ],
        "formula": {
            "title": "STANDAR AREA BLEED PRE-PRESS",
            "latex": "\\text{Dimensi Kanvas Cetak} = \\text{Ukuran Bersih (Trim)} + (2 \\times \\text{Bleed}) \\implies A4 + (2 \\times 3\\,\\text{mm})",
            "legend": "• Trim Line: Garis ukuran potong final dokumen<br>• Bleed: Lebihan gambar/latar 3-5 mm ke luar trim line<br>• Margin Aman: Jarak teks minimal 5 mm ke dalam dari trim line"
        },
        "hints": {
            "concept": "Pisau potong mesin potong kertas (guillotine) memiliki toleransi pergeseran mikro (1-2 mm). Jika tidak ada bleed, selisih potong meninggalkan tepi putih kertas kosong.",
            "execution": "Bleed menjamin gambar latar tercetak penuh hingga ke tepi lembaran tanpa cela putih."
        }
    },
    {
        "id": "tekd-lat-e-14",
        "materi": "KOMPUTER GRAFIS & VEKTOR",
        "topic": "Pen Tool: Anchor Point & Direction Handle",
        "stem": "Saat membuat gambar ilustrasi maskot kartun di software Adobe Illustrator menggunakan Pen Tool, seorang desainer menarik tuas kendali (direction handle) dari sebuah titik jangkar (anchor point). Dampak langsung dari pemanjangan tuas kendali tersebut terhadap garis kurva Bézier yang terbentuk adalah...",
        "correct": "Tingkat kelengkungan (curvature) garis kurva semakin melambung tinggi dan tumpul seiring bertambah panjangnya tarikan tuas kendali arah.",
        "distractors": [
            "Garis kurva secara otomatis berubah seketika menjadi garis patah-patah dengan sudut lancip 90 derajat siku-siku.",
            "Warna isian (fill color) objek vektor secara instan terhapus dan digantikan oleh tekstur gradasi transparan.",
            "Titik jangkar terhapus secara permanen dari kanvas kerja tanpa meninggalkan jejak koordinat vektor.",
            "Resolusi piksel kanvas Adobe Illustrator turun dari 300 PPI menjadi 72 PPI secara otomatis."
        ],
        "formula": {
            "title": "MATEMATIKA KURVA BÉZIER KUBIK",
            "latex": "\\frac{d\\mathbf{B}(0)}{dt} = 3(\\mathbf{P}_1 - \\mathbf{P}_0) \\implies |\\mathbf{P}_1 - \\mathbf{P}_0| \\propto \\text{Radius Kelengkungan}",
            "legend": "• $\\mathbf{P}_0, \\mathbf{P}_3$: Anchor point (titik jangkar)<br>• $\\mathbf{P}_1, \\mathbf{P}_2$: Control handle (tuas kendali vektor)<br>• Panjang Handle: Menentukan kekuatan gaya tarik kelengkungan kurva"
        },
        "hints": {
            "concept": "Semakin panjang handle ditarik dari anchor point, semakin besar tegangan kurva sehingga lengkungannya makin dalam dan lebar.",
            "execution": "Tuas kendali (handle) menentukan amplitudo dan arah kelengkungan kurva Bézier."
        }
    },
    {
        "id": "tekd-lat-e-15",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Nirmana Warna: Komplementer vs Analog",
        "stem": "Sebuah restoran cepat saji ingin merancang logo yang menciptakan kontras dramatis, menarik perhatian mata seketika dari kejauhan, dan menonjolkan energi dinamis. Berdasarkan roda warna Brewster (color wheel), perpaduan skema warna komplementer yang tepat diaplikasikan adalah...",
        "correct": "Memadukan dua warna yang posisinya saling berseberangan langsung 180 derajat pada lingkaran warna, seperti warna merah dengan hijau atau biru dengan jingga.",
        "distractors": [
            "Memadukan tiga warna yang letaknya saling berdampingan bersebelahan pada lingkaran warna, seperti kuning, kuning-hijau, dan hijau.",
            "Menggunakan variasi tingkat kecerahan (tint) dan kegelapan (shade) dari satu warna tunggal yang identik secara monokromatik.",
            "Mengombinasikan tiga warna yang membentuk segitiga sama sisi berjarak seimbang 120 derajat pada lingkaran warna secara triadik.",
            "Hanya menggunakan gradasi warna abu-abu netral antara hitam pekat dan putih bersih tanpa pigmen warna kromatik."
        ],
        "formula": {
            "title": "SKEMA WARNA KOMPLEMENTER (BREWSTER)",
            "latex": "\\theta_{\\text{komplementer}} = 180^\\circ \\implies \\text{Kontras Visual Maksimal}",
            "legend": "• Komplementer: Berseberangan $180^\\circ$ (Merah-Hijau, Biru-Oranye, Kuning-Ungu)<br>• Analog: Bersebelahan $30^\\circ - 60^\\circ$ (Harmonis, tenang)<br>• Triadik: Membentuk sudut $120^\\circ$ (Dinamis seimbang)"
        },
        "hints": {
            "concept": "Warna komplementer adalah pasangan warna yang letaknya berseberangan tepat 180 derajat di color wheel.",
            "execution": "Memberikan kontras visual paling tajam dan memicu stimulasi optis instan pada audiens."
        }
    },
    {
        "id": "tekd-lat-e-16",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Skema Three-Point Lighting",
        "stem": "Dalam sesi pemotretan video profil direktur perusahaan di studio, penata cahaya menyusun tiga sumber lampu buatan. Lampu yang diposisikan di belakang subjek menghadap ke arah punggung dan rambut model untuk memisahkan siluet model dari latar belakang gelap disebut...",
        "correct": "Back light (rim light / hair light), yang menciptakan garis tepian cahaya berkilau di kepala dan bahu subjek agar tidak tenggelam menyatu dengan latar belakang.",
        "distractors": [
            "Key light, yang berfungsi sebagai sumber cahaya utama terkuat untuk menerangi sisi utama wajah subjek dari depan samping.",
            "Fill light, yang diletakkan di sisi berlawanan dari sumber utama untuk melembutkan bayangan pekat pada lekukan wajah.",
            "Ambient light, yaitu cahaya alami yang merembes melalui celah ventilasi jendela tanpa dapat dikontrol intensitas dayanya.",
            "Catch light, yaitu lampu sorot berkekuatan 5000 Watt yang diarahkan langsung tegak lurus ke pupil mata model dari jarak 10 cm."
        ],
        "formula": {
            "title": "THREE-POINT LIGHTING SETUP",
            "latex": "\\text{Pencahayaan Studio} = \\text{Key Light (Utama)} + \\text{Fill Light (Pengisi Bayangan)} + \\text{Back Light (Pemisah Latar)}",
            "legend": "• Key: $45^\\circ$ depan, intensitas $100\\%$<br>• Fill: $-45^\\circ$ depan, intensitas $50\\%$ (rasio 2:1)<br>• Back/Hair: Belakang subjek, memunculkan garis pemisah dimensi kedalaman (rim)"
        },
        "hints": {
            "concept": "Three-point lighting terdiri dari Key light (utama), Fill light (pengisi bayangan), dan Back light (pemisah latar belakang/rim).",
            "execution": "Cahaya dari belakang subjek untuk memberi garis tepian pemisah adalah Back Light."
        }
    },
    {
        "id": "tekd-lat-e-17",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Format Citra: Lossy vs Lossless Compression",
        "stem": "Seorang desainer web UI/UX diminta mengoptimalkan gambar ikon ilustrasi transparan untuk sebuah aplikasi perbankan digital agar waktu muat (loading speed) halaman tetap di bawah 1 detik tanpa kehilangan ketajaman garis batas transparan. Format file grafis yang paling tepat digunakan adalah...",
        "correct": "Format SVG (Scalable Vector Graphics) untuk ikon vektor murni atau WebP/PNG-8 berbobot ringan untuk mendukung transparansi alfa dengan kompresi lossless yang efisien.",
        "distractors": [
            "Format BMP (Bitmap) resolusi mentah tanpa kompresi yang menghasilkan ukuran file 15 Megabyte per ikon aplikasi.",
            "Format JPEG standar dengan tingkat kompresi kualitas 10 persen yang otomatis mengubah latar transparan menjadi kotak hitam pekat.",
            "Format TIFF berlapis ganda (multi-layer) khusus mesin pembuat plat film separasi offset komersial.",
            "Format RAW digital negative langsung dari kamera DSLR tanpa melalui tahapan ekspor digital."
        ],
        "formula": {
            "title": "OPTIMASI FORMAT WEB & TRANSPARANSI",
            "latex": "\\text{Web Asset} = \\text{SVG (Vector Ikon)} \\lor \\text{WebP/PNG (Lossless Alpha Channel Transparansi)}",
            "legend": "• SVG: Vektor murni berbasis XML, ukuran kecil, tajam di segala resolusi layar retina<br>• PNG/WebP: Raster dengan dukungan transparansi kanal alfa 8-bit/24-bit<br>• JPEG: Raster lossy tanpa kanal transparansi (selalu terisi latar putih/hitam)"
        },
        "hints": {
            "concept": "JPEG tidak mendukung transparansi latar. Ikon web paling ideal memakai SVG (vektor) atau PNG/WebP (raster transparan).",
            "execution": "SVG dan PNG/WebP mendukung kanal alfa transparan dengan kompresi web yang cepat."
        }
    },
    {
        "id": "tekd-lat-e-18",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Skala Hierarki Visual Tipografi",
        "stem": "Pada halaman depan surat kabar cetak harian, susunan judul berita, sub-judul, dan isi teks bacaan dirancang dengan ukuran poin font, ketebalan (weight), dan gaya yang berbeda secara mencolok. Tujuan fungsional utama penerapan hierarki visual tipografi tersebut adalah...",
        "correct": "Mengarahkan alur membaca mata pembaca dari informasi paling penting (headline) ke informasi penjelas pendukung secara bertahap dan teratur.",
        "distractors": [
            "Menghabiskan seluruh stok variasi font berbayar yang dimiliki oleh perusahaan media massa dalam satu terbitan.",
            "Membuat tampilan halaman terlihat rumit dan membingungkan agar pembaca membutuhkan waktu lebih lama di lapak koran.",
            "Memenuhi kuota aturan kementerian komunikasi yang mewajibkan penggunaan minimal lima jenis font asing per lembar koran.",
            "Menghindari penggunaan spasi antar kata agar seluruh bidang kertas terisi penuh oleh tinta cetak hitam."
        ],
        "formula": {
            "title": "HIERARKI TIPOGRAFI & SCANABILITY",
            "latex": "\\text{Level Hierarki}: \\text{H1 (Headline/Primer)} > \\text{H2 (Subhead/Sekunder)} > \\text{Body Text (Tersier)}",
            "legend": "• Primer (Headline): Ukuran besar/bold, eye catcher pertama<br>• Sekunder (Subhead): Poin ringkasan penuntun konteks<br>• Tersier (Body text): Nyaman dibaca panjang (readability tinggi)"
        },
        "hints": {
            "concept": "Hierarki tipografi mengatur urutan atensi membaca dari yang paling krusial ke detail pendukung.",
            "execution": "Tujuannya membimbing pembaca menyerap berita terpenting lebih dulu secara terstruktur."
        }
    },
    {
        "id": "tekd-lat-e-19",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Lisensi Creative Commons: CC BY-NC",
        "stem": "Seorang desainer mengambil sebuah aset ilustrasi dari internet yang berlabel lisensi Creative Commons 'CC BY-NC'. Tindakan hukum yang sah dan diperbolehkan bagi desainer tersebut terkait penggunaan aset tersebut adalah...",
        "correct": "Menggunakan dan memodifikasi ilustrasi tersebut untuk poster kampanye sosial non-komersial di sekolah dengan tetap mencantumkan kredit nama pencipta aslinya.",
        "distractors": [
            "Menjual langsung karya ilustrasi tersebut sebagai paket stiker merchandise komersial di marketplace demi meraup keuntungan pribadi.",
            "Mengganti nama pencipta asli dengan nama sendiri lalu mendaftarkan karya tersebut ke Ditjen KI sebagai merek dagang eksklusif.",
            "Memasukkan ilustrasi tersebut ke dalam desain kemasan produk sabun mandi komersial yang diproduksi pabrik secara massal.",
            "Melarang masyarakat umum melihat poster tersebut karena lisensi NC berarti karya tersebut rahasia negara."
        ],
        "formula": {
            "title": "DEKODIFIKASI LISENSI CREATIVE COMMONS",
            "latex": "\\text{CC BY-NC} = \\text{BY (Attribution / Wajib Sebut Pencipta)} + \\text{NC (Non-Commercial / Dilarang Tujuan Dagang)}",
            "legend": "• BY: Atribusi nama wajib dicantumkan<br>• NC: Dilarang untuk tujuan keuntungan komersial/finansial<br>• SA (ShareAlike): Wajib rilis dengan lisensi serupa jika diubah<br>• ND (NoDerivatives): Tidak boleh diubah/dimodifikasi"
        },
        "hints": {
            "concept": "BY = Atribusi (beri kredit pencipta); NC = Non-Commercial (bukan untuk jualan komersial).",
            "execution": "Boleh untuk kegiatan sosial nirlaba/sekolah asalkan nama pembuat aslinya dicantumkan."
        }
    },
    {
        "id": "tekd-lat-e-20",
        "materi": "DESAIN MEDIA & KEMASAN",
        "topic": "Tipe-Tipe Logo: Logomark vs Logotype",
        "stem": "Perusahaan apparel olahraga ternama dunia menggunakan lambang centang ikonik (Swoosh) tanpa teks nama perusahaan, namun konsumen di seluruh dunia langsung mengenali identitas merek tersebut. Ditinjau dari klasifikasi tipologi bentuk logo, jenis logo lambang centang tersebut dikategorikan sebagai...",
        "correct": "Pictorial Mark (Brand Mark / Logomark), yaitu logo berbasis simbol atau ikon grafis representatif tanpa menggunakan elemen teks nama merek secara langsung.",
        "distractors": [
            "Wordmark (Logotype), yaitu logo yang hanya berupa tipografi teks nama perusahaan tanpa ada simbol gambar pendukung.",
            "Monogram (Lettermark), yaitu logo berbasis inisial huruf tunggal atau kombinasi beberapa huruf awal nama perusahaan.",
            "Emblem, yaitu logo di mana teks nama merek berada terkurung di dalam bingkai lencana atau stempel tradisional.",
            "Mascot Logo, yaitu logo yang menggunakan karakter tokoh kartun manusia atau hewan sebagai juru bicara merek."
        ],
        "formula": {
            "title": "TAKSONOMI BENTUK LOGO",
            "latex": "\\text{Brand Identity} = \\text{Brandmark (Simbol Murni)} \\lor \\text{Wordmark (Tipografi Teks)} \\lor \\text{Kombinasi}",
            "legend": "• Pictorial/Brand Mark: Ikon murni (Apple, Nike Swoosh, Twitter Bird)<br>• Wordmark/Logotype: Tipografi nama (Google, Coca-Cola, Sony)<br>• Lettermark: Singkatan (NASA, IBM, HBO)<br>• Emblem: Lencana padat (Starbucks, Harley Davidson)"
        },
        "hints": {
            "concept": "Lambang visual mandiri tanpa tulisan huruf disebut Brandmark atau Pictorial Mark.",
            "execution": "Nike Swoosh dan Apple adalah contoh paling representatif dari Brand Mark / Pictorial Mark murni."
        }
    },
    {
        "id": "tekd-lat-e-21",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Nirmana Dwimatra: Tekstur Nyata vs Tekstur Semu",
        "stem": "Pada sebuah lukisan digital di layar tablet grafis, desainer berhasil membuat objek kain sutra dan dinding bata tampak sangat kasar dan bergelombang. Namun ketika permukaan layar tablet disentuh dengan jari, terasa tetap rata dan licin sempurna. Karakteristik permukaan visual pada layar tersebut dinamakan...",
        "correct": "Tekstur semu (visual texture), yaitu ilusi tekstur yang hanya dapat dinikmati oleh indra penglihatan melalui permainan bayangan dan warna, tetapi tidak memiliki nilai raba fisik saat disentuh.",
        "distractors": [
            "Tekstur nyata (tactile texture), yaitu permukaan fisik benda yang nilai lihatnya sama persis dengan sensasi kasar-halus saat diraba langsung oleh tangan.",
            "Nirmana Trimatra plastis, yaitu patung berdimensi panjang, lebar, dan tinggi yang menembus ruang hampa fisik nyata.",
            "Tekstur holografis kinetik, yaitu pergeseran molekul layar kaca secara mekanis mengikuti instruksi file grafik.",
            "Anatomi tipografi display, yaitu tekstur yang terbentuk secara alami dari tumpukan serat kertas koran basah."
        ],
        "formula": {
            "title": "KLASIFIKASI TEKSTUR NIRMANA DWIMATRA",
            "latex": "\\text{Tekstur Visual (Semu)}: \\text{Mata} \\ne \\text{Rabaan Fisik}; \\quad \\text{Tekstur Taktil (Nyata)}: \\text{Mata} = \\text{Rabaan Fisik}",
            "legend": "• Tekstur Semu: Ilusi 2D melalui shading, highlight, dan pola grafis<br>• Tekstur Nyata: Timbul fisik (emboss, pasir cat minyak, deboss karton)<br>• Fungsi: Memberi dimensi realisme dan kedalaman visual"
        },
        "hints": {
            "concept": "Tekstur semu (visual) hanya menipu mata lewat rendering cahaya/bayangan tanpa sensasi rabaan fisik nyata.",
            "execution": "Layar tablet yang licin meskipun terlihat bertekstur bata kasar merupakan contoh tekstur semu."
        }
    },
    {
        "id": "tekd-lat-e-22",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Komposisi: Sudut Pengambilan Gambar (Camera Angle)",
        "stem": "Dalam proyek pemotretan poster promosi kepemimpinan organisasi siswa, fotografer memosisikan kamera berada jauh lebih rendah daripada posisi tubuh model dan mengarahkan lensa menghadap ke atas. Sudut pandang kamera (camera angle) ini sengaja dipilih untuk memberikan efek psikologis berupa...",
        "correct": "Low Angle, untuk membangun kesan subjek terlihat berwibawa, megah, dominan, kuat, dan memiliki otoritas tinggi.",
        "distractors": [
            "High Angle, untuk membuat subjek terlihat kerdil, lemah, tidak berdaya, dan tertekan oleh situasi lingkungan sekitar.",
            "Bird's Eye View, untuk memperlihatkan denah tata letak panggung dari sudut tegak lurus 90 derajat di langit.",
            "Frog Eye View, khusus untuk menyamarkan wajah model agar tidak dapat dikenali oleh audiens publik.",
            "Eye Level, untuk menampilkan pandangan yang netral, wajar, dan sejajar dengan pandangan mata manusia biasa."
        ],
        "formula": {
            "title": "PSIKOLOGI SUDUT PENGAMBILAN GAMBAR",
            "latex": "\\text{Low Angle} (\\theta < 0^\\circ \\implies \\text{Lensa Menghadap ke Atas}) \\implies \\text{Persepsi Kekuasaan/Dominasi} \\uparrow",
            "legend": "• Low Angle: Dari bawah ke atas $\\implies$ Berkuasa, megah, heroik<br>• High Angle: Dari atas ke bawah $\\implies$ Lemah, rentan, kecil<br>• Eye Level: Sejajar mata $\\implies$ Netral, intim, objektif"
        },
        "hints": {
            "concept": "Low Angle mengambil gambar dari bawah mengarah ke atas, memberi kesan sosok yang gagah dan berwibawa.",
            "execution": "Membangun figur kepemimpinan yang dominan menggunakan sudut rendah (Low Angle)."
        }
    },
    {
        "id": "tekd-lat-e-23",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Warna Khusus Spot Color / Pantone",
        "stem": "Sebuah bank multinasional memiliki warna identitas korporat biru toska yang sangat spesifik. Pimpinan bank menuntut agar warna biru toska pada brosur, amplop, map, dan buku tabungan yang dicetak di sepuluh percetakan rekanan berbeda memiliki warna yang 100% presisi tanpa ada sedikit pun variasi perbedaan tone warna. Solusi teknis pre-press terbaik adalah...",
        "correct": "Menggunakan sistem warna tinta khusus (Spot Color / Pantone Matching System - PMS) dengan nomor formula tinta pabrikan standar internasional.",
        "distractors": [
            "Menyerahkan kepada operator mesin cetak untuk mencampur sendiri tinta Cyan dan Yellow berdasarkan perkiraan mata secara manual.",
            "Mengonversi seluruh file cetak ke model warna RGB 8-bit lalu mencetaknya pada printer inkjet rumahan biasa.",
            "Menaikkan saturasi warna Magenta sebesar 100% pada semua file desain sebelum diekspor ke format PDF cetak.",
            "Mengganti seluruh jenis kertas di semua percetakan dengan kertas koran bekas berwarna kuning buram."
        ],
        "formula": {
            "title": "STANDARISASI WARNA BRAND - PANTONE PMS",
            "latex": "\\text{Warna Brand Presisi} = \\text{Spot Color (PMS Formula)} \\implies \\Delta E < 1.0 \\text{ antar-percetakan}",
            "legend": "• CMYK (Process): Tergantung campuran 4 tinta (rentan meleset tipis)<br>• Spot Color (PMS): Tinta premixed pabrikan dengan resep formula baku<br>• $\\Delta E < 1$: Perbedaan warna tak kasat mata manusia"
        },
        "hints": {
            "concept": "Proses separasi CMYK bisa sedikit berbeda antar mesin cetak. Spot Color (Pantone) adalah tinta pra-campur paten untuk konsistensi 100%.",
            "execution": "Pantone Matching System (PMS) menjamin akurasi warna brand identik di percetakan mana pun."
        }
    },
    {
        "id": "tekd-lat-e-24",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "UI/UX: Wireframe vs Mockup vs Prototype",
        "stem": "Dalam alur perancangan produk digital mobile banking, desainer mengawali proses dengan membuat sketsa tata letak kerangka dasar kotak abu-abu hitam-putih tanpa warna, tanpa gambar final, dan tanpa tipografi detail untuk memetakan penempatan tombol dan struktur informasi. Tahapan perancangan visual awal tersebut dinamakan...",
        "correct": "Wireframe (Low-Fidelity), yaitu bagan kerangka arsitektur tata letak antarmuka untuk memvalidasi alur fungsi navigasi sebelum tahap visual estetika diterapkan.",
        "distractors": [
            "Mockup (High-Fidelity), yaitu representasi visual final statis yang sudah dilengkapi palet warna, tipografi, dan aset visual realistis.",
            "Interactive Prototype, yaitu simulasi antarmuka yang sudah dapat diklik dan ditransisikan antar halaman untuk uji coba interaksi pengguna.",
            "Design System Tokens, yaitu dokumentasi kode CSS variabel untuk ukuran spasi dan palet warna komponen web.",
            "A/B Testing Production, yaitu pelepasan dua versi aplikasi perbankan secara acak ke jutaan nasabah perbankan aktif di pasar modal."
        ],
        "formula": {
            "title": "TAHAPAN MATURITAS DESAIN UI/UX",
            "latex": "\\text{Wireframe (Lo-Fi)} \\longrightarrow \\text{Mockup (Hi-Fi Statis)} \\longrightarrow \\text{Prototype (Hi-Fi Interaktif)}",
            "legend": "• Wireframe: Struktur & arsitektur informasi (skeletal, greyscale)<br>• Mockup: Estetika visual (warna, tipografi, visual polish)<br>• Prototype: Simulasi interaksi pengguna (clickable flows)"
        },
        "hints": {
            "concept": "Kerangka kasar hitam-putih abu-abu untuk mengatur tata letak dan fungsi disebut Wireframe (low-fidelity).",
            "execution": "Fokus pada struktur fungsional sebelum melangkah ke estetika mockup dan interaktivitas prototype."
        }
    },
    {
        "id": "tekd-lat-e-25",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Pencahayaan Ruang Kerja Komputer Grafis",
        "stem": "Seorang desainer grafis bekerja di ruang kerja studio dengan lampu sorot ruangan yang memantul langsung secara silau (glare) pada permukaan kaca layar monitor komputernya. Dampak ergonomis dan langkah penyesuaian tata cahaya ruang studio yang benar menurut K3LH adalah...",
        "correct": "Pantulan silau memicu ketegangan saraf optis mata dan distorsi penilaian warna; posisi monitor harus diatur menyamping 90 derajat terhadap sumber jendela/lampu dan menggunakan tudung monitor (hood).",
        "distractors": [
            "Silau pada layar meningkatkan kontras warna secara alami sehingga desainer tidak perlu mengubah posisi monitor sama sekali.",
            "Desainer disarankan mematikan seluruh lampu ruangan hingga gelap gulita total dan menaikkan kontras monitor ke 100 persen.",
            "Mengarahkan sorot lampu meja tepat lurus ke tengah layar monitor agar intensitas bayangan di kanvas desain menghilang.",
            "Menutup seluruh permukaan layar komputer grafis dengan kain spanduk tebal berwarna hitam saat mendesain."
        ],
        "formula": {
            "title": "STANDAR ILUMINASI & ERGONOMI LAYAR DKV",
            "latex": "\\text{Illuminance} = 300 - 500\\,\\text{lux}, \\quad \\theta_{\\text{monitor/window}} = 90^\\circ \\implies \\text{Glare} \\approx 0",
            "legend": "• Glare (Silau): Mengaburkan persepsi warna & memicu CVS<br>• Sudut $90^\\circ$: Menghindari cahaya langsung dari depan atau belakang layar<br>• Monitor Hood: Tudung pelindung samping monitor untuk akurasi kalibrasi warna"
        },
        "hints": {
            "concept": "Silau (glare) layar mengganggu akurasi warna dan merusak mata. Monitor harus diposisikan tegak lurus (90 derajat) terhadap jendela atau lampu.",
            "execution": "Hindari membelakangi atau menghadap langsung ke arah sumber cahaya untuk meniadakan silau."
        }
    }
]
