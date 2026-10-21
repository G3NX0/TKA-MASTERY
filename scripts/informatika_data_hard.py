# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Informatika (SMA/MA)
Dataset: Latihan Tingkat Hard (25 Authentic Questions, inf-lat-h-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

INFORMATIKA_HARD_ITEMS = [
    {
        "id": "inf-lat-h-01",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Formulasi Rekurensi 0/1 Knapsack Problem Berbasis Dynamic Programming",
        "stem": "Diberikan $n$ buah barang, di mana barang ke-$i$ memiliki bobot $w_i$ dan nilai keuntungan $v_i$. Sebuah ransel memiliki batas kapasitas tampung maksimum $W$. Setiap barang hanya dapat diambil satu kali atau ditinggalkan sama sekali (0/1 Knapsack). Relasi rekurensi matriks pemrograman dinamis $DP[i][w]$ yang menyatakan nilai keuntungan maksimum yang dapat diperoleh dari subset barang $1$ sampai $i$ dengan kapasitas ransel tersisa $w$ adalah...",
        "correct": "$DP[i][w] = \\max(DP[i-1][w], \\ DP[i-1][w - w_i] + v_i)$ untuk kondisi $w \\ge w_i$, dan $DP[i][w] = DP[i-1][w]$ jika $w < w_i$, dengan kompleksitas waktu pseudo-polinomial $O(n \\cdot W)$.",
        "distractors": [
            "$DP[i][w] = DP[i-1][w] + \\min(DP[i][w - w_i], v_i)$, dengan kompleksitas waktu eksponensial $O(2^{n+W})$.",
            "$DP[i][w] = \\frac{v_i}{w_i} \\times DP[i-1][w]$, dengan kompleksitas waktu polinomial murni $O(n \\log n)$.",
            "$DP[i][w] = DP[i-1][w - 1] + DP[i - 1][w + 1] - v_i$, dengan kompleksitas waktu konstan $O(1)$.",
            "$DP[i][w] = \\sum_{k=1}^i \\left( \\frac{w}{w_k} \\cdot v_k \\right)$, yang mengasumsikan barang dapat dipotong menjadi pecahan desimal tak hingga."
        ],
        "formula": {
            "title": "FORMULASI PEMROGRAMAN DINAMIS 0/1 KNAPSACK",
            "latex": "DP[i][w] = \\begin{cases} DP[i-1][w] & \\text{jika } w < w_i \\\\ \\max\\Big(DP[i-1][w], \\ DP[i-1][w - w_i] + v_i\\Big) & \\text{jika } w \\ge w_i \\end{cases}",
            "legend": "• Kasus 1 (Tidak Ambil Barang i): Nilai optimal sama dengan baris sebelumnya pada kapasitas $w$<br>• Kasus 2 (Ambil Barang i): Nilai barang $v_i$ ditambah keuntungan optimal kapasitas sisa $(w - w_i)$<br>• Kompleksitas Waktu: $O(n \\cdot W)$ (Pseudo-polynomial time)<br>• Ruang Memori: Dapat dioptimasi menjadi array 1 dimensi $O(W)$ dengan iterasi mundur"
        },
        "hints": {
            "concept": "Pada 0/1 Knapsack, keputusan biner: ambil barang ke-i (jika kapasitas muat) atau lewatkan. Nilai adalah maksimum dari kedua pilihan tersebut.",
            "execution": "Pilih formula DP: DP[i][w] = max(DP[i-1][w], DP[i-1][w - w_i] + v_i)."
        }
    },
    {
        "id": "inf-lat-h-02",
        "materi": "SISTEM KOMPUTER",
        "topic": "Penanganan Bahaya Data (Data Hazard RAW) pada Pipelining CPU",
        "stem": "Dalam prosesor berpita pipa (pipelined CPU) 5 tahap (IF, ID, EX, MEM, WB), diberikan dua instruksi berurutan berikut:\n```assembly\nADD R1, R2, R3   ; R1 = R2 + R3 (Hasil ditulis pada tahap WB)\nSUB R4, R1, R5   ; R4 = R1 - R5 (R1 dibaca pada tahap ID)\n```\nInstruksi `SUB` membutuhkan nilai register `R1` yang baru saja dihitung oleh `ADD`. Jika prosesor tidak menggunakan stall (gelembung tunda), teknik arsitektur perangkat keras yang tepat untuk menyelesaikan bahaya data Read-After-Write (RAW) ini dalam siklus tercepat adalah...",
        "correct": "Penerusan Data (Data Forwarding / Bypassing), yaitu menyalurkan hasil perhitungan ALU dari tahap EX atau register perantara EX/MEM milik instruksi `ADD` secara langsung ke input ALU pada tahap EX milik instruksi `SUB` tanpa menunggu tahap WB selesai.",
        "distractors": [
            "Prediksi Cabang Dinamis (Dynamic Branch Prediction), yaitu menebak hasil perhitungan R1 menggunakan tabel Branch Target Buffer (BTB).",
            "Instruksi NOP Injection, yaitu menyisipkan sepuluh instruksi kosong ke dalam memori RAM utama untuk menghentikan clock.",
            "Cache Invalidation, yaitu menghapus seluruh baris cache data L1 agar register R1 dipaksa dimuat ulang dari SSD.",
            "Spekulasi Eksekusi Terbalik, yaitu membalik urutan eksekusi instruksi SUB sebelum instruksi ADD dimulai."
        ],
        "formula": {
            "title": "DATA FORWARDING PADA PIPELINE MIPS 5-STAGE",
            "latex": "\\begin{aligned} \\text{Instruksi 1 (ADD):} & \\quad \\text{IF} \\to \\text{ID} \\to \\mathbf{\\text{EX}} \\xrightarrow{\\text{Forwarding Path}} \\text{MEM} \\to \\text{WB (Tulis R1)} \\\\ \\text{Instruksi 2 (SUB):} & \\quad \\text{IF} \\to \\text{ID} \\to \\mathbf{\\text{EX (Terima R1)}}\\text{ via Multiplexer} \\to \\text{MEM} \\to \\text{WB} \\end{aligned}",
            "legend": "• Hazard RAW: Instruksi berikutnya mencoba membaca register sebelum instruksi sebelumnya menulis kembali hasil akhir<br>• Solusi Tanpa Forwarding: Membutuhkan 2 stall cycle (bubble)<br>• Solusi Dengan Forwarding: 0 stall cycle untuk operasi ALU-ke-ALU"
        },
        "hints": {
            "concept": "Teknik meneruskan hasil kalkulasi ALU langsung dari output pipeline EX ke input ALU instruksi berikutnya disebut Data Forwarding (Bypassing).",
            "execution": "Pilih: Data Forwarding / Bypassing."
        }
    },
    {
        "id": "inf-lat-h-03",
        "materi": "STRUKTUR DATA",
        "topic": "Penyeimbangan Pohon AVL: Operasi Rotasi Ganda Left-Right",
        "stem": "Sebuah pohon biner seimbang AVL Tree memiliki faktor keseimbangan (Balance Factor) yang didefinisikan sebagai $\\text{BF}(N) = \\text{tinggi}(\\text{kiri}) - \\text{tinggi}(\\text{kanan})$. Jika sebuah penyisipan simpul baru menyebabkan simpul $A$ memiliki $\\text{BF}(A) = +2$ dan anak kirinya simpul $B$ memiliki $\\text{BF}(B) = -1$ (kondisi Left-Right / LR Inbalance), rangkaian operasi rotasi yang wajib dilakukan untuk memulihkan keseimbangan pohon AVL tersebut adalah...",
        "correct": "Rotasi Kiri pada simpul anak $B$ terlebih dahulu (mengubah kondisi menjadi Left-Left), diikuti dengan Rotasi Kanan pada simpul induk $A$ (Left-Right Double Rotation).",
        "distractors": [
            "Satu kali Rotasi Kanan tunggal secara langsung pada simpul induk $A$ tanpa memodifikasi simpul anak $B$.",
            "Rotasi Kanan pada simpul anak $B$ diikuti dengan Rotasi Kiri pada simpul induk $A$ (Right-Left Double Rotation).",
            "Dua kali Rotasi Kiri berturut-turut pada simpul induk $A$ hingga seluruh simpul berpindah ke sisi kanan.",
            "Menghapus simpul yang baru disisipkan secara permanen karena struktur AVL menolak penyisipan asimetris."
        ],
        "formula": {
            "title": "ROTASI GANDA PADA POHON AVL (LEFT-RIGHT DOUBLE ROTATION)",
            "latex": "\\begin{aligned} \\text{Kondisi Awal (LR):} & \\quad \\text{BF}(A) = +2, \\quad \\text{BF}(\\text{LeftChild}(A)) = -1 \\\\ \\text{Langkah 1 (Rotasi Kiri pada B):} & \\quad B \\xrightarrow{\\text{Left Rotate}} C \\implies \\text{Pohon berubah menjadi format Left-Left (LL)} \\\\ \\text{Langkah 2 (Rotasi Kanan pada A):} & \\quad A \\xrightarrow{\\text{Right Rotate}} C \\implies \\text{Simpul } C \\text{ naik menjadi akar baru terpusat} \\end{aligned}",
            "legend": "• Syarat AVL Tree: $\\text{BF} \\in \\{-1, 0, +1\\}$ untuk setiap simpul<br>• LL Inbalance ($+2, +1$): Cukup 1 Rotasi Kanan<br>• RR Inbalance ($-2, -1$): Cukup 1 Rotasi Kiri<br>• LR Inbalance ($+2, -1$): Rotasi Kiri pada anak, lalu Rotasi Kanan pada induk<br>• RL Inbalance ($-2, +1$): Rotasi Kanan pada anak, lalu Rotasi Kiri pada induk"
        },
        "hints": {
            "concept": "Kasus Left-Right (LR) diselesaikan dengan rotasi ganda: rotasi kiri pada anak kiri (B), lalu rotasi kanan pada induk (A).",
            "execution": "Pilih: Rotasi Kiri pada simpul anak B, diikuti Rotasi Kanan pada simpul induk A."
        }
    },
    {
        "id": "inf-lat-h-04",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Desain Alokasi Pengalamatan VLSM (Variable Length Subnet Masking)",
        "stem": "Sebuah perusahaan memiliki blok alamat IP dasar `10.50.0.0/22`. Administrator jaringan ditugaskan merancang subnetting menggunakan VLSM untuk memenuhi 3 kebutuhan departemen terbesar:\n1. Departemen A: Membutuhkan 450 alamat host valid\n2. Departemen B: Membutuhkan 200 alamat host valid\n3. Departemen C: Membutuhkan 100 alamat host valid\nJika pengalokasian subnet dilakukan secara berurutan dari kebutuhan host terbesar ke terkecil tanpa ada pemborosan bit, prefix subnet mask yang tepat dialokasikan untuk Departemen A, B, dan C berturut-turut adalah...",
        "correct": "Departemen A menggunakan `/23` (510 host valid), Departemen B menggunakan `/24` (254 host valid), dan Departemen C menggunakan `/25` (126 host valid).",
        "distractors": [
            "Departemen A menggunakan `/22` (1022 host valid), Departemen B menggunakan `/23` (510 host valid), dan Departemen C menggunakan `/24` (254 host valid).",
            "Departemen A menggunakan `/24` (254 host valid), Departemen B menggunakan `/25` (126 host valid), dan Departemen C menggunakan `/26` (62 host valid).",
            "Departemen A menggunakan `/25` (126 host valid), Departemen B menggunakan `/26` (62 host valid), dan Departemen C menggunakan `/27` (30 host valid).",
            "Seluruh departemen wajib menggunakan prefix seragam `/23` agar router tidak mengalami kegagalan protokol."
        ],
        "formula": {
            "title": "DESAIN HIERARKIS VLSM BERDASARKAN KEBUTUHAN HOST",
            "latex": "\\begin{aligned} \\text{Dep A (450 host):} & \\quad 2^h - 2 \\ge 450 \\implies h = 9 \\implies \\text{Prefix } 32 - 9 = \\mathbf{/23} \\ (510 \\text{ host}) \\\\ \\text{Dep B (200 host):} & \\quad 2^h - 2 \\ge 200 \\implies h = 8 \\implies \\text{Prefix } 32 - 8 = \\mathbf{/24} \\ (254 \\text{ host}) \\\\ \\text{Dep C (100 host):} & \\quad 2^h - 2 \\ge 100 \\implies h = 7 \\implies \\text{Prefix } 32 - 7 = \\mathbf{/25} \\ (126 \\text{ host}) \\end{aligned}",
            "legend": "• Total IP blok /22 = $2^{10} = 1024$ IP<br>• Alokasi: /23 memakan 512 IP, /24 memakan 256 IP, /25 memakan 128 IP. Total terpakai = 896 IP $\\le 1024$ IP (Efisien tanpa overlap)"
        },
        "hints": {
            "concept": "450 host butuh 2^9 - 2 = 510 host (/23). 200 host butuh 2^8 - 2 = 254 host (/24). 100 host butuh 2^7 - 2 = 126 host (/25).",
            "execution": "Pilih: Dep A (/23), Dep B (/24), Dep C (/25)."
        }
    },
    {
        "id": "inf-lat-h-05",
        "materi": "ANALISIS DATA",
        "topic": "Trade-off Teorema CAP pada Sistem Basis Data Terdistribusi",
        "stem": "Dalam sistem basis data terdistribusi berskala besar (Distributed Databases), Teorema CAP yang dirumuskan oleh Eric Brewer menyatakan bahwa sebuah sistem penyimpanan data terdistribusi hanya mampu menjamin secara maksimal DUA dari TIGA karakteristik berikut: Consistency, Availability, dan Partition Tolerance. Pada kondisi jaringan fisik mengalami pemutusan komunikasi antar kluster server (Network Partitioning terjadi), sistem bertipe CP (Consistency & Partition Tolerance) seperti MongoDB atau HBase akan memilih...",
        "correct": "Mengorbankan Availability (Ketersediaan); sistem menolak melayani permintaan tulis/baca baru (mengembalikan pesan error atau timeout) pada node yang terisolasi demi mencegah terjadinya inkonsistensi data antar replika server.",
        "distractors": [
            "Mengorbankan Consistency; sistem tetap menerima penulisan data baru di semua node meskipun data antar node menjadi tidak sinkron dan bertentangan.",
            "Menghapus seluruh salinan data di seluruh node server secara permanen untuk memulihkan koneksi jaringan fisik.",
            "Mengubah protokol jaringan secara otomatis menjadi model centralized client-server tanpa melalui proses partisi.",
            "Memaksa hardware sakelar jaringan fisik untuk tersambung kembali menggunakan sinyal kompresi perangkat lunak."
        ],
        "formula": {
            "title": "TEOREMA CAP DALAM SISTEM TERDISTRIBUSI",
            "latex": "\\text{Jaringan Terdistribusi Realistis Wajib Mendukung } \\mathbf{P} \\implies \\text{Pilihan Nyata: } \\mathbf{CP} \\lor \\mathbf{AP}",
            "legend": "• CP (Consistency + Partition Tolerance): Prioritas konsistensi data kuat, rela offline/reject jika partisi putus (misal transaksi perbankan)<br>• AP (Availability + Partition Tolerance): Sistem tetap online melayani klien, menerapkan model Eventual Consistency (misal timeline media sosial Cassandra/DynamoDB)"
        },
        "hints": {
            "concept": "Sistem CP saat terjadi partisi (P) akan memilih menjaga konsistensi (C) dan mengorbankan ketersediaan (A) dengan menolak request pada partisi yang terisolasi.",
            "execution": "Pilih: Mengorbankan Availability demi mencegah terjadinya inkonsistensi data."
        }
    },
    {
        "id": "inf-lat-h-06",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Penanganan Sisi Berbobot Negatif: Dijkstra vs Bellman-Ford",
        "stem": "Diberikan sebuah graf berarah dengan bobot sisi (directed weighted graph). Jika graf tersebut memuat beberapa sisi dengan bobot bernilai negatif, algoritma Dijkstra tidak dapat diandalkan dan berpotensi menghasilkan rute yang salah. Algoritma alternatif yang tepat digunakan untuk mencari lintasan terpendek dari satu titik sumber serta mampu mendeteksi keberadaan siklus berbobot negatif (negative weight cycle) adalah...",
        "correct": "Algoritma Bellman-Ford, yang melakukan relaksasi terhadap seluruh $|E|$ sisi graf sebanyak $|V| - 1$ kali dengan kompleksitas waktu $O(|V| \\cdot |E|)$, serta mampu mendeteksi siklus negatif pada relaksasi ke-$|V|$.",
        "distractors": [
            "Algoritma Floyd-Warshall, yang hanya dapat mengeksekusi graf tanpa sisi sama sekali dalam waktu linier $O(|V|)$.",
            "Algoritma Prim, yang khusus dirancang untuk mendeteksi siklus berbobot negatif pada pohon rentang minimum.",
            "Algoritma Breadth-First Search (BFS), yang secara otomatis mengabaikan bobot negatif dengan mengubahnya menjadi nilai nol.",
            "Algoritma A* Search, yang selalu menjamin rute terpendek tanpa memerlukan fungsi heuristik admissibel."
        ],
        "formula": {
            "title": "ALGORITMA BELLMAN-FORD DAN DETEKSI SIKLUS NEGATIF",
            "latex": "\\begin{aligned} \\text{Relaksasi (Iterasi } 1 \\text{ s.d. } |V|-1\\text{):} & \\quad \\text{if } dist[u] + w(u, v) < dist[v] : \\ dist[v] = dist[u] + w(u, v) \\\\ \\text{Deteksi Siklus (Iterasi ke-}|V|\\text{):} & \\quad \\text{if } dist[u] + w(u, v) < dist[v] \\implies \\text{Graf memiliki Negative Cycle!} \\end{aligned}",
            "legend": "• Kelemahan Dijkstra: Greedy approach mengasumsikan jarak yang sudah difinalisasi tidak akan pernah bisa diperpendek lagi (gagal pada bobot negatif)<br>• Keunggulan Bellman-Ford: Mampu menangani bobot negatif dan mendeteksi siklus pengurang nilai tanpa batas"
        },
        "hints": {
            "concept": "Algoritma untuk single-source shortest path dengan bobot negatif dan deteksi negative weight cycle adalah Bellman-Ford.",
            "execution": "Pilih: Algoritma Bellman-Ford dengan relaksasi (|V|-1) kali dan kompleksitas O(|V| . |E|)."
        }
    },
    {
        "id": "inf-lat-h-07",
        "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
        "topic": "Protokol Pertukaran Kunci Diffie-Hellman dan Logaritma Diskrit",
        "stem": "Protokol pertukaran kunci Diffie-Hellman memungkinkan dua pihak (Alice dan Bob) yang berkomunikasi melalui saluran publik yang tidak aman untuk menyepakati sebuah kunci rahasia bersama (shared secret key) tanpa pernah mengirimkan kunci rahasia tersebut. Keamanan matematis dari protokol Diffie-Hellman bertumpu pada...",
        "correct": "Tingginya kesulitan komputasi Masalah Logaritma Diskrit (Discrete Logarithm Problem) pada grup perkalian medan terhingga modulo bilangan prima besar ($g^a \\pmod p$), di mana menghitung hasil perpangkatan modular sangat mudah, tetapi mencari eksponen $a$ dari nilai publik adalah persoalan yang secara komputasi mustahil diselesaikan dalam waktu wajar.",
        "distractors": [
            "Kecepatan transmisi foton kuantum melalui kabel serat optik bawah laut yang tidak dapat dicegat oleh peretas.",
            "Penggunaan kunci simetris rahasia yang telah dipasang secara permanen di pabrik sirkuit prosesor komputer sejak awal.",
            "Kemustahilan matematis melakukan operasi modulus sisa bagi pada bilangan ganjil yang memiliki lebih dari 10 digit.",
            "Proses enkripsi satu kali pakai (One-Time Pad) yang secara fisik menghancurkan sinyal data setelah dibaca oleh penerima."
        ],
        "formula": {
            "title": "MATEMATIKA PROTOKOL DIFFIE-HELLMAN KEY EXCHANGE",
            "latex": "\\begin{aligned} \\text{Parameter Publik:} & \\quad p \\text{ (Prima Besar)}, \\ g \\text{ (Generator / Primitive Root)} \\\\ \\text{Kunci Privat:} & \\quad a \\text{ (Alice)}, \\ b \\text{ (Bob)} \\\\ \\text{Kunci Publik:} & \\quad A = g^a \\pmod p, \\quad B = g^b \\pmod p \\\\ \\text{Kunci Rahasia Bersama:} & \\quad K = B^a \\pmod p = (g^b)^a = g^{ab} = (g^a)^b = A^b \\pmod p \\end{aligned}",
            "legend": "• Keamanan: Penyerang pasif hanya melihat $p, g, A, B$. Untuk mencari $K$, penyerang harus memecahkan $a$ dari $A = g^a \\pmod p$ (Discrete Logarithm Problem yang teramat sulit)"
        },
        "hints": {
            "concept": "Landasan keamanan Diffie-Hellman adalah kesulitan komputasi Masalah Logaritma Diskrit (Discrete Logarithm Problem) modulo bilangan prima besar.",
            "execution": "Pilih opsi: Kesulitan komputasi Masalah Logaritma Diskrit pada grup modulo prima besar."
        }
    },
    {
        "id": "inf-lat-h-08",
        "materi": "SISTEM KOMPUTER",
        "topic": "Pencegahan Kebuntuan Sistem (Deadlock) dan Algoritma Banker",
        "stem": "Dalam sistem operasi multiprogramming, kebuntuan sistem (deadlock) terjadi ketika sekumpulan proses saling menunggu sumber daya yang sedang ditahan oleh proses lain dalam himpunan tersebut secara melingkar. Untuk menghindari terjadinya deadlock, sistem operasi dapat menerapkan Algoritma Banker (Dijkstra's Banker Algorithm). Prinsip kerja fundamental dari Algoritma Banker adalah...",
        "correct": "Menguji setiap permintaan alokasi sumber daya dengan menyimulasikan keadaan alokasi masa depan; permintaan hanya akan dipenuhi jika hasil simulasi menjamin sistem tetap berada dalam Keadaan Aman (Safe State) di mana terdapat urutan eksekusi (safe sequence) yang memungkinkan seluruh proses menyelesaikan tugasnya.",
        "distractors": [
            "Mematikan (kill) secara paksa seluruh proses aktif yang meminta lebih dari satu sumber daya secara acak.",
            "Mengabaikan pengecekan sumber daya dan langsung mengalokasikan memori hingga kapasitas RAM fisik habis total.",
            "Memaksa setiap proses untuk berjalan dalam satu utas (single thread) tunggal secara bergiliran menggunakan timer FCFS.",
            "Mengenkripsi tabel sumber daya sistem sehingga proses yang bersaing tidak dapat saling melihat status alokasi."
        ],
        "formula": {
            "title": "EMPAT KONDISI KEBUTUHAN DEADLOCK (COFFMAN CONDITIONS)",
            "latex": "\\text{Deadlock} \\iff \\text{Mutual Exclusion} \\land \\text{Hold and Wait} \\land \\text{No Preemption} \\land \\text{Circular Wait}",
            "legend": "• Safe State: Status sistem di mana ada setidaknya satu Safe Sequence $\\langle P_1, P_2, \\dots, P_n \\rangle$ alokasi sumber daya yang tidak berujung kebuntuan<br>• Matriks Algoritma Banker: Allocation, Max, Available, Need = Max - Allocation"
        },
        "hints": {
            "concept": "Algoritma Banker menguji simulasi alokasi dan hanya mengabulkan permintaan jika sistem tetap berada dalam Status Aman (Safe State).",
            "execution": "Pilih: Menguji alokasi dan hanya memenuhinya jika sistem tetap berada dalam Keadaan Aman (Safe State)."
        }
    },
    {
        "id": "inf-lat-h-09",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Pohon Rentang Minimum (MST) Kruskal dan Disjoint Set Union (DSU)",
        "stem": "Algoritma Kruskal digunakan untuk menemukan Pohon Rentang Minimum (Minimum Spanning Tree / MST) pada graf terhubung berbobot dengan cara mengurutkan seluruh sisi berdasarkan bobotnya dari yang terkecil, lalu memilih sisi satu per satu selama tidak membentuk siklus. Struktur data yang paling efisien digunakan untuk mendeteksi dan mencegah terbentuknya siklus secara instan dalam algoritma Kruskal adalah...",
        "correct": "Disjoint Set Union (DSU / Union-Find) yang dilengkapi teknik Path Compression dan Union by Rank/Size, dengan kompleksitas waktu mendekati linier $O(|E| \\log |E| + |E| \\cdot \\alpha(|V|))$.",
        "distractors": [
            "Matriks Ketetanggaan (Adjacency Matrix) dengan penelusuran DFS berulang-ulang yang memiliki kompleksitas waktu $O(|E| \\cdot |V|^2)$.",
            "Tumpukan Ganda (Double Stack) yang membalikkan urutan pembacaan bobot sisi setiap kali percabangan terdeteksi.",
            "Tabel Hash linier tanpa penanganan tabrakan yang langsung menghapus sisi berbobot ganjil.",
            "Pohon Biner Terurut (Binary Search Tree) yang menyimpan alamat memori fisik kartu jaringan router."
        ],
        "formula": {
            "title": "KOMPLEKSITAS ALGORITMA KRUSKAL DENGAN DSU",
            "latex": "T(V, E) = O(|E| \\log |E|) + O(|E| \\cdot \\alpha(|V|)) \\approx O(|E| \\log |V|)",
            "legend": "• $\\alpha(n)$: Fungsi Inverse Ackermann (tumbuh sangat lambat, $\\alpha(n) \\le 4$ untuk seluruh nilai praktis di alam semesta)<br>• Find(u) == Find(v): Menandakan bahwa kedua simpul sudah berada di komponen yang sama (menambahkan sisi ini akan membentuk siklus!)<br>• Union(u, v): Menggabungkan dua komponen pohon menjadi satu"
        },
        "hints": {
            "concept": "Struktur data standar deteksi siklus pada Kruskal adalah Disjoint Set Union (DSU / Union-Find) dengan Path Compression.",
            "execution": "Pilih: Disjoint Set Union (DSU / Union-Find) dengan Path Compression dan Union by Rank."
        }
    },
    {
        "id": "inf-lat-h-10",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Pencocokan String Cepat Algoritma Knuth-Morris-Pratt (KMP)",
        "stem": "Dalam pencarian pola teks (string matching) di mana pola $P$ berukuran $m$ dicari di dalam teks $T$ berukuran $n$, algoritma pencarian naif membutuhkan waktu terburuk $O(n \\cdot m)$ karena memundurkan penunjuk teks kembali ke awal saat terjadi ketidakcocokan karakter. Algoritma Knuth-Morris-Pratt (KMP) mampu mencapai kompleksitas linier optimal $O(n + m)$ dengan memanfaatkan...",
        "correct": "Tabel Prefix $\\pi$ / LPS (Longest Proper Prefix which is also Suffix), yang menentukan seberapa jauh penunjuk karakter pola dapat digeser ke depan tanpa perlu memeriksa ulang karakter teks yang sudah terbukti cocok sebelumnya.",
        "distractors": [
            "Matriks substitusi probabilitas Markov yang menebak karakter teks berikutnya secara acak.",
            "Fungsi kompresi Huffman yang mengubah seluruh teks dan pola menjadi deretan bit biner tetap sebelum dicari.",
            "Struktur data Trie raksasa yang menduplikasi teks sebanyak $n$ kali di dalam memori cache sekunder.",
            "Proses pengurutan alfabetik terhadap teks menggunakan algoritma Quicksort tiga dimensi."
        ],
        "formula": {
            "title": "TABEL LPS (LONGEST PROPER PREFIX SUFFIX) ALGORITMA KMP",
            "latex": "\\text{Kompleksitas Preprocessing Pola: } O(m) + \\text{Kompleksitas Pencarian Teks: } O(n) \\implies T_{\\text{total}} = O(n + m)",
            "legend": "• LPS[i]: Panjang prefiks terpanjang dari $P[0..i]$ yang juga merupakan sufiks dari $P[0..i]$<br>• Manfaat KMP: Penunjuk indeks pada teks utama $T$ tidak pernah bergerak mundur (no backtracking on text), sangat ideal untuk pemrosesan aliran data (data stream)"
        },
        "hints": {
            "concept": "KMP memanfaatkan tabel LPS (Longest Proper Prefix which is also Suffix) untuk menggeser pola tanpa memundurkan pointer teks.",
            "execution": "Pilih opsi: Tabel Prefix / LPS (Longest Proper Prefix which is also Suffix)."
        }
    },
    {
        "id": "inf-lat-h-11",
        "materi": "TEKNOLOGI INFORMASI DAN KOMUNIKASI",
        "topic": "Arsitektur Komunikasi API Modern: RESTful vs GraphQL",
        "stem": "Dalam arsitektur pengembangan web dan aplikasi seluler modern, GraphQL dirancang untuk mengatasi beberapa limitasi arsitektur RESTful konvensional. Masalah utama pada arsitektur REST di mana klien menerima terlalu banyak data atribut yang tidak dibutuhkan (misalnya meminta data profil tetapi server mengirim seluruh histori posting dan relasi teman) serta solusinya pada GraphQL adalah...",
        "correct": "Masalah Over-fetching; diselesaikan oleh GraphQL melalui kueri deklaratif di mana klien secara spesifik mendefinisikan atribut persis apa saja yang dibutuhkannya dalam payload permintaan, sehingga server hanya mengirimkan atribut yang diminta.",
        "distractors": [
            "Masalah Under-fetching; diselesaikan oleh GraphQL dengan melarang klien mengirimkan parameter kueri ke server.",
            "Masalah Connection Timeout; diselesaikan oleh GraphQL dengan mematikan fungsi enkripsi HTTPS pada jaringan seluler.",
            "Masalah SQL Injection; diselesaikan oleh GraphQL dengan mengubah seluruh basis data relasional menjadi dokumen XML statis.",
            "Masalah N+1 Query; diselesaikan oleh GraphQL dengan secara otomatis menambah jumlah tabel basis data hingga ribuan."
        ],
        "formula": {
            "title": "KOMPARASI EFISIENSI PAYLOAD REST VS GRAPHQL",
            "latex": "\\begin{aligned} \\text{REST Over-fetching:} & \\quad \\text{GET /user/1} \\implies \\{\\text{id, nama, alamat, nik, no\\_hp, riwayat\\_medis, saldo, ... (50 KB)}\\} \\\\ \\text{GraphQL Declarative:} & \\quad \\text{query } \\{\\text{user(id: 1) } \\{\\text{nama}\\}\\} \\implies \\{\\text{data: } \\{\\text{\"nama\": \"Budi\"}\\} \\ (100 \\text{ Bytes})\\} \\end{aligned}",
            "legend": "• Over-fetching: Menerima data berlebih dari endpoint REST tetap<br>• Under-fetching: Satu endpoint REST tidak cukup, butuh multiple network round-trips<br>• GraphQL: Single endpoint (/graphql), kueri fleksibel sesuai kebutuhan klien"
        },
        "hints": {
            "concept": "Menerima data berlebih yang tidak dibutuhkan disebut Over-fetching. Di GraphQL diselesaikan karena klien dapat meminta persis field yang diinginkan.",
            "execution": "Pilih: Masalah Over-fetching; diselesaikan melalui kueri deklaratif spesifik kebutuhan klien."
        }
    },
    {
        "id": "inf-lat-h-12",
        "materi": "ANALISIS DATA",
        "topic": "Normalisasi Basis Data Lanjut: 3NF vs Boyce-Codd Normal Form (BCNF)",
        "stem": "Sebuah tabel relasional sudah memenuhi Bentuk Normal Ketiga (3NF), namun masih memiliki anomali pembaruan (update anomaly). Kondisi spesifik di mana sebuah tabel yang telah memenuhi 3NF dinyatakan BELUM memenuhi Bentuk Normal Boyce-Codd (BCNF) adalah...",
        "correct": "Jika pada ketergantungan fungsional non-trivial $X \\to Y$ yang berlaku pada tabel, determinan $X$ BUKAN merupakan Superkey (sering terjadi pada tabel yang memiliki beberapa overlap candidate keys komposit).",
        "distractors": [
            "Jika tabel tersebut memiliki atribut yang nilainya berupa bilangan pecahan desimal yang belum dibulatkan.",
            "Jika tabel memiliki ketergantungan parsial di mana kunci primer terdiri dari satu kolom tunggal.",
            "Jika tabel tidak memiliki indeks clustered B-Tree pada media penyimpanan sekunder fisik.",
            "Jika jumlah baris rekaman pada tabel melebihi batas 1.000 data entri per partisi disk."
        ],
        "formula": {
            "title": "DEFINISI BENTUK NORMAL BOYCE-CODD (BCNF)",
            "latex": "R \\in \\text{BCNF} \\iff \\forall X \\to Y \\text{ (Non-trivial FD)} : \\quad X \\text{ adalah Superkey}",
            "legend": "• Perbedaan 3NF dan BCNF: Pada 3NF, jika $X$ bukan superkey, kondisi masih sah jika $Y$ adalah Prime Attribute (bagian dari candidate key). Pada BCNF, relaksasi ini dihapus secara mutlak ($X$ wajib superkey)<br>• BCNF adalah bentuk normal yang lebih ketat daripada 3NF"
        },
        "hints": {
            "concept": "Aturan BCNF mensyaratkan untuk setiap ketergantungan fungsional X -> Y, penentu (X) wajib merupakan Superkey.",
            "execution": "Pilih opsi: Jika determinan X bukan merupakan Superkey pada ketergantungan fungsional non-trivial X -> Y."
        }
    },
    {
        "id": "inf-lat-h-13",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Protokol Routing Dinamis: Link-State (OSPF) vs Distance-Vector (RIP)",
        "stem": "Protokol perutean dinamis interior (IGP) dikelompokkan menjadi algoritma Distance-Vector (seperti RIP) dan Link-State (seperti OSPF). Keunggulan arsitektural utama protokol Link-State seperti OSPF dalam jaringan enterprise berskala besar adalah...",
        "correct": "Setiap router memiliki peta topologi jaringan global yang lengkap dan identik melalui pertukaran Link-State Advertisements (LSA) dan menghitung rute bebas loop tercepat menggunakan Algoritma Dijkstra, sehingga konvergensi jaringan tercapai sangat cepat tanpa masalah Count-to-Infinity.",
        "distractors": [
            "OSPF hanya mengandalkan informasi jarak lompatan (hop count) dari tetangga langsungnya dan dibatasi maksimal 15 hop.",
            "OSPF menyiarkan seluruh tabel routingnya secara berkala setiap 30 detik ke seluruh jaringan menggunakan paket broadcast.",
            "OSPF tidak memerlukan daya pemrosesan CPU dan memori sama sekali pada perangkat keras router.",
            "OSPF secara otomatis mengenkripsi kabel tembaga fisik menggunakan protokol token ring nirkabel."
        ],
        "formula": {
            "title": "KOMPARASI PROTOKOL ROUTING INTERIOR (IGP)",
            "latex": "\\begin{aligned} \\text{RIP (Distance-Vector):} & \\quad \\text{Metrik: Hop Count (Maks 15)}, \\ \\text{Algoritma: Bellman-Ford}, \\ \\text{Konvergensi Lambat (Looping)} \\\\ \\text{OSPF (Link-State):} & \\quad \\text{Metrik: Cost (Bandwidth)}, \\ \\text{Algoritma: Dijkstra (SPF)}, \\ \\text{Konvergensi Cepat, Area Hierarki} \\end{aligned}",
            "legend": "• LSDB (Link-State Database): Basis data topologi lengkap yang disinkronkan antar router dalam satu area OSPF<br>• SPF Tree: Pohon jalur terpendek dihitung dengan router itu sendiri sebagai akar"
        },
        "hints": {
            "concept": "OSPF adalah link-state: router memiliki peta topologi utuh via LSA dan menghitung lintasan terpendek bebas loop dengan algoritma Dijkstra (konvergensi cepat).",
            "execution": "Pilih: Memiliki peta topologi global lengkap, menggunakan Dijkstra, dan konvergensi cepat tanpa loop."
        }
    },
    {
        "id": "inf-lat-h-14",
        "materi": "SISTEM KOMPUTER",
        "topic": "Protokol Koherensi Cache MESI pada Sistem Multiprocessor",
        "stem": "Pada prosesor modern multi-core, setiap inti CPU memiliki cache memori L1/L2 privat masing-masing yang dapat menyimpan salinan variabel data yang sama dari RAM utama. Untuk mencegah terjadinya inkonsistensi data ketika salah satu inti menulis nilai baru ke variabel tersebut, sistem menerapkan protokol koherensi cache MESI. Empat status valid dalam protokol MESI yang merepresentasikan kondisi baris cache tersebut adalah...",
        "correct": "Modified (data kotor diubah lokal, berbeda dengan RAM), Exclusive (data bersih hanya ada di cache lokal), Shared (data bersih ada di beberapa cache inti), dan Invalid (data sudah usang tidak valid akibat modifikasi inti lain).",
        "distractors": [
            "Master (pengendali bus), Execution (sedang dihitung), Suspended (ditunda sementara), dan Idle (tidak aktif).",
            "Monitored (dipantau), Encrypted (terenkripsi), Stored (tersimpan permanen), dan Indexed (terindeks).",
            "Memory (di RAM), External (di SSD), Static (konstan), dan Interrupted (terputus sinyal).",
            "Main (utama), Ephemeral (sementara), Swapped (ditukar ke disk), dan Isolated (terisolasi)."
        ],
        "formula": {
            "title": "PROTOKOL KOHERENSI CACHE MESI (ILLINOIS PROTOCOL)",
            "latex": "\\text{State MESI} \\equiv \\begin{cases} \\mathbf{M} \\text{ (Modified):} & \\text{Dirty line, eksklusif, RAM belum diperbarui} \\\\ \\mathbf{E} \\text{ (Exclusive):} & \\text{Clean line, hanya ada di cache ini, sama dengan RAM} \\\\ \\mathbf{S} \\text{ (Shared):} & \\text{Clean line, mungkin ada di cache inti lain, sama dengan RAM} \\\\ \\mathbf{I} \\text{ (Invalid):} & \\text{Data usang/tidak valid, wajib reload dari memori jika diakses} \\end{cases}",
            "legend": "• Bus Snooping: Setiap inti cache memantau lalu lintas bus memori<br>• Transisi Write: Inti yang ingin menulis ke status S menyiarkan sinyal invalidate ke inti lain, mengubah status barisnya menjadi M dan inti lain menjadi I"
        },
        "hints": {
            "concept": "MESI singkatan dari: Modified, Exclusive, Shared, Invalid.",
            "execution": "Pilih opsi: Modified, Exclusive, Shared, dan Invalid."
        }
    },
    {
        "id": "inf-lat-h-15",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Struktur Data Pohon Segmen (Segment Tree) untuk Range Query",
        "stem": "Sebuah aplikasi sistem informasi geografis memerlukan kalkulasi berkala nilai minimum pada rentang indeks $[L, R]$ (Range Minimum Query / RMQ) serta pembaruan nilai elemen tunggal pada indeks $k$ (Point Update) secara bergantian pada larik berisi $n = 100.000$ data. Jika digunakan struktur data Segment Tree, kompleksitas waktu asimtotik untuk operasi Range Query dan Point Update secara berturut-turut adalah...",
        "correct": "$O(\\log_2 n)$ untuk Range Minimum Query dan $O(\\log_2 n)$ untuk Point Update, dengan waktu pembangunan pohon awal sebesar $O(n)$.",
        "distractors": [
            "$O(1)$ untuk Range Minimum Query dan $O(n)$ untuk Point Update, dengan waktu pembangunan awal $O(n^2)$.",
            "$O(n)$ untuk Range Minimum Query dan $O(1)$ untuk Point Update, seperti halnya larik statis sederhana.",
            "$O(n \\log_2 n)$ untuk Range Minimum Query dan $O(n \\log_2 n)$ untuk Point Update.",
            "$O(1)$ untuk Range Minimum Query dan $O(1)$ untuk Point Update konstan instan."
        ],
        "formula": {
            "title": "KOMPLEKSITAS OPERASI STRUKTUR DATA SEGMENT TREE",
            "latex": "\\begin{aligned} \\text{Build Tree:} & \\quad O(n) \\\\ \\text{Point Update (Perbarui 1 Elemen):} & \\quad O(\\log n) \\\\ \\text{Range Query (Hitung Nilai Segmen } [L, R]\\text{):} & \\quad O(\\log n) \\\\ \\text{Ruang Memori (Ukuran Larik Simpul):} & \\quad \\le 4n \\end{aligned}",
            "legend": "• Keunggulan Segment Tree: Menggabungkan efisiensi query dan update dinamis pada $O(\\log n)$<br>• Pohon Biner Sempurna: Setiap simpul internal menyimpan hasil agregasi (min, sum, gcd) dari kedua anak segmennya"
        },
        "hints": {
            "concept": "Segment Tree melakukan query rentang dan update titik pada tinggi pohon log(n), jadi keduanya berkecepatan O(log n).",
            "execution": "Pilih: O(log n) untuk Range Minimum Query dan O(log n) untuk Point Update."
        }
    },
    {
        "id": "inf-lat-h-16",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Paradigma Keamanan Arsitektur Zero Trust (Never Trust, Always Verify)",
        "stem": "Model keamanan jaringan tradisional berbasis perimeter (Castle-and-Moat) mengasumsikan bahwa seluruh entitas di dalam jaringan lokal (intranet) adalah tepercaya. Kelemahan fatal model ini terbukti saat penyerang berhasil membobol satu perangkat internal dan leluasa melakukan pergerakan lateral (lateral movement). Paradigma modern Zero Trust Architecture (ZTA) mengatasi kerentanan ini dengan menerapkan prinsip inti...",
        "correct": "\"Never Trust, Always Verify\"; tidak ada pengguna, perangkat, atau beban kerja yang dipercaya secara bawaan meskipun berada di dalam jaringan internal, sehingga setiap permintaan akses wajib diotentikasi, diotorisasi, dan dienkripsi secara ketat berdasarkan konteks hak akses terkecil (Least Privilege).",
        "distractors": [
            "Mematikan seluruh sistem pertahanan firewall dan membiarkan jaringan terbuka bebas demi transparansi data publik.",
            "Memberikan hak akses Administrator (Root) penuh kepada seluruh karyawan agar operasional kantor tidak terhambat.",
            "Hanya mempercayai perangkat komputer yang dibeli secara langsung dari pabrik tanpa memerlukan kata sandi masuk.",
            "Menghapus seluruh berkas enkripsi sertifikat SSL agar lalu lintas data dapat dipantau oleh siapa saja."
        ],
        "formula": {
            "title": "TIGA PRINSIP UTAMA ARSITEKTUR ZERO TRUST (NIST SP 800-207)",
            "latex": "\\text{Zero Trust} \\equiv \\text{Verify Explicitly} \\cap \\text{Use Least Privilege Access} \\cap \\text{Assume Breach}",
            "legend": "• Verify Explicitly: Otentikasi dan otorisasi selalu berdasarkan identitas, lokasi, kesehatan perangkat, dan anomali data<br>• Least Privilege: Batasi akses pengguna hanya pada sumber daya yang benar-benar esensial (JIT & JEA)<br>• Assume Breach: Minimalkan radius ledakan (blast radius) melalui mikrosegmentasi jaringan"
        },
        "hints": {
            "concept": "Prinsip inti Zero Trust: \"Never Trust, Always Verify\" dan menerapkan hak akses terendah (Least Privilege).",
            "execution": "Pilih opsi yang mencantumkan \"Never Trust, Always Verify\" dan prinsip hak akses terkecil (Least Privilege)."
        }
    },
    {
        "id": "inf-lat-h-17",
        "materi": "BERPIKIR KOMPUTASIONAL",
        "topic": "Pengurutan Topologis (Topological Sort) Menggunakan Algoritma Kahn",
        "stem": "Dalam manajemen penjadwalan kompilasi dependensi paket perangkat lunak yang dimodelkan sebagai Directed Acyclic Graph (DAG), pengurutan linier simpul di mana setiap sisi terarah $(u, v)$ menuntut $u$ dieksekusi sebelum $v$ disebut Topological Sort. Algoritma Kahn mengimplementasikan pengurutan topologis dengan menggunakan konsep derajat masuk (In-Degree). Langkah inisialisasi yang tepat pada algoritma Kahn adalah...",
        "correct": "Menghitung In-Degree setiap simpul, memasukkan seluruh simpul yang memiliki In-Degree sama dengan 0 ke dalam antrean (Queue), lalu secara berulang mengeluarkan simpul dari antrean dan mengurangi In-Degree simpul-simpul tetangganya.",
        "distractors": [
            "Memasukkan simpul yang memiliki In-Degree tertinggi ke dalam tumpukan (Stack) lalu menghapus seluruh sisi masuk.",
            "Mengurutkan simpul secara alfabetis berdasarkan label nama teks menggunakan algoritma Quicksort rekursif.",
            "Mencari jalur lintasan terpendek menggunakan algoritma Dijkstra dimulai dari simpul berbobot sisi negatif.",
            "Membalikkan arah panah seluruh sisi pada graf dan mencari pohon rentang minimum menggunakan algoritma Prim."
        ],
        "formula": {
            "title": "ALUR KERJA ALGORITMA KAHN (TOPOLOGICAL SORT)",
            "latex": "\\begin{aligned} 1. & \\quad \\text{Hitung } \\text{in\\_degree}[v] \\ \\forall v \\in V \\\\ 2. & \\quad Q = \\{v \\mid \\text{in\\_degree}[v] == 0\\} \\\\ 3. & \\quad \\text{while } Q \\ne \\emptyset : \\ u = Q.\\text{pop}() \\to \\text{Hasil.append}(u) \\to \\forall (u, v) : \\text{in\\_degree}[v]-- \\ (\\text{if } 0 \\implies Q.\\text{push}(v)) \\end{aligned}",
            "legend": "• Syarat Graf: Wajib berupa DAG (Directed Acyclic Graph). Jika di akhir hasil pengurutan jumlah simpul < $|V|$, maka graf memuat siklus (terjadi deadlock dependensi)<br>• Kompleksitas Waktu: $O(V + E)$ linier"
        },
        "hints": {
            "concept": "Algoritma Kahn memasukkan simpul dengan in-degree = 0 ke Queue, mencatatnya, lalu mengurangi in-degree tetangganya.",
            "execution": "Pilih: Menghitung in-degree, memasukkan simpul in-degree = 0 ke Queue, dan mengurangi in-degree tetangganya."
        }
    },
    {
        "id": "inf-lat-h-18",
        "materi": "ANALISIS DATA",
        "topic": "Pemberian Peringkat dengan Window Function SQL: RANK() vs DENSE_RANK()",
        "stem": "Diberikan tabel `Nilai_Siswa` dengan nilai skor matematika: `[100, 95, 95, 90, 85]`. Seorang analis mengeksekusi kueri SQL menggunakan fungsi analitis jendela (Window Function):\n```sql\nSELECT nama, nilai,\n       RANK() OVER (ORDER BY nilai DESC) as rnk,\n       DENSE_RANK() OVER (ORDER BY nilai DESC) as drnk\nFROM Nilai_Siswa;\n```\nNilai peringkat `rnk` dan `drnk` yang akan diperoleh oleh siswa yang mendapatkan nilai `90` secara berturut-turut adalah...",
        "correct": "`rnk = 4` dan `drnk = 3`, karena `RANK()` melompati nomor urutan berikutnya setelah ada nilai kembar seri (1, 2, 2, 4), sedangkan `DENSE_RANK()` tidak pernah melompati nomor peringkat (1, 2, 2, 3).",
        "distractors": [
            "`rnk = 3` dan `drnk = 4`, karena fungsi RANK() selalu memprioritaskan nomor urut yang lebih padat.",
            "`rnk = 3` dan `drnk = 3`, karena kedua fungsi menghasilkan urutan peringkat yang identik pada semua kasus.",
            "`rnk = 4` dan `drnk = 4`, karena nomor peringkat siswa selalu disesuaikan dengan posisi indeks baris tabel.",
            "`rnk = 2` dan `drnk = 2`, karena nilai kembar dianggap sebagai satu kesatuan data tunggal tanpa pembagian."
        ],
        "formula": {
            "title": "KOMPARASI WINDOW FUNCTION PERINGKAT SQL",
            "latex": "\\begin{array}{|c|c|c|c|} \\hline \\text{Nilai} & \\text{ROW\\_NUMBER()} & \\text{RANK()} & \\text{DENSE\\_RANK()} \\\\ \\hline 100 & 1 & 1 & 1 \\\\ 95 & 2 & 2 & 2 \\\\ 95 & 3 & 2 & 2 \\\\ \\mathbf{90} & 4 & \\mathbf{4} & \\mathbf{3} \\\\ 85 & 5 & 5 & 4 \\\\ \\hline \\end{array}",
            "legend": "• ROW_NUMBER(): Menghasilkan nomor urut baris unik berkelanjutan tanpa peduli nilai kembar<br>• RANK(): Memberikan peringkat sama pada nilai kembar, lalu MELOMPATI nomor urut berikutnya ($1, 2, 2, 4$)<br>• DENSE_RANK(): Memberikan peringkat sama pada nilai kembar TANPA melompati nomor ($1, 2, 2, 3$)"
        },
        "hints": {
            "concept": "Nilai 100 (rank 1, dense 1). Nilai 95 & 95 (rank 2 & 2, dense 2 & 2). Nilai 90 berikutnya mendapat rank 4 (karena lewati 3) dan dense_rank 3.",
            "execution": "Pilih: rnk = 4 dan drnk = 3."
        }
    },
    {
        "id": "inf-lat-h-19",
        "materi": "JARINGAN KOMPUTER & INTERNET",
        "topic": "Algoritma Kontrol Kemacetan TCP: Slow Start dan AIMD",
        "stem": "Protokol TCP mengimplementasikan mekanisme pengendalian kemacetan (Congestion Control) untuk mencegah jaringan internet mengalami kelebihan beban paket data. Pada fase Slow Start, ukuran jendela kemacetan (Congestion Window / `cwnd`) digandakan secara eksponensial setiap siklus RTT hingga mencapai ambang batas `ssthresh`. Ketika `cwnd` telah melampaui `ssthresh`, fase kontrol TCP yang aktif selanjutnya serta pola penambahan ukurannya adalah...",
        "correct": "Fase Penghindaran Kemacetan (Congestion Avoidance), di mana `cwnd` ditingkatkan secara linier sebesar 1 MSS (Maximum Segment Size) setiap RTT (prinsip Additive Increase).",
        "distractors": [
            "Fase Fast Retransmit, di mana `cwnd` langsung diturunkan menjadi 0 byte untuk menghentikan transmisi paket.",
            "Fase Exponential Burst, di mana `cwnd` dinaikkan menjadi kuadrat dari nilai sebelumnya setiap milidetik.",
            "Fase Multiplicative Decrease, di mana jendela kemacetan diperbesar sepuluh kali lipat untuk memaksa router bekerja.",
            "Fase Static Allocation, di mana ukuran jendela dikunci secara permanen dan tidak dapat diubah kembali."
        ],
        "formula": {
            "title": "MEKANISME PENGENDALIAN KEMACETAN TCP (AIMD)",
            "latex": "\\begin{aligned} \\text{Slow Start (}\\text{cwnd} < \\text{ssthresh}\\text{):} & \\quad \\text{cwnd} = \\text{cwnd} \\times 2 \\ \\text{per RTT (Eksponensial)} \\\\ \\text{Congestion Avoidance (}\\text{cwnd} \\ge \\text{ssthresh}\\text{):} & \\quad \\text{cwnd} = \\text{cwnd} + 1 \\text{ MSS per RTT (Linier / Additive Increase)} \\\\ \\text{Deteksi Paket Hilang (Timeout):} & \\quad \\text{ssthresh} = \\frac{\\text{cwnd}}{2}, \\quad \\text{cwnd} = 1 \\text{ MSS (Multiplicative Decrease)} \\end{aligned}",
            "legend": "• AIMD: Additive Increase, Multiplicative Decrease menjamin kestabilan dan keadilan (fairness) pembagian bandwidth internet antar koneksi"
        },
        "hints": {
            "concept": "Setelah Slow Start melewati ssthresh, TCP masuk fase Congestion Avoidance yang menaikkan cwnd secara linier (+1 MSS per RTT).",
            "execution": "Pilih: Congestion Avoidance, dengan peningkatan linier sebesar 1 MSS per RTT (Additive Increase)."
        }
    },
    {
        "id": "inf-lat-h-20",
        "materi": "ALGORITMA & PEMROGRAMAN",
        "topic": "Strategi Penelusuran Balik (Backtracking) dan Pemangkasan Cabang (Pruning)",
        "stem": "Dalam memecahkan masalah penempatan $N$ Ratu pada papan catur ukuran $N \\times N$ (N-Queens Problem) sedemikian rupa sehingga tidak ada dua ratu yang saling menyerang, pendekatan brute-force mencoba seluruh $\\binom{N^2}{N}$ kombinasi yang membutuhkan waktu teramat lambat. Pendekatan Backtracking menyelesaikan masalah ini jauh lebih efisien karena menerapkan teknik pemangkasan cabang (pruning). Mekanisme pruning pada algoritma ini bekerja dengan cara...",
        "correct": "Menghentikan eksplorasi cabang pohon pencarian seketika saat penempatan ratu baru terbukti melanggar kendali keselamatan (berada di baris, kolom, atau diagonal yang sama dengan ratu sebelumnya), lalu mundur (backtrack) ke langkah sebelumnya tanpa menjelajahi sub-cabang di bawahnya.",
        "distractors": [
            "Menghapus seluruh baris papan catur yang tidak memuat bidak ratu pada awal eksekusi program.",
            "Mengubah representasi papan catur menjadi graf tak berarah dan mencari siklus Euler menggunakan matriks.",
            "Mengabaikan aturan pergerakan diagonal ratu dan hanya memeriksa benturan pada baris horizontal saja.",
            "Membalikkan nilai koordinat ratu menggunakan operasi bitwise XOR pada memori register mikroprosesor."
        ],
        "formula": {
            "title": "PRINSIP PEMANGKASAN CABANG (PRUNING) ALGORITMA BACKTRACKING",
            "latex": "\\text{Ruang Status Brute-Force: } O(N^N) \\xrightarrow{\\text{Pruning State Valid}} \\text{Pencarian Efisien Terfokus}",
            "legend": "• Vektor Solusi: $Q[i] = c$, menyatakan ratu pada baris $i$ ditempatkan di kolom $c$<br>• Syarat Konflik: $Q[i] == Q[k]$ (Kolom Sama) atau $|Q[i] - Q[k]| == |i - k|$ (Diagonal Sama)<br>• Jika konflik terdeteksi pada baris $i$, sub-pohon baris $i+1 \\dots N$ langsung dipangkas (pruned)"
        },
        "hints": {
            "concept": "Pruning pada Backtracking menghentikan eksplorasi cabang sesaat setelah kondisi tidak valid terdeteksi, lalu kembali (backtrack) ke langkah sebelumnya.",
            "execution": "Pilih opsi: Menghentikan eksplorasi cabang saat penempatan melanggar aturan dan langsung mundur (backtrack)."
        }
    },
    {
        "id": "inf-lat-h-21",
        "materi": "SISTEM KOMPUTER",
        "topic": "Fragmentasi Memori dan Strategi Alokasi Dinamis: First-Fit vs Best-Fit",
        "stem": "Dalam manajemen memori sistem operasi tanpa paging (contiguous memory allocation), pemuatan dan penghentian proses secara bergantian dapat menyebabkan fenomena Fragmentasi Eksternal (External Fragmentation). Kondisi yang mencirikan terjadinya fragmentasi eksternal adalah...",
        "correct": "Total ruang memori kosong yang tersedia di sistem sebenarnya mencukupi untuk menampung proses baru, namun ruang memori tersebut terpecah-pecah menjadi blok-blok kecil yang tidak berurutan (non-contiguous) sehingga sistem gagal mengalokasikannya.",
        "distractors": [
            "Ruang memori yang dialokasikan untuk suatu proses jauh lebih besar daripada kebutuhan data proses sehingga terjadi pemborosan ruang di dalam blok partisi.",
            "Modul perangkat keras RAM mengalami kerusakan sirkuit fisik akibat kelebihan panas voltase listrik.",
            "Sistem operasi kehabisan alamat bit register Program Counter untuk mengeksekusi instruksi perulangan.",
            "Kecepatan transfer data memori cache L3 lebih lambat daripada kecepatan pembacaan piringan magnetik hard disk."
        ],
        "formula": {
            "title": "KOMPARASI FRAGMENTASI MEMORI SISTEM OPERASI",
            "latex": "\\begin{aligned} \\text{Fragmentasi Internal:} & \\quad \\text{Ruang terbuang DI DALAM blok partisi teralokasi (Partisi Tetap)} \\\\ \\text{Fragmentasi Eksternal:} & \\quad \\text{Total memori bebas } \\sum \\text{Hole} \\ge \\text{Kebutuhan}, \\text{ tapi NON-CONTIGUOUS (Partisi Dinamis)} \\end{aligned}",
            "legend": "• Solusi Fragmentasi Eksternal: Pemadatan Memori (Compaction) atau beralih ke Memori Virtual Paging<br>• Strategi Alokasi: First-Fit (tercepat), Best-Fit (menyisakan lubang terkecil), Worst-Fit (menyisakan lubang terbesar)"
        },
        "hints": {
            "concept": "Fragmentasi eksternal: total memori bebas cukup, namun terpecah-pecah menjadi lubang kecil yang tidak berdampingan (non-contiguous).",
            "execution": "Pilih: Total memori kosong mencukupi tetapi terpecah-pecah menjadi blok kecil yang tidak bersebelahan."
        }
    },
    {
        "id": "inf-lat-h-22",
        "materi": "KRIPTOGRAFI & KEAMANAN SIBER",
        "topic": "Mekanisme Otentikasi dan Non-Repudiation pada Tanda Tangan Digital",
        "stem": "Tanda Tangan Digital (Digital Signature) menjamin integritas data, otentikasi pengirim, dan nirsangkal (non-repudiation) dalam transaksi elektronik. Alur pembentukan tanda tangan digital oleh pengirim (Alice) serta proses verifikasinya oleh penerima (Bob) yang benar secara kriptografis adalah...",
        "correct": "Alice membuat intisari pesan (hash) $\\rightarrow$ Mengenkripsi hash tersebut menggunakan Private Key miliknya sendiri untuk menghasilkan Digital Signature; Bob memverifikasinya dengan mendekripsi Digital Signature menggunakan Public Key milik Alice, lalu membandingkan hasilnya dengan hash dokumen yang dihitungnya sendiri.",
        "distractors": [
            "Alice mengenkripsi seluruh dokumen menggunakan Public Key milik Bob; Bob mendekripsinya menggunakan Private Key milik Alice.",
            "Alice mengenkripsi hash dokumen menggunakan Public Key milik Bob; Bob mendekripsinya menggunakan kunci simetris AES bersama.",
            "Alice menandatangani berkas dengan foto tanda tangan basah; Bob memverifikasinya menggunakan perangkat lunak OCR komputer.",
            "Alice mengirimkan Private Key miliknya ke Bob melalui surel terbuka agar Bob dapat mendekripsi dokumen rahasia."
        ],
        "formula": {
            "title": "ALUR KRIPTOGRAFIS TANDA TANGAN DIGITAL (DIGITAL SIGNATURE)",
            "latex": "\\begin{aligned} \\text{Pemberian Tanda Tangan (Alice):} & \\quad S = \\text{Encrypt}_{\\text{Priv}_A}(\\text{Hash}(M)) \\\\ \\text{Verifikasi Tanda Tangan (Bob):} & \\quad \\text{Decrypt}_{\\text{Pub}_A}(S) \\stackrel{?}{=} \\text{Hash}(M) \\implies \\text{Otentik & Utuh!} \\end{aligned}",
            "legend": "• Non-Repudiation (Nirsangkal): Hanya Alice yang memiliki Private Key miliknya, sehingga Alice tidak dapat menyangkal telah menandatangani pesan tersebut<br>• Integritas: Jika pesan $M$ dimodifikasi penyerang sekecil apapun, nilai hash tidak akan cocok"
        },
        "hints": {
            "concept": "Digital Signature dibuat dengan mengenkripsi hash pesan memakai Kunci Privat pengirim. Diverifikasi penerima memakai Kunci Publik pengirim.",
            "execution": "Pilih: Alice mengenkripsi hash memakai Private Key miliknya; Bob memverifikasi mendekripsi memakai Public Key Alice."
        }
    },
    {
        "id": "inf-lat-h-23",
        "materi": "PRAKTIK LINTAS BIDANG",
        "topic": "Strategi Rilis Perangkat Lunak: Blue-Green vs Canary Deployment",
        "stem": "Dalam arsitektur pipeline CI/CD modern, tim rekayasa perangkat lunak ingin merilis pembaruan aplikasi besar tanpa mengalami waktu henti (zero downtime) dan meminimalkan risiko gangguan operasional bagi seluruh pengguna. Strategi rilis Canary Deployment bekerja dengan cara...",
        "correct": "Mengarahkan sebagian kecil lalu lintas pengguna nyata (misalnya 5%–10%) ke versi aplikasi baru secara bertahap sambil memantau metrik performa dan log galat; jika stabil, lalu lintas dinaikkan bertahap hingga 100%, namun jika terdeteksi galat, rute lalu lintas langsung dibalikkan kembali ke versi lama.",
        "distractors": [
            "Menyiapkan dua lingkungan produksi identik penuh (Blue dan Green) lalu mengalihkan sakelar router 100% secara instan.",
            "Mematikan server produksi selama 6 jam di tengah malam untuk menginstal pembaruan basis data secara manual.",
            "Merilis kode yang belum diuji coba langsung ke repositori publik tanpa melalui tahapan kompilasi dan audit keamanan.",
            "Menghapus seluruh basis data pengguna lama agar aplikasi versi baru dapat berjalan dengan memori kosong optimal."
        ],
        "formula": {
            "title": "KOMPARASI STRATEGI DEPLOYMENT MODERN",
            "latex": "\\begin{aligned} \\text{Blue-Green:} & \\quad \\text{Environment Aktif (Blue)} \\xrightarrow{\\text{Switch Router 100\\%}} \\text{Environment Baru (Green)} \\implies \\text{Instant Switch} \\\\ \\text{Canary:} & \\quad 95\\% \\text{ Traffic} \\to v1.0 \\quad \\land \\quad 5\\% \\text{ Traffic} \\to v2.0 \\implies \\text{Gradual Rollout & Telemetry Audit} \\end{aligned}",
            "legend": "• Asal Istilah: Burung kenari (canary) di tambang batu bara sebagai pendeteksi dini gas beracun<br>• Keunggulan Canary: Jika ada bug fatal, hanya sebagian kecil pengguna uji coba yang terdampak sebelum rilis massal"
        },
        "hints": {
            "concept": "Canary deployment mengalirkan persentase kecil traffic (misal 5-10%) ke versi baru bertahap sambil memantau metrik kesehatan aplikasi.",
            "execution": "Pilih opsi yang menjelaskan pengalihan sebagian kecil lalu lintas secara bertahap sambil memantau metrik performa."
        }
    },
    {
        "id": "inf-lat-h-24",
        "materi": "ANALISIS DATA",
        "topic": "Analisis Asosiasi Fitur: Korelasi Pearson vs Spearman Rank",
        "stem": "Seorang data scientist memeriksa hubungan antara jam belajar harian ($X$) dan nilai ujian kelulusan ($Y$). Setelah dibuatkan diagram pencar (scatter plot), terlihat bahwa hubungan antar variabel bersifat monotonik non-linier melengkung kuat (eksponensial mulus tanpa hubungan garis lurus sempurna). Koefisien korelasi yang paling valid dan akurat digunakan untuk mengukur kekuatan hubungan monotonik tersebut adalah...",
        "correct": "Koefisien Korelasi Spearman Rank ($r_s$), karena menghitung korelasi berdasarkan peringkat data (ranking) sehingga mampu menangkap hubungan monotonik non-linier dan lebih tangguh terhadap keberadaan nilai pencilan (outlier) daripada Korelasi Pearson.",
        "distractors": [
            "Koefisien Korelasi Pearson ($r$), karena secara eksklusif hanya mengukur hubungan keterkaitan garis lurus linier sempurna antar variabel kontinu.",
            "Koefisien Determinasi Regresi Kuadrat Terkecil, yang mengasumsikan variansi galat berdistribusi Poisson diskret.",
            "Uji Hipotesis Chi-Square Independensi, yang khusus dirancang untuk menguji keterkaitan dua variabel data kategorik nominal.",
            "Koefisien Gini Kemiskinan, yang mengukur ketimpangan distribusi pendapatan populasi dalam kurva Lorenz."
        ],
        "formula": {
            "title": "KOMPARASI KOEFISIEN KORELASI STATISTIKA DATA",
            "latex": "\\begin{aligned} \\text{Pearson } r: & \\quad \\frac{\\sum (X - \\bar{X})(Y - \\bar{Y})}{\\sqrt{\\sum (X - \\bar{X})^2 \\sum (Y - \\bar{Y})^2}} \\implies \\text{Hubungan Garis Lurus (Linier Murni)} \\\\ \\text{Spearman } r_s: & \\quad 1 - \\frac{6 \\sum d_i^2}{n(n^2 - 1)} \\implies \\text{Hubungan Monotonik Non-Linier Berdasarkan Ranking} \\end{aligned}",
            "legend": "• Monotonik: Ketika $X$ naik, $Y$ selalu naik (atau selalu turun), meskipun tidak membentuk garis lurus linier<br>• Pearson sensitif terhadap outlier dan gagal mendeteksi kelengkungan non-linier"
        },
        "hints": {
            "concept": "Untuk hubungan monotonik non-linier dan data bertingkat, gunakan Korelasi Spearman Rank (berbasis peringkat data).",
            "execution": "Pilih: Koefisien Korelasi Spearman Rank (r_s)."
        }
    },
    {
        "id": "inf-lat-h-25",
        "materi": "DAMPAK SOSIAL INFORMATIKA",
        "topic": "Etika Kecerdasan Buatan: Bias Algoritmik dan Explainable AI (XAI)",
        "stem": "Sebuah sistem kecerdasan buatan (Machine Learning) yang digunakan untuk menyaring calon penerima beasiswa universitas secara otomatis ditemukan menolak berkas lamaran dari pendaftar perempuan dan kelompok minoritas dengan probabilitas yang jauh lebih tinggi daripada kelompok mayoritas, meskipun memiliki kualifikasi akademik yang setara. Fenomena diskriminasi komputasi ini serta upaya solutifnya dalam etika AI adalah...",
        "correct": "Bias Algoritmik (Algorithmic Bias), yang timbul akibat data historis pelatihan yang tidak representatif atau mengandung prasangka masa lalu manusia; solusinya memerlukan audit keadilan data (fairness metrics), penyeimbangan dataset, dan penerapan Explainable AI (XAI) untuk transparansi keputusan.",
        "distractors": [
            "Overfitting Model Komputasi; diselesaikan dengan mematikan algoritma backpropagation jaringan saraf tiruan secara total.",
            "Underfitting Data Latihan; diselesaikan dengan menghapus seluruh data kualifikasi akademik pendaftar dari model.",
            "Kegagalan Hardware GPU; diselesaikan dengan mengganti sirkuit grafis prosesor kecerdasan buatan dengan chip kuantum.",
            "Kejahatan Siber Phishing; diselesaikan dengan mengubah kata sandi masuk ke basis data universitas secara berkala."
        ],
        "formula": {
            "title": "ETIKA DAN TATA KELOLA KECERDASAN BUATAN (AI ETHICS & FAIRNESS)",
            "latex": "\\text{Model ML Adil} \\implies \\text{Equalized Odds} \\land \\text{Demographic Parity} \\land \\text{Explainability (XAI)}",
            "legend": "• Sumber Bias Algoritmik: Sampling bias pada dataset historis, proxy variable tersembunyi, ketiadaan representasi minoritas<br>• Explainable AI (SHAP / LIME): Membuka kotak hitam (black-box) algoritma agar fitur penentu keputusan dapat dipertanggungjawabkan secara hukum dan etika"
        },
        "hints": {
            "concept": "Diskriminasi otomatis akibat data pelatihan historis yang timpang disebut Algorithmic Bias. Solusinya dengan audit keadilan dataset dan Explainable AI (XAI).",
            "execution": "Pilih opsi yang menyebutkan Bias Algoritmik (Algorithmic Bias) dan solusi audit keadilan serta Explainable AI (XAI)."
        }
    }
]
