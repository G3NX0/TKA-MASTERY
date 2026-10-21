# -*- coding: utf-8 -*-
"""
ind_lanjut_data_hard.py
25 Authentic Hard Items for TKA 2026 Bahasa Indonesia Tingkat Lanjut (SMA/MA Fase F Lanjutan).
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik Kemendikdasmen.
Topics: Analisis Wacana Kritis (Fairclough & Van Dijk), Hermeneutika Ricoeur, Naratologi Genette (Fokalitas & Anakroni),
Teori Karnavalisasi & Polifoni Bakhtin, Systemic Functional Linguistics Halliday (Nominalisasi Gramatikal),
Teori Relevansi Sperber & Wilson, Logika Fallacy Kompleks (Equivocation, Petitio Principii).
"""

IND_LANJUT_HARD_ITEMS = [
    {
        "id": "ind_lanjut-lat-h-01",
        "materi": "ANALISIS WACANA KRITIS (AWK)",
        "topic": "Model Tiga Dimensi Norman Fairclough",
        "stem": "Dalam model Analisis Wacana Kritis (AWK) Norman Fairclough, wacana dianalisis melalui tiga dimensi yang saling berkelindan: dimensi teks (*textual analysis*), dimensi praktik diskursif (*discursive practice*), dan dimensi praktik sosial-budaya (*sociocultural practice*). Analisis yang membedah proses sirkulasi, produksi, konsumsi berita oleh redaksi media massa, serta intertekstualitas teks berada pada dimensi...",
        "correct": "praktik diskursif (discursive practice)",
        "distractors": [
            "analisis mikro linguistik tekstual",
            "praktik sosial-budaya makro institusional",
            "epistemologi strukturalisme genetis",
            "analisis semiotika visual denotatif murni"
        ],
        "formula": {
            "title": "DIMENSI WACANA FAIRCLOUGH",
            "latex": "\\text{Text} \\subset \\text{Discursive Practice (Produksi/Konsumsi)} \\subset \\text{Social Practice (Hegemoni)}",
            "legend": "• Praktik diskursif memediasi teks linguistik mikro dengan struktur sosial makro"
        },
        "hints": {
            "concept": "Fairclough membagi AWK menjadi 3 dimensi: Teks (linguistik), Praktik Diskursif (produksi, distribusi, konsumsi teks), dan Praktik Sosial (ideologi & kekuasaan).",
            "execution": "Proses produksi dan konsumsi teks oleh redaksi adalah dimensi praktik diskursif (discursive practice)."
        }
    },
    {
        "id": "ind_lanjut-lat-h-02",
        "materi": "ANALISIS WACANA KRITIS (AWK)",
        "topic": "Model Kognisi Sosial Teun A. van Dijk",
        "stem": "Teun A. van Dijk merumuskan struktur analisis wacana yang terdiri atas struktur makro, superstruktur, dan struktur mikro. Jika seorang peneliti mengkaji bagaimana seorang jurnalis memilih kosa kata metaforis (*stilistika*), menyusun kalimat aktif-pasif untuk mengaburkan pelaku kejahatan (*sintaksis*), serta mengatur detail informasi latar belakang (*semantik*), maka peneliti tersebut sedang membedah tingkatan...",
        "correct": "struktur mikro (analisis unsur-unsur lokal teks: semantik, sintaksis, stilistika, retorika)",
        "distractors": [
            "struktur makro (makna global tema utama teks wacana)",
            "superstruktur (skema atau alur kerangka penataan teks)",
            "kognisi sosial representasi mental wartawan",
            "konteks historis sosiologis era pra-kemerdekaan"
        ],
        "formula": {
            "title": "STRUKTUR WACANA TEUN A. VAN DIJK",
            "latex": "\\text{Struktur Mikro} \\iff \\text{Semantik (Latar, Detail)} + \\text{Sintaksis (Kohesi, Pasif)} + \\text{Stilistika (Leksikon)} + \\text{Retorika}",
            "legend": "• Mengungkap bagaimana ideologi disusupkan lewat pilihan gramatika dan leksikal mikro"
        },
        "hints": {
            "concept": "Van Dijk: Struktur makro = tema/topik global; Superstruktur = skematika bagan; Struktur mikro = semantik, sintaksis, stilistika, dan retorika.",
            "execution": "Pilihan kata, kalimat pasif, dan detail informasi merupakan ranah struktur mikro."
        }
    },
    {
        "id": "ind_lanjut-lat-h-03",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Tipologi Fokalitas Naratologi Gerard Genette",
        "stem": "Dalam sebuah novel psikologis, seluruh peristiwa diuraikan oleh narator orang ketiga, tetapi pembaca hanya memperoleh informasi peristiwa dan deskripsi lingkungan sejauh yang dapat diindera, dipikirkan, dan dirasakan oleh tokoh utama 'Raka'. Narator tidak pernah mengungkapkan isi batin tokoh-tokoh lain di sekitar Raka. Berdasarkan teori naratologi Gerard Genette, fokalitas yang diterapkan dalam novel tersebut adalah...",
        "correct": "fokalitas internal tetap (fixed internal focalization)",
        "distractors": [
            "fokalitas nol / mahatahu (zero focalization)",
            "fokalitas eksternal murni (external focalization)",
            "fokalitas internal ganda (multiple internal focalization)",
            "fokalitas variabel bergiliran (variable internal focalization)"
        ],
        "formula": {
            "title": "TIPOLOGI FOKALITAS GENETTE",
            "latex": "\\text{Narator Mengatakan} = \\text{Apa yang Tokoh Raka Ketahui} \\implies \\text{Fokalitas Internal Tetap}",
            "legend": "• Fokalitas nol: Narator tahu > Tokoh; Fokalitas eksternal: Narator tahu < Tokoh (hanya perilaku tampak)"
        },
        "hints": {
            "concept": "Genette: Fokalitas internal terjadi saat narasi disaring melalui kesadaran tokoh tertentu. Jika tokoh penyaringnya tetap satu, disebut fixed internal focalization.",
            "execution": "Peristiwa disaring hanya lewat persepsi dan batin tokoh Raka sepanjang cerita = fokalitas internal tetap."
        }
    },
    {
        "id": "ind_lanjut-lat-h-04",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Anakroni Naratologi: Analepsis vs Prolepsis",
        "stem": "Perhatikan kutipan novel berikut:<br><em>'Ketika melangkah menuju mimbar pelantikan rektor pagi itu, ingatan Farhan seketika melayang ke sebuah gubuk reot di tepi kali Brantas tiga puluh tahun silam, saat ia terpaksa belajar membaca di bawah temaram lampu minyak sambil menahan perih lambung yang kosong.'</em><br>Penyimpangan urutan waktu (*anachrony*) dari garis masa kini cerita primer ke masa lampau tokoh dalam terminologi naratologi Genette dinamakan...",
        "correct": "analepsis (kilas balik temporal ke masa lalu)",
        "distractors": [
            "prolepsis (kilas maju antisipatif ke masa depan)",
            "elipsis naratif (peloncatan lompatan waktu kosong)",
            "pauze deskriptif (penghentian waktu aksi demi latar)",
            "isokroni (keselarasan mutlak tempo wacana dan cerita)"
        ],
        "formula": {
            "title": "ANAKRONI NARATOLOGI GENETTE",
            "latex": "\\text{Cerita Primer (T)} \\xrightarrow{\\text{mundur ke }} \\text{Peristiwa Masa Lalu } (T - \\Delta t) \\implies \\text{Analepsis}",
            "legend": "• Prolepsis bergerak maju ke masa depan (flashforward); analepsis melompat ke masa silam (flashback)"
        },
        "hints": {
            "concept": "Genette membagi anakroni (penyimpangan kronologis) menjadi analepsis (retrospeksi/flashback) dan prolepsis (antisipasi/flashforward).",
            "execution": "Farhan mengingat masa lalunya 30 tahun silam saat di mimbar pelantikan = analepsis."
        }
    },
    {
        "id": "ind_lanjut-lat-h-05",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Teori Polifoni dan Dialogisme Mikhail Bakhtin",
        "stem": "Mikhail Bakhtin memuji novel-novel karya Fyodor Dostoevsky karena tidak menundukkan karakter-karakter tokohnya di bawah suara tunggal otoritas ideologis pengarang. Setiap tokoh tampil sebagai kesadaran merdeka dengan pandangan dunianya sendiri yang setara dan berdebat secara otonom. Konsep sastra yang menampilkan pluralitas suara mandiri yang tidak tereduksi ini dinamakan...",
        "correct": "polifoni (polyphony) dan heteroglosia",
        "distractors": [
            "monologisme absolut otoritarian",
            "solilokui dramatik puitis",
            "mimesis representasionalis murni",
            "alegori didaktik moralistik linier"
        ],
        "formula": {
            "title": "POLIFONI BAKHTIN",
            "latex": "\\text{Karya Polifonik} \\iff \\sum_{i=1}^n \\text{Suara Tokoh Otonom} \\quad (\\text{tanpa dominasi hegemoni suara pengarang})",
            "legend": "• Berlawanan dengan karya monologik di mana seluruh tokoh hanya menjadi corong doktrin pengarang"
        },
        "hints": {
            "concept": "Bakhtin mengenalkan konsep novel polifonik (banyak suara otonom) dan heteroglosia (keberagaman dialek sosial/ideologi).",
            "execution": "Pluralitas suara mandiri yang setara tanpa hegemoni pengarang adalah polifoni (polyphony)."
        }
    },
    {
        "id": "ind_lanjut-lat-h-06",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Nominalisasi Gramatikal dalam SFL (Halliday)",
        "stem": "Dalam Linguistik Fungsional Sistemis (SFL) Michael Halliday, salah satu ciri khas ragam bahasa ilmiah tinggi adalah terjadinya metafora gramatikal berupa nominalisasi. Perubahan klausa kongruen <em>'Pemerintah memangkas subsidi bahan bakar fosil secara drastis sehingga harga komoditas pangan melonjak tinggi'</em> menjadi klausa ilmiah bernominalisasi metaforis yang tepat adalah...",
        "correct": "Pemangkasan drastis subsidi bahan bakar fosil oleh pemerintah berdampak langsung pada lonjakan tinggi harga komoditas pangan.",
        "distractors": [
            "Ketika pemerintah memangkas bahan bakar, maka masyarakat pun segera merasakan betapa tingginya harga makanan.",
            "Harga pangan melonjak tinggi karena bahan bakar subsidi dipangkas sangat drastis oleh para menteri.",
            "Pemerintah memotong subsidi, oleh sebab itu harga sayur dan beras di pasar mengalami kenaikan harga.",
            "Lonjakan harga terjadi karena pemerintah suka sekali memangkas anggaran bahan bakar tanpa bermusyawarah."
        ],
        "formula": {
            "title": "METAFORA GRAMATIKAL (NOMINALISASI SFL)",
            "latex": "\\text{Verba } (\\text{memangkas, melonjak}) \\xrightarrow{\\text{Nominalisasi}} \\text{Nomina } (\\text{Pemangkasan, Lonjakan})",
            "legend": "• Mengubah proses/tindakan dinamis menjadi entitas konsep abstrak padat informasi ilmiah"
        },
        "hints": {
            "concept": "Nominalisasi mengubah verba proses ('memangkas', 'melonjak') menjadi nomina konsep ('pemangkasan', 'lonjakan') dan konjungsi menjadi verba relasional ('berdampak pada').",
            "execution": "Pilih kalimat yang mengemas peristiwa ke dalam nomina: 'Pemangkasan drastis... berdampak langsung pada lonjakan tinggi...'."
        }
    },
    {
        "id": "ind_lanjut-lat-h-07",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Teori Relevansi Sperber & Wilson",
        "stem": "Dalam Teori Relevansi yang digagas oleh Dan Sperber dan Deirdre Wilson, sebuah ujaran dinilai memiliki derajat relevansi kognitif yang optimal bagi pendengar apabila...",
        "correct": "menghasilkan efek kognitif positif (positive cognitive effects) yang maksimal dengan upaya pemrosesan mental (processing effort) yang sekecil mungkin",
        "distractors": [
            "memerlukan upaya pemikiran mental yang sangat rumit dan panjang untuk memecahkan teka-teki bahasanya",
            "menggunakan kata-kata arkais kuno yang tidak dikenal oleh masyarakat awam",
            "disampaikan dengan mematuhi seluruh aturan tata bahasa preskriptif secara kaku tanpa makna implisit",
            "meniadakan seluruh konteks latar belakang kebudayaan antara penutur dan mitra tutur"
        ],
        "formula": {
            "title": "PRINSIP RELEVANSI SPERBER & WILSON",
            "latex": "\\text{Relevansi} \\propto \\frac{\\text{Efek Kognitif Positif}}{\\text{Upaya Pemrosesan Mental (Processing Effort)}}",
            "legend": "• Relevansi tertinggi dicapai saat wawasan baru maksimal diperoleh dengan beban kerja kognitif minimal"
        },
        "hints": {
            "concept": "Sperber & Wilson: Relevansi berbanding lurus dengan efek kognitif dan berbanding terbalik dengan upaya pemrosesan.",
            "execution": "Relevansi optimal = efek kognitif positif maksimal dengan usaha pemrosesan mental minimal."
        }
    },
    {
        "id": "ind_lanjut-lat-h-08",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy Petitio Principii (Begging the Question)",
        "stem": "Perhatikan pertukaran argumen berikut:<br>Mahasiswa: <em>'Mengapa kita harus mempercayai bahwa isi naskah babon kuno ini sepenuhnya memuat kebenaran sejarah mutlak?'</em><br>Pemandu: <em>'Karena naskah ini ditulis oleh seorang pujangga agung yang kata-katanya tidak pernah salah. Dan kita tahu pujangga tersebut tidak pernah salah karena naskah suci agung ini sendiri secara tegas menyatakannya demikian.'</em><br>Bentuk kesesatan penalaran (*fallacy*) dalam argumentasi pemandu di atas adalah...",
        "correct": "petitio principii / circular reasoning (argumen berputar yang menjadikan kesimpulan sebagai premis pembukti)",
        "distractors": [
            "straw man fallacy (membuat argumen karikatur palsu)",
            "slippery slope (menghubungkan rangkaian bencana ekstrem)",
            "ad misericordiam (memanfaatkan eksploitasi belas kasihan)",
            "post hoc ergo propter hoc (kausalitas waktu kronologis)"
        ],
        "formula": {
            "title": "FALLACY PETITIO PRINCIPII",
            "latex": "\\text{Premis } P \\implies \\text{Kesimpulan } Q, \\quad \\text{di mana } Q \\equiv P",
            "legend": "• Argumen sirkular di mana validitas premis mengandalkan kebenaran kesimpulan yang justru sedang dipertanyakan"
        },
        "hints": {
            "concept": "Petitio principii (penalaran melingkar/circular reasoning) membuktikan klaim dengan menggunakan klaim itu sendiri sebagai premis.",
            "execution": "Kebenaran naskah dibuktikan oleh pujangga yang tak pernah salah, dan kemaksuman pujangga dibuktikan oleh naskah itu sendiri."
        }
    },
    {
        "id": "ind_lanjut-lat-h-09",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Hermeneutika Paul Ricoeur (Hermeneutika Curiga vs Pemulihan)",
        "stem": "Dalam kajian hermeneutika sastra Paul Ricoeur, pendekatan pembacaan kritis yang memperlakukan teks dengan kecurigaan mendalam untuk membongkar distorsi kesadaran palsu, ideologi tersembunyi, atau represi psikologis yang tersamar di balik permukaan teks—sebagaimana dipelopori oleh Karl Marx, Friedrich Nietzsche, dan Sigmund Freud—dikenal sebagai...",
        "correct": "hermeneutika kecurigaan (hermeneutics of suspicion)",
        "distractors": [
            "hermeneutika pemulihan iman (hermeneutics of faith/recollection)",
            "hermeneutika intensionalisme biografis pengarang",
            "lingkaran hermeneutika filologis Schleiermacher",
            "hermeneutika ontologis keberadaan Dasein Heidegger"
        ],
        "formula": {
            "title": "HERMENEUTIKA KECURIGAAN RICOEUR",
            "latex": "\\text{Hermeneutics of Suspicion} \\iff \\text{Dekonstruksi ilusi makna sadar demi menyingkap motif represi tersembunyi}",
            "legend": "• Menganggap teks bukan sebagai cermin kebenaran polos, melainkan topeng bagi kuasa, hasrat, atau ideologi"
        },
        "hints": {
            "concept": "Ricoeur menjuluki Marx, Nietzsche, dan Freud sebagai 'tiga guru kecurigaan' (masters of suspicion).",
            "execution": "Membongkar kepalsuan dan ilusi di balik teks adalah hermeneutika kecurigaan (hermeneutics of suspicion)."
        }
    },
    {
        "id": "ind_lanjut-lat-h-10",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy Equivocation (Ekuivokasi / Kerancuan Semantis)",
        "stem": "Perhatikan silogisme semu berikut:<br><em>Premis 1: Manusia adalah makhluk yang berakal budi.<br>Premis 2: Bayi yang baru lahir berumur satu jam belum mampu berpikir menggunakan akal budinya.<br>Kesimpulan: Oleh karena itu, bayi yang baru lahir tersebut secara ontologis bukan merupakan seorang manusia.</em><br>Kesesatan bernalar dalam silogisme di atas terjadi akibat...",
        "correct": "ekuivokasi (equivocation: menggunakan kata 'akal budi' dengan pergeseran makna antara kapasitas potensial spesies dan fungsi kognitif aktual)",
        "distractors": [
            "ad ignorantiam (menganggap sesuatu benar karena belum terbukti salah)",
            "hasty generalization (mengambil sampel yang terlalu sedikit)",
            "false dilemma (membatasi alternatif menjadi dua)",
            "ad baculum (menggunakan ancaman kekuatan fisik)"
        ],
        "formula": {
            "title": "FALLACY OF EQUIVOCATION",
            "latex": "\\text{Term } X_1 (\\text{Kapasitas Esensial}) \\neq \\text{Term } X_2 (\\text{Operasionalisasi Aktual})",
            "legend": "• Menyamarkan dua makna kata yang berbeda dalam struktur silogisme logis"
        },
        "hints": {
            "concept": "Ekuivokasi terjadi ketika sebuah istilah kunci digunakan dengan arti yang berbeda dalam premis yang berbeda pada argumen yang sama.",
            "execution": "Kata 'akal budi' pada Premis 1 merujuk pada hakikat/spesies manusia, sedangkan Premis 2 merujuk pada kematangan fungsi berpikir aktual."
        }
    },
    {
        "id": "ind_lanjut-lat-h-11",
        "materi": "ANALISIS WACANA KRITIS (AWK)",
        "topic": "Strategi Eksklusi dan Inklusi Wacana Theo van Leeuwen",
        "stem": "Dalam kerangka representasi aktor sosial (*social actor representation*) yang dikembangkan oleh Theo van Leeuwen, penghilangan aktor sosial tertentu dari dalam teks wacana berita yang dilakukan melalui nominalisasi verba tindakan atau penghilangan agen dalam kalimat pasif (seperti: <em>'Harga beras dinaikkan'</em> tanpa menyebut pihak yang menaikkan) diklasifikasikan sebagai strategi...",
        "correct": "eksklusi melalui pasivasi dan supresi (suppression)",
        "distractors": [
            "inklusi melalui diferensiasi individual",
            "nominasi fungsionalisasi peran jabatan",
            "identifikasi spasial relasional",
            "generalisasi agregasi statistik"
        ],
        "formula": {
            "title": "TEORI REPRESENTASI AKTOR SOSIAL THEO VAN LEEUWEN",
            "latex": "\\text{Eksklusi (Pengeluaran Aktor)} \\iff \\text{Supresi (dihilangkan total)} \\lor \\text{Latar Belakang (disebut samar)}",
            "legend": "• Menghilangkan aktor pembuat kebijakan untuk menghindarkan mereka dari pertanggungjawaban publik"
        },
        "hints": {
            "concept": "Theo van Leeuwen membedakan strategi Eksklusi (mengeluarkan aktor) dan Inklusi (memasukkan aktor). Penghilangan total aktor disebut supresi.",
            "execution": "Menghilangkan pihak pelaku melalui kalimat pasif tanpa pelengkap pelaku adalah eksklusi supresi (suppression)."
        }
    },
    {
        "id": "ind_lanjut-lat-h-12",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Sintaksis Paralelisme Kompleks dalam Kalimat Majemuk",
        "stem": "Kesejajaran bentuk gramatikal (*paralelisme*) sangat penting untuk menjaga kejelasan makna dalam kalimat akademik bertingkat majemuk. Kalimat berikut yang memenuhi prinsip paralelisme sintaksis secara sempurna adalah...",
        "correct": "Penelitian ini bertujuan untuk mengidentifikasi senyawa aktif daun sirih, menganalisis daya hambat antibakterinya, dan merumuskan dosis formulasi gel antiseptik yang aman.",
        "distractors": [
            "Penelitian ini bertujuan untuk mengidentifikasi senyawa aktif daun sirih, analisis daya hambat antibakterinya, dan merumuskan dosis formulasi gel antiseptik yang aman.",
            "Penelitian ini bertujuan untuk mengidentifikasi senyawa aktif daun sirih, menganalisis daya hambat antibakterinya, dan perumusan dosis gel antiseptik yang aman.",
            "Penelitian ini bertujuan untuk pengidentifikasian senyawa aktif daun sirih, menganalisis daya hambat antibakterinya, dan merumuskan dosis formulasi gel antiseptik.",
            "Penelitian ini bertujuan untuk diidentifikasinya senyawa aktif daun sirih, menganalisis daya hambat antibakterinya, dan merumuskan dosis gel."
        ],
        "formula": {
            "title": "KAIDAH PARALELISME SINTAKSIS",
            "latex": "\\text{Tujuan: } \\text{Verba Aktif } (\\text{meng-}) + \\text{Verba Aktif } (\\text{meng-}) + \\text{Verba Aktif } (\\text{merumuskan})",
            "legend": "• Menjaga konsistensi imbuhan dan kategori kata di seluruh rincian predikatif kalimat"
        },
        "hints": {
            "concept": "Paralelisme menuntut seluruh unsur yang dirinci memiliki bentuk gramatikal yang setara (misal: semuanya verba aktif me-).",
            "execution": "Pilihan yang konsisten menggunakan verba aktif transitif adalah 'mengidentifikasi..., menganalisis..., dan merumuskan...'."
        }
    },
    {
        "id": "ind_lanjut-lat-h-13",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Kritik Dekonstruksi dan Konsep *Différance* Derrida",
        "stem": "Jacques Derrida menciptakan neologisme *différance* yang menggabungkan dua makna dalam bahasa Prancis: *to differ* (berbeda/membedakan) dan *to defer* (menunda). Dalam analisis teks sastra, konsep ini menegaskan bahwa...",
        "correct": "makna sebuah kata atau teks tidak pernah hadir secara utuh, stabil, atau final pada saat ini, melainkan senantiasa ditangguhkan tanpa henti melalui jejaring jejak (traces) tanda-tanda lainnya",
        "distractors": [
            "setiap karya sastra memiliki satu makna inti transendental yang dapat ditangkap secara pasti oleh pembaca yang tekun",
            "bahasa sastra sepenuhnya bebas dari pengaruh struktur gramatika mana pun",
            "pengarang memiliki kontrol kedaulatan mutlak atas penafsiran pembaca di masa depan",
            "semua teks sastra pada hakikatnya identik dan tidak memiliki perbedaan estetis apa pun"
        ],
        "formula": {
            "title": "KONSEP DIFFÉRANCE JACQUES DERRIDA",
            "latex": "\\text{Différance} \\iff \\text{Perbedaan Ruang Spasial (Differing)} + \\text{Penundaan Waktu Temporal (Deferring)}",
            "legend": "• Makna final selalu lolos dan tertunda di dalam rantai penanda (chain of signifiers)"
        },
        "hints": {
            "concept": "Différance Derrida menunjukkan bahwa makna tanda tidak pernah murni hadir secara instan, melainkan selalu berbeda dan tertunda tak terbatas.",
            "execution": "Pilih opsi yang menjelaskan penundaan makna (deferred) tanpa henti melalui jejak tanda lainnya."
        }
    },
    {
        "id": "ind_lanjut-lat-h-14",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy Straw Man (Manusia Jerami)",
        "stem": "Perhatikan dialog debat publik berikut:<br>Pakar Ekologi: <em>'Pemerintah sebaiknya memperketat uji kelayakan lingkungan dan menghentikan sementara ekspansi tambang batu bara baru di kawasan hutan lindung demi melindungi sumber air bersih warga.'</em><br>Pengusaha: <em>'Rekan akademisi ini rupanya ingin kita semua kembali hidup di zaman purba tanpa aliran listrik sama sekali, mematikan seluruh pabrik industri nasional, dan membiarkan jutaan buruh mati kelaparan.'</em><br>Strategi penyerangan argumen yang dilakukan oleh sang pengusaha merupakan kesesatan...",
        "correct": "straw man fallacy (memutarbalikkan argumen lawan menjadi versi ekstrem yang mudah diserang)",
        "distractors": [
            "ad hominem abusive (menghina latar belakang fisik lawan bicara)",
            "slippery slope murni tanpa distorsi premis",
            "appeal to ignorance (berlandaskan ketiadaan bukti lawan)",
            "tu quoque (menuduh balik inkonsistensi perilaku lawan)"
        ],
        "formula": {
            "title": "FALLACY STRAW MAN",
            "latex": "\\text{Argumen Riil A (Pengaturan Tambang)} \\xrightarrow{\\text{Distorsi Ekstrem}} \\text{Argumen Boneka Jerami B (Hidup di Zaman Purba)}",
            "legend": "• Menyerang argumen rekaan yang dilebih-lebihkan secara karikatural alih-alih merespons substansi usulan awal"
        },
        "hints": {
            "concept": "Straw man terjadi saat seseorang mengubah argumen lawan menjadi sangat ekstrem, konyol, atau tidak masuk akal agar mudah dihancurkan.",
            "execution": "Mengganti usulan 'evaluasi tambang' menjadi 'ingin mematikan seluruh listrik dan kembali ke zaman purba' adalah straw man klasik."
        }
    },
    {
        "id": "ind_lanjut-lat-h-15",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Struktur Naratif Todorov (Transformasi Keseimbangan)",
        "stem": "Tzvetan Todorov merumuskan bahwa alur sebuah narasi klasik bergerak melintasi lima tahapan transformasi: (1) ekuilibrium awal, (2) gangguan/disrupsi, (3) kesadaran akan disrupsi, (4) upaya pemulihan, dan (5) ekuilibrium baru. Ciri mendasar dari *ekuilibrium baru* (new equilibrium) menurut Todorov adalah...",
        "correct": "tercapainya tatanan keseimbangan baru yang telah mengalami transformasi dan tidak pernah kembali identik secara persis dengan ekuilibrium awal sebelum krisis",
        "distractors": [
            "kembalinya situasi masyarakat secara persis seratus persen seperti pada adegan pembuka cerita",
            "penghancuran total seluruh karakter tokoh tanpa menyisakan satu pun penyelesaian cerita",
            "keadaan di mana seluruh tokoh melupakan seluruh penderitaan dan peristiwa konflik yang telah terjadi",
            "terhentinya perjalanan waktu tokoh secara permanen dalam kondisi katarsis abadi"
        ],
        "formula": {
            "title": "TRANSFORMASI NARATIF TODOROV",
            "latex": "\\text{Ekuilibrium Awal } (E_0) \\xrightarrow{\\text{Krisis}} \\text{Ekuilibrium Baru } (E_1), \\quad E_1 \\neq E_0",
            "legend": "• Ekuilibrium baru memuat bekas luka, kedewasaan psikologis, atau tatanan hukum baru hasil resolusi konflik"
        },
        "hints": {
            "concept": "Todorov menekankan bahwa ekuilibrium baru bukanlah pengulangan identik dari kondisi awal, melainkan keadaan seimbang yang termodifikasi.",
            "execution": "Pilih opsi yang menyatakan bahwa ekuilibrium baru telah mengalami transformasi dan tidak identik dengan kondisi awal."
        }
    },
    {
        "id": "ind_lanjut-lat-h-16",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Sintesis Meta-Analisis dan Penyajian Keterbatasan Riset",
        "stem": "Dalam menyusun bagian Keterbatasan Penelitian (*Limitations*) pada tesis magister, rumusan kalimat yang menunjukkan kejujuran akademik, kematangan metodologis, serta membuka peluang bagi riset mendatang adalah...",
        "correct": "Generalisasi temuan penelitian ini terbatas pada ekosistem sekolah menengah kejuruan teknik berbasis asrama, sehingga penelitian lanjutan dengan sampel sekolah umum heterogen sangat disarankan untuk menguji validitas ekologis model.",
        "distractors": [
            "Penelitian ini memiliki kelemahan yang sangat fatal karena peneliti tidak sempat menyebarkan kuesioner ke sekolah lain akibat kehabisan biaya transportasi.",
            "Kami mengakui bahwa metode yang kami gunakan salah sasaran, tetapi penguji diharapkan tetap meluluskan tesis ini demi kebaikan bersama.",
            "Tidak ada keterbatasan apa pun dalam penelitian ini karena semua instrumen telah dirancang secara sempurna tanpa cacat sedikit pun.",
            "Keterbatasan utama riset ini adalah responden siswa yang sangat malas menjawab pertanyaan sehingga data yang diperoleh tidak dapat diandalkan."
        ],
        "formula": {
            "title": "PENULISAN KETERBATASAN AKADEMIK ELEGAN",
            "latex": "\\text{Limitations} \\iff \\text{Identifikasi Batasan Validitas Eksternal} + \\text{Rekomendasi Agenda Riset Lanjutan}",
            "legend": "• Mengarahkan kelemahan metodologis terukur menjadi pemantik kontribusi ilmiah bagi peneliti berikutnya"
        },
        "hints": {
            "concept": "Keterbatasan riset ditulis secara objektif, berfokus pada ruang lingkup metodologis (validitas internal/eksternal), dan memberikan rekomendasi konstruktif.",
            "execution": "Opsi pertama menyampaikan batasan generalisasi secara elegan dan merekomendasikan riset lanjutan untuk menguji validitas ekologis."
        }
    },
    {
        "id": "ind_lanjut-lat-h-17",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Tindak Ilokusi vs Perlokusi (Austin)",
        "stem": "Seorang guru berdiri di depan kelas yang bising, menatap para siswa dengan tenang lalu berucap: <em>'Ujian akhir semester dimulai dalam lima menit.'</em> Seketika itu juga, para siswa berhenti berbicara, menutup buku teks mereka, dan duduk tegak dengan tertib. Dalam teori tindakan bahasa J.L. Austin, tindakan siswa yang menjadi tenang dan duduk tertib tersebut merupakan...",
        "correct": "efek perlokusi (perlocutionary effect: dampak atau konsekuensi psikologis/tindakan nyata pada mitra tutur)",
        "distractors": [
            "tindak lokusi (locutionary act: pemroduksian bunyi bermakna semantis harfiah)",
            "daya ilokusi (illocutionary force: maksud tuturan penutur)",
            "presuposisi semantis eksistensial mutlak",
            "deiksis persona inklusif langsung"
        ],
        "formula": {
            "title": "TRIKOTOMI TINDAK TUTUR AUSTIN",
            "latex": "\\text{Lokusi (Ujaran)} \\to \\text{Ilokusi (Maksud/Peringatan)} \\to \\text{Perlokusi (Efek Nyata: Murid Tertib)}",
            "legend": "• Perlokusi adalah akibat nyata (respons kognitif/afektif/perilaku) yang timbul pada pendengar akibat ujaran"
        },
        "hints": {
            "concept": "Lokusi = melafalkan kata; Ilokusi = maksud tuturan; Perlokusi = akibat/reaksi nyata pada mitra tutur.",
            "execution": "Reaksi siswa yang menjadi tertib dan tenang adalah dampak/efek tuturan, yakni efek perlokusi (perlocutionary effect)."
        }
    },
    {
        "id": "ind_lanjut-lat-h-18",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Arketipe Jungian dalam Kritik Sastra",
        "stem": "Dalam kritik sastra psikoanalisis arketipal berbasis Carl Gustav Jung, motif naratif di mana seorang protagonis harus menuruni ruang bawah tanah yang gelap, labirin tak berujung, atau menyelam ke dasar samudra untuk menghadapi monster purba sebelum meraih kebijaksanaan hidup merupakan manifestasi simbolis dari arketipe...",
        "correct": "integrasi bayang-bayang (confronting the Shadow) dan perjalanan bawah sadar kolektif",
        "distractors": [
            "proyeksi persona topeng sosial publik",
            "regresi fiksasi fase oral Freud",
            "katarsis dramatik penderitaan fisik",
            "alienasi kelas borjuasi boros"
        ],
        "formula": {
            "title": "ARKETIPE JUNGIAN SASTRA",
            "latex": "\\text{Nekyia (Katabasis/Turun ke Bawah)} \\iff \\text{Menyelami Bawah Sadar Kolektif demi Integrasi The Shadow}",
            "legend": "• Menghadapi sisi gelap kepribadian yang tersembunyi sebagai syarat mencapai individuasi diri sejati"
        },
        "hints": {
            "concept": "Jung: Simbol labirin, kegelapan bawah tanah, dan monster purba merepresentasikan alam bawah sadar kolektif dan figur Shadow (Bayang-bayang).",
            "execution": "Pilih konfrontasi dengan bayang-bayang (the Shadow) dan penyelaman bawah sadar kolektif."
        }
    },
    {
        "id": "ind_lanjut-lat-h-19",
        "materi": "ANALISIS WACANA KRITIS (AWK)",
        "topic": "Analisis Modalitas dan Relasi Kuasa Teks",
        "stem": "Perhatikan dua rumusan regulasi organisasi berikut:<br><em>Teks A: 'Seluruh staf wajib menyerahkan laporan kinerja mingguan tepat waktu sebelum hari Jumat pukul 16.00 WIB.'<br>Teks B: 'Staf dipersilakan untuk dapat berbagi perkembangan kinerja mingguan apabila memungkinkan sebelum akhir pekan.'</em><br>Perbedaan derajat modalitas deontik antara Teks A dan Teks B mencerminkan perbedaan relasi kuasa wacana, yaitu...",
        "correct": "Teks A menggunakan modalitas deontik berkadar tinggi ('wajib') yang menegaskan hierarki kekuasaan asimetris institusional, sedangkan Teks B menggunakan modalitas berkadar rendah yang menyamarkan kontrol koersif menjadi ajakan partisipatif.",
        "distractors": [
            "Teks A dan Teks B memiliki kekuatan hukum yang sama persis tanpa perbedaan derajat kewajiban apa pun.",
            "Teks B menunjukkan kekuasaan yang jauh lebih kejam dan otoriter dibandingkan Teks A.",
            "Teks A ditulis dengan melanggar etika tata bahasa baku bahasa Indonesia modern.",
            "Teks B merupakan teks ilegal yang tidak boleh diterbitkan dalam organisasi mana pun."
        ],
        "formula": {
            "title": "MODALITAS DEONTIK DAN RELASI KUASA",
            "latex": "\\text{Kadar Deontik: 'Wajib'} (\\text{High}) > \\text{Kadar Deontik: 'Dipersilakan/Apabila Memungkinkan'} (\\text{Low})",
            "legend": "• Modalitas tinggi mencerminkan dominasi vertikal; modalitas rendah melembutkan relasi antaraktor"
        },
        "hints": {
            "concept": "Modalitas deontik berkaitan dengan keharusan/kewajiban (obligation/permission). Tingkat modalitas merefleksikan posisi kekuasaan penutur.",
            "execution": "Pilih analisis yang membedakan ketegasan imperatif Teks A (asimetris/hierarkis) dengan pelunakan persuasif Teks B."
        }
    },
    {
        "id": "ind_lanjut-lat-h-20",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy False Cause: Post Hoc vs Cum Hoc",
        "stem": "Dalam penelitian korelasi sosial, seorang analis menemukan koefisien korelasi $r = 0,85$ antara konsumsi es krim per kapita dan angka kasus kematian akibat tenggelam di pantai pada musim panas. Ia kemudian menyimpulkan: <em>'Makan es krim menyebabkan penurunan fungsi motorik perenang sehingga berakibat fatal tenggelam.'</em> Kesesatan penalaran analis tersebut mengabaikan adanya...",
        "correct": "variabel perancu laten (confounding variable / third-cause fallacy), yaitu suhu cuaca terik musim panas yang meningkatkan konsumsi es krim sekaligus frekuensi warga berenang di pantai",
        "distractors": [
            "kesalahan perhitungan aritmetika pecahan desimal pada rumus koefisien korelasi Pearson",
            "sampel es krim yang diuji di laboratorium mengandung racun sianida konsentrasi tinggi",
            "fakta bahwa semua orang yang tenggelam di pantai tidak bisa berenang gaya dada",
            "keberpihakan subjektif analis terhadap industri minuman bersoda pesaing es krim"
        ],
        "formula": {
            "title": "CUM HOC ERGO PROPTER HOC (KORELASI BUKAN KAUSALITAS)",
            "latex": "A \\sim B \\centernot\\implies A \\to B \\quad (\\exists C \\implies A \\land B)",
            "legend": "• Suhu udara panas (C) memicu kenaikan es krim (A) dan lonjakan kerumunan perenang (B)"
        },
        "hints": {
            "concept": "Correlation does not imply causation. Adanya korelasi tinggi sering kali dipicu oleh faktor ketiga (variabel perancu / confounding variable).",
            "execution": "Faktor musim panas yang panas (variabel perancu) menyebabkan kedua fenomena tersebut meningkat bersamaan."
        }
    },
    {
        "id": "ind_lanjut-lat-h-21",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Strukturalisme Genetik Lucien Goldmann",
        "stem": "Lucien Goldmann mengembangkan pendekatan strukturalisme genetik dalam telaah sastra. Pendekatan ini meyakini bahwa karya sastra besar tidak dapat dipahami semata-mata dari struktur intrinsik otonomnya, melainkan harus dihubungkan dengan...",
        "correct": "pandangan dunia (worldview / vision du monde) kelompok sosial tertentu yang diwakili oleh pengarang sebagai subjek kolektif dalam konteks sosio-historisnya",
        "distractors": [
            "susunan kromosom biologis dan kelainan genetik bawaan lahir pengarang naskah",
            "peraturan gramatika fonologi bahasa daerah yang digunakan dalam dialog tokoh",
            "jumlah eksemplar buku yang terjual di toko buku komersial perkotaan",
            "kecepatan mengetik pengarang saat merampungkan draf pertama naskah novel"
        ],
        "formula": {
            "title": "STRUKTURALISME GENETIK LUCIEN GOLDMANN",
            "latex": "\\text{Struktur Karya Sastra} \\iff \\text{Homologi Struktur Sosial} + \\text{Pandangan Dunia (Vision du Monde)}",
            "legend": "• Pengarang diposisikan sebagai transindividual subject yang mengartikulasikan kesadaran kelas sosialnya"
        },
        "hints": {
            "concept": "Strukturalisme genetik mengkaji relasi karya sastra dengan struktur sosial melalui konsep 'pandangan dunia' (vision du monde) dan subjek kolektif.",
            "execution": "Pilihlah opsi yang merujuk pada konsep pandangan dunia (worldview) kelompok sosial dan subjek kolektif pengarang."
        }
    },
    {
        "id": "ind_lanjut-lat-h-22",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Kohesi Leksikal Kompleks: Meronimi dan Hiponimi",
        "stem": "Perhatikan teks deskripsi botani farmasi berikut:<br><em>'Sebagai bagian dari famili <strong>Zingiberaceae</strong>, tanaman <strong>temulawak</strong> memiliki bagian organ yang kaya khasiat, terutama pada <strong>rimpang</strong> dan <strong>akarnya</strong>.'</em><br>Relasi semantis antara kata <em>'temulawak'</em> terhadap <em>'Zingiberaceae'</em>, serta antara kata <em>'rimpang'</em> terhadap <em>'tanaman'</em> berturut-turut merupakan relasi...",
        "correct": "hiponimi (hubungan hierarkis genus-spesies) dan meronimi (hubungan bagian-keseluruhan / part-whole)",
        "distractors": [
            "meronimi (bagian-keseluruhan) dan hiponimi (genus-spesies)",
            "antonimi komplementer dan sinonimi absolut",
            "homonimi gramatikal dan polisemi kontekstual",
            "metonimi spasial dan sinekdoke totum pro parte"
        ],
        "formula": {
            "title": "RELASI SEMANTIK LEKSIKAL",
            "latex": "\\text{Temulawak} \\subset \\text{Zingiberaceae (Hiponimi)}; \\quad \\text{Rimpang} \\in \\text{Tanaman (Meronimi)}",
            "legend": "• Hiponimi adalah relasi jenis/anggota kelas (is a kind of); meronimi adalah relasi bagian fisik (is a part of)"
        },
        "hints": {
            "concept": "Hiponimi = relasi jenis (temulawak adalah salah satu jenis Zingiberaceae). Meronimi = relasi bagian fisik (rimpang adalah bagian fisik dari tanaman).",
            "execution": "Pilihan yang tepat: hiponimi lalu meronimi."
        }
    },
    {
        "id": "ind_lanjut-lat-h-23",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Model Toulmin: Rebuttal dan Kondisi Pengecualian",
        "stem": "Dalam argumentasi kompleks model Toulmin, komponen <em>Rebuttal</em> (sanggahan/pengecualian) berperan krusial dalam memperkuat integritas ilmiah suatu klaim karena...",
        "correct": "secara eksplisit mengantisipasi dan merumuskan kondisi-kondisi luar biasa di mana klaim utama tersebut tidak berlaku atau mengalami kegagalan fungsi",
        "distractors": [
            "menyerang kepribadian lawan bicara secara pribadi agar debat segera berakhir",
            "menjamin bahwa klaim pasti berlaku secara absolut seratus persen di semua kondisi kosmik",
            "menggantikan peran data statistik sehingga peneliti tidak perlu melakukan uji coba lapangan",
            "mengubah topik pembicaraan ke bidang keilmuan lain yang tidak relevan"
        ],
        "formula": {
            "title": "KOMPONEN REBUTTAL MODEL TOULMIN",
            "latex": "\\text{Claim holds true, } \\mathbf{unless} \\text{ Rebuttal condition } (R) \\text{ occurs}",
            "legend": "• Menunjukkan batas keberlakuan klaim secara saintifik, mencegah klaim mutlak yang rapuh"
        },
        "hints": {
            "concept": "Rebuttal dalam model Toulmin adalah pengakuan atas batasan atau kondisi perkecualian di mana klaim tidak berlaku.",
            "execution": "Pilih opsi yang menjelaskan peran Rebuttal dalam merumuskan kondisi di mana klaim tidak berlaku."
        }
    },
    {
        "id": "ind_lanjut-lat-h-24",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Pendekatan Feminisme Gelombang Ketiga dalam Sastra",
        "stem": "Kritik sastra feminis gelombang ketiga (*third-wave feminist criticism*) memperluas perspektif telaah dengan menolak gagasan universal tentang 'pengalaman perempuan tunggal'. Pendekatan ini menggunakan lensa interseksionalitas (*intersectionality*) yang dikembangkan oleh Kimberlé Crenshaw, yang menganalisis bagaimana penindasan terhadap perempuan dalam teks sastra saling bertaut silang dengan...",
        "correct": "identitas ras, kelas sosial-ekonomi, etnisitas, usia, dan orientasi kultural",
        "distractors": [
            "kecepatan reaksi kimia tubuh perempuan saat mengalami menstruasi semata",
            "perbedaan gaya tulisan tangan alfabet antara perempuan dan laki-laki",
            "kewajiban perempuan untuk selalu menjadi tokoh antagonis dalam setiap cerita",
            "keinginan universal seluruh perempuan di dunia untuk hidup terasing di pulau terpencil"
        ],
        "formula": {
            "title": "INTERSEKSIONALITAS DALAM KRITIK SASTRA FEMINIS",
            "latex": "\\text{Opression Matrix} = \\text{Gender} \\otimes \\text{Ras} \\otimes \\text{Kelas Sosial} \\otimes \\text{Kultural}",
            "legend": "• Menolak generalisasi esensialis borjuis kulit putih dan menelaah kompleksitas penindasan berlapis"
        },
        "hints": {
            "concept": "Interseksionalitas mengkaji persilangan antara gender dengan dimensi sosial lain seperti ras, kelas ekonomi, dan etnisitas.",
            "execution": "Pilih opsi yang memuat persilangan ras, kelas sosial-ekonomi, dan identitas kultural."
        }
    },
    {
        "id": "ind_lanjut-lat-h-25",
        "materi": "ANALISIS WACANA KRITIS (AWK)",
        "topic": "Analisis Ideologis Metafora Konseptual Lakoff & Johnson",
        "stem": "Dalam kajian linguistik kognitif George Lakoff dan Mark Johnson, metafora bukan sekadar hiasan retoris bahasa, melainkan menstrukturkan cara manusia berpikir dan bertindak. Dalam wacana politik dan kebijakan ekonomi negara, pemakaian metafora konseptual <em>'PERSAINGAN PASAR ADALAH MEDAN PERANG'</em> (seperti: <em>menembus pertahanan lawan, melancarkan strategi invasi pasar, menghabisi kompetitor</em>) secara ideologis mengonstruksi realitas bisnis menjadi...",
        "correct": "arena pertarungan destruktif zero-sum game yang menjustifikasi agresi agresif dan meniadakan nilai-nilai kerja sama mutualisme",
        "distractors": [
            "taman rekreasi yang penuh kegembiraan dan kedamaian tanpa sengketa",
            "ruang ibadah suci yang melarang seluruh transaksi finansial komersial",
            "laboratorium kimia yang sepenuhnya bebas dari kepentingan manusia",
            "kegiatan olahraga amatir yang tidak mempermasalahkan menang atau kalah"
        ],
        "formula": {
            "title": "METAFORA KONSEPTUAL LAKOFF & JOHNSON",
            "latex": "\\text{Source Domain (Perang/War)} \\xrightarrow{\\text{Mapping}} \\text{Target Domain (Ekonomi/Pasar)}",
            "legend": "• Pemetaan konsep militeristik menjustifikasi perilaku bisnis agresif dan mengikis kesadaran etis kerja sama"
        },
        "hints": {
            "concept": "Metafora konseptual memetakan ranah sumber (perang) ke ranah sasaran (pasar). Jika pasar dipandang sebagai perang, maka pelaku usaha diposisikan sebagai prajurit yang harus menghabisi musuh.",
            "execution": "Metafora ini menjustifikasi agresi dan memandang pasar sebagai permainan zero-sum destruktif."
        }
    }
]
