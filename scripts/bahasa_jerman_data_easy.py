# -*- coding: utf-8 -*-
"""
BAHASA JERMAN - PAKET SOAL LATIHAN MUDAH (EASY) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / CEFR A1-A2 (Goethe-Zertifikat A1-A2)
Distribusi:
- 8 Butir: Wortschatz dasar (Familie, Zahlen, Uhrzeit, Hobbys, Essen/Trinken, Berufe)
- 10 Butir: Grammatik dasar (Präsens Konjugation, Trennbare Verben, Modalverben, Bestimmter/Unbestimmter Artikel Nom/Akk, Negation nicht vs kein)
- 7 Butir: Situasi Komunikasi Harian & Pragmatika Dasar (Begrüßung, Nach dem Weg fragen, Im Restaurant, Beim Arzt)
"""

BAHASA_JERMAN_EASY_ITEMS = [
    {
        "id": "ger-lat-e-01",
        "materi": "GRAMMATIK: PRÄSENS KONJUGATION (VOKALWECHSEL)",
        "topic": "Perubahan Vokal Akar Verba e -> ie pada Orang Kedua dan Ketiga Tunggal",
        "stem": "Lukas menceritakan kebiasaan membaca saudaranya:\n'Mein Bruder ( ... ) jeden Abend vor dem Schlafen einen Kriminalroman.'\nBentuk konjugasi kata kerja 'lesen' yang TEPAT untuk melengkapi kalimat tersebut adalah...",
        "correct": "liest (bentuk konjugasi orang ketiga tunggal 'er/mein Bruder' dengan perubahan vokal e menjadi ie).",
        "distractors": [
            "lest (bentuk konjugasi orang kedua jamak 'ihr' yang tidak mengalami perubahan vokal ie).",
            "lese (bentuk konjugasi orang pertama tunggal 'ich' yang tidak sesuai dengan subjek tunggal orang ketiga).",
            "lestet (bentuk lampau Präteritum jamak yang keliru secara kala waktu dan nomor persona).",
            "lesen (bentuk infinitif dasar atau konjugasi persona jamak wir/sie/Sie)."
        ],
        "formula": {
            "title": "VOKALWECHSEL IM PRÄSENS (e -> ie)",
            "latex": "\\text{lesen: } \\text{du liest}, \\quad \\text{er/sie/es liest}, \\quad \\text{ihr lest}",
            "legend": "• Subjek orang ketiga tunggal (er/sie/es) mengalami perubahan vokal dasar e $\\rightarrow$ ie.<br>• Bentuk teratur hanya berlaku pada persona jamak (wir/ihr/sie)."
        },
        "hints": {
            "concept": "Kata kerja kuat (starke Verben) seperti 'lesen' mengalami perubahan vokal akar kata (Vokalwechsel) dari 'e' menjadi 'ie' pada persona kedua tunggal (du) dan ketiga tunggal (er/sie/es).",
            "execution": "Subjek kalimat adalah 'Mein Bruder' (= er). Konjugasi untuk 'er' adalah 'liest' (l-i-e-s-t)."
        }
    },
    {
        "id": "ger-lat-e-02",
        "materi": "GRAMMATIK: KASUS AKKUSATIV (BESTIMMTER ARTIKEL)",
        "topic": "Deklinasi Artikel Tentu Maskulin sebagai Objek Penderita",
        "stem": "Di toko alat tulis, seorang siswa berkata kepada kasir:\n'Ich brauche einen Füller. Ich kaufe ( ... ) Füller hier, weil er von sehr guter Qualität ist.'\nKata sandang tertentu (bestimmter Artikel) yang TEPAT untuk kata benda maskulin 'Füller' pada posisi Akkusativ adalah...",
        "correct": "den (artikel Akkusativ maskulin tunggal yang menandai objek langsung penderita).",
        "distractors": [
            "der (artikel Nominativ maskulin tunggal yang hanya boleh digunakan sebagai subjek).",
            "dem (artikel Dativ maskulin tunggal yang digunakan untuk objek penyerta/tak langsung).",
            "des (artikel Genitiv maskulin tunggal yang menandai kepemilikan formal).",
            "das (artikel netral tunggal yang keliru gender gramatikalnya untuk kata benda Füller)."
        ],
        "formula": {
            "title": "DEKLINASI ARTIKEL MASKULIN",
            "latex": "\\text{Maskulin: } \\text{Nom: der} \\quad \\rightarrow \\quad \\text{Akk: den} \\quad \\rightarrow \\quad \\text{Dat: dem}",
            "legend": "• Verba transitif 'kaufen' menuntut objek langsung dalam kasus Akkusativ.<br>• Gender gramatikal: der Füller (maskulin)."
        },
        "hints": {
            "concept": "Kata kerja 'kaufen' merupakan verba transitif yang membutuhkan objek langsung dalam kasus Akkusativ. Dalam Akkusativ, hanya artikel maskulin yang berubah: 'der' menjadi 'den'.",
            "execution": "Gender 'Füller' adalah maskulin (der Füller). Sebagai objek penderita dari 'kaufe', artikelnya berubah menjadi 'den'."
        }
    },
    {
        "id": "ger-lat-e-03",
        "materi": "GRAMMATIK: TRENNBARE VERBEN (KATA KERJA TERPISAH)",
        "topic": "Posisi Prefiks Terpisah dalam Kalimat Utama (Hauptsatz)",
        "stem": "Dalam rutinitas pagi hari, seorang siswa menjelaskan jadwalnya:\n'Der Wecker klingelt um sechs Uhr, und ich stehe sofort ( ... ).'\nPrefiks yang TEPAT untuk melengkapi kata kerja terpisah 'aufstehen' (bangun tidur) adalah...",
        "correct": "auf (prefiks terpisah yang diletakkan di akhir klausula utama pada kalimat Präsens).",
        "distractors": [
            "aus (prefiks yang membentuk verba 'ausstehen' dengan makna menanggung/mentoleransi).",
            "ein (prefiks yang membentuk verba 'einstehen' dengan makna menjamin atau bertanggung jawab).",
            "an (prefiks yang membentuk verba 'anstehen' dengan makna mengantre dalam barisan).",
            "mit (prefiks yang membentuk verba 'mitstehen' yang tidak lazim dalam idiom bangun tidur)."
        ],
        "formula": {
            "title": "TRENNBARE VERBEN IM HAUPTSATZ",
            "latex": "\\text{Hauptsatz: } \\text{Subjekt} + \\text{Verbstamm (Pos. 2)} + \\dots + \\text{Präfix (Satzende)}",
            "legend": "• Infinitif: aufstehen $\\rightarrow$ Ich stehe ... auf.<br>• Prefiks terpisah 'auf' wajib menempati posisi paling akhir klausula."
        },
        "hints": {
            "concept": "Kata kerja terpisah (trennbare Verben) melepaskan prefiksnya saat dikonjugasikan dalam kalimat utama (Hauptsatz). Akar kata menempati posisi kedua, sedangkan prefiks berada di posisi paling akhir klausula.",
            "execution": "Kata kerja bangun tidur adalah 'aufstehen'. Subjek 'ich stehe', maka prefiks penutup di akhir kalimat adalah 'auf'."
        }
    },
    {
        "id": "ger-lat-e-04",
        "materi": "GRAMMATIK: MODALVERBEN (KÖNNEN VS DÜRFEN)",
        "topic": "Menyatakan Izin Resmi (Erlaubnis) Menggunakan Modalverb 'dürfen'",
        "stem": "Pengawas perpustakaan sekolah menegaskan tata tertib kepada siswa:\n'Hier im Lesesaal ist absolutes Schweigen vorgeschrieben. Man ( ... ) hier nicht laut telefonieren.'\nModalverb yang TEPAT untuk menyatakan larangan atau ketiadaan izin adalah...",
        "correct": "darf (bentuk tunggal persona impersonal 'man' dari modalverb 'dürfen' yang menyatakan larangan/aturan izin).",
        "distractors": [
            "kann (modalverb yang menyatakan kemampuan fisik atau kapabilitas teknis individu).",
            "will (modalverb yang menyatakan kehendak atau tekad pribadi subjek).",
            "soll (modalverb yang menyatakan mandat tugas atau anjuran pihak ketiga).",
            "mag (modalverb yang menyatakan rasa suka atau kecenderungan emosional pribadi)."
        ],
        "formula": {
            "title": "SEMANTIK MODALVERBEN: DÜRFEN VS KÖNNEN",
            "latex": "\\text{nicht dürfen} = \\text{Verbot (Larangan resmi)}, \\quad \\text{nicht können} = \\text{Unfähigkeit (Ketidakmampuan)}",
            "legend": "• 'man darf nicht' = tidak diperbolehkan/dilarang secara aturan.<br>• Subjek 'man' mengikuti konjugasi orang ketiga tunggal (er/sie/es darf)."
        },
        "hints": {
            "concept": "Dalam tata tertib resmi, larangan (Verbot) dinyatakan dengan 'nicht dürfen'. Konjugasi orang ketiga tunggal (er/sie/es/man) untuk 'dürfen' adalah 'darf'.",
            "execution": "Subjek adalah 'man' (impersonal tunggal). Bentuk konjugasi 'dürfen' untuk 'man' adalah 'darf'."
        }
    },
    {
        "id": "ger-lat-e-05",
        "materi": "GRAMMATIK: NEGATION (NICHT VS KEIN)",
        "topic": "Penggunaan Kata Penyangkal Benda 'kein' dengan Gender Feminin",
        "stem": "Ketika ditawari camilan oleh temannya, Martin menjawab:\n'Danke, aber ich habe im Moment ( ... ) Zeit, weil mein Bus in fünf Minuten abfährt.'\nKata sangkal yang TEPAT untuk kata benda tanpa artikel bergender feminin 'Zeit' adalah...",
        "correct": "keine (kata sangkal benda bergender feminin tunggal dalam kasus Akkusativ).",
        "distractors": [
            "nicht (partikel negasi yang digunakan untuk menyangkal verba, ajektiva, atau frasa berartikel tentu).",
            "kein (kata sangkal maskulin/netral dalam kasus Nominativ atau netral Akkusativ).",
            "keinen (kata sangkal maskulin tunggal dalam kasus Akkusativ).",
            "keinem (kata sangkal maskulin/netral tunggal dalam kasus Dativ)."
        ],
        "formula": {
            "title": "NEGASI: KEIN- VS NICHT",
            "latex": "\\text{kein/e/en} + \\text{Nomen (ohne Artikel)}, \\quad \\text{nicht} + \\text{Verb / Adjektiv / Eigennamen}",
            "legend": "• Nomen: die Zeit (feminin) $\\rightarrow$ Akkusativ feminin: keine Zeit.<br>• 'nicht' tidak digunakan langsung di depan kata benda telanjang."
        },
        "hints": {
            "concept": "Kata sangkal 'kein-' digunakan untuk menyangkal kata benda yang memakai unbestimmter Artikel (ein-) atau tanpa artikel (Nullartikel). Untuk gender feminin (die Zeit), bentuk Akkusativ adalah 'keine'.",
            "execution": "'Zeit' adalah kata benda feminin (die Zeit) dan berposisi sebagai objek dari 'haben'. Bentuk penolakan yang tepat adalah 'keine Zeit'."
        }
    },
    {
        "id": "ger-lat-e-06",
        "materi": "WORTSCHATZ & PRAGMATIKA: UHRZEIT (WAKTU INFORMAL)",
        "topic": "Menyatakan Waktu Setengah Jam Menuju Jam Berikutnya (Halb)",
        "stem": "Dua orang siswa janjian untuk belajar bersama. Jam dinding menunjukkan pukul 14:30. Dalam bahasa Jerman ragam santai/lisan (Umgangssprache), waktu tersebut diucapkan sebagai...",
        "correct": "Es ist halb drei. (pukul setengah tiga atau 30 menit sebelum jam 3 tepat).",
        "distractors": [
            "Es ist halb zwei. (keliru karena bermakna pukul 01:30 atau setengah dua).",
            "Es ist zwei Uhr dreißig Minuten spät. (ungkapan kaku tidak lazim dalam komunikasi lisan Jerman).",
            "Es ist Viertel nach zwei. (bermakna pukul 14:15 atau lewat seperempat jam).",
            "Es ist Viertel vor drei. (bermakna pukul 14:45 atau kurang seperempat jam)."
        ],
        "formula": {
            "title": "UHRZEIT IM DEUTSCHEN (HALB)",
            "latex": "\\text{halb } [N+1] = \\text{pukul } N:30",
            "legend": "• 14:30 = halb drei (setengah jam menuju pukul 3).<br>• Bahasa Jerman selalu mengacu pada jam yang akan dituju saat menggunakan 'halb'."
        },
        "hints": {
            "concept": "Dalam bahasa Jerman, ungkapan waktu 'halb' selalu merujuk pada jam berikutnya (jam target): 'halb' + (jam sekarang + 1). Pukul 14:30 berarti setengah jam menuju pukul 15:00 (drei).",
            "execution": "Pukul 14:30 = halb drei."
        }
    },
    {
        "id": "ger-lat-e-07",
        "materi": "GRAMMATIK: PERSONALPRONOMEN IM AKKUSATIV",
        "topic": "Kata Ganti Persona Ketiga Tunggal Netral dan Maskulin sebagai Objek",
        "stem": "Thomas kehilangan bolpoin barunya di kelas:\n'Wo ist mein Kugelschreiber? Ich suche ( ... ) schon seit zwanzig Minuten.'\nKata ganti orang (Personalpronomen) yang TEPAT untuk menggantikan kata benda maskulin 'Kugelschreiber' pada posisi Akkusativ adalah...",
        "correct": "ihn (kata ganti persona ketiga maskulin tunggal pada kasus Akkusativ).",
        "distractors": [
            "er (kata ganti persona ketiga maskulin tunggal pada kasus Nominativ).",
            "es (kata ganti persona ketiga netral tunggal yang tidak sesuai gender Kugelschreiber).",
            "sie (kata ganti persona ketiga feminin atau persona jamak).",
            "ihm (kata ganti persona ketiga maskulin/netral tunggal pada kasus Dativ)."
        ],
        "formula": {
            "title": "PERSONALPRONOMEN: MASKULIN AKKUSATIV",
            "latex": "\\text{der Kugelschreiber } \\rightarrow \\text{Nom: er} \\quad \\rightarrow \\quad \\text{Akk: ihn} \\quad \\rightarrow \\quad \\text{Dat: ihm}",
            "legend": "• Verba transitif 'suchen' menuntut objek langsung dalam kasus Akkusativ.<br>• Pengganti benda maskulin: 'ihn'."
        },
        "hints": {
            "concept": "Kata benda 'der Kugelschreiber' bergender maskulin. Ketika digantikan oleh pronomina persona pada posisi objek penderita (Akkusativ) dari verba 'suchen', bentuknya menjadi 'ihn'.",
            "execution": "Gender 'Kugelschreiber' adalah der (maskulin). Bentuk Akkusativ dari 'er' adalah 'ihn'."
        }
    },
    {
        "id": "ger-lat-e-08",
        "materi": "KOMUNIKASI HARIAN: SICH VORSTELLEN & HERKUNFT",
        "topic": "Preposisi Asal Daerah 'aus' vs Tinggal di Kota 'in'",
        "stem": "Seorang mahasiswa pertukaran memperkenalkan diri di hadapan kelas:\n'Guten Tag! Ich komme ( ... ) Indonesien, aber zurzeit wohne ich ( ... ) Berlin bei einer Gastfamilie.'\nPasangan preposisi yang TEPAT untuk menyatakan negara asal dan kota tempat tinggal adalah...",
        "correct": "aus / in (preposisi 'aus' untuk asal negara dan 'in' untuk lokasi keberadaan di kota).",
        "distractors": [
            "von / nach (kombinasi keliru yang bermakna titik awal relatif dan pergerakan ke kota).",
            "in / aus (urutan terbalik antara tempat tinggal dan negara asal).",
            "nach / bei (preposisi pergerakan arah ke negara dan kebersamaan).",
            "ab / an (preposisi titik keberangkatan waktu dan kontak tepi permukaan)."
        ],
        "formula": {
            "title": "HERKUNFT & WOHNORT",
            "latex": "\\text{kommen aus } + \\text{Land/Stadt}, \\quad \\text{wohnen in } + \\text{Stadt/Land}",
            "legend": "• Asal usul / kelahiran: kommen aus (Dativ).<br>• Domisili statis: wohnen in (Dativ)."
        },
        "hints": {
            "concept": "Untuk menyatakan asal negara/daerah (Herkunft), digunakan kata kerja 'kommen' + preposisi 'aus'. Untuk menyatakan tempat tinggal/domisili kota (Wohnort), digunakan 'wohnen' + preposisi 'in'.",
            "execution": "'kommen aus Indonesien' dan 'wohnen in Berlin'. Pilihan tepat: aus / in."
        }
    },
    {
        "id": "ger-lat-e-09",
        "materi": "GRAMMATIK: PRÄSENS VERBEN MIT VOKALWECHSEL (a -> ä)",
        "topic": "Perubahan Vokal Umlaut pada Verba 'fahren' untuk Persona Kedua Tunggal",
        "stem": "Seorang ibu menanyakan sarana transportasi anaknya ke sekolah:\n'Wie ( ... ) du morgens zur Schule, mit dem Fahrrad oder mit dem Bus?'\nBentuk konjugasi kata kerja 'fahren' yang TEPAT untuk subjek 'du' adalah...",
        "correct": "fährst (mengalami perubahan vokal a menjadi ä ditambah akhiran persona -st).",
        "distractors": [
            "fahrst (keliru karena tidak memunculkan perubahan vokal umlaut ä pada persona kedua).",
            "fährt (bentuk konjugasi untuk persona ketiga tunggal er/sie/es).",
            "fahre (bentuk konjugasi persona pertama tunggal ich).",
            "fahren (bentuk infinitif atau persona jamak wir/sie/Sie)."
        ],
        "formula": {
            "title": "VOKALWECHSEL (a -> ä)",
            "latex": "\\text{fahren: } \\text{du fährst}, \\quad \\text{er/sie/es fährt}, \\quad \\text{ihr fahrt}",
            "legend": "• Verba akar vokal 'a' mengalami penambahan Umlaut (ä) pada 'du' dan 'er/sie/es'.<br>• Pada 'ihr' dan 'wir', vokal tetap normal."
        },
        "hints": {
            "concept": "Kata kerja kuat dengan vokal akar 'a' seperti 'fahren' mengalami perubahan vokal menjadi 'ä' pada persona kedua tunggal (du) dan ketiga tunggal (er/sie/es).",
            "execution": "Subjeknya adalah 'du'. Konjugasinya adalah 'fährst'."
        }
    },
    {
        "id": "ger-lat-e-10",
        "materi": "GRAMMATIK: KATA TANYA (W-FRAGEN)",
        "topic": "Membedakan Arah Pergerakan 'Wohin?' vs Posisi Diam 'Wo?'",
        "stem": "Stefan melihat temannya membawa koper besar di stasiun:\n'Hallo Anna! ( ... ) fährst du am kommenden Wochenende? — Nach München zu meiner Tante.'\nKata tanya yang TEPAT untuk menanyakan destinasi tujuan pergerakan adalah...",
        "correct": "Wohin (kata tanya yang menanyakan arah tujuan pergerakan suatu perjalanan).",
        "distractors": [
            "Wo (kata tanya yang menanyakan posisi diam statis di suatu lokasi).",
            "Woher (kata tanya yang menanyakan asal kedatangan dari suatu tempat).",
            "Wann (kata tanya yang menanyakan waktu kejadian temporal).",
            "Warum (kata tanya yang menanyakan alasan kausalitas penyebab)."
        ],
        "formula": {
            "title": "W-FRAGEN: WO VS WOHIN VS WOHER",
            "latex": "\\text{Wohin? (Tujuan Arah/Akk)}, \\quad \\text{Wo? (Lokasi Statis/Dat)}, \\quad \\text{Woher? (Asal Usul)}",
            "legend": "• Jawaban 'Nach München' mengindikasikan destinasi arah gerak.<br>• Kata tanya arah yang tepat adalah 'Wohin'."
        },
        "hints": {
            "concept": "Kata tanya 'Wohin?' digunakan untuk menanyakan arah/tujuan pergerakan (ke mana?). Jawaban 'Nach München' (ke München) menegaskan bahwa pertanyaan menghendaki arah gerak.",
            "execution": "Arah tujuan = 'Wohin'."
        }
    },
    {
        "id": "ger-lat-e-11",
        "materi": "WORTSCHATZ: ESSEN & TRINKEN",
        "topic": "Pemilihan Kata Benda Makanan dan Minuman Sehari-hari",
        "stem": "Di kantin sekolah saat jam istirahat:\n'Zum Frühstück trinke ich meistens eine Tasse Kaffee mit Milch und esse ein ( ... ) mit Butter und Marmelade.'\nKata benda yang TEPAT dan lazim untuk melengkapi sarapan khas Jerman tersebut adalah...",
        "correct": "Brötchen (roti bulat kecil khas Jerman bergender netral yang disantap dengan mentega dan selai).",
        "distractors": [
            "Suppe (makanan berkuah sup yang tidak lazim diolesi mentega dan selai saat sarapan).",
            "Fleisch (daging bergender netral yang tidak biasa disantap bersama selai manis saat sarapan).",
            "Kuchen (kue tart manis bergender maskulin yang tidak cocok dengan artikel ein pada sarapan pagi).",
            "Salat (sayuran selada bergender maskulin yang tidak lazim disajikan dengan selai buah)."
        ],
        "formula": {
            "title": "WORTSCHATZ FRÜHSTÜCK",
            "latex": "\\text{das Brötchen (Netral)} \\rightarrow \\text{ein Brötchen mit Butter und Marmelade}",
            "legend": "• Gender: das Brötchen.<br>• Makanan pokok sarapan Jerman yang dimakan bersama mentega dan selai."
        },
        "hints": {
            "concept": "Di Jerman, menu sarapan klasik terdiri atas 'Brötchen' (roti bundar garing kecil) yang diolesi 'Butter und Marmelade'. Kata 'Brötchen' bergender netral (das Brötchen), sehingga cocok dengan artikel 'ein'.",
            "execution": "Kombinasi sarapan 'ein ... mit Butter und Marmelade' merujuk pada 'Brötchen'."
        }
    },
    {
        "id": "ger-lat-e-12",
        "materi": "GRAMMATIK: POSSESSIVPRONOMEN (NOMINATIV FEMININ)",
        "topic": "Kata Ganti Kepemilikan Orang Pertama untuk Benda Feminin",
        "stem": "Dalam percakapan keluarga:\n'Das ist ( ... ) Mutter. Sie arbeitet als Ärztin im städtischen Krankenhaus.'\nBentuk kata ganti kepemilikan orang pertama (Possessivpronomen) yang TEPAT untuk subjek feminin 'Mutter' adalah...",
        "correct": "meine (bentuk kepemilikan orang pertama tunggal untuk kata benda bergender feminin pada kasus Nominativ).",
        "distractors": [
            "mein (bentuk kepemilikan tanpa akhiran untuk kata benda maskulin atau netral).",
            "meinen (bentuk kepemilikan maskulin tunggal pada kasus Akkusativ).",
            "meinem (bentuk kepemilikan maskulin atau netral tunggal pada kasus Dativ).",
            "meiner (bentuk kepemilikan feminin pada kasus Dativ atau Genitiv)."
        ],
        "formula": {
            "title": "POSSESSIVPRONOMEN: NOMINATIV",
            "latex": "\\text{die Mutter (feminin) } \\rightarrow \\text{meine Mutter}, \\quad \\text{der Vater } \\rightarrow \\text{mein Vater}",
            "legend": "• Kata benda bergender feminin (die Mutter) menerima akhiran -e pada kasus Nominativ.<br>• Kasus Nominativ predikatif setelah verba 'sein' (Das ist...)."
        },
        "hints": {
            "concept": "Kata benda 'die Mutter' adalah feminin. Dalam kasus Nominativ (sebagai pelengkap predikatif dari verba 'sein'), Possessivpronomen 'mein-' mendapat akhiran '-e' menjadi 'meine'.",
            "execution": "Feminin Nominativ = 'meine Mutter'."
        }
    },
    {
        "id": "ger-lat-e-13",
        "materi": "GRAMMATIK: KATA KERJA TIDAK TERATUR 'MÖCHTEN'",
        "topic": "Menyatakan Keinginan Santun dalam Situasi Pemesanan",
        "stem": "Seorang pelanggan memesan minuman di sebuah kafe di Berlin:\n'Guten Tag! Ich ( ... ) bitte ein Glas Mineralwasser ohne Kohlensäure.'\nBentuk verba kesantunan 'möchten' yang TEPAT untuk subjek 'ich' adalah...",
        "correct": "möchte (bentuk tunggal persona pertama dari verba modalitas kesantunan möchten).",
        "distractors": [
            "möchtest (bentuk persona kedua tunggal untuk subjek du).",
            "möchtet (bentuk persona kedua jamak untuk subjek ihr).",
            "möchten (bentuk persona jamak wir/sie/Sie atau bentuk infinitif).",
            "mochte (bentuk lampau Präteritum dari mögen yang bermakna menyukai di masa lalu)."
        ],
        "formula": {
            "title": "KONJUGASI MÖCHTEN (HÖFLICHE BITTE)",
            "latex": "\\text{ich möchte}, \\quad \\text{du möchtest}, \\quad \\text{er/sie/es möchte}, \\quad \\text{wir möchten}",
            "legend": "• Persona pertama tunggal (ich) memiliki bentuk yang sama dengan persona ketiga tunggal (er/sie/es): möchte.<br>• Akhiran bukan -e melainkan sama persis dengan aturan dasar Konjunktiv II."
        },
        "hints": {
            "concept": "Verba 'möchten' (ingin/berkehendak secara santun) memiliki konjugasi persona pertama tunggal (ich) yang identik dengan persona ketiga tunggal (er/sie/es), yaitu 'möchte'.",
            "execution": "Subjek 'ich' -> konjugasi 'möchte'."
        }
    },
    {
        "id": "ger-lat-e-14",
        "materi": "WORTSCHATZ & GRAMMATIK: PLURALBILDUNG",
        "topic": "Pembentukan Bentuk Jamak Kata Benda Netral 'das Buch'",
        "stem": "Guru meminta para siswa membuka bahan ajar:\n'Bitte macht eure ( ... ) auf Seite 45 auf und lest den ersten Textabschnitt!'\nBentuk jamak (Plural) yang BENAR dari kata benda 'das Buch' adalah...",
        "correct": "Bücher (bentuk jamak dengan penambahan Umlaut u -> ü dan akhiran -er).",
        "distractors": [
            "Buchs (keliru karena menyerupai bentuk jamak bahasa Inggris dengan akhiran -s).",
            "Buchen (keliru karena akhiran -en adalah nama pohon fagus/beech dalam bahasa Jerman).",
            "Buche (keliru karena akhiran -e tanpa umlaut bukan bentuk jamak baku dari kata das Buch).",
            "Büchern (keliru karena bentuk ini memiliki akhiran Dativ jamak, sedangkan di sini posisinya adalah Akkusativ)."
        ],
        "formula": {
            "title": "PLURALBILDUNG: DAS BUCH",
            "latex": "\\text{das Buch} \\quad \\rightarrow \\quad \\text{die Bücher (Nom/Akk Plural)}",
            "legend": "• Kata benda netral monosilabel berakar vokal belakang sering membentuk jamak dengan Umlaut + -er.<br>• Akkusativ Plural: eure Bücher."
        },
        "hints": {
            "concept": "Bentuk jamak dari 'das Buch' adalah 'die Bücher' (dengan perubahan vokal u menjadi ü dan penambahan sufiks -er). Kasus di sini adalah Akkusativ Plural (eure Bücher).",
            "execution": "Plural dari Buch = Bücher."
        }
    },
    {
        "id": "ger-lat-e-15",
        "materi": "GRAMMATIK: PRÄPOSITIONEN MIT AKKUSATIV (FÜR)",
        "topic": "Preposisi Murni Akkusativ 'für' yang Diikuti Kata Ganti Persona",
        "stem": "Klaus membawa hadiah ulang tahun untuk temannya:\n'Heute hat Claudia Geburtstag. Dieses Geschenk ist ( ... ).'\nBentuk kata ganti yang TEPAT setelah preposisi Akkusativ 'für' untuk persona ketiga feminin 'Claudia' adalah...",
        "correct": "für sie (preposisi 'für' selalu menuntut kasus Akkusativ; pronomina feminin Akkusativ adalah 'sie').",
        "distractors": [
            "für ihr (keliru karena 'ihr' adalah bentuk Dativ tunggal feminin).",
            "für ihnen (keliru karena 'ihnen' adalah bentuk Dativ jamak).",
            "zu sie (preposisi 'zu' menuntut Dativ dan tidak lazim untuk penyerahan kado).",
            "von sie (preposisi 'von' menuntut Dativ der/ihr)."
        ],
        "formula": {
            "title": "AKKUSATIV-PRÄPOSITION: FÜR",
            "latex": "\\text{Präposition } \\mathbf{für} + \\text{Akkusativ} \\quad (\\text{sie } \\rightarrow \\text{sie})",
            "legend": "• Preposisi Akkusativ murni: bis, durch, für, gegen, ohne, um (FUDG-BO).<br>• Claudia (sie) dalam kasus Akkusativ tetap 'sie'."
        },
        "hints": {
            "concept": "Preposisi 'für' adalah salah satu preposisi yang selalu dan mutlak menuntut kasus Akkusativ. Kata ganti untuk Claudia (feminin tunggal) dalam kasus Akkusativ adalah 'sie'.",
            "execution": "'für' + Akkusativ feminin = 'für sie'."
        }
    },
    {
        "id": "ger-lat-e-16",
        "materi": "KOMUNIKASI HARIAN: BEIM ARZT & KÖRPERTEILE",
        "topic": "Mengungkapkan Rasa Sakit Fisik Menggunakan Verba 'wehtun'",
        "stem": "Pasien mengeluhkan keluhannya kepada dokter:\n'Herr Doktor, ich kann kaum schlucken und habe Fieber. Mein ( ... ) tut schrecklich weh.'\nBagian tubuh bergender maskulin tunggal yang TEPAT sesuai keluhan sakit menelan tersebut adalah...",
        "correct": "Hals (leher/tenggorokan bergender maskulin tunggal yang cocok dengan verba tunggal tut weh).",
        "distractors": [
            "Ohren (telinga bentuk jamak yang seharusnya membutuhkan verba jamak tun weh).",
            "Augen (mata bentuk jamak yang tidak berkaitan langsung dengan keluhan sakit menelan).",
            "Bauch (perut bergender maskulin yang tidak berhubungan langsung dengan kesulitan menelan).",
            "Füße (kaki bentuk jamak yang keliru secara gejala klinis kesulitan menelan)."
        ],
        "formula": {
            "title": "SYMPTOME AUSDRÜCKEN: WEHTUN",
            "latex": "\\text{Nomen Sing. + tut weh} \\quad \\leftrightarrow \\quad \\text{Nomen Plur. + tun weh}",
            "legend": "• 'Mein Hals' (der Hals = leher/tenggorokan, maskulin tunggal) $\\rightarrow$ tut weh.<br>• Konteks sulit menelan (schlucken) spesifik merujuk pada tenggorokan/leher."
        },
        "hints": {
            "concept": "Ungkapan rasa sakit di Jerman menggunakan verba terpisah 'wehtun': 'etwas tut weh' (tunggal) atau 'etwas tun weh' (jamak). Kesulitan menelan (schlucken) berhubungan langsung dengan tenggorokan (der Hals).",
            "execution": "Subjek tunggal maskulin 'Mein Hals' + 'tut weh'."
        }
    },
    {
        "id": "ger-lat-e-17",
        "materi": "GRAMMATIK: KATA KERJA MODAL 'MÜSSEN'",
        "topic": "Menyatakan Keharusan Objektif yang Tidak Dapat Dihindari",
        "stem": "Seorang murid menyadari waktu ujian sudah semakin dekat:\n'Es ist schon spät und morgen schreiben wir eine Klassenarbeit. Ich ( ... ) jetzt wirklich fleißig lernen.'\nBentuk konjugasi kata kerja modal 'müssen' yang TEPAT untuk subjek 'ich' adalah...",
        "correct": "muss (bentuk konjugasi persona pertama tunggal tanpa akhiran -e dan tanpa umlaut).",
        "distractors": [
            "müsse (bentuk Konjunktiv I yang digunakan dalam kutipan tidak langsung formal).",
            "müsst (bentuk konjugasi persona kedua jamak untuk subjek ihr).",
            "müssen (bentuk infinitif atau konjugasi persona jamak wir/sie/Sie).",
            "musste (bentuk lampau Präteritum yang tidak sesuai dengan konteks waktu sekarang jetzt)."
        ],
        "formula": {
            "title": "KONJUGASI MODALVERB MÜSSEN (PRÄSENS)",
            "latex": "\\text{ich muss}, \\quad \\text{du musst}, \\quad \\text{er/sie/es muss}, \\quad \\text{wir müssen}",
            "legend": "• Pada persona tunggal (ich, du, er/sie/es), modalverb 'müssen' kehilangan tanda Umlaut (ü $\\rightarrow$ u).<br>• Persona 'ich' dan 'er/sie/es' memiliki bentuk identik tanpa sufiks persona: 'muss'."
        },
        "hints": {
            "concept": "Modalverb 'müssen' pada bentuk Präsens mengalami pelepasan Umlaut pada nomor tunggal. Untuk persona pertama tunggal (ich), bentuknya adalah 'muss' (tanpa akhiran -e).",
            "execution": "Subjek 'ich' -> konjugasi 'muss'."
        }
    },
    {
        "id": "ger-lat-e-18",
        "materi": "WORTSCHATZ: BERUFE & GENDER ENDING (-IN)",
        "topic": "Pembentukan Nama Profesi Wanita dengan Sufiks -in",
        "stem": "Dalam perkenalan profil karier:\n'Herr Wagner ist Lehrer an einem Gymnasium, und seine Frau arbeitet auch an derselben Schule als ( ... ).'\nBentuk nama profesi wanita yang TEPAT untuk rekan seprofesinya adalah...",
        "correct": "Lehrerin (bentuk feminin dari profesi guru dengan penambahan sufiks gender -in).",
        "distractors": [
            "Lehrer (bentuk maskulin tunggal profesi guru yang keliru diterapkan pada subjek wanita).",
            "Lehrerinnen (bentuk jamak feminin yang tidak cocok dengan subjek tunggal seine Frau).",
            "Lehrerfrau (istilah kolokial usang yang bermakna istri guru, bukan profesi mandiri sang wanita).",
            "Lehrerschaft (kata benda kolektif yang merujuk pada dewan korps keguruan secara keseluruhan)."
        ],
        "formula": {
            "title": "BERUFSBEZEICHNUNGEN (FEMININ)",
            "latex": "\\text{der Lehrer (Maskulin)} \\quad + \\text{ -in} \\quad \\rightarrow \\quad \\text{die Lehrerin (Feminin)}",
            "legend": "• Penambahan sufiks '-in' membentuk nama profesi feminin tunggal.<br>• Subjek tunggal: seine Frau als Lehrerin."
        },
        "hints": {
            "concept": "Dalam bahasa Jerman baku, nama profesi untuk perempuan dibentuk dengan menambahkan akhiran '-in' pada bentuk maskulinnya (der Lehrer -> die Lehrerin).",
            "execution": "Subjek adalah perempuan tunggal ('seine Frau'), maka profesinya adalah 'Lehrerin'."
        }
    },
    {
        "id": "ger-lat-e-19",
        "materi": "GRAMMATIK: KATA TANYA JA/NEIN-FRAGEN",
        "topic": "Struktur Kalimat Tanya Tertutup dengan Verba di Posisi Pertama",
        "stem": "Dua sahabat bertemu di lobi bioskop:\n'( ... ) du heute Abend Zeit, um mit mir den neuen Film anzuschauen? — Ja, sehr gern!'\nBentuk kata kerja yang TEPAT untuk mengawali kalimat tanya tertutup tersebut adalah...",
        "correct": "Hast (verba 'haben' yang dikonjugasikan untuk persona 'du' pada posisi pertama kalimat tanya).",
        "distractors": [
            "Haben (bentuk infinitif atau konjugasi jamak yang tidak cocok dengan subjek du).",
            "Hat (bentuk persona ketiga tunggal er/sie/es).",
            "Hattest (bentuk lampau Präteritum yang kontradiktif dengan keterangan waktu heute Abend).",
            "Bist (verba sein yang keliru secara idiomatis karena memiliki waktu diungkapkan dengan verba haben)."
        ],
        "formula": {
            "title": "JA/NEIN-FRAGE (VERB-ERST-STELLUNG)",
            "latex": "\\text{Posisi 1: Verb} + \\text{Posisi 2: Subjekt} + \\dots + \\text{?}",
            "legend": "• Kalimat tanya tertutup diawali kata kerja konjugasi (Posisi 1).<br>• Idiom: Zeit haben (memiliki waktu luang) $\\rightarrow$ Hast du Zeit?"
        },
        "hints": {
            "concept": "Kalimat tanya tanpa kata tanya (Ja/Nein-Frage) menempatkan kata kerja yang dikonjugasikan pada posisi pertama (Verb-Erst-Stellung). Ungkapan memiliki waktu luang adalah 'Zeit haben'.",
            "execution": "Subjek 'du' -> konjugasi 'haben' adalah 'hast'. Kalimat diawali dengan 'Hast'."
        }
    },
    {
        "id": "ger-lat-e-20",
        "materi": "GRAMMATIK: IMPERATIV (DU-FORM)",
        "topic": "Pembentukan Kalimat Perintah untuk Teman Sebaya (Du-Form)",
        "stem": "Seorang kakak memberi instruksi kepada adik laki-lakinya:\n'Peter, es ist schon sehr kalt draußen. ( ... ) bitte deine warme Jacke an!'\nBentuk kata kerja perintah (Imperativ) yang TEPAT dari verba 'anziehen' untuk persona 'du' adalah...",
        "correct": "Zieh (bentuk Imperativ untuk persona 'du' yang dibentuk dengan mencopot sufiks -en dan pronomina subjek).",
        "distractors": [
            "Zieht (bentuk Imperativ untuk persona jamak ihr).",
            "Ziehen Sie (bentuk Imperativ ragam formal/sopan).",
            "Ziehst (bentuk indikatif kalimat pernyataan biasa yang keliru dalam kalimat perintah).",
            "Ziehste (bentuk dialek percakapan daerah yang tidak baku secara gramatika nasional)."
        ],
        "formula": {
            "title": "IMPERATIV DER DU-FORM",
            "latex": "\\text{anziehen } \\rightarrow \\text{du ziehst an } \\rightarrow \\text{Zieh ... an!}",
            "legend": "• Copot pronomina 'du' dan akhiran personal '-st'.<br>• Prefiks terpisah 'an' diletakkan di akhir kalimat perintah."
        },
        "hints": {
            "concept": "Imperativ untuk persona 'du' dibentuk dari verba bentuk 'du' dengan menghilangkan pronomina 'du' dan akhiran personal '-st'. Verba 'anziehen' -> du ziehst an -> Zieh ... an!",
            "execution": "Bentuk perintah akrab tunggal = 'Zieh'."
        }
    },
    {
        "id": "ger-lat-e-21",
        "materi": "WORTSCHATZ: WOCHENTAGE & PRÄPOSITION 'AM'",
        "topic": "Penggunaan Preposisi Temporal 'am' untuk Hari dan Bagian Hari",
        "stem": "Dalam jadwal mingguan klub olahraga sekolah:\n'Das Fußballtraining findet jede Woche ( ... ) Samstagnachmittag auf dem Sportplatz statt.'\nPreposisi temporal yang TEPAT untuk menerangkan waktu hari dan bagian hari tertentu adalah...",
        "correct": "am (kontraksi dari an + dem yang digunakan secara wajib untuk nama hari dan bagian hari).",
        "distractors": [
            "im (kontraksi in + dem yang digunakan khusus untuk nama bulan, musim, dan tahun).",
            "um (preposisi waktu jam tepat atau menit spesifik).",
            "nach (preposisi yang menyatakan urutan sesudah peristiwa).",
            "von (preposisi titik awal rentang waktu yang menuntut pasangan bis)."
        ],
        "formula": {
            "title": "TEMPORALE PRÄPOSITIONEN: AM VS IM VS UM",
            "latex": "\\mathbf{am} + \\text{Tage/Tageszeiten}, \\quad \\mathbf{im} + \\text{Monate/Jahreszeiten}, \\quad \\mathbf{um} + \\text{Uhrzeit}",
            "legend": "• Hari (Montag, Dienstag...) & bagian hari (Vormittag, Nachmittag) memakai 'am'.<br>• Kontraksi: an + dem = am."
        },
        "hints": {
            "concept": "Preposisi 'am' (singkatan dari an dem) digunakan untuk menyatakan waktu berupa nama hari (Wochentage), tanggal (Datum), dan bagian hari (Tageszeiten seperti Vormittag/Nachmittag).",
            "execution": "Samstagnachmittag adalah kombinasi hari dan bagian hari -> gunakan 'am'."
        }
    },
    {
        "id": "ger-lat-e-22",
        "materi": "GRAMMATIK: KATA GANTI PENUNJUK 'DIESER/DIESE/DIESES'",
        "topic": "Deklinasi Demonstrativpronomen Netral sebagai Objek Akkusativ",
        "stem": "Di etalase toko pakaian:\n'Schau mal! Wie findest du ( ... ) blaue T-Shirt dort drüben? Ich finde es wirklich schick.'\nBentuk kata ganti penunjuk (Demonstrativpronomen) yang TEPAT untuk kata benda netral 'T-Shirt' adalah...",
        "correct": "dieses (kata penunjuk netral tunggal dalam kasus Akkusativ yang sesuai dengan gender das T-Shirt).",
        "distractors": [
            "dieser (kata penunjuk maskulin tunggal pada kasus Nominativ).",
            "diesen (kata penunjuk maskulin tunggal pada kasus Akkusativ).",
            "diese (kata penunjuk feminin tunggal atau plural pada kasus Nominativ/Akkusativ).",
            "diesem (kata penunjuk maskulin atau netral tunggal pada kasus Dativ)."
        ],
        "formula": {
            "title": "DEMONSTRATIVPRONOMEN DIES-",
            "latex": "\\text{das T-Shirt (Netral) } \\rightarrow \\text{Nom/Akk: dieses T-Shirt}",
            "legend": "• Kata benda netral 'das T-Shirt' memiliki bentuk identik pada Nominativ dan Akkusativ.<br>• Objek penderita dari verba 'finden' berada dalam kasus Akkusativ netral: 'dieses'."
        },
        "hints": {
            "concept": "Kata benda 'das T-Shirt' bergender netral. Dalam kasus Akkusativ (objek dari verba 'finden'), kata penunjuk 'dies-' mendapat akhiran '-es' menjadi 'dieses'.",
            "execution": "Netral Akkusativ = 'dieses T-Shirt'."
        }
    },
    {
        "id": "ger-lat-e-23",
        "materi": "WORTSCHATZ & WETTERBERICHT",
        "topic": "Menyatakan Cuaca Hujan Menggunakan Konstruksi Impersonal 'es'",
        "stem": "Melihat awan gelap dan rintik air turun dari langit:\n'Nimm unbedingt deinen Regenschirm mit! Draußen ( ... ) es ziemlich stark.'\nKata kerja cuaca yang TEPAT untuk melengkapi kalimat tersebut adalah...",
        "correct": "regnet (verba cuaca impersonal 'regnen' yang bermakna turun hujan).",
        "distractors": [
            "scheint (verba yang bermakna bersinar untuk matahari: die Sonne scheint).",
            "friert (verba yang bermakna membeku atau kedinginan tanpa adanya turun hujan).",
            "weht (verba yang bermakna berembus khusus untuk angin: der Wind weht).",
            "blitzt (verba yang bermakna kilatan petir tanpa menandai hujan secara menyeluruh)."
        ],
        "formula": {
            "title": "WETTERAUSDRÜCKE (IMPERSONAL ES)",
            "latex": "\\text{Es regnet (Hujan)}, \\quad \\text{Es schneit (Salju)}, \\quad \\text{Die Sonne scheint (Cerah)}",
            "legend": "• Kebutuhan payung (Regenschirm) secara logis diakibatkan oleh hujan (regnen).<br>• Konstruksi impersonal: es regnet."
        },
        "hints": {
            "concept": "Dalam bahasa Jerman, fenomena cuaca hujan dinyatakan dengan kata kerja impersonal 'regnen' berpasangan dengan subjek semu 'es' (es regnet). Konteks membawa payung (Regenschirm) menegaskan kondisi hujan.",
            "execution": "Membawa payung karena hujan = 'es regnet'."
        }
    },
    {
        "id": "ger-lat-e-24",
        "materi": "GRAMMATIK: KATA PENGHUBUNG KOORDINATIF 'ABER'",
        "topic": "Menghubungkan Dua Klausa dengan Pertentangan Ringan (Posisi 0)",
        "stem": "Seorang remaja menjelaskan rencananya di akhir pekan:\n'Ich wollte eigentlich mit meinen Freunden ins Kino gehen, ( ... ) ich muss leider zu Hause für die Matheprüfung lernen.'\nKata hubung koordinatif (Konjunktion) yang TEPAT untuk menyatakan kontras atau pertentangan adalah...",
        "correct": "aber (konjungsi pertentangan yang tidak mengubah susunan kata/menempati posisi nol).",
        "distractors": [
            "denn (konjungsi kausalitas yang menyatakan alasan sebab-akibat).",
            "und (konjungsi penambahan kumulatif yang menyatakan kesinambungan setara).",
            "oder (konjungsi alternatif pilihan yang menyatakan opsi pengganti).",
            "weil (konjungsi subordinatif yang menuntut pemindahan verba ke akhir kalimat)."
        ],
        "formula": {
            "title": "KOORDINIERENDE KONJUNKTIONEN (ADUSO)",
            "latex": "\\text{ADUSO: } \\text{aber, denn, und, sondern, oder } (\\text{Posisi 0})",
            "legend": "• Klausa kedua tetap mempertahankan susunan Hauptsatz (Subjek di Posisi 1, Verb di Posisi 2).<br>• Makna pertentangan keinginan vs keharusan belajar diungkapkan oleh 'aber'."
        },
        "hints": {
            "concept": "Konjungsi koordinatif 'aber' (tetapi) digunakan untuk menghubungkan dua kalimat utama yang bertentangan. Konjungsi ini menempati posisi nol (Position 0), sehingga urutan kata berikutnya tetap: Subjek (ich) + Verba (muss).",
            "execution": "Pertentangan antara rencana ke bioskop dan kewajiban belajar = 'aber'."
        }
    },
    {
        "id": "ger-lat-e-25",
        "materi": "KOMUNIKASI HARIAN: EINKAUFEN & PREIS",
        "topic": "Menanyakan Harga Suatu Barang di Pasar atau Toko",
        "stem": "Seorang pembeli menunjuk ke arah seikat bunga tulip di pasar:\n'Entschuldigung, ( ... ) kosten diese schönen Blumen? — Zehn Euro, bitte.'\nUngkapan tanya yang TEPAT untuk menanyakan harga barang adalah...",
        "correct": "wie viel (frasa interogatif yang baku untuk menanyakan nominal harga barang: Wie viel kostet/kosten...).",
        "distractors": [
            "wie viele (kata tanya yang menanyakan jumlah kuantitas benda yang dapat dihitung).",
            "wie alt (kata tanya yang menanyakan usia seseorang atau umur benda).",
            "wie weit (kata tanya yang menanyakan jarak geografis suatu lokasi).",
            "wie lange (kata tanya yang menanyakan durasi rentang waktu kejadian)."
        ],
        "formula": {
            "title": "NACH DEM PREIS FRAGEN",
            "latex": "\\text{Wie viel kostet / kosten } + \\text{Nomen}?",
            "legend": "• 'Wie viel kostet...' (benda tunggal) / 'Wie viel kosten...' (benda jamak).<br>• Menanyakan total nominal harga."
        },
        "hints": {
            "concept": "Untuk menanyakan harga barang dalam bahasa Jerman, digunakan struktur 'Wie viel kostet ... ?' (untuk benda tunggal) atau 'Wie viel kosten ... ?' (untuk benda jamak).",
            "execution": "Menanyakan harga seikat bunga = 'Wie viel'."
        }
    }
]
