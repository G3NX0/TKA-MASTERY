# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Desain Komunikasi Visual (DKV / Rekayasa Desain SMK/MAK)
Dataset: Medium Practice (25 Authentic Questions, tekd-lat-m-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

DKV_MEDIUM_ITEMS = [
    {
        "id": "tekd-lat-m-01",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Proporsi Golden Ratio & Tata Letak",
        "stem": "Seorang desainer grafis membagi bidang kanvas editorial menggunakan perbandingan Rasio Emas (Golden Ratio $\\approx 1:1.618$). Jika kolom utama (body text) majalah dirancang dengan lebar 161.8 mm, berapakah lebar ideal kolom samping (sidebar) agar proporsi tata letak mencapai keharmonisan visual alami menurut rasio emas tersebut?",
        "correct": "100 mm, yang diperoleh dari pembagian lebar kolom utama dengan konstanta rasio emas ($161.8 \\div 1.618 = 100$).",
        "distractors": [
            "80.9 mm, yang merupakan hasil pembagian langsung kolom utama dengan angka dua bulat tanpa mempertimbangkan konstanta rasio emas.",
            "120 mm, yang merupakan perbandingan rasio diagonal sepertiga kuadratik bidang kanvas majalah standar folio.",
            "261.8 mm, yang merupakan hasil penjumlahan kumulatif deret Fibonacci tanpa memperhatikan batas total bidang margin kertas.",
            "50 mm, yang merupakan batas minimum standar kolom iklan baris menurut regulasi persuratkabaran nasional."
        ],
        "formula": {
            "title": "FORMULA GOLDEN RATIO (DIVINE PROPORTION)",
            "latex": "\\phi = \\frac{1 + \\sqrt{5}}{2} \\approx 1.618, \\quad W_{\\text{sidebar}} = \\frac{W_{\\text{main}}}{\\phi} = \\frac{161.8}{1.618} = 100\\,\\text{mm}",
            "legend": "• $\\phi$ (Phi): 1.618 (Rasio geometri alami pembentuk spiral Fibonacci)<br>• Proporsi Harmonik: $\\frac{A+B}{A} = \\frac{A}{B} = 1.618$<br>• Aplikasi: Grid majalah, logo Apple, struktur Parthenon"
        },
        "hints": {
            "concept": "Rasio Emas membagi dua bagian sedemikian rupa sehingga rasio bagian besar ke bagian kecil sama dengan rasio total ke bagian besar (1.618).",
            "execution": "Bila bagian besar adalah 161.8 mm, maka bagian kecil adalah $161.8 / 1.618 = 100$ mm."
        }
    },
    {
        "id": "tekd-lat-m-02",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Penataan Paragraf Justified & Masalah 'Rivers of White'",
        "stem": "Dalam layout kolom koran yang sempit, desainer menerapkan perataan teks rata kiri-kanan (justified alignment) dengan fitur pemenggalan kata (hyphenation) dinonaktifkan. Akibatnya, pada blok teks bacaan terlihat alur celah-celah spasi kosong putih yang mengalir secara vertikal dan diagonal menyerupai sungai di antara kata-kata. Fenomena cacat tipografi ini dan solusi teknisnya adalah...",
        "correct": "Rivers of white (sungai putih); solusinya adalah mengaktifkan hyphenation, mengatur toleransi word spacing pada dialog justification, atau beralih ke rata kiri (flush left / ragged right).",
        "distractors": [
            "Widow and Orphan; solusinya adalah menambah nilai baseline shift pada kata terakhir di setiap halaman ganjil majalah.",
            "Font Banding; solusinya adalah meningkatkan resolusi layar monitor komputer desainer ke tingkat 8K ultra-HD.",
            "Kerning Trap; solusinya adalah mengganti semua huruf kapital dengan huruf kecil italic sans-serif berbobot light.",
            "Bleed Creep; solusinya adalah memotong margin kertas koran sebanyak 10 sentimeter sebelum proses cetak."
        ],
        "formula": {
            "title": "PENGENDALIAN TIPOGRAFI KOLOM SEMPIT",
            "latex": "\\text{Justified} + \\text{Narrow Column} - \\text{Hyphenation} \\implies \\text{Rivers of White (Cacat Visual)}",
            "legend": "• Rivers: Celah ruang putih antar-kata yang saling menyambung vertikal mengganggu mata<br>• Solusi 1: Aktifkan auto/manual hyphenation (pemenggalan suku kata)<br>• Solusi 2: Flush left / Ragged right (rata kiri lebih alami untuk kolom sempit)"
        },
        "hints": {
            "concept": "Rivers of white adalah celah spasi putih vertikal yang merusak kenyamanan membaca pada teks justified tanpa hyphenation di kolom sempit.",
            "execution": "Cari opsi yang menyebut 'rivers of white' dan solusinya: hyphenation atau beralih ke rata kiri (ragged right)."
        }
    },
    {
        "id": "tekd-lat-m-03",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Rich Black vs Standard Black & Total Area Coverage (TAC)",
        "stem": "Sebuah percetakan menolak file booklet pameran karena desainer mewarnai bidang latar belakang hitam luas menggunakan formula $C=100\\%, M=100\\%, Y=100\\%, K=100\\%$. Alasan teknis penolakan dari pihak percetakan offset berdasarkan batas Total Area Coverage (TAC) adalah...",
        "correct": "Nilai TAC mencapai 400% yang melampaui batas toleransi serap kertas ($300\\%$), menyebabkan tinta terlalu tebal dan basah, lambat kering, serta menempel dan mengotori lembaran cetak lain (set-off).",
        "distractors": [
            "Warna hitam empat komponen tinta otomatis berubah menjadi putih transparan saat terkena sinar lampu UV pengering offset.",
            "Mesin cetak offset tidak memiliki silinder plat untuk warna hitam sehingga nilai K wajib diatur selalu $0\\%$.",
            "Penggunaan tinta CMYK penuh menyebabkan berat kertas booklet bertambah menjadi 5 kilogram per lembar.",
            "Perpaduan keempat tinta CMYK secara fisik melanggar undang-undang perlindungan konsumen tentang penggunaan bahan pewarna kimia."
        ],
        "formula": {
            "title": "TOTAL AREA COVERAGE (TAC) & RICH BLACK",
            "latex": "\\text{TAC} = C + M + Y + K \\le 300\\% \\quad (\\text{Rich Black Rekomendasi: } C=40, M=30, Y=30, K=100 \\implies 200\\%)",
            "legend": "• Standard Black ($K=100\\%$): $TAC = 100\\%$, pekat untuk teks kecil, agak abu pada blok besar<br>• TAC $> 300\\%$: Risiko tinggi tinta basah meluber, set-off (menjiplak), dan kertas sobek<br>• Rich Black: Hitam pekat mewah dan aman pre-press"
        },
        "hints": {
            "concept": "TAC (Total Area Coverage) tidak boleh melebihi 280-300% pada kertas coated standard agar tinta tidak basah dan menodai kertas berikutnya (set-off).",
            "execution": "Nilai $C100+M100+Y100+K100 = 400\\%$, jauh melampaui batas aman serap tinta percetakan."
        }
    },
    {
        "id": "tekd-lat-m-04",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Interpretasi Histogram Kamera (Clipping Highlights/Shadows)",
        "stem": "Saat mereview hasil jepretan foto gaun pengantin putih di layar kamera, fotografer melihat grafik histogram menumpuk tajam dan terpotong di dinding batas paling kanan (right edge). Indikasi teknis dari bentuk grafik histogram tersebut adalah...",
        "correct": "Terjadi overexposure dan highlight clipping, di mana detail tekstur kain renda putih hilang total dan menjadi putih polos tanpa data informasi piksel ($RGB=255,255,255$).",
        "distractors": [
            "Terjadi underexposure berat di mana seluruh bayangan menjadi hitam pekat pejal tanpa ada cahaya yang masuk ke sensor.",
            "Kamera mengalami kerusakan mekanis pada cermin pentaprisma sehingga tidak mampu merekam spektrum warna hijau daun.",
            "Foto berada pada kondisi pencahayaan yang sangat seimbang dan memiliki kontras warna yang sempurna untuk cetak kanvas.",
            "Nilai ketajaman lensa berada pada titik optimal sweet spot sehingga tidak memerlukan proses sharpening digital."
        ],
        "formula": {
            "title": "INTERPRETASI GRAFIK HISTOGRAM FOTOGRAFI",
            "latex": "\\text{Piksel Terpotong pada Titik } 255 \\implies \\text{Blown Highlights (Detail Putih Hilang Total)}",
            "legend": "• Sumbu X: Kecerahan dari 0 (Pure Black) ke 255 (Pure White)<br>• Sumbu Y: Jumlah piksel pada tingkat kecerahan tersebut<br>• Right Wall Spike: Overexposure (clipping highlight putih)<br>• Left Wall Spike: Underexposure (crushed shadows)"
        },
        "hints": {
            "concept": "Sisi kanan histogram mewakili kecerahan maksimum (putih). Jika kurva menabrak dinding kanan, artinya highlight terpotong (blown out).",
            "execution": "Tekstur gaun putih hilang menjadi putih pekat tak terbaca (clipping)."
        }
    },
    {
        "id": "tekd-lat-m-05",
        "materi": "KOMPUTER GRAFIS & VEKTOR",
        "topic": "Operasi Vektor: Pathfinder Minus Front vs Exclude",
        "stem": "Dua objek geometris di Adobe Illustrator, yaitu sebuah lingkaran merah di lapisan atas dan kotak biru di lapisan bawah, saling bertumpukan sebagian. Desainer ingin memotong kotak biru sehingga area yang tertimpa oleh lingkaran merah terbuang berlubang mengikuti bentuk lingkaran. Operasi Pathfinder yang wajib dieksekusi adalah...",
        "correct": "Minus Front, yang memotong dan membuang area irisan objek atas dari objek di bawahnya, sekaligus menghapus objek atas tersebut.",
        "distractors": [
            "Intersect, yang membuang seluruh bagian kedua objek dan hanya menyisakan area yang saling beririsan bertumpuk.",
            "Unite, yang menggabungkan lingkaran dan kotak menjadi satu bentuk kurva utuh tunggal dengan satu warna seragam.",
            "Exclude, yang menyisakan bagian unik kedua objek dan hanya melubangi area pertemuan tumpang tindihnya.",
            "Divide, yang memotong semua objek menjadi potongan-potongan terpisah di setiap garis perpotongan kanvas."
        ],
        "formula": {
            "title": "OPERASI BOOLEAN PATHFINDER VEKTOR",
            "latex": "A \\setminus B = \\{ x \\mid x \\in A \\land x \\notin B \\} \\implies \\text{Minus Front (Objek Bawah Dipotong Objek Atas)}",
            "legend": "• Unite ($A \\cup B$): Gabung total<br>• Minus Front ($A - B$): Memangkas objek latar menggunakan objek terdepan<br>• Intersect ($A \\cap B$): Hanya menyisakan irisan<br>• Exclude ($A \\oplus B$): Membuang irisan (kebalikan Intersect)"
        },
        "hints": {
            "concept": "Minus Front memotong bentuk di lapisan belakang menggunakan bentuk lapisan di depannya layaknya cetakan kue.",
            "execution": "Objek lingkaran merah di depan memotong objek kotak biru di belakang."
        }
    },
    {
        "id": "tekd-lat-m-06",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Sistem Pendaftaran Merek First to File di Indonesia",
        "stem": "Sebuah studio desain lokal telah memakai nama merek 'KREASIKU' selama lima tahun tanpa pernah mendaftarkannya ke Direktorat Jenderal Kekayaan Intelektual (DJKI). Tiba-tiba pengusaha lain mendaftarkan merek 'KREASIKU' untuk kelas usaha sejenis ke DJKI dan sertifikatnya terbit. Berdasarkan hukum merek di Indonesia (UU No. 20 Tahun 2016), konsekuensi yuridisnya adalah...",
        "correct": "Hak atas merek menjadi milik pengusaha yang baru mendaftar karena Indonesia menganut sistem 'First to File', di mana perlindungan hukum diberikan kepada pihak pertama yang mengajukan permohonan pendaftaran.",
        "distractors": [
            "Studio desain lokal secara otomatis memenangkan kepemilikan merek karena menganut sistem 'First to Use' tanpa syarat pendaftaran tertulis.",
            "Kedua belah pihak diwajibkan oleh DJKI untuk menggabungkan perusahaan mereka menjadi satu badan usaha milik negara.",
            "Sertifikat merek pengusaha baru otomatis gugur demi hukum karena durasi penggunaan usaha studio lokal sudah melampaui lima tahun.",
            "Merek 'KREASIKU' disita oleh kementerian kominfo dan diubah statusnya menjadi lisensi umum gratis untuk seluruh rakyat."
        ],
        "formula": {
            "title": "PRINSIP HUKUM MEREK (UU NO. 20 TAHUN 2016)",
            "latex": "\\text{Perlindungan Merek} = \\text{Sistem First-to-File (Bukan First-to-Use)} \\implies \\text{Pendaftar Pertama Berhak Mutlak}",
            "legend": "• First to File: Hak eksklusif timbul sejak tanggal permohonan pendaftaran resmi<br>• Masa Berlaku: 10 tahun dan dapat diperpanjang seterusnya<br>• Risiko: Brand yang tidak didaftarkan rentan diambil pihak lain secara legal"
        },
        "hints": {
            "concept": "Di Indonesia, hak merek menganut sistem konstitutif 'First to File' (siapa cepat mendaftar, dialah yang sah secara hukum), bukan 'First to Use'.",
            "execution": "Pengusaha yang mendaftar secara sah di DJKI menjadi pemilik legal merek tersebut."
        }
    },
    {
        "id": "tekd-lat-m-07",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Carpal Tunnel Syndrome & Solusi Ergonomis Mouse/Tablet",
        "stem": "Seorang ilustrator digital mengalami kesemutan, mati rasa, dan nyeri hebat pada pergelangan tangan kanannya yang menjalar ke jempol dan jari telunjuk akibat penggunaan mouse komputer konvensional secara berulang selama bertahun-tahun. Gangguan kesehatan kerja tersebut dan langkah ergonomis pencegahannya adalah...",
        "correct": "Carpal Tunnel Syndrome (CTS) akibat kompresi saraf medianus; solusinya adalah mengganti mouse konvensional dengan vertical ergonomic mouse atau pen tablet grafis dengan posisi pergelangan netral.",
        "distractors": [
            "Tendinitis Patela; solusinya adalah memasang alas mouse berbahan logam besi berdaya magnet tinggi pada lantai studio.",
            "Presbiopi Dini; solusinya adalah menaikkan resolusi monitor dan memakai kacamata lensa silinder anti radiasi matahari.",
            "Skoliosis Akut; solusinya adalah berdiri tegak di atas satu kaki sambil memegang mouse di udara tanpa bertumpu pada meja.",
            "Bursitis Bahu; solusinya adalah mencelupkan pergelangan tangan ke dalam tinta cetak dingin sebelum mulai bekerja."
        ],
        "formula": {
            "title": "ERGONOMI PERGELANGAN TANGAN & CTS",
            "latex": "\\text{Repetitive Strain Injury (RSI)} \\implies \\text{Tekanan Saraf Medianus} \\implies \\text{CTS}",
            "legend": "• Pronasi Ekstrem: Mouse datar memaksa pergelangan tangan terpelintir datar $90^\\circ$<br>• Vertical Mouse / Pen Tablet: Mempertahankan posisi 'handshake position' alami<br>• Netral: Mencegah jepitan pada carpal tunnel pergelangan tangan"
        },
        "hints": {
            "concept": "Rasa kebas pada ibu jari dan telunjuk akibat beban berulang mouse adalah sindrom lorong karpal (Carpal Tunnel Syndrome).",
            "execution": "Vertical mouse atau graphic tablet menempatkan pergelangan tangan dalam posisi jabat tangan netral."
        }
    },
    {
        "id": "tekd-lat-m-08",
        "materi": "DESAIN MEDIA & KEMASAN",
        "topic": "Pemilihan Bahan Karton Kemasan (Gramatur & Karakteristik)",
        "stem": "Sebuah pabrik lampu bohlam LED kaca ingin merancang kemasan kotak satuan yang murah, namun memiliki daya tahan benturan yang baik saat ditumpuk di dalam kardus ekspedisi logistik. Jenis dan gramatur bahan karton yang paling tepat untuk kemasan pelindung produk tersebut adalah...",
        "correct": "Corrugated cardboard gelombang mikro (E-flute / F-flute), yang memiliki struktur lapisan gelombang di bagian tengah untuk menyerap gaya benturan dan getaran mekanis.",
        "distractors": [
            "Kertas HVS 70 GSM tipis, karena permukaannya yang sangat halus mempermudah proses pengeleman otomatis tanpa mesin press.",
            "Kertas Samson Kraft 80 GSM tanpa lapisan penahan, karena bahan ini paling mudah sobek saat terkena tetesan air hujan.",
            "Kertas Art Paper 120 GSM yang dilaminasi doff dua sisi, karena ketebalannya setara dengan balok kayu jati solid.",
            "Kertas kalkir transparan 60 GSM, agar konsumen dapat melihat filamen lampu secara langsung dari luar kemasan."
        ],
        "formula": {
            "title": "KLASIFIKASI BAHAN KEMASAN KARTON",
            "latex": "\\text{Impact Resistance} \\propto \\text{Fluting Structure (Corrugated E/F Flute)}",
            "legend": "• Duplex/Ivory ($250-350$ GSM): Kotak farmasi/kosmetik ringan (estetika tinggi)<br>• Corrugated (Karton Bergelombang): Bantalan udara peredam getaran dan benturan fisik<br>• E-Flute: Gelombang mikro ($1.1-1.8$ mm), ideal untuk die-cut kemasan kecil tapi tangguh"
        },
        "hints": {
            "concept": "Untuk barang mudah pecah seperti bohlam kaca yang ditumpuk, diperlukan lapisan karton bergelombang (corrugated) untuk meredam impak.",
            "execution": "E-flute corrugated cardboard menggabungkan kemampuan cetak die-cut dengan daya serap benturan."
        }
    },
    {
        "id": "tekd-lat-m-09",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Teknik Trapping (Overprint vs Knockout)",
        "stem": "Dalam proses cetak offset separasi, teks berwarna hitam kecil ($K=100\\%$) dicetak di atas latar belakang bidang warna biru pekat ($C=100, M=80$). Jika desainer mengatur teks hitam tersebut dengan perintah 'Knockout' dan terjadi pergeseran mekanis plat mesin cetak sebesar 0.2 mm, apa cacat visual yang akan terlihat pada hasil cetakan?",
        "correct": "Muncul garis putih tak bertinta (misregistration gap) di sekeliling pinggiran huruf hitam karena plat warna latar berlubang tidak pas berhimpitan dengan teks.",
        "distractors": [
            "Teks hitam secara otomatis meleleh dan menyatu menjadi warna emas berkilau di atas permukaan kertas cetak.",
            "Warna biru pada latar belakang berubah menjadi merah muda menyala karena pengaruh radiasi tinta hitam.",
            "Plat cetak silinder mesin offset langsung patah menjadi dua bagian akibat ketegangan tegangan permukaan tinta.",
            "Seluruh huruf hitam tercetak miring 45 derajat mengikuti arah putaran roda mesin cetak offset."
        ],
        "formula": {
            "title": "TRAPPING PRE-PRESS: OVERPRINT VS KNOCKOUT",
            "latex": "\\text{Text } K=100 \\implies \\text{Wajib OVERPRINT (Bukan Knockout)} \\implies \\text{Celah Putih} = 0",
            "legend": "• Knockout: Melubangi warna di bawahnya (berbahaya jika plat meleset tipis $\\implies$ celah putih)<br>• Overprint: Mencetak langsung di atas warna dasar (tinta hitam menimpa tanpa melubangi)<br>• Trapping: Tumpang tindih mikro (0.1 pt) antara warna berdampingan"
        },
        "hints": {
            "concept": "Teks hitam kecil harus diatur OVERPRINT, bukan KNOCKOUT. Jika di-knockout dan plat cetak bergeser mikro, timbul celah putih bocor.",
            "execution": "Cacat celah putih di sekeliling teks akibat pergeseran plat cetak disebut misregistration gap."
        }
    },
    {
        "id": "tekd-lat-m-10",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Karakteristik X-Height & Readability Ukuran Font Kecil",
        "stem": "Dua jenis font berbeda, yaitu Helvetica dan Garamond, dicetak pada ukuran yang sama persis (10 pt) di atas media kertas petunjuk pemakaian obat. Namun, huruf Helvetica terlihat jauh lebih besar, lebih kokoh, dan lebih mudah terbaca dari jarak baca normal. Faktor anatomi tipografi utama yang menyebabkan perbedaan persepsi visual tersebut adalah...",
        "correct": "Helvetica memiliki nilai x-height (proporsi tinggi huruf kecil) yang jauh lebih tinggi dibandingkan Garamond, sehingga 'badan' hurufnya tampak lebih dominan dan terbuka pada ukuran kecil.",
        "distractors": [
            "Garamond tidak memiliki garis dasar (baseline) sehingga huruf-hurufnya melayang secara acak di luar grid paragraf.",
            "Helvetica menggunakan ruang warna Adobe RGB 1998 yang secara otomatis mempertebal stroke huruf saat diekspor ke PDF.",
            "Garamond diciptakan khusus untuk layar bioskop 70mm sehingga tidak boleh dicetak di atas kertas di bawah ukuran 50 pt.",
            "Helvetica memiliki nilai ascender dan descender yang sepuluh kali lebih panjang daripada tinggi huruf kapitalnya."
        ],
        "formula": {
            "title": "ANATOMI TIPOGRAFI: X-HEIGHT RATIO",
            "latex": "\\text{Readability pada Ukuran Kecil} \\propto \\frac{\\text{X-Height}}{\\text{Cap Height}}",
            "legend": "• X-Height: Ketinggian badan huruf kecil non-ascender (seperti x, o, a, e, n)<br>• Large X-Height (e.g. Helvetica, Segoe UI): Terbaca lebih besar dan jelas pada teks kecil/UI<br>• Small X-Height (e.g. Garamond, Bodoni): Lebih anggun dan klasik, tapi butuh ukuran pt lebih besar"
        },
        "hints": {
            "concept": "X-height adalah tinggi badan huruf kecil (seperti x, a, e). Font dengan x-height besar terlihat jauh lebih besar dan jelas pada ukuran poin kecil.",
            "execution": "Helvetica memiliki proporsi x-height yang tinggi dibanding Garamond pada ukuran 10 pt yang sama."
        }
    },
    {
        "id": "tekd-lat-m-11",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Color Temperature (Kelvin) & White Balance",
        "stem": "Seorang fotografer memotret suasana makan malam di sebuah restoran mewah yang diterangi oleh lampu pijar bohlam pijar kuning (tungsten). Jika fotografer membiarkan pengaturan White Balance kamera pada preset 'Daylight' (5600K), hasil foto akan tampak sangat kekuning-kuningan (orange cast). Pengaturan White Balance yang benar untuk menetralkan warna agar pakaian putih subjek tampak putih alami adalah...",
        "correct": "Mengubah preset White Balance ke 'Tungsten / Incandescent' (sekitar 3200K) atau mengkalibrasi manual dengan abu-abu netral (Grey Card 18%).",
        "distractors": [
            "Mengubah White Balance ke mode 'Shade' (7500K) yang akan menambahkan lebih banyak warna jingga hangat ke dalam sensor.",
            "Menaikkan nilai ISO dari 100 menjadi 12.800 untuk membakar kelebihan suhu warna kuning pada lensa optik.",
            "Mematikan sensor inframerah kamera dan membiarkan diafragma lensa terbuka pada mode makro f/1.4.",
            "Mengganti kartu memori SD card dengan jenis berkecepatan UHS-II kelas 10 khusus pemotretan luar ruangan."
        ],
        "formula": {
            "title": "SUHU WARNA (KELVIN) & WHITE BALANCE",
            "latex": "T_{\\text{Tungsten}} \\approx 3200\\,\\text{K} \\implies \\text{WB Kamera Menambahkan Spektrum Biru untuk Kompensasi Netral}",
            "legend": "• 2500K - 3200K: Lilin & Lampu Pijar Rumah (Kuning/Jingga Hangat)<br>• 5500K - 5600K: Cahaya Matahari Siang Hari (Daylight Netral)<br>• 7000K - 9000K: Langit Berawan / Bayangan Mendung (Biru Dingin)"
        },
        "hints": {
            "concept": "White Balance mengkompensasi suhu warna ruangan. Lampu pijar bersuhu rendah (~3200K, kekuningan); kamera mengoreksinya dengan menambahkan warna biru.",
            "execution": "Pilih preset Tungsten/Incandescent (3200K) atau custom white balance menggunakan grey card 18%."
        }
    },
    {
        "id": "tekd-lat-m-12",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Gestalt Law of Closure pada Desain Identitas",
        "stem": "Logo terkenal World Wildlife Fund (WWF) berupa siluet panda hitam-putih tidak memiliki garis tepi luar penutup pada bagian punggung dan kepalanya. Namun, mata manusia yang melihat logo tersebut secara otomatis menangkap bentuk tubuh panda yang utuh dan solid. Prinsip Gestalt yang bekerja dalam fenomena persepsi ini adalah...",
        "correct": "Law of Closure, di mana otak manusia secara otomatis mengisi celah kosong atau bentuk yang tidak lengkap untuk menciptakan persepsi visual satu objek yang utuh.",
        "distractors": [
            "Law of Proximity, di mana objek-objek grafis yang saling berjauhan dianggap memiliki ikatan batin yang sama oleh pengamat.",
            "Law of Similarity, di mana bentuk kotak dan lingkaran selalu dianggap setara oleh otak manusia tanpa membedakan warna.",
            "Law of Symmetry, di mana separuh tubuh panda wajib dicerminkan secara identik menggunakan sumbu cermin kartesian.",
            "Law of Common Fate, di mana seluruh bagian logo bergerak ke satu arah koordinat vektor yang sama secara kinetik."
        ],
        "formula": {
            "title": "GESTALT LAW OF CLOSURE (PENUTUPAN BENTUK)",
            "latex": "\\text{Bentuk Terbuka (Gaps)} + \\text{Kognisi Manusia} \\implies \\text{Persepsi Objek Utuh Sempurna}",
            "legend": "• Closure: Kecenderungan kognitif menutup celah tak tersambung<br>• Keuntungan Logo: Memancing keterlibatan mental audiens (engaging visual)<br>• Contoh: WWF Panda, IBM horizontal bars, logo Carrefour"
        },
        "hints": {
            "concept": "Closure terjadi saat otak kita melengkapi potongan-potongan informasi visual yang terputus menjadi satu bentuk utuh.",
            "execution": "Punggung panda terbuka yang secara spontan disatukan oleh pikiran pengamat adalah contoh klasik Law of Closure."
        }
    },
    {
        "id": "tekd-lat-m-13",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "12 Prinsip Animasi: Squash & Stretch",
        "stem": "Dalam pembuatan animasi gerak (motion graphics) bola karet yang memantul di lantai, bentuk bola tampak gepeng melebar secara elastis saat menyentuh lantai beton, lalu memanjang lonjong saat melesat kembali ke udara. Prinsip fundamental animasi yang diterapkan oleh animator untuk memberi kesan massa, elastisitas, dan bobot tersebut adalah...",
        "correct": "Squash and Stretch, di mana objek mengalami peregangan dan penekanan bentuk untuk memperlihatkan fleksibilitas tanpa mengubah volume total objek.",
        "distractors": [
            "Anticipation, yaitu ancang-ancang gerakan berlawanan arah sebelum karakter melakukan aksi lompatan besar.",
            "Staging, yaitu pengaturan posisi kamera dan tata lampu agar aksi karakter terlihat jelas di layar tanpa distraksi.",
            "Follow Through, yaitu gerakan bagian rambut dan pakaian yang tetap melayang maju beberapa saat setelah tubuh berhenti bergerak.",
            "Slow In and Slow Out, yaitu penambahan jumlah frame pada awal dan akhir gerakan agar gerakan terasa lebih mulus dan natural."
        ],
        "formula": {
            "title": "PRINSIP ANIMASI DISNEY: SQUASH & STRETCH",
            "latex": "V_{\\text{bola}} = \\text{Konstan} \\implies \\Delta x \\times \\Delta y \\times \\Delta z = C",
            "legend": "• Squash: Menekan/menggepeng saat membentur permukaan keras<br>• Stretch: Meregang panjang searah garis laju kinetik<br>• Volume Tetap: Jika melebar horizontal, tinggi vertikal harus berkurang proporsional"
        },
        "hints": {
            "concept": "Squash & stretch adalah prinsip paling vital dari 12 prinsip animasi untuk memberikan ilusi elastisitas dan massa benda lentur.",
            "execution": "Bola gepeng saat mendarat dan lonjong saat melesat menggambarkan Squash and Stretch."
        }
    },
    {
        "id": "tekd-lat-m-14",
        "materi": "DESAIN MEDIA & KEMASAN",
        "topic": "Aksesibilitas UI/UX: Standar Kontras Rasio WCAG 2.1",
        "stem": "Seorang desainer UI merancang tombol konfirmasi transaksi aplikasi dompet digital dengan teks abu-abu muda (#AAAAAA) di atas latar belakang tombol putih bersih (#FFFFFF). Berdasarkan pedoman aksesibilitas Web Content Accessibility Guidelines (WCAG 2.1 Level AA), desain tombol tersebut gagal memenuhi standar karena...",
        "correct": "Rasio kontras warna antara teks normal dan latar belakangnya jauh di bawah ambang minimum 4.5:1, sehingga menyulitkan pengguna dengan gangguan penglihatan atau di bawah terik matahari.",
        "distractors": [
            "Aplikasi perbankan dilarang menggunakan warna putih karena dapat meningkatkan konsumsi baterai layar OLED secara drastis.",
            "Teks pada tombol konfirmasi transaksi wajib dibuat berkedip (blinking) sebanyak 10 kali per detik menurut standar ISO.",
            "Tombol digital wajib memiliki ketebalan bayangan drop shadow minimal 50 piksel pada sistem operasi Android.",
            "WCAG 2.1 melarang penggunaan font non-latin untuk seluruh aplikasi finansial di Asia Tenggara."
        ],
        "formula": {
            "title": "STANDAR AKSESIBILITAS WCAG 2.1 LEVEL AA",
            "latex": "\\text{Rasio Kontras} = \\frac{L_1 + 0.05}{L_2 + 0.05} \\ge 4.5:1 \\quad (\\text{Teks Normal}), \\quad \\ge 3:1 \\quad (\\text{Teks Besar } \\ge 18\\,\\text{pt})",
            "legend": "• $L_1, L_2$: Luminansi relatif warna terang dan gelap ($0.0 - 1.0$)<br>• Abu-abu muda di atas putih hanya memiliki rasio $\\approx 2.3:1$ (Gagal AA)<br>• Teks harus kontras agar inklusif bagi tunanetra parsial/lansia"
        },
        "hints": {
            "concept": "Standar WCAG 2.1 Level AA mewajibkan rasio kontras warna teks normal terhadap latarnya minimal 4.5:1.",
            "execution": "Teks abu-abu muda di atas putih memiliki kontras sangat rendah, gagal memenuhi standar WCAG 4.5:1."
        }
    },
    {
        "id": "tekd-lat-m-15",
        "materi": "KOMPUTER GRAFIS & VEKTOR",
        "topic": "Clipping Mask vs Opacity Mask",
        "stem": "Seorang desainer grafis ingin memasukkan foto lanskap pegunungan ke dalam bentuk huruf kapital 'B' secara presisi, sehingga gambar foto pegunungan hanya terlihat di dalam lekukan tubuh huruf 'B'. Fitur manipulasi objek vektor di software desain grafis yang paling tepat dan efisien digunakan adalah...",
        "correct": "Clipping Mask, di mana objek vektor huruf 'B' di posisi teratas berfungsi sebagai bingkai pembatas tampak (mask) bagi foto di bawahnya.",
        "distractors": [
            "Rasterize Image, yang mengubah seluruh kanvas kerja menjadi gambar bitmap hitam-putih 1-bit.",
            "Envelope Distort Mesh, yang menarik dan merusak sudut-sudut foto pegunungan secara acak dengan kisi 4x4.",
            "Trace Image Black and White, yang menghapus seluruh foto pegunungan dan menggantinya dengan siluet hitam pekat.",
            "Simplify Path, yang mengurangi jumlah titik koordinat jangkar hingga bentuk huruf 'B' menjadi segitiga lancip."
        ],
        "formula": {
            "title": "PRINSIP VEKTOR CLIPPING MASK",
            "latex": "\\text{Layer Visible Area} = \\text{Aset Grafis (Bawah)} \\cap \\text{Vektor Mask Shape (Atas)}",
            "legend": "• Top Object: Berfungsi sebagai batas 'jendela' (clipping path)<br>• Bottom Object: Konten gambar/foto yang di-masking<br>• Sifat: Non-destruktif (foto asli tetap utuh dan dapat digeser di dalam frame)"
        },
        "hints": {
            "concept": "Clipping Mask mengunci objek di bawahnya agar hanya terlihat di dalam area bentuk vektor yang berada tepat di atasnya.",
            "execution": "Bentuk huruf 'B' di layer atas meng-klip foto pegunungan di layer bawah."
        }
    },
    {
        "id": "tekd-lat-m-16",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Perspektif Lensa: Focal Length (Wide vs Telephoto)",
        "stem": "Dalam pemotretan foto potret wajah (close-up portrait), fotografer menghindari penggunaan lensa sudut lebar (ultra-wide 18mm) dari jarak dekat dan lebih memilih lensa telephoto menengah (85mm atau 105mm). Alasan optis utama pemilihan panjang fokus (focal length) tersebut adalah...",
        "correct": "Lensa sudut lebar dari jarak dekat menimbulkan distorsi barel yang membuat hidung dan bagian tengah wajah tampak membesar tidak proporsional, sedangkan lensa 85mm menghasilkan proporsi wajah yang rata dan natural.",
        "distractors": [
            "Lensa 85mm secara otomatis memancarkan sinar laser pemutih kulit wajah saat tombol shutter ditekan separuh.",
            "Lensa sudut lebar 18mm memiliki bobot fisik 10 kali lebih berat daripada lensa telephoto studio 105mm.",
            "Lensa telephoto tidak memerlukan baterai kamera sama sekali karena bekerja berdasarkan hukum pantulan cermin datar.",
            "Lensa sudut lebar hanya dapat menangkap gambar berwarna hitam-putih tanpa saturasi warna kulit manusia."
        ],
        "formula": {
            "title": "DISTORSI PERSPEKTIF & FOCAL LENGTH",
            "latex": "f < 24\\,\\text{mm} \\implies \\text{Barrel Distortion (Peregangan Pusat)}, \\quad f = 85-105\\,\\text{mm} \\implies \\text{Flattering Portrait Compression}",
            "legend": "• Wide Lens ($< 35$ mm): Melebarkan perspektif (jarak dekat membuat hidung membesar)<br>• Standard Lens ($50$ mm): Setara sudut pandang mata manusia normal<br>• Portrait Tele ($85-135$ mm): Mengompresi latar belakang dan mempertahankan proporsi wajah asli"
        },
        "hints": {
            "concept": "Lensa sudut lebar dari jarak dekat mendistorsi wajah (efek mata ikan/hidung besar). Lensa 85-105mm memberikan proporsi wajah paling alami dan indah.",
            "execution": "Pilih jawaban yang menjelaskan distorsi barel pada lensa lebar vs proporsi wajah natural pada focal length 85mm."
        }
    },
    {
        "id": "tekd-lat-m-17",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Karakteristik Kertas: Coated vs Uncoated & Dot Gain",
        "stem": "Ketika mencetak katalog foto produk mebel jati di atas kertas koran berserat kasar tanpa lapisan (uncoated paper), warna foto tampak jauh lebih gelap dan detail bayangan kayu menjadi pekat tersumbat dibandingkan saat dicetak di atas kertas Art Paper licin (coated paper). Fenomena fisik percetakan ini terjadi akibat...",
        "correct": "Dot gain tinggi pada kertas uncoated, di mana tinta cair merembes dan melebar ke serat-serat pori kertas sehingga titik raster halftone membesar dan meningkatkan densitas kegelapan gambar.",
        "distractors": [
            "Kertas koran memantulkan 99% cahaya matahari langsung sehingga lensa mata manusia mengalami kebutaan sesaat.",
            "Mesin cetak offset secara otomatis menyemprotkan cat pernis tebal pada kertas koran untuk mencegah kebakaran.",
            "Pigmen tinta Cyan dan Yellow saling bertabrakan dan membentuk medan magnet statis di permukaan kertas uncoated.",
            "Resolusi plat cetak offset pada kertas koran dipaksa turun dari 300 DPI menjadi 1 DPI oleh komputer RIP."
        ],
        "formula": {
            "title": "FENOMENA PRE-PRESS: DOT GAIN PADA KERTAS",
            "latex": "\\text{Dot Gain} = \\text{Ukuran Titik Efektif pada Kertas} - \\text{Ukuran Titik Asli pada Plat Cetak}",
            "legend": "• Coated Paper (Art Paper): Dot gain rendah ($10-15\\%$, permukaan licin menahan tinta di atas)<br>• Uncoated Paper (HVS/Koran): Dot gain tinggi ($25-35\\%$, tinta meresap melebar ke pori serat)<br>• Kompensasi RIP: Kurangi densitas kurva raster sebelum ekspos plat"
        },
        "hints": {
            "concept": "Kertas tanpa lapisan (uncoated/koran) menyerap tinta seperti spons, membuat titik-titik tinta melebar (dot gain), sehingga cetakan tampak lebih gelap.",
            "execution": "Dot gain tinggi akibat perembesan tinta ke dalam serat pori kertas uncoated."
        }
    },
    {
        "id": "tekd-lat-m-18",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Desain Industri (UU No. 31 Tahun 2000)",
        "stem": "Sebuah produsen botol parfum merancang bentuk fisik botol kaca 3 dimensi yang unik dengan lekukan asimetris futuristik dan tutup botol berbentuk kristal bersegi delapan. Agar bentuk rancangan fisik botol tersebut tidak ditiru atau dicetak ulang oleh produsen kompetitor, jenis perlindungan HAKI yang tepat didaftarkan adalah...",
        "correct": "Desain Industri, yang melindungi kreasi tentang bentuk, konfigurasi, atau komposisi garis dan warna berbentuk tiga dimensi atau dua dimensi yang memberikan kesan estetis pada suatu komoditas.",
        "distractors": [
            "Hak Rahasia Dagang, yang melindungi formula resep kimia cairan parfum agar tidak dibocorkan oleh mantan karyawan pabrik.",
            "Paten Sederhana, yang melindungi mekanisme mesin hidrolik otomatis pembuat kaca di dalam tungku peleburan baja.",
            "Hak Cipta Musik, yang melindungi alunan nada jingle iklan radio produk parfum yang disiarkan di stasiun radio komersial.",
            "Perlindungan Varietas Tanaman, yang melindungi jenis bibit bunga melati yang diekstrak menjadi minyak wangi esensial."
        ],
        "formula": {
            "title": "RUANG LINGKUP DESAIN INDUSTRI (UU 31/2000)",
            "latex": "\\text{Desain Industri} \\implies \\text{Bentuk/Konfigurasi Estetis Produk Fisik 2D/3D (Masa Perlindungan: 10 Tahun)}",
            "legend": "• Objek: Penampilan visual luar produk komersial (botol, velg, casing ponsel)<br>• Syarat: Memiliki nilai kebaruan (novelty) dan tidak bertentangan dengan kesusilaan<br>• Paten vs Desain Industri: Paten = Fungsi teknologi/cara kerja; Desain Industri = Estetika bentuk fisik"
        },
        "hints": {
            "concept": "Perlindungan atas kreasi bentuk, konfigurasi, atau komposisi 3 dimensi suatu produk komersial diatur dalam rezim Desain Industri.",
            "execution": "Bentuk fisik estetik botol parfum 3D dilindungi di bawah UU Desain Industri."
        }
    },
    {
        "id": "tekd-lat-m-19",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Tipologi Brand Architecture (House of Brands vs Branded House)",
        "stem": "Perusahaan multinasional consumer goods Unilever memproduksi berbagai merek produk seperti sabun Lifebuoy, deterjen Rinso, kecap Bango, dan es krim Wall's, di mana masing-masing merek tampil independen dengan identitas visual mandiri tanpa menonjolkan logo induk Unilever di bagian depan kemasan. Strategi arsitektur merek ini disebut...",
        "correct": "House of Brands (Pluralistic), di mana perusahaan induk menaungi portofolio berbagai merek independen yang berdiri sendiri dengan target audiens dan citra spesifik masing-masing.",
        "distractors": [
            "Branded House (Monolithic), di mana seluruh lini produk menggunakan satu nama dan logo merek induk tunggal seperti Virgin atau FedEx.",
            "Endorsed Brand, di mana logo merek anak selalu disertai kalimat pengesahan merek induk seperti 'Courtyard by Marriott'.",
            "Co-Branding Aliansi, di mana dua perusahaan berbeda bergabung memproduksi satu produk kolaborasi terbatas.",
            "Generic Branding, di mana produk dijual dalam wadah kardus polos tanpa label nama dan tanpa logo apa pun."
        ],
        "formula": {
            "title": "STRATEGI ARSITEKTUR MEREK (BRAND ARCHITECTURE)",
            "latex": "\\text{Arsitektur Merek} = \\begin{cases} \\text{Branded House (Virgin, Apple, FedEx)} \\\\ \\text{Endorsed Brand (PlayStation by Sony, Marriott)} \\\\ \\text{House of Brands (Unilever, P\\&G, Indofood)} \\end{cases}",
            "legend": "• House of Brands: Merek independen terlindung jika salah satu brand gagal/krisis<br>• Branded House: Efisiensi biaya promosi, tapi risiko reputasi merembet ke seluruh produk<br>• Fungsi DKV: Menciptakan diferensiasi visual kontras antar anak merek"
        },
        "hints": {
            "concept": "House of Brands memayungi banyak merek independen yang memiliki identitas visualnya sendiri (contoh: Unilever, P&G).",
            "execution": "Lifebuoy, Rinso, Bango yang memiliki logo sendiri-sendiri berada di bawah model House of Brands."
        }
    },
    {
        "id": "tekd-lat-m-20",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Nirmana Trimatra: Serial Planes (Rangkaian Bidang Berseri)",
        "stem": "Dalam perancangan paviliun instalasi pameran arsitektur grafis, desainer menyusun puluhan lembar papan kayu tipis dua dimensi yang dipotong dengan bentuk kontur bergradasi dan dijejerkan secara sejajar dengan jarak spasi tertentu. Hasil susunan tersebut menciptakan ilusi bentuk gelombang 3 dimensi yang dinamis saat dilalui pengunjung. Konsep dasar Nirmana ruang ini dikenal sebagai...",
        "correct": "Serial Planes (Bidang Berseri), yaitu metode konstruksi trimatra di mana pengulangan dan perubahan bertahap bentuk bidang dua dimensi membentuk ilusi massa dan ruang volumetrik.",
        "distractors": [
            "Linear Framework, yaitu penyusunan rangka kubus hanya menggunakan batang-batang kawat besi tanpa permukaan bidang.",
            "Planar Polyhedron, yaitu pembuatan bentuk benda padat geometris tertutup bersisi banyak seperti prisma dan ikosahedron.",
            "Tessellation Monokrom, yaitu penataan ubin keramik datar tanpa celah spasi sama sekali di atas permukaan lantai dua dimensi.",
            "Möbius Strip, yaitu lingkaran pita satu sisi tak terhingga yang tidak memiliki batas permukaan atas dan bawah."
        ],
        "formula": {
            "title": "KONSTRUKSI NIRMANA TRIMATRA: SERIAL PLANES",
            "latex": "\\sum_{i=1}^n \\text{Bidang 2D}_i (\\Delta z, \\Delta \\text{skala}, \\Delta \\theta) \\implies \\text{Ilusi Volume 3D Dinamis}",
            "legend": "• Serial Planes: Setiap bidang mewakili 'irisan tipis' dari bentuk 3 dimensi utuh<br>• Variasi: Pergeseran posisi (displacement), rotasi sudut, atau graduasi ukuran<br>• Aplikasi: Desain interior modern, instalasi parametrik arsitektur, trophy design"
        },
        "hints": {
            "concept": "Serial Planes menyusun lembaran bidang 2 dimensi berjejer dengan variasi kontur bertahap untuk membangun volume 3 dimensi.",
            "execution": "Papan-papan sejajar pembentuk gelombang spasial adalah teknik Serial Planes (Bidang Berseri)."
        }
    },
    {
        "id": "tekd-lat-m-21",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Prinsip Font Pairing (Penyandingan Dua Jenis Huruf)",
        "stem": "Seorang desainer grafis diminta merancang identitas visual poster festival teater klasik modern. Ia ingin memasangkan dua jenis font yang berbeda untuk judul utama dan teks isi. Pendekatan perancangan tipografi yang paling disarankan untuk menciptakan keharmonisan tanpa konflik visual (font discord) adalah...",
        "correct": "Menciptakan kontras yang terukur dan berimbang, misalnya memadukan font Display/Serif klasik yang kaya karakter untuk judul dengan font Sans-Serif netral ber-readability tinggi untuk teks isi.",
        "distractors": [
            "Menggunakan dua jenis font yang bentuk dan karakteristiknya hampir mirip persis, seperti Arial dan Helvetica, secara berdampingan di baris yang sama.",
            "Menggabungkan minimal tujuh jenis font dekoratif yang sangat rumit dan penuh ornamen dalam satu paragraf pendek teks isi.",
            "Mengubah setiap huruf vokal menjadi font huruf sambung (script) dan huruf konsonan menjadi font balok gothic tebal.",
            "Menggunakan font Comic Sans berukuran 48 pt dengan warna kuning neon untuk seluruh naskah narasi festival teater."
        ],
        "formula": {
            "title": "PRINSIP EMAS FONT PAIRING",
            "latex": "\\text{Visual Harmony} = \\text{Clear Contrast} \\gg \\text{Similarity (Discord / Konflik Visual)}",
            "legend": "• Aturan 1: Hindari 2 font yang mirip tapi berbeda (misal: Arial + Helvetica terlihat seperti salah ketik)<br>• Aturan 2: Gunakan pasangan komplementer (Serif Headline + Sans-Serif Body)<br>• Aturan 3: Batasi maksimal 2-3 jenis typeface dalam satu kesatuan sistem desain"
        },
        "hints": {
            "concept": "Font pairing sukses menuntut kontras yang jelas dan harmonis (misal Serif judul + Sans-Serif body teks). Jangan pakai 2 font yang mirip tipis.",
            "execution": "Kontras terukur: Headline ekspresif dipadukan dengan Sans-Serif netral untuk teks isi."
        }
    },
    {
        "id": "tekd-lat-m-22",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Pengolahan Limbah B3 Industri Percetakan DKV",
        "stem": "Dalam operasional laboratorium percetakan offset di SMK jurusan DKV, kegiatan pencucian rol silinder tinta mesin cetak menghasilkan cairan sisa pelarut kimia dan residu tinta berbasis hidrokarbon. Berdasarkan regulasi K3LH dan lingkungan hidup (AMDAL), prosedur penanganan limbah cair berbahaya tersebut adalah...",
        "correct": "Menampung cairan sisa pelarut dan tinta ke dalam drum tertutup berlabel khusus B3 (Bahan Berbahaya dan Beracun) untuk diserahkan kepada pihak pengolah limbah B3 berlisensi resmi, bukan dibuang ke saluran air umum.",
        "distractors": [
            "Menyiramkan seluruh cairan sisa pelarut ke tanaman taman sekolah sebagai pupuk cair penyubur daun bunga.",
            "Membuang langsung cairan pelarut kimia ke wastafel toilet siswa agar larut dan hanyut bersama air selokan umum.",
            "Membakar cairan sisa pelarut di dalam ruang kelas tertutup menggunakan korek api saat jam istirahat sekolah.",
            "Mencampurkan sisa pelarut kimia dengan air minum galon untuk dikonsumsi sebagai penambah stamina kerja malam."
        ],
        "formula": {
            "title": "MANAJEMEN LIMBAH B3 PERCETAKAN (PP NO. 22 TAHUN 2021)",
            "latex": "\\text{Residu Tinta/Pelarut} \\in \\text{Limbah B3} \\implies \\text{Penyimpanan TPS B3} \\longrightarrow \\text{Transporter Resmi Berizin LHK}",
            "legend": "• Bahaya: Mengandung VOC (Volatile Organic Compounds), logam berat, dan pelarut hidrokarbon<br>• Dilarang: Pembuangan ke drainase kota tanpa IPAL instalasi pengolahan air limbah<br>• APD Wajib: Sarung tangan nitril tebal dan respirator uap organik saat pencucian mesin"
        },
        "hints": {
            "concept": "Pelarut tinta cetak adalah limbah B3 beracun yang dilarang keras dibuang ke selokan umum. Wajib ditampung di wadah khusus B3.",
            "execution": "Tampung dalam drum khusus B3 dan diserahkan ke pengolah limbah berizin."
        }
    },
    {
        "id": "tekd-lat-m-23",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Hukum Fitts (Fitts's Law) dalam UI Mobile Design",
        "stem": "Dalam perancangan antarmuka pengguna (UI) aplikasi pesan antar makanan pada smartphone, tim UX meletakkan tombol utama 'Pesan Sekarang' di bagian bawah layar selebar jempol pengguna, bukan di sudut kiri atas layar. Penerapan prinsip ergonomi interaksi manusia dan komputer ini didasarkan pada...",
        "correct": "Hukum Fitts (Fitts's Law) dan konsep Thumb Zone, di mana waktu untuk mencapai target tombol berkurang secara signifikan jika target berukuran besar dan berada dekat dengan jangkauan gerak alami ibu jari pengguna.",
        "distractors": [
            "Hukum Moore, yang menyatakan bahwa kecepatan prosesor smartphone berlipat ganda setiap kali tombol bawah ditekan.",
            "Hukum Archimedes, yang menyatakan bahwa tombol digital akan terapung jika layar smartphone dimasukkan ke dalam air mineral.",
            "Hukum Pareto 80/20, yang melarang desainer meletakkan lebih dari 20 huruf dalam satu tombol aplikasi ponsel pintar.",
            "Hukum Gestalt Similarity, yang mewajibkan seluruh tombol antarmuka memiliki warna yang identik dengan logo sponsor."
        ],
        "formula": {
            "title": "FITTS'S LAW DALAM ERGONOMI UI MOBILE",
            "latex": "MT = a + b \\log_2 \\left( 2\\frac{D}{W} \\right) \\implies D \\downarrow, W \\uparrow \\implies \\text{Movement Time (MT)} \\downarrow",
            "legend": "• $MT$: Waktu tempuh jari menuju tombol aksi<br>• $D$: Jarak tempuh (Distance) dari posisi istirahat jempol<br>• $W$: Lebar ukuran target tombol (Width)<br>• Thumb Zone: 1/3 bagian bawah layar smartphone paling mudah diakses satu tangan"
        },
        "hints": {
            "concept": "Hukum Fitts menyatakan bahwa makin dekat dan makin besar tombol, makin cepat pengguna dapat mengekliknya. Pada ponsel, area bawah adalah area jempol alami (thumb zone).",
            "execution": "Tombol besar di bawah layar memanfaatkan Fitts's Law dan kemudahan jangkauan ibu jari (Thumb Zone)."
        }
    },
    {
        "id": "tekd-lat-m-24",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Kedalaman Bit (Bit Depth: 8-Bit vs 16-Bit) & Fenomena Color Banding",
        "stem": "Ketika seorang desainer grafis membuat gradasi warna langit senja yang sangat halus di Photoshop pada mode gambar 8-bit per channel, terlihat garis-garis patahan batas warna yang tidak mulus (color banding). Solusi teknis digital untuk mengatasi cacat gradasi garis patahan tersebut adalah...",
        "correct": "Mengubah mode kedalaman warna gambar menjadi 16-bit per channel untuk melipatgandakan jumlah level gradasi warna, atau menambahkan efek noise/dither mikro secara halus.",
        "distractors": [
            "Menurunkan resolusi dokumen kerja ke 1-bit monokrom hitam putih agar seluruh warna jingga terhapus secara permanen.",
            "Mengonversi gambar langsung ke format GIF 256 warna dengan kompresi lossy tanpa transparansi.",
            "Menyimpan file dalam format teks mentah Notepad .TXT lalu membukanya kembali di Adobe InDesign.",
            "Menaikkan kecerahan layar monitor hingga 1000 nits agar garis batas warna tidak tampak oleh pandangan mata."
        ],
        "formula": {
            "title": "KEDALAMAN BIT (BIT DEPTH) DIGITAL IMAGING",
            "latex": "\\text{Level Nada}: \\quad 8\\text{-bit} = 2^8 = 256 \\text{ level/kanal}; \\quad 16\\text{-bit} = 2^{16} = 65.536 \\text{ level/kanal}",
            "legend": "• Color Banding: Tangga warna patah-patah akibat keterbatasan kuantisasi 256 tingkatan nada<br>• 16-bit Workflow: Menghasilkan gradasi ultra-mulus tanpa garis transisi patah<br>• Dithering: Pola acak titik semu penyamar transisi banding pada mode 8-bit"
        },
        "hints": {
            "concept": "8-bit hanya punya 256 gradasi warna per kanal, memicu color banding pada langit gradasi halus. 16-bit memiliki 65.536 gradasi per kanal.",
            "execution": "Solusi: Ubah ke 16-bit per channel atau tambahkan sedikit noise/dithering penyamar garis patahan."
        }
    },
    {
        "id": "tekd-lat-m-25",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Gestalt Law of Common Fate dalam Motion Graphic",
        "stem": "Dalam sebuah animasi bumper video promosi pariwisata, sekelompok bentuk geometris segitiga acak tiba-tiba bergerak bersama-sama ke arah sudut kanan atas layar dengan kecepatan konstan, sementara elemen lingkaran lainnya bergerak ke arah bawah. Penonton secara spontan mempersepsikan kelompok segitiga tersebut sebagai satu kesatuan rombongan yang memiliki tujuan sama. Prinsip Gestalt yang melandasinya adalah...",
        "correct": "Law of Common Fate, di mana elemen-elemen visual yang bergerak bersama ke arah dan kecepatan yang sama dipersepsikan oleh otak sebagai satu kelompok atau entitas tunggal.",
        "distractors": [
            "Law of Proximity, di mana bentuk-bentuk yang diam statis selalu dianggap bergerak jika diletakkan di sudut layar.",
            "Law of Pragnanz, di mana otak manusia menolak melihat gerakan animasi dan mematikan layar proyektor.",
            "Law of Figure-Ground, di mana semua objek segitiga wajib diwarnai hitam di atas kanvas putih bertekstur.",
            "Law of Continuity, di mana desainer dilarang menganimasikan objek selain garis lurus horizontal kaku."
        ],
        "formula": {
            "title": "GESTALT LAW OF COMMON FATE (NASIB BERSAMA)",
            "latex": "\\vec{v}_i = \\vec{v}_j \\implies \\text{Persepsi Visual: } \\text{Objek}_i \\text{ dan Objek}_j \\text{ Tergabung dalam 1 Unit Sistem}",
            "legend": "• Common Fate: Khusus berlaku pada dinamika gerak kinetik (animasi, video, interaksi UI)<br>• Vektor Kecepatan Identik: Mengikat elemen terpisah menjadi satu formasi utuh (seperti kawanan burung terbang)<br>• Aplikasi UI: Elemen menu yang bergeser bersama saat tombol navigasi ditekan"
        },
        "hints": {
            "concept": "Common Fate berlaku pada animasi: objek yang bergerak bersama ke arah dan kecepatan yang sama dianggap satu kawanan/kelompok oleh persepsi otak.",
            "execution": "Segitiga yang bergerak searah ke kanan atas secara kohesif menunjukkan Law of Common Fate."
        }
    }
]
