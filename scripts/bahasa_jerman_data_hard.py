# -*- coding: utf-8 -*-
"""
BAHASA JERMAN - PAKET SOAL LATIHAN SULIT (HARD / HOTS) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / CEFR B1 (Goethe-Zertifikat B1 / DSD I)
Distribusi:
- 8 Butir: Nebensätze lanjutan (obwohl, damit / um...zu Infinitiv, während, nachdem + Plusquamperfekt) & Relativsätze (Relativpronomen Nom/Akk/Dat)
- 9 Butir: Konjunktiv II (Höflichkeit/Irrealis), Passiv (Präsens/Präteritum), Adjektivdeklination (Typ 1 & 2), Genitiv & Genitivpräpositionen (trotz, wegen, während)
- 8 Butir: Verben mit festen Präpositionen (warten auf, teilnehmen an, sich interessieren für) serta Wacana Analitis & Landeskunde (Duale Ausbildung, Energiewende, D-A-CH)
"""

BAHASA_JERMAN_HARD_ITEMS = [
    {
        "id": "ger-lat-h-01",
        "materi": "GRAMMATIK LANJUTAN: NEBENSATZ MIT 'OBWOHL' (KONZESSIV)",
        "topic": "Hubungan Konsesif Pertentangan Logis dengan Verba di Posisi Paling Akhir",
        "stem": "Dalam evaluasi kinerja proyek teknologi hijau:\n'( ... ) die Anschaffungskosten für Solaranlagen anfangs relativ hoch sind, entscheiden sich immer mehr Haushalte für die Installation sauberer Photovoltaik.'\nKata penghubung subordinatif konsesif yang TEPAT untuk menyatakan paradoks pertentangan tersebut adalah...",
        "correct": "Obwohl (konjungsi konsesif yang bermakna 'meskipun/walaupun' dan memindahkan verba berkonjugasi ke akhir klausula).",
        "distractors": [
            "Weil (konjungsi kausalitas yang keliru karena biaya awal yang tinggi bukan merupakan penyebab positif adopsi).",
            "Damit (konjungsi finalitas yang menyatakan tujuan masa depan, bukan pertentangan fakta realita).",
            "Trotzdem (adverbia penghubung koordinatif yang harus diikuti langsung oleh kata kerja di posisi kedua Hauptsatz).",
            "Sodass (konjungsi konsekutif yang menyatakan konsekuensi logis lanjutan)."
        ],
        "formula": {
            "title": "KONZESSIVSATZ MIT OBWOHL",
            "latex": "\\mathbf{Obwohl} + \\text{Subjekt} + \\dots + \\text{Verb (sind)}, \\quad \\text{Verb (entscheiden)} + \\text{Subjekt} + \\dots",
            "legend": "• Meskipun ada rintangan A (biaya tinggi), aksi B tetap dilakukan.<br>• Memicu susunan Nebensatz (Verb-Letzt) dan membalik induk kalimat (Verb-Erst)."
        },
        "hints": {
            "concept": "Konjungsi konsesif 'obwohl' (meskipun/walaupun) mengawali klausa anak yang menyatakan kondisi yang berlawanan dengan hasil pada klausa utama. Sebagai konjungsi subordinatif, kata kerja berada di ujung akhir klausa anak.",
            "execution": "Pertentangan antara biaya awal mahal dan tingginya minat masyarakat = 'Obwohl'."
        }
    },
    {
        "id": "ger-lat-h-02",
        "materi": "GRAMMATIK LANJUTAN: FINALSÄTZE (DAMIT VS UM...ZU)",
        "topic": "Pemilihan Konstruksi Tujuan: Subjek Berbeda Mewajibkan Pemakaian 'damit'",
        "stem": "Seorang ibu menjelaskan alasannya bekerja lembur di kantor:\n'Die Mutter arbeitet jeden Tag zusätzliche Überstunden, ( ... ) ihre Kinder an einer renommierten Musikakademie studieren können.'\nStruktur penghubung tujuan (Finalsatz) yang TEPAT untuk melengkapi kalimat dengan dua subjek berbeda tersebut adalah...",
        "correct": "damit (konjungsi subordinatif tujuan 'supaya/agar' yang wajib digunakan bila subjek klausa induk dan klausa anak berbeda).",
        "distractors": [
            "um ... zu (konstruksi infinitif yang hanya boleh digunakan apabila subjek induk dan anak identik/sama).",
            "weil (konjungsi kausalitas yang menyatakan alasan peristiwa lampau/kini, bukan intensi tujuan ke depan).",
            "dass (konjungsi penjelas fakta yang tidak mengekspresikan intensi finalitas pengorbanan).",
            "ob (konjungsi keraguan interogatif yang tidak masuk akal dalam konteks tujuan pembiayaan studi)."
        ],
        "formula": {
            "title": "FINALSÄTZE: DAMIT VS UM...ZU",
            "latex": "\\text{Subjekt 1 (Mutter)} \\neq \\text{Subjekt 2 (Kinder)} \\quad \\implies \\quad \\mathbf{damit} + \\text{Nebensatz}",
            "legend": "• Bila subjek berbeda (Mutter vs Kinder), 'um...zu' DILARANG keras.<br>• Wajib menggunakan 'damit' dengan klausa lengkap dan verba di akhir."
        },
        "hints": {
            "concept": "Konstruksi tujuan (Finalsatz) dalam bahasa Jerman: jika subjek kalimat utama berbeda dengan subjek kalimat anak (Die Mutter vs ihre Kinder), maka HANYA konjungsi 'damit' yang boleh dipakai. Konstruksi 'um ... zu + Infinitiv' hanya sah jika subjek kedua klausa adalah orang yang sama.",
            "execution": "Subjek 1 = Die Mutter, Subjek 2 = ihre Kinder (berbeda). Gunakan 'damit'."
        }
    },
    {
        "id": "ger-lat-h-03",
        "materi": "GRAMMATIK LANJUTAN: RELATIVSÄTZE IM DATIV",
        "topic": "Penggunaan Relativpronomen Feminin dalam Kasus Dativ (der)",
        "stem": "Dalam sambutan perpisahan kepala laboratorium kimia:\n'Frau Professor Hoffmann ist eine herausragende Wissenschaftlerin, ( ... ) wir für die großartige Unterstützung während des Forschungsprojekts sehr danken.'\nKata ganti relatif (Relativpronomen) yang TEPAT untuk merujuk pada 'eine Wissenschaftlerin' adalah...",
        "correct": "der (pronomina relatif feminin tunggal dalam kasus Dativ yang dituntut oleh verba 'danken').",
        "distractors": [
            "die (pronomina relatif feminin tunggal dalam kasus Nominativ atau Akkusativ).",
            "denen (pronomina relatif jamak dalam kasus Dativ yang keliru nomor jumlahnya).",
            "dessen (pronomina relatif Genitiv maskulin/netral yang menyatakan kepemilikan).",
            "deren (pronomina relatif Genitiv feminin tunggal yang tidak cocok dengan valensi verba danken)."
        ],
        "formula": {
            "title": "RELATIVPRONOMEN IM DATIV (FEMININ)",
            "latex": "\\text{die Wissenschaftlerin (feminin)} + \\mathbf{danken} (+\\text{Dativ}) \\quad \\rightarrow \\quad \\text{Relativpronomen: } \\mathbf{der}",
            "legend": "• Gender dan numerus ditentukan oleh anteseden (eine Wissenschaftlerin = feminin tunggal).<br>• Kasus ditentukan oleh peran gramatikal di dalam anak kalimat (danken jemandeM = Dativ)."
        },
        "hints": {
            "concept": "Pronomina relatif mengambil gender dan jumlah (numerus) dari kata benda yang dirujuknya (eine Wissenschaftlerin = feminin tunggal), tetapi mengambil kasus dari fungsinya di dalam klausa relatif. Verba 'danken' menuntut Dativ. Bentuk Dativ feminin tunggal dari pronomina relatif adalah 'der'.",
            "execution": "Feminin + Dativ = 'der'."
        }
    },
    {
        "id": "ger-lat-h-04",
        "materi": "GRAMMATIK LANJUTAN: KONJUNKTIV II (IRREALIS DER GEGENWART)",
        "topic": "Menyatakan Pengandaian Hipotetis Tak Nyata dengan Verba 'sein' (wäre)",
        "stem": "Dua mahasiswa kelelahan menghadapi pekan ujian akhir semester:\n'Ich bin so gestresst. Wenn ich doch bloß reich ( ... ), ( ... ) ich jetzt sofort einen Flug in die Karibik buchen.'\nPasangan bentuk Konjunktiv II yang TEPAT untuk menyatakan pengandaian tak nyata masa kini tersebut adalah...",
        "correct": "wäre / würde (bentuk Konjunktiv II dari verba sein 'wäre' dan konstruksi pengandaian verba penuh 'würde buchen').",
        "distractors": [
            "war / werde (kombinasi indikatif masa lalu dan futur yang bukan ragam irrealis pengandaian).",
            "hätte / könnte (penggunaan verba kepemilikan hätte yang tidak cocok dengan kata sifat predikatif reich).",
            "sei / werde (bentuk Konjunktiv I kutipan wicara tidak langsung yang keliru konteks angan-angan).",
            "gewesen wäre / gebucht hätte (bentuk lampau lampau/Vergangenheit yang tidak cocok dengan penanda waktu sekarang jetzt)."
        ],
        "formula": {
            "title": "KONJUNKTIV II: IRREALER KONDITIONALSATZ",
            "latex": "\\text{Wenn ich reich } \\mathbf{wäre}, \\quad \\mathbf{würde} \\text{ ich } \\dots \\text{ buchen}",
            "legend": "• Pengandaian masa kini: sein $\\rightarrow$ wäre.<br>• Verba aksi biasa (buchen): würde + Infinitiv."
        },
        "hints": {
            "concept": "Pengandaian tidak nyata pada masa sekarang (Irrealis der Gegenwart) menggunakan Konjunktiv II. Kata kerja 'sein' berubah menjadi 'wäre' (jika saya kaya = wenn ich reich wäre). Untuk kata kerja umum seperti 'buchen', digunakan konstruksi 'würde + Infinitiv'.",
            "execution": "Wenn ich reich wäre, würde ich ... buchen."
        }
    },
    {
        "id": "ger-lat-h-05",
        "materi": "GRAMMATIK LANJUTAN: PASSIV PRÄSENS MIT 'WERDEN'",
        "topic": "Transformasi Kalimat Pasif dengan Pelaku Tindakan Preposisi 'von' (+ Dativ)",
        "stem": "Dalam proses perakitan kendaraan modern di pabrik mobil Stuttgart:\n'Die hochentwickelten Elektromotoren ( ... ) vollautomatisch von spezialisierten Industrie-Robotern ( ... ).'\nPasangan kata kerja bantu pasif dan bentuk Partizip II yang TEPAT untuk subjek jamak tersebut adalah...",
        "correct": "werden / montiert (bentuk pasif Präsens: werden jamak + Partizip II dari verba teratur montieren).",
        "distractors": [
            "wurden / montieren (kombinasi bentuk lampau dan bentuk infinitif dasar yang melanggar rumus pasif).",
            "worden / montiert (worden hanya digunakan pada pasif Perfekt setelah kata kerja Partizip II).",
            "wird / gemontiert (kesalahan bentuk nomor tunggal untuk subjek jamak serta penambahan ge- keliru pada verba berakhiran -ieren).",
            "haben / montiert (bentuk aktif Perfekt yang membalik arah tindakan manufaktur mesin)."
        ],
        "formula": {
            "title": "VORGANGSPASSIV IM PRÄSENS",
            "latex": "\\text{Subjekt (Plural)} + \\mathbf{werden} + \\dots + \\text{von (Dativ)} + \\mathbf{Partizip II (montiert)}",
            "legend": "• Subjek: Die Elektromotoren (jamak) $\\rightarrow$ werden.<br>• Verba berakhiran '-ieren' membentuk Partizip II tanpa 'ge-': montier + -t = montiert."
        },
        "hints": {
            "concept": "Kalimat pasif proses (Vorgangspassiv) dibentuk dengan rumus: Subjek + werden (dikonjugasikan) + ... + Partizip II. Subjeknya adalah 'Die Elektromotoren' (jamak -> werden). Verba berakhiran '-ieren' (montieren) membentuk Partizip II tanpa awalan 'ge-' -> montiert.",
            "execution": "Jamak -> werden, Partizip II dari montieren -> montiert. Pilihan tepat: werden / montiert."
        }
    },
    {
        "id": "ger-lat-h-06",
        "materi": "GRAMMATIK LANJUTAN: GENITIV-PRÄPOSITIONEN",
        "topic": "Preposisi 'trotz' yang Menuntut Kasus Genitiv",
        "stem": "Pemberitaan mengenai kelancaran operasi kereta cepat saat badai salju:\n'Trotz ( ... ) heftigen Schneesturms erreichten fast alle Züge der Deutschen Bahn ihr Ziel ohne größere Verspätung.'\nBentuk artikel Genitiv maskulin tunggal yang TEPAT untuk melengkapi frasa preposisi tersebut adalah...",
        "correct": "des (artikel Genitiv maskulin tunggal yang dituntut oleh preposisi 'trotz').",
        "distractors": [
            "dem (artikel Dativ maskulin tunggal yang merupakan bentuk kolokial lisan tidak baku dalam ragam formal).",
            "den (artikel Akkusativ maskulin tunggal yang salah total secara aturan kasus preposisi trotz).",
            "der (artikel Genitiv feminin tunggal atau Nominativ maskulin yang keliru gender untuk Schneesturm).",
            "das (artikel netral Nominativ/Akkusativ yang tidak sesuai gender kata der Sturm)."
        ],
        "formula": {
            "title": "GENITIV-PRÄPOSITION: TROTZ",
            "latex": "\\mathbf{trotz} + \\text{Genitiv} \\quad (\\text{der Schneesturm } \\rightarrow \\text{des Schneesturms})",
            "legend": "• Preposisi Genitiv standar B1/B2: trotz, wegen, während, statt/anstelle.<br>• Maskulin Genitiv: des + Nomen berakhiran -(e)s."
        },
        "hints": {
            "concept": "Preposisi konsesif 'trotz' (meskipun/terlepas dari) dalam bahasa Jerman baku menuntut kasus Genitiv. Kata benda 'der Schneesturm' adalah maskulin tunggal, sehingga artikelnya berubah menjadi 'des' (dan kata bendanya mendapat akhiran -s/-es).",
            "execution": "trotz + Genitiv maskulin = 'trotz des heftigen Schneesturms'."
        }
    },
    {
        "id": "ger-lat-h-07",
        "materi": "GRAMMATIK LANJUTAN: ADJEKTIVDEKLINATION (TYP 1)",
        "topic": "Deklinasi Kata Sifat Setelah Artikel Tentu dalam Kasus Akkusativ Maskulin",
        "stem": "Dalam pameran arsitektur perkotaan modern:\n'Der Bürgermeister lobte den ( ... ) Entwurf des jungen Architekten für den neuen Hauptbahnhof.'\nBentuk deklinasi kata sifat 'kreativ' yang TEPAT setelah artikel tentu maskulin Akkusativ 'den' adalah...",
        "correct": "kreativen (akhiran kata sifat -en setelah artikel tentu maskulin dalam kasus Akkusativ).",
        "distractors": [
            "kreativer (akhiran kata sifat komparatif atau deklinasi tanpa artikel Nominativ maskulin).",
            "kreative (akhiran kata sifat Nominativ/Akkusativ feminin atau Nominativ maskulin).",
            "kreatives (akhiran kata sifat netral Nominativ/Akkusativ).",
            "kreativem (akhiran kata sifat Dativ maskulin/netral tanpa artikel)."
        ],
        "formula": {
            "title": "SCHWACHE ADJEKTIVDEKLINATION (TYP 1)",
            "latex": "\\text{den (bestimmter Artikel Akk. Mask.) } + \\text{Adjektiv-}\\mathbf{en} + \\text{Nomen}",
            "legend": "• Pola schwache Deklination (setelah der/die/das/den...):<br>• Seluruh bentuk Akkusativ maskulin, seluruh Dativ, dan seluruh Plural wajib berakhiran '-en'."
        },
        "hints": {
            "concept": "Pada deklinasi kata sifat lemah (schwache Adjektivdeklination, yaitu setelah artikel tentu der/die/das), jika berada dalam kasus Akkusativ maskulin tunggal (den ... Entwurf), kata sifat SELALU berakhiran '-en'.",
            "execution": "den + Adjektiv + maskulin Nomen = 'den kreativen Entwurf'."
        }
    },
    {
        "id": "ger-lat-h-08",
        "materi": "GRAMMATIK LANJUTAN: VERBEN MIT FESTEN PRÄPOSITIONEN",
        "topic": "Verba 'warten' yang Berpasangan Permanen dengan Preposisi 'auf' (+ Akkusativ)",
        "stem": "Di ruang tunggu bandara internasional Frankfurt:\n'Seit über zwei Stunden warten die Passagiere ungeduldig ( ... ) den verspäteten Abflug ihrer Maschine.'\nPreposisi dan kasus yang TEPAT sebagai pasangan permanen kata kerja 'warten' adalah...",
        "correct": "auf (+ Akkusativ: warten auf etwas/jemanden).",
        "distractors": [
            "für (+ Akkusativ: kesalahan interferensi harfiah bahasa Inggris 'wait for').",
            "an (+ Dativ: preposisi yang keliru untuk objek penantian waktu/peristiwa).",
            "über (+ Akkusativ: preposisi yang lazim digunakan untuk verba sprechen atau sich ärgern).",
            "zu (+ Dativ: preposisi arah pergerakan yang tidak membentuk idiom penantian)."
        ],
        "formula": {
            "title": "FESTE PRÄPOSITION: WARTEN AUF (+ AKK)",
            "latex": "\\mathbf{warten auf} + \\text{Akkusativ} \\quad (\\text{der Abflug } \\rightarrow \\text{den Abflug})",
            "legend": "• Idiom baku: menunggu seseorang/sesuatu = warten auf (+Akk).<br>• Jangan terkecoh frasa bahasa Inggris 'wait for' $\\rightarrow$ BUKAN 'warten für'."
        },
        "hints": {
            "concept": "Kata kerja 'warten' (menunggu) memiliki pasangan preposisi tetap yang tidak dapat diubah, yaitu 'auf' yang selalu menuntut kasus Akkusativ (warten auf + Akkusativ).",
            "execution": "warten auf + Akkusativ maskulin = 'warten ... auf den verspäteten Abflug'."
        }
    },
    {
        "id": "ger-lat-h-09",
        "materi": "GRAMMATIK LANJUTAN: NEBENSATZ MIT 'WÄHREND' (TEMPORAL)",
        "topic": "Menyatakan Dua Aksi Simultan Bersamaan Waktu Menggunakan 'während'",
        "stem": "Dalam deskripsi kebiasaan belajar seorang akademisi:\n'( ... ) der Professor die wissenschaftlichen Daten am Computer analysierte, notierte seine Assistentin alle Auffälligkeiten im Laborbericht.'\nKata penghubung subordinatif temporal yang TEPAT untuk menyatakan dua peristiwa yang terjadi secara bersamaan adalah...",
        "correct": "Während (konjungsi subordinatif temporal yang bermakna 'sementara/selama' dan memindahkan verba ke akhir klausula).",
        "distractors": [
            "Nachdem (konjungsi anterioritas waktu yang menyatakan peristiwa yang sudah selesai sebelum peristiwa lain dimulai).",
            "Bevor (konjungsi posterioritas yang menyatakan peristiwa terjadi sebelum aksi lain berlangsung).",
            "Seitdem (konjungsi durasi titik awal masa lalu yang berlanjut hingga kini).",
            "Sobald (konjungsi ketepatan momen yang bermakna 'segera setelah')."
        ],
        "formula": {
            "title": "TEMPORALSATZ: GLEICHZEITIGKEIT MIT WÄHREND",
            "latex": "\\mathbf{Während} + \\text{Aktion A (Präteritum)}, \\quad \\text{Aktion B (Präteritum simultan)}",
            "legend": "• Menunjukkan simultanitas/kebersamaan dua aksi berdurasi.<br>• 'während' sebagai konjungsi memicu susunan Nebensatz (Verb di akhir)."
        },
        "hints": {
            "concept": "Konjungsi temporal subordinatif 'während' (selama/sementara) digunakan untuk menyatakan keserentakan (Gleichzeitigkeit) dua peristiwa yang berlangsung pada rentang waktu yang sama.",
            "execution": "Dua kegiatan simultan yang terjadi berbarengan = 'Während'."
        }
    },
    {
        "id": "ger-lat-h-10",
        "materi": "GRAMMATIK LANJUTAN: RELATIVSÄTZE MIT DATIV PLURAL (DENEN)",
        "topic": "Bentuk Khusus Relativpronomen Dativ Jamak 'denen'",
        "stem": "Direktur yayasan sosial memberikan penghargaan kepada relawan kemanusiaan:\n'Wir danken allen ehrenamtlichen Helfern, ohne ( ... ) unermüdlichen Einsatz diese Hilfsaktion unmöglich gewesen wäre, und ( ... ) wir heute großen Respekt zollen.'\nBentuk pronomina relatif Dativ jamak yang TEPAT untuk mengisi rujukan kedua (orang kepada siapa rasa hormat diberikan) adalah...",
        "correct": "denen (bentuk khusus pronomina relatif jamak dalam kasus Dativ).",
        "distractors": [
            "den (artikel biasa Akkusativ maskulin atau Dativ jamak yang dilarang pada pronomina relatif Dativ plural).",
            "die (pronomina relatif jamak dalam kasus Nominativ atau Akkusativ).",
            "deren (pronomina relatif kepemilikan Genitiv jamak/feminin).",
            "ihnen (pronomina persona biasa yang tidak dapat menghubungkan klausa relatif)."
        ],
        "formula": {
            "title": "RELATIVPRONOMEN IM DATIV PLURAL",
            "latex": "\\text{die Helfer (Plural)} + \\text{Respekt zollen (}+\\text{Dativ)} \\quad \\rightarrow \\quad \\text{Relativpronomen: } \\mathbf{denen}",
            "legend": "• Berbeda dari artikel biasa 'den', Relativpronomen Dativ Plural memiliki bentuk istimewa: 'denen'.<br>• Menghindari kerancuan dengan artikel penunjuk benda."
        },
        "hints": {
            "concept": "Pronomina relatif dalam bahasa Jerman memiliki satu bentuk khusus yang berbeda dari artikel tentu, yaitu pada kasus Dativ Plural, bentuknya adalah 'denen' (bukan 'den').",
            "execution": "Plural + Dativ pada Relativsatz = 'denen'."
        }
    },
    {
        "id": "ger-lat-h-11",
        "materi": "GRAMMATIK LANJUTAN: VERBEN MIT FESTEN PRÄPOSITIONEN (TEILNEHMEN)",
        "topic": "Verba 'teilnehmen' yang Berpasangan Permanen dengan Preposisi 'an' (+ Dativ)",
        "stem": "Dalam pengumuman pendaftaran simposium sains nasional:\n'Mehr als dreihundert renommierte Wissenschaftler aus ganz Europa nehmen in diesem Jahr ( ... ) Fachkongress für Biotechnologie in Leipzig teil.'\nPasangan preposisi dan artikel yang TEPAT untuk verba terpisah 'teilnehmen' adalah...",
        "correct": "an dem (preposisi 'an' menuntut Dativ dalam idiom 'teilnehmen an etwas'; maskulin: der Kongress -> dem Kongress).",
        "distractors": [
            "an den (kasus Akkusativ yang keliru karena teilnehmen an menuntut Dativ).",
            "in dem (kesalahan pemilihan preposisi spasial untuk kegiatan partisipasi acara keilmuan).",
            "bei dem (preposisi yang tidak membentuk kolokasi idiomatik resmi dengan verba teilnehmen).",
            "auf den (preposisi penantian arah yang tidak cocok dengan konsep berpartisipasi)."
        ],
        "formula": {
            "title": "FESTE PRÄPOSITION: TEILNEHMEN AN (+ DAT)",
            "latex": "\\mathbf{teilnehmen an} + \\text{Dativ} \\quad (\\text{der Kongress } \\rightarrow \\text{an dem / am Kongress})",
            "legend": "• Idiom: teilnehmen an + Dativ = berpartisipasi/ikut serta dalam...<br>• der Kongress (maskulin) $\\rightarrow$ dem Kongress."
        },
        "hints": {
            "concept": "Kata kerja terpisah 'teilnehmen' (ikut serta/berpartisipasi) selalu berpasangan dengan preposisi 'an' yang mewajibkan kasus Dativ (teilnehmen an + Dativ). Kata 'der Fachkongress' bergender maskulin, sehingga Dativ-nya adalah 'dem'.",
            "execution": "teilnehmen + an + Dativ maskulin = 'an dem Fachkongress'."
        }
    },
    {
        "id": "ger-lat-h-12",
        "materi": "GRAMMATIK LANJUTAN: PASSIV IM PRÄTERITUM",
        "topic": "Transformasi Pasif Kala Lampau Sejarah Menggunakan 'wurden + Partizip II'",
        "stem": "Dalam buku teks sejarah integrasi Eropa pasca Perang Dunia II:\n'Die Verträge zur Gründung der Europäischen Wirtschaftsgemeinschaft ( ... ) im Jahr 1957 in Rom von den Vertretern der sechs Gründerstaaten feierlich ( ... ).'\nPasangan bentuk kata kerja pasif Präteritum yang TEPAT untuk subjek jamak 'Die Verträge' adalah...",
        "correct": "wurden / unterzeichnet (bentuk pasif Präteritum jamak 'wurden' dan Partizip II tak terpisah 'unterzeichnet').",
        "distractors": [
            "wurden / geunterzeichnet (kesalahan penambahan awalan ge- pada kata kerja berprefiks tak terpisah unter-).",
            "wurdet / unterzeichnet (bentuk konjugasi persona kedua jamak ihr yang keliru nomor/persona).",
            "waren / unterzeichnet (membentuk Zustandspassiv yang tidak mengekspresikan aksi historis penandatanganan).",
            "worden / unterzeichnet (worden tidak dapat berdiri di posisi kedua kalimat utama tanpa kata kerja bantu)."
        ],
        "formula": {
            "title": "VORGANGSPASSIV IM PRÄTERITUM",
            "latex": "\\text{Subjekt (Plural)} + \\mathbf{wurden} + \\dots + \\mathbf{Partizip II (unterzeichnet)}",
            "legend": "• Präteritum dari werden: ich wurde, er wurde, wir/sie wurden.<br>• Unterzeichnen (untrennbar) $\\rightarrow$ Partizip II: unterzeichnet (tanpa ge-)."
        },
        "hints": {
            "concept": "Kalimat pasif proses dalam bentuk lampau naratif (Präteritum) dibentuk dengan: wurden (jamak) + Partizip II. Subjek 'Die Verträge' adalah jamak (wurden). Verba 'unterzeichnen' adalah verba berawalan tak terpisah, sehingga Partizip II-nya adalah 'unterzeichnet' (tanpa 'ge-').",
            "execution": "Subjek jamak lampau = 'wurden ... unterzeichnet'."
        }
    },
    {
        "id": "ger-lat-h-13",
        "materi": "WACANA ANALITIS & SOSIOKULTUR: DUALE AUSBILDUNG",
        "topic": "Memahami Konsep Inti Sistem Pendidikan Vokasi Ganda (Duales System) di Jerman",
        "stem": "Bacalah wacana analitis ketenagakerjaan berikut:\n'Das deutsche Modell der Dualen Ausbildung gilt weltweit als Erfolgsrezept gegen Jugendarbeitslosigkeit. Die Besonderheit liegt in der engen Verzahnung zweier Lernorte: Die Auszubildenden verbringen einen Teil ihrer Woche in der Berufsschule, wo theoretisches Fachwissen vermittelt wird, und den anderen Teil direkt in einem Ausbildungsbetrieb, wo sie praktische Fertigkeiten im realen Arbeitsumfeld erwerben.'\nBerdasarkan teks di atas, pilar utama yang menjadikan 'Duale Ausbildung' sangat diakui secara global adalah...",
        "correct": "Kombinasi terstruktur antara pembelajaran teori di sekolah kejuruan (Berufsschule) dan praktik kerja langsung di perusahaan (Betrieb).",
        "distractors": [
            "Pemberian gelar akademis sarjana doktoral secara otomatis kepada lulusan sekolah menengah kejuruan tanpa ujian.",
            "Penghapusan seluruh materi teori keilmuan demi memfokuskan siswa sepenuhnya pada kerja kasar di pabrik manufaktur.",
            "Kewajiban seluruh peserta magang untuk menanggung seluruh biaya operasional mesin pelatihan perusahaan secara mandiri.",
            "Sentralisasi pendidikan vokasi yang melarang keras keterlibatan sektor industri swasta dalam kurikulum nasional."
        ],
        "formula": {
            "title": "DUALES SYSTEM DER BERUFSAUSBILDUNG",
            "latex": "\\text{Duales System} = \\text{Theorie (Berufsschule)} + \\text{Praxis (Ausbildungsbetrieb)}",
            "legend": "• 2 Lernorte: Berufsschule (teori kejuruan) & Betrieb (praktik kerja nyata).<br>• Menghasilkan tenaga terampil siap kerja tanpa kesenjangan kompetensi."
        },
        "hints": {
            "concept": "Teks secara eksplisit menyatakan 'Verzahnung zweier Lernorte': satu bagian waktu di 'Berufsschule' untuk teori kejuruan dan bagian lain di 'Ausbildungsbetrieb' untuk keterampilan praktis.",
            "execution": "Pilar utama = kombinasi teori di Berufsschule dan praktik kerja di Betrieb."
        }
    },
    {
        "id": "ger-lat-h-14",
        "materi": "GRAMMATIK LANJUTAN: NEBENSATZ MIT 'NACHDEM' & PLUSQUAMPERFEKT",
        "topic": "Kaidah Anterioritas Waktu (Vorzeitigkeit) Antara Klausa Anak dan Induk",
        "stem": "Dalam laporan investigasi laboratorium forensik:\n'Nachdem die Forscher alle Blutproben gründlich ( ... ), ( ... ) sie die Ergebnisse im offiziellen Abschlussbericht.'\nPasangan kala waktu yang TEPAT untuk memenuhi kaidah 'Vorzeitigkeit' (Plusquamperfekt pada Nebensatz dan Präteritum pada Hauptsatz) adalah...",
        "correct": "analysiert hatten / veröffentlichten (klausa 'nachdem' lampau anterior memakai Plusquamperfekt dan induk kalimat memakai Präteritum).",
        "distractors": [
            "analysieren / veröffentlichen (kombinasi bentuk waktu sekarang Präsens yang mengabaikan ketuntasan masa lampau).",
            "analysiert haben / veröffentlichten (penggunaan Perfekt yang melanggar keselarasan anterioritas Präteritum baku).",
            "analysiert hatten / haben veröffentlicht (penggabungan bentuk Plusquamperfekt dengan Perfekt lisan yang tidak baku dalam laporan ilmiah).",
            "analysierten / veröffentlicht hatten (urutan kronologi terbalik yang menempatkan publikasi mendahului analisis laboratorium)."
        ],
        "formula": {
            "title": "VORZEITIGKEIT MIT NACHDEM",
            "latex": "\\mathbf{Nachdem} + \\text{Plusquamperfekt (analysiert hatten)}, \\quad \\text{Hauptsatz in } \\mathbf{Präteritum (veröffentlichten)}",
            "legend": "• Aksi pertama yang selesai lebih dulu wajib berada dalam Plusquamperfekt (hatten/waren + Partizip II).<br>• Aksi kedua yang menyusul berada dalam Präteritum."
        },
        "hints": {
            "concept": "Konjungsi 'nachdem' (setelah) menuntut aturan pergeseran waktu (Vorzeitigkeit). Jika kalimat utama berada dalam bentuk lampau (Präteritum), maka klausa 'nachdem' wajib berada dalam bentuk lampau yang lebih lampau, yaitu Plusquamperfekt (hatten/waren + Partizip II).",
            "execution": "Aksi lampau lebih dulu: analysiert hatten. Aksi berikutnya: veröffentlichten."
        }
    },
    {
        "id": "ger-lat-h-15",
        "materi": "GRAMMATIK LANJUTAN: ADJEKTIVDEKLINATION (TYP 2 - NACH UNBESTIMMTEM ARTIKEL)",
        "topic": "Deklinasi Kata Sifat Setelah Possessivartikel dalam Kasus Dativ Maskulin",
        "stem": "Dalam sambutan ulang tahun sahabat karib:\n'Ich danke meinem ( ... ) Freund aus tiefstem Herzen für seine langjährige Treue und Hilfsbereitschaft.'\nBentuk kata sifat 'treu' yang TEPAT setelah artikel kepemilikan Dativ 'meinem' adalah...",
        "correct": "treuen (akhiran kata sifat -en setelah artikel Dativ maskulin tunggal).",
        "distractors": [
            "treuer (akhiran deklinasi tanpa artikel pada kasus Nominativ maskulin).",
            "treue (akhiran kata sifat Nominativ/Akkusativ feminin).",
            "treues (akhiran kata sifat Nominativ/Akkusativ netral).",
            "treuem (kesalahan penambahan akhiran Dativ ganda -em pada kata sifat setelah artikel mein-em)."
        ],
        "formula": {
            "title": "GEMISCHTE ADJEKTIVDEKLINATION (TYP 2)",
            "latex": "\\text{meinem (Possessivartikel Dat. Mask.) } + \\text{Adjektiv-}\\mathbf{en} + \\text{Nomen}",
            "legend": "• Setelah ein-, kein-, mein- (Typ 2), jika kasusnya Dativ, akhiran kata sifat SELALU '-en'.<br>• Dilarang keras akhiran ganda: 'meinem treuem' (SALAH!). Yang benar: 'meinem treuen'."
        },
        "hints": {
            "concept": "Dalam deklinasi kata sifat campuran (gemischte Deklination, setelah ein-/kein-/mein-), pada kasus Dativ (meinem ... Freund), akhiran kata sifat selalu '-en' untuk semua gender.",
            "execution": "meinem + treu + -en = 'meinem treuen Freund'."
        }
    },
    {
        "id": "ger-lat-h-16",
        "materi": "GRAMMATIK LANJUTAN: KONJUNKTIV II DER VERGANGENHEIT (IRREALIS)",
        "topic": "Penyesalan Hipotetis Masa Lampau Menggunakan 'hätte + Partizip II'",
        "stem": "Seorang pelamar kerja menyesali kegagalannya dalam sesi wawancara bahasa asing:\n'Wenn ich während der Schulzeit doch nur fleißiger Deutsch ( ... ), ( ... ) ich die prestigeträchtige Stelle bei Siemens in München bekommen.'\nPasangan bentuk Konjunktiv II masa lampau (Irrealis der Vergangenheit) yang TEPAT adalah...",
        "correct": "gelernt hätte / hätte (konstruksi penyesalan masa lampau: hätte + Partizip II pada anak kalimat dan induk kalimat).",
        "distractors": [
            "lernen würde / würde (bentuk Konjunktiv II masa kini yang tidak mengekspresikan penyesalan masa sekolah lampau).",
            "gelernt habe / habe (bentuk indikatif Perfekt faktual yang bertentangan dengan fakta kegagalan).",
            "lernte / bekam (bentuk indikatif Präteritum yang menyatakan peristiwa nyata, bukan situasi hipotetis kontrafaktual).",
            "gelernt wäre / wäre (verba lernen membentuk konjugasi dengan haben, bukan kata kerja bantu sein)."
        ],
        "formula": {
            "title": "KONJUNKTIV II DER VERGANGENHEIT",
            "latex": "\\text{Wenn } \\dots \\text{Part. II } + \\mathbf{hätte/wäre}, \\quad \\mathbf{hätte/wäre} + \\dots + \\text{Part. II}",
            "legend": "• Irrealis der Vergangenheit menyatakan penyesalan atau situasi yang tidak pernah terjadi di masa lalu.<br>• lernen $\\rightarrow$ gelernt hätte; bekommen $\\rightarrow$ hätte bekommen."
        },
        "hints": {
            "concept": "Konjunktiv II masa lampau digunakan untuk menyatakan penyesalan atau situasi hipotetis yang bertentangan dengan kenyataan masa lampau. Rumusnya: Partizip II + hätte/wäre. Kata kerja 'lernen' dan 'bekommen' membentuk Perfekt dengan 'haben' -> gelernt hätte / hätte bekommen.",
            "execution": "gelernt hätte / hätte ... bekommen."
        }
    },
    {
        "id": "ger-lat-h-17",
        "materi": "GRAMMATIK LANJUTAN: VERBEN MIT FESTEN PRÄPOSITIONEN (SICH INTERESSIEREN)",
        "topic": "Pembedaan Verba Refleksif 'sich interessieren für (+Akk)' vs 'Interesse haben an (+Dat)'",
        "stem": "Dalam kuesioner orientasi bakat siswa sekolah menengah atas:\n'Viele Jugendliche in Deutschland interessieren sich heutzutage brennend ( ... ) moderne Informationstechnologien und künstliche Intelligenz.'\nPreposisi dan kasus yang TEPAT untuk melengkapi verba refleksif 'sich interessieren' adalah...",
        "correct": "für (+ Akkusativ: sich interessieren für etwas/jemanden).",
        "distractors": [
            "an (+ Dativ: preposisi yang hanya berpasangan dengan kata benda 'Interesse haben an', bukan verba sich interessieren).",
            "über (+ Akkusativ: preposisi yang digunakan untuk verba sich informieren atau sich ärgern).",
            "auf (+ Akkusativ: preposisi penantian atau harapan masa depan).",
            "mit (+ Dativ: preposisi keterlibatan instrumen atau kebersamaan sosial)."
        ],
        "formula": {
            "title": "FESTE PRÄPOSITION: SICH INTERESSIEREN FÜR",
            "latex": "\\mathbf{sich interessieren für} + \\text{Akkusativ} \\quad \\leftrightarrow \\quad \\mathbf{Interesse haben an} + \\text{Dativ}",
            "legend": "• Bentuk verba: sich interessieren für (+Akk).<br>• Bentuk nomina: das Interesse haben an (+Dat)."
        },
        "hints": {
            "concept": "Kata kerja refleksif 'sich interessieren' (berminat/tertarik pada) secara baku selalu diikuti preposisi 'für' dengan kasus Akkusativ. Jangan tertukar dengan frasa nominal 'Interesse haben an (+ Dativ)'.",
            "execution": "sich interessieren + für (+ Akkusativ)."
        }
    },
    {
        "id": "ger-lat-h-18",
        "materi": "GRAMMATIK LANJUTAN: PASSIV MIT MODALVERBEN",
        "topic": "Konstruksi Pasif Disertai Kata Kerja Modal (Modalverb + Partizip II + werden)",
        "stem": "Instruksi keselamatan operasional di laboratorium mikrobiologi:\n'Aus Sicherheitsgründen ( ... ) alle chemischen Substanzen nach Versuchsende vorschriftsmäßig in den dafür vorgesehenen Spezialbehältern ( ... ).'\nPasangan bentuk kata kerja modal pasif yang TEPAT untuk subjek jamak adalah...",
        "correct": "müssen / entsorgt werden (modalverb 'müssen' di posisi kedua + Partizip II 'entsorgt' + infinitif 'werden' di akhir kalimat).",
        "distractors": [
            "muss / entsorgen (bentuk tunggal aktif yang mewajibkan subjek manusia sebagai pelaku pembuangan).",
            "müssen / entsorgt worden (worden hanya digunakan dalam pasif Perfekt/lampau, bukan infinitif setelah modalverb).",
            "sollen / entsorgen werden (kesalahan bentuk infinitif aktif 'entsorgen' yang seharusnya berwujud Partizip II entsorgt).",
            "werden / entsorgen müssen (susunan aktif yang menempatkan zat kimia sebagai subjek yang memiliki kewajiban)."
        ],
        "formula": {
            "title": "PASSIV MIT MODALVERBEN IM HAUPTSATZ",
            "latex": "\\text{Modalverb (Pos. 2)} + \\dots + \\mathbf{Partizip II} + \\mathbf{werden (Satzende)}",
            "legend": "• Subjek: alle Substanzen (jamak) $\\rightarrow$ müssen.<br>• Kerangka akhir (Satzklammer): entsorgt werden."
        },
        "hints": {
            "concept": "Konstruksi pasif dengan modalverb dalam kalimat utama: Modalverb (berkonjugasi di posisi 2) + ... + Partizip II + werden (infinitif di akhir kalimat). Subjek jamak 'alle chemischen Substanzen' memerlukan modalverb jamak 'müssen'.",
            "execution": "Subjek jamak -> müssen ... entsorgt werden."
        }
    },
    {
        "id": "ger-lat-h-19",
        "materi": "WACANA ANALITIS & SOSIOKULTUR: ENERGIEWENDE",
        "topic": "Memahami Kebijakan Transisi Energi Hijau dan Penutupan Pembangkit Nuklir di Jerman",
        "stem": "Bacalah wacana kebijakan lingkungan berikut:\n'Unter dem Begriff \"Energiewende\" versteht die deutsche Bundesregierung den tiefgreifenden Umbau der nationalen Energieversorgung: weg von fossilen Brennstoffen wie Kohle sowie dem endgültigen Atomausstieg, hin zu erneuerbaren Energieträgern wie Windkraft, Photovoltaik und Biomasse. Kernziel dieser langfristigen Strategie ist es, bis zum Jahr 2045 vollständige Treibhausgasneutralität zu erreichen und gleichzeitig die Versorgungssicherheit für die heimische Industrie zu garantieren.'\nBerdasarkan wacana di atas, sasaran strategis jangka panjang dari proyek 'Energiewende' Jerman adalah...",
        "correct": "Mewujudkan netralitas emisi gas rumah kaca secara penuh pada tahun 2045 melalui peralihan total ke energi terbarukan.",
        "distractors": [
            "Membangun puluhan reaktor nuklir generasi terbaru di sepanjang perbatasan negara untuk menurunkan harga listrik.",
            "Meningkatkan konsumsi batu bara domestik guna menghindari ketergantungan impor panel surya dari luar negeri.",
            "Menghentikan seluruh aktivitas industri manufaktur berat agar pencemaran udara dapat berkurang seketika.",
            "Menjual seluruh cadangan listrik nasional ke negara tetangga demi mengejar keuntungan finansial jangka pendek."
        ],
        "formula": {
            "title": "DIE DEUTSCHE ENERGIEWENDE",
            "latex": "\\text{Energiewende} = \\text{Atomausstieg} + \\text{Kohleausstieg} \\quad \\rightarrow \\quad \\text{Treibhausgasneutralität bis 2045}",
            "legend": "• Transisi dari energi fosil & nuklir menuju energi terbarukan (Sonne, Wind, Biomasse).<br>• Target: 100% netralitas emisi iklim pada tahun 2045."
        },
        "hints": {
            "concept": "Teks secara gamblang menegaskan: 'Kernziel dieser langfristigen Strategie ist es, bis zum Jahr 2045 vollständige Treibhausgasneutralität zu erreichen' melalui pemanfaatan energi terbarukan.",
            "execution": "Sasaran utama = netralitas gas rumah kaca penuh pada tahun 2045 melalui energi terbarukan."
        }
    },
    {
        "id": "ger-lat-h-20",
        "materi": "GRAMMATIK LANJUTAN: PARTICIPLE ATTRIBUTES (PARTIZIP I ALS ADJEKTIV)",
        "topic": "Penggunaan Partizip I (-end) sebagai Kata Sifat Atributif Bermakna Aktif Sedang Berlangsung",
        "stem": "Dalam laporan sosiologi urban tentang tren demografi kota-kota besar:\n'Die stetig ( ... ) Zahl älterer Mitbürger stellt das deutsche Pflegesystem vor enorme finanzielle und personelle Herausforderungen.'\nBentuk Partizip I atributif dari kata kerja 'steigen' yang TEPAT untuk kata benda feminin 'die Zahl' dalam kasus Nominativ adalah...",
        "correct": "steigende (Partizip I dengan penambahan akhiran -d- dan deklinasi kata sifat feminin -e).",
        "distractors": [
            "gestiegene (bentuk Partizip II yang bermakna pasif atau peristiwa yang sudah selesai tuntas terjadi).",
            "steigenden (akhiran deklinasi yang keliru untuk kasus Nominativ tunggal setelah artikel tertentu die).",
            "steigend (bentuk adverbial dasar tanpa akhiran deklinasi atributif).",
            "steigendes (akhiran deklinasi netral yang keliru gender untuk kata benda feminin die Zahl)."
        ],
        "formula": {
            "title": "PARTIZIP I ALS ADJEKTIV (AKTIV & GLEICHZEITIG)",
            "latex": "\\text{Infinitiv (steigen)} + \\mathbf{d} + \\text{Adjektivendung (}\\mathbf{e}\\text{)} \\quad \\rightarrow \\quad \\text{die steigen}\\mathbf{de} \\text{ Zahl}",
            "legend": "• Partizip I menyatakan tindakan aktif yang sedang berlangsung secara kontinu.<br>• Deklinasi kata sifat tipe 1 (setelah die): Nominativ feminin = -e."
        },
        "hints": {
            "concept": "Partizip I dibentuk dari Infinitif + 'd' (steigen -> steigend) dan berfungsi sebagai kata sifat bermakna aktif-berlangsung (yang terus meningkat). Karena berada di depan kata benda feminin Nominativ berartikel tentu 'die Zahl', kata sifat mendapat akhiran '-e' (die steigende Zahl).",
            "execution": "steigend + e = 'steigende'."
        }
    },
    {
        "id": "ger-lat-h-21",
        "materi": "GRAMMATIK LANJUTAN: NEBENSATZ MIT 'SEITDEM' (TEMPORAL)",
        "topic": "Menyatakan Titik Awal Perubahan Berkelanjutan Menggunakan 'seitdem'",
        "stem": "Seorang atlet lari maraton menceritakan pola hidup barunya:\n'( ... ) ich meine Ernährung komplett auf pflanzliche Kost umgestellt habe, fühle ich mich tagsüber wesentlich fitter und leistungsfähiger.'\nKata penghubung subordinatif yang TEPAT untuk menandai titik awal mula perubahan kebiasaan yang berlanjut hingga kini adalah...",
        "correct": "Seitdem (konjungsi subordinatif temporal yang bermakna 'sejak saat' suatu aksi dimulai di masa lalu).",
        "distractors": [
            "Bis (konjungsi temporal batas akhir yang bermakna 'sampai/hingga').",
            "Bevor (konjungsi posterioritas yang bermakna 'sebelum').",
            "Solange (konjungsi durasi paralel yang bermakna 'selama').",
            "Sodass (konjungsi akibat logis yang bermakna 'sehingga')."
        ],
        "formula": {
            "title": "TEMPORALSATZ: SEITDEM",
            "latex": "\\mathbf{Seitdem} + \\text{Auslöser (Perfekt)}, \\quad \\text{Resultat bis heute (Präsens)}",
            "legend": "• 'seitdem' menandai titik tolak waktu permulaan di masa lalu.<br>• Dampak atau perubahan kondisi dirasakan berlanjut terus sampai sekarang."
        },
        "hints": {
            "concept": "Konjungsi subordinatif 'seitdem' (sejak / semenjak) digunakan untuk menghubungkan peristiwa awal di masa lampau yang menandai permulaan suatu keadaan yang dampaknya terus berlangsung sampai masa sekarang.",
            "execution": "Titik tolak waktu perubahan pola makan sejak saat itu = 'Seitdem'."
        }
    },
    {
        "id": "ger-lat-h-22",
        "materi": "GRAMMATIK LANJUTAN: N-DEKLINATION (SCHWACHE NOMEN)",
        "topic": "Deklinasi Khusus Kata Benda Maskulin Lemah dalam Kasus Akkusativ/Dativ",
        "stem": "Dalam sesi konsultasi hukum perdata di kantor notaris:\n'Der Anwalt bat den anwesenden ( ... ), das offizielle Protokoll sorgfältig durchzulesen und persönlich zu unterzeichnen.'\nBentuk kata benda maskulin lemah (n-Deklination) yang TEPAT dari 'der Zeuge' (saksi) pada posisi Akkusativ adalah...",
        "correct": "Zeugen (kata benda maskulin n-Deklination yang wajib menerima akhiran -n di semua kasus selain Nominativ tunggal).",
        "distractors": [
            "Zeuge (bentuk dasar Nominativ yang keliru karena berada di posisi objek penderita Akkusativ).",
            "Zeuges (kesalahan penambahan akhiran Genitiv kuat -s pada kata benda tipe lemah).",
            "Zeugens (penambahan akhiran ganda yang tidak dikenal dalam paradigma n-Deklination).",
            "Zeuger (bentuk buatan yang keliru mengacaukan kata benda saksi dengan verba zeugen)."
        ],
        "formula": {
            "title": "N-DEKLINATION (SCHWACHE MASCHULINA)",
            "latex": "\\text{der Zeuge (Nom.)} \\quad \\rightarrow \\quad \\text{den Zeugen (Akk.)} \\quad \\rightarrow \\quad \\text{dem Zeugen (Dat.)}",
            "legend": "• Kata benda maskulin berakhiran -e (Zeuge, Kunde, Kollege, Junge) termasuk n-Deklination.<br>• Menambahkan sufiks -(e)n di seluruh kasus kecuali Nominativ tunggal."
        },
        "hints": {
            "concept": "Kata benda maskulin tertentu yang berakhiran '-e' (seperti der Zeuge, der Kunde, der Kollege) tergolong ke dalam 'n-Deklination' (kata benda lemah). Ciri khasnya adalah selalu mendapat tambahan akhiran '-n' atau '-en' pada semua kasus selain Nominativ tunggal.",
            "execution": "den anwesenden + Zeuge -> 'den anwesenden Zeugen'."
        }
    },
    {
        "id": "ger-lat-h-23",
        "materi": "GRAMMATIK LANJUTAN: VERBEN MIT PRÄPOSITIONEN (ABHÄNGEN VON)",
        "topic": "Verba 'abhängen' yang Berpasangan Permanen dengan Preposisi 'von' (+ Dativ)",
        "stem": "Ekonom menganalisis prospek stabilitas nilai mata uang tunggal Eropa:\n'Der wirtschaftliche Erfolg der Eurozone hängt in hohem Maße ( ... ) geopolitischen Stabilität und den globalen Energiepreisen ab.'\nPreposisi dan bentuk artikel Dativ feminin yang TEPAT untuk melengkapi verba terpisah 'abhängen' adalah...",
        "correct": "von der (preposisi 'von' menuntut kasus Dativ; kata benda feminin die Stabilität menjadi der Stabilität).",
        "distractors": [
            "von die (kesalahan mempertahankan artikel Nominativ/Akkusativ setelah preposisi Dativ von).",
            "an der (preposisi an keliru karena bukan pasangan idiomatik dari verba abhängen).",
            "aus der (preposisi asal material yang keliru membentuk kolokasi ketergantungan kausalitas).",
            "über die (preposisi yang tidak memiliki asosiasi gramatikal dengan abhängen)."
        ],
        "formula": {
            "title": "FESTE PRÄPOSITION: ABHÄNGEN VON (+ DAT)",
            "latex": "\\mathbf{abhängen von} + \\text{Dativ} \\quad (\\text{die Stabilität } \\rightarrow \\text{von der Stabilität})",
            "legend": "• Idiom baku: bergantung pada sesuatu = abhängen von (+Dat).<br>• die Stabilität (feminin) $\\rightarrow$ der Stabilität."
        },
        "hints": {
            "concept": "Kata kerja terpisah 'abhängen' (bergantung pada) selalu berpasangan dengan preposisi 'von' yang mewajibkan kasus Dativ (abhängen von + Dativ). Kata 'die Stabilität' adalah feminin, sehingga bentuk Dativ-nya adalah 'der'.",
            "execution": "abhängen + von + Dativ feminin = 'von der geopolitischen Stabilität'."
        }
    },
    {
        "id": "ger-lat-h-24",
        "materi": "WACANA ANALITIS & LANDESKUNDE: D-A-CH REGION",
        "topic": "Karakteristik Linguistik dan Geografis Wilayah Berbahasa Jerman (D-A-CH)",
        "stem": "Dalam materi studi kebudayaan dan kawasan berbahasa Jerman:\n'Der Begriff \"D-A-CH-Länder\" ist ein etabliertes Akronym für die drei großen deutschsprachigen Staaten im Herzen Europas, die trotz gemeinsamer Standardsprache bemerkenswerte sprachliche Varietäten (Austriazismen, Helvetismen) und föderale Besonderheiten aufweisen.'\nNegara-negara yang secara resmi diwakili oleh singkatan huruf 'D', 'A', dan 'CH' adalah...",
        "correct": "Deutschland (D), Österreich (A - Austria), dan die Schweiz (CH - Confoederatio Helvetica).",
        "distractors": [
            "Dänemark (D), Australien (A), dan Chile (CH) yang secara geografis berada di benua berbeda.",
            "Deutschland (D), Amsterdam (A), dan Chemnitz (CH) yang mengacaukan nama negara dengan nama kota.",
            "Dresden (D), Athen (A), dan Cham (CH) yang sama sekali tidak merepresentasikan aliansi negara penutur bahasa Jerman.",
            "Deutschland (D), Andorra (A), dan China (CH) yang keliru secara rumpun linguistik bahasa Jermanik."
        ],
        "formula": {
            "title": "D-A-CH RAUM (DEUTSCHSPRACHIGER RAUM)",
            "latex": "\\text{D = Deutschland}, \\quad \\text{A = Österreich (Austria)}, \\quad \\text{CH = die Schweiz (Confoederatio Helvetica)}",
            "legend": "• Kode pelat kendaraan internasional resmi ketiga negara.<br>• Menandai kawasan budaya dan penutur asli bahasa Jerman di Eropa Tengah."
        },
        "hints": {
            "concept": "Singkatan 'D-A-CH' berasal dari kode internasional resmi kendaraan bermotor: D = Deutschland (Jerman), A = Austria (Österreich dalam bahasa Latin/internasional), dan CH = Confoederatio Helvetica (nama resmi Konfederasi Swiss dalam bahasa Latin).",
            "execution": "D = Deutschland, A = Österreich, CH = die Schweiz."
        }
    },
    {
        "id": "ger-lat-h-25",
        "materi": "GRAMMATIK LANJUTAN: INDIREKTE REDE (KONJUNKTIV I)",
        "topic": "Penggunaan Konjunktiv I Orang Ketiga Tunggal dalam Laporan Berita Jurnalistik",
        "stem": "Dalam warta berita harian mengenai pernyataan menteri keuangan:\n'Der Finanzminister erklärte gestern auf der Pressekonferenz, die Inflation ( ... ) im kommenden Quartal spürbar zurückgehen.'\nBentuk kata kerja bantu Konjunktiv I orang ketiga tunggal yang TEPAT untuk laporan wicara tak langsung (indirekte Rede) adalah...",
        "correct": "werde (bentuk Konjunktiv I orang ketiga tunggal dari verba werden untuk mengutip pernyataan netral pihak ketiga).",
        "distractors": [
            "wird (bentuk indikatif Präsens yang menyatakan fakta kepastian mutlak pembicara sendiri, bukan kutipan jurnalistik).",
            "würde (bentuk Konjunktiv II yang lazim dipakai untuk kalimat pengandaian atau pengganti bila bentuk Konjunktiv I rancu).",
            "worden (bentuk Partizip II pasif yang salah fungsi sintaksis).",
            "geworden sei (bentuk lampau Perfekt yang bertentangan dengan keterangan waktu masa depan im kommenden Quartal)."
        ],
        "formula": {
            "title": "INDIREKTE REDE: KONJUNKTIV I",
            "latex": "\\text{Aussage: \"Die Inflation wird zurückgehen.\" } \\rightarrow \\text{Er sagte, die Inflation } \\mathbf{werde} \\text{ zurückgehen.}",
            "legend": "• Bahasa jurnalistik Jerman menggunakan Konjunktiv I untuk menjaga jarak objektifitas pelaporan.<br>• er/sie/es (die Inflation) $\\rightarrow$ werde (akar verb wer- + -e)."
        },
        "hints": {
            "concept": "Dalam bahasa jurnalistik dan berita resmi Jerman, kutipan pernyataan pihak ketiga (indirekte Rede) wajib menggunakan Konjunktiv I untuk menunjukkan netralitas laporan. Bentuk Konjunktiv I orang ketiga tunggal (die Inflation = sie) dari verba 'werden' adalah 'werde'.",
            "execution": "Orang ketiga tunggal Konjunktiv I = 'werde'."
        }
    }
]
