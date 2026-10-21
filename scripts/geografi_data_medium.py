# -*- coding: utf-8 -*-
"""
geografi_data_medium.py
-----------------------
25 Authentic Medium Practice Questions for TKA 2026 Geografi (SMA/MA Soshum).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: geo-lat-m-01 .. geo-lat-m-25
"""

GEOGRAFI_MEDIUM_ITEMS = [
    {
        "id": "geo-lat-m-01",
        "materi": "DINAMIKA LITOSFER & PEDOSFER",
        "topic": "Siklus Batuan dan Klasifikasi Batuan Beku Berdasarkan Tempat Pembekuan",
        "stem": "Magma pijar di dalam astenosfer mengalami pendinginan dan pembekuan pada berbagai kedalaman litosfer bumi. Perbedaan tekstur kristal antara batuan granit (batuan beku dalam / plutonik) dan batuan obsidian / basal (batuan beku luar / efusif) dijelaskan oleh fenomena...",
        "correct": "Batuan granit membeku sangat lambat jauh di dalam kerak bumi sehingga atom-atom mineral memiliki waktu cukup untuk membentuk kristal-kristal besar berbutir kasar (faneritik), sedangkan obsidian/basal membeku seketika di permukaan bumi sehingga membentuk tekstur amorf halus atau kaca tanpa kristal (afanitik).",
        "distractors": [
            "Batuan granit terbentuk akibat tekanan hidrotermal bawah laut sedangkan basal terbentuk dari abu vulkanik yang memadat di danau kawah.",
            "Batuan obsidian membeku di bawah pengaruh tekanan tektonik lempeng konvergen sedangkan granit membeku pada zona sesar transform.",
            "Batuan granit hanya tersusun dari mineral kalsit gamping sedangkan batuan basal terbentuk dari fosil cangkang moluska laut dalam.",
            "Kedua jenis batuan membeku pada kecepatan yang sama tetapi granit terpapar sinar radiasi matahari sehingga butirannya membesar."
        ],
        "formula": {
            "title": "KLASIFIKASI BATUAN BEKU BERDASARKAN GENESA",
            "latex": "\\begin{cases} \\mathbf{\\text{Batuan Beku Dalam (Plutonik/Abisis):}} & \\text{Pendinginan sangat lambat} \\implies \\mathbf{\\text{Kristal Besar Kasar (Faneritik)}} \\ (\\text{Granit, Diorit, Gabro}) \\\\ \\text{Batuan Beku Gang (Korok/Porfirik):} & \\text{Pendinginan sedang di celah pipa} \\implies \\text{Kristal Campuran (Porfiri)} \\\\ \\mathbf{\\text{Batuan Beku Luar (Efusif/Vulkanik):}} & \\text{Pendinginan seketika di udara/air} \\implies \\mathbf{\\text{Halus/Kaca (Afanitik)}} \\ (\\text{Obsidian, Basal, Andesit, Riolit}) \\end{cases}",
            "legend": "• Kecepatan pendinginan magma berbanding terbalik dengan ukuran butir kristal mineral yang terbentuk"
        },
        "hints": {
            "concept": "Batuan beku dalam (granit) membeku perlahan -> kristal kasar (faneritik). Batuan beku luar (obsidian/basal) membeku seketika di permukaan -> kristal halus/kaca (afanitik).",
            "execution": "Pilih opsi: Granit membeku lambat di dalam kerak (faneritik), obsidian membeku seketika di permukaan (afanitik/kaca)."
        }
    },
    {
        "id": "geo-lat-m-02",
        "materi": "DINAMIKA LITOSFER & PEDOSFER",
        "topic": "Zona Tumbukan Lempeng Konvergen Subduksi di Indonesia",
        "stem": "Pertemuan antara Lempeng Samudra Indo-Australia yang menunjam ke bawah Lempeng Benua Eurasia di sepanjang pantai barat Sumatera, selatan Jawa, hingga Nusa Tenggara membentuk sistem busur subduksi aktif (_Sunda Arc_). Bentang alam dasar samudra dan bahaya geologis yang terbentuk tepat di sepanjang garis penunjaman lempeng tersebut adalah...",
        "correct": "Palung Laut Dalam (_Trench_ / Palung Jawa), jajaran kepulauan busur luar non-vulkanik (Pulau Simeulue, Nias, Mentawai, Enggano), busur pegunungan vulkanik aktif di pedalaman, serta potensi gempa megathrust yang memicu tsunami.",
        "distractors": [
            "Pematang tengah samudra (_Mid-Ocean Ridge_) yang memuntahkan lava bantal dasar laut dan membentuk dataran abisal baru.",
            "Sesar geser mendatar tanpa aktivitas kegempaan yang memisahkan benua Australia dan pulau Jawa sejauh ribuan kilometer.",
            "Zona rift valley daratan luas yang membuat pulau Sumatera dan Jawa saling menjauh membentuk danau air tawar purba.",
            "Kubah garam raksasa yang menutupi seluruh cekungan sedimen minyak bumi di perairan utara laut Jawa."
        ],
        "formula": {
            "title": "ANATOMI ZONA SUBDUKSI BUSUR KEPULAUAN (SUNDA ARC SYSTEM)",
            "latex": "\\text{Lempeng Samudra (Densitas Tinggi)} \\xrightarrow{\\text{Subduksi}} \\text{Lempeng Benua} \\implies \\begin{cases} \\text{1. Palung Laut (Trench)} \\\\ \\text{2. Busur Luar Non-Vulkanik (Prisma Akresi)} \\\\ \\text{3. Cekungan Muka Busur (Forearc Basin)} \\\\ \\mathbf{\\text{4. Busur Vulkanik Magmatik (Volcanic Arc)}} \\\\ \\mathbf{\\text{5. Zona Megathrust Gempa/Tsunami}} \\end{cases}",
            "legend": "• Zona Wadati-Benioff: Bidang miring pusat gempa dari dangkal di palung hingga sangat dalam (> 300 km) di bawah pulau Jawa"
        },
        "hints": {
            "concept": "Ciri zona subduksi: Palung laut (trench), busur luar prisma akresi (Nias, Mentawai), jajaran gunung api aktif (busur vulkanik), dan potensi gempa megathrust/tsunami.",
            "execution": "Pilih: Palung laut dalam, busur luar non-vulkanik (Nias, Mentawai), busur vulkanik aktif, dan gempa megathrust."
        }
    },
    {
        "id": "geo-lat-m-03",
        "materi": "DINAMIKA LITOSFER & PEDOSFER",
        "topic": "Bentang Alam Karst Hasil Pelapukan Kimiawi di Kawasan Karst Gunung Sewu",
        "stem": "Kawasan Karst Gunung Sewu (membentang di Gunungkidul, Wonogiri, dan Pacitan) didominasi oleh perbukitan kerucut gamping (_cockpit karst_). Proses pelarutan kimiawi kalsium karbonat ($CaCO_3$) oleh air hujan yang mengandung karbon dioksida ($CO_2$) membentuk fenomena eksokarst berupa cekungan tertutup berbentuk corong tempat masuknya air ke bawah tanah yang dinamakan...",
        "correct": "Doline (Sinkhole), yang jika beberapa doline menyatu membentuk cekungan pelarutan yang lebih luas disebut Uvala atau Polje.",
        "distractors": [
            "Stalaktit, yaitu bentukan endapan kapur yang menggantung runcing menetes dari atap gua kapur.",
            "Stalagmit, yaitu bentukan endapan kalsit tumpul yang tumbuh menjulang tegak dari lantai dasar gua kapur.",
            "Mekander, yaitu kelokan sungai berkelok yang terbentuk di dataran alluvial berlumpur halus.",
            "Sand Dune (Barchan), yaitu gumuk pasir pantai yang dihembus angin laut muson timur di pantai Parangtritis."
        ],
        "formula": {
            "title": "REAKSI KIMIAWI PELARUTAN KARSTIFIKASI",
            "latex": "\\begin{aligned} \\text{Air Hujan Asam:} & \\quad H_2O + CO_2 \\rightleftharpoons H_2CO_3 \\text{ (Asam Karbonat)} \\\\ \\text{Pelarutan Batugamping:} & \\quad CaCO_3 + H_2CO_3 \\rightleftharpoons Ca(HCO_3)_2 \\text{ (Kalsium Bikarbonat Larut)} \\\\ \\mathbf{\\text{Bentuk Eksokarst:}} & \\quad \\mathbf{\\text{Doline (Sinkhole)} \\to \\text{Uvala} \\to \\text{Polje}} \\\\ \\mathbf{\\text{Bentuk Endokarst:}} & \\quad \\text{Gua Karst, Stalaktit (Atap), Stalagmit (Lantai), Sungai Bawah Tanah} \\end{aligned}",
            "legend": "• Kawasan karst memiliki drainase permukaan yang sangat miskin karena air hujan langsung meresap ke sungai bawah tanah"
        },
        "hints": {
            "concept": "Cekungan corong pelarutan kapur di permukaan tanah tempat air masuk ke bawah tanah adalah Doline (Sinkhole). Penggabungan doline membentuk uvala dan polje.",
            "execution": "Pilih: Doline (Sinkhole)."
        }
    },
    {
        "id": "geo-lat-m-04",
        "materi": "DINAMIKA ATMOSFER & IKLIM",
        "topic": "Kalkulasi Gradien Temperatur Termis (Lapse Rate Elevasi)",
        "stem": "Sebuah stasiun BMKG di pantai utara Jawa pada ketinggian $0 \\text{ meter dpl}$ mencatat temperatur udara rata-rata sebesar $27,0^\\circ C$. Berdasarkan hukum gradien termis vertikal (Lapse Rate Braak di wilayah tropis Indonesia: setiap kenaikan ketinggian $100 \\text{ meter}$, temperatur udara rata-rata turun sebesar $0,6^\\circ C$), temperatur udara di sebuah kawasan peristirahatan pegunungan yang terletak pada elevasi $1.500 \\text{ meter dpl}$ adalah...",
        "correct": "$18,0^\\circ C$, dihitung dari formula $T = T_0 - \\left( 0,6 \\times \\frac{h}{100} \\right) = 27,0 - \\left( 0,6 \\times 15 \\right) = 27,0 - 9,0 = 18,0^\\circ C$.",
        "distractors": [
            "$21,0^\\circ C$, hasil perhitungan dengan menggunakan koefisien penurunan suhu nol koma empat derajat.",
            "$15,0^\\circ C$, hasil pengurangan suhu sebesar dua belas derajat mengikuti lapse rate udara kering.",
            "$24,0^\\circ C$, hasil estimasi penurunan suhu hanya pada puncak siang hari bolong.",
            "$12,0^\\circ C$, suhu ekstrim yang hanya terjadi saat fenomena embun upas salju Dieng."
        ],
        "formula": {
            "title": "FORMULA LAPSE RATE VERTIKAL BRAAK (INDONESIA)",
            "latex": "\\begin{aligned} T_h & = T_0 - 0,6 \\times \\left( \\frac{h}{100} \\right) \\\\ & = 27,0 - 0,6 \\times \\left( \\frac{1.500}{100} \\right) = 27,0 - (0,6 \\times 15) = 27,0 - 9,0 = \\mathbf{18,0^\\circ C} \\end{aligned}",
            "legend": "• $T_0$: Suhu pada ketinggian referensi awal ($27,0^\\circ C$ pada 0 m dpl)<br>• $h$: Ketinggian elevasi tempat tujuan dalam meter<br>• $0,6^\\circ C$: Nilai gradien temperatur vertikal rata-rata udara basah Indonesia"
        },
        "hints": {
            "concept": "T = T0 - (0,6 * h / 100). Penurunan suhu = 0,6 * (1500 / 100) = 0,6 * 15 = 9,0°C. Suhu = 27,0 - 9,0 = 18,0°C.",
            "execution": "Pilih: 18,0°C."
        }
    },
    {
        "id": "geo-lat-m-05",
        "materi": "DINAMIKA ATMOSFER & IKLIM",
        "topic": "Kalkulasi Kelembapan Relatif / Nisbah (Relative Humidity)",
        "stem": "Dalam satu meter kubik udara pada temperatur $25^\\circ C$, terkandung uap air aktual sebesar $16 \\text{ gram}$. Jika pada temperatur yang sama kapasitas uap air maksimum yang mampu ditampung udara hingga mencapai titik jenuh adalah $20 \\text{ gram/m}^3$, besarnya Kelembapan Relatif (_Relative Humidity_ / $RH$) udara tersebut adalah...",
        "correct": "$80\\%$, dihitung dari formula kelembapan relatif $RH = \\frac{\\text{Kandungan Uap Aktual}}{\\text{Kapasitas Uap Maksimum}} \\times 100\\% = \\frac{16}{20} \\times 100\\% = 80\\%$.",
        "distractors": [
            "$64\\%$, hasil perhitungan kuadrat dari rasio kelembapan absolut.",
            "$75\\%$, hasil perkalian rasio uap air dengan tekanan barometrik standar.",
            "$85\\%$, hasil koreksi kelembapan menggunakan indeks bias psikrometer sling.",
            "$90\\%$, kondisi mendekati kejenuhan yang memicu kondensasi awan kumulonimbus."
        ],
        "formula": {
            "title": "FORMULA KELEMBAPAN RELATIF / NISBAH",
            "latex": "\\begin{aligned} RH & = \\frac{e}{e_s} \\times 100\\% = \\frac{\\text{Kelembapan Mutlak (Aktual)}}{\\text{Nilai Jenuh Maksimum}} \\times 100\\% \\\\ & = \\frac{16 \\text{ g/m}^3}{20 \\text{ g/m}^3} \\times 100\\% = 0,80 \\times 100\\% = \\mathbf{80\\%} \\end{aligned}",
            "legend": "• Jika $RH = 100\\%$, udara telah mencapai titik jenuh (_Dew Point_), sehingga kelebihan uap air akan mengalami kondensasi membentuk kabut, embun, atau titik-titik awan hujan"
        },
        "hints": {
            "concept": "Kelembapan relatif RH = (Uap Aktual / Uap Maksimum) * 100% = (16 / 20) * 100% = 80%.",
            "execution": "Pilih: 80%."
        }
    },
    {
        "id": "geo-lat-m-06",
        "materi": "DINAMIKA ATMOSFER & IKLIM",
        "topic": "Penentuan Tipe Iklim Schmidt-Ferguson Berdasarkan Nilai Q",
        "stem": "Data curah hujan bulanan di suatu stasiun agroklimat selama 10 tahun terakhir mencatat rata-rata:\n- Jumlah Bulan Kering (curah hujan $< 60 \\text{ mm/bulan}$) = $3 \\text{ bulan}$\n- Jumlah Bulan Basah (curah hujan $> 100 \\text{ mm/bulan}$) = $8 \\text{ bulan}$\n- Jumlah Bulan Lembap (curah hujan $60 - 100 \\text{ mm/bulan}$) = $1 \\text{ bulan}$\nBerdasarkan klasifikasi iklim Schmidt-Ferguson, nilai rasio $Q$ dan tipe iklim stasiun tersebut adalah...",
        "correct": "$Q = 37,5\\% \\ (0,375)$, tergolong ke dalam **Tipe Iklim B (Basah)** dengan vegetasi alami hutan hujan tropis.",
        "distractors": [
            "$Q = 25,0\\%$, tergolong ke dalam Tipe Iklim A (Sangat Basah) tanpa bulan kering nyata.",
            "$Q = 60,0\\%$, tergolong ke dalam Tipe Iklim C (Agak Basah) dengan dominasi hutan musim gugur daun.",
            "$Q = 100,0\\%$, tergolong ke dalam Tipe Iklim D (Sedang) dengan pembagian musim seimbang.",
            "$Q = 133,3\\%$, tergolong ke dalam Tipe Iklim E (Agak Kering) dengan padang sabana luas."
        ],
        "formula": {
            "title": "KLASIFIKASI IKLIM SCHMIDT-FERGUSON",
            "latex": "\\begin{aligned} Q & = \\frac{\\text{Rata-rata Jumlah Bulan Kering (BK)}}{\\text{Rata-rata Jumlah Bulan Basah (BB)}} \\times 100\\% \\\\ & = \\frac{3}{8} \\times 100\\% = \\mathbf{37,5\\%} \\\\ \\text{Tipe B (Basah):} & \\quad 0,143 \\le Q < 0,333 \\text{ (Tipe A)}, \\quad \\mathbf{0,333 \\le Q < 0,600 \\implies \\text{Tipe B (Basah)}} \\end{aligned}",
            "legend": "• Kriteria Schmidt-Ferguson: Bulan Kering ($< 60$ mm), Bulan Lembap ($60 - 100$ mm), Bulan Basah ($> 100$ mm)<br>• Bulan lembap tidak diikutsertakan dalam pembagian rumus nilai $Q$"
        },
        "hints": {
            "concept": "Rumus Schmidt-Ferguson: Q = (BK / BB) * 100% = (3 / 8) * 100% = 37,5%. Rentang 33,3% <= Q < 60% adalah Tipe B (Basah).",
            "execution": "Pilih: Q = 37,5%, tergolong ke dalam Tipe Iklim B (Basah)."
        }
    },
    {
        "id": "geo-lat-m-07",
        "materi": "DINAMIKA ATMOSFER & IKLIM",
        "topic": "Dinamika Angin Muson Barat dan Terjadinya Musim Hujan di Indonesia",
        "stem": "Pada periode bulan Oktober hingga April, posisi semu tahunan matahari berada di Belahan Bumi Selatan (BBS). Perbedaan tekanan udara antara Benua Asia dan Benua Australia memicu pergerakan Angin Muson Barat. Mekanisme fisis yang menyebabkan Angin Muson Barat membawa musim hujan lebat di sebagian besar wilayah Indonesia adalah...",
        "correct": "Angin bertiup dari pusat tekanan tinggi Benua Asia menuju tekanan rendah Benua Australia, melintasi Samudra Hindia dan Laut Natuna luas sehingga menyerap uap air dalam jumlah sangat masif sebelum dibelokkan ke timur oleh Gaya Coriolis saat melintasi garis khatulistiwa.",
        "distractors": [
            "Angin bertiup dari gurun kering Benua Australia yang dingin menuju Asia sehingga tidak membawa uap air sedikit pun.",
            "Angin terperangkap di pegunungan Himalaya dan melepaskan energi panas terpendam di atas kepulauan Filipina.",
            "Gaya gravitasi bulan menyebabkan seluruh massa awan di Samudra Pasifik tersedot ke arah teluk Jakarta secara mendadak.",
            "Pemanasan global meniadakan gaya pembelokan Coriolis sehingga angin bertiup tegak lurus menembus inti bumi."
        ],
        "formula": {
            "title": "MEKANISME ANGIN MUSON DI INDONESIA",
            "latex": "\\begin{cases} \\mathbf{\\text{Muson Barat (Okt - Apr):}} & \\text{Asia Tekanan Tinggi } \\to \\text{Australia Tekanan Rendah} \\implies \\mathbf{\\text{Musim Hujan (Bawa Uap Air)}} \\\\ \\text{Muson Timur (Apr - Okt):} & \\text{Australia Tekanan Tinggi } \\to \\text{Asia Tekanan Rendah} \\implies \\text{Musim Kemarau (Kering dari Gurun)} \\end{cases}",
            "legend": "• Hukum Buys Ballot: Angin bertiup dari daerah bertekanan maksimum ke minimum; di belahan bumi utara dibelokkan ke kanan, di belahan selatan dibelokkan ke kiri oleh Gaya Coriolis"
        },
        "hints": {
            "concept": "Muson Barat bertiup dari Asia ke Australia, melintasi samudra luas membawa banyak uap air sehingga menyebabkan musim hujan di Indonesia.",
            "execution": "Pilih opsi: Bertiup dari tekanan tinggi Asia ke Australia melintasi samudra luas membawa uap air masif."
        }
    },
    {
        "id": "geo-lat-m-08",
        "materi": "DINAMIKA HIDROSFER & PERAIRAN",
        "topic": "Siklus Hidrologi: Infiltrasi, Perkolasi, dan Limpasan Permukaan (Runoff)",
        "stem": "Dalam siklus hidrologi, air hujan yang jatuh ke permukaan tanah akan mengalami berbagai proses pergerakan air. Proses pergerakan air meresap secara vertikal ke dalam lapisan pori-pori tanah teratas disebut (1), pergerakan air terus ke bawah menembus lapisan tanah yang lebih dalam hingga mengisi akuifer air tanah dalam disebut (2), dan kelebihan air yang tidak mampu meresap lalu mengalir di atas permukaan tanah menuju sungai dinamakan (3). Urutan istilah hidrologis yang tepat untuk (1), (2), dan (3) adalah...",
        "correct": "(1) Infiltrasi, (2) Perkolasi, dan (3) Limpasan Permukaan (_Surface Runoff_).",
        "distractors": [
            "(1) Perkolasi, (2) Infiltrasi, dan (3) Evapotranspirasi.",
            "(1) Kondensasi, (2) Sublimasi, dan (3) Presipitasi.",
            "(1) Transpirasi, (2) Kapilaritas, dan (3) Aliran Dasar (_Baseflow_).",
            "(1) Infiltrasi, (2) Desalinisasi, dan (3) Erosi Lembar."
        ],
        "formula": {
            "title": "TAHAPAN PERGERAKAN AIR DALAM SIKLUS HIDROLOGI",
            "latex": "\\text{Presipitasi (Hujan)} \\implies \\begin{cases} \\mathbf{\\text{Infiltrasi:}} & \\text{Air masuk menembus permukaan tanah lapisan atas} \\\\ \\mathbf{\\text{Perkolasi:}} & \\text{Air mengalir vertikal ke lapisan jenuh akuifer dalam} \\\\ \\mathbf{\\text{Runoff:}} & \\text{Air mengalir di atas permukaan (karena infiltrasi jenuh)} \\end{cases}",
            "legend": "• Deforestasi menurunkan laju infiltrasi dan melipatgandakan koefisien limpasan (runoff coefficient), memicu bencana banjir bandang"
        },
        "hints": {
            "concept": "Infiltrasi = meresap ke lapisan tanah atas. Perkolasi = meresap lebih dalam ke akuifer. Runoff = limpasan air mengalir di permukaan.",
            "execution": "Pilih: (1) Infiltrasi, (2) Perkolasi, dan (3) Limpasan Permukaan (Surface Runoff)."
        }
    },
    {
        "id": "geo-lat-m-09",
        "materi": "DINAMIKA HIDROSFER & PERAIRAN",
        "topic": "Morfologi Sungai: Meander, Cut Bank, Point Bar, dan Oxbow Lake",
        "stem": "Di daerah dataran banjir hilir sungai, aliran air sering membentuk kelokan tajam (meander). Pada sisi luar kelokan sungai terjadi arus air yang deras dan pusaran yang mengikis tebing sungai dinamakan (1), sedangkan pada sisi dalam kelokan sungai terjadi aliran tenang yang mengendapkan sedimen pasir dinamakan (2). Jika leher kelokan meander terpotong saat banjir besar, saluran kelokan lama yang terisolasi akan membentuk danau berbentuk tapal kuda yang dinamakan (3). Istilah yang benar untuk (1), (2), dan (3) adalah...",
        "correct": "(1) _Cut Bank_ (Tebing Erosi), (2) _Point Bar_ (Punggung Endapan Pasir), dan (3) _Oxbow Lake_ (Danau Tapal Kuda).",
        "distractors": [
            "(1) Delta Alluvial, (2) Kipas Alluvial, dan (3) Lembah Graben.",
            "(1) Tanggul Alam, (2) Dataran Banjir, dan (3) Palung Laut Abisal.",
            "(1) Sinkhole, (2) Stalaktit, dan (3) Danau Glasial Fjord.",
            "(1) Sand Spit, (2) Tombolo, dan (3) Laguna Karang Cincin."
        ],
        "formula": {
            "title": "EVOLUSI MEANDER DAN DANAU TAPAL KUDA (OXBOW LAKE)",
            "latex": "\\begin{aligned} \\text{Sisi Luar Kelokan (Arus Cepat):} & \\quad \\text{Erosi Horizontal Kuat} \\implies \\mathbf{\\text{Cut Bank (Tebing Terpotong)}} \\\\ \\text{Sisi Dalam Kelokan (Arus Lambat):} & \\quad \\text{Pengendapan Sedimen} \\implies \\mathbf{\\text{Point Bar (Gosong Pasir)}} \\\\ \\text{Penyempitan Leher Meander} & \\xrightarrow{\\text{Terobosan Banjir}} \\text{Saluran Lurus Baru} + \\mathbf{\\text{Oxbow Lake (Danau Tapal Kuda)}} \\end{aligned}",
            "legend": "• Pembentukan oxbow lake merupakan proses alamiah migrasi saluran sungai di dataran aluvial"
        },
        "hints": {
            "concept": "Sisi luar kelokan yang tererosi = Cut bank. Sisi dalam yang mengendap = Point bar. Danau tapal kuda yang terputus = Oxbow lake.",
            "execution": "Pilih: (1) Cut Bank, (2) Point Bar, dan (3) Oxbow Lake."
        }
    },
    {
        "id": "geo-lat-m-10",
        "materi": "DINAMIKA HIDROSFER & PERAIRAN",
        "topic": "Stratifikasi Suhu Air Laut dan Karakteristik Lapisan Termoklin",
        "stem": "Pengukuran suhu vertikal kolom air laut dari permukaan hingga kedalaman ribuan meter menunjukkan adanya lapisan transisi di mana temperatur air laut anjlok secara sangat drastis seiring bertambahnya kedalaman (misalnya turun dari $25^\\circ C$ menjadi $5^\\circ C$ pada kedalaman $200 - 1.000 \\text{ meter}$). Lapisan batas termal vertikal tersebut dinamakan...",
        "correct": "Lapisan Termoklin (_Thermocline_), yang memisahkan lapisan air hangat permukaan yang teraduk angin (_Mixed Layer_) dengan massa air laut dalam yang dingin beku dan berdensitas tinggi.",
        "distractors": [
            "Lapisan Haloklin, yaitu lapisan batas vertikal yang mengalami penurunan salinitas garam secara mendadak.",
            "Lapisan Piknoklin, yaitu lapisan batas vertikal yang mengalami penurunan massa jenis batuan dasar samudra.",
            "Zona Litoral, yaitu perairan pasang surut tempat hidup moluska dan kepiting pantai berpasir.",
            "Paparan Sahul, yaitu jembatan daratan purba yang menghubungkan benua Asia dengan kepulauan Maluku."
        ],
        "formula": {
            "title": "STRATIFIKASI VERTIKAL AIR LAUT SAMUDRA",
            "latex": "\\begin{cases} \\text{Epipelagik (Surface Layer):} & 0 - 200 \\text{ m, Hangat } (20^\\circ - 28^\\circ C), \\text{ teraduk angin} \\\\ \\mathbf{\\text{Lapisan Termoklin (Thermocline):}} & \\mathbf{200 - 1.000 \\text{ m, Penurunan Suhu Sangat Curam}} \\\\ \\text{Lapisan Laut Dalam (Deep Zone):} & > 1.000 \\text{ m, Dingin Stabil } (1^\\circ - 3^\\circ C) \\end{cases}",
            "legend": "• Termoklin permanen terdapat di perairan tropis sepanjang tahun; di perairan sedang termoklin bersifat musiman"
        },
        "hints": {
            "concept": "Lapisan air laut di mana suhu turun drastis seiring kedalaman (antara kedalaman 200 - 1000 m) adalah Lapisan Termoklin.",
            "execution": "Pilih: Lapisan Termoklin (Thermocline)."
        }
    },
    {
        "id": "geo-lat-m-11",
        "materi": "DINAMIKA LITOSFER & PEDOSFER",
        "topic": "Susunan Profil Vertikal Horizon Tanah Dewasa",
        "stem": "Profil sayatan vertikal tanah dewasa memperlihatkan lapisan-lapisan horizon tanah yang terbentuk melalui proses pelapukan dan translokasi mineral. Horizon tanah yang terletak tepat di bawah lapisan serasah organik, berwarna gelap karena kaya akan humus terdekomposisi, serta menjadi zona utama aktivitas perakaran tanaman pangan dinamakan...",
        "correct": "Horizon A (Topsoil / Lapisan Tanah Atas), yaitu horizon mineral yang mengalami pencampuran intensif dengan bahan organik humus dan menjadi zona eluviasi awal.",
        "distractors": [
            "Horizon O (Organik), yaitu lapisan paling atas yang murni terdiri atas serasah daun dan ranting yang belum terurai.",
            "Horizon B (Subsoil / Lapisan Tanah Bawah), yaitu zona akumulasi atau iluviasi liat dan oksida besi yang tercuci dari atas.",
            "Horizon C (Regolit), yaitu lapisan batuan induk yang baru mulai mengalami pelapukan mekanik awal.",
            "Horizon R (Bedrock), yaitu lapisan batuan dasar pejal keras yang belum mengalami pelapukan sedikit pun."
        ],
        "formula": {
            "title": "SUSUNAN SEKUENS HORIZON TANAH DARI ATAS KE BAWAH",
            "latex": "\\mathbf{O} \\text{ (Serasah)} \\to \\mathbf{A} \\text{ (Topsoil/Humus)} \\to \\mathbf{E} \\text{ (Eluviasi/Pucat)} \\to \\mathbf{B} \\text{ (Subsoil/Iluviasi)} \\to \\mathbf{C} \\text{ (Regolit/Batuan Lapuk)} \\to \\mathbf{R} \\text{ (Bedrock/Batuan Dasar)}",
            "legend": "• Solum Tanah Sejati meliputi gabungan Horizon A, E, dan B di mana proses pedogenesis berlangsung paling aktif"
        },
        "hints": {
            "concept": "Lapisan tanah atas berwarna gelap kaya humus tempat perakaran tanaman adalah Horizon A (Topsoil).",
            "execution": "Pilih: Horizon A (Topsoil / Lapisan Tanah Atas)."
        }
    },
    {
        "id": "geo-lat-m-12",
        "materi": "DINAMIKA LITOSFER & PEDOSFER",
        "topic": "Metode Konservasi Tanah Mekanik vs Vegetatif",
        "stem": "Pada lahan pertanian dengan kemiringan lereng curam ($15\\% - 30\\%$), erosi lembar dan erosi parit dapat dikendalikan dengan memadukan metode mekanik dan vegetatif. Tindakan konservasi tanah yang tergolong ke dalam **Metode Mekanik (Sipil Teknis)** adalah...",
        "correct": "Pembuatan terasering (sengkedan bangku), saluran pembuangan air (SPA), rorak penampung sedimen, dan pembuatan guludan tanah melintang lereng.",
        "distractors": [
            "Penanaman tanaman penutup tanah (_cover crop_), tumpang sari (_intercropping_), dan reboisasi pohon berakar tunjang.",
            "Penanaman rumput pakan ternak secara berselang-seling mengikuti garis kontur (_contour strip cropping_).",
            "Pemberian mulsa jerami padi di atas permukaan tanah untuk mengurangi energi kinetik tumbukan butir hujan.",
            "Rotasi pergiliran tanaman polong-polongan untuk mengembalikan kesuburan nitrogen tanah secara biologis."
        ],
        "formula": {
            "title": "KLASIFIKASI METODE KONSERVASI TANAH DAN AIR",
            "latex": "\\begin{cases} \\mathbf{\\text{Metode Mekanik (Sipil Teknis):}} & \\mathbf{\\text{Terasering, Guludan, Rorak, Cekdam, Tanggul Saluran (SPA)}} \\\\ \\text{Metode Vegetatif (Biologis):} & \\text{Reboisasi, Strip Cropping, Cover Crops, Mulching, Tumpang Sari} \\\\ \\text{Metode Kimiawi:} & \\text{Pemberian zat pemantap tanah (Soil Conditioner / Polimer)} \\end{cases}",
            "legend": "• Metode mekanik bertujuan memperlambat kecepatan aliran permukaan dan memberi kesempatan air meresap ke dalam tanah"
        },
        "hints": {
            "concept": "Metode mekanik/sipil teknis menggunakan rekayasa fisik tanah: terasering, guludan, rorak, saluran air (SPA). Vegetatif menggunakan tumbuhan.",
            "execution": "Pilih: Pembuatan terasering, saluran pembuangan air (SPA), rorak, dan guludan tanah."
        }
    },
    {
        "id": "geo-lat-m-13",
        "materi": "DINAMIKA BIOSFER & BIOMA",
        "topic": "Karakteristik Wilayah Fauna Neartik dan Neotropik Dunia",
        "stem": "Alfred Russel Wallace membagi wilayah persebaran fauna dunia ke dalam enam zona zoogeografi. Kawasan zoogeografi yang mencakup wilayah Amerika Tengah dan Amerika Selatan yang beriklim tropis-subtropis serta dihuni oleh fauna khas seperti trenggiling raksasa, llama, kukang (sloth), anakonda, dan piranha adalah...",
        "correct": "Zona Neotropik (Neotropical Region), yang memiliki keanekaragaman primata berekor prehensil dan reptil amfibi hutan hujan Amazon terkaya.",
        "distractors": [
            "Zona Neartik, yang mencakup Amerika Utara (AS dan Kanada) dengan fauna khas bison, serigala abu-abu, dan kalkun liar.",
            "Zona Paleartik, yang mencakup seluruh benua Eropa, Rusia, dan Asia utara dengan fauna beruang cokelat dan rusa kutub.",
            "Zona Afrotropik (Etiopian), yang mencakup benua Afrika selatan sahara dengan mamalia sabana seperti gajah afrika dan jerapah.",
            "Zona Oriental, yang mencakup Asia Selatan dan Asia Tenggara dengan harimau loreng dan gajah sumatera."
        ],
        "formula": {
            "title": "ENAM WILAYAH FAUNA DUNIA (ALFRED RUSSEL WALLACE)",
            "latex": "\\begin{array}{|l|l|l|} \\hline \\text{Zona Fauna} & \\text{Wilayah Geografis} & \\text{Fauna Karakteristik} \\\\ \\hline \\text{Paleartik} & \\text{Eropa, Rusia, Asia Utara} & \\text{Panda, Beruang Cokelat, Serigala} \\\\ \\text{Neartik} & \\text{Amerika Utara, Greenland} & \\text{Bison, Berang-berang, Kalkun} \\\\ \\mathbf{\\text{Neotropik}} & \\mathbf{\\text{Amerika Selatan \\& Tengah}} & \\mathbf{\\text{Llama, Sloth (Kukang), Anakonda, Piranha}} \\\\ \\text{Afrotropik} & \\text{Afrika Sub-Sahara, Madagaskar} & \\text{Zebra, Jerapah, Singa, Gorila} \\\\ \\text{Oriental} & \\text{Asia Selatan \\& Tenggara} & \\text{Gajah Asia, Harimau, Badak, Orangutan} \\\\ \\text{Australis} & \\text{Australia, Papua, Selandia Baru} & \\text{Kanguru, Koala, Platipus, Kiwi} \\\\ \\hline \\end{array}",
            "legend": "• Zona Neotropik sangat kaya akan fauna endemik karena isolasi geografis benua Amerika Selatan selama jutaan tahun"
        },
        "hints": {
            "concept": "Amerika Tengah dan Selatan dengan fauna llama, sloth, anakonda, dan piranha adalah Zona Neotropik. (Amerika Utara adalah Neartik).",
            "execution": "Pilih: Zona Neotropik (Neotropical Region)."
        }
    },
    {
        "id": "geo-lat-m-14",
        "materi": "DINAMIKA BIOSFER & BIOMA",
        "topic": "Komparasi Bioma Taiga (Hutan Boreal) vs Bioma Tundra",
        "stem": "Di kawasan lingkar kutub utara belahan bumi utara terdapat dua bioma daratan yang berbatasan langsung: Taiga dan Tundra. Perbedaan ekologis dan vegetasi yang paling mendasar antara Bioma Taiga dan Bioma Tundra adalah...",
        "correct": "Taiga didominasi oleh hutan pohon berdaun jarum (konifer evergreen) seperti pinus, spruce, dan cemara yang tahan beku; sedangkan Tundra merupakan padang terbuka tanpa pepohonan (_treeless_) yang hanya ditumbuhi lumut kerak (lichen) dan semak kerdil di atas tanah beku abadi (_permafrost_).",
        "distractors": [
            "Taiga tidak memiliki musim dingin sama sekali sedangkan Tundra mengalami malam kutub selama dua belas bulan penuh.",
            "Taiga merupakan bioma padang rumput beriklim kering sedangkan Tundra merupakan rawa-rawa hutan bakau air payau.",
            "Tundra ditumbuhi oleh pohon-pohon jati meranggas berukuran raksasa sedangkan Taiga murni gurun pasir bersuhu beku.",
            "Kedua bioma memiliki jenis vegetasi yang identik dan perbedaannya hanya terletak pada koordinat bujur peta dunia."
        ],
        "formula": {
            "title": "KOMPARASI BIOMA DINGIN: TAIGA VS TUNDRA",
            "latex": "\\begin{cases} \\mathbf{\\text{Bioma Taiga (Boreal Forest):}} & \\text{Ada pohon (Hutan Konifer berdaun jarum: Pinus, Cemara, Spruce)} \\\\ \\mathbf{\\text{Bioma Tundra:}} & \\mathbf{\\text{Tanpa Pohon (Treeless)}, \\text{ Tanah beku abadi (Permafrost), Lumut (Lichen)}} \\end{cases}",
            "legend": "• Batas antara Taiga dan Tundra ditandai oleh garis batas pohon (Tree Line), di mana di sebelah utaranya pohon tidak mampu lagi tumbuh"
        },
        "hints": {
            "concept": "Taiga = hutan konifer berdaun jarum tahan dingin (pinus/spruce). Tundra = padang tanpa pohon (treeless) di atas tanah beku abadi (permafrost) hanya ada lumut/lichen.",
            "execution": "Pilih: Taiga didominasi hutan konifer berdaun jarum, Tundra padang tanpa pohon dengan lumut di atas permafrost."
        }
    },
    {
        "id": "geo-lat-m-15",
        "materi": "DINAMIKA KEPENDUDUKAN (ANTROPOSFER)",
        "topic": "Kalkulasi Pertumbuhan Penduduk Alami dan Total",
        "stem": "Data kependudukan sebuah kota metropolitan pada awal tahun 2024 mencatat:\n- Total Penduduk Awal = $1.000.000$ jiwa\n- Jumlah Kelahiran Bayi ($L$) = $25.000$ jiwa\n- Jumlah Kematian ($M$) = $10.000$ jiwa\n- Jumlah Penduduk Masuk / Imigran ($I$) = $12.000$ jiwa\n- Jumlah Penduduk Keluar / Emigran ($E$) = $7.000$ jiwa\nBesarnya Pertumbuhan Penduduk Alami ($P_n$) dan Pertumbuhan Penduduk Total ($P_t$) kota tersebut selama tahun 2024 adalah...",
        "correct": "$P_n = 15.000$ jiwa (tingkat pertumbuhan alami $1,5\\%$) dan $P_t = 20.000$ jiwa (tingkat pertumbuhan total $2,0\\%$).",
        "distractors": [
            "$P_n = 25.000$ jiwa dan $P_t = 32.000$ jiwa.",
            "$P_n = 10.000$ jiwa dan $P_t = 15.000$ jiwa.",
            "$P_n = 15.000$ jiwa dan $P_t = 10.000$ jiwa.",
            "$P_n = 20.000$ jiwa dan $P_t = 25.000$ jiwa."
        ],
        "formula": {
            "title": "FORMULA PERTUMBUHAN PENDUDUK ALAMI DAN TOTAL",
            "latex": "\\begin{aligned} \\mathbf{P_n} & = L - M = 25.000 - 10.000 = \\mathbf{15.000 \\text{ jiwa}} \\implies \\%P_n = \\frac{15.000}{1.000.000} \\times 100\\% = \\mathbf{1,5\\%} \\\\ \\mathbf{P_t} & = (L - M) + (I - E) = 15.000 + (12.000 - 7.000) = 15.000 + 5.000 = \\mathbf{20.000 \\text{ jiwa}} \\\\ \\%P_t & = \\frac{20.000}{1.000.000} \\times 100\\% = \\mathbf{2,0\\%} \\end{aligned}",
            "legend": "• Pertumbuhan Alami murni memperhitungkan faktor biologis (kelahiran dan kematian)<br>• Pertumbuhan Total memperhitungkan faktor biologis ditambah migrasi neto ($I - E$)"
        },
        "hints": {
            "concept": "Pertumbuhan alami Pn = L - M = 25.000 - 10.000 = 15.000 (1,5%). Pertumbuhan total Pt = Pn + (I - E) = 15.000 + (12.000 - 7.000) = 20.000 (2,0%).",
            "execution": "Pilih: Pn = 15.000 jiwa (1,5%) dan Pt = 20.000 jiwa (2,0%)."
        }
    },
    {
        "id": "geo-lat-m-16",
        "materi": "DINAMIKA KEPENDUDUKAN (ANTROPOSFER)",
        "topic": "Empat Tahap Model Transisi Demografi (Demographic Transition Model)",
        "stem": "Dalam Model Transisi Demografi klasik, suatu negara mengalami pergeseran dari masyarakat agraris tradisional menuju masyarakat industri maju melalui 4 tahap. Karakteristik yang menandai **Tahap II (Transisi Awal / Early Expanding)** adalah...",
        "correct": "Tingkat kelahiran tetap tinggi sementara tingkat kematian turun tajam secara drastis (akibat perbaikan sanitasi, pasokan pangan, dan obat-obatan modern), sehingga memicu lonjakan pertumbuhan penduduk yang sangat cepat (_ledakan penduduk_).",
        "distractors": [
            "Tingkat kelahiran dan kematian sama-sama sangat tinggi sehingga jumlah penduduk berfluktuasi stabil di tingkat rendah (Tahap I).",
            "Tingkat kelahiran mulai menurun drastis menyusul penurunan kematian karena urbanisasi dan program KB (Tahap III).",
            "Tingkat kelahiran dan kematian sama-sama sangat rendah sehingga pertumbuhan penduduk stabil atau mendekati nol (Tahap IV).",
            "Tingkat kematian melampaui angka kelahiran sehingga jumlah penduduk mengalami penurunan populasi secara absolut (Tahap V)."
        ],
        "formula": {
            "title": "EMPAT TAHAP TRANSISI DEMOGRAFI (WARREN THOMPSON)",
            "latex": "\\begin{array}{|l|c|c|l|} \\hline \\text{Tahap} & \\text{Kelahiran (CBR)} & \\text{Kematian (CDR)} & \\text{Pertumbuhan Alami} \\\\ \\hline \\text{I. Pra-Transisi} & \\text{Tinggi} & \\text{Tinggi} & \\text{Sangat Rendah / Fluktuatif} \\\\ \\mathbf{\\text{II. Transisi Awal}} & \\mathbf{\\text{Tinggi Tetap}} & \\mathbf{\\text{Turun Cepat (Anjlok)}} & \\mathbf{\\text{Sangat Cepat (Ledakan Penduduk)}} \\\\ \\text{III. Transisi Akhir} & \\text{Turun Cepat} & \\text{Turun Lambat} & \\text{Melambat} \\\\ \\text{IV. Pasca-Transisi} & \\text{Rendah} & \\text{Rendah} & \\text{Stabil / Mendekati Nol} \\\\ \\hline \\end{array}",
            "legend": "• Sebagian besar negara berkembang di Asia dan Afrika saat ini sedang berada pada Tahap II menuju Tahap III"
        },
        "hints": {
            "concept": "Tahap II (Early Expanding) dicirikan oleh: angka kelahiran masih tinggi, tetapi angka kematian turun drastis karena medis/sanitasi, memicu ledakan penduduk.",
            "execution": "Pilih: Kelahiran tetap tinggi sementara kematian turun tajam memicu lonjakan pertumbuhan penduduk sangat cepat."
        }
    },
    {
        "id": "geo-lat-m-17",
        "materi": "PENGINDERAAN JAUH & SISTEM INFORMASI GEOGRAFIS",
        "topic": "Empat Karakteristik Resolusi Citra Satelit Penginderaan Jauh",
        "stem": "Satelit penginderaan jauh memiliki empat dimensi resolusi sensorik: spasial, spektral, radiometrik, dan temporal. Kemampuan sensor satelit untuk merekam data pada objek permukaan bumi yang sama secara berkala dalam interval waktu tertentu (misalnya Satelit Sentinel-2 merekam lokasi yang sama setiap 5 hari sekali) disebut...",
        "correct": "Resolusi Temporal, yaitu frekuensi atau interval perulangan waktu yang dibutuhkan satelit untuk kembali merekam area geografis yang sama di permukaan bumi.",
        "distractors": [
            "Resolusi Spasial, yaitu ukuran terkecil objek di permukaan bumi yang masih dapat dibedakan dan direkam oleh satu sel piksel sensor satelit.",
            "Resolusi Spektral, yaitu kemampuan sensor dalam memisahkan dan merekam rentang panjang gelombang elektromagnetik secara spesifik.",
            "Resolusi Radiometrik, yaitu kepekaan sensor dalam membedakan gradasi perbedaan kekuatan pantulan energi (tingkat kuantisasi bit warna).",
            "Resolusi Termal, yaitu kapasitas sensor dalam mendeteksi pancaran gelombang panas inframerah magma gunung api."
        ],
        "formula": {
            "title": "EMPAT RESOLUSI SENSOR PENGINDERAAN JAUH",
            "latex": "\\begin{cases} \\text{Spasial:} & \\text{Ukuran piksel terkecil di bumi (misal } 10 \\text{ m } \\times 10 \\text{ m)} \\\\ \\text{Spektral:} & \\text{Jumlah saluran band panjang gelombang (Multispektral/Hiperspektral)} \\\\ \\text{Radiometrik:} & \\text{Tingkat bit kuantisasi warna (8-bit: 256 rona, 12-bit: 4096 rona)} \\\\ \\mathbf{\\text{Temporal:}} & \\mathbf{\\text{Waktu perulangan perekaman area yang sama (Revisit Time)}} \\end{cases}",
            "legend": "• Resolusi temporal tinggi (1-2 hari) sangat krusial untuk pemantauan bencana banjir, kebakaran hutan, dan erupsi gunung api"
        },
        "hints": {
            "concept": "Resolusi yang menunjukkan interval perulangan waktu satelit merekam lokasi yang sama adalah Resolusi Temporal.",
            "execution": "Pilih: Resolusi Temporal."
        }
    },
    {
        "id": "geo-lat-m-18",
        "materi": "PENGINDERAAN JAUH & SISTEM INFORMASI GEOGRAFIS",
        "topic": "Pemanfaatan Saluran Inframerah Dekat (NIR) dan Indeks Vegetasi NDVI",
        "stem": "Dalam analisis penginderaan jauh multispektral, vegetasi hijau yang sehat dan berdaun lebat tampak sangat terang pada saluran Inframerah Dekat (_Near Infrared_ / NIR) dan tampak gelap pada saluran Merah (_Red_). Formula Indeks Vegetasi NDVI (_Normalized Difference Vegetation Index_) dan alasan fisis respon spektral tersebut adalah...",
        "correct": "$\\text{NDVI} = \\frac{\\text{NIR} - \\text{Red}}{\\text{NIR} + \\text{Red}}$, karena klorofil menyerap kuat cahaya merah untuk fotosintesis sementara struktur sel mesofil daun memantulkan radiasi inframerah dekat secara sangat kuat.",
        "distractors": [
            "$\\text{NDVI} = \\frac{\\text{Red} - \\text{NIR}}{\\text{Red} + \\text{NIR}}$, karena daun hijau memantulkan seluruh radiasi sinar tampak merah dan menyerap radiasi inframerah.",
            "$\\text{NDVI} = \\text{NIR} \\times \\text{Red}$, karena klorofil memancarkan gelombang radar yang memanaskan lapisan atmosfer.",
            "$\\text{NDVI} = \\frac{\\text{Green} - \\text{Blue}}{\\text{Green} + \\text{Blue}}$, karena indeks vegetasi hanya bergantung pada spektrum cahaya tampak mata manusia.",
            "$\\text{NDVI} = \\frac{\\text{Thermal}}{\\text{Albedo}}$, karena daun yang subur memiliki suhu permukaan yang sama dengan air es kutub."
        ],
        "formula": {
            "title": "FORMULA INDEKS VEGETASI NORMALISASI (NDVI)",
            "latex": "\\begin{aligned} \\mathbf{\\text{NDVI}} & = \\frac{\\rho_{\\text{NIR}} - \\rho_{\\text{Red}}}{\\rho_{\\text{NIR}} + \\rho_{\\text{Red}}} \\\\ \\text{Rentang Nilai:} & \\quad -1,0 \\le \\text{NDVI} \\le +1,0 \\\\ \\text{Interpretasi:} & \\quad \\begin{cases} \\text{NDVI } > 0,6: & \\text{Hutan lebat, tajuk sangat rapat, vegetasi sehat} \\\\ 0,2 \\le \\text{NDVI} \\le 0,5: & \\text{Semak belukar, pertanian, vegetasi jarang} \\\\ \\text{NDVI } < 0,1: & \\text{Tanah terbuka, batuan, pemukiman, badan air (negatif)} \\end{cases} \\end{aligned}",
            "legend": "• Saluran Red diserap pigmen klorofil ($0,66 \\ \\mu m$)<br>• Saluran NIR dipantulkan struktur dinding sel berongga daun ($0,86 \\ \\mu m$)"
        },
        "hints": {
            "concept": "Formula NDVI = (NIR - Red) / (NIR + Red). Klorofil menyerap sinar Red untuk fotosintesis dan mesofil daun memantulkan sinar NIR sangat kuat.",
            "execution": "Pilih opsi: NDVI = (NIR - Red) / (NIR + Red), karena klorofil serap merah dan mesofil pantulkan inframerah dekat."
        }
    },
    {
        "id": "geo-lat-m-19",
        "materi": "PENGINDERAAN JAUH & SISTEM INFORMASI GEOGRAFIS",
        "topic": "Analisis Spasial Tumpang Susun (Overlay) SIG untuk Penentuan Lokasi TPS",
        "stem": "Dinas Lingkungan Hidup merencanakan lokasi Tempat Pembuangan Akhir (TPA) sampah terpadu dengan menggabungkan tiga peta tematik:\n1. Peta Kemiringan Lereng (kriteria lereng $< 8\\%$)\n2. Peta Jenis Tanah (kriteria tanah lempung permeabilitas rendah)\n3. Peta Kerawanan Bencana Geologi (kriteria bebas patahan aktif)\nOperasi analisis spasial SIG yang mengekstrak perpotongan poligon yang memenuhi KETIGA kriteria tersebut secara simultan adalah...",
        "correct": "Analisis Tumpang Susun (_Overlay Intersect_), yang menggabungkan fitur-fitur spasial dan tabel atribut dari beberapa layer data sehingga hanya area irisan yang memenuhi seluruh kriteria yang akan terpilih.",
        "distractors": [
            "Analisis Penyangga (_Buffering_), yaitu pembuatan zona radius batas jangkauan melingkar di sekitar titik fasilitas umum.",
            "Analisis Jaringan (_Network Analysis_), yaitu penentuan rute jalan terpendek untuk armada truk pengangkut logistik.",
            "Analisis Klasifikasi Ulang (_Reclassify_), yaitu pengubahan nilai piksel citra satelit mentah menjadi data tabel Excel.",
            "Analisis Interpolasi Kriging, yaitu penaksiran nilai curah hujan di titik yang tidak memiliki stasiun pengukur hujan."
        ],
        "formula": {
            "title": "OPERASI SPASIAL SIG MULTI-LAYER (OVERLAY INTERSECT)",
            "latex": "\\text{Layer 1 } (\\text{Lereng}) \\cap \\text{Layer 2 } (\\text{Tanah}) \\cap \\text{Layer 3 } (\\text{Geologi}) \\implies \\mathbf{\\text{Kawasan Layak TPA (Irisan Poligon)} \\equiv \\text{Overlay Intersect}}",
            "legend": "• Intersect: Mengambil irisan bersama (Logika boolean AND)<br>• Union: Menggabungkan seluruh area poligon (Logika boolean OR)<br>• Erase: Menghapus area poligon tertentu"
        },
        "hints": {
            "concept": "Menggabungkan beberapa layer peta untuk mencari irisan area yang memenuhi seluruh kriteria adalah analisis Overlay Intersect.",
            "execution": "Pilih: Analisis Tumpang Susun (Overlay Intersect)."
        }
    },
    {
        "id": "geo-lat-m-20",
        "materi": "PENGINDERAAN JAUH & SISTEM INFORMASI GEOGRAFIS",
        "topic": "Analisis Penyangga (Buffering) untuk Penetapan Sempadan Sungai",
        "stem": "Berdasarkan Peraturan Pemerintah Nomor 38 Tahun 2011 tentang Sungai, kawasan sempadan sungai bertanggul di dalam kawasan perkotaan ditetapkan memiliki garis sempadan minimal $3 \\text{ meter}$ dari tepi luar kaki tanggul, sedangkan sungai tidak bertanggul di luar perkotaan berkedalaman lebih dari 20 meter memiliki sempadan selebar $30 \\text{ meter}$. Dalam perangkat lunak SIG, pembentukan zona proteksi sempadan di sepanjang kiri dan kanan fitur garis sungai tersebut diproses menggunakan fungsi...",
        "correct": "Fungsi Buffer (_Buffering_), yaitu pembentukan zona sabuk wilayah penyangga dengan radius jarak tertentu di sekeliling objek titik, garis, atau poligon.",
        "distractors": [
            "Fungsi Dissolve, yaitu penggabungan poligon-poligon bertetangga yang memiliki nilai atribut sama menjadi satu poligon besar.",
            "Fungsi Clip, yaitu pemotongan layer data peta spasial menggunakan poligon batas administratif daerah lain.",
            "Fungsi Merge, yaitu penggabungan dua tabel basis data relasional yang memiliki primary key berbeda.",
            "Fungsi Digitasi, yaitu proses penggambaran manual garis batas peta analog menjadi format vektor digital."
        ],
        "formula": {
            "title": "FUNGSI BUFFERING DATA VEKTOR SIG",
            "latex": "\\text{Fitur Garis Sungai} \\xrightarrow{\\text{Buffer Distance } d = 30 \\text{ m}} \\mathbf{\\text{Zona Sempadan (Poligon Sabuk Kiri-Kanan Lebar } 2d = 60 \\text{ m)}}",
            "legend": "• Aplikasi Buffering: Zona sempadan sungai, zona bahaya sempadan sesar gempa (50 m), zona bebas kebisingan bandara, dan area jangkauan menara BTS"
        },
        "hints": {
            "concept": "Pembuatan zona sabuk penyangga dengan jarak radius tertentu di sekeliling garis sungai adalah fungsi Buffering.",
            "execution": "Pilih: Fungsi Buffer (Buffering)."
        }
    },
    {
        "id": "geo-lat-m-21",
        "materi": "DASAR-DASAR PERPETAN & PEMETAAN",
        "topic": "Kalkulasi Kemiringan Lereng dari Peta Topografi Kontur",
        "stem": "Pada sebuah peta topografi berskala $1 : 25.000$, jarak antara titik $A$ dan titik $B$ diukur pada peta adalah $4 \\text{ cm}$. Titik $A$ berada pada garis kontur $200 \\text{ meter dpl}$ dan titik $B$ berada pada garis kontur $300 \\text{ meter dpl}$. Persentase kemiringan lereng (_Slope Gradient_) antara titik $A$ dan titik $B$ di lapangan adalah...",
        "correct": "$10\\%$, dihitung dari rasio beda tinggi terhadap jarak mendatar sebenarnya di lapangan: $\\frac{300 - 200}{4 \\times 250} \\times 100\\% = \\frac{100}{1.000} \\times 100\\% = 10\\%$.",
        "distractors": [
            "$25\\%$, hasil perkalian beda tinggi dengan angka penyebut skala peta per seratus.",
            "$4\\%$, hasil pembagian jarak peta dengan beda tinggi antar kedua garis kontur.",
            "$40\\%$, hasil perhitungan tanpa mengalikan jarak peta dengan skala sebenarnya.",
            "$2,5\\%$, kemiringan lereng landai dataran pantai alluvial."
        ],
        "formula": {
            "title": "FORMULA KEMIRINGAN LERENG DARI PETA TOPOGRAFI",
            "latex": "\\begin{aligned} \\text{Beda Tinggi } (\\Delta h) & = 300 - 200 = 100 \\text{ meter} \\\\ \\text{Jarak Riil di Lapangan } (d) & = 4 \\text{ cm} \\times 25.000 = 100.000 \\text{ cm} = \\mathbf{1.000 \\text{ meter}} \\\\ \\mathbf{\\%\\text{Kemiringan Lereng}} & = \\frac{\\Delta h}{d} \\times 100\\% = \\frac{100 \\text{ m}}{1.000 \\text{ m}} \\times 100\\% = \\mathbf{10\\%} \\end{aligned}",
            "legend": "• Klasifikasi Kemiringan Lereng (Bappenas): Datar (0-8%), Landai (8-15%), Agak Curam (15-25%), Curam (25-45%), Sangat Curam (> 45%)"
        },
        "hints": {
            "concept": "Beda tinggi Delta h = 300 - 200 = 100 m. Jarak riil = 4 cm x 25.000 = 100.000 cm = 1.000 m. %Lereng = (100 / 1.000) * 100% = 10%.",
            "execution": "Pilih: 10%."
        }
    },
    {
        "id": "geo-lat-m-22",
        "materi": "TATA RUANG & INTERAKSI SPASIAL",
        "topic": "Penentuan Lokasi Fasilitas Ideal dengan Teori Titik Henti Carrothers",
        "stem": "Pemerintah kabupaten akan membangun sebuah Rumah Sakit Umum Daerah (RSUD) rujukan untuk melayani dua kota:\n- Kota Melati berpenduduk $P_A = 40.000$ jiwa\n- Kota Kenanga berpenduduk $P_B = 10.000$ jiwa\nJarak antara Kota Melati dan Kota Kenanga adalah $d_{AB} = 30 \\text{ km}$. Berdasarkan Teori Titik Henti (_Breaking Point Theory_ dari William J. Reilly dan William J. Carrothers), lokasi paling ideal untuk mendirikan RSUD tersebut adalah...",
        "correct": "$10 \\text{ km}$ dari Kota Kenanga (atau $20 \\text{ km}$ dari Kota Melati), yaitu lebih dekat ke arah kota yang jumlah penduduknya lebih sedikit.",
        "distractors": [
            "$15 \\text{ km}$ tepat di tengah-tengah jarak antar kedua kota tanpa mempertimbangkan bobot populasi.",
            "$10 \\text{ km}$ dari Kota Melati, sehingga warga kota besar mendapatkan akses yang jauh lebih dekat.",
            "$5 \\text{ km}$ dari Kota Kenanga, hasil pembagian rasio kuadrat akar populasi murni.",
            "$25 \\text{ km}$ dari Kota Kenanga, tepat berada di pinggiran perbatasan Kota Melati."
        ],
        "formula": {
            "title": "FORMULA TEORI TITIK HENTI (BREAKING POINT THEORY)",
            "latex": "\\begin{aligned} D_{AB} & = \\frac{d_{AB}}{1 + \\sqrt{\\frac{P_{\\text{besar}}}{P_{\\text{kecil}}}}} \\quad (\\text{Diukur dari kota berpenduduk lebih KECIL}) \\\\ & = \\frac{30}{1 + \\sqrt{\\frac{40.000}{10.000}}} = \\frac{30}{1 + \\sqrt{4}} = \\frac{30}{1 + 2} = \\frac{30}{3} = \\mathbf{10 \\text{ km dari Kota Kenanga}} \\end{aligned}",
            "legend": "• Prinsip Titik Henti: Fasilitas layanan diletakkan lebih dekat ke kota kecil agar daya tarik gravitasi kota besar yang kuat terimbangi oleh kedekatan jarak kota kecil"
        },
        "hints": {
            "concept": "Titik Henti D_AB = d / (1 + sqrt(P_besar / P_kecil)) diukur dari kota berpenduduk lebih KECIL. D = 30 / (1 + sqrt(40.000/10.000)) = 30 / (1 + 2) = 10 km dari Kenanga.",
            "execution": "Pilih: 10 km dari Kota Kenanga (atau 20 km dari Kota Melati)."
        }
    },
    {
        "id": "geo-lat-m-23",
        "materi": "TATA RUANG & INTERAKSI SPASIAL",
        "topic": "Teori Tempat Sentral Walter Christaller: Hierarki K=3 Asas Pasar",
        "stem": "Dalam Teori Tempat Sentral (_Central Place Theory_) yang dikemukakan oleh Walter Christaller dengan heksagonal ruang geometris, Tempat Sentral Berhierarki Tiga ($K = 3$) mencerminkan asas...",
        "correct": "Asas Pasar Optimum (_Marketing Principle_), di mana pusat pelayanan melayani seluruh wilayah kota inti ditambah sepertiga ($1/3$) bagian dari wilayah heksagonal tetangga di sekelilingnya.",
        "distractors": [
            "Asas Transportasi Optimum ($K = 4$), di mana pusat pelayanan melayani setengah ($1/2$) dari wilayah heksagonal tetangga di sepanjang jalur jalan.",
            "Asas Administrasi Pemerintahan ($K = 7$), di mana pusat pelayanan mengendalikan secara mutlak seluruh ($100\\%$) wilayah administratif tetangga.",
            "Asas Pertanian Monokultur ($K = 1$), di mana tidak ada interaksi spasial yang melintasi batas heksagonal tertutup.",
            "Asas Kawasan Industri Terpadu ($K = 12$), di mana kota inti membagi pangsa pasarnya kepada dua belas kota satelit."
        ],
        "formula": {
            "title": "TIGA HIERARKI TEMPAT SENTRAL WALTER CHRISTALLER",
            "latex": "\\begin{cases} \\mathbf{K = 3:} & \\mathbf{\\text{Asas Pasar Optimum } (1 + 6 \\times 1/3 = 3) \\implies \\text{Penyediaan barang konsumsi harian}} \\\\ \\mathbf{K = 4:} & \\mathbf{\\text{Asas Transportasi Optimum } (1 + 6 \\times 1/2 = 4) \\implies \\text{Lalu lintas jalan raya terpadu}} \\\\ \\mathbf{K = 7:} & \\mathbf{\\text{Asas Administratif Optimum } (1 + 6 \\times 1 = 7) \\implies \\text{Pemerintahan \\& keamanan}} \\end{cases}",
            "legend": "• Threshold: Jumlah minimal penduduk yang dibutuhkan untuk kelangsungan hidup suatu unit pelayanan<br>• Range: Jarak maksimal yang bersedia ditempuh konsumen untuk mendapatkan barang/jasa"
        },
        "hints": {
            "concept": "K = 3 adalah Asas Pasar Optimum (1 kota inti + 6 x 1/3 tetangga = 3). K = 4 adalah Asas Transportasi. K = 7 adalah Asas Administratif.",
            "execution": "Pilih: Asas Pasar Optimum (Marketing Principle), melayani wilayah sendiri + sepertiga wilayah tetangga."
        }
    },
    {
        "id": "geo-lat-m-24",
        "materi": "MITIGASI BENCANA ALAM & ADAPTASI",
        "topic": "Sistem Peringatan Dini Tsunami (InaTEWS) Berbasis Multi-Sensor",
        "stem": "Badan Meteorologi, Klimatologi, dan Geofisika (BMKG) mengoperasikan Sistem Peringatan Dini Tsunami Indonesia (_Indonesia Tsunami Early Warning System_ / InaTEWS). Komponen sensor bawah laut yang mendeteksi perubahan anomali tekanan air laut secara langsung di dasar samudra saat gelombang tsunami melintas di lepas pantai adalah...",
        "correct": "_Ocean Bottom Pressure Recorder_ (OBPR) yang terhubung dengan pelampung tsunami (_Tsunami Buoy_) di permukaan laut dan kabel serat optik bawah laut (_Cable Based Tomography_).",
        "distractors": [
            "Stasiun Pasang Surut (_Tide Gauge_), yang hanya dipasang menempel di dermaga pelabuhan pantai untuk mengukur pasang surut.",
            "Seismometer akselerograf darat, yang merekam getaran gelombang primer dan sekunder di puncak bukit batuan beku.",
            "Radar cuaca Doppler pita C, yang mendeteksi curah hujan lebat dan pergerakan pusaran awan badai di troposfer.",
            "Peralatan GPS genggam yang dibawa oleh regu penyelamat bencana SAR di daratan."
        ],
        "formula": {
            "title": "ARSITEKTUR MULTI-SENSOR INATEWS (BMKG)",
            "latex": "\\text{Gempa Bawah Laut} \\implies \\begin{cases} \\text{Seismograf (Daratan):} & \\text{Deteksi Parameter Gempa (M > 7,0, Kedalaman < 60 km) dalam 3-5 Menit} \\\\ \\mathbf{\\text{OBPR / Buoy / Ina-CBT:}} & \\mathbf{\\text{Verifikasi Riil Gelombang Tsunami di Lepas Pantai Samudra}} \\\\ \\text{Tide Gauge (Pesisir):} & \\text{Konfirmasi Kenaikan Muka Air Laut di Garis Pantai} \\end{cases}",
            "legend": "• Informasi 'Waspada' (< 0,5 m), 'Siaga' (0,5 - 3 m), dan 'Awas' (> 3 m) disiarkan langsung ke masyarakat dalam waktu kurang dari 5 menit"
        },
        "hints": {
            "concept": "Sensor tekanan air laut di dasar samudra yang mendeteksi tsunami sebelum sampai ke pantai adalah OBPR (Ocean Bottom Pressure Recorder) yang terhubung ke Buoy/kabel laut.",
            "execution": "Pilih: Ocean Bottom Pressure Recorder (OBPR) yang terhubung dengan Tsunami Buoy."
        }
    },
    {
        "id": "geo-lat-m-25",
        "materi": "LINGKUNGAN HIDUP & PEMBANGUNAN BERKELANJUTAN",
        "topic": "Penyusunan Dokumen Analisis Mengenai Dampak Lingkungan (AMDAL)",
        "stem": "Setiap rencana usaha atau kegiatan pembangunan yang diperkirakan berpotensi menimbulkan dampak penting terhadap lingkungan hidup (seperti pembangunan pelabuhan peti kemas, jalan tol antarkota, dan pabrik semen) wajib dilengkapi dengan dokumen Analisis Mengenai Dampak Lingkungan Hidup (AMDAL) menurut PP No. 22 Tahun 2021. Komponen dokumen AMDAL yang memuat rencana terinci mengenai upaya pengelolaan teknis untuk mencegah, mengendalikan, dan menanggulangi dampak negatif lingkungan adalah...",
        "correct": "Rencana Pengelolaan Lingkungan Hidup (RKL), yang disusun bersama dengan Rencana Pemantauan Lingkungan Hidup (RPL) berdasarkan temuan dokumen ANDAL.",
        "distractors": [
            "Kerangka Acuan (KA-ANDAL), yang merupakan ruang lingkup kajian pelingkupan dampak penting sebelum penelitian lapangan.",
            "Analisis Dampak Lingkungan Hidup (ANDAL), yang berisi telaah cermat dan mendalam mengenai besaran dan sifat penting dampak.",
            "Surat Pernyataan Kesanggupan Pengelolaan dan Pemantauan Lingkungan Hidup (SPPL), yang hanya untuk usaha mikro tanpa dampak penting.",
            "Dokumen Izin Mendirikan Bangunan (IMB), yang mengatur ketinggian genteng dan saluran pembuangan air hujan perumahan."
        ],
        "formula": {
            "title": "EMPAT DOKUMEN DALAM SISTEM AMDAL",
            "latex": "\\text{Proses AMDAL} \\implies \\begin{cases} \\text{1. KA (Kerangka Acuan):} & \\text{Pelingkupan isu prioritas studi} \\\\ \\text{2. ANDAL:} & \\text{Analisis dampak penting mendalam (Fisik, Kimia, Hayati, Sosial)} \\\\ \\mathbf{\\text{3. RKL:}} & \\mathbf{\\text{Rencana Pengelolaan Lingkungan (Tindakan Mitigasi/Pencegahan)}} \\\\ \\text{4. RPL:} & \\text{Rencana Pemantauan Lingkungan (Monitoring berkala dampak)} \\end{cases}",
            "legend": "• Dokumen RKL dan RPL menjadi dasar hukum penerbitan Persetujuan Lingkungan dan Izin Usaha Komersial"
        },
        "hints": {
            "concept": "Dokumen AMDAL yang memuat upaya teknis mengelola dan menanggulangi dampak negatif adalah RKL (Rencana Pengelolaan Lingkungan Hidup). Pemantauan berkala adalah RPL.",
            "execution": "Pilih: Rencana Pengelolaan Lingkungan Hidup (RKL)."
        }
    }
]
