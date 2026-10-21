# -*- coding: utf-8 -*-
"""
ind_lanjut_data_easy.py
25 Authentic Easy Items for TKA 2026 Bahasa Indonesia Tingkat Lanjut (SMA/MA Fase F Lanjutan).
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik Kemendikdasmen.
Topics: Teks Akademik & Jurnal Ilmiah, Konvensi Sitasi, Kohesi Gramatikal/Leksikal, Ragam Bahasa Ilmiah Baku, Unsur Kritik Sastra & Logika Wacana.
"""

IND_LANJUT_EASY_ITEMS = [
    {
        "id": "ind_lanjut-lat-e-01",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Konvensi Sitasi APA Edisi ke-7",
        "stem": "Dalam penulisan artikel ilmiah bereputasi, seorang penulis merujuk gagasan dari artikel jurnal karya tiga orang penulis (Budi Santoso, Siti Rahayu, dan Ahmad Fauzi) yang diterbitkan pada tahun 2023. Menurut panduan *American Psychological Association* (APA) edisi ke-7, bentuk rujukan dalam teks (*in-text citation*) sejak pemunculan pertama yang tepat adalah...",
        "correct": "(Santoso et al., 2023) atau Santoso et al. (2023)",
        "distractors": [
            "(Santoso, Rahayu, & Fauzi, 2023) pada pemunculan pertama",
            "(Santoso dkk., 2023) dengan mencantumkan seluruh gelar akademis penulis",
            "(Budi, Siti, & Ahmad, 2023) sesuai urutan abjad nama depan penulis",
            "(Santoso dkk., hlm. 45, 2023) tanpa mencantumkan kurung tahun secara terpisah"
        ],
        "formula": {
            "title": "KONVENSI SITASI APA 7TH",
            "latex": "\\text{3+ Penulis} \\implies (\\text{Penulis 1 } et\\ al., \\text{Tahun})",
            "legend": "• Pada APA 7th, karya dengan 3 atau lebih penulis disingkat menjadi et al. sejak pemunculan pertama"
        },
        "hints": {
            "concept": "Pedoman APA edisi ke-7 menyederhanakan aturan sitasi karya dengan tiga atau lebih penulis.",
            "execution": "Gunakan nama belakang penulis pertama diikuti 'et al.' dan tahun penerbitan sejak penyebutan pertama."
        }
    },
    {
        "id": "ind_lanjut-lat-e-02",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Struktur Abstrak IMRaD",
        "stem": "Abstrak artikel ilmiah yang berstandar internasional umumnya memuat ringkasan padat dari empat komponen utama IMRaD. Komponen yang menyajikan latar belakang masalah, urgensi teoretis, dan tujuan spesifik penelitian adalah bagian...",
        "correct": "Introduction (Pendahuluan)",
        "distractors": [
            "Methods (Metode Penelitian)",
            "Results (Hasil Penelitian)",
            "Discussion (Pembahasan Temuan)",
            "Conclusion (Simpulan dan Rekomendasi)"
        ],
        "formula": {
            "title": "STRUKTUR WACANA IMRAD",
            "latex": "\\text{IMRaD} = \\text{Introduction} + \\text{Methods} + \\text{Results} + \\text{Discussion}",
            "legend": "• Pendahuluan memuat rasionalisasi gap penelitian dan tujuan penelitian"
        },
        "hints": {
            "concept": "Pahami fungsi masing-masing komponen dalam format IMRaD.",
            "execution": "Bagian yang mendeskripsikan 'alasan penelitian dilakukan' dan 'tujuan studi' adalah Pendahuluan (Introduction)."
        }
    },
    {
        "id": "ind_lanjut-lat-e-03",
        "materi": "KOHESI & KOHERENSI WACANA",
        "topic": "Kohesi Gramatikal Substitusi",
        "stem": "Perhatikan kalimat berikut:<br><em>'Pemerintah telah meluncurkan berbagai program bantuan sosial tunai untuk masyarakat prasejahtera. Kebijakan serupa juga diberlakukan oleh pemerintah daerah di wilayah kepulauan.'</em><br>Piranti kohesi yang ditandai oleh frasa <em>'kebijakan serupa'</em> pada kalimat kedua dikategorikan sebagai kohesi gramatikal...",
        "correct": "substitusi (penggantian)",
        "distractors": [
            "elipsis (pelesapan konstituen)",
            "referensi demonstratif ruang",
            "konjungsi temporal koordinatif",
            "repetisi leksikal penuh"
        ],
        "formula": {
            "title": "PIRANTI KOHESI GRAMATIKAL",
            "latex": "\\text{Substitusi} \\iff \\text{Penggantian unsur lingual dengan unsur lain yang sepadan}",
            "legend": "• Substitusi nominal menggantikan klausa/konstituen sebelumnya tanpa pengulangan kata sama persis"
        },
        "hints": {
            "concept": "Substitusi merupakan penggantian konstituen bahasa dengan konstituen lain untuk menjaga variasi tanpa mengubah rujukan makna.",
            "execution": "'Kebijakan serupa' menggantikan konstituen 'berbagai program bantuan sosial tunai'."
        }
    },
    {
        "id": "ind_lanjut-lat-e-04",
        "materi": "KOHESI & KOHERENSI WACANA",
        "topic": "Kohesi Leksikal Hiponimi",
        "stem": "Perhatikan kutipan berikut:<br><em>'Hutan lindung tersebut menjadi habitat alami berbagai jenis <strong>satwa langka</strong>. Di sana, petugas balai konservasi menemukan populasi <strong>anoa, babirusa, dan maleo</strong> yang masih berkembang biak secara alami.'</em><br>Hubungan semantik antara frasa <em>'satwa langka'</em> dan kata <em>'anoa, babirusa, maleo'</em> adalah hubungan kohesi leksikal...",
        "correct": "hipernim dan hiponim (hubungan kelas atas dan subordinat)",
        "distractors": [
            "sinonimi mutlak (makna bersinonim setara)",
            "antonimi komplementer (oposisi kutub)",
            "meronimi (hubungan bagian dengan keseluruhan benda fisik)",
            "kolokasi sintagmatik bebas"
        ],
        "formula": {
            "title": "KOHESI LEKSIKAL HIPONIMI",
            "latex": "\\text{Satwa Langka (Hipernim)} \\supset \\{\\text{Anoa, Babirusa, Maleo}\\} \\text{ (Hiponim)}",
            "legend": "• Hiponimi mencerminkan hubungan relasi makna umum-khusus dalam tata wacana"
        },
        "hints": {
            "concept": "Hipernim adalah superordinat (kata umum) dan hiponim adalah subordinat (kata khusus/anggota kelompok).",
            "execution": "'Satwa langka' adalah hipernim, sedangkan anoa, babirusa, dan maleo adalah hiponim-hiponimnya."
        }
    },
    {
        "id": "ind_lanjut-lat-e-05",
        "materi": "RAGAM BAHASA ILMIAH",
        "topic": "Objektivitas dan Kalimat Pasif Ilmiah",
        "stem": "Dalam ragam bahasa ilmiah, penulisan laporan penelitian menuntut kadar objektivitas tinggi dan desubjektifikasi penulis. Kalimat berikut yang memenuhi kaidah objektivitas ragam ilmiah formal adalah...",
        "correct": "Data penelitian dikumpulkan melalui instrumen kuesioner terstruktur berskala Likert lima poin.",
        "distractors": [
            "Saya dan tim telah sukses mengumpulkan data kuesioner dari seluruh responden penelitian.",
            "Kami merasa bahwa instrumen kuesioner berskala Likert merupakan cara paling mantap.",
            "Penulis dengan bangga menyampaikan keberhasilan pengumpulan seluruh lembar kuesioner lapangan.",
            "Data kuesioner berhasil didapatkan berkat kerja keras para asisten peneliti yang luar biasa gigih."
        ],
        "formula": {
            "title": "RAGAM BAHASA ILMIAH FORMAL",
            "latex": "\\text{Objektif} \\iff \\text{Menghindari pronomina persona pertama & penekanan pada proses/objek}",
            "legend": "• Konstruksi pasif impersonal menonjolkan fokus metodologis penelitian"
        },
        "hints": {
            "concept": "Ragam ilmiah menghindari pronomina orang pertama (saya, kami) dan ungkapan emotif/subjektif.",
            "execution": "Pilih kalimat pasif impersonal yang lugas dan netral secara akademis."
        }
    },
    {
        "id": "ind_lanjut-lat-e-06",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Pendekatan Mimetik",
        "stem": "Dalam telaah kritik sastra menurut tipologi M.H. Abrams, pendekatan kritik yang memandang karya sastra sebagai tiruan, cerminan, atau representasi dari kenyataan semesta kehidupan sosial masyarakat disebut pendekatan...",
        "correct": "mimetik",
        "distractors": [
            "ekspresif",
            "pragmatik",
            "objektif (strukturalisme)",
            "psikoanalisis"
        ],
        "formula": {
            "title": "4 PENDEKATAN KRITIK ABRAMS",
            "latex": "\\text{Mimetik} \\iff \\text{Karya Sastra sebagai Refleksi/Tiruan Semesta (Universe)}",
            "legend": "• Abrams membagi fokus kritik pada: Semesta (Mimetik), Pengarang (Ekspresif), Pembaca (Pragmatik), Karya (Objektif)"
        },
        "hints": {
            "concept": "Pendekatan mimetik (berakar dari mimesis Plato/Aristoteles) menitikberatkan keterkaitan karya dengan realitas empiris di dunia nyata.",
            "execution": "Pilih pendekatan mimetik yang meneliti keselarasan representasi sastra dengan kenyataan sosial."
        }
    },
    {
        "id": "ind_lanjut-lat-e-07",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Unsur Intrinsik Penokohan Berlapis",
        "stem": "Tokoh dalam novel yang digambarkan mengalami perubahan karakter, kematangan psikologis, atau pergeseran paradigma pandangan hidup secara signifikan sepanjang alur cerita berlangsung dinamakan tokoh...",
        "correct": "bulat / dinamis (round character)",
        "distractors": [
            "pipih / statis (flat character)",
            "karikatural (tokoh stereotip sederhana)",
            "figuran pasif (stock character)",
            "antagonis sekunder tanpa perkembangan batin"
        ],
        "formula": {
            "title": "TIPOLOGI PENOKOHAN E.M. FORSTER",
            "latex": "\\text{Round Character} \\implies \\text{Kompleks, berlapis, & mengalami perkembangan psikologis}",
            "legend": "• Flat character bersifat statis dan berdimensi tunggal dari awal hingga akhir cerita"
        },
        "hints": {
            "concept": "E.M. Forster membedakan karakter pipih (flat) dan bulat (round/dinamis).",
            "execution": "Tokoh yang kompleks dan wataknya bertransformasi seiring dinamika peristiwa disebut tokoh bulat (round character)."
        }
    },
    {
        "id": "ind_lanjut-lat-e-08",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy Ad Hominem",
        "stem": "Perhatikan argumen dalam sebuah sidang debat akademik berikut:<br><em>'Kita tidak perlu mempertimbangkan argumen Saudara Randy mengenai model ekonomi sirkular karena Saudara Randy sendiri belum pernah menyelesaikan studi magisternya dan sering terlambat datang ke forum diskusi.'</em><br>Kesesatan berpikir (*logical fallacy*) yang terjadi pada penolakan argumen tersebut adalah...",
        "correct": "argumentum ad hominem",
        "distractors": [
            "straw man fallacy (argumen orang-orangan jerami)",
            "false dilemma (dikotomi palsu)",
            "post hoc ergo propter hoc",
            "slippery slope (lereng licin tak berdasar)"
        ],
        "formula": {
            "title": "LOGICAL FALLACY AD HOMINEM",
            "latex": "\\text{Ad Hominem} \\iff \\text{Menyerang pribadi lawan bicara, bukan substansi argumennya}",
            "legend": "• Pelanggaran validitas silogisme akibat penolakan berbasis karakteristik personal"
        },
        "hints": {
            "concept": "Ad hominem adalah penyerangan terhadap kondisi pribadi, status, atau karakter pembuat argumen alih-alih menguji kebenaran premis logisnya.",
            "execution": "Penolakan gagasan Randy didasarkan pada status studinya, bukan pada kalkulasi model ekonomi sirkularnya."
        }
    },
    {
        "id": "ind_lanjut-lat-e-09",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Silogisme Kategoris Deduktif",
        "stem": "Diberikan premis-premis silogisme kategoris berikut:<br>Premis Mayor: <em>Semua artikel ilmiah yang terindeks Scopus Q1 melalui proses penelaahan sejawat (*peer review*) secara ketat.</em><br>Premis Minor: <em>Naskah penelitian tentang katalis zeolit karya Dr. Wardhana diterbitkan dalam jurnal terindeks Scopus Q1.</em><br>Simpulan deduktif yang sah (*valid*) dan benar (*sound*) dari penalaran silogisme tersebut adalah...",
        "correct": "Naskah penelitian tentang katalis zeolit karya Dr. Wardhana melalui proses penelaahan sejawat secara ketat.",
        "distractors": [
            "Sebagian artikel karya Dr. Wardhana tidak membutuhkan penelaahan sejawat yang ketat.",
            "Semua naskah katalis zeolit secara otomatis terindeks pada jurnal Scopus Q1 tanpa revisi.",
            "Dr. Wardhana adalah satu-satunya peneliti yang mampu menembus jurnal Scopus Q1 bereputasi.",
            "Naskah penelitian tentang katalis zeolit belum tentu melalui penelaahan sejawat yang ketat."
        ],
        "formula": {
            "title": "SILOGISME KATEGORIS MODUS BARBARA",
            "latex": "(M \\subset P) \\land (S \\subset M) \\implies S \\subset P",
            "legend": "• M = Artikel terindeks Scopus Q1, P = Melalui peer review ketat, S = Naskah Dr. Wardhana"
        },
        "hints": {
            "concept": "Gunakan aturan penarikan simpulan silogisme standar: Semua M adalah P, S adalah M, maka S adalah P.",
            "execution": "Substitusikan subjek minor ke predikat mayor secara langsung."
        }
    },
    {
        "id": "ind_lanjut-lat-e-10",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Parafrase Menghindari Plagiarisme Mosaik",
        "stem": "Seorang mahasiswa menyusun tinjauan pustaka dengan mengganti beberapa kata kerja dari teks sumber asli dengan sinonimnya, tetapi mempertahankan urutan struktur klausa dan susunan kalimat sumber tanpa parafrase mandiri. Bentuk pelanggaran integritas akademik semacam ini dikenal sebagai...",
        "correct": "plagiarisme mosaik (patchwriting)",
        "distractors": [
            "autoplagiarisme (self-plagiarism)",
            "fabrikasi data primer laboratorium",
            "falsifikasi hasil eksperimen",
            "ghostwriting komersial legal"
        ],
        "formula": {
            "title": "DEFINISI PATCHWRITING",
            "latex": "\\text{Patchwriting} \\iff \\text{Menyalin struktur kalimat sumber dengan substitusi sinonim parsial}",
            "legend": "• Parafrase sah menuntut restrukturisasi total sintaksis dan pengungkapan dengan bahasa sendiri"
        },
        "hints": {
            "concept": "Plagiarisme tambal sulam (patchwriting/mosaik) terjadi jika penulis hanya menambal sinonim tanpa merombak konstruksi sintaksis teks asli.",
            "execution": "Kenali istilah patchwriting atau plagiarisme mosaik dalam etika karya tulis ilmiah."
        }
    },
    {
        "id": "ind_lanjut-lat-e-11",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Tindak Tutur Ilokusi (John Searle)",
        "stem": "Dalam teori pragmatik tindak tutur John Searle, ujaran seorang penguji sidang skripsi: <em>'Dengan ini, saya menyatakan Anda lulus dengan predikat sangat memuaskan'</em> diklasifikasikan ke dalam kategori tindak tutur...",
        "correct": "deklarasi (declarations)",
        "distractors": [
            "asertif (assertives)",
            "direktif (directives)",
            "komisif (commissives)",
            "ekspresif (expressives)"
        ],
        "formula": {
            "title": "TAKSONOMI TINDAK TUTUR SEARLE",
            "latex": "\\text{Deklarasi} \\iff \\text{Ujaran yang langsung mengubah realitas institusional status objek}",
            "legend": "• Asertif: menyatakan fakta; Direktif: menyuruh; Komisif: berjanji; Ekspresif: emosi; Deklarasi: mengubah status"
        },
        "hints": {
            "concept": "Tindak tutur deklarasi menyebabkan perubahan seketika pada keadaan dunia nyata atau status sosial/institusional seseorang.",
            "execution": "Pernyataan kelulusan seketika mengubah status mahasiswa menjadi sarjana secara legal."
        }
    },
    {
        "id": "ind_lanjut-lat-e-12",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Maksim Percakapan Kuantitas (Grice)",
        "stem": "Seorang dokter bertanya kepada pasiennya: <em>'Berapa kali Anda meminum obat ini kemarin?'</em> Pasien menjawab: <em>'Kemarin pagi sekitar pukul tujuh saya sarapan bubur ayam di warung Bu Siti, lalu setelah mengobrol sebentar dengan paman saya, saya meminum satu butir tablet, kemudian sore hari saya tidur siang dan lupa minum obat, lalu malam hari sebelum tidur saya minum lagi satu butir.'</em> Tindak komunikasi pasien tersebut melanggar prinsip kerja sama Grice, khususnya maksim...",
        "correct": "kuantitas (memberikan informasi berlebih dari yang dibutuhkan)",
        "distractors": [
            "kualitas (menyampaikan kebohongan faktual)",
            "relevansi (mengalihkan topik ke topik lain)",
            "cara (menggunakan bahasa asing ambigu)",
            "kesantunan tindak basa-basi sosial"
        ],
        "formula": {
            "title": "PRINSIP KERJASAMA GRICE",
            "latex": "\\text{Maksim Kuantitas} \\iff \\text{Berikan informasi seperlunya (tidak kurang dan tidak lebih)}",
            "legend": "• Menyelipkan rincian sarapan dan obrolan paman melanggar batasan informatif maksim kuantitas"
        },
        "hints": {
            "concept": "Maksim kuantitas menuntut penutur memberikan informasi seringkas dan sepadat yang diperlukan konteks dialog.",
            "execution": "Pasien memberikan detail yang jauh melampaui jumlah hitungan frekuensi yang diminta dokter."
        }
    },
    {
        "id": "ind_lanjut-lat-e-13",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Majas Sinekdoke Pars Pro Toto",
        "stem": "Perhatikan penggalan puisi berikut:<br><em>'Sudah tiga purnama berlalu sejak kepergianmu,<br>namun belum tampak sebatang hidung pun di dermaga itu.'</em><br>Penggunaan frasa <em>'sebatang hidung'</em> untuk merujuk kehadiran manusia secara utuh merupakan penerapan gaya bahasa (majas)...",
        "correct": "sinekdoke pars pro toto",
        "distractors": [
            "sinekdoke totem pro parte",
            "metonimia asosiatif",
            "alegori filosofis",
            "litotes merendah diri"
        ],
        "formula": {
            "title": "SINEKDOKE DALAM SASTRA",
            "latex": "\\text{Pars Pro Toto} \\iff \\text{Menyebutkan sebagian unsur untuk mewakili keseluruhan}",
            "legend": "• 'Sebatang hidung' (sebagian) mewakili manusia utuh (keseluruhan)"
        },
        "hints": {
            "concept": "Pars pro toto menyebut sebagian untuk menyatakan seluruh, sedangkan totem pro parte menyebut seluruh untuk menyatakan sebagian.",
            "execution": "Menyebut 'hidung' untuk menyatakan 'sosok orang' adalah pars pro toto."
        }
    },
    {
        "id": "ind_lanjut-lat-e-14",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Kalimat Efektif dan Kesejajaran Struktur Sintaksis",
        "stem": "Perhatikan rumusan tujuan penelitian yang belum efektif berikut:<br><em>'Tujuan penelitian ini adalah untuk menganalisis kadar antioksidan, menentukan konsentrasi ekstrak terbaik, dan pengujian stabilitas sediaan krim.'</em><br>Perbaikan yang tepat agar kalimat tersebut memiliki kesejajaran (*paralelisme*) bentuk infleksi kata kerja adalah...",
        "correct": "menguji stabilitas sediaan krim",
        "distractors": [
            "uji stabilitas sediaan krim dilakukan",
            "penguji stabilitas sediaan krim terlaksana",
            "terujinya stabilitas pada sediaan krim",
            "keberhasilan pengujian stabilitas sediaan krim"
        ],
        "formula": {
            "title": "PARALELISME SINTAKSIS ILMIAH",
            "latex": "\\text{Pola: } \\text{menganalisis} \\dots \\text{menentukan} \\dots \\implies \\text{menguji}",
            "legend": "• Kesejajaran gramatikal verba aktif transitif berprefiks me-"
        },
        "hints": {
            "concept": "Kesejajaran bentuk mengharuskan verba dalam deret koordinatif menggunakan imbuhan yang seragam.",
            "execution": "Karena dua verba sebelumnya berprefiks me- (menganalisis, menentukan), kata ketiga harus 'menguji'."
        }
    },
    {
        "id": "ind_lanjut-lat-e-15",
        "materi": "KOHESI & KOHERENSI WACANA",
        "topic": "Konjungsi Koordinatif Antarkalimat Sebab-Akibat",
        "stem": "Perhatikan pasangan kalimat berikut:<br><em>'Pemerintah menaikkan tarif pajak pertambahan nilai sebesar 12%. [...] daya beli masyarakat pada sektor barang sekunder mengalami kontraksi yang cukup signifikan.'</em><br>Konjungsi antarkalimat yang paling tepat untuk mengisi bagian rumpang agar menunjukkan hubungan konsekuensi kausalitas adalah...",
        "correct": "Oleh karena itu,",
        "distractors": [
            "Sebaliknya,",
            "Meskipun demikian,",
            "Selain itu,",
            "Akan tetapi,"
        ],
        "formula": {
            "title": "KONJUNGSI ANTARKALIMAT KAUSAL",
            "latex": "\\text{Premis Sebab} + \\text{[Oleh karena itu,]} \\to \\text{Konsekuensi Logis Akibat}",
            "legend": "• 'Oleh karena itu' menandai simpulan akibat logis antarkalimat dalam teks eksposisi"
        },
        "hints": {
            "concept": "Pahami hubungan logika antara kenaikan tarif pajak (sebab) dan penurunan daya beli (akibat).",
            "execution": "Gunakan konjungsi antarkalimat penanda akibat formal: 'Oleh karena itu,'."
        }
    },
    {
        "id": "ind_lanjut-lat-e-16",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Pendekatan Strukturalisme Genetik (Lucien Goldmann)",
        "stem": "Pendekatan sosiologi sastra yang digagas oleh Lucien Goldmann, yang mengkaji hubungan dialektis antara struktur intrinsik karya sastra dengan pandangan dunia (*world view*) kelas sosial pengarangnya dalam periode historis tertentu, disebut pendekatan...",
        "correct": "strukturalisme genetik",
        "distractors": [
            "formalismo Rusia murni",
            "stilistika linguistik kuantitatif",
            "dekonstruksi pascastrukturalis Derrida",
            "ekokritik biosentrisme lingkungan"
        ],
        "formula": {
            "title": "STRUKTURALISME GENETIK GOLDMANN",
            "latex": "\\text{Struktur Karya} \\iff \\text{Pandangan Dunia (World View)} \\iff \\text{Struktur Sosial Historis}",
            "legend": "• Menjembatani analisis intrinsik teks sastra dengan kondisi sosio-historis masyarakat penciptanya"
        },
        "hints": {
            "concept": "Lucien Goldmann memadukan strukturalisme intrinsik teks sastra dengan latar belakang historis kelas sosial pembuatnya.",
            "execution": "Pendekatan ini dikenal dengan nama strukturalisme genetik (genetic structuralism)."
        }
    },
    {
        "id": "ind_lanjut-lat-e-17",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Ragam Leksikon Akademik Baku (PUEBI/EYD V)",
        "stem": "Dalam penulisan naskah akademik, pilihan kata harus mengacu pada ejaan resmi bahasa Indonesia yang baku (EYD Edisi V). Kelompok kata berikut yang seluruhnya merupakan kata serapan baku adalah...",
        "correct": "hipotesis, analisis, sintesis, metodologi",
        "distractors": [
            "hipotesa, analisa, sintesa, metoda",
            "hipotesis, analisa, sintesis, metodik",
            "hipotesa, analisis, sintesa, metode",
            "hipotese, analisir, sintetis, metodologi"
        ],
        "formula": {
            "title": "STANDAR BAKU KATA SERAPAN (EYD V)",
            "latex": "\\text{Akhiran -is/-sis}: \\text{hypothesis} \\to \\text{hipotesis}, \\text{analysis} \\to \\text{analisis}",
            "legend": "• Pola serapan Yunani/Latin baku dalam KBBI VI dan EYD V mengadopsi -sis dan -is"
        },
        "hints": {
            "concept": "Bentuk baku serapan kata berakhiran -is/-sis: hipotesis (bukan hipotesa), analisis (bukan analisa), sintesis (bukan sintesa).",
            "execution": "Pilih deretan kata yang seluruhnya menggunakan akhiran baku bahasa Indonesia."
        }
    },
    {
        "id": "ind_lanjut-lat-e-18",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Analisis Bias Bahasa dalam Wacana Jurnalistik",
        "stem": "Perhatikan kutipan berita berikut:<br><em>'Aparat keamanan terpaksa mengambil tindakan tegas terukur terhadap gerombolan perusuh yang memblokade jalan protokol.'</em><br>Penggunaan eufemisme <em>'tindakan tegas terukur'</em> dan leksikon berkonotasi negatif peyoratif <em>'gerombolan perusuh'</em> memperlihatkan adanya strategi pembingkaian wacana (*media framing*) untuk...",
        "correct": "melegitimasi penggunaan kekerasan oleh aparat dan mendelegitimasi aksi demonstran",
        "distractors": [
            "menyajikan fakta peristiwa secara berimbang sesuai kode etik jurnalistik netral",
            "meningkatkan empati publik terhadap penderitaan massa demonstran",
            "menyamarkan identitas kedua belah pihak agar tidak menimbulkan kepanikan sosial",
            "mengedukasi masyarakat mengenai tata tertib lalu lintas jalan protokol perkotaan"
        ],
        "formula": {
            "title": "ANALISIS WACANA KRITIS (FAIRCLOUGH/ENTMAN)",
            "latex": "\\text{Leksikon Ideologis} \\implies \\text{Legitimasi Kekuasaan} + \\text{Marginalisasi Pihak Tertuduh}",
            "legend": "• Pilihan kata pada wacana berita merefleksikan keberpihakan ideologis pembingkain (framing)"
        },
        "hints": {
            "concept": "Eufemisme melembutkan tindakan aparat, sedangkan kata 'gerombolan perusuh' memberi label kriminal pada demonstran.",
            "execution": "Tujuannya adalah melegitimasi aksi aparat dan mendelegitimasi para demonstran di mata publik."
        }
    },
    {
        "id": "ind_lanjut-lat-e-19",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Pendekatan Pragmatik Sastra",
        "stem": "Kritik sastra yang menitikberatkan keberhasilan sebuah karya fiksi berdasarkan sejauh mana karya tersebut mampu mendidik budi pekerti, menggugah katarsis emosional, dan menanamkan nilai moral kepada pembacanya menerapkan pendekatan...",
        "correct": "pragmatik (horatius: dulce et utile)",
        "distractors": [
            "mimetik murni",
            "objektif struktural",
            "ekspresif biographical",
            "arkeologi teks hermeneutika murni"
        ],
        "formula": {
            "title": "PENDEKATAN PRAGMATIK ABRAMS",
            "latex": "\\text{Pragmatik} \\iff \\text{Fokus pada Efek Estetik & Moralitas terhadap Pembaca}",
            "legend": "• Berakar dari doktrin klasik Horatius: karya sastra harus dulce (menyenangkan) dan utile (bermanfaat)"
        },
        "hints": {
            "concept": "Pendekatan pragmatik berfokus pada pembaca (audiens) dan dampak etis, moral, maupun emosional yang ditimbulkan karya.",
            "execution": "Perhatikan kata kunci 'mendidik budi pekerti' dan 'dampak kepada pembacanya'."
        }
    },
    {
        "id": "ind_lanjut-lat-e-20",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Penyusunan Rumusan Masalah Penelitian",
        "stem": "Dalam proposal penelitian ilmiah tingkat lanjut, rumusan masalah yang baik harus memenuhi kriteria operasional, dapat diuji secara empiris (*researchable*), dan tidak ambigu. Rumusan masalah berikut yang memenuhi kriteria ilmiah tersebut adalah...",
        "correct": "Bagaimanakah pengaruh konsentrasi ekstrak daun kelor terhadap laju penghambatan bakteri Staphylococcus aureus?",
        "distractors": [
            "Apakah daun kelor merupakan tumbuhan ciptaan Tuhan yang paling mulia bagi kesehatan manusia?",
            "Mengapa masyarakat di desa pedalaman lebih menyukai pengobatan tradisional daripada medis modern?",
            "Bukankah penggunaan daun kelor sudah terbukti manjur sejak zaman dahulu kala di pelosok Nusantara?",
            "Bagaimana cara kita meyakinkan para dokter bahwa daun kelor lebih ampuh daripada antibiotik sintesis?"
        ],
        "formula": {
            "title": "STANDAR RUMUSAN MASALAH PENELITIAN",
            "latex": "\\text{Rumusan Masalah} \\iff \\text{Operasional, terukur empiris, & menghubungkan variabel penelitian}",
            "legend": "• Menghindari pertanyaan bernada normatif filosofis, retoris, atau asumtif apriori"
        },
        "hints": {
            "concept": "Rumusan masalah ilmiah harus menghubungkan variabel yang terukur secara kuantitatif atau kualitatif empiris.",
            "execution": "Pilih rumusan yang menghubungkan variabel bebas (konsentrasi ekstrak) dan variabel terikat (laju penghambatan bakteri)."
        }
    },
    {
        "id": "ind_lanjut-lat-e-21",
        "materi": "PRAGMATIK WACANA & TINDAK TUTUR",
        "topic": "Deiksis Wacana Sosial",
        "stem": "Perhatikan kalimat dalam surat dinas berikut:<br><em>'Sehubungan dengan surat <strong>tersebut</strong>, kami memohon kesediaan <strong>Bapak</strong> untuk menghadiri rapat pleno besok pagi.'</em><br>Kata <em>'tersebut'</em> dan <em>'Bapak'</em> berturut-turut merepresentasikan penerapan deiksis...",
        "correct": "wacana anafora dan sosial honorifik",
        "distractors": [
            "tempat ruang proksimal dan persona pertama",
            "wacana katafora dan deiksis temporal absolut",
            "persona ketiga jamak dan deiksis spasial distal",
            "sosial peyoratif dan deiksis waktu relatif"
        ],
        "formula": {
            "title": "TIPOLOGI DEIKSIS PRAGMATIK",
            "latex": "\\text{Deiksis Wacana (Tersebut)} + \\text{Deiksis Sosial (Bapak)}",
            "legend": "• 'Tersebut' merujuk teks sebelumnya (anafora); 'Bapak' mencerminkan tata kesantunan relasi hierarki sosial (honorifik)"
        },
        "hints": {
            "concept": "Deiksis wacana merujuk bagian wacana terdahulu/berikutnya, deiksis sosial merujuk status hierarki sosial pembicara dan lawan bicara.",
            "execution": "'Tersebut' merujuk surat sebelumnya (wacana anafora) dan 'Bapak' menunjukkan penghormatan sosial (honorifik)."
        }
    },
    {
        "id": "ind_lanjut-lat-e-22",
        "materi": "KOHESI & KOHERENSI WACANA",
        "topic": "Kohesi Gramatikal Elipsis (Pelesapan)",
        "stem": "Perhatikan kalimat majemuk bertingkat berikut:<br><em>'Profesor Hendrawan menyajikan makalah tentang kecerdasan artifisial di sesi pleno pertama, sedangkan Dr. Laila [Ø] di sesi pleno kedua.'</em><br>Pelesapan konstituen verba <em>'menyajikan makalah tentang kecerdasan artifisial'</em> pada klausa kedua (ditandai dengan [Ø]) merupakan perwujudan kohesi gramatikal...",
        "correct": "elipsis (pelesapan)",
        "distractors": [
            "substitusi verbal",
            "referensi demonstratif",
            "repetisi anafora leksikal",
            "konjungsi korelatif formal"
        ],
        "formula": {
            "title": "KOHESI GRAMATIKAL ELIPSIS",
            "latex": "[A + V + O] + [B + \\emptyset + \\text{Ket}] \\implies \\emptyset = \\text{Elipsis Verba Predikat}",
            "legend": "• Penghilangan unsur konstituen yang sudah disebutkan sebelumnya demi efisiensi kalimat tanpa merusak makna"
        },
        "hints": {
            "concept": "Elipsis adalah peniadaan atau penghilangan kata atau konstituen yang maknanya dapat dipahami dari konteks kalimat sebelumnya.",
            "execution": "Pelesapan predikat 'menyajikan makalah' disebut elipsis."
        }
    },
    {
        "id": "ind_lanjut-lat-e-23",
        "materi": "KRITIK SASTRA & APRESIASI",
        "topic": "Pendekatan Ekspresif Sastra",
        "stem": "Penelaahan naskah drama komedi karya Arifin C. Noer yang menitikberatkan penyelidikan biografi, latar belakang kejiwaan, pengalaman masa kecil, dan riwayat hidup sastrawan untuk menafsirkan motif penciptaan teks sastra merupakan penerapan pendekatan...",
        "correct": "ekspresif (biographical criticism)",
        "distractors": [
            "objektif struktural murni",
            "mimetik sosio-ekologis",
            "pragmatik resepsi pembaca",
            "dekonstruksi gramatikal semantik"
        ],
        "formula": {
            "title": "PENDEKATAN EKSPRESIF SASTRA",
            "latex": "\\text{Ekspresif} \\iff \\text{Karya sastra sebagai pancaran emosi, visi, & biografi pengarang}",
            "legend": "• Menggunakan fakta riwayat hidup sastrawan sebagai instrumen primer dalam menafsirkan teks karya sastra"
        },
        "hints": {
            "concept": "Pendekatan ekspresif memandang karya sastra sebagai ekspresi perasaan, temperamen, dan pengalaman biografi pengarang.",
            "execution": "Penyelidikan riwayat hidup pengarang merupakan ciri khas pendekatan ekspresif."
        }
    },
    {
        "id": "ind_lanjut-lat-e-24",
        "materi": "TEKS AKADEMIK & KARYA ILMIAH",
        "topic": "Pembedaan Hasil Penelitian (Results) vs Pembahasan (Discussion)",
        "stem": "Dalam anatomi artikel jurnal ilmiah internasional, perbedaan fundamental antara subbab Hasil (*Results*) dan subbab Pembahasan (*Discussion*) terletak pada...",
        "correct": "Hasil menyajikan deskripsi temuan data empiris secara objektif, sedangkan Pembahasan menafsirkan makna temuan, mengaitkannya dengan teori/pustaka terdahulu, dan menguraikan implikasinya.",
        "distractors": [
            "Hasil memuat analisis statistik komparatif mendalam, sedangkan Pembahasan hanya mengulang data tabel secara naratif.",
            "Hasil berisi perdebatan teoretis filsafat ilmu, sedangkan Pembahasan berisi rincian metode pengumpulan data lapangan.",
            "Hasil menguraikan simpulan akhir naskah, sedangkan Pembahasan memuat latar belakang masalah penelitian.",
            "Hasil merupakan ringkasan abstrak satu paragraf, sedangkan Pembahasan berisi lampiran kuesioner mentah."
        ],
        "formula": {
            "title": "DEMARKASI HASIL VS PEMBAHASAN",
            "latex": "\\text{Hasil} = \\text{What was found}; \\quad \\text{Pembahasan} = \\text{What it means in broader context}",
            "legend": "• Pembahasan wajib mengonfirmasi atau menyangkal hipotesis serta membandingkan dengan literatur relevan"
        },
        "hints": {
            "concept": "Hasil memaparkan data apa adanya, sedangkan pembahasan memberi interpretasi ilmiah, justifikasi teori, dan posisi kebaruan studi.",
            "execution": "Pilih opsi yang menjelaskan peran penafsiran dan pengaitan teori pada bagian Pembahasan."
        }
    },
    {
        "id": "ind_lanjut-lat-e-25",
        "materi": "LOGIKA WACANA & PENALARAN",
        "topic": "Logical Fallacy Straw Man",
        "stem": "Dalam suatu seminar lingkungan hidup, Pembicara A mengusulkan: <em>'Sebaiknya kota kita memperbanyak jalur sepeda dan membatasi kendaraan pribadi di jalan protokol saat jam sibuk untuk menekan polusi udara.'</em> Pembicara B menanggapi: <em>'Pembicara A ingin melarang semua warga memiliki mobil dan memaksa lansia serta ibu hamil mengayuh sepeda sejauh puluhan kilometer setiap hari!'</em> Kesesatan berpikir (*fallacy*) yang dilakukan oleh Pembicara B adalah...",
        "correct": "straw man fallacy (memutarbalikkan argumen lawan menjadi bentuk ekstrem)",
        "distractors": [
            "argumentum ad populum (berlindung di balik suara mayoritas)",
            "slippery slope (mengaitkan rentetan bencana tanpa argumen perantara)",
            "circular reasoning (argumen berputar-putar tautologis)",
            "false dilemma (membatasi opsi hanya menjadi dua pilihan kaku)"
        ],
        "formula": {
            "title": "STRAW MAN FALLACY",
            "latex": "\\text{Straw Man} \\iff \\text{Menyederhanakan/mendistorsi argumen lawan secara ekstrem lalu menyerangnya}",
            "legend": "• Menuduh 'ingin melarang semua orang punya mobil' padahal usulannya hanya membatasi saat jam sibuk"
        },
        "hints": {
            "concept": "Straw man terjadi saat seseorang mendistorsi atau melebih-lebihkan argumen lawan menjadi karikatur ekstrem yang mudah diserang.",
            "execution": "Pembicara B membuat argumen orang-orangan jerami dengan mengatakan lawan ingin melarang seluruh mobil dan menyiksa lansia."
        }
    }
]
