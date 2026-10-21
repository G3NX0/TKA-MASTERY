# -*- coding: utf-8 -*-
"""
BAHASA JERMAN - PAKET SOAL LATIHAN MENENGAH (MEDIUM) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / CEFR A2-B1 (Goethe-Zertifikat A2/B1)
Distribusi:
- 8 Butir: Dativ & Verben mit Dativ (helfen, danken, gefallen, gehören, schmecken) serta Personalpronomen im Dativ
- 9 Butir: Preposisi Kasus (Dativ-Präpositionen: aus, bei, mit, nach, seit, von, zu; Wechselpräpositionen Akkusativ vs Dativ dengan pasangan stellen/stehen, legen/liegen)
- 8 Butir: Perfekt (haben vs sein, Partizip II), Komparativ/Superlativ, serta Konjunktionen mit Nebensatz (weil, dass, wenn)
"""

BAHASA_JERMAN_MEDIUM_ITEMS = [
    {
        "id": "ger-lat-m-01",
        "materi": "GRAMMATIK: VERBEN MIT DATIV",
        "topic": "Kata Kerja 'helfen' yang Menuntut Objek Tak Langsung (Dativ)",
        "stem": "Seorang kakek membawa koper yang sangat berat di peron kereta api:\n'Entschuldigen Sie, junger Mann! Könnten Sie ( ... ) bitte beim Tragen dieses schweren Koffers helfen?'\nBentuk kata ganti orang (Personalpronomen) yang TEPAT untuk objek verba 'helfen' pada persona pertama tunggal adalah...",
        "correct": "mir (pronomina persona pertama tunggal dalam kasus Dativ yang dituntut oleh verba 'helfen').",
        "distractors": [
            "mich (pronomina persona pertama tunggal dalam kasus Akkusativ yang keliru untuk verba helfen).",
            "mein (bentuk dasar kepemilikan yang tidak dapat berdiri sendiri sebagai objek pronominal).",
            "meiner (bentuk genitiv atau feminin dativ yang tidak sesuai secara kategori persona).",
            "ich (pronomina persona pertama tunggal dalam kasus Nominativ yang hanya berfungsi sebagai subjek)."
        ],
        "formula": {
            "title": "VERB MIT DATIV: HELFEN",
            "latex": "\\text{helfen} + \\text{Dativ} \\quad (\\text{ich } \\rightarrow \\text{mir})",
            "legend": "• Verba intrik Dativ: helfen, danken, antworten, gratulieren, gehören, gefallen.<br>• Objek penderita dalam bahasa Indonesia menjadi objek Dativ dalam bahasa Jerman."
        },
        "hints": {
            "concept": "Kata kerja 'helfen' (menolong) dalam bahasa Jerman merupakan verba intransitif yang mewajibkan objeknya berada dalam kasus Dativ, bukan Akkusativ. Bentuk Dativ dari kata ganti 'ich' adalah 'mir'.",
            "execution": "'helfen' + Dativ = 'Könnten Sie mir helfen?'"
        }
    },
    {
        "id": "ger-lat-m-02",
        "materi": "GRAMMATIK: WECHSELPRAEPOSITIONEN (WOHIN VS WO)",
        "topic": "Kontras Tindakan Dinamis (stellen + Akkusativ) vs Status Diam (stehen + Dativ)",
        "stem": "Ibu memberikan instruksi penataan ruang tamu kepada anaknya:\n'Bitte stelle die Stehlampe ( ... ) Ecke! Dort ( ... ) sie am besten und stört niemanden.'\nPasangan frasa preposisi dan kata kerja yang TEPAT untuk melengkapi kalimat tersebut adalah...",
        "correct": "in die / steht (tindakan dinamis 'in die Ecke' memakai Akkusativ, dan posisi diam memakai verba 'stehen').",
        "distractors": [
            "in der / stellt (penggunaan kasus Dativ yang keliru pada verba dinamis serta verba aktif untuk posisi diam).",
            "an die / liegt (penggunaan verba berbaring 'liegen' yang keliru untuk benda yang berdiri tegak seperti lampu).",
            "auf der / sitzt (kombinasi preposisi di atas permukaan dan verba duduk yang tidak masuk akal untuk lampu sudut).",
            "hinter den / steht (kasus maskulin Akkusativ yang keliru untuk kata benda bergender feminin die Ecke)."
        ],
        "formula": {
            "title": "WECHSELPRÄPOSITIONEN & VERBENPAARE",
            "latex": "\\text{stellen (Aktion, Wohin?)} \\rightarrow \\text{Akkusativ}, \\quad \\text{stehen (Zustand, Wo?)} \\rightarrow \\text{Dativ}",
            "legend": "• die Ecke (feminin): Akkusativ = in die Ecke.<br>• Stehlampe steht = posisi tegak diam (stehen)."
        },
        "hints": {
            "concept": "Verba 'stellen' (menempatkan berdiri) menjawab pertanyaan 'Wohin?' (dinamis) sehingga Wechselpräposition 'in' menuntut Akkusativ (in die Ecke). Setelah ditempatkan, lampu tersebut berada dalam posisi diam berdiri tegak, sehingga digunakan verba 'stehen'.",
            "execution": "Wohin? -> in die Ecke (feminin Akkusativ). Benda berdiri tegak diam -> sie steht."
        }
    },
    {
        "id": "ger-lat-m-03",
        "materi": "GRAMMATIK: PRÄPOSITIONEN MIT DATIV (MIT)",
        "topic": "Preposisi Sarana Transportasi 'mit' yang Mewajibkan Kasus Dativ",
        "stem": "Dalam survei mobilitas komuter di kota Frankfurt:\n'Viele Angestellte fahren morgens nicht mit dem Auto, sondern ( ... ) U-Bahn zur Arbeit, um Staus zu vermeiden.'\nBentuk artikel yang TEPAT setelah preposisi Dativ 'mit' untuk kata benda feminin 'U-Bahn' adalah...",
        "correct": "mit der (preposisi 'mit' mewajibkan Dativ; artikel feminin Dativ adalah 'der').",
        "distractors": [
            "mit die (keliru karena mempertahankan artikel Nominativ/Akkusativ feminin).",
            "mit den (keliru karena merupakan artikel Akkusativ maskulin atau Dativ jamak).",
            "mit dem (keliru karena merupakan artikel maskulin atau netral dalam kasus Dativ).",
            "mit einer (kurang tepat dalam frasa idiomatis sarana transportasi umum harian komuter)."
        ],
        "formula": {
            "title": "DATIV-PRÄPOSITION: MIT",
            "latex": "\\text{Präposition } \\mathbf{mit} + \\text{Dativ} \\quad (\\text{die U-Bahn } \\rightarrow \\text{mit der U-Bahn})",
            "legend": "• Preposisi Dativ murni: aus, bei, mit, nach, seit, von, zu (Blue Danube Song).<br>• Feminin Dativ: die $\\rightarrow$ der."
        },
        "hints": {
            "concept": "Preposisi 'mit' (dengan/menggunakan) selalu menuntut kasus Dativ. Kata benda 'die U-Bahn' adalah feminin tunggal. Dalam kasus Dativ, artikel tentu feminin berubah dari 'die' menjadi 'der'.",
            "execution": "'mit' + Dativ feminin = 'mit der U-Bahn'."
        }
    },
    {
        "id": "ger-lat-m-04",
        "materi": "GRAMMATIK: PERFEKT MIT SEIN",
        "topic": "Penggunaan Kata Kerja Bantu 'sein' untuk Verba Perpindahan Tempat",
        "stem": "Setelah liburan musim panas, seorang siswa bercerita kepada guru:\n'In den Ferien ( ... ) meine Familie und ich für zwei Wochen nach Wien ( ... ).'\nPasangan kata kerja bantu (Hilfsverb) dan bentuk lampau (Partizip II) yang TEPAT dari verba 'fahren' adalah...",
        "correct": "sind / gefahren (verba perpindahan lokasi 'fahren' membentuk Perfekt dengan 'sein'; subjek jamak memakai 'sind').",
        "distractors": [
            "haben / gefahren (keliru karena verba gerak perpindahan tempat tidak membentuk Perfekt dengan haben).",
            "haben / gefahrt (keliru kata kerja bantu dan bentuk Partizip II yang diregulerkan secara salah).",
            "sind / geffahrt (kesalahan ejaan bentuk Partizip II dari verba kuat fahren).",
            "waren / gefahren (membentuk Plusquamperfekt yang tidak lazim untuk narasi lisan sederhana)."
        ],
        "formula": {
            "title": "PERFEKT MIT SEIN (ORTSWECHSEL)",
            "latex": "\\text{Subjek Plural} + \\mathbf{sind} + \\dots + \\text{Partizip II (}\\mathbf{gefahren}\\text{)}",
            "legend": "• Kriteria 'sein': Perpindahan tempat (Ortswechsel), perubahan status (Zustandswechsel), atau sein/bleiben.<br>• Subjek: 'meine Familie und ich' = wir $\\rightarrow$ sind."
        },
        "hints": {
            "concept": "Kata kerja yang menunjukkan perpindahan tempat (Ortswechsel) seperti 'fahren', 'gehen', 'fliegen' membentuk kala Perfekt dengan kata kerja bantu 'sein'. Subjek 'meine Familie und ich' setara dengan persona jamak 'wir' (sind).",
            "execution": "Wir -> sind. Partizip II dari fahren -> gefahren. Pilihan tepat: sind / gefahren."
        }
    },
    {
        "id": "ger-lat-m-05",
        "materi": "GRAMMATIK: NEBENSATZ MIT 'WEIL'",
        "topic": "Struktur Kalimat Anak Kausalitas dengan Verba di Posisi Paling Akhir",
        "stem": "Leon tidak dapat menghadiri pesta ulang tahun temannya:\n'Leon kommt heute leider nicht zur Geburtstagsparty, weil er ( ... ).'\nSusunan klausa anak (Nebensatz) yang BENAR sesuai kaidah gramatika bahasa Jerman adalah...",
        "correct": "sich für die wichtige Prüfung vorbereiten muss (verba berkonjugasi 'muss' ditempatkan di posisi paling akhir klausa).",
        "distractors": [
            "muss sich für die wichtige Prüfung vorbereiten (urutan Hauptsatz yang keliru diterapkan setelah konjungsi subordinatif weil).",
            "sich vorbereiten muss für die wichtige Prüfung (keterangan preposisi diletakkan di luar kerangka kalimat anak / Ausklammerung keliru).",
            "für die wichtige Prüfung muss sich vorbereiten (posisi verba bantu menyela di tengah klausa subordinat).",
            "vorbereiten sich muss für die Prüfung (susunan acak yang melanggar hukum urutan pronomina refleksif)."
        ],
        "formula": {
            "title": "NEBENSATZ MIT WEIL (VERB-LETZT-STELLUNG)",
            "latex": "\\text{weil} + \\text{Subjekt} + \\dots + \\text{Infinitiv} + \\mathbf{konjugiertes Verb (Ende)}",
            "legend": "• Konjungsi subordinatif (weil, dass, wenn, ob) memindahkan verba berkonjugasi ke posisi paling akhir.<br>• Struktur: ... weil er sich ... vorbereiten muss."
        },
        "hints": {
            "concept": "Kata penghubung subordinatif 'weil' (karena) membentuk kalimat anak (Nebensatz). Aturan baku Nebensatz mengharuskan kata kerja berkonjugasi (finite verb) berpindah ke posisi paling akhir kalimat.",
            "execution": "Subjek 'er', infinitif 'vorbereiten', dan verba modal berkonjugasi 'muss' wajib berada di ujung akhir: '... vorbereiten muss'."
        }
    },
    {
        "id": "ger-lat-m-06",
        "materi": "GRAMMATIK: DATIV-OBJEKT & PERSONALPRONOMEN",
        "topic": "Kata Kerja 'gefallen' dan Penggunaan Kata Ganti Orang Ketiga Jamak 'ihnen'",
        "stem": "Para turis sangat menikmati keindahan kota tua Heidelberg:\n'Die alten Schlösser und engen Gassen in Heidelberg gefallen ( ... ) unglaublich gut.'\nBentuk pronomina persona ketiga jamak (mereka) dalam kasus Dativ yang TEPAT adalah...",
        "correct": "ihnen (pronomina persona ketiga jamak dalam kasus Dativ yang dituntut oleh verba 'gefallen').",
        "distractors": [
            "sie (pronomina persona ketiga jamak dalam kasus Nominativ atau Akkusativ).",
            "ihr (pronomina persona ketiga feminin tunggal dalam kasus Dativ atau persona kedua jamak Nominativ).",
            "ihrem (bentuk kepemilikan maskulin/netral Dativ tunggal yang tidak dapat berdiri sendiri).",
            "Ihnen (bentuk honorifik sopan persona kedua Anda yang keliru untuk merujuk turis pihak ketiga)."
        ],
        "formula": {
            "title": "VERB MIT DATIV: GEFALLEN",
            "latex": "\\text{etwas (Nom.) gefällt / gefallen} + \\text{jemandem (Dativ)}",
            "legend": "• Subjek gramatikal adalah hal yang disukai (die Schlösser = Plural $\\rightarrow$ gefallen).<br>• Orang yang menyukai menempati posisi kasus Dativ: sie (jamak) $\\rightarrow$ ihnen."
        },
        "hints": {
            "concept": "Kata kerja 'gefallen' (menyenangkan/disukai) menggunakan konstruksi: Subjek (hal yang disukai) + gefallen + Dativ (orang yang menyukai). Objek untuk 'mereka' (para turis) dalam kasus Dativ adalah 'ihnen' (huruf kecil).",
            "execution": "Pronomina Dativ orang ketiga jamak = 'ihnen'."
        }
    },
    {
        "id": "ger-lat-m-07",
        "materi": "GRAMMATIK: KOMPARATIV & SUPERLATIV (UNREGELMÄSSIG)",
        "topic": "Tingkat Perbandingan Tidak Teratur untuk Adjektiva 'gern' (gern - lieber - am liebsten)",
        "stem": "Dalam wawancara mengenai kegemaran membaca dan menonton:\n'Ich lese gern historische Romane, aber noch ( ... ) sehe ich mir Dokumentarfilme über Natur an.'\nBentuk perbandingan tingkat lebih (Komparativ) yang TEPAT dari kata keterangan 'gern' adalah...",
        "correct": "lieber (bentuk komparatif tidak teratur dari gern yang bermakna 'lebih suka').",
        "distractors": [
            "gerner (bentuk perbandingan teratur buatan yang keliru dan tidak ada dalam bahasa Jerman baku).",
            "am liebsten (bentuk superlatif tingkat paling tinggi yang membutuhkan partikel am).",
            "besser (bentuk komparatif dari kata sifat gut yang bermakna lebih baik kualitasnya).",
            "mehr (bentuk komparatif dari kata sifat viel yang bermakna lebih banyak kuantitasnya)."
        ],
        "formula": {
            "title": "STEIGERUNG VON GERN",
            "latex": "\\text{Positiv: gern} \\quad \\rightarrow \\quad \\text{Komparativ: lieber} \\quad \\rightarrow \\quad \\text{Superlativ: am liebsten}",
            "legend": "• 'noch lieber' = bahkan lebih suka lagi.<br>• Adverbia frekuensi preferensi emosional."
        },
        "hints": {
            "concept": "Kata keterangan 'gern' (suka/senang melakukan) memiliki bentuk perbandingan tidak teratur (unregelmäßige Steigerung): gern -> lieber (lebih suka) -> am liebsten (paling suka).",
            "execution": "Tingkat komparatif (lebih suka) = 'lieber'."
        }
    },
    {
        "id": "ger-lat-m-08",
        "materi": "GRAMMATIK: PRÄPOSITIONEN MIT DATIV (SEIT)",
        "topic": "Preposisi Durasi Waktu Lampau yang Masih Berlangsung (seit + Dativ)",
        "stem": "Seorang ekspatriat menceritakan lama tinggalnya di Jerman:\n'Herr Meyer wohnt schon ( ... ) einem ganzen Jahr in Hamburg und lernt fleißig Deutsch.'\nPreposisi temporal yang TEPAT untuk menyatakan peristiwa yang dimulai di masa lalu dan masih berlangsung hingga kini adalah...",
        "correct": "seit (preposisi temporal Dativ yang menyatakan aksi yang telah dimulai di masa lampau dan terus berlanjut).",
        "distractors": [
            "vor (preposisi temporal Dativ yang menyatakan peristiwa lampau yang sudah selesai sepenuhnya).",
            "ab (preposisi yang menyatakan titik awal masa kini atau masa depan).",
            "bis (preposisi Akkusativ yang menyatakan batas akhir waktu kejadian).",
            "in (preposisi waktu yang menyatakan durasi di masa depan: in einem Jahr = setahun lagi)."
        ],
        "formula": {
            "title": "TEMPORALE PRÄPOSITION: SEIT",
            "latex": "\\mathbf{seit} + \\text{Dativ (Präsens)} = \\text{Aksi dimulai di masa lalu & masih berlanjut}",
            "legend": "• das Jahr (netral): Dativ = einem Jahr.<br>• Menggunakan kala Präsens (wohnt schon seit einem Jahr)."
        },
        "hints": {
            "concept": "Preposisi 'seit' selalu diikuti kasus Dativ dan digunakan untuk aksi yang dimulai pada masa lampau namun masih berlangsung saat ini. Kalimatnya menggunakan verba dalam bentuk waktu sekarang (Präsens).",
            "execution": "Sudah setahun dan masih tinggal di sana = 'seit einem ganzen Jahr'."
        }
    },
    {
        "id": "ger-lat-m-09",
        "materi": "GRAMMATIK: NEBENSATZ MIT 'DASS'",
        "topic": "Klausa Objek Subordinatif dengan Konjungsi 'dass'",
        "stem": "Dokter memberikan kepastian diagnosis kepada pasien:\n'Der Arzt hat mir gestern versichert, ( ... ) die Operation völlig schmerzfrei verlaufen wird.'\nKata penghubung subordinatif yang TEPAT untuk menghubungkan klausa isi pernyataan faktual adalah...",
        "correct": "dass (kata sambung subordinatif 'bahwa' yang mengantarkan klausa isi dan memindahkan verba ke akhir).",
        "distractors": [
            "das (artikel tentu atau pronomina relatif netral yang keliru secara fungsi konjungsi).",
            "ob (kata sambung subordinatif 'apakah' yang digunakan untuk kalimat tanya tidak langsung).",
            "weil (kata sambung kausalitas 'karena' yang menyatakan alasan logis, bukan isi penegasan).",
            "damit (kata sambung finalitas 'supaya/agar' yang menyatakan tujuan perbuatan)."
        ],
        "formula": {
            "title": "OBJEKTSATZ MIT DASS",
            "latex": "\\text{Hauptsatz (versichert)} + , \\mathbf{dass} + \\dots + \\text{Verb-Ende (verlaufen wird)}",
            "legend": "• Konjungsi 'dass' (bahwa) mengawali klausa komplemen objek dari verba wicara/pikiran.<br>• Wajib diawali tanda koma dan dieja dengan 'ss'."
        },
        "hints": {
            "concept": "Konjungsi 'dass' (bahwa) digunakan untuk mengantarkan klausa isi pikiran, ucapan, atau keyakinan (Objektsatz). Konjungsi ini bersifat subordinatif sehingga kata kerja finite (wird) berada di posisi paling akhir kalimat anak.",
            "execution": "Klausa isi pernyataan (bahwa operasi akan berjalan tanpa rasa sakit) = 'dass'."
        }
    },
    {
        "id": "ger-lat-m-10",
        "materi": "GRAMMATIK: PRÄTERITUM DER MODALVERBEN",
        "topic": "Bentuk Lampau Präteritum dari Modalverb 'können' (konnte)",
        "stem": "Jonas menceritakan alasan ia tidak masuk sekolah kemarin:\n'Gestern hatte ich hohes Fieber, deshalb ( ... ) ich leider nicht zum Unterricht kommen.'\nBentuk lampau sederhana (Präteritum) dari modalverb 'können' yang TEPAT untuk subjek 'ich' adalah...",
        "correct": "konnte (bentuk Präteritum persona pertama tunggal dari modalverb 'können' tanpa tanda umlaut).",
        "distractors": [
            "könnte (bentuk Konjunktiv II yang menyatakan pengandaian hipotetis atau kesantunan bersyarat).",
            "konntest (bentuk Präteritum persona kedua tunggal untuk subjek du).",
            "kann (bentuk Präsens sekarang yang bertentangan dengan keterangan waktu lampau gestern).",
            "gekonnt (bentuk Partizip II yang membutuhkan kata kerja bantu haben dalam konstruksi Perfekt)."
        ],
        "formula": {
            "title": "PRÄTERITUM DER MODALVERBEN: KÖNNEN",
            "latex": "\\text{ich konnte}, \\quad \\text{du konntest}, \\quad \\text{er/sie/es konnte}, \\quad \\text{wir konnten}",
            "legend": "• Seluruh modalverben kehilangan tanda Umlaut pada bentuk Präteritum.<br>• Persona 'ich' dan 'er/sie/es' identik tanpa sufiks -t: konnte."
        },
        "hints": {
            "concept": "Kala lampau sederhana (Präteritum) dari modalverb 'können' dibentuk tanpa Umlaut: konnte, konntest, konnte, konnten, konntet, konnten. Untuk persona pertama tunggal (ich), bentuknya adalah 'konnte'.",
            "execution": "Keterangan waktu 'gestern' + subjek 'ich' -> 'konnte'."
        }
    },
    {
        "id": "ger-lat-m-11",
        "materi": "GRAMMATIK: WECHSELPRAEPOSITIONEN (LEGEN VS LIEGEN)",
        "topic": "Distingsi Tindakan Meletakkan Datar (legen) vs Keadaan Berbaring (liegen)",
        "stem": "Setelah selesai membaca majalah, ayah berkata:\n'Ich ( ... ) die Zeitschrift auf den Wohnzimmertisch, und jetzt ( ... ) sie dort neben der Vase.'\nPasangan kata kerja yang TEPAT untuk melengkapi tindakan dinamis dan keadaan statis tersebut adalah...",
        "correct": "lege / liegt (verba aktif-dinamis 'legen' menuntut Akkusativ 'auf den Tisch', dan verba statis 'liegen' menyatakan letak).",
        "distractors": [
            "liege / legt (kombinasi terbalik yang rancu secara logika semantik gerak dan status benda).",
            "stelle / steht (verba untuk posisi berdiri tegak vertikal yang tidak sesuai untuk majalah tipis yang diletakkan mendatar).",
            "setze / sitzt (verba yang lazim digunakan untuk makhluk hidup atau benda berwujud boneka yang didudukkan).",
            "hänge / hängt (verba yang digunakan untuk menggantung benda pada dinding atau gantungan baju)."
        ],
        "formula": {
            "title": "VERBENPAAR: LEGEN VS LIEGEN",
            "latex": "\\text{legen (Aktion, Wohin? + Akk)} \\quad \\leftrightarrow \\quad \\text{liegen (Zustand, Wo? + Dat)}",
            "legend": "• Majalah (Zeitschrift) diletakkan secara horizontal/datar $\\rightarrow$ legen/liegen.<br>• Aksi: Ich lege ... auf den Tisch. Status: Sie liegt dort."
        },
        "hints": {
            "concept": "Kata kerja 'legen' adalah verba teratur aktif/dinamis (meletakkan secara mendatar) yang menjawab pertanyaan 'Wohin?' (auf den Tisch - Akkusativ). Kata kerja 'liegen' adalah verba kuat intransitif/statis (tergeletak/terbaring mendatar) yang menjawab 'Wo?'.",
            "execution": "Aksi pertama 'ich lege', keadaan berikutnya 'sie liegt'. Pilihan tepat: lege / liegt."
        }
    },
    {
        "id": "ger-lat-m-12",
        "materi": "GRAMMATIK: NEBENSATZ MIT 'WENN' (KONDISIONAL/TEMPORAL)",
        "topic": "Penggunaan Konjungsi 'wenn' untuk Kalimat Pengandaian Nyata atau Kebiasaan Berulang",
        "stem": "Seorang kawan menyarankan kegiatan saat cuaca cerah di akhir pekan:\n'( ... ) das Wetter am Samstag schön bleibt, machen wir einen Tagesausflug in den Schwarzwald.'\nKata penghubung subordinatif yang TEPAT untuk mengawali klausa syarat atau kondisi tersebut adalah...",
        "correct": "Wenn (konjungsi subordinatif bersyarat/temporal yang bermakna 'jika / apabila' dan memindahkan verba ke akhir).",
        "distractors": [
            "Wann (kata tanya interogatif yang hanya menanyakan waktu temporal spesifik, bukan konjungsi syarat).",
            "Als (konjungsi temporal masa lampau untuk peristiwa tunggal definit di masa lalu).",
            "Ob (konjungsi keraguan yang bermakna 'apakah' pada kalimat tidak langsung).",
            "Weil (konjungsi kausalitas yang menyatakan alasan peristiwa yang sudah pasti terjadi)."
        ],
        "formula": {
            "title": "KONDITIONALSATZ MIT WENN",
            "latex": "\\mathbf{Wenn} + \\text{Subjekt} + \\dots + \\text{Verb (bleibt)}, \\quad \\text{Verb (machen)} + \\text{Subjekt} + \\dots",
            "legend": "• Konjungsi 'wenn' memicu Verb-Letzt pada anak kalimat dan Verb-Erst pada induk kalimat.<br>• Memuat makna kondisional (jika/apabila cuaca tetap bagus)."
        },
        "hints": {
            "concept": "Konjungsi 'wenn' digunakan untuk menyatakan kondisi/syarat (jika/apabila) atau waktu kejadian yang berulang/masa depan (setiap kali/bila). Perhatikan bahwa 'wann' hanyalah kata tanya, bukan konjungsi penyambung klausa syarat.",
            "execution": "Klausa pengandaian masa depan 'jika cuaca bagus' = 'Wenn'."
        }
    },
    {
        "id": "ger-lat-m-13",
        "materi": "GRAMMATIK: REFLEXIVE VERBEN MIT AKKUSATIV",
        "topic": "Verba Refleksif 'sich freuen auf' untuk Menantikan Peristiwa Masa Depan",
        "stem": "Murid-murid menyambut antusias rencana kunjungan museum:\n'Alle Schüler freuen ( ... ) schon riesig auf die bevorstehende Klassenfahrt nach Berlin.'\nBentuk kata ganti refleksif (Reflexivpronomen) yang TEPAT untuk subjek persona ketiga jamak 'alle Schüler' adalah...",
        "correct": "sich (pronomina refleksif baku untuk persona ketiga tunggal maupun jamak).",
        "distractors": [
            "euch (pronomina refleksif untuk persona kedua jamak subjek ihr).",
            "uns (pronomina refleksif untuk persona pertama jamak subjek wir).",
            "sie (bukan pronomina refleksif, melainkan pronomina persona biasa yang salah secara sintaksis refleksif).",
            "ihnen (pronomina persona Dativ biasa yang tidak berfungsi sebagai penanda refleksif verba sich freuen)."
        ],
        "formula": {
            "title": "REFLEXIVPRONOMEN IM AKKUSATIV",
            "latex": "\\text{Subjekt: er/sie/es/sie(Pl.)} \\quad \\rightarrow \\quad \\text{Reflexivpronomen: } \\mathbf{sich}",
            "legend": "• sich freuen auf (+Akk) = menantikan dengan gembira peristiwa yang akan datang.<br>• Persona ketiga selalu menggunakan 'sich'."
        },
        "hints": {
            "concept": "Kata kerja 'sich freuen' adalah verba refleksif. Untuk subjek persona ketiga, baik tunggal (er/sie/es) maupun jamak (sie/Plural), pronomina refleksifnya selalu 'sich'.",
            "execution": "Subjek jamak 'Alle Schüler' (= sie) -> pronomina refleksif adalah 'sich'."
        }
    },
    {
        "id": "ger-lat-m-14",
        "materi": "GRAMMATIK: PERFEKT MIT HABEN & UNTRENNBARE VERBEN",
        "topic": "Pembentukan Partizip II Verba dengan Prefiks Tak Terpisah (ver-)",
        "stem": "Felix meminta maaf karena datang terlambat ke pertemuan:\n'Entschuldigung für die Verspätung! Ich habe meinen Zug nach Köln leider ( ... ).'\nBentuk Partizip II yang BENAR dari kata kerja tak terpisah 'verpassen' (ketinggalan kereta) adalah...",
        "correct": "verpasst (dibentuk tanpa awalan ge- karena memiliki prefiks tak terpisah 'ver-').",
        "distractors": [
            "geverpasst (kesalahan penambahan awalan ge- di depan prefiks tak terpisah).",
            "verpassen (bentuk infinitif yang belum diubah ke dalam bentuk Partizip II).",
            "verpasset (bentuk arkais dengan sisipan vokal -e- yang keliru secara ortografi modern).",
            "gepasst (merupakan Partizip II dari verba dasar passen yang maknanya berubah total menjadi cocok/muat)."
        ],
        "formula": {
            "title": "PARTIZIP II UNTRENNBARER VERBEN",
            "latex": "\\text{Präfixe: be-, emp-, ent-, er-, ge-, miss-, ver-, zer-} \\rightarrow \\text{OHNE ge-}",
            "legend": "• verpassen: ver- (untrennbar) + pass (akar) + -t (akhiran teratur) = verpasst.<br>• Dilarang keras menambahkan awalan 'ge-'."
        },
        "hints": {
            "concept": "Kata kerja dengan prefiks tidak terpisah (untrennbare Präfixe: be-, emp-, ent-, er-, ge-, miss-, ver-, zer-) membentuk Partizip II TANPA awalan 'ge-'. Bentuk lampau dari 'verpassen' adalah 'verpasst'.",
            "execution": "verpassen -> ver- + pass + -t = verpasst."
        }
    },
    {
        "id": "ger-lat-m-15",
        "materi": "WORTSCHATZ & LESEVERSTEHEN: WOHNUNGSANZEIGE",
        "topic": "Memahami Singkatan Standar dalam Iklan Sewa Apartemen di Jerman",
        "stem": "Dalam iklan properti di koran Jerman tertulis:\n'Schöne 3-Zi.-Whg., 75 qm, EBK, Balkon, KM 850 € + NK 180 €.'\nBerdasarkan konvensi sewa tempat tinggal di Jerman, singkatan 'KM' dan 'NK' merujuk pada...",
        "correct": "Kaltmiete (biaya sewa dasar tanpa pemanas/utilitas) dan Nebenkosten (biaya utilitas tambahan seperti air dan sampah).",
        "distractors": [
            "Kilometer (jarak menuju pusat kota) dan Notkosten (dana darurat perbaikan gedung apartemen).",
            "Kautionsmiete (uang jaminan deposit awal) dan Netto-Kosten (biaya bersih setelah pemotongan pajak).",
            "Küchenmiete (biaya khusus sewa perabot dapur) dan Nachzahlung (denda keterlambatan pembayaran bulanan).",
            "Komfortmiete (biaya fasilitas kemewahan gedung) dan Nebenkonto (nomor rekening perbankan sekunder pengelola)."
        ],
        "formula": {
            "title": "WOHNUNGSABKÜRZUNGEN",
            "latex": "\\text{Warmmiete (Total)} = \\text{KM (Kaltmiete)} + \\text{NK (Nebenkosten)}",
            "legend": "• KM = Kaltmiete (biaya murni pemakaian ruang apartemen).<br>• NK = Nebenkosten (biaya operasional pemanas, air, kebersihan, pembuangan sampah)."
        },
        "hints": {
            "concept": "Dalam iklan sewa hunian di Jerman, 'KM' adalah singkatan dari 'Kaltmiete' (biaya sewa dingin/murni ruang tanpa energi dan utilitas). 'NK' adalah singkatan dari 'Nebenkosten' (biaya sampingan mencakup air, pemanas, kebersihan lingkungan, dan sampah).",
            "execution": "KM = Kaltmiete, NK = Nebenkosten."
        }
    },
    {
        "id": "ger-lat-m-16",
        "materi": "GRAMMATIK: PRÄPOSITIONEN MIT DATIV (ZU)",
        "topic": "Preposisi Arah Tujuan Orang/Institusi 'zu' dengan Kontraksi Kasus Dativ",
        "stem": "Pasien yang sedang demam tinggi menelpon tempat kerjanya:\n'Ich fühle mich heute gar nicht gut und gehe jetzt direkt ( ... ) Arzt.'\nBentuk kontraksi preposisi dan artikel Dativ yang TEPAT untuk tujuan profesi dokter (der Arzt) adalah...",
        "correct": "zum (kontraksi baku dari preposisi Dativ 'zu' + artikel maskulin 'dem').",
        "distractors": [
            "zur (kontraksi preposisi 'zu' + artikel feminin 'der' yang keliru untuk kata benda maskulin der Arzt).",
            "in den (penggunaan preposisi Akkusativ 'in' yang bermakna masuk secara harfiah ke dalam tubuh fisik sang dokter).",
            "nach dem (preposisi nach digunakan untuk nama kota/negara tanpa artikel atau urutan waktu, bukan persona).",
            "beim (kontraksi bei + dem yang menyatakan posisi statis sedang berada di tempat dokter, bukan arah tujuan pergerakan)."
        ],
        "formula": {
            "title": "PRÄPOSITION ZU + PERSON (DATIV)",
            "latex": "\\mathbf{zu} + \\text{Person/Beruf (Dativ)} \\quad \\rightarrow \\quad \\text{zu + dem} = \\mathbf{zum}",
            "legend": "• Menuju orang/profesi: selalu menggunakan preposisi 'zu'.<br>• Maskulin Dativ: der Arzt $\\rightarrow$ dem Arzt $\\rightarrow$ zum Arzt."
        },
        "hints": {
            "concept": "Untuk menyatakan pergerakan arah menuju seseorang atau figur profesi, bahasa Jerman menggunakan preposisi 'zu' (+ Dativ). Preposisi 'zu' berkontraksi dengan artikel maskulin 'dem' menjadi 'zum' (zum Arzt).",
            "execution": "zu + dem Arzt = 'zum Arzt'."
        }
    },
    {
        "id": "ger-lat-m-17",
        "materi": "GRAMMATIK: KATA TANYA TIDAK LANGSUNG (OB)",
        "topic": "Klausa Pertanyaan Tertutup Tidak Langsung dengan Konjungsi 'ob'",
        "stem": "Di pusat informasi stasiun pusat kereta api:\n'Können Sie mir bitte sagen, ( ... ) der Intercity-Express nach Hamburg heute planmäßig abfährt?'\nKata sambung subordinatif yang TEPAT untuk pertanyaan ya/tidak tidak langsung (indirekte Ja/Nein-Frage) adalah...",
        "correct": "ob (kata hubung yang bermakna 'apakah' untuk mengantarkan pertanyaan tidak langsung berbasis ya/tidak).",
        "distractors": [
            "dass (kata hubung yang bermakna 'bahwa' untuk pernyataan faktual positif yang sudah pasti).",
            "wenn (kata hubung syarat/kondisional yang bermakna 'jika/apabila').",
            "wann (kata tanya waktu spesifik yang mengabaikan kepastian keberangkatan terjadwal).",
            "wie (kata tanya cara/metode yang tidak cocok dengan konfirmasi ketepatan jadwal keberangkatan)."
        ],
        "formula": {
            "title": "INDIREKTE FRAGESÄTZE MIT OB",
            "latex": "\\text{Indirekte Ja/Nein-Frage: } \\mathbf{ob} + \\text{Subjekt} + \\dots + \\text{konjugiertes Verb (Ende)}",
            "legend": "• Pertanyaan langsung: Fährt der Zug planmäßig ab? (Ja/Nein)<br>• Menjadi pertanyaan tidak langsung: ... ob der Zug planmäßig abfährt."
        },
        "hints": {
            "concept": "Bila kalimat tanya tertutup (Ja/Nein-Frage) diubah menjadi kalimat tanya tidak langsung (indirekte Frage), kalimat tersebut dihubungkan dengan konjungsi subordinatif 'ob' (apakah). Kata kerja berkonjugasi pindah ke akhir klausa.",
            "execution": "Pertanyaan ya/tidak tidak langsung = 'ob'."
        }
    },
    {
        "id": "ger-lat-m-18",
        "materi": "GRAMMATIK: KOMPARATIV DENGAN 'ALS' & POSITIV DENGAN 'SO...WIE'",
        "topic": "Partikel Pembanding Derajat Lebih (Komparativ + als)",
        "stem": "Dua sahabat membandingkan rute perjalanan kereta api:\n'Die Fahrt mit dem Hochgeschwindigkeitszug ICE ist deutlich schneller ( ... ) die Reise mit dem Regionalexpress.'\nPartikel pembanding yang TEPAT untuk melengkapi tingkat perbandingan lebih (Komparativ) adalah...",
        "correct": "als (partikel pembanding wajib yang menyertai bentuk komparatif untuk menyatakan perbedaan derajat 'daripada').",
        "distractors": [
            "wie (partikel pembanding yang hanya digunakan pada derajat setara/Positiv: so schnell wie).",
            "denn (partikel pembanding arkais yang sudah usang dan digantikan sepenuhnya oleh als dalam bahasa modern).",
            "von (preposisi asal atau kepemilikan yang keliru digunakan sebagai pembanding ajektiva).",
            "zu (partikel yang bermakna terlalu intensif atau arah tujuan, bukan pembanding kualitas)."
        ],
        "formula": {
            "title": "VERGLEICHSPARTIKELN: ALS VS WIE",
            "latex": "\\text{Komparativ} + \\mathbf{als} \\quad (\\text{schneller als}), \\quad \\text{Positiv: } \\mathbf{so} \\dots \\mathbf{wie} \\quad (\\text{so schnell wie})",
            "legend": "• Bentuk komparatif berakhiran -er selalu dipasangkan dengan 'als'.<br>• Makna: jauh lebih cepat daripada..."
        },
        "hints": {
            "concept": "Dalam bahasa Jerman baku, bentuk perbandingan lebih (Komparativ, berakhiran -er) selalu menggunakan partikel 'als' (daripada). Bentuk setara menggunakan 'so ... wie' (sama ... seperti).",
            "execution": "schneller (Komparativ) -> pasangannya adalah 'als'."
        }
    },
    {
        "id": "ger-lat-m-19",
        "materi": "GRAMMATIK: PRÄPOSITIONEN MIT DATIV (NACH)",
        "topic": "Preposisi Temporal 'nach' yang Menyatakan Urutan Waktu Sesudah Peristiwa",
        "stem": "Dalam aturan pemakaian obat dari apotek:\n'Bitte nehmen Sie diese Tablette immer dreimal täglich ( ... ) dem Essen mit einem großen Glas Wasser ein.'\nPreposisi temporal yang TEPAT untuk menyatakan waktu 'sesudah makan' adalah...",
        "correct": "nach (preposisi temporal Dativ yang bermakna 'sesudah / setelah' suatu peristiwa atau waktu).",
        "distractors": [
            "vor (preposisi yang bermakna 'sebelum' makan, bertolak belakang dengan instruksi sesudah makan).",
            "während (preposisi Genitiv yang bermakna 'selama' proses makan berlangsung).",
            "zu (preposisi arah atau momen perayaan yang tidak lazim untuk petunjuk minum obat).",
            "in (preposisi yang menyatakan jangka waktu di masa depan, bukan urutan konsumsi obat)."
        ],
        "formula": {
            "title": "TEMPORALE PRÄPOSITION: NACH (+ DATIV)",
            "latex": "\\mathbf{nach} + \\text{Dativ} = \\text{sesudah / setelah}",
            "legend": "• das Essen (netral): Dativ = dem Essen.<br>• nach dem Essen = setelah makan."
        },
        "hints": {
            "concept": "Preposisi 'nach' (+ Dativ) dalam fungsi temporal berarti 'sesudah/setelah'. Kata benda 'das Essen' (makanan/makan) dalam Dativ menjadi 'dem Essen'.",
            "execution": "Sesudah makan = 'nach dem Essen'."
        }
    },
    {
        "id": "ger-lat-m-20",
        "materi": "GRAMMATIK: KATA SAMBUNG KOORDINATIF 'SONDERN'",
        "topic": "Penggunaan Konjungsi Korektif 'sondern' Setelah Kalimat Negatif",
        "stem": "Klaus meluruskan informasi mengenai jurusan kuliah adiknya:\n'Mein Bruder studiert nicht Medizin an der Universität München, ( ... ) er lernt Maschinenbau an der TU Berlin.'\nKata hubung koordinatif korektif yang TEPAT setelah kalimat negasi adalah...",
        "correct": "sondern (konjungsi koreksi yang bermakna 'melainkan' dan wajib didahului oleh klausula bernilai negatif).",
        "distractors": [
            "aber (konjungsi pertentangan umum yang tidak berfungsi mengoreksi elemen sanggahan mutlak sebelumnya).",
            "denn (konjungsi alasan kausalitas yang menyatakan sebab-akibat pembuktian).",
            "oder (konjungsi pilihan alternatif antara dua opsi yang terbuka).",
            "und (konjungsi penambahan yang tidak mengekspresikan koreksi kontradiksi faktual)."
        ],
        "formula": {
            "title": "KORREKTIVE KONJUNKTION: SONDERN",
            "latex": "\\text{nicht } A, \\quad \\mathbf{sondern} \\quad B \\quad (\\text{Posisi 0})",
            "legend": "• Syarat mutlak pemakaian 'sondern': Klausa pertama harus memuat negasi (nicht/kein).<br>• Berfungsi mengoreksi fakta: bukan A, melainkan B."
        },
        "hints": {
            "concept": "Konjungsi koordinatif 'sondern' (melainkan) digunakan secara khusus untuk membetulkan/mengoreksi suatu pernyataan, dengan syarat klausa sebelumnya wajib mengandung kata sangkal negatif (nicht atau kein).",
            "execution": "Ada negasi 'nicht Medizin' diikuti koreksi 'er lernt Maschinenbau' -> gunakan 'sondern'."
        }
    },
    {
        "id": "ger-lat-m-21",
        "materi": "GRAMMATIK: PRONOMI DATIV & AKKUSATIV (DOPPELTE OBJEKTE)",
        "topic": "Urutan Dua Pronomina Objek dalam Satu Klausa (Akkusativ sebelum Dativ)",
        "stem": "Ibu membelikan buku cerita baru untuk anaknya:\n'Hast du deinem kleinen Bruder das schöne Märchenbuch schon gegeben? — Ja, ich habe es ( ... ) eben gegeben.'\nBentuk pronomina persona ketiga maskulin tunggal (adik laki-laki) dalam kasus Dativ yang TEPAT adalah...",
        "correct": "ihm (pronomina persona ketiga maskulin tunggal dalam kasus Dativ: der Bruder -> ihm).",
        "distractors": [
            "ihn (pronomina persona ketiga maskulin tunggal dalam kasus Akkusativ yang keliru karena posisi objek langsung sudah diisi oleh es).",
            "er (pronomina persona Nominativ yang tidak dapat mengisi peran objek penerima bantuan).",
            "sein (kata ganti kepemilikan yang salah fungsi gramatikal pada struktur verba geben).",
            "ihr (pronomina Dativ feminin tunggal yang keliru gender untuk kata maskulin der Bruder)."
        ],
        "formula": {
            "title": "PRONOMEN-STELLUNG BEI ZWEI OBJEKTEN",
            "latex": "\\text{Wenn beide Objekte Pronomen sind: } \\mathbf{Akkusativ (es)} + \\mathbf{Dativ (ihm)}",
            "legend": "• das Märchenbuch (netral) = es (Akkusativ).<br>• der Bruder (maskulin) = ihm (Dativ penerima). Urutan: Ich habe es ihm gegeben."
        },
        "hints": {
            "concept": "Kata kerja 'geben' menuntut dua objek: Akkusativ (benda yang diberikan) dan Dativ (orang penerima). Bila kedua objek berbentuk kata ganti (Pronomen), urutannya adalah Akkusativ terlebih dahulu, disusul Dativ: 'ich habe es (Akk) ihm (Dat) gegeben'.",
            "execution": "Penerima adik laki-laki (der Bruder) dalam kasus Dativ adalah 'ihm'."
        }
    },
    {
        "id": "ger-lat-m-22",
        "materi": "GRAMMATIK: PERFEKT DENGAN VERBA KUAT TIDAK TERATUR",
        "topic": "Pembentukan Partizip II dari Verba 'schreiben' (geschrieben)",
        "stem": "Dalam korespondensi surat elektronik:\n'Frau Müller hat den ausführlichen Geschäftsbericht für den Vorstand bereits gestern Abend ( ... ).'\nBentuk Partizip II yang BENAR dari verba kuat 'schreiben' adalah...",
        "correct": "geschrieben (bentuk Partizip II verba kuat dengan perubahan vokal akar ei -> ie dan akhiran -en).",
        "distractors": [
            "geschreibt (bentuk lemah teratur buatan yang keliru untuk verba kuat schreiben).",
            "geschriben (kesalahan ejaan vokal pendek tanpa huruf -e pemanjang bunyi).",
            "schrieb (bentuk lampau Präteritum yang tidak boleh dipasangkan langsung dengan kata kerja bantu hat).",
            "geschriebenet (penambahan akhiran ganda yang melanggar morfologi bahasa Jerman)."
        ],
        "formula": {
            "title": "PARTIZIP II STARKER VERBEN: SCHREIBEN",
            "latex": "\\text{schreiben (Ablautreihe 1): } \\text{schreiben} \\rightarrow \\text{schrieb} \\rightarrow \\mathbf{geschrieben}",
            "legend": "• Verba kuat berakar vokal 'ei' umumnya berubah menjadi 'ie' pada Präteritum dan Partizip II.<br>• Akhiran Partizip II verba kuat adalah -en (ge-...-en)."
        },
        "hints": {
            "concept": "Verba 'schreiben' adalah verba kuat (starkes Verb). Pembentukan bentuk lampau Partizip II-nya mengalami pergeseran vokal (Ablaut) dari 'ei' menjadi 'ie' serta berakhiran '-en': ge-schrieb-en.",
            "execution": "Partizip II dari schreiben = 'geschrieben'."
        }
    },
    {
        "id": "ger-lat-m-23",
        "materi": "WORTSCHATZ & KULTUR: MÜLLTRENNUNG",
        "topic": "Kategori Pemilahan Sampah Rumah Tangga di Jerman (Gelbe Tonne/Gelber Sack)",
        "stem": "Dalam panduan pemilahan sampah ramah lingkungan di apartemen kota Köln:\n'Leere Plastikflaschen ohne Pfand, Milchtüten und Konservendosen gehören in die ( ... ).'\nWadah penampung sampah daur ulang yang TEPAT sesuai sistem pemilahan sampah Jerman adalah...",
        "correct": "Gelbe Tonne / den Gelben Sack (wadah khusus untuk limbah kemasan berbahan plastik, logam, dan komposit berlogo Grüne Punkt).",
        "distractors": [
            "Blaue Tonne (wadah penampung khusus untuk kertas, kardus, dan koran bekas).",
            "Braune Tonne / Biotonne (wadah khusus untuk sampah organik basah seperti sisa makanan dan tanaman).",
            "Schwarze Tonne / Restmülltonne (wadah khusus untuk residu sampah sisa yang tidak dapat didaur ulang).",
            "Altglascontainer (tempat pembuangan khusus pecahan botol kaca non-deposit)."
        ],
        "formula": {
            "title": "MÜLLTRENNUNG IN DEUTSCHLAND",
            "latex": "\\text{Gelbe Tonne/Sack} = \\text{Verpackungen (Plastik, Metall, Tetrapak)}",
            "legend": "• Blau = Papier/Karton.<br>• Braun/Grün = Biomüll.<br>• Schwarz/Grau = Restmüll.<br>• Gelb = Wertstoffe/Leichtverpackungen."
        },
        "hints": {
            "concept": "Di Jerman, sistem pemilahan sampah (Mülltrennung) sangat ketat: 'Gelbe Tonne' atau 'Gelber Sack' khusus untuk kemasan plastik, kaleng kaleng logam (Konservendosen), dan karton susu (Tetrapak).",
            "execution": "Plastik kemasan dan kaleng dimasukkan ke 'Gelbe Tonne / Gelber Sack'."
        }
    },
    {
        "id": "ger-lat-m-24",
        "materi": "GRAMMATIK: PRÄPOSITIONEN MIT DATIV (GEGENÜBER)",
        "topic": "Preposisi 'gegenüber' yang Menuntut Dativ dan Fleksibilitas Posisinya",
        "stem": "Seseorang memberikan petunjuk arah di pusat kota:\n'Die städtische Zentralbibliothek befindet sich direkt gegenüber ( ... ) großen Park.'\nBentuk artikel yang TEPAT setelah preposisi Dativ 'gegenüber' untuk kata benda maskulin 'der Park' adalah...",
        "correct": "dem (artikel kasus Dativ maskulin tunggal yang dituntut oleh preposisi gegenüber).",
        "distractors": [
            "den (artikel kasus Akkusativ maskulin yang salah diterapkan setelah preposisi Dativ).",
            "der (artikel Nominativ maskulin atau Dativ feminin).",
            "des (artikel Genitiv maskulin tunggal).",
            "das (artikel netral Nominativ/Akkusativ)."
        ],
        "formula": {
            "title": "DATIV-PRÄPOSITION: GEGENÜBER",
            "latex": "\\mathbf{gegenüber} + \\text{Dativ} \\quad (\\text{der Park } \\rightarrow \\text{dem Park})",
            "legend": "• Preposisi posisi 'gegenüber' (berseberangan/berhadapan langsung) mewajibkan kasus Dativ.<br>• der Park (maskulin) $\\rightarrow$ dem Park."
        },
        "hints": {
            "concept": "Preposisi 'gegenüber' (di seberang/berhadapan dengan) mewajibkan kata bendanya berada dalam kasus Dativ. Kata benda 'der Park' adalah maskulin, sehingga bentuk Dativ-nya adalah 'dem'.",
            "execution": "'gegenüber dem großen Park'."
        }
    },
    {
        "id": "ger-lat-m-25",
        "materi": "GRAMMATIK: MODALVERB 'SOLLEN' (AUFTRAG/RATSCHLAG)",
        "topic": "Penggunaan Modalverb 'sollen' untuk Menyampaikan Pesan atau Amanat Pihak Lain",
        "stem": "Sekretaris menyampaikan instruksi direktur kepada seorang staf:\n'Frau Schmidt, der Chef hat gesagt, Sie ( ... ) ihn sofort in seinem Büro anrufen.'\nBentuk konjugasi modalverb 'sollen' yang TEPAT untuk persona formal 'Sie' adalah...",
        "correct": "sollen (bentuk persona kedua formal Sie yang digunakan untuk menyampaikan mandat/perintah pihak ketiga).",
        "distractors": [
            "sollt (bentuk konjugasi untuk persona kedua jamak akrab ihr).",
            "sollten (bentuk Konjunktiv II yang bermakna anjuran/saran hipotetis, bukan mandat instruktif langsung).",
            "soll (bentuk persona pertama atau ketiga tunggal ich/er/sie/es).",
            "solle (bentuk Konjunktiv I orang ketiga tunggal yang tidak sesuai persona Sie)."
        ],
        "formula": {
            "title": "MODALVERB SOLLEN (FREMDER WILLE)",
            "latex": "\\text{Chef sagt: \"Rufen Sie mich an!\" } \\rightarrow \\text{Sie } \\mathbf{sollen} \\text{ ihn anrufen.}",
            "legend": "• 'sollen' digunakan untuk meneruskan instruksi, perintah, atau kehendak pihak ketiga.<br>• Konjugasi persona formal: Sie sollen."
        },
        "hints": {
            "concept": "Modalverb 'sollen' digunakan untuk meneruskan perintah, tugas, atau instruksi dari pihak ketiga (fremder Wille). Subjek kalimat adalah persona formal 'Sie', sehingga konjugasinya adalah 'sollen'.",
            "execution": "Subjek formal 'Sie' -> konjugasi 'sollen'."
        }
    }
]
