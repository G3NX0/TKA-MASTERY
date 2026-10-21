# -*- coding: utf-8 -*-
"""
tkj_data_easy.py
25 Unique Authentic Easy Items for TKA 2026 Teknik Jaringan Komputer dan Telekomunikasi (TJKT / TKJ).
Strictly aligned with Pusmendik TKA 2026 & BSKAP 033/H/KR/2024.
Zero AI Slop - Zero Duplicates.
"""

TKJ_EASY = [
    {
        "id": "tkj-lat-e-01",
        "subject": "tkj",
        "materi": "PENGALAMATAN IPV4 & SUBNETTING",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Kalkulasi Subnet Mask IPv4 CIDR",
        "type": "mcq",
        "questionHtml": "Sebuah lab komputer sekolah membutuhkan alokasi IP untuk 28 unit komputer klien dan 1 unit printer jaringan (total 29 host). Prefix subnet mask paling hemat (efisien) yang harus dipilih administrator adalah...",
        "options": [
            {"key": "A", "text": "/27 dengan subnet mask 255.255.255.224 yang menyediakan kapasitas maksimum 30 usable host."},
            {"key": "B", "text": "/28 dengan subnet mask 255.255.255.240 yang menyediakan kapasitas maksimum 14 usable host."},
            {"key": "C", "text": "/26 dengan subnet mask 255.255.255.192 yang menyediakan kapasitas maksimum 62 usable host."},
            {"key": "D", "text": "/25 dengan subnet mask 255.255.255.128 yang menyediakan kapasitas maksimum 126 usable host."},
            {"key": "E", "text": "/24 dengan subnet mask 255.255.255.0 yang menyediakan kapasitas maksimum 254 usable host."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "FORMULA KALKULASI USABLE HOST IPV4",
            "latex": "\\text{Usable Host} = 2^{(32 - \\text{prefix})} - 2 \\ge \\text{Host Dibutuhkan}",
            "legend": "• 32: Panjang total bit IPv4<br>• -2: Dikurangi Network ID dan Broadcast ID<br>• Prefix /27: 2^(32-27) - 2 = 32 - 2 = 30 host"
        },
        "hints": {
            "concept": "Hitung pangkat dua terkecil yang lebih besar dari total host + 2. Kebutuhan 29 host memerlukan minimal 31 alamat, sehingga blok ukuran 32 (prefix /27) adalah yang paling pas.",
            "execution": "Prefix /28 hanya menyediakan 14 host (kurang). Prefix /27 menyediakan 30 host (mencukupi 29 host dengan sisa 1). Prefix /26 ke atas terlalu boros."
        },
        "explanation": "Pada subnetting IPv4, jumlah host yang dapat dialokasikan dihitung dengan rumus 2^(32 - prefix) - 2. Untuk 29 perangkat, dibutuhkan minimal 31 alamat (termasuk Network ID dan Broadcast ID). Pangkat 2 terdekat adalah 2^5 = 32 alamat, yang berkorespondensi dengan prefix 32 - 5 = /27 (255.255.255.224), menghasilkan 30 usable host. Pilihan A adalah yang paling efisien.",
        "isDiagnostic": True
    },
    {
        "id": "tkj-lat-e-02",
        "subject": "tkj",
        "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Karakteristik Kabel Twisted Pair UTP Cat 6",
        "type": "mcq",
        "questionHtml": "Standar kabel Twisted Pair Unshielded (UTP) Kategori 6 (Cat 6) dirancang untuk mentransmisikan data Gigabit Ethernet. Batas jarak maksimum segmen kabel horizontal dari switch ke workstation tanpa repeater menurut standar TIA/EIA-568 adalah...",
        "options": [
            {"key": "A", "text": "100 meter (90 meter kabel solid horizontal + 10 meter total patch cord)."},
            {"key": "B", "text": "50 meter untuk menjaga redaman sinyal frekuensi tinggi di bawah 100 MHz."},
            {"key": "C", "text": "185 meter mengikuti spesifikasi standar transmisi 10BASE2 koaksial tipis."},
            {"key": "D", "text": "250 meter dengan syarat menggunakan konektor modular berpelindung RJ-45 Cat 6A."},
            {"key": "E", "text": "500 meter jika dihubungkan secara point-to-point tanpa melewati patch panel."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "STANDAR PANJANG KABEL TIA/EIA-568",
            "latex": "L_{\\text{channel}} = L_{\\text{permanent link}} (90\\text{ m}) + L_{\\text{patch cords}} (10\\text{ m}) = 100\\text{ m}",
            "legend": "• Permanent Link: Rentang kabel dinding terpasang tetap (maks 90 m)<br>• Channel Link: Total lintasan ujung-ke-ujung (maks 100 m)"
        },
        "hints": {
            "concept": "Standar industri telekomunikasi TIA/EIA untuk kabel twisted pair tembaga (Cat 5e, Cat 6, Cat 6A) membatasi panjang total kanal transmisi Ethernet.",
            "execution": "Panjang maksimal segmen saluran kabel tembaga Ethernet adalah tepat 100 meter untuk mencegah degradasi propagasi sinyal dan collision window."
        },
        "explanation": "Berdasarkan standar TIA/EIA-568.2-D, batas panjang kanal (Channel Link) kabel UTP dari switch ke perangkat akhir adalah 100 meter, yang terdiri atas 90 meter kabel permanent link di dalam dinding/plafon ditambah total 10 meter kabel patch cord fleksibel. Melebihi 100 meter akan menimbulkan redaman sinyal (attenuation) dan delay propagasi yang merusak frame Ethernet.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-03",
        "subject": "tkj",
        "materi": "MODEL OSI & PROTOKOL INTERNET",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Pemetaan Perangkat Jaringan pada Layer OSI",
        "type": "mcq",
        "questionHtml": "Sebuah switch unmanaged layer 2 bekerja dengan membaca header frame untuk meneruskan paket data ke port tujuan. Identitas perangkat yang digunakan oleh switch layer 2 untuk membuat tabel forwarding adalah...",
        "options": [
            {"key": "A", "text": "MAC Address tujuan (Media Access Control 48-bit hex) pada Data Link Layer."},
            {"key": "B", "text": "IP Address tujuan (Logical Address 32-bit biner) pada Network Layer."},
            {"key": "C", "text": "Port Number aplikasi tujuan (Transport Port 16-bit) pada Transport Layer."},
            {"key": "D", "text": "Domain Name System FQDN melalui query balik pada Application Layer."},
            {"key": "E", "text": "Sequence Number dan Acknowledgment Number pada sesi TCP handshake."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "STRUKTUR IDENTITAS LAYER 2",
            "latex": "\\text{MAC} = \\underbrace{\\text{XX:XX:XX}}_{\\text{OUI (Vendor)}} : \\underbrace{\\text{XX:XX:XX}}_{\\text{NIC Serial}} \\quad (48\\text{ bit})",
            "legend": "• Data Link Layer (OSI Layer 2): Mengatur framing dan addressing fisik<br>• Switch CAM Table: Memetakan MAC Address ke nomor Port fisik switch"
        },
        "hints": {
            "concept": "Ingat perbedaan perangkat Layer 2 (Switch/Bridge) yang membaca alamat fisik (MAC) dengan perangkat Layer 3 (Router) yang membaca alamat logika (IP).",
            "execution": "Switch unmanaged Layer 2 beroperasi di Data Link Layer dan menggunakan MAC Address pada CAM Table untuk meneruskan frame."
        },
        "explanation": "Switch Layer 2 bekerja pada Data Link Layer dalam model OSI. Perangkat ini membaca alamat fisik perangkat yang disebut MAC Address (48-bit) yang tercantum di header frame Ethernet. Switch menyimpan pemetaan antara MAC Address pengirim dengan nomor port fisiknya di dalam CAM (Content Addressable Memory) Table untuk meneruskan frame langsung ke port tujuan tanpa broadcast berulang.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-04",
        "subject": "tkj",
        "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Perbedaan Serat Optik Single Mode vs Multi Mode",
        "type": "mcq",
        "questionHtml": "Dalam instalasi tulang punggung (backbone) antar gedung berjarak 5 kilometer, teknisi telekomunikasi memilih kabel fiber optik Single Mode (SMF) daripada Multi Mode (MMF). Alasan teknis utama pemilihan tersebut adalah...",
        "options": [
            {"key": "A", "text": "Diameter inti SMF sangat kecil (±9 µm) sehingga dispersi modal rendah dan sinyal mampu menjangkau jarak jauh."},
            {"key": "B", "text": "Diameter inti SMF sangat besar (±50 µm) sehingga mampu menampung banyak panjang gelombang cahaya LED murah."},
            {"key": "C", "text": "Kabel SMF tidak memerlukan perangkat pemancar berbasis laser melainkan cukup menggunakan lampu LED inframerah biasa."},
            {"key": "D", "text": "Kabel SMF kebal terhadap efek tekukan tajam (macrobending) tanpa mengalami redaman daya sama sekali."},
            {"key": "E", "text": "Biaya terminasi dan konektor SMF jauh lebih murah serta tidak membutuhkan proses fusion splicing presisi."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "KARAKTERISTIK CORE FIBER OPTIK",
            "latex": "\\text{Core}_{\\text{SMF}} \\approx 9\\,\\mu\\text{m} \\quad \\text{vs} \\quad \\text{Core}_{\\text{MMF}} \\approx 50/62.5\\,\\mu\\text{m}",
            "legend": "• SMF: Menggunakan sumber cahaya Laser Diode, 1 mode perambatan, jarak > 10 km<br>• MMF: Menggunakan VCSEL/LED, banyak mode perambatan, jarak < 2 km"
        },
        "hints": {
            "concept": "Perhatikan kata 'Single Mode': hanya satu mode (berkas cahaya lurus) yang merambat karena intinya sangat kecil, meminimalkan pelebaran pulsa (dispersi modal).",
            "execution": "Single Mode Core 9 mikron dengan laser menjangkau puluhan kilometer. Multi Mode core 50-62.5 mikron mengalami dispersi modal tinggi sehingga terbatas untuk jarak pendek."
        },
        "explanation": "Fiber optik Single Mode (SMF) memiliki diameter core yang sangat tipis (sekitar 8-10 mikrometer). Ukuran kecil ini memaksa cahaya merambat hanya melalui satu lintasan lurus tunggal tanpa memantul ke dinding cladding (tidak ada dispersi modal / modal dispersion). Akibatnya, pelebaran pulsa cahaya sangat minimal dan sinyal dapat menjangkau jarak puluhan kilometer dengan redaman rendah.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-05",
        "subject": "tkj",
        "materi": "LAYANAN JARINGAN & SERVER",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Mekanisme Kerja Protokol DHCP (DORA)",
        "type": "mcq",
        "questionHtml": "Saat sebuah komputer klien pertama kali dinyalakan dan diatur untuk memperoleh IP Address secara otomatis, urutan 4 tahap komunikasi (handshake) protokol DHCP yang benar adalah...",
        "options": [
            {"key": "A", "text": "Discover, Offer, Request, dan Acknowledgment (DORA)."},
            {"key": "B", "text": "Request, Offer, Discover, dan Acknowledgment (RODA)."},
            {"key": "C", "text": "Solicit, Advertise, Request, dan Confirm (SARC)."},
            {"key": "D", "text": "Query, Response, Association, dan Verification (QRAV)."},
            {"key": "E", "text": "Handshake, Allocation, Binding, dan Termination (HABT)."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "SIKLUS PROTOKOL DHCP (DORA)",
            "latex": "\\text{Client} \\xrightarrow{\\text{Discover}} \\text{Server} \\xrightarrow{\\text{Offer}} \\text{Client} \\xrightarrow{\\text{Request}} \\text{Server} \\xrightarrow{\\text{Ack}} \\text{Client}",
            "legend": "• Discover: Broadcast mencari DHCP server (UDP 67)<br>• Offer: Penawaran IP dari server (UDP 68)<br>• Request: Klien meminta IP yang ditawarkan<br>• Ack: Konfirmasi penyewaan (Lease Time)"
        },
        "hints": {
            "concept": "Hafalkan akronim universal protokol DHCP: D-O-R-A.",
            "execution": "Klien mencari (Discover), Server menawar (Offer), Klien meminta resmi (Request), Server menyetujui (Acknowledgment)."
        },
        "explanation": "Siklus pengalokasian IP address secara dinamis oleh Dynamic Host Configuration Protocol (DHCP) mengikuti tahapan DORA: (1) DHCP Discover: klien mengirim broadcast mencari server; (2) DHCP Offer: server menawarkan konfigurasi IP; (3) DHCP Request: klien mengonfirmasi menerima penawaran tersebut; (4) DHCP ACK (Acknowledgment): server mencatat IP lease dan memberikan konfirmasi final ke klien.",
        "isDiagnostic": True
    },
    {
        "id": "tkj-lat-e-06",
        "subject": "tkj",
        "materi": "PENGALAMATAN IPV4 & SUBNETTING",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Identifikasi Blok Alamat IP Private RFC 1918",
        "type": "mcq",
        "questionHtml": "Berdasarkan standar RFC 1918, alamat IP yang dialokasikan khusus untuk jaringan privat (LAN lokal) dan tidak boleh diroutingkan langsung di jaringan publik internet global adalah...",
        "options": [
            {"key": "A", "text": "10.0.0.0/8, 172.16.0.0/12, dan 192.168.0.0/16."},
            {"key": "B", "text": "11.0.0.0/8, 172.32.0.0/12, dan 192.169.0.0/16."},
            {"key": "C", "text": "127.0.0.0/8, 169.254.0.0/16, dan 224.0.0.0/4."},
            {"key": "D", "text": "8.8.8.8/32, 1.1.1.1/32, dan 208.67.222.222/32."},
            {"key": "E", "text": "100.64.0.0/10, 192.0.2.0/24, dan 198.51.100.0/24."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "RENTANG IP PRIVATE RFC 1918",
            "latex": "\\begin{cases} \\text{Kelas A:} & 10.0.0.0 - 10.255.255.255 \\; (/8) \\\\ \\text{Kelas B:} & 172.16.0.0 - 172.31.255.255 \\; (/12) \\\\ \\text{Kelas C:} & 192.168.0.0 - 192.168.255.255 \\; (/16) \\end{cases}",
            "legend": "• RFC 1918: Alamat non-routable di Internet publik<br>• Butuh NAT (Network Address Translation) untuk ke internet"
        },
        "hints": {
            "concept": "Tiga blok IP privat standar yang selalu dijumpai di jaringan lokal sekolah, rumah, dan kantor adalah prefiks 10.x.x.x, 172.16-31.x.x, dan 192.168.x.x.",
            "execution": "Pilihan A tepat menyebutkan ketiga rentang CIDR resmi RFC 1918."
        },
        "explanation": "RFC 1918 menetapkan 3 blok alamat IPv4 privat: Kelas A (10.0.0.0/8), Kelas B (172.16.0.0/12 yang mencakup 172.16.0.0 hingga 172.31.255.255), dan Kelas C (192.168.0.0/16 yang mencakup 192.168.0.0 hingga 192.168.255.255). Alamat-alamat ini bebas digunakan dalam jaringan lokal tanpa perlu registrasi ke IANA/APNIC, namun membutuhkan NAT agar perangkat di dalamnya dapat bertukar data dengan internet.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-07",
        "subject": "tkj",
        "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Standar Urutan Warna Kabel UTP T568B",
        "type": "mcq",
        "questionHtml": "Pada pembuatan kabel jaringan UTP tipe Straight-Through menggunakan standar T568B, urutan pin 1 hingga pin 8 dari kiri ke kanan saat konektor RJ-45 diposisikan menghadap ke atas dengan klip pengunci di bagian bawah adalah...",
        "options": [
            {"key": "A", "text": "Putih-Oranye, Oranye, Putih-Hijau, Biru, Putih-Biru, Hijau, Putih-Cokelat, Cokelat."},
            {"key": "B", "text": "Putih-Hijau, Hijau, Putih-Oranye, Biru, Putih-Biru, Oranye, Putih-Cokelat, Cokelat."},
            {"key": "C", "text": "Putih-Oranye, Putih-Hijau, Oranye, Biru, Putih-Biru, Hijau, Putih-Cokelat, Cokelat."},
            {"key": "D", "text": "Oranye, Putih-Oranye, Hijau, Putih-Hijau, Biru, Putih-Biru, Cokelat, Putih-Cokelat."},
            {"key": "E", "text": "Putih-Biru, Biru, Putih-Oranye, Oranye, Putih-Hijau, Hijau, Putih-Cokelat, Cokelat."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "URUTAN WARNA STANDAR T568B",
            "latex": "\\text{Pin: } 1(\\text{PO}) - 2(\\text{O}) - 3(\\text{PH}) - 4(\\text{B}) - 5(\\text{PB}) - 6(\\text{H}) - 7(\\text{PC}) - 8(\\text{C})",
            "legend": "• PO: Putih-Oranye | O: Oranye<br>• PH: Putih-Hijau | B: Biru | PB: Putih-Biru | H: Hijau<br>• PC: Putih-Cokelat | C: Cokelat"
        },
        "hints": {
            "concept": "T568B diawali dengan pasangan warna Oranye. Ingat posisi pin 3 dan 6 yang membelah pasangan Biru (pin 3 Putih-Hijau, pin 6 Hijau).",
            "execution": "Urutan T568B: Putih-Oranye, Oranye, Putih-Hijau, Biru, Putih-Biru, Hijau, Putih-Cokelat, Cokelat."
        },
        "explanation": "Standar terminasi kabel TIA/EIA T568B memiliki urutan pin: 1: Putih-Oranye, 2: Oranye, 3: Putih-Hijau, 4: Biru, 5: Putih-Biru, 6: Hijau, 7: Putih-Cokelat, 8: Cokelat. Pada standar Fast Ethernet 100BASE-TX, pin 1 dan 2 berfungsi sebagai pengirim sinyal (Transmit / Tx), sedangkan pin 3 dan 6 berfungsi sebagai penerima sinyal (Receive / Rx).",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-08",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Fungsi Default Gateway pada Host",
        "type": "mcq",
        "questionHtml": "Di sebuah workstation kantor dengan IP `192.168.1.15/24`, pengguna tidak dapat membuka website internet meskipun koneksi fisik kabel menyala dan dapat melakukan ping ke sesama rekan kantor di `192.168.1.20`. Penyebab paling logis pada pengaturan TCP/IP adalah...",
        "options": [
            {"key": "A", "text": "Alamat Default Gateway belum diisi atau salah mengarah ke IP di luar subnet 192.168.1.0/24."},
            {"key": "B", "text": "Subnet mask komputer diset menjadi 255.255.255.0 sehingga memblokir port HTTP."},
            {"key": "C", "text": "Kabel UTP terpasang longgar sehingga hanya mendukung paket data transmisi broadcast lokal."},
            {"key": "D", "text": "Kartu jaringan (NIC) mengalami kerusakan duplex sehingga hanya bisa mode Half-Duplex."},
            {"key": "E", "text": "Workstation mengalami collision domain karena switch menggunakan kabel Cat 5e."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "PRINSIP ROUTING LOGIKAL GATEWAY",
            "latex": "\\text{Jika } \\text{IP}_{\\text{dest}} \\notin \\text{Subnet}_{\\text{local}} \\implies \\text{Forward to Default Gateway}",
            "legend": "• Subnet lokal: 192.168.1.0/24 (Dapat komunikasi via ARP langsung)<br>• Subnet publik/internet: Membutuhkan IP router lokal sebagai Default Gateway"
        },
        "hints": {
            "concept": "Komunikasi ke sesama subnet lokal berhasil berarti Layer 1 dan Layer 2 aman. Kegagalan ke internet (luar subnet) menunjuk pada ketiadaan pintu keluar (Gateway).",
            "execution": "Default Gateway adalah pintu keluar paket menuju jaringan lain. Tanpa default gateway yang valid, host tidak tahu ke mana harus meneruskan paket di luar subnet lokalnya."
        },
        "explanation": "Ketika sebuah host hendak mengirim paket ke alamat IP yang berada di luar subnet lokalnya (misal ke IP web server di internet), host akan memeriksa routing table lokal dan meneruskan paket tersebut ke alamat Default Gateway (antarmuka router lokal). Jika Default Gateway kosong atau salah, komunikasi intra-LAN tetap lancar tetapi komunikasi inter-network atau ke internet akan gagal total.",
        "isDiagnostic": True
    },
    {
        "id": "tkj-lat-e-09",
        "subject": "tkj",
        "materi": "LAYANAN JARINGAN & SERVER",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Fungsi DNS Server dan Tipe Record",
        "type": "mcq",
        "questionHtml": "Saat seorang teknisi mengonfigurasi Domain Name System (DNS) pada server Linux BIND9 untuk memetakan nama domain `smkhebat.sch.id` ke alamat IPv4 `103.25.10.5`, tipe DNS Resource Record yang harus ditambahkan pada file forward zone adalah...",
        "options": [
            {"key": "A", "text": "Record 'A' (Address Record untuk pemetaan FQDN ke IPv4 32-bit)."},
            {"key": "B", "text": "Record 'AAAA' (Quad-A Record untuk pemetaan FQDN ke IPv6 128-bit)."},
            {"key": "C", "text": "Record 'PTR' (Pointer Record untuk resolusi pemetaan balik IP ke Domain)."},
            {"key": "D", "text": "Record 'CNAME' (Canonical Name untuk membuat nama alias dari domain lain)."},
            {"key": "E", "text": "Record 'MX' (Mail Exchange Record untuk mengarahkan pengiriman email server)."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "FORMAT DNS RESOURCE RECORD",
            "latex": "\\texttt{smkhebat.sch.id.}\\quad \\texttt{IN}\\quad \\texttt{A}\\quad \\texttt{103.25.10.5}",
            "legend": "• A Record: Nama Domain -> IPv4<br>• AAAA Record: Nama Domain -> IPv6<br>• CNAME: Nama Domain Alias -> Nama Domain Asli<br>• MX: Mail Server Target"
        },
        "hints": {
            "concept": "Ingat jenis record: A untuk alamat IPv4 biasa, AAAA untuk IPv6, MX untuk mail, PTR untuk reverse lookup.",
            "execution": "Pemetaan domain ke IPv4 menggunakan Record 'A' (Address)."
        },
        "explanation": "DNS Record tipe 'A' (Address Mapping record) digunakan untuk menerjemahkan nama host atau Fully Qualified Domain Name (FQDN) menjadi alamat IPv4 32-bit. Sedangkan Record 'AAAA' digunakan untuk alamat IPv6 128-bit, 'CNAME' untuk alias nama lain, 'MX' untuk penunjuk mail exchanger, dan 'PTR' untuk reverse lookup dari IP kembali ke nama domain.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-10",
        "subject": "tkj",
        "materi": "ALAT UKUR & PERANGKAT KERJA FIBER OPTIK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Fungsi Optical Power Meter (OPM) dan Visual Fault Locator (VFL)",
        "type": "mcq",
        "questionHtml": "Alat ukur fiber optik portabel yang memancarkan laser sinar merah tampak berpanjang gelombang 650 nm untuk mendeteksi secara visual titik kabel yang putus, tertekuk tajam, atau konektor yang retak disebut...",
        "options": [
            {"key": "A", "text": "Visual Fault Locator (VFL / Laser Pen Fiber Optic)."},
            {"key": "B", "text": "Optical Power Meter (OPM pengukur daya sinyal dBm)."},
            {"key": "C", "text": "Optical Time-Domain Reflectometer (OTDR pemeta grafik loss)."},
            {"key": "D", "text": "Fiber Fusion Splicer (Mesin penyambung leburan kaca inti)."},
            {"key": "E", "text": "Fiber Cleaver (Alat pemotong sudut presisi ujung core kaca)."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "ALAT KERJA DASAR FIBER OPTIK",
            "latex": "\\text{VFL (Laser Merah } 650\\,\\text{nm)} \\implies \\text{Visual Leakage Test pada Core Fiber}",
            "legend": "• VFL: Melacak kontinuitas kabel dan kebocoran cahaya akibat bending/crack<br>• OPM: Mengukur daya redaman absolut (dBm) dan relatif (dB)"
        },
        "hints": {
            "concept": "Kata kunci: 'memancarkan laser sinar merah tampak untuk mendeteksi secara kasat mata (visual)'.",
            "execution": "Visual Fault Locator (VFL) menggunakan laser merah kasat mata. OPM mengukur angka daya, OTDR menganalisis jarak dan event refleksi."
        },
        "explanation": "Visual Fault Locator (VFL), sering disebut senter atau pena laser fiber optik, memancarkan sinar laser merah tampak dengan panjang gelombang 650 nm. Jika ada serat kaca yang patah di dalam jaket kabel atau sambungan patch cord yang bocor, cahaya merah tersebut akan berpendar keluar menembus selubung kabel, sehingga titik kerusakan dapat ditemukan secara visual dengan cepat.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-11",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Konsep Virtual LAN (VLAN) 802.1Q",
        "type": "mcq",
        "questionHtml": "Manfaat utama penerapan Virtual Local Area Network (VLAN) berbasis standar IEEE 802.1Q pada switch manageable di lingkungan sekolah atau perkantoran adalah...",
        "options": [
            {"key": "A", "text": "Memecah satu broadcast domain besar menjadi beberapa broadcast domain kecil secara logikal demi efisiensi dan keamanan."},
            {"key": "B", "text": "Meningkatkan daya listrik PoE yang dihantarkan ke perangkat Access Point di plafon."},
            {"key": "C", "text": "Menggantikan peran kabel serat optik dengan kabel tembaga berkecepatan 100 Gbps."},
            {"key": "D", "text": "Menghilangkan kebutuhan konfigurasi IP Address pada setiap workstation di jaringan."},
            {"key": "E", "text": "Mengubah switch unmanaged menjadi router BGP kelas backbone antar negara."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "SEGMENTASI VLAN PADA SWITCH",
            "latex": "1\\text{ Switch Fisik} \\xrightarrow{\\text{IEEE 802.1Q}} N\\text{ Broadcast Domain Terisolasi}",
            "legend": "• Default: 1 Switch = 1 Broadcast Domain besar (Rawan broadcast storm)<br>• VLAN: Membagi port secara logis (VLAN 10 Guru, VLAN 20 Siswa)"
        },
        "hints": {
            "concept": "Switch membagi collision domain pada setiap portnya, namun secara default seluruh port switch berada dalam satu broadcast domain yang sama. VLAN memecah broadcast domain tersebut.",
            "execution": "VLAN mengisolasi broadcast traffic dan meningkatkan keamanan antar departemen/ruang kelas secara logis."
        },
        "explanation": "Secara default, seluruh port pada switch berada dalam satu broadcast domain yang sama. Jika ada paket broadcast (misalnya ARP request), seluruh komputer akan menerima paket tersebut sehingga menghabiskan bandwidth dan membuka celah keamanan. Dengan VLAN (IEEE 802.1Q), switch dapat membagi port-portnya menjadi kelompok logis terpisah (berbeda broadcast domain) sehingga lalu lintas data terisolasi rapi.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-12",
        "subject": "tkj",
        "materi": "KEAMANAN JARINGAN & FIREWALL",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Perbedaan Port Standar TCP Layanan Internet",
        "type": "mcq",
        "questionHtml": "Seorang administrator jaringan ingin membuka port firewall agar pengguna dapat mengakses website sekolah dengan enkripsi TLS/SSL yang aman. Port default protokol HTTPS yang harus diizinkan pada firewall adalah...",
        "options": [
            {"key": "A", "text": "Port TCP 443."},
            {"key": "B", "text": "Port TCP 80."},
            {"key": "C", "text": "Port TCP 21."},
            {"key": "D", "text": "Port TCP 22."},
            {"key": "E", "text": "Port UDP 53."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "WELL-KNOWN PORTS STANDAR IANA",
            "latex": "\\text{HTTPS} = \\text{TCP } 443, \\quad \\text{HTTP} = \\text{TCP } 80, \\quad \\text{SSH} = \\text{TCP } 22, \\quad \\text{DNS} = 53",
            "legend": "• Range Well-Known Ports: 0 s/d 1023<br>• Port 443: HTTP over TLS/SSL (Aman/Terenkripsi)"
        },
        "hints": {
            "concept": "Ingat: HTTP biasa adalah port 80, sedangkan HTTPS yang terenkripsi gembok aman adalah port 443.",
            "execution": "Port TCP 443 adalah port standar untuk HTTPS."
        },
        "explanation": "Internet Assigned Numbers Authority (IANA) menetapkan port standar untuk layanan jaringan: HTTP menggunakan TCP port 80 (tidak terenkripsi), HTTPS menggunakan TCP port 443 (terenkripsi SSL/TLS), SSH menggunakan TCP port 22, FTP menggunakan TCP port 20/21, dan DNS menggunakan UDP/TCP port 53. Membuka port 443 memungkinkan pertukaran data web yang terenkripsi.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-13",
        "subject": "tkj",
        "materi": "PENGALAMATAN IPV4 & SUBNETTING",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Penentuan Network ID dan Broadcast ID",
        "type": "mcq",
        "questionHtml": "Diberikan alamat IP sebuah komputer klien `192.168.10.75` dengan subnet mask `255.255.255.192` (/26). Alamat Network ID dan Broadcast ID dari subnet tempat komputer tersebut berada adalah...",
        "options": [
            {"key": "A", "text": "Network ID: 192.168.10.64 dan Broadcast ID: 192.168.10.127."},
            {"key": "B", "text": "Network ID: 192.168.10.0 dan Broadcast ID: 192.168.10.63."},
            {"key": "C", "text": "Network ID: 192.168.10.64 dan Broadcast ID: 192.168.10.128."},
            {"key": "D", "text": "Network ID: 192.168.10.32 dan Broadcast ID: 192.168.10.95."},
            {"key": "E", "text": "Network ID: 192.168.10.0 dan Broadcast ID: 192.168.10.255."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "RUMUS INTERVAL BLOK SUBNET",
            "latex": "\\text{Interval Blok} = 256 - \\text{Octet Terakhir Subnet} = 256 - 192 = 64",
            "legend": "• Subnet 1: 192.168.10.0 s/d .63<br>• Subnet 2: 192.168.10.64 s/d .127 (IP 75 berada di sini)<br>• Subnet 3: 192.168.10.128 s/d .191"
        },
        "hints": {
            "concept": "Subnet mask 255.255.255.192 (/26) memiliki interval blok 256 - 192 = 64. Buat daftar rentang blok kelipatan 64.",
            "execution": "Blok 1: 0 - 63. Blok 2: 64 - 127. Karena 75 berada di antara 64 dan 127, maka Network ID = 192.168.10.64 dan Broadcast ID = 192.168.10.127."
        },
        "explanation": "Nilai octet terakhir subnet mask adalah 192. Nilai loncatan (interval blok) dihitung dengan 256 - 192 = 64. Subnet yang terbentuk pada octet ke-4 adalah: Subnet 1 (0 s/d 63), Subnet 2 (64 s/d 127), Subnet 3 (128 s/d 191), dan Subnet 4 (192 s/d 255). IP 192.168.10.75 berada di Subnet 2, sehingga Network ID adalah 192.168.10.64, usable IP adalah 192.168.10.65 - 192.168.10.126, dan Broadcast ID adalah 192.168.10.127.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-14",
        "subject": "tkj",
        "materi": "JARINGAN NIRKABEL & WIRELESS",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Perbandingan Frekuensi Wi-Fi 2.4 GHz vs 5 GHz",
        "type": "mcq",
        "questionHtml": "Dalam perencanaan instalasi Access Point (AP) di lorong gedung sekolah, teknisi menganalisis karakteristik frekuensi radio. Keunggulan utama frekuensi 2.4 GHz dibandingkan frekuensi 5 GHz adalah...",
        "options": [
            {"key": "A", "text": "Jangkauan sinyal lebih jauh dan kemampuan menembus dinding padat lebih baik karena panjang gelombangnya lebih besar."},
            {"key": "B", "text": "Menyediakan jumlah non-overlapping channel yang jauh lebih banyak hingga 24 channel mandiri."},
            {"key": "C", "text": "Kecepatan transfer data (throughput) maksimumnya jauh melampaui frekuensi 5 GHz pada jarak dekat."},
            {"key": "D", "text": "Bebas dari gangguan interferensi gelombang elektromagnetik perangkat Bluetooth dan microwave oven."},
            {"key": "E", "text": "Mendukung bandwidth channel 160 MHz untuk transmisi ultra-broadband nirkabel."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "HUBUNGAN FREKUENSI DAN PANJANG GELOMBANG",
            "latex": "\\lambda = \\frac{c}{f} \\implies f \\uparrow \\iff \\lambda \\downarrow \\iff \\text{Penetrasi Objek Solid} \\downarrow",
            "legend": "• 2.4 GHz: Panjang gelombang ~12.5 cm -> Penetrasi lebih baik, jangkauan luas<br>• 5 GHz: Panjang gelombang ~6 cm -> Throughput tinggi, teredam dinding"
        },
        "hints": {
            "concept": "Hukum fisika perambatan gelombang radio: frekuensi lebih rendah memiliki panjang gelombang lebih besar sehingga redamannya lebih kecil saat menembus partisi dinding.",
            "execution": "2.4 GHz memiliki jangkauan lebih luas dan penetrasi dinding lebih kuat dibanding 5 GHz, meskipun 2.4 GHz lebih lambat dan kanal non-overlap hanya ada 3 (1, 6, 11)."
        },
        "explanation": "Frekuensi radio 2.4 GHz memiliki panjang gelombang yang lebih panjang (sekitar 12.5 cm) dibandingkan 5 GHz (sekitar 6 cm). Gelombang elektromagnetik yang lebih panjang mengalami redaman (attenuation) yang lebih kecil saat menembus objek padat seperti tembok bata atau kayu, sehingga sinyal 2.4 GHz mampu menjangkau area yang lebih luas dan menembus rintangan lebih baik dibanding 5 GHz.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-15",
        "subject": "tkj",
        "materi": "K3LH & KETENAGAKERJAAN TJKT",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Keselamatan Kerja Penyambungan Fiber Optik",
        "type": "mcq",
        "questionHtml": "Saat teknisi melakukan proses penyiapan dan pemotongan kabel fiber optik menggunakan stripper dan cleaver, sisa serpihan potongan serat kaca (fiber core) harus diperlakukan secara hati-hati dengan prosedur K3LH yang tepat, yaitu...",
        "options": [
            {"key": "A", "text": "Dibersihkan dengan selotip/alat khusus dan dimasukkan ke dalam wadah tertutup rapat berlabel limbah tajam berbahaya."},
            {"key": "B", "text": "Ditiup dengan kuat menggunakan kompresor angin bertekanan tinggi ke arah lantai ruang kerja."},
            {"key": "C", "text": "Diusap langsung menggunakan telapak tangan telanjang untuk memastikan meja kerja sudah bersih licin."},
            {"key": "D", "text": "Dibuang langsung ke tempat sampah kertas biasa di bawah meja kerja teknisi."},
            {"key": "E", "text": "Dilarutkan dengan cairan alkohol 70% agar serpihan kaca meleleh secara kimiawi."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "STANDAR K3LH PENANGANAN FIBER OPTIK",
            "latex": "\\text{Diameter Serat Core} = 125\\,\\mu\\text{m (Cladding)} \\implies \\text{Dapat Menembus Pembuluh Darah Kulit}",
            "legend": "• Bahaya: Serat kaca mikroskopis tidak dapat dideteksi X-ray jika masuk kulit/mata<br>• Solusi: Wadah khusus sharps disposal container bertutup"
        },
        "hints": {
            "concept": "Pecahan kaca serat optik berdiameter sehelai rambut manusia, tajam, dan tidak terlihat. Jika menusuk kulit atau terhirup, sangat berbahaya bagi kesehatan.",
            "execution": "Sisa potongan harus diambil dengan lakban/selotip dan dibuang ke wadah tertutup khusus limbah tajam (sharps disposal container)."
        },
        "explanation": "Serat optik terbuat dari silika kaca murni dengan diameter luar (cladding) hanya 125 mikrometer. Pecahan serat kaca ini sangat tajam dan transparan. Jika serpihan tertusuk ke dalam kulit atau masuk ke aliran darah dan mata, serpihan tersebut tidak dapat terurai dan sulit dideteksi bahkan dengan sinar X. Standar K3LH mewajibkan pengumpulan serpihan kaca dengan selotip atau pinset ke dalam wadah limbah tertutup rapat (sharps container).",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-16",
        "subject": "tkj",
        "materi": "LAYANAN JARINGAN & SERVER",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Protokol Pengalamatan Otomatis Statis vs Dinamis",
        "type": "mcq",
        "questionHtml": "Sebuah komputer Windows tidak dapat memperoleh IP Address dari DHCP Server karena kabel LAN belum tertancap ke switch. Windows kemudian secara otomatis menetapkan alamat IP berawalan `169.254.X.X`. Mekanisme pengalamatan otomatis bawaan sistem operasi ini disebut...",
        "options": [
            {"key": "A", "text": "APIPA (Automatic Private IP Addressing / Link-Local IPv4)."},
            {"key": "B", "text": "SLAAC (Stateless Address Autoconfiguration IPv6)."},
            {"key": "C", "text": "Static Manual Configuration melalui registry Windows."},
            {"key": "D", "text": "DNS Dynamic Update Client Registration."},
            {"key": "E", "text": "DHCP Relay Discovery Fallback Agent."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "RENTANG BLOK IP APIPA (RFC 3927)",
            "latex": "\\text{APIPA} = 169.254.0.1 \\text{ s/d } 169.254.255.254 \\quad (/16)",
            "legend": "• Subnet Mask: 255.255.0.0<br>• Digunakan saat klien diset DHCP namun tidak ada respon DHCP server"
        },
        "hints": {
            "concept": "Rentang 169.254.0.0/16 adalah alamat Link-Local IPv4 yang diberikan Windows ketika DHCP gagal.",
            "execution": "Fitur ini dinamakan APIPA (Automatic Private IP Addressing)."
        },
        "explanation": "Automatic Private IP Addressing (APIPA) adalah fitur pada sistem operasi modern yang secara otomatis menetapkan alamat IPv4 link-local dalam rentang 169.254.0.1 hingga 169.254.255.254 dengan subnet mask 255.255.0.0 ketika komputer diatur untuk menerima IP dari DHCP tetapi tidak mendapat respons dalam batas waktu tertentu. Klien dengan IP APIPA hanya dapat berkomunikasi dengan sesama host di link lokal yang sama, tetapi tidak dapat mengakses gateway atau internet.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-17",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Tipe Port Switch: Access Port vs Trunk Port",
        "type": "mcq",
        "questionHtml": "Dalam topologi jaringan berbasis VLAN, antarmuka port switch yang menghubungkan switch satu dengan switch lainnya atau switch dengan router untuk membawa lalu lintas beberapa VLAN sekaligus dengan tag 802.1Q disebut...",
        "options": [
            {"key": "A", "text": "Trunk Port (Tagging port pembawa banyak VLAN)."},
            {"key": "B", "text": "Access Port (Untagged port khusus satu VLAN untuk end-device)."},
            {"key": "C", "text": "Console Port (Port serial khusus konfigurasi terminal lokal)."},
            {"key": "D", "text": "Mirror Port (Port pengganda paket untuk packet analyzer)."},
            {"key": "E", "text": "Auxiliary Port (Port modem cadangan koneksi out-of-band)."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "PERBEDAAN ACCESS VS TRUNK PORT",
            "latex": "\\begin{cases} \\text{Access Port:} & \\text{Membawa 1 VLAN (Untagged frame ke PC)} \\\\ \\text{Trunk Port:} & \\text{Membawa } N\\text{ VLAN (Menyisipkan 4-byte 802.1Q Header)} \\end{cases}",
            "legend": "• Trunk: Switch-ke-Switch atau Switch-ke-Router (Router-on-a-Stick)<br>• Access: Switch-ke-PC/Printer"
        },
        "hints": {
            "concept": "Port yang menuju PC pengguna biasa disebut Access Port. Port yang membawa banyak VLAN antar perangkat interkoneksi disebut Trunk Port.",
            "execution": "Trunk Port menyisipkan tag VLAN ID 802.1Q agar switch penerima mengetahui paket tersebut milik VLAN mana."
        },
        "explanation": "Pada konfigurasi VLAN, terdapat dua mode utama port switch: (1) Access Port: hanya menjadi anggota dari 1 VLAN tunggal dan mengirimkan frame standar tanpa tag (untagged) langsung ke perangkat pengguna seperti PC atau printer; (2) Trunk Port: dirancang untuk menghubungkan antar switch atau switch ke router, mampu melewatkan lalu lintas dari banyak VLAN sekaligus dengan menambahkan 4-byte tag 802.1Q (VLAN ID) pada setiap frame.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-18",
        "subject": "tkj",
        "materi": "PERINTAH DIAGNOSTIK JARINGAN",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Utilitas Ping dan Protokol ICMP",
        "type": "mcq",
        "questionHtml": "Perintah utilitas baris perintah (CLI) `ping` yang sering digunakan teknisi untuk menguji konektivitas dasar ujung-ke-ujung (end-to-end) bekerja dengan memanfaatkan protokol pada Network Layer, yaitu...",
        "options": [
            {"key": "A", "text": "ICMP (Internet Control Message Protocol, paket Echo Request & Echo Reply)."},
            {"key": "B", "text": "IGMP (Internet Group Management Protocol untuk multicast IPTV)."},
            {"key": "C", "text": "SNMP (Simple Network Management Protocol untuk monitoring CPU router)."},
            {"key": "D", "text": "SMTP (Simple Mail Transfer Protocol untuk pengiriman pesan elektronik)."},
            {"key": "E", "text": "ARP (Address Resolution Protocol untuk memetakan IP ke MAC)."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "TIPE PESAN ICMP PADA PING",
            "latex": "\\text{Echo Request (Type 8, Code 0)} \\xrightarrow{\\text{Ping}} \\text{Echo Reply (Type 0, Code 0)}",
            "legend": "• ICMP beroperasi di Network Layer (Layer 3)<br>• Digunakan untuk diagnosis konektivitas, latency, dan packet loss"
        },
        "hints": {
            "concept": "Utilitas ping mengirimkan pesan 'Echo Request' dan menunggu 'Echo Reply' yang merupakan bagian dari protokol ICMP.",
            "execution": "ICMP (Internet Control Message Protocol) adalah protokol pembawa pesan kendali dan diagnostik jaringan."
        },
        "explanation": "Perintah ping menggunakan protokol ICMP (Internet Control Message Protocol) yang berjalan di atas layer IP (Network Layer). Pengirim mengeksekusi ICMP Type 8 (Echo Request) ke alamat target, dan jika target aktif serta tidak memblokir firewall ICMP, target akan merespons dengan ICMP Type 0 (Echo Reply). Dari respons tersebut dapat dianalisis latensi bolak-balik (Round-Trip Time / RTT) dan persentase packet loss.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-19",
        "subject": "tkj",
        "materi": "ROUTING & SWITCHING ENTERPRISE",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Fungsi Protokol ARP (Address Resolution Protocol)",
        "type": "mcq",
        "questionHtml": "Dalam jaringan LAN lokal berbasis Ethernet, sebuah workstation mengetahui alamat IP tujuan rekan satu subnet namun belum mengetahui alamat fisik MAC Address tujuannya. Protokol yang bertugas menemukan MAC Address berdasarkan IP tujuan tersebut adalah...",
        "options": [
            {"key": "A", "text": "ARP (Address Resolution Protocol melalui paket broadcast ARP Request)."},
            {"key": "B", "text": "RARP (Reverse Address Resolution Protocol melalui multicast)."},
            {"key": "C", "text": "DHCP (Dynamic Host Configuration Protocol melalui unicast)."},
            {"key": "D", "text": "DNS (Domain Name System melalui query rekursif UDP)."},
            {"key": "E", "text": "NAT (Network Address Translation melalui translasi port)."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME KERJA PROTOKOL ARP",
            "latex": "\\text{Host A} \\xrightarrow{\\text{ARP Request (Broadcast)}} \\text{Semua PC} \\implies \\text{Host Target} \\xrightarrow{\\text{ARP Reply (Unicast)}} \\text{Host A}",
            "legend": "• Input: Alamat IP tujuan yang diketahui<br>• Output: MAC Address fisik dari pemilik IP tersebut<br>• Disimpan pada: ARP Cache Table"
        },
        "hints": {
            "concept": "Pemetaan dari IP (Layer 3) ke MAC Address (Layer 2) adalah tugas Address Resolution Protocol (ARP).",
            "execution": "ARP membroadcast pertanyaan 'Siapa pemilik IP ini? Beritahu MAC address-mu ke saya'."
        },
        "explanation": "Sebelum frame Ethernet dapat dikirimkan melalui media fisik, komputer pengirim harus menyisipkan MAC Address tujuan pada header frame layer 2. Jika pengirim hanya mengetahui alamat IP tujuan, pengirim akan menjalankan protokol ARP (Address Resolution Protocol) dengan mengirimkan paket ARP Request secara broadcast (FF:FF:FF:FF:FF:FF). Komputer yang memiliki IP tersebut akan membalas dengan ARP Reply unicast yang berisi MAC Address fisiknya.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-20",
        "subject": "tkj",
        "materi": "KEAMANAN JARINGAN & FIREWALL",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Fungsi NAT (Network Address Translation) Masquerade",
        "type": "mcq",
        "questionHtml": "Pada router gateway MikroTik kantor, administrator mengonfigurasi aturan firewall NAT dengan aksi `masquerade` pada antarmuka publik yang mengarah ke ISP. Fungsi utama dari aksi masquerade tersebut adalah...",
        "options": [
            {"key": "A", "text": "Mengubah alamat IP privat klien LAN menjadi IP publik dinamis router saat paket keluar menuju internet."},
            {"key": "B", "text": "Mengenkripsi seluruh isi payload paket data dengan algoritma RSA 4096-bit."},
            {"key": "C", "text": "Membatasi kecepatan download dan upload setiap klien menjadi tepat 512 Kbps."},
            {"key": "D", "text": "Memblokir secara permanen seluruh serangan virus trojan yang masuk melalui port HTTP."},
            {"key": "E", "text": "Menduplikasi paket data klien ke server cadangan untuk keperluan audit forensik."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "PRINSIP NAT MASQUERADE (SRC-NAT)",
            "latex": "\\text{IP Private:Port} \\xrightarrow{\\text{Router Masquerade}} \\text{IP Publik Router:Port Baru} \\implies \\text{Internet}",
            "legend": "• Src-NAT: Mengubah alamat IP asal paket saat keluar dari router<br>• Masquerade: Menggunakan IP dinamis antarmuka keluar secara otomatis"
        },
        "hints": {
            "concept": "IP privat RFC 1918 tidak bisa beredar di internet publik. Router perlu 'menyamarkan' IP privat tersebut menjadi IP publik milik router itu sendiri.",
            "execution": "Masquerade adalah varian Source NAT yang secara otomatis mengambil IP publik yang terpasang pada interface out router."
        },
        "explanation": "Karena IP privat (RFC 1918) tidak dapat diroutingkan di internet publik, router harus melakukan Source Network Address Translation (Src-NAT). Aksi 'masquerade' pada MikroTik adalah bentuk khusus dari Src-NAT yang mengganti alamat IP privat pengirim dengan alamat IP yang sedang aktif pada interface keluar (out-interface) router secara dinamis, sehingga ratusan komputer di LAN dapat berbagi satu koneksi IP publik internet.",
        "isDiagnostic": True
    },
    {
        "id": "tkj-lat-e-21",
        "subject": "tkj",
        "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Fungsi Konektor Fiber Optik Tipe SC, LC, FC",
        "type": "mcq",
        "questionHtml": "Konektor kabel patch cord fiber optik berukuran kecil dengan sistem pengunci kait dorong-tarik (push-pull latching) yang sangat umum digunakan pada modul SFP (Small Form-factor Pluggable) di switch manageable berkerapatan tinggi adalah...",
        "options": [
            {"key": "A", "text": "Konektor LC (Lucent Connector berkuran kecil 1.25 mm ferrule)."},
            {"key": "B", "text": "Konektor FC (Ferrule Connector dengan sistem ulir putar baut metal)."},
            {"key": "C", "text": "Konektor ST (Straight Tip dengan sistem bayonet putar putus)."},
            {"key": "D", "text": "Konektor BNC (Bayonet Neill-Concelman untuk kabel koaksial analog)."},
            {"key": "E", "text": "Konektor RJ-11 (Registered Jack 4-pin untuk jaringan telepon kabel)."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "TIPE KONEKTOR FIBER OPTIK POPULER",
            "latex": "\\text{LC (Small Form Factor } 1.25\\,\\text{mm)} \\quad \\text{vs} \\quad \\text{SC (Standard Subscriber } 2.5\\,\\text{mm)}",
            "legend": "• LC: Digunakan pada transceiver SFP/SFP+ switch modern<br>• SC: Berbentuk kotak persegi (banyak digunakan pada ONT/converter media)<br>• FC: Ulir metal (peralatan lab/telekomunikasi presisi)"
        },
        "hints": {
            "concept": "Konektor pada modul SFP switch harus berukuran kecil (Small Form Factor) agar dapat dipasang berdampingan dalam jumlah puluhan port.",
            "execution": "Konektor LC (Lucent Connector) memiliki ferrule 1.25 mm, setengah dari ukuran ferrule SC/FC yang 2.5 mm."
        },
        "explanation": "Konektor LC (Lucent Connector) dikembangkan sebagai konektor Small Form Factor (SFF) dengan ferrule keramik berdiameter 1.25 mm (setengah dari konektor SC/FC/ST yang berdiameter 2.5 mm). Desain kompak dengan mekanisme klip pengunci mirip RJ-45 ini menjadikannya standar utama pada port transceiver optik SFP/SFP+ pada switch enterprise modern.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-22",
        "subject": "tkj",
        "materi": "JARINGAN NIRKABEL & WIRELESS",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Kanal Non-Overlapping Wi-Fi 2.4 GHz",
        "type": "mcq",
        "questionHtml": "Pada pita frekuensi Wi-Fi 2.4 GHz standar 802.11b/g/n dengan lebar kanal (channel bandwidth) 20 MHz, tiga nomor kanal independen yang tidak saling tumpang tindih (non-overlapping) yang wajib digunakan untuk menghindari co-channel interference adalah...",
        "options": [
            {"key": "A", "text": "Kanal 1, Kanal 6, dan Kanal 11."},
            {"key": "B", "text": "Kanal 1, Kanal 2, dan Kanal 3."},
            {"key": "C", "text": "Kanal 2, Kanal 7, dan Kanal 12."},
            {"key": "D", "text": "Kanal 3, Kanal 6, dan Kanal 9."},
            {"key": "E", "text": "Kanal 4, Kanal 8, dan Kanal 12."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "JARAK KANAL WI-FI 2.4 GHZ",
            "latex": "\\Delta f_{\\text{channel}} = 5\\,\\text{MHz}, \\quad B_{\\text{channel}} = 20\\,\\text{MHz} \\implies \\text{Jarak Aman} \\ge 25\\,\\text{MHz}",
            "legend": "• Ch 1: 2412 MHz | Ch 6: 2437 MHz | Ch 11: 2462 MHz<br>• Selisih Ch 1 ke Ch 6 = 25 MHz (Aman dari interferensi sinyal)"
        },
        "hints": {
            "concept": "Pita 2.4 GHz hanya memiliki 3 kanal yang benar-benar bersih tanpa saling bertubrukan jika menggunakan lebar 20 MHz.",
            "execution": "Tiga kanal standar non-overlapping universal adalah 1, 6, dan 11."
        },
        "explanation": "Pada pita 2.4 GHz, jarak antara pusat kanal yang berdekatan hanya 5 MHz, padahal satu sinyal Wi-Fi membutuhkan lebar pita 20 MHz (atau 22 MHz pada 802.11b). Akibatnya, kanal-kanal yang berdekatan akan saling bertumpukan sinyalnya. Hanya kanal 1 (2412 MHz), kanal 6 (2437 MHz), dan kanal 11 (2462 MHz) yang memiliki jarak 25 MHz sehingga tidak saling tumpang tindih sama sekali.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-23",
        "subject": "tkj",
        "materi": "LAYANAN JARINGAN & SERVER",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Protokol Remote Management SSH vs Telnet",
        "type": "mcq",
        "questionHtml": "Dalam administrasi perangkat switch dan router dari jarak jauh, administrator jaringan diwajibkan menggunakan protokol SSH (Secure Shell) dan melarang penggunaan Telnet. Kelemahan fatal dari protokol Telnet adalah...",
        "options": [
            {"key": "A", "text": "Mengirimkan seluruh teks termasuk username dan password dalam format plain text (tidak terenkripsi) sehingga rawan disadap."},
            {"key": "B", "text": "Tidak mendukung autentikasi username dan password sehingga siapa saja bisa langsung masuk."},
            {"key": "C", "text": "Hanya dapat berjalan pada media serat optik dan menolak koneksi melalui kabel UTP tembaga."},
            {"key": "D", "text": "Membutuhkan bandwidth internet minimum 100 Mbps untuk membuka satu sesi command line."},
            {"key": "E", "text": "Mengubah konfigurasi hardware router menjadi read-only secara otomatis setelah 5 menit."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "ENKRIPSI PROTOKOL REMOTE MANAGEMENT",
            "latex": "\\begin{cases} \\text{Telnet (Port 23):} & \\text{Clear-text / Plain-text (Rawan Eavesdropping via Wireshark)} \\\\ \\text{SSH (Port 22):} & \\text{Asymmetric/Symmetric Encryption (TLS/Diffie-Hellman)} \\end{cases}",
            "legend": "• Paket Telnet dapat dibaca telanjang melalui packet sniffer<br>• SSH mengamankan channel komunikasi dari ancaman Man-in-the-Middle"
        },
        "hints": {
            "concept": "Kata kunci keamanan: 'Plain text' vs 'Enkripsi'.",
            "execution": "Telnet (port 23) mengirimkan kredensial tanpa enkripsi sama sekali, sedangkan SSH (port 22) mengenkripsi seluruh sesi."
        },
        "explanation": "Protokol Telnet (port 23) dikembangkan sebelum era ancaman keamanan modern. Telnet mentransmisikan seluruh lalu lintas datanya—termasuk kredensial login akun root/admin dan perintah yang diketikkan—dalam bentuk teks biasa (plain text). Seseorang yang menjalankan packet analyzer (seperti Wireshark) di jalur jaringan yang sama dapat menangkap dan membaca username serta password tersebut dengan mudah. SSH menggantikan Telnet dengan mengenkripsi seluruh sesi komunikasi.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-24",
        "subject": "tkj",
        "materi": "PERINTAH DIAGNOSTIK JARINGAN",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Fungsi Perintah Traceroute / Tracert",
        "type": "mcq",
        "questionHtml": "Perintah diagnostik `tracert` pada sistem operasi Windows atau `traceroute` pada Linux bekerja dengan memanipulasi nilai pada header IP untuk memetakan setiap hop router yang dilewati paket. Nilai field header IP yang dimanipulasi adalah...",
        "options": [
            {"key": "A", "text": "Time to Live (TTL) yang dinaikkan secara bertahap mulai dari nilai 1."},
            {"key": "B", "text": "Quality of Service (QoS) Differentiated Services Code Point (DSCP)."},
            {"key": "C", "text": "Checksum IP yang dibuat sengaja rusak agar paket didrop router target."},
            {"key": "D", "text": "Fragment Offset yang diisi nilai acak untuk memecah frame data."},
            {"key": "E", "text": "Source IP Address yang disamarkan dengan metode dynamic IP spoofing."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "MEKANISME KERJA TRACEROUTE (TTL EXPIRY)",
            "latex": "\\text{Hop } 1: \\text{TTL}=1 \\implies \\text{Router 1 reply } \\texttt{ICMP Time Exceeded (Type 11)}",
            "legend": "• TTL = 1: Didrop oleh router pertama<br>• TTL = 2: Didrop oleh router kedua<br>• Terus dinaikkan hingga paket mencapai host tujuan akhir"
        },
        "hints": {
            "concept": "Setiap kali paket melewati satu router (hop), nilai TTL akan dikurangi 1. Jika TTL = 0, router akan membuang paket dan mengirim pesan 'Time Exceeded'.",
            "execution": "Traceroute mengirim paket dengan TTL=1, lalu TTL=2, TTL=3, dst., untuk merekam alamat IP dari setiap router yang mengirimkan pesan ICMP Time Exceeded."
        },
        "explanation": "Traceroute bekerja dengan mengirimkan serangkaian paket (ICMP atau UDP) dengan nilai Time to Live (TTL) yang dinaikkan secara bertahap. Paket pertama dikirim dengan TTL=1. Saat mencapai router pertama, router mengurangi TTL menjadi 0, mendrop paket, dan mengirim kembali pesan 'ICMP Time-to-Live Exceeded' ke pengirim (sehingga IP router pertama terdeteksi). Paket berikutnya dikirim dengan TTL=2, dan seterusnya hingga mencapai tujuan akhir.",
        "isDiagnostic": False
    },
    {
        "id": "tkj-lat-e-25",
        "subject": "tkj",
        "materi": "K3LH & KETENAGAKERJAAN TJKT",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Alat Pelindung Diri (APD) Pemasangan Antena Tower",
        "type": "mcq",
        "questionHtml": "Saat seorang teknisi jaringan ditugaskan memasang perangkat radio wireless point-to-point pada menara tower triangle setinggi 30 meter, Alat Pelindung Diri (APD) wajib yang paling krusial untuk mencegah kecelakaan fatal jatuh dari ketinggian adalah...",
        "options": [
            {"key": "A", "text": "Full Body Harness dengan tali lanyard ganda penyerap kejut (energy absorber)."},
            {"key": "B", "text": "Kacamata pelindung sinar UV matahari dan sarung tangan kain biasa."},
            {"key": "C", "text": "Sepatu beralas karet biasa tanpa pelindung baja di ujung jari kaki."},
            {"key": "D", "text": "Jas hujan anti air parasut dan masker kain penangkal debu jalanan."},
            {"key": "E", "text": "Rompi visibilitas oranye tanpa tali pengait sabuk keselamatan."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "STANDAR K3 BEKERJA DI KETINGGIAN (PERMENAKER NO. 9 TAHUN 2016)",
            "latex": "h > 1.8\\,\\text{m} \\implies \\text{Wajib Fall Protection System (Full Body Harness + Lanyard)}",
            "legend": "• Full Body Harness: Menahan beban tubuh saat terjatuh tanpa mencederai organ dalam<br>• Double Lanyard with Absorber: Menjamin teknisi selalu terhubung saat berpindah pijakan"
        },
        "hints": {
            "concept": "Bekerja pada menara di atas ketinggian 1.8 meter wajib menggunakan sistem penahan jatuh (fall protection system).",
            "execution": "Full Body Harness dengan tali ganda (double lanyard) adalah perlengkapan utama keselamatan kerja di ketinggian."
        },
        "explanation": "Berdasarkan Peraturan Menteri Ketenagakerjaan No. 9 Tahun 2016 tentang Keselamatan dan Kesehatan Kerja dalam Pekerjaan pada Ketinggian, pekerjaan di atas ketinggian 1.8 meter wajib dilengkapi dengan Alat Pelindung Jatuh Perorangan. Penggunaan Full Body Harness dengan double lanyard berpengait besar (carabiner/snap hook) dan energy absorber memastikan bahwa teknisi selalu memiliki minimal satu titik cantolan yang terpasang kokoh saat bergerak memanjat tower.",
        "isDiagnostic": False
    }
]
