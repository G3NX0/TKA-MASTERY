# -*- coding: utf-8 -*-
"""
bahasa_arab_data_simulasi.py
-----------------------------
35 Authentic Simulasi CBT HOTS Questions for TKA 2026 Bahasa Arab (SMA/MA Bahasa & Budaya / Agama).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
Composition:
- 25 MCQ items (arb-sim-01 .. arb-sim-25)
- 5 Multi-select items (arb-sim-26 .. arb-sim-30)
- 5 Matrix Benar-Salah items (arb-sim-31 .. arb-sim-35)
"""

BAHASA_ARAB_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 MCQ ITEMS (arb-sim-01 .. arb-sim-25)
    # -------------------------------------------------------------
    {
        "id": "arb-sim-01",
        "materi": "TATA BAHASA NAHWU: NAWASIKH KAANA",
        "topic": "Isim Kaana Jama' Mu'annats Salim Marfu' & Khabar Kaana Manshub",
        "stem": "Perhatikan kalimat dengan amil nawasikh Kaana berikut:\n'كَانَتِ الطَّالِبَاتُ فِي مَعْمَلِ اللُّغَةِ ... بِتَوْجِيهَاتِ المُعَلِّمِ.'\n(Para siswi di laboratorium bahasa dahulu adalah ... terhadap petunjuk guru).\nKata yang TEPAT untuk berkedudukan sebagai Khabar Kaana (jama' mu'annats salim manshub dengan tanda harakat kasrah) adalah...",
        "correct": "مُنْصِتَاتٍ (munshitaatin - khabar kaana manshub dengan harakat kasratain sebagai pengganti fathah pada jama' mu'annats salim).",
        "distractors": [
            "مُنْصِتَاتٌ (munshitaatun - marfu' dengan dhommatain yang keliru untuk posisi khabar kaana).",
            "مُنْصِتُونَ (munshituuna - jama' mudzakkar salim yang menyalahi gender siswi perempuan).",
            "مُنْصِتَاتًا (munshitaatan - penambahan fathatain yang mustahil secara kaidah pada jama' mu'annats salim).",
            "مُنْصِتَةً (munshitatan - mufrad yang tidak selaras dengan subjek thalibaat yang jamak)."
        ],
        "formula": {
            "title": "I'RAB JAMA' MU'ANNATS SALIM PADA KHABAR KAANA",
            "latex": "\\text{كَانَتْ} + \\text{الطَّالِبَاتُ (Isim Kaana Marfu' bil-Dhommah)} + \\mathbf{\\text{مُنْصِتَاتٍ (Khabar Kaana Manshub bil-Kasrah)}}",
            "legend": "• Jama' mu'annats salim bertanda rafa' dhommah, serta bertanda nashab dan jar kasrah (tanpa fathah)"
        },
        "hints": {
            "concept": "Khabar kaana berkedudukan manshub. Pada jama' mu'annats salim, tanda nashab-nya adalah kasrah (kasratain): 'مُنْصِتَاتٍ'.",
            "execution": "Pilih: 'مُنْصِتَاتٍ' (munshitaatin)."
        }
    },
    {
        "id": "arb-sim-02",
        "materi": "TATA BAHASA NAHWU: NAWASIKH INNA",
        "topic": "Isim Inna Asma'ul Khamsah Manshub bil-Alif",
        "stem": "Cermati kalimat inna berikut ini:\n'إِنَّ ... بَكْرٍ الصِّدِّيقَ كَانَ أَوَّلَ الخُلَفَاءِ الرَّاشِدِينَ مَكَانَةً.'\n(Sesungguhnya Abu Bakar ash-Shiddiq adalah khalifah rasyidin pertama yang mulia kedudukannya).\nBentuk kata Asma'ul Khamsah yang TEPAT untuk mengisi posisi Isim Inna (manshub dengan tanda huruf alif) adalah...",
        "correct": "أَبَا (Abaa - isim inna manshub dengan tanda huruf alif karena bagian dari Asma'ul Khamsah).",
        "distractors": [
            "أَبُو (Abuu - marfu' dengan huruf wawu yang keliru untuk posisi isim inna).",
            "أَبِي (Abii - majrur dengan huruf ya' yang hanya berlaku jika ada huruf jar).",
            "أَبٌ (Abun - mufrad bertanwin tanpa idhafah yang tidak cocok untuk nama gelar Abu Bakar).",
            "إِبَّا (Ibbaa - kesalahan ortografi yang tidak ada dalam kosakata bahasa Arab fusha)."
        ],
        "formula": {
            "title": "I'RAB ASMA'UL KHAMSAH SETELAH INNA",
            "latex": "\\text{إِنَّ (Amil Nashab)} + \\mathbf{\\text{Isim Inna (أَبَا - Manshub bil-Alif)}} + \\text{Mudhaf Ilaih (بَكْرٍ)}",
            "legend": "• Asma'ul khamsah bertanda nashab Alif saat bersambung dengan mudhaf ilaih isim zhahir"
        },
        "hints": {
            "concept": "Isim Inna berkedudukan manshub. Tanda nashab Asma'ul Khamsah adalah huruf Alif (أَبَا بَكْرٍ).",
            "execution": "Pilih: 'أَبَا' (Abaa)."
        }
    },
    {
        "id": "arb-sim-03",
        "materi": "SHOROF & MORFOLOGI: WAZAN TAFA''ALA",
        "topic": "Faedah Makna At-Tadrij / At-Takalluf pada Wazan Tafa''ala (تَعَلَّمَ)",
        "stem": "Kata 'عَلِمَ' (mengetahui) ketika ditashrif ke wazan tsulatsi mazid bi harfaini 'تَفَعَّلَ' (تَعَلَّمَ - ta'allama) memiliki makna 'belajar'. Ditinjau dari kaidah semantik shorof, penambahan huruf ta' dan tasydid pada wazan تَعَلَّمَ mengandung faedah makna...",
        "correct": "At-Tadrij wat-Takalluf (memperoleh ilmu secara bertahap sedikit demi sedikit dengan kesungguhan usaha batin).",
        "distractors": [
            "Al-Musyarakah al-Kamilah (saling bertukar pengetahuan secara instan tanpa proses berpikir).",
            "At-Ta'diyah al-Mujarradah (semata-mata menjadikan orang lain mengetahui tanpa usaha pribadi).",
            "Li Thalabil Maal (memohon bayaran upah materi atas jasa mengajar di ruang kelas).",
            "Li Nafyil Fahm (peniadaan pemahaman terhadap isi teks buku bacaan)."
        ],
        "formula": {
            "title": "FAEDAH WAZAN تَفَعَّلَ (تَعَلَّمَ)",
            "latex": "\\text{عَلِمَ (Tahu)} \\xrightarrow{\\mathbf{\\text{Wazan تَفَعَّلَ}}} \\mathbf{\\text{تَعَلَّمَ (Belajar)}} \\implies \\text{Faedah: At-Tadrij (Bertahap) \\& At-Takalluf (Bersungguh-sungguh)}",
            "legend": "• Menggambarkan proses perolehan kompetensi yang memerlukan ketekunan waktu dan daya juang"
        },
        "hints": {
            "concept": "Wazan تَفَعَّلَ (seperti ta'allama) berfaedah at-tadrij (bertahap sedikit demi sedikit) dan at-takalluf (usaha sungguh-sungguh).",
            "execution": "Pilih: At-Tadrij wat-Takalluf (memperoleh ilmu bertahap sedikit demi sedikit dengan kesungguhan)."
        }
    },
    {
        "id": "arb-sim-04",
        "materi": "SHOROF & MORFOLOGI: WAZAN ISTAF'ALA",
        "topic": "Analisis Semantik Wazan Istaf'ala pada Kata 'اسْتَخْرَجَ'",
        "stem": "Dalam wacana geologi dan ekonomi pertambangan, kalimat 'اسْتَخْرَجَتِ الشَّرِكَةُ الوَطَنِيَّةُ النِّفْطَ مِنَ الآبَارِ البَحْرِيَّةِ' menggunakan fi'il 'اسْتَخْرَجَ' (istakhraja). Makna gramatikal yang tepat dari kata 'اسْتَخْرَجَ' dalam konteks tersebut adalah...",
        "correct": "Mengeksplorasi dan mengeluarkan minyak bumi dari kedalaman sumur dengan mengerahkan daya upaya dan teknologi mesin.",
        "distractors": [
            "Memohon agar minyak bumi keluar dengan sendirinya tanpa perlu melakukan pengeboran.",
            "Berpura-pura mengeluarkan minyak mentah demi mengelabui para pengawas pelabuhan internasional.",
            "Menjual seluruh kilang pengeboran lepas pantai kepada konsorsium maskapai penerbangan asing.",
            "Menimbun kembali sumur-sumur minyak dengan pasir pantai agar tidak dapat dimanfaatkan."
        ],
        "formula": {
            "title": "SEMANTIK WAZAN اسْتَفْعَلَ (اسْتَخْرَجَ)",
            "latex": "\\text{خَرَجَ (Keluar)} \\xrightarrow{\\mathbf{\\text{Wazan اسْتَفْعَلَ}}} \\mathbf{\\text{اسْتَخْرَجَ}} \\implies \\text{Mengerahkan upaya keras untuk mengekstrak/mengeluarkan}",
            "legend": "• Menunjukkan proses ekstraksi komoditas bernilai tinggi dengan teknologi rekayasa"
        },
        "hints": {
            "concept": "Kata 'istakhraja' berarti mengerahkan tenaga/alat untuk mengeluarkan atau mengeksplorasi bahan tambang.",
            "execution": "Pilih opsi: Mengeksplorasi dan mengeluarkan minyak bumi dengan daya upaya dan teknologi mesin."
        }
    },
    {
        "id": "arb-sim-05",
        "materi": "TATA BAHASA NAHWU: DHARAF MUKHTASH VS GHAIRU MUKHTASH",
        "topic": "I'rab Maf'ul Fih Ghairu Mukhtash (Zaman & Makan)",
        "stem": "Dalam kaidah nahwu, semua isim zaman (waktu) boleh di-i'rab sebagai zharf zaman manshub baik yang terbatas (*mukhtash*) maupun tidak terbatas (*mubham/ghairu mukhtash*). Namun untuk isim makan (tempat), hanya isim makan mubham yang boleh langsung di-i'rab sebagai zharf makan manshub. Manakah kalimat berikut yang MENERAPKAN isim makan mubham manshub secara TEPAT?",
        "correct": "وَقَفَ الخَطِيبُ أَمَامَ الجُمْهُورِ يُلْقِي خُطْبَتَهُ (amama adalah zharf makan mubham penunjuk arah depan yang sah berharakat manshub).",
        "distractors": [
            "صَلَّيْتُ المَسْجِدَ بِالنَّصْبِ بِلَا حَرْفِ جَرٍّ (salah karena al-masjid adalah isim makan mukhtash yang wajib didahului huruf jar fii).",
            "جَلَسْتُ الفَصْلَ لِسَمَاعِ الشَّرْحِ (salah karena al-fashl adalah tempat terbatas yang wajib memakai fii al-fashli).",
            "نِمْتُ البَيْتَ لَيْلًا (salah karena al-bait adalah mukhtash yang tidak boleh langsung dinashabkan sebagai zharf).",
            "سَافَرْتُ مَكَّةَ لِلْعُمْرَةِ (salah karena Makkah adalah nama kota terbatas yang wajib diawali ilaa)."
        ],
        "formula": {
            "title": "SYARAT NASHAB DHARAF MAKAN",
            "latex": "\\text{Dharaf Makan} = \\begin{cases} \\mathbf{\\text{Mubham (Jihatus Sitt: أَمَامَ، خَلْفَ):}} & \\mathbf{\\text{Sah Manshub Langsung (أَمَامَ الجُمْهُورِ)}} \\\\ \\text{Mukhtash (Tempat Berbatas: المَسْجِد):} & \\text{Wajib Majrur dengan فِي (فِي المَسْجِدِ)} \\end{cases}",
            "legend": "• Isim makan mukhtash (berbatas dinding/wilayah) tidak boleh langsung dinashabkan tanpa fi'il dakhala"
        },
        "hints": {
            "concept": "Zharf makan yang boleh langsung dinashabkan adalah isim makan mubham (arah yang 6: amama, khala, fawqa, tahta, yamina, syimala). Tempat berbatas seperti masjid/kelas wajib memakai huruf jar 'fii'.",
            "execution": "Pilih: 'وَقَفَ الخَطِيبُ أَمَامَ الجُمْهُورِ'."
        }
    },
    {
        "id": "arb-sim-06",
        "materi": "TATA BAHASA NAHWU: ADWATUL ISTITSNA' (خَلَا / عَدَا / حَاشَا)",
        "topic": "Dualisme Hukum I'rab Mustatsna setelah Khala dan 'Ada",
        "stem": "Perhatikan kalimat pengecualian berikut:\n'نَجَحَ الطُّلَّابُ فِي الِامْتِحَانِ خَلَا ...'\n(Para siswa telah lulus dalam ujian itu kecuali ...).\nApabila kata 'خَلَا' (khalaa) pada kalimat di atas dianggap sebagai HURUF JAR (karena tidak didahului 'مَا' mashdariyyah), maka kata setelahnya berstatus...",
        "correct": "Majrur bil-kasrah: طَالِبٍ (thaalibin - berharakat kasratain sebagai isim majrur oleh huruf jar khala).",
        "distractors": [
            "Wajib marfu' bil-dhommah: طَالِبٌ (thaalibun - yang tidak memiliki landasan gramatikal sama sekali).",
            "Mabni di atas sukun mutlak tanpa memedulikan harakat fonetis.",
            "Wajib ber-alif lam mutsanna marfu' dengan huruf alif.",
            "Berstatus sebagai khabar kaana yang tersembunyi di dalam dada pembicara."
        ],
        "formula": {
            "title": "HUKUM I'RAB KHALLA / 'ADA / HASYA (خَلَا، عَدَا، حَاشَا)",
            "latex": "\\text{خَلَا / عَدَا (Tanpa مَا)} \\implies \\begin{cases} \\text{Dianggap Fi'il Madhi:} & \\text{Kata setelahnya Manshub (Maf'ul Bih: طَالِبًا)} \\\\ \\mathbf{\\text{Dianggap Huruf Jar:}} & \\mathbf{\\text{Kata setelahnya Majrur (Isim Majrur: طَالِبٍ)}} \\end{cases}",
            "legend": "• Bila didahului 'مَا' (مَا خَلَا / مَا عَدَا), maka wajib fi'il dan kata setelahnya wajib manshub"
        },
        "hints": {
            "concept": "Jika 'خَلَا' dianggap huruf jar (karena tanpa 'مَا'), maka kata setelahnya berkedudukan sebagai isim majrur bil-kasrah: 'طَالِبٍ'.",
            "execution": "Pilih opsi: Majrur bil-kasrah: 'طَالِبٍ' (thaalibin)."
        }
    },
    {
        "id": "arb-sim-07",
        "materi": "TATA BAHASA NAHWU: ADAD MA'DUD (ALFAZHUL 'UQUD)",
        "topic": "I'rab Bilangan Puluhan 'Uqud (20, 30, ... 90) dan Tamyiz-nya",
        "stem": "Perhatikan kalimat transaksi berikut:\n'دَفَعَ التَّاجِرُ ... أَلْفَ رُوبِيَّةٍ لِشِرَاءِ البَضَائِعِ.'\n(Pedagang itu telah membayar ... ribu rupiah untuk membeli barang dagangan).\nJika pedagang membayar sebesar 'tiga puluh ribu' dan kata bilangan 'tiga puluh' tersebut menduduki posisi Maf'ul Bih (manshub), maka bentuk kata bilangan puluhan 'uqud yang BENAR adalah...",
        "correct": "ثَلَاثِينَ (tsalaathiina - maf'ul bih manshub dengan tanda ya' karena mulhaq bi jama' mudzakkar salim).",
        "distractors": [
            "ثَلَاثُونَ (tsalaatsuuna - marfu' dengan wawu yang keliru untuk posisi objek penderita).",
            "ثَلَاثَةَ (tsalaatsata - bentuk satuan mu'annats bermakna tiga, bukan tiga puluh).",
            "ثَلَاثُ (tsalaatsu - bentuk satuan mudzakkar yang salah makna).",
            "ثَلَاثَاتٍ (tsalaatsaatin - bentuk jamak yang tidak ada dalam kaidah bilangan puluhan)."
        ],
        "formula": {
            "title": "I'RAB ALFAZHUL 'UQUD (عُقُودُ الأَعْدَادِ)",
            "latex": "\\text{Maf'ul Bih Manshub} \\implies \\mathbf{\\text{ثَلَاثِينَ (Manshub bil-Yaa')}} \\iff \\text{Mulhaq bi Jama' Mudzakkar Salim}",
            "legend": "• Alfazhul 'uqud (20-90) dihukumi sama seperti jama' mudzakkar salim: rafa' wawu, nashab/jar ya'"
        },
        "hints": {
            "concept": "Bilangan puluhan (alfazhul 'uqud: 20-90) mulhaq jama' mudzakkar salim. Pada posisi maf'ul bih (manshub), tandanya adalah huruf ya': 'ثَلَاثِينَ'.",
            "execution": "Pilih: 'ثَلَاثِينَ' (tsalaathiina)."
        }
    },
    {
        "id": "arb-sim-08",
        "materi": "TATA BAHASA NAHWU: AL-HAAL JUMLAH",
        "topic": "Struktur Haal Berupa Jumlah Ismiyyah dengan Wawul Hal",
        "stem": "Perhatikan kalimat berikut:\n'خَرَجَ المُسَافِرُ مِنَ القَرْيَةِ ...'\n(Pengembara itu telah keluar dari desa dalam keadaan matahari sedang terbit).\nKaidah nahwu mewajibkan adanya *Wawul Hal* dan dhamir (atau salah satunya) sebagai pengikat (*raabith*) ketika Haal berbentuk Jumlah Ismiyyah. Susunan Haal Jumlah Ismiyyah yang SAHIH untuk melengkapi kalimat tersebut adalah...",
        "correct": "وَالشَّمْسُ طَالِعَةٌ (wasy-syamsu thaali'atun - wawul hal menghubungkan jumlah ismiyyah mubtada' dan khabar yang berada pada posisi fi mahalli nashbin haal).",
        "distractors": [
            "الشَّمْسُ طَالِعَةٌ بِدُونِ وَاوٍ (tanpa wawul hal yang menyebabkan kalimat terputus tanpa ikatan raabith).",
            "وَالشَّمْسَ طَالِعَةً (menashabkan mubtada' dan khabar secara keliru tanpa adanya amil nawasikh).",
            "وَالشَّمْسِ طَالِعَةٍ (memajrurkan mubtada' dan khabar seolah-olah wawu tersebut adalah wawu qasam).",
            "طَالِعَةُ الشَّمْسِ بِالإِضَافَةِ (susunan idhafah yang tidak membentuk struktur klausa keadaan berwawu)."
        ],
        "formula": {
            "title": "STRUKTUR HAAL JUMLAH ISMIYYAH",
            "latex": "\\text{Shahibul Hal (المُسَافِرُ)} + \\mathbf{\\text{Wawul Hal (وَـ)}} + \\mathbf{\\text{Jumlah Ismiyyah (الشَّمْسُ طَالِعَةٌ)}} \\implies \\text{Fi Mahalli Nashbin Haal}",
            "legend": "• Wawul hal berfungsi mengikat klausa kondisi serempak dengan tindakan fi'il utama"
        },
        "hints": {
            "concept": "Haal berupa jumlah ismiyyah wajib diawali Wawul Hal, dan di dalamnya tersusun dari mubtada' marfu' dan khabar marfu': 'وَالشَّمْسُ طَالِعَةٌ'.",
            "execution": "Pilih: 'وَالشَّمْسُ طَالِعَةٌ' (wasy-syamsu thaali'atun)."
        }
    },
    {
        "id": "arb-sim-09",
        "materi": "TATA BAHASA NAHWU: AT-TAMYIZ",
        "topic": "Tamyiz Malfuzh dari Isim Takaran / Ukuran (Kail / Wazn)",
        "stem": "Cermati kalimat berikut:\n'اشْتَرَى أَبِي رِطْلًا ... مِنَ السُّوقِ المَرْكَزِيِّ.'\n(Ayahku telah membeli satu rithl [ukuran timbangan] ... dari pasar induk).\nKata yang TEPAT untuk berkedudukan sebagai Tamyiz Malfuzh (isim nakirah manshub penjelas kesamaran kata ukuran timbangan rithlan) adalah...",
        "correct": "عَسَلًا (asalan - tamyiz malfuzh manshub dengan harakat fathatain bermakna madu).",
        "distractors": [
            "عَسَلٌ (asalun - marfu' dengan dhommatain yang keliru untuk posisi tamyiz).",
            "عَسَلٍ (asalin - majrur yang hanya sah jika susunan diubah menjadi idhafah rithla 'asalin).",
            "العَسَلُ (al-'asalu - isim ma'rifah yang tidak memenuhi syarat kenakiran tamyiz).",
            "بِالعَسَلِ (bil-'asali - susunan huruf jar majrur yang tidak membentuk tamyiz malfuzh murni)."
        ],
        "formula": {
            "title": "TAMYIZ MALFUZH UKURAN TIMBANGAN",
            "latex": "\\text{Isim Timbangan (رِطْلًا)} + \\mathbf{\\text{Tamyiz Malfuzh (عَسَلًا - Manshub bil-Fathah)}}",
            "legend": "• Tamyiz malfuzh menjelaskan kesamaran kata benda penakar, penimbang, atau pengukur"
        },
        "hints": {
            "concept": "Setelah isim ukuran/timbangan (rithlan), kata penjelas jenisnya adalah Tamyiz Malfuzh yang berstatus nakirah manshub: 'عَسَلًا'.",
            "execution": "Pilih kata bertanwin fathah: 'عَسَلًا' (asalan)."
        }
    },
    {
        "id": "arb-sim-10",
        "materi": "BALAGHAH: ILMU BAYAN (AL-MAJAZ AL-MURSAL)",
        "topic": "Analisis Hubungan Relasi Sebab ('Alaqah Sababiyyah) pada Majaz Mursal",
        "stem": "Perhatikan kalimat majaz sastra Arab berikut:\n'رَعَتِ المَاشِيَةُ الغَيْثَ'\n(Hewan ternak itu memakan hujan).\nSecara harfiah, hewan ternak memakan rumput/tumbuhan hijau, bukan memakan butiran air hujan (*al-ghaits*). Penggunaan kata 'hujan' untuk memaksudkan 'rumput' diklasifikasikan sebagai Majaz Mursal dengan 'Alaqah (hubungan korelasi)...",
        "correct": "Sababiyyah (سَبَبِيَّةٌ - menyebutkan sebab yaitu hujan, tetapi yang dimaksudkan adalah akibat yang ditimbulkannya yaitu tumbuhnya rumput).",
        "distractors": [
            "Musabbabiyyah (penyebutan akibat untuk memaksudkan sebab terjadinya peristiwa).",
            "Kulliyyah (penyebutan keseluruhan tubuh untuk memaksudkan satu ujung jari).",
            "Juz'iyyah (penyebutan sebagian kecil untuk memaksudkan keseluruhan badan).",
            "I'tibaru Ma Kaana (penyebutan masa lalu seseorang sebelum berganti status)."
        ],
        "formula": {
            "title": "MAJAZ MURSAL: 'ALAQAH SABABIYYAH",
            "latex": "\\text{Lafadz Disebut: الغَيْثَ (Hujan = Sebab)} \\implies \\mathbf{\\text{Makna Dimaksud: Rumput/Tumbuhan (Akibat)}} \\implies \\text{'Alaqah Sababiyyah}",
            "legend": "• Hujan adalah sebab utama tumbuhnya rerumputan yang dimakan kawanan ternak"
        },
        "hints": {
            "concept": "Majaz Mursal 'Alaqah Sababiyyah menyebutkan sebabnya (hujan/al-ghaits), padahal yang dimaksud adalah akibatnya (rumput/an-nabat).",
            "execution": "Pilih: Sababiyyah (سَبَبِيَّةٌ - menyebut sebab, memaksudkan akibat)."
        }
    },
    {
        "id": "arb-sim-11",
        "materi": "BALAGHAH: ILMU BADI' (AL-MUQABALAH)",
        "topic": "Konsep Gaya Bahasa Muqabalah (Penyandingan Multi-Antitesis)",
        "stem": "Cermati firman Allah Swt. dalam QS. Al-A'raf ayat 157 berikut:\n'وَيُحِلُّ لَهُمُ الطَّيِّبَاتِ وَيُحَرِّمُ عَلَيْهِمُ الخَبَائِثَ'\n(Dan Dia menghalalkan bagi mereka segala yang baik dan mengharamkan atas mereka segala yang buruk).\nPada penggalan ayat di atas disandingkan kata 'يُحِلُّ' lawan dari 'يُحَرِّمُ', 'لَهُمْ' lawan dari 'عَلَيْهِمْ', dan 'الطَّيِّبَاتِ' lawan dari 'الخَبَائِثَ' secara berurutan dan teratur. Gaya bahasa retorika badi' ini dinamakan...",
        "correct": "Muqabalah (مُقَابَلَةٌ - mendatangkan dua makna atau lebih, kemudian mendatangkan lawan-lawan maknanya secara tertib/sejajar).",
        "distractors": [
            "Thibaq Ijab semata (karena hanya melibatkan satu pasang kata berlawanan saja).",
            "Jinas Isytiqaq (penggabungan akar kata yang serupa secara fonetis).",
            "Iltifat (peralihan gaya tutur kata dari orang ketiga ke orang pertama).",
            "Tauriyah (penggunaan kata yang memiliki makna dekat dan makna jauh yang tersembunyi)."
        ],
        "formula": {
            "title": "STRUKTUR GAYA BAHASA MUQABALAH",
            "latex": "\\begin{pmatrix} \\text{يُحِلُّ} & \\text{لَهُمْ} & \\text{الطَّيِّبَاتِ} \\end{pmatrix} \\iff \\begin{pmatrix} \\mathbf{\\text{يُحَرِّمُ}} & \\mathbf{\\text{عَلَيْهِمْ}} & \\mathbf{\\text{الخَبَائِثَ}} \\end{pmatrix} \\implies \\mathbf{\\text{Muqabalah (3 Lawan 3 Sejajar)}}",
            "legend": "• Perbedaan mendasar: Thibaq terjadi pada 1 pasang kata, Muqabalah terjadi pada $\\ge 2$ pasang kata sejajar"
        },
        "hints": {
            "concept": "Muqabalah adalah mempertemukan dua kata/makna atau lebih lalu mendatangkan lawan-lawannya secara berurutan/sejajar.",
            "execution": "Pilih: Muqabalah (مُقَابَلَةٌ)."
        }
    },
    {
        "id": "arb-sim-12",
        "materi": "SHOROF & MORFOLOGI: FI'IL SHAHIH",
        "topic": "Klasifikasi Tiga Varian Fi'il Shahih (Salim, Mahmuz, Mudha'af)",
        "stem": "Dalam ilmu shorof, fi'il shahih (kata kerja yang huruf aslinya bebas dari huruf 'illat alif, wawu, dan ya') dibedakan menjadi tiga kelompok: Salim, Mahmuz, dan Mudha'af. Pasangan kata kerja berikut yang KETIGA-TIGANYA tergolong Fi'il Shahih Salim (bebas dari hamzah dan bebas dari tasydid ganda) adalah...",
        "correct": "كَتَبَ، جَلَسَ، فَتَحَ (semuanya fi'il shahih salim tanpa hamzah dan tanpa huruf ganda).",
        "distractors": [
            "أَكَلَ، سَأَلَ، قَرَأَ (ketiganya adalah fi'il shahih mahmuz karena mengandung huruf hamzah).",
            "مَدَّ، شَدَّ، عَدَّ (ketiganya adalah fi'il shahih mudha'af karena memiliki huruf kedua dan ketiga kembar).",
            "وَجَدَ، قَالَ، رَمَى (ketiganya adalah fi'il mu'tal yang mengandung huruf 'illat).",
            "أَمَرَ، فَرَّ، نَصَرَ (campuran antara mahmuz, mudha'af, dan salim)."
        ],
        "formula": {
            "title": "TAKSONOMI FI'IL SHAHIH",
            "latex": "\\text{Fi'il Shahih} = \\begin{cases} \\mathbf{\\text{1. Saalim:}} & \\mathbf{\\text{Bebas Hamzah \\& Bebas Tadh'if (كَتَبَ، جَلَسَ)}} \\\\ \\text{2. Mahmuuz:} & \\text{Ada Hamzah (أَكَلَ، سَأَلَ، قَرَأَ)} \\\\ \\text{3. Mudha''af:} & \\text{'Ain \\& Lam Kembar Tasydid (مَدَّ، رَدَّ)} \\end{cases}",
            "legend": "• Memahami peta pembagian fi'il shahih adalah kompetensi dasar shorof analitis"
        },
        "hints": {
            "concept": "Fi'il Shahih Salim adalah fi'il shahih yang huruf aslinya selamat/bebas dari huruf hamzah dan tasydid kembar (seperti kataba, jalasa, fataha).",
            "execution": "Pilih: 'كَتَبَ، جَلَسَ، فَتَحَ'."
        }
    },
    {
        "id": "arb-sim-13",
        "materi": "SHOROF & MORFOLOGI: FI'IL LAFIF",
        "topic": "Perbedaan Fi'il Lafif Mafruq (وَقَى) dan Lafif Maqrun (رَوَى)",
        "stem": "Fi'il yang memiliki dua huruf 'illat di dalam akar katanya dinamakan Fi'il Lafif. Kata kerja 'وَقَى' (memelihara/menjaga) memiliki huruf 'illat pada huruf pertama (wawu) dan huruf ketiga (ya'), yang dipisahkan oleh huruf shahih qaf di tengahnya. Berdasarkan kaidah morfologi, 'وَقَى' diklasifikasikan sebagai...",
        "correct": "Fi'il Lafif Mafruq (لَفِيفٌ مَفْرُوقٌ - fi'il yang kedua huruf 'illat-nya terpisah oleh huruf shahih).",
        "distractors": [
            "Fi'il Lafif Maqrun (لَفِيفٌ مَقْرُونٌ - fi'il yang kedua huruf 'illat-nya berdampingan bersambung seperti rawaa dan hawaa).",
            "Fi'il Mu'tal Mithal (fi'il yang hanya huruf pertamanya saja berupa huruf 'illat).",
            "Fi'il Mu'tal Ajwaf (fi'il yang hanya huruf tengahnya saja berupa huruf 'illat).",
            "Fi'il Mu'tal Naqish (fi'il yang hanya huruf ujung akhirnya saja berupa huruf 'illat)."
        ],
        "formula": {
            "title": "DIKOTOMI FI'IL LAFIF (MAFRUQ VS MAQRUN)",
            "latex": "\\text{Fi'il Lafif (2 Huruf 'Illat)} = \\begin{cases} \\mathbf{\\text{Lafif Mafruq:}} & \\mathbf{\\text{Terpisah huruf shahih (وَقَى: Wawu } \\dots \\text{ Yaa')}} \\\\ \\text{Lafif Maqrun:} & \\text{Berdampingan gandeng (رَوَى: Wawu + Yaa')} \\end{cases}",
            "legend": "• Mafruq = berjarak/terpisah; Maqrun = beriringan/bergandengan"
        },
        "hints": {
            "concept": "Dua huruf 'illat yang terpisah oleh huruf shahih (seperti wa-qa-ya) dinamakan Lafif Mafruq (terpisah).",
            "execution": "Pilih: Fi'il Lafif Mafruq (لَفِيفٌ مَفْرُوقٌ)."
        }
    },
    {
        "id": "arb-sim-14",
        "materi": "TATA BAHASA NAHWU: ISIM TAFDHIL MA'RIFAH",
        "topic": "Kaidah Kesesuaian Gender dan Bilangan pada Isim Tafdhil Ber-Alif Lam",
        "stem": "Ketika isim tafdhil (wazan af'alu) digabungkan dengan alif lam ma'rifah (*mu'arraf bi AL*), kaidah nahwu mewajibkan isim tafdhil tersebut menyesuaikan diri (*mutabaqah*) secara penuh dengan benda yang disifatinya dalam hal jenis kelamin (mudzakkar/mu'annats) dan bilangan (mufrad/mutsanna/jama'). Bentuk kalimat yang BENAR untuk menyatakan 'Fathimah adalah siswi terbaik di kelas' adalah...",
        "correct": "فَاطِمَةُ هِيَ الطَّالِبَةُ الفُضْلَى فِي الفَصْلِ (al-fudhlaa adalah bentuk mufrad mu'annats dari wazan af'alu yang wajib selaras dengan Faathimah).",
        "distractors": [
            "فَاطِمَةُ هِيَ الطَّالِبَةُ الأَفْضَلُ فِي الفَصْلِ (salah karena al-afdhala berbentuk mudzakkar saat ber-alif lam).",
            "فَاطِمَةُ هِيَ الطَّالِبَةُ الفَاضِلَةُ مِنْ غَيْرِ تَفْضِيلٍ (tidak membentuk isim tafdhil superlatif).",
            "فَاطِمَةُ هِيَ الطَّالِبَةُ الفُضْلَيَاتُ فِي الفَصْلِ (menggunakan bentuk jamak untuk subjek tunggal).",
            "فَاطِمَةُ هِيَ الطَّالِبَةُ الأَفْضَلُونَ فِي الفَصْلِ (menggunakan jamak mudzakkar salim yang menyalahi kaidah)."
        ],
        "formula": {
            "title": "MUTABAQAH ISIM TAFDHIL BER-ALIF LAM",
            "latex": "\\text{فَاطِمَةُ (Mufrad Mu'annats)} \\implies \\mathbf{\\text{Isim Tafdhil Ber-Al: الفُضْلَى (Wazan فُعْلَى)}}",
            "legend": "• Pasangan wazan tafdhil ma'rifah: Mudzakkar = الأَفْعَلُ, Mu'annats = الفُعْلَى"
        },
        "hints": {
            "concept": "Isim tafdhil yang ber-Alif Lam wajib menyamai yang disifati. Untuk perempuan tunggal (Fathimah), wazan mu'annats-nya adalah فُعْلَى: 'الفُضْلَى'.",
            "execution": "Pilih: 'فَاطِمَةُ هِيَ الطَّالِبَةُ الفُضْلَى'."
        }
    },
    {
        "id": "arb-sim-15",
        "materi": "TATA BAHASA NAHWU: AN-NAWASIB",
        "topic": "Pengaruh Lamul Juhud (لَامُ الجُحُودِ) Menashabkan Fi'il Mudhari'",
        "stem": "Cermati firman Allah Swt. dalam QS. Al-Anfal ayat 33 berikut:\n'وَمَا كَانَ اللهُ لِيُعَذِّبَهُمْ وَأَنْتَ فِيهِمْ'\n(Dan Allah sekali-kali tidak akan mengazab mereka, sedangkan engkau [Muhammad] berada di antara mereka).\nHarakat akhir fi'il mudhari' 'لِيُعَذِّبَهُمْ' berstatus manshub bil-fathah karena didahului oleh huruf lam istimewa yang dinamakan...",
        "correct": "Laamul Juhud (لَامُ الجُحُودِ - lam penegasan penolakan mutlak yang jatuh setelah kaana manfiyyah 'مَا كَانَ' dan menashabkan fi'il mudhari' dengan perantara an mudhmarah wujuuban).",
        "distractors": [
            "Laamut Ta'lil (lam yang semata-mata menerangkan sebab alasan terjadinya pekerjaan).",
            "Laamul Amr (lam perintah yang bertugas menjazmkan fi'il mudhari' dengan harakat sukun).",
            "Laamul Ibtida' (lam penegas yang berada di awal mubtada' tanpa merusak harakat rofa').",
            "Laamul Qasam (lam penjelas sumpah yang mewajibkan fi'il bersambung dengan nun taukid)."
        ],
        "formula": {
            "title": "IDENTIFIKASI LAAMUL JUHUD (لَامُ الجُحُودِ)",
            "latex": "\\mathbf{\\text{Kaana Manfiyyah (مَا كَانَ / لَمْ يَكُنْ)}} + \\mathbf{\\text{لَامُ الجُحُودِ (لِـ)}} \\implies \\mathbf{\\text{Fi'il Mudhari' Manshub (لِيُعَذِّبَ)}}",
            "legend": "• Ciri khas laamul juhud: selalu didahului oleh konstelasi kata 'Maa Kaana' atau 'Lam Yakun'"
        },
        "hints": {
            "concept": "Huruf lam yang jatuh setelah kata 'Maa Kaana' (penafian masa lampau) disebut Laamul Juhud (لَامُ الجُحُودِ) dan berfungsi menashabkan fi'il mudhari'.",
            "execution": "Pilih: Laamul Juhud (لَامُ الجُحُودِ)."
        }
    },
    {
        "id": "arb-sim-16",
        "materi": "TATA BAHASA NAHWU: AN-NAWASIB",
        "topic": "Kaidah Hatta Gha'iyyah Penashab Fi'il Mudhari'",
        "stem": "Perhatikan kalimat berikut:\n'وَاصِلْ جُهُودَكَ الدِّرَاسِيَّةَ حَتَّى ... هَدَفَكَ المَنْشُودَ.'\n(Lanjutkanlah ikhtiar belajarmu sampai kamu ... tujuan yang engkau dambakan).\nBentuk fi'il mudhari' yang TEPAT dan manshub setelah partikel tujuan 'حَتَّى' al-gha'iyyah adalah...",
        "correct": "تَبْلُغَ (tablugha - fi'il mudhari' manshub bil-fathah setelah hatta gha'iyyah yang bermakna 'ilaa an').",
        "distractors": [
            "تَبْلُغُ (tablughu - marfu' dengan dhommah yang mengabaikan fungsi amil nashab pada hatta).",
            "تَبْلُغْ (tablugh - majzum dengan sukun yang keliru karena hatta bukan huruf jazm).",
            "تَبْلُغُونَ (tablughuuna - marfu' dengan tsubutun nun yang tidak sesuai subjek tunggal anta).",
            "بَلَغْتَ (balaghta - bentuk fi'il madhi yang tidak selaras dengan partikel masa depan hatta)."
        ],
        "formula": {
            "title": "I'RAB FI'IL MUDHARI' SETELAH HATTA",
            "latex": "\\text{حَتَّى (Gha'iyyah: إِلى أَنْ)} + \\mathbf{\\text{Fi'il Mudhari' Manshub (تَبْلُغَ - Manshub bi 'An' Mudhmarah)}}",
            "legend": "• Syarat nashab fi'il setelah hatta: perbuatan tersebut berorientasi pada masa yang akan datang (istiqbal)"
        },
        "hints": {
            "concept": "Kata 'حَتَّى' yang bermakna hingga/sampai (gha'iyyah) menashabkan fi'il mudhari' dengan harakat fathah: 'تَبْلُغَ'.",
            "execution": "Pilih: 'تَبْلُغَ' (tablugha)."
        }
    },
    {
        "id": "arb-sim-17",
        "materi": "FAHM AL-MAQRU': SEJARAH SAINS ISLAM",
        "topic": "Instrumen Astronomi Islam Astrolabe (الأُسْطُرْلَابُ) dan Fungsinya",
        "stem": "Bacalah teks wacana sejarah astronomi peradaban Islam berikut:\n'ابْتَكَرَ عُلَمَاءُ الفَلَكِ المُسْلِمُونَ فِي العَصْرِ العَبَّاسِيِّ آلَةَ 'الأُسْطُرْلَابِ' وَطَوَّرُوهَا بِدِقَّةٍ بَالِغَةٍ. وَكَانَتْ هَذِهِ الآلَةُ تُسْتَخْدَمُ لِتَحْدِيدِ مَوَاقِعِ النُّجُومِ، وَحِسَابِ حَرَكَةِ الشَّمْسِ، وَتَحْدِيدِ أَوْقَاتِ الصَّلَوَاتِ الخَمْسِ، ف hisab فضلاً عَنْ تَعْيِينِ اتِّجَاهِ القِبْلَةِ لِلْمُسَافِرِينَ فِي الصَّحْرَاءِ وَالبِحَارِ.'\nBerdasarkan wacana di atas, fungsi praktis religius dan navigasi dari penemuan astrolabe oleh para ilmuwan muslim adalah...",
        "correct": "Menentukan arah kiblat bagi musafir di gurun dan lautan serta menghitung waktu pelaksanaan sholat lima waktu secara akurat melalui pengamatan posisi bintang.",
        "distractors": [
            "Memprediksi masa depan ramalan nasib kekayaan seseorang berdasarkan tanggal kelahiran di kalender romawi.",
            "Menggali sumur minyak bumi bawah tanah dengan bantuan medan magnet buatan manusia.",
            "Mendeteksi kebocoran lambung kapal uap niaga dari serangan peluru meriam musuh.",
            "Mengirimkan pesan sandi telegraf nirkabel antarkerajaan di sepanjang pesisir Laut Kaspia."
        ],
        "formula": {
            "title": "ANALISIS FUNGSI INSTRUMEN ASTRONOMI ISLAM",
            "latex": "\\text{الأُسْطُرْلَابُ (Astrolabe)} \\implies \\begin{cases} \\mathbf{\\text{Fungsi Fikih:}} & \\mathbf{\\text{Waktu Sholat \\& Arah Kiblat}} \\\\ \\mathbf{\\text{Fungsi Sains:}} & \\mathbf{\\text{Posisi Bintang, Gerak Matahari, Navigasi}} \\end{cases}",
            "legend": "• Menunjukkan integrasi sains empiris astronomi dengan kebutuhan ritual ibadah syariat"
        },
        "hints": {
            "concept": "Teks menyatakan astrolabe digunakan untuk: 'تَحْدِيدِ أَوْقَاتِ الصَّلَوَاتِ الخَمْسِ ... وَتَعْيِينِ اتِّجَاهِ القِبْلَةِ لِلْمُسَافِرِينَ' (menentukan waktu sholat dan arah kiblat musafir).",
            "execution": "Pilih: Menentukan arah kiblat dan menghitung waktu sholat lima waktu melalui posisi bintang."
        }
    },
    {
        "id": "arb-sim-18",
        "materi": "FAHM AL-MAQRU': HISTORIOGRAFI INDONESIA",
        "topic": "Catatan Pelayaran Haji Nusantara Abad ke-19 dengan Kapal Uap",
        "stem": "Cermati teks sejarah sosial keagamaan berikut:\n'شَهِدَ النِّصْفُ الثَّانِي مِنَ القَرْنِ التَّاسِعَ عَشَرَ المِيلَادِيِّ تَحَوُّلًا كَبِيرًا فِي رِحْلَةِ الحَجِّ لِأَهْلِ إِنْدُونِيسِيَا (أَهْلِ جَاوَى)، حَيْثُ أَدَّى افْتِتَاحُ قَنَاةِ السُّوَيْسِ عَامَ 1869م وَدُخُولُ السُّفُنِ البُخَارِيَّةِ إِلَى اخْتِصَارِ زَمَنِ السَّفَرِ مِنْ عِدَّةِ أَشْهُرٍ إِلَى عِدَّةِ أَسَابِيعَ، مِمَّا زَادَ مِنْ أَعْدَادِ الحُجَّاجِ وَعَمَّقَ التَّوَاصُلَ العِلْمِيَّ مَعَ عُلَمَاءِ الحَرَمَيْنِ الشَّرِيفَيْنِ.'\nFaktor teknologi dan infrastruktur maritim yang merevolusi mobilitas jemaah haji Nusantara pada akhir abad ke-19 menurut teks adalah...",
        "correct": "Pembukaan Terusan Suez dan pengoperasian kapal uap yang memangkas waktu tempuh pelayaran laut dari beberapa bulan menjadi beberapa minggu.",
        "distractors": [
            "Pembangunan jalur rel kereta api super cepat yang menghubungkan kota Surabaya langsung ke kota Makkah.",
            "Penemuan pesawat terbang komersial bermesin jet yang mengangkut jemaah dari Batavia dalam hitungan jam.",
            "Pemberian subsidi tiket gratis tanpa syarat oleh kongsi dagang VOC kepada seluruh santri pesantren pedalaman.",
            "Penutupan seluruh dermaga pelabuhan samudra Hindia oleh armada militer kekaisaran Ottoman."
        ],
        "formula": {
            "title": "FAKTOR SEJARAH PERJALANAN HAJI NUSANTARA",
            "latex": "\\begin{pmatrix} \\text{Terusan Suez (1869)} \\\\ \\text{Kapal Uap (السُّفُن البُخَارِيَّة)} \\end{pmatrix} \\xrightarrow{\\mathbf{\\text{Reduksi Waktu (Bulan } \\to \\text{ Minggu)}}} \\begin{cases} \\mathbf{\\text{Lonjakan Jumlah Haji}} \\\\ \\mathbf{\\text{Intensitas Jaringan Ulama Jawi}} \\end{cases}",
            "legend": "• Menunjukkan hubungan revolusi transportasi industri dengan dinamika keagamaan Nusantara"
        },
        "hints": {
            "concept": "Teks menegaskan faktor kuncinya: 'افْتِتَاحُ قَنَاةِ السُّوَيْسِ عَامَ 1869م وَدُخُولُ السُّفُنِ البُخَارِيَّةِ' (pembukaan Terusan Suez dan kapal uap yang memangkas waktu tempuh).",
            "execution": "Pilih opsi: Pembukaan Terusan Suez dan pengoperasian kapal uap yang memangkas waktu tempuh."
        }
    },
    {
        "id": "arb-sim-19",
        "materi": "FAHM AL-MAQRU': ARSITEKTUR ISLAM NUSANTARA",
        "topic": "Akulturasi Arsitektur Menara Masjid Kudus Jawa Tengah",
        "stem": "Bacalah wacana kebudayaan Islam berikut:\n'يُعَدُّ مَسْجِدُ مَنَارَةِ قُدُس فِي جَاوَى الوُسْطَى نَمُوذَجًا فَرِيدًا لِلِانْدِمَاجِ الثَّقَافِيِّ (الأَكُولْتُرَاسِي) بَيْنَ الحَضَارَةِ الإِسْلَامِيَّةِ وَالتُّرَاثِ الهِنْدُوسِيِّ الجَاوِيِّ القَدِيمِ. بُنِيَتِ المَنَارَةُ بِآجُرٍّ أَحْمَرَ يُشْبِهُ تَصْمِيمَ مَعَابِدِ كَانْدِي الجَاوِيَّةِ، مِمَّا يَعْكِسُ حِكْمَةَ سُنَنْ قُدُس فِي نَشْرِ الدَّعْوَةِ السِّلْمِيَّةِ دُونَ الصِّدَامِ مَعَ التَّقَالِيدِ المَحَلِّيَّةِ.'\nStrategi kultural Sunan Kudus yang tercermin dalam arsitektur Menara Kudus berdasarkan teks di atas adalah...",
        "correct": "Melakukan dakwah persuasif-akomodatif dengan memadukan estetika arsitektur bata merah bercorak candi Hindu ke dalam kompleks masjid demi keharmonisan sosial masyarakat lokal.",
        "distractors": [
            "Menghancurkan seluruh bangunan bersejarah peninggalan kerajaan Majapahit dengan kekuatan pasukan perang.",
            "Mewajibkan seluruh warga kota Kudus memakai jubah putih dan berbicara dalam bahasa Arab pasar setiap hari.",
            "Melarang penggunaan bahan bata merah lokal dalam pembuatan menara dan menggantinya dengan marmer impor Italia.",
            "Menyerahkan pengelolaan masjid agung kepada kantor kamar dagang kolonial Belanda."
        ],
        "formula": {
            "title": "AKULTURASI ARSITEKTUR ISLAM (SUNAN KUDUS)",
            "latex": "\\text{Arsitektur Menara Candi Bata Merah} + \\text{Fungsi Menara Adzan Masjid} \\xrightarrow{\\mathbf{\\text{Dakwah Hikmah Sunan Kudus}}} \\mathbf{\\text{Akomodasi Budaya Harmonis}}",
            "legend": "• Bukti otentik kearifan wali songo dalam mengonversi simbol kultural lokal menjadi media dakwah Islam"
        },
        "hints": {
            "concept": "Teks menerangkan strategi Sunan Kudus: 'حِكْمَةَ سُنَنْ قُدُس فِي نَشْرِ الدَّعْوَةِ السِّلْمِيَّةِ دُونَ الصِّدَامِ' melalui akulturasi menara bata merah mirip candi Jawa.",
            "execution": "Pilih: Dakwah persuasif-akomodatif memadukan arsitektur bata merah candi Hindu ke dalam kompleks masjid."
        }
    },
    {
        "id": "arb-sim-20",
        "materi": "KITABAH & SINTAKSIS: KONJUNGSI WACANA",
        "topic": "Penggunaan Konjungsi Pertentangan 'لَكِنَّ' (Lakinna) dan I'rab Isim-nya",
        "stem": "Perhatikan kalimat bertingkat berikut:\n'الِامْتِحَانُ كَانَ صَعْبًا جِدًّا، ... مُجْتَهِدٌ وَحَصَلَ عَلَى دَرَجَةٍ مُمْتَازَةٍ.'\n(Ujian itu sangat sulit, akan tetapi ... giat belajar dan memperoleh nilai istimewa).\nKonjungsi pertentangan (*istidrak*) beserta isim-nya yang TEPAT secara kaidah nawasikh inna (memanshubkan isim bertanwin fathah) adalah...",
        "correct": "لَكِنَّ زَيْدًا (lakinna Zaidan - lakinna bermakna istidrak dan isim-nya manshub bil-fathah).",
        "distractors": [
            "لَكِنَّ زَيْدٌ (lakinna Zaidun - marfu' dengan dhommah yang keliru setelah amil nawasikh lakinna).",
            "لَكِنَّ زَيْدٍ (lakinna Zaidin - majrur dengan kasrah yang menyalahi kaidah isim lakinna).",
            "لِأَنَّ زَيْدٌ (li'anna zaidun - selain salah harakat dhommah, li'anna berfungsi sebab akibat bukan pertentangan).",
            "بَلْ زَيْدًا (bal zaidan - partikel bal adalah huruf 'athaf biasa yang tidak memanshubkan isim bertanwin tanpa amil)."
        ],
        "formula": {
            "title": "I'RAB AMIL LAKINNA (لَكِنَّ)",
            "latex": "\\text{Klausa 1 (Ujian Sulit)} + \\mathbf{\\text{لَكِنَّ (Istidrak)}} + \\mathbf{\\text{Isim Lakinna Manshub (زَيْدًا)}} + \\text{Khabar Marfu' (مُجْتَهِدٌ)}",
            "legend": "• Lakinna adalah saudara Inna yang berfungsi meralat prasangka awal kalimat (istidrak)"
        },
        "hints": {
            "concept": "Lakinna adalah saudara Inna yang menashabkan isim: 'لَكِنَّ زَيْدًا' (lakinna Zaidan).",
            "execution": "Pilih: 'لَكِنَّ زَيْدًا' (lakinna Zaidan)."
        }
    },
    {
        "id": "arb-sim-21",
        "materi": "TATA BAHASA NAHWU: 'AMAL ISIM FA'IL",
        "topic": "Syarat Isim Fa'il Beramal Menashabkan Maf'ul Bih ('Amalul Fi'li)",
        "stem": "Cermati kalimat berikut:\n'أَنَا ... وَاجِبِي المَدْرَسِيَّ الآنَ فِي غُرْفَةِ المُذَاكَرَةِ.'\n(Saya adalah orang yang sedang menulis tugasku sekarang di ruang belajar).\nBila isim fa'il 'كَاتِبٌ' ingin difungsikan beramal seperti kata kerjanya (yaitu menashabkan 'وَاجِبِي' sebagai maf'ul bih) dengan syarat bertanwin dan menunjukkan waktu sekarang (*hal/istiqbal*), maka bentuk yang TEPAT adalah...",
        "correct": "كَاتِبٌ (kaatibun - isim fa'il bertanwin dhommatain marfu' sebagai khabar dan beramal menashabkan waajibii).",
        "distractors": [
            "كَاتِبُ بِدُونِ تَنْوِينٍ (kaatibu tanpa tanwin yang mengubah konstruksi menjadi susunan idhafah terputus).",
            "كَاتِبًا (kaatiban - berharakat fathatain yang keliru untuk posisi khabar mubtada' ana).",
            "مَكْتُوبٌ (maktuubun - isim maf'ul yang membutuhkan na'ibul fa'il, bukan maf'ul bih).",
            "كِتَابَةً (kitaabatan - bentuk masdar muthlaq yang bukan isim fa'il pemangku pekerjaan)."
        ],
        "formula": {
            "title": "'AMAL ISIM FA'IL (عَمَلُ اسْمِ الفَاعِلِ)",
            "latex": "\\text{Mubtada' (أَنَا)} + \\mathbf{\\text{Isim Fa'il Bertanwin (كَاتِبٌ)}} + \\mathbf{\\text{Maf'ul Bih-nya (وَاجِبِي)}}",
            "legend": "• Isim fa'il nakirah beramal menashabkan objek jika bertanwin dan bermakna saat ini atau masa depan"
        },
        "hints": {
            "concept": "Isim fa'il beramal seperti fi'il-nya (menashabkan maf'ul bih) bila bertanwin dan bersandar pada mubtada': 'أَنَا كَاتِبٌ وَاجِبِي'.",
            "execution": "Pilih: 'كَاتِبٌ' (kaatibun)."
        }
    },
    {
        "id": "arb-sim-22",
        "materi": "TATA BAHASA NAHWU: 'AMAL ISIM MAF'UL",
        "topic": "Kedudukan Na'ibul Fa'il setelah Isim Maf'ul (مَرْفُوعٌ بِالضَّمَّةِ)",
        "stem": "Perhatikan kalimat yang memuat Isim Maf'ul berikut:\n'المَسْجِدُ مَفْتُوحٌ ... لِاسْتِقْبَالِ المُصَلِّينَ لَيْلًا وَنَهَارًا.'\n(Masjid itu dibuka ...nya untuk menyambut jemaah sholat siang dan malam).\nKata yang TEPAT untuk berkedudukan sebagai Na'ibul Fa'il marfu' bil-dhommah dari isim maf'ul 'مَفْتُوحٌ' adalah...",
        "correct": "بَابُهُ (baabuhu - na'ibul fa'il marfu' dengan harakat dhommah bersambung dhamir hu merujuk pada al-masjid).",
        "distractors": [
            "بَابَهُ (baabahu - manshub dengan fathah yang keliru karena isim maf'ul merafa'kan na'ibul fa'il).",
            "بَابِهِ (baabihi - majrur dengan kasrah yang tidak memiliki landasan gramatikal).",
            "أَبْوَابًا (abwaaban - jama' taksir manshub bertanwin yang menyalahi kaidah rafa').",
            "بِالبَابِ (bil-baabi - susunan huruf jar yang membatalkan fungsi na'ibul fa'il murni)."
        ],
        "formula": {
            "title": "'AMAL ISIM MAF'UL (عَمَلُ اسْمِ المَفْعُولِ)",
            "latex": "\\text{Isim Maf'ul (مَفْتُوحٌ)} \\implies \\mathbf{\\text{Na'ibul Fa'il Marfu' (بَابُهُ - Marfu' bil-Dhommah)}}",
            "legend": "• Isim maf'ul diturunkan dari fi'il majhul sehingga menuntut kehadiran na'ibul fa'il marfu'"
        },
        "hints": {
            "concept": "Isim maf'ul (مَفْتُوحٌ) beramal seperti fi'il majhul (yuf-tahu), yaitu merafa'kan Na'ibul Fa'il: 'بَابُهُ' (baabuhu).",
            "execution": "Pilih: 'بَابُهُ' (baabuhu)."
        }
    },
    {
        "id": "arb-sim-23",
        "materi": "TATA BAHASA NAHWU: AS-SHIFAT AL-MUSYABBAHAH",
        "topic": "Karakteristik Shifat Musyabbahah bi Ismil Fa'il (Menunjukkan Sifat Menetap)",
        "stem": "Dalam wacana bahasa Arab, kata sifat 'كَرِيمٌ' (dermawan), 'شُجَاعٌ' (pemberani), dan 'طَاهِرٌ' (suci) diklasifikasikan sebagai *Shifat Musyabbahah bi Ismil Fa'il*. Perbedaan mendasar antara Shifat Musyabbahah dengan Isim Fa'il biasa adalah...",
        "correct": "Shifat Musyabbahah menunjukkan sifat watak yang melekat tetap (tsubut wad-dawam) pada diri pelaku dan dibentuk dari fi'il lazim, sedangkan Isim Fa'il menunjukkan perbuatan insidental yang sedang/akan terjadi dan bisa berubah sewaktu-waktu.",
        "distractors": [
            "Shifat Musyabbahah hanya boleh digunakan untuk benda mati seperti batu dan kayu bakar.",
            "Shifat Musyabbahah wajib selalu berharakat majrur bil-fathah tanpa memedulikan amil kalimat.",
            "Isim Fa'il hanya dibentuk dari kata kerja bahasa Persia kuno yang diserap ke bahasa Arab.",
            "Kedua bentuk kata tersebut tidak memiliki perbedaan sama sekali dan dapat dipertukarkan secara acak."
        ],
        "formula": {
            "title": "DISTINGSI SHIFAT MUSYABBAHAH VS ISIM FA'IL",
            "latex": "\\begin{cases} \\mathbf{\\text{Shifat Musyabbahah (كَرِيمٌ، شُجَاعٌ):}} & \\mathbf{\\text{Sifat Tetap Melekat / Permanen (Tsubuut / Dawam)}} \\\\ \\text{Isim Fa'il (كَاتِبٌ، ضَارِبٌ):} & \\text{Perbuatan Temporer / Insidental (Huduts / Taghayyur)} \\end{cases}",
            "legend": "• Karakter watak bawaan selalu menggunakan shifat musyabbahah (fa'iil, fu'aal, fa'al)"
        },
        "hints": {
            "concept": "Shifat musyabbahah menunjukkan sifat watak yang menetap/permanen (tsubuut wad-dawaam) dari fi'il lazim, berbeda dari isim fa'il yang aksinya temporer.",
            "execution": "Pilih opsi: Menunjukkan sifat watak yang melekat tetap (tsubut wad-dawam) dari fi'il lazim."
        }
    },
    {
        "id": "arb-sim-24",
        "materi": "BALAGHAH: ILMU MA'ANI (USLUB INSYA'I)",
        "topic": "Klasifikasi Kalam Insya'i Ghairu Thalabi (At-Ta'ajjub)",
        "stem": "Cermati ungkapan kekaguman mendalam (*shighatut ta'ajjub*) berikut ini:\n'مَا أَجْمَلَ هَذِهِ الحَدِيقَةَ الغَنَّاءَ!'\n(Alangkah indahnya taman yang rindang nan asri ini!).\nDalam ilmu ma'ani, kalimat ta'ajjub di atas dikelompokkan ke dalam kategori...",
        "correct": "Kalam Insya'i Ghairu Thalabi (كَلَامٌ إِنْشَائِيٌّ غَيْرُ طَلَبِيٍّ - gaya tutur yang tidak menuntut terjadinya sesuatu dari lawan bicara, melainkan mengekspresikan ketakjuban emosional).",
        "distractors": [
            "Kalam Insya'i Thalabi (karena dianggap menuntut tukang kebun membersihkan seluruh daun kering).",
            "Kalam Khabari Ibtida'i (karena pendengar sama sekali tidak meragukan keindahan taman).",
            "Kalam Khabari Thalabi (karena pembicara memperkuat kalimat dengan dua huruf taukid).",
            "Uslub Qashr Hakiki (karena membatasi keindahan hanya pada satu taman bunga saja)."
        ],
        "formula": {
            "title": "TAKSONOMI KALAM INSYA'I",
            "latex": "\\text{Kalam Insya'i} = \\begin{cases} \\text{1. Thalabi (Ada Tuntutan):} & \\text{Amr, Nahyi, Istifham, Tamanni, Nida'} \\\\ \\mathbf{\\text{2. Ghairu Thalabi (Tanpa Tuntutan):}} & \\mathbf{\\text{Ta'ajjub (مَا أَجْمَلَ!), Qasam, Madh, Dzam, 'Uqud}} \\end{cases}",
            "legend": "• Ta'ajjub adalah luapan emosi jiwa apresiatif tanpa menuntut respons aksi dari mukhatab"
        },
        "hints": {
            "concept": "Kalimat ta'ajjub (مَا أَفْعَلَ!) tergolong ke dalam Kalam Insya'i Ghairu Thalabi (tidak menuntut respon tindakan, hanya luapan kekaguman).",
            "execution": "Pilih: Kalam Insya'i Ghairu Thalabi (كَلَامٌ إِنْشَائِيٌّ غَيْرُ طَلَبِيٍّ)."
        }
    },
    {
        "id": "arb-sim-25",
        "materi": "FAHM AL-MAQRU': INTEGRASI SAINS & ISLAM",
        "topic": "Wacana Filosofis Harmoni antara Akal Pikiran dan Wahyu Ilahi",
        "stem": "Bacalah teks telaah pemikiran filsafat Islam berikut:\n'أَكَّدَ فَلَاسِفَةُ الإِسْلَامِ مِثْلُ ابْنِ رُشْدٍ (أَفِيرُوس) أَنَّهُ لَا تَعَارُضَ عَلَى الإِطْلَاقِ بَيْنَ العَقْلِ الصَّرِيحِ وَالنَّقْلِ الصَّحِيحِ. فَالشَّرِيعَةُ الإِسْلَامِيَّةُ تَحُثُّ عَلَى النَّظَرِ العَقْلِيِّ وَالتَّأَمُّلِ فِي مَلَكُوتِ السَّمَاوَاتِ وَالأَرْضِ، وَالعِلْمُ النَّافِعُ يَقُودُ الإِنْسَانَ إِلَى مَعْرِفَةِ الخَالِقِ سُبْحَانَهُ وَتَعَالَى وَعِمَارَةِ الأَرْضِ بِالعَدْلِ وَالإِحْسَانِ.'\nKesimpulan filosofis yang menjadi inti pokok argumentasi Ibnu Rusyd dalam teks di atas adalah...",
        "correct": "Tidak ada pertentangan hakiki antara akal murni (filsafat/sains) dan wahyu yang sahih (agama), karena keduanya sama-sama bersumber dari kebenaran mutlak yang saling melengkapi.",
        "distractors": [
            "Filsafat akal wajib dilarang secara total karena pasti merusak kemurnian akidah umat beragama.",
            "Teks wahyu suci hanya boleh dibaca oleh para astronom yang menguasai ilmu perhitungan gerhana matahari.",
            "Akal manusia memiliki kedudukan lebih tinggi daripada kitab suci sehingga wahyu boleh dihapus sesuka hati.",
            "Seluruh karya sains klasik wajib dibakar demi menjaga stabilitas kekuasaan dinasti penguasa."
        ],
        "formula": {
            "title": "SINTESIS IBNU RUSYD (فَصْلُ المَقَالِ)",
            "latex": "\\mathbf{\\text{العَقْلُ الصَّرِيحُ (Akal Murni/Sains)}} \\iff \\mathbf{\\text{النَّقْلُ الصَّحِيحُ (Wahyu Sahih/Agama)}} \\implies \\mathbf{\\text{Harmoni Tanpa Kontradiksi}}",
            "legend": "• 'Al-Haqqu la yudhaddu al-haqqa' (Kebenaran sejati tidak akan pernah bertentangan dengan kebenaran)"
        },
        "hints": {
            "concept": "Teks menegaskan pandangan Ibnu Rusyd: 'لَا تَعَارُضَ عَلَى الإِطْلَاقِ بَيْنَ العَقْلِ الصَّرِيحِ وَالنَّقْلِ الصَّحِيحِ' (tidak ada pertentangan antara akal murni dan wahyu sahih).",
            "execution": "Pilih opsi: Tidak ada pertentangan hakiki antara akal murni (sains) dan wahyu sahih (agama)."
        }
    },

    # -------------------------------------------------------------
    # 5 MULTI-SELECT ITEMS (arb-sim-26 .. arb-sim-30)
    # -------------------------------------------------------------
    {
        "id": "arb-sim-26",
        "materi": "TATA BAHASA NAHWU: I'RAB ISIM",
        "topic": "Tanda-Tanda I'rab Khusus pada Isim Mutsanna dan Jama' Mudzakkar Salim",
        "stem": "Dalam ilmu nahwu, isim mutsanna (dua) dan jama' mudzakkar salim memiliki tanda I'rab menggunakan huruf (*I'rab bil-huruf*). Manakah pernyataan berikut yang TEPAT mengenai kaidah I'rab kedua bentuk isim tersebut? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Isim mutsanna bertanda I'rab rafa' dengan huruf Alif (ـانِ) seperti pada kata 'المُعَلِّمَانِ'."},
            {"key": "B", "text": "Isim mutsanna bertanda I'rab nashab dan jar dengan huruf Ya' sukun didahului fathah (ـيْنِ) seperti pada kata 'المُعَلِّمَيْنِ'."},
            {"key": "C", "text": "Jama' mudzakkar salim bertanda I'rab rafa' dengan huruf Wawu (ـونَ) dan bertanda nashab/jar dengan huruf Ya' (ـينَ)."},
            {"key": "D", "text": "Jama' mudzakkar salim bertanda I'rab rafa' dengan harakat dhommah zhahirah dan bertanda nashab dengan harakat kasrah."},
            {"key": "E", "text": "Isim mutsanna dan jama' mudzakkar salim wajib selalu berstatus mabni di atas sukun dalam semua posisi kalimat."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "I'RAB BIL-HURUF (MUTSANNA & JAMA' MUDZAKKAR)",
            "latex": "\\begin{aligned} \\text{Mutsanna: } & \\text{Rafa' = Alif (انِ), Nashab/Jar = Yaa' (يْنِ)} \\\\ \\text{Jama' Mudzakkar: } & \\text{Rafa' = Wawu (ونَ), Nashab/Jar = Yaa' (ينَ)} \\end{aligned}",
            "legend": "• Keduanya menggunakan huruf sebagai pengganti harakat pokok dhommah, fathah, kasrah"
        },
        "hints": {
            "concept": "Mutsanna: rafa' alif, nashab/jar ya'. Jama' mudzakkar salim: rafa' wawu, nashab/jar ya'.",
            "execution": "Pilih A, B, dan C. Tolak D (itu kaidah jama' mu'annats) dan E (bukan isim mabni)."
        }
    },
    {
        "id": "arb-sim-27",
        "materi": "TATA BAHASA NAHWU: NAWASIKH KAANA",
        "topic": "Anggota Saudara Kaana (أَخَوَاتُ كَانَ) dan Karakteristik Amalnya",
        "stem": "Amil nawasikh *Kaana wa Akhwatuha* masuk ke dalam Jumlah Ismiyyah untuk merafa'kan isim dan memanshubkan khabar. Manakah di antara kata-kata berikut yang merupakan anggota sah dari saudara-saudara Kaana? (Pilihlah EMPAT jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "أَصْبَحَ (ashbaha - memasuki waktu pagi hari / menjadi)."},
            {"key": "B", "text": "صَارَ (shaara - menunjukkan perubahan wujud atau keadaan)."},
            {"key": "C", "text": "لَيْسَ (laisa - menunjukkan peniadaan atau negasi kabar)."},
            {"key": "D", "text": "ظَلَّ (zhalla - menunjukkan keberlangsungan di waktu siang hari)."},
            {"key": "E", "text": "إِنَّ (inna - amil taukid penashab isim dan perafa' khabar)."}
        ],
        "correctKeys": ["A", "B", "C", "D"],
        "formula": {
            "title": "ANGGOTA SAUDARA KAANA (أَخَوَاتُ كَانَ)",
            "latex": "\\text{Akhawaatu Kaana} = \\{ \\mathbf{\\text{كَانَ، أَصْبَحَ، أَضْحَى، ظَلَّ، أَمْسَى، بَاتَ، صَارَ، لَيْسَ}} \\}",
            "legend": "• Seluruh anggotanya merafa'kan isim dan memanshubkan khabar (Tarfa'ul isma wa tanshibul khabar)"
        },
        "hints": {
            "concept": "Saudara-saudara Kaana meliputi: Kaana, Ashbaha, Adh-ha, Zhalla, Amsa, Baata, Shaara, Laisa, dll. Huruf 'Inna' adalah nawasikh tersendiri yang beramal kebalikannya.",
            "execution": "Pilih A, B, C, D (Ashbaha, Shaara, Laisa, Zhalla). Tolak E (Inna)."
        }
    },
    {
        "id": "arb-sim-28",
        "materi": "SHOROF & MORFOLOGI: FI'IL SHAHIH",
        "topic": "Karakteristik Tiga Pembagian Fi'il Shahih",
        "stem": "Fi'il shahih adalah kata kerja yang huruf-huruf aslinya terbebas dari huruf 'illat. Manakah pernyataan berikut yang BENAR mengenai pembagian fi'il shahih dalam ilmu shorof? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Fi'il Salim adalah fi'il shahih yang huruf aslinya bersih dari huruf hamzah dan bersih dari tasydid (seperti: عَلِمَ، كَتَبَ)."},
            {"key": "B", "text": "Fi'il Mahmuz adalah fi'il shahih yang salah satu huruf aslinya berupa huruf hamzah (seperti: أَخَذَ، سَأَلَ، قَرَأَ)."},
            {"key": "C", "text": "Fi'il Mudha'af Tsulatsi adalah fi'il yang huruf 'ain dan lam fi'il-nya sejenis dan disatukan dengan tasydid (seperti: مَدَّ، فَرَّ)."},
            {"key": "D", "text": "Fi'il Ajwaf adalah fi'il shahih yang huruf tengahnya berupa huruf hamzah qatha' berharakat fathah."},
            {"key": "E", "text": "Fi'il Salim wajib selalu memiliki huruf 'illat alif layyinah di bagian akhir katanya."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "TRIAS FI'IL SHAHIH",
            "latex": "\\text{Fi'il Shahih} \\implies \\begin{cases} \\mathbf{\\text{Salim:}} & \\text{Bebas hamzah \\& tasydid (عَلِمَ)} \\\\ \\mathbf{\\text{Mahmuz:}} & \\text{Memuat hamzah (أَخَذَ)} \\\\ \\mathbf{\\text{Mudha'af:}} & \\text{Dua huruf kembar tasydid (مَدَّ)} \\end{cases}",
            "legend": "• Ketiadaan huruf 'illat (alif, wawu, ya') menjadikannya stabil dalam konjugasi dasar"
        },
        "hints": {
            "concept": "Tiga pembagian fi'il shahih: Salim (bebas hamzah & tasydid), Mahmuz (ada hamzah), Mudha'af (huruf kembar bertasydid). Ajwaf adalah fi'il mu'tal, bukan shahih.",
            "execution": "Pilih A, B, dan C. Tolak D (Ajwaf adalah mu'tal) dan E (Salim tidak punya huruf 'illat)."
        }
    },
    {
        "id": "arb-sim-29",
        "materi": "TATA BAHASA NAHWU: ADWATUL ISTITSNA'",
        "topic": "Rukun-Rukun Kalimat Pengecualian (Arkanul Istitsna')",
        "stem": "Dalam menyusun kalimat pengecualian (*kalamul istitsna'*), terdapat rukun-rukun pokok yang membangun keutuhan struktur kalimat. Manakah di antara komponen berikut yang merupakan rukun resmi dalam bab istitsna'? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Mustatsna Minhu (مُسْتَثْنَى مِنْهُ - kelompok himpunan umum yang dikeluarkan darinya sebagian anggota)."},
            {"key": "B", "text": "Adatut Istitsna' (أَدَاةُ الِاسْتِثْنَاءِ - peranti pengecualian seperti إِلَّا، غَيْرَ، سِوَى، خَلَا)."},
            {"key": "C", "text": "Al-Mustatsna (المُسْتَثْنَى - kata yang terletak setelah adat istitsna' yang menjadi objek pengecualian)."},
            {"key": "D", "text": "Shahibul Hal (kata benda ma'rifah yang diterangkan keadaannya oleh kata sifat)."},
            {"key": "E", "text": "Mubdal Minhu (kata yang digantikan posisinya secara mutlak oleh kata badal)."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "RUKUN KALIMAT ISTITSNA'",
            "latex": "\\mathbf{\\text{Mustatsna Minhu (الحُضُورُ)}} + \\mathbf{\\text{Adat Istitsna' (إِلَّا)}} + \\mathbf{\\text{Mustatsna (عَلِيًّا)}}",
            "legend": "• Menunjukkan struktur logika himpunan (A - B) dalam sintaksis tata bahasa Arab"
        },
        "hints": {
            "concept": "Tiga rukun istitsna': Mustatsna Minhu (himpunan umum), Adat Istitsna' (kata peranti seperti illaa), dan Mustatsna (yang dikecualikan).",
            "execution": "Pilih A, B, dan C. Tolak D (bab Hal) dan E (bab Badal)."
        }
    },
    {
        "id": "arb-sim-30",
        "materi": "BALAGHAH: ILMU BAYAN (AT-TASYBIH)",
        "topic": "Empat Rukun Tasybih Lengkap dalam Ilmu Bayan",
        "stem": "Ilmu Bayan menetapkan bahwa tasybih (penyerupaan estetis) tersusun atas rukun-rukun tertentu. Manakah di antara unsur-unsur berikut yang merupakan rukun pokok dari At-Tasybih? (Pilihlah EMPAT jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Al-Musyabbah (المُشَبَّهُ - entitas pokok yang hendak diserupakan)."},
            {"key": "B", "text": "Al-Musyabbah Bih (المُشَبَّهُ بِهِ - entitas pembanding yang memiliki sifat lebih kuat)."},
            {"key": "C", "text": "Adatut Tasybih (أَدَاةُ التَّشْبِيهِ - kata peranti pembanding seperti huruf kaf atau lafadz ka'anna)."},
            {"key": "D", "text": "Wajhusy Syabah (وَجْهُ الشَّبَهِ - sifat keserupaan yang mempertemukan musyabbah dan musyabbah bih)."},
            {"key": "E", "text": "Al-Makhshush bil-Madh (subjek khusus yang menerima kalimat pujian ni'ma)."}
        ],
        "correctKeys": ["A", "B", "C", "D"],
        "formula": {
            "title": "EMPAT RUKUN TASYBIH (أَرْكَانُ التَّشْبِيهِ)",
            "latex": "\\mathbf{\\text{1. Musyabbah}} + \\mathbf{\\text{2. Adat Tasybih}} + \\mathbf{\\text{3. Musyabbah Bih}} + \\mathbf{\\text{4. Wajhusy Syabah}}",
            "legend": "• Contoh utuh: 'عَلِيٌّ كَالأَسَدِ فِي الشَّجَاعَةِ' (Ali seperti singa dalam hal keberanian)"
        },
        "hints": {
            "concept": "Empat rukun tasybih: Musyabbah, Musyabbah Bih, Adat Tasybih, dan Wajhusy Syabah.",
            "execution": "Pilih A, B, C, D. Tolak E (bab Nahwu madh wadz-dzam)."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH ITEMS (arb-sim-31 .. arb-sim-35)
    # -------------------------------------------------------------
    {
        "id": "arb-sim-31",
        "materi": "TATA BAHASA NAHWU: MANSYUBATUL ASMA'",
        "topic": "Evaluasi Hukum I'rab Isim-Isim Manshub",
        "stem": "Berikut disajikan pernyataan mengenai kaidah I'rab kelompok Isim Manshub (*Manshubatul Asma'*) dalam tata bahasa Arab. Tentukan apakah masing-masing pernyataan BENAR atau SALAH!",
        "statements": [
            {
                "text": "Maf'ul Bih adalah isim manshub yang berfungsi sebagai objek penderita yang dikenai perbuatan oleh fa'il.",
                "correct": "Benar"
            },
            {
                "text": "Maf'ul Liajlih adalah kata kerja fi'il madhi yang diubah harakatnya menjadi kasrah untuk menunjukkan tempat.",
                "correct": "Salah"
            },
            {
                "text": "Haal Mufradah wajib berupa isim nakirah manshubah yang menerangkan keadaan shahibul hal saat peristiwa berlangsung.",
                "correct": "Benar"
            },
            {
                "text": "Isim Inna berstatus I'rab marfu' bil-dhommah, sedangkan Khabar Inna berstatus manshub bil-fathah.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI MANSYUBATUL ASMA'",
            "latex": "\\begin{aligned} \\text{Maf'ul Bih: } & \\text{Benar (Objek penderita perbuatan, Manshub)} \\\\ \\text{Maf'ul Liajlih: } & \\text{Salah (Masdar qolbi manshub alasan perbuatan, bukan fi'il)} \\\\ \\text{Haal Mufradah: } & \\text{Benar (Nakirah, manshub, menerangkan shahibul hal)} \\\\ \\text{Inna: } & \\text{Salah (Inna menashabkan isim dan merafa'kan khabar)} \\end{aligned}",
            "legend": "• Menunjukkan ketepatan penguasaan rumpun isim-isim berkategori manshub"
        },
        "hints": {
            "concept": "1=Benar (Maf'ul bih objek manshub). 2=Salah (Maf'ul liajlih adalah masdar qolbi manshub, bukan fi'il). 3=Benar (Haal nakirah manshubah). 4=Salah (Inna menashabkan isim dan merafa'kan khabar, bukan sebaliknya).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "arb-sim-32",
        "materi": "SHOROF & MORFOLOGI: DERIVASI KATA",
        "topic": "Evaluasi Kaidah Wazan dan Derivasi Morfologi Bahasa Arab",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan terkait derivasi kata dalam ilmu shorof berikut!",
        "statements": [
            {
                "text": "Wazan 'فَاعِلٌ' dari fi'il tsulatsi mujarrad berfungsi membentuk Isim Fa'il penunjuk pelaku tindakan perbuatan.",
                "correct": "Benar"
            },
            {
                "text": "Wazan 'مَفْعُولٌ' dari fi'il tsulatsi mujarrad berfungsi membentuk Isim Maf'ul penunjuk sasaran yang dikenai perbuatan.",
                "correct": "Benar"
            },
            {
                "text": "Penambahan wazan 'أَفْعَلَ' (af'ala) pada fi'il lazim berfungsi menjadikannya fi'il muta'addi yang membutuhkan objek.",
                "correct": "Benar"
            },
            {
                "text": "Isim Alat dibentuk dengan wazan 'مَفْعَلٌ' khusus untuk menunjukkan nama hari dan penanggalan bulan qamariyah.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI WAZAN MORFOLOGI SHOROF",
            "latex": "\\begin{aligned} \\text{فَاعِلٌ: } & \\text{Benar (Isim Fa'il: Pelaku)} \\\\ \\text{مَفْعُولٌ: } & \\text{Benar (Isim Maf'ul: Objek)} \\\\ \\text{أَفْعَلَ: } & \\text{Benar (Ta'diyah / Transitif)} \\\\ \\text{Isim Alat: } & \\text{Salah (Wazan isim alat mifaal/mif'al untuk perkakas, bukan kalender)} \\end{aligned}",
            "legend": "• Menunjukkan penguasaan sistem timbangan morfologi derivasi Arab baku"
        },
        "hints": {
            "concept": "1=Benar (Fa'ilun isim fa'il). 2=Benar (Maf'ulun isim maf'ul). 3=Benar (Af'ala berfaedah ta'diyah). 4=Salah (Isim alat untuk perkakas seperti miftah/miqash, bukan penanggalan).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "arb-sim-33",
        "materi": "BALAGHAH: KETETAPAN ILMU SASTRA",
        "topic": "Evaluasi Kaidah Balaghah (Bayan, Ma'ani, Badi')",
        "stem": "Berikut disajikan pernyataan mengenai konsep-konsep pokok dalam tiga cabang ilmu balaghah. Tentukan apakah masing-masing pernyataan BENAR atau SALAH!",
        "statements": [
            {
                "text": "Ilmu Bayan berfokus pada pengungkapan satu makna dengan berbagai ragam cara penyampaian seperti tasybih dan majaz.",
                "correct": "Benar"
            },
            {
                "text": "Thibaq Ijab adalah gaya bahasa mempertemukan dua kata yang berlawanan di mana salah satunya didahului partikel negasi nafi.",
                "correct": "Salah"
            },
            {
                "text": "Jinas Taam menuntut kesamaan sempurna dua kata dalam 4 kriteria: jenis huruf, jumlah huruf, harakat, dan urutan huruf.",
                "correct": "Benar"
            },
            {
                "text": "Isti'arah pada hakikatnya adalah tasybih yang dibuang salah satu dari dua rukun utamanya (musyabbah atau musyabbah bih).",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "EVALUASI TEORI BALAGHAH TIGA CABANG",
            "latex": "\\begin{aligned} \\text{Ilmu Bayan: } & \\text{Benar (Tasybih, Majaz, Kinayah)} \\\\ \\text{Thibaq Ijab: } & \\text{Salah (Yang didahului partikel nafi adalah Thibaq Salab)} \\\\ \\text{Jinas Taam: } & \\text{Benar (Sama 4 kriteria huruf, beda makna)} \\\\ \\text{Isti'arah: } & \\text{Benar (Tasybih hadzafa ahadu tharafaihi)} \\end{aligned}",
            "legend": "• Memahami pilar-pilar balaghah: Bayan (gaya kiasan), Ma'ani (konteks situasi), Badi' (keindahan)"
        },
        "hints": {
            "concept": "1=Benar (Bayan mengkaji ragam ekspresi tasybih/majaz). 2=Salah (Itu adalah definisi Thibaq Salab, bukan Thibaq Ijab). 3=Benar (Jinas taam sama dalam 4 aspek huruf). 4=Benar (Isti'arah adalah tasybih yang dibuang salah satu tharaf-nya).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Benar."
        }
    },
    {
        "id": "arb-sim-34",
        "materi": "FAHM AL-MAQRU': HISTORIOGRAFI ISLAM",
        "topic": "Evaluasi Fakta Tokoh-Tokoh Keilmuan Peradaban Islam Klasik",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan terkait tokoh ilmuwan besar dalam peradaban Islam berikut!",
        "statements": [
            {
                "text": "Al-Khawarizmi dikenal sebagai Bapak Aljabar dunia yang menulis karya monumental 'Al-Kitab al-Mukhtashar fi Hisab al-Jabr wal-Muqabala'.",
                "correct": "Benar"
            },
            {
                "text": "Ibnu Khaldun menulis karya sosiologi dan filsafat sejarah 'Al-Muqaddimah' yang memperkenalkan teori solidaritas sosial ('ashabiyyah).",
                "correct": "Benar"
            },
            {
                "text": "Ibnu Sina menulis ensiklopedia kedokteran 'Al-Qanun fit-Thibb' yang menjadi rujukan universitas di Eropa selama berabad-abad.",
                "correct": "Benar"
            },
            {
                "text": "Al-Biruni adalah penemu benua Amerika yang berlayar menggunakan kapal uap bermesin diesel pada abad ke-8 Masehi.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI TOKOH ILMUWAN MUSLIM KLASIK",
            "latex": "\\begin{aligned} \\text{Al-Khawarizmi: } & \\text{Benar (Bapak Aljabar, Angka Nol)} \\\\ \\text{Ibnu Khaldun: } & \\text{Benar (Muqaddimah, Sosiologi 'Ashabiyyah)} \\\\ \\text{Ibnu Sina: } & \\text{Benar (Al-Qanun fit-Thibb, Kedokteran)} \\\\ \\text{Al-Biruni: } & \\text{Salah (Al-Biruni ahli geodesi, astronomi, bukan penemu kapal diesel)} \\end{aligned}",
            "legend": "• Menunjukkan wawasan historis mengenai kontribusi peradaban Islam bagi kemajuan sains global"
        },
        "hints": {
            "concept": "1=Benar (Al-Khawarizmi bapak aljabar). 2=Benar (Ibnu Khaldun perumus 'ashabiyyah di Al-Muqaddimah). 3=Benar (Ibnu Sina menulis Al-Qanun fit-Thibb). 4=Salah (Al-Biruni adalah astronom dan fisikawan, klaim kapal uap diesel abad ke-8 adalah anakronisme palsu).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "arb-sim-35",
        "materi": "TATA BAHASA NAHWU: ADAD MA'DUD & BILANGAN",
        "topic": "Evaluasi Kaidah Bilangan (Adad Ma'dud) Bahasa Arab",
        "stem": "Berikut disajikan pernyataan mengenai kaidah bilangan (*adad ma'dud*) dalam tata bahasa Arab. Tentukan apakah masing-masing pernyataan BENAR atau SALAH!",
        "statements": [
            {
                "text": "Bilangan 1 dan 2 selalu bersesuaian jenis kelaminnya (muwafaqah) dengan kata benda yang dihitung dan berposisi sebagai na'at.",
                "correct": "Benar"
            },
            {
                "text": "Bilangan 3 sampai 10 jenis kelamin adad-nya berlawanan (mukhalafah) dengan ma'dud-nya, dan ma'dud-nya berbentuk jama' majrur.",
                "correct": "Benar"
            },
            {
                "text": "Bilangan belasan 11 sampai 19 ma'dud-nya wajib berbentuk jama' marfu' dengan harakat dhommatain.",
                "correct": "Salah"
            },
            {
                "text": "Bilangan ratusan (mi'ah) dan ribuan (alf) ma'dud-nya berbentuk isim mufrad majrur bil-kasrah.",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "EVALUASI KAIDAH ADAD MA'DUD",
            "latex": "\\begin{aligned} \\text{Adad 1-2: } & \\text{Benar (Muwafaqah gender, posisi na'at)} \\\\ \\text{Adad 3-10: } & \\text{Benar (Mukhalafah gender, ma'dud jama' majrur)} \\\\ \\text{Adad 11-19: } & \\text{Salah (Ma'dud belasan wajib mufrad manshub, bukan jama' marfu')} \\\\ \\text{Mi'ah \\& Alf: } & \\text{Benar (Ma'dud mufrad majrur)} \\end{aligned}",
            "legend": "• Menunjukkan penguasaan sistematis terhadap ragam kaidah adad ma'dud bahasa Arab"
        },
        "hints": {
            "concept": "1=Benar (1-2 selaras jenis sebagai sifat). 2=Benar (3-10 lawan jenis, ma'dud jama' majrur). 3=Salah (Belasan 11-19 ma'dud-nya WAJIB mufrad manshub seperti kaukaban/rajulan). 4=Benar (100 dan 1000 ma'dud-nya mufrad majrur).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Salah, 4=Benar."
        }
    }
]
