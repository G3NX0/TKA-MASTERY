# -*- coding: utf-8 -*-
"""
BAHASA KOREA - PAKET SOAL SIMULASI CBT HOTS (SIMULASI) - 35 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / TOPIK I-II (CEFR A2-B2)
Distribusi:
- 25 Butir: Pilihan Ganda Autentik HOTS (kor-sim-01 s.d. kor-sim-25)
- 5 Butir: Pilihan Ganda Kompleks / Multi-Select (kor-sim-26 s.d. kor-sim-30)
- 5 Butir: Matriks Benar / Salah / Evaluasi Kritis (kor-sim-31 s.d. kor-sim-35)
"""

BAHASA_KOREA_SIMULASI_ITEMS = [
    # -------------------------------------------------------------------------
    # 25 BUTIR PILIHAN GANDA (MCQ) HOTS (kor-sim-01 s.d. kor-sim-25)
    # -------------------------------------------------------------------------
    {
        "id": "kor-sim-01",
        "materi": "TATA BAHASA: PENGGUNAAN WICARA TAK LANGSUNG PADA LAPORAN BERITA",
        "topic": "Pelaporan Temuan Ilmiah Menggunakan Bentuk Kutipan Tak Langsung Deklaratif (-ㄴ/는다고 밝히다)",
        "stem": "Dalam siaran warta berita sains dan teknologi Korea:\n'연구진은 이번에 개발된 차세대 배터리가 기존 리튬 배터리보다 에너지 밀도가 30% 이상 ( ... ) 공식 발표했습니다.'\nBentuk konjugasi kutipan tak langsung objektif yang TEPAT dari kata sifat '높다' (tinggi) adalah...",
        "correct": "높다고 (kata sifat 높다 berakar konsonan berpasangan langsung dengan akhiran kutipan deklaratif -다고).",
        "distractors": [
            "높는다고 (kesalahan memperlakukan kata sifat seperti kata kerja yang disisipi penanda aspek 는).",
            "높냐고 (bentuk kutipan kalimat tanya yang tidak cocok untuk laporan rilis pers ilmiah).",
            "높으라고 (bentuk kutipan kalimat instruksi perintah).",
            "높자고 (bentuk kutipan kalimat ajakan bersama)."
        ]
    },
    {
        "id": "kor-sim-02",
        "materi": "TATA BAHASA: KEPURA-PURAAN DENGAN BENTUK KALA LAMPAU (-(으)ㄴ 척하다)",
        "topic": "Menyatakan Seseorang Berpura-pura Sudah Mengetahui Berita Rahasia",
        "stem": "Cerita seorang rekan kerja dalam suasana percakapan santai:\n'영수는 그 소식을 오늘 아침에 처음 들었으면서도 다른 사람들 앞에서는 이미 다 알고 ( ... ) 고개를 끄덕였습니다.'\nBentuk konjugasi kepura-puraan lampau yang TEPAT dari verba '알다' (tahu/mengetahui, ber-batchim ㄹ) adalah...",
        "correct": "있었던 척하며 (aspek telah mengetahui di masa lampau berpadu dengan penanda kepura-puraan -척하다).",
        "distractors": [
            "있을 척하며 (bentuk prospektif futuristik yang salah tata bahasa untuk fakta masa lalu).",
            "있는 셈 치며 (ungkapan menganggap/merelakan sesuatu yang salah makna kontekstual).",
            "있을 텐데 (ungkapan praduga kontras pengantar tuturan).",
            "있어야 하며 (ungkapan keharusan mutlak yang merusak alur narasi kepura-puraan)."
        ]
    },
    {
        "id": "kor-sim-03",
        "materi": "TATA BAHASA: ASPEK KAUSATIF DENGAN INFIKS '-이/히/리/기-'",
        "topic": "Distingsi Verba Transitif Biasa '읽다' (Membaca) vs Verba Kausatif '읽히다' (Membacakan Dongeng pada Anak)",
        "stem": "Aktivitas ayah menjelang tidur malam anak tercinta:\n'아버지는 잠자리에 든 아이에게 머리를 쓰다듬으며 재미있는 동화책을 나지막한 목소리로 ( ... ).'\nBentuk kata kerja kausatif (사동사) yang TEPAT dari verba dasar '읽다' (membaca) adalah...",
        "correct": "읽혔습니다 (verba dasar 읽다 disisipi imbuhan kausatif 히 menjadi 읽히다, lalu terkonjugasi lampau 읽혔습니다).",
        "distractors": [
            "읽었습니다 (bentuk aktif transitif di mana ayah membaca sendiri untuk keperluan pribadinya).",
            "읽게 되었습니다 (bentuk pasif situasi di mana dongeng terbaca dengan sendirinya).",
            "읽으라고 했습니다 (bentuk menyuruh anak kecil membaca sendiri tanpa pendampingan).",
            "읽지 않도록 했습니다 (bentuk pencegahan agar anak tidak membaca buku)."
        ]
    },
    {
        "id": "kor-sim-04",
        "materi": "TATA BAHASA: PENGUNGKAPAN KORELASI SEJAJAR (-(으)ㄹ수록)",
        "topic": "Korelasi Tingkat Kerumitan Desain Algoritma Komputasi dengan Beban Memori Sistem",
        "stem": "Prinsip optimasi rekayasa perangkat lunak:\n'알고리즘의 구조가 지나치게 ( ... ) 시스템의 메모리 점유율이 높아지고 예기치 못한 오류가 발생하기 쉽습니다.'\nBentuk konjugasi proporsional (-(으)ㄹ수록) yang TEPAT dari kata sifat '복잡하다' (rumit) adalah...",
        "correct": "복잡할수록 (akar kata sifat berakhiran vokal 하- berpadu dengan akhiran perbandingan proporsional -ㄹ수록).",
        "distractors": [
            "복잡하을수록 (kesalahan morfologis menyisipkan vokal 으 pada akar tanpa batchim).",
            "복잡하더라도 (hanya menyatakan konsesi 'meskipun rumit', tanpa makna eskalasi dampak berbanding lurus).",
            "복잡한 셈 치고 (ungkapan mengikhlaskan/menganggap seolah-olah yang keliru nalar teknis).",
            "복잡할 리가 없이 (ungkapan kemustahilan 'tidak mungkin rumit', bertolak belakang dengan premis)."
        ]
    },
    {
        "id": "kor-sim-05",
        "materi": "TATA BAHASA: PENGUNGKAPAN PENYESALAN MASA LALU (-(으)ㄹ 걸 그랬다)",
        "topic": "Penyesalan Karena Tidak Melakukan Pemesanan Tiket Kereta Mudik Chuseok Lebih Awal",
        "stem": "Keluhan seorang perantau saat kehabisan tiket pulang kampung jelang hari raya Chuseok:\n'연휴 기차표 예매가 오늘 시작되는 줄 알았더라면 아침 7시 정각에 미리 사이트에 ( ... ). 결국 표가 다 매진되었어요.'\nBentuk penyesalan atas tindakan yang tidak dilakukan (-(으)ㄹ 걸 그랬다) dari verba '접속하다' (mengakses/login) adalah...",
        "correct": "접속할 걸 그랬어요 (akar verba 접속하- berpadu dengan penanda penyesalan kontrafaktual -ㄹ 걸 그랬다).",
        "distractors": [
            "접속하지 말 걸 그랬어요 (menyesal karena telah mengakses situs, bertolak belakang dengan rasa kecewa kehabisan tiket).",
            "접속할 수 있었어요 (hanya menyatakan kemampuan teoritis tanpa penyesalan emosional).",
            "접속하게 되었어요 (menyatakan hasil perubahan situasi di luar rencana).",
            "접속하기로 했어요 (hanya menyatakan janji temu masa depan)."
        ]
    },
    {
        "id": "kor-sim-06",
        "materi": "ANALISIS WACANA: TRADISI GOTONG ROYONG MASYARAKAT KOREA (품앗이 & 두레)",
        "topic": "Nilai Solidaritas Sosial Komunal Pertanian Tradisional Nusantara dan Korea",
        "stem": "Bacalah wacana antropologi budaya berikut:\n'한국 전통 농경 사회에서는 모내기나 추수철처럼 일손이 크게 부족할 때 마을 주민들이 서로 노동력을 무상으로 교환하는 '품앗이'와 공동 노동 조직인 '두레'가 발달하였다. 이러한 공동체적 협동 관습은 단순한 경제적 노동력 절감을 넘어, 마을 구성원 간의 유대감을 강화하고 상부상조의 사회적 자본을 형성하는 데 결정적인 역할을 하였다.'\nBerdasarkan teks di atas, padanan nilai sosiologis kearifan lokal yang PALING SETARA dalam konteks masyarakat Indonesia adalah...",
        "correct": "Tradisi gotong royong dan gugur gunung dalam menyelesaikan panen serta pembangunan fasilitas publik desa.",
        "distractors": [
            "Sistem sewa tanah feodal dengan upah bagi hasil harian tanpa ikatan solidaritas komunal.",
            "Lembaga pembiayaan perbankan modern yang memberikan pinjaman modal usaha berbunga rendah.",
            "Gerakan isolasionisme pedesaan untuk menolak interaksi ekonomi dengan warga dari daerah luar.",
            "Sistem kerja paksa rodi zaman kolonial untuk membangun infrastruktur jalan raya pos."
        ]
    },
    {
        "id": "kor-sim-07",
        "materi": "TATA BAHASA: PENGUNGKAPAN DAMPAK MUSIBAH TAK TERDUGA (-는 바람에)",
        "topic": "Alasan Pembatalan Acara Konser Musik Terbuka Akibat Angin Puting Beliung",
        "stem": "Pemberitahuan penyelenggara festival musik kampus:\n'갑자기 들이닥친 돌풍으로 야외 무대 조명 장치가 ( ... ) 관객 여러분의 안전을 위해 공연을 부득이 중단하게 되었습니다.'\nBentuk konjugasi peristiwa mendadak berdampak buruk (-는 바람에) dari verba '무너지다' (runtuh/roboh) adalah...",
        "correct": "무너지는 바람에 (akar verba 무너지- + akhiran kausalitas musibah mendadak berkonsekuensi negatif -는 바람에).",
        "distractors": [
            "무너지는 덕분에 (akhiran 'berkat/untunglah', sangat absurd untuk robohnya instalasi panggung musik).",
            "무너지기 때문에 (akhiran kausalitas netral yang kehilangan nuansa kepanikan musibah tak terduga).",
            "무너지더라도 (akhiran konsesi pengandaian meskipun yang merusak logika penundaan konser).",
            "무너지자마자 (hanya menyatakan kecepatan waktu urutan tanpa penekanan faktor penyebab utama)."
        ]
    },
    {
        "id": "kor-sim-08",
        "materi": "TATA BAHASA: KETIADAAN PILIHAN LAIN (-(으)ㄹ 수밖에 없다)",
        "topic": "Ketiadaan Alternatif Lain Selain Beristirahat Total Saat Terjangkit Demam Tinggi",
        "stem": "Saran dokter kepada seorang pekerja yang memaksakan diri masuk kantor:\n'체온이 39도까지 올라가고 독감 증상이 뚜렷하므로 오늘은 출근하지 말고 집에서 푹 ( ... ).'\nBentuk ekspresi ketiadaan pilihan selain istirahat dari verba '쉬다' (beristirahat) adalah...",
        "correct": "쉴 수밖에 없습니다 (akar verba 쉬- tanpa batchim berpadu dengan -ㄹ 수밖에 없다).",
        "distractors": [
            "쉬지 않을 수 있었습니다 (menyatakan kemampuan untuk tidak istirahat, membahayakan kesehatan pasien).",
            "쉬기로 되어 있었습니다 (hanya menyatakan jadwal libur formal yang sudah tercatat sebelumnya).",
            "쉴 뻔했습니다 (bermakna nyaris beristirahat namun akhirnya batal, kontradiktif dengan perintah dokter).",
            "쉬도록 했습니다 (mengimplikasikan menyuruh orang lain yang beristirahat)."
        ]
    },
    {
        "id": "kor-sim-09",
        "materi": "TATA BAHASA: PASIF SPONTAN DENGAN INFIKS '-이-' (보이다, 들리다)",
        "topic": "Suara Ombak Laut yang Terdengar Jelas dari Jendela Kamar Hotel",
        "stem": "Deskripsi keindahan suasana menginap di tepi pantai Haeundae Busan:\n'호텔 방 창문을 활짝 열자 시원한 바닷바람과 함께 철썩이는 파도 소리가 귀에 생생하게 ( ... ).'\nBentuk kata kerja pasif spontan (피동사) yang TEPAT dari verba dasar '듣다' (mendengar) adalah...",
        "correct": "들려왔습니다 (verba dasar 듣다 disisipi imbuhan pasif 리 menjadi 들리다, lalu berpadu dengan arah datang -어 오다).",
        "distractors": [
            "들었습니다 (bentuk aktif transitif di mana suara ombak yang mendengarkan telinga manusia).",
            "듣이었습니다 (kesalahan afiks pasif yang keliru menggunakan imbuhan 이 pada konsonan ㄷ).",
            "들리게 했습니다 (bentuk kausatif analitis yang menyuruh suara ombak bersuara).",
            "듣지 않도록 했습니다 (bentuk pencegahan agar deburan ombak tidak terdengar)."
        ]
    },
    {
        "id": "kor-sim-10",
        "materi": "ANALISIS WACANA: TREN EKONOMI KONSUMEN 'KASIMBI' (가심비)",
        "topic": "Pergeseran Paradigma dari 'Gaseongbi' (Rasio Harga/Fungsi) Menuju 'Gasimbi' (Kepuasan Emosional)",
        "stem": "Bacalah kutipan analisis tren konsumsi generasi muda Korea:\n'과거 소비자들은 가격 대비 성능을 따지는 '가성비(價性比)'를 최우선으로 고려하였으나, 최근에는 가격 대비 심리적 만족감을 중시하는 '가심비(價心比)' 소비가 대세로 자리 잡고 있다. 젊은 세대는 다소 비싸더라도 자신의 가치관에 부합하는 친환경 제품이나 정서적 힐링을 주는 소품, 취향 맞춤형 서비스에 기꺼이 지갑을 열고 있다.'\nBerdasarkan teks di atas, faktor penentu utama dalam perilaku konsumsi 'Gasimbi' adalah...",
        "correct": "Kepuasan emosional batin dan keselarasan nilai etis pribadi terhadap barang yang dibeli meskipun harganya relatif lebih mahal.",
        "distractors": [
            "Pencarian barang dengan harga paling murah di pasaran tanpa mempedulikan mutu dan estetika produk.",
            "Kepatuhan mutlak terhadap anjuran pemotongan anggaran rumah tangga yang dikeluarkan oleh kementerian keuangan.",
            "Penolakan terhadap seluruh produk ramah lingkungan demi memaksimalkan jumlah akumulasi tabungan pensiun.",
            "Kecenderungan membeli produk hanya berdasarkan rekomendasi selebritas asing tanpa pertimbangan pribadi."
        ]
    },
    {
        "id": "kor-sim-11",
        "materi": "TATA BAHASA: WICARA TAK LANGSUNG PERINTAH DENGAN BENTUK NEGASI (-지 말라고 하다)",
        "topic": "Instruksi Guru kepada Murid untuk Tidak Menyerah di Tengah Kesulitan",
        "stem": "Pesan motivasi wali kelas saat membimbing siswa bimbingan belajar:\n'선생님께서 우리에게 말씀하셨습니다: \"꿈을 향해 나아가는 과정에서 실패를 두려워하여 중간에 포기하지 마십시오.\"\nBentuk kutipan wicara tak langsung (간접화법) larangan yang TEPAT untuk menyampaikan kembali pesan guru adalah...",
        "correct": "포기하지 말라고 하셨습니다 (akar verba 포기하- + akhiran larangan tidak langsung -지 말라고 하다).",
        "distractors": [
            "포기하지 말자고 하셨습니다 (bentuk kutipan ajakan bersama yang mengubah perintah guru menjadi usulan setara).",
            "포기하지 않는다고 하셨습니다 (bentuk kutipan deklaratif bahwa guru sendiri yang tidak menyerah).",
            "포기하지 않냐고 하셨습니다 (bentuk kutipan interogatif yang menanyakan apakah siswa menyerah).",
            "포기하라고 하셨습니다 (makna terbalik yang mengutip guru menyuruh siswa untuk menyerah)."
        ]
    },
    {
        "id": "kor-sim-12",
        "materi": "TATA BAHASA: PENGUNGKAPAN KELAYAKAN TINDAKAN (-(으)ㄹ 만하다)",
        "topic": "Rekomendasi Film Dokumenter Sejarah Kemerdekaan yang Sangat Patut Ditonton",
        "stem": "Rekomendasi guru sejarah mengenai film dokumenter pahlawan kemerdekaan:\n'이 다큐멘터리 영화는 잊혀져 가던 독립운동가들의 헌신을 사실적으로 재조명하여 국민이라면 꼭 한 번 ( ... ).'\nBentuk ungkapan kelayakan rekomendasi (-(으)ㄹ 만하다) dari verba '보다' (menonton) adalah...",
        "correct": "볼 만합니다 (akar verba 보- tanpa batchim berpadu dengan penanda kelayakan rekomendasi -ㄹ 만하다).",
        "distractors": [
            "볼 리가 없습니다 (menyatakan kemustahilan untuk ditonton, sangat menghina karya edukasi sejarah).",
            "보기 십상입니다 (akhiran probabilitas rentan tertimpa bencana keburukan).",
            "보는 척했습니다 (menyatakan berpura-pura menonton film).",
            "보지 않을 수 없었습니다 (bentuk lampau keterpaksaan kaku yang tidak menyatakan rekomendasi persuasif)."
        ]
    },
    {
        "id": "kor-sim-13",
        "materi": "TATA BAHASA: KONSESI KONTRASTIF DENGAN VERBA PENEGAS (-기는커녕)",
        "topic": "Penyangkalan Ekstrem: Alih-alih Menabung, Uang Pokok Malah Habis Terkuras",
        "stem": "Keluhan seorang pekerja mengenai inflasi harga kebutuhan pokok:\n'월급이 물가 상승률을 따라가지 못해 매달 저축을 하( ... ) 기본 생활비를 대기에도 빠듯한 형편입니다.'\nBentuk konjugasi penyangkalan ekstrem 'alih-alih... malah...' (-기는커녕) dari verba '저축하다' adalah...",
        "correct": "하기는커녕 (akar verba 하- + nomina penanda nominalisasi -기 + partikel penyangkalan ekstrem 는커녕).",
        "distractors": [
            "하기는 하지만 (hanya mengakui secara wajar bahwa ia tetap berhasil menabung sedikit uang).",
            "할수록 (menyatakan hubungan proporsional semakin sering menabung semakin kekurangan).",
            "하는 셈 치고 (ungkapan menganggap seolah-olah telah menabung).",
            "할 텐데 (klausula pengantar praduga yang tidak mengekspresikan kontras ekstrem)."
        ]
    },
    {
        "id": "kor-sim-14",
        "materi": "ANALISIS WACANA: BUDAYA MINUM TEH TRADISIONAL (다도 / 茶道)",
        "topic": "Nilai Meditatif Ketenangan Jiwa dan Tata Krama Penyajian Teh Hijau Tradisional",
        "stem": "Bacalah artikel kebudayaan spiritual Korea berikut:\n'한국의 전통 다도(茶道)는 단순히 차를 우려 마시는 기호 행위를 넘어, 차를 달이고 따르는 일련의 정제된 동작을 통해 번잡한 마음을 비우고 자연과 교감하는 명상적 수양의 과정이다. 다도 예절에서는 찻잔을 잡는 손의 위치, 차의 온도와 향을 음미하는 순서, 손님을 배려하는 조용한 눈빛 하나에도 정성과 존중의 미덕이 깃들어 있다.'\nNilai filosofis esensial yang tercermin dalam tradisi 'Dado' berdasarkan teks di atas adalah...",
        "correct": "Pengendalian diri dan pembersihan batin melalui kesadaran penuh serta penghormatan tulus kepada tamu dalam setiap tetes sajian teh.",
        "distractors": [
            "Persaingan kecepatan menyeduh minuman panas demi efisiensi waktu kerja di kantor modern.",
            "Pamer kemewahan perangkat porselen istana untuk menunjukkan strata kasta ekonomi keluarga bangsawan.",
            "Kewajiban menghafal rumus kimia kandungan antioksidan daun teh hijau secara akademis.",
            "Penyajian jamuan pesta minuman beralkohol yang diiringi musik gamelan berirama cepat."
        ]
    },
    {
        "id": "kor-sim-15",
        "materi": "TATA BAHASA: KONTRAFAKTUAL HIPOTETIKAL DENGAN HASIL BURUK (-았/었더라면 큰일 날 뻔했다)",
        "topic": "Rasa Syukur Terselamatkan dari Kecelakaan Berkat Mengenakan Sabuk Pengaman",
        "stem": "Testimoni korban kecelakaan lalu lintas di jalan tol:\n'사고 당시 안전벨트를 매고 있지 ( ... ) 차량 밖으로 튕겨 나가서 정말 큰 부상을 입을 뻔했습니다.'\nBentuk pengandaian kontrafaktual negatif (-았/었더라면) dari verba '않다' (tidak mengenakan) adalah...",
        "correct": "않았더라면 (akar verba negasi 않- berpadu dengan kala lampau 았- + akhiran kontrafaktual -더라면).",
        "distractors": [
            "않는다면 (pengandaian masa kini/depan biasa tanpa konteks kecelakaan nyata yang telah berhasil dilalui).",
            "않았을수록 (kombinasi struktur proporsional yang merusak tata kalimat kecelakaan).",
            "않더라도 (hanya menyatakan konsesi 'meskipun tidak memakai', fatal bagi keselamatan).",
            "않았을 텐데 (klausula pengantar yang tidak dapat berfungsi sebagai anteseden pengandaian celaka)."
        ]
    },
    {
        "id": "kor-sim-16",
        "materi": "TATA BAHASA: TINDAKAN SEGERA SETELAH KEJADIAN PERTAMA (-자마자)",
        "topic": "Tindakan Langsung Menghubungi Layanan Darurat Begitu Melihat Percikan Api",
        "stem": "Tindakan cepat tanggap satpam gedung saat melihat korsleting listrik:\n'관리실 직원은 배전반에서 연기와 불꽃이 튀는 것을 목격하( ... ) 즉시 119 화재 신고 센터로 전화를 걸었습니다.'\nBentuk konjugasi kesegeraan seketika (-자마자) yang TEPAT dari verba '목격하다' (menyaksikan) adalah...",
        "correct": "목격하자마자 (akar verba 하- langsung dilekati akhiran kesegeraan tindakan seketika -자마자).",
        "distractors": [
            "목격한 후에야 비로소 (mengimplikasikan penundaan waktu yang cukup lama sebelum melapor).",
            "목격하기는커녕 (menyangkal keras pernah melihat kebakaran tersebut).",
            "목격하는 척하며 (bermakna berpura-pura melihat percikan api).",
            "목격할수록 (mengimplikasikan semakin sering melihat percikan api semakin lambat menelpon)."
        ]
    },
    {
        "id": "kor-sim-17",
        "materi": "TATA BAHASA: DUA PERISTIWA YANG SALING TERIKAT / INTERDEPENDEN (-는 한편)",
        "topic": "Perkembangan Industri Otomotif Ramah Lingkungan Sambil Mengembangkan Jaringan Pengisian Daya",
        "stem": "Laporan kebijakan industri energi hijau:\n'정부는 전기차 보급을 대폭 확대하( ... ), 고속도로 휴게소와 도심 곳곳에 급속 충전 인프라를 신속히 확충하고 있습니다.'\nBentuk ungkapan pelaksanaan dua kebijakan komplementer simultan (-는 한편) dari verba '확대하다' adalah...",
        "correct": "확대하는 한편 (akar verba 확대하- + penanda aksi simultan komplementer -는 한편).",
        "distractors": [
            "확대하기는커녕 (menyangkal keras adanya perluasan kendaraan listrik).",
            "확대하는 셈 치고 (menganggap seolah-olah perluasan telah selesai padahal belum).",
            "확대할 리가 없이 (menyatakan kemustahilan ekspansi kendaraan listrik).",
            "확대할 뻔하며 (menyatakan nyaris memperluas namun akhirnya dibatalkan)."
        ]
    },
    {
        "id": "kor-sim-18",
        "materi": "ANALISIS WACANA: KEUNIKAN TEKNIK FERMENTASI MAKANAN KOREA (장류 & 김치)",
        "topic": "Peran Mikroorganisme Bersahabat dan Wadah Tembikar Tanah Liat 'Onggi' (옹기)",
        "stem": "Bacalah wacana sains kuliner tradisional berikut:\n'한국 발효식품(된장, 고추장, 간장, 김치)의 우수성은 숨 쉬는 그릇이라 불리는 '옹기(甕器)'와 불가분의 관계를 맺고 있다. 미세한 기포가 분포하는 옹기는 외부의 신선한 공기는 통과시키면서 수분과 유해 미생물의 침입은 차단하여 유익한 젖산균의 증식을 최적화한다. 이러한 지혜는 인공 방부제 없이도 장기간 신선한 영양과 독특한 풍미를 보존하는 과학적 토대가 되었다.'\nBerdasarkan wacana di atas, fungsi esensial dari wadah tembikar 'Onggi' dalam proses fermentasi adalah...",
        "correct": "Memfasilitasi sirkulasi udara mikro secara alami sekaligus menghalau bakteri perusak sehingga bakteri asam laktat dapat berkembang biak optimal.",
        "distractors": [
            "Memanaskan bahan makanan secara buatan dengan menyerap radiasi ultraviolet matahari secara ekstrem.",
            "Mengubah komposisi sayuran menjadi zat kimia sintetis agar rasa asam tereliminasi total.",
            "Menutup rapat seluruh rongga udara hingga mencapai kondisi hampa udara absolut tanpa sirkulasi gas.",
            "Menghancurkan seluruh kultur bakteri hidup termasuk bakteri asam laktat demi sterilisasi kimiawi."
        ]
    },
    {
        "id": "kor-sim-19",
        "materi": "TATA BAHASA: PENGUNGKAPAN ANGGAPAN SEOLAH-OLAH (-(으)ㄴ/는 셈 치다)",
        "topic": "Merelakan Uang yang Hilang Seolah-olah Sedang Bersedekah / Membayar Pengalaman Hidup",
        "stem": "Penghiburan diri seseorang saat tertipu membeli barang imitasi secara daring:\n'이미 사기를 당해 돌려받기 어려운 돈이니, 인생의 값비싼 교훈을 배운 ( ... ) 잊어버리기로 마음먹었습니다.'\nBentuk konjugasi merelakan/menganggap seolah-olah (-(으)ㄴ 셈 치다) dari verba '배우다' (mempelajari) adalah...",
        "correct": "배운 셈 치고 (akar verba 배우- berpadu dengan kala lampau penanda anggapan -ㄴ 셈 치다).",
        "distractors": [
            "배우기는커녕 (menyatakan penyangkalan keras pernah belajar dari pengalaman).",
            "배울수록 (menyatakan hubungan proporsional semakin sering tertipu semakin rugi).",
            "배울 뻔하고 (bermakna nyaris belajar namun gagal memahami).",
            "배워야만 하고 (ungkapan kewajiban yang tidak membawa nuansa penghiburan batin)."
        ]
    },
    {
        "id": "kor-sim-20",
        "materi": "TATA BAHASA: PENGUNGKAPAN KEMUSTAHILAN LOGIS (-(으)ㄹ 리가 없다)",
        "topic": "Keyakinan Bahwa Rekan Kerja yang Sangat Jujur dan Amanah Tidak Mungkin Menggelapkan Uang",
        "stem": "Pembelaan manajer terhadap staf teladan yang difitnah:\n'김 대리는 입사 이래 단 한 번도 부정을 저지른 적이 없는 성실한 직원이므로 회사 공금을 횡령( ... ).'\nBentuk ungkapan kemustahilan rasional (-(으)ㄹ 리가 없다) yang TEPAT dari verba '횡령하다' (menggelapkan dana) adalah...",
        "correct": "횡령했을 리가 없습니다 (akar verba 횡령하- berpadu dengan kala lampau penanda kemustahilan logis -았/었을 리가 없다).",
        "distractors": [
            "횡령할 뻔했습니다 (bermakna 김 대리 nyaris saja menggelapkan uang perusahaan, justru mencurigakan).",
            "횡령하는 셈입니다 (bermakna tindakannya bisa dianggap sebagai penggelapan uang).",
            "횡령하기 십상입니다 (menyatakan 김 대리 rentan dan mudah terjerumus korupsi).",
            "횡령하지 않을 수 없었습니다 (menyatakan 김 대리 terpaksa menggelapkan uang tanpa pilihan lain)."
        ]
    },
    {
        "id": "kor-sim-21",
        "materi": "TATA BAHASA: WICARA TAK LANGSUNG DENGAN NOMINA (-이라고 하다)",
        "topic": "Pengenalan Istilah Ilmiah Kecerdasan Buatan dalam Bahasa Korea Menggunakan Kutipan Tak Langsung",
        "stem": "Penjelasan dosen informatika dalam kuliah pengantar sains data:\n'인간의 지적 능력을 컴퓨터 소프트웨어로 구현하여 스스로 학습하도록 만든 기술을 '인공지능( ... ) 부릅니다.'\nBentuk penanda kutipan istilah nama benda (-이라고 하다) yang TEPAT dari kata benda ber-batchim '인공지능' (AI) adalah...",
        "correct": "이라고 (nomina berakhiran konsonan/batchim 인공지능 berpasangan dengan penanda kutipan definisi -이라고).",
        "distractors": [
            "라고 (kesalahan menggunakan 라고 yang hanya diperuntukkan bagi kata benda berakhiran vokal).",
            "다고 (kesalahan menggunakan akhiran adjektiva untuk kata benda rujukan nama istilah).",
            "자고 (akhiran ajakan bersama yang tidak memiliki fungsi penetapan istilah nomina).",
            "냐고 (akhiran interogatif yang salah fungsi gramatikal)."
        ]
    },
    {
        "id": "kor-sim-22",
        "materi": "ANALISIS WACANA: TRANSFORMASI SASTRA LISAN KE SASTRA TULIS (판소리 / PANSORI)",
        "topic": "Seni Bercerita Teatrikal Berbalas Vokal dan Tabuhan Genderang Buk (소리꾼 & 고수)",
        "stem": "Bacalah teks apresiasi warisan mahakarya lisan UNESCO berikut:\n'유네스코 인류무형문화유산으로 등재된 '판소리'는 한 명의 소리꾼이 고수(북 치는 사람)의 북장단에 맞추어 창(노래), 아니리(말), 너름새(몸짓)를 섞어가며 장편의 서사적 이야기를 구연하는 전통 종합 공연 예술이다. 관객들은 공연 중간중간에 \"얼씨구!\", \"좋다!\"와 같은 '추임새'를 넣어 공연자와 호흡을 맞추며 신명 나는 축제의 장을 완성한다.'\nUnsur interaktif khas yang membedakan pertunjukan Pansori dari teater opera Barat berdasarkan teks di atas adalah...",
        "correct": "Keterlibatan aktif penonton dalam menyemangati penampil melalui seruan responsif spontan (Chuimsae) di sepanjang pementasan.",
        "distractors": [
            "Keharusan penonton untuk duduk mematung dalam keheningan mutlak tanpa suara sedikit pun.",
            "Penggunaan puluhan instrumen musik gesek dan tiup barat secara orkestral di bawah panggung.",
            "Pemisahan panggung yang sangat tinggi dan berjarak puluhan meter dari tempat duduk penonton.",
            "Penyajian naskah yang wajib dibaca secara kaku dari lembaran buku panduan tanpa improvisasi gerak."
        ]
    },
    {
        "id": "kor-sim-23",
        "materi": "TATA BAHASA: PENGUNGKAPAN KEKHAWATIRAN MASA DEPAN (-(으)ㄹ까 봐)",
        "topic": "Kekhawatiran Terlambat Hadir Pertemuan Bisnis Karena Antrean Taksi yang Panjang",
        "stem": "Alasan seorang eksekutif memilih naik subway cepat:\n'월요일 아침 출근길 도로가 정체되어 거래처 약속 시간에 늦( ... ) 차를 두고 지하철을 탔습니다.'\nBentuk ungkapan kekhawatiran antisipatif (-(으)ㄹ까 봐) dari kata kerja '늦다' (terlambat) adalah...",
        "correct": "늦을까 봐 (akar verba ber-batchim 늦- berpadu dengan penanda kecemasan preventif -을까 봐).",
        "distractors": [
            "늦는 척하여 (bermakna berpura-pura terlambat, sangat kontradiktif dengan upaya naik kereta bawah tanah).",
            "늦을 리가 없어서 (menyatakan kepastian tidak akan terlambat sehingga tidak perlu cemas).",
            "늦을 만해서 (menyatakan kelayakan untuk terlambat).",
            "늦기는커녕 (menyangkal keras pernah terlambat)."
        ]
    },
    {
        "id": "kor-sim-24",
        "materi": "TATA BAHASA: AKIBAT KUMULATIF BERTAHAP (-다 보니)",
        "topic": "Hasil Belajar Kosakata Secara Rutin yang Tanpa Disadari Berbuah Kemampuan Membaca Berita",
        "stem": "Refleksi kemajuan belajar seorang pembelajar otodidak:\n'매일 한국어 신문 사설을 한 편씩 꾸준히 읽( ... ) 어느새 시사 어휘 실력이 크게 늘어 뉴스 방송도 자연스럽게 이해하게 되었습니다.'\nBentuk konjugasi tindakan berulang berkesinambungan (-다 보니) dari verba '읽다' (membaca) adalah...",
        "correct": "읽다 보니 (akar verba 읽- + akhiran pengalaman akumulatif berulang -다 보니).",
        "distractors": [
            "읽자마자 (menyatakan kesegeraan instan, mustahil menguasai kosakata berita rumit dalam satu detik membaca).",
            "읽기는커녕 (menyangkal keras pernah membaca tajuk rencana koran).",
            "읽을 텐데 (klausula pengantar praduga yang tidak mengekspresikan proses pengalaman nyata).",
            "읽어야만 (hanya menyatakan beban kewajiban mutlak tanpa menyinggung hasil penemuan akumulatif)."
        ]
    },
    {
        "id": "kor-sim-25",
        "materi": "TATA BAHASA: PENGUNGKAPAN KEMUDAHAN TERTEMPA KEBURUKAN (-기 십상이다)",
        "topic": "Kerentanan Tertipu Informasi Hoaks di Media Sosial Tanpa Verifikasi Kritis",
        "stem": "Peringatan pakar literasi digital kepada para pengguna jejaring sosial:\n'출처가 불분명한 자극적인 인터넷 뉴스를 비판적 검증 없이 그대로 믿었다가는 거짓 정보에 속( ... ). 기사의 진위 여부를 반드시 확인해야 합니다.'\nBentuk ungkapan kerentanan probabilitas negatif (-기 십상이다) dari verba '속다' (tertipu) adalah...",
        "correct": "속기 십상입니다 (akar verba ber-batchim 속- + akhiran risiko tinggi tertimpa petaka -기 십상이다).",
        "distractors": [
            "속을 리가 없습니다 (menyatakan 'mustahil tertipu', meremehkan bahaya konten manipulatif di internet).",
            "속는 셈 칩니다 (bermakna sengaja mengikhlaskan diri ditipu oleh berita bohong).",
            "속을 만합니다 (menyatakan berita bohong tersebut sangat layak untuk dipercayai).",
            "속는 척합니다 (bermakna berpura-pura tertipu padahal sadar sepenuhnya)."
        ]
    },

    # -------------------------------------------------------------------------
    # 5 BUTIR PILIHAN GANDA KOMPLEKS / MULTI-SELECT (kor-sim-26 s.d. kor-sim-30)
    # -------------------------------------------------------------------------
    {
        "id": "kor-sim-26",
        "type": "complex",
        "materi": "TATA BAHASA & SOSIOLINGUISTIK: KAIDAH KESANTUNAN TINGGI (HONORIFIK / 높임말)",
        "topic": "Identifikasi Seluruh Kalimat yang Memenuhi Kaidah Kesantunan Gramatikal Baku Korea",
        "stem": "Perhatikan lima kalimat tuturan sehari-hari berikut!\nManakah DUA pernyataan yang mematuhi kaidah tata bahasa honorifik (높임말) dan kesantunan sosial secara BENAR?",
        "options": [
            "할아버지께서는 지금 방에서 편안히 주무시고 계십니다.",
            "선생님, 제가 오늘 작성한 보고서를 직접 선생님께 읽어 드리겠습니다.",
            "사장님, 저에게 약속 시간이 언제인지 직접 말씀해 주십시오.",
            "어머니가 저한테 밥을 많이 먹었습니다.",
            "과장님께서는 오늘 오후에 급한 출장이 계십니다."
        ],
        "correctAnswer": [0, 1]
    },
    {
        "id": "kor-sim-27",
        "type": "complex",
        "materi": "ANALISIS WACANA: 4 PRINSIP DAUR ULANG KOREA (분리배출)",
        "topic": "Tindakan-Tindakan Warga yang Sesuai dengan Regulasi Lingkungan Hidup Nasional Korea",
        "stem": "Perhatikan skenario pemilahan sampah di kompleks apartemen kota Seoul berikut!\nManakah DUA tindakan warga yang SESUAI secara tepat dengan 4 prinsip baku pemilahan sampah daur ulang (비우고, 헹구고, 분리하고, 섞지 않는다)?",
        "options": [
            "Membilas bersih botol kaca sirup dengan air dan membuang tutup logamnya ke wadah khusus kaleng/besi.",
            "Membuang sisa minyak goreng bekas dan kuah ramen pedas langsung ke wadah sampah daur ulang plastik.",
            "Melepas label stiker vinil dari botol air mineral transparan dan meremas botol hingga pipih sebelum dibuang.",
            "Mencampurkan pecahan cermin rias yang rusak ke dalam kantong daur ulang kaca transparan.",
            "Memasukkan popok bayi dan puntung rokok ke dalam kantong kompos sampah makanan organik."
        ],
        "correctAnswer": [0, 2]
    },
    {
        "id": "kor-sim-28",
        "type": "complex",
        "materi": "TATA BAHASA: POLA WICARA TAK LANGSUNG (간접화법)",
        "topic": "Pasangan Konversi Tuturan Langsung Menjadi Wicara Tak Langsung yang Benar",
        "stem": "Perhatikan lima pasangan konversi kalimat langsung ke tuturan tak langsung berikut!\nManakah DUA pasangan konversi yang memiliki struktur sintaksis yang BENAR?",
        "options": [
            "\"날씨가 정말 춥습니다.\" -> 날씨가 정말 춥다고 했습니다.",
            "\"친구와 함께 도서관에 갑시다.\" -> 도서관에 가자고 했습니다.",
            "\"내일 시험이 어렵습니까?\" -> 내일 시험이 어렵다고 했습니다.",
            "\"이 문을 지금 즉시 닫으십시오.\" -> 이 문을 닫는다고 했습니다.",
            "\"저는 인도네시아 사람입니다.\" -> 인도네시아 사람이라고 물었습니다."
        ],
        "correctAnswer": [0, 1]
    },
    {
        "id": "kor-sim-29",
        "type": "complex",
        "materi": "ANALISIS WACANA: KEUNGGULAN LINGUISTIK AKSARA HANGEUL",
        "topic": "Faktor Ilmiah dan Filosofis yang Menjadikan Hangeul Diakui UNESCO",
        "stem": "Perhatikan klaim-klaim mengenai karakteristik aksara Hangeul ciptaan Raja Sejong berikut!\nManakah DUA keunggulan ilmiah dan filosofis aksara Hangeul yang diakui secara global?",
        "options": [
            "Bentuk huruf konsonan dirancang secara sistematis meniru bentuk organ vokal manusia saat melafalkan bunyi tersebut.",
            "Huruf vokal dibentuk berdasarkan filosofi kosmis Timur yang menyimbolkan langit (천), bumi (지), dan manusia (인).",
            "Hangeul dirancang khusus agar hanya kaum bangsawan istana yang dapat menguasai sandi literasi kenegaraan.",
            "Karakter Hangeul mengadopsi puluhan ribu simbol piktograf rumit yang mewajibkan hafalan tanpa kaidah fonologis.",
            "Aksara Hangeul diciptakan untuk memusnahkan seluruh warisan sastra lisan rakyat pedesaan Joseon."
        ],
        "correctAnswer": [0, 1]
    },
    {
        "id": "kor-sim-30",
        "type": "complex",
        "materi": "TATA BAHASA: PENGGUNAAN PARTIKEL KOMPLEKS (-(으)로, 에, 에서, 보다)",
        "topic": "Ketepatan Penggunaan Partikel Kasus dan Instrumental dalam Kalimat Baku",
        "stem": "Perhatikan lima kalimat bahasa Korea berikut!\nManakah DUA kalimat yang menggunakan partikel kasus dan adverbial secara TEPAT?",
        "options": [
            "지하철이 버스보다 출퇴근 시간에 훨씬 빠르고 정확합니다.",
            "저는 아침에 빵을 나이프로 잘라서 맛있게 먹었습니다.",
            "친구는 도서관에 친구와 함께 열심히 공부하고 있습니다.",
            "우리는 제주도에서 비행기로 갈 계획입니다.",
            "식당에 음식이 아주 맛있어서 손님이 많이 있습니다."
        ],
        "correctAnswer": [0, 1]
    },

    # -------------------------------------------------------------------------
    # 5 BUTIR MATRIKS BENAR / SALAH (kor-sim-31 s.d. kor-sim-35)
    # -------------------------------------------------------------------------
    {
        "id": "kor-sim-31",
        "type": "matrix",
        "materi": "EVALUASI KRITIS: KAIDAH PENGGUNAAN VERBA KHUSUS HONORIFIK (높임말)",
        "topic": "Verifikasi Kebenaran Penggunaan Kosakata Khusus Penghormatan",
        "stem": "Evaluasi ketepatan penggunaan bentuk kata kerja honorifik leksikal khusus dalam kalimat berikut (Benar / Salah)!",
        "rows": [
            "Kata '계시다' digunakan untuk sosok manusia yang dihormati di suatu lokasi (예: 할머니께서 집에 계십니다).",
            "Kata '있으시다' digunakan saat merujuk pada benda/jadwal yang dimiliki orang tua (예: 선생님께서는 질문이 있으십니다).",
            "Kata '드시다' boleh digunakan saat pembicara membicarakan dirinya sendiri yang sedang makan nasi di depan orang tua."
        ],
        "columns": ["Benar", "Salah"],
        "correctAnswer": {
            "0": "Benar",
            "1": "Benar",
            "2": "Salah"
        }
    },
    {
        "id": "kor-sim-32",
        "type": "matrix",
        "materi": "EVALUASI KRITIS: DISTINGSI SEBAB AKIBAT (-아/어서 VS -(으)니까)",
        "topic": "Kaidah Sintaksis Pembatasan Jenis Klausa Akhir pada Konjungsi Sebab Akibat",
        "stem": "Tentukan keabsahan kaidah sintaksis penggunaan akhiran kausalitas bahasa Korea berikut (Benar / Salah)!",
        "rows": [
            "Akhiran '-아/어서' boleh diikuti oleh kalimat perintah (-(으)세요) maupun kalimat ajakan (-(으)ㅂ시다).",
            "Akhiran '-(으)니까' adalah bentuk yang tepat digunakan saat klausa utama berupa ajakan mari kita pergi (갑시다).",
            "Penanda kala lampau (-았/었-) tidak boleh dilekatkan langsung di depan akhiran sebab akibat '-아/어서'."
        ],
        "columns": ["Benar", "Salah"],
        "correctAnswer": {
            "0": "Salah",
            "1": "Benar",
            "2": "Benar"
        }
    },
    {
        "id": "kor-sim-33",
        "type": "matrix",
        "materi": "EVALUASI KRITIS: BUDAYA DAN TRADISI HARI BESAR KOREA (명절)",
        "topic": "Verifikasi Pernyataan Mengenai Tradisi Seollal dan Chuseok",
        "stem": "Tentukan kebenaran fakta budaya mengenai hari raya tradisional Korea berikut (Benar / Salah)!",
        "rows": [
            "Pada perayaan Seollal (Tahun Baru Imlek), masyarakat menyantap hidangan sup kue beras putih 'Tteokguk'.",
            "Kue 'Songpyeon' berbentuk bulan sabit dibuat dari hasil panen beras baru khusus untuk hari raya Chuseok.",
            "Tradisi sungkem 'Sebae' dilakukan oleh generasi muda kepada orang yang lebih tua saat malam festival Chuseok."
        ],
        "columns": ["Benar", "Salah"],
        "correctAnswer": {
            "0": "Benar",
            "1": "Benar",
            "2": "Salah"
        }
    },
    {
        "id": "kor-sim-34",
        "type": "matrix",
        "materi": "EVALUASI KRITIS: ARSITEKTUR TRADISIONAL HANOK (한옥)",
        "topic": "Prinsip Kerja Sistem Pemanas Lantai 'Ondol' dan Ventilasi Udara 'Maru'",
        "stem": "Tentukan kebenaran analisis struktural mengenai arsitektur tradisional Hanok berikut (Benar / Salah)!",
        "rows": [
            "Sistem 'Ondol' memanfaatkan hawa panas asap tungku yang dialirkan di bawah lantai batu untuk menghangatkan kamar di musim dingin.",
            "Koridor kayu 'Maru' dirancang terbuka dengan lantai terangkat dari tanah untuk mengalirkan angin sejuk di musim panas.",
            "Rumah Hanok dirancang menggunakan material baja sintetis modern agar kedap udara secara mutlak terhadap lingkungan alam sekitar."
        ],
        "columns": ["Benar", "Salah"],
        "correctAnswer": {
            "0": "Benar",
            "1": "Benar",
            "2": "Salah"
        }
    },
    {
        "id": "kor-sim-35",
        "type": "matrix",
        "materi": "EVALUASI KRITIS: SISTEM BILANGAN SINO-KOREA VS ASLI KOREA",
        "topic": "Penentuan Sistem Angka Sesuai Objek dan Satuan Penggolong (Counter Units)",
        "stem": "Tentukan kebenaran kaidah penggunaan sistem bilangan bahasa Korea berikut (Benar / Salah)!",
        "rows": [
            "Satuan jam (시) menggunakan bilangan Asli Korea, sedangkan satuan menit (분) menggunakan bilangan Sino-Korea.",
            "Penghitungan jumlah lembaran kertas (장) dan botol minuman (병) menggunakan bilangan Sino-Korea (일, 이, 삼...).",
            "Penyebutan nama bulan kalender (월) selalu menggunakan bilangan Sino-Korea (dengan kekecualian 유월 dan 시월)."
        ],
        "columns": ["Benar", "Salah"],
        "correctAnswer": {
            "0": "Benar",
            "1": "Salah",
            "2": "Benar"
        }
    }
]
