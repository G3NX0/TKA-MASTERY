# -*- coding: utf-8 -*-
"""
BAHASA JEPANG - PAKET SOAL LATIHAN SULIT (HARD / HOTS) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / JLPT N4+-N3 Dasar
Distribusi:
- 8 Butir: Bunpou Lanjutan & Keigo (Ukemi Pasif Merugikan, Shieki Kausatif, Shieki-Ukemi, Sonkeigo/Kenjougo, ~noni vs ~node, ~tameni vs ~youni)
- 10 Butir: Wacana Analitis & Dokkai Kompleks (Shoushikoureika, etika Omotenashi, Aizuchi, infografis & perbandingan teks)
- 7 Butir: Pragmatik Komunikasi Tingkat Tinggi (Register formal bisnis, Meishi Koukan, ~te itadakemasen ka, evaluasi implikatur kesantunan)
"""

BAHASA_JEPANG_HARD_ITEMS = [
    {
        "id": "jpn-lat-h-01",
        "materi": "BUNPOU LANJUTAN: PASIF MERUGIKAN (MEIWAKU UKEMI)",
        "topic": "Analisis Struktur Pasif Kerugian Pribadi (迷惑の受身)",
        "stem": "Perhatikan kalimat bahasa Jepang berikut:\n'昨日、傘を 持たずに 出かけたら、途中で 雨に ( ... )、風邪を ひいてしまいました。'\nBentuk konjugasi verba pasif yang TEPAT untuk mengekspresikan bahwa subjek 'mengalami kerugian/kesusahan karena kehujanan di jalan' adalah...",
        "correct": "ふられて (Furarete - bentuk pasif ukemi dari furimasu yang menyatakan rasa terganggu/menderita akibat turunnya hujan).",
        "distractors": [
            "ふって (Futte - bentuk te aktif biasa yang tidak mampu menyatakan nuansa kerugian atau penderitaan subjek).",
            "ふらせて (Furasete - bentuk kausatif shieki yang keliru karena bermakna subjek yang menyebabkan hujan turun).",
            "ふれられて (Furerarete - bentuk pasif potensial rancu yang menyalahi kaidah konjugasi verba godan).",
            "ふらせられて (Furaserarete - bentuk kausatif-pasif berlebihan yang tidak logis diterapkan pada fenomena cuaca alam)."
        ],
        "formula": {
            "title": "KONSEP PASIF MERUGIKAN (迷惑の受身 / 間接受身)",
            "latex": "\\mathbf{S \\text{ は }} + \\mathbf{\\text{Peristiwa Alam/Orang Lain に}} + \\mathbf{V\\text{-られる (Ukemi)}} \\implies \\text{Subjek menderita akibat } V",
            "legend": "• Hujan (雨に) memposisikan alam sebagai pelaku pemicu ketidaknyamanan fisik subjek"
        },
        "hints": {
            "concept": "Fenomena alam yang menyebabkan kesusahan bagi subjek diungkapkan dengan pasif merugikan (meiwaku ukemi): 雨に降られる (ame ni furareru). Te-form: ふられて.",
            "execution": "Pilih: 'ふられて (Furarete)'."
        }
    },
    {
        "id": "jpn-lat-h-02",
        "materi": "BUNPOU LANJUTAN: BENTUK KAUSATIF (SHIEKI DOUSHI)",
        "topic": "Fungsi Kausatif Paksaan vs Kausatif Izin (使役動詞: せる / させる)",
        "stem": "Ibu berkata mengenai pendisiplinan anaknya di rumah:\n'子どもが 野菜を 嫌がりますが、健康の ために 毎日 野菜を ( ... ) います。'\nBentuk verba kausatif yang TEPAT untuk menyatakan tindakan ibu 'membuat/menyuruh anak memakan sayur demi kesehatan' adalah...",
        "correct": "たべさせて (Tabesasete - bentuk kausatif dari verba ichidan taberu -> tabesaseru -> tabesasete imasu).",
        "distractors": [
            "たべられて (Taberarete - bentuk pasif yang bermakna ibu yang dimakan oleh anak).",
            "たべさせられて (Tabesaserarete - bentuk kausatif-pasif yang bermakna ibu yang dipaksa memakan sayur).",
            "たべてもらって (Tabetemoratte - bentuk menerima jasa bantuan yang tidak selaras dengan relasi kuasa orang tua-anak).",
            "たべないで (Tabenaide - bentuk permohonan negatif yang bertentangan dengan tujuan hidup sehat)."
        ],
        "formula": {
            "title": "PEMBENTUKAN VERBA KAUSATIF (使役形「〜せる・〜させる」)",
            "latex": "\\begin{aligned} \\text{Golongan II (Ichidan): } & \\text{食べる} \\to \\mathbf{\\text{食べさせる (Tabesaseru)}} \\\\ \\text{Makna: } & \\text{Menyuruh / Membiarkan orang lain melakukan aksi } V \\end{aligned}",
            "legend": "• Ibu memegang otoritas volisional penuh untuk menginstruksikan anak mengonsumsi gizi"
        },
        "hints": {
            "concept": "Menyuruh orang lain makan adalah kausatif (shieki). Verba taberu (Golongan 2) berubah menjadi 食べさせる (tabesaseru) -> たべさせて.",
            "execution": "Pilih: 'たべさせて (Tabesasete)'."
        }
    },
    {
        "id": "jpn-lat-h-03",
        "materi": "BUNPOU LANJUTAN: KAUSATIF-PASIF (SHIEKI UKEMI)",
        "topic": "Menyatakan Keterpaksaan Melakukan Sesuatu di Bawah Tekanan (使役受身)",
        "stem": "Ken menceritakan pengalamannya saat pesta penyambutan mahasiswa baru:\n'お酒が あまり 飲めないのに、先輩に 無理に ビールを ( ... )、本当に 困りました。'\nBentuk verba kausatif-pasif yang TEPAT untuk mengungkapkan bahwa Ken 'dipaksa meminum bir oleh seniornya' adalah...",
        "correct": "のまされて (Nomasarete - bentuk kausatif-pasif ringkas dari nomu -> nomaserareru / nomasareru yang bermakna dipaksa minum).",
        "distractors": [
            "のませて (Nomasete - bentuk kausatif murni yang keliru karena menyiratkan Ken yang mencekoki senior).",
            "のまれて (Nomarete - bentuk pasif biasa yang tidak menonjolkan aspek pemaksaan kehendak).",
            "のんで (Nonde - bentuk aktif biasa yang tidak mencerminkan situasi tertekan tanpa daya).",
            "のまないで (Nomanaide - bentuk negatif yang bertolak belakang dengan fakta bahwa bir tersebut terlanjur diminum)."
        ],
        "formula": {
            "title": "BENTUK KAUSATIF-PASIF KETERPAKSAAN (使役受身の短縮形)",
            "latex": "\\text{飲む (nomu)} \\xrightarrow{\\text{Kausatif-Pasif Ringkas}} \\mathbf{\\text{飲まされる (nomasareru)}} \\xrightarrow{\\text{Te-form}} \\mathbf{\\text{飲まされて}}",
            "legend": "• Mengekspresikan penderitaan psikologis subjek yang dipaksa tunduk pada otoritas pihak luar"
        },
        "hints": {
            "concept": "Pola dipaksa melakukan perbuatan oleh orang lain adalah Shieki-Ukemi. Nomu -> Nomasareru -> のまされて.",
            "execution": "Pilih opsi: 'のまされて (Nomasarete)'."
        }
    },
    {
        "id": "jpn-lat-h-04",
        "materi": "BUNPOU LANJUTAN: KEIGO (SONKEIGO)",
        "topic": "Bentuk Kata Kerja Hormat Khusus untuk Pihak Atasan (尊敬語)",
        "stem": "Sekretaris perusahaan berbicara kepada klien tamu mengenai aktivitas Direktur Utama (Shachou):\n'社長は たった今、会議室へ ( ... ) ました。少々 お待ちください。'\nVerba Sonkeigo bentuk hormat khusus dari '行きました' (pergi) yang TEPAT untuk menghormati direktur utama adalah...",
        "correct": "いらっしゃい (Irasshai - bentuk Sonkeigo khusus dari ikimasu, kimasu, dan imasu).",
        "distractors": [
            "まいり (Mairi - bentuk Kenjougo rendah hati yang hanya boleh dipakai untuk diri sendiri atau orang dalam).",
            "もうし (Moushi - bentuk Kenjougo yang bermakna berbicara/bernama untuk merendahkan diri).",
            "いただき (Itadaki - bentuk Kenjougo untuk menerima pemberian atau makan dan minum).",
            "おめにかかり (Omenikakari - bentuk Kenjougo untuk bertemu dengan seseorang yang dihormati)."
        ],
        "formula": {
            "title": "DISTINGSI SONKEIGO VS KENJOUGO (尊敬語と謙譲語の厳格な対立)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Sonkeigo (Hormat Subjek Atasan):}} & \\text{行く / 来る / いる} \\implies \\mathbf{\\text{いらっしゃる (Irassharu)}} \\\\ \\mathbf{\\text{Kenjougo (Merendahkan Pihak Sendiri):}} & \\text{行く / 来る} \\implies \\text{参る (まいる - Mairu)} \\end{aligned}",
            "legend": "• Menjaga jarak martabat sosial atasan (Shachou) saat berkomunikasi dengan mitra eksternal"
        },
        "hints": {
            "concept": "Subjek adalah Shachou (Direktur Utama/Atasan). Kata kerja yang meninggikan subjek (Sonkeigo) dari ikimashita adalah 'いらっしゃいました'.",
            "execution": "Pilih: 'いらっしゃい (Irasshai)'."
        }
    },
    {
        "id": "jpn-lat-h-05",
        "materi": "BUNPOU LANJUTAN: KEIGO (KENJOUGO)",
        "topic": "Bentuk Kata Kerja Rendah Hati Khusus saat Menyapa Klien (謙譲語: 申す & 参る)",
        "stem": "Saat seorang staf sales memperkenalkan diri di hadapan direksi perusahaan mitra bisnis:\n'はじめまして。わたくし、ABC商事の 田中と ( ... )。どうぞ よろしくお願い申し上げます。'\nVerba Kenjougo yang TEPAT untuk menyebut nama diri sendiri secara rendah hati dan sangat santun adalah...",
        "correct": "もうします (Moushimasu - bentuk Kenjougo dari verba iimasu untuk menyebut identitas diri sendiri).",
        "distractors": [
            "おっしゃいます (Osshaimasu - bentuk Sonkeigo yang dilarang keras digunakan untuk diri sendiri karena meninggikan diri).",
            "いらっしゃいます (Irasshaimasu - bentuk Sonkeigo yang hanya berlaku untuk subjek lawan bicara atau pihak ketiga yang dihormati).",
            "なさいます (Nasaimasu - bentuk Sonkeigo dari shimasu yang meninggikan perbuatan orang lain).",
            "ぞんじます (Zonjimasu - bentuk Kenjougo dari shitte imasu / omoimasu yang bermakna mengetahui atau mengira)."
        ],
        "formula": {
            "title": "KENJOUGO PERKENALAN IDENTITAS (自己紹介の謙譲語)",
            "latex": "\\text{Nama Sendiri } + \\text{と } + \\mathbf{\\text{申します (もうします - Moushimasu)}}",
            "legend": "• Dilarang keras menggunakan Sonkeigo (seperti ossharu) terhadap tindakan diri sendiri"
        },
        "hints": {
            "concept": "Menyebut nama diri sendiri kepada mitra kerja secara rendah hati wajib menggunakan Kenjougo: 田中と申します (Tanaka to moushimasu).",
            "execution": "Pilih opsi: 'もうします (Moushimasu)'."
        }
    },
    {
        "id": "jpn-lat-h-06",
        "materi": "BUNPOU LANJUTAN: KONJUNGSI ADVERSATIF KONTRASTIF",
        "topic": "Distingsi Nuansa ~Noni (〜のに: Kekecewaan) vs ~Keredomo (〜けれども)",
        "stem": "Cermati kalimat rumpang yang memuat nuansa ketidakpuasan subjektif pembicara berikut:\n'あんなに 一生懸命 勉強した ( ... )、試験の 点数は よくありませんでした。本当に 悔しいです。'\nPartikel konjungsi yang TEPAT untuk menautkan ekspektasi tinggi dengan hasil yang mengecewakan secara emosional adalah...",
        "correct": "のに (noni - partikel penghubung pertentangan yang sarat muatan emosi kecewa, heran, atau menyesal).",
        "distractors": [
            "ので (node - partikel penanda alasan logis objektif yang menyatakan hubungan sebab-akibat lurus).",
            "から (kara - partikel kausalitas subjektif yang tidak mengekspresikan kontradiksi hasil).",
            "なら (nara - partikel penanda topik kondisional kontekstual).",
            "ても (temo - bentuk konsesif netral yang kurang tajam dalam memancarkan kekecewaan batin personal)."
        ],
        "formula": {
            "title": "PRAGMATIK EMOSIONAL KONJUNGSI NONI (逆接の「のに」の感情性)",
            "latex": "\\mathbf{\\text{Ekspektasi (Kerja Keras)}} + \\mathbf{\\text{のに (Padahal)}} + \\mathbf{\\text{Fakta Mengecewakan (Nilai Buruk)}} \\implies \\text{Emosi Kesal / Kecewa}",
            "legend": "• Berbeda dari 'keredomo' yang netral, 'noni' selalu menyiratkan kontradiksi yang menyakitkan hati"
        },
        "hints": {
            "concept": "Pola 'padahal sudah belajar sekuat tenaga, tetapi nilainya tidak bagus' mengandung rasa kecewa/kesal. Partikel yang tepat adalah 'のに' (noni).",
            "execution": "Pilih: 'のに (noni)'."
        }
    },
    {
        "id": "jpn-lat-h-07",
        "materi": "BUNPOU LANJUTAN: POLA TUJUAN INTENSIONAL VS KONDISIONAL",
        "topic": "Distingsi Sintaksis ~Tame ni (〜ために) vs ~You ni (〜ように)",
        "stem": "Perhatikan dua kalimat tujuan berikut ini:\n1) 新しい 車を 買う ( A )、毎月 貯金しています。\n2) 後ろの 人にも よく 見える ( B )、字を 大きく 書きました。\nUnsur gramatikal yang TEPAT untuk mengisi posisi ( A ) yang melibatkan verba volisional manusia dan ( B ) yang melibatkan verba non-volisional keadaan (melihat/terlihat) berturut-turut adalah...",
        "correct": "A: ために (Tame ni - tujuan aksi kehendak sadar), B: ように (You ni - harapan agar tercipta kondisi keadaan baru).",
        "distractors": [
            "A: ように, B: ために (terbalik fungsi antara verba tindakan intensional dan verba potensial/keadaan).",
            "A: ために, B: ために (kedua kalimat disamakan sebagai tindakan volisional tanpa mempertimbangkan kata mieru).",
            "A: ように, B: ように (kedua kalimat disamakan sebagai perubahan kondisi keadaan).",
            "A: のに, B: ので (mengganti klausa tujuan dengan klausa kontras dan kausalitas yang merusak makna)."
        ],
        "formula": {
            "title": "DISTINGSI KLAUSA TUJUAN (目的表現の統語論)",
            "latex": "\\begin{aligned} \\mathbf{V_{\\text{Volisional}} \\text{ (辞書形)}} + \\mathbf{\\text{ために}} & \\implies \\text{Tujuan Tindakan Kehendak (買うために)} \\\\ \\mathbf{V_{\\text{Non-Volisional / Potensial}} \\text{ (可能形・無意志)}} + \\mathbf{\\text{ように}} & \\implies \\text{Demi Tercapainya Kondisi (見えるように)} \\end{aligned}",
            "legend": "• Verba 見える (mieru) adalah kata kerja keadaan/potensial, sehingga wajib berpasangan dengan ように"
        },
        "hints": {
            "concept": "Kalimat 1 memakai verba tindakan sadar (kau/membeli) -> ために. Kalimat 2 memakai verba potensi/keadaan (mieru/terlihat) -> ように.",
            "execution": "Pilih opsi: 'A: ために, B: ように'."
        }
    },
    {
        "id": "jpn-lat-h-08",
        "materi": "BUNPOU LANJUTAN: DERAJAT KEPASTIAN LOGIS",
        "topic": "Kepastian Logis Berdasar Bukti Valid (~Hazu da vs ~Kamoshirenai)",
        "stem": "Analisis dialog penentuan keberangkatan kereta berikut:\nTanaka: '鈴木さんは もう 駅に 着きましたか。'\nYamada: 'はい、彼は 朝6時の 新幹線に 乗ったので、今ごろは もう 東京に ( ... ) です。'\nUngkapan derajat kepastian logis yang TEPAT diucapkan Yamada ('seharusnya sudah tiba di Tokyo berdasarkan perhitungan jam') adalah...",
        "correct": "着いているはず (Tsuite iru hazu - keyakinan logis berdasar fakta pasti bahwa subjek telah naik Shinkansen jam 6 pagi).",
        "distractors": [
            "着くかもしれない (Tsuku kamoshirenai - kemungkinan samar berbobot 50% atau kurang yang meragukan fakta).",
            "着くつもり (Tsuku tsumori - niat pribadi yang tidak logis diucapkan oleh pihak ketiga mengenai tibanya orang lain).",
            "着くようだ (Tsuku youda - dugaan sensorik yang kurang tepat dipakai untuk kesimpulan jadwal pasti).",
            "着かないはず (Tsukanai hazu - kesimpulan negatif yang bertentangan dengan perhitungan waktu perjalanan)."
        ],
        "formula": {
            "title": "MODALITAS KEPASTIAN RASIONAL (確信の「はずだ」)",
            "latex": "\\mathbf{\\text{Fakta Premis (Naik Kereta Jam 6)}} \\xrightarrow{\\text{Kalkulasi Rasional}} \\mathbf{V\\text{-辞書形 / ている}} + \\mathbf{\\text{はずです (Pasti / Semestinya)}}",
            "legend": "• Mengindikasikan probabilitas rasional sangat tinggi mendekati kepastian matematis"
        },
        "hints": {
            "concept": "Ada alasan objektif yang jelas (naik Shinkansen jam 6 pagi), maka kesimpulan logis 'semestinya/pasti sudah sampai' memakai ~はずです (hazu desu).",
            "execution": "Pilih: '着いているはず (Tsuite iru hazu)'."
        }
    },
    {
        "id": "jpn-lat-h-09",
        "materi": "DOKKAI ANALITIS: ISU DEMOGRAFI JEPANG",
        "topic": "Fenomena Penurunan Kelahiran dan Penuaan Populasi (少子高齢化)",
        "stem": "Bacalah teks analisis sosiologis Jepang berikut:\n--------------------------------------------------\n日本は 現在、「少子高齢化（しょうしこうれいか）」という 深刻な 社会問題に 直面しています。子どもの 生まれる 数が 減る 一方で、65歳以上の 高齢者の 割合が 年々 増加しています。この 現象に より、将来の 労働力不足が 心配されており、年金や 医療などの 社会保障費の 負担も 若い世代に 重く のしかかっています。この 問題を 解決するために、政府は 育児休業の 推進や 外国人労働者の 受け入れ拡大、さらには 介護ロボットの 開発など 多様な 対策を 進めています。\n--------------------------------------------------\nBerdasarkan wacana di atas, apa konsekuensi langsung dari fenomena *shoushikoureika* terhadap generasi muda di Jepang?",
        "correct": "Generasi muda menghadapi beban biaya jaminan sosial yang semakin berat serta ancaman krisis kekurangan tenaga kerja produktif di masa depan.",
        "distractors": [
            "Generasi muda kehilangan hak untuk memperoleh cuti mengasuh anak dan dilarang bekerja di luar negeri.",
            "Generasi muda diwajibkan oleh pemerintah untuk pensiun dini pada usia 65 tahun guna memberi ruang bagi tenaga kerja asing.",
            "Generasi muda tidak lagi diperbolehkan memanfaatkan teknologi robotik dalam merawat orang tua di panti jompo.",
            "Generasi muda menolak seluruh bantuan subsidi pemerintah di bidang fasilitas medis dan jaminan hari tua."
        ],
        "formula": {
            "title": "ANALISIS PROBLEMATIKA SHOUSHIKOUREIKA (少子高齢化の因果構造)",
            "latex": "\\begin{cases} \\text{少子化 (Angka Lahir Turun)} \\\\ \\text{高齢化 (Lansia Meningkat)} \\end{cases} \\implies \\begin{cases} \\mathbf{\\text{労働力不足 (Krisis Tenaga Kerja)}} \\\\ \\mathbf{\\text{社会保障負担の増大 (Beban Jaminan Sosial Berat)}} \\end{cases}",
            "legend": "• Tantangan struktural multidimensi yang memengaruhi perekonomian dan tata kelola kesejahteraan Jepang"
        },
        "hints": {
            "concept": "Teks menyatakan: '将来の 労働力不足が 心配されており、年金や 医療などの 社会保障費の 負担も 若い世代に 重く のしかかっています。'.",
            "execution": "Pilih opsi yang menyoroti beban jaminan sosial yang berat dan kekurangan tenaga kerja produktif bagi generasi muda."
        }
    },
    {
        "id": "jpn-lat-h-10",
        "materi": "DOKKAI ANALITIS: LITERASI TEKNOLOGI & LANSIA",
        "topic": "Peran Robotika dan Otomasi dalam Industri Perawatan Medis Lansia (Kaigo Robot)",
        "stem": "Melanjutkan wacana demografi di atas, mengapa pengembangan 'robot pendamping perawatan' (*kaigo robot*) menjadi strategi prioritas di Jepang?",
        "correct": "Untuk meringankan beban fisik tenaga perawat manusia dalam merawat kaum lansia sekaligus mengatasi krisis kelangkaan tenaga perawat.",
        "distractors": [
            "Untuk menggantikan seluruh dokter bedah di rumah sakit umum agar biaya operasional medis menjadi gratis.",
            "Untuk melatih kaum lansia agar mampu merakit mesin-mesin industri elektronik canggih secara mandiri.",
            "Karena lansia di Jepang menolak berinteraksi dengan perawat manusia dan hanya bersedia dirawat oleh robot.",
            "Sebagai strategi pemasaran perusahaan manufaktur otomotif untuk menghabiskan stok suku cadang mobil yang tidak terjual."
        ],
        "formula": {
            "title": "URGENSI TEKNOLOGI KAIGO ROBOT (介護現場のロボット導入)",
            "latex": "\\text{Lansia Melonjak} + \\text{Tenaga Perawat Langka} \\implies \\mathbf{\\text{Robot Perawat: Mengurangi Beban Fisik \\& Mengisi Defisit SDM}}",
            "legend": "• Solusi konvergen rekayasa mekatronika terhadap krisis kemanusiaan era modern"
        },
        "hints": {
            "concept": "Robot kaigo dikembangkan untuk membantu meringankan beban fisik pekerjaan perawat lansia dan menutupi kekurangan tenaga kerja.",
            "execution": "Pilih opsi yang berkaitan dengan meringankan beban fisik perawat manusia dan mengatasi krisis defisit SDM."
        }
    },
    {
        "id": "jpn-lat-h-11",
        "materi": "DOKKAI ANALITIS: BUDAYA & PRAGMATIKA SOSIAL",
        "topic": "Filosofi Keramahan Pelayanan Jepang (おもてなし - Omotenashi)",
        "stem": "Bacalah teks berikut:\n'「おもてなし」とは、見返りを 求めず、相手の 立場に 立って 心を 込めて 接客や 配慮を 行う 日本独自の 精神です。「おもて」は 表（おもてめん）、「なし」は 無いという 意味から、「裏表が ない 純粋な 心で 客を 迎える」という 語源も あります。相手が 言葉に 出して 頼む まえに、その 人が 何を 必要としているかを 先回りして 察し、自然に 行動することが「おもてなし」の 真髄と されています。'\nBerdasarkan wacana di atas, ciri pokok yang menjadi intisari (*shinzui*) dari semangat *omotenashi* adalah...",
        "correct": "Kemampuan berempati untuk merasakan dan memenuhi kebutuhan tamu secara alami sebelum tamu tersebut menyatakannya lewat kata-kata.",
        "distractors": [
            "Memberikan pelayanan mewah dengan menuntut imbalan tip uang tunai dalam persentase yang tinggi.",
            "Mengharuskan setiap tamu menghafal tata tertib perjamuan minum teh sebelum diizinkan memasuki ruangan hotel.",
            "Menolak melayani tamu yang tidak mengenakan pakaian tradisional kimono saat berkunjung ke restoran.",
            "Menyediakan fasilitas modern berbasis kecerdasan buatan tanpa melibatkan kehadiran sentuhan manusia sama sekali."
        ],
        "formula": {
            "title": "INTISARI OMOTE-NASHI (おもてなしの真髄)",
            "latex": "\\text{裏表がない心 (Tulus Tanpa Pamrih)} + \\mathbf{\\text{察し (Sasshi - Membaca Kebutuhan Sebelum Diminta)}} \\implies \\mathbf{\\text{おもてなし}}",
            "legend": "• Standar emas hospitality Jepang yang berakar dari kearifan upacara minum teh (Chado)"
        },
        "hints": {
            "concept": "Intisari omotenashi: '相手が 言葉に 出して 頼む まえに、その 人が 何を 必要としているかを 先回りして 察し、自然に 行動すること'.",
            "execution": "Pilih opsi yang menyebutkan pemenuhan kebutuhan secara peka sebelum tamu sempat memintanya dengan kata-kata."
        }
    },
    {
        "id": "jpn-lat-h-12",
        "materi": "DOKKAI ANALITIS: PRAGMATIKA LINGUISTIK",
        "topic": "Fungsi Respon Balik Interaktif dalam Percakapan (相槌 - Aizuchi)",
        "stem": "Bacalah uraian linguistik terapan berikut:\n'日本語の 会話では、「相槌（あいづち）」が 非常に 重要な 役割を 果たします。「はい」「ええ」「そうですね」「なるほど」などの 短い 言葉を、相手が 話している 最中に 適切な タイミングで 挟みます。これは 相手の 話の 邪魔を しているのではなく、「あなたの 話を 熱心に 聞いていますよ」「理解していますよ」という 共感と 傾聴の サインを 伝える ための 礼儀正しい コミュニケーション技術です。'\nApa tujuan utama penutur bahasa Jepang menyisipkan *aizuchi* saat mitra tutur sedang berbicara?",
        "correct": "Memberikan sinyal bahwa pembicara mendengarkan dengan penuh perhatian dan memahami pesan yang disampaikan sebagai wujud empati kesantunan.",
        "distractors": [
            "Memotong pembicaraan lawan bicara agar topik percakapan dapat segera dialihkan ke kepentingan diri sendiri.",
            "Menunjukkan ketidaksetujuan argumentasi secara implisit agar lawan bicara merasa ragu terhadap gagasannya.",
            "Menguji kecepatan berpikir lawan bicara dalam merespons sanggahan spontan di ruang publik.",
            "Menyamarkan ketidaktahuan pembicara terhadap kosakata asing yang digunakan oleh mitra bicara."
        ],
        "formula": {
            "title": "FUNGSI PRAGMATIK AIZUCHI (相槌の談話機能)",
            "latex": "\\text{Kata Singkat (なるほど, そうですね)} \\xrightarrow{\\text{Waktu Tepat}} \\mathbf{\\text{Sinyal Mendengarkan Aktif (傾聴) \\& Empati (共感)}}",
            "legend": "• Menjaga ritme dan kehangatan koneksi antarpribadi dalam diskursus lisan Jepang"
        },
        "hints": {
            "concept": "Teks menyatakan: aizuchi bukan memotong, melainkan sinyal bahwa 'saya mendengarkan dengan antusias dan memahami perkataan Anda' (共感と傾聴のサイン).",
            "execution": "Pilih opsi yang menjelaskan tanda empati dan bukti menyimak dengan penuh perhatian."
        }
    },
    {
        "id": "jpn-lat-h-13",
        "materi": "DOKKAI ANALITIS: INFOGRAFIS & ANGKET MAHASISWA",
        "topic": "Menganalisis Tren Pemilihan Pekerjaan Lulusan Baru (Shuukatsu)",
        "stem": "Cermati tabel survei kriteria pemilihan perusahaan oleh mahasiswa tingkat akhir di Jepang berikut:\n--------------------------------------------------\n【就職先を 選ぶ 基準（複数回答可）】\n1位：職場の 人間関係や 雰囲気が 良いこと（68%）\n2位：ワークライフバランス（休日の 多さ・残業の 少なさ）（62%）\n3位：給料や ボーナスが 高いこと（55%）\n4位：企業の 知名度・社会的な 安定性（41%）\n5位：海外で 活躍できる チャンスが あること（18%）\n--------------------------------------------------\nKesimpulan interpretatif yang PALING TEPAT berdasarkan data survei di atas adalah...",
        "correct": "Faktor iklim kerja yang harmonis dan keseimbangan hidup-kerja (work-life balance) lebih diutamakan oleh generasi muda dibanding sekadar besaran gaji materi atau nama besar perusahaan.",
        "distractors": [
            "Mayoritas mahasiswa menganggap kesempatan bekerja dan berkarier di luar negeri sebagai syarat paling mutlak dalam memilih perusahaan.",
            "Tingkat ketenaran nama perusahaan dan jaminan stabilitas sosial berada di urutan teratas melampaui seluruh indikator kenyamanan lingkungan kerja.",
            "Mahasiswa Jepang sudah tidak peduli sama sekali terhadap ada atau tidaknya pemberian upah bonus tahunan.",
            "Faktor jumlah libur dan sedikitnya lembur lembur kerja menduduki peringkat terbawah dalam daftar prioritas karier mahasiswa."
        ],
        "formula": {
            "title": "EVALUASI HIERARKI DATA SURVEI (就職意識調査の分析)",
            "latex": "\\mathbf{\\text{Hubungan Kerja (68\\%)}} > \\mathbf{\\text{Work-Life Balance (62\\%)}} > \\text{Gaji (55\\%)} > \\text{Popularitas (41\\%)}",
            "legend": "• Pergeseran orientasi nilai generasi baru menuju kesehatan mental dan kenyamanan relasional"
        },
        "hints": {
            "concept": "Peringkat 1 (68%) adalah hubungan kerja yang baik dan peringkat 2 (62%) adalah work-life balance, keduanya melampaui gaji (55%) dan nama besar perusahaan (41%).",
            "execution": "Pilih kesimpulan: Iklim kerja harmonis dan work-life balance lebih diutamakan dibanding gaji tinggi atau nama besar."
        }
    },
    {
        "id": "jpn-lat-h-14",
        "materi": "DOKKAI ANALITIS: TEKS OPINI EKOLOGI",
        "topic": "Fenomena Kantong Belanja Berbayar (Rejibukuro Yuuryouka) dan Dampaknya",
        "stem": "Bacalah wacana kebijakan lingkungan berikut:\n--------------------------------------------------\n2020年7月から、日本全国の スーパーや コンビニで レジ袋の 有料化が 義務付けられました。この 施策の 目的は、プラスチックゴミを 削減し、海洋環境を 守ることです。導入から 数年が 経ち、国民の 8割以上が マイバッグ（エコバッグ）を 持参するようになり、プラスチックの 消費量は 確実に 減りました。しかし、一部からは「紙袋や 生分解性プラスチックへの 切り替えコストが 高い」「万引きが 増えた」といった 新たな 課題も 指摘されています。\n--------------------------------------------------\nPernyataan mana yang merefleksikan keberhasilan implementasi kebijakan tas belanja berbayar menurut teks?",
        "correct": "Lebih dari 80% masyarakat kini terbiasa membawa tas belanja ramah lingkungan sendiri sehingga konsumsi plastik belanjaan nyata menurun.",
        "distractors": [
            "Seluruh toko serba ada di Jepang kini memberikan tas kertas mewah secara cuma-cuma tanpa memungut biaya apa pun.",
            "Pemerintah berhasil menghapuskan angka pencurian barang di pasar swalayan hingga mencapai tingkat nol persen.",
            "Konsumsi plastik di wilayah pesisir pantai Jepang langsung mengalami peningkatan sebesar delapan puluh persen.",
            "Masyarakat menghentikan kebiasaan berbelanja bahan makanan segar di supermarket dan beralih ke toko daring."
        ],
        "formula": {
            "title": "EVALUASI KEBIJAKAN PUBLIK EKOLOGI (レジ袋有料化の効果と課題)",
            "latex": "\\text{Indikator Sukses: } \\mathbf{\\text{8割以上が マイバッグ持参}} \\implies \\mathbf{\\text{プラスチック消費量の確実な減少}}",
            "legend": "• Analisis capaian tujuan regulasi lingkungan terhadap transformasi kebiasaan warga"
        },
        "hints": {
            "concept": "Teks menyatakan keberhasilan: '国民の 8割以上が マイバッグ（エコバッグ）を 持参するようになり、プラスチックの 消費量は 確実に 減りました。'.",
            "execution": "Pilih opsi: 'Lebih dari 80% masyarakat kini terbiasa membawa tas belanja ramah lingkungan sendiri sehingga konsumsi plastik menurun'."
        }
    },
    {
        "id": "jpn-lat-h-15",
        "materi": "DOKKAI ANALITIS: EVALUASI KRITIS WACANA EKOLOGI",
        "topic": "Mengidentifikasi Dampak Samping / Masalah Baru dari Kebijakan Plastik Berbayar",
        "stem": "Berdasarkan teks wacana ekologi pada nomor sebelumnya, tantangan atau dampak sampingan baru (*arata na kadai*) yang muncul akibat penerapan tas belanja berbayar adalah...",
        "correct": "Beban biaya peralihan ke bahan ramah lingkungan yang relatif tinggi bagi pedagang serta adanya laporan peningkatan insiden pencurian barang toko.",
        "distractors": [
            "Terjadinya kepunahan massal spesies penyu laut di sepanjang pesisir kepulauan Okinawa.",
            "Keluarnya instruksi penutupan permanen seluruh jaringan toko swalayan waralaba di Tokyo.",
            "Masyarakat tidak lagi diperbolehkan membawa dompet dan telepon genggam ke dalam toko kelontong.",
            "Penurunan drastis produksi hasil pertanian sayur mayur lokal akibat ketiadaan pupuk plastik."
        ],
        "formula": {
            "title": "IDENTIFIKASI TRADE-OFF KEBIJAKAN (政策の副作用・課題抽出)",
            "latex": "\\text{Tantangan Baru (課題): } \\begin{cases} \\mathbf{\\text{切り替えコストの高さ (Biaya Konversi Mahal)}} \\\\ \\mathbf{\\text{万引きの増加 (Pencurian Mengutil Naik)}} \\end{cases}",
            "legend": "• Keterampilan berpikir kritis dalam mengevaluasi konsekuensi tak terduga (unintended consequences)"
        },
        "hints": {
            "concept": "Teks menyebutkan: '「紙袋や 生分解性プラスチックへの 切り替えコストが 高い」「万引きが 増えた」といった 新たな 課題も 指摘されています。'.",
            "execution": "Pilih opsi yang menyebutkan biaya peralihan yang tinggi dan peningkatan pencurian (manbiki)."
        }
    },
    {
        "id": "jpn-lat-h-16",
        "materi": "DOKKAI ANALITIS: TEKS NARASI SEJARAH PANGAN",
        "topic": "Sejarah Mi Instan (Ramen Instan) dan Daya Cipta Momofuku Ando",
        "stem": "Bacalah cuplikan biografi tokoh inovasi Jepang berikut:\n--------------------------------------------------\n世界初の インスタントラーメン「チキンラーメン」は、1958年に 安藤百福（あんどう ももふく）によって 発明されました。戦後の 混乱期、屋台の ラーメンに 長い 行列を 作る 人々の 姿を 見て、「手軽に、美味しく、安全で、長持ちする ラーメンを 作りたい」と 決意したのが きっかけでした。彼は 自宅の 小さな 研究小屋で 試行錯誤を 重ね、天ぷらの 揚げ方を ヒントに「油で 揚げて 乾燥させる（瞬間油熱乾燥法）」という 画期的な 技術を 編み出しました。お湯を 注ぐだけで 3分で 食べられる この 商品は、「魔法の ラーメン」と 呼ばれ、瞬く間に 世界的な 食文化へと 成長しました。\n--------------------------------------------------\nInspirasi teknis apakah yang mendasari penemuan metode pengawetan mi kering instan oleh Momofuku Ando?",
        "correct": "Melihat teknik penggorengan tempura, yang menginspirasinya untuk mengeringkan mi basah dengan minyak panas berkecepatan tinggi.",
        "distractors": [
            "Mengamati proses pembekuan es di lemari pendingin laboratorium sains universitas terkemuka.",
            "Mempelajari teknik fermentasi ragi tradisional yang digunakan dalam pembuatan pasta kedelai miso.",
            "Meniru resep pengasapan daging ikan salmon liar yang dipraktikkan masyarakat suku pedalaman Ainu.",
            "Menggunakan sinar radiasi kimiawi modern untuk mematikan seluruh spora bakteri pada adonan tepung."
        ],
        "formula": {
            "title": "HEURISTIK ANALOGI INOVASI TEKNOLOGI (発想の転換・技術革新)",
            "latex": "\\text{天ぷらの 揚げ方 (Goreng Tempura)} \\xrightarrow{\\text{ヒント (Inspirasi)}} \\mathbf{\\text{瞬間油熱乾燥法 (Dehidrasi Minyak Panas Kering)}}",
            "legend": "• Rekayasa proses berbasis transfer domain kuliner domestik ke skala manufaktur pangan massal"
        },
        "hints": {
            "concept": "Teks menyatakan: '天ぷらの 揚げ方を ヒントに「油で 揚げて 乾燥させる（瞬間油熱乾燥法）」という 画期的な 技術を 編み出しました。'.",
            "execution": "Pilih opsi yang mengaitkan metode penggorengan mi dengan teknik memasak tempura."
        }
    },
    {
        "id": "jpn-lat-h-17",
        "materi": "DOKKAI ANALITIS: APRESIASI SASTRA TEKSTUAL",
        "topic": "Memahami Makna Implisit Puisi Singkat Haiku (Haiku & Kigo)",
        "stem": "Dalam seni puisi klasik Jepang (*Haiku*), terdapat aturan struktur metrum 5-7-5 suku kata dan kewajiban memuat kata musim (*Kigo*). Perhatikan karya agung Matsuo Basho berikut:\n'古池や / 蛙飛びこむ / 水の音'\n(Furuike ya / Kawazu tobikomu / Mizu no oto)\nKata penanda musim (*kigo*) yang tersemat dalam bait puisi tersebut beserta musim yang diwakilinya adalah...",
        "correct": "「蛙（かわず - Katak）」yang secara konvensional menjadi penanda datangnya musim semi (春).",
        "distractors": [
            "「古池（ふるいけ - Kolam tua）」yang menjadi penanda beku musim dingin yang menusuk kalbu.",
            "「水の音（みずのおと - Suara air）」yang menjadi penanda guyuran hujan badai musim panas.",
            "「飛びこむ（とびこむ - Melompat）」yang mewakili musim gugur saat dedaunan luruh.",
            "Puisi tersebut sama sekali tidak memiliki kigo karena disusun di luar tradisi haiku formal."
        ],
        "formula": {
            "title": "KONVENSI KIGO PUISI HAIKU (俳句の季語体系)",
            "latex": "\\text{Teks: } \\text{古池や (5)} + \\mathbf{\\text{蛙 (かわず) }} \\text{飛びこむ (7)} + \\text{水の音 (5)} \\implies \\mathbf{\\text{Kigo: 蛙 } \\to \\text{Musim Semi (春)}}",
            "legend": "• Katak yang mulai aktif bernyanyi dan melompat setelah masa hibernasi musim dingin"
        },
        "hints": {
            "concept": "Kata 'かわず' (kawazu/katak) dalam haiku klasik adalah kigo resmi untuk musim semi (春 - haru).",
            "execution": "Pilih opsi: '「蛙（かわず - Katak）」penanda musim semi (春)'."
        }
    },
    {
        "id": "jpn-lat-h-18",
        "materi": "DOKKAI ANALITIS: MEMO RENCANA PERJALANAN KELOMPOK",
        "topic": "Kalkulasi Waktu Transit dan Biaya Perjalanan Turis di Tokyo",
        "stem": "Bacalah petunjuk rute perjalanan berikut:\n--------------------------------------------------\n【新宿駅から 浅草寺への 移動ガイド】\n・ルートA（JR中央線 快速 ＋ 地下鉄銀座線 神田駅乗り換え）：\n  所要時間：約25分 / 運賃：340円\n・ルートB（都営新宿線 ＋ 都営浅草線 浅草橋駅乗り換え）：\n  所要時間：約30分 / 運賃：280円\n※現在、神田駅で エレベーター改修工事中のため、車椅子の 方や 重い 荷物の 方は ルートBの 利用を 推奨します。\n--------------------------------------------------\nJika seorang wisatawan membawa dua koper besar yang sangat berat dan memiliki anggaran terbatas, rute manakah yang paling direkomendasikan beserta alasannya?",
        "correct": "Rute B, karena ongkosnya lebih murah (280 yen) dan menghindari stasiun Kanda yang sedang mengalami renovasi lift.",
        "distractors": [
            "Rute A, karena waktu tempuhnya 5 menit lebih cepat tanpa perlu mempedulikan kondisi ketiadaan lift di Kanda.",
            "Rute A, karena seluruh kereta di jalur Ginza Line dilengkapi layanan pengangkutan koper otomatis.",
            "Rute B, meskipun biayanya jauh lebih mahal daripada Rute A demi memperoleh fasilitas bagasi khusus.",
            "Kedua rute dilarang digunakan oleh wisatawan asing yang membawa barang bawaan koper beroda."
        ],
        "formula": {
            "title": "PENGAMBILAN KEPUTUSAN MULTIKRITERIA RUTE (移動最適化の判断)",
            "latex": "\\text{Kriteria: } \\begin{cases} \\text{Koper Berat} \\implies \\text{Hindari Kanda (Rute B)} \\\\ \\text{Hemat Biaya} \\implies 280\\text{円 } < 340\\text{円 (Rute B)} \\end{cases} \\implies \\mathbf{\\text{Pilih Rute B}}",
            "legend": "• Mengintegrasikan kendala fisik mobilitas (aksesibilitas) dan batasan finansial"
        },
        "hints": {
            "concept": "Wisatawan membawa koper berat (stasiun Kanda rute A sedang renovasi lift, rute B direkomendasikan pengelola) dan ingin murah (rute B 280 yen vs rute A 340 yen).",
            "execution": "Pilih opsi Rute B dengan pertimbangan biaya lebih murah dan menghindari renovasi lift di Kanda."
        }
    },
    {
        "id": "jpn-lat-h-19",
        "materi": "KAIWA HYOUGEN: ETIKA BISNIS FORMAL",
        "topic": "Etika Penyerahan dan Penerimaan Kartu Nama (名刺交換 - Meishi Koukan)",
        "stem": "Dalam dunia bisnis profesional di Jepang, penukaran kartu nama (*Meishi Koukan*) merupakan ritual perkenalan yang sangat sakral. Prosedur manakah yang WAJIB dipatuhi saat menerima kartu nama dari klien?",
        "correct": "Menerima dengan kedua belah tangan, membaca nama dan jabatannya dengan cermat, lalu menaruhnya dengan rapi di atas dompet kartu nama di meja.",
        "distractors": [
            "Menerima dengan cepat menggunakan tangan kiri sambil langsung memasukkannya ke dalam saku celana belakang.",
            "Menuliskan catatan nomor telepon pribadi langsung di atas permukaan kartu nama klien menggunakan pulpen tinta.",
            "Melipat ujung kartu nama menjadi dua bagian sebagai penanda bahwa pertemuan tatap muka telah berhasil dilaksanakan.",
            "Mengibaskan kartu nama di udara sebagai bentuk apresiasi atas kualitas kertas cetak yang tebal."
        ],
        "formula": {
            "title": "PROTOKOL MEISHI KOUKAN (ビジネスマナー・名刺交換)",
            "latex": "\\text{Kartu Nama Klien} \\equiv \\mathbf{\\text{Representasi Raga Klien}} \\implies \\begin{cases} \\text{Terima: Dua Tangan (両手)} \\\\ \\text{Letak: Di Atas Meishi-ire (名刺入れの上)} \\\\ \\text{Tabu: Menulis / Melipat / Masuk Saku} \\end{cases}",
            "legend": "• Menunjukkan martabat penghormatan mutlak terhadap identitas mitra usaha"
        },
        "hints": {
            "concept": "Kartu nama dianggap sebagai 'wajah' pemiliknya. Wajib diterima dengan kedua tangan, dibaca teliti, dan ditaruh di atas dompet kartu nama di meja rapat.",
            "execution": "Pilih opsi yang menjelaskan penerimaan dengan dua tangan dan meletakkannya rapi di atas dompet kartu nama."
        }
    },
    {
        "id": "jpn-lat-h-20",
        "materi": "KAIWA HYOUGEN: MEMOHON BANTUAN TINGKAT TINGGI",
        "topic": "Penggunaan Pola Permohonan Halus Bersyarat (~Te Itadakemasen ka)",
        "stem": "Seorang mahasiswa ingin meminta dosen pembimbing memeriksa draf proposal skripsinya yang telah selesai ditulis. Kalimat permohonan yang PALING TEPAT dan beretika akademik tinggi adalah...",
        "correct": "先生、お忙しいところ 大変 恐縮ですが、論文の 原稿を 見て いただけないでしょうか。 (Melihat draf dengan bentuk permohonan bersyarat sangat santun).",
        "distractors": [
            "先生、論文の 原稿を 見てください。 (Bentuk instruksi kudasai standar yang dianggap kurang sopan kepada profesor pembimbing).",
            "先生、論文の 原稿を 見てあげます。 (Bentuk memberi bantuan yang sangat lancang dan memalukan jika ditujukan kepada atasan).",
            "先生、論文の 原稿を 見てもらいたいです。 (Menyatakan keinginan sepihak tanpa mempertimbangkan kesibukan profesor).",
            "先生、論文の 原稿を 見なさい。 (Bentuk perintah imperatif mutlak yang hanya digunakan atasan kepada bawahan)."
        ],
        "formula": {
            "title": "POLA PERMOHONAN AKADEMIK TERTINGGI (最敬体の依頼表現)",
            "latex": "\\text{Klausula Basa-Basi: } \\text{お忙しいところ恐縮ですが} + \\mathbf{V\\text{-て}} + \\mathbf{\\text{いただけないでしょうか}}",
            "legend": "• Memadukan ungkapan empati atas waktu dosen dengan bentuk negatif potensial rendah hati"
        },
        "hints": {
            "concept": "Meminta bantuan kepada orang berstatus sosial tinggi (dosen/profesor) menggunakan '〜ていただけないでしょうか' (te itadakenai deshou ka).",
            "execution": "Pilih opsi: '先生、お忙しいところ 大変 恐縮ですが、論文の 原稿を 見て いただけないでしょうか。'."
        }
    },
    {
        "id": "jpn-lat-h-21",
        "materi": "KAIWA HYOUGEN: ETIKA KELUAR RUANGAN KANTOR",
        "topic": "Salam Pulang Mendahului Rekan Kerja (お先に失礼します)",
        "stem": "Jam kerja telah usai pada pukul 18.00. Seorang staf junior telah menyelesaikan tugasnya dan bersiap pulang, sementara seniornya masih lembur di meja kerja. Ungkapan salam yang WAJIB diucapkan staf junior sebelum melangkah keluar pintu adalah...",
        "correct": "お先に 失礼します。 (Osaki ni shitsurei shimasu - saya mohon permisi karena pulang mendahului rekan-rekan).",
        "distractors": [
            "お疲れ様でした。さようなら。 (Mengucapkan sayounara kepada rekan kerja sekantor dianggap tidak lazim dan berjarak dingin).",
            "ご苦労様でした。 (Gokurousama deshita - ucapan terima kasih atas kerja keras yang HANYA boleh diucapkan atasan kepada bawahan).",
            "じゃあ、また あした ね。 (Ungkapan kasual pergaulan santai yang tidak pantas diucapkan staf junior kepada senior di kantor).",
            "早く 帰ってください。 (Menyuruh senior agar bergegas pulang yang melanggar hierarki kewenangan)."
        ],
        "formula": {
            "title": "SALAM KEPULANGAN KANTOR (退社時の挨拶マナー)",
            "latex": "\\begin{aligned} \\text{Orang yang Pulang Duluan: } & \\mathbf{\\text{お先に 失礼します (Osaki ni shitsurei shimasu)}} \\\\ \\text{Rekan yang Masih Lembur: } & \\text{お疲れ様でした (Otsukaresama deshita)} \\end{aligned}",
            "legend": "• Menjaga kepekaan rasa bersalah positif karena meninggalkan rekan yang masih bertugas"
        },
        "hints": {
            "concept": "Meninggalkan kantor lebih dulu mendahului rekan kerja yang masih bertugas wajib mengucapkan: 'お先に失礼します' (Osaki ni shitsurei shimasu).",
            "execution": "Pilih: 'お先に 失礼します。'."
        }
    },
    {
        "id": "jpn-lat-h-22",
        "materi": "KAIWA HYOUGEN: TABU LINGUISTIK KANTOR",
        "topic": "Bahaya Pemakaian Kata Gokurousama (ご苦労様) oleh Bawahan",
        "stem": "Mengapa seorang staf bawahan DILARANG KERAS mengucapkan 'ご苦労様でした' (*Gokurousama deshita*) kepada manajer divisi yang baru selesai memimpin proyek?",
        "correct": "Karena secara kultural dan pragmatik, *Gokurousama* adalah ucapan apresiasi vertikal dari pihak yang berstatus lebih tinggi kepada bawahannya, bukan sebaliknya.",
        "distractors": [
            "Karena ungkapan tersebut mengandung kosakata kuno yang hanya boleh diucapkan di dalam kuil Shinto.",
            "Karena kata *Gokurousama* berarti mengharapkan musibah kebangkrutan menimpa manajemen perusahaan.",
            "Karena ungkapan tersebut hanya boleh digunakan saat menyapa kurir pengantar paket pos di luar jam kerja.",
            "Karena manajer divisi di Jepang tidak menyukai segala bentuk ucapan terima kasih dari staf kantor."
        ],
        "formula": {
            "title": "TABU ARAH HIERARKI KESANTUNAN (上下関係の挨拶禁則)",
            "latex": "\\begin{cases} \\mathbf{\\text{Atasan } \\to \\text{ Bawahan:}} & \\text{ご苦労様 (Gokurousama) - Boleh} \\\\ \\mathbf{\\text{Bawahan } \\to \\text{ Atasan:}} & \\text{ご苦労様 - } \\mathbf{\\text{TABU MUTLAK! Wajib: お疲れ様 (Otsukaresama)}} \\end{cases}",
            "legend": "• Pelanggaran arah vertikal dianggap sebagai pelecehan terhadap hierarki manajerial"
        },
        "hints": {
            "concept": "ご苦労様 (gokurousama) secara mutlak hanya boleh diucapkan dari orang berkedudukan lebih tinggi kepada bawahannya. Bawahan wajib memakai お疲れ様 (otsukaresama).",
            "execution": "Pilih opsi yang menjelaskan bahwa Gokurousama adalah ungkapan dari atasan kepada bawahan, bukan sebaliknya."
        }
    },
    {
        "id": "jpn-lat-h-23",
        "materi": "KAIWA HYOUGEN: ETIKA MENERIMA TELEPON KANTOR",
        "topic": "Protokol Komunikasi Telepon Korporat (Uchi vs Soto)",
        "stem": "Saat menerima panggilan telepon dari klien luar perusahaan yang mencari rekan sekantornya bernama Yamada, manakah kalimat respons yang TEPAT diucapkan oleh resepsionis?",
        "correct": "「山田は ただ今、席を 外しております。」 (Menyebut Yamada tanpa embel-embel gelar 'san' karena merupakan orang dalam / uchi di hadapan klien luar).",
        "distractors": [
            "「山田さんは ただ今、席を 外しております。」 (Menyebut rekan sendiri dengan akhiran 'san' di hadapan klien luar dianggap melanggar etika uchi-soto).",
            "「山田部長様は 今 トイレに 行っています。」 (Menggunakan gelar kehormatan ganda dan menyebut alasan toilet secara vulgar kepada mitra bisnis).",
            "「山田は どこかに 遊びに 行きました。」 (Memberikan keterangan tidak profesional yang merusak citra kedisiplinan perusahaan).",
            "「山田先生は 忙しいので 電話に 出られません。」 (Menyebut rekan kerja sebagai 'sensei' dan menolak panggilan klien secara arogan)."
        ],
        "formula": {
            "title": "KONSEP UCHI-SOTO TELEPON BISNIS (ビジネス電話の内外区別)",
            "latex": "\\text{Bicara ke Klien Luar (Soto)} \\implies \\mathbf{\\text{Keluarga / Rekan Kantor (Uchi) Disebut Tanpa Gelar (Tanpa さん/部長)}}",
            "legend": "• Menghilangkan seluruh partikel kehormatan pada anggota kelompok sendiri di hadapan orang luar"
        },
        "hints": {
            "concept": "Di hadapan pihak luar (klien telepon), rekan sekantor (kelompok uchi) disebut nama belakang polos tanpa 'san': 山田は (Yamada wa).",
            "execution": "Pilih opsi: '「山田は ただ今、席を 外しております。」'."
        }
    },
    {
        "id": "jpn-lat-h-24",
        "materi": "KAIWA HYOUGEN: MERESPONS PUJIAN SECARA KULTURAL",
        "topic": "Etika Kerendahan Hati Merespons Pujian (Kenxun - 謙遜)",
        "stem": "Seorang penutur asli Jepang memuji kemampuan bahasa Anda:\n'日本語が とても お上手ですね！'\nBerdasarkan norma kesantunan tradisional Jepang (*Kenxun*), respons manakah yang PALING ALAMI dan mencerminkan kerendahan hati?",
        "correct": "「いいえ、まだまだです。」 (Tidak, kemampuan saya masih jauh dari sempurna / belum ada apa-apanya).",
        "distractors": [
            "「はい、私は天才ですから。」 (Menyombongkan diri sebagai orang jenius yang melanggar nilai kesopanan sosial).",
            "「当然です。毎日十時間勉強していますから。」 (Menyatakan kepantasan diri secara jumawa tanpa tedeng aling-aling).",
            "「あなたのほうが下手ですね。」 (Menghina balik kemampuan bahasa lawan bicara secara kasar).",
            "「その通りです。もっと褒めてください。」 (Meminta tambahan pujian yang dinilai sangat memalukan)."
        ],
        "formula": {
            "title": "PRAGMATIK KERENDAHAN HATI (謙遜の美徳)",
            "latex": "\\text{Pujian Lawan Bicara (お上手)} \\xrightarrow{\\text{Respon Kultural Ideal}} \\mathbf{\\text{「いいえ、まだまだです」 (Penyangkalan Santun)}}",
            "legend": "• Mencegah timbulnya kesan sombong dan menjaga keselarasan atmosfer pergaulan (Wa)"
        },
        "hints": {
            "concept": "Merespons pujian dalam budaya Jepang wajib disangkal dengan rendah hati: 'いいえ、まだまだです' (iie, mada mada desu).",
            "execution": "Pilih: '「いいえ、まだまだです。」'."
        }
    },
    {
        "id": "jpn-lat-h-25",
        "materi": "DOKKAI ANALITIS: KONSEP HARMONI SOSIAL",
        "topic": "Konsep Harmoni Kolektif (和 - Wa) dan Penyesuaian Diri di Ruang Publik",
        "stem": "Bacalah wacana antropologi budaya berikut:\n--------------------------------------------------\n日本社会の 基盤には、「和（わ）」、すなわち 集団の 調和を 重んじる 価値観が 深く 根付いています。個人の 主張や 権利を 強く 押し通すことよりも、周囲の 人々との バランスや 協力関係を 維持することが 優先されます。電車内での 通話禁止や、公共の 場所で 大声で 話さない マナー、列に きちんと 並ぶ 習慣などは、すべて 他人に 迷惑を かけず、社会全体の「和」を 乱さないための 具体的な 行動の 表れです。\n--------------------------------------------------\nBerdasarkan teks di atas, mengapa masyarakat Jepang sangat menjunjung tinggi ketertiban seperti mengantre rapi dan tidak menelepon di dalam gerbong kereta?",
        "correct": "Karena masyarakat memprioritaskan penjagaan harmoni kelompok ('Wa') dan berusaha sekuat tenaga agar tidak menimbulkan gangguan (*meiwaku*) bagi orang lain.",
        "distractors": [
            "Karena adanya ancaman denda pidana penjara seumur hidup bagi siapa pun yang bersuara di tempat umum.",
            "Karena telepon genggam yang diproduksi di Jepang dilarang memiliki teknologi pemancar suara di dalam kereta.",
            "Agar masyarakat asing merasa takut dan tidak berani mendatangi fasilitas stasiun kereta perkotaan.",
            "Karena tradisi tersebut diwajibkan oleh ajaran militer zaman kuno yang melarang tentara berbicara saat berjalan."
        ],
        "formula": {
            "title": "FILOSOFI HARMONI DAN MEIWAKU (和の精神と迷惑の回避)",
            "latex": "\\mathbf{\\text{和 (Wa - Harmoni Kolektif)}} + \\mathbf{\\text{迷惑防止 (Anti Mengganggu Orang Lain)}} \\implies \\text{Ketertiban Fasilitas Umum}",
            "legend": "• Menempatkan kohesi sosial di atas individualisme dalam ekosistem ruang publik"
        },
        "hints": {
            "concept": "Teks menyatakan ketertiban publik bertujuan: 'すべて 他人に 迷惑を かけず、社会全体の「和」を 乱さないための 具体的な 行動の 表れです。'.",
            "execution": "Pilih opsi yang mengaitkan ketertiban dengan menjaga harmoni ('Wa') dan menghindari gangguan ('meiwaku') bagi orang lain."
        }
    }
]
