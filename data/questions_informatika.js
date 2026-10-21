/**
 * TKA MASTERY HUB — QUESTIONS_INFORMATIKA.JS (110 SOAL AUTENTIK PUSMENDIK 2026)
 * Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
 * Composition: 25 Latihan Easy, 25 Medium, 25 Hard, 35 Simulasi (25 MCQ, 5 Multi, 5 Matrix)
 */
window.TKA_INFORMATIKA_QUESTIONS = [
  {
    "id": "inf-lat-e-01",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Empat Pilar Fondasi Berpikir Komputasional",
    "hints": {
      "concept": "Membagi masalah besar menjadi bagian-bagian kecil adalah definisi dekomposisi.",
      "execution": "Pilih: Dekomposisi (Decomposition)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam memecahkan permasalahan kompleks sistem antrean rumah sakit yang rumit, seorang analis sistem membagi alur besar menjadi subsistem registrasi, triase pasien, pelayanan poli, dan pembayaran farmasi secara terpisah agar mudah dikaji. Pilar berpikir komputasional yang diterapkan pada langkah pemecahan masalah tersebut adalah...",
    "formulaHud": {
      "title": "4 PILAR BERPIKIR KOMPUTASIONAL (BK)",
      "latex": "\\text{Masalah Kompleks} \\xrightarrow{\\text{Dekomposisi}} \\sum \\text{Sub-Masalah} \\xrightarrow{\\text{Abstraksi}} \\text{Model Sederhana} \\xrightarrow{\\text{Algoritma}} \\text{Solusi}",
      "legend": "• Dekomposisi: Memecah masalah kompleks menjadi komponen kecil terisolasi<br>• Pengenalan Pola: Mengidentifikasi kesamaan karakteristik/alur<br>• Abstraksi: Fokus pada informasi esensial dan mengeliminasi detail sepele<br>• Algoritma: Langkah terurut logis penyelesaian masalah"
    },
    "options": [
      {
        "key": "A",
        "text": "Dekomposisi (Decomposition), yaitu teknik memecah masalah besar dan kompleks menjadi bagian-bagian yang lebih kecil, mandiri, dan lebih mudah dikelola."
      },
      {
        "key": "B",
        "text": "Pengenalan Pola (Pattern Recognition), yaitu mencari kesamaan bentuk tren historis kunjungan pasien antar hari sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Abstraksi (Abstraction), yaitu mengabaikan informasi identitas pasien yang tidak relevan dengan proses triase medis."
      },
      {
        "key": "D",
        "text": "Desain Algoritma (Algorithm Design), yaitu menyusun langkah-langkah komputasi otomatis tanpa menguraikan struktur masalah."
      },
      {
        "key": "E",
        "text": "Generalisasi Komputasi, yaitu menerapkan solusi algoritma yang sama secara membabi buta tanpa modifikasi modul."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Dekomposisi (Decomposition), yaitu teknik memecah masalah besar dan kompleks menjadi bagian-bagian yang lebih kecil, mandiri, dan lebih mudah dikelola.. Membagi masalah besar menjadi bagian-bagian kecil adalah definisi dekomposisi. Pilih: Dekomposisi (Decomposition)."
  },
  {
    "id": "inf-lat-e-02",
    "materi": "SISTEM KOMPUTER",
    "topic": "Siklus Kerja Utama Central Processing Unit (CPU)",
    "hints": {
      "concept": "Siklus instruksi mesin CPU standar: Ambil (Fetch) -> Terjemahkan (Decode) -> Jalankan (Execute) -> Simpan (Store).",
      "execution": "Pilih opsi: Fetch -> Decode -> Execute -> Store."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Mikroprosesor komputer mengeksekusi instruksi program perangkat lunak melalui siklus mesin yang berulang secara terus-menerus. Urutan tahapan fundamental dalam siklus instruksi CPU yang benar adalah...",
    "formulaHud": {
      "title": "SIKLUS INSTRUKSI MESIN VON NEUMANN",
      "latex": "\\text{PC} \\xrightarrow{\\text{Fetch}} \\text{IR} \\xrightarrow{\\text{Decode (CU)}} \\text{ALU Operations} \\xrightarrow{\\text{Execute}} \\text{Register/RAM (Store)}",
      "legend": "• PC (Program Counter): Menyimpan alamat memori instruksi berikutnya<br>• IR (Instruction Register): Menyimpan kode instruksi aktif saat ini<br>• CU (Control Unit): Mendekode sinyal kendali mikroprosesor<br>• ALU (Arithmetic Logic Unit): Melakukan kalkulasi aritmetika dan logika"
    },
    "options": [
      {
        "key": "A",
        "text": "Decode $\\rightarrow$ Fetch $\\rightarrow$ Store $\\rightarrow$ Interrupt $\\rightarrow$ Execute sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Fetch (mengambil kode instruksi dari RAM ke register) $\\rightarrow$ Decode (menerjemahkan kode operasi oleh Control Unit) $\\rightarrow$ Execute (mengeksekusi operasi pada ALU) $\\rightarrow$ Store (menulis hasil kembali ke register/memori)."
      },
      {
        "key": "C",
        "text": "Compile $\\rightarrow$ Link $\\rightarrow$ Load $\\rightarrow$ Execute $\\rightarrow$ Terminate."
      },
      {
        "key": "D",
        "text": "Store $\\rightarrow$ ALU Compute $\\rightarrow$ Fetch $\\rightarrow$ Cache $\\rightarrow$ Decode."
      },
      {
        "key": "E",
        "text": "Interrupt $\\rightarrow$ Paging $\\rightarrow$ Context Switch $\\rightarrow$ Decode $\\rightarrow$ Fetch."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Fetch (mengambil kode instruksi dari RAM ke register) $\\rightarrow$ Decode (menerjemahkan kode operasi oleh Control Unit) $\\rightarrow$ Execute (mengeksekusi operasi pada ALU) $\\rightarrow$ Store (menulis hasil kembali ke register/memori).. Siklus instruksi mesin CPU standar: Ambil (Fetch) -> Terjemahkan (Decode) -> Jalankan (Execute) -> Simpan (Store). Pilih opsi: Fetch -> Decode -> Execute -> Store."
  },
  {
    "id": "inf-lat-e-03",
    "materi": "STRUKTUR DATA",
    "topic": "Prinsip Mekanisme Akses Data Stack vs Queue",
    "hints": {
      "concept": "Undo/Redo dan Back browser membalik urutan langkah terakhir, menggunakan prinsip Last-In First-Out (LIFO), yaitu Stack.",
      "execution": "Pilih: Stack (Tumpukan) dengan prinsip LIFO."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Fitur tombol Undo/Redo pada pengolah kata teks dan tombol navigasi Back pada peramban web bekerja berdasarkan mekanisme struktur data yang melayani elemen data terakhir dimasukkan sebagai elemen pertama yang diproses. Struktur data yang menerapkan mekanisme tersebut adalah...",
    "formulaHud": {
      "title": "KOMPARASI STRUKTUR DATA LINEAR",
      "latex": "\\begin{aligned} \\text{Stack (LIFO):} & \\quad \\text{Elemen Masuk Terakhir} \\iff \\text{Elemen Keluar Pertama (Top)} \\\\ \\text{Queue (FIFO):} & \\quad \\text{Elemen Masuk Pertama (Rear)} \\iff \\text{Elemen Keluar Pertama (Front)} \\end{aligned}",
      "legend": "• Stack: Undo/Redo, Call Stack fungsi rekursif, evaluasi notasi Postfix<br>• Queue: Antrean spooler printer, penjadwalan proses CPU Round-Robin, algoritma BFS"
    },
    "options": [
      {
        "key": "A",
        "text": "Queue (Antrean) dengan prinsip FIFO (First-In, First-Out), di mana elemen pertama masuk akan diproses pertama kali ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Priority Queue, di mana setiap elemen data wajib memiliki bobot prioritas bilangan bulat sebelum dialokasikan."
      },
      {
        "key": "C",
        "text": "Stack (Tumpukan) dengan prinsip LIFO (Last-In, First-Out), di mana operasi penambahan (push) dan penghapusan (pop) hanya dapat dilakukan pada satu ujung puncak (top)."
      },
      {
        "key": "D",
        "text": "Circular Linked List, di mana simpul terakhir selalu menunjuk kembali ke simpul awal tanpa ada titik akhir."
      },
      {
        "key": "E",
        "text": "Binary Search Tree, di mana data diurutkan berdasarkan perbandingan nilai kunci simpul induk dan cabang."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Stack (Tumpukan) dengan prinsip LIFO (Last-In, First-Out), di mana operasi penambahan (push) dan penghapusan (pop) hanya dapat dilakukan pada satu ujung puncak (top).. Undo/Redo dan Back browser membalik urutan langkah terakhir, menggunakan prinsip Last-In First-Out (LIFO), yaitu Stack. Pilih: Stack (Tumpukan) dengan prinsip LIFO."
  },
  {
    "id": "inf-lat-e-04",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Hierarki dan Peran Lapisan Model Referensi OSI",
    "hints": {
      "concept": "IP Address dan pemilihan rute (routing) bekerja di Lapisan ke-3, yaitu Network Layer.",
      "execution": "Pilih: Network Layer (Lapisan 3)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam model referensi 7 Lapisan OSI (Open Systems Interconnection), lapisan yang bertanggung jawab untuk menentukan rute logis terbaik pengiriman paket data antar jaringan yang berbeda melalui pengalamatan logis (IP Address) adalah...",
    "formulaHud": {
      "title": "ENKAPSULASI 7 LAPISAN MODEL OSI",
      "latex": "\\text{App (L7)} \\to \\text{Pres (L6)} \\to \\text{Sess (L5)} \\to \\text{Trans (Segmen/L4)} \\to \\text{Net (Paket/L3)} \\to \\text{DataLink (Frame/L2)} \\to \\text{Phys (Bit/L1)}",
      "legend": "• L3 (Network): Router, IP Address, ICMP, Paket data<br>• L2 (Data Link): Switch, MAC Address, Frame data<br>• L4 (Transport): Port, TCP/UDP, Segmen data, Flow control"
    },
    "options": [
      {
        "key": "A",
        "text": "Data Link Layer (Lapisan 2), yang menangani framing fisik dan physical addressing berupa MAC Address lokal menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Transport Layer (Lapisan 4), yang menyediakan komunikasi end-to-end dengan segmentasi data TCP/UDP."
      },
      {
        "key": "C",
        "text": "Physical Layer (Lapisan 1), yang mentransmisikan bit-bit biner mentah melalui media transmisi kabel atau nirkabel."
      },
      {
        "key": "D",
        "text": "Network Layer (Lapisan 3), yang mengelola routing paket data dan logical addressing menggunakan protokol IP (Internet Protocol)."
      },
      {
        "key": "E",
        "text": "Session Layer (Lapisan 5), yang membuka, mengelola, dan mengakhiri sesi dialog antar aplikasi jaringan."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Network Layer (Lapisan 3), yang mengelola routing paket data dan logical addressing menggunakan protokol IP (Internet Protocol).. IP Address dan pemilihan rute (routing) bekerja di Lapisan ke-3, yaitu Network Layer. Pilih: Network Layer (Lapisan 3)."
  },
  {
    "id": "inf-lat-e-05",
    "materi": "ANALISIS DATA",
    "topic": "Karakteristik Kunci Utama (Primary Key) Basis Data Relasional",
    "hints": {
      "concept": "Syarat mutlak Primary Key (PK): Unik untuk setiap rekaman dan tidak boleh bernilai NULL (NOT NULL).",
      "execution": "Pilih: Menjamin nilai yang unik dan tidak boleh bernilai kosong (NOT NULL)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam perancangan basis data relasional untuk sistem akademik sekolah, entitas siswa memiliki beberapa atribut: `NISN`, `Nama_Lengkap`, `Tanggal_Lahir`, dan `Alamat`. Alasan paling fundamental mengapa atribut `NISN` dipilih sebagai Primary Key adalah...",
    "formulaHud": {
      "title": "SYARAT KEABSAHAN PRIMARY KEY BASIS DATA",
      "latex": "\\forall x, y \\in T: \\quad x \\neq y \\implies \\text{PK}(x) \\neq \\text{PK}(y) \\quad \\land \\quad \\text{PK}(x) \\neq \\text{NULL}",
      "legend": "• Entity Integrity Constraint: Kunci utama wajib unik dan tidak boleh kosong (NOT NULL)<br>• Foreign Key: Kunci tamu yang mereferensikan Primary Key dari tabel induk untuk menjaga integritas referensial"
    },
    "options": [
      {
        "key": "A",
        "text": "Atribut `NISN` memiliki panjang karakter teks paling pendek sehingga mempercepat proses backup hard disk diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Atribut `NISN` dapat diubah nilainya sewaktu-waktu oleh pengguna tanpa memengaruhi relasi tabel lainnya."
      },
      {
        "key": "C",
        "text": "Atribut `NISN` otomatis mengurutkan nama siswa sesuai abjad alfabet dari huruf A sampai Z secara fisik."
      },
      {
        "key": "D",
        "text": "Atribut `NISN` merupakan tipe data numerik yang wajib dapat dijumlahkan dan dihitung nilai rata-ratanya."
      },
      {
        "key": "E",
        "text": "Atribut `NISN` menjamin nilai yang unik bagi setiap baris rekaman siswa dan secara mutlak tidak boleh bernilai kosong (NOT NULL)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Atribut `NISN` menjamin nilai yang unik bagi setiap baris rekaman siswa dan secara mutlak tidak boleh bernilai kosong (NOT NULL).. Syarat mutlak Primary Key (PK): Unik untuk setiap rekaman dan tidak boleh bernilai NULL (NOT NULL). Pilih: Menjamin nilai yang unik dan tidak boleh bernilai kosong (NOT NULL)."
  },
  {
    "id": "inf-lat-e-06",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Kompleksitas Asimtotik Algoritma Pencarian Biner",
    "hints": {
      "concept": "Binary search membagi ruang pencarian menjadi setengah pada setiap langkah: log2(1024) = 10 pembagian, maksimal 11 perbandingan.",
      "execution": "Hitung: log2(1024) + 1 = 11 kali."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah larik data (array) berisi 1.024 elemen bilangan bulat yang telah terurut rapi secara menaik (sorted ascending). Jika dilakukan pencarian suatu elemen menggunakan algoritma Binary Search, jumlah perbandingan maksimum (worst case) yang dibutuhkan hingga elemen ditemukan atau dipastikan tidak ada adalah...",
    "formulaHud": {
      "title": "KOMPLEKSITAS PENCARIAN BINER (BINARY SEARCH)",
      "latex": "T_{\\text{worst}}(n) = \\lfloor \\log_2 n \\rfloor + 1, \\quad \\text{Untuk } n = 1024 = 2^{10} \\implies 10 + 1 = 11 \\text{ perbandingan}",
      "legend": "• Linear Search: Kompleksitas $O(n)$, membutuhkan hingga $n$ perbandingan<br>• Binary Search: Kompleksitas $O(\\log n)$, syarat mutlak data harus sudah terurut"
    },
    "options": [
      {
        "key": "A",
        "text": "11 kali perbandingan, karena kompleksitas pencarian biner adalah $O(\\log_2 n)$ sehingga $\\lfloor \\log_2(1024) \\rfloor + 1 = 10 + 1 = 11$."
      },
      {
        "key": "B",
        "text": "1.024 kali perbandingan, karena algoritma harus memeriksa setiap elemen dari indeks pertama hingga terakhir sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "512 kali perbandingan, karena algoritma membagi array menjadi dua bagian dan memeriksa seluruh separuh array."
      },
      {
        "key": "D",
        "text": "1 kali perbandingan, karena data sudah terurut sehingga elemen langsung terdeteksi pada percobaan pertama."
      },
      {
        "key": "E",
        "text": "100 kali perbandingan, sesuai dengan kapasitas memori buffer prosesor komputer."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) 11 kali perbandingan, karena kompleksitas pencarian biner adalah $O(\\log_2 n)$ sehingga $\\lfloor \\log_2(1024) \\rfloor + 1 = 10 + 1 = 11$.. Binary search membagi ruang pencarian menjadi setengah pada setiap langkah: log2(1024) = 10 pembagian, maksimal 11 perbandingan. Hitung: log2(1024) + 1 = 11 kali."
  },
  {
    "id": "inf-lat-e-07",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Triad Keamanan Informasi (CIA Triad)",
    "hints": {
      "concept": "Penyadapan data rahasia tanpa izin melanggar pilar Kerahasiaan (Confidentiality).",
      "execution": "Pilih: Kerahasiaan (Confidentiality)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam manajemen keamanan informasi (Information Security), pilar CIA Triad menjadi standar evaluasi proteksi sistem. Jika seorang peretas berhasil menyadap pesan surel rahasia perusahaan yang sedang dikirimkan melalui internet karena pesan tersebut tidak dienkripsi, aspek keamanan yang telah dilanggar adalah...",
    "formulaHud": {
      "title": "PILAR UTAMA CIA TRIAD",
      "latex": "\\text{Keamanan Informasi} \\equiv \\text{Confidentiality (Kerahasiaan)} \\cap \\text{Integrity (Keutuhan)} \\cap \\text{Availability (Ketersediaan)}",
      "legend": "• Confidentiality terancam oleh: Sniffing, pembobolan kata sandi, pencurian berkas<br>• Integrity terancam oleh: Man-in-the-Middle (MitM), injeksi data palsu, perusakan virus<br>• Availability terancam oleh: Serangan DDoS, ransomware, pemadaman listrik/server"
    },
    "options": [
      {
        "key": "A",
        "text": "Integritas (Integrity), yaitu jaminan bahwa data tidak mengalami manipulasi, perubahan, atau perusakan oleh pihak tidak berhak sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Kerahasiaan (Confidentiality), yaitu jaminan bahwa informasi hanya dapat diakses, dibaca, dan disingkap oleh pihak yang berhak dan memiliki otorisasi sah."
      },
      {
        "key": "C",
        "text": "Ketersediaan (Availability), yaitu jaminan bahwa sistem dan data dapat diakses oleh pengguna yang berwenang kapan pun dibutuhkan."
      },
      {
        "key": "D",
        "text": "Non-Repudiation, yaitu mekanisme pembuktian bahwa pengirim tidak dapat menyangkal telah mengirimkan pesan."
      },
      {
        "key": "E",
        "text": "Akuntabilitas (Accountability), yaitu pencatatan jejak audit aktivitas pengguna ke dalam berkas log sistem."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Kerahasiaan (Confidentiality), yaitu jaminan bahwa informasi hanya dapat diakses, dibaca, dan disingkap oleh pihak yang berhak dan memiliki otorisasi sah.. Penyadapan data rahasia tanpa izin melanggar pilar Kerahasiaan (Confidentiality). Pilih: Kerahasiaan (Confidentiality)."
  },
  {
    "id": "inf-lat-e-08",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Rentang Pengalamatan IPv4 Privat Menurut RFC 1918",
    "hints": {
      "concept": "Blok IP privat kelas C adalah 192.168.0.0 s.d. 192.168.255.255.",
      "execution": "Pilih: 192.168.1.50."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Untuk mencegah kehabisan alamat IPv4 global di internet, IETF menerbitkan dokumen RFC 1918 yang menetapkan blok alamat IP Privat yang tidak dapat dirutekan langsung di jaringan internet publik (non-routable). Manakah di antara alamat IP berikut yang tergolong sebagai alamat IPv4 Privat kelas C?",
    "formulaHud": {
      "title": "RENTANG BLOK IPV4 PRIVAT (RFC 1918)",
      "latex": "\\begin{aligned} \\text{Kelas A:} & \\quad 10.0.0.0 - 10.255.255.255 \\quad (/8) \\\\ \\text{Kelas B:} & \\quad 172.16.0.0 - 172.31.255.255 \\quad (/12) \\\\ \\text{Kelas C:} & \\quad 192.168.0.0 - 192.168.255.255 \\quad (/16) \\end{aligned}",
      "legend": "• Loopback address: 127.0.0.0/8 (127.0.0.1 localhost)<br>• APIPA (Automatic Private IP): 169.254.0.0/16<br>• IP Privat wajib ditranslasikan melalui NAT (Network Address Translation) untuk mengakses internet"
    },
    "options": [
      {
        "key": "A",
        "text": "`172.35.10.1`, karena berada di luar rentang privat kelas B yang dibatasi hingga `172.31.255.255` ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "`10.0.0.1`, karena alamat ini merupakan blok alamat IP privat Kelas A murni bukan Kelas C."
      },
      {
        "key": "C",
        "text": "`192.168.1.50`, karena berada di dalam rentang alamat privat blok `192.168.0.0` sampai `192.168.255.255` (prefix `/16`)."
      },
      {
        "key": "D",
        "text": "`8.8.8.8`, karena alamat ini merupakan DNS server publik milik Google yang dapat dirutekan secara global."
      },
      {
        "key": "E",
        "text": "`127.0.0.1`, karena alamat ini dicadangkan secara khusus sebagai antarmuka Loopback lokal sistem komputer."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) `192.168.1.50`, karena berada di dalam rentang alamat privat blok `192.168.0.0` sampai `192.168.255.255` (prefix `/16`).. Blok IP privat kelas C adalah 192.168.0.0 s.d. 192.168.255.255. Pilih: 192.168.1.50."
  },
  {
    "id": "inf-lat-e-09",
    "materi": "SISTEM KOMPUTER",
    "topic": "Hierarki Memori dan Karakteristik Cache Memory",
    "hints": {
      "concept": "Cache memori berbahan SRAM berfungsi menutupi gap kecepatan (von Neumann bottleneck) antara CPU dan RAM.",
      "execution": "Pilih: Menjembatani perbedaan kecepatan antara prosesor dan RAM utama."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam arsitektur komputer modern, hierarki memori dirancang bertingkat mulai dari Register, Cache (L1, L2, L3), RAM utama, hingga Secondary Storage (SSD/HDD). Peran mendasar dari Cache Memory dalam hierarki tersebut adalah...",
    "formulaHud": {
      "title": "HIERARKI MEMORI KOMPUTER",
      "latex": "\\text{Kecepatan} \\uparrow, \\text{Biaya} \\uparrow, \\text{Kapasitas} \\downarrow : \\quad \\text{Register} > \\text{L1 Cache} > \\text{L2 Cache} > \\text{L3 Cache} > \\text{RAM} > \\text{SSD} > \\text{HDD}",
      "legend": "• Cache Hit: Data yang dicari CPU tersedia di cache memory (latensi rendah)<br>• Cache Miss: Data tidak ditemukan di cache, CPU harus mengambil dari RAM utama (latensi tinggi)<br>• Prinsip Locality of Reference: Temporal Locality & Spatial Locality"
    },
    "options": [
      {
        "key": "A",
        "text": "Menyimpan data arsip jangka panjang secara permanen saat komputer dimatikan (non-volatile storage) menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Menggantikan fungsi sistem operasi dalam melakukan manajemen berkas dan penjadwalan antrean I/O."
      },
      {
        "key": "C",
        "text": "Mendinginkan suhu sirkuit mikroprosesor dengan menyerap panas berlebih melalui semikonduktor termal."
      },
      {
        "key": "D",
        "text": "Menjembatani perbedaan kecepatan operasi yang sangat timpang antara prosesor yang super cepat dan RAM utama yang relatif lebih lambat dengan menyimpan salinan data dan instruksi yang sering diakses."
      },
      {
        "key": "E",
        "text": "Menambah kapasitas total ruang penyimpanan sekunder komputer tanpa memerlukan penambahan modul SSD fisik."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Menjembatani perbedaan kecepatan operasi yang sangat timpang antara prosesor yang super cepat dan RAM utama yang relatif lebih lambat dengan menyimpan salinan data dan instruksi yang sering diakses.. Cache memori berbahan SRAM berfungsi menutupi gap kecepatan (von Neumann bottleneck) antara CPU dan RAM. Pilih: Menjembatani perbedaan kecepatan antara prosesor dan RAM utama."
  },
  {
    "id": "inf-lat-e-10",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Evaluasi Logika Kondisional Boolean",
    "hints": {
      "concept": "Evaluasi bertahap: 1) a+c >= b (20 >= 20: True). 2) 20 % 15 == 0 (False). 3) 5*3 > 15 (False). False or False = False. not(False) = True. True and True = True.",
      "execution": "Nilai akhir adalah True."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Diberikan cuplikan kode program logika komputasi sederhana berikut:\n```python\na = 15\nb = 20\nc = 5\nhasil = (a + c >= b) and not (b % a == 0 or c * 3 > a)\n```\nNilai boolean akhir yang tersimpan di dalam variabel `hasil` setelah kode dieksekusi adalah...",
    "formulaHud": {
      "title": "TABEL KEBENARAN LOGIKA OPERATOR BOOLEAN",
      "latex": "P \\land \\neg(Q \\lor R): \\quad (15+5 \\ge 20) = \\text{True}, \\quad (20 \\pmod{15} = 5 \\ne 0) = \\text{False}, \\quad (15 > 15) = \\text{False} \\implies \\text{True} \\land \\neg(\\text{False}) = \\text{True}",
      "legend": "• a + c = 20 >= 20 -> True<br>• b % a = 20 % 15 = 5 == 0 -> False<br>• c * 3 = 15 > 15 -> False<br>• False or False -> False; not False -> True; True and True -> True"
    },
    "options": [
      {
        "key": "A",
        "text": "`False`, karena operator logika `not` membalik seluruh hasil ekspresi awal menjadi bernilai salah secara mutlak diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "`SyntaxError`, karena penulisan operator modulus `%` tidak dapat digabungkan dengan operator perbandingan dan boolean dalam satu baris."
      },
      {
        "key": "C",
        "text": "`None`, karena operasi perbandingan majemuk tidak mengembalikan tipe data primitif jika tidak diberi klausa `else` eksplisit."
      },
      {
        "key": "D",
        "text": "`TypeError`, karena variabel integer tidak dapat dievaluasi bersama konstanta boolean tanpa fungsi konversi tipe `bool()`."
      },
      {
        "key": "E",
        "text": "`True`, karena sub-kondisi pertama `(a + c >= b)` bernilai `True` ($20 \\ge 20$), sub-kondisi di dalam tanda kurung `(b % a == 0 or c * 3 > a)` bernilai `False` ($5 == 0$ bernilai `False` dan $15 > 15$ bernilai `False`), sehingga negasinya `not (False)` bernilai `True`, dan evaluasi akhir `True and True` menghasilkan `True`."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) `True`, karena sub-kondisi pertama `(a + c >= b)` bernilai `True` ($20 \\ge 20$), sub-kondisi di dalam tanda kurung `(b % a == 0 or c * 3 > a)` bernilai `False` ($5 == 0$ bernilai `False` dan $15 > 15$ bernilai `False`), sehingga negasinya `not (False)` bernilai `True`, dan evaluasi akhir `True and True` menghasilkan `True`.. Evaluasi bertahap: 1) a+c >= b (20 >= 20: True). 2) 20 % 15 == 0 (False). 3) 5*3 > 15 (False). False or False = False. not(False) = True. True and True = True. Nilai akhir adalah True."
  },
  {
    "id": "inf-lat-e-11",
    "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
    "topic": "Fungsi Pencarian Referensi Spreadsheet VLOOKUP vs XLOOKUP",
    "hints": {
      "concept": "VLOOKUP (Vertical Lookup) secara fundamental hanya mencari kunci pada kolom pertama tabel referensi dan mengembalikan nilai ke arah kanan.",
      "execution": "Pilih: Hanya mampu mencari nilai pada kolom paling kiri dari rentang tabel."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam aplikasi lembar sebar (spreadsheet) seperti Microsoft Excel atau Google Sheets, seorang staf tata usaha ingin mencari gaji pokok pegawai berdasarkan `ID_Pegawai` dari tabel referensi master. Karakteristik utama dari fungsi `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])` adalah...",
    "formulaHud": {
      "title": "SINTAKSIS FORMULA PENCARIAN SPREADSHEET",
      "latex": "\\text{VLOOKUP}(K, A, c, \\text{FALSE}) \\implies \\text{Cari } K \\text{ pada } A_{*, 1}, \\text{ Ambil nilai pada kolom ke-} c",
      "legend": "• Keterbatasan VLOOKUP klasik: Kunci pencarian wajib di kolom 1 (paling kiri)<br>• XLOOKUP (Modern) / INDEX-MATCH: Mengatasi limitasi VLOOKUP, mampu mencari ke arah kiri dan vertikal/horizontal fleksibel"
    },
    "options": [
      {
        "key": "A",
        "text": "Hanya mampu mencari nilai kecocokan (`lookup_value`) pada kolom paling kiri (kolom pertama) dari rentang tabel referensi, lalu mengambil data dari kolom di sebelah kanannya."
      },
      {
        "key": "B",
        "text": "Mampu mencari nilai kecocokan pada sembarang kolom dan secara bebas mengambil data dari kolom sebelah kirinya tanpa batas sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Otomatis menjumlahkan seluruh nilai numerik yang cocok dengan kriteria tanpa memerlukan fungsi SUMIF tambahan."
      },
      {
        "key": "D",
        "text": "Hanya dapat digunakan untuk mencocokkan data bertipe tanggal kalender dan tidak dapat memproses teks alfabetik."
      },
      {
        "key": "E",
        "text": "Wajib menyortir data master secara menurun (descending) sebelum rumus pencarian dapat dieksekusi tanpa galat."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Hanya mampu mencari nilai kecocokan (`lookup_value`) pada kolom paling kiri (kolom pertama) dari rentang tabel referensi, lalu mengambil data dari kolom di sebelah kanannya.. VLOOKUP (Vertical Lookup) secara fundamental hanya mencari kunci pada kolom pertama tabel referensi dan mengembalikan nilai ke arah kanan. Pilih: Hanya mampu mencari nilai pada kolom paling kiri dari rentang tabel."
  },
  {
    "id": "inf-lat-e-12",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Representasi Graf Sederhana dan Derajat Simpul",
    "hints": {
      "concept": "Hitung jumlah koneksi per simpul: A:2, B:3, C:3, D:3, E:1. Jadi B, C, dan D berderajat 3.",
      "execution": "Pilih opsi yang menyatakan simpul dengan derajat 3 sebagai simpul berderajat tertinggi."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah jaringan pertemanan media sosial dimodelkan sebagai graf tak berarah (undirected graph) $G = (V, E)$, di mana $V = \\{A, B, C, D, E\\}$ merepresentasikan orang dan $E = \\{(A,B), (A,C), (B,C), (B,D), (C,D), (D,E)\\}$ merepresentasikan hubungan pertemanan. Simpul (vertex) yang memiliki derajat pertemanan (degree) tertinggi adalah...",
    "formulaHud": {
      "title": "DERAJAT SIMPUL GRAF TAK BERARAH",
      "latex": "\\text{deg}(v) = |\\{e \\in E : v \\in e\\}|, \\quad \\sum_{v \\in V} \\text{deg}(v) = 2|E| = 2(6) = 12",
      "legend": "• Hubungan simpul: A terhubung ke B, C (deg = 2)<br>• B terhubung ke A, C, D (deg = 3)<br>• C terhubung ke A, B, D (deg = 3)<br>• D terhubung ke B, C, E (deg = 3)<br>• E terhubung ke D (deg = 1)<br>• B, C, dan D masing-masing memiliki derajat 3 (tertinggi)"
    },
    "options": [
      {
        "key": "A",
        "text": "Simpul $A$, karena berada di urutan alfabet pertama dan terhubung dengan seluruh simpul lainnya sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Simpul $B$ dan $C$, keduanya memiliki derajat 3 karena masing-masing terhubung langsung dengan tiga sisi pertemanan."
      },
      {
        "key": "C",
        "text": "Simpul $D$, karena merupakan satu-satunya jembatan (bridge) yang menghubungkan simpul $E$ ke jaringan."
      },
      {
        "key": "D",
        "text": "Simpul $E$, karena memiliki derajat pertemanan tertinggi sebesar 4 sisi langsung."
      },
      {
        "key": "E",
        "text": "Seluruh simpul memiliki derajat yang persis sama sebesar 2 sisi pertemanan reguler."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Simpul $B$ dan $C$, keduanya memiliki derajat 3 karena masing-masing terhubung langsung dengan tiga sisi pertemanan.. Hitung jumlah koneksi per simpul: A:2, B:3, C:3, D:3, E:1. Jadi B, C, dan D berderajat 3. Pilih opsi yang menyatakan simpul dengan derajat 3 sebagai simpul berderajat tertinggi."
  },
  {
    "id": "inf-lat-e-13",
    "materi": "ANALISIS DATA",
    "topic": "Pengelompokan dan Agregasi Query SQL Dasar",
    "hints": {
      "concept": "Untuk menghitung total unit per kategori, gunakan fungsi SUM(jumlah_terjual) dan klausul GROUP BY kategori_produk.",
      "execution": "Pilih: SELECT kategori_produk, SUM(jumlah_terjual) FROM Penjualan GROUP BY kategori_produk;"
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Diberikan tabel basis data `Penjualan` dengan kolom `kategori_produk`, `nama_produk`, dan `jumlah_terjual`. Perintah SQL yang tepat untuk menampilkan setiap kategori produk beserta total unit yang berhasil terjual di setiap kategori tersebut adalah...",
    "formulaHud": {
      "title": "SINTAKSIS KLAUSA AGREGASI BASIS DATA SQL",
      "latex": "\\text{SELECT } C, \\text{ AGG}(V) \\text{ FROM } T \\text{ GROUP BY } C \\text{ [HAVING kondisi]};",
      "legend": "• SUM(): Menghitung total akumulasi nilai numerik<br>• GROUP BY: Mengelompokkan baris berdasarkan nilai kolom penentu<br>• WHERE memfilter sebelum agregasi, sedangkan HAVING memfilter setelah agregasi"
    },
    "options": [
      {
        "key": "A",
        "text": "`SELECT kategori_produk, COUNT(jumlah_terjual) FROM Penjualan WHERE SUM(jumlah_terjual) > 0;`"
      },
      {
        "key": "B",
        "text": "`SELECT DISTINCT kategori_produk, jumlah_terjual FROM Penjualan ORDER BY kategori_produk;`"
      },
      {
        "key": "C",
        "text": "`SELECT kategori_produk, SUM(jumlah_terjual) FROM Penjualan GROUP BY kategori_produk;`"
      },
      {
        "key": "D",
        "text": "`SELECT kategori_produk, AVG(jumlah_terjual) FROM Penjualan HAVING kategori_produk IS NOT NULL;`"
      },
      {
        "key": "E",
        "text": "`SELECT TOTAL(jumlah_terjual) IN Penjualan GROUPED BY kategori_produk;`"
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) `SELECT kategori_produk, SUM(jumlah_terjual) FROM Penjualan GROUP BY kategori_produk;`. Untuk menghitung total unit per kategori, gunakan fungsi SUM(jumlah_terjual) dan klausul GROUP BY kategori_produk. Pilih: SELECT kategori_produk, SUM(jumlah_terjual) FROM Penjualan GROUP BY kategori_produk;"
  },
  {
    "id": "inf-lat-e-14",
    "materi": "SISTEM KOMPUTER",
    "topic": "Konversi Sistem Bilangan Biner ke Desimal",
    "hints": {
      "concept": "Jumlahkan bobot pangkat dua: bit ke-7 (128) + bit ke-5 (32) + bit ke-4 (16) + bit ke-1 (2) = 178.",
      "execution": "Pilih: 178."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah nilai biner 8-bit tanpa tanda (unsigned 8-bit binary) yang tersimpan di dalam register prosesor adalah `10110010_2`. Nilai representasi bilangan tersebut dalam sistem desimal berbasis 10 adalah...",
    "formulaHud": {
      "title": "KONVERSI BILANGAN BINER KE DESIMAL",
      "latex": "N_{10} = \\sum_{i=0}^{n-1} b_i \\cdot 2^i = 128 + 0 + 32 + 16 + 0 + 0 + 2 + 0 = 178_{10}",
      "legend": "• Bit posisi: b7=1 (128), b6=0 (0), b5=1 (32), b4=1 (16), b3=0 (0), b2=0 (0), b1=1 (2), b0=0 (0)<br>• Total desimal: 128 + 32 + 16 + 2 = 178"
    },
    "options": [
      {
        "key": "A",
        "text": "$162_{10}$, hasil penjumlahan dari bit-bit aktif tanpa memperhitungkan bobot pangkat kelipatan dua menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "$194_{10}$, hasil konversi dengan membalik nilai bit terendah (least significant bit)."
      },
      {
        "key": "C",
        "text": "$146_{10}$, hasil konversi kesalahan membaca bit pembobot orde ketiga dan keempat."
      },
      {
        "key": "D",
        "text": "$178_{10}$, hasil dari $1\\cdot 2^7 + 0\\cdot 2^6 + 1\\cdot 2^5 + 1\\cdot 2^4 + 0\\cdot 2^3 + 0\\cdot 2^2 + 1\\cdot 2^1 + 0\\cdot 2^0 = 128 + 32 + 16 + 2 = 178$."
      },
      {
        "key": "E",
        "text": "$210_{10}$, hasil interpretasi langsung digit biner sebagai bilangan oktal desimal."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $178_{10}$, hasil dari $1\\cdot 2^7 + 0\\cdot 2^6 + 1\\cdot 2^5 + 1\\cdot 2^4 + 0\\cdot 2^3 + 0\\cdot 2^2 + 1\\cdot 2^1 + 0\\cdot 2^0 = 128 + 32 + 16 + 2 = 178$.. Jumlahkan bobot pangkat dua: bit ke-7 (128) + bit ke-5 (32) + bit ke-4 (16) + bit ke-1 (2) = 178. Pilih: 178."
  },
  {
    "id": "inf-lat-e-15",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Perbandingan Karakteristik Protokol TCP vs UDP",
    "hints": {
      "concept": "UDP dipilih untuk live streaming karena rendah latensi (overhead kecil tanpa retransmisi paket rusak).",
      "execution": "Pilih: UDP connectionless dan meminimalkan latensi tanpa retransmisi."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Aplikasi streaming video langsung (live streaming) dan panggilan suara interaktif VoIP umumnya lebih memilih menggunakan protokol UDP (User Datagram Protocol) daripada TCP (Transmission Control Protocol). Alasan teknis utama di balik pemilihan tersebut adalah...",
    "formulaHud": {
      "title": "KOMPARASI PROTOKOL TRANSPORT (LAYER 4)",
      "latex": "\\begin{aligned} \\text{TCP:} & \\quad \\text{Connection-oriented}, \\ 3\\text{-way Handshake}, \\ \\text{Reliable (Retransmisi)}, \\ \\text{Latensi Tinggi} \\\\ \\text{UDP:} & \\quad \\text{Connectionless}, \\ \\text{No Handshake}, \\ \\text{Unreliable (Best Effort)}, \\ \\text{Latensi Super Rendah} \\end{aligned}",
      "legend": "• TCP cocok untuk: Web browsing (HTTP/HTTPS), email (SMTP/IMAP), transfer berkas (FTP)<br>• UDP cocok untuk: Live video streaming, gaming online kompetitif, DNS query, VoIP"
    },
    "options": [
      {
        "key": "A",
        "text": "UDP menjamin 100% data pasti sampai secara utuh dan berurutan tanpa ada satu bit pun yang rusak diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "UDP secara otomatis mengenkripsi seluruh muatan data menggunakan algoritma AES-256 tingkat militer."
      },
      {
        "key": "C",
        "text": "UDP menggunakan jalur transmisi fisik gelombang radio terpisah yang kebal terhadap kemacetan kabel optik."
      },
      {
        "key": "D",
        "text": "TCP dilarang oleh konsorsium web internasional untuk mentransmisikan data multimedia grafis."
      },
      {
        "key": "E",
        "text": "UDP bersifat connectionless dan meminimalkan latensi tunda (overhead rendah) tanpa mekanisme handshaking dan retransmisi paket yang hilang, sehingga transmisi real-time berjalan lancar."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) UDP bersifat connectionless dan meminimalkan latensi tunda (overhead rendah) tanpa mekanisme handshaking dan retransmisi paket yang hilang, sehingga transmisi real-time berjalan lancar.. UDP dipilih untuk live streaming karena rendah latensi (overhead kecil tanpa retransmisi paket rusak). Pilih: UDP connectionless dan meminimalkan latensi tanpa retransmisi."
  },
  {
    "id": "inf-lat-e-16",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Fungsi Rekursif dan Peran Vital Base Case",
    "hints": {
      "concept": "Kondisi penghenti pemanggilan rekursif disebut Base Case.",
      "execution": "Pilih: Base Case (Kondisi Basis)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam pemrograman, sebuah fungsi rekursif memanggil dirinya sendiri secara berulang. Bagian terpenting yang wajib didefinisikan di awal fungsi rekursif untuk mencegah program mengalami galat kehabisan memori (_Stack Overflow_) adalah...",
    "formulaHud": {
      "title": "STRUKTUR UMUM ALGORITMA REKURSIF",
      "latex": "f(n) = \\begin{cases} \\text{Nilai Konstan} & \\text{jika } n \\le \\text{kondisi\\_basis (Base Case)} \\\\ f(n - 1) + g(n) & \\text{jika } n > \\text{kondisi\\_basis (Recursive Case)} \\end{cases}",
      "legend": "• Tanpa Base Case: Call stack akan terus bertambah hingga batas memori terlampaui (Stack Overflow)<br>• Setiap panggilan rekursif harus memodifikasi argumen menuju ke arah kondisi basis"
    },
    "options": [
      {
        "key": "A",
        "text": "Base Case (Kondisi Basis), yaitu kondisi pemberhentian eksplisit yang menghentikan rantai pemanggilan rekursif dan mengembalikan nilai konstan."
      },
      {
        "key": "B",
        "text": "Recursive Step, yaitu pernyataan baris kode yang memanggil kembali nama fungsi dengan parameter membesar sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Global Variable, yaitu deklarasi variabel di luar lingkup fungsi untuk menampung riwayat iterasi."
      },
      {
        "key": "D",
        "text": "Looping While, yaitu sintaksis perulangan bersarang yang memaksa fungsi keluar dari memori secara paksa."
      },
      {
        "key": "E",
        "text": "Exception Handler, yaitu blok kode try-catch untuk menangani kegagalan eksekusi compiler sistem."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Base Case (Kondisi Basis), yaitu kondisi pemberhentian eksplisit yang menghentikan rantai pemanggilan rekursif dan mengembalikan nilai konstan.. Kondisi penghenti pemanggilan rekursif disebut Base Case. Pilih: Base Case (Kondisi Basis)."
  },
  {
    "id": "inf-lat-e-17",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Ancaman Kejahatan Siber Rekayasa Sosial (Social Engineering)",
    "hints": {
      "concept": "Menyamar sebagai pihak tepercaya via email palsu untuk mencuri data pribadi adalah Phishing.",
      "execution": "Pilih: Phishing."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Seorang pegawai kantor menerima surel palsu yang mengatasnamakan manajer bank resmi dan mendesaknya untuk segera mengklik tautan formulir agar rekening tabungannya tidak diblokir. Serangan siber manipulasi psikologis manusia semacam ini diklasifikasikan sebagai...",
    "formulaHud": {
      "title": "TAKSONOMI SERANGAN REKAYASA SOSIAL (SOCIAL ENGINEERING)",
      "latex": "\\text{Social Engineering} \\implies \\text{Manipulasi Psikologis (Urgensi/Ketakutan)} \\to \\text{Pencurian Identitas/Kredensial}",
      "legend": "• Phishing: Serangan massal via surel palsu<br>• Spear Phishing: Serangan terarah ke individu/eksekutif tertentu<br>• Smishing / Vishing: Phishing via SMS / panggilan suara<br>• Mitigasi: Verifikasi domain alamat pengirim dan aktifkan MFA (Multi-Factor Authentication)"
    },
    "options": [
      {
        "key": "A",
        "text": "Distributed Denial of Service (DDoS), yaitu membanjiri server korban dengan jutaan permintaan palsu hingga tumbang sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Phishing, yaitu bentuk rekayasa sosial yang berupaya memancing korban untuk membocorkan informasi kredensial sensitif dengan menyamar sebagai institusi tepercaya."
      },
      {
        "key": "C",
        "text": "SQL Injection, yaitu menyisipkan kode kueri manipulatif ke dalam kolom formulir masukan web aplikasi."
      },
      {
        "key": "D",
        "text": "Cross-Site Scripting (XSS), yaitu menyuntikkan skrip berbahaya ke dalam halaman peramban pengguna lain."
      },
      {
        "key": "E",
        "text": "Ransomware, yaitu mengeksekusi enkripsi sepihak terhadap seluruh berkas komputer korban demi tebusan uang."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Phishing, yaitu bentuk rekayasa sosial yang berupaya memancing korban untuk membocorkan informasi kredensial sensitif dengan menyamar sebagai institusi tepercaya.. Menyamar sebagai pihak tepercaya via email palsu untuk mencuri data pribadi adalah Phishing. Pilih: Phishing."
  },
  {
    "id": "inf-lat-e-18",
    "materi": "STRUKTUR DATA",
    "topic": "Karakteristik Traversal In-Order pada Binary Search Tree (BST)",
    "hints": {
      "concept": "In-Order pada BST (Kiri < Akar < Kanan) otomatis menghasilkan barisan terurut menaik (sorted ascending).",
      "execution": "Pilih: Terurut menaik (ascending) dari nilai terkecil hingga terbesar."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Diberikan sebuah Pohon Pencarian Biner (Binary Search Tree / BST) yang valid. Jika dilakukan penelusuran simpul dengan metode traversal In-Order (Kiri $\\rightarrow$ Akar $\\rightarrow$ Kanan), barisan data simpul yang dicetak akan selalu memiliki sifat...",
    "formulaHud": {
      "title": "TRAVERSAL POHON BINER PENCARIAN (BST)",
      "latex": "\\text{In-Order}(\\text{BST}) = \\text{In-Order}(\\text{Left}) \\cup \\{\\text{Root}\\} \\cup \\text{In-Order}(\\text{Right}) \\implies \\text{Sorted Ascending}",
      "legend": "• Sifat dasar BST: Semua kunci di Subtree Kiri < Kunci Akar < Semua kunci di Subtree Kanan<br>• Pre-Order: Root -> Left -> Right (berguna untuk duplikasi struktur pohon)<br>• Post-Order: Left -> Right -> Root (berguna untuk pembebasan memori / kalkulasi postfix)"
    },
    "options": [
      {
        "key": "A",
        "text": "Terurut menurun (descending) dimulai dari simpul daun terbesar menuju simpul akar ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Tercetak berdasarkan urutan kronologis waktu penyisipan simpul data ke dalam memori komputer."
      },
      {
        "key": "C",
        "text": "Terurut menaik (ascending) secara monotonik dari nilai simpul terkecil hingga simpul terbesar."
      },
      {
        "key": "D",
        "text": "Tercetak tingkat demi tingkat (level by level) dari kedalaman pohon paling atas ke bawah."
      },
      {
        "key": "E",
        "text": "Acak tidak berpola karena struktur pohon biner bersifat dinamis dan non-sekuensial."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Terurut menaik (ascending) secara monotonik dari nilai simpul terkecil hingga simpul terbesar.. In-Order pada BST (Kiri < Akar < Kanan) otomatis menghasilkan barisan terurut menaik (sorted ascending). Pilih: Terurut menaik (ascending) dari nilai terkecil hingga terbesar."
  },
  {
    "id": "inf-lat-e-19",
    "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
    "topic": "Fitur Otomasi Surat Massal Mail Merge",
    "hints": {
      "concept": "Menggabungkan dokumen master dengan data tabel untuk surat massal adalah fitur Mail Merge.",
      "execution": "Pilih: Mail Merge."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam aplikasi pengolah dokumen perkantoran, staf administrasi diminta mencetak 500 lembar surat undangan resmi yang memiliki format teks identik namun nama penerima, nomor induk, dan alamatnya berbeda-beda untuk tiap orang. Fitur aplikasi yang paling tepat dan efisien digunakan adalah...",
    "formulaHud": {
      "title": "PRINSIP KERJA OTOMASI MAIL MERGE",
      "latex": "\\text{Template Dokumen Master} + \\text{Sumber Data Tabular (Excel/DB)} \\xrightarrow{\\text{Merge Fields}} \\prod_{i=1}^{n} \\text{Dokumen Terpersonalisasi}",
      "legend": "• Main Document: Format statis surat undangan<br>• Data Source: Berkas spreadsheet berisi baris data penerima<br>• Merge Fields: Placeholder dinamis (misal: «Nama», «Alamat»)"
    },
    "options": [
      {
        "key": "A",
        "text": "Track Changes, yang melacak riwayat suntingan dan catatan revisi antar beberapa editor dokumen menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "AutoCorrect, yang otomatis memperbaiki kesalahan ketik ejaan kata sesuai kamus tata bahasa."
      },
      {
        "key": "C",
        "text": "Hyperlink Embedding, yang menyematkan tautan pranala web ke dalam teks surat undangan fisik."
      },
      {
        "key": "D",
        "text": "Mail Merge, yang mengintegrasikan dokumen template master dengan sumber data eksternal (tabel spreadsheet atau basis data) untuk menghasilkan dokumen personal secara otomatis."
      },
      {
        "key": "E",
        "text": "Macros Scripting, yang wajib memprogram kode mesin assembly untuk mengatur margin tata letak cetak."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Mail Merge, yang mengintegrasikan dokumen template master dengan sumber data eksternal (tabel spreadsheet atau basis data) untuk menghasilkan dokumen personal secara otomatis.. Menggabungkan dokumen master dengan data tabel untuk surat massal adalah fitur Mail Merge. Pilih: Mail Merge."
  },
  {
    "id": "inf-lat-e-20",
    "materi": "ANALISIS DATA",
    "topic": "Prinsip Bentuk Normal Pertama (1NF) Basis Data",
    "hints": {
      "concept": "1NF mensyaratkan setiap kolom memiliki nilai atomik (nilai tunggal yang tidak bisa dipecah lagi) dan bebas perulangan nilai dalam satu sel.",
      "execution": "Pilih: Memastikan setiap kolom memuat nilai tunggal yang atomik dan menghilangkan repeating groups."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Sebuah tabel data siswa memiliki kolom `hobi` yang berisi nilai gabungan beberapa teks seperti `'Membaca, Futsal, Musik'` dalam satu baris sel data. Untuk memenuhi aturan Bentuk Normal Pertama (1st Normal Form / 1NF), langkah yang wajib dilakukan adalah...",
    "formulaHud": {
      "title": "ATURAN BENTUK NORMAL PERTAMA (1NF)",
      "latex": "\\forall r \\in R, \\forall A \\in \\text{Attributes}(R) : \\quad \\text{Nilai}(r, A) \\in \\text{Domain Atomik}",
      "legend": "• 1NF: Nilai atribut wajib atomik (tidak bernilai jamak/kumpulan data dalam satu sel)<br>• 2NF: Memenuhi 1NF dan tidak memiliki ketergantungan fungsional parsial (partial dependency)<br>• 3NF: Memenuhi 2NF dan tidak memiliki ketergantungan transitif (transitive dependency)"
    },
    "options": [
      {
        "key": "A",
        "text": "Menghapus seluruh baris data siswa yang memiliki lebih dari satu jenis hobi secara permanen diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Menambahkan kunci asing (Foreign Key) ke tabel lain tanpa mengubah komposisi nilai sel kolom hobi."
      },
      {
        "key": "C",
        "text": "Mengenkripsi kolom hobi menjadi kode biner rahasia agar tidak dapat dibaca oleh pengguna biasa."
      },
      {
        "key": "D",
        "text": "Mengubah nama kolom hobi menjadi hobi_1, hobi_2, hobi_3 hingga puluhan kolom kosong tak terbatas."
      },
      {
        "key": "E",
        "text": "Menghilangkan nilai berulang (repeating groups) dan memastikan setiap kolom hanya memuat nilai tunggal yang atomik (atomic value) pada setiap baris rekaman."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Menghilangkan nilai berulang (repeating groups) dan memastikan setiap kolom hanya memuat nilai tunggal yang atomik (atomic value) pada setiap baris rekaman.. 1NF mensyaratkan setiap kolom memiliki nilai atomik (nilai tunggal yang tidak bisa dipecah lagi) dan bebas perulangan nilai dalam satu sel. Pilih: Memastikan setiap kolom memuat nilai tunggal yang atomik dan menghilangkan repeating groups."
  },
  {
    "id": "inf-lat-e-21",
    "materi": "SISTEM KOMPUTER",
    "topic": "Perbedaan Perangkat Lunak Sistem vs Perangkat Lunak Aplikasi",
    "hints": {
      "concept": "Perangkat lunak sistem bertugas mengelola sumber daya perangkat keras dan platform dasar komputasi.",
      "execution": "Pilih: Mengelola sumber daya perangkat keras dan menyediakan antarmuka dasar bagi perangkat lunak lain."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Perangkat lunak pada sistem komputasi diklasifikasikan menjadi perangkat lunak sistem (system software) dan perangkat lunak aplikasi (application software). Karakteristik pembeda utama perangkat lunak sistem adalah...",
    "formulaHud": {
      "title": "LAPISAN EKOSISTEM KOMPUTASI",
      "latex": "\\text{User} \\leftrightarrow \\text{Application Software} \\leftrightarrow \\text{Operating System (System Software)} \\leftrightarrow \\text{Hardware}",
      "legend": "• System Software: Kernel OS, Device Drivers, Firmware, Utility pengelola disk<br>• Application Software: Web browser, Word processor, Video editor, Game"
    },
    "options": [
      {
        "key": "A",
        "text": "Berfungsi mengelola dan mengontrol sumber daya perangkat keras secara langsung serta menyediakan antarmuka dasar bagi perangkat lunak lain untuk berjalan, contohnya Linux, Windows, dan driver perangkat."
      },
      {
        "key": "B",
        "text": "Didesain khusus untuk membantu pengguna menyelesaikan tugas spesifik personal seperti mengedit gambar dan berselancar web sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Selalu ditulis menggunakan bahasa pemrograman web seperti HTML dan CSS tanpa mengakses komponen memori CPU."
      },
      {
        "key": "D",
        "text": "Hanya dapat dijalankan apabila komputer terhubung secara aktif dengan jaringan internet pita lebar nirkabel."
      },
      {
        "key": "E",
        "text": "Bersifat opsional dan komputer tetap dapat beroperasi menjalankan aplikasi pengolah kata tanpa adanya sistem operasi."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Berfungsi mengelola dan mengontrol sumber daya perangkat keras secara langsung serta menyediakan antarmuka dasar bagi perangkat lunak lain untuk berjalan, contohnya Linux, Windows, dan driver perangkat.. Perangkat lunak sistem bertugas mengelola sumber daya perangkat keras dan platform dasar komputasi. Pilih: Mengelola sumber daya perangkat keras dan menyediakan antarmuka dasar bagi perangkat lunak lain."
  },
  {
    "id": "inf-lat-e-22",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Fungsi dan Alur Kerja Domain Name System (DNS)",
    "hints": {
      "concept": "Menerjemahkan nama domain manusia menjadi alamat IP numerik komputer adalah tugas DNS.",
      "execution": "Pilih: Domain Name System (DNS)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Ketika seorang pengguna mengetik alamat `www.kemdikbud.go.id` pada bilah alamat peramban web, peramban tidak dapat langsung terhubung ke server tujuan tanpa mengetahui alamat numerik server tersebut. Layanan jaringan internet yang bertugas menerjemahkan nama domain yang mudah dibaca manusia menjadi alamat IP numerik mesin adalah...",
    "formulaHud": {
      "title": "MEKANISME RESOLUSI DOMAIN NAME SYSTEM (DNS)",
      "latex": "\\text{FQDN (kemdikbud.go.id)} \\xrightarrow{\\text{DNS Query (Port 53 UDP)}} \\text{DNS Hierarchy (Root } \\to \\text{ TLD } \\to \\text{ Authoritative)} \\to \\text{IP: 118.98.x.x}",
      "legend": "• Rekursif Resolver: Membantu klien mencari IP ke DNS bertingkat<br>• DNS Record A: Memetakan domain ke IPv4<br>• DNS Record AAAA: Memetakan domain ke IPv6<br>• DNS Record CNAME: Alias nama domain"
    },
    "options": [
      {
        "key": "A",
        "text": "Dynamic Host Configuration Protocol (DHCP), yang otomatis membagikan konfigurasi IP ke komputer klien lokal sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Domain Name System (DNS), yang bekerja sebagai buku telepon global internet yang memetakan FQDN ke alamat IP publik server tujuan."
      },
      {
        "key": "C",
        "text": "Simple Mail Transfer Protocol (SMTP), yang bertugas mengirimkan pesan surel antar server pos elektronik."
      },
      {
        "key": "D",
        "text": "Network Address Translation (NAT), yang memodifikasi informasi header paket untuk berbagi satu IP publik."
      },
      {
        "key": "E",
        "text": "Address Resolution Protocol (ARP), yang memetakan alamat IP logis ke MAC Address fisik dalam satu subnet LAN."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Domain Name System (DNS), yang bekerja sebagai buku telepon global internet yang memetakan FQDN ke alamat IP publik server tujuan.. Menerjemahkan nama domain manusia menjadi alamat IP numerik komputer adalah tugas DNS. Pilih: Domain Name System (DNS)."
  },
  {
    "id": "inf-lat-e-23",
    "materi": "PRAKTIK LINTAS BIDANG",
    "topic": "Operasi Dasar Version Control System Git",
    "hints": {
      "concept": "Perintah untuk menyimpan snapshot berkas dari staging area ke repositori lokal beserta pesan adalah git commit -m.",
      "execution": "Pilih: git commit -m \"Pesan deskripsi perubahan\"."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Dalam pengembangan proyek perangkat lunak menggunakan sistem kendali versi Git, seorang pengembang telah selesai memodifikasi kode program dan menambahkan berkas perubahan ke staging area menggunakan `git add .`. Perintah Git yang tepat untuk menyimpan rekaman snapshot perubahan tersebut ke repositori lokal dengan menyertakan pesan deskriptif adalah...",
    "formulaHud": {
      "title": "SIKLUS TIGA POHON SISTEM GIT (THREE-TREE ARCHITECTURE)",
      "latex": "\\text{Working Directory} \\xrightarrow{\\text{git add}} \\text{Staging Area (Index)} \\xrightarrow{\\text{git commit}} \\text{Local Repository} \\xrightarrow{\\text{git push}} \\text{Remote Repo}",
      "legend": "• git add: Menandai file yang akan disimpan ke commit berikutnya<br>• git commit: Menyimpan snapshot permanen di basis data riwayat lokal<br>• git push: Mengirim commit lokal ke server kolaborasi daring (GitHub/GitLab)"
    },
    "options": [
      {
        "key": "A",
        "text": "`git push origin main` ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "`git checkout -b branch_baru`"
      },
      {
        "key": "C",
        "text": "`git commit -m \"Pesan deskripsi perubahan\"`"
      },
      {
        "key": "D",
        "text": "`git pull upstream master`"
      },
      {
        "key": "E",
        "text": "`git clone https://repository.git`"
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) `git commit -m \"Pesan deskripsi perubahan\"`. Perintah untuk menyimpan snapshot berkas dari staging area ke repositori lokal beserta pesan adalah git commit -m. Pilih: git commit -m \"Pesan deskripsi perubahan\"."
  },
  {
    "id": "inf-lat-e-24",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Mekanisme dan Kompleksitas Algoritma Pengurutan Bubble Sort",
    "hints": {
      "concept": "Bubble sort worst-case memiliki perulangan bersarang n x n, sehingga kompleksitasnya adalah O(n^2).",
      "execution": "Pilih: O(n^2)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Algoritma pengurutan Bubble Sort bekerja dengan cara membandingkan pasangan elemen yang bersebelahan secara berulang dan menukarnya jika urutannya salah. Jika sebuah array memiliki $n$ elemen dan berada dalam keadaan terurut terbalik (worst case), kompleksitas waktu asimtotik dari Bubble Sort adalah...",
    "formulaHud": {
      "title": "KOMPLEKSITAS ASIMTOTIK PENGURUTAN BUBBLE SORT",
      "latex": "T_{\\text{worst}}(n) = \\sum_{i=1}^{n-1} i = \\frac{n(n - 1)}{2} = \\frac{1}{2}n^2 - \\frac{1}{2}n \\implies O(n^2)",
      "legend": "• Worst Case (Terurut Terbalik): $O(n^2)$ perbandingan dan penukaran<br>• Best Case (Sudah Terurut dengan flag optimasi): $O(n)$<br>• Algoritma pengurutan efisien ($O(n \\log n)$): Merge Sort, Quick Sort, Heap Sort"
    },
    "options": [
      {
        "key": "A",
        "text": "$O(n \\log n)$, karena algoritma memanfaatkan teknik memecah dan menaklukkan array menjadi dua bagian simetris menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "$O(n)$, karena algoritma hanya memerlukan satu kali lintasan pemeriksaan dari indeks awal ke akhir."
      },
      {
        "key": "C",
        "text": "$O(1)$, karena penukaran elemen selalu dilakukan secara instan di dalam memori register konstan."
      },
      {
        "key": "D",
        "text": "$O(n^2)$, karena algoritma membutuhkan sekitar $\\frac{n(n-1)}{2}$ kali operasi perbandingan dan penukaran elemen."
      },
      {
        "key": "E",
        "text": "$O(\\log n)$, karena setiap iterasi berhasil mengeliminasi separuh dari total data yang belum terurut."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) $O(n^2)$, karena algoritma membutuhkan sekitar $\\frac{n(n-1)}{2}$ kali operasi perbandingan dan penukaran elemen.. Bubble sort worst-case memiliki perulangan bersarang n x n, sehingga kompleksitasnya adalah O(n^2). Pilih: O(n^2)."
  },
  {
    "id": "inf-lat-e-25",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Etika Perangkat Lunak dan Lisensi Sumber Terbuka (Open Source)",
    "hints": {
      "concept": "Lisensi open source memberikan kebebasan melihat, memodifikasi, dan mendistribusikan kode dengan menyertakan atribusi.",
      "execution": "Pilih opsi yang menjamin kebebasan akses, modifikasi, dan distribusi dengan mencantumkan atribusi hak cipta asli."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "questionHtml": "Banyak perangkat lunak modern didistribusikan di bawah lisensi Open Source permisif seperti Lisensi MIT atau Lisensi Apache 2.0. Hak paling mendasar yang diberikan oleh lisensi sumber terbuka kepada pengembang perangkat lunak lain adalah...",
    "formulaHud": {
      "title": "KATEGORI LISENSI PERANGKAT LUNAK",
      "latex": "\\begin{aligned} \\text{Proprietary (Closed Source):} & \\quad \\text{Kode sumber rahasia, hak cipta dilindungi penuh (EULA)} \\\\ \\text{Copyleft (GPL):} & \\quad \\text{Turunan wajib berlisensi terbuka yang sama} \\\\ \\text{Permissive (MIT/Apache):} & \\quad \\text{Bebas digunakan & dikomersialkan dengan atribusi hak cipta} \\end{aligned}",
      "legend": "• OSI (Open Source Initiative): Standar 10 kriteria perangkat lunak sumber terbuka<br>• Atribusi: Menyertakan notice hak cipta asli dalam salinan berkas lisensi"
    },
    "options": [
      {
        "key": "A",
        "text": "Kewajiban untuk membayar royalti bulanan kepada pencipta asli apabila perangkat lunak dijalankan di komputer kantor diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Larangan keras untuk membaca baris kode sumber asli demi melindungi hak paten rahasia dagang pencipta."
      },
      {
        "key": "C",
        "text": "Kewajiban untuk menyerahkan seluruh hak milik intelektual ciptaan baru kepada pemilik repositori induk."
      },
      {
        "key": "D",
        "text": "Keharusan mengunci kode hasil modifikasi agar tidak dapat diakses oleh sistem operasi berbasis Unix."
      },
      {
        "key": "E",
        "text": "Kebebasan untuk melihat, memodifikasi, mendistribusikan ulang, dan menggunakan kode sumber baik untuk keperluan non-komersial maupun komersial dengan tetap mencantumkan atribusi hak cipta pencipta aslinya."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Kebebasan untuk melihat, memodifikasi, mendistribusikan ulang, dan menggunakan kode sumber baik untuk keperluan non-komersial maupun komersial dengan tetap mencantumkan atribusi hak cipta pencipta aslinya.. Lisensi open source memberikan kebebasan melihat, memodifikasi, dan mendistribusikan kode dengan menyertakan atribusi. Pilih opsi yang menjamin kebebasan akses, modifikasi, dan distribusi dengan mencantumkan atribusi hak cipta asli."
  },
  {
    "id": "inf-lat-m-01",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Pemrograman Dinamis (Dynamic Programming) vs Divide and Conquer",
    "hints": {
      "concept": "Syarat mutlak DP: Overlapping subproblems (sub-masalah tumpang tindih) dan optimal substructure. Hasil disimpan agar tidak dihitung ulang.",
      "execution": "Pilih opsi yang menyebutkan Sub-masalah Tumpang Tindih (Overlapping Subproblems) dan Struktur Bawah Optimal."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dalam menghitung bilangan Fibonacci ke-$n$, pendekatan rekursif naif memiliki kompleksitas waktu eksponensial $O(2^n)$ karena mengevaluasi ulang sub-masalah yang sama berulang kali. Pendekatan Pemrograman Dinamis (Dynamic Programming) dengan teknik memoization atau tabulasi mampu menurunkan kompleksitas waktu menjadi $O(n)$ linier. Alasan konseptual mengapa teknik DP efektif pada masalah ini adalah...",
    "formulaHud": {
      "title": "PRINSIP PEMROGRAMAN DINAMIS (DYNAMIC PROGRAMMING)",
      "latex": "F(n) = F(n-1) + F(n-2), \\quad \\text{MemoTable}[n] \\implies \\text{Kompleksitas: } O(2^n) \\xrightarrow{\\text{DP}} O(n)",
      "legend": "• Overlapping Subproblems: Sub-masalah yang sama dihitung berulang kali<br>• Optimal Substructure: Solusi optimal masalah utama dibentuk dari solusi optimal sub-masalahnya<br>• Memoization (Top-down): Rekursi + Caching; Tabulation (Bottom-up): Iterasi tabel"
    },
    "options": [
      {
        "key": "A",
        "text": "Masalah memiliki sifat Sub-masalah Tumpang Tindih (Overlapping Subproblems) dan Struktur Bawah Optimal (Optimal Substructure), sehingga hasil sub-masalah disimpan sekali dan dapat langsung digunakan kembali tanpa komputasi ulang."
      },
      {
        "key": "B",
        "text": "Masalah membagi data menjadi dua himpunan independen yang tidak pernah saling beririsan seperti halnya Merge Sort sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Masalah mengubah proses perhitungan menjadi fungsi acak nondeterministik yang kebal terhadap galat rekursi."
      },
      {
        "key": "D",
        "text": "Masalah mengeliminasi seluruh operasi penambahan aritmetika dengan menggantikannya menjadi operasi pergeseran bitwise konstan."
      },
      {
        "key": "E",
        "text": "Masalah secara otomatis mengalokasikan memori grafis GPU untuk menjalankan komputasi paralel secara fisik."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Masalah memiliki sifat Sub-masalah Tumpang Tindih (Overlapping Subproblems) dan Struktur Bawah Optimal (Optimal Substructure), sehingga hasil sub-masalah disimpan sekali dan dapat langsung digunakan kembali tanpa komputasi ulang.. Syarat mutlak DP: Overlapping subproblems (sub-masalah tumpang tindih) dan optimal substructure. Hasil disimpan agar tidak dihitung ulang. Pilih opsi yang menyebutkan Sub-masalah Tumpang Tindih (Overlapping Subproblems) dan Struktur Bawah Optimal."
  },
  {
    "id": "inf-lat-m-02",
    "materi": "SISTEM KOMPUTER",
    "topic": "Manajemen Memori Virtual: Paging dan Fenomena Page Fault",
    "hints": {
      "concept": "Akses halaman yang belum ada di RAM memicu interrupt Page Fault. OS memuat halaman dari disk ke RAM lalu mengulang instruksi.",
      "execution": "Pilih: Terjadi Page Fault Interrupt; OS memuat halaman dari disk ke RAM."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dalam sistem operasi modern, memori virtual memungkinkan komputer menjalankan program yang membutuhkan ruang memori lebih besar daripada kapasitas RAM fisik melalui mekanisme paging. Jika CPU mencoba mengakses sebuah instruksi yang berada pada halaman memori (page) yang sedang tersimpan di penyimpanan sekunder (SSD) dan belum dimuat ke bingkai memori fisik (page frame), peristiwa yang terjadi adalah...",
    "formulaHud": {
      "title": "PENANGANAN KESALAHAN HALAMAN (PAGE FAULT HANDLING)",
      "latex": "\\text{Akses Memori} \\xrightarrow{\\text{Valid Bit = 0}} \\text{Trap/Page Fault} \\to \\text{OS Baca Disk} \\to \\text{Load ke Frame RAM} \\to \\text{Update Page Table (Valid Bit = 1)} \\to \\text{Restart Instruksi}",
      "legend": "• Page Table: Memetakan alamat logika (Virtual Page Number) ke alamat fisik (Frame Number)<br>• Thrashing: Kondisi sistem terlalu sibuk melakukan swap paging daripada mengeksekusi proses akibat kehabisan RAM"
    },
    "options": [
      {
        "key": "A",
        "text": "Terjadi Segmentation Fault permanen yang langsung menghentikan paksa (crash) sistem operasi seketika sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Terjadi Page Fault Interrupt; sistem operasi menangguhkan proses aktif, mencari halaman yang diminta di secondary storage, memuatnya ke frame RAM kosong, memperbarui page table, lalu melanjutkan eksekusi proses."
      },
      {
        "key": "C",
        "text": "CPU langsung beralih mengeksekusi instruksi berikutnya secara acak tanpa mempedulikan data yang hilang."
      },
      {
        "key": "D",
        "text": "Sistem operasi otomatis menghapus seluruh isi memori RAM fisik untuk mencegah kerusakan perangkat keras."
      },
      {
        "key": "E",
        "text": "Prosesor menaikkan kecepatan frekuensi clock secara instan untuk menciptakan modul memori semikonduktor baru."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Terjadi Page Fault Interrupt; sistem operasi menangguhkan proses aktif, mencari halaman yang diminta di secondary storage, memuatnya ke frame RAM kosong, memperbarui page table, lalu melanjutkan eksekusi proses.. Akses halaman yang belum ada di RAM memicu interrupt Page Fault. OS memuat halaman dari disk ke RAM lalu mengulang instruksi. Pilih: Terjadi Page Fault Interrupt; OS memuat halaman dari disk ke RAM."
  },
  {
    "id": "inf-lat-m-03",
    "materi": "STRUKTUR DATA",
    "topic": "Analisis Efisiensi Penyisipan Elemen: Linked List vs Array Dinamis",
    "hints": {
      "concept": "Menyisipkan di awal: Array butuh shifting semua elemen (O(n)), sedangkan Linked List hanya mengubah pointer head (O(1)).",
      "execution": "Pilih opsi: Linked List memiliki kompleksitas penyisipan O(1) konstan sedangkan Array butuh O(n) karena shifting."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi memerlukan operasi penyisipan data baru secara terus-menerus tepat di posisi indeks paling awal (elemen terdepan). Dibandingkan dengan struktur data Array Dinamis berukuran $n$, struktur data Singly Linked List lebih unggul untuk kebutuhan operasi ini karena...",
    "formulaHud": {
      "title": "KOMPARASI OPERASI PENYISIPAN DI ELEMEN TERDEPAN (INSERT AT HEAD)",
      "latex": "\\begin{aligned} \\text{Singly Linked List:} & \\quad \\text{newNode.next} = \\text{head}; \\ \\text{head} = \\text{newNode} \\implies O(1) \\\\ \\text{Dynamic Array:} & \\quad \\text{for } i = n \\text{ down to } 1 : A[i] = A[i-1] \\implies O(n) \\text{ Shifting} \\end{aligned}",
      "legend": "• Akses Acak (Index Access): Array $O(1)$, Linked List $O(n)$<br>• Penyisipan di Depan: Linked List $O(1)$, Array $O(n)$<br>• Overhead Memori: Linked List membutuhkan memori tambahan untuk penunjuk pointer (next)"
    },
    "options": [
      {
        "key": "A",
        "text": "Linked List menyimpan data dalam blok memori fisik yang berdampingan secara berurutan sehingga akses acaknya berkecepatan $O(1)$ ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Array dinamis tidak dapat dialokasikan kembali jika kapasitas awal memori sudah terpenuhi oleh data sebelumnya."
      },
      {
        "key": "C",
        "text": "Linked List memiliki kompleksitas penyisipan di awal sebesar $O(1)$ konstan karena hanya memperbarui penunjuk pointer `head`, sedangkan Array membutuhkan $O(n)$ karena harus menggeser (shifting) seluruh $n$ elemen yang ada ke kanan."
      },
      {
        "key": "D",
        "text": "Linked List secara otomatis mengurutkan elemen data dari yang terkecil ke terbesar setiap kali simpul baru disisipkan."
      },
      {
        "key": "E",
        "text": "Array membutuhkan alokasi memori dua kali lebih besar untuk setiap elemen data karena menyimpan alamat pointer ganda."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Linked List memiliki kompleksitas penyisipan di awal sebesar $O(1)$ konstan karena hanya memperbarui penunjuk pointer `head`, sedangkan Array membutuhkan $O(n)$ karena harus menggeser (shifting) seluruh $n$ elemen yang ada ke kanan.. Menyisipkan di awal: Array butuh shifting semua elemen (O(n)), sedangkan Linked List hanya mengubah pointer head (O(1)). Pilih opsi: Linked List memiliki kompleksitas penyisipan O(1) konstan sedangkan Array butuh O(n) karena shifting."
  },
  {
    "id": "inf-lat-m-04",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Kalkulasi Subnetting IPv4 Berbasis CIDR /27",
    "hints": {
      "concept": "/27 menyisakan 5 bit host (32 - 27 = 5). Total IP = 2^5 = 32. Host valid = 32 - 2 = 30. Broadcast = 64 + 31 = 95.",
      "execution": "Pilih: 30 host valid dan broadcast 192.168.10.95."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah laboratorium komputer sekolah diberikan blok alamat jaringan IPv4 `192.168.10.64/27`. Berdasarkan notasi CIDR tersebut, jumlah alamat host yang dapat dikonfigurasi secara valid pada komputer klien serta alamat broadcast dari subnet tersebut adalah...",
    "formulaHud": {
      "title": "FORMULA KALKULASI SUBNETTING IPV4",
      "latex": "\\text{Prefix /27} \\implies \\text{Host Bits } h = 32 - 27 = 5 \\implies \\text{Total IP} = 2^5 = 32 \\implies \\text{Host Valid} = 2^5 - 2 = 30",
      "legend": "• Network Address: 192.168.10.64 (IP pertama, tidak boleh untuk host)<br>• Rentang Host Valid: 192.168.10.65 s.d. 192.168.10.94 (30 host)<br>• Broadcast Address: 192.168.10.64 + 31 = 192.168.10.95 (IP terakhir subnet)"
    },
    "options": [
      {
        "key": "A",
        "text": "32 host valid, dengan alamat broadcast `192.168.10.96`."
      },
      {
        "key": "B",
        "text": "62 host valid, dengan alamat broadcast `192.168.10.127`."
      },
      {
        "key": "C",
        "text": "14 host valid, dengan alamat broadcast `192.168.10.79`."
      },
      {
        "key": "D",
        "text": "30 host valid, dengan alamat broadcast `192.168.10.95`."
      },
      {
        "key": "E",
        "text": "28 host valid, dengan alamat broadcast `192.168.10.92`."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) 30 host valid, dengan alamat broadcast `192.168.10.95`.. /27 menyisakan 5 bit host (32 - 27 = 5). Total IP = 2^5 = 32. Host valid = 32 - 2 = 30. Broadcast = 64 + 31 = 95. Pilih: 30 host valid dan broadcast 192.168.10.95."
  },
  {
    "id": "inf-lat-m-05",
    "materi": "ANALISIS DATA",
    "topic": "Perbedaan Karakteristik Relasi SQL INNER JOIN vs LEFT JOIN",
    "hints": {
      "concept": "Untuk menampilkan semua baris tabel kiri (Pelanggan) meskipun belum ada transaksi di tabel kanan, gunakan LEFT JOIN.",
      "execution": "Pilih: LEFT OUTER JOIN."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Diberikan tabel `Pelanggan` dan tabel `Pesanan` yang dihubungkan melalui atribut `id_pelanggan`. Seorang analis data ingin menampilkan daftar seluruh pelanggan yang terdaftar di sistem, termasuk pelanggan yang belum pernah melakukan pesanan sama sekali (kolom pesanan akan bernilai NULL). Klausa SQL JOIN yang tepat digunakan adalah...",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL OPERASI JOIN SQL",
      "latex": "\\begin{aligned} \\text{INNER JOIN:} & \\quad R \\bowtie_{R.A = S.A} S = \\{(r, s) \\mid r \\in R, s \\in S, r.A = s.A\\} \\\\ \\text{LEFT JOIN:} & \\quad R \\leftouterjoin_{R.A = S.A} S = (R \\bowtie S) \\cup \\{(r, \\text{NULL}) \\mid r \\in R, \\neg \\exists s \\in S (r.A = s.A)\\} \\end{aligned}",
      "legend": "• INNER JOIN: Hanya menampilkan data yang berelasi di kedua tabel<br>• LEFT JOIN: Menampilkan semua data tabel kiri, data kanan kosong diisi NULL<br>• Kasus penggunaan: Mencari entitas yang belum memiliki transaksi aktif"
    },
    "options": [
      {
        "key": "A",
        "text": "`INNER JOIN`, karena hanya mengembalikan baris yang memiliki nilai kecocokan di kedua tabel secara bersamaan diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "`RIGHT OUTER JOIN`, karena secara eksklusif hanya menampilkan data pesanan yang tidak memiliki identitas pembeli."
      },
      {
        "key": "C",
        "text": "`CROSS JOIN`, karena menghasilkan perkalian kartesian tanpa memperhatikan hubungan kunci asing sama sekali."
      },
      {
        "key": "D",
        "text": "`FULL OUTER JOIN`, karena hanya menampilkan baris yang tidak memiliki irisan sama sekali di kedua tabel."
      },
      {
        "key": "E",
        "text": "`LEFT OUTER JOIN`, karena akan mempertahankan seluruh baris dari tabel kiri (`Pelanggan`) dan mencocokkan data dari tabel kanan (`Pesanan`), mengisi nilai NULL jika tidak ada kecocokan."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) `LEFT OUTER JOIN`, karena akan mempertahankan seluruh baris dari tabel kiri (`Pelanggan`) dan mencocokkan data dari tabel kanan (`Pesanan`), mengisi nilai NULL jika tidak ada kecocokan.. Untuk menampilkan semua baris tabel kiri (Pelanggan) meskipun belum ada transaksi di tabel kanan, gunakan LEFT JOIN. Pilih: LEFT OUTER JOIN."
  },
  {
    "id": "inf-lat-m-06",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Analisis Kompleksitas Waktu Divide and Conquer pada Merge Sort",
    "hints": {
      "concept": "Merge sort memiliki kedalaman rekursi log(n) dan merge linier n pada tiap level, sehingga T(n) = O(n log n) di semua kasus.",
      "execution": "Pilih: O(n log n) pada semua kasus."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Algoritma Merge Sort mengurutkan larik berukuran $n$ dengan membagi larik menjadi dua sub-larik yang sama besar secara rekursif, mengurutkan masing-masing sub-larik, lalu menggabungkannya kembali (merge). Relasi rekurensi waktu dari Merge Sort dirumuskan sebagai $T(n) = 2T(n/2) + O(n)$. Berdasarkan Teorema Master, kompleksitas waktu asimtotik dari Merge Sort adalah...",
    "formulaHud": {
      "title": "TEOREMA MASTER PADA ALGORITMA MERGE SORT",
      "latex": "T(n) = aT\\left(\\frac{n}{b}\\right) + f(n) \\implies T(n) = 2T\\left(\\frac{n}{2}\\right) + cn \\implies n^{\\log_b a} = n^{\\log_2 2} = n^1 \\implies T(n) = \\Theta(n \\log n)",
      "legend": "• Kedalaman rekursi: $\\log_2 n$ level<br>• Biaya penggabungan (merge) per level: $O(n)$ operasi<br>• Total waktu: $(\\text{kedalaman}) \\times (\\text{biaya per level}) = n \\log n$<br>• Sifat stabil (stable sort), namun butuh memori tambahan $O(n)$"
    },
    "options": [
      {
        "key": "A",
        "text": "$O(n \\log_2 n)$ pada semua kasus (best, average, dan worst case), karena pohon rekursi memiliki kedalaman $\\log_2 n$ dan setiap level pohon membutuhkan waktu penggabungan linier $O(n)$."
      },
      {
        "key": "B",
        "text": "$O(n^2)$ pada worst case, karena proses penggabungan membutuhkan perbandingan kuadratik antar elemen sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "$O(n)$ pada best case, karena jika larik sudah terurut algoritma tidak melakukan pemecahan rekursif."
      },
      {
        "key": "D",
        "text": "$O(\\log_2 n)$, karena algoritma berhasil mengabaikan separuh elemen larik pada setiap tahapan partisi."
      },
      {
        "key": "E",
        "text": "$O(2^n)$, karena pohon pemanggilan fungsi rekursif bercabang dua tanpa henti hingga batas memori."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $O(n \\log_2 n)$ pada semua kasus (best, average, dan worst case), karena pohon rekursi memiliki kedalaman $\\log_2 n$ dan setiap level pohon membutuhkan waktu penggabungan linier $O(n)$.. Merge sort memiliki kedalaman rekursi log(n) dan merge linier n pada tiap level, sehingga T(n) = O(n log n) di semua kasus. Pilih: O(n log n) pada semua kasus."
  },
  {
    "id": "inf-lat-m-07",
    "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
    "topic": "Sistem Kriptografi Hibrida pada Protokol HTTPS / TLS",
    "hints": {
      "concept": "Kriptografi asimetris lambat sehingga hanya dipakai saat handshake untuk bertukar Session Key. Enkripsi data massal memakai AES simetris yang cepat.",
      "execution": "Pilih: Komputasi asimetris sangat lambat sehingga hanya digunakan untuk menukar kunci sesi simetris yang cepat."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Protokol keamanan web HTTPS (SSL/TLS) menggunakan pendekatan kriptografi hibrida (hybrid cryptography) yang menggabungkan algoritma kunci asimetris (seperti RSA atau ECC) dan algoritma kunci simetris (seperti AES-256). Alasan mendasar mengapa protokol ini tidak menggunakan kunci asimetris untuk seluruh enkripsi data transfer adalah...",
    "formulaHud": {
      "title": "ALUR KERJA KRIPTOGRAFI HIBRIDA (HYBRID CRYPTOSYSTEM)",
      "latex": "\\begin{aligned} \\text{Fase Handshake (Asimetris):} & \\quad \\text{Klien enkripsi Kunci Sesi (Session Key)} \\xrightarrow{\\text{Public Key Server}} \\text{Server Dekripsi via Private Key} \\\\ \\text{Fase Transfer Data (Simetris):} & \\quad \\text{Klien} \\xleftrightarrow{\\text{AES-GCM (Session Key)}} \\text{Server (Cepat & Ringan Komputasi)} \\end{aligned}",
      "legend": "• Kunci Asimetris (RSA/ECC): Otentikasi identitas server & pertukaran rahasia kunci sesi (key exchange)<br>• Kunci Simetris (AES/ChaCha20): Enkripsi muatan massal data aplikasi berkecepatan tinggi"
    },
    "options": [
      {
        "key": "A",
        "text": "Kunci asimetris memiliki celah keamanan fatal di mana kunci privat dapat ditebak secara langsung dari sertifikat digital sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Komputasi enkripsi dan dekripsi asimetris berbasis operasi matematika bilangan prima besar sangat lambat dan membebani CPU, sehingga kunci asimetris hanya digunakan saat negosiasi jabat tangan awal untuk menukar kunci sesi simetris yang jauh lebih cepat."
      },
      {
        "key": "C",
        "text": "Algoritma simetris tidak mampu mengenkripsi data multimedia berukuran besar seperti video dan berkas gambar."
      },
      {
        "key": "D",
        "text": "Kunci asimetris dilarang oleh badan standardisasi internet dunia karena membutuhkan sambungan kabel tembaga khusus."
      },
      {
        "key": "E",
        "text": "Algoritma simetris tidak memerlukan kunci apapun untuk mengenkripsi maupun mendekripsi pesan rahasia pengguna."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Komputasi enkripsi dan dekripsi asimetris berbasis operasi matematika bilangan prima besar sangat lambat dan membebani CPU, sehingga kunci asimetris hanya digunakan saat negosiasi jabat tangan awal untuk menukar kunci sesi simetris yang jauh lebih cepat.. Kriptografi asimetris lambat sehingga hanya dipakai saat handshake untuk bertukar Session Key. Enkripsi data massal memakai AES simetris yang cepat. Pilih: Komputasi asimetris sangat lambat sehingga hanya digunakan untuk menukar kunci sesi simetris yang cepat."
  },
  {
    "id": "inf-lat-m-08",
    "materi": "SISTEM KOMPUTER",
    "topic": "Penjadwalan Proses CPU: Preemptive vs Non-Preemptive",
    "hints": {
      "concept": "Time quantum terlalu kecil menyebabkan terlalu sering terjadi context switching sehingga waktu CPU habis untuk overhead alih tugas.",
      "execution": "Pilih: Kinerja merosot karena tingginya overhead context switching."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dalam sistem operasi multitasking, algoritma penjadwalan Round-Robin (RR) membagi waktu pemrosesan CPU ke setiap proses menggunakan kuantum waktu (time quantum) yang telah ditentukan secara bergiliran. Jika ukuran kuantum waktu ditetapkan terlalu kecil (misalnya mendekati 0 milidetik), dampak negatif yang akan dialami oleh kinerja sistem adalah...",
    "formulaHud": {
      "title": "PENGARUH QUANTUM TIME PADA PENJADWALAN ROUND ROBIN",
      "latex": "q \\to 0 \\implies \\text{Context Switches} \\to \\infty \\implies \\text{Throughput} \\to 0, \\quad q \\to \\infty \\implies \\text{Round Robin} \\to \\text{FCFS}",
      "legend": "• Context Switch: Menyimpan state (register, PC) proses lama dan memuat state proses baru ke CPU<br>• Jika $q$ terlalu kecil: Overhead switching mendominasi pemakaian CPU<br>• Jika $q$ terlalu besar: Waktu respons interaktif menjadi lambat"
    },
    "options": [
      {
        "key": "A",
        "text": "Terjadi fenomena Starvation di mana proses yang memiliki burst time panjang tidak akan pernah dieksekusi sama sekali ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Algoritma Round-Robin akan otomatis berubah menjadi algoritma First-Come, First-Served (FCFS) konvensional."
      },
      {
        "key": "C",
        "text": "Efisiensi sistem merosot tajam karena waktu prosesor habis terbuang hanya untuk melakukan peralihan konteks (context switching overhead) antar proses daripada menjalankan instruksi program."
      },
      {
        "key": "D",
        "text": "Sistem operasi akan mengalami deadlock permanen karena memori RAM terfragmentasi secara fisik."
      },
      {
        "key": "E",
        "text": "Seluruh proses dalam sistem akan selesai dieksekusi dalam waktu 0 milidetik secara instan."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Efisiensi sistem merosot tajam karena waktu prosesor habis terbuang hanya untuk melakukan peralihan konteks (context switching overhead) antar proses daripada menjalankan instruksi program.. Time quantum terlalu kecil menyebabkan terlalu sering terjadi context switching sehingga waktu CPU habis untuk overhead alih tugas. Pilih: Kinerja merosot karena tingginya overhead context switching."
  },
  {
    "id": "inf-lat-m-09",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Kelemahan Strategi Algoritma Serakah (Greedy Approach)",
    "hints": {
      "concept": "Greedy memilih koin terbesar dulu: 4, lalu sisa 2 (koin 1 dan 1), total 3 koin. Padahal solusi terbaik adalah 3+3 = 2 koin.",
      "execution": "Pilih: Greedy menghasilkan 3 koin (4+1+1), bukan optimal global karena solusi optimal adalah 2 koin (3+3)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Algoritma Serakah (Greedy Algorithm) bekerja dengan prinsip membuat pilihan optimal secara lokal pada setiap langkah dengan harapan mencapai solusi optimal secara global. Diberikan pecahan koin bernilai $\\{1, 3, 4\\}$ dan target kembalian sebesar $6$. Jika algoritma Greedy diterapkan untuk meminimalkan jumlah koin, solusi yang dihasilkan serta kondisi keoptimalannya adalah...",
    "formulaHud": {
      "title": "ANALISIS KEGAGALAN ALGORITMA GREEDY (COIN CHANGE PROBLEM)",
      "latex": "\\begin{aligned} \\text{Target: } 6, \\quad \\text{Koin: } \\{4, 3, 1\\} \\\\ \\text{Solusi Greedy (Ambil Koin Terbesar):} & \\quad 4 \\to \\text{Sisa } 2 \\to 1 \\to \\text{Sisa } 1 \\to 1 \\implies 3 \\text{ Koin } (4+1+1) \\\\ \\text{Solusi Optimal (Dynamic Programming):} & \\quad 3 + 3 = 6 \\implies 2 \\text{ Koin } (3+3) \\end{aligned}",
      "legend": "• Greedy Choice Property tidak selalu menjamin solusi global optimal pada canonical coin systems non-standar<br>• Masalah penukaran koin umum diselesaikan optimal menggunakan Dynamic Programming ($O(n \\times V)$)"
    },
    "options": [
      {
        "key": "A",
        "text": "Greedy menghasilkan 2 koin ($3 + 3$), yang membuktikan bahwa algoritma serakah selalu optimal pada setiap sistem mata uang menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Greedy menghasilkan 6 koin ($1 + 1 + 1 + 1 + 1 + 1$), karena selalu memprioritaskan koin berbobot terkecil."
      },
      {
        "key": "C",
        "text": "Greedy gagal mengeksekusi komputasi dan program mengalami crash karena nilai koin tidak habis dibagi dua."
      },
      {
        "key": "D",
        "text": "Greedy menghasilkan 3 koin ($4 + 1 + 1$), yang BUKAN solusi optimal global karena solusi paling optimal adalah 2 koin ($3 + 3$)."
      },
      {
        "key": "E",
        "text": "Greedy menghasilkan 2 koin ($4 + 2$), dengan otomatis mencetak koin baru bernilai 2 yang tidak ada di daftar."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Greedy menghasilkan 3 koin ($4 + 1 + 1$), yang BUKAN solusi optimal global karena solusi paling optimal adalah 2 koin ($3 + 3$).. Greedy memilih koin terbesar dulu: 4, lalu sisa 2 (koin 1 dan 1), total 3 koin. Padahal solusi terbaik adalah 3+3 = 2 koin. Pilih: Greedy menghasilkan 3 koin (4+1+1), bukan optimal global karena solusi optimal adalah 2 koin (3+3)."
  },
  {
    "id": "inf-lat-m-10",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Penelusuran Algoritma Pemangkatan Cepat (Binary Exponentiation)",
    "hints": {
      "concept": "Hitung urutan nilai n yang dipanggil: 13 (ke-1), 12 (ke-2), 6 (ke-3), 3 (ke-4), 2 (ke-5), 1 (ke-6), 0 (ke-7). Total 7 panggilan.",
      "execution": "Pilih opsi yang sesuai dengan tracing rantai nilai n (7 pemanggilan)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Diberikan algoritma rekursif perhitungan pangkat bilangan bulat berikut:\n```python\ndef power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        half = power(x, n // 2)\n        return half * half\n    else:\n        return x * power(x, n - 1)\n```\nJika fungsi dipanggil dengan argumen `power(3, 13)`, jumlah total pemanggilan fungsi `power` (termasuk pemanggilan awal) yang dieksekusi di dalam memori adalah...",
    "formulaHud": {
      "title": "ALUR TRACING EKSPOKSI CEPAT (BINARY EXPONENTIATION)",
      "latex": "n: 13 \\xrightarrow{\\text{ganjil}} 12 \\xrightarrow{\\text{genap}} 6 \\xrightarrow{\\text{genap}} 3 \\xrightarrow{\\text{ganjil}} 2 \\xrightarrow{\\text{genap}} 1 \\xrightarrow{\\text{ganjil}} 0 \\implies 7 \\text{ transisi} \\implies 8 \\text{ pemanggilan}",
      "legend": "• Panggilan 1: power(3, 13) -> n ganjil -> panggil power(3, 12)<br>• Panggilan 2: power(3, 12) -> n genap -> panggil power(3, 6)<br>• Panggilan 3: power(3, 6) -> n genap -> panggil power(3, 3)<br>• Panggilan 4: power(3, 3) -> n ganjil -> panggil power(3, 2)<br>• Panggilan 5: power(3, 2) -> n genap -> panggil power(3, 1)<br>• Panggilan 6: power(3, 1) -> n ganjil -> panggil power(3, 0)<br>• Panggilan 7: power(3, 0) -> n==0 -> return 1<br>• Total panggilan = 7 pemanggilan rekursif unik"
    },
    "options": [
      {
        "key": "A",
        "text": "14 kali pemanggilan, karena fungsi dipanggil sebanyak $n + 1$ kali secara linier diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "4 kali pemanggilan, karena hanya memperhitungkan kasus cabang genap saja."
      },
      {
        "key": "C",
        "text": "13 kali pemanggilan, sesuai dengan nilai eksponen pangkat yang dimasukkan."
      },
      {
        "key": "D",
        "text": "6 kali pemanggilan, karena pembulatan logaritma basis dua dari angka 13."
      },
      {
        "key": "E",
        "text": "8 kali pemanggilan, dengan rantai parameter $n$: $13 \\to 12 \\to 6 \\to 3 \\to 2 \\to 1 \\to 0$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) 8 kali pemanggilan, dengan rantai parameter $n$: $13 \\to 12 \\to 6 \\to 3 \\to 2 \\to 1 \\to 0$.. Hitung urutan nilai n yang dipanggil: 13 (ke-1), 12 (ke-2), 6 (ke-3), 3 (ke-4), 2 (ke-5), 1 (ke-6), 0 (ke-7). Total 7 panggilan. Pilih opsi yang sesuai dengan tracing rantai nilai n (7 pemanggilan)."
  },
  {
    "id": "inf-lat-m-11",
    "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
    "topic": "Interoperabilitas dan Karakteristik Format Pertukaran Data JSON vs XML",
    "hints": {
      "concept": "JSON lebih ringkas tanpa tag pembuka/penutup ganda, payload lebih kecil, dan native diparsing ke objek pemrograman.",
      "execution": "Pilih: Memiliki struktur teks lebih ringkas, payload lebih kecil, dan langsung diparsing menjadi objek."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dalam pengembangan antarmuka pemrograman aplikasi web modern (RESTful API), format JSON (JavaScript Object Notation) telah menggeser dominasi XML (Extensible Markup Language) sebagai format pertukaran data standar. Keunggulan teknis utama dari JSON adalah...",
    "formulaHud": {
      "title": "KOMPARASI FORMAT PERTUKARAN DATA (DATA INTERCHANGE)",
      "latex": "\\begin{aligned} \\text{JSON:} & \\quad \\{\\text{\"id\": 1, \"nama\": \"Budi\"}\\} \\implies \\text{Ringkas, Cepat di-parse, Ukuran kecil} \\\\ \\text{XML:} & \\quad \\text{<siswa><id>1</id><nama>Budi</nama></siswa>} \\implies \\text{Banyak Tag Berulang (Verbose)} \\end{aligned}",
      "legend": "• JSON Types: String, Number, Object, Array, Boolean, Null<br>• Parsing: JSON.parse() pada browser berjalan native di level C++ engine<br>• Format ideal untuk komunikasi mikroservis dan mobile API"
    },
    "options": [
      {
        "key": "A",
        "text": "Memiliki struktur teks yang jauh lebih ringkas (tanpa tag penutup yang bertele-tele), ukuran payload lebih kecil sehingga menghemat bandwidth, serta secara bawaan dapat diparsing langsung menjadi objek bahasa pemrograman seperti JavaScript dan Python."
      },
      {
        "key": "B",
        "text": "Mendukung validasi skema berbasis DTD dan transformasi XSLT bawaan yang tidak dimiliki oleh format data lainnya sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Wajib dienkripsi menggunakan kunci asimetris sebelum dapat ditransmisikan melalui jaringan internet."
      },
      {
        "key": "D",
        "text": "Menjamin bahwa data tidak dapat diubah oleh siapapun karena berbasis format biner terkompresi permanen."
      },
      {
        "key": "E",
        "text": "Mampu menyimpan data logika program berupa kode mesin yang dapat dieksekusi langsung oleh prosesor klien."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Memiliki struktur teks yang jauh lebih ringkas (tanpa tag penutup yang bertele-tele), ukuran payload lebih kecil sehingga menghemat bandwidth, serta secara bawaan dapat diparsing langsung menjadi objek bahasa pemrograman seperti JavaScript dan Python.. JSON lebih ringkas tanpa tag pembuka/penutup ganda, payload lebih kecil, dan native diparsing ke objek pemrograman. Pilih: Memiliki struktur teks lebih ringkas, payload lebih kecil, dan langsung diparsing menjadi objek."
  },
  {
    "id": "inf-lat-m-12",
    "materi": "ANALISIS DATA",
    "topic": "Normalisasi Basis Data: Eliminasi Ketergantungan Parsial pada 2NF",
    "hints": {
      "concept": "2NF melarang ketergantungan parsial (atribut non-kunci hanya bergantung pada sebagian dari composite primary key).",
      "execution": "Pilih opsi yang menyebutkan Ketergantungan Fungsional Parsial (Partial Dependency) dan pemecahan tabel."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebuah tabel relasional `Nilai_Siswa` memiliki composite primary key `(NISN, Kode_Mapel)` dengan atribut lain: `Nama_Siswa`, `Nama_Mapel`, dan `Nilai_Ujian`. Tabel tersebut belum memenuhi Bentuk Normal Kedua (2NF). Alasan mengapa tabel tersebut melanggar 2NF dan langkah perbaikannya adalah...",
    "formulaHud": {
      "title": "DEFINISI BENTUK NORMAL KEDUA (2ND NORMAL FORM / 2NF)",
      "latex": "R \\in \\text{2NF} \\iff R \\in \\text{1NF} \\quad \\land \\quad \\forall A \\notin \\text{Candidate Keys}: \\ A \\text{ tidak bergantung parsial pada sembarang subset kunci}",
      "legend": "• Partial Dependency: $(\\text{NISN}, \\text{Kode\\_Mapel}) \\to \\text{Nama\\_Siswa}$, padahal $\\text{NISN} \\to \\text{Nama\\_Siswa}$ sudah cukup<br>• Solusi Dekomposisi 2NF: Pisahkan atribut parsial ke tabel master masing-masing"
    },
    "options": [
      {
        "key": "A",
        "text": "Terdapat Ketergantungan Transitif di mana atribut `Nilai_Ujian` menentukan nilai atribut `Nama_Siswa` secara tidak langsung sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Terdapat Ketergantungan Fungsional Parsial (Partial Dependency), di mana atribut non-kunci `Nama_Siswa` hanya bergantung pada `NISN` dan `Nama_Mapel` hanya bergantung pada `Kode_Mapel`; solusinya adalah memecah tabel menjadi tabel `Siswa`, `Mata_Pelajaran`, dan `Nilai`."
      },
      {
        "key": "C",
        "text": "Tabel memiliki atribut yang bernilai jamak (multivalued attributes) sehingga melanggar aturan atomitas data dasar."
      },
      {
        "key": "D",
        "text": "Kunci utama tabel terdiri atas lebih dari satu kolom yang dilarang keras dalam standar arsitektur SQL relasional."
      },
      {
        "key": "E",
        "text": "Tabel tidak memiliki indeks pencarian B-Tree sehingga sistem operasi gagal melakukan pengurutan otomatis."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Terdapat Ketergantungan Fungsional Parsial (Partial Dependency), di mana atribut non-kunci `Nama_Siswa` hanya bergantung pada `NISN` dan `Nama_Mapel` hanya bergantung pada `Kode_Mapel`; solusinya adalah memecah tabel menjadi tabel `Siswa`, `Mata_Pelajaran`, dan `Nilai`.. 2NF melarang ketergantungan parsial (atribut non-kunci hanya bergantung pada sebagian dari composite primary key). Pilih opsi yang menyebutkan Ketergantungan Fungsional Parsial (Partial Dependency) dan pemecahan tabel."
  },
  {
    "id": "inf-lat-m-13",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Hierarki Resolusi Alamat Domain Name System (DNS)",
    "hints": {
      "concept": "Alur hierarki DNS dari kanan ke kiri: Root (.) -> TLD (.id) -> SLD (.go.id) -> Authoritative (kemdikbud.go.id).",
      "execution": "Pilih: Root DNS Server -> TLD Server -> Second-Level Domain Server -> Authoritative DNS Server."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Ketika komputer klien mencari alamat IP dari domain `belajar.kemdikbud.go.id` untuk pertama kalinya (cache DNS kosong), resolver rekursif akan menanyai server-server DNS secara berjenjang. Urutan hierarki server DNS yang dihubungi oleh resolver tersebut secara benar adalah...",
    "formulaHud": {
      "title": "HIERARKI RESOLUSI REKURSIF DNS GLOBAL",
      "latex": "\\text{Klien} \\xrightarrow{\\text{Query}} \\text{Resolver} \\to \\text{Root DNS (\".\")} \\to \\text{TLD DNS (\".id\")} \\to \\text{SLD (\".go.id\")} \\to \\text{Authoritative DNS}",
      "legend": "• Root DNS: Dikelola oleh 13 identitas server logis global (A-M)<br>• TLD DNS: Mengelola domain tingkat atas (.com, .id, .org, .net)<br>• Authoritative DNS: Memegang basis data catatan DNS asli dari pemilik domain"
    },
    "options": [
      {
        "key": "A",
        "text": "Authoritative DNS Server $\\rightarrow$ Root DNS Server $\\rightarrow$ DHCP Server $\\rightarrow$ Web Proxy Gateway ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Internet Service Provider (ISP) Server $\\rightarrow$ Browser Cache $\\rightarrow$ Switch LAN $\\rightarrow$ Client Host."
      },
      {
        "key": "C",
        "text": "Root DNS Server (`.`) $\\rightarrow$ Top-Level Domain (TLD) Server (`.id`) $\\rightarrow$ Second-Level Domain Server (`.go.id`) $\\rightarrow$ Authoritative DNS Server (`kemdikbud.go.id`)."
      },
      {
        "key": "D",
        "text": "Top-Level Domain Server $\\rightarrow$ Authoritative Server $\\rightarrow$ Root Server $\\rightarrow$ Web Application Firewall."
      },
      {
        "key": "E",
        "text": "Web Hosting Server $\\rightarrow$ Local Router $\\rightarrow$ Cloudflare Server $\\rightarrow$ Google Root Server."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Root DNS Server (`.`) $\\rightarrow$ Top-Level Domain (TLD) Server (`.id`) $\\rightarrow$ Second-Level Domain Server (`.go.id`) $\\rightarrow$ Authoritative DNS Server (`kemdikbud.go.id`).. Alur hierarki DNS dari kanan ke kiri: Root (.) -> TLD (.id) -> SLD (.go.id) -> Authoritative (kemdikbud.go.id). Pilih: Root DNS Server -> TLD Server -> Second-Level Domain Server -> Authoritative DNS Server."
  },
  {
    "id": "inf-lat-m-14",
    "materi": "SISTEM KOMPUTER",
    "topic": "Mekanisme Penanganan Interupsi Perangkat Keras (Hardware Interrupt)",
    "hints": {
      "concept": "Saat interupsi: CPU simpan status (PC dan register) ke stack, jalankan fungsi penangan (ISR), lalu pulihkan status dan lanjutkan program.",
      "execution": "Pilih urutan: Selesaikan instruksi aktif -> Simpan status/PC ke Stack -> Jalankan ISR -> Pulihkan status -> Lanjutkan program."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Ketika pengguna menekan tombol pada papan ketik (keyboard), pengontrol perangkat keras mengirimkan sinyal Interrupt Request (IRQ) ke CPU melalui Programmable Interrupt Controller (PIC). Urutan langkah yang diambil oleh CPU untuk menangani peristiwa interupsi tersebut adalah...",
    "formulaHud": {
      "title": "SIKLUS PENANGANAN INTERUPSI (INTERRUPT HANDLING CYCLE)",
      "latex": "\\text{Signal IRQ} \\to \\text{Selesai Siklus Instruksi} \\to \\text{Push Context ke Stack} \\to \\text{Eksekusi ISR} \\to \\text{IRET (Pop Context)} \\to \\text{Resume Program}",
      "legend": "• ISR (Interrupt Service Routine): Handler fungsi di memori kernel OS yang melayani kejadian interupsi spesifik<br>• Context Saving: Menjamin program yang diinterupsi dapat dilanjutkan kembali tanpa kehilangan state data"
    },
    "options": [
      {
        "key": "A",
        "text": "CPU langsung mematikan prosesor $\\rightarrow$ Menghapus seluruh memori RAM $\\rightarrow$ Mengulang kembali proses booting komputer dari BIOS/UEFI menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "CPU mengabaikan sinyal keyboard hingga seluruh program aktif yang ada di sistem operasi selesai dijalankan."
      },
      {
        "key": "C",
        "text": "CPU menyalin seluruh isi hard disk ke memori cache L1 untuk mengantisipasi kerusakan data masukan."
      },
      {
        "key": "D",
        "text": "CPU menyelesaikan instruksi aktif saat ini $\\rightarrow$ Menyimpan status register dan Program Counter (PC) ke Call Stack $\\rightarrow$ Melompat mengeksekusi rutin Interrupt Service Routine (ISR) keyboard $\\rightarrow$ Memulihkan status register dari stack $\\rightarrow$ Melanjutkan instruksi program semula."
      },
      {
        "key": "E",
        "text": "CPU mengubah arsitektur von Neumann menjadi Harvard architecture secara dinamis pada level sirkuit gerbang logika."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) CPU menyelesaikan instruksi aktif saat ini $\\rightarrow$ Menyimpan status register dan Program Counter (PC) ke Call Stack $\\rightarrow$ Melompat mengeksekusi rutin Interrupt Service Routine (ISR) keyboard $\\rightarrow$ Memulihkan status register dari stack $\\rightarrow$ Melanjutkan instruksi program semula.. Saat interupsi: CPU simpan status (PC dan register) ke stack, jalankan fungsi penangan (ISR), lalu pulihkan status dan lanjutkan program. Pilih urutan: Selesaikan instruksi aktif -> Simpan status/PC ke Stack -> Jalankan ISR -> Pulihkan status -> Lanjutkan program."
  },
  {
    "id": "inf-lat-m-15",
    "materi": "STRUKTUR DATA",
    "topic": "Implementasi Antrean Prioritas Menggunakan Binary Heap",
    "hints": {
      "concept": "Tinggi binary heap adalah log(n). Baik penyisipan (bubble-up) maupun ekstraksi akar (bubble-down) membutuhkan waktu O(log n).",
      "execution": "Pilih: O(log n) untuk penyisipan dan O(log n) untuk ekstraksi elemen minimum."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Struktur data Binary Heap sering digunakan untuk mengimplementasikan antrean prioritas (Priority Queue) pada algoritma jalur terpendek Dijkstra. Jika sebuah Min-Heap berisi $n$ elemen data, kompleksitas waktu asimtotik untuk operasi penyisipan elemen baru (`insert/heapify-up`) dan operasi ekstraksi elemen dengan prioritas terkecil (`extract-min/heapify-down`) secara berturut-turut adalah...",
    "formulaHud": {
      "title": "KOMPLEKSITAS OPERASI BINARY HEAP",
      "latex": "\\text{Tinggi Pohon } h = \\lfloor \\log_2 n \\rfloor \\implies \\begin{cases} \\text{Insert (Percolate Up):} & O(\\log n) \\\\ \\text{Extract-Min (Percolate Down):} & O(\\log n) \\\\ \\text{Peek Min (Akar):} & O(1) \\\\ \\text{Build Heap (Floyd's):} & O(n) \\end{cases}",
      "legend": "• Sifat Min-Heap: Nilai simpul induk selalu $\\le$ nilai simpul anak-anaknya<br>• Keunggulan dibanding Array Tak Terurut: Ekstraksi minimum $O(\\log n)$ jauh lebih cepat dibanding $O(n)$"
    },
    "options": [
      {
        "key": "A",
        "text": "$O(1)$ untuk penyisipan dan $O(n)$ untuk ekstraksi elemen minimum diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "$O(n)$ untuk penyisipan dan $O(1)$ untuk ekstraksi elemen minimum."
      },
      {
        "key": "C",
        "text": "$O(n \\log_2 n)$ untuk penyisipan dan $O(n^2)$ untuk ekstraksi elemen minimum."
      },
      {
        "key": "D",
        "text": "$O(1)$ untuk penyisipan dan $O(1)$ untuk ekstraksi elemen minimum konstan."
      },
      {
        "key": "E",
        "text": "$O(\\log_2 n)$ untuk penyisipan dan $O(\\log_2 n)$ untuk ekstraksi elemen minimum."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $O(\\log_2 n)$ untuk penyisipan dan $O(\\log_2 n)$ untuk ekstraksi elemen minimum.. Tinggi binary heap adalah log(n). Baik penyisipan (bubble-up) maupun ekstraksi akar (bubble-down) membutuhkan waktu O(log n). Pilih: O(log n) untuk penyisipan dan O(log n) untuk ekstraksi elemen minimum."
  },
  {
    "id": "inf-lat-m-16",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Prinsip Perlindungan Data Pribadi (UU PDP No. 27 Tahun 2022)",
    "hints": {
      "concept": "Meminta penghapusan rekam jejak pribadi setelah mencabut consent adalah pelaksanaan hak pemusnahan data (right to erasure/forgotten).",
      "execution": "Pilih: Hak untuk Menghapus dan Memusnahkan Data Pribadi (Right to Erasure)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Undang-Undang Perlindungan Data Pribadi (UU PDP No. 27/2022) di Indonesia mengatur hak-hak subjek data pribadi dan kewajiban pengendali data. Jika seorang pengguna aplikasi pinjaman daring menarik kembali persetujuan pemrosesan datanya dan meminta pengelola aplikasi untuk menghapus seluruh data rekam jejak finansialnya, hak yang sedang digunakan oleh subjek data tersebut adalah...",
    "formulaHud": {
      "title": "HAK-HAK SUBJEK DATA PRIBADI (PASAL 5 - 13 UU PDP NO. 27/2022)",
      "latex": "\\text{Hak Subjek Data} \\supset \\{\\text{Akses Data}, \\text{Koreksi Kesalahan}, \\text{Penarikan Consent}, \\text{Penghapusan/Pemusnahan Data}, \\text{Portabilitas}\\}",
      "legend": "• Pengendali Data Pribadi: Pihak yang menentukan tujuan dan kendali pemrosesan data<br>• Kewajiban Pengendali Data: Melindungi data dengan enkripsi, memberitahukan insiden kebocoran maksimal 3x24 jam"
    },
    "options": [
      {
        "key": "A",
        "text": "Hak untuk Menghapus dan Memusnahkan Data Pribadi (Right to Erasure / Right to be Forgotten), di mana pengendali data wajib menghentikan pemrosesan dan memusnahkan data pribadi pemohon sesuai regulasi hukum."
      },
      {
        "key": "B",
        "text": "Hak Portabilitas Data, yaitu hak untuk meminta ganti rugi uang tunai atas kegagalan sistem keamanan aplikasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Hak Monopoli Komersial, yaitu hak subjek data untuk menjual kembali basis data perusahaan kepada pihak ketiga."
      },
      {
        "key": "D",
        "text": "Hak Anonimitas Mutlak, yaitu jaminan bahwa pengguna bebas melakukan transaksi tanpa identitas yang sah secara perbankan."
      },
      {
        "key": "E",
        "text": "Hak Imunitas Siber, yaitu pembebasan subjek data dari kewajiban membayar utang pokok pinjaman yang telah disepakati."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Hak untuk Menghapus dan Memusnahkan Data Pribadi (Right to Erasure / Right to be Forgotten), di mana pengendali data wajib menghentikan pemrosesan dan memusnahkan data pribadi pemohon sesuai regulasi hukum.. Meminta penghapusan rekam jejak pribadi setelah mencabut consent adalah pelaksanaan hak pemusnahan data (right to erasure/forgotten). Pilih: Hak untuk Menghapus dan Memusnahkan Data Pribadi (Right to Erasure)."
  },
  {
    "id": "inf-lat-m-17",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Penelusuran Graf: Karakteristik Algoritma BFS vs DFS",
    "hints": {
      "concept": "BFS menelusuri lapis demi lapis dengan Queue, menjamin jalur pertama yang sampai adalah yang terpendek pada graf berbobot seragam.",
      "execution": "Pilih: BFS menelusuri simpul tingkat demi tingkat menggunakan Queue sehingga jalur pertama kali mencapai tujuan adalah yang terpendek."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dalam mencari rute jalan keluar terpendek pada sebuah labirin (maze) tanpa bobot, seorang pemrogram dapat menggunakan algoritma penelusuran Breadth-First Search (BFS) atau Depth-First Search (DFS). Alasan mengapa BFS dijamin selalu menemukan solusi jalur dengan jumlah langkah paling sedikit dibandingkan DFS adalah...",
    "formulaHud": {
      "title": "KOMPARASI PENELUSURAN GRAF (GRAPH TRAVERSAL)",
      "latex": "\\begin{aligned} \\text{BFS (Breadth-First):} & \\quad \\text{Struktur: Queue (FIFO)} \\implies \\text{Jalur Terpendek pada Graf Tanpa Bobot} \\\\ \\text{DFS (Depth-First):} & \\quad \\text{Struktur: Stack (LIFO) / Rekursif} \\implies \\text{Deteksi Siklus, Topological Sort} \\end{aligned}",
      "legend": "• Kompleksitas Waktu BFS & DFS: $O(V + E)$ dengan adjacency list<br>• Kelemahan DFS untuk rute terpendek: Dapat terjebak di cabang dalam yang bukan merupakan solusi minimum"
    },
    "options": [
      {
        "key": "A",
        "text": "BFS mengeksplorasi satu cabang jalan sedalam mungkin hingga menemui jalan buntu menggunakan tumpukan (Stack) sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "BFS menelusuri simpul secara melebar tingkat demi tingkat (level by level) menggunakan struktur data antrean (Queue), sehingga jalur yang pertama kali mencapai simpul tujuan pasti merupakan jalur terpendek."
      },
      {
        "key": "C",
        "text": "BFS menghitung bobot nilai heuristik prediksi arah mata angin menggunakan formula trigonometri Euclidean."
      },
      {
        "key": "D",
        "text": "BFS mengurutkan seluruh simpul labirin menggunakan algoritma Quicksort sebelum langkah penelusuran dimulai."
      },
      {
        "key": "E",
        "text": "DFS selalu membutuhkan waktu komputasi yang tak terhingga karena tidak dapat menandai simpul yang telah dikunjungi."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) BFS menelusuri simpul secara melebar tingkat demi tingkat (level by level) menggunakan struktur data antrean (Queue), sehingga jalur yang pertama kali mencapai simpul tujuan pasti merupakan jalur terpendek.. BFS menelusuri lapis demi lapis dengan Queue, menjamin jalur pertama yang sampai adalah yang terpendek pada graf berbobot seragam. Pilih: BFS menelusuri simpul tingkat demi tingkat menggunakan Queue sehingga jalur pertama kali mencapai tujuan adalah yang terpendek."
  },
  {
    "id": "inf-lat-m-18",
    "materi": "ANALISIS DATA",
    "topic": "Filter Agregat SQL: Perbedaan Klausa WHERE vs HAVING",
    "hints": {
      "concept": "Filter pada fungsi agregat (AVG(gaji) > 10000000) wajib menggunakan klausa HAVING setelah GROUP BY, bukan WHERE.",
      "execution": "Pilih kueri yang menggunakan GROUP BY departemen HAVING AVG(gaji) > 10000000."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Diberikan tabel `Karyawan` dengan kolom `departemen` dan `gaji`. Manajemen perusahaan ingin mengetahui departemen mana saja yang memiliki rata-rata gaji karyawan di atas Rp 10.000.000,-. Kueri SQL yang benar untuk memenuhi kebutuhan laporan tersebut adalah...",
    "formulaHud": {
      "title": "URUTAN EKSEKUSI LOGIKA PERINTAH SQL",
      "latex": "\\text{FROM} \\to \\text{WHERE (Filter Baris Individu)} \\to \\text{GROUP BY} \\to \\text{HAVING (Filter Kelompok Agregat)} \\to \\text{SELECT} \\to \\text{ORDER BY}",
      "legend": "• WHERE tidak dapat digunakan bersama fungsi agregasi (AVG, SUM, COUNT)<br>• HAVING secara spesifik diciptakan untuk memfilter hasil setelah fungsi agregasi dikelompokkan oleh GROUP BY"
    },
    "options": [
      {
        "key": "A",
        "text": "`SELECT departemen, AVG(gaji) FROM Karyawan WHERE AVG(gaji) > 10000000 GROUP BY departemen;`"
      },
      {
        "key": "B",
        "text": "`SELECT departemen, SUM(gaji) FROM Karyawan WHERE departemen IS NOT NULL ORDER BY AVG(gaji) > 10000000;`"
      },
      {
        "key": "C",
        "text": "`SELECT departemen, AVG(gaji) FROM Karyawan GROUP BY departemen HAVING AVG(gaji) > 10000000;`"
      },
      {
        "key": "D",
        "text": "`SELECT departemen FROM Karyawan HAVING gaji > 10000000 GROUP BY departemen;`"
      },
      {
        "key": "E",
        "text": "`SELECT departemen, AVG(gaji) IN Karyawan FILTER BY AVG(gaji) > 10000000;`"
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) `SELECT departemen, AVG(gaji) FROM Karyawan GROUP BY departemen HAVING AVG(gaji) > 10000000;`. Filter pada fungsi agregat (AVG(gaji) > 10000000) wajib menggunakan klausa HAVING setelah GROUP BY, bukan WHERE. Pilih kueri yang menggunakan GROUP BY departemen HAVING AVG(gaji) > 10000000."
  },
  {
    "id": "inf-lat-m-19",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Mekanisme Jabat Tangan Tiga Langkah (TCP Three-Way Handshake)",
    "hints": {
      "concept": "Tiga langkah koneksi TCP: Klien kirim SYN -> Server balas SYN-ACK -> Klien konfirmasi dengan ACK.",
      "execution": "Pilih: SYN -> SYN-ACK -> ACK."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Sebelum protokol TCP mentransmisikan data aplikasi, koneksi logis yang andal (reliable) harus dibangun antara klien dan server melalui mekanisme TCP 3-Way Handshake. Urutan pertukaran segmen kendali TCP yang tepat pada tahapan tersebut adalah...",
    "formulaHud": {
      "title": "DIAGRAM ALIR TCP THREE-WAY HANDSHAKE",
      "latex": "\\begin{aligned} \\text{Klien} & \\xrightarrow{\\text{SYN (Seq = } x\\text{)}} \\text{Server} \\\\ \\text{Klien} & \\xleftarrow{\\text{SYN-ACK (Seq = } y, \\text{ Ack = } x + 1\\text{)}} \\text{Server} \\\\ \\text{Klien} & \\xrightarrow{\\text{ACK (Seq = } x + 1, \\text{ Ack = } y + 1\\text{)}} \\text{Server} \\implies \\text{ESTABLISHED} \\end{aligned}",
      "legend": "• Sequence Number: Mengurutkan segmen dan mendeteksi paket hilang<br>• Acknowledgment Number: Mengonfirmasi penerimaan paket berikutnya yang diharapkan<br>• Pelepasan Koneksi (Teardown): Menggunakan 4-Way Handshake (FIN -> ACK -> FIN -> ACK)"
    },
    "options": [
      {
        "key": "A",
        "text": "Klien mengirimkan segmen `ACK` $\\rightarrow$ Server membalas `FIN` $\\rightarrow$ Klien mengirimkan segmen data payload menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Klien mengirimkan `RST` $\\rightarrow$ Server membalas `SYN` $\\rightarrow$ Klien merespons dengan `FIN-ACK`."
      },
      {
        "key": "C",
        "text": "Server menyiarkan paket `PING` $\\rightarrow$ Klien merespons `PONG` $\\rightarrow$ Gateway memverifikasi sertifikat digital."
      },
      {
        "key": "D",
        "text": "Klien mengirimkan segmen `SYN` (Synchronize) $\\rightarrow$ Server merespons dengan segmen `SYN-ACK` (Synchronize-Acknowledgment) $\\rightarrow$ Klien membalas dengan segmen `ACK` (Acknowledgment)."
      },
      {
        "key": "E",
        "text": "Klien mengirimkan `HELLO` $\\rightarrow$ Server merespons `READY` $\\rightarrow$ Klien mengirimkan `START`."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Klien mengirimkan segmen `SYN` (Synchronize) $\\rightarrow$ Server merespons dengan segmen `SYN-ACK` (Synchronize-Acknowledgment) $\\rightarrow$ Klien membalas dengan segmen `ACK` (Acknowledgment).. Tiga langkah koneksi TCP: Klien kirim SYN -> Server balas SYN-ACK -> Klien konfirmasi dengan ACK. Pilih: SYN -> SYN-ACK -> ACK."
  },
  {
    "id": "inf-lat-m-20",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Penurunan Kinerja Algoritma Quicksort Menjadi Kasus Terburuk",
    "hints": {
      "concept": "Pada data terurut dengan pivot di ujung, partisi menjadi 0 dan n-1. Kedalaman pohon menjadi n, kompleksitas memburuk jadi O(n^2).",
      "execution": "Pilih: O(n^2) kuadratik karena partisi sangat timpang (0 dan n-1) dengan kedalaman pohon n."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Algoritma pengurutan Quicksort rata-rata memiliki kinerja sangat cepat dengan kompleksitas $O(n \\log_2 n)$. Namun, jika implementasi partisi naif selalu memilih elemen pertama atau elemen terakhir sebagai pivot dan larik masukan yang diberikan sudah dalam kondisi terurut sempurna (sorted), kompleksitas waktu Quicksort akan merosot menjadi...",
    "formulaHud": {
      "title": "KASUS TERBURUK ALGORITMA QUICKSORT",
      "latex": "T(n) = T(n - 1) + O(n) = \\sum_{i=1}^n i = \\frac{n(n + 1)}{2} \\implies O(n^2)",
      "legend": "• Kasus Terbaik / Rata-rata ($O(n \\log n)$): Pivot selalu membagi larik menjadi dua bagian seimbang ($n/2$ dan $n/2$)<br>• Mitigasi Kasus Terburuk: Menggunakan teknik Median-of-Three atau Randomized Pivot Selection"
    },
    "options": [
      {
        "key": "A",
        "text": "$O(1)$ konstan, karena algoritma mendeteksi bahwa larik sudah terurut sehingga langsung menghentikan program diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "$O(n)$ linier, karena algoritma hanya melakukan satu kali pengecekan partisi dari depan ke belakang."
      },
      {
        "key": "C",
        "text": "$O(n^3)$ kubik, karena perbandingan elemen dilakukan tiga dimensi di dalam ruang memori tumpukan."
      },
      {
        "key": "D",
        "text": "$O(\\log_2 n)$, karena partisi yang timpang justru mempercepat penggabungan elemen pivot."
      },
      {
        "key": "E",
        "text": "$O(n^2)$ kuadratik, karena pada setiap tahapan partisi dihasilkan pembagian sub-larik yang sangat timpang tidak seimbang (berukuran $0$ dan $n-1$), sehingga pohon rekursi memiliki kedalaman $n$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $O(n^2)$ kuadratik, karena pada setiap tahapan partisi dihasilkan pembagian sub-larik yang sangat timpang tidak seimbang (berukuran $0$ dan $n-1$), sehingga pohon rekursi memiliki kedalaman $n$.. Pada data terurut dengan pivot di ujung, partisi menjadi 0 dan n-1. Kedalaman pohon menjadi n, kompleksitas memburuk jadi O(n^2). Pilih: O(n^2) kuadratik karena partisi sangat timpang (0 dan n-1) dengan kedalaman pohon n."
  },
  {
    "id": "inf-lat-m-21",
    "materi": "SISTEM KOMPUTER",
    "topic": "Arsitektur Kumpulan Instruksi: RISC vs CISC",
    "hints": {
      "concept": "Ciri khas RISC: instruksi sederhana berukuran tetap, eksekusi satu siklus, operasi data hanya di register (Load/Store).",
      "execution": "Pilih opsi: Instruksi sederhana berukuran seragam, eksekusi satu siklus clock, dan arsitektur Load/Store."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dalam desain prosesor komputer, arsitektur Reduced Instruction Set Computer (RISC) seperti ARM berbeda secara fundamental dengan Complex Instruction Set Computer (CISC) seperti Intel x86. Karakteristik utama dari filosofi arsitektur RISC adalah...",
    "formulaHud": {
      "title": "KOMPARASI ARSITEKTUR SET INSTRUKSI CPU",
      "latex": "\\begin{aligned} \\text{RISC (ARM, RISC-V):} & \\quad \\text{Instruksi Fixed, Eksekusi 1 Siklus, Load/Store Murni, Pipelining Efisien} \\\\ \\text{CISC (x86-64):} & \\quad \\text{Instruksi Variabel, Multi-Siklus, Memanipulasi Memori Langsung, Kaya Fitur} \\end{aligned}",
      "legend": "• Waktu Eksekusi Program: $\\text{Waktu} = (\\text{Jumlah Instruksi}) \\times (\\text{CPI}) \\times (\\text{Waktu Siklus Clock})$<br>• RISC mengoptimalkan CPI $\\approx 1$, sedangkan CISC meminimalkan jumlah instruksi per program"
    },
    "options": [
      {
        "key": "A",
        "text": "Memiliki set instruksi sederhana berukuran seragam (fixed-length), sebagian besar instruksi dieksekusi dalam satu siklus clock, serta menerapkan arsitektur Load/Store di mana operasi manipulasi data hanya dapat dilakukan di dalam register CPU."
      },
      {
        "key": "B",
        "text": "Memiliki instruksi tingkat tinggi berukuran bervariasi yang mampu memanipulasi operan langsung di dalam memori RAM utama sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Tidak memiliki register internal sehingga seluruh perhitungan dilakukan langsung pada sirkuit bus sistem."
      },
      {
        "key": "D",
        "text": "Hanya mampu mengeksekusi instruksi program secara sekuensial tanpa mendukung teknik pipelining prosesor."
      },
      {
        "key": "E",
        "text": "Membutuhkan perangkat keras mikro-kode (microcode engine) yang rumit untuk memecah instruksi sebelum dieksekusi ALU."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Memiliki set instruksi sederhana berukuran seragam (fixed-length), sebagian besar instruksi dieksekusi dalam satu siklus clock, serta menerapkan arsitektur Load/Store di mana operasi manipulasi data hanya dapat dilakukan di dalam register CPU.. Ciri khas RISC: instruksi sederhana berukuran tetap, eksekusi satu siklus, operasi data hanya di register (Load/Store). Pilih opsi: Instruksi sederhana berukuran seragam, eksekusi satu siklus clock, dan arsitektur Load/Store."
  },
  {
    "id": "inf-lat-m-22",
    "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
    "topic": "Karakteristik Fungsi Hash Kriptografis dan Efek Avalanche",
    "hints": {
      "concept": "Perubahan 1 bit input menyebabkan perubahan drastis pada nilai hash output disebut Avalanche Effect (Efek Longsoran).",
      "execution": "Pilih: Efek Longsoran (Avalanche Effect)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Fungsi hash kriptografis seperti SHA-256 digunakan secara luas untuk verifikasi integritas data dan penyimpanan kata sandi. Karakteristik penting di mana perubahan sekecil satu bit saja pada data masukan (input) akan menghasilkan nilai digest hash keluaran yang berubah secara drastis dan acak total disebut...",
    "formulaHud": {
      "title": "PROPERTI MATEMATIS FUNGSI HASH KRIPTOGRAFIS",
      "latex": "x \\xrightarrow{\\text{Flip 1 Bit}} x' \\implies \\text{HammingDistance}(\\text{Hash}(x), \\text{Hash}(x')) \\approx 50\\% \\text{ Total Bits}",
      "legend": "• Avalanche Effect: Mengubah 'cat' menjadi 'bat' mengubah total seluruh 256-bit digest keluaran<br>• Pre-image Resistance: $h = H(m) \\implies$ Sulit mencari $m$ jika hanya diketahui $h$<br>• Collision Resistance: Sulit menemukan $m_1 \\ne m_2$ sedemikian rupa sehingga $H(m_1) = H(m_2)$"
    },
    "options": [
      {
        "key": "A",
        "text": "Collision Resistance, yaitu sifat kemustahilan matematis menemukan dua masukan berbeda yang menghasilkan hash identik sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Efek Longsoran (Avalanche Effect), yang menjamin bahwa keluaran hash tidak dapat diprediksi hubungannya dengan masukan awal."
      },
      {
        "key": "C",
        "text": "Pre-image Resistance, yaitu sifat satu arah di mana nilai masukan asli mustahil dihitung balik dari nilai hash."
      },
      {
        "key": "D",
        "text": "Zero-Knowledge Proof, yaitu pembuktian kebenaran suatu pernyataan rahasia tanpa mengungkapkan isi rahasia itu sendiri."
      },
      {
        "key": "E",
        "text": "Homomorphic Encryption, yaitu kemampuan melakukan operasi komputasi matematika pada teks tersandi tanpa didekripsi."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Efek Longsoran (Avalanche Effect), yang menjamin bahwa keluaran hash tidak dapat diprediksi hubungannya dengan masukan awal.. Perubahan 1 bit input menyebabkan perubahan drastis pada nilai hash output disebut Avalanche Effect (Efek Longsoran). Pilih: Efek Longsoran (Avalanche Effect)."
  },
  {
    "id": "inf-lat-m-23",
    "materi": "PRAKTIK LINTAS BIDANG",
    "topic": "Penyelesaian Konflik Penggabungan Cabang (Git Merge Conflict)",
    "hints": {
      "concept": "Menyelesaikan git merge conflict: buka file, edit kode di antara marker conflict, hapus marker, lakukan git add dan git commit.",
      "execution": "Pilih opsi: Buka file, selesaikan penanda konflik secara manual, hapus penanda, lalu git add dan git commit."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dua pemrogram bekerja pada repositori Git yang sama dan mengedit baris kode yang sama pada berkas `app.py` di cabang fiturnya masing-masing. Ketika pemrogram kedua mencoba menggabungkan cabangnya menggunakan `git merge feature-b`, terminal menampilkan pesan peringatan `CONFLICT (content): Merge conflict in app.py`. Tindakan teknis yang benar untuk menyelesaikan konflik tersebut adalah...",
    "formulaHud": {
      "title": "STRUKTUR PENANDA MERGE CONFLICT PADA GIT",
      "latex": "\\begin{aligned} & \\text{<<<<<<< HEAD (Cabang Saat Ini)} \\\\ & \\text{Kode cabang aktif} \\\\ & \\text{======= (Pemisah)} \\\\ & \\text{Kode cabang yang digabungkan} \\\\ & \\text{>>>>>>> feature-b (Cabang Masuk)} \\end{aligned}",
      "legend": "• Tahap resolusi: Review manual -> Putuskan logika kode -> Hapus marker -> Staging (git add) -> Selesaikan commit (git commit)"
    },
    "options": [
      {
        "key": "A",
        "text": "Menghapus folder tersembunyi `.git` secara permanen agar riwayat konflik langsung hilang dari komputer ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Menjalankan perintah `git push --force origin main` untuk menimpa seluruh kode di repositori server secara paksa."
      },
      {
        "key": "C",
        "text": "Membuka berkas `app.py`, meninjau penanda konflik (`<<<<<<<`, `=======`, `>>>>>>>`), menyunting baris kode untuk memilih atau menggabungkan perubahan yang benar, menghapus penanda konflik, lalu menjalankan `git add app.py` dan `git commit`."
      },
      {
        "key": "D",
        "text": "Mengganti nama berkas `app.py` menjadi `app_backup.py` lalu membiarkan sistem Git menyelesaikan sendiri secara otomatis."
      },
      {
        "key": "E",
        "text": "Mematikan sambungan internet komputer dan menginstal ulang sistem operasi untuk memulihkan kode sumber."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Membuka berkas `app.py`, meninjau penanda konflik (`<<<<<<<`, `=======`, `>>>>>>>`), menyunting baris kode untuk memilih atau menggabungkan perubahan yang benar, menghapus penanda konflik, lalu menjalankan `git add app.py` dan `git commit`.. Menyelesaikan git merge conflict: buka file, edit kode di antara marker conflict, hapus marker, lakukan git add dan git commit. Pilih opsi: Buka file, selesaikan penanda konflik secara manual, hapus penanda, lalu git add dan git commit."
  },
  {
    "id": "inf-lat-m-24",
    "materi": "ANALISIS DATA",
    "topic": "Deteksi Pencilan Data (Outlier) Berbasis Interquartile Range (IQR)",
    "hints": {
      "concept": "IQR = Q3 - Q1 = 14 - 6 = 8. Batas atas = Q3 + 1.5 * IQR = 14 + 1.5 * 8 = 14 + 12 = 26 juta.",
      "execution": "Pilih: Rp 26.000.000,-."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Dalam tahap pembersihan data (data cleaning), seorang analis data memeriksa distribusi gaji karyawan. Dari hasil perhitungan statistik deskriptif diperoleh nilai Kuartil Bawah ($Q_1$) sebesar Rp 6.000.000,- dan Kuartil Atas ($Q_3$) sebesar Rp 14.000.000,-. Menggunakan aturan Tukey berbasis Interquartile Range (IQR), ambang batas atas (upper bound) untuk mengidentifikasi nilai pencilan (outlier) adalah...",
    "formulaHud": {
      "title": "DETEKSI PENCILAN DATA METODE TUKEY IQR",
      "latex": "\\begin{aligned} \\text{IQR} & = Q_3 - Q_1 = 14 - 6 = 8 \\text{ Juta} \\\\ \\text{Batas Bawah (Lower Fence)} & = Q_1 - 1,5 \\times \\text{IQR} = 6 - 1,5(8) = -6 \\text{ Juta (0)} \\\\ \\text{Batas Atas (Upper Fence)} & = Q_3 + 1,5 \\times \\text{IQR} = 14 + 1,5(8) = 26 \\text{ Juta} \\end{aligned}",
      "legend": "• Outlier: Setiap titik data $x > \\text{Upper Fence}$ atau $x < \\text{Lower Fence}$<br>• Visualisasi: Ditampilkan sebagai titik-titik di luar kumis (whiskers) pada diagram Box Plot"
    },
    "options": [
      {
        "key": "A",
        "text": "Rp 22.000.000,-, hasil penjumlahan kuartil atas dengan satu kali nilai rentang interkuartil dasar menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Rp 20.000.000,-, nilai tengah dari batas maksimum data gaji normal di perusahaan."
      },
      {
        "key": "C",
        "text": "Rp 32.000.000,-, hasil perkalian kuartil atas dengan koefisien variansi populasi dua."
      },
      {
        "key": "D",
        "text": "Rp 26.000.000,-, dihitung dari formula $Q_3 + 1,5 \\times \\text{IQR}$, di mana $\\text{IQR} = Q_3 - Q_1 = 14 - 6 = 8$ juta, sehingga $14 + 1,5(8) = 26$ juta."
      },
      {
        "key": "E",
        "text": "Rp 18.000.000,-, hasil penambahan standar deviasi pada kuartil ketiga statistik sampel."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Rp 26.000.000,-, dihitung dari formula $Q_3 + 1,5 \\times \\text{IQR}$, di mana $\\text{IQR} = Q_3 - Q_1 = 14 - 6 = 8$ juta, sehingga $14 + 1,5(8) = 26$ juta.. IQR = Q3 - Q1 = 14 - 6 = 8. Batas atas = Q3 + 1.5 * IQR = 14 + 1.5 * 8 = 14 + 12 = 26 juta. Pilih: Rp 26.000.000,-."
  },
  {
    "id": "inf-lat-m-25",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Strategi Pencadangan Data 3-2-1 untuk Mitigasi Serangan Siber",
    "hints": {
      "concept": "Aturan 3-2-1: 3 salinan data, 2 jenis media berbeda, 1 salinan disimpan off-site / cloud di lokasi terpisah.",
      "execution": "Pilih opsi: 3 salinan data, 2 media penyimpanan berbeda, dan 1 salinan di lokasi terpisah (off-site/cloud)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "questionHtml": "Untuk melindungi data penting sekolah dari ancaman enkripsi malware ransomware dan kerusakan bencana fisik, administrator jaringan menerapkan strategi pencadangan standar industri \"Aturan Cadangan 3-2-1\". Implementasi yang benar dari aturan 3-2-1 tersebut adalah...",
    "formulaHud": {
      "title": "ATURAN CADANGAN DATA STRATEGIS 3-2-1",
      "latex": "\\text{Ketahanan Data} \\equiv \\text{3 Salinan Data} + \\text{2 Media Penyimpanan Berbeda} + \\text{1 Salinan di Lokasi Eksternal (Off-site/Cloud)}",
      "legend": "• 3 Copies: Data primer + 2 backup mandiri<br>• 2 Media Types: Mencegah kegagalan bersamaan dari teknologi media yang sama (misal Disk + Cloud/Tape)<br>• 1 Off-site: Melindungi dari kebakaran, banjir, pencurian fisik, dan infeksi ransomware lateral"
    },
    "options": [
      {
        "key": "A",
        "text": "Membuat cadangan data setiap 3 jam sekali, ditinjau oleh 2 teknisi berbeda, dan disimpan selama 1 tahun penuh diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Menyimpan data pada 3 komputer dalam 1 ruangan laboratorium yang sama menggunakan 2 kabel LAN dan 1 sakelar."
      },
      {
        "key": "C",
        "text": "Membagi berkas data menjadi 3 pecahan arsip ZIP dengan 2 kata sandi dan 1 kunci pemulihan perangkat keras."
      },
      {
        "key": "D",
        "text": "Menyimpan data di 3 flashdisk yang dicolokkan secara terus-menerus pada 2 port USB di 1 komputer server utama."
      },
      {
        "key": "E",
        "text": "Menyimpan minimal 3 salinan data (1 data produksi asli dan 2 data cadangan), menggunakan 2 jenis media penyimpanan fisik yang berbeda (misalnya SSD server lokal dan Network Attached Storage / pita magnetik), serta menempatkan 1 salinan di lokasi eksternal terpisah (off-site atau cloud terenkripsi)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Menyimpan minimal 3 salinan data (1 data produksi asli dan 2 data cadangan), menggunakan 2 jenis media penyimpanan fisik yang berbeda (misalnya SSD server lokal dan Network Attached Storage / pita magnetik), serta menempatkan 1 salinan di lokasi eksternal terpisah (off-site atau cloud terenkripsi).. Aturan 3-2-1: 3 salinan data, 2 jenis media berbeda, 1 salinan disimpan off-site / cloud di lokasi terpisah. Pilih opsi: 3 salinan data, 2 media penyimpanan berbeda, dan 1 salinan di lokasi terpisah (off-site/cloud)."
  },
  {
    "id": "inf-lat-h-01",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Formulasi Rekurensi 0/1 Knapsack Problem Berbasis Dynamic Programming",
    "hints": {
      "concept": "Pada 0/1 Knapsack, keputusan biner: ambil barang ke-i (jika kapasitas muat) atau lewatkan. Nilai adalah maksimum dari kedua pilihan tersebut.",
      "execution": "Pilih formula DP: DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Diberikan $n$ buah barang, di mana barang ke-$i$ memiliki bobot $w_i$ dan nilai keuntungan $v_i$. Sebuah ransel memiliki batas kapasitas tampung maksimum $W$. Setiap barang hanya dapat diambil satu kali atau ditinggalkan sama sekali (0/1 Knapsack). Relasi rekurensi matriks pemrograman dinamis $DP[i][w]$ yang menyatakan nilai keuntungan maksimum yang dapat diperoleh dari subset barang $1$ sampai $i$ dengan kapasitas ransel tersisa $w$ adalah...",
    "formulaHud": {
      "title": "FORMULASI PEMROGRAMAN DINAMIS 0/1 KNAPSACK",
      "latex": "DP[i][w] = \\begin{cases} DP[i-1][w] & \\text{jika } w < w_i \\\\ \\max\\Big(DP[i-1][w], \\ DP[i-1][w - w_i] + v_i\\Big) & \\text{jika } w \\ge w_i \\end{cases}",
      "legend": "• Kasus 1 (Tidak Ambil Barang i): Nilai optimal sama dengan baris sebelumnya pada kapasitas $w$<br>• Kasus 2 (Ambil Barang i): Nilai barang $v_i$ ditambah keuntungan optimal kapasitas sisa $(w - w_i)$<br>• Kompleksitas Waktu: $O(n \\cdot W)$ (Pseudo-polynomial time)<br>• Ruang Memori: Dapat dioptimasi menjadi array 1 dimensi $O(W)$ dengan iterasi mundur"
    },
    "options": [
      {
        "key": "A",
        "text": "$DP[i][w] = \\max(DP[i-1][w], \\ DP[i-1][w - w_i] + v_i)$ untuk kondisi $w \\ge w_i$, dan $DP[i][w] = DP[i-1][w]$ jika $w < w_i$, dengan kompleksitas waktu pseudo-polinomial $O(n \\cdot W)$."
      },
      {
        "key": "B",
        "text": "$DP[i][w] = DP[i-1][w] + \\min(DP[i][w - w_i], v_i)$, dengan kompleksitas waktu eksponensial $O(2^{n+W})$ sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "$DP[i][w] = \\frac{v_i}{w_i} \\times DP[i-1][w]$, dengan kompleksitas waktu polinomial murni $O(n \\log n)$."
      },
      {
        "key": "D",
        "text": "$DP[i][w] = DP[i-1][w - 1] + DP[i - 1][w + 1] - v_i$, dengan kompleksitas waktu konstan $O(1)$."
      },
      {
        "key": "E",
        "text": "$DP[i][w] = \\sum_{k=1}^i \\left( \\frac{w}{w_k} \\cdot v_k \\right)$, yang mengasumsikan barang dapat dipotong menjadi pecahan desimal tak hingga."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $DP[i][w] = \\max(DP[i-1][w], \\ DP[i-1][w - w_i] + v_i)$ untuk kondisi $w \\ge w_i$, dan $DP[i][w] = DP[i-1][w]$ jika $w < w_i$, dengan kompleksitas waktu pseudo-polinomial $O(n \\cdot W)$.. Pada 0/1 Knapsack, keputusan biner: ambil barang ke-i (jika kapasitas muat) atau lewatkan. Nilai adalah maksimum dari kedua pilihan tersebut. Pilih formula DP: DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i)."
  },
  {
    "id": "inf-lat-h-02",
    "materi": "SISTEM KOMPUTER",
    "topic": "Penanganan Bahaya Data (Data Hazard RAW) pada Pipelining CPU",
    "hints": {
      "concept": "Teknik meneruskan hasil kalkulasi ALU langsung dari output pipeline EX ke input ALU instruksi berikutnya disebut Data Forwarding (Bypassing).",
      "execution": "Pilih: Data Forwarding / Bypassing."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam prosesor berpita pipa (pipelined CPU) 5 tahap (IF, ID, EX, MEM, WB), diberikan dua instruksi berurutan berikut:\n```assembly\nADD R1, R2, R3   ; R1 = R2 + R3 (Hasil ditulis pada tahap WB)\nSUB R4, R1, R5   ; R4 = R1 - R5 (R1 dibaca pada tahap ID)\n```\nInstruksi `SUB` membutuhkan nilai register `R1` yang baru saja dihitung oleh `ADD`. Jika prosesor tidak menggunakan stall (gelembung tunda), teknik arsitektur perangkat keras yang tepat untuk menyelesaikan bahaya data Read-After-Write (RAW) ini dalam siklus tercepat adalah...",
    "formulaHud": {
      "title": "DATA FORWARDING PADA PIPELINE MIPS 5-STAGE",
      "latex": "\\begin{aligned} \\text{Instruksi 1 (ADD):} & \\quad \\text{IF} \\to \\text{ID} \\to \\mathbf{\\text{EX}} \\xrightarrow{\\text{Forwarding Path}} \\text{MEM} \\to \\text{WB (Tulis R1)} \\\\ \\text{Instruksi 2 (SUB):} & \\quad \\text{IF} \\to \\text{ID} \\to \\mathbf{\\text{EX (Terima R1)}}\\text{ via Multiplexer} \\to \\text{MEM} \\to \\text{WB} \\end{aligned}",
      "legend": "• Hazard RAW: Instruksi berikutnya mencoba membaca register sebelum instruksi sebelumnya menulis kembali hasil akhir<br>• Solusi Tanpa Forwarding: Membutuhkan 2 stall cycle (bubble)<br>• Solusi Dengan Forwarding: 0 stall cycle untuk operasi ALU-ke-ALU"
    },
    "options": [
      {
        "key": "A",
        "text": "Prediksi Cabang Dinamis (Dynamic Branch Prediction), yaitu menebak hasil perhitungan R1 menggunakan tabel Branch Target Buffer (BTB) sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Penerusan Data (Data Forwarding / Bypassing), yaitu menyalurkan hasil perhitungan ALU dari tahap EX atau register perantara EX/MEM milik instruksi `ADD` secara langsung ke input ALU pada tahap EX milik instruksi `SUB` tanpa menunggu tahap WB selesai."
      },
      {
        "key": "C",
        "text": "Instruksi NOP Injection, yaitu menyisipkan sepuluh instruksi kosong ke dalam memori RAM utama untuk menghentikan clock."
      },
      {
        "key": "D",
        "text": "Cache Invalidation, yaitu menghapus seluruh baris cache data L1 agar register R1 dipaksa dimuat ulang dari SSD."
      },
      {
        "key": "E",
        "text": "Spekulasi Eksekusi Terbalik, yaitu membalik urutan eksekusi instruksi SUB sebelum instruksi ADD dimulai."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Penerusan Data (Data Forwarding / Bypassing), yaitu menyalurkan hasil perhitungan ALU dari tahap EX atau register perantara EX/MEM milik instruksi `ADD` secara langsung ke input ALU pada tahap EX milik instruksi `SUB` tanpa menunggu tahap WB selesai.. Teknik meneruskan hasil kalkulasi ALU langsung dari output pipeline EX ke input ALU instruksi berikutnya disebut Data Forwarding (Bypassing). Pilih: Data Forwarding / Bypassing."
  },
  {
    "id": "inf-lat-h-03",
    "materi": "STRUKTUR DATA",
    "topic": "Penyeimbangan Pohon AVL: Operasi Rotasi Ganda Left-Right",
    "hints": {
      "concept": "Kasus Left-Right (LR) diselesaikan dengan rotasi ganda: rotasi kiri pada anak kiri (B), lalu rotasi kanan pada induk (A).",
      "execution": "Pilih: Rotasi Kiri pada simpul anak B, diikuti Rotasi Kanan pada simpul induk A."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah pohon biner seimbang AVL Tree memiliki faktor keseimbangan (Balance Factor) yang didefinisikan sebagai $\\text{BF}(N) = \\text{tinggi}(\\text{kiri}) - \\text{tinggi}(\\text{kanan})$. Jika sebuah penyisipan simpul baru menyebabkan simpul $A$ memiliki $\\text{BF}(A) = +2$ dan anak kirinya simpul $B$ memiliki $\\text{BF}(B) = -1$ (kondisi Left-Right / LR Inbalance), rangkaian operasi rotasi yang wajib dilakukan untuk memulihkan keseimbangan pohon AVL tersebut adalah...",
    "formulaHud": {
      "title": "ROTASI GANDA PADA POHON AVL (LEFT-RIGHT DOUBLE ROTATION)",
      "latex": "\\begin{aligned} \\text{Kondisi Awal (LR):} & \\quad \\text{BF}(A) = +2, \\quad \\text{BF}(\\text{LeftChild}(A)) = -1 \\\\ \\text{Langkah 1 (Rotasi Kiri pada B):} & \\quad B \\xrightarrow{\\text{Left Rotate}} C \\implies \\text{Pohon berubah menjadi format Left-Left (LL)} \\\\ \\text{Langkah 2 (Rotasi Kanan pada A):} & \\quad A \\xrightarrow{\\text{Right Rotate}} C \\implies \\text{Simpul } C \\text{ naik menjadi akar baru terpusat} \\end{aligned}",
      "legend": "• Syarat AVL Tree: $\\text{BF} \\in \\{-1, 0, +1\\}$ untuk setiap simpul<br>• LL Inbalance ($+2, +1$): Cukup 1 Rotasi Kanan<br>• RR Inbalance ($-2, -1$): Cukup 1 Rotasi Kiri<br>• LR Inbalance ($+2, -1$): Rotasi Kiri pada anak, lalu Rotasi Kanan pada induk<br>• RL Inbalance ($-2, +1$): Rotasi Kanan pada anak, lalu Rotasi Kiri pada induk"
    },
    "options": [
      {
        "key": "A",
        "text": "Satu kali Rotasi Kanan tunggal secara langsung pada simpul induk $A$ tanpa memodifikasi simpul anak $B$ ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Rotasi Kanan pada simpul anak $B$ diikuti dengan Rotasi Kiri pada simpul induk $A$ (Right-Left Double Rotation)."
      },
      {
        "key": "C",
        "text": "Rotasi Kiri pada simpul anak $B$ terlebih dahulu (mengubah kondisi menjadi Left-Left), diikuti dengan Rotasi Kanan pada simpul induk $A$ (Left-Right Double Rotation)."
      },
      {
        "key": "D",
        "text": "Dua kali Rotasi Kiri berturut-turut pada simpul induk $A$ hingga seluruh simpul berpindah ke sisi kanan."
      },
      {
        "key": "E",
        "text": "Menghapus simpul yang baru disisipkan secara permanen karena struktur AVL menolak penyisipan asimetris."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Rotasi Kiri pada simpul anak $B$ terlebih dahulu (mengubah kondisi menjadi Left-Left), diikuti dengan Rotasi Kanan pada simpul induk $A$ (Left-Right Double Rotation).. Kasus Left-Right (LR) diselesaikan dengan rotasi ganda: rotasi kiri pada anak kiri (B), lalu rotasi kanan pada induk (A). Pilih: Rotasi Kiri pada simpul anak B, diikuti Rotasi Kanan pada simpul induk A."
  },
  {
    "id": "inf-lat-h-04",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Desain Alokasi Pengalamatan VLSM (Variable Length Subnet Masking)",
    "hints": {
      "concept": "450 host butuh 2^9 - 2 = 510 host (/23). 200 host butuh 2^8 - 2 = 254 host (/24). 100 host butuh 2^7 - 2 = 126 host (/25).",
      "execution": "Pilih: Dep A (/23), Dep B (/24), Dep C (/25)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah perusahaan memiliki blok alamat IP dasar `10.50.0.0/22`. Administrator jaringan ditugaskan merancang subnetting menggunakan VLSM untuk memenuhi 3 kebutuhan departemen terbesar:\n1. Departemen A: Membutuhkan 450 alamat host valid\n2. Departemen B: Membutuhkan 200 alamat host valid\n3. Departemen C: Membutuhkan 100 alamat host valid\nJika pengalokasian subnet dilakukan secara berurutan dari kebutuhan host terbesar ke terkecil tanpa ada pemborosan bit, prefix subnet mask yang tepat dialokasikan untuk Departemen A, B, dan C berturut-turut adalah...",
    "formulaHud": {
      "title": "DESAIN HIERARKIS VLSM BERDASARKAN KEBUTUHAN HOST",
      "latex": "\\begin{aligned} \\text{Dep A (450 host):} & \\quad 2^h - 2 \\ge 450 \\implies h = 9 \\implies \\text{Prefix } 32 - 9 = \\mathbf{/23} \\ (510 \\text{ host}) \\\\ \\text{Dep B (200 host):} & \\quad 2^h - 2 \\ge 200 \\implies h = 8 \\implies \\text{Prefix } 32 - 8 = \\mathbf{/24} \\ (254 \\text{ host}) \\\\ \\text{Dep C (100 host):} & \\quad 2^h - 2 \\ge 100 \\implies h = 7 \\implies \\text{Prefix } 32 - 7 = \\mathbf{/25} \\ (126 \\text{ host}) \\end{aligned}",
      "legend": "• Total IP blok /22 = $2^{10} = 1024$ IP<br>• Alokasi: /23 memakan 512 IP, /24 memakan 256 IP, /25 memakan 128 IP. Total terpakai = 896 IP $\\le 1024$ IP (Efisien tanpa overlap)"
    },
    "options": [
      {
        "key": "A",
        "text": "Departemen A menggunakan `/22` (1022 host valid), Departemen B menggunakan `/23` (510 host valid), dan Departemen C menggunakan `/24` (254 host valid)."
      },
      {
        "key": "B",
        "text": "Departemen A menggunakan `/24` (254 host valid), Departemen B menggunakan `/25` (126 host valid), dan Departemen C menggunakan `/26` (62 host valid)."
      },
      {
        "key": "C",
        "text": "Departemen A menggunakan `/25` (126 host valid), Departemen B menggunakan `/26` (62 host valid), dan Departemen C menggunakan `/27` (30 host valid)."
      },
      {
        "key": "D",
        "text": "Departemen A menggunakan `/23` (510 host valid), Departemen B menggunakan `/24` (254 host valid), dan Departemen C menggunakan `/25` (126 host valid)."
      },
      {
        "key": "E",
        "text": "Seluruh departemen wajib menggunakan prefix seragam `/23` agar router tidak mengalami kegagalan protokol."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Departemen A menggunakan `/23` (510 host valid), Departemen B menggunakan `/24` (254 host valid), dan Departemen C menggunakan `/25` (126 host valid).. 450 host butuh 2^9 - 2 = 510 host (/23). 200 host butuh 2^8 - 2 = 254 host (/24). 100 host butuh 2^7 - 2 = 126 host (/25). Pilih: Dep A (/23), Dep B (/24), Dep C (/25)."
  },
  {
    "id": "inf-lat-h-05",
    "materi": "ANALISIS DATA",
    "topic": "Trade-off Teorema CAP pada Sistem Basis Data Terdistribusi",
    "hints": {
      "concept": "Sistem CP saat terjadi partisi (P) akan memilih menjaga konsistensi (C) dan mengorbankan ketersediaan (A) dengan menolak request pada partisi yang terisolasi.",
      "execution": "Pilih: Mengorbankan Availability demi mencegah terjadinya inkonsistensi data."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam sistem basis data terdistribusi berskala besar (Distributed Databases), Teorema CAP yang dirumuskan oleh Eric Brewer menyatakan bahwa sebuah sistem penyimpanan data terdistribusi hanya mampu menjamin secara maksimal DUA dari TIGA karakteristik berikut: Consistency, Availability, dan Partition Tolerance. Pada kondisi jaringan fisik mengalami pemutusan komunikasi antar kluster server (Network Partitioning terjadi), sistem bertipe CP (Consistency & Partition Tolerance) seperti MongoDB atau HBase akan memilih...",
    "formulaHud": {
      "title": "TEOREMA CAP DALAM SISTEM TERDISTRIBUSI",
      "latex": "\\text{Jaringan Terdistribusi Realistis Wajib Mendukung } \\mathbf{P} \\implies \\text{Pilihan Nyata: } \\mathbf{CP} \\lor \\mathbf{AP}",
      "legend": "• CP (Consistency + Partition Tolerance): Prioritas konsistensi data kuat, rela offline/reject jika partisi putus (misal transaksi perbankan)<br>• AP (Availability + Partition Tolerance): Sistem tetap online melayani klien, menerapkan model Eventual Consistency (misal timeline media sosial Cassandra/DynamoDB)"
    },
    "options": [
      {
        "key": "A",
        "text": "Mengorbankan Consistency; sistem tetap menerima penulisan data baru di semua node meskipun data antar node menjadi tidak sinkron dan bertentangan diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Menghapus seluruh salinan data di seluruh node server secara permanen untuk memulihkan koneksi jaringan fisik."
      },
      {
        "key": "C",
        "text": "Mengubah protokol jaringan secara otomatis menjadi model centralized client-server tanpa melalui proses partisi."
      },
      {
        "key": "D",
        "text": "Memaksa hardware sakelar jaringan fisik untuk tersambung kembali menggunakan sinyal kompresi perangkat lunak."
      },
      {
        "key": "E",
        "text": "Mengorbankan Availability (Ketersediaan); sistem menolak melayani permintaan tulis/baca baru (mengembalikan pesan error atau timeout) pada node yang terisolasi demi mencegah terjadinya inkonsistensi data antar replika server."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Mengorbankan Availability (Ketersediaan); sistem menolak melayani permintaan tulis/baca baru (mengembalikan pesan error atau timeout) pada node yang terisolasi demi mencegah terjadinya inkonsistensi data antar replika server.. Sistem CP saat terjadi partisi (P) akan memilih menjaga konsistensi (C) dan mengorbankan ketersediaan (A) dengan menolak request pada partisi yang terisolasi. Pilih: Mengorbankan Availability demi mencegah terjadinya inkonsistensi data."
  },
  {
    "id": "inf-lat-h-06",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Penanganan Sisi Berbobot Negatif: Dijkstra vs Bellman-Ford",
    "hints": {
      "concept": "Algoritma untuk single-source shortest path dengan bobot negatif dan deteksi negative weight cycle adalah Bellman-Ford.",
      "execution": "Pilih: Algoritma Bellman-Ford dengan relaksasi (|V|-1) kali dan kompleksitas O(|V| . |E|)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Diberikan sebuah graf berarah dengan bobot sisi (directed weighted graph). Jika graf tersebut memuat beberapa sisi dengan bobot bernilai negatif, algoritma Dijkstra tidak dapat diandalkan dan berpotensi menghasilkan rute yang salah. Algoritma alternatif yang tepat digunakan untuk mencari lintasan terpendek dari satu titik sumber serta mampu mendeteksi keberadaan siklus berbobot negatif (negative weight cycle) adalah...",
    "formulaHud": {
      "title": "ALGORITMA BELLMAN-FORD DAN DETEKSI SIKLUS NEGATIF",
      "latex": "\\begin{aligned} \\text{Relaksasi (Iterasi } 1 \\text{ s.d. } |V|-1\\text{):} & \\quad \\text{if } dist[u] + w(u, v) < dist[v] : \\ dist[v] = dist[u] + w(u, v) \\\\ \\text{Deteksi Siklus (Iterasi ke-}|V|\\text{):} & \\quad \\text{if } dist[u] + w(u, v) < dist[v] \\implies \\text{Graf memiliki Negative Cycle!} \\end{aligned}",
      "legend": "• Kelemahan Dijkstra: Greedy approach mengasumsikan jarak yang sudah difinalisasi tidak akan pernah bisa diperpendek lagi (gagal pada bobot negatif)<br>• Keunggulan Bellman-Ford: Mampu menangani bobot negatif dan mendeteksi siklus pengurang nilai tanpa batas"
    },
    "options": [
      {
        "key": "A",
        "text": "Algoritma Bellman-Ford, yang melakukan relaksasi terhadap seluruh $|E|$ sisi graf sebanyak $|V| - 1$ kali dengan kompleksitas waktu $O(|V| \\cdot |E|)$, serta mampu mendeteksi siklus negatif pada relaksasi ke-$|V|$."
      },
      {
        "key": "B",
        "text": "Algoritma Floyd-Warshall, yang hanya dapat mengeksekusi graf tanpa sisi sama sekali dalam waktu linier $O(|V|)$ sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Algoritma Prim, yang khusus dirancang untuk mendeteksi siklus berbobot negatif pada pohon rentang minimum."
      },
      {
        "key": "D",
        "text": "Algoritma Breadth-First Search (BFS), yang secara otomatis mengabaikan bobot negatif dengan mengubahnya menjadi nilai nol."
      },
      {
        "key": "E",
        "text": "Algoritma A* Search, yang selalu menjamin rute terpendek tanpa memerlukan fungsi heuristik admissibel."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Algoritma Bellman-Ford, yang melakukan relaksasi terhadap seluruh $|E|$ sisi graf sebanyak $|V| - 1$ kali dengan kompleksitas waktu $O(|V| \\cdot |E|)$, serta mampu mendeteksi siklus negatif pada relaksasi ke-$|V|$.. Algoritma untuk single-source shortest path dengan bobot negatif dan deteksi negative weight cycle adalah Bellman-Ford. Pilih: Algoritma Bellman-Ford dengan relaksasi (|V|-1) kali dan kompleksitas O(|V| . |E|)."
  },
  {
    "id": "inf-lat-h-07",
    "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
    "topic": "Protokol Pertukaran Kunci Diffie-Hellman dan Logaritma Diskrit",
    "hints": {
      "concept": "Landasan keamanan Diffie-Hellman adalah kesulitan komputasi Masalah Logaritma Diskrit (Discrete Logarithm Problem) modulo bilangan prima besar.",
      "execution": "Pilih opsi: Kesulitan komputasi Masalah Logaritma Diskrit pada grup modulo prima besar."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Protokol pertukaran kunci Diffie-Hellman memungkinkan dua pihak (Alice dan Bob) yang berkomunikasi melalui saluran publik yang tidak aman untuk menyepakati sebuah kunci rahasia bersama (shared secret key) tanpa pernah mengirimkan kunci rahasia tersebut. Keamanan matematis dari protokol Diffie-Hellman bertumpu pada...",
    "formulaHud": {
      "title": "MATEMATIKA PROTOKOL DIFFIE-HELLMAN KEY EXCHANGE",
      "latex": "\\begin{aligned} \\text{Parameter Publik:} & \\quad p \\text{ (Prima Besar)}, \\ g \\text{ (Generator / Primitive Root)} \\\\ \\text{Kunci Privat:} & \\quad a \\text{ (Alice)}, \\ b \\text{ (Bob)} \\\\ \\text{Kunci Publik:} & \\quad A = g^a \\pmod p, \\quad B = g^b \\pmod p \\\\ \\text{Kunci Rahasia Bersama:} & \\quad K = B^a \\pmod p = (g^b)^a = g^{ab} = (g^a)^b = A^b \\pmod p \\end{aligned}",
      "legend": "• Keamanan: Penyerang pasif hanya melihat $p, g, A, B$. Untuk mencari $K$, penyerang harus memecahkan $a$ dari $A = g^a \\pmod p$ (Discrete Logarithm Problem yang teramat sulit)"
    },
    "options": [
      {
        "key": "A",
        "text": "Kecepatan transmisi foton kuantum melalui kabel serat optik bawah laut yang tidak dapat dicegat oleh peretas sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Tingginya kesulitan komputasi Masalah Logaritma Diskrit (Discrete Logarithm Problem) pada grup perkalian medan terhingga modulo bilangan prima besar ($g^a \\pmod p$), di mana menghitung hasil perpangkatan modular sangat mudah, tetapi mencari eksponen $a$ dari nilai publik adalah persoalan yang secara komputasi mustahil diselesaikan dalam waktu wajar."
      },
      {
        "key": "C",
        "text": "Penggunaan kunci simetris rahasia yang telah dipasang secara permanen di pabrik sirkuit prosesor komputer sejak awal."
      },
      {
        "key": "D",
        "text": "Kemustahilan matematis melakukan operasi modulus sisa bagi pada bilangan ganjil yang memiliki lebih dari 10 digit."
      },
      {
        "key": "E",
        "text": "Proses enkripsi satu kali pakai (One-Time Pad) yang secara fisik menghancurkan sinyal data setelah dibaca oleh penerima."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Tingginya kesulitan komputasi Masalah Logaritma Diskrit (Discrete Logarithm Problem) pada grup perkalian medan terhingga modulo bilangan prima besar ($g^a \\pmod p$), di mana menghitung hasil perpangkatan modular sangat mudah, tetapi mencari eksponen $a$ dari nilai publik adalah persoalan yang secara komputasi mustahil diselesaikan dalam waktu wajar.. Landasan keamanan Diffie-Hellman adalah kesulitan komputasi Masalah Logaritma Diskrit (Discrete Logarithm Problem) modulo bilangan prima besar. Pilih opsi: Kesulitan komputasi Masalah Logaritma Diskrit pada grup modulo prima besar."
  },
  {
    "id": "inf-lat-h-08",
    "materi": "SISTEM KOMPUTER",
    "topic": "Pencegahan Kebuntuan Sistem (Deadlock) dan Algoritma Banker",
    "hints": {
      "concept": "Algoritma Banker menguji simulasi alokasi dan hanya mengabulkan permintaan jika sistem tetap berada dalam Status Aman (Safe State).",
      "execution": "Pilih: Menguji alokasi dan hanya memenuhinya jika sistem tetap berada dalam Keadaan Aman (Safe State)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam sistem operasi multiprogramming, kebuntuan sistem (deadlock) terjadi ketika sekumpulan proses saling menunggu sumber daya yang sedang ditahan oleh proses lain dalam himpunan tersebut secara melingkar. Untuk menghindari terjadinya deadlock, sistem operasi dapat menerapkan Algoritma Banker (Dijkstra's Banker Algorithm). Prinsip kerja fundamental dari Algoritma Banker adalah...",
    "formulaHud": {
      "title": "EMPAT KONDISI KEBUTUHAN DEADLOCK (COFFMAN CONDITIONS)",
      "latex": "\\text{Deadlock} \\iff \\text{Mutual Exclusion} \\land \\text{Hold and Wait} \\land \\text{No Preemption} \\land \\text{Circular Wait}",
      "legend": "• Safe State: Status sistem di mana ada setidaknya satu Safe Sequence $\\langle P_1, P_2, \\dots, P_n \\rangle$ alokasi sumber daya yang tidak berujung kebuntuan<br>• Matriks Algoritma Banker: Allocation, Max, Available, Need = Max - Allocation"
    },
    "options": [
      {
        "key": "A",
        "text": "Mematikan (kill) secara paksa seluruh proses aktif yang meminta lebih dari satu sumber daya secara acak ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Mengabaikan pengecekan sumber daya dan langsung mengalokasikan memori hingga kapasitas RAM fisik habis total."
      },
      {
        "key": "C",
        "text": "Menguji setiap permintaan alokasi sumber daya dengan menyimulasikan keadaan alokasi masa depan; permintaan hanya akan dipenuhi jika hasil simulasi menjamin sistem tetap berada dalam Keadaan Aman (Safe State) di mana terdapat urutan eksekusi (safe sequence) yang memungkinkan seluruh proses menyelesaikan tugasnya."
      },
      {
        "key": "D",
        "text": "Memaksa setiap proses untuk berjalan dalam satu utas (single thread) tunggal secara bergiliran menggunakan timer FCFS."
      },
      {
        "key": "E",
        "text": "Mengenkripsi tabel sumber daya sistem sehingga proses yang bersaing tidak dapat saling melihat status alokasi."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Menguji setiap permintaan alokasi sumber daya dengan menyimulasikan keadaan alokasi masa depan; permintaan hanya akan dipenuhi jika hasil simulasi menjamin sistem tetap berada dalam Keadaan Aman (Safe State) di mana terdapat urutan eksekusi (safe sequence) yang memungkinkan seluruh proses menyelesaikan tugasnya.. Algoritma Banker menguji simulasi alokasi dan hanya mengabulkan permintaan jika sistem tetap berada dalam Status Aman (Safe State). Pilih: Menguji alokasi dan hanya memenuhinya jika sistem tetap berada dalam Keadaan Aman (Safe State)."
  },
  {
    "id": "inf-lat-h-09",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Pohon Rentang Minimum (MST) Kruskal dan Disjoint Set Union (DSU)",
    "hints": {
      "concept": "Struktur data standar deteksi siklus pada Kruskal adalah Disjoint Set Union (DSU / Union-Find) dengan Path Compression.",
      "execution": "Pilih: Disjoint Set Union (DSU / Union-Find) dengan Path Compression dan Union by Rank."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Algoritma Kruskal digunakan untuk menemukan Pohon Rentang Minimum (Minimum Spanning Tree / MST) pada graf terhubung berbobot dengan cara mengurutkan seluruh sisi berdasarkan bobotnya dari yang terkecil, lalu memilih sisi satu per satu selama tidak membentuk siklus. Struktur data yang paling efisien digunakan untuk mendeteksi dan mencegah terbentuknya siklus secara instan dalam algoritma Kruskal adalah...",
    "formulaHud": {
      "title": "KOMPLEKSITAS ALGORITMA KRUSKAL DENGAN DSU",
      "latex": "T(V, E) = O(|E| \\log |E|) + O(|E| \\cdot \\alpha(|V|)) \\approx O(|E| \\log |V|)",
      "legend": "• $\\alpha(n)$: Fungsi Inverse Ackermann (tumbuh sangat lambat, $\\alpha(n) \\le 4$ untuk seluruh nilai praktis di alam semesta)<br>• Find(u) == Find(v): Menandakan bahwa kedua simpul sudah berada di komponen yang sama (menambahkan sisi ini akan membentuk siklus!)<br>• Union(u, v): Menggabungkan dua komponen pohon menjadi satu"
    },
    "options": [
      {
        "key": "A",
        "text": "Matriks Ketetanggaan (Adjacency Matrix) dengan penelusuran DFS berulang-ulang yang memiliki kompleksitas waktu $O(|E| \\cdot |V|^2)$ menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Tumpukan Ganda (Double Stack) yang membalikkan urutan pembacaan bobot sisi setiap kali percabangan terdeteksi."
      },
      {
        "key": "C",
        "text": "Tabel Hash linier tanpa penanganan tabrakan yang langsung menghapus sisi berbobot ganjil."
      },
      {
        "key": "D",
        "text": "Disjoint Set Union (DSU / Union-Find) yang dilengkapi teknik Path Compression dan Union by Rank/Size, dengan kompleksitas waktu mendekati linier $O(|E| \\log |E| + |E| \\cdot \\alpha(|V|))$."
      },
      {
        "key": "E",
        "text": "Pohon Biner Terurut (Binary Search Tree) yang menyimpan alamat memori fisik kartu jaringan router."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Disjoint Set Union (DSU / Union-Find) yang dilengkapi teknik Path Compression dan Union by Rank/Size, dengan kompleksitas waktu mendekati linier $O(|E| \\log |E| + |E| \\cdot \\alpha(|V|))$.. Struktur data standar deteksi siklus pada Kruskal adalah Disjoint Set Union (DSU / Union-Find) dengan Path Compression. Pilih: Disjoint Set Union (DSU / Union-Find) dengan Path Compression dan Union by Rank."
  },
  {
    "id": "inf-lat-h-10",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Pencocokan String Cepat Algoritma Knuth-Morris-Pratt (KMP)",
    "hints": {
      "concept": "KMP memanfaatkan tabel LPS (Longest Proper Prefix which is also Suffix) untuk menggeser pola tanpa memundurkan pointer teks.",
      "execution": "Pilih opsi: Tabel Prefix / LPS (Longest Proper Prefix which is also Suffix)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam pencarian pola teks (string matching) di mana pola $P$ berukuran $m$ dicari di dalam teks $T$ berukuran $n$, algoritma pencarian naif membutuhkan waktu terburuk $O(n \\cdot m)$ karena memundurkan penunjuk teks kembali ke awal saat terjadi ketidakcocokan karakter. Algoritma Knuth-Morris-Pratt (KMP) mampu mencapai kompleksitas linier optimal $O(n + m)$ dengan memanfaatkan...",
    "formulaHud": {
      "title": "TABEL LPS (LONGEST PROPER PREFIX SUFFIX) ALGORITMA KMP",
      "latex": "\\text{Kompleksitas Preprocessing Pola: } O(m) + \\text{Kompleksitas Pencarian Teks: } O(n) \\implies T_{\\text{total}} = O(n + m)",
      "legend": "• LPS[i]: Panjang prefiks terpanjang dari $P[0..i]$ yang juga merupakan sufiks dari $P[0..i]$<br>• Manfaat KMP: Penunjuk indeks pada teks utama $T$ tidak pernah bergerak mundur (no backtracking on text), sangat ideal untuk pemrosesan aliran data (data stream)"
    },
    "options": [
      {
        "key": "A",
        "text": "Matriks substitusi probabilitas Markov yang menebak karakter teks berikutnya secara acak diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Fungsi kompresi Huffman yang mengubah seluruh teks dan pola menjadi deretan bit biner tetap sebelum dicari."
      },
      {
        "key": "C",
        "text": "Struktur data Trie raksasa yang menduplikasi teks sebanyak $n$ kali di dalam memori cache sekunder."
      },
      {
        "key": "D",
        "text": "Proses pengurutan alfabetik terhadap teks menggunakan algoritma Quicksort tiga dimensi."
      },
      {
        "key": "E",
        "text": "Tabel Prefix $\\pi$ / LPS (Longest Proper Prefix which is also Suffix), yang menentukan seberapa jauh penunjuk karakter pola dapat digeser ke depan tanpa perlu memeriksa ulang karakter teks yang sudah terbukti cocok sebelumnya."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Tabel Prefix $\\pi$ / LPS (Longest Proper Prefix which is also Suffix), yang menentukan seberapa jauh penunjuk karakter pola dapat digeser ke depan tanpa perlu memeriksa ulang karakter teks yang sudah terbukti cocok sebelumnya.. KMP memanfaatkan tabel LPS (Longest Proper Prefix which is also Suffix) untuk menggeser pola tanpa memundurkan pointer teks. Pilih opsi: Tabel Prefix / LPS (Longest Proper Prefix which is also Suffix)."
  },
  {
    "id": "inf-lat-h-11",
    "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
    "topic": "Arsitektur Komunikasi API Modern: RESTful vs GraphQL",
    "hints": {
      "concept": "Menerima data berlebih yang tidak dibutuhkan disebut Over-fetching. Di GraphQL diselesaikan karena klien dapat meminta persis field yang diinginkan.",
      "execution": "Pilih: Masalah Over-fetching; diselesaikan melalui kueri deklaratif spesifik kebutuhan klien."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam arsitektur pengembangan web dan aplikasi seluler modern, GraphQL dirancang untuk mengatasi beberapa limitasi arsitektur RESTful konvensional. Masalah utama pada arsitektur REST di mana klien menerima terlalu banyak data atribut yang tidak dibutuhkan (misalnya meminta data profil tetapi server mengirim seluruh histori posting dan relasi teman) serta solusinya pada GraphQL adalah...",
    "formulaHud": {
      "title": "KOMPARASI EFISIENSI PAYLOAD REST VS GRAPHQL",
      "latex": "\\begin{aligned} \\text{REST Over-fetching:} & \\quad \\text{GET /user/1} \\implies \\{\\text{id, nama, alamat, nik, no\\_hp, riwayat\\_medis, saldo, ... (50 KB)}\\} \\\\ \\text{GraphQL Declarative:} & \\quad \\text{query } \\{\\text{user(id: 1) } \\{\\text{nama}\\}\\} \\implies \\{\\text{data: } \\{\\text{\"nama\": \"Budi\"}\\} \\ (100 \\text{ Bytes})\\} \\end{aligned}",
      "legend": "• Over-fetching: Menerima data berlebih dari endpoint REST tetap<br>• Under-fetching: Satu endpoint REST tidak cukup, butuh multiple network round-trips<br>• GraphQL: Single endpoint (/graphql), kueri fleksibel sesuai kebutuhan klien"
    },
    "options": [
      {
        "key": "A",
        "text": "Masalah Over-fetching; diselesaikan oleh GraphQL melalui kueri deklaratif di mana klien secara spesifik mendefinisikan atribut persis apa saja yang dibutuhkannya dalam payload permintaan, sehingga server hanya mengirimkan atribut yang diminta."
      },
      {
        "key": "B",
        "text": "Masalah Under-fetching; diselesaikan oleh GraphQL dengan melarang klien mengirimkan parameter kueri ke server sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Masalah Connection Timeout; diselesaikan oleh GraphQL dengan mematikan fungsi enkripsi HTTPS pada jaringan seluler."
      },
      {
        "key": "D",
        "text": "Masalah SQL Injection; diselesaikan oleh GraphQL dengan mengubah seluruh basis data relasional menjadi dokumen XML statis."
      },
      {
        "key": "E",
        "text": "Masalah N+1 Query; diselesaikan oleh GraphQL dengan secara otomatis menambah jumlah tabel basis data hingga ribuan."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Masalah Over-fetching; diselesaikan oleh GraphQL melalui kueri deklaratif di mana klien secara spesifik mendefinisikan atribut persis apa saja yang dibutuhkannya dalam payload permintaan, sehingga server hanya mengirimkan atribut yang diminta.. Menerima data berlebih yang tidak dibutuhkan disebut Over-fetching. Di GraphQL diselesaikan karena klien dapat meminta persis field yang diinginkan. Pilih: Masalah Over-fetching; diselesaikan melalui kueri deklaratif spesifik kebutuhan klien."
  },
  {
    "id": "inf-lat-h-12",
    "materi": "ANALISIS DATA",
    "topic": "Normalisasi Basis Data Lanjut: 3NF vs Boyce-Codd Normal Form (BCNF)",
    "hints": {
      "concept": "Aturan BCNF mensyaratkan untuk setiap ketergantungan fungsional X -> Y, penentu (X) wajib merupakan Superkey.",
      "execution": "Pilih opsi: Jika determinan X bukan merupakan Superkey pada ketergantungan fungsional non-trivial X -> Y."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah tabel relasional sudah memenuhi Bentuk Normal Ketiga (3NF), namun masih memiliki anomali pembaruan (update anomaly). Kondisi spesifik di mana sebuah tabel yang telah memenuhi 3NF dinyatakan BELUM memenuhi Bentuk Normal Boyce-Codd (BCNF) adalah...",
    "formulaHud": {
      "title": "DEFINISI BENTUK NORMAL BOYCE-CODD (BCNF)",
      "latex": "R \\in \\text{BCNF} \\iff \\forall X \\to Y \\text{ (Non-trivial FD)} : \\quad X \\text{ adalah Superkey}",
      "legend": "• Perbedaan 3NF dan BCNF: Pada 3NF, jika $X$ bukan superkey, kondisi masih sah jika $Y$ adalah Prime Attribute (bagian dari candidate key). Pada BCNF, relaksasi ini dihapus secara mutlak ($X$ wajib superkey)<br>• BCNF adalah bentuk normal yang lebih ketat daripada 3NF"
    },
    "options": [
      {
        "key": "A",
        "text": "Jika tabel tersebut memiliki atribut yang nilainya berupa bilangan pecahan desimal yang belum dibulatkan sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Jika pada ketergantungan fungsional non-trivial $X \\to Y$ yang berlaku pada tabel, determinan $X$ BUKAN merupakan Superkey (sering terjadi pada tabel yang memiliki beberapa overlap candidate keys komposit)."
      },
      {
        "key": "C",
        "text": "Jika tabel memiliki ketergantungan parsial di mana kunci primer terdiri dari satu kolom tunggal."
      },
      {
        "key": "D",
        "text": "Jika tabel tidak memiliki indeks clustered B-Tree pada media penyimpanan sekunder fisik."
      },
      {
        "key": "E",
        "text": "Jika jumlah baris rekaman pada tabel melebihi batas 1.000 data entri per partisi disk."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Jika pada ketergantungan fungsional non-trivial $X \\to Y$ yang berlaku pada tabel, determinan $X$ BUKAN merupakan Superkey (sering terjadi pada tabel yang memiliki beberapa overlap candidate keys komposit).. Aturan BCNF mensyaratkan untuk setiap ketergantungan fungsional X -> Y, penentu (X) wajib merupakan Superkey. Pilih opsi: Jika determinan X bukan merupakan Superkey pada ketergantungan fungsional non-trivial X -> Y."
  },
  {
    "id": "inf-lat-h-13",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Protokol Routing Dinamis: Link-State (OSPF) vs Distance-Vector (RIP)",
    "hints": {
      "concept": "OSPF adalah link-state: router memiliki peta topologi utuh via LSA dan menghitung lintasan terpendek bebas loop dengan algoritma Dijkstra (konvergensi cepat).",
      "execution": "Pilih: Memiliki peta topologi global lengkap, menggunakan Dijkstra, dan konvergensi cepat tanpa loop."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Protokol perutean dinamis interior (IGP) dikelompokkan menjadi algoritma Distance-Vector (seperti RIP) dan Link-State (seperti OSPF). Keunggulan arsitektural utama protokol Link-State seperti OSPF dalam jaringan enterprise berskala besar adalah...",
    "formulaHud": {
      "title": "KOMPARASI PROTOKOL ROUTING INTERIOR (IGP)",
      "latex": "\\begin{aligned} \\text{RIP (Distance-Vector):} & \\quad \\text{Metrik: Hop Count (Maks 15)}, \\ \\text{Algoritma: Bellman-Ford}, \\ \\text{Konvergensi Lambat (Looping)} \\\\ \\text{OSPF (Link-State):} & \\quad \\text{Metrik: Cost (Bandwidth)}, \\ \\text{Algoritma: Dijkstra (SPF)}, \\ \\text{Konvergensi Cepat, Area Hierarki} \\end{aligned}",
      "legend": "• LSDB (Link-State Database): Basis data topologi lengkap yang disinkronkan antar router dalam satu area OSPF<br>• SPF Tree: Pohon jalur terpendek dihitung dengan router itu sendiri sebagai akar"
    },
    "options": [
      {
        "key": "A",
        "text": "OSPF hanya mengandalkan informasi jarak lompatan (hop count) dari tetangga langsungnya dan dibatasi maksimal 15 hop ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "OSPF menyiarkan seluruh tabel routingnya secara berkala setiap 30 detik ke seluruh jaringan menggunakan paket broadcast."
      },
      {
        "key": "C",
        "text": "Setiap router memiliki peta topologi jaringan global yang lengkap dan identik melalui pertukaran Link-State Advertisements (LSA) dan menghitung rute bebas loop tercepat menggunakan Algoritma Dijkstra, sehingga konvergensi jaringan tercapai sangat cepat tanpa masalah Count-to-Infinity."
      },
      {
        "key": "D",
        "text": "OSPF tidak memerlukan daya pemrosesan CPU dan memori sama sekali pada perangkat keras router."
      },
      {
        "key": "E",
        "text": "OSPF secara otomatis mengenkripsi kabel tembaga fisik menggunakan protokol token ring nirkabel."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Setiap router memiliki peta topologi jaringan global yang lengkap dan identik melalui pertukaran Link-State Advertisements (LSA) dan menghitung rute bebas loop tercepat menggunakan Algoritma Dijkstra, sehingga konvergensi jaringan tercapai sangat cepat tanpa masalah Count-to-Infinity.. OSPF adalah link-state: router memiliki peta topologi utuh via LSA dan menghitung lintasan terpendek bebas loop dengan algoritma Dijkstra (konvergensi cepat). Pilih: Memiliki peta topologi global lengkap, menggunakan Dijkstra, dan konvergensi cepat tanpa loop."
  },
  {
    "id": "inf-lat-h-14",
    "materi": "SISTEM KOMPUTER",
    "topic": "Protokol Koherensi Cache MESI pada Sistem Multiprocessor",
    "hints": {
      "concept": "MESI singkatan dari: Modified, Exclusive, Shared, Invalid.",
      "execution": "Pilih opsi: Modified, Exclusive, Shared, dan Invalid."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Pada prosesor modern multi-core, setiap inti CPU memiliki cache memori L1/L2 privat masing-masing yang dapat menyimpan salinan variabel data yang sama dari RAM utama. Untuk mencegah terjadinya inkonsistensi data ketika salah satu inti menulis nilai baru ke variabel tersebut, sistem menerapkan protokol koherensi cache MESI. Empat status valid dalam protokol MESI yang merepresentasikan kondisi baris cache tersebut adalah...",
    "formulaHud": {
      "title": "PROTOKOL KOHERENSI CACHE MESI (ILLINOIS PROTOCOL)",
      "latex": "\\text{State MESI} \\equiv \\begin{cases} \\mathbf{M} \\text{ (Modified):} & \\text{Dirty line, eksklusif, RAM belum diperbarui} \\\\ \\mathbf{E} \\text{ (Exclusive):} & \\text{Clean line, hanya ada di cache ini, sama dengan RAM} \\\\ \\mathbf{S} \\text{ (Shared):} & \\text{Clean line, mungkin ada di cache inti lain, sama dengan RAM} \\\\ \\mathbf{I} \\text{ (Invalid):} & \\text{Data usang/tidak valid, wajib reload dari memori jika diakses} \\end{cases}",
      "legend": "• Bus Snooping: Setiap inti cache memantau lalu lintas bus memori<br>• Transisi Write: Inti yang ingin menulis ke status S menyiarkan sinyal invalidate ke inti lain, mengubah status barisnya menjadi M dan inti lain menjadi I"
    },
    "options": [
      {
        "key": "A",
        "text": "Master (pengendali bus), Execution (sedang dihitung), Suspended (ditunda sementara), dan Idle (tidak aktif) menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Monitored (dipantau), Encrypted (terenkripsi), Stored (tersimpan permanen), dan Indexed (terindeks)."
      },
      {
        "key": "C",
        "text": "Memory (di RAM), External (di SSD), Static (konstan), dan Interrupted (terputus sinyal)."
      },
      {
        "key": "D",
        "text": "Modified (data kotor diubah lokal, berbeda dengan RAM), Exclusive (data bersih hanya ada di cache lokal), Shared (data bersih ada di beberapa cache inti), dan Invalid (data sudah usang tidak valid akibat modifikasi inti lain)."
      },
      {
        "key": "E",
        "text": "Main (utama), Ephemeral (sementara), Swapped (ditukar ke disk), dan Isolated (terisolasi)."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Modified (data kotor diubah lokal, berbeda dengan RAM), Exclusive (data bersih hanya ada di cache lokal), Shared (data bersih ada di beberapa cache inti), dan Invalid (data sudah usang tidak valid akibat modifikasi inti lain).. MESI singkatan dari: Modified, Exclusive, Shared, Invalid. Pilih opsi: Modified, Exclusive, Shared, dan Invalid."
  },
  {
    "id": "inf-lat-h-15",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Struktur Data Pohon Segmen (Segment Tree) untuk Range Query",
    "hints": {
      "concept": "Segment Tree melakukan query rentang dan update titik pada tinggi pohon log(n), jadi keduanya berkecepatan O(log n).",
      "execution": "Pilih: O(log n) untuk Range Minimum Query dan O(log n) untuk Point Update."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi sistem informasi geografis memerlukan kalkulasi berkala nilai minimum pada rentang indeks $[L, R]$ (Range Minimum Query / RMQ) serta pembaruan nilai elemen tunggal pada indeks $k$ (Point Update) secara bergantian pada larik berisi $n = 100.000$ data. Jika digunakan struktur data Segment Tree, kompleksitas waktu asimtotik untuk operasi Range Query dan Point Update secara berturut-turut adalah...",
    "formulaHud": {
      "title": "KOMPLEKSITAS OPERASI STRUKTUR DATA SEGMENT TREE",
      "latex": "\\begin{aligned} \\text{Build Tree:} & \\quad O(n) \\\\ \\text{Point Update (Perbarui 1 Elemen):} & \\quad O(\\log n) \\\\ \\text{Range Query (Hitung Nilai Segmen } [L, R]\\text{):} & \\quad O(\\log n) \\\\ \\text{Ruang Memori (Ukuran Larik Simpul):} & \\quad \\le 4n \\end{aligned}",
      "legend": "• Keunggulan Segment Tree: Menggabungkan efisiensi query dan update dinamis pada $O(\\log n)$<br>• Pohon Biner Sempurna: Setiap simpul internal menyimpan hasil agregasi (min, sum, gcd) dari kedua anak segmennya"
    },
    "options": [
      {
        "key": "A",
        "text": "$O(1)$ untuk Range Minimum Query dan $O(n)$ untuk Point Update, dengan waktu pembangunan awal $O(n^2)$ diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "$O(n)$ untuk Range Minimum Query dan $O(1)$ untuk Point Update, seperti halnya larik statis sederhana."
      },
      {
        "key": "C",
        "text": "$O(n \\log_2 n)$ untuk Range Minimum Query dan $O(n \\log_2 n)$ untuk Point Update."
      },
      {
        "key": "D",
        "text": "$O(1)$ untuk Range Minimum Query dan $O(1)$ untuk Point Update konstan instan."
      },
      {
        "key": "E",
        "text": "$O(\\log_2 n)$ untuk Range Minimum Query dan $O(\\log_2 n)$ untuk Point Update, dengan waktu pembangunan pohon awal sebesar $O(n)$."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $O(\\log_2 n)$ untuk Range Minimum Query dan $O(\\log_2 n)$ untuk Point Update, dengan waktu pembangunan pohon awal sebesar $O(n)$.. Segment Tree melakukan query rentang dan update titik pada tinggi pohon log(n), jadi keduanya berkecepatan O(log n). Pilih: O(log n) untuk Range Minimum Query dan O(log n) untuk Point Update."
  },
  {
    "id": "inf-lat-h-16",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Paradigma Keamanan Arsitektur Zero Trust (Never Trust, Always Verify)",
    "hints": {
      "concept": "Prinsip inti Zero Trust: \"Never Trust, Always Verify\" dan menerapkan hak akses terendah (Least Privilege).",
      "execution": "Pilih opsi yang mencantumkan \"Never Trust, Always Verify\" dan prinsip hak akses terkecil (Least Privilege)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Model keamanan jaringan tradisional berbasis perimeter (Castle-and-Moat) mengasumsikan bahwa seluruh entitas di dalam jaringan lokal (intranet) adalah tepercaya. Kelemahan fatal model ini terbukti saat penyerang berhasil membobol satu perangkat internal dan leluasa melakukan pergerakan lateral (lateral movement). Paradigma modern Zero Trust Architecture (ZTA) mengatasi kerentanan ini dengan menerapkan prinsip inti...",
    "formulaHud": {
      "title": "TIGA PRINSIP UTAMA ARSITEKTUR ZERO TRUST (NIST SP 800-207)",
      "latex": "\\text{Zero Trust} \\equiv \\text{Verify Explicitly} \\cap \\text{Use Least Privilege Access} \\cap \\text{Assume Breach}",
      "legend": "• Verify Explicitly: Otentikasi dan otorisasi selalu berdasarkan identitas, lokasi, kesehatan perangkat, dan anomali data<br>• Least Privilege: Batasi akses pengguna hanya pada sumber daya yang benar-benar esensial (JIT & JEA)<br>• Assume Breach: Minimalkan radius ledakan (blast radius) melalui mikrosegmentasi jaringan"
    },
    "options": [
      {
        "key": "A",
        "text": "\"Never Trust, Always Verify\"; tidak ada pengguna, perangkat, atau beban kerja yang dipercaya secara bawaan meskipun berada di dalam jaringan internal, sehingga setiap permintaan akses wajib diotentikasi, diotorisasi, dan dienkripsi secara ketat berdasarkan konteks hak akses terkecil (Least Privilege)."
      },
      {
        "key": "B",
        "text": "Mematikan seluruh sistem pertahanan firewall dan membiarkan jaringan terbuka bebas demi transparansi data publik sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Memberikan hak akses Administrator (Root) penuh kepada seluruh karyawan agar operasional kantor tidak terhambat."
      },
      {
        "key": "D",
        "text": "Hanya mempercayai perangkat komputer yang dibeli secara langsung dari pabrik tanpa memerlukan kata sandi masuk."
      },
      {
        "key": "E",
        "text": "Menghapus seluruh berkas enkripsi sertifikat SSL agar lalu lintas data dapat dipantau oleh siapa saja."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) \"Never Trust, Always Verify\"; tidak ada pengguna, perangkat, atau beban kerja yang dipercaya secara bawaan meskipun berada di dalam jaringan internal, sehingga setiap permintaan akses wajib diotentikasi, diotorisasi, dan dienkripsi secara ketat berdasarkan konteks hak akses terkecil (Least Privilege).. Prinsip inti Zero Trust: \"Never Trust, Always Verify\" dan menerapkan hak akses terendah (Least Privilege). Pilih opsi yang mencantumkan \"Never Trust, Always Verify\" dan prinsip hak akses terkecil (Least Privilege)."
  },
  {
    "id": "inf-lat-h-17",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Pengurutan Topologis (Topological Sort) Menggunakan Algoritma Kahn",
    "hints": {
      "concept": "Algoritma Kahn memasukkan simpul dengan in-degree = 0 ke Queue, mencatatnya, lalu mengurangi in-degree tetangganya.",
      "execution": "Pilih: Menghitung in-degree, memasukkan simpul in-degree = 0 ke Queue, dan mengurangi in-degree tetangganya."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam manajemen penjadwalan kompilasi dependensi paket perangkat lunak yang dimodelkan sebagai Directed Acyclic Graph (DAG), pengurutan linier simpul di mana setiap sisi terarah $(u, v)$ menuntut $u$ dieksekusi sebelum $v$ disebut Topological Sort. Algoritma Kahn mengimplementasikan pengurutan topologis dengan menggunakan konsep derajat masuk (In-Degree). Langkah inisialisasi yang tepat pada algoritma Kahn adalah...",
    "formulaHud": {
      "title": "ALUR KERJA ALGORITMA KAHN (TOPOLOGICAL SORT)",
      "latex": "\\begin{aligned} 1. & \\quad \\text{Hitung } \\text{in\\_degree}[v] \\ \\forall v \\in V \\\\ 2. & \\quad Q = \\{v \\mid \\text{in\\_degree}[v] == 0\\} \\\\ 3. & \\quad \\text{while } Q \\ne \\emptyset : \\ u = Q.\\text{pop}() \\to \\text{Hasil.append}(u) \\to \\forall (u, v) : \\text{in\\_degree}[v]-- \\ (\\text{if } 0 \\implies Q.\\text{push}(v)) \\end{aligned}",
      "legend": "• Syarat Graf: Wajib berupa DAG (Directed Acyclic Graph). Jika di akhir hasil pengurutan jumlah simpul < $|V|$, maka graf memuat siklus (terjadi deadlock dependensi)<br>• Kompleksitas Waktu: $O(V + E)$ linier"
    },
    "options": [
      {
        "key": "A",
        "text": "Memasukkan simpul yang memiliki In-Degree tertinggi ke dalam tumpukan (Stack) lalu menghapus seluruh sisi masuk sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Menghitung In-Degree setiap simpul, memasukkan seluruh simpul yang memiliki In-Degree sama dengan 0 ke dalam antrean (Queue), lalu secara berulang mengeluarkan simpul dari antrean dan mengurangi In-Degree simpul-simpul tetangganya."
      },
      {
        "key": "C",
        "text": "Mengurutkan simpul secara alfabetis berdasarkan label nama teks menggunakan algoritma Quicksort rekursif."
      },
      {
        "key": "D",
        "text": "Mencari jalur lintasan terpendek menggunakan algoritma Dijkstra dimulai dari simpul berbobot sisi negatif."
      },
      {
        "key": "E",
        "text": "Membalikkan arah panah seluruh sisi pada graf dan mencari pohon rentang minimum menggunakan algoritma Prim."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Menghitung In-Degree setiap simpul, memasukkan seluruh simpul yang memiliki In-Degree sama dengan 0 ke dalam antrean (Queue), lalu secara berulang mengeluarkan simpul dari antrean dan mengurangi In-Degree simpul-simpul tetangganya.. Algoritma Kahn memasukkan simpul dengan in-degree = 0 ke Queue, mencatatnya, lalu mengurangi in-degree tetangganya. Pilih: Menghitung in-degree, memasukkan simpul in-degree = 0 ke Queue, dan mengurangi in-degree tetangganya."
  },
  {
    "id": "inf-lat-h-18",
    "materi": "ANALISIS DATA",
    "topic": "Pemberian Peringkat dengan Window Function SQL: RANK() vs DENSE_RANK()",
    "hints": {
      "concept": "Nilai 100 (rank 1, dense 1). Nilai 95 & 95 (rank 2 & 2, dense 2 & 2). Nilai 90 berikutnya mendapat rank 4 (karena lewati 3) dan dense_rank 3.",
      "execution": "Pilih: rnk = 4 dan drnk = 3."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Diberikan tabel `Nilai_Siswa` dengan nilai skor matematika: `[100, 95, 95, 90, 85]`. Seorang analis mengeksekusi kueri SQL menggunakan fungsi analitis jendela (Window Function):\n```sql\nSELECT nama, nilai,\n       RANK() OVER (ORDER BY nilai DESC) as rnk,\n       DENSE_RANK() OVER (ORDER BY nilai DESC) as drnk\nFROM Nilai_Siswa;\n```\nNilai peringkat `rnk` dan `drnk` yang akan diperoleh oleh siswa yang mendapatkan nilai `90` secara berturut-turut adalah...",
    "formulaHud": {
      "title": "KOMPARASI WINDOW FUNCTION PERINGKAT SQL",
      "latex": "\\begin{array}{|c|c|c|c|} \\hline \\text{Nilai} & \\text{ROW\\_NUMBER()} & \\text{RANK()} & \\text{DENSE\\_RANK()} \\\\ \\hline 100 & 1 & 1 & 1 \\\\ 95 & 2 & 2 & 2 \\\\ 95 & 3 & 2 & 2 \\\\ \\mathbf{90} & 4 & \\mathbf{4} & \\mathbf{3} \\\\ 85 & 5 & 5 & 4 \\\\ \\hline \\end{array}",
      "legend": "• ROW_NUMBER(): Menghasilkan nomor urut baris unik berkelanjutan tanpa peduli nilai kembar<br>• RANK(): Memberikan peringkat sama pada nilai kembar, lalu MELOMPATI nomor urut berikutnya ($1, 2, 2, 4$)<br>• DENSE_RANK(): Memberikan peringkat sama pada nilai kembar TANPA melompati nomor ($1, 2, 2, 3$)"
    },
    "options": [
      {
        "key": "A",
        "text": "`rnk = 3` dan `drnk = 4`, karena fungsi RANK() selalu memprioritaskan nomor urut yang lebih padat ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "`rnk = 3` dan `drnk = 3`, karena kedua fungsi menghasilkan urutan peringkat yang identik pada semua kasus."
      },
      {
        "key": "C",
        "text": "`rnk = 4` dan `drnk = 3`, karena `RANK()` melompati nomor urutan berikutnya setelah ada nilai kembar seri (1, 2, 2, 4), sedangkan `DENSE_RANK()` tidak pernah melompati nomor peringkat (1, 2, 2, 3)."
      },
      {
        "key": "D",
        "text": "`rnk = 4` dan `drnk = 4`, karena nomor peringkat siswa selalu disesuaikan dengan posisi indeks baris tabel."
      },
      {
        "key": "E",
        "text": "`rnk = 2` dan `drnk = 2`, karena nilai kembar dianggap sebagai satu kesatuan data tunggal tanpa pembagian."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) `rnk = 4` dan `drnk = 3`, karena `RANK()` melompati nomor urutan berikutnya setelah ada nilai kembar seri (1, 2, 2, 4), sedangkan `DENSE_RANK()` tidak pernah melompati nomor peringkat (1, 2, 2, 3).. Nilai 100 (rank 1, dense 1). Nilai 95 & 95 (rank 2 & 2, dense 2 & 2). Nilai 90 berikutnya mendapat rank 4 (karena lewati 3) dan dense_rank 3. Pilih: rnk = 4 dan drnk = 3."
  },
  {
    "id": "inf-lat-h-19",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Algoritma Kontrol Kemacetan TCP: Slow Start dan AIMD",
    "hints": {
      "concept": "Setelah Slow Start melewati ssthresh, TCP masuk fase Congestion Avoidance yang menaikkan cwnd secara linier (+1 MSS per RTT).",
      "execution": "Pilih: Congestion Avoidance, dengan peningkatan linier sebesar 1 MSS per RTT (Additive Increase)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Protokol TCP mengimplementasikan mekanisme pengendalian kemacetan (Congestion Control) untuk mencegah jaringan internet mengalami kelebihan beban paket data. Pada fase Slow Start, ukuran jendela kemacetan (Congestion Window / `cwnd`) digandakan secara eksponensial setiap siklus RTT hingga mencapai ambang batas `ssthresh`. Ketika `cwnd` telah melampaui `ssthresh`, fase kontrol TCP yang aktif selanjutnya serta pola penambahan ukurannya adalah...",
    "formulaHud": {
      "title": "MEKANISME PENGENDALIAN KEMACETAN TCP (AIMD)",
      "latex": "\\begin{aligned} \\text{Slow Start (}\\text{cwnd} < \\text{ssthresh}\\text{):} & \\quad \\text{cwnd} = \\text{cwnd} \\times 2 \\ \\text{per RTT (Eksponensial)} \\\\ \\text{Congestion Avoidance (}\\text{cwnd} \\ge \\text{ssthresh}\\text{):} & \\quad \\text{cwnd} = \\text{cwnd} + 1 \\text{ MSS per RTT (Linier / Additive Increase)} \\\\ \\text{Deteksi Paket Hilang (Timeout):} & \\quad \\text{ssthresh} = \\frac{\\text{cwnd}}{2}, \\quad \\text{cwnd} = 1 \\text{ MSS (Multiplicative Decrease)} \\end{aligned}",
      "legend": "• AIMD: Additive Increase, Multiplicative Decrease menjamin kestabilan dan keadilan (fairness) pembagian bandwidth internet antar koneksi"
    },
    "options": [
      {
        "key": "A",
        "text": "Fase Fast Retransmit, di mana `cwnd` langsung diturunkan menjadi 0 byte untuk menghentikan transmisi paket menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Fase Exponential Burst, di mana `cwnd` dinaikkan menjadi kuadrat dari nilai sebelumnya setiap milidetik."
      },
      {
        "key": "C",
        "text": "Fase Multiplicative Decrease, di mana jendela kemacetan diperbesar sepuluh kali lipat untuk memaksa router bekerja."
      },
      {
        "key": "D",
        "text": "Fase Penghindaran Kemacetan (Congestion Avoidance), di mana `cwnd` ditingkatkan secara linier sebesar 1 MSS (Maximum Segment Size) setiap RTT (prinsip Additive Increase)."
      },
      {
        "key": "E",
        "text": "Fase Static Allocation, di mana ukuran jendela dikunci secara permanen dan tidak dapat diubah kembali."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Fase Penghindaran Kemacetan (Congestion Avoidance), di mana `cwnd` ditingkatkan secara linier sebesar 1 MSS (Maximum Segment Size) setiap RTT (prinsip Additive Increase).. Setelah Slow Start melewati ssthresh, TCP masuk fase Congestion Avoidance yang menaikkan cwnd secara linier (+1 MSS per RTT). Pilih: Congestion Avoidance, dengan peningkatan linier sebesar 1 MSS per RTT (Additive Increase)."
  },
  {
    "id": "inf-lat-h-20",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Strategi Penelusuran Balik (Backtracking) dan Pemangkasan Cabang (Pruning)",
    "hints": {
      "concept": "Pruning pada Backtracking menghentikan eksplorasi cabang sesaat setelah kondisi tidak valid terdeteksi, lalu kembali (backtrack) ke langkah sebelumnya.",
      "execution": "Pilih opsi: Menghentikan eksplorasi cabang saat penempatan melanggar aturan dan langsung mundur (backtrack)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam memecahkan masalah penempatan $N$ Ratu pada papan catur ukuran $N \\times N$ (N-Queens Problem) sedemikian rupa sehingga tidak ada dua ratu yang saling menyerang, pendekatan brute-force mencoba seluruh $\\binom{N^2}{N}$ kombinasi yang membutuhkan waktu teramat lambat. Pendekatan Backtracking menyelesaikan masalah ini jauh lebih efisien karena menerapkan teknik pemangkasan cabang (pruning). Mekanisme pruning pada algoritma ini bekerja dengan cara...",
    "formulaHud": {
      "title": "PRINSIP PEMANGKASAN CABANG (PRUNING) ALGORITMA BACKTRACKING",
      "latex": "\\text{Ruang Status Brute-Force: } O(N^N) \\xrightarrow{\\text{Pruning State Valid}} \\text{Pencarian Efisien Terfokus}",
      "legend": "• Vektor Solusi: $Q[i] = c$, menyatakan ratu pada baris $i$ ditempatkan di kolom $c$<br>• Syarat Konflik: $Q[i] == Q[k]$ (Kolom Sama) atau $|Q[i] - Q[k]| == |i - k|$ (Diagonal Sama)<br>• Jika konflik terdeteksi pada baris $i$, sub-pohon baris $i+1 \\dots N$ langsung dipangkas (pruned)"
    },
    "options": [
      {
        "key": "A",
        "text": "Menghapus seluruh baris papan catur yang tidak memuat bidak ratu pada awal eksekusi program diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Mengubah representasi papan catur menjadi graf tak berarah dan mencari siklus Euler menggunakan matriks."
      },
      {
        "key": "C",
        "text": "Mengabaikan aturan pergerakan diagonal ratu dan hanya memeriksa benturan pada baris horizontal saja."
      },
      {
        "key": "D",
        "text": "Membalikkan nilai koordinat ratu menggunakan operasi bitwise XOR pada memori register mikroprosesor."
      },
      {
        "key": "E",
        "text": "Menghentikan eksplorasi cabang pohon pencarian seketika saat penempatan ratu baru terbukti melanggar kendali keselamatan (berada di baris, kolom, atau diagonal yang sama dengan ratu sebelumnya), lalu mundur (backtrack) ke langkah sebelumnya tanpa menjelajahi sub-cabang di bawahnya."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Menghentikan eksplorasi cabang pohon pencarian seketika saat penempatan ratu baru terbukti melanggar kendali keselamatan (berada di baris, kolom, atau diagonal yang sama dengan ratu sebelumnya), lalu mundur (backtrack) ke langkah sebelumnya tanpa menjelajahi sub-cabang di bawahnya.. Pruning pada Backtracking menghentikan eksplorasi cabang sesaat setelah kondisi tidak valid terdeteksi, lalu kembali (backtrack) ke langkah sebelumnya. Pilih opsi: Menghentikan eksplorasi cabang saat penempatan melanggar aturan dan langsung mundur (backtrack)."
  },
  {
    "id": "inf-lat-h-21",
    "materi": "SISTEM KOMPUTER",
    "topic": "Fragmentasi Memori dan Strategi Alokasi Dinamis: First-Fit vs Best-Fit",
    "hints": {
      "concept": "Fragmentasi eksternal: total memori bebas cukup, namun terpecah-pecah menjadi lubang kecil yang tidak berdampingan (non-contiguous).",
      "execution": "Pilih: Total memori kosong mencukupi tetapi terpecah-pecah menjadi blok kecil yang tidak bersebelahan."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam manajemen memori sistem operasi tanpa paging (contiguous memory allocation), pemuatan dan penghentian proses secara bergantian dapat menyebabkan fenomena Fragmentasi Eksternal (External Fragmentation). Kondisi yang mencirikan terjadinya fragmentasi eksternal adalah...",
    "formulaHud": {
      "title": "KOMPARASI FRAGMENTASI MEMORI SISTEM OPERASI",
      "latex": "\\begin{aligned} \\text{Fragmentasi Internal:} & \\quad \\text{Ruang terbuang DI DALAM blok partisi teralokasi (Partisi Tetap)} \\\\ \\text{Fragmentasi Eksternal:} & \\quad \\text{Total memori bebas } \\sum \\text{Hole} \\ge \\text{Kebutuhan}, \\text{ tapi NON-CONTIGUOUS (Partisi Dinamis)} \\end{aligned}",
      "legend": "• Solusi Fragmentasi Eksternal: Pemadatan Memori (Compaction) atau beralih ke Memori Virtual Paging<br>• Strategi Alokasi: First-Fit (tercepat), Best-Fit (menyisakan lubang terkecil), Worst-Fit (menyisakan lubang terbesar)"
    },
    "options": [
      {
        "key": "A",
        "text": "Total ruang memori kosong yang tersedia di sistem sebenarnya mencukupi untuk menampung proses baru, namun ruang memori tersebut terpecah-pecah menjadi blok-blok kecil yang tidak berurutan (non-contiguous) sehingga sistem gagal mengalokasikannya."
      },
      {
        "key": "B",
        "text": "Ruang memori yang dialokasikan untuk suatu proses jauh lebih besar daripada kebutuhan data proses sehingga terjadi pemborosan ruang di dalam blok partisi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Modul perangkat keras RAM mengalami kerusakan sirkuit fisik akibat kelebihan panas voltase listrik."
      },
      {
        "key": "D",
        "text": "Sistem operasi kehabisan alamat bit register Program Counter untuk mengeksekusi instruksi perulangan."
      },
      {
        "key": "E",
        "text": "Kecepatan transfer data memori cache L3 lebih lambat daripada kecepatan pembacaan piringan magnetik hard disk."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Total ruang memori kosong yang tersedia di sistem sebenarnya mencukupi untuk menampung proses baru, namun ruang memori tersebut terpecah-pecah menjadi blok-blok kecil yang tidak berurutan (non-contiguous) sehingga sistem gagal mengalokasikannya.. Fragmentasi eksternal: total memori bebas cukup, namun terpecah-pecah menjadi lubang kecil yang tidak berdampingan (non-contiguous). Pilih: Total memori kosong mencukupi tetapi terpecah-pecah menjadi blok kecil yang tidak bersebelahan."
  },
  {
    "id": "inf-lat-h-22",
    "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
    "topic": "Mekanisme Otentikasi dan Non-Repudiation pada Tanda Tangan Digital",
    "hints": {
      "concept": "Digital Signature dibuat dengan mengenkripsi hash pesan memakai Kunci Privat pengirim. Diverifikasi penerima memakai Kunci Publik pengirim.",
      "execution": "Pilih: Alice mengenkripsi hash memakai Private Key miliknya; Bob memverifikasi mendekripsi memakai Public Key Alice."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Tanda Tangan Digital (Digital Signature) menjamin integritas data, otentikasi pengirim, dan nirsangkal (non-repudiation) dalam transaksi elektronik. Alur pembentukan tanda tangan digital oleh pengirim (Alice) serta proses verifikasinya oleh penerima (Bob) yang benar secara kriptografis adalah...",
    "formulaHud": {
      "title": "ALUR KRIPTOGRAFIS TANDA TANGAN DIGITAL (DIGITAL SIGNATURE)",
      "latex": "\\begin{aligned} \\text{Pemberian Tanda Tangan (Alice):} & \\quad S = \\text{Encrypt}_{\\text{Priv}_A}(\\text{Hash}(M)) \\\\ \\text{Verifikasi Tanda Tangan (Bob):} & \\quad \\text{Decrypt}_{\\text{Pub}_A}(S) \\stackrel{?}{=} \\text{Hash}(M) \\implies \\text{Otentik & Utuh!} \\end{aligned}",
      "legend": "• Non-Repudiation (Nirsangkal): Hanya Alice yang memiliki Private Key miliknya, sehingga Alice tidak dapat menyangkal telah menandatangani pesan tersebut<br>• Integritas: Jika pesan $M$ dimodifikasi penyerang sekecil apapun, nilai hash tidak akan cocok"
    },
    "options": [
      {
        "key": "A",
        "text": "Alice mengenkripsi seluruh dokumen menggunakan Public Key milik Bob; Bob mendekripsinya menggunakan Private Key milik Alice sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Alice membuat intisari pesan (hash) $\\rightarrow$ Mengenkripsi hash tersebut menggunakan Private Key miliknya sendiri untuk menghasilkan Digital Signature; Bob memverifikasinya dengan mendekripsi Digital Signature menggunakan Public Key milik Alice, lalu membandingkan hasilnya dengan hash dokumen yang dihitungnya sendiri."
      },
      {
        "key": "C",
        "text": "Alice mengenkripsi hash dokumen menggunakan Public Key milik Bob; Bob mendekripsinya menggunakan kunci simetris AES bersama."
      },
      {
        "key": "D",
        "text": "Alice menandatangani berkas dengan foto tanda tangan basah; Bob memverifikasinya menggunakan perangkat lunak OCR komputer."
      },
      {
        "key": "E",
        "text": "Alice mengirimkan Private Key miliknya ke Bob melalui surel terbuka agar Bob dapat mendekripsi dokumen rahasia."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Alice membuat intisari pesan (hash) $\\rightarrow$ Mengenkripsi hash tersebut menggunakan Private Key miliknya sendiri untuk menghasilkan Digital Signature; Bob memverifikasinya dengan mendekripsi Digital Signature menggunakan Public Key milik Alice, lalu membandingkan hasilnya dengan hash dokumen yang dihitungnya sendiri.. Digital Signature dibuat dengan mengenkripsi hash pesan memakai Kunci Privat pengirim. Diverifikasi penerima memakai Kunci Publik pengirim. Pilih: Alice mengenkripsi hash memakai Private Key miliknya; Bob memverifikasi mendekripsi memakai Public Key Alice."
  },
  {
    "id": "inf-lat-h-23",
    "materi": "PRAKTIK LINTAS BIDANG",
    "topic": "Strategi Rilis Perangkat Lunak: Blue-Green vs Canary Deployment",
    "hints": {
      "concept": "Canary deployment mengalirkan persentase kecil traffic (misal 5-10%) ke versi baru bertahap sambil memantau metrik kesehatan aplikasi.",
      "execution": "Pilih opsi yang menjelaskan pengalihan sebagian kecil lalu lintas secara bertahap sambil memantau metrik performa."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam arsitektur pipeline CI/CD modern, tim rekayasa perangkat lunak ingin merilis pembaruan aplikasi besar tanpa mengalami waktu henti (zero downtime) dan meminimalkan risiko gangguan operasional bagi seluruh pengguna. Strategi rilis Canary Deployment bekerja dengan cara...",
    "formulaHud": {
      "title": "KOMPARASI STRATEGI DEPLOYMENT MODERN",
      "latex": "\\begin{aligned} \\text{Blue-Green:} & \\quad \\text{Environment Aktif (Blue)} \\xrightarrow{\\text{Switch Router 100\\%}} \\text{Environment Baru (Green)} \\implies \\text{Instant Switch} \\\\ \\text{Canary:} & \\quad 95\\% \\text{ Traffic} \\to v1.0 \\quad \\land \\quad 5\\% \\text{ Traffic} \\to v2.0 \\implies \\text{Gradual Rollout & Telemetry Audit} \\end{aligned}",
      "legend": "• Asal Istilah: Burung kenari (canary) di tambang batu bara sebagai pendeteksi dini gas beracun<br>• Keunggulan Canary: Jika ada bug fatal, hanya sebagian kecil pengguna uji coba yang terdampak sebelum rilis massal"
    },
    "options": [
      {
        "key": "A",
        "text": "Menyiapkan dua lingkungan produksi identik penuh (Blue dan Green) lalu mengalihkan sakelar router 100% secara instan ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Mematikan server produksi selama 6 jam di tengah malam untuk menginstal pembaruan basis data secara manual."
      },
      {
        "key": "C",
        "text": "Mengarahkan sebagian kecil lalu lintas pengguna nyata (misalnya 5%–10%) ke versi aplikasi baru secara bertahap sambil memantau metrik performa dan log galat; jika stabil, lalu lintas dinaikkan bertahap hingga 100%, namun jika terdeteksi galat, rute lalu lintas langsung dibalikkan kembali ke versi lama."
      },
      {
        "key": "D",
        "text": "Merilis kode yang belum diuji coba langsung ke repositori publik tanpa melalui tahapan kompilasi dan audit keamanan."
      },
      {
        "key": "E",
        "text": "Menghapus seluruh basis data pengguna lama agar aplikasi versi baru dapat berjalan dengan memori kosong optimal."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Mengarahkan sebagian kecil lalu lintas pengguna nyata (misalnya 5%–10%) ke versi aplikasi baru secara bertahap sambil memantau metrik performa dan log galat; jika stabil, lalu lintas dinaikkan bertahap hingga 100%, namun jika terdeteksi galat, rute lalu lintas langsung dibalikkan kembali ke versi lama.. Canary deployment mengalirkan persentase kecil traffic (misal 5-10%) ke versi baru bertahap sambil memantau metrik kesehatan aplikasi. Pilih opsi yang menjelaskan pengalihan sebagian kecil lalu lintas secara bertahap sambil memantau metrik performa."
  },
  {
    "id": "inf-lat-h-24",
    "materi": "ANALISIS DATA",
    "topic": "Analisis Asosiasi Fitur: Korelasi Pearson vs Spearman Rank",
    "hints": {
      "concept": "Untuk hubungan monotonik non-linier dan data bertingkat, gunakan Korelasi Spearman Rank (berbasis peringkat data).",
      "execution": "Pilih: Koefisien Korelasi Spearman Rank (r_s)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Seorang data scientist memeriksa hubungan antara jam belajar harian ($X$) dan nilai ujian kelulusan ($Y$). Setelah dibuatkan diagram pencar (scatter plot), terlihat bahwa hubungan antar variabel bersifat monotonik non-linier melengkung kuat (eksponensial mulus tanpa hubungan garis lurus sempurna). Koefisien korelasi yang paling valid dan akurat digunakan untuk mengukur kekuatan hubungan monotonik tersebut adalah...",
    "formulaHud": {
      "title": "KOMPARASI KOEFISIEN KORELASI STATISTIKA DATA",
      "latex": "\\begin{aligned} \\text{Pearson } r: & \\quad \\frac{\\sum (X - \\bar{X})(Y - \\bar{Y})}{\\sqrt{\\sum (X - \\bar{X})^2 \\sum (Y - \\bar{Y})^2}} \\implies \\text{Hubungan Garis Lurus (Linier Murni)} \\\\ \\text{Spearman } r_s: & \\quad 1 - \\frac{6 \\sum d_i^2}{n(n^2 - 1)} \\implies \\text{Hubungan Monotonik Non-Linier Berdasarkan Ranking} \\end{aligned}",
      "legend": "• Monotonik: Ketika $X$ naik, $Y$ selalu naik (atau selalu turun), meskipun tidak membentuk garis lurus linier<br>• Pearson sensitif terhadap outlier dan gagal mendeteksi kelengkungan non-linier"
    },
    "options": [
      {
        "key": "A",
        "text": "Koefisien Korelasi Pearson ($r$), karena secara eksklusif hanya mengukur hubungan keterkaitan garis lurus linier sempurna antar variabel kontinu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Koefisien Determinasi Regresi Kuadrat Terkecil, yang mengasumsikan variansi galat berdistribusi Poisson diskret."
      },
      {
        "key": "C",
        "text": "Uji Hipotesis Chi-Square Independensi, yang khusus dirancang untuk menguji keterkaitan dua variabel data kategorik nominal."
      },
      {
        "key": "D",
        "text": "Koefisien Korelasi Spearman Rank ($r_s$), karena menghitung korelasi berdasarkan peringkat data (ranking) sehingga mampu menangkap hubungan monotonik non-linier dan lebih tangguh terhadap keberadaan nilai pencilan (outlier) daripada Korelasi Pearson."
      },
      {
        "key": "E",
        "text": "Koefisien Gini Kemiskinan, yang mengukur ketimpangan distribusi pendapatan populasi dalam kurva Lorenz."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Koefisien Korelasi Spearman Rank ($r_s$), karena menghitung korelasi berdasarkan peringkat data (ranking) sehingga mampu menangkap hubungan monotonik non-linier dan lebih tangguh terhadap keberadaan nilai pencilan (outlier) daripada Korelasi Pearson.. Untuk hubungan monotonik non-linier dan data bertingkat, gunakan Korelasi Spearman Rank (berbasis peringkat data). Pilih: Koefisien Korelasi Spearman Rank (r_s)."
  },
  {
    "id": "inf-lat-h-25",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Etika Kecerdasan Buatan: Bias Algoritmik dan Explainable AI (XAI)",
    "hints": {
      "concept": "Diskriminasi otomatis akibat data pelatihan historis yang timpang disebut Algorithmic Bias. Solusinya dengan audit keadilan dataset dan Explainable AI (XAI).",
      "execution": "Pilih opsi yang menyebutkan Bias Algoritmik (Algorithmic Bias) dan solusi audit keadilan serta Explainable AI (XAI)."
    },
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah sistem kecerdasan buatan (Machine Learning) yang digunakan untuk menyaring calon penerima beasiswa universitas secara otomatis ditemukan menolak berkas lamaran dari pendaftar perempuan dan kelompok minoritas dengan probabilitas yang jauh lebih tinggi daripada kelompok mayoritas, meskipun memiliki kualifikasi akademik yang setara. Fenomena diskriminasi komputasi ini serta upaya solutifnya dalam etika AI adalah...",
    "formulaHud": {
      "title": "ETIKA DAN TATA KELOLA KECERDASAN BUATAN (AI ETHICS & FAIRNESS)",
      "latex": "\\text{Model ML Adil} \\implies \\text{Equalized Odds} \\land \\text{Demographic Parity} \\land \\text{Explainability (XAI)}",
      "legend": "• Sumber Bias Algoritmik: Sampling bias pada dataset historis, proxy variable tersembunyi, ketiadaan representasi minoritas<br>• Explainable AI (SHAP / LIME): Membuka kotak hitam (black-box) algoritma agar fitur penentu keputusan dapat dipertanggungjawabkan secara hukum dan etika"
    },
    "options": [
      {
        "key": "A",
        "text": "Overfitting Model Komputasi; diselesaikan dengan mematikan algoritma backpropagation jaringan saraf tiruan secara total diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Underfitting Data Latihan; diselesaikan dengan menghapus seluruh data kualifikasi akademik pendaftar dari model."
      },
      {
        "key": "C",
        "text": "Kegagalan Hardware GPU; diselesaikan dengan mengganti sirkuit grafis prosesor kecerdasan buatan dengan chip kuantum."
      },
      {
        "key": "D",
        "text": "Kejahatan Siber Phishing; diselesaikan dengan mengubah kata sandi masuk ke basis data universitas secara berkala."
      },
      {
        "key": "E",
        "text": "Bias Algoritmik (Algorithmic Bias), yang timbul akibat data historis pelatihan yang tidak representatif atau mengandung prasangka masa lalu manusia; solusinya memerlukan audit keadilan data (fairness metrics), penyeimbangan dataset, dan penerapan Explainable AI (XAI) untuk transparansi keputusan."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Bias Algoritmik (Algorithmic Bias), yang timbul akibat data historis pelatihan yang tidak representatif atau mengandung prasangka masa lalu manusia; solusinya memerlukan audit keadilan data (fairness metrics), penyeimbangan dataset, dan penerapan Explainable AI (XAI) untuk transparansi keputusan.. Diskriminasi otomatis akibat data pelatihan historis yang timpang disebut Algorithmic Bias. Solusinya dengan audit keadilan dataset dan Explainable AI (XAI). Pilih opsi yang menyebutkan Bias Algoritmik (Algorithmic Bias) dan solusi audit keadilan serta Explainable AI (XAI)."
  },
  {
    "id": "inf-sim-01",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Algoritma Lintasan Terpendek Seluruh Pasangan (Floyd-Warshall)",
    "hints": {
      "concept": "Floyd-Warshall mengevaluasi intermediate vertex k melalui 3 perulangan bersarang (for k, for i, for j), kompleksitasnya O(V^3).",
      "execution": "Pilih: O(|V|^3) kubik karena tiga lapis perulangan bersarang."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam mencari jarak terpendek antar semua pasangan simpul (All-Pairs Shortest Path) pada sebuah graf berarah dengan $|V| = 50$ simpul yang dapat memuat bobot negatif tanpa siklus negatif, pemrogram dapat menggunakan algoritma Floyd-Warshall berbasis pemrograman dinamis dengan matriks $D^{(k)}[i][j]$. Kompleksitas waktu asimtotik dari algoritma Floyd-Warshall tersebut adalah...",
    "formulaHud": {
      "title": "RELASI REKURENSI ALGORITMA FLOYD-WARSHALL",
      "latex": "D^{(k)}[i][j] = \\min\\Big(D^{(k-1)}[i][j], \\ D^{(k-1)}[i][k] + D^{(k-1)}[k][j]\\Big) \\implies \\text{Tiga Nested Loops: } O(|V|^3)",
      "legend": "• $k$: Simpul perantara yang diizinkan (dari himpunan $\\{1, 2, \\dots, k\\}$)<br>• Ruang Memori: $O(|V|^2)$ matriks jarak 2D<br>• Keunggulan: Sangat mudah diimplementasikan untuk graf padat (dense graph) dan mendukung bobot negatif"
    },
    "options": [
      {
        "key": "A",
        "text": "$O(|V|^3)$ kubik, karena algoritma mengeksekusi tiga lapis perulangan bersarang untuk mengevaluasi setiap kemungkinan simpul perantara $k$ dari $1$ hingga $|V|$."
      },
      {
        "key": "B",
        "text": "$O(|V|^2)$ kuadratik, karena hanya membutuhkan perbandingan langsung antar baris dan kolom matriks ketetanggaan sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "$O(|V| \\cdot |E| \\log |V|)$, setara dengan menjalankan algoritma Dijkstra sebanyak $|V|$ kali secara paralel."
      },
      {
        "key": "D",
        "text": "$O(|V|!)$, karena mencoba seluruh kemungkinan permutasi urutan simpul satu per satu."
      },
      {
        "key": "E",
        "text": "$O(|E| \\log |V|)$, setara dengan pencarian pohon rentang minimum pada graf berbobot tunggal."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) $O(|V|^3)$ kubik, karena algoritma mengeksekusi tiga lapis perulangan bersarang untuk mengevaluasi setiap kemungkinan simpul perantara $k$ dari $1$ hingga $|V|$.. Floyd-Warshall mengevaluasi intermediate vertex k melalui 3 perulangan bersarang (for k, for i, for j), kompleksitasnya O(V^3). Pilih: O(|V|^3) kubik karena tiga lapis perulangan bersarang."
  },
  {
    "id": "inf-sim-02",
    "materi": "SISTEM KOMPUTER",
    "topic": "Penentuan Safe Sequence pada Algoritma Banker",
    "hints": {
      "concept": "Available awal = 3. Hanya P1 (butuh 2) yang bisa jalan. Setelah P1 selesai, release 2, available jadi 5. Lalu P0 (butuh 5) atau P2 (butuh 4) bisa jalan.",
      "execution": "Pilih: <P1, P0, P2> atau <P1, P2, P0>."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Diberikan sebuah sistem komputasi dengan 3 proses ($P_0, P_1, P_2$) dan satu tipe sumber daya berjumlah 12 unit. Saat ini status alokasi dan kebutuhan maksimum adalah:\n- $P_0$: Alokasi = 4, Max = 9 $\\implies$ Butuh = 5\n- $P_1$: Alokasi = 2, Max = 4 $\\implies$ Butuh = 2\n- $P_2$: Alokasi = 3, Max = 7 $\\implies$ Butuh = 4\nTotal sumber daya teralokasi adalah $4 + 2 + 3 = 9$, sehingga sumber daya yang tersedia (Available) saat ini adalah $12 - 9 = 3$ unit. Urutan eksekusi aman (Safe Sequence) yang menjamin sistem terhindar dari deadlock adalah...",
    "formulaHud": {
      "title": "TRACING STATUS AMAN ALGORITMA BANKER",
      "latex": "\\begin{aligned} \\text{Awal Available} = 3 & \\implies \\text{Cek Need}: \\ P_0(5)>3, \\ \\mathbf{P_1(2) \\le 3}, \\ P_2(4)>3 \\implies \\text{Pilih } P_1 \\\\ \\text{Selesai } P_1 & \\implies \\text{Available Baru} = 3 + 2 = \\mathbf{5} \\implies P_0(5) \\le 5 \\text{ atau } P_2(4) \\le 5 \\\\ \\text{Jika Pilih } P_0 & \\implies \\text{Available Baru} = 5 + 4 = 9 \\implies P_2(4) \\le 9 \\implies \\text{Urutan: } \\langle P_1, P_0, P_2 \\rangle \\end{aligned}",
      "legend": "• Safe Sequence membuktikan sistem berada dalam Safe State<br>• Alokasi dikembalikan ke Available saat proses selesai mengeksekusi seluruh tugasnya"
    },
    "options": [
      {
        "key": "A",
        "text": "$\\langle P_0, P_1, P_2 \\rangle$, karena $P_0$ adalah proses dengan prioritas nomor indeks terendah sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "$\\langle P_1, P_0, P_2 \\rangle$ atau $\\langle P_1, P_2, P_0 \\rangle$, karena hanya $P_1$ yang kebutuhan sumber dayanya ($2$) dapat dipenuhi langsung oleh ketersediaan saat ini ($3$)."
      },
      {
        "key": "C",
        "text": "$\\langle P_2, P_1, P_0 \\rangle$, karena $P_2$ memiliki alokasi sumber daya awal paling seimbang."
      },
      {
        "key": "D",
        "text": "Tidak ada Safe Sequence yang valid sehingga sistem seketika mengalami deadlock permanen."
      },
      {
        "key": "E",
        "text": "$\\langle P_0, P_2, P_1 \\rangle$, karena seluruh proses dapat dieksekusi secara simultan tanpa antrean."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) $\\langle P_1, P_0, P_2 \\rangle$ atau $\\langle P_1, P_2, P_0 \\rangle$, karena hanya $P_1$ yang kebutuhan sumber dayanya ($2$) dapat dipenuhi langsung oleh ketersediaan saat ini ($3$).. Available awal = 3. Hanya P1 (butuh 2) yang bisa jalan. Setelah P1 selesai, release 2, available jadi 5. Lalu P0 (butuh 5) atau P2 (butuh 4) bisa jalan. Pilih: <P1, P0, P2> atau <P1, P2, P0>."
  },
  {
    "id": "inf-sim-03",
    "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
    "topic": "Mitigasi Serangan ARP Spoofing (Man-in-the-Middle) di Jaringan Lokal",
    "hints": {
      "concept": "Fitur switch untuk memvalidasi paket ARP dan mencegah ARP spoofing/poisoning adalah Dynamic ARP Inspection (DAI).",
      "execution": "Pilih: Dynamic ARP Inspection (DAI)."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam jaringan LAN sekolah, penyerang mengirimkan paket balasan ARP palsu (gratuitous ARP) secara berulang ke komputer korban dan gateway, mengklaim bahwa alamat IP default gateway diasosiasikan dengan MAC Address milik penyerang. Akibatnya, seluruh lalu lintas internet korban dibelokkan melalui komputer penyerang (Man-in-the-Middle). Mekanisme keamanan sakelar switch jaringan yang paling efektif untuk mencegah serangan ARP Spoofing ini adalah...",
    "formulaHud": {
      "title": "MEKANISME PERTAHANAN DYNAMIC ARP INSPECTION (DAI)",
      "latex": "\\text{Paket ARP} \\xrightarrow{\\text{Masuk Port Untrusted}} \\text{Switch Cek DAI} \\stackrel{?}{\\in} \\text{DHCP Snooping Binding Table} \\implies \\begin{cases} \\text{Cocok} & \\to \\text{Forward} \\\\ \\text{Palsu} & \\to \\text{Drop & Log Alert} \\end{cases}",
      "legend": "• Celah Keamanan Dasar ARP: Protokol ARP bersifat stateless dan tidak memiliki mekanisme otentikasi bawaan<br>• Prasyarat DAI: Fitur DHCP Snooping harus aktif terlebih dahulu untuk mencatat IP-MAC-Port yang sah"
    },
    "options": [
      {
        "key": "A",
        "text": "Mematikan fungsi penomoran IP dinamis dan membiarkan setiap komputer memilih alamat IP privat secara acak ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Memasang perangkat lunak antivirus pada komputer gateway tanpa mengonfigurasi perangkat keras sakelar switch."
      },
      {
        "key": "C",
        "text": "Dynamic ARP Inspection (DAI), yang bekerja memvalidasi setiap paket balasan ARP terhadap tabel ikatan tepercaya DHCP Snooping Binding Table dan menjatuhkan (drop) paket ARP yang memalsukan pemetaan IP-ke-MAC."
      },
      {
        "key": "D",
        "text": "Mengganti seluruh kabel jaringan tembaga dengan kabel nirkabel Wi-Fi tanpa kata sandi akses."
      },
      {
        "key": "E",
        "text": "Mengaktifkan protokol Spanning Tree Protocol (STP) untuk memblokir port jaringan yang memiliki nomor ganjil."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Dynamic ARP Inspection (DAI), yang bekerja memvalidasi setiap paket balasan ARP terhadap tabel ikatan tepercaya DHCP Snooping Binding Table dan menjatuhkan (drop) paket ARP yang memalsukan pemetaan IP-ke-MAC.. Fitur switch untuk memvalidasi paket ARP dan mencegah ARP spoofing/poisoning adalah Dynamic ARP Inspection (DAI). Pilih: Dynamic ARP Inspection (DAI)."
  },
  {
    "id": "inf-sim-04",
    "materi": "STRUKTUR DATA",
    "topic": "Efisiensi Struktur Data Pohon Awalan (Trie / Prefix Tree)",
    "hints": {
      "concept": "Trie unggul untuk autocomplete dan prefix query karena waktu pencariannya O(k) proporsional terhadap panjang kata k, bukan jumlah kata N.",
      "execution": "Pilih: Mampu mencari seluruh kata berawalan sama dalam O(k) independen dari total kata N."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah mesin pencari ingin mengimplementasikan fitur pelengkapan otomatis (autocomplete) dan pemeriksa ejaan (spell checker) untuk kamus berisi $N = 500.000$ kosakata kata bahasa Indonesia. Struktur data Trie (Prefix Tree) dipilih daripada Tabel Hash untuk kebutuhan fitur ini karena...",
    "formulaHud": {
      "title": "KOMPLEKSITAS OPERASI STRUKTUR DATA TRIE",
      "latex": "\\begin{aligned} \\text{Pencarian Kata / Awalan (Prefix Search):} & \\quad O(k), \\quad k = \\text{panjang kata (independen dari } N\\text{)} \\\\ \\text{Ruang Memori Simpul Alfabet } \\Sigma: & \\quad O(|\\Sigma| \\cdot k \\cdot N) \\end{aligned}",
      "legend": "• Struktur Simpul Trie: Setiap simpul memuat array pointer penunjuk anak berukuran alfabet (misal 26 huruf) dan flag boolean `isEndOfWord`<br>• Keunggulan vs Hash Table: Hash Table $O(1)$ untuk exact match, namun tidak mampu melakukan prefix query / autocomplete secara efisien"
    },
    "options": [
      {
        "key": "A",
        "text": "Trie memiliki waktu pencarian instan $O(1)$ untuk semua jenis kueri kemiripan semantik kecerdasan buatan menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Tabel Hash tidak mampu menyimpan data bertipe string teks alfabetik yang memiliki panjang lebih dari 5 huruf."
      },
      {
        "key": "C",
        "text": "Trie secara otomatis menerjemahkan kosakata asing ke dalam bahasa komputer biner tanpa kamus terjemahan."
      },
      {
        "key": "D",
        "text": "Trie mampu mencari seluruh kata yang memiliki awalan (prefix) yang sama dalam waktu $O(k)$ di mana $k$ adalah panjang string masukan, sepenuhnya independen dari total jumlah kata $N$ yang ada di kamus, serta menghemat memori untuk kata-kata dengan prefiks identik."
      },
      {
        "key": "E",
        "text": "Trie menjamin bahwa tidak ada tabrakan memori fisik karena menyimpan simpul langsung di sirkuit hard disk."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Trie mampu mencari seluruh kata yang memiliki awalan (prefix) yang sama dalam waktu $O(k)$ di mana $k$ adalah panjang string masukan, sepenuhnya independen dari total jumlah kata $N$ yang ada di kamus, serta menghemat memori untuk kata-kata dengan prefiks identik.. Trie unggul untuk autocomplete dan prefix query karena waktu pencariannya O(k) proporsional terhadap panjang kata k, bukan jumlah kata N. Pilih: Mampu mencari seluruh kata berawalan sama dalam O(k) independen dari total kata N."
  },
  {
    "id": "inf-sim-05",
    "materi": "ANALISIS DATA",
    "topic": "Tingkat Isolasi Transaksi Basis Data dan Anomali Phantom Read",
    "hints": {
      "concept": "Tingkat isolasi transaksi yang sepenuhnya mencegah Phantom Read adalah SERIALIZABLE.",
      "execution": "Pilih: SERIALIZABLE."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam sistem basis data perbankan yang mengimplementasikan prinsip ACID, dua transaksi konkuren dijalankan bersamaan. Transaksi A mengeksekusi kueri `SELECT COUNT(*) FROM Rekening WHERE saldo > 100000000;`. Sesaat kemudian, Transaksi B melakukan `INSERT` baris nasabah baru dengan saldo Rp 150.000.000,- dan melakukan `COMMIT`. Ketika Transaksi A menjalankan kembali kueri hitung yang sama dalam sesi yang sama, jumlah baris bertambah satu. Tingkat isolasi transaksi tertinggi yang mutlak dibutuhkan untuk mencegah fenomena Phantom Read tersebut adalah...",
    "formulaHud": {
      "title": "TINGKAT ISOLASI TRANSAKSI SQL (ANSI/ISO SQL-92)",
      "latex": "\\begin{array}{|l|c|c|c|} \\hline \\text{Tingkat Isolasi} & \\text{Dirty Read} & \\text{Non-repeatable} & \\text{Phantom Read} \\\\ \\hline \\text{Read Uncommitted} & \\text{Bisa} & \\text{Bisa} & \\text{Bisa} \\\\ \\text{Read Committed} & \\text{Aman} & \\text{Bisa} & \\text{Bisa} \\\\ \\text{Repeatable Read} & \\text{Aman} & \\text{Aman} & \\text{Bisa (Standar SQL)} \\\\ \\mathbf{\\text{Serializable}} & \\mathbf{\\text{Aman}} & \\mathbf{\\text{Aman}} & \\mathbf{\\text{Aman}} \\\\ \\hline \\end{array}",
      "legend": "• Phantom Read: Baris baru muncul di pembacaan kedua dalam transaksi yang sama akibat INSERT konkuren yang telah committed<br>• Serializable: Menjamin eksekusi transaksi konkuren menghasilkan efek yang sama dengan eksekusi serial satu per satu"
    },
    "options": [
      {
        "key": "A",
        "text": "`READ COMMITTED`, yang hanya mencegah pembacaan data kotor (Dirty Read) dari transaksi yang belum committed diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "`REPEATABLE READ`, yang hanya menjamin nilai baris yang telah dibaca tidak berubah, namun masih mengizinkan penyisipan baris baru."
      },
      {
        "key": "C",
        "text": "`READ UNCOMMITTED`, yang mengizinkan seluruh transaksi membaca perubahan data yang belum disimpan."
      },
      {
        "key": "D",
        "text": "`SNAPSHOT ISOLATION`, yang menghapus seluruh data transaksi nasabah lama secara otomatis."
      },
      {
        "key": "E",
        "text": "`SERIALIZABLE`, yang mengunci rentang baris (Range Locks / Predicate Locking) sehingga transaksi konkuren tidak dapat menyisipkan baris baru yang memenuhi kriteria filter transaksi pertama."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) `SERIALIZABLE`, yang mengunci rentang baris (Range Locks / Predicate Locking) sehingga transaksi konkuren tidak dapat menyisipkan baris baru yang memenuhi kriteria filter transaksi pertama.. Tingkat isolasi transaksi yang sepenuhnya mencegah Phantom Read adalah SERIALIZABLE. Pilih: SERIALIZABLE."
  },
  {
    "id": "inf-sim-06",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Penelusuran Algoritma Longest Common Subsequence (LCS)",
    "hints": {
      "concept": "Karakter yang muncul berurutan di keduanya: A (indeks 0 di keduanya), C (indeks 1 di S1, indeks 2 di S2), G (indeks 3 di S1, indeks 4 di S2) -> 'ACG' (panjang 3).",
      "execution": "Pilih: Panjang 3, dengan sekuens \"ACG\" atau \"ACT\"."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Diberikan dua rantai sekuens DNA: $S_1 = \\text{\"ACCGT\"}$ dan $S_2 = \\text{\"AGCTG\"}$. Panjang dari Sekuens Bagian Terpanjang yang Sama (Longest Common Subsequence / LCS) antara kedua rantai tersebut serta salah satu bentuk sekuensnya adalah...",
    "formulaHud": {
      "title": "MATRIKS PEMROGRAMAN DINAMIS LCS",
      "latex": "LCS[i][j] = \\begin{cases} 0 & \\text{jika } i=0 \\lor j=0 \\\\ LCS[i-1][j-1] + 1 & \\text{jika } S_1[i-1] == S_2[j-1] \\\\ \\max(LCS[i-1][j], \\ LCS[i][j-1]) & \\text{jika } S_1[i-1] \\ne S_2[j-1] \\end{cases}",
      "legend": "• S1 = A - C - C - G - T (panjang 5)<br>• S2 = A - G - C - T - G (panjang 5)<br>• Subsequence yang sama berurutan: A -> C -> G (panjang 3) atau A -> C -> T (panjang 3)<br>• Nilai maksimum LCS = 3"
    },
    "options": [
      {
        "key": "A",
        "text": "Panjang 3, dengan sekuens $\\text{\"ACG\"}$ atau $\\text{\"ACT\"}$."
      },
      {
        "key": "B",
        "text": "Panjang 5, dengan sekuens $\\text{\"ACCGT\"}$ sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Panjang 4, dengan sekuens $\\text{\"ACGT\"}$."
      },
      {
        "key": "D",
        "text": "Panjang 2, dengan sekuens $\\text{\"AG\"}$."
      },
      {
        "key": "E",
        "text": "Panjang 1, dengan sekuens $\\text{\"A\"}$ saja."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Panjang 3, dengan sekuens $\\text{\"ACG\"}$ atau $\\text{\"ACT\"}$.. Karakter yang muncul berurutan di keduanya: A (indeks 0 di keduanya), C (indeks 1 di S1, indeks 2 di S2), G (indeks 3 di S1, indeks 4 di S2) -> 'ACG' (panjang 3). Pilih: Panjang 3, dengan sekuens \"ACG\" atau \"ACT\"."
  },
  {
    "id": "inf-sim-07",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Arsitektur Perutean Global Internet Protokol BGP (Border Gateway Protocol)",
    "hints": {
      "concept": "BGP disebut path-vector karena mengiklankan rute beserta lintasan nomor AS (AS-Path) untuk mendeteksi loop perutean internet global.",
      "execution": "Pilih opsi yang menyebutkan penyertaan daftar nomor AS (AS-Path) untuk kebijakan rute dan pencegahan loop."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Jaringan internet global terdiri atas ribuan Autonomous System (AS) yang saling terhubung dan bertukar informasi rute jaringan menggunakan protokol Border Gateway Protocol (BGP-4). Alasan mengapa BGP diklasifikasikan sebagai protokol Path-Vector (bukan Distance-Vector atau Link-State murni) adalah...",
    "formulaHud": {
      "title": "PENCEGAHAN LOOP PADA PROTOKOL BGP PATH-VECTOR",
      "latex": "\\text{Router AS } X \\text{ terima rute dengan } \\text{AS-Path: } [A, B, C] \\implies \\begin{cases} \\text{Jika } X \\in [A, B, C] & \\to \\text{DROP (Terdeteksi Routing Loop!)} \\\\ \\text{Jika } X \\notin [A, B, C] & \\to \\text{Terima & Tambahkan } X \\text{ ke AS-Path} \\end{cases}",
      "legend": "• AS (Autonomous System): Kumpulan jaringan di bawah satu administrasi teknis (memiliki ASN unik)<br>• BGP Policy Routing: Pemilihan rute tidak hanya berdasarkan performa teknis tetapi kebijakan bisnis/peering"
    },
    "options": [
      {
        "key": "A",
        "text": "BGP mengukur kualitas rute internet secara eksklusif berdasarkan jumlah sakelar switch lokal yang dilewati paket data sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "BGP menyertakan daftar lengkap nomor urutan Autonomous System (atribut AS-Path) yang dilalui oleh sebuah rute iklan ke jaringan tujuan, yang digunakan router untuk menentukan rute kebijakan terbaik dan mendeteksi serta mencegah terbentuknya loop perutean antar AS secara mutlak."
      },
      {
        "key": "C",
        "text": "BGP menyiarkan seluruh isi memori kernel router menggunakan gelombang mikro satelit setiap 5 milidetik."
      },
      {
        "key": "D",
        "text": "BGP hanya dapat menghubungkan dua komputer yang berada di dalam satu ruangan gedung yang sama."
      },
      {
        "key": "E",
        "text": "BGP secara otomatis memblokir seluruh koneksi internet yang menggunakan protokol TCP lapisan keempat."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) BGP menyertakan daftar lengkap nomor urutan Autonomous System (atribut AS-Path) yang dilalui oleh sebuah rute iklan ke jaringan tujuan, yang digunakan router untuk menentukan rute kebijakan terbaik dan mendeteksi serta mencegah terbentuknya loop perutean antar AS secara mutlak.. BGP disebut path-vector karena mengiklankan rute beserta lintasan nomor AS (AS-Path) untuk mendeteksi loop perutean internet global. Pilih opsi yang menyebutkan penyertaan daftar nomor AS (AS-Path) untuk kebijakan rute dan pencegahan loop."
  },
  {
    "id": "inf-sim-08",
    "materi": "SISTEM KOMPUTER",
    "topic": "Anomali Belady pada Algoritma Penggantian Halaman FIFO",
    "hints": {
      "concept": "Penambahan frame justru menaikkan page fault pada algoritma FIFO disebut Anomali Belady (Belady's Anomaly).",
      "execution": "Pilih: Anomali Belady (Belady's Anomaly)."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam evaluasi algoritma penggantian halaman memori virtual (Page Replacement), penambahan jumlah bingkai memori fisik (page frame) secara teoritis diharapkan dapat menurunkan atau minimal mempertahankan jumlah terjadinya page fault. Namun, pada algoritma First-In, First-Out (FIFO), penambahan frame memori fisik dari 3 frame menjadi 4 frame justru dapat menyebabkan jumlah page fault meningkat. Fenomena paradoksikal ini dikenal sebagai...",
    "formulaHud": {
      "title": "ANOMALI BELADY PADA PENGGANTIAN HALAMAN FIFO",
      "latex": "\\text{String Referensi: } 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 \\implies \\begin{cases} 3 \\text{ Frame:} & 9 \\text{ Page Faults} \\\\ 4 \\text{ Frame:} & \\mathbf{10} \\text{ Page Faults (Meningkat!)} \\end{cases}",
      "legend": "• Stack Algorithm: Algoritma di mana $H(m, t) \\subseteq H(m+1, t)$ untuk setiap saat $t$<br>• LRU (Least Recently Used) dan OPT (Belady's Optimal) adalah Stack Algorithm sehingga KEBAL terhadap Anomali Belady"
    },
    "options": [
      {
        "key": "A",
        "text": "Anomali Amdahl, yaitu perlambatan akselerasi pemrosesan paralel saat inti prosesor ditambahkan secara fisik ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Konflik Peterson, yaitu kegagalan algoritma sinkronisasi dua proses dalam menjamin mutual exclusion."
      },
      {
        "key": "C",
        "text": "Anomali Belady (Belady's Anomaly), yang terjadi karena algoritma FIFO tidak memiliki properti Stack Algorithm (seperti halnya LRU atau Optimal) di mana himpunan halaman pada $m$ frame belum tentu merupakan subset dari himpunan halaman pada $m+1$ frame."
      },
      {
        "key": "D",
        "text": "Thrashing Sinkron, yaitu kondisi di mana seluruh disk SSD komputer terbakar akibat frekuensi I/O tinggi."
      },
      {
        "key": "E",
        "text": "Deadlock Dine-In, yaitu kebuntuan filosofis sistem akibat kekurangan garpu pemrosesan data."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Anomali Belady (Belady's Anomaly), yang terjadi karena algoritma FIFO tidak memiliki properti Stack Algorithm (seperti halnya LRU atau Optimal) di mana himpunan halaman pada $m$ frame belum tentu merupakan subset dari himpunan halaman pada $m+1$ frame.. Penambahan frame justru menaikkan page fault pada algoritma FIFO disebut Anomali Belady (Belady's Anomaly). Pilih: Anomali Belady (Belady's Anomaly)."
  },
  {
    "id": "inf-sim-09",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Kompleksitas Masalah NP-Hard: Travelling Salesperson Problem (TSP)",
    "hints": {
      "concept": "Untuk masalah NP-Hard berukuran besar seperti TSP, gunakan algoritma heuristik/metaheuristik (Algoritma Genetika, Simulated Annealing) untuk menemukan solusi mendekati optimal secara cepat.",
      "execution": "Pilih opsi: Menggunakan Algoritma Heuristik atau Metaheuristik."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Masalah Travelling Salesperson Problem (TSP) menuntut seorang kurir untuk mengunjungi $N$ buah kota tepat satu kali dan kembali ke kota awal dengan total jarak tempuh minimum. Untuk $N = 30$ kota, pendekatan brute-force memeriksa seluruh $(N-1)! / 2$ permutasi rute membutuhkan waktu miliaran tahun komputasi. Strategi komputasional yang paling realistis dan efektif digunakan dalam industri logistik modern untuk menyelesaikan masalah NP-Hard ini adalah...",
    "formulaHud": {
      "title": "KOMPLEKSITAS KOMBINATORIAL MASALAH TSP",
      "latex": "\\text{Total Rute Brute-Force} = \\frac{(N - 1)!}{2}, \\quad \\text{Untuk } N = 30 \\implies \\approx 4,42 \\times 10^{30} \\text{ rute (Intractable)}",
      "legend": "• Kategori Masalah: NP-Hard (Optimasi) / NP-Complete (Keputusan)<br>• Heuristik: Mengorbankan jaminan optimalitas mutlak demi efisiensi waktu pemrosesan yang realistis dalam hitungan detik"
    },
    "options": [
      {
        "key": "A",
        "text": "Menunggu terciptanya komputer kuantum komersial karena komputer digital mustahil menyelesaikan masalah kombinatorial menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Mengurangi jumlah kota menjadi 2 kota saja dan membatalkan pesanan pengiriman logistik pada kota-kota lainnya."
      },
      {
        "key": "C",
        "text": "Menjalankan algoritma Binary Search pada koordinat garis bujur kota untuk menemukan rute linier langsung."
      },
      {
        "key": "D",
        "text": "Menggunakan Algoritma Heuristik atau Metaheuristik (seperti Algoritma Genetika, Simulated Annealing, atau Ant Colony Optimization) yang mampu menemukan solusi rute yang mendekati optimal (near-optimal) dalam waktu komputasi yang sangat cepat dan wajar."
      },
      {
        "key": "E",
        "text": "Menggunakan algoritma Bubble Sort untuk mengurutkan jarak kota berdasarkan kode pos administrasi daerah."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Menggunakan Algoritma Heuristik atau Metaheuristik (seperti Algoritma Genetika, Simulated Annealing, atau Ant Colony Optimization) yang mampu menemukan solusi rute yang mendekati optimal (near-optimal) dalam waktu komputasi yang sangat cepat dan wajar.. Untuk masalah NP-Hard berukuran besar seperti TSP, gunakan algoritma heuristik/metaheuristik (Algoritma Genetika, Simulated Annealing) untuk menemukan solusi mendekati optimal secara cepat. Pilih opsi: Menggunakan Algoritma Heuristik atau Metaheuristik."
  },
  {
    "id": "inf-sim-10",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Mekanisme dan Analisis Ruang In-Place Algoritma Heapsort",
    "hints": {
      "concept": "Keunggulan utama Heapsort atas Merge Sort: Heapsort adalah in-place sorting dengan memori tambahan O(1), sedangkan Merge Sort butuh memori tambahan O(n).",
      "execution": "Pilih: Heapsort bekerja in-place dengan memori tambahan O(1) konstan, sedangkan Merge Sort butuh O(n)."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Algoritma pengurutan Heapsort membangun struktur data Max-Heap di dalam larik masukan itu sendiri, lalu menukar elemen maksimum (akar) dengan elemen terakhir larik secara berulang sambil memulihkan sifat heap. Keunggulan teknis utama dari Heapsort dibandingkan dengan Merge Sort adalah...",
    "formulaHud": {
      "title": "KOMPARASI ALGORITMA HEAPSORT VS MERGE SORT",
      "latex": "\\begin{array}{|l|c|c|c|} \\hline \\text{Algoritma} & \\text{Waktu (Worst)} & \\text{Ruang Memori (Auxiliary)} & \\text{Stabilitas} \\\\ \\hline \\text{Merge Sort} & O(n \\log n) & O(n) & \\text{Stabil} \\\\ \\mathbf{\\text{Heapsort}} & \\mathbf{O(n \\log n)} & \\mathbf{O(1) \\ (\\text{In-Place})} & \\text{Tidak Stabil} \\\\ \\hline \\end{array}",
      "legend": "• Build Max-Heap (Floyd's Algorithm): Membutuhkan waktu $O(n)$<br>• $n-1$ kali Extract-Max: Membutuhkan waktu $(n - 1) \\times O(\\log n) = O(n \\log n)$<br>• Total Waktu: $O(n \\log n)$ di semua kondisi"
    },
    "options": [
      {
        "key": "A",
        "text": "Heapsort memiliki kompleksitas waktu asimtotik terbaik sebesar $O(1)$ instan pada larik yang belum terurut diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Heapsort bersifat stabil (stable sort) sehingga posisi relatif elemen bernilai kembar selalu terjamin tidak berubah."
      },
      {
        "key": "C",
        "text": "Heapsort tidak memerlukan operasi perbandingan antar elemen data sama sekali selama proses pengurutan berlangsung."
      },
      {
        "key": "D",
        "text": "Heapsort secara otomatis mengubah prosesor komputer menjadi sistem paralel multi-threading tanpa sistem operasi."
      },
      {
        "key": "E",
        "text": "Heapsort bekerja secara in-place dengan kompleksitas ruang memori tambahan sebesar $O(1)$ konstan, sedangkan Merge Sort membutuhkan alokasi memori larik tambahan sebesar $O(n)$ untuk proses penggabungan (merge)."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Heapsort bekerja secara in-place dengan kompleksitas ruang memori tambahan sebesar $O(1)$ konstan, sedangkan Merge Sort membutuhkan alokasi memori larik tambahan sebesar $O(n)$ untuk proses penggabungan (merge).. Keunggulan utama Heapsort atas Merge Sort: Heapsort adalah in-place sorting dengan memori tambahan O(1), sedangkan Merge Sort butuh memori tambahan O(n). Pilih: Heapsort bekerja in-place dengan memori tambahan O(1) konstan, sedangkan Merge Sort butuh O(n)."
  },
  {
    "id": "inf-sim-11",
    "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
    "topic": "Komunikasi Real-Time Web: Protokol WebSockets vs HTTP Polling",
    "hints": {
      "concept": "WebSockets membuat koneksi TCP full-duplex persisten dengan overhead header frame sangat kecil (2-10 byte) dan mendukung server-push.",
      "execution": "Pilih opsi yang menjelaskan koneksi TCP persisten full-duplex dengan overhead header sangat kecil (2-10 byte)."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Aplikasi dasbor pemantauan sensor lalu lintas perkotaan memerlukan pembaruan data telemetri puluhan kali per detik dengan latensi sekecil mungkin. Arsitektur komunikasi berbasis WebSockets (RFC 6455) jauh lebih unggul dibandingkan HTTP Short/Long Polling untuk kebutuhan ini karena...",
    "formulaHud": {
      "title": "KOMPARASI OVERHEAD PROTOKOL REAL-TIME WEB",
      "latex": "\\begin{aligned} \\text{HTTP Polling:} & \\quad \\text{Koneksi Baru / Request Berulang} \\implies \\text{Header Overhead: } \\approx 500 - 1000 \\text{ Bytes/Request} \\\\ \\text{WebSockets:} & \\quad \\text{1x Handshake (TCP Persisten)} \\implies \\text{Header Overhead: } \\mathbf{2 - 10 \\text{ Bytes/Frame (Full-Duplex)}} \\end{aligned}",
      "legend": "• Full-Duplex: Klien dan server dapat mengirimkan data secara simultan bersamaan<br>• Server-Push: Server dapat mengirimkan data secara spontan tanpa menunggu permintaan (request) klien"
    },
    "options": [
      {
        "key": "A",
        "text": "WebSockets membangun satu koneksi TCP persisten dua arah (full-duplex) tunggal setelah jabat tangan HTTP awal, sehingga pesan data dapat dikirimkan secara instan oleh server ke klien (server-push) hanya dengan overhead header frame sebesar 2 hingga 10 byte tanpa overhead header HTTP berulang."
      },
      {
        "key": "B",
        "text": "HTTP Polling secara otomatis mengompresi data menjadi sinyal inframerah yang kebal terhadap hambatan jarak sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "WebSockets tidak menggunakan jaringan internet sama sekali melainkan frekuensi radio gelombang pendek FM lokal."
      },
      {
        "key": "D",
        "text": "HTTP Short Polling selalu menjamin nol persen pemborosan bandwidth meskipun tidak ada pembaruan data dari sensor."
      },
      {
        "key": "E",
        "text": "WebSockets mewajibkan pengguna untuk melakukan penyegaran halaman peramban (F5) setiap kali data baru masuk."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) WebSockets membangun satu koneksi TCP persisten dua arah (full-duplex) tunggal setelah jabat tangan HTTP awal, sehingga pesan data dapat dikirimkan secara instan oleh server ke klien (server-push) hanya dengan overhead header frame sebesar 2 hingga 10 byte tanpa overhead header HTTP berulang.. WebSockets membuat koneksi TCP full-duplex persisten dengan overhead header frame sangat kecil (2-10 byte) dan mendukung server-push. Pilih opsi yang menjelaskan koneksi TCP persisten full-duplex dengan overhead header sangat kecil (2-10 byte)."
  },
  {
    "id": "inf-sim-12",
    "materi": "ANALISIS DATA",
    "topic": "Pemodelan Dimensi Data Warehouse: Skema Bintang (Star Schema)",
    "hints": {
      "concept": "Star Schema terdiri dari satu Fact Table di tengah yang dikelilingi oleh Dimension Tables terdenormalisasi.",
      "execution": "Pilih: Satu Tabel Fakta di tengah dikelilingi oleh Tabel Dimensi terdenormalisasi."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam perancangan basis data analitis Data Warehouse (OLAP), Skema Bintang (Star Schema) sering digunakan untuk mempercepat kueri pelaporan agregat bisnis. Struktur arsitektural yang mendefinisikan Skema Bintang adalah...",
    "formulaHud": {
      "title": "ARSITEKTUR SKEMA BINTANG (STAR SCHEMA)",
      "latex": "\\text{Fact Table (Pusat)} \\longleftrightarrow \\begin{cases} \\text{Dim\\_Waktu} \\\\ \\text{Dim\\_Produk} \\\\ \\text{Dim\\_Cabang} \\\\ \\text{Dim\\_Pelanggan} \\end{cases} \\implies \\text{Denormalized Dimensions (Fast OLAP Queries)}",
      "legend": "• Fact Table: Menyimpan metrik (kuantitas terjual, total omzet) dan foreign keys<br>• Dimension Table: Menyimpan atribut konteks analisis (nama hari, kategori produk, wilayah)<br>• Keunggulan vs Snowflake: Kueri analitis membutuhkan lebih sedikit operasi JOIN"
    },
    "options": [
      {
        "key": "A",
        "text": "Terdiri atas tabel-tabel data yang dinormalisasi penuh hingga 3NF dengan rantai relasi bertingkat menyerupai struktur kepingan salju sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Terdiri atas satu Tabel Fakta (Fact Table) terpusat yang memuat kunci-kunci asing dan metrik pengukuran numerik kuantitatif bisnis, yang dikelilingi oleh sekumpulan Tabel Dimensi (Dimension Tables) yang terdenormalisasi secara langsung tanpa hierarki bertingkat."
      },
      {
        "key": "C",
        "text": "Hanya memuat satu tabel tunggal raksasa tanpa adanya hubungan relasi kunci primer dan kunci asing sama sekali."
      },
      {
        "key": "D",
        "text": "Tabel-tabel dimensi yang saling terhubung membentuk graf siklis tanpa adanya tabel penampung data numerik."
      },
      {
        "key": "E",
        "text": "Tabel data yang disimpan dalam berkas teks terenkripsi di mana setiap baris mewakili konfigurasi perangkat keras server."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Terdiri atas satu Tabel Fakta (Fact Table) terpusat yang memuat kunci-kunci asing dan metrik pengukuran numerik kuantitatif bisnis, yang dikelilingi oleh sekumpulan Tabel Dimensi (Dimension Tables) yang terdenormalisasi secara langsung tanpa hierarki bertingkat.. Star Schema terdiri dari satu Fact Table di tengah yang dikelilingi oleh Dimension Tables terdenormalisasi. Pilih: Satu Tabel Fakta di tengah dikelilingi oleh Tabel Dimensi terdenormalisasi."
  },
  {
    "id": "inf-sim-13",
    "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
    "topic": "Remediasi Kerentanan Injeksi SQL Menggunakan Prepared Statements",
    "hints": {
      "concept": "Pencegahan utama SQL Injection adalah Parameterized Queries / Prepared Statements yang memisahkan instruksi SQL dari data literal.",
      "execution": "Pilih: Menggunakan Kueri Berparameter (Parameterized Queries / Prepared Statements)."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi web otentikasi login memiliki celah keamanan SQL Injection pada baris kode PHP naif berikut:\n```php\n$query = \"SELECT * FROM users WHERE user = '\" . $_POST['username'] . \"' AND pass = '\" . $_POST['password'] . \"'\";\n```\nSeorang penyerang memasukkan nilai `' OR '1'='1` ke dalam kolom username sehingga berhasil masuk tanpa kata sandi. Teknik remediasi standar industri yang paling tepat dan mutlak mampu mencegah serangan SQL Injection tersebut adalah...",
    "formulaHud": {
      "title": "REMEDIASI PREPARED STATEMENTS PADA SQL INJECTION",
      "latex": "\\text{Kueri SQL:} \\quad \\text{SELECT * FROM users WHERE user = ? AND pass = ?} \\implies \\text{Input di-bind sebagai Data Murni, Bukan Kode!}",
      "legend": "• Sanitasi String: Penggunaan fungsi escape (addslashes) masih rentan terhadap encoding bypass<br>• Prepared Statements: Solusi mutlak karena kompilasi struktur perintah SQL dilakukan SEBELUM parameter data diinjeksikan"
    },
    "options": [
      {
        "key": "A",
        "text": "Menghapus seluruh kata kunci `SELECT` dari aplikasi web dan menggantinya dengan berkas spreadsheet ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Mengubah metode permintaan formulir HTML dari `POST` menjadi `GET` pada peramban pengguna."
      },
      {
        "key": "C",
        "text": "Menggunakan Kueri Berparameter (Parameterized Queries / Prepared Statements), di mana mesin basis data memisahkan secara tegas antara struktur logika kueri SQL dan nilai data masukan pengguna, sehingga masukan berbahaya hanya diperlakukan sebagai literal teks murni dan bukan kode eksekusi."
      },
      {
        "key": "D",
        "text": "Mematikan fungsi logging server basis data agar aktivitas peretas tidak tercatat di memori hard disk."
      },
      {
        "key": "E",
        "text": "Mengganti seluruh kata sandi pengguna menjadi kombinasi huruf kapital tanpa melibatkan angka numerik."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Menggunakan Kueri Berparameter (Parameterized Queries / Prepared Statements), di mana mesin basis data memisahkan secara tegas antara struktur logika kueri SQL dan nilai data masukan pengguna, sehingga masukan berbahaya hanya diperlakukan sebagai literal teks murni dan bukan kode eksekusi.. Pencegahan utama SQL Injection adalah Parameterized Queries / Prepared Statements yang memisahkan instruksi SQL dari data literal. Pilih: Menggunakan Kueri Berparameter (Parameterized Queries / Prepared Statements)."
  },
  {
    "id": "inf-sim-14",
    "materi": "SISTEM KOMPUTER",
    "topic": "Sinkronisasi Utas: Kondisi Balapan (Race Condition) dan Mutex Lock",
    "hints": {
      "concept": "Masalah dua thread memanipulasi data bersamaan tanpa sinkronisasi disebut Race Condition. Solusinya dengan Mutex Lock pada Critical Section.",
      "execution": "Pilih: Kondisi Balapan (Race Condition); diselesaikan menggunakan Mutual Exclusion / Mutex Lock."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dua utas (threads) yang berjalan secara konkuren mencoba menambah nilai variabel bersama `counter` yang awalnya bernilai 100 secara bersamaan melalui instruksi:\n```c\ncounter = counter + 1;\n```\nPada level bahasa mesin prosesor, instruksi ini dieksekusi menjadi 3 tahapan: (1) `LOAD R, [counter]`; (2) `ADD R, 1`; (3) `STORE [counter], R`. Jika terjadi peralihan konteks tepat di antara langkah 1 dan 3, nilai akhir `counter` dapat menjadi 101 alih-alih 102. Masalah konkuren ini serta mekanisme penguncian yang tepat untuk menyelesaikannya adalah...",
    "formulaHud": {
      "title": "SINKRONISASI CRITICAL SECTION DENGAN MUTEX LOCK",
      "latex": "\\text{Acquire(Mutex)} \\to \\mathbf{\\text{Critical Section: } \\text{counter} = \\text{counter} + 1} \\to \\text{Release(Mutex)}",
      "legend": "• Race Condition: Hasil akhir komputasi bergantung pada urutan eksekusi timing non-deterministik antar utas konkuren<br>• Mutex Lock: Menjamin hanya satu utas yang dapat mengakses bagian kritis pada satu satuan waktu"
    },
    "options": [
      {
        "key": "A",
        "text": "Fragmentasi Memori; diselesaikan dengan melakukan defragmentasi piringan hard disk secara terjadwal menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Paging Fault; diselesaikan dengan mematikan memori virtual pada pengaturan BIOS motherboard."
      },
      {
        "key": "C",
        "text": "Buffer Overflow; diselesaikan dengan memperbesar ukuran register Program Counter CPU."
      },
      {
        "key": "D",
        "text": "Kondisi Balapan (Race Condition); diselesaikan dengan melindungi blok instruksi tersebut sebagai Bagian Kritis (Critical Section) menggunakan mekanisme penguncian saling mengeluarkan (Mutual Exclusion / Mutex Lock)."
      },
      {
        "key": "E",
        "text": "Deadlock Melingkar; diselesaikan dengan menghentikan secara paksa proses sistem operasi induk."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Kondisi Balapan (Race Condition); diselesaikan dengan melindungi blok instruksi tersebut sebagai Bagian Kritis (Critical Section) menggunakan mekanisme penguncian saling mengeluarkan (Mutual Exclusion / Mutex Lock).. Masalah dua thread memanipulasi data bersamaan tanpa sinkronisasi disebut Race Condition. Solusinya dengan Mutex Lock pada Critical Section. Pilih: Kondisi Balapan (Race Condition); diselesaikan menggunakan Mutual Exclusion / Mutex Lock."
  },
  {
    "id": "inf-sim-15",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Penelusuran Antrean pada Algoritma Breadth-First Search (BFS)",
    "hints": {
      "concept": "Tingkat 0: A. Tingkat 1: B, C. Dari B dimasukkan D, E. Dari C dimasukkan F. Maka urutan BFS adalah A, B, C, D, E, F.",
      "execution": "Pilih: A -> B -> C -> D -> E -> F."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Diberikan sebuah graf tak berarah dengan daftar ketetanggaan:\n- $A: [B, C]$\n- $B: [A, D, E]$\n- $C: [A, F]$\n- $D: [B]$\n- $E: [B, F]$\n- $F: [C, E]$\nJika penelusuran Breadth-First Search (BFS) dimulai dari simpul $A$ dan tetangga yang belum dikunjungi dimasukkan ke antrean (Queue) sesuai urutan abjad alfabet, urutan simpul saat dikeluarkan (visited) dari antrean secara lengkap adalah...",
    "formulaHud": {
      "title": "TRACING ANTREAN QUEUE ALGORITMA BFS",
      "latex": "\\begin{aligned} \\text{Awal:} & \\quad Q = [A] \\implies \\text{Visit } A, \\text{ Enqueue tetangga } (B, C) \\implies Q = [B, C] \\\\ \\text{Langkah 1:} & \\quad \\text{Visit } B, \\text{ Enqueue tetangga baru } (D, E) \\implies Q = [C, D, E] \\\\ \\text{Langkah 2:} & \\quad \\text{Visit } C, \\text{ Enqueue tetangga baru } (F) \\implies Q = [D, E, F] \\\\ \\text{Langkah 3-5:} & \\quad \\text{Visit } D, E, F \\implies \\text{Urutan: } A \\to B \\to C \\to D \\to E \\to F \\end{aligned}",
      "legend": "• Struktur Data: Queue (FIFO)<br>• Tingkat 0: {A}<br>• Tingkat 1: {B, C}<br>• Tingkat 2: {D, E, F}"
    },
    "options": [
      {
        "key": "A",
        "text": "$A \\rightarrow B \\rightarrow D \\rightarrow E \\rightarrow F \\rightarrow C$ diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "$A \\rightarrow C \\rightarrow F \\rightarrow E \\rightarrow B \\rightarrow D$"
      },
      {
        "key": "C",
        "text": "$A \\rightarrow B \\rightarrow C \\rightarrow F \\rightarrow E \\rightarrow D$"
      },
      {
        "key": "D",
        "text": "$A \\rightarrow D \\rightarrow E \\rightarrow B \\rightarrow C \\rightarrow F$"
      },
      {
        "key": "E",
        "text": "$A \\rightarrow B \\rightarrow C \\rightarrow D \\rightarrow E \\rightarrow F$"
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $A \\rightarrow B \\rightarrow C \\rightarrow D \\rightarrow E \\rightarrow F$. Tingkat 0: A. Tingkat 1: B, C. Dari B dimasukkan D, E. Dari C dimasukkan F. Maka urutan BFS adalah A, B, C, D, E, F. Pilih: A -> B -> C -> D -> E -> F."
  },
  {
    "id": "inf-sim-16",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Taktik Pemerasan Ganda (Double Extortion) pada Serangan Ransomware",
    "hints": {
      "concept": "Double Extortion memeras dua kali: mengenkripsi sistem DAN mengancam menyebarkan data curian ke publik jika tebusan tak dibayar.",
      "execution": "Pilih opsi: Mencuri data sensitif sebelum enkripsi, lalu mengancam mempublikasikannya ke dark web jika tebusan ditolak."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam evolusi ancaman siber terkini, kelompok kriminal ransomware modern tidak hanya mengenkripsi basis data korban untuk meminta tebusan uang dekripsi, tetapi juga menerapkan taktik \"Double Extortion\". Mekanisme operasional dari taktik pemerasan ganda ini adalah...",
    "formulaHud": {
      "title": "ANATOMI TREN RANSOMWARE DOUBLE EXTORTION",
      "latex": "\\text{Tahap 1: Eksfiltrasi Data Rahasia} \\to \\text{Tahap 2: Enkripsi Sistem} \\to \\text{Tahap 3: Pemerasan Tebusan Ganda (Kunci + Non-Bocor)}",
      "legend": "• Kegagalan Backup Konvensional: Backup hanya memulihkan ketersediaan (Availability), tetapi gagal melindungi kerahasiaan (Confidentiality) dari ancaman bocornya data<br>• Mitigasi: Enkripsi data at-rest & in-transit, Data Loss Prevention (DLP), dan segmentasi jaringan ketat"
    },
    "options": [
      {
        "key": "A",
        "text": "Sebelum mengenkripsi sistem korban, penyerang terlebih dahulu mencuri dan menyedot data sensitif rahasia perusahaan (eksdiltrasi data); jika korban menolak membayar tebusan dekripsi karena memiliki cadangan data (backup), penyerang mengancam akan mempublikasikan data rahasia tersebut ke forum gelap (dark web) atau menjualnya ke kompetitor."
      },
      {
        "key": "B",
        "text": "Penyerang meminta tebusan uang dua kali lipat menggunakan mata uang kripto yang berbeda jenisnya sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Penyerang merusak komponen fisik prosesor dan kartu memori RAM server secara permanen dari jarak jauh."
      },
      {
        "key": "D",
        "text": "Penyerang mengirimkan dua jenis virus trojan yang berbeda untuk menginfeksi dua sistem operasi bersamaan."
      },
      {
        "key": "E",
        "text": "Penyerang mengharuskan pembayaran tebusan dilakukan oleh dua direktur perusahaan secara serentak."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Sebelum mengenkripsi sistem korban, penyerang terlebih dahulu mencuri dan menyedot data sensitif rahasia perusahaan (eksdiltrasi data); jika korban menolak membayar tebusan dekripsi karena memiliki cadangan data (backup), penyerang mengancam akan mempublikasikan data rahasia tersebut ke forum gelap (dark web) atau menjualnya ke kompetitor.. Double Extortion memeras dua kali: mengenkripsi sistem DAN mengancam menyebarkan data curian ke publik jika tebusan tak dibayar. Pilih opsi: Mencuri data sensitif sebelum enkripsi, lalu mengancam mempublikasikannya ke dark web jika tebusan ditolak."
  },
  {
    "id": "inf-sim-17",
    "materi": "BERPIKIR KOMPUTASIONAL",
    "topic": "Prinsip Pembentukan Pohon Pengkodean Huffman (Huffman Coding)",
    "hints": {
      "concept": "Prinsip dasar Huffman: Karakter berfrekuensi tinggi diberi kode bit terpendek (dekat dengan akar), frekuensi rendah diberi bit lebih panjang.",
      "execution": "Pilih: Kode biner berukuran paling pendek, ditempatkan paling dekat dengan akar pohon Huffman."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Algoritma kompresi data bebas kehilangan (lossless) Huffman Coding mengalokasikan kode biner dengan panjang bervariasi (variable-length prefix code) untuk setiap karakter teks. Karakter yang memiliki frekuensi kemunculan sangat tinggi di dalam berkas teks akan mendapatkan...",
    "formulaHud": {
      "title": "PRINSIP OPTIMALITAS PENGKODEAN HUFFMAN",
      "latex": "L_{\\text{avg}} = \\sum_{i=1}^n p_i \\cdot l_i \\implies \\min \\left( \\sum p_i \\cdot l_i \\right) \\iff (p_i > p_j \\implies l_i \\le l_j)",
      "legend": "• $p_i$: Probabilitas/frekuensi karakter $i$<br>• $l_i$: Panjang kode bit karakter $i$<br>• Prefix Rule: Tidak ada kode biner yang menjadi prefiks dari kode biner karakter lain (menjamin dekoding deterministik instan)"
    },
    "options": [
      {
        "key": "A",
        "text": "Kode biner berukuran paling panjang, yang ditempatkan pada cabang pohon terdalam untuk menjaga keaslian data sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Kode biner berukuran paling pendek (sedikit bit), yang ditempatkan pada simpul daun yang posisinya paling dekat dengan simpul akar pada Pohon Huffman."
      },
      {
        "key": "C",
        "text": "Kode biner berukuran tepat 8-bit tetap yang identik dengan pengkodean karakter ASCII standar."
      },
      {
        "key": "D",
        "text": "Dihapus dari berkas teks asli dan digantikan dengan karakter spasi kosong otomatis."
      },
      {
        "key": "E",
        "text": "Kode biner acak yang berganti-ganti nilainya setiap kali berkas teks ditransmisikan melalui jaringan."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Kode biner berukuran paling pendek (sedikit bit), yang ditempatkan pada simpul daun yang posisinya paling dekat dengan simpul akar pada Pohon Huffman.. Prinsip dasar Huffman: Karakter berfrekuensi tinggi diberi kode bit terpendek (dekat dengan akar), frekuensi rendah diberi bit lebih panjang. Pilih: Kode biner berukuran paling pendek, ditempatkan paling dekat dengan akar pohon Huffman."
  },
  {
    "id": "inf-sim-18",
    "materi": "ANALISIS DATA",
    "topic": "Pencegahan Kebocoran Data (Data Leakage) pada Machine Learning",
    "hints": {
      "concept": "Melakukan scaling sebelum split menyebabkan data leakage (informasi data test bocor ke data train), menghasilkan evaluasi performa palsu.",
      "execution": "Pilih: Kebocoran Data (Data Leakage), informasi statistik data uji merembes ke pelatihan."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam melatih model prediktif Machine Learning, seorang pemula melakukan standarisasi fitur (skala normalisasi Z-score) pada seluruh dataset gabungan sebelum membaginya menjadi set data pelatihan (training set) dan set data pengujian (test set). Praktik ini merupakan kesalahan fatal metodologis karena menimbulkan masalah...",
    "formulaHud": {
      "title": "ALUR KERJA PREPROCESSING DATA YANG BENAR",
      "latex": "\\begin{aligned} \\text{Salah (Data Leakage):} & \\quad \\text{FitScaler}(\\text{Seluruh Data}) \\to \\text{Split Train/Test} \\\\ \\mathbf{\\text{Benar:}} & \\quad \\text{Split Train/Test} \\to \\text{FitScaler}(\\mathbf{\\text{Data Train Saja}}) \\to \\text{Transform}(\\text{Data Train \\& Test}) \\end{aligned}",
      "legend": "• Data Leakage: Menggunakan informasi di luar data latih untuk membangun model<br>• Solusi Arsitektural: Memanfaatkan Scikit-Learn `Pipeline` untuk membungkus transformasi data dan estimator"
    },
    "options": [
      {
        "key": "A",
        "text": "Underfitting Ekstrem, di mana model tidak mampu mempelajari pola data sama sekali akibat ketiadaan parameter ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Galat Sintaksis Kompilasi, yang menyebabkan bahasa pemrograman Python menolak mengeksekusi fungsi scikit-learn."
      },
      {
        "key": "C",
        "text": "Kebocoran Data (Data Leakage), di mana informasi statistik (seperti rata-rata $\\mu$ dan standar deviasi $\\sigma$) dari data pengujian ikut merembes dan mencemari proses pelatihan model, sehingga evaluasi akurasi model menjadi terlalu optimis secara palsu dan berkinerja buruk di dunia nyata."
      },
      {
        "key": "D",
        "text": "Kerusakan Hardware Memori RAM, karena dataset terduplikasi secara fisik pada sirkuit motherboard komputer."
      },
      {
        "key": "E",
        "text": "Penurunan Resolusi Grafis, di mana diagram visualisasi data kehilangan warna aslinya saat disimpan."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Kebocoran Data (Data Leakage), di mana informasi statistik (seperti rata-rata $\\mu$ dan standar deviasi $\\sigma$) dari data pengujian ikut merembes dan mencemari proses pelatihan model, sehingga evaluasi akurasi model menjadi terlalu optimis secara palsu dan berkinerja buruk di dunia nyata.. Melakukan scaling sebelum split menyebabkan data leakage (informasi data test bocor ke data train), menghasilkan evaluasi performa palsu. Pilih: Kebocoran Data (Data Leakage), informasi statistik data uji merembes ke pelatihan."
  },
  {
    "id": "inf-sim-19",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Ekstensi Keamanan DNS (DNSSEC) dan Pencegahan Cache Poisoning",
    "hints": {
      "concept": "DNSSEC mengotentikasi respon DNS dengan tanda tangan digital kriptografis (RRSIG) melalui rantai kepercayaan hierarkis (Chain of Trust).",
      "execution": "Pilih opsi: Mengotentikasi keabsahan respons DNS menggunakan tanda tangan digital kriptografi asimetris (RRSIG) via Chain of Trust."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam serangan DNS Cache Poisoning, penyerang membanjiri resolver DNS dengan catatan alamat IP palsu sehingga mengarahkan korban ke situs web phishing tiruan. Ekstensi keamanan DNSSEC (DNS Security Extensions) dirancang untuk memitigasi serangan ini secara fundamental dengan cara...",
    "formulaHud": {
      "title": "RANTAI KEPERCAYAAN DNSSEC (CHAIN OF TRUST)",
      "latex": "\\text{Root Key (KSK)} \\xrightarrow{\\text{DS Record}} \\text{TLD Key} \\xrightarrow{\\text{DS Record}} \\text{Zone Key (ZSK)} \\xrightarrow{\\text{RRSIG}} \\text{A Record (IP Valid)}",
      "legend": "• RRSIG: Tanda tangan digital atas kumpulan record DNS<br>• DNSKEY: Kunci publik yang digunakan resolver untuk memverifikasi RRSIG<br>• DS (Delegation Signer): Hash dari kunci DNS anak yang disimpan di zona induk<br>• Catatan: DNSSEC menjamin Integritas & Otentikasi, BUKAN Kerahasiaan (DNS over HTTPS / DoH yang menangani privasi)"
    },
    "options": [
      {
        "key": "A",
        "text": "Mengenkrpsi seluruh kueri DNS sehingga nama domain yang dicari tidak dapat dibaca oleh penyedia ISP lokal menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Mengganti seluruh server DNS global dengan alamat IP tunggal yang dijaga oleh petugas kepolisian internasional."
      },
      {
        "key": "C",
        "text": "Memaksa seluruh peramban web untuk menghafal seluruh alamat IP situs web di seluruh dunia tanpa bertanya ke resolver."
      },
      {
        "key": "D",
        "text": "Mengotentikasi keabsahan respons kueri DNS menggunakan tanda tangan digital kriptografi asimetris (catatan RRSIG) yang divalidasi melalui rantai kepercayaan hierarkis (Chain of Trust) dari zona root hingga domain otoritatif."
      },
      {
        "key": "E",
        "text": "Memblokir semua situs web yang memiliki ekstensi domain selain `.com` dan `.id` secara permanen."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Mengotentikasi keabsahan respons kueri DNS menggunakan tanda tangan digital kriptografi asimetris (catatan RRSIG) yang divalidasi melalui rantai kepercayaan hierarkis (Chain of Trust) dari zona root hingga domain otoritatif.. DNSSEC mengotentikasi respon DNS dengan tanda tangan digital kriptografis (RRSIG) melalui rantai kepercayaan hierarkis (Chain of Trust). Pilih opsi: Mengotentikasi keabsahan respons DNS menggunakan tanda tangan digital kriptografi asimetris (RRSIG) via Chain of Trust."
  },
  {
    "id": "inf-sim-20",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Analisis Waktu Teramortisasi (Amortized Time Complexity) Array Dinamis",
    "hints": {
      "concept": "Strategi doubling pada vector/list membuat biaya total n operasi adalah < 3n, sehingga biaya rata-rata per operasi adalah O(1) teramortisasi.",
      "execution": "Pilih: O(1) konstan teramortisasi."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Struktur data Array Dinamis (seperti `std::vector` pada C++ atau `list` pada Python) menggandakan kapasitas tampung memorinya menjadi dua kali lipat ($2 \\times$) setiap kali ukuran array penuh saat operasi `append` data baru dipanggil. Meskipun proses penggandaan kapasitas membutuhkan alokasi memori baru dan penyalinan seluruh $n$ elemen sebelumnya ($O(n)$ pada operasi tersebut), kompleksitas waktu teramortisasi (amortized time complexity) per operasi `append` adalah...",
    "formulaHud": {
      "title": "METODE AGREGASI ANALISIS TERAMORTISASI (DOUBLING STRATEGY)",
      "latex": "\\text{Total Biaya } n \\text{ Operasi} = n + \\sum_{j=0}^{\\lfloor \\log_2 n \\rfloor} 2^j = n + (2n - 1) < 3n \\implies T_{\\text{amortized}} = \\frac{\\text{Total Biaya}}{n} = \\frac{< 3n}{n} = O(1)",
      "legend": "• Operasi mahal jarang terjadi: $n$ operasi hanya memicu $\\log_2 n$ kali resizing<br>• Kelemahan Worst-Case Tunggal: Operasi append saat kapasitas pas penuh tetap memakan waktu $O(n)$"
    },
    "options": [
      {
        "key": "A",
        "text": "$O(n)$ linier, karena setiap kali operasi append dipanggil prosesor harus memeriksa seluruh isi array diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "$O(\\log_2 n)$, karena kapasitas array bertambah secara logaritmik setiap kali tombol keyboard ditekan."
      },
      {
        "key": "C",
        "text": "$O(n^2)$ kuadratik, karena penyalinan elemen membutuhkan perbandingan bersarang di dalam memori cache."
      },
      {
        "key": "D",
        "text": "$O(0)$, karena alokasi memori tidak memakan waktu prosesor komputer sama sekali."
      },
      {
        "key": "E",
        "text": "$O(1)$ konstan, karena operasi ekspansi yang mahal ($O(n)$) terjadi sangat jarang (hanya pada kelipatan pangkat dua $1, 2, 4, 8, \\dots, 2^k$), sehingga biaya total ekspansi terbagi rata ke seluruh rangkaian operasi penyisipan."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) $O(1)$ konstan, karena operasi ekspansi yang mahal ($O(n)$) terjadi sangat jarang (hanya pada kelipatan pangkat dua $1, 2, 4, 8, \\dots, 2^k$), sehingga biaya total ekspansi terbagi rata ke seluruh rangkaian operasi penyisipan.. Strategi doubling pada vector/list membuat biaya total n operasi adalah < 3n, sehingga biaya rata-rata per operasi adalah O(1) teramortisasi. Pilih: O(1) konstan teramortisasi."
  },
  {
    "id": "inf-sim-21",
    "materi": "SISTEM KOMPUTER",
    "topic": "Arsitektur Virtualisasi: Hypervisor Tipe 1 vs Hypervisor Tipe 2 vs Kontainer",
    "hints": {
      "concept": "VM memvirtualisasikan hardware dan punya OS/kernel sendiri. Kontainer berbagi kernel host yang sama via namespaces & cgroups sehingga jauh lebih ringan.",
      "execution": "Pilih: VM menjalankan kernel Guest OS mandiri, sedangkan Kontainer berbagi kernel host yang sama dengan isolasi user-space."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam pusat data komputasi awan (Cloud Computing), teknologi virtualisasi digunakan untuk memaksimalkan utilisasi perangkat keras server fisik. Perbedaan arsitektural mendasar antara Virtual Machine berbasis Hypervisor Tipe 1 (Bare-Metal seperti VMware ESXi / KVM) dan Kontainerisasi (seperti Docker) adalah...",
    "formulaHud": {
      "title": "KOMPARASI STACK VIRTUALISASI VS KONTAINERISASI",
      "latex": "\\begin{aligned} \\text{VM (Hypervisor Tipe 1):} & \\quad [\\text{Hardware}] \\to [\\text{Hypervisor}] \\to [\\mathbf{\\text{Guest OS}} + \\text{Bins/Libs} + \\text{App}] \\implies \\text{Isolasi Kuat, Berat} \\\\ \\text{Container (Docker):} & \\quad [\\text{Hardware}] \\to [\\mathbf{\\text{Host OS (Shared Kernel)}}] \\to [\\text{Container Engine}] \\to [\\text{Bins/Libs} + \\text{App}] \\implies \\text{Ringan, Instan} \\end{aligned}",
      "legend": "• Guest OS Overhead: VM memakan RAM gigabytes untuk kernel OS masing-masing<br>• Kontainer: Menggunakan Linux Namespaces (isolasi PID, NET, MNT) dan Control Groups (cgroups untuk batas CPU/RAM)"
    },
    "options": [
      {
        "key": "A",
        "text": "Virtual Machine memvirtualisasikan perangkat keras fisik penuh dan menjalankan kernel sistem operasi tamu (Guest OS) mandiri di setiap instance, sedangkan Kontainer berbagi kernel sistem operasi host yang sama dan hanya mengisolasi ruang pengguna (user-space via cgroups dan namespaces) sehingga jauh lebih ringan dan cepat dimulai."
      },
      {
        "key": "B",
        "text": "Kontainer membutuhkan perangkat keras server fisik terpisah untuk setiap aplikasi yang dijalankan sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "C",
        "text": "Virtual Machine tidak dapat menjalankan sistem operasi berbasis Linux sama sekali di dalam pusat data."
      },
      {
        "key": "D",
        "text": "Kontainer memiliki ukuran berkas citra (image) puluhan gigabyte yang jauh lebih besar daripada berkas Virtual Disk."
      },
      {
        "key": "E",
        "text": "Hypervisor Tipe 1 berjalan di atas sistem operasi komersial Windows Desktop seperti halnya aplikasi biasa."
      }
    ],
    "correctKey": "A",
    "explanation": "Kunci Jawaban: (A) Virtual Machine memvirtualisasikan perangkat keras fisik penuh dan menjalankan kernel sistem operasi tamu (Guest OS) mandiri di setiap instance, sedangkan Kontainer berbagi kernel sistem operasi host yang sama dan hanya mengisolasi ruang pengguna (user-space via cgroups dan namespaces) sehingga jauh lebih ringan dan cepat dimulai.. VM memvirtualisasikan hardware dan punya OS/kernel sendiri. Kontainer berbagi kernel host yang sama via namespaces & cgroups sehingga jauh lebih ringan. Pilih: VM menjalankan kernel Guest OS mandiri, sedangkan Kontainer berbagi kernel host yang sama dengan isolasi user-space."
  },
  {
    "id": "inf-sim-22",
    "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
    "topic": "Algoritma Time-Based One-Time Password (TOTP RFC 6238)",
    "hints": {
      "concept": "TOTP menghitung counter T = UnixTime / 30, lalu di-hash dengan shared secret memakai HMAC-SHA1, lalu dipangkas (truncated) menjadi 6 digit.",
      "execution": "Pilih opsi yang menjelaskan perhitungan counter waktu T = (Unix Time / 30), evaluasi HMAC-SHA1 dengan kunci rahasia bersama, dan Dynamic Truncation."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Aplikasi otentikator dua faktor (2FA seperti Google Authenticator) menghasilkan 6 digit kode sandi sekali pakai yang berganti setiap 30 detik tanpa memerlukan koneksi internet aktif pada ponsel pengguna. Mekanisme komputasi yang digunakan oleh algoritma Time-Based One-Time Password (TOTP RFC 6238) tersebut adalah...",
    "formulaHud": {
      "title": "FORMULA ALGORITMA TOTP (RFC 6238)",
      "latex": "T = \\left\\lfloor \\frac{\\text{Unix Epoch Time}}{30} \\right\\rfloor, \\quad \\text{TOTP} = \\text{Truncate}\\Big(\\text{HMAC-SHA1}(K, T)\\Big) \\pmod{10^6}",
      "legend": "• $K$: Kunci rahasia bersama (Shared Secret) berbentuk Base32 yang disimpan saat memindai QR code<br>• $T$: Penghitung interval waktu 30 detik yang tersinkronisasi antara ponsel dan server via NTP<br>• Truncate: Mengambil 4-byte integer dinamis dari 20-byte digest hash HMAC"
    },
    "options": [
      {
        "key": "A",
        "text": "Menerima sinyal siaran gelombang radio GPS satelit rahasia yang dikirimkan langsung oleh server aplikasi ke ponsel sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi."
      },
      {
        "key": "B",
        "text": "Menghitung nilai counter waktu diskret $T = \\lfloor (\\text{Unix Time Saat Ini} - T_0) / 30 \\rfloor$, lalu mengevaluasi nilai Hash-based Message Authentication Code (HMAC-SHA1) menggunakan kunci rahasia bersama (shared secret key) yang dipindai saat registrasi QR Code awal, kemudian memangkas hasilnya menjadi 6 digit angka melalui Dynamic Truncation."
      },
      {
        "key": "C",
        "text": "Mengirimkan permintaan kueri HTTP POST rahasia melalui jaringan seluler tersembunyi setiap 30 detik secara terus-menerus."
      },
      {
        "key": "D",
        "text": "Membaca nomor seri perangkat keras kartu SIM pengguna dan membaginya dengan angka tahun kabisat kalender."
      },
      {
        "key": "E",
        "text": "Menghasilkan bilangan acak murni yang ditebak secara telepati komputasional oleh server web autentikasi."
      }
    ],
    "correctKey": "B",
    "explanation": "Kunci Jawaban: (B) Menghitung nilai counter waktu diskret $T = \\lfloor (\\text{Unix Time Saat Ini} - T_0) / 30 \\rfloor$, lalu mengevaluasi nilai Hash-based Message Authentication Code (HMAC-SHA1) menggunakan kunci rahasia bersama (shared secret key) yang dipindai saat registrasi QR Code awal, kemudian memangkas hasilnya menjadi 6 digit angka melalui Dynamic Truncation.. TOTP menghitung counter T = UnixTime / 30, lalu di-hash dengan shared secret memakai HMAC-SHA1, lalu dipangkas (truncated) menjadi 6 digit. Pilih opsi yang menjelaskan perhitungan counter waktu T = (Unix Time / 30), evaluasi HMAC-SHA1 dengan kunci rahasia bersama, dan Dynamic Truncation."
  },
  {
    "id": "inf-sim-23",
    "materi": "PRAKTIK LINTAS BIDANG",
    "topic": "Ketahanan Sistem Terdistribusi: Circuit Breaker Pattern",
    "hints": {
      "concept": "Pola untuk mencegah cascading failure dengan memutus panggilan ke servis yang mati dan memberikan fallback instan adalah Circuit Breaker Pattern.",
      "execution": "Pilih: Circuit Breaker Pattern (status Closed -> Open -> Half-Open)."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam arsitektur mikroservis perbankan, Layanan Pembayaran memanggil API Layanan Pengecekan Skor Kredit secara berkala melalui jaringan. Jika server skor kredit mengalami mati total (down) dan responsnya hang, Layanan Pembayaran akan kehabisan thread penampung antrean permintaan koneksi (connection pool exhaustion) sehingga ikut tumbang, memicu kegagalan beruntun (cascading failure) ke seluruh sistem. Pola desain ketahanan perangkat lunak yang paling tepat untuk mengisolasi dan memitigasi kegagalan ini adalah...",
    "formulaHud": {
      "title": "STATE MACHINE POLA CIRCUIT BREAKER",
      "latex": "\\begin{aligned} \\mathbf{\\text{Closed:}} & \\quad \\text{Operasi normal} \\xrightarrow{\\text{Tingkat Galat } > \\text{ Threshold}} \\mathbf{\\text{Open}} \\\\ \\mathbf{\\text{Open:}} & \\quad \\text{Semua panggilan langsung di-reject (Fail Fast / Fallback)} \\xrightarrow{\\text{Sleep Window Habis}} \\mathbf{\\text{Half-Open}} \\\\ \\mathbf{\\text{Half-Open:}} & \\quad \\text{Izinkan beberapa panggilan uji coba} \\implies \\begin{cases} \\text{Sukses} & \\to \\mathbf{\\text{Closed}} \\\\ \\text{Gagal} & \\to \\mathbf{\\text{Open}} \\end{cases} \\end{aligned}",
      "legend": "• Manfaat: Mencegah thread starvation, mengurangi beban pada layanan yang sedang bermasalah, dan mempertahankan stabilitas sistem utama"
    },
    "options": [
      {
        "key": "A",
        "text": "Pola Singleton Pattern; membatasi jumlah objek layanan pembayaran hanya satu instansiasi di seluruh memori server ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data ditinjau dari keutuhan relasi model data terstruktur serta integritas referensial basis data."
      },
      {
        "key": "B",
        "text": "Pola Infinite Retry Pattern; secara agresif mengirimkan jutaan panggilan permintaan baru setiap milidetik ke server yang mati."
      },
      {
        "key": "C",
        "text": "Pola Pemutus Arus (Circuit Breaker Pattern); jika rasio kegagalan panggilan layanan eksternal melampaui ambang batas, sirkuit berpindah ke status 'Open' dan langsung mengembalikan respons kegagalan instan (fallback) tanpa membuang waktu memanggil layanan yang rusak, lalu secara berkala beralih ke status 'Half-Open' untuk menguji pemulihan layanan."
      },
      {
        "key": "D",
        "text": "Pola Monolithic Migration; menghapus seluruh repositori Git dan menulis ulang program menggunakan satu berkas kode tunggal."
      },
      {
        "key": "E",
        "text": "Pola Factory Method; membuat kelas turunan baru untuk menampung data kartu kredit nasabah secara manual."
      }
    ],
    "correctKey": "C",
    "explanation": "Kunci Jawaban: (C) Pola Pemutus Arus (Circuit Breaker Pattern); jika rasio kegagalan panggilan layanan eksternal melampaui ambang batas, sirkuit berpindah ke status 'Open' dan langsung mengembalikan respons kegagalan instan (fallback) tanpa membuang waktu memanggil layanan yang rusak, lalu secara berkala beralih ke status 'Half-Open' untuk menguji pemulihan layanan.. Pola untuk mencegah cascading failure dengan memutus panggilan ke servis yang mati dan memberikan fallback instan adalah Circuit Breaker Pattern. Pilih: Circuit Breaker Pattern (status Closed -> Open -> Half-Open)."
  },
  {
    "id": "inf-sim-24",
    "materi": "ANALISIS DATA",
    "topic": "Asumsi Fundamental Pengklasifikasi Naive Bayes",
    "hints": {
      "concept": "Disebut \"Naive\" karena mengasumsikan semua fitur saling independen secara bersyarat (conditionally independent) terhadap kelas target, padahal di realita ada korelasi antar kata.",
      "execution": "Pilih opsi: Mengasumsikan setiap fitur saling independen bersyarat satu sama lain terhadap kelas target."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Pengklasifikasi Naive Bayes sering digunakan untuk mendeteksi pesan spam surel berdasarkan kemunculan kata-kata teks. Alasan mengapa algoritma klasifikasi probabilistik berbasis Teorema Bayes ini dinamakan \"Naive\" (lugu/naif) adalah...",
    "formulaHud": {
      "title": "TEOREMA NAIVE BAYES DENGAN ASUMSI INDEPENDENSI BERSYARAT",
      "latex": "P(C_k \\mid x_1, \\dots, x_n) \\propto P(C_k) \\prod_{i=1}^n P(x_i \\mid C_k)",
      "legend": "• Asumsi Naif: $P(x_1, x_2, \\dots, x_n \\mid C_k) = \\prod_{i=1}^n P(x_i \\mid C_k)$<br>• Keunggulan: Menghindari perhitungan distribusi probabilitas gabungan eksponensial yang mustahil dihitung pada dimensi besar<br>• Tetap bekerja sangat baik di dunia nyata untuk klasifikasi teks dan spam filtering"
    },
    "options": [
      {
        "key": "A",
        "text": "Algoritma tidak mampu melakukan kalkulasi matematika pecahan desimal sehingga seluruh angka dibulatkan ke nol menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu."
      },
      {
        "key": "B",
        "text": "Algoritma hanya dapat dilatih menggunakan data buatan yang dibuat oleh manusia tanpa algoritma komputasi."
      },
      {
        "key": "C",
        "text": "Algoritma secara naif mengasumsikan bahwa semua pengirim surel di dunia adalah peretas berbahaya."
      },
      {
        "key": "D",
        "text": "Algoritma membuat asumsi penyederhanaan yang sangat kuat dan naif bahwa setiap fitur atribut (keberadaan kata dalam pesan) saling independen bersyarat (conditionally independent) satu sama lain terhadap kelas target, mengabaikan fakta nyata bahwa dalam bahasa manusia keberadaan suatu kata sering kali berkorelasi erat dengan kata lainnya."
      },
      {
        "key": "E",
        "text": "Algoritma membutuhkan waktu pelatihan jutaan jam komputasi karena tidak memiliki rumus probabilitas tertutup."
      }
    ],
    "correctKey": "D",
    "explanation": "Kunci Jawaban: (D) Algoritma membuat asumsi penyederhanaan yang sangat kuat dan naif bahwa setiap fitur atribut (keberadaan kata dalam pesan) saling independen bersyarat (conditionally independent) satu sama lain terhadap kelas target, mengabaikan fakta nyata bahwa dalam bahasa manusia keberadaan suatu kata sering kali berkorelasi erat dengan kata lainnya.. Disebut \"Naive\" karena mengasumsikan semua fitur saling independen secara bersyarat (conditionally independent) terhadap kelas target, padahal di realita ada korelasi antar kata. Pilih opsi: Mengasumsikan setiap fitur saling independen bersyarat satu sama lain terhadap kelas target."
  },
  {
    "id": "inf-sim-25",
    "materi": "DAMPAK SOSIAL INFORMATIKA",
    "topic": "Privasi Kriptografis Zero-Knowledge Proofs (ZKP)",
    "hints": {
      "concept": "Zero-Knowledge Proof membuktikan kebenaran sebuah pernyataan TANPA membocorkan isi rahasia itu sendiri (zero knowledge leak).",
      "execution": "Pilih: Tanpa perlu mengungkapkan informasi rahasia atau data pribadi pendukung kepada pihak pemverifikasi."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "questionHtml": "Dalam era perlindungan data identitas digital, protokol Zero-Knowledge Proof (ZKP) memungkinkan pihak pembukti (Prover) untuk meyakinkan pihak pemverifikasi (Verifier) bahwa suatu pernyataan rahasia adalah benar (misalnya membuktikan bahwa usia pemohon sudah di atas 17 tahun untuk membeli tiket film dewasa), dengan karakteristik kriptografis yang luar biasa yaitu...",
    "formulaHud": {
      "title": "TIGA PROPERTI PROTOKOL ZERO-KNOWLEDGE PROOFS (ZKP)",
      "latex": "\\text{ZKP} \\equiv \\begin{cases} \\mathbf{\\text{Completeness:}} & \\text{Jika pernyataan benar, Verifier jujur pasti yakin} \\\\ \\mathbf{\\text{Soundness:}} & \\text{Jika pernyataan salah, Prover penipu tidak bisa meyakinkan Verifier} \\\\ \\mathbf{\\text{Zero-Knowledge:}} & \\text{Verifier tidak mempelajari apapun selain fakta bahwa pernyataan tersebut benar} \\end{cases}",
      "legend": "• Implementasi Modern: zk-SNARKs pada teknologi blockchain, otentikasi identitas berdaulat mandiri (Self-Sovereign Identity)"
    },
    "options": [
      {
        "key": "A",
        "text": "Dengan mengirimkan seluruh salinan kartu identitas KTP fisik asli melalui surel publik tanpa enkripsi diturunkan dari kaidah penalaran rekursif dan struktur pohon biner pencarian data."
      },
      {
        "key": "B",
        "text": "Dengan mewajibkan pihak pemverifikasi untuk menyerahkan kunci privat rekening banknya kepada pihak pembukti."
      },
      {
        "key": "C",
        "text": "Dengan cara menghapus seluruh catatan transaksi di peladen pemerintah secara sepihak dan permanen."
      },
      {
        "key": "D",
        "text": "Hanya berlaku jika kedua belah pihak menandatangani kontrak hukum di hadapan notaris resmi di kantor pengadilan."
      },
      {
        "key": "E",
        "text": "Tanpa perlu mengungkapkan informasi rahasia itu sendiri atau data pribadi pendukung lainnya (seperti tanggal lahir asli, nama lengkap, atau nomor NIK) kepada pihak pemverifikasi."
      }
    ],
    "correctKey": "E",
    "explanation": "Kunci Jawaban: (E) Tanpa perlu mengungkapkan informasi rahasia itu sendiri atau data pribadi pendukung lainnya (seperti tanggal lahir asli, nama lengkap, atau nomor NIK) kepada pihak pemverifikasi.. Zero-Knowledge Proof membuktikan kebenaran sebuah pernyataan TANPA membocorkan isi rahasia itu sendiri (zero knowledge leak). Pilih: Tanpa perlu mengungkapkan informasi rahasia atau data pribadi pendukung kepada pihak pemverifikasi."
  },
  {
    "id": "inf-sim-26",
    "type": "multi",
    "materi": "BERPIKIR KOMPUTASIONAL & TEORI KOMPLEKSITAS",
    "topic": "Karakteristik Kelas Kompleksitas Masalah Komputasi (P, NP, NP-Complete)",
    "options": [
      {
        "key": "A",
        "text": "Masalah dalam kelas P (Polynomial Time) dapat diselesaikan oleh mesin Turing deterministik dalam waktu polinomial $O(n^k)$."
      },
      {
        "key": "B",
        "text": "Masalah dalam kelas NP (Nondeterministic Polynomial Time) adalah masalah keputusan yang solusi usulannya (certificate) dapat diverifikasi kebenarannya dalam waktu polinomial."
      },
      {
        "key": "C",
        "text": "Sebuah masalah $X$ diklasifikasikan sebagai NP-Complete jika $X \\in \\text{NP}$ dan setiap masalah lain di kelas NP dapat direduksi ke $X$ dalam waktu polinomial (Polynomial-Time Reduction)."
      },
      {
        "key": "D",
        "text": "Hingga saat ini telah terbukti secara matematis bahwa kelas masalah P sama persis dengan kelas masalah NP ($P = NP$)."
      },
      {
        "key": "E",
        "text": "Seluruh masalah dalam kelas NP-Complete dapat diselesaikan dalam waktu logaritmik $O(\\log n)$ oleh komputer kuantum personal."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Kelas P: diselesaikan dalam waktu polinomial (A). Kelas NP: diverifikasi dalam waktu polinomial (B). NP-Complete: anggota NP dan semua masalah NP bisa direduksi secara polinomial ke masalah tersebut (C). P vs NP masih problem terbuka.",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Dalam teori komputasi teoritis, klasifikasi masalah komputasi terbagi menjadi kelas P, NP, NP-Complete, dan NP-Hard. Manakah TIGA pernyataan berikut yang secara ilmiah BENAR mengenai kelas kompleksitas masalah tersebut? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "RELASI HIMPUNAN KELAS KOMPLEKSITAS KOMPUTASI",
      "latex": "P \\subseteq NP, \\quad \\text{NP-Complete} = NP \\cap \\text{NP-Hard}",
      "legend": "• A BENAR: Definisi kelas P (Deterministic Polynomial Time)<br>• B BENAR: Definisi kelas NP (Polynomially Verifiable)<br>• C BENAR: Definisi NP-Complete menurut Teorema Cook-Levin<br>• D dan E SALAH: Masalah $P \\stackrel{?}{=} NP$ adalah Millennium Prize Problem terbuka; NP-Complete belum terbukti bisa diselesaikan logaritmik"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Kelas P: diselesaikan dalam waktu polinomial (A). Kelas NP: diverifikasi dalam waktu polinomial (B). NP-Complete: anggota NP dan semua masalah NP bisa direduksi secara polinomial ke masalah tersebut (C). P vs NP masih problem terbuka. Pilih A, B, dan C."
  },
  {
    "id": "inf-sim-27",
    "materi": "SISTEM KOMPUTER",
    "topic": "Penyebab Terjadinya Fenomena Thrashing pada Memori Virtual",
    "options": [
      {
        "key": "A",
        "text": "Derajat multiprogramming (Degree of Multiprogramming) dinaikkan terlalu tinggi sehingga terlalu banyak proses aktif yang bersaing memperebutkan alokasi memori fisik yang terbatas."
      },
      {
        "key": "B",
        "text": "Jumlah bingkai memori fisik (page frames) yang dialokasikan untuk setiap proses berada di bawah ukuran kebutuhan himpunan kerja minimumnya (Working-Set Size)."
      },
      {
        "key": "C",
        "text": "Proses-proses yang sedang berjalan memiliki sifat lokalitas referensi (Locality of Reference) yang sangat buruk atau mengakses memori secara acak melintasi rentang alamat yang teramat luas."
      },
      {
        "key": "D",
        "text": "Kapasitas media penyimpanan sekunder SSD telah terisi penuh 100% sehingga tidak ada ruang swap file yang tersedia sama sekali."
      },
      {
        "key": "E",
        "text": "Sistem operasi menggunakan algoritma penjadwalan CPU Round-Robin dengan kuantum waktu yang terlalu besar."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Pemicu Thrashing: derajat multiprogramming terlalu tinggi (A), alokasi frame kurang dari working-set (B), dan rusaknya locality of reference (C).",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "questionHtml": "Thrashing adalah kondisi kritis di mana sistem operasi menghabiskan lebih banyak waktu untuk melakukan pertukaran halaman memori (paging/swapping) antara RAM dan hard disk daripada mengeksekusi instruksi program, sehingga utilisasi CPU anjlok mendekati nol. Manakah TIGA faktor berikut yang menjadi pemicu utama terjadinya fenomena Thrashing? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "MODEL WORKING-SET PENCEGAHAN THRASHING",
      "latex": "D = \\sum_{i} WSS_i > \\text{Total RAM Frames} \\implies \\text{Terjadi Thrashing!}",
      "legend": "• A, B, C BENAR: Ketika total kebutuhan working-set seluruh proses ($D$) melebihi total frame RAM fisik, proses akan saling merebut halaman memori satu sama lain secara terus-menerus<br>• Solusi OS: Turunkan derajat multiprogramming (suspend beberapa proses sementara)"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Pemicu Thrashing: derajat multiprogramming terlalu tinggi (A), alokasi frame kurang dari working-set (B), dan rusaknya locality of reference (C). Pilih A, B, dan C."
  },
  {
    "id": "inf-sim-28",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Fitur Modern Protokol Keamanan Transport Layer Security (TLS 1.3)",
    "options": [
      {
        "key": "A",
        "text": "Memangkas waktu negosiasi jabat tangan (handshake latency) dari 2-RTT menjadi hanya 1-RTT untuk sambungan baru, dan mendukung mode 0-RTT (Zero Round Trip Time) untuk koneksi berulang."
      },
      {
        "key": "B",
        "text": "Menghapus secara permanen seluruh cipher suite dan algoritma kriptografi yang usang dan rentan, seperti RSA key exchange statis, CBC mode, RC4, MD5, dan SHA-1."
      },
      {
        "key": "C",
        "text": "Mewajibkan penggunaan Forward Secrecy secara mutlak melalui algoritma pertukaran kunci Diffie-Hellman Ephemeral (DHE / ECDHE) sehingga rekaman data masa lalu tidak dapat didekripsi jika kunci privat server bocor di masa depan."
      },
      {
        "key": "D",
        "text": "Menghapus kewajiban sertifikat digital X.509 sehingga siapa saja dapat menyamar sebagai server bank tanpa otoritas Certificate Authority (CA)."
      },
      {
        "key": "E",
        "text": "Menggantikan seluruh alamat IP versi 4 menjadi alamat MAC address fisik pada lapisan aplikasi."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "TLS 1.3: Handshake lebih cepat (1-RTT/0-RTT) (A), menghapus cipher usang (B), dan mewajibkan Perfect Forward Secrecy via ephemeral key exchange (C).",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "questionHtml": "Protokol keamanan web TLS 1.3 (RFC 8446) membawa lompatan besar dalam hal performa latensi dan ketahanan kriptografi dibandingkan versi TLS pendahulunya. Manakah TIGA fitur pembaharuan kunci berikut yang diperkenalkan pada standar TLS 1.3? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "EVOLUSI PROTOKOL KEAMANAN TLS 1.2 KE TLS 1.3",
      "latex": "\\begin{aligned} \\text{TLS 1.2:} & \\quad \\text{Handshake: 2-RTT}, \\ \\text{Dukung RSA Key Exchange (No Forward Secrecy)}, \\ \\text{Banyak Algoritma Usang} \\\\ \\text{TLS 1.3:} & \\quad \\mathbf{\\text{Handshake: 1-RTT / 0-RTT}}, \\ \\mathbf{\\text{PFS Mutlak (ECDHE Saja)}}, \\ \\mathbf{\\text{Hanya AEAD Ciphers (AES-GCM/ChaCha20)}} \\end{aligned}",
      "legend": "• A, B, C BENAR: Karakteristik revolusioner TLS 1.3<br>• D dan E SALAH: CA tetap wajib untuk otentikasi identitas publik"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "TLS 1.3: Handshake lebih cepat (1-RTT/0-RTT) (A), menghapus cipher usang (B), dan mewajibkan Perfect Forward Secrecy via ephemeral key exchange (C). Pilih A, B, dan C."
  },
  {
    "id": "inf-sim-29",
    "materi": "ANALISIS DATA",
    "topic": "Karakteristik Transaksi ACID pada Basis Data Relasional",
    "options": [
      {
        "key": "A",
        "text": "Atomicity (Keutuhan) menjamin bahwa transaksi dieksekusi dengan prinsip 'semua atau tidak sama sekali' (all-or-nothing); jika salah satu operasi gagal, seluruh perubahan dibatalkan (rollback) ke kondisi awal."
      },
      {
        "key": "B",
        "text": "Isolation (Keterisolasian) menjamin bahwa eksekusi transaksi konkuren berjalan independen tanpa saling mencemari status antara satu sama lain sebelum transaksi di-commit."
      },
      {
        "key": "C",
        "text": "Durability (Ketahanan) menjamin bahwa begitu transaksi berhasil di-commit, seluruh perubahannya tersimpan secara permanen di media penyimpanan non-volatile dan tidak akan hilang meskipun terjadi pemadaman listrik seketika."
      },
      {
        "key": "D",
        "text": "Consistency menjamin bahwa basis data tidak memerlukan kunci primer (Primary Key) dalam merelasikan entitas data."
      },
      {
        "key": "E",
        "text": "Atomicity menjamin bahwa kecepatan eksekusi kueri transaksi selalu berjalan di bawah 1 milidetik terlepas dari volume data."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Pilar ACID: Atomicity adalah all-or-nothing (A), Isolation adalah eksekusi konkuren terisolasi (B), Durability adalah permanen pasca-commit meski mati listrik (C).",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "questionHtml": "Prinsip ACID (Atomicity, Consistency, Isolation, Durability) menjamin integritas pemrosesan data finansial di dalam sistem manajemen basis data relasional (RDBMS). Manakah TIGA pernyataan berikut yang mendefinisikan pilar ACID secara tepat? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "DEFINISI EMPAT PILAR TRANSAKSI BASIS DATA ACID",
      "latex": "\\text{ACID} \\equiv \\begin{cases} \\mathbf{\\text{A (Atomicity):}} & \\text{All-or-Nothing (Rollback jika gagal)} \\\\ \\mathbf{\\text{C (Consistency):}} & \\text{Mempertahankan seluruh invariant dan integritas skema DB} \\\\ \\mathbf{\\text{I (Isolation):}} & \\text{Transaksi konkuren tidak saling mengganggu (Concurrecy Control)} \\\\ \\mathbf{\\text{D (Durability):}} & \\text{Perubahan commit bersifat permanen (Write-Ahead Logging / WAL)} \\end{cases}",
      "legend": "• A, B, C BENAR: Definisi formal Atomicity, Isolation, dan Durability<br>• D dan E SALAH: Consistency justru menjaga aturan integritas, dan ACID tidak mengatur batas kecepatan waktu milidetik"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Pilar ACID: Atomicity adalah all-or-nothing (A), Isolation adalah eksekusi konkuren terisolasi (B), Durability adalah permanen pasca-commit meski mati listrik (C). Pilih A, B, dan C."
  },
  {
    "id": "inf-sim-30",
    "materi": "ALGORITMA & PEMROGRAMAN",
    "topic": "Tiga Kondisi Kasus pada Teorema Master Asimtotik",
    "options": [
      {
        "key": "A",
        "text": "Jika fungsi kerja pembagian/penggabungan $f(n) = O(n^{\\log_b a - \\epsilon})$ untuk suatu konstanta $\\epsilon > 0$, maka kompleksitas waktu didominasi oleh daun pohon rekursi dengan solusi $T(n) = \\Theta(n^{\\log_b a})$ (Kasus 1)."
      },
      {
        "key": "B",
        "text": "Jika fungsi kerja $f(n) = \\Theta(n^{\\log_b a})$, maka biaya pada setiap level pohon rekursi adalah seimbang sehingga solusinya adalah $T(n) = \\Theta(n^{\\log_b a} \\log_2 n)$ (Kasus 2)."
      },
      {
        "key": "C",
        "text": "Jika fungsi kerja $f(n) = \\Omega(n^{\\log_b a + \\epsilon})$ untuk $\\epsilon > 0$ dan memenuhi kondisi keteraturan $a f(n/b) \\le c f(n)$ dengan $c < 1$, maka solusinya didominasi oleh akar dengan $T(n) = \\Theta(f(n))$ (Kasus 3)."
      },
      {
        "key": "D",
        "text": "Teorema Master dapat digunakan untuk menyelesaikan semua jenis relasi rekurensi tanpa syarat, termasuk jika $a < 1$ atau $b$ bernilai pecahan negatif."
      },
      {
        "key": "E",
        "text": "Algoritma Binary Search memiliki nilai $a = 2$ dan $b = 2$ sehingga diselesaikan menggunakan Kasus 1 Teorema Master."
      }
    ],
    "correctAnswer": [
      "A",
      "B",
      "C"
    ],
    "hints": {
      "concept": "Tiga kasus Teorema Master: Kasus 1 didominasi daun (A), Kasus 2 seimbang per level dikali log n (B), Kasus 3 didominasi akar f(n) dengan syarat keteraturan (C).",
      "execution": "Pilih A, B, dan C."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "questionHtml": "Teorema Master digunakan untuk menyelesaikan relasi rekurensi algoritma bertipe divide-and-conquer dalam bentuk $T(n) = aT(n/b) + f(n)$ dengan $a \\ge 1$ dan $b > 1$. Manakah TIGA pernyataan berikut yang BENAR mengenai kasus Teorema Master? (Pilih TIGA jawaban yang benar)",
    "formulaHud": {
      "title": "FORMULASI MATEMATIS TEOREMA MASTER",
      "latex": "T(n) = aT(n/b) + f(n) \\implies \\text{Bandingkan } f(n) \\text{ dengan } n^{\\log_b a} \\implies \\begin{cases} \\text{Kasus 1:} & f(n) < n^{\\log_b a} \\implies T(n) = \\Theta(n^{\\log_b a}) \\\\ \\text{Kasus 2:} & f(n) = n^{\\log_b a} \\implies T(n) = \\Theta(n^{\\log_b a} \\log n) \\\\ \\text{Kasus 3:} & f(n) > n^{\\log_b a} \\implies T(n) = \\Theta(f(n)) \\end{cases}",
      "legend": "• A, B, C BENAR: Tiga pilar kasus fundamental Teorema Master<br>• D SALAH: Ada syarat regularitas dan keterbatasan fungsi<br>• E SALAH: Binary Search memiliki $a = 1$ (hanya memanggil 1 sub-masalah), $b = 2$, dan $f(n) = O(1)$"
    },
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "explanation": "Tiga kasus Teorema Master: Kasus 1 didominasi daun (A), Kasus 2 seimbang per level dikali log n (B), Kasus 3 didominasi akar f(n) dengan syarat keteraturan (C). Pilih A, B, dan C."
  },
  {
    "id": "inf-sim-31",
    "type": "matrix",
    "materi": "ARSITEKTUR SISTEM KOMPUTER & MEMORI",
    "topic": "Karakteristik Arsitektur Prosesor, Hierarki Memori, dan Eksekusi Instruksi",
    "statements": [
      {
        "text": "Program Counter (PC) adalah register CPU yang bertugas menyimpan alamat memori dari instruksi berikutnya yang akan diambil (fetched) untuk dieksekusi.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Memori SRAM (Static RAM) yang digunakan pada Cache Memory membutuhkan penyegaran berkala (refresh cycle) ribuan kali per detik seperti halnya DRAM pada RAM utama.",
        "correct": "Salah",
        "id": "1"
      },
      {
        "text": "Dalam arsitektur Harvard, bus instruksi dan bus data dipisahkan secara fisik sehingga CPU dapat membaca instruksi dan data secara bersamaan tanpa saling menunggu.",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Memori virtual (Virtual Memory) memungkinkan ukuran total alokasi memori proses melampaui kapasitas fisik RAM yang terpasang di komputer.",
        "correct": "Benar",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "PC menyimpan alamat instruksi berikutnya. SRAM tidak butuh refresh (DRAM yang butuh refresh). Arsitektur Harvard memisahkan bus instruksi dan data. Virtual memory memungkinkan memori melebihi RAM fisik.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai arsitektur sistem komputer modern dan manajemen memori!",
    "formulaHud": {
      "title": "PRINSIP PERANGKAT KERAS & ARSITEKTUR KOMPUTER",
      "latex": "\\text{Arsitektur Von Neumann (Shared Bus)} \\iff \\text{Arsitektur Harvard (Separate Code/Data Buses)}",
      "legend": "• Pernyataan 1 BENAR: Fungsi mutlak Program Counter (PC)<br>• Pernyataan 2 SALAH: SRAM menggunakan sirkuit bistable flip-flop sehingga TIDAK memerlukan refresh cycle (DRAM yang butuh kapasitor refresh)<br>• Pernyataan 3 BENAR: Karakteristik utama arsitektur Harvard<br>• Pernyataan 4 BENAR: Esensi memori virtual berbasis swapping/paging ke disk"
    },
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "explanation": "PC menyimpan alamat instruksi berikutnya. SRAM tidak butuh refresh (DRAM yang butuh refresh). Arsitektur Harvard memisahkan bus instruksi dan data. Virtual memory memungkinkan memori melebihi RAM fisik. Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
  },
  {
    "id": "inf-sim-32",
    "type": "matrix",
    "materi": "STRUKTUR DATA & ALGORITMA",
    "topic": "Sifat Struktur Data Linear, Pohon, dan Kompleksitas Algoritma",
    "statements": [
      {
        "text": "Operasi penelusuran In-Order pada Binary Search Tree (BST) selalu menghasilkan barisan data simpul yang terurut menaik (ascending).",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Algoritma Merge Sort bersifat in-place dan tidak membutuhkan alokasi memori tambahan sama sekali selama proses penggabungan larik.",
        "correct": "Salah",
        "id": "1"
      },
      {
        "text": "Struktur data Queue menerapkan prinsip FIFO (First-In First-Out) dan digunakan sebagai struktur pendukung utama pada penelusuran Breadth-First Search (BFS).",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Algoritma Binary Search dapat dieksekusi dengan kompleksitas O(log n) pada struktur data Singly Linked List yang elemennya sudah terurut.",
        "correct": "Salah",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "BST In-order menghasilkan urutan terurut menaik. Merge Sort butuh memori tambahan O(n). Queue menerapkan FIFO dan dipakai BFS. Binary Search tidak efisien di Linked List karena tidak ada akses acak O(1) ke elemen tengah.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai struktur data dan efisiensi algoritma!",
    "formulaHud": {
      "title": "EVALUASI STRUKTUR DATA DAN KOMPLEKSITAS",
      "latex": "\\text{BST In-Order} \\implies \\text{Sorted}, \\quad \\text{Merge Sort Aux Mem} = O(n), \\quad \\text{Binary Search Linked List} = O(n) \\text{ (No Random Access!)}",
      "legend": "• Pernyataan 1 BENAR: Sifat khas BST<br>• Pernyataan 2 SALAH: Merge Sort membutuhkan larik bantu $O(n)$ (bukan in-place)<br>• Pernyataan 3 BENAR: Hubungan fundamental Queue dan BFS<br>• Pernyataan 4 SALAH: Linked list tidak memiliki akses acak $O(1)$ ke indeks tengah, sehingga Binary Search pada linked list tetap memakan waktu $O(n)$"
    },
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "explanation": "BST In-order menghasilkan urutan terurut menaik. Merge Sort butuh memori tambahan O(n). Queue menerapkan FIFO dan dipakai BFS. Binary Search tidak efisien di Linked List karena tidak ada akses acak O(1) ke elemen tengah. Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
  },
  {
    "id": "inf-sim-33",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & INTERNET",
    "topic": "Lapisan Model OSI, Protokol Transport, dan Pengalamatan IP",
    "statements": [
      {
        "text": "Router bekerja pada Lapisan Jaringan (Layer 3 OSI) dan meneruskan paket data berdasarkan alamat logis IP Address tujuan.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Protokol UDP menjamin paket data tiba secara utuh dan berurutan dengan menyertakan mekanisme konfirmasi ACK dan retransmisi paket rusak.",
        "correct": "Salah",
        "id": "1"
      },
      {
        "text": "Subnet mask /26 pada IPv4 menyediakan total 62 alamat host yang dapat dikonfigurasi secara valid untuk perangkat klien.",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Domain Name System (DNS) menggunakan protokol TCP pada port 53 untuk kueri resolusi nama domain standar dari komputer klien.",
        "correct": "Salah",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Router beroperasi di Layer 3 OSI. UDP tidak memiliki mekanisme ACK dan retransmisi (itu fitur TCP). /26 memiliki 64 - 2 = 62 host valid. DNS query standar menggunakan UDP port 53, bukan TCP.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai protokol jaringan komputer dan internet!",
    "formulaHud": {
      "title": "STANDAR JARINGAN DAN PROTOKOL INTERNET",
      "latex": "\\text{Router (L3 IP)}, \\quad \\text{UDP (Unreliable)}, \\quad \\text{/26} \\implies 2^6 - 2 = 62, \\quad \\text{DNS Query (Port 53 UDP)}",
      "legend": "• Pernyataan 1 BENAR: Router adalah perangkat Layer 3 OSI<br>• Pernyataan 2 SALAH: Mekanisme ACK dan retransmisi adalah milik TCP, bukan UDP<br>• Pernyataan 3 BENAR: Host bits $= 32 - 26 = 6 \\implies 2^6 - 2 = 62$ host valid<br>• Pernyataan 4 SALAH: Kueri standar DNS klien menggunakan UDP port 53 (TCP hanya dipakai untuk zone transfer antar server)"
    },
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "explanation": "Router beroperasi di Layer 3 OSI. UDP tidak memiliki mekanisme ACK dan retransmisi (itu fitur TCP). /26 memiliki 64 - 2 = 62 host valid. DNS query standar menggunakan UDP port 53, bukan TCP. Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
  },
  {
    "id": "inf-sim-34",
    "type": "matrix",
    "materi": "BASIS DATA RELASIONAL & ANALISIS DATA",
    "topic": "Integritas Basis Data, Aturan Normalisasi, dan Eksekusi Kueri SQL",
    "statements": [
      {
        "text": "Kunci Utama (Primary Key) sebuah tabel basis data boleh bernilai NULL selama nilai tersebut tidak berulang dengan baris lain.",
        "correct": "Salah",
        "id": "0"
      },
      {
        "text": "Sebuah tabel relasional dikatakan memenuhi Bentuk Normal Kedua (2NF) jika telah memenuhi 1NF dan tidak memiliki ketergantungan fungsional parsial.",
        "correct": "Benar",
        "id": "1"
      },
      {
        "text": "Klausa WHERE dalam kueri SQL dieksekusi sebelum pengelompokan GROUP BY, sedangkan klausa HAVING dieksekusi setelah pengelompokan GROUP BY.",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Operasi INNER JOIN antara dua tabel selalu mengembalikan jumlah baris yang sama dengan operasi FULL OUTER JOIN.",
        "correct": "Salah",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Primary Key mutlak NOT NULL. 2NF melarang ketergantungan parsial. WHERE memfilter sebelum GROUP BY, HAVING setelahnya. FULL OUTER JOIN menghasilkan baris yang lebih banyak atau sama dengan INNER JOIN.",
      "execution": "Pernyataan 1: Salah; Pernyataan 2: Benar; Pernyataan 3: Benar; Pernyataan 4: Salah."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai perancangan basis data relasional dan analisis SQL!",
    "formulaHud": {
      "title": "PRINSIP BASIS DATA RELASIONAL DAN NORMALISASI",
      "latex": "\\text{PK} \\ne \\text{NULL}, \\quad \\text{2NF} \\implies \\text{No Partial FD}, \\quad \\text{WHERE} \\to \\text{GROUP BY} \\to \\text{HAVING}, \\quad \\text{INNER} \\subseteq \\text{OUTER}",
      "legend": "• Pernyataan 1 SALAH: Primary Key secara mutlak tidak boleh bernilai NULL (Entity Integrity)<br>• Pernyataan 2 BENAR: Definisi baku 2NF<br>• Pernyataan 3 BENAR: Urutan pemrosesan logika kueri SQL<br>• Pernyataan 4 SALAH: FULL OUTER JOIN mengikutsertakan baris yang tidak cocok dari kedua sisi sehingga barisnya hampir selalu lebih banyak daripada INNER JOIN"
    },
    "correctAnswers": {
      "0": false,
      "1": true,
      "2": true,
      "3": false
    },
    "explanation": "Primary Key mutlak NOT NULL. 2NF melarang ketergantungan parsial. WHERE memfilter sebelum GROUP BY, HAVING setelahnya. FULL OUTER JOIN menghasilkan baris yang lebih banyak atau sama dengan INNER JOIN. Pernyataan 1: Salah; Pernyataan 2: Benar; Pernyataan 3: Benar; Pernyataan 4: Salah."
  },
  {
    "id": "inf-sim-35",
    "type": "matrix",
    "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
    "topic": "Prinsip Enkripsi, Integritas Hash, dan Etika Keamanan Informasi",
    "statements": [
      {
        "text": "Pada algoritma kriptografi kunci simetris seperti AES, kunci yang digunakan untuk proses enkripsi identik dengan kunci yang digunakan untuk proses dekripsi.",
        "correct": "Benar",
        "id": "0"
      },
      {
        "text": "Fungsi hash kriptografis seperti SHA-256 dapat didekripsi kembali menjadi teks pesan aslinya jika menggunakan kunci privat yang tepat.",
        "correct": "Salah",
        "id": "1"
      },
      {
        "text": "Tanda Tangan Digital (Digital Signature) dibuat oleh pengirim dengan mengenkripsi hash dokumen menggunakan kunci privat (Private Key) miliknya sendiri.",
        "correct": "Benar",
        "id": "2"
      },
      {
        "text": "Model keamanan Zero Trust mengasumsikan bahwa semua perangkat yang terhubung ke jaringan Wi-Fi internal kantor dapat dipercaya secara otomatis tanpa autentikasi berulang.",
        "correct": "Salah",
        "id": "3"
      }
    ],
    "hints": {
      "concept": "Kriptografi simetris menggunakan kunci yang sama untuk enkripsi dan dekripsi. Fungsi hash bersifat satu arah dan tidak bisa didekripsi. Digital signature dibuat dengan kunci privat pengirim. Zero Trust tidak pernah mempercayai perangkat otomatis.",
      "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
    },
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "questionHtml": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai kriptografi dan keamanan informasi!",
    "formulaHud": {
      "title": "PRINSIP FONDASI KRIPTOGRAFI DAN ZERO TRUST",
      "latex": "\\text{Simetris: } K_{\\text{enc}} = K_{\\text{dec}}, \\quad \\text{Hash: One-Way (No Decryption)}, \\quad \\text{Signature: Encrypt with PrivKey}, \\quad \\text{Zero Trust: Never Trust}",
      "legend": "• Pernyataan 1 BENAR: Ciri khas algoritma kunci simetris<br>• Pernyataan 2 SALAH: Fungsi hash adalah fungsi satu arah (one-way function) dan tidak dapat didekripsi<br>• Pernyataan 3 BENAR: Definisi pembentukan Digital Signature<br>• Pernyataan 4 SALAH: Zero Trust justru berasumsi bahwa jaringan internal TIDAK tepercaya (Never Trust, Always Verify)"
    },
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "explanation": "Kriptografi simetris menggunakan kunci yang sama untuk enkripsi dan dekripsi. Fungsi hash bersifat satu arah dan tidak bisa didekripsi. Digital signature dibuat dengan kunci privat pengirim. Zero Trust tidak pernah mempercayai perangkat otomatis. Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
  }
];
