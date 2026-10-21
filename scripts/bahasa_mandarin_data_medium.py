# -*- coding: utf-8 -*-
"""
BAHASA MANDARIN - PAKET SOAL LATIHAN MENENGAH (MEDIUM) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / HSK 3
Distribusi:
- 8 Butir: Kosakata & Gabungan Karakter HSK 3 (Cíyǔ - 决定, 相信, 经验, 参加, 环境, 了解)
- 10 Butir: Tata Bahasa Menengah (Yufa HSK 3 - Aspek 了, 着, 过; Komparatif 比, 一样; Komplemen 完, 懂, 得; Konjungsi 不但...而且...)
- 7 Butir: Teks Fungsional & Membaca Singkat (Tiket Gaotie, pengumuman bandara, memo WeChat, menu makanan, jadwal ujian)
"""

BAHASA_MANDARIN_MEDIUM_ITEMS = [
    {
        "id": "man-lat-m-01",
        "materi": "YUFA: ASPEK PENGALAMAN (GUÒ - 过)",
        "topic": "Menyatakan Riwayat Pernah Melakukan Sesuatu (V + 过)",
        "stem": "Dalam wawancara kebudayaan Tiongkok, penanya ingin mengetahui riwayat pengalaman narasumber:\n'你去 ( ... ) 北京爬长城吗？'\nPartikel aspek yang TEPAT untuk menanyakan apakah subjek 'pernah pergi ke Beijing' di masa lalu adalah...",
        "correct": "过 (guo - partikel aspek yang melekat pada verba untuk menandai pengalaman hidup di masa lalu).",
        "distractors": [
            "了 (le - partikel aspek yang menandai ketuntasan perbuatan atau perubahan status terkini).",
            "着 (zhe - partikel aspek yang menandai keberlangsungan suatu aksi atau bertahannya keadaan).",
            "在 (zài - partikel penanda aspek sedang berlangsungnya aksi progresif).",
            "的 (de - partikel struktural modifikasi kepemilikan atau frasa nomina)."
        ],
        "formula": {
            "title": "ASPEK PENGALAMAN MASA LALU (经验体助词「过」)",
            "latex": "\\mathbf{V} + \\mathbf{\\text{过 (guo)}} + \\mathbf{\\text{Objek}} \\implies \\text{Pernah melakukan } V \\text{ dalam riwayat hidup}",
            "legend": "• Menunjukkan bahwa peristiwa tersebut telah terjadi sekurang-kurangnya sekali di masa lampau"
        },
        "hints": {
            "concept": "Menyatakan pengalaman 'pernah' melakukan sesuatu dalam bahasa Mandarin memakai kata kerja + 过 (guo): 去过 (pernah pergi).",
            "execution": "Pilih: '过 (guo)'."
        }
    },
    {
        "id": "man-lat-m-02",
        "materi": "YUFA: ASPEK KELANGSUNGAN KONDISI (ZHE - 着)",
        "topic": "Menandai Keberlanjutan Keadaan Statis (V + 着)",
        "stem": "Perhatikan deskripsi suasana ruang kelas berikut:\n'门开 ( ... )，教室里坐 ( ... ) 很多学生。'\nPartikel aspek yang TEPAT untuk menyatakan bahwa pintu 'dalam keadaan terbuka' dan para siswa 'dalam kondisi duduk' adalah...",
        "correct": "着 (zhe - menandai keberlanjutan suatu keadaan fisik atau postur tubuh yang bertahan).",
        "distractors": [
            "了 (le - hanya menandai bahwa aksi membuka pintu telah selesai dieksekusi).",
            "过 (guo - menyiratkan pintu pernah terbuka di masa lalu namun kini sudah tertutup kembali).",
            "在 (zài - dilarang diletakkan di belakang kata kerja sebagai sufiks aspek).",
            "得 (dé - komplemen derajat yang memerlukan kata sifat penjelas di belakangnya)."
        ],
        "formula": {
            "title": "ASPEK KEBERLANJUTAN STATUS (持续态助词「着」)",
            "latex": "\\mathbf{V} + \\mathbf{\\text{着 (zhe)}} \\implies \\text{Keadaan fisik / postur hasil tindakan } V \\text{ sedang terus bertahan}",
            "legend": "• 门开着 (pintu dalam keadaan terbuka); 坐着 (dalam posisi duduk)"
        },
        "hints": {
            "concept": "Menyatakan keadaan yang sedang bertahan (pintu terbuka, orang duduk) menggunakan verba + 着 (zhe): 门开着, 坐着.",
            "execution": "Pilih opsi: '着 (zhe)'."
        }
    },
    {
        "id": "man-lat-m-03",
        "materi": "YUFA: KOMPARATIF BǏ (比)",
        "topic": "Struktur Kalimat Perbandingan (A 比 B + Kata Sifat + Selisih)",
        "stem": "Perhatikan data tinggi badan dua orang siswa:\nWang Ming: 175 cm\nLi Hua: 170 cm\nKalimat perbandingan yang TEPAT dan baku dalam tata bahasa Mandarin untuk mendeskripsikan data di atas adalah...",
        "correct": "王明比李华高五厘米。 (Wáng Míng bǐ Lǐ Huá gāo wǔ límǐ - Wang Ming lebih tinggi 5 cm daripada Li Hua).",
        "distractors": [
            "王明比李华很最高。 (Menambahkan kata keterangan 'hěn' atau 'zuì' yang dilarang keras di belakang struktur bǐ).",
            "王明比李华五厘米高。 (Meletakkan selisih angka sebelum kata sifat yang menyalahi susunan kata sintaksis).",
            "王明不高比李华。 (Meletakkan negasi di depan verba/adjektiva utama mendahului frasa pembanding).",
            "王明跟李华更高五厘米。 (Menggunakan gēn yang berarti 'sama dengan' dan tidak kompatibel dengan selisih angka konkret)."
        ],
        "formula": {
            "title": "STRUKTUR PERBANDINGAN KOMPARATIF (「比」字句的差量表达)",
            "latex": "\\mathbf{A + \\text{比 (bǐ)} + B + \\text{Kata Sifat} + \\text{Selisih Nilai}} \\implies \\text{Wang Ming } \\mathbf{\\text{比}} \\text{ Li Hua } \\mathbf{\\text{高 }} 5\\text{ 厘米}",
            "legend": "• Dilarang keras menyisipkan kata keterangan derajat seperti 很 (hěn) atau 非常 (fēicháng) pada predikat 比"
        },
        "hints": {
            "concept": "Rumus perbandingan 'bǐ' dengan selisih: A + 比 + B + Kata Sifat + Selisih. Jadi: 王明比李华高五厘米.",
            "execution": "Pilih opsi: '王明比李华高五厘米。'."
        }
    },
    {
        "id": "man-lat-m-04",
        "materi": "YUFA: KOMPARATIF KESETARAAN (YĪYÀNG - 一样)",
        "topic": "Menyatakan Kesamaan Karakteristik (A 跟/和 B 一样 + Sifat)",
        "stem": "Kakak dan adik memiliki tinggi badan yang sama persis (keduanya 165 cm). Kalimat kesetaraan yang BENAR adalah...",
        "correct": "哥哥跟弟弟一样高。 (Gēge gēn dìdi yíyàng gāo - kakak laki-laki sama tingginya dengan adik laki-laki).",
        "distractors": [
            "哥哥比弟弟一样高。 (Menggabungkan partikel bǐ yang menuntut perbedaan dengan kata yíyàng yang berarti sama).",
            "哥哥和弟弟一样不高。 (Konstruksi negasi yang rancu dan tidak lazim dalam perbandingan kesetaraan alami).",
            "哥哥一样高跟弟弟。 (Memecah susunan frasa preposisi gēn dìdi ke posisi akhir kalimat).",
            "哥哥像弟弟很高。 (Penggunaan xiàng yang bermakna 'menyerupai' tanpa partikel kesetaraan yíyàng)."
        ],
        "formula": {
            "title": "STRUKTUR KESETARAAN KOMPARATIF (同等比较句「一样」)",
            "latex": "\\mathbf{A + \\text{跟 / 和} + B + \\text{一样 (yíyàng)} + \\text{Kata Sifat}} \\implies A \\text{ sama } [\\text{Sifat}] \\text{ dengan } B",
            "legend": "• Untuk bentuk negasi: A 跟 B 不一样 (A tidak sama dengan B)"
        },
        "hints": {
            "concept": "Menyatakan sama tingginya: A 跟 B 一样 (yíyàng) + Sifat -> 哥哥跟弟弟一样高.",
            "execution": "Pilih: '哥哥跟弟弟一样高。'."
        }
    },
    {
        "id": "man-lat-m-05",
        "materi": "YUFA: KOMPLEMEN HASIL (JIÉGUǑ BǓYǓ)",
        "topic": "Penggunaan Komplemen Hasil Selesai (完 - Wán) dan Paham (懂 - Dǒng)",
        "stem": "Perhatikan kalimat rumpang kegiatan membaca berikut:\n'这篇文章我听了两遍，终于听 ( A ) 了，作业也写 ( B ) 了。'\nKomplemen hasil yang TEPAT untuk menyatakan 'mendengar hingga paham' ( A ) dan 'menulis hingga selesai' ( B ) berturut-turut adalah...",
        "correct": "A: 懂 (dǒng - mengerti/paham makna teks melalui pendengaran), B: 完 (wán - tuntas menyelesaikan seluruh halaman tugas).",
        "distractors": [
            "A: 完 (wán), B: 懂 (dǒng) - terbalik esensi hasil pemahaman intelektual dengan tuntasnya tugas fisik.",
            "A: 见 (jiàn), B: 到 (dào) - jiàn menandai persepsi indra penangkapan suara/cahaya sekilas.",
            "A: 对 (duì), B: 错 (cuò) - duì dan cuò menandai benar atau salahnya hasil pengerjaan.",
            "A: 好 (hǎo), B: 走 (zǒu) - zǒu adalah kata kerja gerak berjalan yang tidak berfungsi sebagai komplemen tugas."
        ],
        "formula": {
            "title": "SISTEM KOMPLEMEN HASIL MANDARIN (结果补语体系)",
            "latex": "\\begin{aligned} \\text{听 (Mendengar)} + \\mathbf{\\text{懂 (dǒng / Paham)}} & \\implies \\mathbf{\\text{听懂 (Mendengar dan mengerti)}} \\\\ \\text{写 (Menulis)} + \\mathbf{\\text{完 (wán / Tuntas)}} & \\implies \\mathbf{\\text{写完 (Menulis hingga tuntas)}} \\end{aligned}",
            "legend": "• Menunjukkan bahwa aksi predikat primer berhasil mencapai target kualitatif/kuantitatif tertentu"
        },
        "hints": {
            "concept": "Mendengar sampai paham: 听懂 (tīngdǒng). Menulis sampai selesai: 写完 (xiěwán).",
            "execution": "Pilih opsi: 'A: 懂 (dǒng), B: 完 (wán)'."
        }
    },
    {
        "id": "man-lat-m-06",
        "materi": "YUFA: KOMPLEMEN DERAJAT (CHÉNGDÙ BǓYǓ)",
        "topic": "Evaluasi Struktur Partikel Struktural De (得) Penjelas Aksi",
        "stem": "Seorang penutur asli memuji kemahiran bermain tenis meja temannya:\n'他乒乓球打 ( ... ) 很好。'\nPartikel struktural yang WAJIB diletakkan di antara kata kerja transitif '打' (bermain/memukul) dan frasa evaluasi derajat '很好' (sangat bagus) adalah...",
        "correct": "得 (de - partikel struktural yang menghubungkan kata kerja dengan komplemen penjelas tingkat kualitas tindakan).",
        "distractors": [
            "的 (de - partikel kepemilikan nomina yang salah fatal jika diletakkan setelah kata kerja untuk komplemen).",
            "地 (de - partikel adverbial yang hanya dipakai sebelum kata kerja untuk menerangkan sikap tindakan).",
            "很 (hěn - kata keterangan yang tidak dapat bertindak sebagai partikel struktural penghubung).",
            "了 (le - partikel aspek yang tidak dapat mengikat langsung kata sifat evaluatif kualitas)."
        ],
        "formula": {
            "title": "DISTINGSI TIGA PARTIKEL DE MANDARIN (结构助词「的、地、得」)",
            "latex": "\\begin{aligned} \\text{Nomina: } & \\text{Atribut} + \\mathbf{\\text{的 (de)}} + \\text{Nomina} \\quad (\\text{红色的花}) \\\\ \\text{Adverbia: } & \\text{Adverbia} + \\mathbf{\\text{地 (de)}} + \\text{Verba} \\quad (\\text{快快地跑}) \\\\ \\mathbf{\\text{Komplemen:}} & \\mathbf{V} + \\mathbf{\\text{得 (de)}} + \\mathbf{\\text{Evaluasi/Derajat}} \\quad (\\text{打 } \\mathbf{\\text{得}} \\text{ 很好}) \\end{aligned}",
            "legend": "• Salah satu batu uji gramatika paling ketat dalam standar kemahiran HSK"
        },
        "hints": {
            "concept": "Menilai kualitas perbuatan (V + de + Sifat) wajib memakai '得' (de): 打得很好 (bermain dengan sangat baik).",
            "execution": "Pilih: '得 (de)'."
        }
    },
    {
        "id": "man-lat-m-07",
        "materi": "YUFA: INTENSITAS BERTAHAP (YUÈ LÁI YUÈ)",
        "topic": "Penggunaan Frasa Keterangan 'Semakin' (越来越 + Sifat)",
        "stem": "Saat memasuki musim dingin di Beijing, suhu udara terus menurun setiap harinya. Kalimat yang TEPAT untuk menyatakan 'Cuaca semakin hari menjadi semakin dingin' adalah...",
        "correct": "天气越来越冷了。 (Tiānqì yuè lái yuè lěng le - cuaca semakin lama menjadi semakin dingin).",
        "distractors": [
            "天气越来越很冷。 (Menyisipkan kata keterangan 'hěn' di dalam struktur yuèláiyuè yang dilarang keras).",
            "天气越来越非常冷。 (Menyisipkan kata keterangan 'fēicháng' yang merusak fungsi intensitas bertahap).",
            "天气更越来越冷。 (Penggabungan dobel kata 'gèng' yang rancu di depan yuèláiyuè).",
            "天气最越来越冷。 (Penggabungan kata superlatif 'zuì' yang bertentangan dengan proses kontinuitas)."
        ],
        "formula": {
            "title": "POLA INTENSIFIKASI PROGRESIF (渐进结构「越来越...」)",
            "latex": "\\mathbf{\\text{越来越 (yuè lái yuè)}} + \\mathbf{\\text{Kata Sifat / Verba Psikologis}} \\quad (\\cancel{\\text{越来越很}}, \\cancel{\\text{越来越非常}})",
            "legend": "• Menunjukkan eskalasi derajat yang berkembang seiring berjalannya waktu"
        },
        "hints": {
            "concept": "Pola 'semakin...': 越来越 (yuè lái yuè) + Kata Sifat. Tidak boleh disisipkan '很' (hěn) atau '非常' (fēicháng).",
            "execution": "Pilih: '天气越来越冷了。'."
        }
    },
    {
        "id": "man-lat-m-08",
        "materi": "YUFA: KONJUNGSI BERTINGKAT KUMULATIF",
        "topic": "Pasangan Konjungsi Bukan Hanya... Bahkan... (不但...而且...)",
        "stem": "Lengkapilah kalimat prestasi siswa berikut:\n'李华 ( A ) 会说流利的英语，( B ) 还会说法语。'\nPasangan konjungsi penambahan kumulatif yang TEPAT untuk ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: 不但 (búdàn), B: 而且 (érqiě).",
        "distractors": [
            "A: 虽然 (suīrán), B: 但是 (dànshì) - menyatakan pertentangan yang tidak selaras dengan akumulasi dua bahasa).",
            "A: 因为 (yīnwèi), B: 所以 (suǒyǐ) - menyatakan hubungan sebab akibat lurus yang kurang pas).",
            "A: 如果 (rúguǒ), B: 就 (jiù) - menyatakan syarat hipotetis bersyarat).",
            "A: 宁可 (nìngkě), B: 也不 (yěbù) - menyatakan pilihan kompromi berkorban)."
        ],
        "formula": {
            "title": "KONJUNGSI AKUMULATIF BERTINGKAT (递进复句)",
            "latex": "\\mathbf{\\text{不但 (búdàn) } + \\text{Unsur 1}} \\dots \\mathbf{\\text{而且 (érqiě) } + \\text{Unsur 2 Lebih Lanjut}} \\implies \\text{Bukan hanya } \\dots \\text{ bahkan juga } \\dots",
            "legend": "• Mengindikasikan penambahan tingkat keunggulan atau keluasan kapasitas subjek"
        },
        "hints": {
            "concept": "Bukan hanya bisa bahasa Inggris, bahkan juga bisa bahasa Prancis: 不但 (búdàn)... 而且 (érqiě)...",
            "execution": "Pilih: 'A: 不但 (búdàn), B: 而且 (érqiě)'."
        }
    },
    {
        "id": "man-lat-m-09",
        "materi": "YUFA: KATA HUBUNG KONDISIONAL BERSYARAT",
        "topic": "Pasangan Konjungsi Pengandaian (如果...就... - Rúguǒ... Jiù...)",
        "stem": "Cermati kalimat rencana rekreasi akhir pekan berikut:\n'( A ) 明天不下雨，我们 ( B ) 去爬山。'\nPasangan kata penghubung pengandaian yang TEPAT mengisi ( A ) 'jika' dan ( B ) 'maka' adalah...",
        "correct": "A: 如果 (rúguǒ), B: 就 (jiù).",
        "distractors": [
            "A: 虽然 (suīrán), B: 可是 (kěshì) - konjungsi pertentangan konsesif.",
            "A: 只有 (zhǐyǒu), B: 才 (cái) - syarat tunggal mutlak yang menuntut inversi makna keharusan.",
            "A: 因为 (yīnwèi), B: 所以 (suǒyǐ) - kausalitas fakta yang sudah terjadi.",
            "A: 即使 (jíshǐ), B: 也 (yě) - pengandaian ekstrem konsesif (meskipun seandainya)."
        ],
        "formula": {
            "title": "KONJUNGSI BERSYARAT HIPOTETIS (假设复句)",
            "latex": "\\mathbf{\\text{如果 (rúguǒ) } + \\text{Kondisi Syarat}} \\dots \\mathbf{\\text{就 (jiù) } + \\text{Konsekuensi Hasil}} \\implies \\text{Jika } \\dots \\text{ maka } \\dots",
            "legend": "• Menghubungkan premis kemungkinan masa depan dengan rencana aksi subjek"
        },
        "hints": {
            "concept": "Jika besok tidak hujan, maka kita pergi mendaki: 如果 (rúguǒ)... 就 (jiù)...",
            "execution": "Pilih opsi: 'A: 如果 (rúguǒ), B: 就 (jiù)'."
        }
    },
    {
        "id": "man-lat-m-10",
        "materi": "YUFA: PREPOSISI INSTRUMEN & SARANA",
        "topic": "Penggunaan Kata Kerja Bantu Preposisi 'Yòng' (用 - Menggunakan)",
        "stem": "Dalam wacana kuliner Tionghoa, kalimat yang TEPAT untuk menyatakan 'Orang Tiongkok terbiasa makan menggunakan sumpit' adalah...",
        "correct": "中国人习惯用筷子吃饭。 (Zhōngguórén xíguàn yòng kuàizi chīfàn - orang Tiongkok terbiasa memakai sumpit untuk makan).",
        "distractors": [
            "中国人习惯吃饭用筷子。 (Menempatkan sarana 'yòng kuàizi' di belakang objek makanan meniru pola bahasa Indonesia/Inggris).",
            "中国人习惯在筷子吃饭。 (Preposisi zài menandai lokasi tempat, bukan alat instrumen makan).",
            "中国人习惯被筷子吃饭。 (Struktur kalimat pasif bèi yang keliru mengartikan orang dimakan oleh sumpit).",
            "中国人习惯把筷子吃饭。 (Struktur bǎ yang rancu tanpa verba tindakan yang tuntas terhadap sumpit)."
        ],
        "formula": {
            "title": "STRUKTUR SARANA INSTRUMEN MANDARIN (连动句・方式状语)",
            "latex": "\\mathbf{\\text{Subjek}} + \\mathbf{\\text{用 (yòng) } + \\text{Instrumen/Alat}} + \\mathbf{\\text{Kata Kerja } + \\text{Objek}} \\quad (\\cancel{\\text{V + O + yòng Alat}})",
            "legend": "• Pola kalimat berangkai (Liándòngjù) di mana cara/alat mendahului aksi utama"
        },
        "hints": {
            "concept": "Menggunakan alat melakukan perbuatan: 用 (yòng) Alat + Kata Kerja. Jadi: 用筷子吃饭 (memakai sumpit makan).",
            "execution": "Pilih: '中国人习惯用筷子吃饭。'."
        }
    },
    {
        "id": "man-lat-m-11",
        "materi": "MOJIGOI: KATA MAJEMUK KEPUTUSAN & PERENCANAAN",
        "topic": "Makna dan Penggunaan Kata '决定' (Juédìng)",
        "stem": "Perhatikan kalimat berikut:\n'经过深思熟虑，他最终 [决定] 放弃出国的机会，留在国内创业。'\nMakna yang TEPAT dari kata yang berada di dalam kurung siku [决定] (juédìng) adalah...",
        "correct": "Memutuskan / Mengambil keputusan bulat setelah mempertimbangkan secara matang.",
        "distractors": [
            "Meragukan / Menolak mempercayai fakta yang ada di lapangan.",
            "Menyesal / Merasa kecewa atas peristiwa buruk yang terlanjur terjadi.",
            "Memohon / Meminta bantuan kepada pihak keluarga besar.",
            "Menunda / Mengulur-ulur waktu pelaksanaan rencana kerja."
        ],
        "formula": {
            "title": "LEKSIKOGRAFI KATA JUEDING (词汇语义「决定」)",
            "latex": "[\\text{决 (jué / Pasti/Tegas)}] + [\\text{定 (dìng / Tetap/Pasti)}] \\implies \\mathbf{\\text{决定 (juédìng / Memutuskan)}}",
            "legend": "• Berfungsi ganda sebagai kata kerja (memutuskan) maupun kata benda (sebuah keputusan)"
        },
        "hints": {
            "concept": "决定 (juédìng) bermakna memutuskan atau keputusan.",
            "execution": "Pilih: 'Memutuskan / Mengambil keputusan bulat'."
        }
    },
    {
        "id": "man-lat-m-12",
        "materi": "MOJIGOI: KATA KERJA RELASIONAL SOSIAL",
        "topic": "Makna dan Penggunaan Kata '相信' (Xiāngxìn) vs '帮助' (Bāngzhù)",
        "stem": "Lengkapilah kalimat saling percaya dan tolong-menolong berikut:\n'朋友之间应该互相 ( A )，遇到困难时要互相 ( B )。'\nKata yang TEPAT untuk mengisi posisi saling 'mempercayai' ( A ) dan saling 'membantu' ( B ) berturut-turut adalah...",
        "correct": "A: 相信 (xiāngxìn - mempercayai), B: 帮助 (bāngzhù - menolong/membantu).",
        "distractors": [
            "A: 帮助 (bāngzhù), B: 相信 (xiāngxìn) - terbalik urutan logika batin pertemanan.",
            "A: 明白 (míngbai), B: 决定 (juédìng) - mengerti dan memutuskan.",
            "A: 介绍 (jièshào), B: 离开 (líkāi) - memperkenalkan dan meninggalkan.",
            "A: 清楚 (qīngchu), B: 迟到 (chídào) - jelas dan terlambat."
        ],
        "formula": {
            "title": "KOLOKASI KATA KERJA RESIPROKAL (互助词汇搭配)",
            "latex": "\\begin{cases} \\text{互相 (Hùxiāng / Saling)} + \\mathbf{\\text{相信 (xiāngxìn)}} & \\implies \\text{Saling Mempercayai} \\\\ \\text{互相 (Hùxiāng / Saling)} + \\mathbf{\\text{帮助 (bāngzhù)}} & \\implies \\text{Saling Menolong/Membantu} \\end{cases}",
            "legend": "• Menunjukkan nilai kebajikan etika relasi interpersonal Tionghoa (Renqing)"
        },
        "hints": {
            "concept": "Saling percaya: 互相相信 (hùxiāng xiāngxìn). Saling membantu: 互相帮助 (hùxiāng bāngzhù).",
            "execution": "Pilih: 'A: 相信 (xiāngxìn), B: 帮助 (bāngzhù)'."
        }
    },
    {
        "id": "man-lat-m-13",
        "materi": "MOJIGOI: KATA SIFAT FASILITAS & LINGKUNGAN",
        "topic": "Makna Kata '方便' (Fāngbiàn) dan '环境' (Huánjìng)",
        "stem": "Dalam ulasan sewa apartemen di Beijing tertulis:\n'这里的交通非常 [方便]，小区的 [环境] 也很安静漂亮。'\nMakna dari dua kata di dalam kurung siku [方便] dan [环境] berturut-turut adalah...",
        "correct": "方便 (praktis / mudah / nyaman aksesnya), dan 环境 (lingkungan / suasana sekitar perumahan).",
        "distractors": [
            "方便 (mahal / mewah), dan 环境 (keamanan gedung / satpam).",
            "方便 (sempit / sesak), dan 环境 (cuaca dingin bersalju).",
            "方便 (kuno / tradisional), dan 环境 (kualitas jaringan internet).",
            "方便 (jauh / terpencil), dan 环境 (kebisingan pasar malam)."
        ],
        "formula": {
            "title": "LEKSIKAL DESKRIPSI HUNIAN (居住环境评价词汇)",
            "latex": "\\mathbf{\\text{交通方便 (Akses Transportasi Praktis/Mudah)}} \\quad \\& \\quad \\mathbf{\\text{环境安静 (Lingkungan Tenang Asri)}}",
            "legend": "• Kosakata esensial dalam literasi interaksi sosial dan pemilihan tempat tinggal"
        },
        "hints": {
            "concept": "方便 (fāngbiàn) berarti praktis/mudah/nyaman. 环境 (huánjìng) berarti lingkungan.",
            "execution": "Pilih opsi: '方便 (praktis / mudah / nyaman), dan 环境 (lingkungan / suasana sekitar)'."
        }
    },
    {
        "id": "man-lat-m-14",
        "materi": "MOJIGOI: KATA KERJA PENGETAHUAN MENDALAM",
        "topic": "Perbedaan Kata '知道' (Zhīdào), '认识' (Rènshi), dan '了解' (Liǎojiě)",
        "stem": "Lengkapilah kalimat berikut dengan kata yang menandai pemahaman mendalam dan komprehensif mengenai suatu kebudayaan:\n'他在中国生活了十年，非常 ( ... ) 中国的茶文化和传统风俗。'",
        "correct": "了解 (liǎojiě - memahami secara mendalam, menyeluruh, dan menghayati seluk-beluk suatu objek).",
        "distractors": [
            "知道 (zhīdào - semata-mata mengetahui sebatas informasi fakta umum di permukaan).",
            "认识 (rènshi - mengenal rupa fisik orang atau mengenali aksara visual tertentu).",
            "认为 (rènwéi - berpendapat atau beranggapan subjektif menurut pemikiran sendiri).",
            "觉得 (juéde - merasakan atau mengira sesuatu secara sekilas)."
        ],
        "formula": {
            "title": "GRADASI KATA PENGETAHUAN KOGNITIF (认知动词的语义梯度)",
            "latex": "\\text{知道 (Tahu Fakta)} \\subset \\text{认识 (Kenal Rupa)} \\subset \\mathbf{\\text{了解 (Liǎojiě - Paham Mendalam \\& Menghayati)}}",
            "legend": "• Mengindikasikan akumulasi wawasan mendalam berkat pengalaman hidup selama 10 tahun"
        },
        "hints": {
            "concept": "Tinggal 10 tahun di Tiongkok membuatnya 'sangat memahami secara mendalam' (非常了解 - fēicháng liǎojiě) budaya teh dan adat istiadat.",
            "execution": "Pilih: '了解 (liǎojiě)'."
        }
    },
    {
        "id": "man-lat-m-15",
        "materi": "MOJIGOI: KATA KERJA KEIKUTSERTAAN",
        "topic": "Penggunaan Kata '参加' (Cānjiā - Mengikuti Acara/Ujian)",
        "stem": "Kalimat manakah di bawah ini yang menunjukkan penggunaan kata kerja '参加' (cānjiā) secara TEPAT dan berterima dalam bahasa Mandarin baku?",
        "correct": "很多留学生报名参加了今年的汉语水平考试（HSK）。 (Banyak mahasiswa asing mendaftar untuk mengikuti ujian HSK tahun ini).",
        "distractors": [
            "我今天参加图书馆看书。 (Dilarang menggunakan cānjiā untuk lokasi tempat; seharusnya pergi ke túshūguǎn).",
            "他参加了一个苹果。 (Dilarang menggunakan cānjiā untuk memakan atau membeli benda fisik makanan).",
            "妈妈正在厨房参加饭。 (Dilarang menggunakan cānjiā untuk memasak nasi di dapur).",
            "我们一起参加公共汽车去市中心。 (Dilarang menggunakan cānjiā untuk menaiki moda transportasi; seharusnya zuò/dā)."
        ],
        "formula": {
            "title": "KOLOKASI KATA KERJA PARTISIPASI (「参加」的宾语搭配范围)",
            "latex": "\\mathbf{\\text{参加 (cānjiā)}} + \\begin{cases} \\mathbf{\\text{Ujian / Kompetisi:}} & \\text{考试 (kǎoshì), 比赛 (bǐsài)} \\\\ \\mathbf{\\text{Kegiatan / Rapat:}} & \\text{活动 (huódòng), 会议 (huìyì)} \\end{cases}",
            "legend": "• Cānjiā HANYA berpasangan dengan event, acara kolektif, perhelatan, atau ujian resmi"
        },
        "hints": {
            "concept": "参加 (cānjiā) berarti mengikuti kegiatan, rapat, atau ujian (参加考试). Tidak bisa dipakai untuk benda fisik atau naik bus.",
            "execution": "Pilih: '很多留学生报名参加了今年的汉语水平考试（HSK）。'."
        }
    },
    {
        "id": "man-lat-m-16",
        "materi": "DOKKAI TEKSTUAL: TIKET KERETA CEPAT GAOTIE",
        "topic": "Menganalisis Informasi Rute, Waktu, dan Tempat Duduk Tiket Kereta Cepat",
        "stem": "Bacalah informasi pada tiket kereta cepat (*Gāotiě*) Tiongkok berikut:\n--------------------------------------------------\n【中国铁路客票】\nG102次　上海虹桥站 (Shanghai Hongqiao) \\to 北京南站 (Beijing South)\n2026年10月15日　08:00开\n票价：¥ 553.0元　二等座 (Second Class Seat)\n05车厢　12F号 (Gerbong 05, Kursi 12F - Dekat Jendela)\n限乘当日当次车\n--------------------------------------------------\nBerdasarkan data tiket di atas, pernyataan manakah yang BENAR?",
        "correct": "Kereta G102 berangkat dari Stasiun Shanghai Hongqiao menuju Stasiun Beijing South pada pukul 08.00 pagi dengan kelas kursi kedua di dekat jendela (12F).",
        "distractors": [
            "Kereta berangkat dari stasiun Beijing South menuju ke stasiun Shanghai Hongqiao pada sore hari pukul 17.00.",
            "Harga tiket kereta api cepat tersebut adalah 102 Yuan Tiongkok dan berlaku untuk kelas bisnis VIP.",
            "Penumpang memiliki nomor kursi di gerbong 12 dengan nomor tempat duduk 05F di dekat lorong jalan.",
            "Tiket tersebut dapat digunakan bebas di sembarang kereta api reguler selama bulan Oktober 2026."
        ],
        "formula": {
            "title": "ANALISIS ELEMEN TIKET GAOTIE (高铁车票信息要素)",
            "latex": "\\begin{aligned} \\text{Nomor KA: } & \\text{G102} \\\\ \\text{Rute: } & \\mathbf{\\text{Shanghai Hongqiao } \\longrightarrow \\text{ Beijing South}} \\\\ \\text{Jam/Biaya: } & \\mathbf{08:00} \\quad / \\quad \\mathbf{¥ 553.0} \\\\ \\text{Posisi Duduk: } & \\mathbf{\\text{Gerbong 05, Kursi 12F (Jendela/Window)}} \\end{aligned}",
            "legend": "• Huruf kursi kereta Tiongkok: A/F = Jendela (Window), C/D = Lorong (Aisle), B = Tengah (Middle)"
        },
        "hints": {
            "concept": "Tiket menunjukkan: G102 上海虹桥 -> 北京南 (Shanghai Hongqiao ke Beijing South), 08:00开 (berangkat jam 8 pagi), 05车厢 12F (Gerbong 5, Kursi 12F jendela), 二等座 (Second class).",
            "execution": "Pilih opsi yang menyebutkan keberangkatan jam 08.00 pagi dari Shanghai Hongqiao ke Beijing South gerbong 5 kursi 12F."
        }
    },
    {
        "id": "man-lat-m-17",
        "materi": "DOKKAI TEKSTUAL: PENGUMUMAN BANDARA INTERNASIONAL",
        "topic": "Memahami Instruksi Panggilan Pintu Masuk Pesawat (Boarding Gate)",
        "stem": "Dengarkan pengumuman audio di terminal bandara internasional Beijing berikut:\n--------------------------------------------------\n“前往雅加达的 CA977次 航班的 旅客请注意：您乘坐的 航班现在 开始登机了。请您 带好 随身物品，出示 登机牌，由 18号登机口 上飞机。祝您 旅途愉快！”\n--------------------------------------------------\nInstruksi apakah yang disampaikan kepada para penumpang pesawat CA977 dalam pengumuman tersebut?",
        "correct": "Pemberitahuan bahwa proses naik ke pesawat (*登机 - dēngjī*) telah dimulai dan penumpang dipersilakan menuju Pintu Masuk Nomor 18 (18号登机口).",
        "distractors": [
            "Pemberitahuan bahwa penerbangan menuju Jakarta mengalami pembatalan sepihak akibat badai salju lebat.",
            "Instruksi kepada seluruh penumpang untuk segera mengambil bagasi koper di sabuk konveyor nomor 18.",
            "Peringatan bahwa pintu gerbang nomor 18 telah ditutup permanen karena pesawat telah lepas landas.",
            "Permintaan kepada penumpang untuk menukarkan kembali uang mata uang asing di loket kasir bandara."
        ],
        "formula": {
            "title": "DEKODING INFORMASI BANDARA (机场登机广播解析)",
            "latex": "\\mathbf{\\text{开始登机 (Mulai Boarding)}} + \\mathbf{\\text{18号登机口 (Gate 18)}} + \\text{CA977次 (Ke Jakarta)}",
            "legend": "• Kosakata kunci: 登机 (dēngjī - naik pesawat); 登机口 (dēngjīkǒu - boarding gate)"
        },
        "hints": {
            "concept": "Teks pengumuman: '现在 开始登机了 (sekarang mulai boarding)... 由 18号登机口 上飞机 (naik pesawat lewat boarding gate 18)'.",
            "execution": "Pilih opsi: Pemberitahuan boarding telah dimulai di Gate 18."
        }
    },
    {
        "id": "man-lat-m-18",
        "materi": "DOKKAI TEKSTUAL: MEMO PERCAKAPAN WECHAT KANTOR",
        "topic": "Memverifikasi Perubahan Jadwal Pertemuan Rapat Kerja",
        "stem": "Bacalah pesan singkat pada grup kerja WeChat berikut:\n--------------------------------------------------\n张经理：@所有人 原定于 今天下午 两点在 第三会议室 召开的 部门会议，因 客户临时来访，现 推迟到 明天上午 九点半举行。会议地点 不变，请 大家准时 参加，并 提前准备好 销售报告。\n--------------------------------------------------\nBerdasarkan pesan Manajer Zhang di atas, kapankah rapat divisi tersebut akhirnya akan diselenggarakan?",
        "correct": "Besok pagi pukul 09.30 di Ruang Rapat Ketiga.",
        "distractors": [
            "Hari ini siang tepat pukul 14.00 di Ruang Rapat Pertama.",
            "Hari ini sore pukul 16.00 setelah klien bisnis meninggalkan kantor.",
            "Besok sore pukul 14.00 dengan memindahkan lokasi ke kantor cabang lain.",
            "Rapat dibatalkan selamanya dan laporan penjualan ditiadakan."
        ],
        "formula": {
            "title": "ANALISIS JADWAL PESAN WECHAT (微信通知的时间推移)",
            "latex": "\\text{Jadwal Semula (原定): } \\text{Hari ini 14:00} \\xrightarrow{\\mathbf{\\text{推迟到 (Diundur ke)}}} \\mathbf{\\text{明天上午 09:30 (Ruang Rapat 3)}}",
            "legend": "• Kata kunci: 推迟到 (tuīchí dào - diundur ke waktu tertentu)"
        },
        "hints": {
            "concept": "Pesan menyatakan: '现 推迟到 明天上午 九点半举行。会议地点 不变' (sekarang diundur ke besok pagi jam 9.30, tempat ruang rapat 3 tetap).",
            "execution": "Pilih opsi: 'Besok pagi pukul 09.30 di Ruang Rapat Ketiga'."
        }
    },
    {
        "id": "man-lat-m-19",
        "materi": "DOKKAI TEKSTUAL: RESEP MASAKAN & MENU",
        "topic": "Mengenal Ciri Khas Kuliner Tionghoa (Bebek Panggang Beijing - Běijīng Kǎoyā)",
        "stem": "Bacalah deskripsi menu kuliner tradisional berikut:\n--------------------------------------------------\n北京烤鸭是 中国著名的 传统名菜。这道菜 以 优质的 鸭肉为 原料，用 果木炭火 烤制而成。烤好的 鸭子 皮肤呈 枣红色，油亮香脆，肉质 鲜嫩多汁。吃烤鸭时，厨师会当着 客人的 面把 鸭皮和 鸭肉切成 薄片。地道的 吃法是用 特制的 薄荷叶饼（荷叶饼），抹上 甜面酱，卷入 鸭肉、葱条和 黄瓜条 一起食用，风味非常 独特。\n--------------------------------------------------\nBagaimanakah tata cara autentik menyantap Bebek Panggang Beijing (*Běijīng Kǎoyā*) menurut wacana di atas?",
        "correct": "Mengambil selembar panekuk tipis (*héyèbǐng*), mengoleskan saus manis (*tiánmiànjiàng*), lalu menggulungnya bersama irisan daging/kulit bebek, daun bawang, dan potongan mentimun.",
        "distractors": [
            "Memasukkan seluruh potongan bebek utuh ke dalam mangkuk kuah sup pedas mendidih bercampur cabai rawit.",
            "Memakan irisan daging bebek dengan mencelupkannya langsung ke dalam susu manis dingin tanpa bumbu saus.",
            "Mengeringkan irisan daging bebek di bawah terik matahari sebelum digoreng kembali dengan tepung krispi.",
            "Meminum saus manis pekat terlebih dahulu sebelum menyantap potongan kulit bebek tanpa sayuran apa pun."
        ],
        "formula": {
            "title": "TATA BOGA KULINER KAOYA (北京烤鸭的正宗吃法)",
            "latex": "\\mathbf{\\text{薄饼 (Héyèbǐng)}} + \\mathbf{\\text{甜面酱 (Saus Manis)}} + \\mathbf{\\text{鸭肉 (Daging Bebek)}} + \\mathbf{\\text{葱条/黄瓜条 (Sayur Segar)}} \\implies \\text{Gulungan Autentik Kaoya}",
            "legend": "• Harmoni perpaduan rasa gurih renyah hewani dengan kesegaran nabati saus fermentasi"
        },
        "hints": {
            "concept": "Teks mendeskripsikan: '用 特制的 薄荷叶饼，抹上 甜面酱，卷入 鸭肉、葱条和 黄瓜条 一起食用' (gulung bebek, saus manis, daun bawang, mentimun dalam panekuk tipis).",
            "execution": "Pilih opsi yang menjelaskan menggulung bebek dengan panekuk tipis, saus manis, daun bawang, dan mentimun."
        }
    },
    {
        "id": "man-lat-m-20",
        "materi": "DOKKAI TEKSTUAL: WACANA KEARIFAN TRADISI",
        "topic": "Budaya Minum Teh Tiongkok (Chá Wénhuà - 茶文化)",
        "stem": "Bacalah wacana kebudayaan berikut:\n'茶在 中国已经有 数千年的 历史。中国人 不仅把 茶当作 日常的 饮料，还把它 提升为 一种 精神艺术，即“茶道”。在 中国，茶主要 分为 绿茶、红茶、乌龙茶、白茶、黄茶和 黑茶（如普洱茶）六大类。泡茶时，对 水温、茶具和 泡茶时间 都有 严格的 讲究。客人来访时，主人为 客人 倒茶一般 只倒 七分满，俗话说“茶满 欺客”，留出 三分 象征着 彼此的情谊与 尊重。'\nMengapa dalam etika menyuguhkan teh kepada tamu di Tiongkok, tuan rumah hanya menuangkan air teh sebanyak 70% penuh (tujuh persepuluh cangkir)?",
        "correct": "Karena menurut tradisi 'Chá mǎn qī kè', mengisi cangkir hingga penuh meluap dianggap tidak sopan/menghina tamu, dan sisa ruang kosong melambangkan rasa hormat serta persahabatan.",
        "distractors": [
            "Karena tuan rumah ingin menghemat persediaan air minum dan daun teh mahal agar tidak cepat habis.",
            "Karena cangkir teh porselen kuno Tiongkok akan pecah secara otomatis jika diisi air panas melebihi separuh wadah.",
            "Agar tamu merasa kehausan dan terpaksa membeli air teh botolan yang dijual oleh anggota keluarga tuan rumah.",
            "Karena daun teh Tiongkok mengandung zat racun alami yang baru mengendap jika cangkir dibiarkan terisi penuh meluber."
        ],
        "formula": {
            "title": "ETIKA MENUANG AIR TEH TIONGHOA (客礼哲学「茶满欺客」)",
            "latex": "\\text{Tuang Teh: } \\mathbf{\\text{七分满 (70\\% Penuh)}} \\quad \\longleftrightarrow \\quad \\mathbf{\\text{三分情 (30\\% Ruang Persahabatan \\& Keamanan Tangan)}}",
            "legend": "• Mencegah cangkir panas membakar jari jemari tamu saat diangkat dari nampan kayu"
        },
        "hints": {
            "concept": "Teks menyatakan: '俗话说“茶满 欺客”，留出 三分 象征着 彼此的情谊与 尊重' (menuang penuh dianggap menghina tamu, menyisakan 30% cangkir melambangkan rasa hormat dan persahabatan).",
            "execution": "Pilih opsi yang menjelaskan pepatah 'Cha man qi ke' dan sisa ruang sebagai simbol rasa hormat serta persahabatan."
        }
    },
    {
        "id": "man-lat-m-21",
        "materi": "DOKKAI TEKSTUAL: SASTRA PEPATAH KLASIK (CHÉNGYǓ)",
        "topic": "Memahami Pepatah Menanam Pohon untuk Keturunan (前人栽树，后人乘凉)",
        "stem": "Dalam pidato bertema pembangunan berkelanjutan, seorang pejabat mengutip peribahasa terkenal:\n'“前人栽树，后人乘凉”（Qián rén zāi shù, hòu rén chéng liáng）。\n这句话 告诉我们，今天 我们 所享受的 幸福生活，是 前辈们 辛勤 付出和 努力的 结果；同样，我们 现在的 奋斗，也是 为了 子孙后代 能够 拥有 更美好的 明天。'\nNilai moral utama yang ditekankan oleh peribahasa 'Qián rén zāi shù, hòu rén chéng liáng' di atas adalah...",
        "correct": "Generasi terdahulu bersusah payah menanam kebajikan dan infrastruktur agar generasi penerus dapat menikmati kesejahteraan dan keteduhan hidup.",
        "distractors": [
            "Masyarakat diwajibkan untuk menebang seluruh pohon rindang di pinggir jalan raya agar tidak menghalangi sinar matahari.",
            "Setiap individu dilarang beristirahat di bawah naungan pohon sebelum membayar pajak perkebunan kepada pemerintah.",
            "Generasi muda tidak perlu bekerja keras karena seluruh kekayaan telah diwariskan secara berlimpah oleh orang tua.",
            "Menanam bibit pohon buah di hutan lindung merupakan perbuatan sia-sia yang merugikan anggaran kas negara."
        ],
        "formula": {
            "title": "HERMENEUTIKA PERIBAHASA CHENGYU (俗语哲理「前人栽树后人乘凉」)",
            "latex": "\\mathbf{\\text{前人栽树 (Generasi Dahulu Menanam Pohon)}} \\implies \\mathbf{\\text{后人乘凉 (Generasi Penerus Menikmati Keteduhan)}}",
            "legend": "• Menekankan tanggung jawab etis antargenerasi (intergenerational equity) dan pengorbanan leluhur"
        },
        "hints": {
            "concept": "Peribahasa bermakna: orang zaman dulu menanam pohon, orang zaman sekarang berteduh di bawahnya. Artinya generasi terdahulu berjuang agar generasi penerus menikmati hasilnya.",
            "execution": "Pilih opsi yang menjelaskan perjuangan generasi terdahulu agar generasi penerus dapat menikmati kesejahteraan."
        }
    },
    {
        "id": "man-lat-m-22",
        "materi": "DOKKAI TEKSTUAL: ISU TEKNOLOGI MODERN TIONGKOK",
        "topic": "Gaya Hidup Tanpa Uang Tunai (Wú Xiànjīn Shèhuì - 无现金社会)",
        "stem": "Bacalah teks mengenai transformasi ekonomi digital di Tiongkok berikut:\n--------------------------------------------------\n在 现代中国，“无现金生活”已经 成为 普通百姓的 日常。出门时，人们 几乎 不用 带现金和 钱包，只需 一部 智能手机，通过 微信支付（WeChat Pay）或 支付宝（Alipay）扫描 二维码（QR Code），就能 轻松 完成 购物、打车、用餐、甚至 在路边摊 买早点。移动支付的 普及，不仅 极大地 提高了 交易效率，也 改变了 人们的 消费习惯。\n--------------------------------------------------\nFaktor utama apakah yang memungkinkan terciptanya masyarakat tanpa uang tunai (*Cashless Society*) di Tiongkok?",
        "correct": "Popularitas pembayaran seluler melalui pemindaian kode QR pada aplikasi seperti WeChat Pay dan Alipay di berbagai level transaksi masyarakat.",
        "distractors": [
            "Larangan mutlak dari perbankan pusat bagi siapa pun untuk memiliki rekening tabungan bank secara pribadi.",
            "Pemusnahan seluruh uang kertas Renminbi oleh pemerintah pusat dan penggantiannya dengan koin emas murni.",
            "Kewajiban setiap warga negara untuk menyerahkan telepon pintarnya kepada petugas kasir pasar swalayan.",
            "Ketiadaan akses jaringan internet dan listrik di seluruh wilayah perkotaan besar Tiongkok."
        ],
        "formula": {
            "title": "EKOSISTEM MOBILE PAYMENT TIONGKOK (移动支付生态系统)",
            "latex": "\\mathbf{\\text{Smartphone}} + \\mathbf{\\text{Scan QR Code (扫码)}} + \\mathbf{\\text{WeChat Pay / Alipay}} \\implies \\text{Masyarakat Tanpa Uang Tunai}",
            "legend": "• Penetrasi teknologi finansial inklusif mulai dari mal mewah hingga pedagang kaki lima"
        },
        "hints": {
            "concept": "Teks menyebutkan peran pembayaran seluler lewat scan QR code di WeChat Pay dan Alipay yang sangat populer di segala level transaksi.",
            "execution": "Pilih opsi: Popularitas pembayaran seluler via pemindaian kode QR pada aplikasi WeChat Pay dan Alipay."
        }
    },
    {
        "id": "man-lat-m-23",
        "materi": "JIĀOJÌ & PRAGMATIKA: PEMBERIAN HADIAH TIONGHOA",
        "topic": "Tabu Budaya Memberikan Hadiah Jam Dinding (Sòng Zhōng - 送钟)",
        "stem": "Dalam etika pergaulan masyarakat Tionghoa, memberikan kado ulang tahun berupa 'jam dinding' (*zhōng - 钟*) merupakan TABU BESAR yang sangat dihindari. Alasan kultural dan fonologis di balik larangan tersebut adalah...",
        "correct": "Karena pelafalan kata 'memberi jam dinding' (送钟 - sòng zhōng) berbunyi homofon identik dengan kata 'mengantar jenazah / menghadiri pemakaman' (送终 - sòng zhōng).",
        "distractors": [
            "Karena jam dinding tradisional Tiongkok dipercaya mengandung radiasi jarum magnetik yang merusak memori otak.",
            "Karena masyarakat Tiongkok zaman kuno dilarang menghitung waktu dan hanya boleh berpatokan pada matahari terbit.",
            "Karena harga jam dinding jauh lebih murah dibandingkan buah apel merah segar sehingga dinilai pelit.",
            "Karena warna angka pada jam dinding bertentangan dengan prinsip penanggalan kalender lunar imlek."
        ],
        "formula": {
            "title": "HOMOFON TABU HADIAH TIONGHOA (汉语谐音禁忌：送钟/送终)",
            "latex": "\\mathbf{\\text{送钟 (sòng zhōng / Beri Jam Dinding)}} \\equiv \\mathbf{\\text{送终 (sòng zhōng / Mengantar Kematian Pemakaman)}}",
            "legend": "• Menimbulkan asosiasi psikologis buruk tentang kematian dan akhir usia seseorang"
        },
        "hints": {
            "concept": "Memberi jam dinding (送钟 sòng zhōng) bunyinya sama persis dengan mengantar upacara kematian (送终 sòng zhōng).",
            "execution": "Pilih opsi yang menjelaskan kemiripan bunyi (homofon) antara memberi jam dinding dengan mengantar jenazah/kematian."
        }
    },
    {
        "id": "man-lat-m-24",
        "materi": "JIĀOJÌ & PRAGMATIKA: SIMBOLISME WARNA",
        "topic": "Makna Simbolik Warna Merah (Hóngsè - 红色) vs Warna Putih (Báisè - 白色)",
        "stem": "Pada saat perayaan Tahun Baru Imlek (*Chūnjié*) atau resepsi pernikahan tradisional Tionghoa, masyarakat menghias rumah dengan lentera dan amplop angpao berwarna merah (*hóngsè*), serta menghindari dekorasi berwarna putih (*báisè*). Alasan filosofisnya adalah...",
        "correct": "Warna merah melambangkan keberuntungan, kegembiraan, dan kemakmuran berkah, sedangkan warna putih secara tradisional berkonotasi dengan duka cita dan upacara kematian.",
        "distractors": [
            "Warna merah melambangkan kemarahan dan peperangan kaisar, sedangkan warna putih melambangkan perdamaian internasional.",
            "Warna putih dilarang oleh undang-undang kehutanan Tiongkok karena memantulkan panas sinar matahari yang berlebihan.",
            "Warna merah adalah satu-satunya pigmen pewarna cat yang diproduksi oleh pabrik industri kimia Tiongkok kuno.",
            "Amplop putih hanya boleh digunakan untuk menyimpan surat rahasia dinas intelijen kaisar di istana terlarang."
        ],
        "formula": {
            "title": "SIMBOLISME WARNA BUDAYA TIONGHOA (色彩文化心理)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Merah (红色):}} & \\implies \\text{Hóng (Untung, Bahagia, Sukses, Rezeki)} \\\\ \\mathbf{\\text{Putih (白色):}} & \\implies \\text{Bái (Duka Cita, Pemakaman, Kehampaan Tradisional)} \\end{aligned}",
            "legend": "• Pengaruh semiotika warna yang mengakar kuat dalam ritual perayaan siklus hidup"
        },
        "hints": {
            "concept": "Merah (红色) melambangkan keberuntungan/sukacita/kemakmuran. Putih (白色) berkonotasi perkabungan/kematian.",
            "execution": "Pilih opsi: Merah melambangkan keberuntungan dan kegembiraan, sedangkan putih berkonotasi duka cita."
        }
    },
    {
        "id": "man-lat-m-25",
        "materi": "JIĀOJÌ & BUDAYA: ETIKA BERSULANG MEJA MAKAN",
        "topic": "Etika Bersulang Gān Bēi (干杯) dan Posisi Gelas Penghormatan",
        "stem": "Saat menghadiri jamuan makan malam resmi di Tiongkok dan melakukan prosesi bersulang (*gānbēi - 干杯*) dengan atasan atau orang yang lebih tua, etika posisi bibir gelas yang BENAR sesuai kaidah kesantunan adalah...",
        "correct": "Menurunkan bibir gelas sendiri sedikit lebih rendah daripada bibir gelas atasan/orang yang lebih tua saat membenturkannya perlahan.",
        "distractors": [
            "Mengangkat gelas sendiri setinggi mungkin jauh melampaui kepala atasan sebagai bukti supremasi diri.",
            "Membenturkan gelas dengan sekuat tenaga hingga kedua gelas pecah dan membasahi meja makan.",
            "Membuang isi cairan minuman ke lantai ruangan sebagai bentuk persembahan roh leluhur jamuan.",
            "Menolak menyentuhkan gelas sama sekali dan membalikkan posisi cangkir menjadi tengkurap di hadapan atasan."
        ],
        "formula": {
            "title": "PROTOKOL DUDUK DAN BERSULANG (酒桌敬酒礼仪)",
            "latex": "\\text{Posisi Gelas Sendiri (Bawahan/Junior)} \\mathbf{\\text{ < }} \\text{Posisi Gelas Atasan/Senior} \\implies \\text{Kerendahan Hati (谦逊)}",
            "legend": "• Gestur visual kerendahan hati vertikal yang sangat dihargai dalam perjamuan bisnis Tionghoa"
        },
        "hints": {
            "concept": "Etika bersulang (干杯) di hadapan atasan/orang tua: bibir gelas kita diturunkan sedikit lebih rendah dari gelas pihak yang dihormati.",
            "execution": "Pilih opsi yang menjelaskan memposisikan bibir gelas sendiri sedikit lebih rendah saat bersulang."
        }
    }
]
