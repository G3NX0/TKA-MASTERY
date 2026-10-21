# -*- coding: utf-8 -*-
"""
geografi_data_simulasi.py
-------------------------
35 Authentic HOTS Simulation Questions for TKA 2026 Geografi (SMA/MA Soshum).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: geo-sim-01 .. geo-sim-35
Breakdown:
- 25 Single MCQ HOTS (geo-sim-01 .. geo-sim-25)
- 5 Multi-select HOTS (geo-sim-26 .. geo-sim-30)
- 5 Matrix Benar-Salah HOTS (geo-sim-31 .. geo-sim-35)
"""

GEOGRAFI_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 SINGLE MCQ HOTS (geo-sim-01 to geo-sim-25)
    # -------------------------------------------------------------
    {
        "id": "geo-sim-01",
        "materi": "PENGINDERAAN JAUH & FOTOGRAMETRI",
        "topic": "Penentuan Skala Foto Udara Menggunakan Panjang Fokus dan Tinggi Terbang",
        "stem": "Pesawat pemotretan udara memotret wilayah dataran tinggi dengan data teknis berikut:\n- Panjang fokus lensa kamera ($f$): $152 \\text{ mm}$ ($0{,}152 \\text{ meter}$)\n- Ketinggian terbang pesawat di atas permukaan air laut ($H$): $3.500 \\text{ meter}$ dpl\n- Rata-rata ketinggian permukaan tanah medan yang dipotret ($h$): $500 \\text{ meter}$ dpl\nBesarnya skala foto udara vertikal yang dihasilkan ($S$) adalah...",
        "correct": "$1 : 19.737$ (dibulatkan menjadi $1 : 20.000$).",
        "distractors": [
            "$1 : 23.026$ (mengabaikan ketinggian medan $h$).",
            "$1 : 10.000$.",
            "$1 : 50.000$.",
            "$1 : 5.000$."
        ],
        "formula": {
            "title": "FORMULA SKALA FOTO UDARA VERTIKAL",
            "latex": "\\begin{aligned} S & = \\frac{f}{H - h} = \\frac{0{,}152 \\text{ m}}{3.500 \\text{ m} - 500 \\text{ m}} = \\frac{0{,}152}{3.000} = \\frac{1}{\\frac{3.000}{0{,}152}} \\\\ & = \\frac{1}{19.736{,}8} \\approx \\mathbf{1 : 20.000} \\end{aligned}",
            "legend": "• $f$: Panjang fokus lensa kamera fotogrametri<br>• $H$: Tinggi terbang wahana dari permukaan laut<br>• $h$: Ketinggian rata-rata objek medan dari permukaan laut"
        },
        "hints": {
            "concept": "Rumus skala foto udara: S = f / (H - h). H - h = 3.500 m - 500 m = 3.000 m. Skala = 0,152 m / 3.000 m = 1 : (3.000 / 0,152) = 1 : 19.737 (sekitar 1 : 20.000).",
            "execution": "Hitung: 1 : 19.737 atau dibulatkan 1 : 20.000."
        }
    },
    {
        "id": "geo-sim-02",
        "materi": "DINAMIKA KEPENDUDUKAN & KETENAGAKERJAAN",
        "topic": "Proyeksi Pertumbuhan Penduduk Model Geometris",
        "stem": "Jumlah penduduk Kota Satelit pada tahun 2020 tercatat sebanyak $P_0 = 500.000 \\text{ jiwa}$. Laju pertumbuhan penduduk geometris rata-rata per tahun adalah $r = 2\\%$ ($0{,}02$). Berapakah perkiraan jumlah penduduk kota tersebut pada tahun 2030 ($t = 10 \\text{ tahun}$) dengan asumsi laju pertumbuhan konstan? (Gunakan nilai aproksimasi $1{,}02^{10} \\approx 1{,}219$)",
        "correct": "$609.500 \\text{ jiwa}$.",
        "distractors": [
            "$600.000 \\text{ jiwa}$ (proyeksi linier aritmatika sederhana).",
            "$550.000 \\text{ jiwa}$.",
            "$725.000 \\text{ jiwa}$.",
            "$800.000 \\text{ jiwa}$."
        ],
        "formula": {
            "title": "FORMULA PROYEKSI PENDUDUK GEOMETRIS",
            "latex": "\\begin{aligned} P_t & = P_0 \\cdot (1 + r)^t = 500.000 \\times (1 + 0{,}02)^{10} \\\\ & = 500.000 \\times 1{,}02^{10} = 500.000 \\times 1{,}219 = \\mathbf{609.500 \\text{ jiwa}} \\end{aligned}",
            "legend": "• $P_t$: Jumlah penduduk setelah $t$ tahun<br>• $P_0$: Jumlah penduduk tahun dasar<br>• $r$: Laju pertumbuhan penduduk per tahun<br>• $t$: Rentang waktu proyeksi (2030 - 2020 = 10 tahun)"
        },
        "hints": {
            "concept": "Proyeksi geometris: Pt = P0 * (1 + r)^t = 500.000 * (1,02)^10. Dengan (1,02)^10 = 1,219, hitung 500.000 * 1,219.",
            "execution": "500.000 * 1,219 = 609.500 jiwa."
        }
    },
    {
        "id": "geo-sim-03",
        "materi": "POLA KERUANGAN DESA & KOTA",
        "topic": "Analisis Pola Sebaran Permukiman Menggunakan Indeks Tetangga Terdekat (Nearest Neighbor Analysis)",
        "stem": "Dalam analisis spasial kuantitatif pola persebaran permukiman pedesaan di dataran aluvial pantai, nilai Indeks Tetangga Terdekat (_Nearest Neighbor Index_ / $T$) diperoleh sebesar $T = 0{,}15$. Pola sebaran permukiman desa tersebut serta faktor fisik penentunya adalah...",
        "correct": "Pola mengelompok (_clustered_), di mana permukiman terkonsentrasi rapat di sekitar sumber air tawar bersih atau tanggul alam sungai bebas genangan pasang rob laut ($T \\to 0$).",
        "distractors": [
            "Pola acak (_random_), di mana permukiman tersebar bebas di seluruh penjuru dataran tanpa adanya gaya gravitasi fisik yang dominan ($T = 1{,}0$).",
            "Pola seragam teratur (_regular / dispersed_), di mana rumah-rumah berjarak sama persis membentuk pola heksagonal terencana ($T = 2{,}15$).",
            "Pola linear memanjang pantai, yang ditandai oleh nilai indeks tetangga terdekat mendekati nilai maksimum $T > 2{,}0$.",
            "Pola radial melingkar, yang hanya terbentuk di kawasan puncak kepundan gunung berapi aktif."
        ],
        "formula": {
            "title": "RENTANG NILAI INDEKS TETANGGA TERDEKAT (NEAREST NEIGHBOR)",
            "latex": "\\begin{cases} T = 0 & \\implies \\mathbf{\\text{Mengelompok Sempurna (Clustered)}} \\\\ 0 < T < 1 & \\implies \\mathbf{\\text{Cenderung Mengelompok (T = 0{,}15)}} \\\\ T = 1{,}0 & \\implies \\text{Pola Acak (Random)} \\\\ 1{,}0 < T < 2{,}15 & \\implies \\text{Cenderung Teratur / Menyebar} \\\\ T = 2{,}15 & \\implies \\text{Pola Teratur Sempurna / Heksagonal (Dispersed)} \\end{cases}",
            "legend": "• $T = \\frac{\\bar{r}_o}{\\bar{r}_e}$ (Rasio jarak rata-rata teramati terhadap jarak rata-rata harapan acak)"
        },
        "hints": {
            "concept": "Indeks Tetangga Terdekat (Clark & Evans): Nilai T berkisar antara 0 (mengelompok sempurna), 1 (acak), hingga 2,15 (seragam/teratur). Nilai T = 0,15 berarti pola mengelompok (clustered).",
            "execution": "Pilih: Pola mengelompok (clustered), terkonsentrasi di sekitar sumber air tawar."
        }
    },
    {
        "id": "geo-sim-04",
        "materi": "DINAMIKA ATMOSFER & CUACA",
        "topic": "Kalkulasi Kelembapan Relatif dan Defisit Tekanan Uap Air",
        "stem": "Pada suhu udara $25^\\circ \\text{C}$, udara dalam satu meter kubik ruang terbuka memiliki kapasitas maksimum menampung uap air jenuh sebesar $24 \\text{ gram/m}^3$. Hasil pengukuran higrometer digital di stasiun BMKG menunjukkan kandungan uap air aktual di udara tersebut adalah sebesar $18 \\text{ gram/m}^3$. Besarnya kelembapan relatif (relatif humidity) udara tersebut adalah...",
        "correct": "$75\\%$.",
        "distractors": [
            "$60\\%$.",
            "$80\\%$.",
            "$68\\%$.",
            "$90\\%$."
        ],
        "formula": {
            "title": "FORMULA KELEMBAPAN RELATIF (RELATIVE HUMIDITY)",
            "latex": "\\begin{aligned} RH & = \\frac{\\text{Kandungan Uap Air Aktual (Kelembapan Mutlak)}}{\\text{Kapasitas Uap Air Maksimum (Kelembapan Jenuh)}} \\times 100\\% \\\\ & = \\frac{18 \\text{ g/m}^3}{24 \\text{ g/m}^3} \\times 100\\% = \\frac{3}{4} \\times 100\\% = \\mathbf{75\\%} \\end{aligned}",
            "legend": "• Jika udara didinginkan hingga mencapai titik embun (_dew point_), kapasitas maksimum turun menjadi 18 g/m³ sehingga $RH$ menjadi 100% dan terjadi kondensasi kabut/awan"
        },
        "hints": {
            "concept": "Kelembapan relatif RH = (Uap air aktual / Uap air maksimum) * 100% = (18 / 24) * 100% = 0,75 * 100% = 75%.",
            "execution": "Hitung: 18 / 24 * 100% = 75%."
        }
    },
    {
        "id": "geo-sim-05",
        "materi": "POLA KERUANGAN & PERTUMBUHAN WILAYAH",
        "topic": "Model Gravitasi Carey Modifikasi: Interaksi Spasial Dua Wilayah",
        "stem": "Dua kota di koridor ekonomi regional memiliki data sebagai berikut:\n- Jumlah penduduk Kota A ($P_A$): $40.000 \\text{ jiwa}$\n- Jumlah penduduk Kota B ($P_B$): $10.000 \\text{ jiwa}$\n- Jarak mutlak antarkota ($d_{AB}$): $20 \\text{ km}$\nDengan konstanta interaksi spasial $k = 1$, besarnya kekuatan interaksi gravitasi antara Kota A dan Kota B ($I_{AB}$) menurut rumus W.J. Reilly adalah...",
        "correct": "$1.000.000$.",
        "distractors": [
            "$2.000.000$.",
            "$500.000$.",
            "$20.000.000$.",
            "$400.000$."
        ],
        "formula": {
            "title": "FORMULA GRAVITASI REILLY",
            "latex": "\\begin{aligned} I_{AB} & = k \\cdot \\frac{P_A \\cdot P_B}{(d_{AB})^2} = 1 \\times \\frac{40.000 \\times 10.000}{20^2} \\\\ & = \\frac{400.000.000}{400} = \\mathbf{1.000.000} \\end{aligned}",
            "legend": "• $P_A, P_B$: Jumlah penduduk masing-masing kota<br>• $d_{AB}$: Jarak antara kedua kota (dikuadratkan)"
        },
        "hints": {
            "concept": "Rumus gravitasi Reilly: I = (PA * PB) / d^2. Hitung: (40.000 * 10.000) / 20^2 = 400.000.000 / 400 = 1.000.000.",
            "execution": "Pilih: 1.000.000."
        }
    },
    {
        "id": "geo-sim-06",
        "materi": "DINAMIKA LITOSFER & VULKANISME",
        "topic": "Karakteristik Letusan Tipe Plinian dan Indeks Eksplosivitas Vulkanik (VEI)",
        "stem": "Letusan Gunung Tambora pada tahun 1815 dan Krakatau pada tahun 1883 dikategorikan sebagai letusan bertipe Plinian hingga Ultra-Plinian dengan Indeks Eksplosivitas Vulkanik ($VEI \\ge 6$). Karakteristik fisik magma dan dinamika erupsi tipe Plinian tersebut adalah...",
        "correct": "Magma asam bersifat riolitik-dasitik dengan viskositas (kekentalan) dan kandungan silika ($SiO_2 > 65\\%$) serta gas terlarut sangat tinggi, yang meledak dahsyat melontarkan kolom abu tefra hingga menembus lapisan stratosfer (> 30 km) dan membentuk kaldera runtuhan.",
        "distractors": [
            "Magma basa encer berkomposisi basaltik dengan gas rendah yang mengalir tenang membentuk lelehan lava pijar tanpa ledakan debu.",
            "Magma intermediet yang hanya menghasilkan semburan lava pijar kecil setinggi puluhan meter seperti kembang api berkala.",
            "Letusan yang dipicu oleh uap air hidrotermal dangkal tanpa adanya material magma segar yang keluar dari perut bumi.",
            "Erupsi efusif rekahan linier yang membentuk dataran tinggi basal plateau seluas ribuan kilometer persegi."
        ],
        "formula": {
            "title": "PARAMETER LETUSAN TIPE PLINIAN (VEI TINGGI)",
            "latex": "\\text{Magma Riolitik/Dasitik} \\implies \\begin{cases} \\text{Kandungan Silika } (SiO_2 > 65\\%) \\\\ \\text{Viskositas Sangat Tinggi (Sangat Kental)} \\\\ \\text{Tekanan Gas Sangat Kuat} \\end{cases} \\implies \\mathbf{\\text{Erupsi Eksplosif Kataklisma (VEI 6 - 8)}}",
            "legend": "• Menghasilkan awan piroklastik kolosal, hujan abu tefra global, dan pendinginan suhu iklim bumi (_Year Without a Summer_)"
        },
        "hints": {
            "concept": "Tipe Plinian: Magma asam kental (silika tinggi >65%), gas bertekanan luar biasa, ledakan kataklisma membentuk kolom abu tembus stratosfer dan kaldera runtuhan.",
            "execution": "Pilih opsi: Magma asam riolitik-dasitik kental, silika dan gas sangat tinggi, melontarkan kolom abu tembus stratosfer dan membentuk kaldera."
        }
    },
    {
        "id": "geo-sim-07",
        "materi": "DINAMIKA HIDROSFER & OSEANOGRAFI",
        "topic": "Dinamika Pasang Surut Laut: Pasang Purnama (Spring Tide) vs Pasang Perbani (Neap Tide)",
        "stem": "Fenomena pasang surut air laut dipengaruhi oleh kombinasi gaya tarik gravitasi bulan dan matahari serta gaya sentrifugal rotasi bumi. Peristiwa Pasang Purnama (_Spring Tide_), di mana amplitudo pasang mencapai titik tertinggi dan surut mencapai titik terendah secara maksimal, terjadi pada saat...",
        "correct": "Posisi Matahari, Bulan, dan Bumi berada pada satu garis lurus simetris (_syzygy_), yang terjadi pada fase Bulan Baru (Tilem) dan fase Bulan Purnama.",
        "distractors": [
            "Posisi Bulan dan Matahari membentuk sudut siku-siku $90^\\circ$ terhadap Bumi pada fase kuartir pertama dan kuartir ketiga.",
            "Bumi berada pada titik terjauh dari matahari (aphelion) di puncak musim dingin belahan bumi utara.",
            "Bulan mengalami gerhana total tepat saat terjadi badai siklon tropis di samudra Hindia selatan.",
            "Gaya gravitasi matahari saling meniadakan secara sempurna dengan gaya gravitasi bulan setiap akhir pekan."
        ],
        "formula": {
            "title": "KONFIGURASI ORBIT PASANG PURNAMA VS PASANG PERBANI",
            "latex": "\\begin{cases} \\mathbf{\\text{Spring Tide (Pasang Purnama):}} & \\text{Posisi Sejajar (Syzygy): Matahari - Bulan - Bumi (Sudut } 0^\\circ / 180^\\circ) \\implies \\mathbf{\\text{Gaya Gravitasi Saling Memperkuat}} \\\\ \\mathbf{\\text{Neap Tide (Pasang Perbani):}} & \\text{Posisi Kuadratur (Sudut } 90^\\circ) \\implies \\text{Gaya Saling Mengurangi (Pasang Terkecil)} \\end{cases}",
            "legend": "• Pasang Purnama terjadi 2 kali setiap bulan kamariah (bulan sinodis)"
        },
        "hints": {
            "concept": "Spring tide (pasang purnama) terjadi saat matahari, bulan, dan bumi sejajar (syzygy) pada saat bulan baru dan bulan purnama, gravitasi bulan dan matahari saling memperkuat.",
            "execution": "Pilih: Posisi Matahari, Bulan, dan Bumi berada pada satu garis lurus (syzygy) saat Bulan Baru dan Bulan Purnama."
        }
    },
    {
        "id": "geo-sim-08",
        "materi": "MITIGASI BENCANA ALAM & EKOLOGI PESISIR",
        "topic": "Hutan Mangrove sebagai Bioshield Alami Peredam Tsunami",
        "stem": "Dalam mitigasi bencana gempa bumi dan tsunami pesisir, ekosistem hutan mangrove dengan zonasi pohon _Rhizophora_ (bakau tunjang) dan _Avicennia_ (api-api) berfungsi efektif sebagai benteng alami (_bioshield_). Mekanisme biofisik hutan mangrove dalam meredam ancaman destruktif gelombang tsunami adalah...",
        "correct": "Sistem perakaran tunjang dan napas yang rapat menciptakan kekasaran hidrolik tinggi yang memecah energi kinetik gelombang, memperlambat kecepatan arus bah, serta menjebak puing-puing apung yang berbahaya bagi daratan.",
        "distractors": [
            "Daun mangrove melepaskan zat kimiawi yang mampu membekukan air laut secara instan sehingga gelombang tidak dapat merambat.",
            "Pohon mangrove menyerap seluruh massa air laut ke dalam batang pohonnya hingga surut mengering.",
            "Mangrove memantulkan gelombang tsunami $100\\%$ kembali ke samudra tanpa ada penurunan amplitudo sama sekali.",
            "Akar mangrove menahan getaran lempeng tektonik di palung laut agar tidak merambat ke garis pantai."
        ],
        "formula": {
            "title": "DISIPASI ENERGI GELOMBANG OLEH VEGETASI PESISIR",
            "latex": "\\Delta E_{\\text{tsunami}} \\propto \\rho_w \\cdot C_D \\cdot b \\cdot v^3 \\cdot \\Delta x",
            "legend": "• $C_D$: Koefisien hambatan gesek perakaran tunjang mangrove<br>• Keberadaan sabuk hijau (_greenbelt_) mangrove selebar 100 meter dapat mereduksi tinggi gelombang tsunami hingga 50 - 60%"
        },
        "hints": {
            "concept": "Mangrove sebagai bioshield: sistem perakaran rapat (akar tunjang dan napas) meningkatkan kekasaran hidrolik, memecah energi kinetik gelombang dan menahan laju kecepatan tsunami serta puing apung.",
            "execution": "Pilih: Perakaran tunjang dan napas rapat menciptakan kekasaran hidrolik tinggi yang memecah energi gelombang dan memperlambat arus."
        }
    },
    {
        "id": "geo-sim-09",
        "materi": "PENGINDERAAN JAUH & SISTEM INFORMASI GEOGRAFIS",
        "topic": "Penghitungan Luas Lahan Berbasis Resolusi Spasial Citra Raster",
        "stem": "Sebuah poligon penutup lahan perkebunan kelapa sawit teridentifikasi pada citra satelit Sentinel-2 (resolusi spasial piksel $10 \\times 10 \\text{ meter}$). Setelah dilakukan analisis perhitungan sel piksel pada sistem informasi geografis, poligon perkebunan tersebut terdiri atas $25.000 \\text{ sel piksel}$. Luas sebenarnya dari area perkebunan kelapa sawit tersebut adalah...",
        "correct": "$250 \\text{ hektar}$ ($2{,}5 \\text{ km}^2$).",
        "distractors": [
            "$25 \\text{ hektar}$.",
            "$2.500 \\text{ hektar}$.",
            "$250.000 \\text{ meter persegi}$ ($25 \\text{ hektar}$).",
            "$25 \\text{ km}^2$ ($2.500 \\text{ hektar}$)."
        ],
        "formula": {
            "title": "FORMULA LUAS AREA MODEL DATA RASTER",
            "latex": "\\begin{aligned} \\text{Luas Satu Piksel} & = 10 \\text{ m} \\times 10 \\text{ m} = 100 \\text{ m}^2 \\\\ \\text{Total Luas Area} & = N \\times \\text{Luas Piksel} = 25.000 \\times 100 \\text{ m}^2 = 2.500.000 \\text{ m}^2 \\\\ \\text{Konversi ke Hektar:} & \\quad 1 \\text{ ha} = 10.000 \\text{ m}^2 \\implies \\frac{2.500.000}{10.000} = \\mathbf{250 \\text{ hektar}} = \\mathbf{2{,}5 \\text{ km}^2} \\end{aligned}",
            "legend": "• $N$: Jumlah total piksel dalam kelas klasifikasi<br>• $1 \\text{ km}^2 = 100 \\text{ ha} = 1.000.000 \\text{ m}^2$"
        },
        "hints": {
            "concept": "Satu piksel = 10 m * 10 m = 100 m^2. Luas total = 25.000 * 100 m^2 = 2.500.000 m^2. Karena 1 ha = 10.000 m^2, maka 2.500.000 / 10.000 = 250 ha (atau 2,5 km^2).",
            "execution": "Hitung: 2.500.000 m^2 = 250 ha (2,5 km^2)."
        }
    },
    {
        "id": "geo-sim-10",
        "materi": "POLA KERUANGAN & PERTUMBUHAN WILAYAH",
        "topic": "Penentuan Lokasi Fasilitas Kesehatan Menggunakan Titik Henti Carrothers",
        "stem": "Pemerintah provinsi berencana membangun Rumah Sakit Rujukan Regional di antara Kota Cempaka ($P_C = 90.000 \\text{ jiwa}$) dan Kota Melati ($P_M = 10.000 \\text{ jiwa}$). Jarak antara kedua kota tersebut adalah $d_{CM} = 24 \\text{ km}$. Berdasarkan Hukum Titik Henti William J. Reilly / Carrothers, lokasi rumah sakit tersebut sebaiknya didirikan pada jarak...",
        "correct": "$6 \\text{ km}$ dari Kota Melati (atau $18 \\text{ km}$ dari Kota Cempaka).",
        "distractors": [
            "$12 \\text{ km}$ tepat di tengah-tengah antara Kota Cempaka dan Melati.",
            "$6 \\text{ km}$ dari Kota Cempaka (merapat ke kota besar berpenduduk padat).",
            "$8 \\text{ km}$ dari Kota Melati.",
            "$4 \\text{ km}$ dari Kota Melati."
        ],
        "formula": {
            "title": "HUKUM TITIK HENTI (BREAKING POINT THEORY)",
            "latex": "\\begin{aligned} D_M & = \\frac{d_{CM}}{1 + \\sqrt{\\frac{P_C}{P_M}}} = \\frac{24}{1 + \\sqrt{\\frac{90.000}{10.000}}} = \\frac{24}{1 + \\sqrt{9}} \\\\ & = \\frac{24}{1 + 3} = \\frac{24}{4} = \\mathbf{6 \\text{ km dari Kota Melati (Penduduk Lebih Sedikit)}} \\\\ D_C & = 24 - 6 = \\mathbf{18 \\text{ km dari Kota Cempaka}} \\end{aligned}",
            "legend": "• Titik henti selalu bergeser mendekati wilayah/kota yang memiliki jumlah penduduk lebih sedikit"
        },
        "hints": {
            "concept": "Rumus titik henti diukur dari kota berpenduduk lebih sedikit (Melati): D = d / (1 + sqrt(P_besar / P_kecil)) = 24 / (1 + sqrt(90.000 / 10.000)) = 24 / (1 + 3) = 6 km dari Kota Melati.",
            "execution": "Pilih: 6 km dari Kota Melati (atau 18 km dari Kota Cempaka)."
        }
    },
    {
        "id": "geo-sim-11",
        "materi": "PEMBANGUNAN BERKELANJUTAN & BIOSFER",
        "topic": "Siklus Karbon Terestrial: Lahan Gambut Tropis Indonesia sebagai Penyimpan Karbon",
        "stem": "Lahan gambut tropis di Sumatera, Kalimantan, dan Papua menyimpan cadangan karbon terestrial raksasa dunia dalam bentuk material organik sisa tumbuhan terdekomposisi anaerobik selama ribuan tahun. Dampak hidrologis dan biogeokimia pembukaan kanal drainase sawit pada lahan gambut yang memicu ancaman kebakaran hutan dan lahan (Karhutla) adalah...",
        "correct": "Penurunan muka air tanah gambut (_groundwater table_) menyebabkan kubah gambut mengering, terjadi proses subsidensi dan oksidasi karbon masif yang melepaskan emisi gas $CO_2$ ke atmosfer, serta gambut kering menjadi bahan bakar api bawah permukaan (_smoldering fire_) yang sangat sulit dipadamkan.",
        "distractors": [
            "Lahan gambut yang mengering secara spontan akan memadat menjadi batu bara antrasit bermutu tinggi tanpa risiko terbakar.",
            "Kanal drainase meningkatkan kelembapan tanah gambut sehingga memicu pertumbuhan lumut permafrost kutub.",
            "Gambut kering menyerap seluruh gas rumah kaca dari atmosfer secara permanen sehingga mendinginkan iklim bumi.",
            "Air gambut yang asam akan berubah menjadi air tawar murni pH netral yang menyuburkan seluruh terumbu karang laut."
        ],
        "formula": {
            "title": "DINAMIKA PENURUNAN MUKA AIR TANAH DAN OKSIDASI GAMBUT",
            "latex": "\\text{Kanal Drainase} \\implies \\text{Muka Air Tanah Gambut Turun} \\implies \\begin{cases} \\mathbf{\\text{Gambut Kering \\& Rentan Terbakar (Smoldering)}} \\\\ \\mathbf{\\text{Subsidensi Lahan (Amblesan Tanpa Balik)}} \\\\ \\mathbf{\\text{Oksidasi Mikroba Masif: C } + O_2 \\to CO_2 \\uparrow\\uparrow} \\end{cases}",
            "legend": "• Peraturan Pemerintah menetapkan batas kedalaman muka air tanah gambut maksimal 0,4 meter untuk mencegah kebakaran"
        },
        "hints": {
            "concept": "Kanal drainase gambut membuat gambut kering -> oksidasi organik melepaskan CO2 masif -> kebakaran bawah tanah (smoldering) yang sulit dipadamkan.",
            "execution": "Pilih opsi: Penurunan muka air tanah menyebabkan kubah gambut mengering, subsidensi, emisi CO2 masif, dan api bawah permukaan (smoldering fire)."
        }
    },
    {
        "id": "geo-sim-12",
        "materi": "POLA KERUANGAN & PERTUMBUHAN WILAYAH",
        "topic": "Konsep Threshold dan Range dalam Teori Tempat Sentral Walter Christaller",
        "stem": "Dalam Teori Tempat Sentral (_Central Place Theory_) yang dikemukakan Walter Christaller, penyediaan barang dan jasa di suatu pusat permukiman ditentukan oleh dua konsep dasar: Jangkauan (_Range_) dan Ambang Batas (_Threshold_). Hubungan keruangan yang tepat antara kedua konsep tersebut agar suatu usaha jasa (seperti toko perhiasan mewah atau rumah sakit spesialis) dapat beroperasi secara berkelanjutan adalah...",
        "correct": "Nilai _Range_ (jarak maksimum yang rela ditempuh konsumen untuk membeli barang) harus lebih besar daripada nilai _Threshold_ (lingkaran batas populasi minimum yang diperlukan agar usaha memperoleh laba normal), yaitu $\\text{Range} > \\text{Threshold}$.",
        "distractors": [
            "Nilai _Threshold_ harus jauh lebih besar daripada _Range_, sehingga pedagang mengalami defisit modal operasional.",
            "Nilai _Range_ dan _Threshold_ harus selalu identik nol agar konsumen tidak perlu keluar rumah sama sekali.",
            "_Range_ hanya berlaku untuk barang kebutuhan pokok harian berorde rendah sedangkan _Threshold_ hanya berlaku untuk udara bersih.",
            "Pemerintah wajib melarang keberadaan _Range_ agar seluruh wilayah memiliki harga barang yang sama secara mutlak."
        ],
        "formula": {
            "title": "SYARAT KELANGSUNGAN USAHA TEMPAT SENTRAL CHRISTALLER",
            "latex": "\\mathbf{\\text{Range}} > \\mathbf{\\text{Threshold}} \\implies \\text{Usaha Memperoleh Pasar Laba Memadai (Surplus)}",
            "legend": "• $\\text{Range}$: Jarak maksimum yang bersedia ditempuh konsumen<br>• $\\text{Threshold}$: Jumlah penduduk/daya beli minimum penopang kelangsungan hidup jenis layanan"
        },
        "hints": {
            "concept": "Syarat usaha bertahan dalam teori Christaller: Range (jangkauan konsumen) harus lebih besar dari Threshold (ambang batas minimum kelayakan modal).",
            "execution": "Pilih: Nilai Range harus lebih besar daripada nilai Threshold (Range > Threshold)."
        }
    },
    {
        "id": "geo-sim-13",
        "materi": "DINAMIKA ATMOSFER & CUACA",
        "topic": "Fenomena Angin Föhn (Angin Jatuh Panas Kering) di Indonesia",
        "stem": "Penduduk di kawasan Cirebon (Angin Kumbang), Deli Serdang (Angin Bohorok), Pasuruan (Angin Gending), dan Biak (Angin Wambraw) kerap mengalami fenomena angin lokal berkecepatan tinggi yang bersifat sangat panas dan kering saat menuruni lereng pegunungan. Proses termodinamika atmosfer yang menjelaskan mengapa angin tersebut bersifat panas dan kering di lereng bawah angin (_leeward slope_) adalah...",
        "correct": "Saat massa udara naik di lereng hadap angin (_windward_), uap air mengalami kondensasi melepaskan panas laten dan turun sebagai hujan dengan gradien adiabatik basah ($0{,}5^\\circ - 0{,}6^\\circ \\text{C} / 100 \\text{ m}$), sedangkan saat menuruni lereng belakang angin (_leeward_), massa udara kering mengalami pemanasan adiabatik kering ($1^\\circ \\text{C} / 100 \\text{ m}$) tanpa kehilangan kalor.",
        "distractors": [
            "Angin menyedot lava panas di puncak kepundan gunung berapi aktif lalu menghembuskannya ke perkebunan tembakau warga.",
            "Terjadi pembakaran hutan massal di punggung bukit yang menaikkan suhu udara secara konduksi darat.",
            "Lapisan stratosfer pecah sehingga sinar ultraviolet langsung memanaskan angin yang bertiup kencang.",
            "Angin laut berbelok mendadak di atas puncak gunung dan kehilangan seluruh kandungan oksigennya."
        ],
        "formula": {
            "title": "MEKANISME TERMODINAMIKA ANGIN FÖHN",
            "latex": "\\begin{cases} \\text{Lereng Hadap Angin (Naik):} & \\text{Gradien Adiabatik Basah } \\gamma_w \\approx 0{,}6^\\circ \\text{C} / 100 \\text{ m} \\ (\\text{Hujan Orografis}) \\\\ \\mathbf{\\text{Lereng Belakang (Turun):}} & \\mathbf{\\text{Gradien Adiabatik Kering } \\gamma_d = 1{,}0^\\circ \\text{C} / 100 \\text{ m}} \\implies \\mathbf{\\text{Suhu Naik Drastis \\& Kering}} \\end{cases}",
            "legend": "• Angin Bohorok sering merusak tanaman perkebunan tembakau Deli karena menurunkan kelembapan relatif secara drastis"
        },
        "hints": {
            "concept": "Massa udara naik di lereng windward mendingin secara adiabatik basah (0,6 C/100m) dan hujan. Saat turun di leeward, udara kering memanas secara adiabatik kering (1,0 C/100m), menghasilkan angin panas dan kering.",
            "execution": "Pilih opsi yang menjelaskan gradien adiabatik basah saat naik dan pemanasan adiabatik kering saat turun."
        }
    },
    {
        "id": "geo-sim-14",
        "materi": "DINAMIKA LITOSFER & MORFOLOGI PESISIR",
        "topic": "Klasifikasi Tipe Morfologi Pesisir Laut: Pantai Ria, Fjord, dan Barrier Island",
        "stem": "Garis pantai di dunia memiliki keragaman bentang alam akibat pengaruh tektonik, glasial, dan sedimentasi laut. Karakteristik tipe pantai Fjord yang banyak dijumpai di kawasan lintang tinggi seperti Norwegia, Alaska, dan Selandia Baru adalah...",
        "correct": "Lembah erosi gletser purba berbentuk huruf U curam berdinding terjal yang tenggelam oleh naiknya permukaan air laut pasca-pencairan es glasial, dengan perairan sempit dan sangat dalam hingga ratusan meter.",
        "distractors": [
            "Lembah sungai daratan biasa berbentuk huruf V yang tenggelam di daerah beriklim tropis basah tanpa pengaruh es.",
            "Hamparan pasir pantai datar yang memanjang sejajar garis pantai dan memisahkan laguna air asin dangkal.",
            "Pantai tebing karang terangkat yang memiliki teras-teras abrasi bertingkat akibat epirogenesa positif daratan.",
            "Delta muara sungai raksasa yang terus maju ke arah laut akibat tumpukan sedimen lumpur erosi hulu DAS."
        ],
        "formula": {
            "title": "KOMPARASI TIPE PANTAI TENGGELAM (SUBMERGENCE COASTS)",
            "latex": "\\begin{cases} \\mathbf{\\text{Pantai Fjord:}} & \\mathbf{\\text{Lembah Glasial Berbentuk U Curam Tenggelam oleh Air Laut (Sangat Dalam)}} \\\\ \\text{Pantai Ria:} & \\text{Lembah Sungai Fluvial Berbentuk V Tenggelam oleh Air Laut} \\\\ \\text{Pantai Haff / Barrier:} & \\text{Sedimentasi Spit Pasir Sejajar Garis Pantai Membentuk Laguna} \\end{cases}",
            "legend": "• Fjord memiliki ambang dangkal (_sill_) di mulut teluk dan basin sangat dalam di bagian pedalaman"
        },
        "hints": {
            "concept": "Pantai fjord = lembah glasial es berbentuk U terjal yang tenggelam oleh naiknya muka air laut pasca-zaman es, sempit dan sangat dalam.",
            "execution": "Pilih: Lembah erosi gletser purba berbentuk huruf U curam yang tenggelam oleh naiknya air laut pasca-pencairan es glasial."
        }
    },
    {
        "id": "geo-sim-15",
        "materi": "DINAMIKA KEPENDUDUKAN & KETENAGAKERJAAN",
        "topic": "Penuaan Populasi (Ageing Population) dan Angka Beban Ketergantungan Lanjut Usia",
        "stem": "Negara maju seperti Jepang dan beberapa negara Eropa telah memasuki fase struktur penduduk menua (_Ageing Population_) dengan tingkat fertilitas total ($TFR < 1{,}5$) dan angka harapan hidup di atas 84 tahun. Implikasi demografis dan tantangan sosio-ekonomi utama yang dihadapi oleh negara dengan struktur demografi tersebut adalah...",
        "correct": "Peningkatan rasio ketergantungan lansia (_old-age dependency ratio_), defisit tenaga kerja produktif di sektor riil, meningkatnya beban fiskal pensiun dan jaminan kesehatan nasional, serta ancaman penyusutan populasi absolut.",
        "distractors": [
            "Ledakan kebutuhan sekolah dasar dan fasilitas taman kanak-kanak akibat kelahiran bayi yang melonjak di luar kendali.",
            "Tingginya angka pengangguran terbuka di kalangan pemuda lulusan baru akibat surplus generasi muda usia produktif.",
            "Peningkatan pesat rasio ketergantungan anak-anak balita yang melampaui angka ketergantungan orang tua.",
            "Terjadinya gelombang emigrasi massal generasi tua ke negara-negara berkembang untuk mencari pekerjaan kasar."
        ],
        "formula": {
            "title": "RASIO BEBAN KETERGANTUNGAN LANSIA (OLD-AGE DEPENDENCY RATIO)",
            "latex": "DR_{\\text{old}} = \\frac{P_{65+}}{P_{15-64}} \\times 100 \\implies \\text{Beban Anggaran Pensiun \\& Pelayanan Kesehatan Lansia Melonjak}",
            "legend": "• Peluang baru: _Silver Economy_ (industri produk dan layanan kebutuhan lansia)"
        },
        "hints": {
            "concept": "Ageing population: proporsi lansia (65+) meningkat tinggi, usia produktif menyusut -> old-age dependency ratio naik, beban jaminan pensiun/kesehatan membengkak, kelangkaan tenaga kerja.",
            "execution": "Pilih: Peningkatan rasio ketergantungan lansia, defisit tenaga kerja produktif, beban fiskal jaminan pensiun melonjak."
        }
    },
    {
        "id": "geo-sim-16",
        "materi": "SISTEM INFORMASI GEOGRAFIS & KEBENCANAAN",
        "topic": "Analisis Tumpang Susun Berbobot (Weighted Overlay Analysis) Kerawanan Longsor",
        "stem": "Dalam penyusunan peta zonasi kerawanan longsor di kawasan perbukitan, analis SIG melakukan metode tumpang susun berbobot (_Weighted Overlay Analysis_) terhadap empat parameter spasial:\n1. Kemiringan Lereng (Bobot: $40\\%$)\n2. Jenis Batuan / Geologi (Bobot: $25\\%$)\n3. Curah Hujan Harian Rerata (Bobot: $20\\%$)\n4. Penggunaan Lahan / Tutupan Vegetasi (Bobot: $15\\%$)\nPada sebuah lereng perbukitan, diperoleh skor nilai masing-masing parameter (skala 1 - 5, di mana 5 = sangat rawan):\n- Kemiringan lereng curam: skor $5$\n- Batuan lempung napalan mudah lolos air: skor $4$\n- Curah hujan tinggi: skor $4$\n- Tutupan lahan ladang semusim tanpa terasering: skor $5$\nNilai total indeks kerawanan longsor komposit kawasan perbukitan tersebut adalah...",
        "correct": "$4{,}55$ (termasuk kelas sangat rawan bencana longsor).",
        "distractors": [
            "$3{,}80$ (kelas kerawanan sedang).",
            "$4{,}00$.",
            "$4{,}90$.",
            "$3{,}50$."
        ],
        "formula": {
            "title": "FORMULA WEIGHTED OVERLAY INDEX (SIG)",
            "latex": "\\begin{aligned} \\text{Skor Komposit} & = \\sum_{i=1}^{n} (W_i \\times S_i) \\\\ & = (0{,}40 \\times 5) + (0{,}25 \\times 4) + (0{,}20 \\times 4) + (0{,}15 \\times 5) \\\\ & = 2{,}00 + 1{,}00 + 0{,}80 + 0{,}75 = \\mathbf{4{,}55} \\end{aligned}",
            "legend": "• $W_i$: Bobot relatif parameter ($i$), $\\sum W_i = 1{,}00$ (100%)<br>• $S_i$: Skor kerawanan internal atribut piksel (skala 1 - 5)"
        },
        "hints": {
            "concept": "Weighted overlay: Skor komposit = (0,40 * 5) + (0,25 * 4) + (0,20 * 4) + (0,15 * 5) = 2,00 + 1,00 + 0,80 + 0,75 = 4,55.",
            "execution": "Hitung: 2,00 + 1,00 + 0,80 + 0,75 = 4,55."
        }
    },
    {
        "id": "geo-sim-17",
        "materi": "PENGINDERAAN JAUH & KEBAKARAN HUTAN",
        "topic": "Indeks Spektral Citra: Normalized Burn Ratio (NBR) untuk Evaluasi Karhutla",
        "stem": "Dalam pemantauan dampak kebakaran hutan dan lahan menggunakan citra multispektral Landsat-9, analis lingkungan menghitung indeks _Normalized Burn Ratio_ ($NBR$) dengan rumus $NBR = \\frac{\\text{NIR} - \\text{SWIR}}{\\text{NIR} + \\text{SWIR}}$. Karakteristik respon spektral vegetasi sehat dibandingkan dengan area hutan bekas terbakar (_burn scar_) pada saluran inframerah dekat (NIR) dan inframerah gelombang pendek (SWIR) yang mendasari rumus tersebut adalah...",
        "correct": "Vegetasi sehat memiliki pantulan sangat tinggi pada saluran NIR dan serapan kuat (pantulan sangat rendah) pada SWIR sehingga menghasilkan nilai $NBR$ positif tinggi, sedangkan area bekas terbakar kehilangan struktur daun (pantulan NIR anjlok) dan arang tanah kering memantulkan gelombang SWIR sangat tinggi sehingga nilai $NBR$ anjlok negatif.",
        "distractors": [
            "Vegetasi sehat memantulkan seluruh gelombang SWIR dan menyerap 100% gelombang cahaya tampak merah.",
            "Bekas terbakar memancarkan radiasi panas yang membuat pantulan inframerah dekat (NIR) melonjak hingga seribu kali lipat.",
            "Air dan arang arang hitam memiliki respon spektral yang identik dengan tajuk pohon kanopi hutan primer.",
            "Gelombang inframerah tidak dapat menembus atmosfer bumi sehingga nilai NBR murni dihasilkan dari estimasi suhu malam hari."
        ],
        "formula": {
            "title": "DINAMIKA SPEKTRAL VEGETASI VS BEKAS TERBAKAR (NBR)",
            "latex": "\\begin{cases} \\mathbf{\\text{Vegetasi Sehat (Klorofil Tinggi):}} & \\text{NIR Tinggi } + \\text{SWIR Rendah} \\implies \\mathbf{NBR \\gg 0 \\ (\\approx +0{,}4 \\text{ s.d. } +0{,}8)} \\\\ \\mathbf{\\text{Bekas Terbakar (Burn Scar):}} & \\text{NIR Rendah } + \\text{SWIR Tinggi} \\implies \\mathbf{NBR < 0 \\ (\\text{Bernilai Negatif})} \\end{cases}",
            "legend": "• $\\Delta NBR = NBR_{\\text{pre-fire}} - NBR_{\\text{post-fire}}$ mengukur tingkat keparahan kebakaran (_Burn Severity_)"
        },
        "hints": {
            "concept": "Vegetasi sehat: pantulan NIR tinggi, SWIR rendah -> NBR positif tinggi. Bekas terbakar: klorofil hancur (NIR rendah), tanah arang kering (SWIR tinggi) -> NBR negatif.",
            "execution": "Pilih: Vegetasi sehat pantulan NIR tinggi dan SWIR rendah (NBR positif), bekas terbakar pantulan NIR anjlok dan SWIR tinggi (NBR negatif)."
        }
    },
    {
        "id": "geo-sim-18",
        "materi": "DINAMIKA ATMOSFER & IKLIM TROPIS",
        "topic": "Klasifikasi Iklim Junghuhn Berdasarkan Ketinggian dan Komoditas Agroklimat",
        "stem": "Franz Wilhelm Junghuhn membagi zona iklim di wilayah kepulauan Indonesia berdasarkan ketinggian tempat dari permukaan laut (elevasi) dan kesesuaian tanaman budidaya pertanian. Kawasan perkebunan yang berada pada ketinggian $1.200 \\text{ meter}$ dpl dengan suhu rata-rata berkisar antara $17{,}1^\\circ - 22^\\circ \\text{C}$ diklasifikasikan ke dalam...",
        "correct": "Zona Iklim Sedang ($650 - 1.500 \\text{ m}$ dpl), yang sangat ideal untuk pengembangan komoditas perkebunan teh, kopi, kina, kina, dan tanaman hortikultura sayuran.",
        "distractors": [
            "Zona Iklim Panas ($0 - 650 \\text{ m}$ dpl), yang didominasi oleh perkebunan tebu, kelapa sawit, padi, dan pohon kelapa.",
            "Zona Iklim Sejuk ($1.500 - 2.500 \\text{ m}$ dpl), yang hanya ditumbuhi oleh hutan lumut dan pohon cemara pinus pegunungan.",
            "Zona Iklim Dingin (> $2.500 \\text{ m}$ dpl), yang membentang di puncak bersalju tanpa tanaman budidaya pertanian.",
            "Zona Iklim Kering Subtropis, yang didominasi oleh semak berduri kaktus dan tanaman kurma."
        ],
        "formula": {
            "title": "ZONASI IKLIM VERTIKAL JUNGHUHN",
            "latex": "\\begin{cases} \\mathbf{\\text{1. Zona Panas (0 - 650 m):}} & 22^\\circ - 26{,}3^\\circ \\text{C} \\implies \\text{Padi, Jagung, Tebu, Kelapa, Karet} \\\\ \\mathbf{\\text{2. Zona Sedang (650 - 1.500 m):}} & \\mathbf{17{,}1^\\circ - 22^\\circ \\text{C}} \\implies \\mathbf{\\text{Teh, Kopi, Kina, Karet, Sayuran Hortikultura}} \\\\ \\mathbf{\\text{3. Zona Sejuk (1.500 - 2.500 m):}} & 11{,}1^\\circ - 17{,}1^\\circ \\text{C} \\implies \\text{Pinus, Cemara, Hutan Lumut, Sayuran Tertentu} \\\\ \\mathbf{\\text{4. Zona Dingin (> 2.500 m):}} & < 11{,}1^\\circ \\text{C} \\implies \\text{Tidak Ada Tanaman Budidaya (Hanya Lumut)} \\end{cases}",
            "legend": "• Penurunan temperatur mengikuti gradien geotermis atmosfer bebas ($0{,}6^\\circ \\text{C}$ per kenaikan 100 meter)"
        },
        "hints": {
            "concept": "Ketinggian 1.200 m dpl masuk Zona Sedang Junghuhn (650 - 1.500 m dpl), suhu 17,1 - 22 C. Komoditas utama: teh, kopi, kina, sayuran.",
            "execution": "Pilih: Zona Iklim Sedang (650 - 1.500 m dpl), cocok untuk teh, kopi, kina, dan sayuran."
        }
    },
    {
        "id": "geo-sim-19",
        "materi": "DINAMIKA LITOSFER & GEOLOGI",
        "topic": "Genesa Pembentukan Kaldera Vulkano-Tektonik Danau Toba",
        "stem": "Danau Toba di Sumatera Utara merupakan danau terbesar di Indonesia dengan keberadaan Pulau Samosir di bagian tengahnya. Berdasarkan proses genesa geologis pembentukannya, Danau Toba diklasifikasikan sebagai danau vulkano-tektonik karena...",
        "correct": "Terbentuk akibat letusan supervolcano kataklisma purba yang mengosongkan dapur magma raksasa dan meruntuhkan atap kerak bumi (vulkanik), diikuti oleh amblasnya blok sesar Sesar Besar Sumatera (tektonik), serta pengangkatan kembali dasar kaldera pasca-letusan (_resurgent dome_) yang memunculkan Pulau Samosir.",
        "distractors": [
            "Terbentuk dari jatuhnya meteorit raksasa dari luar angkasa yang melubangi lempeng benua dan terisi air hujan meteorik.",
            "Terbentuk dari erosi pelarutan kimiawi batuan gamping karst secara masif yang menghubungkan sungai bawah tanah.",
            "Terbentuk murni akibat bendungan glasial es purba yang mencair saat pemanasan zaman interglasial.",
            "Merupakan teluk samudra Hindia yang terisolasi oleh pertumbuhan spit endapan pasir pantai penghalang."
        ],
        "formula": {
            "title": "GENESA KALDERA SUPERVOLCANO VULKANO-TEKTONIK",
            "latex": "\\text{Erupsi Supervolcano (74.000 BP)} \\xrightarrow{\\text{Runtuhnya Dapur Magma}} \\text{Kaldera Ambruk} \\xrightarrow{\\text{Sesar Semangko}} \\text{Danau Vulkano-Tektonik} \\xrightarrow{\\text{Resurgent Domal Uplift}} \\mathbf{\\text{Pulau Samosir}}",
            "legend": "• Letusan Toba mengeluarkan lebih dari 2.800 km³ material piroklastik dan memicu kemacetan genetik (_genetic bottleneck_) manusia purba"
        },
        "hints": {
            "concept": "Danau Toba adalah danau vulkano-tektonik: letusan supervolcano mengosongkan kantung magma -> atap runtuh membentuk kaldera -> amblas di zona sesar tektonik -> pengangkatan kembali (resurgent dome) membentuk Pulau Samosir.",
            "execution": "Pilih: Letusan supervolcano mengosongkan dapur magma dan meruntuhkan atap kerak (vulkanik), amblasan sesar tektonik, dan resurgent dome membentuk Pulau Samosir."
        }
    },
    {
        "id": "geo-sim-20",
        "materi": "DINAMIKA LITOSFER & PALEOMAGNETISME",
        "topic": "Bukti Pemekaran Dasar Samudra (Seafloor Spreading) dan Pita Magnetik Purba",
        "stem": "Teori Tektonik Lempeng mendapat konfirmasi empiris terkuat melalui penemuan pola pita kemagnetan purba (_magnetic stripes_) simetris di dasar Samudra Atlantik oleh Vine dan Matthews pada tahun 1963. Fenomena geologis yang membuktikan bahwa kerak samudra terus memekar dan bergerak menjauh dari pematang tengah samudra (_Mid-Ocean Ridge_) adalah...",
        "correct": "Pola polaritas medan magnetik bumi normal dan terbalik (_magnetic reversals_) yang terekam dalam mineral magnetit batuan basal dasar laut tersusun simetris di kedua sisi pematang, dengan usia batuan yang semakin tua seiring bertambahnya jarak dari poros pematang tengah samudra.",
        "distractors": [
            "Usia batuan beku di poros pematang tengah samudra terbukti berusia paling tua dibandingkan batuan di dekat benua.",
            "Dasar samudra tersusun atas lapisan batuan granit berusia miliaran tahun yang tidak pernah bergerak sejak bumi terbentuk.",
            "Ketebalan lapisan sedimen lumpur laut di atas pematang tengah samudra terbukti paling tebal di seluruh dunia.",
            "Medan magnet bumi di dasar samudra selalu menunjuk ke arah khatulistiwa tanpa pernah mengalami pembalikan arah kutub."
        ],
        "formula": {
            "title": "HIPOTESIS PEMEKARAN DASAR SAMUDRA VINE-MATTHEWS-MORLEY",
            "latex": "\\begin{cases} \\mathbf{\\text{Poros Ridge:}} & \\text{Magma Basal Baru Membeku } \\implies \\text{Usia Paling Muda (0 Juta Tahun)} \\\\ \\mathbf{\\text{Simetri Pita:}} & \\text{Rekaman Polaritas Magnetik (Normal/Reversed) Cermin Identik Kiri-Kanan} \\\\ \\mathbf{\\text{Arah Menjauh:}} & \\text{Usia Batuan Basal } (t \\uparrow) \\text{ dan Tebal Sedimen } (d \\uparrow) \\text{ Makin Meningkat Menuju Benua} \\end{cases}",
            "legend": "• Menjadi bukti valid mekanisme arus konveksi mantel dalam mendorong lempeng tektonik divergen"
        },
        "hints": {
            "concept": "Bukti pemekaran dasar samudra (seafloor spreading): pita anomali magnetik bumi normal-terbalik tersusun simetris di kedua sisi pematang, batuan di poros ridge paling muda dan semakin menjauh semakin tua.",
            "execution": "Pilih: Pola polaritas magnetik bumi tersusun simetris di kedua sisi pematang, usia batuan semakin tua menjauhi pematang."
        }
    },
    {
        "id": "geo-sim-21",
        "materi": "PEMBANGUNAN BERKELANJUTAN & TATA RUANG",
        "topic": "Analisis Daya Dukung Lingkungan Hidup (Carrying Capacity) Lahan Pangan",
        "stem": "Dalam penataan ruang wilayah kabupaten, daya dukung lahan pertanian pangan dihitung menggunakan formula Odum/Ketetapan Menteri LHK dengan membandingkan ketersediaan lahan pangan efektif ($S_L$) terhadap kebutuhan lahan minimum untuk hidup layak per kapita ($D_L$). Jika suatu wilayah memiliki status daya dukung lahan pangan $D_L > S_L$ (defisit daya dukung), implikasi perencanaan spasial yang harus diambil adalah...",
        "correct": "Menghentikan konversi lahan pertanian basah beririgasi teknis (_zero conversion_), meningkatkan indeks pertanaman melalui intensifikasi teknologi pertanian, serta mengendalikan laju pertambahan penduduk lokal.",
        "distractors": [
            "Mempercepat alih fungsi seluruh sawah tersisa menjadi kawasan perumahan komersial dan kawasan industri padat modal.",
            "Mengusir seluruh petani miskin ke luar perbatasan provinsi tanpa ganti rugi pembebasan lahan garapan.",
            "Menutup seluruh saluran irigasi primer bendungan agar lahan sawah mengering menjadi lahan semak belukar.",
            "Menghapus sektor pertanian dari dokumen RPJMD dan menggantungkan seratus persen pangan dari pasokan impor luar negeri tanpa cadangan logistik."
        ],
        "formula": {
            "title": "STATUS DAYA DUKUNG LAHAN PERTANIAN PANGAN",
            "latex": "\\begin{cases} S_L > D_L & \\implies \\text{Status Surplus: Daya Dukung Lahan Aman} \\\\ S_L = D_L & \\implies \\text{Status Kritis: Daya Dukung Lahan Seimbang} \\\\ \\mathbf{S_L < D_L} & \\implies \\mathbf{\\text{Status Defisit: Tekanan Penduduk Melampaui Kemampuan Lahan Pangan}} \\end{cases}",
            "legend": "• Kebutuhan lahan minimum hidup layak standar nasional $\\approx 0{,}1 - 0{,}15$ hektar beras per kapita per tahun"
        },
        "hints": {
            "concept": "Defisit daya dukung lahan pangan (SL < DL): lahan tidak cukup menopang pangan penduduk -> langkah tata ruang: moratorium alih fungsi sawah (zero conversion), intensifikasi pertanian, dan kendali laju penduduk.",
            "execution": "Pilih: Menghentikan konversi lahan pertanian sawah, meningkatkan intensifikasi teknologi pertanian, dan mengendalikan laju penduduk."
        }
    },
    {
        "id": "geo-sim-22",
        "materi": "DINAMIKA LITOSFER & MORFOLOGI FLUVIAL",
        "topic": "Karakteristik Pola Aliran Sungai Trellis pada Struktur Lipatan Geologi",
        "stem": "Pola aliran sungai di permukaan bumi sangat dikontrol oleh struktur batuan geologi dasar dan lereng topografi. Karakteristik geometris dari pola aliran sungai _Trellis_ yang khas terbentuk di wilayah pegunungan lipatan antiklin dan sinklin paralel (seperti di Pegunungan Appalachia atau Pegunungan Kendeng) adalah...",
        "correct": "Sungai utama mengalir sejajar di sepanjang lembah sinklin paralel, dan anak-anak sungai bermuara tegak lurus ($90^\\circ$) ke sungai utama setelah memotong sayap antiklin melalui celah sempit.",
        "distractors": [
            "Anak-anak sungai membentuk sudut lancip menyatu menyerupai cabang-cabang ranting pohon alami pada batuan beku homogen.",
            "Aliran sungai memencar melingkar keluar dari satu titik puncak kerucut gunung berapi tunggal secara simetris.",
            "Anak-anak sungai membelok patah-patah tajam membentuk sudut $90^\\circ$ murni mengikuti rekahan patahan sesar batuan keras.",
            "Aliran sungai mengalir memusat menuju satu danau cekungan depresi tertutup tanpa saluran pelepasan ke laut."
        ],
        "formula": {
            "title": "KLASIFIKASI POLA ALIRAN SUNGAI FLUVIAL",
            "latex": "\\begin{cases} \\mathbf{\\text{Dendritik:}} & \\text{Bercabang seperti ranting pohon (Batuan sedimen horisontal/homogen)} \\\\ \\mathbf{\\text{Trellis:}} & \\mathbf{\\text{Sejajar lembah sinklin, anak sungai tegak lurus (Pegunungan Lipatan)}} \\\\ \\mathbf{\\text{Rektangular:}} & \\text{Patah-patah menyiku } 90^\\circ \\text{ dikontrol sistem rekahan patahan / sesar} \\\\ \\mathbf{\\text{Radial Sentrifugal:}} & \\text{Menyebar keluar dari puncak kerucut kubah / gunung api} \\\\ \\mathbf{\\text{Radial Sentripetal:}} & \\text{Memusat ke cekungan danau depresi} \\end{cases}",
            "legend": "• Pola Trellis memperlihatkan jajaran perbukitan antiklin paralel yang diselingi lembah sinklin luas"
        },
        "hints": {
            "concept": "Pola trellis: khas pada pegunungan lipatan antiklin-sinklin, sungai utama sejajar di lembah, anak sungai masuk tegak lurus (90 derajat).",
            "execution": "Pilih: Sungai utama mengalir sejajar di sepanjang lembah sinklin, anak sungai bermuara tegak lurus (90 derajat)."
        }
    },
    {
        "id": "geo-sim-23",
        "materi": "DINAMIKA ATMOSFER & IKLIM PERKOTAAN",
        "topic": "Fenomena Pulau Bahang Perkotaan (Urban Heat Island / UHI)",
        "stem": "Kawasan pusat kota metropolitan Jakarta dan Surabaya secara konsisten mencatat suhu udara rata-rata $2^\\circ - 5^\\circ \\text{C}$ lebih panas dibandingkan wilayah pedesaan di sekelilingnya pada malam hari, membentuk fenomena Pulau Bahang Perkotaan (_Urban Heat Island_ / UHI). Faktor utama penyebab terjadinya efek UHI tersebut ditinjau dari neraca energi permukaan adalah...",
        "correct": "Dominasi material buatan berkemampuan menyerap panas tinggi (aspal, beton) dengan albedo rendah, pelepasan panas antropogenik (kendaraan bermotor, AC gedung perkantoran), serta minimnya ruang terbuka hijau (RTH) yang membatasi proses pendinginan evapotranspirasi alami.",
        "distractors": [
            "Tingginya aktivitas letusan gunung berapi bawah tanah di bawah pusat perkantoran perbankan kota metropolitan.",
            "Penebalan lapisan ozon stratosfer di atas langit kota yang memantulkan kembali panas bumi ke tanah.",
            "Tiupan angin darat dan angin laut yang terhenti total di seluruh wilayah pesisir kepulauan Indonesia.",
            "Adanya reaksi fisi nuklir spontan pada pondasi tiang pancang gedung pencakar langit kota besar."
        ],
        "formula": {
            "title": "PENYEBAB UTAMA URBAN HEAT ISLAND (UHI)",
            "latex": "\\text{Efek UHI} \\equiv \\begin{cases} \\mathbf{\\text{1. Albedo Rendah:}} & \\text{Permukaan aspal \\& beton menyerap radiasi siang hari} \\\\ \\mathbf{\\text{2. Panas Antropogenik:}} & \\text{Buangan panas AC sentral, mesin industri, \\& transportasi} \\\\ \\mathbf{\\text{3. Defisit Evapotranspirasi:}} & \\text{Minimnya vegetasi RTH mereduksi pendinginan evaporatif} \\\\ \\mathbf{\\text{4. Efek Urban Canyon:}} & \\text{Gedung tinggi memperangkap radiasi gelombang panjang} \\end{cases}",
            "legend": "• Solusi mitigasi: Penambahan Ruang Terbuka Hijau (RTH minimal 30%), atap hijau (_green roofs_), dan pemakaian material ber-albedo tinggi"
        },
        "hints": {
            "concept": "Urban Heat Island (UHI): aspal/beton ber-albedo rendah menyerap panas, buangan panas AC dan kendaraan (antropogenik), serta minimnya RTH untuk pendinginan evapotranspirasi.",
            "execution": "Pilih opsi: Dominasi material buatan penyerap panas (aspal, beton), pelepasan panas antropogenik, dan minimnya ruang terbuka hijau."
        }
    },
    {
        "id": "geo-sim-24",
        "materi": "DINAMIKA KEPENDUDUKAN & KETENAGAKERJAAN",
        "topic": "Kepadatan Penduduk Agraris dan Tekanan Involusi Pertanian",
        "stem": "Sosiolog antropologi Clifford Geertz mencetuskan istilah 'Involusi Pertanian' (_Agricultural Involution_) untuk mendeskripsikan kondisi perdesaan di Pulau Jawa di mana pertumbuhan jumlah penduduk yang tinggi tidak diimbangi oleh perluasan lahan sawah garapan. Akibat fenomena fragmentasi lahan sawah menjadi petak-petak sangat sempit (< 0,25 hektar per kepala keluarga petani gurem) tersebut terhadap produktivitas tenaga kerja agraris adalah...",
        "correct": "Terjadinya penyerapan tenaga kerja berlebih tanpa peningkatan output marjinal (produk marjinal tenaga kerja mendekati nol / $MP_L \\approx 0$), yang memicu pengangguran terselubung (_disguised unemployment_) dan kemiskinan perdesaan.",
        "distractors": [
            "Peningkatan dramatis keuntungan bersih petani gurem hingga mampu membeli mesin pemanen modern dari luar negeri.",
            "Terjadinya lonjakan ekspor beras pulau Jawa ke pasar komoditas internasional secara mandiri.",
            "Keluarga petani beralih secara serentak menjadi investor pasar modal saham korporasi agribisnis multinasional.",
            "Lahan pertanian sawah berubah secara alami menjadi padang rumput sabana luas tempat peternakan kuda liar."
        ],
        "formula": {
            "title": "FENOMENA INVOLUSI PERTANIAN DAN PRODUK MARJINAL TENAGA KERJA",
            "latex": "\\text{Fragmentasi Lahan Kritis} + \\text{Tenaga Kerja Berlebih} \\implies \\mathbf{MP_L \\approx 0} \\implies \\mathbf{\\text{Pengangguran Terbuka / Terselubung (Disguised Unemployment)}}",
            "legend": "• 'Membagi kemiskinan bersama' (_shared poverty_) di mana kerja fisik dibagi makin banyak orang tanpa kenaikan hasil panen total"
        },
        "hints": {
            "concept": "Involusi pertanian Geertz di Jawa: fragmentasi lahan sawah sempit + penduduk padat -> produk marjinal mendekati nol (MPL ~ 0) -> timbul pengangguran terselubung dan kemiskinan.",
            "execution": "Pilih: Penyerapan tenaga kerja berlebih tanpa peningkatan output marjinal (MPL ~ 0), memicu pengangguran terselubung."
        }
    },
    {
        "id": "geo-sim-25",
        "materi": "DINAMIKA HIDROSFER & IKLIM GLOBAL",
        "topic": "Pengaruh Indian Ocean Dipole (IOD) terhadap Curah Hujan di Indonesia",
        "stem": "Selain fenomena ENSO di Samudra Pasifik, variabilitas iklim antartahunan di wilayah barat Indonesia sangat dipengaruhi oleh fenomena Indian Ocean Dipole (IOD) di Samudra Hindia. Karakteristik fase IOD Positif ($+IOD$) dan dampaknya terhadap sektor pertanian di wilayah barat Sumatera dan selatan Jawa adalah...",
        "correct": "Suhu muka laut di Samudra Hindia bagian barat (pantai timur Afrika) menghangat luar biasa sedangkan di timur (barat Sumatera/selatan Jawa) mendingin drastis, menyebabkan konveksi awan bergeser ke Afrika sehingga wilayah barat Indonesia mengalami penurunan curah hujan tajam dan kekeringan lahan pertanian.",
        "distractors": [
            "Suhu muka laut di perairan barat Sumatera memanas drastis memicu banjir bandang terus-menerus sepanjang tahun.",
            "Terjadinya pembalikan arah rotasi bumi yang menghentikan tiupan angin muson barat di laut Jawa.",
            "Salinitas air laut Samudra Hindia anjlok menjadi tawar akibat pencairan gunung es di kutub selatan.",
            "Tidak ada pengaruh sama sekali karena Samudra Hindia terpisah secara fisik dari pulau-pulau di Indonesia."
        ],
        "formula": {
            "title": "KOMPARASI FASE INDIAN OCEAN DIPOLE (IOD)",
            "latex": "\\begin{cases} \\mathbf{\\text{IOD Positif (+IOD):}} & \\text{Suhu Muka Laut Barat Sumatera Dingin} \\implies \\mathbf{\\text{Kekeringan Parah di Indonesia Barat}} \\\\ \\mathbf{\\text{IOD Negatif (-IOD):}} & \\text{Suhu Muka Laut Barat Sumatera Hangat} \\implies \\text{Curah Hujan Tinggi / Banjir di Indonesia Barat} \\end{cases}",
            "legend": "• Jika peristiwa IOD Positif terjadi bersamaan dengan El Niño, Indonesia mengalami kemarau berkepanjangan yang sangat dahsyat"
        },
        "hints": {
            "concept": "IOD Positif: Suhu laut di dekat Sumatera/Jawa mendingin, di Afrika barat memanas -> konveksi pindah ke barat (Afrika) -> Indonesia barat mengalami kekeringan ekstrem.",
            "execution": "Pilih opsi: Suhu laut Samudra Hindia barat Afrika menghangat, barat Sumatera mendingin, memicu penurunan curah hujan tajam dan kekeringan di Indonesia barat."
        }
    },

    # -------------------------------------------------------------
    # 5 MULTI-SELECT HOTS (geo-sim-26 to geo-sim-30)
    # -------------------------------------------------------------
    {
        "id": "geo-sim-26",
        "materi": "DINAMIKA LITOSFER & PEDOSFER",
        "topic": "Karakteristik Fisik dan Kesuburan Tanah Vulkanik Andosol",
        "stem": "Tanah Andosol merupakan jenis tanah subur yang berkembang dari pelapukan material piroklastik abu vulkanik di lereng gunung api aktif. Manakah TIGA karakteristik fisik dan kimiawi tanah Andosol berikut yang BENAR? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Memiliki solum tanah yang tebal dan gembur dengan kandungan bahan organik (humus) yang sangat tinggi."},
            {"key": "B", "text": "Didominasi oleh mineral amorf alofan yang memiliki daya jerap (retensi) air dan kapasitas pertukaran kation (KPK) tinggi."},
            {"key": "C", "text": "Memiliki fiksasi fosfat ($P$) yang sangat tinggi oleh mineral amorf sehingga pemupukan fosfat membutuhkan perlakuan khusus."},
            {"key": "D", "text": "Merupakan tanah yang sangat tua dan miskin hara karena telah terlapuk lanjut di daerah tropis berkapur keras."},
            {"key": "E", "text": "Memiliki permeabilitas sangat buruk dan selalu tergenang air asin pasang surut di muara delta sungai."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "KARAKTERISTIK PEDOLOGI TANAH ANDOSOL (ORDER ANDISOLS)",
            "latex": "\\text{Andosol} \\equiv \\begin{cases} \\mathbf{\\text{1. Induk: Abu / Tefra Vulkanik}} \\\\ \\mathbf{\\text{2. Mineralogi: Alofan, Imodolit (Mineral Amorf)}} \\\\ \\mathbf{\\text{3. Retensi Air Sangat Tinggi \\& Bulk Density Rendah (< 0{,}9 g/cm}^3)} \\\\ \\mathbf{\\text{4. Fiksasi Fosfat Kuat (P-Retention > 85\\%)}} \\end{cases}",
            "legend": "• A, B, C BENAR: Karakteristik khas ordo tanah Andisols lereng vulkanik<br>• D adalah tanah Oksisol/Laterit; E adalah tanah Aluvial/Gambut pantai"
        },
        "hints": {
            "concept": "Ciri tanah Andosol: solum tebal gembur kaya bahan organik (A), kaya mineral amorf alofan dengan retensi air tinggi (B), fiksasi fosfat tinggi (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "geo-sim-27",
        "materi": "MITIGASI BENCANA ALAM & GEOLOGI",
        "topic": "Faktor Penyebab Terjadinya Likuifaksi Pasca-Gempa Bumi",
        "stem": "Peristiwa gempa bumi Palu 2018 memicu likuifaksi dahsyat di Petobo dan Balaroa yang menenggelamkan ribuan permukiman. Manakah TIGA kondisi geologis dan hidrologis lokal berikut yang menjadi prasyarat mutlak terjadinya likuifaksi? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Lapisan tanah bawah permukaan tersusun atas endapan pasir berbutir lepas, halus hingga sedang, yang belum terkonsolidasi padat."},
            {"key": "B", "text": "Kondisi muka air tanah dangkal (jenuh air / _saturated soil_) tepat di bawah permukaan tanah permukiman."},
            {"key": "C", "text": "Adanya getaran siklik beban dinamis yang kuat dan berulang dari gelombang gempa bumi tektonik (biasanya magnitudo $M_w \\ge 6{,}0$)."},
            {"key": "D", "text": "Lapisan batuan dasar merupakan batuan beku granit pejal monolit tanpa retakan sedalam puluhan kilometer."},
            {"key": "E", "text": "Kawasan perbukitan gersang berkapur dengan kelembapan tanah $0\\%$ dan beriklim gurun pasir."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "TIGA PRASYARAT MUTLAK LIKUIFAKSI TANAH (SOIL LIQUEFACTION)",
            "latex": "\\begin{aligned} \\mathbf{\\text{Likuifaksi}} & \\iff \\begin{cases} \\mathbf{\\text{1. Pasir Lepas / Lanau Tak Terkonsolidasi}} \\\\ \\mathbf{\\text{2. Kejenuhan Air Penuh (Muka Air Dangkal)}} \\\\ \\mathbf{\\text{3. Guncangan Gempa Bumi Siklik Kuat}} \\end{cases} \\\\ & \\implies \\text{Tekanan Air Pori (u) Melonjak} \\implies \\sigma' = \\sigma - u = 0 \\implies \\mathbf{\\text{Tanah Berperilaku Seperti Cairan Lumpur}} \\end{aligned}",
            "legend": "• Tegangan efektif tanah ($\\sigma'$) anjlok menjadi nol sehingga daya dukung tanah lenyap seketika"
        },
        "hints": {
            "concept": "Syarat likuifaksi: lapisan pasir lepas belum terkonsolidasi (A), muka air tanah dangkal jenuh air (B), guncangan gempa bumi kuat berulang (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "geo-sim-28",
        "materi": "SISTEM INFORMASI GEOGRAFIS & KEBENCANAAN",
        "topic": "Parameter Kunci Analisis Kerentanan Banjir Perkotaan dalam SIG",
        "stem": "Dalam pemodelan spasial analisis risiko dan kerentanan bencana banjir perkotaan (_Urban Flood Vulnerability_) menggunakan SIG, manakah TIGA lapisan tematik spasial berikut yang paling krusial untuk ditumpang-susunkan (_overlay_)? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Model Elevasi Digital (DEM) untuk menganalisis kemiringan lereng, bentuk cekungan mikro, dan akumulasi aliran limpasan permukaan."},
            {"key": "B", "text": "Peta tutupan lahan dan koefisien limpasan (_runoff coefficient_) untuk menghitung persentase permukaan kedap air (_impervious surface_)."},
            {"key": "C", "text": "Peta kapasitas jaringan saluran drainase primer-sekunder perkotaan dan sempadan sungai eksisting."},
            {"key": "D", "text": "Peta sebaran mineral tambang emas dan tembaga bawah tanah di pedalaman pulau."},
            {"key": "E", "text": "Peta jalur orbit satelit navigasi global di lapisan termosfer luar angkasa."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "LAYER TEMATIK ANALISIS BANJIR KOTA DALAM SIG",
            "latex": "\\text{Model Kerentanan Banjir} = f(\\mathbf{\\text{DEM Elevasi Cekungan}}, \\ \\mathbf{\\text{Permukaan Kedap Air Lahan}}, \\ \\mathbf{\\text{Kapasitas Drainase Sungai}})",
            "legend": "• A, B, C BENAR: Parameter hidro-geomorfologi perkotaan esensial<br>• D dan E tidak relevan dengan genangan air hujan permukaan perkotaan"
        },
        "hints": {
            "concept": "Tiga layer krusial analisis banjir kota dalam SIG: DEM elevasi/cekungan lereng (A), Peta tutupan lahan dan koefisien limpasan kedap air (B), Peta kapasitas drainase dan sungai (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "geo-sim-29",
        "materi": "POLA KERUANGAN DESA & KOTA",
        "topic": "Dampak Negatif Fenomena Urban Sprawl terhadap Lingkungan Pinggiran Kota",
        "stem": "Fenomena perembetan kota tak terkendali ke arah pinggiran (_Urban Sprawl_) menjadi permasalahan tata ruang akut di kawasan aglomerasi Jabodetabek, Gerbangkertosusila, dan Mebidang. Manakah TIGA dampak negatif _urban sprawl_ berikut terhadap lingkungan dan ekonomi perkotaan? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Alih fungsi masif lahan sawah subur dan daerah resapan air di wilayah pinggiran menjadi perumahan klaster dan ruko komersial."},
            {"key": "B", "text": "Meningkatnya ketergantungan mobilitas harian pada kendaraan pribadi bermotor yang memicu pemborosan konsumsi BBM dan kemacetan parah di koridor komuter."},
            {"key": "C", "text": "Membengkaknya biaya penyediaan infrastruktur publik dasar (jaringan air bersih, listrik, pipa sanitasi, jalan raya) karena permukiman menyebar sporadis dan terpisah-pisah."},
            {"key": "D", "text": "Terwujudnya efisiensi mutlak penggunaan angkutan umum massal terpadu di setiap lorong pedesaan terpencil."},
            {"key": "E", "text": "Penurunan suhu udara kota metropolitan secara alami menjadi sejuk seperti di pegunungan es."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "DAMPAK KERUANGAN DAN LINGKUNGAN URBAN SPRAWL",
            "latex": "\\text{Urban Sprawl} \\implies \\begin{cases} \\mathbf{\\text{1. Konversi Lahan Subur \\& Resapan Air Pinggiran}} \\\\ \\mathbf{\\text{2. Ketergantungan Kendaraan Pribadi (Tinggi Emisi CO}_2\\text{)}} \\\\ \\mathbf{\\text{3. Inefisiensi Penyediaan Infrastruktur Publik}} \\\\ \\text{Solusi:} \\quad \\text{Konsep Kota Kompak (Compact City) \\& Transit-Oriented Development (TOD)} \\end{cases}",
            "legend": "• A, B, C BENAR: Gejala kegagalan tata ruang akibat perembetan horizontal tak terkendali"
        },
        "hints": {
            "concept": "Dampak negatif urban sprawl: konversi lahan sawah dan resapan air (A), ketergantungan kendaraan pribadi dan emisi BBM tinggi (B), biaya infrastruktur publik membengkak akibat permukiman sporadis (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "geo-sim-30",
        "materi": "DINAMIKA BIOSFER & BIOGEOGRAFI",
        "topic": "Karakteristik Fauna Endemik Wilayah Peralihan (Wallacea)",
        "stem": "Kawasan Kepulauan Wallacea (Sulawesi, Maluku, dan Nusa Tenggara) dibatasi oleh Garis Wallace di barat dan Garis Lydekker/Weber di timur. Manakah TIGA satwa berikut yang merupakan fauna endemik asli khas Wilayah Peralihan Wallacea Indonesia? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Komodo (_Varanus komodoensis_) di Nusa Tenggara Timur."},
            {"key": "B", "text": "Babirusa (_Babyrousa babyrussa_) dan Anoa (_Bubalus depressicornis_) di Sulawesi."},
            {"key": "C", "text": "Burung Maleo (_Macrocephalon maleo_) yang memanfaatkan panas geotermal bumi untuk menetaskan telurnya di Sulawesi."},
            {"key": "D", "text": "Orangutan Sumatera (_Pongo abelii_) dan Harimau Sumatera yang berciri khas fauna tipe Asiatis."},
            {"key": "E", "text": "Kanguru Pohon dan Burung Cenderawasih yang merupakan fauna khas tipe Australis di Papua."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "FAUNA ENDEMIK WALLACEA (WILAYAH PERALIHAN)",
            "latex": "\\text{Zona Wallacea} \\implies \\mathbf{\\text{Komodo, Babirusa, Anoa, Burung Maleo, Tarsius, Kuskus Beruang}}",
            "legend": "• D adalah fauna Asiatis Barat (Paparan Sunda)<br>• E adalah fauna Australis Timur (Paparan Sahul)<br>• A, B, C BENAR: Fauna purba endemik pulau terisolasi Wallacea"
        },
        "hints": {
            "concept": "Fauna peralihan Wallacea: Komodo di NTT (A), Babirusa dan Anoa di Sulawesi (B), Burung Maleo di Sulawesi (C). Orangutan adalah fauna Asiatis, Cenderawasih adalah fauna Australis.",
            "execution": "Pilih A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH HOTS (geo-sim-31 to geo-sim-35)
    # -------------------------------------------------------------
    {
        "id": "geo-sim-31",
        "type": "matrix",
        "materi": "KONSEP DASAR & PENDEKATAN GEOGRAFI",
        "topic": "Konsep, Prinsip, dan Pendekatan Analisis Geografi",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai konsep, prinsip, dan pendekatan dalam kajian geografi modern!",
        "statements": [
            {
                "text": "Pendekatan Kelingkungan (Ekologi) mengkaji interaksi timbal balik antara organisme hidup (terutama aktivitas manusia) dengan lingkungan fisiknya.",
                "correct": True
            },
            {
                "text": "Prinsip Korologi memadukan prinsip persebaran, interelasi, dan deskripsi dalam mengkaji fenomena geosfer pada ruang wilayah tertentu secara komprehensif.",
                "correct": True
            },
            {
                "text": "Konsep Morfologi geografi hanya mempelajari tata letak lintang astronomis suatu wilayah terhadap khatulistiwa tanpa memperhitungkan bentuk relief muka bumi.",
                "correct": False
            },
            {
                "text": "Pendekatan Keruangan (Spasial) menganalisis variasi perbedaan lokasi fenomena geosfer di permukaan bumi dengan mempertimbangkan pola, struktur, dan proses keruangan.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP DAN PENDEKATAN KAJIAN GEOGRAFI",
            "latex": "\\text{Pendekatan} = \\begin{cases} \\text{Spasial (Keruangan)} \\\\ \\text{Ekologis (Kelingkungan)} \\\\ \\text{Kompleks Wilayah} \\end{cases}, \\quad \\text{Prinsip} = \\begin{cases} \\text{Persebaran, Interelasi} \\\\ \\text{Deskripsi, Korologi (Sintesis)} \\end{cases}",
            "legend": "• Pernyataan 1 BENAR: Esensi pendekatan kelingkungan Bintarto<br>• Pernyataan 2 BENAR: Definisi baku prinsip korologi modern<br>• Pernyataan 3 SALAH: Konsep morfologi mempelajari bentuk relief permukaan bumi (pegunungan, lembah, dataran), bukan posisi lintang bujur<br>• Pernyataan 4 BENAR: Definisi pendekatan keruangan spasial"
        },
        "hints": {
            "concept": "Pendekatan ekologi mengkaji relasi manusia dan alam. Korologi menggabungkan persebaran, interelasi, deskripsi. Morfologi mempelajari bentuk relief permukaan bumi (bukan koordinat astronomis). Pendekatan spasial menganalisis pola keruangan.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    },
    {
        "id": "geo-sim-32",
        "type": "matrix",
        "materi": "DINAMIKA ATMOSFER & KLIMATOLOGI",
        "topic": "Dinamika Atmosfer, Tekanan Udara, dan Sirkulasi Angin",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai dinamika atmosfer dan sirkulasi angin di bumi!",
        "statements": [
            {
                "text": "Hukum Buys Ballot menyatakan bahwa angin bertiup dari daerah bertekanan maksimum ke minimum, dan mengalami pembiasan ke arah kanan di belahan bumi utara serta ke arah kiri di belahan bumi selatan.",
                "correct": True
            },
            {
                "text": "Gaya Coriolis timbul akibat pengaruh gravitasi bulan dan mencapai nilai pembelokan maksimum tepat di atas garis khatulistiwa (0 derajat).",
                "correct": False
            },
            {
                "text": "Lapisan Stratosfer memiliki fenomena pembalikan suhu (inversi termal) di mana suhu udara semakin ke atas semakin meningkat karena adanya penyerapan sinar ultraviolet oleh gas ozon.",
                "correct": True
            },
            {
                "text": "Awan Cumulonimbus merupakan awan rendah tipis berlapis-lapis yang tidak pernah menimbulkan kilat, petir, maupun hujan lebat.",
                "correct": False
            }
        ],
        "formula": {
            "title": "HUKUM DINAMIKA ATMOSFERIK BUMI",
            "latex": "\\text{Hukum Buys Ballot}, \\quad F_{\\text{coriolis}} = 2m\\Omega v \\sin\\phi \\implies \\text{Di Ekuator } (\\phi = 0^\\circ) \\implies F_c = 0",
            "legend": "• Pernyataan 1 BENAR: Hukum Buys Ballot pembiasan angin<br>• Pernyataan 2 SALAH: Gaya Coriolis bernilai NOL di khatulistiwa dan maksimum di kutub bumi ($90^\\circ$)<br>• Pernyataan 3 BENAR: Ciri lapisan stratosfer berkat lapisan ozon ($O_3$)<br>• Pernyataan 4 SALAH: Cumulonimbus adalah awan konvektif raksasa pemicu badai guntur, petir, dan hujan es"
        },
        "hints": {
            "concept": "Buys Ballot: belok kanan di BBU, belok kiri di BBS. Gaya Coriolis bernilai NOL di ekuator. Stratosfer mengalami inversi suhu karena ozon. Cumulonimbus adalah awan badai petir lebat.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "geo-sim-33",
        "type": "matrix",
        "materi": "PENGINDERAAN JAUH & SISTEM INFORMASI GEOGRAFIS",
        "topic": "Prinsip Penginderaan Jauh dan Analisis Spasial SIG",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai teknologi penginderaan jauh dan sistem informasi geografis!",
        "statements": [
            {
                "text": "Sensor radar (SAR) merupakan sistem penginderaan jauh aktif yang mampu merekam permukaan bumi menembus awan dan kegelapan malam hari.",
                "correct": True
            },
            {
                "text": "Model data raster dalam SIG merepresentasikan objek geografis dalam bentuk pasangan koordinat titik (point), garis (polyline), dan poligon (polygon).",
                "correct": False
            },
            {
                "text": "Analisis Buffering dalam SIG digunakan untuk membuat zona penyangga dengan jarak tertentu di sekitar fitur geografis (misalnya batas sempadan sungai 50 meter).",
                "correct": True
            },
            {
                "text": "Resolusi spektral citra satelit mengacu pada ukuran terkecil luas objek di permukaan bumi yang dapat direkam oleh satu sel piksel sensor.",
                "correct": False
            }
        ],
        "formula": {
            "title": "PRINSIP RESOLUSI DAN MODEL DATA SPASIAL",
            "latex": "\\begin{cases} \\text{Vektor: Titik, Garis, Poligon} \\iff \\text{Raster: Matriks Sel Piksel Bergrid} \\\\ \\text{Resolusi Spasial: Ukuran Fisik Piksel (m)} \\iff \\text{Resolusi Spektral: Jumlah Saluran Gelombang (Bands)} \\end{cases}",
            "legend": "• Pernyataan 1 BENAR: Radar menggunakan gelombang mikro buatan (aktif) sehingga menembus awan dan malam hari<br>• Pernyataan 2 SALAH: Titik-garis-poligon adalah model data Vektor, bukan Raster<br>• Pernyataan 3 BENAR: Definisi fungsi analisis buffering spasial SIG<br>• Pernyataan 4 SALAH: Ukuran terkecil objek adalah Resolusi Spasial, bukan Spektral"
        },
        "hints": {
            "concept": "Radar SAR adalah sistem aktif tembus awan/malam. Titik-garis-poligon adalah data VEKTOR (bukan raster). Buffer membuat zona penyangga berjarak tertentu. Ukuran objek terkecil adalah resolusi spasial (resolusi spektral adalah jumlah saluran/panjang gelombang).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "geo-sim-34",
        "materi": "DINAMIKA KEPENDUDUKAN & KETENAGAKERJAAN",
        "topic": "Transisi Demografi, Struktur Penduduk, dan Piramida Penduduk",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai teori kependudukan dan struktur demografi!",
        "statements": [
            {
                "text": "Piramida penduduk konstruktif (berbentuk batu nisan / granat) mencerminkan angka kelahiran yang sangat rendah dan proporsi kelompok penduduk usia tua yang besar.",
                "correct": True
            },
            {
                "text": "Pada Tahap I Model Transisi Demografi, angka kelahiran dan angka kematian sama-sama sangat tinggi sehingga pertumbuhan penduduk alami bergerak mendekati nol.",
                "correct": True
            },
            {
                "text": "Bonus demografi tercapai secara optimal jika rasio ketergantungan (dependency ratio) berada pada posisi puncak tertinggi di atas 100.",
                "correct": False
            },
            {
                "text": "Pertumbuhan penduduk alami hanya memperhitungkan selisih antara angka kelahiran dan angka kematian tanpa memasukkan unsur migrasi neto.",
                "correct": True
            }
        ],
        "formula": {
            "title": "MODEL TRANSISI DEMOGRAFI DAN BONUS DEMOGRAFI",
            "latex": "\\text{Tahap I: High Stationary (CBR \\& CDR Tinggi)}, \\quad \\mathbf{\\text{Bonus Demografi}} \\implies \\mathbf{\\text{Dependency Ratio Minimum (< 50)}}, \\quad P_n = B - D",
            "legend": "• Pernyataan 1 BENAR: Ciri piramida konstruktif negara maju Eropa/Jepang<br>• Pernyataan 2 BENAR: Ciri masyarakat pra-industri tahap I transisi demografi<br>• Pernyataan 3 SALAH: Bonus demografi mensyaratkan rasio ketergantungan serendah mungkin (< 50), di mana usia produktif mendominasi<br>• Pernyataan 4 BENAR: Definisi pertumbuhan alami ($P_n = B - D$)"
        },
        "hints": {
            "concept": "Piramida konstruktif = kelahiran rendah, lansia tinggi. Tahap I transisi demografi = kelahiran dan kematian tinggi, pertumbuhan lambat. Bonus demografi terjadi saat dependency ratio rendah (<50), bukan tinggi di atas 100. Pertumbuhan alami = kelahiran - kematian.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    },
    {
        "id": "geo-sim-35",
        "materi": "PENGEMBANGAN WILAYAH & TATA RUANG",
        "topic": "Penataan Ruang Wilayah Nasional Berdasarkan UU No. 26/2007",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai sistem penataan ruang wilayah di Indonesia!",
        "statements": [
            {
                "text": "Rencana Tata Ruang Wilayah Nasional (RTRWN) berlaku selama 20 tahun dan dapat ditinjau kembali (direvisi) satu kali dalam 5 tahun.",
                "correct": True
            },
            {
                "text": "Kawasan Lindung ditetapkan dengan fungsi utama untuk dieksploitasi sumber daya tambangnya guna mendongkrak pendapatan asli daerah secara maksimal.",
                "correct": False
            },
            {
                "text": "Undang-Undang Penataan Ruang mewajibkan proporsi Ruang Terbuka Hijau (RTH) pada kawasan perkotaan minimal sebesar 30% dari luas wilayah kota.",
                "correct": True
            },
            {
                "text": "Kawasan Strategis Nasional (KSN) ditetapkan berdasarkan pertimbangan kedaulatan negara, pertahanan keamanan, pertumbuhan ekonomi, sosial budaya, dan lingkungan hidup.",
                "correct": True
            }
        ],
        "formula": {
            "title": "REGULASI PENATAAN RUANG (UU NO. 26 TAHUN 2007)",
            "latex": "\\begin{cases} \\text{RTRW:} & \\text{Masa Berlaku 20 Tahun, PK 5 Tahun Sekali} \\\\ \\mathbf{\\text{RTH Perkotaan:}} & \\mathbf{\\ge 30\\% \\ (20\\% \\text{ Publik} + 10\\% \\text{ Privat})} \\\\ \\mathbf{\\text{Kawasan Lindung:}} & \\mathbf{\\text{Konservasi Tanah \\& Air, Keanekaragaman Hayati, Perlindungan Lingkungan}} \\\\ \\text{KSN:} & \\text{Kedaulatan, Ekonomi, Sosbud, Lingkungan} \\end{cases}",
            "legend": "• Pernyataan 1 BENAR: Ketentuan jangka waktu RTRW menurut UU Penataan Ruang<br>• Pernyataan 2 SALAH: Kawasan lindung berfungsi utama mencegah kerusakan lingkungan dan bencana, bukan dieksploitasi tambang<br>• Pernyataan 3 BENAR: Pasal 29 UU No. 26/2007 menetapkan RTH kota minimal 30%<br>• Pernyataan 4 BENAR: Kriteria penentuan Kawasan Strategis Nasional"
        },
        "hints": {
            "concept": "RTRW berlaku 20 tahun ditinjau 5 tahun sekali. Kawasan lindung berfungsi melindungi kelestarian lingkungan (bukan dieksploitasi tambang). RTH kota minimal 30%. KSN mempertimbangkan kedaulatan, ekonomi, budaya, dan lingkungan.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    }
]
