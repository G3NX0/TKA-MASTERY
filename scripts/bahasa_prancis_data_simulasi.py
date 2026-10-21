# -*- coding: utf-8 -*-
"""
BAHASA PRANCIS - PAKET SOAL SIMULASI CBT HOTS - 35 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / CEFR A2-B1 (DELF B1 / CBT Format)
Distribusi:
- 25 Butir: Pilihan Ganda Tunggal HOTS (fra-sim-01 .. fra-sim-25)
- 5 Butir: Pilihan Ganda Kompleks / Multi-Select (fra-sim-26 .. fra-sim-30)
- 5 Butir: Matriks Asosiasi Benar-Salah (fra-sim-31 .. fra-sim-35)
"""

BAHASA_PRANCIS_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 SOAL PILIHAN GANDA TUNGGAL (MCQ) HOTS (fra-sim-01 .. fra-sim-25)
    # -------------------------------------------------------------
    {
        "id": "fra-sim-01",
        "materi": "COMPRÉHENSION ÉCRITE: TRANSITION ÉCOLOGIQUE & MOBILITÉS DOUCES",
        "topic": "Analisis Kebijakan Jalur Sepeda dan Pengurangan Polusi Emisi di Kota Paris",
        "stem": "Bacalah wacana kebijakan transportasi perkotaan berikut:\n'Face à l'urgence climatique et à la dégradation de la qualité de l'air métropolitain, la ville de Paris a mis en œuvre le plan «Vélo 2021–2026». Ce projet ambitieux consacre plus de 250 millions d'euros à la création de pistes cyclables sécurisées et continues, connectant le centre-ville aux banlieues périphériques. En réduisant drastiquement l'espace alloué à l'automobile individuelle au profit des mobilités douces et des transports collectifs, la municipalité vise non seulement une diminution substantielle des émissions de gaz à effet de serre, mais aussi une amélioration directe de la santé publique des résidents par la pratique d'une activité physique quotidienne.'\nBerdasarkan wacana di atas, sasaran strategis ganda dari rencana 'Vélo 2021–2026' di Paris adalah...",
        "correct": "Mengurangi emisi gas rumah kaca perkotaan sekaligus meningkatkan derajat kesehatan masyarakat melalui sarana mobilitas aktif yang aman.",
        "distractors": [
            "Menghapus seluruh jaringan transportasi kereta bawah tanah demi memaksa warga membeli sepeda motor pribadi.",
            "Meningkatkan penjualan kendaraan berbahan bakar solar dengan membangun jalan tol layang di pusat kota Paris.",
            "Melarang penggunaan sepeda di jalan umum agar seluruh masyarakat hanya berjalan kaki ke tempat kerja.",
            "Memberikan subsidi bahan bakar minyak secara gratis kepada pemilik mobil mewah di kawasan pinggiran."
        ],
        "formula": {
            "title": "LES MOBILITÉS DOUCES ET L'URBANISME DURABLE",
            "latex": "\\text{Plan Vélo} \\implies \\text{Pistes cyclables sécurisées} \\rightarrow \\mathbf{\\Delta \\text{Émissions } CO_2 \\downarrow} + \\mathbf{\\Delta \\text{Santé publique } \\uparrow}",
            "legend": "• Mengalihkan ruang jalan mobil ke moda transportasi ramah lingkungan (mobilités douces).<br>• Sasaran terpadu: penurunan emisi karbon & peningkatan kesehatan masyarakat."
        },
        "hints": {
            "concept": "Teks secara eksplisit menyatakan target ganda: 'vise non seulement une diminution substantielle des émissions de gaz à effet de serre, mais aussi une amélioration directe de la santé publique des résidents par la pratique d'une activité physique'.",
            "execution": "Pilihan yang menyebutkan pengurangan gas rumah kaca dan peningkatan kesehatan publik."
        }
    },
    {
        "id": "fra-sim-02",
        "materi": "GRAMMAIRE: L'ACCORD DU PARTICIPE PASSÉ AVEC LE PRONOM RELATIF 'QUE'",
        "topic": "Penyesuaian Participe Passé dengan Anteseden Feminin Jamak yang Mendahului",
        "stem": "Dalam ulasan kuratorial pameran busana haute couture di Paris:\n'Les magnifiques créations de haute couture que la modéliste talentueuse a ( ... ) lors du défilé ont émerveillé le public international.'\nBentuk Participe Passé dari kata kerja 'présenter' yang TEPAT untuk menyelaraskan dengan anteseden 'les créations' (feminin jamak) adalah...",
        "correct": "présentées (Participe Passé yang wajib diberi akhiran feminin jamak -es karena pronomina relatif COD 'que' merujuk pada anteseden les créations yang mendahului kata kerja bantu avoir).",
        "distractors": [
            "présenté (bentuk maskulin tunggal tanpa accord yang keliru karena mengabaikan posisi COD sebelum verba).",
            "présentée (bentuk feminin tunggal yang melupakan penanda kuantitas jamak créations).",
            "présentés (bentuk maskulin jamak yang salah gender untuk kata benda feminin une création).",
            "présentaient (bentuk Imparfait yang merusak konstruksi waktu majemuk Passé Composé a présenté)."
        ],
        "formula": {
            "title": "ACCORD AVEC LE PRONOM RELATIF 'QUE' (COD ANTÉCÉDENT)",
            "latex": "\\text{Antécédent: } \\mathbf{les \\text{ } créations} \\text{ (Fém. Plur.)} + \\mathbf{que} + \\text{a } \\mathbf{présentées}",
            "legend": "• 'que' bertindak sebagai COD dari kata kerja présenter.<br>• Karena antesedennya mendahului kata kerja bantu avoir, Participe Passé WAJIB bersepakat dengannya (+es)."
        },
        "hints": {
            "concept": "Bila kata kerja bantu adalah 'avoir' dan didahului oleh pronomina relatif 'que', Participe Passé harus bersepakat (accord) dengan anteseden yang dirujuk oleh 'que'. Anteseden 'les créations' adalah feminin jamak. Maka 'présenter' menjadi 'présentées'.",
            "execution": "les créations (feminin jamak) + que a... -> 'présentées'."
        }
    },
    {
        "id": "fra-sim-03",
        "materi": "GRAMMAIRE: LE SUBJONCTIF PRÉSENT DU VERBE POUVOIR",
        "topic": "Konjugasi Subjonctif Setelah Ungkapan Harapan Emosional 'souhaiter que'",
        "stem": "Pesan resmi walikota kepada warga pada perayaan tahun baru:\n'La municipalité souhaite de tout cœur que chaque famille ( ... ) profiter des nouvelles installations sportives du quartier.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'pouvoir' untuk persona ketiga tunggal 'chaque famille' adalah...",
        "correct": "puisse (akar tidak beraturan puiss- + akhiran Subjonctif persona ketiga tunggal -e).",
        "distractors": [
            "peut (bentuk Présent de l'indicatif yang salah modus karena verba kehendak/harapan souhaiter que menuntut subjonctif).",
            "pourra (bentuk Futur Simple indikatif yang salah modus).",
            "pourrait (bentuk Conditionnel Présent yang tidak sesuai fungsi klausula subordinat keinginan).",
            "puissent (bentuk Subjonctif persona jamak yang keliru jumlah untuk subjek tunggal chaque famille)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DE SOUHAIT: POUVOIR",
            "latex": "\\text{souhaiter que (volonté/souhait)} \\quad \\implies \\quad \\text{qu'elle } \\mathbf{puisse} \\quad (\\text{radical: puiss-})",
            "legend": "• Verba harapan/keinginan mewajibkan Subjonctif.<br>• chaque famille = elle $\\rightarrow$ puisse."
        },
        "hints": {
            "concept": "Kata kerja keinginan/harapan 'souhaiter que' (berharap agar) mewajibkan pemakaian modus Subjonctif. Subjek 'chaque famille' bernilai tunggal (elle). Bentuk Subjonctif verba 'pouvoir' untuk orang ketiga tunggal adalah 'puisse'.",
            "execution": "souhaiter que + chaque famille + pouvoir -> 'puisse'."
        }
    },
    {
        "id": "fra-sim-04",
        "materi": "COMPRÉHENSION ÉCRITE: LE SYSTÈME DE SANTÉ ET LA SÉCURITÉ SOCIALE",
        "topic": "Prinsip Solidaritas Nasional Asuransi Kesehatan Semesta di Prancis (Carte Vitale)",
        "stem": "Bacalah wacana sosial kenegaraan Prancis berikut:\n'Créée en 1945 au lendemain de la Seconde Guerre mondiale, la Sécurité sociale française repose sur un principe fondateur de solidarité nationale: «chacun cotise selon ses moyens et reçoit selon ses besoins». Grâce à ce mécanisme universel, financé par les cotisations patronales et salariales ainsi que par l'impôt, tout résident sur le territoire national bénéficie d'une couverture médicale de base. Matérialisée par la «Carte Vitale», cette prise en charge garantit l'accès aux soins hospitaliers, aux consultations médicales et aux médicaments essentiels, prévenant ainsi l'exclusion sanitaire des populations les plus vulnérables.'\nBerdasarkan wacana di atas, pilar etika utama yang mendasari sistem 'Sécurité sociale' di Prancis adalah...",
        "correct": "Prinsip keadilan sosial di mana setiap individu menyumbang iuran sesuai kemampuan finansialnya dan memperoleh pelayanan kesehatan sesuai kebutuhan medisnya.",
        "distractors": [
            "Kewajiban pasien membayar seluruh biaya pengobatan secara tunai tanpa bantuan pemerintah sedikit pun.",
            "Penolakan pemberian layanan kesehatan bagi masyarakat berpenghasilan rendah dan kelompok lansia.",
            "Penentuan kualitas pengobatan medis yang semata-mata bergantung pada status kepemilikan saham korporat pasien.",
            "Privatisasi penuh seluruh rumah sakit negeri untuk membatasi pengeluaran anggaran kesehatan negara."
        ],
        "formula": {
            "title": "LE MODÈLE SOCIAL FRANÇAIS: LA SÉCURITÉ SOCIALE",
            "latex": "\\text{Solidarité nationale: } \\mathbf{Cotiser \\text{ } selon \\text{ } ses \\text{ } moyens} \\quad \\iff \\quad \\mathbf{Recevoir \\text{ } selon \\text{ } ses \\text{ } besoins}",
            "legend": "• Diciptakan tahun 1945 untuk melindungi seluruh warga dari risiko sakit, kecelakaan, dan hari tua.<br>• Carte Vitale memudahkan klaim pengobatan elektronik secara langsung."
        },
        "hints": {
            "concept": "Wacana secara lugas menegaskan semboyan pilar keadilan sosial: 'chacun cotise selon ses moyens et reçoit selon ses besoins' (setiap orang menyumbang sesuai kemampuannya dan menerima layanan sesuai kebutuhannya).",
            "execution": "Pilihan yang menjelaskan kontribusi berdasar kemampuan dan pelayanan berdasar kebutuhan."
        }
    },
    {
        "id": "fra-sim-05",
        "materi": "GRAMMAIRE: LE CONDITIONNEL D'HYPOTHÈSE (SI + IMPARFAIT)",
        "topic": "Pengandaian Kontrafaktual Sekarang Menggunakan 'Si + Imparfait -> Conditionnel Présent'",
        "stem": "Dalam diskusi tentang perencanaan karier internasional:\n'Si Thomas ( ... ) couramment trois langues vivantes, les recruteurs lui ( ... ) immédiatement ce poste de responsable commercial pour l'Europe du Nord.'\nPasangan bentuk konjugasi kata kerja yang TEPAT untuk pengandaian kontrafaktual saat ini adalah...",
        "correct": "parlait / offriraient (anak kalimat si dengan Imparfait 'parlait' dan induk kalimat akibat dengan Conditionnel Présent 'offriraient').",
        "distractors": [
            "parle / offriront (pengandaian realitas masa depan nyata dengan Présent dan Futur Simple).",
            "parlerait / offraient (urutan terbalik yang dilarang mutlak karena menempatkan Conditionnel di dalam anak kalimat si).",
            "avait parlé / auraient offert (pengandaian kontrafaktual masa lampau Irréel du passé).",
            "parlerait / offriraient (kesalahan penggunaan Conditionnel ganda pada kedua klausula)."
        ],
        "formula": {
            "title": "L'IRRÉEL DU PRÉSENT: SI + IMPARFAIT",
            "latex": "\\mathbf{Si} + \\text{Thomas } \\mathbf{parlait} \\text{ (Imparfait)}, \\quad \\text{les recruteurs } \\mathbf{offriraient} \\text{ (Conditionnel)}",
            "legend": "• Subjek anak kalimat: Thomas (il) $\\rightarrow$ parlait.<br>• Subjek induk kalimat: les recruteurs (ils) $\\rightarrow$ offriraient.<br>• DILARANG keras: 'Si Thomas parlerait' (SALAH!)."
        },
        "hints": {
            "concept": "Pola baku pengandaian masa kini yang bertentangan dengan kenyataan (Irréel du présent) adalah: 'Si + Imparfait, ... Conditionnel Présent'. Subjek 'Thomas' (il) -> parlait; subjek 'les recruteurs' (ils) -> offriraient.",
            "execution": "Si + Imparfait (parlait) -> Conditionnel Présent (offriraient)."
        }
    },
    {
        "id": "fra-sim-06",
        "materi": "GRAMMAIRE: DOUBLE PRONOMS COMPLÉMENTS DEVANT LE VERBE",
        "topic": "Urutan Pronomina Objek Persona Pertama/Kedua Mendahului Objek Persona Ketiga (me les)",
        "stem": "Seorang fotografer meminta kembali berkas foto aslinya:\n'As-tu retrouvé les photos argentiques de notre voyage à Lyon? — Oui, je ( ... ) envoie par courrier postal dès demain matin.'\nKombinasi dua pronomina komplemen (COI orang pertama tunggal 'à toi' dan COD benda jamak 'les photos') yang TEPAT di depan kata kerja adalah...",
        "correct": "te les (urutan baku pronomina: pronomina orang pertama/kedua 'te' mendahului pronomina COD persona ketiga 'les').",
        "distractors": [
            "les te (urutan terbalik yang melanggar hukum urutan pronomina klitik bahasa Prancis).",
            "les lui (kesalahan merujuk pada orang ketiga padahal pembicara sedang berdialog langsung dengan lawan bicara te).",
            "t'en (penggunaan pronomina partitif en yang keliru untuk objek spesifik definit les photos argentiques).",
            "te leur (kesalahan mencampuradukkan dua pronomina COI orang sekaligus)."
        ],
        "formula": {
            "title": "L'ORDRE DES PRONOMS: 1RE/2E PERSONNE DEVANT 3E PERSONNE",
            "latex": "\\mathbf{me / te / se / nous / vous} \\quad \\rightarrow \\quad \\mathbf{le / la / les} \\quad \\rightarrow \\quad \\text{lui / leur} \\quad \\rightarrow \\quad \\text{y} \\quad \\rightarrow \\quad \\text{en}",
            "legend": "• Lawan bicara (te) berada di urutan PERTAMA.<br>• Objek langsung (les photos = les) berada di urutan KEDUA.<br>• Hasil: je TE LES envoie."
        },
        "hints": {
            "concept": "Tabel urutan pronomina di depan kata kerja menetapkan bahwa pronomina persona 1 & 2 (me, te, nous, vous) SELALU diletakkan mendahului pronomina COD persona 3 (le, la, les). Karena ditujukan kepada lawan bicara 'kamu' (te) dan bendanya adalah 'les photos' (les), urutannya adalah 'te les'.",
            "execution": "te (COI persona 2) + les (COD jamak) = 'te les'."
        }
    },
    {
        "id": "fra-sim-07",
        "materi": "GRAMMAIRE: LE SUBJONCTIF APRÈS 'BIEN QUE' (CONCESSION)",
        "topic": "Penggunaan Subjonctif dari Kata Kerja 'avoir' Setelah Konjungsi 'bien que'",
        "stem": "Dalam evaluasi kinerja atlet maraton:\n'Bien que les coureurs ( ... ) une fatigue musculaire intense après quarante kilomètres d'effort, ils ont réussi à franchir la ligne d'arrivée.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'avoir' untuk subjek jamak 'les coureurs' adalah...",
        "correct": "aient (bentuk Subjonctif Présent persona ketiga jamak yang dituntut oleh konjungsi konsesif bien que).",
        "distractors": [
            "ont (bentuk Présent de l'indicatif yang salah modus setelah konjungsi subordinatif bien que).",
            "avaient (bentuk Imparfait indikatif yang salah modus).",
            "auront (bentuk Futur Simple indikatif yang salah modus).",
            "aies (bentuk Subjonctif untuk persona kedua tunggal tu)."
        ],
        "formula": {
            "title": "BIEN QUE + SUBJONCTIF (VERBE AVOIR)",
            "latex": "\\mathbf{Bien \\text{ } que} + \\text{Subjonctif: } \\text{les coureurs (ils) } \\implies \\mathbf{aient}",
            "legend": "• Konjungsi 'bien que' tidak pernah boleh diikuti oleh Indikatif.<br>• ils $\\rightarrow$ qu'ils aient."
        },
        "hints": {
            "concept": "Konjungsi konsesif 'bien que' (meskipun/walaupun) wajib diikuti oleh modus Subjonctif. Subjek klausa ini adalah 'les coureurs' (= ils). Bentuk Subjonctif dari kata kerja 'avoir' untuk 'ils' adalah 'aient' (qu'ils aient).",
            "execution": "bien que + ils (les coureurs) + avoir -> 'aient'."
        }
    },
    {
        "id": "fra-sim-08",
        "materi": "COMPRÉHENSION ÉCRITE: LE PATRIMOINE LITTÉRAIRE ET CULTUREL",
        "topic": "Analisis Nilai Humanisme dalam Karya Klasik Victor Hugo (Les Misérables)",
        "stem": "Bacalah ulasan sastra Prancis berikut:\n'Publié en 1862, le monument romanesque de Victor Hugo, «Les Misérables», dépasse largement le simple cadre de la fiction pour s'ériger en un vibrant plaidoyer social et humaniste. À travers l'itinéraire rédempteur de Jean Valjean et le calvaire de Fantine, Hugo dissèque avec une acuité poignante les ravages de la misère, l'injustice d'une législation aveugle et la cruauté des préjugés bourgeois. Selon l'auteur, l'élévation morale, l'éducation universelle et la compassion rédemptrice constituent les seuls véritables remèdes capables de dissiper les ténèbres de l'ignorance et de réhabiliter la dignité inaliénable de l'être humain.'\nBerdasarkan wacana di atas, pesan etis sentral yang disampaikan Victor Hugo melalui karyanya adalah...",
        "correct": "Pembelaan kemanusiaan yang menegaskan bahwa pendidikan universal, kasih sayang, dan pengampunan moral adalah solusi sejati untuk memulihkan martabat manusia dari belenggu kemiskinan.",
        "distractors": [
            "Pemberian hukuman mati tanpa pengadilan bagi siapa pun warga miskin yang mencuri sepotong roti.",
            "Penolakan terhadap pendidikan bagi rakyat jelata demi menjaga privilese kaum bangsawan kaya raya.",
            "Dukungan terhadap sistem peradilan yang kaku dan kejam untuk menghukum mantan narapidana seumur hidup.",
            "Penghapusan seluruh karya sastra romantis demi memusatkan perhatian pada transaksi komersial perbankan."
        ],
        "formula": {
            "title": "L'ENGAGEMENT HUMANISTE DE VICTOR HUGO",
            "latex": "\\text{Les Misérables (1862)} \\implies \\text{Plaidoyer social: } \\mathbf{Éducation \\text{ } universelle} + \\mathbf{Compassion} + \\mathbf{Dignité \\text{ } humaine}",
            "legend": "• Hugo menggunakan sastra sebagai senjata melawan ketidakadilan sosial dan kemiskinan.<br>• Nilai sentral: Pencerahan melalui pendidikan dan rehabilitasi martabat manusia."
        },
        "hints": {
            "concept": "Wacana menegaskan: 'l'élévation morale, l'éducation universelle et la compassion rédemptrice constituent les seuls véritables remèdes capables de dissiper les ténèbres de l'ignorance et de réhabiliter la dignité inaliénable de l'être humain'.",
            "execution": "Pilihan yang menekankan pendidikan universal, kasih sayang, dan pemulihan martabat manusia."
        }
    },
    {
        "id": "fra-sim-09",
        "materi": "GRAMMAIRE: LE PRONOM RELATIF 'DONT' DANS UNE STRUCTURE COMPLEXE",
        "topic": "Penggunaan 'dont' untuk Menggantikan Frasa Komplemen Adjektiva 'être fier de'",
        "stem": "Seorang rektor universitas memberikan sambutan wisuda:\n'Voici les jeunes chercheurs prometteurs ( ... ) notre établissement académique est immensément fier pour leurs découvertes scientifiques majeures.'\nPronomina relatif yang TEPAT untuk menggantikan komplemen yang terikat dengan ekspresi 'être fier de quelqu'un' adalah...",
        "correct": "dont (pronomina relatif yang menggantikan komplemen yang diperkenalkan oleh preposisi de dalam konstruksi être fier de).",
        "distractors": [
            "que (pronomina relatif COD yang salah karena tidak dapat mengekspresikan preposisi de).",
            "qui (pronomina relatif subjek yang keliru karena klausula subordinat sudah memiliki subjek lengkap notre établissement).",
            "auxquels (pronomina relatif majemuk dengan preposisi à yang keliru valensi karena ekspresi bangga menggunakan preposisi de).",
            "pour qui (frasa preposisional yang redundan dan tidak membentuk struktur sintaksis baku dengan être fier de)."
        ],
        "formula": {
            "title": "LE PRONOM RELATIF DONT AVEC 'ÊTRE FIER DE'",
            "latex": "\\text{être fier } \\mathbf{de} \\text{ ces chercheurs} \\quad \\implies \\quad \\text{les chercheurs } \\mathbf{dont} \\text{ notre établissement est fier}",
            "legend": "• Struktur: être fier DE $\\dots \\rightarrow$ relatif 'dont'.<br>• Begitu pula: avoir besoin DE, avoir envie DE, se souvenir DE."
        },
        "hints": {
            "concept": "Struktur kata sifat 'être fier de' (bangga akan) menuntut preposisi 'de'. Pronomina relatif yang berfungsi menggantikan frasa yang didahului preposisi 'de' adalah 'dont' (les chercheurs dont notre établissement est fier).",
            "execution": "être fier de -> pronomina relatif = 'dont'."
        }
    },
    {
        "id": "fra-sim-10",
        "materi": "GRAMMAIRE: LE SUBJONCTIF DU VERBE PRENDRE",
        "topic": "Konjugasi Subjonctif dari Verba Kelompok 3 'prendre' untuk Subjek 'ils/elles'",
        "stem": "Instruksi dari otoritas kesehatan masyarakat saat gelombang panas musim panas:\n'En période de canicule extrême, il est impératif que les personnes âgées ( ... ) d'abondantes boissons fraîches tout au long de la journée.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'prendre' untuk subjek jamak 'les personnes âgées' (elles) adalah...",
        "correct": "prennent (konjugasi Subjonctif persona ketiga jamak dengan konsonan ganda -nnent yang dituntut oleh frasa il est impératif que).",
        "distractors": [
            "prenent (kesalahan ortografi dengan hanya menulis satu huruf konsonan n).",
            "prennentent (kesalahan redundansi akhiran persona jamak).",
            "prennentions (kesalahan mencampur akhiran jamak -ions dengan bentuk dasar).",
            "prissent (bentuk Subjonctif Imparfait kuno yang tidak lagi digunakan dalam bahasa Prancis modern)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DU VERBE PRENDRE (ILS/ELLES)",
            "latex": "\\text{il est impératif que} \\quad \\implies \\quad \\text{Subjonctif: } \\text{qu'elles } \\mathbf{prennent}",
            "legend": "• Konjugasi Subjonctif verba prendre diturunkan dari akar 'ils prennent' waktu sekarang.<br>• Konsonan 'n' digandakan (-nnent)."
        },
        "hints": {
            "concept": "Frasa impersonal 'il est impératif que' (sangat mendesak bahwa) menuntut modus Subjonctif. Subjonctif orang ketiga jamak dibentuk dari akar waktu sekarang persona 'ils/elles' (ils prennent) + akhiran '-ent' = 'prennent'.",
            "execution": "il est impératif que + elles + prendre -> 'prennent'."
        }
    },
    {
        "id": "fra-sim-11",
        "materi": "GRAMMAIRE: LA VOIX PASSIVE ET LA PRÉPOSITION 'DE' (VERBES DE SENTIMENT)",
        "topic": "Penggunaan Preposisi 'de' Alih-alih 'par' untuk Pelaku Pasif pada Kata Kerja Perasaan/Kekaguman",
        "stem": "Dalam biografi seorang guru teladan di sekolah kejuruan:\n'Grâce à son dévouement exceptionnel et à sa patience inépuisable, ce professeur dévoué est aimé et respecté ( ... ) tous ses élèves.'\nPreposisi pelaku pasif yang PALING TEPAT dan elegan secara gramatika sastra setelah verba perasaan 'aimé et respecté' adalah...",
        "correct": "de (preposisi pelaku pasif yang secara baku digunakan untuk verba keadaan, perasaan, sentimen batin, dan deskripsi moral).",
        "distractors": [
            "par (preposisi pelaku yang lazim untuk tindakan fisik nyata, namun kurang tepat untuk verba perasaan batin aimer/respecter).",
            "avec (preposisi sarana kebersamaan yang salah fungsi sebagai penanda agen pasif).",
            "pour (preposisi tujuan atau alasan yang keliru makna sintaksis).",
            "envers (preposisi sikap perilaku yang tidak berfungsi sebagai pengantar agen dalam konstruksi pasif)."
        ],
        "formula": {
            "title": "VOIX PASSIVE: 'DE' OU 'PAR' POUR L'AGENT?",
            "latex": "\\text{Verbes de sentiment (aimer, respecter, admirer)} + \\text{Passif} \\quad \\implies \\quad \\mathbf{de} + \\text{Agent}",
            "legend": "• Aksi fisik langsung: La souris est mangée PAR le chat.<br>• Perasaan batin & kondisi statis: Il est aimé DE tous; Le mont est couvert DE neige."
        },
        "hints": {
            "concept": "Dalam kalimat pasif, jika kata kerjanya menyatakan perasaan batin, kekaguman, atau kondisi statis (seperti aimer, respecter, admirer, estimer, haïr), preposisi pelaku yang digunakan secara baku dan elegan adalah 'de' (bukan 'par'). Contoh: 'aimé et respecté de tous'.",
            "execution": "Verba perasaan pasif 'aimé et respecté' -> preposisi agen = 'de'."
        }
    },
    {
        "id": "fra-sim-12",
        "materi": "GRAMMAIRE: LE CONDITIONNEL PASSÉ DE L'IRRÉEL DU PASSÉ",
        "topic": "Pengandaian Masa Lampau Kontrafaktual Menggunakan Rumus 'Si + Plus-que-parfait -> Conditionnel Passé'",
        "stem": "Seorang ilmuwan mengomentari keberhasilan pendaratan wahana antariksa:\n'Si nos ingénieurs ( ... ) une infime erreur de calcul de trajectoire, la sonde spatiale ( ... ) sur la surface lunaire sans pouvoir freiner.'\nPasangan bentuk kata kerja yang TEPAT untuk memenuhi kaidah pengandaian kontrafaktual masa lalu adalah...",
        "correct": "avaient commis / se serait écrasée (anak kalimat si dengan Plus-que-parfait 'avaient commis' dan klausula akibat dengan Conditionnel Passé 'se serait écrasée' dengan penyesuaian feminin -e untuk la sonde).",
        "distractors": [
            "ont commis / s'est écrasée (kombinasi Passé Composé faktual yang salah karena mengklaim wahana tersebut benar-benar jatuh hancur).",
            "auraient commis / s'écrasait (urutan terbalik yang dilarang karena menempatkan Conditionnel di anak kalimat si).",
            "avaient commis / s'écraserait (kombinasi pincang antara Plus-que-parfait di anak kalimat dengan Conditionnel Présent di induk kalimat).",
            "commettraient / se serait écrasée (penggunaan Conditionnel Présent di anak kalimat si yang melanggar aturan sintaksis)."
        ],
        "formula": {
            "title": "L'IRRÉEL DU PASSÉ: CONDITIONNEL PASSÉ",
            "latex": "\\mathbf{Si} + \\text{avaient commis (PQP)}, \\quad \\text{la sonde (Fém.) } \\mathbf{se \\text{ } serait \\text{ } écrasée} \\text{ (Cond. Passé)}",
            "legend": "• Menyatakan hipotesis yang tidak pernah terjadi di masa lampau.<br>• la sonde adalah feminin $\\rightarrow$ se serait écrasée (+e)."
        },
        "hints": {
            "concept": "Pola pengandaian masa lampau (Irréel du passé) adalah: 'Si + Plus-que-parfait, ... Conditionnel Passé'. Subjek anak kalimat: 'nos ingénieurs' -> avaient commis. Subjek induk kalimat: 'la sonde spatiale' (feminin) -> se serait écrasée (dengan penyesuaian feminin -e).",
            "execution": "Si + avaient commis -> se serait écrasée."
        }
    },
    {
        "id": "fra-sim-13",
        "materi": "GRAMMAIRE: DISCOURS INDIRECT AU PASSÉ AVEC INTERROGATION TOTALE",
        "topic": "Penggunaan Kata Sambung 'si' dan Penyesuaian Waktu dalam Kalimat Tanya Tak Langsung Lampau",
        "stem": "Ibu guru menanyakan kesiapan murid kemarin sore:\nUjaran langsung: La professeure a demandé aux élèves: «Avez-vous compris la règle de grammaire?»\nBentuk kalimat wicara tidak langsung (Discours indirect au passé) yang TEPAT secara gramatikal adalah...",
        "correct": "La professeure a demandé aux élèves s'ils avaient compris la règle de grammaire.",
        "distractors": [
            "La professeure a demandé aux élèves qu'est-ce qu'ils avaient compris la règle de grammaire.",
            "La professeure a demandé aux élèves si ont-ils compris la règle de grammaire.",
            "La professeure a demandé aux élèves s'ils ont compris la règle de grammaire sans changer le temps.",
            "La professeure a demandé aux élèves que s'ils avaient compris la règle de grammaire."
        ],
        "formula": {
            "title": "LE DISCOURS INDIRECT AU PASSÉ: INTERROGATION TOTALE",
            "latex": "\\text{Question oui/non (Avez-vous...)} \\quad \\implies \\quad \\mathbf{demander \\text{ } si} + \\mathbf{Plus-que-parfait (avaient compris)}",
            "legend": "• Pertanyaan ya/tidak berubah menggunakan kata sambung 'si' (mengalami elisi di depan ils: s'ils).<br>• Inversi subjek-verba DIHAPUS.<br>• Passé Composé (avez compris) bergeser menjadi Plus-que-parfait (avaient compris)."
        },
        "hints": {
            "concept": "Tiga aturan Discours indirect au passé untuk pertanyaan total (ya/tidak): 1) Gunakan kata sambung 'si' (melebur menjadi s'ils); 2) Hilangkan inversi (kembali ke urutan subjek + verba); 3) Geser waktu lampau: Passé Composé (avez compris) berubah menjadi Plus-que-parfait (avaient compris).",
            "execution": "demander s'ils avaient compris."
        }
    },
    {
        "id": "fra-sim-14",
        "materi": "GRAMMAIRE: LE SUBJONCTIF PASSÉ",
        "topic": "Menyatakan Kelegaan Atas Peristiwa yang Telah Selesai dengan Subjonctif Passé",
        "stem": "Seorang ibu merasa lega setelah menerima kabar kepulangan putranya dari luar negeri:\n'Je suis tellement soulagée que mon fils ( ... ) sain et sauf de son voyage en haute montagne.'\nBentuk konjugasi Subjonctif Passé dari kata kerja gerak 'revenir' untuk subjek tunggal 'mon fils' adalah...",
        "correct": "soit revenu (Subjonctif Passé dengan kata kerja bantu être 'soit' + Participe Passé 'revenu').",
        "distractors": [
            "ait revenu (kesalahan fatal kata kerja bantu avoir untuk verba perpindahan tempat revenir).",
            "soit revenue (kesalahan penambahan akhiran feminin -e untuk subjek maskulin mon fils).",
            "est revenu (bentuk Passé Composé indikatif yang keliru karena être soulagé que menuntut modus subjonctif).",
            "serait revenu (bentuk Conditionnel Passé yang tidak cocok untuk klausula emosional perasaan lega)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF PASSÉ AVEC ÊTRE",
            "latex": "\\text{Expression de soulagement (être soulagé que)} \\implies \\text{Subjonctif Passé: } \\text{qu'il } \\mathbf{soit \\text{ } revenu}",
            "legend": "• Subjonctif Passé: être/avoir au subjonctif présent + Participe Passé.<br>• Verba gerak revenir menggunakan auxiliaire 'être' $\\rightarrow$ qu'il soit revenu."
        },
        "hints": {
            "concept": "Ungkapan perasaan emosional 'être soulagé que' (merasa lega bahwa) mewajibkan Subjonctif. Karena peristiwa kepulangannya sudah selesai terjadi sebelum rasa lega diungkapkan, digunakan Subjonctif Passé. Kata kerja 'revenir' menggunakan auxiliaire 'être', sehingga bentuknya adalah 'soit revenu'.",
            "execution": "Subjonctif Passé dari revenir untuk mon fils = 'soit revenu'."
        }
    },
    {
        "id": "fra-sim-15",
        "materi": "COMPRÉHENSION ÉCRITE: LES ÉNERGIES RENOUVELABLES EN FRANCE",
        "topic": "Dilema Transisi Energi antara Tenaga Nuklir Historis dan Pengembangan Energi Terbarukan",
        "stem": "Bacalah wacana kebijakan energi nasional Prancis berikut:\n'La France présente une spécificité énergétique unique en Europe: près de 70 % de son électricité est d'origine nucléaire, ce qui lui confère un niveau d'émissions de carbone par habitant parmi les plus bas des pays industrialisés. Néanmoins, face au vieillissement prévisible du parc de réacteurs et aux impératifs d'indépendance stratégique, l'État français engage une double trajectoire ambitieuse: d'une part, la prolongation sous haute sécurité des centrales existantes et la construction de réacteurs de nouvelle génération (EPR), et d'autre part, l'accélération massive des investissements dans l'éolien maritime et le solaire photovoltaïque afin de diversifier durablement le mix énergétique national.'\nBerdasarkan wacana di atas, pendekatan strategis Prancis dalam mengamankan masa depan pasokan energinya adalah...",
        "correct": "Menempuh strategi gabungan (double trajectoire) antara peremajaan teknologi tenaga nuklir rendah karbon dan ekspansi besar-besaran energi terbarukan angin dan surya.",
        "distractors": [
            "Penutupan mendadak seluruh reaktor nuklir besok pagi dan mengimpor batubara polutif dari luar negeri.",
            "Penghentian seluruh proyek tenaga angin dan surya karena dianggap merusak pemandangan estetika pedesaan.",
            "Pelarangan penggunaan listrik di sektor perumahan demi memprioritaskan industri persenjataan militer.",
            "Privatisasi seluruh sumber daya air dan penghentian pemeliharaan bendungan pembangkit listrik tenaga air."
        ],
        "formula": {
            "title": "LE MIX ÉNERGÉTIQUE FRANÇAIS",
            "latex": "\\text{Mix énergétique} = \\text{Nucléaire décarboné (EPR)} + \\text{Énergies renouvelables (Éolien / Solaire)}",
            "legend": "• 70% listrik Prancis berasal dari nuklir (rendah emisi karbon).<br>• Strategi ganda: modernisasi nuklir + percepatan energi terbarukan."
        },
        "hints": {
            "concept": "Wacana menegaskan: 'engage une double trajectoire ambitieuse: d'une part, la prolongation ... et la construction de réacteurs de nouvelle génération (EPR), et d'autre part, l'accélération massive des investissements dans l'éolien maritime et le solaire'.",
            "execution": "Strategi gabungan antara nuklir modern dan ekspansi energi terbarukan (angin/surya)."
        }
    },
    {
        "id": "fra-sim-16",
        "materi": "GRAMMAIRE: LES PRONOMS INDÉFINIS (CHACUN, AUCUN, CERTAINS)",
        "topic": "Penggunaan Pronomina 'aucun' dengan Partikel Negasi 'ne' Tanpa 'pas'",
        "stem": "Dalam rapat dewan direksi mengenai pemilihan kandidat kepala perwakilan baru:\n'Après un examen minutieux des vingt dossiers reçus, ( ... ) des candidats ( ... ) possède l'expérience internationale requise pour ce poste stratégique.'\nPasangan struktur negasi pronominal yang TEPAT adalah...",
        "correct": "aucun / ne (pronomina negasi subjek 'aucun' yang berpasangan secara eksklusif dengan partikel 'ne' tanpa menyertakan partikel pas).",
        "distractors": [
            "aucun / ne ... pas (kesalahan memasukkan partikel pas yang dilarang keras bila sudah ada pronomina negasi aucun).",
            "personne / ne ... rien (penggunaan negasi ganda yang merusak struktur semantik kalimat kualifikasi kerja).",
            "nul / n'a pas (kesalahan sintaksis penambahan partikel pas setelah subjek negasi nul).",
            "certains / ne ... jamais (kontradiksi logika semantik antara kata beberapa dengan negasi tidak pernah)."
        ],
        "formula": {
            "title": "LA NÉGATION AVEC AUCUN (SUJET)",
            "latex": "\\mathbf{Aucun} + \\text{de } \\dots + \\mathbf{ne} + \\text{Verbe} \\quad (\\text{SANS 'pas'!})",
            "legend": "• 'Aucun' bertindak sebagai subjek negatif tunggal.<br>• ATURAN EMAS: Jangan pernah menambahkan kata 'pas' jika kalimat sudah memakai aucun, personne, atau rien!"
        },
        "hints": {
            "concept": "Kata ganti negatif 'aucun' (tak satu pun) bertindak sebagai penanda negasi, sehingga hanya membutuhkan partikel verbal 'ne'. Penambahan kata 'pas' dilarang mutlak karena akan menjadi negasi ganda yang salah (aucun des candidats ne possède...).",
            "execution": "aucun + ne (tanpa pas)."
        }
    },
    {
        "id": "fra-sim-17",
        "materi": "GRAMMAIRE: LE SUBJONCTIF DU VERBE CROIRE À LA FORME NÉGATIVE",
        "topic": "Konjugasi Subjonctif dari Verba 'croire' untuk Persona Pertama Jamak 'nous'",
        "stem": "Seorang anggota parlemen menyatakan ketidakyakinannya atas klaim statistik kementerian:\n'Bien que les rapports officiels soient optimistes, nous ne croyons pas que nous ( ... ) éradiquer complètement la précarité urbaine d'ici deux ans.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'pouvoir' untuk subjek 'nous' adalah...",
        "correct": "puissions (akar subjonctif puiss- + akhiran Subjonctif persona pertama jamak -ions).",
        "distractors": [
            "pouvons (bentuk Présent de l'indicatif yang keliru karena ne pas croire que menuntut subjonctif).",
            "pouvions (bentuk Imparfait indikatif yang salah modus).",
            "pourrions (bentuk Conditionnel Présent yang salah fungsi pada klausula subordinat).",
            "puissons (kesalahan akhiran -ons pada akar subjonctif)."
        ],
        "formula": {
            "title": "NE PAS CROIRE QUE + SUBJONCTIF",
            "latex": "\\text{ne pas croire que (incertitude)} \\quad \\implies \\quad \\text{Subjonctif: } \\text{que nous } \\mathbf{puissions}",
            "legend": "• Kalimat negatif 'ne pas croire que' menunjukkan ketidakyakinan $\\rightarrow$ Subjonctif.<br>• nous $\\rightarrow$ puissions."
        },
        "hints": {
            "concept": "Kata kerja opini dalam bentuk negatif ('ne pas croire que' = tidak percaya bahwa) menyatakan ketidakpastian mendalam, sehingga mewajibkan pemakaian modus Subjonctif. Subjonctif dari verba 'pouvoir' untuk subjek 'nous' adalah 'puissions'.",
            "execution": "ne pas croire que + nous + pouvoir -> 'puissions'."
        }
    },
    {
        "id": "fra-sim-18",
        "materi": "GRAMMAIRE: LES PRONOMS EN ET Y COMBINÉS DANS UNE SEULE CLAUSE",
        "topic": "Urutan Dua Pronomina Adverbial 'y' Sebelum 'en' (il y en a)",
        "stem": "Dalam percakapan mengenai ketersediaan tiket konser musik klasik:\n'Reste-t-il encore des places disponibles pour la représentation d'opéra de ce soir à Garnier? — Oui, il ( ... ) reste encore une dizaine au balcon.'\nBentuk susunan pronomina tempat dan kuantitas yang TEPAT dalam konstruksi impersonal 'il reste' adalah...",
        "correct": "y en (urutan baku pronomina adverbial di mana pronomina tempat 'y' mendahului pronomina kuantitas 'en').",
        "distractors": [
            "en y (urutan terbalik yang melanggar hukum fonetik dan sintaksis bahasa Prancis).",
            "l'en (kombinasi keliru pronomina langsung dengan partitif).",
            "les y (penggunaan pronomina definit les yang tidak sesuai dengan partisi kuantitas une dizaine).",
            "y les (kombinasi salah fungsi sintaksis)."
        ],
        "formula": {
            "title": "L'ORDRE DES PRONOMS: Y DEVANT EN",
            "latex": "\\text{Structure: } \\mathbf{y} + \\mathbf{en} \\quad (\\text{ex: Il } \\mathbf{y \\text{ } en} \\text{ a / Il } \\mathbf{y \\text{ } en} \\text{ reste})",
            "legend": "• 'y' (tempat di Garnier) SELALU mendahului 'en' (kuantitas des places).<br>• Urutan 'en y' TIDAK PERNAH ada dalam bahasa Prancis baku."
        },
        "hints": {
            "concept": "Bila pronomina adverbial 'y' (tempat) dan 'en' (kuantitas) muncul bersamaan dalam satu klausa, aturannya mutlak: 'y' SELALU mendahului 'en' (il y en a, il y en reste). Bentuk 'en y' adalah kesalahan fatal.",
            "execution": "y + en -> 'y en'."
        }
    },
    {
        "id": "fra-sim-19",
        "materi": "GRAMMAIRE: L'EXPRESSION DE L'OPPOSITION (TANDIS QUE / ALORS QUE)",
        "topic": "Penggunaan Konjungsi 'tandis que' yang Diikuti oleh Modus Indikatif untuk Menyatakan Kontras",
        "stem": "Dalam studi perbandingan demografi perkotaan:\n'Tandis que la population des zones rurales ( ... ) progressivement en raison du vieillissement, les grandes métropoles régionales continuent d'attirer de jeunes actifs.'\nBentuk konjugasi kata kerja 'diminuer' pada kala Présent de l'indicatif yang TEPAT setelah konjungsi oposisi kontras 'tandis que' untuk subjek tunggal 'la population' adalah...",
        "correct": "diminue (bentuk Présent de l'indicatif persona ketiga tunggal yang dituntut oleh konjungsi oposisi fakta nyata tandis que).",
        "distractors": [
            "diminue (Subjonctif yang secara kebetulan berakhiran sama namun salah konsep landasan gramatikal).",
            "diminuât (bentuk Subjonctif Imparfait yang tidak sesuai dengan penanda waktu waktu sekarang).",
            "diminuerait (bentuk Conditionnel Présent yang tidak dapat menjadi pelengkap konjungsi perbandingan fakta nyata tandis que).",
            "ayant diminué (bentuk Participe Passé Composé yang merusak integritas klausa berkonjungsi)."
        ],
        "formula": {
            "title": "EXPRESSION DE L'OPPOSITION: TANDIS QUE + INDICATIF",
            "latex": "\\mathbf{Tandis \\text{ } que / Alors \\text{ } que} + \\mathbf{Indicatif} \\quad (\\text{opposition / contraste de faits réels})",
            "legend": "• 'Tandis que' menyatakan pertentangan/perbandingan dua fakta nyata yang terjadi bersamaan.<br>• Selalu menggunakan modus INDIKATIF (bukan Subjonctif!)."
        },
        "hints": {
            "concept": "Konjungsi oposisi 'tandis que' (sementara itu / padahal) menyatakan kontras perbandingan antara dua fakta nyata. Berbeda dengan 'bien que', 'tandis que' SELALU diikuti oleh modus INDIKATIF. Subjek 'la population' (tunggal) -> 'diminue'.",
            "execution": "tandis que + indicatif tunggal = 'diminue'."
        }
    },
    {
        "id": "fra-sim-20",
        "materi": "GRAMMAIRE: LE SUBJONCTIF DU VERBE VALOIR",
        "topic": "Akar Subjonctif Tidak Beraturan dari Kata Kerja 'valoir' dalam Konstruksi 'il vaut mieux que'",
        "stem": "Saran dari seorang penasihat hukum keluarga:\n'Avant de signer un engagement contractuel d'une telle importance, il vaut beaucoup mieux que vous ( ... ) un avocat spécialisé.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'consulter' untuk subjek 'vous' adalah...",
        "correct": "consultiez (akar consult- + akhiran Subjonctif persona kedua jamak -iez yang dipicu oleh frasa penilaian il vaut mieux que).",
        "distractors": [
            "consultez (bentuk Présent de l'indicatif yang salah modus karena frasa il vaut mieux que mewajibkan subjonctif).",
            "consulterez (bentuk Futur Simple indikatif yang salah modus).",
            "consulteriez (bentuk Conditionnel Présent yang salah fungsi pada anak kalimat subordinat saran).",
            "avez consulté (bentuk Passé Composé indikatif yang keliru aspek waktu)."
        ],
        "formula": {
            "title": "IL VAUT MIEUX QUE + SUBJONCTIF",
            "latex": "\\text{Expression de conseil préférentiel: } \\mathbf{Il \\text{ } vaut \\text{ } mieux \\text{ } que} \\implies \\mathbf{Subjonctif (consultiez)}",
            "legend": "• Frasa 'il vaut mieux que' (lebih baik bahwa) selalu menuntut Subjonctif.<br>• vous $\\rightarrow$ consultiez."
        },
        "hints": {
            "concept": "Struktur saran impersonal 'il vaut mieux que' (lebih baik jika/bahwa) mewajibkan kata kerja dalam anak kalimat menggunakan modus Subjonctif. Verba kelompok 1 'consulter' untuk subjek 'vous' pada modus Subjonctif adalah 'consultiez'.",
            "execution": "il vaut mieux que + vous + consulter -> 'consultiez'."
        }
    },
    {
        "id": "fra-sim-21",
        "materi": "GRAMMAIRE: ACCORD DU PARTICIPE PASSÉ SUIVI D'UN INFINITIF",
        "topic": "Kaidah Penyelarasan Participe Passé 'faire' yang Diikuti Langsung Kata Kerja Infinitif",
        "stem": "Dalam laporan arsitektur restorasi monumen bersejarah:\n'Les pierres de taille calcaires que l'architecte en chef a ( ... ) tailler par les artisans compagnons proviennent des carrières de Bourgogne.'\nBentuk Participe Passé dari kata kerja 'faire' yang TEPAT dalam konstruksi faktitif (faire + infinitif) adalah...",
        "correct": "fait (Participe Passé dari kata kerja 'faire' yang diikuti langsung oleh infinitif TIDAK PERNAH mengalami accord dalam kondisi apa pun).",
        "distractors": [
            "faite (kesalahan penambahan penanda feminin tunggal -e).",
            "faites (kesalahan menyelaraskan Participe Passé dengan objek les pierres de taille yang mendahului).",
            "faisait (bentuk Imparfait indikatif yang merusak tenses waktu Passé Composé).",
            "faits (kesalahan penambahan akhiran maskulin jamak)."
        ],
        "formula": {
            "title": "RÈGLE D'INVARIABILITÉ: FAIT + INFINITIF",
            "latex": "\\mathbf{faire} + \\text{Infinitif} \\quad \\implies \\quad \\mathbf{FAIT \\text{ est TOUJOURS INVARIABLE}} \\quad (\\text{a } \\mathbf{fait} \\text{ tailler})",
            "legend": "• ATURAN EMAS TKA PRANCIS: Participe Passé 'fait' bila diikuti oleh kata kerja infinitif TIDAK PERNAH bersepakat (invariable)!<br>• Dilarang keras menulis: 'les pierres qu'il a faites tailler' (SALAH BESAR!)."
        },
        "hints": {
            "concept": "Aturan gramatika baku Prancis tingkat tinggi: Participe Passé dari kata kerja 'faire' yang langsung diikuti oleh kata kerja Infinitif (konstruksi faktitif) SELALU BERSIFAT INVARIABEL (tidak pernah berubah atau mendapat tambahan huruf apa pun), meskipun didahului oleh objek COD jamak (a fait tailler).",
            "execution": "fait + infinitif -> selalu tetap 'fait'."
        }
    },
    {
        "id": "fra-sim-22",
        "materi": "COMPRÉHENSION ÉCRITE: L'INTELLIGENCE ARTIFICIELLE ET L'ÉTHIQUE",
        "topic": "Tantangan Regulasi Hukum AI Act Uni Eropa terhadap Perlindungan Privasi",
        "stem": "Bacalah teks analisis teknologi dan hukum Eropa berikut:\n'Adopté par les institutions européennes, l'«IA Act» constitue la première législation contraignante au monde destinée à encadrer le développement et le déploiement de l'intelligence artificielle. Fondé sur une approche graduée par les risques, ce texte interdit formellement les systèmes jugés inacceptables pour les droits fondamentaux, tels que la notation sociale généralisée ou la manipulation cognitive subliminale. Pour les applications à \"haut risque\" (santé, éducation, infrastructures critiques), les concepteurs doivent garantir une transparence rigoureuse des algorithmes, une supervision humaine effective et l'absence de biais discriminatoires dans les données d'entraînement.'\nBerdasarkan wacana di atas, filosofi utama pendekatan regulasi 'IA Act' Uni Eropa adalah...",
        "correct": "Penerapan kerangka hukum berbasis klasifikasi tingkat risiko (approche par les risques) yang melarang sistem perusak hak asasi serta mewajibkan pengawasan manusia dan transparansi data.",
        "distractors": [
            "Pemberian kebebasan tanpa batas kepada perusahaan teknologi untuk menggunakan data pribadi warga tanpa izin.",
            "Pelarangan total terhadap seluruh pengembangan komputer dan ponsel pintar di benua Eropa.",
            "Penghapusan seluruh hak cipta karya intelektual demi melatih model kecerdasan buatan secara liar.",
            "Kewajiban menggantikan seluruh tenaga medis rumah sakit dengan algoritma otomatis tanpa dokter manusia."
        ],
        "formula": {
            "title": "LA RÉGULATION DE L'IA EN EUROPE (IA ACT)",
            "latex": "\\text{Approche par les risques} \\implies \\text{Interdiction des risques inacceptables} + \\text{Supervision humaine obligatoire}",
            "legend": "• Regulasi global pertama yang mengikat secara hukum.<br>• Melindungi hak asasi warga dari manipulasi kognitif dan diskriminasi algoritma."
        },
        "hints": {
            "concept": "Teks memaparkan: 'Fondé sur une approche graduée par les risques, ce texte interdit formellement les systèmes jugés inacceptables pour les droits fondamentaux ... Pour les applications à haut risque ... garantir une transparence rigoureuse ... une supervision humaine effective'.",
            "execution": "Pilihan yang menjelaskan pendekatan klasifikasi tingkat risiko, larangan risiko fatal, dan pengawasan manusia."
        }
    },
    {
        "id": "fra-sim-23",
        "materi": "GRAMMAIRE: LE SUBJONCTIF DU VERBE MOURIR",
        "topic": "Konjugasi Subjonctif dari Kata Kerja 'mourir' untuk Persona Ketiga Tunggal 'il/elle'",
        "stem": "Dalam wacana pelestarian satwa langka yang terancam punah:\n'Les écologistes se mobilisent sans relâche de peur que cette espèce emblématique de tortue marine ne ( ... ) dans l'indifférence générale.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'mourir' untuk persona ketiga tunggal 'cette espèce' adalah...",
        "correct": "meure (akar tidak beraturan meur- + akhiran Subjonctif persona ketiga tunggal -e).",
        "distractors": [
            "meurt (bentuk Présent de l'indicatif yang salah modus setelah konjungsi rasa takut de peur que).",
            "mourait (bentuk Imparfait indikatif yang salah modus).",
            "mourra (bentuk Futur Simple indikatif yang salah modus).",
            "meurent (bentuk Subjonctif jamak yang keliru jumlah untuk subjek tunggal cette espèce)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DU VERBE MOURIR",
            "latex": "\\text{de peur que + 'ne' explétif} \\implies \\text{Subjonctif: } \\text{qu'elle } \\mathbf{meure} \\quad (\\text{radical: meur-})",
            "legend": "• Konjungsi kekhawatiran/ketakutan 'de peur que' menuntut Subjonctif (disertai partikel 'ne' ekspletif).<br>• cette espèce (elle) $\\rightarrow$ meure."
        },
        "hints": {
            "concept": "Konjungsi rasa takut 'de peur que' (karena takut bahwa / jangan-jangan) mewajibkan kata kerja dalam modus Subjonctif. Verba 'mourir' memiliki konjugasi Subjonctif: que je meure, que tu meures, qu'il/elle meure, que nous mourions, que vous mouriez, qu'ils meurent. Untuk 'cette espèce' (tunggal), bentuknya adalah 'meure'.",
            "execution": "de peur que + elle + mourir -> 'meure'."
        }
    },
    {
        "id": "fra-sim-24",
        "materi": "GRAMMAIRE: L'ACCORD DU PARTICIPE PASSÉ DU VERBE 'LAISSER' SUIVI D'UN INFINITIF",
        "topic": "Reformasi Ejaan 1990 Terkait Imutabilitas Participe Passé 'laissé + infinitif'",
        "stem": "Dalam narasi sastra modern:\n'Fatiguée par son long voyage en train, la fillette s'est ( ... ) endormir sur les genoux de sa mère.'\nBentuk Participe Passé dari kata kerja 'se laisser' yang TEPAT sesuai rekomendasi ejaan modern Akademi Prancis (rectifications orthographiques) adalah...",
        "correct": "laissé (invariabel tanpa accord ketika diikuti langsung oleh kata kerja infinitif endormir).",
        "distractors": [
            "laissée (bentuk tradisional dengan accord yang rentan menimbulkan kerancuan gramatikal dan tidak lagi diwajibkan).",
            "laissées (bentuk jamak yang keliru jumlah untuk subjek tunggal la fillette).",
            "laisser (bentuk dasar infinitif yang salah kedudukan dalam struktur Passé Composé).",
            "laisserait (bentuk Conditionnel Présent yang salah tenses waktu)."
        ],
        "formula": {
            "title": "INVARIABILITÉ DE 'LAISSER + INFINITIF'",
            "latex": "\\mathbf{se \\text{ } laisser} + \\text{Infinitif} \\quad \\implies \\quad \\mathbf{laissé \\text{ est invariable}} \\quad (\\text{s'est } \\mathbf{laissé} \\text{ endormir})",
            "legend": "• Sesuai kaidah resmi Académie française, 'laisser' yang diikuti infinitif diperlakukan invariabel seperti halnya 'faire'.<br>• Menghindari kerumitan penentuan subjek aktif infinitif."
        },
        "hints": {
            "concept": "Berdasarkan pedoman gramatika baku modern (Académie française), kata kerja 'laisser' yang langsung diikuti oleh infinitif diperlakukan sama seperti verba 'faire', yaitu bersifat INVARIABEL (tidak mengalami accord gender/jumlah): 'elle s'est laissé endormir'.",
            "execution": "se laisser + infinitif -> bentuk invariabel = 'laissé'."
        }
    },
    {
        "id": "fra-sim-25",
        "materi": "GRAMMAIRE: LE SUBJONCTIF DANS LES PROPOSITIONS RELATIVES À VALEUR D'ATTENTE OU DE BUT",
        "topic": "Penggunaan Subjonctif dalam Klausa Relatif yang Menyatakan Benda/Orang yang Masih Dicari Keberadaannya",
        "stem": "Dalam iklan lowongan pekerjaan manajerial:\n'Notre entreprise internationale recherche urgemment un traducteur bilingue français-indonésien qui ( ... ) rédiger des contrats juridiques complexes sans aucune assistance.'\nBentuk konjugasi kata kerja 'pouvoir' yang TEPAT dalam klausa relatif yang mendeskripsikan profil sosok yang dicari dan belum dipastikan keberadaannya adalah...",
        "correct": "puisse (modus Subjonctif yang wajib digunakan dalam klausa relatif ketika anteseden mengekspresikan entitas yang diinginkan, dicari, atau belum pasti eksistensinya).",
        "distractors": [
            "peut (bentuk Indikatif yang keliru karena mengimplikasikan orang tersebut sudah ada dan dikenal pasti di depan mata).",
            "pourra (bentuk Futur Simple indikatif yang salah modus).",
            "pourrait (bentuk Conditionnel yang tidak mencerminkan modus wajib pencarian eksistensial).",
            "pouvait (bentuk Imparfait indikatif yang salah aspek waktu)."
        ],
        "formula": {
            "title": "SUBJONCTIF DANS LA RELATIVE (OBJET RECHERCHÉ)",
            "latex": "\\text{Verbe de recherche (chercher, vouloir)} + \\text{Nom indéfini} + \\mathbf{qui} \\implies \\mathbf{Subjonctif (puisse)}",
            "legend": "• Bila entitas yang dicari belum tentu ada di dunia nyata, anak kalimat relatif WAJIB menggunakan Subjonctif.<br>• Menandakan harapan kualifikasi (profil ideal yang dicari)."
        },
        "hints": {
            "concept": "Dalam bahasa Prancis tingkat tinggi, anak kalimat relatif (diawali 'qui/que') wajib menggunakan modus Subjonctif jika kata benda yang disifatinya adalah sosok/benda yang sedang dicari, diinginkan, dan belum dipastikan keberadaan nyatanya ('recherche un traducteur qui puisse...').",
            "execution": "recherche un traducteur qui + Subjonctif dari pouvoir = 'puisse'."
        }
    },

    # -------------------------------------------------------------
    # 5 PILIHAN GANDA KOMPLEKS / MULTI-SELECT (fra-sim-26 .. fra-sim-30)
    # -------------------------------------------------------------
    {
        "id": "fra-sim-26",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: VERBES DU PASSÉ COMPOSÉ AVEC ÊTRE",
        "topic": "Klasifikasi Kata Kerja Perpindahan/Keberadaan yang Wajib Menggunakan Auxiliaire 'être'",
        "questionHtml": "Dalam pembentukan kala lampau Passé Composé, sebagian kata kerja intransitif perpindahan tempat atau perubahan status (dikenal sebagai <em>verbes de la maison d'être</em>) wajib berpasangan dengan kata kerja bantu <strong>être</strong> dan Participe Passé-nya menyelaraskan gender serta jumlah dengan subjek. Dari daftar kata kerja di bawah ini, manakah <strong>DUA (2)</strong> kata kerja yang WAJIB menggunakan kata kerja bantu <em>être</em>?",
        "options": [
            {
                "key": "A",
                "text": "naître (lahir: il est né / elle est née, mengalami perubahan status kehidupan).",
                "correct": True
            },
            {
                "key": "B",
                "text": "manger (makan: verba transitif aksi fisik yang menggunakan kata kerja bantu avoir).",
                "correct": False
            },
            {
                "key": "C",
                "text": "tomber (jatuh: verba gerak perpindahan posisi fisik yang membentuk lampau dengan être: il est tombé).",
                "correct": True
            },
            {
                "key": "D",
                "text": "chanter (bernyanyi: verba aktivitas bersuara yang berkonjugasi dengan kata kerja bantu avoir).",
                "correct": False
            },
            {
                "key": "E",
                "text": "lire (membaca: verba transitif yang membutuhkan objek bacaan dan berpasangan dengan avoir).",
                "correct": False
            }
        ],
        "correctAnswer": ["A", "C"],
        "formula": {
            "title": "LES VERBES CONJUGUÉS AVEC ÊTRE (MAISON D'ÊTRE)",
            "latex": "\\text{Verbes avec être: } \\text{naître, mourir, monter, descendre, arriver, partir, venir, aller, } \\mathbf{tomber}, \\text{ rester...}",
            "legend": "• naître dan tomber adalah anggota inti verba gerak/status (la maison d'être).<br>• manger, chanter, lire menggunakan auxiliaire 'avoir'."
        },
        "hints": {
            "concept": "14 kata kerja dasar yang menggunakan 'être' pada Passé Composé meliputi: naître, mourir, aller, venir, arriver, partir, monter, descendre, entrer, sortir, retourner, passer, rester, tomber. Di antara opsi di atas, yang termasuk adalah 'naître' (A) dan 'tomber' (C).",
            "execution": "Verba yang berpasangan dengan être = A (naître) dan C (tomber)."
        }
    },
    {
        "id": "fra-sim-27",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: DÉCLENCHEURS DU SUBJONCTIF",
        "topic": "Identifikasi Ungkapan Pemicu Modus Subjonctif dalam Bahasa Prancis Baku",
        "stem": "Modus Subjonctif dalam bahasa Prancis digunakan untuk mengekspresikan subjektivitas, keharusan, kehendak, keraguan, atau perasaan emosional pada anak kalimat subordinat. Dari ungkapan-ungkapan pengantar klausa di bawah ini, manakah <strong>DUA (2)</strong> ungkapan yang WAJIB memicu pemakaian modus <em>Subjonctif</em> pada anak kalimat?",
        "options": [
            {
                "key": "A",
                "text": "Il est certain que (ungkapan kepastian mutlak yang wajib diikuti oleh modus Indikatif).",
                "correct": False
            },
            {
                "key": "B",
                "text": "Bien que (konjungsi subordinatif konsesif yang selalu menuntut pemakaian modus Subjonctif).",
                "correct": True
            },
            {
                "key": "C",
                "text": "Il est évident que (ungkapan bukti nyata obyektif yang diikuti oleh modus Indikatif).",
                "correct": False
            },
            {
                "key": "D",
                "text": "Il est indispensable que (ungkapan impersonal keharusan mutlak yang wajib diikuti oleh modus Subjonctif).",
                "correct": True
            },
            {
                "key": "E",
                "text": "Je sais que (ungkapan pengetahuan kepastian fakta yang wajib diikuti oleh modus Indikatif).",
                "correct": False
            }
        ],
        "correctAnswer": ["B", "D"],
        "formula": {
            "title": "DÉCLENCHEURS: SUBJONCTIF VS INDICATIF",
            "latex": "\\mathbf{Subjonctif: } \\text{Bien que, Il est indispensable que} \\quad \\leftrightarrow \\quad \\mathbf{Indicatif: } \\text{Il est certain que, Il est évident que, Je sais que}",
            "legend": "• Kepastian (certitude) $\\rightarrow$ Indicatif.<br>• Konsesi & Keharusan (obligation/concession) $\\rightarrow$ Subjonctif."
        },
        "hints": {
            "concept": "Subjonctif dipicu oleh keharusan impersonal (Il est indispensable que...) dan konjungsi konsesif (Bien que...). Sebaliknya, ungkapan yang menyatakan fakta pasti (Il est certain que, Il est évident que, Je sais que) selalu menggunakan Indikatif.",
            "execution": "Pemicu Subjonctif = B (Bien que) dan D (Il est indispensable que)."
        }
    },
    {
        "id": "fra-sim-28",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: CIVILISATION FRANÇAISE & PATRIMOINE",
        "topic": "Karakteristik Unik Tradisi Santap Gastronomi Prancis (Repas Gastronomique UNESCO)",
        "stem": "Tradisi bersantap Prancis (*le repas gastronomique des Français*) telah diakui oleh UNESCO sebagai Warisan Budaya Takbenda. Dari pernyataan-pernyataan di bawah ini, manakah <strong>DUA (2)</strong> karakteristik otentik dari ritual sosial gastronomi tersebut?",
        "options": [
            {
                "key": "A",
                "text": "Kewajiban menghabiskan makanan dalam waktu kurang dari lima belas menit tanpa boleh berbicara dengan sesama tamu meja.",
                "correct": False
            },
            {
                "key": "B",
                "text": "Penghayatan nilai kebersamaan (*convivialité*) dan seni berbagi kebahagiaan antarmanusia dalam suasana santap yang hangat.",
                "correct": True
            },
            {
                "key": "C",
                "text": "Penataan urutan hidangan yang terstruktur secara harmonis (aperitif, hidangan pembuka, hidangan utama, keju, hidangan penutup) yang dipadukan dengan anggur.",
                "correct": True
            },
            {
                "key": "D",
                "text": "Larangan menyajikan produk pertanian lokal (*terroir*) demi menggantikannya dengan produk makanan kemasan pabrik.",
                "correct": False
            },
            {
                "key": "E",
                "text": "Penyajian seluruh menu makanan sekaligus di atas piring plastik sekali pakai tanpa penataan meja formal.",
                "correct": False
            }
        ],
        "correctAnswer": ["B", "C"],
        "formula": {
            "title": "LES PILIERS DU REPAS GASTRONOMIQUE UNESCO",
            "latex": "\\text{Repas gastronomique} = \\mathbf{Convivialité \\text{ } et \\text{ } partage} + \\mathbf{Ordre \\text{ } rigoureux \\text{ } des \\text{ } mets \\text{ } et \\text{ } vins}",
            "legend": "• Menekankan hubungan sosial kekeluargaan/persahabatan (convivialité).<br>• Menghormati urutan klasik penyajian hidangan dan pairing anggur."
        },
        "hints": {
            "concept": "Dua pilar fundamental yang diakui UNESCO pada repas gastronomique Prancis adalah: 1) Nilai kebersamaan dan seni berbagi rasa kekeluargaan (convivialité - B); 2) Struktur urutan hidangan yang tertata rapi dari pembuka hingga penutup yang dipadukan harmonis dengan anggur (C).",
            "execution": "Karakteristik otentik = B dan C."
        }
    },
    {
        "id": "fra-sim-29",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: ACCORD DU PARTICIPE PASSÉ AVEC AVOIR",
        "topic": "Kondisi Munculnya Keselarasan (Accord) Participe Passé pada Kata Kerja Bantu 'avoir'",
        "stem": "Dalam kaidah tata bahasa Prancis, Participe Passé yang dikonjugasikan dengan kata kerja bantu <em>avoir</em> pada umumnya tidak menyelaraskan gender dan jumlah dengan subjek. Namun, terdapat pengecualian mutlak di mana Participe Passé WAJIB bersepakat. Dari situasi sintaksis di bawah ini, manakah <strong>DUA (2)</strong> kondisi yang MEWAJIBKAN Participe Passé bersepakat saat menggunakan kata kerja bantu <em>avoir</em>?",
        "options": [
            {
                "key": "A",
                "text": "Ketika objek penderita langsung (COD) ditempatkan mendahului kata kerja bantu dalam bentuk pronomina persona (me, te, le, la, nous, vous, les).",
                "correct": True
            },
            {
                "key": "B",
                "text": "Ketika subjek kalimat adalah kata ganti orang pertama jamak nous tanpa memandang posisi objek.",
                "correct": False
            },
            {
                "key": "C",
                "text": "Ketika kata kerja diikuti oleh objek penderita langsung (COD) yang berada di belakang Participe Passé.",
                "correct": False
            },
            {
                "key": "D",
                "text": "Ketika klausa menggunakan pronomina relatif COD 'que' yang merujuk pada anteseden kata benda di depan kalimat.",
                "correct": True
            },
            {
                "key": "E",
                "text": "Ketika kalimat menggunakan kata kerja bentuk pasif yang didahului oleh preposisi par.",
                "correct": False
            }
        ],
        "correctAnswer": ["A", "D"],
        "formula": {
            "title": "CONDITIONS D'ACCORD AVEC L'AUXILIAIRE AVOIR",
            "latex": "\\text{Accord avec AVOIR } \\iff \\mathbf{COD \\text{ est placé AVANT le verbe}} \\quad (\\mathbf{Pronom \\text{ } COD} \\text{ ou } \\mathbf{Pronom \\text{ } relatif \\text{ } 'que'})",
            "legend": "• Contoh Pronom COD: 'Il les a vues' (les = Fém. Plur. mendahului $\\rightarrow$ vues).<br>• Contoh Pronom relatif: 'La lettre qu'il a écrite' (que = la lettre mendahului $\\rightarrow$ écrite)."
        },
        "hints": {
            "concept": "Participe Passé dengan kata kerja bantu 'avoir' HANYA bersepakat jika Objek Langsung (COD) terletak SEBELUM kata kerja bantu. Dua situasi utamanya adalah: 1) Menggunakan pronomina COD di depan kata kerja bantu (A: les a vues); 2) Menggunakan pronomina relatif 'que' yang antesedennya berada di depan (D: les fleurs qu'il a cueillies).",
            "execution": "Kondisi wajib accord avoir = A dan D."
        }
    },
    {
        "id": "fra-sim-30",
        "type": "multi",
        "materi": "MULTIKOMPETENSI: PRONOMS ADVERBIAUX 'EN' ET 'Y'",
        "topic": "Aturan Sintaksis Pemilihan Pronomina Adverbial 'y' vs 'en'",
        "stem": "Pronomina adverbial <strong>y</strong> dan <strong>en</strong> memiliki fungsi spesifik untuk menggantikan komplemen berpreposisi. Dari pernyataan kaidah gramatika di bawah ini, manakah <strong>DUA (2)</strong> pernyataan yang BENAR mengenai penggunaan <em>y</em> dan <em>en</em>?",
        "options": [
            {
                "key": "A",
                "text": "Pronomina 'y' digunakan untuk menggantikan frasa keterangan tempat yang diawali oleh preposisi arah atau lokasi seperti à, au, en, dans, chez.",
                "correct": True
            },
            {
                "key": "B",
                "text": "Pronomina 'en' digunakan untuk menggantikan manusia yang terikat dengan kata kerja berpreposisi à seperti téléphoner à.",
                "correct": False
            },
            {
                "key": "C",
                "text": "Pronomina 'en' digunakan untuk menggantikan kata benda kuantitas yang didahului oleh artikel partitif (du, de la, des) atau penanda angka terbilang.",
                "correct": True
            },
            {
                "key": "D",
                "text": "Pronomina 'y' selalu ditempatkan setelah kata kerja utama dalam kalimat bentuk negatif lampau.",
                "correct": False
            },
            {
                "key": "E",
                "text": "Jika 'y' dan 'en' muncul bersamaan di depan satu kata kerja, pronomina 'en' selalu mendahului pronomina 'y'.",
                "correct": False
            }
        ],
        "correctAnswer": ["A", "C"],
        "formula": {
            "title": "FONCTIONS DES PRONOMS Y ET EN",
            "latex": "\\mathbf{Y} = \\text{Lieu introduit par } \\mathbf{à, en, dans, chez} \\quad | \\quad \\mathbf{EN} = \\text{Quantité / Partitif introduit par } \\mathbf{de, du, des, nombre}",
            "legend": "• j'y vais (au bureau) $\\rightarrow$ y = tempat.<br>• j'en mange deux (des pommes) $\\rightarrow$ en = partitif/kuantitas."
        },
        "hints": {
            "concept": "Pernyataan yang benar: A) Pronomina 'y' menggantikan tempat berpreposisi arah à/dans/chez; C) Pronomina 'en' menggantikan kata benda kuantitas dengan partitif (de/du/des/angka). Opsi E salah karena 'y' selalu mendahului 'en' (y en).",
            "execution": "Pernyataan benar = A dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIKS ASOSIASI BENAR-SALAH (fra-sim-31 .. fra-sim-35)
    # -------------------------------------------------------------
    {
        "id": "fra-sim-31",
        "type": "matrix",
        "materi": "MULTIKOMPETENSI MATRIKS: ANALISIS TEKS TRANSISI ENERGI & EKOLOGI",
        "topic": "Evaluasi Validitas Pernyataan Mengenai Kebijakan Iklim dan Transportasi Rendah Karbon",
        "stem": "Bacalah wacana kebijakan lingkungan hidup berikut:\n'Pour atteindre la neutralité carbone à l'horizon 2050, la France combine plusieurs leviers sectoriels: la décarbonation complète du secteur des transports par le développement des véhicules électriques et du réseau ferroviaire à grande vitesse (TGV), la rénovation thermique obligatoire des bâtiments résidentiels anciens pour éradiquer les passoires thermiques, et l'accélération du mix électrique équilibré entre énergies renouvelables et nucléaire de nouvelle génération.'\nTentukan kebenaran masing-masing pernyataan berikut berdasarkan wacana di atas (Benar atau Salah):",
        "statements": [
            {
                "text": "Sasaran utama kebijakan iklim Prancis adalah mencapai netralitas karbon pada tahun 2050 melalui berbagai langkah sektoral terpadu.",
                "correct": "Benar"
            },
            {
                "text": "Pemerintah Prancis melarang sepenuhnya pengembangan jaringan kereta api cepat TGV demi menggantikannya dengan truk diesel.",
                "correct": "Salah"
            },
            {
                "text": "Renovasi termal pada bangunan tempat tinggal tua diwajibkan untuk menghentikan pemborosan energi termal (passoires thermiques).",
                "correct": "Benar"
            },
            {
                "text": "Kombinasi energi listrik nasional Prancis diarahkan pada keseimbangan antara energi terbarukan dan tenaga nuklir generasi baru.",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "LA NEUTRALITÉ CARBONE EN FRANCE (HORIZON 2050)",
            "latex": "\\text{Neutralité 2050} = \\text{Transports décarbonés (TGV/Électrique)} + \\text{Rénovation thermique} + \\text{Mix Renouvelable/Nucléaire}",
            "legend": "• Pernyataan 1: Sesuai teks (Benar).<br>• Pernyataan 2: Bertentangan dengan teks (Salah).<br>• Pernyataan 3: Sesuai teks (Benar).<br>• Pernyataan 4: Sesuai teks (Benar)."
        },
        "hints": {
            "concept": "Evaluasi fakta teks: 1) Netralitas karbon 2050 disebutkan eksplisit di awal teks (Benar). 2) TGV justru dikembangkan untuk dekarbonisasi transportasi, bukan dilarang (Salah). 3) Renovasi termal bangunan diwajibkan untuk passoires thermiques (Benar). 4) Keseimbangan energi terbarukan dan nuklir generasi baru tercantum jelas (Benar).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "fra-sim-32",
        "type": "matrix",
        "materi": "MULTIKOMPETENSI MATRIKS: SUBJONCTIF VS INDICATIF (VALEUR DES MODES)",
        "topic": "Penetapan Modus Gramatikal yang Tepat (Subjonctif vs Indikatif) Berdasarkan Makna Klausa Utama",
        "stem": "Modus Indikatif digunakan untuk menyatakan fakta nyata dan kepastian objektif, sedangkan Subjonctif menyatakan keharusan, keraguan, perasaan batin, atau ketidakpastian. Tentukan kebenaran analisis pemilihan modus gramatikal pada masing-masing pernyataan berikut (Benar atau Salah):",
        "statements": [
            {
                "text": "Klausa 'Il est certain que...' (Pasti bahwa...) wajib diikuti oleh modus Indikatif karena mengekspresikan kepastian objektif.",
                "correct": "Benar"
            },
            {
                "text": "Klausa 'Il faut absolument que...' (Harus mutlak bahwa...) wajib diikuti oleh modus Indikatif waktu lampau.",
                "correct": "Salah"
            },
            {
                "text": "Klausa 'Je crains que...' (Saya khawatir bahwa...) wajib diikuti oleh modus Subjonctif karena mengekspresikan rasa takut dan kecemasan emosional.",
                "correct": "Benar"
            },
            {
                "text": "Klausa opini afirmatif 'Je crois que...' (Saya percaya bahwa...) selalu mewajibkan modus Subjonctif.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "DISTINCTION RIGORISTE: INDICATIF VS SUBJONCTIF",
            "latex": "\\text{Certitude / Fait réel} \\implies \\mathbf{Indicatif} \\quad | \\quad \\text{Obligation / Crainte / Volonté} \\implies \\mathbf{Subjonctif}",
            "legend": "• Il est certain que $\\rightarrow$ Indicatif (Benar).<br>• Il faut que $\\rightarrow$ SUBJONCTIF, bukan indikatif (Salah).<br>• Je crains que $\\rightarrow$ SUBJONCTIF (Benar).<br>• Je crois que (positif) $\\rightarrow$ INDICATIF, bukan subjonctif (Salah)."
        },
        "hints": {
            "concept": "1) Il est certain que -> Indikatif (Benar). 2) Il faut que menuntut Subjonctif, bukan indikatif (Salah). 3) Je crains que menyatakan perasaan takut -> Subjonctif (Benar). 4) Je crois que bentuk afirmatif menggunakan Indikatif, bukan Subjonctif (Salah).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "fra-sim-33",
        "type": "matrix",
        "materi": "MULTIKOMPETENSI MATRIKS: CIVILISATION & MODÈLE SOCIAL EUROPÉEN",
        "topic": "Validitas Karakteristik Sistem Kesejahteraan Sosial dan Layanan Publik Prancis",
        "stem": "Republik Prancis memiliki model perlindungan sosial yang khas di dunia (*le modèle social français*). Tentukan kebenaran masing-masing pernyataan sosiopolitik berikut (Benar atau Salah):",
        "statements": [
            {
                "text": "Semboyan 'Liberté, Égalité, Fraternité' merupakan moto resmi Republik Prancis yang terpampang pada gedung-gedung institusi publik.",
                "correct": "Benar"
            },
            {
                "text": "Sistem kesehatan Prancis Carte Vitale membebankan seluruh biaya operasi darurat rumah sakit kepada pasien tanpa subsidi negara.",
                "correct": "Salah"
            },
            {
                "text": "Pendidikan dasar dan menengah di sekolah negeri Prancis (*l'école publique*) bersifat gratis dan wajib bagi seluruh anak usia sekolah.",
                "correct": "Benar"
            },
            {
                "text": "Prinsip Laïcité menjamin kebebasan warga untuk beribadah secara damai sekaligus menjaga netralitas aparatur pemerintah dari pengaruh agama.",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "LES VALEURS RÉPUBLICAINES ET LE MODÈLE SOCIAL",
            "latex": "\\text{République française: } \\mathbf{Devise (Liberté, Égalité, Fraternité)} + \\mathbf{École \\text{ } gratuite \\text{ } et \\text{ } laïque} + \\mathbf{Sécurité \\text{ } sociale}",
            "legend": "• Pernyataan 1: Moto resmi republik (Benar).<br>• Pernyataan 2: Sécurité sociale justru menanggung biaya medis (Salah).<br>• Pernyataan 3: Sesuai undang-undang Jules Ferry (Benar).<br>• Pernyataan 4: Pilar laïcité konstitusional (Benar)."
        },
        "hints": {
            "concept": "1) Moto resmi Prancis adalah Liberté, Égalité, Fraternité (Benar). 2) Carte Vitale dan Sécurité sociale menanggung sebagian besar atau seluruh biaya medis pasien rentan (Salah). 3) Sekolah negeri gratis dan wajib sejak era Jules Ferry (Benar). 4) Laïcité menjamin kebebasan hati nurani dan netralitas negara (Benar).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "fra-sim-34",
        "type": "matrix",
        "materi": "MULTIKOMPETENSI MATRIKS: SINTAKSIS DAN KEDUDUKAN PRONOMINA",
        "topic": "Validitas Aturan Sintaksis Posisi Pronomina Objek dalam Ragam Kalimat Prancis",
        "stem": "Penempatan kata ganti komplemen (COD, COI, y, en) diatur oleh hukum sintaksis yang sangat ketat. Tentukan kebenaran masing-masing kaidah penempatan pronomina berikut (Benar atau Salah):",
        "statements": [
            {
                "text": "Dalam kalimat indikatif bentuk sekarang biasa, pronomina objek selalu ditempatkan SEBELUM kata kerja yang dikonjugasikan (contoh: Je le vois).",
                "correct": "Benar"
            },
            {
                "text": "Dalam kalimat perintah positif (Impératif affirmatif), pronomina objek ditempatkan SETELAH kata kerja dengan tanda hubung (contoh: Donne-moi ce livre!).",
                "correct": "Benar"
            },
            {
                "text": "Dalam kalimat perintah negatif (Impératif négatif), pronomina objek diletakkan setelah kata kerja utama tanpa partikel ne.",
                "correct": "Salah"
            },
            {
                "text": "Bila ada kombinasi pronomina adverbial y dan en di depan satu kata kerja, pronomina y selalu mendahului pronomina en (contoh: Il y en a).",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "SYNTAXE DES PRONOMS: INDICATIF VS IMPÉRATIF",
            "latex": "\\text{Indicatif: } \\mathbf{Pronom} + \\mathbf{Verbe} \\quad | \\quad \\text{Impératif positif: } \\mathbf{Verbe} + \\mathbf{trait \\text{ } d'union} + \\mathbf{Pronom}",
            "legend": "• Kalimat afirmatif: Je le vois (Benar).<br>• Impératif positif: Donne-moi (Benar).<br>• Impératif negatif: Pronomina KEMBALI ke depan verba: Ne me donne pas! (Pernyataan 3 Salah).<br>• Urutan y + en: selalu y en (Benar)."
        },
        "hints": {
            "concept": "1) Sebelum verba pada indikatif: Je le vois (Benar). 2) Setelah verba dengan tanda hubung pada kalimat perintah positif: Donne-moi (Benar). 3) Pada kalimat perintah negatif, pronomina KEMBALI ke depan kata kerja (Ne me donne pas!) sehingga pernyataan 3 Salah. 4) Urutan 'y en' selalu mendahulukan y (Benar).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    },
    {
        "id": "fra-sim-35",
        "type": "matrix",
        "materi": "MULTIKOMPETENSI MATRIKS: ANALISIS KARYA SASTRA DAN PEMIKIRAN KRITIS",
        "topic": "Validitas Pemikiran Filosofis Zaman Pencerahan Prancis (Les Lumières)",
        "stem": "Gerakan filsafat Pencerahan abad ke-18 (*Les Lumières*) di Prancis telah meletakkan pilar-pilar peradaban modern dunia. Tentukan kebenaran masing-masing pernyataan pemikiran filosofis berikut (Benar atau Salah):",
        "statements": [
            {
                "text": "Montesquieu dalam karyanya 'De l'esprit des lois' merumuskan teori pemisahan tiga kekuasaan negara (legislatif, eksekutif, dan yudikatif) guna mencegah tirani.",
                "correct": "Benar"
            },
            {
                "text": "Voltaire adalah pendukung fanatik pengadilan inkuisisi dan penindasan kebebasan berbicara.",
                "correct": "Salah"
            },
            {
                "text": "Denis Diderot dan Jean d'Alembert memimpin proyek penyusunan 'L'Encyclopédie' untuk menghimpun ilmu pengetahuan ilmiah dan membebaskan masyarakat dari takhayul.",
                "correct": "Benar"
            },
            {
                "text": "Jean-Jacques Rousseau dalam 'Du contrat social' menegaskan bahwa kedaulatan tertinggi suatu negara berada di tangan rakyat (souveraineté populaire).",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "LES GRANDS APPORTS DES LUMIÈRES",
            "latex": "\\text{Montesquieu: Séparation des pouvoirs} \\quad | \\quad \\text{Diderot: L'Encyclopédie} \\quad | \\quad \\text{Rousseau: Souveraineté du peuple}",
            "legend": "• Montesquieu: Trias Politika (Benar).<br>• Voltaire: Tokoh pejuang toleransi dan penentang fanatisme (Pernyataan 2 Salah).<br>• Diderot & d'Alembert: Ensiklopedia sains (Benar).<br>• Rousseau: Kedaulatan rakyat (Benar)."
        },
        "hints": {
            "concept": "1) Montesquieu merumuskan pemisahan kekuasaan negara (Benar). 2) Voltaire justru merupakan musuh utama inkuisisi dan pejuang toleransi sejati (Salah). 3) Diderot dan d'Alembert menyusun L'Encyclopédie untuk menyebarkan sains (Benar). 4) Rousseau menegaskan kedaulatan berada di tangan rakyat melalui Kontrak Sosial (Benar).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    }
]
