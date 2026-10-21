# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Informatika (SMA/MA)
Dataset: Latihan Tingkat Easy (25 Authentic Questions, inf-lat-e-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

INFORMATIKA_EASY_ITEMS = [
    {
        "id": "inf-lat-e-01",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Empat Pilar Fondasi Berpikir Komputasional",
        "stem": "Dalam memecahkan permasalahan kompleks sistem antrean rumah sakit yang rumit, seorang analis sistem membagi alur besar menjadi subsistem registrasi, triase pasien, pelayanan poli, dan pembayaran farmasi secara terpisah agar mudah dikaji. Pilar berpikir komputasional yang diterapkan pada langkah pemecahan masalah tersebut adalah...",
        "correct": "Dekomposisi (Decomposition), yaitu teknik memecah masalah besar dan kompleks menjadi bagian-bagian yang lebih kecil, mandiri, dan lebih mudah dikelola.",
        "distractors": [
            "Pengenalan Pola (Pattern Recognition), yaitu mencari kesamaan bentuk tren historis kunjungan pasien antar hari.",
            "Abstraksi (Abstraction), yaitu mengabaikan informasi identitas pasien yang tidak relevan dengan proses triase medis.",
            "Desain Algoritma (Algorithm Design), yaitu menyusun langkah-langkah komputasi otomatis tanpa menguraikan struktur masalah.",
            "Generalisasi Komputasi, yaitu menerapkan solusi algoritma yang sama secara membabi buta tanpa modifikasi modul."
        ],
        "formula": {
            "title": "4 PILAR BERPIKIR KOMPUTASIONAL (BK)",
            "latex": "\\text{Masalah Kompleks} \\xrightarrow{\\text{Dekomposisi}} \\sum \\text{Sub-Masalah} \\xrightarrow{\\text{Abstraksi}} \\text{Model Sederhana} \\xrightarrow{\\text{Algoritma}} \\text{Solusi}",
            "legend": "• Dekomposisi: Memecah masalah kompleks menjadi komponen kecil terisolasi<br>• Pengenalan Pola: Mengidentifikasi kesamaan karakteristik/alur<br>• Abstraksi: Fokus pada informasi esensial dan mengeliminasi detail sepele<br>• Algoritma: Langkah terurut logis penyelesaian masalah"
        },
        "hints": {
            "concept": "Membagi masalah besar menjadi bagian-bagian kecil adalah definisi dekomposisi.",
            "execution": "Pilih: Dekomposisi (Decomposition)."
        }
    },
    {
        "id": "inf-lat-e-02",
        "materi": "SISTEM KOMPUTER",
        "topic": "Siklus Kerja Utama Central Processing Unit (CPU)",
        "stem": "Mikroprosesor komputer mengeksekusi instruksi program perangkat lunak melalui siklus mesin yang berulang secara terus-menerus. Urutan tahapan fundamental dalam siklus instruksi CPU yang benar adalah...",
        "correct": "Fetch (mengambil kode instruksi dari RAM ke register) $\\rightarrow$ Decode (menerjemahkan kode operasi oleh Control Unit) $\\rightarrow$ Execute (mengeksekusi operasi pada ALU) $\\rightarrow$ Store (menulis hasil kembali ke register/memori).",
        "distractors": [
            "Decode $\\rightarrow$ Fetch $\\rightarrow$ Store $\\rightarrow$ Interrupt $\\rightarrow$ Execute.",
            "Compile $\\rightarrow$ Link $\\rightarrow$ Load $\\rightarrow$ Execute $\\rightarrow$ Terminate.",
            "Store $\\rightarrow$ ALU Compute $\\rightarrow$ Fetch $\\rightarrow$ Cache $\\rightarrow$ Decode.",
            "Interrupt $\\rightarrow$ Paging $\\rightarrow$ Context Switch $\\rightarrow$ Decode $\\rightarrow$ Fetch."
        ],
        "formula": {
            "title": "SIKLUS INSTRUKSI MESIN VON NEUMANN",
            "latex": "\\text{PC} \\xrightarrow{\\text{Fetch}} \\text{IR} \\xrightarrow{\\text{Decode (CU)}} \\text{ALU Operations} \\xrightarrow{\\text{Execute}} \\text{Register/RAM (Store)}",
            "legend": "• PC (Program Counter): Menyimpan alamat memori instruksi berikutnya<br>• IR (Instruction Register): Menyimpan kode instruksi aktif saat ini<br>• CU (Control Unit): Mendekode sinyal kendali mikroprosesor<br>• ALU (Arithmetic Logic Unit): Melakukan kalkulasi aritmetika dan logika"
        },
        "hints": {
            "concept": "Siklus instruksi mesin CPU standar: Ambil (Fetch) -> Terjemahkan (Decode) -> Jalankan (Execute) -> Simpan (Store).",
            "execution": "Pilih opsi: Fetch -> Decode -> Execute -> Store."
        }
    },
    {
        "id": "inf-lat-e-03",
        "materi": "STRUKTUR DATA",
        "topic": "Prinsip Mekanisme Akses Data Stack vs Queue",
        "stem": "Fitur tombol Undo/Redo pada pengolah kata teks dan tombol navigasi Back pada peramban web bekerja berdasarkan mekanisme struktur data yang melayani elemen data terakhir dimasukkan sebagai elemen pertama yang diproses. Struktur data yang menerapkan mekanisme tersebut adalah...",
        "correct": "Stack (Tumpukan) dengan prinsip LIFO (Last-In, First-Out), di mana operasi penambahan (push) dan penghapusan (pop) hanya dapat dilakukan pada satu ujung puncak (top).",
        "distractors": [
            "Queue (Antrean) dengan prinsip FIFO (First-In, First-Out), di mana elemen pertama masuk akan diproses pertama kali.",
            "Priority Queue, di mana setiap elemen data wajib memiliki bobot prioritas bilangan bulat sebelum dialokasikan.",
            "Circular Linked List, di mana simpul terakhir selalu menunjuk kembali ke simpul awal tanpa ada titik akhir.",
            "Binary Search Tree, di mana data diurutkan berdasarkan perbandingan nilai kunci simpul induk dan cabang."
        ],
        "formula": {
            "title": "KOMPARASI STRUKTUR DATA LINEAR",
            "latex": "\\begin{aligned} \\text{Stack (LIFO):} & \\quad \\text{Elemen Masuk Terakhir} \\iff \\text{Elemen Keluar Pertama (Top)} \\\\ \\text{Queue (FIFO):} & \\quad \\text{Elemen Masuk Pertama (Rear)} \\iff \\text{Elemen Keluar Pertama (Front)} \\end{aligned}",
            "legend": "• Stack: Undo/Redo, Call Stack fungsi rekursif, evaluasi notasi Postfix<br>• Queue: Antrean spooler printer, penjadwalan proses CPU Round-Robin, algoritma BFS"
        },
        "hints": {
            "concept": "Undo/Redo dan Back browser membalik urutan langkah terakhir, menggunakan prinsip Last-In First-Out (LIFO), yaitu Stack.",
            "execution": "Pilih: Stack (Tumpukan) dengan prinsip LIFO."
        }
    },
    {
        "id": "inf-lat-e-04",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Hierarki dan Peran Lapisan Model Referensi OSI",
        "stem": "Dalam model referensi 7 Lapisan OSI (Open Systems Interconnection), lapisan yang bertanggung jawab untuk menentukan rute logis terbaik pengiriman paket data antar jaringan yang berbeda melalui pengalamatan logis (IP Address) adalah...",
        "correct": "Network Layer (Lapisan 3), yang mengelola routing paket data dan logical addressing menggunakan protokol IP (Internet Protocol).",
        "distractors": [
            "Data Link Layer (Lapisan 2), yang menangani framing fisik dan physical addressing berupa MAC Address lokal.",
            "Transport Layer (Lapisan 4), yang menyediakan komunikasi end-to-end dengan segmentasi data TCP/UDP.",
            "Physical Layer (Lapisan 1), yang mentransmisikan bit-bit biner mentah melalui media transmisi kabel atau nirkabel.",
            "Session Layer (Lapisan 5), yang membuka, mengelola, dan mengakhiri sesi dialog antar aplikasi jaringan."
        ],
        "formula": {
            "title": "ENKAPSULASI 7 LAPISAN MODEL OSI",
            "latex": "\\text{App (L7)} \\to \\text{Pres (L6)} \\to \\text{Sess (L5)} \\to \\text{Trans (Segmen/L4)} \\to \\text{Net (Paket/L3)} \\to \\text{DataLink (Frame/L2)} \\to \\text{Phys (Bit/L1)}",
            "legend": "• L3 (Network): Router, IP Address, ICMP, Paket data<br>• L2 (Data Link): Switch, MAC Address, Frame data<br>• L4 (Transport): Port, TCP/UDP, Segmen data, Flow control"
        },
        "hints": {
            "concept": "IP Address dan pemilihan rute (routing) bekerja di Lapisan ke-3, yaitu Network Layer.",
            "execution": "Pilih: Network Layer (Lapisan 3)."
        }
    },
    {
        "id": "inf-lat-e-05",
        "materi": "ANALISIS DATA",
        "topic": "Karakteristik Kunci Utama (Primary Key) Basis Data Relasional",
        "stem": "Dalam perancangan basis data relasional untuk sistem akademik sekolah, entitas siswa memiliki beberapa atribut: `NISN`, `Nama_Lengkap`, `Tanggal_Lahir`, dan `Alamat`. Alasan paling fundamental mengapa atribut `NISN` dipilih sebagai Primary Key adalah...",
        "correct": "Atribut `NISN` menjamin nilai yang unik bagi setiap baris rekaman siswa dan secara mutlak tidak boleh bernilai kosong (NOT NULL).",
        "distractors": [
            "Atribut `NISN` memiliki panjang karakter teks paling pendek sehingga mempercepat proses backup hard disk.",
            "Atribut `NISN` dapat diubah nilainya sewaktu-waktu oleh pengguna tanpa memengaruhi relasi tabel lainnya.",
            "Atribut `NISN` otomatis mengurutkan nama siswa sesuai abjad alfabet dari huruf A sampai Z secara fisik.",
            "Atribut `NISN` merupakan tipe data numerik yang wajib dapat dijumlahkan dan dihitung nilai rata-ratanya."
        ],
        "formula": {
            "title": "SYARAT KEABSAHAN PRIMARY KEY BASIS DATA",
            "latex": "\\forall x, y \\in T: \\quad x \\neq y \\implies \\text{PK}(x) \\neq \\text{PK}(y) \\quad \\land \\quad \\text{PK}(x) \\neq \\text{NULL}",
            "legend": "• Entity Integrity Constraint: Kunci utama wajib unik dan tidak boleh kosong (NOT NULL)<br>• Foreign Key: Kunci tamu yang mereferensikan Primary Key dari tabel induk untuk menjaga integritas referensial"
        },
        "hints": {
            "concept": "Syarat mutlak Primary Key (PK): Unik untuk setiap rekaman dan tidak boleh bernilai NULL (NOT NULL).",
            "execution": "Pilih: Menjamin nilai yang unik dan tidak boleh bernilai kosong (NOT NULL)."
        }
    },
    {
        "id": "inf-lat-e-06",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Kompleksitas Asimtotik Algoritma Pencarian Biner",
        "stem": "Sebuah larik data (array) berisi 1.024 elemen bilangan bulat yang telah terurut rapi secara menaik (sorted ascending). Jika dilakukan pencarian suatu elemen menggunakan algoritma Binary Search, jumlah perbandingan maksimum (worst case) yang dibutuhkan hingga elemen ditemukan atau dipastikan tidak ada adalah...",
        "correct": "11 kali perbandingan, karena kompleksitas pencarian biner adalah $O(\\log_2 n)$ sehingga $\\lfloor \\log_2(1024) \\rfloor + 1 = 10 + 1 = 11$.",
        "distractors": [
            "1.024 kali perbandingan, karena algoritma harus memeriksa setiap elemen dari indeks pertama hingga terakhir.",
            "512 kali perbandingan, karena algoritma membagi array menjadi dua bagian dan memeriksa seluruh separuh array.",
            "1 kali perbandingan, karena data sudah terurut sehingga elemen langsung terdeteksi pada percobaan pertama.",
            "100 kali perbandingan, sesuai dengan kapasitas memori buffer prosesor komputer."
        ],
        "formula": {
            "title": "KOMPLEKSITAS PENCARIAN BINER (BINARY SEARCH)",
            "latex": "T_{\\text{worst}}(n) = \\lfloor \\log_2 n \\rfloor + 1, \\quad \\text{Untuk } n = 1024 = 2^{10} \\implies 10 + 1 = 11 \\text{ perbandingan}",
            "legend": "• Linear Search: Kompleksitas $O(n)$, membutuhkan hingga $n$ perbandingan<br>• Binary Search: Kompleksitas $O(\\log n)$, syarat mutlak data harus sudah terurut"
        },
        "hints": {
            "concept": "Binary search membagi ruang pencarian menjadi setengah pada setiap langkah: log2(1024) = 10 pembagian, maksimal 11 perbandingan.",
            "execution": "Hitung: log2(1024) + 1 = 11 kali."
        }
    },
    {
        "id": "inf-lat-e-07",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Triad Keamanan Informasi (CIA Triad)",
        "stem": "Dalam manajemen keamanan informasi (Information Security), pilar CIA Triad menjadi standar evaluasi proteksi sistem. Jika seorang peretas berhasil menyadap pesan surel rahasia perusahaan yang sedang dikirimkan melalui internet karena pesan tersebut tidak dienkripsi, aspek keamanan yang telah dilanggar adalah...",
        "correct": "Kerahasiaan (Confidentiality), yaitu jaminan bahwa informasi hanya dapat diakses, dibaca, dan disingkap oleh pihak yang berhak dan memiliki otorisasi sah.",
        "distractors": [
            "Integritas (Integrity), yaitu jaminan bahwa data tidak mengalami manipulasi, perubahan, atau perusakan oleh pihak tidak berhak.",
            "Ketersediaan (Availability), yaitu jaminan bahwa sistem dan data dapat diakses oleh pengguna yang berwenang kapan pun dibutuhkan.",
            "Non-Repudiation, yaitu mekanisme pembuktian bahwa pengirim tidak dapat menyangkal telah mengirimkan pesan.",
            "Akuntabilitas (Accountability), yaitu pencatatan jejak audit aktivitas pengguna ke dalam berkas log sistem."
        ],
        "formula": {
            "title": "PILAR UTAMA CIA TRIAD",
            "latex": "\\text{Keamanan Informasi} \\equiv \\text{Confidentiality (Kerahasiaan)} \\cap \\text{Integrity (Keutuhan)} \\cap \\text{Availability (Ketersediaan)}",
            "legend": "• Confidentiality terancam oleh: Sniffing, pembobolan kata sandi, pencurian berkas<br>• Integrity terancam oleh: Man-in-the-Middle (MitM), injeksi data palsu, perusakan virus<br>• Availability terancam oleh: Serangan DDoS, ransomware, pemadaman listrik/server"
        },
        "hints": {
            "concept": "Penyadapan data rahasia tanpa izin melanggar pilar Kerahasiaan (Confidentiality).",
            "execution": "Pilih: Kerahasiaan (Confidentiality)."
        }
    },
    {
        "id": "inf-lat-e-08",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Rentang Pengalamatan IPv4 Privat Menurut RFC 1918",
        "stem": "Untuk mencegah kehabisan alamat IPv4 global di internet, IETF menerbitkan dokumen RFC 1918 yang menetapkan blok alamat IP Privat yang tidak dapat dirutekan langsung di jaringan internet publik (non-routable). Manakah di antara alamat IP berikut yang tergolong sebagai alamat IPv4 Privat kelas C?",
        "correct": "`192.168.1.50`, karena berada di dalam rentang alamat privat blok `192.168.0.0` sampai `192.168.255.255` (prefix `/16`).",
        "distractors": [
            "`172.35.10.1`, karena berada di luar rentang privat kelas B yang dibatasi hingga `172.31.255.255`.",
            "`10.0.0.1`, karena alamat ini merupakan blok alamat IP privat Kelas A murni bukan Kelas C.",
            "`8.8.8.8`, karena alamat ini merupakan DNS server publik milik Google yang dapat dirutekan secara global.",
            "`127.0.0.1`, karena alamat ini dicadangkan secara khusus sebagai antarmuka Loopback lokal sistem komputer."
        ],
        "formula": {
            "title": "RENTANG BLOK IPV4 PRIVAT (RFC 1918)",
            "latex": "\\begin{aligned} \\text{Kelas A:} & \\quad 10.0.0.0 - 10.255.255.255 \\quad (/8) \\\\ \\text{Kelas B:} & \\quad 172.16.0.0 - 172.31.255.255 \\quad (/12) \\\\ \\text{Kelas C:} & \\quad 192.168.0.0 - 192.168.255.255 \\quad (/16) \\end{aligned}",
            "legend": "• Loopback address: 127.0.0.0/8 (127.0.0.1 localhost)<br>• APIPA (Automatic Private IP): 169.254.0.0/16<br>• IP Privat wajib ditranslasikan melalui NAT (Network Address Translation) untuk mengakses internet"
        },
        "hints": {
            "concept": "Blok IP privat kelas C adalah 192.168.0.0 s.d. 192.168.255.255.",
            "execution": "Pilih: 192.168.1.50."
        }
    },
    {
        "id": "inf-lat-e-09",
        "materi": "SISTEM KOMPUTER",
        "topic": "Hierarki Memori dan Karakteristik Cache Memory",
        "stem": "Dalam arsitektur komputer modern, hierarki memori dirancang bertingkat mulai dari Register, Cache (L1, L2, L3), RAM utama, hingga Secondary Storage (SSD/HDD). Peran mendasar dari Cache Memory dalam hierarki tersebut adalah...",
        "correct": "Menjembatani perbedaan kecepatan operasi yang sangat timpang antara prosesor yang super cepat dan RAM utama yang relatif lebih lambat dengan menyimpan salinan data dan instruksi yang sering diakses.",
        "distractors": [
            "Menyimpan data arsip jangka panjang secara permanen saat komputer dimatikan (non-volatile storage).",
            "Menggantikan fungsi sistem operasi dalam melakukan manajemen berkas dan penjadwalan antrean I/O.",
            "Mendinginkan suhu sirkuit mikroprosesor dengan menyerap panas berlebih melalui semikonduktor termal.",
            "Menambah kapasitas total ruang penyimpanan sekunder komputer tanpa memerlukan penambahan modul SSD fisik."
        ],
        "formula": {
            "title": "HIERARKI MEMORI KOMPUTER",
            "latex": "\\text{Kecepatan} \\uparrow, \\text{Biaya} \\uparrow, \\text{Kapasitas} \\downarrow : \\quad \\text{Register} > \\text{L1 Cache} > \\text{L2 Cache} > \\text{L3 Cache} > \\text{RAM} > \\text{SSD} > \\text{HDD}",
            "legend": "• Cache Hit: Data yang dicari CPU tersedia di cache memory (latensi rendah)<br>• Cache Miss: Data tidak ditemukan di cache, CPU harus mengambil dari RAM utama (latensi tinggi)<br>• Prinsip Locality of Reference: Temporal Locality & Spatial Locality"
        },
        "hints": {
            "concept": "Cache memori berbahan SRAM berfungsi menutupi gap kecepatan (von Neumann bottleneck) antara CPU dan RAM.",
            "execution": "Pilih: Menjembatani perbedaan kecepatan antara prosesor dan RAM utama."
        }
    },
    {
        "id": "inf-lat-e-10",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Evaluasi Logika Kondisional Boolean",
        "stem": "Diberikan cuplikan kode program logika komputasi sederhana berikut:\n```python\na = 15\nb = 20\nc = 5\nhasil = (a + c >= b) and not (b % a == 0 or c * 3 > a)\n```\nNilai boolean akhir yang tersimpan di dalam variabel `hasil` setelah kode dieksekusi adalah...",
        "correct": "`True`, karena sub-kondisi pertama `(a + c >= b)` bernilai `True` ($20 \\ge 20$), sub-kondisi di dalam tanda kurung `(b % a == 0 or c * 3 > a)` bernilai `False` ($5 == 0$ bernilai `False` dan $15 > 15$ bernilai `False`), sehingga negasinya `not (False)` bernilai `True`, dan evaluasi akhir `True and True` menghasilkan `True`.",
        "distractors": [
            "`False`, karena operator logika `not` membalik seluruh hasil ekspresi awal menjadi bernilai salah secara mutlak.",
            "`SyntaxError`, karena penulisan operator modulus `%` tidak dapat digabungkan dengan operator perbandingan dan boolean dalam satu baris.",
            "`None`, karena operasi perbandingan majemuk tidak mengembalikan tipe data primitif jika tidak diberi klausa `else` eksplisit.",
            "`TypeError`, karena variabel integer tidak dapat dievaluasi bersama konstanta boolean tanpa fungsi konversi tipe `bool()`."
        ],
        "formula": {
            "title": "TABEL KEBENARAN LOGIKA OPERATOR BOOLEAN",
            "latex": "P \\land \\neg(Q \\lor R): \\quad (15+5 \\ge 20) = \\text{True}, \\quad (20 \\pmod{15} = 5 \\ne 0) = \\text{False}, \\quad (15 > 15) = \\text{False} \\implies \\text{True} \\land \\neg(\\text{False}) = \\text{True}",
            "legend": "• a + c = 20 >= 20 -> True<br>• b % a = 20 % 15 = 5 == 0 -> False<br>• c * 3 = 15 > 15 -> False<br>• False or False -> False; not False -> True; True and True -> True"
        },
        "hints": {
            "concept": "Evaluasi bertahap: 1) a+c >= b (20 >= 20: True). 2) 20 % 15 == 0 (False). 3) 5*3 > 15 (False). False or False = False. not(False) = True. True and True = True.",
            "execution": "Nilai akhir adalah True."
        }
    },
    {
        "id": "inf-lat-e-11",
        "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
        "topic": "Fungsi Pencarian Referensi Spreadsheet VLOOKUP vs XLOOKUP",
        "stem": "Dalam aplikasi lembar sebar (spreadsheet) seperti Microsoft Excel atau Google Sheets, seorang staf tata usaha ingin mencari gaji pokok pegawai berdasarkan `ID_Pegawai` dari tabel referensi master. Karakteristik utama dari fungsi `=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])` adalah...",
        "correct": "Hanya mampu mencari nilai kecocokan (`lookup_value`) pada kolom paling kiri (kolom pertama) dari rentang tabel referensi, lalu mengambil data dari kolom di sebelah kanannya.",
        "distractors": [
            "Mampu mencari nilai kecocokan pada sembarang kolom dan secara bebas mengambil data dari kolom sebelah kirinya tanpa batas.",
            "Otomatis menjumlahkan seluruh nilai numerik yang cocok dengan kriteria tanpa memerlukan fungsi SUMIF tambahan.",
            "Hanya dapat digunakan untuk mencocokkan data bertipe tanggal kalender dan tidak dapat memproses teks alfabetik.",
            "Wajib menyortir data master secara menurun (descending) sebelum rumus pencarian dapat dieksekusi tanpa galat."
        ],
        "formula": {
            "title": "SINTAKSIS FORMULA PENCARIAN SPREADSHEET",
            "latex": "\\text{VLOOKUP}(K, A, c, \\text{FALSE}) \\implies \\text{Cari } K \\text{ pada } A_{*, 1}, \\text{ Ambil nilai pada kolom ke-} c",
            "legend": "• Keterbatasan VLOOKUP klasik: Kunci pencarian wajib di kolom 1 (paling kiri)<br>• XLOOKUP (Modern) / INDEX-MATCH: Mengatasi limitasi VLOOKUP, mampu mencari ke arah kiri dan vertikal/horizontal fleksibel"
        },
        "hints": {
            "concept": "VLOOKUP (Vertical Lookup) secara fundamental hanya mencari kunci pada kolom pertama tabel referensi dan mengembalikan nilai ke arah kanan.",
            "execution": "Pilih: Hanya mampu mencari nilai pada kolom paling kiri dari rentang tabel."
        }
    },
    {
        "id": "inf-lat-e-12",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Representasi Graf Sederhana dan Derajat Simpul",
        "stem": "Sebuah jaringan pertemanan media sosial dimodelkan sebagai graf tak berarah (undirected graph) $G = (V, E)$, di mana $V = \\{A, B, C, D, E\\}$ merepresentasikan orang dan $E = \\{(A,B), (A,C), (B,C), (B,D), (C,D), (D,E)\\}$ merepresentasikan hubungan pertemanan. Simpul (vertex) yang memiliki derajat pertemanan (degree) tertinggi adalah...",
        "correct": "Simpul $B$ dan $C$, keduanya memiliki derajat 3 karena masing-masing terhubung langsung dengan tiga sisi pertemanan.",
        "distractors": [
            "Simpul $A$, karena berada di urutan alfabet pertama dan terhubung dengan seluruh simpul lainnya.",
            "Simpul $D$, karena merupakan satu-satunya jembatan (bridge) yang menghubungkan simpul $E$ ke jaringan.",
            "Simpul $E$, karena memiliki derajat pertemanan tertinggi sebesar 4 sisi langsung.",
            "Seluruh simpul memiliki derajat yang persis sama sebesar 2 sisi pertemanan reguler."
        ],
        "formula": {
            "title": "DERAJAT SIMPUL GRAF TAK BERARAH",
            "latex": "\\text{deg}(v) = |\\{e \\in E : v \\in e\\}|, \\quad \\sum_{v \\in V} \\text{deg}(v) = 2|E| = 2(6) = 12",
            "legend": "• Hubungan simpul: A terhubung ke B, C (deg = 2)<br>• B terhubung ke A, C, D (deg = 3)<br>• C terhubung ke A, B, D (deg = 3)<br>• D terhubung ke B, C, E (deg = 3)<br>• E terhubung ke D (deg = 1)<br>• B, C, dan D masing-masing memiliki derajat 3 (tertinggi)"
        },
        "hints": {
            "concept": "Hitung jumlah koneksi per simpul: A:2, B:3, C:3, D:3, E:1. Jadi B, C, dan D berderajat 3.",
            "execution": "Pilih opsi yang menyatakan simpul dengan derajat 3 sebagai simpul berderajat tertinggi."
        }
    },
    {
        "id": "inf-lat-e-13",
        "materi": "ANALISIS DATA",
        "topic": "Pengelompokan dan Agregasi Query SQL Dasar",
        "stem": "Diberikan tabel basis data `Penjualan` dengan kolom `kategori_produk`, `nama_produk`, dan `jumlah_terjual`. Perintah SQL yang tepat untuk menampilkan setiap kategori produk beserta total unit yang berhasil terjual di setiap kategori tersebut adalah...",
        "correct": "`SELECT kategori_produk, SUM(jumlah_terjual) FROM Penjualan GROUP BY kategori_produk;`",
        "distractors": [
            "`SELECT kategori_produk, COUNT(jumlah_terjual) FROM Penjualan WHERE SUM(jumlah_terjual) > 0;`",
            "`SELECT DISTINCT kategori_produk, jumlah_terjual FROM Penjualan ORDER BY kategori_produk;`",
            "`SELECT kategori_produk, AVG(jumlah_terjual) FROM Penjualan HAVING kategori_produk IS NOT NULL;`",
            "`SELECT TOTAL(jumlah_terjual) IN Penjualan GROUPED BY kategori_produk;`"
        ],
        "formula": {
            "title": "SINTAKSIS KLAUSA AGREGASI BASIS DATA SQL",
            "latex": "\\text{SELECT } C, \\text{ AGG}(V) \\text{ FROM } T \\text{ GROUP BY } C \\text{ [HAVING kondisi]};",
            "legend": "• SUM(): Menghitung total akumulasi nilai numerik<br>• GROUP BY: Mengelompokkan baris berdasarkan nilai kolom penentu<br>• WHERE memfilter sebelum agregasi, sedangkan HAVING memfilter setelah agregasi"
        },
        "hints": {
            "concept": "Untuk menghitung total unit per kategori, gunakan fungsi SUM(jumlah_terjual) dan klausul GROUP BY kategori_produk.",
            "execution": "Pilih: SELECT kategori_produk, SUM(jumlah_terjual) FROM Penjualan GROUP BY kategori_produk;"
        }
    },
    {
        "id": "inf-lat-e-14",
        "materi": "SISTEM KOMPUTER",
        "topic": "Konversi Sistem Bilangan Biner ke Desimal",
        "stem": "Sebuah nilai biner 8-bit tanpa tanda (unsigned 8-bit binary) yang tersimpan di dalam register prosesor adalah `10110010_2`. Nilai representasi bilangan tersebut dalam sistem desimal berbasis 10 adalah...",
        "correct": "$178_{10}$, hasil dari $1\\cdot 2^7 + 0\\cdot 2^6 + 1\\cdot 2^5 + 1\\cdot 2^4 + 0\\cdot 2^3 + 0\\cdot 2^2 + 1\\cdot 2^1 + 0\\cdot 2^0 = 128 + 32 + 16 + 2 = 178$.",
        "distractors": [
            "$162_{10}$, hasil penjumlahan dari bit-bit aktif tanpa memperhitungkan bobot pangkat kelipatan dua.",
            "$194_{10}$, hasil konversi dengan membalik nilai bit terendah (least significant bit).",
            "$146_{10}$, hasil konversi kesalahan membaca bit pembobot orde ketiga dan keempat.",
            "$210_{10}$, hasil interpretasi langsung digit biner sebagai bilangan oktal desimal."
        ],
        "formula": {
            "title": "KONVERSI BILANGAN BINER KE DESIMAL",
            "latex": "N_{10} = \\sum_{i=0}^{n-1} b_i \\cdot 2^i = 128 + 0 + 32 + 16 + 0 + 0 + 2 + 0 = 178_{10}",
            "legend": "• Bit posisi: b7=1 (128), b6=0 (0), b5=1 (32), b4=1 (16), b3=0 (0), b2=0 (0), b1=1 (2), b0=0 (0)<br>• Total desimal: 128 + 32 + 16 + 2 = 178"
        },
        "hints": {
            "concept": "Jumlahkan bobot pangkat dua: bit ke-7 (128) + bit ke-5 (32) + bit ke-4 (16) + bit ke-1 (2) = 178.",
            "execution": "Pilih: 178."
        }
    },
    {
        "id": "inf-lat-e-15",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Perbandingan Karakteristik Protokol TCP vs UDP",
        "stem": "Aplikasi streaming video langsung (live streaming) dan panggilan suara interaktif VoIP umumnya lebih memilih menggunakan protokol UDP (User Datagram Protocol) daripada TCP (Transmission Control Protocol). Alasan teknis utama di balik pemilihan tersebut adalah...",
        "correct": "UDP bersifat connectionless dan meminimalkan latensi tunda (overhead rendah) tanpa mekanisme handshaking dan retransmisi paket yang hilang, sehingga transmisi real-time berjalan lancar.",
        "distractors": [
            "UDP menjamin 100% data pasti sampai secara utuh dan berurutan tanpa ada satu bit pun yang rusak.",
            "UDP secara otomatis mengenkripsi seluruh muatan data menggunakan algoritma AES-256 tingkat militer.",
            "UDP menggunakan jalur transmisi fisik gelombang radio terpisah yang kebal terhadap kemacetan kabel optik.",
            "TCP dilarang oleh konsorsium web internasional untuk mentransmisikan data multimedia grafis."
        ],
        "formula": {
            "title": "KOMPARASI PROTOKOL TRANSPORT (LAYER 4)",
            "latex": "\\begin{aligned} \\text{TCP:} & \\quad \\text{Connection-oriented}, \\ 3\\text{-way Handshake}, \\ \\text{Reliable (Retransmisi)}, \\ \\text{Latensi Tinggi} \\\\ \\text{UDP:} & \\quad \\text{Connectionless}, \\ \\text{No Handshake}, \\ \\text{Unreliable (Best Effort)}, \\ \\text{Latensi Super Rendah} \\end{aligned}",
            "legend": "• TCP cocok untuk: Web browsing (HTTP/HTTPS), email (SMTP/IMAP), transfer berkas (FTP)<br>• UDP cocok untuk: Live video streaming, gaming online kompetitif, DNS query, VoIP"
        },
        "hints": {
            "concept": "UDP dipilih untuk live streaming karena rendah latensi (overhead kecil tanpa retransmisi paket rusak).",
            "execution": "Pilih: UDP connectionless dan meminimalkan latensi tanpa retransmisi."
        }
    },
    {
        "id": "inf-lat-e-16",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Fungsi Rekursif dan Peran Vital Base Case",
        "stem": "Dalam pemrograman, sebuah fungsi rekursif memanggil dirinya sendiri secara berulang. Bagian terpenting yang wajib didefinisikan di awal fungsi rekursif untuk mencegah program mengalami galat kehabisan memori (_Stack Overflow_) adalah...",
        "correct": "Base Case (Kondisi Basis), yaitu kondisi pemberhentian eksplisit yang menghentikan rantai pemanggilan rekursif dan mengembalikan nilai konstan.",
        "distractors": [
            "Recursive Step, yaitu pernyataan baris kode yang memanggil kembali nama fungsi dengan parameter membesar.",
            "Global Variable, yaitu deklarasi variabel di luar lingkup fungsi untuk menampung riwayat iterasi.",
            "Looping While, yaitu sintaksis perulangan bersarang yang memaksa fungsi keluar dari memori secara paksa.",
            "Exception Handler, yaitu blok kode try-catch untuk menangani kegagalan eksekusi compiler sistem."
        ],
        "formula": {
            "title": "STRUKTUR UMUM ALGORITMA REKURSIF",
            "latex": "f(n) = \\begin{cases} \\text{Nilai Konstan} & \\text{jika } n \\le \\text{kondisi\\_basis (Base Case)} \\\\ f(n - 1) + g(n) & \\text{jika } n > \\text{kondisi\\_basis (Recursive Case)} \\end{cases}",
            "legend": "• Tanpa Base Case: Call stack akan terus bertambah hingga batas memori terlampaui (Stack Overflow)<br>• Setiap panggilan rekursif harus memodifikasi argumen menuju ke arah kondisi basis"
        },
        "hints": {
            "concept": "Kondisi penghenti pemanggilan rekursif disebut Base Case.",
            "execution": "Pilih: Base Case (Kondisi Basis)."
        }
    },
    {
        "id": "inf-lat-e-17",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Ancaman Kejahatan Siber Rekayasa Sosial (Social Engineering)",
        "stem": "Seorang pegawai kantor menerima surel palsu yang mengatasnamakan manajer bank resmi dan mendesaknya untuk segera mengklik tautan formulir agar rekening tabungannya tidak diblokir. Serangan siber manipulasi psikologis manusia semacam ini diklasifikasikan sebagai...",
        "correct": "Phishing, yaitu bentuk rekayasa sosial yang berupaya memancing korban untuk membocorkan informasi kredensial sensitif dengan menyamar sebagai institusi tepercaya.",
        "distractors": [
            "Distributed Denial of Service (DDoS), yaitu membanjiri server korban dengan jutaan permintaan palsu hingga tumbang.",
            "SQL Injection, yaitu menyisipkan kode kueri manipulatif ke dalam kolom formulir masukan web aplikasi.",
            "Cross-Site Scripting (XSS), yaitu menyuntikkan skrip berbahaya ke dalam halaman peramban pengguna lain.",
            "Ransomware, yaitu mengeksekusi enkripsi sepihak terhadap seluruh berkas komputer korban demi tebusan uang."
        ],
        "formula": {
            "title": "TAKSONOMI SERANGAN REKAYASA SOSIAL (SOCIAL ENGINEERING)",
            "latex": "\\text{Social Engineering} \\implies \\text{Manipulasi Psikologis (Urgensi/Ketakutan)} \\to \\text{Pencurian Identitas/Kredensial}",
            "legend": "• Phishing: Serangan massal via surel palsu<br>• Spear Phishing: Serangan terarah ke individu/eksekutif tertentu<br>• Smishing / Vishing: Phishing via SMS / panggilan suara<br>• Mitigasi: Verifikasi domain alamat pengirim dan aktifkan MFA (Multi-Factor Authentication)"
        },
        "hints": {
            "concept": "Menyamar sebagai pihak tepercaya via email palsu untuk mencuri data pribadi adalah Phishing.",
            "execution": "Pilih: Phishing."
        }
    },
    {
        "id": "inf-lat-e-18",
        "materi": "STRUKTUR DATA",
        "topic": "Karakteristik Traversal In-Order pada Binary Search Tree (BST)",
        "stem": "Diberikan sebuah Pohon Pencarian Biner (Binary Search Tree / BST) yang valid. Jika dilakukan penelusuran simpul dengan metode traversal In-Order (Kiri $\\rightarrow$ Akar $\\rightarrow$ Kanan), barisan data simpul yang dicetak akan selalu memiliki sifat...",
        "correct": "Terurut menaik (ascending) secara monotonik dari nilai simpul terkecil hingga simpul terbesar.",
        "distractors": [
            "Terurut menurun (descending) dimulai dari simpul daun terbesar menuju simpul akar.",
            "Tercetak berdasarkan urutan kronologis waktu penyisipan simpul data ke dalam memori komputer.",
            "Tercetak tingkat demi tingkat (level by level) dari kedalaman pohon paling atas ke bawah.",
            "Acak tidak berpola karena struktur pohon biner bersifat dinamis dan non-sekuensial."
        ],
        "formula": {
            "title": "TRAVERSAL POHON BINER PENCARIAN (BST)",
            "latex": "\\text{In-Order}(\\text{BST}) = \\text{In-Order}(\\text{Left}) \\cup \\{\\text{Root}\\} \\cup \\text{In-Order}(\\text{Right}) \\implies \\text{Sorted Ascending}",
            "legend": "• Sifat dasar BST: Semua kunci di Subtree Kiri < Kunci Akar < Semua kunci di Subtree Kanan<br>• Pre-Order: Root -> Left -> Right (berguna untuk duplikasi struktur pohon)<br>• Post-Order: Left -> Right -> Root (berguna untuk pembebasan memori / kalkulasi postfix)"
        },
        "hints": {
            "concept": "In-Order pada BST (Kiri < Akar < Kanan) otomatis menghasilkan barisan terurut menaik (sorted ascending).",
            "execution": "Pilih: Terurut menaik (ascending) dari nilai terkecil hingga terbesar."
        }
    },
    {
        "id": "inf-lat-e-19",
        "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
        "topic": "Fitur Otomasi Surat Massal Mail Merge",
        "stem": "Dalam aplikasi pengolah dokumen perkantoran, staf administrasi diminta mencetak 500 lembar surat undangan resmi yang memiliki format teks identik namun nama penerima, nomor induk, dan alamatnya berbeda-beda untuk tiap orang. Fitur aplikasi yang paling tepat dan efisien digunakan adalah...",
        "correct": "Mail Merge, yang mengintegrasikan dokumen template master dengan sumber data eksternal (tabel spreadsheet atau basis data) untuk menghasilkan dokumen personal secara otomatis.",
        "distractors": [
            "Track Changes, yang melacak riwayat suntingan dan catatan revisi antar beberapa editor dokumen.",
            "AutoCorrect, yang otomatis memperbaiki kesalahan ketik ejaan kata sesuai kamus tata bahasa.",
            "Hyperlink Embedding, yang menyematkan tautan pranala web ke dalam teks surat undangan fisik.",
            "Macros Scripting, yang wajib memprogram kode mesin assembly untuk mengatur margin tata letak cetak."
        ],
        "formula": {
            "title": "PRINSIP KERJA OTOMASI MAIL MERGE",
            "latex": "\\text{Template Dokumen Master} + \\text{Sumber Data Tabular (Excel/DB)} \\xrightarrow{\\text{Merge Fields}} \\prod_{i=1}^{n} \\text{Dokumen Terpersonalisasi}",
            "legend": "• Main Document: Format statis surat undangan<br>• Data Source: Berkas spreadsheet berisi baris data penerima<br>• Merge Fields: Placeholder dinamis (misal: «Nama», «Alamat»)"
        },
        "hints": {
            "concept": "Menggabungkan dokumen master dengan data tabel untuk surat massal adalah fitur Mail Merge.",
            "execution": "Pilih: Mail Merge."
        }
    },
    {
        "id": "inf-lat-e-20",
        "materi": "ANALISIS DATA",
        "topic": "Prinsip Bentuk Normal Pertama (1NF) Basis Data",
        "stem": "Sebuah tabel data siswa memiliki kolom `hobi` yang berisi nilai gabungan beberapa teks seperti `'Membaca, Futsal, Musik'` dalam satu baris sel data. Untuk memenuhi aturan Bentuk Normal Pertama (1st Normal Form / 1NF), langkah yang wajib dilakukan adalah...",
        "correct": "Menghilangkan nilai berulang (repeating groups) dan memastikan setiap kolom hanya memuat nilai tunggal yang atomik (atomic value) pada setiap baris rekaman.",
        "distractors": [
            "Menghapus seluruh baris data siswa yang memiliki lebih dari satu jenis hobi secara permanen.",
            "Menambahkan kunci asing (Foreign Key) ke tabel lain tanpa mengubah komposisi nilai sel kolom hobi.",
            "Mengenkripsi kolom hobi menjadi kode biner rahasia agar tidak dapat dibaca oleh pengguna biasa.",
            "Mengubah nama kolom hobi menjadi hobi_1, hobi_2, hobi_3 hingga puluhan kolom kosong tak terbatas."
        ],
        "formula": {
            "title": "ATURAN BENTUK NORMAL PERTAMA (1NF)",
            "latex": "\\forall r \\in R, \\forall A \\in \\text{Attributes}(R) : \\quad \\text{Nilai}(r, A) \\in \\text{Domain Atomik}",
            "legend": "• 1NF: Nilai atribut wajib atomik (tidak bernilai jamak/kumpulan data dalam satu sel)<br>• 2NF: Memenuhi 1NF dan tidak memiliki ketergantungan fungsional parsial (partial dependency)<br>• 3NF: Memenuhi 2NF dan tidak memiliki ketergantungan transitif (transitive dependency)"
        },
        "hints": {
            "concept": "1NF mensyaratkan setiap kolom memiliki nilai atomik (nilai tunggal yang tidak bisa dipecah lagi) dan bebas perulangan nilai dalam satu sel.",
            "execution": "Pilih: Memastikan setiap kolom memuat nilai tunggal yang atomik dan menghilangkan repeating groups."
        }
    },
    {
        "id": "inf-lat-e-21",
        "materi": "SISTEM KOMPUTER",
        "topic": "Perbedaan Perangkat Lunak Sistem vs Perangkat Lunak Aplikasi",
        "stem": "Perangkat lunak pada sistem komputasi diklasifikasikan menjadi perangkat lunak sistem (system software) dan perangkat lunak aplikasi (application software). Karakteristik pembeda utama perangkat lunak sistem adalah...",
        "correct": "Berfungsi mengelola dan mengontrol sumber daya perangkat keras secara langsung serta menyediakan antarmuka dasar bagi perangkat lunak lain untuk berjalan, contohnya Linux, Windows, dan driver perangkat.",
        "distractors": [
            "Didesain khusus untuk membantu pengguna menyelesaikan tugas spesifik personal seperti mengedit gambar dan berselancar web.",
            "Selalu ditulis menggunakan bahasa pemrograman web seperti HTML dan CSS tanpa mengakses komponen memori CPU.",
            "Hanya dapat dijalankan apabila komputer terhubung secara aktif dengan jaringan internet pita lebar nirkabel.",
            "Bersifat opsional dan komputer tetap dapat beroperasi menjalankan aplikasi pengolah kata tanpa adanya sistem operasi."
        ],
        "formula": {
            "title": "LAPISAN EKOSISTEM KOMPUTASI",
            "latex": "\\text{User} \\leftrightarrow \\text{Application Software} \\leftrightarrow \\text{Operating System (System Software)} \\leftrightarrow \\text{Hardware}",
            "legend": "• System Software: Kernel OS, Device Drivers, Firmware, Utility pengelola disk<br>• Application Software: Web browser, Word processor, Video editor, Game"
        },
        "hints": {
            "concept": "Perangkat lunak sistem bertugas mengelola sumber daya perangkat keras dan platform dasar komputasi.",
            "execution": "Pilih: Mengelola sumber daya perangkat keras dan menyediakan antarmuka dasar bagi perangkat lunak lain."
        }
    },
    {
        "id": "inf-lat-e-22",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Fungsi dan Alur Kerja Domain Name System (DNS)",
        "stem": "Ketika seorang pengguna mengetik alamat `www.kemdikbud.go.id` pada bilah alamat peramban web, peramban tidak dapat langsung terhubung ke server tujuan tanpa mengetahui alamat numerik server tersebut. Layanan jaringan internet yang bertugas menerjemahkan nama domain yang mudah dibaca manusia menjadi alamat IP numerik mesin adalah...",
        "correct": "Domain Name System (DNS), yang bekerja sebagai buku telepon global internet yang memetakan FQDN ke alamat IP publik server tujuan.",
        "distractors": [
            "Dynamic Host Configuration Protocol (DHCP), yang otomatis membagikan konfigurasi IP ke komputer klien lokal.",
            "Simple Mail Transfer Protocol (SMTP), yang bertugas mengirimkan pesan surel antar server pos elektronik.",
            "Network Address Translation (NAT), yang memodifikasi informasi header paket untuk berbagi satu IP publik.",
            "Address Resolution Protocol (ARP), yang memetakan alamat IP logis ke MAC Address fisik dalam satu subnet LAN."
        ],
        "formula": {
            "title": "MEKANISME RESOLUSI DOMAIN NAME SYSTEM (DNS)",
            "latex": "\\text{FQDN (kemdikbud.go.id)} \\xrightarrow{\\text{DNS Query (Port 53 UDP)}} \\text{DNS Hierarchy (Root } \\to \\text{ TLD } \\to \\text{ Authoritative)} \\to \\text{IP: 118.98.x.x}",
            "legend": "• Rekursif Resolver: Membantu klien mencari IP ke DNS bertingkat<br>• DNS Record A: Memetakan domain ke IPv4<br>• DNS Record AAAA: Memetakan domain ke IPv6<br>• DNS Record CNAME: Alias nama domain"
        },
        "hints": {
            "concept": "Menerjemahkan nama domain manusia menjadi alamat IP numerik komputer adalah tugas DNS.",
            "execution": "Pilih: Domain Name System (DNS)."
        }
    },
    {
        "id": "inf-lat-e-23",
        "materi": "PRAKTIK LINTAS BIDANG",
        "topic": "Operasi Dasar Version Control System Git",
        "stem": "Dalam pengembangan proyek perangkat lunak menggunakan sistem kendali versi Git, seorang pengembang telah selesai memodifikasi kode program dan menambahkan berkas perubahan ke staging area menggunakan `git add .`. Perintah Git yang tepat untuk menyimpan rekaman snapshot perubahan tersebut ke repositori lokal dengan menyertakan pesan deskriptif adalah...",
        "correct": "`git commit -m \"Pesan deskripsi perubahan\"`",
        "distractors": [
            "`git push origin main`",
            "`git checkout -b branch_baru`",
            "`git pull upstream master`",
            "`git clone https://repository.git`"
        ],
        "formula": {
            "title": "SIKLUS TIGA POHON SISTEM GIT (THREE-TREE ARCHITECTURE)",
            "latex": "\\text{Working Directory} \\xrightarrow{\\text{git add}} \\text{Staging Area (Index)} \\xrightarrow{\\text{git commit}} \\text{Local Repository} \\xrightarrow{\\text{git push}} \\text{Remote Repo}",
            "legend": "• git add: Menandai file yang akan disimpan ke commit berikutnya<br>• git commit: Menyimpan snapshot permanen di basis data riwayat lokal<br>• git push: Mengirim commit lokal ke server kolaborasi daring (GitHub/GitLab)"
        },
        "hints": {
            "concept": "Perintah untuk menyimpan snapshot berkas dari staging area ke repositori lokal beserta pesan adalah git commit -m.",
            "execution": "Pilih: git commit -m \"Pesan deskripsi perubahan\"."
        }
    },
    {
        "id": "inf-lat-e-24",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Mekanisme dan Kompleksitas Algoritma Pengurutan Bubble Sort",
        "stem": "Algoritma pengurutan Bubble Sort bekerja dengan cara membandingkan pasangan elemen yang bersebelahan secara berulang dan menukarnya jika urutannya salah. Jika sebuah array memiliki $n$ elemen dan berada dalam keadaan terurut terbalik (worst case), kompleksitas waktu asimtotik dari Bubble Sort adalah...",
        "correct": "$O(n^2)$, karena algoritma membutuhkan sekitar $\\frac{n(n-1)}{2}$ kali operasi perbandingan dan penukaran elemen.",
        "distractors": [
            "$O(n \\log n)$, karena algoritma memanfaatkan teknik memecah dan menaklukkan array menjadi dua bagian simetris.",
            "$O(n)$, karena algoritma hanya memerlukan satu kali lintasan pemeriksaan dari indeks awal ke akhir.",
            "$O(1)$, karena penukaran elemen selalu dilakukan secara instan di dalam memori register konstan.",
            "$O(\\log n)$, karena setiap iterasi berhasil mengeliminasi separuh dari total data yang belum terurut."
        ],
        "formula": {
            "title": "KOMPLEKSITAS ASIMTOTIK PENGURUTAN BUBBLE SORT",
            "latex": "T_{\\text{worst}}(n) = \\sum_{i=1}^{n-1} i = \\frac{n(n - 1)}{2} = \\frac{1}{2}n^2 - \\frac{1}{2}n \\implies O(n^2)",
            "legend": "• Worst Case (Terurut Terbalik): $O(n^2)$ perbandingan dan penukaran<br>• Best Case (Sudah Terurut dengan flag optimasi): $O(n)$<br>• Algoritma pengurutan efisien ($O(n \\log n)$): Merge Sort, Quick Sort, Heap Sort"
        },
        "hints": {
            "concept": "Bubble sort worst-case memiliki perulangan bersarang n x n, sehingga kompleksitasnya adalah O(n^2).",
            "execution": "Pilih: O(n^2)."
        }
    },
    {
        "id": "inf-lat-e-25",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Etika Perangkat Lunak dan Lisensi Sumber Terbuka (Open Source)",
        "stem": "Banyak perangkat lunak modern didistribusikan di bawah lisensi Open Source permisif seperti Lisensi MIT atau Lisensi Apache 2.0. Hak paling mendasar yang diberikan oleh lisensi sumber terbuka kepada pengembang perangkat lunak lain adalah...",
        "correct": "Kebebasan untuk melihat, memodifikasi, mendistribusikan ulang, dan menggunakan kode sumber baik untuk keperluan non-komersial maupun komersial dengan tetap mencantumkan atribusi hak cipta pencipta aslinya.",
        "distractors": [
            "Kewajiban untuk membayar royalti bulanan kepada pencipta asli apabila perangkat lunak dijalankan di komputer kantor.",
            "Larangan keras untuk membaca baris kode sumber asli demi melindungi hak paten rahasia dagang pencipta.",
            "Kewajiban untuk menyerahkan seluruh hak milik intelektual ciptaan baru kepada pemilik repositori induk.",
            "Keharusan mengunci kode hasil modifikasi agar tidak dapat diakses oleh sistem operasi berbasis Unix."
        ],
        "formula": {
            "title": "KATEGORI LISENSI PERANGKAT LUNAK",
            "latex": "\\begin{aligned} \\text{Proprietary (Closed Source):} & \\quad \\text{Kode sumber rahasia, hak cipta dilindungi penuh (EULA)} \\\\ \\text{Copyleft (GPL):} & \\quad \\text{Turunan wajib berlisensi terbuka yang sama} \\\\ \\text{Permissive (MIT/Apache):} & \\quad \\text{Bebas digunakan & dikomersialkan dengan atribusi hak cipta} \\end{aligned}",
            "legend": "• OSI (Open Source Initiative): Standar 10 kriteria perangkat lunak sumber terbuka<br>• Atribusi: Menyertakan notice hak cipta asli dalam salinan berkas lisensi"
        },
        "hints": {
            "concept": "Lisensi open source memberikan kebebasan melihat, memodifikasi, dan mendistribusikan kode dengan menyertakan atribusi.",
            "execution": "Pilih opsi yang menjamin kebebasan akses, modifikasi, dan distribusi dengan mencantumkan atribusi hak cipta asli."
        }
    }
]
