# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Desain Komunikasi Visual (DKV / Rekayasa Desain SMK/MAK)
Dataset: Hard Practice (25 Authentic Questions, tekd-lat-h-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

DKV_HARD_ITEMS = [
    {
        "id": "tekd-lat-h-01",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Separasi Halftone & Sudut Layar (Screen Angles) Anti-Moiré",
        "stem": "Dalam proses cetak offset separasi 4 warna (CMYK), plat cetak masing-masing warna harus diatur dengan sudut raster halftone tertentu. Jika sudut layar antara dua warna kuat (seperti Cyan dan Magenta) diatur terlalu dekat dengan selisih sudut di bawah $15^\\circ$, hasil cetak akan memunculkan cacat pola interferensi geometris bergelombang yang merusak foto. Susunan sudut raster standar industri yang benar untuk meniadakan efek moiré tersebut adalah...",
        "correct": "Cyan $15^\\circ$, Magenta $75^\\circ$, Yellow $0^\\circ$ (atau $90^\\circ$), dan Black/Key $45^\\circ$ (sudut $45^\\circ$ diberikan ke warna tergelap karena paling sedikit disadari oleh orientasi mata manusia).",
        "distractors": [
            "Seluruh warna Cyan, Magenta, Yellow, dan Black diatur tepat pada sudut yang sama persis $0^\\circ$ agar titik raster saling tumpang tindih secara absolut.",
            "Cyan $0^\\circ$, Magenta $10^\\circ$, Yellow $20^\\circ$, dan Black $30^\\circ$ agar membentuk garis diagonal sejajar berurutan di seluruh permukaan kanvas.",
            "Yellow diatur pada sudut $45^\\circ$ karena merupakan warna paling gelap dan kontras, sementara Black diatur pada sudut $0^\\circ$ karena transparan.",
            "Sudut raster hanya boleh ditentukan secara acak oleh sensor panas mesin offset saat suhu ruangan mencapai 100 derajat Celsius."
        ],
        "formula": {
            "title": "STANDAR SUDUT RASTER HALFTONE (ISO 12647-2)",
            "latex": "\\Delta \\theta_{\\text{kuat}} = 30^\\circ \\implies K=45^\\circ, M=75^\\circ, C=15^\\circ, Y=0^\\circ/90^\\circ \\implies \\text{Pola Rosette Sempurna}",
            "legend": "• Moiré Effect: Pola cacat interferensi visual saat sudut kisi tumpang tindih salah<br>• Warna Terkuat (K=45°): Mata paling peka terhadap garis vertikal/horizontal, sudut $45^\\circ$ paling tidak kentara<br>• Yellow (0°): Warna terlemah dengan selisih $15^\\circ$ terhadap C dan M"
        },
        "hints": {
            "concept": "Untuk mencegah efek moiré, warna-warna kuat harus berselisih sudut minimal 30 derajat. Warna tergelap (Black) selalu di 45 derajat.",
            "execution": "Kombinasi standar: K=45°, M=75°, C=15°, Y=0° (atau 90°)."
        }
    },
    {
        "id": "tekd-lat-h-02",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "ICC Profile & Rendering Intent (Perceptual vs Relative Colorimetric)",
        "stem": "Seorang fotografer seni rupa mengonversi foto karya lukisan bernilai tinggi dari profil warna Adobe RGB 1998 ke profil cetak CMYK Coated FOGRA39 di Adobe Photoshop. Terdapat beberapa warna gradasi jenuh di luar gamut cetak CMYK. Fotografer ingin mempertahankan hubungan visual proporsional di antara seluruh gradasi warna meskipun seluruh saturasi warna sedikit diturunkan secara merata. Opsi Rendering Intent yang wajib dipilih adalah...",
        "correct": "Perceptual (Photographic), karena mengompresi seluruh gamut warna dokumen asli (baik warna di dalam maupun di luar gamut) secara proporsional sehingga hubungan harmonis gradasi visual tetap terjaga alami bagi mata.",
        "distractors": [
            "Absolute Colorimetric, yang mempertahankan titik putih asli ruangan dan membiarkan warna di luar gamut terpotong kaku tanpa kompensasi kertas.",
            "Saturation, yang memaksa seluruh warna menjadi jenuh maksimal secara hiperbolik tanpa memedulikan akurasi warna kulit manusia.",
            "Relative Colorimetric, yang hanya memotong warna di luar gamut ke batas terluar tanpa mengubah warna di dalam gamut, sehingga rentan menghilangkan detail gradasi di area jenuh.",
            "Bilinear Interpolation, yang menghapus seluruh kanal warna biru dan menggantikannya dengan kurva hitam pekat."
        ],
        "formula": {
            "title": "RENDERING INTENT DALAM COLOR MANAGEMENT SYSTEM (CMS)",
            "latex": "\\text{Perceptual}: \\quad \\mathbf{C}' = \\alpha \\cdot \\mathbf{C} \\implies \\text{Preserve Relative Relationships (Harmoni Gradasi Utuh)}",
            "legend": "• Perceptual: Seluruh warna digeser masuk proporsional (ideal untuk fotografi & seni rupa)<br>• Relative Colorimetric: Warna in-gamut tidak berubah, out-of-gamut di-clamp (ideal untuk logo & grafis vektor)<br>• Saturation: Memaksimalkan kepekatan warna (grafik bisnis / pie chart)"
        },
        "hints": {
            "concept": "Perceptual mengorbankan saturasi absolut namun mempertahankan hubungan proporsional antarsemua warna, mencegah hilangnya detail gradasi pada foto halus.",
            "execution": "Pilih Perceptual untuk kompresi proporsional seluruh spektrum warna pada karya seni fotografi."
        }
    },
    {
        "id": "tekd-lat-h-03",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Tipografi Mikro: Small Caps Asli vs Faux Small Caps",
        "stem": "Dalam tata letak buku sejarah ilmiah, desainer memerlukan huruf kapital kecil (small caps) untuk penulisan singkatan 'UNESCO' di tengah paragraf teks isi Garamond. Alih-alih mengaktifkan fitur OpenType 'True Small Caps', desainer pemula sekadar mengecilkan font kapital normal menjadi 70% secara manual (Faux Small Caps). Cacat visual tipografis yang terjadi akibat tindakan desainer pemula tersebut adalah...",
        "correct": "Ketebalan garis (stroke weight) huruf singkatan tampak jauh lebih tipis dan kurus secara timpang dibandingkan huruf-huruf kecil di sekitarnya, merusak ritme kepekatan warna visual (typographic color) paragraf.",
        "distractors": [
            "Huruf-huruf singkatan otomatis berubah posisi menjadi terbalik 180 derajat mengikuti arah jarum jam.",
            "Seluruh spasi antar kata di dalam bab tersebut otomatis terhapus dan digantikan oleh simbol tanda tanya.",
            "Komputer percetakan secara otomatis menolak mencetak buku dan mengeluarkan peringatan virus berbahaya.",
            "Tinta cetak hitam pada huruf kapital kecil tersebut meleleh dan membakar serat halaman buku."
        ],
        "formula": {
            "title": "TIPOGRAFI MIKRO: TRUE VS FAUX SMALL CAPS",
            "latex": "\\text{Stroke Weight}(\\text{True Small Caps}) = \\text{Stroke Weight}(\\text{Lowercase}) \\gg \\text{Stroke}(\\text{Faux Caps } 70\\%)",
            "legend": "• True Small Caps: Didesain khusus oleh typographer dengan stroke weight tebal setara huruf kecil x-height<br>• Faux Small Caps: Penskalaan matematis 70% yang membuat garis huruf menciut tipis pucat<br>• Typographic Color: Kepadatan dan kehitaman rata blok teks dalam satu halaman"
        },
        "hints": {
            "concept": "Mengecilkan font kapital biasa secara manual (faux) membuat batangnya menjadi terlalu kurus dibanding huruf kecil sekitarnya. True Small Caps dirancang khusus berbobot tebal seimbang.",
            "execution": "Ketebalan garis (stroke weight) menjadi terlalu tipis dan pucat merusak konsistensi warna tipografis paragraf."
        }
    },
    {
        "id": "tekd-lat-h-04",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Kalkulasi Shades of Gray pada Halftone Screening",
        "stem": "Sebuah buku foto monokrom dicetak menggunakan mesin cetak beresolusi plat 2400 DPI dengan kerapatan garis raster (screen frequency) sebesar 150 LPI. Berapakah jumlah tingkatan gradasi abu-abu (shades of gray) maksimal yang secara teoritis mampu dihasilkan oleh setiap sel halftone pada kombinasi teknis tersebut?",
        "correct": "257 tingkatan abu-abu, yang dihitung berdasarkan rumus formula $(\\text{DPI} / \\text{LPI})^2 + 1 = (2400 / 150)^2 + 1 = 16^2 + 1 = 256 + 1 = 257$.",
        "distractors": [
            "16 tingkatan abu-abu, yang hanya merupakan hasil pembagian langsung nilai 2400 DPI dengan 150 LPI tanpa dipangkatkan.",
            "150 tingkatan abu-abu, yang nilainya selalu dibatasi tepat setara dengan frekuensi garis raster LPI kertas.",
            "1024 tingkatan abu-abu, yang merupakan kapasitas memori buffer acak kartu grafis komputer desainer.",
            "64 tingkatan abu-abu, yang dihitung dari akar kuadrat frekuensi garis raster dikalikan koefisien tinta monokrom."
        ],
        "formula": {
            "title": "FORMULA TINGKATAN ABU-ABU HALFTONE",
            "latex": "\\text{Shades of Gray} = \\left( \\frac{\\text{Output Resolution (DPI)}}{\\text{Screen Frequency (LPI)}} \\right)^2 + 1",
            "legend": "• DPI: Resolusi perangkat output laser imagesetter/CtP (2400 DPI)<br>• LPI: Garis raster per inci (150 LPI)<br>• Nilai 257 $\\ge 256$ (8-bit): Menjamin gradasi abu-abu mulus sempurna tanpa efek tangga posterisasi (banding)"
        },
        "hints": {
            "concept": "Rumus jumlah gradasi abu-abu halftone cetak adalah $(DPI/LPI)^2 + 1$.",
            "execution": "$(2400 / 150) = 16$. Kemudian $16^2 + 1 = 256 + 1 = 257$ level gradasi."
        }
    },
    {
        "id": "tekd-lat-h-05",
        "materi": "KOMPUTER GRAFIS & VEKTOR",
        "topic": "Winding Rules pada Compound Path: Non-Zero vs Even-Odd",
        "stem": "Saat seorang desainer membuat logo vektor dengan bentuk rumit bertumpuk (compound path) di Illustrator, ia mendapati bahwa lubang di tengah lingkaran terkadang terisi warna atau tetap berlubang tergantung pengisian jalur kurva. Perbedaan mendasar antara aturan pengisian 'Non-Zero Winding Rule' dan 'Even-Odd Rule' dalam komputasi kurva vektor adalah...",
        "correct": "Even-Odd Rule menentukan area berlubang murni berdasarkan jumlah perpotongan sinar garis ganjil-genap terlepas dari arah kurva, sedangkan Non-Zero Rule mempertimbangkan arah arah jarum jam (path direction) vektor untuk menentukan daerah isi atau lubang.",
        "distractors": [
            "Even-Odd Rule hanya dapat diterapkan pada gambar berformat JPEG resolusi rendah di bawah 72 PPI.",
            "Non-Zero Winding Rule secara otomatis menghapus seluruh kurva terbuka dan mengubahnya menjadi segitiga siku-siku.",
            "Even-Odd Rule mewajibkan desainer menginput angka ganjil pada setiap koordinat anchor point di kanvas.",
            "Non-Zero Rule tidak mengizinkan penggunaan warna gradasi selain warna merah dan kuning primer."
        ],
        "formula": {
            "title": "ALGORITMA WINDING RULES PADA GRAFIK VEKTOR",
            "latex": "\\text{Winding Number } W = \\sum \\text{Arah Vektor Potong}; \\quad \\begin{cases} W \\ne 0 \\implies \\text{Fill (Non-Zero)} \\\\ \\text{Count mod } 2 = 1 \\implies \\text{Fill (Even-Odd)} \\end{cases}",
            "legend": "• Non-Zero: Arah sub-path berlawanan (Clockwise vs Counter-Clockwise) membatalkan winding $\\implies$ membentuk lubang<br>• Even-Odd: Hitung garis tembus; ganjil = isi, genap = lubang (konsisten dan mudah diprediksi desainer)<br>• Standar SVG / PostScript: Menggunakan kedua algoritma ini"
        },
        "hints": {
            "concept": "Even-Odd Rule hanya menghitung jumlah perpotongan (ganjil = isi, genap = bolong), sementara Non-Zero memperhitungkan arah kurva (searah vs berlawanan jarum jam).",
            "execution": "Pilih jawaban yang menjelaskan peran arah kurva (path direction) pada Non-Zero vs hitungan perpotongan pada Even-Odd."
        }
    },
    {
        "id": "tekd-lat-h-06",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Lighting Ratio & Pengendalian Kontras Mood (Key to Fill Ratio)",
        "stem": "Dalam pemotretan poster film bertema misteri kriminal (film noir), penata cahaya mengatur intensitas Key Light menghasilkan pembacaan lightmeter sebesar f/8 pada sisi terang wajah aktor, sementara Fill Light diatur sangat redup menghasilkan pembacaan f/2.8 pada sisi bayangan. Berapakah rasio kontras pencahayaan (Lighting Ratio) pada wajah aktor tersebut?",
        "correct": "8:1 (atau 3 stop perbedaan), yang menciptakan kontras tinggi dramatis dengan bayangan pekat (chiaroscuro / low key lighting) yang menonjolkan ketegangan misterius.",
        "distractors": [
            "2:1 (hanya 1 stop perbedaan), yang menghasilkan pencahayaan datar lembut tanpa bayangan sama sekali layaknya iklan kosmetik pagi hari.",
            "16:1 (4 stop perbedaan), di mana sisi bayangan wajah aktor terbakar menjadi putih menyilaukan melebihi batas lampu utama.",
            "1:1 (rasio seimbang sempurna), di mana kedua sisi wajah aktor memiliki intensitas terang yang sama persis tanpa dimensi kedalaman.",
            "64:1 (6 stop perbedaan), yang menyebabkan sensor kamera DSLR langsung meledak karena kelebihan tegangan foton."
        ],
        "formula": {
            "title": "FORMULA LIGHTING RATIO & STOP PERBEDAAN",
            "latex": "\\text{Rasio Kontras} = 2^{\\Delta \\text{stops}} = 2^{(f/8 - f/2.8)} = 2^3 = 8:1",
            "legend": "• Skala f-stop: f/2.8 $\\rightarrow$ f/4 (1 stop) $\\rightarrow$ f/5.6 (2 stop) $\\rightarrow$ f/8 (3 stop)<br>• Rasio 2:1 (1 stop): Komersial / Beauty High Key<br>• Rasio 3:1 - 4:1 (1.5 - 2 stop): Potret standar dramatis<br>• Rasio 8:1 (3 stop): Low Key / Film Noir misteri"
        },
        "hints": {
            "concept": "Dari f/2.8 ke f/8 terdapat selisih 3 stop f-number ($f/2.8 \\rightarrow f/4 \\rightarrow f/5.6 \\rightarrow f/8$). Setiap 1 stop melipatgandakan cahaya $2\\times$, sehingga $2^3 = 8$.",
            "execution": "Selisih 3 stop menghasilkan rasio 8:1 (kontras tinggi gaya Low Key)."
        }
    },
    {
        "id": "tekd-lat-h-07",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Teknik Repro: UCR vs GCR (Gray Component Replacement)",
        "stem": "Sebuah percetakan majalah nasional berkecepatan tinggi beralih menggunakan metode separasi Gray Component Replacement (GCR) alih-alih Under Color Removal (UCR) konvensional untuk dokumen edisi cetak mereka. Keunggulan teknis dan ekonomis paling signifikan dari penerapan GCR pada mesin cetak rotasi adalah...",
        "correct": "Menggantikan komponen abu-abu netral yang dibentuk oleh perpaduan tiga tinta mahal (Cyan, Magenta, Yellow) dengan tinta hitam (Black/Key) tunggal yang murah di seluruh rentang nada, menghemat biaya tinta dan menjaga stabilitas netralitas abu-abu dari fluktuasi tinta.",
        "distractors": [
            "Menghapus seluruh penggunaan tinta hitam sehingga gambar majalah hanya dicetak menggunakan tiga warna primer transparan.",
            "Membuat kertas majalah menjadi tahan api dan tahan air secara permanen tanpa perlu proses laminasi plastik tambahan.",
            "Menaikkan batas Total Area Coverage (TAC) kertas menjadi 500% agar tinta lebih lambat mengering di tumpukan palet.",
            "Mengganti proses cetak separasi plat menjadi cetak stempel karet manual di setiap lembaran majalah."
        ],
        "formula": {
            "title": "SEPARASI PRE-PRESS: UCR VS GCR",
            "latex": "\\text{CMY Terpadu Netral} \\xrightarrow{\\text{GCR}} \\text{K (Tinta Hitam)} \\implies \\Delta \\text{Cost Tinta CMY} \\downarrow, \\quad \\text{Gray Balance Stability} \\uparrow",
            "legend": "• UCR (Under Color Removal): Hanya mengganti CMY netral di area bayangan gelap pekat (shadows)<br>• GCR (Gray Component Replacement): Mengganti CMY netral di seluruh nada (highlight, midtone, shadow)<br>• Keuntungan: Abu-abu tidak berubah kehijauan/kemerahan saat mesin bergetar"
        },
        "hints": {
            "concept": "GCR menggantikan komponen warna abu-abu netral (campuran C+M+Y) dengan tinta hitam tunggal. Menghemat tinta CMY mahal dan membuat warna abu-abu stabil.",
            "execution": "GCR menstabilkan gray balance dan memangkas konsumsi tinta warna Cyan, Magenta, Yellow di mesin cetak cepat."
        }
    },
    {
        "id": "tekd-lat-h-08",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Hukum Kuadrat Terbalik Cahaya (Inverse Square Law)",
        "stem": "Dalam pemotretan studio berjarak, sebuah lampu softbox diletakkan pada jarak 2 meter dari model dan menghasilkan intensitas paparan cahaya yang tepat pada aperture f/8. Jika fotografer memindahkan lampu softbox tersebut mundur menjauh menjadi berjarak 4 meter dari model, berapakah intensitas cahaya yang tersisa menyinari model menurut Hukum Kuadrat Terbalik (Inverse Square Law)?",
        "correct": "Tersisa 1/4 (25%) dari intensitas cahaya awal, sehingga fotografer harus membuka diafragma lensa sebanyak 2 stop penuh (menjadi f/4) untuk mempertahankan eksposur yang setara.",
        "distractors": [
            "Tersisa 1/2 (50%) dari intensitas awal, sehingga fotografer hanya perlu mengubah bukaan diafragma sebanyak setengah stop ke f/5.6.",
            "Intensitas cahaya meningkat 4 kali lipat lebih terang karena gelombang foton menyerap molekul udara di dalam ruangan studio.",
            "Intensitas cahaya tetap persis sama 100% karena daya watt bohlam lampu studio tidak diturunkan oleh saklar listrik.",
            "Cahaya padam total dan sensor kamera tidak dapat merekam objek apa pun pada jarak melampaui 3 meter."
        ],
        "formula": {
            "title": "INVERSE SQUARE LAW PENCAHAYAAN STUDIO",
            "latex": "I \\propto \\frac{1}{d^2} \\implies \\frac{I_2}{I_1} = \\left( \\frac{d_1}{d_2} \\right)^2 = \\left( \\frac{2}{4} \\right)^2 = \\frac{1}{4} \\implies \\Delta = -2\\,\\text{stops} \\ (f/8 \\rightarrow f/4)",
            "legend": "• $d$ digandakan ($2\\times$) $\\implies$ Intensitas $I$ anjlok menjadi $\\frac{1}{4}$ (turun 2 stop)<br>• $d$ ditipiskan setengah ($0.5\\times$) $\\implies$ Intensitas $I$ melonjak $4\\times$ (naik 2 stop)<br>• Kunci Penguasaan: Mengatur kejatuhan cahaya (light falloff) pada model vs latar belakang"
        },
        "hints": {
            "concept": "Hukum Kuadrat Terbalik: jika jarak digandakan ($2\\times$), intensitas cahaya turun menjadi $(1/2)^2 = 1/4$.",
            "execution": "Penurunan intensitas menjadi 1/4 setara dengan kehilangan 2 stop cahaya ($f/8 \\rightarrow f/5.6 \\rightarrow f/4$)."
        }
    },
    {
        "id": "tekd-lat-h-09",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Doktrin Persamaan pada Pokoknya (Likelihood of Confusion)",
        "stem": "Sebuah merek sepatu lokal mendaftarkan logo dan nama 'ADIDASSO' dengan jenis font trefoil bergaris miring tiga yang sangat mirip dengan merek global terdaftar 'ADIDAS' untuk produk sepatu olahraga sejenis. Ditinjau dari Pasal 21 UU No. 20 Tahun 2016 tentang Merek dan Indikasi Geografis, permohonan pendaftaran merek tersebut wajib ditolak karena...",
        "correct": "Memiliki persamaan pada pokoknya (substantial similarity) baik secara visual, fonetik (bunyi pengucapan), maupun konseptual yang berpotensi menyesatkan konsumen mengenai asal-usul produk (likelihood of confusion).",
        "distractors": [
            "Menggunakan warna hitam yang telah dipatenkan secara tunggal oleh kementerian olahraga republik Indonesia.",
            "Kata 'ADIDASSO' memiliki jumlah suku kata ganjil yang melanggar kaidah tata bahasa baku bahasa Indonesia.",
            "Perusahaan pemohon belum terdaftar sebagai anggota perserikatan bangsa-bangsa di bidang standardisasi tekstil.",
            "Sepatu olahraga dilarang diproduksi di wilayah Asia Tenggara menurut kesepakatan perdagangan Jenewa."
        ],
        "formula": {
            "title": "DOKTRIN PERSAMAAN PADA POKOKNYA (PASAL 21 UU MEREK)",
            "latex": "\\text{Penolakan Merek} \\iff \\text{Similarity}(\\text{Visual, Fonetik, Konseptual}) \\implies \\text{Likelihood of Confusion} > 0",
            "legend": "• Visual: Kemiripan bentuk logo, susunan garis, warna, dan gaya tipografi<br>• Fonetik: Kemiripan bunyi saat dilafalkan secara lisan (Adidasso vs Adidas)<br>• Kriteria: Menyesatkan konsumen awam seolah barang berasal dari produsen yang sama"
        },
        "hints": {
            "concept": "Merek ditolak jika memiliki 'persamaan pada pokoknya' (visual, bunyi ucapan/fonetik, atau konsep) untuk kelas barang yang sejenis.",
            "execution": "Kemiripan visual dan fonetik yang memicu kebingungan konsumen (likelihood of confusion) menjadi dasar penolakan mutlak."
        }
    },
    {
        "id": "tekd-lat-h-10",
        "materi": "DESAIN MEDIA & KEMASAN",
        "topic": "Kalkulasi Uji Beban Kardus: BCT vs ECT (McKee Formula)",
        "stem": "Dalam perancangan kemasan karton boks ekspor keramik hias seberat 20 kg per boks, boks tersebut akan ditumpuk setinggi 6 lapis di dalam kontainer kapal laut selama 30 hari dalam kondisi kelembapan tinggi. Jika desainer harus memperhitungkan faktor keamanan (safety factor) sebesar 5 untuk mengantisipasi kelembapan dan getaran dinamis, berapakah beban tekan minimal (Box Compression Strength - BCT) yang harus ditahan oleh boks paling bawah?",
        "correct": "500 kg-force (kgf), yang dihitung dari beban 5 tumpukan di atas boks bawah ($5 \\times 20\\,\\text{kg} = 100\\,\\text{kg}$) dikalikan faktor keamanan ($100 \\times 5 = 500\\,\\text{kgf}$).",
        "distractors": [
            "120 kg-force, yang hanya merupakan total berat 6 boks tanpa dikalikan faktor keamanan kelembapan kontainer laut.",
            "20 kg-force, yang hanya setara dengan berat satu boks satuan tunggal di atas lantai pabrik.",
            "2000 kg-force, yang merupakan kapasitas angkut maksimal satu unit truk kontainer tronton antar provinsi.",
            "50 kg-force, yang dihitung dari pembagian berat keramik dengan luas permukaan tutup atas karton."
        ],
        "formula": {
            "title": "FORMULA BEBAN TEKAN KEMASAN KARTON (BCT)",
            "latex": "\\text{BCT} = (N - 1) \\times W_{\\text{boks}} \\times \\text{Safety Factor} = (6 - 1) \\times 20 \\times 5 = 500\\,\\text{kgf}",
            "legend": "• $N$: Jumlah total lapisan tumpukan (6 boks)<br>• $N-1$: Beban yang ditanggung boks terbawah (5 boks)<br>• Safety Factor ($4-5$): Mengkompensasi kelembapan udara $> 80\\%$, degradasi waktu, dan guncangan kapal"
        },
        "hints": {
            "concept": "Boks paling bawah menahan beban boks di atasnya ($6-1 = 5$ boks). Beban statis $= 5 \\times 20 = 100$ kg. Dengan safety factor 5, $100 \\times 5 = 500$ kgf.",
            "execution": "$BCT = (6-1) \\times 20 \\times 5 = 500$ kgf."
        }
    },
    {
        "id": "tekd-lat-h-11",
        "materi": "MODEL WARNA & PRE-PRESS",
        "topic": "Pengukuran Akurasi Warna Spektrofotometer: CIE Delta E 2000",
        "stem": "Sebuah percetakan kemasan farmasi mengaudit kualitas cetak warna logo obat pada lembaran cetak produksi massal menggunakan instrumen spektrofotometer berdasarkan standar toleransi warna ISO 12647-2. Nilai deviasi warna formula $\\Delta E_{00}$ (CIE Delta E 2000) terukur sebesar 0.8 terhadap sampel warna standar acuan klien. Interpretasi profesional atas hasil pengukuran warna tersebut adalah...",
        "correct": "Kualitas cetak sangat prima dan lolos uji kontrol kualitas, karena nilai $\\Delta E_{00} < 1.0$ berada di bawah ambang batas persepsi mata manusia biasa (perbedaan warna tidak kasat mata).",
        "distractors": [
            "Hasil cetak ditolak secara mutlak karena nilai toleransi deviasi warna di industri farmasi wajib mencapai tepat angka nol koma nol mutlak.",
            "Tinta cetak terbukti mengalami keracunan bakteri sehingga seluruh batch kemasan harus dimusnahkan di ruang pembakaran khusus.",
            "Operator mesin offset harus segera mengganti seluruh rol silinder mesin cetak karena warna bergeser sejauh 80 persen.",
            "Nilai tersebut membuktikan bahwa percetakan menggunakan model warna RGB 8-bit alih-alih tinta separasi offset."
        ],
        "formula": {
            "title": "SKALA AKURASI WARNA CIE $\\Delta E_{00}$ (ISO 12647-2)",
            "latex": "\\Delta E_{00} = \\sqrt{ \\left( \\frac{\\Delta L'}{k_L S_L} \\right)^2 + \\left( \\frac{\\Delta C'}{k_C S_C} \\right)^2 + \\left( \\frac{\\Delta H'}{k_H S_H} \\right)^2 + R_T \\dots }",
            "legend": "• $\\Delta E < 1.0$: Perbedaan tak terlihat oleh mata manusia (imperceptible / perfect)<br>• $1.0 \\le \\Delta E < 2.0$: Terlihat oleh pengamat terlatih melalui inspeksi teliti<br>• $\\Delta E \\ge 3.0$: Terlihat jelas oleh konsumen awam (rejection threshold)"
        },
        "hints": {
            "concept": "Nilai Delta E mengukur selisih dua warna. Jika $\\Delta E < 1.0$, mata manusia secara fisiologis tidak mampu melihat perbedaannya.",
            "execution": "Nilai 0.8 berada di bawah 1.0, menandakan hasil cetak presisi sempurna dan lolos QC."
        }
    },
    {
        "id": "tekd-lat-h-12",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Hukum Hick-Hyman (Hick's Law) dalam Information Architecture UI",
        "stem": "Dalam audit antarmuka (UX Audit) sebuah marketplace online, ditemukan bahwa pengguna membutuhkan waktu rata-rata 45 detik hanya untuk menemukan kategori produk yang diinginkan pada menu beranda yang menyajikan 64 pilihan kategori acak sekaligus dalam satu halaman. Rekomendasi restrukturisasi arsitektur informasi berdasarkan Hukum Hick-Hyman ($T = b \\log_2(n+1)$) adalah...",
        "correct": "Mengelompokkan 64 pilihan tersebut ke dalam 5 hingga 7 kategori induk utama berbasis hierarki logis untuk meminimalkan beban kognitif dan mempersingkat waktu pengambilan keputusan pengguna.",
        "distractors": [
            "Menambah jumlah pilihan menjadi 128 kategori dengan warna latar belakang berkedip-kedip untuk menarik mata.",
            "Menghapus seluruh navigasi menu kategori dan memaksa pengguna menebak kata kunci pencarian tanpa panduan apa pun.",
            "Menampilkan seluruh 64 kategori dalam satu baris horizontal teks berjalan (marquee) berkecepatan 100 piksel per detik.",
            "Mengubah ukuran font seluruh nama kategori menjadi 4 pt agar seluruh pilihan muat di dalam layar ponsel tanpa perlu scroll."
        ],
        "formula": {
            "title": "HICK-HYMAN LAW REAKSI KEPUTUSAN UI/UX",
            "latex": "T = b \\log_2(n + 1) \\implies n \\downarrow (64 \\rightarrow 7) \\implies T \\text{ (Waktu Keputusan)} \\downarrow \\text{ Drastis}",
            "legend": "• $T$: Waktu reaksi yang dibutuhkan untuk memilih target<br>• $n$: Jumlah opsi stimulus alternatif yang disajikan<br>• Beban Kognitif: Semakin banyak pilihan acak sejajar, semakin tinggi paralisis analisis (decision fatigue)"
        },
        "hints": {
            "concept": "Hukum Hick menyatakan bahwa waktu untuk mengambil keputusan meningkat secara logaritmik seiring bertambahnya jumlah opsi.",
            "execution": "Mereduksi opsi dari 64 pilihan berserakan menjadi 5-7 kategori induk mempercepat keputusan secara drastis."
        }
    },
    {
        "id": "tekd-lat-h-13",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "180-Degree Shutter Rule pada Sinematografi Komersial",
        "stem": "Seorang desainer multimedia merekam video iklan televisi minuman energi pada kecepatan frame standar bioskop 24 Frame Per Detik (FPS). Untuk menghasilkan efek kekaburan gerak (motion blur) yang paling natural dan sinematik sesuai aturan sudut rana 180 derajat (180-Degree Shutter Rule), kecepatan rana (shutter speed) kamera video wajib diatur tepat pada...",
        "correct": "1/48 atau 1/50 detik, yang merupakan dua kali lipat dari kecepatan frame per detik ($t_{\\text{shutter}} = 1 / (2 \\times \\text{FPS})$).",
        "distractors": [
            "1/24 detik (360 derajat sudut rana), yang menyebabkan seluruh adegan lari atlet tampak buram berbayang tanpa ketajaman sama sekali.",
            "1/1000 detik (sudut rana mikro), yang menghasilkan gerakan patah-patah kaku (strobe/choppy) yang membuat mata penonton lelah.",
            "1 detik penuh, di mana kamera merekam jejak cahaya lampu malam tanpa memperlihatkan sosok atlet minuman energi.",
            "1/12 detik, yang mengakibatkan memori kamera video kehabisan bandwidth transmisi sinyal audio."
        ],
        "formula": {
            "title": "180-DEGREE SHUTTER RULE SINEMATOGRAFI",
            "latex": "\\text{Shutter Speed} = \\frac{1}{2 \\times \\text{FPS}} \\implies \\text{Pada 24/25 FPS} \\implies t_{\\text{shutter}} = \\frac{1}{48} \\approx \\frac{1}{50}\\,\\text{detik}",
            "legend": "• 180° Rule: Standar baku emulasi motion blur rana putar mekanik kamera film 35mm<br>• Shutter Terlalu Cepat ($> 1/250$): Gerakan terputus kaku/stroboskopik (cocok hanya untuk adegan perang/ledakan)<br>• Shutter Terlalu Lambat ($< 1/24$): Gerakan menyeret buram (smearing/dreamy effect)"
        },
        "hints": {
            "concept": "Aturan 180 derajat dalam sinematografi menyatakan bahwa kecepatan rana harus sama dengan 1 dibagi (2 kali frame rate).",
            "execution": "Pada 24 atau 25 FPS, $1/(2 \\times 24) = 1/48$ detik atau $1/50$ detik."
        }
    },
    {
        "id": "tekd-lat-h-14",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Angka Tabular vs Proportional & Old Style Figures",
        "stem": "Dalam penyusunan tata letak laporan tahunan keuangan (Annual Report) sebuah bank nasional yang memuat tabel neraca laba-rugi puluhan miliar rupiah, desainer wajib memastikan bahwa angka ribuan, jutaan, dan desimal lurus vertikal sejajar sempurna di setiap baris kolom tabel. Konfigurasi OpenType angka yang wajib diaktifkan adalah...",
        "correct": "Tabular Lining Figures, di mana setiap angka memiliki lebar karakter horizontal yang sama persis (monospaced) dan tinggi angka sejajar rata dengan huruf kapital.",
        "distractors": [
            "Proportional Old Style Figures, di mana angka memiliki lebar bervariasi dan bagian bawah angka 3, 4, 5, 7, 9 menggantung di bawah garis dasar (descender).",
            "Faux Italic Numbers, di mana seluruh angka dimiringkan paksa 45 derajat sehingga memotong batas kolom tabel.",
            "Discretionary Fractions, yang mengubah seluruh angka neraca keuangan menjadi pecahan matematika perdelapanan.",
            "Small Caps Numerals, yang mengubah angka menjadi huruf hieroglif Mesir kuno tanpa nilai nominal."
        ],
        "formula": {
            "title": "TIPOGRAFI ANGKA: TABULAR VS PROPORTIONAL",
            "latex": "\\text{Lebar Huruf}(\\text{Angka 1}) = \\text{Lebar Huruf}(\\text{Angka 8}) \\iff \\text{Tabular Figures (Rata Vertikal Kolom)}",
            "legend": "• Tabular Lining: Lebar sama (monospaced) + Cap Height $\\implies$ Wajib untuk tabel finansial & data numerik<br>• Proportional Lining: Lebar bervariasi + Cap Height $\\implies$ Bagus untuk judul headline<br>• Old Style (Lilliput): Memiliki ascender/descender $\\implies$ Menyatu harmonis di dalam paragraf body text"
        },
        "hints": {
            "concept": "Untuk kolom tabel data keuangan yang berjejer ke bawah, angka harus menggunakan Tabular Figures agar lebar setiap karakter angka identik dan titik desimal lurus rapi.",
            "execution": "Tabular Lining Figures menjamin seluruh angka sejajar lurus secara vertikal dalam tabel neraca."
        }
    },
    {
        "id": "tekd-lat-h-15",
        "materi": "HAKI & ETIKA DESAIN",
        "topic": "Doktrin Work Made for Hire pada Hubungan Kerja Desainer",
        "stem": "Seorang desainer grafis bekerja sebagai karyawan tetap di divisi kreatif PT Maju Jaya Makmur. Selama jam kerja resmi dan menggunakan komputer fasilitas kantor, ia merancang maskot perusahaan yang kemudian sangat populer dan mendatangkan omset miliaran rupiah. Dua tahun kemudian desainer tersebut keluar dan menuntut royalti penjualan maskot tersebut. Berdasarkan Pasal 36 UU No. 28 Tahun 2014 tentang Hak Cipta, bagaimanakah status kepemilikan hak cipta maskot tersebut?",
        "correct": "Pemegang hak cipta atas maskot tersebut adalah pihak perusahaan (PT Maju Jaya Makmur) sebagai pemberi kerja dalam hubungan dinas resmi, kecuali diperjanjikan lain secara tertulis dalam kontrak kerja.",
        "distractors": [
            "Hak cipta sepenuhnya beralih menjadi milik pribadi mantan desainer karena perusahaan hanya menyediakan perangkat komputer tanpa menyumbang ide kreatif.",
            "Hak cipta otomatis hangus dan maskot menjadi domain publik gratis yang boleh dipakai oleh seluruh kompetitor bisnis secara bebas.",
            "Perusahaan diwajibkan oleh pengadilan membagi separuh saham kepemilikan pabrik kepada mantan desainer tersebut.",
            "Pemerintah kota setempat menyita maskot tersebut untuk dijadikan lambang resmi kantor dinas perpajakan."
        ],
        "formula": {
            "title": "HAK CIPTA DALAM HUBUNGAN KERJA (PASAL 36 UU HAK CIPTA)",
            "latex": "\\text{Karya Dibuat dalam Hubungan Dinas/Kerja Tetap} \\implies \\text{Pemberi Kerja = Pemegang Hak Cipta}",
            "legend": "• Syarat: Dikerjakan dalam jam kerja resmi, atas arahan atasan, dan fasilitas dinas<br>• Hak Moral: Nama perancang tetap dapat diakui sebagai pencipta asli<br>• Hak Ekonomi: Dimiliki penuh oleh korporasi pemberi kerja (kecuali ada klausul perjanjian khusus)"
        },
        "hints": {
            "concept": "Menurut UU Hak Cipta Indonesia, ciptaan yang dibuat oleh karyawan tetap dalam hubungan dinas/kerja resmi menjadi milik pemberi kerja (perusahaan), kecuali ada perjanjian tertulis lain.",
            "execution": "Perusahaan adalah pemegang hak cipta yang sah secara hukum."
        }
    },
    {
        "id": "tekd-lat-h-16",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Prägnanz (Law of Good Figure) & Cognitive Load Reduction",
        "stem": "Dalam merancang dashboard visual sistem kendali pesawat terbang atau pembangkit listrik tenaga nuklir, desainer menyederhanakan bentuk-bentuk indikator yang rumit menjadi figur geometris murni yang simetris, teratur, dan minim distorsi visual. Landasan psikologi kognitif Gestalt yang diterapkan untuk meminimalkan beban kerja mental operator dalam situasi darurat adalah...",
        "correct": "Law of Prägnanz (Hukum Keteraturan / Simplicity), di mana otak manusia memproses dan mengingat stimulus visual dalam bentuk yang paling sederhana, teratur, dan stabil dengan usaha kognitif seminimal mungkin.",
        "distractors": [
            "Law of Past Experience, di mana operator harus mengingat kembali lagu masa kanak-kanak sebelum menekan tombol darurat.",
            "Law of Proximity, di mana seluruh jarum indikator harus ditumpuk menjadi satu titik di tengah layar kaca.",
            "Law of Invariance, yang melarang penggunaan warna selain warna hitam dan putih pada seluruh panel industri nuklir.",
            "Law of Continuity, yang memaksa operator hanya memandang layar dari sudut 180 derajat membelakangi panel kendali."
        ],
        "formula": {
            "title": "GESTALT LAW OF PRÄGNANZ (HUKUM SIMPLISITAS)",
            "latex": "\\text{Beban Kognitif (Cognitive Load)} \\propto \\text{Kompleksitas Visual}; \\quad \\min(\\text{Entropy}) \\implies \\text{Prägnanz}",
            "legend": "• Prägnanz: Prinsip payung Gestalt (otak selalu mereduksi objek acak ke bentuk paling teratur & stabil)<br>• Aplikasi Mission-Critical: Cockpit display, medical equipment, industrial SCADA<br>• Tujuan: Mencegah human error operator saat beban stres tinggi"
        },
        "hints": {
            "concept": "Hukum Prägnanz menyatakan bahwa persepsi visual cenderung memilih konfigurasi paling sederhana, simetris, dan teratur demi efisiensi otak.",
            "execution": "Penyederhanaan indikator untuk meminimalkan beban kognitif operator darurat menerapkan Law of Prägnanz."
        }
    },
    {
        "id": "tekd-lat-h-17",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Paparan Uap Kimia Pelarut Cetak (VOC / IPA) & Ventilasi LEV",
        "stem": "Pada ruang produksi percetakan digital dan offset komersial, operator sering menghirup uap pelarut pembersih tinta beracun yang mengandung Senyawa Organik Yang Mudah Menguap (Volatile Organic Compounds - VOC) dan Isopropil Alkohol (IPA). Sistem pengendalian teknis K3LH yang paling efektif untuk melindungi sistem pernapasan pekerja menurut hierarki pengendalian bahaya adalah...",
        "correct": "Memasang sistem ventilasi pembuangan lokal (Local Exhaust Ventilation - LEV) berupa tudung hisap (fume hood) tepat di atas titik penguapan mesin cetak untuk menyedot uap beracun keluar sebelum terhirup pekerja.",
        "distractors": [
            "Menutup seluruh jendela dan pintu ruangan rapat-rapat serta menyemprotkan pengharum ruangan beraroma mawar melati.",
            "Menyuruh pekerja menahan napas selama 8 jam jam kerja tanpa menggunakan alat bantu pernapasan apa pun.",
            "Menyediakan susu kental manis kalengan sebanyak satu sendok teh setiap akhir bulan sebagai penawar racun paru-paru.",
            "Mengganti seluruh lampu penerangan ruangan kerja dengan bohlam warna merah untuk menyamarkan bau uap pelarut kimia."
        ],
        "formula": {
            "title": "HIERARKI PENGENDALIAN K3LH (HIERARCHY OF CONTROLS)",
            "latex": "\\text{Eliminasi} > \\text{Substitusi} > \\text{Rekayasa Teknik (LEV)} > \\text{Administratif} > \\text{APD (Respirator)}",
            "legend": "• LEV (Local Exhaust Ventilation): Pengendalian rekayasa terbaik untuk gas/uap VOC<br>• NAB (Nilai Ambang Batas) IPA: $200\\,\\text{ppm}$ (Permenaker No. 5/2018)<br>• Paparan Kronis VOC: Kerusakan sistem saraf pusat, fungsi hati, dan karsinogenik"
        },
        "hints": {
            "concept": "Hierarki pengendalian teknik (engineering controls) mengharuskan penangkapan sumber bahaya di titik awalnya menggunakan ventilasi hisap lokal (LEV / fume hood).",
            "execution": "Pemasangan Local Exhaust Ventilation (LEV) menyedot uap kimia berbahaya langsung di sumbernya sebelum mencemari udara kerja."
        }
    },
    {
        "id": "tekd-lat-h-18",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Design System Tokenization (Design Tokens Hierarchy)",
        "stem": "Dalam pengembangan produk digital berskala enterprise yang melibatkan puluhan tim desainer grafis UI dan software engineer di berbagai platform (iOS, Android, Web), tim menerapkan arsitektur Design Tokens. Struktur hirarki tingkatan token yang benar dari tingkat paling dasar hingga komponen spesifik adalah...",
        "correct": "Global/Primitive Tokens (misal: `blue-500: #1E88E5`) $\\rightarrow$ Semantic/Alias Tokens (misal: `color-interactive-primary: blue-500`) $\\rightarrow$ Component Tokens (misal: `btn-primary-bg: color-interactive-primary`).",
        "distractors": [
            "Component Tokens $\\rightarrow$ Global Tokens $\\rightarrow$ Pixel Dimensions $\\rightarrow$ User Persona Description.",
            "Marketing Budget Tokens $\\rightarrow$ Copyright License Tokens $\\rightarrow$ Vector Curve Tokens $\\rightarrow$ Typography Tokens.",
            "CSS Inline Styles $\\rightarrow$ Adobe Illustrator Swatches $\\rightarrow$ Print Proofing Tokens $\\rightarrow$ Bleed Margin Tokens.",
            "RGB Values $\\rightarrow$ CMYK Halftone Screen $\\rightarrow$ Paper Weight GSM $\\rightarrow$ Corrugated Flute Code."
        ],
        "formula": {
            "title": "ARSITEKTUR MULTI-LEVEL DESIGN TOKENS",
            "latex": "\\text{Primitive} (\\text{Raw Values}) \\xrightarrow{\\text{Aliasing}} \\text{Semantic} (\\text{Intent/Context}) \\xrightarrow{\\text{Scoping}} \\text{Component-Specific}",
            "legend": "• Tier 1 (Global/Primitive): Nilai absolut warna, spasi, radius (`color-red-600: #E53935`)<br>• Tier 2 (Semantic): Makna fungsi (`color-feedback-danger: {color-red-600}`)<br>• Tier 3 (Component): Batasan spesifik elemen (`alert-banner-bg: {color-feedback-danger}`)"
        },
        "hints": {
            "concept": "Hirarki design token standar industri: Global (nilai mentah) -> Semantic/Alias (fungsi/arti konteks) -> Component (spesifik tombol/komponen).",
            "execution": "Primitive (`blue-500`) -> Semantic (`interactive-primary`) -> Component (`btn-primary-bg`)."
        }
    },
    {
        "id": "tekd-lat-h-19",
        "materi": "KOMPUTER GRAFIS & VEKTOR",
        "topic": "Optimasi Kurva Bézier: Anchor Point Reduction pada Plotter Cutting",
        "stem": "Sebuah file desain stiker vinyl otomotif diekspor untuk dipotong menggunakan mesin mesin cutting plotter pisau geser (drag knife). Operator menemukan bahwa pisau mesin bergerak tersendat-sendat kasar, merobek sudut stiker, dan memakan waktu potong 5 kali lebih lama. Setelah diperiksa, file vektor desainer memiliki ribuan titik jangkar (anchor point) padat yang saling berdekatan akibat fitur auto-trace kasar. Tindakan optimasi vektor yang tepat adalah...",
        "correct": "Menyederhanakan kurva (Simplify Path / kurva reduksi) untuk meminimalkan jumlah titik jangkar hanya pada titik ekstrem sudut dan puncak kelengkungan, memaksimalkan penggunaan tuas kendali (handles) halus.",
        "distractors": [
            "Mengonversi kurva vektor menjadi gambar raster bitmap hitam-putih 72 PPI berformat BMP.",
            "Menambahkan 10.000 anchor point baru di setiap segmen garis lurus untuk memperkuat daya rekat pisau plotter.",
            "Menaikkan tekanan pisau mesin potong hingga menembus meja kerja besi hingga keluar percikan api.",
            "Mencelupkan lembaran stiker vinyl ke dalam minyak pelumas mesin sebelum dimasukkan ke mesin cutting plotter."
        ],
        "formula": {
            "title": "VEKTOR & DRAG-KNIFE KINEMATICS",
            "latex": "\\min(N_{\\text{anchors}}) \\iff \\text{Smooth Acceleration} \\quad (\\text{Plat Ekstrem: } \\frac{d^2\\mathbf{B}}{dt^2} = 0)",
            "legend": "• Anchor Point Berlebih: Pisau drag knife harus berputar orientasi mekanis di setiap titik $\\implies$ robek & getaran<br>• Titik Ekstrem (On-Curve Extremities): Titik tertinggi, terendah, terkiri, terkanan<br>• Handles Panjang: Menggantikan 50 anchor point padat menjadi 2 titik dengan 1 busur mulus"
        },
        "hints": {
            "concept": "Titik jangkar yang terlalu padat membuat pisau plotter tersendat karena harus mengubah orientasi pisau terus-menerus. Kurva harus disederhanakan (Simplify Path).",
            "execution": "Gunakan Simplify Path untuk menyisakan anchor point di titik-titik ekstrem penting saja."
        }
    },
    {
        "id": "tekd-lat-h-20",
        "materi": "FOTOGRAFI & PENCAHAYAAN",
        "topic": "Log Gamma Profile (Log C / S-Log) & Dynamic Range Video",
        "stem": "Dalam produksi video profil komersial pariwisata yang menampilkan pemandangan dari dalam gua gelap mengarah ke luar pantai yang terik matahari menyengat, videografer merekam dengan profil warna flat gamma logaritmik (Log Profile, misal S-Log3 / C-Log). Keunggulan teknis utama dari perekaman Log Gamma dibandingkan profil Rec.709 standar adalah...",
        "correct": "Mengompresi kurva respons cahaya secara logaritmik untuk memaksimalkan perekaman rentang dinamis (Dynamic Range) sensor kamera hingga 14+ stop, menyelamatkan detail di area bayangan gelap dan highlight terik secara bersamaan untuk tahapan color grading.",
        "distractors": [
            "Menghasilkan video yang sudah memiliki kontras tajam dan warna sangat menyala sehingga tidak memerlukan proses editing sama sekali.",
            "Menghapus suara bising angin secara otomatis menggunakan algoritma kecerdasan buatan di dalam lensa kamera.",
            "Membuat ukuran file video menjadi nol Megabyte sehingga dapat disimpan di kartu SIM telepon genggam lama.",
            "Memaksa proyektor bioskop memutar film pada kecepatan 240 frame per detik tanpa distorsi gambar."
        ],
        "formula": {
            "title": "KURVA LOGARITMIK VS STANDAR DISPLAY REC.709",
            "latex": "y_{\\text{log}} = a \\ln(x + b) + c \\implies \\text{Dynamic Range Extended to } 14-16\\,\\text{stops} \\ (\\text{Rec.709} \\approx 6-8\\,\\text{stops})",
            "legend": "• Log Profile: Menghasilkan gambar mentah yang terlihat pudar, datar (low contrast), dan desaturasi di monitor preview<br>• Retensi Informasi: Tidak ada highlight yang blown out atau shadow yang crushed<br>• Color Grading: Memerlukan LUT (Look-Up Table) saat post-processing untuk mengembalikan kontras estetis"
        },
        "hints": {
            "concept": "Log gamma merekam gambar berpenampilan flat/kusam dengan tujuan menyimpan rentang dinamis (dynamic range) sensor semaksimal mungkin dari gelap hingga terang.",
            "execution": "Mempertahankan rentang dinamis (dynamic range) tinggi hingga 14+ stop untuk color grading."
        }
    },
    {
        "id": "tekd-lat-h-21",
        "materi": "PRINSIP DESAIN & NIRMANA",
        "topic": "Nirmana Trimatra: Gaya Struktural (Tension, Compression, Cantilever)",
        "stem": "Dalam merancang gerbang masuk pameran desain grafis internasional, tim desainer membuat atap bentang kanopi yang menjorok keluar sepanjang 8 meter ke arah depan tanpa ada tiang penyangga di ujungnya (konstruksi kantilever). Untuk memastikan struktur trimatra tersebut seimbang dan tidak runtuh secara estetis dan struktural, gaya fisik yang bekerja pada bagian atas dan bawah balok kantilever berturut-turut adalah...",
        "correct": "Tarik (Tension) pada bagian serat atas balok kantilever, dan Tekan (Compression) pada bagian serat bawah balok.",
        "distractors": [
            "Tekan pada bagian serat atas balok, dan Tarik pada bagian serat bawah balok kantilever.",
            "Gaya geser murni nol tanpa ada tegangan internal di sepanjang penampang balok kayu.",
            "Gaya magnet bumi vertikal yang mendorong balok ke arah langit secara gravitasi terbalik.",
            "Gaya putar puntir (torsion) sebesar 360 derajat di setiap titik jangkar bidang dua dimensi."
        ],
        "formula": {
            "title": "MEKANIKA STRUKTUR TRIMATRA KANTILEVER",
            "latex": "\\text{Momen Lentur } M(x) = -\\frac{w x^2}{2} \\implies \\sigma_{\\text{atas}} > 0 \\text{ (Tension / Tarik)}, \\quad \\sigma_{\\text{bawah}} < 0 \\text{ (Compression / Tekan)}",
            "legend": "• Cantilever: Balok dengan satu ujung terjepit mati dan satu ujung bebas melayang<br>• Atas Meregang: Menahan gaya tarik (tension failure bila material rapuh)<br>• Bawah Tertekan: Menahan gaya desak (compression buckling bila material tipis)"
        },
        "hints": {
            "concept": "Pada balok kantilever (menjorok tanpa tiang ujung), beban menyebabkan bagian atas tertarik (tension) dan bagian bawah tertekan (compression).",
            "execution": "Serat atas mengalami gaya tarik (tension), serat bawah mengalami gaya tekan (compression)."
        }
    },
    {
        "id": "tekd-lat-h-22",
        "materi": "DESAIN MEDIA & KEMASAN",
        "topic": "Sustainable Packaging: Life Cycle Assessment (LCA) Kemasan",
        "stem": "Sebuah merek kosmetik organik ingin beralih dari kemasan botol plastik konvensional Virgin PET ke kemasan ramah lingkungan. Berdasarkan evaluasi Life Cycle Assessment (LCA) menyeluruh yang mencakup jejak karbon produksi, transportasi, dan degradasi akhir di tempat pembuangan, opsi kemasan paling berkelanjutan yang disarankan desainer adalah...",
        "correct": "Menggunakan botol 100% Post-Consumer Recycled (PCR) PET dengan sistem kemasan isi ulang (refill pouch berbahan mono-material fleksibel yang mudah didaur ulang).",
        "distractors": [
            "Mengganti seluruh botol plastik dengan botol kaca tebal berlapis cat keramik seberat 2 kilogram per botol untuk dikirim ke seluruh dunia.",
            "Menggunakan plastik Oxo-degradable yang hancur menjadi serpihan mikroplastik berbahaya yang mencemari air tanah dan rantai makanan laut.",
            "Membungkus cairan kosmetik menggunakan kertas koran bekas tanpa lapisan penahan kebocoran air.",
            "Mengimpor wadah kayu jati solid langka yang ditebang dari hutan lindung purba setiap kali produksi batch kosmetik baru."
        ],
        "formula": {
            "title": "PENILAIAN DAUR HIDUP KEMASAN (LCA ISO 14040)",
            "latex": "\\text{LCA Index} = \\text{Carbon Footprint (Material + Transport)} + \\text{Circular Recyclability Index}",
            "legend": "• Virgin PET: Emisi minyak bumi tinggi<br>• Glass: Bobot berat meningkatkan emisi karbon transportasi ekspedisi hingga 5x lipat<br>• Mono-Material PCR + Refill System: Mengurangi 80% emisi karbon dan mendukung ekonomi sirkular"
        },
        "hints": {
            "concept": "LCA mempertimbangkan rantai pasok lengkap. Kaca berat meningkatkan emisi pengiriman. Solusi modern paling sirkular adalah PCR (Post-Consumer Recycled) dengan sistem isi ulang mono-material.",
            "execution": "PCR PET dengan sistem kantong isi ulang (refill) mono-material."
        }
    },
    {
        "id": "tekd-lat-h-23",
        "materi": "WAWASAN INDUSTRI DKV",
        "topic": "Brand Equity & Resiko De-Branding (Simplifikasi Ekstrem Logo)",
        "stem": "Banyak jenama mewah (fashion luxury brands seperti Balenciaga, Burberry, dan Yves Saint Laurent) melakukan simplifikasi logo secara radikal menjadi font sans-serif geometris seragam (fenomena blanding). Risiko kerugian terbesar dari sudut pandang strategi ekuitas merek (Brand Equity) akibat de-branding ekstrem tersebut adalah...",
        "correct": "Kehilangan diferensiasi identitas visual unik dan nilai warisan sejarah (heritage value), sehingga merek tampak generik dan sulit dibedakan dari kompetitor di pasar.",
        "distractors": [
            "Mesin cetak tidak lagi mampu mencetak font sans-serif karena keterbatasan teknologi digital masa kini.",
            "Pelanggan lama secara otomatis kehilangan seluruh koleksi baju di lemari pakaian mereka di rumah.",
            "Pemerintah federal membatalkan seluruh izin ekspor impor pakaian rajut di benua Eropa.",
            "Situs web resmi perusahaan akan mengalami server down permanen selama sepuluh tahun berturut-turut."
        ],
        "formula": {
            "title": "BRAND ASSETS & BLANDING RISK",
            "latex": "\\text{Brand Distinctiveness} \\downarrow \\iff \\text{Blanding (Uniform Sans-Serif)} \\implies \\text{Price Premium Justification} \\downarrow",
            "legend": "• Blanding: Tren konvergensi logo menjadi sans-serif minimalis demi kemudahan rendering layar smartphone mikro<br>• Kelemahan: Erosi distinctive brand assets (aset visual pembeda unik yang dibangun puluhan tahun)<br>• Akibat: Menurunkan perceived value dan status eksklusivitas merek mewah"
        },
        "hints": {
            "concept": "Tren penyeragaman logo luxury brand menjadi font sans-serif sederhana (blanding) memicu hilangnya diferensiasi khas dan nilai historis warisan merek.",
            "execution": "Hilangnya diferensiasi dan nilai warisan sejarah brand membuat identitas menjadi generik."
        }
    },
    {
        "id": "tekd-lat-h-24",
        "materi": "K3LH & ERGONOMI DKV",
        "topic": "Ergonomi Kognitif: Batas Paparan Kebisingan Studio Audio-Visual",
        "stem": "Dalam studio pascaproduksi audio-visual DKV, seorang video editor mendengarkan suara mixing video menggunakan headphone tertutup (closed-back) dengan volume intensitas suara mencapai 95 dBA secara terus-menerus. Berdasarkan Permenaker No. 5 Tahun 2018 tentang Keselamatan dan Kesehatan Kerja Lingkungan Kerja, durasi pajanan maksimal yang diperkenankan per hari tanpa alat pelindung pendengaran adalah...",
        "correct": "Maksimal 2 jam per hari kerja, karena paparan intensitas bising 95 dBA di luar batas durasi tersebut dapat menyebabkan Trauma Akustik dan Gangguan Pendengaran Akibat Bising (Noise-Induced Hearing Loss - NIHL) permanen.",
        "distractors": [
            "Boleh didengarkan selama 24 jam nonstop setiap hari asalkan editor meminum suplemen vitamin C dosis tinggi.",
            "Maksimal 8 jam per hari kerja karena telinga manusia secara otomatis kebal terhadap suara di bawah 120 dBA.",
            "Maksimal 15 detik saja karena telinga manusia akan langsung terbakar jika terpapar suara berintensitas 95 dBA.",
            "Tidak ada batasan waktu sama sekali karena suara musik studio tergolong gelombang suara harmonis yang menyehatkan."
        ],
        "formula": {
            "title": "NILAI AMBANG BATAS (NAB) KEBISINGAN (PERMENAKER 5/2018)",
            "latex": "\\text{Durasi Izin: } 85\\,\\text{dBA} \\rightarrow 8\\,\\text{jam}, \\quad 88\\,\\text{dBA} \\rightarrow 4\\,\\text{jam}, \\quad 91\\,\\text{dBA} \\rightarrow 2\\,\\text{jam}, \\quad 94-95\\,\\text{dBA} \\rightarrow 1-2\\,\\text{jam}",
            "legend": "• Aturan Exchange Rate 3 dB: Setiap kenaikan intensitas suara $3\\,\\text{dBA}$, waktu paparan aman dipotong separuh ($50\\%$)<br>• NIHL: Kerusakan sel rambut koklea telinga bagian dalam yang bersifat permanen dan tidak dapat diobati<br>• Editor DKV: Wajib menerapkan batas volume aman $60\\%$ dan istirahat pendengaran berkala"
        },
        "hints": {
            "concept": "NAB kebisingan kerja standar: 85 dBA untuk 8 jam. Setiap kenaikan 3 dB, waktu pajanan aman berkurang 50%: 88 dB = 4 jam, 91 dB = 2 jam, 94-95 dB = 1-2 jam.",
            "execution": "Pada 95 dBA, batas aman paparan per hari adalah maksimal sekitar 2 jam."
        }
    },
    {
        "id": "tekd-lat-h-25",
        "materi": "TIPOGRAFI & KOMUNIKASI VISUAL",
        "topic": "Dekonstruksi Tipografi: Swiss Style vs David Carson Postmodernisme",
        "stem": "Dalam sejarah perkembangan tipografi modern, terjadi pergeseran paradigma radikal antara aliran Swiss Style (International Typographic Style) tahun 1950-an dan tipografi dekonstruksi eksperimental majalah Ray Gun karya David Carson pada era 1990-an. Pertentangan filosofis utama antara kedua gerakan desain komunikasi visual tersebut berpusat pada...",
        "correct": "Swiss Style menjunjung objektivitas rasional, grid ketat, dan netralitas font (seperti Helvetica) agar pesan terbaca murni (legibility absolute), sedangkan Carson mendobrak aturan grid dan menganggap tipografi sebagai media ekspresi emosional murni di mana 'jangan bingungkan keterbacaan dengan komunikasi'.",
        "distractors": [
            "Swiss Style hanya mengizinkan tulisan berbahasa Jerman kuno, sedangkan David Carson hanya mendesain huruf alfabet Arab kaligrafi.",
            "David Carson mewajibkan seluruh majalah dicetak di atas batu marmer, sedangkan Swiss Style mencetak majalah di atas kain sutra tipis.",
            "Swiss Style melarang penggunaan huruf vokal, sedangkan David Carson melarang penggunaan huruf konsonan.",
            "Kedua aliran desain tersebut tidak memiliki perbedaan filosofis sama sekali dan diciptakan oleh orang yang sama pada tahun yang sama."
        ],
        "formula": {
            "title": "DIALEKTIKA SEJARAH TIPOGRAFI: MODERNISME VS POSTMODERNISME",
            "latex": "\\text{Swiss Style (Müller-Brockmann)}: \\text{Form Follows Function} \\iff \\text{Postmodern (Carson)}: \\text{Don't Mistake Legibility for Communication}",
            "legend": "• Swiss Style: Grid sistem matematis, sans-serif netral, informasi hierarkis jelas, anti-ekspresionisme subjektif<br>• Dekonstruksi 90-an: Distorsi jenis huruf, overlapping text, tabrakan intuisi, teks sebagai karya seni visual ekspresif<br>• Pelajaran DKV: Pemilihan pendekatan disesuaikan dengan konteks fungsional vs emosional audiens"
        },
        "hints": {
            "concept": "Swiss Style berfokus pada ketertiban grid dan keterbacaan objektif (Helvetica). David Carson mendobrak semua aturan grid, menjadikan tipografi wahana ekspresi emosional yang liar.",
            "execution": "Swiss Style mengutamakan objektivitas rasional dan keterbacaan mutlak vs David Carson yang mengutamakan ekspresi emosional dekonstruktif."
        }
    }
]
