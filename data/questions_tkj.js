/**
 * TKA MASTERY HUB — QUESTIONS_TKJ.JS (135 SOAL AUTENTIK)
 */
window.TKA_TKJ_QUESTIONS = [
  {
    "id": "tkj-lat-e-01",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": true
  },
  {
    "id": "tkj-lat-e-02",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-03",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-04",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": true
  },
  {
    "id": "tkj-lat-e-05",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-06",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-07",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-08",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-09",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-10",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-11",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-12",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "multi",
    "questionHtml": "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
    "options": [
      {
        "key": "A",
        "text": "Channel 1 (2412 MHz)"
      },
      {
        "key": "B",
        "text": "Channel 6 (2437 MHz)"
      },
      {
        "key": "C",
        "text": "Channel 11 (2462 MHz)"
      },
      {
        "key": "D",
        "text": "Channel 3 (2422 MHz)"
      },
      {
        "key": "E",
        "text": "Channel 9 (2452 MHz)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Standar IEEE 802.11b/g/n pada 2.4 GHz di region FCC/ETSI memiliki 3 channel utama yang tidak saling interferensi: 1, 6, dan 11.",
      "execution": "Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping)."
    },
    "explanation": "Analisis multi-jawaban TKJ: Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping). Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-13",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-14",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-15",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-16",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-17",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-18",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-19",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-20",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-21",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-22",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-23",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-24",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "multi",
    "questionHtml": "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
    "options": [
      {
        "key": "A",
        "text": "Channel 1 (2412 MHz)"
      },
      {
        "key": "B",
        "text": "Channel 6 (2437 MHz)"
      },
      {
        "key": "C",
        "text": "Channel 11 (2462 MHz)"
      },
      {
        "key": "D",
        "text": "Channel 3 (2422 MHz)"
      },
      {
        "key": "E",
        "text": "Channel 9 (2452 MHz)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Standar IEEE 802.11b/g/n pada 2.4 GHz di region FCC/ETSI memiliki 3 channel utama yang tidak saling interferensi: 1, 6, dan 11.",
      "execution": "Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping)."
    },
    "explanation": "Analisis multi-jawaban TKJ: Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping). Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-25",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-26",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-27",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-28",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-29",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-30",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-31",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-32",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-33",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-34",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-e-35",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-01",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-02",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-03",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-04",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-05",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-06",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-07",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-08",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-09",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-10",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-11",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-12",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "multi",
    "questionHtml": "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
    "options": [
      {
        "key": "A",
        "text": "Channel 1 (2412 MHz)"
      },
      {
        "key": "B",
        "text": "Channel 6 (2437 MHz)"
      },
      {
        "key": "C",
        "text": "Channel 11 (2462 MHz)"
      },
      {
        "key": "D",
        "text": "Channel 3 (2422 MHz)"
      },
      {
        "key": "E",
        "text": "Channel 9 (2452 MHz)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Standar IEEE 802.11b/g/n pada 2.4 GHz di region FCC/ETSI memiliki 3 channel utama yang tidak saling interferensi: 1, 6, dan 11.",
      "execution": "Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping)."
    },
    "explanation": "Analisis multi-jawaban TKJ: Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping). Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-13",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-14",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-15",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-16",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-17",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-18",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-19",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-20",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-21",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-22",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-23",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-24",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "multi",
    "questionHtml": "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
    "options": [
      {
        "key": "A",
        "text": "Channel 1 (2412 MHz)"
      },
      {
        "key": "B",
        "text": "Channel 6 (2437 MHz)"
      },
      {
        "key": "C",
        "text": "Channel 11 (2462 MHz)"
      },
      {
        "key": "D",
        "text": "Channel 3 (2422 MHz)"
      },
      {
        "key": "E",
        "text": "Channel 9 (2452 MHz)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Standar IEEE 802.11b/g/n pada 2.4 GHz di region FCC/ETSI memiliki 3 channel utama yang tidak saling interferensi: 1, 6, dan 11.",
      "execution": "Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping)."
    },
    "explanation": "Analisis multi-jawaban TKJ: Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping). Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-25",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-26",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-27",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-28",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-29",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-30",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-31",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-32",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-33",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-34",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-m-35",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-01",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-02",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-03",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-04",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-05",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-06",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-07",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-08",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-09",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-10",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-11",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-12",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "multi",
    "questionHtml": "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
    "options": [
      {
        "key": "A",
        "text": "Channel 1 (2412 MHz)"
      },
      {
        "key": "B",
        "text": "Channel 6 (2437 MHz)"
      },
      {
        "key": "C",
        "text": "Channel 11 (2462 MHz)"
      },
      {
        "key": "D",
        "text": "Channel 3 (2422 MHz)"
      },
      {
        "key": "E",
        "text": "Channel 9 (2452 MHz)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Standar IEEE 802.11b/g/n pada 2.4 GHz di region FCC/ETSI memiliki 3 channel utama yang tidak saling interferensi: 1, 6, dan 11.",
      "execution": "Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping)."
    },
    "explanation": "Analisis multi-jawaban TKJ: Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping). Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-13",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-14",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-15",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-16",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-17",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-18",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-19",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-20",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-21",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-22",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-23",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-24",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "multi",
    "questionHtml": "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
    "options": [
      {
        "key": "A",
        "text": "Channel 1 (2412 MHz)"
      },
      {
        "key": "B",
        "text": "Channel 6 (2437 MHz)"
      },
      {
        "key": "C",
        "text": "Channel 11 (2462 MHz)"
      },
      {
        "key": "D",
        "text": "Channel 3 (2422 MHz)"
      },
      {
        "key": "E",
        "text": "Channel 9 (2452 MHz)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Standar IEEE 802.11b/g/n pada 2.4 GHz di region FCC/ETSI memiliki 3 channel utama yang tidak saling interferensi: 1, 6, dan 11.",
      "execution": "Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping)."
    },
    "explanation": "Analisis multi-jawaban TKJ: Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping). Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-25",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
      "execution": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
    },
    "explanation": "Analisis teknik jaringan komputer: Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-26",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
      "execution": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost).",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-27",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
      "execution": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-28",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
      "execution": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
    },
    "explanation": "Analisis teknik jaringan komputer: Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-29",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
      "execution": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-30",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
      "execution": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-31",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
      "execution": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
    },
    "explanation": "Analisis teknik jaringan komputer: Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-32",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "LINK BUDGET & REDAMAN FIBER OPTIK",
      "latex": "\\text{Loss Total (dB)} = (\\alpha \\times L) + (N_s \\times \\text{Loss}_s) + (N_c \\times \\text{Loss}_c)",
      "legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice"
    },
    "hints": {
      "concept": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
      "execution": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-33",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNET IPV4",
      "latex": "\\text{Jumlah Host} = 2^{(32 - \\text{Prefix})} - 2, \\quad \\text{Subnet Mask} = 256 - 2^{(32 - \\text{Prefix})}",
      "legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast"
    },
    "hints": {
      "concept": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
      "execution": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
    },
    "explanation": "Analisis multi-jawaban TKJ: Pilihan A, B, dan C adalah fitur fundamental standar IPv6. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-34",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR IEEE 802.1Q & METRIK OSPF",
      "latex": "\\text{Cost OSPF} = \\frac{\\text{Reference Bandwidth}}{\\text{Interface Bandwidth}} = \\frac{10^8 \\text{ bps}}{\\text{Bandwidth (bps)}}",
      "legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone"
    },
    "hints": {
      "concept": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
      "execution": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
    },
    "explanation": "Analisis teknik jaringan komputer: Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN. Opsi yang tepat adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-lat-h-35",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
      "latex": "\\text{Chain PREROUTING} \\to \\text{Routing Decision} \\to \\begin{cases} \\text{Chain INPUT} \\to \\text{Local Process} \\\\ \\text{Chain FORWARD} \\to \\text{POSTROUTING} \\end{cases}",
      "legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik"
    },
    "hints": {
      "concept": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
      "execution": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
    },
    "explanation": "Evaluasi kompetensi kejuruan TKJ: Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter.",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-01",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-02",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-03",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-04",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-05",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-06",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-07",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-08",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-09",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-10",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-11",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-12",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "multi",
    "questionHtml": "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
    "options": [
      {
        "key": "A",
        "text": "Channel 1 (2412 MHz)"
      },
      {
        "key": "B",
        "text": "Channel 6 (2437 MHz)"
      },
      {
        "key": "C",
        "text": "Channel 11 (2462 MHz)"
      },
      {
        "key": "D",
        "text": "Channel 3 (2422 MHz)"
      },
      {
        "key": "E",
        "text": "Channel 9 (2452 MHz)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-13",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-14",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-15",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-16",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-17",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-18",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-19",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "mcq",
    "questionHtml": "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"
      },
      {
        "key": "B",
        "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"
      },
      {
        "key": "C",
        "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"
      },
      {
        "key": "D",
        "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"
      },
      {
        "key": "E",
        "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-20",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "matrix",
    "questionHtml": "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh."
      },
      {
        "id": "1",
        "text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik."
      },
      {
        "id": "2",
        "text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz."
      },
      {
        "id": "3",
        "text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-21",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
    "options": [
      {
        "key": "A",
        "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal."
      },
      {
        "key": "B",
        "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal."
      },
      {
        "key": "C",
        "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien."
      },
      {
        "key": "D",
        "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat."
      },
      {
        "key": "E",
        "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-22",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "mcq",
    "questionHtml": "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"
      },
      {
        "key": "B",
        "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"
      },
      {
        "key": "C",
        "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"
      },
      {
        "key": "D",
        "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-23",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "matrix",
    "questionHtml": "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain."
      },
      {
        "id": "1",
        "text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet."
      },
      {
        "id": "2",
        "text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim."
      },
      {
        "id": "3",
        "text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-24",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "multi",
    "questionHtml": "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
    "options": [
      {
        "key": "A",
        "text": "Channel 1 (2412 MHz)"
      },
      {
        "key": "B",
        "text": "Channel 6 (2437 MHz)"
      },
      {
        "key": "C",
        "text": "Channel 11 (2462 MHz)"
      },
      {
        "key": "D",
        "text": "Channel 3 (2422 MHz)"
      },
      {
        "key": "E",
        "text": "Channel 9 (2452 MHz)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-25",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
    "options": [
      {
        "key": "A",
        "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"
      },
      {
        "key": "B",
        "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"
      },
      {
        "key": "C",
        "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"
      },
      {
        "key": "D",
        "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"
      },
      {
        "key": "E",
        "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-26",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "matrix",
    "questionHtml": "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop."
      },
      {
        "id": "1",
        "text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone)."
      },
      {
        "id": "2",
        "text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala."
      },
      {
        "id": "3",
        "text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-27",
    "subject": "tkj",
    "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Firewall Filter & Server Linux Services",
    "type": "multi",
    "questionHtml": "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
    "options": [
      {
        "key": "A",
        "text": "DNS (Domain Name System): Port 53 UDP/TCP"
      },
      {
        "key": "B",
        "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP"
      },
      {
        "key": "C",
        "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)"
      },
      {
        "key": "D",
        "text": "SSH (Secure Shell): Port 8080 UDP"
      },
      {
        "key": "E",
        "text": "FTP (File Transfer Protocol): Port 443 UDP"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-28",
    "subject": "tkj",
    "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Transmisi FO & Standar Wi-Fi 802.11",
    "type": "mcq",
    "questionHtml": "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "6,15 dB"
      },
      {
        "key": "B",
        "text": "5,25 dB"
      },
      {
        "key": "C",
        "text": "7,35 dB"
      },
      {
        "key": "D",
        "text": "8,45 dB"
      },
      {
        "key": "E",
        "text": "4,80 dB"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-29",
    "subject": "tkj",
    "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "IPv4 VLSM & CIDR Subnetting",
    "type": "matrix",
    "questionHtml": "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240."
      },
      {
        "id": "1",
        "text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128."
      },
      {
        "id": "2",
        "text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143."
      },
      {
        "id": "3",
        "text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "tkj-sim-30",
    "subject": "tkj",
    "materi": "SWITCHING & ROUTING ENTERPRISE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "VLAN 802.1Q & Protokol Routing OSPF",
    "type": "multi",
    "questionHtml": "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
    "options": [
      {
        "key": "A",
        "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm)."
      },
      {
        "key": "B",
        "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover)."
      },
      {
        "key": "C",
        "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU."
      },
      {
        "key": "D",
        "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik."
      },
      {
        "key": "E",
        "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  }
];
