# -*- coding: utf-8 -*-
"""
bahasa_arab_data_medium.py
---------------------------
25 Authentic Medium Practice Questions for TKA 2026 Bahasa Arab (SMA/MA Bahasa & Budaya / Agama).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: arb-lat-m-01 .. arb-lat-m-25
"""

BAHASA_ARAB_MEDIUM_ITEMS = [
    {
        "id": "arb-lat-m-01",
        "materi": "TATA BAHASA NAHWU: TAWABI' (NA'AT SABABI)",
        "topic": "Kaidah Struktur dan Kesesuaian Gender pada Na'at Sababi",
        "stem": "Perhatikan kalimat yang mengandung Na'at Sababi berikut ini:\n'زَارَنِي صَدِيقٌ ... أَبُوهُ فِي المَدِينَةِ.'\n(Telah mengunjungiku seorang kawan yang ayahnya ... di kota).\nDalam kaidah nahwu, Na'at Sababi mengikuti isim sebelumnya (man'ut) dalam hal i'rab dan ke-ma'rifah-annya, namun mengikuti isim sesudahnya (fa'il sababi) dalam hal jenis (mudzakkar/mu'annats) dan selalu berbentuk mufrad. Bentuk na'at sababi yang BENAR untuk mengisi titik-titik tersebut adalah...",
        "correct": "كَرِيمٌ (kariimun - berbentuk mufrad mudzakkar marfu' mengikuti jenis 'أَبُوهُ' dan i'rab rofa' 'صَدِيقٌ').",
        "distractors": [
            "كَرِيمَةٌ (kariimatun - bentuk mu'annats yang keliru karena fa'il isim sesudahnya adalah abuhu yang mudzakkar).",
            "كُرَمَاءُ (kuramaa'u - bentuk jama' taksir yang menyalahi kaidah na'at sababi yang wajib selalu mufrad).",
            "كَرِيمَيْنِ (kariimaini - bentuk mutsanna manshub/majrur yang tidak selaras dengan syarat mufrad).",
            "الكَرِيمُ (al-kariimu - isim ma'rifah yang bertentangan dengan man'ut sebelumnya yang nakirah)."
        ],
        "formula": {
            "title": "KAIDAH NA'AT SABABI",
            "latex": "\\text{Man'ut (صَدِيقٌ: Nakirah, Marfu')} \\iff \\mathbf{\\text{Na'at Sababi (كَرِيمٌ: Mufrad, Mudzakkar)}} \\iff \\text{Fa'il Sababi (أَبُوهُ: Mudzakkar)}",
            "legend": "• Na'at sababi mengikuti man'ut dalam i'rab & ma'rifah/nakirah; mengikuti fa'il-nya dalam mudzakkar/mu'annats, dan selalu mufrad"
        },
        "hints": {
            "concept": "Na'at sababi wajib selalu mufrad. Mengikuti kata sebelumnya (صَدِيقٌ) dalam i'rab (marfu') dan nakirah; mengikuti kata setelahnya (أَبُوهُ) dalam jenis (mudzakkar).",
            "execution": "Pilih: 'كَرِيمٌ' (kariimun)."
        }
    },
    {
        "id": "arb-lat-m-02",
        "materi": "TATA BAHASA NAHWU: ISIM MAUSHUL",
        "topic": "Kesesuaian Isim Maushul Jamak Perempuan (اللاَّتِي / اللَّوَائِي)",
        "stem": "Cermati kalimat rumpang berikut:\n'شَكَرَتْ مُدِيرَةُ المَدْرَسَةِ الطَّالِبَاتِ ... فَزْنَ فِي مُسَابَقَةِ الخَطِّ العَرَبِيِّ.'\n(Kepala sekolah perempuan telah berterima kasih kepada para siswi yang ... telah memenangkan lomba kaligrafi Arab).\nIsim maushul (kata sambung 'yang') yang TEPAT untuk merujuk pada 'الطَّالِبَاتِ' (jama' mu'annats salim) adalah...",
        "correct": "اللاَّتِي (al-laatii - isim maushul khusus untuk kelompok jamak perempuan / jama' mu'annats).",
        "distractors": [
            "الَّذِينَ (al-ladhiina - isim maushul jamak yang khusus digunakan untuk kelompok laki-laki).",
            "الَّتِي (al-latii - isim maushul untuk perempuan tunggal / mufrad mu'annats).",
            "الَّذِي (al-ladhii - isim maushul untuk laki-laki tunggal / mufrad mudzakkar).",
            "اللَّذَانِ (al-ladhaani - isim maushul untuk dua orang laki-laki / mutsanna mudzakkar)."
        ],
        "formula": {
            "title": "PEMETAAN ISIM MAUSHUL",
            "latex": "\\text{الطَّالِبَاتِ (Jama' Mu'annats)} \\implies \\mathbf{\\text{Isim Maushul: اللاَّتِي / اللَّوَائِي}} \\iff \\text{Shilah: فَزْنَ}",
            "legend": "• Isim maushul wajib selaras dengan isim maushul ma'thuf 'alaih dalam gender dan jumlah bilangan"
        },
        "hints": {
            "concept": "Kata 'الطَّالِبَاتِ' adalah jama' mu'annats (perempuan jamak). Isim maushul yang sesuai adalah 'اللاَّتِي' atau 'اللَّوَائِي'.",
            "execution": "Pilih: 'اللاَّتِي' (al-laatii)."
        }
    },
    {
        "id": "arb-lat-m-03",
        "materi": "TATA BAHASA NAHWU: AF'ALUL KHAMSAH",
        "topic": "Tanda I'rab Nashab/Jazm pada Af'alul Khamsah (حَذْفُ النُّونِ)",
        "stem": "Perhatikan kalimat larangan berikut:\n'يَا طُلَّابُ، لَا ... فِي أَدَاءِ وَاجِبَاتِكُمُ المَدْرَسِيَّةِ!'\n(Wahai para siswa, janganlah kalian ... dalam menunaikan tugas-tugas sekolah kalian!).\nBentuk fi'il mudhari' jamak mukhatab (Af'alul Khamsah) yang TEPAT dan majzum setelah Laa an-Nahiyah adalah...",
        "correct": "تُقَصِّرُوا (tuqash-shiruu - majzum dengan membuang huruf nun / hadzfun nun disertai penambahan alif fariqah).",
        "distractors": [
            "تُقَصِّرُونَ (tuqash-shiruuna - marfu' dengan tetap adanya nun / tsubutun nun yang belum dijazmkan).",
            "تُقَصِّرْنَ (tuqash-shirna - mabni di atas sukun khusus untuk jamak mu'annats perempuan).",
            "يُقَصِّرُوا (yuqash-shiruu - bentuk gha'ib orang ketiga yang tidak cocok untuk panggilan langsung yaa thullaab).",
            "قَصَّرْتُمْ (qash-shartum - bentuk fi'il madhi yang tidak dapat didahului partikel laa an-nahiyah)."
        ],
        "formula": {
            "title": "I'RAB AF'ALUL KHAMSAH DALAM KEADAAN MAJZUM",
            "latex": "\\text{لَا النَّاهِيَةُ} + \\mathbf{\\text{Fi'il Af'alul Khamsah (تَفْعَلُونَ)}} \\xrightarrow{\\mathbf{\\text{Hadzfun Nun}}} [\\text{لَا } \\mathbf{\\text{تُقَصِّرُوا}}]",
            "legend": "• Tanda rafa' af'alul khamsah adalah tsubutun nun, tanda nashab dan jazm-nya adalah hadzfun nun"
        },
        "hints": {
            "concept": "Af'alul khamsah (seperti tuqash-shiruuna) jika dimasuki huruf jazm (Laa nahiyah) tanda jazm-nya adalah menghapus huruf nun (hadzfun nun): 'تُقَصِّرُوا'.",
            "execution": "Pilih: 'تُقَصِّرُوا' (tuqash-shiruu)."
        }
    },
    {
        "id": "arb-lat-m-04",
        "materi": "TATA BAHASA NAHWU: ISIM GHAIRU MUNSHARIF",
        "topic": "Tanda I'rab Majrur dengan Fathah pada Isim Ghairu Munsharif",
        "stem": "Isim ghairu munsharif (kata benda yang tidak menerima tanwin) memiliki keunikan tanda I'rab, yaitu majrur dengan harakat fathah sebagai pengganti kasrah selama tidak ber-alif lam dan tidak menjadi mudhaf. Manakah kalimat berikut yang MENERAPKAN kaidah tersebut secara tepat pada wazan shighah muntahal jumuu' 'مَسَاجِدَ'?",
        "correct": "صَلَّيْتُ فِي مَسَاجِدَ كَثِيرَةٍ فِي جَزِيرَةِ جَاوَى (shallaitu fii masaajida katsiiratin - masaajida majrur bil-fathah karena ghairu munsharif dan tanpa alif lam).",
        "distractors": [
            "صَلَّيْتُ فِي مَسَاجِدِ المَدِينَةِ الكَبِيرَةِ (masaajidi berharakat kasrah karena berposisi sebagai mudhaf).",
            "صَلَّيْتُ فِي المَسَاجِدِ الأَثَرِيَّةِ التَّارِيخِيَّةِ (al-masaajidi berharakat kasrah karena memiliki alif lam ma'rifah).",
            "صَلَّيْتُ فِي مَسَاجِدٍ كَثِيرَةٍ بِالتَّنْوِينِ (penambahan tanwin kasrah yang melanggar hukum ghairu munsharif).",
            "صَلَّيْتُ فِي مَسَاجِدُ بِالضَّمَّةِ بَعْدَ حَرْفِ الجَرِّ (pemberian dhommah yang menyalahi fungsi huruf jar fii)."
        ],
        "formula": {
            "title": "I'RAB ISIM GHAIRU MUNSHARIF MAJRUR",
            "latex": "\\text{حَرْفُ الجَرِّ (فِي)} + \\mathbf{\\text{مَسَاجِدَ (Shighah Muntahal Jumuu')}} \\xrightarrow{\\text{Tanpa AL \\& Tanpa Idhafah}} \\mathbf{\\text{Majrur bil-Fathah Niyabatan 'anil-Kasrah}}",
            "legend": "• Isim ghairu munsharif kembali majrur dengan kasrah bila kemasukan 'Al-' atau di-idhafah-kan"
        },
        "hints": {
            "concept": "Isim ghairu munsharif majrur dengan fathah tanpa tanwin syaratnya: tidak ada Alif Lam dan tidak di-idhafah-kan.",
            "execution": "Pilih: 'صَلَّيْتُ فِي مَسَاجِدَ كَثِيرَةٍ' di mana masaajida berfathah dan tidak ber-Al."
        }
    },
    {
        "id": "arb-lat-m-05",
        "materi": "TATA BAHASA NAHWU: AL-HAAL (الحَالُ)",
        "topic": "Syarat Hal Mufradah (Nakirah & Manshubah) dan Shahibul Hal (Ma'rifah)",
        "stem": "Perhatikan kalimat berikut ini:\n'رَجَعَ الفَائِزُ مِنَ المُسَابَقَةِ ... بِفَوْزِهِ العَظِيمِ.'\n(Sang pemenang telah kembali dari perlombaan dalam keadaan ... atas kemenangannya yang gemilang).\nKata yang TEPAT untuk berkedudukan sebagai Haal Mufradah (isim sifat nakirah manshubah yang menerangkan keadaan fa'il saat perbuatan berlangsung) adalah...",
        "correct": "فَرِحًا (farihan - isim nakirah manshub dengan harakat fathatain yang berfungsi sebagai haal).",
        "distractors": [
            "فَرِحٌ (farihun - marfu' dengan dhommatain yang keliru untuk kategori manshubatul asma').",
            "الفَرِحُ (al-farihu - isim ma'rifah ber-alif lam yang menyalahi syarat pokok ke-nakirah-an haal).",
            "فَرِحِينَ (farihiina - jamak yang bertentangan dengan shahibul hal tunggal al-faa'izu).",
            "فَرِحَةً (farihatan - mu'annats yang tidak selaras dengan shahibul hal mudzakkar)."
        ],
        "formula": {
            "title": "STRUKTUR KALIMAT BER-HAAL",
            "latex": "\\text{Fi'il (رَجَعَ)} + \\text{Shahibul Hal Ma'rifah (الفَائِزُ)} + \\mathbf{\\text{Haal Nakirah Manshubah (فَرِحًا)}}",
            "legend": "• Haal adalah jawaban atas pertanyaan 'kaifa' (bagaimana kondisi pelaku/objek saat kejadian)"
        },
        "hints": {
            "concept": "Haal mufradah wajib berupa isim sifat nakirah dan manshub (fathah), serta menyamai shahibul hal (الفَائِزُ) dalam gender dan bilangannya.",
            "execution": "Pilih kata sifat nakirah manshub: 'فَرِحًا' (farihan)."
        }
    },
    {
        "id": "arb-lat-m-06",
        "materi": "TATA BAHASA NAHWU: AT-TAMYIZ (التَّمْيِيزُ)",
        "topic": "Tamyiz Malhuzh Penjelas Isim Tafdhil (مَنْصُوبٌ بِالفَتْحَةِ)",
        "stem": "Cermati kalimat komparatif berikut:\n'إِنْدُونِيسِيَا أَكْبَرُ مِنَ الفِلِبِّينِ ... فِي جَنُوبِ شَرْقِ آسِيَا.'\n(Indonesia lebih besar daripada Filipina ... di kawasan Asia Tenggara).\nKata penjelas kesamaran (Tamyiz Malhuzh manshub bil-fathah) yang TEPAT untuk memperjelas aspek keunggulan ukuran negara pada kalimat tersebut adalah...",
        "correct": "مِسَاحَةً (misaahatan - tamyiz malhuzh manshub dengan harakat fathatain bermakna 'dari segi luas wilayah').",
        "distractors": [
            "مِسَاحَةٌ (misaahatun - berharakat dhommatain yang keliru untuk jabatan i'rab tamyiz).",
            "مِسَاحَةٍ (misaahatin - majrur dengan kasratain yang tidak memenuhi hukum nashab tamyiz).",
            "المِسَاحَةُ (al-misaahatu - isim ma'rifah ber-alif lam yang melanggar sifat kenakiran tamyiz).",
            "بِالمِسَاحَةِ (bil-misaahati - susunan jar majrur yang tidak membentuk pola tamyiz murni)."
        ],
        "formula": {
            "title": "TAMYIZ SETELAH ISIM TAFDHIL",
            "latex": "\\text{Isim Tafdhil (أَكْبَرُ مِنْ)} + \\mathbf{\\text{Tamyiz Malhuzh (مِسَاحَةً - Manshub bil-Fathah)}}",
            "legend": "• Isim nakirah manshub setelah wazan 'af'alu' berfungsi membedakan dan memperjelas spesifikasi keunggulan"
        },
        "hints": {
            "concept": "Setelah isim tafdhil (akbaru min), kata yang menjelaskan aspek keunggulan adalah tamyiz malhuzh berharakat fathatain (manshub nakirah).",
            "execution": "Pilih: 'مِسَاحَةً' (misaahatan)."
        }
    },
    {
        "id": "arb-lat-m-07",
        "materi": "TATA BAHASA NAHWU: MAF'UL LIAJLIH",
        "topic": "Fungsi dan I'rab Maf'ul Liajlih (Al-Maf'ul Lahu)",
        "stem": "Perhatikan kalimat tujuan berikut:\n'يَجْتَهِدُ الطَّالِبُ فِي مُذَاكَرَةِ دُرُوسِهِ ... فِي النَّجَاحِ البَاهِرِ.'\n(Siswa itu bersungguh-sungguh dalam menelaah pelajarannya ... akan kesuksesan yang gilang-gemilang).\nKata yang TEPAT untuk menduduki posisi Maf'ul Liajlih (masdar qolbi manshub yang menjelaskan alasan/motif mengapa perbuatan dilakukan) adalah...",
        "correct": "رَغْبَةً (raghbatan - maf'ul liajlih manshub dengan harakat fathatain bermakna 'karena menginginkan/berhasrat').",
        "distractors": [
            "رَغْبَةٌ (raghbatun - marfu' dengan dhommatain yang tidak sesuai untuk i'rab maf'ul liajlih).",
            "رَاغِبًا (raaghiban - bentuk isim fa'il yang lebih condong menjadi haal daripada masdar qolbi).",
            "رَغْبَةٍ (raghbatin - majrur dengan kasratain tanpa adanya amil pen-jar).",
            "الرَّغْبَةُ (ar-raghbatu - isim ma'rifah yang bukan format baku maf'ul liajlih tunggal)."
        ],
        "formula": {
            "title": "STRUKTUR MAF'UL LIAJLIH",
            "latex": "\\text{Perbuatan (يَجْتَهِدُ)} \\xrightarrow{\\text{Menjawab: 'Li-Maadha?'}} \\mathbf{\\text{Maf'ul Liajlih (رَغْبَةً - Masdar Qolbi Manshub)}}",
            "legend": "• Menjelaskan dorongan emosi batin (harapan, rasa hormat, rasa takut) penyebab terjadinya fi'il"
        },
        "hints": {
            "concept": "Maf'ul liajlih adalah masdar qolbi (hati/keinginan) manshub yang menjawab pertanyaan 'mengapa perbuatan itu dilakukan'.",
            "execution": "Pilih: 'رَغْبَةً' (raghbatan)."
        }
    },
    {
        "id": "arb-lat-m-08",
        "materi": "TATA BAHASA NAHWU: MAF'UL MUTHLAQ",
        "topic": "Tiga Fungsi Maf'ul Muthlaq (Taukid, Bayanun Nau', Bayanul 'Adad)",
        "stem": "Cermati kalimat berikut:\n'شَكَرْتُ الأُسْتَاذَ شُكْرًا جَزِيلًا عَلَى حُسْنِ تَوْجِيهِهِ.'\n(Saya telah berterima kasih kepada guru itu dengan rasa terima kasih yang banyak atas bimbingannya yang baik).\nFungsi gramatikal dari Maf'ul Muthlaq 'شُكْرًا جَزِيلًا' pada kalimat di atas adalah...",
        "correct": "Li Bayaani an-Nau' (menjelaskan jenis atau kualitas dari perbuatan terima kasih tersebut karena diikuti kata sifat).",
        "distractors": [
            "Li Taukidil Fi'li semata (hanya menegaskan perbuatan tanpa memberikan keterangan jenis atau sifat).",
            "Li Bayaanil 'Adad (menjelaskan jumlah kuantitas berapa kali perbuatan dilakukan).",
            "Li Bayaaniz-Zaman (menjelaskan masa atau waktu pelaksanaan akad pertemuan).",
            "Li Bayaanil-Makan (menunjukkan lokasi tempat dilangsungkannya bimbingan belajar)."
        ],
        "formula": {
            "title": "FUNGSI MAF'UL MUTHLAQ",
            "latex": "\\text{Maf'ul Muthlaq} = \\begin{cases} \\text{1. Taukid:} & \\text{شَكَرْتُ شُكْرًا (Menegaskan)} \\\\ \\mathbf{\\text{2. Bayan Nau':}} & \\mathbf{\\text{شَكَرْتُ شُكْرًا جَزِيلًا (Disifati / Idhafah)}} \\\\ \\text{3. Bayan 'Adad:} & \\text{شَكَرْتُ شَكْرَتَيْنِ (Menghitung frekuensi)} \\end{cases}",
            "legend": "• Kehadiran na'at (جَزِيلًا) mengubah fungsi penegasan murni menjadi penjelas jenis/kualitas perbuatan"
        },
        "hints": {
            "concept": "Jika maf'ul muthlaq diikuti kata sifat (na'at seperti جَزِيلًا) atau mudhaf ilaih, maka fungsinya adalah li bayaani an-nau' (menjelaskan macam/kualitas perbuatan).",
            "execution": "Pilih: Li Bayaani an-Nau' (menjelaskan jenis/kualitas perbuatan)."
        }
    },
    {
        "id": "arb-lat-m-09",
        "materi": "SHOROF & MORFOLOGI: WAZAN FA''ALA (فَعَّلَ)",
        "topic": "Faedah Makna Lit-Taktsir dan Lit-Ta'diyah pada Wazan Fa''ala",
        "stem": "Kata 'قَطَعَ' (qatha'a) bermakna 'memotong'. Namun ketika diubah ke wazan tasydid 'قَطَّعَ' (qath-tha'a), seperti dalam kalimat 'قَطَّعَ اللَّحْمَ إِرَبًا إِرَبًا', penambahan tasydid (*tadh'if*) pada wazan فَعَّلَ tersebut memberikan faedah makna gramatikal...",
        "correct": "At-Taktsir wal-Mubalaghah (menunjukkan intensitas perbuatan yang dilakukan berulang-ulang hingga terpotong menjadi berkeping-keping).",
        "distractors": [
            "Al-Musyarakah (saling memotong secara bergantian antardua kubu pedagang pasar).",
            "At-Talab (memohon dan meminta orang lain untuk memotongkan daging).",
            "As-Sairurah (perubahan zat dari daging segar menjadi daging olahan panggang).",
            "At-Tahwil (mengubah fungsi pisau pemotong menjadi perkakas pajangan dinding)."
        ],
        "formula": {
            "title": "FAEDAH WAZAN فَعَّلَ (TADH'IF 'AIN FI'IL)",
            "latex": "\\text{قَطَعَ (Memotong sekali)} \\xrightarrow{\\mathbf{\\text{Wazan فَعَّلَ}}} \\mathbf{\\text{قَطَّعَ (Memotong berkeping-keping)}} \\implies \\text{Faedah: At-Taktsir (Intensitas/Banyak)}",
            "legend": "• Tasydid pada huruf kedua sering kali melipatgandakan frekuensi dan intensitas kerja"
        },
        "hints": {
            "concept": "Wazan فَعَّلَ (dengan tasydid) memiliki faedah at-taktsir (banyaknya/intensifnya pekerjaan, seperti qath-tha'a = memotong-motong hingga lumat).",
            "execution": "Pilih opsi: At-Taktsir wal-Mubalaghah (intensitas berulang-ulang)."
        }
    },
    {
        "id": "arb-lat-m-10",
        "materi": "SHOROF & MORFOLOGI: WAZAN FAA'ALA (فَاعَلَ)",
        "topic": "Faedah Makna Lil-Musyarakah (Timbal Balik) pada Wazan Faa'ala",
        "stem": "Dalam wacana bahasa Arab, kalimat 'صَافَحَ عَلِيٌّ زَيْدًا' (Ali bersalaman dengan Zaid) menggunakan fi'il wazan 'فَاعَلَ' (faa'ala). Makna gramatikal yang terkandung dalam wazan faa'ala pada kalimat tersebut adalah...",
        "correct": "Al-Musyarakah baina itsnain (perbuatan timbal balik yang dilakukan secara bersamaan oleh dua orang pelaku).",
        "distractors": [
            "At-Takalluf (pemaksaan diri untuk melakukan sesuatu secara susah payah).",
            "Li Nafyil Fi'li (peniadaan mutlak terhadap terjadinya jabat tangan antarteman).",
            "Li Thalabil Ma'rifah (permintaan untuk berkenalan secara formal melalui surat kabar).",
            "Li Muthawa'ati af'ala (akibat otomatis yang ditimbulkan oleh perintah penguasa)."
        ],
        "formula": {
            "title": "FAEDAH WAZAN فَاعَلَ (MUSYARAKAH)",
            "latex": "\\text{Wazan فَاعَلَ (صَافَحَ)} \\implies \\mathbf{\\text{Al-Musyarakah (Saling/Timbal Balik Dua Pihak)}}",
            "legend": "• Fa'il dan maf'ul sama-sama berpartisipasi aktif dalam aksi perbuatan tersebut"
        },
        "hints": {
            "concept": "Wazan فَاعَلَ (faa'ala) paling sering berfaedah lil-musyarakah baina itsnain (saling melakukan perbuatan antardua pihak).",
            "execution": "Pilih: Al-Musyarakah baina itsnain (perbuatan timbal balik dua pelaku)."
        }
    },
    {
        "id": "arb-lat-m-11",
        "materi": "SHOROF & MORFOLOGI: FI'IL MU'TAL AJWAF",
        "topic": "Perubahan Fi'il Mu'tal Ajwaf saat Bersambung dengan Ta' Fa'il",
        "stem": "Fi'il mu'tal ajwaf 'قَالَ' (dia telah berkata) memiliki huruf 'illat alif di tengahnya. Apabila kata kerja ini disambungkan dengan dhamir mutakallim 'أَنَا' (saya berkata), maka terjadi pembuangan huruf 'illat karena bertemunya dua sukun (*iltiqa'us-sakinain*), sehingga bentuk konjugasinya yang TEPAT adalah...",
        "correct": "قُلْتُ (qultu - huruf qaf didhommahkan dan huruf 'illat dibuang).",
        "distractors": [
            "قَالْتُ (qaaltu - kesalahan mempertahankan huruf alif yang menyebabkan bertemunya dua huruf sukun).",
            "قِلْتُ (qiltu - pengkasrahan huruf qaf yang hanya berlaku untuk ajwaf ya'i seperti bi'tu).",
            "قُولْتُ (quultu - penulisan wawu panjang yang keliru saat lam fi'il bersukun).",
            "قَلْتُ (qaltu - pembacaan fathah yang tidak mencerminkan asal wazan wawu yaquulu)."
        ],
        "formula": {
            "title": "KAIDAH I'LAL FI'IL AJWAF (قَالَ $\\to$ قُلْتُ)",
            "latex": "\\text{قَالَ (أَصْلُهُ: قَوَلَ)} + \\text{تُ} \\to \\text{قَوْلْتُ} \\xrightarrow{\\mathbf{\\text{Iltiqa'us-Sakinain}}} \\mathbf{\\text{قُلْتُ (Qultu)}}",
            "legend": "• Dhommah pada huruf awal menunjukkan bahwa huruf 'illat aslinya adalah Wawu (قَالَ - يَقُولُ)"
        },
        "hints": {
            "concept": "Karena fi'il ajwaf 'qaala' berasal dari wawu (yaquulu), saat bersambung dengan dhamir berharakat (ta' mutakallim), alif dibuang dan huruf pertama berharakat dhommah: 'قُلْتُ'.",
            "execution": "Pilih: 'قُلْتُ' (qultu)."
        }
    },
    {
        "id": "arb-lat-m-12",
        "materi": "TATA BAHASA NAHWU: ADWATUL ISTITSNA'",
        "topic": "I'rab Mustatsna dengan Illaa pada Kalimat Tam Mujab",
        "stem": "Perhatikan kalimat pengecualian (istitsna') berikut ini:\n'حَضَرَ المُهَنْدِسُونَ المَشْرُوعَ إِلَّا ... وَاحِدًا كَانَ مُسَافِرًا.'\n(Para insinyur telah menghadiri proyek itu kecuali ... orang yang sedang bepergian).\nKarena kalimat di atas berbentuk *Kalam Tam Mujab* (kalimat sempurna tanpa partikel negasi/nafyi), maka Mustatsna setelah 'إِلَّا' wajib berstatus...",
        "correct": "Wajib manshub bil-fathah: مُهَنْدِسًا (muhandisan).",
        "distractors": [
            "Wajib marfu' bil-dhommah: مُهَنْدِسٌ (muhandisun).",
            "Wajib majrur bil-kasrah: مُهَنْدِسٍ (muhandisin).",
            "Boleh marfu' atau majrur sesuai kehendak pembicara tanpa ada ikatan kaidah.",
            "Mabni di atas sukun karena dianggap sebagai isim istifham penanya."
        ],
        "formula": {
            "title": "HUKUM I'RAB MUSTATSNA BI ILLAA",
            "latex": "\\text{Kalam Taam Muujab (حَضَرَ المُهَنْدِسُونَ)} + \\text{إِلَّا} \\implies \\mathbf{\\text{Wajib Manshub: مُهَنْدِسًا}}",
            "legend": "• Jika kalimat positif (mujab) dan mustatsna minhu disebutkan (taam), mustatsna wajib manshub"
        },
        "hints": {
            "concept": "Pada kalam taam muujab (disebutkan mustatsna minhu dan tidak dinafikan), mustatsna setelah 'illaa' WAJIB manshub.",
            "execution": "Pilih: Wajib manshub bil-fathah: 'مُهَنْدِسًا' (muhandisan)."
        }
    },
    {
        "id": "arb-lat-m-13",
        "materi": "TATA BAHASA NAHWU: MUNADA (المُنَادَى)",
        "topic": "I'rab Munada Mudhaf (Manshub bil-Fathah)",
        "stem": "Cermati kalimat panggilan (nida') berikut ini:\n'يَا ... العِلْمِ، لَا تَبْخَلْ بِمَعْلُومَاتِكَ عَلَى زُمَلَائِكَ!'\n(Wahai ... ilmu, janganlah kamu pelit dengan informasimu kepada rekan-rekanmu!).\nBentuk kata yang TEPAT untuk mengisi posisi Munada Mudhaf (yang berkedudukan I'rab manshub bil-fathah) adalah...",
        "correct": "طَالِبَ (thaaliba - munada mudhaf berharakat fathah tanpa tanwin).",
        "distractors": [
            "طَالِبُ (thaalibu - berharakat dhommah yang hanya berlaku pada munada mufrad 'alam atau nakirah maqshudah).",
            "طَالِبٍ (thaalibin - majrur dengan kasrah yang keliru diterapkan pada posisi munada).",
            "طَالِبًا (thaaliban - bertanwin yang tidak sah disandingkan sebagai kata pertama susunan idhafah).",
            "طَالِبُونَ (thaalibuuna - jamak marfu' berakhiran wawu dan nun)."
        ],
        "formula": {
            "title": "I'RAB MUNADA MUDHAF",
            "latex": "\\text{حَرْفُ النِّدَاءِ (يَا)} + \\mathbf{\\text{Munada Mudhaf (طَالِبَ - Manshub bil-Fathah)}} + \\text{Mudhaf Ilaih (العِلْمِ)}",
            "legend": "• Munada yang di-idhafah-kan selalu berstatus I'rab manshub dan tidak boleh bertanwin"
        },
        "hints": {
            "concept": "Munada mudhaf hukumnya adalah manshub bil-fathah tanpa tanwin karena berposisi sebagai mudhaf.",
            "execution": "Pilih: 'طَالِبَ' (thaaliba)."
        }
    },
    {
        "id": "arb-lat-m-14",
        "materi": "TATA BAHASA NAHWU: AL-BADAL (البَدَلُ)",
        "topic": "Badal Muthabaq / Badal Kul min Kul setelah Gelar Jabatan",
        "stem": "Perhatikan kalimat berikut:\n'تَوَلَّى الخَلِيفَةُ ... الخِلَافَةَ بَعْدَ وَفَاةِ أَبِي بَكْرٍ الصِّدِّيقِ.'\n(Khalifah ... telah memangku jabatan kekhalifahan setelah wafatnya Abu Bakar ash-Shiddiq).\nKata yang TEPAT untuk menduduki posisi Badal Muthabaq marfu' bil-dhommah (mengikuti mubdal minhu 'الخَلِيفَةُ' yang marfu' sebagai fa'il) adalah...",
        "correct": "عُمَرُ (Umaru - badal muthabaq marfu' dengan dhommah tanpa tanwin karena isim ghairu munsharif).",
        "distractors": [
            "عُمَرَ (Umara - manshub bil-fathah yang menyalahi i'rab mubdal minhu yang berkedudukan marfu').",
            "عُمَرٍ (Umarin - berharakat kasratain yang melanggar hukum isim ghairu munsharif).",
            "عُمَرٌ (Umarun - bertanwin dhommatain yang tidak dibenarkan pada nama berwazan fu'alu).",
            "أَبَا حَفْصٍ (Abaa Hafshin - bentuk manshub kun-yah yang tidak selaras dengan subjek marfu')."
        ],
        "formula": {
            "title": "I'RAB BADAL MUTHABAQ (KUL MIN KUL)",
            "latex": "\\text{Fa'il Marfu' (الخَلِيفَةُ)} \\implies \\mathbf{\\text{Badal Marfu' (عُمَرُ - Isim Ghairu Munsharif Tanpa Tanwin)}}",
            "legend": "• Badal mengikuti i'rab mubdal minhu dalam keadaan rafa', nashab, maupun jar"
        },
        "hints": {
            "concept": "Badal mengikuti mubdal minhu. Karena 'الخَلِيفَةُ' adalah fa'il marfu' (dhommah), maka 'عُمَرُ' juga marfu' (dhommah tanpa tanwin karena ghairu munsharif).",
            "execution": "Pilih: 'عُمَرُ' (Umaru)."
        }
    },
    {
        "id": "arb-lat-m-15",
        "materi": "TATA BAHASA NAHWU: AT-TAUKID (التَّوْكِيدُ)",
        "topic": "Taukid Ma'nawi Menggunakan Lafadz 'نَفْسُهُ' dan 'كُلُّهُمْ'",
        "stem": "Perhatikan kalimat penegasan berikut:\n'قَابَلْتُ الرَّئِيسَ ... فِي قَصْرِ الرِّئَاسَةِ أَمْسِ.'\n(Saya telah menemui presiden ... di istana kepresidenan kemarin).\nBentuk kata taukid ma'nawi yang TEPAT untuk menegaskan objek 'الرَّئِيسَ' (manshub bil-fathah) adalah...",
        "correct": "نَفْسَهُ (nafsahu - taukid ma'nawi manshub bil-fathah bersambung dhamir hu merujuk pada ar-ra'iisa).",
        "distractors": [
            "نَفْسُهُ (nafsuhu - marfu' dengan dhommah yang keliru karena mu'akkad-nya berstatus maf'ul bih manshub).",
            "نَفْسِهِ (nafsihi - majrur dengan kasrah yang menyalahi i'rab objek penderita).",
            "كُلُّهُمْ (kulluhum - taukid jamak yang tidak cocok untuk subjek tunggal ar-ra'iisa).",
            "أَنْفُسُهُمْ (anfusuhum - jamak taksir marfu' yang bertentangan dengan kaidah mufrad manshub)."
        ],
        "formula": {
            "title": "I'RAB TAUKID MA'NAWI (نَفْس / عَيْن)",
            "latex": "\\text{Mu'akkad Manshub (الرَّئِيسَ)} \\implies \\mathbf{\\text{Taukid Manshub (نَفْسَهُ)}} + \\text{Dhamir Mutabaqah (ـهُ)}",
            "legend": "• Taukid ma'nawi wajib mengikuti i'rab kata yang ditegaskannya dan mengikat dhamir perujuk"
        },
        "hints": {
            "concept": "Objek yang ditegaskan adalah 'الرَّئِيسَ' (maf'ul bih manshub fathah). Taukid ma'nawi-nya wajib manshub fathah: 'نَفْسَهُ'.",
            "execution": "Pilih: 'نَفْسَهُ' (nafsahu)."
        }
    },
    {
        "id": "arb-lat-m-16",
        "materi": "TATA BAHASA NAHWU: ADAD MA'DUD (11 - 19)",
        "topic": "Kaidah Bilangan Belasan Mabni Fathatai Juz'aini",
        "stem": "Dalam kaidah bilangan belasan (13 sampai 19), bagian pertama berlawanan jenis dengan ma'dud, bagian kedua menyamai jenis ma'dud, keduanya mabni di atas fathah (*mabni 'ala fathatai al-juz'aini*), dan ma'dud-nya berupa isim mufrad manshub. Jika kita ingin menyatakan 'lima belas siswa' (di mana siswa mufrad-nya adalah 'طَالِبًا' - mudzakkar), maka susunan yang BENAR adalah...",
        "correct": "خَمْسَةَ عَشَرَ طَالِبًا (khamsata 'asyara thaaliban - juz 1 mu'annats, juz 2 mudzakkar, keduanya berfathah, ma'dud mufrad manshub).",
        "distractors": [
            "خَمْسَ عَشْرَةَ طَالِبًا (khamsa 'asyrata thaaliban - susunan gender terbalik yang menyalahi kaidah).",
            "خَمْسَةُ عَشَرَ طَالِبٍ (khamsatu 'asyara thaalibin - juz 1 berharakat dhommah dan ma'dud majrur).",
            "خَمْسَ عَشَرَ طُلَّابٍ (khamsa 'asyara thullaabin - ma'dud berbentuk jamak yang tidak sah untuk adad belasan).",
            "خَامِسَ عَشَرَ طَالِبًا (khaamisa 'asyara thaaliban - susunan bilangan bertingkat ke-15)."
        ],
        "formula": {
            "title": "KAIDAH ADAD BELASAN (13 - 19)",
            "latex": "\\text{Ma'dud Mudzakkar (طَالِبًا)} \\implies \\mathbf{\\text{Juz 1: خَمْسَةَ (Mu'annats)}} + \\mathbf{\\text{Juz 2: عَشَرَ (Mudzakkar)}} + \\mathbf{\\text{Tamyiz Mufrad Manshub}}",
            "legend": "• Kedua juz bilangan 11-19 selalu mabni fathah (kecuali juz pertama pada bilangan 12)"
        },
        "hints": {
            "concept": "Adad 13-19: Juz 1 lawan jenis ma'dud (khamsata), Juz 2 sejenis ma'dud ('asyara), keduanya fathah, ma'dud mufrad manshub (thaaliban).",
            "execution": "Pilih: 'خَمْسَةَ عَشَرَ طَالِبًا'."
        }
    },
    {
        "id": "arb-lat-m-17",
        "materi": "FAHM AL-MAQRU': TOKOH SAINS ISLAM",
        "topic": "Analisis Wacana Kontribusi Kedokteran Ibnu Sina (Avicenna)",
        "stem": "Bacalah teks biografi ringkas berikut:\n'يُعَدُّ ابْنُ سِينَا (أَفِيسِينَا) مِنْ أَعْظَمِ عُلَمَاءِ الطِّبِّ فِي التَّارِيخِ الإِسْلَامِيِّ وَالعَالَمِيِّ. أَلَّفَ كِتَابَهُ الشَّهِيرَ 'القَانُون فِي الطِّبِّ' الَّذِي ظَلَّ المَرْجِعَ الأَسَاسِيَّ لِتَدْرِيسِ الطِّبِّ فِي جَامِعَاتِ أُورُوبَّا لِعِدَّةِ قُرُونٍ، وَقَدْ وَصَفَ فِيهِ العَدِيدَ مِنَ الأَمْرَاضِ المُعْدِيَةِ وَطُرُقَ انْتِقَالِهَا.'\nBerdasarkan teks di atas, bukti keunggulan monumental karya Ibnu Sina 'Al-Qanun fit-Thibb' adalah...",
        "correct": "Menjadi buku rujukan utama pembelajaran kedokteran di berbagai universitas Eropa selama berabad-abad karena deskripsinya yang akurat mengenai penyakit menular.",
        "distractors": [
            "Menjadi pedoman pembuatan persenjataan meriam mesiu pada masa ekspedisi laut kesultanan Turki Utsmani.",
            "Berisi peta navigasi pelayaran samudra yang pertama kali memetakan benua Antartika di kutub selatan.",
            "Merupakan naskah undang-undang perpajakan tanah pertama yang diterapkan di kawasan gurun Sahara barat.",
            "Berisi kumpulan syair puisi cinta romantik yang dinyanyikan para penunggang kuda di padang rumput."
        ],
        "formula": {
            "title": "ANALISIS EKSPLANASI FAHM AL-MAQRU'",
            "latex": "\\text{كتاب القانون في الطب} \\implies \\begin{cases} \\mathbf{\\text{Marja' Asasi di Universitas Eropa Berabad-abad}} \\\\ \\mathbf{\\text{Deskripsi Penyakit Menular \\& Cara Penularannya}} \\end{cases}",
            "legend": "• Menunjukkan transfer keilmuan dan supremasi saintifik peradaban Islam ke dunia barat"
        },
        "hints": {
            "concept": "Teks menyatakan: 'ظَلَّ المَرْجِعَ الأَسَاسِيَّ لِتَدْرِيسِ الطِّبِّ فِي جَامِعَاتِ أُورُوبَّا لِعِدَّةِ قُرُونٍ' (menjadi rujukan dasar kedokteran di Eropa berabad-abad).",
            "execution": "Pilih opsi: Menjadi buku rujukan utama kedokteran di universitas Eropa selama berabad-abad."
        }
    },
    {
        "id": "arb-lat-m-18",
        "materi": "FAHM AL-MAQRU': SENI & KEBUDAYAAN",
        "topic": "Karakteristik Jenis Khat Kaligrafi Arab (النَّسْخُ vs الثُّلُثُ vs الرُّقْعَةُ)",
        "stem": "Dalam seni kaligrafi Islam (*al-khathth al-'arabi*), gaya khat yang memiliki karakteristik huruf jelas, proporsional, mudah dibaca, serta paling banyak digunakan untuk menyalin mushaf Al-Qur'an dan mencetak buku teks kontemporer adalah khat...",
        "correct": "An-Naskhi (خَطُّ النَّسْخِ - khat naskah yang menjadi standar percetakan buku dan mushaf resmi).",
        "distractors": [
            "Ar-Riq'ah (خَطُّ الرُّقْعَةِ - khat cepat untuk catatan tangan sehari-hari dengan huruf rapat dan sederhana).",
            "Ats-Tsuluts (خَطُّ الثُّلُثِ - khat megah dekoratif bersudut lentur untuk kubah masjid dan sampul kitab).",
            "Al-Diwani (خَطُّ الدِّيوَانِيِّ - khat berlekuk indah yang dahulu digunakan untuk surat resmi istana khalifah).",
            "Al-Kufi (خَطُّ الكُوفِيِّ - khat tertua bermodel geometris kaku tanpa harakat pada batu nisan kuno)."
        ],
        "formula": {
            "title": "TIPOLOGI KHAT ARAB (أَنْوَاعُ الخُطُوطِ)",
            "latex": "\\begin{aligned} \\mathbf{\\text{1. خَطُّ النَّسْخِ:}} & \\mathbf{\\text{Mushaf Al-Qur'an, Buku Percetakan (Jelas, Mudah Dibaca)}} \\\\ \\text{2. خَطُّ الرُّقْعَةِ:} & \\text{Catatan Harian, Cepat, Sederhana} \\\\ \\text{3. خَطُّ الثُّلُثِ:} & \\text{Dekorasi Masjid, Monumen, Judul Kitab (Megah, Rumit)} \\end{aligned}",
            "legend": "• Khat Naskhi dinamai demikian karena fungsi historisnya dalam 'menasakh' (menyalin) buku/mushaf"
        },
        "hints": {
            "concept": "Khat yang digunakan untuk menyalin mushaf Al-Qur'an dan buku percetakan karena keterbacaannya yang tinggi adalah Khat Naskhi.",
            "execution": "Pilih: An-Naskhi (خَطُّ النَّسْخِ)."
        }
    },
    {
        "id": "arb-lat-m-19",
        "materi": "KITABAH: TARTIBUL JUMAL (MENYUSUN PARAGRAF)",
        "topic": "Menyusun Urutan Kalimat Acak Menjadi Paragraf Koheren",
        "stem": "Cermati empat kalimat acak berikut:\n(1) ثُمَّ تَوَجَّهَ إِلَى المَسْجِدِ لِأَدَاءِ صَلَاةِ الجُمُعَةِ جَمَاعَةً.\n(2) اسْتَيْقَظَ أَحْمَدُ صَبَاحَ يَوْمِ الجُمُعَةِ مُبَكِّرًا.\n(3) وَبَعْدَ ذَلِكَ تَنَاوَلَ طَعَامَ الفَطُورِ مَعَ أُسْرَتِهِ الكَرِيمَةِ.\n(4) فَتَوَضَّأَ وَصَلَّى رَكْعَتَيْنِ قَبْلَ شُرُوقِ الشَّمْسِ.\nUrutan yang LOGIS dan KOHEREN untuk membentuk paragraf cerita harian yang padu adalah...",
        "correct": "(2) - (4) - (3) - (1)",
        "distractors": [
            "(1) - (3) - (2) - (4)",
            "(2) - (3) - (1) - (4)",
            "(4) - (2) - (3) - (1)",
            "(3) - (1) - (4) - (2)"
        ],
        "formula": {
            "title": "URUTAN KRONOLOGIS KEGIATAN",
            "latex": "\\text{(2) Bangun tidur pagi} \\to \\text{(4) Wudhu \\& sholat fajar} \\to \\text{(3) Sarapan bersama keluarga} \\to \\text{(1) Berangkat Jum'atan}",
            "legend": "• Menunjukkan kohesi temporal (اسْتَيْقَظَ $\\to$ فَتَوَضَّأَ $\\to$ وَبَعْدَ ذَلِكَ $\\to$ ثُمَّ)"
        },
        "hints": {
            "concept": "Kronologi logis: Bangun pagi (2) -> Wudhu & sholat fajar (4) -> Sarapan bersama keluarga (3) -> Menuju masjid Jum'atan (1).",
            "execution": "Pilih urutan: (2) - (4) - (3) - (1)."
        }
    },
    {
        "id": "arb-lat-m-20",
        "materi": "TATA BAHASA NAHWU: KESESUAIAN FI'IL & FA'IL",
        "topic": "Kaidah Fi'il di Awal Kalimat Tetap Mufrad Walaupun Fa'il-nya Jamak",
        "stem": "Dalam kaidah penyusunan Jumlah Fi'liyyah, apabila kata kerja (fi'il) diletakkan mendahului pelaku (fa'il) yang berbentuk jamak, maka fi'il tersebut WAJIB tetap berstatus mufrad (tunggal) namun tetap menyamai jenis kelamin gender fa'il-nya. Kalimat yang MENERAPKAN kaidah ini secara BENAR adalah...",
        "correct": "حَضَرَ المُعَلِّمُونَ فِي قَاعَةِ الِاجْتِمَاعِ (hadhara al-mu'allimuuna - fi'il tetap mufrad mudzakkar hadhara meskipun fa'il jamak).",
        "distractors": [
            "حَضَرُوا المُعَلِّمُونَ فِي قَاعَةِ الِاجْتِمَاعِ (menyalahi kaidah karena fi'il berakhiran wawu jama'ah sebelum fa'il zhahir).",
            "حَضَرْنَ المُعَلِّمُونَ فِي قَاعَةِ الِاجْتِمَاعِ (menggunakan nun niswah jamak perempuan pada fa'il laki-laki).",
            "حَضَرَتِ المُعَلِّمُونَ فِي قَاعَةِ الِاجْتِمَاعِ (menggunakan ta' ta'nits perempuan untuk kelompok guru laki-laki).",
            "حَضَرَا المُعَلِّمُونَ فِي قَاعَةِ الِاجْتِمَاعِ (menggunakan alif itsnain mutsanna untuk subjek jamak)."
        ],
        "formula": {
            "title": "KAIDAH FI'IL DI AWAL JUMLAH FI'LIYYAH",
            "latex": "\\mathbf{\\text{Fi'il Mufrad (حَضَرَ)}} + \\mathbf{\\text{Fa'il Jama' Mudzakkar (المُعَلِّمُونَ)}} \\implies \\text{Haram menyertakan Wawu Jama'ah}",
            "legend": "• Bahasa Arab fusha melarang penggabungan fi'il jamak dengan fa'il isim zhahir (lughat akaluuni al-baraghit)"
        },
        "hints": {
            "concept": "Kaidah Jumlah Fi'liyyah: Fi'il di awal kalimat selalu MUFRAD meskipun fa'il-nya mutsanna atau jamak. Cukup sesuaikan jenisnya (mudzakkar/muannats).",
            "execution": "Pilih: 'حَضَرَ المُعَلِّمُونَ' (bukan hadharuu)."
        }
    },
    {
        "id": "arb-lat-m-21",
        "materi": "SHOROF & MORFOLOGI: ISIM ALAT",
        "topic": "Wazan Isim Alat (مِفْعَالٌ / مِفْعَلٌ / مِفْعَلَةٌ)",
        "stem": "Perkakas yang digunakan oleh seorang penjahit untuk memotong kain dinamakan gunting ('مِقَصٌّ' - miqashshun), dan alat yang digunakan untuk menimbang berat beras dinamakan timbangan ('مِيزَانٌ' - miizaanun). Kedua kata benda perkakas tersebut dalam ilmu shorof digolongkan sebagai...",
        "correct": "Isim Alat (kata benda turunan yang menunjukkan instrumen atau perkakas perantara untuk melakukan pekerjaan).",
        "distractors": [
            "Isim Makan (kata benda yang menunjukkan lokasi tempat pelaksanaan kegiatan).",
            "Isim Zaman (kata benda yang menyatakan waktu jam atau musim terjadinya aksi).",
            "Isim Marrah (kata benda yang menunjukkan bahwa perbuatan hanya terjadi satu kali saja).",
            "Isim Hai'ah (kata benda yang melukiskan gaya atau sikap tingkah laku perbuatan)."
        ],
        "formula": {
            "title": "DERIVASI ISIM ALAT (أَوْزَانُ اسْمِ الآلَةِ)",
            "latex": "\\text{Wazan Isim Alat} = \\begin{cases} \\mathbf{\\text{مِفْعَالٌ:}} & \\text{مِيزَانٌ (Timbangan), مِفْتَاحٌ (Kunci)} \\\\ \\mathbf{\\text{مِفْعَلٌ:}} & \\text{مِقَصٌّ (Gunting), مِبْرَدٌ (Kikir)} \\\\ \\mathbf{\\text{مِفْعَلَةٌ:}} & \\text{مِسْطَرَةٌ (Penggaris), مِكْنَسَةٌ (Sapu)} \\end{cases}",
            "legend": "• Menunjukkan instrumen fisik mekanik perantara tindakan kerja"
        },
        "hints": {
            "concept": "Miqashshun (gunting) dan miizaanun (timbangan) adalah nama-nama perkakas/alat bantu pekerjaan (Isim Alat).",
            "execution": "Pilih kategori Isim Alat."
        }
    },
    {
        "id": "arb-lat-m-22",
        "materi": "TATA BAHASA NAHWU: LA LI NAFYIL JINSI",
        "topic": "Hukum Isim Laa an-Nafiyah lil-Jinsi (Mabni 'alal-Fath)",
        "stem": "Cermati kalimat tauhid berikut ini:\n'لَا ... مَوْجُودٌ بِحَقٍّ فِي الكَوْنِ إِلَّا اللهُ.'\n(Tidak ada ... yang berhak disembah di alam semesta ini selain Allah).\nKata yang TEPAT untuk menduduki posisi Isim Laa an-Nafiyah lil-Jinsi (mufrad nakirah yang mabni di atas harakat fathah tanpa tanwin) adalah...",
        "correct": "إِلَهَ (ilaha - isim laa mabni di atas fathah karena berupa isim mufrad nakirah muttashil).",
        "distractors": [
            "إِلَهٌ (ilahun - marfu' bertanwin yang menyalahi hukum mabni fathah isim laa).",
            "إِلَهٍ (ilahin - bertanwin kasratain yang keliru untuk posisi isim laa).",
            "إِلَهًا (ilahan - manshub bertanwin yang hanya berlaku jika berupa syabih bil-mudhaf).",
            "الإِلَهُ (al-ilahu - ma'rifah ber-alif lam yang melanggar syarat kenakiran mutlak isim laa)."
        ],
        "formula": {
            "title": "KAIDAH LAA NAFYI AL-JINSI",
            "latex": "\\text{لَا النَّافِيَةُ لِلْجِنْسِ} + \\mathbf{\\text{Isim Laa (إِلَهَ - Mabni 'alal-Fath Tanpa Tanwin)}} + \\text{Khabar Laa}",
            "legend": "• Menafikan seluruh jenis entitas secara total, isim-nya mabni fathah bila mufrad nakirah langsung"
        },
        "hints": {
            "concept": "Isim Laa an-Nafiyah lil-Jinsi jika mufrad (bukan mudhaf atau syabih mudhaf) dihukumi mabni 'alal-fath tanpa tanwin: 'لَا إِلَهَ'.",
            "execution": "Pilih: 'إِلَهَ' (ilaha)."
        }
    },
    {
        "id": "arb-lat-m-23",
        "materi": "FAHM AL-MAQRU': HUBUNGAN BILATERAL",
        "topic": "Inferensi Makna Hubungan Perdagangan & Kebudayaan Arab-Indonesia",
        "stem": "Bacalah teks hubungan internasional berikut:\n'تَرْبِطُ إِنْدُونِيسِيَا بِالدُّوَلِ العَرَبِيَّةِ عَلَاقَاتٌ تَارِيخِيَّةٌ وَثِيقَةٌ مُنْذُ قُرُونٍ طَوِيلَةٍ. وَفِي العَصْرِ الحَاضِرِ، تَشْهَدُ هَذِهِ العَلَاقَاتُ تَطَوُّرًا مَلْحُوظًا فِي المَجَالَاتِ الدِّبْلُومَاسِيَّةِ وَالتِّجَارِيَّةِ، حَيْثُ تُصَدِّرُ إِنْدُونِيسِيَا المُنْتَجَاتِ الزِّرَاعِيَّةَ مِثْلَ زَيْتِ النَّخِيلِ وَالبُنِّ، بَيْنَمَا تَسْتَوْرِدُ النِّفْطَ وَالمَشْتَقَّاتِ البِتْرُولِيَّةَ.'\nBerdasarkan wacana di atas, komoditas utama yang diekspor Indonesia ke negara-negara Arab adalah...",
        "correct": "Produk-produk pertanian perkebunan seperti minyak kelapa sawit (minyak nabati) dan biji kopi.",
        "distractors": [
            "Minyak mentah bumi dan gas alam cair hasil pengeboran laut lepas pantai.",
            "Mesin pesawat terbang tempur dan sistem radar navigasi satelit militer.",
            "Buku-buku naskah kaligrafi kuno yang ditulis dengan tinta emas murni.",
            "Mobil mewah lapis baja dan kendaraan berat traktor pembajak sawah."
        ],
        "formula": {
            "title": "INFERENSI EKSPOR IMPOR RI - ARAB",
            "latex": "\\begin{cases} \\mathbf{\\text{Ekspor RI ke Arab (تُصَدِّرُ):}} & \\mathbf{\\text{زَيْت النَّخِيل (Sawit) + البُنّ (Kopi)}} \\\\ \\text{Impor RI dari Arab (تَسْتَوْرِدُ):} & \\text{النِّفْط (Minyak Bumi) + مشتقات بترولية} \\end{cases}",
            "legend": "• Membedakan kata 'tushaddiru' (mengekspor) dengan 'tastawridu' (mengimpor)"
        },
        "hints": {
            "concept": "Teks menyatakan: 'تُصَدِّرُ إِنْدُونِيسِيَا المُنْتَجَاتِ الزِّرَاعِيَّةَ مِثْلَ زَيْتِ النَّخِيلِ وَالبُنِّ' (Indonesia mengekspor produk pertanian seperti minyak sawit dan kopi).",
            "execution": "Pilih: Minyak kelapa sawit dan biji kopi."
        }
    },
    {
        "id": "arb-lat-m-24",
        "materi": "SHOROF & MORFOLOGI: FI'IL MU'TAL NAQISH",
        "topic": "Pembuangan Huruf 'Illat pada Fi'il Naqish saat Majzum",
        "stem": "Fi'il mu'tal naqish 'دَعَا - يَدْعُو' (berdoa / mengajak) memiliki huruf 'illat wawu di akhir katanya. Apabila kata kerja ini didahului oleh huruf jazm 'لَمْ' (lam yaf'al), maka tanda jazm-nya adalah pembuangan huruf 'illat (*hadzfu harfil 'illah*). Bentuk fi'il mudhari' majzum yang BENAR adalah...",
        "correct": "لَمْ يَدْعُ (lam yad'u - huruf wawu dibuang dan huruf 'ain tetap berharakat dhommah pendek).",
        "distractors": [
            "لَمْ يَدْعُو (lam yad'uu - kesalahan mempertahankan huruf 'illat wawu panjang setelah huruf jazm).",
            "لَمْ يَدْعُكْ (lam yad'uk - penambahan huruf kaf yang tidak sesuai dengan bentuk kata kerja asli).",
            "لَمْ يَدْعَى (lam yad'aa - penggantian huruf 'illat menjadi alif layyinah yang keliru).",
            "لَمْ يَدْعُونَ (lam yad'uuna - bentuk jamak yang menyalahi subjek tunggal gha'ib)."
        ],
        "formula": {
            "title": "I'RAB JAZM FI'IL NAQISH (حَذْفُ حَرْفِ العِلَّةِ)",
            "latex": "\\text{يَدْعُو (Fi'il Mu'tal Akhir Wawu)} + \\text{لَمْ (Amil Jazm)} \\implies \\mathbf{\\text{لَمْ يَدْعُ (Lam Yad'u)}}",
            "legend": "• Tanda jazm fi'il mu'tal akhir adalah dibuangnya huruf alif, wawu, atau ya' di ujung kata"
        },
        "hints": {
            "concept": "Fi'il mu'tal naqish yang berakhiran huruf 'illat (seperti yad'uu) jika majzum tanda jazm-nya adalah membuang huruf 'illat: 'لَمْ يَدْعُ'.",
            "execution": "Pilih: 'لَمْ يَدْعُ' (lam yad'u)."
        }
    },
    {
        "id": "arb-lat-m-25",
        "materi": "TATA BAHASA NAHWU: USLUBUSY SYARTH",
        "topic": "Kaidah Dua Fi'il Majzum dalam Kalimat Bersyarat (In Syarthiyyah)",
        "stem": "Cermati peribahasa bersyarat (*uslubusy syarth*) yang menjazmkan dua fi'il mudhari' berikut ini:\n'إِنْ ... فِي دِرَاسَتِكَ تَنْجَحْ فِي حَيَاتِكَ المُسْتَقْبَلِيَّةِ.'\n(Jika kamu bersungguh-sungguh dalam belajarmu, niscaya kamu akan sukses dalam kehidupan masa depanmu).\nFi'il syarth yang TEPAT dan berstatus majzum bis-sukun setelah 'إِنْ' syarthiyyah adalah...",
        "correct": "تَجْتَهِدْ (tajtahid - fi'il syarth majzum dengan tanda sukun pada huruf dal).",
        "distractors": [
            "تَجْتَهِدُ (tajtahidu - marfu' dengan dhommah yang mengabaikan amil jazm syarthiyyah).",
            "تَجْتَهِدَ (tajtahida - manshub dengan fathah yang keliru diterapkan pada kalimat syarat).",
            "تَجْتَهِدُونَ (tajtahiduuna - jamak marfu' yang tidak sesuai dengan khitab tunggal anta).",
            "اجْتَهَدْتُمْ (ijtahadtum - bentuk jamak madhi yang tidak selaras dengan jawab syarth tanjah)."
        ],
        "formula": {
            "title": "USLUBUSY SYARTH (إِنْ جَازِمَةٌ)",
            "latex": "\\text{إِنْ (Adatusy Syarth)} + \\mathbf{\\text{Fi'lusy Syarth Majzum (تَجْتَهِدْ)}} + \\text{Jawaabusy Syarth Majzum (تَنْجَحْ)}",
            "legend": "• In syarthiyyah menjazmkan dua fi'il mudhari' sekaligus (perbuatan syarat dan jawabannya)"
        },
        "hints": {
            "concept": "Partikel 'إِنْ' syarthiyyah menjazmkan dua fi'il: fi'il syarat dan jawab syarat. Fi'il syarat harus majzum bis-sukun: 'تَجْتَهِدْ'.",
            "execution": "Pilih: 'تَجْتَهِدْ' (tajtahid)."
        }
    }
]
