# -*- coding: utf-8 -*-
"""
BAHASA JEPANG - PAKET SOAL SIMULASI HOTS LENGKAP (35 BUTIR)
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / JLPT N5–N4
Distribusi:
- 25 Butir: Pilihan Ganda Tunggal (MCQ - jpn-sim-01 s.d. jpn-sim-25)
- 5 Butir: Pilihan Ganda Kompleks / Multi-Select (jpn-sim-26 s.d. jpn-sim-30)
- 5 Butir: Matriks Asosiasi Benar-Salah (jpn-sim-31 s.d. jpn-sim-35)
"""

BAHASA_JEPANG_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 MCQ ITEMS (jpn-sim-01 .. jpn-sim-25)
    # -------------------------------------------------------------
    {
        "id": "jpn-sim-01",
        "materi": "TATA BAHASA BUNPOU: PERBANDINGAN TIGA ENTITAS (SUPERLATIF)",
        "topic": "Struktur Pertanyaan Pilihan Superlatif (の中で どれ/何 が 一番〜ですか)",
        "stem": "Dalam sesi wawancara mengenai kegemaran berolahraga di Jepang, penanya ingin menanyakan olahraga mana yang paling disukai dari empat pilihan yang diajukan:\n'サッカーと 野球と テニスと 水泳の なかで、( ... ) が いちばん 好きですか。'\nKata tanya interrogativa yang TEPAT untuk mengisi rumpang tersebut adalah...",
        "correct": "どれ (Dore - kata tanya pilihan di antara tiga atau lebih objek konkret yang telah disebutkan secara eksplisit).",
        "distractors": [
            "なに (Nani - kata tanya umum terbuka yang tidak mengacu pada himpunan opsi tertutup tertentu).",
            "どちら (Dochira - kata tanya komparatif yang khusus hanya digunakan untuk memilih di antara DUA entitas).",
            "だれ (Dare - kata tanya yang khusus menanyakan identitas subjek manusia).",
            "どこ (Doko - kata tanya lokatif yang khusus menanyakan posisi tempat geografis)."
        ],
        "formula": {
            "title": "STRUKTUR SUPERLATIF PILIHAN TERTUTUP (最上級の疑問文)",
            "latex": "\\mathbf{[A \\text{ と } B \\text{ と } C \\text{ のなかで}]} + \\mathbf{\\text{どれ が}} + \\text{いちばん } + \\text{Sifat} \\implies \\text{Paling } [\\text{Sifat}] \\text{ di antara pilihan}",
            "legend": "• どちら digunakan jika 2 pilihan; どれ digunakan jika $\\ge 3$ pilihan konkret"
        },
        "hints": {
            "concept": "Ada 4 pilihan olahraga (tiga atau lebih). Kata tanya untuk memilih di antara $\\ge 3$ pilihan benda adalah 'どれ' (dore). Jika hanya 2 pilihan barulah 'どちら' (dochira).",
            "execution": "Pilih: 'どれ (Dore)'."
        }
    },
    {
        "id": "jpn-sim-02",
        "materi": "TATA BAHASA BUNPOU: BENTUK MEMBERI DAN MENERIMA (JUSHU HYOUGEN)",
        "topic": "Analisis Arah Transaksi Kebaikan (あげる, もらう, くれる)",
        "stem": "Perhatikan situasi berikut:\nSeorang guru warga negara Jepang dengan ramah membantu mengoreksi karangan bahasa Jepang milik saya.\nKalimat yang TEPAT dan santun untuk mengungkapkan bahwa 'guru berkenan mengoreksikan karangan untuk saya' adalah...",
        "correct": "先生が 私の 作文を 直して くださいました。 (Guru berbuat kebaikan mengoreksi untuk saya dengan verba hormat kudasaimashita).",
        "distractors": [
            "私が 先生の 作文を 直して あげました。 (Saya yang mengoreksikan karangan milik guru dengan nada terkesan merendahkan martabat guru).",
            "先生が 私の 作文を 直して やりました。 (Menggunakan yarimashita yang hanya ditujukan untuk hewan, tanaman, atau anak kecil).",
            "私は 先生に 作文を 直して あげたいです。 (Menyatakan keinginan diri sendiri untuk mengajari atau mengoreksi tulisan guru).",
            "先生は 私に 作文を 直して もらいました。 (Terbalik subjek, menyiratkan bahwa guru yang berterima kasih menerima jasa dari saya)."
        ],
        "formula": {
            "title": "VEKTOR TRANSAKSI KEBAIKAN (授受表現の方向性)",
            "latex": "\\begin{aligned} \\text{Orang Lain } \\to \\text{ Saya: } & \\mathbf{\\text{Pihak Lain が 私に }} \\mathbf{V\\text{-て くれる / くださる}} \\\\ \\text{Saya } \\to \\text{ Orang Lain: } & \\text{私が Pihak Lain に } V\\text{-て あげる / さしあげる} \\end{aligned}",
            "legend": "• Menggunakan くださる (bentuk Sonkeigo dari くれる) saat subjek pemberi jasa adalah guru/atasan"
        },
        "hints": {
            "concept": "Guru melakukan kebaikan untuk saya (arah dari orang lain ke saya). Bentuk hormat dari te-kureru adalah te-kudasaru: 直してくださいました.",
            "execution": "Pilih: '先生が 私の 作文を 直して くださいました。'."
        }
    },
    {
        "id": "jpn-sim-03",
        "materi": "TATA BAHASA BUNPOU: PERUBAHAN KEADAAN (HENKA)",
        "topic": "Konstruksi Menjadi Kata Sifat-i dan Kata Sifat-na (~Ku naru vs ~Ni naru)",
        "stem": "Perhatikan proses pergantian musim berikut:\n1) 秋に なって、木の 葉が 赤 [ A ] なりました。\n2) 工事の あと、この 町は とても にぎやか [ B ] なりました。\nImbuhan ( A ) untuk kata sifat-i 'あかい' dan ( B ) untuk kata sifat-na 'にぎやか' yang TEPAT berturut-turut adalah...",
        "correct": "A: く (Akaku - sifat-i coret い berganti く), B: に (Nigiyaka ni - sifat-na dilekatkan partikel に).",
        "distractors": [
            "A: に, B: く (terbalik antara kaidah pembentukan kata sifat-i dan kata sifat-na).",
            "A: い, B: な (mempertahankan bentuk dasar tanpa konjugasi perubahan keadaan).",
            "A: く, B: な (kata sifat-na keliru dilekatkan partikel na di depan verba naru).",
            "A: で, B: に (kata sifat-i keliru dilekatkan kopula partikel de)."
        ],
        "formula": {
            "title": "KONSTRUKSI PERUBAHAN KEADAAN (状態変化「〜になる」)",
            "latex": "\\begin{cases} \\mathbf{\\text{Kata Sifat-i:}} & \\text{赤}[\\cancel{\\text{い}}] + \\mathbf{\\text{く}} + \\text{なる} \\implies \\mathbf{\\text{赤くなる}} \\\\ \\mathbf{\\text{Kata Sifat-na:}} & \\text{にぎやか} + \\mathbf{\\text{に}} + \\text{なる} \\implies \\mathbf{\\text{にぎやかになる}} \\end{cases}",
            "legend": "• Menunjukkan dinamika transisi kondisi objek dari fase awal menuju fase baru"
        },
        "hints": {
            "concept": "Sifat-i (akai) menjadi: あかく なります (ku naru). Sifat-na (nigiyaka) menjadi: にぎやかに なります (ni naru).",
            "execution": "Pilih opsi: 'A: く, B: に'."
        }
    },
    {
        "id": "jpn-sim-04",
        "materi": "TATA BAHASA BUNPOU: KALIMAT KUTIPAN TIDAK LANGSUNG",
        "topic": "Mengutip Pernyataan Pihak Lain (~To itte imashita)",
        "stem": "Yamada mengabarkan perkataan Sato yang tidak bisa hadir dalam rapat:\n'さとうさんは「あした 出張で 大阪へ 行きます」と 言いました。'\nBagaimanakah bentuk kalimat kutipan tidak langsung (*kansetsu inyou*) yang BENAR secara gramatikal?",
        "correct": "さとうさんは あした 出張で 大阪へ 行く と 言っていました。 (Bentuk sopan ikimasu diubah ke bentuk biasa/kamus iku sebelum partikel kutipan と).",
        "distractors": [
            "さとうさんは あした 出張で 大阪へ 行きます と 言っていました。 (Mempertahankan bentuk formal masu di dalam klausa kutipan subordinat).",
            "さとうさんは あした 出張で 大阪へ 行った と 言っていました。 (Mengubah kala waktu menjadi lampau padahal peristiwa baru akan berlangsung besok).",
            "さとうさんは あした 出張で 大阪へ 行かない と 言っていました。 (Mengubah polaritas pernyataan menjadi negatif tanpa dasar teks).",
            "さとうさんは あした 出張で 大阪へ 行け と 言っていました。 (Mengubah pernyataan deklaratif menjadi kalimat perintah imperatif)."
        ],
        "formula": {
            "title": "KAIDAH KUTIPAN KLAUSA SUBORDINAT (間接引用の普通形化)",
            "latex": "\\mathbf{\\text{Klausa Kalimat (Bentuk Biasa / Futsukei)}} + \\mathbf{\\text{と 言っていました}} \\implies \\text{Menyampaikan bahwa } \\dots",
            "legend": "• Ragam sopan (Teineigo) di dalam kutipan wajib disederhanakan menjadi Futsuukei"
        },
        "hints": {
            "concept": "Dalam kutipan tidak langsung, predikat sebelum partikel と (to) wajib menggunakan bentuk biasa (futsuukei): 行きます (ikimasu) -> 行く (iku).",
            "execution": "Pilih opsi yang menggunakan verba '行く と 言っていました'."
        }
    },
    {
        "id": "jpn-sim-05",
        "materi": "TATA BAHASA BUNPOU: POLA KALIMAT TERTUTUP",
        "topic": "Menyatakan Keberangkatan Melakukan Aktivitas (~Ni ikimasu)",
        "stem": "Lengkapilah kalimat tujuan aktivitas berikut:\n'週末、デパートへ 新しい 冬物の コートを ( ... ) 行きました。'",
        "correct": "買いに (Kai ni - akar kata verba masu-stem 'kai' diikuti partikel tujuan gerak 'ni' untuk menyatakan pergi demi membeli).",
        "distractors": [
            "買うに (Kau ni - kesalahan gramatikal fatal karena bentuk kamus tidak boleh langsung dilekatkan partikel ni).",
            "買ってに (Katte ni - kesalahan gramatikal menggabungkan bentuk te dengan partikel ni).",
            "買いたいに (Kaitai ni - bentuk keinginan yang tidak kompatibel dengan verba pergerakan ikimashita).",
            "買わないに (Kawanai ni - bentuk negatif yang merusak struktur kepergian berbelanja)."
        ],
        "formula": {
            "title": "POLA TUJUAN PERGERAKAN (移動の目的「〜に行く」)",
            "latex": "\\mathbf{V\\text{-ます形 (Coret ます)}} + \\mathbf{\\text{に}} + \\mathbf{\\text{行く / 来る / 帰る}} \\implies \\text{Pergi/Datang untuk melakukan } V",
            "legend": "• Menjelaskan intensi spesifik di balik aksi perpindahan fisik ke lokasi tertentu"
        },
        "hints": {
            "concept": "Pola pergi untuk melakukan sesuatu: V(masu-stem) + に行きます. Beli (kaimasu) -> 買いに (kai ni).",
            "execution": "Pilih: '買いに (Kai ni)'."
        }
    },
    {
        "id": "jpn-sim-06",
        "materi": "TATA BAHASA BUNPOU: WAKTU RELATIF",
        "topic": "Penggunaan Maeni (〜まえに) vs Ato de (〜あとで)",
        "stem": "Perhatikan aturan minum obat berikut:\n'しょくじを ( A ) まえに、手を 洗います。\n ごはんを ( B ) あとで、くすりを 飲みます。'\nBentuk verba 'たべる' yang BENAR untuk mengisi posisi ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: たべる (bentuk kamus wajib mendahului まえに), B: たべた (bentuk lampau ta-kei wajib mendahului あとで).",
        "distractors": [
            "A: たべた, B: たべる (terbalik mutlak antara kaidah sekuensial waktu sebelum dan sesudah).",
            "A: たべる, B: たべる (menggunakan bentuk kamus untuk kedua konstruksi waktu).",
            "A: たべた, B: たべた (menggunakan bentuk lampau untuk kedua konstruksi waktu).",
            "A: たべて, B: たべて (menggunakan bentuk te yang menyalahi modifikasi nomina gramatikal)."
        ],
        "formula": {
            "title": "SEKUENSI KRONOLOGIS VERBA (前後の時間的連関)",
            "latex": "\\begin{cases} \\mathbf{V\\text{-辞書形 (Kamus)}} + \\mathbf{\\text{まえに}} & \\implies \\text{Sebelum melakukan } V \\\\ \\mathbf{V\\text{-た形 (Lampau)}} + \\mathbf{\\text{あとで}} & \\implies \\text{Sesudah tuntas melakukan } V \\end{cases}",
            "legend": "• Perbedaan aspek tuntas/belum tuntas yang mengendalikan bentuk predikat klausula"
        },
        "hints": {
            "concept": "Sebelum: V(kamus) + まえに -> たべる まえに. Sesudah: V(lampau ta) + あとで -> たべた あとで.",
            "execution": "Pilih: 'A: たべる, B: たべた'."
        }
    },
    {
        "id": "jpn-sim-07",
        "materi": "TATA BAHASA BUNPOU: MENYATAKAN DUA KEGIATAN SIMULTAN",
        "topic": "Penggunaan Pola ~Nagara (〜ながら)",
        "stem": "Dokter melarang pasien melakukan kebiasaan buruk saat makan:\n'テレビを ( ... ) ごはんを 食べてはいけません。消化に 悪いです。'\nBentuk verba 'みます' yang TEPAT untuk menyatakan 'makan sambil menonton TV' adalah...",
        "correct": "見ながら (Minagara - akar verba masu-stem mi- dilekatkan partikel konjungsi simultan nagara).",
        "distractors": [
            "見るながら (Mirunagara - bentuk kamus yang dilarang melekat pada akhiran nagara).",
            "見てながら (Mitenagara - kesalahan menggabungkan bentuk te dengan nagara).",
            "見たながら (Mitanagara - kesalahan menggabungkan bentuk lampau dengan nagara).",
            "見ないながら (Minainagara - bentuk negatif yang menyalahi pembentukan baku nagara)."
        ],
        "formula": {
            "title": "AKSI PARALEL SIMULTAN (同時動作「〜ながら」)",
            "latex": "\\mathbf{V\\text{-ます形 (Coret ます)}} + \\mathbf{\\text{ながら}} + V_2 \\implies \\text{Melakukan } V_2 \\text{ sambil melakukan } V_1",
            "legend": "• Aksi utama diletakkan pada predikat akhir ($V_2$); aksi sampingan pada $V_1$"
        },
        "hints": {
            "concept": "Sambil melakukan perbuatan: V(masu-stem) + ながら. Mimasu -> 見ながら (minagara).",
            "execution": "Pilih: '見ながら (Minagara)'."
        }
    },
    {
        "id": "jpn-sim-08",
        "materi": "TATA BAHASA BUNPOU: DAFTAR TINDAKAN PERWAKILAN",
        "topic": "Penggunaan Pola ~Tari ~Tari Suru (〜たり〜たりする)",
        "stem": "Seseorang menceritakan rutinitas santainya saat hari libur di rumah:\n'日曜日は 部屋を ( A )、本を ( B ) して、のんびり 過ごします。'\nBentuk verba yang TEPAT untuk mengisi posisi ( A ) dan ( B ) secara berturut-turut adalah...",
        "correct": "A: そうじしたり, B: よんだり (akar ta-kei dilekatkan partikel ri untuk mendata contoh perbuatan non-kronologis).",
        "distractors": [
            "A: そうじして, B: よんで (bentuk te biasa yang membatasi tindakan sebagai urutan kaku).",
            "A: そうじする, B: よむ (bentuk kamus yang tidak memiliki morfem penanda variasi aktivitas).",
            "A: そうじした, B: よんだ (bentuk lampau terputus yang merusak konstruksi pembantu suru).",
            "A: そうじしろ, B: よめ (bentuk imperatif kasar yang menyimpang dari deskripsi hari libur)."
        ],
        "formula": {
            "title": "ENUMERASI TINDAKAN REPRESENTATIF (例示表現「〜たり〜たりする」)",
            "latex": "\\mathbf{V_1\\text{-たり}} + \\mathbf{V_2\\text{-たりする}} \\implies \\text{Melakukan kegiatan seperti } V_1 \\text{ dan } V_2",
            "legend": "• Menunjukkan contoh dari beberapa aktivitas tanpa urutan waktu yang mengikat"
        },
        "hints": {
            "concept": "Pola menyebutkan beberapa kegiatan contoh: V-tari V-tari shimasu. Souji shimasu -> そうじしたり; yomimasu -> よんだり.",
            "execution": "Pilih opsi: 'A: そうじしたり, B: よんだり'."
        }
    },
    {
        "id": "jpn-sim-09",
        "materi": "TATA BAHASA BUNPOU: PEMBERIAN SARAN / ANJURAN",
        "topic": "Pola Nasehat Positif vs Negatif (~Hou ga ii desu)",
        "stem": "Seorang dokter memberikan nasehat kesehatan kepada pasien yang terkena flu berat:\n'熱が 高いので、今日はお風呂に ( A ) ほうが いいです。\n そして、暖かい 部屋で 早く ( B ) ほうが いいですよ。'\nPasangan bentuk verba yang TEPAT untuk nasehat negatif ( A ) dan nasehat positif ( B ) adalah...",
        "correct": "A: 入らない (Hai-ranai - bentuk nai untuk saran pencegahan), B: 寝た (Neta - bentuk ta untuk anjuran perbuatan).",
        "distractors": [
            "A: 入った, B: 寝ない (terbalik total yang justru membahayakan kondisi kesehatan pasien).",
            "A: 入らない, B: 寝る (saran positif anjuran baku wajib menggunakan verba bentuk ta, bukan jisho-kei).",
            "A: 入らなくて, B: 寝て (bentuk te tidak kompatibel dengan konstruksi pembanding hou ga ii).",
            "A: 入るな, B: 寝ろ (perintah larangan kasar yang tidak etis diucapkan dokter kepada pasien)."
        ],
        "formula": {
            "title": "KONSTRUKSI SARAN NORMATIF (助言・忠告の文法)",
            "latex": "\\begin{cases} \\mathbf{\\text{Saran Positif (Sebaiknya lakukan):}} & \\mathbf{V\\text{-た形}} + \\mathbf{\\text{ほうが いい}} \\\\ \\mathbf{\\text{Saran Negatif (Sebaiknya jangan):}} & \\mathbf{V\\text{-ない形}} + \\mathbf{\\text{ほうが いい}} \\end{cases}",
            "legend": "• Bentuk lampau (ta) pada saran positif menyiratkan kepastian hasil yang telah teruji baik"
        },
        "hints": {
            "concept": "Saran negatif (sebaiknya jangan mandi): V-nai + ほうがいい -> はいらない. Saran positif (sebaiknya tidur cepat): V-ta + ほうがいい -> ねた.",
            "execution": "Pilih: 'A: 入らない, B: 寝た'."
        }
    },
    {
        "id": "jpn-sim-10",
        "materi": "TATA BAHASA BUNPOU: MENYATAKAN PROBABILITAS TINGKAT MENENGAH",
        "topic": "Penggunaan Kamoshiremasen (〜かもしれません: 50% Kemungkinan)",
        "stem": "Melihat langit yang mendung hitam pekat di sore hari, seseorang berujar:\n'空が 暗くなってきましたね。夕方から 雨が ( ... )。傘を 持って行きましょう。'\nPola modalitas dugaan probabilitas yang TEPAT mengisi kalimat tersebut adalah...",
        "correct": "ふるかもしれません (Furu kamoshiremasen - ada kemungkinan hujan akan turun, berbobot dugaan sekitar 50%).",
        "distractors": [
            "ふらなければなりません (Menyatakan kewajiban hukum bahwa hujan wajib turun).",
            "ふってはいけません (Menyatakan larangan bahwa hujan tidak boleh turun).",
            "ふることが できます (Menyatakan kemampuan kompetensi bahwa hujan bisa turun).",
            "ふりたいです (Menyatakan keinginan subjektif bahwa pembicara ingin turun hujan)."
        ],
        "formula": {
            "title": "MODALITAS KEMUNGKINAN DUA ARAH (不確定推量「〜かもしれない」)",
            "latex": "\\mathbf{V\\text{-普通形}} + \\mathbf{\\text{かもしれません}} \\implies \\text{Mungkin / Bisa jadi terjadi } V \\quad (P \\approx 50\\%)",
            "legend": "• Menunjukkan ketidakpastian pembicara terhadap peristiwa yang berada di luar kendali"
        },
        "hints": {
            "concept": "Melihat gejala cuaca dan memperkirakan 'mungkin turun hujan' memakai ~かもしれません (kamoshiremasen).",
            "execution": "Pilih: 'ふるかもしれません (Furu kamoshiremasen)'."
        }
    },
    {
        "id": "jpn-sim-11",
        "materi": "DOKKAI TEKSTUAL: PEMBERITAHUAN FASILITAS UMUM",
        "topic": "Menganalisis Informasi Operasional Kolam Renang Kota",
        "stem": "Bacalah pengumuman fasilitas olahraga berikut:\n--------------------------------------------------\n【市民温水プールの ご利用案内】\n・開館時間：午前9時〜午後9時（最終入場 午後8時半）\n・休館日：毎週月曜日（祝日の 場合は 翌火曜日）、年末年始\n・利用料金：大人 500円 / 高校生以下 200円\n※水泳帽（スイミングキャップ）を 必ず 着用してください。お持ちでない 方は 受付で 300円で レンタルできます。\n※小学3年生以下の お子様は、保護者の 同伴が 必要です。\n--------------------------------------------------\nSeorang siswa SMA ingin berenang pada hari Senin yang bertepatan dengan Hari Libur Nasional (*Shukujitsu*). Berapakah total biaya yang harus dibayar siswa tersebut jika ia tidak membawa topi renang?",
        "correct": "500 yen (tiket masuk pelajar SMA 200 yen + biaya sewa topi renang 300 yen, dan kolam renang buka karena libur nasional dialihkan ke hari Selasa).",
        "distractors": [
            "800 yen (dihitung menggunakan tarif tiket masuk orang dewasa 500 yen ditambah biaya topi renang).",
            "200 yen (hanya membayar tiket masuk karena topi renang dipinjamkan secara gratis untuk pelajar).",
            "Kolam renang tutup total sehingga siswa tersebut tidak dapat masuk sama sekali pada hari Senin.",
            "700 yen (karena dikenakan denda tambahan hari libur sebesar 200 yen)."
        ],
        "formula": {
            "title": "KALKULASI TARIF FASILITAS BERKONDISI (条件付き利用料金の算出)",
            "latex": "\\begin{aligned} \\text{Status Buka: } & \\text{Senin Libur Nasional} \\implies \\text{Buka (Libur pindah ke Selasa)} \\\\ \\text{Total Biaya: } & \\text{Tiket SMA (200円)} + \\text{Sewa Topi (300円)} = \\mathbf{500\\text{円}} \\end{aligned}",
            "legend": "• Memerlukan integrasi klausula kalender (祝日の場合) dan klausula tarif kelompok umur"
        },
        "hints": {
            "concept": "1) Senin libur nasional, maka hari libur gedung diundur ke Selasa (tetap BUKA). 2) Pelajar SMA (高校生以下) = 200 yen. 3) Sewa topi = 300 yen. Total: 200 + 300 = 500 yen.",
            "execution": "Pilih opsi: '500 yen'."
        }
    },
    {
        "id": "jpn-sim-12",
        "materi": "DOKKAI TEKSTUAL: SUREL RESERVASI HOTEL",
        "topic": "Memverifikasi Perubahan Jadwal Menginap Ryokan",
        "stem": "Bacalah surel balasan dari pihak penginapan tradisional (*Ryokan*) berikut:\n--------------------------------------------------\nスミス様\nこの度は「四季の宿」を ご予約いただき、誠に ありがとうございます。\nご予約内容の 変更を 承りました。\n・ご宿泊日：12月23日（2泊3日） \\to 12月24日（1泊2日）に変更\n・お部屋タイプ：和室（富士山側）\n・お食事：夕食・朝食付き（アレルギー対応：エビ・カニ除去）\nなお、日程短縮に 伴う キャンセル料は 発生いたしません。\n当日、午後3時より チェックインが 可能です。お気をつけて お越しくださいませ。\n--------------------------------------------------\nInformasi mana yang SESUAI dengan surel konfirmasi di atas?",
        "correct": "Tamu mengubah jadwal kunjungannya menjadi hanya 1 malam 2 hari mulai tanggal 24 Desember dan pihak ryokan membebaskan biaya pembatalan.",
        "distractors": [
            "Tamu menambah durasi masa inap menjadi 3 malam 4 hari dengan kamar berpemandangan laut.",
            "Pihak penginapan menolak permintaan perubahan menu makanan yang bebas udang dan kepiting.",
            "Tamu diwajibkan membayar denda penalti pembatalan sebesar 50% karena mempersingkat hari menginap.",
            "Waktu proses lapor masuk (check-in) baru dibuka pada malam hari mulai pukul 20.00."
        ],
        "formula": {
            "title": "ANALISIS TRANSAKSI RESERVASI (宿泊変更確認書の読解)",
            "latex": "\\text{Jadwal Baru: } \\mathbf{\\text{12月24日 (1泊2日)}} + \\mathbf{\\text{キャンセル料なし (Bebas Biaya Penalti)}}",
            "legend": "• Menunjukkan kemampuan memvalidasi data administratif pemesanan akomodasi"
        },
        "hints": {
            "concept": "Perhatikan teks: '12月24日（1泊2日）に変更' dan '日程短縮に伴うキャンセル料は発生いたしません'.",
            "execution": "Pilih opsi: 'Tamu mengubah jadwal kunjungannya menjadi hanya 1 malam 2 hari mulai tanggal 24 Desember dan bebas biaya pembatalan'."
        }
    },
    {
        "id": "jpn-sim-13",
        "materi": "DOKKAI TEKSTUAL: WACANA SOSIAL BUDAYA",
        "topic": "Fenomena Toko Serba Ada 24 Jam (Konbini) dalam Infrastruktur Kebencanaan",
        "stem": "Bacalah artikel mengenai peran toko kelontong modern di Jepang berikut:\n--------------------------------------------------\n日本の コンビニエンスストア（コンビニ）は、単に 食料品や 日用品を 売る 場所にとどまりません。公共料金の 支払いや 宅配便の 発送、銀行ATMなど 多彩な サービスを 提供しています。さらに 重要なのは、大地震などの 災害時における「防災拠点」としての 役割です。多くの コンビニが 自治体と 協定を 結んでおり、被災者に対して 水や 食料、トイレ、帰宅ルートの 地図情報などを 無償で 提供する 体制を 整えています。今や コンビニは、日本の 不可欠な 社会インフラと なっています。\n--------------------------------------------------\nBerdasarkan wacana di atas, mengapa *konbini* diakui sebagai infrastruktur sosial yang vital bagi masyarakat Jepang?",
        "correct": "Karena selain menyediakan berbagai layanan publik harian, konbini juga berfungsi sebagai posko darurat bencana yang menyediakan air, toilet, dan logistik bagi para korban.",
        "distractors": [
            "Karena konbini merupakan satu-satunya badan usaha swasta yang berhak mencetak uang kertas yen di Jepang.",
            "Karena setiap warga negara diwajibkan mendaftarkan dokumen kependudukan resmi di meja kasir konbini.",
            "Karena konbini melarang penjualan produk luar negeri demi memproteksi barang produksi industri lokal.",
            "Karena bangunan konbini dibangun menggunakan bunker baja bawah tanah tahan serangan rudal nuklir."
        ],
        "formula": {
            "title": "KONBINI SEBAGAI INFRASTRUKTUR MULTIFUNGSI (コンビニの社会機能)",
            "latex": "\\mathbf{\\text{Fasilitas Harian (ATM, Tagihan, Logistik)}} + \\mathbf{\\text{Posko Mitigasi Bencana (Air, Peta, Toilet)}} \\implies \\text{Infrastruktur Vital}",
            "legend": "• Transformasi fungsi retail komersial menjadi jejaring ketahanan publik perkotaan"
        },
        "hints": {
            "concept": "Teks menekankan peran konbini bukan sekadar toko retail, tapi melayani tagihan/ATM dan menjadi posko darurat bencana penyedia air/toilet/peta gratis.",
            "execution": "Pilih opsi yang mencakup layanan publik harian dan posko darurat penyedia logistik/air/toilet saat bencana."
        }
    },
    {
        "id": "jpn-sim-14",
        "materi": "DOKKAI TEKSTUAL: TRADISI UPACARA MINUM TEH",
        "topic": "Empat Prinsip Luhur Sadou (和・敬・清・寂 - Wa Kei Sei Jaku)",
        "stem": "Bacalah teks mengenai seni tradisi Jepang (*Sadou*) berikut:\n'茶道（さどう）の 精神は、千利休（せんの りきゅう）によって 大成された「和・敬・清・寂（わけいせいじゃく）」という 四つの 言葉に 集約されています。「和」は お互いの 心を 開き 仲良くすること、「敬」は 互いの 人格を 尊重し 敬い合うこと、「清」は 心と 身の回りを 清らかに 保つこと、そして「寂」は どんな ときにも 動じない 穏やかな 静けさを 意味します。'\nMakna dari prinsip '敬 (Kei)' dalam ajaran upacara minum teh menurut wacana di atas adalah...",
        "correct": "Sikap saling menghormati dan menghargai martabat kepribadian sesama manusia.",
        "distractors": [
            "Membuka pintu hati untuk menciptakan kerukunan dan persaudaraan tanpa permusuhan.",
            "Menjaga kesucian raga dan kebersihan ruang peralatan minum teh dari segala debu kotoran.",
            "Mencapai kedamaian batin hening yang tidak goyah oleh kebisingan duniawi.",
            "Mengharuskan tamu membeli mangkuk teh keramik mahal buatan seniman istana."
        ],
        "formula": {
            "title": "EMPAT PILAR SADOU (四規：和敬清寂)",
            "latex": "\\begin{aligned} \\text{和 (Wa): } & \\text{Kerukunan Hati} \\\\ \\mathbf{\\text{敬 (Kei):}} & \\mathbf{\\text{Saling Menghormati Martabat (互いの人格を尊重)}} \\\\ \\text{清 (Sei): } & \\text{Kemurnian / Kebersihan} \\\\ \\text{寂 (Jaku): } & \\text{Keheningan Batin Mendalam} \\end{aligned}",
            "legend": "• Prinsip estetika Zen yang membimbing interaksi tuan rumah dan tamu perjamuan"
        },
        "hints": {
            "concept": "Teks menyatakan: '「敬」は 互いの 人格を 尊重し 敬い合うこと' (saling menghormati martabat kepribadian).",
            "execution": "Pilih opsi: 'Sikap saling menghormati dan menghargai martabat kepribadian sesama manusia'."
        }
    },
    {
        "id": "jpn-sim-15",
        "materi": "MOJIGOI & BUNPOU: KATA KETERANGAN WAKTU RUTIN",
        "topic": "Pasangan Adverbia Frekuensi (いつも, よく, ときどき, あまり〜ない, ぜんぜん〜ない)",
        "stem": "Perhatikan skala frekuensi kebiasaan olahraga Ken berikut:\n'Ken tidak berolahraga sama sekali (0% frekuensi) sepanjang tahun ini.'\nKalimat bahasa Jepang yang TEPAT mengekspresikan kondisi mutlak Ken tersebut adalah...",
        "correct": "Kenさんは 今年 全然 運動しませんでした。 (Zenzen berpasangan dengan bentuk predikat negatif masen untuk menyatakan sama sekali tidak).",
        "distractors": [
            "Kenさんは 今年 いつも 運動しませんでした。 (Penggabungan itsumo dengan negatif yang tidak berterima dalam tata bahasa Jepang).",
            "Kenさんは 今年 あまり 運動しませんでした。 (Amari bermakna 'jarang / tidak begitu sering', bukan penolakan mutlak 0%).",
            "Kenさんは 今年 ときどき 運動しました。 (Tokidoki bermakna kadang-kadang yang bertentangan dengan fakta 0%).",
            "Kenさんは 今年 よく 運動しました。 (Yoku bermakna sering/kerap kali berolahraga)."
        ],
        "formula": {
            "title": "SPEKTRUM ADVERBIA FREKUENSI (頻度副詞の呼応関係)",
            "latex": "\\begin{array}{ccc} \\mathbf{\\text{ぜんぜん (Zenzen)}} & + & \\mathbf{\\text{Negatif (〜ません)}} \\implies 0\\% \\text{ (Sama sekali tidak)} \\\\ \\text{あまり (Amari)} & + & \\text{Negatif (〜ません)} \\implies 20\\% \\text{ (Jarang)} \\\\ \\text{ときどき (Tokidoki)} & + & \\text{Positif (〜ます)} \\implies 50\\% \\text{ (Kadang-kadang)} \\\\ \\text{いつも (Itsumo)} & + & \\text{Positif (〜ます)} \\implies 100\\% \\text{ (Selalu)} \\end{array}",
            "legend": "• Menuntut keselarasan sintaksis (呼応 - koou) antara kata keterangan dan kutub predikat"
        },
        "hints": {
            "concept": "Tingkat frekuensi 0% (sama sekali tidak) diungkapkan dengan pasangan '全然' (zenzen) + bentuk negatif (〜ません).",
            "execution": "Pilih: 'Kenさんは 今年 全然 運動しませんでした。'."
        }
    },
    {
        "id": "jpn-sim-16",
        "materi": "TATA BAHASA BUNPOU: KATA BANTU TANYA KO-SO-A-DO ADJEKTIVAL",
        "topic": "Pembedaan Kono/Sono/Ano/Dono vs Kore/Sore/Are/Dore",
        "stem": "Lengkapilah kalimat rumpang berikut di mana pembicara menunjuk sebuah jam tangan yang berada di dekat lawan bicara:\n'( ... ) とけいは だれの ですか。とても すてきですね。'",
        "correct": "その (Sono - kata tunjuk yang wajib diikuti langsung oleh kata benda nomina 'tokei').",
        "distractors": [
            "それ (Sore - kata ganti benda independen yang dilarang keras memodifikasi kata benda lain secara langsung tanpa partikel).",
            "これ (Kore - kata ganti mandiri untuk benda di tangan pembicara sendiri).",
            "この (Kono - kata tunjuk yang keliru karena mengacu pada area pembicara, bukan lawan bicara).",
            "あの (Ano - kata tunjuk yang mengacu pada benda yang posisinya jauh dari kedua pihak)."
        ],
        "formula": {
            "title": "DISTINGSI PRENOMINAL VS PRONOMINA (連体詞と代名詞の区別)",
            "latex": "\\begin{cases} \\mathbf{\\text{Prenominal:}} & \\mathbf{\\text{この / その / あの / どの}} + \\mathbf{\\text{Nomina (とけい)}} \\\\ \\mathbf{\\text{Pronomina:}} & \\text{これ / それ / あれ / どれ} + [\\cancel{\\text{Nomina}}] \\end{cases}",
            "legend": "• Kata tunjuk yang melekat langsung pada kata benda wajib berakhiran fonem /-no/"
        },
        "hints": {
            "concept": "Di depan kata benda (tokei) yang letaknya dekat lawan bicara wajib memakai bentuk rentai-shi: その (sono), bukan それ (sore).",
            "execution": "Pilih: 'その (Sono)'."
        }
    },
    {
        "id": "jpn-sim-17",
        "materi": "TATA BAHASA BUNPOU: NOMINALISASI KATA KERJA",
        "topic": "Teknik Nominalisasi Klausa dengan No (〜の) dan Koto (〜こと)",
        "stem": "Perhatikan kalimat pernyataan hobi berikut:\n'私の 趣味は 休日に ギターを ( ... ) ことです。'\nBentuk verba 'ひきます' (memetik/memainkan alat musik dawai) yang BENAR untuk mengisi rumpang nominalisasi adalah...",
        "correct": "ひく (Hiku - bentuk kamus jisho-kei wajib mendahului kata pembenda 'koto').",
        "distractors": [
            "ひきます (Hikimasu - bentuk masu formal yang tidak boleh memodifikasi kata benda koto).",
            "ひいて (Hiite - bentuk te yang memerlukan kata kerja sambungan lain).",
            "ひいた (Hiita - bentuk lampau yang tidak logis untuk menyatakan deskripsi hobi permanen).",
            "ひき (Hiki - bentuk akar kata yang tidak baku sebelum koto)."
        ],
        "formula": {
            "title": "NOMINALISASI KLAUSA VERBAL (動詞の連体形名詞化)",
            "latex": "\\mathbf{V\\text{-辞書形 (Kamus)}} + \\mathbf{\\text{こと / の}} \\implies \\text{Hal / Tindakan melakukan } V",
            "legend": "• Mengonversi predikat dinamis menjadi frasa nomina yang dapat mengisi fungsi gramatikal"
        },
        "hints": {
            "concept": "Sebelum 'ことです' untuk menyatakan hobi, kata kerja wajib berada dalam bentuk kamus (jisho-kei): ひく (hiku).",
            "execution": "Pilih opsi: 'ひく (Hiku)'."
        }
    },
    {
        "id": "jpn-sim-18",
        "materi": "TATA BAHASA BUNPOU: POLA KALIMAT MODALITAS HASIL",
        "topic": "Keputusan Institusional / Ketetapan Pihak Luar (Koto ni naru - 〜ことになる)",
        "stem": "Seorang karyawan memberi tahu keluarganya mengenai keputusan mutasi kantor:\n'会社の 命令で、来月から 大阪支社へ 転勤する ( ... ) ました。'\nUngkapan gramatikal yang TEPAT untuk menyatakan bahwa mutasi tersebut merupakan 'keputusan sepihak dari perusahaan' (bukan keputusan pribadi karyawan) adalah...",
        "correct": "ことに なり (Koto ni nari - pola koto ni naru menandai keputusan atau ketetapan yang ditentukan oleh otoritas luar/organisasi).",
        "distractors": [
            "ことに きめ (Koto ni kime - pola koto ni kimeru menandai keputusan kehendak pribadi karyawan sendiri).",
            "ように し (You ni shi - pola you ni suru menandai usaha pembiasaan diri melakukan sesuatu secara rutin).",
            "はずが あり (Hazu ga ari - pola hazu ga arimasen yang menandai ketiadaan keniscayaan rasional).",
            "つもりで い (Tsumori de i - menyatakan prasangka subjektif diri sendiri)."
        ],
        "formula": {
            "title": "DISTINGSI SUMBER KEPUTUSAN (決定の主体表現)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Keputusan Otoritas / Luar:}} & V\\text{-辞書形} + \\mathbf{\\text{ことに なりました (Koto ni narimashita)}} \\\\ \\mathbf{\\text{Keputusan Mandiri:}} & V\\text{-辞書形} + \\text{ことに しました (Koto ni shimashita)} \\end{aligned}",
            "legend": "• Menunjukkan kepatuhan subjek terhadap garis instruksi korporat (Meirei)"
        },
        "hints": {
            "concept": "Keputusan yang datang dari pihak luar/perusahaan (会社の命令で) diungkapkan dengan: ことになりました (koto ni narimashita).",
            "execution": "Pilih: 'ことに なり (Koto ni nari)'."
        }
    },
    {
        "id": "jpn-sim-19",
        "materi": "TATA BAHASA BUNPOU: PERKIRAAN BERDASARKAN INDRA",
        "topic": "Penggunaan You da (~ようだ) Berdasarkan Fakta Lapangan",
        "stem": "Melihat orang-orang di luar gedung yang berjalan mengenakan jas hujan dan membuka payung basah, seseorang berujar:\n'外を 歩いている 人たちが 傘を さしていますね。外は 雨が ( ... ) ようです。'\nBentuk predikat yang TEPAT melengkapi kesimpulan dugaan observasional tersebut adalah...",
        "correct": "ふっている (Futte iru - bentuk sedang berlangsung te iru mendahului kopula dugaan you da).",
        "distractors": [
            "ふりそう (Furisou - dugaan sekilas sebelum hujan turun yang bertentangan dengan fakta payung basah).",
            "ふったらしい (Bentuk rashii kabar angin yang kurang tepat untuk pengamatan langsung mata kepala sendiri).",
            "ふらなさ (Bentuk peniadaan yang bertentangan dengan visual orang memakai payung).",
            "ふれ (Bentuk imperatif perintah yang tidak dapat melekat sebelum you da)."
        ],
        "formula": {
            "title": "DUGAAN DEDUKTIF VISUAL (視覚証拠に基づく推量「〜ようだ」)",
            "latex": "\\mathbf{\\text{Bukti Visual (Orang Buka Payung)}} \\xrightarrow{\\text{Deduksi Rasional}} \\mathbf{V\\text{-ている}} + \\mathbf{\\text{ようです (Tampaknya sedang hujan)}}",
            "legend": "• Mengonstruksi kesimpulan logis dari tanda-tanda fisik yang tertangkap panca indra"
        },
        "hints": {
            "concept": "Melihat orang-orang memakai payung basah, kesimpulan deduktifnya adalah di luar tampaknya sedang turun hujan: ふっている ようです.",
            "execution": "Pilih: 'ふっている (Futte iru)'."
        }
    },
    {
        "id": "jpn-sim-20",
        "materi": "TATA BAHASA BUNPOU: KATA SAMBUNG KONDISIONAL",
        "topic": "Kondisional Alamiah / Keniscayaan Mutlak (~To)",
        "stem": "Instruksi pengoperasian mesin otomatis:\n'この 赤い ボタンを ( ... )、おつりが 出ます。'\nBentuk verba bersyarat yang TEPAT untuk menyatakan 'jika tombol ini ditekan, uang kembalian pasti otomatis keluar' adalah...",
        "correct": "おすと (Osu to - partikel to melekat pada verba bentuk kamus untuk menyatakan hukum sebab-akibat mesin/alam yang pasti).",
        "distractors": [
            "おしたら (Oshitara - kondisional percakapan umum yang kurang tepat untuk relasi mekanis keniscayaan tombol).",
            "おせば (Oseba - bentuk pengandaian hipotetis yang tidak menekankan otomatisasi seketika).",
            "おすなら (Osunara - partikel nara yang digunakan untuk merespons topik yang diangkat lawan bicara).",
            "おして (Oshite - bentuk te sekuensial yang tidak memiliki kekuatan klausa bersyarat mutlak)."
        ],
        "formula": {
            "title": "KENISCAYAAN MEKANIK & ALAM (確定条件・自然法則の「と」)",
            "latex": "\\mathbf{V\\text{-辞書形 (Kamus)}} + \\mathbf{\\text{と}} \\implies \\text{Pasti seketika terjadi akibat otomatis (Keniscayaan Mesin/Hukum Alam)}",
            "legend": "• Menandai korelasi deterministik 100% tanpa adanya intervensi kehendak manusia"
        },
        "hints": {
            "concept": "Hubungan otomatis mesin (menekan tombol -> uang keluar) menggunakan pola kondisional pasti: V(kamus) + と: おすと (osu to).",
            "execution": "Pilih: 'おすと (Osu to)'."
        }
    },
    {
        "id": "jpn-sim-21",
        "materi": "KAIWA HYOUGEN: ETIKA BERKUNJUNG KE RUMAH",
        "topic": "Salam Memasuki Rumah Orang Lain (お邪魔します)",
        "stem": "Saat diundang dan melangkahkan kaki melewati pintu masuk (*genkan*) rumah orang Jepang, ungkapan salam yang WAJIB diucapkan tamu adalah...",
        "correct": "お邪魔します (Ojamashimasu - permisi karena kehadiran saya akan sedikit mengganggu ketenangan rumah tuan rumah).",
        "distractors": [
            "いらっしゃいませ (Irasshaimase - salam selamat datang yang diucapkan tuan rumah atau pelayan toko).",
            "ごめんください (Gomen kudasai - ucapan memanggil dari luar pintu saat mengetuk rumah yang sepi).",
            "おかえりなさい (Okaerinasai - salam menyambut anggota keluarga sendiri yang baru pulang ke rumah).",
            "かしこまりました (Kashikomarimashita - ungkapan kepatuhan staf hotel/restoran saat menerima pesanan klien)."
        ],
        "formula": {
            "title": "ETIKA MEMASUKI KEDIAMAN (訪問時の挨拶作法)",
            "latex": "\\text{Masuk Rumah Tamu: } \\mathbf{\\text{お邪魔します (Ojamashimasu)}} \\quad \\longleftrightarrow \\quad \\text{Pamit Pulang: } \\text{お邪魔しました}",
            "legend": "• Kerendahan hati mengakui bahwa kedatangan tamu membawa kerepotan bagi tuan rumah"
        },
        "hints": {
            "concept": "Masuk ke rumah orang lain mengucapkan: 'お邪魔します' (Ojamashimasu).",
            "execution": "Pilih: 'お邪魔します (Ojamashimasu)'."
        }
    },
    {
        "id": "jpn-sim-22",
        "materi": "KAIWA HYOUGEN: APRESIASI KERJA KERAS",
        "topic": "Salam Penutupan Acara / Selesai Bekerja Sama (お疲れ様でした)",
        "stem": "Setelah seluruh siswa selesai membersihkan ruang kelas dan lapangan sekolah bersama-sama, ucapan saling mengapresiasi kerja keras yang PALING TEPAT diucapkan antarsiswa adalah...",
        "correct": "お疲れ様でした (Otsukaresama deshita - terima kasih atas kerja keras dan keletihan yang telah kita curahkan bersama).",
        "distractors": [
            "ごちそうさまでした (Ucapan selesai makan yang tidak relevan dengan aktivitas kerja bakti kebersihan).",
            "失礼します (Ungkapan permisi saat memasuki ruang guru atau menyela pembicaraan).",
            "どういたしまして (Balasan sama-sama yang kurang mencerminkan apresiasi kolektif atas kerja fisik).",
            "お大事に (Odaiji ni - ucapan lekas sembuh yang khusus ditujukan kepada orang yang sedang sakit)."
        ],
        "formula": {
            "title": "SALAM APRESIASI KOLEKTIF (労いの挨拶)",
            "latex": "\\text{Selesai Aktivitas Bersama} \\implies \\mathbf{\\text{お疲れ様でした (Otsukaresama deshita)}}",
            "legend": "• Membangun solidaritas kelompok dengan mengakui kelelahan fisik sebagai pengorbanan mulia"
        },
        "hints": {
            "concept": "Selesai bekerja keras/kerja bakti bersama, ucapan apresiasi yang baku adalah 'お疲れ様でした' (Otsukaresama deshita).",
            "execution": "Pilih: 'お疲れ様でした (Otsukaresama deshita)'."
        }
    },
    {
        "id": "jpn-sim-23",
        "materi": "KAIWA HYOUGEN: MENJENGUK ORANG SAKIT",
        "topic": "Doa Lekas Sembuh (お大事に)",
        "stem": "Saat menjenguk teman sekelas yang sedang dirawat di ruang UKS atau rumah sakit, ucapan simpati dan doa lekas sembuh yang BENAR dalam bahasa Jepang adalah...",
        "correct": "お大事に (Odaiji ni - semoga lekas sembuh dan rawatlah tubuh Anda dengan sebaik-baiknya).",
        "distractors": [
            "お元気ですか (Menanyakan kabar seolah-olah orang tersebut dalam kondisi prima bugar).",
            "おめでとうございます (Ucapan selamat berbahagia yang sangat tidak pantas diucapkan kepada orang sakit).",
            "気をつけてください (Peringatan agar berhati-hati di jalan yang ditujukan kepada pelancong).",
            "頑張ってください (Dorongan semangat berkompetisi yang justru dapat membebani psikologis orang sakit parah)."
        ],
        "formula": {
            "title": "UNGKAPAN SIMPATI KESEHATAN (見舞いの言葉)",
            "latex": "\\text{Kepada Orang Sakit} \\implies \\mathbf{\\text{お大事に (おだいじに - Odaiji ni)}}",
            "legend": "• Singkatan santun dari 'どうぞ お体を お大事に なさってください'"
        },
        "hints": {
            "concept": "Ucapan lekas sembuh untuk orang sakit adalah 'お大事に' (Odaiji ni).",
            "execution": "Pilih: 'お大事に (Odaiji ni)'."
        }
    },
    {
        "id": "jpn-sim-24",
        "materi": "BUDAYA & ETIKA: ETIKA ALAT MAKAN SUMPIT (HASHI)",
        "topic": "Tabu Menusukkan Sumpit Tegak pada Mangkuk Nasi (Tsukitate-bashi)",
        "stem": "Dalam etika bersantap di Jepang, menusukkan sepasang sumpit secara tegak lurus di tengah-tengah mangkuk nasi (*Tsukitate-bashi*) merupakan TABU BESAR yang dilarang keras karena...",
        "correct": "Menyerupai ritual pemakaman tradisional Buddha di mana nasi persembahan untuk arwah orang meninggal disajikan dengan sumpit tertancap tegak.",
        "distractors": [
            "Dapat merusak lapisan keramik mangkuk nasi sehingga pemilik restoran akan menuntut ganti rugi materiil.",
            "Dipercaya dapat membuat kandungan karbohidrat dan gizi pada nasi menguap hilang seketika.",
            "Merupakan tanda deklarasi permusuhan fisik kepada koki yang memasak nasi di dapur restoran.",
            "Dapat mengundang serbuan burung gagak hitam masuk ke dalam ruang makan perjamuan."
        ],
        "formula": {
            "title": "TABU PENGGUNAAN SUMPIT (箸の禁忌マナー：突き立て箸)",
            "latex": "\\mathbf{\\text{突き立て箸 (Sumpit Tegak)}} \\equiv \\mathbf{\\text{枕ご飯 (Nasi Persembahan Jenazah / Kematian)}} \\implies \\text{TABU BESAR}",
            "legend": "• Asosiasi simbolik kematian yang dilarang keras muncul dalam perjamuan orang hidup"
        },
        "hints": {
            "concept": "Menusukkan sumpit tegak di mangkuk nasi (Tsukitate-bashi) menyerupai dupa/nasi persembahan arwah pada upacara kematian (pemakaman).",
            "execution": "Pilih opsi yang mengaitkan tabu tersebut dengan ritual pemakaman / persembahan orang meninggal."
        }
    },
    {
        "id": "jpn-sim-25",
        "materi": "BUDAYA & ETIKA: ETIKA TRANSPORTASI PUBLIK",
        "topic": "Aturan Kursi Prioritas Kereta Listrik (Yuusenseki - 優先席)",
        "stem": "Di setiap gerbong kereta listrik di Jepang, terdapat area khusus 'Kursi Prioritas' (*Yuusenseki*). Manakah etika yang BENAR dan wajib dipatuhi penumpang terkait area tersebut?",
        "correct": "Wajib mendahulukan kursi bagi lansia, penyandang disabilitas, ibu hamil, atau penumpang sakit, serta mematikan daya ponsel jika gerbong dalam kondisi sangat padat.",
        "distractors": [
            "Seluruh penumpang usia muda dilarang keras menginjakkan kaki di lantai gerbong di depan area kursi prioritas.",
            "Kursi prioritas hanya boleh diduduki oleh penumpang yang membeli tiket kelas satu shinkansen bertarif khusus.",
            "Penumpang yang duduk di kursi prioritas diwajibkan menyalakan pengeras suara telepon untuk memantau berita terkini.",
            "Kursi prioritas harus selalu dibiarkan kosong 24 jam meskipun di dalam kereta sama sekali tidak ada lansia atau penumpang berkebutuhan khusus."
        ],
        "formula": {
            "title": "REGULASI KURSI PRIORITAS (優先席の利用規律)",
            "latex": "\\mathbf{\\text{優先席 (Yuusenseki)}} \\implies \\begin{cases} \\text{Prioritas: Lansia, Difabel, Ibu Hamil, Cedera} \\\\ \\text{Elektronik: Nonaktifkan HP saat padat (Pacemaker)} \\end{cases}",
            "legend": "• Menjaga keamanan medis pengguna alat pacu jantung dan keadilan akses sosial"
        },
        "hints": {
            "concept": "Kursi prioritas diutamakan untuk lansia, difabel, ibu hamil, orang sakit, serta mematikan HP saat gerbong sangat padat (demi pengguna alat pacu jantung).",
            "execution": "Pilih opsi yang menjelaskan prioritas bagi kelompok rentan dan mematikan HP saat padat."
        }
    },

    # -------------------------------------------------------------
    # 5 MULTI-SELECT ITEMS (jpn-sim-26 .. jpn-sim-30)
    # -------------------------------------------------------------
    {
        "id": "jpn-sim-26",
        "materi": "MOJIGOI: RADIKAL KANJI (BUSHU)",
        "topic": "Radikal Air (Sanzui - 氵) pada Kanji Bahasa Jepang",
        "stem": "Radikal dasar kanji (*Bushu*) sering kali mencerminkan rumpun makna semantik kata. Manakah di antara kanji-kanji berikut yang tersusun dengan radikal 'Air' (*Sanzui* - 氵)? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "海 (Umi - Laut / Samudra)."},
            {"key": "B", "text": "池 (Ike - Kolam air)."},
            {"key": "C", "text": "泳 (Oyogu - Berenang di air)."},
            {"key": "D", "text": "校 (Kou - Sekolah tempat menuntut ilmu)."},
            {"key": "E", "text": "休 (Yasumu - Beristirahat di bawah pohon)."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "RADIKAL SANZUI AIR (部首「さんずい・氵」)",
            "latex": "\\mathbf{[氵 (Air)]} \\implies \\begin{cases} \\mathbf{\\text{海 (Umi / Laut)}} \\\\ \\mathbf{\\text{池 (Ike / Kolam)}} \\\\ \\mathbf{\\text{泳 (Oyogu / Renang)}} \\end{cases}",
            "legend": "• 校 beradikalkan pohon (木); 休 beradikalkan manusia (亻)"
        },
        "hints": {
            "concept": "Radikal Sanzui (氵) berhubungan dengan air: 海 (laut), 池 (kolam), 泳 (berenang). Kanji 校 memakai radikal pohon (木), 休 memakai radikal manusia (亻).",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },
    {
        "id": "jpn-sim-27",
        "materi": "TATA BAHASA BUNPOU: KLASIFIKASI VERBA",
        "topic": "Identifikasi Verba Golongan I (Godan Doushi)",
        "stem": "Dalam morfologi bahasa Jepang, kata kerja terbagi ke dalam tiga kelompok (Golongan I/Godan, Golongan II/Ichidan, dan Golongan III/Fukisoku). Manakah di antara kata kerja bentuk kamus (*Jisho-kei*) berikut yang termasuk ke dalam Verba Golongan I (Godan Doushi)? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "飲む (Nomu - minum)."},
            {"key": "B", "text": "書く (Kaku - menulis)."},
            {"key": "C", "text": "話す (Hanasu - berbicara)."},
            {"key": "D", "text": "食べる (Taberu - makan, berakhiran -eru vokal e sebelum ru)."},
            {"key": "E", "text": "する (Suru - melakukan, kata kerja tidak beraturan Golongan III)."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "KLASIFIKASI KELOMPOK KATA KERJA (動詞のグループ分類)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Golongan I (Godan):}} & \\mathbf{\\text{飲む (nom-u), 書く (kak-u), 話す (hanas-u)}} \\\\ \\text{Golongan II (Ichidan):} & \\text{食べる (tabe-ru), 見る (mi-ru)} \\\\ \\text{Golongan III (Irregular):} & \\text{する (suru), 来る (kuru)} \\end{aligned}",
            "legend": "• Godan doushi mengalami konjugasi fonologis melintasi lima baris vokal (a, i, u, e, o)"
        },
        "hints": {
            "concept": "Nomu, Kaku, dan Hanasu adalah verba Golongan 1 (Godan). Taberu adalah Golongan 2 (Ichidan). Suru adalah Golongan 3 (Irregular).",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },
    {
        "id": "jpn-sim-28",
        "materi": "TATA BAHASA BUNPOU: REGISTER KEIGO",
        "topic": "Pasangan Verba Sonkeigo (Hormat Subjek Atasan) yang Sahih",
        "stem": "Manakah di antara pasangan kata kerja biasa dan bentuk Sonkeigo (ragam hormat untuk meninggikan perbuatan atasan) berikut yang BENAR menurut kaidah keigo baku? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "言う (Iu) \\to おっしゃる (Ossharu)."},
            {"key": "B", "text": "食べる (Taberu) \\to 召し上がる (Meshiagaru)."},
            {"key": "C", "text": "見る (Miru) \\to ご覧になる (Goran ni naru)."},
            {"key": "D", "text": "行く (Iku) \\to 参る (Mairu - ini adalah bentuk Kenjougo rendah hati, bukan Sonkeigo)."},
            {"key": "E", "text": "する (Suru) \\to いたす (Itasu - ini adalah bentuk Kenjougo rendah hati, bukan Sonkeigo)."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "INVENTARIS KOSAKATA SONKEIGO KHUSUS (特定の尊敬語対応)",
            "latex": "\\begin{aligned} \\mathbf{\\text{言う}} & \\to \\mathbf{\\text{おっしゃる}} \\\\ \\mathbf{\\text{食べる / 飲む}} & \\to \\mathbf{\\text{召し上がる}} \\\\ \\mathbf{\\text{見る}} & \\to \\mathbf{\\text{ご覧になる}} \\end{aligned}",
            "legend": "• Mairu dan Itasu adalah Kenjougo (merendahkan diri), bukan Sonkeigo"
        },
        "hints": {
            "concept": "Sonkeigo: Iu -> Ossharu; Taberu -> Meshiagaru; Miru -> Goran ni naru. Bentuk Mairu dan Itasu adalah Kenjougo (merendahkan diri sendiri).",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },
    {
        "id": "jpn-sim-29",
        "materi": "BUDAYA & ETIKA: TATA CARA ZIARAH KUIL SHINTO (JINJA)",
        "topic": "Protokol Ibadah di Kuil Shinto (Temizuya & Nirei Nihai Ichirei)",
        "stem": "Saat mengunjungi kuil Shinto (*Jinja*) di Jepang, terdapat tata tertib peribadatan dan penyucian diri tradisional yang wajib ditaati pengunjung. Manakah di antara prosedur berikut yang BENAR sesuai adat Shinto? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Menundukkan kepala sedikit (*eshaku*) saat melewati pintu gerbang suci *Torii* di jalan masuk kuil."},
            {"key": "B", "text": "Membersihkan tangan kiri, tangan kanan, dan berkumur air di paviliun penyucian air (*Temizuya*) sebelum berdoa."},
            {"key": "C", "text": "Melakukan ritual doa dengan urutan: 2 kali membungkuk dalam, 2 kali tepuk tangan, berdoa, dan 1 kali membungkuk (*Ni-rei, Ni-hai, Ichi-rei*)."},
            {"key": "D", "text": "Berjalan tepat di tengah-tengah jalan utama (*Seichuu*) karena jalur tengah memang khusus disediakan untuk peziarah umum."},
            {"key": "E", "text": "Menyembelih hewan kurban di depan altar utama kuil sebagai syarat wajib penerimaan doa peziarah."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "PROTOKOL ZIARAH JINJA (神社参拝の作法)",
            "latex": "\\text{1. Bungkuk di Torii} \\to \\text{2. Bersuci di Temizuya} \\to \\mathbf{\\text{3. Ritual 二礼二拍手一礼 (2 Bungkuk, 2 Tepuk, 1 Bungkuk)}}",
            "legend": "• Jalur tengah (Seichuu) adalah jalur lewatnya para Kami (Dewa), manusia wajib berjalan di sisi pinggir"
        },
        "hints": {
            "concept": "Prosedur ziarah kuil Shinto: 1) Membungkuk di gerbang Torii, 2) Menyucikan tangan dan mulut di Temizuya, 3) Ritual Ni-rei Ni-hai Ichi-rei (2 bungkuk, 2 tepuk, 1 bungkuk). Jalur tengah (Seichuu) tidak boleh dilewati karena jalan dewa.",
            "execution": "Pilih A, B, dan C. Tolak D (jalan tengah tabu) dan E (tidak ada kurban hewan)."
        }
    },
    {
        "id": "jpn-sim-30",
        "materi": "BUDAYA & SENI: TRADISI SENI KLASIK JEPANG",
        "topic": "Karakteristik Teater Klasik Kabuki dan Noh",
        "stem": "Kesenian teater panggung tradisional Jepang memiliki sejarah panjang yang kaya. Manakah pernyataan berikut yang TEPAT mengenai seni teater tradisional *Kabuki* dan *Noh*? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Kabuki dikenal dengan riasan wajah mencolok yang dramatis (*Kumadori*) dan kostum panggung yang sangat mewah."},
            {"key": "B", "text": "Dalam tradisi teater Noh, para pemeran utama mengenakan topeng kayu artistik (*Noh-men*) untuk mengekspresikan karakter emosi tokoh."},
            {"key": "C", "text": "Dalam teater Kabuki tradisional, seluruh peran tokoh wanita diperankan oleh aktor pria yang terlatih khusus (*Onnagata*)."},
            {"key": "D", "text": "Kabuki dan Noh merupakan seni pertunjukan modern abad ke-21 yang diadaptasi sepenuhnya dari animasi anime barat."},
            {"key": "E", "text": "Penonton teater Kabuki diwajibkan ikut naik ke atas panggung untuk bertarung pedang dengan para pemeran samurai."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "KARAKTERISTIK TEATER TRADISIONAL (伝統芸能：歌舞伎と能)",
            "latex": "\\begin{cases} \\mathbf{\\text{Kabuki:}} & \\text{Riasan Kumadori, Aktor Pria Pemeran Wanita (Onnagata), Dinamis} \\\\ \\mathbf{\\text{Noh:}} & \\text{Topeng Kayu Noh-men, Gerakan Lambat Meditatif Simbolik} \\end{cases}",
            "legend": "• Warisan Budaya Takbenda Dunia UNESCO yang terpelihara lintas generasi"
        },
        "hints": {
            "concept": "A (rias kumadori), B (topeng noh-men pada teater Noh), dan C (onnagata: pria memerankan wanita di Kabuki) adalah karakteristik otentik seni teater tradisional Jepang.",
            "execution": "Pilih A, B, dan C. Tolak D dan E."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH ITEMS (jpn-sim-31 .. jpn-sim-35)
    # -------------------------------------------------------------
    {
        "id": "jpn-sim-31",
        "materi": "TATA BAHASA BUNPOU: EVALUASI PARTIKEL SINTAKSIS",
        "topic": "Validitas Penggunaan Partikel Bahasa Jepang dalam Berbagai Konteks",
        "stem": "Berikut disajikan pernyataan mengenai fungsi dan kaidah partikel bahasa Jepang (*Joshi*). Tentukan apakah masing-masing pernyataan BENAR atau SALAH!",
        "statements": [
            {
                "text": "Partikel 「を」 (wo/o) berfungsi menandai objek penderita langsung yang menerima tindakan dari kata kerja transitif.",
                "correct": "Benar"
            },
            {
                "text": "Partikel 「で」 (de) digunakan untuk menandai titik waktu spesifik yang memiliki angka kalender pasti seperti jam dan tanggal.",
                "correct": "Salah"
            },
            {
                "text": "Partikel 「に」 (ni) dapat berfungsi menunjukkan target arah kedatangan atau tujuan akhir dari verba perpindahan seperti ikimasu.",
                "correct": "Benar"
            },
            {
                "text": "Partikel 「へ」 (e) ditulis dengan huruf hiragana 'he' namun wajib dilafalkan sebagai fonem vokal 'e' saat berfungsi sebagai penunjuk arah gerak.",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "EVALUASI FUNGSI KASUS PARTIKEL (助詞機能の正誤判定)",
            "latex": "\\begin{aligned} \\text{Partikel を: } & \\text{Benar (Objek langsung transitif)} \\\\ \\text{Partikel で: } & \\text{Salah (Waktu spesifik memakai に, de untuk sarana/tempat aksi)} \\\\ \\text{Partikel に: } & \\text{Benar (Titik target arah gerak)} \\\\ \\text{Partikel へ: } & \\text{Benar (Ditulis 'he', dilafalkan 'e')} \\end{aligned}",
            "legend": "• Menunjukkan ketelitian penguasaan partikel dasar dan fonologinya"
        },
        "hints": {
            "concept": "1=Benar (を untuk objek). 2=Salah (waktu spesifik memakai に, bukan で). 3=Benar (に untuk target arah tujuan). 4=Benar (へ ditulis he dilafalkan e).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Benar."
        }
    },
    {
        "id": "jpn-sim-32",
        "materi": "TATA BAHASA BUNPOU: EVALUASI KONJUGASI VERBA",
        "topic": "Kaidah Morfologi dan Perubahan Bentuk Kata Kerja Jepang",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan terkait aturan konjugasi kata kerja bahasa Jepang berikut!",
        "statements": [
            {
                "text": "Kata kerja Golongan II (Ichidan) seperti 'たべる' dan 'みる' membentuk bentuk Te dengan cukup mencoret 'る' dan menambahkan 'て'.",
                "correct": "Benar"
            },
            {
                "text": "Kata kerja bentuk kamus 'いく' (ikimasu) berubah menjadi bentuk Te beraturan 'いいて' sesuai kaidah umum akhiran -ku.",
                "correct": "Salah"
            },
            {
                "text": "Pola kalimat keharusan 「〜なければなりません」 dibentuk dari verba bentuk negatif (Nai-kei) dengan mencoret huruf vokal 'い' dan menggantinya dengan 'ければなりません'.",
                "correct": "Benar"
            },
            {
                "text": "Bentuk potensial (kemampuan / bisa) dari kata kerja Golongan I selalu berakhiran bunyi vokal baris 'あ' (a-dan).",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI KONJUGASI VERBAL (動詞活用の正誤判定)",
            "latex": "\\begin{aligned} \\text{Ichidan Te: } & \\text{Benar (る } \\to \\text{ て)} \\\\ \\text{Ikimasu: } & \\text{Salah (Pengecualian mutlak: 行く } \\to \\mathbf{\\text{行って}}, \\text{ bukan いいて)} \\\\ \\text{Nakereba: } & \\text{Benar (〜ない } \\to \\text{ 〜なければなりません)} \\\\ \\text{Potensial Godan: } & \\text{Salah (Berubah ke baris 'え' / e-dan, seperti 書く } \\to \\text{ 書ける)} \\end{aligned}",
            "legend": "• Evaluasi komprehensif morfologi verba baku Kurikulum Merdeka"
        },
        "hints": {
            "concept": "1=Benar. 2=Salah (Pengecualian khusus: 行く menjadi 行って, bukan いいて). 3=Benar (Nai -> Nakereba narimasen). 4=Salah (Potensial Godan berubah ke baris 'e', seperti kaku -> kakeru, bukan baris 'a').",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "jpn-sim-33",
        "materi": "MOJIGOI: PASANGAN VERBA TRANSITIF & INTRANSITIF",
        "topic": "Evaluasi Pasangan Jidoushi (Otomatis) dan Tadoushi (Sengaja)",
        "stem": "Berikut disajikan pasangan kata kerja transitif (*Tadoushi*) dan intransitif (*Jidoushi*). Tentukan apakah klasifikasi makna dan partikelnya BENAR atau SALAH!",
        "statements": [
            {
                "text": "「ドアが 閉まる (shimaru)」merupakan bentuk intransitif yang berarti pintu tertutup dengan sendirinya.",
                "correct": "Benar"
            },
            {
                "text": "「電気を 消す (keshu)」merupakan bentuk transitif yang berarti seseorang sengaja memadamkan lampu.",
                "correct": "Benar"
            },
            {
                "text": "「財布を 落とす (otosu)」merupakan bentuk intransitif di mana dompet jatuh sendiri tanpa ada subjek yang menjatuhkan.",
                "correct": "Salah"
            },
            {
                "text": "「お湯が 沸く (waku)」merupakan bentuk intransitif yang berarti air mendidih karena proses pemanasan alami/ketel.",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "EVALUASI PASANGAN JIDOUSHI-TADOUSHI (自他動詞対の判定)",
            "latex": "\\begin{aligned} \\text{閉まる (shimaru): } & \\text{Benar (Intransitif / Otomatis)} \\\\ \\text{消す (kesu): } & \\text{Benar (Transitif / Sengaja dimatikan)} \\\\ \\text{落とす (otosu): } & \\text{Salah (Otosu adalah transitif; intransitifnya adalah 落ちる / ochiru)} \\\\ \\text{沸く (waku): } & \\text{Benar (Intransitif; transitifnya adalah 沸かす / wakasu)} \\end{aligned}",
            "legend": "• Menentukan ketepatan relasi agen dan perubahan kondisi objek"
        },
        "hints": {
            "concept": "Pernyataan 3 SALAH karena '落とす' (otosu) adalah verba transitif (menjatuhkan). Bentuk intransitifnya (jatuh sendiri) adalah '落ちる' (ochiru).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Salah, 4=Benar."
        }
    },
    {
        "id": "jpn-sim-34",
        "materi": "KAIWA HYOUGEN: EVALUASI UNGKAPAN HARIAN & AISATSU",
        "topic": "Validitas Pemakaian Salam dan Respons Situasional Keseharian",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap pernyataan penggunaan ungkapan komunikasi harian bahasa Jepang berikut!",
        "statements": [
            {
                "text": "Ungkapan 「ただいま」 (Tadaima) diucapkan oleh orang yang menyambut kepulangan anggota keluarga di dalam rumah.",
                "correct": "Salah"
            },
            {
                "text": "Ucapan 「いただきます」 (Itadakimasu) secara etika diucapkan sesaat sebelum seseorang mulai menyantap hidangan makanannya.",
                "correct": "Benar"
            },
            {
                "text": "Kata 「どうも」 (Doumo) dapat berfungsi secara fleksibel sebagai sapaan santai, ucapan terima kasih ringan, maupun permohonan maaf singkat dalam konteks kasual.",
                "correct": "Benar"
            },
            {
                "text": "Salam 「さようなら」 (Sayounara) adalah sapaan wajib harian yang paling lumrah diucapkan seorang suami kepada istrinya setiap pagi saat pamit berangkat kerja.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI PRAGMATIK SALAM (日常挨拶の文脈適合性)",
            "latex": "\\begin{aligned} \\text{ただいま: } & \\text{Salah (Diucapkan orang yang baru pulang, penyambut menjawab おかえりなさい)} \\\\ \\text{いただきます: } & \\text{Benar (Sebelum makan)} \\\\ \\text{どうも: } & \\text{Benar (Ekspresi serbaguna santai)} \\\\ \\text{さようなら: } & \\text{Salah (Pamit ke kantor memakai いってきます, sayounara berjarak perpisahan lama)} \\end{aligned}",
            "legend": "• Menghindari kerancuan sosiolinguistik antara lingkungan domestik dan relasi formal"
        },
        "hints": {
            "concept": "1=Salah (Tadaima diucapkan oleh orang yang pulang, bukan yang menyambut). 2=Benar (sebelum makan). 3=Benar (doumo serbaguna). 4=Salah (suami pamit kerja memakai いってきます, bukan さようなら).",
            "execution": "Tentukan: 1=Salah, 2=Benar, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "jpn-sim-35",
        "materi": "BUDAYA & ETIKA SOSIAL: EVALUASI NORMA BUDAYA JEPANG",
        "topic": "Kebenaran Konsep Filosofi dan Etika Perilaku Masyarakat Jepang",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan mengenai konsep kebudayaan dan norma sosial Jepang berikut!",
        "statements": [
            {
                "text": "Konsep 'Uchi' (pihak dalam/kelompok sendiri) dan 'Soto' (pihak luar) mendasari pemilihan tata bahasa kesantunan (Keigo) dalam masyarakat Jepang.",
                "correct": "Benar"
            },
            {
                "text": "Di Jepang, memberikan uang tip tunai secara terpisah di atas meja restoran adalah kewajiban hukum yang sangat dihargai oleh para pelayan.",
                "correct": "Salah"
            },
            {
                "text": "Pada saat menaiki tangga berjalan (eskalator) di wilayah Tokyo dan sekitarnya (Kanto), orang yang berdiri diam berdiri di sebelah kiri untuk memberi jalan bagi orang yang tergesa-gesa di sebelah kanan.",
                "correct": "Benar"
            },
            {
                "text": "Membuka sepatu dan menggantinya dengan sandal rumah (*surippa*) di area *genkan* merupakan etika wajib saat memasuki rumah hunian orang Jepang.",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "EVALUASI SOSIO-KULTURAL JEPANG (日本文化・社会規範の判定)",
            "latex": "\\begin{aligned} \\text{Uchi-Soto: } & \\text{Benar (Pilar fundamental ragam bahasa hormat Keigo)} \\\\ \\text{Uang Tip: } & \\text{Salah (Tidak ada budaya tip di Jepang, bahkan dinilai merendahkan)} \\\\ \\text{Eskalator Tokyo: } & \\text{Benar (Berdiri di kiri di Kanto / Tokyo, kanan di Kansai)} \\\\ \\text{Lepas Sepatu di Genkan: } & \\text{Benar (Etika higienitas dan pemisahan batas ruang sakral rumah)} \\end{aligned}",
            "legend": "• Menunjukkan pemahaman mendalam tentang tata nilai dan etika hidup bangsa Jepang"
        },
        "hints": {
            "concept": "1=Benar (Uchi-Soto adalah basis Keigo). 2=Salah (di Jepang TIDAK ADA budaya memberi uang tip, pelayanan sudah termasuk dan tip dianggap tidak sopan). 3=Benar (di Tokyo berdiri di kiri eskalator). 4=Benar (lepas sepatu di genkan wajib).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Benar."
        }
    }
]
