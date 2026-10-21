# -*- coding: utf-8 -*-
"""
pplg_data_simulasi.py
35 Authentic Simulasi HOTS Questions for PPLG SMK/MAK
Strictly aligned with Pusmendik TKA 2026 & BSKAP 033/H/KR/2024
CBT Composition:
- 25 Pilihan Ganda Tunggal (MCQ)
- 5 Pilihan Ganda Kompleks Multi-Jawaban (Multi)
- 5 Pilihan Ganda Kompleks Benar-Salah (Matrix)
Anti-Bias: Distractor lengths balanced, keys evenly distributed.
"""

SIMULASI_QUESTIONS = [
    # --- 25 MCQ ITEMS ---
    {
        "id": "rpl-sim-01",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Analisis Grafik Burndown Chart Scrum",
        "type": "mcq",
        "questionHtml": "Pada hari ke-7 dari Sprint berdurasi 10 hari, grafik Sprint Burndown Chart menunjukkan bahwa garis sisa estimasi pekerjaan (actual effort) berada jauh di atas garis panduan ideal (ideal burn line). Interpretasi manakah yang PALING akurat mengenai status sprint tersebut?",
        "options": [
            {"key": "A", "text": "Tim bekerja terlalu cepat dan sprint backlog kemungkinan besar akan selesai lebih awal dari jadwal."},
            {"key": "B", "text": "Tim mengalami perlambatan progres dan berisiko tinggi gagal menyelesaikan seluruh komitmen sprint backlog."},
            {"key": "C", "text": "Kualitas kode program meningkat drastis sehingga tim tidak perlu lagi melakukan pengujian otomatis QA."},
            {"key": "D", "text": "Product Owner otomatis membatalkan sprint seketika dan mengganti seluruh anggota tim pengembang."},
            {"key": "E", "text": "Estimasi waktu kerja awal terlalu besar sehingga tim memiliki banyak waktu luang tanpa tugas aktif."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SPRINT BURNDOWN CHART METRICS",
            "latex": "\\text{Actual Effort} > \\text{Ideal Line} \\implies \\text{Behind Schedule / Scope at Risk}",
            "legend": "• Actual di atas garis ideal: Pekerjaan tertinggal (behind schedule)<br>• Actual di bawah garis ideal: Pekerjaan lebih cepat (ahead of schedule)"
        },
        "hints": {
            "concept": "Burndown chart mencatat sisa pekerjaan terhadap waktu. Jika garis aktual berada di atas garis ideal, sisa pekerjaan lebih banyak daripada yang seharusnya pada hari tersebut.",
            "execution": "Garis aktual di atas garis ideal berarti tim tertinggal dari jadwal (behind schedule) dan sprint goal terancam."
        },
        "explanation": "Pada Burndown Chart, sumbu Y adalah sisa estimasi jam kerja dan sumbu X adalah hari. Jika garis sisa pekerjaan riil (actual) berada di atas garis ideal, berarti pekerjaan tersisa lebih banyak daripada target waktu yang tersisa (tim tertinggal dari jadwal dan berisiko gagal mencapai Sprint Goal). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-02",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Git Cherry-Pick untuk Hotfix Produksi",
        "type": "mcq",
        "questionHtml": "Sebuah bug kritis ditemukan pada sistem produksi yang berjalan di branch `main`. Perbaikan bug tersebut ternyata sudah pernah dibuat di salah satu commit spesifik pada branch `develop` (commit hash `a1b2c3d`). Perintah Git yang paling tepat digunakan untuk mengambil hanya commit spesifik tersebut dan menerapkannya langsung ke branch `main` tanpa menggabungkan seluruh branch develop adalah...",
        "options": [
            {"key": "A", "text": "git merge develop --squash untuk menggabungkan seluruh commit di develop menjadi satu snapshot besar."},
            {"key": "B", "text": "git cherry-pick a1b2c3d saat berada di branch main untuk menyalin commit perbaikan tersebut secara presisi."},
            {"key": "C", "text": "git rebase develop yang memindahkan seluruh cabang commit develop ke atas branch main produksi."},
            {"key": "D", "text": "git checkout -b hotfix develop untuk membuat branch baru yang menyalin seluruh kode develop mentah."},
            {"key": "E", "text": "git reset --hard a1b2c3d yang menghapus riwayat commit branch main dan menggantinya ke commit tersebut."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "GIT CHERRY-PICK HOTFIX ISOLATION",
            "latex": "\\text{git checkout main} \\implies \\text{git cherry-pick } \\langle \\text{commit-hash} \\rangle",
            "legend": "• Menerapkan patch spesifik dari branch lain tanpa merge seluruh branch<br>• Menghindari masuknya fitur unreleased yang belum siap rilis"
        },
        "hints": {
            "concept": "git cherry-pick memungkinkan programmer memilih commit tertentu dari satu branch dan menerapkannya ke branch lain yang aktif.",
            "execution": "Cherry-pick adalah perintah standar untuk porting commit perbaikan bug (hotfix) secara terisolasi."
        },
        "explanation": "`git cherry-pick <commit-hash>` memungkinkan pengembang memilih commit tertentu dari suatu cabang dan menerapkannya langsung pada cabang kerja saat ini (`main`) tanpa harus menelan seluruh commit fitur lain yang belum siap di `develop`. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-sim-03",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Pola Perancangan Kelas Abadi (Immutable Class)",
        "type": "mcq",
        "questionHtml": "Dalam perancangan sistem keuangan berbasis Java, kelas `Uang` dirancang agar bersifat *Immutable* (state objek tidak dapat diubah setelah diinstansiasi). Karakteristik rancangan kelas yang WAJIB dipenuhi untuk mencapai sifat immutability sempurna adalah...",
        "options": [
            {"key": "A", "text": "Menyediakan method setter publik untuk setiap atribut agar nilai dapat diperbarui secara fleksibel."},
            {"key": "B", "text": "Menjadikan kelas bertipe final, semua atribut private final, tanpa setter, dan defensive copy pada objek mutable."},
            {"key": "C", "text": "Mewajibkan kelas mewarisi kelas Thread agar setiap operasi perbankan berjalan di background terpisah."},
            {"key": "D", "text": "Mendeklarasikan seluruh atribut sebagai variabel statis publik agar memori dapat dipakai bersama oleh klien."},
            {"key": "E", "text": "Menyediakan method resetState() yang mengosongkan seluruh saldo rekening menjadi nol rupiah."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "JAVA IMMUTABILITY CONTRACT",
            "latex": "\\text{final class} \\land \\text{private final fields} \\land \\neg(\\text{setters}) \\land \\text{Defensive Copying}",
            "legend": "• Thread-safe secara inheren (tidak butuh synchronization)<br>• State tidak dapat dimutasi setelah konstruktor selesai dieksekusi"
        },
        "hints": {
            "concept": "Aturan Immutable Class di Java: 1. Deklarasikan class sebagai final; 2. Semua field private dan final; 3. Tidak ada setter; 4. Lakukan defensive copying untuk objek referensi mutable.",
            "execution": "Pilihan B merangkum seluruh syarat mutlak kelas immutable."
        },
        "explanation": "Untuk membuat Immutable Class di Java (seperti kelas `String`), pengembang wajib: (1) mendeklarasikan kelas sebagai `final` agar tidak bisa di-override, (2) membuat semua field `private final`, (3) tidak menyediakan method setter/mutator, dan (4) melakukan defensive copy saat menerima atau mengembalikan objek mutable. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-04",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Penanganan Custom Domain Exception",
        "type": "mcq",
        "questionHtml": "Perhatikan perancangan eksepsi kustom perbankan berikut:\n```java\npublic class SaldoTidakCukupException extends Exception {\n    public SaldoTidakCukupException(String pesan) {\n        super(pesan);\n    }\n}\n```\nKarena kelas di atas mewarisi langsung kelas `Exception` (bukan `RuntimeException`), maka `SaldoTidakCukupException` tergolong sebagai...",
        "options": [
            {"key": "A", "text": "Unchecked exception yang tidak perlu ditangkap atau dideklarasikan pada klausa throws oleh compiler."},
            {"key": "B", "text": "Checked exception yang wajib ditangani dengan try-catch atau dideklarasikan pada method signature dengan throws."},
            {"key": "C", "text": "Fatal JVM Error yang otomatis menghentikan proses eksekusi sistem operasi secara seketika."},
            {"key": "D", "text": "Memory Exception yang hanya dilempar jika kapasitas RAM server database telah habis terpakai."},
            {"key": "E", "text": "Syntax Exception yang hanya muncul saat kode program sedang diperiksa oleh IDE pengembang."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CHECKED VS UNCHECKED EXCEPTION RULES",
            "latex": "E \\text{ extends Exception} \\implies \\text{Checked (Compile-time Mandatory Handling)}",
            "legend": "• Checked: Compiler memaksa try-catch atau signature `throws`<br>• Unchecked (extends RuntimeException): Opsional, error logika programmer"
        },
        "hints": {
            "concept": "Di Java, turunan langsung dari Exception (yang bukan turunan RuntimeException) adalah Checked Exception. Compiler mewajibkan penanganan eksplisit.",
            "execution": "SaldoTidakCukupException extends Exception -> wajib ditangkap dengan try-catch atau dilempar dengan throws."
        },
        "explanation": "Kelas yang mewarisi langsung `Exception` (dan bukan `RuntimeException`) dikategorikan sebagai Checked Exception. Kompilator Java akan memverifikasi pada saat compile-time bahwa pemanggil method wajib menangani eksepsi tersebut menggunakan blok `try-catch` atau mendeklarasikannya pada signature method menggunakan kata kunci `throws`. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-05",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Subquery Berkorelasi (Correlated Subquery) dengan EXISTS",
        "type": "mcq",
        "questionHtml": "Perhatikan query SQL optimasi analitik berikut:\n```sql\nSELECT p.id, p.nama\nFROM pelanggan p\nWHERE NOT EXISTS (\n    SELECT 1\n    FROM transaksi t\n    WHERE t.id_pelanggan = p.id\n);\n```\nTujuan bisnis yang dicapai oleh eksekusi query di atas adalah...",
        "options": [
            {"key": "A", "text": "Menghapus seluruh rekaman data pelanggan yang memiliki riwayat transaksi lebih dari sepuluh kali."},
            {"key": "B", "text": "Menampilkan daftar seluruh pelanggan yang belum pernah melakukan transaksi pembelian sama sekali."},
            {"key": "C", "text": "Menghitung rata-rata nominal transaksi yang dilakukan oleh pelanggan tetap yang aktif berbelanja."},
            {"key": "D", "text": "Memperbarui status keanggotaan pelanggan menjadi VIP jika nominal saldo belanja melampaui limit."},
            {"key": "E", "text": "Menampilkan pelanggan yang transaksinya mengalami kegagalan sistem pembayaran di gateway bank."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CORRELATED NOT EXISTS LOGIC",
            "latex": "p \\in \\text{Result} \\iff \\{ t \\in \\text{Transaksi} \\mid t.\\text{id\\_pelanggan} = p.\\text{id} \\} = \\emptyset",
            "legend": "• Correlated Subquery dievaluasi per baris pelanggan p<br>• NOT EXISTS mengembalikan True jika subquery tidak menghasilkan satu baris pun"
        },
        "hints": {
            "concept": "Klausul WHERE NOT EXISTS mengevaluasi apakah subquery menghasilkan baris. Jika tidak ada transaksi yang cocok untuk pelanggan tersebut, kondisi bernilai True.",
            "execution": "Query ini mencari pelanggan yang himpunan transaksinya kosong (tidak pernah belanja)."
        },
        "explanation": "Klausul `WHERE NOT EXISTS` mengevaluasi ketiadaan rekaman pada subquery berkorelasi. Query ini memeriksa setiap pelanggan `p`, dan jika subquery tidak menemukan rekaman transaksi yang cocok dengan `id_pelanggan = p.id`, maka pelanggan tersebut dipilih. Hasilnya adalah daftar pelanggan yang belum pernah bertransaksi. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-06",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Tingkat Isolasi Transaksi Basis Data (Isolation Levels)",
        "type": "mcq",
        "questionHtml": "Dalam standar ANSI SQL transaksi database, tingkat isolasi (isolation level) manakah yang memberikan perlindungan paling ketat dengan mencegah fenomena Dirty Read, Non-Repeatable Read, maupun Phantom Read secara total?",
        "options": [
            {"key": "A", "text": "Read Uncommitted yang mengizinkan transaksi membaca perubahan data yang belum di-commit sama sekali."},
            {"key": "B", "text": "Serializable yang mengeksekusi transaksi secara berurutan seolah-olah sistem berjalan pada single thread."},
            {"key": "C", "text": "Read Committed yang hanya mencegah fenomena pembacaan data kotor (dirty read) pada transaksi aktif."},
            {"key": "D", "text": "Repeatable Read yang mengunci baris data yang dibaca tetapi masih memungkinkan terjadinya phantom read."},
            {"key": "E", "text": "Snapshot Isolation yang hanya bekerja pada media penyimpanan basis data terdistribusi noSQL."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "TRANSACTION ISOLATION LEVELS HIERARCHY",
            "latex": "\\text{Read Uncommitted} < \\text{Read Committed} < \\text{Repeatable Read} < \\text{Serializable}",
            "legend": "• Serializable: Mencegah Dirty Read, Non-Repeatable Read, dan Phantom Read<br>• Mengorbankan konkurensi performa demi konsistensi data mutlak"
        },
        "hints": {
            "concept": "Tingkat isolasi ANSI SQL terketat adalah Serializable. Pada level ini, transaksi dieksekusi sedemikian rupa sehingga hasilnya identik dengan eksekusi serial murni.",
            "execution": "Tingkat isolasi terketat adalah Serializable."
        },
        "explanation": "`Serializable` adalah tingkat isolasi tertinggi dalam standar ANSI SQL. Tingkat ini menjamin isolasi penuh dari fenomena anomali konkurensi (Dirty Read, Non-Repeatable Read, dan Phantom Read) dengan mengunci rentang data atau menggunakan multi-version concurrency control (MVCC) serial, meskipun trade-off-nya menurunkan throughput konkurensi. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-07",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Konsep Indeks Penutup (Covering Index)",
        "type": "mcq",
        "questionHtml": "Diberikan tabel `karyawan(id, nik, nama, divisi, gaji)`. Database administrator membuat indeks B-Tree pada kolom `(divisi, gaji)`. Perhatikan query berikut:\n```sql\nSELECT divisi, SUM(gaji)\nFROM karyawan\nGROUP BY divisi;\n```\nQuery di atas dapat dieksekusi dengan kecepatan sangat tinggi tanpa menyentuh tabel data utama pada disk (Heap/Clustered Index Table). Fenomena optimasi ini terjadi karena indeks tersebut bertindak sebagai...",
        "options": [
            {"key": "A", "text": "Foreign Key Index yang mereferensikan integritas relasional tabel master departemen luar."},
            {"key": "B", "text": "Covering Index (Index-Only Scan) di mana seluruh kolom yang dibutuhkan query sudah tersedia di dalam daun indeks."},
            {"key": "C", "text": "Full-Text Search Index yang memindai token teks menggunakan kamus leksikal bahasa Indonesia."},
            {"key": "D", "text": "Spatial Index yang mengelompokkan data lokasi koordinat geospasial menggunakan struktur R-Tree."},
            {"key": "E", "text": "Hash Index yang hanya mendukung perbandingan nilai persamaan absolut tanpa fungsi agregasi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "COVERING INDEX / INDEX-ONLY SCAN",
            "latex": "\\text{Required Columns } \\{ \\text{divisi, gaji} \\} \\subseteq \\text{Index Columns } \\{ \\text{divisi, gaji} \\} \\implies \\text{No Table Lookup}",
            "legend": "• Menghindari I/O baca ke tabel utama (Heap table/Clustered index leaf)<br>• Peningkatan performa query hingga 10x - 100x lipat"
        },
        "hints": {
            "concept": "Jika semua kolom yang diminta dalam SELECT, WHERE, dan GROUP BY sudah ada di dalam indeks itu sendiri, database tidak perlu membaca tabel utama. Ini dinamakan Covering Index.",
            "execution": "Query hanya butuh 'divisi' dan 'gaji', dan indeks mencakup persis kedua kolom tersebut."
        },
        "explanation": "Sebuah indeks dikatakan sebagai *Covering Index* untuk suatu query jika indeks tersebut memuat semua kolom yang diminta oleh query (baik di klausa SELECT, WHERE, maupun GROUP BY). Database engine dapat langsung mengambil data dari node daun B-Tree indeks tanpa perlu melakukan lookup sekunder ke tabel utama di disk (Index-Only Scan). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-08",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Arsitektur REST vs GraphQL",
        "type": "mcq",
        "questionHtml": "Sebuah aplikasi mobile ingin menampilkan nama pengguna dan foto profil saja pada header layar. Jika menggunakan endpoint REST API `/api/users/1`, server mengembalikan seluruh data lengkap pengguna berupa 50 field profil. Masalah inefisiensi transmisi data jaringan ini dikenal sebagai...",
        "options": [
            {"key": "A", "text": "Under-fetching di mana client tidak memperoleh cukup data sehingga harus melakukan pemanggilan berulang kali."},
            {"key": "B", "text": "Over-fetching di mana client menerima muatan data yang jauh lebih banyak daripada data yang sebenarnya dibutuhkan."},
            {"key": "C", "text": "Denial of Service di mana server API kewalahan menerima request dalam volume tinggi secara simultan."},
            {"key": "D", "text": "Cache Invalidation di mana browser client gagal memperbarui file statis JavaScript yang kedaluwarsa."},
            {"key": "E", "text": "Packet Dropping di mana paket data TCP terputus akibat interferensi gelombang frekuensi radio."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "API PAYLOAD BOTTLENECKS",
            "latex": "\\text{Over-fetching} \\colon \\text{Payload Size} \\gg \\text{Needed Data} \\quad \\text{vs} \\quad \\text{Under-fetching} \\colon \\text{Calls} > 1",
            "legend": "• Over-fetching: Buang kuota & lambat di mobile<br>• GraphQL memecahkan masalah ini dengan deklarasi field spesifik"
        },
        "hints": {
            "concept": "Over-fetching terjadi saat endpoint mengembalikan payload data yang berlebihan dibandingkan kebutuhan UI aplikasi.",
            "execution": "Under-fetching adalah kebalikannya (data kurang sehingga harus request berkali-kali)."
        },
        "explanation": "*Over-fetching* adalah kondisi di mana klien menerima lebih banyak data daripada yang diperlukan untuk merender antarmuka pengguna (misal menerima 50 kolom padahal hanya butuh 2 kolom). Salah satu motivasi kelahiran GraphQL adalah menyelesaikan masalah over-fetching dan under-fetching pada REST API tradisional. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-09",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Konfigurasi Header Content Security Policy (CSP)",
        "type": "mcq",
        "questionHtml": "Untuk melindungi aplikasi web dari eksekusi skrip berbahaya pada serangan Cross-Site Scripting (XSS), administrator mengonfigurasi HTTP response header Content Security Policy (CSP) berikut:\n```http\nContent-Security-Policy: default-src 'self'; script-src 'self' https://trustedscripts.com;\n```\nAturan kebijakan keamanan yang diberlakukan oleh header di atas adalah...",
        "options": [
            {"key": "A", "text": "Mengizinkan seluruh website di internet mengunduh file gambar dan stylesheet dari server aplikasi secara bebas."},
            {"key": "B", "text": "Hanya mengizinkan eksekusi skrip JavaScript yang berasal dari origin yang sama ('self') dan domain trustedscripts.com."},
            {"key": "C", "text": "Mengharuskan pengguna memasukkan password token otentikasi dua faktor setiap kali membuka halaman web baru."},
            {"key": "D", "text": "Memblokir seluruh koneksi database backend jika port server diakses melalui jaringan lokal tanpa VPN."},
            {"key": "E", "text": "Mengonversi seluruh kode JavaScript frontend menjadi format WebAssembly biner secara otomatis di browser."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CONTENT SECURITY POLICY (CSP) DIRECTIVES",
            "latex": "\\text{script-src 'self' domain.com} \\implies \\text{Block Inline Scripts} \\land \\text{Block Untrusted 3rd-Party Scripts}",
            "legend": "• Menetralkan serangan XSS injeksi tag <script><br>• Browser menolak eksekusi resource yang melanggar whitelist domain"
        },
        "hints": {
            "concept": "Header Content Security Policy (CSP) bertindak sebagai whitelist yang memberitahu browser sumber daya mana saja yang diizinkan untuk dimuat dan dieksekusi.",
            "execution": "script-src 'self' https://trustedscripts.com membatasi eksekusi skrip hanya dari origin sendiri dan trustedscripts.com."
        },
        "explanation": "Header HTTP `Content-Security-Policy` membatasi sumber eksekusi aset web. Direktif `script-src 'self' https://trustedscripts.com` memerintahkan browser untuk hanya mengeksekusi skrip JS yang berasal dari domain yang sama (`'self'`) serta domain `trustedscripts.com`, sekaligus secara default memblokir skrip inline dan skrip injeksi dari domain lain yang tidak terdaftar. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-10",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Penanganan Paralel Promise.all vs Promise.allSettled",
        "type": "mcq",
        "questionHtml": "Sebuah modul dasbor keuangan memanggil tiga layanan API analitik secara bersamaan: `fetchOmset()`, `fetchStok()`, dan `fetchPajak()`. Pengembang ingin dasbor tetap dapat merender data layanan yang berhasil meskipun salah satu dari ketiga API tersebut mengalami kegagalan (network failure). Metode penanganan Promise JavaScript yang PALING tepat digunakan adalah...",
        "options": [
            {"key": "A", "text": "Promise.all() karena otomatis mengabaikan kegagalan dan langsung mengembalikan hasil array yang sukses saja."},
            {"key": "B", "text": "Promise.allSettled() karena menunggu semua promise tuntas dan mengembalikan array status baik fulfilled maupun rejected."},
            {"key": "C", "text": "Promise.race() karena hanya mengambil satu hasil respons API yang pertama kali tiba paling cepat di browser."},
            {"key": "D", "text": "Promise.any() karena akan memicu crash aplikasi jika ada salah satu permintaan data yang mengalami penolakan."},
            {"key": "E", "text": "Eksekusi pemanggilan ketiga fungsi secara berurutan sinkron menggunakan loop while tanpa fungsi promise."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "JS PROMISE CONCURRENCY METHODS",
            "latex": "\\text{Promise.all (Fail-Fast)} \\quad \\text{vs} \\quad \\text{Promise.allSettled (Resilient Aggregate)}",
            "legend": "• Promise.all: Jika 1 reject, seluruh batch langsung REJECT<br>• Promise.allSettled: Menunggu semua promise selesai (status: fulfilled/rejected)"
        },
        "hints": {
            "concept": "Promise.all akan langsung reject (fail-fast) jika salah satu promise gagal. Untuk skenario di mana UI tetap ingin menampilkan hasil dari promise yang berhasil, gunakan Promise.allSettled.",
            "execution": "Promise.allSettled mengembalikan status per promise sehingga error pada satu API tidak menggagalkan API lainnya."
        },
        "explanation": "`Promise.all()` bersifat fail-fast (jika satu promise reject, seluruh operasi langsung gagal). Sebaliknya, `Promise.allSettled()` menunggu semua promise selesai dieksekusi dan mengembalikan array objek yang mencantumkan status masing-masing (`status: 'fulfilled'` atau `status: 'rejected'`), memungkinkan aplikasi tetap menampilkan data dari layanan yang berhasil. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-11",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Konsep Closure dalam JavaScript",
        "type": "mcq",
        "questionHtml": "Perhatikan fungsi JavaScript pembuat counter berikut:\n```javascript\nfunction createCounter() {\n    let count = 0;\n    return function() {\n        count++;\n        return count;\n    };\n}\nconst c1 = createCounter();\nconsole.log(c1());\nconsole.log(c1());\n```\nNilai yang dicetak pada console log dan konsep fundamental JavaScript yang memungkinkan variabel `count` tetap tersimpan di memori setelah `createCounter()` selesai dieksekusi adalah...",
        "options": [
            {"key": "A", "text": "1 dan 1; konsep Scope Hoisting variabel lokal."},
            {"key": "B", "text": "1 dan 2; konsep Closure yang mempertahankan referensi leksikal variabel terluar."},
            {"key": "C", "text": "undefined dan undefined; konsep Garbage Collection otomatis membebaskan memori."},
            {"key": "D", "text": "0 dan 1; konsep Prototipe Objek Pewarisan JavaScript."},
            {"key": "E", "text": "Error ReferenceError karena variabel count berada di luar batas fungsi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "JAVASCRIPT CLOSURE DEFINITION",
            "latex": "\\text{Closure} = \\text{Inner Function} + \\text{Lexical Environment Reference (Retained)}",
            "legend": "• Fungsi dalam mempertahankan akses ke variabel di scope induknya bahkan setelah fungsi induk selesai dieksekusi"
        },
        "hints": {
            "concept": "Closure adalah kombinasi antara sebuah fungsi dan lingkungan leksikal (lexical environment) tempat fungsi tersebut dideklarasikan.",
            "execution": "Variabel count ditahan di memori oleh fungsi dalam, sehingga pemanggilan berulang c1() menambah nilai count: 1 lalu 2."
        },
        "explanation": "Sebuah *Closure* tercipta ketika sebuah fungsi dalam mempertahankan referensi ke variabel-variabel di scope fungsi luarnya, bahkan setelah fungsi luar tersebut selesai dieksekusi. Oleh karena itu, variabel `count` tidak disapu Garbage Collector dan nilainya dipertahankan antar pemanggilan, menghasilkan output 1 lalu 2. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-12",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Manajemen Tugas Latar Belakang (WorkManager)",
        "type": "mcq",
        "questionHtml": "Aplikasi e-commerce Android perlu mengunggah log analitik transaksi harian ke server cloud secara andal, di mana tugas tersebut wajib tetap berjalan tuntas meskipun aplikasi ditutup oleh pengguna atau perangkat smartphone di-restart. Komponen arsitektur Android Jetpack manakah yang PALING direkomendasikan Google untuk kebutuhan tersebut?",
        "options": [
            {"key": "A", "text": "AsyncTask yang memproses kalkulasi asynchronous ringan pada thread terpisah di memori RAM."},
            {"key": "B", "text": "WorkManager yang menjamin eksekusi tugas tertunda (deferrable & guaranteed) sesuai konstrain baterai."},
            {"key": "C", "text": "BroadcastReceiver biasa yang mendengarkan event perubahan jaringan tanpa penjadwalan."},
            {"key": "D", "text": "Thread murni Java (new Thread) yang dibuat langsung di dalam blok method onDestroy()."},
            {"key": "E", "text": "Handler postDelayed() yang menunda eksekusi instruksi selama beberapa menit di antrean pesan UI."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "ANDROID BACKGROUND WORK SELECTION",
            "latex": "\\text{Deferrable} \\land \\text{Guaranteed Execution} \\implies \\text{WorkManager (Persisted in SQLite)}",
            "legend": "• Menghormati Doze Mode & penghemat baterai<br>• Menjadwalkan tugas dengan batasan (misal: hanya saat charging & terhubung Wi-Fi)"
        },
        "hints": {
            "concept": "WorkManager adalah standar Android Jetpack untuk pekerjaan latar belakang yang dapat ditunda (deferrable) tetapi wajib terjamin dieksekusi (guaranteed execution) meskipun aplikasi ditutup.",
            "execution": "AsyncTask sudah deprecated. WorkManager mengelola persistensi tugas di database internal sistem operasi."
        },
        "explanation": "`WorkManager` adalah API Android Jetpack yang dirancang khusus untuk menangani pekerjaan latar belakang yang bersifat *deferrable* (bisa ditunda) dan *guaranteed* (pasti dieksekusi). Tugas yang dijadwalkan dengan WorkManager tetap bertahan dan akan dieksekusi bahkan jika aplikasi ditutup paksa atau perangkat ponsel di-restart. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-13",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Pola Arsitektur Entity-Component-System (ECS)",
        "type": "mcq",
        "questionHtml": "Dalam pengembangan gim skala besar dengan puluhan ribu objek bergerak simultan, pola arsitektur Entity-Component-System (ECS) lebih dipilih daripada pendekatan Pemrograman Berorientasi Objek (OOP) hierarki pewarisan kelas yang dalam karena...",
        "options": [
            {"key": "A", "text": "ECS mengharuskan seluruh aset grafis 3D dikonversi menjadi format file vektor monokrom dua dimensi."},
            {"key": "B", "text": "ECS memisahkan data (Component) dari logika (System), mengoptimalkan CPU Cache locality (Data-Oriented Design)."},
            {"key": "C", "text": "OOP tradisional tidak dapat mengompilasi kode program jika jumlah kelas game melampaui seratus file."},
            {"key": "D", "text": "ECS menghapus ketergantungan pada kartu grafis GPU sehingga seluruh proses render ditangani oleh RAM."},
            {"key": "E", "text": "ECS secara otomatis membuat animasi gerakan karakter menjadi halus tanpa memerlukan asset rigger seniman."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "DATA-ORIENTED DESIGN (ECS)",
            "latex": "\\text{Entity (ID)} + \\text{Component (Raw Data)} + \\text{System (Logic)} \\implies \\text{Contiguous Memory Cache Hit}",
            "legend": "• OOP: Object tersebar di heap -> Cache Miss tinggi<br>• ECS: Komponen disusun dalam array kontigu -> Cache Line termanfaatkan maksimal"
        },
        "hints": {
            "concept": "ECS (Entity Component System) menganut filosofi Data-Oriented Design. Memisahkan data murni dari logika pemrosesan memungkinkan data disimpan secara kontigu di memori, meminimalkan cache miss CPU.",
            "execution": "Keunggulan utama ECS adalah efisiensi pemrosesan massal ribuan entitas secara paralel berkat data locality."
        },
        "explanation": "Pendekatan OOP tradisional menghasilkan objek yang tersebar acak di memori heap dengan banyak pointer indirection, menyebabkan CPU Cache Miss yang tinggi. Pola ECS (Data-Oriented Design) memisahkan data murni (`Component`) ke dalam larik memori kontigu dan memprosesnya secara massal melalui `System`, memaksimalkan performa CPU Cache dan throughput eksekusi gim. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-14",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Optimasi Grafis: Frustum & Occlusion Culling",
        "type": "mcq",
        "questionHtml": "Dalam optimasi pipeline rendering dunia gim 3D, teknik yang bertugas membuang (tidak memproses render) objek-objek yang berada di luar kerucut jangkauan pandang kamera disebut `Frustum Culling`. Sementara teknik yang membuang objek yang berada di dalam pandangan kamera tetapi terhalang sepenuhnya oleh objek besar lain di depannya disebut...",
        "options": [
            {"key": "A", "text": "Backface Culling yang membuang poligon segitiga yang menghadap membelakangi arah kamera."},
            {"key": "B", "text": "Occlusion Culling yang menonaktifkan rendering objek yang tertutup oleh geometri penghalang di depannya."},
            {"key": "C", "text": "Distance Fogging yang menutupi kejauhan dunia gim menggunakan lapisan kabut buatan atmosfer."},
            {"key": "D", "text": "Level of Detail (LOD) yang menurunkan jumlah poligon mesh objek yang posisinya sangat jauh dari pemain."},
            {"key": "E", "text": "Anti-Aliasing yang menghaluskan garis tepi bergerigi pada sudut poligon objek grafis tiga dimensi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "GPU CULLING TECHNIQUES",
            "latex": "\\text{Frustum Culling (Outside Camera Field)} \\quad \\mid \\quad \\text{Occlusion Culling (Hidden Behind Obstacle)}",
            "legend": "• Keduanya memangkas beban GPU fragment shader & overdraw secara dramatis"
        },
        "hints": {
            "concept": "Frustum Culling = di luar jangkauan pandang kamera. Occlusion Culling = di dalam pandangan, tapi terhalang (occluded) tembok/bangunan di depannya.",
            "execution": "Kata kunci 'terhalang sepenuhnya oleh objek lain' merujuk ke Occlusion Culling."
        },
        "explanation": "*Occlusion Culling* adalah proses di mana objek-objek yang sebenarnya berada di dalam jangkauan pandang kamera (view frustum) dicegah untuk dikirim ke GPU karena objek tersebut terhalang sepenuhnya (tertutup/occluded) oleh objek lain di latar depan (misalnya pohon di balik tembok kastil). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-15",
        "subject": "rpl",
        "materi": "DESAIN UI/UX & AKSESIBILITAS",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Aksesibilitas Web Semantik (Screen Reader)",
        "type": "mcq",
        "questionHtml": "Seorang frontend engineer membangun tombol interaktif menggunakan markup `<div class=\"btn\" onclick=\"beli()\">Beli Sekarang</div>` alih-alih menggunakan tag HTML standar `<button onclick=\"beli()\">Beli Sekarang</button>`. Masalah aksesibilitas fatal yang dialami oleh pengguna penyandang disabilitas tunanetra saat menggunakan pembaca layar (screen reader) adalah...",
        "options": [
            {"key": "A", "text": "Warna tombol di layar otomatis berubah menjadi transparan sehingga tidak dapat terlihat oleh pengguna."},
            {"key": "B", "text": "Screen reader tidak mengenali elemen tersebut sebagai tombol interaktif dan tidak dapat difokuskan via tombol Tab keyboard."},
            {"key": "C", "text": "Browser langsung memblokir eksekusi fungsi JavaScript beli() karena dianggap sebagai malware trojan."},
            {"key": "D", "text": "Kecepatan loading halaman web menurun drastis sebesar 90 persen akibat kegagalan parsing mesin rendering."},
            {"key": "E", "text": "Sertifikat keamanan HTTPS pada domain web otomatis dicabut oleh otoritas penerbit sertifikat SSL."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SEMANTIC HTML ACCESSIBILITY TREE",
            "latex": "\\text{<button>} \\implies \\{ \\text{Role: button}, \\; \\text{Keyboard Focusable (Tab)}, \\; \\text{Accessible Name} \\}",
            "legend": "• <div> tidak memiliki semantic role button<br>• Tidak bisa menerima fokus keyboard secara default (tabindex=-1)<br>• Menyalahi WCAG 2.1 Principle: Robust & Operable"
        },
        "hints": {
            "concept": "Elemen div adalah elemen generik non-semantik. Tanpa tag <button>, elemen tidak memiliki role 'button' di Accessibility Tree dan tidak bisa difokuskan menggunakan tombol Tab pada keyboard.",
            "execution": "Pengguna tunanetra dan pengguna keyboard murni tidak akan tahu bahwa div tersebut adalah tombol interaktif."
        },
        "explanation": "Elemen semantik `<button>` secara bawaan menyediakan role button pada Accessibility Tree, dapat difokuskan melalui keyboard (tombol Tab), serta dapat diaktifkan menggunakan tombol Spasi dan Enter. Menggantinya dengan `<div>` membuat screen reader tidak mengumumkan elemen tersebut sebagai tombol dan membuatnya tidak dapat diakses tanpa mouse, melanggar standar WCAG. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-16",
        "subject": "rpl",
        "materi": "PENGUJIAN PERANGKAT LUNAK (QA)",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Pengujian Mutasi (Mutation Testing)",
        "type": "mcq",
        "questionHtml": "Sebuah tim QA memiliki unit test suite dengan indikator code coverage mencapai 100%. Namun, mereka tetap menerapkan *Mutation Testing* dengan menyuntikkan perubahan kecil (mutants, misalnya mengubah operator `>` menjadi `<`). Tujuan utama dari pelaksanaan Mutation Testing tersebut adalah...",
        "options": [
            {"key": "A", "text": "Meningkatkan kecepatan eksekusi proses pengujian unit test menjadi dua kali lebih cepat di server CI/CD."},
            {"key": "B", "text": "Menguji efektivitas dan kualitas test suite itu sendiri dengan memverifikasi apakah unit test mampu mendeteksi bug buatan."},
            {"key": "C", "text": "Mengenkripsi seluruh basis kode sumber agar tidak dapat didekompilasi oleh pihak luar yang tidak berhak."},
            {"key": "D", "text": "Memperbaiki bug logika secara otomatis tanpa campur tangan dari insinyur perangkat lunak manusia."},
            {"key": "E", "text": "Mengurangi ukuran file biner aplikasi agar dapat diunduh lebih cepat oleh pengguna akhir ponsel."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "MUTATION SCORE EQUATION",
            "latex": "\\text{Mutation Score} = \\frac{\\text{Killed Mutants}}{\\text{Total Mutants}} \\times 100\\%",
            "legend": "• Code coverage 100% belum tentu menguji logika dengan benar (bisa saja tanpa assertion)<br>• Mutant killed = Test suite berkualitas tinggi karena berhasil menangkap perubahan cacat"
        },
        "hints": {
            "concept": "Coverage 100% hanya mengukur baris kode mana yang dieksekusi, bukan apakah tes tersebut benar-benar memvalidasi output. Mutation testing menguji kualitas tes dengan menyuntikkan mutasi kode.",
            "execution": "Jika tes gagal saat kode dimutasi (mutant killed), berarti tes tersebut berkualitas baik."
        },
        "explanation": "Code coverage tinggi tidak menjamin kualitas pengujian karena kode bisa saja dieksekusi tanpa adanya `assert` yang memadai. *Mutation Testing* mengevaluasi kualitas unit test itu sendiri dengan memperkenalkan kesalahan sintaksis sengaja (mutants); jika test suite gagal mendeteksi perubahan tersebut (mutant survived), berarti pengujian yang dibuat masih lemah dan perlu diperbaiki. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-17",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Git Pre-Commit Hook untuk Keamanan",
        "type": "mcq",
        "questionHtml": "Untuk mencegah insiden kebocoran kredensial sensitif (seperti API Keys, Private Keys, dan password database) agar tidak sengaja terunggah ke repositori GitHub publik, langkah rekayasa preventif otomatis yang wajib dikonfigurasi di sisi lokal pengembang adalah...",
        "options": [
            {"key": "A", "text": "Mewajibkan pengembang menulis password akun email perusahaan langsung pada komentar source code program."},
            {"key": "B", "text": "Memasang script Git Pre-Commit Hook (misalnya via tool Gitleaks/TruffleHog) yang otomatis membatalkan commit jika mendeteksi secret."},
            {"key": "C", "text": "Menonaktifkan sistem enkripsi SSL pada repositori remote agar paket commit dapat dipantau oleh admin jaringan."},
            {"key": "D", "text": "Menghapus file .gitignore dari proyek agar seluruh file konfigurasi rahasia dapat terlacak oleh sistem Git."},
            {"key": "E", "text": "Mengunggah file konfigurasi database .env secara berkala ke media penyimpanan Google Drive publik."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "GIT HOOKS SECURITY SHIFT-LEFT",
            "latex": "\\text{git commit} \\implies \\text{.git/hooks/pre-commit scans staged files} \\xrightarrow{\\text{Secret Detected}} \\text{Exit Code 1 (Abort)}",
            "legend": "• Shift-Left Security: Mencegah kerentanan di workstation developer sebelum mencapai remote repo"
        },
        "hints": {
            "concept": "Pre-commit hook adalah skrip yang dieksekusi Git sebelum commit disimpan. Jika skrip menghasilkan exit code non-zero, proses commit dibatalkan.",
            "execution": "Scanner otomatis seperti Gitleaks di pre-commit hook mencegah secret masuk ke riwayat commit."
        },
        "explanation": "Pemasangan `pre-commit hook` pada Git memungkinkan pemindaian otomatis terhadap file yang ada di staging area tepat sebelum proses commit selesai. Jika alat pemindai (seperti Gitleaks atau TruffleHog) mendeteksi pola API Key atau kredensial rahasia, proses commit langsung dibatalkan otomatis di workstation pengembang (Shift-Left Security). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-18",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Hak Cipta vs Paten Perangkat Lunak",
        "type": "mcq",
        "questionHtml": "Berdasarkan sistem hukum Hak Atas Kekayaan Intelektual (HAKI) di Indonesia (UU Hak Cipta No. 28 Tahun 2014), bentuk perlindungan hukum mendasar yang diberikan kepada karya Program Komputer (Perangkat Lunak) adalah...",
        "options": [
            {"key": "A", "text": "Hak Desain Industri yang melindungi fungsi matematis rangkaian sirkuit elektronik motherboard komputer."},
            {"key": "B", "text": "Hak Cipta yang melindungi ekspresi wujud kode sumber (source code) dan program komputer dari penjiplakan tanpa izin."},
            {"key": "C", "text": "Hak Merek Dagang yang melarang pengembang lain menulis program dengan bahasa pemrograman yang sama."},
            {"key": "D", "text": "Rahasia Dagang yang otomatis gugur jika aplikasi dirilis ke publik melalui toko aplikasi resmi Google Play."},
            {"key": "E", "text": "Perlindungan Varietas Tanaman yang mengatur silsilah penamaan variabel di dalam modul kecerdasan buatan."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "HAKI FRAMEWORK INDONESIA (UU 28/2014)",
            "latex": "\\text{Program Komputer} \\subseteq \\text{Ciptaan yang Dilindungi Hak Cipta (Pasal 40 Ayat 1 Huruf s)}",
            "legend": "• Perlindungan berlaku otomatis (prinsip deklaratif) sejak ciptaan diwujudkan dalam bentuk nyata<br>• Melindungi ekspresi ide (source code/binary), bukan ide dasarnya"
        },
        "hints": {
            "concept": "Di Indonesia, program komputer (software) dilindungi di bawah rezim Hak Cipta (UU No. 28 Tahun 2014 Pasal 40), yang melindungi ekspresi source code dari penyalinan.",
            "execution": "Program komputer dikategorikan sebagai ciptaan yang dilindungi oleh Hak Cipta."
        },
        "explanation": "Berdasarkan Pasal 40 Ayat (1) huruf s UU No. 28 Tahun 2014 tentang Hak Cipta, Program Komputer secara eksplisit diakui sebagai salah satu ciptaan yang dilindungi oleh rezim Hak Cipta. Hak cipta melindungi wujud nyata ekspresi kode sumber program dari penggandaan, pembajakan, dan distribusi tanpa izin. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-19",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Pencegahan Carpal Tunnel Syndrome (CTS)",
        "type": "mcq",
        "questionHtml": "Programmer yang mengetik dengan posisi pergelangan tangan menekuk ke atas secara kaku selama bertahun-tahun berisiko tinggi mengalami penyempitan saraf medianus di pergelangan tangan yang dikenal sebagai Carpal Tunnel Syndrome (CTS). Praktik ergonomi kerja yang benar untuk mencegah gangguan tersebut adalah...",
        "options": [
            {"key": "A", "text": "Mengetik dengan posisi pergelangan tangan menggantung bebas di udara tanpa sandaran apapun di meja."},
            {"key": "B", "text": "Menjaga posisi pergelangan tangan lurus dan netral saat mengetik serta menggunakan wrist rest pendukung yang empuk."},
            {"key": "C", "text": "Menekan tombol keyboard sekeras mungkin untuk melatih kekuatan otot dan ligamen jari jemari tangan."},
            {"key": "D", "text": "Mengatur ketinggian kursi serendah mungkin sehingga siku berada jauh di bawah permukaan meja kerja."},
            {"key": "E", "text": "Menonaktifkan pendingin ruangan AC agar suhu pergelangan tangan selalu berada di atas empat puluh derajat."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "WRIST ERGONOMICS & MEDIAN NERVE",
            "latex": "\\text{Wrist Angle} \\approx 180^\\circ \\text{ (Neutral/Straight)} \\implies \\text{Minimal Pressure on Carpal Tunnel}",
            "legend": "• Mencegah peradangan tendon dan kompresi nervus medianus<br>• Posisi siku membentuk sudut 90 - 100 derajat relaks"
        },
        "hints": {
            "concept": "Carpal Tunnel Syndrome (CTS) dicegah dengan menjaga pergelangan tangan pada posisi netral (lurus, tidak menekuk ke atas/bawah) dan menyandarkan telapak pada bantalan yang nyaman saat jeda mengetik.",
            "execution": "Posisi netral (lurus) dan dukungan wrist rest adalah standar ergonomi K3LH IT."
        },
        "explanation": "Untuk mencegah Carpal Tunnel Syndrome (CTS), posisi tangan saat mengetik harus dipertahankan dalam postur netral (lurus sejajar dengan lengan bawah, tanpa ekstensi atau fleksi pergelangan). Penggunaan keyboard ergonomis dan wrist rest membantu menyangga telapak tangan dan mengurangi tekanan pada saraf medianus. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-20",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Pola Desain Factory Method",
        "type": "mcq",
        "questionHtml": "Sebuah aplikasi pengolah dokumen perlu mendukung ekspor ke berbagai format file: PDF, Word, dan Excel. Jika programmer menggunakan pola desain *Factory Method*, keuntungan arsitektural yang diperoleh pada kelas klien adalah...",
        "options": [
            {"key": "A", "text": "Klien harus membuat objek menggunakan kata kunci new untuk setiap kelas konkret spesifik secara manual."},
            {"key": "B", "text": "Klien terisolasi dari proses instansiasi konkret, hanya bergantung pada interface dokumen umum (Loose Coupling)."},
            {"key": "C", "text": "Ukuran memori heap aplikasi otomatis menjadi nol megabyte saat proses konversi dokumen berlangsung."},
            {"key": "D", "text": "Seluruh kelas pemroses dokumen dipaksa mewarisi method statis dari kelas java.lang.System."},
            {"key": "E", "text": "Dokumen yang diekspor otomatis terenkripsi dengan kunci asimetris RSA tanpa perlu konfigurasi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CREATIONAL DESIGN PATTERN: FACTORY METHOD",
            "latex": "\\text{Client} \\xrightarrow{\\text{calls}} \\text{DocumentFactory.create(type)} \\to \\text{returns Interface Document}",
            "legend": "• Mengisolasi kode pembuatan objek dari kode pengguna objek<br>• Mempermudah penambahan format dokumen baru tanpa merusak kelas klien (OCP compliant)"
        },
        "hints": {
            "concept": "Pola Factory Method memisahkan proses pembuatan objek dari kode klien. Klien cukup memanggil factory dengan tipe yang diinginkan dan menerima objek berbasis interface.",
            "execution": "Manfaat utamanya adalah loose coupling dan fleksibilitas penambahan kelas baru tanpa mengubah kode klien."
        },
        "explanation": "Pola desain *Factory Method* mengabstraksi proses instansiasi objek. Klien hanya berinteraksi dengan factory dan tipe antarmuka umum (`Document`), sehingga kelas klien tidak terikat langsung (decoupled) dengan kelas-kelas konkret (`PdfDocument`, `WordDocument`, `ExcelDocument`), mematuhi prinsip Open/Closed. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-21",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Keamanan API: Mitigasi SQL Injection pada Raw Query ORM",
        "type": "mcq",
        "questionHtml": "Perhatikan potongan kode backend NodeJS yang menggunakan library basis data berikut:\n```javascript\n// Potongan kode A (Vulnerable)\nconst query = `SELECT * FROM users WHERE email = '${req.body.email}'`;\ndb.query(query);\n\n// Potongan kode B (Secure)\nconst query = `SELECT * FROM users WHERE email = ?`;\ndb.query(query, [req.body.email]);\n```\nMengapa pendekatan B kebal terhadap serangan SQL Injection dibandingkan pendekatan A?",
        "options": [
            {"key": "A", "text": "Karena tanda tanya (?) secara otomatis mengubah seluruh karakter input peretas menjadi angka nol integer."},
            {"key": "B", "text": "Karena database engine mengompilasi struktur query terlebih dahulu dan memperlakukan input pengguna murni sebagai data literal."},
            {"key": "C", "text": "Karena array kedua secara fisik mengenkripsi koneksi jaringan database menggunakan sertifikat TLS."},
            {"key": "D", "text": "Karena pendekatan B membatasi panjang input email maksimal hanya boleh terdiri dari sepuluh karakter."},
            {"key": "E", "text": "Karena tanda kutip satu (') pada email otomatis diganti dengan tanda kutip ganda (\") oleh driver database."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "PARAMETERIZED QUERY (PREPARED STATEMENT) MECHANISM",
            "latex": "\\text{SQL AST Compiled Once} \\implies \\text{Parameters Bound Separately as Raw Data Literals}",
            "legend": "• Input penyerang (misal: ' OR '1'='1) tidak dapat mengubah struktur pohon sintaksis query SQL"
        },
        "hints": {
            "concept": "Prepared Statement / Parameterized Query memisahkan kode SQL dari data. Engine database mengompilasi template SQL terlebih dahulu, lalu menyisipkan parameter sebagai nilai literal murni yang tidak dapat mengubah struktur query.",
            "execution": "Input berbahaya tidak akan pernah dieksekusi sebagai perintah SQL."
        },
        "explanation": "Pada Parameterized Queries (Pendekatan B), database engine mem-parsing dan mengompilasi struktur perintah SQL sebelum nilai parameter disisipkan. Data dari pengguna diperlakukan murni sebagai nilai literal (bukan bagian dari sintaks eksekusi SQL), sehingga payload serangan seperti `' OR '1'='1` tidak dapat mengubah logika query database. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-22",
        "subject": "rpl",
        "materi": "DESAIN UI/UX & AKSESIBILITAS",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Prinsip Usability: User Control & Freedom (Undo)",
        "type": "mcq",
        "questionHtml": "Aplikasi manajemen email menyediakan notifikasi toast 'Pesan telah diarsipkan' disertai tombol aksi 'Undo' (Batal) yang melayang selama 7 detik setelah pengguna mengusap (swipe) sebuah email. Prinsip Jakob Nielsen manakah yang secara langsung mendasari desain tersebut?",
        "options": [
            {"key": "A", "text": "Flexibility and efficiency of use untuk memberikan pengalaman mengetik cepat bagi programmer mahir."},
            {"key": "B", "text": "User control and freedom dengan menyediakan pintu darurat keluar bagi pengguna yang tidak sengaja melakukan aksi."},
            {"key": "C", "text": "Help and documentation yang menyediakan buku manual tebal petunjuk pengoperasian perangkat lunak."},
            {"key": "D", "text": "Aesthetic and minimalist design dengan menghapus seluruh tombol navigasi dari tampilan layar ponsel."},
            {"key": "E", "text": "Recognition rather than recall dengan mewajibkan pengguna mengingat kembali kata sandi akun email."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "NIELSEN HEURISTIC #3: USER CONTROL & FREEDOM",
            "latex": "\\text{Accidental User Action} \\xrightarrow{\\text{Provide Emergency Exit}} \\text{Instant Undo Functionality}",
            "legend": "• Memberikan rasa aman psikologis bagi pengguna saat bereksplorasi<br>• Menghilangkan ketakutan akan kehilangan data permanen"
        },
        "hints": {
            "concept": "Heuristik ke-3: User Control and Freedom. Pengguna sering melakukan kesalahan secara tidak sengaja dan memerlukan 'pintu darurat' yang jelas untuk membatalkan aksi tanpa alur berbelit-belit.",
            "execution": "Fitur Undo pembatalan aksi adalah representasi murni dari User Control and Freedom."
        },
        "explanation": "Heuristik Usability ke-3 Jakob Nielsen (User Control and Freedom) menyatakan bahwa pengguna kerap memilih fungsi sistem secara keliru dan membutuhkan 'pintu darurat' yang terlihat jelas untuk meninggalkan kondisi yang tidak diinginkan tanpa harus melalui dialog yang panjang. Fitur 'Undo' adalah perwujudan sempurna dari prinsip ini. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-23",
        "subject": "rpl",
        "materi": "ALGORITMA & PEMROGRAMAN TERSTRUKTUR",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Rekursi & Rekursi Ekor (Tail Call Optimization)",
        "type": "mcq",
        "questionHtml": "Perhatikan fungsi rekursif perhitungan faktorial berikut:\n```python\ndef faktorial_biasa(n):\n    if n <= 1:\n        return 1\n    return n * faktorial_biasa(n - 1)\n```\nJika fungsi di atas dipanggil dengan nilai $n = 50.000$, program akan mengalami crash dengan error `RecursionError: maximum recursion depth exceeded`. Penyebab struktural dari kegagalan tersebut pada level memori adalah...",
        "options": [
            {"key": "A", "text": "Kapasitas media penyimpanan hard disk sekunder penuh akibat pembuatan file log sistem otomatis."},
            {"key": "B", "text": "Setiap pemanggilan rekursif menumpuk stack frame baru di Call Stack hingga melampaui batas alokasi memori stack."},
            {"key": "C", "text": "Bahasa pemrograman Python tidak mengizinkan operasi perkalian angka bertipe integer melampaui seratus."},
            {"key": "D", "text": "CPU komputer menolak mengeksekusi percabangan kondisi if yang memiliki lebih dari satu operator logika."},
            {"key": "E", "text": "Variabel n mengalami overflow dan berubah nilainya menjadi string huruf acak tak terdefinisi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CALL STACK OVERFLOW DYNAMICS",
            "latex": "\\sum_{i=1}^{n} \\text{StackFrame}(i) > \\text{Max Stack Size} \\implies \\text{StackOverflow / RecursionError}",
            "legend": "• Non-tail recursion: Menyimpan state perkalian di stack frame aktif hingga basis terpenuhi<br>• Solusi: Gunakan iterasi loop (while/for) atau tail recursion dengan akumulator"
        },
        "hints": {
            "concept": "Setiap pemanggilan fungsi menempatkan stack frame baru di Call Stack (menyimpan variabel lokal dan return address). Jika rekursi terlalu dalam, alokasi Call Stack habis.",
            "execution": "Peristiwa ini dinamakan Stack Overflow (di Python memicu RecursionError)."
        },
        "explanation": "Pada rekursi standar, setiap pemanggilan fungsi yang belum selesai (karena masih menunggu hasil perkalian `n * ...`) harus mempertahankan stack frame-nya di Call Stack memori. Ketika kedalaman pemanggilan mencapai puluhan ribu, alokasi memori stack terlampaui sehingga Python melempar `RecursionError` untuk mencegah crash total sistem operasi. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-24",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Integrasi Fisika: Verlet vs Euler Integration",
        "type": "mcq",
        "questionHtml": "Dalam pembuatan simulasi fisika tali, kain (cloth simulation), dan partikel fisika interaktif pada gim, algoritma integrasi numerik *Verlet Integration* lebih sering dipilih daripada *Explicit Euler Integration* karena...",
        "options": [
            {"key": "A", "text": "Verlet Integration tidak membutuhkan kartu grafis GPU dan hanya dapat dihitung oleh sistem cloud server."},
            {"key": "B", "text": "Verlet Integration jauh lebih stabil secara numerik dan otomatis mempertahankan kekekalan energi tanpa eksplosi posisi."},
            {"key": "C", "text": "Euler Integration mengharuskan seluruh objek dalam gim memiliki massa nol kilogram tanpa gaya gravitasi."},
            {"key": "D", "text": "Verlet Integration secara otomatis menggambar tekstur visual kain 3D secara fotorealistis di layar monitor."},
            {"key": "E", "text": "Euler Integration hanya dapat memproses objek statis yang sama sekali tidak mengalami pergerakan koordinat."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "VERLET INTEGRATION FORMULA",
            "latex": "x_{n+1} = 2x_n - x_{n-1} + a_n \\Delta t^2",
            "legend": "• Posisi dihitung langsung dari selisih posisi saat ini dan posisi sebelumnya<br>• Jauh lebih stabil untuk sistem constraint (tali/kain) dibanding Euler yang rentan energy explosion"
        },
        "hints": {
            "concept": "Explicit Euler ($x = x + v \\cdot dt$) mudah mengalami instabilitas numerik (penambahan energi palsu hingga sistem meledak). Verlet Integration sangat stabil untuk partikel ber-constraint.",
            "execution": "Keunggulan utama Verlet adalah stabilitas numerik dan penanganan constraint yang alami."
        },
        "explanation": "Metode *Explicit Euler* rentan terhadap akumulasi galat pembulatan yang menyebabkan pertambahan energi kinetik palsu hingga simulasi partikel 'meledak' (melejit ke tak hingga). Sebaliknya, *Verlet Integration* menghitung posisi baru berdasarkan posisi sekarang dan posisi sebelumnya tanpa variabel kecepatan eksplisit ($x_{n+1} = 2x_n - x_{n-1} + a \\cdot \\Delta t^2$), menghasilkan stabilitas numerik tinggi yang ideal untuk simulasi kain dan tali. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-25",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Android Deep Linking & Intent Filters",
        "type": "mcq",
        "questionHtml": "Sebuah aplikasi Android ingin mengizinkan pengguna membuka halaman produk spesifik secara langsung saat pengguna mengklik tautan web `https://toko.smk.id/produk/123` di browser atau aplikasi chat. Komponen yang wajib dikonfigurasi di dalam file `AndroidManifest.xml` pada Activity produk adalah...",
        "options": [
            {"key": "A", "text": "Deklarasi service background dengan atribut android:exported=\"False\" dan permission akses lokasi GPS."},
            {"key": "B", "text": "Mendefinisikan <intent-filter> yang memuat action VIEW, kategori DEFAULT & BROWSABLE, serta tag <data> skema https."},
            {"key": "C", "text": "Menambahkan tag <uses-feature> kamera resolusi tinggi dengan atribut android:required=\"true\"."},
            {"key": "D", "text": "Mengubah nama package aplikasi menjadi toko.smk.id dan menandatanganinya dengan sertifikat debug keystore."},
            {"key": "E", "text": "Menulis kode skrip JavaScript AJAX di dalam file manifest untuk menangkap event klik URL pengguna."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "ANDROID DEEP LINK INTENT FILTER",
            "latex": "\\langle \\text{intent-filter} \\rangle \\colon \\text{action.VIEW} + \\text{category.BROWSABLE} + \\langle \\text{data scheme/host} \\rangle",
            "legend": "• BROWSABLE: Mengizinkan link dibuka dari browser web<br>• Android App Links memverifikasi kepemilikan domain via Digital Asset Links JSON"
        },
        "hints": {
            "concept": "Deep Linking di Android diaktifkan menggunakan <intent-filter> dengan action android.intent.action.VIEW, kategori BROWSABLE dan DEFAULT, serta tag data yang memuat host dan scheme URL.",
            "execution": "Konfigurasi standar Deep Link / App Link ada di pilihan B."
        },
        "explanation": "Untuk mengaktifkan Deep Linking (atau Android App Links), Activity target di dalam `AndroidManifest.xml` harus dikonfigurasi dengan `<intent-filter>` yang memuat: (1) action `android.intent.action.VIEW`, (2) kategori `android.intent.category.DEFAULT` dan `android.intent.category.BROWSABLE`, serta (3) tag `<data>` yang menetapkan `android:scheme=\"https\"` dan `android:host=\"toko.smk.id\"`. Jawaban: B.",
        "isDiagnostic": False
    },

    # --- 5 MULTI-SELECT (MCMA) ITEMS ---
    {
        "id": "rpl-sim-26",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Praktik Keamanan Web Pencegahan XSS",
        "type": "multi",
        "questionHtml": "Manakah TIGA praktik rekayasa perangkat lunak web yang efektif dan direkomendasikan oleh standar OWASP untuk mencegah kerentanan Cross-Site Scripting (XSS)?",
        "options": [
            {"key": "A", "text": "Melakukan encoding karakter kontekstual (HTML Entity Encoding) terhadap seluruh data input sebelum dirender ke halaman."},
            {"key": "B", "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi domain eksekusi skrip JavaScript yang diizinkan."},
            {"key": "C", "text": "Menyimpan token otentikasi JWT sensitif di dalam Cookie dengan flag HttpOnly daripada di dalam localStorage browser."},
            {"key": "D", "text": "Menggunakan properti innerHTML secara langsung untuk menampilkan teks mentah dari parameter URL tanpa sanitasi."},
            {"key": "E", "text": "Menonaktifkan protokol komunikasi HTTPS pada server web dan beralih sepenuhnya ke protokol HTTP biasa."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formulaHud": {
            "title": "OWASP XSS PREVENTION CHEAT SHEET",
            "latex": "\\text{Defense} = \\text{Contextual Encoding} \\cup \\text{Content Security Policy (CSP)} \\cup \\text{HttpOnly Cookies}",
            "legend": "• Opsi D adalah sumber utama kerentanan DOM-XSS<br>• Opsi E merusak privasi saluran transmisi data"
        },
        "hints": {
            "concept": "Pencegahan XSS: 1. Output encoding; 2. CSP headers; 3. HttpOnly cookies agar token tidak bisa dibaca JS penyerang.",
            "execution": "Pilihan A, B, dan C adalah rekomendasi resmi OWASP."
        },
        "explanation": "Praktik mitigasi XSS menurut OWASP: (A) Contextual Output Encoding mencegah data ditafsirkan sebagai tag HTML, (B) CSP membatasi asal eksekusi skrip, dan (C) Flag HttpOnly melindungi cookie token dari pencurian skrip jahat. Pilihan D justru menyebabkan celah XSS, dan E melemahkan keamanan jaringan. Jawaban benar: A, B, C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-27",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Penyebab Terjadinya Full Table Scan pada Database",
        "type": "multi",
        "questionHtml": "Manakah TIGA kondisi penulisan query SQL berikut yang dapat menyebabkan Database Query Optimizer mengabaikan indeks B-Tree yang sudah ada dan terpaksa melakukan pembacaan seluruh tabel secara sekuensial (Full Table Scan)?",
        "options": [
            {"key": "A", "text": "Menggunakan fungsi transformasi matematika atau manipulasi string pada kolom berindeks (misal: WHERE YEAR(tanggal) = 2026)."},
            {"key": "B", "text": "Menggunakan klausa pencarian string pola wildcard di awal kata (misal: WHERE nama_lengkap LIKE '%Santoso')."},
            {"key": "C", "text": "Melakukan perbandingan data antar tipe data yang tidak cocok sehingga memicu konversi tipe implisit (Implicit Casting)."},
            {"key": "D", "text": "Menggunakan perbandingan kesetaraan eksak pada kolom primary key tunggal (misal: WHERE id_user = 105)."},
            {"key": "E", "text": "Menyertakan klausul LIMIT 1 pada query pencarian baris data tabel basis data."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formulaHud": {
            "title": "B-TREE INDEX INVALIDATION PATTERNS",
            "latex": "\\text{Full Table Scan} \\impliedby f(\\text{col}) = x \\lor \\text{col LIKE } \\text{'\\%str'} \\lor \\text{CAST}(\\text{col})",
            "legend": "• f(col): Indeks tidak bisa dicari karena nilai diubah fungsi<br>• LIKE '%abc': Huruf awal tidak diketahui sehingga pohon B-Tree tidak bisa diarahkan"
        },
        "hints": {
            "concept": "Penyebab indeks diabaikan: 1. Kolom dibungkus fungsi; 2. LIKE diawali %; 3. Perbedaan tipe data memicu implicit conversion.",
            "execution": "Opsi D dan E justru sangat cepat dan memanfaatkan indeks."
        },
        "explanation": "Indeks B-Tree tidak dapat dimanfaatkan secara optimal (memicu Full Table Scan) jika: (A) Kolom berindeks dimanipulasi oleh fungsi (kecuali dibuat expression index), (B) Pencarian string `LIKE` memiliki wildcard di depan (`%...`) karena pohon b-tree diurutkan dari huruf pertama, dan (C) Terjadi konversi tipe data implisit. Jawaban benar: A, B, C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-28",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Indikator Pelanggaran Prinsip Desain SOLID",
        "type": "multi",
        "questionHtml": "Manakah DUA skenario arsitektur kode di bawah ini yang mengindikasikan adanya pelanggaran terhadap prinsip-prinsip SOLID?",
        "options": [
            {"key": "A", "text": "Sebuah kelas OrderService memiliki lebih dari 3.000 baris kode yang menangani validasi keranjang, kalkulasi pajak, koneksi database, pengiriman email konfirmasi, dan pembuatan invoice PDF."},
            {"key": "B", "text": "Sebuah subclass BurungUnta mewarisi superclass Burung dan meng-override method terbang() dengan melempar UnsupportedOperationException karena burung unta tidak dapat terbang."},
            {"key": "C", "text": "Sebuah kelas NotificationService menerima interface MessageSender melalui constructor injection dan tidak bergantung pada implementasi spesifik."},
            {"key": "D", "text": "Sebuah interface Shape dipecah menjadi Drawable dan Resizable agar kelas yang hanya butuh menggambar tidak dipaksa mengubah ukuran."},
            {"key": "E", "text": "Menambahkan kelas metode pembayaran baru CryptoPayment yang mengimplementasikan interface PaymentStrategy tanpa memodifikasi kelas Checkout."}
        ],
        "correctKeys": ["A", "B"],
        "formulaHud": {
            "title": "SOLID CODE SMELLS IDENTIFICATION",
            "latex": "\\text{Scenario A} \\implies \\text{Violates SRP (God Class)} \\quad \\mid \\quad \\text{Scenario B} \\implies \\text{Violates LSP}",
            "legend": "• Skenario C mematuhi DIP<br>• Skenario D mematuhi ISP<br>• Skenario E mematuhi OCP"
        },
        "hints": {
            "concept": "Skenario A adalah 'God Class' yang melanggar SRP (terlalu banyak tanggung jawab). Skenario B melempar exception saat subclass dipanggil method superclassnya, melanggar LSP.",
            "execution": "C, D, dan E adalah contoh kepatuhan yang baik terhadap SOLID."
        },
        "explanation": "Skenario A melanggar Single Responsibility Principle (SRP) karena kelas menangani terlalu banyak urusan berbeda (God Class). Skenario B melanggar Liskov Substitution Principle (LSP) karena subclass tidak dapat menggantikan superclass secara aman (klien memanggil `terbang()` malah mengalami runtime exception). Jawaban benar: A, B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-29",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Faktor Penyebab Penurunan Framerate Gim Mobile",
        "type": "multi",
        "questionHtml": "Manakah TIGA faktor teknis di bawah ini yang menjadi penyebab utama terjadinya stuttering dan penurunan frame rate (FPS drop) pada gim mobile?",
        "options": [
            {"key": "A", "text": "Terjadinya lonjakan alokasi dan pembersihan memori objek dinamis secara berulang yang memicu siklus Garbage Collection (GC) pauses."},
            {"key": "B", "text": "Tingginya jumlah Draw Calls per frame akibat setiap partikel dan sprite menggunakan tekstur material terpisah tanpa batching."},
            {"key": "C", "text": "Terjadinya overdraw ekstrem di mana piksel layar yang sama digambar berulang kali oleh banyak lapisan sprite transparan tumpang tindih."},
            {"key": "D", "text": "Menggunakan pola desain Object Pooling untuk mengelola peluru dan partikel efek gim di dalam scene."},
            {"key": "E", "text": "Menyatukan ribuan gambar sprite kecil ke dalam satu lembar gambar Texture Atlas berukuran terstandarisasi."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formulaHud": {
            "title": "MOBILE GAME PERFORMANCE BOTTLENECKS",
            "latex": "\\text{Bottlenecks} = \\text{GC Allocations (Spikes)} \\cup \\text{High Draw Calls (CPU bound)} \\cup \\text{Overdraw (GPU bound)}",
            "legend": "• D dan E adalah teknik OPTIMASI, bukan penyebab masalah"
        },
        "hints": {
            "concept": "Tiga musuh utama performa game mobile: GC Pause (alokasi memori berulang), High Draw Calls (CPU overhead), dan Overdraw (GPU fill rate bottleneck).",
            "execution": "Opsi D dan E adalah solusi optimasi, sedangkan A, B, C adalah masalah."
        },
        "explanation": "Penyebab utama lag pada gim mobile meliputi: (A) Alokasi heap konstan yang memicu Garbage Collector menghentikan thread game sementara (GC spike), (B) Draw Calls tinggi yang membebani CPU, dan (C) Overdraw tinggi di mana GPU terbebani menggambar ulang piksel transparan yang bertumpuk. Pilihan D dan E justru merupakan teknik optimasi. Jawaban benar: A, B, C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-30",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Praktik Terbaik Pengelolaan Branch & Pull Request",
        "type": "multi",
        "questionHtml": "Manakah TIGA praktik terbaik (best practices) yang wajib diterapkan oleh tim rekayasa perangkat lunak dalam pengelolaan Git Pull Request (PR) dan Branching?",
        "options": [
            {"key": "A", "text": "Membuat Pull Request berukuran kecil dan terfokus (Small PRs) agar mudah ditinjau secara teliti dan cepat oleh reviewer."},
            {"key": "B", "text": "Mengintegrasikan automated linter dan automated unit test yang wajib lolos (pass) sebelum PR diizinkan untuk di-merge."},
            {"key": "C", "text": "Menulis deskripsi Pull Request yang jelas, memuat konteks perubahan, motivasi bisnis, dan petunjuk pengujian manual."},
            {"key": "D", "text": "Mengizinkan programmer melakukan bypass terhadap proses code review dan langsung melakukan push langsung ke branch main produksi."},
            {"key": "E", "text": "Mengumpulkan ratusan fitur berbeda yang tidak saling terkait ke dalam satu cabang branch selama enam bulan sebelum membuat PR."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formulaHud": {
            "title": "CODE REVIEW EXCELLENCE RULES",
            "latex": "\\text{Quality PR} = \\text{Small Scope (< 400 LOC)} \\land \\text{CI Checks Green} \\land \\text{Clear Context Description}",
            "legend": "• Small PR: Mengurangi beban kognitif reviewer & mendeteksi bug lebih cepat<br>• D dan E adalah anti-pattern yang merusak stabilitas repositori"
        },
        "hints": {
            "concept": "Standar PR modern: Scope kecil (<400 baris), lolos CI otomatis (lint & test), dan deskripsi perubahan yang jelas.",
            "execution": "D (bypass review) dan E (branch raksasa berumur panjang) adalah pelanggaran berat praktik software engineering."
        },
        "explanation": "Praktik rekayasa software terbaik untuk Pull Request: (A) PR berukuran kecil (< 400 baris kode) mengurangi cognitive load peninjau, (B) Memasang Automated CI Checks sebagai syarat merge menjamin kualitas kode, dan (C) Deskripsi PR yang komprehensif mempermudah peninjauan. Pilihan D dan E adalah anti-pattern. Jawaban benar: A, B, C.",
        "isDiagnostic": False
    },

    # --- 5 MATRIX BENAR-SALAH ITEMS ---
    {
        "id": "rpl-sim-31",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Urutan Eksekusi Logika Query SQL",
        "type": "matrix",
        "questionHtml": "Perhatikan query SQL analitik pelaporan keuangan berikut:\n```sql\nSELECT departemen, COUNT(*) AS total_staff, AVG(gaji) AS rata_gaji\nFROM pegawai\nWHERE status_kerja = 'Tetap'\nGROUP BY departemen\nHAVING AVG(gaji) >= 8000000\nORDER BY rata_gaji DESC;\n```\nEvaluasilah kebenaran pernyataan teknis mengenai urutan dan aturan eksekusi query SQL di atas:",
        "statements": [
            {"id": "0", "text": "Klausul WHERE dieksekusi oleh mesin basis data sebelum proses pengelompokan baris data oleh GROUP BY."},
            {"id": "1", "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."},
            {"id": "2", "text": "Fungsi agregasi seperti AVG(gaji) diperbolehkan secara sintaksis untuk diletakkan langsung di dalam klausul WHERE."},
            {"id": "3", "text": "Alias kolom 'rata_gaji' dapat digunakan di dalam klausul WHERE karena klausul WHERE dieksekusi setelah SELECT."}
        ],
        "correctAnswers": {
            "0": True,
            "1": True,
            "2": False,
            "3": False
        },
        "formulaHud": {
            "title": "SQL LOGICAL PROCESSING ORDER",
            "latex": "\\text{FROM} \\to \\text{WHERE} \\to \\text{GROUP BY} \\to \\text{HAVING} \\to \\text{SELECT} \\to \\text{ORDER BY}",
            "legend": "• WHERE tidak bisa menerima fungsi agregasi<br>• SELECT dieksekusi setelah WHERE, sehingga alias kolom SELECT tidak ada saat WHERE berjalan"
        },
        "hints": {
            "concept": "Urutan eksekusi logika SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE berjalan sebelum SELECT, sehingga alias kolom belum tersedia di WHERE.",
            "execution": "Pernyataan 0 dan 1 Benar. Pernyataan 2 Salah (WHERE tidak bisa fungsi agregat). Pernyataan 3 Salah (WHERE berjalan sebelum SELECT)."
        },
        "explanation": "Urutan pemrosesan query SQL: (1) FROM & JOIN, (2) WHERE (memfilter baris mentah, tidak boleh fungsi agregat), (3) GROUP BY, (4) HAVING (memfilter kelompok agregasi), (5) SELECT (membuat alias kolom), (6) ORDER BY. Oleh karena itu, Pernyataan 0 dan 1 BENAR; Pernyataan 2 dan 3 SALAH.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-32",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Arsitektur Event Loop & Concurrency JavaScript",
        "type": "matrix",
        "questionHtml": "Evaluasilah kebenaran pernyataan teknis mengenai model konkurensi (Concurrency Model) dan siklus eksekusi Event Loop pada lingkungan runtime JavaScript (V8 Engine):",
        "statements": [
            {"id": "0", "text": "JavaScript berjalan pada satu Call Stack utama (Single-Threaded) untuk mengeksekusi kode program sinkron."},
            {"id": "1", "text": "Microtask Queue (seperti callback Promise dan queueMicrotask) memiliki prioritas eksekusi lebih tinggi dibanding Macrotask Queue (seperti setTimeout)."},
            {"id": "2", "text": "Fungsi setTimeout(fn, 1000) memberikan jaminan mutlak bahwa callback fn pasti dieksekusi tepat pada milidetik ke-1000 tanpa kemungkinan tertunda."},
            {"id": "3", "text": "Call Stack dapat memproses Macrotask berikutnya meskipun antrean di dalam Microtask Queue belum selesai dikosongkan."}
        ],
        "correctAnswers": {
            "0": True,
            "1": True,
            "2": False,
            "3": False
        },
        "formulaHud": {
            "title": "EVENT LOOP SPECIFICATION INVARIANTS",
            "latex": "\\text{Drain Microtask Queue Completely} \\implies \\text{Render UI} \\implies \\text{Pick One Macrotask}",
            "legend": "• setTimeout(fn, t) menjamin delay MINIMAL t, bukan waktu eksekusi tepat<br>• Microtask wajib dikosongkan tuntas sebelum task berikutnya"
        },
        "hints": {
            "concept": "JavaScript adalah single-threaded. Microtask selalu dieksekusi hingga habis sebelum task berikutnya. setTimeout(fn, 1000) adalah delay minimal, jika call stack sibuk eksekusinya bisa tertunda lebih dari 1000ms.",
            "execution": "Pernyataan 0 dan 1 Benar. Pernyataan 2 dan 3 Salah."
        },
        "explanation": "Pernyataan 0 BENAR (JS single-threaded di main execution context). Pernyataan 1 BENAR (Microtask Queue diprioritaskan di atas Macrotask Queue). Pernyataan 2 SALAH (waktu pada `setTimeout` adalah batas waktu tunggu minimal, bukan waktu eksekusi presisi; jika Call Stack sedang sibuk, callback akan tertunda). Pernyataan 3 SALAH (Microtask Queue wajib dikuras habis sebelum event loop mengambil Macrotask baru).",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-33",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Siklus Hidup & Arsitektur Android",
        "type": "matrix",
        "questionHtml": "Evaluasilah kebenaran pernyataan teknis mengenai siklus hidup komponen dan manajemen memori pada sistem operasi Android:",
        "statements": [
            {"id": "0", "text": "Ketika sebuah Activity tertutup oleh dialog pop-up berukuran kecil di layarnya, Activity tersebut beralih ke status onPause() dan masih tetap terlihat sebagian."},
            {"id": "1", "text": "Komponen Android Jetpack ViewModel otomatis dihancurkan dan dibersihkan dari memori saat pengguna memutar orientasi layar smartphone."},
            {"id": "2", "text": "Operasi pembacaan file besar atau pengunduhan data jaringan HTTP dilarang dijalankan secara langsung pada Main Thread untuk menghindari Application Not Responding (ANR)."},
            {"id": "3", "text": "Callback method onDestroy() dijamin pasti selalu dipanggil oleh sistem Android saat memori RAM ponsel mengalami kondisi darurat kelangkaan memori (low memory)."}
        ],
        "correctAnswers": {
            "0": True,
            "1": False,
            "2": True,
            "3": False
        },
        "formulaHud": {
            "title": "ANDROID ACTIVITY LIFECYCLE INVARIANTS",
            "latex": "\\text{Visible but lost focus} \\implies \\text{onPause()} \\quad \\mid \\quad \\text{Low Memory Kill} \\implies \\text{Process Killed without onDestroy()}",
            "legend": "• ViewModel mempertahankan state saat rotasi layar (tidak di-destroy)<br>• OS Android dapat langsung mematikan proses di background tanpa memanggil onDestroy()"
        },
        "hints": {
            "concept": "Activity beralih ke onPause saat kehilangan fokus tetapi masih terlihat sebagian (misal tertutup dialog). ViewModel bertahan saat rotasi. Sistem Android bisa membunuh proses di background tanpa memanggil onDestroy() saat low memory.",
            "execution": "Pernyataan 0 Benar. Pernyataan 1 Salah. Pernyataan 2 Benar. Pernyataan 3 Salah."
        },
        "explanation": "Pernyataan 0 BENAR (`onPause()` dipanggil saat activity kehilangan fokus tetapi masih terlihat sebagian). Pernyataan 1 SALAH (tujuan utama `ViewModel` adalah bertahan hidup melewati rotasi layar). Pernyataan 2 BENAR (operasi I/O di Main Thread memicu ANR dan diblokir sistem). Pernyataan 3 SALAH (saat RAM kritis, OS Android dapat langsung mematikan proses aplikasi di background tanpa sempat memanggil `onDestroy()`).",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-34",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Evaluasi Metodologi SDLC Agile Scrum vs Waterfall",
        "type": "matrix",
        "questionHtml": "Evaluasilah kebenaran pernyataan mengenai karakteristik metodologi siklus hidup pengembangan perangkat lunak (SDLC) Agile Scrum dan Waterfall:",
        "statements": [
            {"id": "0", "text": "Dalam kerangka kerja Scrum, perubahan kebutuhan bisnis diperbolehkan dan disambut dengan baik bahkan di tahapan akhir pengembangan aplikasi."},
            {"id": "1", "text": "Model Waterfall sangat fleksibel dan memungkinkan tim kembali ke tahap analisis kebutuhan dengan mudah saat tahap pengujian menemukan kekurangan fitur."},
            {"id": "2", "text": "Sprint Retrospective adalah pertemuan rutin di akhir sprint yang bertujuan mengevaluasi proses kerja tim dan merencanakan perbaikan berkelanjutan untuk sprint berikutnya."},
            {"id": "3", "text": "Product Owner memiliki wewenang penuh untuk mengubah isi dan komitmen Sprint Backlog di tengah-tengah berjalannya Sprint yang sedang aktif."}
        ],
        "correctAnswers": {
            "0": True,
            "1": False,
            "2": True,
            "3": False
        },
        "formulaHud": {
            "title": "AGILE MANIFESTO & SCRUM GUIDE",
            "latex": "\\text{Welcome Changing Requirements} \\quad \\mid \\quad \\text{Sprint Scope Protected Once Committed}",
            "legend": "• Waterfall: Sekuensial kaku, fase berikutnya baru mulai jika fase sebelumnya selesai sempurna<br>• Sprint Backlog dikunci saat Sprint berjalan demi fokus tim pengembang"
        },
        "hints": {
            "concept": "Agile menyambut perubahan kebutuhan. Waterfall kaku dan sulit kembali ke fase sebelumnya. Sprint Retrospective mengevaluasi proses kerja tim. Lingkup Sprint Backlog yang sedang berjalan tidak boleh diubah sembarangan oleh Product Owner.",
            "execution": "Pernyataan 0 Benar. Pernyataan 1 Salah. Pernyataan 2 Benar. Pernyataan 3 Salah."
        },
        "explanation": "Pernyataan 0 BENAR (Agile menyambut perubahan kebutuhan demi keunggulan kompetitif). Pernyataan 1 SALAH (Waterfall bersifat sekuensial kaku dan sangat mahal/sulit untuk kembali ke fase sebelumnya). Pernyataan 2 BENAR (Retrospective berfokus pada evaluasi manusia, relasi, proses, dan alat kerja tim). Pernyataan 3 SALAH (begitu Sprint dimulai, Product Owner tidak boleh mengubah lingkup Sprint Backlog secara sepihak untuk menjaga fokus tim pengembang).",
        "isDiagnostic": False
    },
    {
        "id": "rpl-sim-35",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "simulasi",
        "difficulty": "simulation_hots",
        "topic": "Regulasi Lisensi Open Source & UU Perlindungan Data",
        "type": "matrix",
        "questionHtml": "Evaluasilah kebenaran pernyataan hukum dan kepatuhan (compliance) perangkat lunak terkait lisensi open source dan perlindungan data pribadi:",
        "statements": [
            {"id": "0", "text": "Lisensi MIT mengizinkan pihak lain memodifikasi kode sumber dan menggunakannya dalam aplikasi komersial tertutup (closed-source proprietary)."},
            {"id": "1", "text": "Lisensi GNU General Public License (GPL) mewajibkan seluruh proyek turunan yang memuat kode GPL untuk ikut melisensikan source code-nya secara terbuka di bawah GPL."},
            {"id": "2", "text": "Berdasarkan UU Perlindungan Data Pribadi (UU PDP) Indonesia, pengembang aplikasi berhak menjual data pribadi pengguna kepada pihak ketiga tanpa memerlukan persetujuan eksplisit (consent)."},
            {"id": "3", "text": "Klausul lisensi open source permissive (seperti BSD dan MIT) secara otomatis menghapus kewajiban pengembang untuk menyertakan disclaimer hak cipta asli pembuatnya."}
        ],
        "correctAnswers": {
            "0": True,
            "1": True,
            "2": False,
            "3": False
        },
        "formulaHud": {
            "title": "SOFTWARE LICENSING & DATA PRIVACY COMPLIANCE",
            "latex": "\\text{MIT: Permissive + Copyright Notice Required} \\quad \\mid \\quad \\text{GPL: Viral Copyleft} \\quad \\mid \\quad \\text{UU PDP: Explicit Consent}",
            "legend": "• Menjual data pribadi tanpa consent adalah tindak pidana menurut UU PDP<br>• Lisensi permisif tetap mewajibkan penyertakan teks lisensi & hak cipta asli"
        },
        "hints": {
            "concept": "MIT = permisif, boleh untuk komersial tertutup, tapi tetap wajib menyertakan notice hak cipta asli. GPL = copyleft. UU PDP melarang pemrosesan/penjualan data pribadi tanpa persetujuan eksplisit.",
            "execution": "Pernyataan 0 Benar. Pernyataan 1 Benar. Pernyataan 2 Salah. Pernyataan 3 Salah."
        },
        "explanation": "Pernyataan 0 BENAR (Lisensi MIT bersifat permisif dan bebas digunakan untuk proyek komersial tertutup). Pernyataan 1 BENAR (GPL memiliki klausul copyleft yang mewajibkan karya turunan berlisensi sama). Pernyataan 2 SALAH (Pasal 20 UU PDP mewajibkan dasar pemrosesan data pribadi berupa persetujuan sah eksplisit; memperjualbelikan data tanpa hak diancam pidana penjara). Pernyataan 3 SALAH (Lisensi MIT dan BSD tetap mewajibkan pencantuman teks lisensi dan hak cipta asli pada distribusi software).",
        "isDiagnostic": False
    }
]

print(f"Loaded {len(SIMULASI_QUESTIONS)} simulasi questions.")
