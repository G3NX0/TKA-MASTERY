window.TKA_RPL_QUESTIONS = [
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
      {
        "key": "A",
        "text": "Product Owner yang menyusun prioritas backlog dan mendefinisikan kriteria bisnis."
      },
      {
        "key": "B",
        "text": "Scrum Master yang memfasilitasi daily standup dan menghilangkan hambatan kerja tim."
      },
      {
        "key": "C",
        "text": "Lead Developer yang merancang arsitektur kode dan mengawasi implementasi basis data."
      },
      {
        "key": "D",
        "text": "Quality Assurance yang memverifikasi acceptance criteria dan menjalankan pengujian."
      },
      {
        "key": "E",
        "text": "Project Sponsor yang mendanai inisiatif perangkat lunak dan menyetujui anggaran."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SCRUM ARTIFACTS & RESPONSIBILITIES",
      "latex": "\\text{Product Backlog} \\xrightarrow{\\text{Sprint Planning}} \\text{Sprint Backlog} \\to \\text{Increment}",
      "legend": "• Product Owner: Value maximizer & backlog owner<br>• Scrum Master: Process coach & impediment remover<br>• Dev Team: Increment builder"
    },
    "hints": {
      "concept": "Scrum membagi 3 peran inti: Product Owner (kelola backlog & nilai bisnis), Scrum Master (fasilitasi proses), dan Development Team (rekayasa teknis).",
      "execution": "Pilihlah peran yang fokus pada visi produk dan prioritas backlog bisnis, yaitu Product Owner."
    },
    "explanation": "Product Owner bertanggung jawab mengoptimalkan nilai produk dan mengelola Product Backlog secara berkesinambungan. Pilihan B adalah peran Scrum Master, sedangkan C dan D adalah tim pengembang teknis. Jawaban: A.",
    "isDiagnostic": true
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
      {
        "key": "A",
        "text": "Mengizinkan semua kelas dalam package yang sama mengakses nilai variabel saldo secara langsung."
      },
      {
        "key": "B",
        "text": "Mencegah variabel saldo diakses atau dimodifikasi langsung secara sembarangan dari luar kelas."
      },
      {
        "key": "C",
        "text": "Mempercepat proses alokasi memori runtime saat objek kelas RekeningBank diinstansiasi oleh JVM."
      },
      {
        "key": "D",
        "text": "Membuat variabel saldo dapat diwariskan secara otomatis tanpa pembatasan ke seluruh subclass turunan."
      },
      {
        "key": "E",
        "text": "Mengharuskan JVM menganggap variabel saldo sebagai konstanta mutlak yang nilainya tidak dapat diubah."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DATA HIDING & ENKAPSULASI",
      "latex": "\\text{Class} \\{ \\text{private attribute} + \\text{public getter/setter} \\}",
      "legend": "• private: Akses eksklusif dalam kelas deklarasi<br>• protected: Akses dalam package & turunan subclass<br>• public: Akses global tanpa restriksi"
    },
    "hints": {
      "concept": "Enkapsulasi menyembunyikan data internal objek (data hiding) menggunakan modifier private dan menyediakan gerbang terkontrol melalui public method.",
      "execution": "Modifier private memastikan integritas state objek agar tidak diubah secara langsung dari kode eksternal."
    },
    "explanation": "Modifier `private` menerapkan prinsip enkapsulasi (data hiding) agar atribut tidak dapat diakses atau diubah langsung dari luar kelas, melainkan melalui method perantara seperti getter atau setter. Jawaban: B.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "implements yang digunakan saat mendeklarasikan adopsi kontrak interface abstrak."
      },
      {
        "key": "B",
        "text": "inherits yang digunakan secara eksplisit dalam pewarisan kelas turunan Java modern."
      },
      {
        "key": "C",
        "text": "extends yang digunakan untuk memperluas fungsionalitas dari superclass induk."
      },
      {
        "key": "D",
        "text": "super yang digunakan untuk mereferensikan instance objek superclass pada constructor."
      },
      {
        "key": "E",
        "text": "instanceof yang digunakan untuk memeriksa kesesuaian tipe objek pada waktu runtime."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "SELECT, INSERT, UPDATE, dan DELETE yang digunakan untuk manipulasi data baris.     "
      },
      {
        "key": "B",
        "text": "GRANT, REVOKE, DENY, dan AUDIT yang digunakan untuk pengelolaan hak akses otorisasi data."
      },
      {
        "key": "C",
        "text": "COMMIT, ROLLBACK, SAVEPOINT, dan RELEASE yang digunakan untuk mengontrol siklus transaksi ACID."
      },
      {
        "key": "D",
        "text": "CREATE, ALTER, DROP, dan TRUNCATE yang digunakan untuk mendefinisikan skema struktur tabel."
      },
      {
        "key": "E",
        "text": "MERGE, UPSERT, REPLACE, dan BULK LOAD yang digunakan untuk sinkronisasi rekaman basis data."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "SQL COMMAND TAXONOMY",
      "latex": "\\text{SQL} = \\text{DDL} \\cup \\text{DML} \\cup \\text{DCL} \\cup \\text{TCL}",
      "legend": "• DDL (Struktur): CREATE, ALTER, DROP, TRUNCATE<br>• DML (Data): SELECT, INSERT, UPDATE, DELETE<br>• DCL (Hak Akses): GRANT, REVOKE<br>• TCL (Transaksi): COMMIT, ROLLBACK"
    },
    "hints": {
      "concept": "DDL (Data Definition Language) mendefinisikan dan memodifikasi struktur skema tabel, bukan isi data rekaman.",
      "execution": "Carilah opsi yang memuat perintah pembentukan dan penghapusan tabel: CREATE, ALTER, DROP."
    },
    "explanation": "DDL (Data Definition Language) mencakup perintah yang mengelola struktur/skema database: `CREATE`, `ALTER`, `DROP`, dan `TRUNCATE`. Pilihan A adalah DML, pilihan B adalah DCL, dan C adalah TCL. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Seluruh atribut non-kunci primer tidak memiliki ketergantungan transitif terhadap atribut lain."
      },
      {
        "key": "B",
        "text": "Tabel telah memiliki foreign key yang terhubung secara referensial ke tabel induk lain."
      },
      {
        "key": "C",
        "text": "Semua atribut non-kunci bergantung secara fungsional penuh pada primary key komposit."
      },
      {
        "key": "D",
        "text": "Setiap baris data telah diurutkan secara fisik berdasarkan nilai indeks clustered B-Tree."
      },
      {
        "key": "E",
        "text": "Setiap kolom bernilai atomik dan tidak terdapat kelompok data berulang (repeating groups)."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TAHAPAN NORMALISASI DATA",
      "latex": "\\text{Unnormalized} \\xrightarrow{1\\text{NF}} \\text{Atomik} \\xrightarrow{2\\text{NF}} \\text{No Partial} \\xrightarrow{3\\text{NF}} \\text{No Transitive}",
      "legend": "• 1NF: Atomic values & no multi-valued attributes<br>• 2NF: 1NF + no partial functional dependency<br>• 3NF: 2NF + no transitive dependency"
    },
    "hints": {
      "concept": "1NF fokus pada keatoman data (satu sel hanya memuat satu nilai tunggal) dan ketiadaan kolom/baris yang berulang.",
      "execution": "Opsi A adalah 3NF, opsi D adalah 2NF. 1NF mensyaratkan nilai atomik."
    },
    "explanation": "Syarat 1NF adalah setiap kolom hanya memuat nilai atomik (tidak dapat dipecah lagi) dan tidak memiliki repeating groups/multi-valued attributes. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "201 Created yang mengindikasikan entitas sumber daya baru telah berhasil dibuat di server."
      },
      {
        "key": "B",
        "text": "200 OK yang mengindikasikan keberhasilan umum pemrosesan request tanpa entitas baru."
      },
      {
        "key": "C",
        "text": "204 No Content yang mengindikasikan permintaan sukses tetapi respons tidak memiliki isi bodi."
      },
      {
        "key": "D",
        "text": "301 Moved Permanently yang mengalihkan URL request secara permanen ke lokasi endpoint baru."
      },
      {
        "key": "E",
        "text": "400 Bad Request yang mengindikasikan payload request tidak sesuai format validasi schema."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "HTTP SUCCESS STATUS CODES",
      "latex": "200 \\text{ (OK)}, \\quad 201 \\text{ (Created)}, \\quad 204 \\text{ (No Content)}",
      "legend": "• 200: Operasi standar berhasil<br>• 201: Resource berhasil dibuat (POST)<br>• 204: Berhasil tanpa return body (DELETE)"
    },
    "hints": {
      "concept": "HTTP status 201 Created secara spesifik dirancang untuk operasi pembuatan resource baru yang berhasil.",
      "execution": "200 adalah kesuksesan generik, 201 spesifik untuk created resource."
    },
    "explanation": "HTTP 201 Created adalah kode status standar RFC 7231 saat request POST sukses membuat resource baru di server. 200 adalah respons umum, 204 tanpa bodi respons. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Nilai maxCapacity berhasil diperbarui menjadi 120 secara mulus tanpa peringatan apapun guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "B",
        "text": "Terjadi TypeError: Assignment to constant variable karena nilai referensi const di-assign ulang.                                            "
      },
      {
        "key": "C",
        "text": "Terjadi SyntaxError saat fase kompilasi sebelum kode sempat dieksekusi oleh engine V8.                                                      "
      },
      {
        "key": "D",
        "text": "Variabel maxCapacity otomatis diubah tipenya oleh engine menjadi variabel bertipe var global.                                               "
      },
      {
        "key": "E",
        "text": "Nilai variabel maxCapacity menjadi undefined karena konflik alokasi memori runtime V8.                                                      "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "onStart() yang membuat activity mulai terlihat di layar pengguna tetapi belum dapat berinteraksi."
      },
      {
        "key": "B",
        "text": "onResume() yang menandakan activity berada di foreground dan siap menerima input interaksi."
      },
      {
        "key": "C",
        "text": "onCreate() yang menginisialisasi komponen dasar, data binding, dan memanggil setContentView()."
      },
      {
        "key": "D",
        "text": "onPause() yang dipanggil ketika activity kehilangan fokus utama akibat pop-up atau dialog."
      },
      {
        "key": "E",
        "text": "onRestart() yang memulihkan activity setelah sebelumnya berada pada status onStop.   "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Mengompilasi ulang seluruh source code gim secara real-time setiap kali pemain melakukan aksi.                                                      "
      },
      {
        "key": "B",
        "text": "Menghubungkan gim secara terus-menerus ke server basis data cloud untuk sinkronisasi leaderboard.                                                   "
      },
      {
        "key": "C",
        "text": "Membersihkan alokasi memori RAM secara paksa setiap frame agar tidak terjadi fragmentasi heap untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "D",
        "text": "Menerima input pengguna, memperbarui kondisi logika objek dunia gim, dan merender tampilan grafis.                                                  "
      },
      {
        "key": "E",
        "text": "Memeriksa keaslian lisensi perangkat lunak gim dari store server sebelum aset dimuat ke GPU.                                                        "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "CLASSIC GAME LOOP PATTERN",
      "latex": "\\text{while}(\\text{running}) \\;\\{ \\text{processInput}(); \\; \\text{updateState}(\\Delta t); \\; \\text{renderView}(); \\}",
      "legend": "• Input: Keyboard, touch, controller event<br>• Update: Fisika, AI, collision, timer<br>• Render: Gambar scene ke frame buffer"
    },
    "hints": {
      "concept": "Game loop memiliki 3 tahapan siklis utama: Process Input -> Update Game State -> Render Output.",
      "execution": "Siklus ini dieksekusi berulang kali (misal 60 fps) untuk menjaga dunia game responsif."
    },
    "explanation": "Game Loop adalah jantung aplikasi gim yang berjalan berulang-ulang untuk: (1) membaca input pemain, (2) mengkalkulasi logika/fisika/AI (update), dan (3) menggambar scene ke layar (render). Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Raycasting yang menembakkan berkas garis vektor lurus untuk mengukur jarak objek target."
      },
      {
        "key": "B",
        "text": "Oriented Bounding Box (OBB) yang menggunakan pemisahan sumbu SAT dengan sudut rotasi dinamis."
      },
      {
        "key": "C",
        "text": "Convex Hull Detection yang menghitung poligon terluar yang membungkus seluruh vertex objek."
      },
      {
        "key": "D",
        "text": "Spatial Hashing yang membagi ruang dunia gim ke dalam grid sel matriks berindeks terpisah."
      },
      {
        "key": "E",
        "text": "Axis-Aligned Bounding Box (AABB) yang membandingkan koordinat batas minimum dan maksimum."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "AABB COLLISION FORMULA",
      "latex": "\\text{overlap} = (x_{1\\text{min}} \\le x_{2\\text{max}}) \\land (x_{1\\text{max}} \\ge x_{2\\text{min}}) \\land (y_{1\\text{min}} \\le y_{2\\text{max}}) \\land (y_{1\\text{max}} \\ge y_{2\\text{min}})",
      "legend": "• AABB: Efisien, komputasi murah (hanya perbandingan angka aljabar sederhana)<br>• Sumbu sejajar X dan Y (tanpa rotasi sudut)"
    },
    "hints": {
      "concept": "Axis-Aligned Bounding Box (AABB) adalah metode deteksi tabrakan kotak non-rotasi paling mendasar.",
      "execution": "Perhatikan frasa 'kotak pembatas sejajar sumbu koordinat' yang merupakan terjemahan dari Axis-Aligned Bounding Box."
    },
    "explanation": "AABB (Axis-Aligned Bounding Box) adalah algoritma deteksi tabrakan yang mengasumsikan batas kotak objek selalu sejajar dengan sumbu X dan Y dunia gim, menjadikannya sangat cepat dikomputasi. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Visibility of system status dengan selalu memberi tahu pengguna kondisi yang sedang berlangsung.                                           "
      },
      {
        "key": "B",
        "text": "Match between system and real world dengan menggunakan metafora objek kehidupan nyata.                                                     "
      },
      {
        "key": "C",
        "text": "User control and freedom dengan menyediakan tombol darurat undo untuk membatalkan aksi.                                                    "
      },
      {
        "key": "D",
        "text": "Error prevention dengan mencegah kesalahan pengguna terjadi sebelum aksi dieksekusi.                                                       "
      },
      {
        "key": "E",
        "text": "Flexibility and efficiency of use dengan menyediakan shortcut bagi pengguna mahir sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "NIELSEN HEURISTIC #1",
      "latex": "\\text{Feedback Time} < 100\\text{ms (Instant)}, \\quad < 1\\text{s (Flow)}, \\quad > 10\\text{s (Show Progress)}",
      "legend": "• Heuristic 1: Visibility of system status<br>• Memberikan umpan balik visual tepat waktu kepada pengguna"
    },
    "hints": {
      "concept": "Heuristik pertama Nielsen menyatakan sistem harus selalu menginformasikan status kerjanya kepada user melalui feedback yang wajar dan tepat waktu.",
      "execution": "Progress bar dan indikator loading adalah contoh klasik pemenuhan status sistem."
    },
    "explanation": "Prinsip 'Visibility of system status' mengharuskan sistem selalu memberi tahu pengguna mengenai apa yang sedang terjadi melalui umpan balik yang sesuai dalam waktu yang wajar (seperti loading bar). Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "2.0:1 yang merupakan standar rasio kontras minimum bagi elemen dekoratif non-teks antarmuka."
      },
      {
        "key": "B",
        "text": "4.5:1 yang merupakan standar rasio kontras minimum untuk teks normal agar terbaca dengan jelas."
      },
      {
        "key": "C",
        "text": "3.0:1 yang merupakan standar rasio kontras untuk teks berukuran besar (large text minimal 18pt)."
      },
      {
        "key": "D",
        "text": "7.0:1 yang merupakan standar rasio kontras ketat level AAA untuk keterbacaan tingkat tinggi."
      },
      {
        "key": "E",
        "text": "10.0:1 yang merupakan rasio kontras ekstrim monokrom hitam putih murni tanpa gradasi."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "WCAG CONTRAST RATIO SPECIFICATION",
      "latex": "\\text{Ratio} = \\frac{L_1 + 0.05}{L_2 + 0.05} \\ge 4.5:1 \\quad (\\text{Level AA Normal Text})",
      "legend": "• Level AA Normal Text: Minimal 4.5:1<br>• Level AA Large Text (>=18pt/14pt bold): Minimal 3.0:1<br>• Level AAA Normal Text: Minimal 7.0:1"
    },
    "hints": {
      "concept": "WCAG 2.1 Level AA mensyaratkan rasio kontras 4.5:1 untuk teks normal dan 3:1 untuk teks besar.",
      "execution": "Pilihlah angka 4.5:1 untuk teks biasa pada level AA."
    },
    "explanation": "WCAG 2.1 Level AA menetapkan ambang batas rasio kontras minimal 4.5:1 untuk teks reguler. Untuk teks besar (18pt atau 14pt tebal), batasnya adalah 3:1. Jawaban: B.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "GNU General Public License (GPL) yang menerapkan klausul copyleft ketat pada proyek turunan."
      },
      {
        "key": "B",
        "text": "Affero General Public License (AGPL) yang mewajibkan rilis source code layanan berbasis jaringan."
      },
      {
        "key": "C",
        "text": "MIT License yang memberikan kebebasan penuh penggunaan komersial dengan mencantumkan lisensi."
      },
      {
        "key": "D",
        "text": "Creative Commons Non-Commercial (CC-NC) yang melarang keras pemanfaatan untuk tujuan profit."
      },
      {
        "key": "E",
        "text": "End User License Agreement (EULA) yang merupakan perjanjian pembatasan lisensi hak milik vendor."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "SOFTWARE LICENSE CATEGORIES",
      "latex": "\\text{Open Source} = \\text{Permissive (MIT/BSD/Apache)} \\cup \\text{Copyleft (GPL/AGPL)}",
      "legend": "• MIT: Permissive, komersial diizinkan, no copyleft<br>• GPL: Viral copyleft, turunan wajib open source GPL"
    },
    "hints": {
      "concept": "Lisensi MIT adalah lisensi permisif populer yang memungkinkan pengembang memakai kode untuk aplikasi komersial tanpa kewajiban membuka source code.",
      "execution": "GPL mewajibkan copyleft, sedangkan MIT bersifat permisif."
    },
    "explanation": "Lisensi MIT adalah jenis lisensi permisif yang memberikan izin bagi siapa pun untuk menggunakan, memodifikasi, dan mendistribusikan kode, termasuk untuk keperluan komersial tertutup, dengan syarat tetap menyertakan hak cipta dan disclaimer asli. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Setiap 20 jam bekerja, istirahatlah selama 20 menit penuh sambil mengonsumsi 20 mililiter air mineral."
      },
      {
        "key": "B",
        "text": "Mengatur tingkat kecerahan layar monitor pada angka 20% dengan sudut kemiringan tepat 20 derajat."
      },
      {
        "key": "C",
        "text": "Setiap 20 baris kode program yang ditulis, lakukan peregangan jari tangan sebanyak 20 kali repetisi."
      },
      {
        "key": "D",
        "text": "Setiap 20 menit menatap layar, alihkan pandangan ke objek berjarak 20 kaki (6 meter) selama 20 detik."
      },
      {
        "key": "E",
        "text": "Menjaga jarak mata dari layar kaca monitor sejauh tepat 20 sentimeter dengan sudut pandang 20 derajat."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "THE 20-20-20 RULE FOR EYE ERGONOMICS",
      "latex": "20\\text{ minutes work} \\implies \\text{Look at } 20\\text{ feet distant object} \\implies \\text{for } 20\\text{ seconds}",
      "legend": "• Mencegah Computer Vision Syndrome (CVS)<br>• Melemaskan otot silier lensa mata"
    },
    "hints": {
      "concept": "Rule 20-20-20 adalah rekomendasi medis ergonomi: setiap 20 menit, pandang objek sejauh 20 kaki selama 20 detik.",
      "execution": "20 feet setara dengan 6 meter."
    },
    "explanation": "Aturan ergonomi mata 20-20-20 menyatakan bahwa setiap 20 menit bekerja di depan komputer, istirahatkan mata dengan memandang objek berjarak minimal 20 kaki (sekitar 6 meter) selama minimal 20 detik untuk mengistirahatkan otot fokus mata. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Pengujian black-box hanya dapat dilakukan oleh komputer secara otomatis tanpa keterlibatan manusia.                                                                  "
      },
      {
        "key": "B",
        "text": "White-box testing hanya menguji antarmuka visual grafis pengguna tanpa memeriksa basis data server.                                                                  "
      },
      {
        "key": "C",
        "text": "Black-box mensyaratkan penguji memiliki akses penuh terhadap diagram logika kode sumber aplikasi.                                                                    "
      },
      {
        "key": "D",
        "text": "White-box testing hanya dijalankan pada tahapan pengujian penerimaan pengguna akhir (User Acceptance Test) dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "E",
        "text": "Black-box menguji fungsi berdasarkan input-output spesifikasi, sedangkan white-box menguji alur kode internal.                                                       "
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TESTING PARADIGMS COMPARISON",
      "latex": "\\text{Black-Box} \\colon f(x) \\to y \\quad \\text{vs} \\quad \\text{White-Box} \\colon \\text{Control Flow Graph & Branch}",
      "legend": "• Black-Box: Uji spesifikasi & fungsional (tanpa lihat kode)<br>• White-Box: Uji struktur, percabangan, & jalur logika internal"
    },
    "hints": {
      "concept": "Black-box menguji 'apa yang dilakukan sistem' dari luar (spesifikasi), sedangkan white-box menguji 'bagaimana sistem bekerja' di dalam (struktur kode).",
      "execution": "Black box = tanpa akses kode sumber; White box = dengan analisis kode sumber."
    },
    "explanation": "Black-Box Testing berfokus pada pengujian fungsionalitas berdasarkan spesifikasi kebutuhan tanpa melihat struktur kode internal, sedangkan White-Box Testing menganalisis struktur internal, alur percabangan, dan logika kode sumber program. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "B karena nilai 85 memenuhi kondisi elif kedua score >= 80 dan eksekusi blok percabangan berakhir."
      },
      {
        "key": "B",
        "text": "A karena evaluasi kondisi percabangan selalu memilih nilai grade tertinggi yang tersedia."
      },
      {
        "key": "C",
        "text": "C karena kondisi 85 juga secara matematis lebih besar sama dengan 70 pada evaluasi ketiga."
      },
      {
        "key": "D",
        "text": "D karena struktur percabangan mengalami runtime fallback ke blok klausa else default."
      },
      {
        "key": "E",
        "text": "Terjadi error kompilasi karena variabel grade dideklarasikan berulang di dalam blok if."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "CONDITIONAL CONTROL FLOW",
      "latex": "85 \\ge 90 \\; (\\text{False}) \\implies 85 \\ge 80 \\; (\\text{True}) \\implies \\text{Execute & Exit Branch}",
      "legend": "• if-elif-else mengeksekusi blok pertama yang bernilai True lalu keluar dari seluruh rantai seleksi"
    },
    "hints": {
      "concept": "Dalam struktur if-elif-else, begitu sebuah kondisi terpenuhi (True), blok tersebut dieksekusi dan sisa kondisi di bawahnya diabaikan.",
      "execution": "Kondisi score >= 90 bernilai False. Kondisi score >= 80 bernilai True, sehingga grade = 'B' dieksekusi."
    },
    "explanation": "Karena 85 < 90 (False), evaluasi berlanjut ke `elif score >= 80`. Karena 85 >= 80 bernilai True, maka `grade = 'A'` dijalankan dan rantai percabangan selesai. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "git commit -m yang menyimpan snapshot perubahan secara permanen ke repositori lokal."
      },
      {
        "key": "B",
        "text": "git add yang mendaftarkan perubahan file yang dipilih ke dalam staging area."
      },
      {
        "key": "C",
        "text": "git push origin yang mengunggah riwayat commit lokal ke repositori remote di cloud."
      },
      {
        "key": "D",
        "text": "git checkout yang beralih antar branch kerja atau membatalkan perubahan lokal."
      },
      {
        "key": "E",
        "text": "git status yang menampilkan status pelacakan file pada direktori kerja saat ini."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "GIT WORKFLOW STAGES",
      "latex": "\\text{Working Directory} \\xrightarrow{\\text{git add}} \\text{Staging Area} \\xrightarrow{\\text{git commit}} \\text{Local Repo}",
      "legend": "• Working directory: Berkas diubah di editor<br>• Staging area (Index): Berkas siap di-commit<br>• Repository: Riwayat permanen"
    },
    "hints": {
      "concept": "Tiga zona Git: Working Directory -> Staging Area -> Commit History.",
      "execution": "git add digunakan untuk memindahkan perubahan ke Staging Area."
    },
    "explanation": "Perintah `git add <nama_file>` atau `git add .` berfungsi menambahkan file dari working directory ke staging area (index) agar siap disertakan dalam commit berikutnya. Jawaban: B.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Jumlah akumulasi total nominal harga seluruh produk dengan kategori Elektronik di tabel."
      },
      {
        "key": "B",
        "text": "Rata-rata jumlah stok unit barang yang termasuk dalam klasifikasi produk Elektronik."
      },
      {
        "key": "C",
        "text": "Jumlah total baris (rekaman) produk yang memenuhi kriteria kategori 'Elektronik'."
      },
      {
        "key": "D",
        "text": "Daftar nama seluruh produk barang Elektronik yang diurutkan secara berurutan abjad."
      },
      {
        "key": "E",
        "text": "Nilai transaksi harga tertinggi di antara produk-produk dalam kategori Elektronik."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "SQL AGGREGATE FUNCTIONS",
      "latex": "\\text{COUNT}(*) \\to \\text{Row Count}, \\quad \\text{SUM}(c) \\to \\text{Total}, \\quad \\text{AVG}(c) \\to \\text{Mean}",
      "legend": "• COUNT(*): Menghitung seluruh baris termasuk nilai NULL<br>• SUM: Akumulasi nilai angka<br>• AVG: Rata-rata nilai"
    },
    "hints": {
      "concept": "Fungsi COUNT(*) menghitung banyaknya baris rekaman yang lolos filter klausul WHERE.",
      "execution": "Untuk total harga digunakan SUM(), rata-rata AVG(), dan jumlah baris COUNT()."
    },
    "explanation": "Fungsi `COUNT(*)` menghitung banyaknya jumlah baris rekaman yang dihasilkan oleh query setelah disaring oleh klausul `WHERE kategori = 'Elektronik'`. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Java Standard Output Network yang merupakan protokol transfer data biner antar server guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "B",
        "text": "Joint Security Organization Network yang mengatur enkripsi paket pada protokol HTTPS.                                                      "
      },
      {
        "key": "C",
        "text": "Java Source Object Network yang berfungsi mengompilasi file bytecode di browser client.                                                    "
      },
      {
        "key": "D",
        "text": "Java Script Object Notation yang merupakan format pertukaran data teks ringan berbasis key-value.                                          "
      },
      {
        "key": "E",
        "text": "JavaScript Operational Node yang mengelola thread eksekusi multi-core pada runtime Node.js.                                                "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "JSON DATA STRUCTURE",
      "latex": "\\text{JSON} = \\{ \\text{\"key\"} \\colon \\text{value} \\}, \\quad \\text{where value} \\in \\{ \\text{string, number, bool, array, object, null} \\}",
      "legend": "• Format berbasis teks, human-readable, language-independent"
    },
    "hints": {
      "concept": "JSON singkatan dari JavaScript Object Notation, format teks standar untuk representasi struktur data berpasangan key-value.",
      "execution": "JSON mudah dibaca manusia dan didukung oleh hampir semua bahasa pemrograman modern."
    },
    "explanation": "JSON (JavaScript Object Notation) adalah format standar pertukaran data terbuka berbasis teks yang ringan, mudah dibaca manusia dan mesin, serta independen dari bahasa pemrograman. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "System Testing yang menguji keseluruhan sistem perangkat lunak secara utuh end-to-end. "
      },
      {
        "key": "B",
        "text": "Integration Testing yang memverifikasi komunikasi dan interaksi antar beberapa modul komponen."
      },
      {
        "key": "C",
        "text": "Acceptance Testing yang dilakukan oleh pengguna akhir untuk memastikan kesesuaian kebutuhan bisnis."
      },
      {
        "key": "D",
        "text": "Performance Testing yang mengukur daya tahan dan waktu respons server di bawah beban tinggi."
      },
      {
        "key": "E",
        "text": "Unit Testing yang memvalidasi kebenaran logika fungsi atau method terkecil secara terisolasi."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "TEST PYRAMID HIERARCHY",
      "latex": "\\text{E2E / UI Test} \\; (10\\%) \\to \\text{Integration Test} \\; (20\\%) \\to \\text{Unit Test} \\; (70\\%)",
      "legend": "• Unit: Paling banyak, cepat, menguji fungsi individual<br>• Integration: Uji gabungan modul/DB/API<br>• E2E: Uji alur pengguna menyeluruh"
    },
    "hints": {
      "concept": "Pengujian pada level terkecil komponen perangkat lunak (fungsi, prosedur, class method) disebut unit test.",
      "execution": "Piramida pengujian menempatkan unit test di lapisan terbawah karena paling cepat dan terisolasi."
    },
    "explanation": "Unit Testing adalah pengujian terhadap bagian terkecil dari perangkat lunak (seperti fungsi atau method individual) secara terisolasi dari dependensi luar. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menyimpan elemen-elemen bertipe sama dalam lokasi blok memori yang berurutan (kontigu).                                                  "
      },
      {
        "key": "B",
        "text": "Dapat menampung berbagai tipe data heterogen tanpa batasan kapasitas alokasi awal.                                                       "
      },
      {
        "key": "C",
        "text": "Elemen hanya dapat diakses secara sekuensial dari elemen pertama hingga terakhir untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "D",
        "text": "Alokasi ukuran panjang array otomatis bertambah saat terjadi penambahan data baru.                                                       "
      },
      {
        "key": "E",
        "text": "Setiap elemen memiliki pointer referensi eksplisit ke alamat memori elemen berikutnya.                                                   "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ARRAY MEMORY ADDRESS CALCULATION",
      "latex": "\\text{Address}(A[i]) = \\text{BaseAddress} + (i \\times \\text{ElementSize})",
      "legend": "• Akses langsung konstan: $O(1)$ random access time<br>• Memori kontigu (berurutan tanpa jeda)"
    },
    "hints": {
      "concept": "Array statis mengalokasikan memori secara kontigu (berdampingan) dan memiliki ukuran tetap dengan tipe data homogen.",
      "execution": "Lokasi memori kontigu memungkinkan akses acak $O(1)$ via indeks."
    },
    "explanation": "Array menyimpan elemen-elemen bertipe data sama pada blok memori yang berurutan (kontigu), memungkinkan akses instan $O(1)$ menggunakan indeks. Pilihan E adalah karakteristik Linked List. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "ConstraintLayout yang menyusun view berdasarkan hubungan pembatas relatif terhadap elemen lain."
      },
      {
        "key": "B",
        "text": "LinearLayout yang menata widget anak secara berurutan dalam satu orientasi garis lurus."
      },
      {
        "key": "C",
        "text": "FrameLayout yang menumpuk view anak di atas view lainnya pada sudut kiri atas layar."
      },
      {
        "key": "D",
        "text": "TableLayout yang menyusun elemen ke dalam baris dan kolom kisi-kisi matriks kaku.  "
      },
      {
        "key": "E",
        "text": "RelativeLayout yang menempatkan view berdasarkan posisi relatif terhadap view saudaranya."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Sebuah kelas konkret di Java diperbolehkan mewarisi lebih dari satu superclass abstrak.                                                              "
      },
      {
        "key": "B",
        "text": "Interface hanya mendefinisikan kontrak tanpa bisa memiliki method dengan implementasi default sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "C",
        "text": "Sebuah kelas konkret dapat mengimplementasikan beberapa interface sekaligus (multiple interfaces).                                                   "
      },
      {
        "key": "D",
        "text": "Abstract class tidak dapat memiliki constructor untuk menginisialisasi atribut instansinya.                                                          "
      },
      {
        "key": "E",
        "text": "Interface dapat diinstansiasi secara langsung menjadi objek mandiri dengan kata kunci new.                                                           "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Pasal tentang penyebaran informasi hoaks dan berita bohong yang menyesatkan publik.                                                                  "
      },
      {
        "key": "B",
        "text": "Pasal tentang pencemaran nama baik dan penghinaan personal melalui media sosial online.                                                              "
      },
      {
        "key": "C",
        "text": "Pasal tentang transaksi perdagangan elektronik dan pendaftaran penyelenggara sistem komersial.                                                       "
      },
      {
        "key": "D",
        "text": "Pasal 30 tentang akses ilegal (illegal access) terhadap sistem komputer atau jaringan orang lain.                                                    "
      },
      {
        "key": "E",
        "text": "Pasal tentang perlindungan hak cipta konten multimedia yang diunggah ke portal streaming dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "CYBER LAW FRAMEWORK (UU ITE)",
      "latex": "\\text{Pasal 30 UU ITE} \\implies \\text{Illegal Access to Computer System / Data}",
      "legend": "• Ayat 1: Akses tanpa hak<br>• Ayat 2: Akses untuk memperoleh info/dokumen<br>• Ayat 3: Membobol sistem pengamanan (cracking)"
    },
    "hints": {
      "concept": "Pasal 30 UU ITE mengatur tindak pidana akses ilegal (illegal access) ke komputer/jaringan orang lain dengan melanggar pengamanan.",
      "execution": "Ingat konsep Illegal Access = Pasal 30 UU ITE."
    },
    "explanation": "Pasal 30 UU ITE secara tegas melarang perbuatan setiap orang yang dengan sengaja dan tanpa hak atau melawan hukum mengakses komputer dan/atau sistem elektronik milik orang lain dengan cara apa pun (illegal access). Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Aplikasi rintisan (startup) baru di mana fitur dan target pasar masih dalam tahap eksperimen cepat."
      },
      {
        "key": "B",
        "text": "Game online mobile yang membutuhkan pembaruan konten dan penyesuaian event berkala tiap minggu."
      },
      {
        "key": "C",
        "text": "Portal e-commerce ritel yang ingin sering merilis fitur baru berdasarkan tren belanja konsumen."
      },
      {
        "key": "D",
        "text": "Sistem media sosial interaktif yang terus mengembangkan algoritma rekomendasi berdasarkan feedback."
      },
      {
        "key": "E",
        "text": "Sistem kendali kedirgantaraan dengan spesifikasi kebutuhan yang sudah fix, kaku, dan regulasi ketat."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "SDLC MODEL SELECTION MATRIX",
      "latex": "\\text{Requirements Clarity} \\land \\text{High Regulation} \\implies \\text{Waterfall}",
      "legend": "• Waterfall: Spesifikasi jelas, stabil, minim perubahan, dokumentasi ketat<br>• Agile: Dinamis, eksperimental, feedback cepat"
    },
    "hints": {
      "concept": "Model Waterfall sangat cocok untuk sistem dengan persyaratan yang telah pasti dan tidak berubah-ubah serta memiliki standar keselamatan/regulasi ketat.",
      "execution": "Sistem kedirgantaraan atau alat medis memiliki spesifikasi baku yang fatal jika diubah di tengah jalan."
    },
    "explanation": "Model Waterfall ideal untuk proyek berskala kritis dengan spesifikasi kebutuhan yang sudah pasti, jelas, tidak boleh berubah di tengah jalan, dan memiliki standar dokumentasi ketat (seperti sistem kedirgantaraan, militer, atau perangkat medis). Jawaban: E.",
    "isDiagnostic": false
  },
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
      {
        "key": "A",
        "text": "Menghapus seluruh file auth.js dari repositori lalu menjalankan git pull paksa dari branch main remote.                                              "
      },
      {
        "key": "B",
        "text": "Berdiskusi dengan tim untuk memilih durasi expiry yang valid, menghapus marker konflik, lalu git add dan commit.                                     "
      },
      {
        "key": "C",
        "text": "Membiarkan tanda kurung siku dan marker konflik di dalam file karena Git otomatis memilih baris terpanjang.                                          "
      },
      {
        "key": "D",
        "text": "Menjalankan perintah git push --force agar branch feature-login menimpa seluruh riwayat branch develop.                                              "
      },
      {
        "key": "E",
        "text": "Membuat branch baru dari HEAD lalu menduplikasi seluruh perubahan konfigurasi token secara manual guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menghapus seluruh commit lama yang cacat dan menggantinya dengan snapshot kode tunggal terkompresi."
      },
      {
        "key": "B",
        "text": "Mencegah terjadinya konflik antar file sama sekali secara otomatis melalui kecerdasan algoritma Git."
      },
      {
        "key": "C",
        "text": "Menghasilkan riwayat riwayat commit yang linier, bersih, dan rapi tanpa adanya extra merge commit node."
      },
      {
        "key": "D",
        "text": "Mengunggah commit langsung ke server cloud remote tanpa memerlukan otentikasi kunci SSH pengembang."
      },
      {
        "key": "E",
        "text": "Mengizinkan banyak developer mengedit commit yang sama di remote repository secara bersamaan tanpa lock."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "REBASE VS MERGE COMMIT TOPOLOGY",
      "latex": "\\text{Merge: } C_1 \\to C_2 \\to M_{\\text{merge}} \\quad \\text{vs} \\quad \\text{Rebase: } C_1' \\to C_2' \\to C_{\\text{linear}}",
      "legend": "• Rebase: Memindahkan basis branch menghasilkan riwayat 1 garis lurus<br>• Merge: Mempertahankan cabang riwayat dengan simpul merge commit baru"
    },
    "hints": {
      "concept": "Git rebase menerapkan kembali commit dari feature branch di atas commit terakhir branch target, menciptakan riwayat lurus tanpa percabangan ganda.",
      "execution": "Keunggulan rebase adalah commit history yang linier dan mudah dilacak saat debugging (misal menggunakan git bisect)."
    },
    "explanation": "Keuntungan utama `git rebase` adalah menghasilkan riwayat commit linier yang rapi tanpa 'merge commit' tambahan, mempermudah pelacakan perubahan kode dan audit git log. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Sensor-Aktif karena tipe referensi variabel deklarasi s adalah kelas induk Sensor pada saat kompilasi."
      },
      {
        "key": "B",
        "text": "Sensor-Aktif Suhu:28C karena superclass otomatis dieksekusi terlebih dahulu sebelum method subclass."
      },
      {
        "key": "C",
        "text": "Compile-time error karena variabel tipe Sensor tidak dapat menampung instansiasi objek kelas turunannya."
      },
      {
        "key": "D",
        "text": "Suhu:28C karena JVM memanggil method objek riil SensorSuhu di memori heap via dynamic method dispatch."
      },
      {
        "key": "E",
        "text": "Runtime error ClassCastException karena ketidakcocokan tipe referensi objek polimorfik di stack JVM."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "DYNAMIC METHOD DISPATCH PRINCIPLE",
      "latex": "\\text{Reference Type } (\\text{Sensor}) \\xrightarrow{\\text{Runtime Resolution}} \\text{Actual Object Method } (\\text{SensorSuhu.baca()})",
      "legend": "• Penentuan pemanggilan method override dilakukan saat runtime berdasarkan tipe objek riil di heap"
    },
    "hints": {
      "concept": "Pada polimorfisme dinamis, method yang dipanggil ditentukan oleh objek sebenarnya yang dibuat dengan 'new', bukan tipe variabel referensinya.",
      "execution": "Variabel s merujuk ke objek baru SensorSuhu(), sehingga method baca() milik SensorSuhu yang dijalankan."
    },
    "explanation": "Meskipun tipe referensi `s` bertipe `Sensor`, objek sebenarnya yang diinstansiasi di memori heap adalah `SensorSuhu()`. Berdasarkan prinsip polimorfisme dinamis (dynamic method dispatch), JVM akan memanggil method override milik `SensorSuhu`. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Tidak mengimplementasikan interface Serializable untuk penyimpanan state objek ke media disk sekunder untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "B",
        "text": "Menggunakan method dengan visibilitas public yang membahayakan enkapsulasi data internal objek.                                                            "
      },
      {
        "key": "C",
        "text": "Tidak mendeklarasikan variabel konstanta statis untuk menyimpan string query SQL dan konfigurasi PDF.                                                      "
      },
      {
        "key": "D",
        "text": "Menolak pewarisan kelas turunan karena tidak ditambahkan keyword abstract pada deklarasi kelasnya.                                                         "
      },
      {
        "key": "E",
        "text": "Memiliki lebih dari satu tanggung jawab (alasan untuk berubah): kalkulasi bisnis, persistensi data, dan rendering UI.                                      "
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "SOLID - SINGLE RESPONSIBILITY PRINCIPLE (SRP)",
      "latex": "\\text{A Class should have one, and only one, reason to change}",
      "legend": "• Solusi: Pisahkan ke 3 kelas: SalesCalculator, SalesRepository, dan SalesPdfExporter"
    },
    "hints": {
      "concept": "SRP (prinsip pertama SOLID) menegaskan bahwa satu kelas hanya boleh memiliki satu tanggung jawab atau satu alasan untuk berubah.",
      "execution": "Kelas tersebut mengurusi logika bisnis (hitung laba), database (simpan DB), dan presentasi (cetak PDF)."
    },
    "explanation": "SRP menyatakan 'A class should have only one reason to change'. Kelas `LaporanPenjualan` memiliki 3 alasan berbeda untuk berubah: perubahan aturan bisnis perhitungan, perubahan skema database, atau perubahan template PDF. Solusinya adalah memisahkannya menjadi 3 kelas berbeda. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Terdapat ketergantungan fungsional parsial di mana atribut non-kunci hanya bergantung pada sebagian kunci komposit.                                          "
      },
      {
        "key": "B",
        "text": "Nilai_Huruf memiliki nilai berulang yang tidak terindeks secara seimbang pada struktur B-Tree.                                                               "
      },
      {
        "key": "C",
        "text": "Terdapat ketergantungan transitif antar sesama atribut non-kunci primer di dalam relasi tabel tersebut sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "D",
        "text": "Kolom primary key komposit tidak boleh terdiri dari lebih dari satu atribut dalam sistem basis data RDBMS.                                                   "
      },
      {
        "key": "E",
        "text": "Tabel KRS tidak menyertakan foreign key ke tabel dosen pembimbing akademik mahasiswa bersangkutan.                                                           "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SECOND NORMAL FORM (2NF) CONDITION",
      "latex": "\\text{2NF} \\iff \\text{1NF} \\land \\neg(\\exists \\text{ non-key } A \\colon P_{\\text{partial}} \\to A)",
      "legend": "• Partial dependency: NIM -> Nama_Mhs (hanya bergantung pada separuh composite key)<br>• Solusi: Dekomposisi ke Mahasiswa, MataKuliah, dan KRS"
    },
    "hints": {
      "concept": "Syarat 2NF adalah 1NF dan tidak ada ketergantungan parsial (atribut non-kunci bergantung pada sebagian saja dari primary key gabungan).",
      "execution": "Atribut Nama_Mahasiswa hanya bergantung pada NIM, dan Nama_MK hanya bergantung pada Kode_MK."
    },
    "explanation": "2NF melarang adanya Partial Functional Dependency pada tabel yang memiliki Composite Primary Key. Karena `Nama_Mahasiswa` hanya bergantung pada `NIM` (sebagian dari key `(NIM, Kode_MK)`), tabel harus didekomposisi agar memenuhi 2NF. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Membuat satu tabel baru yang menggabungkan seluruh data pegawai dan riwayat penggajian secara utuh dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "B",
        "text": "Memecah menjadi Pegawai(ID_Pegawai, Nama, Kode_Departemen) dan Departemen(Kode_Departemen, Nama_Departemen).                                                  "
      },
      {
        "key": "C",
        "text": "Menghapus kolom Kode_Departemen dan hanya menyisakan Nama_Departemen langsung di tabel Pegawai.                                                               "
      },
      {
        "key": "D",
        "text": "Menambahkan kolom ID_Pegawai sebagai primary key kedua di dalam tabel Departemen yang didekomposisi.                                                          "
      },
      {
        "key": "E",
        "text": "Mengubah Primary Key ID_Pegawai menjadi composite key (ID_Pegawai, Kode_Departemen, Nama_Departemen).                                                         "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "2 baris data karena hanya pelanggan ID 1 dan ID 2 yang memiliki relasi transaksi pesanan aktif."
      },
      {
        "key": "B",
        "text": "3 baris data karena query dibatasi oleh jumlah baris pada tabel pesanan sisi kanan join.      "
      },
      {
        "key": "C",
        "text": "5 baris data karena pelanggan 2 muncul 2 kali, pelanggan 1 muncul 1 kali, dan pelanggan 3 & 4 bernilai NULL."
      },
      {
        "key": "D",
        "text": "4 baris data karena tabel sisi kiri Pelanggan memiliki tepat 4 rekaman unik tanpa duplikasi.  "
      },
      {
        "key": "E",
        "text": "7 baris data hasil perkalian Cartesian Product antara tabel Pelanggan dan tabel Pesanan.      "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menyaring transaksi satuan sebelum dilakukan pengelompokan baris data oleh sistem database engine."
      },
      {
        "key": "B",
        "text": "Mengurutkan nama cabang toko dari perolehan total omset terbesar ke yang terkecil secara descending."
      },
      {
        "key": "C",
        "text": "Menghitung rata-rata pendapatan harian untuk setiap transaksi yang statusnya lunas terverifikasi."
      },
      {
        "key": "D",
        "text": "Menyaring kelompok cabang toko yang memiliki akumulasi total omset minimal lima puluh juta rupiah."
      },
      {
        "key": "E",
        "text": "Membuat index clustered virtual pada kolom cabang_toko untuk mengoptimalkan pembacaan disk."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "WHERE VS HAVING LOGICAL EXECUTION ORDER",
      "latex": "\\text{FROM} \\to \\text{WHERE (Row Filter)} \\to \\text{GROUP BY} \\to \\text{HAVING (Group Filter)} \\to \\text{SELECT}",
      "legend": "• WHERE: Filter individual rows sebelum agregasi<br>• HAVING: Filter groups hasil agregasi"
    },
    "hints": {
      "concept": "HAVING bertindak sebagai filter untuk kelompok data (hasil agregasi SUM, COUNT, AVG), berbeda dengan WHERE yang memfilter baris mentah.",
      "execution": "Klausul HAVING menyaring hasil kelompok cabang toko yang total_omset-nya >= 50.000.000."
    },
    "explanation": "Klausul `HAVING` digunakan khusus untuk memfilter baris kelompok hasil agregasi (di sini: `SUM(total_harga) >= 50000000`), sedangkan klausul `WHERE` menyaring baris individual sebelum proses grouping dilakukan. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Rentan SQL Injection; solusinya adalah menggunakan prepared statement pada query database server.                                                    "
      },
      {
        "key": "B",
        "text": "Rentan Cross-Site Request Forgery (CSRF); solusinya adalah menyisipkan token acak pada form input guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "C",
        "text": "Rentan Denial of Service (DoS); solusinya membatasi panjang input komentar maksimal 200 karakter.                                                    "
      },
      {
        "key": "D",
        "text": "Rentan Broken Authentication; solusinya menggunakan algoritma hashing password Argon2 di backend.                                                    "
      },
      {
        "key": "E",
        "text": "Rentan Cross-Site Scripting (XSS); solusinya menggunakan textContent atau melakukan sanitasi HTML entitas.                                           "
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "DOM-BASED XSS MITIGATION",
      "latex": "\\text{Sink: innerHTML (Vulnerable)} \\xrightarrow{\\text{Refactor}} \\text{textContent} \\lor \\text{DOMPurify.sanitize()}",
      "legend": "• innerHTML: Mengeksekusi tag <script> atau <img onerror=...><br>• textContent: Merender teks aman tanpa interpretasi markup"
    },
    "hints": {
      "concept": "Menyematkan string pengguna langsung ke properti innerHTML membuka celah Cross-Site Scripting (XSS).",
      "execution": "Gantilah innerHTML dengan textContent atau gunakan library sanitasi HTML."
    },
    "explanation": "Penggunaan `innerHTML` secara langsung dengan data mentah dari pengguna menyebabkan kerentanan Cross-Site Scripting (XSS). Penyerang dapat menyuntikkan skrip jahat. Solusi aman adalah menggunakan `textContent` atau sanitasi string HTML sebelum dirender. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "1, 4, 3, 2 karena Call Stack tuntas, disusul Microtask Queue (Promise), lalu Macrotask Queue (setTimeout)."
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4 karena eksekusi baris kode asynchronous JavaScript selalu berurutan sesuai urutan deklarasi."
      },
      {
        "key": "C",
        "text": "1, 4, 2, 3 karena delay timeout bernilai 0 milidetik langsung diproses sebelum promise diselesaikan engine."
      },
      {
        "key": "D",
        "text": "3, 1, 4, 2 karena resolver promise memiliki hak prioritas eksekusi tertinggi di atas thread JavaScript."
      },
      {
        "key": "E",
        "text": "1, 2, 4, 3 karena fungsi setTimeout ditempatkan sebelum pemanggilan promise pada urutan baris program."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "JS EVENT LOOP EXECUTION ORDER",
      "latex": "\\text{Call Stack (Sync)} \\to \\text{Microtask Queue (Promise)} \\to \\text{Macrotask Queue (Timer/IO)}",
      "legend": "• Sinkron: '1' lalu '4'<br>• Microtask: '3'<br>• Macrotask: '2'<br>• Urutan final: 1 -> 4 -> 3 -> 2"
    },
    "hints": {
      "concept": "Urutan eksekusi JavaScript: 1. Kode sinkron di Call Stack; 2. Semua antrean Microtask (Promise .then); 3. Antrean Macrotask/Task (setTimeout).",
      "execution": "1 dan 4 dieksekusi sinkron. Kemudian Promise (microtask) mencetak 3. Terakhir setTimeout (macrotask) mencetak 2."
    },
    "explanation": "Urutan eksekusi: (1) `console.log('1')` dan `console.log('4')` dieksekusi langsung di Call Stack secara sinkron. (2) `Promise.then()` masuk ke Microtask Queue dan dieksekusi segera setelah stack kosong (mencetak '3'). (3) Callback `setTimeout` masuk ke Macrotask Queue dan baru dieksekusi pada iterasi event loop berikutnya (mencetak '2'). Urutan output: 1, 4, 3, 2. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Activity hanya memanggil onResume() ulang tanpa menghancurkan objek view yang sudah ada di memori.                                                        "
      },
      {
        "key": "B",
        "text": "Activity dihancurkan (onPause -> onStop -> onDestroy) lalu diciptakan kembali (onCreate -> onStart -> onResume).                                          "
      },
      {
        "key": "C",
        "text": "Sistem operasi Android langsung mematikan aplikasi dan memunculkan dialog Application Not Responding.                                                     "
      },
      {
        "key": "D",
        "text": "Activity masuk ke status background onStop() secara permanen sampai pengguna menyentuh layar kembali untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "E",
        "text": "Hanya method onSaveInstanceState() yang dieksekusi tanpa memicu method inisialisasi onCreate().                                                           "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menghapus kebutuhan pembuatan layout tampilan antarmuka berekstensi XML atau Jetpack Compose sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "B",
        "text": "Otomatis mengompresi ukuran file APK dan bundle aplikasi menjadi setengah ukuran semula.                                                            "
      },
      {
        "key": "C",
        "text": "Data bertahan hidup melewati perubahan konfigurasi (seperti rotasi layar) tanpa perlu memuat ulang data dari network.                               "
      },
      {
        "key": "D",
        "text": "Memungkinkan eksekusi query basis data secara langsung pada Main Thread tanpa memicu exception.                                                     "
      },
      {
        "key": "E",
        "text": "Menjamin aplikasi dapat berjalan normal tanpa memerlukan izin permissions koneksi internet sama sekali.                                             "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "VIEWMODEL LIFESPAN",
      "latex": "\\text{ViewModel Life} \\ge \\sum \\text{Activity Rotations (Retains State)}",
      "legend": "• ViewModel tetap berada di memori saat Activity re-create karena rotasi layar<br>• Membersihkan resource di onCleared() saat Activity selesai (finish)"
    },
    "hints": {
      "concept": "Tujuan utama ViewModel adalah mengelola dan mempertahankan data untuk UI dengan siklus hidup yang bertahan terhadap perubahan konfigurasi layar.",
      "execution": "Data yang disimpan di ViewModel tidak hilang saat Activity di-destroy dan di-recreate akibat rotasi."
    },
    "explanation": "Objek `ViewModel` dirancang untuk mempertahankan state dan data UI saat terjadi perubahan konfigurasi (seperti rotasi layar), sehingga aplikasi tidak perlu melakukan fetch ulang data dari REST API atau basis data saat Activity dibangun kembali. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Meningkatkan resolusi grafis tekstur gambar karakter secara otomatis saat performa frame rate melonjak.                                                    "
      },
      {
        "key": "B",
        "text": "Mencegah karakter menembus batas dinding pembatas arena pertempuran gim akibat lag koneksi internet.                                                       "
      },
      {
        "key": "C",
        "text": "Menghemat konsumsi daya baterai perangkat dengan menurunkan frekuensi refresh rate layar secara drastis.                                                   "
      },
      {
        "key": "D",
        "text": "Menjaga kecepatan pergerakan objek tetap konsisten per detik terlepas dari fluktuasi frame rate perangkat pemain.                                          "
      },
      {
        "key": "E",
        "text": "Mengunci kecepatan putaran animasi sprite 2D agar selalu tepat berjalan pada 30 frame per detik dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "FRAME-RATE INDEPENDENT MOTION",
      "latex": "\\Delta s = v \\times \\Delta t \\quad (\\text{Displacement} = \\text{Velocity} \\times \\text{Delta Time})",
      "legend": "• 30 FPS: dt = 0.033s -> Gerak = v * 0.033<br>• 60 FPS: dt = 0.016s -> Gerak = v * 0.016<br>• Jarak tempuh per detik identik di semua perangkat"
    },
    "hints": {
      "concept": "Delta time (dt) adalah selisih waktu antara frame saat ini dan frame sebelumnya. Perkalian dengan dt membuat pergerakan berbasis waktu riil, bukan frame.",
      "execution": "Tanpa dt, game di monitor 120Hz akan bergerak 2x lebih cepat dibanding monitor 60Hz."
    },
    "explanation": "Mengalikan perpindahan dengan `deltaTime` (waktu yang dihabiskan untuk menyelesaikan satu frame) menjamin pergerakan objek bersifat independen dari frame rate (frame-rate independent movement), sehingga kecepatan karakter konstan baik di perangkat yang berjalan pada 30 FPS maupun 120 FPS. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Fungsi Math.sqrt() memiliki keterbatasan kapasitas bit sehingga tidak dapat memproses angka floating-point presisi."
      },
      {
        "key": "B",
        "text": "Menghitung akar kuadrat memicu pembagian dengan nol ketika kedua pusat lingkaran saling berhimpitan. "
      },
      {
        "key": "C",
        "text": "Bahasa pemrograman gim tidak menyediakan pustaka pustaka fungsi aljabar trigonometri bawaan di modul matematika."
      },
      {
        "key": "D",
        "text": "Rumus perbandingan kuadrat otomatis menghasilkan vektor normal pantulan fisika pasca tabrakan terjadi."
      },
      {
        "key": "E",
        "text": "Operasi akar kuadrat (square root) membebani siklus CPU secara intensif dibanding perkalian matematika biasa."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "CIRCLE COLLISION OPTIMIZATION",
      "latex": "\\sqrt{dx^2 + dy^2} \\le (r_1 + r_2) \\iff dx^2 + dy^2 \\le (r_1 + r_2)^2",
      "legend": "• Menghindari instruksi sqrt CPU yang mahal<br>• Operasi perkalian dan penjumlahan integer/float jauh lebih cepat"
    },
    "hints": {
      "concept": "Dalam fisika game 2D, operasi Math.sqrt() adalah salah satu instruksi CPU yang paling memakan waktu komputasi.",
      "execution": "Membandingkan kuadrat kedua sisi persamaan menghasilkan logika matematika yang identik dengan biaya komputasi jauh lebih murah."
    },
    "explanation": "Operasi akar kuadrat (`Math.sqrt`) membutuhkan puluhan siklus CPU (clock cycles) yang lambat jika dieksekusi ribuan kali per frame. Mengkuadratkan kedua ruas persamaan ($dx^2 + dy^2 \\le (r_1 + r_2)^2$) memberikan hasil evaluasi logika yang persis sama dengan operasi perkalian aljabar yang jauh lebih cepat. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Beralih ke state Chase untuk bergerak mendekati posisi koordinat pemain hingga jarak serang tercapai."
      },
      {
        "key": "B",
        "text": "Beralih ke state Die dan menghapus instance musuh dari hierarki active game objects di scene."
      },
      {
        "key": "C",
        "text": "Tetap berada pada state Patrol dan mematikan fungsi deteksi tabrakan fisik musuh terhadap rintangan."
      },
      {
        "key": "D",
        "text": "Otomatis me-restart level permainan dari awal karena musuh telah mendeteksi keberadaan target."
      },
      {
        "key": "E",
        "text": "Beralih ke state Idle secara permanen tanpa melakukan animasi tindakan responsif apapun."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "NPC FINITE STATE MACHINE (FSM)",
      "latex": "\\text{Patrol} \\xrightarrow{\\text{Player in View}} \\text{Chase} \\xrightarrow{\\text{Player in Range}} \\text{Attack}",
      "legend": "• Patrol: Jalan santai rute waypoint<br>• Chase: Kejar pemain<br>• Attack: Lakukan pukulan/tembakan"
    },
    "hints": {
      "concept": "FSM AI musuh standar terdiri dari 3 siklus dasar: Patrol (patroli rute) -> Chase (mengejar saat pemain terlihat) -> Attack (menyerang saat dalam jangkauan).",
      "execution": "Kondisi pemain masuk radius pandang memicu transisi dari Patrol ke Chase."
    },
    "explanation": "Dalam pola FSM AI game klasik, ketika entitas dalam kondisi `Patrol` mendeteksi target dalam jangkauan penglihatan (`viewRadius`), trigger tersebut memicu transisi ke state `Chase` (mengejar pemain) hingga berada dalam jarak serang (`attackRange`). Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "25, 35, 45, dan 55 tahun yang mewakili titik tengah rentang umur normal.                                                                     "
      },
      {
        "key": "B",
        "text": "17, 18, 19, 59, 60, dan 61 tahun yang menguji nilai tepat di batas, tepat di bawah, dan tepat di atas batas.                                 "
      },
      {
        "key": "C",
        "text": "0, 10, 50, dan 100 tahun yang merupakan rentang umur manusia secara umum di dunia nyata guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "D",
        "text": "-18 dan -60 tahun yang menguji penanganan sistem terhadap input angka negatif tidak logis.                                                   "
      },
      {
        "key": "E",
        "text": "18 dan 60 tahun saja tanpa perlu memeriksa nilai sebelum dan sesudah batas ambang batas.                                                     "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menulis kode implementasi -> menguji secara manual di browser -> membuat dokumentasi API laporan.                                                        "
      },
      {
        "key": "B",
        "text": "REFACTOR (rancang arsitektur) -> RED (buat unit test) -> GREEN (rilis kode langsung ke production) untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "C",
        "text": "RED (tulis test gagal) -> GREEN (tulis kode minimal agar test lulus) -> REFACTOR (rapikan kode tanpa merusak test).                                      "
      },
      {
        "key": "D",
        "text": "GREEN (buat test yang pasti sukses) -> RED (buat test yang error) -> DEPLOY (unggah aplikasi ke server).                                                 "
      },
      {
        "key": "E",
        "text": "Membuat skema database -> membuat antarmuka frontend -> menulis unit testing di tahapan akhir rilis.                                                     "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "TDD CYCLE (RED - GREEN - REFACTOR)",
      "latex": "\\text{RED (Write Failing Test)} \\to \\text{GREEN (Pass Minimal Code)} \\to \\text{REFACTOR (Clean & Optimize)}",
      "legend": "• RED: Tentukan ekspektasi fungsi sebelum kodenya dibuat<br>• GREEN: Implementasikan solusi paling sederhana<br>• REFACTOR: Hilangkan duplikasi dan optimasi struktur"
    },
    "hints": {
      "concept": "TDD mengikuti irama Red-Green-Refactor: buat tes yang gagal dahulu, implementasikan kode minimal agar tes lulus, lalu bersihkan kode.",
      "execution": "Kata kuncinya adalah RED -> GREEN -> REFACTOR."
    },
    "explanation": "Siklus inti TDD adalah: (1) RED: menulis unit test yang mendefinisikan fitur baru dan memastikannya gagal karena kode belum dibuat, (2) GREEN: menulis kode program minimal yang membuat test berhasil lulus, dan (3) REFACTOR: memperbaiki struktur dan kebersihan kode tanpa mengubah fungsionalitasnya. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "IOException yang merupakan checked exception yang wajib ditangkap menggunakan klausa try-catch."
      },
      {
        "key": "B",
        "text": "Compile-time Error: Variable teks has not been initialized correctly on heap memory.          "
      },
      {
        "key": "C",
        "text": "ArithmeticException karena operasi panjang karakter pada nilai null menghasilkan pembagian tak terdefinisi."
      },
      {
        "key": "D",
        "text": "NullPointerException yang merupakan unchecked exception (turunan langsung dari RuntimeException)."
      },
      {
        "key": "E",
        "text": "IllegalArgumentException yang dilemparkan otomatis oleh method length() milik kelas String.   "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "JAVA EXCEPTION HIERARCHY",
      "latex": "\\text{Throwable} \\to \\text{Exception} \\to \\text{RuntimeException} \\to \\text{NullPointerException (Unchecked)}",
      "legend": "• Checked: Wajib di-catch atau throws (misal IOException, SQLException)<br>• Unchecked: Runtime error akibat kelalaian logika kode"
    },
    "hints": {
      "concept": "Mengakses method atau atribut pada variabel yang bernilai null menghasilkan NullPointerException di runtime (kategori unchecked exception).",
      "execution": "Kode lolos kompilasi, namun saat runtime baris teks.length() melempar NullPointerException."
    },
    "explanation": "Memanggil method (`length()`) pada referensi objek yang bernilai `null` akan melempar `NullPointerException` pada saat runtime. Karena merupakan turunan dari `RuntimeException`, eksepsi ini tergolong unchecked exception (tidak diwajibkan oleh compiler untuk ditangkap secara eksplisit). Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "POST dan PATCH yang digunakan untuk menambahkan entitas rekaman baru dan memperbarui data.                                                 "
      },
      {
        "key": "B",
        "text": "POST dan DELETE yang digunakan untuk memproses transaksi baru dan menghapus record.                                                        "
      },
      {
        "key": "C",
        "text": "CONNECT dan POST yang digunakan untuk membangun tunnel jaringan dan mengirim payload.                                                      "
      },
      {
        "key": "D",
        "text": "PATCH dan POST yang digunakan untuk manipulasi data parsial pada database backend sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "E",
        "text": "GET dan PUT yang digunakan untuk mengambil data serta mengganti data sumber daya secara utuh.                                              "
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "HTTP METHODS IDEMPOTENCY MATRIX",
      "latex": "f(f(x)) = f(x) \\implies \\text{Idempotent: GET, PUT, DELETE, HEAD, OPTIONS}",
      "legend": "• GET: Safe & Idempotent<br>• PUT: Idempotent (replace resource)<br>• DELETE: Idempotent (hapus resource berkali-kali tetap hilang)<br>• POST: Non-idempotent (bikin entitas baru setiap dipanggil)"
    },
    "hints": {
      "concept": "Method idempotent: efek pemanggilan N kali sama dengan 1 kali pemanggilan. GET, PUT, DELETE adalah idempotent. POST bukan idempotent.",
      "execution": "GET (hanya membaca) dan PUT (mengganti utuh state resource) keduanya adalah idempotent."
    },
    "explanation": "GET, PUT, dan DELETE adalah method HTTP yang bersifat idempotent menurut spesifikasi RFC 7231. Memanggil `PUT` berkali-kali dengan payload yang sama akan menghasilkan state resource yang persis sama. Sebaliknya, `POST` tidak idempotent karena setiap eksekusi akan membuat entitas data baru yang berbeda di server. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "44x44 pt (iOS) atau 48x48 dp (Android) untuk menyesuaikan dengan luas permukaan ujung jari manusia.                                                       "
      },
      {
        "key": "B",
        "text": "16x16 dp/pt yang merupakan ukuran standar ikon teks inline di dalam paragraf artikel web.                                                                 "
      },
      {
        "key": "C",
        "text": "100x100 dp/pt yang wajib diterapkan pada setiap komponen interaktif formulir pendaftaran.                                                                 "
      },
      {
        "key": "D",
        "text": "24x24 dp/pt yang merupakan ukuran default bounding box aset vektor ikon sistem.                                                                           "
      },
      {
        "key": "E",
        "text": "80x80 dp/pt untuk memastikan tombol terlihat jelas oleh pengguna dari jarak pandang dua meter dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MINIMUM ACCESSIBLE TOUCH TARGET",
      "latex": "\\text{Apple HIG} \\ge 44 \\times 44\\text{ pt}, \\quad \\text{Google Material} \\ge 48 \\times 48\\text{ dp}",
      "legend": "• Menghindari error miss-click pada layar sentuh ponsel<br>• Standar WCAG 2.1 Success Criterion 2.5.5 (Target Size)"
    },
    "hints": {
      "concept": "Pedoman desain antarmuka mobile menetapkan 44x44 pt (Apple) dan 48x48 dp (Android) sebagai ukuran minimal area sentuh ramah jari.",
      "execution": "Ukuran ini memperhitungkan rata-rata luas sentuhan bantalan jari manusia (sekitar 7-10 mm)."
    },
    "explanation": "Google Material Design menetapkan minimal touch target 48x48 dp, sementara Apple HIG menetapkan minimal 44x44 pt. Hal ini dirancang agar elemen interaktif dapat ditekan dengan nyaman oleh jemari manusia tanpa memicu kesalahan klik pada elemen di sebelahnya. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Perusahaan hanya wajib membayar royalti tahunan kepada Free Software Foundation tanpa membagikan kode."
      },
      {
        "key": "B",
        "text": "Seluruh source code aplikasi perusahaan wajib dilisensikan di bawah GPLv3 dan dibuka untuk publik."
      },
      {
        "key": "C",
        "text": "Perusahaan bebas mendistribusikan aplikasi secara closed-source selama nama pembuat pustaka tidak diubah."
      },
      {
        "key": "D",
        "text": "Lisensi GPLv3 otomatis gugur ketika aplikasi dijual dengan harga nominal tertentu di pasar komersial."
      },
      {
        "key": "E",
        "text": "Perusahaan hanya wajib menyertakan file binary executable tanpa perlu menyediakan dokumentasi teknis."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Merahasiakan insiden kebocoran tersebut dari publik selamanya demi menjaga nilai saham perusahaan."
      },
      {
        "key": "B",
        "text": "Menghapus seluruh rekaman log server dan database cadangan agar jejak digital peretas hilang seketika."
      },
      {
        "key": "C",
        "text": "Menyampaikan pemberitahuan tertulis kepada subjek data dan lembaga terkait maksimal 3x24 jam. "
      },
      {
        "key": "D",
        "text": "Memberikan ganti rugi finansial tunai secara langsung kepada seluruh penduduk Indonesia dalam waktu 24 jam."
      },
      {
        "key": "E",
        "text": "Menutup permanen operasional server aplikasi dan membubarkan entitas bisnis perusahaan seketika."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "UU PDP DATA BREACH NOTIFICATION TIMELINE",
      "latex": "\\text{Data Breach Detected} \\implies \\text{Mandatory Written Notice within } 3 \\times 24 \\text{ hours (72 hours)}",
      "legend": "• Pasal 46 UU PDP: Wajib menyampaikan pemberitahuan ke subjek data & lembaga berwenang<br>• Memuat rincian data terkompromi & kontak penanganan"
    },
    "hints": {
      "concept": "Pasal 46 UU PDP mewajibkan pengendali data memberitahukan insiden kebocoran data secara tertulis paling lambat 3 x 24 jam.",
      "execution": "Batas waktu pelaporan resmi kebocoran data di Indonesia adalah 3x24 jam."
    },
    "explanation": "Berdasarkan Pasal 46 UU PDP No. 27 Tahun 2022, dalam hal terjadi kegagalan pelindungan data pribadi (kebocoran), Pengendali Data Pribadi wajib menyampaikan pemberitahuan secara tertulis paling lambat 3 x 24 jam (72 jam) kepada Subjek Data Pribadi dan lembaga yang berwenang. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Best case O(n) dan worst case O(n^2) karena elemen harus diperiksa melalui nested loop bersarang.       "
      },
      {
        "key": "B",
        "text": "Best case O(log n) dan worst case O(n) karena ruang pencarian menyusut secara eksponensial di setiap langkah."
      },
      {
        "key": "C",
        "text": "Best case O(1) dan worst case O(n) karena jika elemen tidak ada maka seluruh array wajib dipindai sekuensial."
      },
      {
        "key": "D",
        "text": "Best case O(1) dan worst case O(log n) karena target dapat ditemukan di titik tengah awal atau melalui pembagian biner."
      },
      {
        "key": "E",
        "text": "Best case O(n log n) dan worst case O(n log n) karena array wajib di-reorganisasi ulang setiap iterasi. "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "BINARY SEARCH TIME COMPLEXITY",
      "latex": "T_{\\text{best}} = O(1), \\quad T_{\\text{worst}} = O(\\log_2 n)",
      "legend": "• Best case: Elemen target tepat berada di indeks tengah pertama ($O(1)$)<br>• Worst case: Setiap langkah membagi n dengan 2 hingga tersisa 1 elemen ($O(\\log n)$)"
    },
    "hints": {
      "concept": "Binary Search membagi dua area pencarian pada setiap iterasi. Jika elemen tengah adalah target, itu kasus terbaik O(1). Jika pencarian sampai ujung, kasus terburuknya adalah O(log n).",
      "execution": "Best case = O(1), Worst case = O(log n)."
    },
    "explanation": "Pada Binary Search, best case terjadi saat elemen yang dicari tepat berada di posisi tengah array pada pengecekan pertama ($O(1)$). Worst case terjadi saat elemen berada di ujung atau tidak ditemukan sama sekali, di mana ruang pencarian berukuran $n$ dibagi dua berulang kali sebanyak $\\log_2 n$ langkah ($O(\\log n)$). Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Interface Segregation Principle dengan membagi interface besar menjadi interface yang sangat kecil.                                                 "
      },
      {
        "key": "B",
        "text": "Liskov Substitution Principle di mana objek subclass harus dapat menggantikan objek superclassnya.                                                  "
      },
      {
        "key": "C",
        "text": "Single Responsibility Principle di mana sebuah kelas hanya memiliki satu fungsi logging terpusat guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "D",
        "text": "Law of Demeter di mana objek hanya boleh berkomunikasi dengan objek tetangga terdekatnya.                                                           "
      },
      {
        "key": "E",
        "text": "Open/Closed Principle (OCP) di mana entitas terbuka untuk perluasan tetapi tertutup untuk modifikasi.                                               "
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "SOLID - OPEN/CLOSED PRINCIPLE (OCP)",
      "latex": "\\text{Open for Extension} \\land \\text{Closed for Modification}",
      "legend": "• Implementasi: Gunakan Interface PaymentStrategy<br>• Menambah metode pembayaran baru cukup membuat kelas baru implementor interface tanpa ubah CheckoutService"
    },
    "hints": {
      "concept": "Open/Closed Principle (huruf 'O' dalam SOLID) menyatakan entitas software harus terbuka untuk perluasan (open for extension) tetapi tertutup untuk modifikasi (closed for modification).",
      "execution": "Menambah fitur tanpa mengubah kode lama adalah definisi inti OCP."
    },
    "explanation": "Open/Closed Principle (OCP) menyatakan bahwa entitas perangkat lunak harus terbuka untuk diekstensi (menambahkan metode pembayaran baru) tetapi tertutup untuk modifikasi (tidak perlu mengedit kode `CheckoutService` yang sudah stabil). Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Jika promise api.get di-reject akibat network down, eksekusi melompat ke blok catch dan mengembalikan null.                                         "
      },
      {
        "key": "B",
        "text": "Kata kunci await memblokir seluruh thread utama browser sehingga animasi halaman web membeku untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "C",
        "text": "Fungsi fetchUserProfile mengembalikan nilai primitif null secara langsung tanpa dibungkus Promise.                                                  "
      },
      {
        "key": "D",
        "text": "Blok try-catch tidak mampu menangkap rejection dari fungsi asynchronous yang menggunakan await.                                                     "
      },
      {
        "key": "E",
        "text": "Fungsi akan memicu TypeError karena kata kunci async tidak kompatibel dengan penanganan try-catch.                                                  "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ASYNC/AWAIT ERROR HANDLING FLOW",
      "latex": "\\text{Promise Rejected} \\implies \\text{await throws Error} \\implies \\text{Handled in catch block}",
      "legend": "• await membongkar hasil promise yang resolved<br>• Rejection diubah menjadi exception yang ditangkap oleh blok catch"
    },
    "hints": {
      "concept": "Di dalam fungsi async, penanganan error untuk Promise yang rejected dapat dilakukan secara natural dan elegan menggunakan blok try-catch.",
      "execution": "Jika api.get gagal/reject, aliran kode langsung melompat ke blok catch dan mengembalikan null."
    },
    "explanation": "Pada fungsi `async`, ketika sebuah Promise yang di-`await` mengalami rejection (gagal/error), runtime JavaScript akan melempar exception tersebut ke blok `catch`. Di sana pesan kesalahan dicatat ke console dan fungsi secara aman mengembalikan `null`. Jawaban: A.",
    "isDiagnostic": false
  },
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
      {
        "key": "A",
        "text": "Melakukan bypass pengujian dan langsung merilis container Docker ke cluster Kubernetes production secara paksa sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "B",
        "text": "Menghapus commit terakhir dari branch main remote secara permanen menggunakan perintah git push --force.                                                            "
      },
      {
        "key": "C",
        "text": "Menghentikan pipeline seketika, mencegah rilis ke production, mengirim notifikasi alert ke tim, dan auto-rollback staging.                                          "
      },
      {
        "key": "D",
        "text": "Menonaktifkan server staging dan memindahkan seluruh database produksi ke cloud provider lain seketika.                                                             "
      },
      {
        "key": "E",
        "text": "Mengubah kode status HTTP response pada smoke test menjadi 200 OK agar proses build dapat tetap selesai.                                                            "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "CI/CD PIPELINE QUALITY GATE",
      "latex": "\\text{Smoke Test Failed (exit 1)} \\implies \\text{Block Promotion} \\land \\text{Trigger Auto-Rollback} \\land \\text{Alert}",
      "legend": "• Quality Gate: Mencegah kode cacat mencapai production<br>• Fail-Fast principle: Kegagalan seawal mungkin demi menjaga stabilitas sistem"
    },
    "hints": {
      "concept": "Prinsip inti CI/CD adalah Fail-Fast: jika pengujian smoke test gagal di staging, deployment ke production harus langsung diblokir dan environment dikembalikan ke state stabil.",
      "execution": "Pilihan yang menerapkan mitigasi aman dan memblokir promosi ke production adalah B."
    },
    "explanation": "Pada pipeline CI/CD profesional, kegagalan automated smoke test di lingkungan staging memicu penghentian pipeline seketika untuk mencegah kode cacat dipromosikan ke production. Sistem juga melakukan rollback otomatis ke versi stabil sebelumnya serta mengirimkan alert notifikasi kepada tim pengembang. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Kelas Persegi tidak mengimplementasikan interface Cloneable untuk menduplikasi objek secara mendalam.                                                         "
      },
      {
        "key": "B",
        "text": "Method hitungLuas() tidak diberi anotasi @Override pada deklarasi di dalam kelas anak Persegi.                                                                "
      },
      {
        "key": "C",
        "text": "Variabel panjang dan lebar dideklarasikan dengan access modifier protected daripada public statis.                                                            "
      },
      {
        "key": "D",
        "text": "Subclass Persegi merusak invarian kelas induk di mana pengubahan lebar juga ikut mengubah panjang secara tersembunyi.                                         "
      },
      {
        "key": "E",
        "text": "Kelas PersegiPanjang tidak dijadikan abstract class dengan method abstrak murni tanpa implementasi dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "LISKOV SUBSTITUTION PRINCIPLE (LSP)",
      "latex": "\\text{If } S \\text{ is a subtype of } T, \\text{ then objects of type } T \\text{ may be replaced with } S \\text{ without altering correctness}",
      "legend": "• Subclass Persegi melanggar ekspektasi perilaku superclass PersegiPanjang (invarian: ubah lebar tidak ubah panjang)"
    },
    "hints": {
      "concept": "LSP mensyaratkan bahwa subclass harus dapat menggantikan superclass tanpa merusak kebenaran program. Klien yang menggunakan PersegiPanjang berekspektasi bahwa setLebar(l) hanya mengubah lebar.",
      "execution": "Pada Persegi, memanggil setLebar() secara tak terduga mengubah panjang juga, merusak kalkulasi klien yang memegang referensi PersegiPanjang."
    },
    "explanation": "LSP menyatakan bahwa objek subclass harus dapat menggantikan superclass tanpa mengubah ekspektasi perilaku sistem. Pada kelas `Persegi`, mengubah atribut lebar melalui `setLebar()` secara sepihak mengubah nilai panjang, melanggar kontrak perilaku `PersegiPanjang` di mana panjang dan lebar dapat dimodifikasi secara independen. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Memaksa JVM menyimpan seluruh instansiasi objek DatabaseConnection langsung ke memori non-volatile SSD."
      },
      {
        "key": "B",
        "text": "Mengizinkan banyak instance objek diciptakan secara paralel saat beban thread server melampaui ambang batas."
      },
      {
        "key": "C",
        "text": "Menghapus kebutuhan blok synchronized saat method getInstance() dipanggil oleh thread yang berbeda."
      },
      {
        "key": "D",
        "text": "Mengamankan kredensial password koneksi basis data dari teknik pembacaan memory dump heap JVM."
      },
      {
        "key": "E",
        "text": "Mencegah reordering instruksi kompilator JVM yang dapat menyebabkan thread lain membaca objek setengah jadi."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "DOUBLE-CHECKED LOCKING & VOLATILE MEMORY BARRIER",
      "latex": "\\text{instance = new Obj()} \\implies \\{ 1.\\text{Alloc mem}, \\; 2.\\text{Init ctor}, \\; 3.\\text{Assign ref} \\}",
      "legend": "• Tanpa volatile: Compiler dapat me-reorder instruksi menjadi 1 -> 3 -> 2<br>• Akibat: Thread lain melihat instance != null padahal konstruktor belum selesai dieksekusi"
    },
    "hints": {
      "concept": "Keyword volatile di Java menyediakan jaminan visibilitas memori dan mencegah instruction reordering (memory barrier) oleh CPU/compiler.",
      "execution": "Tanpa volatile, alokasi memori bisa di-reorder sehingga thread lain memperoleh referensi objek yang belum selesai diinisialisasi."
    },
    "explanation": "Operasi `new DatabaseConnection()` melibatkan 3 langkah di level instruksi: (1) alokasi memori, (2) eksekusi konstruktor, dan (3) penugasan referensi ke variabel `instance`. Tanpa keyword `volatile`, JVM dapat melakukan instruksi reordering (1 -> 3 -> 2), menyebabkan thread lain melihat `instance != null` padahal inisialisasi objek belum tuntas. `volatile` bertindak sebagai memory barrier yang mencegah reordering tersebut. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Karena objek masih memiliki rantai referensi hidup yang terhubung ke GC Root melalui variabel koleksi statis cache.                                  "
      },
      {
        "key": "B",
        "text": "Karena objek dalam heap Java hanya bisa dibersihkan jika server dimatikan dan dinyalakan ulang secara fisik.                                         "
      },
      {
        "key": "C",
        "text": "Karena Garbage Collector hanya membersihkan memori variabel primitif dan tidak memproses objek bertipe kelas.                                        "
      },
      {
        "key": "D",
        "text": "Karena ukuran memori heap JVM dibatasi secara kaku maksimal 64 megabyte oleh sistem operasi Linux guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "E",
        "text": "Karena kelas UserData tidak mengimplementasikan method finalize() untuk memicu penghapusan otomatis.                                                 "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GARBAGE COLLECTION REACHABILITY ANALYSIS",
      "latex": "\\text{GC Root (Static Variable)} \\xrightarrow{\\text{Strong Reference}} \\text{List Cache} \\xrightarrow{} \\text{UserData Object}",
      "legend": "• Objek yang masih dapat dijangkau (reachable) dari GC Roots TIDAK AKAN PERNAH disapu oleh GC<br>• Solusi: Gunakan WeakReference atau Eviction Policy (LRU Cache)"
    },
    "hints": {
      "concept": "Garbage Collector hanya mengklaim objek yang tidak lagi dapat dijangkau (unreachable) dari GC Roots (seperti variabel statis, stack frames aktif).",
      "execution": "Variabel static hidup sepanjang siklus hidup classloader aplikasi, sehingga semua objek di dalamnya dianggap tetap aktif oleh GC."
    },
    "explanation": "Variabel berstatus `static` hidup di method area/metaspace sepanjang siklus hidup aplikasi dan bertindak sebagai GC Root. Karena list statis tersebut terus memegang strong reference ke setiap objek `UserData`, Garbage Collector menganggap objek tersebut masih aktif dan 'reachable', sehingga memori heap tidak dapat dibebaskan hingga memicu OutOfMemoryError. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Tabel memiliki lebih dari satu candidate key komposit yang saling tumpang tindih atribut pembentuknya untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "B",
        "text": "Terdapat ketergantungan fungsional NIP_Dosen -> Kode_Keahlian di mana determinan NIP_Dosen bukan candidate key superkey.                                   "
      },
      {
        "key": "C",
        "text": "Atribut NIM tidak dapat digunakan sebagai foreign key ke tabel master data mahasiswa universitas.                                                          "
      },
      {
        "key": "D",
        "text": "Nilai pada kolom NIP_Dosen masih mengandung repeating groups yang melanggar aturan atomisitas 1NF.                                                         "
      },
      {
        "key": "E",
        "text": "Atribut Kode_Keahlian bukan merupakan atribut prima (prime attribute) dalam struktur relasi tabel.                                                         "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Database langsung menolak eksekusi query karena urutan klausa WHERE terbalik dari urutan indeks komposit sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "B",
        "text": "Database dipaksa melakukan Full Table Scan karena kolom status_transaksi diletakkan di baris pertama WHERE.                                                    "
      },
      {
        "key": "C",
        "text": "Database tetap memanfaatkan indeks secara efisien karena indeks dimulai dengan created_at (Leftmost Prefix cocok).                                             "
      },
      {
        "key": "D",
        "text": "Database otomatis memecah indeks komposit menjadi dua indeks tunggal terpisah di memori RAM server.                                                            "
      },
      {
        "key": "E",
        "text": "Indeks hanya bisa digunakan jika seluruh kolom pada tabel transaksi disertakan dalam klausa SELECT.                                                            "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "B-TREE COMPOSITE INDEX & LEFTMOST PREFIX",
      "latex": "\\text{Index: } (A, B) \\implies \\text{Filter on } (A) \\lor (A \\land B) \\text{ uses Index}",
      "legend": "• Leftmost prefix: created_at adalah kolom pertama indeks komposit<br>• Urutan penulisan di WHERE (A AND B vs B AND A) dioptimasi otomatis oleh Query Optimizer"
    },
    "hints": {
      "concept": "Leftmost prefix rule mensyaratkan kolom pertama indeks komposit hadir dalam kondisi WHERE. Modern RDBMS Query Optimizer mampu mereorganisasi urutan operator AND.",
      "execution": "created_at ada di dalam query sebagai filter rentang (range scan), sehingga database tetap dapat memanfaatkan indeks B-Tree."
    },
    "explanation": "Query Optimizer pada RDBMS modern (seperti PostgreSQL atau MySQL) secara otomatis mengevaluasi kondisi komutatif `AND`. Karena kolom pertama dari indeks komposit (`created_at`) digunakan dalam filter rentang, optimizer tetap dapat menggunakan indeks tersebut untuk memangkas pembacaan disk (Range Scan) secara efisien sesuai Leftmost Prefix Rule. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Dirty Read di mana Transaksi 1 membaca saldo Rekening B yang belum di-commit oleh Transaksi 2.                                                       "
      },
      {
        "key": "B",
        "text": "Phantom Read di mana jumlah baris tabel rekening berubah saat dieksekusi dalam satu transaksi.                                                       "
      },
      {
        "key": "C",
        "text": "Non-Repeatable Read di mana nilai saldo rekening berubah di tengah pembacaan Transaksi 1 dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "D",
        "text": "Deadlock di mana kedua transaksi saling menunggu kunci resource dilepaskan oleh transaksi lainnya.                                                   "
      },
      {
        "key": "E",
        "text": "Cascade Rollback di mana seluruh transaksi database lain di server otomatis terhapus.                                                                "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "DEADLOCK CYCLE IN TRANSACTION PROCESSING",
      "latex": "T_1 \\xrightarrow{\\text{holds}} \\text{Lock}(A) \\xrightarrow{\\text{waits for}} \\text{Lock}(B) \\xleftarrow{\\text{holds}} T_2 \\xrightarrow{\\text{waits for}} \\text{Lock}(A)",
      "legend": "• Siklus saling tunggu melingkar (Circular Wait)<br>• Mitigasi: RDBMS Deadlock Detector memilih 1 transaksi sebagai korban (victim) lalu di-ROLLBACK"
    },
    "hints": {
      "concept": "Deadlock terjadi saat transaksi T1 memegang kunci A dan menunggu kunci B, sementara transaksi T2 memegang kunci B dan menunggu kunci A.",
      "execution": "Situasi saling tunggu melingkar tanpa akhir ini dinamakan Deadlock."
    },
    "explanation": "Situasi di mana dua atau lebih transaksi saling menunggu resource yang sedang dikunci oleh transaksi lain dalam siklus melingkar (circular wait) dinamakan Deadlock. Database engine akan mendeteksi siklus ini dan secara otomatis membatalkan (ROLLBACK) salah satu transaksi korban (victim) untuk memecah kebuntuan. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Di dalam localStorage browser agar token dapat dibaca dan dimanipulasi dengan mudah oleh skrip JavaScript."
      },
      {
        "key": "B",
        "text": "Di dalam sessionStorage browser agar token otomatis terhapus saat tab browser pengguna ditutup.  "
      },
      {
        "key": "C",
        "text": "Di dalam atribut data-token pada tag HTML body agar dapat diakses oleh seluruh elemen DOM halaman."
      },
      {
        "key": "D",
        "text": "Di dalam parameter query string URL agar token selalu disertakan pada setiap navigasi tautan web."
      },
      {
        "key": "E",
        "text": "Di dalam HttpOnly, Secure, dan SameSite Cookie sehingga skrip JavaScript pihak ketiga tidak dapat mengaksesnya."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "JWT SECURITY ARCHITECTURE",
      "latex": "\\text{JWT} = \\text{Base64}(H) \\, . \\, \\text{Base64}(P) \\, . \\, \\text{HMAC}(\\text{Secret}, H.P)",
      "legend": "• localStorage / sessionStorage: Rentan XSS (dapat dicuri via document.cookie / window.localStorage)<br>• HttpOnly Cookie: Kebal pembacaan via JavaScript DOM API"
    },
    "hints": {
      "concept": "Cookie dengan atribut HttpOnly tidak dapat dibaca oleh kode JavaScript di browser (misal melalui document.cookie).",
      "execution": "Kombinasi HttpOnly, Secure (hanya HTTPS), dan SameSite (cegah CSRF) adalah standar industri OWASP untuk menyimpan token otentikasi."
    },
    "explanation": "Menyimpan JWT di `localStorage` sangat berbahaya karena rentan dicuri jika aplikasi memiliki celah XSS. Pendekatan yang direkomendasikan OWASP adalah menyimpan token otentikasi di dalam Cookie dengan flag `HttpOnly` (memblokir akses skrip JS), `Secure` (hanya dikirim via HTTPS), dan `SameSite=Strict/Lax` (memitigasi CSRF). Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Sebagai mekanisme CORS Preflight untuk memverifikasi apakah server mengizinkan method dan custom header tersebut.                                         "
      },
      {
        "key": "B",
        "text": "Untuk menguji kecepatan latensi koneksi internet antara browser client dan data center server API.                                                        "
      },
      {
        "key": "C",
        "text": "Untuk mengunduh sertifikat SSL/TLS publik server API sebelum saluran enkripsi HTTPS dibangun.                                                             "
      },
      {
        "key": "D",
        "text": "Karena server API mengalami kelebihan beban sehingga meminta browser mengirim request penyeimbang beban guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "E",
        "text": "Sebagai bentuk kompresi payload biner untuk menghemat kuota transmisi jaringan pengguna.                                                                  "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "CORS PREFLIGHT PROTOCOL",
      "latex": "\\text{Non-Simple Request} \\implies \\text{Browser sends HTTP OPTIONS} \\xrightarrow{\\text{Server 204 with CORS Headers}} \\text{Actual POST/PUT}",
      "legend": "• Pemicu preflight: Content-Type application/json, Custom header (Authorization), Method PUT/DELETE/PATCH"
    },
    "hints": {
      "concept": "Permintaan cross-origin yang bukan 'simple request' (misalnya menyertakan header Authorization atau Content-Type JSON) memicu browser mengirimkan preflight OPTIONS request.",
      "execution": "Preflight memastikan server memahami dan menyetujui request sebenarnya sebelum data sensitif dikirim."
    },
    "explanation": "Spesifikasi W3C Cross-Origin Resource Sharing (CORS) mengharuskan browser mengirimkan preflight request menggunakan method `OPTIONS` untuk jenis permintaan non-simple (seperti menyertakan header `Authorization` atau payload JSON). Preflight bertujuan memeriksa izin server sebelum request utama yang sesungguhnya dikirimkan. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Browser langsung mencetak string 'Timer selesai' karena timer macrotask memiliki prioritas lebih tinggi untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "B",
        "text": "Terjadi Microtask Starvation di mana timer setTimeout dan rendering UI tidak pernah dieksekusi (browser membeku).                                            "
      },
      {
        "key": "C",
        "text": "V8 engine membatasi rekursi maksimal 10.000 kali lalu secara otomatis melempar RangeError: Maximum call stack.                                               "
      },
      {
        "key": "D",
        "text": "Fungsi setTimeout otomatis membatalkan antrean promise dan membersihkan microtask queue.                                                                     "
      },
      {
        "key": "E",
        "text": "Sistem operasi komputer langsung mengalami restart paksa akibat kebocoran memori RAM fisik.                                                                  "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Paket data internet yang melintasi Main Thread otomatis kehilangan enkripsi keamanan protokol HTTPS sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "B",
        "text": "Main Thread pada sistem Android tidak memiliki alokasi hak akses izin internet di AndroidManifest.xml.                                                    "
      },
      {
        "key": "C",
        "text": "Operasi I/O jaringan yang lambat akan memblokir thread UI, menyebabkan frame drop dan memicu dialog ANR.                                                  "
      },
      {
        "key": "D",
        "text": "Driver kartu jaringan seluler pada smartphone hanya dapat berkomunikasi dengan thread bertipe daemon.                                                     "
      },
      {
        "key": "E",
        "text": "Sistem operasi Android membatasi penggunaan RAM pada Main Thread maksimal sebesar 128 kilobyte.                                                           "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "ANDROID ANR (APPLICATION NOT RESPONDING) TRIGGER",
      "latex": "\\text{Main Thread Blocked} > 5\\text{ seconds} \\implies \\text{Android OS triggers ANR Dialog}",
      "legend": "• Main Thread bertugas me-render UI 60/120 fps (16ms per frame)<br>• Solusi: Gunakan Coroutines (Dispatchers.IO) atau WorkManager"
    },
    "hints": {
      "concept": "Main Thread (UI Thread) bertanggung jawab menggambar layar dan merespons sentuhan pengguna. Memblokir Main Thread dengan operasi jaringan akan membekukan UI.",
      "execution": "Jika Main Thread terblokir selama 5 detik, sistem Android memunculkan dialog Application Not Responding (ANR)."
    },
    "explanation": "Main Thread pada Android bertanggung jawab merender antarmuka pengguna pada 60-120 fps. Operasi jaringan bersifat lambat dan tak terduga (I/O blocking). Jika dijalankan di Main Thread, aplikasi akan membeku dan memicu dialog Application Not Responding (ANR). Android melempar `NetworkOnMainThreadException` untuk memaksa developer menjalankan I/O pada background thread (misalnya menggunakan Coroutines `Dispatchers.IO`). Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Mengaktifkan method fallbackToDestructiveMigration() pada Room database builder saat rilis aplikasi.                                               "
      },
      {
        "key": "B",
        "text": "Menghapus file database SQLite lokal secara manual di penyimpanan internal perangkat pengguna.                                                     "
      },
      {
        "key": "C",
        "text": "Mengubah nama file database menjadi nama baru sehingga sistem membuat basis data kosong yang baru.                                                 "
      },
      {
        "key": "D",
        "text": "Mendefinisikan objek Migration(1, 2) yang menjalankan perintah SQL ALTER TABLE dengan nilai DEFAULT yang valid.                                    "
      },
      {
        "key": "E",
        "text": "Menurunkan nomor versi database menjadi 0 agar Room mengabaikan perbedaan skema tabel dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "ROOM DATABASE MIGRATION STRATEGY",
      "latex": "\\text{Migration}(1, 2) \\colon \\text{database.execSQL(\"ALTER TABLE users ADD COLUMN email TEXT NOT NULL DEFAULT ''\")}",
      "legend": "• fallbackToDestructiveMigration(): Menghapus seluruh data tabel lama (DATA LOSS)<br>• Manual Migration: Menjaga integritas data pengguna tanpa kehilangan record"
    },
    "hints": {
      "concept": "fallbackToDestructiveMigration() menghapus semua data lama pengguna. Solusi yang benar untuk production adalah membuat objek Migration eksplisit.",
      "execution": "Migration(1, 2) dengan eksekusi ALTER TABLE dan nilai DEFAULT memastikan data lama tetap aman."
    },
    "explanation": "Menggunakan `fallbackToDestructiveMigration()` akan menghapus seluruh data pengguna yang tersimpan saat skema berubah. Solusi yang tepat pada aplikasi production adalah menyediakan skrip `Migration(1, 2)` eksplisit menggunakan perintah SQL `ALTER TABLE` disertai nilai `DEFAULT` agar integritas data pengguna lama tetap terjaga. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menggunakan file gambar PNG resolusi tinggi 4K individual terpisah untuk setiap sprite karakter gim."
      },
      {
        "key": "B",
        "text": "Menaikkan frekuensi clock CPU komputer pemain menggunakan perangkat lunak overclocking pihak ketiga."
      },
      {
        "key": "C",
        "text": "Merender setiap musuh pada kamera viewport terpisah dengan shader material yang berbeda-beda.  "
      },
      {
        "key": "D",
        "text": "Menonaktifkan v-sync dan mengubah format penyimpanan aset gambar menjadi format GIF animasi.   "
      },
      {
        "key": "E",
        "text": "Menggabungkan seluruh sprite ke dalam Texture Atlas (Sprite Sheet) tunggal dan memanfaatkan Dynamic Batching."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "GPU DRAW CALL BATCHING",
      "latex": "\\text{Separate Textures} \\implies N \\text{ State Changes} \\quad \\text{vs} \\quad \\text{Texture Atlas} \\implies 1 \\text{ Batched Draw Call}",
      "legend": "• Setiap pergantian tekstur memaksa GPU melakukan state switch yang mahal<br>• Sprite Sheet memungkinkan penggabungan geometri ke dalam 1 batch render"
    },
    "hints": {
      "concept": "Draw Call adalah instruksi dari CPU ke GPU untuk menggambar objek. Pergantian tekstur individual memicu Draw Call baru.",
      "execution": "Texture Atlas menyatukan banyak gambar kecil ke satu tekstur besar sehingga GPU dapat merender ratusan sprite sekaligus dalam 1 Draw Call."
    },
    "explanation": "Tingginya jumlah Draw Call biasanya disebabkan oleh pergantian state material dan tekstur pada GPU. Dengan menggabungkan ribuan aset sprite ke dalam satu lembar gambar besar (Texture Atlas / Sprite Sheet), game engine dapat melakukan 'Batching'—merender ratusan objek sekaligus hanya dengan 1 panggilan Draw Call ke GPU. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Alokasi dan dealokasi memori berulang memicu Garbage Collector (GC); solusinya menerapkan Object Pooling."
      },
      {
        "key": "B",
        "text": "Kelebihan beban GPU; solusinya adalah menurunkan resolusi layar gim menjadi format monokrom.  "
      },
      {
        "key": "C",
        "text": "Koneksi internet tidak stabil; solusinya adalah mewajibkan pemain bermain dalam mode single player offline."
      },
      {
        "key": "D",
        "text": "Hard disk membaca file audio peluru secara lambat; solusinya adalah menghapus seluruh efek suara tembakan."
      },
      {
        "key": "E",
        "text": "Suhu prosesor CPU meningkat drastis; solusinya adalah menurunkan kecepatan game loop menjadi 10 FPS."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OBJECT POOLING PATTERN",
      "latex": "\\text{Pool Init (N items)} \\xrightarrow{\\text{Acquire (Set Active)}} \\text{In Use} \\xrightarrow{\\text{Release (Set Inactive)}} \\text{Return to Pool}",
      "legend": "• Menghindari alokasi heap baru secara konstan (`new`/`Instantiate`)<br>• Meniadakan lonjakan kerja Garbage Collector (Stop-The-World pause)"
    },
    "hints": {
      "concept": "Membuat (Instantiate) dan menghancurkan (Destroy) ribuan objek secara dinamis mengotori heap memori, memicu Garbage Collector bekerja keras menghentikan sementara jalannya game.",
      "execution": "Solusinya adalah Object Pooling: membuat pool objek sekali di awal, lalu mengaktifkan/menonaktifkan objek kembali."
    },
    "explanation": "Pembuatan dan penghancuran objek peluru secara terus-menerus menyebabkan fragmentasi memori heap dan memicu siklus Garbage Collection (GC) yang menghentikan eksekusi sementara (GC pause stutter). Pola desain `Object Pooling` memecahkan masalah ini dengan mendaur ulang objek yang sudah ada (mengubah status aktif/non-aktif) tanpa alokasi memori baru. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Meningkatkan ukuran radius bounding box objek musuh menjadi sepuluh kali lipat dari ukuran visual aslinya."
      },
      {
        "key": "B",
        "text": "Menerapkan Continuous Collision Detection (CCD) menggunakan teknik Raycasting atau Swept Volume."
      },
      {
        "key": "C",
        "text": "Menurunkan kecepatan clock prosesor fisika engine agar objek bergerak lebih lambat di layar pemain."
      },
      {
        "key": "D",
        "text": "Mengubah bentuk collider kotak AABB menjadi jaring poligon tak beraturan (irregular mesh collider)."
      },
      {
        "key": "E",
        "text": "Menghapus komponen Rigidbody dan memproses tabrakan secara manual pada event rendering frame."
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "3 jalur pengujian independen."
      },
      {
        "key": "B",
        "text": "7 jalur pengujian independen."
      },
      {
        "key": "C",
        "text": "5 jalur pengujian independen."
      },
      {
        "key": "D",
        "text": "9 jalur pengujian independen."
      },
      {
        "key": "E",
        "text": "21 jalur pengujian independen."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "MCCABE CYCLOMATIC COMPLEXITY FORMULA",
      "latex": "V(G) = E - N + 2P = 12 - 9 + 2(1) = 5",
      "legend": "• E: Jumlah Edge (12)<br>• N: Jumlah Node (9)<br>• P: Connected Components (1)<br>• Nilai V(G) = 5 merepresentasikan batas atas test cases basis path"
    },
    "hints": {
      "concept": "Rumus Cyclomatic Complexity McCabe: V(G) = E - N + 2P.",
      "execution": "Hitung: 12 - 9 + 2(1) = 3 + 2 = 5."
    },
    "explanation": "Berdasarkan rumus kompleksitas siklomatis McCabe: $V(G) = E - N + 2P$. Dengan $E = 12$, $N = 9$, dan $P = 1$, maka $V(G) = 12 - 9 + 2(1) = 3 + 2 = 5$. Artinya dibutuhkan minimal 5 test case independen untuk menguji seluruh percabangan logika kode program (basis path coverage). Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Stub hanya berjalan di browser, sedangkan Mock hanya dapat dieksekusi di server berbasis NodeJS.                                                       "
      },
      {
        "key": "B",
        "text": "Mock digunakan untuk pengujian performa beban, sedangkan Stub digunakan untuk pengujian keamanan penetrasi.                                            "
      },
      {
        "key": "C",
        "text": "Stub secara otomatis memodifikasi database produksi, sedangkan Mock hanya bekerja pada memori cache guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "D",
        "text": "Stub menyediakan data balasan siap pakai (state verification), sedangkan Mock memverifikasi interaksi pemanggilan method.                              "
      },
      {
        "key": "E",
        "text": "Tidak ada perbedaan teknis sama sekali karena Mock dan Stub adalah sinonim kata yang persis sama.                                                      "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "TEST DOUBLE TAXONOMY (GERARD MESZAROS)",
      "latex": "\\text{Stub (Canned Data)} \\implies \\text{State Verification} \\quad \\text{vs} \\quad \\text{Mock (Expectations)} \\implies \\text{Behavior Verification}",
      "legend": "• Stub: when(api.getData()).thenReturn(sample)<br>• Mock: verify(paymentService, times(1)).charge(amount)"
    },
    "hints": {
      "concept": "Martin Fowler menjelaskan: Stub digunakan untuk State Verification (memberikan jawaban kalengan/canned response). Mock digunakan untuk Behavior Verification (memeriksa apakah method tertentu dipanggil dengan parameter yang benar).",
      "execution": "Stub = verifikasi state data; Mock = verifikasi perilaku/interaksi pemanggilan."
    },
    "explanation": "Menurut taksonomi Gerard Meszaros dan Martin Fowler, `Stub` menyediakan data jawaban siap pakai (canned data) untuk merespons pemanggilan saat pengujian tanpa memverifikasi pemanggilan tersebut (State Verification). Sebaliknya, `Mock` diprogram dengan ekspektasi perilaku dan digunakan untuk memverifikasi apakah method tertentu benar-benar dipanggil dengan parameter yang diharapkan (Behavior Verification). Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Langsung memproses transaksi seketika tombol diklik tanpa menampilkan rincian apapun demi kecepatan alur kerja.                                               "
      },
      {
        "key": "B",
        "text": "Menyembunyikan tombol transfer di dalam menu navigasi tersembunyi agar pengguna tidak dapat menemukannya untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "C",
        "text": "Menampilkan pesan error merah di pojok layar setelah saldo tabungan pengguna terlanjur terpotong sistem.                                                      "
      },
      {
        "key": "D",
        "text": "Menonaktifkan tombol kembali pada browser pengguna sehingga pengguna terpaksa menyelesaikan alur transaksi.                                                   "
      },
      {
        "key": "E",
        "text": "Menampilkan dialog konfirmasi dua langkah yang memuat ringkasan transaksi dan mewajibkan otorisasi PIN/Biometrik.                                             "
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "NIELSEN HEURISTIC #5: ERROR PREVENTION",
      "latex": "\\text{Destructive Action} \\implies \\text{Explicit Review Screen} \\land \\text{Re-authentication (2FA/PIN)}",
      "legend": "• Mencegah slip dan mistake sebelum terjadi<br>• Jauh lebih baik dibanding memberikan pesan error setelah bencana terjadi"
    },
    "hints": {
      "concept": "Heuristik Error Prevention: desain yang baik mencegah terjadinya kesalahan sejak awal, bukan hanya mengobatinya setelah terjadi.",
      "execution": "Layar konfirmasi dan otorisasi PIN memberikan kesempatan bagi pengguna untuk meninjau ulang tindakan berisiko tinggi."
    },
    "explanation": "Heuristik ke-5 Jakob Nielsen (Error Prevention) menekankan bahwa sistem yang luar biasa mencegah masalah terjadi sejak awal. Untuk tindakan berisiko tinggi (keuangan), sistem wajib menyediakan layar konfirmasi yang merinci detail transaksi dan mensyaratkan otentikasi ulang (PIN/biometrik) sebelum eksekusi dijalankan. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Hick's Law yang menyatakan waktu pengambilan keputusan meningkat secara logaritmik seiring bertambahnya opsi pilihan."
      },
      {
        "key": "B",
        "text": "Fitts's Law yang menyatakan waktu menjangkau target berbanding lurus dengan jarak dan ukuran tombol.     "
      },
      {
        "key": "C",
        "text": "Miller's Law yang menyatakan kapasitas memori kerja manusia rata-rata mampu menampung 7 plus minus 2 potongan informasi."
      },
      {
        "key": "D",
        "text": "Jakob's Law yang menyatakan pengguna menghabiskan sebagian besar waktu di situs lain dan menginginkan pola serupa."
      },
      {
        "key": "E",
        "text": "Pareto Principle yang menyatakan 80 persen dampak visual antarmuka dihasilkan oleh 20 persen pilihan palet warna."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "HICK'S LAW MATHEMATICAL MODEL",
      "latex": "RT = b \\cdot \\log_2(n + 1)",
      "legend": "• RT: Reaction Time (Waktu respon)<br>• n: Jumlah pilihan stimulus yang disajikan<br>• Solusi: Progressive disclosure & kategorisasi bertingkat"
    },
    "hints": {
      "concept": "Hick's Law (Hukum Hick-Hyman): semakin banyak pilihan yang diberikan kepada pengguna, semakin lama waktu yang dibutuhkan untuk mengambil keputusan.",
      "execution": "Rumusnya melibatkan logaritma basis 2 dari jumlah opsi: RT = b * log2(n + 1)."
    },
    "explanation": "Hick's Law menyatakan bahwa waktu yang dibutuhkan seseorang untuk membuat keputusan berbanding lurus dengan jumlah dan kompleksitas pilihan yang tersedia ($RT = b \\cdot \\log_2(n + 1)$). Solusi desain terbaik untuk mengatasi beban kognitif ini adalah pengelompokan menu (kategorisasi) dan progressive disclosure. Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Karena lisensi AGPL mewajibkan pembayaran kompensasi royalti finansial bulanan kepada para kontributor pustaka.                                              "
      },
      {
        "key": "B",
        "text": "Karena klausul jaringan AGPL mewajibkan seluruh source code platform SaaS dibuka ke publik jika diakses melalui network.                                     "
      },
      {
        "key": "C",
        "text": "Karena AGPL secara otomatis menghapus hak paten algoritma milik perusahaan yang didaftarkan ke kementerian hukum.                                            "
      },
      {
        "key": "D",
        "text": "Karena pustaka berlisensi AGPL tidak mengizinkan enkripsi data komunikasi pada protokol jaringan HTTPS sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "E",
        "text": "Karena lisensi AGPL hanya dapat dijalankan pada sistem operasi mainframe tua dan tidak mendukung arsitektur Linux.                                           "
      }
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
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Trunk-Based Development menghapus kewajiban pengujian otomatis unit testing sebelum proses rilis production dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "B",
        "text": "Mengizinkan seluruh pengembang mengedit branch produksi secara langsung tanpa melalui proses code review.                                                             "
      },
      {
        "key": "C",
        "text": "Menghindari merge hell dengan mengintegrasikan branch fitur berumur pendek (short-lived) langsung ke trunk setiap hari.                                               "
      },
      {
        "key": "D",
        "text": "Mewajibkan pembuatan minimal sepuluh cabang branch terpisah untuk setiap tiket perbaikan bug kecil.                                                                   "
      },
      {
        "key": "E",
        "text": "Mengharuskan deployment ke server dilakukan secara manual oleh manajer proyek setiap akhir pekan.                                                                     "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "TRUNK-BASED DEVELOPMENT VELOCITY",
      "latex": "\\text{Short-Lived Feature Branches (< 1 day)} \\xrightarrow{\\text{Continuous Integration}} \\text{Trunk (main)}",
      "legend": "• Mencegah akumulasi drift kode antar branch<br>• Didukung oleh Feature Flags untuk menyembunyikan fitur belum tuntas"
    },
    "hints": {
      "concept": "Git Flow tradisional sering memicu 'merge hell' karena feature branch bertahan berpekan-pekan. Trunk-Based Development menggunakan branch kecil yang di-merge ke main/trunk setiap hari.",
      "execution": "Keunggulannya adalah integrasi berkelanjutan yang cepat dan ketiadaan konflik merge besar."
    },
    "explanation": "Trunk-Based Development adalah praktik di mana developer menggabungkan perubahan kecil dan sering (short-lived branches) langsung ke branch utama (`main`/`trunk`) setidaknya sekali sehari. Hal ini menghilangkan masalah 'merge hell' dan konflik integrasi besar yang kerap terjadi pada Git Flow tradisional. Jawaban: C.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Pelanggaran OCP; solusinya adalah menambahkan metode cetakDokumenBerwarna() ke dalam interface tersebut.    "
      },
      {
        "key": "B",
        "text": "Pelanggaran Dependency Inversion Principle; solusinya menggunakan framework Spring IoC container secara paksa."
      },
      {
        "key": "C",
        "text": "Pelanggaran Single Responsibility; solusinya membiarkan method yang tidak didukung melempar UnsupportedOperationException."
      },
      {
        "key": "D",
        "text": "Pelanggaran Interface Segregation Principle (ISP); solusinya memecah interface menjadi Pencetak, Pemindai, dan PengirimFax."
      },
      {
        "key": "E",
        "text": "Pelanggaran Encapsulation; solusinya mengubah seluruh method interface menjadi atribut variabel publik.     "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "SOLID - INTERFACE SEGREGATION PRINCIPLE (ISP)",
      "latex": "\\text{Clients should not be forced to depend upon interfaces that they do not use}",
      "legend": "• Fat interface dipecah menjadi antarmuka peran spesifik (Role Interfaces)<br>• PrinterEkonomis cukup implements Pencetak"
    },
    "hints": {
      "concept": "ISP (prinsip huruf 'I' dalam SOLID): Klien tidak boleh dipaksa bergantung pada method-method yang tidak digunakannya.",
      "execution": "Memecah antarmuka gemuk menjadi beberapa interface kecil yang spesifik (Pencetak, Pemindai, PengirimFax) adalah solusi ISP."
    },
    "explanation": "Interface Segregation Principle (ISP) menyatakan bahwa 'klien tidak boleh dipaksa bergantung pada antarmuka yang tidak digunakannya'. Memaksa `PrinterEkonomis` mengimplementasikan method `scanDokumen()` dan `kirimFax()` melanggar ISP. Solusinya adalah memecah interface monolitik tersebut menjadi antarmuka modular: `Pencetak`, `Pemindai`, dan `PengirimFax`. Jawaban: D.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menghapus kelas GmailSender dan menulis socket jaringan SMTP langsung di dalam kelas NotifikasiService.                                                     "
      },
      {
        "key": "B",
        "text": "Mengubah metode sendEmail menjadi method statis global yang dapat dipanggil langsung dari package mana pun.                                                 "
      },
      {
        "key": "C",
        "text": "Mewariskan kelas NotifikasiService langsung dari kelas konkret GmailSender menggunakan kata kunci extends guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "D",
        "text": "Menyimpan kredensial akun GmailSender secara hardcoded di dalam variabel konstanta kelas NotifikasiService.                                                 "
      },
      {
        "key": "E",
        "text": "Membuat interface PesanSender, mengimplementasikannya pada GmailSender, dan menginjeksi interface ke NotifikasiService.                                     "
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "SOLID - DEPENDENCY INVERSION PRINCIPLE (DIP)",
      "latex": "\\text{High-level & Low-level Modules} \\to \\text{Depend on Abstractions (Interfaces)}",
      "legend": "• NotifikasiService bergantung pada interface PesanSender<br>• GmailSender mengimplementasikan interface PesanSender<br>• Dependency diinjeksi via constructor (Inversion of Control)"
    },
    "hints": {
      "concept": "DIP (huruf 'D' dalam SOLID): Modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah. Keduanya harus bergantung pada abstraksi (interface).",
      "execution": "Gunakan antarmuka perantara PesanSender dan terapkan Dependency Injection."
    },
    "explanation": "Dependency Inversion Principle (DIP) mengharuskan modul tingkat tinggi (`NotifikasiService`) dan modul tingkat rendah (`GmailSender`) bergantung pada abstraksi. Dengan membuat interface `PesanSender` dan menginjeksikannya melalui constructor, `NotifikasiService` menjadi loosely coupled dan dapat dengan mudah dialihkan ke penyedia lain (seperti WhatsAppSender atau SMSSender) tanpa mengubah kodenya. Jawaban: E.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Menerapkan atribut Cookie SameSite=Strict/Lax dan memvalidasi Anti-CSRF Token acak pada setiap request mutasi state.                                       "
      },
      {
        "key": "B",
        "text": "Mengenkripsi seluruh basis data perbankan menggunakan algoritma simetris Advanced Encryption Standard 256-bit.                                             "
      },
      {
        "key": "C",
        "text": "Menghapus penggunaan kata sandi dan menggantinya dengan pertanyaan keamanan nama ibu kandung pengguna untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "D",
        "text": "Mengizinkan seluruh domain luar mengeksekusi request POST melalui konfigurasi header Access-Control-Allow-Origin: *.                                       "
      },
      {
        "key": "E",
        "text": "Mewajibkan pengguna menyegarkan (refresh) halaman browser secara manual setiap kali melakukan transfer dana.                                               "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "CSRF DEFENSE IN DEPTH",
      "latex": "\\text{SameSite=Strict/Lax Cookie} \\land \\text{Cryptographic Anti-CSRF Token} \\implies \\text{Cross-Origin Request Blocked}",
      "legend": "• SameSite=Strict: Cookie tidak dikirim pada navigasi cross-site<br>• Anti-CSRF Token: Nilai rahasia per sesi yang tidak bisa ditebak situs penyerang"
    },
    "hints": {
      "concept": "CSRF memanfaatkan fakta bahwa browser otomatis menyertakan kredensial cookie pada permintaan lintas situs.",
      "execution": "Dua pertahanan utama CSRF: Atribut Cookie SameSite (Strict/Lax) dan Anti-CSRF Token (Synchronizer Token Pattern)."
    },
    "explanation": "CSRF mengeksploitasi mekanisme browser yang otomatis melampirkan cookie sesi saat mengirim request ke domain target. Pertahanan standar OWASP mencakup: (1) Mengatur flag `SameSite=Strict` atau `SameSite=Lax` pada cookie agar tidak ikut terkirim pada request lintas situs, dan (2) Menggunakan Anti-CSRF Synchronizer Token rahasia yang wajib diverifikasi oleh server pada setiap request mutasi data (POST/PUT/DELETE). Jawaban: A.",
    "isDiagnostic": false
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
      {
        "key": "A",
        "text": "Anton ranking 1, Budi ranking 2, dan Citra ranking 3 karena fungsi analitik memecah nilai seri secara sekuensial sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "B",
        "text": "Anton ranking 1, Budi ranking 1, dan Citra ranking 2 karena DENSE_RANK tidak melompati urutan angka setelah nilai seri.                                               "
      },
      {
        "key": "C",
        "text": "Anton ranking 1, Budi ranking 1, dan Citra ranking 3 karena fungsi analitik wajib melompati nomor peringkat.                                                          "
      },
      {
        "key": "D",
        "text": "Anton ranking 1, Budi ranking 2, dan Citra ranking 2 karena peringkat dihitung berdasarkan abjad nama pegawai.                                                        "
      },
      {
        "key": "E",
        "text": "Query memicu runtime error karena fungsi analitik OVER tidak dapat digabungkan dengan klausul PARTITION BY.                                                           "
      }
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-01",
    "subject": "rpl",
    "materi": "PROSES BISNIS & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Analisis Grafik Burndown Chart Scrum",
    "type": "mcq",
    "questionHtml": "Pada hari ke-7 dari Sprint berdurasi 10 hari, grafik Sprint Burndown Chart menunjukkan bahwa garis sisa estimasi pekerjaan (actual effort) berada jauh di atas garis panduan ideal (ideal burn line). Interpretasi manakah yang PALING akurat mengenai status sprint tersebut?",
    "options": [
      {
        "key": "A",
        "text": "Tim bekerja terlalu cepat dan sprint backlog kemungkinan besar akan selesai lebih awal dari jadwal dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "B",
        "text": "Kualitas kode program meningkat drastis sehingga tim tidak perlu lagi melakukan pengujian otomatis QA.                                                        "
      },
      {
        "key": "C",
        "text": "Product Owner otomatis membatalkan sprint seketika dan mengganti seluruh anggota tim pengembang.                                                              "
      },
      {
        "key": "D",
        "text": "Tim mengalami perlambatan progres dan berisiko tinggi gagal menyelesaikan seluruh komitmen sprint backlog.                                                    "
      },
      {
        "key": "E",
        "text": "Estimasi waktu kerja awal terlalu besar sehingga tim memiliki banyak waktu luang tanpa tugas aktif.                                                           "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "SPRINT BURNDOWN CHART METRICS",
      "latex": "\\text{Actual Effort} > \\text{Ideal Line} \\implies \\text{Behind Schedule / Scope at Risk}",
      "legend": "• Actual di atas garis ideal: Pekerjaan tertinggal (behind schedule)<br>• Actual di bawah garis ideal: Pekerjaan lebih cepat (ahead of schedule)"
    },
    "hints": {
      "concept": "Burndown chart mencatat sisa pekerjaan terhadap waktu. Jika garis aktual berada di atas garis ideal, sisa pekerjaan lebih banyak daripada yang seharusnya pada hari tersebut.",
      "execution": "Garis aktual di atas garis ideal berarti tim tertinggal dari jadwal (behind schedule) dan sprint goal terancam."
    },
    "explanation": "Pada Burndown Chart, sumbu Y adalah sisa estimasi jam kerja dan sumbu X adalah hari. Jika garis sisa pekerjaan riil (actual) berada di atas garis ideal, berarti pekerjaan tersisa lebih banyak daripada target waktu yang tersisa (tim tertinggal dari jadwal dan berisiko gagal mencapai Sprint Goal). Jawaban: D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-02",
    "subject": "rpl",
    "materi": "PROSES BISNIS & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Cherry-Pick untuk Hotfix Produksi",
    "type": "mcq",
    "questionHtml": "Sebuah bug kritis ditemukan pada sistem produksi yang berjalan di branch `main`. Perbaikan bug tersebut ternyata sudah pernah dibuat di salah satu commit spesifik pada branch `develop` (commit hash `a1b2c3d`). Perintah Git yang paling tepat digunakan untuk mengambil hanya commit spesifik tersebut dan menerapkannya langsung ke branch `main` tanpa menggabungkan seluruh branch develop adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge develop --squash untuk menggabungkan seluruh commit di develop menjadi satu snapshot besar."
      },
      {
        "key": "B",
        "text": "git rebase develop yang memindahkan seluruh cabang commit develop ke atas branch main produksi."
      },
      {
        "key": "C",
        "text": "git checkout -b hotfix develop untuk membuat branch baru yang menyalin seluruh kode develop mentah."
      },
      {
        "key": "D",
        "text": "git reset --hard a1b2c3d yang menghapus riwayat commit branch main dan menggantinya ke commit tersebut."
      },
      {
        "key": "E",
        "text": "git cherry-pick a1b2c3d saat berada di branch main untuk menyalin commit perbaikan tersebut secara presisi."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "GIT CHERRY-PICK HOTFIX ISOLATION",
      "latex": "\\text{git checkout main} \\implies \\text{git cherry-pick } \\langle \\text{commit-hash} \\rangle",
      "legend": "• Menerapkan patch spesifik dari branch lain tanpa merge seluruh branch<br>• Menghindari masuknya fitur unreleased yang belum siap rilis"
    },
    "hints": {
      "concept": "git cherry-pick memungkinkan programmer memilih commit tertentu dari satu branch dan menerapkannya ke branch lain yang aktif.",
      "execution": "Cherry-pick adalah perintah standar untuk porting commit perbaikan bug (hotfix) secara terisolasi."
    },
    "explanation": "`git cherry-pick <commit-hash>` memungkinkan pengembang memilih commit tertentu dari suatu cabang dan menerapkannya langsung pada cabang kerja saat ini (`main`) tanpa harus menelan seluruh commit fitur lain yang belum siap di `develop`. Jawaban: E.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-sim-03",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pola Perancangan Kelas Abadi (Immutable Class)",
    "type": "mcq",
    "questionHtml": "Dalam perancangan sistem keuangan berbasis Java, kelas `Uang` dirancang agar bersifat *Immutable* (state objek tidak dapat diubah setelah diinstansiasi). Karakteristik rancangan kelas yang WAJIB dipenuhi untuk mencapai sifat immutability sempurna adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menjadikan kelas bertipe final, semua atribut private final, tanpa setter, dan defensive copy pada objek mutable.                               "
      },
      {
        "key": "B",
        "text": "Menyediakan method setter publik untuk setiap atribut agar nilai dapat diperbarui secara fleksibel.                                             "
      },
      {
        "key": "C",
        "text": "Mewajibkan kelas mewarisi kelas Thread agar setiap operasi perbankan berjalan di background terpisah.                                           "
      },
      {
        "key": "D",
        "text": "Mendeklarasikan seluruh atribut sebagai variabel statis publik agar memori dapat dipakai bersama oleh klien.                                    "
      },
      {
        "key": "E",
        "text": "Menyediakan method resetState() yang mengosongkan seluruh saldo rekening menjadi nol rupiah guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "JAVA IMMUTABILITY CONTRACT",
      "latex": "\\text{final class} \\land \\text{private final fields} \\land \\neg(\\text{setters}) \\land \\text{Defensive Copying}",
      "legend": "• Thread-safe secara inheren (tidak butuh synchronization)<br>• State tidak dapat dimutasi setelah konstruktor selesai dieksekusi"
    },
    "hints": {
      "concept": "Aturan Immutable Class di Java: 1. Deklarasikan class sebagai final; 2. Semua field private dan final; 3. Tidak ada setter; 4. Lakukan defensive copying untuk objek referensi mutable.",
      "execution": "Pilihan B merangkum seluruh syarat mutlak kelas immutable."
    },
    "explanation": "Untuk membuat Immutable Class di Java (seperti kelas `String`), pengembang wajib: (1) mendeklarasikan kelas sebagai `final` agar tidak bisa di-override, (2) membuat semua field `private final`, (3) tidak menyediakan method setter/mutator, dan (4) melakukan defensive copy saat menerima atau mengembalikan objek mutable. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-04",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Penanganan Custom Domain Exception",
    "type": "mcq",
    "questionHtml": "Perhatikan perancangan eksepsi kustom perbankan berikut:\n```java\npublic class SaldoTidakCukupException extends Exception {\n    public SaldoTidakCukupException(String pesan) {\n        super(pesan);\n    }\n}\n```\nKarena kelas di atas mewarisi langsung kelas `Exception` (bukan `RuntimeException`), maka `SaldoTidakCukupException` tergolong sebagai...",
    "options": [
      {
        "key": "A",
        "text": "Unchecked exception yang tidak perlu ditangkap atau dideklarasikan pada klausa throws oleh compiler untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "B",
        "text": "Checked exception yang wajib ditangani dengan try-catch atau dideklarasikan pada method signature dengan throws.                                          "
      },
      {
        "key": "C",
        "text": "Fatal JVM Error yang otomatis menghentikan proses eksekusi sistem operasi secara seketika.                                                                "
      },
      {
        "key": "D",
        "text": "Memory Exception yang hanya dilempar jika kapasitas RAM server database telah habis terpakai.                                                             "
      },
      {
        "key": "E",
        "text": "Syntax Exception yang hanya muncul saat kode program sedang diperiksa oleh IDE pengembang.                                                                "
      }
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-05",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Subquery Berkorelasi (Correlated Subquery) dengan EXISTS",
    "type": "mcq",
    "questionHtml": "Perhatikan query SQL optimasi analitik berikut:\n```sql\nSELECT p.id, p.nama\nFROM pelanggan p\nWHERE NOT EXISTS (\n    SELECT 1\n    FROM transaksi t\n    WHERE t.id_pelanggan = p.id\n);\n```\nTujuan bisnis yang dicapai oleh eksekusi query di atas adalah...",
    "options": [
      {
        "key": "A",
        "text": "Menghapus seluruh rekaman data pelanggan yang memiliki riwayat transaksi lebih dari sepuluh kali.                                                       "
      },
      {
        "key": "B",
        "text": "Menghitung rata-rata nominal transaksi yang dilakukan oleh pelanggan tetap yang aktif berbelanja sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "C",
        "text": "Menampilkan daftar seluruh pelanggan yang belum pernah melakukan transaksi pembelian sama sekali.                                                       "
      },
      {
        "key": "D",
        "text": "Memperbarui status keanggotaan pelanggan menjadi VIP jika nominal saldo belanja melampaui limit.                                                        "
      },
      {
        "key": "E",
        "text": "Menampilkan pelanggan yang transaksinya mengalami kegagalan sistem pembayaran di gateway bank.                                                          "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "CORRELATED NOT EXISTS LOGIC",
      "latex": "p \\in \\text{Result} \\iff \\{ t \\in \\text{Transaksi} \\mid t.\\text{id\\_pelanggan} = p.\\text{id} \\} = \\emptyset",
      "legend": "• Correlated Subquery dievaluasi per baris pelanggan p<br>• NOT EXISTS mengembalikan True jika subquery tidak menghasilkan satu baris pun"
    },
    "hints": {
      "concept": "Klausul WHERE NOT EXISTS mengevaluasi apakah subquery menghasilkan baris. Jika tidak ada transaksi yang cocok untuk pelanggan tersebut, kondisi bernilai True.",
      "execution": "Query ini mencari pelanggan yang himpunan transaksinya kosong (tidak pernah belanja)."
    },
    "explanation": "Klausul `WHERE NOT EXISTS` mengevaluasi ketiadaan rekaman pada subquery berkorelasi. Query ini memeriksa setiap pelanggan `p`, dan jika subquery tidak menemukan rekaman transaksi yang cocok dengan `id_pelanggan = p.id`, maka pelanggan tersebut dipilih. Hasilnya adalah daftar pelanggan yang belum pernah bertransaksi. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-06",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Tingkat Isolasi Transaksi Basis Data (Isolation Levels)",
    "type": "mcq",
    "questionHtml": "Dalam standar ANSI SQL transaksi database, tingkat isolasi (isolation level) manakah yang memberikan perlindungan paling ketat dengan mencegah fenomena Dirty Read, Non-Repeatable Read, maupun Phantom Read secara total?",
    "options": [
      {
        "key": "A",
        "text": "Read Uncommitted yang mengizinkan transaksi membaca perubahan data yang belum di-commit sama sekali.                                                          "
      },
      {
        "key": "B",
        "text": "Read Committed yang hanya mencegah fenomena pembacaan data kotor (dirty read) pada transaksi aktif dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "C",
        "text": "Repeatable Read yang mengunci baris data yang dibaca tetapi masih memungkinkan terjadinya phantom read.                                                       "
      },
      {
        "key": "D",
        "text": "Serializable yang mengeksekusi transaksi secara berurutan seolah-olah sistem berjalan pada single thread.                                                     "
      },
      {
        "key": "E",
        "text": "Snapshot Isolation yang hanya bekerja pada media penyimpanan basis data terdistribusi noSQL.                                                                  "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "TRANSACTION ISOLATION LEVELS HIERARCHY",
      "latex": "\\text{Read Uncommitted} < \\text{Read Committed} < \\text{Repeatable Read} < \\text{Serializable}",
      "legend": "• Serializable: Mencegah Dirty Read, Non-Repeatable Read, dan Phantom Read<br>• Mengorbankan konkurensi performa demi konsistensi data mutlak"
    },
    "hints": {
      "concept": "Tingkat isolasi ANSI SQL terketat adalah Serializable. Pada level ini, transaksi dieksekusi sedemikian rupa sehingga hasilnya identik dengan eksekusi serial murni.",
      "execution": "Tingkat isolasi terketat adalah Serializable."
    },
    "explanation": "`Serializable` adalah tingkat isolasi tertinggi dalam standar ANSI SQL. Tingkat ini menjamin isolasi penuh dari fenomena anomali konkurensi (Dirty Read, Non-Repeatable Read, dan Phantom Read) dengan mengunci rentang data atau menggunakan multi-version concurrency control (MVCC) serial, meskipun trade-off-nya menurunkan throughput konkurensi. Jawaban: D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-07",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Konsep Indeks Penutup (Covering Index)",
    "type": "mcq",
    "questionHtml": "Diberikan tabel `karyawan(id, nik, nama, divisi, gaji)`. Database administrator membuat indeks B-Tree pada kolom `(divisi, gaji)`. Perhatikan query berikut:\n```sql\nSELECT divisi, SUM(gaji)\nFROM karyawan\nGROUP BY divisi;\n```\nQuery di atas dapat dieksekusi dengan kecepatan sangat tinggi tanpa menyentuh tabel data utama pada disk (Heap/Clustered Index Table). Fenomena optimasi ini terjadi karena indeks tersebut bertindak sebagai...",
    "options": [
      {
        "key": "A",
        "text": "Foreign Key Index yang mereferensikan integritas relasional tabel master departemen luar.          "
      },
      {
        "key": "B",
        "text": "Full-Text Search Index yang memindai token teks menggunakan kamus leksikal bahasa Indonesia.       "
      },
      {
        "key": "C",
        "text": "Spatial Index yang mengelompokkan data lokasi koordinat geospasial menggunakan struktur R-Tree.    "
      },
      {
        "key": "D",
        "text": "Hash Index yang hanya mendukung perbandingan nilai persamaan absolut tanpa fungsi agregasi.        "
      },
      {
        "key": "E",
        "text": "Covering Index (Index-Only Scan) di mana seluruh kolom yang dibutuhkan query sudah tersedia di dalam daun indeks."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "COVERING INDEX / INDEX-ONLY SCAN",
      "latex": "\\text{Required Columns } \\{ \\text{divisi, gaji} \\} \\subseteq \\text{Index Columns } \\{ \\text{divisi, gaji} \\} \\implies \\text{No Table Lookup}",
      "legend": "• Menghindari I/O baca ke tabel utama (Heap table/Clustered index leaf)<br>• Peningkatan performa query hingga 10x - 100x lipat"
    },
    "hints": {
      "concept": "Jika semua kolom yang diminta dalam SELECT, WHERE, dan GROUP BY sudah ada di dalam indeks itu sendiri, database tidak perlu membaca tabel utama. Ini dinamakan Covering Index.",
      "execution": "Query hanya butuh 'divisi' dan 'gaji', dan indeks mencakup persis kedua kolom tersebut."
    },
    "explanation": "Sebuah indeks dikatakan sebagai *Covering Index* untuk suatu query jika indeks tersebut memuat semua kolom yang diminta oleh query (baik di klausa SELECT, WHERE, maupun GROUP BY). Database engine dapat langsung mengambil data dari node daun E-Tree indeks tanpa perlu melakukan lookup sekunder ke tabel utama di disk (Index-Only Scan). Jawaban: E.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-08",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & API",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Arsitektur REST vs GraphQL",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi mobile ingin menampilkan nama pengguna dan foto profil saja pada header layar. Jika menggunakan endpoint REST API `/api/users/1`, server mengembalikan seluruh data lengkap pengguna berupa 50 field profil. Masalah inefisiensi transmisi data jaringan ini dikenal sebagai...",
    "options": [
      {
        "key": "A",
        "text": "Over-fetching di mana client menerima muatan data yang jauh lebih banyak daripada data yang sebenarnya dibutuhkan.                                             "
      },
      {
        "key": "B",
        "text": "Under-fetching di mana client tidak memperoleh cukup data sehingga harus melakukan pemanggilan berulang kali guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "C",
        "text": "Denial of Service di mana server API kewalahan menerima request dalam volume tinggi secara simultan.                                                           "
      },
      {
        "key": "D",
        "text": "Cache Invalidation di mana browser client gagal memperbarui file statis JavaScript yang kedaluwarsa.                                                           "
      },
      {
        "key": "E",
        "text": "Packet Dropping di mana paket data TCP terputus akibat interferensi gelombang frekuensi radio.                                                                 "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "API PAYLOAD BOTTLENECKS",
      "latex": "\\text{Over-fetching} \\colon \\text{Payload Size} \\gg \\text{Needed Data} \\quad \\text{vs} \\quad \\text{Under-fetching} \\colon \\text{Calls} > 1",
      "legend": "• Over-fetching: Buang kuota & lambat di mobile<br>• GraphQL memecahkan masalah ini dengan deklarasi field spesifik"
    },
    "hints": {
      "concept": "Over-fetching terjadi saat endpoint mengembalikan payload data yang berlebihan dibandingkan kebutuhan UI aplikasi.",
      "execution": "Under-fetching adalah kebalikannya (data kurang sehingga harus request berkali-kali)."
    },
    "explanation": "*Over-fetching* adalah kondisi di mana klien menerima lebih banyak data daripada yang diperlukan untuk merender antarmuka pengguna (misal menerima 50 kolom padahal hanya butuh 2 kolom). Salah satu motivasi kelahiran GraphQL adalah menyelesaikan masalah over-fetching dan under-fetching pada REST API tradisional. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-09",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & API",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Konfigurasi Header Content Security Policy (CSP)",
    "type": "mcq",
    "questionHtml": "Untuk melindungi aplikasi web dari eksekusi skrip berbahaya pada serangan Cross-Site Scripting (XSS), administrator mengonfigurasi HTTP response header Content Security Policy (CSP) berikut:\n```http\nContent-Security-Policy: default-src 'self'; script-src 'self' https://trustedscripts.com;\n```\nAturan kebijakan keamanan yang diberlakukan oleh header di atas adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengizinkan seluruh website di internet mengunduh file gambar dan stylesheet dari server aplikasi secara bebas.                                                 "
      },
      {
        "key": "B",
        "text": "Hanya mengizinkan eksekusi skrip JavaScript yang berasal dari origin yang sama ('self') dan domain trustedscripts.com.                                          "
      },
      {
        "key": "C",
        "text": "Mengharuskan pengguna memasukkan password token otentikasi dua faktor setiap kali membuka halaman web baru untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "D",
        "text": "Memblokir seluruh koneksi database backend jika port server diakses melalui jaringan lokal tanpa VPN.                                                           "
      },
      {
        "key": "E",
        "text": "Mengonversi seluruh kode JavaScript frontend menjadi format WebAssembly biner secara otomatis di browser.                                                       "
      }
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-10",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & API",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Penanganan Paralel Promise.all vs Promise.allSettled",
    "type": "mcq",
    "questionHtml": "Sebuah modul dasbor keuangan memanggil tiga layanan API analitik secara bersamaan: `fetchOmset()`, `fetchStok()`, dan `fetchPajak()`. Pengembang ingin dasbor tetap dapat merender data layanan yang berhasil meskipun salah satu dari ketiga API tersebut mengalami kegagalan (network failure). Metode penanganan Promise JavaScript yang PALING tepat digunakan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Promise.all() karena otomatis mengabaikan kegagalan dan langsung mengembalikan hasil array yang sukses saja.                                                     "
      },
      {
        "key": "B",
        "text": "Promise.race() karena hanya mengambil satu hasil respons API yang pertama kali tiba paling cepat di browser sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "C",
        "text": "Promise.allSettled() karena menunggu semua promise tuntas dan mengembalikan array status baik fulfilled maupun rejected.                                         "
      },
      {
        "key": "D",
        "text": "Promise.any() karena akan memicu crash aplikasi jika ada salah satu permintaan data yang mengalami penolakan.                                                    "
      },
      {
        "key": "E",
        "text": "Eksekusi pemanggilan ketiga fungsi secara berurutan sinkron menggunakan loop while tanpa fungsi promise.                                                         "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "JS PROMISE CONCURRENCY METHODS",
      "latex": "\\text{Promise.all (Fail-Fast)} \\quad \\text{vs} \\quad \\text{Promise.allSettled (Resilient Aggregate)}",
      "legend": "• Promise.all: Jika 1 reject, seluruh batch langsung REJECT<br>• Promise.allSettled: Menunggu semua promise selesai (status: fulfilled/rejected)"
    },
    "hints": {
      "concept": "Promise.all akan langsung reject (fail-fast) jika salah satu promise gagal. Untuk skenario di mana UI tetap ingin menampilkan hasil dari promise yang berhasil, gunakan Promise.allSettled.",
      "execution": "Promise.allSettled mengembalikan status per promise sehingga error pada satu API tidak menggagalkan API lainnya."
    },
    "explanation": "`Promise.all()` bersifat fail-fast (jika satu promise reject, seluruh operasi langsung gagal). Sebaliknya, `Promise.allSettled()` menunggu semua promise selesai dieksekusi dan mengembalikan array objek yang mencantumkan status masing-masing (`status: 'fulfilled'` atau `status: 'rejected'`), memungkinkan aplikasi tetap menampilkan data dari layanan yang berhasil. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-11",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & API",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Konsep Closure dalam JavaScript",
    "type": "mcq",
    "questionHtml": "Perhatikan fungsi JavaScript pembuat counter berikut:\n```javascript\nfunction createCounter() {\n    let count = 0;\n    return function() {\n        count++;\n        return count;\n    };\n}\nconst c1 = createCounter();\nconsole.log(c1());\nconsole.log(c1());\n```\nNilai yang dicetak pada console log dan konsep fundamental JavaScript yang memungkinkan variabel `count` tetap tersimpan di memori setelah `createCounter()` selesai dieksekusi adalah...",
    "options": [
      {
        "key": "A",
        "text": "1 dan 1; konsep Scope Hoisting variabel lokal dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "B",
        "text": "undefined dan undefined; konsep Garbage Collection otomatis membebaskan memori.                                 "
      },
      {
        "key": "C",
        "text": "0 dan 1; konsep Prototipe Objek Pewarisan JavaScript.                                                           "
      },
      {
        "key": "D",
        "text": "1 dan 2; konsep Closure yang mempertahankan referensi leksikal variabel terluar.                                "
      },
      {
        "key": "E",
        "text": "Error ReferenceError karena variabel count berada di luar batas fungsi.                                         "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "JAVASCRIPT CLOSURE DEFINITION",
      "latex": "\\text{Closure} = \\text{Inner Function} + \\text{Lexical Environment Reference (Retained)}",
      "legend": "• Fungsi dalam mempertahankan akses ke variabel di scope induknya bahkan setelah fungsi induk selesai dieksekusi"
    },
    "hints": {
      "concept": "Closure adalah kombinasi antara sebuah fungsi dan lingkungan leksikal (lexical environment) tempat fungsi tersebut dideklarasikan.",
      "execution": "Variabel count ditahan di memori oleh fungsi dalam, sehingga pemanggilan berulang c1() menambah nilai count: 1 lalu 2."
    },
    "explanation": "Sebuah *Closure* tercipta ketika sebuah fungsi dalam mempertahankan referensi ke variabel-variabel di scope fungsi luarnya, bahkan setelah fungsi luar tersebut selesai dieksekusi. Oleh karena itu, variabel `count` tidak disapu Garbage Collector dan nilainya dipertahankan antar pemanggilan, menghasilkan output 1 lalu 2. Jawaban: D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-12",
    "subject": "rpl",
    "materi": "PEMROGRAMAN APLIKASI BERGERAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Manajemen Tugas Latar Belakang (WorkManager)",
    "type": "mcq",
    "questionHtml": "Aplikasi e-commerce Android perlu mengunggah log analitik transaksi harian ke server cloud secara andal, di mana tugas tersebut wajib tetap berjalan tuntas meskipun aplikasi ditutup oleh pengguna atau perangkat smartphone di-restart. Komponen arsitektur Android Jetpack manakah yang PALING direkomendasikan Google untuk kebutuhan tersebut?",
    "options": [
      {
        "key": "A",
        "text": "AsyncTask yang memproses kalkulasi asynchronous ringan pada thread terpisah di memori RAM."
      },
      {
        "key": "B",
        "text": "BroadcastReceiver biasa yang mendengarkan event perubahan jaringan tanpa penjadwalan.   "
      },
      {
        "key": "C",
        "text": "Thread murni Java (new Thread) yang dibuat langsung di dalam blok method onDestroy().   "
      },
      {
        "key": "D",
        "text": "Handler postDelayed() yang menunda eksekusi instruksi selama beberapa menit di antrean pesan UI."
      },
      {
        "key": "E",
        "text": "WorkManager yang menjamin eksekusi tugas tertunda (deferrable & guaranteed) sesuai konstrain baterai."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "ANDROID BACKGROUND WORK SELECTION",
      "latex": "\\text{Deferrable} \\land \\text{Guaranteed Execution} \\implies \\text{WorkManager (Persisted in SQLite)}",
      "legend": "• Menghormati Doze Mode & penghemat baterai<br>• Menjadwalkan tugas dengan batasan (misal: hanya saat charging & terhubung Wi-Fi)"
    },
    "hints": {
      "concept": "WorkManager adalah standar Android Jetpack untuk pekerjaan latar belakang yang dapat ditunda (deferrable) tetapi wajib terjamin dieksekusi (guaranteed execution) meskipun aplikasi ditutup.",
      "execution": "AsyncTask sudah deprecated. WorkManager mengelola persistensi tugas di database internal sistem operasi."
    },
    "explanation": "`WorkManager` adalah API Android Jetpack yang dirancang khusus untuk menangani pekerjaan latar belakang yang bersifat *deferrable* (bisa ditunda) dan *guaranteed* (pasti dieksekusi). Tugas yang dijadwalkan dengan WorkManager tetap bertahan dan akan dieksekusi bahkan jika aplikasi ditutup paksa atau perangkat ponsel di-restart. Jawaban: E.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-13",
    "subject": "rpl",
    "materi": "REKAYASA PEMROGRAMAN GIM",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pola Arsitektur Entity-Component-System (ECS)",
    "type": "mcq",
    "questionHtml": "Dalam pengembangan gim skala besar dengan puluhan ribu objek bergerak simultan, pola arsitektur Entity-Component-System (ECS) lebih dipilih daripada pendekatan Pemrograman Berorientasi Objek (OOP) hierarki pewarisan kelas yang dalam karena...",
    "options": [
      {
        "key": "A",
        "text": "ECS memisahkan data (Component) dari logika (System), mengoptimalkan CPU Cache locality (Data-Oriented Design).                                         "
      },
      {
        "key": "B",
        "text": "ECS mengharuskan seluruh aset grafis 3D dikonversi menjadi format file vektor monokrom dua dimensi.                                                     "
      },
      {
        "key": "C",
        "text": "OOP tradisional tidak dapat mengompilasi kode program jika jumlah kelas game melampaui seratus file.                                                    "
      },
      {
        "key": "D",
        "text": "ECS menghapus ketergantungan pada kartu grafis GPU sehingga seluruh proses render ditangani oleh RAM guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "E",
        "text": "ECS secara otomatis membuat animasi gerakan karakter menjadi halus tanpa memerlukan asset rigger seniman.                                               "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DATA-ORIENTED DESIGN (ECS)",
      "latex": "\\text{Entity (ID)} + \\text{Component (Raw Data)} + \\text{System (Logic)} \\implies \\text{Contiguous Memory Cache Hit}",
      "legend": "• OOP: Object tersebar di heap -> Cache Miss tinggi<br>• ECS: Komponen disusun dalam array kontigu -> Cache Line termanfaatkan maksimal"
    },
    "hints": {
      "concept": "ECS (Entity Component System) menganut filosofi Data-Oriented Design. Memisahkan data murni dari logika pemrosesan memungkinkan data disimpan secara kontigu di memori, meminimalkan cache miss CPU.",
      "execution": "Keunggulan utama ECS adalah efisiensi pemrosesan massal ribuan entitas secara paralel berkat data locality."
    },
    "explanation": "Pendekatan OOP tradisional menghasilkan objek yang tersebar acak di memori heap dengan banyak pointer indirection, menyebabkan CPU Cache Miss yang tinggi. Pola ECS (Data-Oriented Design) memisahkan data murni (`Component`) ke dalam larik memori kontigu dan memprosesnya secara massal melalui `System`, memaksimalkan performa CPU Cache dan throughput eksekusi gim. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-14",
    "subject": "rpl",
    "materi": "REKAYASA PEMROGRAMAN GIM",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Optimasi Grafis: Frustum & Occlusion Culling",
    "type": "mcq",
    "questionHtml": "Dalam optimasi pipeline rendering dunia gim 3D, teknik yang bertugas membuang (tidak memproses render) objek-objek yang berada di luar kerucut jangkauan pandang kamera disebut `Frustum Culling`. Sementara teknik yang membuang objek yang berada di dalam pandangan kamera tetapi terhalang sepenuhnya oleh objek besar lain di depannya disebut...",
    "options": [
      {
        "key": "A",
        "text": "Backface Culling yang membuang poligon segitiga yang menghadap membelakangi arah kamera.                                                           "
      },
      {
        "key": "B",
        "text": "Occlusion Culling yang menonaktifkan rendering objek yang tertutup oleh geometri penghalang di depannya.                                           "
      },
      {
        "key": "C",
        "text": "Distance Fogging yang menutupi kejauhan dunia gim menggunakan lapisan kabut buatan atmosfer untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "D",
        "text": "Level of Detail (LOD) yang menurunkan jumlah poligon mesh objek yang posisinya sangat jauh dari pemain.                                            "
      },
      {
        "key": "E",
        "text": "Anti-Aliasing yang menghaluskan garis tepi bergerigi pada sudut poligon objek grafis tiga dimensi.                                                 "
      }
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-15",
    "subject": "rpl",
    "materi": "DESAIN UI/UX & AKSESIBILITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Aksesibilitas Web Semantik (Screen Reader)",
    "type": "mcq",
    "questionHtml": "Seorang frontend engineer membangun tombol interaktif menggunakan markup `<div class=\"btn\" onclick=\"beli()\">Beli Sekarang</div>` alih-alih menggunakan tag HTML standar `<button onclick=\"beli()\">Beli Sekarang</button>`. Masalah aksesibilitas fatal yang dialami oleh pengguna penyandang disabilitas tunanetra saat menggunakan pembaca layar (screen reader) adalah...",
    "options": [
      {
        "key": "A",
        "text": "Warna tombol di layar otomatis berubah menjadi transparan sehingga tidak dapat terlihat oleh pengguna.                                                  "
      },
      {
        "key": "B",
        "text": "Browser langsung memblokir eksekusi fungsi JavaScript beli() karena dianggap sebagai malware trojan.                                                    "
      },
      {
        "key": "C",
        "text": "Screen reader tidak mengenali elemen tersebut sebagai tombol interaktif dan tidak dapat difokuskan via tombol Tab keyboard.                             "
      },
      {
        "key": "D",
        "text": "Kecepatan loading halaman web menurun drastis sebesar 90 persen akibat kegagalan parsing mesin rendering.                                               "
      },
      {
        "key": "E",
        "text": "Sertifikat keamanan HTTPS pada domain web otomatis dicabut oleh otoritas penerbit sertifikat SSL sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "SEMANTIC HTML ACCESSIBILITY TREE",
      "latex": "\\text{<button>} \\implies \\{ \\text{Role: button}, \\; \\text{Keyboard Focusable (Tab)}, \\; \\text{Accessible Name} \\}",
      "legend": "• <div> tidak memiliki semantic role button<br>• Tidak bisa menerima fokus keyboard secara default (tabindex=-1)<br>• Menyalahi WCAG 2.1 Principle: Robust & Operable"
    },
    "hints": {
      "concept": "Elemen div adalah elemen generik non-semantik. Tanpa tag <button>, elemen tidak memiliki role 'button' di Accessibility Tree dan tidak bisa difokuskan menggunakan tombol Tab pada keyboard.",
      "execution": "Pengguna tunanetra dan pengguna keyboard murni tidak akan tahu bahwa div tersebut adalah tombol interaktif."
    },
    "explanation": "Elemen semantik `<button>` secara bawaan menyediakan role button pada Accessibility Tree, dapat difokuskan melalui keyboard (tombol Tab), serta dapat diaktifkan menggunakan tombol Spasi dan Enter. Menggantinya dengan `<div>` membuat screen reader tidak mengumumkan elemen tersebut sebagai tombol dan membuatnya tidak dapat diakses tanpa mouse, melanggar standar WCAG. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-16",
    "subject": "rpl",
    "materi": "PENGUJIAN PERANGKAT LUNAK (QA)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pengujian Mutasi (Mutation Testing)",
    "type": "mcq",
    "questionHtml": "Sebuah tim QA memiliki unit test suite dengan indikator code coverage mencapai 100%. Namun, mereka tetap menerapkan *Mutation Testing* dengan menyuntikkan perubahan kecil (mutants, misalnya mengubah operator `>` menjadi `<`). Tujuan utama dari pelaksanaan Mutation Testing tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Meningkatkan kecepatan eksekusi proses pengujian unit test menjadi dua kali lebih cepat di server CI/CD dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "B",
        "text": "Mengenkripsi seluruh basis kode sumber agar tidak dapat didekompilasi oleh pihak luar yang tidak berhak.                                                          "
      },
      {
        "key": "C",
        "text": "Memperbaiki bug logika secara otomatis tanpa campur tangan dari insinyur perangkat lunak manusia.                                                                 "
      },
      {
        "key": "D",
        "text": "Menguji efektivitas dan kualitas test suite itu sendiri dengan memverifikasi apakah unit test mampu mendeteksi bug buatan.                                        "
      },
      {
        "key": "E",
        "text": "Mengurangi ukuran file biner aplikasi agar dapat diunduh lebih cepat oleh pengguna akhir ponsel.                                                                  "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "MUTATION SCORE EQUATION",
      "latex": "\\text{Mutation Score} = \\frac{\\text{Killed Mutants}}{\\text{Total Mutants}} \\times 100\\%",
      "legend": "• Code coverage 100% belum tentu menguji logika dengan benar (bisa saja tanpa assertion)<br>• Mutant killed = Test suite berkualitas tinggi karena berhasil menangkap perubahan cacat"
    },
    "hints": {
      "concept": "Coverage 100% hanya mengukur baris kode mana yang dieksekusi, bukan apakah tes tersebut benar-benar memvalidasi output. Mutation testing menguji kualitas tes dengan menyuntikkan mutasi kode.",
      "execution": "Jika tes gagal saat kode dimutasi (mutant killed), berarti tes tersebut berkualitas baik."
    },
    "explanation": "Code coverage tinggi tidak menjamin kualitas pengujian karena kode bisa saja dieksekusi tanpa adanya `assert` yang memadai. *Mutation Testing* mengevaluasi kualitas unit test itu sendiri dengan memperkenalkan kesalahan sintaksis sengaja (mutants); jika test suite gagal mendeteksi perubahan tersebut (mutant survived), berarti pengujian yang dibuat masih lemah dan perlu diperbaiki. Jawaban: D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-17",
    "subject": "rpl",
    "materi": "PROSES BISNIS & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Pre-Commit Hook untuk Keamanan",
    "type": "mcq",
    "questionHtml": "Untuk mencegah insiden kebocoran kredensial sensitif (seperti API Keys, Private Keys, dan password database) agar tidak sengaja terunggah ke repositori GitHub publik, langkah rekayasa preventif otomatis yang wajib dikonfigurasi di sisi lokal pengembang adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mewajibkan pengembang menulis password akun email perusahaan langsung pada komentar source code program.           "
      },
      {
        "key": "B",
        "text": "Menonaktifkan sistem enkripsi SSL pada repositori remote agar paket commit dapat dipantau oleh admin jaringan.     "
      },
      {
        "key": "C",
        "text": "Menghapus file .gitignore dari proyek agar seluruh file konfigurasi rahasia dapat terlacak oleh sistem Git.        "
      },
      {
        "key": "D",
        "text": "Mengunggah file konfigurasi database .env secara berkala ke media penyimpanan Google Drive publik.                 "
      },
      {
        "key": "E",
        "text": "Memasang script Git Pre-Commit Hook (misalnya via tool Gitleaks/TruffleHog) yang otomatis membatalkan commit jika mendeteksi secret."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "GIT HOOKS SECURITY SHIFT-LEFT",
      "latex": "\\text{git commit} \\implies \\text{.git/hooks/pre-commit scans staged files} \\xrightarrow{\\text{Secret Detected}} \\text{Exit Code 1 (Abort)}",
      "legend": "• Shift-Left Security: Mencegah kerentanan di workstation developer sebelum mencapai remote repo"
    },
    "hints": {
      "concept": "Pre-commit hook adalah skrip yang dieksekusi Git sebelum commit disimpan. Jika skrip menghasilkan exit code non-zero, proses commit dibatalkan.",
      "execution": "Scanner otomatis seperti Gitleaks di pre-commit hook mencegah secret masuk ke riwayat commit."
    },
    "explanation": "Pemasangan `pre-commit hook` pada Git memungkinkan pemindaian otomatis terhadap file yang ada di staging area tepat sebelum proses commit selesai. Jika alat pemindai (seperti Gitleaks atau TruffleHog) mendeteksi pola API Key atau kredensial rahasia, proses commit langsung dibatalkan otomatis di workstation pengembang (Shift-Left Security). Jawaban: E.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-18",
    "subject": "rpl",
    "materi": "K3LH & HAKI PERANGKAT LUNAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hak Cipta vs Paten Perangkat Lunak",
    "type": "mcq",
    "questionHtml": "Berdasarkan sistem hukum Hak Atas Kekayaan Intelektual (HAKI) di Indonesia (UU Hak Cipta No. 28 Tahun 2014), bentuk perlindungan hukum mendasar yang diberikan kepada karya Program Komputer (Perangkat Lunak) adalah...",
    "options": [
      {
        "key": "A",
        "text": "Hak Cipta yang melindungi ekspresi wujud kode sumber (source code) dan program komputer dari penjiplakan tanpa izin.                                      "
      },
      {
        "key": "B",
        "text": "Hak Desain Industri yang melindungi fungsi matematis rangkaian sirkuit elektronik motherboard komputer guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      },
      {
        "key": "C",
        "text": "Hak Merek Dagang yang melarang pengembang lain menulis program dengan bahasa pemrograman yang sama.                                                       "
      },
      {
        "key": "D",
        "text": "Rahasia Dagang yang otomatis gugur jika aplikasi dirilis ke publik melalui toko aplikasi resmi Google Play.                                               "
      },
      {
        "key": "E",
        "text": "Perlindungan Varietas Tanaman yang mengatur silsilah penamaan variabel di dalam modul kecerdasan buatan.                                                  "
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "HAKI FRAMEWORK INDONESIA (UU 28/2014)",
      "latex": "\\text{Program Komputer} \\subseteq \\text{Ciptaan yang Dilindungi Hak Cipta (Pasal 40 Ayat 1 Huruf s)}",
      "legend": "• Perlindungan berlaku otomatis (prinsip deklaratif) sejak ciptaan diwujudkan dalam bentuk nyata<br>• Melindungi ekspresi ide (source code/binary), bukan ide dasarnya"
    },
    "hints": {
      "concept": "Di Indonesia, program komputer (software) dilindungi di bawah rezim Hak Cipta (UU No. 28 Tahun 2014 Pasal 40), yang melindungi ekspresi source code dari penyalinan.",
      "execution": "Program komputer dikategorikan sebagai ciptaan yang dilindungi oleh Hak Cipta."
    },
    "explanation": "Berdasarkan Pasal 40 Ayat (1) huruf s UU No. 28 Tahun 2014 tentang Hak Cipta, Program Komputer secara eksplisit diakui sebagai salah satu ciptaan yang dilindungi oleh rezim Hak Cipta. Hak cipta melindungi wujud nyata ekspresi kode sumber program dari penggandaan, pembajakan, dan distribusi tanpa izin. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-19",
    "subject": "rpl",
    "materi": "K3LH & HAKI PERANGKAT LUNAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pencegahan Carpal Tunnel Syndrome (CTS)",
    "type": "mcq",
    "questionHtml": "Programmer yang mengetik dengan posisi pergelangan tangan menekuk ke atas secara kaku selama bertahun-tahun berisiko tinggi mengalami penyempitan saraf medianus di pergelangan tangan yang dikenal sebagai Carpal Tunnel Syndrome (CTS). Praktik ergonomi kerja yang benar untuk mencegah gangguan tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "Mengetik dengan posisi pergelangan tangan menggantung bebas di udara tanpa sandaran apapun di meja.                                                      "
      },
      {
        "key": "B",
        "text": "Menjaga posisi pergelangan tangan lurus dan netral saat mengetik serta menggunakan wrist rest pendukung yang empuk.                                      "
      },
      {
        "key": "C",
        "text": "Menekan tombol keyboard sekeras mungkin untuk melatih kekuatan otot dan ligamen jari jemari tangan.                                                      "
      },
      {
        "key": "D",
        "text": "Mengatur ketinggian kursi serendah mungkin sehingga siku berada jauh di bawah permukaan meja kerja untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "E",
        "text": "Menonaktifkan pendingin ruangan AC agar suhu pergelangan tangan selalu berada di atas empat puluh derajat.                                               "
      }
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-20",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Pola Desain Factory Method",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi pengolah dokumen perlu mendukung ekspor ke berbagai format file: PDF, Word, dan Excel. Jika programmer menggunakan pola desain *Factory Method*, keuntungan arsitektural yang diperoleh pada kelas klien adalah...",
    "options": [
      {
        "key": "A",
        "text": "Klien harus membuat objek menggunakan kata kunci new untuk setiap kelas konkret spesifik secara manual sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "B",
        "text": "Ukuran memori heap aplikasi otomatis menjadi nol megabyte saat proses konversi dokumen berlangsung.                                                          "
      },
      {
        "key": "C",
        "text": "Klien terisolasi dari proses instansiasi konkret, hanya bergantung pada interface dokumen umum (Loose Coupling).                                             "
      },
      {
        "key": "D",
        "text": "Seluruh kelas pemroses dokumen dipaksa mewarisi method statis dari kelas java.lang.System.                                                                   "
      },
      {
        "key": "E",
        "text": "Dokumen yang diekspor otomatis terenkripsi dengan kunci asimetris RSA tanpa perlu konfigurasi.                                                               "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "CREATIONAL DESIGN PATTERN: FACTORY METHOD",
      "latex": "\\text{Client} \\xrightarrow{\\text{calls}} \\text{DocumentFactory.create(type)} \\to \\text{returns Interface Document}",
      "legend": "• Mengisolasi kode pembuatan objek dari kode pengguna objek<br>• Mempermudah penambahan format dokumen baru tanpa merusak kelas klien (OCP compliant)"
    },
    "hints": {
      "concept": "Pola Factory Method memisahkan proses pembuatan objek dari kode klien. Klien cukup memanggil factory dengan tipe yang diinginkan dan menerima objek berbasis interface.",
      "execution": "Manfaat utamanya adalah loose coupling dan fleksibilitas penambahan kelas baru tanpa mengubah kode klien."
    },
    "explanation": "Pola desain *Factory Method* mengabstraksi proses instansiasi objek. Klien hanya berinteraksi dengan factory dan tipe antarmuka umum (`Document`), sehingga kelas klien tidak terikat langsung (decoupled) dengan kelas-kelas konkret (`PdfDocument`, `WordDocument`, `ExcelDocument`), mematuhi prinsip Open/Closed. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & API",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Keamanan API: Mitigasi SQL Injection pada Raw Query ORM",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode backend NodeJS yang menggunakan library basis data berikut:\n```javascript\n// Potongan kode A (Vulnerable)\nconst query = `SELECT * FROM users WHERE email = '${req.body.email}'`;\ndb.query(query);\n\n// Potongan kode B (Secure)\nconst query = `SELECT * FROM users WHERE email = ?`;\ndb.query(query, [req.body.email]);\n```\nMengapa pendekatan B kebal terhadap serangan SQL Injection dibandingkan pendekatan A?",
    "options": [
      {
        "key": "A",
        "text": "Karena tanda tanya (?) secara otomatis mengubah seluruh karakter input peretas menjadi angka nol integer dalam rangka menjaga efisiensi alokasi sumber daya komputasi secara berkelanjutan."
      },
      {
        "key": "B",
        "text": "Karena array kedua secara fisik mengenkripsi koneksi jaringan database menggunakan sertifikat TLS.                                                                 "
      },
      {
        "key": "C",
        "text": "Karena pendekatan B membatasi panjang input email maksimal hanya boleh terdiri dari sepuluh karakter.                                                              "
      },
      {
        "key": "D",
        "text": "Karena database engine mengompilasi struktur query terlebih dahulu dan memperlakukan input pengguna murni sebagai data literal.                                    "
      },
      {
        "key": "E",
        "text": "Karena tanda kutip satu (') pada email otomatis diganti dengan tanda kutip ganda (\") oleh driver database.                                                         "
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "PARAMETERIZED QUERY (PREPARED STATEMENT) MECHANISM",
      "latex": "\\text{SQL AST Compiled Once} \\implies \\text{Parameters Bound Separately as Raw Data Literals}",
      "legend": "• Input penyerang (misal: ' OR '1'='1) tidak dapat mengubah struktur pohon sintaksis query SQL"
    },
    "hints": {
      "concept": "Prepared Statement / Parameterized Query memisahkan kode SQL dari data. Engine database mengompilasi template SQL terlebih dahulu, lalu menyisipkan parameter sebagai nilai literal murni yang tidak dapat mengubah struktur query.",
      "execution": "Input berbahaya tidak akan pernah dieksekusi sebagai perintah SQL."
    },
    "explanation": "Pada Parameterized Queries (Pendekatan D), database engine mem-parsing dan mengompilasi struktur perintah SQL sebelum nilai parameter disisipkan. Data dari pengguna diperlakukan murni sebagai nilai literal (bukan bagian dari sintaks eksekusi SQL), sehingga payload serangan seperti `' OR '1'='1` tidak dapat mengubah logika query database. Jawaban: D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-22",
    "subject": "rpl",
    "materi": "DESAIN UI/UX & AKSESIBILITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Prinsip Usability: User Control & Freedom (Undo)",
    "type": "mcq",
    "questionHtml": "Aplikasi manajemen email menyediakan notifikasi toast 'Pesan telah diarsipkan' disertai tombol aksi 'Undo' (Batal) yang melayang selama 7 detik setelah pengguna mengusap (swipe) sebuah email. Prinsip Jakob Nielsen manakah yang secara langsung mendasari desain tersebut?",
    "options": [
      {
        "key": "A",
        "text": "Flexibility and efficiency of use untuk memberikan pengalaman mengetik cepat bagi programmer mahir."
      },
      {
        "key": "B",
        "text": "Help and documentation yang menyediakan buku manual tebal petunjuk pengoperasian perangkat lunak.  "
      },
      {
        "key": "C",
        "text": "Aesthetic and minimalist design dengan menghapus seluruh tombol navigasi dari tampilan layar ponsel."
      },
      {
        "key": "D",
        "text": "Recognition rather than recall dengan mewajibkan pengguna mengingat kembali kata sandi akun email. "
      },
      {
        "key": "E",
        "text": "User control and freedom dengan menyediakan pintu darurat keluar bagi pengguna yang tidak sengaja melakukan aksi."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "NIELSEN HEURISTIC #3: USER CONTROL & FREEDOM",
      "latex": "\\text{Accidental User Action} \\xrightarrow{\\text{Provide Emergency Exit}} \\text{Instant Undo Functionality}",
      "legend": "• Memberikan rasa aman psikologis bagi pengguna saat bereksplorasi<br>• Menghilangkan ketakutan akan kehilangan data permanen"
    },
    "hints": {
      "concept": "Heuristik ke-3: User Control and Freedom. Pengguna sering melakukan kesalahan secara tidak sengaja dan memerlukan 'pintu darurat' yang jelas untuk membatalkan aksi tanpa alur berbelit-belit.",
      "execution": "Fitur Undo pembatalan aksi adalah representasi murni dari User Control and Freedom."
    },
    "explanation": "Heuristik Usability ke-3 Jakob Nielsen (User Control and Freedom) menyatakan bahwa pengguna kerap memilih fungsi sistem secara keliru dan membutuhkan 'pintu darurat' yang terlihat jelas untuk meninggalkan kondisi yang tidak diinginkan tanpa harus melalui dialog yang panjang. Fitur 'Undo' adalah perwujudan sempurna dari prinsip ini. Jawaban: E.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-23",
    "subject": "rpl",
    "materi": "ALGORITMA & PEMROGRAMAN TERSTRUKTUR",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Rekursi & Rekursi Ekor (Tail Call Optimization)",
    "type": "mcq",
    "questionHtml": "Perhatikan fungsi rekursif perhitungan faktorial berikut:\n```python\ndef faktorial_biasa(n):\n    if n <= 1:\n        return 1\n    return n * faktorial_biasa(n - 1)\n```\nJika fungsi di atas dipanggil dengan nilai $n = 50.000$, program akan mengalami crash dengan error `RecursionError: maximum recursion depth exceeded`. Penyebab struktural dari kegagalan tersebut pada level memori adalah...",
    "options": [
      {
        "key": "A",
        "text": "Setiap pemanggilan rekursif menumpuk stack frame baru di Call Stack hingga melampaui batas alokasi memori stack.                                 "
      },
      {
        "key": "B",
        "text": "Kapasitas media penyimpanan hard disk sekunder penuh akibat pembuatan file log sistem otomatis.                                                  "
      },
      {
        "key": "C",
        "text": "Bahasa pemrograman Python tidak mengizinkan operasi perkalian angka bertipe integer melampaui seratus.                                           "
      },
      {
        "key": "D",
        "text": "CPU komputer menolak mengeksekusi percabangan kondisi if yang memiliki lebih dari satu operator logika.                                          "
      },
      {
        "key": "E",
        "text": "Variabel n mengalami overflow dan berubah nilainya menjadi string huruf acak tak terdefinisi guna mencegah inkonsistensi perilaku sistem pada lingkungan multi-server."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "CALL STACK OVERFLOW DYNAMICS",
      "latex": "\\sum_{i=1}^{n} \\text{StackFrame}(i) > \\text{Max Stack Size} \\implies \\text{StackOverflow / RecursionError}",
      "legend": "• Non-tail recursion: Menyimpan state perkalian di stack frame aktif hingga basis terpenuhi<br>• Solusi: Gunakan iterasi loop (while/for) atau tail recursion dengan akumulator"
    },
    "hints": {
      "concept": "Setiap pemanggilan fungsi menempatkan stack frame baru di Call Stack (menyimpan variabel lokal dan return address). Jika rekursi terlalu dalam, alokasi Call Stack habis.",
      "execution": "Peristiwa ini dinamakan Stack Overflow (di Python memicu RecursionError)."
    },
    "explanation": "Pada rekursi standar, setiap pemanggilan fungsi yang belum selesai (karena masih menunggu hasil perkalian `n * ...`) harus mempertahankan stack frame-nya di Call Stack memori. Ketika kedalaman pemanggilan mencapai puluhan ribu, alokasi memori stack terlampaui sehingga Python melempar `RecursionError` untuk mencegah crash total sistem operasi. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-24",
    "subject": "rpl",
    "materi": "REKAYASA PEMROGRAMAN GIM",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Integrasi Fisika: Verlet vs Euler Integration",
    "type": "mcq",
    "questionHtml": "Dalam pembuatan simulasi fisika tali, kain (cloth simulation), dan partikel fisika interaktif pada gim, algoritma integrasi numerik *Verlet Integration* lebih sering dipilih daripada *Explicit Euler Integration* karena...",
    "options": [
      {
        "key": "A",
        "text": "Verlet Integration tidak membutuhkan kartu grafis GPU dan hanya dapat dihitung oleh sistem cloud server.                                                        "
      },
      {
        "key": "B",
        "text": "Verlet Integration jauh lebih stabil secara numerik dan otomatis mempertahankan kekekalan energi tanpa eksplosi posisi.                                         "
      },
      {
        "key": "C",
        "text": "Euler Integration mengharuskan seluruh objek dalam gim memiliki massa nol kilogram tanpa gaya gravitasi.                                                        "
      },
      {
        "key": "D",
        "text": "Verlet Integration secara otomatis menggambar tekstur visual kain 3D secara fotorealistis di layar monitor untuk memastikan seluruh parameter masukan tervalidasi dengan baik dan aman."
      },
      {
        "key": "E",
        "text": "Euler Integration hanya dapat memproses objek statis yang sama sekali tidak mengalami pergerakan koordinat.                                                     "
      }
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN APLIKASI BERGERAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Android Deep Linking & Intent Filters",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi Android ingin mengizinkan pengguna membuka halaman produk spesifik secara langsung saat pengguna mengklik tautan web `https://toko.smk.id/produk/123` di browser atau aplikasi chat. Komponen yang wajib dikonfigurasi di dalam file `AndroidManifest.xml` pada Activity produk adalah...",
    "options": [
      {
        "key": "A",
        "text": "Deklarasi service background dengan atribut android:exported=\"False\" dan permission akses lokasi GPS sesuai dengan rekomendasi panduan arsitektur rekayasa perangkat lunak modern."
      },
      {
        "key": "B",
        "text": "Menambahkan tag <uses-feature> kamera resolusi tinggi dengan atribut android:required=\"true\".                                                              "
      },
      {
        "key": "C",
        "text": "Mendefinisikan <intent-filter> yang memuat action VIEW, kategori DEFAULT & BROWSABLE, serta tag <data> skema https.                                        "
      },
      {
        "key": "D",
        "text": "Mengubah nama package aplikasi menjadi toko.smk.id dan menandatanganinya dengan sertifikat debug keystore.                                                 "
      },
      {
        "key": "E",
        "text": "Menulis kode skrip JavaScript AJAX di dalam file manifest untuk menangkap event klik URL pengguna.                                                         "
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "ANDROID DEEP LINK INTENT FILTER",
      "latex": "\\langle \\text{intent-filter} \\rangle \\colon \\text{action.VIEW} + \\text{category.BROWSABLE} + \\langle \\text{data scheme/host} \\rangle",
      "legend": "• BROWSABLE: Mengizinkan link dibuka dari browser web<br>• Android App Links memverifikasi kepemilikan domain via Digital Asset Links JSON"
    },
    "hints": {
      "concept": "Deep Linking di Android diaktifkan menggunakan <intent-filter> dengan action android.intent.action.VIEW, kategori BROWSABLE dan DEFAULT, serta tag data yang memuat host dan scheme URL.",
      "execution": "Konfigurasi standar Deep Link / App Link ada di pilihan B."
    },
    "explanation": "Untuk mengaktifkan Deep Linking (atau Android App Links), Activity target di dalam `AndroidManifest.xml` harus dikonfigurasi dengan `<intent-filter>` yang memuat: (1) action `android.intent.action.VIEW`, (2) kategori `android.intent.category.DEFAULT` dan `android.intent.category.BROWSABLE`, serta (3) tag `<data>` yang menetapkan `android:scheme=\"https\"` dan `android:host=\"toko.smk.id\"`. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-26",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & API",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Praktik Keamanan Web Pencegahan XSS",
    "type": "multi",
    "questionHtml": "Manakah TIGA praktik rekayasa perangkat lunak web yang efektif dan direkomendasikan oleh standar OWASP untuk mencegah kerentanan Cross-Site Scripting (XSS)?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan encoding karakter kontekstual (HTML Entity Encoding) terhadap seluruh data input sebelum dirender ke halaman."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi domain eksekusi skrip JavaScript yang diizinkan."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam Cookie dengan flag HttpOnly daripada di dalam localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti innerHTML secara langsung untuk menampilkan teks mentah dari parameter URL tanpa sanitasi."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol komunikasi HTTPS pada server web dan beralih sepenuhnya ke protokol HTTP biasa."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-27",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Penyebab Terjadinya Full Table Scan pada Database",
    "type": "multi",
    "questionHtml": "Manakah TIGA kondisi penulisan query SQL berikut yang dapat menyebabkan Database Query Optimizer mengabaikan indeks B-Tree yang sudah ada dan terpaksa melakukan pembacaan seluruh tabel secara sekuensial (Full Table Scan)?",
    "options": [
      {
        "key": "A",
        "text": "Menggunakan fungsi transformasi matematika atau manipulasi string pada kolom berindeks (misal: WHERE YEAR(tanggal) = 2026)."
      },
      {
        "key": "B",
        "text": "Menggunakan klausa pencarian string pola wildcard di awal kata (misal: WHERE nama_lengkap LIKE '%Santoso')."
      },
      {
        "key": "C",
        "text": "Melakukan perbandingan data antar tipe data yang tidak cocok sehingga memicu konversi tipe implisit (Implicit Casting)."
      },
      {
        "key": "D",
        "text": "Menggunakan perbandingan kesetaraan eksak pada kolom primary key tunggal (misal: WHERE id_user = 105)."
      },
      {
        "key": "E",
        "text": "Menyertakan klausul LIMIT 1 pada query pencarian baris data tabel basis data."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-28",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Indikator Pelanggaran Prinsip Desain SOLID",
    "type": "multi",
    "questionHtml": "Manakah DUA skenario arsitektur kode di bawah ini yang mengindikasikan adanya pelanggaran terhadap prinsip-prinsip SOLID?",
    "options": [
      {
        "key": "A",
        "text": "Sebuah kelas OrderService memiliki lebih dari 3.000 baris kode yang menangani validasi keranjang, kalkulasi pajak, koneksi database, pengiriman email konfirmasi, dan pembuatan invoice PDF."
      },
      {
        "key": "B",
        "text": "Sebuah subclass BurungUnta mewarisi superclass Burung dan meng-override method terbang() dengan melempar UnsupportedOperationException karena burung unta tidak dapat terbang."
      },
      {
        "key": "C",
        "text": "Sebuah kelas NotificationService menerima interface MessageSender melalui constructor injection dan tidak bergantung pada implementasi spesifik."
      },
      {
        "key": "D",
        "text": "Sebuah interface Shape dipecah menjadi Drawable dan Resizable agar kelas yang hanya butuh menggambar tidak dipaksa mengubah ukuran."
      },
      {
        "key": "E",
        "text": "Menambahkan kelas metode pembayaran baru CryptoPayment yang mengimplementasikan interface PaymentStrategy tanpa memodifikasi kelas Checkout."
      }
    ],
    "correctKeys": [
      "A",
      "B"
    ],
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-29",
    "subject": "rpl",
    "materi": "REKAYASA PEMROGRAMAN GIM",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Faktor Penyebab Penurunan Framerate Gim Mobile",
    "type": "multi",
    "questionHtml": "Manakah TIGA faktor teknis di bawah ini yang menjadi penyebab utama terjadinya stuttering dan penurunan frame rate (FPS drop) pada gim mobile?",
    "options": [
      {
        "key": "A",
        "text": "Terjadinya lonjakan alokasi dan pembersihan memori objek dinamis secara berulang yang memicu siklus Garbage Collection (GC) pauses."
      },
      {
        "key": "B",
        "text": "Tingginya jumlah Draw Calls per frame akibat setiap partikel dan sprite menggunakan tekstur material terpisah tanpa batching."
      },
      {
        "key": "C",
        "text": "Terjadinya overdraw ekstrem di mana piksel layar yang sama digambar berulang kali oleh banyak lapisan sprite transparan tumpang tindih."
      },
      {
        "key": "D",
        "text": "Menggunakan pola desain Object Pooling untuk mengelola peluru dan partikel efek gim di dalam scene."
      },
      {
        "key": "E",
        "text": "Menyatukan ribuan gambar sprite kecil ke dalam satu lembar gambar Texture Atlas berukuran terstandarisasi."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-30",
    "subject": "rpl",
    "materi": "PROSES BISNIS & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Praktik Terbaik Pengelolaan Branch & Pull Request",
    "type": "multi",
    "questionHtml": "Manakah TIGA praktik terbaik (best practices) yang wajib diterapkan oleh tim rekayasa perangkat lunak dalam pengelolaan Git Pull Request (PR) dan Branching?",
    "options": [
      {
        "key": "A",
        "text": "Membuat Pull Request berukuran kecil dan terfokus (Small PRs) agar mudah ditinjau secara teliti dan cepat oleh reviewer."
      },
      {
        "key": "B",
        "text": "Mengintegrasikan automated linter dan automated unit test yang wajib lolos (pass) sebelum PR diizinkan untuk di-merge."
      },
      {
        "key": "C",
        "text": "Menulis deskripsi Pull Request yang jelas, memuat konteks perubahan, motivasi bisnis, dan petunjuk pengujian manual."
      },
      {
        "key": "D",
        "text": "Mengizinkan programmer melakukan bypass terhadap proses code review dan langsung melakukan push langsung ke branch main produksi."
      },
      {
        "key": "E",
        "text": "Mengumpulkan ratusan fitur berbeda yang tidak saling terkait ke dalam satu cabang branch selama enam bulan sebelum membuat PR."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-31",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Urutan Eksekusi Logika Query SQL",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik pelaporan keuangan berikut:\n```sql\nSELECT departemen, COUNT(*) AS total_staff, AVG(gaji) AS rata_gaji\nFROM pegawai\nWHERE status_kerja = 'Tetap'\nGROUP BY departemen\nHAVING AVG(gaji) >= 8000000\nORDER BY rata_gaji DESC;\n```\nEvaluasilah kebenaran pernyataan teknis mengenai urutan dan aturan eksekusi query SQL di atas:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi oleh mesin basis data sebelum proses pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Fungsi agregasi seperti AVG(gaji) diperbolehkan secara sintaksis untuk diletakkan langsung di dalam klausul WHERE."
      },
      {
        "id": "3",
        "text": "Alias kolom 'rata_gaji' dapat digunakan di dalam klausul WHERE karena klausul WHERE dieksekusi setelah SELECT."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": false
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-32",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & API",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Arsitektur Event Loop & Concurrency JavaScript",
    "type": "matrix",
    "questionHtml": "Evaluasilah kebenaran pernyataan teknis mengenai model konkurensi (Concurrency Model) dan siklus eksekusi Event Loop pada lingkungan runtime JavaScript (V8 Engine):",
    "statements": [
      {
        "id": "0",
        "text": "JavaScript berjalan pada satu Call Stack utama (Single-Threaded) untuk mengeksekusi kode program sinkron."
      },
      {
        "id": "1",
        "text": "Microtask Queue (seperti callback Promise dan queueMicrotask) memiliki prioritas eksekusi lebih tinggi dibanding Macrotask Queue (seperti setTimeout)."
      },
      {
        "id": "2",
        "text": "Fungsi setTimeout(fn, 1000) memberikan jaminan mutlak bahwa callback fn pasti dieksekusi tepat pada milidetik ke-1000 tanpa kemungkinan tertunda."
      },
      {
        "id": "3",
        "text": "Call Stack dapat memproses Macrotask berikutnya meskipun antrean di dalam Microtask Queue belum selesai dikosongkan."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": false
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-33",
    "subject": "rpl",
    "materi": "PEMROGRAMAN APLIKASI BERGERAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Siklus Hidup & Arsitektur Android",
    "type": "matrix",
    "questionHtml": "Evaluasilah kebenaran pernyataan teknis mengenai siklus hidup komponen dan manajemen memori pada sistem operasi Android:",
    "statements": [
      {
        "id": "0",
        "text": "Ketika sebuah Activity tertutup oleh dialog pop-up berukuran kecil di layarnya, Activity tersebut beralih ke status onPause() dan masih tetap terlihat sebagian."
      },
      {
        "id": "1",
        "text": "Komponen Android Jetpack ViewModel otomatis dihancurkan dan dibersihkan dari memori saat pengguna memutar orientasi layar smartphone."
      },
      {
        "id": "2",
        "text": "Operasi pembacaan file besar atau pengunduhan data jaringan HTTP dilarang dijalankan secara langsung pada Main Thread untuk menghindari Application Not Responding (ANR)."
      },
      {
        "id": "3",
        "text": "Callback method onDestroy() dijamin pasti selalu dipanggil oleh sistem Android saat memori RAM ponsel mengalami kondisi darurat kelangkaan memori (low memory)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-34",
    "subject": "rpl",
    "materi": "PROSES BISNIS & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Evaluasi Metodologi SDLC Agile Scrum vs Waterfall",
    "type": "matrix",
    "questionHtml": "Evaluasilah kebenaran pernyataan mengenai karakteristik metodologi siklus hidup pengembangan perangkat lunak (SDLC) Agile Scrum dan Waterfall:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam kerangka kerja Scrum, perubahan kebutuhan bisnis diperbolehkan dan disambut dengan baik bahkan di tahapan akhir pengembangan aplikasi."
      },
      {
        "id": "1",
        "text": "Model Waterfall sangat fleksibel dan memungkinkan tim kembali ke tahap analisis kebutuhan dengan mudah saat tahap pengujian menemukan kekurangan fitur."
      },
      {
        "id": "2",
        "text": "Sprint Retrospective adalah pertemuan rutin di akhir sprint yang bertujuan mengevaluasi proses kerja tim dan merencanakan perbaikan berkelanjutan untuk sprint berikutnya."
      },
      {
        "id": "3",
        "text": "Product Owner memiliki wewenang penuh untuk mengubah isi dan komitmen Sprint Backlog di tengah-tengah berjalannya Sprint yang sedang aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
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
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-35",
    "subject": "rpl",
    "materi": "K3LH & HAKI PERANGKAT LUNAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Regulasi Lisensi Open Source & UU Perlindungan Data",
    "type": "matrix",
    "questionHtml": "Evaluasilah kebenaran pernyataan hukum dan kepatuhan (compliance) perangkat lunak terkait lisensi open source dan perlindungan data pribadi:",
    "statements": [
      {
        "id": "0",
        "text": "Lisensi MIT mengizinkan pihak lain memodifikasi kode sumber dan menggunakannya dalam aplikasi komersial tertutup (closed-source proprietary)."
      },
      {
        "id": "1",
        "text": "Lisensi GNU General Public License (GPL) mewajibkan seluruh proyek turunan yang memuat kode GPL untuk ikut melisensikan source code-nya secara terbuka di bawah GPL."
      },
      {
        "id": "2",
        "text": "Berdasarkan UU Perlindungan Data Pribadi (UU PDP) Indonesia, pengembang aplikasi berhak menjual data pribadi pengguna kepada pihak ketiga tanpa memerlukan persetujuan eksplisit (consent)."
      },
      {
        "id": "3",
        "text": "Klausul lisensi open source permissive (seperti BSD dan MIT) secara otomatis menghapus kewajiban pengembang untuk menyertakan disclaimer hak cipta asli pembuatnya."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": false
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
    "isDiagnostic": false
  }
];