# -*- coding: utf-8 -*-
"""
BAHASA JEPANG - PAKET SOAL LATIHAN MENENGAH (MEDIUM) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / JLPT N4
Distribusi:
- 8 Butir: Kanji & Kosakata N4 (Jukugo, pasangan verba transitif/intransitif Jidoushi-Tadoushi)
- 10 Butir: Tata Bahasa Menengah (Bunpou N4: ~tara, ~ba, ~to, ~nara, ~sou da, ~you da, kanou-kei, te-shimau, te-oku)
- 7 Butir: Wacana Dokkai & Pemahaman Tekstual N4 (Pengumuman, surel, memo, jadwal kegiatan)
"""

BAHASA_JEPANG_MEDIUM_ITEMS = [
    {
        "id": "jpn-lat-m-01",
        "materi": "MOJIGOI: KANJI N4 & JUKUGO",
        "topic": "Pasangan Verba Transitif vs Intransitif (他動詞と自動詞: 開ける vs 開く)",
        "stem": "Perhatikan dua kalimat berikut ini:\n1) かぜが つよいので、窓が ( A ) ました。\n2) へやの くうきを かえるために、窓を ( B ) ました。\nKata kerja yang TEPAT untuk mengisi posisi ( A ) yang bersifat intransitif (*jidoushi*) dan ( B ) yang bersifat transitif (*tadoushi*) berturut-turut adalah...",
        "correct": "A: あき (aki / terbuka sendiri), B: あけ (ake / sengaja dibuka oleh seseorang).",
        "distractors": [
            "A: あけ (ake / sengaja dibuka), B: あき (aki / terbuka sendiri).",
            "A: しまり (shimari / tertutup sendiri), B: しめ (shime / sengaja ditutup).",
            "A: きえ (kie / padam sendiri), B: けし (keshi / sengaja dipadamkan).",
            "A: おち (ochi / jatuh sendiri), B: おとし (otoshi / sengaja dijatuhkan)."
        ],
        "formula": {
            "title": "DISTINGSI JIDOUSHI & TADOUSHI (自動詞と他動詞の体系)",
            "latex": "\\begin{aligned} \\text{Intransitif (Otomatis): } & \\mathbf{N \\text{ が 開く (あく - Aku)}} \\implies \\text{Jendela terbuka sendiri} \\\\ \\text{Transitif (Intensional): } & \\mathbf{N \\text{ を 開ける (あける - Akeru)}} \\implies \\text{Membuka jendela} \\end{aligned}",
            "legend": "• Partikel が berpasangan dengan verba intransitif; partikel を berpasangan dengan verba transitif"
        },
        "hints": {
            "concept": "Kalimat 1 menggunakan partikel が (窓が) menandakan verba intransitif: あきました. Kalimat 2 menggunakan partikel を (窓を) menandakan perbuatan sengaja (transitif): あけました.",
            "execution": "Pilih: 'A: あき, B: あけ'."
        }
    },
    {
        "id": "jpn-lat-m-02",
        "materi": "MOJIGOI: KANJI N4 & JUKUGO",
        "topic": "Cara Baca Kanji Majemuk Kata Benda Sosial (経験, 案内, 準備)",
        "stem": "Perhatikan kalimat berikut:\n'日本へ 行く まえに、旅行の [準備] を しなければなりません。'\nCara baca gabungan kanji di dalam kurung siku [準備] yang bermakna 'persiapan' adalah...",
        "correct": "じゅんび (Junbi - persiapan perbekalan dan rencana perjalanan).",
        "distractors": [
            "じゅんびょう (Junbyou - kesalahan penambahan vokal panjang pada morfem bi).",
            "せつび (Setsubi - pembacaan yang berarti fasilitas atau perlengkapan gedung).",
            "あんない (Annai - pembacaan kanji 案内 yang bermakna pemanduan informasi).",
            "けいけん (Keiken - pembacaan kanji 経験 yang bermakna pengalaman hidup)."
        ],
        "formula": {
            "title": "PEMBACAAN KANJI JUKUGO N4 (二字熟語の音読み)",
            "latex": "[\\text{準 (Jun / Standar/Siap)}] + [\\text{備 (Bi / Kelengkapan)}] \\implies \\mathbf{\\text{じゅんび (Junbi)}}",
            "legend": "• Kedua morfem dibaca menggunakan jalur onyomi gabungan Sino-Jepang"
        },
        "hints": {
            "concept": "Kanji 準備 dibaca 'じゅんび' (junbi) yang berarti persiapan.",
            "execution": "Pilih: 'じゅんび (Junbi)'."
        }
    },
    {
        "id": "jpn-lat-m-03",
        "materi": "MOJIGOI: KANJI N4 & JUKUGO",
        "topic": "Cara Baca Kanji Hubungan Manusia & Komunikasi (相談, 約束, 連絡)",
        "stem": "Bacalah kalimat berikut:\n'こまったことが あったら、いつでも 先生に [相談] してください。'\nCara baca yang BENAR untuk gabungan kanji di dalam kurung siku [相談] yang bermakna 'berkonsultasi / berdiskusi mencari jalan keluar' adalah...",
        "correct": "そうだん (Soudan - konsultasi atau musyawarah pemecahan masalah).",
        "distractors": [
            "しょうだん (Shoudan - pembacaan yang tertukar dengan negosiasi perdagangan bisnis).",
            "やくそく (Yakusoku - pembacaan kanji 約束 yang bermakna janji temu).",
            "れんらく (Renraku - pembacaan kanji 連絡 yang bermakna komunikasi atau kabar).",
            "せつめい (Setsumei - pembacaan kanji 説明 yang bermakna penjelasan materi)."
        ],
        "formula": {
            "title": "KANJI JUKUGO KONSULTASI (相談の音読み)",
            "latex": "[\\text{相 (Sou / Saling/Menghadap)}] + [\\text{談 (Dan / Percakapan)}] \\implies \\mathbf{\\text{そうだん (Soudan)}}",
            "legend": "• Menunjukkan kegiatan berdialog untuk meminta nasihat atau bertukar pikiran"
        },
        "hints": {
            "concept": "Kanji 相談 dibaca 'そうだん' (soudan).",
            "execution": "Pilih opsi: 'そうだん (Soudan)'."
        }
    },
    {
        "id": "jpn-lat-m-04",
        "materi": "MOJIGOI: KATA BANTU BILANGAN LANJUTAN",
        "topic": "Penghitungan Frekuensi Kejadian (~回 vs ~度) dan Urutan (~番)",
        "stem": "Dokter memberikan instruksi penggunaan obat kepada pasien:\n'この くすりは 1にちに 3 ( ... )、しょくごに のんでください。'\nKata bantu pembilang yang TEPAT untuk menyatakan 'tiga kali dalam sehari' adalah...",
        "correct": "かい (Kai - satuan penghitung frekuensi pengulangan aksi/tindakan dalam satu satuan waktu).",
        "distractors": [
            "ばん (Ban - satuan penanda nomor urut atau peringkat antrean).",
            "こ (Ko - satuan penghitung kuantitas fisik benda-benda bulat kecil seperti buah).",
            "さつ (Satsu - satuan pembilang untuk jilidan buku dan dokumen tertulis).",
            "ほん (Hon - satuan pembilang untuk benda silindris panjang berwujud batangan)."
        ],
        "formula": {
            "title": "PEMBILANG FREKUENSI (頻度を表す助数詞)",
            "latex": "\\text{1日に (Dalam 1 Hari)} + \\text{3} + \\mathbf{\\text{回 (かい - Kai)}} + \\text{飲む (Diminum)}",
            "legend": "• ~回 (~kai) digunakan untuk menyatakan berapa kali suatu perbuatan berulang"
        },
        "hints": {
            "concept": "Menyatakan frekuensi minum obat '3 kali sehari' menggunakan kata bantu bilangan 回 (かい - kai): 3かい (sankai).",
            "execution": "Pilih: 'かい (Kai)'."
        }
    },
    {
        "id": "jpn-lat-m-05",
        "materi": "MOJIGOI: KATA SIFAT-NA N4",
        "topic": "Penggunaan Kata Sifat-Na sebagai Modifikator Nomina dan Adverbia",
        "stem": "Perhatikan kalimat rumpang berikut:\n'としょかんでは、みんなの めいわくに ならないように [しずか] ( ... ) 本を よんでください。'\nPartikel yang WAJIB dilekatkan pada kata sifat-na 'しずか' agar berfungsi sebagai adverbia (menerangkan cara membaca 'dengan tenang') adalah...",
        "correct": "に (ni - mengubah kata sifat-na menjadi kata keterangan cara kerja / adverbial).",
        "distractors": [
            "な (na - hanya digunakan jika kata sifat-na menerangkan langsung kata benda di belakangnya).",
            "で (de - partikel yang berfungsi sebagai kopula penyambung klausa kata sifat).",
            "だ (da - kopula bentuk dasar penutup kalimat deklaratif informal).",
            "の (no - partikel kepemilikan yang hanya menghubungkan dua kata benda)."
        ],
        "formula": {
            "title": "DERIVASI ADVERBIAL KATA SIFAT-NA (形容動詞の連用修飾)",
            "latex": "\\begin{aligned} \\text{Menerangkan Nomina: } & \\text{Kata Sifat-Na} + \\mathbf{\\text{な}} + \\text{Nomina} \\\\ \\text{Menerangkan Verba: } & \\text{Kata Sifat-Na} + \\mathbf{\\text{に}} + \\text{Verba} \\quad (\\text{しずか} + \\mathbf{\\text{に}} + \\text{よむ}) \\end{aligned}",
            "legend": "• Menunjukkan fungsi adverbial cara melakukan tindakan"
        },
        "hints": {
            "concept": "Kata sifat-na menerangkan kata kerja (yomu) wajib memakai akhiran 'に' (ni): しずかに 本を よみます.",
            "execution": "Pilih opsi: 'に (ni)'."
        }
    },
    {
        "id": "jpn-lat-m-06",
        "materi": "MOJIGOI: KOSAKATA TRANSITIF INTRANSITIF",
        "topic": "Pasangan Menyalakan vs Menyala (消える vs 消す / 点く vs 点ける)",
        "stem": "Di ruang kelas, listrik padam karena badai:\n'きゅうに でんきが ( A ) ました。せんせいが かいちゅうでんとうを ( B ) ました。'\nPasangan verba yang TEPAT untuk mengisi posisi ( A ) padam otomatis dan ( B ) menyalakan senter adalah...",
        "correct": "A: きえ (kie / padam sendiri secara tiba-tiba), B: つけ (tsuke / sengaja menyalakan lampu senter).",
        "distractors": [
            "A: けし (keshi / memadamkan dengan sengaja), B: つき (tsuki / menyala sendiri).",
            "A: つき (tsuki / menyala tiba-tiba), B: けし (keshi / mematikan senter).",
            "A: こわれ (koware / rusak sendiri), B: なおし (naoshi / memperbaiki senter).",
            "A: おち (ochi / jatuh sendiri), B: ひろい (hiroi / memungut senter)."
        ],
        "formula": {
            "title": "PASANGAN VERBA SAKELAR (電化機器の自他動詞)",
            "latex": "\\begin{aligned} \\text{Intransitif (Mati Sendiri): } & \\text{でんきが } \\mathbf{\\text{消える (きえる)}} \\\\ \\text{Transitif (Menyalakan): } & \\text{でんとうを } \\mathbf{\\text{点ける (つける)}} \\end{aligned}",
            "legend": "• Korelasi subjek-objek terhadap pengendalian sakelar kelistrikan"
        },
        "hints": {
            "concept": "Lampu padam sendiri: でんきが きえました (kie-). Menyalakan senter: でんとうを つけました (tsuke-).",
            "execution": "Pilih: 'A: きえ, B: つけ'."
        }
    },
    {
        "id": "jpn-lat-m-07",
        "materi": "MOJIGOI: GITAIGO & ONOMATOPE N4",
        "topic": "Mimik Suasana Hati dan Kondisi Fisik (ドキドキ, ペコペコ, イライラ)",
        "stem": "Cermati kalimat berikut:\n'あさから 何も 食べていないので、おなかが ( ... ) です。早く ラーメンが 食べたいです。'\nKata onomatope/gitaigo bahasa Jepang yang TEPAT untuk menggambarkan 'perut lapar keroncongan' adalah...",
        "correct": "ペコペコ (Pekopeko - tiruan kondisi perut yang sangat lapar dan mengempis).",
        "distractors": [
            "ドキドキ (Dokidoki - tiruan detak jantung berdebar-debar karena tegang atau gugup saat ujian).",
            "イライラ (Iraira - keadaan batin yang gelisah, kesal, atau tidak sabar menghadapi antrean).",
            "ニコニコ (Nikoniko - ekspresi senyuman manis dan berseri-seri penuh keramahan).",
            "ワクワク (Wakuwaku - perasaan antusias dan penuh kegembiraan menantikan acara liburan)."
        ],
        "formula": {
            "title": "GITAIGO KONDISI FISIK (状態副詞・オノマトペ)",
            "latex": "\\text{おなかが } + \\mathbf{\\text{ペコペコ (Pekopeko)}} \\implies \\text{Sangat Lapar Keroncongan}",
            "legend": "• Ragam leksikal deskriptif populer dalam komunikasi alami penutur asli Jepang"
        },
        "hints": {
            "concept": "Ungkapan khas perut lapar keroncongan dalam bahasa Jepang adalah 'おなかがペコペコ' (onaka ga pekopeko).",
            "execution": "Pilih: 'ペコペコ (Pekopeko)'."
        }
    },
    {
        "id": "jpn-lat-m-08",
        "materi": "MOJIGOI: KANJI N4 & JUKUGO",
        "topic": "Kanji Gejala Cuaca dan Bencana (地震, 台風, 事故)",
        "stem": "Dalam warta berita televisi NHK diberitakan:\n'きのうの 夜、強い [地震] が ありましたが、津波の 心配は ありません。'\nCara baca yang BENAR untuk gabungan kanji di dalam tanda kurung [地震] adalah...",
        "correct": "じしん (Jishin - gempa bumi tektonik atau seismik).",
        "distractors": [
            "たいふう (Taifuu - pembacaan kanji 台風 yang bermakna badai taifun).",
            "じこ (Jiko - pembacaan kanji 事故 yang bermakna insiden kecelakaan lalu lintas).",
            "かさい (Kasai - pembacaan kanji 火災 yang bermakna musibah kebakaran besar).",
            "こうずい (Kouzui - pembacaan kanji 洪水 yang bermakna bencana luapan air banjir)."
        ],
        "formula": {
            "title": "KANJI BENCANA ALAM (自然災害の語彙)",
            "latex": "[\\text{地 (Ji / Bumi/Tanah)}] + [\\text{震 (Shin / Getaran/Guncangan)}] \\implies \\mathbf{\\text{じしん (Jishin / Gempa Bumi)}}",
            "legend": "• Kosakata vital dalam literasi mitigasi kebencanaan nasional Jepang"
        },
        "hints": {
            "concept": "Kanji 地震 dibaca 'じしん' (jishin) yang berarti gempa bumi.",
            "execution": "Pilih: 'じしん (Jishin)'."
        }
    },
    {
        "id": "jpn-lat-m-09",
        "materi": "BUNPOU: BENTUK POTENSIAL (KANOU-KEI) N4",
        "topic": "Perubahan Verba Bentuk Kemampuan / Bisa (可能形) & Perubahan Partikel",
        "stem": "Perhatikan transformasi kalimat berikut:\nKalimat Asli: 'わたしは 漢字を 読みます。'\nKalimat Potensial: 'わたしは 漢字 [ A ] 読 [ B ] ます。'\nPartikel ( A ) dan konjugasi verba potensial ( B ) yang TEPAT untuk menyatakan 'bisa membaca kanji' adalah...",
        "correct": "A: が, B: め (Kanji ga yomemasu - verba Golongan I akhiran -mu berubah ke baris -e menjadi yomemasu, dan partikel objek を berganti menjadi が).",
        "distractors": [
            "A: を, B: みられ (partikel tidak berganti ke ga dan konjugasi keliru memakai akhiran ichidan).",
            "A: に, B: まれ (partikel ni keliru dan konjugasi tidak mengikuti vokal baris -e).",
            "A: で, B: め (partikel de salah fungsi sarana padahal objek potensial memerlukan ga).",
            "A: は, B: まれ (struktur topik ganda yang merusak struktur predikatif potensial)."
        ],
        "formula": {
            "title": "KAIDAH BENTUK BISA / POTENSIAL (可能動詞の形成規則)",
            "latex": "\\begin{aligned} \\text{Konjugasi: } & \\text{書く (kaku)} \\to \\mathbf{\\text{書ける (kakeru)}} \\quad / \\quad \\text{読む (yomu)} \\to \\mathbf{\\text{読める (yomeru)}} \\\\ \\text{Partikel: } & \\text{Objek [を] wajib bertransformasi menjadi } \\mathbf{[が]} \\end{aligned}",
            "legend": "• Menandai pergeseran makna dari tindakan volisional menjadi kapabilitas/kondisi"
        },
        "hints": {
            "concept": "Verba golongan 1 yomu -> yomemasu (bisa membaca). Objek potensial ditandai partikel が (Kanji ga yomemasu).",
            "execution": "Pilih opsi: 'A: が, B: め'."
        }
    },
    {
        "id": "jpn-lat-m-10",
        "materi": "BUNPOU: POLA KALIMAT BERSYARAT N4",
        "topic": "Penggunaan Pola Pengandaian Bersyarat ~Tara (~たら)",
        "stem": "Cermati dialog rencana kegiatan akhir pekan berikut:\nSato: 'あした 雨が ( ... )、サッカーの 試合は 中止に なります。'\nKen: 'そうですね。晴れると いいですね。'\nBentuk verba bersyarat yang TEPAT untuk mengisi rumpang Sato ('jika besok turun hujan...') adalah...",
        "correct": "ふったら (Futtara - bentuk lampau ta-kei furimashita -> futta + ra untuk syarat waktu/kondisional).",
        "distractors": [
            "ふると (Furu to - syarat keniscayaan alami yang kurang lazim untuk keputusan rapat manusia).",
            "ふれば (Fureba - bentuk ba-kei yang bernada kaku untuk percakapan rencana harian).",
            "ふったなら (Futtanara - penambahan dobel partikel yang tidak baku dalam kalimat sederhana).",
            "ふりながら (Furinagara - bermakna melakukan dua pekerjaan simultan sambil turun hujan)."
        ],
        "formula": {
            "title": "POLA BERSYARAT TARA (条件形「〜たら」)",
            "latex": "\\mathbf{V\\text{-た形}} + \\mathbf{\\text{ら}} \\implies \\text{Jika / Seandainya terjadi } V \\text{ di masa mendatang}",
            "legend": "• Bentuk bersyarat paling fleksibel dan dominan dalam percakapan lisan bahasa Jepang"
        },
        "hints": {
            "concept": "Pola bersyarat 'jika besok hujan...' memakai bentuk lampau + ra: ふったら (futtara).",
            "execution": "Pilih: 'ふったら (Futtara)'."
        }
    },
    {
        "id": "jpn-lat-m-11",
        "materi": "BUNPOU: POLA PENGALAMAN N4",
        "topic": "Menyatakan Pengalaman Masa Lalu dengan Ta Koto ga Aru (〜たことがある)",
        "stem": "Dalam sesi wawancara, pewawancara bertanya:\n'あなたは 今までに 富士山に ( ... ) ことが ありますか。'\nBentuk verba yang BENAR untuk melengkapi pertanyaan pengalaman 'apakah pernah mendaki Gunung Fuji' adalah...",
        "correct": "のぼった (Nobotta - verba bentuk lampau ta-kei wajib mendahului koto ga arimasu).",
        "distractors": [
            "のぼる (Noboru - verba bentuk kamus jisho-kei yang tidak bisa menyatakan pengalaman lampau).",
            "のぼって (Nobotte - verba te-form yang memerlukan verba bantu lain dan salah gramatikal di sini).",
            "のぼり (Nobori - akar kata verba masu-stem yang tidak bisa langsung melekat pada koto ga aru).",
            "のぼらない (Noboranai - bentuk negatif yang merusak struktur pertanyaan pengalaman positif)."
        ],
        "formula": {
            "title": "POLA RIWAYAT PENGALAMAN (経験表現)",
            "latex": "\\mathbf{V\\text{-た形}} + \\mathbf{\\text{ことが あります}} \\implies \\text{Pernah mengalami / melakukan } V",
            "legend": "• Struktur gramatikal baku untuk menanyakan riwayat hidup dan rekam jejak"
        },
        "hints": {
            "concept": "Pola menyatakan 'pernah...' selalu memakai Verba bentuk Ta + ことがある. Bentuk lampau dari noborimasu adalah のぼった (nobotta).",
            "execution": "Pilih opsi: 'のぼった (Nobotta)'."
        }
    },
    {
        "id": "jpn-lat-m-12",
        "materi": "BUNPOU: POLA KEHARUSAN N4",
        "topic": "Menyatakan Keharusan / Kewajiban (~なければなりません)",
        "stem": "Seorang mahasiswa asing diingatkan mengenai masa berlaku visa:\n'来月の 末までに 入国管理局へ 行って、ビザを 更新 ( ... )。'\nBentuk keharusan formal yang TEPAT untuk melengkapi kalimat tersebut adalah...",
        "correct": "しなければなりません (Shinakereba narimasen - harus/wajib memperbarui visa sebelum tenggat).",
        "distractors": [
            "しなくてもいいです (Shinakutemo ii desu - menyatakan tidak perlu atau boleh tidak diperbarui).",
            "してはいけません (Shite wa ikemasen - larangan mutlak bahwa tidak boleh memperbarui visa).",
            "するはずです (Suru hazu desu - perkiraan logis bahwa subjek semestinya memperbarui).",
            "したほうがいいです (Shita hou ga ii desu - anjuran/saran biasa yang tidak memiliki kekuatan hukum wajib)."
        ],
        "formula": {
            "title": "POLA KEHARUSAN / OBLIGASI (義務表現)",
            "latex": "\\mathbf{V\\text{-ない形 (Coret い)}} + \\mathbf{\\text{なければなりません}} \\implies \\text{Harus / Wajib melakukan } V",
            "legend": "• Merupakan keharusan mutlak berdasarkan aturan hukum, regulasi, atau moral"
        },
        "hints": {
            "concept": "Menyatakan kewajiban resmi 'harus melakukan...' memakai ~なければなりません (shinakereba narimasen).",
            "execution": "Pilih: 'しなければなりません'."
        }
    },
    {
        "id": "jpn-lat-m-13",
        "materi": "BUNPOU: PERKIRAAN & INDRA N4",
        "topic": "Pola Dugaan Visual ~Sou Da (〜そうだ: Kelihatannya Enak vs Kabar Angin)",
        "stem": "Seseorang melihat kue tart yang dihias stroberi segar di etalase toko dan berkomentar:\n'わあ、この ケーキ、とても ( ... ) そうですね。買いましょう！'\nBentuk kata sifat 'おいしい' yang TEPAT ketika digabungkan dengan pola dugaan visual (~sou da) adalah...",
        "correct": "おいし (Oishi - huruf い pada kata sifat-i wajib dihilangkan sebelum digabung dengan そうだ).",
        "distractors": [
            "おいしい (Oishii - mempertahankan huruf い akan mengubah maknanya menjadi kabar burung 'katanya enak').",
            "おいしく (Oishiku - bentuk adverbial yang keliru menempel pada imbuhan dugaan visual).",
            "おいしかった (Oishikatta - bentuk lampau yang tidak kompatibel dengan kesan pandangan seketika).",
            "おいしさ (Oishisa - nominalisasi kata sifat yang berarti tingkat kelezatan)."
        ],
        "formula": {
            "title": "DUGAAN PANDANGAN MATA VS KABAR BURUNG (様態と伝聞の「そうだ」)",
            "latex": "\\begin{aligned} \\text{Kesan Visual (Kelihatannya Enak): } & \\text{おいし} [\\cancel{\\text{い}}] + \\mathbf{\\text{そう}} \\implies \\mathbf{\\text{おいしそう}} \\\\ \\text{Kabar Burung (Katanya Enak): } & \\text{おいしい (Bentuk Kamus)} + \\mathbf{\\text{そうだ}} \\implies \\text{おいしいそうだ} \\end{aligned}",
            "legend": "• Perbedaan krusial pemotongan vokal /i/ yang membedakan persepsi visual dan rumor"
        },
        "hints": {
            "concept": "Melihat langsung dan menilai 'kelihatannya enak' menggunakan sifat-i tanpa 'i' + sou: おいし + そう = おいしそう.",
            "execution": "Pilih opsi: 'おいし (Oishi)'."
        }
    },
    {
        "id": "jpn-lat-m-14",
        "materi": "BUNPOU: POLA PENYELESAIAN & PENYESALAN N4",
        "topic": "Bentuk Te Shimau (〜てしまう / 〜てしまいました)",
        "stem": "Seorang siswa menceritakan kelalaiannya kepada teman sekelas:\n'たいへんです！電車の なかに かばんを ( ... ) しまいました。'\nVerba yang TEPAT untuk mengisi rumpang penyesalan 'tidak sengaja tertinggal / terlupa' adalah...",
        "correct": "わすれて (Wasurete - te-form dari wasuremasu yang berpasangan dengan shimaimashita menyatakan penyesalan mendalam).",
        "distractors": [
            "わすれ (Wasure - akar verba yang tidak memenuhi syarat konjugasi te-kei).",
            "わすれた (Wasureta - bentuk lampau ta-kei yang rancu bila disambung langsung dengan shimau).",
            "わすれないで (Wasurenaide - bentuk permohonan negatif yang bertolak belakang dengan fakta kejadian).",
            "わすれる (Wasureru - bentuk kamus yang tidak bisa bersambung dengan shimau)."
        ],
        "formula": {
            "title": "POLA PENYELESAIAN & KESALAHAN TERTELANJUR (完了と後悔の「〜てしまう」)",
            "latex": "\\mathbf{V\\text{-て形}} + \\mathbf{\\text{しまいました}} \\implies \\begin{cases} \\text{1. Tuntas sempurna (Selesai sama sekali)} \\\\ \\mathbf{\\text{2. Menyesal / Tidak sengaja berbuat salah}} \\end{cases}",
            "legend": "• Menunjukkan keterlanjuran peristiwa buruk di luar kehendak sadar pembicara"
        },
        "hints": {
            "concept": "Pola keterlanjuran/penyesalan 'tidak sengaja terlupa' memakai V-te + しまいました. Bentuk te dari wasuremasu adalah わすれて.",
            "execution": "Pilih: 'わすれて (Wasurete)'."
        }
    },
    {
        "id": "jpn-lat-m-15",
        "materi": "BUNPOU: POLA PERSIAPAN & TINDAKAN AWAL N4",
        "topic": "Bentuk Te Oku (〜ておく / 〜ておきます)",
        "stem": "Ibu berkata kepada anggota keluarga sebelum para tamu pesta berdatangan:\n'お客さんが 来る まえに、へやを そうじ ( ... )。'\nPola verba persiapan awal yang TEPAT melengkapi kalimat ibu adalah...",
        "correct": "しておきましょう (Shite okimashou - mari kita bersihkan ruangan terlebih dahulu sebagai persiapan menyambut tamu).",
        "distractors": [
            "してしまいましょう (Shite shimaimashou - pola yang menyiratkan penyelesaian terburu-buru atau penyesalan).",
            "してみましょう (Shite mimashou - pola yang berarti mari kita mencoba-coba membersihkan).",
            "してはいけません (Shite wa ikemasen - pola larangan tegas bahwa tidak boleh membersihkan).",
            "するつもりでした (Suru tsumori deshita - menyatakan niat masa lalu yang kemungkinan besar gagal terlaksana)."
        ],
        "formula": {
            "title": "POLA PERSIAPAN MENGHADAPI MASA DEPAN (準備表現「〜ておく」)",
            "latex": "\\mathbf{V\\text{-て形}} + \\mathbf{\\text{おきます}} \\implies \\text{Melakukan } V \\text{ terlebih dahulu untuk persiapan peristiwa kelak}",
            "legend": "• Sering berpasangan dengan klausa penanda waktu [〜まえに (sebelum)]"
        },
        "hints": {
            "concept": "Melakukan tindakan sebagai persiapan sebelum peristiwa lain terjadi memakai ~ておく (te oku): そうじしておきましょう.",
            "execution": "Pilih: 'しておきましょう (Shite okimashou)'."
        }
    },
    {
        "id": "jpn-lat-m-16",
        "materi": "BUNPOU: POLA MUDAH VS SULIT DILAKUKAN N4",
        "topic": "Pola Afiksasi ~Yasui (〜やすい) dan ~Nikui (〜にくい)",
        "stem": "Seorang kakek memuji ponsel pintar barunya:\n'この スマートフォンは 字が 大きくて、とても ( ... ) です。'\nBentuk kata yang TEPAT untuk menyatakan bahwa teks di ponsel tersebut 'mudah dibaca' adalah...",
        "correct": "よみやすい (Yomiyasui - akar verba yomi- dilekatkan akhiran -yasui untuk menunjukkan kemudahan tindakan).",
        "distractors": [
            "よみにくい (Yominikui - antonim yang berarti sulit atau sukar untuk dibaca).",
            "よむやすい (Yomuyasui - kesalahan gramatikal fatal karena menggunakan bentuk kamus sebelum yasui).",
            "よんでやすい (Yondeyasui - kesalahan gramatikal karena melekatkan te-form pada yasui).",
            "よまないやすい (Yomanaiyasui - kesalahan penggabungan bentuk negatif dengan yasui)."
        ],
        "formula": {
            "title": "AFIKSASI TINGKAT KEMUDAHAN TINDAKAN (難易表現)",
            "latex": "\\begin{aligned} \\mathbf{V\\text{-ます形 (Coret ます)}} + \\mathbf{\\text{やすい}} & \\implies \\text{Mudah dilakukan } (\\text{よみ} + \\text{やすい}) \\\\ \\mathbf{V\\text{-ます形 (Coret ます)}} + \\mathbf{\\text{にくい}} & \\implies \\text{Sukar / Sulit dilakukan } (\\text{よみ} + \\text{にくい}) \\end{aligned}",
            "legend": "• Mengubah verba menjadi kata sifat-i baru yang dapat dikonjugasikan lebih lanjut"
        },
        "hints": {
            "concept": "Mudah dibaca = Masu-stem (yomi) + yasui = よみやすい (yomiyasui).",
            "execution": "Pilih opsi: 'よみやすい (Yomiyasui)'."
        }
    },
    {
        "id": "jpn-lat-m-17",
        "materi": "BUNPOU: PERBANDINGAN KOMPARATIF & SUPERLATIF N4",
        "topic": "Struktur Perbandingan Dua Objek (A のほうが B より ~)",
        "stem": "Dalam percakapan mengenai transportasi di Tokyo, seorang warga lokal menjelaskan:\n'新幹線は 普通電車 ( ... ) ずっと 速いです。'\nPartikel pembanding yang TEPAT untuk melengkapi perbandingan 'Shinkansen jauh lebih cepat daripada kereta lokal biasa' adalah...",
        "correct": "より (yori - partikel penanda objek pembanding / standar acuan perbandingan).",
        "distractors": [
            "ほど (hodo - penanda batas derajat yang lazimnya digunakan dalam konstruksi perbandingan negatif).",
            "から (kara - partikel titik awal mula tempat atau waktu).",
            "まで (made - partikel titik akhir destinasi batas jangkauan).",
            "だけ (dake - partikel pembatas yang memiliki makna eksklusif 'hanya')."
        ],
        "formula": {
            "title": "STRUKTUR KOMPARATIF DUA ENTITAS (比較文型)",
            "latex": "\\mathbf{A \\text{ のほうが }} + \\mathbf{B \\text{ より }} + \\text{Sifat} \\implies A \\text{ lebih } [\\text{Sifat}] \\text{ daripada } B",
            "legend": "• Entitas sesudah より berfungsi sebagai titik tolak perbandingan relatif"
        },
        "hints": {
            "concept": "Pola perbandingan: A wa B yori... (A lebih ... daripada B). Partikelnya adalah より (yori).",
            "execution": "Pilih: 'より (yori)'."
        }
    },
    {
        "id": "jpn-lat-m-18",
        "materi": "BUNPOU: POLA KALIMAT TERTUTUP N4",
        "topic": "Menyatakan Kepastian Rencana dengan Tsumori (~つもり) vs Yotei (~予定)",
        "stem": "Lengkapilah kalimat pernyataan rencana pribadi berikut:\n'大学を 卒業した あと、日本の 会社で ( ... ) つもりです。'",
        "correct": "はたらく (Hataraku - bentuk kamus jisho-kei wajib mendahului kata benda penyimpul rencana tsumori).",
        "distractors": [
            "はたらきます (Hatarakimasu - bentuk masu formal yang dilarang melekat langsung sebelum tsumori).",
            "はたらいた (Hataraita - bentuk lampau yang bertentangan secara logika waktu dengan rencana masa depan).",
            "はたらいて (Hataraite - bentuk te yang memerlukan kata kerja penyambung lain).",
            "はたらき (Hataraki - bentuk akar verba yang tidak dapat memodifikasi tsumori secara gramatikal)."
        ],
        "formula": {
            "title": "POLA RENCANA SUBJEKTIF (意志・意図表現「つもり」)",
            "latex": "\\mathbf{V\\text{-辞書形 (Kamus)}} + \\mathbf{\\text{つもりです}} \\implies \\text{Berniat / Berencana kuat melakukan } V",
            "legend": "• Menunjukkan kehendak intensional orang pertama dalam menata masa depan"
        },
        "hints": {
            "concept": "Pola rencana ~つもり (tsumori) didahului oleh verba bentuk kamus (jisho-kei): はたらく (hataraku).",
            "execution": "Pilih: 'はたらく (Hataraku)'."
        }
    },
    {
        "id": "jpn-lat-m-19",
        "materi": "DOKKAI: TEKS PENGUMUMAN SEKOLAH",
        "topic": "Menganalisis Informasi Jadwal dan Syarat Pendaftaran Lomba Pidato",
        "stem": "Bacalah pengumuman sekolah berikut ini:\n--------------------------------------------------\n【日本語スピーチコンテストのお知らせ】\n・日時：11月20日（水）午後2時〜4時\n・場所：さくらホール\n・対象：留学生（日本滞在 2年以内の人）\n・申込締切：11月10日（日）午後5時までに 事務所へ 原稿を 出してください。\n--------------------------------------------------\nPernyataan yang BENAR dan SESUAI dengan isi pengumuman di atas adalah...",
        "correct": "Peserta yang berhak mendaftar adalah mahasiswa asing yang menetap di Jepang selama tidak lebih dari 2 tahun.",
        "distractors": [
            "Perlombaan pidato akan diselenggarakan pada hari Minggu tanggal 10 November jam 5 sore.",
            "Naskah pidato boleh dikumpulkan langsung di aula Sakura Hall pada saat hari perlombaan tiba.",
            "Lomba pidato berlangsung selama empat jam penuh mulai pukul 12 siang hingga pukul 4 sore.",
            "Seluruh siswa lokal warga negara Jepang diwajibkan mendaftarkan diri ke kantor kantor sekolah."
        ],
        "formula": {
            "title": "ANALISIS PERSYARATAN PENGUMUMAN (募集要項の読解)",
            "latex": "\\text{対象 (Sasaran): } \\text{留学生 (Mahasiswa Asing)} + \\mathbf{\\text{2年以内 (Maksimal 2 Tahun)}}",
            "legend": "• 以内 (inai) bermakna di dalam batas atau tidak lebih dari kuota angka patokan"
        },
        "hints": {
            "concept": "Cermati butir 対象 (taishou): 留学生（日本滞在 2年以内の人）. Artinya mahasiswa asing yang tinggal di Jepang maksimal 2 tahun.",
            "execution": "Pilih opsi: 'Peserta yang berhak mendaftar adalah mahasiswa asing yang menetap di Jepang selama tidak lebih dari 2 tahun'."
        }
    },
    {
        "id": "jpn-lat-m-20",
        "materi": "DOKKAI: SUREL FORMAL PENDIDIKAN",
        "topic": "Menemukan Alasan Keterlambatan Pengumpulan Tugas dalam Email Mahasiswa",
        "stem": "Bacalah surel yang dikirimkan seorang siswa kepada gurunya berikut:\n--------------------------------------------------\n山田先生\nいつも お世話になっております。高校3年の アリです。\n大変 申し訳ありませんが、昨日から 38度の 高い 熱が 出て、病院に おります。\nそのため、今日の 課題の レポートを 期日までに 提出することが できません。\n明日、熱が 下がったら、必ず 学校へ 持ってまいります。\nよろしく お願い申し上げます。\n--------------------------------------------------\nMengapa Ali tidak dapat mengumpulkan tugas laporannya pada hari ini?",
        "correct": "Karena Ali sedang dirawat/berada di rumah sakit akibat mengalami demam tinggi 38 derajat sejak kemarin.",
        "distractors": [
            "Karena Ali lupa membawa naskah laporannya dan tertinggal di dalam gerbong kereta listrik.",
            "Karena Yamada Sensei sedang tidak berada di kantor guru untuk menerima berkas laporan siswa.",
            "Karena komputer milik Ali mengalami kerusakan fatal pada sistem perangkat kerasnya.",
            "Karena tenggat waktu pengumpulan laporan telah diundur secara sepihak hingga pekan depan."
        ],
        "formula": {
            "title": "ANALISIS KAUSALITAS SUREL (メールの因果関係読解)",
            "latex": "\\text{Sebab: } \\mathbf{\\text{38度の 熱 \\& 病院におります}} \\xrightarrow{\\text{そのため (Oleh karena itu)}} \\text{Akibat: } \\text{レポートを提出できない}",
            "legend": "• Konjungtor そのため mengikat alasan medis langsung dengan konsekuensi ketidakhadiran"
        },
        "hints": {
            "concept": "Teks menyatakan: '昨日から 38度の 高い 熱が 出て、病院に おります。そのため...'. Jadi alasannya demam tinggi dan ada di RS.",
            "execution": "Pilih opsi yang menyebutkan kondisi sakit demam tinggi 38 derajat di rumah sakit."
        }
    },
    {
        "id": "jpn-lat-m-21",
        "materi": "DOKKAI: MEMO KEHIDUPAN APARTEMEN",
        "topic": "Memahami Instruksi Pemilahan Sampah Rumah Tangga di Jepang (Gomi Bunbetsu)",
        "stem": "Bacalah instruksi pengelola gedung apartemen (*manshon*) berikut:\n--------------------------------------------------\n【住人の 皆様へ：ゴミの 出し方】\n・燃えるゴミ（生ゴミ・紙くず）：火曜日・金曜日の 朝8時まで\n・燃えないゴミ（ビン・カン・金属）：第2・第4水曜日の 朝8時まで\n※プラスチック製品は 洗ってから、透明な 専用の 袋に 入れて 出してください。\n※夜間に ゴミを 出すと カラスが 荒らすため、絶対に 出さないでください。\n--------------------------------------------------\nBerdasarkan memo tersebut, hal apakah yang DILARANG KERAS dilakukan oleh para penghuni apartemen?",
        "correct": "Membuang atau meletakkan kantong sampah di luar pada malam hari karena berisiko diacak-acak oleh burung gagak.",
        "distractors": [
            "Membuang sampah sisa makanan dan kertas pada hari Selasa dan Jumat pagi.",
            "Mencuci produk kemasan plastik bekas sebelum dimasukkan ke dalam kantong khusus.",
            "Memasukkan kaleng dan botol bekas ke dalam kategori sampah yang tidak bisa dibakar.",
            "Mengikat kantong sampah khusus yang transparan dengan tali sebelum dibuang."
        ],
        "formula": {
            "title": "ATURAN LINGKUNGAN HIDUP JEPANG (ゴミ分別ルールの読解)",
            "latex": "\\text{Klausula Larangan: } \\text{夜間に ゴミを 出すと } \\dots \\implies \\mathbf{\\text{絶対に 出さないでください (Dilarang Mutlak)}}",
            "legend": "• Menjaga kebersihan sanitasi publik dari gangguan hewan liar kota (Karasu/Burung Gagak)"
        },
        "hints": {
            "concept": "Perhatikan kalimat peringatan: '※夜間に ゴミを 出すと カラスが 荒らすため、絶対に 出さないでください。'.",
            "execution": "Pilih opsi yang melarang membuang sampah pada waktu malam hari."
        }
    },
    {
        "id": "jpn-lat-m-22",
        "materi": "DOKKAI: WACANA BUDAYA SINGKAT",
        "topic": "Mengenal Tradisi Ohanami (お花見) dan Estetika Musim Semi",
        "stem": "Bacalah teks berikut:\n'毎年 3月下旬から 4月にかけて、日本人は 家族や 友達と 一緒に 公園へ 行って、「お花見」を します。桜の 木の 下に シートを しいて、お弁当を 食べたり 歌を 歌ったりして 楽しく 過ごします。桜の 花は 一週間から 十日ほどで 散ってしまうので、人々は その 短い 美しさを とても 大切に 感じています。'\nNilai filosofis atau alasan mengapa masyarakat Jepang sangat menghargai bunga sakura menurut wacana di atas adalah...",
        "correct": "Karena bunga sakura hanya mekar dalam periode waktu yang sangat singkat (sekitar 7-10 hari) sebelum akhirnya gugur.",
        "distractors": [
            "Karena kelopak bunga sakura dapat dipetik bebas untuk diolah menjadi bahan baku industri obat herbal.",
            "Karena acara Ohanami merupakan satu-satunya hari libur resmi nasional yang ditetapkan pemerintah di musim semi.",
            "Karena pohon sakura menghasilkan buah ceri manis bernilai jual tinggi untuk ekspor mancanegara.",
            "Karena masyarakat dilarang mengadakan piknik keluarga di taman kota pada selain musim sakura."
        ],
        "formula": {
            "title": "FILOSOFI ESTETIKA JEPANG (もののあわれ・桜の美学)",
            "latex": "\\text{桜の 花は } \\mathbf{\\text{短い 美しさ}} \\impliedby \\mathbf{\\text{一週間〜十日で 散る (Mudah Gugur)}}",
            "legend": "• Konsep Mono no Aware: Apresiasi mendalam terhadap keindahan fana kehidupan alam"
        },
        "hints": {
            "concept": "Teks menyatakan: '桜の 花は 一週間から 十日ほどで 散ってしまうので、人々は その 短い 美しさを とても 大切に 感じています。'.",
            "execution": "Pilih opsi yang mengaitkan keindahan sakura dengan periode mekarnya yang sangat singkat (7-10 hari)."
        }
    },
    {
        "id": "jpn-lat-m-23",
        "materi": "DOKKAI: WACANA ISU KONTEMPORER",
        "topic": "Konsep Budaya Mottainai (もったいない) dalam Daur Ulang",
        "stem": "Bacalah teks wacana berikut:\n'「もったいない」という 言葉は、物を 無駄に することを 惜しむ 日本の 伝統的な 心を 表しています。まだ 使える 物を 捨てたり、食べ物を 残したりすることは「もったいない」ことです。現在、この 考え方は「Reduce（減らす）・Reuse（再利用）・Recycle（再生）」の 精神と 結びつき、世界中で 環境保護の 合言葉として 注目されています。'\nGagasan utama yang diuraikan dalam paragraf di atas adalah...",
        "correct": "Konsep 'Mottainai' mencerminkan kearifan tradisional Jepang untuk tidak menyia-nyiakan barang yang kini diadaptasi dunia sebagai semangat pelestarian lingkungan.",
        "distractors": [
            "Masyarakat Jepang modern sudah sepenuhnya meninggalkan penggunaan kata 'Mottainai' dalam kehidupan konsumsi sehari-hari.",
            "Istilah 'Mottainai' hanya berlaku khusus untuk tata cara menghabiskan seluruh butir beras saat santap malam.",
            "Pemerintah Jepang melarang keras masyarakat membeli barang-barang baru guna menghemat devisa negara.",
            "Negara-negara di dunia menolak integrasi konsep lokal Jepang ke dalam program kerja pelestarian alam PBB."
        ],
        "formula": {
            "title": "SINTESIS NILAI BUDAYA MOTTAINAI (環境精神の世界的展開)",
            "latex": "\\mathbf{\\text{もったいない (Menolak Sia-Sia)}} \\equiv \\mathbf{\\text{3R (Reduce, Reuse, Recycle)}} \\implies \\text{Prinsip Ekologi Global}",
            "legend": "• Menjembatani etika kearifan lokal tradisional dengan gerakan keberlanjutan global modern"
        },
        "hints": {
            "concept": "Paragraf menjelaskan filosofi 'Mottainai' (menolak mubazir/sia-sia) yang terhubung erat dengan prinsip 3R dalam perlindungan lingkungan dunia.",
            "execution": "Pilih opsi sintesis konsep 'Mottainai' dan pelestarian lingkungan."
        }
    },
    {
        "id": "jpn-lat-m-24",
        "materi": "KAIWA HYOUGEN: PENOLAKAN HALUS (HENSURU)",
        "topic": "Etika Menolak Ajakan Rekan Secara Tidak Langsung (ちょっと都合が...)",
        "stem": "Seorang teman mengajak pergi menonton konser musik malam ini:\nKen: '今晩、一緒に コンサートへ 行きませんか。'\nNamun, Hana tidak bisa hadir karena harus mempersiapkan ujian esok hari. Cara menolak yang PALING SOPAN dan lumrah dalam pragmatik komunikasi Jepang tanpa menyinggung perasaan lawan bicara adalah...",
        "correct": "「すみません、今晩は ちょっと 都合が 悪くて...。」 (Maaf, malam ini keadaan waktu saya agak kurang memungkinkan...).",
        "distractors": [
            "「嫌です。絶対に行きたくありません。」 (Penolakan kasar dan konfrontatif yang merusak keharmonisan pertemanan).",
            "「ダメです。今晩は暇がゼロです。」 (Bahasa kaku dan tidak sopan untuk merespons ajakan baik teman).",
            "「いいえ、行きません。」 (Jawaban datar negatif tanpa basa-basi empati yang dianggap sangat dingin).",
            "「コンサートはつまらないのでやめましょう。」 (Meremehkan selera musik teman yang mengajak)."
        ],
        "formula": {
            "title": "PRAGMATIK PENOLAKAN TIDAK LANGSUNG (配慮表現・婉曲な断り)",
            "latex": "\\text{Ajakan} \\xrightarrow{\\text{Penolakan Sopan}} \\mathbf{\\text{すみません、ちょっと都合が悪くて (Chotto tsugou ga warukute...)}}",
            "legend": "• Penggunaan kata 'chotto' dan menggantungkan akhir kalimat untuk menjaga wajah lawan bicara"
        },
        "hints": {
            "concept": "Orang Jepang menolak ajakan secara halus dengan kata 'chotto tsugou ga warukute...' (agak kurang pas waktunya).",
            "execution": "Pilih opsi: '「すみません、今晩は ちょっと 都合が 悪くて...。」'."
        }
    },
    {
        "id": "jpn-lat-m-25",
        "materi": "KAIWA HYOUGEN: MEMINTA IZIN",
        "topic": "Pola Izin Te mo ii desu ka (〜てもいいですか) di Tempat Umum",
        "stem": "Saat berada di museum seni, seorang pengunjung ingin memastikan apakah diperbolehkan mengambil foto lukisan tertentu. Kalimat pertanyaan izin yang TEPAT diajukan kepada petugas museum adalah...",
        "correct": "ここで 写真を 撮っても いいですか。 (Koko de shashin wo totte mo ii desu ka - apakah di sini boleh mengambil foto?).",
        "distractors": [
            "ここで 写真を 撮らなければなりませんか。 (Menanyakan apakah dirinya diwajibkan mengambil foto di tempat tersebut).",
            "ここで 写真を 撮ってはいけませんか。 (Pertanyaan bernada memojokkan apakah dilarang mengambil foto).",
            "ここで 写真を 撮りたいですか。 (Menanyakan apakah petugas museum yang ingin mengambil foto).",
            "ここで 写真を 撮るつもりですか。 (Menanyakan rencana petugas apakah berniat mengambil foto)."
        ],
        "formula": {
            "title": "POLA PERMOHONAN IZIN (許可を求める表現)",
            "latex": "\\mathbf{V\\text{-て形}} + \\mathbf{\\text{も いいですか}} \\implies \\text{Bolehkah saya melakukan } V \\text{?}",
            "legend": "• Standar etika meminta konfirmasi perizinan kepada pemegang otoritas ruang publik"
        },
        "hints": {
            "concept": "Pola meminta izin sopan adalah V-te + もいいですか (totte mo ii desu ka).",
            "execution": "Pilih: 'ここで 写真を 撮っても いいですか。'."
        }
    }
]
