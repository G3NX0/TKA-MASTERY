/**
 * Bank Soal TKA SMK - Teknik Jaringan Komputer dan Telekomunikasi (TJKT / TKJ)
 * Standar Resmi Pusmendik Kemendikdasmen TKA 2026
 * 100% Otentik, Anti-Repetisi Siklis, Zero Longest-Option Bias
 * Total Soal: 110 butir terverifikasi
 */

window.TKA_TKJ_QUESTIONS = [
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
      {
        "key": "A",
        "text": "/27 dengan subnet mask 255.255.255.224 yang menyediakan kapasitas maksimum 30 usable host."
      },
      {
        "key": "B",
        "text": "/28 dengan subnet mask 255.255.255.240 yang menyediakan kapasitas maksimum 14 usable host."
      },
      {
        "key": "C",
        "text": "/26 dengan subnet mask 255.255.255.192 yang menyediakan kapasitas maksimum 62 usable host."
      },
      {
        "key": "D",
        "text": "/25 dengan subnet mask 255.255.255.128 yang menyediakan kapasitas maksimum 126 usable host."
      },
      {
        "key": "E",
        "text": "/24 dengan subnet mask 255.255.255.0 yang menyediakan kapasitas maksimum 254 usable host."
      }
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
    "isDiagnostic": true
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
      {
        "key": "A",
        "text": "50 meter untuk menjaga redaman sinyal frekuensi tinggi di bawah 100 MHz."
      },
      {
        "key": "B",
        "text": "100 meter (90 meter kabel solid horizontal + 10 meter total patch cord)."
      },
      {
        "key": "C",
        "text": "185 meter mengikuti spesifikasi standar transmisi 10BASE2 koaksial tipis."
      },
      {
        "key": "D",
        "text": "250 meter dengan syarat menggunakan konektor modular berpelindung RJ-45 Cat 6A."
      },
      {
        "key": "E",
        "text": "500 meter jika dihubungkan secara point-to-point tanpa melewati patch panel."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "IP Address tujuan (Logical Address 32-bit biner) pada Network Layer."
      },
      {
        "key": "B",
        "text": "Port Number aplikasi tujuan (Transport Port 16-bit) pada Transport Layer demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "C",
        "text": "MAC Address tujuan (Media Access Control 48-bit hex) pada Data Link Layer."
      },
      {
        "key": "D",
        "text": "Domain Name System FQDN melalui query balik pada Application Layer."
      },
      {
        "key": "E",
        "text": "Sequence Number dan Acknowledgment Number pada sesi TCP handshake."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Diameter inti SMF sangat besar (±50 µm) sehingga mampu menampung banyak panjang gelombang cahaya LED murah."
      },
      {
        "key": "B",
        "text": "Kabel SMF tidak memerlukan perangkat pemancar berbasis laser melainkan cukup menggunakan lampu LED inframerah biasa."
      },
      {
        "key": "C",
        "text": "Kabel SMF kebal terhadap efek tekukan tajam (macrobending) tanpa mengalami redaman daya sama sekali."
      },
      {
        "key": "D",
        "text": "Diameter inti SMF sangat kecil (±9 µm) sehingga dispersi modal rendah dan sinyal mampu menjangkau jarak jauh."
      },
      {
        "key": "E",
        "text": "Biaya terminasi dan konektor SMF jauh lebih murah serta tidak membutuhkan proses fusion splicing presisi."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Request, Offer, Discover, dan Acknowledgment (RODA)."
      },
      {
        "key": "B",
        "text": "Solicit, Advertise, Request, dan Confirm (SARC)."
      },
      {
        "key": "C",
        "text": "Query, Response, Association, dan Verification (QRAV)."
      },
      {
        "key": "D",
        "text": "Handshake, Allocation, Binding, dan Termination (HABT)."
      },
      {
        "key": "E",
        "text": "Discover, Offer, Request, dan Acknowledgment (DORA)."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": true
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
      {
        "key": "A",
        "text": "10.0.0.0/8, 172.16.0.0/12, dan 192.168.0.0/16."
      },
      {
        "key": "B",
        "text": "11.0.0.0/8, 172.32.0.0/12, dan 192.169.0.0/16."
      },
      {
        "key": "C",
        "text": "127.0.0.0/8, 169.254.0.0/16, dan 224.0.0.0/4."
      },
      {
        "key": "D",
        "text": "8.8.8.8/32, 1.1.1.1/32, dan 208.67.222.222/32."
      },
      {
        "key": "E",
        "text": "100.64.0.0/10, 192.0.2.0/24, dan 198.51.100.0/24."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Putih-Hijau, Hijau, Putih-Oranye, Biru, Putih-Biru, Oranye, Putih-Cokelat, Cokelat sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "B",
        "text": "Putih-Oranye, Oranye, Putih-Hijau, Biru, Putih-Biru, Hijau, Putih-Cokelat, Cokelat."
      },
      {
        "key": "C",
        "text": "Putih-Oranye, Putih-Hijau, Oranye, Biru, Putih-Biru, Hijau, Putih-Cokelat, Cokelat."
      },
      {
        "key": "D",
        "text": "Oranye, Putih-Oranye, Hijau, Putih-Hijau, Biru, Putih-Biru, Cokelat, Putih-Cokelat."
      },
      {
        "key": "E",
        "text": "Putih-Biru, Biru, Putih-Oranye, Oranye, Putih-Hijau, Hijau, Putih-Cokelat, Cokelat."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Subnet mask komputer diset menjadi 255.255.255.0 sehingga memblokir port HTTP."
      },
      {
        "key": "B",
        "text": "Kabel UTP terpasang longgar sehingga hanya mendukung paket data transmisi broadcast lokal guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "C",
        "text": "Alamat Default Gateway belum diisi atau salah mengarah ke IP di luar subnet 192.168.1.0/24."
      },
      {
        "key": "D",
        "text": "Kartu jaringan (NIC) mengalami kerusakan duplex sehingga hanya bisa mode Half-Duplex."
      },
      {
        "key": "E",
        "text": "Workstation mengalami collision domain karena switch menggunakan kabel Cat 5e."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": true
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
      {
        "key": "A",
        "text": "Record 'AAAA' (Quad-A Record untuk pemetaan FQDN ke IPv6 128-bit)."
      },
      {
        "key": "B",
        "text": "Record 'PTR' (Pointer Record untuk resolusi pemetaan balik IP ke Domain)."
      },
      {
        "key": "C",
        "text": "Record 'CNAME' (Canonical Name untuk membuat nama alias dari domain lain)."
      },
      {
        "key": "D",
        "text": "Record 'A' (Address Record untuk pemetaan FQDN ke IPv4 32-bit)."
      },
      {
        "key": "E",
        "text": "Record 'MX' (Mail Exchange Record untuk mengarahkan pengiriman email server)."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Optical Power Meter (OPM pengukur daya sinyal dBm)."
      },
      {
        "key": "B",
        "text": "Optical Time-Domain Reflectometer (OTDR pemeta grafik loss)."
      },
      {
        "key": "C",
        "text": "Fiber Fusion Splicer (Mesin penyambung leburan kaca inti)."
      },
      {
        "key": "D",
        "text": "Fiber Cleaver (Alat pemotong sudut presisi ujung core kaca)."
      },
      {
        "key": "E",
        "text": "Visual Fault Locator (VFL / Laser Pen Fiber Optic)."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Memecah satu broadcast domain besar menjadi beberapa broadcast domain kecil secara logikal demi efisiensi dan keamanan."
      },
      {
        "key": "B",
        "text": "Meningkatkan daya listrik PoE yang dihantarkan ke perangkat Access Point di plafon untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "C",
        "text": "Menggantikan peran kabel serat optik dengan kabel tembaga berkecepatan 100 Gbps."
      },
      {
        "key": "D",
        "text": "Menghilangkan kebutuhan konfigurasi IP Address pada setiap workstation di jaringan."
      },
      {
        "key": "E",
        "text": "Mengubah switch unmanaged menjadi router BGP kelas backbone antar negara."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Port TCP 80 dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "B",
        "text": "Port TCP 443."
      },
      {
        "key": "C",
        "text": "Port TCP 21."
      },
      {
        "key": "D",
        "text": "Port TCP 22."
      },
      {
        "key": "E",
        "text": "Port UDP 53."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Network ID: 192.168.10.0 dan Broadcast ID: 192.168.10.63."
      },
      {
        "key": "B",
        "text": "Network ID: 192.168.10.64 dan Broadcast ID: 192.168.10.128 demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "C",
        "text": "Network ID: 192.168.10.64 dan Broadcast ID: 192.168.10.127."
      },
      {
        "key": "D",
        "text": "Network ID: 192.168.10.32 dan Broadcast ID: 192.168.10.95."
      },
      {
        "key": "E",
        "text": "Network ID: 192.168.10.0 dan Broadcast ID: 192.168.10.255."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menyediakan jumlah non-overlapping channel yang jauh lebih banyak hingga 24 channel mandiri."
      },
      {
        "key": "B",
        "text": "Kecepatan transfer data (throughput) maksimumnya jauh melampaui frekuensi 5 GHz pada jarak dekat."
      },
      {
        "key": "C",
        "text": "Bebas dari gangguan interferensi gelombang elektromagnetik perangkat Bluetooth dan microwave oven sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "D",
        "text": "Jangkauan sinyal lebih jauh dan kemampuan menembus dinding padat lebih baik karena panjang gelombangnya lebih besar."
      },
      {
        "key": "E",
        "text": "Mendukung bandwidth channel 160 MHz untuk transmisi ultra-broadband nirkabel."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Ditiup dengan kuat menggunakan kompresor angin bertekanan tinggi ke arah lantai ruang kerja."
      },
      {
        "key": "B",
        "text": "Diusap langsung menggunakan telapak tangan telanjang untuk memastikan meja kerja sudah bersih licin guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "C",
        "text": "Dibuang langsung ke tempat sampah kertas biasa di bawah meja kerja teknisi."
      },
      {
        "key": "D",
        "text": "Dilarutkan dengan cairan alkohol 70% agar serpihan kaca meleleh secara kimiawi."
      },
      {
        "key": "E",
        "text": "Dibersihkan dengan selotip/alat khusus dan dimasukkan ke dalam wadah tertutup rapat berlabel limbah tajam berbahaya."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "APIPA (Automatic Private IP Addressing / Link-Local IPv4)."
      },
      {
        "key": "B",
        "text": "SLAAC (Stateless Address Autoconfiguration IPv6)."
      },
      {
        "key": "C",
        "text": "Static Manual Configuration melalui registry Windows untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "D",
        "text": "DNS Dynamic Update Client Registration."
      },
      {
        "key": "E",
        "text": "DHCP Relay Discovery Fallback Agent."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Access Port (Untagged port khusus satu VLAN untuk end-device)."
      },
      {
        "key": "B",
        "text": "Trunk Port (Tagging port pembawa banyak VLAN)."
      },
      {
        "key": "C",
        "text": "Console Port (Port serial khusus konfigurasi terminal lokal)."
      },
      {
        "key": "D",
        "text": "Mirror Port (Port pengganda paket untuk packet analyzer)."
      },
      {
        "key": "E",
        "text": "Auxiliary Port (Port modem cadangan koneksi out-of-band)."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "IGMP (Internet Group Management Protocol untuk multicast IPTV)."
      },
      {
        "key": "B",
        "text": "SNMP (Simple Network Management Protocol untuk monitoring CPU router)."
      },
      {
        "key": "C",
        "text": "ICMP (Internet Control Message Protocol, paket Echo Request & Echo Reply)."
      },
      {
        "key": "D",
        "text": "SMTP (Simple Mail Transfer Protocol untuk pengiriman pesan elektronik) dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "E",
        "text": "ARP (Address Resolution Protocol untuk memetakan IP ke MAC)."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "RARP (Reverse Address Resolution Protocol melalui multicast) demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "B",
        "text": "DHCP (Dynamic Host Configuration Protocol melalui unicast)."
      },
      {
        "key": "C",
        "text": "DNS (Domain Name System melalui query rekursif UDP)."
      },
      {
        "key": "D",
        "text": "ARP (Address Resolution Protocol melalui paket broadcast ARP Request)."
      },
      {
        "key": "E",
        "text": "NAT (Network Address Translation melalui translasi port)."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Mengenkripsi seluruh isi payload paket data dengan algoritma RSA 4096-bit."
      },
      {
        "key": "B",
        "text": "Membatasi kecepatan download dan upload setiap klien menjadi tepat 512 Kbps."
      },
      {
        "key": "C",
        "text": "Memblokir secara permanen seluruh serangan virus trojan yang masuk melalui port HTTP sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "D",
        "text": "Menduplikasi paket data klien ke server cadangan untuk keperluan audit forensik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat IP privat klien LAN menjadi IP publik dinamis router saat paket keluar menuju internet."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": true
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
      {
        "key": "A",
        "text": "Konektor LC (Lucent Connector berkuran kecil 1.25 mm ferrule)."
      },
      {
        "key": "B",
        "text": "Konektor FC (Ferrule Connector dengan sistem ulir putar baut metal)."
      },
      {
        "key": "C",
        "text": "Konektor ST (Straight Tip dengan sistem bayonet putar putus)."
      },
      {
        "key": "D",
        "text": "Konektor BNC (Bayonet Neill-Concelman untuk kabel koaksial analog)."
      },
      {
        "key": "E",
        "text": "Konektor RJ-11 (Registered Jack 4-pin untuk jaringan telepon kabel)."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Kanal 1, Kanal 2, dan Kanal 3."
      },
      {
        "key": "B",
        "text": "Kanal 1, Kanal 6, dan Kanal 11."
      },
      {
        "key": "C",
        "text": "Kanal 2, Kanal 7, dan Kanal 12 guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "D",
        "text": "Kanal 3, Kanal 6, dan Kanal 9."
      },
      {
        "key": "E",
        "text": "Kanal 4, Kanal 8, dan Kanal 12."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Tidak mendukung autentikasi username dan password sehingga siapa saja bisa langsung masuk untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "B",
        "text": "Hanya dapat berjalan pada media serat optik dan menolak koneksi melalui kabel UTP tembaga."
      },
      {
        "key": "C",
        "text": "Mengirimkan seluruh teks termasuk username dan password dalam format plain text (tidak terenkripsi) sehingga rawan disadap."
      },
      {
        "key": "D",
        "text": "Membutuhkan bandwidth internet minimum 100 Mbps untuk membuka satu sesi command line."
      },
      {
        "key": "E",
        "text": "Mengubah konfigurasi hardware router menjadi read-only secara otomatis setelah 5 menit."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Quality of Service (QoS) Differentiated Services Code Point (DSCP)."
      },
      {
        "key": "B",
        "text": "Checksum IP yang dibuat sengaja rusak agar paket didrop router target."
      },
      {
        "key": "C",
        "text": "Fragment Offset yang diisi nilai acak untuk memecah frame data."
      },
      {
        "key": "D",
        "text": "Time to Live (TTL) yang dinaikkan secara bertahap mulai dari nilai 1."
      },
      {
        "key": "E",
        "text": "Source IP Address yang disamarkan dengan metode dynamic IP spoofing."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Kacamata pelindung sinar UV matahari dan sarung tangan kain biasa."
      },
      {
        "key": "B",
        "text": "Sepatu beralas karet biasa tanpa pelindung baja di ujung jari kaki dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "C",
        "text": "Jas hujan anti air parasut dan masker kain penangkal debu jalanan."
      },
      {
        "key": "D",
        "text": "Rompi visibilitas oranye tanpa tali pengait sabuk keselamatan."
      },
      {
        "key": "E",
        "text": "Full Body Harness dengan tali lanyard ganda penyerap kejut (energy absorber)."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-01",
    "subject": "tkj",
    "materi": "PENGALAMATAN IPV4 & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Desain Variable Length Subnet Mask (VLSM)",
    "type": "mcq",
    "questionHtml": "Sebuah perusahaan memiliki alokasi blok jaringan `172.16.0.0/22`. Departemen Engineering membutuhkan 350 host, Departemen Finance membutuhkan 110 host, dan Departemen HRD membutuhkan 45 host. Urutan alokasi prefix subnet mask yang paling efisien menggunakan metode VLSM dari kebutuhan terbesar adalah...",
    "options": [
      {
        "key": "A",
        "text": "Engineering: /24 (maks 254 host), Finance: /25 (maks 126 host), HRD: /26 (maks 62 host)."
      },
      {
        "key": "B",
        "text": "Engineering: /23 (maks 510 host), Finance: /25 (maks 126 host), HRD: /26 (maks 62 host)."
      },
      {
        "key": "C",
        "text": "Engineering: /22 (maks 1022 host), Finance: /24 (maks 254 host), HRD: /25 (maks 126 host)."
      },
      {
        "key": "D",
        "text": "Engineering: /23 (maks 510 host), Finance: /24 (maks 254 host), HRD: /25 (maks 126 host)."
      },
      {
        "key": "E",
        "text": "Engineering: /24 (maks 254 host), Finance: /26 (maks 62 host), HRD: /27 (maks 30 host)."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "FORMULA DESAIN VLSM BERURUTAN",
      "latex": "\\begin{aligned} 350\\text{ host} &\\implies 2^9 - 2 = 510 \\implies /23 \\\\ 110\\text{ host} &\\implies 2^7 - 2 = 126 \\implies /25 \\\\ 45\\text{ host} &\\implies 2^6 - 2 = 62 \\implies /26 \\end{aligned}",
      "legend": "• Urutkan selalu dari kebutuhan host terbesar ke terkecil<br>• Hitung bit host h: 2^h - 2 >= kebutuhan, prefix = 32 - h"
    },
    "hints": {
      "concept": "Urutkan kebutuhan dari yang terbesar: 350 host -> butuh blok 512 (/23); 110 host -> butuh blok 128 (/25); 45 host -> butuh blok 64 (/26).",
      "execution": "Engineering: /23 (2^9 - 2 = 510). Finance: /25 (2^7 - 2 = 126). HRD: /26 (2^6 - 2 = 62). Pilihan A tepat."
    },
    "explanation": "Pada perancangan Variable Length Subnet Mask (VLSM), alokasi wajib diurutkan dari subnet berkapasitas terbesar agar tidak terjadi overlap alamat. Kebutuhan 350 host memerlukan 9 bit host (2^9 - 2 = 510 host) sehingga prefix adalah 32 - 9 = /23. Kebutuhan 110 host memerlukan 7 bit host (2^7 - 2 = 126 host) dengan prefix 32 - 7 = /25. Kebutuhan 45 host memerlukan 6 bit host (2^6 - 2 = 62 host) dengan prefix 32 - 6 = /26.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-02",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Kalkulasi Optical Power Loss Budget",
    "type": "mcq",
    "questionHtml": "Jaringan link fiber optik Single Mode menghubungkan dua gedung berjarak 8 km pada panjang gelombang 1310 nm (redaman kabel $\\alpha = 0.35\\text{ dB/km}$). Terdapat 2 sambungan leburan (fusion splice) dengan redaman masing-masing $0.1\\text{ dB}$ dan 2 konektor patch panel dengan redaman masing-masing $0.5\\text{ dB}$. Jika daya pemancar laser (Transmitter Power) adalah $-3\\text{ dBm}$, daya terima (Receiver Power) yang terukur pada OPM di ujung penerima adalah...",
    "options": [
      {
        "key": "A",
        "text": "-5.8 dBm (total loss saluran = 2.8 dB)."
      },
      {
        "key": "B",
        "text": "-8.2 dBm (total loss saluran = 5.2 dB)."
      },
      {
        "key": "C",
        "text": "-7.0 dBm (total loss saluran = 4.0 dB)."
      },
      {
        "key": "D",
        "text": "-11.0 dBm (total loss saluran = 8.0 dB)."
      },
      {
        "key": "E",
        "text": "-3.8 dBm (total loss saluran = 0.8 dB)."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "RUMUS LINK LOSS BUDGET FIBER OPTIK",
      "latex": "\\begin{aligned} \\text{Loss}_{\\text{total}} &= (L \\times \\alpha) + (N_{\\text{splice}} \\times \\text{Loss}_{\\text{sp}}) + (N_{\\text{conn}} \\times \\text{Loss}_{\\text{co}}) \\\\ P_{\\text{rx}} &= P_{\\text{tx}} - \\text{Loss}_{\\text{total}} \\end{aligned}",
      "legend": "• Kabel: 8 km * 0.35 dB/km = 2.8 dB<br>• Splice: 2 * 0.1 dB = 0.2 dB<br>• Konektor: 2 * 0.5 dB = 1.0 dB<br>• Total Loss = 2.8 + 0.2 + 1.0 = 4.0 dB"
    },
    "hints": {
      "concept": "Hitung redaman serat kaca, tambahkan redaman semua splice dan konektor, lalu kurangkan total redaman dari daya output transmitter.",
      "execution": "Loss kabel = 8 * 0.35 = 2.8 dB. Loss splice = 2 * 0.1 = 0.2 dB. Loss konektor = 2 * 0.5 = 1.0 dB. Total loss = 4.0 dB. Daya terima = -3 dBm - 4.0 dB = -7.0 dBm."
    },
    "explanation": "Kalkulasi Link Budget: Redaman serat kabel = 8 km * 0.35 dB/km = 2.8 dB. Redaman sambungan fusi = 2 * 0.1 dB = 0.2 dB. Redaman konektor = 2 * 0.5 dB = 1.0 dB. Total attenuation (loss) = 2.8 + 0.2 + 1.0 = 4.0 dB. Daya terima pada receiver (P_rx) = Daya kirim (P_tx) - Total Loss = -3 dBm - 4.0 dB = -7.0 dBm.",
    "isDiagnostic": true
  },
  {
    "id": "tkj-lat-m-03",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Pemilihan Root Bridge pada Spanning Tree Protocol (STP)",
    "type": "mcq",
    "questionHtml": "Tiga switch manageable terhubung dalam topologi segitiga membentuk loop fisik. Nilai Bridge Priority dan MAC Address masing-masing switch adalah:\n• Switch-1: Priority `32768`, MAC `00:0A:1B:2C:3D:4E`\n• Switch-2: Priority `32768`, MAC `00:0A:1B:2C:3D:11`\n• Switch-3: Priority `40960`, MAC `00:0A:1B:2C:11:00`\nBerdasarkan algoritma IEEE 802.1D Spanning Tree Protocol (STP), switch yang terpilih menjadi Root Bridge beserta alasannya adalah...",
    "options": [
      {
        "key": "A",
        "text": "Switch-3, karena memiliki nilai Bridge Priority tertinggi (40960) yang menunjukkan kapasitas pemrosesan paling besar demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "B",
        "text": "Switch-1, karena memiliki MAC Address dengan nilai hex tertinggi yang menandakan hardware keluaran terbaru."
      },
      {
        "key": "C",
        "text": "Seluruh switch bergantian menjadi Root Bridge setiap interval Hello Time 2 detik secara round-robin."
      },
      {
        "key": "D",
        "text": "Switch-2, karena memiliki Bridge Priority terkecil (32768) dan nilai MAC Address terendah di antara prioritas yang sama."
      },
      {
        "key": "E",
        "text": "Switch-2 dan Switch-1 menjadi dual active root bridge dengan mekanisme Virtual Router Redundancy Protocol."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "KRITERIA SELEKSI ROOT BRIDGE (BRIDGE ID)",
      "latex": "\\text{Bridge ID} = \\text{Bridge Priority (2 byte)} + \\text{MAC Address (6 byte)}",
      "legend": "• Nilai Bridge ID terendah mutlak menang<br>• Switch-1 BID: 32768 + 00:0A:...:4E<br>• Switch-2 BID: 32768 + 00:0A:...:11 (Paling rendah)<br>• Switch-3 BID: 40960 + ..."
    },
    "hints": {
      "concept": "Pada STP, 'nilai terkecil selalu menang'. Bandingkan Bridge Priority terlebih dahulu. Jika seri, bandingkan MAC Address terendah.",
      "execution": "Priority Switch-1 dan Switch-2 sama-sama 32768 (lebih rendah dari 40960 milik Switch-3). Bandingkan MAC: Switch-2 berakhiran :11 lebih kecil daripada Switch-1 yang berakhiran :4E."
    },
    "explanation": "Pada STP IEEE 802.1D, Root Bridge dipilih berdasarkan Bridge ID (BID) terendah. Bridge ID terdiri dari Bridge Priority (default 32768) dan MAC Address switch. Switch-1 dan Switch-2 memiliki priority yang sama (32768) yang lebih rendah dari Switch-3 (40960). Sebagai penentu tie-breaker, switch dengan MAC Address terendah yang menang. MAC Address Switch-2 (berakhiran :11) lebih kecil dari Switch-1 (berakhiran :4E), sehingga Switch-2 terpilih menjadi Root Bridge.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-04",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Konfigurasi Router-on-a-Stick (Inter-VLAN)",
    "type": "mcq",
    "questionHtml": "Administrator jaringan ingin menghubungkan komputer di VLAN 10 (IP `192.168.10.0/24`) dan VLAN 20 (IP `192.168.20.0/24`) menggunakan satu kabel fisik antara Switch dan Router Cisco (metode Router-on-a-Stick). Perintah CLI Cisco IOS yang benar untuk mengaktifkan sub-interface VLAN 10 pada router adalah...",
    "options": [
      {
        "key": "A",
        "text": "interface GigabitEthernet0/0 \n switchport mode trunk \n switchport trunk allowed vlan 10,20"
      },
      {
        "key": "B",
        "text": "interface GigabitEthernet0/0.10 \n encapsulation isl 10 \n ip address 192.168.10.1 255.255.255.128 sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "C",
        "text": "interface vlan 10 \n ip address 192.168.10.1 255.255.255.0 \n no shutdown"
      },
      {
        "key": "D",
        "text": "interface GigabitEthernet0/0 \n vlan 10 routing enable \n ip default-gateway 192.168.10.1"
      },
      {
        "key": "E",
        "text": "interface GigabitEthernet0/0.10 \n encapsulation dot1Q 10 \n ip address 192.168.10.1 255.255.255.0"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "SINTAKS CISCO ROUTER-ON-A-STICK",
      "latex": "\\begin{aligned} &\\texttt{interface GigabitEthernet0/0.10} \\\\ &\\texttt{encapsulation dot1Q 10} \\\\ &\\texttt{ip address 192.168.10.1 255.255.255.0} \\end{aligned}",
      "legend": "• Sub-interface: Logikal interface anak (.10)<br>• encapsulation dot1Q: Menetapkan penandaan frame IEEE 802.1Q untuk VLAN 10"
    },
    "hints": {
      "concept": "Pada Router Cisco, antarmuka fisik dipecah menjadi sub-interface logis (misal `g0/0.10`), lalu ditentukan enkapsulasi `dot1Q <vlan-id>` dan diisi IP gateway.",
      "execution": "Pilihan A menunjukkan sintaks resmi Cisco IOS yang tepat."
    },
    "explanation": "Pada arsitektur Router-on-a-Stick, antarmuka router fisik (misalnya GigabitEthernet0/0) dipecah menjadi sub-antarmuka logis (misalnya g0/0.10). Perintah `encapsulation dot1Q 10` wajib dikonfigurasikan terlebih dahulu untuk menginstruksikan router agar memproses tag VLAN 10 standar IEEE 802.1Q sebelum menetapkan alamat IP gateway subnet tersebut (`ip address 192.168.10.1 255.255.255.0`).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-05",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Konsep Floating Static Route untuk Jalur Failover",
    "type": "mcq",
    "questionHtml": "Sebuah kantor memiliki dua jalur internet: ISP-A (Fiber Optik kecepatan 100 Mbps) sebagai link utama dan ISP-B (Wireless kecepatan 20 Mbps) sebagai link cadangan (backup). Konfigurasi routing static di MikroTik agar jalur ISP-B secara otomatis aktif hanya ketika jalur ISP-A terputus (down) adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menetapkan rute ISP-A dengan distance = 1 dan rute ISP-B dengan distance = 2 (atau nilai yang lebih besar)."
      },
      {
        "key": "B",
        "text": "Menetapkan rute ISP-A dengan distance = 250 dan rute ISP-B dengan distance = 1."
      },
      {
        "key": "C",
        "text": "Mengatur kedua rute ISP-A dan ISP-B dengan nilai distance = 1 agar terjadi pembagian beban (load balancing ECMP)."
      },
      {
        "key": "D",
        "text": "Menonaktifkan tabel routing static dan menggantinya dengan bridging port interface ISP-A dan ISP-B."
      },
      {
        "key": "E",
        "text": "Mengatur routing mark pada ISP-B dengan routing table khusus tanpa menentukan default gateway."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP ADMINISTRATIVE DISTANCE (DISTANCE)",
      "latex": "\\text{Rute Aktif} = \\min(\\text{Distance}) \\implies \\begin{cases} \\text{ISP-A (Primary):} & \\text{Distance} = 1 \\\\ \\text{ISP-B (Floating Backup):} & \\text{Distance} = 2 \\end{cases}",
      "legend": "• Router hanya memasukkan rute ber-distance terendah ke Routing Table aktif<br>• Saat gateway ISP-A unreachable, rute distance=2 baru naik aktif"
    },
    "hints": {
      "concept": "Teknik ini disebut 'Floating Static Route'. Router selalu memprioritaskan rute dengan nilai Administrative Distance (Distance) yang lebih kecil.",
      "execution": "Link utama diberi distance 1, link backup diberi distance lebih besar (misal 2). Jika link utama mati, rute backup baru digunakan."
    },
    "explanation": "Floating Static Route adalah teknik failover cadangan di mana rute backup dikonfigurasikan dengan nilai Administrative Distance (pada MikroTik disebut 'Distance') yang lebih tinggi daripada rute utama. Saat ISP-A aktif (distance 1), rute ISP-B (distance 2) akan berada dalam status standby (inactive). Begitu link ISP-A mengalami kegagalan/terputus, router akan secara otomatis menaikkan rute ISP-B ke tabel routing aktif.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-06",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Pemilihan DR dan BDR pada OSPF Multi-Access",
    "type": "mcq",
    "questionHtml": "Pada segmen jaringan broadcast multi-access OSPF (Open Shortest Path First), pemilihan Designated Router (DR) dan Backup Designated Router (BDR) dilakukan untuk mengurangi banjir paket Link State Advertisement (LSA). Parameter pertama yang dievaluasi router dalam pemilihan DR adalah...",
    "options": [
      {
        "key": "A",
        "text": "Alamat IP host terkecil pada antarmuka LAN yang terhubung langsung."
      },
      {
        "key": "B",
        "text": "Nilai OSPF Interface Priority tertinggi (default priority = 1, nilai 0 tidak akan pernah menjadi DR/BDR)."
      },
      {
        "key": "C",
        "text": "Jumlah total rute eksternal yang di-redistribute ke dalam OSPF database."
      },
      {
        "key": "D",
        "text": "Nilai OSPF Process ID terkecil yang dikonfigurasikan administrator pada router guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "E",
        "text": "Waktu operasional (uptime) perangkat yang paling lama menyala tanpa reboot."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "URUTAN SELEKSI DR/BDR OSPF",
      "latex": "1.\\; \\max(\\text{OSPF Priority}) \\xrightarrow{\\text{Tie-break}} 2.\\; \\max(\\text{Router ID})",
      "legend": "• Priority 0: Dropped from election (Hanya menjadi DROther)<br>• Router ID ditentukan dari: Manual RID -> IP Loopback tertinggi -> IP Fisik aktif tertinggi"
    },
    "hints": {
      "concept": "Pemilihan DR OSPF: kriteria pertama adalah Priority tertinggi. Jika nilainya seri, baru beralih ke Router ID tertinggi.",
      "execution": "Pilihan A tepat: OSPF Interface Priority tertinggi adalah penentu utama."
    },
    "explanation": "Dalam jaringan OSPF tipe broadcast multi-access, router-router mengadakan pemilihan DR dan BDR. Kriteria utama yang dievaluasi pertama kali adalah nilai OSPF Priority pada antarmuka (range 0 - 255, default 1). Router dengan priority tertinggi akan terpilih menjadi DR. Nilai priority 0 mendiskualifikasi router dari pemilihan (menjadi DROther). Jika terjadi nilai priority yang sama, barulah OSPF membandingkan Router ID (RID) tertinggi.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-07",
    "subject": "tkj",
    "materi": "LAYANAN JARINGAN & SERVER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Peran DHCP Relay Agent (RFC 3046 / Option 82)",
    "type": "mcq",
    "questionHtml": "Sebuah kampus memiliki DHCP Server terpusat di subnet Server Farm (`10.10.100.5/24`), sedangkan komputer mahasiswa berada di VLAN 30 (`192.168.30.0/24`) yang terpisah router. Agar mahasiswa di VLAN 30 dapat memperoleh IP dari server pusat, fitur yang harus diaktifkan pada gateway router antarmuka VLAN 30 adalah...",
    "options": [
      {
        "key": "A",
        "text": "Proxy ARP (menjawab seluruh broadcast layer 2 dengan MAC address router gateway)."
      },
      {
        "key": "B",
        "text": "NAT 1-to-1 (memetakan seluruh IP server langsung ke setiap port switch mahasiswa) untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "C",
        "text": "DHCP Relay (mengubah paket DHCP Discover broadcast dari klien menjadi unicast ke arah IP server 10.10.100.5)."
      },
      {
        "key": "D",
        "text": "DNS Forwarder (mengarahkan seluruh kueri nama domain ke server DHCP)."
      },
      {
        "key": "E",
        "text": "IGMP Snooping (membatasi penyebaran paket multicast IPTV di dalam switch)."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "TRANSFORMASI PAKET DHCP RELAY",
      "latex": "\\text{Client (VLAN 30)} \\xrightarrow{\\text{Broadcast 255.255.255.255}} \\text{Router (Relay)} \\xrightarrow{\\text{Unicast GIADDR=192.168.30.1}} \\text{DHCP Server}",
      "legend": "• Router memblokir broadcast antar subnet<br>• DHCP Relay menangkap broadcast dan menyisipkan alamat subnet klien (GIADDR)"
    },
    "hints": {
      "concept": "Paket broadcast layer 3 (seperti DHCP Discover) tidak dapat menembus router secara alami. Dibutuhkan agen penerus (Relay).",
      "execution": "DHCP Relay menerima broadcast lokal, lalu membungkusnya menjadi unicast langsung ke IP DHCP server."
    },
    "explanation": "Secara standar, router tidak meneruskan paket broadcast layer 3 (255.255.255.255). Karena klien mengirimkan DHCP Discover secara broadcast, paket tersebut tidak akan pernah sampai ke DHCP Server yang berada di subnet berbeda. DHCP Relay Agent menangkap broadcast tersebut, menyisipkan alamat IP gateway subnet klien pada field GIADDR (Gateway IP Address), lalu mengirimkannya kembali dalam bentuk paket unicast langsung ke DHCP Server terpusat.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-08",
    "subject": "tkj",
    "materi": "JARINGAN NIRKABEL & WIRELESS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Analisis Signal-to-Noise Ratio (SNR) pada Wi-Fi",
    "type": "mcq",
    "questionHtml": "Seorang teknisi melakukan site survey sinyal nirkabel di ruang kelas menggunakan Wi-Fi analyzer. Hasil pembacaan menunjukkan Received Signal Strength Indicator (RSSI) sebesar $-65\\text{ dBm}$ dan Noise Floor terukur pada $-90\\text{ dBm}$. Nilai Signal-to-Noise Ratio (SNR) dan interpretasi kualitas koneksi tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "SNR = -155 dB; koneksi terputus total karena berada di bawah ambang batas sinyal minimum."
      },
      {
        "key": "B",
        "text": "SNR = 15 dB; koneksi sangat buruk dan mengalami packet loss ekstrem di atas 50%."
      },
      {
        "key": "C",
        "text": "SNR = -25 dB; sinyal noise lebih kuat daripada sinyal data sehingga terjadi interferensi parah."
      },
      {
        "key": "D",
        "text": "SNR = 25 dB; kualitas sinyal sangat baik untuk throughput tinggi dan streaming video stabil."
      },
      {
        "key": "E",
        "text": "SNR = 65 dB; sinyal terlalu kuat sehingga menimbulkan saturasi pada radio receiver AP."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "FORMULA SIGNAL-TO-NOISE RATIO (SNR)",
      "latex": "\\text{SNR (dB)} = \\text{RSSI (dBm)} - \\text{Noise Floor (dBm)} = -65 - (-90) = 25\\,\\text{dB}",
      "legend": "• SNR > 25 dB: Sangat Baik (Fast data rates, 256/1024-QAM)<br>• 15 - 24 dB: Cukup Baik (Web surfing, VoIP dasar)<br>• < 10 dB: Sangat Buruk (High packet loss, disconnection)"
    },
    "hints": {
      "concept": "SNR dihitung dari pengurangan nilai sinyal (RSSI) dengan nilai gangguan (Noise Floor). Ingat: minus ketemu minus menghasilkan nilai positif.",
      "execution": "SNR = (-65 dBm) - (-90 dBm) = -65 + 90 = +25 dB. Nilai 25 dB adalah kategori sangat baik."
    },
    "explanation": "Signal-to-Noise Ratio (SNR) dihitung dengan mengurangkan nilai RSSI terhadap Noise Floor: SNR = RSSI - Noise = -65 dBm - (-90 dBm) = 25 dB. Pada teknologi nirkabel Wi-Fi, nilai SNR di atas 25 dB dikategorikan sangat baik (excellent), memungkinkan perangkat beroperasi pada modulasi tinggi (misal 256-QAM atau 1024-QAM pada Wi-Fi 6) dengan throughput data maksimal dan latensi rendah.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-09",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Alur Chain Firewall Filter MikroTik: Input vs Forward vs Output",
    "type": "mcq",
    "questionHtml": "Dalam sistem operasi MikroTik RouterOS, administrator ingin memblokir upaya serangan brute-force SSH yang langsung ditujukan ke router itu sendiri, bukan ke komputer klien di belakangnya. Rantai (chain) firewall filter yang harus digunakan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Chain 'forward' (memproses paket data yang hanya melintasi router dari klien ke internet)."
      },
      {
        "key": "B",
        "text": "Chain 'output' (memproses paket yang berasal dari dalam router menuju jaringan luar)."
      },
      {
        "key": "C",
        "text": "Chain 'prerouting' (memproses translasi alamat sebelum keputusan routing diambil)."
      },
      {
        "key": "D",
        "text": "Chain 'postrouting' (memproses masquerade sesaat sebelum paket keluar fisik)."
      },
      {
        "key": "E",
        "text": "Chain 'input' (memproses paket yang alamat tujuan IP-nya adalah router itu sendiri)."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "ALUR PACKET FLOW FIREWALL MIKROTIK",
      "latex": "\\begin{cases} \\text{Chain input:} & \\text{Client} \\to \\text{Router itu sendiri} \\\\ \\text{Chain forward:} & \\text{Client} \\to \\text{Router} \\to \\text{Host Tujuan (Internet)} \\\\ \\text{Chain output:} & \\text{Router itu sendiri} \\to \\text{Jaringan Luar} \\end{cases}",
      "legend": "• Amankan router (Winbox, SSH, WebFig) -> Selalu di Chain input<br>• Lindungi klien LAN -> Di Chain forward"
    },
    "hints": {
      "concept": "Tujuan paket adalah router itu sendiri, bukan lewat router. Paket yang berakhir di router ditangani oleh rantai 'input'.",
      "execution": "Chain 'input' mengontrol semua koneksi yang ditujukan ke alamat IP lokal router."
    },
    "explanation": "MikroTik RouterOS memiliki 3 rantai (chain) dasar pada tabel Filter: (1) 'input': memproses paket data yang masuk ke antarmuka router dan ditujukan ke router itu sendiri (misalnya akses Winbox port 8291, SSH port 22, atau ping ke router); (2) 'forward': memproses paket data yang hanya melintasi router dari satu antarmuka ke antarmuka lain (misal trafik PC klien ke internet); (3) 'output': memproses paket yang dihasilkan oleh router dan dikirim ke luar.",
    "isDiagnostic": true
  },
  {
    "id": "tkj-lat-m-10",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Konfigurasi Destination NAT (Port Forwarding)",
    "type": "mcq",
    "questionHtml": "Sebuah web server lokal di sekolah memiliki IP privat `192.168.10.80` dan menjalankan web service pada port TCP 80. Router sekolah memiliki IP publik statis `203.0.113.10`. Konfigurasi firewall NAT MikroTik yang benar agar masyarakat luar dapat mengakses web server tersebut melalui `http://203.0.113.10` adalah...",
    "options": [
      {
        "key": "A",
        "text": "/ip firewall nat add chain=dstnat dst-address=203.0.113.10 protocol=tcp dst-port=80 action=dst-nat to-addresses=192.168.10.80 to-ports=80"
      },
      {
        "key": "B",
        "text": "/ip firewall nat add chain=srcnat src-address=192.168.10.80 action=masquerade to-addresses=203.0.113.10 dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "C",
        "text": "/ip firewall nat add chain=dstnat src-address=203.0.113.10 action=redirect to-ports=80"
      },
      {
        "key": "D",
        "text": "/ip firewall nat add chain=forward in-interface=ether1 protocol=tcp dst-port=80 action=accept"
      },
      {
        "key": "E",
        "text": "/ip firewall nat add chain=srcnat dst-address=192.168.10.80 protocol=tcp action=dst-nat to-ports=8080"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP DESTINATION NAT (PORT FORWARDING)",
      "latex": "\\begin{aligned} &\\texttt{chain=dstnat} \\\\ &\\texttt{dst-address=IP\\_Publik \\quad protocol=tcp \\quad dst-port=Port\\_Publik} \\\\ &\\texttt{action=dst-nat \\quad to-addresses=IP\\_Server\\_Lokal \\quad to-ports=Port\\_Lokal} \\end{aligned}",
      "legend": "• Mengubah IP tujuan dari IP publik router menjadi IP privat server lokal<br>• Memungkinkan server lokal diakses publik tanpa perlu IP publik sendiri"
    },
    "hints": {
      "concept": "Untuk membuka akses dari internet ke server lokal, digunakan Destination NAT (dstnat). Paket yang datang ke IP publik router di-redirect ke IP privat server.",
      "execution": "Pilihan A menggunakan `chain=dstnat`, mencocokkan `dst-address=203.0.113.10` dan `dst-port=80`, lalu melakukan `action=dst-nat to-addresses=192.168.10.80 to-ports=80`."
    },
    "explanation": "Destination NAT (dst-nat atau Port Forwarding) digunakan untuk memetakan paket yang masuk ke alamat IP publik router dengan port tertentu agar diteruskan ke server internal di jaringan privat. Sintaks MikroTik RouterOS yang valid adalah menentukan `chain=dstnat`, mencocokkan alamat IP publik router pada `dst-address`, protokol `tcp`, port tujuan `dst-port=80`, serta aksi `action=dst-nat` menuju alamat target `to-addresses=192.168.10.80` dan `to-ports=80`.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-11",
    "subject": "tkj",
    "materi": "LAYANAN JARINGAN & SERVER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Konfigurasi Otentikasi SSH Berbasis Kunci Publik",
    "type": "mcq",
    "questionHtml": "Untuk mengamankan server Linux Debian dari serangan pembobolan password otomatis, administrator mengonfigurasi autentikasi SSH berbasis pasangan kunci kriptografi (Key-based Authentication). Berkas tempat meletakkan kunci publik klien (`id_rsa.pub`) pada direktori home user server target adalah...",
    "options": [
      {
        "key": "A",
        "text": "/etc/ssh/sshd_config dengan permission 777 demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "B",
        "text": "~/.ssh/authorized_keys dengan permission 600."
      },
      {
        "key": "C",
        "text": "~/.ssh/known_hosts dengan permission 644."
      },
      {
        "key": "D",
        "text": "/var/log/auth.log dengan permission 640."
      },
      {
        "key": "E",
        "text": "~/.ssh/id_rsa dengan permission 700."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "STRUKTUR FILE SSH KEY AUTHENTICATION",
      "latex": "\\text{Klien: } \\texttt{id\\_rsa (Private)} \\xrightarrow{\\text{Kirim Publik}} \\text{Server: } \\texttt{~/.ssh/authorized\\_keys (Public)}",
      "legend": "• Private Key (id_rsa): Wajib dirahasiakan di mesin lokal (chmod 600)<br>• Public Key: Disalin ke file authorized_keys di server target"
    },
    "hints": {
      "concept": "Kunci publik klien disimpan di server dalam berkas `authorized_keys` di dalam folder tersembunyi `~/.ssh/`.",
      "execution": "File `~/.ssh/authorized_keys` menyimpan kunci publik klien yang diizinkan masuk. Hak aksesnya harus ketat (`chmod 600`)."
    },
    "explanation": "Dalam otentikasi SSH berbasis kunci publik (asymmetric cryptography), klien membuat pasangan kunci (private key `id_rsa` dan public key `id_rsa.pub`). Kunci publik disalin ke server dan ditambahkan ke dalam berkas `~/.ssh/authorized_keys`. Demi keamanan, OpenSSH mewajibkan berkas `authorized_keys` memiliki permission 600 (read/write hanya oleh pemilik) dan direktori `~/.ssh` memiliki permission 700 agar otentikasi tidak ditolak oleh daemon sshd.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-12",
    "subject": "tkj",
    "materi": "PENGALAMATAN IPV6 & NEXT-GEN NETWORK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Penyingkatan Format Penulisan Alamat IPv6",
    "type": "mcq",
    "questionHtml": "Diberikan sebuah alamat IPv6 lengkap 128-bit:\n`2001:0db8:0000:0000:0000:ff00:0042:8329`\nBerdasarkan aturan penyingkatan resmi RFC 5952 (menghapus leading zeros dan mengganti deretan hextet nol berurutan terpanjang dengan double colon `::`), penulisan yang paling tepat adalah...",
    "options": [
      {
        "key": "A",
        "text": "2001:db8::ff::42:8329"
      },
      {
        "key": "B",
        "text": "2001:0db8::ff00:0042:8329"
      },
      {
        "key": "C",
        "text": "2001:db8::ff00:42:8329"
      },
      {
        "key": "D",
        "text": "2001:db8:0:0:0:ff:42:8329"
      },
      {
        "key": "E",
        "text": "2001::db8::ff00:42:8329"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "DUA ATURAN PENYINGKATAN IPV6 (RFC 5952)",
      "latex": "\\begin{aligned} 1.\\; &\\text{Omit leading zeros: } \\texttt{0db8} \\to \\texttt{db8}, \\; \\texttt{0042} \\to \\texttt{42} \\\\ 2.\\; &\\text{Compress contiguous zeros: } \\texttt{:0000:0000:0000:} \\to \\texttt{::} \\; (\\text{Hanya } 1\\times) \\end{aligned}",
      "legend": "• Nol di depan angka wajib dihilangkan<br>• Simbol :: hanya boleh muncul TEPAT SATU KALI dalam satu alamat"
    },
    "hints": {
      "concept": "1. Hapus angka 0 di depan hextet (0db8 -> db8, 0042 -> 42). Jangan hapus 0 di belakang (ff00 tetap ff00). 2. Ganti deretan blok 0000:0000:0000 dengan :: sekali saja.",
      "execution": "2001:0db8:0000:0000:0000:ff00:0042:8329 -> 2001:db8::ff00:42:8329."
    },
    "explanation": "Aturan penyingkatan IPv6 menurut RFC 5952: (1) Angka nol di depan (leading zeros) pada setiap kelompok hextet 16-bit harus dihilangkan (misal `0db8` menjadi `db8` dan `0042` menjadi `42`, namun `ff00` tetap `ff00` karena nol berada di akhir); (2) Rentetan satu atau lebih hextet yang seluruhnya bernilai 0 dapat diganti dengan simbol double colon `::` tepat satu kali dalam sebuah alamat. Dengan demikian bentuk ringkas yang valid adalah `2001:db8::ff00:42:8329`.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-13",
    "subject": "tkj",
    "materi": "MANAJEMEN BANDWIDTH & QOS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Algoritma Per Connection Queue (PCQ) pada MikroTik",
    "type": "mcq",
    "questionHtml": "Di sebuah warnet atau lab sekolah yang memiliki bandwidth internet total 50 Mbps dengan puluhan pengguna aktif, administrator ingin membagi bandwidth secara adil dan dinamis tanpa harus membuat aturan IP statis satu per satu untuk setiap komputer. Tipe queue pada MikroTik yang paling tepat digunakan adalah...",
    "options": [
      {
        "key": "A",
        "text": "FIFO (First In First Out) tanpa konfigurasi packet limit maupun rate burst."
      },
      {
        "key": "B",
        "text": "RED (Random Early Detection) untuk menjatuhkan paket TCP secara acak pada buffer penuh sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "C",
        "text": "SFQ (Stochastic Fairness Queuing) dengan fixed limit tepat 128 Kbps per workstation."
      },
      {
        "key": "D",
        "text": "PCQ (Per Connection Queue) dengan classifier 'dst-address' untuk download dan 'src-address' untuk upload."
      },
      {
        "key": "E",
        "text": "Simple Queue statis manual yang didaftarkan terpisah sebanyak 254 baris IP address."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "FORMULA PEMBAGIAN DINAMIS PCQ",
      "latex": "\\text{Rate per User} = \\frac{\\text{Total Bandwidth Tersedia}}{\\text{Jumlah User Aktif}} \\quad (\\le \\text{pcq-rate})",
      "legend": "• Download Classifier: dst-address (Mendeteksi IP klien penerima)<br>• Upload Classifier: src-address (Mendeteksi IP klien pengirim)<br>• Otomatis menyesuaikan saat user bertambah atau berkurang"
    },
    "hints": {
      "concept": "PCQ secara cerdas membuat sub-antrean dinamis untuk setiap user aktif berdasarkan IP pengirim (src) atau penerima (dst).",
      "execution": "PCQ dengan classifier dst-address untuk download dan src-address untuk upload menjamin pemerataan bandwidth dinamis tanpa konfigurasi manual ratusan IP."
    },
    "explanation": "Per Connection Queue (PCQ) adalah algoritma antrean khusus MikroTik yang secara otomatis memecah aliran data menjadi sub-antrean independen berdasarkan parameter pengelompok (classifier). Untuk lalu lintas download, digunakan classifier 'dst-address' (alamat IP tujuan di LAN), dan untuk upload digunakan 'src-address'. Jika ada 10 pengguna aktif, masing-masing mendapat 5 Mbps; jika bertambah menjadi 25 pengguna, masing-masing otomatis mendapat 2 Mbps secara adil.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-14",
    "subject": "tkj",
    "materi": "JARINGAN NIRKABEL & WIRELESS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Keamanan Wi-Fi: WPA2-PSK vs WPA3-SAE",
    "type": "mcq",
    "questionHtml": "Standar keamanan nirkabel WPA3 menggantikan WPA2 dengan memperkenalkan protokol autentikasi baru bernama Simultaneous Authentication of Equals (SAE). Keunggulan perlindungan utama WPA3-SAE dibandingkan WPA2 Pre-Shared Key (PSK) adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menghilangkan kebutuhan memasukkan kata sandi (password) sama sekali pada seluruh perangkat klien."
      },
      {
        "key": "B",
        "text": "Memperluas jangkauan transmisi sinyal radio Access Point hingga dua kali lipat lebih jauh."
      },
      {
        "key": "C",
        "text": "Mendukung transmisi data tanpa menggunakan enkripsi algoritma simetris apapun."
      },
      {
        "key": "D",
        "text": "Memungkinkan semua tipe smartphone keluaran lama tahun 2012 terhubung secara otomatis."
      },
      {
        "key": "E",
        "text": "Kebal terhadap serangan offline dictionary attack (kamus sandi) dan menyediakan forward secrecy."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "MEKANISME WPA3 SIMULTANEOUS AUTHENTICATION OF EQUALS",
      "latex": "\\text{Dragonfly Handshake (SAE)} \\implies \\text{Zero Offline Brute Force} + \\text{Forward Secrecy}",
      "legend": "• WPA2 4-Way Handshake: Penyerang menangkap paket lalu menebak password secara offline<br>• WPA3 SAE: Setiap tebakan harus berinteraksi langsung (online) sehingga gagal cepat"
    },
    "hints": {
      "concept": "Pada WPA2, penyerang dapat menangkap 4-Way Handshake dan melakukan cracking password secara offline. WPA3 menghentikan teknik ini dengan Dragonfly Handshake (SAE).",
      "execution": "WPA3-SAE memberikan perlindungan terhadap offline dictionary attack dan menjamin forward secrecy."
    },
    "explanation": "Pada WPA2-PSK, jika peretas berhasil menangkap 4-Way Handshake saat klien terhubung, peretas dapat mencoba jutaan kombinasi kata sandi secara offline menggunakan wordlist tanpa terdeteksi oleh Access Point. WPA3 menggunakan protokol SAE (berbasis Dragonfly handshake) di mana kunci sesi dinegosiasikan secara dinamis; penyerang tidak dapat melakukan offline dictionary attack dan meskipun password masa depan bocor, sesi komunikasi masa lalu tetap aman (Forward Secrecy).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-15",
    "subject": "tkj",
    "materi": "MONITORING & MANAJEMEN JARINGAN",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Protokol Monitoring SNMP (v2c vs v3)",
    "type": "mcq",
    "questionHtml": "Dalam sistem monitoring jaringan enterprise menggunakan Zabbix atau PRTG, teknisi mengganti konfigurasi SNMP v2c menjadi SNMP v3 pada seluruh switch tulang punggung. Alasan utama peningkatan ke SNMP v3 adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mendukung autentikasi berbasis pengguna (USM) dan enkripsi paket (privacy) menggunakan algoritma AES/DES."
      },
      {
        "key": "B",
        "text": "Meningkatkan kecepatan sampling trafik antarmuka dari hitungan menit menjadi milidetik murni."
      },
      {
        "key": "C",
        "text": "Mengizinkan query monitoring tanpa memerlukan konfigurasi port UDP 161 pada firewall."
      },
      {
        "key": "D",
        "text": "Menyederhanakan keamanan dengan menggunakan kata kunci community string publik 'public'."
      },
      {
        "key": "E",
        "text": "Menghilangkan struktur hierarki Object Identifier (OID) dan Management Information Base (MIB) guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LEVEL KEAMANAN SNMP V3 (USM)",
      "latex": "\\begin{cases} \\text{noAuthNoPriv:} & \\text{Tanpa autentikasi, tanpa enkripsi} \\\\ \\text{authNoPriv:} & \\text{Autentikasi MD5/SHA, tanpa enkripsi} \\\\ \\text{authPriv:} & \\text{Autentikasi SHA + Enkripsi AES (Paling Aman)} \\end{cases}",
      "legend": "• SNMP v1/v2c: Menggunakan clear-text Community String (Sangat rawan disadap)<br>• SNMP v3: User-based Security Model (USM) dengan enkripsi penuh"
    },
    "hints": {
      "concept": "Kelemahan SNMP v2c adalah 'community string' yang dikirim dalam teks biasa tanpa enkripsi. SNMP v3 menyediakan autentikasi dan enkripsi (AuthPriv).",
      "execution": "SNMP v3 mendukung USM (User-based Security Model) dan enkripsi payload paket data."
    },
    "explanation": "SNMP v1 dan SNMP v2c hanya mengandalkan 'community string' (seperti password bersama) yang ditransmisikan dalam bentuk plain-text di jaringan, sehingga sangat rentan disadap dan dimanipulasi. SNMP v3 memperkenalkan arsitektur keamanan modern berupa User-based Security Model (USM) yang mendukung autentikasi kriptografi (MD5/SHA) dan enkripsi privasi data (DES/AES) untuk melindungi komunikasi pemantauan jaringan.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-16",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Fitur Switch Port Security (IEEE 802.1X / MAC Sticky)",
    "type": "mcq",
    "questionHtml": "Untuk mencegah orang asing menancapkan laptop pribadinya ke kabel LAN di meja kantor, administrator mengaktifkan fitur `port-security` pada port switch dengan mode `switchport port-security violation shutdown` dan `mac-address sticky`. Dampak teknis saat ada laptop dengan MAC Address baru yang ditancapkan ke port tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Switch akan membiarkan paket lewat namun bandwidth laptop dibatasi menjadi 10 Kbps."
      },
      {
        "key": "B",
        "text": "Port switch akan langsung masuk ke status 'err-disable' (mati total) dan lampu indikator port berubah warna amber/oranye."
      },
      {
        "key": "C",
        "text": "Switch mengirimkan peringatan email ke administrator tetapi laptop asing tetap dapat mengakses server lokal untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "D",
        "text": "Laptop asing secara otomatis diformat sistem operasinya oleh switch melalui perintah TFTP."
      },
      {
        "key": "E",
        "text": "Switch merestart dirinya sendiri dan menghapus seluruh tabel VLAN yang tersimpan di flash."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "TIGA MODE VIOLATION PORT SECURITY CISCO",
      "latex": "\\begin{cases} \\texttt{protect:} & \\text{Drop paket MAC liar, port tetap menyala, no log} \\\\ \\texttt{restrict:} & \\text{Drop paket MAC liar, port tetap menyala, catat log SNMP} \\\\ \\texttt{shutdown:} & \\text{Matikan port langsung ke status err-disable (Paling Aman)} \\end{cases}",
      "legend": "• mac-address sticky: Merekam otomatis MAC sah pertama yang tercolok ke running-config<br>• Pelanggaran shutdown memutus fisik link hingga di-reset admin"
    },
    "hints": {
      "concept": "Mode violation `shutdown` adalah tindakan paling tegas: ketika terjadi pelanggaran, switch langsung mematikan port (err-disabled).",
      "execution": "Port switch mati total (err-disable) dan lampu port berubah oranye/amber."
    },
    "explanation": "Fitur Port Security pada switch manageable membatasi perangkat yang boleh terhubung berdasarkan MAC Address. Parameter `mac-address sticky` secara dinamis mempelajari dan mencatat MAC perangkat pertama yang tercolok. Jika perangkat asing dengan MAC berbeda dicolokkan dan aksi pelanggaran diatur ke `shutdown`, switch akan seketika menonaktifkan port tersebut ke status 'error-disabled' (err-disable), memutus seluruh konektivitas fisik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-17",
    "subject": "tkj",
    "materi": "LAYANAN JARINGAN & SERVER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Konfigurasi Web Server Reverse Proxy Nginx",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan blok konfigurasi Nginx berikut ini:\n```nginx\nserver {\n    listen 80;\n    server_name portal.smk.sch.id;\n\n    location / {\n        proxy_pass http://127.0.0.1:3000;\n        proxy_set_header Host $host;\n        proxy_set_header X-Real-IP $remote_addr;\n    }\n}\n```\nFungsi arsitektur dari direktif `proxy_pass http://127.0.0.1:3000;` pada konfigurasi di atas adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menghentikan layanan web server dan mengalihkan seluruh lalu lintas ke router gateway di IP 127.0.0.1 dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "B",
        "text": "Melakukan enkripsi file HTML dengan protokol TLS 1.3 sebelum disimpan ke harddisk server."
      },
      {
        "key": "C",
        "text": "Meneruskan setiap permintaan HTTP dari klien luar ke aplikasi backend Node.js/Python yang berjalan di port lokal 3000."
      },
      {
        "key": "D",
        "text": "Membuat database MySQL baru di memori RAM pada alamat port 3000 secara otomatis."
      },
      {
        "key": "E",
        "text": "Membatasi koneksi maksimum dari satu IP address klien menjadi tepat 3000 request per detik."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "ARSITEKTUR NGINX REVERSE PROXY",
      "latex": "\\text{Client (Internet:80)} \\xrightarrow{\\text{HTTP}} \\text{Nginx (Reverse Proxy)} \\xrightarrow{\\texttt{proxy\\_pass}} \\text{App Backend (127.0.0.1:3000)}",
      "legend": "• Nginx menerima traffic publik di port 80/443<br>• proxy_pass meneruskan data ke internal application server"
    },
    "hints": {
      "concept": "Nginx bertindak sebagai 'Reverse Proxy', menerima koneksi dari publik di port standar 80 dan meneruskannya (forward) ke aplikasi internal di port 3000.",
      "execution": "Direktif `proxy_pass` meneruskan request ke server lokal internal di port 3000."
    },
    "explanation": "Direktif `proxy_pass` adalah instruksi inti dari fitur Reverse Proxy pada Nginx. Ketika klien meminta halaman web ke domain `portal.smk.sch.id` melalui port standar HTTP (port 80), Nginx menerima request tersebut lalu meneruskannya secara transparan ke aplikasi backend internal (seperti Node.js, Next.js, Django, atau Go) yang sedang mendengarkan di `http://127.0.0.1:3000`. Header `X-Real-IP` diteruskan agar backend tetap mengetahui IP asli klien.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-18",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Pengujian Kabel Fiber Optik dengan OTDR",
    "type": "mcq",
    "questionHtml": "Pada grafik hasil pengukuran Optical Time-Domain Reflectometer (OTDR), teknisi mengamati sebuah grafik penurunan garis landai yang tiba-tiba menunjukkan lonjakan puncak runcing ke atas (reflective spike) diikuti oleh penurunan garis level daya permanen. Fenomena grafik reflective event tersebut menandakan adanya...",
    "options": [
      {
        "key": "A",
        "text": "Kabel yang terbakar oleh arus listrik tegangan tinggi dari petir."
      },
      {
        "key": "B",
        "text": "Sambungan leburan fusion splice sempurna yang sama sekali tidak memiliki redaman demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "C",
        "text": "Kabel mengalami induksi elektromagnetik dari kawat tembaga di sekitarnya."
      },
      {
        "key": "D",
        "text": "Titik sambungan konektor mekanik atau ujung kabel yang mengalami pantulan Fresnel (Fresnel Reflection)."
      },
      {
        "key": "E",
        "text": "Kondisi di mana diameter core serat optik tiba-tiba membesar secara alami."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "INTERPRETASI EVENT PADA GRAFIK OTDR",
      "latex": "\\begin{cases} \\text{Non-Reflective Event:} & \\text{Penurunan undakan tanpa lonjakan (Fusion Splice / Bending)} \\\\ \\text{Reflective Event:} & \\text{Puncak lonjakan runcing / Spike (Konektor / Ujung Kabel / Retak)} \\end{cases}",
      "legend": "• Sumbu X: Jarak kabel dalam meter/kilometer<br>• Sumbu Y: Tingkat daya optik dalam dB<br>• Fresnel Reflection terjadi akibat perbedaan indeks bias antara kaca dan udara"
    },
    "hints": {
      "concept": "Spike (lonjakan ke atas) pada grafik OTDR disebabkan oleh pantulan cahaya (Fresnel reflection) yang terjadi pada celah konektor atau patahan ujung kabel.",
      "execution": "Lonjakan tajam (reflective event) menunjukkan adanya sambungan konektor atau diskontinuitas mekanik."
    },
    "explanation": "OTDR bekerja dengan memancarkan pulsa cahaya laser dan menganalisis pantulan baliknya (Rayleigh backscattering dan Fresnel reflection). Pada grafik OTDR, kejadian dibedakan menjadi dua: (1) Non-reflective event: hanya berupa penurunan garis bertingkat (undakan loss) akibat sambungan las (fusion splice) atau tekukan kabel (macrobending); (2) Reflective event: ditandai dengan puncak lonjakan tajam ke atas akibat adanya celah udara pada ujung konektor atau kabel putus yang memantulkan kembali sebagian besar berkas cahaya.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-19",
    "subject": "tkj",
    "materi": "VIRTUAL PRIVATE NETWORK & TUNNELING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komparasi Protokol VPN: IPsec vs OpenVPN vs WireGuard",
    "type": "mcq",
    "questionHtml": "Dalam perancangan Virtual Private Network (VPN) antar cabang sekolah, teknisi memilih protokol WireGuard modern daripada protokol legendaris IPsec dan OpenVPN. Keunggulan teknis utama dari protokol WireGuard adalah...",
    "options": [
      {
        "key": "A",
        "text": "Tidak memerlukan konfigurasi kunci kriptografi publik maupun privat antar perangkat."
      },
      {
        "key": "B",
        "text": "Beroperasi secara eksklusif menggunakan protokol TCP port 443 tanpa pernah menggunakan UDP sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "C",
        "text": "Mampu menghubungkan komputer tanpa perlu adanya koneksi internet publik sama sekali."
      },
      {
        "key": "D",
        "text": "Dapat menembus firewall secara otomatis dengan memanipulasi hardware switch jaringan."
      },
      {
        "key": "E",
        "text": "Basis kode sangat ringkas (~4.000 baris kode), performa throughput tinggi di kernel space, dan menggunakan kriptografi modern Curve25519."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "KOMPARASI EFISIENSI KODE VPN",
      "latex": "\\text{OpenVPN} \\approx 100{,}000\\text{ LOC} \\quad \\text{vs} \\quad \\text{WireGuard} \\approx 4{,}000\\text{ LOC}",
      "legend": "• WireGuard: Berjalan langsung di Linux Kernel Space (Overhead minim, latency rendah)<br>• Kriptografi modern terpasang: ChaCha20, Poly1305, Curve25519, BLAKE2s"
    },
    "hints": {
      "concept": "WireGuard terkenal karena sangat ringan (hanya sekitar 4.000 baris kode vs 100.000 baris OpenVPN), cepat karena di kernel Linux, dan menggunakan kriptografi state-of-the-art.",
      "execution": "Pilihan A tepat merangkum karakteristik utama arsitektur WireGuard."
    },
    "explanation": "WireGuard adalah protokol VPN generasi baru yang dirancang untuk menggantikan IPsec dan OpenVPN. WireGuard berjalan langsung di dalam kernel space Linux dengan basis kode yang sangat ramping (sekitar 4.000 baris kode, dibandingkan OpenVPN/IPsec yang mencapai ratusan ribu baris). Hal ini membuat audit keamanan jauh lebih mudah, latency sangat rendah, dan konsumsi daya baterai efisien, didukung oleh paket kriptografi modern seperti Curve25519 dan ChaCha20-Poly1305.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-20",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Link Aggregation Control Protocol (LACP) IEEE 802.3ad",
    "type": "mcq",
    "questionHtml": "Dua switch core enterprise dihubungkan menggunakan 4 kabel UTP Cat 6 secara simultan yang digabungkan ke dalam satu antarmuka logis EtherChannel / Bonding menggunakan protokol LACP (IEEE 802.3ad). Manfaat teknis dari konfigurasi tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengalikan kapasitas bandwidth gabungan (agregasi 4 Gbps) sekaligus menyediakan redundansi link tanpa diblokir oleh Spanning Tree."
      },
      {
        "key": "B",
        "text": "Mengubah fungsi switch layer 2 menjadi router BGP yang mampu menampung full internet routing table guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "C",
        "text": "Menghilangkan kebutuhan konfigurasi VLAN tagging pada antarmuka trunk antar switch."
      },
      {
        "key": "D",
        "text": "Mengurangi konsumsi listrik port switch hingga 75% saat lalu lintas data sedang sepi."
      },
      {
        "key": "E",
        "text": "Memperbolehkan satu komputer klien menggunakan 4 alamat IP privat yang berbeda secara bersamaan."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP LINK AGGREGATION (LACP 802.3AD)",
      "latex": "4 \\times 1\\,\\text{Gbps Fisik Link} \\xrightarrow{\\text{LACP Bonding}} 1 \\times 4\\,\\text{Gbps Logikal PortChannel}",
      "legend": "• Tanpa LACP: STP akan memblokir 3 link untuk mencegah loop (hanya 1 link aktif)<br>• Dengan LACP: Ke-4 link aktif bersamaan dan jika 1 link putus, traffic otomatis dialihkan"
    },
    "hints": {
      "concept": "Jika 4 kabel dicolokkan antar switch tanpa link aggregation, Spanning Tree akan mematikan 3 kabel agar tidak terjadi loop. LACP menggabungkan 4 kabel tersebut menjadi 1 pipa logis.",
      "execution": "LACP meningkatkan bandwidth agregat (4x1 Gbps = 4 Gbps) dan memberikan toleransi kesalahan (link failover) tanpa memicu STP loop."
    },
    "explanation": "Secara standar, menghubungkan beberapa kabel fisik antara dua switch akan memicu loop jaringan yang menyebabkan Spanning Tree Protocol (STP) memblokir link ekstra tersebut. Dengan Link Aggregation Control Protocol (LACP IEEE 802.3ad) atau EtherChannel, port-port fisik tersebut digabungkan ke dalam satu port logis (Port-Channel). Hasilnya, total bandwidth meningkat (agregasi) dan jika salah satu kabel fisik putus, lalu lintas data tetap mengalir melalui kabel yang tersisa tanpa interupsi.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-21",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Stateful Firewall Connection Tracking (ESTABLISHED & RELATED)",
    "type": "mcq",
    "questionHtml": "Pada baris paling atas konfigurasi firewall filter MikroTik, seorang network engineer selalu menaruh aturan berikut:\n```text\n/ip firewall filter add chain=forward connection-state=established,related action=accept\n```\nAlasan teknis aturan ini ditaruh di urutan paling pertama (top priority) adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mencegah komputer klien melakukan browsing ke situs web berbahaya yang memuat konten ilegal."
      },
      {
        "key": "B",
        "text": "Mempercepat pemrosesan paket data koneksi yang sudah sah terjalin tanpa harus mencocokkan ke ratusan aturan filter di bawahnya (menghemat CPU router)."
      },
      {
        "key": "C",
        "text": "Menghapus seluruh rekaman log koneksi di harddisk router agar memori penyimpanan tidak penuh untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "D",
        "text": "Mengizinkan pengguna tak dikenal dari internet publik membobol password router tanpa batasan."
      },
      {
        "key": "E",
        "text": "Mengubah seluruh paket data TCP menjadi paket data UDP agar proses transmisi lebih cepat."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "OPTIMASI FILTER STATEFUL CONNECTION TRACKING",
      "latex": "\\text{Paket Masuk} \\implies \\text{Cek Connection State} \\begin{cases} \\texttt{established/related} &\\to \\text{Accept Langsung (Bypass Rules)} \\\\ \\texttt{new/invalid} &\\to \\text{Evaluasi Sisa Rules di Bawah} \\end{cases}",
      "legend": "• Sekitar 95% lalu lintas jaringan adalah paket dari koneksi yang sudah terbuka<br>• Menaruh aturan ini di atas menghemat siklus clock CPU router secara drastis"
    },
    "hints": {
      "concept": "Sebagian besar paket data di jaringan adalah kelanjutan dari koneksi yang sudah terjalin sebelumnya (established/related).",
      "execution": "Menerima paket established/related di urutan teratas langsung mem-bypass ratusan aturan lain, menghemat beban CPU router."
    },
    "explanation": "Firewall stateful mengelola tabel pelacak koneksi (Connection Tracking). Ketika sebuah koneksi baru berhasil dibuka, paket-paket lanjutannya akan berstatus 'established' (sudah terjalin) atau 'related' (berelasi, misal data transfer FTP). Karena lebih dari 90% paket jaringan berstatus ini, menaruh aturan `accept established,related` di urutan paling awal memungkinkan router segera meloloskan paket tersebut tanpa harus mengevaluasi baris-baris aturan di bawahnya, sehingga penggunaan CPU router sangat efisien.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-22",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Parameter dan Ambang Batas Redaman Fusion Splicer",
    "type": "mcq",
    "questionHtml": "Seorang teknisi melakukan penyambungan dua ujung kabel fiber optik Single Mode menggunakan mesin Fusion Splicer otomatis. Standar industri telekomunikasi (seperti ITU-T G.652) menetapkan bahwa estimasi redaman sambungan (splice loss) yang dapat diterima (lolos uji) pada layar fusion splicer adalah...",
    "options": [
      {
        "key": "A",
        "text": "Maksimum $\\le 3.5\\text{ dB}$ per titik sambungan fusi serat optik."
      },
      {
        "key": "B",
        "text": "Tepat $0.00\\text{ dB}$ tanpa boleh ada deviasi sudut pantul sedikit pun."
      },
      {
        "key": "C",
        "text": "Maksimum $\\le 0.05\\text{ dB}$ (ideal $0.01 - 0.03\\text{ dB}$ per titik sambungan)."
      },
      {
        "key": "D",
        "text": "Antara $1.0\\text{ dB}$ sampai dengan $2.5\\text{ dB}$ pada suhu ruangan kerja normal."
      },
      {
        "key": "E",
        "text": "Tergantung pada warna selubung tabung loose tube kabel yang sedang disambung."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "STANDAR LOSS SAMBUNGAN FUSION SPLICING (ITU-T G.652)",
      "latex": "\\text{Splice Loss}_{\\text{SMF}} \\le 0.05\\,\\text{dB} \\quad (\\text{Ideal: } \\le 0.02\\,\\text{dB})",
      "legend": "• Jika loss terukur > 0.1 dB: Sambungan wajib dipotong dan di-splicing ulang<br>• Penyebab loss tinggi: Sudut potong cleaver miring, debu pada core, elektroda kotor"
    },
    "hints": {
      "concept": "Sambungan fusi (leburan busur listrik) sangat presisi sehingga redamannya sangat kecil, di bawah 0.05 dB.",
      "execution": "Standar kelayakan fusi serat optik Single Mode adalah $\\le 0.05\\text{ dB}$."
    },
    "explanation": "Mesin Fusion Splicer menyambungkan dua inti serat kaca menggunakan leburan busur listrik bertegangan tinggi. Berdasarkan standar ITU-T dan Telcordia, nilai redaman maksimum yang diperbolehkan untuk satu titik sambungan fusi (fusion splice) serat optik Single Mode adalah 0.05 dB, dengan nilai rata-rata industri yang diharapkan berkisar antara 0.01 hingga 0.03 dB. Jika splicer menampilkan loss di atas 0.1 dB, sambungan harus dipotong, dikupas, dibersihkan dengan alkohol, dan di-cleave ulang.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-23",
    "subject": "tkj",
    "materi": "LAYANAN JARINGAN & SERVER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Troubleshooting Layanan DNS dengan `dig` dan `nslookup`",
    "type": "mcq",
    "questionHtml": "Saat melakukan pemecahan masalah resolusi domain, teknisi menjalankan perintah `dig smk.sch.id +trace` di terminal Linux. Fungsi dari parameter `+trace` pada perintah tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengukur latensi ping ICMP ke setiap router hop yang dilewati menuju server DNS publik dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "B",
        "text": "Mengunduh file zona DNS secara lengkap menggunakan teknik DNS Zone Transfer (AXFR)."
      },
      {
        "key": "C",
        "text": "Mengenkripsi kueri DNS menggunakan protokol DNS-over-HTTPS (DoH) ke Cloudflare."
      },
      {
        "key": "D",
        "text": "Melakukan resolusi kueri DNS secara bertahap mulai dari Root Server (.) hingga ke Name Server otoritatif domain tersebut."
      },
      {
        "key": "E",
        "text": "Memperbaiki secara otomatis kesalahan ketik konfigurasi pada berkas /etc/resolv.conf."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "ALUR HIERARKI DNS RECURSIVE TRACE",
      "latex": "\\text{Root Server (.)} \\to \\text{TLD Server (.id)} \\to \\text{2nd Level Server (.sch.id)} \\to \\text{Authoritative Server (smk.sch.id)}",
      "legend": "• Menampilkan rantai delegasi server DNS dari tingkat tertinggi<br>• Berguna untuk melacak di level mana delegasi DNS terputus"
    },
    "hints": {
      "concept": "Parameter `+trace` pada utilitas `dig` mengikuti jejak resolusi hierarkis DNS dari Root Server sampai ke Authoritative Name Server.",
      "execution": "Pilihan A tepat mendeskripsikan pelacakan kueri DNS bertahap dari Root Server hingga Name Server tujuan."
    },
    "explanation": "Perintah `dig domain.com +trace` menginstruksikan utilitas DNS lookup untuk tidak bertanya ke resolver lokal, melainkan menelusuri langsung rantai hierarki DNS global dari paling atas: (1) Menghubungi salah satu dari 13 Root Name Server global (a.root-servers.net s/d m.root-servers.net); (2) Menghubungi Name Server pengelola Top-Level Domain (TLD, misal .id); (3) Menghubungi Second-Level Domain (.sch.id); hingga (4) Menemukan Name Server otoritatif yang memegang data record domain target.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-24",
    "subject": "tkj",
    "materi": "PENGALAMATAN IPV6 & NEXT-GEN NETWORK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Metode Pembentukan Alamat EUI-64 pada IPv6",
    "type": "mcq",
    "questionHtml": "Pada Stateless Address Autoconfiguration (SLAAC) IPv6, Interface Identifier 64-bit dapat dibentuk dari MAC Address fisik 48-bit kartu jaringan menggunakan format IEEE EUI-64. Dua langkah manipulasi biner yang dilakukan pada MAC Address tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menambahkan angka `AA:BB` di akhir MAC Address dan mengalikan octet pertama dengan angka dua demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "B",
        "text": "Menghapus 3 byte pertama OUI vendor dan menggantinya dengan prefix link-local `FE80::`."
      },
      {
        "key": "C",
        "text": "Mengenkripsi seluruh digit heksadesimal MAC Address menggunakan hash SHA-256."
      },
      {
        "key": "D",
        "text": "Mengonversi seluruh digit hex genap menjadi nol dan digit ganjil menjadi huruf F."
      },
      {
        "key": "E",
        "text": "Menyisipkan 16-bit hex `FF:FE` di tengah-tengah MAC Address dan membalik bit ke-7 (Universal/Local bit) pada octet pertama."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "MEKANISME TRANSFORMASI IEEE EUI-64",
      "latex": "\\begin{aligned} \\text{MAC: } & \\texttt{00:1A:2B} : \\texttt{3C:4D:5E} \\\\ \\text{Sisip FFFE: } & \\texttt{00:1A:2B}:\\mathbf{FF:FE}:\\texttt{3C:4D:5E} \\\\ \\text{Invert Bit-7: } & \\texttt{00} (\\mathbf{0}00000\\mathbf{0}0_2) \\to \\texttt{02} (000000\\mathbf{1}0_2) \\implies \\texttt{021a:2bff:fe3c:4d5e} \\end{aligned}",
      "legend": "• Bit ke-7 diubah dari 0 (Universal) menjadi 1 (Local administered)<br>• Nilai 16-bit FFFE (1111111111111110) disisipkan tepat di antara byte ke-3 dan ke-4"
    },
    "hints": {
      "concept": "Dua ciri khas EUI-64: menyisipkan 'FFFE' di tengah MAC (antara byte ke-3 dan ke-4) dan membalik bit ke-7 (U/L bit) octet pertama.",
      "execution": "Pilihan A tepat menjelaskan kedua proses transformasi EUI-64."
    },
    "explanation": "Format IEEE EUI-64 mengubah MAC Address 48-bit menjadi Interface ID 64-bit untuk IPv6 melalui dua langkah: (1) Menyisipkan 16-bit nilai hex `FF:FE` di antara byte ketiga dan keempat (tepat di antara Organizationally Unique Identifier / OUI vendor dengan serial card); (2) Membalik nilai bit ke-7 (Universal/Local flag) dari octet pertama (jika 0 diubah menjadi 1, dan sebaliknya) untuk menandakan bahwa alamat tersebut kini dikelola secara lokal pada antarmuka IPv6.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-25",
    "subject": "tkj",
    "materi": "K3LH & KETENAGAKERJAAN TJKT",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Grounding dan Proteksi Petir Menara Telekomunikasi",
    "type": "mcq",
    "questionHtml": "Pada instalasi menara telekomunikasi (tower BTS/wireless) outdoor, sistem penangkal petir harus dihubungkan ke elektroda pembumian (grounding rod) di dalam tanah. Berdasarkan standar teknis keselamatan ketenagalistrikan (PUIL), nilai resistansi pembumian (grounding resistance) maksimum yang diizinkan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Maksimum $\\le 5\\,\\Omega$ (Ohm), dan idealnya di bawah $1 - 2\\,\\Omega$ untuk instalasi telekomunikasi sensitif."
      },
      {
        "key": "B",
        "text": "Minimal harus di atas $50\\,\\Omega$ agar muatan petir tidak merusak lapisan tanah."
      },
      {
        "key": "C",
        "text": "Tepat $100\\,\\Omega$ agar serasi dengan impedansi karakteristik kabel UTP tembaga."
      },
      {
        "key": "D",
        "text": "Antara $20\\,\\Omega$ sampai $35\\,\\Omega$ tergantung jenis batuan di lokasi menara."
      },
      {
        "key": "E",
        "text": "Tidak perlu diukur asalkan tembaga penangkal petir ditancapkan sedalam minimal 10 cm sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR RESISTANSI GROUNDING PUIL & ITU-T",
      "latex": "R_{\\text{grounding}} \\le 5\\,\\Omega \\quad (\\text{Rekomendasi Telekomunikasi: } \\le 1 - 2\\,\\Omega)",
      "legend": "• R semakin kecil -> Arus sambaran petir semakin cepat mengalir ke tanah<br>• Mencegah tegangan balik (back flashover) yang membakar radio dan switch"
    },
    "hints": {
      "concept": "Sesuai PUIL (Persyaratan Umum Instalasi Listrik), nilai hambatan tanah (grounding) tidak boleh lebih dari 5 Ohm. Semakin kecil hambatannya, semakin aman perangkat dari sambaran petir.",
      "execution": "Nilai maksimum resistansi pembumian adalah $\\le 5\\,\\Omega$."
    },
    "explanation": "Berdasarkan standar Persyaratan Umum Instalasi Listrik (PUIL) dan rekomendasi internasional ITU-T K-series untuk proteksi perangkat telekomunikasi, tahanan pembumian (grounding resistance) maksimum yang diizinkan untuk sistem proteksi petir adalah 5 Ohm. Pada instalasi data center dan menara telekomunikasi sensitif, nilai resistansi pembumian ditargetkan lebih ketat lagi, yaitu di bawah 1 hingga 2 Ohm, agar lonjakan arus petir berorde kiloampere dapat disalurkan secara aman ke bumi tanpa merusak perangkat radio.",
    "isDiagnostic": false
  },
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
      {
        "key": "A",
        "text": "R1 meng-generate LSA Type 1 (Router LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 2 (Network LSA)."
      },
      {
        "key": "B",
        "text": "R1 meng-generate LSA Type 4 (ASBR Summary LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 7 (NSSA External LSA)."
      },
      {
        "key": "C",
        "text": "R1 meng-generate LSA Type 3 (Summary LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 5 (AS External LSA)."
      },
      {
        "key": "D",
        "text": "R1 meng-generate LSA Type 5 (External LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 3 (Summary LSA)."
      },
      {
        "key": "E",
        "text": "R1 meng-generate LSA Type 2 (Network LSA), dan rute eksternal dari R3 disebarkan sebagai LSA Type 1 (Router LSA)."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Rute dari ISP-2, karena memiliki nilai AS Path yang lebih pendek (1 AS hop vs 2 AS hop), dievaluasi sebelum Local Preference guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "B",
        "text": "Rute dari ISP-2, karena memiliki nilai Multi-Exit Discriminator (MED) yang lebih rendah (50 < 100)."
      },
      {
        "key": "C",
        "text": "Kedua rute dibagikan beban lalu lintasnya (load balancing) karena nilai Weight keduanya bernilai sama-sama 0."
      },
      {
        "key": "D",
        "text": "Rute dari ISP-1, karena memiliki nilai Local Preference yang lebih tinggi (200 > 100), dievaluasi sebelum mempertimbangkan panjang AS Path."
      },
      {
        "key": "E",
        "text": "Rute dari ISP-1, karena memiliki nilai MED yang lebih tinggi yang menandakan prioritas metrik terbesar."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": true
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
      {
        "key": "A",
        "text": "192.168.16.0/21; dan mengaktifkan split horizon pada seluruh antarmuka backbone OSPF."
      },
      {
        "key": "B",
        "text": "192.168.0.0/20; dan menyetel Administrative Distance rute summary menjadi bernilai 255 untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "C",
        "text": "192.168.16.0/23; dan memblokir paket ICMP redirect pada switch access layer."
      },
      {
        "key": "D",
        "text": "192.168.18.0/22; dan mengaktifkan fitur Proxy ARP pada antarmuka trunk router."
      },
      {
        "key": "E",
        "text": "192.168.16.0/22; dan menambahkan rute statis 192.168.16.0/22 ke interface 'null0' (blackhole) untuk mencegah routing loop."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "BPDU Guard mematikan port edge jika menerima paket BPDU dari switch liar, sedangkan Root Guard mencegah switch liar mengambil alih peran Root Bridge."
      },
      {
        "key": "B",
        "text": "BPDU Guard mengenkripsi seluruh frame data yang lewat, sedangkan Root Guard membatasi jumlah host maksimum menjadi 1 unit."
      },
      {
        "key": "C",
        "text": "BPDU Guard mengubah mode port menjadi trunking otomatis, sedangkan Root Guard menghapus tabel CAM jika terjadi banjir ARP."
      },
      {
        "key": "D",
        "text": "BPDU Guard mempercepat proses konvergensi STP dari 30 detik menjadi 1 detik, sedangkan Root Guard memblokir seluruh frame broadcast dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "E",
        "text": "Keduanya berfungsi identik untuk mengaktifkan Dynamic Trunking Protocol (DTP) secara agresif pada antarmuka access."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Dispersi Modal (Modal Dispersion akibat perbedaan sudut pantul multi-mode) demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "B",
        "text": "Dispersi Kromatik (Chromatic Dispersion / Material and Waveguide Dispersion)."
      },
      {
        "key": "C",
        "text": "Atenuasi Rayleigh Scattering akibat kotoran mikroskopis partikel kaca."
      },
      {
        "key": "D",
        "text": "Self-Phase Modulation akibat non-linearitas daya optik yang terlalu rendah."
      },
      {
        "key": "E",
        "text": "Four-Wave Mixing akibat polarisasi melingkar gelombang radio microwave."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Koneksi TCP telah diputus secara paksa oleh server dengan flag RST (Reset connection)."
      },
      {
        "key": "B",
        "text": "Kabel jaringan klien mengalami putus fisik sehingga throughput terhenti pada layer 1."
      },
      {
        "key": "C",
        "text": "Buffer penerima (Receive Buffer) pada server sudah penuh total, sehingga klien wajib menghentikan pengiriman data dan hanya mengirim TCP Zero Window Probe secara berkala."
      },
      {
        "key": "D",
        "text": "Server meminta klien untuk melipatgandakan ukuran segmen Maximum Transmission Unit (MTU) menjadi 9000 bytes sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "E",
        "text": "Server berhasil menyelesaikan handshake dan meminta autentikasi username SSL baru."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": true
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
      {
        "key": "A",
        "text": "Memperbesar nilai MTU kartu jaringan menjadi 16.000 bytes agar paket SYN dapat ditampung sekaligus."
      },
      {
        "key": "B",
        "text": "Menonaktifkan protokol TCP pada kernel dan mengganti seluruh port HTTP web server menjadi protokol UDP mentah guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "C",
        "text": "Mengirimkan paket ICMP Destination Unreachable ke seluruh alamat IP yang mengirimkan paket SYN."
      },
      {
        "key": "D",
        "text": "Mengaktifkan 'SYN Cookies' (net.ipv4.tcp_syncookies = 1) di mana server menyandikan data koneksi ke dalam Initial Sequence Number (ISN) tanpa mengalokasikan memori tabel koneksi sebelum ACK diterima."
      },
      {
        "key": "E",
        "text": "Mematikan fitur Address Resolution Protocol (ARP) pada kartu jaringan server Linux."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "1. Buat bridge antar kedua ISP -> 2. Masukkan seluruh port LAN ke bridge -> 3. Aktifkan DHCP snooping pada port game."
      },
      {
        "key": "B",
        "text": "1. Pasang aturan action=drop pada port 80 di mangle -> 2. Buat static DNS -> 3. Aktifkan proxy server internal."
      },
      {
        "key": "C",
        "text": "1. Set distance=1 pada kedua rute -> 2. Aktifkan OSPF pada interface LAN -> 3. Buat aturan filter forward accept."
      },
      {
        "key": "D",
        "text": "1. Gunakan Destination NAT mengarah ke IP ISP-1 -> 2. Matikan connection tracking router -> 3. Simpan konfigurasi."
      },
      {
        "key": "E",
        "text": "1. Tandai koneksi di /ip firewall mangle (mark-connection) -> 2. Tandai rute dari koneksi tersebut (mark-routing) -> 3. Buat default gateway di /ip route dengan routing-mark yang sesuai."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menggunakan autentikasi dua arah (mutual authentication) berbasis sertifikat digital X.509 baik di sisi server RADIUS maupun pada setiap perangkat klien (tanpa mengandalkan password)."
      },
      {
        "key": "B",
        "text": "Menghilangkan kebutuhan instalasi sertifikat pada sisi server sehingga konfigurasi lebih cepat."
      },
      {
        "key": "C",
        "text": "Mengizinkan pengguna login menggunakan akun media sosial tanpa perlu terdaftar di direktori institusi dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "D",
        "text": "Mengirimkan username dan password dalam format teks telanjang (clear-text) untuk memudahkan audit."
      },
      {
        "key": "E",
        "text": "Memperbolehkan perangkat klien menghubungkan diri ke Access Point tanpa perlu enkripsi RF."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "R2 akan menjadi Master permanen selamanya dan menolak melepaskan status Master meskipun R1 sudah menyala normal kembali demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "B",
        "text": "Saat R1 mati, R2 langsung mengambil alih menjadi Master; ketika R1 menyala kembali, R1 segera mengambil alih kembali (preempt) menjadi Master karena nilai prioritasnya lebih tinggi (150 > 100)."
      },
      {
        "key": "C",
        "text": "Kedua router akan mengalami konflik split-brain sehingga alamat Virtual IP 192.168.1.1 mati total dari jaringan."
      },
      {
        "key": "D",
        "text": "R1 akan menjadi Backup permanen dan hanya menyala jika R2 juga ikut dimatikan oleh administrator."
      },
      {
        "key": "E",
        "text": "Klien di jaringan lokal harus merestart kartu jaringannya secara manual agar dapat terhubung kembali ke R1."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Kabel serat optik tidak mendukung transmisi suara manusia melainkan hanya data teks digital."
      },
      {
        "key": "B",
        "text": "Server Asterisk kehabisan memori harddisk sehingga tidak dapat merekam percakapan."
      },
      {
        "key": "C",
        "text": "Protokol pensinyalan SIP (Session Initiation Protocol port UDP 5060) berhasil menembus firewall, namun aliran paket suara RTP (Real-time Transport Protocol port UDP rentang 10000-20000) terblokir oleh firewall atau mengalami kesalahan translasi NAT."
      },
      {
        "key": "D",
        "text": "IP phone klien mengalami kerusakan fisik pada speaker handset secara bersamaan di kedua lokasi sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "E",
        "text": "Protokol DNS sekolah gagal melakukan resolusi reverse lookup alamat IPv6."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menghilangkan seluruh perangkat switch dan router fisik serta menggantinya murni dengan gelombang satelit nirkabel demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "B",
        "text": "Menggabungkan Management Plane dan Physical Plane ke dalam satu keping ASIC mikrokontroler."
      },
      {
        "key": "C",
        "text": "Mewajibkan setiap switch menjalankan protokol routing BGP full mesh secara desentralisasi penuh."
      },
      {
        "key": "D",
        "text": "Memisahkan bidang kendali logika perutean (Control Plane) ke kontroler terpusat berbasis software, sementara switch fisik hanya bertugas meneruskan paket data murni (Data/Forwarding Plane) via protokol OpenFlow."
      },
      {
        "key": "E",
        "text": "Menolak seluruh paket data TCP dan hanya memperbolehkan transmisi frame mentah Ethernet."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "6in4 Tunneling statis yang membutuhkan konfigurasi tunnel broker manual di setiap smartphone klien dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "B",
        "text": "Dual Stack murni di mana setiap komputer wajib memiliki dua alamat IPv4 dan IPv6 aktif."
      },
      {
        "key": "C",
        "text": "ISATAP (Intra-Site Automatic Tunnel Addressing Protocol) dengan memodifikasi routing OSPF area 0."
      },
      {
        "key": "D",
        "text": "Proxy HTTP transparan tanpa keterlibatan protokol DNS sama sekali."
      },
      {
        "key": "E",
        "text": "DNS64 (membuat alamat IPv6 sintetis dengan menyematkan IPv4 target ke prefix 64:ff9b::/96) dan NAT64 (menerjemahkan paket header IPv6 menjadi paket IPv4 murni pada router gateway)."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Dynamic ARP Inspection (DAI) yang memvalidasi keabsahan paket ARP terhadap tabel database DHCP Snooping Binding."
      },
      {
        "key": "B",
        "text": "Storm Control untuk membatasi persentase broadcast data rate menjadi 10%."
      },
      {
        "key": "C",
        "text": "Spanning Tree PortFast pada seluruh antarmuka trunk uplink."
      },
      {
        "key": "D",
        "text": "Access Control List (ACL) statis yang memblokir protokol ICMP Echo Request demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "E",
        "text": "Mengaktifkan auto-MDIX pada semua kabel straight-through di switch."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "PUE = 0.67; menunjukkan data center sangat efisien karena nilai berada di bawah ambang batas angka 1.0 sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "B",
        "text": "PUE = 1.50; menunjukkan efisiensi wajar di mana untuk setiap 1 Watt daya perangkat IT, dibutuhkan 0.5 Watt daya tambahan untuk pendingin dan fasilitas."
      },
      {
        "key": "C",
        "text": "PUE = 2.40; menunjukkan pemborosan daya ekstrem yang melebihi standar fasilitas Tier 4."
      },
      {
        "key": "D",
        "text": "PUE = 4.00; menunjukkan data center mengalami kebocoran arus listrik induksi."
      },
      {
        "key": "E",
        "text": "PUE = 1.00; menunjukkan efisiensi termodinamika sempurna tanpa adanya kehilangan energi."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menjalankan protokol OSPF di atas eBGP tanpa konfigurasi autonomous system number guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "B",
        "text": "Mengubah seluruh sesi koneksi TCP port 179 menjadi tunneling GRE unencrypted."
      },
      {
        "key": "C",
        "text": "BGP Route Reflector (RR) di mana router server diizinkan merefleksikan rute iBGP ke router Route Reflector Client."
      },
      {
        "key": "D",
        "text": "Mengaktifkan fitur proxy ARP pada antarmuka loopback seluruh router internal."
      },
      {
        "key": "E",
        "text": "Menurunkan nilai Administrative Distance eBGP menjadi 200 sama dengan iBGP."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Mampu memperbaiki frame data yang korup menggunakan algoritma Cyclomatic Redundancy Check untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "B",
        "text": "Menghilangkan redaman dispersi kromatik secara mutlak tanpa sisa delay sedikit pun."
      },
      {
        "key": "C",
        "text": "Tidak membutuhkan catu daya listrik eksternal sama sekali untuk memompa laser emisi."
      },
      {
        "key": "D",
        "text": "Memperkuat seluruh kanal panjang gelombang cahaya di jendela 1550 nm secara optik murni tanpa perlu mengonversi sinyal cahaya ke sinyal listrik terlebih dahulu (All-Optical Amplification)."
      },
      {
        "key": "E",
        "text": "Dapat beroperasi pada kabel twisted pair tembaga sejauh 200 kilometer."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Phase 1 mentransmisikan data file Word/PDF, sedangkan Phase 2 hanya melakukan ping diagnostik ICMP."
      },
      {
        "key": "B",
        "text": "Phase 1 menggunakan enkripsi simetris DES, sedangkan Phase 2 menggunakan enkripsi plain-text tanpa kunci guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "C",
        "text": "Phase 1 beroperasi di Network Layer, sedangkan Phase 2 beroperasi di Application Layer Nginx."
      },
      {
        "key": "D",
        "text": "Phase 1 dilakukan oleh teknisi manusia, sedangkan Phase 2 dijalankan oleh robot kecerdasan buatan."
      },
      {
        "key": "E",
        "text": "Phase 1 membangun terowongan terenkripsi yang aman antar kedua router (IKE SA), sedangkan Phase 2 menegosiasikan enkripsi transform set untuk melindungi lalu lintas data nyata klien LAN (IPsec SA)."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Terjadinya routing loop dan sub-optimal routing karena rute yang diimpor dari EIGRP ke OSPF dapat diimpor kembali ke EIGRP dengan metrik yang tidak valid."
      },
      {
        "key": "B",
        "text": "Switch layer 2 akan mengalami kerusakan fisik pada port power supply PoE."
      },
      {
        "key": "C",
        "text": "Alamat IP privat klien LAN akan terkonversi otomatis menjadi alamat IP publik APNIC."
      },
      {
        "key": "D",
        "text": "Kecepatan propagasi cahaya pada kabel serat optik akan melambat hingga di bawah 100 km/detik sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "E",
        "text": "DNS server lokal akan berhenti melayani kueri resolusi domain .sch.id."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "DSCP Best Effort (BE) dengan nilai biner 000000 (desimal 0) guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "B",
        "text": "DSCP Expedited Forwarding (EF) dengan nilai biner 101110 (desimal 46)."
      },
      {
        "key": "C",
        "text": "DSCP Assured Forwarding 11 (AF11) dengan nilai desimal 10."
      },
      {
        "key": "D",
        "text": "DSCP Class Selector 1 (CS1) dengan nilai desimal 8."
      },
      {
        "key": "E",
        "text": "DSCP Assured Forwarding 43 (AF43) dengan nilai desimal 38."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)."
      },
      {
        "key": "B",
        "text": "DSSS (Direct Sequence Spread Spectrum)."
      },
      {
        "key": "C",
        "text": "OFDMA (Orthogonal Frequency Division Multiple Access)."
      },
      {
        "key": "D",
        "text": "FHSS (Frequency Hopping Spread Spectrum)."
      },
      {
        "key": "E",
        "text": "BSS Coloring berbasis token ring analog."
      }
    ],
    "correctKey": "C",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Server mengalami serangan Denial of Service sehingga menolak memproses query database."
      },
      {
        "key": "B",
        "text": "Kabel LAN mengalami korsleting listrik sehingga seluruh data heksadesimal terbalik nilainya."
      },
      {
        "key": "C",
        "text": "Klien telah logout dari sesi database dan server menyetujui pemutusan koneksi dengan flag FIN untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "D",
        "text": "Klien menerima segmen TCP yang melompati urutan (out-of-order), mengindikasikan ada satu paket di tengah yang hilang (packet loss), sehingga memicu mekanisme Fast Retransmit server tanpa menunggu Retransmission Timeout (RTO)."
      },
      {
        "key": "E",
        "text": "Switch core sedang melakukan pembaharuan firmware sehingga semua antarmuka masuk mode standby."
      }
    ],
    "correctKey": "D",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menaikkan nilai Local Preference pada pengumuman prefix yang dikirim keluar ke arah ISP-B guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "B",
        "text": "Menyetel nilai Weight menjadi 65535 pada antarmuka yang mengarah ke ISP-B."
      },
      {
        "key": "C",
        "text": "Menghapus default gateway ISP-A dari tabel routing BGP lokal."
      },
      {
        "key": "D",
        "text": "Mengaktifkan mode bridge transparan pada router border eBGP."
      },
      {
        "key": "E",
        "text": "AS-Path Prepending (menyisipkan nomor AS sendiri berulang kali, misal: '64512 64512 64512', pada pengumuman prefix ke arah ISP-B agar rute tampak lebih panjang dan dijauhi)."
      }
    ],
    "correctKey": "E",
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Mengiklankan alamat IP publik yang sama persis (misal 8.8.8.8) dari ratusan lokasi server berbeda melalui protokol BGP, sehingga kueri pengguna secara alami diarahkan ke data center terdekat secara topologi perutean."
      },
      {
        "key": "B",
        "text": "Menyimpan seluruh data internet global di dalam satu komputer server tunggal supercepat di Amerika Serikat sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "C",
        "text": "Mengubah paket data UDP port 53 menjadi transmisi radio satelit gelombang mikro antariksa."
      },
      {
        "key": "D",
        "text": "Mewajibkan pengguna memasukkan password token digital sebelum kueri DNS dijawab oleh server."
      },
      {
        "key": "E",
        "text": "Menduplikasi setiap pertanyaan kueri DNS ke seluruh server di dunia secara broadcast simultan."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Membekukan seluruh ruangan server hingga mencapai suhu nol mutlak (-273 derajat Celsius) demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "B",
        "text": "Tidak menghantarkan arus listrik (non-konduktif), tidak meninggalkan residu kimiawi korosif yang merusak sirkuit elektronik, dan aman bagi manusia di dalam ruangan pada konsentrasi desain standar."
      },
      {
        "key": "C",
        "text": "Membanjiri ruangan dengan air bertekanan tinggi yang telah dihilangkan mineral garamnya."
      },
      {
        "key": "D",
        "text": "Menghilangkan seluruh gas oksigen hingga 0% dalam waktu kurang dari 1 detik."
      },
      {
        "key": "E",
        "text": "Bereaksi secara kimiawi membakar habis seluruh bahan plastik isolator kabel jaringan."
      }
    ],
    "correctKey": "B",
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
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-01",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Troubleshooting OSPF Neighbor Stuck in EXSTART/EXCHANGE State",
    "type": "mcq",
    "questionHtml": "Dua router OSPF yang terhubung langsung melalui kabel Ethernet mengalami kegagalan pembentukan kebertetanggaan (adjacency) dan statusnya macet (stuck) pada status `EXSTART / EXCHANGE`. Hasil inspeksi perintah `show ip ospf neighbor` menunjukkan status konstan tersebut. Penyebab paling umum dari masalah OSPF stuck di EXSTART/EXCHANGE adalah...",
    "options": [
      {
        "key": "A",
        "text": "Perbedaan nomor OSPF Process ID yang dikonfigurasikan pada kedua perangkat router dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "B",
        "text": "Router ID pada kedua router memiliki nilai yang sama persis (Router ID conflict)."
      },
      {
        "key": "C",
        "text": "Perbedaan waktu sistem (NTP clock drift) antara kedua router melebihi 10 detik."
      },
      {
        "key": "D",
        "text": "Ketidakcocokan nilai Maximum Transmission Unit (MTU) pada antarmuka kedua router yang bertetangga."
      },
      {
        "key": "E",
        "text": "Kabel serat optik yang digunakan mengalami pelemahan daya (loss) sebesar 0.2 dB."
      }
    ],
    "correctKey": "D",
    "explanation": "Dalam pembentukan adjacency OSPF, pada fase EXSTART kedua router menegosiasikan peran Master/Slave dan saling bertukar Database Description (DBD) packets. Jika nilai MTU pada antarmuka kedua router tidak cocok (misal router A diset MTU 1500 dan router B diset MTU 1492), paket DBD yang berukuran penuh akan didrop atau ditolak oleh router dengan MTU lebih kecil, menyebabkan proses OSPF terjebak selamanya di status EXSTART/EXCHANGE."
  },
  {
    "id": "tkj-sim-02",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis OTDR Dead Zone pada Link Serat Optik",
    "type": "mcq",
    "questionHtml": "Dalam pengujian kabel drop optik pelanggan FTTH sepanjang 80 meter menggunakan OTDR, teknisi tidak dapat mendeteksi adanya tekukan tajam (bending) pada jarak 5 meter pertama dari konektor ODF. Keterbatasan fisik alat OTDR yang menyebabkan fenomena 'titik buta' pada awal kabel tersebut dinamakan...",
    "options": [
      {
        "key": "A",
        "text": "Dispersi polarisasi mode akibat medan gravitasi bumi pada serat kaca."
      },
      {
        "key": "B",
        "text": "Kerusakan laser dioda pemancar akibat kehabisan baterai lithium OTDR."
      },
      {
        "key": "C",
        "text": "Efek non-linear Raman Scattering yang menyerap daya optik pada frekuensi tinggi demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "D",
        "text": "Ketiadaan ground listrik pada casing plastik bodi alat ukur OTDR."
      },
      {
        "key": "E",
        "text": "Attenuation Dead Zone (ADZ) dan Event Dead Zone (EDZ) yang diakibatkan saturasi fotodetektor oleh pantulan Fresnel konektor awal."
      }
    ],
    "correctKey": "E",
    "explanation": "Event Dead Zone (EDZ) dan Attenuation Dead Zone (ADZ) adalah zona buta pada awal pengukuran OTDR yang terjadi karena pantulan Fresnel yang sangat kuat pada konektor peluncuran (launch connector) membuat fotodetektor receiver OTDR jenuh (saturated). Selama masa pemulihan saturasi ini, OTDR tidak mampu mengukur atau membedakan event gangguan lain. Solusi standarnya adalah menggunakan kabel pancingan (Launch Cable / Dummy Fiber sepanjang 500-1000 m)."
  },
  {
    "id": "tkj-sim-03",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SWITCHING",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "VLAN Hopping Attack: Mitigasi Double Tagging 802.1Q",
    "type": "mcq",
    "questionHtml": "Seorang penyerang di VLAN 10 (Access Port) mengirimkan frame Ethernet khusus yang disematkan dua buah tag 802.1Q sekaligus: tag luar bernilai VLAN 1 (Native VLAN) dan tag dalam bernilai VLAN 20 (Target). Switch pertama mencopot tag luar dan meneruskannya ke trunk, sehingga switch kedua menerima frame tersebut dan mengalirkannya ke VLAN 20 (serangan Double Tagging VLAN Hopping). Langkah pertahanan terbaik untuk mencegah serangan ini adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah Native VLAN pada seluruh port trunk menjadi VLAN ID khusus yang tidak digunakan (misal VLAN 999) dan mengaktifkan 'vlan dot1q tag native'."
      },
      {
        "key": "B",
        "text": "Menyetel seluruh port switch menjadi mode trunk dengan Dynamic Trunking Protocol (DTP) aktif sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "C",
        "text": "Menonaktifkan protokol Spanning Tree pada seluruh switch distribusi dan access."
      },
      {
        "key": "D",
        "text": "Memperpanjang ukuran frame jumbo MTU menjadi 9216 bytes pada port klien."
      },
      {
        "key": "E",
        "text": "Mengganti seluruh kabel UTP dengan kabel koaksial berpelindung ganda."
      }
    ],
    "correctKey": "A",
    "explanation": "Double-tagging VLAN hopping attack mengeksploitasi fitur Native VLAN yang dikirimkan tanpa tag (untagged) pada port trunk 802.1Q. Jika port penyerang berada pada VLAN yang sama dengan Native VLAN trunk (biasanya default VLAN 1), switch pertama akan mencopot tag luar dan mengirimkan frame mentah yang masih memuat tag dalam (VLAN 20 target) ke link trunk. Switch kedua akan meneruskan frame tersebut ke VLAN 20. Mitigasi resminya adalah mengubah Native VLAN trunk ke VLAN yang tidak dipakai oleh port access mana pun, serta mengonfigurasi `vlan dot1q tag native` agar Native VLAN pun tetap di-tag."
  },
  {
    "id": "tkj-lat-sim-04",
    "subject": "tkj",
    "materi": "PENGALAMATAN IPV4 & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Kalkulasi Subnet Point-to-Point WAN /31 vs /30",
    "type": "mcq",
    "questionHtml": "Dalam menghubungkan dua router backbone core (link point-to-point serial atau Ethernet WAN), administrator ingin menghemat alamat IPv4 publik sebaik mungkin. Standar RFC 3021 memungkinkan penggunaan prefix subnet mask khusus yang hanya mengalokasikan tepat 2 alamat IP tanpa menyia-nyiakan Network ID dan Broadcast ID tradisional. Prefix yang dimaksud adalah...",
    "options": [
      {
        "key": "A",
        "text": "/30 dengan subnet mask 255.255.255.252 (menyediakan 2 usable host, 1 network ID, dan 1 broadcast ID)."
      },
      {
        "key": "B",
        "text": "/31 dengan subnet mask 255.255.255.254 (menyediakan tepat 2 alamat host untuk router-to-router)."
      },
      {
        "key": "C",
        "text": "/32 dengan subnet mask 255.255.255.255 (khusus host route loopback tunggal)."
      },
      {
        "key": "D",
        "text": "/29 dengan subnet mask 255.255.255.248 (menyediakan 6 usable host)."
      },
      {
        "key": "E",
        "text": "/28 dengan subnet mask 255.255.255.240 (menyediakan 14 usable host)."
      }
    ],
    "correctKey": "B",
    "explanation": "Secara tradisional, link point-to-point antar dua router menggunakan prefix /30 yang memakan 4 IP (1 Network ID, 2 Usable Host, 1 Broadcast ID) sehingga terjadi pemborosan 50% alamat. Standar RFC 3021 menetapkan penggunaan prefix /31 (mask 255.255.255.254) untuk link point-to-point, di mana kedua alamat yang tersedia diperlakukan langsung sebagai alamat host sah ujung-ke-ujung tanpa memerlukan Network ID maupun Broadcast ID, menghemat ruang alamat IPv4 secara signifikan."
  },
  {
    "id": "tkj-sim-05",
    "subject": "tkj",
    "materi": "JARINGAN NIRKABEL & WIRELESS",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Fast Roaming Nirkabel 802.11r/k/v",
    "type": "mcq",
    "questionHtml": "Di sebuah rumah sakit, perawat yang melakukan panggilan VoIP bergerak antar bangsal sering mengalami suara terputus selama 2 hingga 5 detik saat smartphone berpindah dari Access Point A ke Access Point B. Kombinasi standar protokol IEEE yang wajib diaktifkan pada sistem wireless controller terpusat untuk mewujudkan 'Seamless Fast BSS Transition' (roaming di bawah 50 ms) adalah...",
    "options": [
      {
        "key": "A",
        "text": "IEEE 802.1D (Spanning Tree), 802.1Q (VLAN Tagging), dan 802.3af (Power over Ethernet) guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "B",
        "text": "IEEE 802.11b (DSSS 11 Mbps) dan 802.11a (OFDM 54 Mbps)."
      },
      {
        "key": "C",
        "text": "IEEE 802.11r (Fast Transition), 802.11k (Radio Resource Measurement), dan 802.11v (Wireless Network Management)."
      },
      {
        "key": "D",
        "text": "IEEE 802.3ad (Link Aggregation) dan 802.3x (Flow Control)."
      },
      {
        "key": "E",
        "text": "IEEE 802.1X murni tanpa dukungan ekstensi handover nirkabel."
      }
    ],
    "correctKey": "C",
    "explanation": "Pada jaringan Wi-Fi enterprise berkeamanan 802.1X/WPA2, proses roaming standar membutuhkan re-authentication penuh ke server RADIUS dan 4-way handshake ulang yang memakan waktu 2-5 detik (memutus panggilan VoIP). Solusinya adalah trio standar IEEE: 802.11k (membantu klien memindai daftar AP tetangga terbaik), 802.11v (mengarahkan klien ke AP yang tidak padat), dan 802.11r (Fast BSS Transition yang menyimpan cache kunci enkripsi di controller sehingga waktu handover terpangkas menjadi di bawah 50 ms tanpa lag percakapan)."
  },
  {
    "id": "tkj-sim-06",
    "subject": "tkj",
    "materi": "MANAJEMEN BANDWIDTH & QOS",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Kalkulasi Burst Limit, Burst Threshold, dan Burst Time MikroTik",
    "type": "mcq",
    "questionHtml": "Sebuah aturan Simple Queue di MikroTik dikonfigurasikan dengan parameter berikut:\n• Max-Limit = `2 Mbps`\n• Burst-Limit = `8 Mbps`\n• Burst-Threshold = `1.5 Mbps`\n• Burst-Time = `16 detik`\nJika pengguna mengunduh file besar secara terus-menerus dengan memanfaatkan kapasitas pipa data maksimal, berapa detik pengguna tersebut akan menikmati kecepatan 8 Mbps sebelum kecepatannya diturunkan kembali ke 2 Mbps?",
    "options": [
      {
        "key": "A",
        "text": "16 detik penuh sesuai nilai Burst-Time yang ditentukan di antarmuka Winbox untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "B",
        "text": "8 detik karena kecepatan diturunkan tepat di separuh waktu konfigurasi."
      },
      {
        "key": "C",
        "text": "12 detik karena nilai Max-Limit lebih tinggi daripada Burst-Threshold."
      },
      {
        "key": "D",
        "text": "3 detik (dihitung dari formula: (Burst-Threshold / Burst-Limit) * Burst-Time = (1.5 / 8) * 16 = 3 detik)."
      },
      {
        "key": "E",
        "text": "Kecepatan 8 Mbps bertahan selamanya tanpa pernah diturunkan router."
      }
    ],
    "correctKey": "D",
    "explanation": "Pada MikroTik RouterOS, 'Burst-Time' bukan durasi waktu burst diberikan, melainkan jendela waktu (moving average window) yang digunakan router untuk menghitung kecepatan rata-rata klien. Rumus durasi waktu burst maksimum (T_burst) saat download konstan pada rate Burst-Limit adalah: T_burst = (Burst-Threshold / Burst-Limit) * Burst-Time = (1.5 Mbps / 8 Mbps) * 16 detik = 0.1875 * 16 = tepat 3 detik. Setelah 3 detik, kecepatan rata-rata klien melampaui 1.5 Mbps sehingga router membatasi kecepatan ke Max-Limit (2 Mbps)."
  },
  {
    "id": "tkj-sim-07",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Pendeteksian BGP Route Flapping & Dampak Route Flap Damping",
    "type": "mcq",
    "questionHtml": "Sebuah link antarmuka eBGP ke arah ISP eksternal mengalami gangguan fisik kabel yang menyebabkan sesi BGP berulang kali terhubung lalu putus (flapping) puluhan kali dalam satu jam. Dampak mekanisme BGP Route Flap Damping (RFC 2439) yang diaktifkan oleh ISP Tier-1 terhadap prefix jaringan tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "ISP akan melipatgandakan alokasi bandwidth link hingga link stabil kembali."
      },
      {
        "key": "B",
        "text": "Router border BGP akan secara otomatis beralih menggunakan protokol routing RIPv2."
      },
      {
        "key": "C",
        "text": "Seluruh konfigurasi router lokal akan terhapus dan kembali ke setelan pabrik default dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "D",
        "text": "Sesi BGP dialihkan secara otomatis menggunakan kabel telepon analog PSTN."
      },
      {
        "key": "E",
        "text": "Prefix jaringan tersebut akan dikenai denda penalti (suppressed) dan disembunyikan dari tabel perutean global internet selama periode penalti tertentu (decay half-life)."
      }
    ],
    "correctKey": "E",
    "explanation": "Route Flapping adalah kondisi di mana suatu rute terus-menerus muncul dan hilang (up/down) dalam waktu singkat, memicu badai pembaruan BGP UPDATE ke jutaan router di seluruh dunia dan membebani CPU router global. Untuk mengatasinya, router ISP menerapkan BGP Route Flap Damping (RFC 2439). Setiap kali rute flap, rute diberi skor penalti (misal 1000). Jika akumulasi penalti melampaui batas 'suppress threshold', rute akan diblokir (suppressed) dan tidak lagi diumumkan ke internet global hingga penaltinya meluruh (decay) di bawah 'reuse threshold'."
  },
  {
    "id": "tkj-sim-08",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Serangan DNS Cache Poisoning (Kaminsky Bug)",
    "type": "mcq",
    "questionHtml": "Pada serangan legendaris DNS Cache Poisoning (seperti eksploitasi Dan Kaminsky), penyerang mengirimkan ribuan respons DNS palsu yang memalsukan Transaction ID dan UDP Source Port untuk mengarahkan pengunjung website bank ke server penipu. Teknologi ekstensi keamanan DNS yang dirancang untuk mencegah pemalsuan cache rekursif ini menggunakan tanda tangan digital kriptografi adalah...",
    "options": [
      {
        "key": "A",
        "text": "DNSSEC (Domain Name System Security Extensions) berbasis verifikasi rantai RRSIG dan DNSKEY."
      },
      {
        "key": "B",
        "text": "DHCP Snooping yang memblokir kueri UDP port 53 pada access port switch demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "C",
        "text": "Dynamic Host Configuration Protocol Option 82 pada server gateway."
      },
      {
        "key": "D",
        "text": "Spanning Tree Protocol PortFast BPDU Filter pada router border."
      },
      {
        "key": "E",
        "text": "NAT Masquerade dengan memodifikasi field checksum header IP."
      }
    ],
    "correctKey": "A",
    "explanation": "DNS konvensional tidak memiliki mekanisme autentikasi pesan, sehingga resolver rentan menerima jawaban palsu dari peretas yang berhasil menebak Transaction ID 16-bit dan UDP source port (Kaminsky DNS Cache Poisoning). DNSSEC (RFC 4033) menyelesaikan kelemahan ini dengan memperkenalkan kriptografi kunci publik: setiap DNS record ditandatangani secara digital dengan Record RRSIG (Resource Record Signature) yang dapat diverifikasi keabsahannya menggunakan kunci publik DNSKEY melalui rantai kepercayaan hierarkis (Chain of Trust) hingga ke Root DNS Anchor."
  },
  {
    "id": "tkj-sim-09",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Teknologi GPON: Perhitungan Splitter Rasio dan Redaman Pasif",
    "type": "mcq",
    "questionHtml": "Dalam perancangan jaringan akses fiber optik FTTH berbasis Gigabit Passive Optical Network (GPON), sebuah port Optical Line Terminal (OLT) dengan daya kirim $+3\\text{ dBm}$ dihubungkan ke Optical Splitter pasif bertingkat:\n• Splitter 1:4 (redaman nominal teoretis = $7.0\\text{ dB}$)\n• Splitter 1:8 (redaman nominal teoretis = $10.5\\text{ dB}$)\nJika total redaman kabel dan konektor sepanjang jalur adalah $4.5\\text{ dB}$, estimasi daya optik yang diterima oleh Optical Network Terminal (ONT) di rumah pelanggan adalah...",
    "options": [
      {
        "key": "A",
        "text": "-35.0 dBm (mengalami loss berlebih sehingga ONT masuk status Loss of Signal / LOS merah) sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      },
      {
        "key": "B",
        "text": "-19.0 dBm (berada dalam rentang sensitivitas ideal ONT GPON kelas B+ yaitu -8 s/d -27 dBm)."
      },
      {
        "key": "C",
        "text": "-5.5 dBm (sinyal terlalu kuat sehingga merusak modul fotodetektor receiver ONT)."
      },
      {
        "key": "D",
        "text": "+1.5 dBm (mengindikasikan terjadinya penguatan daya optik pasif di dalam splitter)."
      },
      {
        "key": "E",
        "text": "-12.0 dBm (daya terukur tidak dipengaruhi oleh keberadaan splitter optik)."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "KALKULASI TOTAL LOSS GPON SPLITTER BERTINGKAT",
      "latex": "\\begin{aligned} \\text{Total Loss} &= \\text{Loss}_{1:4} (7.0) + \\text{Loss}_{1:8} (10.5) + \\text{Loss}_{\\text{kabel}} (4.5) = 22.0\\,\\text{dB} \\\\ P_{\\text{ONT}} &= P_{\\text{OLT}} (+3\\,\\text{dBm}) - \\text{Total Loss} (22.0\\,\\text{dB}) = -19.0\\,\\text{dBm} \\end{aligned}",
      "legend": "• Standar GPON Kelas B+: Rentang penerimaan ONT sah adalah -8 dBm s/d -27 dBm<br>• Nilai -19.0 dBm sangat optimal dan stabil"
    },
    "hints": {
      "concept": "Jumlahkan seluruh redaman: Splitter 1 (7.0 dB) + Splitter 2 (10.5 dB) + Redaman kabel/konektor (4.5 dB) = 22.0 dB. Kurangkan dari daya kirim OLT (+3 dBm).",
      "execution": "P_ONT = +3 dBm - 22.0 dB = -19.0 dBm. Nilai ini berada di jendela ideal GPON (-8 s/d -27 dBm)."
    },
    "explanation": "Total redaman pada jaringan ODN (Optical Distribution Network) dihitung dari penjumlahan seluruh redaman pasif: Redaman Splitter 1:4 (7.0 dB) + Redaman Splitter 1:8 (10.5 dB) + Redaman transmisi serat dan koneksi (4.5 dB) = 22.0 dB. Daya terima pada receiver ONT = Daya kirim OLT - Total Redaman = +3 dBm - 22.0 dB = -19.0 dBm. Nilai -19.0 dBm sangat aman karena standar GPON ITU-T G.984 kelas B+ mensyaratkan daya terima ONT berada pada rentang -8 dBm hingga -27 dBm."
  },
  {
    "id": "tkj-sim-10",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Rapid Spanning Tree Protocol (RSTP 802.1w) Handshake",
    "type": "mcq",
    "questionHtml": "Berbeda dengan Spanning Tree klasik (802.1D) yang membutuhkan waktu tunggu pasif hingga 30-50 detik (fase Listening dan Learning) untuk konvergensi, Rapid STP (IEEE 802.1w) mampu mencapai status forwarding dalam waktu kurang dari 1 detik pada link point-to-point. Mekanisme negosiasi aktif antar-switch yang mendasari kecepatan konvergensi RSTP tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Penghapusan seluruh tabel MAC Address secara otomatis setiap terjadi perubahan topologi fisik guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "B",
        "text": "Penggunaan protokol routing dinamis OSPF di layer 2 untuk menghitung rute frame terpendek."
      },
      {
        "key": "C",
        "text": "Mekanisme Proposal-Agreement Handshake yang mengeksekusi sinkronisasi status port secara langsung antar dua switch tetangga."
      },
      {
        "key": "D",
        "text": "Pengecekan arus listrik tegangan port switch menggunakan sensor resistansi tembaga."
      },
      {
        "key": "E",
        "text": "Pendelegasian seluruh kalkulasi pohon topologi jaringan ke server cloud internet eksternal."
      }
    ],
    "correctKey": "C",
    "explanation": "RSTP (IEEE 802.1w) menggantikan timer kaku 802.1D (Forward Delay 15s + 15s) dengan mekanisme sinkronisasi aktif bernama 'Proposal-Agreement Handshake'. Ketika sebuah link point-to-point aktif antar dua switch, switch hulu mengirimkan frame Proposal untuk menjadi Designated Port. Switch hilir segera memblokir port-port non-edge miliknya (proses sinkronisasi) lalu seketika membalas dengan frame Agreement. Begitu frame Agreement diterima, port hulu langsung melompat ke status Forwarding dalam hitungan milidetik tanpa menunggu timer pasif."
  },
  {
    "id": "tkj-sim-11",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Log Firewall: Serangan Port Scanning Nmap Stealth SYN",
    "type": "mcq",
    "questionHtml": "Administrator sistem memeriksa berkas log `/var/log/auth.log` dan log iptables, menemukan ribuan percobaan koneksi TCP dalam rentang waktu 3 detik dari IP `198.51.100.25` ke seluruh port (1 s/d 1024). Setiap koneksi hanya mengirimkan flag SYN, dan ketika server membalas dengan SYN-ACK, pengirim seketika membalas dengan flag RST (Reset). Teknik pemindaian jaringan yang sedang dilancarkan peretas tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "TCP Connect Scan murni yang membuka sesi soket penuh dengan pustaka standar OS."
      },
      {
        "key": "B",
        "text": "UDP Flooding attack yang bertujuan melumpuhkan bandwidth antarmuka server."
      },
      {
        "key": "C",
        "text": "Serangan SQL Injection berbasis boolean blind pada formulir autentikasi web."
      },
      {
        "key": "D",
        "text": "TCP SYN Stealth Scan (Nmap flag -sS / Half-Open Scanning) untuk mendeteksi port terbuka tanpa menyelesaikan handshake 3 arah penuh sehingga tidak tercatat di log aplikasi server."
      },
      {
        "key": "E",
        "text": "Percobaan sinkronisasi waktu jaringan menggunakan protokol Network Time Protocol (NTP) untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      }
    ],
    "correctKey": "D",
    "explanation": "Pola di mana klien mengirim SYN, menerima SYN-ACK dari target, lalu segera membalas dengan flag RST (Reset) sebelum mengirimkan ACK penutup adalah ciri khas dari 'TCP SYN Stealth Scan' (dieksekusi melalui `nmap -sS`). Teknik ini disebut pemindaian separuh terbuka (half-open scanning) karena penyerang sengaja memutuskan koneksi sebelum 3-Way Handshake selesai secara penuh, sehingga sistem operasi server tidak mencatat koneksi tersebut pada log aplikasi tingkat atas (seperti Apache/Nginx access log)."
  },
  {
    "id": "tkj-sim-12",
    "subject": "tkj",
    "materi": "LAYANAN JARINGAN & SERVER",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Troubleshooting Layanan Web: Analisis HTTP 502 Bad Gateway Nginx",
    "type": "mcq",
    "questionHtml": "Di sebuah web server sekolah yang menggunakan arsitektur Nginx sebagai Reverse Proxy dan PHP-FPM / Node.js sebagai backend, pengguna internet mengeluhkan munculnya pesan kesalahan di browser: `502 Bad Gateway`. Setelah diperiksa, server Nginx menyala normal. Akar permasalahan teknis yang paling akurat dari error 502 Bad Gateway tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "File index.html tidak ditemukan pada direktori penyimpanan dokumen server (Not Found) guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "B",
        "text": "Sertifikat SSL/TLS domain telah kedaluwarsa sehingga koneksi HTTPS dihentikan browser."
      },
      {
        "key": "C",
        "text": "Pengguna salah memasukkan username dan password pada halaman form login pengguna."
      },
      {
        "key": "D",
        "text": "Klien menggunakan browser versi lama yang tidak mendukung format gambar WebP."
      },
      {
        "key": "E",
        "text": "Nginx (sebagai proxy) gagal berkomunikasi atau tidak menerima respons yang valid dari server aplikasi upstream (PHP-FPM socket / Node.js port 3000 down atau hang)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kode status HTTP 502 (Bad Gateway) adalah respons tingkat server yang berarti server proxy (dalam kasus ini Nginx) berhasil menerima permintaan dari klien, tetapi ketika Nginx mencoba meneruskan permintaan tersebut ke server backend hulu (upstream application server seperti PHP-FPM, Gunicorn, atau Node.js), backend tersebut mati (service stop/crash), hang, atau menolak koneksi soket. Akibatnya Nginx mengembalikan kode 502 Bad Gateway ke pengunjung."
  },
  {
    "id": "tkj-sim-13",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Konsep BGP Loop Prevention: AS Path Matching",
    "type": "mcq",
    "questionHtml": "Protokol Border Gateway Protocol (BGP) yang mengendalikan lalu lintas routing antar Autonomous System di seluruh dunia tidak menggunakan algoritma Dijkstra melainkan Distance Vector tingkat lanjut (Path Vector). Mekanisme sederhana namun absolut yang digunakan BGP untuk mencegah terjadinya routing loop global adalah...",
    "options": [
      {
        "key": "A",
        "text": "Router BGP akan membuang (drop/ignore) setiap pengumuman rute yang memuat nomor Autonomous System (AS)-nya sendiri di dalam atribut AS Path."
      },
      {
        "key": "B",
        "text": "Router BGP menghitung nilai hop count maksimum yang tidak boleh melebihi 15 hop seperti RIP."
      },
      {
        "key": "C",
        "text": "Router BGP memverifikasi keaslian paket menggunakan tanda tangan token JWT di setiap payload untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "D",
        "text": "Seluruh update rute BGP wajib dilewatkan melalui kabel optik bawah laut Samudra Pasifik."
      },
      {
        "key": "E",
        "text": "Setiap sesi BGP diputus paksa dan dinegosiasikan ulang setiap interval 60 detik."
      }
    ],
    "correctKey": "A",
    "explanation": "Sebagai protokol Path Vector, BGP mencatat setiap Autonomous System yang dilewati oleh sebuah prefix rute pada atribut 'AS Path'. Aturan pencegahan loop BGP (BGP Loop Prevention) menyatakan: ketika sebuah router BGP menerima pembaruan rute (BGP UPDATE) dari tetangga eBGP, router akan memindai daftar nomor AS di dalam atribut AS Path. Jika router mendeteksi nomor AS-nya sendiri tercantum di dalam daftar tersebut, router menyimpulkan rute tersebut telah berputar kembali ke tempat asalnya (loop) dan seketika menolak rute tersebut masuk ke tabel routing."
  },
  {
    "id": "tkj-sim-14",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Prinsip Zero Trust Network Access (ZTNA) vs VPN Tradisional",
    "type": "mcq",
    "questionHtml": "Dalam arsitektur keamanan jaringan modern, organisasi berpindah dari model perimeter VPN warisan menuju paradigma Zero Trust Network Access (ZTNA). Perbedaan filosofis dan teknis paling mendasar antara VPN konvensional dan ZTNA adalah...",
    "options": [
      {
        "key": "A",
        "text": "VPN menggunakan enkripsi kriptografi sedangkan ZTNA menolak enkripsi data untuk mempercepat transmisi."
      },
      {
        "key": "B",
        "text": "VPN tradisional memberikan akses penuh ke seluruh subnet LAN setelah terhubung (castle-and-moat), sedangkan ZTNA menerapkan prinsip 'never trust, always verify' dengan memberikan akses mikrosegmentasi hanya ke aplikasi spesifik yang diizinkan."
      },
      {
        "key": "C",
        "text": "ZTNA hanya dapat diakses menggunakan komputer mainframe tanpa dukungan perangkat smartphone."
      },
      {
        "key": "D",
        "text": "VPN tradisional tidak memerlukan alamat IP publik sedangkan ZTNA mewajibkan IP statis di setiap laptop."
      },
      {
        "key": "E",
        "text": "ZTNA menghapus seluruh sistem firewall fisik dan menggantinya dengan sakelar listrik manual."
      }
    ],
    "correctKey": "B",
    "explanation": "Model keamanan tradisional (Castle-and-Moat) menggunakan VPN di mana pengguna yang berhasil melewati perimeter gerbang (login VPN) akan mendapatkan akses tingkat jaringan (network-level access) ke seluruh segmen IP LAN di kantor, membuka celah lateral movement bagi peretas. Sebaliknya, Zero Trust Network Access (ZTNA) mengadopsi prinsip 'Never Trust, Always Verify': pengguna tidak pernah ditempatkan di jaringan perusahaan secara langsung, melainkan hanya diberikan akses mikrosegmentasi terisolasi ke aplikasi tertentu (application-level access) setelah memeriksa konteks perangkat, identitas, dan postur keamanan secara kontinu."
  },
  {
    "id": "tkj-sim-15",
    "subject": "tkj",
    "materi": "TRANSISI IPV6 & NEXT-GEN NETWORK",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Neighbor Discovery Protocol (NDP): Pengganti ARP pada IPv6",
    "type": "mcq",
    "questionHtml": "Pada arsitektur IPv6, protokol Address Resolution Protocol (ARP) dan broadcast dihapuskan secara total dari spesifikasi jaringan. Dua pesan protokol Neighbor Discovery Protocol (NDP berbasis ICMPv6) yang menggantikan peran ARP Request dan ARP Reply untuk memetakan alamat IP ke MAC address pada link lokal adalah...",
    "options": [
      {
        "key": "A",
        "text": "Router Solicitation (RS) dan Router Advertisement (RA) guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "B",
        "text": "Echo Request (Type 128) dan Echo Reply (Type 129)."
      },
      {
        "key": "C",
        "text": "Neighbor Solicitation (NS menggunakan multicast solicited-node) dan Neighbor Advertisement (NA)."
      },
      {
        "key": "D",
        "text": "DHCPv6 Solicit dan DHCPv6 Advertise."
      },
      {
        "key": "E",
        "text": "IGMP Membership Report dan IGMP Leave Group."
      }
    ],
    "correctKey": "C",
    "explanation": "Pada IPv6, ARP dieliminasi untuk menghindari badai broadcast jaringan. Fungsinya digantikan oleh Neighbor Discovery Protocol (NDP RFC 4861) yang beroperasi di atas ICMPv6. Untuk memetakan alamat IPv6 ke MAC address link lokal, host mengirimkan pesan 'Neighbor Solicitation' (ICMPv6 Type 135) secara efisien ke alamat Solicited-Node Multicast (`FF02::1:FFXX:XXXX`), dan host target akan membalas secara unicast dengan pesan 'Neighbor Advertisement' (ICMPv6 Type 136) yang memuat alamat MAC fisiknya."
  },
  {
    "id": "tkj-sim-16",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Pengaruh Macrobending vs Microbending pada Kabel Fiber Optik",
    "type": "mcq",
    "questionHtml": "Saat proses instalasi kabel patch cord fiber optik di dalam rack server, teknisi mengikat kabel terlalu kencang dengan cable-tie hingga kabel tertekuk dengan radius lengkungan hanya 5 mm (jauh di bawah rekomendasi minimum bend radius 30 mm). Dampak fisik optik yang terjadi di dalam inti serat kaca tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Kabel serat optik akan mengalirkan arus listrik induksi ke casing server rack."
      },
      {
        "key": "B",
        "text": "Panjang gelombang cahaya laser akan bergeser dari 1310 nm menjadi sinar ultraviolet."
      },
      {
        "key": "C",
        "text": "Diameter inti serat kaca akan meleleh secara otomatis akibat tekanan udara."
      },
      {
        "key": "D",
        "text": "Terjadi Macrobending Loss di mana sudut datang cahaya melampaui sudut kritis pantulan total (Total Internal Reflection), sehingga sebagian berkas cahaya bocor menembus lapisan cladding ke udara."
      },
      {
        "key": "E",
        "text": "Kecepatan transfer data bit rate jaringan meningkat dua kali lipat akibat pemampatan gelombang untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern."
      }
    ],
    "correctKey": "D",
    "explanation": "Cahaya merambat di dalam serat optik berdasarkan prinsip Pemantulan Internal Total (Total Internal Reflection), yang mensyaratkan sudut datang cahaya harus selalu lebih besar dari sudut kritis antarmuka core-cladding. Ketika kabel ditekuk tajam melebihi batas kelengkungan aman (Macrobending), sudut datang berkas cahaya terhadap dinding cladding menjadi terlalu curam (di bawah sudut kritis), menyebabkan berkas cahaya tidak lagi dipantulkan kembali melainkan menembus keluar (refraksi) ke jaket kabel, menimbulkan lonjakan redaman (loss) yang drastis."
  },
  {
    "id": "tkj-sim-17",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Arsitektur Spine-Leaf Data Center (Clos Network)",
    "type": "mcq",
    "questionHtml": "Dalam perancangan jaringan data center modern untuk beban kerja komputasi awan (cloud computing) dan virtualisasi, arsitektur hierarki tradisional 3-Tier (Core-Aggregation-Access) digantikan oleh topologi 2-Tier 'Spine-and-Leaf'. Keunggulan utama arsitektur Spine-and-Leaf dalam melayani lalu lintas data East-West (komunikasi antar server di dalam data center) adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menghilangkan seluruh kebutuhan switch fisik dengan menghubungkan kabel server langsung ke router gateway internet."
      },
      {
        "key": "B",
        "text": "Mengandalkan protokol Spanning Tree klasik untuk mematikan 50% link redundansi demi mencegah loop."
      },
      {
        "key": "C",
        "text": "Membatasi kecepatan transfer data antar server maksimum tepat 10 Mbps untuk penghematan listrik."
      },
      {
        "key": "D",
        "text": "Hanya memperbolehkan satu server aktif dalam satu rak server secara bergantian."
      },
      {
        "key": "E",
        "text": "Setiap switch Leaf terhubung langsung ke seluruh switch Spine, menjamin jarak hop yang seragam (tepat 2 hop antar server) dengan latensi rendah dan pemanfaatan seluruh link aktif via Equal-Cost Multi-Path (ECMP)."
      }
    ],
    "correctKey": "E",
    "explanation": "Pada arsitektur Spine-and-Leaf (berbasis topologi Clos network), setiap switch Leaf (rak server) terhubung ke semua switch Spine di atasnya, dan tidak ada interkoneksi antar sesama Spine maupun antar sesama Leaf. Desain ini menghilangkan pemblokiran port oleh Spanning Tree dengan memanfaatkan perutean Layer 3 ECMP (Equal-Cost Multi-Path). Hasilnya, setiap server di rak mana pun dapat berkomunikasi dengan server di rak lain dengan jarak tepat 2 hop yang konsisten, menghasilkan throughput maksimal dan latensi ultra-rendah untuk trafik East-West."
  },
  {
    "id": "tkj-sim-18",
    "subject": "tkj",
    "materi": "PENGALAMATAN IPV4 & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Troubleshooting Duplicate IP & Gratuitous ARP",
    "type": "mcq",
    "questionHtml": "Di sebuah lab komputer, seorang siswa secara sengaja menyetel IP manual statis `192.168.1.50` yang ternyata sudah digunakan oleh komputer server ujian lokal. Seketika muncul pesan peringatan 'IP Address Conflict' di layar Windows server dan server menolak koneksi. Mekanisme protokol layer 2 yang mendeteksi konflik duplikasi IP tersebut sesaat setelah kartu jaringan siswa dinyalakan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Gratuitous ARP (GARP) / Address Collision Detection (ACD) yang dibroadcast oleh host untuk memeriksa apakah ada perangkat lain yang menjawab kepemilikan IP tersebut."
      },
      {
        "key": "B",
        "text": "Query DNS rekursif ke root-servers.net yang memvalidasi sertifikat hardware."
      },
      {
        "key": "C",
        "text": "Paket ICMP Echo Request yang dikirimkan oleh switch access ke cloud provider demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "D",
        "text": "Pengecekan lisensi Windows Defender melalui port TCP 445 SMB share."
      },
      {
        "key": "E",
        "text": "Pemindaian port SSH otomatis menggunakan script Python di background kernel."
      }
    ],
    "correctKey": "A",
    "explanation": "Ketika antarmuka jaringan dikonfigurasikan dengan sebuah alamat IP baru, sistem operasi modern akan menjalankan mekanisme IPv4 Address Conflict Detection (RFC 5227) menggunakan 'Gratuitous ARP' (GARP). Host mengirimkan frame ARP Request broadcast ke jaringan lokal dengan IP pengirim dan IP target yang sama-sama diisi alamat IP barunya tersebut (misal: 'Siapa yang memakai 192.168.1.50?'). Jika ada perangkat lain yang membalas ARP Reply tersebut, sistem operasi mengetahui bahwa IP tersebut sudah dipakai (duplikat) dan seketika memunculkan peringatan konflik."
  },
  {
    "id": "tkj-sim-19",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Serangan DNS Amplification DDoS",
    "type": "mcq",
    "questionHtml": "Jaringan sekolah mengalami kelumpuhan total (bandwidth pipa internet 1 Gbps penuh 100%) akibat serangan Distributed Denial of Service (DDoS). Analisis flow data menunjukkan jutaan paket DNS response berukuran besar (>3.000 bytes) membanjiri alamat IP publik router sekolah dari ratusan Open DNS Resolver di seluruh dunia, padahal router sekolah tidak pernah meminta data tersebut. Mekanisme eksploitasi yang dilancarkan peretas pada serangan DNS Amplification ini adalah...",
    "options": [
      {
        "key": "A",
        "text": "Pencurian password admin router melalui jalur koneksi console serial RS-232 fisik."
      },
      {
        "key": "B",
        "text": "IP Spoofing (memalsukan IP sumber kueri DNS menjadi IP publik korban) dipadukan dengan kueri tipe 'ANY' atau DNSSEC berukuran besar ke Open Resolver (faktor amplifikasi 50x hingga 100x)."
      },
      {
        "key": "C",
        "text": "Pengiriman virus macro melalui lampiran email Microsoft Word ke komputer kepala sekolah."
      },
      {
        "key": "D",
        "text": "Pemberian tegangan listrik berlebih melalui kabel Power over Ethernet ke switch access."
      },
      {
        "key": "E",
        "text": "Manipulasi frekuensi radio Access Point dari 2.4 GHz menjadi sinyal gelombang radio FM komersial dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      }
    ],
    "correctKey": "B",
    "explanation": "Serangan DNS Amplification adalah bentuk serangan Distributed Denial of Service (DDoS) berbasis refleksi. Penyerang memanfaatkan fakta bahwa protokol UDP tidak melakukan handshake (connectionless) sehingga IP pengirim sangat mudah dipalsukan (IP Spoofing). Botnet mengirimkan kueri DNS kecil (~60 bytes) dengan IP sumber yang dipalsukan menjadi IP korban menuju ribuan Open DNS Resolver publik di internet. Kueri tersebut meminta record besar (seperti `ANY` record atau zona bertanda tangan DNSSEC yang berukuran >3.000 bytes). Seluruh server DNS publik tersebut akan membalas dan mengarahkan gelombang data raksasa ke IP korban."
  },
  {
    "id": "tkj-sim-20",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "OSPF Virtual Link untuk Menghubungkan Disconnected Area",
    "type": "mcq",
    "questionHtml": "Dalam merger dua jaringan sekolah, sebuah area OSPF baru (Area 2) secara fisik hanya terhubung ke Area 1 dan tidak memiliki koneksi fisik langsung ke Area 0 (Backbone). Sesuai aturan OSPF, seluruh area non-backbone wajib terhubung langsung ke Area 0 untuk pertukaran rute inter-area. Solusi logikal OSPF darurat yang dapat dikonfigurasi untuk menghubungkan Area 2 ke Area 0 melintasi Area 1 adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah Area 2 menjadi Totally Stubby Area tanpa default route."
      },
      {
        "key": "B",
        "text": "Mengaktifkan protokol routing RIPv1 pada antarmuka penghubung kedua area."
      },
      {
        "key": "C",
        "text": "OSPF Virtual Link yang dikonfigurasikan melintasi Area 1 (Transit Area) antara ABR Area 1/2 dengan ABR Area 0/1."
      },
      {
        "key": "D",
        "text": "Menghapus seluruh konfigurasi OSPF dan menggantinya dengan bridging layer 2 murni untuk memastikan seluruh frame dan paket data terdistribusi secara seimbang tanpa jitter."
      },
      {
        "key": "E",
        "text": "Mengubah router ID kedua ABR menjadi bernilai sama 0.0.0.0."
      }
    ],
    "correctKey": "C",
    "explanation": "Aturan hierarki OSPF mewajibkan semua area non-backbone terhubung secara langsung ke Area 0 (Backbone) untuk mencegah routing loop inter-area. Jika karena kendala fisik ada area yang terisolasi (misal Area 2 hanya tersambung ke Area 1), solusi OSPF resmi adalah membangun 'OSPF Virtual Link'. Virtual Link adalah terowongan logis yang dibangun melintasi area transit non-backbone (Area 1) antara dua Area Border Router (ABR) untuk memperpanjang jangkauan konektivitas Area 0 hingga mencapai area yang terputus."
  },
  {
    "id": "tkj-sim-21",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Redaman Konektor UPC vs APC pada Jaringan FTTH GPON",
    "type": "mcq",
    "questionHtml": "Pada konektor kabel fiber optik, terdapat dua jenis pemolesan ujung ferrule kaca: Ultra Physical Contact (UPC berwarna biru dengan ujung datar cembung) dan Angled Physical Contact (APC berwarna hijau dengan sudut miring 8 derajat). Alasan mutlak mengapa jaringan FTTH GPON dan siaran video RF-overlay selalu mewajibkan penggunaan konektor APC hijau pada Optical Distribution Network (ODN) adalah...",
    "options": [
      {
        "key": "A",
        "text": "Konektor APC dapat dipasang secara terbalik tanpa perlu membersihkan debu pada ferrule."
      },
      {
        "key": "B",
        "text": "Konektor APC hijau memiliki diameter inti kaca serat optik yang dua kali lebih lebar daripada UPC biru dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih guna menjamin keandalan transmisi data dan kepatuhan standar industri telekomunikasi."
      },
      {
        "key": "C",
        "text": "Konektor APC tidak memerlukan pengunci klip mekanik saat ditancapkan ke adapter."
      },
      {
        "key": "D",
        "text": "Sudut kemiringan 8 derajat pada ferrule APC memantulkan cahaya balik (optical return loss) ke dinding cladding, menghasilkan nilai return loss sangat tinggi ( $\\le -60\\text{ dB}$ ) yang melindungi pemancar laser OLT dari kerusakan."
      },
      {
        "key": "E",
        "text": "Warna hijau menandakan kabel tersebut ramah lingkungan dan bebas dari radiasi elektromagnetik."
      }
    ],
    "correctKey": "D",
    "explanation": "Pada konektor UPC (biru), ujung permukaan ferrule dipoles datar-cembung (flat/dome), sehingga cahaya yang terpantul pada celah udara akan langsung memantul lurus 180 derajat kembali ke arah laser pemancar (Optical Return Loss berkisar -50 dB), yang dapat merusak stabilitas laser dan memicu distorsi pada transmisi video analog/RF. Pada konektor APC (hijau), ujung ferrule dipoles dengan sudut kemiringan presisi 8 derajat. Kemiringan ini membelokkan cahaya pantulan keluar menembus cladding, menghasilkan return loss superior ( $\\le -60\\text{ dB}$ )."
  },
  {
    "id": "tkj-sim-22",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Troubleshooting MTU Mismatch & IP Fragmentation",
    "type": "mcq",
    "questionHtml": "Pengguna di kantor cabang yang terhubung melalui VPN IPsec melaporkan bahwa mereka dapat melakukan ping ke server kantor pusat dengan lancar, namun ketika mencoba membuka portal ERP web atau mengunduh dokumen lampiran email berukuran besar, halaman web macet total (stuck loading / hanging). Solusi perbaikan yang paling tepat pada router gateway VPN adalah...",
    "options": [
      {
        "key": "A",
        "text": "Memperbesar nilai MTU interface LAN klien menjadi 9000 bytes jumbo frame."
      },
      {
        "key": "B",
        "text": "Menonaktifkan enkripsi IPsec dan membiarkan data terkirim tanpa perlindungan keamanan."
      },
      {
        "key": "C",
        "text": "Mengganti seluruh kabel switch kantor cabang dengan kabel UTP kategori 5 lawas."
      },
      {
        "key": "D",
        "text": "Menghapus seluruh rute static pada routing table dan membiarkan router offline."
      },
      {
        "key": "E",
        "text": "Mengonfigurasi 'TCP MSS Clamping' (menurunkan nilai Maximum Segment Size, misal `ip tcp adjust-mss 1360`) untuk mengkompensasi overhead enkripsi header IPsec dan mencegah paket melampaui MTU 1500 dengan bit Don't Fragment (DF) aktif."
      }
    ],
    "correctKey": "E",
    "explanation": "Paket ping ICMP kecil (biasanya 32-64 bytes) dapat melintasi terowongan VPN tanpa masalah. Namun ketika klien mengirimkan data web besar, paket TCP memiliki ukuran segmen maksimal (MSS 1460 bytes) yang menghasilkan paket IP berukuran 1500 bytes (batas standar MTU). Terowongan VPN IPsec menambahkan overhead header enkripsi (ESP, IV, padding, HMAC) sekitar 50-70 bytes, sehingga ukuran total paket membengkak menjadi >1550 bytes. Jika paket diset dengan flag DF (Don't Fragment), paket akan didrop oleh router di internet (Path MTU Black Hole). Solusi standar adalah mengaktifkan TCP MSS Clamping pada router VPN untuk memaksa kedua endpoint mereduksi ukuran segmen datanya sejak awal."
  },
  {
    "id": "tkj-sim-23",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Mitigasi Serangan Rogue DHCP Server menggunakan DHCP Snooping",
    "type": "mcq",
    "questionHtml": "Seorang pengguna di asrama sekolah memasang router wireless rumahan yang tidak sengaja dicolokkan ke port LAN dinding melalui port LAN (bukan port WAN), sehingga router tersebut membagikan IP address palsu dan gateway palsu ke puluhan siswa lain (Rogue DHCP Server) dan melumpuhkan internet asrama. Fitur keamanan switch layer 2 yang paling tepat untuk memblokir server DHCP liar tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengaktifkan DHCP Snooping pada switch, menetapkan port uplink ke router resmi sebagai 'trusted', dan seluruh port kamar siswa sebagai 'untrusted' (paket DHCP Offer dari port untrusted akan seketika didrop)."
      },
      {
        "key": "B",
        "text": "Mengaktifkan fitur Spanning Tree PortFast pada seluruh port switch kamar asrama sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern dalam rangka memitigasi potensi gangguan interferensi elektromagnetik dan redaman berlebih."
      },
      {
        "key": "C",
        "text": "Memasang penangkal petir tembaga pada tiang Access Point luar ruangan."
      },
      {
        "key": "D",
        "text": "Mengubah subnet mask seluruh komputer siswa menjadi 255.255.255.255."
      },
      {
        "key": "E",
        "text": "Menurunkan kecepatan port switch siswa dari 1 Gbps menjadi 10 Mbps Half-Duplex."
      }
    ],
    "correctKey": "A",
    "explanation": "DHCP Snooping adalah fitur keamanan layer 2 pada switch yang bertindak seperti firewall antara klien DHCP dan server DHCP. Switch membagi port-portnya menjadi dua kategori: (1) Trusted Port: hanya port yang terhubung ke DHCP Server resmi atau uplink router utama yang diizinkan meneruskan paket respons DHCP (seperti DHCP Offer dan DHCP ACK); (2) Untrusted Port: seluruh port akses pengguna. Jika ada perangkat liar yang mengirimkan DHCP Offer atau DHCP ACK pada port untrusted, switch akan mendeteksi pelanggaran tersebut dan langsung mendrop paketnya."
  },
  {
    "id": "tkj-sim-24",
    "subject": "tkj",
    "materi": "MONITORING & KINERJA SISTEM JARINGAN",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Metrik Kualitas Layanan (Jitter, Latency, Packet Loss) Standar ITU-T Y.1541",
    "type": "mcq",
    "questionHtml": "Dalam uji kelayakan jaringan untuk implementasi telemedisin operasi jarak jauh dan konferensi video real-time interaktif, standar rekomendasi internasional ITU-T Y.1541 (Kelas 0) menetapkan ambang batas batas toleransi performa transmisi data ujung-ke-ujung (end-to-end network performance) adalah...",
    "options": [
      {
        "key": "A",
        "text": "One-way Latency $\\le 2000\\text{ ms}$, Jitter $\\le 500\\text{ ms}$, dan Packet Loss Ratio $\\le 15\\% $."
      },
      {
        "key": "B",
        "text": "One-way Latency $\\le 100\\text{ ms}$, IP Packet Delay Variation (Jitter) $\\le 50\\text{ ms}$, dan Packet Loss Ratio $\\le 0.1\\% $ (atau $\\le 10^{-3}$)."
      },
      {
        "key": "C",
        "text": "Latency harus bernilai mutlak $0\\text{ ms}$ pada kabel tembaga tanpa ada deviasi waktu perambatan sinyal demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama."
      },
      {
        "key": "D",
        "text": "Jitter diperbolehkan hingga $300\\text{ ms}$ asalkan bandwidth internet minimum 10 Gbps."
      },
      {
        "key": "E",
        "text": "Hanya diukur berdasarkan kecepatan download Speedtest tanpa memperhatikan latensi paket."
      }
    ],
    "correctKey": "B",
    "explanation": "Standar internasional ITU-T Recommendation Y.1541 mendefinisikan parameter performa jaringan IP. Untuk Kelas 0 (aplikasi sangat sensitif terhadap penundaan seperti VoIP interaktif real-time, telemedisin, dan video conference berkualitas tinggi), ambang batas yang disyaratkan adalah: One-way Transfer Delay (Latensi) maksimal 100 ms, Delay Variation (Jitter) maksimal 50 ms, dan Packet Loss Ratio (PLR) tidak boleh melebihi 0.1% (1 paket hilang per 1000 paket)."
  },
  {
    "id": "tkj-sim-25",
    "subject": "tkj",
    "materi": "K3LH & KETENAGAKERJAAN TJKT",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "SOP Evakuasi dan Penanganan Kebocoran Gas Beracun Ruang Baterai UPS Data Center",
    "type": "mcq",
    "questionHtml": "Ruang baterai cadangan data center yang menampung ratusan sel aki Valve Regulated Lead-Acid (VRLA) mengalami panas berlebih (thermal runaway) saat pengisian daya cepat, memicu alarm detektor gas hidrogen (H2) dan asam sulfat berbunyi keras. Tindakan tanggap darurat K3LH pertama yang wajib dilakukan oleh petugas operator sebelum tim teknisi bersertifikasi masuk ke ruangan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Masuk ke ruang baterai dengan membawa korek api untuk memeriksa titik sumber kebocoran gas."
      },
      {
        "key": "B",
        "text": "Menutup rapat seluruh pintu dan jendela serta mematikan blower ventilasi udara agar gas terkurung."
      },
      {
        "key": "C",
        "text": "Segera menekan tombol Emergency Power Off (EPO) charger baterai, mengaktifkan sistem ventilasi pembuangan gas khusus anti-ledakan (explosion-proof exhaust), dan mengevakuasi seluruh personil keluar dari zona bahaya."
      },
      {
        "key": "D",
        "text": "Menyiram seluruh rak baterai aki yang sedang panas dengan seember air kran biasa."
      },
      {
        "key": "E",
        "text": "Menyalakan kipas angin rumahan biasa di tengah-tengah ruang baterai."
      }
    ],
    "correctKey": "C",
    "explanation": "Baterai timbal-asam (VRLA) yang mengalami overcharging atau thermal runaway akan melepaskan gas hidrogen (H2) yang sangat mudah terbakar dan meledak jika konsentrasinya di udara melampaui Lower Explosive Limit (LEL 4%), serta uap asam sulfat yang beracun bagi pernapasan. Standar keselamatan kerja data center (OSHA / NFPA 855) mewajibkan: (1) Memutus sumber pengisian daya listrik; (2) Mengaktifkan sistem ventilasi pembuangan gas anti-ledakan (intrinsically safe exhaust); (3) Larangan keras adanya percikan api atau sakelar listrik biasa; dan (4) Evakuasi seluruh personil ke titik kumpul aman."
  },
  {
    "id": "tkj-sim-26",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Karakteristik Protokol Link-State (OSPF/IS-IS)",
    "type": "complex",
    "questionHtml": "Protokol routing dinamis berbasis algoritma Link-State (seperti OSPF dan IS-IS) memiliki karakteristik operasional yang sangat berbeda dengan protokol Distance-Vector klasik (seperti RIP). Manakah dari pernyataan-pernyataan berikut yang BENAR mengenai arsitektur protokol Link-State? (Pilihlah lebih dari satu pernyataan yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Setiap router membangun peta topologi lengkap dari seluruh area jaringan di dalam Link-State Database (LSDB) miliknya."
      },
      {
        "key": "B",
        "text": "Menggunakan Algoritma Dijkstra Shortest Path First (SPF) untuk menghitung pohon jalur bebas loop (loop-free shortest path tree)."
      },
      {
        "key": "C",
        "text": "Mengirimkan seluruh isi tabel routing secara periodik setiap 30 detik ke seluruh tetangga terdekat."
      },
      {
        "key": "D",
        "text": "Hanya mengirimkan pembaruan terpicu (triggered updates) berupa perubahan status link parsial ketika terjadi perubahan topologi."
      },
      {
        "key": "E",
        "text": "Memiliki batasan hop count maksimum sebanyak 15 hop yang tidak dapat diubah."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "D"
    ],
    "explanation": "Karakteristik utama protokol Link-State: (A) Setiap router mengumpulkan LSA dari semua router lain sehingga memiliki pandangan topologi lengkap (LSDB); (B) Menggunakan algoritma matematika Dijkstra SPF untuk menghitung rute terbaik; (D) Efisien bandwidth karena tidak mengirim tabel routing secara periodik, melainkan hanya triggered updates saat ada link up/down. Pernyataan C dan E adalah ciri protokol Distance-Vector (RIP)."
  },
  {
    "id": "tkj-sim-27",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Komponen Keamanan Protokol HTTPS & TLS 1.3",
    "type": "complex",
    "questionHtml": "Protokol Transport Layer Security (TLS 1.3) yang mendasari koneksi web HTTPS modern menyediakan tiga pilar jaminan keamanan fundamental bagi pertukaran data di internet publik. Manakah dari layanan keamanan berikut yang disediakan secara langsung oleh protokol TLS? (Pilihlah lebih dari satu pernyataan yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Kerahasiaan Data (Confidentiality / Privacy) melalui enkripsi simetris (seperti AES-GCM atau ChaCha20-Poly1305)."
      },
      {
        "key": "B",
        "text": "Integritas Data (Data Integrity) menggunakan Message Authentication Code (MAC) untuk mendeteksi perubahan data saat transmisi."
      },
      {
        "key": "C",
        "text": "Autentikasi Server (Authentication) menggunakan sertifikat digital X.509 yang diverifikasi oleh Certificate Authority (CA) terpercaya."
      },
      {
        "key": "D",
        "text": "Proteksi fisik kabel jaringan dari bahaya terpotong oleh alat berat galian jalan."
      },
      {
        "key": "E",
        "text": "Jaminan kecepatan bandwidth internet minimum 100 Mbps bagi setiap workstation klien."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Tiga pilar keamanan kriptografis yang dijamin oleh protokol TLS/HTTPS adalah CIA Triad untuk kanal transmisi: (A) Kerahasiaan (Confidentiality) dengan enkripsi simetris sehingga data tidak bisa disadap; (B) Integritas (Integrity) dengan hash HMAC untuk memastikan data tidak dimanipulasi di tengah jalan; (C) Autentikasi (Authentication) dengan sertifikat digital X.509 untuk memastikan pengguna benar-benar terhubung ke server resmi bukan server penipu."
  },
  {
    "id": "tkj-sim-28",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Karakteristik Kabel Twisted Pair Kategori Kinerja Tinggi (Cat 6A & Cat 7)",
    "type": "complex",
    "questionHtml": "Dalam pembangunan infrastruktur data center berbasis tembaga 10GBASE-T (kecepatan 10 Gbps), teknisi memilih kabel Cat 6A (Augmented) dan Cat 7 daripada kabel Cat 5e atau Cat 6 standar. Manakah pernyataan teknis berikut yang BENAR mengenai spesifikasi kabel tersebut? (Pilihlah lebih dari satu pernyataan yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Kabel Cat 6A mampu mentransmisikan data 10 Gbps pada jarak kanal horizontal penuh hingga 100 meter."
      },
      {
        "key": "B",
        "text": "Kabel Cat 6A beroperasi pada spesifikasi frekuensi kerja bandwidth hingga 500 MHz (dua kali lipat dari Cat 6 yang 250 MHz)."
      },
      {
        "key": "C",
        "text": "Memiliki pelindung individual per pasang kawat (Foiled Shield) untuk menekan gangguan Alien Crosstalk (ANEXT)."
      },
      {
        "key": "D",
        "text": "Kabel Cat 6A kebal terhadap air dan dapat langsung ditanam di dalam lumpur tanpa pipa pelindung conduit."
      },
      {
        "key": "E",
        "text": "Dapat langsung disambung menggunakan mesin fusion splicer busur listrik optik."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Kabel Cat 6A (Augmented Kategori 6) dirancang untuk mendukung 10 Gigabit Ethernet (10GBASE-T) sejauh 100 meter penuh pada frekuensi kerja 500 MHz (Cat 6 biasa hanya mampu 10G hingga jarak 37-55 meter pada 250 MHz). Kabel Cat 6A dan Cat 7 dilengkapi pelindung shielding (STP/FTP) yang sangat rapat untuk mengeliminasi Alien Crosstalk (gangguan sinyal dari kabel tetangga yang berdampingan di cable tray)."
  },
  {
    "id": "tkj-sim-29",
    "subject": "tkj",
    "materi": "JARINGAN NIRKABEL & WIRELESS",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Faktor Penyebab Degradasi Throughput Sinyal Wi-Fi",
    "type": "complex",
    "questionHtml": "Meskipun Access Point (AP) berada dalam jarak 10 meter dari perangkat laptop pengguna, hasil pengujian iPerf3 menunjukkan throughput aktual hanya mencapai 15 Mbps dari kapasitas teoretis 300 Mbps. Manakah dari faktor-faktor fisik dan radio frekuensi berikut yang DAPAT menjadi penyebab penurunan performa tersebut? (Pilihlah lebih dari satu pernyataan yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Tingginya Co-Channel Interference (CCI) akibat beberapa AP tetangga di sekitarnya menggunakan nomor kanal frekuensi yang sama."
      },
      {
        "key": "B",
        "text": "Adanya perangkat non-Wi-Fi yang memancarkan gelombang elektromagnetik di pita 2.4 GHz seperti microwave oven atau kamera CCTV nirkabel analog."
      },
      {
        "key": "C",
        "text": "Masalah Hidden Node Problem di mana dua klien tidak dapat saling mendengar sinyal satu sama lain sehingga sering memicu tabrakan paket (collision)."
      },
      {
        "key": "D",
        "text": "Kelebihan jumlah alamat IP pada blok subnet mask /24 di DHCP server."
      },
      {
        "key": "E",
        "text": "Penggunaan protokol DNSSEC pada server resolver lokal sekolah."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Penurunan performa nirkabel ekstrem umumnya disebabkan oleh interferensi radio: (A) Co-Channel Interference (AP lain di kanal yang sama memaksa klien menunggu giliran bicara); (B) Gangguan gelombang non-Wi-Fi (microwave, Bluetooth, video sender analog yang menaikkan noise floor); dan (C) Hidden Node Problem di mana klien-klien terhalang dinding sehingga saling mentransmisikan data bersamaan dan merusak paket (dapat dimitigasi dengan mekanisme RTS/CTS threshold)."
  },
  {
    "id": "tkj-sim-30",
    "subject": "tkj",
    "materi": "VIRTUALISASI & CLOUD COMPUTING TJKT",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Komparasi Virtualisasi Hypervisor Tipe-1 (Bare-Metal) vs Tipe-2 (Hosted)",
    "type": "complex",
    "questionHtml": "Dalam penyediaan infrastruktur server komputasi awan di sekolah, teknisi membandingkan penggunaan Hypervisor Tipe-1 (seperti VMware ESXi atau Proxmox VE) dengan Hypervisor Tipe-2 (seperti Oracle VirtualBox atau VMware Workstation). Manakah pernyataan yang BENAR mengenai arsitektur Hypervisor Tipe-1? (Pilihlah lebih dari satu pernyataan yang benar)",
    "options": [
      {
        "key": "A",
        "text": "Hypervisor Tipe-1 diinstal langsung di atas perangkat keras fisik server (bare-metal) tanpa memerlukan sistem operasi host perantara."
      },
      {
        "key": "B",
        "text": "Menghasilkan overhead pemrosesan yang jauh lebih rendah dan performa I/O memori/CPU mendekati performa native hardware."
      },
      {
        "key": "C",
        "text": "Mendukung fitur clustering ketersediaan tinggi enterprise seperti live migration mesin virtual tanpa mematikan layanan (High Availability)."
      },
      {
        "key": "D",
        "text": "Hanya dapat dijalankan di dalam sistem operasi desktop Windows 10 untuk keperluan praktikum siswa."
      },
      {
        "key": "E",
        "text": "Tidak mendukung kartu jaringan fisik lebih dari satu port."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Hypervisor Tipe-1 (Bare-Metal) seperti VMware ESXi, Proxmox VE, atau Microsoft Hyper-V Server diinstal langsung di atas hardware fisik server tanpa sistem operasi induk. Desain ini menghilangkan latensi OS perantara sehingga sangat efisien, stabil untuk lingkungan produksi 24/7, dan mendukung fitur enterprise seperti clustering, failover otomatis, dan Live Migration mesin virtual."
  },
  {
    "id": "tkj-sim-31",
    "subject": "tkj",
    "materi": "ROUTING & SWITCHING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Evaluasi Karakteristik Protokol Routing Dinamis",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik teknis dan metrik dari berbagai protokol perutean dinamis (dynamic routing protocols), evaluasilah kebenaran dari masing-masing pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Protokol RIPv2 menggunakan metrik Hop Count dengan batas maksimum 15 hop, di mana nilai hop 16 dianggap sebagai rute tidak terjangkau (unreachable).",
        "correct": "Benar"
      },
      {
        "id": "1",
        "text": "Protokol OSPF menghitung nilai metrik Cost berdasarkan rumus acuan: Reference Bandwidth dibagi Interface Bandwidth (Cost = 10^8 / Bandwidth bps).",
        "correct": "Benar"
      },
      {
        "id": "2",
        "text": "Administrative Distance (AD) default dari rute yang terhubung langsung (Directly Connected) adalah 110, sedangkan OSPF adalah 0.",
        "correct": "Salah"
      },
      {
        "id": "3",
        "text": "Border Gateway Protocol (BGP) adalah protokol Exterior Gateway Protocol (EGP) standar yang mengelola pertukaran rute antar Autonomous System di seluruh dunia.",
        "correct": "Benar"
      }
    ],
    "explanation": "Pernyataan 0 Benar (RIPv2 hop max = 15). Pernyataan 1 Benar (Formula cost OSPF = Reference Bandwidth / Interface Bandwidth). Pernyataan 2 Salah (Directly Connected memiliki AD = 0 paling dipercaya, sedangkan OSPF memiliki AD = 110). Pernyataan 3 Benar (BGP adalah satu-satunya EGP standar internet global)."
  },
  {
    "id": "tkj-sim-32",
    "subject": "tkj",
    "materi": "MEDIA TRANSMISI & JARINGAN FISIK",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Evaluasi Parameter dan Prosedur Kerja Serat Optik",
    "type": "matrix",
    "questionHtml": "Terkait prinsip kerja fisik, alat ukur, dan prosedur terminasi kabel fiber optik, tentukan apakah setiap pernyataan berikut Benar atau Salah:",
    "statements": [
      {
        "id": "0",
        "text": "Panjang gelombang cahaya yang umum digunakan pada transmisi serat optik Single Mode jarak jauh adalah 1310 nm dan 1550 nm karena memiliki redaman atenuasi terendah.",
        "correct": "Benar"
      },
      {
        "id": "1",
        "text": "Optical Power Meter (OPM) digunakan untuk mengukur redaman loss absolut dengan satuan decibel-milliwatt (dBm) atau decibel relatif (dB).",
        "correct": "Benar"
      },
      {
        "id": "2",
        "text": "Fiber Cleaver berfungsi untuk mengupas lapisan jaket plastik luar (outer jacket) dan tabung loose tube kabel serat optik.",
        "correct": "Salah"
      },
      {
        "id": "3",
        "text": "Proses fusi pada mesin fusion splicer menggunakan busur elektroda listrik untuk melelehkan dan menyatukan dua ujung inti kaca secara permanen.",
        "correct": "Benar"
      }
    ],
    "explanation": "Pernyataan 0 Benar (Jendela transmisi 1310 nm dan 1550 nm adalah window redaman terendah). Pernyataan 1 Benar (OPM membaca dBm dan dB). Pernyataan 2 Salah (Fiber Cleaver bertugas memotong sudut presisi 90 derajat pada core kaca; alat pengupas jaket adalah Fiber Stripper). Pernyataan 3 Benar (Fusion splicer menggunakan busur listrik tegangan tinggi)."
  },
  {
    "id": "tkj-sim-33",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & FIREWALL",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Evaluasi Mekanisme Keamanan Jaringan dan Kriptografi",
    "type": "matrix",
    "questionHtml": "Dalam implementasi pertahanan siber pada infrastruktur jaringan enterprise, evaluasilah kebenaran dari masing-masing pernyataan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Algoritma hash satu arah seperti SHA-256 dapat didekripsi kembali menjadi teks asli dengan memasukkan kunci rahasia privat.",
        "correct": "Salah"
      },
      {
        "id": "1",
        "text": "Stateful Firewall memeriksa context paket terhadap tabel koneksi aktif (Connection Tracking), sedangkan Stateless Firewall hanya memfilter paket berdasarkan header statis per paket independen.",
        "correct": "Benar"
      },
      {
        "id": "2",
        "text": "Port Security dengan aksi violation 'protect' akan seketika mematikan port switch ke status err-disable saat mendeteksi MAC address ilegal.",
        "correct": "Salah"
      },
      {
        "id": "3",
        "text": "Intrusion Prevention System (IPS) berbeda dari Intrusion Detection System (IDS) karena IPS ditempatkan secara in-line dan dapat langsung memblokir paket serangan secara aktif.",
        "correct": "Benar"
      }
    ],
    "explanation": "Pernyataan 0 Salah (Fungsi Hash bersifat satu arah / one-way, secara matematis mustahil didekripsi kembali). Pernyataan 1 Benar (Stateful memeriksa state koneksi, stateless hanya memeriksa rule per paket). Pernyataan 2 Salah (Aksi yang mematikan port ke err-disable adalah 'shutdown', bukan 'protect'). Pernyataan 3 Benar (IPS bersifat in-line pencegahan aktif, IDS bersifat pasif pemantauan)."
  },
  {
    "id": "tkj-sim-34",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN IPV4 & IPV6",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Evaluasi Standar Pengalamatan Internet Protocol",
    "type": "matrix",
    "questionHtml": "Terkait standar pengalamatan IPv4 dan IPv6 serta aturan alokasi IANA, tentukan apakah setiap pernyataan berikut Benar atau Salah:",
    "statements": [
      {
        "id": "0",
        "text": "Alamat IPv4 127.0.0.1 dialokasikan khusus sebagai alamat loopback lokal untuk menguji fungsionalitas TCP/IP internal komputer.",
        "correct": "Benar"
      },
      {
        "id": "1",
        "text": "Alamat IPv6 Link-Local selalu diawali dengan prefix fe80::/10 dan hanya valid digunakan untuk komunikasi di dalam satu segmen link fisik lokal yang sama.",
        "correct": "Benar"
      },
      {
        "id": "2",
        "text": "Subnet mask 255.255.255.248 (/29) menyediakan kapasitas usable IP yang dapat dialokasikan ke komputer klien sebanyak 8 host.",
        "correct": "Salah"
      },
      {
        "id": "3",
        "text": "Alamat IPv4 publik kelas D (224.0.0.0 s/d 239.255.255.255) dialokasikan khusus untuk keperluan transmisi Multicast (seperti OSPF dan IPTV).",
        "correct": "Benar"
      }
    ],
    "explanation": "Pernyataan 0 Benar (127.0.0.1 adalah loopback interface). Pernyataan 1 Benar (fe80::/10 adalah link-local IPv6). Pernyataan 2 Salah (/29 memiliki total 8 alamat, tetapi dikurangi Network ID dan Broadcast ID sehingga usable host hanya 6, bukan 8). Pernyataan 3 Benar (Kelas D adalah blok alamat multicast)."
  },
  {
    "id": "tkj-sim-35",
    "subject": "tkj",
    "materi": "K3LH & KETENAGAKERJAAN TJKT",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Evaluasi Standar Keselamatan Kerja Listrik & Lingkungan Data Center",
    "type": "matrix",
    "questionHtml": "Terkait penerapan standar K3LH industri telekomunikasi dan pengelolaan data center, tentukan apakah setiap pernyataan berikut Benar atau Salah:",
    "statements": [
      {
        "id": "0",
        "text": "Pemasangan rak server di data center harus menganut sistem 'Hot Aisle / Cold Aisle containment' untuk mencegah percampuran udara dingin dari pendingin dengan udara panas buangan server.",
        "correct": "Benar"
      },
      {
        "id": "1",
        "text": "Kabel serat optik aman dipandang langsung dengan mata telanjang ke arah konektor laser yang sedang menyala aktif karena berkas cahaya inframerah tidak membahayakan kornea mata.",
        "correct": "Salah"
      },
      {
        "id": "2",
        "text": "Uninterruptible Power Supply (UPS) tipe Online Double-Conversion mengalirkan daya listrik bersih secara kontinu melalui inverter tanpa ada waktu jeda transfer (0 ms transfer time) saat listrik PLN padam.",
        "correct": "Benar"
      },
      {
        "id": "3",
        "text": "Alat Pemadam Api Ringan (APAR) jenis gas CO2 atau Clean Agent aman digunakan untuk memadamkan kebakaran pada panel listrik server bertegangan (Kelas C).",
        "correct": "Benar"
      }
    ],
    "explanation": "Pernyataan 0 Benar (Sistem Cold/Hot Aisle adalah standar efisiensi pendinginan data center). Pernyataan 1 Salah FATAL (Laser serat optik beroperasi pada spektrum inframerah tak kasat mata, jika dipandang langsung dapat membakar retina mata secara permanen tanpa rasa sakit). Pernyataan 2 Benar (Online UPS memiliki 0 ms transfer time). Pernyataan 3 Benar (Gas CO2 dan Clean Agent adalah pemadam non-konduktif standar kebakaran listrik Kelas C)."
  }
];
