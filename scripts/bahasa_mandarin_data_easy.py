# -*- coding: utf-8 -*-
"""
BAHASA MANDARIN - PAKET SOAL LATIHAN MUDAH (EASY) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / HSK 2
Distribusi:
- 10 Butir: Hanzi & Pinyin (Mojigoi - Radikal Bushou, 4 nada fonetik, sandhi nada, goresan dasar)
- 10 Butir: Tata Bahasa Dasar (Yufa HSK 2 - SVO, kata bantu bilangan/liangci, partikel de/ma/ne)
- 5 Butir: Ungkapan Komunikasi Harian & Etika Keseharian
"""

BAHASA_MANDARIN_EASY_ITEMS = [
    {
        "id": "man-lat-e-01",
        "materi": "HANZI & PINYIN: RADIKAL DASAR (BUSHOU)",
        "topic": "Radikal Air (三点水 - Sāndiǎnshuǐ / 氵)",
        "stem": "Dalam sistem aksara Hanzi, radikal (部首 - bùshǒu) sering kali mengindikasikan medan semantik suatu karakter. Karakter Hanzi manakah di bawah ini yang memuat radikal 'Air' (*Sāndiǎnshuǐ* - 氵)?",
        "correct": "河 (hé - sungai / aliran air alami).",
        "distractors": [
            "林 (lín - hutan lebat yang tersusun dari radikal pohon 木).",
            "休 (xiū - beristirahat yang memuat radikal manusia 亻 dan pohon 木).",
            "吃 (chī - makan yang memuat radikal mulut 口).",
            "跑 (pǎo - berlari yang memuat radikal kaki 足/𧾷)."
        ],
        "formula": {
            "title": "RADIKAL AIR SAN DIAN SHUI (部首「氵」)",
            "latex": "\\mathbf{[氵 (Sāndiǎnshuǐ / Air)]} \\implies \\begin{cases} \\mathbf{\\text{河 (hé - Sungai)}} \\\\ \\text{海 (hǎi - Laut)} \\\\ \\text{江 (jiāng - Sungai Besar)} \\end{cases}",
            "legend": "• Menandai karakter-karakter yang memiliki keterkaitan langsung dengan zat cair atau hidrologi"
        },
        "hints": {
            "concept": "Radikal 氵 (tiga titik air) ada pada karakter yang berkaitan dengan air. '河' (hé) berarti sungai.",
            "execution": "Pilih opsi: '河 (hé)'."
        }
    },
    {
        "id": "man-lat-e-02",
        "materi": "HANZI & PINYIN: FONETIKA NADA",
        "topic": "Aturan Sandhi Nada Ketiga (第三声变调: Nǐ Hǎo -> Ní Hǎo)",
        "stem": "Ketika dua karakter yang sama-sama memiliki nada ketiga (*shàngshēng* - nada bergelombang ∨) bertemu secara berurutan, seperti pada kata sapaan '你好' (nǐ hǎo), bagaimanakah perubahan nada (*sandhi*) yang WAJIB dilafalkan?",
        "correct": "Karakter pertama (你) berubah menjadi nada kedua (阳平 - yángpíng / nada naik /), sehingga dilafalkan 'ní hǎo'.",
        "distractors": [
            "Karakter kedua (好) berubah menjadi nada keempat (去声 - qùshēng / nada turun tegas).",
            "Kedua karakter sama-sama berubah menjadi nada netral yang diucapkan sangat pendek dan ringan.",
            "Karakter pertama berubah menjadi nada pertama (阴平 - yīnpíng / nada tinggi datar).",
            "Kedua karakter tetap dilafalkan utuh dengan nada ketiga tanpa mengalami perubahan fonetis apa pun."
        ],
        "formula": {
            "title": "KAIDAH SANDHI NADA KETIGA (三声变调规则)",
            "latex": "\\mathbf{3 + 3 \\implies 2 + 3} \\quad (\\text{nǐ } [3] + \\text{hǎo } [3] \\longrightarrow \\mathbf{\\text{ní } [2] + \\text{hǎo } [3]})",
            "legend": "• Menghindari kelelahan pita suara akibat pengulangan kontur frekuensi rendah berturut-turut"
        },
        "hints": {
            "concept": "Pertemuan dua nada 3 (3+3) secara otomatis mengubah nada pertama menjadi nada 2: 你好 nǐ hǎo dilafalkan 'ní hǎo'.",
            "execution": "Pilih opsi yang menjelaskan perubahan karakter pertama menjadi nada kedua (2+3)."
        }
    },
    {
        "id": "man-lat-e-03",
        "materi": "HANZI & PINYIN: ATURAN PERUBAHAN NADA KATA 'BU' (不)",
        "topic": "Sandhi Nada Karakter '不' (Bù vs Bú)",
        "stem": "Kata negasi '不' pada dasarnya bernada keempat (*bù*). Namun, apabila '不' diikuti oleh karakter lain yang juga bernada keempat (*qùshēng*), seperti pada kata '不是' (shì), bagaimanakah pelafalan Pinyin yang BENAR?",
        "correct": "bú shì (nada 'bù' berubah menjadi nada kedua 'bú' saat mendahului nada keempat).",
        "distractors": [
            "bù shì (tetap bernada keempat ganda yang dianggap tidak selaras dengan kaidah eufoni Mandarin).",
            "bǔ shì (berubah menjadi nada ketiga bergelombang).",
            "bū shì (berubah menjadi nada pertama yang datar tinggi).",
            "bu shì (berubah menjadi nada netral tanpa tanda aksen)."
        ],
        "formula": {
            "title": "KAIDAH SANDHI NADA KATA '不' (「不」字变调)",
            "latex": "\\begin{cases} \\mathbf{\\text{不 (bù)} + \\text{Nada 4}} & \\implies \\mathbf{\\text{bú } + \\text{Nada 4}} \\quad (\\text{不是 } \\to \\mathbf{\\text{bú shì}}) \\\\ \\text{不 (bù)} + \\text{Nada 1/2/3} & \\implies \\text{Tetap } \\mathbf{\\text{bù}} \\quad (\\text{不高 } \\to \\text{bù gāo}) \\end{cases}",
            "legend": "• Transisi nada naik sebelum nada turun menciptakan dinamika vokal yang lentur"
        },
        "hints": {
            "concept": "Kaidah '不': jika diikuti nada 4 (seperti 是 shì), maka 不 dibaca nada 2 (bú shì).",
            "execution": "Pilih: 'bú shì'."
        }
    },
    {
        "id": "man-lat-e-04",
        "materi": "HANZI & PINYIN: ATURAN PERUBAHAN NADA KATA 'YI' (一)",
        "topic": "Sandhi Nada Karakter '一' (Yī, Yí, Yì)",
        "stem": "Karakter '一' (satu) memiliki nada dasar pertama (*yī*). Kapan karakter '一' tersebut WAJIB berubah pelafalannya menjadi nada kedua (*yí*)?",
        "correct": "Ketika '一' diikuti oleh karakter yang berharakat nada keempat (*qùshēng*), seperti pada kata '一共' (yígòng) atau '一下' (yíxià).",
        "distractors": [
            "Ketika '一' berdiri sendiri saat menghitung urutan angka satu, dua, tiga (yī, èr, sān).",
            "Ketika '一' diikuti oleh kata bernada pertama seperti '一天' (yìtiān).",
            "Ketika '一' terletak pada akhir frasa atau penutup kalimat pernyataan.",
            "Ketika '一' digunakan untuk menyebut nomor kamar hotel atau nomor telepon pribadi."
        ],
        "formula": {
            "title": "KAIDAH SANDHI NADA KATA '一' (「一」字变调)",
            "latex": "\\begin{aligned} \\text{Urutan Angka Mandiri: } & \\text{yī (Tetap Nada 1)} \\\\ \\mathbf{\\text{Di Depan Nada 4:}} & \\mathbf{\\text{yí }} + \\mathbf{\\text{Nada 4}} \\quad (\\text{一共 } \\to \\mathbf{\\text{yígòng}}) \\\\ \\text{Di Depan Nada 1, 2, 3: } & \\text{yì } + \\text{Nada 1/2/3} \\quad (\\text{一天 } \\to \\text{yìtiān}) \\end{aligned}",
            "legend": "• Menjaga ritme metrik suku kata bahasa Mandarin baku"
        },
        "hints": {
            "concept": "Kata 一 (yī) berubah menjadi nada 2 (yí) hanya jika berada di depan suku kata bernada 4 (seperti 一下 yíxià, 一共 yígòng).",
            "execution": "Pilih opsi yang menyebutkan kondisi mendahului karakter bernada keempat."
        }
    },
    {
        "id": "man-lat-e-05",
        "materi": "HANZI & PINYIN: GORESAN DASAR (BǏHUÀ)",
        "topic": "Identifikasi Goresan Dasar Hanzi (横, 竖, 撇, 捺)",
        "stem": "Dalam seni kaligrafi dan penulisan Hanzi, goresan garis lurus horizontal dari kiri ke kanan (seperti pada karakter '一') dinamakan...",
        "correct": "Héng (横 - goresan mendatar horizontal).",
        "distractors": [
            "Shù (竖 - goresan tegak lurus vertikal dari atas ke bawah).",
            "Piě (撇 - goresan miring melengkung ke arah kiri bawah).",
            "Nà (捺 - goresan tebal meluncur ke arah kanan bawah).",
            "Diǎn (点 - goresan titik kecil penekan aksen)."
        ],
        "formula": {
            "title": "DELAPAN GORESAN POKOK YONGZI (永字八法・基本笔画)",
            "latex": "\\begin{array}{|c|c|c|} \\hline \\mathbf{\\text{Héng (横)}} & \\text{Garis Horizontal Mendatar} & \\mathbf{\\text{一}} \\\\ \\hline \\text{Shù (竖)} & \\text{Garis Vertikal Tegak} & \\text{丨} \\\\ \\hline \\text{Piě (撇)} & \\text{Garis Serong Kiri Bawah} & \\text{丿} \\\\ \\hline \\text{Nà (捺)} & \\text{Garis Luncur Kanan Bawah} & \\text{㇏} \\\\ \\hline \\end{array}",
            "legend": "• Fondasi ortografi pembentukan struktur aksara hanzi fusha"
        },
        "hints": {
            "concept": "Goresan garis horizontal mendatar disebut 横 (Héng). Garis vertikal tegak disebut 竖 (Shù).",
            "execution": "Pilih: 'Héng (横)'."
        }
    },
    {
        "id": "man-lat-e-06",
        "materi": "MOJIGOI: KATA GANTI ORANG (RÉNCHĒNG DÀICÍ)",
        "topic": "Pola Pembentukan Jamak dengan Men (们) dan Kata Hormat Nín (您)",
        "stem": "Perhatikan dua kalimat bahasa Mandarin berikut:\n1) 老师，( A ) 身体好吗？(Menyapa guru dengan bentuk kata ganti 'Anda' yang sangat hormat).\n2) 朋友 ( B ) 一起去图书馆。(Menyatakan bentuk jamak 'teman-teman').\nKata yang TEPAT untuk mengisi posisi ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: 您 (nín), B: 们 (men).",
        "distractors": [
            "A: 你 (nǐ), B: 们 (men) - penggunaan 'nǐ' dinilai kurang sopan untuk menyapa guru.",
            "A: 您 (nín), B: 个 (gè) - 'gè' adalah kata bantu bilangan, bukan penanda jamak nomina manusia.",
            "A: 他 (tā), B: 们 (men) - 'tā' merujuk pada orang ketiga tunggal 'dia'.",
            "A: 谁 (shéi), B: 些 (xiē) - tidak membentuk keselarasan subjek gramatikal."
        ],
        "formula": {
            "title": "PRONOMINA DAN PENANDA JAMAK (人称代词与复数后缀)",
            "latex": "\\begin{cases} \\mathbf{\\text{Hormat (Atasan/Guru):}} & \\mathbf{\\text{您 (nín - Anda)}} \\\\ \\mathbf{\\text{Jamak Insani:}} & \\text{Nomina Insani} + \\mathbf{\\text{们 (men)}} \\implies \\text{朋友们 (Teman-teman)} \\end{cases}",
            "legend": "• Menjaga etika hierarki rasa hormat kepada pendidik dalam budaya Tionghoa"
        },
        "hints": {
            "concept": "Menyapa guru secara hormat: 您 (nín). Bentuk jamak teman-teman: 朋友 + 们 (péngyoumen).",
            "execution": "Pilih: 'A: 您 (nín), B: 们 (men)'."
        }
    },
    {
        "id": "man-lat-e-07",
        "materi": "YUFA: KATA BANTU BILANGAN (LIÀNGCÍ)",
        "topic": "Penggunaan Kata Bantu Bilangan Benda Khusus (本, 张, 件, 条)",
        "stem": "Lengkapilah kalimat rumpang berikut dengan kata bantu bilangan (*liàngcí*) yang TEPAT:\n'我想买一 ( A ) 书和一 ( B ) 桌子。'",
        "correct": "A: 本 (běn - satuan untuk jilidan buku/majalah), B: 张 (zhāng - satuan untuk benda berpermukaan datar rata seperti meja, kertas, atau kasur).",
        "distractors": [
            "A: 个 (gè), B: 本 (běn) - terbalik dan pemakaian gè kurang presisi untuk buku cetak.",
            "A: 张 (zhāng), B: 件 (jiàn) - jiàn adalah satuan untuk pakaian atau perkara urusan.",
            "A: 条 (tiáo), B: 只 (zhī) - tiáo untuk benda panjang menjalar dan zhī untuk binatang berkaki.",
            "A: 块 (kuài), B: 瓶 (píng) - kuài untuk potongan balok/uang dan píng untuk botol minuman."
        ],
        "formula": {
            "title": "SPESIFIKASI LIANGCI MANDARIN (量词的搭配体系)",
            "latex": "\\begin{aligned} \\text{一} + \\mathbf{\\text{本 (běn)}} + \\text{书 (Buku)} & \\implies \\text{Sebuah Buku Jilidan} \\\\ \\text{一} + \\mathbf{\\text{张 (zhāng)}} + \\text{桌子 (Meja)} & \\implies \\text{Sebuah Meja Rata} \\end{aligned}",
            "legend": "• Karakteristik morfologis benda mengikat kata penggolong pembilang secara ketat"
        },
        "hints": {
            "concept": "Buku (书) menggunakan kata bantu bilangan 本 (běn). Meja (桌子) memiliki permukaan rata, menggunakan 张 (zhāng).",
            "execution": "Pilih: 'A: 本 (běn), B: 张 (zhāng)'."
        }
    },
    {
        "id": "man-lat-e-08",
        "materi": "YUFA: KATA BANTU BILANGAN (LIÀNGCÍ)",
        "topic": "Satuan Hitung Pakaian (件 - Jiàn) dan Benda Panjang Lentur (条 - Tiáo)",
        "stem": "Ibu pergi ke pusat perbelanjaan dan membeli sepotong kemeja serta sehelai celana panjang:\n'妈妈买了一 ( A ) 衬衫和一 ( B ) 裤子。'\nPasangan *liàngcí* yang TEPAT untuk mengisi posisi ( A ) pakaian atasan dan ( B ) celana panjang berturut-turut adalah...",
        "correct": "A: 件 (jiàn - satuan pakaian atasan/baju), B: 条 (tiáo - satuan benda panjang ramping seperti celana, ikan, dan sungai).",
        "distractors": [
            "A: 条 (tiáo), B: 件 (jiàn) - terbalik penempatan fungsinya antara baju atasan dan celana bawahan.",
            "A: 双 (shuāng), B: 顶 (dǐng) - shuāng untuk sepasang (sepatu/kaus kaki) dan dǐng untuk topi.",
            "A: 只 (zhī), B: 根 (gēn) - zhī untuk hewan dan gēn untuk benda silindris keras.",
            "A: 块 (kuài), B: 片 (piàn) - kuài untuk batangan dan piàn untuk lembaran tipis roti/daun."
        ],
        "formula": {
            "title": "LIANGCI BUSANA MANDARIN (服装量词搭配)",
            "latex": "\\begin{cases} \\text{Atasan / Kemeja / Mantel:} & \\mathbf{\\text{件 (jiàn)}} \\implies \\text{一件衬衫} \\\\ \\text{Bawahan / Celana / Rok:} & \\mathbf{\\text{条 (tiáo)}} \\implies \\text{一条裤子} \\end{cases}",
            "legend": "• Morfologi pakaian atasan (jiàn) vs panjang menjuntai (tiáo)"
        },
        "hints": {
            "concept": "Kemeja (衬衫) memakai 件 (jiàn). Celana (裤子) bentuknya panjang, memakai 条 (tiáo).",
            "execution": "Pilih: 'A: 件 (jiàn), B: 条 (tiáo)'."
        }
    },
    {
        "id": "man-lat-e-09",
        "materi": "YUFA: KALIMAT TANYA RETORIK & PILIHAN",
        "topic": "Kalimat Tanya Ya/Tidak (吗) vs Pertanyaan Retorik Konfirmasi (吧)",
        "stem": "Perhatikan dialog percakapan berikut:\n1) 你明天去学校 ( A )？(Menanyakan informasi faktual apakah pergi atau tidak).\n2) 今天天气真好，我们去公园散步 ( B )。(Mengajak atau meminta konfirmasi persetujuan dengan nada santai).\nPartikel tanya penutup kalimat yang TEPAT untuk ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: 吗 (ma - penanda interogatif ya/tidak murni), B: 吧 (ba - penanda ajakan, saran, atau konfirmasi perkiraan).",
        "distractors": [
            "A: 吧 (ba), B: 吗 (ma) - terbalik fungsi antara pertanyaan murni dan kalimat ajakan saran.",
            "A: 呢 (ne), B: 的 (de) - ne untuk pertanyaan balik/sedang berlangsung dan de adalah partikel kepemilikan.",
            "A: 吗 (ma), B: 呢 (ne) - kalimat kedua bukan merupakan pertanyaan balik topik eliptis.",
            "A: 啊 (a), B: 啦 (la) - partikel modalitas seru yang tidak membentuk struktur interrogatif standar."
        ],
        "formula": {
            "title": "PARTIKEL AKHIR KALIMAT TANYA (句尾语气助词)",
            "latex": "\\begin{aligned} \\mathbf{\\text{吗 (ma)}} & \\implies \\text{Pertanyaan Tertutup Interogatif Murni (50/50)} \\\\ \\mathbf{\\text{吧 (ba)}} & \\implies \\text{Ajakan / Saran / Dugaan Berkeyakinan Tinggi (Ayo / Bukan?)} \\end{aligned}",
            "legend": "• Menentukan sikap komunikatif penutur terhadap respons yang diharapkan"
        },
        "hints": {
            "concept": "Kalimat 1 pertanyaan fakta: 吗 (ma). Kalimat 2 ajakan mari jalan-jalan: 吧 (ba).",
            "execution": "Pilih: 'A: 吗 (ma), B: 吧 (ba)'."
        }
    },
    {
        "id": "man-lat-e-10",
        "materi": "YUFA: PARTIKEL STRUKTURAL KEPEMILIKAN",
        "topic": "Penggunaan Partikel Struktural De (的)",
        "stem": "Dalam tata bahasa Mandarin, kalimat manakah di bawah ini yang menunjukkan penggunaan partikel struktural '的' (de) untuk menyatakan hubungan kepemilikan (*possessive*) secara TEPAT?",
        "correct": "这是我爸爸的汽车。 (Zhè shì wǒ bàba de qìchē - ini adalah mobil milik ayah saya).",
        "distractors": [
            "跑得很快的。 (Penggunaan 'de' kepemilikan yang tertukar dengan komplemen derajat 得 dé).",
            "他很的高兴。 (Penyisipan partikel 'de' yang salah di antara kata keterangan tingkat dan kata sifat).",
            "的我们去吃饭。 (Partikel 'de' tidak boleh diletakkan di awal kalimat mendahului subjek pronomina).",
            "我看了的电影。 (Partikel 'de' keliru disisipkan menggantikan partikel aspek ketuntasan 了 le)."
        ],
        "formula": {
            "title": "PARTIKEL KEPEMILIKAN DE (定语助词「的」)",
            "latex": "\\mathbf{\\text{Pemilik / Atribut}} + \\mathbf{\\text{的 (de)}} + \\mathbf{\\text{Benda yang Dimiliki}} \\implies \\text{我爸爸 } \\mathbf{\\text{的}} \\text{ 汽车}",
            "legend": "• Berfungsi menghubungkan modifikator nomina (pewatas) dengan inti frasa nomina"
        },
        "hints": {
            "concept": "Partikel 的 (de) berfungsi menghubungkan pemilik dan milik: 我爸爸的汽车 (mobil milik ayah saya).",
            "execution": "Pilih: '这是我爸爸的汽车。'."
        }
    },
    {
        "id": "man-lat-e-11",
        "materi": "YUFA: SUSUNAN KATA KALIMAT DASAR (SVO)",
        "topic": "Penempatan Keterangan Waktu dalam Kalimat Mandarin",
        "stem": "Dalam bahasa Mandarin, penempatan kata keterangan waktu (*time word*) memiliki regulasi posisi yang kaku. Manakah susunan kalimat yang BENAR secara gramatikal untuk menyatakan 'Saya besok pergi ke Beijing'?",
        "correct": "我明天去北京。 / 明天我去北京。 (Keterangan waktu 'míngtiān' diletakkan tepat setelah subjek atau di awal kalimat sebelum subjek).",
        "distractors": [
            "我去北京明天。 (Keterangan waktu diletakkan di akhir kalimat meniru struktur bahasa Indonesia/Inggris yang dilarang keras dalam Mandarin).",
            "我去明天北京。 (Keterangan waktu disisipkan di antara kata kerja dan objek destinasi).",
            "北京明天我去。 (Objek kota diletakkan di awal kalimat tanpa struktur topik-komen yang sahih).",
            "去北京我明天。 (Kata kerja diletakkan di awal kalimat deklaratif tanpa adanya konteks imperatif)."
        ],
        "formula": {
            "title": "SINTAKSIS KETERANGAN WAKTU MANDARIN (时间状语的语序)",
            "latex": "\\mathbf{S + \\text{Time} + V + O} \\quad \\lor \\quad \\mathbf{\\text{Time} + S + V + O} \\quad (\\cancel{\\text{S + V + O + Time}})",
            "legend": "• Kaidah mutlak: Keterangan waktu TIDAK PERNAH boleh ditaruh di akhir kalimat"
        },
        "hints": {
            "concept": "Dalam bahasa Mandarin, keterangan waktu ditaruh SEBELUM kata kerja (setelah subjek atau paling depan). Tidak boleh di ujung belakang kalimat.",
            "execution": "Pilih opsi: '我明天去北京。 / 明天我去北京。'."
        }
    },
    {
        "id": "man-lat-e-12",
        "materi": "YUFA: PREPOSISI TEMPAT (ZÀI - 在)",
        "topic": "Struktur Kalimat Keterangan Tempat (S + 在 + Tempat + Verb + O)",
        "stem": "Susunlah frasa-frasa acak berikut menjadi kalimat baku bahasa Mandarin yang menyatakan 'Adik laki-laki membaca buku di perpustakaan':\n(1) 看书 (kànshū)  (2) 弟弟 (dìdi)  (3) 在图书馆 (zài túshūguǎn)",
        "correct": "(2) - (3) - (1) : 弟弟在图书馆看书。 (Subjek + Keterangan Tempat di depan + Predikat Kata Kerja).",
        "distractors": [
            "(2) - (1) - (3) : 弟弟看书在图书馆。 (Menempatkan keterangan tempat di belakang predikat yang melanggar kaidah Mandarin).",
            "(1) - (2) - (3) : 看书弟弟在图书馆。 (Meletakkan kata kerja di awal mendahului subjek).",
            "(3) - (1) - (2) : 在图书馆看书弟弟。 (Meletakkan subjek di akhir kalimat).",
            "(1) - (3) - (2) : 看书在图书馆弟弟。 (Struktur acak tanpa kohesi gramatikal)."
        ],
        "formula": {
            "title": "STRUKTUR SINTAKSIS TEMPAT MANDARIN (介词短语作状语)",
            "latex": "\\mathbf{\\text{Subjek (弟弟)}} + \\mathbf{\\text{在 + Tempat (在图书馆)}} + \\mathbf{\\text{Verb + O (看书)}}",
            "legend": "• Aksi berlangsung di suatu wadah lokasi, sehingga keterangan tempat mendahului eksekusi perbuatan"
        },
        "hints": {
            "concept": "Rumus bahasa Mandarin: Subjek + 在 (zài) Tempat + Kata Kerja + Objek. Jadi: 弟弟在图书馆看书。",
            "execution": "Pilih urutan: (2) - (3) - (1)."
        }
    },
    {
        "id": "man-lat-e-13",
        "materi": "YUFA: KATA KERJA BANTU MODAL (XIǍNG VS YÀO)",
        "topic": "Perbedaan Derajat Keinginan: 想 (Xiǎng) vs 要 (Yào)",
        "stem": "Dalam percakapan di restoran, seorang pelanggan ingin menyatakan tekad pemesanan yang pasti:\n'服务员，我 ( ... ) 一碗牛肉面。'\nKata yang TEPAT untuk menyatakan pemesanan makanan dengan kehendak tegas dan berniat memesan adalah...",
        "correct": "要 (yào - menyatakan kehendak aktif/pasti menginginkan atau memesan sesuatu barang).",
        "distractors": [
            "想 (xiǎng - hanya bermakna angan-angan atau memikirkan dalam hati tanpa tindakan pemesanan langsung).",
            "会 (huì - menyatakan keterampilan kompetensi yang diperoleh dari proses belajar).",
            "能 (néng - menyatakan kemampuan fisik atau izin situasi kondisional).",
            "可以 (kěyǐ - menyatakan perizinan normatif dari pihak berwenang)."
        ],
        "formula": {
            "title": "DISTINGSI MODALITAS KEINGINAN (助动词「想」与「要」)",
            "latex": "\\begin{aligned} \\mathbf{\\text{想 (xiǎng):}} & \\text{Hasrat batin / Berangan-angan (Wish/Desire)} \\\\ \\mathbf{\\text{要 (yào):}} & \\text{Tekad pasti / Memesan barang konkret (Will/Order)} \\end{aligned}",
            "legend": "• Dalam transaksi kasir dan restoran, kata 要 digunakan untuk memilih menu pesanan"
        },
        "hints": {
            "concept": "Memesan makanan secara pasti di restoran memakai 要 (yào): 我要一碗牛肉面.",
            "execution": "Pilih: '要 (yào)'."
        }
    },
    {
        "id": "man-lat-e-14",
        "materi": "YUFA: KATA KERJA BANTU KEMAMPUAN (HUÌ VS NÉNG)",
        "topic": "Kemampuan Hasil Belajar (会 - Huì) vs Kemampuan Fisik/Kondisi (能 - Néng)",
        "stem": "Lengkapilah dua kalimat rumpang berikut:\n1) 他在中国学过汉语，所以他 ( A ) 说普通话。\n2) 他今天感冒嗓子疼，不 ( B ) 唱歌。\nKata bantu kemampuan yang TEPAT untuk ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: 会 (huì - kemahiran berbahasa hasil proses belajar), B: 能 (néng - kemampuan kondisi fisik saat ini).",
        "distractors": [
            "A: 能 (néng), B: 会 (huì) - terbalik esensi antara keterampilan belajar dan batasan fisik akibat sakit.",
            "A: 可以 (kěyǐ), B: 会 (huì) - kěyǐ menandai izin peraturan sosial.",
            "A: 会 (huì), B: 会 (huì) - mengabaikan faktor batasan fisiologis radang tenggorokan.",
            "A: 能 (néng), B: 能 (néng) - mengabaikan perbedaan domain perolehan ilmu bahasa."
        ],
        "formula": {
            "title": "DISTINGSI MODALITAS KEMAMPUAN (能力助动词「会」与「能」)",
            "latex": "\\begin{cases} \\mathbf{\\text{会 (huì):}} & \\text{Bisa karena belajar / berlatih (Bahasa, Berenang, Mengemudi)} \\\\ \\mathbf{\\text{能 (néng):}} & \\text{Mampu secara fisik / situasi objektif memungkinkan} \\end{cases}",
            "legend": "• Pemilahan fundamental epistemik kemampuan dalam gramatika Tionghoa"
        },
        "hints": {
            "concept": "Bisa bahasa Mandarin karena belajar -> 会 (huì). Tidak bisa nyanyi karena radang tenggorokan/fisik sakit -> 不能 (bù néng).",
            "execution": "Pilih: 'A: 会 (huì), B: 能 (néng)'."
        }
    },
    {
        "id": "man-lat-e-15",
        "materi": "YUFA: PREPOSISI RUTE & JARAK",
        "topic": "Struktur Menyatakan Jarak (A 离 B 很远 / 很近)",
        "stem": "Perhatikan kalimat rumpang mengenai jarak geografis berikut:\n'我家 ( ... ) 学校不太远，每天走五分钟就到了。'\nPreposisi yang TEPAT untuk menyatakan titik acuan jarak ('rumah saya dari sekolah...') adalah...",
        "correct": "离 (lí - preposisi yang menandai jarak spasial atau rentang waktu pemisah antar dua titik).",
        "distractors": [
            "从 (cóng - preposisi yang menandai titik tolak awal keberangkatan rute perjalanan fisik).",
            "到 (dào - preposisi yang menandai titik akhir tujuan destinasi kedatangan).",
            "在 (zài - preposisi yang menandai lokasi keberadaan tempat eksistensial).",
            "往 (wǎng - preposisi yang menandai orientasi arah pergerakan kompas)."
        ],
        "formula": {
            "title": "STRUKTUR JARAK SPASIAL (距离句式「离」)",
            "latex": "\\mathbf{A + \\text{离 (lí)} + B + \\text{很远 / 很近}} \\implies \\text{Titik } A \\text{ jauh/dekat dari titik } B",
            "legend": "• Dari titik acuan statis wajib menggunakan 离; 从 digunakan untuk titik tolak gerak dinamis"
        },
        "hints": {
            "concept": "Pola menyatakan jarak: A 离 (lí) B 很远/很近. Preposisi jarak adalah 离.",
            "execution": "Pilih: '离 (lí)'."
        }
    },
    {
        "id": "man-lat-e-16",
        "materi": "YUFA: KATA HUBUNG SEBAB AKIBAT DASAR",
        "topic": "Pasangan Konjungsi Sebab-Akibat (因为...所以...)",
        "stem": "Lengkapilah kalimat majemuk kausalitas berikut dengan pasangan konjungsi yang TEPAT:\n'( A ) 今天下大雨，( B ) 足球比赛推迟了。'",
        "correct": "A: 因为 (yīnwèi - karena), B: 所以 (suǒyǐ - oleh sebab itu / maka dari itu).",
        "distractors": [
            "A: 虽然 (suīrán), B: 但是 (dànshì) - pasangan konjungsi pertentangan (walaupun...tetapi...).",
            "A: 不但 (búdàn), B: 而且 (érqiě) - pasangan konjungsi penambahan kumulatif (bukan hanya...bahkan...).",
            "A: 如果 (rúguǒ), B: 就 (jiù) - pasangan konjungsi pengandaian bersyarat (jika...maka...).",
            "A: 既 (jì), B: 又 (yòu) - pasangan konjungsi kesetaraan sifat ganda (baik...maupun...)."
        ],
        "formula": {
            "title": "KONJUNGSI KAUSALITAS SINTAKSIS (因果复句)",
            "latex": "\\mathbf{\\text{因为 (yīnwèi) } + \\text{Alasan}} \\dots \\mathbf{\\text{所以 (suǒyǐ) } + \\text{Akibat}} \\implies \\text{Karena } \\dots \\text{ oleh sebab itu } \\dots",
            "legend": "• Hubungan sebab akibat eksplisit yang berpasangan secara korelatif"
        },
        "hints": {
            "concept": "Hubungan karena hujan lebat maka pertandingan ditunda adalah kausalitas: 因为 (yīnwèi)... 所以 (suǒyǐ)...",
            "execution": "Pilih opsi: 'A: 因为 (yīnwèi), B: 所以 (suǒyǐ)'."
        }
    },
    {
        "id": "man-lat-e-17",
        "materi": "YUFA: KATA HUBUNG KONTRASTIF ADVERSATIF",
        "topic": "Pasangan Konjungsi Pertentangan (虽然...但是...)",
        "stem": "Perhatikan kalimat rumpang berikut:\n'( A ) 汉语汉字很难写，( B ) 我觉得非常有意思。'\nPasangan kata hubung yang TEPAT untuk menyatakan 'Meskipun aksara Hanzi sangat sulit ditulis, tetapi saya merasa sangat menarik' adalah...",
        "correct": "A: 虽然 (suīrán), B: 但是 (dànshì).",
        "distractors": [
            "A: 因为 (yīnwèi), B: 所以 (suǒyǐ) - menyatakan hubungan sebab akibat lurus yang keliru secara logika.",
            "A: 如果 (rúguǒ), B: 就 (jiù) - menyatakan hubungan syarat hipotetis masa depan.",
            "A: 只要 (zhǐyào), B: 就 (jiù) - menyatakan syarat cukup mutlak.",
            "A: 无论 (wúlùn), B: 都 (dōu) - menyatakan kondisi tanpa kecuali."
        ],
        "formula": {
            "title": "KONJUNGSI KONTRASTIF MANDARIN (转折复句)",
            "latex": "\\mathbf{\\text{虽然 (suīrán) } + \\text{Klausa Konsesif}} \\dots \\mathbf{\\text{但是 (dànshì) } + \\text{Klausa Kontras}}",
            "legend": "• Menautkan fakta tantangan objektif dengan antusiasme subjektif penutur"
        },
        "hints": {
            "concept": "Meskipun sulit, tetapi menarik: 虽然 (suīrán)... 但是 (dànshì)...",
            "execution": "Pilih: 'A: 虽然 (suīrán), B: 但是 (dànshì)'."
        }
    },
    {
        "id": "man-lat-e-18",
        "materi": "YUFA: TINGKAT SUPERLATIF SIFAT",
        "topic": "Penggunaan Kata Keterangan Derajat Tertinggi (最 - Zuì)",
        "stem": "Dalam sebuah keluarga, ketiga anak memiliki usia yang berbeda-beda. Kalimat manakah yang TEPAT untuk menyatakan 'Kakak perempuan tertua adalah yang paling tinggi postur tubuhnya'?",
        "correct": "姐姐的个子最高。 (Jiějie de gèzi zuì gāo - postur badan kakak perempuan adalah yang paling tinggi).",
        "distractors": [
            "姐姐的个子很最高。 (Dilarang menggabungkan kata keterangan 'hěn' dengan kata tingkat 'zuì' secara bersamaan).",
            "姐姐的个子极高了。 (Struktur 'jí le' menandai derajat sangat ekstrem, bukan perbandingan superlatif kelompok).",
            "姐姐的个子比最高。 (Penggabungan partikel komparatif bǐ dengan zuì yang menyalahi sintaksis).",
            "姐姐的个子太高。 (Tài gāo menandai keberlebihan yang melebihi batas toleransi wajar)."
        ],
        "formula": {
            "title": "DERAJAT SUPERLATIF MANDARIN (最高级状语「最」)",
            "latex": "\\mathbf{\\text{最 (zuì)}} + \\mathbf{\\text{Kata Sifat (高)}} \\implies \\text{Paling } [\\text{Sifat}] \\quad (\\cancel{\\text{很最}}, \\cancel{\\text{太最}})",
            "legend": "• Tidak boleh didampingi adverbia derajat lain (seperti hěn atau fēicháng)"
        },
        "hints": {
            "concept": "Superlatif (paling tinggi) adalah 最 (zuì) + Kata Sifat: 最高 (zuì gāo). Tidak boleh ditambah 很 di depan 最.",
            "execution": "Pilih: '姐姐的个子最高。'."
        }
    },
    {
        "id": "man-lat-e-19",
        "materi": "YUFA: PREPOSISI RUTE ARAH GERAK",
        "topic": "Penggunaan Preposisi Arah (从...到... - Cóng... Dào...)",
        "stem": "Lengkapilah kalimat durasi dan perjalanan berikut:\n'我们学校每天 ( A ) 早上八点 ( B ) 下午四点上课。'\nPasangan preposisi rentang waktu yang TEPAT untuk mengisi ( A ) 'dari' dan ( B ) 'sampai' adalah...",
        "correct": "A: 从 (cóng), B: 到 (dào).",
        "distractors": [
            "A: 离 (lí), B: 到 (dào) - lí tidak digunakan untuk rentang durasi sekuensial jam harian.",
            "A: 在 (zài), B: 去 (qù) - qù adalah kata kerja pergi, bukan penanda batas waktu tiba.",
            "A: 往 (wǎng), B: 向 (xiàng) - keduanya merupakan preposisi arah mata angin kompas.",
            "A: 自 (zì), B: 于 (yú) - register sastra klasik kuno yang tidak selaras dengan bahasa modern sederhana."
        ],
        "formula": {
            "title": "RENTANG WAKTU DAN RUANG (时空起点与终点)",
            "latex": "\\mathbf{\\text{从 (cóng) } + \\text{Titik Awal}} \\dots \\mathbf{\\text{到 (dào) } + \\text{Titik Akhir}} \\implies \\text{Dari } \\dots \\text{ Sampai } \\dots",
            "legend": "• Berlaku serbaguna untuk rentang jam (waktu) maupun jarak stasiun (spasial)"
        },
        "hints": {
            "concept": "Dari jam 8 sampai jam 4: 从 (cóng) 8点 到 (dào) 4点.",
            "execution": "Pilih: 'A: 从 (cóng), B: 到 (dào)'."
        }
    },
    {
        "id": "man-lat-e-20",
        "materi": "YUFA: WAKTU RELATIF KRONOLOGIS",
        "topic": "Penggunaan Waktu Sebelum (...以前) dan Sesudah (...以后)",
        "stem": "Perhatikan aturan kegiatan belajar berikut:\n'上课 ( A )，我们要认真预习生词。\n 毕业 ( B )，我打算去中国留学。'\nKata penunjuk sekuensi waktu 'sebelum' ( A ) dan 'setelah' ( B ) yang TEPAT berturut-turut adalah...",
        "correct": "A: 以前 (yǐqián - sebelum kelas dimulai), B: 以后 (yǐhòu - sesudah lulus kelak).",
        "distractors": [
            "A: 以后 (yǐhòu), B: 以前 (yǐqián) - terbalik total urutan kronologis belajarnya.",
            "A: 之前 (zhīqián), B: 以前 (yǐqián) - keduanya sama-sama bermakna sebelum.",
            "A: 过去 (guòqù), B: 将来 (jiānglái) - kata benda mandiri yang berarti masa lalu dan masa depan.",
            "A: 刚才 (gāngcái), B: 现在 (xiànzài) - baru saja dan sekarang."
        ],
        "formula": {
            "title": "KRONOLOGI RELATIF SINTAKSIS (时间后置短语)",
            "latex": "\\begin{cases} \\text{Aktivitas} + \\mathbf{\\text{以前 (yǐqián)}} & \\implies \\text{Sebelum melakukan aktivitas} \\\\ \\text{Aktivitas} + \\mathbf{\\text{以后 (yǐhòu)}} & \\implies \\text{Sesudah menyelesaikan aktivitas} \\end{cases}",
            "legend": "• Kata yǐqián dan yǐhòu diletakkan SETELAH kata kerja atau peristiwa patokan"
        },
        "hints": {
            "concept": "Sebelum kelas = 上课以前. Sesudah lulus = 毕业以后.",
            "execution": "Pilih opsi: 'A: 以前 (yǐqián), B: 以后 (yǐhòu)'."
        }
    },
    {
        "id": "man-lat-e-21",
        "materi": "JIĀOJÌ: SALAM DAN KESANTUNAN HARIAN",
        "topic": "Respons Santun Ucapan Terima Kasih (不客气 - Bú Kèqi)",
        "stem": "Ketika seseorang membantu mengambilkan buku yang terjatuh dan berkata '谢谢你！' (*Xièxie nǐ!*), jawaban balasan yang PALING LAZIM dan sopan diucapkan adalah...",
        "correct": "不客气 (Bú kèqi - sama-sama / jangan sungkan-sungkan).",
        "distractors": [
            "没关系 (Méi guānxi - jawaban balasan yang khusus untuk merespons permohonan maaf duìbuqǐ).",
            "对不起 (Duìbuqǐ - ungkapan meminta maaf atas kesalahan yang tidak relevan).",
            "请问 (Qǐngwèn - ungkapan permisi sebelum mengajukan pertanyaan kepada orang lain).",
            "不用 (Búyòng - penolakan kasar yang bernada ketus jika diucapkan sendiri tanpa konteks)."
        ],
        "formula": {
            "title": "PASANGAN KOMUNIKASI SOSIAL MANDARIN (礼貌应答系统)",
            "latex": "\\begin{aligned} \\text{Terima Kasih: } \\mathbf{\\text{谢谢 (Xièxie)}} & \\longleftrightarrow \\mathbf{\\text{不客气 (Bú kèqi) / 不用谢 (Búyòng xiè)}} \\\\ \\text{Minta Maaf: } \\text{对不起 (Duìbuqǐ)} & \\longleftrightarrow \\text{没关系 (Méi guānxi)} \\end{aligned}",
            "legend": "• Menghindari kerancuan antara respons rasa terima kasih dan respons permohonan maaf"
        },
        "hints": {
            "concept": "Balasan dari 谢谢 (Xièxie) adalah 不客气 (Bú kèqi). (Sedangkan 没关系 adalah balasan untuk 对不起).",
            "execution": "Pilih: '不客气 (Bú kèqi)'."
        }
    },
    {
        "id": "man-lat-e-22",
        "materi": "JIĀOJÌ: MEMOHON MAAF DAN BALASANNYA",
        "topic": "Respons Santun Permohonan Maaf (没关系 - Méi Guānxi)",
        "stem": "Seorang anak tidak sengaja menginjak kaki temannya di dalam bus dan berujar:\n'对不起，我不是故意的！' (*Duìbuqǐ, wǒ bú shì gùyì de!*)\nBalasan yang TEPAT dan beretika diucapkan oleh temannya adalah...",
        "correct": "没关系 (Méi guānxi - tidak apa-apa / tidak masalah).",
        "distractors": [
            "不客气 (Bú kèqi - balasan terima kasih yang keliru dipakai untuk merespons minta maaf).",
            "谢谢 (Xièxie - mengucapkan terima kasih saat kakinya terinjak).",
            "再见 (Zàijiàn - ucapan selamat tinggal saat hendak berpisah).",
            "慢走 (Màn zǒu - ucapan hati-hati di jalan kepada tamu yang berpamitan)."
        ],
        "formula": {
            "title": "ETIKA MERESPONS PERMINTAAN MAAF (道歉应答作法)",
            "latex": "\\mathbf{\\text{对不起 (Duìbuqǐ / Maaf)}} \\xrightarrow{\\text{Balasan Baku}} \\mathbf{\\text{没关系 (Méi guānxi / Tidak apa-apa)}}",
            "legend": "• Meredakan ketegangan psikologis antarpribadi di ruang publik"
        },
        "hints": {
            "concept": "Balasan permohonan maaf 对不起 (Duìbuqǐ) adalah 没关系 (Méi guānxi).",
            "execution": "Pilih: '没关系 (Méi guānxi)'."
        }
    },
    {
        "id": "man-lat-e-23",
        "materi": "JIĀOJÌ: MENANYAKAN HARGA DAN TAWAR-MENAWAR",
        "topic": "Pertanyaan Harga Barang di Pasar Tradisional (多少钱 - Duōshao Qián)",
        "stem": "Saat berbelanja buah apel di pasar buah, kalimat pertanyaan yang TEPAT diajukan pembeli kepada penjual untuk menanyakan 'Berapa harga satu kilogram buah apel ini?' adalah...",
        "correct": "这个苹果一斤多少钱？ (Zhè ge píngguǒ yì jīn duōshao qián? - buah apel ini satu jin/setengah kilo berapa harganya?).",
        "distractors": [
            "这个苹果叫什么名字？ (Menanyakan siapa nama apel tersebut).",
            "这个苹果在哪里买的？ (Menanyakan di mana apel tersebut dibeli sebelumnya).",
            "这个苹果好吃吗？ (Hanya menanyakan apakah rasa apelnya enak tanpa menanyakan nominal uang).",
            "这个苹果是谁的？ (Menanyakan siapa pemilik buah apel tersebut)."
        ],
        "formula": {
            "title": "POLA TRANSAKSI PERTANYAAN HARGA (询问价格句式)",
            "latex": "\\mathbf{\\text{Barang}} + \\mathbf{\\text{Kuantitas}} + \\mathbf{\\text{多少钱 (duōshao qián)}} \\implies \\text{Berapa harga } [\\text{Barang}]?",
            "legend": "• Jin (斤) adalah satuan berat tradisional Tiongkok (1 jin = 500 gram)"
        },
        "hints": {
            "concept": "Menanyakan harga barang menggunakan kata tanya '多少钱' (duōshao qián).",
            "execution": "Pilih: '这个苹果一斤多少钱？'."
        }
    },
    {
        "id": "man-lat-e-24",
        "materi": "JIĀOJÌ: ETIKA MENYAPA SAAT PERTAMA KALI BERTEMU",
        "topic": "Ungkapan Senang Berkenalan (很高兴认识你 - Hěn Gāoxìng Rènshi Nǐ)",
        "stem": "Setelah memperkenalkan diri kepada teman baru asal Tiongkok, ungkapan kesantunan yang TEPAT diucapkan untuk menyatakan 'Senang berkenalan dengan Anda' adalah...",
        "correct": "很高兴认识你！ (Hěn gāoxìng rènshi nǐ! - sangat senang dapat mengenal Anda!).",
        "distractors": [
            "你叫什么名字？ (Pertanyaan interogatif yang diajukan sebelum perkenalan selesai).",
            "祝你生日快乐！ (Ucapan selamat ulang tahun yang tidak relevan dengan konteks perkenalan).",
            "欢迎光临！ (Ucapan sambutan selamat datang yang dilafalkan pelayan toko kepada pembeli).",
            "一路顺风！ (Ucapan doa selamat jalan kepada pelancong yang hendak bepergian jauh)."
        ],
        "formula": {
            "title": "UNGKAPAN SALAM PERKENALAN PERTAMA (结识新友礼貌用语)",
            "latex": "\\mathbf{\\text{很高兴 (hěn gāoxìng / sangat senang)}} + \\mathbf{\\text{认识你 (rènshi nǐ / mengenal Anda)}}",
            "legend": "• Frasa baku pembangun hubungan keakraban sosial awal (Guanxi)"
        },
        "hints": {
            "concept": "Senang berkenalan dengan Anda dalam bahasa Mandarin adalah '很高兴认识你！' (Hěn gāoxìng rènshi nǐ!).",
            "execution": "Pilih: '很高兴认识你！'."
        }
    },
    {
        "id": "man-lat-e-25",
        "materi": "JIĀOJÌ & BUDAYA: SALAM KEPULANGAN TAMU",
        "topic": "Etika Melepas Tamu Berpamitan Pulang (慢走 - Màn Zǒu)",
        "stem": "Ketika seorang tamu selesai berkunjung ke rumah dan berpamitan hendak pulang (*'我先走了'*), tuan rumah yang beretika sopan di Tiongkok biasanya mengantar hingga ke pintu dan mengucapkan...",
        "correct": "慢走！ (Màn zǒu! - jalan perlahan dan hati-hati di jalan!).",
        "distractors": [
            "快走！ (Kuài zǒu! - perintah kasar yang berarti 'bersegeralah angkat kaki / enyahlah').",
            "不送！ (Bú sòng! - ungkapan dingin yang menyiratkan keengganan mengantar tamu).",
            "别走！ (Bié zǒu! - memohon secara dramatis agar tamu jangan pergi).",
            "请坐！ (Qǐng zuò! - mempersilakan duduk yang hanya diucapkan saat tamu baru tiba)."
        ],
        "formula": {
            "title": "ETIKA PELEPASAN TAMU TIONGHOA (送客礼仪用语)",
            "latex": "\\text{Tamu Pamit: } \\text{我先走了} \\xrightarrow{\\text{Respons Tuan Rumah}} \\mathbf{\\text{慢走 (màn zǒu / Jalan Hati-hati)}}",
            "legend": "• Kata 'màn' (pelan) mengandung doa keselamatan agar tamu tidak terantuk atau celaka di jalan"
        },
        "hints": {
            "concept": "Melepas tamu yang pulang, tuan rumah mengucapkan '慢走' (màn zǒu - jalan hati-hati/pelan-pelan).",
            "execution": "Pilih: '慢走！ (Màn zǒu!)'."
        }
    }
]
