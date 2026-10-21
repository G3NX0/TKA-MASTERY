# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Informatika (SMA/MA)
Dataset: Latihan Tingkat Medium (25 Authentic Questions, inf-lat-m-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

INFORMATIKA_MEDIUM_ITEMS = [
    {
        "id": "inf-lat-m-01",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Pemrograman Dinamis (Dynamic Programming) vs Divide and Conquer",
        "stem": "Dalam menghitung bilangan Fibonacci ke-$n$, pendekatan rekursif naif memiliki kompleksitas waktu eksponensial $O(2^n)$ karena mengevaluasi ulang sub-masalah yang sama berulang kali. Pendekatan Pemrograman Dinamis (Dynamic Programming) dengan teknik memoization atau tabulasi mampu menurunkan kompleksitas waktu menjadi $O(n)$ linier. Alasan konseptual mengapa teknik DP efektif pada masalah ini adalah...",
        "correct": "Masalah memiliki sifat Sub-masalah Tumpang Tindih (Overlapping Subproblems) dan Struktur Bawah Optimal (Optimal Substructure), sehingga hasil sub-masalah disimpan sekali dan dapat langsung digunakan kembali tanpa komputasi ulang.",
        "distractors": [
            "Masalah membagi data menjadi dua himpunan independen yang tidak pernah saling beririsan seperti halnya Merge Sort.",
            "Masalah mengubah proses perhitungan menjadi fungsi acak nondeterministik yang kebal terhadap galat rekursi.",
            "Masalah mengeliminasi seluruh operasi penambahan aritmetika dengan menggantikannya menjadi operasi pergeseran bitwise konstan.",
            "Masalah secara otomatis mengalokasikan memori grafis GPU untuk menjalankan komputasi paralel secara fisik."
        ],
        "formula": {
            "title": "PRINSIP PEMROGRAMAN DINAMIS (DYNAMIC PROGRAMMING)",
            "latex": "F(n) = F(n-1) + F(n-2), \\quad \\text{MemoTable}[n] \\implies \\text{Kompleksitas: } O(2^n) \\xrightarrow{\\text{DP}} O(n)",
            "legend": "• Overlapping Subproblems: Sub-masalah yang sama dihitung berulang kali<br>• Optimal Substructure: Solusi optimal masalah utama dibentuk dari solusi optimal sub-masalahnya<br>• Memoization (Top-down): Rekursi + Caching; Tabulation (Bottom-up): Iterasi tabel"
        },
        "hints": {
            "concept": "Syarat mutlak DP: Overlapping subproblems (sub-masalah tumpang tindih) dan optimal substructure. Hasil disimpan agar tidak dihitung ulang.",
            "execution": "Pilih opsi yang menyebutkan Sub-masalah Tumpang Tindih (Overlapping Subproblems) dan Struktur Bawah Optimal."
        }
    },
    {
        "id": "inf-lat-m-02",
        "materi": "SISTEM KOMPUTER",
        "topic": "Manajemen Memori Virtual: Paging dan Fenomena Page Fault",
        "stem": "Dalam sistem operasi modern, memori virtual memungkinkan komputer menjalankan program yang membutuhkan ruang memori lebih besar daripada kapasitas RAM fisik melalui mekanisme paging. Jika CPU mencoba mengakses sebuah instruksi yang berada pada halaman memori (page) yang sedang tersimpan di penyimpanan sekunder (SSD) dan belum dimuat ke bingkai memori fisik (page frame), peristiwa yang terjadi adalah...",
        "correct": "Terjadi Page Fault Interrupt; sistem operasi menangguhkan proses aktif, mencari halaman yang diminta di secondary storage, memuatnya ke frame RAM kosong, memperbarui page table, lalu melanjutkan eksekusi proses.",
        "distractors": [
            "Terjadi Segmentation Fault permanen yang langsung menghentikan paksa (crash) sistem operasi seketika.",
            "CPU langsung beralih mengeksekusi instruksi berikutnya secara acak tanpa mempedulikan data yang hilang.",
            "Sistem operasi otomatis menghapus seluruh isi memori RAM fisik untuk mencegah kerusakan perangkat keras.",
            "Prosesor menaikkan kecepatan frekuensi clock secara instan untuk menciptakan modul memori semikonduktor baru."
        ],
        "formula": {
            "title": "PENANGANAN KESALAHAN HALAMAN (PAGE FAULT HANDLING)",
            "latex": "\\text{Akses Memori} \\xrightarrow{\\text{Valid Bit = 0}} \\text{Trap/Page Fault} \\to \\text{OS Baca Disk} \\to \\text{Load ke Frame RAM} \\to \\text{Update Page Table (Valid Bit = 1)} \\to \\text{Restart Instruksi}",
            "legend": "• Page Table: Memetakan alamat logika (Virtual Page Number) ke alamat fisik (Frame Number)<br>• Thrashing: Kondisi sistem terlalu sibuk melakukan swap paging daripada mengeksekusi proses akibat kehabisan RAM"
        },
        "hints": {
            "concept": "Akses halaman yang belum ada di RAM memicu interrupt Page Fault. OS memuat halaman dari disk ke RAM lalu mengulang instruksi.",
            "execution": "Pilih: Terjadi Page Fault Interrupt; OS memuat halaman dari disk ke RAM."
        }
    },
    {
        "id": "inf-lat-m-03",
        "materi": "STRUKTUR DATA",
        "topic": "Analisis Efisiensi Penyisipan Elemen: Linked List vs Array Dinamis",
        "stem": "Sebuah aplikasi memerlukan operasi penyisipan data baru secara terus-menerus tepat di posisi indeks paling awal (elemen terdepan). Dibandingkan dengan struktur data Array Dinamis berukuran $n$, struktur data Singly Linked List lebih unggul untuk kebutuhan operasi ini karena...",
        "correct": "Linked List memiliki kompleksitas penyisipan di awal sebesar $O(1)$ konstan karena hanya memperbarui penunjuk pointer `head`, sedangkan Array membutuhkan $O(n)$ karena harus menggeser (shifting) seluruh $n$ elemen yang ada ke kanan.",
        "distractors": [
            "Linked List menyimpan data dalam blok memori fisik yang berdampingan secara berurutan sehingga akses acaknya berkecepatan $O(1)$.",
            "Array dinamis tidak dapat dialokasikan kembali jika kapasitas awal memori sudah terpenuhi oleh data sebelumnya.",
            "Linked List secara otomatis mengurutkan elemen data dari yang terkecil ke terbesar setiap kali simpul baru disisipkan.",
            "Array membutuhkan alokasi memori dua kali lebih besar untuk setiap elemen data karena menyimpan alamat pointer ganda."
        ],
        "formula": {
            "title": "KOMPARASI OPERASI PENYISIPAN DI ELEMEN TERDEPAN (INSERT AT HEAD)",
            "latex": "\\begin{aligned} \\text{Singly Linked List:} & \\quad \\text{newNode.next} = \\text{head}; \\ \\text{head} = \\text{newNode} \\implies O(1) \\\\ \\text{Dynamic Array:} & \\quad \\text{for } i = n \\text{ down to } 1 : A[i] = A[i-1] \\implies O(n) \\text{ Shifting} \\end{aligned}",
            "legend": "• Akses Acak (Index Access): Array $O(1)$, Linked List $O(n)$<br>• Penyisipan di Depan: Linked List $O(1)$, Array $O(n)$<br>• Overhead Memori: Linked List membutuhkan memori tambahan untuk penunjuk pointer (next)"
        },
        "hints": {
            "concept": "Menyisipkan di awal: Array butuh shifting semua elemen (O(n)), sedangkan Linked List hanya mengubah pointer head (O(1)).",
            "execution": "Pilih opsi: Linked List memiliki kompleksitas penyisipan O(1) konstan sedangkan Array butuh O(n) karena shifting."
        }
    },
    {
        "id": "inf-lat-m-04",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Kalkulasi Subnetting IPv4 Berbasis CIDR /27",
        "stem": "Sebuah laboratorium komputer sekolah diberikan blok alamat jaringan IPv4 `192.168.10.64/27`. Berdasarkan notasi CIDR tersebut, jumlah alamat host yang dapat dikonfigurasi secara valid pada komputer klien serta alamat broadcast dari subnet tersebut adalah...",
        "correct": "30 host valid, dengan alamat broadcast `192.168.10.95`.",
        "distractors": [
            "32 host valid, dengan alamat broadcast `192.168.10.96`.",
            "62 host valid, dengan alamat broadcast `192.168.10.127`.",
            "14 host valid, dengan alamat broadcast `192.168.10.79`.",
            "28 host valid, dengan alamat broadcast `192.168.10.92`."
        ],
        "formula": {
            "title": "FORMULA KALKULASI SUBNETTING IPV4",
            "latex": "\\text{Prefix /27} \\implies \\text{Host Bits } h = 32 - 27 = 5 \\implies \\text{Total IP} = 2^5 = 32 \\implies \\text{Host Valid} = 2^5 - 2 = 30",
            "legend": "• Network Address: 192.168.10.64 (IP pertama, tidak boleh untuk host)<br>• Rentang Host Valid: 192.168.10.65 s.d. 192.168.10.94 (30 host)<br>• Broadcast Address: 192.168.10.64 + 31 = 192.168.10.95 (IP terakhir subnet)"
        },
        "hints": {
            "concept": "/27 menyisakan 5 bit host (32 - 27 = 5). Total IP = 2^5 = 32. Host valid = 32 - 2 = 30. Broadcast = 64 + 31 = 95.",
            "execution": "Pilih: 30 host valid dan broadcast 192.168.10.95."
        }
    },
    {
        "id": "inf-lat-m-05",
        "materi": "ANALISIS DATA",
        "topic": "Perbedaan Karakteristik Relasi SQL INNER JOIN vs LEFT JOIN",
        "stem": "Diberikan tabel `Pelanggan` dan tabel `Pesanan` yang dihubungkan melalui atribut `id_pelanggan`. Seorang analis data ingin menampilkan daftar seluruh pelanggan yang terdaftar di sistem, termasuk pelanggan yang belum pernah melakukan pesanan sama sekali (kolom pesanan akan bernilai NULL). Klausa SQL JOIN yang tepat digunakan adalah...",
        "correct": "`LEFT OUTER JOIN`, karena akan mempertahankan seluruh baris dari tabel kiri (`Pelanggan`) dan mencocokkan data dari tabel kanan (`Pesanan`), mengisi nilai NULL jika tidak ada kecocokan.",
        "distractors": [
            "`INNER JOIN`, karena hanya mengembalikan baris yang memiliki nilai kecocokan di kedua tabel secara bersamaan.",
            "`RIGHT OUTER JOIN`, karena secara eksklusif hanya menampilkan data pesanan yang tidak memiliki identitas pembeli.",
            "`CROSS JOIN`, karena menghasilkan perkalian kartesian tanpa memperhatikan hubungan kunci asing sama sekali.",
            "`FULL OUTER JOIN`, karena hanya menampilkan baris yang tidak memiliki irisan sama sekali di kedua tabel."
        ],
        "formula": {
            "title": "ALJABAR RELASIONAL OPERASI JOIN SQL",
            "latex": "\\begin{aligned} \\text{INNER JOIN:} & \\quad R \\bowtie_{R.A = S.A} S = \\{(r, s) \\mid r \\in R, s \\in S, r.A = s.A\\} \\\\ \\text{LEFT JOIN:} & \\quad R \\leftouterjoin_{R.A = S.A} S = (R \\bowtie S) \\cup \\{(r, \\text{NULL}) \\mid r \\in R, \\neg \\exists s \\in S (r.A = s.A)\\} \\end{aligned}",
            "legend": "• INNER JOIN: Hanya menampilkan data yang berelasi di kedua tabel<br>• LEFT JOIN: Menampilkan semua data tabel kiri, data kanan kosong diisi NULL<br>• Kasus penggunaan: Mencari entitas yang belum memiliki transaksi aktif"
        },
        "hints": {
            "concept": "Untuk menampilkan semua baris tabel kiri (Pelanggan) meskipun belum ada transaksi di tabel kanan, gunakan LEFT JOIN.",
            "execution": "Pilih: LEFT OUTER JOIN."
        }
    },
    {
        "id": "inf-lat-m-06",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Analisis Kompleksitas Waktu Divide and Conquer pada Merge Sort",
        "stem": "Algoritma Merge Sort mengurutkan larik berukuran $n$ dengan membagi larik menjadi dua sub-larik yang sama besar secara rekursif, mengurutkan masing-masing sub-larik, lalu menggabungkannya kembali (merge). Relasi rekurensi waktu dari Merge Sort dirumuskan sebagai $T(n) = 2T(n/2) + O(n)$. Berdasarkan Teorema Master, kompleksitas waktu asimtotik dari Merge Sort adalah...",
        "correct": "$O(n \\log_2 n)$ pada semua kasus (best, average, dan worst case), karena pohon rekursi memiliki kedalaman $\\log_2 n$ dan setiap level pohon membutuhkan waktu penggabungan linier $O(n)$.",
        "distractors": [
            "$O(n^2)$ pada worst case, karena proses penggabungan membutuhkan perbandingan kuadratik antar elemen.",
            "$O(n)$ pada best case, karena jika larik sudah terurut algoritma tidak melakukan pemecahan rekursif.",
            "$O(\\log_2 n)$, karena algoritma berhasil mengabaikan separuh elemen larik pada setiap tahapan partisi.",
            "$O(2^n)$, karena pohon pemanggilan fungsi rekursif bercabang dua tanpa henti hingga batas memori."
        ],
        "formula": {
            "title": "TEOREMA MASTER PADA ALGORITMA MERGE SORT",
            "latex": "T(n) = aT\\left(\\frac{n}{b}\\right) + f(n) \\implies T(n) = 2T\\left(\\frac{n}{2}\\right) + cn \\implies n^{\\log_b a} = n^{\\log_2 2} = n^1 \\implies T(n) = \\Theta(n \\log n)",
            "legend": "• Kedalaman rekursi: $\\log_2 n$ level<br>• Biaya penggabungan (merge) per level: $O(n)$ operasi<br>• Total waktu: $(\\text{kedalaman}) \\times (\\text{biaya per level}) = n \\log n$<br>• Sifat stabil (stable sort), namun butuh memori tambahan $O(n)$"
        },
        "hints": {
            "concept": "Merge sort memiliki kedalaman rekursi log(n) dan merge linier n pada tiap level, sehingga T(n) = O(n log n) di semua kasus.",
            "execution": "Pilih: O(n log n) pada semua kasus."
        }
    },
    {
        "id": "inf-lat-m-07",
        "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
        "topic": "Sistem Kriptografi Hibrida pada Protokol HTTPS / TLS",
        "stem": "Protokol keamanan web HTTPS (SSL/TLS) menggunakan pendekatan kriptografi hibrida (hybrid cryptography) yang menggabungkan algoritma kunci asimetris (seperti RSA atau ECC) dan algoritma kunci simetris (seperti AES-256). Alasan mendasar mengapa protokol ini tidak menggunakan kunci asimetris untuk seluruh enkripsi data transfer adalah...",
        "correct": "Komputasi enkripsi dan dekripsi asimetris berbasis operasi matematika bilangan prima besar sangat lambat dan membebani CPU, sehingga kunci asimetris hanya digunakan saat negosiasi jabat tangan awal untuk menukar kunci sesi simetris yang jauh lebih cepat.",
        "distractors": [
            "Kunci asimetris memiliki celah keamanan fatal di mana kunci privat dapat ditebak secara langsung dari sertifikat digital.",
            "Algoritma simetris tidak mampu mengenkripsi data multimedia berukuran besar seperti video dan berkas gambar.",
            "Kunci asimetris dilarang oleh badan standardisasi internet dunia karena membutuhkan sambungan kabel tembaga khusus.",
            "Algoritma simetris tidak memerlukan kunci apapun untuk mengenkripsi maupun mendekripsi pesan rahasia pengguna."
        ],
        "formula": {
            "title": "ALUR KERJA KRIPTOGRAFI HIBRIDA (HYBRID CRYPTOSYSTEM)",
            "latex": "\\begin{aligned} \\text{Fase Handshake (Asimetris):} & \\quad \\text{Klien enkripsi Kunci Sesi (Session Key)} \\xrightarrow{\\text{Public Key Server}} \\text{Server Dekripsi via Private Key} \\\\ \\text{Fase Transfer Data (Simetris):} & \\quad \\text{Klien} \\xleftrightarrow{\\text{AES-GCM (Session Key)}} \\text{Server (Cepat & Ringan Komputasi)} \\end{aligned}",
            "legend": "• Kunci Asimetris (RSA/ECC): Otentikasi identitas server & pertukaran rahasia kunci sesi (key exchange)<br>• Kunci Simetris (AES/ChaCha20): Enkripsi muatan massal data aplikasi berkecepatan tinggi"
        },
        "hints": {
            "concept": "Kriptografi asimetris lambat sehingga hanya dipakai saat handshake untuk bertukar Session Key. Enkripsi data massal memakai AES simetris yang cepat.",
            "execution": "Pilih: Komputasi asimetris sangat lambat sehingga hanya digunakan untuk menukar kunci sesi simetris yang cepat."
        }
    },
    {
        "id": "inf-lat-m-08",
        "materi": "SISTEM KOMPUTER",
        "topic": "Penjadwalan Proses CPU: Preemptive vs Non-Preemptive",
        "stem": "Dalam sistem operasi multitasking, algoritma penjadwalan Round-Robin (RR) membagi waktu pemrosesan CPU ke setiap proses menggunakan kuantum waktu (time quantum) yang telah ditentukan secara bergiliran. Jika ukuran kuantum waktu ditetapkan terlalu kecil (misalnya mendekati 0 milidetik), dampak negatif yang akan dialami oleh kinerja sistem adalah...",
        "correct": "Efisiensi sistem merosot tajam karena waktu prosesor habis terbuang hanya untuk melakukan peralihan konteks (context switching overhead) antar proses daripada menjalankan instruksi program.",
        "distractors": [
            "Terjadi fenomena Starvation di mana proses yang memiliki burst time panjang tidak akan pernah dieksekusi sama sekali.",
            "Algoritma Round-Robin akan otomatis berubah menjadi algoritma First-Come, First-Served (FCFS) konvensional.",
            "Sistem operasi akan mengalami deadlock permanen karena memori RAM terfragmentasi secara fisik.",
            "Seluruh proses dalam sistem akan selesai dieksekusi dalam waktu 0 milidetik secara instan."
        ],
        "formula": {
            "title": "PENGARUH QUANTUM TIME PADA PENJADWALAN ROUND ROBIN",
            "latex": "q \\to 0 \\implies \\text{Context Switches} \\to \\infty \\implies \\text{Throughput} \\to 0, \\quad q \\to \\infty \\implies \\text{Round Robin} \\to \\text{FCFS}",
            "legend": "• Context Switch: Menyimpan state (register, PC) proses lama dan memuat state proses baru ke CPU<br>• Jika $q$ terlalu kecil: Overhead switching mendominasi pemakaian CPU<br>• Jika $q$ terlalu besar: Waktu respons interaktif menjadi lambat"
        },
        "hints": {
            "concept": "Time quantum terlalu kecil menyebabkan terlalu sering terjadi context switching sehingga waktu CPU habis untuk overhead alih tugas.",
            "execution": "Pilih: Kinerja merosot karena tingginya overhead context switching."
        }
    },
    {
        "id": "inf-lat-m-09",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Kelemahan Strategi Algoritma Serakah (Greedy Approach)",
        "stem": "Algoritma Serakah (Greedy Algorithm) bekerja dengan prinsip membuat pilihan optimal secara lokal pada setiap langkah dengan harapan mencapai solusi optimal secara global. Diberikan pecahan koin bernilai $\\{1, 3, 4\\}$ dan target kembalian sebesar $6$. Jika algoritma Greedy diterapkan untuk meminimalkan jumlah koin, solusi yang dihasilkan serta kondisi keoptimalannya adalah...",
        "correct": "Greedy menghasilkan 3 koin ($4 + 1 + 1$), yang BUKAN solusi optimal global karena solusi paling optimal adalah 2 koin ($3 + 3$).",
        "distractors": [
            "Greedy menghasilkan 2 koin ($3 + 3$), yang membuktikan bahwa algoritma serakah selalu optimal pada setiap sistem mata uang.",
            "Greedy menghasilkan 6 koin ($1 + 1 + 1 + 1 + 1 + 1$), karena selalu memprioritaskan koin berbobot terkecil.",
            "Greedy gagal mengeksekusi komputasi dan program mengalami crash karena nilai koin tidak habis dibagi dua.",
            "Greedy menghasilkan 2 koin ($4 + 2$), dengan otomatis mencetak koin baru bernilai 2 yang tidak ada di daftar."
        ],
        "formula": {
            "title": "ANALISIS KEGAGALAN ALGORITMA GREEDY (COIN CHANGE PROBLEM)",
            "latex": "\\begin{aligned} \\text{Target: } 6, \\quad \\text{Koin: } \\{4, 3, 1\\} \\\\ \\text{Solusi Greedy (Ambil Koin Terbesar):} & \\quad 4 \\to \\text{Sisa } 2 \\to 1 \\to \\text{Sisa } 1 \\to 1 \\implies 3 \\text{ Koin } (4+1+1) \\\\ \\text{Solusi Optimal (Dynamic Programming):} & \\quad 3 + 3 = 6 \\implies 2 \\text{ Koin } (3+3) \\end{aligned}",
            "legend": "• Greedy Choice Property tidak selalu menjamin solusi global optimal pada canonical coin systems non-standar<br>• Masalah penukaran koin umum diselesaikan optimal menggunakan Dynamic Programming ($O(n \\times V)$)"
        },
        "hints": {
            "concept": "Greedy memilih koin terbesar dulu: 4, lalu sisa 2 (koin 1 dan 1), total 3 koin. Padahal solusi terbaik adalah 3+3 = 2 koin.",
            "execution": "Pilih: Greedy menghasilkan 3 koin (4+1+1), bukan optimal global karena solusi optimal adalah 2 koin (3+3)."
        }
    },
    {
        "id": "inf-lat-m-10",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Penelusuran Algoritma Pemangkatan Cepat (Binary Exponentiation)",
        "stem": "Diberikan algoritma rekursif perhitungan pangkat bilangan bulat berikut:\n```python\ndef power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        half = power(x, n // 2)\n        return half * half\n    else:\n        return x * power(x, n - 1)\n```\nJika fungsi dipanggil dengan argumen `power(3, 13)`, jumlah total pemanggilan fungsi `power` (termasuk pemanggilan awal) yang dieksekusi di dalam memori adalah...",
        "correct": "8 kali pemanggilan, dengan rantai parameter $n$: $13 \\to 12 \\to 6 \\to 3 \\to 2 \\to 1 \\to 0$.",
        "distractors": [
            "14 kali pemanggilan, karena fungsi dipanggil sebanyak $n + 1$ kali secara linier.",
            "4 kali pemanggilan, karena hanya memperhitungkan kasus cabang genap saja.",
            "13 kali pemanggilan, sesuai dengan nilai eksponen pangkat yang dimasukkan.",
            "6 kali pemanggilan, karena pembulatan logaritma basis dua dari angka 13."
        ],
        "formula": {
            "title": "ALUR TRACING EKSPOKSI CEPAT (BINARY EXPONENTIATION)",
            "latex": "n: 13 \\xrightarrow{\\text{ganjil}} 12 \\xrightarrow{\\text{genap}} 6 \\xrightarrow{\\text{genap}} 3 \\xrightarrow{\\text{ganjil}} 2 \\xrightarrow{\\text{genap}} 1 \\xrightarrow{\\text{ganjil}} 0 \\implies 7 \\text{ transisi} \\implies 8 \\text{ pemanggilan}",
            "legend": "• Panggilan 1: power(3, 13) -> n ganjil -> panggil power(3, 12)<br>• Panggilan 2: power(3, 12) -> n genap -> panggil power(3, 6)<br>• Panggilan 3: power(3, 6) -> n genap -> panggil power(3, 3)<br>• Panggilan 4: power(3, 3) -> n ganjil -> panggil power(3, 2)<br>• Panggilan 5: power(3, 2) -> n genap -> panggil power(3, 1)<br>• Panggilan 6: power(3, 1) -> n ganjil -> panggil power(3, 0)<br>• Panggilan 7: power(3, 0) -> n==0 -> return 1<br>• Total panggilan = 7 pemanggilan rekursif unik"
        },
        "hints": {
            "concept": "Hitung urutan nilai n yang dipanggil: 13 (ke-1), 12 (ke-2), 6 (ke-3), 3 (ke-4), 2 (ke-5), 1 (ke-6), 0 (ke-7). Total 7 panggilan.",
            "execution": "Pilih opsi yang sesuai dengan tracing rantai nilai n (7 pemanggilan)."
        }
    },
    {
        "id": "inf-lat-m-11",
        "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
        "topic": "Interoperabilitas dan Karakteristik Format Pertukaran Data JSON vs XML",
        "stem": "Dalam pengembangan antarmuka pemrograman aplikasi web modern (RESTful API), format JSON (JavaScript Object Notation) telah menggeser dominasi XML (Extensible Markup Language) sebagai format pertukaran data standar. Keunggulan teknis utama dari JSON adalah...",
        "correct": "Memiliki struktur teks yang jauh lebih ringkas (tanpa tag penutup yang bertele-tele), ukuran payload lebih kecil sehingga menghemat bandwidth, serta secara bawaan dapat diparsing langsung menjadi objek bahasa pemrograman seperti JavaScript dan Python.",
        "distractors": [
            "Mendukung validasi skema berbasis DTD dan transformasi XSLT bawaan yang tidak dimiliki oleh format data lainnya.",
            "Wajib dienkripsi menggunakan kunci asimetris sebelum dapat ditransmisikan melalui jaringan internet.",
            "Menjamin bahwa data tidak dapat diubah oleh siapapun karena berbasis format biner terkompresi permanen.",
            "Mampu menyimpan data logika program berupa kode mesin yang dapat dieksekusi langsung oleh prosesor klien."
        ],
        "formula": {
            "title": "KOMPARASI FORMAT PERTUKARAN DATA (DATA INTERCHANGE)",
            "latex": "\\begin{aligned} \\text{JSON:} & \\quad \\{\\text{\"id\": 1, \"nama\": \"Budi\"}\\} \\implies \\text{Ringkas, Cepat di-parse, Ukuran kecil} \\\\ \\text{XML:} & \\quad \\text{<siswa><id>1</id><nama>Budi</nama></siswa>} \\implies \\text{Banyak Tag Berulang (Verbose)} \\end{aligned}",
            "legend": "• JSON Types: String, Number, Object, Array, Boolean, Null<br>• Parsing: JSON.parse() pada browser berjalan native di level C++ engine<br>• Format ideal untuk komunikasi mikroservis dan mobile API"
        },
        "hints": {
            "concept": "JSON lebih ringkas tanpa tag pembuka/penutup ganda, payload lebih kecil, dan native diparsing ke objek pemrograman.",
            "execution": "Pilih: Memiliki struktur teks lebih ringkas, payload lebih kecil, dan langsung diparsing menjadi objek."
        }
    },
    {
        "id": "inf-lat-m-12",
        "materi": "ANALISIS DATA",
        "topic": "Normalisasi Basis Data: Eliminasi Ketergantungan Parsial pada 2NF",
        "stem": "Sebuah tabel relasional `Nilai_Siswa` memiliki composite primary key `(NISN, Kode_Mapel)` dengan atribut lain: `Nama_Siswa`, `Nama_Mapel`, dan `Nilai_Ujian`. Tabel tersebut belum memenuhi Bentuk Normal Kedua (2NF). Alasan mengapa tabel tersebut melanggar 2NF dan langkah perbaikannya adalah...",
        "correct": "Terdapat Ketergantungan Fungsional Parsial (Partial Dependency), di mana atribut non-kunci `Nama_Siswa` hanya bergantung pada `NISN` dan `Nama_Mapel` hanya bergantung pada `Kode_Mapel`; solusinya adalah memecah tabel menjadi tabel `Siswa`, `Mata_Pelajaran`, dan `Nilai`.",
        "distractors": [
            "Terdapat Ketergantungan Transitif di mana atribut `Nilai_Ujian` menentukan nilai atribut `Nama_Siswa` secara tidak langsung.",
            "Tabel memiliki atribut yang bernilai jamak (multivalued attributes) sehingga melanggar aturan atomitas data dasar.",
            "Kunci utama tabel terdiri atas lebih dari satu kolom yang dilarang keras dalam standar arsitektur SQL relasional.",
            "Tabel tidak memiliki indeks pencarian B-Tree sehingga sistem operasi gagal melakukan pengurutan otomatis."
        ],
        "formula": {
            "title": "DEFINISI BENTUK NORMAL KEDUA (2ND NORMAL FORM / 2NF)",
            "latex": "R \\in \\text{2NF} \\iff R \\in \\text{1NF} \\quad \\land \\quad \\forall A \\notin \\text{Candidate Keys}: \\ A \\text{ tidak bergantung parsial pada sembarang subset kunci}",
            "legend": "• Partial Dependency: $(\\text{NISN}, \\text{Kode\\_Mapel}) \\to \\text{Nama\\_Siswa}$, padahal $\\text{NISN} \\to \\text{Nama\\_Siswa}$ sudah cukup<br>• Solusi Dekomposisi 2NF: Pisahkan atribut parsial ke tabel master masing-masing"
        },
        "hints": {
            "concept": "2NF melarang ketergantungan parsial (atribut non-kunci hanya bergantung pada sebagian dari composite primary key).",
            "execution": "Pilih opsi yang menyebutkan Ketergantungan Fungsional Parsial (Partial Dependency) dan pemecahan tabel."
        }
    },
    {
        "id": "inf-lat-m-13",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Hierarki Resolusi Alamat Domain Name System (DNS)",
        "stem": "Ketika komputer klien mencari alamat IP dari domain `belajar.kemdikbud.go.id` untuk pertama kalinya (cache DNS kosong), resolver rekursif akan menanyai server-server DNS secara berjenjang. Urutan hierarki server DNS yang dihubungi oleh resolver tersebut secara benar adalah...",
        "correct": "Root DNS Server (`.`) $\\rightarrow$ Top-Level Domain (TLD) Server (`.id`) $\\rightarrow$ Second-Level Domain Server (`.go.id`) $\\rightarrow$ Authoritative DNS Server (`kemdikbud.go.id`).",
        "distractors": [
            "Authoritative DNS Server $\\rightarrow$ Root DNS Server $\\rightarrow$ DHCP Server $\\rightarrow$ Web Proxy Gateway.",
            "Internet Service Provider (ISP) Server $\\rightarrow$ Browser Cache $\\rightarrow$ Switch LAN $\\rightarrow$ Client Host.",
            "Top-Level Domain Server $\\rightarrow$ Authoritative Server $\\rightarrow$ Root Server $\\rightarrow$ Web Application Firewall.",
            "Web Hosting Server $\\rightarrow$ Local Router $\\rightarrow$ Cloudflare Server $\\rightarrow$ Google Root Server."
        ],
        "formula": {
            "title": "HIERARKI RESOLUSI REKURSIF DNS GLOBAL",
            "latex": "\\text{Klien} \\xrightarrow{\\text{Query}} \\text{Resolver} \\to \\text{Root DNS (\".\")} \\to \\text{TLD DNS (\".id\")} \\to \\text{SLD (\".go.id\")} \\to \\text{Authoritative DNS}",
            "legend": "• Root DNS: Dikelola oleh 13 identitas server logis global (A-M)<br>• TLD DNS: Mengelola domain tingkat atas (.com, .id, .org, .net)<br>• Authoritative DNS: Memegang basis data catatan DNS asli dari pemilik domain"
        },
        "hints": {
            "concept": "Alur hierarki DNS dari kanan ke kiri: Root (.) -> TLD (.id) -> SLD (.go.id) -> Authoritative (kemdikbud.go.id).",
            "execution": "Pilih: Root DNS Server -> TLD Server -> Second-Level Domain Server -> Authoritative DNS Server."
        }
    },
    {
        "id": "inf-lat-m-14",
        "materi": "SISTEM KOMPUTER",
        "topic": "Mekanisme Penanganan Interupsi Perangkat Keras (Hardware Interrupt)",
        "stem": "Ketika pengguna menekan tombol pada papan ketik (keyboard), pengontrol perangkat keras mengirimkan sinyal Interrupt Request (IRQ) ke CPU melalui Programmable Interrupt Controller (PIC). Urutan langkah yang diambil oleh CPU untuk menangani peristiwa interupsi tersebut adalah...",
        "correct": "CPU menyelesaikan instruksi aktif saat ini $\\rightarrow$ Menyimpan status register dan Program Counter (PC) ke Call Stack $\\rightarrow$ Melompat mengeksekusi rutin Interrupt Service Routine (ISR) keyboard $\\rightarrow$ Memulihkan status register dari stack $\\rightarrow$ Melanjutkan instruksi program semula.",
        "distractors": [
            "CPU langsung mematikan prosesor $\\rightarrow$ Menghapus seluruh memori RAM $\\rightarrow$ Mengulang kembali proses booting komputer dari BIOS/UEFI.",
            "CPU mengabaikan sinyal keyboard hingga seluruh program aktif yang ada di sistem operasi selesai dijalankan.",
            "CPU menyalin seluruh isi hard disk ke memori cache L1 untuk mengantisipasi kerusakan data masukan.",
            "CPU mengubah arsitektur von Neumann menjadi Harvard architecture secara dinamis pada level sirkuit gerbang logika."
        ],
        "formula": {
            "title": "SIKLUS PENANGANAN INTERUPSI (INTERRUPT HANDLING CYCLE)",
            "latex": "\\text{Signal IRQ} \\to \\text{Selesai Siklus Instruksi} \\to \\text{Push Context ke Stack} \\to \\text{Eksekusi ISR} \\to \\text{IRET (Pop Context)} \\to \\text{Resume Program}",
            "legend": "• ISR (Interrupt Service Routine): Handler fungsi di memori kernel OS yang melayani kejadian interupsi spesifik<br>• Context Saving: Menjamin program yang diinterupsi dapat dilanjutkan kembali tanpa kehilangan state data"
        },
        "hints": {
            "concept": "Saat interupsi: CPU simpan status (PC dan register) ke stack, jalankan fungsi penangan (ISR), lalu pulihkan status dan lanjutkan program.",
            "execution": "Pilih urutan: Selesaikan instruksi aktif -> Simpan status/PC ke Stack -> Jalankan ISR -> Pulihkan status -> Lanjutkan program."
        }
    },
    {
        "id": "inf-lat-m-15",
        "materi": "STRUKTUR DATA",
        "topic": "Implementasi Antrean Prioritas Menggunakan Binary Heap",
        "stem": "Struktur data Binary Heap sering digunakan untuk mengimplementasikan antrean prioritas (Priority Queue) pada algoritma jalur terpendek Dijkstra. Jika sebuah Min-Heap berisi $n$ elemen data, kompleksitas waktu asimtotik untuk operasi penyisipan elemen baru (`insert/heapify-up`) dan operasi ekstraksi elemen dengan prioritas terkecil (`extract-min/heapify-down`) secara berturut-turut adalah...",
        "correct": "$O(\\log_2 n)$ untuk penyisipan dan $O(\\log_2 n)$ untuk ekstraksi elemen minimum.",
        "distractors": [
            "$O(1)$ untuk penyisipan dan $O(n)$ untuk ekstraksi elemen minimum.",
            "$O(n)$ untuk penyisipan dan $O(1)$ untuk ekstraksi elemen minimum.",
            "$O(n \\log_2 n)$ untuk penyisipan dan $O(n^2)$ untuk ekstraksi elemen minimum.",
            "$O(1)$ untuk penyisipan dan $O(1)$ untuk ekstraksi elemen minimum konstan."
        ],
        "formula": {
            "title": "KOMPLEKSITAS OPERASI BINARY HEAP",
            "latex": "\\text{Tinggi Pohon } h = \\lfloor \\log_2 n \\rfloor \\implies \\begin{cases} \\text{Insert (Percolate Up):} & O(\\log n) \\\\ \\text{Extract-Min (Percolate Down):} & O(\\log n) \\\\ \\text{Peek Min (Akar):} & O(1) \\\\ \\text{Build Heap (Floyd's):} & O(n) \\end{cases}",
            "legend": "• Sifat Min-Heap: Nilai simpul induk selalu $\\le$ nilai simpul anak-anaknya<br>• Keunggulan dibanding Array Tak Terurut: Ekstraksi minimum $O(\\log n)$ jauh lebih cepat dibanding $O(n)$"
        },
        "hints": {
            "concept": "Tinggi binary heap adalah log(n). Baik penyisipan (bubble-up) maupun ekstraksi akar (bubble-down) membutuhkan waktu O(log n).",
            "execution": "Pilih: O(log n) untuk penyisipan dan O(log n) untuk ekstraksi elemen minimum."
        }
    },
    {
        "id": "inf-lat-m-16",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Prinsip Perlindungan Data Pribadi (UU PDP No. 27 Tahun 2022)",
        "stem": "Undang-Undang Perlindungan Data Pribadi (UU PDP No. 27/2022) di Indonesia mengatur hak-hak subjek data pribadi dan kewajiban pengendali data. Jika seorang pengguna aplikasi pinjaman daring menarik kembali persetujuan pemrosesan datanya dan meminta pengelola aplikasi untuk menghapus seluruh data rekam jejak finansialnya, hak yang sedang digunakan oleh subjek data tersebut adalah...",
        "correct": "Hak untuk Menghapus dan Memusnahkan Data Pribadi (Right to Erasure / Right to be Forgotten), di mana pengendali data wajib menghentikan pemrosesan dan memusnahkan data pribadi pemohon sesuai regulasi hukum.",
        "distractors": [
            "Hak Portabilitas Data, yaitu hak untuk meminta ganti rugi uang tunai atas kegagalan sistem keamanan aplikasi.",
            "Hak Monopoli Komersial, yaitu hak subjek data untuk menjual kembali basis data perusahaan kepada pihak ketiga.",
            "Hak Anonimitas Mutlak, yaitu jaminan bahwa pengguna bebas melakukan transaksi tanpa identitas yang sah secara perbankan.",
            "Hak Imunitas Siber, yaitu pembebasan subjek data dari kewajiban membayar utang pokok pinjaman yang telah disepakati."
        ],
        "formula": {
            "title": "HAK-HAK SUBJEK DATA PRIBADI (PASAL 5 - 13 UU PDP NO. 27/2022)",
            "latex": "\\text{Hak Subjek Data} \\supset \\{\\text{Akses Data}, \\text{Koreksi Kesalahan}, \\text{Penarikan Consent}, \\text{Penghapusan/Pemusnahan Data}, \\text{Portabilitas}\\}",
            "legend": "• Pengendali Data Pribadi: Pihak yang menentukan tujuan dan kendali pemrosesan data<br>• Kewajiban Pengendali Data: Melindungi data dengan enkripsi, memberitahukan insiden kebocoran maksimal 3x24 jam"
        },
        "hints": {
            "concept": "Meminta penghapusan rekam jejak pribadi setelah mencabut consent adalah pelaksanaan hak pemusnahan data (right to erasure/forgotten).",
            "execution": "Pilih: Hak untuk Menghapus dan Memusnahkan Data Pribadi (Right to Erasure)."
        }
    },
    {
        "id": "inf-lat-m-17",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Penelusuran Graf: Karakteristik Algoritma BFS vs DFS",
        "stem": "Dalam mencari rute jalan keluar terpendek pada sebuah labirin (maze) tanpa bobot, seorang pemrogram dapat menggunakan algoritma penelusuran Breadth-First Search (BFS) atau Depth-First Search (DFS). Alasan mengapa BFS dijamin selalu menemukan solusi jalur dengan jumlah langkah paling sedikit dibandingkan DFS adalah...",
        "correct": "BFS menelusuri simpul secara melebar tingkat demi tingkat (level by level) menggunakan struktur data antrean (Queue), sehingga jalur yang pertama kali mencapai simpul tujuan pasti merupakan jalur terpendek.",
        "distractors": [
            "BFS mengeksplorasi satu cabang jalan sedalam mungkin hingga menemui jalan buntu menggunakan tumpukan (Stack).",
            "BFS menghitung bobot nilai heuristik prediksi arah mata angin menggunakan formula trigonometri Euclidean.",
            "BFS mengurutkan seluruh simpul labirin menggunakan algoritma Quicksort sebelum langkah penelusuran dimulai.",
            "DFS selalu membutuhkan waktu komputasi yang tak terhingga karena tidak dapat menandai simpul yang telah dikunjungi."
        ],
        "formula": {
            "title": "KOMPARASI PENELUSURAN GRAF (GRAPH TRAVERSAL)",
            "latex": "\\begin{aligned} \\text{BFS (Breadth-First):} & \\quad \\text{Struktur: Queue (FIFO)} \\implies \\text{Jalur Terpendek pada Graf Tanpa Bobot} \\\\ \\text{DFS (Depth-First):} & \\quad \\text{Struktur: Stack (LIFO) / Rekursif} \\implies \\text{Deteksi Siklus, Topological Sort} \\end{aligned}",
            "legend": "• Kompleksitas Waktu BFS & DFS: $O(V + E)$ dengan adjacency list<br>• Kelemahan DFS untuk rute terpendek: Dapat terjebak di cabang dalam yang bukan merupakan solusi minimum"
        },
        "hints": {
            "concept": "BFS menelusuri lapis demi lapis dengan Queue, menjamin jalur pertama yang sampai adalah yang terpendek pada graf berbobot seragam.",
            "execution": "Pilih: BFS menelusuri simpul tingkat demi tingkat menggunakan Queue sehingga jalur pertama kali mencapai tujuan adalah yang terpendek."
        }
    },
    {
        "id": "inf-lat-m-18",
        "materi": "ANALISIS DATA",
        "topic": "Filter Agregat SQL: Perbedaan Klausa WHERE vs HAVING",
        "stem": "Diberikan tabel `Karyawan` dengan kolom `departemen` dan `gaji`. Manajemen perusahaan ingin mengetahui departemen mana saja yang memiliki rata-rata gaji karyawan di atas Rp 10.000.000,-. Kueri SQL yang benar untuk memenuhi kebutuhan laporan tersebut adalah...",
        "correct": "`SELECT departemen, AVG(gaji) FROM Karyawan GROUP BY departemen HAVING AVG(gaji) > 10000000;`",
        "distractors": [
            "`SELECT departemen, AVG(gaji) FROM Karyawan WHERE AVG(gaji) > 10000000 GROUP BY departemen;`",
            "`SELECT departemen, SUM(gaji) FROM Karyawan WHERE departemen IS NOT NULL ORDER BY AVG(gaji) > 10000000;`",
            "`SELECT departemen FROM Karyawan HAVING gaji > 10000000 GROUP BY departemen;`",
            "`SELECT departemen, AVG(gaji) IN Karyawan FILTER BY AVG(gaji) > 10000000;`"
        ],
        "formula": {
            "title": "URUTAN EKSEKUSI LOGIKA PERINTAH SQL",
            "latex": "\\text{FROM} \\to \\text{WHERE (Filter Baris Individu)} \\to \\text{GROUP BY} \\to \\text{HAVING (Filter Kelompok Agregat)} \\to \\text{SELECT} \\to \\text{ORDER BY}",
            "legend": "• WHERE tidak dapat digunakan bersama fungsi agregasi (AVG, SUM, COUNT)<br>• HAVING secara spesifik diciptakan untuk memfilter hasil setelah fungsi agregasi dikelompokkan oleh GROUP BY"
        },
        "hints": {
            "concept": "Filter pada fungsi agregat (AVG(gaji) > 10000000) wajib menggunakan klausa HAVING setelah GROUP BY, bukan WHERE.",
            "execution": "Pilih kueri yang menggunakan GROUP BY departemen HAVING AVG(gaji) > 10000000."
        }
    },
    {
        "id": "inf-lat-m-19",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Mekanisme Jabat Tangan Tiga Langkah (TCP Three-Way Handshake)",
        "stem": "Sebelum protokol TCP mentransmisikan data aplikasi, koneksi logis yang andal (reliable) harus dibangun antara klien dan server melalui mekanisme TCP 3-Way Handshake. Urutan pertukaran segmen kendali TCP yang tepat pada tahapan tersebut adalah...",
        "correct": "Klien mengirimkan segmen `SYN` (Synchronize) $\\rightarrow$ Server merespons dengan segmen `SYN-ACK` (Synchronize-Acknowledgment) $\\rightarrow$ Klien membalas dengan segmen `ACK` (Acknowledgment).",
        "distractors": [
            "Klien mengirimkan segmen `ACK` $\\rightarrow$ Server membalas `FIN` $\\rightarrow$ Klien mengirimkan segmen data payload.",
            "Klien mengirimkan `RST` $\\rightarrow$ Server membalas `SYN` $\\rightarrow$ Klien merespons dengan `FIN-ACK`.",
            "Server menyiarkan paket `PING` $\\rightarrow$ Klien merespons `PONG` $\\rightarrow$ Gateway memverifikasi sertifikat digital.",
            "Klien mengirimkan `HELLO` $\\rightarrow$ Server merespons `READY` $\\rightarrow$ Klien mengirimkan `START`."
        ],
        "formula": {
            "title": "DIAGRAM ALIR TCP THREE-WAY HANDSHAKE",
            "latex": "\\begin{aligned} \\text{Klien} & \\xrightarrow{\\text{SYN (Seq = } x\\text{)}} \\text{Server} \\\\ \\text{Klien} & \\xleftarrow{\\text{SYN-ACK (Seq = } y, \\text{ Ack = } x + 1\\text{)}} \\text{Server} \\\\ \\text{Klien} & \\xrightarrow{\\text{ACK (Seq = } x + 1, \\text{ Ack = } y + 1\\text{)}} \\text{Server} \\implies \\text{ESTABLISHED} \\end{aligned}",
            "legend": "• Sequence Number: Mengurutkan segmen dan mendeteksi paket hilang<br>• Acknowledgment Number: Mengonfirmasi penerimaan paket berikutnya yang diharapkan<br>• Pelepasan Koneksi (Teardown): Menggunakan 4-Way Handshake (FIN -> ACK -> FIN -> ACK)"
        },
        "hints": {
            "concept": "Tiga langkah koneksi TCP: Klien kirim SYN -> Server balas SYN-ACK -> Klien konfirmasi dengan ACK.",
            "execution": "Pilih: SYN -> SYN-ACK -> ACK."
        }
    },
    {
        "id": "inf-lat-m-20",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Penurunan Kinerja Algoritma Quicksort Menjadi Kasus Terburuk",
        "stem": "Algoritma pengurutan Quicksort rata-rata memiliki kinerja sangat cepat dengan kompleksitas $O(n \\log_2 n)$. Namun, jika implementasi partisi naif selalu memilih elemen pertama atau elemen terakhir sebagai pivot dan larik masukan yang diberikan sudah dalam kondisi terurut sempurna (sorted), kompleksitas waktu Quicksort akan merosot menjadi...",
        "correct": "$O(n^2)$ kuadratik, karena pada setiap tahapan partisi dihasilkan pembagian sub-larik yang sangat timpang tidak seimbang (berukuran $0$ dan $n-1$), sehingga pohon rekursi memiliki kedalaman $n$.",
        "distractors": [
            "$O(1)$ konstan, karena algoritma mendeteksi bahwa larik sudah terurut sehingga langsung menghentikan program.",
            "$O(n)$ linier, karena algoritma hanya melakukan satu kali pengecekan partisi dari depan ke belakang.",
            "$O(n^3)$ kubik, karena perbandingan elemen dilakukan tiga dimensi di dalam ruang memori tumpukan.",
            "$O(\\log_2 n)$, karena partisi yang timpang justru mempercepat penggabungan elemen pivot."
        ],
        "formula": {
            "title": "KASUS TERBURUK ALGORITMA QUICKSORT",
            "latex": "T(n) = T(n - 1) + O(n) = \\sum_{i=1}^n i = \\frac{n(n + 1)}{2} \\implies O(n^2)",
            "legend": "• Kasus Terbaik / Rata-rata ($O(n \\log n)$): Pivot selalu membagi larik menjadi dua bagian seimbang ($n/2$ dan $n/2$)<br>• Mitigasi Kasus Terburuk: Menggunakan teknik Median-of-Three atau Randomized Pivot Selection"
        },
        "hints": {
            "concept": "Pada data terurut dengan pivot di ujung, partisi menjadi 0 dan n-1. Kedalaman pohon menjadi n, kompleksitas memburuk jadi O(n^2).",
            "execution": "Pilih: O(n^2) kuadratik karena partisi sangat timpang (0 dan n-1) dengan kedalaman pohon n."
        }
    },
    {
        "id": "inf-lat-m-21",
        "materi": "SISTEM KOMPUTER",
        "topic": "Arsitektur Kumpulan Instruksi: RISC vs CISC",
        "stem": "Dalam desain prosesor komputer, arsitektur Reduced Instruction Set Computer (RISC) seperti ARM berbeda secara fundamental dengan Complex Instruction Set Computer (CISC) seperti Intel x86. Karakteristik utama dari filosofi arsitektur RISC adalah...",
        "correct": "Memiliki set instruksi sederhana berukuran seragam (fixed-length), sebagian besar instruksi dieksekusi dalam satu siklus clock, serta menerapkan arsitektur Load/Store di mana operasi manipulasi data hanya dapat dilakukan di dalam register CPU.",
        "distractors": [
            "Memiliki instruksi tingkat tinggi berukuran bervariasi yang mampu memanipulasi operan langsung di dalam memori RAM utama.",
            "Tidak memiliki register internal sehingga seluruh perhitungan dilakukan langsung pada sirkuit bus sistem.",
            "Hanya mampu mengeksekusi instruksi program secara sekuensial tanpa mendukung teknik pipelining prosesor.",
            "Membutuhkan perangkat keras mikro-kode (microcode engine) yang rumit untuk memecah instruksi sebelum dieksekusi ALU."
        ],
        "formula": {
            "title": "KOMPARASI ARSITEKTUR SET INSTRUKSI CPU",
            "latex": "\\begin{aligned} \\text{RISC (ARM, RISC-V):} & \\quad \\text{Instruksi Fixed, Eksekusi 1 Siklus, Load/Store Murni, Pipelining Efisien} \\\\ \\text{CISC (x86-64):} & \\quad \\text{Instruksi Variabel, Multi-Siklus, Memanipulasi Memori Langsung, Kaya Fitur} \\end{aligned}",
            "legend": "• Waktu Eksekusi Program: $\\text{Waktu} = (\\text{Jumlah Instruksi}) \\times (\\text{CPI}) \\times (\\text{Waktu Siklus Clock})$<br>• RISC mengoptimalkan CPI $\\approx 1$, sedangkan CISC meminimalkan jumlah instruksi per program"
        },
        "hints": {
            "concept": "Ciri khas RISC: instruksi sederhana berukuran tetap, eksekusi satu siklus, operasi data hanya di register (Load/Store).",
            "execution": "Pilih opsi: Instruksi sederhana berukuran seragam, eksekusi satu siklus clock, dan arsitektur Load/Store."
        }
    },
    {
        "id": "inf-lat-m-22",
        "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
        "topic": "Karakteristik Fungsi Hash Kriptografis dan Efek Avalanche",
        "stem": "Fungsi hash kriptografis seperti SHA-256 digunakan secara luas untuk verifikasi integritas data dan penyimpanan kata sandi. Karakteristik penting di mana perubahan sekecil satu bit saja pada data masukan (input) akan menghasilkan nilai digest hash keluaran yang berubah secara drastis dan acak total disebut...",
        "correct": "Efek Longsoran (Avalanche Effect), yang menjamin bahwa keluaran hash tidak dapat diprediksi hubungannya dengan masukan awal.",
        "distractors": [
            "Collision Resistance, yaitu sifat kemustahilan matematis menemukan dua masukan berbeda yang menghasilkan hash identik.",
            "Pre-image Resistance, yaitu sifat satu arah di mana nilai masukan asli mustahil dihitung balik dari nilai hash.",
            "Zero-Knowledge Proof, yaitu pembuktian kebenaran suatu pernyataan rahasia tanpa mengungkapkan isi rahasia itu sendiri.",
            "Homomorphic Encryption, yaitu kemampuan melakukan operasi komputasi matematika pada teks tersandi tanpa didekripsi."
        ],
        "formula": {
            "title": "PROPERTI MATEMATIS FUNGSI HASH KRIPTOGRAFIS",
            "latex": "x \\xrightarrow{\\text{Flip 1 Bit}} x' \\implies \\text{HammingDistance}(\\text{Hash}(x), \\text{Hash}(x')) \\approx 50\\% \\text{ Total Bits}",
            "legend": "• Avalanche Effect: Mengubah 'cat' menjadi 'bat' mengubah total seluruh 256-bit digest keluaran<br>• Pre-image Resistance: $h = H(m) \\implies$ Sulit mencari $m$ jika hanya diketahui $h$<br>• Collision Resistance: Sulit menemukan $m_1 \\ne m_2$ sedemikian rupa sehingga $H(m_1) = H(m_2)$"
        },
        "hints": {
            "concept": "Perubahan 1 bit input menyebabkan perubahan drastis pada nilai hash output disebut Avalanche Effect (Efek Longsoran).",
            "execution": "Pilih: Efek Longsoran (Avalanche Effect)."
        }
    },
    {
        "id": "inf-lat-m-23",
        "materi": "PRAKTIK LINTAS BIDANG",
        "topic": "Penyelesaian Konflik Penggabungan Cabang (Git Merge Conflict)",
        "stem": "Dua pemrogram bekerja pada repositori Git yang sama dan mengedit baris kode yang sama pada berkas `app.py` di cabang fiturnya masing-masing. Ketika pemrogram kedua mencoba menggabungkan cabangnya menggunakan `git merge feature-b`, terminal menampilkan pesan peringatan `CONFLICT (content): Merge conflict in app.py`. Tindakan teknis yang benar untuk menyelesaikan konflik tersebut adalah...",
        "correct": "Membuka berkas `app.py`, meninjau penanda konflik (`<<<<<<<`, `=======`, `>>>>>>>`), menyunting baris kode untuk memilih atau menggabungkan perubahan yang benar, menghapus penanda konflik, lalu menjalankan `git add app.py` dan `git commit`.",
        "distractors": [
            "Menghapus folder tersembunyi `.git` secara permanen agar riwayat konflik langsung hilang dari komputer.",
            "Menjalankan perintah `git push --force origin main` untuk menimpa seluruh kode di repositori server secara paksa.",
            "Mengganti nama berkas `app.py` menjadi `app_backup.py` lalu membiarkan sistem Git menyelesaikan sendiri secara otomatis.",
            "Mematikan sambungan internet komputer dan menginstal ulang sistem operasi untuk memulihkan kode sumber."
        ],
        "formula": {
            "title": "STRUKTUR PENANDA MERGE CONFLICT PADA GIT",
            "latex": "\\begin{aligned} & \\text{<<<<<<< HEAD (Cabang Saat Ini)} \\\\ & \\text{Kode cabang aktif} \\\\ & \\text{======= (Pemisah)} \\\\ & \\text{Kode cabang yang digabungkan} \\\\ & \\text{>>>>>>> feature-b (Cabang Masuk)} \\end{aligned}",
            "legend": "• Tahap resolusi: Review manual -> Putuskan logika kode -> Hapus marker -> Staging (git add) -> Selesaikan commit (git commit)"
        },
        "hints": {
            "concept": "Menyelesaikan git merge conflict: buka file, edit kode di antara marker conflict, hapus marker, lakukan git add dan git commit.",
            "execution": "Pilih opsi: Buka file, selesaikan penanda konflik secara manual, hapus penanda, lalu git add dan git commit."
        }
    },
    {
        "id": "inf-lat-m-24",
        "materi": "ANALISIS DATA",
        "topic": "Deteksi Pencilan Data (Outlier) Berbasis Interquartile Range (IQR)",
        "stem": "Dalam tahap pembersihan data (data cleaning), seorang analis data memeriksa distribusi gaji karyawan. Dari hasil perhitungan statistik deskriptif diperoleh nilai Kuartil Bawah ($Q_1$) sebesar Rp 6.000.000,- dan Kuartil Atas ($Q_3$) sebesar Rp 14.000.000,-. Menggunakan aturan Tukey berbasis Interquartile Range (IQR), ambang batas atas (upper bound) untuk mengidentifikasi nilai pencilan (outlier) adalah...",
        "correct": "Rp 26.000.000,-, dihitung dari formula $Q_3 + 1,5 \\times \\text{IQR}$, di mana $\\text{IQR} = Q_3 - Q_1 = 14 - 6 = 8$ juta, sehingga $14 + 1,5(8) = 26$ juta.",
        "distractors": [
            "Rp 22.000.000,-, hasil penjumlahan kuartil atas dengan satu kali nilai rentang interkuartil dasar.",
            "Rp 20.000.000,-, nilai tengah dari batas maksimum data gaji normal di perusahaan.",
            "Rp 32.000.000,-, hasil perkalian kuartil atas dengan koefisien variansi populasi dua.",
            "Rp 18.000.000,-, hasil penambahan standar deviasi pada kuartil ketiga statistik sampel."
        ],
        "formula": {
            "title": "DETEKSI PENCILAN DATA METODE TUKEY IQR",
            "latex": "\\begin{aligned} \\text{IQR} & = Q_3 - Q_1 = 14 - 6 = 8 \\text{ Juta} \\\\ \\text{Batas Bawah (Lower Fence)} & = Q_1 - 1,5 \\times \\text{IQR} = 6 - 1,5(8) = -6 \\text{ Juta (0)} \\\\ \\text{Batas Atas (Upper Fence)} & = Q_3 + 1,5 \\times \\text{IQR} = 14 + 1,5(8) = 26 \\text{ Juta} \\end{aligned}",
            "legend": "• Outlier: Setiap titik data $x > \\text{Upper Fence}$ atau $x < \\text{Lower Fence}$<br>• Visualisasi: Ditampilkan sebagai titik-titik di luar kumis (whiskers) pada diagram Box Plot"
        },
        "hints": {
            "concept": "IQR = Q3 - Q1 = 14 - 6 = 8. Batas atas = Q3 + 1.5 * IQR = 14 + 1.5 * 8 = 14 + 12 = 26 juta.",
            "execution": "Pilih: Rp 26.000.000,-."
        }
    },
    {
        "id": "inf-lat-m-25",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Strategi Pencadangan Data 3-2-1 untuk Mitigasi Serangan Siber",
        "stem": "Untuk melindungi data penting sekolah dari ancaman enkripsi malware ransomware dan kerusakan bencana fisik, administrator jaringan menerapkan strategi pencadangan standar industri \"Aturan Cadangan 3-2-1\". Implementasi yang benar dari aturan 3-2-1 tersebut adalah...",
        "correct": "Menyimpan minimal 3 salinan data (1 data produksi asli dan 2 data cadangan), menggunakan 2 jenis media penyimpanan fisik yang berbeda (misalnya SSD server lokal dan Network Attached Storage / pita magnetik), serta menempatkan 1 salinan di lokasi eksternal terpisah (off-site atau cloud terenkripsi).",
        "distractors": [
            "Membuat cadangan data setiap 3 jam sekali, ditinjau oleh 2 teknisi berbeda, dan disimpan selama 1 tahun penuh.",
            "Menyimpan data pada 3 komputer dalam 1 ruangan laboratorium yang sama menggunakan 2 kabel LAN dan 1 sakelar.",
            "Membagi berkas data menjadi 3 pecahan arsip ZIP dengan 2 kata sandi dan 1 kunci pemulihan perangkat keras.",
            "Menyimpan data di 3 flashdisk yang dicolokkan secara terus-menerus pada 2 port USB di 1 komputer server utama."
        ],
        "formula": {
            "title": "ATURAN CADANGAN DATA STRATEGIS 3-2-1",
            "latex": "\\text{Ketahanan Data} \\equiv \\text{3 Salinan Data} + \\text{2 Media Penyimpanan Berbeda} + \\text{1 Salinan di Lokasi Eksternal (Off-site/Cloud)}",
            "legend": "• 3 Copies: Data primer + 2 backup mandiri<br>• 2 Media Types: Mencegah kegagalan bersamaan dari teknologi media yang sama (misal Disk + Cloud/Tape)<br>• 1 Off-site: Melindungi dari kebakaran, banjir, pencurian fisik, dan infeksi ransomware lateral"
        },
        "hints": {
            "concept": "Aturan 3-2-1: 3 salinan data, 2 jenis media berbeda, 1 salinan disimpan off-site / cloud di lokasi terpisah.",
            "execution": "Pilih opsi: 3 salinan data, 2 media penyimpanan berbeda, dan 1 salinan di lokasi terpisah (off-site/cloud)."
        }
    }
]
