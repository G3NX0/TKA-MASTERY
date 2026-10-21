# -*- coding: utf-8 -*-
"""
BAHASA JEPANG - PAKET SOAL LATIHAN MUDAH (EASY) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / JLPT N5
Distribusi:
- 10 Butir: Kanji & Kosakata N5 (Mojigoi - Cara baca on/kun, makna kata, jukugo dasar)
- 10 Butir: Tata Bahasa Dasar (Bunpou N5 - Partikel wa, ga, wo, ni, de, he, to, konjugasi masu/te/nai)
- 5 Butir: Ungkapan Komunikasi Keseharian & Etika Aisatsu
"""

BAHASA_JEPANG_EASY_ITEMS = [
    {
        "id": "jpn-lat-e-01",
        "materi": "MOJIGOI: KANJI DASAR N5",
        "topic": "Cara Baca Kanji Angka dan Penanggalan (日, 月, 年)",
        "stem": "Perhatikan kalimat berikut ini:\n'わたしは 毎月 [一日] に としょかんへ 行きます。'\nBagaimanakah cara baca yang TEPAT untuk kata kanji di dalam kurung [一日] ketika merujuk pada tanggal satu dalam penanggalan Jepang?",
        "correct": "ついたち (Tsuitachi - cara baca khusus penanggalan untuk tanggal 1 setiap bulan).",
        "distractors": [
            "いちにち (Ichinichi - cara baca yang merujuk pada durasi waktu selama satu hari, bukan penanggalan).",
            "ひとつひ (Hitotsuhi - penggabungan kunyomi angka hitotsu dan hi yang keliru dalam penanggalan).",
            "いちひ (Ichihi - pembacaan harfiah yang tidak dikenal dalam ortografi bahasa Jepang baku).",
            "つぎひ (Tsugihi - kesalahan asosiasi fonetis dengan kata tsugi yang berarti berikutnya)."
        ],
        "formula": {
            "title": "PENANGGALAN KHUSUS JEPANG (暦の特別な読み方)",
            "latex": "\\text{Kanji } [\\text{一日}] \\implies \\begin{cases} \\mathbf{\\text{ついたち (Tsuitachi)}} & \\text{Tanggal 1 (Kalender)} \\\\ \\text{いちにち (Ichinichi)} & \\text{Durasi 1 Hari} \\end{cases}",
            "legend": "• Tanggal 1-10 memiliki pembacaan khusus (tsuitachi, futsuka, mikka, yokka, dsb.)"
        },
        "hints": {
            "concept": "Tanggal satu dalam kalender Jepang memiliki pembacaan khusus tak reguler yaitu 'tsuitachi'. Bentuk 'ichinichi' dipakai untuk menyatakan rentang durasi (1 hari lamanya).",
            "execution": "Pilih opsi: 'ついたち (Tsuitachi)'."
        }
    },
    {
        "id": "jpn-lat-e-02",
        "materi": "MOJIGOI: KANJI DASAR N5",
        "topic": "Cara Baca Kanji Arah dan Posisi (上, 下, 中, 右, 左)",
        "stem": "Perhatikan kalimat berikut:\n'つくえの [上] に ノートと えんぴつが あります。'\nCara baca kunyomi yang TEPAT untuk kanji di dalam kurung [上] pada kalimat di atas adalah...",
        "correct": "うえ (Ue - di atas, menunjukkan posisi benda yang berada di permukaan meja).",
        "distractors": [
            "した (Shita - antonim yang memiliki arti posisi di bawah).",
            "なか (Naka - posisi di dalam ruang tertutup atau laci meja).",
            "まえ (Mae - posisi di depan atau di muka suatu objek).",
            "よこ (Yoko - posisi di samping atau sejajar secara horizontal)."
        ],
        "formula": {
            "title": "KANJI POSISI DASAR (位置の漢字)",
            "latex": "[\\text{上}] = \\mathbf{\\text{うえ (Ue / Atas)}} \\quad \\longleftrightarrow \\quad [\\text{下}] = \\text{した (Shita / Bawah)}",
            "legend": "• Menyatakan letak spasial benda relatif terhadap permukaan objek patokan"
        },
        "hints": {
            "concept": "Kanji 上 dibaca 'うえ' (ue) yang berarti bagian atas atau permukaan atas meja.",
            "execution": "Pilih opsi: 'うえ (Ue)'."
        }
    },
    {
        "id": "jpn-lat-e-03",
        "materi": "MOJIGOI: KANJI DASAR N5",
        "topic": "Cara Baca Kanji Waktu (時, 分, 半)",
        "stem": "Cermati teks singkat berikut:\n'いま [午前八時半] です。じゅぎょうが はじまります。'\nCara baca yang BENAR untuk gabungan kanji di dalam tanda kurung siku [午前八時半] adalah...",
        "correct": "ごぜんはちじはん (Gozen hachiji han - pukul 08.30 pagi).",
        "distractors": [
            "ごごはちじはん (Gogo hachiji han - keliru pada kanji 前 yang disalahartikan sebagai gogo/sore).",
            "ごぜんようじはん (Gozen youji han - pembacaan angka delapan yang tertukar dengan angka empat).",
            "ごぜんはちときはん (Gozen hachitoki han - pembacaan kanji 時 dengan kunyomi toki yang tidak tepat untuk jam).",
            "ごぜんはちじぶん (Gozen hachijibun - pembacaan kanji 半 yang disalahartikan sebagai bun/menit)."
        ],
        "formula": {
            "title": "NOTASI WAKTU JEPANG (時刻の表記)",
            "latex": "\\text{午前 (Gozen - AM)} + \\text{八時 (Hachi-ji - Pukul 8)} + \\text{半 (Han - Setengah/30 Menit)} = \\mathbf{\\text{ごぜんはちじはん}}",
            "legend": "• 午前 = AM (pagi), 午後 = PM (siang/malam), 半 = lewat 30 menit"
        },
        "hints": {
            "concept": "午前 dibaca 'gozen', 八時 dibaca 'hachiji', dan 半 dibaca 'han'.",
            "execution": "Pilih: 'ごぜんはちじはん'."
        }
    },
    {
        "id": "jpn-lat-e-04",
        "materi": "MOJIGOI: KANJI DASAR N5",
        "topic": "Makna Kanji Manusia dan Keluarga (父, 母, 兄, 姉, 子)",
        "stem": "Dalam percakapan sopan mengenai keluarga sendiri kepada lawan bicara, seseorang berkata:\n'私の [母] は 病院の 看護師です。'\nCara baca kanji [母] ketika menyebut ibu kandung sendiri adalah...",
        "correct": "はは (Haha - sebutan rendah hati untuk ibu kandung sendiri kepada pihak luar).",
        "distractors": [
            "おかあさん (Okaasan - sebutan sopan/hormat untuk ibu orang lain atau panggilan langsung di rumah).",
            "ちち (Chichi - sebutan rendah hati yang khusus digunakan untuk ayah kandung sendiri).",
            "おばあさん (Obaasan - sebutan hormat untuk nenek atau wanita lanjut usia).",
            "あね (Ane - sebutan rendah hati untuk kakak perempuan kandung sendiri)."
        ],
        "formula": {
            "title": "SEBUTAN KELUARGA SENDIRI VS ORANG LAIN (内と外の家族呼称)",
            "latex": "\\begin{aligned} \\text{Keluarga Sendiri (Uchi): } & \\mathbf{\\text{母 (はは - Haha)}} \\quad / \\quad \\text{父 (ちち - Chichi)} \\\\ \\text{Orang Lain (Soto): } & \\text{お母さん (おかあさん)} \\quad / \\quad \\text{お父さん (おとうさん)} \\end{aligned}",
            "legend": "• Konsep Uchi-Soto: Menyebut keluarga sendiri kepada orang luar wajib memakai bentuk netral/rendah hati"
        },
        "hints": {
            "concept": "Menyebut ibu sendiri kepada orang lain menggunakan kanji 母 yang dibaca 'はは' (haha), bukan 'おかあさん'.",
            "execution": "Pilih opsi: 'はは (Haha)'."
        }
    },
    {
        "id": "jpn-lat-e-05",
        "materi": "MOJIGOI: KATA BENDA & KOSAKATA N5",
        "topic": "Klasifikasi Benda di Sekolah dan Ruang Belajar",
        "stem": "Bacalah kalimat rumpang berikut:\n'せんせいは こくばんに しろい ( ... ) で 字を 書きました。'\nKosakata alat tulis yang PALING LOGIS untuk melengkapi kalimat di atas adalah...",
        "correct": "チョーク (Chooku - kapur tulis yang digunakan untuk menulis pada papan tulis hitam / kokuban).",
        "distractors": [
            "はさみ (Hasami - gunting yang digunakan untuk memotong kertas kerajinan).",
            "ホッチキス (Hotchikisu - staples penjilid lembaran dokumen tugas sekolah).",
            "けしゴム (Keshigomu - karet penghapus tulisan pensil pada buku catatan siswa).",
            "じょうぎ (Jougi - penggaris yang dipakai untuk mengukur dan menarik garis lurus)."
        ],
        "formula": {
            "title": "ALAT TULIS PAPAN KOKUBAN (文房具の機能)",
            "latex": "\\text{こくばん (Papan Tulis Hitam)} + \\text{しろい (Putih)} + \\text{書く (Menulis)} \\implies \\mathbf{\\text{チョーク (Chooku)}}",
            "legend": "• Asosiasi semantik media papan tulis dan sarana penulisan"
        },
        "hints": {
            "concept": "Menulis pada 'kokuban' (papan tulis hitam) dengan warna 'shiroi' (putih) alatnya adalah kapur tulis (チョーク).",
            "execution": "Pilih opsi: 'チョーク'."
        }
    },
    {
        "id": "jpn-lat-e-06",
        "materi": "MOJIGOI: KATA SIFAT N5",
        "topic": "Pasangan Antonim Kata Sifat-i (大きい vs 小さい, 高い vs 低い/安い)",
        "stem": "Perhatikan dialog singkat berikut:\nTanaka: 'この シャツは とても [たかい] ですね。'\nKen: 'いいえ、そんなに たかくないですよ。あそこの 店のほうが もっと [ ... ] です。'\nKata sifat antonim dari 'たかい' (mahal) untuk melengkapi pernyataan Ken adalah...",
        "correct": "やすい (Yasui - murah dari segi harga barang di toko).",
        "distractors": [
            "ひくい (Hikui - rendah dari segi ukuran tinggi fisik permukaan atau postur).",
            "ちいさい (Chiisai - kecil dari segi volume atau dimensi ukuran benda pakaian).",
            "ふるい (Furui - usang atau tua dari segi usia pemakaian barang).",
            "おもい (Omoi - berat dari segi timbangan massa benda pakaian)."
        ],
        "formula": {
            "title": "ANTONIM KATA SIFAT-I (対義語)",
            "latex": "\\text{高い (たかい - Mahal)} \\quad \\longleftrightarrow \\quad \\mathbf{\\text{安い (やすい - Murah)}}",
            "legend": "• Takai memiliki dua makna: tinggi (lawannya hikui) dan mahal (lawannya yasui)"
        },
        "hints": {
            "concept": "Konteks kalimat membahas harga pakaian di toko. Lawan kata 'takai' (mahal) adalah 'yasui' (murah).",
            "execution": "Pilih: 'やすい (Yasui)'."
        }
    },
    {
        "id": "jpn-lat-e-07",
        "materi": "MOJIGOI: KATA KERJA N5",
        "topic": "Pasangan Kata Kerja Transitif Keseharian (食べる, 飲む, 見る, 聞く)",
        "stem": "Lengkapilah kalimat berikut dengan kata kerja bentuk -masu yang TEPAT:\n'毎晩 ねる まえに、へやで お気に入りの おんがくを ( ... )。'",
        "correct": "ききます (Kikimasu - mendengarkan musik kegemaran dengan seksama).",
        "distractors": [
            "みます (Mimasu - menonton tayangan visual seperti film atau televisi).",
            "よみます (Yomimasu - membaca bahan literatur berupa buku, novel, atau koran).",
            "かきます (Kakimasu - menulis teks catatan atau menggambar ilustrasi grafis).",
            "はなします (Hanashimasu - berbicara atau berkomunikasi lisan dengan mitra bicara)."
        ],
        "formula": {
            "title": "KOLOKASI OBJEK & VERBA (目的語と動詞の共起関係)",
            "latex": "\\text{おんがく (Musik)} + \\text{を (Partikel Objek)} \\implies \\mathbf{\\text{ききます (Kikimasu / Mendengarkan)}}",
            "legend": "• Kolokasi tetap antara media audio (ongaku) dan indra pendengaran"
        },
        "hints": {
            "concept": "Objek kalimat adalah 'ongaku' (musik). Kata kerja yang berpasangan secara alami adalah 'kikimasu' (mendengarkan).",
            "execution": "Pilih: 'ききます (Kikimasu)'."
        }
    },
    {
        "id": "jpn-lat-e-08",
        "materi": "MOJIGOI: KATA BANTU BILANGAN (JOSHI)",
        "topic": "Penghitungan Benda Tipis/Kertas (枚 - Mai)",
        "stem": "Ketika membeli tiket kereta api atau memesan lembaran kertas, kata bantu bilangan (*josuushi*) yang WAJIB digunakan untuk menghitung benda tipis dan rata adalah...",
        "correct": "まい (Mai - satuan hitung khusus untuk benda lembaran tipis seperti kertas, baju, piring, dan tiket).",
        "distractors": [
            "ほん / ぽん (Hon/Pon - satuan hitung untuk benda berbentuk silindris panjang seperti pensil dan botol).",
            "さつ (Satsu - satuan hitung untuk buku berukuran tebal atau jilidan majalah).",
            "だい (Dai - satuan hitung untuk mesin mekanik, kendaraan bermotor, atau alat elektronik).",
            "ひき / ぴき (Hiki/Piki - satuan hitung untuk hewan berkaki empat berukuran kecil atau ikan)."
        ],
        "formula": {
            "title": "SATUAN HITUNG JEPANG (助数詞)",
            "latex": "\\text{Kertas / Tiket / Piring / Baju (Tipis Rata)} \\implies \\mathbf{\\text{~枚 (~まい / Mai)}}",
            "legend": "• Kategori bentuk fisik menentukan morfem pembilang yang melekat pada angka"
        },
        "hints": {
            "concept": "Benda pipih, tipis, dan rata (kertas, tiket, prangko, piring) dihitung menggunakan 'mai' (枚).",
            "execution": "Pilih: 'まい (Mai)'."
        }
    },
    {
        "id": "jpn-lat-e-09",
        "materi": "MOJIGOI: KOSAKATA CUACA & MUSIM N5",
        "topic": "Empat Musim di Jepang (春, 夏, 秋, 冬)",
        "stem": "Bacalah deskripsi fenomena alam berikut:\n'日本では 4月に さくらが さきます。暖かくなって、新学期が はじまります。'\nMusim yang digambarkan dalam kalimat di atas adalah...",
        "correct": "はる (Haru - musim semi yang identik dengan mekarnya bunga sakura dan dimulainya tahun ajaran baru).",
        "distractors": [
            "なつ (Natsu - musim panas yang ditandai dengan suhu terik dan liburan pantai).",
            "あき (Aki - musim gugur yang ditandai dengan perubahan daun memerah / koyo).",
            "ふゆ (Fuyu - musim dingin yang bersuhu beku dan diwarnai hujan salju lebat).",
            "つゆ (Tsuyu - musim hujan musiman yang berlangsung antara akhir musim semi dan awal musim panas)."
        ],
        "formula": {
            "title": "EMPAT MUSIM JEPANG (日本の四季)",
            "latex": "\\text{4月 (April)} + \\text{さくら (Sakura Mekar)} + \\text{あたたかい (Hangat)} \\implies \\mathbf{\\text{春 (はる - Haru)}}",
            "legend": "• Kalender tahun ajaran dan tahun fiskal Jepang resmi bermula di musim semi (April)"
        },
        "hints": {
            "concept": "Bunga sakura mekar dan udara mulai hangat pada bulan April adalah ciri khas musim semi: 'はる' (haru).",
            "execution": "Pilih: 'はる (Haru)'."
        }
    },
    {
        "id": "jpn-lat-e-10",
        "materi": "MOJIGOI: KATA GANTI PENUNJUK KO-SO-A-DO",
        "topic": "Sistem Demonstrativa Ruang (これ, それ, あれ, どれ)",
        "stem": "Seseorang sedang memegang sebuah buku di tangannya dan ingin bertanya kepada rekannya tentang isi buku tersebut. Kata tunjuk benda yang TEPAT digunakan oleh pembicara tersebut adalah...",
        "correct": "これ (Kore - kata tunjuk benda yang berada di area jangkauan tangan pembicara sendiri).",
        "distractors": [
            "それ (Sore - kata tunjuk benda yang berada di dekat lawan bicara).",
            "あれ (Are - kata tunjuk benda yang letaknya jauh dari pembicara maupun lawan bicara).",
            "どれ (Dore - kata tanya penunjuk pilihan di antara beberapa alternatif benda).",
            "どこ (Doko - kata tanya penunjuk lokasi tempat keberadaan suatu entitas)."
        ],
        "formula": {
            "title": "SISTEM DEMONSTRATIVA KO-SO-A-DO (指示語体系)",
            "latex": "\\begin{aligned} \\mathbf{\\text{これ (Kore)}} & \\implies \\text{Dekat Pembicara (Ko)} \\\\ \\text{それ (Sore)} & \\implies \\text{Dekat Lawan Bicara (So)} \\\\ \\text{あれ (Are)} & \\implies \\text{Jauh dari Keduanya (A)} \\end{aligned}",
            "legend": "• Pembagian zona kedekatan fisik dalam pragmatik percakapan bahasa Jepang"
        },
        "hints": {
            "concept": "Benda berada di tangan pembicara sendiri (zona 'ko-'), sehingga kata tunjuk benda yang tepat adalah 'これ' (kore).",
            "execution": "Pilih: 'これ (Kore)'."
        }
    },
    {
        "id": "jpn-lat-e-11",
        "materi": "BUNPOU: PARTIKEL DASAR N5",
        "topic": "Fungsi Partikel Penanda Topik (は) dan Penanda Objek (を)",
        "stem": "Lengkapilah kalimat rumpang berikut dengan partikel yang TEPAT:\n'わたし [ ... ] 毎朝 りんご [ ... ] たべます。'",
        "correct": "は (wa) sebagai penanda topik kalimat, dan を (wo/o) sebagai penanda objek penderita verba transitif.",
        "distractors": [
            "が (ga) sebagai penanda subjek fokus, dan に (ni) sebagai penanda titik waktu atau target.",
            "を (wo) sebagai penanda objek langsung, dan で (de) sebagai penanda sarana alat makan.",
            "に (ni) sebagai penanda arah tujuan gerak, dan は (wa) sebagai penanda pembanding latar.",
            "で (de) sebagai penanda tempat peristiwa, dan と (to) sebagai penanda kesertaan rekan."
        ],
        "formula": {
            "title": "STRUKTUR DASAR SOV (基本文型)",
            "latex": "\\mathbf{S \\text{ は }} + \\mathbf{O \\text{ を }} + \\mathbf{V \\text{ ます}} \\implies \\text{わたし } \\mathbf{\\text{は}} \\text{ りんご } \\mathbf{\\text{を}} \\text{ たべます}",
            "legend": "• は menandai topik pembicaraan; を menandai objek langsung yang menerima aksi"
        },
        "hints": {
            "concept": "Topik pembicaraan ('watashi') ditandai partikel は (wa). Objek makanan ('ringo') ditandai partikel を (o/wo).",
            "execution": "Pilih opsi dengan pasangan: は (wa) dan を (wo)."
        }
    },
    {
        "id": "jpn-lat-e-12",
        "materi": "BUNPOU: PARTIKEL DASAR N5",
        "topic": "Fungsi Partikel Penanda Sarana Alat dan Tempat Aktivitas (で)",
        "stem": "Perhatikan kalimat rumpang berikut:\n'スピーチコンテストの 原稿を パソコン ( ... ) 作りました。'\nPartikel yang TEPAT untuk mengisi rumpang yang menyatakan sarana/alat teknologi pembuatan naskah adalah...",
        "correct": "で (de - partikel yang berfungsi menandai alat, sarana instrumen, atau metode kerja).",
        "distractors": [
            "に (ni - partikel penanda waktu spesifik atau sasaran tujuan perpindahan).",
            "へ (e - partikel penanda arah pergerakan menuju destinasi geografis).",
            "を (wo - partikel penanda objek penderita langsung verba transitif).",
            "から (kara - partikel penanda titik awal waktu atau tempat keberangkatan)."
        ],
        "formula": {
            "title": "PARTIKEL SARANA / ALAT (手段・道具の「で」)",
            "latex": "\\text{パソコン (Komputer/Laptop)} + \\mathbf{\\text{で (de)}} + \\text{作りました (Membuat)}",
            "legend": "• で menandai piranti/metode yang digunakan subjek untuk mengeksekusi perbuatan"
        },
        "hints": {
            "concept": "Menyatakan sarana, alat, atau kendaraan yang digunakan melakukan perbuatan menggunakan partikel で (de).",
            "execution": "Pilih: 'で (de)'."
        }
    },
    {
        "id": "jpn-lat-e-13",
        "materi": "BUNPOU: PARTIKEL DASAR N5",
        "topic": "Fungsi Partikel Titik Waktu Spesifik (に) vs Tanpa Partikel",
        "stem": "Dalam kaidah tata bahasa Jepang, kata penunjuk waktu manakah di bawah ini yang WAJIB diikuti oleh partikel titik waktu 'に' (ni)?",
        "correct": "「日曜日」 (Nichiyoubi - nama hari dalam sepekan merupakan titik waktu terukur pasti yang memerlukan partikel に).",
        "distractors": [
            "「きょう」 (Kyou - kata penunjuk waktu relatif hari ini tidak boleh dilekatkan partikel に).",
            "「あした」 (Ashita - kata penunjuk waktu relatif besok tidak boleh menggunakan partikel に).",
            "「きのう」 (Kinou - penunjuk waktu relatif kemarin yang berfungsi langsung sebagai kata keterangan nomina).",
            "「まいあさ」 (Maiasa - penunjuk frekuensi rutin setiap pagi yang tidak memakai partikel に)."
        ],
        "formula": {
            "title": "REGULASI PENGGUNAAN PARTIKEL に PADA WAKTU",
            "latex": "\\begin{cases} \\mathbf{\\text{Pakai に:}} & \\text{Hari (日曜日), Jam (7時), Tanggal (15日), Bulan (4月)} \\\\ \\mathbf{\\text{Tanpa に:}} & \\text{Waktu Relatif (きょう, あした, きのう, まいにち, いま)} \\end{cases}",
            "legend": "• Titik waktu kalenderis/angka berpatokan memerlukan に; waktu relatif tidak memerlukan に"
        },
        "hints": {
            "concept": "Nama hari (Nichiyoubi) atau waktu berangka pasti memerlukan partikel に. Waktu relatif seperti kyou/ashita tidak memakai に.",
            "execution": "Pilih opsi: '「日曜日」'."
        }
    },
    {
        "id": "jpn-lat-e-14",
        "materi": "BUNPOU: PARTIKEL DASAR N5",
        "topic": "Fungsi Partikel Penanda Arah Tujuan Gerak (へ / に)",
        "stem": "Lengkapilah kalimat pergerakan fisik berikut dengan partikel yang BENAR:\n'らいしゅうの 土曜日に 家族と 一緒に きょうと ( ... ) 行きます。'",
        "correct": "へ (e - partikel yang ditulis dengan hiragana 'he' namun dilafalkan 'e' untuk menandai arah destinasi perjalanan).",
        "distractors": [
            "で (de - keliru karena de menandai tempat terjadinya aksi aktif, bukan tujuan perpindahan).",
            "を (wo - penanda objek langsung yang tidak berpasangan dengan verba intransitif ikimasu).",
            "が (ga - penanda subjek gramatikal yang tidak tepat mengisi posisi destinasi kota).",
            "と (to - penanda hubungan kesertaan yang sudah terwakili pada frasa kazoku to)."
        ],
        "formula": {
            "title": "PARTIKEL DESTINASI PERPINDAHAN (移動動詞の方向格)",
            "latex": "\\text{きょうと (Kyoto)} + \\mathbf{\\text{へ / に}} + \\text{行きます (Pergi)}",
            "legend": "• Ditulis dengan karakter へ (he) tetapi dilafalkan sebagai fonem 'e' saat berfungsi partikel arah"
        },
        "hints": {
            "concept": "Verba gerak seperti 行きます (ikimasu) mengambil partikel arah へ (e) atau partikel target に (ni).",
            "execution": "Pilih opsi: 'へ (e)'."
        }
    },
    {
        "id": "jpn-lat-e-15",
        "materi": "BUNPOU: KONJUGASI VERBA N5",
        "topic": "Pembentukan Bentuk Negatif Lampau Masendeshita (~ませんでした)",
        "stem": "Bentuk negatif lampau yang TEPAT dari verba 'たべます' (makan) untuk menyatakan bahwa subjek tidak makan apa pun kemarin malam adalah...",
        "correct": "たべませんでした (Tabemasendeshita - bentuk sopan negatif untuk peristiwa lampau).",
        "distractors": [
            "たべません (Tabemasen - bentuk sopan negatif untuk waktu sekarang/kebiasaan masa depan).",
            "たべました (Tabemashita - bentuk sopan positif untuk peristiwa masa lampau).",
            "たべないでした (Tabenaideshita - konstruksi bahasa percakapan informal yang tidak baku dalam ragam sopan).",
            "たべなかったです (Tabenakattadesu - bentuk pergaulan kasual yang dilekati kopula desu)."
        ],
        "formula": {
            "title": "KONJUGASI BENTUK MASU (ます形の時制・極性変化)",
            "latex": "\\begin{array}{|c|c|c|} \\hline & \\text{Non-Lampau} & \\text{Lampau} \\\\ \\hline \\text{Positif} & \\text{~ます} & \\text{~ました} \\\\ \\hline \\text{Negatif} & \\text{~ません} & \\mathbf{\\text{~ませんでした}} \\\\ \\hline \\end{array}",
            "legend": "• Standar pembentukan ragam sopan formal (Teineigo) dasar"
        },
        "hints": {
            "concept": "Negatif lampau bentuk sopan (~masu) adalah ~ませんでした (~masendeshita).",
            "execution": "Pilih: 'たべませんでした'."
        }
    },
    {
        "id": "jpn-lat-e-16",
        "materi": "BUNPOU: KONJUGASI VERBA N5",
        "topic": "Pembentukan Bentuk Te (て形) Verba Golongan I (Godan Doushi)",
        "stem": "Verba 'かきます' (menulis / Kakimasu) termasuk dalam kata kerja Golongan I (akhiran bunyi -ki). Bagaimanakah perubahan bentuk -te (te-kei) yang BENAR dari verba tersebut?",
        "correct": "かいて (Kaite - bunyi ki meluruh menjadi i diikuti te: ki -> ite).",
        "distractors": [
            "かきて (Kakite - tidak mengalami peluruhan fonologis onbin yang diwajibkan kaidah).",
            "かって (Katte - perubahan sokuonbin untuk verba berakhiran -chi, -ri, atau -i).",
            "かんで (Kande - perubahan hatsuonbin untuk verba berakhiran -mi, -bi, atau -ni).",
            "かいで (Kaide - perubahan dakuon untuk verba berakhiran -gi seperti oyogimasu -> oyoide)."
        ],
        "formula": {
            "title": "KAIDAH ONBIN VERBA GOLONGAN I (イ音便の規則)",
            "latex": "\\text{Verba akhiran } [\\text{〜きます}] \\xrightarrow{\\text{Te-form}} \\mathbf{\\text{〜いて (ite)}} \\quad (\\text{かきます } \\to \\mathbf{\\text{かいて}})",
            "legend": "• Pengecualian mutlak: 行きます (ikimasu) berubah menjadi 行って (itte)"
        },
        "hints": {
            "concept": "Kata kerja Golongan 1 berakhiran 'kimasu' (seperti kakimasu) berubah menjadi 'ite' -> かいて (kaite).",
            "execution": "Pilih: 'かいて (Kaite)'."
        }
    },
    {
        "id": "jpn-lat-e-17",
        "materi": "BUNPOU: POLA KALIMAT N5",
        "topic": "Permohonan Halus Bentuk Te Kudasai (〜てください)",
        "stem": "Guru di kelas ingin meminta para siswa membuka buku halaman 20 dengan sopan. Kalimat permohonan yang TEPAT adalah...",
        "correct": "教科書の 20ページを あけてください。 (Kyoukasho no nijuu peeji wo akete kudasai - silakan buka buku paket halaman 20).",
        "distractors": [
            "教科書の 20ページを あけないでください。 (Permohonan negatif yang berarti meminta agar jangan membuka buku).",
            "教科書の 20ページを あけてはいけません。 (Ungkapan larangan tegas yang berarti tidak boleh membuka buku).",
            "教科書の 20ページを あけてもいいです。 (Pemberian izin yang berarti boleh membuka buku paket).",
            "教科書の 20ページを あけます。 (Pernyataan diri sendiri bahwa pembicara yang akan membuka buku)."
        ],
        "formula": {
            "title": "POLA PERMOHONAN SOPAN (依頼表現)",
            "latex": "\\mathbf{V\\text{-て形}} + \\mathbf{\\text{ください}} \\implies \\text{Silakan / Tolong lakukan } V",
            "legend": "• Menunjukkan instruksi atau permintaan tolong bernada santun"
        },
        "hints": {
            "concept": "Pola meminta tolong/instruksi santun adalah V-te + kudasai (あけてください).",
            "execution": "Pilih opsi: '教科書の 20ページを あけてください。'."
        }
    },
    {
        "id": "jpn-lat-e-18",
        "materi": "BUNPOU: POLA KALIMAT N5",
        "topic": "Menyatakan Keberadaan Benda Mati vs Makhluk Hidup (あります vs います)",
        "stem": "Perhatikan dua kalimat keberadaan berikut:\n1) きょうしつに 机と いすが ( A )。\n2) にわに かわいい いぬが ( B )。\nKata kerja keberadaan yang TEPAT untuk mengisi posisi ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: あります (benda mati/tidak bergerak), B: います (makhluk hidup/bernyawa).",
        "distractors": [
            "A: います (makhluk hidup), B: あります (benda mati).",
            "A: あります, B: あります (kedua entitas disamakan sebagai benda mati tanpa pembedaan biologis).",
            "A: います, B: います (kedua entitas disamakan sebagai makhluk hidup bernyawa).",
            "A: ありません, B: いません (bentuk peniadaan yang bertentangan dengan konteks afirmasi)."
        ],
        "formula": {
            "title": "DISTINGSI EKSISTENSIAL (存在動詞の区別)",
            "latex": "\\begin{cases} \\mathbf{\\text{あります (Arimasu)}} & \\implies \\text{Benda Mati / Tumbuhan / Konsep Abstrak} \\\\ \\mathbf{\\text{います (Imasu)}} & \\implies \\text{Manusia / Hewan (Bergerak Mandiri)} \\end{cases}",
            "legend": "• Pembedaan fundamental bahasa Jepang atas entitas bernyawa versus tak bernyawa"
        },
        "hints": {
            "concept": "Meja/kursi (benda mati) menggunakan あります (arimasu). Anjing (hewan bernyawa) menggunakan います (imasu).",
            "execution": "Pilih: 'A: あります, B: います'."
        }
    },
    {
        "id": "jpn-lat-e-19",
        "materi": "BUNPOU: POLA KALIMAT N5",
        "topic": "Menyatakan Keinginan Pribadi Bentuk Tai (〜たいです)",
        "stem": "Ketika seseorang merasa sangat haus setelah berolahraga di siang hari, ungkapan keinginan pribadi yang TEPAT diucapkannya adalah...",
        "correct": "冷たい 水が 飲みたいです。 (Tsumetai mizu ga nomitaidesu - saya ingin minum air dingin).",
        "distractors": [
            "冷たい 水を 飲まないです。 (Pernyataan negatif biasa bahwa pembicara tidak minum air dingin).",
            "冷たい 水を 飲んでください。 (Permintaan kepada orang lain untuk meminum air dingin tersebut).",
            "冷たい 水を 飲んでもいいです。 (Pemberian izin kepada pihak lain untuk meminum air dingin).",
            "冷たい 水を 飲みましょう。 (Ajakan bersama untuk meminum air dingin secara kolektif)."
        ],
        "formula": {
            "title": "POLA KEINGINAN SUBJEK ORANG PERTAMA (願望表現)",
            "latex": "\\mathbf{V\\text{-ます形 (Coret ます)}} + \\mathbf{\\text{たいです}} \\implies \\text{Ingin melakukan } V",
            "legend": "• Objek verba pada pola ~tai dapat ditandai dengan partikel が (ga) atau を (wo)"
        },
        "hints": {
            "concept": "Menyatakan keinginan sendiri melakukan aktivitas menggunakan verba bentuk ~たいです (nomitaidesu).",
            "execution": "Pilih: '冷たい 水が 飲みたいです。'."
        }
    },
    {
        "id": "jpn-lat-e-20",
        "materi": "BUNPOU: POLA KALIMAT N5",
        "topic": "Pola Ajakan Bersama Mashou (〜ましょう / 〜ましょうか)",
        "stem": "Dua orang sahabat sedang kelelahan setelah berjalan kaki cukup jauh. Salah satu dari mereka ingin mengajak beristirahat sebentar di bawah pohon rindang. Kalimat ajakan yang TEPAT adalah...",
        "correct": "あそこで 少し やすみましょう。 (Asoko de sukoshi yasumimashou - mari kita beristirahat sebentar di sana).",
        "distractors": [
            "あそこで 少し やすみます。 (Pernyataan deklaratif tunggal bahwa dirinya sendiri akan beristirahat).",
            "あそこで 少し やすんでください。 (Perintah atau permohonan sepihak kepada lawan bicara untuk beristirahat).",
            "あそこで 少し やすみません。 (Pernyataan negatif bahwa mereka tidak akan beristirahat di tempat itu).",
            "あそこで 少し やすみたいです。 (Ungkapan keinginan pribadi tanpa ada unsur mengajak lawan bicara secara inklusif)."
        ],
        "formula": {
            "title": "POLA AJAKAN INKLUSIF (勧誘表現)",
            "latex": "\\mathbf{V\\text{-ます形 (Coret ます)}} + \\mathbf{\\text{ましょう}} \\implies \\text{Mari kita } V \\text{ bersama-sama}",
            "legend": "• Mengandung ajakan tegas dan bersahabat kepada mitra tutur"
        },
        "hints": {
            "concept": "Ajakan bersama 'mari kita...' menggunakan bentuk ~ましょう (yasumimashou).",
            "execution": "Pilih opsi: 'あそこで 少し やすみましょう。'."
        }
    },
    {
        "id": "jpn-lat-e-21",
        "materi": "AISATSU & BUDAYA: SALAM HARIAN",
        "topic": "Etika Salam Pertemuan Pagi Hari (おはようございます)",
        "stem": "Saat seorang siswa berpapasan dengan kepala sekolah di koridor sekolah pada pukul 07.15 pagi, ungkapan salam yang WAJIB diucapkan secara sopan dan beretika adalah...",
        "correct": "おはようございます (Ohayou gozaimasu - salam selamat pagi formal yang wajib digunakan kepada pihak yang dihormati).",
        "distractors": [
            "おはよう (Ohayou - salam pagi bentuk kasual yang hanya boleh ditujukan kepada teman sebaya atau bawahan).",
            "こんにちは (Konnichiwa - salam selamat siang yang lazim digunakan mulai pukul 10.30 pagi ke atas).",
            "こんばんは (Konbanwa - salam selamat petang/malam hari saat matahari telah tenggelam).",
            "おやすみなさい (Oyasuminasai - ucapan selamat beristirahat yang diucapkan menjelang tidur)."
        ],
        "formula": {
            "title": "REGISTER KESOPANAN SALAM (挨拶の敬体・簡体)",
            "latex": "\\begin{aligned} \\text{Formal (Kepada Guru / Atasan): } & \\mathbf{\\text{おはようございます}} \\\\ \\text{Kasual (Kepada Teman Akrab): } & \\text{おはよう} \\end{aligned}",
            "legend": "• Menjaga prinsip kesantunan vertikal dalam hubungan hierarkis di sekolah dan kantor"
        },
        "hints": {
            "concept": "Bertegur sapa di pagi hari dengan pihak yang dihormati (kepala sekolah) wajib menggunakan bentuk lengkap sopan: 'おはようございます'.",
            "execution": "Pilih: 'おはようございます (Ohayou gozaimasu)'."
        }
    },
    {
        "id": "jpn-lat-e-22",
        "materi": "AISATSU & BUDAYA: ETIKA MAKAN",
        "topic": "Ucapan Sakral Sebelum dan Sesudah Makan (いただきます & ごちそうさまでした)",
        "stem": "Di Jepang, sebelum menyantap makanan yang telah dihidangkan, setiap orang merapatkan kedua telapak tangan di dada sembari mengucapkan ungkapan rasa syukur dan penghormatan kepada bahan makanan serta juru masak, yaitu...",
        "correct": "いただきます (Itadakimasu - secara harfiah bermakna menerima berkah hidangan dengan kerendahan hati).",
        "distractors": [
            "ごちそうさまでした (Gochisousama deshita - ucapan rasa terima kasih yang diucapkan sesudah menyelesaikan santapan).",
            "いってきます (Ittekimasu - ucapan pamit saat hendak melangkah keluar meninggalkan rumah).",
            "ただいま (Tadaima - ungkapan pemberitahuan bahwa diri sendiri telah kembali tiba di rumah).",
            "おじゃまします (Ojamashimasu - ungkapan permisi saat memasuki rumah atau kediaman orang lain)."
        ],
        "formula": {
            "title": "UNGKAPAN ETIKA BERSANTAP (食事の作法)",
            "latex": "\\text{Sebelum Makan: } \\mathbf{\\text{いただきます}} \\quad \\longleftrightarrow \\quad \\text{Sesudah Makan: } \\text{ごちそうさまでした}",
            "legend": "• Merefleksikan filosofi syukur Shinto-Buddhis atas pengorbanan alam dan jerih payah juru masak"
        },
        "hints": {
            "concept": "Sebelum makan mengucapkan 'いただきます' (Itadakimasu). Sesudah makan mengucapkan 'ごちそうさまでした' (Gochisousama deshita).",
            "execution": "Pilih: 'いただきます (Itadakimasu)'."
        }
    },
    {
        "id": "jpn-lat-e-23",
        "materi": "AISATSU & BUDAYA: PERJALANAN RUMAH",
        "topic": "Pasangan Salam Keberangkatan dan Kepulangan Rumah",
        "stem": "Ketika seorang anak hendak berangkat ke sekolah, ia mengucapkan 'いってきます' (Ittekimasu). Jawaban balasan yang TEPAT dan lumrah diucapkan oleh orang tua yang berada di rumah adalah...",
        "correct": "いってらっしゃい (Itterasshai - ucapan selamat jalan dan doa agar kembali dengan selamat).",
        "distractors": [
            "おかえりなさい (Okaerinasai - ucapan sambutan selamat datang kembali saat seseorang tiba di rumah).",
            "おつかれさまでした (Otsukaresama deshita - ucapan apresiasi atas kerja keras rekan kerja sesudah beraktivitas).",
            "おげんきですか (Ogenki desu ka - kalimat menanyakan kabar kesehatan seseorang saat lama tak berjumpa).",
            "さようなら (Sayounara - salam perpisahan berjarak yang jarang diucapkan di dalam internal rumah keluarga)."
        ],
        "formula": {
            "title": "PASANGAN UNGKAPAN RUMAH TANGGA (出立と帰宅の挨拶)",
            "latex": "\\begin{aligned} \\text{Orang Berangkat: } \\text{いってきます} & \\longleftrightarrow \\mathbf{\\text{いってらっしゃい (Orang di Rumah)}} \\\\ \\text{Orang Pulang: } \\text{ただいま} & \\longleftrightarrow \\text{おかえりなさい (Orang di Rumah)} \\end{aligned}",
            "legend": "• Menunjukkan keharmonisan komunikasi sosial harian dalam keluarga Jepang"
        },
        "hints": {
            "concept": "Pasangan dari 'いってきます' (Ittekimasu) bagi yang melepas di rumah adalah 'いってらっしゃい' (Itterasshai).",
            "execution": "Pilih: 'いってらっしゃい (Itterasshai)'."
        }
    },
    {
        "id": "jpn-lat-e-24",
        "materi": "AISATSU & BUDAYA: MEMINTA MAAF & PERMISI",
        "topic": "Distingsi Sumimasen (すみません) vs Gomennasai (ごめんなさい)",
        "stem": "Di dalam gerbong kereta yang padat, seorang penumpang tidak sengaja menyenggol bahu penumpang lain dan ingin meminta maaf sekaligus permisi untuk bergeser menuju pintu keluar. Kata yang PALING TEPAT dan lazim dalam norma sosial publik adalah...",
        "correct": "すみません (Sumimasen - permohonan maaf sopan sekaligus serbaguna untuk menarik perhatian atau meminta permisi di ruang publik).",
        "distractors": [
            "ごめんなさい (Gomennasai - ungkapan minta maaf emosional yang lazimnya terbatas pada pergaulan keluarga atau teman akrab).",
            "どういたしまして (Douitashimashite - balasan berupa ucapan terima kasih kembali / sama-sama).",
            "しつれいしました (Shitsurei shimashita - bentuk lampau kaku yang biasanya dipakai sesudah selesai rapat formal kantor).",
            "おめでとうございます (Omedetou gozaimasu - ucapan selamat atas pencapaian prestasi atau peristiwa membahagiakan)."
        ],
        "formula": {
            "title": "PRAGMATIK KATA SUMIMASEN (「すみません」の多機能性)",
            "latex": "\\mathbf{\\text{すみません}} = \\begin{cases} \\text{1. Maaf (Kesalahan kecil / Khilaf)} \\\\ \\text{2. Permisi (Memotong jalan / Memanggil pelayan)} \\\\ \\text{3. Terima kasih (Merepotkan orang lain)} \\end{cases}",
            "legend": "• Kata kunci utama interaksi publik di Jepang yang bernilai kesantunan tinggi"
        },
        "hints": {
            "concept": "Di ruang umum kepada orang tak dikenal, kata minta maaf dan permisi yang paling tepat adalah 'すみません' (Sumimasen).",
            "execution": "Pilih: 'すみません (Sumimasen)'."
        }
    },
    {
        "id": "jpn-lat-e-25",
        "materi": "AISATSU & BUDAYA: ETIKA MEMBUNGKUK (OJIGI)",
        "topic": "Tiga Derajat Sudut Membungkuk Tradisional (Eshaku, Keirei, Saikeirei)",
        "stem": "Dalam etika budaya Jepang, gerakan membungkukkan badan (*Ojigi*) memiliki tingkatan sudut kemiringan sesuai bobot rasa hormat. Gerakan membungkuk ringan dengan sudut kemiringan sekitar 15 derajat yang digunakan saat berpapasan dengan rekan sejawat disebut...",
        "correct": "会釈 (Eshaku - salam bungkuk ringan bersudut sekitar 15 derajat untuk sapaan santai sehari-hari).",
        "distractors": [
            "敬礼 (Keirei - salam bungkuk standar bersudut sekitar 30 derajat untuk menyapa atasan, guru, atau klien bisnis).",
            "最敬礼 (Saikeirei - salam bungkuk rasa hormat tertinggi bersudut 45 derajat untuk memohon maaf mendalam atau upacara sakral).",
            "正座 (Seiza - posisi duduk bersimpuh formal dengan melipat kedua kaki di atas tatami).",
            "土下座 (Dogeza - posisi bersujud hingga kepala menyentuh lantai sebagai bentuk penyesalan luar biasa)."
        ],
        "formula": {
            "title": "KLASIFIKASI SUDUT MEMBUNGKUK JEPANG (お辞儀の種類)",
            "latex": "\\begin{aligned} \\mathbf{\\text{会釈 (Eshaku)}} & \\approx 15^\\circ \\quad (\\text{Sapaan Ringan / Teman Sejawat}) \\\\ \\text{敬礼 (Keirei)} & \\approx 30^\\circ \\quad (\\text{Hormat Standar / Tamu / Atasan}) \\\\ \\text{最敬礼 (Saikeirei)} & \\approx 45^\\circ \\quad (\\text{Hormat Tertinggi / Minta Maaf Serius}) \\end{aligned}",
            "legend": "• Standar etika gestur raga dalam komunikasi nonverbal bangsa Jepang"
        },
        "hints": {
            "concept": "Membungkuk 15 derajat untuk sapaan ringan disebut 会釈 (Eshaku). 30 derajat Keirei, 45 derajat Saikeirei.",
            "execution": "Pilih opsi: '会釈 (Eshaku)'."
        }
    }
]
