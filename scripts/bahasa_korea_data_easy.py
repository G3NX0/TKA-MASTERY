# -*- coding: utf-8 -*-
"""
BAHASA KOREA - PAKET SOAL LATIHAN DASAR (EASY) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / TOPIK I Level 1-2 (CEFR A1-A2)
Distribusi:
- 8 Butir: Partikel Dasar (은/는, 이/가, 을/를, 에, 에서, 와/과/하고, 의, 도)
- 9 Butir: Konjugasi Bentuk Akhiran Kalimat & Waktu (-ㅂ니다/-습니다, -아요/-어요, -았/었어요, 안/-지 않다)
- 8 Butir: Sistem Bilangan (Sino-Korea vs Asli Korea + Kata Penggolong 개, 명, 권, 잔, 마리, 대)
"""

BAHASA_KOREA_EASY_ITEMS = [
    {
        "id": "kor-lat-e-01",
        "materi": "TATA BAHASA: PARTIKEL PENANDA TOPIK (은/는)",
        "topic": "Penentuan Partikel Penanda Topik Kalimat Berdasarkan Konsonan/Vokal Akhir",
        "stem": "Dalam sesi perkenalan diri di depan kelas bahasa Korea:\n'안녕하세요? 저( ... ) 인도네시아에서 온 바유입니다. 제 친구( ... ) 한국 사람입니다.'\nPasangan partikel penanda topik (은/는) yang TEPAT untuk melengkapi subjek '저' (akhiran vokal) dan '제 친구' (akhiran vokal) adalah...",
        "correct": "는 / 는 (karena kedua nomina berakhiran vokal tanpa batchim: 저 + 는, 친구 + 는).",
        "distractors": [
            "은 / 은 (keliru menggunakan 은 yang khusus untuk kata berakhiran konsonan dengan batchim).",
            "는 / 은 (kesalahan mengasumsikan kata 친구 berakhiran konsonan).",
            "은 / 는 (kesalahan mengasumsikan kata ganti 저 memiliki batchim).",
            "이 / 가 (partikel penanda subjek gramatikal, bukan partikel penanda topik perkenalan umum)."
        ],
        "formula": {
            "title": "PARTIKEL TOPIK: 은/는 (TOPIC MARKER)",
            "latex": "\\text{Konsonan (Batchim)} + \\mathbf{은} \\quad \\leftrightarrow \\quad \\text{Vokal (Tanpa Batchim)} + \\mathbf{는}",
            "legend": "• 저 (vokal ㅓ) $\\rightarrow$ 저는 (Saya adalah...).<br>• 친구 (vokal ㅜ) $\\rightarrow$ 친구는 (Sahabat saya adalah...).<br>• Berfungsi memperkenalkan topik utama atau membandingkan kontras."
        },
        "hints": {
            "concept": "Partikel topik '은/는' digunakan untuk memperkenalkan topik utama pembicaraan. Aturan fonologis: kata berakhiran vokal (tanpa batchim) menggunakan '는' (저 -> 저는; 친구 -> 친구는), sedangkan kata berakhiran konsonan (dengan batchim) menggunakan '은'.",
            "execution": "저 (vokal) -> 는; 친구 (vokal) -> 는. Pasangan tepat: 는 / 는."
        }
    },
    {
        "id": "kor-lat-e-02",
        "materi": "TATA BAHASA: PARTIKEL PENANDA OBJEK (을/를)",
        "topic": "Pemilihan Partikel Objek Penderita Sesuai Keberadaan Konsonan Akhir (Batchim)",
        "stem": "Seorang siswa menceritakan aktivitas belajarnya di perpustakaan:\n'저는 도서관에서 한국어 책( ... ) 읽고, 음악( ... ) 듣습니다.'\nPasangan partikel penanda objek (을/를) yang TEPAT untuk kata benda '책' (buku, ber-batchim ㄱ) dan '음악' (musik, ber-batchim ㄱ) adalah...",
        "correct": "을 / 을 (kedua kata benda berakhiran konsonan/batchim sehingga wajib diikuti partikel objek 을).",
        "distractors": [
            "를 / 를 (keliru menggunakan 를 yang diperuntukkan bagi kata berakhiran vokal).",
            "을 / 를 (kesalahan menganggap kata benda 음악 berakhiran vokal).",
            "를 / 을 (kesalahan menganggap kata benda 책 berakhiran vokal).",
            "에 / 에서 (partikel penunjuk tempat atau waktu, bukan penanda objek penderita kata kerja transitif)."
        ],
        "formula": {
            "title": "PARTIKEL OBJEK: 을/를 (OBJECT MARKER)",
            "latex": "\\text{Kata ber-Batchim} + \\mathbf{을} \\quad \\leftrightarrow \\quad \\text{Kata tanpa Batchim} + \\mathbf{를}",
            "legend": "• 책 (ada batchim ㄱ) $\\rightarrow$ 책을 읽다.<br>• 음악 (ada batchim ㄱ) $\\rightarrow$ 음악을 듣다.<br>• Keduanya mewajibkan partikel '을'."
        },
        "hints": {
            "concept": "Partikel penanda objek langsung (을/를) dilekatkan pada kata benda yang dikenai tindakan verba transitif. Jika kata benda berakhiran konsonan (memiliki batchim), gunakan '을' (책 -> 책을; 음악 -> 음악을). Jika berakhiran vokal, gunakan '를'.",
            "execution": "책 (batchim) -> 을; 음악 (batchim) -> 을. Pilihan tepat: 을 / 을."
        }
    },
    {
        "id": "kor-lat-e-03",
        "materi": "TATA BAHASA: PARTIKEL TEMPAT '에' VS '에서'",
        "topic": "Distingsi Lokasi Keberadaan/Arah (에) vs Lokasi Terjadinya Aktivitas Dinamis (에서)",
        "stem": "Dua mahasiswa membicarakan kegiatan harian di kampus:\n'수진 씨는 지금 학생식당( ... ) 점심을 먹고 있습니다. 그리고 오후에는 도서관( ... ) 갑니다.'\nPasangan partikel tempat yang TEPAT untuk melengkapi lokasi aktivitas makan dan tujuan perpindahan pergi adalah...",
        "correct": "에서 / 에 (에서 untuk tempat terjadinya aktivitas dinamis makan, dan 에 untuk arah tujuan pergerakan verba 'pergi' 가다).",
        "distractors": [
            "에 / 에서 (urutan terbalik yang keliru menempatkan arah pergerakan dengan 에서 dan aksi dinamis dengan 에).",
            "에서 / 에서 (penggunaan 에서 pada tujuan pergerakan yang melanggar kolokasi baku kata kerja 가다).",
            "에 / 에 (penggunaan 에 pada lokasi aksi dinamis makan yang salah fungsi gramatikal).",
            "로 / 에게 (kombinasi partikel arah instrumental dan penanda penerima manusia yang salah konteks)."
        ],
        "formula": {
            "title": "DISTINCTION: 에 (LIEU DE DESTINATION/EXISTENCE) VS 에서 (LIEU D'ACTION)",
            "latex": "\\text{Aktivitas Dinamis} + \\mathbf{에서} \\quad | \\quad \\text{Tujuan Gerak (가다/오다) / Keberadaan (있다/없다)} + \\mathbf{에}",
            "legend": "• 식당에서 밥을 먹다: makan (aksi dinamis) $\\rightarrow$ 에서.<br>• 도서관에 가다: pergi ke tujuan $\\rightarrow$ 에."
        },
        "hints": {
            "concept": "Dalam bahasa Korea: '에서' digunakan untuk menandai tempat berlangsungnya suatu aksi atau aktivitas dinamis (makan, belajar, berolahraga). Sedangkan '에' digunakan untuk menandai tujuan pergerakan (bersama 가다/오다) atau tempat keberadaan statis (bersama 있다/없다).",
            "execution": "Aktivitas makan di kafetaria -> 에서; Pergi ke perpustakaan -> 에. Pasangan: 에서 / 에."
        }
    },
    {
        "id": "kor-lat-e-04",
        "materi": "TATA BAHASA: BILANGAN ASLI KOREA & KATA PENGGOLONG (COUNTING UNITS)",
        "topic": "Penghitungan Jumlah Orang Menggunakan Bilangan Asli Korea dan Penggolong '명'",
        "stem": "Seorang pelanggan memesan tempat duduk di restoran tradisional:\n'식당 직원: 손님, 모두 몇 분이십니까?\n손님: 어른 ( ... ) 하고 아이 한 명입니다. 자리 있습니까?'\nBentuk bilangan asli Korea yang TEPAT untuk menyatakan 'tiga orang dewasa' di depan satuan '명' adalah...",
        "correct": "세 명 (bilangan asli 셋 berubah menjadi 세 saat diikuti langsung oleh kata penggolong 名/명).",
        "distractors": [
            "셋 명 (kesalahan mempertahankan konsonan ㅅ pada angka tiga sebelum kata satuan hitung).",
            "삼 명 (kesalahan menggunakan bilangan Sino-Korea 삼 untuk menghitung orang dengan penggolong 명).",
            "석 명 (bentuk arkaik penghitungan benda tradisional yang tidak lazim untuk manusia).",
            "세 개 (kesalahan menggunakan kata penggolong benda mati 개 untuk manusia)."
        ],
        "formula": {
            "title": "BILANGAN ASLI KOREA DENGAN PENGGOLONG ORANG (명)",
            "latex": "\\text{Angka Asli: } \\text{하나} \\rightarrow \\mathbf{한}, \\text{ 둘} \\rightarrow \\mathbf{두}, \\text{ 셋} \\rightarrow \\mathbf{세}, \\text{ 넷} \\rightarrow \\mathbf{네}, \\text{ 스물} \\rightarrow \\mathbf{스무}",
            "legend": "• 셋 (3) berubah menjadi '세' di depan kata penggolong satuan.<br>• Menghitung manusia menggunakan penggolong '명' (formal: 분).<br>• 3 orang = '세 명'."
        },
        "hints": {
            "concept": "Untuk menghitung jumlah orang/benda dengan penggolong (counter units), bahasa Korea menggunakan bilangan asli Korea. Empat angka pertama mengalami pemendekan: 하나->한, 둘->두, 셋->세, 넷->네. Angka 'tiga' sebelum penggolong '명' menjadi '세 명'.",
            "execution": "3 orang = '세 명'."
        }
    },
    {
        "id": "kor-lat-e-05",
        "materi": "TATA BAHASA: BENTUK FORMAL KESOPANAN (-ㅂ니다/-습니다)",
        "topic": "Konjugasi Akhiran Kalimat Formal Deklaratif Sesuai Keberadaan Batchim",
        "stem": "Dalam pidato pembukaan acara seminar mahasiswa internasional:\n'오늘 바쁘신 중에도 참석해 주신 여러분께 진심으로 감사( ... ). 지금부터 행사를 시작( ... ).'\nBentuk akhiran formal kesopanan (-ㅂ니다/-습니다) yang TEPAT dari verba '감사하다' (akhiran vokal 하) dan '시작하다' (akhiran vokal 하) adalah...",
        "correct": "감사합니다 / 시작합니다 (akar kata kerja berakhiran vokal 하 sehingga langsung dilekati akhiran -ㅂ니다).",
        "distractors": [
            "감사습니다 / 시작습니다 (kesalahan menerapkan akhiran 습니다 pada akar kata yang berakhiran vokal).",
            "감사합니다 / 시작습니다 (inkonsistensi penerapan kaidah batchim pada dua akar kata kerja sejenis).",
            "감사해요 / 시작해요 (bentuk informal santun -아요/어요 yang kurang tepat untuk laras pidato resmi formal).",
            "감사하십시오 / 시작하십시오 (bentuk kalimat perintah imperatif resmi yang keliru untuk tuturan deklaratif)."
        ],
        "formula": {
            "title": "KONJUGASI FORMAL RESMI: -ㅂ니다 / -습니다",
            "latex": "\\text{Akar Vokal (Tanpa Batchim)} + \\mathbf{-ㅂ니다} \\quad \\leftrightarrow \\quad \\text{Akar Konsonan (Batchim)} + \\mathbf{-습니다}",
            "legend": "• 감사하- (vokal) $\\rightarrow$ 감사합니다.<br>• 시작하- (vokal) $\\rightarrow$ 시작합니다.<br>• Digunakan pada situasi resmi, pidato, berita, dan militer."
        },
        "hints": {
            "concept": "Akhiran formal resmi tingkat tinggi deklaratif adalah '-ㅂ니다/-습니다'. Jika akar kata kerja berakhiran vokal (tidak ada batchim), imbuhkan '-ㅂ니다' langsung di bawah vokal (감사하- + ㅂ니다 = 감사합니다; 시작하- + ㅂ니다 = 시작합니다). Jika berakhiran konsonan (ada batchim), gunakan '-습니다' (먹다 -> 먹습니다).",
            "execution": "감사하다 -> 감사합니다; 시작하다 -> 시작합니다."
        }
    },
    {
        "id": "kor-lat-e-06",
        "materi": "TATA BAHASA: BENTUK LAMPAU TERATUR (-았/었어요)",
        "topic": "Penentuan Asimilasi Vokal Bentuk Lampau Berdasarkan Harmoni Vokal Terakhir Akar Kata",
        "stem": "Dua sahabat membicarakan kegiatan akhir pekan kemarin:\n'가: 어제 주말에 무엇을 했어요?\n나: 친구들과 같이 명동에 ( ... ) 맛있는 한국 음식을 ( ... ).'\nPasangan bentuk lampau (-았/었어요) yang TEPAT dari kata kerja '가다' (pergi) dan '먹다' (makan) adalah...",
        "correct": "갔어요 / 먹었어요 (가다 berakar vokal ㅏ melebur dengan -았- menjadi 갔어요; 먹다 berakar vokal ㅓ berpadu dengan -었- menjadi 먹었어요).",
        "distractors": [
            "갔어요 / 먹았어요 (kesalahan harmoni vokal ㅓ pada 먹다 yang keliru dipadukan dengan akhiran 았).",
            "가았어요 / 먹었어요 (kesalahan tidak meleburkan vokal ㅏ rangkap pada kata kerja 가다).",
            "갔었어요 / 먹었었어요 (bentuk lampau lampau/terputus yang tidak dibutuhkan untuk konteks kemarin biasa).",
            "가요 / 먹어요 (bentuk waktu sekarang yang bertentangan dengan keterangan waktu lampau 어제)."
        ],
        "formula": {
            "title": "HARMONI VOKAL KALA LAMPAU: -았/었어요",
            "latex": "\\text{Vokal Akhir } \\mathbf{ㅏ, ㅗ} + \\mathbf{-았어요} \\quad | \\quad \\text{Vokal Selain itu } + \\mathbf{-었어요} \\quad | \\quad \\mathbf{하-} + \\text{였-} \\rightarrow \\mathbf{했어요}",
            "legend": "• 가- + 았어요 $\\rightarrow$ 갔어요 (peleburan vokal).<br>• 먹- + 었어요 $\\rightarrow$ 먹었어요 (vokal ㅓ menggunakan -었-)."
        },
        "hints": {
            "concept": "Aturan kala lampau informal santun (-았/었어요): 1) Jika vokal terakhir akar kata adalah 'ㅏ' atau 'ㅗ', gunakan '-았어요' (가다 -> 가+았어요 -> 갔어요). 2) Jika vokal selain 'ㅏ/ㅗ', gunakan '-었어요' (먹다 -> 먹+었어요 -> 먹었어요).",
            "execution": "가다 -> 갔어요; 먹다 -> 먹었어요. Pilihan tepat: 갔어요 / 먹었어요."
        }
    },
    {
        "id": "kor-lat-e-07",
        "materi": "TATA BAHASA: BILANGAN SINO-KOREA (TANGGAL & UANG)",
        "topic": "Penyebutan Tanggal dan Bulan Menggunakan Bilangan Sino-Korea (일, 이, 삼, 사...)",
        "stem": "Percakapan mengenai jadwal ujian akhir semester:\n'가: 한국어 기말시험이 몇 월 며칠입니까?\n나: 10월 24일입니다.'\nCara pelafalan baku dalam angka Sino-Korea untuk tanggal '10월 24일' (dengan perubahan fonologis bulan Oktober) adalah...",
        "correct": "시월 이십사일 (bulan 10 dilafalkan 시월 dengan pelepasan batchim ㅂ; tanggal 24 dilafalkan 이십사일).",
        "distractors": [
            "십월 이십사일 (kesalahan mempertahankan konsonan batchim ㅂ pada penyebutan bulan Oktober).",
            "시월 스물네일 (kesalahan fatal mencampur angka asli Korea 스물네 untuk penyebutan tanggal kalender).",
            "유월 이십사일 (유월 adalah sebutan untuk bulan Juni/bulan 6, bukan bulan 10).",
            "십월 스물네일 (kesalahan ganda pada penyebutan nama bulan dan sistem penanggalan)."
        ],
        "formula": {
            "title": "SINO-KOREAN NUMBERS: TANGGAL & BULAN (월/일)",
            "latex": "\\text{Bulan: } \\text{Sino-Korea} + \\mathbf{월} \\quad | \\quad \\text{Pengecualian: } 6\\text{월 } (\\mathbf{유월}), \\quad 10\\text{월 } (\\mathbf{시월})",
            "legend": "• Tanggal kalender SELALU menggunakan sistem Sino-Korea.<br>• Bulan 10 (10월): '십월' berubah menjadi '시월' demi kemudahan fonotaktik pelafalan.<br>• Tanggal 24 (24일): 이십사일."
        },
        "hints": {
            "concept": "Penyebutan tanggal dan bulan selalu menggunakan bilangan Sino-Korea (일, 이, 삼, 사...). Pengecualian fonologis mutlak dalam kalender Korea: Bulan 6 (6월) dibaca '유월' (bukan 육월), dan Bulan 10 (10월) dibaca '시월' (bukan 십월). Angka 24 adalah 이십사 (24일 = 이십사일).",
            "execution": "10월 24일 = '시월 이십사일'."
        }
    },
    {
        "id": "kor-lat-e-08",
        "materi": "TATA BAHASA: PARTIKEL PENGHUBUNG '와/과' DAN '하고'",
        "topic": "Penentuan Partikel Penghubung 'Dan' Berdasarkan Batchim pada Ragam Tulis Formal",
        "stem": "Dalam deskripsi menu sarapan khas Korea:\n'한국 사람들은 아침 식사로 밥( ... ) 국을 자주 먹습니다. 그리고 김치( ... ) 여러 가지 반찬도 함께 먹습니다.'\nPasangan partikel penghubung setara (와/과) yang TEPAT untuk menghubungkan '밥' (nasi, ber-batchim ㅂ) dan '김치' (kimchi, berakhiran vokal ㅣ) adalah...",
        "correct": "과 / 와 (kata ber-batchim 밥 diikuti 과; kata tanpa batchim 김치 diikuti 와).",
        "distractors": [
            "와 / 과 (urutan terbalik yang keliru memasangkan 와 pada kata ber-batchim).",
            "과 / 과 (kesalahan menerapkan 과 pada kata yang berakhiran vokal 김치).",
            "와 / 와 (kesalahan menerapkan 와 pada kata yang memiliki batchim 밥).",
            "하고 / 하고 (ragam lisan sehari-hari yang kurang mencerminkan partikel formal ragam tulis teks eksposisi)."
        ],
        "formula": {
            "title": "PARTIKEL KOORDINATIF: 와/과 (DAN/BERSAMA)",
            "latex": "\\text{Ada Batchim} + \\mathbf{과} \\quad \\leftrightarrow \\quad \\text{Tanpa Batchim} + \\mathbf{와}",
            "legend": "• 밥 (ada batchim ㅂ) $\\rightarrow$ 밥과 국.<br>• 김치 (akhiran vokal ㅣ) $\\rightarrow$ 김치와 반찬.<br>• Khusus ragam tulis formal."
        },
        "hints": {
            "concept": "Partikel koordinatif 'dan/bersama' dalam ragam tulis formal: kata berakhiran konsonan/batchim menggunakan '과' (밥 -> 밥과), sedangkan kata berakhiran vokal/tanpa batchim menggunakan '와' (김치 -> 김치와).",
            "execution": "밥 (batchim) -> 과; 김치 (vokal) -> 와. Pasangan: 과 / 와."
        }
    },
    {
        "id": "kor-lat-e-09",
        "materi": "TATA BAHASA: BENTUK NEGASI DASAR (안 VS -지 않다)",
        "topic": "Penempatan Partikel Negasi Pendek '안' di Depan Kata Kerja",
        "stem": "Percakapan antara dua teman yang berjanji temu:\n'가: 민수 씨, 오늘 오후에 약속이 있어서 나갑니까?\n나: 아니요, 비가 많이 와서 오늘은 밖에 ( ... ) 나가요. 집에서 쉴 거예요.'\nBentuk kata negasi pendek yang TEPAT untuk melengkapi kalimat di atas adalah...",
        "correct": "안 (kata keterangan penyangkal pendek yang diletakkan tepat mendahului kata kerja dasar 나가다).",
        "distractors": [
            "못 (penyangkal ketidakmampuan fisik/keadaan yang kurang tepat karena ia menolak keluar secara sukarela).",
            "없 (akar kata ketiadaan yang tidak dapat berfungsi sebagai adverbia negasi sebelum verba).",
            "아니 (kata seru penolakan jawaban mandiri yang tidak dapat disisipkan tepat di depan verba terkonjugasi).",
            "마 (akar kata larangan imperatif yang hanya digunakan bersama -지 말다)."
        ],
        "formula": {
            "title": "LA NÉGATION COURTE: 안 + VERBE",
            "latex": "\\mathbf{안} + \\text{Kata Kerja} \\quad \\iff \\quad \\text{Kata Kerja} + \\mathbf{-지 \\text{ } 않다}",
            "legend": "• Menunjukkan kehendak sukarela untuk tidak melakukan sesuatu (tidak pergi).<br>• Diletakkan tepat di depan kata kerja: 안 나가요."
        },
        "hints": {
            "concept": "Negasi pendek sukarela dalam bahasa Korea menggunakan kata '안' yang diletakkan tepat di depan kata kerja (안 나가요 = tidak pergi). Jika menggunakan bentuk panjang, digunakan akhiran '-지 않아요' (나가지 않아요).",
            "execution": "Tepat di depan verba '나가요' -> gunakan '안'."
        }
    },
    {
        "id": "kor-lat-e-10",
        "materi": "TATA BAHASA: PARTIKEL KEPEMILIKAN (의)",
        "topic": "Pelafalan dan Fungsi Partikel Genitif '의' Menunjukkan Kepemilikan",
        "stem": "Di meja resepsionis asrama mahasiswa:\n'가: 이 지갑은 누구( ... ) 것입니까?\n나: 그 지갑은 제 룸메이트( ... ) 지갑입니다.'\nPartikel kepemilikan/genitif yang TEPAT untuk mengisi kedua tanda kurung di atas adalah...",
        "correct": "의 / 의 (partikel genitif resmi yang menandai hubungan kepemilikan antara subjek pemilik dan benda yang dimiliki).",
        "distractors": [
            "에 / 에 (partikel penanda lokasi atau waktu yang salah fungsi gramatikal).",
            "은 / 는 (partikel penanda topik kalimat).",
            "을 / 를 (partikel penanda objek penderita verba transitif).",
            "도 / 도 (partikel inklusi penambah yang bermakna 'juga')."
        ],
        "formula": {
            "title": "PARTIKEL KEPEMILIKAN: 의 (GENITIVE MARKER)",
            "latex": "\\text{Pemilik} + \\mathbf{의} + \\text{Benda Milik} \\quad (\\text{Pelafalan partikel 의: } [\\text{에}])",
            "legend": "• 누구의 것: milik siapa?<br>• 룸메이트의 지갑: dompet milik teman sekamar.<br>• Saat berfungsi sebagai partikel kepemilikan, '의' dilafalkan [에]."
        },
        "hints": {
            "concept": "Partikel kepemilikan (genitif) dalam bahasa Korea adalah '의' (dibaca [에]). Partikel ini dilekatkan pada pemilik untuk menerangkan kata benda miliknya (누구의 것 = milik siapa; 룸메이트의 지갑 = dompet teman sekamar).",
            "execution": "Partikel kepemilikan = '의 / 의'."
        }
    },
    {
        "id": "kor-lat-e-11",
        "materi": "TATA BAHASA: PENGGOLONG BENDA & BILANGAN ASLI KOREA (개, 권, 잔, 병)",
        "topic": "Pasangan Kata Penggolong yang Tepat untuk Buku (권) dan Minuman Botol (병)",
        "stem": "Daftar belanjaan perlengkapan belajar dan konsumsi:\n'서점에서 한국어 책 두 ( ... )을 샀습니다. 그리고 편의점에서 시원한 생수 세 ( ... )을 샀습니다.'\nPasangan kata penggolong (classifier units) yang TEPAT untuk buku dan botol air mineral adalah...",
        "correct": "권 / 병 (권 adalah kata penggolong untuk buku/jilid berhalaman; 병 adalah kata penggolong untuk botol minuman).",
        "distractors": [
            "개 / 마리 (개 adalah penggolong umum benda mati; 마리 adalah penggolong untuk hewan peliharaan).",
            "장 / 잔 (장 adalah penggolong lembaran kertas tipis; 잔 adalah penggolong cangkir/gelas).",
            "대 / 명 (대 adalah penggolong kendaraan/mesin elektronik; 명 adalah penggolong manusia).",
            "권 / 장 (kesalahan menggunakan penggolong lembaran kertas untuk botol air mineral)."
        ],
        "formula": {
            "title": "KATA PENGGOLONG BENDA (CLASSIFIERS)",
            "latex": "\\text{Buku/Majalah} \\rightarrow \\mathbf{권} \\quad | \\quad \\text{Botol} \\rightarrow \\mathbf{병} \\quad | \\quad \\text{Cangkir} \\rightarrow \\mathbf{잔} \\quad | \\quad \\text{Lembar} \\rightarrow \\mathbf{장}",
            "legend": "• 책 두 권: dua jilid/buku.<br>• 생수 세 병: tiga botol air mineral."
        },
        "hints": {
            "concept": "Kata penggolong khusus dalam bahasa Korea: untuk buku dan media berjilid menggunakan '권' (두 권 = 2 jilid buku); untuk botol menggunakan '병' (세 병 = 3 botol).",
            "execution": "Buku = 권; Botol = 병. Pasangan: 권 / 병."
        }
    },
    {
        "id": "kor-lat-e-12",
        "materi": "TATA BAHASA: PARTIKEL INKLUSIF '도' (JUGA)",
        "topic": "Penggantian Partikel Kasus Dasar dengan Partikel Penambahan '도'",
        "stem": "Seorang turis menceritakan destinasi wisatanya di Korea Selatan:\n'저는 서울을 여행했습니다. 그리고 제주도( ... ) 여행했습니다. 두 곳 모두 정말 아름다웠습니다.'\nPartikel penambah yang TEPAT untuk menyatakan 'juga' (menggantikan partikel objek 를) adalah...",
        "correct": "도 (partikel penanda inklusi yang bermakna 'juga/pula', menggantikan partikel penanda kasus dasar 은/는/이/가/을/를).",
        "distractors": [
            "만 (partikel eksklusivitas pembatasan yang bermakna 'hanya', bertentangan dengan konteks kedua tempat dikunjungi).",
            "를 (partikel objek biasa yang tidak memiliki muatan makna penambahan juga).",
            "는 (partikel topik biasa yang tidak menekankan makna penambahan kesamaan destinasi).",
            "와 (partikel penghubung yang membutuhkan nomina pelengkap berikutnya)."
        ],
        "formula": {
            "title": "PARTIKEL INKLUSIF: 도 (JUGA/PULA)",
            "latex": "\\text{Nomina} + \\mathbf{도} \\quad (\\text{menggantikan 은/는, 이/가, 을/를})",
            "legend": "• 서울을 여행하다 + 제주도를 여행하다 $\\rightarrow$ 제주도도 여행했습니다.<br>• Bermakna menambahkan hal serupa pada situasi sebelumnya."
        },
        "hints": {
            "concept": "Partikel '도' berarti 'juga' atau 'pun'. Ketika dilekatkan pada kata benda, partikel '도' menggantikan partikel dasar seperti 은/는, 이/가, 을/를 (제주도를 -> 제주도도 = pulau Jeju juga).",
            "execution": "Menyatakan 'juga' -> gunakan '도'."
        }
    },
    {
        "id": "kor-lat-e-13",
        "materi": "TATA BAHASA: BENTUK WAKTU SEKARANG INFORMAL SANTUN (-아요/어요)",
        "topic": "Konjugasi Verba '보이다' dan '만나다' Menjadi Bentuk Santun Percakapan Sehari-hari",
        "stem": "Dua sahabat berjanji temu di depan bioskop:\n'가: 오늘 저녁에 영화관 앞에서 친구를 ( ... ).\n나: 저도 그 영화를 정말 ( ... ) 싶어요. 같이 가요.'\nPasangan bentuk kata kerja '만나다' (bertemu) dan verba keinginan '보고 싶다' (ingin menonton) yang TEPAT adalah...",
        "correct": "만나요 / 보고 (만나다 melebur menjadi 만나요; struktur keinginan -고 싶다 menuntut bentuk akar dasar verba 보- + 고).",
        "distractors": [
            "만나요 / 봐 (kesalahan mengonjugasikan verba sebelum akhiran pembantu -고 싶다).",
            "만나어요 / 보고 (kesalahan tidak meleburkan vokal ㅏ rangkap pada verba 만나다).",
            "만납니다 / 봤 (kombinasi pincang formal resmi dan bentuk lampau yang salah konteks ajakan hari ini).",
            "만났어요 / 보고 (bentuk lampau yang bertentangan dengan keterangan waktu petang nanti 오늘 저녁에)."
        ],
        "formula": {
            "title": "BENTUK INFORMAL SANTUN (-아요/어요) & INGIN (-고 싶다)",
            "latex": "\\text{만나-} + \\text{-아요} \\rightarrow \\mathbf{만나요} \\quad | \\quad \\text{보-} + \\mathbf{-고 \\text{ } 싶다} \\rightarrow \\mathbf{보고 \\text{ } 싶어요}",
            "legend": "• 만나다 (vokal ㅏ) $\\rightarrow$ 만나요.<br>• Struktur keinginan: Akar kata kerja + -고 싶다 $\\rightarrow$ 보고 싶다."
        },
        "hints": {
            "concept": "Kata kerja '만나다' berakhiran vokal 'ㅏ' sehingga ditambah '-아요' dan melebur menjadi '만나요'. Rumus menyatakan keinginan 'ingin melakukan sesuatu' adalah: akar kata kerja + '-고 싶다'. Verba '보다' menjadi '보고 싶어요'.",
            "execution": "만나요 / 보고."
        }
    },
    {
        "id": "kor-lat-e-14",
        "materi": "TATA BAHASA: PENUNJUK WAKTU 'JAM DAN MENIT' (시 & 분)",
        "topic": "Kombinasi Bilangan Asli Korea untuk Jam (시) dan Bilangan Sino-Korea untuk Menit (분)",
        "stem": "Jadwal keberangkatan kereta cepat KTX:\n'서울행 KTX 열차는 오후 4시 35분에 출발합니다.'\nCara pelafalan baku dalam bahasa Korea untuk jam dan menit '4시 35분' adalah...",
        "correct": "네 시 삼십오 분 (jam menggunakan angka asli Korea 네 시; menit menggunakan angka Sino-Korea 삼십오 분).",
        "distractors": [
            "사 시 삼십오 분 (kesalahan menggunakan angka Sino-Korea 사 untuk penunjuk satuan jam).",
            "네 시 서른다섯 분 (kesalahan fatal menggunakan angka asli Korea 서른다섯 untuk penunjuk menit).",
            "넷 시 삼십오 분 (kesalahan tidak memendekkan 넷 menjadi 네 di depan kata penggolong jam 시).",
            "사 시 서른다섯 분 (kesalahan ganda terbalik pada seluruh penanda jam dan menit)."
        ],
        "formula": {
            "title": "WAKTU KOREA: JAM (ASLI) & MENIT (SINO-KOREA)",
            "latex": "\\mathbf{Bilangan \\text{ } Asli \\text{ } Korea} + \\mathbf{시 (Jam)} \\quad + \\quad \\mathbf{Bilangan \\text{ } Sino-Korea} + \\mathbf{분 (Menit)}",
            "legend": "• 4시 (Jam 4): 넷 $\\rightarrow$ '네 시' (Angka Asli).<br>• 35분 (35 menit): '삼십오 분' (Angka Sino-Korea).<br>• ATURAN EMAS: Jam pakai Asli, Menit pakai Sino!"
        },
        "hints": {
            "concept": "Aturan emas membaca waktu dalam bahasa Korea: Satuan Jam (시) SELALU menggunakan bilangan Asli Korea (한 시, 두 시, 세 시, 네 시...). Satuan Menit (분) SELALU menggunakan bilangan Sino-Korea (일 분, 이십 분, 삼십오 분...). Maka 4시 35분 dibaca: '네 시 삼십오 분'.",
            "execution": "Jam = Asli (네 시); Menit = Sino (삼십오 분)."
        }
    },
    {
        "id": "kor-lat-e-15",
        "materi": "TATA BAHASA: BENTUK AJAKAN SANTUN (-읍시다/-ㅂ시다 & -아요/어요)",
        "topic": "Penggunaan Akhiran Ajakan Bersama '-(으)ㅂ시다' dalam Situasi Formal Sopan",
        "stem": "Ketua kelompok belajar mengajak rekan-rekannya sebelum istirahat siang:\n'시간이 벌써 12시가 되었습니다. 우리 다 같이 학생식당에 가서 점심을 ( ... ).'\nBentuk ajakan formal sopan yang TEPAT dari kata kerja '먹다' (makan, ber-batchim ㄱ) untuk subjek bersama '우리' adalah...",
        "correct": "먹읍시다 (akar kata kerja ber-batchim 먹- berpasangan dengan akhiran ajakan -읍시다).",
        "distractors": [
            "먹ㅂ시다 (kesalahan ortografi dengan menempelkan ㅂ langsung tanpa vokal penyambung 으 pada konsonan ㄱ).",
            "먹으십시오 (bentuk perintah penghormatan resmi yang ditujukan kepada lawan bicara, bukan ajakan bersama).",
            "먹었습니다 (bentuk waktu lampau deklaratif yang tidak menyatakan ajakan masa kini).",
            "먹겠습니까 (bentuk kalimat tanya menanyakan kesediaan, bukan ajakan langsung kelompok)."
        ],
        "formula": {
            "title": "AKHIRAN AJAKAN FORMAL: -(으)ㅂ시다 (LET'S)",
            "latex": "\\text{Akar Ber-Batchim} + \\mathbf{-읍시다} \\quad \\leftrightarrow \\quad \\text{Akar Tanpa Batchim} + \\mathbf{-ㅂ시다}",
            "legend": "• 먹- (ada batchim ㄱ) $\\rightarrow$ 먹읍시다 (Mari kita makan).<br>• 가- (tanpa batchim) $\\rightarrow$ 갑시다 (Mari kita pergi).<br>• Hanya digunakan untuk mengajak orang sebaya atau yang lebih muda dalam forum formal."
        },
        "hints": {
            "concept": "Akhiran formal untuk mengajak melakukan sesuatu bersama-sama ('mari kita...') adalah '-(으)ㅂ시다'. Jika akar kata berakhiran konsonan (ada batchim), gunakan '-읍시다' (먹다 -> 먹- + 읍시다 = 먹읍시다).",
            "execution": "먹다 (batchim) + ajakan formal = '먹읍시다'."
        }
    },
    {
        "id": "kor-lat-e-16",
        "materi": "TATA BAHASA: PARTIKEL ARAH DAN TUJUAN (-(으)로)",
        "topic": "Distingsi Pemakaian '-(으)로' Sesuai Keberadaan Konsonan Akhir dan Pengecualian Batchim ㄹ",
        "stem": "Instruksi petugas stasiun subway kepada penumpang:\n'시청 방면으로 가실 승객께서는 오른쪽( ... ) 가시고, 2호선으로 갈아타실 분은 지하 2층( ... ) 내려가십시오.'\nPasangan partikel penanda arah tujuan (-(으)로) yang TEPAT untuk '오른쪽' (arah kanan, ber-batchim ㄱ) dan '지하 2층' (lantai bawah tanah 2, ber-batchim ㅇ) adalah...",
        "correct": "으로 / 으로 (kedua kata berakhiran konsonan/batchim sehingga wajib berpasangan dengan 으로).",
        "distractors": [
            "로 / 로 (keliru menggunakan 로 yang hanya diperuntukkan bagi kata berakhiran vokal atau batchim ㄹ).",
            "으로 / 로 (kesalahan mengasumsikan kata 2층 berakhiran vokal).",
            "로 / 으로 (kesalahan mengasumsikan kata 오른쪽 berakhiran vokal).",
            "에 / 에서 (partikel lokasi statis atau dinamis, bukan penanda arah pergerakan koridor)."
        ],
        "formula": {
            "title": "PARTIKEL ARAH/SARANA: -(으)로",
            "latex": "\\text{Ada Batchim (selain ㄹ)} + \\mathbf{으로} \\quad \\leftrightarrow \\quad \\text{Tanpa Batchim / Batchim ㄹ} + \\mathbf{로}",
            "legend": "• 오른쪽 (batchim ㄱ) $\\rightarrow$ 오른쪽으로 (ke arah kanan).<br>• 지하 2층 (batchim ㅇ) $\\rightarrow$ 지하 2층으로 (ke arah lantai B2)."
        },
        "hints": {
            "concept": "Partikel '-(으)로' digunakan untuk menunjukkan arah pergerakan atau sarana/alat. Jika kata berakhiran konsonan selain 'ㄹ', gunakan '으로' (오른쪽 -> 오른쪽으로; 2층 -> 2층으로). Jika berakhiran vokal atau konsonan 'ㄹ', gunakan '로'.",
            "execution": "오른쪽 (batchim ㄱ) -> 으로; 2층 (batchim ㅇ) -> 으로. Pasangan: 으로 / 으로."
        }
    },
    {
        "id": "kor-lat-e-17",
        "materi": "TATA BAHASA: BENTUK LARANGAN HALUS (-지 마세요)",
        "topic": "Konstruksi Larangan Santun Menggunakan Akar Verba + '-지 마세요'",
        "stem": "Papan peringatan di dalam ruang perpustakaan umum:\n'도서관 안에서는 다른 사람들에게 방해가 되니 큰 소리로 이야기하( ... ).'\nBentuk kalimat larangan santun yang TEPAT dari verba '이야기하다' (berbicara) adalah...",
        "correct": "이야기하지 마세요 (akar verba 이야기하- + akhiran larangan santun -지 마세요).",
        "distractors": [
            "이야기하지 마십시오 (bentuk larangan imperatif sangat kaku dan otoriter yang kurang lazim pada instruksi santun umum).",
            "이야기안 해요 (struktur negasi kehendak deklaratif biasa, bukan kalimat instruksi larangan).",
            "이야기하지 마요 (bentuk santun informal yang kurang baku secara kaidah kesantunan publik).",
            "이야기하지 않으세요 (bentuk pertanyaan negasi honorifik yang menanyakan apakah Anda tidak berbicara)."
        ],
        "formula": {
            "title": "LARANGAN SANTUN: VERBA + -지 마세요 (PLEASE DON'T)",
            "latex": "\\text{Akar Kata Kerja} + \\mathbf{-지 \\text{ } 마세요} \\quad (\\text{ 이야기하-} + \\mathbf{-지 \\text{ } 마세요})",
            "legend": "• Menyatakan larangan secara halus dan sopan kepada publik.<br>• 이야기하다 $\\rightarrow$ 이야기하지 마세요 (Tolong jangan berbicara keras)."
        },
        "hints": {
            "concept": "Pola kalimat larangan sopan dalam bahasa Korea dibentuk dengan menempelkan '-지 마세요' langsung pada akar kata kerja (tanpa memandang ada/tidaknya batchim). Verba '이야기하다' menjadi '이야기하지 마세요' (tolong jangan berbicara).",
            "execution": "이야기하다 + larangan sopan = '이야기하지 마세요'."
        }
    },
    {
        "id": "kor-lat-e-18",
        "materi": "TATA BAHASA: PARTIKEL PEMBATAS '만' (HANYA)",
        "topic": "Penempatan Partikel Eksklusivitas '만' yang Menggantikan Partikel Subjek/Objek",
        "stem": "Percakapan mengenai selera makanan: \n'가: 수진 씨는 매운 음식을 잘 드십니까?\n나: 아니요, 저는 매운 음식을 전혀 못 먹어서 안 매운 음식( ... ) 먹습니다.'\nPartikel pembatas yang TEPAT untuk menyatakan 'hanya memakan makanan yang tidak pedas' adalah...",
        "correct": "만 (partikel penanda pembatasan eksklusif yang bermakna 'hanya/cuma').",
        "distractors": [
            "도 (partikel inklusi yang bermakna 'juga', kontradiktif dengan pernyataan tidak bisa makan pedas sama sekali).",
            "부터 (partikel titik tolak waktu/tempat yang bermakna 'mulai dari').",
            "까지 (partikel batas akhir yang bermakna 'sampai dengan').",
            "보다 (partikel komparasi yang bermakna 'daripada')."
        ],
        "formula": {
            "title": "PARTIKEL PEMBATAS: 만 (ONLY / HANYA)",
            "latex": "\\text{Nomina} + \\mathbf{만} \\quad (\\text{안 매운 음식} + \\mathbf{만} \\rightarrow \\text{hanya makanan tidak pedas})",
            "legend": "• Menunjukkan pengecualian tunggal atau fokus eksklusif.<br>• Menggantikan partikel kasus 을/를: 안 매운 음식만 먹습니다."
        },
        "hints": {
            "concept": "Partikel '만' berarti 'hanya' atau 'cuma'. Partikel ini digunakan untuk membatasi pilihan hanya pada satu hal tersebut (안 매운 음식만 = hanya makanan yang tidak pedas).",
            "execution": "Menyatakan 'hanya' -> gunakan '만'."
        }
    },
    {
        "id": "kor-lat-e-19",
        "materi": "TATA BAHASA: PENGHUBUNG KRONOLOGIS SEDERHANA (-고)",
        "topic": "Penggabungan Dua Tindakan Sekuensial Setara Menggunakan '-고'",
        "stem": "Aktivitas pagi hari sebelum berangkat ke sekolah:\n'저는 아침에 일찍 일어나서 세수를 하( ... ) 아침 밥을 맛있게 먹었습니다.'\nAkhiran konjungsi koordinatif sekuensial yang TEPAT untuk menyambung kata kerja '하다' adalah...",
        "correct": "하고 (akar kata kerja 하- + akhiran penghubung koordinatif urutan tindakan -고).",
        "distractors": [
            "하지만 (konjungsi pertentangan yang bermakna 'tetapi/namun').",
            "하면 (akhiran pengandaian kondisional yang bermakna 'jika/apabila').",
            "해서 (akhiran sebab akibat yang mengimplikasikan mencuci muka menjadi penyebab makan nasi).",
            "하러 (akhiran tujuan pergerakan yang wajib berpasangan dengan kata kerja pergi/datang)."
        ],
        "formula": {
            "title": "KONJUNGSI KRONOLOGIS SETARA: -고 (AND / KEMUDIAN)",
            "latex": "\\text{Akar Verba 1} + \\mathbf{-고} + \\text{Klausa Verba 2} \\quad (\\text{세수를 하-} + \\mathbf{-고})",
            "legend": "• Menghubungkan dua tindakan berurutan secara netral tanpa hubungan sebab-akibat.<br>• Tenses waktu lampau diletakkan HANYA pada kata kerja terakhir kalimat (먹었습니다)."
        },
        "hints": {
            "concept": "Akhiran '-고' dilekatkan pada akar kata kerja untuk menyatakan urutan dua tindakan yang setara (mencuci muka DAN/KEMUDIAN sarapan). Penanda waktu lampau tidak perlu diletakkan di klausa pertama, melainkan cukup di akhir kalimat.",
            "execution": "하다 -> '하고'."
        }
    },
    {
        "id": "kor-lat-e-20",
        "materi": "TATA BAHASA: PARTIKEL WAKTU '부터' DAN '까지'",
        "topic": "Menyatakan Rentang Waktu 'Mulai Dari ... Sampai Dengan ...'",
        "stem": "Pengumuman jam operasional kantor pos distrik:\n'우체국 업무 시간은 평일 오전 9시( ... ) 오후 6시( ... )입니다. 주말에는 쉽니다.'\nPasangan partikel penanda awal dan akhir rentang waktu yang TEPAT adalah...",
        "correct": "부터 / 까지 (부터 menandai titik awal waktu operasional; 까지 menandai batas akhir waktu operasional).",
        "distractors": [
            "에서 / 까지 (에서 biasanya digunakan untuk titik tolak tempat/lokasi spasial, bukan titik tolak jam waktu).",
            "부터 / 에 (에 hanya penanda waktu tunggal tanpa makna batas rentang hingga berakhir).",
            "까지 / 부터 (urutan terbalik yang keliru menempatkan akhir sebelum awal).",
            "에 / 에서 (kombinasi partikel tempat yang keliru diterapkan pada penunjuk jam)."
        ],
        "formula": {
            "title": "RENTANG WAKTU: 부터 (SEJAK/MULAI) ~ 까지 (SAMPAI)",
            "latex": "\\text{Waktu Awal} + \\mathbf{부터} \\quad \\sim \\quad \\text{Waktu Akhir} + \\mathbf{까지}",
            "legend": "• 9시부터 (mulai jam 9) ~ 6시까지 (sampai jam 6).<br>• Untuk rentang tempat spasial: 에서 ~ 까지."
        },
        "hints": {
            "concept": "Untuk menyatakan rentang waktu (dari jam ... sampai jam ...), bahasa Korea menggunakan pasangan partikel: 'Waktu + 부터 (mulai dari)' dan 'Waktu + 까지 (sampai dengan)'.",
            "execution": "9시 -> 부터; 6시 -> 까지. Pasangan: 부터 / 까지."
        }
    },
    {
        "id": "kor-lat-e-21",
        "materi": "TATA BAHASA: BENTUK PERMOHONAN/BANTUAN SANTUN (-아/어 주세요)",
        "topic": "Permohonan Tolong Menggunakan Verba Pembantu '주다' (Memberi Bantuan)",
        "stem": "Di toko suvenir saat meminta pegawai membungkus barang:\n'손님: 저기요, 이 도자기 인형을 선물할 건데 예쁘게 포장( ... )?\n직원: 네, 손님. 잠시만 기다려 주십시오.'\nBentuk permohonan pertolongan santun yang TEPAT dari verba '포장하다' (membungkus) adalah...",
        "correct": "해 주세요 (verba 하다 berubah menjadi 해 + akhiran bantuan permohonan sopan 주세요).",
        "distractors": [
            "하 주세요 (kesalahan tidak mengonjugasikan akar verba 하- menjadi bentuk harmoni vokal 해).",
            "해 마세요 (bentuk larangan yang meminta pegawai untuk tidak membungkus kado).",
            "해 보세요 (bentuk ajakan mencoba melakukan sesuatu, bukan permintaan bantuan jasa).",
            "해 주었습니다 (bentuk lampau deklaratif yang salah konteks permohonan langsung)."
        ],
        "formula": {
            "title": "PERMOHONAN BANTUAN SOPAN: -아/어 주세요 (PLEASE DO FOR ME)",
            "latex": "\\text{Akar Verba} + \\mathbf{-아/어 \\text{ } 주세요} \\quad (\\text{포장하-} \\rightarrow \\mathbf{포장해 \\text{ } 주세요})",
            "legend": "• Menghubungi akar kata verba dengan verba bantu 주다 (memberi).<br>• Bermakna 'tolong lakukan ... untuk saya'."
        },
        "hints": {
            "concept": "Pola kalimat meminta tolong atau permohonan santun dibentuk dengan: akar verba konjugasi vokal (-아/어) + '주세요'. Kata kerja berakhiran '하다' selalu berubah menjadi '해 주세요' (포장하다 -> 포장해 주세요 = tolong bungkuskan).",
            "execution": "포장하다 -> '포장해 주세요'."
        }
    },
    {
        "id": "kor-lat-e-22",
        "materi": "TATA BAHASA: KATA GANTI PENUNJUK BENDA & TEMPAT (이, 그, 저)",
        "topic": "Distingsi Rujukan Posisi Spasial Pembicara dan Lawan Bicara (이것, 그것, 저것)",
        "stem": "Dua sahabat berada di toko pakaian:\n'민수: (pembicara memegang baju di tangannya) 지훈 씨, ( ... ) 옷 어때요? 마음에 들어요?\n지훈: 와, 색깔이 아주 화사하고 잘 어울려요.'\nKata penunjuk demonstratif yang TEPAT untuk benda yang berada dekat dengan tangan pembicara adalah...",
        "correct": "이 (kata penunjuk demonstratif benda yang berada dekat dengan posisi pembicara).",
        "distractors": [
            "그 (kata penunjuk demonstratif benda yang berada dekat dengan lawan bicara atau benda yang sedang dibicarakan).",
            "저 (kata penunjuk demonstratif benda yang posisinya jauh dari pembicara maupun lawan bicara).",
            "어느 (kata tanya pemilihan yang menanyakan 'yang mana').",
            "무슨 (kata tanya jenis yang menanyakan 'apa/macam apa')."
        ],
        "formula": {
            "title": "PENUNJUK DEMONSTRATIF SPASIAL (이, 그, 저)",
            "latex": "\\mathbf{이} \\text{ (Dekat Pembicara)} \\quad | \\quad \\mathbf{그} \\text{ (Dekat Lawan Bicara)} \\quad | \\quad \\mathbf{저} \\text{ (Jauh dari Keduanya)}",
            "legend": "• Pembicara sedang memegang baju di tangannya sendiri $\\rightarrow$ dekat pembicara: '이 옷' (baju ini)."
        },
        "hints": {
            "concept": "Sistem penunjuk demonstratif bahasa Korea: '이' (ini - dekat dengan pembicara), '그' (itu - dekat dengan lawan bicara atau sudah disebut sebelumnya), '저' (itu - jauh dari pembicara maupun lawan bicara). Karena pembicara memegang langsung baju tersebut, gunakan '이 옷'.",
            "execution": "Dekat pembicara -> gunakan '이'."
        }
    },
    {
        "id": "kor-lat-e-23",
        "materi": "TATA BAHASA: PENGGOLONG HEWAN (마리) & BILANGAN ASLI KOREA",
        "topic": "Penghitungan Hewan Peliharaan Menggunakan Bilangan Asli Korea dan Penggolong '마리'",
        "stem": "Bercerita tentang hewan peliharaan di rumah:\n'우리 집에는 귀여운 강아지 두 ( ... )와 고양이 한 ( ... )가 살고 있습니다.'\nKata penggolong (classifier) yang TEPAT untuk menghitung anjing dan kucing adalah...",
        "correct": "마리 / 마리 (마리 adalah kata satuan penggolong khusus untuk seluruh jenis hewan/binatang).",
        "distractors": [
            "명 / 명 (kata penggolong yang hanya diperuntukkan bagi manusia).",
            "개 / 개 (kata penggolong umum untuk benda mati tidak bernyawa).",
            "대 / 대 (kata penggolong khusus kendaraan atau perabot elektronik mesin).",
            "마리 / 개 (kesalahan memperlakukan kucing peliharaan sebagai benda mati)."
        ],
        "formula": {
            "title": "PENGGOLONG HEWAN: 마RI (ANIMALS COUNTER)",
            "latex": "\\text{Hewan (강아지, 고양이, 새, 물고기)} + \\text{Bilangan Asli} + \\mathbf{마리}",
            "legend": "• 강아지 두 마리: 2 ekor anak anjing.<br>• 고양이 한 마리: 1 ekor kucing."
        },
        "hints": {
            "concept": "Kata satuan penggolong untuk hewan (anjing, kucing, ikan, burung) dalam bahasa Korea selalu menggunakan '마리' (두 마리 = 2 ekor; 한 마리 = 1 ekor).",
            "execution": "Penggolong hewan = '마리 / 마리'."
        }
    },
    {
        "id": "kor-lat-e-24",
        "materi": "TATA BAHASA: BENTUK KEMAMPUAN DASAR (-(으)ㄹ 수 있다/없다)",
        "topic": "Menyatakan Kemampuan Berenang Menggunakan Akar Kata Kerja Berakhiran Batchim",
        "stem": "Percakapan mengenai kegiatan olahraga renang:\n'가: 민수 씨는 수영을 잘합니까?\n나: 아니요, 저는 물을 무서워해서 수영을 전혀 ( ... ).'\nBentuk kalimat yang TEPAT dari verba '수영하다' untuk menyatakan 'tidak bisa berenang sama sekali' adalah...",
        "correct": "할 수 없어요 (akar verba 하- tanpa batchim berpadu dengan -ㄹ 수 없다 untuk menyatakan ketidakmampuan).",
        "distractors": [
            "할 수 있어요 (bentuk yang menyatakan kemampuan bisa berenang, bertentangan dengan kata sama sekali takut air).",
            "하지 마세요 (bentuk kalimat larangan kepada orang lain yang keliru subjek).",
            "하러 가요 (bentuk tujuan pergerakan hendak pergi berenang).",
            "하고 싶어요 (hanya menyatakan keinginan, bukan ketidakmampuan faktual)."
        ],
        "formula": {
            "title": "KEMAMPUAN: -(으)ㄹ 수 있다 / 없다 (CAN / CANNOT)",
            "latex": "\\text{Bisa: } \\text{Akar} + \\mathbf{-(으)ㄹ \\text{ } 수 \\text{ } 있다} \\quad | \\quad \\text{Tidak Bisa: } \\text{Akar} + \\mathbf{-(으)ㄹ \\text{ } 수 \\text{ } 없다}",
            "legend": "• 수영하- (vokal) $\\rightarrow$ 수영할 수 없다.<br>• Bentuk santun negatif: 수영을 전혀 할 수 없어요."
        },
        "hints": {
            "concept": "Rumus menyatakan kemampuan atau ketidakmampuan: akar verba + '-(으)ㄹ 수 있다' (bisa) atau '-(으)ㄹ 수 없다' (tidak bisa). Karena akar '하-' berakhiran vokal, tambahkan 'ㄹ 수 없다' -> '할 수 없어요'.",
            "execution": "Tidak bisa berenang = '할 수 없어요'."
        }
    },
    {
        "id": "kor-lat-e-25",
        "materi": "TATA BAHASA: PENGHUBUNG SEBAB AKIBAT DASAR (-아/어서)",
        "topic": "Menyatakan Alasan Keterlambatan Menggunakan Harmoni Vokal '-아/어서'",
        "stem": "Permohonan maaf seorang karyawan saat tiba terlambat di kantor:\n'죄송합니다. 오늘 아침에 도로에 차가 너무 ( ... ) 회사에 늦었습니다.'\nBentuk konjugasi sebab akibat (-아/어서) yang TEPAT dari kata sifat '많다' (banyak, ber-batchim 많 dengan vokal ㅏ) adalah...",
        "correct": "많아서 (akar kata ber-vokal ㅏ sehingga berpasangan dengan akhiran kausalitas -아서).",
        "distractors": [
            "많어서 (kesalahan menerapkan harmoni vokal ㅓ pada akar kata yang bervokal ㅏ).",
            "많고 (akhiran sekuensial dan yang tidak mengekspresikan hubungan sebab akibat langsung keterlambatan).",
            "많으면 (akhiran pengandaian jika/apabila yang keliru untuk fakta kemacetan yang nyata terjadi).",
            "많으니까요 (bentuk akhiran akhir kalimat penjelasan mandiri yang salah kedudukan di tengah klausa subordinat)."
        ],
        "formula": {
            "title": "KONJUNGSI SEBAB AKIBAT: -아/어서 (BECAUSE / SO)",
            "latex": "\\text{Vokal } \\mathbf{ㅏ, ㅗ} + \\mathbf{-아서} \\quad | \\quad \\text{Vokal Lain} + \\mathbf{-어서} \\quad (\\text{많-} + \\mathbf{-아서} \\rightarrow \\mathbf{많아서})",
            "legend": "• Menghubungkan alasan mendasar terjadinya akibat di klausa kedua.<br>• Vokal 'ㅏ' pada 많- mewajibkan akhiran '-아서'."
        },
        "hints": {
            "concept": "Konjungsi kausalitas '-아/어서' (karena/sehingga) mengikuti aturan harmoni vokal: akar bervokal 'ㅏ' atau 'ㅗ' menggunakan '-아서' (많다 -> 많아서). Karena lalu lintas padat sehingga terlambat, bentuknya adalah '많아서'.",
            "execution": "많다 + sebab akibat = '많아서'."
        }
    }
]
