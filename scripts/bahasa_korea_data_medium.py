# -*- coding: utf-8 -*-
"""
BAHASA KOREA - PAKET SOAL LATIHAN MENENGAH (MEDIUM) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / TOPIK I Level 2 - TOPIK II Level 3 (CEFR A2-B1)
Distribusi:
- 9 Butir: Tata Bahasa Honorifik (높임말: -(으)시-, Verba & Nomina Khusus, Partikel 께/께서)
- 8 Butir: Konjungsi Kompleks (-아/어서 vs -(으)니까, -(으)ㄴ/는데, -(으)면서, -기 전에 vs -(으)ㄴ 후에)
- 8 Butir: Pola Ekspresi Tujuan, Izin & Keharusan (-(으)려고, -아야/어야 되다, -아/어도 되다, -(으)면 안 되다)
"""

BAHASA_KOREA_MEDIUM_ITEMS = [
    {
        "id": "kor-lat-m-01",
        "materi": "TATA BAHASA HONORIFIK: VERBA KHUSUS KEBERADAAN (계시다 VS 있으시다)",
        "topic": "Pembedaan Honorifik Langsung Sosok Manusia (계시다) vs Honorifik Kepemilikan Benda/Gejala (있으시다)",
        "stem": "Dalam percakapan telepon dengan sekretaris kantor dekan:\n'가: 실례지만 학장님 지금 연구실에 ( ... )?\n나: 아니요, 학장님께서는 지금 중요한 회의가 ( ... ) 잠시 자리를 비우셨습니다.'\nPasangan bentuk honorifik kata kerja keberadaan yang TEPAT adalah...",
        "correct": "계십니까 / 있으셔서 (계시다 untuk keberadaan langsung sosok manusia yang dihormati; 있으시다 untuk kepemilikan agenda/benda dari sosok yang dihormati).",
        "distractors": [
            "있으십니까 / 계셔서 (urutan terbalik yang keliru memperlakukan agenda rapat seolah-olah bernyawa dan merendahkan sosok dekan).",
            "있습니까 / 있어서 (bentuk biasa tanpa honorifik yang sangat tidak sopan dalam percakapan dengan pejabat kampus).",
            "계십니까 / 계셔서 (kesalahan menggunakan verba 계시다 untuk subjek agenda rapat 회의).",
            "계셨습니까 / 계시어서 (kesalahan tenses waktu lampau dan penggunaan verba manusia untuk benda)."
        ],
        "formula": {
            "title": "DISTINCTION: 계시다 (SUBJEK MANUSIA) VS 있으시다 (KEPEMILIKAN/OBJEK)",
            "latex": "\\text{Sosok Dihormati di Lokasi} \\implies \\mathbf{계시다} \\quad | \\quad \\text{Sosok Dihormati Memiliki Sesuatu} \\implies \\mathbf{있으시다}",
            "legend": "• 학장님 계십니까? (Apakah Bapak Dekan ada di ruangan? $\\rightarrow$ keberadaan fisik orang).<br>• 회의가 있으시다 (Bapak Dekan memiliki agenda rapat $\\rightarrow$ kepemilikan)."
        },
        "hints": {
            "concept": "Aturan emas honorifik Korea: Jika subjek yang dihormati adalah sosok manusia yang berada di suatu tempat, gunakan kata kerja khusus '계시다' (계십니까?). Jika subjek kalimat adalah benda/urusan/keluhan fisik yang dimiliki oleh sosok yang dihormati, gunakan honorifik tidak langsung '있으시다' (회의가 있으셔서).",
            "execution": "Orang di ruangan = 계십니까; Dekan memiliki rapat = 있으셔서."
        }
    },
    {
        "id": "kor-lat-m-02",
        "materi": "TATA BAHASA: DISTINGSI SEBAB AKIBAT (-아/어서 VS -(으)니까)",
        "topic": "Larangan Penggunaan '-아/어서' pada Kalimat Perintah/Ajakan dan Penggunaan '-(으)니까'",
        "stem": "Dalam percakapan saat hujan lebat di luar ruangan:\n'가: 비가 너무 많이 ( ... ) 오늘은 등산을 가지 말고 영화관에 갑시다.\n나: 네, 좋습니다. 날씨가 개면 다음 주에 가요.'\nBentuk konjugasi sebab akibat yang TEPAT untuk menghubungkan klausa alasan dengan klausa ajakan (-ㅂ시다) adalah...",
        "correct": "오니까 (akhiran kausalitas -(으)니까 adalah satu-satunya bentuk yang diizinkan berpasangan dengan kalimat ajakan -ㅂ시다 atau perintah -세요).",
        "distractors": [
            "와서 (aturan mutlak bahasa Korea melarang pemakaian -아/어서 bila klausula utama berbentuk ajakan atau perintah).",
            "오기 때문에 (akhiran kausalitas objektif formal yang tidak lazim disambung langsung dengan ajakan santun mendadak).",
            "오지만 (konjungsi pertentangan yang kontradiktif dengan keputusan membatalkan naik gunung).",
            "오면서 (akhiran simultan yang bermakna 'sambil', merusak logika kalimat)."
        ],
        "formula": {
            "title": "RÈGLE D'OR: -(으)니까 AVEC IMPÉRATIF & PROPOSITIF",
            "latex": "\\mathbf{-(으)니까} + \\text{Ajakan (-ㅂ시다 / -자) / Perintah (-세요)} \\quad (\\mathbf{-아/어서 \\text{ DILARANG!}})",
            "legend": "• Kalimat ajakan (갑시다) TIDAK PERNAH boleh didahului oleh -아/어서.<br>• 비가 오니까 ... 갑시다 (BENAR).<br>• 비가 와서 ... 갑시다 (SALAH MUTLAK!)."
        },
        "hints": {
            "concept": "Hukum gramatika mutlak bahasa Korea: Konjungsi kausalitas '-아/어서' DILARANG KERAS digunakan jika klausa akhir berupa kalimat perintah (-(으)세요, -(으)십시오) atau kalimat ajakan (-(으)ㅂ시다, -자). Dalam situasi ajakan/perintah, WAJIB menggunakan '-(으)니까' (비가 오니까 ... 갑시다).",
            "execution": "Klausa akhir adalah ajakan '갑시다' -> gunakan '오니까'."
        }
    },
    {
        "id": "kor-lat-m-03",
        "materi": "TATA BAHASA HONORIFIK: KOSAKATA KHUSUS PENGHORMATAN",
        "topic": "Penggunaan Verba Honorifik Khusus Makan (드시다), Tidur (주무시다), dan Bertanya/Berkata (말씀하시다)",
        "stem": "Bercerita dengan sopan tentang rutinitas kakek di rumah:\n'할아버지께서는 아침에 일찍 ( ... ) 진지를 맛있게 ( ... ).'\nPasangan bentuk honorifik kata kerja '일어나다' (bangun) dan '먹다' (makan) yang TEPAT adalah...",
        "correct": "일어나셔서 / 드십니다 (일어나다 disisipi infiks honorifik -(으)시- menjadi 일어나시다; verba makan 먹다 berubah total menjadi verba honorifik khusus 드시다).",
        "distractors": [
            "일어나고 / 먹습니다 (bentuk biasa tanpa honorifik yang sangat tidak pantas untuk kakek kandung).",
            "일어나셔서 / 먹으십니다 (kesalahan menerapkan infiks pada 먹다 yang memiliki bentuk honorifik leksikal khusus 드시다).",
            "일어나서 / 잡수십니다 (bentuk klausa pertama yang lupa menyematkan infiks penghormatan).",
            "주무셔서 / 드십니다 (주무시다 adalah honorifik untuk tidur, bukan bangun tidur)."
        ],
        "formula": {
            "title": "HONORIFIK LEKSIKAL KHUSUS (SPECIAL HONORIFIC VERBS)",
            "latex": "\\text{먹다 (makan)} \\rightarrow \\mathbf{드시다 / 잡수시다} \\quad | \\quad \\text{밥 (nasi)} \\rightarrow \\mathbf{진지}",
            "legend": "• Infiks reguler: 일어나다 $\\rightarrow$ 일어나시다 (일어나셔서).<br>• Verba khusus: makan $\\rightarrow$ 드시다 (드십니다).<br>• Nomina khusus: 밥 $\\rightarrow$ 진지."
        },
        "hints": {
            "concept": "Untuk menghormati orang yang lebih tua (kakek/할아버지): verba reguler '일어나다' disisipkan infiks honorifik '-(으)시-' menjadi '일어나시다' (일어나셔서). Verba '먹다' memiliki padanan leksikal khusus penghormatan '드시다' atau '잡수시다' (드십니다).",
            "execution": "일어나셔서 / 드십니다."
        }
    },
    {
        "id": "kor-lat-m-04",
        "materi": "TATA BAHASA: PENGHUBUNG LATAR BELAKANG / KONTRAS (-(으)ㄴ/는데)",
        "topic": "Penggunaan '-(으)ㄴ/는데' Sebagai Pengantar Informasi Latar Belakang Sebelum Saran/Pertanyaan",
        "stem": "Seorang mahasiswa menyapa rekan asramanya:\n'지금 밖에는 비가 많이 ( ... ), 우산이 없으면 제 우산을 같이 쓰고 가요.'\nBentuk konjugasi latar belakang (-(으)ㄴ/는데) yang TEPAT dari kata kerja '오다' (datang/turun hujan) adalah...",
        "correct": "오는데 (akar kata kerja waktu sekarang 오- langsung dilekati akhiran pembuka wacana -는데).",
        "distractors": [
            "오은데 (kesalahan morfologis memasukkan vokal 은 pada akar verba yang tidak ber-batchim).",
            "온데 (kesalahan memperlakukan verba tindakan waktu sekarang seperti adjektiva).",
            "오니까 (hanya menekankan sebab akibat logis, bukan pembuka wacana situasional).",
            "오지만 (terlalu kaku mengontraskan dua klausa tanpa nuansa mengundang tindak lanjut)."
        ],
        "formula": {
            "title": "PENGHUBUNG LATAR BELAKANG: -(으)ㄴ/는데",
            "latex": "\\text{Kata Kerja (Présent)} + \\mathbf{-는데} \\quad | \\quad \\text{Kata Sifat} + \\mathbf{-(으)ㄴ데} \\quad | \\quad \\text{Benda} + \\mathbf{-인데}",
            "legend": "• 오다 adalah kata kerja $\\rightarrow$ 오는데.<br>• Berfungsi memberikan latar belakang situasi sebelum menyampaikan ajakan/saran."
        },
        "hints": {
            "concept": "Akhiran '-(으)ㄴ/는데' berfungsi memberikan konteks latar belakang situasi sebelum pembicara menyampaikan saran, pertanyaan, atau ajakan. Aturan morfologis: untuk seluruh kata kerja (동사) pada kala sekarang, SELALU menggunakan '-는데' (오다 -> 오- + 는데 = 오는데).",
            "execution": "Kata kerja 오다 + latar belakang waktu sekarang = '오는데'."
        }
    },
    {
        "id": "kor-lat-m-05",
        "materi": "TATA BAHASA HONORIFIK: PARTIKEL SUBJEK '께서' DAN PENERIMA '께'",
        "topic": "Penggantian Partikel 이/가 dengan '께서' dan 에게 dengan '께'",
        "stem": "Menceritakan perayaan hari ulang tahun ibu:\n'어제는 어머니( ... ) 생신이어서 제가 어머니( ... ) 예쁜 카네이션 꽃과 선물을 드렸습니다.'\nPasangan partikel honorifik subjek dan penerima yang TEPAT adalah...",
        "correct": "께서 / 께 (께서 menggantikan partikel subjek 이/가 untuk orang yang dihormati; 께 menggantikan partikel objek penerima 에게/한테).",
        "distractors": [
            "께 / 께서 (urutan terbalik yang keliru menempatkan partikel subjek pada posisi penerima objek tidak langsung).",
            "께서 / 에게 (ketidakkonsistenan penghormatan dengan menggunakan partikel biasa 에게 untuk ibu).",
            "이 / 한테 (ragam bahasa akrab informal yang merendahkan kedudukan orang tua kandung).",
            "께서는 / 에서 (kesalahan menggunakan partikel tempat spasial 에서 untuk manusia)."
        ],
        "formula": {
            "title": "PARTIKEL HONORIFIK SUBJEK & DATIVUS (HONORIFIC PARTICLES)",
            "latex": "\\text{Subjek Dihormati} + \\mathbf{께서} \\quad | \\quad \\text{Penerima Aksi Dihormati} + \\mathbf{께} \\quad (\\text{verba bantu: } \\mathbf{드리다})",
            "legend": "• 어머니께서 (Ibu sebagai subjek mulia).<br>• 어머니께 꽃을 드리다 (Mempersembahkan bunga kepada Ibu)."
        },
        "hints": {
            "concept": "Dalam sistem honorifik Korea: Partikel subjek '이/가' digantikan oleh '께서' untuk subjek mulia (어머니께서). Partikel dative/penerima '에게/한테' (kepada) digantikan oleh '께' (어머니께), yang biasanya dipadukan dengan verba memberi khusus '드리다'.",
            "execution": "Subjek ibu = 께서; Memberi kepada ibu = 께. Pasangan: 께서 / 께."
        }
    },
    {
        "id": "kor-lat-m-06",
        "materi": "TATA BAHASA: DUA TINDAKAN SIMULTAN (-(으)면서)",
        "topic": "Menyatakan Dua Tindakan yang Dilakukan Bersamaan oleh Satu Pelaku",
        "stem": "Kebiasaan belajar seorang siswa teladan:\n'저는 저녁마다 클래식 음악을 ( ... ) 한국어 단어를 외웁니다.'\nBentuk konjugasi tindakan simultan (-(으)면서) yang TEPAT dari kata kerja tidak beraturan '듣다' (mendengarkan, ber-batchim ㄷ tak beraturan) adalah...",
        "correct": "들으면서 (konsonan batchim ㄷ berubah menjadi ㄹ saat bertemu akhiran yang diawali huruf vokal 으: 듣- + 으면서 -> 들으면서).",
        "distractors": [
            "듣으면서 (kesalahan tidak menerapkan hukum perubahan fonologis konsonan ㄷ tidak beraturan).",
            "듣면서 (kesalahan menghilangkan vokal penyambung 으 pada akar ber-batchim).",
            "들면서 (kesalahan menghilangkan suku kata dasar verba 들-).",
            "듣고 (hanya menyatakan urutan tindakan terpisah, bukan dua kegiatan simultan bersamaan)."
        ],
        "formula": {
            "title": "AKHIRAN SIMULTAN & IRREGULAR ㄷ: -(으)면서",
            "latex": "\\text{듣다 (ㄷ Irregular)} + \\mathbf{-(으)면서} \\quad \\implies \\quad \\mathbf{들으면서} \\quad (ㄷ \\rightarrow ㄹ)",
            "legend": "• Dilakukan oleh satu subjek pada saat yang persis bersamaan.<br>• Konsonan ㄷ pada 듣다 berubah menjadi ㄹ saat bertemu vokal."
        },
        "hints": {
            "concept": "Akhiran '-(으)면서' berarti 'sambil' (dua aksi bersamaan oleh subjek yang sama). Kata kerja '듣다' adalah kata kerja tidak beraturan 'ㄷ 불규칙': ketika bertemu akhiran yang diawali vokal (seperti -으면서), konsonan batchim 'ㄷ' berubah menjadi 'ㄹ' -> '들으면서'.",
            "execution": "듣다 + -(으)면서 = '들으면서'."
        }
    },
    {
        "id": "kor-lat-m-07",
        "materi": "TATA BAHASA: PENGUNGKAPAN NIAT/RENCANA (-(으)려고 하다)",
        "topic": "Menyatakan Kehendak/Rencana Masa Depan yang Sedang Dipersiapkan",
        "stem": "Rencana setelah lulus sekolah menengah atas:\n'저는 고등학교를 졸업한 후에 한국 대학교에서 컴퓨터공학을 ( ... ). 그래서 요즘 한국어를 열심히 공부하고 있습니다.'\nBentuk pengungkapan rencana (-(으)려고 하다) yang TEPAT dari verba '전공하다' (mengambil jurusan) adalah...",
        "correct": "전공하려고 합니다 (akar kata kerja berakhiran vokal 하- berpasangan dengan -려고 하다).",
        "distractors": [
            "전공하으려고 합니다 (kesalahan memasukkan vokal 으 pada akar kata yang berakhiran vokal).",
            "전공하기 때문입니다 (akhiran alasan penyebab yang tidak menyatakan rencana masa depan).",
            "전공할 수 있습니다 (hanya menyatakan kapabilitas, bukan rencana tindakan sengaja).",
            "전공해야 합니다 (hanya menyatakan beban kewajiban mutlak, bukan niat pribadi)."
        ],
        "formula": {
            "title": "RENCANA / INTENSI: -(으)려고 하다 (INTEND TO)",
            "latex": "\\text{Akar Vokal / ㄹ} + \\mathbf{-려고 \\text{ } 하다} \\quad \\leftrightarrow \\quad \\text{Akar Konsonan (selain ㄹ)} + \\mathbf{-으려고 \\text{ } 하다}",
            "legend": "• 전공하- (vokal) $\\rightarrow$ 전공하려고 합니다.<br>• Menyatakan niat yang telah dipikirkan matang-matang."
        },
        "hints": {
            "concept": "Pola kalimat untuk menyatakan maksud, niat, atau rencana adalah '-(으)려고 하다' (bermaksud untuk...). Jika akar kata kerja berakhiran vokal, gunakan '-려고 하다' (전공하다 -> 전공하- + 려고 합니다 = 전공하려고 합니다).",
            "execution": "전공하다 + niat = '전공하려고 합니다'."
        }
    },
    {
        "id": "kor-lat-m-08",
        "materi": "TATA BAHASA: URUTAN WAKTU SEBELUM (-기 전에) & SESUDAH (-(으)ㄴ 후에)",
        "topic": "Struktur Gramatikal 'Sebelum Makan Obat' dan 'Setelah Sarapan'",
        "stem": "Petunjuk minum obat dari dokter klinik:\n'약사: 식사를 ( ... ) 30분 뒤에 이 약을 꼭 드세요. 빈속에 약을 ( ... ) 위가 아플 수 있습니다.'\nPasangan bentuk kata kerja '하다' (setelah makan) dan '먹다' (sebelum minum obat) yang TEPAT adalah...",
        "correct": "한 후에 / 먹기 전에 (-(으)ㄴ 후에 untuk menyatakan urutan sesudah; -기 전에 untuk menyatakan urutan sebelum).",
        "distractors": [
            "하기 전에 / 먹은 후에 (urutan logika medis terbalik yang menyuruh minum obat sebelum makan).",
            "하고 / 먹어서 (kombinasi konjungsi biasa yang tidak mengekspresikan klausula pembatasan waktu obat).",
            "하러 / 먹으려고 (akhiran tujuan pergerakan yang salah konteks medis).",
            "하면 / 먹으면 (kombinasi pengandaian ganda yang membingungkan aturan minum obat)."
        ],
        "formula": {
            "title": "URUTAN WAKTU: -기 전에 (BEFORE) VS -(으)ㄴ 후에 (AFTER)",
            "latex": "\\text{Akar Verba} + \\mathbf{-기 \\text{ } 전에} \\quad \\leftrightarrow \\quad \\text{Akar Verba} + \\mathbf{-(으)ㄴ \\text{ } 후에}",
            "legend": "• 식사를 한 후에: setelah makan.<br>• 약을 먹기 전에: sebelum minum obat.<br>• Struktur baku pedoman medis dan instruksi harian."
        },
        "hints": {
            "concept": "Dua penanda urutan kronologis penting: 1) '-(으)ㄴ 후에' = setelah (식사를 하다 -> 식사를 한 후에 30분 뒤에); 2) '-기 전에' = sebelum (약을 먹다 -> 약을 먹기 전에).",
            "execution": "Setelah makan = 한 후에; Sebelum minum obat = 먹기 전에."
        }
    },
    {
        "id": "kor-lat-m-09",
        "materi": "TATA BAHASA: ATURAN KEHARUSAN (-아야/어야 하다/되다)",
        "topic": "Menyatakan Kewajiban Masuk Tepat Waktu Menggunakan Harmoni Vokal",
        "stem": "Instruksi pengawas ruang ujian TKA:\n'수험생 여러분, 시험 시작 15분 전까지 반드시 시험실에 ( ... ). 늦으면 입실할 수 없습니다.'\nBentuk pernyataan keharusan mutlak yang TEPAT dari kata kerja '입실하다' (masuk ruang) adalah...",
        "correct": "입실해야 합니다 (verba 하다 berpadu dengan keharusan -아야/어야 하다 menjadi 해야 합니다).",
        "distractors": [
            "입실하어야 합니다 (kesalahan tidak mengonjugasikan akar 하- menjadi 해).",
            "입실해도 됩니다 (bentuk yang menyatakan izin kebolehan 'boleh', bertentangan dengan kata wajib 반드시).",
            "입실하면 안 됩니다 (bentuk larangan yang menyatakan 'tidak boleh masuk', kontradiktif).",
            "입실할 수 있습니다 (hanya menyatakan kapabilitas, bukan kewajiban peraturan)."
        ],
        "formula": {
            "title": "KEWAJIBAN / KEHARUSAN: -아야/어야 하다/되다 (MUST)",
            "latex": "\\text{Akar Vokal } \\mathbf{ㅏ, ㅗ} + \\mathbf{-아야 \\text{ } 하다} \\quad | \\quad \\mathbf{하-} \\rightarrow \\mathbf{해야 \\text{ } 하다/되다}",
            "legend": "• 반드시 (wajib/harus) menjadi penanda kuat kewajiban.<br>• 입실하다 $\\rightarrow$ 입실해야 합니다 (Wajib masuk ruangan)."
        },
        "hints": {
            "concept": "Pola kalimat keharusan 'harus/wajib melakukan sesuatu' dibentuk dengan: akar kata kerja + '-아야/어야 하다' (atau '되다'). Seluruh verba yang berakhiran '하다' selalu berubah menjadi '해야 하다' (입실하다 -> 입실해야 합니다).",
            "execution": "입실하다 + harus = '입실해야 합니다'."
        }
    },
    {
        "id": "kor-lat-m-10",
        "materi": "TATA BAHASA: IZIN (-아/어도 되다) VS LARANGAN (-(으)면 안 되다)",
        "topic": "Pasangan Kontras Boleh Mengambil Gambar vs Dilarang Menyentuh Benda Museum",
        "stem": "Tata tertib pengunjung di museum seni nasional:\n'이곳에서는 사진을 ( ... ). 하지만 전시된 작품을 손으로 ( ... ).'\nPasangan bentuk izin kebolehan (-아/어도 되다) dan larangan (-(으)면 안 되다) yang TEPAT adalah...",
        "correct": "찍어도 됩니다 / 만지면 안 됩니다 (찍다 bervokal ㅣ berpadu dengan -어도 되다; 만지다 berakar vokal berpasangan dengan -면 안 되다).",
        "distractors": [
            "찍으면 안 됩니다 / 만져도 됩니다 (makna terbalik yang membahayakan koleksi karya seni museum).",
            "찍어야 합니다 / 만지지 마세요 (bentuk klausa pertama mewajibkan memotret foto, bukan izin).",
            "찍어도 됩니다 / 만져야 합니다 (klausa kedua keliru mewajibkan pengunjung menyentuh lukisan).",
            "찍기 전에 / 만진 후에 (kombinasi penanda kronologis waktu yang salah fungsi semantik regulasi)."
        ],
        "formula": {
            "title": "IZIN (-아/어도 되다) VS LARANGAN (-(으)면 안 되다)",
            "latex": "\\mathbf{-아/어도 \\text{ } 되다} \\text{ (Boleh/Diizinkan)} \\quad \\leftrightarrow \\quad \\mathbf{-(으)면 \\text{ } 안 \\text{ } 되다} \\text{ (Tidak Boleh/Dilarang)}",
            "legend": "• 사진을 찍어도 됩니다: Boleh memotret.<br>• 손으로 만지면 안 됩니다: Tidak boleh menyentuh dengan tangan."
        },
        "hints": {
            "concept": "1) Menyatakan izin kebolehan (boleh): akar verba + '-아/어도 되다' (찍다 -> 찍어도 됩니다). 2) Menyatakan larangan (tidak boleh): akar verba + '-(으)면 안 되다' (만지다 -> 만지면 안 됩니다).",
            "execution": "Boleh memotret = 찍어도 됩니다; Tidak boleh menyentuh = 만지면 안 됩니다."
        }
    },
    {
        "id": "kor-lat-m-11",
        "materi": "TATA BAHASA: PENGALAMAN MASA LALU (-(으)ㄴ 적이 있다/없다)",
        "topic": "Menyatakan Pernah atau Belum Pernah Mengalami Suatu Pengalaman",
        "stem": "Percakapan tentang pengalaman budaya Korea:\n'가: 수진 씨는 한복을 ( ... )?\n나: 네, 지난번 추석 때 한국 친구 집에서 한복을 ( ... ). 정말 아름다웠어요.'\nPasangan bentuk kalimat yang TEPAT untuk menanyakan dan mengonfirmasi pengalaman 'pernah mengenakan pakaian hanbok' adalah...",
        "correct": "입은 적이 있습니까 / 입어 본 적이 있어요 (akar ber-batchim 입- berpadu dengan penanda pengalaman -(으)ㄴ 적이 있다).",
        "distractors": [
            "입은 적이 없습니까 / 입은 적이 없어요 (klausa kedua menyatakan tidak pernah, bertentangan dengan kata ya dan kenangan indah).",
            "입으려고 합니까 / 입고 있어요 (menanyakan niat dan menyatakan sedang berlangsung, bukan menanyakan pengalaman lampau).",
            "입어도 됩니까 / 입어야 해요 (menanyakan izin dan menyatakan kewajiban, salah konteks wacana).",
            "입지 않습니까 / 입지 않아요 (menanyakan negasi biasa tanpa muatan makna pengalaman historis)."
        ],
        "formula": {
            "title": "PENGALAMAN: -(으)ㄴ 적이 있다/없다 (HAVE EVER / NEVER)",
            "latex": "\\text{Akar Ber-Batchim} + \\mathbf{-은 \\text{ } 적이 \\text{ } 있다} \\quad | \\quad \\text{Mencoba: } \\mathbf{-아/어 \\text{ } 본 \\text{ } 적이 \\text{ } 있다}",
            "legend": "• 한복을 입은 적이 있습니까? (Pernahkah Anda mengenakan hanbok?).<br>• 입어 본 적이 있어요 (Saya pernah mencobanya)."
        },
        "hints": {
            "concept": "Pola kalimat untuk menyatakan pengalaman 'pernah/tidak pernah melakukan sesuatu' adalah: akar verba + '-(으)ㄴ 적이 있다/없다' (atau dipadukan dengan mencoba: '-아/어 본 적이 있다'). Akar '입다' (ber-batchim) menjadi '입은 적이 있다'.",
            "execution": "입은 적이 있습니까 / 입어 본 적이 있어요."
        }
    },
    {
        "id": "kor-lat-m-12",
        "materi": "TATA BAHASA: PENGANDAIAN SYARAT (-(으)면)",
        "topic": "Penggunaan Akhiran Bersyarat '-(으)면' dengan Perubahan Konsonan Batchim ㅂ Tak Beraturan",
        "stem": "Saran dari seorang pemandu wisata saat musim dingin di pegunungan:\n'가: 산 정상에 올라가면 바람이 많이 불어서 매우 ( ... ) 어떻게 하지요?\n나: 날씨가 ( ... ) 이 두꺼운 패딩 점퍼와 장갑을 착용하십시오.'\nBentuk konjugasi bersyarat (-(으)면) dari kata sifat tidak beraturan '춥다' (dingin) adalah...",
        "correct": "추우면 (konsonan batchim ㅂ meleleh menjadi vokal 우 saat bertemu akhiran kondisional: 춥- + 으면 -> 추우면).",
        "distractors": [
            "춥으면 (kesalahan mempertahankan konsonan batchim ㅂ tanpa menerapkan hukum irregular ㅂ).",
            "춥면 (kesalahan menghilangkan vokal penghubung 으 pada akar ber-batchim).",
            "추우니까 (akhiran sebab akibat yang kurang tepat untuk klausula murni bersyarat hipotetikal).",
            "추워서 (akhiran sebab akibat yang dilarang berpasangan dengan kalimat perintah sopan 착용하십시오)."
        ],
        "formula": {
            "title": "SYARAT BERSYARAT (-(으)면) & ㅂ IRREGULAR",
            "latex": "\\text{춥다 (ㅂ Irregular)} + \\mathbf{-(으)면} \\quad \\implies \\quad \\mathbf{추우면} \\quad (ㅂ \\rightarrow 우)",
            "legend": "• Kata sifat/verba dengan batchim ㅂ (춥다, 덥다, 어렵다, 쉽다) melebur ㅂ $\\rightarrow$ 우.<br>• 추우면 (Jika dingin...)."
        },
        "hints": {
            "concept": "Kata sifat '춥다' tergolong dalam 'ㅂ 불규칙' (konsonan ㅂ tidak beraturan). Saat bertemu akhiran yang diawali huruf vokal (seperti -(으)면), batchim 'ㅂ' berubah menjadi '우': 춥- -> 추우- + 면 = '추우면' (jika dingin).",
            "execution": "춥다 + -(으)면 = '추우면'."
        }
    },
    {
        "id": "kor-lat-m-13",
        "materi": "TATA BAHASA: MENYATAKAN DURASI WAKTU BERLALU (-(으)ㄴ 지 ... 되다)",
        "topic": "Menyatakan Lama Waktu Sejak Suatu Kejadian Lampau Dimulai",
        "stem": "Pertanyaan wawancara adaptasi hidup di Korea:\n'가: 민수 씨, 한국에 ( ... ) 얼마나 되었습니까?\n나: 한국에 ( ... ) 벌써 2년이 다 되었습니다.'\nBentuk konjugasi penanda durasi waktu yang TEPAT dari verba '오다' (datang) adalah...",
        "correct": "온 지 / 온 지 (akar kata kerja tanpa batchim 오- berpadu dengan penanda durasi kala lampau -ㄴ 지).",
        "distractors": [
            "오는 지 (bentuk waktu sekarang yang salah fungsi karena kedatangan ke Korea sudah terjadi di masa lampau).",
            "왔는 지 (kesalahan menyematkan penanda lampau 았 pada struktur baku durasi -ㄴ 지).",
            "오기 전에 (bermakna sebelum datang, bertentangan dengan durasi waktu 2 tahun yang sudah dilalui).",
            "오면서 (akhiran tindakan simultan yang merusak makna durasi waktu berlalu)."
        ],
        "formula": {
            "title": "DURASI WAKTU BERLALU: -(으)ㄴ 지 ... 되다/지나다",
            "latex": "\\text{Akar Verba} + \\mathbf{-(으)ㄴ \\text{ } 지} + \\text{Durasi Waktu} + \\mathbf{되다/지나다}",
            "legend": "• 오- (vokal) $\\rightarrow$ 온 지 2년이 되었습니다 (Sudah genap 2 tahun sejak saya datang ke Korea).<br>• Wajib menggunakan spasi antara '지' dan durasi."
        },
        "hints": {
            "concept": "Rumus baku untuk menyatakan durasi waktu yang telah berlalu sejak suatu peristiwa dilakukan adalah: akar kata kerja + '-(으)ㄴ 지 + keterangan waktu + 되다/지나다'. Akar kata '오다' (tanpa batchim) menjadi '온 지' (한국에 온 지 2년이 되었습니다).",
            "execution": "오다 + durasi waktu berlalu = '온 지'."
        }
    },
    {
        "id": "kor-lat-m-14",
        "materi": "TATA BAHASA HONORIFIK: KATA KERJA TIDAK BERATURAN DENGAN INFIKS '-(으)시-'",
        "topic": "Konjugasi Verba Ber-batchim ㄹ (만들다) dan Verba Ber-batchim ㅅ (낫다) dengan Honorifik",
        "stem": "Keluarga membicarakan masakan lezat dan kesembuhan nenek:\n'할머니께서 우리를 위해 맛있는 불고기를 손수 ( ... ). 그리고 감기가 다 ( ... ) 정말 다행입니다.'\nPasangan bentuk honorifik yang TEPAT dari verba '만들다' (membuat, batchim ㄹ) dan '낫다' (sembuh, batchim ㅅ) adalah...",
        "correct": "만드셨습니다 / 나으셔서 (batchim ㄹ luluh saat bertemu infiks honorifik -(으)시- menjadi 만드시다; batchim ㅅ luluh saat bertemu vokal menjadi 나으시다).",
        "distractors": [
            "만들으셨습니다 / 낫으셔서 (kesalahan tidak meluluhkan konsonan ㄹ dan konsonan ㅅ sesuai kaidah irregular).",
            "만드셨습니다 / 낫으셔서 (kesalahan mempertahankan konsonan ㅅ pada kata 낫다).",
            "만들었습니다 / 나아서 (bentuk biasa tanpa honorifik yang merendahkan kedudukan nenek kandung).",
            "만드시었습니다 / 나으시어서 (bentuk analitis panjang yang kaku dan jarang digunakan dalam tuturan wajar)."
        ],
        "formula": {
            "title": "HONORIFIK DENGAN IRREGULAR ㄹ & ㅅ",
            "latex": "\\text{만들다 (ㄹ Drop)} + \\text{-(으)시-} \\rightarrow \\mathbf{만드시다} \\quad | \\quad \\text{낫다 (ㅅ Drop)} + \\text{-(으)시-} \\rightarrow \\mathbf{나으시다}",
            "legend": "• Konsonan ㄹ luluh di depan konsonan ㄴ, ㅂ, ㅅ, atau vokal 으 $\\rightarrow$ 만드시다.<br>• Konsonan ㅅ luluh di depan vokal $\\rightarrow$ 나으시다."
        },
        "hints": {
            "concept": "Dua aturan irregular penting pada honorifik: 1) 'ㄹ 탈락' (peluluhan ㄹ): '만들다' bertemu '-(으)시-' -> konsonan ㄹ dan vokal 으 hilang menjadi '만드시다' (만드셨습니다). 2) 'ㅅ 불규칙' (ㅅ tidak beraturan): '낫다' bertemu vokal -> ㅅ hilang menjadi '나으시다' (나으셔서).",
            "execution": "만들다 -> 만드셨습니다; 낫다 -> 나으셔서."
        }
    },
    {
        "id": "kor-lat-m-15",
        "materi": "TATA BAHASA: PENGGUNAAN BENTUK DUGAAN / PROBABILITAS (-(으)ㄹ 것 같다)",
        "topic": "Menyatakan Dugaan Berdasarkan Pengamatan Cuaca Langit Mendung",
        "stem": "Melihat langit sore yang gelap dan berangin kencang:\n'하늘에 먹구름이 가득 끼고 천둥이 치는 것을 보니 곧 소나기가 ( ... ). 우산을 챙기세요.'\nBentuk ungkapan dugaan masa depan yang TEPAT dari kata kerja '오다' (turun hujan) adalah...",
        "correct": "올 것 같아요 (akar kata kerja berakhiran vokal 오- berpadu dengan penanda dugaan -(으)ㄹ 것 같다).",
        "distractors": [
            "오는 것 같아요 (bentuk dugaan untuk peristiwa yang sedang berlangsung saat ini, padahal hujan baru akan turun).",
            "온 것 같아요 (bentuk dugaan lampau yang mengasumsikan hujan sudah selesai turun).",
            "오기 때문이에요 (menegaskan fakta alasan kausal pasti, bukan perkiraan dugaan berdasarkan tanda alam).",
            "오지 않을 수 없어요 (ungkapan ganda 'pasti turun tanpa terhindarkan' yang terlalu mutlak dan kaku)."
        ],
        "formula": {
            "title": "DUGAAN / PERKIRAAN: -(으)ㄹ 것 같다 (IT SEEMS / PROBABLY)",
            "latex": "\\text{Akar Verba} + \\mathbf{-(으)ㄹ \\text{ } 것 \\text{ } 같다} \\quad (\\text{오-} + \\mathbf{-ㄹ \\text{ } 것 \\text{ } 같아요})",
            "legend": "• Menunjukkan perkiraan dugaan subjektif pembicara berdasarkan pengamatan tanda-tanda fisik.<br>•곧 (segera) mengindikasikan waktu yang akan datang $\\rightarrow$ -ㄹ 것 같다."
        },
        "hints": {
            "concept": "Pola kalimat dugaan/perkiraan masa depan berdasarkan tanda-tanda yang tampak (seperti langit mendung) adalah: akar verba + '-(으)ㄹ 것 같다' (tampaknya akan...). Kata kerja '오다' menjadi '올 것 같아요' (tampaknya hujan akan segera turun).",
            "execution": "오다 + dugaan masa depan = '올 것 같아요'."
        }
    },
    {
        "id": "kor-lat-m-16",
        "materi": "TATA BAHASA: BENTUK UPAYA / KEBIASAAN (-도록 하다)",
        "topic": "Instruksi Dokter untuk Memastikan Minum Air Putih Cukup Setiap Hari",
        "stem": "Instruksi dokter gizi kepada pasien pemulihan dehidrasi:\n'건강을 유지하기 위해서는 매일 물을 2리터 이상 ( ... ). 규칙적인 운동도 중요합니다.'\nBentuk instruksi anjuran memastikan upaya yang TEPAT dari verba '마시다' (minum) adalah...",
        "correct": "마시도록 하십시오 (akar kata kerja 마시- + akhiran instruksi upaya pemastian formal -도록 하다).",
        "distractors": [
            "마시게 되었습니다 (bentuk pasif akibat situasi di luar kendali yang salah tenses waktu).",
            "마실 뻔했습니다 (ungkapan nyaris/hampir saja minum air yang keliru makna).",
            "마시지 않도록 되었습니다 (kombinasi struktur negasi yang merusak maksud anjuran kesehatan).",
            "마시기로 했습니다 (hanya menyatakan keputusan sepihak yang telah disepakati sendiri)."
        ],
        "formula": {
            "title": "INSTRUKSI UPAYA / ANJURAN: -도록 하다 (MAKE SURE TO)",
            "latex": "\\text{Akar Kata Kerja} + \\mathbf{-도록 \\text{ } 하다/하십시오}",
            "legend": "• Menginstruksikan atau menganjurkan seseorang untuk mengupayakan tindakan tertentu.<br>• 마시다 $\\rightarrow$ 마시도록 하십시오."
        },
        "hints": {
            "concept": "Pola kalimat '-도록 하다' digunakan untuk menginstruksikan atau menyarankan lawan bicara agar berusaha sungguh-sungguh melakukan tindakan tertentu ('pastikanlah untuk...'). Verba '마시다' menjadi '마시도록 하십시오' (pastikanlah untuk meminum).",
            "execution": "마시다 + anjuran upaya = '마시도록 하십시오'."
        }
    },
    {
        "id": "kor-lat-m-17",
        "materi": "TATA BAHASA: PERUBAHAN KEADAAN DI LUAR KENDALI (-게 되다)",
        "topic": "Menyatakan Hasil Perubahan Situasi Mendapat Beasiswa Belajar ke Luar Negeri",
        "stem": "Kabar gembira dari seorang mahasiswa berprestasi:\n'열심히 준비한 결과, 다음 학기부터 정부 장학금을 받고 서울대학교에서 ( ... ). 정말 꿈만 같습니다.'\nBentuk pengungkapan perubahan keadaan situasi yang TEPAT dari kata kerja '공부하다' (belajar) adalah...",
        "correct": "공부하게 되었습니다 (akar verba 공부하- + akhiran perubahan takdir/situasi -게 되다).",
        "distractors": [
            "공부하도록 했습니다 (mengimplikasikan memaksa orang lain belajar, bukan hasil penerimaan beasiswa diri sendiri).",
            "공부할 뻔했습니다 (menyatakan 'nyaris saja belajar namun gagal', bertentangan dengan rasa syukur).",
            "공부하기로 들었습니다 (struktur kalimat rancu yang mencampuradukkan wicara tak langsung).",
            "공부해야 되었습니다 (kesalahan konstruksi waktu lampau keharusan yang kaku)."
        ],
        "formula": {
            "title": "PERUBAHAN KEADAAN / HASIL SITUASI: -게 되다 (COME TO / END UP)",
            "latex": "\\text{Akar Kata Kerja} + \\mathbf{-게 \\text{ } 되다} \\quad (\\text{공부하-} + \\mathbf{-게 \\text{ } 되었습니다})",
            "legend": "• Menunjukkan terjadinya suatu keadaan atau hasil baru karena faktor situasi eksternal/takdir.<br>• 'Menjadi bisa belajar di Universitas Nasional Seoul'."
        },
        "hints": {
            "concept": "Akhiran '-게 되다' digunakan untuk mengekspresikan bahwa suatu keadaan atau hasil baru telah terjadi karena pengaruh situasi luar atau keputusan resmi di luar kendali langsung pelaku semata ('akhirnya menjadi...'). Verba '공부하다' menjadi '공부하게 되었습니다'.",
            "execution": "공부하다 + perubahan keadaan = '공부하게 되었습니다'."
        }
    },
    {
        "id": "kor-lat-m-18",
        "materi": "TATA BAHASA: PENGUNGKAPAN KONTRASTIF SEDERHANA (-지만)",
        "topic": "Menghubungkan Dua Klausa Bertentangan Mengenai Harga Mahal dan Kualitas Bagus",
        "stem": "Ulasan barang elektronik laptop di situs belanja online:\n'이 노트북은 가격이 다소 ( ... ) 성능이 매우 우수하고 디자인도 세련되었습니다.'\nBentuk konjugasi pertentangan langsung (-지만) yang TEPAT dari kata sifat '비싸다' (mahal) adalah...",
        "correct": "비싸지만 (akar kata sifat 비싸- langsung dilekati akhiran pertentangan objektif -지만).",
        "distractors": [
            "비싸서 (akhiran sebab akibat yang mengimplikasikan mahal menyebabkan laptop tersebut bagus).",
            "비싸니까 (akhiran alasan subjektif yang tidak tepat untuk kontras harga vs kualitas).",
            "비싸면 (akhiran pengandaian jika yang keliru untuk laptop yang sudah dibeli dan diuji faktual).",
            "비싸면서 (akhiran simultan yang tidak lazim untuk mengontraskan harga dan keunggulan teknis)."
        ],
        "formula": {
            "title": "KONJUNGSI PERTENTANGAN: -지만 (BUT / NAMUN)",
            "latex": "\\text{Akar Kata (Verba/Adjektiva)} + \\mathbf{-지만} \\quad (\\text{비싸-} + \\mathbf{-지만})",
            "legend": "• Menghubungkan dua klausa yang saling bertolak belakang maknanya.<br>• Harga mahal, TETAPI performanya sangat unggul."
        },
        "hints": {
            "concept": "Akhiran '-지만' melekat langsung pada akar kata kerja atau kata sifat untuk menyatakan pertentangan lugas ('tetapi/namun'). Kata sifat '비싸다' menjadi '비싸지만' (harganya agak mahal, TETAPI performanya sangat unggul).",
            "execution": "비싸다 + tetapi = '비싸지만'."
        }
    },
    {
        "id": "kor-lat-m-19",
        "materi": "TATA BAHASA: KEPUTUSAN BERSAMA / PERJANJIAN (-기로 하다)",
        "topic": "Menyatakan Kesepakatan Jadwal Pertemuan Bersama Rekan Tim Proyek",
        "stem": "Hasil rapat kelompok tugas akhir mahasiswa:\n'프로젝트 과제를 완성하기 위해 이번 주 토요일 오후 2시에 도서관 스터디룸에서 ( ... ).'\nBentuk pengungkapan keputusan janji temu yang TEPAT dari verba '만나다' (bertemu) adalah...",
        "correct": "만나기로 했습니다 (akar verba 만나- + akhiran pemufakatan keputusan bersama -기로 하다).",
        "distractors": [
            "만나게 되었습니다 (mengimplikasikan peristiwa kebetulan tanpa rencana musyawarah kelompok).",
            "만나도록 했습니다 (mengimplikasikan menyuruh orang lain bertemu).",
            "만날 뻔했습니다 (bermakna nyaris saja bertemu namun akhirnya batal).",
            "만나야 되었습니다 (hanya menekankan beban keharusan masa lalu)."
        ],
        "formula": {
            "title": "KEPUTUSAN / JANJI TEMU: -기로 하다 (DECIDE TO)",
            "latex": "\\text{Akar Kata Kerja} + \\mathbf{-기로 \\text{ } 하다} \\quad (\\text{만나-} + \\mathbf{-기로 \\text{ } 했습니다})",
            "legend": "• Menunjukkan keputusan bersama atau resolusi pribadi yang telah disepakati.<br>• 'Telah sepakat untuk bertemu pada hari Sabtu'."
        },
        "hints": {
            "concept": "Pola kalimat '-기로 하다' (memutuskan untuk...) digunakan untuk menyatakan kesepakatan bersama, janji temu, atau rencana bulat yang telah diputuskan. Verba '만나다' menjadi '만나기로 했습니다' (telah memutuskan untuk bertemu).",
            "execution": "만나다 + keputusan janji = '만나기로 했습니다'."
        }
    },
    {
        "id": "kor-lat-m-20",
        "materi": "TATA BAHASA: KOMPARATIF PERBANDINGAN (-보다)",
        "topic": "Membandingkan Tingkat Kemudahan Transportasi Kereta Bawah Tanah Dibandingkan Bus",
        "stem": "Pendapat warga Seoul mengenai sistem transportasi umum:\n'출퇴근 시간대에는 교통 체증 때문에 버스( ... ) 지하철을 이용하는 것이 훨씬 빠르고 편리합니다.'\nPartikel komparatif yang TEPAT untuk menyatakan perbandingan 'daripada bus' adalah...",
        "correct": "보다 (partikel komparasi yang melekat pada nomina pembanding dan bermakna 'daripada').",
        "distractors": [
            "처럼 (partikel simile metafora yang bermakna 'seperti/laksana').",
            "만큼 (partikel ekuatif kesetaraan yang bermakna 'sebanyak/sebanding dengan').",
            "마저 (partikel inklusi ekstrem yang bermakna 'bahkan sampai... pun').",
            "따라 (partikel khusus yang menyatakan kebetulan pada hari tertentu)."
        ],
        "formula": {
            "title": "KOMPARATIF: NOMINA + 보다 (THAN / DARIPADA)",
            "latex": "\\text{Objek Pembanding} + \\mathbf{보다} + \\text{Subjek Unggul} + \\mathbf{훨씬 / 더} + \\text{Adjektiva}",
            "legend": "• 버스보다 지하철이 훨씬 빠르다.<br>• Partikel '보다' SELALU dilekatkan pada benda yang kalah/dibandingkan (bus)."
        },
        "hints": {
            "concept": "Partikel komparasi '보다' berarti 'daripada'. Partikel ini dilekatkan langsung pada kata benda yang menjadi standar pembanding: '버스보다 지하철이 훨씬 빠릅니다' (kereta subway jauh lebih cepat DARIPADA bus).",
            "execution": "Daripada bus = '버스보다'."
        }
    },
    {
        "id": "kor-lat-m-21",
        "materi": "TATA BAHASA: PENGUNGKAPAN KESIAPAN / STATUS TINDAKAN (-고 있다)",
        "topic": "Menyatakan Tindakan Progresif yang Sedang Berlangsung Saat Ini (-고 있다)",
        "stem": "Jawaban seseorang saat menerima panggilan telepon di tengah kesibukan:\n'가: 민수 씨, 지금 통화할 시간 괜찮으세요?\n나: 죄송하지만 제가 지금 거래처 고객과 중요한 상담을 ( ... ). 10분 뒤에 다시 전화 드리겠습니다.'\nBentuk kala sedang berlangsung (progresif) yang TEPAT dari verba '하다' adalah...",
        "correct": "하고 있습니다 (akar verba 하- + akhiran progresif formal -고 있다).",
        "distractors": [
            "한 적이 있습니다 (menyatakan pengalaman lampau, bertentangan dengan situasi panggilan masuk saat ini).",
            "할 뻔했습니다 (menyatakan nyaris melakukan sesuatu).",
            "하고 싶었습니다 (menyatakan keinginan masa lampau).",
            "하지 않기로 했습니다 (menyatakan pembatalan kesepakatan konseling)."
        ],
        "formula": {
            "title": "ASPEK PROGRESIF SEDANG BERLANGSUNG: -고 있다",
            "latex": "\\text{Akar Verba} + \\mathbf{-고 \\text{ } 있다} \\quad (\\text{상담을 하-} + \\mathbf{-고 \\text{ } 있습니다})",
            "legend": "• Menunjukkan aktivitas yang sedang dilakukan secara aktif tepat pada detik pembicaraan berlangsung."
        },
        "hints": {
            "concept": "Pola kalimat untuk menyatakan aspek tindakan yang sedang berlangsung (progresif / sedang melakukan...) adalah: akar kata kerja + '-고 있다'. Kata kerja '하다' menjadi '하고 있습니다' (sedang melakukan konsultasi).",
            "execution": "하다 + sedang berlangsung = '하고 있습니다'."
        }
    },
    {
        "id": "kor-lat-m-22",
        "materi": "TATA BAHASA: KONDISI KELANJUTAN HASIL TINDAKAN (-아/어 있다)",
        "topic": "Menyatakan Kondisi Bertahan Pasca Aksi Intransitif Duduk (앉아 있다) vs Membuka Pintu",
        "stem": "Deskripsi ruang tunggu klinik dokter:\n'대기실 소파에는 환자들이 조용히 ( ... ), 벽에는 진료 안내문이 깔끔하게 붙( ... ).'\nPasangan bentuk status kondisi bertahan (-아/어 있다) yang TEPAT dari verba '앉다' (duduk) dan verba pasif '붙다' (menempel) adalah...",
        "correct": "앉아 있고 / 어 있습니다 (앉다 berakar vokal ㅏ berpadu dengan -아 있다; 붙다 berakar vokal ㅜ berpadu dengan -어 있다).",
        "distractors": [
            "앉고 있고 / 고 있습니다 (penggunaan -고 있다 yang keliru mengindikasikan gerakan fisik menurunkan pantat secara berulang terus menerus).",
            "앉아서 / 어서 (akhiran sebab akibat yang merusak struktur deskripsi ruangan statis).",
            "앉으면 / 으면 (akhiran pengandaian bersyarat yang tidak sesuai untuk mendeskripsikan fakta ruangan nyata).",
            "앉으려고 / 으려고 (akhiran niat masa depan yang salah fungsi)."
        ],
        "formula": {
            "title": "STATUS KONDISI BERTAHAN: -아/어 있다",
            "latex": "\\text{Verba Intransitif (Gerak/Posisi)} + \\mathbf{-아/어 \\text{ } 있다}",
            "legend": "• 앉아 있다: dalam kondisi sudah duduk dan tetap duduk (bukan sedang jongkok duduk).<br>• 붙어 있다: dalam kondisi tertempel rapi di dinding."
        },
        "hints": {
            "concept": "Untuk verba intransitif perubahan posisi tubuh atau keadaan statis (seperti 앉다=duduk, 서다=berdiri, 피다=mekar), kondisi hasil yang terus bertahan dinyatakan dengan '-아/어 있다' (bukan -고 있다). Maka '앉아 있고' dan '붙어 있습니다'.",
            "execution": "앉다 -> 앉아 있고; 붙다 -> 붙어 있습니다."
        }
    },
    {
        "id": "kor-lat-m-23",
        "materi": "TATA BAHASA: PENGUNGKAPAN KESULITAN/KEMUDAHAN (-기 쉽다/어렵다)",
        "topic": "Menyatakan Kerentanan Terkena Flu Saat Perubahan Suhu Ekstrem di Musim Pancaroba",
        "stem": "Peringatan ramalan cuaca pada masa pergantian musim (환절기):\n'요즘처럼 일교차가 10도 이상 크게 벌어지는 환절기에는 면역력이 떨어져 감기에 걸리( ... ). 건강 관리에 유의하십시오.'\nBentuk ungkapan yang TEPAT untuk menyatakan 'mudah terserang flu' dari verba '걸리다' adalah...",
        "correct": "걸리기 쉽습니다 (akar verba 걸리- + nomina penanda nominalisasi -기 + kata sifat 쉽다).",
        "distractors": [
            "걸리기 어렵습니다 (menyatakan 'sulit terserang flu', bertentangan dengan konteks bahaya pancaroba).",
            "걸릴 수 없습니다 (menyatakan ketidakmampuan mutlak terserang flu).",
            "걸리지 않아야 합니다 (struktur kalimat anjuran yang salah subjek).",
            "걸린 적이 없습니다 (hanya menyatakan rekam jejak pribadi belum pernah sakit flu)."
        ],
        "formula": {
            "title": "KECENDERUNGAN / KEMUDAHAN: -기 쉽다 (EASY TO / PRONE TO)",
            "latex": "\\text{Akar Verba} + \\mathbf{-기 \\text{ } 쉽다 (Mudah/Rentan)} \\quad \\leftrightarrow \\quad \\text{Akar Verba} + \\mathbf{-기 \\text{ } 어렵다 (Sulit)}",
            "legend": "• 감기에 걸리기 쉽다: Mudah/rentan terkena flu saat pergantian musim.<br>• -기 mengubah verba menjadi nomina tindakan."
        },
        "hints": {
            "concept": "Pola kalimat '-기 쉽다' berarti 'mudah untuk...' atau 'rentan mengalami...'. Akar kata kerja '걸리다' diubah menjadi nomina dengan '-기' lalu dipadukan dengan '쉽다' -> '걸리기 쉽습니다' (mudah terkena flu).",
            "execution": "걸리다 + mudah terkena = '걸리기 쉽습니다'."
        }
    },
    {
        "id": "kor-lat-m-24",
        "materi": "TATA BAHASA: PENGUNGKAPAN PERCOBAAN TINDAKAN (-아/어 보다)",
        "topic": "Saran Rekan Kerja untuk Mencicipi Masakan Pedas Tradisional",
        "stem": "Rekomendasi kuliner saat berkunjung ke pasar malam tradisional di Busan:\n'가: 부산에 오면 자갈치시장에서 신선한 생선회를 꼭 ( ... ). 정말 잊을 수 없는 맛이에요.\n나: 그래요? 그럼 오늘 저녁에 바로 가 볼게요.'\nBentuk saran percobaan tindakan (-아/어 보다) yang TEPAT dari verba '먹다' (makan) adalah...",
        "correct": "먹어 보세요 (akar verba 먹- bervokal ㅓ berpadu dengan -어 보다 menjadi bentuk anjuran mencoba 먹어 보세요).",
        "distractors": [
            "먹아 보세요 (kesalahan harmoni vokal ㅓ yang keliru digabungkan dengan 아).",
            "먹으면 안 됩니다 (larangan mencicipi makanan yang kontradiktif dengan pujian lezat).",
            "먹도록 했습니다 (bentuk pemaksaan otoritatif yang tidak cocok untuk saran wisata santai).",
            "먹기 전에 (klausula waktu yang menggantung tanpa predikat utama)."
        ],
        "formula": {
            "title": "MENCOBA MELAKUKAN SESUATU: -아/어 보다 (TRY DOING)",
            "latex": "\\text{Akar Verba} + \\mathbf{-아/어 \\text{ } 보다} \\quad (\\text{먹-} + \\mathbf{-어 \\text{ } 보세요})",
            "legend": "• Menganjurkan seseorang untuk mencoba suatu pengalaman baru.<br>• 꼭 먹어 보세요: Pastikan Anda mencobanya!"
        },
        "hints": {
            "concept": "Pola kalimat untuk menganjurkan seseorang mencoba melakukan sesuatu ('cobalah lakukan...') adalah: akar verba konjugasi vokal (-아/어) + '보다'. Verba '먹다' menjadi '먹어 보세요' (cobalah cicipi/makan).",
            "execution": "먹다 + anjuran mencoba = '먹어 보세요'."
        }
    },
    {
        "id": "kor-lat-m-25",
        "materi": "TATA BAHASA: PENGUNGKAPAN PENYESALAN LAMPAU (-(으)ㄹ 걸 그랬다)",
        "topic": "Penyesalan Karena Tidak Membawa Payung Saat Kehujanan",
        "stem": "Keluhan seorang pejalan kaki yang basah kuyup terkena hujan lebat:\n'일기예보에서 오후에 비가 온다고 했는데 아침에 우산을 ( ... ). 옷이 다 젖어 버렸어요.'\nBentuk pengungkapan rasa penyesalan atas tindakan yang tidak dilakukan di masa lalu (-(으)ㄹ 걸 그랬다) dari verba '챙기다' (menyiapkan/membawa) adalah...",
        "correct": "챙길 걸 그랬어요 (akar verba 챙기- tanpa batchim berpadu dengan penanda penyesalan kontrafaktual -ㄹ 걸 그랬다).",
        "distractors": [
            "챙기지 말 걸 그랬어요 (menyesal karena telah membawa payung, bertentangan dengan baju yang basah kuyup).",
            "챙길 수 있었어요 (hanya menyatakan kemampuan teoritis tanpa nuansa ratapan penyesalan emosional).",
            "챙기려고 했어요 (hanya menyatakan niat yang tidak tuntas tanpa penyesalan mendalam).",
            "챙기게 되었어요 (menyatakan hasil perubahan situasi di luar kehendak)."
        ],
        "formula": {
            "title": "PENYESALAN LAMPAU: -(으)ㄹ 걸 그랬다 (SHOULD HAVE DONE)",
            "latex": "\\text{Akar Verba} + \\mathbf{-(으)ㄹ \\text{ } 걸 \\text{ } 그랬다} \\quad (\\text{챙기-} + \\mathbf{-ㄹ \\text{ } 걸 \\text{ } 그랬어요})",
            "legend": "• Mengekspresikan penyesalan mendalam karena tidak melakukan tindakan yang seharusnya dilakukan.<br>• 'Seharusnya saya bawa payung tadi pagi...'"
        },
        "hints": {
            "concept": "Pola kalimat '-(으)ㄹ 걸 그랬다' digunakan untuk mengekspresikan penyesalan atas hal yang tidak dilakukan di masa lalu ('seharusnya saya...'). Akar kata '챙기다' (tanpa batchim) menjadi '챙길 걸 그랬어요' (seharusnya tadi pagi saya membawa payung).",
            "execution": "챙기다 + penyesalan lampau = '챙길 걸 그랬어요'."
        }
    }
]
