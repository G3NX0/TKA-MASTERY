# -*- coding: utf-8 -*-
"""
tkj_data_hard.py
25 Unique Authentic Hard Items for TKA 2026 Teknik Jaringan Komputer dan Telekomunikasi (TJKT / TKJ).
Strictly aligned with Pusmendik TKA 2026 & BSKAP 033/H/KR/2024.
Zero AI Slop - Zero Duplicates.
"""

TKJ_HARD = [
    {
        "id": "tkj-lat-h-01",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Analisis Tipe LSA pada Multi-Area OSPF",
        "type": "mcq",
        "questionHtml": "Dalam topologi OSPF Multi-Area enterprise, router R1 bertindak sebagai Area Border Router (ABR) yang menghubungkan Area 0 (Backbone) dengan Area 1 (Standard). Di Area 2 terdapat router R3 yang me-redistribute rute eksternal dari protokol BGP ISP. Tipe Link-State Advertisement (LSA) yang di-generate oleh R1 untuk mengabarkan rute ringkasan antar-area (inter-area routes) ke dalam Area 1, serta LSA yang membawa informasi rute eksternal dari R3 adalah...",
        "options": [
            {"key": "A", "text": "R1 meng-generate LSA Type 3 (Summary LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 5 (AS External LSA)."},
            {"key": "B", "text": "R1 meng-generate LSA Type 1 (Router LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 2 (Network LSA)."},
            {"key": "C", "text": "R1 meng-generate LSA Type 4 (ASBR Summary LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 7 (NSSA External LSA)."},
            {"key": "D", "text": "R1 meng-generate LSA Type 5 (External LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 3 (Summary LSA)."},
            {"key": "E", "text": "R1 meng-generate LSA Type 2 (Network LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 1 (Router LSA)."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "TAKSONOMI TIPE LSA PADA PROTOKOL OSPF",
            "latex": "\\begin{aligned} \\text{LSA 1:} & \\text{ Router (Intra-Area)} & \\text{LSA 4:} & \\text{ ASBR Summary (Menuju ASBR)} \\\\ \\text{LSA 2:} & \\text{ Network (Dihasilkan DR)} & \\text{LSA 5:} & \\text{ AS External (Dihasilkan ASBR)} \\\\ \\text{LSA 3:} & \\text{ Summary (Dihasilkan ABR)} & \\text{LSA 7:} & \\text{ NSSA External (Dihasilkan NSSA)} \\end{aligned}",
            "legend": "• ABR merangkum rute intra-area menjadi LSA Type 3 untuk disuntikkan ke area lain<br>• ASBR mengimpor rute dari luar OSPF dan membungkusnya dalam LSA Type 5"
        },
        "hints": {
            "concept": "ABR (Area Border Router) bertanggung jawab menghasilkan LSA Type 3 (Summary LSA). ASBR (Autonomous System Boundary Router) bertanggung jawab menghasilkan LSA Type 5 (AS External LSA).",
            "execution": "Pilihan A tepat memasangkan peran ABR (LSA 3) dan ASBR (LSA 5)."
        },
        "explanation": "Dalam arsitektur OSPF: (1) LSA Type 3 (Summary LSA) dibuat oleh ABR untuk mengiklankan jaringan yang dipelajari dari satu area ke area lainnya; (2) LSA Type 5 (AS-External LSA) dibuat oleh ASBR (router yang melakukan redistribution dari protokol lain seperti BGP/EIGRP/Static) untuk mengiklankan rute eksternal ke seluruh domain OSPF (kecuali stub area). LSA Type 4 dibuat oleh ABR untuk menginformasikan lokasi ASBR tersebut.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-02",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Algoritma Seleksi BGP Best Path Attributes",
        "type": "mcq",
        "questionHtml": "Sebuah router Border BGP menerima dua rute alternatif untuk prefix jaringan yang sama `203.0.113.0/24` dari dua ISP yang berbeda (ISP-1 dan ISP-2). Parameter atribut yang terbaca adalah:\n• Rute dari ISP-1: Weight = `0`, Local Preference = `200`, AS Path = `64500 64501`, MED = `100`\n• Rute dari ISP-2: Weight = `0`, Local Preference = `100`, AS Path = `64500`, MED = `50`\nBerdasarkan urutan resmi algoritma BGP Best Path Selection, rute yang akan dipilih menjadi rute terbaik (best path) beserta alasannya adalah...",
        "options": [
            {"key": "A", "text": "Rute dari ISP-1, karena memiliki nilai Local Preference yang lebih tinggi (200 > 100), dievaluasi sebelum mempertimbangkan panjang AS Path."},
            {"key": "B", "text": "Rute dari ISP-2, karena memiliki nilai AS Path yang lebih pendek (1 AS hop vs 2 AS hop), dievaluasi sebelum Local Preference."},
            {"key": "C", "text": "Rute dari ISP-2, karena memiliki nilai Multi-Exit Discriminator (MED) yang lebih rendah (50 < 100)."},
            {"key": "D", "text": "Kedua rute dibagikan beban lalu lintasnya (load balancing) karena nilai Weight keduanya bernilai sama-sama 0."},
            {"key": "E", "text": "Rute dari ISP-1, karena memiliki nilai MED yang lebih tinggi yang menandakan prioritas metrik terbesar."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "URUTAN HIERARKI BGP BEST PATH SELECTION",
            "latex": "1.\\,\\text{Weight (Highest)} \\to 2.\\,\\text{Local-Pref (Highest)} \\to 3.\\,\\text{Originate} \\to 4.\\,\\text{AS-Path (Shortest)} \\to 5.\\,\\text{Origin Code} \\to 6.\\,\\text{MED (Lowest)}",
            "legend": "• Weight (Cisco proprietary): Nilai tertinggi menang<br>• Local Preference: Standar BGP RFC, nilai TERTINGGI menang, dievaluasi SEBELUM AS Path"
        },
        "hints": {
            "concept": "Hafalkan jembatan keledai BGP path selection: 'We Love Originating As Oranges Mean Pure Refreshment' (Weight, Local Pref, Originate, AS Path, Origin, MED...).",
            "execution": "Karena Weight bernilai sama (0), kriteria berikutnya adalah Local Preference tertinggi. ISP-1 (200) mengalahkan ISP-2 (100) langsung di langkah kedua sebelum panjang AS Path diperiksa."
        },
        "explanation": "Urutan BGP Best Path Selection adalah: (1) Weight tertinggi (Cisco proprietary); (2) Local Preference TERTINGGI; (3) Rute yang di-originate secara lokal; (4) AS Path TERPENDEK; (5) Origin code terendah (IGP < EGP < Incomplete); (6) MED TERENDAH. Karena Weight sama-sama 0, router langsung mengevaluasi Local Preference. Rute dari ISP-1 memiliki Local Preference 200, mengalahkan ISP-2 yang bernilai 100, sehingga rute ISP-1 langsung terpilih tanpa perlu mengevaluasi AS Path.",
        "isDiagnostic": True
    },
    {
        "id": "tkj-lat-h-03",
        "subject": "tkj",
        "materi": "PENGALAMATAN IPV4 & SUBNETTING",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Supernetting / Route Summarization & Blackhole Routing",
        "type": "mcq",
        "questionHtml": "Seorang core engineer ingin meringkas (summarize) 4 buah rute subnet lokal berikut ke dalam satu rute tunggal pada tabel routing OSPF:\n• `192.168.16.0/24`\n• `192.168.17.0/24`\n• `192.168.18.0/24`\n• `192.168.19.0/24`\nAlamat supernet summary paling spesifik yang mencakup tepat keempat subnet tersebut tanpa menyisakan ruang kosong (zero wasted subnet), serta tindakan mitigasi loop yang wajib diterapkan pada router perangkum adalah...",
        "options": [
            {"key": "A", "text": "192.168.16.0/22; dan menambahkan rute statis 192.168.16.0/22 ke interface 'null0' (blackhole) untuk mencegah routing loop."},
            {"key": "B", "text": "192.168.16.0/21; dan mengaktifkan split horizon pada seluruh antarmuka backbone OSPF."},
            {"key": "C", "text": "192.168.0.0/20; dan menyetel Administrative Distance rute summary menjadi bernilai 255."},
            {"key": "D", "text": "192.168.16.0/23; dan memblokir paket ICMP redirect pada switch access layer."},
            {"key": "E", "text": "192.168.18.0/22; dan mengaktifkan fitur Proxy ARP pada antarmuka trunk router."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "KALKULASI RUTE RINGKASAN (ROUTE SUMMARIZATION)",
            "latex": "\\begin{aligned} .16 &= 000100\\mathbf{00}_2 \\\\ .17 &= 000100\\mathbf{01}_2 \\\\ .18 &= 000100\\mathbf{10}_2 \\\\ .19 &= 000100\\mathbf{11}_2 \\end{aligned} \\implies 6\\text{ bit sama di oktet ke-3} \\implies 16 + 6 = 22\\text{ bit} \\implies /22",
            "legend": "• Network Summary: 192.168.16.0/22<br>• Rentang: 192.168.16.0 s/d 192.168.19.255 (Tepat 4 subnet /24)<br>• Rute discard/null0: Membuang paket ke IP tak terpakai agar tidak memantul ke default route"
        },
        "hints": {
            "concept": "Tuliskan oktet ke-3 dalam biner: 16 (00010000), 17 (00010001), 18 (00010010), 19 (00010011). Bit yang sama ada 6 bit pertama. Prefix = 16 + 6 = /22. Alamat dasar = 192.168.16.0/22.",
            "execution": "Pilihan A tepat: 192.168.16.0/22 dengan rute Null0 (Blackhole) untuk memutus potensi routing loop jika ada paket menuju IP tak terpasang di dalam blok summary."
        },
        "explanation": "Konversi biner oktet ke-3: 16 (00010000_2) hingga 19 (00010011_2) berbagi 6 bit prefix yang sama persis (000100_2). Dengan demikian, panjang prefix adalah 8 + 8 + 6 = 22 bit, menghasilkan supernet `192.168.16.0/22`. Ketika router mengumumkan rute summary ini ke jaringan luar, router wajib menginstal rute statis summary tersebut ke interface virtual `Null0` (discard/blackhole) secara lokal. Hal ini krusial: jika ada paket yang ditujukan ke IP di dalam rentang summary tetapi subnet aslinya sedang down, paket tidak akan dipantulkan bolak-balik antara router ini dengan default gateway yang menimbulkan routing loop.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-04",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Mekanisme Proteksi Spanning Tree: BPDU Guard vs Root Guard",
        "type": "mcq",
        "questionHtml": "Di sebuah lingkungan enterprise, teknisi mengaktifkan fitur `spanning-tree bpduguard enable` pada seluruh port switch yang terhubung ke komputer user (PortFast / Edge Port). Kemudian teknisi mengaktifkan `spanning-tree guard root` pada port trunk switch distribution yang mengarah ke switch access. Tujuan spesifik dari kombinasi kedua fitur keamanan layer 2 ini adalah...",
        "options": [
            {"key": "A", "text": "BPDU Guard mematikan port edge jika menerima paket BPDU dari switch liar, sedangkan Root Guard mencegah switch liar mengambil alih peran Root Bridge."},
            {"key": "B", "text": "BPDU Guard mengenkripsi seluruh frame data yang lewat, sedangkan Root Guard membatasi jumlah host maksimum menjadi 1 unit."},
            {"key": "C", "text": "BPDU Guard mengubah mode port menjadi trunking otomatis, sedangkan Root Guard menghapus tabel CAM jika terjadi banjir ARP."},
            {"key": "D", "text": "BPDU Guard mempercepat proses konvergensi STP dari 30 detik menjadi 1 detik, sedangkan Root Guard memblokir seluruh frame broadcast."},
            {"key": "E", "text": "Keduanya berfungsi identik untuk mengaktifkan Dynamic Trunking Protocol (DTP) secara agresif pada antarmuka access."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME MITIGASI SERANGAN SPANNING TREE",
            "latex": "\\begin{aligned} \\text{BPDU Guard (Access):} & \\; \\text{Terima BPDU} \\implies \\text{Port mati langsung (err-disable)} \\\\ \\text{Root Guard (Trunk):} & \\; \\text{Terima Superior BPDU} \\implies \\text{Root-Inconsistent (Blocking)} \\end{aligned}",
            "legend": "• Mencegah rogue switch / switch liar yang dibawa user merusak topologi pohon STP<br>• Menjaga Core Switch tetap menjadi pusat Root Bridge permanen"
        },
        "hints": {
            "concept": "BPDU Guard ditaruh di port komputer user: komputer tidak boleh mengirim BPDU. Jika mengirim BPDU (misal ada yang mencolok switch baru), port langsung dimatikan. Root Guard ditaruh di port downlink untuk memastikan tidak ada switch di bawah yang mengklaim jadi Root.",
            "execution": "Pilihan A tepat membedakan fungsi BPDU Guard (mematikan port edge jika terima BPDU) dan Root Guard (mempertahankan posisi Root Bridge sah)."
        },
        "explanation": "BPDU Guard diterapkan pada antarmuka PortFast/Edge yang terhubung langsung ke end-device (PC/server); jika perangkat di port tersebut mengirimkan frame BPDU (misalnya pengguna iseng mencolokkan switch manageable liar), BPDU Guard seketika mematikan port ke status err-disable. Sedangkan Root Guard dipasang pada port trunk switch hierarki atas yang mengarah ke switch subordinat; jika switch subordinat mengirimkan 'Superior BPDU' dengan Bridge Priority lebih rendah untuk merebut takhta Root Bridge, Root Guard akan memindahkan port tersebut ke status 'root-inconsistent' (blocking) sehingga struktur topologi STP core tetap aman.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-05",
        "subject": "tkj",
        "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Dispersi Kromatik dan Polariasi pada Transmisi DWDM 100G",
        "type": "mcq",
        "questionHtml": "Pada link transmisi serat optik Dense Wavelength Division Multiplexing (DWDM) berkecepatan 100 Gbps yang membentang lebih dari 500 kilometer, terjadi fenomena di mana komponen spektral panjang gelombang yang berbeda dari pulsa cahaya merambat dengan kecepatan yang sedikit berbeda di dalam serat silika, menyebabkan pulsa melebar seiring bertambahnya jarak hingga saling tumpang tindih (Inter-Symbol Interference). Fenomena fisik degradasi sinyal ini disebut...",
        "options": [
            {"key": "A", "text": "Dispersi Kromatik (Chromatic Dispersion / Material and Waveguide Dispersion)."},
            {"key": "B", "text": "Dispersi Modal (Modal Dispersion akibat perbedaan sudut pantul multi-mode)."},
            {"key": "C", "text": "Atenuasi Rayleigh Scattering akibat kotoran mikroskopis partikel kaca."},
            {"key": "D", "text": "Self-Phase Modulation akibat non-linearitas daya optik yang terlalu rendah."},
            {"key": "E", "text": "Four-Wave Mixing akibat polarisasi melingkar gelombang radio microwave."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "FORMULA DISPERSI KROMATIK OPTIK",
            "latex": "\\Delta t = D \\times \\Delta \\lambda \\times L \\quad [\\text{ps}]",
            "legend": "• D: Koefisien Dispersi Kromatik (misal 17 ps/(nm·km) pada 1550 nm standar G.652)<br>• Δλ: Lebar spektral sumber cahaya pemancar (nm)<br>• L: Jarak bentangan serat optik (km)"
        },
        "hints": {
            "concept": "Pada kabel Single Mode, tidak ada dispersi modal. Pelebaran pulsa disebabkan oleh kecepatan rambat panjang gelombang yang berbeda-beda di dalam material kaca. Ini adalah 'Dispersi Kromatik'.",
            "execution": "Dispersi Kromatik (gabungan dispersi material dan waveguide) adalah faktor pembatas utama jarak pada transmisi optik kecepatan tinggi (10G/100G) jarak jauh."
        },
        "explanation": "Dispersi Kromatik (Chromatic Dispersion) terjadi pada serat optik Single Mode karena indeks bias kaca bervariasi bergantung pada panjang gelombang cahaya. Karena pulsa laser memiliki lebar spektral tertentu (Δλ), komponen gelombang dengan frekuensi berbeda akan merambat dengan kecepatan kelompok (group velocity) yang berbeda di sepanjang serat optik. Akibatnya, pulsa cahaya melebar (broadening) sebanding dengan jarak (L). Pada sistem DWDM 100G, hal ini dikompensasi menggunakan Dispersion Compensating Fiber (DCF) atau modul Digital Signal Processor (DSP) koheren.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-06",
        "subject": "tkj",
        "materi": "ANALISIS PAKET DATA & TROUBLESHOOTING",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Analisis Flag TCP Handshake dan Window Zero pada Wireshark",
        "type": "mcq",
        "questionHtml": "Saat menganalisis kegagalan transmisi file besar pada capture Wireshark, teknisi mengamati bahwa server web tiba-tiba mengirimkan paket TCP dengan field `Window Size = 0` (TCP ZeroWindow). Implikasi teknis dari paket tersebut terhadap alur transmisi data klien adalah...",
        "options": [
            {"key": "A", "text": "Buffer penerima (Receive Buffer) pada server sudah penuh total, sehingga klien wajib menghentikan pengiriman data dan hanya mengirim TCP Zero Window Probe secara berkala."},
            {"key": "B", "text": "Koneksi TCP telah diputus secara paksa oleh server dengan flag RST (Reset connection)."},
            {"key": "C", "text": "Kabel jaringan klien mengalami putus fisik sehingga throughput terhenti pada layer 1."},
            {"key": "D", "text": "Server meminta klien untuk melipatgandakan ukuran segmen Maximum Transmission Unit (MTU) menjadi 9000 bytes."},
            {"key": "E", "text": "Server berhasil menyelesaikan handshake dan meminta autentikasi username SSL baru."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "KONTROL ALIRAN DATA TCP SLIDING WINDOW",
            "latex": "\\text{Throughput Maksimum} = \\frac{\\text{TCP Window Size}}{\\text{Round-Trip Time (RTT)}} \\implies \\text{Win}=0 \\implies \\text{Throughput}=0",
            "legend": "• Flow Control: Menjaga pengirim cepat agar tidak menenggelamkan penerima lambat<br>• Zero Window Probe: Paket kecil 1-byte dari klien untuk mengecek apakah buffer server sudah longgar"
        },
        "hints": {
            "concept": "TCP Window Size mengindikasikan berapa banyak byte yang siap ditampung oleh buffer penerima. Jika bernilai 0, berarti 'Saya sedang penuh, tolong jangan kirim data lagi'.",
            "execution": "TCP ZeroWindow memaksa klien menghentikan transmisi payload data sementara waktu hingga server mengirim paket 'TCP Window Update'."
        },
        "explanation": "Protokol TCP menggunakan mekanisme Sliding Window untuk pengendalian aliran data (Flow Control). Nilai Window Size dalam header TCP menunjukkan kapasitas memori penyangga (buffer) aplikasi penerima yang masih tersisa. Jika aplikasi di server sibuk dan buffer penerimanya terisi penuh hingga 100%, TCP stack server akan mengirimkan paket `TCP ZeroWindow`. Klien wajib segera menghentikan pengiriman data payload, dan klien akan mengirimkan paket 'Zero Window Probe' secara periodik untuk memeriksa apakah buffer server sudah memiliki ruang kosong kembali.",
        "isDiagnostic": True
    },
    {
        "id": "tkj-lat-h-07",
        "subject": "tkj",
        "materi": "KEAMANAN JARINGAN & FIREWALL",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Mitigasi Serangan TCP SYN Flood menggunakan SYN Cookies",
        "type": "mcq",
        "questionHtml": "Sebuah server web diserang dengan jutaan paket TCP SYN per detik dengan alamat IP sumber palsu (spoofed IP), mengakibatkan tabel antrean koneksi separuh terbuka (half-open connection / SYN backlog queue) penuh dan menolak pengguna sah. Mekanisme pertahanan kernel Linux yang paling efektif untuk memitigasi serangan ini tanpa menghabiskan memori backlog adalah...",
        "options": [
            {"key": "A", "text": "Mengaktifkan 'SYN Cookies' (net.ipv4.tcp_syncookies = 1) di mana server menyandikan data koneksi ke dalam Initial Sequence Number (ISN) tanpa mengalokasikan memori tabel koneksi sebelum ACK diterima."},
            {"key": "B", "text": "Memperbesar nilai MTU kartu jaringan menjadi 16.000 bytes agar paket SYN dapat ditampung sekaligus."},
            {"key": "C", "text": "Menonaktifkan protokol TCP pada kernel dan mengganti seluruh port HTTP web server menjadi protokol UDP mentah."},
            {"key": "D", "text": "Mengirimkan paket ICMP Destination Unreachable ke seluruh alamat IP yang mengirimkan paket SYN."},
            {"key": "E", "text": "Mematikan fitur Address Resolution Protocol (ARP) pada kartu jaringan server Linux."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME KRIPTOGRAFI TCP SYN COOKIES",
            "latex": "\\text{ISN}_{\\text{Server}} = \\text{Hash}(\\text{Src IP, Dst IP, Src Port, Dst Port, Secret Key, Time Counter}) + \\text{MSS Encoded}",
            "legend": "• Tanpa SYN Cookies: Setiap paket SYN mengalokasikan memori TCB (Transmission Control Block) -> Ram habis<br>• Dengan SYN Cookies: Zero memory allocation saat SYN, memori baru dialokasikan saat klien membalas ACK yang sah"
        },
        "hints": {
            "concept": "SYN Flood menghabiskan memori server dengan menaruh koneksi setengah jadi di antrean. Solusinya adalah teknik kriptografi 'SYN Cookies' di mana server tidak menyimpan status apa pun di memori sampai handshake selesai.",
            "execution": "Pilihan A tepat mendeskripsikan enkoding informasi koneksi ke dalam Initial Sequence Number (ISN) melalui TCP SYN Cookies."
        },
        "explanation": "Pada serangan TCP SYN Flood, penyerang mengirim ribuan paket SYN tanpa pernah membalas dengan ACK final, sehingga antrean SYN Backlog memori server penuh dan server crash. Solusi standar pada kernel Linux adalah mengaktifkan TCP SYN Cookies (`sysctl net.ipv4.tcp_syncookies = 1`). Saat diserang, server tidak lagi mengalokasikan blok memori (TCB) saat menerima SYN; sebaliknya, server menghitung Initial Sequence Number (ISN) kriptografis yang berisi informasi koneksi dan mengirimkannya pada paket SYN-ACK. Hanya jika klien membalas dengan ACK yang memuat nomor urut valid (cookie cocok), memori koneksi baru akan dialokasikan.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-08",
        "subject": "tkj",
        "materi": "ROUTING BERBASIS KEBIJAKAN (PBR) & MANGLE",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Pemisahan Trafik Menggunakan MikroTik Mangle & PBR",
        "type": "mcq",
        "questionHtml": "Di sebuah warnet gaming berkapasitas 50 client dengan dua koneksi ISP (ISP-1 dedicated untuk game online port UDP 5000-8000, ISP-2 untuk browsing web HTTP/HTTPS), administrator mengonfigurasi Policy-Based Routing (PBR) di MikroTik. Alur tahapan konfigurasi yang benar pada MikroTik RouterOS adalah...",
        "options": [
            {"key": "A", "text": "1. Tandai koneksi di /ip firewall mangle (mark-connection) -> 2. Tandai rute dari koneksi tersebut (mark-routing) -> 3. Buat default gateway di /ip route dengan routing-mark yang sesuai."},
            {"key": "B", "text": "1. Buat bridge antar kedua ISP -> 2. Masukkan seluruh port LAN ke bridge -> 3. Aktifkan DHCP snooping pada port game."},
            {"key": "C", "text": "1. Pasang aturan action=drop pada port 80 di mangle -> 2. Buat static DNS -> 3. Aktifkan proxy server internal."},
            {"key": "D", "text": "1. Set distance=1 pada kedua rute -> 2. Aktifkan OSPF pada interface LAN -> 3. Buat aturan filter forward accept."},
            {"key": "E", "text": "1. Gunakan Destination NAT mengarah ke IP ISP-1 -> 2. Matikan connection tracking router -> 3. Simpan konfigurasi."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "URUTAN EKSEKUSI POLICY-BASED ROUTING MIKROTIK",
            "latex": "\\text{Traffic Game} \\xrightarrow{\\text{Mangle}} \\texttt{mark-conn} \\xrightarrow{\\text{Mangle}} \\texttt{mark-routing='to\\_ISP1'} \\xrightarrow{\\text{IP Route}} \\texttt{gateway=IP\\_ISP1 routing-mark='to\\_ISP1'}",
            "legend": "• Menandai paket berdasarkan port/protokol (bukan hanya IP tujuan)<br>• Mengarahkan paket ke tabel routing khusus yang berbeda dari tabel main"
        },
        "hints": {
            "concept": "Best practice di MikroTik: Mangle mark-connection terlebih dahulu (karena lebih ringan dievaluasi), lalu mangle mark-routing pada koneksi tersebut, kemudian pasangkan routing-mark tersebut ke tabel routing (`/ip route`).",
            "execution": "Pilihan A tepat merinci alur: mark-connection -> mark-routing -> /ip route dengan routing-mark."
        },
        "explanation": "Policy-Based Routing (PBR) pada MikroTik mengarahkan lalu lintas data berdasarkan kriteria selain IP tujuan (misalnya port aplikasi game). Tahapan best practice: (1) Pada tabel `/ip firewall mangle`, buat aturan untuk menandai koneksi (`action=mark-connection`) yang mencocokkan protokol UDP dan rentang port 5000-8000; (2) Buat aturan mangle berikutnya untuk membaca connection-mark tersebut dan memberikan label rute (`action=mark-routing new-routing-mark=to-Game`); (3) Pada `/ip route`, tambahkan rute `0.0.0.0/0 gateway=IP-ISP1 routing-mark=to-Game`. Dengan demikian hanya trafik game yang melintasi ISP-1.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-09",
        "subject": "tkj",
        "materi": "JARINGAN NIRKABEL & WIRELESS",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Autentikasi Enterprise WPA2/WPA3 802.1X (RADIUS)",
        "type": "mcq",
        "questionHtml": "Sebuah universitas menerapkan keamanan Wi-Fi berbasis 802.1X EAP-TLS yang terintegrasi dengan server FreeRADIUS dan Certificate Authority (CA). Keunggulan arsitektural EAP-TLS dibandingkan metode PEAP-MSCHAPv2 adalah...",
        "options": [
            {"key": "A", "text": "Menggunakan autentikasi dua arah (mutual authentication) berbasis sertifikat digital X.509 baik di sisi server RADIUS maupun pada setiap perangkat klien (tanpa mengandalkan password)."},
            {"key": "B", "text": "Menghilangkan kebutuhan instalasi sertifikat pada sisi server sehingga konfigurasi lebih cepat."},
            {"key": "C", "text": "Mengizinkan pengguna login menggunakan akun media sosial tanpa perlu terdaftar di direktori institusi."},
            {"key": "D", "text": "Mengirimkan username dan password dalam format teks telanjang (clear-text) untuk memudahkan audit."},
            {"key": "E", "text": "Memperbolehkan perangkat klien menghubungkan diri ke Access Point tanpa perlu enkripsi RF."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "KOMPARASI PROTOKOL EAP WIRELESS ENTERPRISE",
            "latex": "\\begin{aligned} \\text{PEAP-MSCHAPv2:} & \\; \\text{Sertifikat di Server} + \\text{Username/Password di Klien (Rawan Phishing)} \\\\ \\text{EAP-TLS:} & \\; \\text{Sertifikat Digital di Server} + \\text{Sertifikat Digital di Klien (Paling Aman)} \\end{aligned}",
            "legend": "• EAP-TLS: Standar emas keamanan militer & korporasi (Zero Password Phishing)<br>• Jika laptop dicuri, sertifikat digitalnya dapat dicabut via CRL/OCSP"
        },
        "hints": {
            "concept": "EAP-TLS (Transport Layer Security) mensyaratkan kedua belah pihak (Server dan Klien) memiliki sertifikat digital (Mutual Authentication). Tidak ada password yang bisa ditebak atau dicuri melalui phishing.",
            "execution": "Pilihan A tepat mendeskripsikan autentikasi dua arah (mutual authentication) berbasis sertifikat digital X.509."
        },
        "explanation": "EAP-TLS (RFC 5216) adalah standar keamanan tertinggi untuk autentikasi nirkabel 802.1X. Berbeda dengan PEAP yang masih meminta username dan password dari pengguna (yang rentan terhadap serangan credential harvesting atau rogue AP phishing), EAP-TLS menerapkan autentikasi timbal balik (mutual authentication) murni berbasis sertifikat digital X.509: server memverifikasi sertifikat unik yang terinstal di perangkat klien, dan klien memverifikasi sertifikat server. Jika salah satu sertifikat tidak valid atau dicabut (revoked), akses ditolak seketika.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-10",
        "subject": "tkj",
        "materi": "LAYANAN JARINGAN & SERVER",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Redundansi Gateway Menggunakan VRRP (Virtual Router Redundancy)",
        "type": "mcq",
        "questionHtml": "Dua buah router MikroTik (R1 dan R2) dikonfigurasi fitur Virtual Router Redundancy Protocol (VRRP) versi 3 dengan Virtual IP `192.168.1.1` pada VRID 10:\n• R1: Priority = `150`\n• R2: Priority = `100`\nKedua router mengaktifkan parameter `preemption-mode=yes`. Jika R1 mengalami mati listrik selama 10 menit kemudian menyala kembali secara normal, perilaku transisi status VRRP yang terjadi pada kedua router adalah...",
        "options": [
            {"key": "A", "text": "Saat R1 mati, R2 langsung mengambil alih menjadi Master; ketika R1 menyala kembali, R1 segera mengambil alih kembali (preempt) menjadi Master karena nilai prioritasnya lebih tinggi (150 > 100)."},
            {"key": "B", "text": "R2 akan menjadi Master permanen selamanya dan menolak melepaskan status Master meskipun R1 sudah menyala normal kembali."},
            {"key": "C", "text": "Kedua router akan mengalami konflik split-brain sehingga alamat Virtual IP 192.168.1.1 mati total dari jaringan."},
            {"key": "D", "text": "R1 akan menjadi Backup permanen dan hanya menyala jika R2 juga ikut dimatikan oleh administrator."},
            {"key": "E", "text": "Klien di jaringan lokal harus merestart kartu jaringannya secara manual agar dapat terhubung kembali ke R1."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME PREEMPTION VRRP (RFC 5798)",
            "latex": "\\begin{aligned} \\text{R1 Down} &\\implies \\text{R2 (Priority 100) naik menjadi Master} \\\\ \\text{R1 Up (Priority 150) + Preempt=Yes} &\\implies \\text{R1 merebut kembali status Master} \\end{aligned}",
            "legend": "• Priority: Nilai tertinggi (1-254) menjadi Master pemegang Virtual MAC & VIP<br>• Preemption: Mengizinkan router berprioritas lebih tinggi merebut kembali hak Master"
        },
        "hints": {
            "concept": "Karena `preemption-mode=yes`, router dengan prioritas tertinggi (R1 = 150) berhak merebut kembali status Master ketika dirinya hidup kembali.",
            "execution": "R2 menjadi Master saat R1 mati, namun saat R1 hidup kembali, R1 langsung mengambil alih status Master kembali karena prioritasnya lebih besar (150 > 100)."
        },
        "explanation": "VRRP (Virtual Router Redundancy Protocol) menyediakan failover gateway otomatis transparan bagi klien. Router dengan priority tertinggi (R1 dengan nilai 150) terpilih sebagai Master. Jika R1 down, R2 (priority 100) mendeteksi hilangnya advertisement VRRP dan naik status menjadi Master. Berkat parameter `preemption-mode=yes`, ketika R1 selesai booting dan kembali online, R1 akan membandingkan prioritasnya yang lebih tinggi (150 vs 100) dan secara otomatis mengambil alih kembali peran Master router.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-11",
        "subject": "tkj",
        "materi": "VOIP & TELEKOMUNIKASI MULTIMEDIA",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Analisis Protokol Voice over IP: SIP Signaling vs RTP Media",
        "type": "mcq",
        "questionHtml": "Dalam sistem Voice over IP (VoIP) berbasis Asterisk PBX, panggilan telepon IP mengalami masalah aneh di mana dering panggilan tersambung normal, tombol panggil berfungsi, namun saat diangkat tidak ada suara sama sekali dari kedua belah pihak (one-way / no-way audio). Penyebab paling mendasar dari kegagalan komunikasi tersebut pada level protokol adalah...",
        "options": [
            {"key": "A", "text": "Protokol pensinyalan SIP (Session Initiation Protocol port UDP 5060) berhasil menembus firewall, namun aliran paket suara RTP (Real-time Transport Protocol port UDP rentang 10000-20000) terblokir oleh firewall atau mengalami kesalahan translasi NAT."},
            {"key": "B", "text": "Kabel serat optik tidak mendukung transmisi suara manusia melainkan hanya data teks digital."},
            {"key": "C", "text": "Server Asterisk kehabisan memori harddisk sehingga tidak dapat merekam percakapan."},
            {"key": "D", "text": "IP phone klien mengalami kerusakan fisik pada speaker handset secara bersamaan di kedua lokasi."},
            {"key": "E", "text": "Protokol DNS sekolah gagal melakukan resolusi reverse lookup alamat IPv6."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "PEMISAHAN PROTOKOL VOIP DUAL-STREAM",
            "latex": "\\begin{cases} \\text{Signaling (Call Setup):} & \\text{SIP (Session Initiation Protocol) - UDP/TCP 5060} \\\\ \\text{Media Audio (Voice Payload):} & \\text{RTP (Real-time Transport Protocol) - UDP 10000-20000} \\end{cases}",
            "legend": "• Masalah No-Audio / One-Way Audio klasik terjadi akibat NAT Traversal gagal pada RTP<br>• SIP Header mencantumkan IP privat lokal di dalam payload SDP"
        },
        "hints": {
            "concept": "VoIP memisahkan antara panggilan dering (Signaling lewat SIP) dan suara percakapan (Media stream lewat RTP). Dering lancar tapi suara hening berarti SIP tembus tetapi RTP diblokir/gagal NAT.",
            "execution": "Pilihan A tepat mendeskripsikan pemisahan alur SIP (port 5060) dan RTP (port 10000-20000)."
        },
        "explanation": "Arsitektur VoIP membedakan dua aliran protokol: (1) Signaling Channel menggunakan SIP (UDP port 5060) untuk proses panggilan dering, negosiasi codec, dan pemutusan hubungan; (2) Media Channel menggunakan RTP (UDP port dinamis, umumnya 10000 - 20000) untuk mentransmisikan paket suara digital secara real-time. Masalah klasik 'one-way audio' atau suara hening terjadi saat firewall hanya meloloskan port 5060 tetapi memblokir rentang port RTP, atau ketika router NAT tidak memiliki SIP ALG (Application Layer Gateway) sehingga alamat IP privat di dalam header SDP tidak ditranslasi dengan benar.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-12",
        "subject": "tkj",
        "materi": "SOFTWARE-DEFINED NETWORKING (SDN)",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Pemisahan Control Plane dan Data Plane pada Arsitektur SDN",
        "type": "mcq",
        "questionHtml": "Dalam paradigma Software-Defined Networking (SDN), arsitektur jaringan tradisional dirombak secara radikal. Perubahan fundamental yang diperkenalkan oleh SDN adalah...",
        "options": [
            {"key": "A", "text": "Memisahkan bidang kendali logika perutean (Control Plane) ke kontroler terpusat berbasis software, sementara switch fisik hanya bertugas meneruskan paket data murni (Data/Forwarding Plane) via protokol OpenFlow."},
            {"key": "B", "text": "Menghilangkan seluruh perangkat switch dan router fisik serta menggantinya murni dengan gelombang satelit nirkabel."},
            {"key": "C", "text": "Menggabungkan Management Plane dan Physical Plane ke dalam satu keping ASIC mikrokontroler."},
            {"key": "D", "text": "Mewajibkan setiap switch menjalankan protokol routing BGP full mesh secara desentralisasi penuh."},
            {"key": "E", "text": "Menolak seluruh paket data TCP dan hanya memperbolehkan transmisi frame mentah Ethernet."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "ARSITEKTUR DASAR SOFTWARE-DEFINED NETWORKING",
            "latex": "\\begin{aligned} \\text{Application Plane} &\\xrightarrow{\\text{Northbound API (REST/JSON)}} \\\\ \\text{Control Plane} &\\; \\text{(SDN Controller: ONOS, ODL, Ryu)} \\\\ &\\xrightarrow{\\text{Southbound API (OpenFlow/NETCONF)}} \\\\ \\text{Data Plane} &\\; \\text{(Flow Switches: Forwarding Engines)} \\end{aligned}",
            "legend": "• Tradisional: Control Plane & Data Plane bersatu di setiap router (Distributed)<br>• SDN: Control Plane terpusat (Centralized Intelligence), Data Plane terdistribusi sederhana"
        },
        "hints": {
            "concept": "Prinsip utama SDN: Decoupling Control Plane (otak pengambil keputusan) dari Data Plane (otot penerus paket).",
            "execution": "Pilihan A tepat menjelaskan pemisahan Control Plane ke controller terpusat dan Data Plane pada switch OpenFlow."
        },
        "explanation": "Pada arsitektur jaringan konvensional, setiap router atau switch mengelola keputusan peruteannya sendiri (Control Plane) dan meneruskan paket datanya sendiri (Data Plane) secara terdesentralisasi. SDN memisahkan kedua bidang ini secara tegas: Control Plane (logika routing, policy, manajemen) dipindahkan ke server perangkat lunak terpusat (SDN Controller), sementara perangkat keras jaringan (switch OpenFlow) hanya menjalankan Data/Forwarding Plane murni, yaitu mencocokkan paket ke tabel alur (Flow Table) dan meneruskannya dengan latensi minimal.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-13",
        "subject": "tkj",
        "materi": "TRANSISI IPV6 & MEKANISME DUAL STACK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Mekanisme Transisi NAT64 dan DNS64",
        "type": "mcq",
        "questionHtml": "Dalam migrasi jaringan IPv6-only modern (di mana klien di LAN hanya memiliki alamat IPv6 tanpa alamat IPv4 sama sekali), pengguna tetap harus dapat membuka web server lawas di internet yang hanya memiliki alamat IPv4 publik. Mekanisme transisi kombinasi yang digunakan untuk menjembatani komunikasi ini adalah...",
        "options": [
            {"key": "A", "text": "DNS64 (membuat alamat IPv6 sintetis dengan menyematkan IPv4 target ke prefix 64:ff9b::/96) dan NAT64 (menerjemahkan paket header IPv6 menjadi paket IPv4 murni pada router gateway)."},
            {"key": "B", "text": "6in4 Tunneling statis yang membutuhkan konfigurasi tunnel broker manual di setiap smartphone klien."},
            {"key": "C", "text": "Dual Stack murni di mana setiap komputer wajib memiliki dua alamat IPv4 dan IPv6 aktif."},
            {"key": "D", "text": "ISATAP (Intra-Site Automatic Tunnel Addressing Protocol) dengan memodifikasi routing OSPF area 0."},
            {"key": "E", "text": "Proxy HTTP transparan tanpa keterlibatan protokol DNS sama sekali."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME TRANSISI NAT64 & DNS64 (RFC 6146 / 6052)",
            "latex": "\\begin{aligned} \\text{Query DNS klien (AAAA)} &\\xrightarrow{\\text{DNS64}} \\text{Kombinasi } \\texttt{64:ff9b::} + \\text{IPv4 Hex} \\\\ \\text{Paket IPv6 Klien} &\\xrightarrow{\\text{Router NAT64}} \\text{Translasi ke IPv4 Asli} \\implies \\text{IPv4 Web Server} \\end{aligned}",
            "legend": "• Solusi hemat alamat: Mengizinkan klien murni IPv6 mengakses seluruh ekosistem IPv4 dunia<br>• Prefix Well-Known: 64:ff9b::/96"
        },
        "hints": {
            "concept": "Teknologi IPv6-only modern mengandalkan pasangan DNS64 (mengubah kueri domain menjadi format IPv6 buatan) dan NAT64 (mentranslasi paket IPv6 buatan tadi menjadi paket IPv4 nyata).",
            "execution": "Pilihan A tepat menjabarkan kolaborasi DNS64 dan NAT64."
        },
        "explanation": "Pada jaringan IPv6 murni (IPv6-only network), kombinasi DNS64 dan NAT64 menjadi standar transisi: Ketika klien IPv6 menanyakan domain IPv4, server DNS64 mendeteksi bahwa domain tersebut hanya memiliki Record 'A'. DNS64 kemudian menyintesis Record 'AAAA' palsu dengan menggabungkan prefix Well-Known `64:ff9b::/96` dengan alamat IPv4 target. Saat klien mengirim paket ke alamat sintetis tersebut, router NAT64 mencegat paket, mencopot header IPv6, dan menerjemahkannya menjadi paket IPv4 asli menuju server target di internet.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-14",
        "subject": "tkj",
        "materi": "KEAMANAN JARINGAN & FORENSIK LAYER 2",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Mitigasi Serangan ARP Spoofing menggunakan Dynamic ARP Inspection (DAI)",
        "type": "mcq",
        "questionHtml": "Seorang penyerang di jaringan LAN melakukan Man-in-the-Middle (MitM) attack menggunakan tools Ettercap/Cain & Abel dengan membanjiri jaringan menggunakan paket ARP Reply palsu untuk meracuni tabel ARP korban (ARP Cache Poisoning). Fitur keamanan switch manageable yang paling efektif untuk menggagalkan serangan ini adalah...",
        "options": [
            {"key": "A", "text": "Dynamic ARP Inspection (DAI) yang memvalidasi keabsahan paket ARP terhadap tabel database DHCP Snooping Binding."},
            {"key": "B", "text": "Storm Control untuk membatasi persentase broadcast data rate menjadi 10%."},
            {"key": "C", "text": "Spanning Tree PortFast pada seluruh antarmuka trunk uplink."},
            {"key": "D", "text": "Access Control List (ACL) statis yang memblokir protokol ICMP Echo Request."},
            {"key": "E", "text": "Mengaktifkan auto-MDIX pada semua kabel straight-through di switch."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME VALIDASI DYNAMIC ARP INSPECTION (DAI)",
            "latex": "\\text{Paket ARP Masuk} \\implies \\text{Cek IP-MAC Binding Table} \\begin{cases} \\text{Cocok dengan DHCP Snooping DB} &\\to \\text{Forward} \\\\ \\text{Tidak Cocok (Palsu/Spoofed)} &\\to \\text{Drop Langsung + Log Alert} \\end{cases}",
            "legend": "• Mengharuskan DHCP Snooping aktif terlebih dahulu<br>• Port yang menuju router/server diatur sebagai 'trusted', port user sebagai 'untrusted'"
        },
        "hints": {
            "concept": "Serangan ARP Poisoning di Layer 2 ditangkal oleh fitur Dynamic ARP Inspection (DAI) yang bekerja sama dengan DHCP Snooping.",
            "execution": "DAI mencegat semua paket ARP pada port untrusted dan mencocokkannya ke database DHCP Snooping. Jika ada klaim IP palsu, paket langsung dibuang."
        },
        "explanation": "Dynamic ARP Inspection (DAI) adalah fitur keamanan Layer 2 pada switch yang memvalidasi setiap paket ARP yang melintasi antarmuka untrusted. DAI membandingkan pasangan IP Address dan MAC Address pengirim di dalam paket ARP terhadap database sah yang dibangun oleh fitur DHCP Snooping. Jika penyerang mencoba mengklaim bahwa MAC address miliknya adalah IP default gateway (ARP Poisoning), switch mendeteksi ketidaksesuaian data binding dan seketika mendrop paket ARP palsu tersebut.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-15",
        "subject": "tkj",
        "materi": "DATA CENTER & CATU DAYA KELISTRIKAN",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Efisiensi Daya Data Center: Perhitungan Nilai PUE (Power Usage Effectiveness)",
        "type": "mcq",
        "questionHtml": "Audit efisiensi energi pada data center sebuah ISP mencatat konsumsi daya total fasilitas gedung sebesar $240\\text{ kW}$. Dari total konsumsi daya tersebut, daya listrik yang benar-benar dikonsumsi oleh perangkat komputasi IT (server, storage SAN, router backbone) adalah sebesar $160\\text{ kW}$, sedangkan sisanya dikonsumsi oleh pendingin Precision Air Conditioner (PAC), UPS loss, dan penerangan. Nilai Power Usage Effectiveness (PUE) data center tersebut beserta interpretasinya adalah...",
        "options": [
            {"key": "A", "text": "PUE = 1.50; menunjukkan efisiensi wajar di mana untuk setiap 1 Watt daya perangkat IT, dibutuhkan 0.5 Watt daya tambahan untuk pendingin dan fasilitas."},
            {"key": "B", "text": "PUE = 0.67; menunjukkan data center sangat efisien karena nilai berada di bawah ambang batas angka 1.0."},
            {"key": "C", "text": "PUE = 2.40; menunjukkan pemborosan daya ekstrem yang melebihi standar fasilitas Tier 4."},
            {"key": "D", "text": "PUE = 4.00; menunjukkan data center mengalami kebocoran arus listrik induksi."},
            {"key": "E", "text": "PUE = 1.00; menunjukkan efisiensi termodinamika sempurna tanpa adanya kehilangan energi."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "FORMULA STANDAR POWER USAGE EFFECTIVENESS (THE GREEN GRID)",
            "latex": "\\text{PUE} = \\frac{\\text{Total Facility Energy}}{\\text{IT Equipment Energy}} = \\frac{240\\,\\text{kW}}{160\\,\\text{kW}} = 1.50",
            "legend": "• Nilai PUE ideal teoretis = 1.0 (Seluruh daya masuk ke IT equipment)<br>• Rata-rata industri global: 1.5 - 1.8<br>• Hyperscale modern (Google/Meta): ~1.1 - 1.2"
        },
        "hints": {
            "concept": "PUE dihitung dari Total Daya Fasilitas dibagi Daya Perangkat IT. Nilai PUE tidak pernah bisa kurang dari 1.0.",
            "execution": "PUE = 240 kW / 160 kW = 1.50. Artinya, setiap 1 Watt daya IT membutuhkan 0.5 Watt daya overhead pendingin."
        },
        "explanation": "Power Usage Effectiveness (PUE) adalah metrik standar internasional yang dikembangkan oleh The Green Grid untuk mengukur efisiensi energi fasilitas data center: PUE = Total Daya Fasilitas / Daya Peralatan IT = 240 kW / 160 kW = 1.50. Angka 1.50 berarti bahwa dari setiap 1.5 Watt daya yang ditarik dari gardu PLN, 1.0 Watt diserap oleh server/perangkat jaringan, dan 0.5 Watt terpakai untuk sistem pendukung non-IT (seperti pendingin HVAC, chiller, lampu, dan inefisiensi konversi UPS).",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-16",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Penanganan Split Horizon dan Mesh pada iBGP Route Reflector",
        "type": "mcq",
        "questionHtml": "Dalam implementasi Internal BGP (iBGP) pada Autonomous System (AS) skala besar, aturan 'iBGP Split Horizon' melarang router meneruskan rute yang dipelajari dari satu tetangga iBGP ke tetangga iBGP lainnya. Untuk menghindari kebutuhan full mesh peering yang rumit ($N(N-1)/2$), solusi arsitektur yang digunakan adalah...",
        "options": [
            {"key": "A", "text": "BGP Route Reflector (RR) di mana router server diizinkan merefleksikan rute iBGP ke router Route Reflector Client."},
            {"key": "B", "text": "Menjalankan protokol OSPF di atas eBGP tanpa konfigurasi autonomous system number."},
            {"key": "C", "text": "Mengubah seluruh sesi koneksi TCP port 179 menjadi tunneling GRE unencrypted."},
            {"key": "D", "text": "Mengaktifkan fitur proxy ARP pada antarmuka loopback seluruh router internal."},
            {"key": "E", "text": "Menurunkan nilai Administrative Distance eBGP menjadi 200 sama dengan iBGP."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "SKALABILITAS PEERING IBGP DENGAN ROUTE REFLECTOR",
            "latex": "\\text{Full Mesh: } \\frac{N(N-1)}{2} \\text{ sesi} \\quad \\xrightarrow{\\text{Route Reflector}} \\quad N-1 \\text{ sesi peering terpusat}",
            "legend": "• Misal 50 router iBGP: Butuh 1.225 sesi peering -> Tidak skalabel!<br>• Dengan Route Reflector: Cukup terhubung ke RR server yang bertindak merefleksikan rute"
        },
        "hints": {
            "concept": "Dua solusi untuk memecahkan batas iBGP full-mesh: BGP Confederation atau BGP Route Reflector (RR).",
            "execution": "Pilihan A tepat: Route Reflector memodifikasi aturan iBGP split horizon sehingga dapat merefleksikan update rute ke RR clients."
        },
        "explanation": "Untuk mencegah routing loop di dalam satu Autonomous System, iBGP memiliki aturan Split Horizon: sebuah router dilarang meneruskan rute yang diterimanya dari tetangga iBGP ke tetangga iBGP lainnya. Ini mewajibkan setiap router memiliki peering langsung ke semua router lain (Full Mesh). Jika ada 100 router, dibutuhkan 4.950 sesi BGP. Solusi standar industri yang elegan adalah BGP Route Reflector (RFC 4456), di mana router tertentu ditunjuk sebagai server penampung dan pemancar ulang (reflector) rute ke client-clientnya.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-17",
        "subject": "tkj",
        "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Penguat Sinyal Optik EDFA (Erbium-Doped Fiber Amplifier)",
        "type": "mcq",
        "questionHtml": "Dalam sistem transmisi serat optik bawah laut antar pulau (submarine cable) berjarak ribuan kilometer, penguat sinyal optik jenis EDFA (Erbium-Doped Fiber Amplifier) dipasang di tengah laut. Keunggulan revolusioner EDFA dibandingkan repeater optoelektronik konvensional adalah...",
        "options": [
            {"key": "A", "text": "Memperkuat seluruh kanal panjang gelombang cahaya di jendela 1550 nm secara optik murni tanpa perlu mengonversi sinyal cahaya ke sinyal listrik terlebih dahulu (All-Optical Amplification)."},
            {"key": "B", "text": "Mampu memperbaiki frame data yang korup menggunakan algoritma Cyclomatic Redundancy Check."},
            {"key": "C", "text": "Menghilangkan redaman dispersi kromatik secara mutlak tanpa sisa delay sedikit pun."},
            {"key": "D", "text": "Tidak membutuhkan catu daya listrik eksternal sama sekali untuk memompa laser emisi."},
            {"key": "E", "text": "Dapat beroperasi pada kabel twisted pair tembaga sejauh 200 kilometer."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "PRINSIP KERJA OPTICAL AMPLIFIER EDFA",
            "latex": "\\text{Signal Optik (1530-1565 nm)} + \\text{Pump Laser (980/1480 nm)} \\xrightarrow{\\text{Erbium Ion Fiber}} \\text{Amplified Optical Output}",
            "legend": "• All-Optical: Tidak ada proses Optik -> Listrik -> Optik (O-E-O)<br>• Mampu menguatkan puluhan kanal DWDM secara serempak"
        },
        "hints": {
            "concept": "Teknologi EDFA menguatkan sinyal langsung di domain optik (cahaya) tanpa proses konversi ke listrik (O-E-O).",
            "execution": "Pilihan A tepat: penguatan optik murni (All-Optical) simultan pada pita C-band (1550 nm)."
        },
        "explanation": "Sebelum penemuan EDFA, transmisi optik jarak jauh memerlukan regenerator O-E-O yang mengubah sinyal optik menjadi sinyal listrik, memperkuatnya secara elektronik, lalu memancarkannya kembali dengan laser baru (sangat mahal dan lambat). EDFA (Erbium-Doped Fiber Amplifier) menggunakan inti serat kaca yang dicampur ion tanah jarang Erbium yang dieksitasi oleh laser pompa (pump laser 980/1480 nm). Ketika sinyal cahaya DWDM di pita 1550 nm melintas, emisi terstimulasi terjadi sehingga seluruh sinyal cahaya diperkuat secara instan di domain optik murni.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-18",
        "subject": "tkj",
        "materi": "KEAMANAN JARINGAN & FIREWALL",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Analisis Paket Handshake IPsec: IKEv2 Phase 1 vs Phase 2",
        "type": "mcq",
        "questionHtml": "Dalam pembangunan VPN Site-to-Site berbasis IPsec antara Kantor Pusat dan Kantor Cabang, proses negosiasi terbagi menjadi dua fase utama. Perbedaan substansial antara IKE Phase 1 dan IKE Phase 2 (IPsec SA) adalah...",
        "options": [
            {"key": "A", "text": "Phase 1 membangun terowongan terenkripsi yang aman antar kedua router (IKE SA), sedangkan Phase 2 menegosiasikan enkripsi transform set untuk melindungi lalu lintas data nyata klien LAN (IPsec SA)."},
            {"key": "B", "text": "Phase 1 mentransmisikan data file Word/PDF, sedangkan Phase 2 hanya melakukan ping diagnostik ICMP."},
            {"key": "C", "text": "Phase 1 menggunakan enkripsi simetris DES, sedangkan Phase 2 menggunakan enkripsi plain-text tanpa kunci."},
            {"key": "D", "text": "Phase 1 beroperasi di Network Layer, sedangkan Phase 2 beroperasi di Application Layer Nginx."},
            {"key": "E", "text": "Phase 1 dilakukan oleh teknisi manusia, sedangkan Phase 2 dijalankan oleh robot kecerdasan buatan."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "DUA FASE NEGOSIASI TEROWONGAN IPSEC",
            "latex": "\\begin{aligned} \\text{Phase 1 (IKE SA):} & \\; \\text{Autentikasi Router (PSK/Cert) + Diffie-Hellman Key Exchange} \\\\ \\text{Phase 2 (IPsec SA):} & \\; \\text{Negosiasi Transform Set (ESP-AES-GCM) + Enkripsi Data Pengguna LAN} \\end{aligned}",
            "legend": "• Phase 1 mengamankan percakapan antar kedua perangkat gateway VPN<br>• Phase 2 membangun terowongan data untuk trafik end-to-end klien"
        },
        "hints": {
            "concept": "Fase 1 membuat 'lorong aman untuk router berbicara' (IKE SA). Fase 2 membuat 'lorong di dalam lorong' untuk mengamankan data pengguna (IPsec SA).",
            "execution": "Pilihan A tepat mendeskripsikan perbedaan peran IKE SA (Phase 1) dan IPsec SA (Phase 2)."
        },
        "explanation": "Protokol IPsec membagi proses koneksi menjadi 2 fase: (1) IKE Phase 1: Kedua router VPN saling mengautentikasi identitas (menggunakan pre-shared key atau sertifikat digital) dan menjalankan Diffie-Hellman untuk membentuk saluran terenkripsi yang aman yang disebut IKE Security Association (IKE SA); (2) IKE Phase 2 (Quick Mode / Child SA): Di dalam saluran aman Fase 1 tersebut, kedua router menegosiasikan parameter enkripsi (seperti ESP AES-256 dan SHA-256) untuk membentuk IPsec SA yang secara nyata mengenkripsi dan mendekripsi payload data pengguna yang mengalir antar subnet LAN.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-19",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Penanganan Sub-optimal Routing pada Mutual Route Redistribution",
        "type": "mcq",
        "questionHtml": "Dua router perbatasan (R1 dan R2) menjalankan redistribusi rute timbal balik (mutual redistribution) antara protokol OSPF dan EIGRP secara simultan pada dua titik interkoneksi. Bahaya laten terbesar dari topologi mutual redistribution dual-point ini jika tidak dikonfigurasi dengan route-tagging adalah...",
        "options": [
            {"key": "A", "text": "Terjadinya routing loop dan sub-optimal routing karena rute yang diimpor dari EIGRP ke OSPF dapat diimpor kembali ke EIGRP dengan metrik yang tidak valid."},
            {"key": "B", "text": "Switch layer 2 akan mengalami kerusakan fisik pada port power supply PoE."},
            {"key": "C", "text": "Alamat IP privat klien LAN akan terkonversi otomatis menjadi alamat IP publik APNIC."},
            {"key": "D", "text": "Kecepatan propagasi cahaya pada kabel serat optik akan melambat hingga di bawah 100 km/detik."},
            {"key": "E", "text": "DNS server lokal akan berhenti melayani kueri resolusi domain .sch.id."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MITIGASI FEEDBACK LOOP PADA REDISTRIBUSI RUTE",
            "latex": "\\text{Route Tagging: } \\texttt{route-map OSPF->EIGRP set tag 100} \\implies \\texttt{route-map EIGRP->OSPF deny tag 100}",
            "legend": "• Menandai (tagging) rute saat keluar dari satu protokol<br>• Memblokir rute bertag tersebut agar tidak diumpan-balikkan (feedback) kembali"
        },
        "hints": {
            "concept": "Masalah klasik redistribusi dua arah pada dua router berbeda adalah 'Routing Feedback Loop' (rute melompat bolak-balik antar protokol). Solusinya adalah Route Tagging.",
            "execution": "Pilihan A tepat mengidentifikasi risiko routing loop dan sub-optimal routing akibat rute dipelajari kembali."
        },
        "explanation": "Pada topologi multi-homed mutual route redistribution (dua router meredistribusikan dua protokol routing berbeda), terjadi risiko fatal 'Routing Feedback Loop'. Rute yang berasal dari domain OSPF dapat diredistribusikan ke EIGRP oleh Router 1, lalu dipelajari oleh Router 2 dan diredistribusikan kembali ke OSPF dengan metrik yang lebih disukai (misalnya karena perbedaan Administrative Distance). Akibatnya terjadi sub-optimal routing atau paket berputar-putar tanpa akhir. Mitigasi wajibnya adalah menggunakan Route Map untuk menandai (tag) rute saat keluar dan memfilter rute bertag tersebut agar tidak diimpor ulang.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-20",
        "subject": "tkj",
        "materi": "MANAJEMEN BANDWIDTH & QOS",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Arsitektur Differentiated Services (DiffServ) & PHB Expedited Forwarding",
        "type": "mcq",
        "questionHtml": "Dalam penerapan Quality of Service (QoS) enterprise berbasis model Differentiated Services (DiffServ RFC 2474), paket suara VoIP harus diberikan prioritas tertinggi dengan latensi dan jitter mendekati nol. Nilai Differentiated Services Code Point (DSCP) standar yang wajib disematkan pada header IPv4 paket VoIP tersebut adalah...",
        "options": [
            {"key": "A", "text": "DSCP Expedited Forwarding (EF) dengan nilai biner 101110 (desimal 46)."},
            {"key": "B", "text": "DSCP Best Effort (BE) dengan nilai biner 000000 (desimal 0)."},
            {"key": "C", "text": "DSCP Assured Forwarding 11 (AF11) dengan nilai desimal 10."},
            {"key": "D", "text": "DSCP Class Selector 1 (CS1) dengan nilai desimal 8."},
            {"key": "E", "text": "DSCP Assured Forwarding 43 (AF43) dengan nilai desimal 38."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MAPPING DIFFSERV DSCP EXPEDITED FORWARDING",
            "latex": "\\text{DSCP Field (6 bit)} = \\mathbf{101110}_2 = 46_{10} \\implies \\text{Per-Hop Behavior: Expedited Forwarding (EF)}",
            "legend": "• EF (46): Jalur antrean khusus Priority Queue (PQ) untuk VoIP suara real-time<br>• AF (Assured Forwarding): Untuk video streaming dan data bisnis<br>• BE (0): Default best effort untuk browsing umum"
        },
        "hints": {
            "concept": "Kelas tertinggi untuk trafik suara real-time pada DiffServ adalah Expedited Forwarding (EF) dengan kode desimal 46.",
            "execution": "Pilihan A tepat: DSCP Expedited Forwarding (EF) nilai desimal 46 (biner 101110)."
        },
        "explanation": "Model Differentiated Services (DiffServ) memetakan 6-bit field DSCP pada header IP untuk menentukan perilaku penanganan antrean (Per-Hop Behavior / PHB) di setiap router. Untuk trafik audio VoIP interaktif yang sangat sensitif terhadap delay dan jitter, standar IETF menetapkan kelas 'Expedited Forwarding' (EF) dengan nilai biner `101110` (desimal 46). Router yang mengenali tanda EF akan memasukkan paket tersebut ke dalam antrean Strict Priority Queue (PQ) untuk dikirimkan terlebih dahulu sebelum antrean lainnya.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-21",
        "subject": "tkj",
        "materi": "JARINGAN NIRKABEL & WIRELESS",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Teknologi Wi-Fi 6 (802.11ax): OFDMA vs MU-MIMO",
        "type": "mcq",
        "questionHtml": "Standar Wi-Fi 6 (IEEE 802.11ax) dirancang khusus untuk menangani lingkungan berkepadatan tinggi (high-density clients) seperti stadion dan ruang ujian SMK. Teknologi inti yang memungkinkan satu kanal radio frekuensi dipecah menjadi beberapa alokasi sub-carrier frekuensi kecil (Resource Units / RU) untuk melayani transmisi data dari beberapa perangkat klien secara serentak dalam satu waktu adalah...",
        "options": [
            {"key": "A", "text": "OFDMA (Orthogonal Frequency Division Multiple Access)."},
            {"key": "B", "text": "CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)."},
            {"key": "C", "text": "DSSS (Direct Sequence Spread Spectrum)."},
            {"key": "D", "text": "FHSS (Frequency Hopping Spread Spectrum)."},
            {"key": "E", "text": "BSS Coloring berbasis token ring analog."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME OFDMA RESOURCE UNITS (RU)",
            "latex": "1\\,\\text{Kanal 20 MHz} \\xrightarrow{\\text{OFDMA}} \\text{Hingga 9 Resource Units (RU 26-tone)} \\implies 9\\,\\text{Klien Simultan}",
            "legend": "• Wi-Fi 5 (OFDM): 1 Transmisi menguasai seluruh lebar kanal 20 MHz (Monopoli)<br>• Wi-Fi 6 (OFDMA): Kanal dibagi menjadi sub-saluran Resource Units (Multi-User efisien)"
        },
        "hints": {
            "concept": "Teknologi yang memecah spektrum frekuensi menjadi Resource Units (RU) kecil untuk melayani banyak user secara simultan diadaptasi dari teknologi seluler 4G/5G, yaitu OFDMA.",
            "execution": "Pilihan A tepat: OFDMA (Orthogonal Frequency Division Multiple Access)."
        },
        "explanation": "Pada standar Wi-Fi 5 ke bawah (OFDM konvensional), ketika sebuah klien mentransmisikan data, klien tersebut memonopoli seluruh spektrum kanal 20/40/80 MHz meskipun data yang dikirim hanya beberapa byte (misalnya paket ACK atau game packet kecil). Wi-Fi 6 memperkenalkan OFDMA (diadopsi dari teknologi seluler LTE/5G) yang membagi kanal menjadi sub-carrier ortogonal kecil yang disebut Resource Units (RU). Hal ini memungkinkan Access Point melayani hingga puluhan perangkat klien secara simultan dalam satu rentang waktu frame transmisi.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-22",
        "subject": "tkj",
        "materi": "ANALISIS PAKET DATA & TROUBLESHOOTING",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Investigasi TCP Retransmission dan Duplicate ACK",
        "type": "mcq",
        "questionHtml": "Dalam tangkapan paket Wireshark pada koneksi database server, teknisi menemukan rentetan 3 paket `TCP Dup ACK` berturut-turut yang dikirimkan oleh klien, diikuti seketika oleh paket `TCP Fast Retransmission` dari server. Interpretasi teknis yang benar dari kejadian tersebut adalah...",
        "options": [
            {"key": "A", "text": "Klien menerima segmen TCP yang melompati urutan (out-of-order), mengindikasikan ada satu paket di tengah yang hilang (packet loss), sehingga memicu mekanisme Fast Retransmit server tanpa menunggu Retransmission Timeout (RTO)."},
            {"key": "B", "text": "Server mengalami serangan Denial of Service sehingga menolak memproses query database."},
            {"key": "C", "text": "Kabel LAN mengalami korsleting listrik sehingga seluruh data heksadesimal terbalik nilainya."},
            {"key": "D", "text": "Klien telah logout dari sesi database dan server menyetujui pemutusan koneksi dengan flag FIN."},
            {"key": "E", "text": "Switch core sedang melakukan pembaharuan firmware sehingga semua antarmuka masuk mode standby."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME TCP FAST RETRANSMIT (RFC 5681)",
            "latex": "3\\times \\text{Duplicate ACKs} \\implies \\text{Segera kirim ulang paket hilang (Bypass RTO Timer)}",
            "legend": "• Menghindari penundaan panjang akibat menunggu timer RTO (bisa 200ms - 1 detik)<br>• Menjaga throughput TCP tetap optimal saat terjadi kehilangan paket acak"
        },
        "hints": {
            "concept": "Aturan TCP Fast Retransmit: ketika pengirim menerima 3 Duplicate ACK untuk sequence number yang sama, pengirim menyimpulkan paket tersebut hilang dan langsung mengirimkannya kembali tanpa menunggu RTO timeout.",
            "execution": "Pilihan A tepat menjelaskan fenomena penerimaan paket out-of-order dan pemicuan Fast Retransmit."
        },
        "explanation": "Ketika penerima TCP mendeteksi adanya celah urutan dalam aliran data yang diterimanya (misalnya menerima segmen 1, lalu langsung menerima segmen 3 karena segmen 2 hilang di jaringan), penerima akan mengirimkan paket ACK dengan nomor urut segmen 2 yang belum diterimanya. Saat menerima segmen berikutnya (segmen 4 dan 5), penerima tetap membalas dengan ACK untuk segmen 2 (disebut Duplicate ACK). Ketika pengirim menerima 3 Duplicate ACK yang identik, algoritma Fast Retransmit TCP menyimpulkan segmen 2 hilang dan langsung mentransmisikan ulang segmen 2 seketika tanpa perlu menunggu timer RTO (Retransmission Timeout) habis.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-23",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Konsep BGP AS-Path Prepending untuk Traffic Engineering Inbound",
        "type": "mcq",
        "questionHtml": "Sebuah penyedia jasa internet (ISP) lokal memiliki nomor Autonomous System `AS 64512` dan terhubung ke dua upstream Tier-1 (ISP-A dan ISP-B). Administrator ingin agar seluruh lalu lintas data masuk (inbound traffic dari internet global) hanya mengalir melalui ISP-A, sedangkan ISP-B hanya menjadi cadangan. Teknik BGP Path Attribute yang harus diimplementasikan pada sesi eBGP ke arah ISP-B adalah...",
        "options": [
            {"key": "A", "text": "AS-Path Prepending (menyisipkan nomor AS sendiri berulang kali, misal: '64512 64512 64512', pada pengumuman prefix ke arah ISP-B agar rute tampak lebih panjang dan dijauhi)."},
            {"key": "B", "text": "Menaikkan nilai Local Preference pada pengumuman prefix yang dikirim keluar ke arah ISP-B."},
            {"key": "C", "text": "Menyetel nilai Weight menjadi 65535 pada antarmuka yang mengarah ke ISP-B."},
            {"key": "D", "text": "Menghapus default gateway ISP-A dari tabel routing BGP lokal."},
            {"key": "E", "text": "Mengaktifkan mode bridge transparan pada router border eBGP."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "TEKNIK AS-PATH PREPENDING UNTUK INBOUND TRAFFIC",
            "latex": "\\begin{aligned} \\text{Iklan ke ISP-A:} & \\; \\text{AS-Path} = [64512] \\quad (\\text{Panjang}=1) \\implies \\mathbf{Dipilih\\;Dunia} \\\\ \\text{Iklan ke ISP-B:} & \\; \\text{AS-Path} = [64512\\; 64512\\; 64512] \\quad (\\text{Panjang}=3) \\implies \\text{Dijauhi} \\end{aligned}",
            "legend": "• Local Preference hanya mengontrol Outbound traffic lokal<br>• AS-Path Prepending mempengaruhi keputusan perutean router global di internet (Inbound)"
        },
        "hints": {
            "concept": "Untuk mengontrol lalu lintas yang MASUK dari internet luar (inbound), kita harus membuat rute yang tidak diinginkan terlihat jelek di mata dunia luar. Caranya adalah memanjangkan AS Path-nya dengan mengulang AS sendiri (AS-Path Prepending).",
            "execution": "Pilihan A tepat: AS-Path Prepending ke arah ISP-B membuat rute melalui ISP-B terlihat lebih panjang (kurang diminati)."
        },
        "explanation": "Mengatur lalu lintas keluar (outbound traffic) dari AS lokal sangat mudah menggunakan atribut Local Preference. Namun untuk mempengaruhi lalu lintas yang masuk (inbound traffic) dari seluruh dunia, administrator harus memanipulasi atribut yang dievaluasi oleh router di internet publik. Teknik standar industri yang paling efektif adalah 'AS-Path Prepending': administrator mengiklankan prefix jaringannya ke ISP cadangan (ISP-B) dengan menambahkan nomor AS-nya sendiri berkali-kali. Router di internet global yang melihat rute via ISP-B memiliki AS Path lebih panjang akan memprioritaskan rute via ISP-A yang lebih pendek.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-24",
        "subject": "tkj",
        "materi": "LAYANAN JARINGAN & SERVER",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Arsitektur Anycast DNS untuk Skalabilitas dan DDoS Resistance",
        "type": "mcq",
        "questionHtml": "Penyedia DNS publik terkemuka seperti Google Public DNS (`8.8.8.8`) dan Cloudflare (`1.1.1.1`) menggunakan metode perutean 'Anycast' pada ratusan data center di seluruh dunia. Prinsip operasional teknologi BGP Anycast tersebut adalah...",
        "options": [
            {"key": "A", "text": "Mengiklankan alamat IP publik yang sama persis (misal 8.8.8.8) dari ratusan lokasi server berbeda melalui protokol BGP, sehingga kueri pengguna secara alami diarahkan ke data center terdekat secara topologi perutean."},
            {"key": "B", "text": "Menyimpan seluruh data internet global di dalam satu komputer server tunggal supercepat di Amerika Serikat."},
            {"key": "C", "text": "Mengubah paket data UDP port 53 menjadi transmisi radio satelit gelombang mikro antariksa."},
            {"key": "D", "text": "Mewajibkan pengguna memasukkan password token digital sebelum kueri DNS dijawab oleh server."},
            {"key": "E", "text": "Menduplikasi setiap pertanyaan kueri DNS ke seluruh server di dunia secara broadcast simultan."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME BGP ANYCAST ROUTING",
            "latex": "1\\,\\text{IP Address Target (8.8.8.8)} \\iff N\\,\\text{Server Fisik di Seluruh Dunia (BGP PoP)}",
            "legend": "• Klien Jakarta -> BGP mengarahkan ke Node Jakarta (Latency < 5 ms)<br>• Klien London -> BGP mengarahkan ke Node London<br>• DDoS Resilience: Beban serangan terdistribusi dan terserap secara lokal per-region"
        },
        "hints": {
            "concept": "Anycast: 'Satu alamat IP diumumkan dari banyak lokasi berbeda'. Protokol BGP akan membawa trafik pengguna ke lokasi terdekat secara metrik jaringan.",
            "execution": "Pilihan A tepat mendeskripsikan pengiklanan satu IP identik dari berbagai lokasi melalui BGP Anycast."
        },
        "explanation": "Pada arsitektur Anycast BGP, satu alamat IP tunggal (seperti 8.8.8.8) dikonfigurasikan pada ratusan server Point of Presence (PoP) di berbagai penjuru dunia dan diiklankan ke tabel perutean global internet via BGP. Ketika pengguna di Indonesia melakukan kueri DNS, router internet akan memilih jalur BGP terpendek menuju server Google terdekat di Jakarta atau Singapura, sementara pengguna di Jerman akan diarahkan ke Frankfurt. Selain memangkas latensi, Anycast sangat tangguh terhadap serangan DDoS karena beban trafik serangan secara alami terpecah dan terserap di masing-masing node regional.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-h-25",
        "subject": "tkj",
        "materi": "K3LH & KETENAGAKERJAAN TJKT",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Sistem Proteksi Kebakaran Clean Agent Data Center (FM-200 / Novec 1230)",
        "type": "mcq",
        "questionHtml": "Di ruang server data center modern tier-3 yang memuat ratusan server bernilai miliaran rupiah, penggunaan sistem pemadam kebakaran semprotan air otomatis (water sprinkler) dilarang keras untuk pemadaman utama. Sistem pemadam kebakaran yang wajib digunakan adalah sistem gas Clean Agent (seperti Novec 1230 atau FM-200 / HFC-227ea). Alasan teknis pemilihan sistem gas clean agent tersebut adalah...",
        "options": [
            {"key": "A", "text": "Tidak menghantarkan arus listrik (non-konduktif), tidak meninggalkan residu kimiawi korosif yang merusak sirkuit elektronik, dan aman bagi manusia di dalam ruangan pada konsentrasi desain standar."},
            {"key": "B", "text": "Membekukan seluruh ruangan server hingga mencapai suhu nol mutlak (-273 derajat Celsius)."},
            {"key": "C", "text": "Membanjiri ruangan dengan air bertekanan tinggi yang telah dihilangkan mineral garamnya."},
            {"key": "D", "text": "Menghilangkan seluruh gas oksigen hingga 0% dalam waktu kurang dari 1 detik."},
            {"key": "E", "text": "Bereaksi secara kimiawi membakar habis seluruh bahan plastik isolator kabel jaringan."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "STANDAR SISTEM PEMADAM CLEAN AGENT (NFPA 2001)",
            "latex": "\\text{Total Flooding System (Novec 1230 / FM-200)} \\implies \\text{Heat Absorption} + \\text{Zero Electrical Damage}",
            "legend": "• Water Sprinkler: Menyebabkan hubungan arus pendek fatal pada server bertegangan<br>• Bubuk Kimia (Dry Chemical): Meninggalkan residu garam korosif yang merusak PCB motherboard<br>• Clean Agent: Menguap seketika tanpa residu sama sekali"
        },
        "hints": {
            "concept": "Air dan bubuk kimia biasa akan menghancurkan server elektronik. Gas Clean Agent memadamkan api dengan menyerap panas tanpa menghantarkan listrik dan tanpa meninggalkan residu.",
            "execution": "Pilihan A tepat: non-konduktif, tidak meninggalkan residu korosif, dan aman bagi personil."
        },
        "explanation": "Standar NFPA 2001 mengatur tentang Sistem Pemadam Kebakaran Gas Bersih (Clean Agent Extinguishing Systems). Penggunaan air bertekanan pada perangkat server yang menyala akan memicu hubungan pendek arus listrik (short circuit) dan ledakan, sedangkan bubuk kimia kering (dry powder) akan merusak komponen mikroelektronika motherboard karena bersifat korosif dan abrasif. Gas Clean Agent (seperti Novec 1230 atau FM-200) bekerja memadamkan api melalui penyerapan energi panas secara kimiawi dan fisik, tidak menghantarkan listrik, menguap tanpa meninggalkan residu apa pun, dan memiliki batas aman NOAEL (No Observed Adverse Effect Level) bagi personil teknisi yang sedang berada di dalam ruang server.",
        "isDiagnostic": False
    }
]
