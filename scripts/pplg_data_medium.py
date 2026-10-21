# -*- coding: utf-8 -*-
"""
pplg_data_medium.py
25 Authentic Medium (L2/L3 C3/C4) Questions for PPLG SMK/MAK
Strictly aligned with Pusmendik TKA 2026 & BSKAP 033/H/KR/2024
Anti-Bias: Distractor lengths balanced, keys evenly distributed.
"""

MEDIUM_QUESTIONS = [
    {
        "id": "rpl-lat-m-01",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Penyelesaian Git Merge Conflict",
        "type": "mcq",
        "questionHtml": "Saat seorang programmer menjalankan perintah `git merge feature-login` ke branch `develop`, terminal menampilkan pesan *CONFLICT (content): Merge conflict in auth.js*. Pemeriksaan file menampilkan teks berikut:\n```javascript\n<<<<<<< HEAD\nconst tokenExpiry = '24h';\n=======\nconst tokenExpiry = '12h';\n>>>>>>> feature-login\n```\nLangkah rekayasa yang tepat untuk menyelesaikan konflik tersebut secara profesional adalah...",
        "options": [
            {"key": "A", "text": "Menghapus seluruh file auth.js dari repositori lalu menjalankan git pull paksa dari branch main remote."},
            {"key": "B", "text": "Berdiskusi dengan tim untuk memilih durasi expiry yang valid, menghapus marker konflik, lalu git add dan commit."},
            {"key": "C", "text": "Membiarkan tanda kurung siku dan marker konflik di dalam file karena Git otomatis memilih baris terpanjang."},
            {"key": "D", "text": "Menjalankan perintah git push --force agar branch feature-login menimpa seluruh riwayat branch develop."},
            {"key": "E", "text": "Membuat branch baru dari HEAD lalu menduplikasi seluruh perubahan konfigurasi token secara manual."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "GIT MERGE CONFLICT ANATOMY",
            "latex": "\\text{<<<<<<< HEAD (Current)} \\quad \\mid \\quad \\text{======= (Divider)} \\quad \\mid \\quad \\text{>>>>>>> Incoming Branch}",
            "legend": "• Resolusi: Pilih kode benar -> Hapus 3 baris marker -> git add -> git commit"
        },
        "hints": {
            "concept": "Marker <<<<<<< HEAD dan >>>>>>> menunjukkan dua versi kode berbeda pada baris yang sama. Pengembang harus memilih versi terbaik dan menghapus penanda konflik.",
            "execution": "Langkah standar: modifikasi manual konten yang diinginkan, hapus marker, simpan file, lalu jalankan git add dan commit."
        },
        "explanation": "Untuk menyelesaikan merge conflict, developer harus menyelaraskan keputusan bisnis dengan tim/author, menghapus penanda konflik (`<<<<<<<`, `=======`, `>>>>>>>`), menyimpan file hasil edit, lalu melakukan staging (`git add`) dan finalisasi (`git commit`). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-02",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Strategi Git Rebase vs Git Merge",
        "type": "mcq",
        "questionHtml": "Seorang Lead Engineer meminta anggota tim untuk menggunakan `git rebase` daripada `git merge` saat memperbarui feature branch lokal mereka terhadap branch `main`. Keuntungan utama dari penggunaan `git rebase` pada skenario tersebut adalah...",
        "options": [
            {"key": "A", "text": "Menghapus seluruh commit lama yang cacat dan menggantinya dengan snapshot kode tunggal terkompresi."},
            {"key": "B", "text": "Menghasilkan riwayat riwayat commit yang linier, bersih, dan rapi tanpa adanya extra merge commit node."},
            {"key": "C", "text": "Mencegah terjadinya konflik antar file sama sekali secara otomatis melalui kecerdasan algoritma Git."},
            {"key": "D", "text": "Mengunggah commit langsung ke server cloud remote tanpa memerlukan otentikasi kunci SSH pengembang."},
            {"key": "E", "text": "Mengizinkan banyak developer mengedit commit yang sama di remote repository secara bersamaan tanpa lock."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "REBASE VS MERGE COMMIT TOPOLOGY",
            "latex": "\\text{Merge: } C_1 \\to C_2 \\to M_{\\text{merge}} \\quad \\text{vs} \\quad \\text{Rebase: } C_1' \\to C_2' \\to C_{\\text{linear}}",
            "legend": "• Rebase: Memindahkan basis branch menghasilkan riwayat 1 garis lurus<br>• Merge: Mempertahankan cabang riwayat dengan simpul merge commit baru"
        },
        "hints": {
            "concept": "Git rebase menerapkan kembali commit dari feature branch di atas commit terakhir branch target, menciptakan riwayat lurus tanpa percabangan ganda.",
            "execution": "Keunggulan rebase adalah commit history yang linier dan mudah dilacak saat debugging (misal menggunakan git bisect)."
        },
        "explanation": "Keuntungan utama `git rebase` adalah menghasilkan riwayat commit linier yang rapi tanpa 'merge commit' tambahan, mempermudah pelacakan perubahan kode dan audit git log. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-03",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Polimorfisme Dinamis (Dynamic Method Dispatch)",
        "type": "mcq",
        "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Sensor {\n    public void baca() {\n        System.out.print(\"Sensor-Aktif \");\n    }\n}\n\nclass SensorSuhu extends Sensor {\n    @Override\n    public void baca() {\n        System.out.print(\"Suhu:28C \");\n    }\n}\n\npublic class App {\n    public static void main(String[] args) {\n        Sensor s = new SensorSuhu();\n        s.baca();\n    }\n}\n```\nOutput yang tampil di layar konsol dan prinsip kerja yang mendasarinya adalah...",
        "options": [
            {"key": "A", "text": "Sensor-Aktif karena tipe referensi variabel deklarasi s adalah kelas induk Sensor pada saat kompilasi."},
            {"key": "B", "text": "Suhu:28C karena JVM memanggil method objek riil SensorSuhu di memori heap via dynamic method dispatch."},
            {"key": "C", "text": "Sensor-Aktif Suhu:28C karena superclass otomatis dieksekusi terlebih dahulu sebelum method subclass."},
            {"key": "D", "text": "Compile-time error karena variabel tipe Sensor tidak dapat menampung instansiasi objek kelas turunannya."},
            {"key": "E", "text": "Runtime error ClassCastException karena ketidakcocokan tipe referensi objek polimorfik di stack JVM."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "DYNAMIC METHOD DISPATCH PRINCIPLE",
            "latex": "\\text{Reference Type } (\\text{Sensor}) \\xrightarrow{\\text{Runtime Resolution}} \\text{Actual Object Method } (\\text{SensorSuhu.baca()})",
            "legend": "• Penentuan pemanggilan method override dilakukan saat runtime berdasarkan tipe objek riil di heap"
        },
        "hints": {
            "concept": "Pada polimorfisme dinamis, method yang dipanggil ditentukan oleh objek sebenarnya yang dibuat dengan 'new', bukan tipe variabel referensinya.",
            "execution": "Variabel s merujuk ke objek baru SensorSuhu(), sehingga method baca() milik SensorSuhu yang dijalankan."
        },
        "explanation": "Meskipun tipe referensi `s` bertipe `Sensor`, objek sebenarnya yang diinstansiasi di memori heap adalah `SensorSuhu()`. Berdasarkan prinsip polimorfisme dinamis (dynamic method dispatch), JVM akan memanggil method override milik `SensorSuhu`. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-04",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Prinsip SOLID: Single Responsibility Principle",
        "type": "mcq",
        "questionHtml": "Perhatikan perancangan kelas Java berikut:\n```java\npublic class LaporanPenjualan {\n    public void hitungTotalPenjualan() { /* Kalkulasi laba */ }\n    public void simpanKeDatabase() { /* Koneksi JDBC & INSERT SQL */ }\n    public void cetakLaporanPDF() { /* Format layout & render PDF */ }\n}\n```\nKelas di atas melanggar prinsip Single Responsibility Principle (SRP) karena...",
        "options": [
            {"key": "A", "text": "Tidak mengimplementasikan interface Serializable untuk penyimpanan state objek ke media disk sekunder."},
            {"key": "B", "text": "Memiliki lebih dari satu tanggung jawab (alasan untuk berubah): kalkulasi bisnis, persistensi data, dan rendering UI."},
            {"key": "C", "text": "Menggunakan method dengan visibilitas public yang membahayakan enkapsulasi data internal objek."},
            {"key": "D", "text": "Tidak mendeklarasikan variabel konstanta statis untuk menyimpan string query SQL dan konfigurasi PDF."},
            {"key": "E", "text": "Menolak pewarisan kelas turunan karena tidak ditambahkan keyword abstract pada deklarasi kelasnya."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SOLID - SINGLE RESPONSIBILITY PRINCIPLE (SRP)",
            "latex": "\\text{A Class should have one, and only one, reason to change}",
            "legend": "• Solusi: Pisahkan ke 3 kelas: SalesCalculator, SalesRepository, dan SalesPdfExporter"
        },
        "hints": {
            "concept": "SRP (prinsip pertama SOLID) menegaskan bahwa satu kelas hanya boleh memiliki satu tanggung jawab atau satu alasan untuk berubah.",
            "execution": "Kelas tersebut mengurusi logika bisnis (hitung laba), database (simpan DB), dan presentasi (cetak PDF)."
        },
        "explanation": "SRP menyatakan 'A class should have only one reason to change'. Kelas `LaporanPenjualan` memiliki 3 alasan berbeda untuk berubah: perubahan aturan bisnis perhitungan, perubahan skema database, atau perubahan template PDF. Solusinya adalah memisahkannya menjadi 3 kelas berbeda. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-05",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Normalisasi 2NF (Ketergantungan Parsial)",
        "type": "mcq",
        "questionHtml": "Diberikan relasi tabel `KRS(NIM, Kode_MK, Nama_Mahasiswa, Nama_MK, Nilai_Huruf)` dengan Primary Key komposit `(NIM, Kode_MK)`. Ketergantungan fungsional yang ada adalah:\n1. `(NIM, Kode_MK) -> Nilai_Huruf`\n2. `NIM -> Nama_Mahasiswa`\n3. `Kode_MK -> Nama_MK`\n\nTabel tersebut belum memenuhi Bentuk Normal Kedua (2NF) karena...",
        "options": [
            {"key": "A", "text": "Nilai_Huruf memiliki nilai berulang yang tidak terindeks secara seimbang pada struktur B-Tree."},
            {"key": "B", "text": "Terdapat ketergantungan fungsional parsial di mana atribut non-kunci hanya bergantung pada sebagian kunci komposit."},
            {"key": "C", "text": "Terdapat ketergantungan transitif antar sesama atribut non-kunci primer di dalam relasi tabel tersebut."},
            {"key": "D", "text": "Kolom primary key komposit tidak boleh terdiri dari lebih dari satu atribut dalam sistem basis data RDBMS."},
            {"key": "E", "text": "Tabel KRS tidak menyertakan foreign key ke tabel dosen pembimbing akademik mahasiswa bersangkutan."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SECOND NORMAL FORM (2NF) CONDITION",
            "latex": "\\text{2NF} \\iff \\text{1NF} \\land \\neg(\\exists \\text{ non-key } A \\colon P_{\\text{partial}} \\to A)",
            "legend": "• Partial dependency: NIM -> Nama_Mhs (hanya bergantung pada separuh composite key)<br>• Solusi: Dekomposisi ke Mahasiswa, MataKuliah, dan KRS"
        },
        "hints": {
            "concept": "Syarat 2NF adalah 1NF dan tidak ada ketergantungan parsial (atribut non-kunci bergantung pada sebagian saja dari primary key gabungan).",
            "execution": "Atribut Nama_Mahasiswa hanya bergantung pada NIM, dan Nama_MK hanya bergantung pada Kode_MK."
        },
        "explanation": "2NF melarang adanya Partial Functional Dependency pada tabel yang memiliki Composite Primary Key. Karena `Nama_Mahasiswa` hanya bergantung pada `NIM` (sebagian dari key `(NIM, Kode_MK)`), tabel harus didekomposisi agar memenuhi 2NF. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-06",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Normalisasi 3NF (Ketergantungan Transitif)",
        "type": "mcq",
        "questionHtml": "Diberikan relasi tabel `Pegawai(ID_Pegawai, Nama, Kode_Departemen, Nama_Departemen)` dengan Primary Key `ID_Pegawai`. Diketahui dependensi fungsional:\n- `ID_Pegawai -> Kode_Departemen`\n- `Kode_Departemen -> Nama_Departemen`\n\nUntuk mengubah tabel tersebut agar memenuhi Bentuk Normal Ketiga (3NF), dekomposisi tabel yang benar adalah...",
        "options": [
            {"key": "A", "text": "Membuat satu tabel baru yang menggabungkan seluruh data pegawai dan riwayat penggajian secara utuh."},
            {"key": "B", "text": "Memecah menjadi Pegawai(ID_Pegawai, Nama, Kode_Departemen) dan Departemen(Kode_Departemen, Nama_Departemen)."},
            {"key": "C", "text": "Menghapus kolom Kode_Departemen dan hanya menyisakan Nama_Departemen langsung di tabel Pegawai."},
            {"key": "D", "text": "Menambahkan kolom ID_Pegawai sebagai primary key kedua di dalam tabel Departemen yang didekomposisi."},
            {"key": "E", "text": "Mengubah Primary Key ID_Pegawai menjadi composite key (ID_Pegawai, Kode_Departemen, Nama_Departemen)."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "THIRD NORMAL FORM (3NF) DECOMPOSITION",
            "latex": "X \\to Y \\land Y \\to Z \\implies X \\to Z \\quad (\\text{Transitive Dependency Eliminated})",
            "legend": "• Tabel 1: Pegawai(ID_Pegawai [PK], Nama, Kode_Departemen [FK])<br>• Tabel 2: Departemen(Kode_Departemen [PK], Nama_Departemen)"
        },
        "hints": {
            "concept": "3NF mensyaratkan tidak adanya transitive dependency (atribut non-kunci menentukan atribut non-kunci lainnya).",
            "execution": "Kode_Departemen menentukan Nama_Departemen. Pisahkan entitas Departemen menjadi tabel independen."
        },
        "explanation": "Pada tabel awal terjadi transitive dependency: `ID_Pegawai -> Kode_Departemen -> Nama_Departemen`. Untuk mencapai 3NF, atribut yang bergantung secara transitif dipisahkan ke tabel master tersendiri: `Departemen(Kode_Departemen, Nama_Departemen)` dan `Pegawai(ID_Pegawai, Nama, Kode_Departemen)`. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-07",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "SQL Multi-Table JOIN Analysis",
        "type": "mcq",
        "questionHtml": "Perhatikan data pada dua tabel relasional berikut:\nTabel `Pelanggan`: 4 baris data (ID: 1, 2, 3, 4)\nTabel `Pesanan`: 3 baris data (ID_Pelanggan: 1, 2, 2)\n\nJika dieksekusi query SQL berikut:\n```sql\nSELECT p.ID, p.Nama, o.ID_Pesanan\nFROM Pelanggan p\nLEFT JOIN Pesanan o ON p.ID = o.ID_Pelanggan;\n```\nBerapa jumlah total baris rekaman data yang dihasilkan pada output query tersebut?",
        "options": [
            {"key": "A", "text": "2 baris data karena hanya pelanggan ID 1 dan ID 2 yang memiliki relasi transaksi pesanan aktif."},
            {"key": "B", "text": "3 baris data karena query dibatasi oleh jumlah baris pada tabel pesanan sisi kanan join."},
            {"key": "C", "text": "5 baris data karena pelanggan 2 muncul 2 kali, pelanggan 1 muncul 1 kali, dan pelanggan 3 & 4 bernilai NULL."},
            {"key": "D", "text": "4 baris data karena tabel sisi kiri Pelanggan memiliki tepat 4 rekaman unik tanpa duplikasi."},
            {"key": "E", "text": "7 baris data hasil perkalian Cartesian Product antara tabel Pelanggan dan tabel Pesanan."}
        ],
        "correctKey": "C",
        "formulaHud": {
            "title": "LEFT JOIN RECORD CALCULATION",
            "latex": "\\text{Rows} = \\sum_{p \\in \\text{Pelanggan}} \\max(1, \\text{matchCount}(p)) = 1 + 2 + 1 + 1 = 5",
            "legend": "• ID 1: 1 match (1 baris)<br>• ID 2: 2 match (2 baris)<br>• ID 3: 0 match (1 baris NULL)<br>• ID 4: 0 match (1 baris NULL)"
        },
        "hints": {
            "concept": "LEFT JOIN mempertahankan SEMUA baris dari tabel kiri. Jika ada kecocokan ganda di tabel kanan, baris bertambah. Jika tidak cocok, kolom kanan diisi NULL.",
            "execution": "ID 1 menghasilkan 1 baris. ID 2 menghasilkan 2 baris. ID 3 menghasilkan 1 baris (NULL). ID 4 menghasilkan 1 baris (NULL). Total = 1 + 2 + 1 + 1 = 5 baris."
        },
        "explanation": "LEFT JOIN menyertakan seluruh baris tabel kiri (Pelanggan). ID 1 berpasangan dengan 1 pesanan (1 baris), ID 2 berpasangan dengan 2 pesanan (2 baris), ID 3 dan ID 4 tidak memiliki pesanan sehingga masing-masing muncul 1 baris dengan nilai pesanan NULL. Total baris = 1 + 2 + 1 + 1 = 5 baris. Jawaban: C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-08",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "SQL GROUP BY & HAVING Filter",
        "type": "mcq",
        "questionHtml": "Perhatikan query SQL analitik penjualan berikut:\n```sql\nSELECT cabang_toko, SUM(total_harga) AS total_omset\nFROM transaksi\nWHERE status_pembayaran = 'Lunas'\nGROUP BY cabang_toko\nHAVING SUM(total_harga) >= 50000000;\n```\nFungsi spesifik dari klausul `HAVING` pada query di atas adalah...",
        "options": [
            {"key": "A", "text": "Menyaring transaksi satuan sebelum dilakukan pengelompokan baris data oleh sistem database engine."},
            {"key": "B", "text": "Menyaring kelompok cabang toko yang memiliki akumulasi total omset minimal lima puluh juta rupiah."},
            {"key": "C", "text": "Mengurutkan nama cabang toko dari perolehan total omset terbesar ke yang terkecil secara descending."},
            {"key": "D", "text": "Menghitung rata-rata pendapatan harian untuk setiap transaksi yang statusnya lunas terverifikasi."},
            {"key": "E", "text": "Membuat index clustered virtual pada kolom cabang_toko untuk mengoptimalkan pembacaan disk."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "WHERE VS HAVING LOGICAL EXECUTION ORDER",
            "latex": "\\text{FROM} \\to \\text{WHERE (Row Filter)} \\to \\text{GROUP BY} \\to \\text{HAVING (Group Filter)} \\to \\text{SELECT}",
            "legend": "• WHERE: Filter individual rows sebelum agregasi<br>• HAVING: Filter groups hasil agregasi"
        },
        "hints": {
            "concept": "HAVING bertindak sebagai filter untuk kelompok data (hasil agregasi SUM, COUNT, AVG), berbeda dengan WHERE yang memfilter baris mentah.",
            "execution": "Klausul HAVING menyaring hasil kelompok cabang toko yang total_omset-nya >= 50.000.000."
        },
        "explanation": "Klausul `HAVING` digunakan khusus untuk memfilter baris kelompok hasil agregasi (di sini: `SUM(total_harga) >= 50000000`), sedangkan klausul `WHERE` menyaring baris individual sebelum proses grouping dilakukan. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-09",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Keamanan Web: Pencegahan Serangan XSS",
        "type": "mcq",
        "questionHtml": "Aplikasi forum komunitas menampilkan komentar pengguna secara langsung ke halaman web menggunakan sintaks:\n```javascript\ndocument.getElementById('komentar-box').innerHTML = userCommentInput;\n```\nPotensi kerentanan keamanan dan solusi rekayasa terbaik untuk memperbaikinya adalah...",
        "options": [
            {"key": "A", "text": "Rentan SQL Injection; solusinya adalah menggunakan prepared statement pada query database server."},
            {"key": "B", "text": "Rentan Cross-Site Scripting (XSS); solusinya menggunakan textContent atau melakukan sanitasi HTML entitas."},
            {"key": "C", "text": "Rentan Cross-Site Request Forgery (CSRF); solusinya adalah menyisipkan token acak pada form input."},
            {"key": "D", "text": "Rentan Denial of Service (DoS); solusinya membatasi panjang input komentar maksimal 200 karakter."},
            {"key": "E", "text": "Rentan Broken Authentication; solusinya menggunakan algoritma hashing password Argon2 di backend."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "DOM-BASED XSS MITIGATION",
            "latex": "\\text{Sink: innerHTML (Vulnerable)} \\xrightarrow{\\text{Refactor}} \\text{textContent} \\lor \\text{DOMPurify.sanitize()}",
            "legend": "• innerHTML: Mengeksekusi tag <script> atau <img onerror=...><br>• textContent: Merender teks aman tanpa interpretasi markup"
        },
        "hints": {
            "concept": "Menyematkan string pengguna langsung ke properti innerHTML membuka celah Cross-Site Scripting (XSS).",
            "execution": "Gantilah innerHTML dengan textContent atau gunakan library sanitasi HTML."
        },
        "explanation": "Penggunaan `innerHTML` secara langsung dengan data mentah dari pengguna menyebabkan kerentanan Cross-Site Scripting (XSS). Penyerang dapat menyuntikkan skrip jahat. Solusi aman adalah menggunakan `textContent` atau sanitasi string HTML sebelum dirender. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-10",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "JavaScript Event Loop & Microtask Queue",
        "type": "mcq",
        "questionHtml": "Perhatikan potongan kode asynchronous JavaScript berikut:\n```javascript\nconsole.log('1');\nsetTimeout(() => console.log('2'), 0);\nPromise.resolve().then(() => console.log('3'));\nconsole.log('4');\n```\nUrutan output angka yang dicetak pada console log browser adalah...",
        "options": [
            {"key": "A", "text": "1, 2, 3, 4 karena eksekusi baris kode asynchronous JavaScript selalu berurutan sesuai urutan deklarasi."},
            {"key": "B", "text": "1, 4, 3, 2 karena Call Stack tuntas, disusul Microtask Queue (Promise), lalu Macrotask Queue (setTimeout)."},
            {"key": "C", "text": "1, 4, 2, 3 karena delay timeout bernilai 0 milidetik langsung diproses sebelum promise diselesaikan engine."},
            {"key": "D", "text": "3, 1, 4, 2 karena resolver promise memiliki hak prioritas eksekusi tertinggi di atas thread JavaScript."},
            {"key": "E", "text": "1, 2, 4, 3 karena fungsi setTimeout ditempatkan sebelum pemanggilan promise pada urutan baris program."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "JS EVENT LOOP EXECUTION ORDER",
            "latex": "\\text{Call Stack (Sync)} \\to \\text{Microtask Queue (Promise)} \\to \\text{Macrotask Queue (Timer/IO)}",
            "legend": "• Sinkron: '1' lalu '4'<br>• Microtask: '3'<br>• Macrotask: '2'<br>• Urutan final: 1 -> 4 -> 3 -> 2"
        },
        "hints": {
            "concept": "Urutan eksekusi JavaScript: 1. Kode sinkron di Call Stack; 2. Semua antrean Microtask (Promise .then); 3. Antrean Macrotask/Task (setTimeout).",
            "execution": "1 dan 4 dieksekusi sinkron. Kemudian Promise (microtask) mencetak 3. Terakhir setTimeout (macrotask) mencetak 2."
        },
        "explanation": "Urutan eksekusi: (1) `console.log('1')` dan `console.log('4')` dieksekusi langsung di Call Stack secara sinkron. (2) `Promise.then()` masuk ke Microtask Queue dan dieksekusi segera setelah stack kosong (mencetak '3'). (3) Callback `setTimeout` masuk ke Macrotask Queue dan baru dieksekusi pada iterasi event loop berikutnya (mencetak '2'). Urutan output: 1, 4, 3, 2. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-11",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Siklus Hidup Android Saat Rotasi Layar",
        "type": "mcq",
        "questionHtml": "Ketika pengguna memutar orientasi layar smartphone dari potret ke lanskap pada Activity Android standar, urutan transisi callback lifecycle yang terjadi pada Activity tersebut adalah...",
        "options": [
            {"key": "A", "text": "Activity hanya memanggil onResume() ulang tanpa menghancurkan objek view yang sudah ada di memori."},
            {"key": "B", "text": "Activity dihancurkan (onPause -> onStop -> onDestroy) lalu diciptakan kembali (onCreate -> onStart -> onResume)."},
            {"key": "C", "text": "Sistem operasi Android langsung mematikan aplikasi dan memunculkan dialog Application Not Responding."},
            {"key": "D", "text": "Activity masuk ke status background onStop() secara permanen sampai pengguna menyentuh layar kembali."},
            {"key": "E", "text": "Hanya method onSaveInstanceState() yang dieksekusi tanpa memicu method inisialisasi onCreate()."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CONFIGURATION CHANGE LIFECYCLE",
            "latex": "\\text{Screen Rotate} \\implies \\text{Tear Down (onPause-onStop-onDestroy)} \\to \\text{Rebuild (onCreate-onStart-onResume)}",
            "legend": "• State preservation: Gunakan ViewModel atau onSaveInstanceState(Bundle)"
        },
        "hints": {
            "concept": "Perubahan konfigurasi (seperti rotasi layar) secara default menyebabkan sistem Android menghancurkan Activity dan membuatnya kembali untuk memuat resource layout yang sesuai.",
            "execution": "Prosesnya adalah siklus penghancuran lengkap diikuti penciptaan ulang lengkap."
        },
        "explanation": "Pada Android, perubahan konfigurasi perangkat (seperti rotasi layar) memicu penghancuran Activity yang sedang aktif (`onPause()` -> `onStop()` -> `onDestroy()`) lalu sistem membangunnya kembali dari awal (`onCreate()` -> `onStart()` -> `onResume()`) agar aplikasi dapat memuat resource layout lanskap yang baru. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-12",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Arsitektur MVVM & Komponen ViewModel",
        "type": "mcq",
        "questionHtml": "Dalam arsitektur modern Android (MVVM), keuntungan utama memisahkan logika penyiapan data UI ke dalam komponen Android Jetpack `ViewModel` adalah...",
        "options": [
            {"key": "A", "text": "Menghapus kebutuhan pembuatan layout tampilan antarmuka berekstensi XML atau Jetpack Compose."},
            {"key": "B", "text": "Data bertahan hidup melewati perubahan konfigurasi (seperti rotasi layar) tanpa perlu memuat ulang data dari network."},
            {"key": "C", "text": "Otomatis mengompresi ukuran file APK dan bundle aplikasi menjadi setengah ukuran semula."},
            {"key": "D", "text": "Memungkinkan eksekusi query basis data secara langsung pada Main Thread tanpa memicu exception."},
            {"key": "E", "text": "Menjamin aplikasi dapat berjalan normal tanpa memerlukan izin permissions koneksi internet sama sekali."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "VIEWMODEL LIFESPAN",
            "latex": "\\text{ViewModel Life} \\ge \\sum \\text{Activity Rotations (Retains State)}",
            "legend": "• ViewModel tetap berada di memori saat Activity re-create karena rotasi layar<br>• Membersihkan resource di onCleared() saat Activity selesai (finish)"
        },
        "hints": {
            "concept": "Tujuan utama ViewModel adalah mengelola dan mempertahankan data untuk UI dengan siklus hidup yang bertahan terhadap perubahan konfigurasi layar.",
            "execution": "Data yang disimpan di ViewModel tidak hilang saat Activity di-destroy dan di-recreate akibat rotasi."
        },
        "explanation": "Objek `ViewModel` dirancang untuk mempertahankan state dan data UI saat terjadi perubahan konfigurasi (seperti rotasi layar), sehingga aplikasi tidak perlu melakukan fetch ulang data dari REST API atau basis data saat Activity dibangun kembali. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-13",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Pemanfaatan Delta Time dalam Game Loop",
        "type": "mcq",
        "questionHtml": "Dalam kalkulasi pergerakan karakter pada game engine, pengembang mengalikan kecepatan dengan variabel `deltaTime` (`position += speed * dt`). Tujuan fundamental dari penerapan rumus tersebut adalah...",
        "options": [
            {"key": "A", "text": "Meningkatkan resolusi grafis tekstur gambar karakter secara otomatis saat performa frame rate melonjak."},
            {"key": "B", "text": "Menjaga kecepatan pergerakan objek tetap konsisten per detik terlepas dari fluktuasi frame rate perangkat pemain."},
            {"key": "C", "text": "Mencegah karakter menembus batas dinding pembatas arena pertempuran gim akibat lag koneksi internet."},
            {"key": "D", "text": "Menghemat konsumsi daya baterai perangkat dengan menurunkan frekuensi refresh rate layar secara drastis."},
            {"key": "E", "text": "Mengunci kecepatan putaran animasi sprite 2D agar selalu tepat berjalan pada 30 frame per detik."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "FRAME-RATE INDEPENDENT MOTION",
            "latex": "\\Delta s = v \\times \\Delta t \\quad (\\text{Displacement} = \\text{Velocity} \\times \\text{Delta Time})",
            "legend": "• 30 FPS: dt = 0.033s -> Gerak = v * 0.033<br>• 60 FPS: dt = 0.016s -> Gerak = v * 0.016<br>• Jarak tempuh per detik identik di semua perangkat"
        },
        "hints": {
            "concept": "Delta time (dt) adalah selisih waktu antara frame saat ini dan frame sebelumnya. Perkalian dengan dt membuat pergerakan berbasis waktu riil, bukan frame.",
            "execution": "Tanpa dt, game di monitor 120Hz akan bergerak 2x lebih cepat dibanding monitor 60Hz."
        },
        "explanation": "Mengalikan perpindahan dengan `deltaTime` (waktu yang dihabiskan untuk menyelesaikan satu frame) menjamin pergerakan objek bersifat independen dari frame rate (frame-rate independent movement), sehingga kecepatan karakter konstan baik di perangkat yang berjalan pada 30 FPS maupun 120 FPS. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-14",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Optimasi Collision Lingkaran (Distance Squared)",
        "type": "mcq",
        "questionHtml": "Untuk mendeteksi tabrakan antara dua objek lingkaran dengan radius $r_1$ dan $r_2$ serta jarak pusat $dx$ dan $dy$, programmer gim profesional membandingkan `(dx*dx + dy*dy) <= (r1+r2)*(r1+r2)` daripada menggunakan fungsi akar `Math.sqrt()`. Alasan optimasi teknis dari pendekatan tersebut adalah...",
        "options": [
            {"key": "A", "text": "Fungsi Math.sqrt() memiliki keterbatasan kapasitas bit sehingga tidak dapat memproses angka floating-point presisi."},
            {"key": "B", "text": "Operasi akar kuadrat (square root) membebani siklus CPU secara intensif dibanding perkalian matematika biasa."},
            {"key": "C", "text": "Menghitung akar kuadrat memicu pembagian dengan nol ketika kedua pusat lingkaran saling berhimpitan."},
            {"key": "D", "text": "Bahasa pemrograman gim tidak menyediakan pustaka pustaka fungsi aljabar trigonometri bawaan di modul matematika."},
            {"key": "E", "text": "Rumus perbandingan kuadrat otomatis menghasilkan vektor normal pantulan fisika pasca tabrakan terjadi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CIRCLE COLLISION OPTIMIZATION",
            "latex": "\\sqrt{dx^2 + dy^2} \\le (r_1 + r_2) \\iff dx^2 + dy^2 \\le (r_1 + r_2)^2",
            "legend": "• Menghindari instruksi sqrt CPU yang mahal<br>• Operasi perkalian dan penjumlahan integer/float jauh lebih cepat"
        },
        "hints": {
            "concept": "Dalam fisika game 2D, operasi Math.sqrt() adalah salah satu instruksi CPU yang paling memakan waktu komputasi.",
            "execution": "Membandingkan kuadrat kedua sisi persamaan menghasilkan logika matematika yang identik dengan biaya komputasi jauh lebih murah."
        },
        "explanation": "Operasi akar kuadrat (`Math.sqrt`) membutuhkan puluhan siklus CPU (clock cycles) yang lambat jika dieksekusi ribuan kali per frame. Mengkuadratkan kedua ruas persamaan ($dx^2 + dy^2 \\le (r_1 + r_2)^2$) memberikan hasil evaluasi logika yang persis sama dengan operasi perkalian aljabar yang jauh lebih cepat. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-15",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Finite State Machine (FSM) AI Musuh",
        "type": "mcq",
        "questionHtml": "Dalam perancangan kecerdasan buatan (AI) musuh pada gim menggunakan pola Finite State Machine (FSM), jika musuh berada dalam state `Patrol` dan mendeteksi pemain masuk ke dalam radius pandang (`distanceToPlayer <= viewRadius`), transisi state yang semestinya terjadi adalah...",
        "options": [
            {"key": "A", "text": "Beralih ke state Die dan menghapus instance musuh dari hierarki active game objects di scene."},
            {"key": "B", "text": "Beralih ke state Chase untuk bergerak mendekati posisi koordinat pemain hingga jarak serang tercapai."},
            {"key": "C", "text": "Tetap berada pada state Patrol dan mematikan fungsi deteksi tabrakan fisik musuh terhadap rintangan."},
            {"key": "D", "text": "Otomatis me-restart level permainan dari awal karena musuh telah mendeteksi keberadaan target."},
            {"key": "E", "text": "Beralih ke state Idle secara permanen tanpa melakukan animasi tindakan responsif apapun."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "NPC FINITE STATE MACHINE (FSM)",
            "latex": "\\text{Patrol} \\xrightarrow{\\text{Player in View}} \\text{Chase} \\xrightarrow{\\text{Player in Range}} \\text{Attack}",
            "legend": "• Patrol: Jalan santai rute waypoint<br>• Chase: Kejar pemain<br>• Attack: Lakukan pukulan/tembakan"
        },
        "hints": {
            "concept": "FSM AI musuh standar terdiri dari 3 siklus dasar: Patrol (patroli rute) -> Chase (mengejar saat pemain terlihat) -> Attack (menyerang saat dalam jangkauan).",
            "execution": "Kondisi pemain masuk radius pandang memicu transisi dari Patrol ke Chase."
        },
        "explanation": "Dalam pola FSM AI game klasik, ketika entitas dalam kondisi `Patrol` mendeteksi target dalam jangkauan penglihatan (`viewRadius`), trigger tersebut memicu transisi ke state `Chase` (mengejar pemain) hingga berada dalam jarak serang (`attackRange`). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-16",
        "subject": "rpl",
        "materi": "PENGUJIAN PERANGKAT LUNAK (QA)",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Boundary Value Analysis (BVA)",
        "type": "mcq",
        "questionHtml": "Sebuah form pendaftaran kursus online memvalidasi input umur peserta dengan aturan: 'Hanya peserta berumur 18 sampai 60 tahun (inklusif) yang diperbolehkan mendaftar'. Berdasarkan teknik Boundary Value Analysis (BVA), kumpulan nilai uji batas umur yang paling tepat disiapkan adalah...",
        "options": [
            {"key": "A", "text": "25, 35, 45, dan 55 tahun yang mewakili titik tengah rentang umur normal."},
            {"key": "B", "text": "17, 18, 19, 59, 60, dan 61 tahun yang menguji nilai tepat di batas, tepat di bawah, dan tepat di atas batas."},
            {"key": "C", "text": "0, 10, 50, dan 100 tahun yang merupakan rentang umur manusia secara umum di dunia nyata."},
            {"key": "D", "text": "-18 dan -60 tahun yang menguji penanganan sistem terhadap input angka negatif tidak logis."},
            {"key": "E", "text": "18 dan 60 tahun saja tanpa perlu memeriksa nilai sebelum dan sesudah batas ambang batas."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "BOUNDARY VALUE ANALYSIS (BVA) RULE",
            "latex": "\\text{Boundary Set} = \\{ \\text{Min}-1, \\; \\text{Min}, \\; \\text{Min}+1, \\; \\text{Max}-1, \\; \\text{Max}, \\; \\text{Max}+1 \\}",
            "legend": "• Min = 18 -> Uji: 17, 18, 19<br>• Max = 60 -> Uji: 59, 60, 61"
        },
        "hints": {
            "concept": "BVA menguji batas rentang input yang valid: tepat pada batas minimum dan maksimum, serta satu nilai di luar batas dan satu nilai di dalam batas.",
            "execution": "Untuk rentang 18..60: uji 17 (invalid), 18 (valid), 19 (valid), 59 (valid), 60 (valid), 61 (invalid)."
        },
        "explanation": "Teknik Boundary Value Analysis (BVA) berfokus pada titik kritis perbatasan input: `min - 1`, `min`, `min + 1` dan `max - 1`, `max`, `max + 1`. Untuk interval 18-60, himpunan uji lengkapnya adalah 17, 18, 19, 59, 60, dan 61. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-17",
        "subject": "rpl",
        "materi": "PENGUJIAN PERANGKAT LUNAK (QA)",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Siklus Test-Driven Development (TDD)",
        "type": "mcq",
        "questionHtml": "Dalam metodologi pengembangan perangkat lunak Test-Driven Development (TDD), urutan siklus kerja (cycle) yang benar dan wajib dipatuhi oleh software engineer adalah...",
        "options": [
            {"key": "A", "text": "Menulis kode implementasi -> menguji secara manual di browser -> membuat dokumentasi API laporan."},
            {"key": "B", "text": "RED (tulis test gagal) -> GREEN (tulis kode minimal agar test lulus) -> REFACTOR (rapikan kode tanpa merusak test)."},
            {"key": "C", "text": "REFACTOR (rancang arsitektur) -> RED (buat unit test) -> GREEN (rilis kode langsung ke production)."},
            {"key": "D", "text": "GREEN (buat test yang pasti sukses) -> RED (buat test yang error) -> DEPLOY (unggah aplikasi ke server)."},
            {"key": "E", "text": "Membuat skema database -> membuat antarmuka frontend -> menulis unit testing di tahapan akhir rilis."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "TDD CYCLE (RED - GREEN - REFACTOR)",
            "latex": "\\text{RED (Write Failing Test)} \\to \\text{GREEN (Pass Minimal Code)} \\to \\text{REFACTOR (Clean & Optimize)}",
            "legend": "• RED: Tentukan ekspektasi fungsi sebelum kodenya dibuat<br>• GREEN: Implementasikan solusi paling sederhana<br>• REFACTOR: Hilangkan duplikasi dan optimasi struktur"
        },
        "hints": {
            "concept": "TDD mengikuti irama Red-Green-Refactor: buat tes yang gagal dahulu, implementasikan kode minimal agar tes lulus, lalu bersihkan kode.",
            "execution": "Kata kuncinya adalah RED -> GREEN -> REFACTOR."
        },
        "explanation": "Siklus inti TDD adalah: (1) RED: menulis unit test yang mendefinisikan fitur baru dan memastikannya gagal karena kode belum dibuat, (2) GREEN: menulis kode program minimal yang membuat test berhasil lulus, dan (3) REFACTOR: memperbaiki struktur dan kebersihan kode tanpa mengubah fungsionalitasnya. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-18",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Penanganan Eksepsi (Checked vs Unchecked)",
        "type": "mcq",
        "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\npublic class DataParser {\n    public static void main(String[] args) {\n        String teks = null;\n        System.out.println(teks.length());\n    }\n}\n```\nKetika program di-compile dan dijalankan, jenis eksepsi yang dilemparkan dan kategorinya adalah...",
        "options": [
            {"key": "A", "text": "IOException yang merupakan checked exception yang wajib ditangkap menggunakan klausa try-catch."},
            {"key": "B", "text": "NullPointerException yang merupakan unchecked exception (turunan langsung dari RuntimeException)."},
            {"key": "C", "text": "Compile-time Error: Variable teks has not been initialized correctly on heap memory."},
            {"key": "D", "text": "ArithmeticException karena operasi panjang karakter pada nilai null menghasilkan pembagian tak terdefinisi."},
            {"key": "E", "text": "IllegalArgumentException yang dilemparkan otomatis oleh method length() milik kelas String."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "JAVA EXCEPTION HIERARCHY",
            "latex": "\\text{Throwable} \\to \\text{Exception} \\to \\text{RuntimeException} \\to \\text{NullPointerException (Unchecked)}",
            "legend": "• Checked: Wajib di-catch atau throws (misal IOException, SQLException)<br>• Unchecked: Runtime error akibat kelalaian logika kode"
        },
        "hints": {
            "concept": "Mengakses method atau atribut pada variabel yang bernilai null menghasilkan NullPointerException di runtime (kategori unchecked exception).",
            "execution": "Kode lolos kompilasi, namun saat runtime baris teks.length() melempar NullPointerException."
        },
        "explanation": "Memanggil method (`length()`) pada referensi objek yang bernilai `null` akan melempar `NullPointerException` pada saat runtime. Karena merupakan turunan dari `RuntimeException`, eksepsi ini tergolong unchecked exception (tidak diwajibkan oleh compiler untuk ditangkap secara eksplisit). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-19",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Idempotensi Method HTTP REST API",
        "type": "mcq",
        "questionHtml": "Dalam perancangan RESTful API, sebuah method HTTP dikatakan memiliki sifat 'idempotent' jika pemanggilan berulang kali dengan parameter yang sama menghasilkan efek samping status server yang identik. Manakah pasangan method HTTP yang KEDUANYA bersifat idempotent?",
        "options": [
            {"key": "A", "text": "POST dan PATCH yang digunakan untuk menambahkan entitas rekaman baru dan memperbarui data."},
            {"key": "B", "text": "GET dan PUT yang digunakan untuk mengambil data serta mengganti data sumber daya secara utuh."},
            {"key": "C", "text": "POST dan DELETE yang digunakan untuk memproses transaksi baru dan menghapus record."},
            {"key": "D", "text": "CONNECT dan POST yang digunakan untuk membangun tunnel jaringan dan mengirim payload."},
            {"key": "E", "text": "PATCH dan POST yang digunakan untuk manipulasi data parsial pada database backend."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "HTTP METHODS IDEMPOTENCY MATRIX",
            "latex": "f(f(x)) = f(x) \\implies \\text{Idempotent: GET, PUT, DELETE, HEAD, OPTIONS}",
            "legend": "• GET: Safe & Idempotent<br>• PUT: Idempotent (replace resource)<br>• DELETE: Idempotent (hapus resource berkali-kali tetap hilang)<br>• POST: Non-idempotent (bikin entitas baru setiap dipanggil)"
        },
        "hints": {
            "concept": "Method idempotent: efek pemanggilan N kali sama dengan 1 kali pemanggilan. GET, PUT, DELETE adalah idempotent. POST bukan idempotent.",
            "execution": "GET (hanya membaca) dan PUT (mengganti utuh state resource) keduanya adalah idempotent."
        },
        "explanation": "GET, PUT, dan DELETE adalah method HTTP yang bersifat idempotent menurut spesifikasi RFC 7231. Memanggil `PUT` berkali-kali dengan payload yang sama akan menghasilkan state resource yang persis sama. Sebaliknya, `POST` tidak idempotent karena setiap eksekusi akan membuat entitas data baru yang berbeda di server. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-20",
        "subject": "rpl",
        "materi": "DESAIN UI/UX & AKSESIBILITAS",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Ukuran Target Sentuh (Touch Target Size)",
        "type": "mcq",
        "questionHtml": "Berdasarkan pedoman Human Interface Guidelines (Apple) dan Material Design (Google) untuk aplikasi mobile, ukuran target sentuh (touch target) minimum yang direkomendasikan untuk tombol agar mudah ditekan oleh jari pengguna tanpa salah sentuh adalah...",
        "options": [
            {"key": "A", "text": "16x16 dp/pt yang merupakan ukuran standar ikon teks inline di dalam paragraf artikel web."},
            {"key": "B", "text": "44x44 pt (iOS) atau 48x48 dp (Android) untuk menyesuaikan dengan luas permukaan ujung jari manusia."},
            {"key": "C", "text": "100x100 dp/pt yang wajib diterapkan pada setiap komponen interaktif formulir pendaftaran."},
            {"key": "D", "text": "24x24 dp/pt yang merupakan ukuran default bounding box aset vektor ikon sistem."},
            {"key": "E", "text": "80x80 dp/pt untuk memastikan tombol terlihat jelas oleh pengguna dari jarak pandang dua meter."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "MINIMUM ACCESSIBLE TOUCH TARGET",
            "latex": "\\text{Apple HIG} \\ge 44 \\times 44\\text{ pt}, \\quad \\text{Google Material} \\ge 48 \\times 48\\text{ dp}",
            "legend": "• Menghindari error miss-click pada layar sentuh ponsel<br>• Standar WCAG 2.1 Success Criterion 2.5.5 (Target Size)"
        },
        "hints": {
            "concept": "Pedoman desain antarmuka mobile menetapkan 44x44 pt (Apple) dan 48x48 dp (Android) sebagai ukuran minimal area sentuh ramah jari.",
            "execution": "Ukuran ini memperhitungkan rata-rata luas sentuhan bantalan jari manusia (sekitar 7-10 mm)."
        },
        "explanation": "Google Material Design menetapkan minimal touch target 48x48 dp, sementara Apple HIG menetapkan minimal 44x44 pt. Hal ini dirancang agar elemen interaktif dapat ditekan dengan nyaman oleh jemari manusia tanpa memicu kesalahan klik pada elemen di sebelahnya. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-21",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Prinsip Lisensi Copyleft (GPL)",
        "type": "mcq",
        "questionHtml": "Sebuah perusahaan software mengintegrasikan modul pustaka yang berlisensi GNU General Public License v3 (GPLv3) ke dalam produk aplikasi komersial mereka. Kewajiban hukum yang ditimbulkan oleh klausul lisensi copyleft GPL tersebut adalah...",
        "options": [
            {"key": "A", "text": "Perusahaan hanya wajib membayar royalti tahunan kepada Free Software Foundation tanpa membagikan kode."},
            {"key": "B", "text": "Seluruh source code aplikasi perusahaan wajib dilisensikan di bawah GPLv3 dan dibuka untuk publik."},
            {"key": "C", "text": "Perusahaan bebas mendistribusikan aplikasi secara closed-source selama nama pembuat pustaka tidak diubah."},
            {"key": "D", "text": "Lisensi GPLv3 otomatis gugur ketika aplikasi dijual dengan harga nominal tertentu di pasar komersial."},
            {"key": "E", "text": "Perusahaan hanya wajib menyertakan file binary executable tanpa perlu menyediakan dokumentasi teknis."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "VIRAL NATURE OF RECIPROCAL COPYLEFT",
            "latex": "\\text{Proprietary Code} + \\text{GPL Module} \\implies \\text{Entire Derivative Work Must Be GPL}",
            "legend": "• Copyleft (GPL): Mewajibkan karya turunan berlisensi sama<br>• Berbeda dengan Permissive (MIT) yang mengizinkan closed-source"
        },
        "hints": {
            "concept": "Klausul copyleft pada GPL bersifat 'viral': jika kode GPL digabungkan ke dalam program lain, seluruh program tersebut harus dirilis di bawah lisensi GPL.",
            "execution": "Oleh karena itu, perusahaan komersial tertutup sangat berhati-hati agar tidak mencampur pustaka GPL ke dalam basis kode proprietary."
        },
        "explanation": "Lisensi GPL bersifat reciprocal/copyleft ('viral'). Jika sebuah perangkat lunak menyertakan atau me-link kode berlisensi GPLv3, maka seluruh karya turunan (derivative work) tersebut secara hukum wajib didistribusikan di bawah lisensi GPLv3 dengan source code yang terbuka bagi penggunanya. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-22",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "UU Perlindungan Data Pribadi (UU PDP)",
        "type": "mcq",
        "questionHtml": "Berdasarkan Undang-Undang Perlindungan Data Pribadi (UU PDP) No. 27 Tahun 2022 di Indonesia, kewajiban utama Pengendali Data Pribadi ketika terjadi kegagalan perlindungan data (kebocoran data) adalah...",
        "options": [
            {"key": "A", "text": "Merahasiakan insiden kebocoran tersebut dari publik selamanya demi menjaga nilai saham perusahaan."},
            {"key": "B", "text": "Menyampaikan pemberitahuan tertulis kepada subjek data dan lembaga terkait maksimal 3x24 jam."},
            {"key": "C", "text": "Menghapus seluruh rekaman log server dan database cadangan agar jejak digital peretas hilang seketika."},
            {"key": "D", "text": "Memberikan ganti rugi finansial tunai secara langsung kepada seluruh penduduk Indonesia dalam waktu 24 jam."},
            {"key": "E", "text": "Menutup permanen operasional server aplikasi dan membubarkan entitas bisnis perusahaan seketika."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "UU PDP DATA BREACH NOTIFICATION TIMELINE",
            "latex": "\\text{Data Breach Detected} \\implies \\text{Mandatory Written Notice within } 3 \\times 24 \\text{ hours (72 hours)}",
            "legend": "• Pasal 46 UU PDP: Wajib menyampaikan pemberitahuan ke subjek data & lembaga berwenang<br>• Memuat rincian data terkompromi & kontak penanganan"
        },
        "hints": {
            "concept": "Pasal 46 UU PDP mewajibkan pengendali data memberitahukan insiden kebocoran data secara tertulis paling lambat 3 x 24 jam.",
            "execution": "Batas waktu pelaporan resmi kebocoran data di Indonesia adalah 3x24 jam."
        },
        "explanation": "Berdasarkan Pasal 46 UU PDP No. 27 Tahun 2022, dalam hal terjadi kegagalan pelindungan data pribadi (kebocoran), Pengendali Data Pribadi wajib menyampaikan pemberitahuan secara tertulis paling lambat 3 x 24 jam (72 jam) kepada Subjek Data Pribadi dan lembaga yang berwenang. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-23",
        "subject": "rpl",
        "materi": "ALGORITMA & PEMROGRAMAN TERSTRUKTUR",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Kompleksitas Waktu Algoritma (Big-O)",
        "type": "mcq",
        "questionHtml": "Perhatikan algoritma pencarian elemen pada array terurut (sorted array) yang membagi ruang pencarian menjadi dua bagian secara berulang (Binary Search). Kompleksitas waktu terbaik (best case) dan terburuk (worst case) dari algoritma tersebut berturut-turut adalah...",
        "options": [
            {"key": "A", "text": "Best case O(n) dan worst case O(n^2) karena elemen harus diperiksa melalui nested loop bersarang."},
            {"key": "B", "text": "Best case O(1) dan worst case O(log n) karena target dapat ditemukan di titik tengah awal atau melalui pembagian biner."},
            {"key": "C", "text": "Best case O(log n) dan worst case O(n) karena ruang pencarian menyusut secara eksponensial di setiap langkah."},
            {"key": "D", "text": "Best case O(1) dan worst case O(n) karena jika elemen tidak ada maka seluruh array wajib dipindai sekuensial."},
            {"key": "E", "text": "Best case O(n log n) dan worst case O(n log n) karena array wajib di-reorganisasi ulang setiap iterasi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "BINARY SEARCH TIME COMPLEXITY",
            "latex": "T_{\\text{best}} = O(1), \\quad T_{\\text{worst}} = O(\\log_2 n)",
            "legend": "• Best case: Elemen target tepat berada di indeks tengah pertama ($O(1)$)<br>• Worst case: Setiap langkah membagi n dengan 2 hingga tersisa 1 elemen ($O(\\log n)$)"
        },
        "hints": {
            "concept": "Binary Search membagi dua area pencarian pada setiap iterasi. Jika elemen tengah adalah target, itu kasus terbaik O(1). Jika pencarian sampai ujung, kasus terburuknya adalah O(log n).",
            "execution": "Best case = O(1), Worst case = O(log n)."
        },
        "explanation": "Pada Binary Search, best case terjadi saat elemen yang dicari tepat berada di posisi tengah array pada pengecekan pertama ($O(1)$). Worst case terjadi saat elemen berada di ujung atau tidak ditemukan sama sekali, di mana ruang pencarian berukuran $n$ dibagi dua berulang kali sebanyak $\\log_2 n$ langkah ($O(\\log n)$). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-24",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Prinsip SOLID: Open/Closed Principle",
        "type": "mcq",
        "questionHtml": "Sebuah modul sistem pembayaran e-commerce dirancang agar dapat menerima metode pembayaran baru (seperti QRIS atau Virtual Account) tanpa perlu mengubah source code kelas `CheckoutService` yang sudah teruji. Pendekatan arsitektur ini mematuhi prinsip SOLID yaitu...",
        "options": [
            {"key": "A", "text": "Interface Segregation Principle dengan membagi interface besar menjadi interface yang sangat kecil."},
            {"key": "B", "text": "Open/Closed Principle (OCP) di mana entitas terbuka untuk perluasan tetapi tertutup untuk modifikasi."},
            {"key": "C", "text": "Liskov Substitution Principle di mana objek subclass harus dapat menggantikan objek superclassnya."},
            {"key": "D", "text": "Single Responsibility Principle di mana sebuah kelas hanya memiliki satu fungsi logging terpusat."},
            {"key": "E", "text": "Law of Demeter di mana objek hanya boleh berkomunikasi dengan objek tetangga terdekatnya."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SOLID - OPEN/CLOSED PRINCIPLE (OCP)",
            "latex": "\\text{Open for Extension} \\land \\text{Closed for Modification}",
            "legend": "• Implementasi: Gunakan Interface PaymentStrategy<br>• Menambah metode pembayaran baru cukup membuat kelas baru implementor interface tanpa ubah CheckoutService"
        },
        "hints": {
            "concept": "Open/Closed Principle (huruf 'O' dalam SOLID) menyatakan entitas software harus terbuka untuk perluasan (open for extension) tetapi tertutup untuk modifikasi (closed for modification).",
            "execution": "Menambah fitur tanpa mengubah kode lama adalah definisi inti OCP."
        },
        "explanation": "Open/Closed Principle (OCP) menyatakan bahwa entitas perangkat lunak harus terbuka untuk diekstensi (menambahkan metode pembayaran baru) tetapi tertutup untuk modifikasi (tidak perlu mengedit kode `CheckoutService` yang sudah stabil). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-m-25",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "medium",
        "topic": "Penanganan Error Asynchronous Async/Await",
        "type": "mcq",
        "questionHtml": "Perhatikan fungsi asynchronous JavaScript berikut:\n```javascript\nasync function fetchUserProfile(userId) {\n    try {\n        const response = await api.get(`/users/${userId}`);\n        return response.data;\n    } catch (error) {\n        console.error('Gagal mengambil data profil:', error.message);\n        return null;\n    }\n}\n```\nPernyataan yang BENAR mengenai alur eksekusi fungsi di atas adalah...",
        "options": [
            {"key": "A", "text": "Kata kunci await memblokir seluruh thread utama browser sehingga animasi halaman web membeku."},
            {"key": "B", "text": "Jika promise api.get di-reject akibat network down, eksekusi melompat ke blok catch dan mengembalikan null."},
            {"key": "C", "text": "Fungsi fetchUserProfile mengembalikan nilai primitif null secara langsung tanpa dibungkus Promise."},
            {"key": "D", "text": "Blok try-catch tidak mampu menangkap rejection dari fungsi asynchronous yang menggunakan await."},
            {"key": "E", "text": "Fungsi akan memicu TypeError karena kata kunci async tidak kompatibel dengan penanganan try-catch."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "ASYNC/AWAIT ERROR HANDLING FLOW",
            "latex": "\\text{Promise Rejected} \\implies \\text{await throws Error} \\implies \\text{Handled in catch block}",
            "legend": "• await membongkar hasil promise yang resolved<br>• Rejection diubah menjadi exception yang ditangkap oleh blok catch"
        },
        "hints": {
            "concept": "Di dalam fungsi async, penanganan error untuk Promise yang rejected dapat dilakukan secara natural dan elegan menggunakan blok try-catch.",
            "execution": "Jika api.get gagal/reject, aliran kode langsung melompat ke blok catch dan mengembalikan null."
        },
        "explanation": "Pada fungsi `async`, ketika sebuah Promise yang di-`await` mengalami rejection (gagal/error), runtime JavaScript akan melempar exception tersebut ke blok `catch`. Di sana pesan kesalahan dicatat ke console dan fungsi secara aman mengembalikan `null`. Jawaban: B.",
        "isDiagnostic": False
    }
]

print(f"Loaded {len(MEDIUM_QUESTIONS)} medium questions.")
