# -*- coding: utf-8 -*-
"""
BAHASA PRANCIS - PAKET SOAL LATIHAN MENENGAH (MEDIUM) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / CEFR A2-B1 (DELF A2-B1)
Distribusi:
- 8 Butir: Passé Composé dengan être vs avoir & accord du participe passé dengan subjek
- 9 Butir: L'Imparfait vs Passé Composé (Distingsi Latar Suasana/Durasi vs Peristiwa Mendadak/Aksi Selesai)
- 8 Butir: Pronoms compléments (COD vs COI), pronoms adverbiaux (y, en), et la comparaison (meilleur vs mieux, plus...que)
"""

BAHASA_PRANCIS_MEDIUM_ITEMS = [
    {
        "id": "fra-lat-m-01",
        "materi": "GRAMMAIRE: PASSÉ COMPOSÉ AVEC ÊTRE & ACCORD",
        "topic": "Penyelarasan Participe Passé Kata Kerja Gerak 'partir' dengan Subjek Feminin Jamak",
        "stem": "Dalam laporan perjalanan karyawisata siswi sekolah:\n'Hier soir, après la cérémonie de remise des diplômes, mes deux sœurs ( ... ) pour Paris en train de nuit.'\nBentuk kata kerja bantu dan Participe Passé yang TEPAT dari verba 'partir' adalah...",
        "correct": "sont parties (kata kerja gerak partir memakai auxiliaire être; subjek feminin jamak 'mes deux sœurs' mewajibkan accord -es).",
        "distractors": [
            "ont parti (keliru menggunakan kata kerja bantu avoir dan tanpa accord feminin jamak).",
            "sont partis (kesalahan accord maskulin jamak -s untuk subjek dua orang saudari perempuan).",
            "sont partie (kesalahan accord tunggal -e untuk subjek jamak dua orang).",
            "ont parties (kombinasi keliru kata kerja bantu avoir yang tidak berpasangan dengan verba perpindahan tempat partir)."
        ],
        "formula": {
            "title": "PASSÉ COMPOSÉ AVEC ÊTRE (ACCORD DU PARTICIPE)",
            "latex": "\\text{Sujet (Fém. Plur.)} + \\mathbf{sont} + \\text{Participe } (\\text{parti} + \\mathbf{e} + \\mathbf{s}) = \\mathbf{sont \\text{ } parties}",
            "legend": "• 14 Verba gerak (Maison d'être) wajib menggunakan auxiliaire 'être'.<br>• Bila menggunakan 'être', Participe Passé SELALU menyelaraskan gender dan jumlah dengan subjek."
        },
        "hints": {
            "concept": "Kata kerja 'partir' (berangkat) adalah verba perpindahan tempat yang membentuk Passé Composé dengan kata kerja bantu 'être'. Dengan 'être', Participe Passé wajib bersepakat (accord) dengan subjek. Subjek 'mes deux sœurs' adalah feminin jamak, sehingga ditambahkan akhiran '-es' (sont parties).",
            "execution": "mes deux sœurs (feminin plural) + être + partir -> 'sont parties'."
        }
    },
    {
        "id": "fra-lat-m-02",
        "materi": "GRAMMAIRE: IMPARFAIT VS PASSÉ COMPOSÉ",
        "topic": "Distingsi Latar Suasana Duratif (Imparfait) vs Aksi Interupsi Mendadak (Passé Composé)",
        "stem": "Seorang saksi menceritakan kejadian di peron stasiun:\n'Pendant que les passagers ( ... ) tranquillement leur train sur le quai, une alarme sonore ( ... ) soudainement.'\nPasangan bentuk kata kerja lampau yang TEPAT untuk menggambarkan situasi berlangsung dan interupsi mendadak tersebut adalah...",
        "correct": "attendaient / a retenti (Imparfait untuk aksi berdurasi sedang berlangsung, dan Passé Composé untuk kejadian interupsi tiba-tiba).",
        "distractors": [
            "ont attendu / retentissait (urutan terbalik yang memperlakukan penantian sebagai aksi kilat dan alarme sebagai latar statis).",
            "attendaient / retentissait (penggunaan Imparfait pada kedua klausula yang mengaburkan kejutan interupsi mendadak).",
            "ont attendu / a retenti (penggunaan Passé Composé ganda yang mengabaikan sifat latar belakang duratif dari pendant que).",
            "attendent / va retentir (kombinasi Présent dan Futur yang melanggar kerangka narasi masa lampau)."
        ],
        "formula": {
            "title": "IMPARFAIT (CADRE) VS PASSÉ COMPOSÉ (ACTION PONCTUELLE)",
            "latex": "\\mathbf{Pendant \\text{ } que} + \\text{Imparfait (attendaient)}, \\quad \\mathbf{soudainement} + \\text{Passé Composé (a retenti)}",
            "legend": "• Imparfait: Latar suasana/proses yang sedang berlangsung (sedang menunggu).<br>• Passé Composé: Peristiwa mendadak yang memotong proses (tiba-tiba berbunyi)."
        },
        "hints": {
            "concept": "Klausa 'pendant que' (sementara/selagi) mengindikasikan aksi yang sedang berlangsung berdurasi lama pada masa lalu, sehingga wajib menggunakan Imparfait (attendaient). Kejadian mendadak yang memotong ('soudainement') wajib menggunakan Passé Composé (a retenti).",
            "execution": "Latar duratif = attendaient; Interupsi mendadak = a retenti."
        }
    },
    {
        "id": "fra-lat-m-03",
        "materi": "GRAMMAIRE: PRONOMS COMPLÉMENTS D'OBJET DIRECT (COD)",
        "topic": "Penggantian Objek Penderita Langsung Maskulin Tunggal dengan Pronomina 'le'",
        "stem": "Dalam koordinasi penyusunan laporan keuangan kantor:\n'Est-ce que le directeur a déjà signé le contrat officiel avec le client allemand? — Oui, il ( ... ) a signé ce matin.'\nBentuk pronomina objek langsung (COD) dengan elisi vokal yang TEPAT di depan kata kerja bantu 'a' adalah...",
        "correct": "l' (pronomina COD 'le' yang mengalami elisi vokal sebelum kata kerja bantu a).",
        "distractors": [
            "lui (pronomina objek tak langsung COI yang keliru karena verba signer menuntut objek langsung tanpa preposisi à).",
            "le (bentuk tanpa elisi yang salah ortografi karena bertabrakan langsung dengan huruf vokal a).",
            "en (pronomina kuantitas/partitif yang tidak cocok untuk objek definit le contrat).",
            "y (pronomina tempat atau objek berpreposisi à yang salah fungsi sintaksis)."
        ],
        "formula": {
            "title": "LE PRONOM COMPLÉMENT D'OBJET DIRECT (COD)",
            "latex": "\\text{signer } \\mathbf{le \\text{ } contrat} \\quad \\rightarrow \\quad \\text{il } \\mathbf{l'} \\text{a signé} \\quad (\\text{le } + \\text{a } \\rightarrow \\mathbf{l'a})",
            "legend": "• le contrat (maskulin tunggal) adalah COD (tanpa preposisi).<br>• Menggantikan 'le' di depan huruf vokal 'a' mengalami elisi menjadi 'l''.<br>• Tidak ada accord pada past participle bila COD maskulin tunggal."
        },
        "hints": {
            "concept": "Kata kerja 'signer' adalah verba transitif langsung (signer quelque chose -> COD). Benda yang digantikan adalah 'le contrat' (maskulin tunggal = le). Di depan kata kerja bantu yang diawali vokal 'a', pronomina 'le' mengalami elisi menjadi 'l''.",
            "execution": "le contrat -> COD maskulin tunggal diawali vokal = 'l''. Pilihan tepat: l'."
        }
    },
    {
        "id": "fra-lat-m-04",
        "materi": "GRAMMAIRE: PRONOMS COMPLÉMENTS D'OBJET INDIRECT (COI)",
        "topic": "Penggantian Objek Penerima Orang Tunggal dengan Pronomina 'lui'",
        "stem": "Seorang ibu mengingatkan putrinya untuk menghubungi dokter:\n'As-tu pensé à téléphoner à ta grand-mère pour prendre de ses nouvelles? — Oui maman, je ( ... ) ai téléphoné hier soir.'\nBentuk pronomina objek tak langsung (COI) yang TEPAT untuk menggantikan 'à ta grand-mère' adalah...",
        "correct": "lui (pronomina COI persona ketiga tunggal yang menggantikan orang berpreposisi à tanpa terpengaruh gender maskulin/feminin).",
        "distractors": [
            "la (pronomina objek langsung COD yang salah karena verba téléphoner menuntut preposisi à).",
            "leur (pronomina COI jamak yang keliru jumlah untuk subjek tunggal nenek).",
            "l' (bentuk elisi COD yang melanggar aturan valensi verba téléphoner à quelqu'un).",
            "elle (pronomina tonik yang tidak boleh diletakkan di depan verba terkonjugasi tanpa preposisi)."
        ],
        "formula": {
            "title": "LE PRONOM COMPLÉMENT D'OBJET INDIRECT (COI)",
            "latex": "\\text{téléphoner } \\mathbf{à \\text{ } quelqu'un} \\quad \\rightarrow \\quad \\mathbf{lui} \\quad (\\text{masculin ou féminin singulier})",
            "legend": "• téléphoner à ta grand-mère = verbe + à + personne $\\rightarrow$ COI.<br>• COI orang ketiga tunggal adalah 'lui' (baik untuk pria maupun wanita).<br>• DILARANG elisi: 'je lui ai téléphoné' (bukan l'ai!)."
        },
        "hints": {
            "concept": "Kata kerja 'téléphoner' menuntut preposisi 'à' untuk orang (téléphoner à quelqu'un -> COI). Pronomina COI orang ketiga tunggal untuk pria maupun wanita adalah 'lui' (à mon père -> lui; à ma grand-mère -> lui). Pronomina 'lui' TIDAK pernah mengalami elisi.",
            "execution": "à ta grand-mère -> COI tunggal = 'lui'."
        }
    },
    {
        "id": "fra-lat-m-05",
        "materi": "GRAMMAIRE: LE PRONOM ADVERBIAL 'Y'",
        "topic": "Penggantian Keterangan Tempat Berpreposisi dengan Pronomina 'y'",
        "stem": "Dua sahabat membicarakan rencana akhir pekan di museum seni:\n'Tu vas souvent au musée du Louvre le dimanche? — Oui, j'( ... ) vais presque tous les mois avec mes camarades.'\nBentuk pronomina adverbial yang TEPAT untuk menggantikan frasa tempat 'au musée du Louvre' adalah...",
        "correct": "y (pronomina adverbial yang menggantikan komplemen tempat yang diperkenalkan oleh preposisi arah à/au/en/dans).",
        "distractors": [
            "en (pronomina adverbial yang menggantikan tempat berpreposisi asal de atau komplemen kuantitas partitif).",
            "le (pronomina COD yang salah fungsi sintaksis untuk keterangan lokasi tempat).",
            "lui (pronomina orang tak langsung yang keliru untuk merujuk pada gedung museum).",
            "là (kata keterangan penunjuk tempat mandiri yang tidak dapat disisipkan sebagai klitik di depan kata kerja)."
        ],
        "formula": {
            "title": "LE PRONOM ADVERBIAL Y (LIEU)",
            "latex": "\\text{aller } \\mathbf{au \\text{ } musée} \\quad (\\text{à} + \\text{lieu}) \\quad \\rightarrow \\quad \\mathbf{y} \\quad (\\text{j'} \\mathbf{y} \\text{ vais})",
            "legend": "• Menggantikan frasa tempat dengan preposisi à, au, à la, en, dans, chez, sur.<br>• Posisinya berada tepat di depan kata kerja: j'y vais."
        },
        "hints": {
            "concept": "Pronomina adverbial 'y' digunakan untuk menggantikan keterangan tempat yang diawali oleh preposisi arah atau lokasi seperti 'à', 'au', 'en', 'dans'. Frasa 'au musée du Louvre' digantikan oleh 'y' (j'y vais).",
            "execution": "au musée du Louvre -> ganti dengan pronomina tempat 'y'."
        }
    },
    {
        "id": "fra-lat-m-06",
        "materi": "GRAMMAIRE: LE PRONOM ADVERBIAL 'EN'",
        "topic": "Penggantian Komplemen Partitif atau Kuantitas dengan Pronomina 'en'",
        "stem": "Di pasar buah tradisional:\n'Voulez-vous encore des pommes bio, Madame? — Non merci, j'( ... ) ai déjà acheté deux kilos ce matin.'\nBentuk pronomina yang TEPAT untuk menggantikan kata benda kuantitas dengan artikel partitif 'des pommes' adalah...",
        "correct": "en (pronomina adverbial yang wajib digunakan untuk menggantikan kata benda yang didahului kuantitas, angka, atau partitif de/des).",
        "distractors": [
            "les (pronomina COD definit yang salah digunakan untuk kuantitas partitif atau benda berangka terbilang).",
            "y (pronomina tempat yang keliru fungsi sintaksis untuk bahan makanan terhitung kuantitas).",
            "la (pronomina COD feminin tunggal yang tidak cocok untuk kuantitas des pommes).",
            "leur (pronomina COI orang jamak yang tidak memiliki relasi semantik dengan apel)."
        ],
        "formula": {
            "title": "LE PRONOM ADVERBIAL EN (QUANTITÉ)",
            "latex": "\\text{acheter } \\mathbf{des \\text{ } pommes} \\text{ (partitif / quantité)} \\quad \\rightarrow \\quad \\mathbf{en} \\quad (\\text{j'} \\mathbf{en} \\text{ ai acheté deux kilos})",
            "legend": "• Menggantikan kata benda diawali de, du, de la, des, un, une, atau angka/kuantitas.<br>• Kata jumlah (deux kilos) wajib disebutkan di akhir kalimat."
        },
        "hints": {
            "concept": "Pronomina 'en' digunakan untuk menggantikan kata benda yang didahului oleh artikel partitif (du, de la, des) atau penanda kuantitas/angka. Bila ada kata takaran (dua kilo), 'en' diletakkan di depan verba dan kata takarannya di akhir kalimat: 'j'en ai acheté deux kilos'.",
            "execution": "des pommes + kuantitas -> ganti dengan 'en'."
        }
    },
    {
        "id": "fra-lat-m-07",
        "materi": "GRAMMAIRE: VERBES PRONOMINAUX AU PASSÉ COMPOSÉ",
        "topic": "Penyelarasan Participe Passé Verba Refleksif dengan Subjek Feminin Tunggal",
        "stem": "Hélène menceritakan rutinitas paginya kemarin:\n'Hier, comme j'avais un train très tôt, je me ( ... ) à cinq heures du matin.'\nBentuk kata kerja bantu dan Participe Passé yang TEPAT dari verba refleksif 'se réveiller' untuk subjek Hélène (wanita) adalah...",
        "correct": "suis réveillée (verba refleksif selalu membentuk Passé Composé dengan être; subjek wanita menuntut penambahan akhiran feminin -e).",
        "distractors": [
            "ai réveillé (keliru menggunakan kata kerja bantu avoir yang dilarang mutlak pada verba refleksif).",
            "suis réveillé (kesalahan mengabaikan accord feminin -e untuk subjek wanita Hélène).",
            "suis réveillés (kesalahan penambahan akhiran jamak -s untuk subjek tunggal je).",
            "ai réveillée (kombinasi keliru kata kerja bantu avoir dengan accord refleksif)."
        ],
        "formula": {
            "title": "VERBES PRONOMINAUX AU PASSÉ COMPOSÉ",
            "latex": "\\text{Sujet (Fém. Sing.)} + \\mathbf{me \\text{ } suis} + \\mathbf{réveillée} \\quad (\\text{accord avec le sujet})",
            "legend": "• Semua verba refleksif/pronominal (se...) WAJIB menggunakan auxiliaire 'être'.<br>• Bila pronomina refleksif berfungsi sebagai COD (réveiller qui? -> me = Hélène), terjadi accord feminin (+e)."
        },
        "hints": {
            "concept": "Seluruh kata kerja refleksif (verbes pronominaux) membentuk Passé Composé dengan kata kerja bantu 'être' (je me suis, tu t'es, il s'est...). Karena Hélène adalah seorang perempuan dan pronomina 'me' adalah COD, Participe Passé mendapat tambahan huruf '-e' (réveillée).",
            "execution": "je (Hélène) + se réveiller -> 'je me suis réveillée'."
        }
    },
    {
        "id": "fra-lat-m-08",
        "materi": "GRAMMAIRE: LA COMPARAISON (MEILLEUR VS MIEUX)",
        "topic": "Distingsi Komparatif Adjektiva 'meilleur' (Kualitas Benda) vs Adverbia 'mieux' (Cara Kerja)",
        "stem": "Dua mahasiswa mengevaluasi cara belajar bahasa asing:\n'La prononciation de Marc est excellente, mais Claire parle encore ( ... ) que lui.'\nBentuk perbandingan tingkat lebih yang TEPAT untuk memodifikasi kata kerja wicara 'parle' adalah...",
        "correct": "mieux (bentuk komparatif dari kata keterangan bien yang digunakan untuk memodifikasi kata kerja tindakan).",
        "distractors": [
            "meilleur (bentuk komparatif dari kata sifat bon yang hanya boleh memodifikasi kata benda maskulin).",
            "meilleure (bentuk komparatif dari kata sifat bon untuk kata benda bergender feminin).",
            "plus bon (bentuk terlarang dalam bahasa Prancis yang merupakan kesalahan analogi kasar).",
            "plus bien (bentuk tidak baku yang dilarang mutlak dalam gramatika bahasa Prancis baku)."
        ],
        "formula": {
            "title": "DISTINCTION: MEILLEUR VS MIEUX",
            "latex": "\\mathbf{bon} \\rightarrow \\mathbf{meilleur} \\text{ (Adjectif, qualifie un nom)} \\quad | \\quad \\mathbf{bien} \\rightarrow \\mathbf{mieux} \\text{ (Adverbe, modifie un verbe)}",
            "legend": "• Verba tindakan (parle): Claire parle bien $\\rightarrow$ Claire parle MIEUX.<br>• Nomina (le vin): Un bon vin $\\rightarrow$ Un MEILLEUR vin.<br>• 'Plus bon' dan 'plus bien' TIDAK ADA dalam bahasa Prancis."
        },
        "hints": {
            "concept": "Dalam bahasa Prancis: 'bon' (baik/enak, kata sifat) berubah menjadi 'meilleur' saat memodifikasi kata benda. Sedangkan 'bien' (dengan baik, kata keterangan) berubah menjadi 'mieux' saat memodifikasi kata kerja. Karena kalimat memodifikasi kata kerja 'parle', bentuk yang tepat adalah 'mieux'.",
            "execution": "Memodifikasi kata kerja 'parle' -> gunakan 'mieux'."
        }
    },
    {
        "id": "fra-lat-m-09",
        "materi": "GRAMMAIRE: LE FUTUR SIMPLE DE L'INDICATIF",
        "topic": "Akar Kata Kerja Tidak Beraturan dari Verba 'faire' pada Futur Simple (fer-)",
        "stem": "Dalam rencana pembangunan infrastruktur hijau lima tahun ke depan:\n'D'ici 2030, la municipalité de Paris ( ... ) de grands efforts pour réduire la pollution automobile dans le centre historique.'\nBentuk konjugasi Futur Simple yang TEPAT dari kata kerja 'faire' untuk persona ketiga tunggal 'la municipalité' adalah...",
        "correct": "fera (akar tidak beraturan fer- + akhiran Futur Simple persona ketiga tunggal -a).",
        "distractors": [
            "faira (kesalahan analogi dengan mempertahankan bentuk dasar infinitif fair-).",
            "faisait (bentuk lampau Imparfait yang bertentangan dengan keterangan masa depan d'ici 2030).",
            "feras (bentuk Futur Simple persona kedua tunggal untuk subjek tu).",
            "feront (bentuk Futur Simple persona ketiga jamak yang keliru jumlah untuk subjek tunggal la municipalité)."
        ],
        "formula": {
            "title": "LE FUTUR SIMPLE: RADICAL DU VERBE FAIRE",
            "latex": "\\text{Radical irrégulier: } \\mathbf{fer-} + \\text{Terminaisons: } \\text{-ai, -as, } \\mathbf{-a}, \\text{ -ons, -ez, -ont}",
            "legend": "• la municipalité (elle) $\\rightarrow$ radical 'fer-' + akhiran '-a' = 'fera'.<br>• Tidak boleh ada huruf 'i' dari kata faire pada akar bentuk futur."
        },
        "hints": {
            "concept": "Kata kerja 'faire' memiliki akar tidak beraturan pada Futur Simple, yaitu 'fer-'. Akhiran Futur Simple untuk persona ketiga tunggal (il/elle/la municipalité) adalah '-a'. Maka bentuknya adalah 'fera'.",
            "execution": "faire -> radical 'fer-' + '-a' = 'fera'."
        }
    },
    {
        "id": "fra-lat-m-10",
        "materi": "GRAMMAIRE: LES PRONOMS RELATIFS SIMPLES (QUI VS QUE)",
        "topic": "Penggunaan Pronomina Relatif 'qui' sebagai Subjek dari Anak Kalimat",
        "stem": "Dalam ulasan novel sastra pemenang penghargaan:\n'C'est un auteur talentueux ( ... ) raconte avec une grande émotion l'histoire des immigrés arrivés en France dans les années soixante.'\nPronomina relatif yang TEPAT untuk menggantikan subjek pelaku 'un auteur talentueux' dalam anak kalimat adalah...",
        "correct": "qui (pronomina relatif yang berfungsi sebagai subjek gramatikal yang langsung diikuti kata kerja raconte).",
        "distractors": [
            "que (pronomina relatif yang berfungsi sebagai objek langsung COD dan wajib diikuti oleh subjek baru).",
            "dont (pronomina relatif yang menggantikan komplemen berpreposisi de).",
            "où (pronomina relatif yang menggantikan keterangan tempat atau waktu kejadian).",
            "lequel (pronomina relatif majemuk yang tidak lazim digunakan untuk subjek manusia tunggal tanpa preposisi)."
        ],
        "formula": {
            "title": "PRONOMS RELATIFS: QUI (SUJET) VS QUE (COD)",
            "latex": "\\text{Antécédent} + \\mathbf{qui} + \\mathbf{Verbe} \\quad \\leftrightarrow \\quad \\text{Antécédent} + \\mathbf{que} + \\mathbf{Sujet} + \\text{Verbe}",
            "legend": "• 'qui' selalu berfungsi sebagai subjek anak kalimat (langsung diikuti kata kerja: qui raconte).<br>• 'que' berfungsi sebagai objek langsung (diikuti subjek: que j'aime)."
        },
        "hints": {
            "concept": "Aturan praktis pronomina relatif sederhana: 'qui' berfungsi sebagai subjek dan langsung diikuti oleh kata kerja (qui + verbe). 'que' berfungsi sebagai objek penderita dan diikuti oleh subjek baru (que + sujet + verbe). Karena langsung diikuti kata kerja 'raconte', gunakan 'qui'.",
            "execution": "Diikuti langsung kata kerja 'raconte' -> gunakan 'qui'."
        }
    },
    {
        "id": "fra-lat-m-11",
        "materi": "GRAMMAIRE: L'ACCORD DU PARTICIPE PASSÉ AVEC AVOIR",
        "topic": "Kaidah Accord Participe Passé Ketika Objek Langsung (COD) Mendahului Kata Kerja",
        "stem": "Seorang kurator museum memamerkan koleksi lukisan antik:\n'Regardez ces magnifiques toiles de maître! Le musée les a ( ... ) lors d'une vente aux enchères internationale à Genève.'\nBentuk Participe Passé dari kata kerja 'acheter' yang TEPAT untuk menyelaraskan dengan pronomina COD 'les' (merujuk pada 'ces toiles', feminin jamak) adalah...",
        "correct": "achetées (Participe Passé dengan penambahan akhiran feminin jamak -es karena COD 'les' mendahului kata kerja bantu avoir).",
        "distractors": [
            "acheté (bentuk maskulin tunggal tanpa accord yang keliru karena posisi COD berada di depan verba).",
            "achetée (bentuk feminin tunggal yang melupakan penanda kuantitas jamak toiles).",
            "achetés (bentuk maskulin jamak yang salah gender untuk kata benda feminin une toile).",
            "achetez (bentuk Présent persona kedua jamak yang merusak struktur Passé Composé)."
        ],
        "formula": {
            "title": "ACCORD DU PARTICIPE PASSÉ AVEC AVOIR (RÈGLE DU COD PRÉCÉDENT)",
            "latex": "\\text{COD précédent (les = ces toiles, Fém. Plur.)} + \\text{avoir} + \\mathbf{Participe } (\\text{acheté} + \\mathbf{e} + \\mathbf{s}) = \\mathbf{achetées}",
            "legend": "• Dengan 'avoir', biasanya Participe Passé TIDAK bersepakat dengan subjek.<br>• PENGECUALIAN EMAS: Bila objek langsung (COD) diletakkan SEBELUM kata kerja bantu, Participe Passé WAJIB bersepakat dengan COD tersebut."
        },
        "hints": {
            "concept": "Aturan emas bahasa Prancis: Kata kerja bantu 'avoir' umumnya tidak mengalami accord. Namun, jika objek penderita langsung (COD) mendahului kata kerja (les = ces magnifiques toiles, feminin jamak), Participe Passé WAJIB bersepakat dengan COD tersebut (+es -> achetées).",
            "execution": "COD 'les' (feminin jamak mendahului verba) -> 'achetées'."
        }
    },
    {
        "id": "fra-lat-m-12",
        "materi": "GRAMMAIRE: FORMATION DE L'IMPARFAIT DE L'INDICATIF",
        "topic": "Penurunan Bentuk Imparfait dari Akar Persona Pertama Jamak 'nous' (Prendre -> Prenions)",
        "stem": "Kakek mengenang kebiasaan masa mudanya di pedesaan Provence:\n'Quand nous étions jeunes, mon frère et moi ( ... ) toujours le train à vapeur pour aller au marché le samedi.'\nBentuk konjugasi Imparfait yang TEPAT dari kata kerja 'prendre' untuk subjek 'mon frère et moi' (nous) adalah...",
        "correct": "prenions (akar kata kerja dari nous au présent 'pren-' + akhiran Imparfait persona pertama jamak -ions).",
        "distractors": [
            "prenionss (kesalahan ejaan konsonan ganda pada akhiran Imparfait).",
            "prenaient (bentuk konjugasi persona ketiga jamak untuk subjek ils/elles).",
            "prenais (bentuk konjugasi persona tunggal je/tu).",
            "avons pris (bentuk Passé Composé yang keliru untuk konteks kebiasaan berulang masa lalu yang ditandai kata toujours)."
        ],
        "formula": {
            "title": "FORMATION DE L'IMPARFAIT",
            "latex": "\\text{Radical: } \\text{nous prenons (Présent)} \\rightarrow \\mathbf{pren-} + \\text{Terminaisons: } \\text{-ais, -ais, -ait, } \\mathbf{-ions}, \\text{ -iez, -aient}",
            "legend": "• Mon frère et moi = nous.<br>• Radical 'pren-' + akhiran '-ions' = 'prenions'.<br>• Digunakan untuk kebiasaan masa lalu (habitude dans le passé)."
        },
        "hints": {
            "concept": "L'Imparfait dibentuk dari akar kata kerja subjek 'nous' pada waktu sekarang (nous prenons -> akar: 'pren-') ditambah akhiran Imparfait (-ais, -ais, -ait, -ions, -iez, -aient). Untuk subjek 'mon frère et moi' (= nous), bentuknya adalah 'prenions'.",
            "execution": "nous + Imparfait dari prendre = 'prenions'."
        }
    },
    {
        "id": "fra-lat-m-13",
        "materi": "GRAMMAIRE: LE COMPARATIF D'ÉGALITÉ",
        "topic": "Perbandingan Derajat Kesetaraan untuk Kata Sifat Menggunakan 'aussi ... que'",
        "stem": "Dua saudara kembar memiliki prestasi akademis yang seimbang:\n'Dans cette classe bilingue, Marc est ( ... ) travailleur que sa sœur jumelle Juliette.'\nStruktur perbandingan kesetaraan yang TEPAT untuk menyertai kata sifat 'travailleur' adalah...",
        "correct": "aussi (partikel perbandingan kesetaraan baku 'aussi + adjectif + que' yang bermakna 'sama ... seperti').",
        "distractors": [
            "autant (partikel kesetaraan yang hanya digunakan untuk kata kerja atau kata benda dengan de, bukan kata sifat).",
            "plus (partikel perbandingan keunggulan yang bermakna lebih, bukan kesetaraan seimbang).",
            "si (partikel penegas intensitas yang tidak membentuk perbandingan berpasangan resmi dengan que).",
            "comme (kata pembanding persamaan gaya yang keliru dipasangkan dengan kata sifat dan que)."
        ],
        "formula": {
            "title": "LE COMPARATIF D'ÉGALITÉ: AUSSI VS AUTANT",
            "latex": "\\mathbf{aussi} + \\text{Adjectif / Adverbe} + \\mathbf{que} \\quad \\leftrightarrow \\quad \\mathbf{autant \\text{ } de} + \\text{Nom} + \\mathbf{que}",
            "legend": "• Di depan kata sifat (travailleur): SELALU gunakan 'aussi'.<br>• 'Autant' hanya untuk kata benda (autant de livres) atau kata kerja (il travaille autant que)."
        },
        "hints": {
            "concept": "Untuk menyatakan perbandingan setara: di depan kata sifat (adjectif seperti 'travailleur'), bahasa Prancis selalu menggunakan 'aussi ... que'. Partikel 'autant' hanya digunakan untuk membandingkan kata kerja atau kata benda ('autant de').",
            "execution": "kata sifat 'travailleur' + perbandingan setara -> 'aussi'."
        }
    },
    {
        "id": "fra-lat-m-14",
        "materi": "GRAMMAIRE: LE VERBE DEVOIR AU PRÉSENT",
        "topic": "Konjugasi Kata Kerja Kewajiban 'devoir' untuk Persona Pertama Jamak 'nous'",
        "stem": "Sebelum batas waktu pengumpulan tugas akhir semester:\n'Pour réussir notre projet de recherche, nous ( ... ) respecter scrupuleusement les consignes méthodologiques du professeur.'\nBentuk konjugasi kata kerja 'devoir' yang TEPAT untuk subjek 'nous' pada waktu sekarang adalah...",
        "correct": "devons (bentuk konjugasi teratur persona pertama jamak nous dari verba devoir).",
        "distractors": [
            "doivent (bentuk konjugasi persona ketiga jamak untuk subjek ils/elles).",
            "devez (bentuk konjugasi persona kedua jamak untuk subjek vous).",
            "dois (bentuk konjugasi persona tunggal je/tu).",
            "doit (bentuk konjugasi persona ketiga tunggal il/elle)."
        ],
        "formula": {
            "title": "CONJUGAISON DU VERBE DEVOIR AU PRÉSENT",
            "latex": "\\text{je dois, tu dois, il doit, } \\mathbf{nous \\text{ } devons}, \\text{ vous devez, ils doivent}",
            "legend": "• Verba modalitas kewajiban/keharusan.<br>• Persona 'nous' mempertahankan akar vokal e: devons."
        },
        "hints": {
            "concept": "Kata kerja 'devoir' (harus/wajib) dikonjugasikan: je dois, tu dois, il doit, nous devons, vous devez, ils doivent. Untuk subjek 'nous', bentuknya adalah 'devons'.",
            "execution": "nous + devoir -> 'nous devons'."
        }
    },
    {
        "id": "fra-lat-m-15",
        "materi": "GRAMMAIRE: LES PRONOMS RELATIFS SIMPLES (DONT)",
        "topic": "Penggunaan Pronomina Relatif 'dont' untuk Menggantikan Objek Berpreposisi 'de'",
        "stem": "Dalam rekomendasi buku literatur klasik:\n'Le Petit Prince est un chef-d'œuvre littéraire d'Antoine de Saint-Exupéry ( ... ) tout le monde connaît les célèbres citations sur l'amitié.'\nPronomina relatif yang TEPAT untuk menggantikan komplemen kepemilikan 'les citations de ce chef-d'œuvre' adalah...",
        "correct": "dont (pronomina relatif yang menggantikan komplemen benda yang terikat dengan preposisi 'de').",
        "distractors": [
            "que (pronomina relatif COD yang salah karena tidak dapat mengekspresikan hubungan partitif/genitif de).",
            "qui (pronomina relatif subjek yang keliru karena klausula sudah memiliki subjek lengkap tout le monde).",
            "où (pronomina relatif spasial/temporal yang keliru untuk rujukan karya seni konseptual).",
            "d'où (adverbia relatif yang menyatakan titik tolak asal pergerakan fisik secara harfiah)."
        ],
        "formula": {
            "title": "LE PRONOM RELATIF DONT",
            "latex": "\\text{Antécédent} + \\mathbf{dont} + \\text{Proposition avec complément introduit par } \\mathbf{de}",
            "legend": "• Menggantikan 'de + nom' (les citations DE ce chef-d'œuvre).<br>• Digunakan juga untuk verba berpreposisi de: parler de, avoir besoin de, avoir peur de."
        },
        "hints": {
            "concept": "Pronomina relatif 'dont' digunakan untuk menggantikan frasa yang diawali preposisi 'de' (dalam hal ini hubungan kepemilikan: les citations DE ce chef-d'œuvre).",
            "execution": "les citations de ce chef-d'œuvre -> gunakan pronomina relatif 'dont'."
        }
    },
    {
        "id": "fra-lat-m-16",
        "materi": "GRAMMAIRE: LE CONDITIONNEL PRÉSENT DE POLITESSE",
        "topic": "Bentuk Kesantunan Menggunakan Verba 'pouvoir' (pourriez-vous)",
        "stem": "Di konter layanan pelanggan bandara Charles de Gaulle:\n'Pardon Monsieur, ( ... )-vous m'indiquer où se trouve la porte d'embarquement B24?'\nBentuk konjugasi kesantunan Conditionnel Présent dari kata kerja 'pouvoir' untuk subjek 'vous' adalah...",
        "correct": "Pourriez (akar verba pourr- + akhiran Conditionnel persona kedua jamak -iez).",
        "distractors": [
            "Pouvez (bentuk Présent indikatif biasa yang kurang bernada santun halus dalam permintaan bantuan).",
            "Pouviez (bentuk Imparfait yang menyatakan kemampuan di masa lampau).",
            "Pourrez (bentuk Futur Simple indikatif yang menanyakan kepastian masa depan, bukan permohonan santun).",
            "Puissiez (bentuk Subjonctif yang tidak dapat digunakan sebagai verba mandiri dalam kalimat tanya langsung)."
        ],
        "formula": {
            "title": "CONDITIONNEL DE POLITESSE: POUVOIR",
            "latex": "\\text{Radical du futur: } \\mathbf{pourr-} + \\text{Terminaison de l'imparfait: } \\mathbf{-iez} = \\mathbf{Pourriez-vous}",
            "legend": "• Standar kesantunan tertinggi untuk meminta bantuan orang asing.<br>• Padanan: 'Sudikah/Bisakah kiranya Anda...'."
        },
        "hints": {
            "concept": "Untuk meminta bantuan secara sangat santun (demande polie), bahasa Prancis menggunakan Conditionnel Présent dari kata kerja 'pouvoir' (pourriez-vous). Rumusnya: akar futur (pourr-) + akhiran imparfait (-iez) = 'Pourriez-vous'.",
            "execution": "pouvoir di Conditionnel dengan vous = 'Pourriez-vous'."
        }
    },
    {
        "id": "fra-lat-m-17",
        "materi": "GRAMMAIRE: LES PRONOMS COMBINÉS (DOUBLE PRONOM)",
        "topic": "Urutan Dua Pronomina Objek di Depan Kata Kerja (COD sebelum COI Persona Ketiga: le lui)",
        "stem": "Ibu guru menanyakan tugas siswa kepada ketua kelas:\n'Est-ce que tu as déjà rendu le devoir de mathématiques au professeur? — Oui, je ( ... ) ai rendu ce matin avant le début des cours.'\nKombinasi dua pronomina objek (COD 'le devoir' dan COI 'au professeur') yang TEPAT di depan kata kerja adalah...",
        "correct": "le lui (urutan baku pronomina orang ketiga: COD 'le' mendahului COI 'lui').",
        "distractors": [
            "lui le (urutan terbalik yang melanggar hukum sintaksis kombinasi pronomina bahasa Prancis).",
            "l'y (kesalahan mengganti orang au professeur dengan pronomina tempat y).",
            "en lui (penggunaan pronomina partitif en yang salah untuk objek definit le devoir).",
            "le leur (kesalahan jumlah pronomina jamak leur untuk satu orang guru au professeur)."
        ],
        "formula": {
            "title": "L'ORDRE DES DOUBLES PRONOMS COMPLÉMENTS",
            "latex": "\\text{Devant le verbe: } \\text{me/te/se/nous/vous} \\rightarrow \\mathbf{le/la/les} \\rightarrow \\mathbf{lui/leur} \\rightarrow \\text{y} \\rightarrow \\text{en}",
            "legend": "• Bila kedua pronomina adalah orang ketiga: COD (le/la/les) WAJIB mendahului COI (lui/leur).<br>• le devoir (le) + au professeur (lui) $\\rightarrow$ je le lui ai rendu."
        },
        "hints": {
            "concept": "Urutan dua kata ganti komplemen persona ketiga di depan kata kerja dalam bahasa Prancis: COD (le/la/les) diletakkan LEBIH DAHULU daripada COI (lui/leur). Objeknya: 'le devoir' (le) dan 'au professeur' (lui). Maka urutannya adalah 'le lui'.",
            "execution": "COD (le) + COI (lui) = 'le lui'."
        }
    },
    {
        "id": "fra-lat-m-18",
        "materi": "GRAMMAIRE: LE GÉRONDIF (EN + PARTICIPE PRÉSENT)",
        "topic": "Menyatakan Cara atau Keserentakan Tindakan Menggunakan Gérondif",
        "stem": "Dalam tips kesehatan tentang gaya hidup aktif:\n'On peut facilement améliorer sa forme physique quotidienne ( ... ) les escaliers au lieu de prendre systématiquement l'ascenseur.'\nBentuk Gérondif yang TEPAT dari kata kerja 'prendre' adalah...",
        "correct": "en prenant (pembentukan Gérondif dengan partikel en + akar nous au présent pren- + akhiran -ant).",
        "distractors": [
            "en prendant (kesalahan analogi bentuk akar dasar tanpa pembentukan teratur dari nous prenons).",
            "prenant (bentuk Participe Présent biasa tanpa partikel en yang tidak mengekspresikan fungsi instrumental).",
            "en pris (kesalahan memadukan partikel en dengan bentuk Participe Passé pris).",
            "pour prendre (konstruksi infinitif tujuan yang mengubah makna instrumen sarana menjadi tujuan)."
        ],
        "formula": {
            "title": "FORMATION DU GÉRONDIF",
            "latex": "\\mathbf{en} + \\text{Radical de nous au présent (pren-)} + \\mathbf{-ant} = \\mathbf{en \\text{ } prenant}",
            "legend": "• Menyatakan cara (manière) atau keserentakan aksi (simultanéité).<br>• Subjek kedua tindakan harus identik."
        },
        "hints": {
            "concept": "Le Gérondif dibentuk dengan partikel 'en' + akar kata kerja persona 'nous' waktu sekarang (nous prenons -> 'pren-') + akhiran '-ant' (en prenant). Gérondif digunakan untuk menyatakan cara atau metode (dengan menaiki tangga).",
            "execution": "en + prenant = 'en prenant'."
        }
    },
    {
        "id": "fra-lat-m-19",
        "materi": "GRAMMAIRE: LA NÉGATION COMPLEXE (NE...JAMAIS / NE...PLUS)",
        "topic": "Menyatakan Penghentian Suatu Kebiasaan dengan 'ne ... plus'",
        "stem": "Setelah dokter mendiagnosis gangguan lambung akut pada pasiennya:\n'Le patient a décidé de changer ses habitudes: il était un grand buveur de café, mais maintenant il ( ... ) en boit ( ... ).'\nPasangan partikel negasi yang TEPAT untuk menyatakan bahwa ia 'tidak lagi meminum kopi' adalah...",
        "correct": "n' / plus (partikel negasi 'ne ... plus' yang bermakna 'tidak lagi' untuk aksi yang dahulu dilakukan namun kini dihentikan).",
        "distractors": [
            "ne / jamais (negasi yang bermakna 'tidak pernah sama sekali' yang bertentangan dengan fakta bahwa dahulu ia sering minum kopi).",
            "ne / rien (negasi yang bermakna 'tidak meminum apa-apa', bukan penghentian kebiasaan).",
            "n' / pas encore (negasi yang bermakna 'belum', mengindikasikan ia akan meminumnya lagi nanti).",
            "ne / que (konstruksi pembatasan yang bermakna 'hanya', bukan penyangkalan penghentian kebiasaan)."
        ],
        "formula": {
            "title": "LA NÉGATION COMPLEXE: NE...PLUS",
            "latex": "\\mathbf{ne \\dots plus} = \\text{arrêt d'une action continue (ne fait plus = tidak lagi)}",
            "legend": "• Menunjukkan kontras: dahulu sering minum kopi, sekarang sudah berhenti.<br>• Elisi di depan vokal/pronomina en: n'en boit plus."
        },
        "hints": {
            "concept": "Negasi 'ne ... plus' berarti 'tidak lagi' (penghentian suatu kebiasaan yang dulu ada). Karena dahulu ia peminum kopi berat tetapi sekarang berhenti, negasi yang tepat adalah 'n' ... plus' (mengalami elisi sebelum pronomina 'en').",
            "execution": "Tidak lagi = 'n' ... plus'."
        }
    },
    {
        "id": "fra-lat-m-20",
        "materi": "GRAMMAIRE: PRÉPOSITIONS AVEC LES NOMS DE VILLES & ÎLES",
        "topic": "Penggunaan Preposisi 'à' Tanpa Artikel untuk Kota",
        "stem": "Dalam profil seorang diplomat internasional:\n'Après avoir vécu dix ans à Tokyo et cinq ans à New York, elle travaille désormais ( ... ) Genève pour les Nations Unies.'\nPreposisi tempat yang TEPAT di depan nama kota 'Genève' adalah...",
        "correct": "à (preposisi tempat standar yang digunakan di depan nama kota di seluruh dunia tanpa memandang gender).",
        "distractors": [
            "en (preposisi yang hanya digunakan untuk nama negara feminin atau wilayah provinsi, bukan kota).",
            "au (preposisi kontraksi maskulin yang digunakan untuk negara maskulin).",
            "dans la (preposisi yang menuntut artikel dan tidak lazim untuk rujukan umum keberadaan di kota).",
            "chez (preposisi yang hanya digunakan untuk orang, kediaman pribadi, atau tempat usaha profesional)."
        ],
        "formula": {
            "title": "PRÉPOSITION DEVANT LES VILLES",
            "latex": "\\mathbf{à} + \\text{Nom de ville (Paris, Genève, Tokyo, Jakarta)}",
            "legend": "• Semua nama kota selalu menggunakan preposisi 'à' tanpa artikel (kecuali kota berkata sandang bawaan seperti Le Havre $\\rightarrow$ au Havre).<br>• Genève adalah kota di Swiss $\\rightarrow$ à Genève."
        },
        "hints": {
            "concept": "Nama kota di seluruh dunia dalam bahasa Prancis selalu menggunakan preposisi 'à' tanpa artikel (à Paris, à Genève, à Jakarta).",
            "execution": "Nama kota 'Genève' -> preposisi = 'à Genève'."
        }
    },
    {
        "id": "fra-lat-m-21",
        "materi": "GRAMMAIRE: L'EXPRESSION DE LA CAUSE (PARCE QUE VS GRÂCE À)",
        "topic": "Menyatakan Sebab Positif Menggunakan Preposisi 'grâce à'",
        "stem": "Dalam pidato kelulusan sarjana berprestasi:\n'J'ai réussi à obtenir cette bourse d'excellence internationale ( ... ) soutien indéfectible de mes professeurs et de ma famille.'\nPreposisi kausalitas bernada positif yang TEPAT di depan kata benda maskulin 'le soutien' adalah...",
        "correct": "grâce au (kontraksi preposisi kausalitas positif grâce à + le soutien yang bermakna 'berkat dukungan').",
        "distractors": [
            "à cause du (preposisi kausalitas bernada negatif yang bermakna 'gara-gara/karena akibat buruk').",
            "parce que (konjungsi subordinatif yang menuntut klausula lengkap dengan subjek dan kata kerja, bukan frasa nominal).",
            "faute de (preposisi yang bermakna 'akibat ketiadaan/kekurangan suatu hal').",
            "en raison à (konstruksi rancu yang mencampuradukkan en raison de dengan preposisi à)."
        ],
        "formula": {
            "title": "EXPRESSION DE LA CAUSE: GRÂCE À VS À CAUSE DE",
            "latex": "\\mathbf{grâce \\text{ } à} + \\text{Nom (cause positive)} \\quad \\leftrightarrow \\quad \\mathbf{à \\text{ } cause \\text{ } de} + \\text{Nom (cause négative)}",
            "legend": "• berkat sesuatu yang positif: grâce à + le soutien = grâce au soutien.<br>• gara-gara sesuatu yang negatif: à cause de la pluie."
        },
        "hints": {
            "concept": "Untuk menyatakan penyebab yang bernilai positif atau menguntungkan (berkat bantuan/dukungan), bahasa Prancis menggunakan 'grâce à' (+ kontraksi au di depan kata benda maskulin 'le soutien'). Preposisi 'à cause de' digunakan untuk sebab yang bernuansa negatif (gara-gara).",
            "execution": "Penyebab positif 'le soutien' -> 'grâce à + le = grâce au'."
        }
    },
    {
        "id": "fra-lat-m-22",
        "materi": "GRAMMAIRE: LE COMPARATIF D'INFÉRIORITÉ",
        "topic": "Menyatakan Tingkat Perbandingan Lebih Rendah Menggunakan 'moins ... que'",
        "stem": "Dalam perbandingan gaya hidup perkotaan dan pedesaan:\n'La vie dans un petit village de campagne est généralement beaucoup ( ... ) stressante ( ... ) dans une métropole comme Paris.'\nPasangan kata pembanding yang TEPAT untuk menyatakan derajat perbandingan lebih rendah (kurang menegangkan) adalah...",
        "correct": "moins / que (pola perbandingan derajat lebih rendah 'moins + adjectif + que' yang bermakna 'kurang/lebih sedikit ... daripada').",
        "distractors": [
            "plus / de (kombinasi keliru yang mencampur partikel komparatif keunggulan dengan preposisi de).",
            "aussi / comme (kesalahan memasangkan partikel aussi dengan kata sambung comme alih-alih que).",
            "peu / que (peu adalah adverbia kuantitas, bukan partikel pembentuk komparatif adjektiva).",
            "moins / de (penggunaan de yang keliru karena pembanding kata sifat selalu menggunakan partikel que)."
        ],
        "formula": {
            "title": "LE COMPARATIF D'INFÉRIORITÉ",
            "latex": "\\mathbf{moins} + \\text{Adjectif (stressante)} + \\mathbf{que} \\quad (\\text{kurang menegangkan daripada})",
            "legend": "• Komparatif keunggulan: plus ... que.<br>• Komparatif kesetaraan: aussi ... que.<br>• Komparatif kerendahan: moins ... que."
        },
        "hints": {
            "concept": "Perbandingan tingkat lebih rendah (derajat inferioritas) untuk kata sifat dibentuk dengan rumus: 'moins + adjectif + que' (kurang ... daripada).",
            "execution": "Kurang menegangkan daripada = 'moins stressante que'."
        }
    },
    {
        "id": "fra-lat-m-23",
        "materi": "GRAMMAIRE: LES ADJECTIFS INDÉFINIS (TOUT, TOUTE, TOUS, TOUTES)",
        "topic": "Penyesuaian Bentuk Maskulin Jamak 'tous' di Depan Kata Benda Jamak",
        "stem": "Instruksi panitia ujian sekolah kepada para peserta:\n'Avant de commencer l'épreuve de rédaction, ( ... ) les candidats doivent déposer leurs téléphones portables sur la table du surveillant.'\nBentuk kata sifat tak tentu yang TEPAT di depan kata benda maskulin jamak 'les candidats' adalah...",
        "correct": "tous (bentuk maskulin jamak dari kata sifat tak tentu tout yang diselaraskan dengan les candidats).",
        "distractors": [
            "tout (bentuk maskulin tunggal yang keliru jumlah untuk kata benda jamak).",
            "toute (bentuk feminin tunggal yang keliru gender dan jumlah).",
            "toutes (bentuk feminin jamak yang keliru gender untuk kata benda maskulin candidats).",
            "tout les (kesalahan ejaan bentuk tunggal sebelum artikel jamak les)."
        ],
        "formula": {
            "title": "LES FORMES DE 'TOUT' (ADJECTIF)",
            "latex": "\\text{Masculin Singulier: tout} \\quad | \\quad \\text{Féminin Singulier: toute} \\quad | \\quad \\mathbf{Masculin Pluriel: tous} \\quad | \\quad \\text{Féminin Pluriel: toutes}",
            "legend": "• les candidats = maskulin jamak $\\rightarrow$ 'tous les candidats'.<br>• Bila berfungsi sebagai adjektiva penentu, huruf 's' pada 'tous' TIDAK dilafalkan (/tu/)."
        },
        "hints": {
            "concept": "Kata sifat 'tout' memiliki empat bentuk penyesuaian: tout (maskulin tunggal), toute (feminin tunggal), tous (maskulin jamak), toutes (feminin jamak). 'Les candidats' adalah maskulin jamak, sehingga bentuk yang benar adalah 'tous'.",
            "execution": "maskulin jamak 'les candidats' -> 'tous les candidats'."
        }
    },
    {
        "id": "fra-lat-m-24",
        "materi": "GRAMMAIRE: LE PASSÉ RÉCENT (VENIR DE + INFINITIF)",
        "topic": "Menyatakan Aksi yang Baru Saja Terjadi dengan 'venir de'",
        "stem": "Seorang resepsionis menyambut tamu yang baru tiba:\n'Vous arrivez au bon moment! Le directeur ( ... ) d'entrer dans la salle de conférence il y a deux minutes.'\nBentuk konjugasi kata kerja 'venir' pada kala Présent yang TEPAT untuk membentuk Passé Récent dengan subjek 'le directeur' adalah...",
        "correct": "vient (konjugasi kata kerja venir persona ketiga tunggal il untuk rumus Passé Récent 'venir de + infinitif').",
        "distractors": [
            "viens (konjugasi persona tunggal je/tu).",
            "venait (bentuk Imparfait yang menggeser konteks waktu lampau baru saja menjadi lampau lampau).",
            "va (verba aller yang membentuk Futur Proche, bertolak belakang dengan makna il y a deux minutes).",
            "viennent (bentuk jamak ils/elles yang keliru jumlah untuk subjek tunggal le directeur)."
        ],
        "formula": {
            "title": "LE PASSÉ RÉCENT: VENIR DE + INFINITIF",
            "latex": "\\text{Sujet (il)} + \\mathbf{venir \\text{ (au présent)}} + \\mathbf{de} + \\text{Infinitif} \\quad (\\text{Le directeur } \\mathbf{vient} \\text{ d'entrer})",
            "legend": "• Menyatakan tindakan yang baru saja selesai terjadi beberapa saat lalu.<br>• Disertai penanda waktu 'il y a quelques minutes'."
        },
        "hints": {
            "concept": "Passé Récent (masa lampau yang baru saja terjadi) dibentuk dengan rumus: konjugasi 'venir' pada waktu sekarang (Présent) + de/d' + Infinitif. Subjek 'le directeur' (= il) berpasangan dengan bentuk 'vient'.",
            "execution": "Le directeur + venir de -> 'vient d'entrer'."
        }
    },
    {
        "id": "fra-lat-m-25",
        "materi": "GRAMMAIRE: LES PRONOMS DÉMONSTRATIFS (CELUI, CELLE, CEUX, CELLES)",
        "topic": "Pronomina Demonstratif Maskulin Tunggal 'celui' dengan Frasa Preposisi 'de'",
        "stem": "Dua sahabat membandingkan kualitas laptop kerja:\n'Mon ordinateur portable est très lent, alors que ( ... ) de Thomas est extrêmement rapide et performant.'\nBentuk pronomina penunjuk (Pronom démonstratif) yang TEPAT untuk menggantikan 'l'ordinateur' (maskulin tunggal) adalah...",
        "correct": "celui (pronomina demonstratif maskulin tunggal yang merujuk pada benda l'ordinateur).",
        "distractors": [
            "celle (pronomina demonstratif feminin tunggal yang keliru gender untuk kata maskulin un ordinateur).",
            "ceux (pronomina demonstratif maskulin jamak yang keliru jumlah).",
            "celles (pronomina demonstratif feminin jamak).",
            "ce (kata penunjuk netral yang tidak dapat berdiri sendiri sebelum frasa kepemilikan de Thomas)."
        ],
        "formula": {
            "title": "LES PRONOMS DÉMONSTRATIFS",
            "latex": "\\text{l'ordinateur (Masc. Sing.) de Thomas} \\quad \\rightarrow \\quad \\mathbf{celui} \\text{ de Thomas}",
            "legend": "• Menghindari pengulangan kata benda: celui de (milik/punya si...).<br>• Maskulin tunggal: celui; Feminin tunggal: celle; Maskulin jamak: ceux; Feminin jamak: celles."
        },
        "hints": {
            "concept": "Untuk menghindari pengulangan kata benda maskulin tunggal 'l'ordinateur' yang diikuti frasa kepemilikan 'de Thomas', digunakan pronomina demonstratif 'celui' (celui de Thomas = laptop milik Thomas).",
            "execution": "l'ordinateur (maskulin tunggal) -> ganti dengan 'celui'."
        }
    }
]
