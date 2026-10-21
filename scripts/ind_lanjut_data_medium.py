# -*- coding: utf-8 -*-
"""
ind_lanjut_data_medium.py
25 Authentic Medium Items for TKA 2026 Bahasa Indonesia Tingkat Lanjut (SMA/MA Fase F Lanjutan).
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik Kemendikdasmen.
Topics: Resepsi Sastra (Hans Robert Jauss), Model Argumen Toulmin, Analisis Framing Entman,
Pragmatik Kesantunan Leech, Ekokritik, Poskolonial Sastra, Rekonstruksi Kalimat Akademik Rancu.
"""

IND_LANJUT_MEDIUM_ITEMS = [
    {
        "id": "ind_lanjut-lat-m-01",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Teori Resepsi Sastra & Cakrawala Harapan (Jauss)",
        "stem": "Dalam estetika resepsi yang dikembangkan oleh Hans Robert Jauss, penerimaan pembaca terhadap suatu karya sastra baru senantiasa ditentukan oleh kerangka acuan awal pembaca berupa pengalaman membaca teks-teks terdahulu, norma estetika zamannya, serta pemahaman budaya yang dimilikinya. Konsep kerangka acuan awal pembaca ini dalam terminologi Jauss disebut...",
        "correct": "cakrawala harapan (horizon of expectations)",
        "distractors": [
            "jarak estetis (aesthetic distance)",
            "pembaca implisit (implied reader)",
            "katarsis dramatik (dramatic catharsis)",
            "kesadaran kolektif struktural (genetic consciousness)"
        ],
        "formula": {
            "title": "TEORI RESEPSI HANS ROBERT JAUSS",
            "latex": "\\text{Horizon of Expectations} \\iff \\text{Sistem acuan pra-pemahaman pembaca terhadap konvensi sastra}",
            "legend": "• Pergeseran horizon ekspektasi terjadi saat karya menyimpang dari konvensi sastra konvensional sezamannya"
        },
        "hints": {
            "concept": "Jauss menekankan peran historis pembaca dalam merekonstruksi makna karya sastra melalui konsep 'Erwartungshorizont'.",
            "execution": "Istilah baku untuk konsep pra-pemahaman pembaca menurut Jauss adalah cakrawala harapan (horizon of expectations)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-02",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Komponen Argumen Stephen Toulmin (Warrant)",
        "stem": "Perhatikan konstruksi argumen kebijakan berikut:<br><em>Klaim: Pemerintah kota wajib memberlakukan pajak emisi progresif bagi kendaraan bermotor pribadi di pusat kota.<br>Data: Tingkat partikulat PM2.5 di pusat kota meningkat 48% selama jam berangkat kerja dan menyebabkan lonjakan kasus infeksi saluran pernapasan akut (ISPA) anak.<br>Pernyataan Jembatan: Pengenaan disinsentif finansial pada sektor penyumbang emisi terbukti secara empiris mengubah preferensi mobilitas masyarakat ke transportasi massal ramah lingkungan.</em><br>Dalam model argumentasi Stephen Toulmin, pernyataan jembatan yang menghubungkan antara data empiris dengan klaim kebijakan tersebut berfungsi sebagai...",
        "correct": "warrant (penjamin keabsahan logika hubungan data ke klaim)",
        "distractors": [
            "backing (dukungan otoritas data sekunder lanjutan)",
            "rebuttal (kondisi penyangkalan atau pengecualian)",
            "qualifier (pembatas modalitas probabilitas argumen)",
            "grounds (fakta mentah bukti observasi langsung)"
        ],
        "formula": {
            "title": "MODEL ARGUMENTASI TOULMIN",
            "latex": "\\text{Data} \\xrightarrow{\\text{Warrant}} \\text{Claim} \\quad (\\text{didukung oleh Backing})",
            "legend": "• Warrant merupakan prinsip jembatan rasional yang menjelaskan mengapa data relevan untuk membuktikan klaim"
        },
        "hints": {
            "concept": "Dalam model Toulmin, komponen pembangun argumen meliputi: Claim, Data/Grounds, Warrant, Backing, Qualifier, dan Rebuttal.",
            "execution": "Pernyataan yang berfungsi sebagai prinsip umum penjamin bahwa data membenarkan klaim adalah Warrant."
        }
    },
    {
        "id": "ind_lanjut-lat-m-03",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Model Pembingkaian Wacana Robert Entman",
        "stem": "Robert Entman merumuskan empat elemen fungsional dalam analisis pembingkaian teks media (*framing analysis*): *define problems, diagnose causes, make moral judgments,* dan *suggest remedies*. Jika dalam sebuah artikel berita dinyatakan: <em>'Krisis banjir bandang di kawasan hulu terjadi akibat maraknya alih fungsi lahan resapan air menjadi vila komersial ilegal tanpa amdal'</em>, maka kutipan tersebut secara dominan merepresentasikan elemen...",
        "correct": "diagnose causes (mendiagnosis faktor penyebab masalah)",
        "distractors": [
            "define problems (mendefinisikan apa hakikat masalahnya)",
            "make moral judgments (memberikan justifikasi moral etis)",
            "suggest remedies (merekomendasikan tawaran solusi konkret)",
            "predict outcomes (meramalkan konsekuensi masa depan)"
        ],
        "formula": {
            "title": "4 ELEMEN FRAMING ROBERT ENTMAN",
            "latex": "\\text{Diagnose Causes} \\iff \\text{Mengidentifikasi aktor atau kekuatan penyebab timbulnya masalah}",
            "legend": "• Alih fungsi lahan ilegal tanpa amdal ditunjuk secara eksplisit sebagai kausa banjir bandang"
        },
        "hints": {
            "concept": "Entman membagi framing menjadi: definisi masalah, diagnosis kausalitas/penyebab, penilaian moralitas, dan anjuran penyelesaian.",
            "execution": "Kutipan menjelaskan 'mengapa' banjir terjadi (alih fungsi lahan), yang merupakan diagnosis penyebab (diagnose causes)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-04",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Prinsip Kesantunan Berbahasa Leech (Maksim Kerendahan Hati)",
        "stem": "Dalam teori kesantunan berbahasa Geoffrey Leech, seorang pemakalah seminar menjawab pujian moderator atas keberhasilan penelitiannya dengan ujaran: <em>'Ah, makalah ini masih sangat sederhana dan penuh keterbatasan. Keberhasilan penelitian ini sepenuhnya berkat arahan luar biasa dari para dosen pembimbing dan ketekunan rekan-rekan laboratorium.'</em> Pemakalah tersebut mematuhi prinsip kesantunan berbahasa, khususnya maksim...",
        "correct": "kerendahan hati / kerendahan diri (modesty maxim)",
        "distractors": [
            "kearifan / kebijaksanaan (tact maxim)",
            "kedermawanan / kemurahan (generosity maxim)",
            "pujian / penghargaan (approbation maxim)",
            "kesepakatan / kecocokan (agreement maxim)"
        ],
        "formula": {
            "title": "PRINSIP KESANTUNAN BERBAHASA LEECH",
            "latex": "\\text{Maksim Kerendahan Hati} \\iff \\text{Minimalkan pujian pada diri sendiri; maksimalkan celaan pada diri sendiri}",
            "legend": "• Menolak klaim kehebatan diri sendiri dan mengatribusikan keberhasilan kepada pihak lain"
        },
        "hints": {
            "concept": "Leech merumuskan 6 maksim kesantunan: Kebijaksanaan, Kedermawanan, Pujian, Kerendahan Hati, Kesepakatan, dan Simpati.",
            "execution": "Meminimalkan pujian terhadap diri sendiri dan menonjolkan keterbatasan merupakan ciri maksim kerendahan hati (modesty)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-05",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Pendekatan Ekokritik Sastra",
        "stem": "Kritik sastra kontemporer yang menganalisis relasi timbal balik antara manusia dan lingkungan alam dalam karya sastra, menentang paradigma antroposentrisme yang eksploitatif, serta mempromosikan kesadaran biosentrisme atau ekosentrisme dikenal sebagai kritik...",
        "correct": "ekokritik (ecocriticism)",
        "distractors": [
            "psikoanalisis Jungian",
            "formalisme baru (new criticism)",
            "strukturalisme naratologi Genette",
            "filologi teks naskah kuno"
        ],
        "formula": {
            "title": "PARADIGMA EKOKRITIK SASTRA (GLOTFELTY/BUELL)",
            "latex": "\\text{Ekokritik} \\iff \\text{Studi interkoneksi sastra & lingkungan fisik biosfer}",
            "legend": "• Menggugat dominasi antroposentrisme dan mengangkat eksploitasi alam sebagai isu sentral teks"
        },
        "hints": {
            "concept": "Ekokritik mempelajari bagaimana alam dan krisis ekologis direpresentasikan dalam karya sastra.",
            "execution": "Pilihlah istilah ekokritik (ecocriticism) yang fokus pada relasi manusia dan biosfer."
        }
    },
    {
        "id": "ind_lanjut-lat-m-06",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Kritik Poskolonialisme (Edward Said & Homi Bhabha)",
        "stem": "Telaah kritik sastra terhadap novel berlatar era kolonial Hindia Belanda yang mengungkap bagaimana teks sastra melanggengkan stereotip inferioritas masyarakat pribumi sebagai bangsa yang malas, irasional, dan pasif di hadapan hegemoni penjajah Barat yang diposisikan rasional dan superior menerapkan teori...",
        "correct": "poskolonialisme (orientalisme Edward Said)",
        "distractors": [
            "dekonstruksi linguistik Derrida",
            "fenomenologi persepsi Merleau-Ponty",
            "strukturalisme semiotika Saussure",
            "marxisme ortodoks determinisme ekonomi murni"
        ],
        "formula": {
            "title": "TEORI POSKOLONIALISME EDWARD SAID",
            "latex": "\\text{Orientalisme} \\iff \\text{Wacana Barat yang mengonstruksi Timur sebagai 'Liyan' (Other) yang inferior}",
            "legend": "• Mengkaji hegemoni kultural dan representasi kuasa biner kolonial-terjajah dalam karya sastra"
        },
        "hints": {
            "concept": "Teori poskolonial (khususnya Orientalisme Edward Said) membongkar konstruksi biner Barat superior vs Timur inferior dalam teks.",
            "execution": "Gunakan pendekatan poskolonialisme (postcolonial criticism)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-07",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Rekonstruksi Kalimat Akademik yang Ambigu dan Rancu",
        "stem": "Perhatikan kalimat karya tulis ilmiah yang tidak efektif berikut:<br><em>'Berdasarkan hasil analisis data laboratorium yang mana telah dilakukan pengujian berkali-kali menunjukkan bahwa senyawa metabolit sekunder dapat menghambat proliferasi sel kanker.'</em><br>Kesalahan gramatikal mendasar pada kalimat tersebut beserta perbaikan terbaiknya adalah...",
        "correct": "Kalimat kehilangan subjek akibat pemakaian frasa preposisional 'Berdasarkan...' di awal kalimat yang dipadukan dengan klausa rancu 'yang mana'; perbaikan: 'Hasil analisis data laboratorium menunjukkan bahwa senyawa metabolit sekunder dapat menghambat proliferasi sel kanker.'",
        "distractors": [
            "Kalimat kekurangan predikat transitif; perbaikan: tambahkan kata 'adalah' di depan kata 'menunjukkan'.",
            "Penggunaan konjungsi 'bahwa' salah secara sintaksis; perbaikan: ganti kata 'bahwa' dengan kata 'jikalau'.",
            "Kata 'proliferasi' merupakan kata asing nonbaku; perbaikan: ganti dengan frasa 'pembelahan yang banyak'.",
            "Kalimat tersebut sudah efektif dan baku tanpa perlu mengalami perubahan struktur sintaksis apa pun."
        ],
        "formula": {
            "title": "REKONSTRUKSI KALIMAT BAKU AKADEMIK",
            "latex": "\\text{Salah: } \\text{Ket } + \\text{yang mana } + \\text{Predikat} \\implies \\text{Benar: } \\text{Subjek } (\\text{Hasil}) + \\text{Predikat } (\\text{menunjukkan})",
            "legend": "• Menghilangkan kalkir 'yang mana' dan menjamin adanya subjek gramatikal yang jelas"
        },
        "hints": {
            "concept": "Kalimat yang diawali 'Berdasarkan...' menjadi keterangan utuh. Jika setelah itu ada 'menunjukkan', kalimat menjadi tidak memiliki subjek (anakalut/rancu).",
            "execution": "Jadikan 'Hasil analisis data laboratorium' sebagai subjek langsung dengan membuang 'Berdasarkan' dan 'yang mana'."
        }
    },
    {
        "id": "ind_lanjut-lat-m-08",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy Post Hoc Ergo Propter Hoc",
        "stem": "Seorang komentator sosial menyatakan dalam sebuah artikel opini surat kabar:<br><em>'Tingkat kejahatan siber di daerah kita melonjak drastis tepat sebulan setelah pemerintah meresmikan fasilitas internet gratis di balai desa. Jelas sekali bahwa penyediaan fasilitas internet gratis itulah biang keladi utama peningkatan tindak pidana siber tersebut.'</em><br>Kesesatan penalaran (*logical fallacy*) yang terkandung dalam argumen komentator tersebut adalah...",
        "correct": "post hoc ergo propter hoc (menganggap peristiwa yang mendahului otomatis sebagai penyebab)",
        "distractors": [
            "ad populum (klaim kebenaran berdasarkan kesukaan khalayak umum)",
            "slippery slope (mengasumsikan efek domino kehancuran global)",
            "appeal to authority (mengutip tokoh yang tidak relevan kompetensinya)",
            "hasty generalization (generalisasi terburu-buru satu sampel)"
        ],
        "formula": {
            "title": "FALLACY POST HOC ERGO PROPTER HOC",
            "latex": "A \\text{ terjadi sebelum } B \\centernot\\implies A \\text{ adalah penyebab pasti bagi } B",
            "legend": "• Kesalahan menyimpulkan relasi kausalitas semata-mata dari urutan sekuensial waktu"
        },
        "hints": {
            "concept": "Post hoc ergo propter hoc mengasumsikan karena A terjadi sebelum B, maka A pasti merupakan penyebab B.",
            "execution": "Fasilitas internet gratis diresmikan sebelum kejahatan melonjak, namun urutan waktu tersebut bukan bukti kausalitas tanpa analisis variabel kontrol."
        }
    },
    {
        "id": "ind_lanjut-lat-m-09",
        "materi": "KOHESI & KOHERENSI WACANA",
        "topic": "Kohesi Gramatikal Referensi Anafora vs Katafora",
        "stem": "Perhatikan teks berikut:<br><em>'Karena <strong>ia</strong> memiliki dedikasi tinggi terhadap pelestarian terumbu karang, <strong>Dr. Sasmita</strong> dianugerahi penghargaan kalpataru nasional. Prestasi <strong>tersebut</strong> menginspirasi generasi muda pesisir.'</em><br>Hubungan referensi antara kata <em>'ia'</em> terhadap <em>'Dr. Sasmita'</em>, serta kata <em>'tersebut'</em> terhadap <em>'dianugerahi penghargaan kalpataru nasional'</em> berturut-turut merupakan referensi...",
        "correct": "katafora (rujukan ke depan) dan anafora (rujukan ke belakang)",
        "distractors": [
            "anafora (rujukan ke belakang) dan katafora (rujukan ke depan)",
            "deiksis spasial distal dan deiksis temporal absolut",
            "substitusi komparatif dan elipsis frasa verba",
            "repetisi epizeuksis dan referensi eksofora luar wacana"
        ],
        "formula": {
            "title": "DEMARKASI ANAFORA VS KATAFORA",
            "latex": "\\text{Katafora: } \\text{ia} \\to \\text{Dr. Sasmita (ke depan)}; \\quad \\text{Anafora: } \\text{Penghargaan} \\leftarrow \\text{tersebut (ke belakang)}",
            "legend": "• Katafora menunjuk anteseden di sebelah kanan; anafora menunjuk anteseden di sebelah kiri teks"
        },
        "hints": {
            "concept": "Katafora merujuk ke depan (anteseden disebut belakangan), anafora merujuk ke belakang (anteseden sudah disebutkan sebelumnya).",
            "execution": "'ia' muncul sebelum 'Dr. Sasmita' (katafora), sedangkan 'tersebut' merujuk ke peristiwa penghargaan yang sudah lewat (anafora)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-10",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Model Argumen Toulmin (Backing)",
        "stem": "Dalam kerangka argumen Toulmin, seorang peneliti merumuskan argumen:<br><em>Klaim: Kurikulum berbasis proyek terintegrasi harus segera diterapkan secara nasional.<br>Warrant: Pembelajaran berbasis proyek secara konsisten mengasah keterampilan pemecahan masalah kritis dan kolaborasi tim siswa.<br>Backing: Meta-analisis terhadap 120 riset empiris pendidikan global oleh Hattie (2023) menunjukkan effect size pembelajaran berbasis proyek mencapai 0,75 (kategori dampak sangat tinggi).</em><br>Fungsi utama komponen <em>Backing</em> dalam struktur argumen tersebut adalah...",
        "correct": "menyediakan bukti empiris, landasan teoretis, atau otoritas keilmuan untuk mendukung kebenaran prinsip warrant",
        "distractors": [
            "merumuskan bantahan langsung terhadap argumen lawan debat",
            "membatasi keberlakuan klaim hanya pada sekolah perkotaan",
            "mengubah klaim utama menjadi pertanyaan penelitian kualitatif",
            "menggantikan data mentah agar klaim tidak dapat dibantah sama sekali"
        ],
        "formula": {
            "title": "FUNGSI BACKING DALAM TOULMIN",
            "latex": "\\text{Backing} \\implies \\text{Support/Justification for the Warrant}",
            "legend": "• Backing menopang warrant agar jembatan logika antara data dan klaim memiliki validitas keilmuan yang kuat"
        },
        "hints": {
            "concept": "Backing adalah landasan pendukung yang menopang Warrant, biasanya berupa riset terdahulu, hukum ilmiah, atau data statistik.",
            "execution": "Pilih opsi yang menjelaskan peran Backing dalam memberikan bukti empiris/otoritas keilmuan bagi Warrant."
        }
    },
    {
        "id": "ind_lanjut-lat-m-11",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Implikatur Percakapan (Gricean Implicature)",
        "stem": "Perhatikan dialog singkat antara dua rekan dosen berikut:<br>Dosen A: <em>'Apakah artikel penelitian Pak Bowo layak untuk kita usulkan menerima dana hibah riset unggulan tahun ini?'</em><br>Dosen B: <em>'Tata letak sampul proposalnya sangat rapi dan jenis kertas yang digunakan berkualitas prima.'</em><br>Secara pragmatik, Dosen B melakukan pelanggaran maksim relevansi (*flouting the maxim of relation*) untuk menghasilkan implikatur percakapan bahwa...",
        "correct": "substansi ilmiah dan kualitas metodologi penelitian proposal tersebut kurang memadai atau kurang berbobot",
        "distractors": [
            "Pak Bowo adalah seorang desainer grafis profesional yang sangat kompeten",
            "proposal tersebut pasti lolos seleksi pendanaan karena sampulnya sangat elegan",
            "Dosen B tidak mendengar pertanyaan yang diajukan oleh Dosen A",
            "pendanaan hibah riset harus dialokasikan untuk membeli kertas berkualitas prima"
        ],
        "formula": {
            "title": "IMPLIKATUR PERCAKAPAN GRICE",
            "latex": "\\text{Flouting Maxim of Relevance} \\implies \\text{Menolak memuji substansi} \\to \\text{Makna tersirat negatif}",
            "legend": "• Menjawab pertanyaan kualitas riset hanya dengan memuji sampul kertas menyiratkan isi ilmiahnya mengecewakan"
        },
        "hints": {
            "concept": "Pelanggaran maksim (flouting) sengaja dilakukan penutur untuk memunculkan makna implisit (implikatur).",
            "execution": "Memuji tampilan fisik kertas saat ditanya kelayakan isi ilmiah secara implisit menyiratkan bahwa isinya tidak layak."
        }
    },
    {
        "id": "ind_lanjut-lat-m-12",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Analisis Semiotika Sastra (Roland Barthes)",
        "stem": "Dalam semiologi Roland Barthes, makna lapis pertama yang bersifat harfiah dan langsung menghubungkan penanda (*signifier*) dengan petanda (*signified*) disebut makna denotasi. Adapun sistem pemaknaan lapis kedua yang memuat muatan nilai kultural, ideologis, dan memproduksi mitos sosial disebut...",
        "correct": "konotasi (connotation)",
        "distractors": [
            "elipsis struktural",
            "sinkronisitas murni",
            "paradigma gramatikal",
            "fonologis artikulatoris"
        ],
        "formula": {
            "title": "SISTEM DUA TINGKAT BARTHEZ",
            "latex": "\\text{Lapis I: Denotasi} (Signifier + Signified) \\to \\text{Lapis II: Konotasi / Mitos (Myth)}",
            "legend": "• Konotasi Barthes menjadi wahana bagi penanaman ideologi dominan masyarakat"
        },
        "hints": {
            "concept": "Barthes membedakan signifikasi tingkat pertama (denotasi) dan signifikasi tingkat kedua (konotasi yang melahirkan mitos).",
            "execution": "Makna lapis kedua bermuatan ideologi kultural adalah konotasi (connotation)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-13",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Modalitas Epistemik dalam Kalimat Akademik",
        "stem": "Dalam wacana penulisan akademik, seorang peneliti harus bersikap cermat dan tidak menyampaikan klaim mutlak sebelum diverifikasi oleh bukti yang tak terbantahkan. Sikap kehati-hatian ini diwujudkan melalui penggunaan peranti pemagaran wacana (*hedging*) dengan modalitas epistemik. Kalimat berikut yang menggunakan modalitas epistemik bernuansa *hedging* ilmiah yang tepat adalah...",
        "correct": "Temuan empiris ini mengindikasikan adanya kecenderungan korelasi positif antara literasi digital dan resiliensi psikologis siswa.",
        "distractors": [
            "Data ini tanpa keraguan sedikit pun membuktikan bahwa semua siswa yang melek digital pasti tidak akan pernah stres.",
            "Sudah menjadi fakta mutlak yang tak terbantahkan bahwa literasi digital adalah satu-satunya penentu mental siswa.",
            "Penelitian ini secara mutlak menyangkal seluruh teori terdahulu mengenai ketahanan psikologis remaja.",
            "Kami menjamin seratus persen bahwa hasil penelitian kami berlaku di seluruh belahan bumi manapun."
        ],
        "formula": {
            "title": "HEDGING DALAM WACANA AKADEMIK",
            "latex": "\\text{Hedging} \\iff \\text{Kata penanda probabilitas: 'mengindikasikan', 'cenderung', 'tampaknya'}",
            "legend": "• Menjaga integritas peneliti dari overklaim yang tidak terbukti secara universal"
        },
        "hints": {
            "concept": "Hedging (pemagaran ilmiah) menggunakan verba epistemik seperti 'mengindikasikan', 'berpotensi', 'cenderung' agar tidak terjadi overgeneralisasi.",
            "execution": "Cari kalimat yang memakai frasa 'mengindikasikan adanya kecenderungan'."
        }
    },
    {
        "id": "ind_lanjut-lat-m-14",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy Red Herring",
        "stem": "Perhatikan perdebatan kebijakan berikut:<br>Wartawan: <em>'Bagaimana tanggapan Bapak Menteri terkait temuan Badan Pemeriksa Keuangan mengenai indikasi kebocoran anggaran pengadaan infrastruktur server sebesar 30 miliar rupiah?'</em><br>Menteri: <em>'Kita harus menyadari bahwa bangsa kita adalah bangsa yang besar dan ramah tamah. Pekan lalu tim sepak bola nasional kita meraih kemenangan bersejarah yang membanggakan seluruh rakyat dari Sabang sampai Merauke.'</em><br>Strategi pengalihan isu yang dilakukan oleh Menteri tersebut merupakan bentuk kesesatan berpikir...",
        "correct": "red herring (mengalihkan topik ke isu populer yang tidak relevan sama sekali)",
        "distractors": [
            "ad misericordiam (memohon belas kasihan emosional)",
            "circular reasoning (menjawab secara berputar-putar tautologis)",
            "false dilemma (mempersempit opsi menjadi dua kutub)",
            "slippery slope (menghubungkan runtutan bencana hipotetis)"
        ],
        "formula": {
            "title": "FALLACY RED HERRING",
            "latex": "\\text{Pertanyaan Isu A (Anggaran)} \\xrightarrow{\\text{Alihkan}} \\text{Topik Isu B (Sepak Bola Populer)}",
            "legend": "• Menghindari substansi masalah kritis dengan melemparkan isu emosional/populer yang tidak berkaitan"
        },
        "hints": {
            "concept": "Red herring adalah teknik mengalihkan perhatian audiens dari topik perdebatan utama ke topik lain yang tidak relevan namun menarik minat publik.",
            "execution": "Menjawab kebocoran anggaran dengan kemenangan sepak bola adalah contoh klasik red herring."
        }
    },
    {
        "id": "ind_lanjut-lat-m-15",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Pendekatan Dekonstruksi Sastra (Jacques Derrida)",
        "stem": "Pendekatan kritik sastra pascastrukturalis yang menolak kemapanan makna tunggal (*center/logos*), mengungkap kontradiksi internal atau aporia di dalam teks, serta mendemonstrasikan bahwa oposisi biner tradisional (seperti benar/salah, alam/budaya, pria/wanita) dalam karya sastra senantiasa tidak stabil dan saling mendekonstruksi diri digagas oleh...",
        "correct": "Jacques Derrida",
        "distractors": [
            "Ferdinand de Saussure",
            "Roman Jakobson",
            "Claude Levi-Strauss",
            "Terry Eagleton"
        ],
        "formula": {
            "title": "TEORI DEKONSTRUKSI DERRIDA",
            "latex": "\\text{Aporia} \\implies \\text{Ketidakstabilan makna teks & penolakan logosentrisme}",
            "legend": "• Membongkar hierarki oposisi biner untuk menunjukkan bahwa teks membatalkan klaim maknanya sendiri"
        },
        "hints": {
            "concept": "Dekonstruksi (deconstruction) diasosiasikan dengan filsuf Prancis Jacques Derrida.",
            "execution": "Pilih Jacques Derrida sebagai tokoh dekonstruksi sastra dan pembongkaran logosentrisme."
        }
    },
    {
        "id": "ind_lanjut-lat-m-16",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Struktur Pembahasan (Discussion) dan Implikasi Riset",
        "stem": "Dalam menuliskan subbab Pembahasan (*Discussion*) sebuah penelitian eksperimental, seorang penulis menemukan bahwa efektivitas katalis zeolit alam yang diujinya lebih rendah 15% dibandingkan dengan temuan penelitian terdahulu oleh Smith et al. (2022). Tindakan penulisan akademik yang paling etis, ilmiah, dan berbobot dalam menyikapi anomali tersebut adalah...",
        "correct": "Menyajikan data apa adanya, menguraikan potensi faktor pembeda metodologis (seperti suhu kalsinasi atau kemurnian sampel), dan mendiskusikan batasan studi tersebut secara transparan.",
        "distractors": [
            "Mengubah angka data mentah agar hasil pengujian tampak identik dan selaras dengan temuan Smith et al.",
            "Menghapus sitasi penelitian Smith et al. dari daftar pustaka agar tidak tampak ada perbedaan temuan ilmiah.",
            "Menyalahkan kualitas alat laboratorium lokal secara emosional tanpa bukti kalibrasi yang sahih.",
            "Mengabaikan anomali tersebut dan hanya membahas variabel-variabel lain yang sesuai dengan hipotesis awal."
        ],
        "formula": {
            "title": "INTEGRITAS PEMBAHASAN AKADEMIK",
            "latex": "\\text{Anomali Data} \\implies \\text{Eksplorasi Variabel Perancu (Confounding Variables)} + \\text{Diskusi Batasan}",
            "legend": "• Menolak falsifikasi/fabrikasi data dan menjunjung tinggi transparansi metodologi ilmiah"
        },
        "hints": {
            "concept": "Integritas akademik menuntut keterbukaan terhadap disparitas data dan eksplorasi ilmiah atas faktor penyebabnya.",
            "execution": "Pilih opsi yang menyajikan data jujur dan mengkaji perbedaan kondisi metodologis secara ilmiah."
        }
    },
    {
        "id": "ind_lanjut-lat-m-17",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Tindak Tutur Komisif",
        "stem": "Perhatikan ujaran seorang calon ketua organisasi siswa dalam sidang debat terbuka:<br><em>'Jika para siswa memberikan amanah kepemimpinan kepada saya, saya berjanji akan menyediakan ruang konsultasi konseling sebaya dan memperjuangkan keterbukaan anggaran kegiatan ekstrakurikuler setiap bulan.'</em><br>Ditinjau dari klasifikasi tindak tutur John Searle, ujaran tersebut secara dominan merupakan tindak tutur...",
        "correct": "komisif (commissives)",
        "distractors": [
            "asertif faktual (assertives)",
            "direktif perintah (directives)",
            "ekspresif emosi (expressives)",
            "deklarasi institusional (declarations)"
        ],
        "formula": {
            "title": "TINDAK TUTUR KOMISIF SEARLE",
            "latex": "\\text{Komisif} \\iff \\text{Mengikat penutur pada tindakan di masa depan (janji, sumpah, tekad)}",
            "legend": "• Ujaran janji (promise) berkomitmen mengubah perilaku penutur untuk melakukan sesuatu di masa mendatang"
        },
        "hints": {
            "concept": "Tindak tutur komisif adalah ujaran yang mengikat penutur untuk melakukan sesuatu di masa depan (misal: berjanji, bernazar, menjamin).",
            "execution": "Kata kunci 'saya berjanji akan menyediakan...' menandai tindak tutur komisif."
        }
    },
    {
        "id": "ind_lanjut-lat-m-18",
        "materi": "KOHESI & KOHERENSI WACANA",
        "topic": "Koherensi Wacana Hubungan Konsesif",
        "stem": "Perhatikan pasangan klausa berikut:<br><em>[Klausa 1] Anggaran belanja riset dan pengembangan universitas mengalami rasionalisasi pemotongan sebesar 15%.<br>[Klausa 2] Publikasi artikel ilmiah dosen di jurnal bereputasi global justru mengalami lonjakan sebesar 20%.</em><br>Hubungan koherensi logis antarklausa di atas adalah hubungan...",
        "correct": "konsesif / perlawanan tak terduga (concessive relation)",
        "distractors": [
            "kausalitas deterministik langsung",
            "aditif penambahan linier setara",
            "temporal kronologis berurutan",
            "spasial tata ruang letak geografis"
        ],
        "formula": {
            "title": "HUBUNGAN WACANA KONSESIF",
            "latex": "\\text{Konsesif} \\iff \\text{Peristiwa B tetap terjadi meskipun terdapat hambatan pada Peristiwa A}",
            "legend": "• Anggaran dipotong (hambatan) tetapi publikasi justru melonjak (hasil bertentangan dengan ekspektasi umum)"
        },
        "hints": {
            "concept": "Hubungan konsesif menyatakan suatu peristiwa tetap terjadi meskipun ada kondisi yang berlawanan atau menghalangi.",
            "execution": "Pemotongan anggaran umumnya menurunkan publikasi, namun di sini publikasi melonjak (perlawanan konsesif)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-19",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Gaya Retorika Ironi Dramatik",
        "stem": "Dalam struktur naratif sebuah drama teater atau cerpen fiksi, situasi di mana pembaca atau penonton mengetahui suatu fakta krusial masa lalu atau kebenaran rahasia yang sama sekali belum disadari oleh tokoh utama di panggung cerita dinamakan...",
        "correct": "ironi dramatik (dramatic irony)",
        "distractors": [
            "ironi verbal (sarkasme tuturan)",
            "ironi situasional murni",
            "deus ex machina penyelamat alur",
            "foreshadowing eksplisit langsung"
        ],
        "formula": {
            "title": "TIPOLOGI IRONI NARATOLOGI",
            "latex": "\\text{Penonton Tahu} > \\text{Karakter Tokoh Tahu} \\implies \\text{Ironi Dramatik}",
            "legend": "• Menciptakan ketegangan psikologis dramatis karena audiens mengantisipasi kejatuhan sang tokoh"
        },
        "hints": {
            "concept": "Ironi dramatik terjadi ketika audiens memiliki informasi lebih lengkap dibanding tokoh dalam cerita.",
            "execution": "Kondisi penonton tahu rahasia yang tidak diketahui tokoh disebut ironi dramatik (dramatic irony)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-20",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy False Dilemma (Dikotomi Palsu)",
        "stem": "Perhatikan ujaran seorang politisi dalam rapat koordinasi penataan kota:<br><em>'Pilihan kita sekarang sangat sederhana dan gamblang: kita menyetujui seluruh proyek reklamasi pantai ini tanpa syarat, atau kota kita akan tertinggal selamanya dan tenggelam dalam kemiskinan ekstrem.'</em><br>Kesesatan bernalar (*logical fallacy*) yang digunakan untuk memaksa audiens menyetujui kebijakan tersebut adalah...",
        "correct": "false dilemma / false dichotomy (membatasi pilihan hanya pada dua kutub ekstrem)",
        "distractors": [
            "ad verecundiam (berlindung di balik nama tokoh besar)",
            "post hoc ergo propter hoc (kausalitas kronologis semu)",
            "slippery slope (loncatan asumsi bencana domino)",
            "bandwagon fallacy (mengikuti arus massa mayoritas)"
        ],
        "formula": {
            "title": "FALLACY FALSE DILEMMA",
            "latex": "P \\lor Q \\text{ diasumsikan mutlak padahal masih ada opsi } R, S, T",
            "legend": "• Menutup alternatif kompromi penataan lingkungan dengan memaksakan biner hitam-putih"
        },
        "hints": {
            "concept": "False dilemma membatasi masalah kompleks menjadi dua pilihan hitam-putih ekstrem, padahal terdapat banyak solusi alternatif.",
            "execution": "Pilihan 'setuju reklamasi penuh' ATAU 'tenggelam dalam kemiskinan' adalah dikotomi palsu (false dilemma)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-21",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Sintesis Integratif Multirujukan",
        "stem": "Perhatikan data temuan penelitian berikut:<br>1. <em>Nugroho (2022): Gamifikasi digital meningkatkan motivasi belajar intrinsik siswa sekolah menengah sebesar 35%.</em><br>2. <em>Lestari (2024): Penerapan elemen gim kompetitif tanpa pendampingan afektif guru justru memicu kecemasan akademik pada 28% siswa pemalu.</em><br>Kalimat sintesis integratif yang paling tepat, berimbang, dan bernas untuk merangkum kedua temuan di atas dalam kajian pustaka adalah...",
        "correct": "Meskipun gamifikasi digital terbukti signifikan meningkatkan motivasi belajar intrinsik (Nugroho, 2022), penerapannya menuntut mediasi afektif guru untuk memitigasi risiko kecemasan pada peserta didik tertentu (Lestari, 2024).",
        "distractors": [
            "Nugroho (2022) dan Lestari (2024) sama-sama meneliti gim sekolah dan menemukan hasil yang sama persis tentang keunggulan teknologi.",
            "Penelitian Nugroho (2022) salah besar karena telah dibantah secara mutlak oleh hasil riset Lestari (2024) yang lebih mutakhir.",
            "Gamifikasi digital sebaiknya dilarang total di sekolah karena temuan Lestari (2024) membuktikan teknologi merusak mental siswa.",
            "Nugroho (2022) menyatakan motivasi naik 35%, lalu Lestari (2024) menambahkan bahwa siswa pemalu suka bermain gim di sekolah."
        ],
        "formula": {
            "title": "TEKNIK SINTESIS INTEGRATIF AKADEMIK",
            "latex": "\\text{Tesis Positif (A)} + [\\text{Konjungsi Konsesif / Transisi Dialektis}] + \\text{Kondisi Batasan (B)}",
            "legend": "• Sintesis berbobot menggabungkan polaritas temuan menjadi wawasan komparatif yang utuh dan dialektis"
        },
        "hints": {
            "concept": "Sintesis akademik mengintegrasikan kedua temuan secara dialektis tanpa membuang salah satu fakta.",
            "execution": "Gunakan struktur konsesif: mengakui peningkatan motivasi (Nugroho) sekaligus menggarisbawahi pentingnya mediasi guru (Lestari)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-22",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Tipologi Narator Genette (Heterodiegetik vs Homodiegetik)",
        "stem": "Dalam teori naratologi Gerard Genette, pencerita (*narrator*) yang berada di luar dunia cerita dan tidak pernah mengambil bagian sebagai tokoh atau pelaku peristiwa di dalam dunia fiksi tersebut dinamakan narator...",
        "correct": "heterodiegetik (narator sudut pandang orang ketiga pengamat/mahatahu)",
        "distractors": [
            "homodiegetik (narator yang bertindak sebagai tokoh cerita)",
            "autodiegetik (narator yang menjadi tokoh utama biografisnya sendiri)",
            "intradiegetik (tokoh dalam cerita yang menceritakan cerita lain)",
            "ekstradiegetik murni tanpa fokalitas naratif"
        ],
        "formula": {
            "title": "TIPOLOGI NARATOR GERARD GENETTE",
            "latex": "\\text{Heterodiegetik} \\iff \\text{Narator berada di luar diegesis (dunia cerita)}",
            "legend": "• Berbeda dari homodiegetik di mana narator hadir langsung sebagai pelaku peristiwa cerita"
        },
        "hints": {
            "concept": "Genette membagi tingkat kehadiran narator dalam diegesis: Homodiegetik (di dalam cerita) dan Heterodiegetik (di luar cerita).",
            "execution": "Narator yang tidak terlibat sebagai pelaku peristiwa adalah narator heterodiegetik."
        }
    },
    {
        "id": "ind_lanjut-lat-m-23",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Pembedaan Fakta, Opini, dan Asumsi dalam Teks Editorial",
        "stem": "Perhatikan kutipan teks editorial surat kabar nasional berikut:<br><em>(1) Badan Pusat Statistik mencatat surplus neraca perdagangan Indonesia pada bulan Maret 2026 mencapai 4,2 miliar dolar AS.<br>(2) Keberhasilan surplus ini disinyalir merupakan kado manis dari lonjakan harga komoditas nikel global.<br>(3) Langkah hilirisasi industri mineral yang digalakkan pemerintah dinilai sebagai strategi paling visioner dalam dekade ini.<br>(4) Namun, apabila pengawasan dampak lingkungan tidak diperketat, industri ini berpotensi menuai krisis ekologis parah di masa mendatang.</em><br>Kalimat yang memuat **fakta objektif empiris** dan kalimat yang memuat **asumsi prediktif bersyarat** berturut-turut ditandai oleh nomor...",
        "correct": "(1) dan (4)",
        "distractors": [
            "(2) dan (3)",
            "(1) dan (3)",
            "(2) dan (4)",
            "(3) dan (4)"
        ],
        "formula": {
            "title": "TIPOLOGI PERNYATAAN WACANA",
            "latex": "(1) = \\text{Fakta Terverifikasi BPS}; \\quad (4) = \\text{Asumsi Prediktif Bersyarat ('apabila...', 'berpotensi...')}",
            "legend": "• Kalimat (2) opini interpretatif ('disinyalir'); (3) opini evaluatif subjektif ('paling visioner')"
        },
        "hints": {
            "concept": "Fakta objektif memuat data kuantitatif dari lembaga resmi yang dapat diverifikasi (1). Asumsi prediktif bersyarat memuat proyeksi kemungkinan bersyarat (4).",
            "execution": "Pilih pasangan (1) dan (4)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-24",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Kesantunan Berbahasa Maksim Kedermawanan (Leech)",
        "stem": "Seorang tuan rumah berkata kepada tamunya yang kehujanan: <em>'Silakan kenakan jaket hangat saya ini dan biarkan baju Anda yang basah saya jemurkan di dekat pemanas.'</em> Berdasarkan teori kesantunan Geoffrey Leech, ujaran tuan rumah tersebut mematuhi maksim...",
        "correct": "kedermawanan / kemurahan (generosity maxim: meminimalkan keuntungan diri, memaksimalkan kerugian diri)",
        "distractors": [
            "kebijaksanaan (tact maxim: meminimalkan kerugian lawan bicara)",
            "pujian (approbation maxim: memuji lawan bicara secara verbal)",
            "kerendahan hati (modesty maxim: merendahkan diri sendiri)",
            "kesepakatan (agreement maxim: menyepakati pendapat)"
        ],
        "formula": {
            "title": "MAKSIM KEDERMAWANAN LEECH",
            "latex": "\\text{Maksim Kedermawanan} \\iff \\text{Minimalkan keuntungan diri sendiri; maksimalkan beban diri sendiri demi menolong}",
            "legend": "• Menawarkan pakaian sendiri dan mencucikan baju tamu mengorbankan kenyamanan diri demi melayani tamu"
        },
        "hints": {
            "concept": "Maksim kedermawanan berpusat pada penutur yang bersedia menanggung beban/repot demi memberi kemudahan bagi orang lain.",
            "execution": "Tuan rumah menawarkan jaketnya sendiri dan bersusah payah menjemurkan pakaian tamunya (maksim kedermawanan)."
        }
    },
    {
        "id": "ind_lanjut-lat-m-25",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Penulisan Batasan Masalah Penelitian (*Scope and Delimitation*)",
        "stem": "Dalam menyusun metodologi penelitian, fungsi esensial dari subbab Batasan Masalah (*Delimitations*) adalah...",
        "correct": "Menetapkan batasan parameter variabel, populasi sasaran, dan ruang lingkup geografis yang secara sadar dipilih oleh peneliti agar studi terfokus dan dapat diselesaikan secara mendalam.",
        "distractors": [
            "Menyembunyikan kelemahan desain penelitian dari penguji agar naskah tidak dibatalkan.",
            "Membatasi jumlah kata dalam artikel jurnal agar sesuai dengan ketentuan biaya percetakan.",
            "Menghindari pertanyaan kritis pembaca dengan menyatakan bahwa topik lain tidak penting.",
            "Mengurangi beban analisis data dengan hanya memilih responden yang memberikan jawaban positif."
        ],
        "formula": {
            "title": "DEFINISI DELIMITATIONS PENELITIAN",
            "latex": "\\text{Delimitations} \\iff \\text{Boundaries consciously set by researchers to narrow the research focus}",
            "legend": "• Berbeda dari Limitations (kelemahan tak terduga yang di luar kendali peneliti)"
        },
        "hints": {
            "concept": "Batasan masalah (delimitations) secara sadar dipasang oleh peneliti untuk menentukan parameter fokus studi.",
            "execution": "Pilih opsi yang menjelaskan penetapan batasan parameter variabel, populasi, dan ruang lingkup secara sadar."
        }
    }
]
