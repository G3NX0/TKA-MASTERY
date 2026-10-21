# -*- coding: utf-8 -*-
"""
BAHASA JERMAN - PAKET SOAL SIMULASI HOTS LENGKAP (35 BUTIR)
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / CEFR A2-B1 (Goethe-Zertifikat B1 / DSD I)
Distribusi:
- 25 Butir: Pilihan Ganda Tunggal (MCQ - ger-sim-01 s.d. ger-sim-25)
- 5 Butir: Pilihan Ganda Kompleks / Multi-Select (ger-sim-26 s.d. ger-sim-30)
- 5 Butir: Matriks Asosiasi Benar-Salah (ger-sim-31 s.d. ger-sim-35)
"""

BAHASA_JERMAN_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 MCQ ITEMS (ger-sim-01 .. ger-sim-25)
    # -------------------------------------------------------------
    {
        "id": "ger-sim-01",
        "materi": "LESEVERSTEHEN & MOBILITÄT: DEUTSCHLANDTICKET",
        "topic": "Analisis Wacana Kebijakan Tiket Transportasi Publik Nasional",
        "stem": "Bacalah teks informasi transportasi berikut:\n'Mit der Einführung des sogenannten Deutschlandtickets für bundesweit 49 Euro im Monat hat die Bundesregierung einen Meilenstein in der Verkehrspolitik gesetzt. Das Ticket gilt als digitales Abonnement im gesamten öffentlichen Personennahverkehr (ÖPNV) und Regionalverkehr aller teilnehmenden Verkehrsverbünde. Fahrten im Fernverkehr der Deutschen Bahn (ICE, IC, EC) sind jedoch strikt von der Gültigkeit ausgeschlossen.'\nBerdasarkan petunjuk regulasi resmi di atas, seorang penumpang yang memegang Deutschlandticket TIDAK DAPAT menggunakan tiket tersebut untuk menaiki...",
        "correct": "Kereta cepat jarak jauh Intercity-Express (ICE) dari Frankfurt menuju Berlin.",
        "distractors": [
            "Kereta regional (Regionalbahn / RE) yang menghubungkan kota Köln dan Bonn.",
            "Bus kota reguler dalam jaringan transportasi umum di pusat kota München.",
            "Kereta bawah tanah (U-Bahn) dan trem perkotaan di seluruh wilayah kota Hamburg.",
            "Kereta komuter perkotaan (S-Bahn) di kawasan metropolitan Stuttgart."
        ],
        "formula": {
            "title": "GELTUNGSBEREICH DES DEUTSCHLANDTICKETS",
            "latex": "\\text{Deutschlandticket} = \\text{ÖPNV + Regionalverkehr} \\quad \\neq \\quad \\text{Fernverkehr (ICE/IC/EC)}",
            "legend": "• Berlaku di seluruh jaringan transportasi umum lokal & regional se-Jerman.<br>• Larangan: Kereta jarak jauh (Fernverkehr) seperti ICE, IC, EC."
        },
        "hints": {
            "concept": "Teks secara eksplisit menegaskan batas keberlakuan: 'Fahrten im Fernverkehr der Deutschen Bahn (ICE, IC, EC) sind jedoch strikt von der Gültigkeit ausgeschlossen'. Artinya, kereta cepat jarak jauh seperti ICE tidak termasuk dalam tiket ini.",
            "execution": "Pengecualian keberlakuan tiket = Kereta cepat jarak jauh ICE."
        }
    },
    {
        "id": "ger-sim-02",
        "materi": "GRAMMATIK: PRONOMINALADVERBIEN (WORAUF / DARAUF)",
        "topic": "Penggabungan Preposisi Vokal dengan Kata Ganti Tunjuk 'da(r)-'",
        "stem": "Dua peneliti sedang mendiskusikan kelanjutan eksperimen biokimia:\n'Habt ihr schon über die unerwarteten Messergebnisse gesprochen? — Ja, natürlich haben wir ausführlich ( ... ) diskutiert.'\nKata keterangan pronominal (Pronominaladverb) yang TEPAT untuk merujuk pada benda/topik bahasan 'über die Messergebnisse' adalah...",
        "correct": "darüber (penggabungan da- + r + über untuk merujuk pada topik pembicaraan non-persona).",
        "distractors": [
            "worüber (bentuk interogatif yang hanya digunakan untuk mengajukan pertanyaan, bukan konfirmasi jawaban).",
            "darauf (penggabungan dengan preposisi auf yang tidak sesuai dengan valensi verba sprechen/diskutieren über).",
            "daran (penggabungan dengan preposisi an yang bermakna mengingat atau berpartisipasi).",
            "über es (kesalahan konstruksi sintaksis karena bahasa Jerman melarang preposisi langsung diikuti pronomina es untuk benda mati)."
        ],
        "formula": {
            "title": "PRONOMINALADVERBIEN: DA(R)- + PRÄPOSITION",
            "latex": "\\text{da-} + \\mathbf{r} + \\text{über (Vokal)} = \\mathbf{darüber}",
            "legend": "• Merujuk pada benda/hal non-manusia: gunakan da(r)- + Präposition.<br>• Bila preposisi diawali vokal (über, an, auf), disisipkan konsonan penghubung '-r-'."
        },
        "hints": {
            "concept": "Untuk merujuk pada fakta atau benda mati yang telah disebutkan dengan preposisi yang diawali vokal (über), digunakan Pronominaladverb 'darüber' (da + r + über). Bahasa Jerman melarang kombinasi 'über es'.",
            "execution": "diskutieren über + die Ergebnisse -> 'darüber'."
        }
    },
    {
        "id": "ger-sim-03",
        "materi": "GRAMMATIK: INFINITIV MIT 'UM...ZU' VS 'OHNE...ZU'",
        "topic": "Menyatakan Tindakan yang Terjadi Tanpa Melakukan Suatu Ekspektasi Wajar",
        "stem": "Seorang saksi mata melaporkan insiden kecelakaan di persimpangan jalan:\n'Der Autofahrer bog mit hoher Geschwindigkeit nach rechts ab, ( ... ) den Blinker zu setzen.'\nFrasa penghubung infinitif yang TEPAT untuk menyatakan tindakan yang dilakukan 'tanpa menyalakan lampu sein' adalah...",
        "correct": "ohne (frasa infinitif modalitas negatif 'ohne ... zu + Infinitiv' yang bermakna tanpa melakukan suatu tindakan wajar).",
        "distractors": [
            "um (frasa infinitif tujuan 'um ... zu + Infinitiv' yang bermakna 'supaya/untuk menyalakan sein').",
            "anstatt (frasa infinitif substitusi 'anstatt ... zu' yang bermakna alih-alih atau sebagai gantinya).",
            "damit (konjungsi subordinatif yang menuntut klausula lengkap dengan subjek dan verba terkonjugasi).",
            "außer (preposisi pengecualian yang tidak membentuk klausula infinitif eliptis baku)."
        ],
        "formula": {
            "title": "INFINITIVGRUPPEN: OHNE...ZU",
            "latex": "\\mathbf{ohne} + \\dots + \\mathbf{zu} + \\text{Infinitiv} = \\text{tanpa melakukan perbuatan}",
            "legend": "• Subjek kedua klausa harus identik (Der Autofahrer).<br>• Menandai tidak dilakukannya aksi keselamatan yang seharusnya."
        },
        "hints": {
            "concept": "Struktur 'ohne ... zu + Infinitiv' digunakan untuk menyatakan bahwa suatu aksi terjadi tanpa disertai tindakan yang semestinya dilakukan (dalam hal ini: tanpa menyalakan lampu sein). Subjek kedua aksi sama.",
            "execution": "Tanpa menyalakan sein = 'ohne ... zu setzen'."
        }
    },
    {
        "id": "ger-sim-04",
        "materi": "GRAMMATIK: GENITIV-ATTRIBUT",
        "topic": "Hubungan Kepemilikan Benda Menggunakan Kasus Genitiv Maskulin/Netral",
        "stem": "Dalam ulasan otomotif tentang mobil listrik terbaru:\n'Die hohe Reichweite und der leistungsstarke Motor ( ... ) neuen Elektroautos haben viele Fachjournalisten überzeugt.'\nBentuk artikel dan deklinasi kata sifat Genitiv netral tunggal yang TEPAT untuk 'das Elektroauto' adalah...",
        "correct": "des (artikel Genitiv netral tunggal 'des' yang diikuti kata sifat berakhiran -en dan akhiran -s pada benda).",
        "distractors": [
            "dem (artikel Dativ yang keliru karena hubungan kepemilikan atributif menuntut kasus Genitiv).",
            "den (artikel Akkusativ maskulin yang tidak dapat berfungsi sebagai penanda kepemilikan).",
            "der (artikel Genitiv feminin atau jamak yang keliru gender untuk kata netral das Auto).",
            "das (artikel Nominativ netral yang tidak mengalami deklinasi kepemilikan atribut)."
        ],
        "formula": {
            "title": "GENITIV-ATTRIBUT: DAS AUTO",
            "latex": "\\text{das Auto (Netral)} \\quad \\rightarrow \\quad \\mathbf{des} \\text{ neuen Elektroauto}\\mathbf{s}",
            "legend": "• Hubungan kepemilikan (Motor milik siapa?) dijawab dengan kasus Genitiv.<br>• Netral Genitiv: des + Adjektiv-en + Nomen-(e)s."
        },
        "hints": {
            "concept": "Frasa kepemilikan atributif (motor milik mobil listrik baru) dinyatakan dalam kasus Genitiv. Gender 'Elektroauto' adalah netral (das Auto). Bentuk Genitiv netral adalah 'des neuen Elektroautos'.",
            "execution": "Genitiv netral = 'des'."
        }
    },
    {
        "id": "ger-sim-05",
        "materi": "GRAMMATIK: KONJUNKTIONALADVERBIEN (DESHALB/TROTZDEM)",
        "topic": "Inversi Subjek dan Verba Setelah Kata Keterangan Penghubung 'deshalb'",
        "stem": "Seorang manajer proyek menjelaskan keputusan strategis perusahaannya:\n'Die Nachfrage nach unseren Produkten im Ausland ist drastisch gestiegen, deshalb ( ... ) wir im nächsten Monat eine neue Produktionslinie eröffnen.'\nSusunan kata yang TEPAT setelah kata keterangan penghubung kausalitas 'deshalb' adalah...",
        "correct": "werden (kata kerja bantu 'werden' menempati posisi kedua Hauptsatz tepat setelah deshalb, diikuti subjek wir).",
        "distractors": [
            "wir werden (urutan yang keliru karena mengabaikan hukum inversi posisi verba setelah adverbia penghubung).",
            "haben wir (penggunaan verba bantu lampau haben yang bertentangan dengan konteks masa depan im nächsten Monat).",
            "wir (penempatan subjek langsung yang melanggar posisi kata kerja kedua).",
            "zu werden (penambahan partikel infinitif zu yang tidak sah pada klausa konjugasi). "
        ],
        "formula": {
            "title": "INVERSION NACH KONJUNKTIONALADVERB (DESHALB)",
            "latex": "\\text{Pos. 1: deshalb} + \\mathbf{Pos. 2: finites Verb (werden)} + \\text{Pos. 3: Subjekt (wir)} + \\dots",
            "legend": "• Adverbia penghubung (deshalb, trotzdem, sonst, dann) menempati Posisi 1.<br>• Terjadi inversi: kata kerja berkonjugasi wajib mendahului subjek."
        },
        "hints": {
            "concept": "Kata keterangan penghubung seperti 'deshalb' (oleh karena itu) menempati posisi pertama (Position 1) di kalimat utama. Akibatnya terjadi pembalikan (Inversion): kata kerja yang dikonjugasikan (werden) wajib berada di posisi kedua, mendahului subjek (wir).",
            "execution": "deshalb + Posisi 2 (werden) + wir = 'deshalb werden wir'."
        }
    },
    {
        "id": "ger-sim-06",
        "materi": "PRAGMATIKA & INTERKULTURELLE KOMPETENZ: BERUFSALLTAG",
        "topic": "Etika Profesionalisme Jerman: Ketepatan Waktu (Pünktlichkeit) dan Kejelasan Fakta (Sachlichkeit)",
        "stem": "Dalam modul pelatihan adaptasi lintas budaya bagi tenaga kerja asing di Jerman:\n'Wenn Sie zu einem offiziellen Geschäftstermin in einem deutschen Unternehmen eingeladen sind, gilt es als oberstes Gebot der Professionalität, dass Sie...'\nSikap profesional yang PALING diharapkan dan dihargai dalam kultur kerja korporasi Jerman adalah...",
        "correct": "Hadir tepat waktu 5-10 menit sebelum jadwal, menyampaikan argumen secara lugas berbasis data faktual (sachlich), dan menghormati agenda.",
        "distractors": [
            "Sengaja datang terlambat satu jam sebagai simbol kedudukan jabatan dan kekuasaan personal.",
            "Menghindari pembahasan teknis pekerjaan dan menghabiskan sebagian besar waktu rapat untuk berbasa-basi urusan keluarga.",
            "Mengabaikan perjanjian tertulis dan mengubah seluruh kesepakatan kontrak secara sepihak tanpa pemberitahuan resmi.",
            "Menolak berbicara secara terbuka dan hanya memberikan persetujuan palsu demi menjaga kesenangan semu rekan bisnis."
        ],
        "formula": {
            "title": "DEUTSCHE ARBEITSKULTUR: SACHLICHKEIT & PÜNKTLICHKEIT",
            "latex": "\\text{Geschäftskultur} = \\text{Pünktlichkeit} + \\text{Sachlichkeit (Fakten)} + \\text{Verbindlichkeit}",
            "legend": "• Pünktlichkeit (ketepatan waktu) dipandang sebagai bentuk respek mendasar.<br>• Sachlichkeit: komunikasi langsung dan fokus pada data objektif."
        },
        "hints": {
            "concept": "Dalam budaya kerja Jerman, nilai fundamental yang dijunjung tinggi adalah ketepatan waktu mutlak (Pünktlichkeit), keterusterangan berbasis data objektif tanpa basa-basi berlebihan (Sachlichkeit), dan komitmen pada agenda.",
            "execution": "Pilihan yang mencerminkan ketepatan waktu dan argumen faktual objektif."
        }
    },
    {
        "id": "ger-sim-07",
        "materi": "GRAMMATIK: RELATIVSATZ MIT PRÄPOSITION",
        "topic": "Klausa Relatif yang Memuat Preposisi Spasial 'in' (+ Dativ)",
        "stem": "Pemandu wisata memperkenalkan bangunan bersejarah di kota Weimar:\n'Das ist das berühmte Goethe-Nationalmuseum, ( ... ) der Dichterfürst Johann Wolfgang von Goethe fast fünfzig Jahre lang gelebt und gearbeitet hat.'\nBentuk frasa relatif preposisional yang TEPAT untuk merujuk pada museum netral 'das Museum' dalam kasus Dativ adalah...",
        "correct": "in dem (preposisi lokasi statis 'in' + pronomina relatif netral Dativ 'dem').",
        "distractors": [
            "in das (kasus Akkusativ yang keliru karena verba leben dan arbeiten menjawab pertanyaan lokasi statis Wo?).",
            "in der (pronomina relatif feminin yang keliru gender untuk kata netral das Museum).",
            "worin das (konstruksi rancu yang menggabungkan adverbia relatif dengan artikel penunjuk benda).",
            "bei dem (preposisi bei yang kurang lazim digunakan untuk ruang lingkup fisik gedung tempat tinggal)."
        ],
        "formula": {
            "title": "RELATIVSATZ MIT PRÄPOSITION (WO? -> DATIV)",
            "latex": "\\text{das Museum (Netral)} + \\text{leben in (Dativ)} \\quad \\rightarrow \\quad \\mathbf{in dem}",
            "legend": "• Menjawab pertanyaan 'Wo?': Wechselpräposition 'in' mewajibkan Dativ.<br>• das Museum (netral) $\\rightarrow$ in dem."
        },
        "hints": {
            "concept": "Klausa relatif menerangkan lokasi statis tempat tinggal dan bekerja (Wo?). Preposisi 'in' mewajibkan kasus Dativ. Kata benda 'das Museum' adalah netral, sehingga pronomina relatifnya adalah 'dem' (in dem).",
            "execution": "in + Dativ netral = 'in dem'."
        }
    },
    {
        "id": "ger-sim-08",
        "materi": "GRAMMATIK: KONJUNKTIV II DER HÖFLICHKEIT (RESTAURANT)",
        "topic": "Menyampaikan Permintaan Santun Formal di Restoran Menggunakan 'könnten Sie'",
        "stem": "Pelanggan di restoran merasa hidangan yang disajikan belum cukup hangat:\n'Entschuldigung, Herr Ober! ( ... ) Sie diese Suppe bitte noch einmal kurz in der Küche aufwärmen lassen?'\nBentuk verba kesantunan formal Konjunktiv II yang TEPAT untuk menyampaikan permohonan tersebut adalah...",
        "correct": "Könnten (bentuk Konjunktiv II kesantunan formal dari verba können untuk persona formal Sie).",
        "distractors": [
            "Konnten (bentuk lampau Präteritum indikatif yang menanyakan kemampuan di masa lalu, bukan permohonan santun).",
            "Kann (bentuk Präsens indikatif yang bernada terlalu langsung dan kurang halus dalam etika pelayanan).",
            "Würden können (konstruksi pleonasme ganda yang tidak baku dalam gramatika bahasa Jerman).",
            "Möchten (modalverb yang membutuhkan objek nomina atau pelengkap berbeda, tidak berpasangan langsung dengan lassen)."
        ],
        "formula": {
            "title": "HÖFLICHE BITTE IM KONJUNKTIV II",
            "latex": "\\mathbf{Könnten Sie} \\dots ? \\quad \\leftrightarrow \\quad \\mathbf{Würden Sie} \\dots ?" ,
            "legend": "• Menyampaikan permohonan santun: gunakan 'Könnten Sie bitte...?'<br>• Menghindari kesan memerintah yang kasar (kann/muss)."
        },
        "hints": {
            "concept": "Untuk menyampaikan permintaan tolong secara sangat santun (höfliche Bitte) kepada pelayan restoran, bahasa Jerman baku menggunakan bentuk Konjunktiv II: 'Könnten Sie bitte ... ?'.",
            "execution": "Permohonan santun persona formal = 'Könnten Sie'."
        }
    },
    {
        "id": "ger-sim-09",
        "materi": "LESEVERSTEHEN & LANDESKUNDE: OKTOBERFEST",
        "topic": "Fakta Sejarah dan Kultural Tradisi Perayaan Terbesar di Bayern",
        "stem": "Bacalah ulasan budaya tradisi Jerman berikut:\n'Das Münchner Oktoberfest, im bayerischen Volksmund einfach \"Wiesn\" genannt, ist das größte Volksfest der Welt. Seine Ursprünge gehen auf das Jahr 1810 zurück, als anlässlich der königlichen Hochzeit von Kronprinz Ludwig von Bayern und Prinzessin Therese von Sachsen-Hildburghausen ein großes Pferderennen auf einer Festwiese vor den Toren der Stadt veranstaltet wurde. Zu Ehren der Braut erhielt das Festgelände den Namen \"Theresienwiese\".'\nBerdasarkan wacana sejarah di atas, alasan awal mula diselenggarakannya perayaan Oktoberfest pada tahun 1810 adalah...",
        "correct": "Peringatan pesta pernikahan kerajaan antara Putra Mahkota Ludwig dari Bayern dan Putri Therese.",
        "distractors": [
            "Perayaan panen raya gandum musim gugur secara serentak oleh para petani Bavaria.",
            "Peringatan kemenangan pasukan militer Jerman dalam pertempuran besar di Eropa Tengah.",
            "Deklarasi kemerdekaan negara bagian Bayern dari kekaisaran Romawi Suci bangsa Jerman.",
            "Pameran dagang internasional untuk mempromosikan teknologi industri pembuatan bir modern."
        ],
        "formula": {
            "title": "URSPRUNG DES OKTOBERFESTS (1810)",
            "latex": "\\text{Theresienwiese} \\leftarrow \\text{Königliche Hochzeit (Ludwig & Therese von Bayern, 1810)}",
            "legend": "• Asal usul: Pacuan kuda pesta pernikahan kerajaan tahun 1810.<br>• Lokasi dinamai 'Theresienwiese' untuk menghormati sang pengantin wanita."
        },
        "hints": {
            "concept": "Teks menyatakan secara gamblang: 'Seine Ursprünge gehen auf das Jahr 1810 zurück, als anlässlich der königlichen Hochzeit von Kronprinz Ludwig ... und Prinzessin Therese ... ein großes Pferderennen ... veranstaltet wurde'.",
            "execution": "Asal mula = Perayaan pernikahan kerajaan Putra Mahkota Ludwig dan Putri Therese."
        }
    },
    {
        "id": "ger-sim-10",
        "materi": "GRAMMATIK: ADJEKTIVDEKLINATION (TYP 3 - NULLARTIKEL)",
        "topic": "Deklinasi Kata Sifat Tanpa Artikel dalam Kasus Akkusativ Maskulin",
        "stem": "Di kedai minuman saat cuaca terik di musim panas:\n'Nach der anstrengenden Bergwanderung trank Michael mit großem Genuss ( ... ) Apfelsaft.'\nBentuk deklinasi kata sifat 'kalt' yang TEPAT tanpa artikel (Nullartikel) di depan kata benda maskulin Akkusativ 'Apfelsaft' adalah...",
        "correct": "kalten (akhiran kata sifat -en yang mengambil alih penanda kasus Akkusativ maskulin saat tidak ada artikel).",
        "distractors": [
            "kalter (akhiran -er yang merupakan penanda kasus Nominativ maskulin tanpa artikel).",
            "kaltes (akhiran -es yang merupakan penanda kasus Nominativ/Akkusativ netral tanpa artikel).",
            "kaltem (akhiran -em yang merupakan penanda kasus Dativ maskulin/netral tanpa artikel).",
            "kalte (akhiran yang keliru untuk kata benda maskulin tunggal pada kasus Akkusativ)."
        ],
        "formula": {
            "title": "STARKE ADJEKTIVDEKLINATION (OHNE ARTIKEL)",
            "latex": "\\text{Nullartikel} + \\text{Akkusativ Maskulin (der Apfelsaft)} \\quad \\implies \\quad \\text{Adjektiv-}\\mathbf{en}",
            "legend": "• Tanpa artikel: Kata sifat wajib mengemban akhiran sinyal penanda artikel definit.<br>• Akkusativ maskulin = den $\\rightarrow$ kalt-en."
        },
        "hints": {
            "concept": "Pada deklinasi kata sifat kuat (tanpa artikel / Nullartikel), kata sifat harus menunjukkan akhiran dari artikel tentu yang diwakilinya. Untuk kasus Akkusativ maskulin (seperti 'den Apfelsaft'), kata sifat mendapat akhiran '-en' (kalten Apfelsaft).",
            "execution": "Akkusativ maskulin tanpa artikel = 'kalten'."
        }
    },
    {
        "id": "ger-sim-11",
        "materi": "GRAMMATIK: TEMPORALKONJUNKTION 'ALS' VS 'WENN'",
        "topic": "Menyatakan Peristiwa Tunggal di Masa Lampau Menggunakan Konjungsi 'als'",
        "stem": "Kakek menceritakan pengalaman masa kecilnya yang sangat berkesan:\n'( ... ) ich zehn Jahre alt war, sah ich zum ersten Mal in meinem Leben das Meer.'\nKata penghubung subordinatif temporal yang TEPAT untuk peristiwa tunggal unik di masa lampau adalah...",
        "correct": "Als (konjungsi temporal khusus untuk peristiwa atau kurun waktu tunggal di masa lampau yang tidak berulang).",
        "distractors": [
            "Wenn (konjungsi yang hanya digunakan untuk kejadian masa kini, masa depan, atau kebiasaan berulang di masa lampau).",
            "Wann (kata tanya interogatif yang menanyakan waktu spesifik, bukan konjungsi penyambung klausula).",
            "Seitdem (konjungsi yang menandai titik mula peristiwa yang terus berlanjut hingga sekarang).",
            "Während (konjungsi yang menyatakan keserentakan proses berdurasi paralel)."
        ],
        "formula": {
            "title": "TEMPORALSÄTZE: ALS VS WENN (VERGANGENHEIT)",
            "latex": "\\mathbf{Als} = \\text{einmaliges Ereignis in der Vergangenheit}, \\quad \\mathbf{Wenn} = \\text{wiederholtes Ereignis (immer wenn)}",
            "legend": "• Usia 10 tahun adalah kurun masa lampau yang hanya terjadi sekali seumur hidup.<br>• Wajib menggunakan 'Als' (bukan 'Wenn' atau 'Wann')."
        },
        "hints": {
            "concept": "Dalam bahasa Jerman, untuk menyatakan peristiwa atau periode waktu di masa lampau yang hanya terjadi satu kali (einmaliges Ereignis in der Vergangenheit, seperti saat berusia sepuluh tahun), HANYA konjungsi 'als' yang boleh digunakan.",
            "execution": "Peristiwa tunggal masa lampau = 'Als ich zehn Jahre alt war'."
        }
    },
    {
        "id": "ger-sim-12",
        "materi": "GRAMMATIK: VERBEN MIT FESTEN PRÄPOSITIONEN (SICH ERINNERN)",
        "topic": "Verba Refleksif 'sich erinnern' yang Berpasangan Permanen dengan 'an' (+ Akkusativ)",
        "stem": "Dalam reuni akbar alumni sekolah menengah:\n'Wir saßen stundenlang zusammen und erinnerten uns gerne ( ... ) die vielen lustigen Erlebnisse aus unserer Schulzeit.'\nPreposisi dan kasus yang TEPAT untuk melengkapi verba refleksif 'sich erinnern' adalah...",
        "correct": "an (+ Akkusativ: sich erinnern an etwas/jemanden).",
        "distractors": [
            "über (+ Akkusativ: preposisi yang keliru digunakan untuk verba sich erinnern).",
            "auf (+ Akkusativ: preposisi yang menyatakan penantian masa depan, bukan kenangan masa lalu).",
            "von (+ Dativ: interferensi harfiah bahasa Inggris 'remind of' yang tidak sah dalam gramatika Jerman).",
            "mit (+ Dativ: preposisi instrumen kebersamaan yang tidak membentuk idiom mengingat)."
        ],
        "formula": {
            "title": "FESTE PRÄPOSITION: SICH ERINNERN AN (+ AKK)",
            "latex": "\\mathbf{sich erinnern an} + \\text{Akkusativ}",
            "legend": "• Idiom baku: mengingat kembali peristiwa/orang = sich erinnern an (+Akk).<br>• Objek jamak Akkusativ: an die vielen lustigen Erlebnisse."
        },
        "hints": {
            "concept": "Kata kerja refleksif 'sich erinnern' (mengingat / mengenang) secara mutlak menuntut preposisi 'an' dengan kasus Akkusativ (sich erinnern an + Akkusativ).",
            "execution": "sich erinnern + an (+ Akkusativ)."
        }
    },
    {
        "id": "ger-sim-13",
        "materi": "LESEVERSTEHEN & DESIGNGESCHICHTE: BAUHAUS",
        "topic": "Filosofi Desain Modernisme Bauhaus: Bentuk Mengikuti Fungsi (Form follows Function)",
        "stem": "Bacalah kutipan apresiasi sejarah seni rupa berikut:\n'Die 1919 von Walter Gropius in Weimar gegründete Kunstschule \"Bauhaus\" revolutionierte Architektur und Produktdesign weltweit. Ihr radikaler Ansatz brach mit den überladenen Ornamenten des Historismus und postulierte das Prinzip: \"Die Form folgt der Funktion\". Alltagsgegenstände und Gebäude sollten nicht nur ästhetisch ansprechend, sondern vor allem zweckmäßig, schlicht und für die breite Bevölkerung industriell erschwinglich sein.'\nPrinsip mendasar yang mendefinisikan filosofi desain gerakan Bauhaus berdasarkan teks di atas adalah...",
        "correct": "Bentuk rancangan harus sepenuhnya mengabdi pada fungsi praktis dan kegunaan (zweckmäßig), dengan estetika sederhana tanpa ornamen berlebihan.",
        "distractors": [
            "Dekorasi ukiran ornamen klasik bergaya abad pertengahan harus mendominasi setiap fasad bangunan modern.",
            "Setiap karya seni dan perabot rumah tangga harus dibuat secara manual tanpa bantuan mesin pabrik demi menjaga eksklusivitas kaum bangsawan.",
            "Harga produk harus dipatok setinggi mungkin agar hanya kalangan konglomerat yang dapat membelinya.",
            "Pemisahan total antara fungsi praktis bangunan dan nilai keindahan visual dalam arsitektur kota."
        ],
        "formula": {
            "title": "BAUHAUS-PHILOSOPHIE (1919)",
            "latex": "\\text{\"Form folgt Funktion\"} \\quad \\implies \\quad \\text{Zweckmäßigkeit, Schlichtheit, Bezahlbarkeit}",
            "legend": "• Menolak ornamen historis yang berlebihan.<br>• Fokus: Fungsionalitas tinggi, desain ramping/sederhana, dan produksi massal terjangkau."
        },
        "hints": {
            "concept": "Teks secara lugas memaparkan prinsip Bauhaus: 'Die Form folgt der Funktion' (bentuk mengikuti fungsi), di mana benda harus 'zweckmäßig' (fungsional/berguna), 'schlicht' (sederhana/ringkas), dan bebas dari 'überladenen Ornamenten'.",
            "execution": "Pilihan yang menjelaskan fungsi praktis (zweckmäßig) dan estetika sederhana tanpa ornamen."
        }
    },
    {
        "id": "ger-sim-14",
        "materi": "GRAMMATIK: ZUSTANDSPASSIV (SEIN + PARTIZIP II)",
        "topic": "Membedakan Status Akhir (Zustandspassiv) vs Proses Aksi (Vorgangspassiv)",
        "stem": "Seorang pelanggan tiba di kantor pos pada pukul 18.30 sore:\n'Es tut mir leid, die Postfiliale ( ... ) seit einer halben Stunde ( ... ). Bitte kommen Sie morgen früh wieder.'\nPasangan kata kerja bantu dan bentuk pasif keadaan (Zustandspassiv) yang TEPAT adalah...",
        "correct": "ist / geschlossen (Zustandspassiv dengan kata kerja bantu 'sein' untuk menggambarkan kondisi status tertutup).",
        "distractors": [
            "wird / geschlossen (Vorgangspassiv yang keliru karena bermakna pintu kantor pos sedang dalam proses bergerak ditutup saat itu juga).",
            "hat / geschlossen (bentuk aktif yang menuntut subjek persona yang menutup).",
            "wurde / schließend (penggunaan Partizip I yang merusak pola gramatikal pasif).",
            "ist / geschließt (kesalahan pembentukan Partizip II dari verba kuat schließen)."
        ],
        "formula": {
            "title": "ZUSTANDSPASSIV VS VORGANGSPASSIV",
            "latex": "\\text{Zustandspassiv (Status selesai): } \\mathbf{sein} + \\text{Partizip II} \\quad (\\text{ist geschlossen})",
            "legend": "• Vorgangspassiv (proses aksi sedang berlangsung): werden + Partizip II.<br>• Zustandspassiv (kondisi/status hasil): sein + Partizip II."
        },
        "hints": {
            "concept": "Zustandspassiv (pasif keadaan) menggunakan rumus 'sein + Partizip II' untuk menggambarkan kondisi atau status akhir yang sudah terwujud (kantor pos sudah dalam keadaan tutup sejak setengah jam lalu).",
            "execution": "Kondisi status tertutup = 'ist geschlossen'."
        }
    },
    {
        "id": "ger-sim-15",
        "materi": "GRAMMATIK: DOPPELKONJUNKTIONEN (NICHT NUR...SONDERN AUCH)",
        "topic": "Menghubungkan Dua Keunggulan Positif yang Saling Melengkapi",
        "stem": "Dalam ulasan kualifikasi seorang kandidat beasiswa doktoral:\n'Dieser Bewerber beherrscht ( ... ) fließend vier Fremdsprachen, ( ... ) besitzt auch bereits profunde Forschungserfahrung im Bereich der erneuerbaren Energien.'\nPasangan konjungsi ganda (Doppelkonjunktion) yang TEPAT untuk menggabungkan dua keunggulan tersebut adalah...",
        "correct": "nicht nur / sondern (pasangan konjungsi korelasi positif 'nicht nur ... sondern auch' yang bermakna 'bukan hanya ... tetapi juga').",
        "distractors": [
            "weder / noch (pasangan negasi ganda yang bermakna 'baik ... maupun ... tidak kedua-duanya').",
            "entweder / oder (pasangan disjungtif alternatif yang bermakna 'entah ... atau salah satu saja').",
            "sowohl / aber (pasangan kombinasi keliru yang merusak harmoni pasangan baku sowohl ... als auch).",
            "zwar / aber (pasangan konsesif pembatasan yang mengekspresikan kekurangan pada klausa kedua)."
        ],
        "formula": {
            "title": "DOPPELKONJUNKTIONEN: POSITIV-KUMULATIV",
            "latex": "\\mathbf{nicht nur} \\dots \\mathbf{sondern auch} \\quad \\iff \\quad \\mathbf{sowohl} \\dots \\mathbf{als auch}",
            "legend": "• Menegaskan akumulasi dua kelebihan positif.<br>• Bagian kedua memuat kata penguat 'auch'."
        },
        "hints": {
            "concept": "Pasangan konjungsi ganda 'nicht nur ... sondern auch' (tidak hanya ... melainkan juga) digunakan untuk menambahkan dua fakta positif yang saling melengkapi. Keberadaan kata 'auch' pada klausa kedua memastikan pasangan ini.",
            "execution": "Pasangan yang tepat = 'nicht nur ... sondern (auch)'."
        }
    },
    {
        "id": "ger-sim-16",
        "materi": "GRAMMATIK: KAUSALITÄT (WEGEN + GENITIV VS WEIL + NEBENSATZ)",
        "topic": "Transformasi Alasan Kausalitas Antara Frasa Preposisi Genitiv dan Klausa Subordinatif",
        "stem": "Perhatikan kalimat preposisional berikut:\n'Wegen des dichten Nebels konnte das Flugzeug in Frankfurt nicht landen.'\nJika kalimat tersebut diubah menjadi kalimat bertingkat dengan anak kalimat subordinatif 'weil', bentuk yang BENAR secara gramatika adalah...",
        "correct": "Weil der Nebel so dicht war, konnte das Flugzeug in Frankfurt nicht landen.",
        "distractors": [
            "Weil war der Nebel so dicht, das Flugzeug konnte in Frankfurt nicht landen.",
            "Weil der Nebel ist dicht gewesen, konnte nicht das Flugzeug in Frankfurt landen.",
            "Weil wegen des Nebels es so dicht war, konnte das Flugzeug nicht landen.",
            "Das Flugzeug konnte nicht in Frankfurt landen, weil der Nebel dicht war gewesen."
        ],
        "formula": {
            "title": "NOMINALSTIL ZU VERBALSTIL (WEGEN -> WEIL)",
            "latex": "\\mathbf{wegen} + \\text{Genitiv (Nebel)} \\quad \\iff \\quad \\mathbf{weil} + \\text{Subjekt} + \\dots + \\mathbf{Verb-Ende (war)}",
            "legend": "• Transformasi gaya nominal ke gaya verbal.<br>• Klausa 'weil' menempatkan verba 'war' di posisi akhir klausa anak."
        },
        "hints": {
            "concept": "Preposisi 'wegen' (+ Genitiv) dapat diubah menjadi klausa anak 'weil' (+ Nebensatz). Klausa 'weil' mewajibkan verba berkonjugasi berada di posisi paling akhir klausa anak: 'Weil der Nebel so dicht war, ...'.",
            "execution": "Susunan Nebensatz yang benar: 'Weil der Nebel so dicht war, konnte ...'."
        }
    },
    {
        "id": "ger-sim-17",
        "materi": "IDIOMATISCHE REDEWENDUNGEN: ALLTAGSSPRACHE",
        "topic": "Memahami Makna Ungkapan Idiomatis 'die Daumen drücken'",
        "stem": "Sebelum sahabatnya melangkah masuk ke ruang ujian lisan penentuan kelulusan:\n'Mach dir keine Sorgen, du hast dich monatelang hervorragend vorbereitet. Ich drücke dir ganz fest die Daumen!'\nMakna komunikatif yang dimaksud dari ungkapan idiomatis 'jemandem die Daumen drücken' adalah...",
        "correct": "Mendoakan dan berharap penuh agar orang tersebut memperoleh keberuntungan dan kesuksesan.",
        "distractors": [
            "Meminta bantuan medis darurat karena mengalami cedera fisik patah tulang pada ibu jari.",
            "Memberikan ancaman kekerasan fisik dan tekanan mental agar lawan bicara merasa takut.",
            "Menuntut ganti rugi materiil secara paksa atas kerugian finansial yang pernah ditimbulkan.",
            "Mengajak bersalaman secara formal untuk menandatangani perjanjian kontrak bisnis bersama."
        ],
        "formula": {
            "title": "REDEWENDUNG: DIE DAUMEN DRÜCKEN",
            "latex": "\\text{jemandem die Daumen drücken} = \\text{Viel Glück / Erfolg wünschen}",
            "legend": "• Metafora visual: mengepalkan ibu jari ke dalam jemari tangan sebagai simbol perlindungan magis kuno.<br>• Padanan: 'semoga berhasil / jari disilangkan (cross fingers)'."
        },
        "hints": {
            "concept": "Idiom terkenal Jerman 'jemandem die Daumen drücken' (menekan ibu jari untuk seseorang) adalah padanan dari 'semoga beruntung / sukses' (Viel Erfolg / Viel Glück), sama seperti gestur menyilangkan jari (fingers crossed) dalam bahasa Inggris.",
            "execution": "Makna idiom = Mendoakan keberuntungan dan kesuksesan."
        }
    },
    {
        "id": "ger-sim-18",
        "materi": "LESEVERSTEHEN & LANDESKUNDE: GESUNDHEITSSYSTEM",
        "topic": "Prinsip Solidaritas Sosial dalam Sistem Asuransi Kesehatan Wajib (GKV) Jerman",
        "stem": "Bacalah wacana sistem jaminan sosial berikut:\n'Das deutsche Gesundheitssystem basiert auf dem fundamentalen Solidaritätsprinzip der Gesetzlichen Krankenversicherung (GKV). Dies bedeutet, dass die monatlichen Versicherungsbeiträge prozentual nach dem Bruttoeinkommen der Versicherten berechnet werden und nicht nach deren individuellem Krankheitsrisiko oder Alter. Gesunde und Gutverdienende unterstützen somit Kranke und Einkommensschwache, während alle Mitglieder im Bedarfsfall denselben umfassenden Anspruch auf medizinische Versorgung haben.'\nBerdasarkan teks di atas, manifestasi nyata dari 'prinsip solidaritas' dalam asuransi kesehatan Jerman adalah...",
        "correct": "Besaran iuran premi dipungut sesuai persentase penghasilan kotor, bukan berdasarkan riwayat risiko penyakit atau usia peserta.",
        "distractors": [
            "Peserta yang memiliki pendapatan tinggi mendapatkan hak istimewa untuk menolak membayar premi bulanan.",
            "Warga yang sering sakit diwajibkan membayar iuran sepuluh kali lipat lebih mahal dibanding warga yang bugar.",
            "Pemerintah hanya memberikan pengobatan gratis kepada para lansia yang tidak memiliki keluarga sama sekali.",
            "Rumah sakit hanya diizinkan merawat pasien yang mampu membayar biaya tindakan medis secara tunai di muka."
        ],
        "formula": {
            "title": "SOLIDARITÄTSPRINZIP DER GKV",
            "latex": "\\text{Beitrag} \\propto \\text{Einkommen (Geld)}, \\quad \\text{Leistung} = \\text{Bedarf (Medizin)}",
            "legend": "• Iuran dihitung dari persentase gaji kotor (prozentual nach Bruttoeinkommen).<br>• Pelayanan medis diberikan setara bagi semua anggota tanpa diskriminasi biaya."
        },
        "hints": {
            "concept": "Teks secara lugas memaparkan: 'monatlichen Versicherungsbeiträge prozentual nach dem Bruttoeinkommen ... berechnet werden und nicht nach deren individuellem Krankheitsrisiko oder Alter'.",
            "execution": "Iuran dihitung berdasar persentase penghasilan kotor, bukan risiko sakit atau usia."
        }
    },
    {
        "id": "ger-sim-19",
        "materi": "GRAMMATIK: MODALVERBEN IM PERFEKT (ERSATZINFINITIV)",
        "topic": "Fenomena Penggantian Partizip II dengan Infinitif (Ersatzinfinitiv) Saat Ada Verba Penuh",
        "stem": "Seorang teknisi komputer menjelaskan kendala yang dialaminya kemarin:\n'Wegen eines unerwarteten Serverausfalls habe ich die defekte Datenbank nicht rechtzeitig ( ... ).'\nBentuk verba akhir yang TEPAT untuk melengkapi konstruksi Perfekt dari modalverb 'können' bersama verba penuh 'reparieren' adalah...",
        "correct": "reparieren können (penggunaan Ersatzinfinitiv: modalverb mempertahankan bentuk infinitif saat didampingi verba penuh).",
        "distractors": [
            "reparieren gekonnt (kesalahan memakai bentuk Partizip II biasa 'gekonnt' saat mendampingi verba penuh).",
            "repariert gekonnt (kesalahan penggunaan dua bentuk Partizip II secara beruntun).",
            "repariert können (kesalahan mendampingkan Partizip II aktif dengan modalverb infinitif).",
            "reparieren konnte (kesalahan mencampur kata kerja bantu lampau Perfekt 'habe' dengan Präteritum 'konnte')."
        ],
        "formula": {
            "title": "ERSATZINFINITIV BEI MODALVERBEN",
            "latex": "\\text{haben} + \\dots + \\text{Vollverb (Infinitiv)} + \\mathbf{Modalverb (Infinitiv)}",
            "legend": "• Aturan baku: Bila modalverb berada di akhir kalimat Perfekt bersama verba penuh, bentuknya BUKAN 'gekonnt', melainkan infinitif 'können'.<br>• Dikenal sebagai fenomena 'Ersatzinfinitiv'."
        },
        "hints": {
            "concept": "Dalam bahasa Jerman, bila kata kerja modal (seperti können) digunakan pada kala Perfekt bersama dengan kata kerja utama (Vollverb), kata kerja modal TIDAK diubah menjadi Partizip II (gekonnt), melainkan menjadi 'Ersatzinfinitiv' (tetap infinitif: reparieren können).",
            "execution": "Kombinasi Perfekt modalverb = 'reparieren können'."
        }
    },
    {
        "id": "ger-sim-20",
        "materi": "GRAMMATIK: RELATIVPRONOMEN IM GENITIV (DESSEN / DEREN)",
        "topic": "Pronomina Relatif Kepemilikan Genitiv Maskulin Tunggal 'dessen'",
        "stem": "Rektor universitas memuji pencapaian mahasiswa teladan:\n'Wir gratulieren dem begabten Studenten, ( ... ) innovative Masterarbeit mit dem prestigeträchtigen Förderpreis für Quantenphysik ausgezeichnet wurde.'\nBentuk pronomina relatif Genitiv yang TEPAT untuk merujuk pada kata benda maskulin tunggal 'der Student' adalah...",
        "correct": "dessen (pronomina relatif Genitiv maskulin/netral tunggal yang menyatakan hubungan kepemilikan 'yang ...-nya').",
        "distractors": [
            "deren (pronomina relatif Genitiv feminin tunggal atau jamak).",
            "dem (pronomina relatif kasus Dativ yang tidak dapat menyatakan kepemilikan atas Masterarbeit).",
            "des (artikel biasa yang dilarang berdiri sendiri sebagai pronomina relatif kepemilikan).",
            "seinem (kata ganti kepemilikan biasa yang tidak memiliki kapabilitas menyambung klausa relatif)."
        ],
        "formula": {
            "title": "RELATIVPRONOMEN IM GENITIV",
            "latex": "\\text{der Student (Maskulin)} \\quad \\rightarrow \\quad \\text{Genitiv: } \\mathbf{dessen} \\text{ Masterarbeit}",
            "legend": "• Maskulin/Netral tunggal: dessen.<br>• Feminin tunggal & Jamak: deren.<br>• Mengindikasikan kepemilikan: mahasiswa yang tesisnya..."
        },
        "hints": {
            "concept": "Pronomina relatif dalam kasus Genitiv digunakan untuk menyatakan kepemilikan (yang ...-nya). Untuk anteseden maskulin tunggal (der Student), bentuk Genitiv-nya adalah 'dessen'.",
            "execution": "der Student -> Genitiv Relativpronomen = 'dessen'."
        }
    },
    {
        "id": "ger-sim-21",
        "materi": "LESEVERSTEHEN & GESCHICHTE: TAG DER DEUTSCHEN EINHEIT",
        "topic": "Signifikansi Historis Tanggal 3 Oktober sebagai Hari Libur Nasional Penyatuan Kembali Jerman",
        "stem": "Bacalah wacana kenegaraan Jerman berikut:\n'Der 3. Oktober ist der offizielle Nationalfeiertag der Bundesrepublik Deutschland und trägt den Namen \"Tag der Deutschen Einheit\". An diesem Tag im Jahr 1990 trat der Einigungsvertrag in Kraft, wodurch die Deutsche Demokratische Republik (DDR) der Bundesrepublik beitrat und die über vier Jahrzehnte andauernde schmerzhafte Teilung des Landes nach dem Zweiten Weltkrieg friedlich überwunden wurde. Anders als in vielen anderen Ländern gedenkt Deutschland damit keinem militärischen Sieg, sondern dem friedlichen Triumph von Freiheit und Wiedervereinigung.'\nBerdasarkan wacana di atas, peristiwa monumental yang diperingati pada 'Tag der Deutschen Einheit' setiap 3 Oktober adalah...",
        "correct": "Penyatuan kembali secara resmi dan damai antara Jerman Barat dan Jerman Timur pada tahun 1990 pasca berakhirnya Perang Dingin.",
        "distractors": [
            "Kemenangan pasukan militer sekutu atas runtuhnya rezim totaliter pada tahun 1945.",
            "Penandatanganan piagam pendirian persekutuan pertahanan militer NATO di benua Eropa.",
            "Proklamasi pembentukan Republik Weimar sebagai sistem demokrasi parlementer pertama Jerman.",
            "Pembangunan Tembok Berlin oleh pemerintah komunis Jerman Timur pada Agustus 1961."
        ],
        "formula": {
            "title": "TAG DER DEUTSCHEN EINHEIT (3. OKTOBER 1990)",
            "latex": "\\text{3. Oktober 1990} = \\text{Inkrafttreten des Einigungsvertrags} \\quad (\\text{Wiedervereinigung BRD & DDR})",
            "legend": "• Peringatan persatuan kembali bangsa Jerman pasca Perang Dingin.<br>• Satu-satunya hari libur nasional yang ditetapkan oleh hukum federal (Bundesrecht)."
        },
        "hints": {
            "concept": "Teks secara eksplisit menerangkan: tanggal 3 Oktober 1990 adalah berlakunya perjanjian persatuan di mana DDR bergabung dengan Republik Federal Jerman, mengakhiri pemisahan negara (Wiedervereinigung).",
            "execution": "Peristiwa = Penyatuan kembali secara damai Jerman Barat dan Jerman Timur tahun 1990."
        }
    },
    {
        "id": "ger-sim-22",
        "materi": "GRAMMATIK: KATA KERJA DENGAN PREPOSISI (DENKEN AN)",
        "topic": "Verba 'denken' yang Berpasangan Permanen dengan Preposisi 'an' (+ Akkusativ)",
        "stem": "Seorang ibu memberikan wejangan kepada putranya yang baru merantau ke luar kota:\n'( ... ) du immer an deine Gesundheit, wenn du in den stressigen Prüfungsphasen bist!'\nBentuk kata kerja perintah (Imperativ) dari verba 'denken' untuk persona 'du' yang TEPAT adalah...",
        "correct": "Denk (bentuk Imperativ du yang lugas tanpa akhiran -e atau akhiran personal -st).",
        "distractors": [
            "Denkst (bentuk indikatif pernyataan yang keliru diterapkan pada kalimat instruksi imperatif).",
            "Denken (bentuk infinitif atau imperatif jamak formal tanpa kata ganti penunjuk Sie).",
            "Gedenke (verba gedenken dengan makna mengenang arwah yang menuntut kasus Genitiv arkais).",
            "Dachte (bentuk lampau Präteritum yang tidak logis untuk kalimat perintah masa sekarang)."
        ],
        "formula": {
            "title": "IMPERATIV & FESTE PRÄPOSITION: DENKEN AN (+ AKK)",
            "latex": "\\text{denken an (+Akk)} \\quad \\rightarrow \\quad \\text{Imperativ (du): } \\mathbf{Denk(e) an} \\dots !",
            "legend": "• Verba berpasangan tetap: denken an + Akkusativ.<br>• Imperativ persona 'du' dibentuk dari akar verba: Denk!"
        },
        "hints": {
            "concept": "Kata kerja 'denken an' (+ Akkusativ) bermakna memikirkan/memperhatikan. Bentuk kalimat perintah (Imperativ) untuk persona tunggal 'du' dibentuk dari akar kata kerja tanpa akhiran persona: 'Denk!'.",
            "execution": "Imperativ du dari denken = 'Denk'."
        }
    },
    {
        "id": "ger-sim-23",
        "materi": "LESEVERSTEHEN: ALEXANDER VON HUMBOLDT",
        "topic": "Pendekatan Holistik Ekologi Alam Semesta oleh Ilmuwan Alexander von Humboldt",
        "stem": "Bacalah teks profil saintifik berikut:\n'Der deutsche Naturforscher Alexander von Humboldt gilt als einer der Wegbereiter des modernen ökologischen Denkens. Auf seiner legendären fünfjährigen Expedition durch Lateinamerika begriff er die Natur nicht als Ansammlung voneinander isolierter biologischer Objekte, sondern als ein zusammenhängendes, dynamisches globales Netz von Wechselwirkungen (\"Kosmos\"), in dem das Klima, die Geografie und alle lebenden Organismen unlösbar miteinander verknüpft sind.'\nBerdasarkan teks di atas, kontribusi pemikiran paling revolusioner dari Alexander von Humboldt bagi ilmu pengetahuan modern adalah...",
        "correct": "Konsep holistik tentang alam semesta sebagai jejaring global yang saling terhubung dan bergantung satu sama lain (interkoneksi ekologis).",
        "distractors": [
            "Teori bahwa seluruh makhluk hidup di dunia dapat dipisahkan secara kaku tanpa keterkaitan timbal balik sama sekali.",
            "Penemuan formula kimia sintetis pertama untuk memproduksi pupuk buatan dalam skala industri raksasa.",
            "Gagasan bahwa manusia berhak merusak seluruh ekosistem alam demi memprioritaskan ekspansi pemukiman kota.",
            "Penolakan terhadap penelitian lapangan langsung dan anjuran agar ilmuwan hanya berteori di dalam ruangan perpustakaan."
        ],
        "formula": {
            "title": "HUMBOLDTS KOSMOS-KONZEPT",
            "latex": "\\text{Natur} = \\text{dynamisches globales Netz von Wechselwirkungen}",
            "legend": "• Pelopor pandangan ekologi modern: segala komponen biosfer saling terikat.<br>• Pemikiran holistik jaringan kehidupan."
        },
        "hints": {
            "concept": "Teks menyatakan bahwa Humboldt memandang alam sebagai 'ein zusammenhängendes, dynamisches globales Netz von Wechselwirkungen ... in dem das Klima, die Geografie und alle lebenden Organismen unlösbar miteinander verknüpft sind'.",
            "execution": "Kontribusi = Konsep holistik alam sebagai jejaring global yang saling terhubung secara ekologis."
        }
    },
    {
        "id": "ger-sim-24",
        "materi": "GRAMMATIK: KATA SAMBUNG KONDISIONAL KONTRAFAKTUAL 'WÄRE...GEWESEN'",
        "topic": "Klausa Pengandaian Tanpa Konjungsi (Verb-Erst-Konditionalsatz im Konjunktiv II)",
        "stem": "Dalam evaluasi pasca misi penyelamatan darurat di pegunungan Alpen:\n'( ... ) das Rettungsteam nur zehn Minuten später eingetroffen, hätten die verunglückten Bergsteiger die eisige Nacht kaum überlebt.'\nBentuk kata kerja bantu yang TEPAT untuk mengawali kalimat pengandaian inversi tanpa kata 'wenn' tersebut adalah...",
        "correct": "Wäre (verba sein pada Konjunktiv II masa lampau yang menempati posisi pertama untuk menggantikan kata sambung 'wenn').",
        "distractors": [
            "Hätte (verba haben yang salah bantu karena kata kerja pergerakan eintreffen membentuk waktu lampau dengan sein).",
            "War (bentuk indikatif fakta nyata yang keliru secara modalitas pengandaian kontrafaktual).",
            "Sei (bentuk Konjunktiv I kutipan tidak langsung yang tidak sesuai fungsi pengandaian).",
            "Würde (bentuk Konjunktiv II sekarang yang tidak cocok dipasangkan dengan Partizip II verba pergerakan eintreffen)."
        ],
        "formula": {
            "title": "VERB-ERST-KONDITIONALSATZ (UNEINGELEITETER KONDITIONALSATZ)",
            "latex": "\\mathbf{Wäre} \\text{ das Team eingetroffen } \\iff \\text{Wenn das Team eingetroffen } \\mathbf{wäre}",
            "legend": "• Tanpa kata 'wenn': Kalimat pengandaian diawali langsung oleh verba Konjunktiv II di Posisi 1.<br>• eintreffen (Ortswechsel) membentuk lampau dengan 'sein' $\\rightarrow$ Wäre ... eingetroffen."
        },
        "hints": {
            "concept": "Kalimat pengandaian (Konditionalsatz) dapat dibentuk tanpa konjungsi 'wenn' dengan cara memindahkan kata kerja Konjunktiv II ke posisi paling depan (Posisi 1). Verba 'eintreffen' (tiba) adalah verba perpindahan tempat yang membentuk Perfekt dengan 'sein' -> 'Wäre das Rettungsteam ... eingetroffen'.",
            "execution": "Verba bantu sein di posisi pertama = 'Wäre'."
        }
    },
    {
        "id": "ger-sim-25",
        "materi": "PRAGMATIKA & FORMALIA: BEWERBUNGSSCHREIBEN",
        "topic": "Register Bahasa Formal dalam Penulisan Surat Lamaran Pekerjaan di Jerman",
        "stem": "Dalam surat lamaran kerja resmi (*Bewerbungsschreiben*) yang ditujukan kepada penanggung jawab perekrutan yang tidak dikenal namanya secara spesifik:\nSalam pembuka resmi yang PALING TEPAT dan memenuhi etika korespondensi bisnis Jerman adalah...",
        "correct": "Sehr geehrte Damen und Herren, (salam pembuka formal standar untuk penerima surat institusional yang belum diketahui nama individunya).",
        "distractors": [
            "Liebe Leute im Büro, (salam informal yang terkesan sangat santai dan tidak sopan untuk lamaran pekerjaan).",
            "Hallo Herr Chef, (sapaan kolokial lisan yang melanggar norma etika formalitas bisnis korporat).",
            "Guten Morgen zusammen, (salam lisan harian internal yang tidak lazim digunakan dalam dokumen lamaran resmi).",
            "Hiermit bewerbe ich mich sofort, (kalimat pembuka isi surat yang tidak memuat salam penghormatan kepada pembaca)."
        ],
        "formula": {
            "title": "ANREDE IN FORMELLEN BRIEFEN",
            "latex": "\\text{Formeller Brief (Nama tidak spesifik)} \\quad \\implies \\quad \\mathbf{Sehr geehrte Damen und Herren,}",
            "legend": "• Standar resmi korespondensi bisnis DIN 5008 di Jerman.<br>• Diikuti tanda koma, dan kalimat berikutnya diawali dengan huruf kecil."
        },
        "hints": {
            "concept": "Dalam etika surat menyurat formal bahasa Jerman (DIN 5008), jika nama pihak yang dituju tidak diketahui secara spesifik, salam pembuka standar yang wajib digunakan adalah 'Sehr geehrte Damen und Herren,'.",
            "execution": "Salam resmi lamaran pekerjaan tanpa nama spesifik = 'Sehr geehrte Damen und Herren,'."
        }
    },

    # -------------------------------------------------------------
    # 5 PILIHAN GANDA KOMPLEKS / MULTI-SELECT (ger-sim-26 .. ger-sim-30)
    # -------------------------------------------------------------
    {
        "id": "ger-sim-26",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: MÜLLTRENNUNG & KREISLAUFWIRTSCHAFT",
        "topic": "Prinsip dan Kategori Pemilahan Sampah Berkelanjutan di Jerman",
        "questionHtml": "Jerman dikenal memiliki sistem pengelolaan sampah dan daur ulang terpadu (*Kreislaufwirtschaft*) yang sangat disiplin. Dari pernyataan-pernyataan di bawah ini, manakah <strong>DUA (2)</strong> tindakan pemilahan sampah yang BENAR sesuai regulasi lingkungan hidup Jerman?",
        "options": [
            {
                "key": "A",
                "text": "Kardus bekas kemasan paket belanja online dan surat kabar bekas dibuang ke dalam 'Blaue Tonne' (tempat sampah kertas)."
            },
            {
                "key": "B",
                "text": "Botol kaca minuman dan cermin rias yang pecah harus dihancurkan lalu dimasukkan ke dalam 'Biotonne' bersama sisa sayuran."
            },
            {
                "key": "C",
                "text": "Botol plastik minuman berbahan PET yang memiliki logo deposit resmi (*Pfandzeichen*) dikembalikan ke mesin otomatis di supermarket untuk mendapatkan uang jaminan kembali."
            },
            {
                "key": "D",
                "text": "Seluruh baterai bekas alat elektronik boleh dibuang bebas ke wadah residu umum 'Restmüll' tanpa perlakuan khusus."
            }
        ],
        "correctKeys": ["A", "C"],
        "formulaHud": {
            "title": "MÜLLTRENNUNG & PFANDSYSTEM",
            "latex": "\\text{Blaue Tonne = Papier/Karton}, \\quad \\text{Pfandautomat = Rückgabe von Pfandflaschen}",
            "legend": "• Baterai bekas adalah limbah B3 (Sondermüll) yang harus dibawa ke kotak khusus di toko.<br>• Biotonne hanya untuk limbah organik basah."
        },
        "hints": {
            "concept": "Di Jerman: (A) Kertas dan karton masuk ke Blaue Tonne (Benar). (B) Pecahan cermin/kaca jendela bukan sampah organik, dan botol kaca masuk ke Altglascontainer sesuai warna (Salah). (C) Botol berlogo Pfand dikembalikan ke Pfandautomat di supermarket untuk ditukar uang (Benar). (D) Baterai mengandung racun dan dilarang dibuang ke Restmüll (Salah).",
            "execution": "Pernyataan yang tepat adalah A dan C."
        }
    },
    {
        "id": "ger-sim-27",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: VERBEN MIT DATIV",
        "topic": "Identifikasi Kata Kerja yang Mewajibkan Objek Kasus Dativ",
        "stem": "Dalam tata bahasa Jerman, terdapat kelompok kata kerja transitif/intransitif khusus yang secara permanen mewajibkan objeknya berada dalam kasus Dativ (bukan Akkusativ). Dari verba-verba berikut, manakah <strong>DUA (2)</strong> kata kerja yang SELALU menuntut objek Dativ?",
        "options": [
            {
                "key": "A",
                "text": "gratulieren (memberikan ucapan selamat kepada seseorang: jemandem gratulieren)."
            },
            {
                "key": "B",
                "text": "kaufen (membeli suatu benda sebagai objek penderita langsung)."
            },
            {
                "key": "C",
                "text": "gehören (menjadi milik atau kepunyaan sah seseorang: jemandem gehören)."
            },
            {
                "key": "D",
                "text": "sehen (melihat seseorang atau objek secara visual dalam kasus Akkusativ)."
            }
        ],
        "correctKeys": ["A", "C"],
        "formulaHud": {
            "title": "DATIV-VERBEN IM DEUTSCHEN",
            "latex": "\\text{Dativ-Verben: } \\mathbf{gratulieren, gehören, helfen, danken, antworten, gefallen}",
            "legend": "• Verba ini langsung diikuti objek Dativ tanpa preposisi.<br>• kaufen dan sehen adalah verba transitif Akkusativ (etwas/jemanden kaufen/sehen)."
        },
        "hints": {
            "concept": "Verba Dativ murni meliputi: gratulieren (+ Dativ, misal: Ich gratuliere dir) dan gehören (+ Dativ, misal: Das Auto gehört mir). Verba 'kaufen' dan 'sehen' menuntut objek Akkusativ (etwas kaufen, jemanden sehen).",
            "execution": "Verba yang menuntut Dativ adalah A dan C."
        }
    },
    {
        "id": "ger-sim-28",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: ADUSO-KONJUNKTIONEN",
        "topic": "Identifikasi Konjungsi Koordinatif yang Menempati Posisi Nol (Position 0)",
        "stem": "Konjungsi koordinatif golongan 'ADUSO' menghubungkan dua kalimat utama (Hauptsatz) tanpa mengubah susunan kata kerja, karena menempati posisi nol (Position 0). Dari kata sambung berikut, manakah <strong>DUA (2)</strong> kata yang tergolong dalam kelompok konjungsi 'ADUSO'?",
        "options": [
            {
                "key": "A",
                "text": "denn (karena - konjungsi koordinatif alasan kausalitas di posisi nol)."
            },
            {
                "key": "B",
                "text": "weil (karena - konjungsi subordinatif yang memindahkan verba ke akhir kalimat)."
            },
            {
                "key": "C",
                "text": "sondern (melainkan - konjungsi koordinatif korektif di posisi nol)."
            },
            {
                "key": "D",
                "text": "obwohl (meskipun - konjungsi subordinatif yang memindahkan verba ke akhir kalimat)."
            }
        ],
        "correctKeys": ["A", "C"],
        "formulaHud": {
            "title": "ADUSO-FORMEL (POSITION 0)",
            "latex": "\\mathbf{A} - \\text{aber}, \\quad \\mathbf{D} - \\text{denn}, \\quad \\mathbf{U} - \\text{und}, \\quad \\mathbf{S} - \\text{sondern}, \\quad \\mathbf{O} - \\text{oder}",
            "legend": "• Semua konjungsi ADUSO berada di Posisi 0: Subjek tetap di Posisi 1 dan Verba di Posisi 2.<br>• 'weil' dan 'obwohl' adalah konjungsi subordinatif (Verb di akhir)."
        },
        "hints": {
            "concept": "Akronim ADUSO terdiri dari: Aber, Denn, Und, Sondern, Oder. Kata sambung ini menempati Posisi Nol. 'weil' dan 'obwohl' adalah konjungsi subordinatif (membuat verba pindah ke akhir kalimat).",
            "execution": "Anggota ADUSO adalah A (denn) dan C (sondern)."
        }
    },
    {
        "id": "ger-sim-29",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: DUALE AUSBILDUNG",
        "topic": "Karakteristik dan Hak Peserta Sistem Pendidikan Vokasi Ganda di Jerman",
        "stem": "Sistem 'Duale Ausbildung' di Jerman memiliki karakteristik struktural yang sangat spesifik dalam membina calon tenaga ahli. Manakah <strong>DUA (2)</strong> fakta di bawah ini yang BENAR mengenai sistem Duale Ausbildung?",
        "options": [
            {
                "key": "A",
                "text": "Peserta magang (*Auszubildende / Azubi*) menandatangani kontrak kerja resmi dengan perusahaan dan menerima uang saku bulanan (*Ausbildungsvergütung*)."
            },
            {
                "key": "B",
                "text": "Seluruh proses belajar mengajar dilaksanakan 100% secara daring di rumah tanpa pernah menginjakkan kaki di tempat kerja fisik."
            },
            {
                "key": "C",
                "text": "Kelulusan dan standar kualifikasi kompetensi akhir diuji secara independen oleh kamar dagang dan industri (*IHK / HWK*)."
            },
            {
                "key": "D",
                "text": "Program ini hanya diperuntukkan bagi warga negara bergelar profesor dan menolak lulusan sekolah menengah."
            }
        ],
        "correctKeys": ["A", "C"],
        "formulaHud": {
            "title": "DUALE BERUFSAUSBILDUNG MERKMALE",
            "latex": "\\text{Azubi} \\rightarrow \\text{Ausbildungsvertrag + Vergütung}, \\quad \\text{Prüfung durch IHK / HWK}",
            "legend": "• IHK (Industrie- und Handelskammer) / HWK (Handwerkskammer) mengawasi standar ujian mutu nasional.<br>• Azubi memperoleh gaji pelatihan bulanan dari perusahaan pembina."
        },
        "hints": {
            "concept": "Dalam Duale Ausbildung: (A) Peserta menandatangani kontrak kerja resmi dan menerima gaji bulanan (Ausbildungsvergütung) (Benar). (B) Pelatihan berlangsung nyata di tempat kerja dan sekolah, bukan murni daring (Salah). (C) Ujian akhir distandarisasi oleh IHK/HWK (Benar). (D) Terbuka luas untuk lulusan sekolah menengah (Salah).",
            "execution": "Fakta yang benar adalah A dan C."
        }
    },
    {
        "id": "ger-sim-30",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: D-A-CH LANDESKUNDE (SCHWEIZ)",
        "topic": "Karakteristik Kebahasaan dan Politik Khusus Konfederasi Swiss",
        "stem": "Swiss (*die Schweiz*) merupakan salah satu pilar penting dalam kawasan berbahasa Jerman (*D-A-CH*). Dari pernyataan di bawah ini, manakah <strong>DUA (2)</strong> karakteristik geografis dan kebahasaan yang BENAR tentang Swiss?",
        "options": [
            {
                "key": "A",
                "text": "Bahasa Jerman merupakan salah satu dari empat bahasa resmi nasional di Swiss, berdampingan dengan bahasa Prancis, Italia, dan Romansh."
            },
            {
                "key": "B",
                "text": "Swiss menggunakan mata uang bersama Euro (€) sebagai alat pembayaran tunggal resmi di seluruh wilayah kantonnya."
            },
            {
                "key": "C",
                "text": "Dalam ejaan bahasa Jerman standar Swiss (*Schweizer Hochdeutsch*), huruf ligatur 'ß' (*Eszett*) tidak digunakan sama sekali dan selalu digantikan dengan 'ss'."
            },
            {
                "key": "D",
                "text": "Ibu kota administratif Swiss yang menjadi pusat pemerintahan federal adalah kota Jenewa (*Genf*)."
            }
        ],
        "correctKeys": ["A", "C"],
        "formulaHud": {
            "title": "BESONDERHEITEN DER SCHWEIZ (CH)",
            "latex": "4 \\text{ Landessprachen: Deutsch, Französisch, Italienisch, Rätoromanisch} \\quad | \\quad \\text{Kein 'ß' } \\rightarrow \\text{'ss'}",
            "legend": "• Mata uang resmi: Schweizer Franken (CHF), bukan Euro.<br>• Ibu kota resmi de facto federal: Bern (bukan Zürich atau Genf)."
        },
        "hints": {
            "concept": "Di Swiss: (A) Memiliki 4 bahasa resmi: Deutsch, Französisch, Italienisch, Rätoromanisch (Benar). (B) Menggunakan Schweizer Franken (CHF), bukan Euro (Salah). (C) Ejaan resmi Swiss tidak menggunakan huruf 'ß', melainkan selalu diganti 'ss' (Benar). (D) Pusat pemerintahan de facto adalah Bern, bukan Genf (Salah).",
            "execution": "Pernyataan yang tepat adalah A dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIKS ASOSIASI BENAR-SALAH (ger-sim-31 .. ger-sim-35)
    # -------------------------------------------------------------
    {
        "id": "ger-sim-31",
        "type": "matrix",
        "materi": "MATRIKS BENAR-SALAH: ANALISIS DEUTSCHLANDTICKET & IKLIM",
        "topic": "Evaluasi Dampak Lingkungan dan Kebijakan Tiket Transportasi 49 Euro",
        "stem": "Tentukan kebenaran pernyataan-pernyataan berikut mengenai kebijakan <strong>Deutschlandticket</strong> dan pengaruhnya terhadap mobilitas masyarakat Jerman:",
        "statements": [
            {
                "text": "Deutschlandticket dirancang sebagai tiket langganan digital bulanan untuk mendorong masyarakat beralih dari mobil pribadi ke transportasi umum ramah lingkungan.",
                "correct": True
            },
            {
                "text": "Pemegang Deutschlandticket bebas menggunakan seluruh armada penerbangan domestik maskapai Lufthansa di seluruh bandara Jerman.",
                "correct": False
            },
            {
                "text": "Tiket ini mempermudah mobilitas lintas negara bagian (*Bundesländer*) karena mengintegrasikan tarif berbagai operator transportasi daerah ke dalam satu tarif seragam.",
                "correct": True
            }
        ],
        "formulaHud": {
            "title": "DEUTSCHLANDTICKET ANALYSE",
            "latex": "\\text{Ziel: Klimaschutz, Tarifharmonisierung, Reduzierung von PKW-Fahrten}",
            "legend": "• Tiket terpadu transportasi lokal & regional se-Jerman.<br>• Tidak berlaku untuk penerbangan atau kereta cepat ICE."
        },
        "hints": {
            "concept": "Deutschlandticket bertujuan menurunkan emisi transportasi dengan mempermudah perpindahan moda ke transportasi umum lokal/regional antarnegara bagian (Benar). Tiket ini sama sekali tidak berlaku untuk penerbangan (Salah). Tiket ini menyatukan tarif ratusan otoritas transportasi lokal (Benar).",
            "execution": "Pernyataan 1 = Benar, Pernyataan 2 = Salah, Pernyataan 3 = Benar."
        }
    },
    {
        "id": "ger-sim-32",
        "type": "matrix",
        "materi": "MATRIKS BENAR-SALAH: GRAMMATIK KASUS & PRÄPOSITIONEN",
        "topic": "Validasi Kebenaran Sintaksis Kasus Dativ dan Akkusativ",
        "stem": "Tentukan kebenaran kaidah gramatikal kasus dan preposisi dalam kalimat-kalimat bahasa Jerman berikut:",
        "statements": [
            {
                "text": "Preposisi 'ohne' dan 'für' selalu mewajibkan kata benda atau kata ganti yang mengikutinya berada dalam kasus Akkusativ.",
                "correct": True
            },
            {
                "text": "Dalam kalimat 'Ich lege das Buch auf dem Tisch', penggunaan kasus Dativ 'dem Tisch' sudah benar karena verba 'legen' menyatakan posisi diam.",
                "correct": False
            },
            {
                "text": "Preposisi 'aus', 'bei', 'mit', 'nach', 'seit', 'von', dan 'zu' selalu mewajibkan kasus Dativ dalam segala situasi penggunaannya.",
                "correct": True
            }
        ],
        "formulaHud": {
            "title": "KASUSREGELN: AKKUSATIV VS DATIV",
            "latex": "\\text{ohne, für } \\rightarrow \\text{Akkusativ} \\quad | \\quad \\text{legen } \\rightarrow \\text{Akkusativ (auf den Tisch)} \\quad | \\quad \\text{aus, bei, mit... } \\rightarrow \\text{Dativ}",
            "legend": "• legen adalah verba dinamis (Wohin? $\\rightarrow$ Akkusativ).<br>• Dativ hanya untuk verba statis liegen (liegt auf dem Tisch)."
        },
        "hints": {
            "concept": "1. Preposisi 'ohne' dan 'für' adalah Akkusativ murni (Benar). 2. Verba 'legen' adalah aksi dinamis (Wohin?), sehingga seharusnya menggunakan Akkusativ 'auf den Tisch', bukan Dativ 'dem Tisch' (Salah). 3. Kelompok preposisi 'aus, bei, mit, nach, seit, von, zu' adalah Dativ murni (Benar).",
            "execution": "Pernyataan 1 = Benar, Pernyataan 2 = Salah, Pernyataan 3 = Benar."
        }
    },
    {
        "id": "ger-sim-33",
        "type": "matrix",
        "materi": "MATRIKS BENAR-SALAH: DUALE AUSBILDUNG & ARBEITSMARKT",
        "topic": "Evaluasi Fakta Sistem Pendidikan Kejuruan dan Ketenagakerjaan Jerman",
        "stem": "Tentukan kebenaran pernyataan-pernyataan berikut mengenai sistem pendidikan kejuruan dan pasar kerja di Jerman:",
        "statements": [
            {
                "text": "Lulusan Duale Ausbildung memiliki daya saing tinggi di pasar kerja karena telah memiliki pengalaman kerja praktis nyata selama masa pelatihannya.",
                "correct": True
            },
            {
                "text": "Di Jerman, seseorang tidak diperbolehkan sama sekali menempuh pendidikan tinggi universitas apabila telah menyelesaikan program Duale Ausbildung.",
                "correct": False
            },
            {
                "text": "Pemerintah federal, serikat pekerja (*Gewerkschaften*), dan asosiasi pengusaha bekerja sama secara tripartit dalam merumuskan standar kurikulum kejuruan.",
                "correct": True
            }
        ],
        "formulaHud": {
            "title": "DUALE AUSBILDUNG: STRUKTUR & CHANCEN",
            "latex": "\\text{Tripartit: Staat} + \\text{Gewerkschaften} + \\text{Arbeitgeberverbände}",
            "legend": "• Menjamin relevansi kurikulum dengan kebutuhan industri nyata.<br>• Lulusan vokasi tetap memiliki jalur melanjutkan studi lanjutan (Meister / Studium)."
        },
        "hints": {
            "concept": "1. Pengalaman kerja nyata memberi lulusan keunggulan daya saing tinggi (Benar). 2. Sistem pendidikan Jerman memiliki jalur fleksibel (Durchlässigkeit) yang memungkinkan lulusan vokasi melanjutkan ke perguruan tinggi (Fachhochschule/Universität) setelah memiliki kualifikasi tertentu (Salah). 3. Kemitraan tripartit menjamin standar mutu kurikulum nasional (Benar).",
            "execution": "Pernyataan 1 = Benar, Pernyataan 2 = Salah, Pernyataan 3 = Benar."
        }
    },
    {
        "id": "ger-sim-34",
        "type": "matrix",
        "materi": "MATRIKS BENAR-SALAH: PERFEKT MIT SEIN VS HABEN",
        "topic": "Penentuan Kata Kerja Bantu Perfekt Berdasarkan Makna Semantis Verba",
        "stem": "Tentukan kebenaran pemilihan kata kerja bantu (*Hilfsverb*) pada kala waktu lampau Perfekt berikut:",
        "statements": [
            {
                "text": "Kata kerja 'aufstehen' (bangun tidur) membentuk Perfekt dengan kata kerja bantu 'sein' (contoh: 'Ich bin um sechs Uhr aufgestanden') karena menandai perubahan kondisi dari tidur menjadi bangun.",
                "correct": True
            },
            {
                "text": "Kata kerja 'arbeiten' (bekerja) membentuk Perfekt dengan kata kerja bantu 'sein' karena membutuhkan banyak energi pergerakan tubuh fisik.",
                "correct": False
            },
            {
                "text": "Kata kerja 'bleiben' (tinggal/menetap) merupakan perkecualian penting yang selalu membentuk Perfekt dengan 'sein' (contoh: 'Wir sind zu Hause geblieben') meskipun tidak menunjukkan perpindahan tempat.",
                "correct": True
            }
        ],
        "formulaHud": {
            "title": "PERFEKT: SEIN VS HABEN REGELN",
            "latex": "\\text{sein: Ortswechsel (fahren), Zustandswechsel (aufstehen), sein/bleiben}",
            "legend": "• arbeiten adalah verba duratif aktif biasa $\\rightarrow$ haben gearbeitet.<br>• bleiben selalu membentuk Perfekt dengan sein (ist geblieben)."
        },
        "hints": {
            "concept": "1. 'aufstehen' menandai Zustandswechsel (perubahan status) sehingga membentuk Perfekt dengan 'sein' (Benar). 2. 'arbeiten' adalah verba tanpa perpindahan tempat/perubahan status, sehingga membentuk Perfekt dengan 'haben' ('Ich habe gearbeitet') (Salah). 3. 'bleiben' adalah verba khusus yang wajib membentuk Perfekt dengan 'sein' ('ist geblieben') (Benar).",
            "execution": "Pernyataan 1 = Benar, Pernyataan 2 = Salah, Pernyataan 3 = Benar."
        }
    },
    {
        "id": "ger-sim-35",
        "type": "matrix",
        "materi": "MATRIKS BENAR-SALAH: TRADISI & BUDAYA PERAYAAN DI JERMAN",
        "topic": "Kebenaran Fakta Mengenai Perayaan Budaya Tradisional di Jerman",
        "stem": "Tentukan kebenaran fakta kultural mengenai festival dan hari perayaan tradisional di negara-negara berbahasa Jerman berikut:",
        "statements": [
            {
                "text": "Perayaan Karnaval (*Karneval / Fasching*) di kawasan Rheinland (Köln, Düsseldorf, Mainz) secara tradisional diawali pada tanggal 11 November tepat pukul 11:11 siang.",
                "correct": True
            },
            {
                "text": "Pasar Natal tradisional (*Weihnachtsmärkte*) di Jerman biasanya baru mulai dibuka setelah perayaan tahun baru tanggal 2 Januari hingga akhir Februari.",
                "correct": False
            },
            {
                "text": "Tradisi merayakan 'Silvester' pada malam tanggal 31 Desember di Jerman identik dengan pesta kembang api untuk menyambut pergantian tahun baru.",
                "correct": True
            }
        ],
        "formulaHud": {
            "title": "DEUTSCHE FESTE & BRÄUCHE",
            "latex": "\\text{Karnevalsbeginn: 11.11. um 11:11 Uhr} \\quad | \\quad \\text{Weihnachtsmarkt: Adventszeit (Dezember)}",
            "legend": "• Weihnachtsmärkte berlangsung selama masa Advent (sepanjang bulan Desember hingga menjelang Natal).<br>• Silvester = perayaan malam tahun baru 31 Desember."
        },
        "hints": {
            "concept": "1. Musim karnaval resmi dibuka pada 11.11 pukul 11:11 (Benar). 2. Pasar Natal dibuka selama masa Advent (akhir November hingga 24 Desember), bukan Januari-Februari (Salah). 3. Malam tahun baru disebut 'Silvester' dan dirayakan dengan pesta kembang api (Benar).",
            "execution": "Pernyataan 1 = Benar, Pernyataan 2 = Salah, Pernyataan 3 = Benar."
        }
    }
]
