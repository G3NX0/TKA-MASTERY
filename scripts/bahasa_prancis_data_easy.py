# -*- coding: utf-8 -*-
"""
BAHASA PRANCIS - PAKET SOAL LATIHAN MUDAH (EASY) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / CEFR A1-A2 (DELF A1-A2)
Distribusi:
- 8 Butir: Vocabulaire dasar (Salutations, famille, nombres, heure, repas, loisirs, vêtements)
- 10 Butir: Grammaire dasar (Présent indicatif 1er groupe, verbes être/avoir/aller/faire, articles définis/indéfinis/partitifs, négation simple ne...pas, adjectifs possessifs)
- 7 Butir: Situations de communication courante (Se présenter, au restaurant, demander son chemin, chez le médecin)
"""

BAHASA_PRANCIS_EASY_ITEMS = [
    {
        "id": "fra-lat-e-01",
        "materi": "GRAMMAIRE: PRÉSENT DE L'INDICATIF (VERBE ÊTRE)",
        "topic": "Konjugasi Kata Kerja Fundamental 'être' untuk Subjek Persona Kedua Jamak/Formal",
        "stem": "Dalam percakapan formal di kantor kedutaan besar:\n'Bonjour Monsieur et Madame Laurent! ( ... )-vous prêts pour votre entretien de visa ce matin?'\nBentuk konjugasi kata kerja 'être' yang TEPAT untuk subjek 'vous' adalah...",
        "correct": "Êtes (bentuk konjugasi persona kedua jamak/formal dari verba être pada kala Présent).",
        "distractors": [
            "Sommes (bentuk konjugasi persona pertama jamak untuk subjek nous).",
            "Sont (bentuk konjugasi persona ketiga jamak untuk subjek ils/elles).",
            "Avez (konjugasi dari verba avoir yang keliru secara makna predikatif kesiapan diri).",
            "Faites (konjugasi dari verba faire yang bermakna melakukan atau membuat)."
        ],
        "formula": {
            "title": "CONJUGAISON DU VERBE ÊTRE AU PRÉSENT",
            "latex": "\\text{je suis, tu es, il/elle est, nous sommes, } \\mathbf{vous \\text{ } êtes}, \\text{ ils/elles sont}",
            "legend": "• Subjek 'vous' (Anda/Kalian) berpasangan dengan 'êtes'.<br>• Tanda aksen sirkumfleks (ê) wajib disertakan pada ejaan baku."
        },
        "hints": {
            "concept": "Kata kerja 'être' (ada / adalah) adalah verba tidak beraturan esensial. Konjugasi untuk subjek persona 'vous' pada waktu sekarang (Présent) adalah 'êtes'.",
            "execution": "Subjek 'vous' -> bentuk verba 'être' = 'Êtes-vous prêts?'."
        }
    },
    {
        "id": "fra-lat-e-02",
        "materi": "GRAMMAIRE: ARTICLES PARTITIFS (DU, DE LA, DE L', DES)",
        "topic": "Penggunaan Artikel Partitif Maskulin Tunggal untuk Benda yang Tidak Dapat Dihitung",
        "stem": "Seorang pembeli memesan sarapan di sebuah bistro di Paris:\n'Le matin, j'aime boire une tasse de thé et manger du pain avec ( ... ) beurre frais.'\nArtikel partitif yang TEPAT untuk melengkapi kata benda maskulin yang tidak dapat dihitung 'beurre' (mentega) adalah...",
        "correct": "du (artikel partitif maskulin tunggal yang terbentuk dari kontraksi de + le).",
        "distractors": [
            "de la (artikel partitif untuk kata benda bergender feminin tunggal).",
            "de l' (artikel partitif yang digunakan sebelum kata benda yang diawali vokal atau huruf h muet).",
            "des (artikel partitif jamak yang digunakan untuk kata benda kuantitas jamak).",
            "un (artikel tak tentu yang keliru untuk zat makanan yang dikonsumsi sebagian/tidak dihitung butiran)."
        ],
        "formula": {
            "title": "LES ARTICLES PARTITIFS",
            "latex": "\\text{de} + \\text{le} = \\mathbf{du} \\quad (\\text{masculin singulier: le beurre})",
            "legend": "• Partitif menyatakan sebagian kuantitas tak terhitung dari suatu bahan makanan.<br>• le beurre (maskulin) $\\rightarrow$ du beurre."
        },
        "hints": {
            "concept": "Artikel partitif digunakan untuk menyatakan jumlah makanan atau zat yang tidak dapat dihitung (sebagian kuantitas). 'Beurre' adalah kata benda maskulin (le beurre). Kontraksi 'de + le' menghasilkan 'du'.",
            "execution": "Masculin singulier 'beurre' -> artikel partitif = 'du'."
        }
    },
    {
        "id": "fra-lat-e-03",
        "materi": "GRAMMAIRE: NÉGATION SIMPLE (NE...PAS)",
        "topic": "Elisi Partikel Negasi 'ne' Menjadi 'n'' di Depan Kata Kerja Berawalan Vokal",
        "stem": "Dalam percakapan mengenai preferensi musik:\n'Julien écoute souvent de la musique classique, mais il ( ... ) aime pas du tout le heavy metal.'\nBentuk partikel negasi pertama yang TEPAT di depan kata kerja 'aime' adalah...",
        "correct": "n' (bentuk elisi dari partikel negasi 'ne' yang melebur di depan kata kerja berawalan vokal).",
        "distractors": [
            "ne (bentuk negasi utuh yang salah karena tidak boleh bersanding langsung dengan huruf vokal a).",
            "pas (unsur negasi kedua yang tidak boleh diletakkan mendahului kata kerja utama).",
            "non (kata penyangkal mandiri yang bermakna 'tidak', bukan partikel negasi verba).",
            "ni (kata hubung negasi yang bermakna 'maupun' dalam konstruksi korelatif ni...ni)."
        ],
        "formula": {
            "title": "LA NÉGATION VERBALE: NE...PAS",
            "latex": "\\text{Sujet} + \\mathbf{n'} + \\text{Verbe (voyelle)} + \\mathbf{pas}",
            "legend": "• Pola negasi: ne + verbe + pas.<br>• Di depan huruf vokal (a, e, i, o, u, y) atau 'h muet', 'ne' mengalami elisi menjadi 'n''."
        },
        "hints": {
            "concept": "Dalam bahasa Prancis, kalimat negatif verbal mengapit kata kerja: 'ne + verbe + pas'. Jika kata kerja diawali oleh huruf vokal (seperti verba 'aimer'), 'ne' mengalami elisi (pengguguran huruf e) menjadi 'n''.",
            "execution": "Kata kerja diawali vokal 'aime' -> partikel negasi = 'n''."
        }
    },
    {
        "id": "fra-lat-e-04",
        "materi": "GRAMMAIRE: ADJECTIFS POSSESSIFS",
        "topic": "Kata Sifat Kepemilikan untuk Kata Benda Feminin Berawalan Vokal (mon/ton/son)",
        "stem": "Camille memperkenalkan sahabat dekatnya di sekolah:\n'Voici Sophie, c'est ( ... ) amie d'enfance depuis l'école primaire.'\nKata sifat kepemilikan orang pertama tunggal yang TEPAT di depan kata benda feminin berawalan vokal 'amie' adalah...",
        "correct": "mon (bentuk kepemilikan maskulin yang wajib digunakan di depan kata benda feminin yang berawalan huruf vokal demi eufoni suara).",
        "distractors": [
            "ma (bentuk feminin biasa yang dilarang digunakan di depan huruf vokal karena menyebabkan tabrakan bunyi hiat).",
            "mes (bentuk kepemilikan jamak yang keliru untuk kata benda tunggal amie).",
            "m' (pronomina klitik objek yang tidak berfungsi sebagai penanda kepemilikan adjektiva).",
            "mien (bentuk pronomina kepemilikan mandiri yang membutuhkan artikel penentu le/la)."
        ],
        "formula": {
            "title": "EUPHONIE DES ADJECTIFS POSSESSIFS",
            "latex": "\\text{Nomen feminin berawalan vokal (amie)} \\quad \\implies \\quad \\mathbf{mon / ton / son} \\quad (\\text{BUKAN ma})",
            "legend": "• Menghindari tabrakan bunyi vokal (hiatus): 'ma amie' (SALAH!).<br>• Digantikan oleh bentuk 'mon amie' agar terjadi penghubungan suara (liaison)."
        },
        "hints": {
            "concept": "Meskipun 'amie' adalah kata benda feminin, bahasa Prancis melarang pemakaian 'ma amie' demi menghindari tabrakan bunyi vokal (hiatus). Sebagai gantinya, digunakan bentuk 'mon' (mon amie) agar tercipta bunyi merdu yang menyambung (liaison).",
            "execution": "Feminin diawali vokal = 'mon amie'."
        }
    },
    {
        "id": "fra-lat-e-05",
        "materi": "GRAMMAIRE: PRÉSENT DE L'INDICATIF (VERBES DU 1ER GROUPE)",
        "topic": "Konjugasi Kata Kerja Berakhiran -er untuk Persona Pertama Jamak 'nous'",
        "stem": "Dalam kegiatan kelompok belajar di perpustakaan:\n'Chaque samedi après-midi, nous ( ... ) ensemble pour préparer nos examens de fin d'année.'\nBentuk konjugasi kata kerja 'étudier' yang TEPAT untuk subjek 'nous' pada kala Présent adalah...",
        "correct": "étudions (akhiran teratur -ons untuk persona pertama jamak nous pada kata kerja kelompok pertama).",
        "distractors": [
            "étudiez (akhiran -ez untuk persona kedua jamak vous).",
            "étudient (akhiran -ent untuk persona ketiga jamak ils/elles).",
            "étudie (akhiran -e untuk persona pertama atau ketiga tunggal je/il/elle).",
            "étudier (bentuk dasar infinitif yang belum dikonjugasikan)."
        ],
        "formula": {
            "title": "CONJUGAISON DU 1ER GROUPE (-ER)",
            "latex": "\\text{Radical: étudi-} + \\mathbf{-ons} = \\mathbf{étudions} \\quad (\\text{Sujet: nous})",
            "legend": "• Akhiran Présent verba -er: -e, -es, -e, -ons, -ez, -ent.<br>• Subjek 'nous' selalu berakhiran '-ons'."
        },
        "hints": {
            "concept": "Kata kerja beraturan kelompok 1 (berakhiran -er) seperti 'étudier' dikonjugasikan dengan mencopot '-er' lalu menambahkan akhiran personal. Untuk subjek 'nous', akhirannya selalu '-ons' (étudions).",
            "execution": "nous + étudier -> 'nous étudions'."
        }
    },
    {
        "id": "fra-lat-e-06",
        "materi": "COMMUNICATION: L'HEURE COURANTE",
        "topic": "Menyatakan Waktu Pagi dengan Ungkapan Kurang Seperempat Jam (moins le quart)",
        "stem": "Dua siswa bergegas menuju halte bus. Jam menunjukkan pukul 07:45. Dalam bahasa Prancis ragam lisan sehari-hari, waktu tersebut dinyatakan sebagai...",
        "correct": "Il est huit heures moins le quart. (pukul delapan kurang seperempat jam).",
        "distractors": [
            "Il est sept heures moins le quart. (keliru karena bermakna pukul 06:45).",
            "Il est sept heures et quart. (bermakna pukul 07:15 atau lewat seperempat jam).",
            "Il est huit heures et demie. (bermakna pukul 08:30 atau setengah sembilan).",
            "Il est quarante-cinq minutes après sept heures. (ungkapan terjemahan harfiah yang kaku dan tidak lazim dalam bahasa Prancis)."
        ],
        "formula": {
            "title": "EXPRIMER L'HEURE: MOINS LE QUART",
            "latex": "07:45 = \\text{Il est } [H+1] \\text{ heures } \\mathbf{moins \\text{ } le \\text{ } quart}",
            "legend": "• 07:45 = Jam 8 kurang seperempat (15 menit menuju jam 8).<br>• Menggunakan kata sandang tertentu 'le': moins le quart."
        },
        "hints": {
            "concept": "Dalam bahasa Prancis, waktu menit ke-45 dinyatakan dengan menyebut jam berikutnya ditambah frasa 'moins le quart' (kurang seperempat). Pukul 07:45 berarti jam 8 kurang seperempat: 'Il est huit heures moins le quart'.",
            "execution": "07:45 = 'Il est huit heures moins le quart'."
        }
    },
    {
        "id": "fra-lat-e-07",
        "materi": "GRAMMAIRE: PRÉPOSITIONS DE LIEU DEVANT LES PAYS",
        "topic": "Penggunaan Preposisi 'en' di Depan Nama Negara Bergender Feminin",
        "stem": "Dalam rencana perjalanan wisata liburan musim semi:\n'Pendant les prochaines vacances, Lucas va voyager ( ... ) Italie pour visiter les monuments historiques de Rome.'\nPreposisi tempat yang TEPAT di depan nama negara bergender feminin 'Italie' adalah...",
        "correct": "en (preposisi tempat untuk negara bergender feminin atau negara yang diawali huruf vokal).",
        "distractors": [
            "au (preposisi kontraksi à + le yang digunakan khusus untuk nama negara maskulin berawalan konsonan).",
            "à la (preposisi yang tidak digunakan untuk nama negara berdaulat).",
            "aux (preposisi kontraksi à + les yang digunakan khusus untuk nama negara kepulauan atau bentuk jamak).",
            "dans le (konstruksi preposisi yang keliru untuk konteks pergi ke suatu negara)."
        ],
        "formula": {
            "title": "PRÉPOSITIONS DEVANT LES NOMS DE PAYS",
            "latex": "\\mathbf{en} + \\text{Pays féminin (Italie, France)} \\quad | \\quad \\mathbf{au} + \\text{Pays masculin (Japon, Canada)}",
            "legend": "• Nama negara berakhiran huruf '-e' umumnya bergender feminin (l'Italie).<br>• Ke/di negara feminin: selalu gunakan 'en'."
        },
        "hints": {
            "concept": "Nama negara yang berakhiran huruf '-e' (seperti la France, l'Italie, l'Espagne) bergender feminin. Untuk menyatakan tujuan atau keberadaan di negara feminin, digunakan preposisi 'en'.",
            "execution": "Italie (feminin) -> preposisi = 'en Italie'."
        }
    },
    {
        "id": "fra-lat-e-08",
        "materi": "GRAMMAIRE: LE VERBE ALLER AU PRÉSENT",
        "topic": "Konjugasi Kata Kerja Tidak Beraturan 'aller' untuk Persona Ketiga Jamak 'ils'",
        "stem": "Ibu guru menanyakan keberadaan murid-murid:\n'Où sont les élèves de la classe de français? — Ils ( ... ) au laboratoire de langues pour l'épreuve d'écoute.'\nBentuk konjugasi kata kerja 'aller' yang TEPAT untuk subjek 'ils' pada waktu sekarang adalah...",
        "correct": "vont (bentuk konjugasi persona ketiga jamak dari verba aller pada kala Présent).",
        "distractors": [
            "vas (bentuk konjugasi persona kedua tunggal untuk subjek tu).",
            "va (bentuk konjugasi persona ketiga tunggal untuk subjek il/elle/on).",
            "allons (bentuk konjugasi persona pertama jamak untuk subjek nous).",
            "allez (bentuk konjugasi persona kedua jamak untuk subjek vous)."
        ],
        "formula": {
            "title": "CONJUGAISON DU VERBE ALLER AU PRÉSENT",
            "latex": "\\text{je vais, tu vas, il va, nous allons, vous allez, } \\mathbf{ils/elles \\text{ } vont}",
            "legend": "• Verba tidak beraturan kelompok 3.<br>• Bentuk orang ketiga jamak: vont."
        },
        "hints": {
            "concept": "Kata kerja 'aller' (pergi) adalah verba tidak beraturan. Konjugasinya: je vais, tu vas, il va, nous allons, vous allez, ils vont. Subjeknya adalah 'ils' (mereka), sehingga bentuk yang benar adalah 'vont'.",
            "execution": "Ils + aller -> 'ils vont'."
        }
    },
    {
        "id": "fra-lat-e-09",
        "materi": "COMMUNICATION: COMMANDER AU RESTAURANT",
        "topic": "Mengungkapkan Pesanan Makanan Secara Santun dengan 'je voudrais'",
        "stem": "Di sebuah restoran tradisional di kota Lyon, pelanggan memanggil pelayan:\n'S'il vous plaît, Monsieur! Je ( ... ) un steak-frites bien cuit et une carafe d'eau, s'il vous plaît.'\nBentuk verba modalitas kesantunan yang PALING TEPAT untuk memesan hidangan adalah...",
        "correct": "voudrais (bentuk Conditionnel Présent dari verba vouloir yang digunakan untuk menyatakan permintaan santun).",
        "distractors": [
            "veux (bentuk Présent indikatif yang bernada terlalu kasar dan menuntut dalam etika pelayanan).",
            "voulait (bentuk lampau Imparfait yang tidak sesuai konteks pemesanan langsung saat ini).",
            "voulez (bentuk konjugasi untuk persona vous).",
            "voudra (bentuk Futur Simple orang ketiga tunggal yang bermakna dia akan mau di masa depan)."
        ],
        "formula": {
            "title": "LA DEMANDE POLIE: JE VOUDRAIS",
            "latex": "\\text{Formule de politesse: } \\mathbf{Je \\text{ } voudrais} + \\text{Nom / Infinitif} + \\text{s'il vous plaît}",
            "legend": "• 'Je veux' terkesan arogan/kasar di restoran Prancis.<br>• 'Je voudrais' (Conditionnel) merupakan standar kesantunan baku."
        },
        "hints": {
            "concept": "Dalam etika komunikasi Prancis, memesan makanan menggunakan 'je veux' (saya mau) dianggap tidak sopan/kasar. Standar kesantunan (politesse) yang wajib digunakan adalah 'je voudrais' (saya ingin/mohon).",
            "execution": "Pemesanan santun = 'Je voudrais'."
        }
    },
    {
        "id": "fra-lat-e-10",
        "materi": "GRAMMAIRE: LE FÉMININ DES ADJECTIFS QUALIFICATIFS",
        "topic": "Pembentukan Bentuk Feminin Kata Sifat Berakhiran -eux (-euse)",
        "stem": "Dalam deskripsi kepribadian anggota keluarga:\n'Mon oncle est très généreux avec tout le monde, et ma tante est également très ( ... ).'\nBentuk feminin yang BENAR dari kata sifat 'généreux' untuk mendeskripsikan 'ma tante' adalah...",
        "correct": "généreuse (perubahan akhiran feminin teratur dari kata sifat maskulin -eux menjadi -euse).",
        "distractors": [
            "généreux (bentuk maskulin yang tidak mengalami penyesuaian gender untuk subjek tante).",
            "généreuxe (kesalahan ejaan penambahan huruf e langsung setelah huruf konsonan x).",
            "généreusement (bentuk kata keterangan adverbia yang bermakna 'dengan murah hati').",
            "généreuses (bentuk feminin jamak yang tidak cocok dengan subjek tunggal ma tante)."
        ],
        "formula": {
            "title": "FÉMININ DES ADJECTIFS EN -EUX",
            "latex": "\\text{Masculin: -eux} \\quad \\rightarrow \\quad \\text{Féminin: } \\mathbf{-euse}",
            "legend": "• Contoh: généreux $\\rightarrow$ généreuse; heureux $\\rightarrow$ heureuse.<br>• Menyesuaikan dengan gender subjek feminin tunggal (ma tante)."
        },
        "hints": {
            "concept": "Kata sifat yang berakhiran '-eux' pada bentuk maskulin tunggal berubah menjadi '-euse' pada bentuk feminin tunggal (généreux -> généreuse, heureux -> heureuse).",
            "execution": "généreux -> bentuk feminin untuk ma tante = 'généreuse'."
        }
    },
    {
        "id": "fra-lat-e-11",
        "materi": "GRAMMAIRE: L'INTERROGATION (MOTS INTERROGATIFS)",
        "topic": "Kata Tanya Alasan Kausalitas 'Pourquoi' dan Jawabannya 'Parce que'",
        "stem": "Seorang guru menanyakan alasan keterlambatan siswa:\n'— ( ... ) es-tu en retard ce matin, Thomas? — Parce que mon réveil n'a pas sonné, Madame.'\nKata tanya yang TEPAT untuk menanyakan alasan atau penyebab keterlambatan adalah...",
        "correct": "Pourquoi (kata tanya interogatif yang menanyakan sebab/alasan dan berpasangan dengan parce que).",
        "distractors": [
            "Comment (kata tanya yang menanyakan cara, sarana, atau kondisi keadaan).",
            "Où (kata tanya yang menanyakan lokasi atau arah tempat berada).",
            "Quand (kata tanya yang menanyakan keterangan waktu kejadian).",
            "Combien (kata tanya yang menanyakan jumlah kuantitas atau harga)."
        ],
        "formula": {
            "title": "L'INTERROGATION CAUSALE",
            "latex": "\\mathbf{Pourquoi} \\dots ? \\quad \\leftrightarrow \\quad \\mathbf{Parce \\text{ } que} \\dots",
            "legend": "• Menanyakan penyebab/alasan: selalu gunakan 'Pourquoi'.<br>• Jawaban kausalitas dimulai dengan 'Parce que' (karena)."
        },
        "hints": {
            "concept": "Kata tanya untuk menanyakan sebab atau alasan (mengapa) dalam bahasa Prancis adalah 'Pourquoi'. Indikator kuatnya adalah jawaban siswa yang diawali dengan 'Parce que' (karena).",
            "execution": "Pertanyaan alasan kausalitas = 'Pourquoi'."
        }
    },
    {
        "id": "fra-lat-e-12",
        "materi": "GRAMMAIRE: LE PLURIEL DES NOMS EN -AL",
        "topic": "Pembentukan Bentuk Jamak Khusus Kata Benda Berakhiran -al (-aux)",
        "stem": "Di kebun binatang kota Marseille:\n'Pendant notre visite guidée, nous avons pu observer plusieurs ( ... ) sauvages venus d'Afrique.'\nBentuk jamak (Pluriel) yang BENAR dari kata benda 'un animal' adalah...",
        "correct": "animaux (bentuk jamak tidak beraturan kata benda berakhiran -al yang berubah menjadi -aux).",
        "distractors": [
            "animals (kesalahan penambahan huruf s langsung seperti pola bahasa Inggris).",
            "animales (kesalahan pembentukan bentuk jamak feminin tiruan).",
            "animalses (bentuk hiperkoreksi ganda yang tidak dikenal dalam morfologi bahasa Prancis).",
            "animau (kesalahan ejaan tanpa huruf konsonan x penanda jamak)."
        ],
        "formula": {
            "title": "PLURIEL DES NOMS EN -AL",
            "latex": "\\text{Singulier: } \\mathbf{-al} \\quad \\rightarrow \\quad \\text{Pluriel: } \\mathbf{-aux}",
            "legend": "• un animal $\\rightarrow$ des animaux; un journal $\\rightarrow$ des journaux.<br>• Perkecualian reguler hanya pada beberapa kata seperti festival, carnaval."
        },
        "hints": {
            "concept": "Kata benda dalam bahasa Prancis yang berakhiran '-al' umumnya membentuk bentuk jamak dengan mengganti akhiran tersebut menjadi '-aux' (un animal -> des animaux, un journal -> des journaux).",
            "execution": "Plural dari 'animal' = 'animaux'."
        }
    },
    {
        "id": "fra-lat-e-13",
        "materi": "GRAMMAIRE: LE VERBE FAIRE AU PRÉSENT",
        "topic": "Konjugasi Kata Kerja 'faire' untuk Subjek Persona Kedua Jamak/Formal 'vous'",
        "stem": "Dalam survei kegiatan waktu luang:\n'Qu'est-ce que vous ( ... ) généralement pendant votre temps libre le week-end?'\nBentuk konjugasi kata kerja 'faire' yang TEPAT untuk subjek 'vous' pada waktu sekarang adalah...",
        "correct": "faites (bentuk konjugasi persona kedua jamak yang khas berakhiran -tes dari verba faire).",
        "distractors": [
            "faisez (kesalahan regularisasi analogis dengan menambahkan akhiran biasa -ez pada akar fais-).",
            "faisons (bentuk konjugasi persona pertama jamak untuk subjek nous).",
            "font (bentuk konjugasi persona ketiga jamak untuk subjek ils/elles).",
            "fais (bentuk konjugasi persona tunggal je/tu)."
        ],
        "formula": {
            "title": "CONJUGAISON DU VERBE FAIRE (VOUS)",
            "latex": "\\text{je fais, tu fais, il fait, nous faisons, } \\mathbf{vous \\text{ } faites}, \\text{ ils font}",
            "legend": "• Tiga verba Prancis yang berakhiran '-tes' pada subjek 'vous': être (êtes), dire (dites), faire (faites).<br>• Bentuk 'faisez' sama sekali TIDAK ADA dalam bahasa Prancis baku."
        },
        "hints": {
            "concept": "Kata kerja 'faire' memiliki konjugasi istimewa untuk subjek 'vous'. Alih-alih berakhiran '-ez', verba ini berakhiran '-tes': 'vous faites'. Ingat tiga serangkai: vous êtes, vous dites, vous faites.",
            "execution": "vous + faire -> 'vous faites'."
        }
    },
    {
        "id": "fra-lat-e-14",
        "materi": "GRAMMAIRE: ARTICLES DÉFINIS CONTRACTÉS (À + ARTICLE)",
        "topic": "Kontraksi Preposisi 'à' dengan Artikel Tentu Maskulin 'le' (au)",
        "stem": "Seorang ayah mengajak anaknya berolahraga di akhir pekan:\n'Dimanche matin, le père emmène son fils ( ... ) parc municipal pour jouer au ballon.'\nBentuk artikel kontraksi yang TEPAT untuk preposisi 'à' dan kata benda maskulin 'le parc' adalah...",
        "correct": "au (kontraksi wajib antara preposisi à dan artikel tentu maskulin le).",
        "distractors": [
            "à le (kesalahan fatal karena bahasa Prancis melarang keras pertemuan langsung à + le tanpa kontraksi).",
            "à la (preposisi untuk kata benda bergender feminin).",
            "aux (kontraksi preposisi untuk kata benda berstatus jamak).",
            "dans (preposisi di dalam ruang tertutup yang tidak sesuai dengan idiom aller au parc)."
        ],
        "formula": {
            "title": "ARTICLES CONTRACTÉS AVEC LA PRÉPOSITION À",
            "latex": "\\mathbf{à} + \\mathbf{le} = \\mathbf{au} \\quad (\\text{masculin singulier: le parc})",
            "legend": "• Kontraksi wajib: à + le = au; à + les = aux.<br>• Bentuk 'à le' dilarang mutlak dalam ortografi Prancis."
        },
        "hints": {
            "concept": "Preposisi 'à' bila bertemu dengan artikel tentu maskulin tunggal 'le' wajib melebur (kontraksi) menjadi 'au'. Kata 'parc' adalah maskulin (le parc), sehingga menjadi 'au parc'.",
            "execution": "à + le parc = 'au parc'."
        }
    },
    {
        "id": "fra-lat-e-15",
        "materi": "COMMUNICATION: CHEZ LE MÉDECIN (LES SENSATIONS)",
        "topic": "Mengungkapkan Rasa Sakit Fisik Menggunakan Struktur 'avoir mal à'",
        "stem": "Pasien mengeluhkan gejala flu berat kepada dokter keluarga:\n'Docteur, j'ai une forte fièvre et j'ai très mal ( ... ) gorge depuis hier soir.'\nBentuk kontraksi preposisi yang TEPAT untuk melengkapi frasa sakit tenggorokan (la gorge, feminin) adalah...",
        "correct": "à la (preposisi à tanpa kontraksi di depan kata benda feminin tunggal: avoir mal à la gorge).",
        "distractors": [
            "au (kontraksi preposisi maskulin yang keliru gender untuk kata benda feminin la gorge).",
            "aux (kontraksi preposisi jamak untuk bagian tubuh berpasangan seperti les yeux).",
            "de la (artikel partitif yang salah struktur karena ungkapan rasa sakit menuntut preposisi à).",
            "dans la (preposisi spasial yang bermakna di dalam organ, bukan idiom klinis rasa sakit)."
        ],
        "formula": {
            "title": "EXPRIMER LA DOULEUR: AVOIR MAL À",
            "latex": "\\mathbf{avoir \\text{ } mal \\text{ } à} + \\text{partie du corps} \\quad (\\text{la gorge } \\rightarrow \\mathbf{à \\text{ } la \\text{ } gorge})",
            "legend": "• Maskulin: au ventre (le ventre).<br>• Feminin: à la tête / à la gorge (la gorge).<br>• Jamak: aux dents (les dents)."
        },
        "hints": {
            "concept": "Struktur idiomatis untuk menyatakan rasa sakit fisik di Prancis adalah 'avoir mal à + bagian tubuh'. Karena 'gorge' (tenggorokan) bergender feminin (la gorge), bentuknya adalah 'à la gorge' (tanpa kontraksi).",
            "execution": "feminin 'la gorge' -> 'avoir mal à la gorge'."
        }
    },
    {
        "id": "fra-lat-e-16",
        "materi": "GRAMMAIRE: LE FUTUR PROCHE (ALLER + INFINITIF)",
        "topic": "Menyatakan Tindakan yang Akan Segera Terjadi di Masa Depan Dekat",
        "stem": "Melihat langit mendung pekat dan suara guntur:\n'Regarde ces gros nuages noirs dans le ciel! Il ( ... ) pleuvoir d'une minute à l'autre.'\nBentuk kata kerja bantu 'aller' pada waktu sekarang yang TEPAT untuk membentuk Futur Proche dengan subjek impersonal 'il' adalah...",
        "correct": "va (konjugasi kata kerja bantu aller untuk persona ketiga tunggal il pada konstruksi Futur Proche).",
        "distractors": [
            "vais (konjugasi persona pertama tunggal untuk subjek je).",
            "vas (konjugasi persona kedua tunggal untuk subjek tu).",
            "allait (bentuk lampau Imparfait yang tidak sesuai dengan prediksi masa depan langsung).",
            "ira (bentuk Futur Simple sintetis yang bukan merupakan struktur analitis Futur Proche)."
        ],
        "formula": {
            "title": "LE FUTUR PROCHE",
            "latex": "\\text{Sujet} + \\mathbf{aller \\text{ (au présent)}} + \\text{Infinitif} \\quad (\\text{Il } \\mathbf{va} \\text{ pleuvoir})",
            "legend": "• Digunakan untuk peristiwa yang akan segera terjadi dalam waktu dekat.<br>• Subjek 'il' $\\rightarrow$ va pleuvoir."
        },
        "hints": {
            "concept": "Kala Futur Proche (waktu yang akan segera terjadi) dibentuk dengan rumus: konjugasi 'aller' pada waktu sekarang (Présent) + kata kerja dasar (Infinitif). Subjeknya adalah 'il' (impersonal), sehingga bentuk konjugasinya adalah 'va'.",
            "execution": "Il + aller -> 'Il va pleuvoir'."
        }
    },
    {
        "id": "fra-lat-e-17",
        "materi": "GRAMMAIRE: PRONOMS PERSONNELS TONIQUES",
        "topic": "Penggunaan Pronomina Tonik Setelah Preposisi 'avec' untuk Persona Pertama Tunggal",
        "stem": "Antoine mengajak temannya belajar kelompok:\n'Est-ce que tu veux venir à la bibliothèque municipale pour réviser avec ( ... ) cet après-midi?'\nBentuk kata ganti penguat (Pronom tonique) yang TEPAT setelah preposisi 'avec' untuk persona pertama tunggal adalah...",
        "correct": "moi (pronomina tonik persona pertama tunggal yang wajib digunakan setelah preposisi).",
        "distractors": [
            "je (pronomina persona subjek yang dilarang berdiri setelah preposisi).",
            "me (pronomina klitik objek langsung/tak langsung yang hanya boleh menempel di depan kata kerja).",
            "mon (kata sifat kepemilikan yang menuntut kata benda di belakangnya).",
            "m' (bentuk elisi objek sebelum huruf vokal yang tidak dapat berdiri sendiri)."
        ],
        "formula": {
            "title": "LES PRONOMS TONIQUES APRÈS PRÉPOSITION",
            "latex": "\\text{Préposition (avec, pour, chez, sans)} + \\mathbf{Pronom \\text{ } tonique \\text{ (moi, toi, lui, elle...)} }",
            "legend": "• Subjek 'je' $\\rightarrow$ tonik: 'moi'.<br>• Dilarang keras: 'avec je' (SALAH!). Yang benar: 'avec moi'."
        },
        "hints": {
            "concept": "Setelah preposisi (seperti avec, pour, chez, sans), bahasa Prancis mewajibkan penggunaan kata ganti penguat/mandiri (Pronom tonique). Untuk persona pertama tunggal ('saya'), bentuk toniknya adalah 'moi'.",
            "execution": "avec + Pronom tonique = 'avec moi'."
        }
    },
    {
        "id": "fra-lat-e-18",
        "materi": "VOCABULAIRE: LES REPAS & LA JOURNÉE",
        "topic": "Nama Jam Makan Siang Tradisional di Prancis",
        "stem": "Dalam jadwal rutinitas kantor di Paris:\n'En France, la plupart des employés font une pause entre 12h30 et 13h30 pour prendre le ( ... ).'\nKata benda yang TEPAT untuk menyebut santap siang dalam budaya kuliner Prancis adalah...",
        "correct": "déjeuner (santap siang hari yang biasa dilakukan antara pukul 12.00 hingga 14.00).",
        "distractors": [
            "petit-déjeuner (santap pagi atau sarapan yang dilakukan saat baru bangun tidur).",
            "dîner (santap malam yang biasa dilakukan keluarga Prancis sekitar pukul 19.30 atau 20.00).",
            "goûter (kudapan manis sore hari sekitar pukul 16.30 yang biasanya dinikmati anak sekolah).",
            "dessert (hidangan penutup manis di akhir sesi makan)."
        ],
        "formula": {
            "title": "LES QUATRE REPAS EN FRANCE",
            "latex": "\\text{Matin: le petit-déjeuner} \\rightarrow \\mathbf{Midi: le \\text{ } déjeuner} \\rightarrow \\text{16h30: le goûter} \\rightarrow \\text{Soir: le dîner}",
            "legend": "• Waktu tengah hari (12h30-13h30) adalah momen santap siang: le déjeuner.<br>• Istirahat makan siang dihargai tinggi dalam budaya kerja Prancis."
        },
        "hints": {
            "concept": "Di Prancis, empat sesi makan utama adalah: petit-déjeuner (sarapan pagi), déjeuner (makan siang tengah hari), goûter (camilan sore), dan dîner (makan malam). Waktu antara 12:30 hingga 13:30 merujuk pada makan siang ('le déjeuner').",
            "execution": "Makan siang jam 12:30 = 'le déjeuner'."
        }
    },
    {
        "id": "fra-lat-e-19",
        "materi": "GRAMMAIRE: LE VERBE PRENDRE AU PRÉSENT",
        "topic": "Konjugasi Kata Kerja Kelompok 3 'prendre' untuk Subjek Persona Ketiga Jamak 'ils'",
        "stem": "Dalam panduan mobilitas siswa komuter:\n'Pour aller au lycée tous les matins, les élèves ( ... ) la ligne 4 du métro à la station Châtelet.'\nBentuk konjugasi kata kerja 'prendre' yang TEPAT untuk subjek jamak 'les élèves' pada waktu sekarang adalah...",
        "correct": "prennent (konjugasi orang ketiga jamak dengan penggandaan huruf konsonan n: ils prennent).",
        "distractors": [
            "prend (bentuk konjugasi persona ketiga tunggal il/elle).",
            "prends (bentuk konjugasi persona pertama dan kedua tunggal je/tu).",
            "prenons (bentuk konjugasi persona pertama jamak nous).",
            "prenez (bentuk konjugasi persona kedua jamak vous)."
        ],
        "formula": {
            "title": "CONJUGAISON DU VERBE PRENDRE (PLURIEL)",
            "latex": "\\text{nous prenons, vous prenez, } \\mathbf{ils/elles \\text{ } prennent}",
            "legend": "• Perhatikan ortografi: pada bentuk orang ketiga jamak (ils/elles), huruf 'n' digandakan (-nnent).<br>• Subjek: les élèves = ils."
        },
        "hints": {
            "concept": "Kata kerja 'prendre' (mengambil / naik kendaraan) pada persona ketiga jamak (ils/elles) mengalami penggandaan konsonan 'n' sebelum akhiran '-ent', sehingga dilafalkan dan ditulis 'prennent'.",
            "execution": "les élèves (ils) -> 'prennent'."
        }
    },
    {
        "id": "fra-lat-e-20",
        "materi": "GRAMMAIRE: L'ACCORD DE L'ADJECTIF QUALIFICATIF",
        "topic": "Penyesuaian Gender dan Jumlah Kata Sifat Warna untuk Benda Feminin Jamak",
        "stem": "Di etalase butik busana wanita:\n'Sarah regarde les nouvelles robes ( ... ) exposées dans la vitrine du magasin.'\nBentuk kata sifat warna 'bleu' yang TEPAT untuk menyelaraskan dengan kata benda feminin jamak 'les robes' adalah...",
        "correct": "bleues (penyesuaian bentuk feminin jamak dengan penambahan akhiran -e untuk feminin dan -s untuk jamak).",
        "distractors": [
            "bleu (bentuk maskulin tunggal dasar tanpa penyesuaian gender maupun nomor).",
            "bleus (bentuk maskulin jamak yang melupakan penanda gender feminin).",
            "bleue (bentuk feminin tunggal yang melupakan penanda jumlah jamak).",
            "bleueux (akhiran buatan yang keliru secara morfologi kata sifat warna)."
        ],
        "formula": {
            "title": "ACCORD DE L'ADJECTIF QUALIFICATIF",
            "latex": "\\text{la robe (Fém. Sing.) } \\rightarrow \\text{les robes (Fém. Plur.) } \\implies \\text{bleu} + \\mathbf{e} + \\mathbf{s} = \\mathbf{bleues}",
            "legend": "• Kata sifat menyelaraskan gender (maskulin/feminin) dan jumlah (tunggal/jamak) dengan kata benda.<br>• Feminin = +e, Jamak = +s."
        },
        "hints": {
            "concept": "Kata sifat dalam bahasa Prancis harus menyelaraskan gender dan jumlah dengan kata benda yang disifatinya. Kata benda 'les robes' adalah feminin jamak (féminin pluriel). Maka kata sifat 'bleu' ditambah '-e' (feminin) dan '-s' (jamak) menjadi 'bleues'.",
            "execution": "les robes + bleu -> 'bleues'."
        }
    },
    {
        "id": "fra-lat-e-21",
        "materi": "COMMUNICATION: DEMANDER SON CHEMIN",
        "topic": "Bertanya Arah Lokasi Stasiun Kereta Api Secara Sopan",
        "stem": "Seorang turis asing menyapa warga lokal di trotoar jalan:\n'Pardon Madame, ( ... ) pour aller à la gare centrale, s'il vous plaît?'\nUngkapan interogatif yang PALING LAZIM dan santun untuk menanyakan arah jalan adalah...",
        "correct": "comment faire (ungkapan praktis 'comment faire pour aller à...' yang bermakna bagaimana caranya menuju ke suatu tempat).",
        "distractors": [
            "pourquoi aller (menanyakan alasan filosofis mengapa harus pergi ke stasiun).",
            "combien coûte (menanyakan nominal harga tiket, bukan arah jalan fisik).",
            "quand partir (menanyakan jadwal waktu keberangkatan kereta).",
            "qui est (menanyakan identitas orang, bukan rute lokasi fasilitas kota)."
        ],
        "formula": {
            "title": "DEMANDER SON CHEMIN",
            "latex": "\\text{Formule: } \\mathbf{Comment \\text{ } faire \\text{ } pour \\text{ } aller \\text{ } à} + \\text{Lieu}?",
            "legend": "• Ungkapan baku menanyakan rute/jalan ke lokasi.<br>• Alternatif: 'Où se trouve la gare, s'il vous plaît?'"
        },
        "hints": {
            "concept": "Untuk menanyakan arah jalan atau rute ke suatu tempat, ungkapan standar bahasa Prancis adalah 'Comment faire pour aller à ... ?' (Bagaimana cara menuju ke ... ?) atau 'Pourriez-vous m'indiquer le chemin pour aller à ... ?'.",
            "execution": "Menanyakan rute jalan = 'comment faire pour aller à...'."
        }
    },
    {
        "id": "fra-lat-e-22",
        "materi": "GRAMMAIRE: LES ADJECTIFS DÉMONSTRATIFS (CE, CET, CETTE, CES)",
        "topic": "Penggunaan Demonstratif Maskulin Tunggal di Depan Vokal 'cet'",
        "stem": "Di resepsionis hotel berbintang:\n'Nous avons réservé une chambre double dans ( ... ) hôtel moderne pour trois nuits.'\nKata sifat penunjuk (Adjectif démonstratif) yang TEPAT di depan kata benda maskulin tunggal berawalan huruf 'h muet' 'hôtel' adalah...",
        "correct": "cet (kata penunjuk maskulin tunggal yang wajib digunakan di depan kata berawalan vokal atau h muet).",
        "distractors": [
            "ce (bentuk maskulin tunggal yang hanya boleh digunakan di depan konsonan).",
            "cette (bentuk penunjuk untuk kata benda bergender feminin tunggal).",
            "ces (bentuk penunjuk jamak untuk semua gender).",
            "c' (pronomina demonstratif netral yang hanya menempel pada verba être)."
        ],
        "formula": {
            "title": "LES ADJECTIFS DÉMONSTRATIFS",
            "latex": "\\mathbf{cet} + \\text{Nomen maskulin berawalan vokal / h muet (hôtel, homme, arbre)}",
            "legend": "• Maskulin konsonan: ce livre.<br>• Maskulin vokal/h: cet hôtel (menghindari tabrakan vokal: 'ce hôtel' SALAH!).<br>• Feminin: cette ville."
        },
        "hints": {
            "concept": "Kata benda maskulin tunggal yang diawali oleh huruf vokal atau 'h muet' (seperti l'hôtel, maskulin) menggunakan kata sifat demonstratif khusus 'cet' (bukan 'ce'), agar terjadi penyambungan bunyi (liaison: cet-hôtel).",
            "execution": "Maskulin berawalan h muet 'hôtel' -> 'cet hôtel'."
        }
    },
    {
        "id": "fra-lat-e-23",
        "materi": "GRAMMAIRE: LE VERBE VENIR AU PRÉSENT",
        "topic": "Konjugasi Kata Kerja 'venir' untuk Persona Pertama Tunggal 'je'",
        "stem": "Dalam perkenalan asal-usul kedaerahan:\n'Bonjour à tous! Je m'appelle Maxime et je ( ... ) de Bordeaux dans le sud-ouest de la France.'\nBentuk konjugasi kata kerja 'venir' yang TEPAT untuk subjek 'je' pada waktu sekarang adalah...",
        "correct": "viens (bentuk konjugasi persona pertama tunggal dari verba kelompok ketiga venir).",
        "distractors": [
            "vient (bentuk konjugasi persona ketiga tunggal untuk subjek il/elle).",
            "venons (bentuk konjugasi persona pertama jamak untuk subjek nous).",
            "venez (bentuk konjugasi persona kedua jamak untuk subjek vous).",
            "viennent (bentuk konjugasi persona ketiga jamak untuk subjek ils/elles)."
        ],
        "formula": {
            "title": "CONJUGAISON DU VERBE VENIR AU PRÉSENT",
            "latex": "\\mathbf{je \\text{ } viens}, \\text{ tu viens, il vient, nous venons, vous venez, ils viennent}",
            "legend": "• Persona pertama tunggal: berakhiran huruf '-s' (viens).<br>• Digunakan bersama preposisi 'de' untuk menyatakan asal kedaerahan."
        },
        "hints": {
            "concept": "Konjugasi waktu sekarang (Présent) dari kata kerja tidak beraturan 'venir' (datang/berasal): je viens, tu viens, il vient, nous venons, vous venez, ils viennent. Untuk persona 'je', bentuknya adalah 'viens'.",
            "execution": "je + venir -> 'je viens'."
        }
    },
    {
        "id": "fra-lat-e-24",
        "materi": "GRAMMAIRE: LES NOMBRES ORDINAUX",
        "topic": "Penulisan Angka Tingkat Pertama Feminin 'première'",
        "stem": "Di koridor sekolah hari pertama semester baru:\n'La salle de cours de chimie se trouve à la ( ... ) porte à gauche au rez-de-chaussée.'\nBentuk kata bilangan tingkat (Nombre ordinal) yang TEPAT untuk kata benda feminin 'porte' adalah...",
        "correct": "première (bentuk feminin tunggal dari bilangan ordinal premier).",
        "distractors": [
            "premier (bentuk maskulin tunggal yang keliru gender untuk kata benda feminin la porte).",
            "un (kata bilangan kuantitas kardinal biasa yang tidak menyatakan urutan tingkat).",
            "une (kata bilangan kardinal feminin yang bermakna 'sebuah', bukan urutan pertama).",
            "premièrement (kata keterangan urutan kronologis yang bermakna 'pertama-tama')."
        ],
        "formula": {
            "title": "LES NOMBRES ORDINAUX (GENDER)",
            "latex": "\\text{Masculin: premier} \\quad \\rightarrow \\quad \\text{Féminin: } \\mathbf{première}",
            "legend": "• la porte (feminin tunggal) $\\rightarrow$ la première porte.<br>• Bilangan ordinal tingkat lainnya berakhiran '-ième' yang tidak berubah gender (deuxième, troisième)."
        },
        "hints": {
            "concept": "Bilangan ordinal 'pertama' memiliki perbedaan bentuk gender: 'premier' untuk maskulin dan 'première' untuk feminin. Karena kata bendanya adalah 'la porte' (feminin), maka bentuk yang benar adalah 'première'.",
            "execution": "la + porte (feminin) -> 'la première porte'."
        }
    },
    {
        "id": "fra-lat-e-25",
        "materi": "COMMUNICATION: LA MÉTÉO COURANTE",
        "topic": "Menyatakan Cuaca Hangat/Bagus Menggunakan Konstruksi Impersonal 'il fait'",
        "stem": "Melihat matahari cerah bersinar di pantai Nice:\n'Aujourd'hui, il n'y a aucun vent et ( ... ) très beau, nous pouvons aller nous baigner dans la mer.'\nKonstruksi kata kerja cuaca impersonal yang TEPAT untuk melengkapi kalimat tersebut adalah...",
        "correct": "il fait (konstruksi impersonal baku 'il fait + adjectif' untuk mendeskripsikan cuaca harian di Prancis).",
        "distractors": [
            "il est (kesalahan interferensi harfiah bahasa Inggris 'it is fine' yang tidak sah untuk cuaca dalam bahasa Prancis).",
            "il a (penggunaan verba avoir yang keliru sintaksis deskripsi atmosfer alam).",
            "il ya (kontraksi keliru dari il y a yang bermakna 'ada', bukan penanda cuaca indah).",
            "il donne (verba memberi yang tidak memiliki asosiasi gramatikal dengan suhu cuaca)."
        ],
        "formula": {
            "title": "EXPRIMER LA MÉTÉO AVEC 'FAIRE'",
            "latex": "\\mathbf{Il \\text{ } fait} + \\text{Adjectif de météo (beau, chaud, froid, mauvais)}",
            "legend": "• Bahasa Prancis selalu menggunakan verba 'faire' untuk kondisi cuaca.<br>• Dilarang keras menggunakan 'il est beau' untuk cuaca (SALAH!). Yang benar: 'il fait beau'."
        },
        "hints": {
            "concept": "Dalam bahasa Prancis, keadaan cuaca selalu dinyatakan dengan konstruksi kata kerja impersonal 'il fait + kata sifat cuaca' (contoh: il fait beau, il fait chaud, il fait froid). Menggunakan 'il est beau' untuk cuaca adalah kesalahan fatal.",
            "execution": "Cuaca bagus/cerah = 'il fait très beau'."
        }
    }
]
