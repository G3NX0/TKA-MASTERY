# -*- coding: utf-8 -*-
"""
geografi_data_hard.py
---------------------
25 Authentic Hard/Advanced Practice Questions for TKA 2026 Geografi (SMA/MA Soshum).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: geo-lat-h-01 .. geo-lat-h-25
"""

GEOGRAFI_HARD_ITEMS = [
    {
        "id": "geo-lat-h-01",
        "materi": "DINAMIKA LITOSFER & PEDOSFER",
        "topic": "Penentuan Jarak Episentrum Gempa Menggunakan Hukum Laska",
        "stem": "Stasiun seismologi Geofisika mencatat gelombang gempa bumi tektonik dengan data getaran sebagai berikut:\n- Gelombang Primer ($P$) pertama kali tiba pada pukul: $08.24'15''$ WIB\n- Gelombang Sekunder ($S$) menyusul tiba pada pukul: $08.28'45''$ WIB\nBerdasarkan Hukum Laska, jarak episentrum pusat gempa bumi tersebut dari stasiun seismologi pencatat adalah...",
        "correct": "$3.500 \\text{ km}$.",
        "distractors": [
            "$4.500 \\text{ km}$.",
            "$2.500 \\text{ km}$.",
            "$3.250 \\text{ km}$.",
            "$4.000 \\text{ km}$."
        ],
        "formula": {
            "title": "HUKUM LASKA UNTUK ESTIMASI JARAK EPISENTRUM",
            "latex": "\\begin{aligned} \\Delta & = \\left\\{ (S - P) - 1' \\right\\} \\times 1.000 \\text{ km} \\\\ S - P & = 08.28'45'' - 08.24'15'' = 4'30'' \\\\ \\Delta & = \\left( 4'30'' - 1' \\right) \\times 1.000 \\text{ km} = 3'30'' \\times 1.000 \\text{ km} \\\\ & = 3{,}5 \\times 1.000 \\text{ km} = \\mathbf{3.500 \\text{ km}} \\end{aligned}",
            "legend": "• $\\Delta$: Jarak stasiun pencatat ke episentrum<br>• $S - P$: Selisih waktu kedatangan gelombang sekunder dan primer<br>• $1'$: Konstanta waktu jeda standar (1 menit)"
        },
        "hints": {
            "concept": "Hukum Laska: Delta = {(S - P) - 1 menit} * 1.000 km. Selisih S - P = 4 menit 30 detik. Dikurangi 1 menit = 3 menit 30 detik (3,5 menit).",
            "execution": "Hitung: 3,5 * 1.000 km = 3.500 km."
        }
    },
    {
        "id": "geo-lat-h-02",
        "materi": "KONEKTIVITAS WILAYAH & TEORI GRAFIK",
        "topic": "Indeks Konektivitas Jaringan Transportasi Teori Grafik K.J. Kansky",
        "stem": "Sebuah kawasan agropolitan regional memiliki 6 simpul permukiman/kota ($v = 6$) yang dihubungkan oleh 9 ruas jalan raya arteri penghubung ($e = 9$). Menurut Teori Grafik K.J. Kansky, nilai Indeks Konektivitas Jaringan (Indeks Beta / $\\beta$) kawasan tersebut serta interpretasi tingkat aksesibilitasnya adalah...",
        "correct": "$\\beta = 1{,}50$, menunjukkan bahwa konektivitas transportasi antarwilayah tergolong tinggi karena memiliki banyak rute alternatif dan sirkulasi jaringan yang padat ($\\beta > 1$).",
        "distractors": [
            "$\\beta = 0{,}67$, menunjukkan bahwa jaringan transportasi sangat terisolasi dan masih berupa pola pohon sederhana cabang tunggal.",
            "$\\beta = 0{,}54$, menunjukkan bahwa sebagian besar simpul kota belum dapat dijangkau oleh kendaraan bermotor angkutan umum.",
            "$\\beta = 2{,}25$, menunjukkan bahwa wilayah tersebut telah mencapai kondisi jaringan heksagonal jenuh tanpa hambatan topografi.",
            "$\\beta = 1{,}00$, menunjukkan bahwa sistem transportasi berada pada ambang batas minimum tanpa kemungkinan memilih rute lain."
        ],
        "formula": {
            "title": "INDEKS KONEKTIVITAS TEORI GRAFIK KANSKY (INDEKS BETA)",
            "latex": "\\begin{aligned} \\beta & = \\frac{e}{v} = \\frac{9}{6} = \\mathbf{1{,}50} \\\\ \\beta < 1 & \\implies \\text{Jaringan Sederhana / Aksesibilitas Rendah} \\\\ \\beta = 1 & \\implies \\text{Jaringan Sirkuit Tunggal Sederhana} \\\\ \\beta > 1 & \\implies \\mathbf{\\text{Konektivitas Kompleks / Aksesibilitas Tinggi}} \\end{aligned}",
            "legend": "• $e$: Jumlah ruas/jalur jalan (_edges/links_)<br>• $v$: Jumlah titik/kota simpul (_vertices/nodes_)"
        },
        "hints": {
            "concept": "Indeks Beta Kansky: beta = e / v, di mana e = 9 dan v = 6. Nilai beta = 9 / 6 = 1,50. Karena beta > 1, wilayah memiliki konektivitas dan alternatif rute tinggi.",
            "execution": "Pilih: beta = 1,50, konektivitas tinggi dengan banyak rute alternatif."
        }
    },
    {
        "id": "geo-lat-h-03",
        "materi": "POLA KERUANGAN & PERTUMBUHAN WILAYAH",
        "topic": "Model Kausalitas Sirkuler Kumulatif Gunnar Myrdal",
        "stem": "Dalam teori polarisasi ekonomi Gunnar Myrdal (_Circular and Cumulative Causation_), pembentukan pusat pertumbuhan baru di kota inti dapat memicu dua kekuatan spasial yang saling bertolak belakang terhadap kawasan pedesaan sekitarnya: _backwash effects_ dan _spread effects_. Fenomena yang mencerminkan dominasi _backwash effects_ yang merugikan daerah pinggiran adalah...",
        "correct": "Terjadinya migrasi tenaga kerja produktif berpendidikan, pengalihan aliran modal tabungan lokal, serta tersedotnya bahan mentah dari pedesaan ke kota metropolitan yang memperlebar ketimpangan pembangunan antarwilayah.",
        "distractors": [
            "Peningkatan permintaan komoditas pangan lokal pedesaan yang menaikkan pendapatan riil petani dan menumbuhkan industri pengolahan kecil.",
            "Penyebaran inovasi teknologi budidaya pertanian modern dan fasilitas perbankan perintis dari kota besar ke pelosok desa.",
            "Relokasi pabrik manufaktur padat karya dari pusat kota metropolitan ke wilayah pedesaan untuk memanfaatkan upah buruh terjangkau.",
            "Keseimbangan pertumbuhan ekonomi antarprovinsi yang tercapai secara spontan melalui mekanisme pasar bebas tanpa intervensi negara."
        ],
        "formula": {
            "title": "DINAMIKA MYRDAL: BACKWASH VS SPREAD EFFECTS",
            "latex": "\\begin{cases} \\mathbf{\\text{Backwash Effects (Polarisasi Negatif):}} & \\text{Tenaga Ahli, Modal, \\& Bahan Baku Tersedot ke Pusat} \\implies \\mathbf{\\text{Ketimpangan Melebar}} \\\\ \\mathbf{\\text{Spread Effects (Penyebaran Positif):}} & \\text{Investasi, Teknologi, \\& Pasar Melimpah ke Pinggiran} \\implies \\text{Pemerataan Tumbuh} \\end{cases}",
            "legend": "• Tanpa intervensi kebijakan tata ruang aktif dari pemerintah, _backwash effects_ cenderung mengalahkan _spread effects_ di negara berkembang"
        },
        "hints": {
            "concept": "Backwash effect = efek pengurasan/polarisasi negatif dari pinggiran ke pusat (tenaga kerja muda tersedot, modal mengalir ke kota, daerah pinggiran tertinggal).",
            "execution": "Pilih opsi: migrasi tenaga kerja produktif, aliran modal tabungan, dan bahan mentah tersedot ke kota metropolitan memperlebar ketimpangan."
        }
    },
    {
        "id": "geo-lat-h-04",
        "materi": "MITIGASI BENCANA ALAM & KELAUTAN",
        "topic": "Kecepatan dan Waktu Tempuh Gelombang Tsunami Berdasarkan Kedalaman Laut",
        "stem": "Gempa tektonik dangkal berkekuatan $M_w = 7{,}8$ mengguncang dasar laut pada kedalaman rata-rata palung $d = 4.000 \\text{ meter}$. Jarak episentrum gempa tersebut ke garis pantai permukiman penduduk adalah sejauh $s = 200 \\text{ km}$. Jika percepatan gravitasi bumi $g = 9{,}8 \\text{ m/s}^2$ (dibulatkan $g \\approx 10 \\text{ m/s}^2$), kecepatan perambatan gelombang tsunami ($v$) di laut dalam serta estimasi waktu tiba gelombang pertama ($t$) di pantai adalah...",
        "correct": "$v = 200 \\text{ m/s}$ ($720 \\text{ km/jam}$) dan waktu tiba gelombang pertama di pantai sekitar $16{,}7 \\text{ menit}$ (16 menit 40 detik).",
        "distractors": [
            "$v = 100 \\text{ m/s}$ ($360 \\text{ km/jam}$) dan waktu tiba gelombang pertama di pantai sekitar $33{,}3 \\text{ menit}$.",
            "$v = 400 \\text{ m/s}$ ($1.440 \\text{ km/jam}$) dan waktu tiba gelombang pertama di pantai sekitar $8{,}3 \\text{ menit}$.",
            "$v = 50 \\text{ m/s}$ ($180 \\text{ km/jam}$) dan waktu tiba gelombang pertama di pantai sekitar $66{,}7 \\text{ menit}$.",
            "$v = 140 \\text{ m/s}$ ($504 \\text{ km/jam}$) dan waktu tiba gelombang pertama di pantai sekitar $23{,}8 \\text{ menit}$."
        ],
        "formula": {
            "title": "FORMULA GELOMBANG AIR DANGKAL TSUNAMI (AIRY SHALLOW WATER THEORY)",
            "latex": "\\begin{aligned} v & = \\sqrt{g \\cdot d} = \\sqrt{10 \\times 4.000} = \\sqrt{40.000} = \\mathbf{200 \\text{ m/s}} = \\mathbf{720 \\text{ km/jam}} \\\\ t & = \\frac{s}{v} = \\frac{200.000 \\text{ meter}}{200 \\text{ m/s}} = 1.000 \\text{ detik} = \\mathbf{16{,}67 \\text{ menit}} \\ (\\mathbf{16'40''}) \\end{aligned}",
            "legend": "• $v$: Kecepatan gelombang tsunami di laut dalam ($m/s$)<br>• $d$: Kedalaman kolom air laut ($m$)<br>• Saat mendekati pantai dangkal, kecepatan $v$ turun drastis tetapi amplitudo tinggi gelombang $H$ membubung tinggi (efek _shoaling_)"
        },
        "hints": {
            "concept": "Rumus kecepatan gelombang tsunami: v = sqrt(g * d) = sqrt(10 * 4.000) = sqrt(40.000) = 200 m/s. Waktu tempuh t = s / v = 200.000 m / 200 m/s = 1.000 s = 16,67 menit.",
            "execution": "Pilih: v = 200 m/s (720 km/jam) dan waktu tiba 16,7 menit (16 menit 40 detik)."
        }
    },
    {
        "id": "geo-lat-h-05",
        "materi": "POLA KERUANGAN & PERTUMBUHAN WILAYAH",
        "topic": "Model Gravitasi Spasial Berbobot Konektivitas Ekonomi",
        "stem": "Dalam perencanaan tata ruang wilayah, kekuatan interaksi gravitasi antara dua pusat pertumbuhan kota tidak hanya ditentukan oleh populasi massa fisik semata, melainkan juga berbanding lurus dengan produk domestik regional bruto (PDRB) serta berbanding terbalik dengan kuadrat jarak tempuh efektif. Jika jarak fisik antara Kota X dan Kota Y tetap sama, namun dibangun jalan tol bebas hambatan dan jalur kereta rel listrik cepat yang memotong waktu perjalanan menjadi setengahnya ($1/2$ kali semula), kekuatan interaksi spasial efektif ($I_{XY}$) antar kedua kota akan meningkat menjadi...",
        "correct": "$4 \\text{ kali lipat}$ dari kekuatan interaksi semula, karena daya tarik spasial berbanding terbalik secara kuadrat terhadap jarak/waktu tempuh ($I \\propto 1/d^2$).",
        "distractors": [
            "$2 \\text{ kali lipat}$ dari kekuatan interaksi semula, karena hubungan antara waktu perjalanan dan interaksi bersifat linear searah.",
            "$8 \\text{ kali lipat}$ dari kekuatan interaksi semula, mengikuti fungsi pertumbuhan kubik volume mobilitas penumpang.",
            "$16 \\text{ kali lipat}$ dari kekuatan interaksi semula, akibat pelipatgandaan eksponensial arus pertukaran komoditas.",
            "Tetap sama tidak berubah, karena populasi absolut penduduk di kedua kota tidak mengalami penambahan instan."
        ],
        "formula": {
            "title": "HUKUM GRAVITASI SPASIAL DENGAN JARAK RELATIF / WAKTU TEMPUH",
            "latex": "\\begin{aligned} I_{XY} & = k \\cdot \\frac{M_X \\cdot M_Y}{d^2} \\\\ d_2 & = \\frac{1}{2} d_1 \\implies I_2 = k \\cdot \\frac{M_X \\cdot M_Y}{\\left( \\frac{1}{2} d_1 \\right)^2} = k \\cdot \\frac{M_X \\cdot M_Y}{\\frac{1}{4} d_1^2} = \\mathbf{4 \\cdot I_1} \\end{aligned}",
            "legend": "• Pemotongan waktu tempuh efektif mereduksi friksi spasial (_friction of distance_) secara kuadratis"
        },
        "hints": {
            "concept": "Hukum gravitasi Reilly/Carey: Interaksi berbanding terbalik dengan kuadrat jarak (I ~ 1/d^2). Jika d menjadi 1/2 d, maka I menjadi 1 / (1/2)^2 = 4 kali lipat.",
            "execution": "Pilih: 4 kali lipat dari interaksi semula karena berbanding terbalik kuadratik."
        }
    },
    {
        "id": "geo-lat-h-06",
        "materi": "DINAMIKA ATMOSFER & PERUBAHAN IKLIM",
        "topic": "Sirkulasi Atmosferik Tiga Sel Global dan Sabuk Tekanan Subtropis",
        "stem": "Model sirkulasi atmosfer bumi skala global terdiri dari tiga sel meridional utama pada masing-masing belahan bumi: Sel Hadley, Sel Ferrel, dan Sel Polar. Fenomena subsidensi (gerak turun massa udara dingin dan kering secara masif) pada batas konvergensi antara Sel Hadley dan Sel Ferrel di lintang $30^\\circ \\text{ LU/LS}$ mengakibatkan terbentuknya...",
        "correct": "Sabuk tekanan tinggi subtropis (_Subtropical High Pressure Belt_ / _Horse Latitudes_) yang beriklim sangat kering, langit cerah tanpa awan, dan menjadi lokasi persebaran gurun-gurun pasir terbesar di dunia.",
        "distractors": [
            "Zona konvergensi antartropis (ITCZ) dengan aktivitas awan konvektif cumulonimbus ekstrem dan curah hujan harian lebat.",
            "Palung siklon kutub bertekanan udara sangat rendah dengan badai salju frontal abadi sepanjang tahun.",
            "Sabuk angin muson periodik yang berbalik arah setiap enam bulan sekali mengikuti deklinasi semu matahari.",
            "Celah lapisan troposfer terbuka yang memungkinkan radiasi sinar ultraviolet langsung membakar permukaan samudra."
        ],
        "formula": {
            "title": "SIRKULASI TIGA SEL GLOBAL DAN SABUK GURUN DUNIA",
            "latex": "\\begin{aligned} \\text{0}^\\circ \\text{ (Ekuator):} & \\quad \\text{Tekanan Rendah Termal (Doldrums / ITCZ) } \\implies \\text{Hujan Hutan Tropis} \\\\ \\mathbf{30^\\circ \\text{ LU/LS:}} & \\quad \\mathbf{\\text{Subsidensi Udara } \\implies \\text{Tekanan Tinggi Dinamis (Subtropical High)}} \\implies \\mathbf{\\text{Gurun Pasir}} \\\\ 60^\\circ \\text{ LU/LS:} & \\quad \\text{Konvergensi Polar Front } \\implies \\text{Tekanan Rendah Subpolar} \\\\ 90^\\circ \\text{ (Kutub):} & \\quad \\text{Tekanan Tinggi Termal Kutub} \\end{aligned}",
            "legend": "• Udara yang naik di ekuator mendingin dan tenggelam di lintang 30°, mengalami pemanasan adiabatik turun sehingga kelembapan relatif anjlok dan mencegah kondensasi awan"
        },
        "hints": {
            "concept": "Di lintang 30 LU/LS, udara dari Sel Hadley turun (subsidensi), menciptakan sabuk tekanan tinggi subtropis (horse latitudes) berawan minim -> terbentuk gurun pasir terbesar dunia (Sahara, Arab, Australia).",
            "execution": "Pilih: Sabuk tekanan tinggi subtropis yang sangat kering, tanpa awan, lokasi gurun pasir dunia."
        }
    },
    {
        "id": "geo-lat-h-07",
        "materi": "DINAMIKA HIDROSFER & IKLIM GLOBAL",
        "topic": "Dinamika ENSO: El Niño Southern Oscillation dan Dampaknya di Indonesia",
        "stem": "Fenomena El Niño terjadi akibat anomali interaksi laut-atmosfer di Samudra Pasifik ekuatorial. Kondisi fisik oseanografi dan atmosferik yang menandai fase El Niño serta dampaknya yang nyata terhadap dinamika cuaca di wilayah kepulauan Indonesia adalah...",
        "correct": "Pelemahan Angin Pasat Timur, pergeseran massa air hangat (_Warm Pool_) ke arah timur menuju pantai barat Peru, terhentinya fenomena _upwelling_ di Pasifik Timur, dan terbentuknya sel tekanan tinggi di atas benua maritim Indonesia yang memicu kemarau ekstrem berkepanjangan serta risiko kebakaran hutan.",
        "distractors": [
            "Penguatan drastis Angin Pasat Timur yang mendorong seluruh air panas ke kepulauan Indonesia dan menimbulkan banjir bandang non-stop.",
            "Penurunan suhu muka laut global hingga memicu glasiasi kutub mini dan penurunan muka air laut di selat Malaka.",
            "Peningkatan intensitas siklon tropis secara simultan tepat di atas garis khatulistiwa khatulistiwa pulau Kalimantan.",
            "Terhentinya sirkulasi arus termohalin kutub yang mengakibatkan seluruh perairan terumbu karang Indonesia membeku."
        ],
        "formula": {
            "title": "MEKANISME ANOMALI SIRKULASI WALKER SAAT EL NIÑO",
            "latex": "\\begin{cases} \\mathbf{\\text{Kondisi Normal / La Niña:}} & \\text{Pasat Kuat} \\implies \\text{Air Hangat di Barat (Indonesia: Konveksi/Hujan)} \\\\ \\mathbf{\\text{Fase El Niño:}} & \\text{Pasat Melemah} \\implies \\text{Air Hangat Bergeser ke Pasifik Timur (Peru)} \\\\ & \\implies \\mathbf{\\text{Tekanan Tinggi di Indonesia } (\\text{Subsidensi/Subsidence})} \\implies \\mathbf{\\text{Kekeringan Ekstrem}} \\end{cases}",
            "legend": "• Indeks SOI (Southern Oscillation Index) bernilai negatif kuat selama peristiwa El Niño"
        },
        "hints": {
            "concept": "El Nino = Angin Pasat melemah, massa air hangat pindah ke Pasifik Timur (Peru). Di Indonesia terjadi subsidensi udara (tekanan tinggi), minim awan, memicu kemarau panjang.",
            "execution": "Pilih opsi: Pelemahan Angin Pasat Timur, pergeseran warm pool ke timur (Peru), dan sel tekanan tinggi di atas Indonesia memicu kemarau ekstrem."
        }
    },
    {
        "id": "geo-lat-h-08",
        "materi": "DINAMIKA HIDROSFER & IKLIM GLOBAL",
        "topic": "Sirkulasi Arus Termohalin Global (The Great Ocean Conveyor Belt)",
        "stem": "Sirkulasi arus termohalin global (_Global Conveyor Belt_) mengalirkan massa air laut melintasi seluruh samudra dunia dalam skala waktu ratusan hingga ribuan tahun. Penggerak utama (_engine_) yang memicu pembentukan massa air laut dalam di kawasan Atlantik Utara dekat Greenland dan Laut Norwegia adalah...",
        "correct": "Pendinginan suhu air permukaan secara ekstrem oleh udara kutub yang disertai pengeluaran garam saat pembentukan es laut (_brine rejection_), sehingga densitas air meningkat drastis dan massa air tenggelam (_downwelling_) menuju dasar samudra.",
        "distractors": [
            "Pemanasan radiasi matahari intensif di wilayah Arktik yang mencairkan gletser air tawar dan membuatnya tenggelam cepat.",
            "Aktivitas gempa bumi vulkanik di pematang tengah samudra yang menyedot air laut ke kantung magma bawah kerak.",
            "Dorongan mekanik pasang surut gravitasi bulan purnama yang menekan permukaan air laut hingga mencapai palung laut.",
            "Tiupan angin topan taifun berkekuatan dahsyat yang mengaduk sedimen lumpur dasar laut hingga menaikkan salinitas permukaan."
        ],
        "formula": {
            "title": "PERSAMAAN DENSITAS AIR LAUT DAN SINKING ATLANTIK UTARA",
            "latex": "\\begin{aligned} \\rho_{\\text{air laut}} & = f(T \\downarrow, \\ S \\uparrow, \\ P \\uparrow) \\\\ \\text{Suhu Dingin Polar } (T \\downarrow) + \\text{Brine Rejection } (S \\uparrow) & \\implies \\mathbf{\\text{Densitas Sangat Tinggi } (\\rho \\uparrow\\uparrow)} \\implies \\mathbf{\\text{Downwelling (Tenggelam)}} \\\\ & \\implies \\text{Pembentukan NADW (North Atlantic Deep Water)} \\end{aligned}",
            "legend": "• Termohalin: Thermo (temperatur) + Haline (salinitas/kandungan garam)<br>• Arus dasar dingin mengalir ke selatan menuju Samudra Hindia dan Pasifik sebelum mengalami upwelling"
        },
        "hints": {
            "concept": "Arus termohalin digerakkan oleh perbedaan densitas (suhu dingin + salinitas tinggi). Di Atlantik Utara, pembentukan es melepaskan garam (brine rejection), membuat air sangat dingin dan asin, lalu tenggelam (downwelling).",
            "execution": "Pilih: Pendinginan suhu ekstrem dan pengeluaran garam (brine rejection) meningkatkan densitas sehingga air tenggelam (downwelling)."
        }
    },
    {
        "id": "geo-lat-h-09",
        "materi": "DINAMIKA ATMOSFER & PERUBAHAN IKLIM",
        "topic": "Neraca Radiasi Bumi, Albedo Permukaan, dan Efek Rumah Kaca",
        "stem": "Permukaan bumi dan atmosfer mempertahankan keseimbangan energi termal melalui neraca radiasi. Jika tutupan es dan salju di kutub mengalami pelebaran albedo luas ($A = 0{,}85$), sedangkan lautan terbuka memiliki albedo rendah ($A = 0{,}08$), umpan balik iklim (_climate feedback loop_) yang terjadi ketika terjadi pemanasan global dan pencairan es kutub secara masif adalah...",
        "correct": "Umpan balik positif es-albedo (_ice-albedo positive feedback_), di mana es mencair menjadi laut terbuka ber-albedo rendah, menyebabkan penyerapan radiasi matahari bertambah, sehingga suhu bumi makin panas dan memicu pencairan es yang lebih masif.",
        "distractors": [
            "Umpan balik negatif otomatis, di mana pelelehan es mendinginkan lautan secara permanen dan memicu zaman es baru seketika.",
            "Peningkatan radiasi gelombang pendek bumi yang dipantulkan langsung ke luar angkasa sehingga iklim menjadi stabil.",
            "Penurunan kapasitas kalor air laut yang menyebabkan samudra membeku kembali dalam kurun waktu satu musim dingin.",
            "Pergeseran orbit elips bumi mengelilingi matahari yang memperjauh jarak aphelion bumi secara drastis."
        ],
        "formula": {
            "title": "MEKANISME ICE-ALBEDO POSITIVE FEEDBACK LOOP",
            "latex": "\\text{Suhu Global } \\uparrow \\implies \\text{Es Mencair} \\implies \\text{Albedo Wilayah } \\downarrow (0{,}85 \\to 0{,}08) \\implies \\mathbf{\\text{Serapan Radiasi } \\uparrow\\uparrow} \\implies \\mathbf{\\text{Pemanasan Makin Parah}}" ,
            "legend": "• Albedo ($A$): Fraksi radiasi matahari datang yang dipantulkan kembali tanpa diserap ($0 \\le A \\le 1$)<br>• Umpan balik positif memperkuat gangguan awal alih-alih meredamnya"
        },
        "hints": {
            "concept": "Ice-albedo positive feedback: Es (albedo tinggi) mencair -> berubah jadi air laut (albedo rendah) -> serapan panas meningkat -> suhu makin panas -> es mencair makin banyak.",
            "execution": "Pilih opsi: Umpan balik positif es-albedo, penyerapan radiasi meningkat, memicu pencairan es yang lebih masif."
        }
    },
    {
        "id": "geo-lat-h-10",
        "materi": "DINAMIKA LITOSFER & PEDOSFER",
        "topic": "Model Prediksi Erosi Tanah USLE (Universal Soil Loss Equation)",
        "stem": "Dalam evaluasi konservasi lahan perbukitan kritis di kawasan hulu DAS Citarum, estimasi laju kehilangan tanah per tahun dihitung menggunakan rumus USLE Wischmeier-Smith ($A = R \\cdot K \\cdot LS \\cdot C \\cdot P$). Jika seorang petani mengubah praktik bercocok tanam dari sistem ladang terbuka searah lereng ($C = 0{,}70; P = 1{,}0$) menjadi sistem agroforestri tumpang sari berteras bangku sempurna dengan drainase rorak ($C = 0{,}10; P = 0{,}14$), penurunan persentase laju erosi tanah ($A$) yang dicapai adalah sebesar...",
        "correct": "$98\\%$ penurunan erosi (laju erosi baru tinggal $2\\%$ dari laju erosi semula).",
        "distractors": [
            "$50\\%$ penurunan erosi.",
            "$70\\%$ penurunan erosi.",
            "$86\\%$ penurunan erosi.",
            "$90\\%$ penurunan erosi."
        ],
        "formula": {
            "title": "FORMULA USLE (UNIVERSAL SOIL LOSS EQUATION)",
            "latex": "\\begin{aligned} A_1 & = R \\cdot K \\cdot LS \\cdot (C_1 \\cdot P_1) = R \\cdot K \\cdot LS \\cdot (0{,}70 \\times 1{,}0) = 0{,}70 \\cdot (R \\cdot K \\cdot LS) \\\\ A_2 & = R \\cdot K \\cdot LS \\cdot (C_2 \\cdot P_2) = R \\cdot K \\cdot LS \\cdot (0{,}10 \\times 0{,}14) = 0{,}014 \\cdot (R \\cdot K \\cdot LS) \\\\ \\frac{A_2}{A_1} & = \\frac{0{,}014}{0{,}70} = 0{,}02 = \\mathbf{2\\%} \\implies \\mathbf{\\text{Penurunan Erosi}} = 100\\% - 2\\% = \\mathbf{98\\%}} \\end{aligned}",
            "legend": "• $R$: Erosivitas hujan, $K$: Erodibilitas tanah, $LS$: Faktor panjang & kemiringan lereng<br>• $C$: Pengelolaan tanaman tutupan, $P$: Praktik tindakan konservasi tanah mekanik"
        },
        "hints": {
            "concept": "Rasio erosi ditentukan oleh perkalian C * P. Kondisi 1: 0,70 * 1,0 = 0,70. Kondisi 2: 0,10 * 0,14 = 0,014. Rasio A2 / A1 = 0,014 / 0,70 = 0,02 (2%). Penurunan erosi = 100% - 2% = 98%.",
            "execution": "Hitung: 100% - (0,014 / 0,70 * 100%) = 98% penurunan erosi."
        }
    },
    {
        "id": "geo-lat-h-11",
        "materi": "PENGEMBANGAN WILAYAH & INDUSTRI",
        "topic": "Model Lokasi Industri Biaya Transportasi Minimum Alfred Weber",
        "stem": "Dalam Teori Lokasi Industri Alfred Weber, penentuan titik lokasi pabrik optimal didasarkan pada prinsip biaya transportasi total minimum dengan memperhitungkan Indeks Material ($IM$). Sebuah industri semen membutuhkan $2{,}5 \\text{ ton}$ batu gamping dari Tambang $R_1$ dan $0{,}5 \\text{ ton}$ pasir silika dari Tambang $R_2$ untuk menghasilkan $1 \\text{ ton}$ produk semen jadi yang akan dipasarkan ke Kota $M$. Nilai Indeks Material ($IM$) industri tersebut serta rekomendasi penempatan lokasi pabrik yang paling efisien adalah...",
        "correct": "$IM = 3{,}0$ ($IM > 1$), sehingga industri bersifat _weight-losing_ dan lokasi pabrik harus ditempatkan merapat ke wilayah sumber bahan baku tambang (_raw material oriented_).",
        "distractors": [
            "$IM = 0{,}33$ ($IM < 1$), sehingga industri bersifat _weight-gaining_ dan pabrik harus dibangun merapat ke kota pasar konsumen.",
            "$IM = 1{,}0$, sehingga biaya transportasi bersifat netral dan pabrik bebas didirikan di mana saja sepanjang jalur jalan.",
            "$IM = 3{,}0$, namun pabrik tetap harus didirikan di pusat kota pasar konsumen untuk menghindari biaya sewa tanah pinggiran.",
            "$IM = 0{,}75$, sehingga lokasi pabrik wajib ditempatkan tepat di tengah-tengah antara tambang dan pasar secara simetris."
        ],
        "formula": {
            "title": "TEORI LOKASI INDUSTRI WEBER: INDEKS MATERIAL (IM)",
            "latex": "\\begin{aligned} IM & = \\frac{\\text{Berat Bahan Baku Total}}{\\text{Berat Produk Jadi}} = \\frac{2{,}5 + 0{,}5}{1{,}0} = \\frac{3{,}0}{1{,}0} = \\mathbf{3{,}0} \\\\ IM > 1 & \\implies \\mathbf{\\text{Industri Hilang Bobot (Weight-Losing)}} \\implies \\mathbf{\\text{Dekat Bahan Baku (Raw Material Oriented)}} \\\\ IM < 1 & \\implies \\text{Industri Tambah Bobot (Weight-Gaining)} \\implies \\text{Dekat Pasar (Market Oriented)} \\\\ IM = 1 & \\implies \\text{Lokasi Bebas (Footloose Industry)} \\end{aligned}",
            "legend": "• Menempatkan pabrik dekat tambang memangkas ongkos angkut 3 ton bahan mentah yang bobotnya menyusut drastis menjadi 1 ton produk jadi"
        },
        "hints": {
            "concept": "Indeks Material (IM) = Berat bahan baku / Berat produk jadi = (2,5 + 0,5) / 1,0 = 3,0. Karena IM > 1 (weight-losing), pabrik harus dekat sumber bahan baku tambang.",
            "execution": "Pilih: IM = 3,0 (IM > 1), weight-losing, orientasi mendekati bahan baku."
        }
    },
    {
        "id": "geo-lat-h-12",
        "materi": "POLA KERUANGAN & PERTUMBUHAN WILAYAH",
        "topic": "Teori Kutub Pertumbuhan (Growth Pole) François Perroux dan Boudeville",
        "stem": "Konsep Kutub Pertumbuhan (_Pôles de Croissance_) yang digagas oleh ekonom regional François Perroux dan kemudian dikembangkan ke dimensi geografis spasial oleh Jacques Boudeville menekankan bahwa pertumbuhan ekonomi tidak muncul di sembarang tempat secara serentak. Ciri fundamental dari 'industri pendorong' (_propulsive / leading industry_) yang menjadi motor penggerak kutub pertumbuhan adalah...",
        "correct": "Memiliki tingkat inovasi dan adopsi teknologi tinggi, pertumbuhan output jauh di atas rata-rata nasional, serta memiliki keterkaitan ekonomi ke belakang (_backward linkages_) dan ke depan (_forward linkages_) yang sangat kuat dengan sektor-sektor industri pendukung lainnya.",
        "distractors": [
            "Bergerak pada sektor ekstraktif primer subsisten dengan pasar tertutup yang tidak memerlukan keterlibatan perbankan komersial.",
            "Beroperasi menggunakan padat karya manual tanpa mekanisasi agar menyerap seluruh pengangguran tanpa menghasilkan laba komersial.",
            "Hanya memproduksi komoditas barang konsumsi akhir yang dibagikan secara gratis kepada masyarakat miskin sekitar pabrik.",
            "Memiliki ketergantungan $100\\%$ pada subsidi APBN seumur hidup tanpa kemampuan bersaing di pasar ekspor internasional."
        ],
        "formula": {
            "title": "KARAKTERISTIK INDUSTRI PENDORONG KUTUB PERTUMBUHAN",
            "latex": "\\begin{cases} \\mathbf{\\text{Inovasi \\& Skala Ekonomi:}} & \\text{Efisiensi tinggi, elastisitas pendapatan besar} \\\\ \\mathbf{\\text{Backward Linkages (Keterkaitan ke Belakang):}} & \\text{Memicu permintaan bahan mentah, suku cadang, logistik} \\\\ \\mathbf{\\text{Forward Linkages (Keterkaitan ke Depan):}} & \\text{Memasok produk setengah jadi untuk industri hilir baru} \\\\ \\mathbf{\\text{Agglomeration Economies:}} & \\text{Menarik klaster penyedia jasa keuangan, talenta, \\& infrastruktur} \\end{cases}",
            "legend": "• Kutub pertumbuhan mentransformasikan struktur ruang kawasan di sekitarnya melalui efek pengganda (_multiplier effect_)"
        },
        "hints": {
            "concept": "Leading industry kutub pertumbuhan Perroux: inovatif, tumbuh pesat di atas rata-rata, memiliki backward linkage (menarik pemasok hulu) dan forward linkage (mendorong industri hilir) yang kuat.",
            "execution": "Pilih: inovasi tinggi, output di atas rata-rata nasional, keterkaitan ke belakang dan ke depan sangat kuat."
        }
    },
    {
        "id": "geo-lat-h-13",
        "materi": "POLA KERUANGAN DESA & KOTA",
        "topic": "Komparasi Model Struktur Ruang Kota: Burgess, Hoyt, dan Harris-Ullman",
        "stem": "Perkembangan morfologi struktur internal kota dianalisis melalui berbagai model klasik tata ruang. Karakteristik pembeda utama antara Teori Konsentris (_Burgess_), Teori Sektoral (_Hoyt_), dan Teori Inti Berganda (_Harris-Ullman_) dalam menjelaskan pola zonasi permukiman kelas atas dan zona industri manufaktur adalah...",
        "correct": "Burgess menempatkan permukiman kelas atas di zona lingkaran terluar (_commuter zone_), Hoyt menempatkan permukiman kelas atas membentang mengikuti koridor jalur transportasi utama terbaik, sedangkan Harris-Ullman menyatakan kota tidak berpaku pada satu pusat melainkan memiliki banyak nukleus/inti kegiatan terpisah.",
        "distractors": [
            "Burgess menyatakan kawasan industri selalu berada di pusat kota, Hoyt menempatkannya di pinggiran danau, dan Harris-Ullman menolak adanya kawasan industri.",
            "Hoyt menempatkan kelas buruh rendah di sepanjang rute pemandangan alam terbaik, sedangkan Burgess menempatkan elit kaya di samping pabrik kumuh.",
            "Harris-Ullman mengasumsikan seluruh kota di dunia berbentuk lingkaran simetris sempurna yang ditarik dari satu titik balai kota.",
            "Ketiga teori tersebut memiliki asumsi yang identik mengenai peran mutlak topografi pegunungan dalam membatasi pemekaran kota."
        ],
        "formula": {
            "title": "KOMPARASI TIGA TEORI STRUKTUR RUANG KOTA KLASIK",
            "latex": "\\begin{cases} \\mathbf{\\text{1. Teori Konsentris (Burgess, 1925):}} & \\text{Pola melingkar konsentris: CBD } \\to \\text{Transisi } \\to \\text{Pekerja } \\to \\text{Menengah } \\to \\mathbf{\\text{Commuter}} \\\\ \\mathbf{\\text{2. Teori Sektoral (Hoyt, 1939):}} & \\text{Pola baji / sektor mengikuti } \\mathbf{\\text{Rute Jaringan Transportasi Utama}} \\\\ \\mathbf{\\text{3. Teori Inti Berganda (Harris-Ullman, 1945):}} & \\mathbf{\\text{Banyak Pusat Pertumbuhan (Multiple Nuclei)}} \\text{ terpisah sesuai aglomerasi} \\end{cases}",
            "legend": "• Burgess: ekspansi radial; Hoyt: pengaruh aksesibilitas koridor; Harris-Ullman: desentralisasi fungsi kota modern"
        },
        "hints": {
            "concept": "Burgess = lingkaran konsentris (zona komuter terluar). Hoyt = sektor/baji mengikuti koridor jalur transportasi. Harris-Ullman = banyak inti/nukleus kegiatan yang terpisah.",
            "execution": "Pilih: Burgess zona lingkaran terluar, Hoyt membentang sepanjang jalur transportasi, Harris-Ullman banyak inti terpisah."
        }
    },
    {
        "id": "geo-lat-h-14",
        "materi": "SISTEM INFORMASI GEOGRAFIS (SIG)",
        "topic": "Analisis Jaringan Spasial SIG: Pemodelan Rute Tercepat (Shortest Path)",
        "stem": "Dalam Sistem Informasi Geografis (SIG) terapan untuk manajemen logistik kebencanaan, fitur analisis jaringan (_Network Analysis_) digunakan untuk menentukan rute evakuasi dan pengiriman bantuan logistik tercepat dari posko utama ke lokasi pengungsian. Algoritma matematis dan struktur data vektor topologis yang digunakan oleh perangkat lunak SIG untuk menghitung jalur terpendek (_shortest path_) berdasarkan friksi hambatan jalan (kecepatan, kemacetan, lebar jalan) adalah...",
        "correct": "Algoritma Dijkstra (atau $A^*$) yang diterapkan pada model data vektor jaringan garis bertopologi (_network graph_) dengan atribut bobot impedansi per ruas jalan.",
        "distractors": [
            "Algoritma K-Means Clustering yang diterapkan pada citra raster tutupan vegetasi hutan lindung tanpa garis jalan.",
            "Model Elevasi Digital TIN yang menghitung volume galian dan timbunan tebing lereng bukit vulkanik.",
            "Interpolasi Spasial Inverse Distance Weighting (IDW) untuk mengukur sebaran polusi debu udara di perempatan jalan.",
            "Transformasi Fourier Cepat yang diterapkan pada citra radar sentinel untuk mendeteksi kelembapan tanah sawah."
        ],
        "formula": {
            "title": "JARINGAN TOPOLOGIS DAN BOBOT IMPEDANSI RUTE SIG",
            "latex": "\\begin{aligned} \\text{Total Waktu Tempuh } (T) & = \\sum_{i=1}^{n} \\frac{L_i}{V_i \\cdot (1 - K_i)} + \\sum_{j=1}^{m} P_j \\\\ \\text{Algoritma Pencarian:} & \\quad \\text{Dijkstra} / A^* \\implies \\min \\left( \\text{Total Cost / Impedance} \\right) \\end{aligned}",
            "legend": "• $L_i$: Panjang ruas segmen, $V_i$: Batas kecepatan ruas, $K_i$: Koefisien kemacetan, $P_j$: Penalti belokan/lampu lalu lintas di persimpangan"
        },
        "hints": {
            "concept": "Analisis rute terpendek/tercepat SIG menggunakan Algoritma Dijkstra / A* pada data vektor topologi garis (edges & nodes) dengan atribut bobot impedansi (panjang ruas, kecepatan, hambatan).",
            "execution": "Pilih: Algoritma Dijkstra (atau A*) pada model data vektor jaringan garis bertopologi dengan atribut bobot impedansi."
        }
    },
    {
        "id": "geo-lat-h-15",
        "materi": "PENGINDERAAN JAUH & FOTOGRAMETRI",
        "topic": "Koreksi Geometrik, Radiometrik, dan Orto-rektifikasi Citra Satelit",
        "stem": "Citra mentah satelit penginderaan jauh resolusi tinggi sering kali mengalami distorsi geometrik akibat variasi ketinggian topografi permukaan bumi (relief displacement), kelengkungan bumi, dan sudut kemiringan sensor saat perekaman. Tahapan pemrosesan digital yang wajib dilakukan dengan memanfaatkan data Model Elevasi Digital (DEM) dan Titik Kontrol Lapangan (GCP) untuk menghasilkan citra tegak ortofoto yang memiliki skala seragam di seluruh lembar peta adalah...",
        "correct": "Orto-rektifikasi geometrik (_Orthorectification_), yang mengoreksi pergeseran letak piksel akibat perbedaan elevasi topografi sehingga citra satelit memiliki karakteristik proyeksi ortogonal seperti peta garis.",
        "distractors": [
            "Penajaman kontras kontras histogram linier yang hanya mengubah nilai kecerahan visual warna tanpa memperbaiki posisi spasial.",
            "Koreksi radiometrik kalibrasi atmosferik _Dark Object Subtraction_ (DOS) untuk menghilangkan hamburan aerosol cahaya matahari.",
            "Klasifikasi piksel tak terbimbing (Unsupervised Classification) menggunakan algoritma ISODATA untuk memisahkan jenis vegetasi.",
            "Penyusunan piramida piramida spasial piksel untuk mempercepat proses visualisasi data di layar monitor komputer."
        ],
        "formula": {
            "title": "PRINSIP PERGESERAN RELIEF DAN ORTO-REKTIFIKASI",
            "latex": "\\begin{aligned} \\text{Pergeseran Relief Mentah:} & \\quad d = \\frac{r \\cdot h}{H} \\\\ \\text{Orto-rektifikasi:} & \\quad [X, Y, Z]_{\\text{DEM + GCP}} \\xrightarrow{\\text{Koreksi Matriks Kolinier}} [X_{\\text{orto}}, Y_{\\text{orto}}] \\end{aligned}",
            "legend": "• $d$: Besar pergeseran letak objek pada foto udara/citra miring<br>• $h$: Ketinggian objek relatif terhadap bidang datum, $H$: Tinggi terbang wahana, $r$: Jarak radial dari pusat foto"
        },
        "hints": {
            "concept": "Koreksi distorsi geometrik akibat variasi relief topografi dengan bantuan DEM dan GCP menghasilkan citra tegak seragam skala disebut Orto-rektifikasi (Orthorectification).",
            "execution": "Pilih: Orto-rektifikasi geometrik (Orthorectification)."
        }
    },
    {
        "id": "geo-lat-h-16",
        "materi": "PENGINDERAAN JAUH & SISTEM INFORMASI GEOGRAFIS",
        "topic": "Klasifikasi Multispektral Digital: Supervised vs Unsupervised",
        "stem": "Dalam pemetaan penutup lahan tematik berbasis citra satelit multispektral (misalnya Sentinel-2 atau Landsat-9), analis SIG memilih metode Klasifikasi Terbimbing (_Supervised Classification_) menggunakan algoritma _Maximum Likelihood Classifier_ (MLC). Prinsip kerja fundamental dari metode klasifikasi terbimbing ini adalah...",
        "correct": "Analis membuat sampel area pelatihan (_training areas/areas of interest_) berdasarkan survei lapangan untuk tiap kelas tutupan lahan, kemudian komputer menghitung probabilitas statistik piksel untuk dimasukkan ke dalam kelas yang paling sesuai.",
        "distractors": [
            "Komputer secara otomatis mengelompokkan piksel murni berdasarkan kedekatan nilai spektral tanpa perlu pengetahuan atau input awal dari analis manusia.",
            "Analis menelusuri batas persil tanah secara manual menggunakan kursor digitasi poligon di atas layar komputer tanpa melibatkan statistik multispektral.",
            "Komputer menghapus seluruh spektrum inframerah dan hanya menggunakan saluran cahaya tampak merah, hijau, biru untuk membedakan bangunan dan air.",
            "Klasifikasi dilakukan dengan mengukur suhu panas termal objek di malam hari untuk menentukan jenis batuan beku dasar litosfer."
        ],
        "formula": {
            "title": "KOMPARASI METODE KLASIFIKASI CITRA DIGITAL",
            "latex": "\\begin{cases} \\mathbf{\\text{Terbimbing (Supervised - MLC):}} & \\text{Training Area Analis} \\implies \\text{Fungsi Kerapatan Probabilitas Gauss} \\implies \\text{Piksel Ditugaskan} \\\\ \\mathbf{\\text{Tak Terbimbing (Unsupervised):}} & \\text{Algoritma Komputer (K-Means / ISODATA)} \\implies \\text{Klasterisasi Alami Spektral Otomatis} \\end{cases}",
            "legend": "• Maximum Likelihood mengasumsikan distribusi normal spektral pada setiap saluran (_bands_) dari kelas sampel"
        },
        "hints": {
            "concept": "Supervised classification: analis membuat sampel area pelatihan (training area) dari lapangan -> algoritma menghitung probabilitas statistik untuk mengklasifikasikan piksel ke kelas yang paling mirip.",
            "execution": "Pilih: Analis membuat sampel area pelatihan (training areas), komputer menghitung probabilitas statistik piksel."
        }
    },
    {
        "id": "geo-lat-h-17",
        "materi": "SISTEM INFORMASI GEOGRAFIS & HIDROLOGI",
        "topic": "Pemodelan Hidrologi Watershed: Flow Direction dan Stream Ordering",
        "stem": "Dalam pemodelan hidrologi Daerah Aliran Sungai (DAS) berbasis data raster DEM, analisis aliran permukaan air hujan dilakukan melalui tahapan penetapan arah aliran (_Flow Direction_) menggunakan model algoritma D8 (Eight-Direction Pour Point). Prinsip penentuan arah aliran piksel pada algoritma D8 tersebut adalah...",
        "correct": "Air diasumsikan mengalir dari satu sel piksel pusat ke tepat satu dari delapan sel tetangganya yang memiliki kemiringan lereng penurunan elevasi tercuram (_steepest descent_).",
        "distractors": [
            "Air mengalir menyebar rata ke seluruh delapan sel tetangga secara proporsional tanpa memandang perbedaan ketinggian tempat.",
            "Air hanya dapat mengalir lurus ke arah empat mata angin utama (Utara, Timur, Selatan, Barat) dan dilarang mengalir diagonal.",
            "Air selalu mengalir naik menuju sel piksel tetangga yang memiliki nilai elevasi kontur paling tinggi.",
            "Air diasumsikan langsung menguap ke atmosfer pada setiap piksel tanpa membentuk jaringan akumulasi anak sungai."
        ],
        "formula": {
            "title": "ALGORITMA D8 MODEL HIDROLOGI RASTER SPASIAL",
            "latex": "\\text{Kemiringan Penurunan (Drop)} = \\frac{\\text{Elevasi Pusat} - \\text{Elevasi Tetangga}}{\\text{Jarak Antar Pusat Sel}} \\implies \\text{Aliran ke Nilai Drop Maksimum}" ,
            "legend": "• Jarak tetangga ortogonal = 1 ukuran sel ($d$); jarak tetangga diagonal = $\\sqrt{2} \\times d$<br>• Tahapan lanjut: _Flow Accumulation_ $\\implies$ Ekstraksi Jaringan Sungai $\\implies$ Delineasi Batas Punggung DAS"
        },
        "hints": {
            "concept": "Algoritma D8 hidrologi: air mengalir ke tepat satu dari 8 sel tetangga di sekitarnya yang memiliki penurunan lereng paling curam (steepest descent).",
            "execution": "Pilih opsi: mengalir ke tepat satu dari delapan sel tetangga yang memiliki penurunan elevasi tercuram."
        }
    },
    {
        "id": "geo-lat-h-18",
        "materi": "DINAMIKA KEPENDUDUKAN & KETENAGAKERJAAN",
        "topic": "Kalkulasi Angka Kematian Bayi (Infant Mortality Rate / IMR)",
        "stem": "Data registrasi kependudukan Kabupaten Makmur pada tahun 2024 mencatat:\n- Total jumlah kelahiran hidup sepanjang tahun: $20.000 \\text{ bayi}$\n- Jumlah bayi yang meninggal dunia sebelum genap mencapai usia 1 tahun: $400 \\text{ bayi}$\n- Total penduduk pertengahan tahun: $800.000 \\text{ jiwa}$\nNilai Angka Kematian Bayi (_Infant Mortality Rate_ / IMR) per 1.000 kelahiran hidup di kabupaten tersebut serta signifikansi indikatornya adalah...",
        "correct": "$IMR = 20$, menunjukkan bahwa terdapat 20 bayi meninggal per 1.000 kelahiran hidup, yang merupakan indikator sensitif atas tingkat kesehatan ibu-anak, gizi, dan sanitasi lingkungan setempat.",
        "distractors": [
            "$IMR = 0{,}5$, menunjukkan bahwa angka kematian bayi dihitung dari total seluruh penduduk kabupaten per 1.000 jiwa.",
            "$IMR = 50$, menunjukkan bahwa separuh dari bayi yang lahir tidak tertolong akibat fasilitas puskesmas yang buruk.",
            "$IMR = 2$, menunjukkan bahwa fasilitas persalinan rumah sakit daerah telah berstandar negara maju tanpa cacat gizi.",
            "$IMR = 40$, menunjukkan bahwa angka kematian balita melebihi batas bahaya stunting gizi buruk nasional."
        ],
        "formula": {
            "title": "FORMULA ANGKA KEMATIAN BAYI (INFANT MORTALITY RATE / IMR)",
            "latex": "\\begin{aligned} IMR & = \\frac{D_0}{B} \\times 1.000 = \\frac{400}{20.000} \\times 1.000 = \\frac{4}{200} \\times 1.000 = \\mathbf{20} \\end{aligned}",
            "legend": "• $D_0$: Jumlah kematian bayi usia $< 1$ tahun dalam 1 tahun kalender<br>• $B$: Total jumlah kelahiran hidup pada tahun yang sama (bukan total penduduk!)"
        },
        "hints": {
            "concept": "Rumus IMR: IMR = (D0 / B) * 1.000. D0 = 400 bayi meninggal usia < 1 tahun, B = 20.000 kelahiran hidup. Pembaginya BUKAN total penduduk, melainkan kelahiran hidup.",
            "execution": "Hitung: (400 / 20.000) * 1.000 = 0,02 * 1.000 = 20."
        }
    },
    {
        "id": "geo-lat-h-19",
        "materi": "DINAMIKA LITOSFER & SEJARAH BUMI",
        "topic": "Transgresi dan Regresi Glasial Pleistosen serta Paparan Sunda dan Sahul",
        "stem": "Pada Zaman Pleistosen (Zaman Es), bumi mengalami fluktuasi siklus iklim Glasial dan Interglasial yang memicu peristiwa turun-naiknya muka air laut global (_glacio-eustasy_). Dampak peristiwa regresi glasial (penurunan muka air laut hingga $100 - 120 \\text{ meter}$ di bawah muka laut sekarang) terhadap konfigurasi daratan dan persebaran flora-fauna di Nusantara adalah...",
        "correct": "Paparan Sunda (_Sunda Shelf_) mengering menyatukan Pulau Sumatera, Jawa, Kalimantan, dan Semenanjung Malaya dengan Benua Asia, sehingga fauna Asiatis (gajah, harimau, badak) leluasa bermigrasi melintasi daratan purba tersebut.",
        "distractors": [
            "Seluruh pulau di Indonesia tenggelam di bawah air laut sedalam ratusan meter dan hanya menyisakan puncak Gunung Kerinci.",
            "Laut Wallacea membeku menjadi dataran garam kering yang membuat satwa Australia dan Asia bercampur merata di Bali.",
            "Paparan Sahul terpisah ribuan kilometer dari Benua Australia akibat gempa tektonik pemekaran dasar samudra.",
            "Pulau Jawa dan Papua tersambung langsung oleh daratan datar tanpa rintangan perairan laut dalam sama sekali."
        ],
        "formula": {
            "title": "REGRESI DAN TRANSGRESI LAUT ZAMAN ES PLEISTOSEN",
            "latex": "\\begin{cases} \\mathbf{\\text{Fase Glasial (Muka Laut Turun } \\sim 120\\text{ m}):}} & \\mathbf{\\text{Paparan Sunda \\& Sahul Terpapar Menjadi Daratan Luas}} \\\\ & \\implies \\text{Jembatan Darat Migrasi Fauna Asiatis \\& Australis} \\\\ \\mathbf{\\text{Fase Interglasial (Pemanasan):}} & \\text{Es Mencair} \\implies \\text{Muka Laut Naik (Transgresi)} \\implies \\text{Isolasi Kepulauan} \\end{cases}",
            "legend": "• Zona Wallacea (Sulawesi, Maluku, Nusa Tenggara) dipisahkan palung laut sangat dalam sehingga tetap terisolasi sebagai wilayah fauna peralihan endemik"
        },
        "hints": {
            "concept": "Saat Zaman Es (regresi laut turun ~120 m), Paparan Sunda menjadi daratan kering yang menyatukan Sumatera, Jawa, Kalimantan dengan Benua Asia -> fauna mamalia besar Asiatis bermigrasi.",
            "execution": "Pilih: Paparan Sunda mengering menyatukan Sumatera, Jawa, Kalimantan dengan Benua Asia sehingga fauna Asiatis leluasa bermigrasi."
        }
    },
    {
        "id": "geo-lat-h-20",
        "materi": "DINAMIKA LITOSFER & GEOMORFOLOGI",
        "topic": "Siklus Geomorfologi William Morris Davis: Siklus Erosi Bentang Alam",
        "stem": "Dalam teori siklus erosi bentang alam William Morris Davis (_Geographical Cycle_), permukaan bumi hasil pengangkatan tektonik mengalami evolusi pelapukan dan erosi berkesinambungan melalui tiga tahapan: Stadia Muda, Stadia Dewasa, dan Stadia Tua. Karakteristik morfologi bentang alam pada Stadia Tua (_Old Stage_) ditandai oleh...",
        "correct": "Lembah sungai sangat lebar dengan lereng landai, kecepatan aliran air lambat, pola meander dan danau tapal kuda (_oxbow lake_) sangat dominan, serta topografi daratan tererosi hampir rata membentuk dataran nyaris (_peneplain_) dengan sisa bukit tahan erosi (_monadnock_).",
        "distractors": [
            "Lembah sungai sempit berbentuk huruf V curam dengan air terjun dan jeram bertingkat berarus deras yang mengikis dasar batuan.",
            "Erosi vertikal sungai mendominasi secara agresif dibandingkan erosi lateral sehingga terjadi pendalaman jurang ngarai ngarai terjal.",
            "Dataran tinggi terlipat dengan tebing sesar aktif yang belum tersentuh oleh aliran limpasan air permukaan dan vegetasi rumput.",
            "Perbukitan kerucut karst gamping dengan lorong gua bawah tanah yang belum terisi oleh endapan stalaktit dan stalagmit."
        ],
        "formula": {
            "title": "EVOLUSI BENTANG ALAM SIKLUS EROSI DAVIS",
            "latex": "\\begin{aligned} \\text{Stadia Muda:} & \\quad \\text{Erosi Vertikal Kuat, Lembah V Curam, Jeram/Air Terjun, Relief Kasar} \\\\ \\text{Stadia Dewasa:} & \\quad \\text{Erosi Lateral Imbang, Mulai Bermelek-leuk (Meander Awal), Lembah U} \\\\ \\mathbf{\\text{Stadia Tua:}} & \\quad \\mathbf{\\text{Erosi Lateral Mutlak, Lembah Sangat Lebar, Oxbow Lake, Peneplain + Monadnock}} \\end{aligned}",
            "legend": "• Monadnock: Sisa bukit terisolasi berbatu keras yang tahan terhadap erosi di tengah hamparan dataran peneplain"
        },
        "hints": {
            "concept": "Tahapan siklus Davis: Muda (lembah V, erosi vertikal, air terjun). Dewasa (lembah U, erosi lateral). Tua (lembah sangat lebar, erosi lateral dominan, meander luas, oxbow lake, dataran nyaris/peneplain, bukit sisa monadnock).",
            "execution": "Pilih: Lembah sungai sangat lebar berlereng landai, meander dan oxbow lake dominan, membentuk peneplain dan monadnock."
        }
    },
    {
        "id": "geo-lat-h-21",
        "materi": "DINAMIKA LITOSFER & GEOLOGI STRUKTUR",
        "topic": "Mekanisme Sesar Geser Mendatar: Sesar Semangko dan Sesar Palu-Koro",
        "stem": "Aktivitas tektonik di Indonesia tidak hanya memicu gempa subduksi megathrust, tetapi juga sesar geser mendatar (_strike-slip fault_) di daratan. Sesar Besar Sumatera (_The Great Sumatran Fault_ / Sesar Semangko) sepanjang $1.900 \\text{ km}$ dan Sesar Palu-Koro di Sulawesi Tengah diklasifikasikan berdasarkan kinematika pergerakan blok batuan sebagai sesar...",
        "correct": "Sesar mendatar dekstral (_dextral / right-lateral strike-slip fault_) untuk Sesar Semangko di mana blok seberang bergeser ke kanan, dan sesar mendatar sinistral (_sinistral / left-lateral strike-slip fault_) untuk Sesar Palu-Koro di mana blok seberang bergeser ke kiri.",
        "distractors": [
            "Sesar normal (_dip-slip fault_) yang terjadi akibat tarikan lempeng tektonik divergen di dasar palung laut dalam.",
            "Sesar naik sungkup (_thrust fault_) yang hanya menggerakkan blok gamping vertikal ke atas tanpa pergeseran horizontal.",
            "Sesar transform samudra yang tidak memiliki potensi memicu getaran gempa di wilayah permukiman daratan.",
            "Kedua sesar tersebut merupakan sesar gravitasi rotasional murni yang tidak berhubungan dengan pertemuan lempeng litosfer."
        ],
        "formula": {
            "title": "KLASIFIKASI KINEMATIKA SESAR GESER (STRIKE-SLIP FAULT)",
            "latex": "\\begin{cases} \\mathbf{\\text{Sesar Dekstral (Right-Lateral):}} & \\text{Pengamat melihat blok di seberang sesar bergerak ke kanan} \\implies \\mathbf{\\text{Sesar Semangko}} \\\\ \\mathbf{\\text{Sesar Sinistral (Left-Lateral):}} & \\text{Pengamat melihat blok di seberang sesar bergerak ke kiri} \\implies \\mathbf{\\text{Sesar Palu-Koro}} \\end{cases}",
            "legend": "• Sesar daratan dangkal (_shallow crustal earthquake_) memiliki kedalaman hiposentrum < 15 km sehingga guncangannya sangat merusak di permukaan"
        },
        "hints": {
            "concept": "Sesar Semangko (Sumatera) = sesar mendatar dekstral (kanan). Sesar Palu-Koro (Sulawesi Tengah) = sesar mendatar sinistral (kiri). Keduanya merupakan strike-slip fault darat aktif.",
            "execution": "Pilih: Sesar mendatar dekstral untuk Sesar Semangko, dan sesar mendatar sinistral untuk Sesar Palu-Koro."
        }
    },
    {
        "id": "geo-lat-h-22",
        "materi": "DINAMIKA ATMOSFER & IKLIM TROPIS",
        "topic": "Klasifikasi Iklim Köppen untuk Wilayah Indonesia (Af, Am, Aw)",
        "stem": "Wladimir Köppen membagi tipe iklim bumi berdasarkan nilai batas curah hujan bulanan dan suhu udara yang berkorelasi langsung dengan formasi vegetasi alami. Pola sebaran iklim Köppen di wilayah Indonesia dari arah barat ke arah timur-tenggara (Sumatera/Kalimantan $\\to$ Jawa $\\to$ Nusa Tenggara) menunjukkan gradasi tipe iklim...",
        "correct": "$Af \\to Am \\to Aw$, yaitu dari Hutan Hujan Tropis selalu basah ($Af$) di Sumatera/Kalimantan, Hutan Muson Tropis berperiodisitas tegas ($Am$) di sebagian Jawa, hingga Sabana Tropis berpadang rumput kering ($Aw$) di Nusa Tenggara Timur.",
        "distractors": [
            "$Aw \\to Am \\to Af$, yaitu dari sabana gersang di Sumatera barat menuju hutan lebat lembap selalu hujan di Timor Leste.",
            "$Cs \\to Cw \\to Cf$, yaitu tipe iklim subtropis sedang mediterania yang mengalami musim dingin bersalju di pantai utara Jawa.",
            "$BW \\to BS \\to Af$, yaitu dari iklim gurun pasir tandus di Kalimantan menuju padang stepa rumput di kepulauan Natuna.",
            "$ET \\to EF \\to Am$, yaitu tipe iklim tundra es beku kutub yang membentang di seluruh pulau dataran rendah Sulawesi."
        ],
        "formula": {
            "title": "GRADASI IKLIM TROPIS KÖPPEN (TIPE A: SUHU BULAN TERDINGIN > 18°C)",
            "latex": "\\begin{cases} \\mathbf{Af \\text{ (Tropical Rainforest):}} & \\text{Bulan terkering } P_{\\min} \\ge 60 \\text{ mm (Sumatera, Kalimantan, Papua Barat)} \\\\ \\mathbf{Am \\text{ (Tropical Monsoon):}} & P_{\\min} < 60 \\text{ mm, tetapi total tahunan mengimbangi musim kemarau (Jawa Tengah/Timur)} \\\\ \\mathbf{Aw \\text{ (Tropical Savanna):}} & \\text{Musim kemarau panjang yang sangat tegas (NTB, NTT, Merauke)} \\end{cases}",
            "legend": "• Variasi dipengaruhi oleh jarak dari sumber uap air Samudra Hindia dan Samudra Pasifik serta pengaruh angin muson timur Australia"
        },
        "hints": {
            "concept": "Gradasi iklim Köppen Indonesia dari barat ke timur: Af (Hutan hujan tropis basah di Sumatera/Kalimantan) -> Am (Muson di Jawa) -> Aw (Sabana tropis kering di NTT).",
            "execution": "Pilih: Af -> Am -> Aw (Hutan Hujan Tropis -> Muson Tropis -> Sabana Tropis)."
        }
    },
    {
        "id": "geo-lat-h-23",
        "materi": "DINAMIKA HIDROSFER & OSEANOGRAFI",
        "topic": "Fenomena Upwelling Oseanografi dan Ekman Transport di Selatan Jawa",
        "stem": "Pada periode Muson Timur (Juni - Agustus), perairan pesisir selatan Jawa, Bali, dan barat Sumatera mengalami peningkatan kelimpahan klorofil-a dan konsentrasi tangkapan ikan pelagis yang sangat tinggi. Fenomena oseanografi fisik yang mendasari peristiwa tersebut adalah...",
        "correct": "Fenomena _upwelling_ yang dipicu oleh Transpor Ekman (_Ekman Transport_), di mana hembusan angin Muson Tenggara mendorong lapisan massa air hangat permukaan menjauhi garis pantai, memicu naiknya massa air dingin dasar laut yang kaya akan nutrien (nitrat dan fosfat) ke lapisan fotik permukaan.",
        "distractors": [
            "Fenomena arus pasang laut purnama yang menumpahkan garam mineral dari kawah gunung lumpur bawah laut ke pantai pasir.",
            "Pemanasan gelombang panas lautan (_marine heatwave_) yang membunuh fitoplankton sehingga air laut menjadi jernih bagi ikan karang.",
            "Intrusi limbah detergen fosfat buangan sungai kota besar yang menyuburkan lumut pantai beracun tanpa hembusan angin.",
            "Tenggelamnya massa air laut hangat ke palung Jawa (_downwelling_) yang menekan zooplankton hingga ke dasar samudra."
        ],
        "formula": {
            "title": "MEKANISME UPWELLING DAN TRANSPOR EKMAN (HEMISFER SELATAN)",
            "latex": "\\text{Angin Muson Tenggara} \\xrightarrow{\\text{Gaya Coriolis Belok Kiri}} \\text{Transpor Ekman Netto Menjauhi Pantai} \\implies \\mathbf{\\text{Naiknya Air Dalam Dingin \\& Bernutrien (Upwelling)}}",
            "legend": "• Nutrien tinggi $\\implies$ _Bloom_ fitoplankton $\\implies$ Klorofil-a melonjak $\\implies$ Migrasi ikan tuna dan lemuru memuncak"
        },
        "hints": {
            "concept": "Upwelling di selatan Jawa saat Muson Tenggara: Transpor Ekman mendorong air hangat permukaan menjauhi pantai -> massa air dingin kaya nutrien dari dasar laut naik ke permukaan (upwelling) -> klorofil dan ikan melimpah.",
            "execution": "Pilih: Fenomena upwelling dipicu Transpor Ekman, naiknya massa air dingin kaya nutrien ke permukaan."
        }
    },
    {
        "id": "geo-lat-h-24",
        "materi": "DINAMIKA KEPENDUDUKAN & KETENAGAKERJAAN",
        "topic": "Kalkulasi Kerapatan Fisiologis dan Kerapatan Agraris Penduduk",
        "stem": "Data sensus kependudukan dan tata guna lahan Wilayah Pertanian Sukamaju menunjukkan:\n- Total jumlah penduduk: $1.200.000 \\text{ jiwa}$\n- Jumlah penduduk yang berprofesi sebagai petani: $360.000 \\text{ jiwa}$\n- Total luas wilayah keseluruhan: $4.000 \\text{ km}^2$\n- Total luas lahan pertanian yang dapat ditanami: $600 \\text{ km}^2$\nBesarnya Kerapatan Penduduk Fisiologis ($K_f$) dan Kerapatan Penduduk Agraris ($K_a$) di wilayah tersebut per kilometer persegi adalah...",
        "correct": "$K_f = 2.000 \\text{ jiwa/km}^2$ dan $K_a = 600 \\text{ petani/km}^2$.",
        "distractors": [
            "$K_f = 300 \\text{ jiwa/km}^2$ dan $K_a = 90 \\text{ petani/km}^2$.",
            "$K_f = 600 \\text{ jiwa/km}^2$ dan $K_a = 2.000 \\text{ petani/km}^2$.",
            "$K_f = 2.000 \\text{ jiwa/km}^2$ dan $K_a = 300 \\text{ petani/km}^2$.",
            "$K_f = 1.200 \\text{ jiwa/km}^2$ dan $K_a = 360 \\text{ petani/km}^2$."
        ],
        "formula": {
            "title": "FORMULA KERAPATAN FISIOLOGIS VS KERAPATAN AGRARIS",
            "latex": "\\begin{aligned} K_f & = \\frac{\\text{Total Jumlah Penduduk}}{\\text{Luas Lahan Pertanian}} = \\frac{1.200.000}{600} = \\mathbf{2.000 \\text{ jiwa/km}^2} \\\\ K_a & = \\frac{\\text{Jumlah Penduduk Petani}}{\\text{Luas Lahan Pertanian}} = \\frac{360.000}{600} = \\mathbf{600 \\text{ petani/km}^2} \\end{aligned}",
            "legend": "• Kerapatan Aritmatika = Total Penduduk / Total Luas Wilayah = $1.200.000 / 4.000 = 300 \\text{ jiwa/km}^2$<br>• Kerapatan Fisiologis & Agraris menjadi tolok ukur tekanan penduduk terhadap daya dukung lahan pangan"
        },
        "hints": {
            "concept": "Kerapatan Fisiologis (Kf) = Total Penduduk / Luas Lahan Pertanian = 1.200.000 / 600 = 2.000 jiwa/km^2. Kerapatan Agraris (Ka) = Petani / Luas Lahan Pertanian = 360.000 / 600 = 600 petani/km^2.",
            "execution": "Hitung: Kf = 2.000 jiwa/km^2 dan Ka = 600 petani/km^2."
        }
    },
    {
        "id": "geo-lat-h-25",
        "materi": "PEMBANGUNAN BERKELANJUTAN & LINGKUNGAN HIDUP",
        "topic": "Pengelolaan DAS Terpadu dan Pembayaran Jasa Lingkungan (PES)",
        "stem": "Dalam pendekatan Pengelolaan Daerah Aliran Sungai Terpadu (_Integrated Watershed Management_), masyarakat di kawasan hulu pegunungan sering kali diwajibkan menjaga tutupan hutan lindung dan meniadakan alih fungsi lahan sawit agar kawasan hilir perkotaan terhindar dari banjir bandang dan krisis sedimentasi air baku. Skema ekonomi lingkungan berkelanjutan yang paling tepat untuk memberikan kompensasi finansial yang adil bagi masyarakat hulu adalah...",
        "correct": "Pembayaran Jasa Lingkungan (_Payment for Ecosystem Services_ / PES), di mana penerima manfaat air bersih dan perlindungan banjir di kawasan hilir (PDAM, industri, warga kota) membayar retribusi jasa lingkungan kepada masyarakat konservasi hulu.",
        "distractors": [
            "Penggusuran paksa seluruh desa di kawasan hulu pegunungan untuk dialihfungsikan menjadi zona tambang terbuka berizin negara.",
            "Pemberian bantuan beras raskin darurat sebulan sekali tanpa mekanisme perlindungan hukum atas hak kepemilikan tanah adat.",
            "Penebangan pohon kayu komersial secara legal oleh perusahaan swasta untuk disumbangkan ke kas pembangunan bendungan hilir.",
            "Penetapan pajak berganda yang lebih tinggi bagi penduduk pedesaan hulu karena dinilai tidak memberikan kontribusi industri bagi negara."
        ],
        "formula": {
            "title": "SKEMA PEMBAYARAN JASA LINGKUNGAN HULU-HILIR (PES)",
            "latex": "\\text{Konservasi Tutupan Hutan Hulu} \\xrightarrow{\\text{Jasa Hidrologis}} \\text{Kestabilan Debit Air \\& Bebas Sedimentasi di Hilir} \\xrightarrow{\\mathbf{\\text{Insentif Finansial (PES)}}} \\text{Kesejahteraan Petani Hulu}",
            "legend": "• Menginternalisasi biaya eksternalitas positif lingkungan agar masyarakat hulu memiliki insentif ekonomi rasional untuk tidak menebang hutan"
        },
        "hints": {
            "concept": "Mekanisme kompensasi ekonomi hilir membayar hulu yang merawat fungsi tata air hutan disebut Pembayaran Jasa Lingkungan (Payment for Ecosystem Services / PES).",
            "execution": "Pilih: Pembayaran Jasa Lingkungan (Payment for Ecosystem Services / PES) dari penerima manfaat hilir ke pelestari hulu."
        }
    }
]
