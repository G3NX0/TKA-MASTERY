# -*- coding: utf-8 -*-
"""
bahasa_arab_data_easy.py
-------------------------
25 Authentic Easy Practice Questions for TKA 2026 Bahasa Arab (SMA/MA Bahasa & Budaya / Agama).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: arb-lat-e-01 .. arb-lat-e-25
"""

BAHASA_ARAB_EASY_ITEMS = [
    {
        "id": "arb-lat-e-01",
        "materi": "TATA BAHASA NAHWU: JUMLAH ISMIYYAH",
        "topic": "Kesesuaian Mubtada' dan Khabar Mufrad (Gender & Number)",
        "stem": "Perhatikan kalimat rumpang berikut ini:\n'الطَّالِبُ الجَدِيدُ فِي المَدْرَسَةِ ... فِي دِرَاسَتِهِ.'\n(Siswa baru di sekolah itu ... dalam pembelajarannya).\nKata yang TEPAT dan memenuhi kaidah gramatikal nahwu (kesesuaian jenis mudzakkar dan bilangan mufrad dengan tanda I'rab rofa') untuk melengkapi khabar pada kalimat tersebut adalah...",
        "correct": "مُجْتَهِدٌ (mujtahidun - khabar mufrad mudzakkar marfu' dengan harakat dhommatain).",
        "distractors": [
            "مُجْتَهِدَةٌ (mujtahidatun - bentuk mu'annats dengan ta' marbuthah yang tidak selaras dengan subjek).",
            "مُجْتَهِدِينَ (mujtahidiina - bentuk jama' mudzakkar salim manshub/majrur berakhiran ya' dan nun).",
            "مُجْتَهِدَانِ (mujtahidaani - bentuk mutsanna dua orang dengan tanda alif yang tidak sesuai dengan subjek tunggal).",
            "مُجْتَهِدَاتٌ (mujtahidaatun - bentuk jama' mu'annats salim yang dikhususkan bagi perempuan jamak)."
        ],
        "formula": {
            "title": "KAIDAH MUBTADA' DAN KHABAR",
            "latex": "\\text{Mubtada' (Mufrad Mudzakkar Marfu')} \\iff \\mathbf{\\text{Khabar (Mufrad Mudzakkar Marfu')}} \\implies [\\text{الطَّالِبُ} \\dots \\mathbf{\\text{مُجْتَهِدٌ}}]",
            "legend": "• Khabar wajib menyamai mubtada' dalam hal gender (mudzakkar/mu'annats) dan bilangan (mufrad/tatsniyah/jama')"
        },
        "hints": {
            "concept": "Mubtada' 'الطَّالِبُ' adalah isim mufrad mudzakkar marfu' (dhommah). Maka khabar-nya wajib berupa isim mufrad mudzakkar marfu' pula (dhommah/dhommatain).",
            "execution": "Pilih 'مُجْتَهِدٌ' (mujtahidun) yang berjenis mudzakkar tunggal dan berharakat marfu'."
        }
    },
    {
        "id": "arb-lat-e-02",
        "materi": "TATA BAHASA NAHWU: NAWASIKH",
        "topic": "Pengaruh Amil Nawasikh Inna wa Akhwatuha terhadap I'rab Isim",
        "stem": "Cermati kalimat berikut:\n'إِنَّ ... نَشِيطُونَ فِي أَدَاءِ وَاجِبَاتِهِمْ اليَوْمِيَّةِ.'\n(Sesungguhnya para ... itu giat dalam menunaikan kewajiban harian mereka).\nBentuk kata yang TEPAT secara kaidah nahwu untuk mengisi posisi Isim Inna (berupa Jama' Mudzakkar Salim manshub) adalah...",
        "correct": "المُعَلِّمِينَ (al-mu'allimiina - isim Inna manshub dengan tanda ya' karena berupa jama' mudzakkar salim).",
        "distractors": [
            "المُعَلِّمُونَ (al-mu'allimuuna - marfu' dengan tanda wawu yang keliru untuk posisi isim Inna).",
            "المُعَلِّمَانِ (al-mu'allimaani - mutsanna marfu' dengan tanda alif yang bertentangan dengan khabar jamak).",
            "المُعَلِّمُ (al-mu'allimu - isim mufrad marfu' dengan dhommah yang tidak sesuai konteks jamak).",
            "المُعَلِّمَاتُ (al-mu'allimaatu - jama' mu'annats salim marfu' yang tidak cocok dengan khabar mudzakkar)."
        ],
        "formula": {
            "title": "AMIL NAWASIKH: INNA WA AKHWATUHA",
            "latex": "\\text{إِنَّ} + \\mathbf{\\text{Isim Inna (Manshub bil-Yaa')}} + \\text{Khabar Inna (Marfu' bil-Waaw)} \\implies [\\text{إِنَّ } \\mathbf{\\text{المُعَلِّمِينَ}} \\text{ نَشِيطُونَ}]",
            "legend": "• Kaidah: 'Inna tanshibul isma wa tarfa'ul khabar' (Inna memanshubkan isim dan merafa'kan khabar)"
        },
        "hints": {
            "concept": "Inna menashabkan isim dan merafa'kan khabar. Tanda nashab jama' mudzakkar salim adalah huruf ya' (ين).",
            "execution": "Pilih kata berakhiran ya' nun: 'المُعَلِّمِينَ' (al-mu'allimiina)."
        }
    },
    {
        "id": "arb-lat-e-03",
        "materi": "TATA BAHASA NAHWU: NAWASIKH",
        "topic": "Pengaruh Kaana wa Akhwatuha terhadap I'rab Khabar",
        "stem": "Perhatikan struktur kalimat kana berikut ini:\n'كَانَ الجَوُّ فِي مَدِينَةِ بَانْدُونق أَمْسِ ...'\n(Cuaca di kota Bandung kemarin adalah ...).\nKata yang TEPAT dan sahih secara kaidah nahwu untuk menduduki posisi Khabar Kaana (manshub bil-fathah) adalah...",
        "correct": "بَارِدًا (baaridan - khabar kaana manshub dengan harakat fathatain).",
        "distractors": [
            "بَارِدٌ (baaridun - marfu' dengan harakat dhommatain yang keliru untuk khabar kaana).",
            "بَارِدٍ (baaridin - majrur dengan harakat kasratain yang hanya berlaku jika ada huruf jar).",
            "بَارِدَةٌ (baaridatun - mu'annats marfu' yang tidak selaras dengan isim kaana mudzakkar).",
            "بَارِدَانِ (baaridaani - mutsanna marfu' dengan alif yang tidak sesuai konteks subjek tunggal)."
        ],
        "formula": {
            "title": "AMIL NAWASIKH: KAANA WA AKHWATUHA",
            "latex": "\\text{كَانَ} + \\text{Isim Kaana (Marfu' bil-Dhommah)} + \\mathbf{\\text{Khabar Kaana (Manshub bil-Fathah)}} \\implies [\\text{كَانَ الجَوُّ } \\mathbf{\\text{بَارِدًا}}]",
            "legend": "• Kaidah: 'Kaana tarfa'ul isma wa tanshibul khabar' (Kaana merafa'kan isim dan memanshubkan khabar)"
        },
        "hints": {
            "concept": "Kaana merafa'kan isim (الجَوُّ) dan memanshubkan khabar. Tanda nashab isim mufrad adalah fathah/fathatain.",
            "execution": "Pilih kata berharakat fathatain: 'بَارِدًا' (baaridan)."
        }
    },
    {
        "id": "arb-lat-e-04",
        "materi": "TATA BAHASA NAHWU: HURUF JAR & IDHAFAH",
        "topic": "Tanda I'rab Majrur pada Isim Mutsanna setelah Huruf Jar",
        "stem": "Cermati kalimat berikut:\n'سَافَرَ الرَّئِيسُ إِلَى ... لِحُضُورِ المُؤْتَمَرِ الدَّوْلِيِّ.'\n(Presiden telah bepergian ke ... untuk menghadiri konferensi internasional).\nIsim mutsanna (dua negara) yang TEPAT secara gramatikal majrur bil-ya' setelah huruf jar 'إِلَى' adalah...",
        "correct": "الدَّوْلَتَيْنِ (ad-dawlataini - isim mutsanna majrur dengan tanda huruf ya' setelah huruf jar).",
        "distractors": [
            "الدَّوْلَتَانِ (ad-dawlataani - bentuk mutsanna marfu' dengan alif yang keliru setelah huruf jar).",
            "الدَّوْلَةُ (ad-dawlatu - isim mufrad marfu' dengan dhommah yang tidak menunjukkan makna dua negara).",
            "الدُّوَلُ (ad-duwalu - jama' taksir marfu' dengan dhommah yang tidak sesuai tanda jar).",
            "الدَّوْلَاتِ (ad-dawlaati - bentuk jamak yang keliru secara konteks gramatikal mutsanna)."
        ],
        "formula": {
            "title": "I'RAB ISIM MUTSANNA SETELAH HURUF JAR",
            "latex": "\\text{إِلَى (Huruf Jar)} + \\mathbf{\\text{Isim Mutsanna Majrur (Tanda Yaa')}} \\implies [\\text{إِلَى } \\mathbf{\\text{الدَّوْلَتَيْنِ}}]",
            "legend": "• Tanda rafa' mutsanna adalah Alif (انِ), sedangkan tanda nashab dan jar-nya adalah Yaa' (يْنِ)"
        },
        "hints": {
            "concept": "Setelah huruf jar (إِلَى), isim menjadi majrur. Isim mutsanna (dua) tanda majrur-nya memakai ya' sukun (يْنِ).",
            "execution": "Pilih bentuk mutsanna berakhiran ya' nun: 'الدَّوْلَتَيْنِ' (ad-dawlataini)."
        }
    },
    {
        "id": "arb-lat-e-05",
        "materi": "TATA BAHASA NAHWU: TAWABI' (NA'AT MAN'UT)",
        "topic": "Kesesuaian Sifat (Na'at) dengan Isim yang Disifati (Man'ut)",
        "stem": "Perhatikan frasa dalam kalimat berikut:\n'اشْتَرَى عَلِيٌّ كِتَابًا ... مِنَ المَكْتَبَةِ الوَطَنِيَّةِ.'\n(Ali telah membeli sebuah buku ... dari perpustakaan nasional).\nKata sifat (na'at) yang TEPAT untuk menyifati 'كِتَابًا' (nakirah, mudzakkar, mufrad, manshub) adalah...",
        "correct": "مُفِيدًا (mufiidan - na'at manshub bil-fathah, nakirah, dan mudzakkar mengikuti man'utnya).",
        "distractors": [
            "مُفِيدٌ (mufiidun - marfu' dengan dhommatain sehingga tidak selaras dengan man'ut yang manshub).",
            "مُفِيدَةً (mufiidatan - mu'annats yang bertentangan dengan kata benda ketaaban yang mudzakkar).",
            "المُفِيدُ (al-mufiidu - ma'rifah ber-alif lam yang tidak cocok dengan man'ut nakirah).",
            "مُفِيدِينَ (mufiidiina - jama' mudzakkar salim yang menyalahi kaidah mufrad bendanya)."
        ],
        "formula": {
            "title": "KONSISTENSI 4 ASPEK NA'AT MAN'UT",
            "latex": "\\text{Na'at} \\equiv \\text{Man'ut} \\text{ dalam: } \\begin{cases} \\text{1. I'rab (Rafa'/Nashab/Jar)} \\\\ \\text{2. Gender (Mudzakkar/Mu'annats)} \\\\ \\text{3. Bilangan (Mufrad/Mutsanna/Jama')} \\\\ \\text{4. Kejelasan (Ma'rifah/Nakirah)} \\end{cases}",
            "legend": "• Pada 'كِتَابًا مُفِيدًا': keduanya nakirah, mufrad, mudzakkar, dan manshub fathah"
        },
        "hints": {
            "concept": "Na'at wajib mengikuti man'ut dalam 4 perkara: i'rab, jenis, bilangan, dan ke-ma'rifah/nakirah-annya.",
            "execution": "Karena 'كِتَابًا' adalah nakirah, mudzakkar, mufrad, manshub, maka na'atnya harus 'مُفِيدًا'."
        }
    },
    {
        "id": "arb-lat-e-06",
        "materi": "SHOROF & MORFOLOGI: WAZAN TSULATSI MAZID",
        "topic": "Perubahan Makna Fi'il dengan Wazan Af'ala (أَفْعَلَ) - Li At-Ta'diyah",
        "stem": "Fi'il tsulatsi mujarrad 'خَرَجَ' (kharaja) bermakna 'dia telah keluar' (lazim / intransitif). Ketika diubah ke dalam wazan tsulatsi mazid bi harfin 'أَخْرَجَ' (akhraja), makna gramatikal kata tersebut berubah menjadi...",
        "correct": "Dia telah mengeluarkan (transitif / muta'addi, membutuhkan objek maf'ul bih).",
        "distractors": [
            "Dia saling keluar bersama-sama (musyarakah timbal balik antardua pihak).",
            "Dia memohon untuk dikeluarkan (thalab al-fi'li seperti wazan istaf'ala).",
            "Dia berpura-pura keluar dari ruangan (tazahur bi al-fi'li).",
            "Dia keluar berulang-ulang tanpa henti secara bertahap (mubalaghah wat-taktsir)."
        ],
        "formula": {
            "title": "FAEDAH WAZAN AF'ALA (أَفْعَلَ)",
            "latex": "\\text{Fi'il Lazim (خَرَجَ: Keluar)} \\xrightarrow{\\mathbf{\\text{Wazan أَفْعَلَ}}} \\mathbf{\\text{Fi'il Muta'addi (أَخْرَجَ: Mengeluarkan)}} \\implies \\text{Faedah: Li at-Ta'diyah}",
            "legend": "• Penambahan hamzah qatha' di awal (af'ala) mengubah predikat intransitif menjadi transitif"
        },
        "hints": {
            "concept": "Salah satu faedah utama wazan أَفْعَلَ (af'ala) adalah li at-ta'diyah (menjadikan fi'il lazim menjadi muta'addi/transitif).",
            "execution": "Kharaja (keluar) -> Akhraja (mengeluarkan)."
        }
    },
    {
        "id": "arb-lat-e-07",
        "materi": "TATA BAHASA NAHWU: FI'IL MUDHARI' & ADWATUN NASHB",
        "topic": "I'rab Fi'il Mudhari' setelah Huruf Nashab 'أنْ' dan 'لَنْ'",
        "stem": "Perhatikan penggalan kalimat berikut:\n'يَجِبُ عَلَى الطَّالِبِ أَنْ ... دُرُوسَهُ بِانْتِظَامٍ.'\n(Wajib bagi siswa untuk ... pelajaran-pelajarannya dengan teratur).\nBentuk fi'il mudhari' mufrad mudzakkar yang TEPAT dan berharakat manshub bil-fathah setelah amil nashab 'أَنْ' adalah...",
        "correct": "يُرَاجِعَ (yuraaji'a - fi'il mudhari' shahih akhir manshub dengan harakat fathah).",
        "distractors": [
            "يُرَاجِعُ (yuraaji'u - marfu' dengan dhommah yang keliru karena telah didahului huruf nashab).",
            "يُرَاجِعْ (yuraaji' - majzum dengan sukun yang hanya berlaku jika didahului huruf jazm).",
            "يُرَاجِعُونَ (yuraaji'uuna - af'alul khamsah marfu' dengan tsubutun nun yang tidak sesuai subjek mufrad).",
            "رَاجَعَ (raaja'a - fi'il madhi yang tidak tepat mengikuti huruf mashdariyah nashab 'an')."
        ],
        "formula": {
            "title": "I'RAB FI'IL MUDHARI' MANSHUB",
            "latex": "\\text{أَنْ (Huruf Nashab)} + \\mathbf{\\text{Fi'il Mudhari' Shahih Akhir (Manshub bil-Fathah)}} \\implies [\\text{أَنْ } \\mathbf{\\text{يُرَاجِعَ}}]",
            "legend": "• Amil nashab (أن، لن، إذن، كي) mengubah harakat dhommah fi'il mudhari' menjadi fathah"
        },
        "hints": {
            "concept": "Huruf 'أَنْ' adalah harf nashab wa mashdariyyah. Fi'il mudhari' shahih al-akhir yang memasukinya menjadi manshub bil-fathah.",
            "execution": "Pilih fi'il mudhari' berharakat fathah: 'يُرَاجِعَ' (yuraaji'a)."
        }
    },
    {
        "id": "arb-lat-e-08",
        "materi": "TATA BAHASA NAHWU: ADWATUL JAZM",
        "topic": "Pengaruh Huruf Nafyi Jazm 'لَمْ' terhadap Fi'il Mudhari' Mufrad",
        "stem": "Cermati kalimat berikut:\n'أَحْمَدُ مَرِيضٌ، لِذَلِكَ لَمْ ... إِلَى المَدْرَسَةِ اليَوْمَ.'\n(Ahmad sedang sakit, oleh karena itu dia belum/tidak ... ke sekolah hari ini).\nBentuk fi'il mudhari' yang TEPAT dan majzum bis-sukun setelah amil jazm 'لَمْ' adalah...",
        "correct": "يَذْهَبْ (yadh-hab - fi'il mudhari' majzum dengan tanda sukun pada huruf ba').",
        "distractors": [
            "يَذْهَبُ (yadh-habu - marfu' dengan dhommah yang mengabaikan amil jazm di depannya).",
            "يَذْهَبَ (yadh-haba - manshub dengan fathah yang keliru diterapkan pada amil jazm).",
            "يَذْهَبُونَ (yadh-habuuna - marfu' dengan nun yang tidak sesuai untuk fa'il tunggal Ahmad).",
            "ذَهَبَ (dhahaba - bentuk fi'il madhi yang tidak digunakan langsung setelah partikel lam)."
        ],
        "formula": {
            "title": "I'RAB FI'IL MUDHARI' MAJZUM",
            "latex": "\\text{لَمْ (Huruf Jazm \\& Nafyi)} + \\mathbf{\\text{Fi'il Mudhari' Shahih (Majzum bis-Sukuun)}} \\implies [\\text{لَمْ } \\mathbf{\\text{يَذْهَبْ}}]",
            "legend": "• Huruf lam menjazmkan fi'il mudhari' dan mengubah maknanya ke masa lampau yang dinafikan"
        },
        "hints": {
            "concept": "Huruf 'لَمْ' adalah adawatul jazm. Fi'il mudhari' shahih akhir yang memasukinya berharakat sukun (majzum).",
            "execution": "Pilih kata bersukun: 'يَذْهَبْ' (yadh-hab)."
        }
    },
    {
        "id": "arb-lat-e-09",
        "materi": "SHOROF & MORFOLOGI: ISIM FA'IL & ISIM MAF'UL",
        "topic": "Pembentukan Isim Fa'il dari Fi'il Tsulatsi Mujarrad (فَاعِلٌ)",
        "stem": "Dalam kaidah morfologi shorof bahasa Arab, isim fa'il (kata benda penunjuk pelaku tindakan) dari kata kerja dasar tsulatsi mujarrad 'كَتَبَ' (kataba - menulis) dibentuk mengikuti wazan 'فَاعِلٌ', yaitu...",
        "correct": "كَاتِبٌ (kaatibun - penulis / sekretaris).",
        "distractors": [
            "مَكْتُوبٌ (maktuubun - isim maf'ul bermakna sesuatu yang tertulis/surat).",
            "مَكْتَبٌ (maktabun - isim makan/alat bermakna meja tulis atau kantor).",
            "كِتَابٌ (kitaabun - bentuk isim masdar/isim jenis bermakna buku).",
            "مِكْتَابٌ (miktaabun - wazan shighah mubalaghah/alat yang tidak baku)."
        ],
        "formula": {
            "title": "DERIVASI ISIM FA'IL TSULATSI MUJARRAD",
            "latex": "\\text{Fi'il (فَعَلَ: كَتَبَ)} \\xrightarrow{\\mathbf{\\text{Wazan فَاعِلٌ}}} \\mathbf{\\text{Isim Fa'il: كَاتِبٌ}} \\implies \\text{Makna: Pelaku Perbuatan (Penulis)}",
            "legend": "• Wazan fa'ilun dibentuk dengan memanjangkan fathah 'ain dengan alif pada huruf pertama"
        },
        "hints": {
            "concept": "Isim fa'il dari fi'il tsulatsi mujarrad berwazan فَاعِلٌ (faa'ilun). Kataba -> Kaatibun.",
            "execution": "Pilih: 'كَاتِبٌ' (kaatibun)."
        }
    },
    {
        "id": "arb-lat-e-10",
        "materi": "TATA BAHASA NAHWU: DHAMIR & MUTABAQAH",
        "topic": "Penggunaan Dhamir Munfashil Mufrad Mu'annats (Gha'ibah)",
        "stem": "Perhatikan kalimat rumpang berikut:\n'فَاطِمَةُ طَبِيبَةٌ مَاهِرَةٌ، ... تَعْمَلُ فِي المُسْتَشْفَى الكَبِيرِ.'\n(Fathimah adalah dokter yang mahir, ... bekerja di rumah sakit besar).\nKata ganti orang ketiga tunggal perempuan (dhamir munfashil gha'ibah) yang TEPAT untuk merujuk pada Fathimah adalah...",
        "correct": "هِيَ (hiya - kata ganti tunggal orang ketiga perempuan).",
        "distractors": [
            "هُوَ (huwa - kata ganti tunggal untuk orang ketiga laki-laki mudzakkar).",
            "هُمْ (hum - kata ganti jamak untuk kelompok laki-laki).",
            "أَنْتِ (anti - kata ganti orang kedua perempuan yang diajak bicara langsung).",
            "هُنَّ (hunna - kata ganti jamak khusus kelompok perempuan)."
        ],
        "formula": {
            "title": "MUTABAQAH DHAMIR GHA'IBAH",
            "latex": "\\text{فَاطِمَةُ (Mufrad Mu'annats)} \\implies \\mathbf{\\text{Dhamir Munfashil: هِيَ (Hiya)}} \\iff \\text{Fi'il Mudhari': تَعْمَلُ}",
            "legend": "• Dhamir munfashil wajib selaras dengan gender dan kuantitas isim marja'-nya"
        },
        "hints": {
            "concept": "Fathimah adalah mufrad mu'annats gha'ibah (orang ketiga tunggal perempuan). Kata ganti yang tepat adalah 'هِيَ' (hiya).",
            "execution": "Pilih 'هِيَ' (hiya)."
        }
    },
    {
        "id": "arb-lat-e-11",
        "materi": "TATA BAHASA NAHWU: ADAD MA'DUD",
        "topic": "Kaidah Bilangan 3-10 (Mukhalafah Gender & Jama' Majrur)",
        "stem": "Dalam kaidah adad dan ma'dud bahasa Arab untuk bilangan 3 sampai 10, jenis kelamin kata bilangan (adad) berlawanan jenis (*mukhalafah*) dengan benda yang dihitung (ma'dud), dan ma'dud-nya wajib berbentuk jama' majrur. Jika kita ingin menyatakan 'lima pulpen' (di mana pulpen mufrad-nya adalah 'قَلَمٌ' - mudzakkar), maka susunan yang BENAR adalah...",
        "correct": "خَمْسَةُ أَقْلَامٍ (khamsatu aqlaamin - adad berbentuk mu'annats ber-ta' marbuthah dan ma'dud berbentuk jama' majrur).",
        "distractors": [
            "خَمْسُ أَقْلَامٍ (khamsu aqlaamin - adad mudzakkar yang menyalahi kaidah lawan jenis dengan qalam).",
            "خَمْسَةُ قَلَمٍ (khamsatu qalamin - ma'dud berbentuk mufrad yang bertentangan dengan kaidah jamak).",
            "خَمْسُ قَلَمًا (khamsu qalaman - susunan salah menyerupai kaidah bilangan belasan).",
            "خَامِسُ أَقْلَامٍ (khaamisu aqlaamin - bentuk bilangan bertingkat yang tidak tepat untuk menghitung jumlah)."
        ],
        "formula": {
            "title": "KAIDAH ADAD MA'DUD (3 - 10)",
            "latex": "\\text{Ma'dud Mudzakkar (قَلَمٌ)} \\implies \\mathbf{\\text{Adad Mu'annats (خَمْسَةُ)}} + \\mathbf{\\text{Ma'dud Jama' Majrur (أَقْلَامٍ)}}",
            "legend": "• Kaidah: Adad 3-10 berlawanan jenis kelamin dengan mufrad ma'dud, ma'dud berbentuk jama' majrur idhafah"
        },
        "hints": {
            "concept": "Untuk bilangan 3-10: Jika ma'dud mudzakkar (qalam), adad harus mu'annats (khamsatu) dan ma'dud berbentuk jama' majrur (aqlaamin).",
            "execution": "Pilih: 'خَمْسَةُ أَقْلَامٍ' (khamsatu aqlaamin)."
        }
    },
    {
        "id": "arb-lat-e-12",
        "materi": "TATA BAHASA NAHWU: MAF'UL BIH",
        "topic": "I'rab Maf'ul Bih Mufrad (Manshub bil-Fathah)",
        "stem": "Perhatikan kalimat fi'liyyah berikut:\n'قَرَأَ التِّلْمِيذُ ... فِي صَفِّهِ هَذَا الصَّبَاحَ.'\n(Murid itu telah membaca ... di kelasnya pagi ini).\nKata yang TEPAT dan berkedudukan sebagai maf'ul bih (objek penderita manshub dengan harakat fathah) adalah...",
        "correct": "الدَّرْسَ (ad-darsa - maf'ul bih manshub dengan tanda fathah di akhir huruf sin).",
        "distractors": [
            "الدَّرْسُ (ad-darsu - marfu' dengan dhommah yang keliru untuk posisi objek maf'ul bih).",
            "الدَّرْسِ (ad-darsi - majrur dengan kasrah yang hanya terjadi jika ada huruf jar atau idhafah).",
            "الدَّرْسَانِ (ad-darsaani - mutsanna marfu' dengan alif yang tidak memenuhi kaidah nashab).",
            "الدُّرُوسُ (ad-duruusu - jama' taksir marfu' dengan dhommah)."
        ],
        "formula": {
            "title": "I'RAB MAF'UL BIH (OBJEK PENDERITA)",
            "latex": "\\text{Fi'il (قَرَأَ)} + \\text{Fa'il (التِّلْمِيذُ)} + \\mathbf{\\text{Maf'ul Bih (الدَّرْسَ - Manshub bil-Fathah)}}",
            "legend": "• Maf'ul bih selalu berkategori I'rab manshub (fathah untuk mufrad dan jama' taksir)"
        },
        "hints": {
            "concept": "Maf'ul bih adalah objek penderita yang berkedudukan manshub. Tanda nashab isim mufrad adalah harakat fathah.",
            "execution": "Pilih kata berharakat fathah: 'الدَّرْسَ' (ad-darsa)."
        }
    },
    {
        "id": "arb-lat-e-13",
        "materi": "SHOROF & MORFOLOGI: TASHRIF LUGHAWI FI'IL MADHI",
        "topic": "Konjugasi Fi'il Madhi dengan Dhamir Nahnu (نَحْنُ)",
        "stem": "Apabila fi'il madhi dasar 'كَتَبَ' (dia laki-laki telah menulis) dikonjugasikan (tashrif lughawi) dengan subjek dhamir 'نَحْنُ' (kami / kita), maka bentuk kata kerja yang BENAR adalah...",
        "correct": "كَتَبْنَا (katabnaa - diakhiri dhamir muttashil nun dan alif panjang tanda fa'il nahnu).",
        "distractors": [
            "كَتَبْتُ (katabtu - mutakallim wahdah tanda orang pertama tunggal 'aku/saya').",
            "كَتَبْتُمْ (katabtum - tanda jamak mukhatab laki-laki 'kalian beramai-ramai').",
            "كَتَبُوا (katabuu - tanda jamak gha'ib laki-laki mereka beramai-ramai).",
            "كَتَبْنَ (katabna - tanda jamak gha'ibah khusus perempuan)."
        ],
        "formula": {
            "title": "KONJUGASI FI'IL MADHI + NAHNU",
            "latex": "\\text{كَتَبَ} + \\text{نَحْنُ} \\implies \\mathbf{\\text{كَتَبْنَا (Katabnaa)}} \\iff \\text{Sukun pada Lam Fi'il + Dhomir نَا}",
            "legend": "• Huruf akhir fi'il disukunkan dan disambung dengan dhamir bariz muttashil 'naa'"
        },
        "hints": {
            "concept": "Tashrif fi'il madhi untuk 'نَحْنُ' (kami) ditandai dengan sufiks 'نَا' (naa) dan sukun pada huruf ketiga kata kerja dasar.",
            "execution": "Pilih: 'كَتَبْنَا' (katabnaa)."
        }
    },
    {
        "id": "arb-lat-e-14",
        "materi": "FAHM AL-MAQRU' & KOSA KATA",
        "topic": "Makna Kosakata Kontekstual seputar Kehidupan Madrasah / Sekolah",
        "stem": "Cermati kalimat berikut:\n'يَسْتَعِيرُ الطُّلَّابُ الكُتُبَ وَالمَرَاجِعَ العِلْمِيَّةَ مِنَ المَكْتَبَةِ أُسْبُوعِيًّا.'\nArti dari kata kerja 'يَسْتَعِيرُ' (yasta'iiru) dalam konteks kalimat tersebut adalah...",
        "correct": "Meminjam (mengambil buku untuk dibaca dan dikembalikan dalam jangka waktu tertentu).",
        "distractors": [
            "Menjual (menukarkan buku dengan sejumlah uang tunai di pasar buku).",
            "Membakar (memusnahkan buku-buku lama yang halamannya robek dan usang).",
            "Mencetak (memperbanyak naskah lembaran kerja menggunakan mesin printer).",
            "Menghafal (mengingat teks materi ujian tanpa melihat lembaran buku)."
        ],
        "formula": {
            "title": "MAKNA LEKSIKAL WAZAN ISTAF'ALA",
            "latex": "\\text{عَارَ (Pinjam)} \\xrightarrow{\\text{Wazan اسْتَفْعَلَ}} \\mathbf{\\text{اسْتَعَارَ - يَسْتَعِيرُ}} \\implies \\text{Memohon/Melakukan Peminjaman}",
            "legend": "• Thalab al-i'arah: aktivitas rutin peminjaman pustaka di lingkungan maktabah"
        },
        "hints": {
            "concept": "'يَسْتَعِيرُ' berasal dari kata 'استعار - يستعير' yang berarti meminjam (istitalah/thalab al-i'arah).",
            "execution": "Pilih arti 'Meminjam'."
        }
    },
    {
        "id": "arb-lat-e-15",
        "materi": "TATA BAHASA NAHWU: HURUF 'ATHAF",
        "topic": "Fungsi Huruf 'Athaf Fa' (فَـ) untuk Urutan Langsung (Tartib ma'at-Ta'qib)",
        "stem": "Dalam ilmu nahwu, partikel 'athaf 'فَـ' (fa) berfungsi untuk menghubungkan dua peristiwa secara berurutan tanpa jeda waktu lama (*at-tartib ma'at-ta'qib*). Manakah kalimat berikut yang TEPAT menggunakan huruf 'فَـ' sesuai fungsi tersebut?",
        "correct": "دَخَلَ الأُسْتَاذُ الفَصْلَ فَوَقَفَ الطُّلَّابُ (Ustadz masuk kelas, seketika itu pula para siswa langsung berdiri menyambutnya).",
        "distractors": [
            "سَافَرَ أَحْمَدُ إِلَى مَكَّةَ فَـبَعْدَ عَشْرِ سَنَوَاتٍ رَجَعَ إِلَى وَطَنِهِ (Penggunaan jeda 10 tahun yang seharusnya memakai tsumma).",
            "تَزَوَّجَ عَلِيٌّ فَـوُلِدَ لَهُ وَلَدٌ بَعْدَ خَمْسِ سِنِينَ (Kelahiran anak berselang 5 tahun yang tidak logis memakai fa').",
            "كَتَبَ التِّلْمِيذُ رِسَالَةً فَـلَمْ يَكْتُبْ شَيْئًا مُطْلَقًا (Pertentangan logika antara menulis dan tidak menulis).",
            "أَكَلْتُ التُّفَّاحَ فَـالسَّيَّارَةَ فِي الشَّارِعِ (Penggabungan dua kata yang tidak memiliki hubungan korelasi makna)."
        ],
        "formula": {
            "title": "MAKNA HURUF 'ATHAF FA'",
            "latex": "\\text{Peristiwa 1 (Masuk)} \\xrightarrow{\\mathbf{\\text{حرف الفاء (فَـ)}}} \\text{Peristiwa 2 (Berdiri)} \\implies \\mathbf{\\text{Tartib ma'a Ta'qib (Langsung Tanpa Jeda)}}",
            "legend": "• Berbeda dengan 'ثُمَّ' yang bermakna at-tarakhi (ada jeda waktu senggang di antaranya)"
        },
        "hints": {
            "concept": "Huruf 'fa' (فَـ) bermakna berurutan langsung seketika tanpa jeda waktu (tartib wa ta'qib).",
            "execution": "Pilih kalimat guru masuk kelas dan siswa langsung berdiri seketika."
        }
    },
    {
        "id": "arb-lat-e-16",
        "materi": "TATA BAHASA NAHWU: FI'IL AMAR",
        "topic": "Pembentukan Fi'il Amar untuk Mukhatab Tunggal Laki-Laki (أَنْتَ)",
        "stem": "Perhatikan kalimat perintah berikut:\n'يَا بَنِيَّ، ... إِلَى نَصِيحَةِ وَالِدِكَ بِعِنَايَةٍ!'\n(Wahai anakku, ...lah nasihat ayahmu dengan saksama!).\nBentuk fi'il amar yang TEPAT dari fi'il tsulatsi 'اسْتَمَعَ - يَسْتَمِعُ' untuk seorang anak laki-laki tunggal (أَنْتَ) adalah...",
        "correct": "اسْتَمِعْ (istami' - fi'il amar mabni di atas sukun).",
        "distractors": [
            "اسْتَمِعِي (istami'ii - fi'il amar untuk mukhatabah perempuan tunggal berakhiran ya' mukhathabah).",
            "اسْتَمِعُوا (istami'uu - fi'il amar untuk kelompok laki-laki jamak berakhiran wawu jama'ah).",
            "اسْتَمِعَا (istami'aa - fi'il amar untuk dua orang mutsanna berakhiran alif itsnain).",
            "اسْتَمَعَ (istama'a - bentuk fi'il madhi lampau yang bukan kalimat perintah)."
        ],
        "formula": {
            "title": "BINA' FI'IL AMAR MUFRAD MUDZAKKAR",
            "latex": "\\text{Fi'il Amar (أَنْتَ)} \\implies \\mathbf{\\text{Mabni 'alas-Sukuun: اسْتَمِعْ}} \\iff \\text{Ditujukan kepada satu orang laki-laki}",
            "legend": "• Tanda asli bina' fi'il amar shahih akhir adalah sukun"
        },
        "hints": {
            "concept": "Subjek perintah adalah 'يَا بَنِيَّ' (wahai anak laki-lakiku/anta). Fi'il amar untuk anta mabni di atas sukun: 'اسْتَمِعْ'.",
            "execution": "Pilih: 'اسْتَمِعْ' (istami')."
        }
    },
    {
        "id": "arb-lat-e-17",
        "materi": "SHOROF & MORFOLOGI: ISIM MAKAN",
        "topic": "Wazan Isim Makan dari Tsulatsi Mujarrad (مَفْعَلٌ / مَفْعِلٌ)",
        "stem": "Tempat dilaksanakannya ibadah sholat berjamaah dinamakan 'مَسْجِدٌ' (masjid). Berdasarkan kaidah morfologi shorof, kata 'مَسْجِدٌ' tergolong ke dalam kategori isim...",
        "correct": "Isim Makan (kata benda derivasi yang menunjukkan keterangan tempat terjadinya suatu perbuatan).",
        "distractors": [
            "Isim Zaman (kata benda yang khusus menunjukkan masa/waktu berlangsungnya pekerjaan).",
            "Isim Alat (kata benda yang menunjukkan perkakas konkret untuk melakukan perbuatan).",
            "Isim Tafdhil (kata benda yang menyatakan perbandingan sifat lebih atau paling unggul).",
            "Isim Fa'il (kata benda yang menyatakan subjek pelaku aktif dari suatu pekerjaan)."
        ],
        "formula": {
            "title": "KLASIFIKASI ISIM DERIVASI (ISIM MAKAN)",
            "latex": "\\text{سَجَدَ (Sujud)} \\xrightarrow{\\text{Wazan مَفْعِلٌ}} \\mathbf{\\text{مَسْجِدٌ (Masjid)}} \\implies \\text{Kategori: Isim Makan (Tempat Sujud)}",
            "legend": "• Isim makan dan isim zaman umumnya mengikuti pola wazan maf'alun atau maf'ilun"
        },
        "hints": {
            "concept": "'Masjid' berasal dari sajada (bersujud) mengikuti wazan maf'ilun untuk menunjukkan tempat sujud (isim makan).",
            "execution": "Pilih kategori Isim Makan (keterangan tempat terjadinya perbuatan)."
        }
    },
    {
        "id": "arb-lat-e-18",
        "materi": "TATA BAHASA NAHWU: ASMA'UL KHAMSAH",
        "topic": "Tanda I'rab Rofa' pada Asma'ul Khamsah (Huruf Wawu)",
        "stem": "Perhatikan kalimat mubtada'-khabar berikut:\n'... عَلِيٍّ رَجُلٌ كَرِيمٌ يُحِبُّ مُسَاعَدَةَ الفُقَرَاءِ.'\n(... Ali adalah seorang laki-laki dermawan yang suka membantu fakir miskin).\nBentuk kata Asma'ul Khamsah yang TEPAT untuk menduduki posisi Mubtada' Marfu' bil-Wawu adalah...",
        "correct": "أَبُو (abuu - marfu' dengan tanda huruf wawu sebagai bagian dari asma'ul khamsah).",
        "distractors": [
            "أَبَا (abaa - manshub dengan tanda huruf alif yang keliru untuk posisi mubtada').",
            "أَبِي (abii - majrur dengan tanda huruf ya' yang hanya berlaku setelah huruf jar).",
            "أَبٌ (abun - mufrad bertanwin tanpa idhafah yang tidak cocok disandingkan dengan Ali).",
            "آبَاءُ (aabaa'u - jama' taksir yang bermakna banyak ayah/leluhur)."
        ],
        "formula": {
            "title": "I'RAB ASMA'UL KHAMSAH (أَبٌ، أَخٌ، حَمٌ، فُو، ذُو)",
            "latex": "\\text{Asma'ul Khamsah (Mubtada')} \\implies \\begin{cases} \\mathbf{\\text{Marfu' bil-Waaw: أَبُو}} \\\\ \\text{Manshub bil-Alif: أَبَا} \\\\ \\text{Majrur bil-Yaa': أَبِي} \\end{cases}",
            "legend": "• Syarat i'rab dengan huruf: bersambung dengan mudhaf ilaih selain ya' mutakallim"
        },
        "hints": {
            "concept": "Asma'ul khamsah (abuu, akhuu, hamuu, fuu, dhuu) bila marfu' bertanda huruf Wawu (أَبُو).",
            "execution": "Pilih: 'أَبُو' (abuu)."
        }
    },
    {
        "id": "arb-lat-e-19",
        "materi": "TATA BAHASA NAHWU: LA NAHIYAH VS LA NAFYAH",
        "topic": "Perbedaan Laa an-Nahiyah (Melarang/Jazm) dan Laa an-Nafiyah (Menolak/Rafa')",
        "stem": "Cermati dua kalimat berikut:\n1) 'يَا مُحَمَّدُ، لَا تَكْذِبْ فِي كَلَامِكَ!' (Wahai Muhammad, janganlah kamu berbohong dalam ucapanmu!).\n2) 'مُحَمَّدٌ لَا يَكْذِبُ فِي كَلَامِهِ.' (Muhammad tidak berbohong dalam ucapannya).\nAnalisis gramatikal yang TEPAT mengenai jenis huruf 'لَا' dan harakat fi'il pada kedua kalimat tersebut adalah...",
        "correct": "Kalimat 1 menggunakan Laa an-Nahiyah (larangan yang menjazmkan fi'il dengan sukun), sedangkan Kalimat 2 menggunakan Laa an-Nafiyah (peniadaan kabar yang membiarkan fi'il tetap marfu' dengan dhommah).",
        "distractors": [
            "Kalimat 1 dan 2 sama-sama menggunakan Laa an-Nahiyah yang mewajibkan harakat fathah pada fi'il mudhari'.",
            "Kalimat 1 adalah Laa an-Nafiyah pembuat ragu, sedangkan Kalimat 2 adalah huruf syarat penegas sumpah.",
            "Kalimat 1 memanshubkan fi'il mudhari', sedangkan Kalimat 2 memajzumkan fi'il madhi.",
            "Kalimat 1 berfungsi sebagai huruf jar, sedangkan Kalimat 2 berfungsi sebagai isim istifham penanya."
        ],
        "formula": {
            "title": "DISTINGSI LAA NAHIYAH VS LAA NAFIYAH",
            "latex": "\\begin{cases} \\mathbf{\\text{لَا النَّاهِيَةُ (Larangan):}} & \\text{Menjazmkan fi'il mudhari' } \\to \\mathbf{\\text{لَا تَكْذِبْ (Sukun)}} \\\\ \\mathbf{\\text{لَا النَّافِيَةُ (Peniadaan):}} & \\text{Tidak beramal (tetap marfu') } \\to \\mathbf{\\text{لَا يَكْذِبُ (Dhommah)}} \\end{cases}",
            "legend": "• Nahiyah mengandung tuntutan pencegahan (larangan), Nafiyah hanya berita negatif"
        },
        "hints": {
            "concept": "Laa Nahiyah (larangan/jangan) menjazmkan fi'il (sukun). Laa Nafiyah (tidak/hanya berita) tidak mengubah i'rab (tetap marfu' dhommah).",
            "execution": "Pilih opsi: Kalimat 1 Laa an-Nahiyah (menjazmkan), Kalimat 2 Laa an-Nafiyah (tetap marfu')."
        }
    },
    {
        "id": "arb-lat-e-20",
        "materi": "FAHM AL-MAQRU' & KOSA KATA",
        "topic": "Antonim Kata (المُتَضَادّ) dalam Konteks Keseharian",
        "stem": "Dalam wacana bahasa Arab, kata 'النَّجَاحُ' (an-najaahu) memiliki arti 'kesuksesan / keberhasilan'. Lawan kata (*antonim / al-adh-dhad*) yang TEPAT dari kata tersebut adalah...",
        "correct": "الفَشَلُ (al-fasyalu - kegagalan / ketidakberhasilan).",
        "distractors": [
            "الفَوْزُ (al-fawzu - sinonim yang bermakna kemenangan atau keberuntungan besar).",
            "السَّعَادَةُ (as-sa'aadatu - kebahagiaan atau ketenteraman batin jiwa).",
            "الصِّحَّةُ (ash-shihhatu - kesehatan fisik tubuh dan kebugaran raga).",
            "الكَسَلُ (al-kasalu - sifat malas dalam menjalankan aktivitas pekerjaan)."
        ],
        "formula": {
            "title": "ANTONIM KOSAKATA (المُتَضَادّ)",
            "latex": "\\mathbf{\\text{النَّجَاحُ (Sukses/Berhasil)}} \\iff \\mathbf{\\text{Lawan Kata: الفَشَلُ (Gagal)}}",
            "legend": "• Penguasaan pasangan antonim penting untuk inferensi makna teks wacana qira'ah"
        },
        "hints": {
            "concept": "Lawan kata dari an-najah (sukses) adalah al-fasyal (kegagalan).",
            "execution": "Pilih: 'الفَشَلُ' (al-fasyalu)."
        }
    },
    {
        "id": "arb-lat-e-21",
        "materi": "TATA BAHASA NAHWU: HURUF ISTIFHAM",
        "topic": "Penggunaan Kata Tanya 'كَمْ' (Berapa) dan I'rab Tamyiz-nya",
        "stem": "Perhatikan kalimat tanya berikut:\n'كَمْ ... اشْتَرَيْتَ مِنَ المَعْرِضِ اليَوْمَ؟'\n(Berapa ... yang telah kamu beli dari pameran hari ini?).\nKata yang TEPAT untuk mengisi posisi tamyiz setelah kata tanya bilangan 'كَمْ' al-istifhamiyyah (wajib berbentuk mufrad manshub) adalah...",
        "correct": "كِتَابًا (kitaaban - isim mufrad manshub bertanwin fathah sebagai tamyiz kam istifhamiyyah).",
        "distractors": [
            "كُتُبٌ (kutubun - jama' taksir marfu' yang menyalahi kaidah mufrad manshub).",
            "كِتَابٍ (kitaabin - majrur dengan kasratain yang hanya berlaku pada kam khabariyyah).",
            "الكِتَابُ (al-kitaabu - isim ma'rifah ber-alif lam yang tidak boleh menjadi tamyiz).",
            "كِتَابَانِ (kitaabaani - mutsanna marfu' dengan alif yang tidak memenuhi syarat tamyiz)."
        ],
        "formula": {
            "title": "TAMYIZ KAM ISTIFHAMIYYAH",
            "latex": "\\text{كَمْ الاِسْتِفْهَامِيَّةُ} + \\mathbf{\\text{Tamyiz (Isim Mufrad Nakirah Manshub)}} \\implies [\\text{كَمْ } \\mathbf{\\text{كِتَابًا}} \\text{؟}]",
            "legend": "• Tamyiz kam istifhamiyyah selalu berstatus mufrad manshub fathatain"
        },
        "hints": {
            "concept": "Setelah 'كَمْ' istifhamiyyah (menanyakan jumlah), kata bendanya wajib berbentuk mufrad nakirah manshub (tamyiz).",
            "execution": "Pilih bentuk mufrad manshub bertanwin fathah: 'كِتَابًا' (kitaaban)."
        }
    },
    {
        "id": "arb-lat-e-22",
        "materi": "TATA BAHASA NAHWU: ISIM ISYARAH",
        "topic": "Kesesuaian Isim Isyarah dengan Benda Jamak Ghairu Aqil",
        "stem": "Dalam kaidah tata bahasa Arab, setiap bentuk jamak yang tidak berakal (*jama' ghairu 'aqil*) diperlakukan secara gramatikal setara dengan isim mufrad mu'annats. Manakah penggunaan isim isyarah (kata tunjuk dekat) yang TEPAT untuk menunjuk 'هَذِهِ الكُتُبُ' (buku-buku ini)?",
        "correct": "هَذِهِ الكُتُبُ نَافِعَةٌ (hadhihi al-kutubu naafi'atun - menggunakan hadhihi karena al-kutub adalah jama' taksir ghairu 'aqil).",
        "distractors": [
            "هَؤُلَاءِ الكُتُبُ نَافِعَةٌ (ha'ulaa'i hanya diperuntukkan bagi jamak manusia berakal).",
            "هَذَا الكُتُبُ نَافِعٌ (hadha adalah kata tunjuk untuk mufrad mudzakkar).",
            "هَذَانِ الكُتُبُ نَافِعَانِ (hadhaani adalah kata tunjuk untuk isim mutsanna dua orang).",
            "ذَلِكَ الكُتُبُ نَافِعَاتٌ (dhalika adalah kata tunjuk jauh untuk tunggal mudzakkar)."
        ],
        "formula": {
            "title": "KAIDAH JAMA' GHAIRU 'AQIL",
            "latex": "\\mathbf{\\text{كُلُّ جَمْعٍ غَيْرِ عَاقِلٍ يُعَامَلُ مُعَامَلَةَ المُفْرَدِ المُؤَنَّثِ}} \\implies [\\mathbf{\\text{هَذِهِ}} \\text{ الكُتُبُ } \\mathbf{\\text{نَافِعَةٌ}}]",
            "legend": "• Setiap kata benda jamak tidak berakal berpasangan dengan kata tunjuk dan sifat mufrad mu'annats"
        },
        "hints": {
            "concept": "Kaidah baku: 'Kullu jam'in ghairi 'aaqilin mu'annats' (Setiap jamak tak berakal dihukumi mufrad mu'annats). Gunakan 'هَذِهِ'.",
            "execution": "Pilih kalimat: 'هَذِهِ الكُتُبُ نَافِعَةٌ'."
        }
    },
    {
        "id": "arb-lat-e-23",
        "materi": "SHOROF & MORFOLOGI: ISIM TAFDHIL",
        "topic": "Pola Pembentukan Wazan Isim Tafdhil (أَفْعَلُ مِنْ)",
        "stem": "Untuk menyatakan perbandingan komparatif 'lebih besar daripada' yang diturunkan dari kata sifat 'كَبِيرٌ' (kabiirun), susunan isim tafdhil yang BENAR menurut kaidah shorof adalah...",
        "correct": "أَكْبَرُ مِنْ (akbaru min - mengikuti wazan af'alu min untuk menyatakan komparasi sifat).",
        "distractors": [
            "كَبِيرٌ مِنْ (kabiirun min - bentuk sifat musyabbahah biasa tanpa perubahan wazan tafdhil).",
            "مَكْبُورٌ مِنْ (makbuurun min - bentuk wazan isim maf'ul yang keliru makna).",
            "تَكْبِيرٌ مِنْ (takbiirun min - bentuk masdar dari wazan fa''ala yang bermakna mengagungkan).",
            "أَكْبَرِينَ مِنْ (akbariina min - bentuk jamak yang tidak lazim dalam konstruksi komparatif tunggal)."
        ],
        "formula": {
            "title": "RUMUS ISIM TAFDHIL (KOMPARATIF)",
            "latex": "\\text{Sifat (كَبِيرٌ: Besar)} \\xrightarrow{\\mathbf{\\text{Wazan أَفْعَلُ + مِنْ}}} \\mathbf{\\text{أَكْبَرُ مِنْ (Lebih besar daripada)}}",
            "legend": "• Isim tafdhil bersifat ghairu munsharif (tidak menerima tanwin pada wazan af'alu)"
        },
        "hints": {
            "concept": "Isim tafdhil untuk perbandingan komparatif (lebih ... daripada) mengikuti wazan 'أَفْعَلُ مِنْ' (af'alu min). Kabiirun -> Akbaru min.",
            "execution": "Pilih: 'أَكْبَرُ مِنْ' (akbaru min)."
        }
    },
    {
        "id": "arb-lat-e-24",
        "materi": "FAHM AL-MAQRU' & SINTAKSIS",
        "topic": "Menentukan Gagasan Utama (الفِكْرَةُ الرَّئِيسِيَّةُ) Paragraf Pendek",
        "stem": "Bacalah teks ringkas berikut:\n'اللُّغَةُ العَرَبِيَّةُ لُغَةٌ عَالَمِيَّةٌ عَظِيمَةٌ. يَنْطِقُ بِهَا مِئَاتُ المَلَايِينِ حَوْلَ العَالَمِ، وَهِيَ لُغَةُ القُرْآنِ الكَرِيمِ وَمَصْدَرُ الحَضَارَةِ الإِسْلَامِيَّةِ.'\nGagasan utama (*al-fikrah ar-ra'iisiyyah*) dari teks wacana di atas adalah...",
        "correct": "Kedudukan luhur dan fungsi global bahasa Arab sebagai bahasa internasional dan bahasa peradaban Islam.",
        "distractors": [
            "Kewajiban membeli kamus tebal terbitan luar negeri bagi setiap turis yang berlibur ke Timur Tengah.",
            "Jumlah total percetakan buku tulis yang beroperasi di sepanjang pesisir Laut Merah.",
            "Metode bertani gandum modern di kawasan padang pasir jazirah Arab pada masa lampau.",
            "Silsilah raja-raja kekaisaran Romawi kuno yang menaklukkan wilayah semenanjung Mediterania."
        ],
        "formula": {
            "title": "IDENTIFIKASI GAGASAN UTAMA (الفِكْرَةُ الرَّئِيسِيَّةُ)",
            "latex": "\\begin{pmatrix} \\text{اللغة العربية لغة عالمية} \\\\ \\text{لغة القرآن الكريم} \\\\ \\text{مصدر الحضارة} \\end{pmatrix} \\implies \\mathbf{\\text{Kedudukan Luhur \\& Fungsi Global Bahasa Arab}}",
            "legend": "• Gagasan utama merangkum inti pesan wacana tanpa terdistraksi detail pelengkap"
        },
        "hints": {
            "concept": "Teks berbicara tentang bahasa Arab sebagai bahasa global (lisan dunia), bahasa Al-Qur'an, dan sumber peradaban Islam.",
            "execution": "Pilih opsi: Kedudukan luhur dan fungsi global bahasa Arab sebagai bahasa internasional dan peradaban."
        }
    },
    {
        "id": "arb-lat-e-25",
        "materi": "TATA BAHASA NAHWU: DHARAF MAKAN & ZAMAN",
        "topic": "I'rab Maf'ul Fih / Dharaf (Manshub bil-Fathah)",
        "stem": "Perhatikan kalimat keterangan berikut:\n'يَسْتَرِيحُ الفَلَّاحُ ... الشَّجَرَةِ الكَبِيرَةِ بَعْدَ العَمَلِ الشَّاقِّ.'\n(Petani itu beristirahat di ... pohon besar setelah kerja kerasnya).\nKata keterangan tempat (dharaf makan manshub) yang TEPAT untuk melengkapi kalimat tersebut adalah...",
        "correct": "تَحْتَ (tahta - dharaf makan manshub bil-fathah bermakna 'di bawah').",
        "distractors": [
            "تَحْتُ (tahtu - marfu' dengan dhommah yang menyalahi i'rab asli dharaf beridhafah).",
            "تَحْتِ (tahti - majrur dengan kasrah yang keliru tanpa adanya huruf jar pendahulu).",
            "فَوْقَ (fawqa - bermakna 'di atas' yang tidak logis untuk tempat berteduh santai petani).",
            "خَلْفُ (khalfu - berharakat dhommah yang tidak sesuai posisi nashab dharaf)."
        ],
        "formula": {
            "title": "I'RAB DHARAF MAKAN (MAF'UL FIH)",
            "latex": "\\text{Dharaf Makan Manshub (تَحْتَ)} + \\text{Mudhaf Ilaih Majrur (الشَّجَرَةِ)} \\implies [\\mathbf{\\text{تَحْتَ}} \\text{ الشَّجَرَةِ}]",
            "legend": "• Dharaf tempat berkedudukan manshub fathah ketika berperan sebagai mudhaf keterangan tempat"
        },
        "hints": {
            "concept": "Kata keterangan tempat (dharaf makan) seperti tahta berkedudukan manshub dengan fathah: 'تَحْتَ' (di bawah).",
            "execution": "Pilih 'تَحْتَ' (tahta)."
        }
    }
]
