# -*- coding: utf-8 -*-
"""
BAHASA MANDARIN - PAKET SOAL SIMULASI HOTS LENGKAP (35 BUTIR)
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / HSK 2–HSK 3
Distribusi:
- 25 Butir: Pilihan Ganda Tunggal (MCQ - man-sim-01 s.d. man-sim-25)
- 5 Butir: Pilihan Ganda Kompleks / Multi-Select (man-sim-26 s.d. man-sim-30)
- 5 Butir: Matriks Asosiasi Benar-Salah (man-sim-31 s.d. man-sim-35)
"""

BAHASA_MANDARIN_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 MCQ ITEMS (man-sim-01 .. man-sim-25)
    # -------------------------------------------------------------
    {
        "id": "man-sim-01",
        "materi": "TATA BAHASA YUFA: PERTANYAAN PILIHAN ALTERNATIF",
        "topic": "Penggunaan Kata Tanya Pilihan '还是' (Háishì) vs '或者' (Huòzhě)",
        "stem": "Pelayan kafe menanyakan pilihan minuman kepada pelanggan:\n'先生，您喝咖啡 ( ... ) 喝茶？'\nKata penghubung pilihan yang TEPAT untuk kalimat tanya interogatif tersebut adalah...",
        "correct": "还是 (háishì - kata hubung 'atau' yang khusus digunakan dalam kalimat tanya pilihan interogatif).",
        "distractors": [
            "或者 (huòzhě - kata hubung 'atau' yang hanya boleh digunakan dalam kalimat pernyataan deklaratif biasa).",
            "而且 (érqiě - konjungsi penambahan kumulatif yang bermakna 'bahkan juga').",
            "但是 (dànshì - konjungsi pertentangan yang bermakna 'tetapi / namun').",
            "因为 (yīnwèi - konjungsi kausalitas yang menandai alasan penyebab)."
        ],
        "formula": {
            "title": "DISTINGSI KATA HUBUNG 'ATAU' MANDARIN (选择连接词辨析)",
            "latex": "\\begin{cases} \\mathbf{\\text{Kalimat Tanya (Interogatif):}} & A + \\mathbf{\\text{还是 (háishì)}} + B \\implies \\text{Pilih } A \\text{ atau } B? \\\\ \\mathbf{\\text{Kalimat Pernyataan (Deklaratif):}} & A + \\mathbf{\\text{或者 (huòzhě)}} + B \\implies A \\text{ atau } B \\text{ (Mana saja boleh)} \\end{cases}",
            "legend": "• Menuntut ketepatan pemilihan konjungsi berdasarkan modalitas kalimat"
        },
        "hints": {
            "concept": "Kata 'atau' dalam kalimat tanya wajib memakai 还是 (háishì). Kata 或者 (huòzhě) hanya untuk kalimat pernyataan biasa.",
            "execution": "Pilih: '还是 (háishì)'."
        }
    },
    {
        "id": "man-sim-02",
        "materi": "TATA BAHASA YUFA: VERBA BANTU MODALITAS WAKTU",
        "topic": "Menyatakan Peristiwa yang Segera Akan Terjadi (就要...了 / 快要...了)",
        "stem": "Petugas stasiun memberi peringatan kepada para penumpang di peron:\n'各位旅客，列车 ( ... ) 开了，请不要在车门附近停留。'\nFrasa penanda waktu yang TEPAT untuk menyatakan bahwa kereta 'sebentar lagi akan segera berangkat' adalah...",
        "correct": "快要 (kuài yào - berpasangan dengan partikel akhir 了 untuk menandai aksi yang segera terwujud dalam hitungan waktu singkat).",
        "distractors": [
            "已经 (yǐjīng - menandai bahwa aksi kereta berangkat telah selesai terjadi di masa lalu).",
            "正在 (zhèngzài - menandai aksi yang sedang berlangsung tepat pada detik sekarang).",
            "曾经 (céngjīng - menandai peristiwa yang pernah terjadi di masa lampau).",
            "刚 (gāng - menandai aksi yang baru saja tuntas sesaat yang lalu)."
        ],
        "formula": {
            "title": "KALA MASA DEPAN SEGERA (即将发生体「快要...了」)",
            "latex": "\\mathbf{\\text{快要 / 就要 (kuài yào / jiù yào)}} + V + \\mathbf{\\text{了 (le)}} \\implies \\text{Akan segera terjadi } V \\text{ dalam waktu dekat}",
            "legend": "• Menunjukkan transisi fase dari persiapan menuju aksi seketika"
        },
        "hints": {
            "concept": "Pola menyatakan 'sebentar lagi/segera akan...': 快要 (kuài yào)... 了: 列车快要开了 (kereta segera akan berangkat).",
            "execution": "Pilih: '快要 (kuài yào)'."
        }
    },
    {
        "id": "man-sim-03",
        "materi": "TATA BAHASA YUFA: PERBANDINGAN TINGKAT LANJUT",
        "topic": "Perbandingan Negatif Menggunakan Méiyǒu (没有)",
        "stem": "Perhatikan data suhu dua kota di Tiongkok pada musim dingin:\nHarbin: -20 derajat Celcius\nBeijing: -5 derajat Celcius\nKalimat perbandingan negatif yang BENAR secara gramatikal untuk menggambarkan bahwa 'Beijing tidak sedingin Harbin' adalah...",
        "correct": "北京没有哈尔滨那么冷。 (Běijīng méiyǒu Hā'ěrbīn nàme lěng - Beijing tidak sedingin Harbin).",
        "distractors": [
            "北京不比哈尔滨那么冷。 (Struktur 'bù bǐ' bermakna Beijing tidak lebih dingin, tapi 'méiyǒu' adalah standar baku untuk menyatakan tidak se-dingin).",
            "北京比哈尔滨没有冷。 (Menempatkan kata méiyǒu di belakang kata bǐ yang merusak sintaksis kalimat).",
            "北京跟哈尔滨一样冷。 (Menyatakan kesetaraan yang bertentangan secara matematis dengan selisih 15 derajat).",
            "哈尔滨没有北京冷。 (Terbalik subjek yang justru memutarbalikkan fakta iklim kedua kota)."
        ],
        "formula": {
            "title": "KOMPARATIF NEGATIF DERAJAT (「没有」表示比较)",
            "latex": "\\mathbf{A + \\text{没有 (méiyǒu)} + B + (\\text{那么 / 这么}) + \\text{Kata Sifat}} \\implies A \\text{ tidak se-} [\\text{Sifat}] \\text{ seperti } B",
            "legend": "• Menunjukkan bahwa derajat kualitas entitas A berada di bawah entitas acuan B"
        },
        "hints": {
            "concept": "Rumus A tidak se-... B: A + 没有 (méiyǒu) + B + (那么) + Sifat -> 北京没有哈尔滨那么冷.",
            "execution": "Pilih: '北京没有哈尔滨那么冷。'."
        }
    },
    {
        "id": "man-sim-04",
        "materi": "TATA BAHASA YUFA: STRUKTUR PENEKANAN KASUS (BǍ-SENTENCE)",
        "topic": "Penempatan Kata Keterangan Negasi dan Waktu pada Kalimat 把",
        "stem": "Dalam kalimat yang menggunakan struktur '把' (*Bǎ*), di manakah letak yang BENAR untuk kata negasi '没' (*méi*) atau '不' (*bù*)?",
        "correct": "Wajib diletakkan TEPAT DI DEPAN kata '把' (sebelum kata 把, contoh: '我没有把钥匙弄丢').",
        "distractors": [
            "Wajib diletakkan di antara kata 把 dan objek penderita (contoh: '我把没有钥匙弄丢').",
            "Wajib diletakkan tepat di depan kata kerja utama (contoh: '我把钥匙没有弄丢').",
            "Wajib diletakkan di akhir kalimat setelah partikel le (contoh: '我把钥匙弄丢没有').",
            "Boleh diletakkan di sembarang posisi karena partikel 把 fleksibel terhadap partikel negasi."
        ],
        "formula": {
            "title": "POSISI NEGASI PADA KALIMAT BA (「把」字句否定词位置法则)",
            "latex": "\\mathbf{S + [\\text{没 / 不 / 别}] + \\text{把 (bǎ)} + \\text{Objek} + V + \\text{Komplemen}} \\quad (\\cancel{\\text{把 + 不 + O}}, \\cancel{\\text{把 + O + 不 + V}})",
            "legend": "• Seluruh kata negasi, modalitas, dan keterangan waktu wajib mendahului kata 把"
        },
        "hints": {
            "concept": "Aturan emas kalimat 把: kata negasi (没/不) dan kata bantu modalitas HARUS diletakkan SEBELUM kata 把 (我没有把... / 你别把...).",
            "execution": "Pilih opsi: Wajib diletakkan TEPAT DI DEPAN kata '把'."
        }
    },
    {
        "id": "man-sim-05",
        "materi": "TATA BAHASA YUFA: KOMPLEMEN KEMUNGKINAN",
        "topic": "Bisa vs Tidak Bisa Melakukan Sesuatu (V + 得/不 + Komplemen)",
        "stem": "Seorang siswa mengeluh karena ruang penyimpanan komputernya sudah penuh sesak:\n'这个硬盘太小了，( ... ) 这么多高清电影。'\nFrasa komplemen kemungkinan yang TEPAT untuk menyatakan 'tidak muat menampung' adalah...",
        "correct": "装不下 (zhuāng bu xià - tidak muat menampung seluruh berkas video karena keterbatasan kapasitas ruang).",
        "distractors": [
            "装得下 (zhuāng de xià - bentuk positif yang berarti muat dan masih memiliki sisa ruang).",
            "装完 (zhuāng wán - komplemen hasil yang hanya berarti selesai mengisi tanpa menilai kapasitas muatan).",
            "不装 (bù zhuāng - penolakan kehendak subjektif untuk tidak mau memasukkan barang).",
            "装好了 (zhuāng hǎo le - menyatakan bahwa proses pemasangan telah rampung dengan baik)."
        ],
        "formula": {
            "title": "KOMPLEMEN KEMUNGKINAN KAPASITAS RUANG (可能补语「装得下 / 装不下」)",
            "latex": "\\begin{cases} \\mathbf{\\text{Kapasitas Muat:}} & \\text{装} + \\mathbf{\\text{得}} + \\text{下 (zhuāng de xià)} \\\\ \\mathbf{\\text{Kapasitas Tidak Muat:}} & \\text{装} + \\mathbf{\\text{不}} + \\text{下 (zhuāng bu xià)} \\end{cases}",
            "legend": "• Menilai kelayakan fisik ruang wadah terhadap volume objek yang hendak ditampung"
        },
        "hints": {
            "concept": "Menyatakan tidak muat menampung menggunakan komplemen kemungkinan negatif: 装不下 (zhuāng bu xià).",
            "execution": "Pilih: '装不下 (zhuāng bu xià)'."
        }
    },
    {
        "id": "man-sim-06",
        "materi": "TATA BAHASA YUFA: ADVERBIA WAKTU RELATIF CEPAT VS LAMBAT",
        "topic": "Penggunaan Jiù (就) vs Cái (才) dalam Penilaian Waktu",
        "stem": "Perhatikan dua kalimat perjalanan berikut:\n1) 坐高铁一个小时 ( A ) 能到，真快啊！(Menilai durasi satu jam sebagai waktu yang sangat cepat dan efisien).\n2) 路上堵车，两个小时 ( B ) 到了，太慢了！(Menilai durasi dua jam sebagai waktu yang lambat dan terlambat).\nKata keterangan yang TEPAT untuk mengisi posisi rasa cepat ( A ) dan rasa lambat ( B ) berturut-turut adalah...",
        "correct": "A: 就 (jiù - menandai waktu yang dinilai cepat, dini, atau lancar), B: 才 (cái - menandai waktu yang dinilai lambat, telat, atau penuh rintangan).",
        "distractors": [
            "A: 才 (cái), B: 就 (jiù) - terbalik persepsi psikologis antara efisiensi waktu dan keterlambatan kemacetan.",
            "A: 都 (dōu), B: 也 (yě) - dōu menandai inklusi dan yě menandai kesamaan yang tidak mengekspresikan tempo.",
            "A: 又 (yòu), B: 再 (zài) - yòu dan zài menandai pengulangan aksi di masa lampau dan masa depan.",
            "A: 就 (jiù), B: 就 (jiù) - mengabaikan kontras emosional antara 'zhēn kuài' dan 'tài màn le'."
        ],
        "formula": {
            "title": "DISTINGSI PSIKOLOGI TEMPO SINTAKSIS (时间快慢副词「就」与「才」)",
            "latex": "\\begin{aligned} \\mathbf{\\text{就 (jiù):}} & \\implies \\text{Cepat / Awal / Mudah / Berjalan Mulus} \\\\ \\mathbf{\\text{才 (cái):}} & \\implies \\text{Lambat / Telat / Susah / Tertunda Rintangan} \\end{aligned}",
            "legend": "• Sifat subyektif penutur yang mewarnai penilaian terhadap durasi angka waktu riil"
        },
        "hints": {
            "concept": "Satu jam sudah sampai (cepat): 就 (jiù). Dua jam baru sampai (lambat/macet): 才 (cái).",
            "execution": "Pilih opsi: 'A: 就 (jiù), B: 才 (cái)'."
        }
    },
    {
        "id": "man-sim-07",
        "materi": "TATA BAHASA YUFA: VERBA REDUPLIKASI",
        "topic": "Makna Gramatikal Pengulangan Kata Kerja (动词重叠: 看看, 听听, 试一试)",
        "stem": "Dalam situasi berbelanja baju, pramuniaga tersenyum dan berkata kepada calon pembeli:\n'这件羽绒服是今年最新的款式，您可以 [试一试]。'\nMakna pragmatik dari bentuk pengulangan kata kerja (*reduplikasi*) [试一试] (shì yi shì) adalah...",
        "correct": "Melakukan tindakan mencoba pakaian tersebut dalam durasi waktu yang singkat dan santai (*mencoba-coba sebentar*).",
        "distractors": [
            "Kewajiban membeli pakaian tersebut secara berulang-ulang sebanyak tiga kali transaksi.",
            "Perintah tegas untuk menguji ketahanan kain pakaian dengan merobeknya di hadapan kasir.",
            "Larangan keras bagi pelanggan untuk menyentuh permukaan kain pakaian di gantungan toko.",
            "Membayar uang muka terlebih dahulu sebelum pakaian boleh dilihat dari jarak dekat."
        ],
        "formula": {
            "title": "MAKNA ASPEK REDUPLIKASI VERBAL (动词重叠语法功能)",
            "latex": "\\mathbf{V \\text{-一-} V \\quad / \\quad VV} \\implies \\begin{cases} \\text{1. Waktu singkat / Aksi sekilas (一下)} \\\\ \\text{2. Bernada santai / Mengurangi nada imperatif kaku} \\\\ \\text{3. Mencoba-coba (尝试)} \\end{cases}",
            "legend": "• Menghaluskan tutur bahasa agar terdengar ramah dan tidak menekan mitra bicara"
        },
        "hints": {
            "concept": "Reduplikasi kata kerja (试一试 shì yi shì) bermakna melakukan perbuatan sebentar/mencoba santai (mencoba sebentar).",
            "execution": "Pilih opsi: Melakukan tindakan mencoba pakaian dalam durasi singkat dan santai."
        }
    },
    {
        "id": "man-sim-08",
        "materi": "TATA BAHASA YUFA: STRUKTUR PENEKANAN KEMAUAN SENDIRI",
        "topic": "Penggunaan Kata Ganti Refleksif Zìjǐ (自己)",
        "stem": "Lengkapilah kalimat kemandirian anak asrama berikut:\n'离开父母以后，他学会了 ( ... ) 做饭和洗衣服。'\nKata penanda kemandirian reflektif yang TEPAT melengkapi kalimat tersebut adalah...",
        "correct": "自己 (zìjǐ - diri sendiri / secara mandiri tanpa bantuan orang lain).",
        "distractors": [
            "别人 (biérén - orang lain yang bertentangan dengan konsep kemandirian anak asrama).",
            "大家 (dàjiā - semua orang / khalayak ramai).",
            "人家 (rénjia - orang tersebut / orang lain).",
            "双方 (shuāngfāng - kedua belah pihak dalam perundingan perjanjian)."
        ],
        "formula": {
            "title": "PRONOMINA REFLEKSIF MANDIRIAN (反身代词「自己」)",
            "latex": "\\mathbf{\\text{Subjek}} + \\mathbf{\\text{自己 (zìjǐ)}} + V \\implies \\text{Melakukan aksi } V \\text{ secara mandiri oleh diri sendiri}",
            "legend": "• Menegaskan agensi personal dalam menyelesaikan urusan domestik"
        },
        "hints": {
            "concept": "Melakukan perbuatan secara mandiri/sendiri: 自己做饭 (memasak sendiri).",
            "execution": "Pilih: '自己 (zìjǐ)'."
        }
    },
    {
        "id": "man-sim-09",
        "materi": "TATA BAHASA YUFA: PERTANYAAN RETORIS ELIPTIS NE (呢)",
        "topic": "Fungsi Partikel Ne (呢) Menanyakan Lokasi Entitas yang Hilang",
        "stem": "Seseorang sedang bersiap berangkat ke kantor dan tiba-tiba tidak menemukan ponselnya di meja:\n'奇怪，我的手机 ( ... )？刚才还在这里呢！'\nPartikel penutup kalimat singkat yang TEPAT untuk menanyakan 'Di manakah gerangan ponsel saya?' secara eliptis adalah...",
        "correct": "呢 (ne - partikel interogatif yang ketika menempel langsung pada nomina berfungsi menanyakan keberadaan 'di mana objek tersebut?').",
        "distractors": [
            "吗 (ma - partikel penanya ya/tidak yang menuntut adanya predikat verba lengkap).",
            "吧 (ba - penanda dugaan yang tidak tepat digunakan saat panik mencari benda hilang).",
            "了 (le - penanda ketuntasan yang tidak membentuk kalimat tanya pencarian posisi benda).",
            "啊 (a - partikel seru modalitas yang tidak memiliki daya interogatif lokatif mandiri)."
        ],
        "formula": {
            "title": "FUNGSI INTEROGATIF ELIPTIS PARTIKEL NE (省略疑问句「名词＋呢」)",
            "latex": "\\mathbf{\\text{Nomina (我的手机)}} + \\mathbf{\\text{呢 (ne)}} \\implies \\text{Di manakah gerangan } [\\text{Nomina}]? \\quad (\\equiv \\text{我的手机在哪里？})",
            "legend": "• Menunjukkan pencarian cepat terhadap entitas yang mendadak lenyap dari jangkauan"
        },
        "hints": {
            "concept": "Kata Benda + 呢 (ne) berfungsi menanyakan 'di mana benda itu berada?': 我的手机呢？(Di mana ponsel saya?).",
            "execution": "Pilih: '呢 (ne)'."
        }
    },
    {
        "id": "man-lat-m-10",
        "materi": "TATA BAHASA YUFA: PENGULANGAN KATA KERJA DENGAN YÒU (又) VS ZÀI (再)",
        "topic": "Pengulangan Aksi Masa Lampau (又) vs Pengulangan Masa Depan (再)",
        "stem": "Perhatikan dua kalimat pengulangan perbuatan berikut:\n1) 昨天的电影太精彩了，我明天想 ( A ) 看一遍。(Pengulangan yang direncanakan di masa depan).\n2) 他今天早上 ( B ) 迟到了，老师很生气。(Pengulangan kejadian buruk yang sudah terbukti terjadi tadi pagi).\nKata keterangan pengulangan yang TEPAT untuk ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: 再 (zài - pengulangan aksi di masa yang akan datang), B: 又 (yòu - pengulangan peristiwa yang sudah terjadi di masa lampau).",
        "distractors": [
            "A: 又 (yòu), B: 再 (zài) - terbalik mutlak antara dimensi waktu lampau dan rencana masa depan.",
            "A: 还 (hái), B: 也 (yě) - tidak menandai pengulangan tindakan verba spesifik.",
            "A: 再 (zài), B: 再 (zài) - mengabaikan fakta bahwa keterlambatan tadi pagi sudah nyata terjadi.",
            "A: 又 (yòu), B: 又 (yòu) - mengabaikan fakta bahwa menonton besok adalah rencana kehendak."
        ],
        "formula": {
            "title": "DISTINGSI PENGULANGAN AKSI MANDARIN (重复副词「又」与「再」)",
            "latex": "\\begin{cases} \\mathbf{\\text{Masa Depan / Belum Terjadi:}} & \\mathbf{\\text{再 (zài)}} + V \\implies \\text{Melakukan lagi kelak (再见 / 再看一遍)} \\\\ \\mathbf{\\text{Masa Lampau / Sudah Terjadi:}} & \\mathbf{\\text{又 (yòu)}} + V + \\text{了} \\implies \\text{Terulang lagi terjadi (他又迟到了)} \\end{cases}",
            "legend": "• Pilar penguasaan aspek temporalitas dalam standar kemahiran HSK 3"
        },
        "hints": {
            "concept": "Mau nonton lagi besok (masa depan) -> 再 (zài). Tadi pagi terlambat lagi (sudah terjadi di masa lampau) -> 又 (yòu).",
            "execution": "Pilih: 'A: 再 (zài), B: 又 (yòu)'."
        }
    },
    {
        "id": "man-sim-11",
        "materi": "DOKKAI TEKSTUAL: WACANA SOSIAL RUMAH TANGGA",
        "topic": "Pembagian Peran Pengasuhan Anak dan Tradisi Kakek-Nenek (Gédài Fǔyǎng)",
        "stem": "Bacalah teks mengenai pola pengasuhan keluarga modern di kota-kota besar Tiongkok berikut:\n--------------------------------------------------\n在中国的大城市里，“隔代抚养”（即由 祖父母、外祖父母 帮助 照看 孙辈）是非常 普遍的 现象。由于 年轻父母的 工作节奏快、加班多、通勤时间长，很多 双职工家庭 没有 足够的时间 照顾年幼的 孩子。爷爷奶奶不仅 负责 接送孩子 上下学，还 操持 全家人的 饮食起居。这种 模式 虽然 极大地 减轻了 年轻人的 经济和 生活压力，但 也常因 两代人在 育儿观念、饮食营养和 教育方式上的 差异而 产生 家庭小摩擦。\n--------------------------------------------------\nBerdasarkan wacana di atas, mengapa fenomena pengasuhan anak oleh kakek-nenek (*Gédài Fǔyǎng*) menjadi sangat lazim di kota-kota besar Tiongkok?",
        "correct": "Karena kedua orang tua sama-sama bekerja penuh waktu dengan jam lembur panjang dan jarak tempuh kantor yang jauh, sehingga membutuhkan bantuan orang tua mereka dalam mengurus anak dan rumah tangga.",
        "distractors": [
            "Karena undang-undang perkawinan Tiongkok melarang keras para ibu kandung untuk tinggal serumah dengan anak kandungnya.",
            "Karena kakek-nenek diwajibkan oleh dinas pendidikan untuk menggantikan seluruh peran guru di sekolah dasar.",
            "Karena biaya sekolah taman kanak-kanak digratiskan khusus bagi anak-anak yang diantar oleh kakek kandung.",
            "Agar para orang tua muda dapat menggunakan seluruh waktu liburnya untuk berkeliling dunia tanpa anak."
        ],
        "formula": {
            "title": "FAKTOR KAUSALITAS GEDAI FUYANG (「隔代抚养」成因机制)",
            "latex": "\\begin{cases} \\text{Ritme Kerja Cepat \\& Lembur Banyak (加班多)} \\\\ \\text{Waktu Komuter Panjang (通勤时间长)} \\\\ \\text{Pasangan Bekerja Keduanya (双职工)} \\end{cases} \\implies \\mathbf{\\text{Ketergantungan Pengasuhan Kakek-Nenek}}",
            "legend": "• Fenomena transisi demografis dan struktur ketenagakerjaan urban modern"
        },
        "hints": {
            "concept": "Teks menyatakan: '由于 年轻父母的 工作节奏快、加班多、通勤时间长，很多 双职工家庭 没有 足够的时间 照顾年幼的 孩子' (karena ritme kerja cepat, lembur, komuter jauh, kedua ortu bekerja).",
            "execution": "Pilih opsi yang menjelaskan kedua orang tua bekerja penuh waktu dengan jam lembur panjang dan perjalanan komuter jauh."
        }
    },
    {
        "id": "man-sim-12",
        "materi": "DOKKAI TEKSTUAL: EVALUASI DAMPAK SOSIAL KELUARGA",
        "topic": "Analisis Masalah dalam Pengasuhan Anak oleh Kakek-Nenek",
        "stem": "Melanjutkan wacana nomor sebelumnya, dampak samping atau potensi gesekan (*mócā*) yang sering timbul dari pola pengasuhan antargenerasi tersebut adalah...",
        "correct": "Timbulnya perbedaan sudut pandang antara generasi tua dan generasi muda dalam hal pola pendidikan anak, gizi makanan, dan konsep pengasuhan.",
        "distractors": [
            "Keluarga mengalami kebangkrutan finansial mendadak akibat biaya konsumsi makanan kakek-nenek yang terlalu mahal.",
            "Pemerintah kota mencabut hak kepemilikan apartemen keluarga yang tinggal bersama tiga generasi.",
            "Anak-anak menolak belajar berbicara bahasa Mandarin dan hanya mau berkomunikasi dengan bahasa isyarat kuno.",
            "Kakek dan nenek menuntut pembayaran gaji profesional dengan nominal setara manajer bank nasional."
        ],
        "formula": {
            "title": "KONFLIK PENDIDIKAN ANTARGENERASI (代际育儿观念冲突)",
            "latex": "\\mathbf{\\text{两代人观念差异 (Beda Pola Pikir 2 Generasi)}} \\implies \\mathbf{\\text{家庭小摩擦 (Gesekan/Friksi Kecil Rumah Tangga)}}",
            "legend": "• Pergeseran orientasi antara pola asuh tradisional (memanjakan) vs edukasi ilmiah modern"
        },
        "hints": {
            "concept": "Teks menyebutkan: '也常因 两代人在 育儿观念、饮食营养和 教育方式上的 差异而 产生 家庭小摩擦' (perbedaan dalam konsep mendidik anak, nutrisi, dan cara asuh).",
            "execution": "Pilih opsi yang menyebutkan perbedaan sudut pandang dalam konsep pendidikan anak, nutrisi, dan pola asuh."
        }
    },
    {
        "id": "man-sim-13",
        "materi": "DOKKAI TEKSTUAL: BIOGRAFI TOKOH FILSAFAT KLASIK",
        "topic": "Konsep Kebajikan Ren dan Pendidikan Konfusius (Kǒngzǐ - 孔子)",
        "stem": "Bacalah teks mengenai tokoh pemikir agung Tiongkok berikut:\n--------------------------------------------------\n孔子（公元前551年－公元前479年）是 中国古代 伟大的 思想家、教育家，儒家学派的 创始人。孔子 核心的 哲学思想是“仁”（Rén），即“仁者爱人”，强调 人与人之间 要有 普遍的 关爱与 同理心。在 教育方面，孔子 首创 私学，提倡“有教无类”（不论 贫富贵贱，人人 都有 接受教育的 权利）和“因材施教”（根据 学生 不同的 才能和 特点 进行 针对性的 教育）。他的 言论被 弟子们 记录在《论语》一书中，对 整个 东亚文明 产生了 深远的影响。\n--------------------------------------------------\nPrinsip pendidikan Konfusius yang menegaskan bahwa 'setiap orang memiliki hak yang sama untuk memperoleh pendidikan tanpa memandang status kekayaan maupun derajat sosial' tercermin dalam pepatah...",
        "correct": "有教无类 (Yǒu jiào wú lèi - dalam menyelenggarakan pendidikan tidak boleh ada sekat kasta atau diskriminasi kelas).",
        "distractors": [
            "因材施教 (Yīn cái shī jiào - prinsip mendidik yang disesuaikan dengan bakat dan karakteristik unik individu murid).",
            "仁者爱人 (Rén zhě ài rén - konsep etika kebajikan bahwa manusia bijak harus mengasihi sesama manusia).",
            "温故知新 (Wēn gù zhī xīn - prinsip belajar mengulang materi lama guna menemukan pemahaman baru).",
            "学而优则仕 (Xué ér yōu zé shì - konsep bahwa sarjana berprestasi unggul hendaknya mengabdi menjadi pejabat negara)."
        ],
        "formula": {
            "title": "HERMENEUTIKA PRINSIP EDUKASI KONFUSIUS (孔子教育思想核心)",
            "latex": "\\begin{cases} \\mathbf{\\text{有教无类 (Yǒu jiào wú lèi):}} & \\mathbf{\\text{Demokratisasi Hak Akses Pendidikan Tanpa Kasta}} \\\\ \\text{因材施教 (Yīn cái shī jiào):} & \\text{Diferensiasi Pembelajaran Sesuai Potensi Murid} \\end{cases}",
            "legend": "• Tonggak revolusi pedagogis yang meruntuhkan monopoli aristokrasi kekaisaran atas literasi"
        },
        "hints": {
            "concept": "Teks menyatakan: '有教无类（不论 贫富贵贱，人人 都有 接受教育的 权利）'. Prinsip tanpa membedakan kaya/miskin adalah 有教无类 (Yǒu jiào wú lèi).",
            "execution": "Pilih: '有教无类 (Yǒu jiào wú lèi)'."
        }
    },
    {
        "id": "man-sim-14",
        "materi": "DOKKAI TEKSTUAL: METODE PEMBELAJARAN KONFUSIUS",
        "topic": "Konsep Pembelajaran Berdiferensiasi (Yīncái Shījiào - 因材施教)",
        "stem": "Melanjutkan wacana Konfusius di atas, prinsip manakah yang menekankan bahwa seorang pendidik harus menyesuaikan materi dan gaya mengajar berdasarkan keunikan bakat dan karakter masing-masing murid?",
        "correct": "因材施教 (Yīn cái shī jiào - mendidik sesuai dengan potensi bahan dan karakteristik siswa).",
        "distractors": [
            "有教无类 (Prinsip kesetaraan akses pendidikan tanpa diskriminasi kasta).",
            "三人行必有我师 (Prinsip bahwa dari tiga orang yang berjalan bersama pasti ada yang bisa menjadi guru kita).",
            "学而不思则罔 (Peringatan bahwa belajar tanpa berpikir kritis akan tersesat dalam kebingungan).",
            "道不同不相为谋 (Prinsip tidak bersekutu dengan orang yang berbeda jalur prinsip moral)."
        ],
        "formula": {
            "title": "PEDAGOGI DIFERENSIASI KLASIK (「因材施教」教学论)",
            "latex": "\\text{因 (Berdasarkan)} + \\text{材 (Karakter/Bakat)} + \\text{施 (Menerapkan)} + \\text{教 (Pendidikan)} \\implies \\mathbf{\\text{Pembelajaran Berdiferensiasi}}",
            "legend": "• Menghindari standardisasi seragam yang membungkam keunikan talenta murid"
        },
        "hints": {
            "concept": "Teks menyatakan: '因材施教（根据 学生 不同的 才能和 特点 进行 针对性的 教育）' (mendidik sesuai bakat dan karakteristik unik murid).",
            "execution": "Pilih: '因材施教 (Yīn cái shī jiào)'."
        }
    },
    {
        "id": "man-sim-15",
        "materi": "DOKKAI TEKSTUAL: WARISAN ALAM & PARIWISATA",
        "topic": "Sungai Yangtze (Chángjiāng) dan Keajaiban Tiga Ngarai (Sānxiá)",
        "stem": "Bacalah wacana geografi dan lingkungan berikut:\n--------------------------------------------------\n长江是 中国也是 亚洲第一大河，全长 约 6300公里。它 发源于 青藏高原，流经 十一个 省市自治区，最终 注入 东海。在 长江上游，有着 举世闻名的“长江三峡”（瞿塘峡、巫峡、西陵峡），两岸 峡谷 奇峰耸立，风光 极其 雄伟壮观。为了 防洪、发电和 改善航运，中国在此 建造了 世界上最大的 水利枢纽工程——三峡大坝。三峡工程 不仅 提供了 源源不断的 清洁电能，也 改变了 长江的 航道条件。\n--------------------------------------------------\nManfaat multifungsi apakah yang dihasilkan dari mega proyek Bendungan Tiga Ngarai (*Sānxiá Dàbà*) menurut teks di atas?",
        "correct": "Pengendalian banjir, pembangkitan energi listrik tenaga air yang ramah lingkungan, serta perbaikan jalur navigasi transportasi pelayaran sungai.",
        "distractors": [
            "Pembuatan tambang batu bara terbuka raksasa di sepanjang dasar aliran ngarai sungai.",
            "Penimbunan air tawar untuk dialirkan seluruhnya ke samudra Arktik di kutub utara.",
            "Pembangunan jalur pacuan kuda internasional di atas puncak bendungan beton.",
            "Pengalihan seluruh rute penerbangan pesawat komersial internasional melintasi ngarai."
        ],
        "formula": {
            "title": "TRILOGI MANFAAT WADUK TIGA NGARAI (三峡工程的综合效益)",
            "latex": "\\mathbf{\\text{三峡大坝}} \\implies \\begin{cases} \\mathbf{\\text{防洪 (Fánghóng / Kendali Banjir)}} \\\\ \\mathbf{\\text{发电 (Fādiàn / Pembangkit Listrik Hijau)}} \\\\ \\mathbf{\\text{改善航运 (Gǎishàn hángyùn / Perbaikan Pelayaran)}} \\end{cases}",
            "legend": "• Infrastruktur hidroelektrik terintegrasi penopang dekarbonisasi dan logistik Tiongkok"
        },
        "hints": {
            "concept": "Teks menyebutkan: '为了 防洪、发电和 改善航运，中国在此 建造了 世界上最大的 水利枢纽工程——三峡大坝' (untuk kendali banjir, pembangkit listrik, dan perbaikan pelayaran).",
            "execution": "Pilih opsi: Pengendalian banjir, pembangkit listrik tenaga air ramah lingkungan, dan perbaikan navigasi pelayaran."
        }
    },
    {
        "id": "man-sim-16",
        "materi": "MOJIGOI: RADIKAL KANJI MAKANAN",
        "topic": "Radikal Makanan / Nasi (饣 - Shízìpáng)",
        "stem": "Dalam sistem pembentukan karakter Hanzi, karakter yang memuat radikal 'Makanan' (*Shízìpáng* - 饣) biasanya berkaitan dengan panganan atau aktivitas kuliner. Karakter manakah yang memuat radikal tersebut?",
        "correct": "饭 (fàn - nasi / makanan pokok harian).",
        "distractors": [
            "跑 (pǎo - berlari yang beradikalkan kaki 足).",
            "睡 (shuì - tidur yang beradikalkan mata 目).",
            "问 (wèn - bertanya yang beradikalkan pintu 门).",
            "玩 (wán - bermain yang beradikalkan giok 王/玉)."
        ],
        "formula": {
            "title": "RADIKAL PANGANAN SHIZIPANG (部首「饣」语义系统)",
            "latex": "\\mathbf{[饣 (Shízìpáng / Pangan)]} \\implies \\mathbf{\\text{饭 (fàn / Nasi)}} \\quad / \\quad \\text{馆 (guǎn / Kedai)} \\quad / \\quad \\text{饱 (bǎo / Kenyang)}",
            "legend": "• Menghubungkan secara visual antara bentuk karakter dengan konsumsi makanan nutrisi"
        },
        "hints": {
            "concept": "Radikal 饣 berkaitan dengan makanan. '饭' (fàn) berarti nasi/makanan.",
            "execution": "Pilih: '饭 (fàn)'."
        }
    },
    {
        "id": "man-sim-17",
        "materi": "TATA BAHASA YUFA: PERTANYAAN RETORIS GANDA",
        "topic": "Bentuk Pertanyaan Afirmatif-Negatif (V-不-V / A-不-A)",
        "stem": "Dalam bahasa Mandarin, pertanyaan pilihan ya/tidak dapat dibentuk dengan mengulang predikat secara afirmatif-negatif (*Zhengfan Yiwenju*). Kalimat manakah yang merupakan bentuk *Zhengfan Yiwenju* yang BENAR?",
        "correct": "你明天去不去图书馆？ (Nǐ míngtiān qù bu qù túshūguǎn? - besok kamu pergi atau tidak pergi ke perpustakaan?).",
        "distractors": [
            "你明天去不去图书馆吗？ (Dilarang keras menyisipkan partikel tanya 'ma' di akhir kalimat yang sudah berstruktur Zhengfan).",
            "你明天去图书馆不去吗？ (Susunan kata kacau yang memecah frasa kata kerja ke ujung kalimat).",
            "你明天是不是去图书馆吗？ (Penggunaan dobel penanya shì bu shì bersama partikel ma yang redundan).",
            "你去图书馆很忙不忙？ (Pencampuran kata keterangan hěn di dalam konstruksi Zhengfan kata sifat)."
        ],
        "formula": {
            "title": "ATURAN MUTLAK PERTANYAAN REGULER (正反疑问句禁忌规则)",
            "latex": "\\mathbf{V + \\text{不} + V \\implies \\text{Pertanyaan Sahih}} \\quad (\\cancel{V + \\text{不} + V + \\mathbf{\\text{吗}}})",
            "legend": "• Larangan mutlak: Struktur V-bù-V TIDAK PERNAH boleh diakhiri partikel 吗 (ma)"
        },
        "hints": {
            "concept": "Struktur pertanyaan bolak-balik (V-不-V) seperti '去不去' TIDAK BOLEH ditambahi '吗' di belakangnya. Bentuk yang benar: 你明天去不去图书馆？",
            "execution": "Pilih: '你明天去不去图书馆？'."
        }
    },
    {
        "id": "man-sim-18",
        "materi": "TATA BAHASA YUFA: PEMBAGIAN PREDIKAT WAKTU LAMPAU",
        "topic": "Penolakan Kejadian Masa Lampau dengan Méiyǒu (没有 / 没)",
        "stem": "Seseorang ingin menegaskan bahwa kemarin dirinya 'sama sekali tidak pergi menonton film'. Kalimat negasi masa lampau yang BENAR adalah...",
        "correct": "我昨天没有去看电影。 (Wǒ zuótiān méiyǒu qù kàn diànyǐng - saya kemarin tidak pergi menonton film).",
        "distractors": [
            "我昨天不去看了电影。 (Dilarang menggunakan kata negasi 'bù' bersama partikel aspek le untuk peristiwa lampau).",
            "我昨天没有看了电影。 (Dilarang menyisipkan partikel aspek 'le' di dalam kalimat negasi méiyǒu).",
            "我昨天看电影不去了。 (Susunan kata terbalik yang tidak memiliki kohesi predikatif).",
            "我昨天不去看电影了。 (Bú qù ... le menandai pembatalan niat mendadak, bukan penegasan fakta historis ketiadaan aktivitas)."
        ],
        "formula": {
            "title": "NEGASI ASPEK LAMPAU (过去完成的否定范式)",
            "latex": "\\mathbf{\\text{Masa Lampau (昨天)}} + \\mathbf{\\text{没有 (méiyǒu)}} + V \\quad (\\cancel{\\text{没有}} + V + \\cancel{\\mathbf{\\text{了}}})",
            "legend": "• Ketika dinegasikan dengan 没有, partikel ketuntasan 了 WAJIB dihilangkan dari kalimat"
        },
        "hints": {
            "concept": "Negasi peristiwa masa lalu menggunakan 没有 (méiyǒu) dan TIDAK BOLEH memakai 了 di belakangnya. Bentuk baku: 我昨天没有去看电影。",
            "execution": "Pilih: '我昨天没有去看电影。'."
        }
    },
    {
        "id": "man-sim-19",
        "materi": "MOJIGOI: KATA BANTU BILANGAN KENDARAAN",
        "topic": "Satuan Hitung Kendaraan Bermotor (辆 - Liàng)",
        "stem": "Ayah baru saja membeli sebuah mobil keluarga baru. Kalimat dengan kata bantu bilangan (*liàngcí*) yang TEPAT adalah...",
        "correct": "爸爸买了一辆新汽车。 (Bàba mǎi le yí liàng xīn qìchē - ayah membeli sebuah mobil baru dengan liangci liàng).",
        "distractors": [
            "爸爸买了一张新汽车。 (Zhāng adalah satuan untuk benda lembaran rata, bukan untuk kendaraan bermotor).",
            "爸爸买了一台新汽车。 (Tái adalah satuan untuk mesin elektronik atau perkakas pabrik).",
            "爸爸买了一条新汽车。 (Tiáo adalah satuan untuk benda memanjang lentur seperti celana atau ikan).",
            "爸爸买了一支新汽车。 (Zhī adalah satuan untuk tangkai bunga atau pena tulis)."
        ],
        "formula": {
            "title": "LIANGCI TRANSPORTASI DARAT (陆路车辆专用量词)",
            "latex": "\\text{Mobil / Truk / Sepeda} \\implies \\mathbf{\\text{辆 (liàng)}} \\implies \\text{一辆汽车 / 一辆自行车}",
            "legend": "• Memuat radikal kereta perang tradisional (车 - chē) pada sisi kirinya"
        },
        "hints": {
            "concept": "Kata bantu bilangan untuk mobil/kendaraan beroda adalah 辆 (liàng): 一辆新汽车.",
            "execution": "Pilih: '爸爸买了一辆新汽车。'."
        }
    },
    {
        "id": "man-sim-20",
        "materi": "TATA BAHASA YUFA: PERNYATAAN WAKTU JAM DAN MENIT",
        "topic": "Penulisan Notasi Waktu Kurang Seperempat (差一刻 - Chà Yí Kè)",
        "stem": "Jam di dinding menunjukkan pukul 08.45 (pukul sembilan kurang 15 menit). Cara pengucapan waktu yang BENAR dalam bahasa Mandarin adalah...",
        "correct": "差一刻九点 (Chà yí kè jiǔ diǎn - kurang satu seperempat jam/15 menit menuju pukul sembilan).",
        "distractors": [
            "八点三刻点 (Kombinasi kata yang tidak baku karena mengulang kata diǎn dua kali).",
            "九点过十五分刻 (Pencampuran mubazir antara menit fēn dengan satuan kè).",
            "差十五刻九点 (Keliru mengartikan satu kè sebagai 1 menit sehingga menjadi kurang 15 kè).",
            "八点半一刻 (Bentuk tidak lazim dalam ortografi jam Mandarin)."
        ],
        "formula": {
            "title": "NOTASI WAKTU FRAKSIONAL KÈ (汉语刻度时间表达)",
            "latex": "\\begin{aligned} \\text{1 刻 (yí kè)} & \\equiv 15 \\text{ Menit} \\\\ \\mathbf{\\text{08:45}} & \\equiv \\mathbf{\\text{差一刻九点 (Chà yí kè jiǔ diǎn)}} \\quad \\lor \\quad \\text{八点四十五分} \\end{aligned}",
            "legend": "• Chà (kurang), Yí kè (15 menit), Jiǔ diǎn (pukul 9)"
        },
        "hints": {
            "concept": "Pukul 08.45 = jam 9 kurang 15 menit. 15 menit adalah 一刻 (yí kè). Jadi: 差一刻九点 (chà yí kè jiǔ diǎn).",
            "execution": "Pilih: '差一刻九点 (Chà yí kè jiǔ diǎn)'."
        }
    },
    {
        "id": "man-sim-21",
        "materi": "JIĀOJÌ: ETIKA BERTANYA ALAMAT DI JALAN",
        "topic": "Penggunaan Kata Permisi 'Qǐngwèn' (请问) Sebelum Bertanya",
        "stem": "Saat tersesat di kota Shanghai dan ingin menanyakan arah menuju stasiun metro terdekat kepada pejalan kaki, ungkapan pembuka yang WAJIB diucapkan demi menjaga kesopanan adalah...",
        "correct": "请问 (Qǐngwèn - permisi, bolehkah saya bertanya sebentar).",
        "distractors": [
            "听我说 (Tīng wǒ shuō - dengarkan perkataan saya yang bernada menuntut perhatian secara arogan).",
            "给我说 (Gěi wǒ shuō - katakan kepada saya yang bernada memaksa).",
            "你告诉我 (Nǐ gàosu wǒ - suruhan langsung tanpa formula kesantunan).",
            "看这里 (Kàn zhèlǐ - suruhan untuk melihat ke arah pembicara)."
        ],
        "formula": {
            "title": "FORMULA KESOPANAN BERTANYA (礼貌问询规范)",
            "latex": "\\mathbf{\\text{请问 (Qǐngwèn / Permisi Numpang Tanya)}} + \\text{Pertanyaan Alamat / Informasi}",
            "legend": "• Menunjukkan etika santun penutur sebelum meminta waktu orang asing di jalan"
        },
        "hints": {
            "concept": "Menanyakan arah atau informasi kepada orang di jalan selalu diawali dengan '请问' (qǐngwèn - permisi numpang tanya).",
            "execution": "Pilih: '请问 (Qǐngwèn)'."
        }
    },
    {
        "id": "man-sim-22",
        "materi": "JIĀOJÌ & PRAGMATIKA: ETIKA BELANJA PASAR",
        "topic": "Ungkapan Meminta Diskon (便宜一点儿吧 - Piányi Yìdiǎnr Ba)",
        "stem": "Saat berbelanja suvenir di pasar seni jalanan Wangfujing, pembeli merasa harga yang ditawarkan penjual terlalu mahal. Kalimat tawar-menawar santai yang TEPAT diucapkan pembeli adalah...",
        "correct": "太贵了，便宜一点儿吧！ (Tài guì le, piányi yìdiǎnr ba! - terlalu mahal, tolong murah sedikit ya!).",
        "distractors": [
            "太便宜了，给贵一点儿吧！ (Menyatakan barang terlalu murah dan meminta penjual menaikkan harga).",
            "我不给钱，你送给我吧！ (Meminta barang secara cuma-cuma tanpa mau membayar uang).",
            "你的东西是假货，退钱！ (Tuduhan kasar barang tiruan palsu tanpa pembuktian yang memicu perselisihan).",
            "我不买了，全部扔掉吧！ (Menyuruh penjual membuang seluruh barang dagangannya)."
        ],
        "formula": {
            "title": "PRAGMATIK TAWAR MENAWAR PASAR (集市议价常规句式)",
            "latex": "\\mathbf{\\text{太贵了 (Tài guì le / Kemahalan)}} + \\mathbf{\\text{便宜一点儿吧 (Piányi yìdiǎnr ba / Lebih murah sedikit ya)}}",
            "legend": "• Menggunakan partikel saran 'ba' untuk melunakkan negosiasi perdagangan"
        },
        "hints": {
            "concept": "Menawar harga secara santun: 太贵了，便宜一点儿吧！(Tài guì le, piányi yìdiǎnr ba!).",
            "execution": "Pilih: '太贵了，便宜一点儿吧！'."
        }
    },
    {
        "id": "man-sim-23",
        "materi": "JIĀOJÌ & KULTUR: PELEPASAN PELANCONG",
        "topic": "Doa Keselamatan Perjalanan Jauh (Yílù Shùnfēng - 一路顺风)",
        "stem": "Sahabat Anda hendak naik pesawat terbang untuk kembali ke tanah airnya setelah menyelesaikan studi pertukaran pelajar. Ungkapan ucapan perpisahan dan doa keselamatan perjalanan yang TEPAT adalah...",
        "correct": "祝你一路平安！ / 祝你一路顺风！ (Zhù nǐ yílù píng'ān / yílù shùnfēng - semoga perjalanan Anda lancar, selamat, dan berhembus angin sejuk).",
        "distractors": [
            "祝你新婚快乐！ (Ucapan selamat atas pernikahan bahagia pengantin baru).",
            "祝你早日康复！ (Ucapan lekas sembuh yang khusus ditujukan kepada orang yang sedang terbaring sakit).",
            "祝你工作顺利！ (Ucapan selamat bekerja dan sukses dalam karier kantor harian).",
            "祝你生意兴隆！ (Ucapan semoga bisnis toko laris manis dan makmur bagi pengusaha)."
        ],
        "formula": {
            "title": "UNGKAPAN DOA PERJALANAN (送别祝愿语)",
            "latex": "\\mathbf{\\text{一路顺风 (Yílù shùnfēng)}} \\quad / \\quad \\mathbf{\\text{一路平安 (Yílù píng'ān)}} \\implies \\text{Selamat Jalan \\& Tiba dengan Selamat}",
            "legend": "• Idiom klasik pelayaran kapal layar yang diadaptasi menjadi doa keselamatan transportasi modern"
        },
        "hints": {
            "concept": "Mendoakan orang yang hendak bepergian jauh/naik pesawat: 祝你一路平安！ / 一路顺风！",
            "execution": "Pilih opsi doa keselamatan perjalanan (yílù píng'ān / yílù shùnfēng)."
        }
    },
    {
        "id": "man-sim-24",
        "materi": "BUDAYA & ETIKA: TABU MEMOTONG MIE ULANG TAHUN",
        "topic": "Filosofi Mi Panjang Umur (Chángshòumiàn - 长寿面)",
        "stem": "Dalam perayaan ulang tahun tradisional Tionghoa, seseorang disuguhi semangkuk 'Mi Panjang Umur' (*Chángshòumiàn*). Mengapa saat memakan mi tersebut DILARANG memotong helaian mi menggunakan gigi atau sumpit?",
        "correct": "Karena helaian mi yang panjang dan tidak terputus melambangkan umur panjang (*chángshòu*); memotong helaian mi dipercaya membawa pertanda buruk memendekkan usia hidup.",
        "distractors": [
            "Karena adonan mi dibuat dari bahan karet sintetis yang tidak bisa putus oleh gigitan manusia.",
            "Karena pemilik restoran akan mendenda pelanggan yang menyisakan potongan mi di dalam mangkuk.",
            "Agar seluruh kuah kaldu panas tersedot habis ke dalam kerongkongan sekaligus tanpa tersisa.",
            "Karena tradisi tersebut diwajibkan oleh dewa dapur untuk menghormati tungku perapian memasak."
        ],
        "formula": {
            "title": "SIMBOLISME KULINER ULANG TAHUN (长寿面的文化内涵)",
            "latex": "\\mathbf{\\text{连绵不断的面条 (Mi Tak Putus)}} \\equiv \\mathbf{\\text{长寿无疆 (Umur Panjang Berkah)}} \\implies \\text{TABU MEMOTONG}",
            "legend": "• Menjaga keutuhan simbolik harapan hidup sehat dalam ritual perayaan usia"
        },
        "hints": {
            "concept": "Helaian mi panjang melambangkan umur panjang. Memotong mi dianggap memotong usia (pertanda buruk).",
            "execution": "Pilih opsi yang menjelaskan helaian mi melambangkan umur panjang dan memotongnya dipercaya pertanda buruk memendekkan usia."
        }
    },
    {
        "id": "man-sim-25",
        "materi": "BUDAYA & KESENIAN: TATA RIAS TOPENG OPERA BEIJING",
        "topic": "Makna Simbolik Warna Wajah Karakter Opera Beijing (Jīngjù Liǎnpǔ)",
        "stem": "Dalam seni teater klasik Opera Beijing (*Jīngjù*), warna riasan wajah (*Liǎnpǔ - 脸谱*) mencerminkan watak moral dari tokoh yang diperankan. Tokoh berwajah warna MERAH (*hóngliǎn* - seperti pahlawan Guan Yu) melambangkan watak...",
        "correct": "Kesetiaan moral yang teguh, keberanian patriotik, dan kejujuran berjiwa ksatria (*zhōngchéng yǒnggǎn*).",
        "distractors": [
            "Kelicikan yang penuh tipu muslihat, pengkhianatan keji, dan kejahatan konspirasi (yang diwakili oleh warna putih).",
            "Kekejaman haus darah, watak buas perampok rimba, dan pemberontak liar.",
            "Kekuatan magis makhluk siluman halus, dewa langit, dan hantu penasaran (yang diwakili oleh warna emas/perak).",
            "Kebodohan orang dungu yang selalu menjadi bahan tertawaan lelucon di atas panggung komedi."
        ],
        "formula": {
            "title": "KODE ETIKA TOPENG OPERA BEIJING (京剧脸谱色彩表意体系)",
            "latex": "\\begin{aligned} \\mathbf{\\text{红色 (Merah):}} & \\implies \\mathbf{\\text{忠勇义烈 (Setia, Berani, Jujur - Guan Yu)}} \\\\ \\text{白色 (Putih):} & \\implies \\text{奸诈多疑 (Licik, Jahat, Khianat - Cao Cao)} \\\\ \\text{黑色 (Hitam):} & \\implies \\text{刚正直率 (Tegas, Adil, Tanpa Kompromi - Hakim Bao)} \\end{aligned}",
            "legend": "• Visualisasi semiotika karakter moral yang dapat langsung dibaca oleh penonton teater"
        },
        "hints": {
            "concept": "Wajah merah (红色) pada Opera Beijing (seperti Guan Yu) melambangkan kesetiaan, keberanian, dan kejujuran (忠勇). Wajah putih melambangkan kelicikan (Cao Cao).",
            "execution": "Pilih opsi: Kesetiaan moral yang teguh, keberanian patriotik, dan kejujuran."
        }
    },

    # -------------------------------------------------------------
    # 5 MULTI-SELECT ITEMS (man-sim-26 .. man-sim-30)
    # -------------------------------------------------------------
    {
        "id": "man-sim-26",
        "materi": "MOJIGOI: RADIKAL POHON / KAYU (MÙZÌPÁNG)",
        "topic": "Karakter Hanzi yang Memuat Radikal Kayu/Pohon (木)",
        "stem": "Radikal 'Kayu / Pohon' (*Mùzìpáng* - 木) dalam aksara Hanzi lazimnya menyusun karakter yang berkaitan dengan flora berkayu, perabot kayu, atau material hutan. Manakah di antara karakter berikut yang memuat radikal '木'? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "树 (shù - pohon rindang di hutan)."},
            {"key": "B", "text": "桥 (qiáo - jembatan penyeberangan sungai yang zaman kuno terbuat dari kayu)."},
            {"key": "C", "text": "椅 (yǐ - kursi tempat duduk yang terbuat dari kayu mebel)."},
            {"key": "D", "text": "钱 (qián - uang logam yang beradikalkan logam emas 金/钅)."},
            {"key": "E", "text": "语 (yǔ - bahasa tuturan yang beradikalkan kata/ucapan 言/讠)."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "RADIKAL KAYU MUZIBANG (部首「木」词族)",
            "latex": "\\mathbf{[木 (Kayu/Pohon)]} \\implies \\begin{cases} \\mathbf{\\text{树 (Pohon)}} \\\\ \\mathbf{\\text{桥 (Jembatan)}} \\\\ \\mathbf{\\text{椅 (Kursi)}} \\end{cases}",
            "legend": "• 钱 beradikalkan 钅 (logam); 语 beradikalkan 讠 (bahasa/bicara)"
        },
        "hints": {
            "concept": "Radikal 木 ada pada 树 (shù), 桥 (qiáo), dan 椅 (yǐ). Karakter 钱 beradikal logam (钅), 语 beradikal bahasa (讠).",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },
    {
        "id": "man-sim-27",
        "materi": "TATA BAHASA YUFA: KATA BANTU BILANGAN SPESIFIK",
        "topic": "Pasangan Kata Bantu Bilangan Khusus yang Sahih",
        "stem": "Manakah pasangan antara kata bantu bilangan (*liàngcí*) dan kata benda (*míngcí*) berikut yang BENAR menurut kaidah tata bahasa Mandarin baku? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "一张照片 (yì zhāng zhàopiàn - selembar foto berpermukaan rata)."},
            {"key": "B", "text": "一本书 (yì běn shū - sebuah buku jilidan tebal)."},
            {"key": "C", "text": "一条鱼 (yì tiáo yú - seekor ikan yang bertubuh panjang meliuk di air)."},
            {"key": "D", "text": "一张飞机 (yì zhāng fēijī - pesawat terbang seharusnya menggunakan liangci jià 架)."},
            {"key": "E", "text": "一件裤子 (yí jiàn kùzi - celana panjang bawahan seharusnya menggunakan liangci tiáo 条)."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "VALIDASI KOLOKASI LIANGCI (名词量词标准匹配表)",
            "latex": "\\begin{aligned} \\mathbf{\\text{张 (zhāng):}} & \\implies \\mathbf{\\text{Foto / Kertas / Meja (Benda Datar)}} \\\\ \\mathbf{\\text{本 (běn):}} & \\implies \\mathbf{\\text{Buku / Kamus / Majalah (Jilidan)}} \\\\ \\mathbf{\\text{条 (tiáo):}} & \\implies \\mathbf{\\text{Ikan / Celana / Sungai (Panjang Menjalar)}} \\end{aligned}",
            "legend": "• Pesawat memakai 架 (jià); Celana memakai 条 (tiáo), bukan 件 (jiàn)"
        },
        "hints": {
            "concept": "A (foto rata pakai 张), B (buku pakai 本), dan C (ikan panjang pakai 条) adalah pasangan liangci yang tepat. Pesawat memakai 架, celana memakai 条.",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },
    {
        "id": "man-sim-28",
        "materi": "BUDAYA & TRADISI KULINER FESTIVAL",
        "topic": "Pasangan Autentik Festival Tradisional dan Panganan Khasnya",
        "stem": "Festival tradisional Tionghoa memiliki hidangan khas yang wajib disantap saat perayaan berlangsung. Manakah pasangan antara festival dan kuliner khas berikut yang BENAR? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "端午节 (Duānwǔjié / Festival Perahu Naga) \\to 吃粽子 (Chī zòngzi / Makan bakcang ketan)."},
            {"key": "B", "text": "中秋节 (Zhōngqiūjié / Festival Musim Gugur) \\to 吃月饼 (Chī yuèbǐng / Makan kue bulan)."},
            {"key": "C", "text": "元宵节 (Yuánxiāojié / Festival Lampion) \\to 吃元宵/汤圆 (Chī yuánxiāo / Makan ronde ketan manis)."},
            {"key": "D", "text": "端午节 (Duānwǔjié) \\to 吃月饼 (Kue bulan disantap saat festival musim gugur, bukan saat festival perahu naga)."},
            {"key": "E", "text": "中秋节 (Zhōngqiūjié) \\to 喝雄黄酒 (Arak Xionghuang diminum saat Duanwujie untuk mengusir serangga berbisa)."
            }
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "KORELASI FESTIVAL DAN KULINER TRADISIONAL (传统节日与食俗对偶)",
            "latex": "\\begin{aligned} \\mathbf{\\text{端午节}} & \\longleftrightarrow \\mathbf{\\text{粽子 (Bakcang Ketan Daun Bambu)}} \\\\ \\mathbf{\\text{中秋节}} & \\longleftrightarrow \\mathbf{\\text{月饼 (Kue Bulan Purnama)}} \\\\ \\mathbf{\\text{元宵节}} & \\longleftrightarrow \\mathbf{\\text{元宵 / 汤圆 (Bola Ketan Manis Reuni)}} \\end{aligned}",
            "legend": "• Menjaga memori kolektif siklus perputaran kalender agraris Tionghoa"
        },
        "hints": {
            "concept": "Duanwu = Zongzi (A), Zhongqiu = Yuebing (B), Yuanxiao = Tangyuan (C). Opsi D dan E terbalik.",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },
    {
        "id": "man-sim-29",
        "materi": "BUDAYA & ETIKA PERGAULAN TIONGHOA",
        "topic": "Etika dan Pantangan Hadiah Tradisional",
        "stem": "Dalam etika pertukaran hadiah dan interaksi sosial masyarakat Tionghoa, manakah perlakuan atau pantangan berikut yang BENAR secara budaya? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Menghindari memberi hadiah buah pir potong (*fēnlí - 分梨*) kepada pasangan suami istri karena berbunyi homofon dengan 'perpisahan / perceraian' (*fēnlí - 分离*)."},
            {"key": "B", "text": "Menghindari memberikan hadiah payung (*sǎn - 伞*) kepada sahabat dekat karena berima mirip dengan 'tercerai-berai' (*sàn - 散*)."},
            {"key": "C", "text": "Menggunakan amplop merah (*Hóngbāo*) saat memberikan uang berkah pada perayaan Tahun Baru Imlek atau pesta pernikahan."},
            {"key": "D", "text": "Wajib memberikan hadiah gunting tajam kepada pengantin baru sebagai simbol memotong kesialan masa lalu."},
            {"key": "E", "text": "Wajib memasukkan uang dalam nominal berangka empat (440 Yuan) ke dalam amplop hadiah ulang tahun kakek."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "HOMOFON TABU HADIAH TIONGHOA (民俗谐音禁忌体系)",
            "latex": "\\begin{aligned} \\mathbf{\\text{分梨 (fēnlí)}} & \\equiv \\mathbf{\\text{分离 (fēnlí / Cerai Pisah)}} \\\\ \\mathbf{\\text{送伞 (sòng sǎn)}} & \\equiv \\mathbf{\\text{离散 (lísàn / Bubar Terpencar)}} \\\\ \\mathbf{\\text{红包 (Hóngbāo)}} & \\equiv \\mathbf{\\text{吉祥如意 (Keberuntungan Berkah)}} \\end{aligned}",
            "legend": "• Gunting tajam melambangkan putus hubungan; Angka 4 berkonotasi kematian"
        },
        "hints": {
            "concept": "A (buah pir = pisah), B (payung = bubar), C (angpao merah = rezeki) adalah etika/tabu hadiah yang sahih. Benda tajam dan angka 4 adalah tabu.",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },
    {
        "id": "man-sim-30",
        "materi": "BUDAYA & WARISAN DUNIA TIONGKOK",
        "topic": "Karakteristik Warisan Kebudayaan dan Kesenian Tiongkok",
        "stem": "Manakah di antara pernyataan berikut yang TEPAT mengenai situs warisan sejarah dan kesenian tradisional Tiongkok? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Tembok Raksasa Tiongkok (*Chángchéng - 长城*) dibangun secara bertahap sejak zaman kuno untuk menahan serbuan pasukan nomaden dari utara."},
            {"key": "B", "text": "Kota Terlarang (*Gùgōng - 故宫*) di Beijing merupakan kompleks istana kekaisaran megah dari Dinasti Ming dan Dinasti Qing."},
            {"key": "C", "text": "Seni bela diri Tai Chi (*Tàijíquán - 太极拳*) mengintegrasikan gerakan lambat yang lentur dengan pengaturan napas dan filosofi keseimbangan Yin-Yang."},
            {"key": "D", "text": "Tembok Raksasa Tiongkok dibangun sepenuhnya menggunakan bahan baku plastik daur ulang pada pertengahan abad ke-20."},
            {"key": "E", "text": "Kota Terlarang di Beijing dulunya adalah pabrik senjata modern yang dibangun oleh bangsa Romawi kuno."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "WARISAN SEJARAH DAN TRADISI TIONGKOK (中国历史文化遗产)",
            "latex": "\\begin{cases} \\mathbf{\\text{长城 (Chángchéng):}} & \\text{Benteng Pertahanan Kuno Terpanjang Dunia} \\\\ \\mathbf{\\text{故宫 (Gùgōng):}} & \\text{Pusat Istana Kekaisaran Dinasti Ming \\& Qing} \\\\ \\mathbf{\\text{太极拳 (Tàijíquán):}} & \\text{Seni Bela Diri Olah Napas Filosofi Yin-Yang} \\end{cases}",
            "legend": "• Monumen peradaban yang diakui sebagai Warisan Budaya Dunia UNESCO"
        },
        "hints": {
            "concept": "A (Tembok Raksasa pertahanan utara), B (Gugong istana dinasti Ming-Qing), dan C (Taijiquan bela diri lambat Yin-Yang) adalah fakta sejarah dan budaya yang benar.",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH ITEMS (man-sim-31 .. man-sim-35)
    # -------------------------------------------------------------
    {
        "id": "man-sim-31",
        "materi": "TATA BAHASA YUFA: EVALUASI KAIDAH SINTAKSIS",
        "topic": "Validitas Struktur Kalimat dan Penempatan Keterangan",
        "stem": "Berikut disajikan pernyataan mengenai aturan tata bahasa Mandarin (*Yǔfǎ*). Tentukan apakah masing-masing pernyataan BENAR atau SALAH!",
        "statements": [
            {
                "text": "Kata keterangan waktu dalam kalimat bahasa Mandarin boleh diletakkan di bagian paling akhir kalimat setelah objek, persis seperti tata bahasa Inggris.",
                "correct": "Salah"
            },
            {
                "text": "Dalam kalimat berpredikat kata sifat murni (misalnya '我很高兴'), tidak boleh disisipkan kata kerja kopula '是' (shì).",
                "correct": "Benar"
            },
            {
                "text": "Preposisi '在' (zài) bersama tempat wadahnya harus diletakkan sebelum kata kerja utama ketika menerangkan lokasi terjadinya suatu aktivitas.",
                "correct": "Benar"
            },
            {
                "text": "Struktur perbandingan 'A 比 B' boleh secara bebas ditambahkan kata keterangan derajat '很' (hěn) di depan kata sifatnya (misal: '他比我很高').",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI KAIDAH YUFA POKOK (语法核心规则判定)",
            "latex": "\\begin{aligned} \\text{Keterangan Waktu di Akhir: } & \\text{Salah (Wajib sebelum kata kerja, tidak boleh di akhir)} \\\\ \\text{Sifat Tanpa 是: } & \\text{Benar (Kata sifat bertindak langsung sebagai predikat)} \\\\ \\text{在 + Tempat + Verb: } & \\text{Benar (Keterangan tempat mendahului aksi)} \\\\ \\text{比 + 很: } & \\text{Salah (Tabu mutlak menambahkan 很 pada predikat 比)} \\end{aligned}",
            "legend": "• Kaidah sintaksis mendasar yang membedakan struktur Mandarin dari bahasa rumpun lain"
        },
        "hints": {
            "concept": "1=Salah (waktu dilarang di akhir kalimat). 2=Benar (kalimat sifat tidak memakai 是). 3=Benar (在 + tempat ditaruh sebelum kata kerja). 4=Salah (struktur 比 dilarang memakai 很).",
            "execution": "Tentukan: 1=Salah, 2=Benar, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "man-sim-32",
        "materi": "TATA BAHASA YUFA: EVALUASI STRUKTUR KHUSUS",
        "topic": "Kebenaran Struktur Kalimat 把, 被, dan 是...的",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan tata bahasa struktur khusus bahasa Mandarin berikut!",
        "statements": [
            {
                "text": "Kalimat yang menggunakan partikel '把' (Bǎ) mewajibkan objek penderitanya berupa entitas yang definit (spesifik/jelas) bagi pembicara dan lawan bicara.",
                "correct": "Benar"
            },
            {
                "text": "Kata kerja utama di dalam kalimat '把' boleh berdiri telanjang sebagai kata kerja tunggal tanpa perlu diikuti komplemen, akhiran, atau objek lain.",
                "correct": "Salah"
            },
            {
                "text": "Kalimat pasif dengan partikel '被' (Bèi) dapat digunakan tanpa menyebutkan subjek pelaku secara eksplisit (contoh: '钱包被偷了').",
                "correct": "Benar"
            },
            {
                "text": "Struktur penekanan '是...的' (Shì...de) hanya boleh digunakan untuk menekankan peristiwa yang baru akan direncanakan di masa depan.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI STRUKTUR BA, BEI, DAN SHI...DE (特殊句式正误判定)",
            "latex": "\\begin{aligned} \\text{Objek 把 Definit: } & \\text{Benar (Wajib spesifik/pasti)} \\\\ \\text{Verba 把 Telanjang: } & \\text{Salah (Wajib ada komplemen/unsur penjelas hasil)} \\\\ \\text{Pelaku 被 Dilesapkan: } & \\text{Benar (Pelaku boleh implisit/anonim)} \\\\ \\text{是...的 Masa Depan: } & \\text{Salah (Hanya untuk peristiwa yang SUDAH PASTI terjadi di masa lalu)} \\end{aligned}",
            "legend": "• Menunjukkan ketepatan analisis komponen gramatikal tingkat menengah HSK"
        },
        "hints": {
            "concept": "1=Benar (objek 把 harus definit). 2=Salah (verba 把 tidak boleh telanjang). 3=Benar (pelaku kalimat 被 boleh tidak disebut). 4=Salah (是...的 hanya untuk peristiwa lampau yang sudah terjadi).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "man-sim-33",
        "materi": "HANZI & PINYIN: EVALUASI FONETIKA DAN NADA",
        "topic": "Kebenaran Kaidah Sandhi Nada Fonetik Mandarin",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan mengenai fonetika Pinyin dan nada berikut!",
        "statements": [
            {
                "text": "Dua suku kata yang sama-sama berharakat nada ketiga (3 + 3) ketika diucapkan berurutan, suku kata pertama wajib berubah pelafalannya menjadi nada kedua (2 + 3).",
                "correct": "Benar"
            },
            {
                "text": "Karakter negasi '不' (bù) akan selalu mempertahankan nada keempatnya dalam segala situasi tanpa pernah mengalami perubahan nada.",
                "correct": "Salah"
            },
            {
                "text": "Karakter angka '一' (yī) ketika berdiri sendiri atau digunakan saat menghitung urutan nomor tetap dilafalkan dengan nada pertama.",
                "correct": "Benar"
            },
            {
                "text": "Bahasa Mandarin baku memiliki enam jenis nada kontur utama ditambah delapan jenis nada sengau tambahan.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI FONOLOGI DAN SANDHI NADA (语音与变调规则判定)",
            "latex": "\\begin{aligned} \\text{Sandhi Nada 3: } & \\text{Benar (3+3 } \\to \\text{ 2+3)} \\\\ \\text{Karakter 不 Kaku: } & \\text{Salah (Berubah jadi nada 2 jika di depan nada 4)} \\\\ \\text{Angka 一 Urutan: } & \\text{Benar (Tetap nada 1 saat berhitung mandiri)} \\\\ \\text{Enam Nada Utama: } & \\text{Salah (Hanya ada 4 nada utama + 1 nada netral qingsheng)} \\end{aligned}",
            "legend": "• Standar fonologi baku Pinyin Republik Rakyat Tiongkok"
        },
        "hints": {
            "concept": "1=Benar (3+3 jadi 2+3). 2=Salah (不 berubah jadi nada 2 di depan nada 4). 3=Benar (一 tetap nada 1 saat hitung angka). 4=Salah (Mandarin hanya punya 4 nada utama + nada netral, bukan enam).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "man-sim-34",
        "materi": "JIĀOJÌ: EVALUASI UNGKAPAN PRAGMATIK KESEHARIAN",
        "topic": "Kesesuaian Konteks Sosial Ungkapan Komunikasi",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan penggunaan ungkapan situasi harian bahasa Mandarin berikut!",
        "statements": [
            {
                "text": "Jawaban balasan yang paling tepat dan sopan untuk merespons ucapan terima kasih '谢谢' adalah '不客气' (Bú kèqi).",
                "correct": "Benar"
            },
            {
                "text": "Ungkapan '对不起' (Duìbuqǐ) lazimnya dibalas oleh mitra bicara dengan ucapan '不客气' (Bú kèqi).",
                "correct": "Salah"
            },
            {
                "text": "Saat tamu berpamitan pulang, tuan rumah yang mengantar ke pintu mengucapkan '慢走' (Màn zǒu) sebagai doa agar berhati-hati di jalan.",
                "correct": "Benar"
            },
            {
                "text": "Kata sapaan '您好' (Nín hǎo) adalah sapaan informal yang hanya boleh digunakan oleh orang tua kepada anak-anak kecil.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI PRAGMATIK KOMUNIKASI (日常交际用语判定)",
            "latex": "\\begin{aligned} \\text{Balasan 谢谢: } & \\text{Benar (不客气)} \\\\ \\text{Balasan 对不起: } & \\text{Salah (Wajib 没关系, bukan 不客气)} \\\\ \\text{Tamu Pulang 慢走: } & \\text{Benar (Hati-hati di jalan)} \\\\ \\text{您好 ke Anak: } & \\text{Salah (您 adalah pronomina hormat vertikal kepada atasan/guru/orang tua)} \\end{aligned}",
            "legend": "• Menjaga ketepatan fungsi sosio-pragmatik bahasa dalam konteks riil"
        },
        "hints": {
            "concept": "1=Benar (terima kasih dibalas 不客气). 2=Salah (对不起 dibalas 没关系, bukan 不客气). 3=Benar (melepas tamu mengucapkan 慢走). 4=Salah (您好 untuk pihak yang dihormati seperti guru/atasan, bukan anak kecil).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "man-sim-35",
        "materi": "BUDAYA & ETIKA SOSIAL: EVALUASI NORMA BUDAYA TIONGHOA",
        "topic": "Validitas Norma dan Pantangan Sosial Masyarakat Tionghoa",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan mengenai norma adat istiadat dan etika pergaulan masyarakat Tionghoa berikut!",
        "statements": [
            {
                "text": "Memberikan hadiah berupa jam dinding (*sòng zhōng*) sangat dihindari karena berbunyi homofon mirip dengan mengantar upacara kematian (*sòng zhōng*).",
                "correct": "Benar"
            },
            {
                "text": "Dalam perjamuan makan meja bundar resmi di Tiongkok, kursi kehormatan utama (*Zhǔwèi*) berada di posisi yang tepat menghadap ke arah pintu masuk.",
                "correct": "Benar"
            },
            {
                "text": "Warna putih secara tradisional dalam budaya Tionghoa melambangkan keberuntungan besar dan berkah rezeki pernikahan.",
                "correct": "Salah"
            },
            {
                "text": "Angka delapan (8) sangat digemari dalam masyarakat Tionghoa karena pelafalannya (*bā*) berima mirip dengan kata makmur dan berjaya (*fā*).",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "EVALUASI KEBUDAYAAN DAN PRAGMATIK TIONGHOA (中华民俗文化正误判定)",
            "latex": "\\begin{aligned} \\text{Beri Jam Tabu: } & \\text{Benar (Homofon kematian)} \\\\ \\text{Kursi 主位 Hadap Pintu: } & \\text{Benar (Etika meja bundar perjamuan)} \\\\ \\text{Warna Putih Berkah: } & \\text{Salah (Putih untuk duka cita; merah untuk berkah)} \\\\ \\text{Angka 8 Makmur: } & \\text{Benar (bā mirip fā)} \\end{aligned}",
            "legend": "• Refleksi holistik penguasaan muatan lintas budaya Kurikulum Merdeka 2026"
        },
        "hints": {
            "concept": "1=Benar (jam dinding homofon kematian). 2=Benar (kursi utama menghadap pintu). 3=Salah (warna berkah adalah merah, putih untuk duka cita). 4=Benar (angka 8 mirip kata makmur fā).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Salah, 4=Benar."
        }
    }
]
