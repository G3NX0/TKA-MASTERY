# -*- coding: utf-8 -*-
"""
BAHASA KOREA - PAKET SOAL LATIHAN TINGKAT TINGGI (HARD) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / TOPIK II Level 3-4 (CEFR B1-B2)
Distribusi:
- 8 Butir: Wicara Tak Langsung (간접화법: -다고 하다, -냐고 하다, -(으)라고 하다, -자고 하다)
- 9 Butir: Bentuk Pasif & Kausatif (피동/사동: -이/히/리/기-) & Aspek Lanjutan (-는 바람에, -(으)ㄹ 수밖에 없다)
- 8 Butir: Analisis Wacana Tingkat Tinggi (HOTS: 고령화 사회, 분리배출, 한글 창제, 한류의 지속가능성)
"""

BAHASA_KOREA_HARD_ITEMS = [
    {
        "id": "kor-lat-h-01",
        "materi": "TATA BAHASA: WICARA TAK LANGSUNG PERNYATAAN (-다고 하다)",
        "topic": "Transformasi Kalimat Deklaratif Langsung Verba Kala Sekarang Menjadi Wicara Tak Langsung",
        "stem": "Dalam rapat koordinasi proyek, manajer mengutip laporan analis riset pasar:\n'김 대리가 말했습니다: \"소비자들의 친환경 제품 선호도가 해마다 크게 증가합니다.\"\nJika tuturan langsung di atas diubah menjadi kalimat wicara tak langsung (간접화법) dengan verba tindakan '증가하다', bentuk yang TEPAT adalah...",
        "correct": "증가한다고 했습니다 (akar kata kerja berakhiran vokal 하- pada waktu sekarang berpasangan dengan akhiran kutipan tidak langsung -ㄴ다고 하다).",
        "distractors": [
            "증가하다고 했습니다 (kesalahan memperlakukan kata kerja tindakan seperti kata sifat tanpa partikel aspek ㄴ).",
            "증가하냐고 했습니다 (bentuk kutipan tidak langsung untuk kalimat tanya/interogatif).",
            "증가하라고 했습니다 (bentuk kutipan tidak langsung untuk kalimat instruksi perintah imperatif).",
            "증가하자고 했습니다 (bentuk kutipan tidak langsung untuk kalimat usulan ajakan bersama propositif)."
        ],
        "formula": {
            "title": "WICARA TAK LANGSUNG PERNYATAAN (INDIRECT SPEECH: -다고 하다)",
            "latex": "\\text{Verba Vokal (Présent)} + \\mathbf{-ㄴ다고 \\text{ } 하다} \\quad | \\quad \\text{Verba Batchim} + \\mathbf{-는다고 \\text{ } 하다} \\quad | \\quad \\text{Adjektiva} + \\mathbf{-다고 \\text{ } 하다}",
            "legend": "• 증가하다 adalah kata kerja berakhiran vokal 하- $\\rightarrow$ 증가한다고 하다.<br>• Untuk kata sifat (크다, 예쁘다): 크다고 하다, 예쁘다고 하다."
        },
        "hints": {
            "concept": "Aturan wicara tak langsung (간접화법) untuk kalimat pernyataan deklaratif waktu sekarang: 1) Verba (동사) berakhiran vokal -> '-ㄴ다고 하다' (증가하다 -> 증가한다고 하다); verba ber-batchim -> '-는다고 하다'. 2) Adjektiva (형용사) -> '-다고 하다'.",
            "execution": "증가하다 (verba vokal) -> '증가한다고 했습니다'."
        }
    },
    {
        "id": "kor-lat-h-02",
        "materi": "TATA BAHASA: WICARA TAK LANGSUNG PERINTAH (-(으)라고 하다)",
        "topic": "Transformasi Instruksi Dokter Minum Obat Tepat Waktu Menjadi Tuturan Tak Langsung",
        "stem": "Seorang pasien menceritakan instruksi dokter kepada keluarganya:\n'의사 선생님께서 말씀하셨습니다: \"이 약을 식사 후에 제시간에 꼭 드십시오.\"\nBentuk kutipan wicara tak langsung (간접화법) yang TEPAT untuk menyampaikan kembali perintah dokter di atas adalah...",
        "correct": "꼭 먹으라고 하셨습니다 (kalimat perintah langsung 드십시오 diubah menjadi verba dasar 먹다 yang ber-batchim + -(으)라고 하다 dengan honorifik pembicara 하셨습니다).",
        "distractors": [
            "꼭 드시라고 하셨습니다 (kesalahan umum mempertahankan verba honorifik 드시다 saat merujuk pada diri sendiri yang harus minum obat).",
            "꼭 먹는다고 하셨습니다 (bentuk pernyataan bahwa dokter yang meminum obat tersebut).",
            "꼭 먹자고 하셨습니다 (bentuk ajakan yang mengasumsikan dokter mengajak pasien minum obat bersama-sama).",
            "꼭 먹냐고 하셨습니다 (bentuk pertanyaan yang menanyakan apakah pasien sudah minum obat)."
        ],
        "formula": {
            "title": "WICARA TAK LANGSUNG PERINTAH (INDIRECT IMPERATIVE: -(으)라고 하다)",
            "latex": "\\text{Kalimat Perintah Langsung} \\implies \\text{Akar Verba Dasar} + \\mathbf{-(으)라고 \\text{ } 하다}",
            "legend": "• Dokter menyuruh pasien (saya) makan $\\rightarrow$ verba kembali ke bentuk dasar '먹다' + '-(으)라고'.<br>• 먹- (ada batchim) $\\rightarrow$ 먹으라고 하셨습니다."
        },
        "hints": {
            "concept": "Aturan kutipan perintah tidak langsung: akar verba + '-(으)라고 하다'. Karena subjek yang disuruh makan obat adalah pembicara sendiri (saya), kata kerja honorifik '드시다' harus dinetralkan kembali menjadi kata kerja dasar '먹다' (먹으라고 하셨습니다) demi kesantunan menempatkan diri.",
            "execution": "Instruksi perintah makan = '먹으라고 하셨습니다'."
        }
    },
    {
        "id": "kor-lat-h-03",
        "materi": "TATA BAHASA: PENYEBAB DAMPAK NEGATIF (-는 바람에)",
        "topic": "Menyatakan Alasan Tak Terduga yang Mengakibatkan Kerugian atau Hambatan",
        "stem": "Penjelasan pembicara saat terlambat menghadiri wawancara kerja penting:\n'죄송합니다. 아침에 지하철 신호 장애로 열차가 갑자기 ( ... ) 면접 시간에 늦고 말았습니다.'\nBentuk konjugasi sebab akibat bernuansa musibah tak terduga (-는 바람에) dari verba '멈추다' (berhenti) adalah...",
        "correct": "멈추는 바람에 (akar kata kerja 멈추- + akhiran kausalitas peristiwa mendadak yang berdampak buruk -는 바람에).",
        "distractors": [
            "멈추기 때문에 (akhiran alasan netral objektif yang tidak membawa nuansa peristiwa mendadak pembawa sial).",
            "멈추는 덕분에 (akhiran kausalitas positif 'berkat/untunglah', sangat bertolak belakang dengan keterlambatan wawancara).",
            "멈추더라도 (akhiran konsesif 'meskipun', merusak hubungan sebab akibat peristiwa).",
            "멈추자마자 (hanya menyatakan kesegeraan waktu, bukan alasan kegagalan tiba tepat waktu)."
        ],
        "formula": {
            "title": "KAUSALITAS DAMPAK NEGATIF TAK TERDUGA: -는 바람에",
            "latex": "\\text{Akar Verba} + \\mathbf{-는 \\text{ } 바람에} \\implies \\text{Dampak Buruk / Kerugian di Luar Kendali}",
            "legend": "• Hanya digunakan bila klausa kedua menghasilkan akibat negatif/merugikan (늦었습니다, 다쳤습니다).<br>• Tidak boleh diikuti bentuk perintah atau ajakan."
        },
        "hints": {
            "concept": "Akhiran '-는 바람에' digunakan secara khusus ketika suatu kejadian mendadak atau di luar dugaan menjadi penyebab terjadinya akibat buruk/negatif pada klausa utama (seperti terlambat, jatuh sakit, atau celaka). Verba '멈추다' menjadi '멈추는 바람에'.",
            "execution": "Kereta mendadak berhenti -> '멈추는 바람에'."
        }
    },
    {
        "id": "kor-lat-h-04",
        "materi": "TATA BAHASA: KETIDAKTERHINDARKAN (-(으)ㄹ 수밖에 없다)",
        "topic": "Menyatakan Ketiadaan Pilihan Lain Selain Mengambil Keputusan Tersebut",
        "stem": "Keputusan direksi maskapai saat badai topan menerjang bandara:\n'기상 악화로 활주로 시야가 전혀 확보되지 않아서 안전을 위해 오늘 모든 항공편을 ( ... ).'\nBentuk ekspresi ketiadaan alternatif (-(으)ㄹ 수밖에 없다) dari verba '취소하다' (membatalkan) adalah...",
        "correct": "취소할 수밖에 없었습니다 (akar verba 취소하- tanpa batchim berpadu dengan -ㄹ 수밖에 없다).",
        "distractors": [
            "취소하지 않을 수 있었습니다 (menyatakan kemampuan untuk tidak membatalkan, bertentangan dengan bahaya badai).",
            "취소하기로 되어 있었습니다 (hanya menyatakan jadwal formal sebelumnya tanpa nuansa keterpaksaan darurat).",
            "취소할 뻔했습니다 (bermakna 'nyaris membatalkan namun ternyata jadi terbang', fatal bagi keselamatan).",
            "취소하도록 권고했습니다 (hanya menyatakan rekomendasi saran, bukan keputusan final mutlak maskapai)."
        ],
        "formula": {
            "title": "KETIADAAN ALTERNATIF LAIN: -(으)ㄹ 수밖에 없다 (NO CHOICE BUT TO)",
            "latex": "\\text{Akar Verba} + \\mathbf{-(으)ㄹ \\text{ } 수밖에 \\text{ } 없다}",
            "legend": "• Menunjukkan tidak ada jalan atau pilihan lain selain melakukan tindakan tersebut karena kondisi darurat.<br>• 취소하- $\\rightarrow$ 취소할 수밖에 없었습니다."
        },
        "hints": {
            "concept": "Pola kalimat '-(으)ㄹ 수밖에 없다' bermakna 'tidak ada pilihan lain selain...' atau 'terpaksa harus...'. Karena akar kata kerja '취소하다' berakhiran vokal, tambahkan '-ㄹ 수밖에 없다' -> '취소할 수밖에 없었습니다'.",
            "execution": "Tidak ada pilihan selain membatalkan = '취소할 수밖에 없었습니다'."
        }
    },
    {
        "id": "kor-lat-h-05",
        "materi": "TATA BAHASA: PASIF SPONTAN (피동사: -이/히/리/기-)",
        "topic": "Distingsi Verba Transitif Aktif '닫다' vs Verba Pasif Spontan '닫히다'",
        "stem": "Deskripsi peristiwa saat angin kencang meniup ruangan:\n'갑자기 거센 바람이 불어오더니 활짝 열려 있던 창문이 쾅 소리를 내며 저절로 ( ... ).'\nBentuk kata kerja pasif spontan (피동) yang TEPAT dari verba dasar '닫다' (menutup, ber-batchim ㄷ) adalah...",
        "correct": "닫혔습니다 (verba dasar 닫- disisipi imbuhan pasif 히 menjadi 닫히다, lalu terkonjugasi lampau 닫혔습니다).",
        "distractors": [
            "닫았습니다 (bentuk aktif transitif yang menuntut subjek manusia pelaku penutup pintu).",
            "닫이었습니다 (kesalahan afiks pasif yang keliru menggunakan imbuhan 이 pada konsonan ㄷ).",
            "닫추었습니다 (kesalahan menggunakan afiks kausatif 추 yang tidak ada dalam gramatika 닫다).",
            "닫히게 했습니다 (bentuk kausatif analitis yang berarti menyuruh jendela tertutup)."
        ],
        "formula": {
            "title": "BENTUK VERBA PASIF KOREA (피동사 SUFFIXES)",
            "latex": "\\text{닫다 (menutup)} + \\mathbf{-히-} \\implies \\mathbf{닫히다} \\text{ (tertutup)} \\quad (\\text{Kala Lampau: } \\mathbf{닫혔습니다})",
            "legend": "• Subjek '창문이' (jendela) tertutup sendiri oleh angin (저절로) $\\rightarrow$ bentuk pasif.<br>• Afiks pasif pada 닫다 adalah -히- (닫히다)."
        },
        "hints": {
            "concept": "Pembentukan kata kerja pasif (피동사) dalam bahasa Korea menggunakan salah satu dari empat infiks: -이-, -히-, -리-, -기-. Untuk verba '닫다' (menutup), infiks pasif yang tepat adalah '-히-' -> '닫히다' (tertutup). Karena kejadian telah selesai, bentuk lampaunya adalah '닫혔습니다'.",
            "execution": "닫다 + pasif lampau = '닫혔습니다'."
        }
    },
    {
        "id": "kor-lat-h-06",
        "materi": "TATA BAHASA: PERBANDINGAN SEJAJAR PROPORSI (-(으)ㄹ수록)",
        "topic": "Menyatakan Korelasi 'Semakin Sering Berlatih Bahasa Korea, Semakin Percaya Diri Berbicara'",
        "stem": "Prinsip pemerolehan kemahiran bahasa asing:\n'외국어는 매일 꾸준히 ( ... ) 말하기 실력이 눈에 띄게 향상되고 자신감이 생깁니다.'\nBentuk konjugasi proporsional (-(으)ㄹ수록) yang TEPAT dari kata kerja '연습하다' (berlatih) adalah...",
        "correct": "연습할수록 (akar kata kerja berakhiran vokal 하- berpadu dengan akhiran proporsi -ㄹ수록).",
        "distractors": [
            "연습하을수록 (kesalahan morfologis menyisipkan vokal 으 pada akar verba tanpa batchim).",
            "연습하느라면 (akhiran yang menyatakan 'apabila terus-menerus melakukan... maka biasanya terjadi...').",
            "연습하는 셈 치고 (ungkapan menganggap/mengikhlaskan seolah-olah telah berlatih).",
            "연습할 리가 없이 (ungkapan kemustahilan 'tidak mungkin berlatih', bertentangan dengan konteks)."
        ],
        "formula": {
            "title": "PROPORSI GRADUAL: -(으)ㄹ수록 (THE MORE ... THE MORE)",
            "latex": "\\text{Akar Vokal / ㄹ} + \\mathbf{-ㄹ수록} \\quad \\leftrightarrow \\quad \\text{Akar Konsonan} + \\mathbf{-을수록}",
            "legend": "• 연습하- (vokal) $\\rightarrow$ 연습할수록.<br>• Bermakna semakin intensitas kondisi A meningkat, semakin meningkat pula hasil B."
        },
        "hints": {
            "concept": "Pola kalimat '-(으)ㄹ수록' bermakna 'semakin... semakin...'. Jika akar kata berakhiran vokal, lekatkan '-ㄹ수록' (연습하다 -> 연습하- + ㄹ수록 = 연습할수록 = semakin sering berlatih, semakin meningkat kemampuannya).",
            "execution": "연습하다 + semakin = '연습할수록'."
        }
    },
    {
        "id": "kor-lat-h-07",
        "materi": "TATA BAHASA: ASPEK KETERLANJURAN SELESAI TUNTAS (-아/어 버리다)",
        "topic": "Menyatakan Kelegaan Selesainya Ujian Skripsi atau Rasa Sesal Benda Berharga yang Hilang",
        "stem": "Keluhan seorang turis yang kehilangan paspor di stasiun kereta:\n'지하철 선반 위에 가방을 두고 내렸는데, 그 안에 여권과 지갑이 들어 있어서 큰일( ... ). 결국 가방을 잃어( ... ).'\nPasangan bentuk aspek keterlanjuran tuntas (-아/어 버리다) yang TEPAT dari verba '잃다' (hilang/kehilangan) adalah...",
        "correct": "잃어버렸습니다 (verba 잃다 bervokal ㅣ berpadu dengan -어 버리다 untuk menyatakan rasa penyesalan mendalam atas kehilangan yang terlanjur terjadi).",
        "distractors": [
            "잃어 보았습니다 (bermakna sengaja mencoba merasakan kehilangan dompet, tidak masuk akal).",
            "잃어야 했습니다 (bermakna berkewajiban menghilangkan dompet dan paspor).",
            "잃는 척했습니다 (bermakna berpura-pura kehilangan paspor padahal tidak).",
            "잃을 뻔했습니다 (bermakna nyaris hilang namun akhirnya terselamatkan, kontradiktif dengan kepanikan 큰일)."
        ],
        "formula": {
            "title": "ASPEK KETERLANJURAN TUNTAS / PENYESALAN: -아/어 버리다",
            "latex": "\\text{Akar Verba} + \\mathbf{-아/어 \\text{ } 버리다} \\quad (\\text{잃-} + \\mathbf{-어 \\text{ } 버렸습니다})",
            "legend": "• Menunjukkan tindakan telah selesai secara tuntas dan tidak dapat diubah kembali.<br>• Sering memuat nuansa emosional penyesalan berat atau rasa lega plong."
        },
        "hints": {
            "concept": "Pola kalimat '-아/어 버리다' mengindikasikan bahwa suatu tindakan telah selesai secara mutlak/tuntas, yang kerap disertai rasa penyesalan mendalam karena musibah tak terbalikkan (atau kelegaan). Akar '잃다' menjadi '잃어버렸습니다' (terlanjur hilang sama sekali).",
            "execution": "잃다 + keterlanjuran tuntas = '잃어버렸습니다'."
        }
    },
    {
        "id": "kor-lat-h-08",
        "materi": "TATA BAHASA: TINDAKAN PURA-PURA (-(으)ㄴ/는 척하다)",
        "topic": "Menyatakan Kepura-puraan Tidak Mendengar Panggilan Teman",
        "stem": "Cerita seorang teman yang berpura-pura sibuk membaca buku:\n'민수는 복도에서 친구가 부르는 소리를 분명히 들었지만, 바쁜 일이 있어서 듣지 못한 것처럼 ( ... ) 계속 걸어갔습니다.'\nBentuk konjugasi pura-pura (-(으)ㄴ/는 척하다) yang TEPAT dari kata kerja '못 들은 척하다' adalah...",
        "correct": "못 들은 척하며 (akar verba 듣다 dalam konteks kala lampau berpadu dengan penanda kepura-puraan -(으)ㄴ 척하다).",
        "distractors": [
            "못 들을 척하며 (bentuk dugaan futuristik yang salah tata bahasa untuk tindakan kepura-puraan).",
            "못 듣는 셈 치며 (ungkapan menganggap/merelakan sesuatu yang salah fungsi semantik).",
            "못 들을 텐데 (ungkapan praduga kontras yang tidak menyatakan aksi pura-pura fisik).",
            "못 들어야 하며 (ungkapan kewajiban yang merusak alur narasi perilaku)."
        ],
        "formula": {
            "title": "KEPURA-PURAAN: -(으)ㄴ/는 척하다 (PRETEND TO)",
            "latex": "\\text{Kala Lampau Verba} + \\mathbf{-(으)ㄴ \\text{ } 척하다} \\quad | \\quad \\text{Kala Sekarang Verba} + \\mathbf{-는 \\text{ } 척하다}",
            "legend": "• Menunjukkan seseorang berpura-pura melakukan atau tidak melakukan sesuatu yang berbeda dari kenyataan.<br>• 못 들은 척하다: berpura-pura tidak mendengar."
        },
        "hints": {
            "concept": "Pola kalimat '-(으)ㄴ/는 척하다' berarti 'berpura-pura...'. Karena pura-pura tidak mendengar apa yang baru saja disuarakan (aspek lampau), bentuknya adalah '못 들은 척하며' (berpura-pura tidak mendengar lalu terus berjalan).",
            "execution": "Pura-pura tidak mendengar = '못 들은 척하며'."
        }
    },
    {
        "id": "kor-lat-h-09",
        "materi": "TATA BAHASA: PENGANDAIAN KONTRAFAKTUAL LAMPAU (-았/었더라면)",
        "topic": "Penyesalan Hipotetikal Terhadap Hasil Ujian Jika Dulu Belajar Lebih Rajin",
        "stem": "Renungan seorang siswa setelah pengumuman kelulusan:\n'학기 초에 시간을 헛되이 보내지 않고 조금만 더 열심히 ( ... ) 지금보다 훨씬 좋은 성적을 받았을 텐데 정말 후회가 됩니다.'\nBentuk pengandaian kontrafaktual lampau (-았/었더라면) dari verba '공부하다' adalah...",
        "correct": "공부했더라면 (akar verba 하- terkonjugasi lampau 했- + akhiran pengandaian kontrafaktual -더라면).",
        "distractors": [
            "공부하더라면 (kesalahan tidak menyertakan penanda kala lampau 었/았 pada struktur kontrafaktual).",
            "공부한다면 (pengandaian masa kini atau masa depan biasa yang tidak berorientasi pada fakta lampau yang mustahil diubah).",
            "공부했을수록 (kombinasi struktur proporsi yang salah tempat).",
            "공부할 텐데 (klausula pengantar yang tidak dapat berfungsi sebagai anteseden kondisional)."
        ],
        "formula": {
            "title": "KONTRAFAKTUAL LAMPAU: -았/었더라면 (IF HAD DONE...)",
            "latex": "\\text{Akar Verba} + \\mathbf{-았/었더라면} + \\dots + \\mathbf{-(으)ㄹ \\text{ } 텐데 / -(으)ㄹ \\text{ } 뻔했다}",
            "legend": "• Menyatakan pengandaian terhadap peristiwa lampau yang bertolak belakang dengan kenyataan (sebenarnya tidak rajin belajar).<br>• 공부하- $\\rightarrow$ 공부했더라면."
        },
        "hints": {
            "concept": "Pola kalimat '-았/었더라면' digunakan untuk menyatakan pengandaian kontrafaktual di masa lalu ('seandainya dulu saya...'). Klausa akhir biasanya diakhiri dengan '-(으)ㄹ 텐데' atau '-(으)ㄹ 뻔했다'. Verba '공부하다' menjadi '공부했더라면'.",
            "execution": "공부하다 + kontrafaktual lampau = '공부했더라면'."
        }
    },
    {
        "id": "kor-lat-h-10",
        "materi": "TATA BAHASA: WICARA TAK LANGSUNG AJAKAN (-자고 하다)",
        "topic": "Transformasi Usulan Rapat Menyelenggarakan Kampanye Daur Ulang Menjadi Kutipan Tidak Langsung",
        "stem": "Sekretaris OSIS menyampaikan usulan ketua panitia festival sekolah:\n'회장: \"이번 축제에서 일회용품 사용을 줄이고 재활용 분리배출 캠페인을 함께 시작합시다.\"\nBentuk kutipan wicara tak langsung (간접화법) yang TEPAT untuk menyampaikan kembali usulan ajakan di atas adalah...",
        "correct": "시작하자고 했습니다 (tuturan ajakan langsung -ㅂ시다 diubah menjadi akar kata kerja 시작하- + akhiran kutipan ajakan -자고 하다).",
        "distractors": [
            "시작하라고 했습니다 (bentuk kutipan perintah otoritatif yang tidak mencerminkan ajakan bersama -ㅂ시다).",
            "시작한다고 했습니다 (bentuk kutipan pernyataan deklaratif).",
            "시작하냐고 했습니다 (bentuk kutipan kalimat tanya interogatif).",
            "시작하지 말자고 했습니다 (bentuk larangan mengajak untuk tidak memulai kampanye)."
        ],
        "formula": {
            "title": "WICARA TAK LANGSUNG AJAKAN: -자고 하다 (SUGGEST DOING TOGETHER)",
            "latex": "\\text{Kalimat Ajakan Langsung (-ㅂ시다 / -자)} \\implies \\text{Akar Verba} + \\mathbf{-자고 \\text{ } 하다}",
            "legend": "• 시작합시다 $\\rightarrow$ 시작하자고 했습니다.<br>• Digunakan untuk melaporkan kembali ajakan melakukan sesuatu bersama."
        },
        "hints": {
            "concept": "Aturan wicara tak langsung untuk kalimat ajakan (propositif): kalimat langsung berakhiran '-(으)ㅂ시다' atau '-자' diubah menjadi: akar verba + '-자고 하다'. Kata kerja '시작하다' menjadi '시작하자고 했습니다'.",
            "execution": "Ajakan memulai bersama = '시작하자고 했습니다'."
        }
    },
    {
        "id": "kor-lat-h-11",
        "materi": "TATA BAHASA: ASPEK KAUSATIF (사동사: -이/히/리/기/우/추-)",
        "topic": "Distingsi Verba Transitif Biasa '입다' (Mengenakan) vs Verba Kausatif '입히다' (Memakaikan Pakaian pada Anak)",
        "stem": "Ibu merawat bayinya di pagi hari yang dingin:\n'어머니는 외출하기 전에 아기에게 따뜻한 털옷을 정성스럽게 ( ... ).'\nBentuk kata kerja kausatif (사동사) yang TEPAT untuk menyatakan 'memakaikan baju kepada orang lain' dari verba '입다' adalah...",
        "correct": "입혔습니다 (verba 입다 disisipi imbuhan kausatif 히 menjadi 입히다, lalu terkonjugasi waktu lampau 입혔습니다).",
        "distractors": [
            "입었습니다 (bentuk aktif biasa di mana ibu yang mengenakan pakaian bayi untuk dirinya sendiri).",
            "입게 되었습니다 (bentuk pasif situasi di mana pakaian tersebut terpakai dengan sendirinya).",
            "입으라고 했습니다 (bentuk menyuruh bayi berbicara/berpakaian sendiri).",
            "입지 않도록 했습니다 (bentuk pencegahan agar bayi tidak berpakaian tebal)."
        ],
        "formula": {
            "title": "VERBA KAUSATIF (사동사: MEMBUAT/MENYEBABKAN ORANG LAIN MELAKUKAN)",
            "latex": "\\text{입다 (mengenakan)} + \\mathbf{-히-} \\implies \\mathbf{입히다} \\text{ (memakaikan baju kepada orang lain)}",
            "legend": "• Subjek (어머니) membuat objek (아기에게) mengenakan pakaian (옷을).<br>• Imbuhan kausatif pada 입다 adalah -히- $\\rightarrow$ 입히다 (입혔습니다)."
        },
        "hints": {
            "concept": "Kata kerja kausatif (사동사) menunjukkan subjek membuat atau membantu pihak lain melakukan tindakan. Verba '입다' (mengenakan pakaian) memiliki bentuk kausatif '입히다' (memakaikan pakaian kepada pihak lain). Bentuk lampaunya adalah '입혔습니다'.",
            "execution": "입다 + kausatif lampau = '입혔습니다'."
        }
    },
    {
        "id": "kor-lat-h-12",
        "materi": "TATA BAHASA: PENGUNGKAPAN KEPUTUSAN / PERKIRAAN WAJAR (-(으)ㄹ 만하다)",
        "topic": "Menyatakan Suatu Tempat atau Karya Seni yang 'Layak / Patut Direkomendasikan'",
        "stem": "Ulasan novel sastra pemenang penghargaan internasional:\n'이 소설은 인간의 내면 심리를 섬세하게 묘사하여 문학을 사랑하는 독자라면 누구나 한 번쯤 꼭 ( ... ).'\nBentuk ungkapan kelayakan rekomendasi (-(으)ㄹ 만하다) yang TEPAT dari verba '읽다' (membaca) adalah...",
        "correct": "읽을 만합니다 (akar verba ber-batchim 읽- berpadu dengan penanda kelayakan -(으)ㄹ 만하다).",
        "distractors": [
            "읽을 리가 없습니다 (menyatakan 'tidak masuk akal untuk dibaca', sangat menghina karya seni).",
            "읽기 십상입니다 (akhiran probabilitas negatif 'pasti celaka/mudah tertimpa keburukan jika membaca').",
            "읽는 셈입니다 (menyatakan 'bisa dianggap sudah membaca', tidak cocok untuk rekomendasi).",
            "읽어야만 합니다 (terlalu memaksakan beban kewajiban hukum yang kaku)."
        ],
        "formula": {
            "title": "KELAYAKAN / REKOMENDASI: -(으)ㄹ 만하다 (WORTH DOING)",
            "latex": "\\text{Akar Verba} + \\mathbf{-(으)ㄹ \\text{ } 만하다} \\quad (\\text{읽-} + \\mathbf{-을 \\text{ } 만합니다})",
            "legend": "• Menunjukkan sesuatu layak, pantas, atau sangat bernilai untuk dicoba/dilakukan.<br>• 꼭 읽을 만합니다: Sangat layak untuk dibaca."
        },
        "hints": {
            "concept": "Pola kalimat '-(으)ㄹ 만하다' berarti 'layak/pantas untuk dilakukan' (worth doing). Akar kata kerja '읽다' (ber-batchim) menjadi '읽을 만합니다' (novel ini sangat layak dibaca oleh siapa saja pecinta sastra).",
            "execution": "읽다 + layak dibaca = '읽을 만합니다'."
        }
    },
    {
        "id": "kor-lat-h-13",
        "materi": "TATA BAHASA: PENGUNGKAPAN KERAGUAN / KEMUNGKINAN KECIL (-(으)ㄹ지도 모르다)",
        "topic": "Kekhawatiran Kemungkinan Pembatalan Penerbangan Akibat Kabut Tebal",
        "stem": "Pemberitahuan situasi cuaca ekstrem di bandara Incheon:\n'현재 짙은 안개와 강풍 때문에 일부 항공편의 출발이 지연되거나 아예 ( ... ). 전광판을 수시로 확인해 주시기 바랍니다.'\nBentuk ungkapan kemungkinan tak pasti (-(으)ㄹ지도 모르다) dari verba '취소되다' (dibatalkan) adalah...",
        "correct": "취소될지도 모릅니다 (akar verba 취소되- tanpa batchim berpadu dengan penanda probabilitas spekulatif -ㄹ지도 모르다).",
        "distractors": [
            "취소될 리가 없습니다 (menyatakan 'mustahil dibatalkan', membahayakan penumpang yang tidak waspada).",
            "취소되는 편입니다 (menyatakan kecenderungan umum biasa tanpa konteks ancaman mendadak).",
            "취소되지 않을 수 없습니다 (penegasan kepastian mutlak yang melampaui fakta perkiraan spekulatif).",
            "취소되는 척합니다 (bermakna berpura-pura dibatalkan, sangat absurd untuk sistem bandara internasional)."
        ],
        "formula": {
            "title": "KEMUNGKINAN TAK PASTI: -(으)ㄹ지도 모르다 (MIGHT / PERHAPS)",
            "latex": "\\text{Akar Verba} + \\mathbf{-(으)ㄹ지도 \\text{ } 모르다/모릅니다}",
            "legend": "• Menunjukkan keraguan atau kemungkinan sesuatu terjadi tanpa kepastian 100%.<br>• 취소되- $\\rightarrow$ 취소될지도 모릅니다 (Mungkin saja dibatalkan)."
        },
        "hints": {
            "concept": "Pola kalimat '-(으)ㄹ지도 모르다' digunakan untuk mengekspresikan kemungkinan atau dugaan yang belum pasti ('bisa jadi / mungkin saja...'). Verba '취소되다' menjadi '취소될지도 모릅니다' (mungkin saja dibatalkan).",
            "execution": "Mungkin saja dibatalkan = '취소될지도 모릅니다'."
        }
    },
    {
        "id": "kor-lat-h-14",
        "materi": "TATA BAHASA: WICARA TAK LANGSUNG PERTANYAAN (-냐고 하다)",
        "topic": "Transformasi Kalimat Tanya Langsung Wawancara Kerja Menjadi Tuturan Tidak Langsung",
        "stem": "Peserta wawancara menceritakan pertanyaan pewawancara:\n'면접관께서 물으셨습니다: \"지원자께서는 우리 회사의 해외 지사 근무가 가능합니까?\"\nBentuk kutipan wicara tak langsung (간접화법) yang TEPAT untuk menyampaikan kembali pertanyaan pewawancara adalah...",
        "correct": "가능하냐고 물으셨습니다 (adjektiva 가능하- dipadukan dengan akhiran kutipan kalimat tanya -냐고 하다).",
        "distractors": [
            "가능하다고 물으셨습니다 (kesalahan mencampur akhiran deklaratif -다고 dengan verba bertanya 묻다).",
            "가능하라고 물으셨습니다 (kesalahan mencampur akhiran perintah -라고 dengan verba bertanya).",
            "가능하자고 물으셨습니다 (kesalahan mencampur akhiran ajakan -자고 dengan verba bertanya).",
            "가능하시냐고 대답했습니다 (kesalahan subjek dan verba tindak tutur yang terbalik antara penanya dan penjawab)."
        ],
        "formula": {
            "title": "WICARA TAK LANGSUNG PERTANYAAN: -냐고 묻다/하다 (ASK IF)",
            "latex": "\\text{Akar Verba / Adjektiva} + \\mathbf{-냐고 \\text{ } 묻다/하다}",
            "legend": "• Melaporkan kembali pertanyaan interogatif orang lain.<br>• 가능합니까? $\\rightarrow$ 가능하냐고 물으셨습니다."
        },
        "hints": {
            "concept": "Aturan wicara tak langsung untuk kalimat tanya (interogatif): akar kata kerja atau kata sifat dilekati akhiran '-냐고 묻다' (atau '-냐고 하다'). Kata sifat '가능하다' menjadi '가능하냐고 물으셨습니다' (pewawancara bertanya apakah saya bisa bekerja di cabang luar negeri).",
            "execution": "Kutipan kalimat tanya = '가능하냐고 물으셨습니다'."
        }
    },
    {
        "id": "kor-lat-h-15",
        "materi": "TATA BAHASA: PENGAKUAN PARSIAL SEBELUM SANGAHAN (-기는 하지만)",
        "topic": "Mengakui Bahasa Korea Sulit Namun Sangat Menarik dan Menyenangkan",
        "stem": "Pendapat pembelajar bahasa asing:\n'한국어 문법은 다른 언어에 비해 다소 복잡하( ... ) 배울수록 깊은 매력이 있어서 아주 재미있습니다.'\nBentuk pengakuan parsial yang TEPAT dari kata sifat '복잡하다' (rumit) adalah...",
        "correct": "복잡하기는 하지만 (akar kata sifat 복잡하- + penanda konsesi pengakuan parsial -기는 하지만).",
        "distractors": [
            "복잡하기는커녕 (ungkapan penyangkalan ekstrem 'alih-alih rumit, malah...').",
            "복잡할 리가 없지만 (ungkapan kemustahilan yang kontradiktif dengan kesulitan tata bahasa nyata).",
            "복잡한 셈 치지만 (ungkapan pengandaian pengikhlasan yang tidak tepat konteks telaah linguistik).",
            "복잡하다시피 (ungkapan komparasi 'sebagaimana yang telah diketahui bersama')."
        ],
        "formula": {
            "title": "PENGAKUAN PARSIAL (KONSESI): -기는 하지만 (IT IS TRUE THAT ... BUT)",
            "latex": "\\text{Akar Kata} + \\mathbf{-기는 \\text{ } 하지만 / -기는 \\text{ } 한데}",
            "legend": "• Mengakui kebenaran klausa pertama, namun menegaskan pandangan positif yang lebih utama pada klausa kedua.<br>• Memang rumit, TETAPI sangat menarik."
        },
        "hints": {
            "concept": "Pola kalimat '-기는 하지만' digunakan untuk mengakui kebenaran suatu fakta pada bagian pertama ('memang benar bahwa...'), namun segera diikuti oleh penegasan sudut pandang lain yang lebih penting pada bagian kedua ('tetapi...'). Bentuknya: '복잡하기는 하지만'.",
            "execution": "복잡하다 + konsesi pengakuan = '복잡하기는 하지만'."
        }
    },
    {
        "id": "kor-lat-h-16",
        "materi": "TATA BAHASA: ASPEK KAUSATIF DENGAN AKHIRAN '-게 하다'",
        "topic": "Tindakan Guru Membuat Para Murid Berpikir Kritis Melalui Pertanyaan Mendalam",
        "stem": "Metode pembelajaran aktif guru sains di kelas:\n'선생님께서는 학생들에게 정답을 바로 알려주지 않고 스스로 깊이 ( ... ) 다양한 질문을 던지셨습니다.'\nBentuk kausatif sintaksis analitis (-게 하다) yang TEPAT dari verba '생각하다' (berpikir) adalah...",
        "correct": "생각하게 하려고 (akar verba 생각하- + kausatif analitis -게 하다 + akhiran tujuan -려고).",
        "distractors": [
            "생각당하게 하려고 (kesalahan mencampur bentuk pasif dan kausatif secara pleonastis).",
            "생각할 수밖에 없게 (menyatakan keterpaksaan tanpa unsur pedagogis tujuan aktif guru).",
            "생각하는 척하려고 (menyatakan berpura-pura berpikir, sangat tidak sesuai konteks pengajaran).",
            "생각하지 않도록 (bertolak belakang dengan filosofi memicu daya kritis siswa)."
        ],
        "formula": {
            "title": "KAUSATIF SINTAKSIS: -게 하다 (MAKE / CAUSE SOMEONE TO DO)",
            "latex": "\\text{Akar Verba} + \\mathbf{-게 \\text{ } 하다} \\quad (\\text{생각하-} + \\mathbf{-게 \\text{ } 하려고})",
            "legend": "• Menunjukkan subjek menyebabkan atau memberi ruang bagi objek untuk melakukan tindakan.<br>• Membuat para murid berpikir sendiri."
        },
        "hints": {
            "concept": "Konstruksi kausatif analitis universal dalam bahasa Korea dibentuk dengan: akar kata kerja + '-게 하다' (membuat seseorang melakukan sesuatu). Bila dipadukan dengan tujuan '-(으)려고', bentuknya menjadi '생각하게 하려고' (agar membuat para murid berpikir sendiri).",
            "execution": "생각하다 + kausatif tujuan = '생각하게 하려고'."
        }
    },
    {
        "id": "kor-lat-h-17",
        "materi": "TATA BAHASA: KEPUTUSAN KESEPAKATAN FORMAL / KETENTUAN HUKUM (-기로 되어 있다)",
        "topic": "Menyatakan Aturan Resmi Gedung Pertemuan Mengenai Larangan Merokok",
        "stem": "Penjelasan petugas keamanan mengenai regulasi gedung publik:\n'관련 법령 및 본 건물 관리 규정에 따라 건물 전체 구역이 금연구역으로 ( ... ). 흡연 적발 시 과태료가 부과됩니다.'\nBentuk pengungkapan aturan ketentuan hukum (-기로 되어 있다) yang TEPAT dari verba '지정되다' (ditetapkan) adalah...",
        "correct": "지정되어 있습니다 (verba pasif 지정되다 berpadu dengan penanda status ketetapan hukum bertahan -어 있다).",
        "distractors": [
            "지정될 뻔했습니다 (menyatakan 'nyaris ditetapkan namun gagal', bertentangan dengan denda tilang nyata).",
            "지정되는 셈 치고 (ungkapan menganggap seolah-olah, merusak otoritas kepastian hukum).",
            "지정할 리가 없습니다 (menyatakan kemustahilan gedung tersebut menjadi area bebas rokok).",
            "지정하지 않기로 했습니다 (menyatakan pembatalan kesepakatan area bebas rokok)."
        ],
        "formula": {
            "title": "STATUS KETETAPAN ATURAN HUKUM: -기로 되어 있다 / -어 있다",
            "latex": "\\text{Regulasi Resmi / Status Hukum} \\implies \\mathbf{-기로 \\text{ } 되어 \\text{ } 있다 / -어 \\text{ } 있다}",
            "legend": "• Menunjukkan status aturan yang sudah disahkan dan berlaku secara mengikat bagi publik.<br>• 지정되어 있습니다."
        },
        "hints": {
            "concept": "Untuk menyatakan suatu aturan resmi atau ketetapan hukum yang berlaku dan bertahan statusnya dalam ruang publik, digunakan verba pasif yang dipadukan dengan status '-어 있다' (지정되다 -> 지정되어 있습니다 = telah resmi ditetapkan sebagai area dilarang merokok).",
            "execution": "지정되다 + status aturan = '지정되어 있습니다'."
        }
    },
    {
        "id": "kor-lat-h-18",
        "materi": "ANALISIS WACANA: FENOMENA MASYARAKAT PENUAAN (고령화 사회)",
        "topic": "Penarikan Kesimpulan Berdasarkan Data Penurunan Angka Kelahiran dan Peningkatan Populasi Lansia",
        "stem": "Bacalah kutipan analisis demografi Korea kontemporer berikut:\n'통계청 발표에 따르면, 대한민국은 유례없이 급격한 저출산 현상과 기대수명 연장으로 인해 전체 인구 중 65세 이상 고령층의 비율이 20%를 넘어서는 '초고령 사회' 진입을 목전에 두고 있다. 이에 따라 생산연령인구의 감소로 인한 잠재성장률 둔화와 노년층 복지·의료 재정 부담 증가가 국가적 핵심 당면 과제로 대두되고 있다.'\nBerdasarkan wacana di atas, kesimpulan analitis yang PALING TEPAT mengenai implikasi sosio-ekonomi fenomena tersebut adalah...",
        "correct": "Penurunan populasi usia produktif beriringan dengan ledakan jumlah lansia menuntut restrukturisasi kebijakan ketenagakerjaan dan jaminan sosial nasional.",
        "distractors": [
            "Peningkatan angka harapan hidup secara otomatis meningkatkan pendapatan per kapita tanpa memerlukan intervensi anggaran negara.",
            "Tingkat kelahiran anak di Korea telah kembali melesat naik berkat efektivitas subsidi perumahan instan.",
            "Beban anggaran belanja jaminan kesehatan publik diproyeksikan mengalami penurunan tajam dalam dasawarsa mendatang.",
            "Pemerintah berencana meniadakan batas usia pensiun untuk menolak status negara berpopulasi lanjut usia."
        ],
        "formula": {
            "title": "ANALISIS WACANA SOSIO-DEMOGRAFI: 고령화 사회 (AGING SOCIETY)",
            "latex": "\\text{저출산 (Penurunan Kelahiran)} + \\text{고령화 (Penuaan)} \\implies \\text{생산가능인구 감소} + \\text{복지재정 압박}",
            "legend": "• 초고령 사회: Proporsi usia 65+ melampaui 20% total populasi.<br>• Menuntut reformasi komprehensif sistem jaminan sosial dan ketenagakerjaan."
        },
        "hints": {
            "concept": "Teks memaparkan bahwa fenomena penurunan angka kelahiran (저출산) dan perpanjangan usia harapan hidup menyebabkan Korea memasuki masyarakat super-lansia (초고령 사회). Akibatnya: jumlah usia kerja produktif berkurang (생산연령인구 감소) dan beban pembiayaan jaminan kesehatan/sosial melonjak (의료 재정 부담 증가).",
            "execution": "Kesimpulan tepat: Penurunan usia produktif dan ledakan lansia menuntut restrukturisasi jaminan sosial."
        }
    },
    {
        "id": "kor-lat-h-19",
        "materi": "ANALISIS WACANA: SISTEM PENGELOLAAN SAMPAH MANDIRI (분리배출)",
        "topic": "Prinsip 4 Langkah Baku Pemilahan Sampah Daur Ulang Korea (비우고, 헹구고, 분리하고, 섞지 않는다)",
        "stem": "Bacalah panduan kampanye ekologi lingkungan kota Seoul:\n'올바른 재활용품 분리배출은 자원 순환 사회를 만드는 첫걸음입니다. 환경부가 제시하는 4대 기본 원칙은 다음과 같습니다. 첫째, 용기 안의 내용물을 깨끗이 '비운다'. 둘째, 이물질이 묻은 용기는 물로 '헹군다'. 셋째, 페트병의 비닐 라벨과 뚜껑 등 재질이 다른 부분은 완전히 '분리한다'. 넷째, 재활용이 가능한 품목과 일반 쓰레기를 절대로 '섞지 않는다'.' \nBerdasarkan petunjuk di atas, tindakan warga yang MENYALAHI aturan baku pemilahan sampah daur ulang adalah...",
        "correct": "Membuang botol plastik air mineral transparan ke tempat sampah daur ulang tanpa melepas label merek dan tutup plastiknya.",
        "distractors": [
            "Membilas kaleng minuman bekas jus dengan air bersih sebelum mengumpulkannya di tempat pembuangan.",
            "Mengosongkan seluruh sisa makanan dari dalam kotak karton susu sebelum melipatnya rapi.",
            "Memisahkan kantong plastik kresek hitam dan memasukkannya ke dalam wadah khusus plastik.",
            "Membuang sisa tisu basah kotor langsung ke kantong plastik sampah umum berbayar (종량제 봉투)."
        ],
        "formula": {
            "title": "4 PRINSIP BAKU PEMILAHAN SAMPAH KOREA (분리배출 4대 원칙)",
            "latex": "\\mathbf{비운다} \\text{ (Kosongkan)} \\rightarrow \\mathbf{헹군다} \\text{ (Bilas)} \\rightarrow \\mathbf{분리한다} \\text{ (Pisahkan Bahan Berbeda)} \\rightarrow \\mathbf{섞지 않는다} \\text{ (Jangan Campur)}",
            "legend": "• Botol PET transparan (투명 페트병) WAJIB dilepas label vinilnya sebelum dibuang.<br>• Melanggar aturan pemisahan material berbeda (분리한다)."
        },
        "hints": {
            "concept": "Prinsip ketiga menyatakan: '재질이 다른 부분은 완전히 분리한다' (bagian yang berbeda material bahan, seperti label vinil dan tutup botol plastik, harus dipisahkan secara sempurna). Maka tindakan membuang botol PET tanpa melepas label vinil adalah pelanggaran aturan.",
            "execution": "Tindakan menyalahi: Membuang botol plastik tanpa melepas label merek dan tutupnya."
        }
    },
    {
        "id": "kor-lat-h-20",
        "materi": "ANALISIS WACANA: SEJARAH PENEMUAN HANGEUL (훈민정음 & 세종대왕)",
        "topic": "Filosofi Humanistis Penciptaan Aksara Hangeul oleh Raja Sejong yang Agung Tahun 1443",
        "stem": "Bacalah teks sejarah kebudayaan berikut:\n'1443년 세종대왕은 백성들이 한자의 어려움으로 인해 자신의 생각과 억울함을 글로 표현하지 못하는 현실을 안타깝게 여겨, 독창적이고 과학적인 문자 체계인 '훈민정음(백성을 가르치는 바른 소리)'을 창제하였다. 훈민정음의 자음은 인간의 발음 기관(혀, 입술, 이, 목구멍)의 모양을 본떠 상형의 원리로 만들어졌으며, 모음은 동양 철학의 삼재인 천(하늘 ·), 지(땅 ㅡ), 인(사람 ㅣ)을 바탕으로 구성되었다.'\nNilai filosofis utama yang melandasi penciptaan aksara Hangeul berdasarkan teks tersebut adalah...",
        "correct": "Semangat humanisme kerakyatan (애민정신) untuk memberdayakan rakyat jelata agar mampu berliterasi dan menyuarakan aspirasinya.",
        "distractors": [
            "Keinginan memperluas kekuasaan militer dinasti Joseon ke seluruh daratan benua Asia.",
            "Tuntutan para bangsawan istana untuk menciptakan sandi rahasia peperangan antar-kerajaan.",
            "Upaya menghapus seluruh kosakata serapan bahasa Mandarin demi isolasi peradaban.",
            "Kebutuhan menggantikan aksara latin yang saat itu dominan di kalangan pedagang tradisional."
        ],
        "formula": {
            "title": "FILOSOFI PENCIPTAAN HANGEUL (훈민정음 창제 정신)",
            "latex": "\\text{세종대왕 (Raja Sejong)} \\implies \\mathbf{애민정신 (Cinta Rakyat)} + \\mathbf{자주정신 (Kemandirian)} + \\mathbf{실용정신 (Kepraktisan)}",
            "legend": "• Latar belakang: Rakyat jelata kesulitan mempelajari Hanja Tiongkok yang rumit.<br>• Tujuan: Memberikan sarana ekspresi literasi yang mudah dipelajari bagi seluruh rakyat jelata."
        },
        "hints": {
            "concept": "Teks menegaskan bahwa Raja Sejong prihatin karena rakyat jelata tidak dapat mengekspresikan pikiran dan ketidakadilan akibat sulitnya aksara Hanja (자신의 생각과 억울함을 글로 표현하지 못하는 현실을 안타깝게 여겨). Nilai utamanya adalah semangat cinta rakyat jelata (애민정신/humanisme).",
            "execution": "Nilai utama: Semangat humanisme kerakyatan untuk memberdayakan literasi rakyat jelata."
        }
    },
    {
        "id": "kor-lat-h-21",
        "materi": "ANALISIS WACANA: TRADISI HARI RAYA KOREA (추석 VS 설날)",
        "topic": "Distingsi Makna Filosofis dan Kuliner Khas Seollal (떡국) vs Chuseok (송편)",
        "stem": "Bacalah wacana komparasi tradisi budaya perayaan Korea:\n'한국의 2대 명절인 설날과 추석은 고유한 의미와 상징적 절식(명절 음식)을 지닌다. 음력 1월 1일인 설날에는 새해의 순결과 장수를 기원하며 하얗고 둥근 가래떡을 썬 '떡국'을 먹고 웃어른께 '세배'를 올린다. 반면 음력 8월 15일인 추석은 한 해의 농사를 무사히 마치고 풍성한 수확에 감사하는 한가위 명절로서, 햅쌀과 햇곡식으로 반달 모양의 '송편'을 빚어 조상께 감사의 차례를 올린다.'\nBerdasarkan wacana di atas, pernyataan komparasi yang BENAR adalah...",
        "correct": "Tteokguk pada hari Seollal melambangkan harapan kesucian dan umur panjang di tahun baru, sedangkan Songpyeon pada hari Chuseok melambangkan rasa syukur atas panen raya.",
        "distractors": [
            "Songpyeon disajikan khusus pada hari Seollal untuk menandai pertambahan usia seseorang genap satu tahun.",
            "Tradisi sungkem Sebae dilakukan saat Chuseok untuk memohon hasil panen yang melimpah kepada para leluhur.",
            "Tteokguk dibuat dari beras ketan baru hasil panen musim gugur yang dibentuk menyerupai bulan sabit.",
            "Kedua hari raya tersebut dirayakan bersamaan pada malam bulan purnama musim semi penanggalan surya."
        ],
        "formula": {
            "title": "KOMPARASI 2 HARI RAYA BESAR KOREA (명절)",
            "latex": "\\text{설날 (Tahun Baru Imlek)} \\rightarrow \\mathbf{떡국 (Tteokguk) / 세배 (Sebae)} \\quad | \\quad \\text{추석 (Panen Raya)} \\rightarrow \\mathbf{송편 (Songpyeon) / 차례 (Charye)}",
            "legend": "• Seollal (1 Januari Imlek): Tteokguk melambangkan kemurnian/panjang umur.<br>• Chuseok (15 Agustus Imlek): Songpyeon melambangkan syukur atas panen raya yang berlimpah."
        },
        "hints": {
            "concept": "Teks memaparkan dengan tegas: 1) Seollal (Tahun Baru Imlek) menyajikan Tteokguk (떡국) sebagai simbol kemurnian dan umur panjang di tahun baru. 2) Chuseok (Hari Panen Raya) menyajikan Songpyeon (송편) berbentuk bulan sabit dari hasil panen baru sebagai wujud syukur atas hasil panen raya.",
            "execution": "Pernyataan benar: Tteokguk untuk kesucian/umur panjang baru; Songpyeon untuk syukur panen raya."
        }
    },
    {
        "id": "kor-lat-h-22",
        "materi": "ANALISIS WACANA: KEBERLANJUTAN GELOMBANG HALLYU (한류)",
        "topic": "Transformasi Hallyu dari Konsumsi Budaya Populer Sesaat Menuju Pertukaran Nilai Kultural Dua Arah",
        "stem": "Bacalah artikel kajian sosiologi budaya global:\n'초기 케이팝과 한국 드라마 중심의 한류가 일방적인 문화 상품 소비에 머물렀다면, 오늘날의 한류는 한국어 학습, K-푸드, 문학, 전통 예술 등으로 저변을 확장하며 다층적인 문화 교류의 양상을 띠고 있다. 전문가들은 한류가 일시적 유행에 그치지 않고 지속 가능한 문화적 영향력을 유지하기 위해서는 타문화에 대한 존중과 상호 소통을 바탕으로 하는 '쌍방향 문화 교류'로 발전해야 한다고 제언한다.'\nMenurut kutipan di atas, kunci utama bagi kelangsungan jangka panjang fenomena Hallyu adalah...",
        "correct": "Mengembangkan dialog dan interaksi pertukaran budaya dua arah yang menghormati keberagaman nilai budaya lokal di setiap negara mitra.",
        "distractors": [
            "Memusatkan seluruh produksi konten hiburan hanya pada grup musik idola pria berbahasa Korea murni.",
            "Membatasi akses penyiaran serial drama televisi Korea agar harga hak cipta di pasar luar negeri meningkat tajam.",
            "Menuntut seluruh penggemar global untuk meniru tradisi berpakaian masyarakat Joseon kuno secara mutlak.",
            "Menghilangkan unsur bahasa Korea dalam lirik lagu pop agar seluruhnya digantikan oleh kosakata bahasa Inggris."
        ],
        "formula": {
            "title": "KEBERLANJUTAN HALLYU: 쌍방향 문화 교류 (TWO-WAY CULTURAL EXCHANGE)",
            "latex": "\\text{Konsumsi Sepihak (일방적 소비)} \\implies \\mathbf{Pertukaran \\text{ } Dua \\text{ } Arah \\text{ (쌍방향 \\text{ } 교류)}} + \\mathbf{Saling \\text{ } Menghormati}",
            "legend": "• Menghindari imperialisme budaya sepihak.<br>• Menjadikan Hallyu jembatan pemahaman lintas bangsa yang inklusif."
        },
        "hints": {
            "concept": "Kunci keberlanjutan Hallyu yang ditegaskan dalam kalimat terakhir teks: '지속 가능한 문화적 영향력을 유지하기 위해서는 타문화에 대한 존중과 상호 소통을 바탕으로 하는 쌍방향 문화 교류로 발전해야 한다' (harus berkembang menjadi pertukaran budaya dua arah yang didasarkan pada rasa hormat terhadap budaya lain dan komunikasi timbal balik).",
            "execution": "Kunci utama: Pertukaran budaya dua arah dengan saling menghormati budaya mitra."
        }
    },
    {
        "id": "kor-lat-h-23",
        "materi": "TATA BAHASA: PENGUNGKAPAN KEPUTUSAN TERPAKSA (-(으)ㄹ 지경이다)",
        "topic": "Menyatakan Keadaan Sangat Lelah yang Nyaris Pingsan Karena Bekerja Lembur",
        "stem": "Ungkapan seorang pekerja setelah lembur menyelesaikan laporan tahunan perusahaan:\n'일주일 내내 밤샘 야근을 했더니 몸이 천근만근 무겁고 당장 길바닥에 ( ... ). 오늘 밤에는 아무 생각 없이 푹 자야겠어요.'\nBentuk pengungkapan ambang batas ekstrem (-(으)ㄹ 지경이다) yang TEPAT dari verba '쓰러지다' (pingsan/jatuh roboh) adalah...",
        "correct": "쓰러질 지경입니다 (akar verba 쓰러지- tanpa batchim berpadu dengan penanda kondisi ekstrem -ㄹ 지경이다).",
        "distractors": [
            "쓰러질 턱이 없습니다 (menyatakan kemustahilan roboh, bertentangan dengan rasa lelah luar biasa).",
            "쓰러지는 척했습니다 (bermakna sengaja berpura-pura jatuh roboh).",
            "쓰러지지 않을 리가 없습니다 (makna ganda berbelit-belit yang canggung).",
            "쓰러질 리 만무합니다 (ungkapan kepastian tidak akan roboh)."
        ],
        "formula": {
            "title": "AMBANG BATAS EKSTREM: -(으)ㄹ 지경이다 (ON THE VERGE OF)",
            "latex": "\\text{Akar Verba} + \\mathbf{-(으)ㄹ \\text{ } 지경이다/지경입니다}",
            "legend": "• Menunjukkan kondisi fisik atau mental yang berada di ambang batas sangat ekstrem (nyaris pingsan/roboh).<br>• 쓰러지- $\\rightarrow$ 쓰러질 지경입니다."
        },
        "hints": {
            "concept": "Pola kalimat '-(으)ㄹ 지경이다' bermakna 'sampai pada batas ambang nyaris...' untuk melukiskan kondisi ekstrem yang dialami pelaku. Verba '쓰러지다' menjadi '쓰러질 지경입니다' (saking lelahnya, saya sampai di ambang batas nyaris roboh pingsan di jalan).",
            "execution": "쓰러지다 + ambang batas ekstrem = '쓰러질 지경입니다'."
        }
    },
    {
        "id": "kor-lat-h-24",
        "materi": "TATA BAHASA: PENGUNGKAPAN AKIBAT LOGIS (-느니 차라리)",
        "topic": "Memilih Berjalan Kaki Menghirup Udara Segar Daripada Terjebak Macet di Dalam Taksi",
        "stem": "Keputusan rasional pejalan kaki saat jalan raya macet total:\n'출퇴근 시간에 꼼짝도 않는 도로 위 택시 안에 ( ... ) 맑은 공기를 마시며 지하철역까지 걸어가는 편이 훨씬 낫겠습니다.'\nBentuk komparasi preferensi ekstrem (-느니 차라리) yang TEPAT dari verba '갇혀 있다' (terjebak terkurung) adalah...",
        "correct": "갇혀 있느니 (akar verba 있- berpadu dengan penanda preferensi perbandingan negatif -느니).",
        "distractors": [
            "갇혀 있더라도 (hanya menyatakan konsesi 'meskipun terjebak', tidak memuat nuansa pemilihan opsi yang lebih disukai).",
            "갇혀 있으면서 (menyatakan simultanitas yang merusak pilihan jalan kaki).",
            "갇혀 있을수록 (menyatakan proporsi yang tidak tepat secara sintaksis).",
            "갇혀 있자마자 (menyatakan kesegeraan waktu yang salah konteks perbandingan)."
        ],
        "formula": {
            "title": "PREFERENSI EKSTREM: A-느니 차라리 B (RATHER B THAN A)",
            "latex": "\\text{Opsi Buruk A} + \\mathbf{-느니 (차라리)} + \\text{Opsi B yang Lebih Masuk Akal} + \\mathbf{낫다/좋다}",
            "legend": "• Menolak mentah-mentah opsi A yang sia-sia demi mengambil opsi B.<br>• 갇혀 있느니 걸어가는 편이 낫다: Daripada terkurung macet, lebih baik jalan kaki."
        },
        "hints": {
            "concept": "Pola kalimat '-느니 (차라리)' digunakan ketika membandingkan dua opsi yang tidak ideal, di mana pembicara menegaskan: 'daripada harus mengalami A, jauh lebih baik melakukan B'. Verba '갇혀 있다' menjadi '갇혀 있느니'.",
            "execution": "갇혀 있다 + preferensi komparatif = '갇혀 있느니'."
        }
    },
    {
        "id": "kor-lat-h-25",
        "materi": "ANALISIS WACANA: ARSITEKTUR TRADISIONAL HANOK (한옥 & 온돌)",
        "topic": "Prinsip Harmoni Alam dan Sistem Pemanas Bawah Lantai 'Ondol' serta Ventilasi 'Maru'",
        "stem": "Bacalah teks arsitektur tradisional Korea:\n'전통 가옥인 '한옥'은 자연과의 조화를 중시하는 조상들의 지혜가 담긴 건축물이다. 한옥의 가장 독창적인 특징은 혹독한 추위의 겨울과 고온다습한 여름이라는 상반된 기후 조건을 동시에 극복했다는 점이다. 방바닥 밑으로 구들장을 놓고 아궁이의 열기를 통과시켜 바닥을 따뜻하게 덥히는 '온돌'은 겨울을 나기 위한 난방 장치이며, 지면에서 띄워 바람이 사방으로 통하도록 만든 나무 복도인 '마루'는 여름의 무더위를 식히는 냉방 구조이다.'\nBerdasarkan teks di atas, keunggulan arsitektural utama rumah tradisional Hanok adalah...",
        "correct": "Memadukan sistem pemanas bawah lantai (Ondol) untuk musim dingin dan koridor berventilasi alami (Maru) untuk musim panas secara harmonis.",
        "distractors": [
            "Mengandalkan material beton kedap air untuk mencegah pertukaran udara alami dengan lingkungan luar.",
            "Menutup seluruh celah ventilasi jendela agar kehangatan tungku dapur terjaga sepanjang tahun.",
            "Menggantikan pemakaian kayu alami dengan dinding batu bata modern demi efisiensi biaya perawatan.",
            "Memusatkan seluruh aktivitas penghuni hanya di satu ruangan sempit tanpa koridor penghubung."
        ],
        "formula": {
            "title": "ARSITEKTUR HANOK: INTEGRASI ONDOL & MARU (자연과의 조화)",
            "latex": "\\mathbf{온돌 (Ondol)} \\text{ [Musim Dingin: Pemanas Bawah Lantai]} \\quad + \\quad \\mathbf{마루 (Maru)} \\text{ [Musim Panas: Ventilasi Terbuka]}",
            "legend": "• Mengatasi dua ekstrem musim dingin dan musim panas dalam satu kesatuan rumah.<br>• Bukti nyata kearifan lokal beradaptasi selaras dengan alam (자연과의 조화)."
        },
        "hints": {
            "concept": "Teks memaparkan bahwa keunikan utama rumah tradisional Hanok adalah kemampuannya mengatasi dua musim bertolak belakang: pemanas lantai 'Ondol' (온돌) untuk musim dingin, dan koridor kayu berventilasi udara sejuk 'Maru' (마루) untuk musim panas.",
            "execution": "Keunggulan utama: Perpaduan Ondol untuk musim dingin dan Maru untuk musim panas."
        }
    }
]
