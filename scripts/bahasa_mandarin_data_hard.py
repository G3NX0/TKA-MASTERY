# -*- coding: utf-8 -*-
"""
BAHASA MANDARIN - PAKET SOAL LATIHAN SULIT (HARD / HOTS) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / HSK 3+-4 Dasar
Distribusi:
- 8 Butir: Yufa Lanjutan (把-sentence, 被-sentence, 是...的 focus, 连...都, 让/叫/使, 除了...以外, 双趋向补语)
- 10 Butir: Wacana Analitis & Kebudayaan Mendalam (Chunyun, Zhongqiujie, Duanwujie, Diplomasi Panda, Shufa, Siheyuan, Zhongyi)
- 7 Butir: Pragmatika & Komunikasi Bisnis Tingkat Tinggi (Budaya Guanxi, Meja Bundar, Simbol Angka 8 vs 4, Tabu Fanyu, Meishi/Mingpian)
"""

BAHASA_MANDARIN_HARD_ITEMS = [
    {
        "id": "man-lat-h-01",
        "materi": "YUFA LANJUTAN: STRUKTUR DISPOSISI BA (把字句)",
        "topic": "Sintaksis Manipulasi Objek Tertentu (S + 把 + Objek Pasti + V + Komplemen)",
        "stem": "Ibu meminta anaknya merapikan kamar sebelum para tamu tiba. Kalimat struktur disposisi '把' (*Bǎ zì jù*) manakah yang BENAR dan memenuhi seluruh kaidah gramatika Mandarin baku?",
        "correct": "你快把桌子上的书放进书包里去。 (Nǐ kuài bǎ zhuōzi shang de shū fàng jìn shūbāo lǐ qù - segera masukkan buku yang di atas meja itu ke dalam tas ransel).",
        "distractors": [
            "你快把一本书看。 (Struktur 把 dilarang menggunakan objek tak tentu / indefinite seperti 'yī běn shū' dan dilarang predikat verba telanjang tanpa komplemen).",
            "你快把书放在。 (Verba fàng tidak dilengkapi penunjuk lokasi tujuan yang tuntas setelah preposisi zài).",
            "你把快书放在书包里。 (Kata keterangan kuài salah penempatan karena diletakkan di antara partikel bǎ dan objek nomina).",
            "书把你放在书包里去。 (Terbalik peran subjek pelaku dan objek penderita yang dimanipulasi)."
        ],
        "formula": {
            "title": "KAIDAH STRUKTUR KALIMAT BA (「把」字句的核心语法条件)",
            "latex": "\\mathbf{S + \\text{把 (bǎ)} + \\text{Objek Pasti (Definite)} + V + \\text{Komplemen / Unsur Lain}}",
            "legend": "• Syarat mutlak: Objek wajib spesifik (bukan sembarang buku) dan verba TIDAK boleh berdiri telanjang"
        },
        "hints": {
            "concept": "Struktur 把 mensyaratkan: 1) Objek definit/jelas (buku di atas meja), 2) Verba diikuti hasil/arah tindakan (放进书包里去). Tidak boleh objek indefinit (一本书) atau verba telanjang (看).",
            "execution": "Pilih: '你快把桌子上的书放进书包里去。'."
        }
    },
    {
        "id": "man-lat-h-02",
        "materi": "YUFA LANJUTAN: STRUKTUR PASIF BEI (被字句)",
        "topic": "Kalimat Pasif Kerugian Akibat Tindakan Agen Pihak Luar (O + 被 + S + V + Hasil)",
        "stem": "Xiao Ming menceritakan insiden kuenya yang hilang diambil oleh adik laki-lakinya:\n'糟糕！我买的巧克力蛋糕 ( ... ) 了！'\nBentuk kalimat pasif '被' (*Bèi zì jù*) yang TEPAT dan alami mengekspresikan bahwa kue tersebut 'telah dimakan habis oleh adik laki-laki' adalah...",
        "correct": "被弟弟吃完了 (Bèi dìdi chī wán le - kue cokelat telah dimakan habis sampai tandas oleh adik laki-laki).",
        "distractors": [
            "把弟弟吃完了 (Struktur bǎ yang bermakna keliru bahwa kue cokelat yang memakan habis adik laki-laki).",
            "叫弟弟吃了没有 (Bentuk kalimat tanya interogatif yang bertentangan dengan konteks seruan mengeluh zāogāo).",
            "让弟弟吃吃 (Bentuk reduplikasi verba chīchī yang mengindikasikan kegiatan mencicipi santai).",
            "给弟弟在吃 (Struktur progresif yang tidak menandai ketuntasan lenyapnya kue cokelat tersebut)."
        ],
        "formula": {
            "title": "STRUKTUR KALIMAT PASIF BEI (「被」字句受事主语句式)",
            "latex": "\\mathbf{\\text{Objek Penderita (蛋糕)}} + \\mathbf{\\text{被 (bèi)}} + \\mathbf{\\text{Pelaku/Agen (弟弟)}} + \\mathbf{V\\text{-Komplemen (吃完了)}}",
            "legend": "• Lazimnya mengekspresikan peristiwa yang menimbulkan dampak merugikan/tidak diharapkan subjek"
        },
        "hints": {
            "concept": "Pola kalimat pasif: Korban + 被 (bèi) Pelaku + Kata Kerja + Komplemen Hasil: 被弟弟吃完了 (dimakan habis oleh adik).",
            "execution": "Pilih opsi: '被弟弟吃完了 (Bèi dìdi chī wán le)'."
        }
    },
    {
        "id": "man-lat-h-03",
        "materi": "YUFA LANJUTAN: STRUKTUR FOKUS PENEKANAN (SHÌ...DE)",
        "topic": "Penekanan Waktu, Tempat, atau Cara Peristiwa Masa Lampau (是...的)",
        "stem": "Perhatikan percakapan mengenai fakta perjalanan lampau berikut:\nA: '你的这件红色旗袍真漂亮！是在哪儿买的？'\nB: '我 ( ... )。'\nJawaban B yang TEPAT menggunakan struktur penekanan '是...的' (*Shì...de*) untuk menegaskan lokasi pembelian di Shanghai adalah...",
        "correct": "是在上海买的 (Shì zài Shànghǎi mǎi de - menegaskan bahwa lokasi pembelian pakaian qipao tersebut adalah di Shanghai).",
        "distractors": [
            "买在上海了的 (Susunan kata acak yang mencampuradukkan partikel aspek le dengan partikel de penekanan).",
            "去上海买了 (Hanya kalimat narasi lampau biasa tanpa adanya struktur penekanan fokus lokasi informasi).",
            "是上海买旗袍 (Kehilangan partikel penutup 'de' yang merupakan pasangan wajib dari kopula 'shì').",
            "的是在上海买 (Penempatan partikel 'de' di awal kalimat yang menyalahi kaidah gramatika)."
        ],
        "formula": {
            "title": "STRUKTUR FOKUS PENEKANAN (强调句型「是...的」)",
            "latex": "\\mathbf{S + \\text{是 (shì)} + [\\text{Waktu / Tempat / Cara / Pelaku}] + V + \\text{的 (de)}}",
            "legend": "• Digunakan ketika peristiwa masa lampau sudah pasti terjadi, dan pembicara ingin menggarisbawahi detailnya"
        },
        "hints": {
            "concept": "Pertanyaan memakai '是在哪儿买的' (di mana belinya). Jawabannya wajib simetris memakai struktur penekanan 是...的: 是在上海买的.",
            "execution": "Pilih: '是在上海买的 (Shì zài Shànghǎi mǎi de)'."
        }
    },
    {
        "id": "man-lat-h-04",
        "materi": "YUFA LANJUTAN: POLA EKSTREM KONSESIF (LIÁN...DŌU/YĚ)",
        "topic": "Menyatakan Bahkan Kasus Paling Sederhana Pun Berlaku (连...都/也...)",
        "stem": "Soal ujian matematika ini dinilai luar biasa rumit dan sulit. Kalimat yang TEPAT menggunakan struktur '连...都...' (*Lián...dōu...*) untuk menyatakan bahwa 'Bahkan anak paling jenius di kelas pun tidak bisa mengerjakannya' adalah...",
        "correct": "这道题太难了，连我们班最聪明的学生都不会做。 (Zhè dào tí tài nán le, lián wǒmen bān zuì cōngmíng de xuésheng dōu bú huì zuò).",
        "distractors": [
            "这道题太难了，虽然最聪明的学生都不会做。 (Konjungsi suīrán tidak membentuk makna ekstrem bahwa yang terpandai pun gagal).",
            "这道题太难了，不但最聪明的学生都做。 (Búdàn menyiratkan penambahan positif yang bertentangan dengan konteks kegagalan).",
            "这道题太难了，连最聪明的学生都做得很好。 (Kontradiksi logika antara soal yang sangat sulit dengan hasil yang sangat baik).",
            "这道题太难了，都最聪明的学生连不会做。 (Posisi kata lián dan dōu terbalik secara fatal dalam kalimat)."
        ],
        "formula": {
            "title": "STRUKTUR PENEKANAN KASUS EKSTREM (递进强调句「连...都/也...」)",
            "latex": "\\mathbf{\\text{连 (lián) } + \\text{Kasus Ekstrem}} + \\mathbf{\\text{都 / 也 (dōu/yě)} + \\text{Predikat Negatif/Afirmatif}}",
            "legend": "• Menunjukkan bahwa jika kasus terunggul saja tidak mampu, maka anggota biasa lainnya pasti tidak mampu"
        },
        "hints": {
            "concept": "Pola 'bahkan... pun...': 连 (lián) [Kasus Ekstrem] 都/也 (dōu/yě) [Predikat]. Jadi: 连最聪明的学生都不会做.",
            "execution": "Pilih opsi yang menggunakan struktur '连...都不会做'."
        }
    },
    {
        "id": "man-lat-h-05",
        "materi": "YUFA LANJUTAN: KALIMAT KAUSATIF RANG/SHI (让 / 使)",
        "topic": "Penggunaan Verba Kausatif Pembuat Reaksi Emosi (使/让 + Seseorang + Emosi)",
        "stem": "Bacalah kalimat tentang keberhasilan proyek kerja sama berikut:\n'听到这个好消息，大家心里都感到非常激动。'\nBagaimanakah rekonstruksi kalimat di atas menggunakan verba kausatif '使' (*shǐ*) yang TEPAT untuk menyatakan 'Kabar baik ini membuat semua orang merasa sangat terharu dan bersemangat'?",
        "correct": "这个好消息使大家都感到非常激动。 (Zhè ge hǎo xiāoxi shǐ dàjiā dōu gǎndào fēicháng jīdòng - kabar baik ini membuat semua orang terharu/bersemangat).",
        "distractors": [
            "大家都使这个好消息非常激动。 (Terbalik subjek penyebab dengan objek penerima efek emosional).",
            "这个好消息被大家都使激动了。 (Mencampuradukkan partikel pasif bèi dengan verba kausatif shǐ secara tumpang tindih).",
            "使这个好消息大家都非常激动。 (Meletakkan verba kausatif di awal kalimat mendahului stimulus pemicu).",
            "这个好消息把大家都使激动了。 (Mencampuradukkan struktur bǎ dengan shǐ yang merusak struktur sintaksis)."
        ],
        "formula": {
            "title": "STRUKTUR KAUSATIF PENYEBAB (兼语句・使役结构)",
            "latex": "\\mathbf{\\text{Stimulus / Peristiwa}} + \\mathbf{\\text{使 / 让 / 叫 (shǐ/ràng/jiào)}} + \\mathbf{\\text{Penerima Dampak}} + \\mathbf{\\text{Kondisi Psikologis/Hasil}}",
            "legend": "• Kata 'shǐ' lazim digunakan dalam ragam bahasa tulis formal dan eksposisi berita resmi"
        },
        "hints": {
            "concept": "Pola kausatif: Hal Pemicu + 使 (shǐ) + Orang/Pihak + Respon Emosi: 这个好消息使大家都感到非常激动.",
            "execution": "Pilih opsi: '这个好消息使大家都感到非常激动。'."
        }
    },
    {
        "id": "man-lat-h-06",
        "materi": "YUFA LANJUTAN: PENGECUALIAN DAN PENAMBAHAN",
        "topic": "Penggunaan Struktur '除了...以外' (Chúle... Yǐwài)",
        "stem": "Perhatikan dua kalimat bahasa Mandarin berikut:\n1) 除了小明以外，大家 ( A ) 准时参加了会议。(Hanya Xiao Ming yang tidak hadir / Pengecualian eksklusif).\n2) 除了英语以外，他 ( B ) 会说韩语。(Selain bahasa Inggris, ia juga bisa bahasa Korea / Penambahan inklusif).\nKata keterangan penjelas yang TEPAT untuk mengisi posisi ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: 都 (dōu - menandai pengecualian total bahwa selain dia, semuanya hadir), B: 还 / 也 (hái/yě - menandai penambahan kumulatif selain A juga bisa B).",
        "distractors": [
            "A: 还 (hái), B: 都 (dōu) - terbalik esensi antara fungsi pengecualian eksklusif dan penambahan inklusif.",
            "A: 只 (zhǐ), B: 就 (jiù) - susunan partikel yang tidak membentuk pasangan baku dengan chúle.",
            "A: 却 (què), B: 又 (yòu) - partikel adversatif yang salah posisi penempatan dalam klausa.",
            "A: 都 (dōu), B: 都 (dōu) - mengabaikan perbedaan logis antara himpunan minus dan himpunan plus."
        ],
        "formula": {
            "title": "DUALITAS FUNGSI STRUKTUR CHULE...YIWAI (「除了...以外」的互补逻辑)",
            "latex": "\\begin{cases} \\mathbf{\\text{Pengecualian (Minus):}} & \\text{除了 } A \\text{ 以外，} \\dots + \\mathbf{\\text{都 (dōu)}} \\implies \\text{Semua kecuali } A \\\\ \\mathbf{\\text{Penambahan (Plus):}} & \\text{除了 } A \\text{ 以外，} \\dots + \\mathbf{\\text{还 / 也 (hái/yě)}} \\implies \\text{Selain } A \\text{ juga } B \\end{cases}",
            "legend": "• Kata 都 menegaskan eksklusi (hanya A yang tidak); kata 还/也 menegaskan inklusi (A ditambah B)"
        },
        "hints": {
            "concept": "1) Pengecualian (semua hadir kecuali Xiao Ming) berpasangan dengan 都 (dōu). 2) Penambahan (selain Inggris juga bisa Korea) berpasangan dengan 还 (hái) atau 也 (yě).",
            "execution": "Pilih: 'A: 都 (dōu), B: 还 / 也 (hái/yě)'."
        }
    },
    {
        "id": "man-lat-h-07",
        "materi": "YUFA LANJUTAN: KOMPLEMEN ARAH MAJEMUK",
        "topic": "Verba Gerak Terarah Ganda (复合趋向补语: 跑出来 vs 拿进去)",
        "stem": "Seorang anak melihat seekor kucing lucu melompat keluar dari dalam kardus menuju ke arah posisi anak tersebut berdiri. Kalimat yang TEPAT mendeskripsikan arah pergerakan tersebut adalah...",
        "correct": "小猫从箱子里跳出来了。 (Xiǎomāo cóng xiāngzi lǐ tiào chūlai le - anak kucing melompat keluar mendekati posisi pembicara).",
        "distractors": [
            "小猫从箱子里跳出去了。 (Tiào chūqu menandai pergerakan menjauhi posisi pembicara yang bertentangan dengan konteks).",
            "小猫从箱子里跳进来了。 (Tiào jìnlái menandai pergerakan melompat masuk ke dalam wadah pembicara).",
            "小猫从箱子里跳上去了。 (Tiào shàngqu menandai pergerakan melompat naik ke tempat yang lebih tinggi).",
            "小猫从箱子里跳下来去。 (Kombinasi arah ganda yang cacat secara fonologi dan morfologi arah gerak)."
        ],
        "formula": {
            "title": "SISTEM KOMPLEMEN ARAH GANDA (复合趋向补语参照系)",
            "latex": "\\text{Verba} + \\begin{cases} \\mathbf{\\text{出 (chū / Keluar)}} \\\\ \\text{进 (jìn / Masuk)} \\end{cases} + \\begin{cases} \\mathbf{\\text{来 (lái / Mendekati Pembicara)}} \\\\ \\text{去 (qù / Menjauhi Pembicara)} \\end{cases} \\implies \\mathbf{\\text{跳出来 (Melompat keluar mendekat)}}",
            "legend": "• Titik tolak fisik penutur menjadi jangkar absolut dalam pemilihan morfem lái versus qù"
        },
        "hints": {
            "concept": "Kucing melompat keluar (出 - chū) menuju ke arah pembicara (来 - lái), maka komplemen arahnya adalah '跳出来' (tiào chūlai).",
            "execution": "Pilih: '小猫从箱子里跳出来了。'."
        }
    },
    {
        "id": "man-lat-h-08",
        "materi": "YUFA LANJUTAN: POLA KORELASI PROGRESIF",
        "topic": "Struktur Kausalitas Eskalatif Bersyarat (越...越... - Yuè... Yuè...)",
        "stem": "Lengkapilah kalimat peribahasa motivasi belajar bahasa berikut:\n'学外语的时候，你 ( A ) 敢开口说，你的口语表达就 ( B ) 流利。'\nPasangan pola 'semakin... semakin...' yang TEPAT untuk mengisi ( A ) dan ( B ) berturut-turut adalah...",
        "correct": "A: 越 (yuè), B: 越 (yuè) - pola yuè... yuè... yang menandai bahwa semakin berani berbicara, maka akan semakin lancar bicaranya.",
        "distractors": [
            "A: 又 (yòu), B: 又 (yòu) - menandai dua sifat setara simultan pada satu objek (misalnya yòu dà yòu tián).",
            "A: 也 (yě), B: 也 (yě) - penanda kesamaan paralel yang tidak memiliki relasi eskalasi bertingkat.",
            "A: 既 (jì), B: 且 (qiě) - konjungsi sastra penambahan sifat.",
            "A: 越 (yuè), B: 更 (gèng) - mengganti kata yuè kedua dengan gèng yang merusak simetri struktur peribahasa."
        ],
        "formula": {
            "title": "STRUKTUR KORELASI PROGRESIF GANDA (关联结构「越...越...」)",
            "latex": "\\mathbf{\\text{越 (yuè) } + \\text{Derajat Kondisi } A} \\dots \\mathbf{\\text{越 (yuè) } + \\text{Derajat Konsekuensi } B} \\implies \\text{Semakin } A \\dots \\text{ Semakin } B",
            "legend": "• Menunjukkan fungsi korelasi positif linear antara input keberanian dan output kelancaran"
        },
        "hints": {
            "concept": "Pola 'semakin... semakin...': 越 (yuè)... 越 (yuè)... -> 你越敢说，就越流利.",
            "execution": "Pilih opsi: 'A: 越 (yuè), B: 越 (yuè)'."
        }
    },
    {
        "id": "man-lat-h-09",
        "materi": "DOKKAI ANALITIS: FESTIVAL TRADISIONAL CHUNJIE",
        "topic": "Fenomena Arus Mudik Terbesar di Dunia (Chunyun - 春运) dan Budaya Imlek",
        "stem": "Bacalah wacana kebudayaan dan sosial Tiongkok berikut:\n--------------------------------------------------\n春节是 中国人 最重视的 传统节日。每逢 春节，无论 离家 多远，人们 都会 想方设法 回到 家乡 与 亲人 团聚，吃一顿 丰盛的“年夜饭”，这种 现象 被称为“春运”（春节期间的 交通运输）。在 短短 四十天 左右的 时间里，全国 有 数十亿人次 乘坐 火车、飞机、长途汽车 奔波在 回家的 路上。这不仅是 人类历史上 规模最大的 周期性 人口大迁徙，更 深深 体现了 中国人 对“家”和“团圆”的 执着追求。\n--------------------------------------------------\nBerdasarkan wacana di atas, nilai filosofis mendasar apakah yang menjadi daya dorong jutaan masyarakat Tiongkok rela menempuh perjalanan berat selama periode *Chūnyùn*?",
        "correct": "Keterikatan batin yang sangat mendalam terhadap konsep 'Keluarga' (*Jiā*) dan kerinduan sakral untuk berkumpul kembali dalam keutuhan (*Tuányuán*) saat malam tahun baru.",
        "distractors": [
            "Kewajiban dari pemerintah pusat untuk mengikuti parade militer nasional tahunan di kota kelahirannya.",
            "Keinginan untuk menghindari pajak penghasilan tahunan yang hanya ditagihkan kepada warga yang tinggal di kota rantau.",
            "Syarat wajib bagi seluruh warga negara untuk membeli tiket kereta cepat Gaotie bersubsidi separuh harga.",
            "Larangan dari perbankan nasional untuk menggunakan uang digital WeChat Pay selama bulan Februari."
        ],
        "formula": {
            "title": "HAKIKAT FILOSOFIS CHUNYUN (「春运」现象的文化内核)",
            "latex": "\\mathbf{\\text{人口大迁徙 (Migrasi Terbesar)}} \\impliedby \\mathbf{\\text{家 (Jiā / Keluarga) } + \\text{团圆 (Tuányuán / Reuni Utuh)}}",
            "legend": "• Menempatkan kohesi kekerabatan dan bakti leluhur di atas segala hambatan logistik fisik"
        },
        "hints": {
            "concept": "Teks menyatakan: '更 深深 体现了 中国人 对“家”和“团圆”的 执着追求' (menunjukkan pencarian mendalam terhadap 'keluarga' dan 'reuni berkumpul bersama').",
            "execution": "Pilih opsi yang menjelaskan konsep 'Jiā' (keluarga) dan 'Tuányuán' (keutuhan berkumpul bersama)."
        }
    },
    {
        "id": "man-lat-h-10",
        "materi": "DOKKAI ANALITIS: FESTIVAL KUE BULAN (ZHŌNGQIŪJIÉ)",
        "topic": "Makna Simbolik Bulan Purnama dan Kue Bulan (Yùebǐng - 月饼)",
        "stem": "Bacalah teks tradisi festival berikut:\n'农历八月十五是 中国的“中秋节”。在 这一天，月亮 比 平时 更加 圆满、明亮。中国人 习惯 全家人 坐在一起，一边 赏月，一边 品尝 美味的“月饼”。圆圆的 月饼 象征着 家庭的“团圆”与“美满”。在 中国古典文学中，月亮 常常 被用来 寄托 对 远方 亲人和 故乡的 思念之情，正如 著名诗句 所云：“但愿人长久，千里共婵娟”。'\nKutipan puisi klasik karya Su Shi “但愿人长久，千里共婵娟” (*Dàn yuàn rén chángjiǔ, qiānlǐ gòng chánjuān*) dalam wacana Festival Musim Gugur di atas mengandung doa dan harapan tentang...",
        "correct": "Semoga orang-orang yang kita cintai berumur panjang dan senantiasa sehat, sehingga meskipun terpisah jarak ribuan mil, dapat bersama-sama memandang keindahan rembulan yang sama.",
        "distractors": [
            "Harapan agar harga tepung terigu dan kacang merah untuk bahan baku kue bulan tidak mengalami kenaikan harga di pasar.",
            "Doa memohon agar kaisar memberikan kenaikan pangkat jabatan militer kepada para prajurit perbatasan dinasti Song.",
            "Harapan agar cuaca musim gugur tidak menghasilkan embun beku yang dapat merusak tanaman padi gogo.",
            "Peringatan kepada para nelayan laut dalam agar tidak melaut saat air laut mengalami fenomena pasang purnama."
        ],
        "formula": {
            "title": "HERMENEUTIKA PUISI SU SHI (苏轼《水调歌头》文化寓意)",
            "latex": "\\mathbf{\\text{千里共婵娟 (Memandang Rembulan Bersama Meski Terpisah Ribuan Mil)}} \\implies \\text{Doa Panjang Umur \\& Ikatan Batin Jarak Jauh}",
            "legend": "• Rembulan (婵娟 - Chánjuān) menjadi media sublimasi spiritual yang melintasi sekat geografis"
        },
        "hints": {
            "concept": "Puisi 'Dàn yuàn rén chángjiǔ, qiānlǐ gòng chánjuān' bermakna doa agar orang tercinta panjang umur dan dapat memandang keindahan rembulan yang sama meski terpisah ribuan mil.",
            "execution": "Pilih opsi yang menjelaskan doa umur panjang dan memandang keindahan bulan bersama meski terpisah jarak."
        }
    },
    {
        "id": "man-lat-h-11",
        "materi": "DOKKAI ANALITIS: FESTIVAL PERAHU NAGA (DUĀNWǓJIÉ)",
        "topic": "Sejarah Tokoh Qu Yuan dan Tradisi Makan Bakcang (Zòngzi - 粽子)",
        "stem": "Bacalah wacana sejarah budaya berikut:\n--------------------------------------------------\n端午节（农历五月初五）是 为了 纪念 中国古代 伟大的 爱国诗人 屈原（Qū Yuán）。相传 楚国 灭亡时，屈原 怀着 极大的 悲愤 投汨罗江 自尽。沿江的 百姓 听到 消息后，纷纷 划着 龙舟 前往 营救，并把 用 苇叶 包裹的 糯米饭（粽子）投入 江中，希望 鱼虾 吃饱后 不去 伤害 屈原的 身体。从此，端午节“赛龙舟”和“吃粽子”的 习俗便 代代相传。\n--------------------------------------------------\nBerdasarkan teks di atas, apakah tujuan awal masyarakat melemparkan bungkusan beras ketan (*Zòngzi*) ke dalam Sungai Miluo?",
        "correct": "Agar ikan dan udang di sungai memakan beras ketan tersebut dan tidak merusak atau memakan jenazah penyair patriotik Qu Yuan.",
        "distractors": [
            "Sebagai sesaji upacara memohon kepada dewa naga agar menurunkan hujan berkah untuk musim tanam padi.",
            "Untuk menguji kekuatan arus sungai sebelum perlombaan perahu naga skala nasional diselenggarakan.",
            "Sebagai teknik memancing ikan massal yang dipraktikkan oleh para prajurit kerajaan Chu zaman kuno.",
            "Untuk meracuni hewan-hewan buas di dasar sungai agar tidak menyerang perahu para nelayan tradisional."
        ],
        "formula": {
            "title": "ETIOLOGI TRADISI DUANWU (端午节吃粽子的民俗起因)",
            "latex": "\\text{Pelemparan 粽子 (Beras Ketan)} \\implies \\mathbf{\\text{鱼虾吃饱 (Ikan Kenyang)}} \\implies \\mathbf{\\text{不伤屈原躯体 (Melindungi Jenazah Qu Yuan)}}",
            "legend": "• Ekspresi cinta kasih dan penghormatan rakyat jelata terhadap integritas moral tokoh patriotik"
        },
        "hints": {
            "concept": "Teks menyatakan: '把 用 苇叶 包裹的 糯米饭（粽子）投入 江中，希望 鱼虾 吃饱后 不去 伤害 屈原的 身体'.",
            "execution": "Pilih opsi yang menjelaskan agar ikan/udang kenyang sehingga tidak merusak tubuh Qu Yuan."
        }
    },
    {
        "id": "man-lat-h-12",
        "materi": "DOKKAI ANALITIS: DIPLOMASI KENEGARAAN & FAUNA",
        "topic": "Peran Panda Raksasa dalam Hubungan Internasional (Xióngmāo Wàijiāo - 熊猫外交)",
        "stem": "Bacalah teks hubungan internasional berikut:\n'大熊猫是 中国特有的 珍稀动物，被誉为 中国的“国宝”。大熊猫 凭借其 黑白相间的 毛色、圆滚滚的 身材和 憨态可掬的 动作，深受 全世界 人民的 喜爱。新中国 成立以来，中国政府 多次将 大熊猫 作为 代表 和平与 友谊的 国礼 赠送或 租借给 友好国家，这在 国际关系中 被称为“熊猫外交”。大熊猫 不仅 促进了 两国之间的 科学保护 合作，更 成为 连接 中国与 世界 人民心灵的“友谊大使”。'\nPeran diplomatik apakah yang diemban oleh satwa panda raksasa (*Dàxióngmāo*) menurut teks di atas?",
        "correct": "Sebagai 'Duta Persahabatan' dan simbol perdamaian yang mempererat kerja sama konservasi sains serta membangun jembatan emosional antara Tiongkok dan dunia.",
        "distractors": [
            "Sebagai instrumen ancaman sanksi ekonomi terhadap negara-negara yang menolak berinvestasi di industri bambu Tiongkok.",
            "Sebagai objek komoditas perdagangan senjata militer yang ditukarkan dengan teknologi eksplorasi antariksa asing.",
            "Sebagai hewan sirkus pertunjukan komersial yang seluruh keuntungan tiketnya disetorkan ke kas dinas perpajakan luar negeri.",
            "Sebagai spesies pengontrol hama hutan cemara di kebun binatang negara-negara beriklim kutub utara."
        ],
        "formula": {
            "title": "KONSEP DIPLOMASI PANDA (「熊猫外交」的软实力功能)",
            "latex": "\\mathbf{\\text{大熊猫 (Duta Satwa Khas)}} \\implies \\mathbf{\\text{Soft Power (Citra Damai, Sahabat, \\& Kerja Sama Konservasi)}}",
            "legend": "• Menunjukkan efektivitas instrumen diplomasi publik fauna dalam memperkuat citra global"
        },
        "hints": {
            "concept": "Teks menyebutkan panda sebagai: '代表 和平与 友谊的 国礼... 连接 中国与 世界 人民心灵的“友谊大使”' (Duta persahabatan dan simbol perdamaian).",
            "execution": "Pilih opsi yang menjelaskan peran panda sebagai 'Duta Persahabatan' dan simbol perdamaian dunia."
        }
    },
    {
        "id": "man-lat-h-13",
        "materi": "DOKKAI ANALITIS: SENI DAN FILOSOFI AKSARA",
        "topic": "Seni Kaligrafi Tionghoa (Shūfǎ - 书法) dan Empat Harta Kamar Belajar (Wénfáng Sībǎo)",
        "stem": "Dalam seni kaligrafi Tionghoa tradisional (*Shūfǎ*), seorang sastrawan dan kaligrafer wajib memiliki 'Empat Harta Kamar Belajar' (*Wénfáng Sībǎo - 文房四宝*). Manakah empat peranti autentik yang dimaksud?",
        "correct": "Bǐ (Kuas Tulis - 笔), Mò (Tinta Bak Batangan - 墨), Zhǐ (Kertas Xuan Khusus - 纸), dan Yàn (Batu Asahan Tinta - 砚).",
        "distractors": [
            "Bǐ (Pensil Grafit), Chǐ (Penggaris Besi), Xiàngpí (Penghapus Karet), dan Jiāoshuǐ (Lem Kertas Cair).",
            "Chá (Daun Teh Hitam), Jiǔ (Arak Beras Putih), Qín (Kecapi Dawai Guzheng), dan Qí (Papan Catur Weiqi).",
            "Dāo (Pisau Ukir), Mù (Kayu Balok Pinus), Qī (Cat Minyak Warna), dan Bù (Kain Sutra Sulam).",
            "Jīn (Emas Murni), Yín (Perak Kuno), Tóng (Tembaga Kuningan), dan Tiě (Besi Baja Tempa)."
        ],
        "formula": {
            "title": "EMPAT PERANTI SAKRAL KALIGRAFI (文房四宝标准体系)",
            "latex": "\\mathbf{\\text{文房四宝 (Wénfáng Sībǎo)}} \\equiv \\mathbf{[\\text{笔 (Kuas)} + \\text{墨 (Tinta)} + \\text{纸 (Kertas Xuan)} + \\text{砚 (Batu Tinta)}]}",
            "legend": "• Medium fisik yang memancarkan estetika pernapasan batin (Qi) dan aliran energi kuas"
        },
        "hints": {
            "concept": "Empat Harta Kamar Belajar (文房四宝) adalah: Kuas (笔 bǐ), Tinta (墨 mò), Kertas (纸 zhǐ), dan Batu tinta (砚 yàn).",
            "execution": "Pilih opsi: 'Bǐ (笔), Mò (墨), Zhǐ (纸), dan Yàn (砚)'."
        }
    },
    {
        "id": "man-lat-h-14",
        "materi": "DOKKAI ANALITIS: ARSITEKTUR TRADISIONAL",
        "topic": "Filosofi Rumah Pekarangan Empat Sisi Beijing (Sìhéyuàn - 四合院)",
        "stem": "Bacalah teks mengenai warisan arsitektur tradisional Beijing berikut:\n--------------------------------------------------\n“四合院”是 中国北方 尤其是 北京的 传统民居 形式。“四”指 东西南北 四个 方向，“合”指 四面的 房屋 围在一起，形成一个 封闭式的 方形 院落。四合院的 布局 严格 遵循 儒家思想的 长幼尊卑 秩序：正房（北房）坐北朝南，光线 最好，由 家中 辈分最高的 长辈 居住；东西厢房 由 晚辈 居住；倒座房（南房）靠近 大门，通常 作为 客房或 仆人房。中间的 宽敞 庭院 则是 全家人 喝茶、赏花、孩子 嬉戏的 和谐 空间。\n--------------------------------------------------\nBagaimanakah pembagian hak ruang kamar dalam kompleks *Sìhéyuàn* merefleksikan nilai hierarki Konfusianisme (*Rújiā Sīxiǎng*)?",
        "correct": "Kamar utama di sisi utara (*Zhèngfáng*) yang menghadap ke selatan dengan pencahayaan terbaik khusus diperuntukkan bagi tetua/orang tua tertinggi dalam keluarga.",
        "distractors": [
            "Kamar utama di sisi utara dikosongkan permanen sebagai gudang penyimpanan pakan ternak kuda.",
            "Seluruh anak cucu usia termuda diwajibkan tinggal di kamar utama utara, sedangkan orang tua tinggal di luar gerbang.",
            "Kamar yang paling dekat dengan pintu gerbang masuk (*Dàozuòfáng*) adalah kamar sakral bagi kakek tertua.",
            "Pembagian kamar dilakukan secara acak melalui pengundian nomor dadu setiap pergantian musim."
        ],
        "formula": {
            "title": "TATA RUANG ETIKA SIHEYUAN (四合院的儒家伦理空间秩序)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Utara Menghadap Selatan (正房):}} & \\implies \\mathbf{\\text{Tetua / Kepala Keluarga Tertinggi (长辈)}} \\\\ \\text{Sayap Timur \\& Barat (厢房):} & \\implies \\text{Generasi Anak / Cucu (晚辈)} \\\\ \\text{Selatan Dekat Gerbang (倒座房):} & \\implies \\text{Tamu Luar / Penjaga Gerbang} \\end{aligned}",
            "legend": "• Menyelaraskan arah sirkulasi angin/matahari (Fengshui) dengan penegakan bakti kekeluargaan (Xiao)"
        },
        "hints": {
            "concept": "Teks menyatakan: '正房（北房）坐北朝南，光线 最好，由 家中 辈分最高的 长辈 居住' (kamar utama utara dengan cahaya terbaik untuk tetua tertinggi).",
            "execution": "Pilih opsi: Kamar utama utara (Zhengfang) menghadap selatan diperuntukkan bagi tetua tertinggi keluarga."
        }
    },
    {
        "id": "man-lat-h-15",
        "materi": "DOKKAI ANALITIS: KESEHATAN DAN PENGOBATAN ALAMI",
        "topic": "Filosofi Yin-Yang dan Keseimbangan Holistik dalam Pengobatan Tradisional Tionghoa (Zhōngyī)",
        "stem": "Bacalah teks wacana kesehatan berikut:\n'中医（中国传统医学）拥有 数千年的 实践经验，其 理论基础 建立在“阴阳五行”和“天人合一”的 哲学观念上。中医 认为，人体的 健康 取决于 体内“气血”的 通畅和“阴阳”的 动态平衡。生病是 身体 内部 平衡 失调的 表现，例如“火气过大（阳盛）”或“体质虚寒（阴盛）”。因此，中医 治疗 不仅针对 局部的 症状，更 注重 调理 全身的 免疫机能，通过 中草药、针灸、拔罐、推拿等 综合疗法，帮助 身体 恢复 自然的 和谐状态。'\nPrinsip fundamental apakah yang membedakan pendekatan Pengobatan Tradisional Tionghoa (*Zhōngyī*) dari pengobatan simptomatik biasa menurut wacana di atas?",
        "correct": "Zhongyi memandang tubuh secara holistik dan menitikberatkan pada pemulihan keseimbangan dinamis Yin-Yang serta kelancaran energi Qi/darah di seluruh tubuh, bukan sekadar mematikan gejala lokal semata.",
        "distractors": [
            "Zhongyi menolak penggunaan bahan alami tumbuhan obat dan hanya mengandalkan operasi pembedahan organ secara massal.",
            "Zhongyi mewajibkan seluruh pasien menjalani puasa makan makanan padat selama 365 hari penuh tanpa minum air.",
            "Zhongyi memandang penyakit semata-mata sebagai kutukan dewa petir yang hanya bisa disembuhkan dengan tarian magis.",
            "Zhongyi hanya boleh dipraktikkan kepada pasien anak-anak balita yang belum pernah mengonsumsi obat kimia modern."
        ],
        "formula": {
            "title": "PARADIGMA HOLISTIK PENGOBATAN TRADISIONAL ZHONGYI (中医学的整体观)",
            "latex": "\\mathbf{\\text{Kesehatan Manusia}} \\equiv \\mathbf{\\text{Keseimbangan Dinamis 阴阳 (Yīn-Yáng) } + \\text{Kelancaran 气血 (Qì-Xuè)}}",
            "legend": "• Pendekatan integratif sistemik yang menyelaraskan mikrokosmos tubuh dengan ritme makrokosmos alam"
        },
        "hints": {
            "concept": "Teks menekankan: kesehatan bergantung pada keseimbangan Yin-Yang dan kelancaran Qi/darah, pengobatan berfokus pada penyelarasan seluruh tubuh (整体调理), bukan cuma gejala lokal.",
            "execution": "Pilih opsi yang menjelaskan pendekatan holistik keseimbangan Yin-Yang dan kelancaran Qi di seluruh tubuh."
        }
    },
    {
        "id": "man-lat-h-16",
        "materi": "DOKKAI ANALITIS: STRATEGI EKONOMI MODERN",
        "topic": "Konsep Inisiatif Sabuk dan Jalan (Yīdài Yīlù - 一带一路)",
        "stem": "Bacalah kutipan analisis ekonomi kontemporer berikut:\n--------------------------------------------------\n“一带一路”倡议（丝绸之路经济带和 21世纪海上丝绸之路）自 2013年 提出以来，旨在 通过 基础设施建设、贸易畅通和 资金融通，深化 中国与 亚欧非等 沿线各国的 互联互通。这一 倡议 强调“共商、共建、共享”的 原则，不仅 帮助 发展中国家 建设了 高速铁路、港口和 电网，推动了 当地 经济发展，也为 全球 贸易增长 提供了 新的 动力。印尼的 雅万高铁（Whoosh）便是 这一 合作框架下的 标志性 旗舰项目。\n--------------------------------------------------\nPrinsip kerja sama apakah yang menjadi pilar utama pelaksanaan inisiatif *Yīdài Yīlù* (Belt and Road Initiative)?",
        "correct": "Gòng shāng, gòng jiàn, gòng xiǎng (共商、共建、共享 - Konsultasi Bersama, Pembangunan Bersama, dan Berbagi Manfaat Bersama).",
        "distractors": [
            "Dú lì, zì zhǔ, fēng bì (Independen, berdiri sendiri, dan menutup akses dari negara luar).",
            "Mǎimài, shōu gòu, jiān bīng (Jual beli, pengambilalihan aset, dan penggabungan paksa korporasi).",
            "Dān biān, qiǎng zhì, zhì cái (Unilateral sepihak, pemaksaan kehendak, dan penjatuhan sanksi embargo).",
            "Zhēng duó, kòng zhì, lǒng duàn (Perebutan sumber daya, pengendalian kekuasaan, dan monopoli pasar tertutup)."
        ],
        "formula": {
            "title": "TRILOGI PRINSIP BELT AND ROAD (「一带一路」三大合作原则)",
            "latex": "\\mathbf{\\text{一带一路 (BRI)}} \\implies \\mathbf{[\\text{共商 (Konsultasi Bersama)} + \\text{共建 (Bangun Bersama)} + \\text{共享 (Nikmati Bersama)}]}",
            "legend": "• Kerangka multilateralisme inklusif yang melandasi proyek infrastruktur global seperti Kereta Cepat Whoosh"
        },
        "hints": {
            "concept": "Teks menyatakan: '这一 倡议 强调“共商、共建、共享”的 原则' (Konsultasi bersama, pembangunan bersama, berbagi manfaat bersama).",
            "execution": "Pilih opsi: '共商、共建、共享 (Gòng shāng, gòng jiàn, gòng xiǎng)'."
        }
    },
    {
        "id": "man-lat-h-17",
        "materi": "DOKKAI ANALITIS: DEMOGRAFI & KEBIJAKAN SOSIAL",
        "topic": "Penuaan Populasi di Tiongkok dan Kebijakan Tiga Anak (Sānhái Zhèngcè - 三孩政策)",
        "stem": "Bacalah wacana demografi Tiongkok berikut:\n--------------------------------------------------\n随着 经济社会的 快速发展，中国面临着“人口老龄化”加剧和 出生率下降的 严峻挑战。为了 优化 人口结构，促进 人口长期均衡发展，中国政府 继“全面两孩政策”之后，正式 出台了“三孩生育政策”，并 推出了一系列 配套支持措施，如 降低 育儿教育成本、延长 产假、完善 普惠托育服务等。然而，由于 城市 生活成本高、年轻人的 就业压力大，如何 真正 提高 年轻夫妇的 生育意愿，依然是一个 复杂的 社会课题。\n--------------------------------------------------\nTantangan nyata apakah yang masih membayangi efektivitas implementasi kebijakan 'Tiga Anak' (*Sānhái Zhèngcè*) di kawasan perkotaan Tiongkok?",
        "correct": "Tingginya biaya hidup di perkotaan dan beratnya tekanan persaingan kerja yang membuat minat generasi muda untuk memiliki banyak anak tetap rendah.",
        "distractors": [
            "Ketiadaan fasilitas rumah sakit dan tenaga bidan terlatih di seluruh wilayah perkotaan provinsi besar.",
            "Kewajiban bagi setiap keluarga untuk menyekolahkan anak-anaknya ke universitas di luar negeri sejak usia balita.",
            "Larangan dari kementerian tenaga kerja bagi kaum perempuan untuk bekerja di luar rumah setelah menikah.",
            "Penolakan dari generasi kakek nenek lansia untuk membantu merawat cucu-cucu di rumah hunian."
        ],
        "formula": {
            "title": "ANALISIS FAKTOR FERTILITAS PERKOTAAN (生育意愿的影响机制)",
            "latex": "\\begin{cases} \\text{Kebijakan Dukungan: Tiga Anak + Subsidi} \\\\ \\mathbf{\\text{Kendala Nyata: 生活成本高 (Biaya Hidup Tinggi) } + \\text{就业压力大 (Tekanan Kerja)}} \\end{cases} \\implies \\text{Minat Lahir Rendah}",
            "legend": "• Menunjukkan kompleksitas struktural biaya ekonomi pengasuhan anak (child-rearing cost)"
        },
        "hints": {
            "concept": "Teks menyebutkan: '由于 城市 生活成本高、年轻人的 就业压力大，如何 真正 提高 年轻夫妇的 生育意愿，依然是一个 复杂的 社会课题'.",
            "execution": "Pilih opsi yang menyebutkan tingginya biaya hidup perkotaan dan beratnya tekanan kerja generasi muda."
        }
    },
    {
        "id": "man-lat-h-18",
        "materi": "DOKKAI ANALITIS: SASTRA FABEL KUNO TIONGHOA",
        "topic": "Fabel Kodok dalam Tempurung Sumur (Jǐng Dǐ Zhī Wā - 井底之蛙)",
        "stem": "Bacalah fabel alegori klasik berikut:\n'一口 废井里 住着一只 青蛙。它 对 偶尔路过的 东海大鳖 炫耀说：“你看我 多快乐！独占这口 浅井，高兴了 跳跳，累了 就在 井壁边 休息，没有 谁比我 更自由！”大海鳖 听了，便向 青蛙 描述 大海的 浩瀚：“海的 广大，何止 千里；海的 深度，何止 万丈。洪水 不能 使它增多，大旱 不能 使它减少。这才是 真正的 快乐呢！”青蛙 听了 惊呆了，方才 感到 自己的 渺小。'\nAmanat moral dari peribahasa fabel 'Jǐng Dǐ Zhī Wā' (井底之蛙) di atas adalah...",
        "correct": "Menyindir orang yang memiliki wawasan sempit dan pengetahuan terbatas namun bersikap sombong serta merasa dirinya paling hebat karena belum melihat luasnya dunia.",
        "distractors": [
            "Mengajarkan bahwa kodok harus belajar menyelam di laut lepas agar tidak dimangsa oleh burung elang.",
            "Memerintahkan masyarakat untuk tidak membuang sampah plastik ke dalam sumur tua pedesaan.",
            "Menjelaskan bahwa air laut rasanya asin karena mengandung mineral garam yang terbawa banjir bandang.",
            "Menganjurkan agar penyu laut pindah tempat tinggal ke sumur pedesaan demi mencari ketenangan hidup."
        ],
        "formula": {
            "title": "ALUSI CHENGYU FABEL KODOK DALAM SUMUR (寓言成语「井底之蛙」)",
            "latex": "\\mathbf{\\text{井底之蛙 (Kodok di Dasar Sumur)}} \\equiv \\mathbf{\\text{目光短浅、盲目自大 (Wawasan Sangat Sempit \\& Jumawa)}}",
            "legend": "• Pelajaran kerendahan hati epistemik di hadapan keluasan cakrawala samudra ilmu pengetahuan"
        },
        "hints": {
            "concept": "Peribahasa 井底之蛙 (kodok dalam tempurung/sumur) menyindir orang yang picik/berwawasan sempit dan sombong karena belum melihat dunia luar yang luas.",
            "execution": "Pilih opsi yang menyindir orang berwawasan sempit namun sombong merasa paling hebat."
        }
    },
    {
        "id": "man-lat-h-19",
        "materi": "JIĀOJÌ BISNIS: KONSEP RELASI JEJARING (GUĀNXÌ - 关系)",
        "topic": "Etika Budaya Hubungan Relasi Sosial dan Bisnis Tionghoa",
        "stem": "Dalam dunia pergaulan bisnis di Tiongkok, konsep *Guānxì* (关系) memegang peranan yang sangat penting. Apakah makna hakiki dari *Guānxì* dalam konteks profesional yang beretika?",
        "correct": "Jejaring relasi interpersonal yang dibangun atas dasar saling percaya (*xìnrèn*), resiprositas timbal balik, dan pemeliharaan persahabatan jangka panjang.",
        "distractors": [
            "Praktik suap menyuap uang tunai ilegal di bawah meja untuk memenangkan tender lelang proyek proyek pemerintah.",
            "Kewajiban menandatangani kontrak kerja tanpa boleh membaca pasal-pasal perlindungan hukum tenaga kerja.",
            "Sistem kasta sosial kuno yang melarang kerja sama perdagangan antara dua marga keluarga yang berbeda.",
            "Perjanjian monopoli pasar sepihak yang memaksa mitra bisnis asing menyerahkan seluruh aset pabriknya."
        ],
        "formula": {
            "title": "DINAMIKA SOSIAL BUDAYA GUANXI (中国式关系网的伦理内核)",
            "latex": "\\mathbf{\\text{关系 (Guānxì)}} \\equiv \\mathbf{[\\text{信任 (Xìnrèn / Kepercayaan)} + \\text{人情 (Rénqíng / Empati)} + \\text{长期合作 (Jangka Panjang)}]}",
            "legend": "• Modal sosial (social capital) yang menuntut investasi waktu, ketulusan, dan integritas reputasi"
        },
        "hints": {
            "concept": "Guanxi secara etis adalah jejaring relasi sosial yang dibangun berlandaskan saling percaya (xìnrèn), saling menghargai, dan komitmen persahabatan jangka panjang.",
            "execution": "Pilih opsi: Jejaring relasi interpersonal berlandaskan saling percaya, resiprositas, dan persahabatan jangka panjang."
        }
    },
    {
        "id": "man-lat-h-20",
        "materi": "JIĀOJÌ BISNIS: ETIKA MEJA BUNDAR MAKAN MALAM",
        "topic": "Penentuan Posisi Duduk Kehormatan (Zhǔwèi - 主位) di Meja Bundar",
        "stem": "Saat menghadiri jamuan makan malam resmi di Tiongkok dengan meja bundar (*yuánzhuō*), di manakah letak 'Posisi Tempat Duduk Kehormatan Utama' (*Zhǔwèi - 主位*) yang diperuntukkan bagi tamu paling terhormat atau tuan rumah kepala?",
        "correct": "Tepat berada di posisi menghadap ke arah pintu masuk utama ruangan (*zhèng duì dà mén*), atau posisi paling tengah di sisi dalam.",
        "distractors": [
            "Tepat berada di sudut tersembunyi di dekat pintu kamar kecil toilet agar mudah mencuci tangan.",
            "Berada di kursi yang membelakangi pintu masuk sehingga wajah tamu tidak terlihat oleh pelayan.",
            "Berada di samping meja kasir pembayaran agar bisa langsung mengawasi tagihan nota makanan.",
            "Bebas di sembarang kursi tanpa ada aturan urutan kehormatan dalam jamuan perjamuan Tionghoa."
        ],
        "formula": {
            "title": "PROTOKOL TEMPAT DUDUK JAMUAN (中餐圆桌座次礼仪)",
            "latex": "\\mathbf{\\text{主位 (Zhǔwèi / Kursi Utama)}} \\equiv \\mathbf{\\text{正对大门 (Tepat Menghadap Pintu Masuk)}} \\quad \\& \\quad \\text{Kanan 主位: Tamu Utama Ke-1}",
            "legend": "• Menunjukkan status penghormatan tertinggi dan penguasaan visual terhadap seluruh dinamika ruangan"
        },
        "hints": {
            "concept": "Kursi kehormatan utama (主位 - zhǔwèi) di meja bundar perjamuan Tionghoa selalu berada di posisi yang menghadap langsung ke arah pintu masuk ruangan.",
            "execution": "Pilih opsi yang menyebutkan posisi tepat menghadap ke arah pintu masuk utama ruangan."
        }
    },
    {
        "id": "man-lat-h-21",
        "materi": "JIĀOJÌ & BUDAYA: TABU KULINER MARITIM",
        "topic": "Tabu Membalikkan Badan Ikan saat Makan di Pesisir Nelayan (Fān Yú - 翻鱼)",
        "stem": "Saat menyantap hidangan ikan utuh (*tiáoyú*) bersama para nelayan atau masyarakat pesisir di Tiongkok selatan, mengapa DILARANG KERAS membalikkan badan ikan (*fān yú - 翻鱼*) setelah menghabiskan daging bagian atas?",
        "correct": "Karena tindakan membalik ikan (*fān yú*) berkonotasi buruk menyerupai peristiwa 'perahu nelayan yang terbalik di tengah lautan' (*fān chuán - 翻船*).",
        "distractors": [
            "Karena tulang punggung ikan mengandung duri beracun yang dapat meledak jika dibalik secara mendadak.",
            "Karena sisik ikan bagian bawah mengandung nilai sejarah arkeologi dinasti kekaisaran yang harus diawetkan.",
            "Karena kuah kecap ikan di dasar piring akan menguap habis jika terkena udara meja makan.",
            "Karena koki restoran akan mendenda pelanggan yang tidak mampu mengangkat tulang ikan dengan satu sumpit."
        ],
        "formula": {
            "title": "TABU MARITIM MEMBALIK IKAN (渔民饮食禁忌「翻鱼/翻船」)",
            "latex": "\\mathbf{\\text{翻鱼 (Fān yú / Membalik Ikan)}} \\equiv \\mathbf{\\text{翻船 (Fān chuán / Kapal Karam Terbalik di Laut)}} \\implies \\text{TABU BESAR}",
            "legend": "• Cara benar: Angkat kerangka tulang ikan dari atas tanpa membalikkan badan ikannya"
        },
        "hints": {
            "concept": "Di kalangan nelayan pesisir Tiongkok, membalik ikan (翻鱼) dihindari karena berasosiasi dengan kapal terbalik di laut (翻船).",
            "execution": "Pilih opsi yang mengaitkan tindakan membalik ikan dengan kapal/perahu nelayan yang terbalik di laut."
        }
    },
    {
        "id": "man-lat-h-22",
        "materi": "JIĀOJÌ & BUDAYA: NUMEROLOGI TIONGHOA",
        "topic": "Simbolisme Angka 8 (Bā) Keberuntungan vs Angka 4 (Sì) Tabu",
        "stem": "Masyarakat Tionghoa sangat menggemari angka 8 (*bā*) untuk nomor pelat kendaraan atau nomor telepon, namun sangat menghindari angka 4 (*sì*). Landasan fonologis dan kultural dari fenomena ini adalah...",
        "correct": "Angka 8 (*bā*) berima fonetis mirip dengan kata makmur/sukses rezeki (*fā - 发财*), sedangkan angka 4 (*sì*) berbunyi sangat mirip dengan kata kematian (*sǐ - 死*).",
        "distractors": [
            "Angka 8 adalah lambang dari 8 kaisar pertama Tiongkok, sedangkan angka 4 adalah lambang dari 4 musim dingin yang beku.",
            "Angka 4 dilarang oleh kalender astronomi bulan imlek karena menyebabkan gerhana matahari total.",
            "Angka 8 melambangkan jumlah arah mata angin kompas, sedangkan angka 4 dilarang dalam ilmu ukur matematika kuno.",
            "Angka 8 ditetapkan oleh kementerian perdagangan sebagai tarif minimum bunga pinjaman modal usaha."
        ],
        "formula": {
            "title": "NUMEROLOGI FONETIK TIONGHOA (数字文化心理学)",
            "latex": "\\begin{cases} \\mathbf{\\text{Angka 8 (bā):}} & \\approx \\mathbf{\\text{发 (fā / Makmur, Kaya, Berjaya)}} \\implies \\text{Sangat Dicari} \\\\ \\mathbf{\\text{Angka 4 (sì):}} & \\approx \\mathbf{\\text{死 (sǐ / Mati, Celaka)}} \\implies \\text{Tabu Dihindari (Lantai 4 ditiadakan)} \\end{cases}",
            "legend": "• Homofon vokal konsonan yang membentuk perilaku konsumsi dan arsitektur gedung pencakar langit"
        },
        "hints": {
            "concept": "Angka 8 (bā) bunyinya mirip 发 (fā / makmur kaya). Angka 4 (sì) bunyinya mirip 死 (sǐ / mati).",
            "execution": "Pilih opsi: Angka 8 berima mirip kata makmur (fā) dan angka 4 mirip kata mati (sǐ)."
        }
    },
    {
        "id": "man-lat-h-23",
        "materi": "JIĀOJÌ BISNIS: ETIKA PERTUKARAN KARTU NAMA",
        "topic": "Protokol Penyerahan dan Penerimaan Kartu Nama (Míngpiàn - 名片)",
        "stem": "Saat memperkenalkan diri dalam pertemuan bisnis bilateral di Tiongkok, tata cara yang BENAR dan beretika tinggi dalam menyerahkan dan menerima kartu nama (*Míngpiàn - 名片*) adalah...",
        "correct": "Menyerahkan dan menerima dengan menggunakan kedua belah tangan (*shuāngshǒu*), dengan posisi teks menghadap ke arah lawan bicara, lalu membacanya sejenak dengan penuh hormat.",
        "distractors": [
            "Menyerahkan kartu nama dengan tangan kiri sambil memasukkan tangan kanan ke dalam saku celana depan.",
            "Langsung memasukkan kartu nama mitra bisnis ke dalam saku celana belakang tanpa membaca nama dan jabatannya.",
            "Menuliskan harga penawaran diskon produk langsung di atas foto kartu nama rekan kerja menggunakan spidol permanen.",
            "Menyelipkan kartu nama ke dalam lipatan taplak meja makan sebelum bersalaman dengan mitra usaha."
        ],
        "formula": {
            "title": "PROTOKOL MINGPIAN TIONGHOA (商务名片交换礼仪)",
            "latex": "\\text{Kartu Nama} \\implies \\mathbf{\\text{双手递交 (Serah 2 Tangan)}} + \\mathbf{\\text{双手接收 (Terima 2 Tangan)}} + \\mathbf{\\text{正面朝向对方 (Teks Hadap Mitra)}}",
            "legend": "• Menunjukkan rasa hormat mutlak terhadap status profesional dan institusi mitra"
        },
        "hints": {
            "concept": "Kartu nama (名片) wajib diserahkan dan diterima dengan kedua tangan (双手), tulisan menghadap lawan bicara, dan dibaca teliti.",
            "execution": "Pilih opsi: Menyerahkan dan menerima dengan kedua belah tangan, teks menghadap lawan bicara, dan dibaca sejenak dengan hormat."
        }
    },
    {
        "id": "man-lat-h-24",
        "materi": "JIĀOJÌ: ETIKA MENOLAK PEMBERIAN DENGAN SOPAN",
        "topic": "Tradisi Menolak Santun Sebelum Menerima (Cítuì - 辞退 / 推辞)",
        "stem": "Dalam etika tradisional Tionghoa, ketika menerima angpao dari kerabat yang lebih tua atau hadiah berharga dari rekan bisnis, sikap komunikasi spontan yang paling lumrah dan dianggap santun (*Cítuì*) adalah...",
        "correct": "Menolak secara halus dengan santun sebanyak satu atau dua kali terlebih dahulu sebelum akhirnya menerimanya dengan penuh rasa terima kasih dan kedua belah tangan.",
        "distractors": [
            "Langsung merebut amplop angpao dengan cepat sambil langsung membuka isinya di depan kerabat yang memberi.",
            "Melemparkan kembali amplop ke wajah pemberi sambil berteriak marah karena merasa dihina secara finansial.",
            "Menuntut agar nominal uang di dalam amplop ditambah dua kali lipat sesuai kurs mata uang asing terbaru.",
            "Menyuruh anak balita untuk mengambil uang tunai tersebut dan menyembunyikannya di bawah karpet ruangan."
        ],
        "formula": {
            "title": "PRAGMATIK KERENDAHAN HATI PENERIMAAN HADIAH (推让之礼)",
            "latex": "\\text{Pemberian Hadiah/Angpao} \\xrightarrow{\\text{Etika Sopan}} \\mathbf{\\text{推辞一两次 (Menolak Halus 1-2 Kali)}} \\xrightarrow{\\text{Akhirnya}} \\mathbf{\\text{双手道谢接受 (Terima 2 Tangan)}}",
            "legend": "• Menghindari kesan rakus materi dan menunjukkan pengendalian diri yang beradab"
        },
        "hints": {
            "concept": "Tradisi kesantunan Tionghoa (推辞 tuīcí): menolak secara halus 1-2 kali sebelum menerima dengan ucapan terima kasih dan kedua tangan.",
            "execution": "Pilih opsi: Menolak secara halus dengan santun 1-2 kali terlebih dahulu sebelum akhirnya menerima dengan terima kasih."
        }
    },
    {
        "id": "man-lat-h-25",
        "materi": "DOKKAI ANALITIS: SEJARAH PENANGGALAN LUNAR",
        "topic": "Siklus 12 Shio Binatang (Shí'èr Shēngxiào - 十二生肖)",
        "stem": "Sistem zodiak tradisional Tionghoa (*Shí'èr Shēngxiào - 十二生肖*) mengaitkan tahun kelahiran dengan dua belas binatang perlambang secara berurutan. Binatang pertama yang membuka urutan siklus shio dan binatang terakhir yang menutup siklus shio berturut-turut adalah...",
        "correct": "Binatang pertama adalah Tikus (Shǔ - 鼠), dan binatang penutup kedua belas adalah Babi (Zhū - 猪).",
        "distractors": [
            "Binatang pertama adalah Naga (Lóng - 龙), dan binatang penutup adalah Harimau (Hǔ - 虎).",
            "Binatang pertama adalah Kerbau (Niú - 牛), dan binatang penutup adalah Anjing (Gǒu - 狗).",
            "Binatang pertama adalah Kuda (Mǎ - 马), dan binatang penutup adalah Kelinci (Tù - 兔).",
            "Binatang pertama adalah Monyet (Hóu - 猴), dan binatang penutup adalah Ayam (Jī - 鸡)."
        ],
        "formula": {
            "title": "URUTAN KRONOLOGIS DUA BELAS SHIO (十二生肖循环序列表)",
            "latex": "\\mathbf{1. \\text{ 鼠 (Tikus)}} \\to 2. \\text{ 牛} \\to 3. \\text{ 虎} \\to 4. \\text{ 兔} \\to 5. \\text{ 龙} \\to 6. \\text{ 蛇} \\to 7. \\text{ 马} \\to 8. \\text{ 羊} \\to 9. \\text{ 猴} \\to 10. \\text{ 鸡} \\to 11. \\text{ 狗} \\to \\mathbf{12. \\text{ 猪 (Babi)}}",
            "legend": "• Siklus duadesimal kalender lunar yang menjadi jangkar perhitungan astrologi Tionghoa"
        },
        "hints": {
            "concept": "Urutan 12 shio dimulai dari Tikus (鼠 - Shǔ) dan diakhiri oleh Babi (猪 - Zhū).",
            "execution": "Pilih opsi: Binatang pertama adalah Tikus (鼠), dan binatang terakhir adalah Babi (猪)."
        }
    }
]
