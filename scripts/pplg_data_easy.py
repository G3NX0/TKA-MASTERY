# -*- coding: utf-8 -*-
"""
pplg_data_easy.py
25 Authentic Easy (L1/L2 C2/C3) Questions for PPLG SMK/MAK
Strictly aligned with Pusmendik TKA 2026 & BSKAP 033/H/KR/2024
Anti-Bias: Distractor lengths balanced, keys evenly distributed.
"""

EASY_QUESTIONS = [
    {
        "id": "rpl-lat-e-01",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Agile Scrum Roles & Responsibilities",
        "type": "mcq",
        "questionHtml": "Dalam kerangka kerja Scrum pada pengembangan perangkat lunak, peran manakah yang bertanggung jawab secara penuh untuk mengelola Product Backlog dan memaksimalkan nilai bisnis produk yang dihasilkan?",
        "options": [
            {"key": "A", "text": "Scrum Master yang memfasilitasi daily standup dan menghilangkan hambatan kerja tim."},
            {"key": "B", "text": "Product Owner yang menyusun prioritas backlog dan mendefinisikan kriteria bisnis."},
            {"key": "C", "text": "Lead Developer yang merancang arsitektur kode dan mengawasi implementasi basis data."},
            {"key": "D", "text": "Quality Assurance yang memverifikasi acceptance criteria dan menjalankan pengujian."},
            {"key": "E", "text": "Project Sponsor yang mendanai inisiatif perangkat lunak dan menyetujui anggaran."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SCRUM ARTIFACTS & RESPONSIBILITIES",
            "latex": "\\text{Product Backlog} \\xrightarrow{\\text{Sprint Planning}} \\text{Sprint Backlog} \\to \\text{Increment}",
            "legend": "• Product Owner: Value maximizer & backlog owner<br>• Scrum Master: Process coach & impediment remover<br>• Dev Team: Increment builder"
        },
        "hints": {
            "concept": "Scrum membagi 3 peran inti: Product Owner (kelola backlog & nilai bisnis), Scrum Master (fasilitasi proses), dan Development Team (rekayasa teknis).",
            "execution": "Pilihlah peran yang fokus pada visi produk dan prioritas backlog bisnis, yaitu Product Owner."
        },
        "explanation": "Product Owner bertanggung jawab mengoptimalkan nilai produk dan mengelola Product Backlog secara berkesinambungan. Pilihan A adalah peran Scrum Master, sedangkan C dan D adalah tim pengembang teknis. Jawaban: B.",
        "isDiagnostic": True
    },
    {
        "id": "rpl-lat-e-02",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Enkapsulasi & Access Modifier",
        "type": "mcq",
        "questionHtml": "Perhatikan potongan kode kelas Java berikut:\n```java\npublic class RekeningBank {\n    private double saldo;\n    \n    public RekeningBank(double saldoAwal) {\n        this.saldo = saldoAwal;\n    }\n    \n    public double getSaldo() {\n        return this.saldo;\n    }\n}\n```\nTujuan utama dari penerapan modifier `private` pada variabel `saldo` adalah...",
        "options": [
            {"key": "A", "text": "Mencegah variabel saldo diakses atau dimodifikasi langsung secara sembarangan dari luar kelas."},
            {"key": "B", "text": "Mengizinkan semua kelas dalam package yang sama mengakses nilai variabel saldo secara langsung."},
            {"key": "C", "text": "Mempercepat proses alokasi memori runtime saat objek kelas RekeningBank diinstansiasi oleh JVM."},
            {"key": "D", "text": "Membuat variabel saldo dapat diwariskan secara otomatis tanpa pembatasan ke seluruh subclass turunan."},
            {"key": "E", "text": "Mengharuskan JVM menganggap variabel saldo sebagai konstanta mutlak yang nilainya tidak dapat diubah."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "DATA HIDING & ENKAPSULASI",
            "latex": "\\text{Class} \\{ \\text{private attribute} + \\text{public getter/setter} \\}",
            "legend": "• private: Akses eksklusif dalam kelas deklarasi<br>• protected: Akses dalam package & turunan subclass<br>• public: Akses global tanpa restriksi"
        },
        "hints": {
            "concept": "Enkapsulasi menyembunyikan data internal objek (data hiding) menggunakan modifier private dan menyediakan gerbang terkontrol melalui public method.",
            "execution": "Modifier private memastikan integritas state objek agar tidak diubah secara langsung dari kode eksternal."
        },
        "explanation": "Modifier `private` menerapkan prinsip enkapsulasi (data hiding) agar atribut tidak dapat diakses atau diubah langsung dari luar kelas, melainkan melalui method perantara seperti getter atau setter. Jawaban: A.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-03",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Pewarisan (Inheritance)",
        "type": "mcq",
        "questionHtml": "Dalam bahasa pemrograman Java, kata kunci (keyword) yang digunakan oleh sebuah subclass untuk mewarisi atribut dan method dari superclass konkret adalah...",
        "options": [
            {"key": "A", "text": "implements yang digunakan saat mendeklarasikan adopsi kontrak interface abstrak."},
            {"key": "B", "text": "inherits yang digunakan secara eksplisit dalam pewarisan kelas turunan Java modern."},
            {"key": "C", "text": "extends yang digunakan untuk memperluas fungsionalitas dari superclass induk."},
            {"key": "D", "text": "super yang digunakan untuk mereferensikan instance objek superclass pada constructor."},
            {"key": "E", "text": "instanceof yang digunakan untuk memeriksa kesesuaian tipe objek pada waktu runtime."}
        ],
        "correctKey": "C",
        "formulaHud": {
            "title": "INHERITANCE RELATIONSHIP",
            "latex": "\\text{class } B \\text{ extends } A \\implies B \\text{ is-a } A",
            "legend": "• extends: Pewarisan kelas induk konkret/abstrak<br>• implements: Realisasi kontrak antarmuka interface<br>• super: Referensi delegasi superclass"
        },
        "hints": {
            "concept": "Keyword 'extends' menyatakan relasi 'is-a' antara subclass dan superclass dalam Java.",
            "execution": "Jangan tertukar antara extends (untuk class) dan implements (untuk interface)."
        },
        "explanation": "Di Java, kelas turunan menggunakan keyword `extends` untuk mewarisi superclass. Keyword `implements` digunakan untuk mengimplementasikan antarmuka (`interface`). Jawaban: C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-04",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Kategori Perintah SQL (DDL vs DML)",
        "type": "mcq",
        "questionHtml": "Manakah kelompok perintah SQL berikut yang seluruh anggotanya termasuk dalam kategori Data Definition Language (DDL)?",
        "options": [
            {"key": "A", "text": "SELECT, INSERT, UPDATE, dan DELETE yang digunakan untuk manipulasi data baris."},
            {"key": "B", "text": "CREATE, ALTER, DROP, dan TRUNCATE yang digunakan untuk mendefinisikan skema struktur tabel."},
            {"key": "C", "text": "GRANT, REVOKE, DENY, dan AUDIT yang digunakan untuk pengelolaan hak akses otorisasi data."},
            {"key": "D", "text": "COMMIT, ROLLBACK, SAVEPOINT, dan RELEASE yang digunakan untuk mengontrol siklus transaksi ACID."},
            {"key": "E", "text": "MERGE, UPSERT, REPLACE, dan BULK LOAD yang digunakan untuk sinkronisasi rekaman basis data."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SQL COMMAND TAXONOMY",
            "latex": "\\text{SQL} = \\text{DDL} \\cup \\text{DML} \\cup \\text{DCL} \\cup \\text{TCL}",
            "legend": "• DDL (Struktur): CREATE, ALTER, DROP, TRUNCATE<br>• DML (Data): SELECT, INSERT, UPDATE, DELETE<br>• DCL (Hak Akses): GRANT, REVOKE<br>• TCL (Transaksi): COMMIT, ROLLBACK"
        },
        "hints": {
            "concept": "DDL (Data Definition Language) mendefinisikan dan memodifikasi struktur skema tabel, bukan isi data rekaman.",
            "execution": "Carilah opsi yang memuat perintah pembentukan dan penghapusan tabel: CREATE, ALTER, DROP."
        },
        "explanation": "DDL (Data Definition Language) mencakup perintah yang mengelola struktur/skema database: `CREATE`, `ALTER`, `DROP`, dan `TRUNCATE`. Pilihan A adalah DML, pilihan C adalah DCL, dan D adalah TCL. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-05",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Prinsip Normalisasi 1NF",
        "type": "mcq",
        "questionHtml": "Sebuah tabel relasional dikatakan telah memenuhi bentuk normal pertama (First Normal Form / 1NF) apabila memenuhi syarat utama yaitu...",
        "options": [
            {"key": "A", "text": "Seluruh atribut non-kunci primer tidak memiliki ketergantungan transitif terhadap atribut lain."},
            {"key": "B", "text": "Tabel telah memiliki foreign key yang terhubung secara referensial ke tabel induk lain."},
            {"key": "C", "text": "Setiap kolom bernilai atomik dan tidak terdapat kelompok data berulang (repeating groups)."},
            {"key": "D", "text": "Semua atribut non-kunci bergantung secara fungsional penuh pada primary key komposit."},
            {"key": "E", "text": "Setiap baris data telah diurutkan secara fisik berdasarkan nilai indeks clustered B-Tree."}
        ],
        "correctKey": "C",
        "formulaHud": {
            "title": "TAHAPAN NORMALISASI DATA",
            "latex": "\\text{Unnormalized} \\xrightarrow{1\\text{NF}} \\text{Atomik} \\xrightarrow{2\\text{NF}} \\text{No Partial} \\xrightarrow{3\\text{NF}} \\text{No Transitive}",
            "legend": "• 1NF: Atomic values & no multi-valued attributes<br>• 2NF: 1NF + no partial functional dependency<br>• 3NF: 2NF + no transitive dependency"
        },
        "hints": {
            "concept": "1NF fokus pada keatoman data (satu sel hanya memuat satu nilai tunggal) dan ketiadaan kolom/baris yang berulang.",
            "execution": "Opsi A adalah 3NF, opsi D adalah 2NF. 1NF mensyaratkan nilai atomik."
        },
        "explanation": "Syarat 1NF adalah setiap kolom hanya memuat nilai atomik (tidak dapat dipecah lagi) dan tidak memiliki repeating groups/multi-valued attributes. Jawaban: C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-06",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "HTTP Response Status Codes",
        "type": "mcq",
        "questionHtml": "Ketika sebuah endpoint RESTful API berhasil membuat entitas sumber daya baru di database server melalui request `POST`, kode status HTTP standar yang paling tepat dikembalikan adalah...",
        "options": [
            {"key": "A", "text": "200 OK yang mengindikasikan keberhasilan umum pemrosesan request tanpa entitas baru."},
            {"key": "B", "text": "201 Created yang mengindikasikan entitas sumber daya baru telah berhasil dibuat di server."},
            {"key": "C", "text": "204 No Content yang mengindikasikan permintaan sukses tetapi respons tidak memiliki isi bodi."},
            {"key": "D", "text": "301 Moved Permanently yang mengalihkan URL request secara permanen ke lokasi endpoint baru."},
            {"key": "E", "text": "400 Bad Request yang mengindikasikan payload request tidak sesuai format validasi schema."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "HTTP SUCCESS STATUS CODES",
            "latex": "200 \\text{ (OK)}, \\quad 201 \\text{ (Created)}, \\quad 204 \\text{ (No Content)}",
            "legend": "• 200: Operasi standar berhasil<br>• 201: Resource berhasil dibuat (POST)<br>• 204: Berhasil tanpa return body (DELETE)"
        },
        "hints": {
            "concept": "HTTP status 201 Created secara spesifik dirancang untuk operasi pembuatan resource baru yang berhasil.",
            "execution": "200 adalah kesuksesan generik, 201 spesifik untuk created resource."
        },
        "explanation": "HTTP 201 Created adalah kode status standar RFC 7231 saat request POST sukses membuat resource baru di server. 200 adalah respons umum, 204 tanpa bodi respons. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-07",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Deklarasi Variabel JavaScript Modern",
        "type": "mcq",
        "questionHtml": "Perhatikan kode JavaScript modern berikut:\n```javascript\nconst maxCapacity = 100;\nmaxCapacity = 120;\n```\nApa yang akan terjadi pada lingkungan eksekusi JavaScript (runtime) saat baris kedua dieksekusi?",
        "options": [
            {"key": "A", "text": "Nilai maxCapacity berhasil diperbarui menjadi 120 secara mulus tanpa peringatan apapun."},
            {"key": "B", "text": "Terjadi TypeError: Assignment to constant variable karena nilai referensi const di-assign ulang."},
            {"key": "C", "text": "Terjadi SyntaxError saat fase kompilasi sebelum kode sempat dieksekusi oleh engine V8."},
            {"key": "D", "text": "Variabel maxCapacity otomatis diubah tipenya oleh engine menjadi variabel bertipe var global."},
            {"key": "E", "text": "Nilai variabel maxCapacity menjadi undefined karena konflik alokasi memori runtime V8."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "JS VARIABLE BINDING RULES",
            "latex": "\\text{const} \\implies \\text{Immutable Binding (Reassignment Forbidden)}",
            "legend": "• const: Block scope, no reassignment, temporal dead zone<br>• let: Block scope, mutable, temporal dead zone<br>• var: Function scope, hoisted"
        },
        "hints": {
            "concept": "Variabel yang dideklarasikan dengan const memiliki binding konstan yang tidak mengizinkan penugasan ulang (reassignment).",
            "execution": "Upaya mengubah nilai primitif variabel const akan memicu TypeError di runtime."
        },
        "explanation": "Pada JavaScript ES6+, variabel `const` tidak dapat di-assign ulang nilainya. Upaya me-reassign nilai pada identifier `const` akan memicu runtime error berupa `TypeError: Assignment to constant variable`. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-08",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Android Activity Lifecycle",
        "type": "mcq",
        "questionHtml": "Pada siklus hidup (lifecycle) Activity sistem operasi Android, callback method manakah yang pertama kali dipanggil saat activity mulai diciptakan dan bertugas menginisialisasi view serta layout UI?",
        "options": [
            {"key": "A", "text": "onStart() yang membuat activity mulai terlihat di layar pengguna tetapi belum dapat berinteraksi."},
            {"key": "B", "text": "onResume() yang menandakan activity berada di foreground dan siap menerima input interaksi."},
            {"key": "C", "text": "onCreate() yang menginisialisasi komponen dasar, data binding, dan memanggil setContentView()."},
            {"key": "D", "text": "onPause() yang dipanggil ketika activity kehilangan fokus utama akibat pop-up atau dialog."},
            {"key": "E", "text": "onRestart() yang memulihkan activity setelah sebelumnya berada pada status onStop."}
        ],
        "correctKey": "C",
        "formulaHud": {
            "title": "ANDROID ACTIVITY LIFECYCLE FLOW",
            "latex": "\\text{onCreate()} \\to \\text{onStart()} \\to \\text{onResume()} \\leftrightarrow \\text{onPause()} \\to \\text{onStop()} \\to \\text{onDestroy()}",
            "legend": "• onCreate: Inisialisasi awal & layout binding<br>• onResume: Interaktif di foreground<br>• onDestroy: Cleanup resource & memori"
        },
        "hints": {
            "concept": "Activity lifecycle diawali dengan onCreate(), di mana pengembang menempatkan inisialisasi view via setContentView().",
            "execution": "onCreate() dipanggil tepat sekali saat instance Activity dibangun."
        },
        "explanation": "`onCreate()` adalah callback pertama yang dieksekusi oleh sistem operasi Android saat Activity dibuat. Di method inilah layout XML dihubungkan menggunakan `setContentView()`. Jawaban: C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-09",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Game Loop Architecture",
        "type": "mcq",
        "questionHtml": "Dalam arsitektur engine gim modern, fungsi inti dari komponen Game Loop yang berjalan secara kontinu setiap frame adalah...",
        "options": [
            {"key": "A", "text": "Mengompilasi ulang seluruh source code gim secara real-time setiap kali pemain melakukan aksi."},
            {"key": "B", "text": "Menerima input pengguna, memperbarui kondisi logika objek dunia gim, dan merender tampilan grafis."},
            {"key": "C", "text": "Menghubungkan gim secara terus-menerus ke server basis data cloud untuk sinkronisasi leaderboard."},
            {"key": "D", "text": "Membersihkan alokasi memori RAM secara paksa setiap frame agar tidak terjadi fragmentasi heap."},
            {"key": "E", "text": "Memeriksa keaslian lisensi perangkat lunak gim dari store server sebelum aset dimuat ke GPU."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CLASSIC GAME LOOP PATTERN",
            "latex": "\\text{while}(\\text{running}) \\;\\{ \\text{processInput}(); \\; \\text{updateState}(\\Delta t); \\; \\text{renderView}(); \\}",
            "legend": "• Input: Keyboard, touch, controller event<br>• Update: Fisika, AI, collision, timer<br>• Render: Gambar scene ke frame buffer"
        },
        "hints": {
            "concept": "Game loop memiliki 3 tahapan siklis utama: Process Input -> Update Game State -> Render Output.",
            "execution": "Siklus ini dieksekusi berulang kali (misal 60 fps) untuk menjaga dunia game responsif."
        },
        "explanation": "Game Loop adalah jantung aplikasi gim yang berjalan berulang-ulang untuk: (1) membaca input pemain, (2) mengkalkulasi logika/fisika/AI (update), dan (3) menggambar scene ke layar (render). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-10",
        "subject": "rpl",
        "materi": "REKAYASA PEMROGRAMAN GIM",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Collision Detection (AABB)",
        "type": "mcq",
        "questionHtml": "Teknik deteksi tabrakan (collision detection) 2D yang menggunakan kotak pembatas sejajar sumbu koordinat tanpa rotasi dikenal dengan istilah...",
        "options": [
            {"key": "A", "text": "Raycasting yang menembakkan berkas garis vektor lurus untuk mengukur jarak objek target."},
            {"key": "B", "text": "Axis-Aligned Bounding Box (AABB) yang membandingkan koordinat batas minimum dan maksimum."},
            {"key": "C", "text": "Oriented Bounding Box (OBB) yang menggunakan pemisahan sumbu SAT dengan sudut rotasi dinamis."},
            {"key": "D", "text": "Convex Hull Detection yang menghitung poligon terluar yang membungkus seluruh vertex objek."},
            {"key": "E", "text": "Spatial Hashing yang membagi ruang dunia gim ke dalam grid sel matriks berindeks terpisah."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "AABB COLLISION FORMULA",
            "latex": "\\text{overlap} = (x_{1\\text{min}} \\le x_{2\\text{max}}) \\land (x_{1\\text{max}} \\ge x_{2\\text{min}}) \\land (y_{1\\text{min}} \\le y_{2\\text{max}}) \\land (y_{1\\text{max}} \\ge y_{2\\text{min}})",
            "legend": "• AABB: Efisien, komputasi murah (hanya perbandingan angka aljabar sederhana)<br>• Sumbu sejajar X dan Y (tanpa rotasi sudut)"
        },
        "hints": {
            "concept": "Axis-Aligned Bounding Box (AABB) adalah metode deteksi tabrakan kotak non-rotasi paling mendasar.",
            "execution": "Perhatikan frasa 'kotak pembatas sejajar sumbu koordinat' yang merupakan terjemahan dari Axis-Aligned Bounding Box."
        },
        "explanation": "AABB (Axis-Aligned Bounding Box) adalah algoritma deteksi tabrakan yang mengasumsikan batas kotak objek selalu sejajar dengan sumbu X dan Y dunia gim, menjadikannya sangat cepat dikomputasi. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-11",
        "subject": "rpl",
        "materi": "DESAIN UI/UX & AKSESIBILITAS",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "10 Nielsen Usability Heuristics",
        "type": "mcq",
        "questionHtml": "Ketika sebuah aplikasi menampilkan ikon progress bar atau animasi loading saat memproses pengunggahan file pengguna, prinsip usability heuristic Jakob Nielsen manakah yang sedang dipenuhi?",
        "options": [
            {"key": "A", "text": "Match between system and real world dengan menggunakan metafora objek kehidupan nyata."},
            {"key": "B", "text": "Visibility of system status dengan selalu memberi tahu pengguna kondisi yang sedang berlangsung."},
            {"key": "C", "text": "User control and freedom dengan menyediakan tombol darurat undo untuk membatalkan aksi."},
            {"key": "D", "text": "Error prevention dengan mencegah kesalahan pengguna terjadi sebelum aksi dieksekusi."},
            {"key": "E", "text": "Flexibility and efficiency of use dengan menyediakan shortcut bagi pengguna mahir."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "NIELSEN HEURISTIC #1",
            "latex": "\\text{Feedback Time} < 100\\text{ms (Instant)}, \\quad < 1\\text{s (Flow)}, \\quad > 10\\text{s (Show Progress)}",
            "legend": "• Heuristic 1: Visibility of system status<br>• Memberikan umpan balik visual tepat waktu kepada pengguna"
        },
        "hints": {
            "concept": "Heuristik pertama Nielsen menyatakan sistem harus selalu menginformasikan status kerjanya kepada user melalui feedback yang wajar dan tepat waktu.",
            "execution": "Progress bar dan indikator loading adalah contoh klasik pemenuhan status sistem."
        },
        "explanation": "Prinsip 'Visibility of system status' mengharuskan sistem selalu memberi tahu pengguna mengenai apa yang sedang terjadi melalui umpan balik yang sesuai dalam waktu yang wajar (seperti loading bar). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-12",
        "subject": "rpl",
        "materi": "DESAIN UI/UX & AKSESIBILITAS",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Standar Kontras Warna WCAG",
        "type": "mcq",
        "questionHtml": "Berdasarkan pedoman aksesibilitas web Web Content Accessibility Guidelines (WCAG) 2.1 level AA, rasio kontras minimum antara warna teks normal dengan latar belakangnya adalah sebesar...",
        "options": [
            {"key": "A", "text": "2.0:1 yang merupakan standar rasio kontras minimum bagi elemen dekoratif non-teks antarmuka."},
            {"key": "B", "text": "3.0:1 yang merupakan standar rasio kontras untuk teks berukuran besar (large text minimal 18pt)."},
            {"key": "C", "text": "4.5:1 yang merupakan standar rasio kontras minimum untuk teks normal agar terbaca dengan jelas."},
            {"key": "D", "text": "7.0:1 yang merupakan standar rasio kontras ketat level AAA untuk keterbacaan tingkat tinggi."},
            {"key": "E", "text": "10.0:1 yang merupakan rasio kontras ekstrim monokrom hitam putih murni tanpa gradasi."}
        ],
        "correctKey": "C",
        "formulaHud": {
            "title": "WCAG CONTRAST RATIO SPECIFICATION",
            "latex": "\\text{Ratio} = \\frac{L_1 + 0.05}{L_2 + 0.05} \\ge 4.5:1 \\quad (\\text{Level AA Normal Text})",
            "legend": "• Level AA Normal Text: Minimal 4.5:1<br>• Level AA Large Text (>=18pt/14pt bold): Minimal 3.0:1<br>• Level AAA Normal Text: Minimal 7.0:1"
        },
        "hints": {
            "concept": "WCAG 2.1 Level AA mensyaratkan rasio kontras 4.5:1 untuk teks normal dan 3:1 untuk teks besar.",
            "execution": "Pilihlah angka 4.5:1 untuk teks biasa pada level AA."
        },
        "explanation": "WCAG 2.1 Level AA menetapkan ambang batas rasio kontras minimal 4.5:1 untuk teks reguler. Untuk teks besar (18pt atau 14pt tebal), batasnya adalah 3:1. Jawaban: C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-13",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Lisensi Perangkat Lunak Open Source",
        "type": "mcq",
        "questionHtml": "Lisensi perangkat lunak open source manakah yang bersifat 'permissive' (sangat longgar) dan mengizinkan kode digunakan kembali dalam proyek komersial tertutup (proprietary) hanya dengan menyertakan pemberitahuan hak cipta aslinya?",
        "options": [
            {"key": "A", "text": "GNU General Public License (GPL) yang menerapkan klausul copyleft ketat pada proyek turunan."},
            {"key": "B", "text": "MIT License yang memberikan kebebasan penuh penggunaan komersial dengan mencantumkan lisensi."},
            {"key": "C", "text": "Affero General Public License (AGPL) yang mewajibkan rilis source code layanan berbasis jaringan."},
            {"key": "D", "text": "Creative Commons Non-Commercial (CC-NC) yang melarang keras pemanfaatan untuk tujuan profit."},
            {"key": "E", "text": "End User License Agreement (EULA) yang merupakan perjanjian pembatasan lisensi hak milik vendor."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SOFTWARE LICENSE CATEGORIES",
            "latex": "\\text{Open Source} = \\text{Permissive (MIT/BSD/Apache)} \\cup \\text{Copyleft (GPL/AGPL)}",
            "legend": "• MIT: Permissive, komersial diizinkan, no copyleft<br>• GPL: Viral copyleft, turunan wajib open source GPL"
        },
        "hints": {
            "concept": "Lisensi MIT adalah lisensi permisif populer yang memungkinkan pengembang memakai kode untuk aplikasi komersial tanpa kewajiban membuka source code.",
            "execution": "GPL mewajibkan copyleft, sedangkan MIT bersifat permisif."
        },
        "explanation": "Lisensi MIT adalah jenis lisensi permisif yang memberikan izin bagi siapa pun untuk menggunakan, memodifikasi, dan mendistribusikan kode, termasuk untuk keperluan komersial tertutup, dengan syarat tetap menyertakan hak cipta dan disclaimer asli. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-14",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "K3LH & Ergonomi Kerja IT",
        "type": "mcq",
        "questionHtml": "Untuk mencegah kelelahan mata (Computer Vision Syndrome) bagi programmer yang menatap monitor berjam-jam, aturan ergonomi '20-20-20' menganjurkan agar...",
        "options": [
            {"key": "A", "text": "Setiap 20 jam bekerja, istirahatlah selama 20 menit penuh sambil mengonsumsi 20 mililiter air mineral."},
            {"key": "B", "text": "Setiap 20 menit menatap layar, alihkan pandangan ke objek berjarak 20 kaki (6 meter) selama 20 detik."},
            {"key": "C", "text": "Mengatur tingkat kecerahan layar monitor pada angka 20% dengan sudut kemiringan tepat 20 derajat."},
            {"key": "D", "text": "Setiap 20 baris kode program yang ditulis, lakukan peregangan jari tangan sebanyak 20 kali repetisi."},
            {"key": "E", "text": "Menjaga jarak mata dari layar kaca monitor sejauh tepat 20 sentimeter dengan sudut pandang 20 derajat."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "THE 20-20-20 RULE FOR EYE ERGONOMICS",
            "latex": "20\\text{ minutes work} \\implies \\text{Look at } 20\\text{ feet distant object} \\implies \\text{for } 20\\text{ seconds}",
            "legend": "• Mencegah Computer Vision Syndrome (CVS)<br>• Melemaskan otot silier lensa mata"
        },
        "hints": {
            "concept": "Rule 20-20-20 adalah rekomendasi medis ergonomi: setiap 20 menit, pandang objek sejauh 20 kaki selama 20 detik.",
            "execution": "20 feet setara dengan 6 meter."
        },
        "explanation": "Aturan ergonomi mata 20-20-20 menyatakan bahwa setiap 20 menit bekerja di depan komputer, istirahatkan mata dengan memandang objek berjarak minimal 20 kaki (sekitar 6 meter) selama minimal 20 detik untuk mengistirahatkan otot fokus mata. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-15",
        "subject": "rpl",
        "materi": "PENGUJIAN PERANGKAT LUNAK (QA)",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Pengujian Black-Box vs White-Box",
        "type": "mcq",
        "questionHtml": "Perbedaan fundamental antara metode pengujian perangkat lunak Black-Box Testing dan White-Box Testing terletak pada...",
        "options": [
            {"key": "A", "text": "Pengujian black-box hanya dapat dilakukan oleh komputer secara otomatis tanpa keterlibatan manusia."},
            {"key": "B", "text": "Black-box menguji fungsi berdasarkan input-output spesifikasi, sedangkan white-box menguji alur kode internal."},
            {"key": "C", "text": "White-box testing hanya menguji antarmuka visual grafis pengguna tanpa memeriksa basis data server."},
            {"key": "D", "text": "Black-box mensyaratkan penguji memiliki akses penuh terhadap diagram logika kode sumber aplikasi."},
            {"key": "E", "text": "White-box testing hanya dijalankan pada tahapan pengujian penerimaan pengguna akhir (User Acceptance Test)."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "TESTING PARADIGMS COMPARISON",
            "latex": "\\text{Black-Box} \\colon f(x) \\to y \\quad \\text{vs} \\quad \\text{White-Box} \\colon \\text{Control Flow Graph & Branch}",
            "legend": "• Black-Box: Uji spesifikasi & fungsional (tanpa lihat kode)<br>• White-Box: Uji struktur, percabangan, & jalur logika internal"
        },
        "hints": {
            "concept": "Black-box menguji 'apa yang dilakukan sistem' dari luar (spesifikasi), sedangkan white-box menguji 'bagaimana sistem bekerja' di dalam (struktur kode).",
            "execution": "Black box = tanpa akses kode sumber; White box = dengan analisis kode sumber."
        },
        "explanation": "Black-Box Testing berfokus pada pengujian fungsionalitas berdasarkan spesifikasi kebutuhan tanpa melihat struktur kode internal, sedangkan White-Box Testing menganalisis struktur internal, alur percabangan, dan logika kode sumber program. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-16",
        "subject": "rpl",
        "materi": "ALGORITMA & PEMROGRAMAN TERSTRUKTUR",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Struktur Kontrol Percabangan",
        "type": "mcq",
        "questionHtml": "Perhatikan potongan kode Python berikut:\n```python\nscore = 85\nif score >= 90:\n    grade = \"A\"\nelif score >= 80:\n    grade = \"B\"\nelif score >= 70:\n    grade = \"C\"\nelse:\n    grade = \"D\"\nprint(grade)\n```\nOutput nilai variabel `grade` yang dicetak pada terminal adalah...",
        "options": [
            {"key": "A", "text": "A karena evaluasi kondisi percabangan selalu memilih nilai grade tertinggi yang tersedia."},
            {"key": "B", "text": "B karena nilai 85 memenuhi kondisi elif kedua score >= 80 dan eksekusi blok percabangan berakhir."},
            {"key": "C", "text": "C karena kondisi 85 juga secara matematis lebih besar sama dengan 70 pada evaluasi ketiga."},
            {"key": "D", "text": "D karena struktur percabangan mengalami runtime fallback ke blok klausa else default."},
            {"key": "E", "text": "Terjadi error kompilasi karena variabel grade dideklarasikan berulang di dalam blok if."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CONDITIONAL CONTROL FLOW",
            "latex": "85 \\ge 90 \\; (\\text{False}) \\implies 85 \\ge 80 \\; (\\text{True}) \\implies \\text{Execute & Exit Branch}",
            "legend": "• if-elif-else mengeksekusi blok pertama yang bernilai True lalu keluar dari seluruh rantai seleksi"
        },
        "hints": {
            "concept": "Dalam struktur if-elif-else, begitu sebuah kondisi terpenuhi (True), blok tersebut dieksekusi dan sisa kondisi di bawahnya diabaikan.",
            "execution": "Kondisi score >= 90 bernilai False. Kondisi score >= 80 bernilai True, sehingga grade = 'B' dieksekusi."
        },
        "explanation": "Karena 85 < 90 (False), evaluasi berlanjut ke `elif score >= 80`. Karena 85 >= 80 bernilai True, maka `grade = 'B'` dijalankan dan rantai percabangan selesai. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-17",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Git Version Control Dasar",
        "type": "mcq",
        "questionHtml": "Perintah Git yang digunakan untuk memindahkan perubahan file dari working directory lokal ke dalam staging area sebelum dilakukan commit adalah...",
        "options": [
            {"key": "A", "text": "git commit -m yang menyimpan snapshot perubahan secara permanen ke repositori lokal."},
            {"key": "B", "text": "git push origin yang mengunggah riwayat commit lokal ke repositori remote di cloud."},
            {"key": "C", "text": "git add yang mendaftarkan perubahan file yang dipilih ke dalam staging area."},
            {"key": "D", "text": "git checkout yang beralih antar branch kerja atau membatalkan perubahan lokal."},
            {"key": "E", "text": "git status yang menampilkan status pelacakan file pada direktori kerja saat ini."}
        ],
        "correctKey": "C",
        "formulaHud": {
            "title": "GIT WORKFLOW STAGES",
            "latex": "\\text{Working Directory} \\xrightarrow{\\text{git add}} \\text{Staging Area} \\xrightarrow{\\text{git commit}} \\text{Local Repo}",
            "legend": "• Working directory: Berkas diubah di editor<br>• Staging area (Index): Berkas siap di-commit<br>• Repository: Riwayat permanen"
        },
        "hints": {
            "concept": "Tiga zona Git: Working Directory -> Staging Area -> Commit History.",
            "execution": "git add digunakan untuk memindahkan perubahan ke Staging Area."
        },
        "explanation": "Perintah `git add <nama_file>` atau `git add .` berfungsi menambahkan file dari working directory ke staging area (index) agar siap disertakan dalam commit berikutnya. Jawaban: C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-18",
        "subject": "rpl",
        "materi": "BASIS DATA RELASIONAL & SQL",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "SQL Agregasi & Klausa WHERE",
        "type": "mcq",
        "questionHtml": "Perhatikan query SQL sederhana berikut:\n```sql\nSELECT COUNT(*) AS total_produk\nFROM produk\nWHERE kategori = 'Elektronik';\n```\nFungsi agregasi `COUNT(*)` pada query di atas menghasilkan...",
        "options": [
            {"key": "A", "text": "Jumlah akumulasi total nominal harga seluruh produk dengan kategori Elektronik di tabel."},
            {"key": "B", "text": "Jumlah total baris (rekaman) produk yang memenuhi kriteria kategori 'Elektronik'."},
            {"key": "C", "text": "Rata-rata jumlah stok unit barang yang termasuk dalam klasifikasi produk Elektronik."},
            {"key": "D", "text": "Daftar nama seluruh produk barang Elektronik yang diurutkan secara berurutan abjad."},
            {"key": "E", "text": "Nilai transaksi harga tertinggi di antara produk-produk dalam kategori Elektronik."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SQL AGGREGATE FUNCTIONS",
            "latex": "\\text{COUNT}(*) \\to \\text{Row Count}, \\quad \\text{SUM}(c) \\to \\text{Total}, \\quad \\text{AVG}(c) \\to \\text{Mean}",
            "legend": "• COUNT(*): Menghitung seluruh baris termasuk nilai NULL<br>• SUM: Akumulasi nilai angka<br>• AVG: Rata-rata nilai"
        },
        "hints": {
            "concept": "Fungsi COUNT(*) menghitung banyaknya baris rekaman yang lolos filter klausul WHERE.",
            "execution": "Untuk total harga digunakan SUM(), rata-rata AVG(), dan jumlah baris COUNT()."
        },
        "explanation": "Fungsi `COUNT(*)` menghitung banyaknya jumlah baris rekaman yang dihasilkan oleh query setelah disaring oleh klausul `WHERE kategori = 'Elektronik'`. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-19",
        "subject": "rpl",
        "materi": "PEMROGRAMAN WEB & API",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Format Data Pertukaran JSON",
        "type": "mcq",
        "questionHtml": "Dalam ekosistem komunikasi data web modern dan REST API, singkatan resmi serta karakteristik utama dari format data JSON adalah...",
        "options": [
            {"key": "A", "text": "Java Script Object Notation yang merupakan format pertukaran data teks ringan berbasis key-value."},
            {"key": "B", "text": "Java Standard Output Network yang merupakan protokol transfer data biner antar server."},
            {"key": "C", "text": "Joint Security Organization Network yang mengatur enkripsi paket pada protokol HTTPS."},
            {"key": "D", "text": "Java Source Object Network yang berfungsi mengompilasi file bytecode di browser client."},
            {"key": "E", "text": "JavaScript Operational Node yang mengelola thread eksekusi multi-core pada runtime Node.js."}
        ],
        "correctKey": "A",
        "formulaHud": {
            "title": "JSON DATA STRUCTURE",
            "latex": "\\text{JSON} = \\{ \\text{\"key\"} \\colon \\text{value} \\}, \\quad \\text{where value} \\in \\{ \\text{string, number, bool, array, object, null} \\}",
            "legend": "• Format berbasis teks, human-readable, language-independent"
        },
        "hints": {
            "concept": "JSON singkatan dari JavaScript Object Notation, format teks standar untuk representasi struktur data berpasangan key-value.",
            "execution": "JSON mudah dibaca manusia dan didukung oleh hampir semua bahasa pemrograman modern."
        },
        "explanation": "JSON (JavaScript Object Notation) adalah format standar pertukaran data terbuka berbasis teks yang ringan, mudah dibaca manusia dan mesin, serta independen dari bahasa pemrograman. Jawaban: A.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-20",
        "subject": "rpl",
        "materi": "PENGUJIAN PERANGKAT LUNAK (QA)",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Tingkatan Pengujian Unit Test",
        "type": "mcq",
        "questionHtml": "Dalam piramida pengujian perangkat lunak, tingkatan pengujian yang berfokus menguji unit kode terkecil (seperti method atau fungsi tunggal) secara terisolasi dinamakan...",
        "options": [
            {"key": "A", "text": "System Testing yang menguji keseluruhan sistem perangkat lunak secara utuh end-to-end."},
            {"key": "B", "text": "Integration Testing yang memverifikasi komunikasi dan interaksi antar beberapa modul komponen."},
            {"key": "C", "text": "Unit Testing yang memvalidasi kebenaran logika fungsi atau method terkecil secara terisolasi."},
            {"key": "D", "text": "Acceptance Testing yang dilakukan oleh pengguna akhir untuk memastikan kesesuaian kebutuhan bisnis."},
            {"key": "E", "text": "Performance Testing yang mengukur daya tahan dan waktu respons server di bawah beban tinggi."}
        ],
        "correctKey": "C",
        "formulaHud": {
            "title": "TEST PYRAMID HIERARCHY",
            "latex": "\\text{E2E / UI Test} \\; (10\\%) \\to \\text{Integration Test} \\; (20\\%) \\to \\text{Unit Test} \\; (70\\%)",
            "legend": "• Unit: Paling banyak, cepat, menguji fungsi individual<br>• Integration: Uji gabungan modul/DB/API<br>• E2E: Uji alur pengguna menyeluruh"
        },
        "hints": {
            "concept": "Pengujian pada level terkecil komponen perangkat lunak (fungsi, prosedur, class method) disebut unit test.",
            "execution": "Piramida pengujian menempatkan unit test di lapisan terbawah karena paling cepat dan terisolasi."
        },
        "explanation": "Unit Testing adalah pengujian terhadap bagian terkecil dari perangkat lunak (seperti fungsi atau method individual) secara terisolasi dari dependensi luar. Jawaban: C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-21",
        "subject": "rpl",
        "materi": "ALGORITMA & PEMROGRAMAN TERSTRUKTUR",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Struktur Data Linier (Array & List)",
        "type": "mcq",
        "questionHtml": "Karakteristik mendasar dari struktur data Array satu dimensi statis dalam memori komputer adalah...",
        "options": [
            {"key": "A", "text": "Dapat menampung berbagai tipe data heterogen tanpa batasan kapasitas alokasi awal."},
            {"key": "B", "text": "Menyimpan elemen-elemen bertipe sama dalam lokasi blok memori yang berurutan (kontigu)."},
            {"key": "C", "text": "Elemen hanya dapat diakses secara sekuensial dari elemen pertama hingga terakhir."},
            {"key": "D", "text": "Alokasi ukuran panjang array otomatis bertambah saat terjadi penambahan data baru."},
            {"key": "E", "text": "Setiap elemen memiliki pointer referensi eksplisit ke alamat memori elemen berikutnya."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "ARRAY MEMORY ADDRESS CALCULATION",
            "latex": "\\text{Address}(A[i]) = \\text{BaseAddress} + (i \\times \\text{ElementSize})",
            "legend": "• Akses langsung konstan: $O(1)$ random access time<br>• Memori kontigu (berurutan tanpa jeda)"
        },
        "hints": {
            "concept": "Array statis mengalokasikan memori secara kontigu (berdampingan) dan memiliki ukuran tetap dengan tipe data homogen.",
            "execution": "Lokasi memori kontigu memungkinkan akses acak $O(1)$ via indeks."
        },
        "explanation": "Array menyimpan elemen-elemen bertipe data sama pada blok memori yang berurutan (kontigu), memungkinkan akses instan $O(1)$ menggunakan indeks. Pilihan E adalah karakteristik Linked List. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-22",
        "subject": "rpl",
        "materi": "PEMROGRAMAN APLIKASI BERGERAK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Komponen UI & Layouting Android",
        "type": "mcq",
        "questionHtml": "Dalam perancangan antarmuka Android menggunakan XML, jenis layout yang menyusun elemen tampilan (views) secara berurutan dalam satu arah, baik horizontal maupun vertikal, adalah...",
        "options": [
            {"key": "A", "text": "ConstraintLayout yang menyusun view berdasarkan hubungan pembatas relatif terhadap elemen lain."},
            {"key": "B", "text": "LinearLayout yang menata widget anak secara berurutan dalam satu orientasi garis lurus."},
            {"key": "C", "text": "FrameLayout yang menumpuk view anak di atas view lainnya pada sudut kiri atas layar."},
            {"key": "D", "text": "TableLayout yang menyusun elemen ke dalam baris dan kolom kisi-kisi matriks kaku."},
            {"key": "E", "text": "RelativeLayout yang menempatkan view berdasarkan posisi relatif terhadap view saudaranya."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "ANDROID LAYOUT ATTRIBUTES",
            "latex": "\\text{android:orientation} = \\text{\"vertical\"} \\mid \\text{\"horizontal\"}",
            "legend": "• LinearLayout: Penataan linier 1 arah<br>• ConstraintLayout: Fleksibel, flat hierarchy, performa tinggi"
        },
        "hints": {
            "concept": "LinearLayout menggunakan atribut android:orientation untuk menyusun komponen secara vertikal atau horizontal.",
            "execution": "ConstraintLayout menggunakan constraints, sedangkan LinearLayout menata dalam satu garis lurus."
        },
        "explanation": "LinearLayout adalah ViewGroup yang mengatur komponen anak-anaknya dalam satu baris (horizontal) atau satu kolom (vertikal) sesuai atribut `android:orientation`. Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-23",
        "subject": "rpl",
        "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Konsep Abstraksi & Interface",
        "type": "mcq",
        "questionHtml": "Pernyataan yang BENAR mengenai perbedaan antara Interface dan Abstract Class dalam bahasa Java murni adalah...",
        "options": [
            {"key": "A", "text": "Sebuah kelas konkret di Java diperbolehkan mewarisi lebih dari satu superclass abstrak."},
            {"key": "B", "text": "Interface hanya mendefinisikan kontrak tanpa bisa memiliki method dengan implementasi default."},
            {"key": "C", "text": "Sebuah kelas konkret dapat mengimplementasikan beberapa interface sekaligus (multiple interfaces)."},
            {"key": "D", "text": "Abstract class tidak dapat memiliki constructor untuk menginisialisasi atribut instansinya."},
            {"key": "E", "text": "Interface dapat diinstansiasi secara langsung menjadi objek mandiri dengan kata kunci new."}
        ],
        "correctKey": "C",
        "formulaHud": {
            "title": "JAVA MULTIPLE INHERITANCE THROUGH INTERFACES",
            "latex": "\\text{class } C \\text{ extends } A \\text{ implements } I_1, I_2, I_3",
            "legend": "• Java mendukung single class inheritance (extends 1 class)<br>• Java mendukung multiple interface implementation (implements banyak interface)"
        },
        "hints": {
            "concept": "Java tidak mengizinkan multiple inheritance untuk class, tetapi mengizinkan implementasi banyak interface sekaligus pada satu kelas.",
            "execution": "Pilihlah fakta bahwa class Java dapat mengimplementasikan banyak interface."
        },
        "explanation": "Di Java, sebuah kelas hanya boleh mewarisi satu kelas induk (single inheritance), tetapi dapat mengimplementasikan banyak interface sekaligus (`implements InterfaceA, InterfaceB`). Jawaban: C.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-24",
        "subject": "rpl",
        "materi": "K3LH & HAKI PERANGKAT LUNAK",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Hukum Digital & UU ITE",
        "type": "mcq",
        "questionHtml": "Tindakan mengakses sistem komputer milik pihak lain tanpa hak atau melawan hukum dengan sengaja melanggar sistem pengamanan merupakan pelanggaran hukum digital yang diatur dalam Undang-Undang ITE pada pasal...",
        "options": [
            {"key": "A", "text": "Pasal tentang penyebaran informasi hoaks dan berita bohong yang menyesatkan publik."},
            {"key": "B", "text": "Pasal 30 tentang akses ilegal (illegal access) terhadap sistem komputer atau jaringan orang lain."},
            {"key": "C", "text": "Pasal tentang pencemaran nama baik dan penghinaan personal melalui media sosial online."},
            {"key": "D", "text": "Pasal tentang transaksi perdagangan elektronik dan pendaftaran penyelenggara sistem komersial."},
            {"key": "E", "text": "Pasal tentang perlindungan hak cipta konten multimedia yang diunggah ke portal streaming."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "CYBER LAW FRAMEWORK (UU ITE)",
            "latex": "\\text{Pasal 30 UU ITE} \\implies \\text{Illegal Access to Computer System / Data}",
            "legend": "• Ayat 1: Akses tanpa hak<br>• Ayat 2: Akses untuk memperoleh info/dokumen<br>• Ayat 3: Membobol sistem pengamanan (cracking)"
        },
        "hints": {
            "concept": "Pasal 30 UU ITE mengatur tindak pidana akses ilegal (illegal access) ke komputer/jaringan orang lain dengan melanggar pengamanan.",
            "execution": "Ingat konsep Illegal Access = Pasal 30 UU ITE."
        },
        "explanation": "Pasal 30 UU ITE secara tegas melarang perbuatan setiap orang yang dengan sengaja dan tanpa hak atau melawan hukum mengakses komputer dan/atau sistem elektronik milik orang lain dengan cara apa pun (illegal access). Jawaban: B.",
        "isDiagnostic": False
    },
    {
        "id": "rpl-lat-e-25",
        "subject": "rpl",
        "materi": "PROSES BISNIS & SDLC",
        "mode": "latihan",
        "difficulty": "easy",
        "topic": "Model SDLC Waterfall vs Agile",
        "type": "mcq",
        "questionHtml": "Situasi proyek pengembangan perangkat lunak manakah yang PALING tepat menggunakan model siklus hidup Waterfall tradisional dibandingkan Agile?",
        "options": [
            {"key": "A", "text": "Aplikasi rintisan (startup) baru di mana fitur dan target pasar masih dalam tahap eksperimen cepat."},
            {"key": "B", "text": "Sistem kendali kedirgantaraan dengan spesifikasi kebutuhan yang sudah fix, kaku, dan regulasi ketat."},
            {"key": "C", "text": "Game online mobile yang membutuhkan pembaruan konten dan penyesuaian event berkala tiap minggu."},
            {"key": "D", "text": "Portal e-commerce ritel yang ingin sering merilis fitur baru berdasarkan tren belanja konsumen."},
            {"key": "E", "text": "Sistem media sosial interaktif yang terus mengembangkan algoritma rekomendasi berdasarkan feedback."}
        ],
        "correctKey": "B",
        "formulaHud": {
            "title": "SDLC MODEL SELECTION MATRIX",
            "latex": "\\text{Requirements Clarity} \\land \\text{High Regulation} \\implies \\text{Waterfall}",
            "legend": "• Waterfall: Spesifikasi jelas, stabil, minim perubahan, dokumentasi ketat<br>• Agile: Dinamis, eksperimental, feedback cepat"
        },
        "hints": {
            "concept": "Model Waterfall sangat cocok untuk sistem dengan persyaratan yang telah pasti dan tidak berubah-ubah serta memiliki standar keselamatan/regulasi ketat.",
            "execution": "Sistem kedirgantaraan atau alat medis memiliki spesifikasi baku yang fatal jika diubah di tengah jalan."
        },
        "explanation": "Model Waterfall ideal untuk proyek berskala kritis dengan spesifikasi kebutuhan yang sudah pasti, jelas, tidak boleh berubah di tengah jalan, dan memiliki standar dokumentasi ketat (seperti sistem kedirgantaraan, militer, atau perangkat medis). Jawaban: B.",
        "isDiagnostic": False
    }
]

print(f"Loaded {len(EASY_QUESTIONS)} easy questions.")
