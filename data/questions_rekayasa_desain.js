/**
 * TKA MASTERY HUB — QUESTIONS_REKAYASA_DESAIN.JS (135 SOAL AUTENTIK)
 */
window.TKA_REKAYASA_DESAIN_QUESTIONS = [
  {
    "id": "tekd-lat-e-01",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": true
  },
  {
    "id": "tekd-lat-e-02",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-03",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-04",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": true
  },
  {
    "id": "tekd-lat-e-05",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-06",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-07",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-08",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-09",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-10",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-11",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-12",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "multi",
    "questionHtml": "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
    "options": [
      {
        "key": "A",
        "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim)."
      },
      {
        "key": "B",
        "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak)."
      },
      {
        "key": "C",
        "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK)."
      },
      {
        "key": "D",
        "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen."
      },
      {
        "key": "E",
        "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Printer marks meliputi Crop marks, Bleed marks, Registration marks, dan Color bars.",
      "execution": "Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-13",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-14",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-15",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-16",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-17",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-18",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-19",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-20",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-21",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-22",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-23",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-24",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "multi",
    "questionHtml": "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
    "options": [
      {
        "key": "A",
        "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim)."
      },
      {
        "key": "B",
        "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak)."
      },
      {
        "key": "C",
        "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK)."
      },
      {
        "key": "D",
        "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen."
      },
      {
        "key": "E",
        "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Printer marks meliputi Crop marks, Bleed marks, Registration marks, dan Color bars.",
      "execution": "Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-25",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-26",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-27",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-28",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-29",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-30",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-31",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-32",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-33",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-34",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-e-35",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-01",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-02",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-03",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-04",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-05",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-06",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-07",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-08",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-09",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-10",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-11",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-12",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "multi",
    "questionHtml": "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
    "options": [
      {
        "key": "A",
        "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim)."
      },
      {
        "key": "B",
        "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak)."
      },
      {
        "key": "C",
        "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK)."
      },
      {
        "key": "D",
        "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen."
      },
      {
        "key": "E",
        "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Printer marks meliputi Crop marks, Bleed marks, Registration marks, dan Color bars.",
      "execution": "Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-13",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-14",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-15",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-16",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-17",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-18",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-19",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-20",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-21",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-22",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-23",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-24",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "multi",
    "questionHtml": "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
    "options": [
      {
        "key": "A",
        "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim)."
      },
      {
        "key": "B",
        "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak)."
      },
      {
        "key": "C",
        "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK)."
      },
      {
        "key": "D",
        "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen."
      },
      {
        "key": "E",
        "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Printer marks meliputi Crop marks, Bleed marks, Registration marks, dan Color bars.",
      "execution": "Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-25",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-26",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-27",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-28",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-29",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-30",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-31",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-32",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-33",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-34",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-m-35",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-01",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-02",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-03",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-04",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-05",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-06",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-07",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-08",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-09",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-10",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-11",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-12",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "multi",
    "questionHtml": "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
    "options": [
      {
        "key": "A",
        "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim)."
      },
      {
        "key": "B",
        "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak)."
      },
      {
        "key": "C",
        "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK)."
      },
      {
        "key": "D",
        "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen."
      },
      {
        "key": "E",
        "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Printer marks meliputi Crop marks, Bleed marks, Registration marks, dan Color bars.",
      "execution": "Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-13",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-14",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-15",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-16",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-17",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-18",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-19",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-20",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-21",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-22",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-23",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-24",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "multi",
    "questionHtml": "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
    "options": [
      {
        "key": "A",
        "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim)."
      },
      {
        "key": "B",
        "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak)."
      },
      {
        "key": "C",
        "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK)."
      },
      {
        "key": "D",
        "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen."
      },
      {
        "key": "E",
        "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Printer marks meliputi Crop marks, Bleed marks, Registration marks, dan Color bars.",
      "execution": "Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-25",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
      "execution": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
    },
    "explanation": "Analisis desain komunikasi visual: Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-26",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
      "execution": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise).",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-27",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
      "execution": "Pilihan A, B, dan C adalah format file vektor murni."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah format file vektor murni. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-28",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
      "execution": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
    },
    "explanation": "Analisis desain komunikasi visual: Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-29",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
      "execution": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-30",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
      "execution": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah definisi anatomi huruf standar. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-31",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
      "execution": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
    },
    "explanation": "Analisis desain komunikasi visual: Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-32",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
      "latex": "\\text{Ukuran Dokumen Akhir} + \\text{Bleed (3 mm)} + \\text{Crop Marks} + \\text{Safety Margin}",
      "legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control"
    },
    "hints": {
      "concept": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
      "execution": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-33",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
      "latex": "\\text{Komposisi} = \\text{Hierarki} + \\text{Kontras} + \\text{Keseimbangan (Simetris/Asimetris)} + \\text{Whitespace}",
      "legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual"
    },
    "hints": {
      "concept": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
      "execution": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
    },
    "explanation": "Analisis multi-jawaban Desain: Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt. Opsi tepat: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-34",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ANATOMI TIPOGRAFI & MODULAR GRID",
      "latex": "\\text{Kerning (Antar-karakter)} \\neq \\text{Tracking (Seluruh kata)} \\neq \\text{Leading (Jarak antar-baris)}",
      "legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf"
    },
    "hints": {
      "concept": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
      "execution": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
    },
    "explanation": "Analisis desain komunikasi visual: Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning. Jawaban benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-lat-h-35",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL WARNA & RESOLUSI GRAFIS",
      "latex": "\\text{RGB (Aditif, Layar, 72--144 PPI)} \\quad \\longleftrightarrow \\quad \\text{CMYK (Subtraktif, Cetak, 300 DPI)}",
      "legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch"
    },
    "hints": {
      "concept": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
      "execution": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
    },
    "explanation": "Evaluasi kejuruan DKV & Desain: Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI.",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-01",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-02",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-03",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-04",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-05",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-06",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-07",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-08",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-09",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-10",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-11",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-12",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "multi",
    "questionHtml": "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
    "options": [
      {
        "key": "A",
        "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim)."
      },
      {
        "key": "B",
        "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak)."
      },
      {
        "key": "C",
        "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK)."
      },
      {
        "key": "D",
        "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen."
      },
      {
        "key": "E",
        "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-13",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-14",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-15",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-16",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-17",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-18",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-19",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "mcq",
    "questionHtml": "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
    "options": [
      {
        "key": "A",
        "text": "Grafik Vektor dengan model ruang warna CMYK"
      },
      {
        "key": "B",
        "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"
      },
      {
        "key": "C",
        "text": "File GIF animasi terkompresi dengan palet 256 warna"
      },
      {
        "key": "D",
        "text": "File JPEG resolusi rendah dengan profil warna sRGB"
      },
      {
        "key": "E",
        "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-20",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "matrix",
    "questionHtml": "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya."
      },
      {
        "id": "1",
        "text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna."
      },
      {
        "id": "2",
        "text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta."
      },
      {
        "id": "3",
        "text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-21",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "multi",
    "questionHtml": "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
    "options": [
      {
        "key": "A",
        "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu."
      },
      {
        "key": "B",
        "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis."
      },
      {
        "key": "C",
        "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh."
      },
      {
        "key": "D",
        "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur."
      },
      {
        "key": "E",
        "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-22",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "mcq",
    "questionHtml": "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
    "options": [
      {
        "key": "A",
        "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"
      },
      {
        "key": "B",
        "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"
      },
      {
        "key": "C",
        "text": "Leading (jarak vertikal antar baris teks paragraph)"
      },
      {
        "key": "D",
        "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"
      },
      {
        "key": "E",
        "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-23",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "matrix",
    "questionHtml": "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan."
      },
      {
        "id": "1",
        "text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak."
      },
      {
        "id": "2",
        "text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless."
      },
      {
        "id": "3",
        "text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-24",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "multi",
    "questionHtml": "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
    "options": [
      {
        "key": "A",
        "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim)."
      },
      {
        "key": "B",
        "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak)."
      },
      {
        "key": "C",
        "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK)."
      },
      {
        "key": "D",
        "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen."
      },
      {
        "key": "E",
        "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-25",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "mcq",
    "questionHtml": "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"
      },
      {
        "key": "B",
        "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"
      },
      {
        "key": "C",
        "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"
      },
      {
        "key": "D",
        "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"
      },
      {
        "key": "E",
        "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-26",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "matrix",
    "questionHtml": "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak."
      },
      {
        "id": "1",
        "text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah."
      },
      {
        "id": "2",
        "text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi."
      },
      {
        "id": "3",
        "text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-27",
    "subject": "rekayasa_desain",
    "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
    "options": [
      {
        "key": "A",
        "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web."
      },
      {
        "key": "B",
        "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial."
      },
      {
        "key": "C",
        "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional."
      },
      {
        "key": "D",
        "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto."
      },
      {
        "key": "E",
        "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-28",
    "subject": "rekayasa_desain",
    "materi": "PRA-CETAK, UI/UX & HAKI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
    "type": "mcq",
    "questionHtml": "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"
      },
      {
        "key": "B",
        "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"
      },
      {
        "key": "C",
        "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"
      },
      {
        "key": "D",
        "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"
      },
      {
        "key": "E",
        "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-29",
    "subject": "rekayasa_desain",
    "materi": "PRINSIP DESAIN & NIRMANA",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Komposisi, Keseimbangan & Gestalt",
    "type": "matrix",
    "questionHtml": "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda."
      },
      {
        "id": "1",
        "text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder."
      },
      {
        "id": "2",
        "text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi."
      },
      {
        "id": "3",
        "text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "tekd-sim-30",
    "subject": "rekayasa_desain",
    "materi": "TIPOGRAFI & SISTEM GRID",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
    "type": "multi",
    "questionHtml": "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
    "options": [
      {
        "key": "A",
        "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h)."
      },
      {
        "key": "B",
        "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y)."
      },
      {
        "key": "C",
        "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a)."
      },
      {
        "key": "D",
        "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender."
      },
      {
        "key": "E",
        "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  }
];
