# -*- coding: utf-8 -*-
"""
tkj_data_simulasi.py
35 Unique Authentic Simulasi CBT HOTS Items for TKA 2026 Teknik Jaringan Komputer dan Telekomunikasi (TJKT / TKJ).
Strictly aligned with Pusmendik TKA 2026 & BSKAP 033/H/KR/2024.
25 MCQ Single + 5 Complex Multi-select + 5 Matrix True/False.
Zero AI Slop - Zero Duplicates.
"""

TKJ_SIMULASI = [
    # =========================================================================
    # PART 1: 25 PILIHAN GANDA TUNGGAL (HOTS INDUSTRIAL CASE STUDIES)
    # =========================================================================
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
            {"key": "A", "text": "Ketidakcocokan nilai Maximum Transmission Unit (MTU) pada antarmuka kedua router yang bertetangga."},
            {"key": "B", "text": "Perbedaan nomor OSPF Process ID yang dikonfigurasikan pada kedua perangkat router."},
            {"key": "C", "text": "Router ID pada kedua router memiliki nilai yang sama persis (Router ID conflict)."},
            {"key": "D", "text": "Perbedaan waktu sistem (NTP clock drift) antara kedua router melebihi 10 detik."},
            {"key": "E", "text": "Kabel serat optik yang digunakan mengalami pelemahan daya (loss) sebesar 0.2 dB."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Attenuation Dead Zone (ADZ) dan Event Dead Zone (EDZ) yang diakibatkan saturasi fotodetektor oleh pantulan Fresnel konektor awal."},
            {"key": "B", "text": "Dispersi polarisasi mode akibat medan gravitasi bumi pada serat kaca."},
            {"key": "C", "text": "Kerusakan laser dioda pemancar akibat kehabisan baterai lithium OTDR."},
            {"key": "D", "text": "Efek non-linear Raman Scattering yang menyerap daya optik pada frekuensi tinggi."},
            {"key": "E", "text": "Ketiadaan ground listrik pada casing plastik bodi alat ukur OTDR."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Mengubah Native VLAN pada seluruh port trunk menjadi VLAN ID khusus yang tidak digunakan (misal VLAN 999) dan mengaktifkan 'vlan dot1q tag native'."},
            {"key": "B", "text": "Menyetel seluruh port switch menjadi mode trunk dengan Dynamic Trunking Protocol (DTP) aktif."},
            {"key": "C", "text": "Menonaktifkan protokol Spanning Tree pada seluruh switch distribusi dan access."},
            {"key": "D", "text": "Memperpanjang ukuran frame jumbo MTU menjadi 9216 bytes pada port klien."},
            {"key": "E", "text": "Mengganti seluruh kabel UTP dengan kabel koaksial berpelindung ganda."}
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
            {"key": "A", "text": "/31 dengan subnet mask 255.255.255.254 (menyediakan tepat 2 alamat host untuk router-to-router)."},
            {"key": "B", "text": "/30 dengan subnet mask 255.255.255.252 (menyediakan 2 usable host, 1 network ID, dan 1 broadcast ID)."},
            {"key": "C", "text": "/32 dengan subnet mask 255.255.255.255 (khusus host route loopback tunggal)."},
            {"key": "D", "text": "/29 dengan subnet mask 255.255.255.248 (menyediakan 6 usable host)."},
            {"key": "E", "text": "/28 dengan subnet mask 255.255.255.240 (menyediakan 14 usable host)."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "IEEE 802.11r (Fast Transition), 802.11k (Radio Resource Measurement), dan 802.11v (Wireless Network Management)."},
            {"key": "B", "text": "IEEE 802.1D (Spanning Tree), 802.1Q (VLAN Tagging), dan 802.3af (Power over Ethernet)."},
            {"key": "C", "text": "IEEE 802.11b (DSSS 11 Mbps) dan 802.11a (OFDM 54 Mbps)."},
            {"key": "D", "text": "IEEE 802.3ad (Link Aggregation) dan 802.3x (Flow Control)."},
            {"key": "E", "text": "IEEE 802.1X murni tanpa dukungan ekstensi handover nirkabel."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "3 detik (dihitung dari formula: (Burst-Threshold / Burst-Limit) * Burst-Time = (1.5 / 8) * 16 = 3 detik)."},
            {"key": "B", "text": "16 detik penuh sesuai nilai Burst-Time yang ditentukan di antarmuka Winbox."},
            {"key": "C", "text": "8 detik karena kecepatan diturunkan tepat di separuh waktu konfigurasi."},
            {"key": "D", "text": "12 detik karena nilai Max-Limit lebih tinggi daripada Burst-Threshold."},
            {"key": "E", "text": "Kecepatan 8 Mbps bertahan selamanya tanpa pernah diturunkan router."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Prefix jaringan tersebut akan dikenai denda penalti (suppressed) dan disembunyikan dari tabel perutean global internet selama periode penalti tertentu (decay half-life)."},
            {"key": "B", "text": "ISP akan melipatgandakan alokasi bandwidth link hingga link stabil kembali."},
            {"key": "C", "text": "Router border BGP akan secara otomatis beralih menggunakan protokol routing RIPv2."},
            {"key": "D", "text": "Seluruh konfigurasi router lokal akan terhapus dan kembali ke setelan pabrik default."},
            {"key": "E", "text": "Sesi BGP dialihkan secara otomatis menggunakan kabel telepon analog PSTN."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "DNSSEC (Domain Name System Security Extensions) berbasis verifikasi rantai RRSIG dan DNSKEY."},
            {"key": "B", "text": "DHCP Snooping yang memblokir kueri UDP port 53 pada access port switch."},
            {"key": "C", "text": "Dynamic Host Configuration Protocol Option 82 pada server gateway."},
            {"key": "D", "text": "Spanning Tree Protocol PortFast BPDU Filter pada router border."},
            {"key": "E", "text": "NAT Masquerade dengan memodifikasi field checksum header IP."}
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
            {"key": "A", "text": "-19.0 dBm (berada dalam rentang sensitivitas ideal ONT GPON kelas B+ yaitu -8 s/d -27 dBm)."},
            {"key": "B", "text": "-35.0 dBm (mengalami loss berlebih sehingga ONT masuk status Loss of Signal / LOS merah)."},
            {"key": "C", "text": "-5.5 dBm (sinyal terlalu kuat sehingga merusak modul fotodetektor receiver ONT)."},
            {"key": "D", "text": "+1.5 dBm (mengindikasikan terjadinya penguatan daya optik pasif di dalam splitter)."},
            {"key": "E", "text": "-12.0 dBm (daya terukur tidak dipengaruhi oleh keberadaan splitter optik)."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Mekanisme Proposal-Agreement Handshake yang mengeksekusi sinkronisasi status port secara langsung antar dua switch tetangga."},
            {"key": "B", "text": "Penghapusan seluruh tabel MAC Address secara otomatis setiap terjadi perubahan topologi fisik."},
            {"key": "C", "text": "Penggunaan protokol routing dinamis OSPF di layer 2 untuk menghitung rute frame terpendek."},
            {"key": "D", "text": "Pengecekan arus listrik tegangan port switch menggunakan sensor resistansi tembaga."},
            {"key": "E", "text": "Pendelegasian seluruh kalkulasi pohon topologi jaringan ke server cloud internet eksternal."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "TCP SYN Stealth Scan (Nmap flag -sS / Half-Open Scanning) untuk mendeteksi port terbuka tanpa menyelesaikan handshake 3 arah penuh sehingga tidak tercatat di log aplikasi server."},
            {"key": "B", "text": "TCP Connect Scan murni yang membuka sesi soket penuh dengan pustaka standar OS."},
            {"key": "C", "text": "UDP Flooding attack yang bertujuan melumpuhkan bandwidth antarmuka server."},
            {"key": "D", "text": "Serangan SQL Injection berbasis boolean blind pada formulir autentikasi web."},
            {"key": "E", "text": "Percobaan sinkronisasi waktu jaringan menggunakan protokol Network Time Protocol (NTP)."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Nginx (sebagai proxy) gagal berkomunikasi atau tidak menerima respons yang valid dari server aplikasi upstream (PHP-FPM socket / Node.js port 3000 down atau hang)."},
            {"key": "B", "text": "File index.html tidak ditemukan pada direktori penyimpanan dokumen server (Not Found)."},
            {"key": "C", "text": "Sertifikat SSL/TLS domain telah kedaluwarsa sehingga koneksi HTTPS dihentikan browser."},
            {"key": "D", "text": "Pengguna salah memasukkan username dan password pada halaman form login pengguna."},
            {"key": "E", "text": "Klien menggunakan browser versi lama yang tidak mendukung format gambar WebP."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Router BGP akan membuang (drop/ignore) setiap pengumuman rute yang memuat nomor Autonomous System (AS)-nya sendiri di dalam atribut AS Path."},
            {"key": "B", "text": "Router BGP menghitung nilai hop count maksimum yang tidak boleh melebihi 15 hop seperti RIP."},
            {"key": "C", "text": "Router BGP memverifikasi keaslian paket menggunakan tanda tangan token JWT di setiap payload."},
            {"key": "D", "text": "Seluruh update rute BGP wajib dilewatkan melalui kabel optik bawah laut Samudra Pasifik."},
            {"key": "E", "text": "Setiap sesi BGP diputus paksa dan dinegosiasikan ulang setiap interval 60 detik."}
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
            {"key": "A", "text": "VPN tradisional memberikan akses penuh ke seluruh subnet LAN setelah terhubung (castle-and-moat), sedangkan ZTNA menerapkan prinsip 'never trust, always verify' dengan memberikan akses mikrosegmentasi hanya ke aplikasi spesifik yang diizinkan."},
            {"key": "B", "text": "VPN menggunakan enkripsi kriptografi sedangkan ZTNA menolak enkripsi data untuk mempercepat transmisi."},
            {"key": "C", "text": "ZTNA hanya dapat diakses menggunakan komputer mainframe tanpa dukungan perangkat smartphone."},
            {"key": "D", "text": "VPN tradisional tidak memerlukan alamat IP publik sedangkan ZTNA mewajibkan IP statis di setiap laptop."},
            {"key": "E", "text": "ZTNA menghapus seluruh sistem firewall fisik dan menggantinya dengan sakelar listrik manual."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Neighbor Solicitation (NS menggunakan multicast solicited-node) dan Neighbor Advertisement (NA)."},
            {"key": "B", "text": "Router Solicitation (RS) dan Router Advertisement (RA)."},
            {"key": "C", "text": "Echo Request (Type 128) dan Echo Reply (Type 129)."},
            {"key": "D", "text": "DHCPv6 Solicit dan DHCPv6 Advertise."},
            {"key": "E", "text": "IGMP Membership Report dan IGMP Leave Group."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Terjadi Macrobending Loss di mana sudut datang cahaya melampaui sudut kritis pantulan total (Total Internal Reflection), sehingga sebagian berkas cahaya bocor menembus lapisan cladding ke udara."},
            {"key": "B", "text": "Kabel serat optik akan mengalirkan arus listrik induksi ke casing server rack."},
            {"key": "C", "text": "Panjang gelombang cahaya laser akan bergeser dari 1310 nm menjadi sinar ultraviolet."},
            {"key": "D", "text": "Diameter inti serat kaca akan meleleh secara otomatis akibat tekanan udara."},
            {"key": "E", "text": "Kecepatan transfer data bit rate jaringan meningkat dua kali lipat akibat pemampatan gelombang."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Setiap switch Leaf terhubung langsung ke seluruh switch Spine, menjamin jarak hop yang seragam (tepat 2 hop antar server) dengan latensi rendah dan pemanfaatan seluruh link aktif via Equal-Cost Multi-Path (ECMP)."},
            {"key": "B", "text": "Menghilangkan seluruh kebutuhan switch fisik dengan menghubungkan kabel server langsung ke router gateway internet."},
            {"key": "C", "text": "Mengandalkan protokol Spanning Tree klasik untuk mematikan 50% link redundansi demi mencegah loop."},
            {"key": "D", "text": "Membatasi kecepatan transfer data antar server maksimum tepat 10 Mbps untuk penghematan listrik."},
            {"key": "E", "text": "Hanya memperbolehkan satu server aktif dalam satu rak server secara bergantian."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Gratuitous ARP (GARP) / Address Collision Detection (ACD) yang dibroadcast oleh host untuk memeriksa apakah ada perangkat lain yang menjawab kepemilikan IP tersebut."},
            {"key": "B", "text": "Query DNS rekursif ke root-servers.net yang memvalidasi sertifikat hardware."},
            {"key": "C", "text": "Paket ICMP Echo Request yang dikirimkan oleh switch access ke cloud provider."},
            {"key": "D", "text": "Pengecekan lisensi Windows Defender melalui port TCP 445 SMB share."},
            {"key": "E", "text": "Pemindaian port SSH otomatis menggunakan script Python di background kernel."}
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
            {"key": "A", "text": "IP Spoofing (memalsukan IP sumber kueri DNS menjadi IP publik korban) dipadukan dengan kueri tipe 'ANY' atau DNSSEC berukuran besar ke Open Resolver (faktor amplifikasi 50x hingga 100x)."},
            {"key": "B", "text": "Pencurian password admin router melalui jalur koneksi console serial RS-232 fisik."},
            {"key": "C", "text": "Pengiriman virus macro melalui lampiran email Microsoft Word ke komputer kepala sekolah."},
            {"key": "D", "text": "Pemberian tegangan listrik berlebih melalui kabel Power over Ethernet ke switch access."},
            {"key": "E", "text": "Manipulasi frekuensi radio Access Point dari 2.4 GHz menjadi sinyal gelombang radio FM komersial."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "OSPF Virtual Link yang dikonfigurasikan melintasi Area 1 (Transit Area) antara ABR Area 1/2 dengan ABR Area 0/1."},
            {"key": "B", "text": "Mengubah Area 2 menjadi Totally Stubby Area tanpa default route."},
            {"key": "C", "text": "Mengaktifkan protokol routing RIPv1 pada antarmuka penghubung kedua area."},
            {"key": "D", "text": "Menghapus seluruh konfigurasi OSPF dan menggantinya dengan bridging layer 2 murni."},
            {"key": "E", "text": "Mengubah router ID kedua ABR menjadi bernilai sama 0.0.0.0."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Sudut kemiringan 8 derajat pada ferrule APC memantulkan cahaya balik (optical return loss) ke dinding cladding, menghasilkan nilai return loss sangat tinggi ( $\\le -60\\text{ dB}$ ) yang melindungi pemancar laser OLT dari kerusakan."},
            {"key": "B", "text": "Konektor APC dapat dipasang secara terbalik tanpa perlu membersihkan debu pada ferrule."},
            {"key": "C", "text": "Konektor APC hijau memiliki diameter inti kaca serat optik yang dua kali lebih lebar daripada UPC biru."},
            {"key": "D", "text": "Konektor APC tidak memerlukan pengunci klip mekanik saat ditancapkan ke adapter."},
            {"key": "E", "text": "Warna hijau menandakan kabel tersebut ramah lingkungan dan bebas dari radiasi elektromagnetik."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Mengonfigurasi 'TCP MSS Clamping' (menurunkan nilai Maximum Segment Size, misal `ip tcp adjust-mss 1360`) untuk mengkompensasi overhead enkripsi header IPsec dan mencegah paket melampaui MTU 1500 dengan bit Don't Fragment (DF) aktif."},
            {"key": "B", "text": "Memperbesar nilai MTU interface LAN klien menjadi 9000 bytes jumbo frame."},
            {"key": "C", "text": "Menonaktifkan enkripsi IPsec dan membiarkan data terkirim tanpa perlindungan keamanan."},
            {"key": "D", "text": "Mengganti seluruh kabel switch kantor cabang dengan kabel UTP kategori 5 lawas."},
            {"key": "E", "text": "Menghapus seluruh rute static pada routing table dan membiarkan router offline."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Mengaktifkan DHCP Snooping pada switch, menetapkan port uplink ke router resmi sebagai 'trusted', dan seluruh port kamar siswa sebagai 'untrusted' (paket DHCP Offer dari port untrusted akan seketika didrop)."},
            {"key": "B", "text": "Mengaktifkan fitur Spanning Tree PortFast pada seluruh port switch kamar asrama."},
            {"key": "C", "text": "Memasang penangkal petir tembaga pada tiang Access Point luar ruangan."},
            {"key": "D", "text": "Mengubah subnet mask seluruh komputer siswa menjadi 255.255.255.255."},
            {"key": "E", "text": "Menurunkan kecepatan port switch siswa dari 1 Gbps menjadi 10 Mbps Half-Duplex."}
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
            {"key": "A", "text": "One-way Latency $\\le 100\\text{ ms}$, IP Packet Delay Variation (Jitter) $\\le 50\\text{ ms}$, dan Packet Loss Ratio $\\le 0.1\\% $ (atau $\\le 10^{-3}$)."},
            {"key": "B", "text": "One-way Latency $\\le 2000\\text{ ms}$, Jitter $\\le 500\\text{ ms}$, dan Packet Loss Ratio $\\le 15\\% $."},
            {"key": "C", "text": "Latency harus bernilai mutlak $0\\text{ ms}$ pada kabel tembaga tanpa ada deviasi waktu perambatan sinyal."},
            {"key": "D", "text": "Jitter diperbolehkan hingga $300\\text{ ms}$ asalkan bandwidth internet minimum 10 Gbps."},
            {"key": "E", "text": "Hanya diukur berdasarkan kecepatan download Speedtest tanpa memperhatikan latensi paket."}
        ],
        "correctKey": "A",
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
            {"key": "A", "text": "Segera menekan tombol Emergency Power Off (EPO) charger baterai, mengaktifkan sistem ventilasi pembuangan gas khusus anti-ledakan (explosion-proof exhaust), dan mengevakuasi seluruh personil keluar dari zona bahaya."},
            {"key": "B", "text": "Masuk ke ruang baterai dengan membawa korek api untuk memeriksa titik sumber kebocoran gas."},
            {"key": "C", "text": "Menutup rapat seluruh pintu dan jendela serta mematikan blower ventilasi udara agar gas terkurung."},
            {"key": "D", "text": "Menyiram seluruh rak baterai aki yang sedang panas dengan seember air kran biasa."},
            {"key": "E", "text": "Menyalakan kipas angin rumahan biasa di tengah-tengah ruang baterai."}
        ],
        "correctKey": "A",
        "explanation": "Baterai timbal-asam (VRLA) yang mengalami overcharging atau thermal runaway akan melepaskan gas hidrogen (H2) yang sangat mudah terbakar dan meledak jika konsentrasinya di udara melampaui Lower Explosive Limit (LEL 4%), serta uap asam sulfat yang beracun bagi pernapasan. Standar keselamatan kerja data center (OSHA / NFPA 855) mewajibkan: (1) Memutus sumber pengisian daya listrik; (2) Mengaktifkan sistem ventilasi pembuangan gas anti-ledakan (intrinsically safe exhaust); (3) Larangan keras adanya percikan api atau sakelar listrik biasa; dan (4) Evakuasi seluruh personil ke titik kumpul aman."
    },

    # =========================================================================
    # PART 2: 5 PILIHAN GANDA KOMPLEKS (MULTI-SELECT / HOTS ADVANCED)
    # =========================================================================
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
            {"key": "A", "text": "Setiap router membangun peta topologi lengkap dari seluruh area jaringan di dalam Link-State Database (LSDB) miliknya."},
            {"key": "B", "text": "Menggunakan Algoritma Dijkstra Shortest Path First (SPF) untuk menghitung pohon jalur bebas loop (loop-free shortest path tree)."},
            {"key": "C", "text": "Mengirimkan seluruh isi tabel routing secara periodik setiap 30 detik ke seluruh tetangga terdekat."},
            {"key": "D", "text": "Hanya mengirimkan pembaruan terpicu (triggered updates) berupa perubahan status link parsial ketika terjadi perubahan topologi."},
            {"key": "E", "text": "Memiliki batasan hop count maksimum sebanyak 15 hop yang tidak dapat diubah."}
        ],
        "correctAnswer": ["A", "B", "D"],
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
            {"key": "A", "text": "Kerahasiaan Data (Confidentiality / Privacy) melalui enkripsi simetris (seperti AES-GCM atau ChaCha20-Poly1305)."},
            {"key": "B", "text": "Integritas Data (Data Integrity) menggunakan Message Authentication Code (MAC) untuk mendeteksi perubahan data saat transmisi."},
            {"key": "C", "text": "Autentikasi Server (Authentication) menggunakan sertifikat digital X.509 yang diverifikasi oleh Certificate Authority (CA) terpercaya."},
            {"key": "D", "text": "Proteksi fisik kabel jaringan dari bahaya terpotong oleh alat berat galian jalan."},
            {"key": "E", "text": "Jaminan kecepatan bandwidth internet minimum 100 Mbps bagi setiap workstation klien."}
        ],
        "correctAnswer": ["A", "B", "C"],
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
            {"key": "A", "text": "Kabel Cat 6A mampu mentransmisikan data 10 Gbps pada jarak kanal horizontal penuh hingga 100 meter."},
            {"key": "B", "text": "Kabel Cat 6A beroperasi pada spesifikasi frekuensi kerja bandwidth hingga 500 MHz (dua kali lipat dari Cat 6 yang 250 MHz)."},
            {"key": "C", "text": "Memiliki pelindung individual per pasang kawat (Foiled Shield) untuk menekan gangguan Alien Crosstalk (ANEXT)."},
            {"key": "D", "text": "Kabel Cat 6A kebal terhadap air dan dapat langsung ditanam di dalam lumpur tanpa pipa pelindung conduit."},
            {"key": "E", "text": "Dapat langsung disambung menggunakan mesin fusion splicer busur listrik optik."}
        ],
        "correctAnswer": ["A", "B", "C"],
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
            {"key": "A", "text": "Tingginya Co-Channel Interference (CCI) akibat beberapa AP tetangga di sekitarnya menggunakan nomor kanal frekuensi yang sama."},
            {"key": "B", "text": "Adanya perangkat non-Wi-Fi yang memancarkan gelombang elektromagnetik di pita 2.4 GHz seperti microwave oven atau kamera CCTV nirkabel analog."},
            {"key": "C", "text": "Masalah Hidden Node Problem di mana dua klien tidak dapat saling mendengar sinyal satu sama lain sehingga sering memicu tabrakan paket (collision)."},
            {"key": "D", "text": "Kelebihan jumlah alamat IP pada blok subnet mask /24 di DHCP server."},
            {"key": "E", "text": "Penggunaan protokol DNSSEC pada server resolver lokal sekolah."}
        ],
        "correctAnswer": ["A", "B", "C"],
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
            {"key": "A", "text": "Hypervisor Tipe-1 diinstal langsung di atas perangkat keras fisik server (bare-metal) tanpa memerlukan sistem operasi host perantara."},
            {"key": "B", "text": "Menghasilkan overhead pemrosesan yang jauh lebih rendah dan performa I/O memori/CPU mendekati performa native hardware."},
            {"key": "C", "text": "Mendukung fitur clustering ketersediaan tinggi enterprise seperti live migration mesin virtual tanpa mematikan layanan (High Availability)."},
            {"key": "D", "text": "Hanya dapat dijalankan di dalam sistem operasi desktop Windows 10 untuk keperluan praktikum siswa."},
            {"key": "E", "text": "Tidak mendukung kartu jaringan fisik lebih dari satu port."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "explanation": "Hypervisor Tipe-1 (Bare-Metal) seperti VMware ESXi, Proxmox VE, atau Microsoft Hyper-V Server diinstal langsung di atas hardware fisik server tanpa sistem operasi induk. Desain ini menghilangkan latensi OS perantara sehingga sangat efisien, stabil untuk lingkungan produksi 24/7, dan mendukung fitur enterprise seperti clustering, failover otomatis, dan Live Migration mesin virtual."
    },

    # =========================================================================
    # PART 3: 5 SOAL MODEL MATRIKS (BENAR / SALAH EVALUATIF)
    # =========================================================================
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
            {"id": "0", "text": "Protokol RIPv2 menggunakan metrik Hop Count dengan batas maksimum 15 hop, di mana nilai hop 16 dianggap sebagai rute tidak terjangkau (unreachable).", "correct": "Benar"},
            {"id": "1", "text": "Protokol OSPF menghitung nilai metrik Cost berdasarkan rumus acuan: Reference Bandwidth dibagi Interface Bandwidth (Cost = 10^8 / Bandwidth bps).", "correct": "Benar"},
            {"id": "2", "text": "Administrative Distance (AD) default dari rute yang terhubung langsung (Directly Connected) adalah 110, sedangkan OSPF adalah 0.", "correct": "Salah"},
            {"id": "3", "text": "Border Gateway Protocol (BGP) adalah protokol Exterior Gateway Protocol (EGP) standar yang mengelola pertukaran rute antar Autonomous System di seluruh dunia.", "correct": "Benar"}
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
            {"id": "0", "text": "Panjang gelombang cahaya yang umum digunakan pada transmisi serat optik Single Mode jarak jauh adalah 1310 nm dan 1550 nm karena memiliki redaman atenuasi terendah.", "correct": "Benar"},
            {"id": "1", "text": "Optical Power Meter (OPM) digunakan untuk mengukur redaman loss absolut dengan satuan decibel-milliwatt (dBm) atau decibel relatif (dB).", "correct": "Benar"},
            {"id": "2", "text": "Fiber Cleaver berfungsi untuk mengupas lapisan jaket plastik luar (outer jacket) dan tabung loose tube kabel serat optik.", "correct": "Salah"},
            {"id": "3", "text": "Proses fusi pada mesin fusion splicer menggunakan busur elektroda listrik untuk melelehkan dan menyatukan dua ujung inti kaca secara permanen.", "correct": "Benar"}
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
            {"id": "0", "text": "Algoritma hash satu arah seperti SHA-256 dapat didekripsi kembali menjadi teks asli dengan memasukkan kunci rahasia privat.", "correct": "Salah"},
            {"id": "1", "text": "Stateful Firewall memeriksa context paket terhadap tabel koneksi aktif (Connection Tracking), sedangkan Stateless Firewall hanya memfilter paket berdasarkan header statis per paket independen.", "correct": "Benar"},
            {"id": "2", "text": "Port Security dengan aksi violation 'protect' akan seketika mematikan port switch ke status err-disable saat mendeteksi MAC address ilegal.", "correct": "Salah"},
            {"id": "3", "text": "Intrusion Prevention System (IPS) berbeda dari Intrusion Detection System (IDS) karena IPS ditempatkan secara in-line dan dapat langsung memblokir paket serangan secara aktif.", "correct": "Benar"}
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
            {"id": "0", "text": "Alamat IPv4 127.0.0.1 dialokasikan khusus sebagai alamat loopback lokal untuk menguji fungsionalitas TCP/IP internal komputer.", "correct": "Benar"},
            {"id": "1", "text": "Alamat IPv6 Link-Local selalu diawali dengan prefix fe80::/10 dan hanya valid digunakan untuk komunikasi di dalam satu segmen link fisik lokal yang sama.", "correct": "Benar"},
            {"id": "2", "text": "Subnet mask 255.255.255.248 (/29) menyediakan kapasitas usable IP yang dapat dialokasikan ke komputer klien sebanyak 8 host.", "correct": "Salah"},
            {"id": "3", "text": "Alamat IPv4 publik kelas D (224.0.0.0 s/d 239.255.255.255) dialokasikan khusus untuk keperluan transmisi Multicast (seperti OSPF dan IPTV).", "correct": "Benar"}
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
            {"id": "0", "text": "Pemasangan rak server di data center harus menganut sistem 'Hot Aisle / Cold Aisle containment' untuk mencegah percampuran udara dingin dari pendingin dengan udara panas buangan server.", "correct": "Benar"},
            {"id": "1", "text": "Kabel serat optik aman dipandang langsung dengan mata telanjang ke arah konektor laser yang sedang menyala aktif karena berkas cahaya inframerah tidak membahayakan kornea mata.", "correct": "Salah"},
            {"id": "2", "text": "Uninterruptible Power Supply (UPS) tipe Online Double-Conversion mengalirkan daya listrik bersih secara kontinu melalui inverter tanpa ada waktu jeda transfer (0 ms transfer time) saat listrik PLN padam.", "correct": "Benar"},
            {"id": "3", "text": "Alat Pemadam Api Ringan (APAR) jenis gas CO2 atau Clean Agent aman digunakan untuk memadamkan kebakaran pada panel listrik server bertegangan (Kelas C).", "correct": "Benar"}
        ],
        "explanation": "Pernyataan 0 Benar (Sistem Cold/Hot Aisle adalah standar efisiensi pendinginan data center). Pernyataan 1 Salah FATAL (Laser serat optik beroperasi pada spektrum inframerah tak kasat mata, jika dipandang langsung dapat membakar retina mata secara permanen tanpa rasa sakit). Pernyataan 2 Benar (Online UPS memiliki 0 ms transfer time). Pernyataan 3 Benar (Gas CO2 dan Clean Agent adalah pemadam non-konduktif standar kebakaran listrik Kelas C)."
    }
]
