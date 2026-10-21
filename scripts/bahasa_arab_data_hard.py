# -*- coding: utf-8 -*-
"""
bahasa_arab_data_hard.py
-------------------------
25 Authentic Hard Practice Questions for TKA 2026 Bahasa Arab (SMA/MA Bahasa & Budaya / Agama).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: arb-lat-h-01 .. arb-lat-h-25
"""

BAHASA_ARAB_HARD_ITEMS = [
    {
        "id": "arb-lat-h-01",
        "materi": "BALAGHAH: ILMU BAYAN (AT-TASYBIH)",
        "topic": "Analisis Rukun Tasybih dan Tasybih Baligh dalam Retorika Sastra",
        "stem": "Perhatikan bait syair balaghah berikut ini:\n'أَنْتَ نَجْمٌ فِي رِفْعَةٍ وَضِيَاءٍ ... تَجْتَلِيكَ العُيُونُ شَرْقًا وَغَرْبًا'\n(Engkau laksana bintang dalam hal keluhuran dan cahaya terang ... mata memandangmu kagum dari ufuk timur hingga ufuk barat).\nDalam bait di atas, penyair menyerupakan sang tokoh (أَنْتَ) dengan bintang (نَجْمٌ) dalam hal keluhuran (رِفْعَةٍ) tanpa menghadirkan huruf/alat tasybih (seperti كَـ atau مِثْلَ). Ditinjau dari kaidah ilmu bayan, kategori tasybih yang tidak menyebutkan adat tasybih dinamakan...",
        "correct": "Tasybih Mu'akkad (تَشْبِيهٌ مُؤَكَّدٌ - tasybih yang dihapuskan peranti perbandingannya untuk memperkuat penegasan keserupaan).",
        "distractors": [
            "Tasybih Mursal (تَشْبِيهٌ مُرْسَلٌ - tasybih yang secara eksplisit menyebutkan huruf perumpamaan ka'anna atau ka).",
            "Tasybih Mujmal (تَشْبِيهٌ مُجْمَلٌ - tasybih yang menghapuskan segi keserupaan wajhusy syabah dari kalimat).",
            "Isti'arah Makniyyah (penghapusan total terhadap musyabbah bih yang hanya menyisakan sifat bawaannya).",
            "Majaz Mursal 'Alaqah Juz'iyyah (penyebutan sebagian organ untuk memaksudkan keseluruhan tubuh)."
        ],
        "formula": {
            "title": "KLASIFIKASI TASYBIH BERDASARKAN ADAT TASYBIH",
            "latex": "\\text{Tasybih} = \\begin{cases} \\text{Sebut Adat Tasybih:} & \\mathbf{\\text{Tasybih Mursal (كَـ / مِثْلَ)}} \\\\ \\mathbf{\\text{Hapus Adat Tasybih:}} & \\mathbf{\\text{Tasybih Mu'akkad (أَنْتَ نَجْمٌ)}} \\\\ \\text{Hapus Wajhusy Syabah:} & \\text{Tasybih Mujmal} \\\\ \\text{Hapus Adat \\& Wajh:} & \\text{Tasybih Baligh} \\end{cases}",
            "legend": "• Menunjukkan keindahan retorika sastra Arab tinggi dalam mempertegas pujian"
        },
        "hints": {
            "concept": "Tasybih yang TIDAK menyebutkan adat tasybih (alat pembanding) disebut Tasybih Mu'akkad. Jika adat disebutkan disebut Mursal.",
            "execution": "Pilih: Tasybih Mu'akkad (تَشْبِيهٌ مُؤَكَّدٌ)."
        }
    },
    {
        "id": "arb-lat-h-02",
        "materi": "BALAGHAH: ILMU BAYAN (AL-ISTI'ARAH)",
        "topic": "Distingsi Isti'arah Tashrihiyyah vs Isti'arah Makniyyah",
        "stem": "Cermati firman Allah Swt. dalam QS. Ibrahim ayat 1 berikut:\n'كِتَابٌ أَنْزَلْنَاهُ إِلَيْكَ لِتُخْرِجَ النَّاسَ مِنَ الظُّلُمَاتِ إِلَى النُّورِ'\n(Sebuah Kitab yang Kami turunkan kepadamu agar engkau mengeluarkan manusia dari kegelapan-kegelapan menuju cahaya terang benderang).\nDalam ayat di atas, kata 'الظُّلُمَاتِ' (kegelapan) dipinjam untuk memaksudkan 'kekafiran/kesesatan', dan 'النُّورِ' (cahaya) dipinjam untuk memaksudkan 'keimanan/petunjuk'. Karena musyabbah-nya dibuang dan musyabbah bih-nya (zhulumat dan an-nur) ditegaskan secara eksplisit (*tashrih*), maka gaya bahasa ini digolongkan sebagai...",
        "correct": "Isti'arah Tashrihiyyah (اسْتِعَارَةٌ تَصْرِيحِيَّةٌ - metafora eksplisit di mana musyabbah bih-nya ditegaskan secara jelas dalam teks).",
        "distractors": [
            "Isti'arah Makniyyah (اسْتِعَارَةٌ مَكْنِيَّةٌ - metafora tersirat di mana musyabbah bih-nya disembunyikan dan hanya disisakan kelazimannya).",
            "Tasybih Dhimni (penyerupaan terselubung yang disimpulkan dari susunan wacana tanpa rukun tasybih formal).",
            "Majaz Mursal 'Alaqah Sababiyyah (penggunaan kata sebab untuk memaksudkan akibat yang ditimbulkan).",
            "Jinas Isytiqaq (keserupaan akar kata bunyi tanpa keterkaitan makna kiasan metaforis)."
        ],
        "formula": {
            "title": "DIKOTOMI ISTI'ARAH (TASHRIHIYYAH VS MAKNIYYAH)",
            "latex": "\\text{Isti'arah} \\implies \\begin{cases} \\mathbf{\\text{Musyabbah Bih Ditampakkan:}} & \\mathbf{\\text{Isti'arah Tashrihiyyah (الظُّلُمَاتِ = الكُفْر)}} \\\\ \\text{Musyabbah Bih Disembunyikan:} & \\text{Isti'arah Makniyyah (Hanya tinggal lawazim-nya)} \\end{cases}",
            "legend": "• Tashrihiyyah: menyatakan secara gamblang lafadz peminjam (musyabbah bih)"
        },
        "hints": {
            "concept": "Jika musyabbah bih-nya disebutkan secara eksplisit (seperti an-nuur untuk petunjuk, az-zhulumaat untuk kesesatan), majaz itu adalah Isti'arah Tashrihiyyah.",
            "execution": "Pilih: Isti'arah Tashrihiyyah (اسْتِعَارَةٌ تَصْرِيحِيَّةٌ)."
        }
    },
    {
        "id": "arb-lat-h-03",
        "materi": "BALAGHAH: ILMU BADI' (AL-MUHASSINAT AL-MA'NAWIYYAH)",
        "topic": "Analisis Bentuk Gaya Bahasa Thibaq Ijab vs Thibaq Salab",
        "stem": "Cermati ayat Al-Qur'an dalam QS. Az-Zumar ayat 9 berikut:\n'قُلْ هَلْ يَسْتَوِي الَّذِينَ يَعْلَمُونَ وَالَّذِينَ لَا يَعْلَمُونَ'\n(Katakanlah: Adakah sama orang-orang yang mengetahui dengan orang-orang yang tidak mengetahui?).\nKeindahan gaya bahasa (*muhassinaat ma'nawiyyah*) yang mempertemukan dua kata yang berlawanan makna pada ayat tersebut dinamakan...",
        "correct": "Thibaq Salab (طِبَاقُ السَّلْبِ - pertemuan dua kata berlawanan di mana yang satu berbentuk positif/itsbat dan yang lainnya berbentuk negatif/nafyi).",
        "distractors": [
            "Thibaq Ijab (طِبَاقُ الإِيجَابِ - pertemuan dua kata berlawanan yang sama-sama berbentuk positif tanpa partikel negasi seperti al-lail wan-nahar).",
            "Muqabalah (penyandingan dua kalimat atau lebih yang masing-masing memiliki lawan kata secara sejajar).",
            "Jinas Taam (kesamaan bunyi dua kata secara mutlak dalam jumlah huruf, harakat, urutan, dan jenis huruf namun beda makna).",
            "Saja' Murashsha' (kesamaan rima huruf akhir pada potongan-potongan kalimat prosa berirama)."
        ],
        "formula": {
            "title": "DIKOTOMI THIBAQ (IJAB VS SALAB)",
            "latex": "\\text{Thibaq (Antitesis)} = \\begin{cases} \\text{Kata Positif } \\iff \\text{ Kata Positif:} & \\text{Thibaq Ijab (اللَّيْلُ } \\iff \\text{ النَّهَارُ)} \\\\ \\mathbf{\\text{Kata Positif } \\iff \\text{ Kata Negatif (Nafyi):}} & \\mathbf{\\text{Thibaq Salab (يَعْلَمُونَ } \\iff \\text{ لَا يَعْلَمُونَ)}} \\end{cases}",
            "legend": "• Thibaq salab menggunakan partikel peniadaan (seperti Laa atau Lam) pada kata yang sama"
        },
        "hints": {
            "concept": "Pertentangan antara bentuk positif (يَعْلَمُونَ) dan bentuk negatif nafi (لَا يَعْلَمُونَ) dari kata yang sama disebut Thibaq Salab (طِبَاقُ السَّلْبِ).",
            "execution": "Pilih: Thibaq Salab (طِبَاقُ السَّلْبِ)."
        }
    },
    {
        "id": "arb-lat-h-04",
        "materi": "TATA BAHASA NAHWU: AF'ALUSY SYURU'",
        "topic": "Hukum Khabar Fi'il Syuru' (Ja'ala, Thafiqa, Syara'a, Akhadza)",
        "stem": "Dalam rumpun *Af'alur Raja' wal-Muqarabah wasy-Syuru'*, kelompok *Af'alusy Syuru'* (seperti: شَرَعَ، أَنْشَأَ، طَفِقَ، جَعَلَ، أَخَذَ) bermakna 'mulai melakukan pekerjaan'. Syarat gramatikal MUTLAK bagi khabar dari Af'alusy Syuru' adalah...",
        "correct": "Wajib berupa Jumlah Fi'liyyah yang predikatnya fi'il mudhari' dan WAJIB BERSIH / TERLARANG (mumtani') dimasuki partikel 'أَنْ' mashdariyyah.",
        "distractors": [
            "Wajib dimasuki partikel 'أَنْ' mashdariyyah tanpa kecuali agar maknanya sah.",
            "Wajib berupa isim mufrad jamid yang berkedudukan majrur bil-kasrah.",
            "Boleh memilih antara fi'il madhi atau fi'il amar sesuai kehendak mutakallim.",
            "Wajib berupa syibh al-jumlah dari susunan zharf makan dan majrur mutsanna."
        ],
        "formula": {
            "title": "HUKUM KHABAR AF'ALUSY SYURU'",
            "latex": "\\text{Fi'il Syuru' (شَرَعَ / طَفِقَ)} + \\text{Isim Syuru' Marfu'} + \\mathbf{\\text{Khabar (Fi'il Mudhari' TANPA أَنْ - Imtina'ul Iqtiran)}}",
            "legend": "• Contoh sah: 'شَرَعَ الطَّالِبُ يَكْتُبُ' (Haram: 'شَرَعَ الطَّالِبُ أَنْ يَكْتُبَ' karena syuru' menunjukkan saat ini/hal)"
        },
        "hints": {
            "concept": "Khabar af'alusy syuru' (mulai berbuat) WAJIB berupa fi'il mudhari' dan DILARANG KERAS (mumtani') dimasuki 'أَنْ' karena syuru' bermakna sedang dimulai saat ini.",
            "execution": "Pilih opsi: Wajib berupa fi'il mudhari' dan terlarang (mumtani') dimasuki partikel 'an'."
        }
    },
    {
        "id": "arb-lat-h-05",
        "materi": "TATA BAHASA NAHWU: ILTIQA'US SAKINAIN",
        "topic": "Kaidah Kasrah 'Aridhah untuk Mencegah Pertemuan Dua Sukun",
        "stem": "Perhatikan pertemuan dua kata berikut:\n'قَالَتِ اخْرُجْ عَلَيْهِنَّ' atau kalimat 'اسْتَمِعِ الكَلَامَ'.\nKata 'اسْتَمِعْ' aslinya berakhiran sukun sebagai fi'il amar, dan huruf pertama dari kata 'الكَلَامَ' juga sukun (lam ta'rif). Mengapa huruf 'ain pada 'اسْتَمِعْ' diubah harakatnya menjadi kasrah ('اسْتَمِعِ الكَلَامَ')?",
        "correct": "Li Tafadi Iltiqa'is-Sakinain (harakat kasrah insidental/'aridhah untuk menghindari bertemunya dua huruf sukun yang mustahil diucapkan dalam fonologi bahasa Arab fusha).",
        "distractors": [
            "Karena kata tersebut kemasukan huruf jar tersembunyi yang mewajibkan harakat kasrah.",
            "Karena kata 'الكَلَامَ' berkedudukan sebagai mudhaf ilaih yang mengkasrahkan kata sebelumnya.",
            "Karena fi'il amar tersebut berubah fungsi menjadi isim mufrad mu'annats makhfudh.",
            "Sebagai tanda bahwa pekerjaan tersebut dilakukan oleh dua orang mutsanna di masa lampau."
        ],
        "formula": {
            "title": "KAIDAH FONOLOGIS ILTIQA'US SAKINAIN",
            "latex": "\\text{اسْتَمِعْ (Sukun 1)} + \\text{الْكَلَامَ (Sukun 2)} \\xrightarrow{\\mathbf{\\text{Iltiqa'us Sakinain}}} \\mathbf{\\text{اسْتَمِعِ الْكَلَامَ (Kasrah 'Aridhah)}}",
            "legend": "• Kaidah dasar fonotaktik Arab: 'Al-ashlu fil-harakah 'inda iltiqa'is-sakinain al-kasr'"
        },
        "hints": {
            "concept": "Dalam bahasa Arab, bertemunya dua huruf mati/sukun (iltiqa'us sakinain) dihindari dengan mengkasrahkan huruf sukun pertama (kasrah 'aridhah).",
            "execution": "Pilih: Menghindari bertemunya dua huruf sukun (li tafadi iltiqa'is-sakinain)."
        }
    },
    {
        "id": "arb-lat-h-06",
        "materi": "TATA BAHASA NAHWU: I'RAB TAQDIRI",
        "topic": "I'rab Taqdiri pada Isim Maqshur (Ta'adz-dzur) dan Isim Manqush (Tsiqal)",
        "stem": "Cermati kalimat berikut:\n'جَاءَ القَاضِي مَعَ الفَتَى إِلَى المَحْكَمَةِ.'\n(Telah datang sang hakim bersama pemuda itu ke pengadilan).\nAnalisis gramatikal yang TEPAT mengenai tanda I'rab pada kata 'القَاضِي' (Isim Manqush) dan 'الفَتَى' (Isim Maqshur) pada kalimat di atas adalah...",
        "correct": "القَاضِي marfu' dengan dhommah muqaddarah karena tsiqal (berat diucapkan), sedangkan الفَتَى majrur dengan kasrah muqaddarah karena ta'adz-dzur (kemustahilan menerima harakat pada alif).",
        "distractors": [
            "Keduanya marfu' dengan tanda zhahir yang tampak jelas di akhir huruf secara fonetis.",
            "القَاضِي majrur dengan ya' sukun mutsanna, sedangkan الفَتَى manshub dengan fathah jazm.",
            "القَاضِي marfu' karena ta'adz-dzur, sedangkan الفَتَى majrur karena tsiqal berat diucapkan.",
            "Keduanya berstatus mabni di atas sukun mutlak dan tidak memiliki kedudukan I'rab."
        ],
        "formula": {
            "title": "DISTINGSI I'RAB TAQDIRI: MAQSHUR VS MANQUSH",
            "latex": "\\begin{cases} \\mathbf{\\text{Isim Maqshur (الفَتَى):}} & \\text{Muqaddarah 'alal-Alif } (\\mathbf{\\text{Ta'adz-dzur / Mustahil}} \\text{ berharakat)} \\\\ \\mathbf{\\text{Isim Manqush (القَاضِي):}} & \\text{Muqaddarah 'alal-Yaa' } (\\mathbf{\\text{Tsiqal / Berat}} \\text{ pada Rafa' \\& Jar)} \\end{cases}",
            "legend": "• Isim manqush hanya menampakkan harakat zhahir pada saat nashab (رَأَيْتُ القَاضِيَ)"
        },
        "hints": {
            "concept": "Isim Maqshur (berakhir alif) dihukumi ta'adz-dzur (mustahil berharakat). Isim Manqush (berakhir ya') pada rafa' & jar dihukumi tsiqal (berat diucapkan).",
            "execution": "Pilih: Al-Qadhi marfu' dhommah muqaddarah tsiqal; Al-Fata majrur kasrah muqaddarah ta'adz-dzur."
        }
    },
    {
        "id": "arb-lat-h-07",
        "materi": "TATA BAHASA NAHWU: IDHAFAH LAFHZIYYAH",
        "topic": "Perbedaan Idhafah Ma'nawiyyah vs Idhafah Lafzhiyyah",
        "stem": "Dalam susunan kata 'طَالِبُ العِلْمِ' (pencari ilmu), hubungan penyandarannya adalah Idhafah Ma'nawiyyah yang memberi faedah *ta'rif* (pendefinisian ma'rifah). Namun pada kalimat 'هَذَا رَجُلٌ حَسَنُ الخُلُقِ' (Ini adalah pria yang baik budi pekertinya), hubungan penyandarannya dinamakan Idhafah Lafzhiyyah karena...",
        "correct": "Mudhaf-nya berupa isim sifat musyabbahah/isim fa'il yang disandarkan kepada ma'mul-nya, yang semata-mata berfungsi untuk takhfif (meringankan lafadz pengucapan dengan membuang tanwin) tanpa memberi faedah ta'rif.",
        "distractors": [
            "Mudhaf-nya berposisi sebagai huruf jar rahasia yang mengharuskan kata kedua berharakat fathah.",
            "Mudhaf ilaih-nya berupa kata kerja fi'il madhi yang diubah secara paksa menjadi kata benda.",
            "Susunan tersebut hanya boleh diucapkan pada saat pembacaan teks proklamasi kemerdekaan.",
            "Kedua kata tersebut saling bertentangan secara semantik dan membentuk makna negatif kutukan."
        ],
        "formula": {
            "title": "KARAKTERISTIK IDHAFAH LAFHZIYYAH",
            "latex": "\\text{Isim Sifat (حَسَنُ)} + \\text{Ma'mul-nya (الخُلُقِ)} \\implies \\mathbf{\\text{Idhafah Lafzhiyyah (Faedah: Takhfif Tanwin)}}",
            "legend": "• Ciri khas: mudhaf pada idhafah lafzhiyyah boleh kemasukan 'Al-' bila bersambung dengan ma'rifah"
        },
        "hints": {
            "concept": "Idhafah lafzhiyyah terjadi bila mudhaf berupa sifat (isim fa'il, maf'ul, sifat musyabbahah) yang disandarkan ke ma'mul-nya, bertujuan meringankan lafadz (takhfif) bukan mema'rifahkan.",
            "execution": "Pilih: Mudhaf berupa isim sifat yang disandarkan ke ma'mul-nya berfungsi takhfif tanpa memberi faedah ta'rif."
        }
    },
    {
        "id": "arb-lat-h-08",
        "materi": "TATA BAHASA NAHWU: BAB TANAZU'",
        "topic": "Konsep At-Tanazu' fil 'Amal antara Mazhab Bashrah dan Kufah",
        "stem": "Cermati kalimat klasik berikut:\n'أَكْرَمْتُ وَأَكْرَمَنِي الأُسْتَاذُ' atau 'أَكْرَمَنِي وَأَكْرَمْتُ الأُسْتَاذَ'.\nDalam gramatika nahwu tingkat tinggi, fenomena ketika dua amil (dua kata kerja) saling berebut pengaruh untuk mengamalkan satu objek/subjek isim zhahir di belakangnya dinamakan *At-Tanazu' fil 'Amal*. Menurut kaidah mayoritas ulama Mazhab Bashrah, amil yang lebih diutamakan untuk beramal secara langsung pada isim zhahir tersebut adalah...",
        "correct": "Amil kedua (al-'aamil ats-thaanii) karena letaknya yang lebih dekat (li qurbihi) dengan isim zhahir tersebut.",
        "distractors": [
            "Amil pertama (al-'aamil al-awwal) karena memiliki hak prioritas mendahului (li sabaqihi) menurut ulama Kufah.",
            "Kedua amil beramal bersama-sama secara merger sehingga isim zhahir menyandang dua harakat sekaligus.",
            "Isim zhahir tersebut digugurkan hak i'rab-nya dan diganti dengan dhamir mustatir wujuban.",
            "Tidak ada amil yang beramal, dan isim zhahir tersebut beralih fungsi menjadi munada mustaghats."
        ],
        "formula": {
            "title": "BAB TANAZU' FIL 'AMAL (تَنَازُعُ العَامِلَيْنِ)",
            "latex": "\\text{Amil 1} + \\text{Amil 2} + \\mathbf{\\text{Ma'mul Zhahir}} \\implies \\begin{cases} \\mathbf{\\text{Mazhab Bashrah:}} & \\mathbf{\\text{Amil Kedua (Li Qurbihi / Lebih Dekat)}} \\\\ \\text{Mazhab Kufah:} & \\text{Amil Pertama (Li Sabaqihi / Lebih Dahulu)} \\end{cases}",
            "legend": "• Bashrah mengamalkan amil kedua, sedangkan amil pertama diisi dhamir (idhmor)"
        },
        "hints": {
            "concept": "Dalam bab Tanazu', ulama Bashrah mengutamakan amil kedua untuk beramal pada isim zhahir karena faktor kedekatan jarak (li qurbihi).",
            "execution": "Pilih: Amil kedua (al-'aamil ats-thaanii) karena letaknya yang lebih dekat (li qurbihi)."
        }
    },
    {
        "id": "arb-lat-h-09",
        "materi": "SHOROF & MORFOLOGI: KAIDAH IBDAL (الإِبْدَالُ)",
        "topic": "Penggantian Ta' Ifti'al menjadi Tha' (ط) setelah Huruf Isti'la' Ithbaq",
        "stem": "Kata dasar 'صَبَرَ' (shabara - sabar) ketika dimasukkan ke wazan 'افْتَعَلَ' (ifta'ala) seharusnya berbunyi 'اصْتَبَرَ' (ishtabara). Namun dalam kaidah shorof fusha, huruf ta' ifti'al wajib diganti (*ibdal*) menjadi huruf tha' ('اصْطَبَرَ'). Alasan fonologis morfologis dilakukannya pergantian huruf tersebut adalah...",
        "correct": "Untuk menyelaraskan artikulasi makhraj bunyi ta' yang tipis agar sesuai dengan sifat huruf shad yang tebal (isti'la' dan ithbaq), sehingga ucapan menjadi harmonis dan mudah dilafalkan.",
        "distractors": [
            "Karena huruf ta' melambangkan perbuatan malas yang tidak pantas disematkan pada sifat sabar.",
            "Karena huruf shad adalah huruf vokal panjang yang tidak boleh berdampingan dengan konsonan gigi.",
            "Untuk mengubah makna kata kerja pasif menjadi kata kerja perintah imperatif langsung.",
            "Karena huruf tha' adalah huruf penutup kalender hijriyah yang wajib diabadikan dalam teks tertulis."
        ],
        "formula": {
            "title": "KAIDAH IBDAL WAZAN IFTA'ALA (ص، ض، ط، ظ)",
            "latex": "\\text{صَبَرَ} + \\text{افْتَعَلَ} \\to \\text{اصْتَبَرَ} \\xrightarrow{\\mathbf{\\text{Ibdal Ta' } \\to \\text{ Tha'}}} \\mathbf{\\text{اصْطَبَرَ (Ishtabara)}}",
            "legend": "• Ta' ifti'al diganti Tha' tebal jika fa' fi'il berupa huruf Ithbaq (Shad, Dhad, Tha', Zha')"
        },
        "hints": {
            "concept": "Huruf ta' pada ifta'ala diganti tha' (ط) jika huruf pertamanya adalah huruf ithbaq (shad, dhad, tha', zha') demi keselarasan fonologis makhraj tebal (ithbaq).",
            "execution": "Pilih: Menyelaraskan artikulasi makhraj bunyi ta' tipis dengan huruf shad tebal (isti'la' & ithbaq)."
        }
    },
    {
        "id": "arb-lat-h-10",
        "materi": "SHOROF & MORFOLOGI: WAZAN ISTAF'ALA",
        "topic": "Faedah Makna Al-I'tiqad / At-Tahawwul pada Wazan Istaf'ala",
        "stem": "Dalam bahasa Arab, kalimat 'اسْتَحْسَنَ المُعَلِّمُ إِجَابَةَ الطَّالِبِ' menggunakan fi'il wazan 'اسْتَفْعَلَ' (istaf'ala). Makna gramatikal yang terkandung dalam kata 'اسْتَحْسَنَ' (istahsana) pada kalimat tersebut adalah...",
        "correct": "Al-I'tiqad / Ar-Ru'yah (meyakini atau menganggap sesuatu memiliki sifat tertentu, yaitu guru menganggap jawaban murid tersebut baik).",
        "distractors": [
            "At-Talab semata (meminta atau memohon agar murid mempercantik gaya tulisannya).",
            "As-Sairurah (perubahan bentuk wujud dari kertas usang menjadi lembaran emas).",
            "Al-Muthawa'ah (akibat pasrah dari tindakan memukul meja ujian berulang kali).",
            "Al-Mubalaghah fin-Nafyi (penolakan mutlak terhadap seluruh isi lembar jawaban)."
        ],
        "formula": {
            "title": "RAGAM FAEDAH WAZAN اسْتَفْعَلَ",
            "latex": "\\text{Wazan اسْتَفْعَلَ} = \\begin{cases} \\text{1. At-Talab (Meminta):} & \\text{اسْتَغْفَرَ (Minta ampun)} \\\\ \\mathbf{\\text{2. Al-I'tiqad (Menganggap):}} & \\mathbf{\\text{اسْتَحْسَنَ (Menganggap baik)}} \\\\ \\text{3. Ash-Shairurah (Menjadi):} & \\text{اسْتَحْجَرَ الطِّينُ (Tanah mengeras jadi batu)} \\end{cases}",
            "legend": "• Menggambarkan kekayaan derivasi semantik bahasa Arab dalam satu timbangan wazan"
        },
        "hints": {
            "concept": "Wazan istaf'ala tidak selalu berarti meminta (thalab). Pada kata 'istahsana' maknanya adalah al-i'tiqad (menganggap/meyakini baik).",
            "execution": "Pilih: Al-I'tiqad / Ar-Ru'yah (menganggap sesuatu memiliki sifat baik)."
        }
    },
    {
        "id": "arb-lat-h-11",
        "materi": "SHOROF & MORFOLOGI: FI'IL MUDHA'AF TSULATSI",
        "topic": "Kaidah Fakkul Idgham saat Fi'il Mudha'af Bersambung Dhamir Rafa' Mutaharrik",
        "stem": "Fi'il mudha'af tsulatsi 'مَدَّ' (madda - membentangkan/mengulurkan) memiliki dua huruf dal yang di-tasydid (*idgham*). Apabila kata kerja ini dikonjugasikan dengan dhamir mutakallim 'أَنَا' (saya telah membentangkan), maka kaidah shorof yang WAJIB diberlakukan adalah...",
        "correct": "Fakkul Idgham (فَكُّ الإِدْغَامِ - wajib mengurai tasydid menjadi dua huruf dal terpisah: مَدَدْتُ / madadtu karena bersambung dengan dhamir rafa' mutaharrik).",
        "distractors": [
            "Wujubul Idgham (wajib mempertahankan tasydid sehingga berbunyi maddtu dengan sukun rangkap).",
            "Ibdal (mengganti huruf dal kedua menjadi huruf ya' sehingga berbunyi madaytu).",
            "Hadzful Fa' (membuang huruf mim awal sehingga hanya tersisa huruf daddtu).",
            "Qalbul Waw (mengubah kata kerja madda menjadi fi'il mu'tal ajwaf maada)."
        ],
        "formula": {
            "title": "KAIDAH FAKKUL IDGHAM FI'IL MUDHA'AF",
            "latex": "\\text{مَدَّ} + \\text{Dhamir Rafa' Mutaharrik (تُ)} \\xrightarrow{\\mathbf{\\text{Wajib Urai Tasydid (Fakk)}}} \\mathbf{\\text{مَدَدْتُ (Madadtu)}}",
            "legend": "• Idgham wajib diurai (fakk) jika lam fi'il disukunkan saat bertemu dhamir ta', na, atau nun niswah"
        },
        "hints": {
            "concept": "Bila fi'il mudha'af bersambung dengan dhamir rafa' mutaharrik (seperti tu, ta, ti, na), tasydid WAJIB diurai (fakkul idgham): 'مَدَدْتُ'.",
            "execution": "Pilih: Fakkul Idgham (wajib mengurai tasydid menjadi dua dal terpisah: مَدَدْتُ)."
        }
    },
    {
        "id": "arb-lat-h-12",
        "materi": "TATA BAHASA NAHWU: USLUBUL IKHTISHASH",
        "topic": "I'rab Isim Mukhtash (Manshub 'ala al-Ikhtishash)",
        "stem": "Perhatikan kalimat pengkhususan (*uslubul ikhtishash*) berikut ini:\n'نَحْنُ ... نَبْنِي مُسْتَقْبَلَ الوَطَنِ بِسَوَاعِدِنَا.'\n(Kami, ... , membangun masa depan bangsa dengan tangan-tangan kami sendiri).\nKata yang TEPAT untuk mengisi posisi Isim Mukhtash (yang berkedudukan manshub dengan fi'il mahdzuf takdirnya 'أَخُصُّ' atau 'أَعْنِي') adalah...",
        "correct": "الشَّبَابَ (asy-syabaaba - isim ma'rifah manshub bil-fathah 'alal-ikhtishash).",
        "distractors": [
            "الشَّبَابُ (asy-syabaabu - marfu' dengan dhommah yang keliru karena menyangka sebagai khabar nahnu).",
            "الشَّبَابِ (asy-syabaabi - majrur dengan kasrah yang tidak memiliki landasan gramatikal).",
            "أَيُّهَا الشَّبَابُ بِالرَّفْعِ (bentuk munada yang mengubah susunan menjadi kalimat panggilan terpisah).",
            "شَبَابٌ (syabaabun - nakirah bertanwin yang menyalahi syarat pokok isim mukhtash yang harus ma'rifah)."
        ],
        "formula": {
            "title": "USLUBUL IKHTISHASH (أُسْلُوبُ الاِخْتِصَاصِ)",
            "latex": "\\text{Dhamir Mutakallim (نَحْنُ)} + \\mathbf{\\text{Isim Mukhtash Manshub (الشَّبَابَ)}} \\implies [\\text{Bi Fi'lin Mahdzuuf Taqdiiruhu: أَعْنِي / أَخُصُّ}]",
            "legend": "• Isim mukhtash selalu ma'rifah dan manshub, terletak di antara dua tanda pisah penjelas"
        },
        "hints": {
            "concept": "Isim mukhtash setelah dhamir mutakallim (nahnu) berkedudukan manshub bil-fathah atas fi'il mahdzuf yang ditakdirkan (a'nii/akhushu).",
            "execution": "Pilih kata ma'rifah manshub: 'الشَّبَابَ' (asy-syabaaba)."
        }
    },
    {
        "id": "arb-lat-h-13",
        "materi": "TATA BAHASA NAHWU: USLUBUT TAHDZIR",
        "topic": "Struktur Kalimat Peringatan Bahaya (Tahdzir) Menggunakan 'إِيَّاكَ'",
        "stem": "Dalam kaidah peringatan bahaya (*uslubut tahdzir*), susunan kalimat 'إِيَّاكَ وَالكَذِبَ!' (Waspadalah engkau dari sifat dusta!) mengandung struktur I'rab yang sangat presisi. Analisis I'rab yang TEPAT mengenai kedudukan kata 'إِيَّاكَ' dan 'الكَذِبَ' pada kalimat tersebut adalah...",
        "correct": "إِيَّاكَ berkedudukan sebagai maf'ul bih manshub (atas fi'il mahdzuf wujuban 'احْذَرْ'), dan الكَذِبَ adalah maf'ul bih manshub atas fi'il mahdzuf lain ('وَاحْذَرِ الكَذِبَ').",
        "distractors": [
            "إِيَّاكَ adalah mubtada' marfu' fardhu, sedangkan الكَذِبَ adalah khabar marfu' bil-dhommah.",
            "إِيَّاكَ adalah huruf jar istimewa, sedangkan الكَذِبَ adalah isim majrur bil-fathah.",
            "Keduanya adalah isim mutsanna mabni di atas alif penanda peringatan masa lampau.",
            "إِيَّاكَ adalah isim fi'il amar, sedangkan الكَذِبَ adalah fa'il marfu' mutlaq."
        ],
        "formula": {
            "title": "ANATOMI I'RAB USLUB TAHDZIR (إِيَّاكَ وَالكَذِبَ)",
            "latex": "\\underbrace{\\text{إِيَّاكَ}}_{\\text{Maf'ul Bih } (\\text{Fi'il: احْذَرْ})} + \\text{حرف العطف} + \\underbrace{\\text{الْكَذِبَ}}_{\\text{Maf'ul Bih } (\\text{Fi'il: احْذَرْ / بَاعِدْ})}",
            "legend": "• Menunjukkan elipsis sintaksis (hadzf al-'aamil wujuban) dalam ragam retorika peringatan bahaya"
        },
        "hints": {
            "concept": "Pada uslub tahdzir 'إِيَّاكَ وَالكَذِبَ', kata 'iyyaaka' berposisi sebagai maf'ul bih dari fi'il mahdzuf (ihdzar), dan 'al-kadziba' juga maf'ul bih manshub.",
            "execution": "Pilih opsi: 'إِيَّاكَ' maf'ul bih manshub atas fi'il mahdzuf 'احْذَرْ', dan 'الكَذِبَ' maf'ul bih atas fi'il mahdzuf lainnya."
        }
    },
    {
        "id": "arb-lat-h-14",
        "materi": "TATA BAHASA NAHWU: AF'ALUL MADH WADZ-DZAM",
        "topic": "Struktur Kalimat Pujian Menggunakan 'نِعْمَ' dan Kedudukan Al-Makhshush bil-Madh",
        "stem": "Perhatikan kalimat pujian (*af'alul madh*) berikut ini:\n'نِعْمَ الخُلُقُ الصِّدْقُ فِي التَّعَامُلِ مَعَ النَّاسِ.'\n(Sebaik-baik budi pekerti adalah kejujuran dalam berinteraksi dengan sesama manusia).\nDalam kaidah nahwu, kedudukan I'rab dari kata 'الصِّدْقُ' sebagai *Al-Makhshush bil-Madh* (subjek yang secara khusus dipuji) adalah...",
        "correct": "Mubtada' Mu'akhkhar yang marfu' bil-dhommah (di mana jumlah fi'liyyah 'نِعْمَ الخُلُقُ' sebelumnya berposisi sebagai Khabar Muqaddam).",
        "distractors": [
            "Maf'ul bih manshub bil-fathah dari fi'il madh yang mendahuluinya.",
            "Mudhaf ilaih majrur bil-kasrah yang menyatu dengan fa'il al-khuluqu.",
            "Tamyiz nakirah manshub penjelas keraguan jenis perbuatan terpuji.",
            "Badal muthabaq yang menggantikan posisi maf'ul muthlaq mahdzuf."
        ],
        "formula": {
            "title": "I'RAB AF'ALUL MADH (نِعْمَ)",
            "latex": "\\underbrace{\\text{نِعْمَ (Fi'il Madh) } + \\text{ الخُلُقُ (Fa'il)}}_{\\mathbf{\\text{Khabar Muqaddam (Jumlah Fi'liyyah)}}} + \\underbrace{\\text{الصِّدْقُ}}_{\\mathbf{\\text{Mubtada' Mu'akhkhar (Makhshush bil-Madh)}}}",
            "legend": "• Boleh juga di-i'rab sebagai Khabar dari Mubtada' Mahdzuf (Taqdiruhu: Huwa ash-Shidqu)"
        },
        "hints": {
            "concept": "Al-Makhshush bil-madh (kata 'الصِّدْقُ') di-i'rab sebagai Mubtada' Mu'akhkhar, dan kalimat 'نِعْمَ الخُلُقُ' di depannya adalah Khabar Muqaddam.",
            "execution": "Pilih: Mubtada' Mu'akhkhar marfu' bil-dhommah (khabar muqaddam adalah jumlah sebelumnya)."
        }
    },
    {
        "id": "arb-lat-h-15",
        "materi": "BALAGHAH: ILMU MA'ANI (AL-QASHR)",
        "topic": "Metode Pembatasan Makna (Thuruqul Qashr) Menggunakan 'إِنَّمَا'",
        "stem": "Cermati sabda Rasulullah saw. yang terkenal berikut:\n'إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ'\n(Hanyasanya segala amal perbuatan itu bergantung pada niatnya).\nDalam ilmu ma'ani, kalimat di atas menggunakan salah satu metode pembatasan (*Thuruqul Qashr*), yaitu dengan peranti 'إِنَّمَا'. Unsur yang menjadi *Al-Maqshur* (perkara yang dibatasi) dan *Al-Maqshur 'Alaih* (tujuan pembatasan) secara berturut-turut adalah...",
        "correct": "Al-Maqshur adalah 'الأَعْمَالُ' (segala amal perbuatan), dan Al-Maqshur 'Alaih adalah 'بِالنِّيَّاتِ' (ketergantungan pada niat).",
        "distractors": [
            "Al-Maqshur adalah 'بِالنِّيَّاتِ', sedangkan Al-Maqshur 'Alaih adalah huruf 'إِنَّمَا'.",
            "Al-Maqshur adalah huruf 'إِنَّمَا', sedangkan Al-Maqshur 'Alaih adalah lafadz 'الأَعْمَالُ'.",
            "Kedua-duanya adalah Al-Maqshur tanpa adanya Al-Maqshur 'Alaih dalam metode innama.",
            "Al-Maqshur adalah ganjaran pahala surga, sedangkan Al-Maqshur 'Alaih adalah keikhlasan hati."
        ],
        "formula": {
            "title": "ANATOMI AL-QASHR BI INNAMA (إِنَّمَا)",
            "latex": "\\text{إِنَّمَا} + \\underbrace{\\text{الأَعْمَالُ}}_{\\mathbf{\\text{Al-Maqshur (Yang Dibatasi)}}} + \\underbrace{\\text{بِالنِّيَّاتِ}}_{\\mathbf{\\text{Al-Maqshur 'Alaih (Tujuan Akhir Pembatasan)}}}",
            "legend": "• Pada metode 'إِنَّمَا', al-maqshur 'alaih selalu terletak di akhir kalimat (wujuban mu'akhkhar)"
        },
        "hints": {
            "concept": "Pada qashr dengan 'إِنَّمَا', Al-Maqshur terletak setelah innama ('الأَعْمَالُ'), dan Al-Maqshur 'Alaih terletak di bagian paling akhir ('بِالنِّيَّاتِ').",
            "execution": "Pilih: Al-Maqshur adalah 'الأَعْمَالُ' dan Al-Maqshur 'Alaih adalah 'بِالنِّيَّاتِ'."
        }
    },
    {
        "id": "arb-lat-h-16",
        "materi": "FAHM AL-MAQRU': HISTORIOGRAFI NUSANTARA",
        "topic": "Analisis Catatan Ibnu Battuta di Samudera Pasai (Abad ke-14)",
        "stem": "Bacalah teks petikan catatan perjalanan pengembara Maroko Ibnu Battuta (*Tuhfatun Nuzzhar*) berikut:\n'وَصَلْنَا إِلَى جَزِيرَةِ جَاوَى (سُومَطْرَة)، وَهِيَ جَزِيرَةٌ خَضْرَاءُ خَصِيبَةٌ، وَحَاكِمُهَا مَلِكٌ مُسْلِمٌ فَاضِلٌ يُدْعَى المَلِكَ الظَّاهِرَ. وَكَانَ المَلِكُ يُحِبُّ الفُقَهَاءَ وَالعُلَمَاءَ، وَيَجْلِسُ مَعَهُمْ لِمُنَاقَشَةِ المَسَائِلِ الدِّينِيَّةِ عَلَى المَذْهَبِ الشَّافِعِيِّ، وَقَدْ شَاهَدْتُ أَهْلَ البَلَدِ يُجَاهِدُونَ فِي سَبِيلِ اللهِ وَيَتَّصِفُونَ بِالتَّوَاضُعِ وَحُسْنِ الضِّيَافَةِ.'\nBerdasarkan catatan Ibnu Battuta di atas, karakteristik kepemimpinan Sultan Malikuz Zhahir di Kesultanan Samudera Pasai adalah...",
        "correct": "Seorang penguasa muslim yang mencintai kaum intelektual/ulama fikih, gemar berdiskusi mendalami hukum Islam bermazhab Syafi'i, serta memimpin rakyat yang ramah dan gigih.",
        "distractors": [
            "Seorang raja otoriter yang mewajibkan seluruh pengembara asing membayar upeti emas batangan murni di dermaga pelabuhan.",
            "Pemimpin militer yang menolak interaksi diplomatik dengan para pedagang muslim dari kawasan Afrika Utara.",
            "Raja yang mewajibkan rakyatnya beralih keyakinan memeluk agama kuno dataran Persia.",
            "Penguasa pulau tandus yang melarang penanaman pohon kelapa dan rempah cengkeh di wilayah kerajaannya."
        ],
        "formula": {
            "title": "ANALISIS TEKSTUAL RIHLATU IBNU BATTUTA",
            "latex": "\\text{الملك الظاهر (Samudera Pasai)} \\implies \\begin{cases} \\mathbf{\\text{Mencintai Ulama \\& Fikih Mazhab Syafi'i}} \\\\ \\mathbf{\\text{Diskusi Ilmiah Keagamaan}} \\\\ \\mathbf{\\text{Rakyat Ramah (Husnud Dhiyafah) \\& Gigih}} \\end{cases}",
            "legend": "• Menjadi bukti historis primer pengamalan mazhab Syafi'i di Nusantara sejak abad ke-14 M"
        },
        "hints": {
            "concept": "Teks menegaskan: 'حَاكِمُهَا مَلِكٌ مُسْلِمٌ فَاضِلٌ ... يُحِبُّ الفُقَهَاءَ وَالعُلَمَاءَ ... عَلَى المَذْهَبِ الشَّافِعِيِّ' (raja utama yang mencintai ulama dan fikih mazhab Syafi'i).",
            "execution": "Pilih opsi: Penguasa muslim yang mencintai ulama/fikih Syafi'i, gemar berdiskusi ilmiah, dan rakyatnya ramah/gigih."
        }
    },
    {
        "id": "arb-lat-h-17",
        "materi": "FAHM AL-MAQRU': SOSIOLOGI IBNU KHALDUN",
        "topic": "Konsep Al-'Ashabiyyah (Solidaritas Sosial) dalam Muqaddimah Ibnu Khaldun",
        "stem": "Cermati teks pemikiran sosiologi politik Ibnu Khaldun berikut:\n'إِنَّ العَصَبِيَّةَ هِيَ الرَّابِطَةُ الِاجْتِمَاعِيَّةُ القَائِمَةُ عَلَى صِلَةِ الرَّحِمِ أَوِ الحِلْفِ، وَهِيَ الأَسَاسُ الَّذِي يَمْنَحُ الجَمَاعَةَ القُدْرَةَ عَلَى الدِّفَاعِ عَنْ نَفْسِهَا، وَالمُطَالَبَةِ بِحُقُوقِهَا، وَتَأْسِيسِ الدُّوَلِ وَالمَمَالِكِ. وَإِذَا ضَعُفَتْ هَذِهِ العَصَبِيَّةُ بِسَبَبِ الإِفْرَاطِ فِي التَّرَفِ وَالرَّخَاءِ، بَدَأَتِ الدَّوْلَةُ فِي الِانْحِدَارِ وَالسُّقُوطِ.'\nInti tesis sosiologis Ibnu Khaldun mengenai eksistensi dan keruntuhan suatu peradaban/negara menurut teks di atas adalah...",
        "correct": "Solidaritas kelompok ('ashabiyyah) merupakan fondasi utama kejayaan dan berdirinya negara, sedangkan pola hidup mewah yang berlebihan (al-ifrath fit-taraf) akan merusak ikatan solidaritas tersebut hingga memicu keruntuhan negara.",
        "distractors": [
            "Negara yang kuat hanya dapat dibangun jika seluruh warga hidup dalam kemewahan harta benda tanpa perlu bekerja.",
            "Kekuasaan politik suatu bangsa semata-mata ditentukan oleh luasnya wilayah tambang minyak bumi di gurun.",
            "Keruntuhan suatu dinasti terjadi akibat terlalu seringnya para pemimpin membaca buku sejarah peradaban kuno.",
            "Hubungan kekerabatan darah wajib dihapus secara total agar negara mampu memenangkan perang antarbangsa."
        ],
        "formula": {
            "title": "SIKLUS PERADABAN IBNU KHALDUN (العَصَبِيَّةُ وَالتَّرَفُ)",
            "latex": "\\mathbf{\\text{العَصَبِيَّةُ (Solidaritas Sosial)}} \\xrightarrow{\\text{Membangun}} \\mathbf{\\text{Kekuatan Negara}} \\xrightarrow{\\text{Taraf (Mewah Berlebih)}} \\mathbf{\\text{Inhidar/Runtuh}}",
            "legend": "• Menunjukkan hukum sosiologis siklus dinasti dalam magnum opus Al-Muqaddimah"
        },
        "hints": {
            "concept": "Ibnu Khaldun menjelaskan bahwa 'ashabiyyah (solidaritas) adalah modal pembangun negara, dan at-taraf (kemewahan berlebih) adalah perusak solidaritas pemicu runtuhnya negara.",
            "execution": "Pilih: Solidaritas fondasi kejayaan negara, sedangkan kemewahan berlebih merusak ikatan dan memicu keruntuhan."
        }
    },
    {
        "id": "arb-lat-h-18",
        "materi": "TATA BAHASA NAHWU: TAQDIMUL KHABAR WUJUUBAN",
        "topic": "Kondisi Wajibnya Khabar Mendahului Mubtada' (Syibh Jumlah & Nakirah Mahdhah)",
        "stem": "Dalam kaidah tata bahasa nahwu, khabar WAJIB mendahului mubtada' (*taqdiimul khabar wujuuban*) pada situasi tertentu. Manakah kalimat berikut yang MENERAPKAN kaidah wajib dahulunya khabar karena alasan: khabar berupa *syibh al-jumlah* (zharf/jar-majrur) dan mubtada'-nya berupa *isim nakirah mahdhah* (nakirah murni tanpa sifat atau idhafah)?",
        "correct": "فِي البَيْتِ رَجُلٌ (fii al-baiti rajulun - wajib mendahulukan khabar fii al-baiti karena mubtada' rajulun adalah nakirah murni).",
        "distractors": [
            "فِي البَيْتِ الرَّجُلُ (khabar boleh mendahului atau diakhirkan karena mubtada' ar-rajulu berbentuk ma'rifah).",
            "فِي البَيْتِ رَجُلٌ كَرِيمٌ (khabar boleh diakhirkan karena mubtada' rajulun telah disifati dengan kariimun).",
            "أَيْنَ المَفَرُّ (wajib dahulunya khabar karena isim istifham memiliki hak shadarul kalam, bukan karena syibh jumlah).",
            "عِنْدِي كِتَابُكَ (khabar boleh diakhirkan karena mudhaf ilaih kaf menjadikannya isim ma'rifah)."
        ],
        "formula": {
            "title": "SYARAT TAQDIMUL KHABAR WUJUUBAN",
            "latex": "\\mathbf{\\text{Khabar Syibh Jumlah (فِي البَيْتِ)}} + \\mathbf{\\text{Mubtada' Nakirah Mahdhah (رَجُلٌ)}} \\implies \\mathbf{\\text{Wajib Taqdimul Khabar}}",
            "legend": "• Bila mubtada' nakirah tidak disifati (ghairu makhshushah), tidak sah diucapkan 'رَجُلٌ فِي البَيْتِ'"
        },
        "hints": {
            "concept": "Khabar wajib mendahului mubtada' jika khabar berupa syibh jumlah (fii al-baiti) dan mubtada' berupa nakirah mahdhah murni tanpa sifat/idhafah ('رَجُلٌ').",
            "execution": "Pilih: 'فِي البَيْتِ رَجُلٌ'."
        }
    },
    {
        "id": "arb-lat-h-19",
        "materi": "TATA BAHASA NAHWU: AN-NAWASIB BIL-FATHAH",
        "topic": "Pengaruh Fa' Sababiyyah (فَـ السَّبَبِيَّةُ) dalam Menashabkan Fi'il Mudhari'",
        "stem": "Perhatikan kalimat bersyarat dalam wacana berikut:\n'لَا تَتَكَاسَلْ عَنْ طَلَبِ العِلْمِ فَتَنْدَمَ فِي كِبَرِكَ.'\n(Janganlah engkau bermalas-malasan dalam menuntut ilmu, sehingga engkau akan menyesal di masa tuamu).\nHarakat huruf mim pada fi'il mudhari' 'فَتَنْدَمَ' berstatus manshub bil-fathah karena...",
        "correct": "Didahului oleh Fa' Sababiyyah yang jatuh setelah kalimat thalab (nahyi / larangan), di mana terdapat 'أَنْ' mudhmarah wujuuban yang menashabkan fi'il mudhari'.",
        "distractors": [
            "Berstatus sebagai fi'il amar mabni di atas fathah karena adanya nun taukid tsaqilah.",
            "Merupakan maf'ul bih dari kata kibaari yang diakhirkan posisinya dalam kalimat.",
            "Tunduk pada kaidah huruf 'athaf biasa yang mengabaikan makna sebab akibat peristiwa.",
            "Berposisi sebagai isim ghairu munsharif yang majrur dengan harakat fathah."
        ],
        "formula": {
            "title": "KAIDAH FA' AS-SABABAYYAH (فَاءُ السَّبَبِيَّةِ)",
            "latex": "\\text{Thalab / Nahyi (لَا تَتَكَاسَلْ)} \\xrightarrow{\\mathbf{\\text{فَـ (Fa' Sababiyyah)}}} \\mathbf{\\text{فَتَنْدَمَ (Manshub bi 'An' Mudhmarah Wujuuban)}}",
            "legend": "• Fa' sababiyyah menashabkan fi'il mudhari' dengan syarat didahului oleh Nafyi Mahdh atau Thalab"
        },
        "hints": {
            "concept": "Fa' Sababiyyah menashabkan fi'il mudhari' (dengan 'an' tersirat secara wajib) apabila didahului oleh thalab (perintah, larangan, doa, istifham) atau nafi.",
            "execution": "Pilih: Didahului Fa' Sababiyyah setelah kalimat thalab/nahyi dengan 'an' mudhmarah wujuuban."
        }
    },
    {
        "id": "arb-lat-h-20",
        "materi": "SHOROF & MORFOLOGI: MASDAR MIMI",
        "topic": "Membedakan Masdar Mimi dari Isim Makan dan Isim Maf'ul",
        "stem": "Perhatikan kalimat berikut:\n'سَعَى المُجْتَهِدُ فِي طَلَبِ الرِّزْقِ مَسْعًى حَمِيدًا.'\nKata 'مَسْعًى' (mas'an) pada kalimat di atas memiliki wazan yang serupa dengan isim makan. Namun secara semantik gramatikal, kata tersebut digolongkan sebagai Masdar Mimi karena...",
        "correct": "Diawali huruf mim za'idah (tambahan) dan bermakna murni masdar hakiki (yaitu semakna dengan kata 'سَعْيًا' - usaha nyata), bukan menunjukkan lokasi tempat terjadinya pekerjaan.",
        "distractors": [
            "Menunjukkan tempat dilangsungkannya ritual lari-lari kecil antara bukit Shafa dan Marwah.",
            "Menunjukkan waktu saat fajar menyingsing sebelum matahari terbit di ufuk timur.",
            "Berfungsi sebagai isim alat yang digunakan untuk menggali sumur zamzam.",
            "Merupakan kata serapan dari dialek bahasa Aram kuno yang tidak memiliki akar kata."
        ],
        "formula": {
            "title": "KARAKTERISTIK MASDAR MIMI (المَصْدَرُ المِيمِيُّ)",
            "latex": "\\text{سَعَى} \\dots \\mathbf{\\text{مَسْعًى حَمِيدًا}} \\iff \\text{Bisa digantikan Masdar Asli: } [\\text{سَعَى } \\dots \\mathbf{\\text{سَعْيًا}} \\text{ حَمِيدًا}]",
            "legend": "• Masdar mimi adalah masdar yang diawali huruf mim za'idah selain wazan mufa'alatun"
        },
        "hints": {
            "concept": "Masdar mimi diawali huruf mim tambahan dan bermakna masdar hakiki (perbuatan/usaha itu sendiri, semakna dengan sa'yan), bukan menunjukkan tempat.",
            "execution": "Pilih: Diawali huruf mim tambahan dan bermakna murni masdar hakiki (semakna dengan sa'yan)."
        }
    },
    {
        "id": "arb-lat-h-21",
        "materi": "BALAGHAH: ILMU BADI' (AL-JINAS)",
        "topic": "Analisis Perbedaan Jinas Taam vs Jinas Naqish / Ghairu Taam",
        "stem": "Cermati ayat Al-Qur'an dalam QS. Ar-Rum ayat 55 berikut:\n'وَيَوْمَ تَقُومُ السَّاعَةُ يُقْسِمُ المُجْرِمُونَ مَا لَبِثُوا غَيْرَ سَاعَةٍ'\n(Dan pada hari terjadinya kiamat, bersumpahlah orang-orang yang berdosa bahwa mereka tidak berdiam di dunia melainkan sesaat saja).\nPada ayat di atas terdapat dua kata yang sama persis susunannya, yaitu 'السَّاعَةُ' (Hari Kiamat) dan 'سَاعَةٍ' (satuan waktu sesaat / satu jam). Keindahan stilistika lafadz (*muhassinaat lafzhiyyah*) ini dinamakan...",
        "correct": "Jinas Taam (جِنَاسٌ تَامٌّ - kesamaan dua kata dalam 4 perkara: jenis huruf, jumlah huruf, harakat, dan urutan huruf, namun memiliki makna yang sama sekali berbeda).",
        "distractors": [
            "Jinas Naqish (جِنَاسٌ نَاقِصٌ - keserupaan dua kata yang memiliki perbedaan pada salah satu dari empat aspek huruf).",
            "Thibaq Ijab (pertemuan dua kata yang saling bertolak belakang maknanya secara hakiki).",
            "Saja' Mutawazi (kesamaan harakat dan rima akhir pada dua kata di ujung bait puisi).",
            "Raddul 'Ajuz 'alas-Shadr (pengulangan kata awal bait pada posisi kata paling akhir bait)."
        ],
        "formula": {
            "title": "SYARAT KESEMPURNAAN JINAS TAAM",
            "latex": "\\text{Lafadz 1 (السَّاعَةُ: Kiamat)} \\iff \\text{Lafadz 2 (سَاعَةٍ: Waktu Sesaat)} \\implies \\mathbf{\\text{Jinas Taam (Sama Huruf, Beda Makna)}}",
            "legend": "• Empat pilar jinas taam: Jenis huruf, Jumlah huruf, Harakat/Bentuk, Urutan huruf"
        },
        "hints": {
            "concept": "Dua kata yang sama persis dalam jenis, jumlah, harakat, dan urutan huruf tetapi memiliki makna yang berbeda disebut Jinas Taam (جِنَاسٌ تَامٌّ).",
            "execution": "Pilih: Jinas Taam (جِنَاسٌ تَامٌّ)."
        }
    },
    {
        "id": "arb-lat-h-22",
        "materi": "FAHM AL-MAQRU': TEKS SAINS & TEKNOLOGI MODERN",
        "topic": "Analisis Wacana Kecerdasan Buatan (الذَّكَاءُ الِاصْطِنَاعِيُّ) dan Etika Sains",
        "stem": "Bacalah teks wacana kontemporer berikut:\n'يُعَدُّ الذَّكَاءُ الِاصْطِنَاعِيُّ ثَوْرَةً تِكْنُولُوجِيَّةً كُبْرَى فِي العَصْرِ الحَدِيثِ، حَيْثُ يُسْهِمُ فِي تَطْوِيرِ مَجَالَاتِ الطِّبِّ وَالهَنْدَسَةِ وَالتَّعْلِيمِ. وَمَعَ ذَلِكَ، يُحَذِّرُ العُلَمَاءُ مِنَ المَخَاطِرِ الأَخْلَاقِيَّةِ المُرْتَبِطَةِ بِانْتِهَاكِ الخُصُوصِيَّةِ وَفِقْدَانِ الوَظَائِفِ التَّقْلِيدِيَّةِ، مِمَّا يَسْتَدْعِي وَضْعَ قَوَانِينَ صَارِمَةٍ لِضَبْطِ اسْتِخْدَامِهِ.'\nBerdasarkan teks di atas, urgensi perumusan regulasi hukum yang ketat (*qawaaniin shaarimah*) dalam penerapan kecerdasan buatan dipicu oleh...",
        "correct": "Kekhawatiran saintis terhadap risiko pelanggaran privasi data pribadi dan hilangnya lapangan pekerjaan konvensional di tengah pesatnya revolusi teknologi.",
        "distractors": [
            "Kekurangan pasokan energi listrik tenaga surya di laboratorium komputer perguruan tinggi.",
            "Keinginan produsen perangkat lunak memonopoli seluruh jaringan satelit komunikasi global.",
            "Penolakan para dokter untuk mengoperasikan alat rontgen sinar-X di ruang gawat darurat.",
            "Kewajiban seluruh siswa menghafal kode bahasa pemrograman mesin dalam naskah kaligrafi."
        ],
        "formula": {
            "title": "ANALISIS IMPLIKASI ETIS TEKNOLOGI (FAHM AL-MAQRU')",
            "latex": "\\text{Revolusi AI (الذكاء الاصطناعي)} \\implies \\begin{cases} \\text{Manfaat:} & \\text{Kedokteran, Rekayasa, Pendidikan} \\\\ \\mathbf{\\text{Risiko:}} & \\mathbf{\\text{Pelanggaran Privasi \\& Hilangnya Pekerjaan}} \\end{cases} \\implies \\mathbf{\\text{Urgensi Regulasi Ketat}}",
            "legend": "• Menunjukkan kompetensi literasi membaca kritis terhadap wacana ilmiah kontemporer berbahasa Arab"
        },
        "hints": {
            "concept": "Teks menyatakan perlunya aturan ketat karena ada risiko: 'انْتِهَاكِ الخُصُوصِيَّةِ وَفِقْدَانِ الوَظَائِفِ التَّقْلِيدِيَّةِ' (pelanggaran privasi dan hilangnya pekerjaan tradisional).",
            "execution": "Pilih opsi: Risiko pelanggaran privasi data dan hilangnya lapangan pekerjaan konvensional."
        }
    },
    {
        "id": "arb-lat-h-23",
        "materi": "TATA BAHASA NAHWU: WAWU MA'IYYAH & MAF'UL MA'AH",
        "topic": "I'rab Maf'ul Ma'ah setelah Wawu Ma'iyyah (Wawu al-Mushahabah)",
        "stem": "Cermati kalimat berikut:\n'سَارَ المُسَافِرُ ... الشَّاطِئِ عِنْدَ غُرُوبِ الشَّمْسِ.'\n(Pengembara itu telah berjalan bersamaan dengan garis pantai saat matahari terbenam).\nKata yang TEPAT untuk menduduki posisi Maf'ul Ma'ah (isim manshub yang terletak setelah Wawu Ma'iyyah bermakna 'bersamaan dengan') adalah...",
        "correct": "وَشَاطِئَ (wa syaathi'a - huruf wawu bermakna ma'a dan isim setelahnya berkedudukan maf'ul ma'ah manshub bil-fathah).",
        "distractors": [
            "وَشَاطِئُ (wa syaathi'u - marfu' dengan dhommah yang keliru karena menyangka sebagai 'athaf kepada musafir).",
            "وَشَاطِئٍ (wa syaathi'in - majrur dengan kasratain tanpa adanya amil jar).",
            "مَعَ شَاطِئًا (penggabungan kata ma'a dengan isim manshub bertanwin yang tidak lazim).",
            "وَالشَّاطِئُ بِالضَّمِّ (berharakat dhommah yang tidak memenuhi fungsi maf'ul ma'ah)."
        ],
        "formula": {
            "title": "I'RAB MAF'UL MA'AH (المَفْعُولُ مَعَهُ)",
            "latex": "\\text{Fi'il (سَارَ)} + \\text{Fa'il (المُسَافِرُ)} + \\mathbf{\\text{Wawu Ma'iyyah (وَـ)}} + \\mathbf{\\text{Maf'ul Ma'ah Manshub (شَاطِئَ)}}",
            "legend": "• Wawu ma'iyyah tidak bisa diartikan sebagai 'athaf serikat kerja bila objeknya tidak mungkin ikut berjalan"
        },
        "hints": {
            "concept": "Karena pantai tidak mungkin ikut berjalan dengan pengembara, wawu di sini adalah Wawu Ma'iyyah (bersamaan dengan), dan kata setelahnya adalah Maf'ul Ma'ah yang MANSHUB: 'وَشَاطِئَ'.",
            "execution": "Pilih: 'وَشَاطِئَ' (wa syaathi'a)."
        }
    },
    {
        "id": "arb-lat-h-24",
        "materi": "BALAGHAH: ILMU MA'ANI (AL-IJAZ WAL-ITHNAB)",
        "topic": "Konsep Ijaz Hadzf (Pembuangan Unsur Kalimat demi Kepadatan Makna)",
        "stem": "Dalam wacana balaghah tinggi, kalimat 'وَاسْأَلِ القَرْيَةَ' (Dan tanyakanlah kepada desa itu - QS. Yusuf: 82) mengandung gaya bahasa *Ijaz bil-Hadzf* (meringkas ungkapan dengan membuang kata tertentu). Kata yang dibuang (*al-mahdzuf*) dalam kalimat tersebut secara logis semantik adalah...",
        "correct": "أَهْلَ (ahla - yang dibuang adalah mudhaf 'penduduk', sehingga takdir kalimat aslinya adalah: 'وَاسْأَلْ أَهْلَ القَرْيَةِ' karena desa berupa bangunan fisik tidak dapat ditanyai).",
        "distractors": [
            "بُيُوتَ (buyuuta - yang dibuang adalah kata rumah-rumah pemukiman).",
            "أَمْوَالَ (amwaala - yang dibuang adalah harta kekayaan desa).",
            "أَشْجَارَ (asyjaara - yang dibuang adalah pepohonan kurma di kebun).",
            "حَيَوَانَاتِ (hayawaanaati - yang dibuang adalah hewan ternak kambing)."
        ],
        "formula": {
            "title": "IJAZ BI HADZFIL MUDHAF (إِيجَازُ الحَذْفِ)",
            "latex": "\\text{وَاسْأَلِ القَرْيَةَ} \\xrightarrow{\\mathbf{\\text{Taqdirul Mahdzuf}}} \\mathbf{\\text{وَاسْأَلْ [أَهْلَ] القَرْيَةِ}} \\implies \\text{Gaya Bahasa: Ijaz bil-Hadzf}",
            "legend": "• Pembuangan kata mudhaf untuk memadatkan pesan tanpa mengurangi kejelasan makna yang dipahami"
        },
        "hints": {
            "concept": "Desa fisik tidak bisa ditanyai. Yang ditanyai adalah penduduknya. Kata yang dibuang (al-mahdzuf) adalah 'أَهْلَ' (penduduk desa).",
            "execution": "Pilih: 'أَهْلَ' (ahla - penduduk desa)."
        }
    },
    {
        "id": "arb-lat-h-25",
        "materi": "TATA BAHASA NAHWU: AMIL NAWASIKH INNA (LA'ALLA & LAITA)",
        "topic": "Perbedaan Semantik Gramatikal antara At-Tarajji (لَعَلَّ) dan At-Tamanni (لَيْتَ)",
        "stem": "Dua saudara amil Inna, yaitu 'لَيْتَ' (laita) dan 'لَعَلَّ' (la'alla), sama-sama memanshubkan isim dan merafa'kan khabar, namun memiliki perbedaan mendasar dalam nuansa makna semantiknya. Perbedaan makna yang TEPAT di antara keduanya adalah...",
        "correct": "لَيْتَ berfungsi untuk at-tamanni (menginginkan sesuatu yang mustahil terjadi atau sangat sulit terwujud), sedangkan لَعَلَّ berfungsi untuk at-tarajji wal-isyfaq (mengharapkan sesuatu yang disukai dan mungkin terwujud, atau mengkhawatirkan hal buruk).",
        "distractors": [
            "لَيْتَ berfungsi untuk memuji sifat dermawan, sedangkan لَعَلَّ berfungsi untuk melarang perbuatan tercela.",
            "لَيْتَ khusus digunakan dalam kalimat masa lampau, sedangkan لَعَلَّ hanya digunakan dalam kalimat masa depan.",
            "لَيْتَ menjazmkan fi'il mudhari', sedangkan لَعَلَّ memajrurkan isim zhahir ber-alif lam.",
            "Keduanya memiliki makna yang identik seratus persen tanpa ada perbedaan retorika sedikit pun."
        ],
        "formula": {
            "title": "DISTINGSI SEMANTIK: LAITA (تَمَنٍّ) VS LA'ALLA (تَرَجٍّ)",
            "latex": "\\begin{cases} \\mathbf{\\text{لَيْتَ (At-Tamanni):}} & \\text{Mengharap hal mustahil (لَيْتَ الشَّبَابَ يَعُودُ يَوْمًا)} \\\\ \\mathbf{\\text{لَعَلَّ (At-Tarajji):}} & \\text{Mengharap hal mungkin terjadi (لَعَلَّ اللهَ يَشْفِينِي)} \\end{cases}",
            "legend": "• Menunjukkan kedalaman rasa bahasa dalam memilih partikel nawasikh yang tepat"
        },
        "hints": {
            "concept": "'Laita' (tamanni) = mengharapkan hal mustahil/sangat sulit terjadi (seperti ingin muda kembali). 'La'alla' (tarajji) = mengharapkan hal yang mungkin terjadi.",
            "execution": "Pilih opsi: Laita untuk at-tamanni (hal mustahil/sulit), La'alla untuk at-tarajji (hal mungkin terwujud/dikhawatirkan)."
        }
    }
]
