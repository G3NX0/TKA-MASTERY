# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Informatika (SMA/MA)
Dataset: Simulasi CBT HOTS (35 Authentic Questions, inf-sim-01 to 35)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
Composition:
  - 25 Authentic Single MCQ HOTS (inf-sim-01 to 25)
  - 5 Complex Multi-select HOTS (inf-sim-26 to 30)
  - 5 Matrix Benar-Salah HOTS (inf-sim-31 to 35)
"""

INFORMATIKA_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 SINGLE MCQ HOTS (inf-sim-01 to inf-sim-25)
    # -------------------------------------------------------------
    {
        "id": "inf-sim-01",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Algoritma Lintasan Terpendek Seluruh Pasangan (Floyd-Warshall)",
        "stem": "Dalam mencari jarak terpendek antar semua pasangan simpul (All-Pairs Shortest Path) pada sebuah graf berarah dengan $|V| = 50$ simpul yang dapat memuat bobot negatif tanpa siklus negatif, pemrogram dapat menggunakan algoritma Floyd-Warshall berbasis pemrograman dinamis dengan matriks $D^{(k)}[i][j]$. Kompleksitas waktu asimtotik dari algoritma Floyd-Warshall tersebut adalah...",
        "correct": "$O(|V|^3)$ kubik, karena algoritma mengeksekusi tiga lapis perulangan bersarang untuk mengevaluasi setiap kemungkinan simpul perantara $k$ dari $1$ hingga $|V|$.",
        "distractors": [
            "$O(|V|^2)$ kuadratik, karena hanya membutuhkan perbandingan langsung antar baris dan kolom matriks ketetanggaan.",
            "$O(|V| \\cdot |E| \\log |V|)$, setara dengan menjalankan algoritma Dijkstra sebanyak $|V|$ kali secara paralel.",
            "$O(|V|!)$, karena mencoba seluruh kemungkinan permutasi urutan simpul satu per satu.",
            "$O(|E| \\log |V|)$, setara dengan pencarian pohon rentang minimum pada graf berbobot tunggal."
        ],
        "formula": {
            "title": "RELASI REKURENSI ALGORITMA FLOYD-WARSHALL",
            "latex": "D^{(k)}[i][j] = \\min\\Big(D^{(k-1)}[i][j], \\ D^{(k-1)}[i][k] + D^{(k-1)}[k][j]\\Big) \\implies \\text{Tiga Nested Loops: } O(|V|^3)",
            "legend": "• $k$: Simpul perantara yang diizinkan (dari himpunan $\\{1, 2, \\dots, k\\}$)<br>• Ruang Memori: $O(|V|^2)$ matriks jarak 2D<br>• Keunggulan: Sangat mudah diimplementasikan untuk graf padat (dense graph) dan mendukung bobot negatif"
        },
        "hints": {
            "concept": "Floyd-Warshall mengevaluasi intermediate vertex k melalui 3 perulangan bersarang (for k, for i, for j), kompleksitasnya O(V^3).",
            "execution": "Pilih: O(|V|^3) kubik karena tiga lapis perulangan bersarang."
        }
    },
    {
        "id": "inf-sim-02",
        "materi": "SISTEM KOMPUTER",
        "topic": "Penentuan Safe Sequence pada Algoritma Banker",
        "stem": "Diberikan sebuah sistem komputasi dengan 3 proses ($P_0, P_1, P_2$) dan satu tipe sumber daya berjumlah 12 unit. Saat ini status alokasi dan kebutuhan maksimum adalah:\n- $P_0$: Alokasi = 4, Max = 9 $\\implies$ Butuh = 5\n- $P_1$: Alokasi = 2, Max = 4 $\\implies$ Butuh = 2\n- $P_2$: Alokasi = 3, Max = 7 $\\implies$ Butuh = 4\nTotal sumber daya teralokasi adalah $4 + 2 + 3 = 9$, sehingga sumber daya yang tersedia (Available) saat ini adalah $12 - 9 = 3$ unit. Urutan eksekusi aman (Safe Sequence) yang menjamin sistem terhindar dari deadlock adalah...",
        "correct": "$\\langle P_1, P_0, P_2 \\rangle$ atau $\\langle P_1, P_2, P_0 \\rangle$, karena hanya $P_1$ yang kebutuhan sumber dayanya ($2$) dapat dipenuhi langsung oleh ketersediaan saat ini ($3$).",
        "distractors": [
            "$\\langle P_0, P_1, P_2 \\rangle$, karena $P_0$ adalah proses dengan prioritas nomor indeks terendah.",
            "$\\langle P_2, P_1, P_0 \\rangle$, karena $P_2$ memiliki alokasi sumber daya awal paling seimbang.",
            "Tidak ada Safe Sequence yang valid sehingga sistem seketika mengalami deadlock permanen.",
            "$\\langle P_0, P_2, P_1 \\rangle$, karena seluruh proses dapat dieksekusi secara simultan tanpa antrean."
        ],
        "formula": {
            "title": "TRACING STATUS AMAN ALGORITMA BANKER",
            "latex": "\\begin{aligned} \\text{Awal Available} = 3 & \\implies \\text{Cek Need}: \\ P_0(5)>3, \\ \\mathbf{P_1(2) \\le 3}, \\ P_2(4)>3 \\implies \\text{Pilih } P_1 \\\\ \\text{Selesai } P_1 & \\implies \\text{Available Baru} = 3 + 2 = \\mathbf{5} \\implies P_0(5) \\le 5 \\text{ atau } P_2(4) \\le 5 \\\\ \\text{Jika Pilih } P_0 & \\implies \\text{Available Baru} = 5 + 4 = 9 \\implies P_2(4) \\le 9 \\implies \\text{Urutan: } \\langle P_1, P_0, P_2 \\rangle \\end{aligned}",
            "legend": "• Safe Sequence membuktikan sistem berada dalam Safe State<br>• Alokasi dikembalikan ke Available saat proses selesai mengeksekusi seluruh tugasnya"
        },
        "hints": {
            "concept": "Available awal = 3. Hanya P1 (butuh 2) yang bisa jalan. Setelah P1 selesai, release 2, available jadi 5. Lalu P0 (butuh 5) atau P2 (butuh 4) bisa jalan.",
            "execution": "Pilih: <P1, P0, P2> atau <P1, P2, P0>."
        }
    },
    {
        "id": "inf-sim-03",
        "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
        "topic": "Mitigasi Serangan ARP Spoofing (Man-in-the-Middle) di Jaringan Lokal",
        "stem": "Dalam jaringan LAN sekolah, penyerang mengirimkan paket balasan ARP palsu (gratuitous ARP) secara berulang ke komputer korban dan gateway, mengklaim bahwa alamat IP default gateway diasosiasikan dengan MAC Address milik penyerang. Akibatnya, seluruh lalu lintas internet korban dibelokkan melalui komputer penyerang (Man-in-the-Middle). Mekanisme keamanan sakelar switch jaringan yang paling efektif untuk mencegah serangan ARP Spoofing ini adalah...",
        "correct": "Dynamic ARP Inspection (DAI), yang bekerja memvalidasi setiap paket balasan ARP terhadap tabel ikatan tepercaya DHCP Snooping Binding Table dan menjatuhkan (drop) paket ARP yang memalsukan pemetaan IP-ke-MAC.",
        "distractors": [
            "Mematikan fungsi penomoran IP dinamis dan membiarkan setiap komputer memilih alamat IP privat secara acak.",
            "Memasang perangkat lunak antivirus pada komputer gateway tanpa mengonfigurasi perangkat keras sakelar switch.",
            "Mengganti seluruh kabel jaringan tembaga dengan kabel nirkabel Wi-Fi tanpa kata sandi akses.",
            "Mengaktifkan protokol Spanning Tree Protocol (STP) untuk memblokir port jaringan yang memiliki nomor ganjil."
        ],
        "formula": {
            "title": "MEKANISME PERTAHANAN DYNAMIC ARP INSPECTION (DAI)",
            "latex": "\\text{Paket ARP} \\xrightarrow{\\text{Masuk Port Untrusted}} \\text{Switch Cek DAI} \\stackrel{?}{\\in} \\text{DHCP Snooping Binding Table} \\implies \\begin{cases} \\text{Cocok} & \\to \\text{Forward} \\\\ \\text{Palsu} & \\to \\text{Drop & Log Alert} \\end{cases}",
            "legend": "• Celah Keamanan Dasar ARP: Protokol ARP bersifat stateless dan tidak memiliki mekanisme otentikasi bawaan<br>• Prasyarat DAI: Fitur DHCP Snooping harus aktif terlebih dahulu untuk mencatat IP-MAC-Port yang sah"
        },
        "hints": {
            "concept": "Fitur switch untuk memvalidasi paket ARP dan mencegah ARP spoofing/poisoning adalah Dynamic ARP Inspection (DAI).",
            "execution": "Pilih: Dynamic ARP Inspection (DAI)."
        }
    },
    {
        "id": "inf-sim-04",
        "materi": "STRUKTUR DATA",
        "topic": "Efisiensi Struktur Data Pohon Awalan (Trie / Prefix Tree)",
        "stem": "Sebuah mesin pencari ingin mengimplementasikan fitur pelengkapan otomatis (autocomplete) dan pemeriksa ejaan (spell checker) untuk kamus berisi $N = 500.000$ kosakata kata bahasa Indonesia. Struktur data Trie (Prefix Tree) dipilih daripada Tabel Hash untuk kebutuhan fitur ini karena...",
        "correct": "Trie mampu mencari seluruh kata yang memiliki awalan (prefix) yang sama dalam waktu $O(k)$ di mana $k$ adalah panjang string masukan, sepenuhnya independen dari total jumlah kata $N$ yang ada di kamus, serta menghemat memori untuk kata-kata dengan prefiks identik.",
        "distractors": [
            "Trie memiliki waktu pencarian instan $O(1)$ untuk semua jenis kueri kemiripan semantik kecerdasan buatan.",
            "Tabel Hash tidak mampu menyimpan data bertipe string teks alfabetik yang memiliki panjang lebih dari 5 huruf.",
            "Trie secara otomatis menerjemahkan kosakata asing ke dalam bahasa komputer biner tanpa kamus terjemahan.",
            "Trie menjamin bahwa tidak ada tabrakan memori fisik karena menyimpan simpul langsung di sirkuit hard disk."
        ],
        "formula": {
            "title": "KOMPLEKSITAS OPERASI STRUKTUR DATA TRIE",
            "latex": "\\begin{aligned} \\text{Pencarian Kata / Awalan (Prefix Search):} & \\quad O(k), \\quad k = \\text{panjang kata (independen dari } N\\text{)} \\\\ \\text{Ruang Memori Simpul Alfabet } \\Sigma: & \\quad O(|\\Sigma| \\cdot k \\cdot N) \\end{aligned}",
            "legend": "• Struktur Simpul Trie: Setiap simpul memuat array pointer penunjuk anak berukuran alfabet (misal 26 huruf) dan flag boolean `isEndOfWord`<br>• Keunggulan vs Hash Table: Hash Table $O(1)$ untuk exact match, namun tidak mampu melakukan prefix query / autocomplete secara efisien"
        },
        "hints": {
            "concept": "Trie unggul untuk autocomplete dan prefix query karena waktu pencariannya O(k) proporsional terhadap panjang kata k, bukan jumlah kata N.",
            "execution": "Pilih: Mampu mencari seluruh kata berawalan sama dalam O(k) independen dari total kata N."
        }
    },
    {
        "id": "inf-sim-05",
        "materi": "ANALISIS DATA",
        "topic": "Tingkat Isolasi Transaksi Basis Data dan Anomali Phantom Read",
        "stem": "Dalam sistem basis data perbankan yang mengimplementasikan prinsip ACID, dua transaksi konkuren dijalankan bersamaan. Transaksi A mengeksekusi kueri `SELECT COUNT(*) FROM Rekening WHERE saldo > 100000000;`. Sesaat kemudian, Transaksi B melakukan `INSERT` baris nasabah baru dengan saldo Rp 150.000.000,- dan melakukan `COMMIT`. Ketika Transaksi A menjalankan kembali kueri hitung yang sama dalam sesi yang sama, jumlah baris bertambah satu. Tingkat isolasi transaksi tertinggi yang mutlak dibutuhkan untuk mencegah fenomena Phantom Read tersebut adalah...",
        "correct": "`SERIALIZABLE`, yang mengunci rentang baris (Range Locks / Predicate Locking) sehingga transaksi konkuren tidak dapat menyisipkan baris baru yang memenuhi kriteria filter transaksi pertama.",
        "distractors": [
            "`READ COMMITTED`, yang hanya mencegah pembacaan data kotor (Dirty Read) dari transaksi yang belum committed.",
            "`REPEATABLE READ`, yang hanya menjamin nilai baris yang telah dibaca tidak berubah, namun masih mengizinkan penyisipan baris baru.",
            "`READ UNCOMMITTED`, yang mengizinkan seluruh transaksi membaca perubahan data yang belum disimpan.",
            "`SNAPSHOT ISOLATION`, yang menghapus seluruh data transaksi nasabah lama secara otomatis."
        ],
        "formula": {
            "title": "TINGKAT ISOLASI TRANSAKSI SQL (ANSI/ISO SQL-92)",
            "latex": "\\begin{array}{|l|c|c|c|} \\hline \\text{Tingkat Isolasi} & \\text{Dirty Read} & \\text{Non-repeatable} & \\text{Phantom Read} \\\\ \\hline \\text{Read Uncommitted} & \\text{Bisa} & \\text{Bisa} & \\text{Bisa} \\\\ \\text{Read Committed} & \\text{Aman} & \\text{Bisa} & \\text{Bisa} \\\\ \\text{Repeatable Read} & \\text{Aman} & \\text{Aman} & \\text{Bisa (Standar SQL)} \\\\ \\mathbf{\\text{Serializable}} & \\mathbf{\\text{Aman}} & \\mathbf{\\text{Aman}} & \\mathbf{\\text{Aman}} \\\\ \\hline \\end{array}",
            "legend": "• Phantom Read: Baris baru muncul di pembacaan kedua dalam transaksi yang sama akibat INSERT konkuren yang telah committed<br>• Serializable: Menjamin eksekusi transaksi konkuren menghasilkan efek yang sama dengan eksekusi serial satu per satu"
        },
        "hints": {
            "concept": "Tingkat isolasi transaksi yang sepenuhnya mencegah Phantom Read adalah SERIALIZABLE.",
            "execution": "Pilih: SERIALIZABLE."
        }
    },
    {
        "id": "inf-sim-06",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Penelusuran Algoritma Longest Common Subsequence (LCS)",
        "stem": "Diberikan dua rantai sekuens DNA: $S_1 = \\text{\"ACCGT\"}$ dan $S_2 = \\text{\"AGCTG\"}$. Panjang dari Sekuens Bagian Terpanjang yang Sama (Longest Common Subsequence / LCS) antara kedua rantai tersebut serta salah satu bentuk sekuensnya adalah...",
        "correct": "Panjang 3, dengan sekuens $\\text{\"ACG\"}$ atau $\\text{\"ACT\"}$.",
        "distractors": [
            "Panjang 5, dengan sekuens $\\text{\"ACCGT\"}$.",
            "Panjang 4, dengan sekuens $\\text{\"ACGT\"}$.",
            "Panjang 2, dengan sekuens $\\text{\"AG\"}$.",
            "Panjang 1, dengan sekuens $\\text{\"A\"}$ saja."
        ],
        "formula": {
            "title": "MATRIKS PEMROGRAMAN DINAMIS LCS",
            "latex": "LCS[i][j] = \\begin{cases} 0 & \\text{jika } i=0 \\lor j=0 \\\\ LCS[i-1][j-1] + 1 & \\text{jika } S_1[i-1] == S_2[j-1] \\\\ \\max(LCS[i-1][j], \\ LCS[i][j-1]) & \\text{jika } S_1[i-1] \\ne S_2[j-1] \\end{cases}",
            "legend": "• S1 = A - C - C - G - T (panjang 5)<br>• S2 = A - G - C - T - G (panjang 5)<br>• Subsequence yang sama berurutan: A -> C -> G (panjang 3) atau A -> C -> T (panjang 3)<br>• Nilai maksimum LCS = 3"
        },
        "hints": {
            "concept": "Karakter yang muncul berurutan di keduanya: A (indeks 0 di keduanya), C (indeks 1 di S1, indeks 2 di S2), G (indeks 3 di S1, indeks 4 di S2) -> 'ACG' (panjang 3).",
            "execution": "Pilih: Panjang 3, dengan sekuens \"ACG\" atau \"ACT\"."
        }
    },
    {
        "id": "inf-sim-07",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Arsitektur Perutean Global Internet Protokol BGP (Border Gateway Protocol)",
        "stem": "Jaringan internet global terdiri atas ribuan Autonomous System (AS) yang saling terhubung dan bertukar informasi rute jaringan menggunakan protokol Border Gateway Protocol (BGP-4). Alasan mengapa BGP diklasifikasikan sebagai protokol Path-Vector (bukan Distance-Vector atau Link-State murni) adalah...",
        "correct": "BGP menyertakan daftar lengkap nomor urutan Autonomous System (atribut AS-Path) yang dilalui oleh sebuah rute iklan ke jaringan tujuan, yang digunakan router untuk menentukan rute kebijakan terbaik dan mendeteksi serta mencegah terbentuknya loop perutean antar AS secara mutlak.",
        "distractors": [
            "BGP mengukur kualitas rute internet secara eksklusif berdasarkan jumlah sakelar switch lokal yang dilewati paket data.",
            "BGP menyiarkan seluruh isi memori kernel router menggunakan gelombang mikro satelit setiap 5 milidetik.",
            "BGP hanya dapat menghubungkan dua komputer yang berada di dalam satu ruangan gedung yang sama.",
            "BGP secara otomatis memblokir seluruh koneksi internet yang menggunakan protokol TCP lapisan keempat."
        ],
        "formula": {
            "title": "PENCEGAHAN LOOP PADA PROTOKOL BGP PATH-VECTOR",
            "latex": "\\text{Router AS } X \\text{ terima rute dengan } \\text{AS-Path: } [A, B, C] \\implies \\begin{cases} \\text{Jika } X \\in [A, B, C] & \\to \\text{DROP (Terdeteksi Routing Loop!)} \\\\ \\text{Jika } X \\notin [A, B, C] & \\to \\text{Terima & Tambahkan } X \\text{ ke AS-Path} \\end{cases}",
            "legend": "• AS (Autonomous System): Kumpulan jaringan di bawah satu administrasi teknis (memiliki ASN unik)<br>• BGP Policy Routing: Pemilihan rute tidak hanya berdasarkan performa teknis tetapi kebijakan bisnis/peering"
        },
        "hints": {
            "concept": "BGP disebut path-vector karena mengiklankan rute beserta lintasan nomor AS (AS-Path) untuk mendeteksi loop perutean internet global.",
            "execution": "Pilih opsi yang menyebutkan penyertaan daftar nomor AS (AS-Path) untuk kebijakan rute dan pencegahan loop."
        }
    },
    {
        "id": "inf-sim-08",
        "materi": "SISTEM KOMPUTER",
        "topic": "Anomali Belady pada Algoritma Penggantian Halaman FIFO",
        "stem": "Dalam evaluasi algoritma penggantian halaman memori virtual (Page Replacement), penambahan jumlah bingkai memori fisik (page frame) secara teoritis diharapkan dapat menurunkan atau minimal mempertahankan jumlah terjadinya page fault. Namun, pada algoritma First-In, First-Out (FIFO), penambahan frame memori fisik dari 3 frame menjadi 4 frame justru dapat menyebabkan jumlah page fault meningkat. Fenomena paradoksikal ini dikenal sebagai...",
        "correct": "Anomali Belady (Belady's Anomaly), yang terjadi karena algoritma FIFO tidak memiliki properti Stack Algorithm (seperti halnya LRU atau Optimal) di mana himpunan halaman pada $m$ frame belum tentu merupakan subset dari himpunan halaman pada $m+1$ frame.",
        "distractors": [
            "Anomali Amdahl, yaitu perlambatan akselerasi pemrosesan paralel saat inti prosesor ditambahkan secara fisik.",
            "Konflik Peterson, yaitu kegagalan algoritma sinkronisasi dua proses dalam menjamin mutual exclusion.",
            "Thrashing Sinkron, yaitu kondisi di mana seluruh disk SSD komputer terbakar akibat frekuensi I/O tinggi.",
            "Deadlock Dine-In, yaitu kebuntuan filosofis sistem akibat kekurangan garpu pemrosesan data."
        ],
        "formula": {
            "title": "ANOMALI BELADY PADA PENGGANTIAN HALAMAN FIFO",
            "latex": "\\text{String Referensi: } 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 \\implies \\begin{cases} 3 \\text{ Frame:} & 9 \\text{ Page Faults} \\\\ 4 \\text{ Frame:} & \\mathbf{10} \\text{ Page Faults (Meningkat!)} \\end{cases}",
            "legend": "• Stack Algorithm: Algoritma di mana $H(m, t) \\subseteq H(m+1, t)$ untuk setiap saat $t$<br>• LRU (Least Recently Used) dan OPT (Belady's Optimal) adalah Stack Algorithm sehingga KEBAL terhadap Anomali Belady"
        },
        "hints": {
            "concept": "Penambahan frame justru menaikkan page fault pada algoritma FIFO disebut Anomali Belady (Belady's Anomaly).",
            "execution": "Pilih: Anomali Belady (Belady's Anomaly)."
        }
    },
    {
        "id": "inf-sim-09",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Kompleksitas Masalah NP-Hard: Travelling Salesperson Problem (TSP)",
        "stem": "Masalah Travelling Salesperson Problem (TSP) menuntut seorang kurir untuk mengunjungi $N$ buah kota tepat satu kali dan kembali ke kota awal dengan total jarak tempuh minimum. Untuk $N = 30$ kota, pendekatan brute-force memeriksa seluruh $(N-1)! / 2$ permutasi rute membutuhkan waktu miliaran tahun komputasi. Strategi komputasional yang paling realistis dan efektif digunakan dalam industri logistik modern untuk menyelesaikan masalah NP-Hard ini adalah...",
        "correct": "Menggunakan Algoritma Heuristik atau Metaheuristik (seperti Algoritma Genetika, Simulated Annealing, atau Ant Colony Optimization) yang mampu menemukan solusi rute yang mendekati optimal (near-optimal) dalam waktu komputasi yang sangat cepat dan wajar.",
        "distractors": [
            "Menunggu terciptanya komputer kuantum komersial karena komputer digital mustahil menyelesaikan masalah kombinatorial.",
            "Mengurangi jumlah kota menjadi 2 kota saja dan membatalkan pesanan pengiriman logistik pada kota-kota lainnya.",
            "Menjalankan algoritma Binary Search pada koordinat garis bujur kota untuk menemukan rute linier langsung.",
            "Menggunakan algoritma Bubble Sort untuk mengurutkan jarak kota berdasarkan kode pos administrasi daerah."
        ],
        "formula": {
            "title": "KOMPLEKSITAS KOMBINATORIAL MASALAH TSP",
            "latex": "\\text{Total Rute Brute-Force} = \\frac{(N - 1)!}{2}, \\quad \\text{Untuk } N = 30 \\implies \\approx 4,42 \\times 10^{30} \\text{ rute (Intractable)}",
            "legend": "• Kategori Masalah: NP-Hard (Optimasi) / NP-Complete (Keputusan)<br>• Heuristik: Mengorbankan jaminan optimalitas mutlak demi efisiensi waktu pemrosesan yang realistis dalam hitungan detik"
        },
        "hints": {
            "concept": "Untuk masalah NP-Hard berukuran besar seperti TSP, gunakan algoritma heuristik/metaheuristik (Algoritma Genetika, Simulated Annealing) untuk menemukan solusi mendekati optimal secara cepat.",
            "execution": "Pilih opsi: Menggunakan Algoritma Heuristik atau Metaheuristik."
        }
    },
    {
        "id": "inf-sim-10",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Mekanisme dan Analisis Ruang In-Place Algoritma Heapsort",
        "stem": "Algoritma pengurutan Heapsort membangun struktur data Max-Heap di dalam larik masukan itu sendiri, lalu menukar elemen maksimum (akar) dengan elemen terakhir larik secara berulang sambil memulihkan sifat heap. Keunggulan teknis utama dari Heapsort dibandingkan dengan Merge Sort adalah...",
        "correct": "Heapsort bekerja secara in-place dengan kompleksitas ruang memori tambahan sebesar $O(1)$ konstan, sedangkan Merge Sort membutuhkan alokasi memori larik tambahan sebesar $O(n)$ untuk proses penggabungan (merge).",
        "distractors": [
            "Heapsort memiliki kompleksitas waktu asimtotik terbaik sebesar $O(1)$ instan pada larik yang belum terurut.",
            "Heapsort bersifat stabil (stable sort) sehingga posisi relatif elemen bernilai kembar selalu terjamin tidak berubah.",
            "Heapsort tidak memerlukan operasi perbandingan antar elemen data sama sekali selama proses pengurutan berlangsung.",
            "Heapsort secara otomatis mengubah prosesor komputer menjadi sistem paralel multi-threading tanpa sistem operasi."
        ],
        "formula": {
            "title": "KOMPARASI ALGORITMA HEAPSORT VS MERGE SORT",
            "latex": "\\begin{array}{|l|c|c|c|} \\hline \\text{Algoritma} & \\text{Waktu (Worst)} & \\text{Ruang Memori (Auxiliary)} & \\text{Stabilitas} \\\\ \\hline \\text{Merge Sort} & O(n \\log n) & O(n) & \\text{Stabil} \\\\ \\mathbf{\\text{Heapsort}} & \\mathbf{O(n \\log n)} & \\mathbf{O(1) \\ (\\text{In-Place})} & \\text{Tidak Stabil} \\\\ \\hline \\end{array}",
            "legend": "• Build Max-Heap (Floyd's Algorithm): Membutuhkan waktu $O(n)$<br>• $n-1$ kali Extract-Max: Membutuhkan waktu $(n - 1) \\times O(\\log n) = O(n \\log n)$<br>• Total Waktu: $O(n \\log n)$ di semua kondisi"
        },
        "hints": {
            "concept": "Keunggulan utama Heapsort atas Merge Sort: Heapsort adalah in-place sorting dengan memori tambahan O(1), sedangkan Merge Sort butuh memori tambahan O(n).",
            "execution": "Pilih: Heapsort bekerja in-place dengan memori tambahan O(1) konstan, sedangkan Merge Sort butuh O(n)."
        }
    },
    {
        "id": "inf-sim-11",
        "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
        "topic": "Komunikasi Real-Time Web: Protokol WebSockets vs HTTP Polling",
        "stem": "Aplikasi dasbor pemantauan sensor lalu lintas perkotaan memerlukan pembaruan data telemetri puluhan kali per detik dengan latensi sekecil mungkin. Arsitektur komunikasi berbasis WebSockets (RFC 6455) jauh lebih unggul dibandingkan HTTP Short/Long Polling untuk kebutuhan ini karena...",
        "correct": "WebSockets membangun satu koneksi TCP persisten dua arah (full-duplex) tunggal setelah jabat tangan HTTP awal, sehingga pesan data dapat dikirimkan secara instan oleh server ke klien (server-push) hanya dengan overhead header frame sebesar 2 hingga 10 byte tanpa overhead header HTTP berulang.",
        "distractors": [
            "HTTP Polling secara otomatis mengompresi data menjadi sinyal inframerah yang kebal terhadap hambatan jarak.",
            "WebSockets tidak menggunakan jaringan internet sama sekali melainkan frekuensi radio gelombang pendek FM lokal.",
            "HTTP Short Polling selalu menjamin nol persen pemborosan bandwidth meskipun tidak ada pembaruan data dari sensor.",
            "WebSockets mewajibkan pengguna untuk melakukan penyegaran halaman peramban (F5) setiap kali data baru masuk."
        ],
        "formula": {
            "title": "KOMPARASI OVERHEAD PROTOKOL REAL-TIME WEB",
            "latex": "\\begin{aligned} \\text{HTTP Polling:} & \\quad \\text{Koneksi Baru / Request Berulang} \\implies \\text{Header Overhead: } \\approx 500 - 1000 \\text{ Bytes/Request} \\\\ \\text{WebSockets:} & \\quad \\text{1x Handshake (TCP Persisten)} \\implies \\text{Header Overhead: } \\mathbf{2 - 10 \\text{ Bytes/Frame (Full-Duplex)}} \\end{aligned}",
            "legend": "• Full-Duplex: Klien dan server dapat mengirimkan data secara simultan bersamaan<br>• Server-Push: Server dapat mengirimkan data secara spontan tanpa menunggu permintaan (request) klien"
        },
        "hints": {
            "concept": "WebSockets membuat koneksi TCP full-duplex persisten dengan overhead header frame sangat kecil (2-10 byte) dan mendukung server-push.",
            "execution": "Pilih opsi yang menjelaskan koneksi TCP persisten full-duplex dengan overhead header sangat kecil (2-10 byte)."
        }
    },
    {
        "id": "inf-sim-12",
        "materi": "ANALISIS DATA",
        "topic": "Pemodelan Dimensi Data Warehouse: Skema Bintang (Star Schema)",
        "stem": "Dalam perancangan basis data analitis Data Warehouse (OLAP), Skema Bintang (Star Schema) sering digunakan untuk mempercepat kueri pelaporan agregat bisnis. Struktur arsitektural yang mendefinisikan Skema Bintang adalah...",
        "correct": "Terdiri atas satu Tabel Fakta (Fact Table) terpusat yang memuat kunci-kunci asing dan metrik pengukuran numerik kuantitatif bisnis, yang dikelilingi oleh sekumpulan Tabel Dimensi (Dimension Tables) yang terdenormalisasi secara langsung tanpa hierarki bertingkat.",
        "distractors": [
            "Terdiri atas tabel-tabel data yang dinormalisasi penuh hingga 3NF dengan rantai relasi bertingkat menyerupai struktur kepingan salju.",
            "Hanya memuat satu tabel tunggal raksasa tanpa adanya hubungan relasi kunci primer dan kunci asing sama sekali.",
            "Tabel-tabel dimensi yang saling terhubung membentuk graf siklis tanpa adanya tabel penampung data numerik.",
            "Tabel data yang disimpan dalam berkas teks terenkripsi di mana setiap baris mewakili konfigurasi perangkat keras server."
        ],
        "formula": {
            "title": "ARSITEKTUR SKEMA BINTANG (STAR SCHEMA)",
            "latex": "\\text{Fact Table (Pusat)} \\longleftrightarrow \\begin{cases} \\text{Dim\\_Waktu} \\\\ \\text{Dim\\_Produk} \\\\ \\text{Dim\\_Cabang} \\\\ \\text{Dim\\_Pelanggan} \\end{cases} \\implies \\text{Denormalized Dimensions (Fast OLAP Queries)}",
            "legend": "• Fact Table: Menyimpan metrik (kuantitas terjual, total omzet) dan foreign keys<br>• Dimension Table: Menyimpan atribut konteks analisis (nama hari, kategori produk, wilayah)<br>• Keunggulan vs Snowflake: Kueri analitis membutuhkan lebih sedikit operasi JOIN"
        },
        "hints": {
            "concept": "Star Schema terdiri dari satu Fact Table di tengah yang dikelilingi oleh Dimension Tables terdenormalisasi.",
            "execution": "Pilih: Satu Tabel Fakta di tengah dikelilingi oleh Tabel Dimensi terdenormalisasi."
        }
    },
    {
        "id": "inf-sim-13",
        "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
        "topic": "Remediasi Kerentanan Injeksi SQL Menggunakan Prepared Statements",
        "stem": "Sebuah aplikasi web otentikasi login memiliki celah keamanan SQL Injection pada baris kode PHP naif berikut:\n```php\n$query = \"SELECT * FROM users WHERE user = '\" . $_POST['username'] . \"' AND pass = '\" . $_POST['password'] . \"'\";\n```\nSeorang penyerang memasukkan nilai `' OR '1'='1` ke dalam kolom username sehingga berhasil masuk tanpa kata sandi. Teknik remediasi standar industri yang paling tepat dan mutlak mampu mencegah serangan SQL Injection tersebut adalah...",
        "correct": "Menggunakan Kueri Berparameter (Parameterized Queries / Prepared Statements), di mana mesin basis data memisahkan secara tegas antara struktur logika kueri SQL dan nilai data masukan pengguna, sehingga masukan berbahaya hanya diperlakukan sebagai literal teks murni dan bukan kode eksekusi.",
        "distractors": [
            "Menghapus seluruh kata kunci `SELECT` dari aplikasi web dan menggantinya dengan berkas spreadsheet.",
            "Mengubah metode permintaan formulir HTML dari `POST` menjadi `GET` pada peramban pengguna.",
            "Mematikan fungsi logging server basis data agar aktivitas peretas tidak tercatat di memori hard disk.",
            "Mengganti seluruh kata sandi pengguna menjadi kombinasi huruf kapital tanpa melibatkan angka numerik."
        ],
        "formula": {
            "title": "REMEDIASI PREPARED STATEMENTS PADA SQL INJECTION",
            "latex": "\\text{Kueri SQL:} \\quad \\text{SELECT * FROM users WHERE user = ? AND pass = ?} \\implies \\text{Input di-bind sebagai Data Murni, Bukan Kode!}",
            "legend": "• Sanitasi String: Penggunaan fungsi escape (addslashes) masih rentan terhadap encoding bypass<br>• Prepared Statements: Solusi mutlak karena kompilasi struktur perintah SQL dilakukan SEBELUM parameter data diinjeksikan"
        },
        "hints": {
            "concept": "Pencegahan utama SQL Injection adalah Parameterized Queries / Prepared Statements yang memisahkan instruksi SQL dari data literal.",
            "execution": "Pilih: Menggunakan Kueri Berparameter (Parameterized Queries / Prepared Statements)."
        }
    },
    {
        "id": "inf-sim-14",
        "materi": "SISTEM KOMPUTER",
        "topic": "Sinkronisasi Utas: Kondisi Balapan (Race Condition) dan Mutex Lock",
        "stem": "Dua utas (threads) yang berjalan secara konkuren mencoba menambah nilai variabel bersama `counter` yang awalnya bernilai 100 secara bersamaan melalui instruksi:\n```c\ncounter = counter + 1;\n```\nPada level bahasa mesin prosesor, instruksi ini dieksekusi menjadi 3 tahapan: (1) `LOAD R, [counter]`; (2) `ADD R, 1`; (3) `STORE [counter], R`. Jika terjadi peralihan konteks tepat di antara langkah 1 dan 3, nilai akhir `counter` dapat menjadi 101 alih-alih 102. Masalah konkuren ini serta mekanisme penguncian yang tepat untuk menyelesaikannya adalah...",
        "correct": "Kondisi Balapan (Race Condition); diselesaikan dengan melindungi blok instruksi tersebut sebagai Bagian Kritis (Critical Section) menggunakan mekanisme penguncian saling mengeluarkan (Mutual Exclusion / Mutex Lock).",
        "distractors": [
            "Fragmentasi Memori; diselesaikan dengan melakukan defragmentasi piringan hard disk secara terjadwal.",
            "Paging Fault; diselesaikan dengan mematikan memori virtual pada pengaturan BIOS motherboard.",
            "Buffer Overflow; diselesaikan dengan memperbesar ukuran register Program Counter CPU.",
            "Deadlock Melingkar; diselesaikan dengan menghentikan secara paksa proses sistem operasi induk."
        ],
        "formula": {
            "title": "SINKRONISASI CRITICAL SECTION DENGAN MUTEX LOCK",
            "latex": "\\text{Acquire(Mutex)} \\to \\mathbf{\\text{Critical Section: } \\text{counter} = \\text{counter} + 1} \\to \\text{Release(Mutex)}",
            "legend": "• Race Condition: Hasil akhir komputasi bergantung pada urutan eksekusi timing non-deterministik antar utas konkuren<br>• Mutex Lock: Menjamin hanya satu utas yang dapat mengakses bagian kritis pada satu satuan waktu"
        },
        "hints": {
            "concept": "Masalah dua thread memanipulasi data bersamaan tanpa sinkronisasi disebut Race Condition. Solusinya dengan Mutex Lock pada Critical Section.",
            "execution": "Pilih: Kondisi Balapan (Race Condition); diselesaikan menggunakan Mutual Exclusion / Mutex Lock."
        }
    },
    {
        "id": "inf-sim-15",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Penelusuran Antrean pada Algoritma Breadth-First Search (BFS)",
        "stem": "Diberikan sebuah graf tak berarah dengan daftar ketetanggaan:\n- $A: [B, C]$\n- $B: [A, D, E]$\n- $C: [A, F]$\n- $D: [B]$\n- $E: [B, F]$\n- $F: [C, E]$\nJika penelusuran Breadth-First Search (BFS) dimulai dari simpul $A$ dan tetangga yang belum dikunjungi dimasukkan ke antrean (Queue) sesuai urutan abjad alfabet, urutan simpul saat dikeluarkan (visited) dari antrean secara lengkap adalah...",
        "correct": "$A \\rightarrow B \\rightarrow C \\rightarrow D \\rightarrow E \\rightarrow F$",
        "distractors": [
            "$A \\rightarrow B \\rightarrow D \\rightarrow E \\rightarrow F \\rightarrow C$",
            "$A \\rightarrow C \\rightarrow F \\rightarrow E \\rightarrow B \\rightarrow D$",
            "$A \\rightarrow B \\rightarrow C \\rightarrow F \\rightarrow E \\rightarrow D$",
            "$A \\rightarrow D \\rightarrow E \\rightarrow B \\rightarrow C \\rightarrow F$"
        ],
        "formula": {
            "title": "TRACING ANTREAN QUEUE ALGORITMA BFS",
            "latex": "\\begin{aligned} \\text{Awal:} & \\quad Q = [A] \\implies \\text{Visit } A, \\text{ Enqueue tetangga } (B, C) \\implies Q = [B, C] \\\\ \\text{Langkah 1:} & \\quad \\text{Visit } B, \\text{ Enqueue tetangga baru } (D, E) \\implies Q = [C, D, E] \\\\ \\text{Langkah 2:} & \\quad \\text{Visit } C, \\text{ Enqueue tetangga baru } (F) \\implies Q = [D, E, F] \\\\ \\text{Langkah 3-5:} & \\quad \\text{Visit } D, E, F \\implies \\text{Urutan: } A \\to B \\to C \\to D \\to E \\to F \\end{aligned}",
            "legend": "• Struktur Data: Queue (FIFO)<br>• Tingkat 0: {A}<br>• Tingkat 1: {B, C}<br>• Tingkat 2: {D, E, F}"
        },
        "hints": {
            "concept": "Tingkat 0: A. Tingkat 1: B, C. Dari B dimasukkan D, E. Dari C dimasukkan F. Maka urutan BFS adalah A, B, C, D, E, F.",
            "execution": "Pilih: A -> B -> C -> D -> E -> F."
        }
    },
    {
        "id": "inf-sim-16",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Taktik Pemerasan Ganda (Double Extortion) pada Serangan Ransomware",
        "stem": "Dalam evolusi ancaman siber terkini, kelompok kriminal ransomware modern tidak hanya mengenkripsi basis data korban untuk meminta tebusan uang dekripsi, tetapi juga menerapkan taktik \"Double Extortion\". Mekanisme operasional dari taktik pemerasan ganda ini adalah...",
        "correct": "Sebelum mengenkripsi sistem korban, penyerang terlebih dahulu mencuri dan menyedot data sensitif rahasia perusahaan (eksdiltrasi data); jika korban menolak membayar tebusan dekripsi karena memiliki cadangan data (backup), penyerang mengancam akan mempublikasikan data rahasia tersebut ke forum gelap (dark web) atau menjualnya ke kompetitor.",
        "distractors": [
            "Penyerang meminta tebusan uang dua kali lipat menggunakan mata uang kripto yang berbeda jenisnya.",
            "Penyerang merusak komponen fisik prosesor dan kartu memori RAM server secara permanen dari jarak jauh.",
            "Penyerang mengirimkan dua jenis virus trojan yang berbeda untuk menginfeksi dua sistem operasi bersamaan.",
            "Penyerang mengharuskan pembayaran tebusan dilakukan oleh dua direktur perusahaan secara serentak."
        ],
        "formula": {
            "title": "ANATOMI TREN RANSOMWARE DOUBLE EXTORTION",
            "latex": "\\text{Tahap 1: Eksfiltrasi Data Rahasia} \\to \\text{Tahap 2: Enkripsi Sistem} \\to \\text{Tahap 3: Pemerasan Tebusan Ganda (Kunci + Non-Bocor)}",
            "legend": "• Kegagalan Backup Konvensional: Backup hanya memulihkan ketersediaan (Availability), tetapi gagal melindungi kerahasiaan (Confidentiality) dari ancaman bocornya data<br>• Mitigasi: Enkripsi data at-rest & in-transit, Data Loss Prevention (DLP), dan segmentasi jaringan ketat"
        },
        "hints": {
            "concept": "Double Extortion memeras dua kali: mengenkripsi sistem DAN mengancam menyebarkan data curian ke publik jika tebusan tak dibayar.",
            "execution": "Pilih opsi: Mencuri data sensitif sebelum enkripsi, lalu mengancam mempublikasikannya ke dark web jika tebusan ditolak."
        }
    },
    {
        "id": "inf-sim-17",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Prinsip Pembentukan Pohon Pengkodean Huffman (Huffman Coding)",
        "stem": "Algoritma kompresi data bebas kehilangan (lossless) Huffman Coding mengalokasikan kode biner dengan panjang bervariasi (variable-length prefix code) untuk setiap karakter teks. Karakter yang memiliki frekuensi kemunculan sangat tinggi di dalam berkas teks akan mendapatkan...",
        "correct": "Kode biner berukuran paling pendek (sedikit bit), yang ditempatkan pada simpul daun yang posisinya paling dekat dengan simpul akar pada Pohon Huffman.",
        "distractors": [
            "Kode biner berukuran paling panjang, yang ditempatkan pada cabang pohon terdalam untuk menjaga keaslian data.",
            "Kode biner berukuran tepat 8-bit tetap yang identik dengan pengkodean karakter ASCII standar.",
            "Dihapus dari berkas teks asli dan digantikan dengan karakter spasi kosong otomatis.",
            "Kode biner acak yang berganti-ganti nilainya setiap kali berkas teks ditransmisikan melalui jaringan."
        ],
        "formula": {
            "title": "PRINSIP OPTIMALITAS PENGKODEAN HUFFMAN",
            "latex": "L_{\\text{avg}} = \\sum_{i=1}^n p_i \\cdot l_i \\implies \\min \\left( \\sum p_i \\cdot l_i \\right) \\iff (p_i > p_j \\implies l_i \\le l_j)",
            "legend": "• $p_i$: Probabilitas/frekuensi karakter $i$<br>• $l_i$: Panjang kode bit karakter $i$<br>• Prefix Rule: Tidak ada kode biner yang menjadi prefiks dari kode biner karakter lain (menjamin dekoding deterministik instan)"
        },
        "hints": {
            "concept": "Prinsip dasar Huffman: Karakter berfrekuensi tinggi diberi kode bit terpendek (dekat dengan akar), frekuensi rendah diberi bit lebih panjang.",
            "execution": "Pilih: Kode biner berukuran paling pendek, ditempatkan paling dekat dengan akar pohon Huffman."
        }
    },
    {
        "id": "inf-sim-18",
        "materi": "ANALISIS DATA",
        "topic": "Pencegahan Kebocoran Data (Data Leakage) pada Machine Learning",
        "stem": "Dalam melatih model prediktif Machine Learning, seorang pemula melakukan standarisasi fitur (skala normalisasi Z-score) pada seluruh dataset gabungan sebelum membaginya menjadi set data pelatihan (training set) dan set data pengujian (test set). Praktik ini merupakan kesalahan fatal metodologis karena menimbulkan masalah...",
        "correct": "Kebocoran Data (Data Leakage), di mana informasi statistik (seperti rata-rata $\\mu$ dan standar deviasi $\\sigma$) dari data pengujian ikut merembes dan mencemari proses pelatihan model, sehingga evaluasi akurasi model menjadi terlalu optimis secara palsu dan berkinerja buruk di dunia nyata.",
        "distractors": [
            "Underfitting Ekstrem, di mana model tidak mampu mempelajari pola data sama sekali akibat ketiadaan parameter.",
            "Galat Sintaksis Kompilasi, yang menyebabkan bahasa pemrograman Python menolak mengeksekusi fungsi scikit-learn.",
            "Kerusakan Hardware Memori RAM, karena dataset terduplikasi secara fisik pada sirkuit motherboard komputer.",
            "Penurunan Resolusi Grafis, di mana diagram visualisasi data kehilangan warna aslinya saat disimpan."
        ],
        "formula": {
            "title": "ALUR KERJA PREPROCESSING DATA YANG BENAR",
            "latex": "\\begin{aligned} \\text{Salah (Data Leakage):} & \\quad \\text{FitScaler}(\\text{Seluruh Data}) \\to \\text{Split Train/Test} \\\\ \\mathbf{\\text{Benar:}} & \\quad \\text{Split Train/Test} \\to \\text{FitScaler}(\\mathbf{\\text{Data Train Saja}}) \\to \\text{Transform}(\\text{Data Train \\& Test}) \\end{aligned}",
            "legend": "• Data Leakage: Menggunakan informasi di luar data latih untuk membangun model<br>• Solusi Arsitektural: Memanfaatkan Scikit-Learn `Pipeline` untuk membungkus transformasi data dan estimator"
        },
        "hints": {
            "concept": "Melakukan scaling sebelum split menyebabkan data leakage (informasi data test bocor ke data train), menghasilkan evaluasi performa palsu.",
            "execution": "Pilih: Kebocoran Data (Data Leakage), informasi statistik data uji merembes ke pelatihan."
        }
    },
    {
        "id": "inf-sim-19",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Ekstensi Keamanan DNS (DNSSEC) dan Pencegahan Cache Poisoning",
        "stem": "Dalam serangan DNS Cache Poisoning, penyerang membanjiri resolver DNS dengan catatan alamat IP palsu sehingga mengarahkan korban ke situs web phishing tiruan. Ekstensi keamanan DNSSEC (DNS Security Extensions) dirancang untuk memitigasi serangan ini secara fundamental dengan cara...",
        "correct": "Mengotentikasi keabsahan respons kueri DNS menggunakan tanda tangan digital kriptografi asimetris (catatan RRSIG) yang divalidasi melalui rantai kepercayaan hierarkis (Chain of Trust) dari zona root hingga domain otoritatif.",
        "distractors": [
            "Mengenkrpsi seluruh kueri DNS sehingga nama domain yang dicari tidak dapat dibaca oleh penyedia ISP lokal.",
            "Mengganti seluruh server DNS global dengan alamat IP tunggal yang dijaga oleh petugas kepolisian internasional.",
            "Memaksa seluruh peramban web untuk menghafal seluruh alamat IP situs web di seluruh dunia tanpa bertanya ke resolver.",
            "Memblokir semua situs web yang memiliki ekstensi domain selain `.com` dan `.id` secara permanen."
        ],
        "formula": {
            "title": "RANTAI KEPERCAYAAN DNSSEC (CHAIN OF TRUST)",
            "latex": "\\text{Root Key (KSK)} \\xrightarrow{\\text{DS Record}} \\text{TLD Key} \\xrightarrow{\\text{DS Record}} \\text{Zone Key (ZSK)} \\xrightarrow{\\text{RRSIG}} \\text{A Record (IP Valid)}",
            "legend": "• RRSIG: Tanda tangan digital atas kumpulan record DNS<br>• DNSKEY: Kunci publik yang digunakan resolver untuk memverifikasi RRSIG<br>• DS (Delegation Signer): Hash dari kunci DNS anak yang disimpan di zona induk<br>• Catatan: DNSSEC menjamin Integritas & Otentikasi, BUKAN Kerahasiaan (DNS over HTTPS / DoH yang menangani privasi)"
        },
        "hints": {
            "concept": "DNSSEC mengotentikasi respon DNS dengan tanda tangan digital kriptografis (RRSIG) melalui rantai kepercayaan hierarkis (Chain of Trust).",
            "execution": "Pilih opsi: Mengotentikasi keabsahan respons DNS menggunakan tanda tangan digital kriptografi asimetris (RRSIG) via Chain of Trust."
        }
    },
    {
        "id": "inf-sim-20",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Analisis Waktu Teramortisasi (Amortized Time Complexity) Array Dinamis",
        "stem": "Struktur data Array Dinamis (seperti `std::vector` pada C++ atau `list` pada Python) menggandakan kapasitas tampung memorinya menjadi dua kali lipat ($2 \\times$) setiap kali ukuran array penuh saat operasi `append` data baru dipanggil. Meskipun proses penggandaan kapasitas membutuhkan alokasi memori baru dan penyalinan seluruh $n$ elemen sebelumnya ($O(n)$ pada operasi tersebut), kompleksitas waktu teramortisasi (amortized time complexity) per operasi `append` adalah...",
        "correct": "$O(1)$ konstan, karena operasi ekspansi yang mahal ($O(n)$) terjadi sangat jarang (hanya pada kelipatan pangkat dua $1, 2, 4, 8, \\dots, 2^k$), sehingga biaya total ekspansi terbagi rata ke seluruh rangkaian operasi penyisipan.",
        "distractors": [
            "$O(n)$ linier, karena setiap kali operasi append dipanggil prosesor harus memeriksa seluruh isi array.",
            "$O(\\log_2 n)$, karena kapasitas array bertambah secara logaritmik setiap kali tombol keyboard ditekan.",
            "$O(n^2)$ kuadratik, karena penyalinan elemen membutuhkan perbandingan bersarang di dalam memori cache.",
            "$O(0)$, karena alokasi memori tidak memakan waktu prosesor komputer sama sekali."
        ],
        "formula": {
            "title": "METODE AGREGASI ANALISIS TERAMORTISASI (DOUBLING STRATEGY)",
            "latex": "\\text{Total Biaya } n \\text{ Operasi} = n + \\sum_{j=0}^{\\lfloor \\log_2 n \\rfloor} 2^j = n + (2n - 1) < 3n \\implies T_{\\text{amortized}} = \\frac{\\text{Total Biaya}}{n} = \\frac{< 3n}{n} = O(1)",
            "legend": "• Operasi mahal jarang terjadi: $n$ operasi hanya memicu $\\log_2 n$ kali resizing<br>• Kelemahan Worst-Case Tunggal: Operasi append saat kapasitas pas penuh tetap memakan waktu $O(n)$"
        },
        "hints": {
            "concept": "Strategi doubling pada vector/list membuat biaya total n operasi adalah < 3n, sehingga biaya rata-rata per operasi adalah O(1) teramortisasi.",
            "execution": "Pilih: O(1) konstan teramortisasi."
        }
    },
    {
        "id": "inf-sim-21",
        "materi": "SISTEM KOMPUTER",
        "topic": "Arsitektur Virtualisasi: Hypervisor Tipe 1 vs Hypervisor Tipe 2 vs Kontainer",
        "stem": "Dalam pusat data komputasi awan (Cloud Computing), teknologi virtualisasi digunakan untuk memaksimalkan utilisasi perangkat keras server fisik. Perbedaan arsitektural mendasar antara Virtual Machine berbasis Hypervisor Tipe 1 (Bare-Metal seperti VMware ESXi / KVM) dan Kontainerisasi (seperti Docker) adalah...",
        "correct": "Virtual Machine memvirtualisasikan perangkat keras fisik penuh dan menjalankan kernel sistem operasi tamu (Guest OS) mandiri di setiap instance, sedangkan Kontainer berbagi kernel sistem operasi host yang sama dan hanya mengisolasi ruang pengguna (user-space via cgroups dan namespaces) sehingga jauh lebih ringan dan cepat dimulai.",
        "distractors": [
            "Kontainer membutuhkan perangkat keras server fisik terpisah untuk setiap aplikasi yang dijalankan.",
            "Virtual Machine tidak dapat menjalankan sistem operasi berbasis Linux sama sekali di dalam pusat data.",
            "Kontainer memiliki ukuran berkas citra (image) puluhan gigabyte yang jauh lebih besar daripada berkas Virtual Disk.",
            "Hypervisor Tipe 1 berjalan di atas sistem operasi komersial Windows Desktop seperti halnya aplikasi biasa."
        ],
        "formula": {
            "title": "KOMPARASI STACK VIRTUALISASI VS KONTAINERISASI",
            "latex": "\\begin{aligned} \\text{VM (Hypervisor Tipe 1):} & \\quad [\\text{Hardware}] \\to [\\text{Hypervisor}] \\to [\\mathbf{\\text{Guest OS}} + \\text{Bins/Libs} + \\text{App}] \\implies \\text{Isolasi Kuat, Berat} \\\\ \\text{Container (Docker):} & \\quad [\\text{Hardware}] \\to [\\mathbf{\\text{Host OS (Shared Kernel)}}] \\to [\\text{Container Engine}] \\to [\\text{Bins/Libs} + \\text{App}] \\implies \\text{Ringan, Instan} \\end{aligned}",
            "legend": "• Guest OS Overhead: VM memakan RAM gigabytes untuk kernel OS masing-masing<br>• Kontainer: Menggunakan Linux Namespaces (isolasi PID, NET, MNT) dan Control Groups (cgroups untuk batas CPU/RAM)"
        },
        "hints": {
            "concept": "VM memvirtualisasikan hardware dan punya OS/kernel sendiri. Kontainer berbagi kernel host yang sama via namespaces & cgroups sehingga jauh lebih ringan.",
            "execution": "Pilih: VM menjalankan kernel Guest OS mandiri, sedangkan Kontainer berbagi kernel host yang sama dengan isolasi user-space."
        }
    },
    {
        "id": "inf-sim-22",
        "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
        "topic": "Algoritma Time-Based One-Time Password (TOTP RFC 6238)",
        "stem": "Aplikasi otentikator dua faktor (2FA seperti Google Authenticator) menghasilkan 6 digit kode sandi sekali pakai yang berganti setiap 30 detik tanpa memerlukan koneksi internet aktif pada ponsel pengguna. Mekanisme komputasi yang digunakan oleh algoritma Time-Based One-Time Password (TOTP RFC 6238) tersebut adalah...",
        "correct": "Menghitung nilai counter waktu diskret $T = \\lfloor (\\text{Unix Time Saat Ini} - T_0) / 30 \\rfloor$, lalu mengevaluasi nilai Hash-based Message Authentication Code (HMAC-SHA1) menggunakan kunci rahasia bersama (shared secret key) yang dipindai saat registrasi QR Code awal, kemudian memangkas hasilnya menjadi 6 digit angka melalui Dynamic Truncation.",
        "distractors": [
            "Menerima sinyal siaran gelombang radio GPS satelit rahasia yang dikirimkan langsung oleh server aplikasi ke ponsel.",
            "Mengirimkan permintaan kueri HTTP POST rahasia melalui jaringan seluler tersembunyi setiap 30 detik secara terus-menerus.",
            "Membaca nomor seri perangkat keras kartu SIM pengguna dan membaginya dengan angka tahun kabisat kalender.",
            "Menghasilkan bilangan acak murni yang ditebak secara telepati komputasional oleh server web autentikasi."
        ],
        "formula": {
            "title": "FORMULA ALGORITMA TOTP (RFC 6238)",
            "latex": "T = \\left\\lfloor \\frac{\\text{Unix Epoch Time}}{30} \\right\\rfloor, \\quad \\text{TOTP} = \\text{Truncate}\\Big(\\text{HMAC-SHA1}(K, T)\\Big) \\pmod{10^6}",
            "legend": "• $K$: Kunci rahasia bersama (Shared Secret) berbentuk Base32 yang disimpan saat memindai QR code<br>• $T$: Penghitung interval waktu 30 detik yang tersinkronisasi antara ponsel dan server via NTP<br>• Truncate: Mengambil 4-byte integer dinamis dari 20-byte digest hash HMAC"
        },
        "hints": {
            "concept": "TOTP menghitung counter T = UnixTime / 30, lalu di-hash dengan shared secret memakai HMAC-SHA1, lalu dipangkas (truncated) menjadi 6 digit.",
            "execution": "Pilih opsi yang menjelaskan perhitungan counter waktu T = (Unix Time / 30), evaluasi HMAC-SHA1 dengan kunci rahasia bersama, dan Dynamic Truncation."
        }
    },
    {
        "id": "inf-sim-23",
        "materi": "PRAKTIK LINTAS BIDANG",
        "topic": "Ketahanan Sistem Terdistribusi: Circuit Breaker Pattern",
        "stem": "Dalam arsitektur mikroservis perbankan, Layanan Pembayaran memanggil API Layanan Pengecekan Skor Kredit secara berkala melalui jaringan. Jika server skor kredit mengalami mati total (down) dan responsnya hang, Layanan Pembayaran akan kehabisan thread penampung antrean permintaan koneksi (connection pool exhaustion) sehingga ikut tumbang, memicu kegagalan beruntun (cascading failure) ke seluruh sistem. Pola desain ketahanan perangkat lunak yang paling tepat untuk mengisolasi dan memitigasi kegagalan ini adalah...",
        "correct": "Pola Pemutus Arus (Circuit Breaker Pattern); jika rasio kegagalan panggilan layanan eksternal melampaui ambang batas, sirkuit berpindah ke status 'Open' dan langsung mengembalikan respons kegagalan instan (fallback) tanpa membuang waktu memanggil layanan yang rusak, lalu secara berkala beralih ke status 'Half-Open' untuk menguji pemulihan layanan.",
        "distractors": [
            "Pola Singleton Pattern; membatasi jumlah objek layanan pembayaran hanya satu instansiasi di seluruh memori server.",
            "Pola Infinite Retry Pattern; secara agresif mengirimkan jutaan panggilan permintaan baru setiap milidetik ke server yang mati.",
            "Pola Monolithic Migration; menghapus seluruh repositori Git dan menulis ulang program menggunakan satu berkas kode tunggal.",
            "Pola Factory Method; membuat kelas turunan baru untuk menampung data kartu kredit nasabah secara manual."
        ],
        "formula": {
            "title": "STATE MACHINE POLA CIRCUIT BREAKER",
            "latex": "\\begin{aligned} \\mathbf{\\text{Closed:}} & \\quad \\text{Operasi normal} \\xrightarrow{\\text{Tingkat Galat } > \\text{ Threshold}} \\mathbf{\\text{Open}} \\\\ \\mathbf{\\text{Open:}} & \\quad \\text{Semua panggilan langsung di-reject (Fail Fast / Fallback)} \\xrightarrow{\\text{Sleep Window Habis}} \\mathbf{\\text{Half-Open}} \\\\ \\mathbf{\\text{Half-Open:}} & \\quad \\text{Izinkan beberapa panggilan uji coba} \\implies \\begin{cases} \\text{Sukses} & \\to \\mathbf{\\text{Closed}} \\\\ \\text{Gagal} & \\to \\mathbf{\\text{Open}} \\end{cases} \\end{aligned}",
            "legend": "• Manfaat: Mencegah thread starvation, mengurangi beban pada layanan yang sedang bermasalah, dan mempertahankan stabilitas sistem utama"
        },
        "hints": {
            "concept": "Pola untuk mencegah cascading failure dengan memutus panggilan ke servis yang mati dan memberikan fallback instan adalah Circuit Breaker Pattern.",
            "execution": "Pilih: Circuit Breaker Pattern (status Closed -> Open -> Half-Open)."
        }
    },
    {
        "id": "inf-sim-24",
        "materi": "ANALISIS DATA",
        "topic": "Asumsi Fundamental Pengklasifikasi Naive Bayes",
        "stem": "Pengklasifikasi Naive Bayes sering digunakan untuk mendeteksi pesan spam surel berdasarkan kemunculan kata-kata teks. Alasan mengapa algoritma klasifikasi probabilistik berbasis Teorema Bayes ini dinamakan \"Naive\" (lugu/naif) adalah...",
        "correct": "Algoritma membuat asumsi penyederhanaan yang sangat kuat dan naif bahwa setiap fitur atribut (keberadaan kata dalam pesan) saling independen bersyarat (conditionally independent) satu sama lain terhadap kelas target, mengabaikan fakta nyata bahwa dalam bahasa manusia keberadaan suatu kata sering kali berkorelasi erat dengan kata lainnya.",
        "distractors": [
            "Algoritma tidak mampu melakukan kalkulasi matematika pecahan desimal sehingga seluruh angka dibulatkan ke nol.",
            "Algoritma hanya dapat dilatih menggunakan data buatan yang dibuat oleh manusia tanpa algoritma komputasi.",
            "Algoritma secara naif mengasumsikan bahwa semua pengirim surel di dunia adalah peretas berbahaya.",
            "Algoritma membutuhkan waktu pelatihan jutaan jam komputasi karena tidak memiliki rumus probabilitas tertutup."
        ],
        "formula": {
            "title": "TEOREMA NAIVE BAYES DENGAN ASUMSI INDEPENDENSI BERSYARAT",
            "latex": "P(C_k \\mid x_1, \\dots, x_n) \\propto P(C_k) \\prod_{i=1}^n P(x_i \\mid C_k)",
            "legend": "• Asumsi Naif: $P(x_1, x_2, \\dots, x_n \\mid C_k) = \\prod_{i=1}^n P(x_i \\mid C_k)$<br>• Keunggulan: Menghindari perhitungan distribusi probabilitas gabungan eksponensial yang mustahil dihitung pada dimensi besar<br>• Tetap bekerja sangat baik di dunia nyata untuk klasifikasi teks dan spam filtering"
        },
        "hints": {
            "concept": "Disebut \"Naive\" karena mengasumsikan semua fitur saling independen secara bersyarat (conditionally independent) terhadap kelas target, padahal di realita ada korelasi antar kata.",
            "execution": "Pilih opsi: Mengasumsikan setiap fitur saling independen bersyarat satu sama lain terhadap kelas target."
        }
    },
    {
        "id": "inf-sim-25",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Privasi Kriptografis Zero-Knowledge Proofs (ZKP)",
        "stem": "Dalam era perlindungan data identitas digital, protokol Zero-Knowledge Proof (ZKP) memungkinkan pihak pembukti (Prover) untuk meyakinkan pihak pemverifikasi (Verifier) bahwa suatu pernyataan rahasia adalah benar (misalnya membuktikan bahwa usia pemohon sudah di atas 17 tahun untuk membeli tiket film dewasa), dengan karakteristik kriptografis yang luar biasa yaitu...",
        "correct": "Tanpa perlu mengungkapkan informasi rahasia itu sendiri atau data pribadi pendukung lainnya (seperti tanggal lahir asli, nama lengkap, atau nomor NIK) kepada pihak pemverifikasi.",
        "distractors": [
            "Dengan mengirimkan seluruh salinan kartu identitas KTP fisik asli melalui surel publik tanpa enkripsi.",
            "Dengan mewajibkan pihak pemverifikasi untuk menyerahkan kunci privat rekening banknya kepada pihak pembukti.",
            "Dengan cara menghapus seluruh catatan transaksi di peladen pemerintah secara sepihak dan permanen.",
            "Hanya berlaku jika kedua belah pihak menandatangani kontrak hukum di hadapan notaris resmi di kantor pengadilan."
        ],
        "formula": {
            "title": "TIGA PROPERTI PROTOKOL ZERO-KNOWLEDGE PROOFS (ZKP)",
            "latex": "\\text{ZKP} \\equiv \\begin{cases} \\mathbf{\\text{Completeness:}} & \\text{Jika pernyataan benar, Verifier jujur pasti yakin} \\\\ \\mathbf{\\text{Soundness:}} & \\text{Jika pernyataan salah, Prover penipu tidak bisa meyakinkan Verifier} \\\\ \\mathbf{\\text{Zero-Knowledge:}} & \\text{Verifier tidak mempelajari apapun selain fakta bahwa pernyataan tersebut benar} \\end{cases}",
            "legend": "• Implementasi Modern: zk-SNARKs pada teknologi blockchain, otentikasi identitas berdaulat mandiri (Self-Sovereign Identity)"
        },
        "hints": {
            "concept": "Zero-Knowledge Proof membuktikan kebenaran sebuah pernyataan TANPA membocorkan isi rahasia itu sendiri (zero knowledge leak).",
            "execution": "Pilih: Tanpa perlu mengungkapkan informasi rahasia atau data pribadi pendukung kepada pihak pemverifikasi."
        }
    },

    # -------------------------------------------------------------
    # 5 COMPLEX MULTI-SELECT HOTS (inf-sim-26 to inf-sim-30)
    # -------------------------------------------------------------
    {
        "id": "inf-sim-26",
        "type": "multi",
        "materi": "BERPIKIR KOMPUTASIONAL & TEORI KOMPLEKSITAS",
        "topic": "Karakteristik Kelas Kompleksitas Masalah Komputasi (P, NP, NP-Complete)",
        "stem": "Dalam teori komputasi teoritis, klasifikasi masalah komputasi terbagi menjadi kelas P, NP, NP-Complete, dan NP-Hard. Manakah TIGA pernyataan berikut yang secara ilmiah BENAR mengenai kelas kompleksitas masalah tersebut? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Masalah dalam kelas P (Polynomial Time) dapat diselesaikan oleh mesin Turing deterministik dalam waktu polinomial $O(n^k)$."},
            {"key": "B", "text": "Masalah dalam kelas NP (Nondeterministic Polynomial Time) adalah masalah keputusan yang solusi usulannya (certificate) dapat diverifikasi kebenarannya dalam waktu polinomial."},
            {"key": "C", "text": "Sebuah masalah $X$ diklasifikasikan sebagai NP-Complete jika $X \\in \\text{NP}$ dan setiap masalah lain di kelas NP dapat direduksi ke $X$ dalam waktu polinomial (Polynomial-Time Reduction)."},
            {"key": "D", "text": "Hingga saat ini telah terbukti secara matematis bahwa kelas masalah P sama persis dengan kelas masalah NP ($P = NP$)."},
            {"key": "E", "text": "Seluruh masalah dalam kelas NP-Complete dapat diselesaikan dalam waktu logaritmik $O(\\log n)$ oleh komputer kuantum personal."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "RELASI HIMPUNAN KELAS KOMPLEKSITAS KOMPUTASI",
            "latex": "P \\subseteq NP, \\quad \\text{NP-Complete} = NP \\cap \\text{NP-Hard}",
            "legend": "• A BENAR: Definisi kelas P (Deterministic Polynomial Time)<br>• B BENAR: Definisi kelas NP (Polynomially Verifiable)<br>• C BENAR: Definisi NP-Complete menurut Teorema Cook-Levin<br>• D dan E SALAH: Masalah $P \\stackrel{?}{=} NP$ adalah Millennium Prize Problem terbuka; NP-Complete belum terbukti bisa diselesaikan logaritmik"
        },
        "hints": {
            "concept": "Kelas P: diselesaikan dalam waktu polinomial (A). Kelas NP: diverifikasi dalam waktu polinomial (B). NP-Complete: anggota NP dan semua masalah NP bisa direduksi secara polinomial ke masalah tersebut (C). P vs NP masih problem terbuka.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "inf-sim-27",
        "materi": "SISTEM KOMPUTER",
        "topic": "Penyebab Terjadinya Fenomena Thrashing pada Memori Virtual",
        "stem": "Thrashing adalah kondisi kritis di mana sistem operasi menghabiskan lebih banyak waktu untuk melakukan pertukaran halaman memori (paging/swapping) antara RAM dan hard disk daripada mengeksekusi instruksi program, sehingga utilisasi CPU anjlok mendekati nol. Manakah TIGA faktor berikut yang menjadi pemicu utama terjadinya fenomena Thrashing? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Derajat multiprogramming (Degree of Multiprogramming) dinaikkan terlalu tinggi sehingga terlalu banyak proses aktif yang bersaing memperebutkan alokasi memori fisik yang terbatas."},
            {"key": "B", "text": "Jumlah bingkai memori fisik (page frames) yang dialokasikan untuk setiap proses berada di bawah ukuran kebutuhan himpunan kerja minimumnya (Working-Set Size)."},
            {"key": "C", "text": "Proses-proses yang sedang berjalan memiliki sifat lokalitas referensi (Locality of Reference) yang sangat buruk atau mengakses memori secara acak melintasi rentang alamat yang teramat luas."},
            {"key": "D", "text": "Kapasitas media penyimpanan sekunder SSD telah terisi penuh 100% sehingga tidak ada ruang swap file yang tersedia sama sekali."},
            {"key": "E", "text": "Sistem operasi menggunakan algoritma penjadwalan CPU Round-Robin dengan kuantum waktu yang terlalu besar."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "MODEL WORKING-SET PENCEGAHAN THRASHING",
            "latex": "D = \\sum_{i} WSS_i > \\text{Total RAM Frames} \\implies \\text{Terjadi Thrashing!}",
            "legend": "• A, B, C BENAR: Ketika total kebutuhan working-set seluruh proses ($D$) melebihi total frame RAM fisik, proses akan saling merebut halaman memori satu sama lain secara terus-menerus<br>• Solusi OS: Turunkan derajat multiprogramming (suspend beberapa proses sementara)"
        },
        "hints": {
            "concept": "Pemicu Thrashing: derajat multiprogramming terlalu tinggi (A), alokasi frame kurang dari working-set (B), dan rusaknya locality of reference (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "inf-sim-28",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Fitur Modern Protokol Keamanan Transport Layer Security (TLS 1.3)",
        "stem": "Protokol keamanan web TLS 1.3 (RFC 8446) membawa lompatan besar dalam hal performa latensi dan ketahanan kriptografi dibandingkan versi TLS pendahulunya. Manakah TIGA fitur pembaharuan kunci berikut yang diperkenalkan pada standar TLS 1.3? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Memangkas waktu negosiasi jabat tangan (handshake latency) dari 2-RTT menjadi hanya 1-RTT untuk sambungan baru, dan mendukung mode 0-RTT (Zero Round Trip Time) untuk koneksi berulang."},
            {"key": "B", "text": "Menghapus secara permanen seluruh cipher suite dan algoritma kriptografi yang usang dan rentan, seperti RSA key exchange statis, CBC mode, RC4, MD5, dan SHA-1."},
            {"key": "C", "text": "Mewajibkan penggunaan Forward Secrecy secara mutlak melalui algoritma pertukaran kunci Diffie-Hellman Ephemeral (DHE / ECDHE) sehingga rekaman data masa lalu tidak dapat didekripsi jika kunci privat server bocor di masa depan."},
            {"key": "D", "text": "Menghapus kewajiban sertifikat digital X.509 sehingga siapa saja dapat menyamar sebagai server bank tanpa otoritas Certificate Authority (CA)."},
            {"key": "E", "text": "Menggantikan seluruh alamat IP versi 4 menjadi alamat MAC address fisik pada lapisan aplikasi."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "EVOLUSI PROTOKOL KEAMANAN TLS 1.2 KE TLS 1.3",
            "latex": "\\begin{aligned} \\text{TLS 1.2:} & \\quad \\text{Handshake: 2-RTT}, \\ \\text{Dukung RSA Key Exchange (No Forward Secrecy)}, \\ \\text{Banyak Algoritma Usang} \\\\ \\text{TLS 1.3:} & \\quad \\mathbf{\\text{Handshake: 1-RTT / 0-RTT}}, \\ \\mathbf{\\text{PFS Mutlak (ECDHE Saja)}}, \\ \\mathbf{\\text{Hanya AEAD Ciphers (AES-GCM/ChaCha20)}} \\end{aligned}",
            "legend": "• A, B, C BENAR: Karakteristik revolusioner TLS 1.3<br>• D dan E SALAH: CA tetap wajib untuk otentikasi identitas publik"
        },
        "hints": {
            "concept": "TLS 1.3: Handshake lebih cepat (1-RTT/0-RTT) (A), menghapus cipher usang (B), dan mewajibkan Perfect Forward Secrecy via ephemeral key exchange (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "inf-sim-29",
        "materi": "ANALISIS DATA",
        "topic": "Karakteristik Transaksi ACID pada Basis Data Relasional",
        "stem": "Prinsip ACID (Atomicity, Consistency, Isolation, Durability) menjamin integritas pemrosesan data finansial di dalam sistem manajemen basis data relasional (RDBMS). Manakah TIGA pernyataan berikut yang mendefinisikan pilar ACID secara tepat? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Atomicity (Keutuhan) menjamin bahwa transaksi dieksekusi dengan prinsip 'semua atau tidak sama sekali' (all-or-nothing); jika salah satu operasi gagal, seluruh perubahan dibatalkan (rollback) ke kondisi awal."},
            {"key": "B", "text": "Isolation (Keterisolasian) menjamin bahwa eksekusi transaksi konkuren berjalan independen tanpa saling mencemari status antara satu sama lain sebelum transaksi di-commit."},
            {"key": "C", "text": "Durability (Ketahanan) menjamin bahwa begitu transaksi berhasil di-commit, seluruh perubahannya tersimpan secara permanen di media penyimpanan non-volatile dan tidak akan hilang meskipun terjadi pemadaman listrik seketika."},
            {"key": "D", "text": "Consistency menjamin bahwa basis data tidak memerlukan kunci primer (Primary Key) dalam merelasikan entitas data."},
            {"key": "E", "text": "Atomicity menjamin bahwa kecepatan eksekusi kueri transaksi selalu berjalan di bawah 1 milidetik terlepas dari volume data."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "DEFINISI EMPAT PILAR TRANSAKSI BASIS DATA ACID",
            "latex": "\\text{ACID} \\equiv \\begin{cases} \\mathbf{\\text{A (Atomicity):}} & \\text{All-or-Nothing (Rollback jika gagal)} \\\\ \\mathbf{\\text{C (Consistency):}} & \\text{Mempertahankan seluruh invariant dan integritas skema DB} \\\\ \\mathbf{\\text{I (Isolation):}} & \\text{Transaksi konkuren tidak saling mengganggu (Concurrecy Control)} \\\\ \\mathbf{\\text{D (Durability):}} & \\text{Perubahan commit bersifat permanen (Write-Ahead Logging / WAL)} \\end{cases}",
            "legend": "• A, B, C BENAR: Definisi formal Atomicity, Isolation, dan Durability<br>• D dan E SALAH: Consistency justru menjaga aturan integritas, dan ACID tidak mengatur batas kecepatan waktu milidetik"
        },
        "hints": {
            "concept": "Pilar ACID: Atomicity adalah all-or-nothing (A), Isolation adalah eksekusi konkuren terisolasi (B), Durability adalah permanen pasca-commit meski mati listrik (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "inf-sim-30",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Tiga Kondisi Kasus pada Teorema Master Asimtotik",
        "stem": "Teorema Master digunakan untuk menyelesaikan relasi rekurensi algoritma bertipe divide-and-conquer dalam bentuk $T(n) = aT(n/b) + f(n)$ dengan $a \\ge 1$ dan $b > 1$. Manakah TIGA pernyataan berikut yang BENAR mengenai kasus Teorema Master? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Jika fungsi kerja pembagian/penggabungan $f(n) = O(n^{\\log_b a - \\epsilon})$ untuk suatu konstanta $\\epsilon > 0$, maka kompleksitas waktu didominasi oleh daun pohon rekursi dengan solusi $T(n) = \\Theta(n^{\\log_b a})$ (Kasus 1)."},
            {"key": "B", "text": "Jika fungsi kerja $f(n) = \\Theta(n^{\\log_b a})$, maka biaya pada setiap level pohon rekursi adalah seimbang sehingga solusinya adalah $T(n) = \\Theta(n^{\\log_b a} \\log_2 n)$ (Kasus 2)."},
            {"key": "C", "text": "Jika fungsi kerja $f(n) = \\Omega(n^{\\log_b a + \\epsilon})$ untuk $\\epsilon > 0$ dan memenuhi kondisi keteraturan $a f(n/b) \\le c f(n)$ dengan $c < 1$, maka solusinya didominasi oleh akar dengan $T(n) = \\Theta(f(n))$ (Kasus 3)."},
            {"key": "D", "text": "Teorema Master dapat digunakan untuk menyelesaikan semua jenis relasi rekurensi tanpa syarat, termasuk jika $a < 1$ atau $b$ bernilai pecahan negatif."},
            {"key": "E", "text": "Algoritma Binary Search memiliki nilai $a = 2$ dan $b = 2$ sehingga diselesaikan menggunakan Kasus 1 Teorema Master."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "FORMULASI MATEMATIS TEOREMA MASTER",
            "latex": "T(n) = aT(n/b) + f(n) \\implies \\text{Bandingkan } f(n) \\text{ dengan } n^{\\log_b a} \\implies \\begin{cases} \\text{Kasus 1:} & f(n) < n^{\\log_b a} \\implies T(n) = \\Theta(n^{\\log_b a}) \\\\ \\text{Kasus 2:} & f(n) = n^{\\log_b a} \\implies T(n) = \\Theta(n^{\\log_b a} \\log n) \\\\ \\text{Kasus 3:} & f(n) > n^{\\log_b a} \\implies T(n) = \\Theta(f(n)) \\end{cases}",
            "legend": "• A, B, C BENAR: Tiga pilar kasus fundamental Teorema Master<br>• D SALAH: Ada syarat regularitas dan keterbatasan fungsi<br>• E SALAH: Binary Search memiliki $a = 1$ (hanya memanggil 1 sub-masalah), $b = 2$, dan $f(n) = O(1)$"
        },
        "hints": {
            "concept": "Tiga kasus Teorema Master: Kasus 1 didominasi daun (A), Kasus 2 seimbang per level dikali log n (B), Kasus 3 didominasi akar f(n) dengan syarat keteraturan (C).",
            "execution": "Pilih A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH HOTS (inf-sim-31 to inf-sim-35)
    # -------------------------------------------------------------
    {
        "id": "inf-sim-31",
        "type": "matrix",
        "materi": "ARSITEKTUR SISTEM KOMPUTER & MEMORI",
        "topic": "Karakteristik Arsitektur Prosesor, Hierarki Memori, dan Eksekusi Instruksi",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai arsitektur sistem komputer modern dan manajemen memori!",
        "statements": [
            {
                "text": "Program Counter (PC) adalah register CPU yang bertugas menyimpan alamat memori dari instruksi berikutnya yang akan diambil (fetched) untuk dieksekusi.",
                "correct": True
            },
            {
                "text": "Memori SRAM (Static RAM) yang digunakan pada Cache Memory membutuhkan penyegaran berkala (refresh cycle) ribuan kali per detik seperti halnya DRAM pada RAM utama.",
                "correct": False
            },
            {
                "text": "Dalam arsitektur Harvard, bus instruksi dan bus data dipisahkan secara fisik sehingga CPU dapat membaca instruksi dan data secara bersamaan tanpa saling menunggu.",
                "correct": True
            },
            {
                "text": "Memori virtual (Virtual Memory) memungkinkan ukuran total alokasi memori proses melampaui kapasitas fisik RAM yang terpasang di komputer.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP PERANGKAT KERAS & ARSITEKTUR KOMPUTER",
            "latex": "\\text{Arsitektur Von Neumann (Shared Bus)} \\iff \\text{Arsitektur Harvard (Separate Code/Data Buses)}",
            "legend": "• Pernyataan 1 BENAR: Fungsi mutlak Program Counter (PC)<br>• Pernyataan 2 SALAH: SRAM menggunakan sirkuit bistable flip-flop sehingga TIDAK memerlukan refresh cycle (DRAM yang butuh kapasitor refresh)<br>• Pernyataan 3 BENAR: Karakteristik utama arsitektur Harvard<br>• Pernyataan 4 BENAR: Esensi memori virtual berbasis swapping/paging ke disk"
        },
        "hints": {
            "concept": "PC menyimpan alamat instruksi berikutnya. SRAM tidak butuh refresh (DRAM yang butuh refresh). Arsitektur Harvard memisahkan bus instruksi dan data. Virtual memory memungkinkan memori melebihi RAM fisik.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "inf-sim-32",
        "type": "matrix",
        "materi": "STRUKTUR DATA & ALGORITMA",
        "topic": "Sifat Struktur Data Linear, Pohon, dan Kompleksitas Algoritma",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai struktur data dan efisiensi algoritma!",
        "statements": [
            {
                "text": "Operasi penelusuran In-Order pada Binary Search Tree (BST) selalu menghasilkan barisan data simpul yang terurut menaik (ascending).",
                "correct": True
            },
            {
                "text": "Algoritma Merge Sort bersifat in-place dan tidak membutuhkan alokasi memori tambahan sama sekali selama proses penggabungan larik.",
                "correct": False
            },
            {
                "text": "Struktur data Queue menerapkan prinsip FIFO (First-In First-Out) dan digunakan sebagai struktur pendukung utama pada penelusuran Breadth-First Search (BFS).",
                "correct": True
            },
            {
                "text": "Algoritma Binary Search dapat dieksekusi dengan kompleksitas O(log n) pada struktur data Singly Linked List yang elemennya sudah terurut.",
                "correct": False
            }
        ],
        "formula": {
            "title": "EVALUASI STRUKTUR DATA DAN KOMPLEKSITAS",
            "latex": "\\text{BST In-Order} \\implies \\text{Sorted}, \\quad \\text{Merge Sort Aux Mem} = O(n), \\quad \\text{Binary Search Linked List} = O(n) \\text{ (No Random Access!)}",
            "legend": "• Pernyataan 1 BENAR: Sifat khas BST<br>• Pernyataan 2 SALAH: Merge Sort membutuhkan larik bantu $O(n)$ (bukan in-place)<br>• Pernyataan 3 BENAR: Hubungan fundamental Queue dan BFS<br>• Pernyataan 4 SALAH: Linked list tidak memiliki akses acak $O(1)$ ke indeks tengah, sehingga Binary Search pada linked list tetap memakan waktu $O(n)$"
        },
        "hints": {
            "concept": "BST In-order menghasilkan urutan terurut menaik. Merge Sort butuh memori tambahan O(n). Queue menerapkan FIFO dan dipakai BFS. Binary Search tidak efisien di Linked List karena tidak ada akses acak O(1) ke elemen tengah.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "inf-sim-33",
        "type": "matrix",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Lapisan Model OSI, Protokol Transport, dan Pengalamatan IP",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai protokol jaringan komputer dan internet!",
        "statements": [
            {
                "text": "Router bekerja pada Lapisan Jaringan (Layer 3 OSI) dan meneruskan paket data berdasarkan alamat logis IP Address tujuan.",
                "correct": True
            },
            {
                "text": "Protokol UDP menjamin paket data tiba secara utuh dan berurutan dengan menyertakan mekanisme konfirmasi ACK dan retransmisi paket rusak.",
                "correct": False
            },
            {
                "text": "Subnet mask /26 pada IPv4 menyediakan total 62 alamat host yang dapat dikonfigurasi secara valid untuk perangkat klien.",
                "correct": True
            },
            {
                "text": "Domain Name System (DNS) menggunakan protokol TCP pada port 53 untuk kueri resolusi nama domain standar dari komputer klien.",
                "correct": False
            }
        ],
        "formula": {
            "title": "STANDAR JARINGAN DAN PROTOKOL INTERNET",
            "latex": "\\text{Router (L3 IP)}, \\quad \\text{UDP (Unreliable)}, \\quad \\text{/26} \\implies 2^6 - 2 = 62, \\quad \\text{DNS Query (Port 53 UDP)}",
            "legend": "• Pernyataan 1 BENAR: Router adalah perangkat Layer 3 OSI<br>• Pernyataan 2 SALAH: Mekanisme ACK dan retransmisi adalah milik TCP, bukan UDP<br>• Pernyataan 3 BENAR: Host bits $= 32 - 26 = 6 \\implies 2^6 - 2 = 62$ host valid<br>• Pernyataan 4 SALAH: Kueri standar DNS klien menggunakan UDP port 53 (TCP hanya dipakai untuk zone transfer antar server)"
        },
        "hints": {
            "concept": "Router beroperasi di Layer 3 OSI. UDP tidak memiliki mekanisme ACK dan retransmisi (itu fitur TCP). /26 memiliki 64 - 2 = 62 host valid. DNS query standar menggunakan UDP port 53, bukan TCP.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "inf-sim-34",
        "type": "matrix",
        "materi": "BASIS DATA RELASIONAL & ANALISIS DATA",
        "topic": "Integritas Basis Data, Aturan Normalisasi, dan Eksekusi Kueri SQL",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai perancangan basis data relasional dan analisis SQL!",
        "statements": [
            {
                "text": "Kunci Utama (Primary Key) sebuah tabel basis data boleh bernilai NULL selama nilai tersebut tidak berulang dengan baris lain.",
                "correct": False
            },
            {
                "text": "Sebuah tabel relasional dikatakan memenuhi Bentuk Normal Kedua (2NF) jika telah memenuhi 1NF dan tidak memiliki ketergantungan fungsional parsial.",
                "correct": True
            },
            {
                "text": "Klausa WHERE dalam kueri SQL dieksekusi sebelum pengelompokan GROUP BY, sedangkan klausa HAVING dieksekusi setelah pengelompokan GROUP BY.",
                "correct": True
            },
            {
                "text": "Operasi INNER JOIN antara dua tabel selalu mengembalikan jumlah baris yang sama dengan operasi FULL OUTER JOIN.",
                "correct": False
            }
        ],
        "formula": {
            "title": "PRINSIP BASIS DATA RELASIONAL DAN NORMALISASI",
            "latex": "\\text{PK} \\ne \\text{NULL}, \\quad \\text{2NF} \\implies \\text{No Partial FD}, \\quad \\text{WHERE} \\to \\text{GROUP BY} \\to \\text{HAVING}, \\quad \\text{INNER} \\subseteq \\text{OUTER}",
            "legend": "• Pernyataan 1 SALAH: Primary Key secara mutlak tidak boleh bernilai NULL (Entity Integrity)<br>• Pernyataan 2 BENAR: Definisi baku 2NF<br>• Pernyataan 3 BENAR: Urutan pemrosesan logika kueri SQL<br>• Pernyataan 4 SALAH: FULL OUTER JOIN mengikutsertakan baris yang tidak cocok dari kedua sisi sehingga barisnya hampir selalu lebih banyak daripada INNER JOIN"
        },
        "hints": {
            "concept": "Primary Key mutlak NOT NULL. 2NF melarang ketergantungan parsial. WHERE memfilter sebelum GROUP BY, HAVING setelahnya. FULL OUTER JOIN menghasilkan baris yang lebih banyak atau sama dengan INNER JOIN.",
            "execution": "Pernyataan 1: Salah; Pernyataan 2: Benar; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "inf-sim-35",
        "type": "matrix",
        "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
        "topic": "Prinsip Enkripsi, Integritas Hash, dan Etika Keamanan Informasi",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai kriptografi dan keamanan informasi!",
        "statements": [
            {
                "text": "Pada algoritma kriptografi kunci simetris seperti AES, kunci yang digunakan untuk proses enkripsi identik dengan kunci yang digunakan untuk proses dekripsi.",
                "correct": True
            },
            {
                "text": "Fungsi hash kriptografis seperti SHA-256 dapat didekripsi kembali menjadi teks pesan aslinya jika menggunakan kunci privat yang tepat.",
                "correct": False
            },
            {
                "text": "Tanda Tangan Digital (Digital Signature) dibuat oleh pengirim dengan mengenkripsi hash dokumen menggunakan kunci privat (Private Key) miliknya sendiri.",
                "correct": True
            },
            {
                "text": "Model keamanan Zero Trust mengasumsikan bahwa semua perangkat yang terhubung ke jaringan Wi-Fi internal kantor dapat dipercaya secara otomatis tanpa autentikasi berulang.",
                "correct": False
            }
        ],
        "formula": {
            "title": "PRINSIP FONDASI KRIPTOGRAFI DAN ZERO TRUST",
            "latex": "\\text{Simetris: } K_{\\text{enc}} = K_{\\text{dec}}, \\quad \\text{Hash: One-Way (No Decryption)}, \\quad \\text{Signature: Encrypt with PrivKey}, \\quad \\text{Zero Trust: Never Trust}",
            "legend": "• Pernyataan 1 BENAR: Ciri khas algoritma kunci simetris<br>• Pernyataan 2 SALAH: Fungsi hash adalah fungsi satu arah (one-way function) dan tidak dapat didekripsi<br>• Pernyataan 3 BENAR: Definisi pembentukan Digital Signature<br>• Pernyataan 4 SALAH: Zero Trust justru berasumsi bahwa jaringan internal TIDAK tepercaya (Never Trust, Always Verify)"
        },
        "hints": {
            "concept": "Kriptografi simetris menggunakan kunci yang sama untuk enkripsi dan dekripsi. Fungsi hash bersifat satu arah dan tidak bisa didekripsi. Digital signature dibuat dengan kunci privat pengirim. Zero Trust tidak pernah mempercayai perangkat otomatis.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    }
]
