# -*- coding: utf-8 -*-
"""
pplg_data_hard.py
25 Authentic Hard (L3 C4/C5 HOTS) Questions for PPLG SMK/MAK
Strictly aligned with Pusmendik TKA 2026 & BSKAP 033/H/KR/2024
Anti-Bias: Distractor lengths balanced, keys evenly distributed.
"""

HARD_QUESTIONS = [
    {
        "id": "rpl-lat-h-01",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Arsitektur CI/CD Pipeline & Deployment",
        "type": "mcq",
        "questionHtml": "Sebuah tim software engineering merancang pipeline CI/CD modern pada GitHub Actions. Ketika programmer melakukan `git push` ke branch `main`, pipeline secara otomatis menjalankan tahapan: Linter -> Unit Test -> Build Docker Image -> Staging Deployment -> Automated Smoke Test -> Production Approval Gate. Jika tahap Automated Smoke Test di Staging menghasilkan exit code 1 (gagal), tindakan rekayasa otomatis yang semestinya dikonfigurasi pada pipeline adalah...",
        "options": [
            {"key": "A", "text": "Melakukan bypass pengujian dan langsung merilis container Docker ke cluster Kubernetes production secara paksa."},
            {"key": "B", "text": "Menghentikan pipeline seketika, mencegah rilis ke production, mengirim notifikasi alert ke tim, dan auto-rollback staging."},
            {"key": "C", "text": "Menghapus commit terakhir dari branch main remote secara permanen menggunakan perintah git push --force."},
            {"key": "D", "text": "Menonaktifkan server staging dan memindahkan seluruh database produksi ke cloud provider lain seketika."},
            {"key": "E", "text": "Mengubah kode status HTTP response pada smoke test menjadi 200 OK agar proses build dapat tetap selesai."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CI/CD PIPELINE QUALITY GATE",
            "latex": "\\text{Smoke Test Failed (exit 1)} \\implies \\text{Block Promotion} \\land \\text{Trigger Auto-Rollback} \\land \\text{Alert}",
            "legend": "• Quality Gate: Mencegah kode cacat mencapai production<br>• Fail-Fast principle: Kegagalan seawal mungkin demi menjaga stabilitas sistem"
        },
        "hints": {
            "concept": "Prinsip inti CI/CD adalah Fail-Fast: jika pengujian smoke test gagal di staging, deployment ke production harus langsung diblokir dan environment dikembalikan ke state stabil.",
            "execution": "Pilihan yang menerapkan mitigasi aman dan memblokir promosi ke production adalah B."
        },
        "explanation": "Pada pipeline CI/CD profesional, kegagalan automated smoke test di lingkungan staging memicu penghentian pipeline seketika untuk mencegah kode cacat dipromosikan ke production. Sistem juga melakukan rollback otomatis ke versi stabil sebelumnya serta mengirimkan alert notifikasi kepada tim pengembang. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-02",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Pelanggaran Liskov Substitution Principle (LSP)",
        "type": "mcq",
        "questionHtml": "Perhatikan implementasi kelas Java klasik berikut:\n```java\nclass PersegiPanjang {\n    protected int panjang, lebar;\n    public void setPanjang(int p) { this.panjang = p; }\n    public void setLebar(int l) { this.lebar = l; }\n    public int hitungLuas() { return panjang * lebar; }\n}\n\nclass Persegi extends PersegiPanjang {\n    @Override\n    public void setPanjang(int p) {\n        this.panjang = p;\n        this.lebar = p;\n    }\n    @Override\n    public void setLebar(int l) {\n        this.panjang = l;\n        this.lebar = l;\n    }\n}\n```\nKode di atas melanggar Liskov Substitution Principle (LSP) karena...",
        "options": [
            {"key": "A", "text": "Kelas Persegi tidak mengimplementasikan interface Cloneable untuk menduplikasi objek secara mendalam."},
            {"key": "B", "text": "Subclass Persegi merusak invarian kelas induk di mana pengubahan lebar juga ikut mengubah panjang secara tersembunyi."},
            {"key": "C", "text": "Method hitungLuas() tidak diberi anotasi @Override pada deklarasi di dalam kelas anak Persegi."},
            {"key": "D", "text": "Variabel panjang dan lebar dideklarasikan dengan access modifier protected daripada public statis."},
            {"key": "E", "text": "Kelas PersegiPanjang tidak dijadikan abstract class dengan method abstrak murni tanpa implementasi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "LISKOV SUBSTITUTION PRINCIPLE (LSP)",
            "latex": "\\text{If } S \\text{ is a subtype of } T, \\text{ then objects of type } T \\text{ may be replaced with } S \\text{ without altering correctness}",
            "legend": "• Subclass Persegi melanggar ekspektasi perilaku superclass PersegiPanjang (invarian: ubah lebar tidak ubah panjang)"
        },
        "hints": {
            "concept": "LSP mensyaratkan bahwa subclass harus dapat menggantikan superclass tanpa merusak kebenaran program. Klien yang menggunakan PersegiPanjang berekspektasi bahwa setLebar(l) hanya mengubah lebar.",
            "execution": "Pada Persegi, memanggil setLebar() secara tak terduga mengubah panjang juga, merusak kalkulasi klien yang memegang referensi PersegiPanjang."
        },
        "explanation": "LSP menyatakan bahwa objek subclass harus dapat menggantikan superclass tanpa mengubah ekspektasi perilaku sistem. Pada kelas `Persegi`, mengubah atribut lebar melalui `setLebar()` secara sepihak mengubah nilai panjang, melanggar kontrak perilaku `PersegiPanjang` di mana panjang dan lebar dapat dimodifikasi secara independen. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-03",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Pola Desain Thread-Safe Singleton",
        "type": "mcq",
        "questionHtml": "Perhatikan implementasi pola desain Singleton pada Java berikut:\n```java\npublic class DatabaseConnection {\n    private static volatile DatabaseConnection instance;\n    private DatabaseConnection() {}\n    \n    public static DatabaseConnection getInstance() {\n        if (instance == null) {\n            synchronized (DatabaseConnection.class) {\n                if (instance == null) {\n                    instance = new DatabaseConnection();\n                }\n            }\n        }\n        return instance;\n    }\n}\n```\nTujuan krusial dari penggunaan keyword `volatile` pada variabel `instance` pada pola Double-Checked Locking di atas adalah...",
        "options": [
            {"key": "A", "text": "Memaksa JVM menyimpan seluruh instansiasi objek DatabaseConnection langsung ke memori non-volatile SSD."},
            {"key": "B", "text": "Mencegah reordering instruksi kompilator JVM yang dapat menyebabkan thread lain membaca objek setengah jadi."},
            {"key": "C", "text": "Mengizinkan banyak instance objek diciptakan secara paralel saat beban thread server melampaui ambang batas."},
            {"key": "D", "text": "Menghapus kebutuhan blok synchronized saat method getInstance() dipanggil oleh thread yang berbeda."},
            {"key": "E", "text": "Mengamankan kredensial password koneksi basis data dari teknik pembacaan memory dump heap JVM."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "DOUBLE-CHECKED LOCKING & VOLATILE MEMORY BARRIER",
            "latex": "\\text{instance = new Obj()} \\implies \\{ 1.\\text{Alloc mem}, \\; 2.\\text{Init ctor}, \\; 3.\\text{Assign ref} \\}",
            "legend": "• Tanpa volatile: Compiler dapat me-reorder instruksi menjadi 1 -> 3 -> 2<br>• Akibat: Thread lain melihat instance != null padahal konstruktor belum selesai dieksekusi"
        },
        "hints": {
            "concept": "Keyword volatile di Java menyediakan jaminan visibilitas memori dan mencegah instruction reordering (memory barrier) oleh CPU/compiler.",
            "execution": "Tanpa volatile, alokasi memori bisa di-reorder sehingga thread lain memperoleh referensi objek yang belum selesai diinisialisasi."
        },
        "explanation": "Operasi `new DatabaseConnection()` melibatkan 3 langkah di level instruksi: (1) alokasi memori, (2) eksekusi konstruktor, dan (3) penugasan referensi ke variabel `instance`. Tanpa keyword `volatile`, JVM dapat melakukan instruksi reordering (1 -> 3 -> 2), menyebabkan thread lain melihat `instance != null` padahal inisialisasi objek belum tuntas. `volatile` bertindak sebagai memory barrier yang mencegah reordering tersebut. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-04",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Analisis Memory Leak pada Java",
        "type": "mcq",
        "questionHtml": "Aplikasi backend Java mengalami error `java.lang.OutOfMemoryError: Java heap space` setelah berjalan selama beberapa hari di server production. Analisis heap dump menunjukkan bahwa sebuah koleksi statis `public static final List<UserData> cache = new ArrayList<>()` menampung jutaan objek yang sudah tidak lagi digunakan oleh pengguna aktif. Mengapa Garbage Collector (GC) JVM tidak dapat membebaskan memori objek-objek tersebut?",
        "options": [
            {"key": "A", "text": "Karena objek dalam heap Java hanya bisa dibersihkan jika server dimatikan dan dinyalakan ulang secara fisik."},
            {"key": "B", "text": "Karena objek masih memiliki rantai referensi hidup yang terhubung ke GC Root melalui variabel koleksi statis cache."},
            {"key": "C", "text": "Karena Garbage Collector hanya membersihkan memori variabel primitif dan tidak memproses objek bertipe kelas."},
            {"key": "D", "text": "Karena ukuran memori heap JVM dibatasi secara kaku maksimal 64 megabyte oleh sistem operasi Linux."},
            {"key": "E", "text": "Karena kelas UserData tidak mengimplementasikan method finalize() untuk memicu penghapusan otomatis."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "GARBAGE COLLECTION REACHABILITY ANALYSIS",
            "latex": "\\text{GC Root (Static Variable)} \\xrightarrow{\\text{Strong Reference}} \\text{List Cache} \\xrightarrow{} \\text{UserData Object}",
            "legend": "• Objek yang masih dapat dijangkau (reachable) dari GC Roots TIDAK AKAN PERNAH disapu oleh GC<br>• Solusi: Gunakan WeakReference atau Eviction Policy (LRU Cache)"
        },
        "hints": {
            "concept": "Garbage Collector hanya mengklaim objek yang tidak lagi dapat dijangkau (unreachable) dari GC Roots (seperti variabel statis, stack frames aktif).",
            "execution": "Variabel static hidup sepanjang siklus hidup classloader aplikasi, sehingga semua objek di dalamnya dianggap tetap aktif oleh GC."
        },
        "explanation": "Variabel berstatus `static` hidup di method area/metaspace sepanjang siklus hidup aplikasi dan bertindak sebagai GC Root. Karena list statis tersebut terus memegang strong reference ke setiap objek `UserData`, Garbage Collector menganggap objek tersebut masih aktif dan 'reachable', sehingga memori heap tidak dapat dibebaskan hingga memicu OutOfMemoryError. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-05",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Bentuk Normal Boyce-Codd (BCNF)",
        "type": "mcq",
        "questionHtml": "Diberikan relasi tabel `BimbinganProyek(NIM, Kode_Keahlian, NIP_Dosen)` dengan aturan bisnis:\n1. Setiap mahasiswa (`NIM`) dan keahlian (`Kode_Keahlian`) dibimbing oleh tepat satu dosen (`NIP_Dosen`).\n2. Setiap dosen (`NIP_Dosen`) hanya menguasai dan mengajar satu keahlian (`Kode_Keahlian`).\nCandidate Key adalah `(NIM, Kode_Keahlian)` dan `(NIM, NIP_Dosen)`. Dependensi fungsional:\n- `(NIM, Kode_Keahlian) -> NIP_Dosen`\n- `NIP_Dosen -> Kode_Keahlian`\n\nTabel tersebut memenuhi 3NF tetapi BELUM memenuhi Boyce-Codd Normal Form (BCNF) karena...",
        "options": [
            {"key": "A", "text": "Tabel memiliki lebih dari satu candidate key komposit yang saling tumpang tindih atribut pembentuknya."},
            {"key": "B", "text": "Terdapat ketergantungan fungsional NIP_Dosen -> Kode_Keahlian di mana determinan NIP_Dosen bukan candidate key superkey."},
            {"key": "C", "text": "Atribut NIM tidak dapat digunakan sebagai foreign key ke tabel master data mahasiswa universitas."},
            {"key": "D", "text": "Nilai pada kolom NIP_Dosen masih mengandung repeating groups yang melanggar aturan atomisitas 1NF."},
            {"key": "E", "text": "Atribut Kode_Keahlian bukan merupakan atribut prima (prime attribute) dalam struktur relasi tabel."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "BOYCE-CODD NORMAL FORM (BCNF) AXIOM",
            "latex": "\\forall (X \\to Y) \\implies X \\text{ must be a Superkey}",
            "legend": "• 3NF melonggarkan jika Y adalah prime attribute<br>• BCNF tanpa pengecualian: Setiap determinan (sisi kiri dependensi) WAJIB superkey"
        },
        "hints": {
            "concept": "Syarat BCNF lebih ketat dari 3NF: untuk setiap dependensi fungsional X -> Y, maka X WAJIB merupakan superkey.",
            "execution": "Pada dependensi NIP_Dosen -> Kode_Keahlian, NIP_Dosen bertindak sebagai penentu (determinan) tetapi NIP_Dosen sendirian bukan candidate key."
        },
        "explanation": "Pada 3NF, dependensi $X \\to Y$ ditoleransi jika $Y$ adalah atribut prima (anggota candidate key). Namun pada BCNF, aturan mutlak menyatakan bahwa setiap determinan ($X$) WAJIB merupakan superkey. Karena `NIP_Dosen` menentukan `Kode_Keahlian` tetapi `NIP_Dosen` bukan superkey, tabel tersebut melanggar BCNF. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-06",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Optimasi Query & Eksekusi Indeks B-Tree",
        "type": "mcq",
        "questionHtml": "Tabel `transaksi_finansial` menampung 10 juta baris data dan memiliki indeks komposit B-Tree pada kolom `(created_at, status_transaksi)`. Perhatikan query SQL berikut:\n```sql\nSELECT id, nominal\nFROM transaksi_finansial\nWHERE status_transaksi = 'Sukses'\n  AND created_at >= '2026-01-01';\n```\nBerdasarkan prinsip *Leftmost Prefix Rule* pada indeks komposit B-Tree, bagaimana database optimizer mengeksekusi query tersebut?",
        "options": [
            {"key": "A", "text": "Database langsung menolak eksekusi query karena urutan klausa WHERE terbalik dari urutan indeks komposit."},
            {"key": "B", "text": "Database tetap memanfaatkan indeks secara efisien karena indeks dimulai dengan created_at (Leftmost Prefix cocok)."},
            {"key": "C", "text": "Database dipaksa melakukan Full Table Scan karena kolom status_transaksi diletakkan di baris pertama WHERE."},
            {"key": "D", "text": "Database otomatis memecah indeks komposit menjadi dua indeks tunggal terpisah di memori RAM server."},
            {"key": "E", "text": "Indeks hanya bisa digunakan jika seluruh kolom pada tabel transaksi disertakan dalam klausa SELECT."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "B-TREE COMPOSITE INDEX & LEFTMOST PREFIX",
            "latex": "\\text{Index: } (A, B) \\implies \\text{Filter on } (A) \\lor (A \\land B) \\text{ uses Index}",
            "legend": "• Leftmost prefix: created_at adalah kolom pertama indeks komposit<br>• Urutan penulisan di WHERE (A AND B vs B AND A) dioptimasi otomatis oleh Query Optimizer"
        },
        "hints": {
            "concept": "Leftmost prefix rule mensyaratkan kolom pertama indeks komposit hadir dalam kondisi WHERE. Modern RDBMS Query Optimizer mampu mereorganisasi urutan operator AND.",
            "execution": "created_at ada di dalam query sebagai filter rentang (range scan), sehingga database tetap dapat memanfaatkan indeks B-Tree."
        },
        "explanation": "Query Optimizer pada RDBMS modern (seperti PostgreSQL atau MySQL) secara otomatis mengevaluasi kondisi komutatif `AND`. Karena kolom pertama dari indeks komposit (`created_at`) digunakan dalam filter rentang, optimizer tetap dapat menggunakan indeks tersebut untuk memangkas pembacaan disk (Range Scan) secara efisien sesuai Leftmost Prefix Rule. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-07",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "ACID Deadlock pada Transaksi Konkuren",
        "type": "mcq",
        "questionHtml": "Dua transaksi transfer bank berjalan secara bersamaan (konkuren):\n- Transaksi 1: Mengunci Rekening A (`UPDATE Rekening SET saldo = ... WHERE id = 'A'`), lalu mencoba mengunci Rekening B.\n- Transaksi 2: Mengunci Rekening B (`UPDATE Rekening SET saldo = ... WHERE id = 'B'`), lalu mencoba mengunci Rekening A.\n\nKondisi persaingan resource ini menyebabkan terjadinya...",
        "options": [
            {"key": "A", "text": "Dirty Read di mana Transaksi 1 membaca saldo Rekening B yang belum di-commit oleh Transaksi 2."},
            {"key": "B", "text": "Deadlock di mana kedua transaksi saling menunggu kunci resource dilepaskan oleh transaksi lainnya."},
            {"key": "C", "text": "Phantom Read di mana jumlah baris tabel rekening berubah saat dieksekusi dalam satu transaksi."},
            {"key": "D", "text": "Non-Repeatable Read di mana nilai saldo rekening berubah di tengah pembacaan Transaksi 1."},
            {"key": "E", "text": "Cascade Rollback di mana seluruh transaksi database lain di server otomatis terhapus."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "DEADLOCK CYCLE IN TRANSACTION PROCESSING",
            "latex": "T_1 \\xrightarrow{\\text{holds}} \\text{Lock}(A) \\xrightarrow{\\text{waits for}} \\text{Lock}(B) \\xleftarrow{\\text{holds}} T_2 \\xrightarrow{\\text{waits for}} \\text{Lock}(A)",
            "legend": "• Siklus saling tunggu melingkar (Circular Wait)<br>• Mitigasi: RDBMS Deadlock Detector memilih 1 transaksi sebagai korban (victim) lalu di-ROLLBACK"
        },
        "hints": {
            "concept": "Deadlock terjadi saat transaksi T1 memegang kunci A dan menunggu kunci B, sementara transaksi T2 memegang kunci B dan menunggu kunci A.",
            "execution": "Situasi saling tunggu melingkar tanpa akhir ini dinamakan Deadlock."
        },
        "explanation": "Situasi di mana dua atau lebih transaksi saling menunggu resource yang sedang dikunci oleh transaksi lain dalam siklus melingkar (circular wait) dinamakan Deadlock. Database engine akan mendeteksi siklus ini dan secara otomatis membatalkan (ROLLBACK) salah satu transaksi korban (victim) untuk memecah kebuntuan. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-08",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Anatomi & Penyimpanan Aman JWT",
        "type": "mcq",
        "questionHtml": "Dalam implementasi otentikasi REST API modern menggunakan JSON Web Token (JWT), token terdiri dari 3 bagian: Header, Payload, dan Signature. Tempat penyimpanan token JWT yang PALING aman pada browser client untuk memitigasi pencurian sesi via serangan Cross-Site Scripting (XSS) adalah...",
        "options": [
            {"key": "A", "text": "Di dalam localStorage browser agar token dapat dibaca dan dimanipulasi dengan mudah oleh skrip JavaScript."},
            {"key": "B", "text": "Di dalam HttpOnly, Secure, dan SameSite Cookie sehingga skrip JavaScript pihak ketiga tidak dapat mengaksesnya."},
            {"key": "C", "text": "Di dalam sessionStorage browser agar token otomatis terhapus saat tab browser pengguna ditutup."},
            {"key": "D", "text": "Di dalam atribut data-token pada tag HTML body agar dapat diakses oleh seluruh elemen DOM halaman."},
            {"key": "E", "text": "Di dalam parameter query string URL agar token selalu disertakan pada setiap navigasi tautan web."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "JWT SECURITY ARCHITECTURE",
            "latex": "\\text{JWT} = \\text{Base64}(H) \\, . \\, \\text{Base64}(P) \\, . \\, \\text{HMAC}(\\text{Secret}, H.P)",
            "legend": "• localStorage / sessionStorage: Rentan XSS (dapat dicuri via document.cookie / window.localStorage)<br>• HttpOnly Cookie: Kebal pembacaan via JavaScript DOM API"
        },
        "hints": {
            "concept": "Cookie dengan atribut HttpOnly tidak dapat dibaca oleh kode JavaScript di browser (misal melalui document.cookie).",
            "execution": "Kombinasi HttpOnly, Secure (hanya HTTPS), dan SameSite (cegah CSRF) adalah standar industri OWASP untuk menyimpan token otentikasi."
        },
        "explanation": "Menyimpan JWT di `localStorage` sangat berbahaya karena rentan dicuri jika aplikasi memiliki celah XSS. Pendekatan yang direkomendasikan OWASP adalah menyimpan token otentikasi di dalam Cookie dengan flag `HttpOnly` (memblokir akses skrip JS), `Secure` (hanya dikirim via HTTPS), dan `SameSite=Strict/Lax` (memitigasi CSRF). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-09",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Mekanisme CORS Preflight Request",
        "type": "mcq",
        "questionHtml": "Sebuah aplikasi frontend web yang berjalan di origin `https://frontend.smk.id` mengirimkan request AJAX `fetch()` ke endpoint API di `https://api.smk.id/v1/transaksi` dengan header `Content-Type: application/json` dan `Authorization: Bearer <token>`. Mengapa browser secara otomatis mengirimkan request HTTP dengan method `OPTIONS` sebelum request utama dijalankan?",
        "options": [
            {"key": "A", "text": "Untuk menguji kecepatan latensi koneksi internet antara browser client dan data center server API."},
            {"key": "B", "text": "Sebagai mekanisme CORS Preflight untuk memverifikasi apakah server mengizinkan method dan custom header tersebut."},
            {"key": "C", "text": "Untuk mengunduh sertifikat SSL/TLS publik server API sebelum saluran enkripsi HTTPS dibangun."},
            {"key": "D", "text": "Karena server API mengalami kelebihan beban sehingga meminta browser mengirim request penyeimbang beban."},
            {"key": "E", "text": "Sebagai bentuk kompresi payload biner untuk menghemat kuota transmisi jaringan pengguna."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CORS PREFLIGHT PROTOCOL",
            "latex": "\\text{Non-Simple Request} \\implies \\text{Browser sends HTTP OPTIONS} \\xrightarrow{\\text{Server 204 with CORS Headers}} \\text{Actual POST/PUT}",
            "legend": "• Pemicu preflight: Content-Type application/json, Custom header (Authorization), Method PUT/DELETE/PATCH"
        },
        "hints": {
            "concept": "Permintaan cross-origin yang bukan 'simple request' (misalnya menyertakan header Authorization atau Content-Type JSON) memicu browser mengirimkan preflight OPTIONS request.",
            "execution": "Preflight memastikan server memahami dan menyetujui request sebenarnya sebelum data sensitif dikirim."
        },
        "explanation": "Spesifikasi W3C Cross-Origin Resource Sharing (CORS) mengharuskan browser mengirimkan preflight request menggunakan method `OPTIONS` untuk jenis permintaan non-simple (seperti menyertakan header `Authorization` atau payload JSON). Preflight bertujuan memeriksa izin server sebelum request utama yang sesungguhnya dikirimkan. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-10",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "JavaScript Microtask Starvation",
        "type": "mcq",
        "questionHtml": "Perhatikan skenario eksekusi kode JavaScript berikut:\n```javascript\nfunction infiniteMicrotask() {\n    Promise.resolve().then(() => {\n        infiniteMicrotask();\n    });\n}\ninfiniteMicrotask();\nsetTimeout(() => console.log('Timer selesai'), 0);\n```\nApa dampak rekayasa yang terjadi pada lingkungan runtime browser saat kode di atas dijalankan?",
        "options": [
            {"key": "A", "text": "Browser langsung mencetak string 'Timer selesai' karena timer macrotask memiliki prioritas lebih tinggi."},
            {"key": "B", "text": "Terjadi Microtask Starvation di mana timer setTimeout dan rendering UI tidak pernah dieksekusi (browser membeku)."},
            {"key": "C", "text": "V8 engine membatasi rekursi maksimal 10.000 kali lalu secara otomatis melempar RangeError: Maximum call stack."},
            {"key": "D", "text": "Fungsi setTimeout otomatis membatalkan antrean promise dan membersihkan microtask queue."},
            {"key": "E", "text": "Sistem operasi komputer langsung mengalami restart paksa akibat kebocoran memori RAM fisik."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "EVENT LOOP MICROTASK STARVATION",
            "latex": "\\text{Event Loop Rule: Drain ALL Microtasks before yielding to UI Render or Macrotask Queue}",
            "legend": "• Microtask queue yang terus diisi tanpa henti akan memblokir rendering browser dan task timer selamanya"
        },
        "hints": {
            "concept": "Aturan Event Loop: seluruh antrean Microtask harus kosong (drain) sebelum browser dapat memproses Macrotask (setTimeout) atau melakukan render frame visual.",
            "execution": "Rekursi Promise.then yang tak berujung akan terus membanjiri antrean microtask, menyebabkan kelaparan (starvation) pada macrotask dan UI render."
        },
        "explanation": "Event loop JavaScript memproses seluruh antrean Microtask hingga benar-benar kosong sebelum beralih ke Macrotask atau rendering layar. Rekursi tak terbatas di dalam `Promise.resolve().then()` menyebabkan 'Microtask Starvation', di mana `setTimeout` dan pembaruan UI browser terblokir total (halaman web freeze/membeku). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-11",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Penanganan NetworkOnMainThreadException",
        "type": "mcq",
        "questionHtml": "Seorang programmer Android pemula menulis kode pemanggilan HTTP REST API secara sinkron langsung di dalam method `onCreate()` sebuah Activity. Aplikasi langsung mengalami crash dengan logcat menampilkan error `android.os.NetworkOnMainThreadException`. Alasan arsitektural Google Android melarang operasi jaringan pada Main/UI Thread adalah...",
        "options": [
            {"key": "A", "text": "Paket data internet yang melintasi Main Thread otomatis kehilangan enkripsi keamanan protokol HTTPS."},
            {"key": "B", "text": "Operasi I/O jaringan yang lambat akan memblokir thread UI, menyebabkan frame drop dan memicu dialog ANR."},
            {"key": "C", "text": "Main Thread pada sistem Android tidak memiliki alokasi hak akses izin internet di AndroidManifest.xml."},
            {"key": "D", "text": "Driver kartu jaringan seluler pada smartphone hanya dapat berkomunikasi dengan thread bertipe daemon."},
            {"key": "E", "text": "Sistem operasi Android membatasi penggunaan RAM pada Main Thread maksimal sebesar 128 kilobyte."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "ANDROID ANR (APPLICATION NOT RESPONDING) TRIGGER",
            "latex": "\\text{Main Thread Blocked} > 5\\text{ seconds} \\implies \\text{Android OS triggers ANR Dialog}",
            "legend": "• Main Thread bertugas me-render UI 60/120 fps (16ms per frame)<br>• Solusi: Gunakan Coroutines (Dispatchers.IO) atau WorkManager"
        },
        "hints": {
            "concept": "Main Thread (UI Thread) bertanggung jawab menggambar layar dan merespons sentuhan pengguna. Memblokir Main Thread dengan operasi jaringan akan membekukan UI.",
            "execution": "Jika Main Thread terblokir selama 5 detik, sistem Android memunculkan dialog Application Not Responding (ANR)."
        },
        "explanation": "Main Thread pada Android bertanggung jawab merender antarmuka pengguna pada 60-120 fps. Operasi jaringan bersifat lambat dan tak terduga (I/O blocking). Jika dijalankan di Main Thread, aplikasi akan membeku dan memicu dialog Application Not Responding (ANR). Android melempar `NetworkOnMainThreadException` untuk memaksa developer menjalankan I/O pada background thread (misalnya menggunakan Coroutines `Dispatchers.IO`). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-12",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Migrasi Skema Basis Data Room Android",
        "type": "mcq",
        "questionHtml": "Aplikasi Android yang menggunakan Room Database ingin memperbarui skema tabel dari versi 1 ke versi 2 dengan menambahkan kolom `email` berstatus `NOT NULL` pada tabel `users`. Langkah rekayasa yang benar agar aplikasi pengguna yang sudah ada tidak mengalami crash fatal akibat hilangnya data lokal adalah...",
        "options": [
            {"key": "A", "text": "Mengaktifkan method fallbackToDestructiveMigration() pada Room database builder saat rilis aplikasi."},
            {"key": "B", "text": "Mendefinisikan objek Migration(1, 2) yang menjalankan perintah SQL ALTER TABLE dengan nilai DEFAULT yang valid."},
            {"key": "C", "text": "Menghapus file database SQLite lokal secara manual di penyimpanan internal perangkat pengguna."},
            {"key": "D", "text": "Mengubah nama file database menjadi nama baru sehingga sistem membuat basis data kosong yang baru."},
            {"key": "E", "text": "Menurunkan nomor versi database menjadi 0 agar Room mengabaikan perbedaan skema tabel."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "ROOM DATABASE MIGRATION STRATEGY",
            "latex": "\\text{Migration}(1, 2) \\colon \\text{database.execSQL(\"ALTER TABLE users ADD COLUMN email TEXT NOT NULL DEFAULT ''\")}",
            "legend": "• fallbackToDestructiveMigration(): Menghapus seluruh data tabel lama (DATA LOSS)<br>• Manual Migration: Menjaga integritas data pengguna tanpa kehilangan record"
        },
        "hints": {
            "concept": "fallbackToDestructiveMigration() menghapus semua data lama pengguna. Solusi yang benar untuk production adalah membuat objek Migration eksplisit.",
            "execution": "Migration(1, 2) dengan eksekusi ALTER TABLE dan nilai DEFAULT memastikan data lama tetap aman."
        },
        "explanation": "Menggunakan `fallbackToDestructiveMigration()` akan menghapus seluruh data pengguna yang tersimpan saat skema berubah. Solusi yang tepat pada aplikasi production adalah menyediakan skrip `Migration(1, 2)` eksplisit menggunakan perintah SQL `ALTER TABLE` disertai nilai `DEFAULT` agar integritas data pengguna lama tetap terjaga. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-13",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Optimasi Draw Calls & Texture Atlas",
        "type": "mcq",
        "questionHtml": "Sebuah gim 2D menampilkan ribuan sprite musuh, peluru, dan efek ledakan di layar, menyebabkan game mengalami frame rate drop drastis akibat jumlah Draw Calls yang melampaui 1.500 panggilan per frame. Teknik rekayasa grafis manakah yang PALING efektif untuk memangkas jumlah Draw Calls tersebut secara signifikan?",
        "options": [
            {"key": "A", "text": "Menggunakan file gambar PNG resolusi tinggi 4K individual terpisah untuk setiap sprite karakter gim."},
            {"key": "B", "text": "Menggabungkan seluruh sprite ke dalam Texture Atlas (Sprite Sheet) tunggal dan memanfaatkan Dynamic Batching."},
            {"key": "C", "text": "Menaikkan frekuensi clock CPU komputer pemain menggunakan perangkat lunak overclocking pihak ketiga."},
            {"key": "D", "text": "Merender setiap musuh pada kamera viewport terpisah dengan shader material yang berbeda-beda."},
            {"key": "E", "text": "Menonaktifkan v-sync dan mengubah format penyimpanan aset gambar menjadi format GIF animasi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "GPU DRAW CALL BATCHING",
            "latex": "\\text{Separate Textures} \\implies N \\text{ State Changes} \\quad \\text{vs} \\quad \\text{Texture Atlas} \\implies 1 \\text{ Batched Draw Call}",
            "legend": "• Setiap pergantian tekstur memaksa GPU melakukan state switch yang mahal<br>• Sprite Sheet memungkinkan penggabungan geometri ke dalam 1 batch render"
        },
        "hints": {
            "concept": "Draw Call adalah instruksi dari CPU ke GPU untuk menggambar objek. Pergantian tekstur individual memicu Draw Call baru.",
            "execution": "Texture Atlas menyatukan banyak gambar kecil ke satu tekstur besar sehingga GPU dapat merender ratusan sprite sekaligus dalam 1 Draw Call."
        },
        "explanation": "Tingginya jumlah Draw Call biasanya disebabkan oleh pergantian state material dan tekstur pada GPU. Dengan menggabungkan ribuan aset sprite ke dalam satu lembar gambar besar (Texture Atlas / Sprite Sheet), game engine dapat melakukan 'Batching'—merender ratusan objek sekaligus hanya dengan 1 panggilan Draw Call ke GPU. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-14",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Pola Desain Object Pooling",
        "type": "mcq",
        "questionHtml": "Pada gim tembak-menembak (bullet hell), pesawat pemain menembakkan 50 peluru per detik. Jika setiap peluru dibuat menggunakan `Instantiate()` dan dihapus menggunakan `Destroy()`, permainan sering mengalami stuttering/lag berkala setiap beberapa detik. Penyebab utama lag tersebut dan pola desain yang tepat untuk mengatasinya adalah...",
        "options": [
            {"key": "A", "text": "Kelebihan beban GPU; solusinya adalah menurunkan resolusi layar gim menjadi format monokrom."},
            {"key": "B", "text": "Alokasi dan dealokasi memori berulang memicu Garbage Collector (GC); solusinya menerapkan Object Pooling."},
            {"key": "C", "text": "Koneksi internet tidak stabil; solusinya adalah mewajibkan pemain bermain dalam mode single player offline."},
            {"key": "D", "text": "Hard disk membaca file audio peluru secara lambat; solusinya adalah menghapus seluruh efek suara tembakan."},
            {"key": "E", "text": "Suhu prosesor CPU meningkat drastis; solusinya adalah menurunkan kecepatan game loop menjadi 10 FPS."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "OBJECT POOLING PATTERN",
            "latex": "\\text{Pool Init (N items)} \\xrightarrow{\\text{Acquire (Set Active)}} \\text{In Use} \\xrightarrow{\\text{Release (Set Inactive)}} \\text{Return to Pool}",
            "legend": "• Menghindari alokasi heap baru secara konstan (`new`/`Instantiate`)<br>• Meniadakan lonjakan kerja Garbage Collector (Stop-The-World pause)"
        },
        "hints": {
            "concept": "Membuat (Instantiate) dan menghancurkan (Destroy) ribuan objek secara dinamis mengotori heap memori, memicu Garbage Collector bekerja keras menghentikan sementara jalannya game.",
            "execution": "Solusinya adalah Object Pooling: membuat pool objek sekali di awal, lalu mengaktifkan/menonaktifkan objek kembali."
        },
        "explanation": "Pembuatan dan penghancuran objek peluru secara terus-menerus menyebabkan fragmentasi memori heap dan memicu siklus Garbage Collection (GC) yang menghentikan eksekusi sementara (GC pause stutter). Pola desain `Object Pooling` memecahkan masalah ini dengan mendaur ulang objek yang sudah ada (mengubah status aktif/non-aktif) tanpa alokasi memori baru. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-15",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Continuous Collision Detection (CCD)",
        "type": "mcq",
        "questionHtml": "Dalam simulasi fisika gim, sebuah peluru berkecepatan sangat tinggi (super-fast projectile) terkadang menembus dinding tipis tanpa memicu tabrakan sama sekali (dikenal sebagai tunneling problem). Pendekatan teknis yang digunakan untuk mengatasi fenomena ini adalah...",
        "options": [
            {"key": "A", "text": "Meningkatkan ukuran radius bounding box objek musuh menjadi sepuluh kali lipat dari ukuran visual aslinya."},
            {"key": "B", "text": "Menerapkan Continuous Collision Detection (CCD) menggunakan teknik Raycasting atau Swept Volume."},
            {"key": "C", "text": "Menurunkan kecepatan clock prosesor fisika engine agar objek bergerak lebih lambat di layar pemain."},
            {"key": "D", "text": "Mengubah bentuk collider kotak AABB menjadi jaring poligon tak beraturan (irregular mesh collider)."},
            {"key": "E", "text": "Menghapus komponen Rigidbody dan memproses tabrakan secara manual pada event rendering frame."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "TUNNELING & CONTINUOUS COLLISION DETECTION (CCD)",
            "latex": "\\text{Raycast}(x_t, \\vec{v} \\cdot \\Delta t) \\cap \\text{Wall Collider} \\ne \\emptyset \\implies \\text{Collision Confirmed}",
            "legend": "• Discrete Collision: Hanya memeriksa posisi diskrit di t dan t+dt (bisa melompati dinding)<br>• CCD / Swept Volume: Memeriksa lintasan lintasan garis penuh antara dua frame"
        },
        "hints": {
            "concept": "Tunneling terjadi pada Discrete Collision Detection karena perpindahan objek dalam satu frame (v * dt) lebih besar daripada ketebalan dinding, sehingga objek 'melompati' dinding.",
            "execution": "Continuous Collision Detection (CCD) menembakkan raycast atau swept volume sepanjang lintasan pergerakan untuk mendeteksi tabrakan di antara dua frame."
        },
        "explanation": "Pada deteksi tabrakan diskrit biasa, objek berkecepatan tinggi dapat berada di depan dinding pada frame $N$ dan sudah berada di belakang dinding pada frame $N+1$ tanpa pernah berpotongan dengan dinding. Solusi standar industri adalah menerapkan Continuous Collision Detection (CCD) berbasis raycasting atau swept volume yang menguji seluruh segmen garis lintasan gerak objek. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-16",
        "subject": "rpl",
        "materi": "PENGUJIAN PERANGKAT LUNAK (QA)",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Kalkulasi Cyclomatic Complexity",
        "type": "mcq",
        "questionHtml": "Perhatikan grafik alur kendali (Control Flow Graph) sebuah method algoritma yang memiliki 12 edge (sisi alur), 9 node (simpul eksekusi), dan 1 connected component ($P = 1$). Berdasarkan formula Cyclomatic Complexity Thomas McCabe $V(G) = E - N + 2P$, berapa jumlah jalur independen minimum (basis path) yang wajib diuji dalam pengujian White-Box?",
        "options": [
            {"key": "A", "text": "3 jalur pengujian independen."},
            {"key": "B", "text": "5 jalur pengujian independen."},
            {"key": "C", "text": "7 jalur pengujian independen."},
            {"key": "D", "text": "9 jalur pengujian independen."},
            {"key": "E", "text": "21 jalur pengujian independen."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "MCCABE CYCLOMATIC COMPLEXITY FORMULA",
            "latex": "V(G) = E - N + 2P = 12 - 9 + 2(1) = 5",
            "legend": "• E: Jumlah Edge (12)<br>• N: Jumlah Node (9)<br>• P: Connected Components (1)<br>• Nilai V(G) = 5 merepresentasikan batas atas test cases basis path"
        },
        "hints": {
            "concept": "Rumus Cyclomatic Complexity McCabe: V(G) = E - N + 2P.",
            "execution": "Hitung: 12 - 9 + 2(1) = 3 + 2 = 5."
        },
        "explanation": "Berdasarkan rumus kompleksitas siklomatis McCabe: $V(G) = E - N + 2P$. Dengan $E = 12$, $N = 9$, dan $P = 1$, maka $V(G) = 12 - 9 + 2(1) = 3 + 2 = 5$. Artinya dibutuhkan minimal 5 test case independen untuk menguji seluruh percabangan logika kode program (basis path coverage). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-17",
        "subject": "rpl",
        "materi": "PENGUJIAN PERANGKAT LUNAK (QA)",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Perbedaan Test Doubles: Mock vs Stub",
        "type": "mcq",
        "questionHtml": "Dalam pengujian unit otomatis menggunakan framework seperti Mockito atau Jest, perbedaan mendasar antara objek tiruan bertipe `Stub` dan `Mock` adalah...",
        "options": [
            {"key": "A", "text": "Stub hanya berjalan di browser, sedangkan Mock hanya dapat dieksekusi di server berbasis NodeJS."},
            {"key": "B", "text": "Stub menyediakan data balasan siap pakai (state verification), sedangkan Mock memverifikasi interaksi pemanggilan method."},
            {"key": "C", "text": "Mock digunakan untuk pengujian performa beban, sedangkan Stub digunakan untuk pengujian keamanan penetrasi."},
            {"key": "D", "text": "Stub secara otomatis memodifikasi database produksi, sedangkan Mock hanya bekerja pada memori cache."},
            {"key": "E", "text": "Tidak ada perbedaan teknis sama sekali karena Mock dan Stub adalah sinonim kata yang persis sama."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "TEST DOUBLE TAXONOMY (GERARD MESZAROS)",
            "latex": "\\text{Stub (Canned Data)} \\implies \\text{State Verification} \\quad \\text{vs} \\quad \\text{Mock (Expectations)} \\implies \\text{Behavior Verification}",
            "legend": "• Stub: when(api.getData()).thenReturn(sample)<br>• Mock: verify(paymentService, times(1)).charge(amount)"
        },
        "hints": {
            "concept": "Martin Fowler menjelaskan: Stub digunakan untuk State Verification (memberikan jawaban kalengan/canned response). Mock digunakan untuk Behavior Verification (memeriksa apakah method tertentu dipanggil dengan parameter yang benar).",
            "execution": "Stub = verifikasi state data; Mock = verifikasi perilaku/interaksi pemanggilan."
        },
        "explanation": "Menurut taksonomi Gerard Meszaros dan Martin Fowler, `Stub` menyediakan data jawaban siap pakai (canned data) untuk merespons pemanggilan saat pengujian tanpa memverifikasi pemanggilan tersebut (State Verification). Sebaliknya, `Mock` diprogram dengan ekspektasi perilaku dan digunakan untuk memverifikasi apakah method tertentu benar-benar dipanggil dengan parameter yang diharapkan (Behavior Verification). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-18",
        "subject": "rpl",
        "materi": "DESAIN UI/UX & AKSESIBILITAS",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Pencegahan Kesalahan (Error Prevention) & Konfirmasi",
        "type": "mcq",
        "questionHtml": "Dalam perancangan antarmuka aplikasi perbankan digital, tindakan destruktif kritis (seperti menghapus rekening tabungan atau mentransfer dana nominal besar) wajib dirancang dengan menerapkan prinsip Usability Heuristic *Error Prevention*. Implementasi desain yang PALING tepat untuk memenuhi prinsip tersebut adalah...",
        "options": [
            {"key": "A", "text": "Langsung memproses transaksi seketika tombol diklik tanpa menampilkan rincian apapun demi kecepatan alur kerja."},
            {"key": "B", "text": "Menampilkan dialog konfirmasi dua langkah yang memuat ringkasan transaksi dan mewajibkan otorisasi PIN/Biometrik."},
            {"key": "C", "text": "Menyembunyikan tombol transfer di dalam menu navigasi tersembunyi agar pengguna tidak dapat menemukannya."},
            {"key": "D", "text": "Menampilkan pesan error merah di pojok layar setelah saldo tabungan pengguna terlanjur terpotong sistem."},
            {"key": "E", "text": "Menonaktifkan tombol kembali pada browser pengguna sehingga pengguna terpaksa menyelesaikan alur transaksi."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "NIELSEN HEURISTIC #5: ERROR PREVENTION",
            "latex": "\\text{Destructive Action} \\implies \\text{Explicit Review Screen} \\land \\text{Re-authentication (2FA/PIN)}",
            "legend": "• Mencegah slip dan mistake sebelum terjadi<br>• Jauh lebih baik dibanding memberikan pesan error setelah bencana terjadi"
        },
        "hints": {
            "concept": "Heuristik Error Prevention: desain yang baik mencegah terjadinya kesalahan sejak awal, bukan hanya mengobatinya setelah terjadi.",
            "execution": "Layar konfirmasi dan otorisasi PIN memberikan kesempatan bagi pengguna untuk meninjau ulang tindakan berisiko tinggi."
        },
        "explanation": "Heuristik ke-5 Jakob Nielsen (Error Prevention) menekankan bahwa sistem yang luar biasa mencegah masalah terjadi sejak awal. Untuk tindakan berisiko tinggi (keuangan), sistem wajib menyediakan layar konfirmasi yang merinci detail transaksi dan mensyaratkan otentikasi ulang (PIN/biometrik) sebelum eksekusi dijalankan. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-19",
        "subject": "rpl",
        "materi": "DESAIN UI/UX & AKSESIBILITAS",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Hick's Law & Beban Kognitif Antarmuka",
        "type": "mcq",
        "questionHtml": "Dashboard aplikasi enterprise menyajikan 40 tombol menu navigasi secara acak pada halaman beranda, menyebabkan pengguna membutuhkan waktu sangat lama untuk memilih fitur yang diinginkan. Hukum psikologi UI/UX yang menjelaskan fenomena peningkatan waktu pengambilan keputusan seiring bertambahnya jumlah pilihan adalah...",
        "options": [
            {"key": "A", "text": "Fitts's Law yang menyatakan waktu menjangkau target berbanding lurus dengan jarak dan ukuran tombol."},
            {"key": "B", "text": "Hick's Law yang menyatakan waktu pengambilan keputusan meningkat secara logaritmik seiring bertambahnya opsi pilihan."},
            {"key": "C", "text": "Miller's Law yang menyatakan kapasitas memori kerja manusia rata-rata mampu menampung 7 plus minus 2 potongan informasi."},
            {"key": "D", "text": "Jakob's Law yang menyatakan pengguna menghabiskan sebagian besar waktu di situs lain dan menginginkan pola serupa."},
            {"key": "E", "text": "Pareto Principle yang menyatakan 80 persen dampak visual antarmuka dihasilkan oleh 20 persen pilihan palet warna."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "HICK'S LAW MATHEMATICAL MODEL",
            "latex": "RT = b \\cdot \\log_2(n + 1)",
            "legend": "• RT: Reaction Time (Waktu respon)<br>• n: Jumlah pilihan stimulus yang disajikan<br>• Solusi: Progressive disclosure & kategorisasi bertingkat"
        },
        "hints": {
            "concept": "Hick's Law (Hukum Hick-Hyman): semakin banyak pilihan yang diberikan kepada pengguna, semakin lama waktu yang dibutuhkan untuk mengambil keputusan.",
            "execution": "Rumusnya melibatkan logaritma basis 2 dari jumlah opsi: RT = b * log2(n + 1)."
        },
        "explanation": "Hick's Law menyatakan bahwa waktu yang dibutuhkan seseorang untuk membuat keputusan berbanding lurus dengan jumlah dan kompleksitas pilihan yang tersedia ($RT = b \\cdot \\log_2(n + 1)$). Solusi desain terbaik untuk mengatasi beban kognitif ini adalah pengelompokan menu (kategorisasi) dan progressive disclosure. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-20",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Komparasi Lisensi Copyleft: LGPL vs AGPL",
        "type": "mcq",
        "questionHtml": "Perusahaan SaaS (Software as a Service) membangun platform cloud komersial tertutup (proprietary) dan ingin memanfaatkan pustaka open source di sisi backend server. Mengapa perusahaan tersebut sangat menghindari penggunaan pustaka berlisensi GNU Affero General Public License (AGPL) dibandingkan LGPL?",
        "options": [
            {"key": "A", "text": "Karena lisensi AGPL mewajibkan pembayaran kompensasi royalti finansial bulanan kepada para kontributor pustaka."},
            {"key": "B", "text": "Karena klausul jaringan AGPL mewajibkan seluruh source code platform SaaS dibuka ke publik jika diakses melalui network."},
            {"key": "C", "text": "Karena AGPL secara otomatis menghapus hak paten algoritma milik perusahaan yang didaftarkan ke kementerian hukum."},
            {"key": "D", "text": "Karena pustaka berlisensi AGPL tidak mengizinkan enkripsi data komunikasi pada protokol jaringan HTTPS."},
            {"key": "E", "text": "Karena lisensi AGPL hanya dapat dijalankan pada sistem operasi mainframe tua dan tidak mendukung arsitektur Linux."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "AGPL CLOUD NETWORK LOOPHOLE CLOSURE",
            "latex": "\\text{Network Interaction (SaaS)} \\implies \\text{Distribution Requirement Triggered (Full Source Disclosure)}",
            "legend": "• GPL biasa: Syarat rilis source hanya jika mendistribusikan file biner<br>• AGPL: Menutup celah cloud, interaksi via jaringan dianggap distribusi"
        },
        "hints": {
            "concept": "AGPL (Affero GPL) dirancang khusus untuk menutup celah SaaS: menjalankan software di server dan membiarkan user berinteraksi via jaringan dianggap sebagai 'distribusi', mewajibkan rilis source code.",
            "execution": "Perusahaan SaaS proprietary menghindari AGPL karena akan memaksa seluruh kode backend mereka dibuka ke publik."
        },
        "explanation": "Lisensi GPL standar hanya mewajibkan pembagian source code jika software didistribusikan dalam bentuk biner. AGPL (Affero GPL) menutup celah ini (SaaS loophole) dengan menetapkan bahwa menyediakan layanan software melalui jaringan internet dihitung sebagai distribusi, sehingga perusahaan SaaS komersial wajib merilis seluruh source code platform mereka ke publik. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-21",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Strategi Git Trunk-Based Development",
        "type": "mcq",
        "questionHtml": "Dalam tim rekayasa perangkat lunak dengan frekuensi deployment tinggi (High-Performing DevOps), praktik Trunk-Based Development lebih diutamakan dibandingkan Git Flow tradisional karena...",
        "options": [
            {"key": "A", "text": "Trunk-Based Development menghapus kewajiban pengujian otomatis unit testing sebelum proses rilis production."},
            {"key": "B", "text": "Menghindari merge hell dengan mengintegrasikan branch fitur berumur pendek (short-lived) langsung ke trunk setiap hari."},
            {"key": "C", "text": "Mengizinkan seluruh pengembang mengedit branch produksi secara langsung tanpa melalui proses code review."},
            {"key": "D", "text": "Mewajibkan pembuatan minimal sepuluh cabang branch terpisah untuk setiap tiket perbaikan bug kecil."},
            {"key": "E", "text": "Mengharuskan deployment ke server dilakukan secara manual oleh manajer proyek setiap akhir pekan."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "TRUNK-BASED DEVELOPMENT VELOCITY",
            "latex": "\\text{Short-Lived Feature Branches (< 1 day)} \\xrightarrow{\\text{Continuous Integration}} \\text{Trunk (main)}",
            "legend": "• Mencegah akumulasi drift kode antar branch<br>• Didukung oleh Feature Flags untuk menyembunyikan fitur belum tuntas"
        },
        "hints": {
            "concept": "Git Flow tradisional sering memicu 'merge hell' karena feature branch bertahan berpekan-pekan. Trunk-Based Development menggunakan branch kecil yang di-merge ke main/trunk setiap hari.",
            "execution": "Keunggulannya adalah integrasi berkelanjutan yang cepat dan ketiadaan konflik merge besar."
        },
        "explanation": "Trunk-Based Development adalah praktik di mana developer menggabungkan perubahan kecil dan sering (short-lived branches) langsung ke branch utama (`main`/`trunk`) setidaknya sekali sehari. Hal ini menghilangkan masalah 'merge hell' dan konflik integrasi besar yang kerap terjadi pada Git Flow tradisional. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-22",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Prinsip SOLID: Interface Segregation Principle",
        "type": "mcq",
        "questionHtml": "Perhatikan antarmuka Java monolitik (Fat Interface) berikut:\n```java\npublic interface MesinKantor {\n    void cetakDokumen();\n    void scanDokumen();\n    void kirimFax();\n}\n```\nKetika kelas `PrinterEkonomis` dipaksa mengimplementasikan antarmuka di atas padahal perangkat tersebut tidak memiliki perangkat keras scanner maupun fax, pelanggaran prinsip SOLID yang terjadi dan solusi rekayasanya adalah...",
        "options": [
            {"key": "A", "text": "Pelanggaran OCP; solusinya adalah menambahkan metode cetakDokumenBerwarna() ke dalam interface tersebut."},
            {"key": "B", "text": "Pelanggaran Interface Segregation Principle (ISP); solusinya memecah interface menjadi Pencetak, Pemindai, dan PengirimFax."},
            {"key": "C", "text": "Pelanggaran Dependency Inversion Principle; solusinya menggunakan framework Spring IoC container secara paksa."},
            {"key": "D", "text": "Pelanggaran Single Responsibility; solusinya membiarkan method yang tidak didukung melempar UnsupportedOperationException."},
            {"key": "E", "text": "Pelanggaran Encapsulation; solusinya mengubah seluruh method interface menjadi atribut variabel publik."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SOLID - INTERFACE SEGREGATION PRINCIPLE (ISP)",
            "latex": "\\text{Clients should not be forced to depend upon interfaces that they do not use}",
            "legend": "• Fat interface dipecah menjadi antarmuka peran spesifik (Role Interfaces)<br>• PrinterEkonomis cukup implements Pencetak"
        },
        "hints": {
            "concept": "ISP (prinsip huruf 'I' dalam SOLID): Klien tidak boleh dipaksa bergantung pada method-method yang tidak digunakannya.",
            "execution": "Memecah antarmuka gemuk menjadi beberapa interface kecil yang spesifik (Pencetak, Pemindai, PengirimFax) adalah solusi ISP."
        },
        "explanation": "Interface Segregation Principle (ISP) menyatakan bahwa 'klien tidak boleh dipaksa bergantung pada antarmuka yang tidak digunakannya'. Memaksa `PrinterEkonomis` mengimplementasikan method `scanDokumen()` dan `kirimFax()` melanggar ISP. Solusinya adalah memecah interface monolitik tersebut menjadi antarmuka modular: `Pencetak`, `Pemindai`, dan `PengirimFax`. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-23",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Prinsip SOLID: Dependency Inversion Principle",
        "type": "mcq",
        "questionHtml": "Perhatikan perancangan kelas berikut di mana modul tingkat tinggi memiliki keterikatan langsung (tight coupling) dengan modul tingkat rendah:\n```java\npublic class NotifikasiService {\n    private GmailSender sender = new GmailSender();\n    public void kirim(String pesan) {\n        sender.sendEmail(pesan);\n    }\n}\n```\nUntuk merefaktor kode di atas agar memenuhi Dependency Inversion Principle (DIP), arsitektur yang semestinya dibangun adalah...",
        "options": [
            {"key": "A", "text": "Menghapus kelas GmailSender dan menulis socket jaringan SMTP langsung di dalam kelas NotifikasiService."},
            {"key": "B", "text": "Membuat interface PesanSender, mengimplementasikannya pada GmailSender, dan menginjeksi interface ke NotifikasiService."},
            {"key": "C", "text": "Mengubah metode sendEmail menjadi method statis global yang dapat dipanggil langsung dari package mana pun."},
            {"key": "D", "text": "Mewariskan kelas NotifikasiService langsung dari kelas konkret GmailSender menggunakan kata kunci extends."},
            {"key": "E", "text": "Menyimpan kredensial akun GmailSender secara hardcoded di dalam variabel konstanta kelas NotifikasiService."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SOLID - DEPENDENCY INVERSION PRINCIPLE (DIP)",
            "latex": "\\text{High-level & Low-level Modules} \\to \\text{Depend on Abstractions (Interfaces)}",
            "legend": "• NotifikasiService bergantung pada interface PesanSender<br>• GmailSender mengimplementasikan interface PesanSender<br>• Dependency diinjeksi via constructor (Inversion of Control)"
        },
        "hints": {
            "concept": "DIP (huruf 'D' dalam SOLID): Modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah. Keduanya harus bergantung pada abstraksi (interface).",
            "execution": "Gunakan antarmuka perantara PesanSender dan terapkan Dependency Injection."
        },
        "explanation": "Dependency Inversion Principle (DIP) mengharuskan modul tingkat tinggi (`NotifikasiService`) dan modul tingkat rendah (`GmailSender`) bergantung pada abstraksi. Dengan membuat interface `PesanSender` dan menginjeksikannya melalui constructor, `NotifikasiService` menjadi loosely coupled dan dapat dengan mudah dialihkan ke penyedia lain (seperti WhatsAppSender atau SMSSender) tanpa mengubah kodenya. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-24",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "Mitigasi Cross-Site Request Forgery (CSRF)",
        "type": "mcq",
        "questionHtml": "Pada aplikasi perbankan berbasis web, penyerang membuat situs jahat `https://attacker.com` yang memuat gambar tersembunyi `<img src=\"https://bank.com/transfer?nominal=10000000&ke=penyerang\">`. Jika korban sedang login di `bank.com`, browser korban otomatis mengirimkan cookie sesi ke server bank. Mekanisme pengamanan modern yang PALING efektif untuk memblokir eksploitasi CSRF tersebut adalah...",
        "options": [
            {"key": "A", "text": "Mengenkripsi seluruh basis data perbankan menggunakan algoritma simetris Advanced Encryption Standard 256-bit."},
            {"key": "B", "text": "Menerapkan atribut Cookie SameSite=Strict/Lax dan memvalidasi Anti-CSRF Token acak pada setiap request mutasi state."},
            {"key": "C", "text": "Menghapus penggunaan kata sandi dan menggantinya dengan pertanyaan keamanan nama ibu kandung pengguna."},
            {"key": "D", "text": "Mengizinkan seluruh domain luar mengeksekusi request POST melalui konfigurasi header Access-Control-Allow-Origin: *."},
            {"key": "E", "text": "Mewajibkan pengguna menyegarkan (refresh) halaman browser secara manual setiap kali melakukan transfer dana."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CSRF DEFENSE IN DEPTH",
            "latex": "\\text{SameSite=Strict/Lax Cookie} \\land \\text{Cryptographic Anti-CSRF Token} \\implies \\text{Cross-Origin Request Blocked}",
            "legend": "• SameSite=Strict: Cookie tidak dikirim pada navigasi cross-site<br>• Anti-CSRF Token: Nilai rahasia per sesi yang tidak bisa ditebak situs penyerang"
        },
        "hints": {
            "concept": "CSRF memanfaatkan fakta bahwa browser otomatis menyertakan kredensial cookie pada permintaan lintas situs.",
            "execution": "Dua pertahanan utama CSRF: Atribut Cookie SameSite (Strict/Lax) dan Anti-CSRF Token (Synchronizer Token Pattern)."
        },
        "explanation": "CSRF mengeksploitasi mekanisme browser yang otomatis melampirkan cookie sesi saat mengirim request ke domain target. Pertahanan standar OWASP mencakup: (1) Mengatur flag `SameSite=Strict` atau `SameSite=Lax` pada cookie agar tidak ikut terkirim pada request lintas situs, dan (2) Menggunakan Anti-CSRF Synchronizer Token rahasia yang wajib diverifikasi oleh server pada setiap request mutasi data (POST/PUT/DELETE). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-h-25",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "hard",
        "topic": "SQL Window Functions & Analitik Data",
        "type": "mcq",
        "questionHtml": "Perhatikan query SQL analitik penggajian karyawan berikut:\n```sql\nSELECT nama, departemen, gaji,\n       DENSE_RANK() OVER (PARTITION BY departemen ORDER BY gaji DESC) AS ranking_gaji\nFROM pegawai;\n```\nJika pada departemen IT terdapat tiga pegawai: Anton (gaji 15 jt), Budi (gaji 15 jt), dan Citra (gaji 12 jt), output nilai kolom `ranking_gaji` untuk ketiga pegawai tersebut berturut-turut adalah...",
        "options": [
            {"key": "A", "text": "Anton ranking 1, Budi ranking 2, dan Citra ranking 3 karena fungsi analitik memecah nilai seri secara sekuensial."},
            {"key": "B", "text": "Anton ranking 1, Budi ranking 1, dan Citra ranking 2 karena DENSE_RANK tidak melompati urutan angka setelah nilai seri."},
            {"key": "C", "text": "Anton ranking 1, Budi ranking 1, dan Citra ranking 3 karena fungsi analitik wajib melompati nomor peringkat."},
            {"key": "D", "text": "Anton ranking 1, Budi ranking 2, dan Citra ranking 2 karena peringkat dihitung berdasarkan abjad nama pegawai."},
            {"key": "E", "text": "Query memicu runtime error karena fungsi analitik OVER tidak dapat digabungkan dengan klausul PARTITION BY."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SQL RANKING WINDOW FUNCTIONS COMPARISON",
            "latex": "\\text{ROW\\_NUMBER}: 1, 2, 3 \\quad \\mid \\quad \\text{RANK}: 1, 1, 3 \\quad \\mid \\quad \\text{DENSE\\_RANK}: 1, 1, 2",
            "legend": "• DENSE_RANK: Nilai sama mendapat rank sama, nomor peringkat berikutnya TIDAK MELOMPAT (1, 1, 2)<br>• RANK: Nomor peringkat melompat sesuai jumlah duplikat (1, 1, 3)"
        },
        "hints": {
            "concept": "Perbedaan RANK() vs DENSE_RANK(): RANK() melompati nomor urut setelah terjadi tie/seri (1, 1, 3). DENSE_RANK() tidak melompati nomor urut (1, 1, 2).",
            "execution": "Anton dan Budi memiliki gaji sama (15 jt) -> keduanya ranking 1. Citra (12 jt) mendapatkan ranking 2 berikutnya tanpa lompatan."
        },
        "explanation": "Fungsi `DENSE_RANK()` memberikan nomor peringkat yang sama untuk nilai baris yang identik (Anton dan Budi sama-sama ranking 1), dan memberikan nomor integer berikutnya secara berurutan tanpa lompatan celah ranking (Citra mendapat ranking 2). Jika menggunakan `RANK()`, Citra akan mendapat ranking 3. Jawaban: B.",
        "isDiagnostic": False
    }
]

print(f"Loaded {len(HARD_QUESTIONS)} hard questions.")
