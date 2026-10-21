# -*- coding: utf-8 -*-
"""
tkj_data_medium.py
25 Unique Authentic Medium Items for TKA 2026 Teknik Jaringan Komputer dan Telekomunikasi (TJKT / TKJ).
Strictly aligned with Pusmendik TKA 2026 & BSKAP 033/H/KR/2024.
Zero AI Slop - Zero Duplicates.
"""

TKJ_MEDIUM = [
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
            {"key": "A", "text": "Engineering: /23 (maks 510 host), Finance: /25 (maks 126 host), HRD: /26 (maks 62 host)."},
            {"key": "B", "text": "Engineering: /24 (maks 254 host), Finance: /25 (maks 126 host), HRD: /26 (maks 62 host)."},
            {"key": "C", "text": "Engineering: /22 (maks 1022 host), Finance: /24 (maks 254 host), HRD: /25 (maks 126 host)."},
            {"key": "D", "text": "Engineering: /23 (maks 510 host), Finance: /24 (maks 254 host), HRD: /25 (maks 126 host)."},
            {"key": "E", "text": "Engineering: /24 (maks 254 host), Finance: /26 (maks 62 host), HRD: /27 (maks 30 host)."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "-7.0 dBm (total loss saluran = 4.0 dB)."},
            {"key": "B", "text": "-5.8 dBm (total loss saluran = 2.8 dB)."},
            {"key": "C", "text": "-8.2 dBm (total loss saluran = 5.2 dB)."},
            {"key": "D", "text": "-11.0 dBm (total loss saluran = 8.0 dB)."},
            {"key": "E", "text": "-3.8 dBm (total loss saluran = 0.8 dB)."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": True
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
            {"key": "A", "text": "Switch-2, karena memiliki Bridge Priority terkecil (32768) dan nilai MAC Address terendah di antara prioritas yang sama."},
            {"key": "B", "text": "Switch-3, karena memiliki nilai Bridge Priority tertinggi (40960) yang menunjukkan kapasitas pemrosesan paling besar."},
            {"key": "C", "text": "Switch-1, karena memiliki MAC Address dengan nilai hex tertinggi yang menandakan hardware keluaran terbaru."},
            {"key": "D", "text": "Seluruh switch bergantian menjadi Root Bridge setiap interval Hello Time 2 detik secara round-robin."},
            {"key": "E", "text": "Switch-2 dan Switch-1 menjadi dual active root bridge dengan mekanisme Virtual Router Redundancy Protocol."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "interface GigabitEthernet0/0.10 \n encapsulation dot1Q 10 \n ip address 192.168.10.1 255.255.255.0"},
            {"key": "B", "text": "interface GigabitEthernet0/0 \n switchport mode trunk \n switchport trunk allowed vlan 10,20"},
            {"key": "C", "text": "interface GigabitEthernet0/0.10 \n encapsulation isl 10 \n ip address 192.168.10.1 255.255.255.128"},
            {"key": "D", "text": "interface vlan 10 \n ip address 192.168.10.1 255.255.255.0 \n no shutdown"},
            {"key": "E", "text": "interface GigabitEthernet0/0 \n vlan 10 routing enable \n ip default-gateway 192.168.10.1"}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Menetapkan rute ISP-A dengan distance = 1 dan rute ISP-B dengan distance = 2 (atau nilai yang lebih besar)."},
            {"key": "B", "text": "Menetapkan rute ISP-A dengan distance = 250 dan rute ISP-B dengan distance = 1."},
            {"key": "C", "text": "Mengatur kedua rute ISP-A dan ISP-B dengan nilai distance = 1 agar terjadi pembagian beban (load balancing ECMP)."},
            {"key": "D", "text": "Menonaktifkan tabel routing static dan menggantinya dengan bridging port interface ISP-A dan ISP-B."},
            {"key": "E", "text": "Mengatur routing mark pada ISP-B dengan routing table khusus tanpa menentukan default gateway."}
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Nilai OSPF Interface Priority tertinggi (default priority = 1, nilai 0 tidak akan pernah menjadi DR/BDR)."},
            {"key": "B", "text": "Alamat IP host terkecil pada antarmuka LAN yang terhubung langsung."},
            {"key": "C", "text": "Jumlah total rute eksternal yang di-redistribute ke dalam OSPF database."},
            {"key": "D", "text": "Nilai OSPF Process ID terkecil yang dikonfigurasikan administrator pada router."},
            {"key": "E", "text": "Waktu operasional (uptime) perangkat yang paling lama menyala tanpa reboot."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "DHCP Relay (mengubah paket DHCP Discover broadcast dari klien menjadi unicast ke arah IP server 10.10.100.5)."},
            {"key": "B", "text": "Proxy ARP (menjawab seluruh broadcast layer 2 dengan MAC address router gateway)."},
            {"key": "C", "text": "NAT 1-to-1 (memetakan seluruh IP server langsung ke setiap port switch mahasiswa)."},
            {"key": "D", "text": "DNS Forwarder (mengarahkan seluruh kueri nama domain ke server DHCP)."},
            {"key": "E", "text": "IGMP Snooping (membatasi penyebaran paket multicast IPTV di dalam switch)."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "SNR = 25 dB; kualitas sinyal sangat baik untuk throughput tinggi dan streaming video stabil."},
            {"key": "B", "text": "SNR = -155 dB; koneksi terputus total karena berada di bawah ambang batas sinyal minimum."},
            {"key": "C", "text": "SNR = 15 dB; koneksi sangat buruk dan mengalami packet loss ekstrem di atas 50%."},
            {"key": "D", "text": "SNR = -25 dB; sinyal noise lebih kuat daripada sinyal data sehingga terjadi interferensi parah."},
            {"key": "E", "text": "SNR = 65 dB; sinyal terlalu kuat sehingga menimbulkan saturasi pada radio receiver AP."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Chain 'input' (memproses paket yang alamat tujuan IP-nya adalah router itu sendiri)."},
            {"key": "B", "text": "Chain 'forward' (memproses paket data yang hanya melintasi router dari klien ke internet)."},
            {"key": "C", "text": "Chain 'output' (memproses paket yang berasal dari dalam router menuju jaringan luar)."},
            {"key": "D", "text": "Chain 'prerouting' (memproses translasi alamat sebelum keputusan routing diambil)."},
            {"key": "E", "text": "Chain 'postrouting' (memproses masquerade sesaat sebelum paket keluar fisik)." }
        ],
        "correctKey": "A",
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
        "isDiagnostic": True
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
            {"key": "A", "text": "/ip firewall nat add chain=dstnat dst-address=203.0.113.10 protocol=tcp dst-port=80 action=dst-nat to-addresses=192.168.10.80 to-ports=80"},
            {"key": "B", "text": "/ip firewall nat add chain=srcnat src-address=192.168.10.80 action=masquerade to-addresses=203.0.113.10"},
            {"key": "C", "text": "/ip firewall nat add chain=dstnat src-address=203.0.113.10 action=redirect to-ports=80"},
            {"key": "D", "text": "/ip firewall nat add chain=forward in-interface=ether1 protocol=tcp dst-port=80 action=accept"},
            {"key": "E", "text": "/ip firewall nat add chain=srcnat dst-address=192.168.10.80 protocol=tcp action=dst-nat to-ports=8080"}
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
        "isDiagnostic": False
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
            {"key": "A", "text": "~/.ssh/authorized_keys dengan permission 600."},
            {"key": "B", "text": "/etc/ssh/sshd_config dengan permission 777."},
            {"key": "C", "text": "~/.ssh/known_hosts dengan permission 644."},
            {"key": "D", "text": "/var/log/auth.log dengan permission 640."},
            {"key": "E", "text": "~/.ssh/id_rsa dengan permission 700."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "2001:db8::ff00:42:8329"},
            {"key": "B", "text": "2001:db8::ff::42:8329"},
            {"key": "C", "text": "2001:0db8::ff00:0042:8329"},
            {"key": "D", "text": "2001:db8:0:0:0:ff:42:8329"},
            {"key": "E", "text": "2001::db8::ff00:42:8329"}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "PCQ (Per Connection Queue) dengan classifier 'dst-address' untuk download dan 'src-address' untuk upload."},
            {"key": "B", "text": "FIFO (First In First Out) tanpa konfigurasi packet limit maupun rate burst."},
            {"key": "C", "text": "RED (Random Early Detection) untuk menjatuhkan paket TCP secara acak pada buffer penuh."},
            {"key": "D", "text": "SFQ (Stochastic Fairness Queuing) dengan fixed limit tepat 128 Kbps per workstation."},
            {"key": "E", "text": "Simple Queue statis manual yang didaftarkan terpisah sebanyak 254 baris IP address."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Kebal terhadap serangan offline dictionary attack (kamus sandi) dan menyediakan forward secrecy."},
            {"key": "B", "text": "Menghilangkan kebutuhan memasukkan kata sandi (password) sama sekali pada seluruh perangkat klien."},
            {"key": "C", "text": "Memperluas jangkauan transmisi sinyal radio Access Point hingga dua kali lipat lebih jauh."},
            {"key": "D", "text": "Mendukung transmisi data tanpa menggunakan enkripsi algoritma simetris apapun."},
            {"key": "E", "text": "Memungkinkan semua tipe smartphone keluaran lama tahun 2012 terhubung secara otomatis."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Mendukung autentikasi berbasis pengguna (USM) dan enkripsi paket (privacy) menggunakan algoritma AES/DES."},
            {"key": "B", "text": "Meningkatkan kecepatan sampling trafik antarmuka dari hitungan menit menjadi milidetik murni."},
            {"key": "C", "text": "Mengizinkan query monitoring tanpa memerlukan konfigurasi port UDP 161 pada firewall."},
            {"key": "D", "text": "Menyederhanakan keamanan dengan menggunakan kata kunci community string publik 'public'."},
            {"key": "E", "text": "Menghilangkan struktur hierarki Object Identifier (OID) dan Management Information Base (MIB)."}
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Port switch akan langsung masuk ke status 'err-disable' (mati total) dan lampu indikator port berubah warna amber/oranye."},
            {"key": "B", "text": "Switch akan membiarkan paket lewat namun bandwidth laptop dibatasi menjadi 10 Kbps."},
            {"key": "C", "text": "Switch mengirimkan peringatan email ke administrator tetapi laptop asing tetap dapat mengakses server lokal."},
            {"key": "D", "text": "Laptop asing secara otomatis diformat sistem operasinya oleh switch melalui perintah TFTP."},
            {"key": "E", "text": "Switch merestart dirinya sendiri dan menghapus seluruh tabel VLAN yang tersimpan di flash."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Meneruskan setiap permintaan HTTP dari klien luar ke aplikasi backend Node.js/Python yang berjalan di port lokal 3000."},
            {"key": "B", "text": "Menghentikan layanan web server dan mengalihkan seluruh lalu lintas ke router gateway di IP 127.0.0.1."},
            {"key": "C", "text": "Melakukan enkripsi file HTML dengan protokol TLS 1.3 sebelum disimpan ke harddisk server."},
            {"key": "D", "text": "Membuat database MySQL baru di memori RAM pada alamat port 3000 secara otomatis."},
            {"key": "E", "text": "Membatasi koneksi maksimum dari satu IP address klien menjadi tepat 3000 request per detik."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Titik sambungan konektor mekanik atau ujung kabel yang mengalami pantulan Fresnel (Fresnel Reflection)."},
            {"key": "B", "text": "Kabel yang terbakar oleh arus listrik tegangan tinggi dari petir."},
            {"key": "C", "text": "Sambungan leburan fusion splice sempurna yang sama sekali tidak memiliki redaman."},
            {"key": "D", "text": "Kabel mengalami induksi elektromagnetik dari kawat tembaga di sekitarnya."},
            {"key": "E", "text": "Kondisi di mana diameter core serat optik tiba-tiba membesar secara alami."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Basis kode sangat ringkas (~4.000 baris kode), performa throughput tinggi di kernel space, dan menggunakan kriptografi modern Curve25519."},
            {"key": "B", "text": "Tidak memerlukan konfigurasi kunci kriptografi publik maupun privat antar perangkat."},
            {"key": "C", "text": "Beroperasi secara eksklusif menggunakan protokol TCP port 443 tanpa pernah menggunakan UDP."},
            {"key": "D", "text": "Mampu menghubungkan komputer tanpa perlu adanya koneksi internet publik sama sekali."},
            {"key": "E", "text": "Dapat menembus firewall secara otomatis dengan memanipulasi hardware switch jaringan."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Mengalikan kapasitas bandwidth gabungan (agregasi 4 Gbps) sekaligus menyediakan redundansi link tanpa diblokir oleh Spanning Tree."},
            {"key": "B", "text": "Mengubah fungsi switch layer 2 menjadi router BGP yang mampu menampung full internet routing table."},
            {"key": "C", "text": "Menghilangkan kebutuhan konfigurasi VLAN tagging pada antarmuka trunk antar switch."},
            {"key": "D", "text": "Mengurangi konsumsi listrik port switch hingga 75% saat lalu lintas data sedang sepi."},
            {"key": "E", "text": "Memperbolehkan satu komputer klien menggunakan 4 alamat IP privat yang berbeda secara bersamaan."}
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Mempercepat pemrosesan paket data koneksi yang sudah sah terjalin tanpa harus mencocokkan ke ratusan aturan filter di bawahnya (menghemat CPU router)."},
            {"key": "B", "text": "Mencegah komputer klien melakukan browsing ke situs web berbahaya yang memuat konten ilegal."},
            {"key": "C", "text": "Menghapus seluruh rekaman log koneksi di harddisk router agar memori penyimpanan tidak penuh."},
            {"key": "D", "text": "Mengizinkan pengguna tak dikenal dari internet publik membobol password router tanpa batasan."},
            {"key": "E", "text": "Mengubah seluruh paket data TCP menjadi paket data UDP agar proses transmisi lebih cepat."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Maksimum $\\le 0.05\\text{ dB}$ (ideal $0.01 - 0.03\\text{ dB}$ per titik sambungan)."},
            {"key": "B", "text": "Maksimum $\\le 3.5\\text{ dB}$ per titik sambungan fusi serat optik."},
            {"key": "C", "text": "Tepat $0.00\\text{ dB}$ tanpa boleh ada deviasi sudut pantul sedikit pun."},
            {"key": "D", "text": "Antara $1.0\\text{ dB}$ sampai dengan $2.5\\text{ dB}$ pada suhu ruangan kerja normal."},
            {"key": "E", "text": "Tergantung pada warna selubung tabung loose tube kabel yang sedang disambung."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Melakukan resolusi kueri DNS secara bertahap mulai dari Root Server (.) hingga ke Name Server otoritatif domain tersebut."},
            {"key": "B", "text": "Mengukur latensi ping ICMP ke setiap router hop yang dilewati menuju server DNS publik."},
            {"key": "C", "text": "Mengunduh file zona DNS secara lengkap menggunakan teknik DNS Zone Transfer (AXFR)."},
            {"key": "D", "text": "Mengenkripsi kueri DNS menggunakan protokol DNS-over-HTTPS (DoH) ke Cloudflare."},
            {"key": "E", "text": "Memperbaiki secara otomatis kesalahan ketik konfigurasi pada berkas /etc/resolv.conf."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Menyisipkan 16-bit hex `FF:FE` di tengah-tengah MAC Address dan membalik bit ke-7 (Universal/Local bit) pada octet pertama."},
            {"key": "B", "text": "Menambahkan angka `AA:BB` di akhir MAC Address dan mengalikan octet pertama dengan angka dua."},
            {"key": "C", "text": "Menghapus 3 byte pertama OUI vendor dan menggantinya dengan prefix link-local `FE80::`."},
            {"key": "D", "text": "Mengenkripsi seluruh digit heksadesimal MAC Address menggunakan hash SHA-256."},
            {"key": "E", "text": "Mengonversi seluruh digit hex genap menjadi nol dan digit ganjil menjadi huruf F."}
        ],
        "correctKey": "A",
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
        "isDiagnostic": False
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
            {"key": "A", "text": "Maksimum $\\le 5\\,\\Omega$ (Ohm), dan idealnya di bawah $1 - 2\\,\\Omega$ untuk instalasi telekomunikasi sensitif."},
            {"key": "B", "text": "Minimal harus di atas $50\\,\\Omega$ agar muatan petir tidak merusak lapisan tanah."},
            {"key": "C", "text": "Tepat $100\\,\\Omega$ agar serasi dengan impedansi karakteristik kabel UTP tembaga."},
            {"key": "D", "text": "Antara $20\\,\\Omega$ sampai $35\\,\\Omega$ tergantung jenis batuan di lokasi menara."},
            {"key": "E", "text": "Tidak perlu diukur asalkan tembaga penangkal petir ditancapkan sedalam minimal 10 cm."}
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
        "isDiagnostic": False
    }
]
