/**
 * TKA MASTERY HUB — QUESTIONS_RPL.JS (135 SOAL AUTENTIK)
 */
window.TKA_RPL_QUESTIONS = [
  {
    "id": "rpl-lat-e-01",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-02",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-03",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-04",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-05",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-06",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-07",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-08",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-09",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-10",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-11",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-12",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "multi",
    "questionHtml": "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
    "options": [
      {
        "key": "A",
        "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)"
      },
      {
        "key": "B",
        "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)"
      },
      {
        "key": "C",
        "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)"
      },
      {
        "key": "D",
        "text": "git push --force origin main (menimpa repositori remote secara paksa)"
      },
      {
        "key": "E",
        "text": "git init --bare (menghapus seluruh working directory di mesin lokal)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Perintah inspeksi non-destruktif: status, diff, dan log.",
      "execution": "Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-13",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-14",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-15",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-16",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-17",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-18",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-19",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-20",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-22",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-23",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-24",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "multi",
    "questionHtml": "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
    "options": [
      {
        "key": "A",
        "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)"
      },
      {
        "key": "B",
        "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)"
      },
      {
        "key": "C",
        "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)"
      },
      {
        "key": "D",
        "text": "git push --force origin main (menimpa repositori remote secara paksa)"
      },
      {
        "key": "E",
        "text": "git init --bare (menghapus seluruh working directory di mesin lokal)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Perintah inspeksi non-destruktif: status, diff, dan log.",
      "execution": "Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-26",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-27",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-28",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-29",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-30",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-31",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-32",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-33",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-34",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-35",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-01",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-02",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-03",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-04",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-05",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-06",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-07",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-08",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-09",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-10",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-11",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-12",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "multi",
    "questionHtml": "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
    "options": [
      {
        "key": "A",
        "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)"
      },
      {
        "key": "B",
        "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)"
      },
      {
        "key": "C",
        "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)"
      },
      {
        "key": "D",
        "text": "git push --force origin main (menimpa repositori remote secara paksa)"
      },
      {
        "key": "E",
        "text": "git init --bare (menghapus seluruh working directory di mesin lokal)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Perintah inspeksi non-destruktif: status, diff, dan log.",
      "execution": "Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-13",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-14",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-15",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-16",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-17",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-18",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-19",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-20",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-22",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-23",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-24",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "multi",
    "questionHtml": "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
    "options": [
      {
        "key": "A",
        "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)"
      },
      {
        "key": "B",
        "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)"
      },
      {
        "key": "C",
        "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)"
      },
      {
        "key": "D",
        "text": "git push --force origin main (menimpa repositori remote secara paksa)"
      },
      {
        "key": "E",
        "text": "git init --bare (menghapus seluruh working directory di mesin lokal)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Perintah inspeksi non-destruktif: status, diff, dan log.",
      "execution": "Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-26",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-27",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-28",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-29",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-30",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-31",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-32",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-33",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-34",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-35",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-01",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-02",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-03",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-04",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-05",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-06",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-07",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-08",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-09",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-10",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-11",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-12",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "multi",
    "questionHtml": "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
    "options": [
      {
        "key": "A",
        "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)"
      },
      {
        "key": "B",
        "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)"
      },
      {
        "key": "C",
        "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)"
      },
      {
        "key": "D",
        "text": "git push --force origin main (menimpa repositori remote secara paksa)"
      },
      {
        "key": "E",
        "text": "git init --bare (menghapus seluruh working directory di mesin lokal)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Perintah inspeksi non-destruktif: status, diff, dan log.",
      "execution": "Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-13",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-14",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-15",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-16",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-17",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-18",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-19",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-20",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-22",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-23",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-24",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "multi",
    "questionHtml": "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
    "options": [
      {
        "key": "A",
        "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)"
      },
      {
        "key": "B",
        "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)"
      },
      {
        "key": "C",
        "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)"
      },
      {
        "key": "D",
        "text": "git push --force origin main (menimpa repositori remote secara paksa)"
      },
      {
        "key": "E",
        "text": "git init --bare (menghapus seluruh working directory di mesin lokal)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Perintah inspeksi non-destruktif: status, diff, dan log.",
      "execution": "Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
      "execution": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-26",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
      "execution": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-27",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
      "execution": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-28",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
      "execution": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
    },
    "explanation": "Analisis rekayasa perangkat lunak: git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-29",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
      "execution": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-30",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
      "execution": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS. Opsi yang benar: A, B, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-31",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
      "execution": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
    },
    "explanation": "Analisis rekayasa perangkat lunak: '1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-32",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
      "latex": "\\text{main} \\leftarrow \\text{release} \\leftarrow \\text{develop} \\leftarrow \\text{feature-branch}",
      "legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik"
    },
    "hints": {
      "concept": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
      "execution": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-33",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "PRINSIP 4 PILAR OOP (SOLID)",
      "latex": "\\text{Class} \\xrightarrow{\\text{Inheritance}} \\text{Subclass}, \\quad \\text{Interface} \\xrightarrow{\\text{Implements}} \\text{Polymorphic Object}",
      "legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class"
    },
    "hints": {
      "concept": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
      "execution": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
    },
    "explanation": "Analisis multi-jawaban RPL: Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture. Opsi yang benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-34",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ALJABAR RELASIONAL & ATURAN ACID",
      "latex": "\\text{Atomik} \\xrightarrow{1\\text{NF}} \\text{Ketergantungan Parsial} \\xrightarrow{2\\text{NF}} \\text{Ketergantungan Transitif} \\xrightarrow{3\\text{NF}} \\text{Ternormalisasi}",
      "legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif"
    },
    "hints": {
      "concept": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
      "execution": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
    },
    "explanation": "Analisis rekayasa perangkat lunak: Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF. Jawaban yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-35",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "formulaHud": {
      "title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
      "latex": "\\text{Call Stack} \\to \\text{Web API} \\to \\text{Callback/Microtask Queue} \\xrightarrow{\\text{Event Loop}} \\text{Call Stack}",
      "legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue"
    },
    "hints": {
      "concept": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
      "execution": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
    },
    "explanation": "Evaluasi kompetensi kejuruan RPL: Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-01",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-02",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-03",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-04",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-05",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-06",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-07",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-08",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-09",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-10",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-11",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-12",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "multi",
    "questionHtml": "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
    "options": [
      {
        "key": "A",
        "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)"
      },
      {
        "key": "B",
        "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)"
      },
      {
        "key": "C",
        "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)"
      },
      {
        "key": "D",
        "text": "git push --force origin main (menimpa repositori remote secara paksa)"
      },
      {
        "key": "E",
        "text": "git init --bare (menghapus seluruh working directory di mesin lokal)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-13",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-14",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-15",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-16",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-17",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-18",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-19",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "mcq",
    "questionHtml": "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\n\nsetTimeout(() => {\n    console.log('2');\n}, 0);\n\nPromise.resolve().then(() => {\n    console.log('3');\n});\n\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
    "options": [
      {
        "key": "A",
        "text": "1, 4, 3, 2"
      },
      {
        "key": "B",
        "text": "1, 2, 3, 4"
      },
      {
        "key": "C",
        "text": "1, 3, 4, 2"
      },
      {
        "key": "D",
        "text": "1, 4, 2, 3"
      },
      {
        "key": "E",
        "text": "3, 1, 4, 2"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-20",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "matrix",
    "questionHtml": "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat."
      },
      {
        "id": "1",
        "text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi."
      },
      {
        "id": "2",
        "text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target."
      },
      {
        "id": "3",
        "text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "multi",
    "questionHtml": "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak."
      },
      {
        "key": "B",
        "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan."
      },
      {
        "key": "C",
        "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation)."
      },
      {
        "key": "D",
        "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar."
      },
      {
        "key": "E",
        "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-22",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "mcq",
    "questionHtml": "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "2NF (karena masih terdapat ketergantungan transitif)"
      },
      {
        "key": "B",
        "text": "1NF (karena kolom belum dipisahkan sama sekali)"
      },
      {
        "key": "C",
        "text": "3NF (karena telah memiliki primary key unik)"
      },
      {
        "key": "D",
        "text": "BCNF (karena setiap penentu adalah candidate key)"
      },
      {
        "key": "E",
        "text": "Unnormalized Form (karena ada redudansi data)"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-23",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "matrix",
    "questionHtml": "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
    "statements": [
      {
        "id": "0",
        "text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal)."
      },
      {
        "id": "1",
        "text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna."
      },
      {
        "id": "2",
        "text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL."
      },
      {
        "id": "3",
        "text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View)."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-24",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "multi",
    "questionHtml": "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
    "options": [
      {
        "key": "A",
        "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)"
      },
      {
        "key": "B",
        "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)"
      },
      {
        "key": "C",
        "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)"
      },
      {
        "key": "D",
        "text": "git push --force origin main (menimpa repositori remote secara paksa)"
      },
      {
        "key": "E",
        "text": "git init --bare (menghapus seluruh working directory di mesin lokal)"
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() {\n        System.out.println(\"Pegawai bekerja\");\n    }\n}\n\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() {\n        System.out.println(\"Programmer coding\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "Programmer coding"
      },
      {
        "key": "B",
        "text": "Pegawai bekerja"
      },
      {
        "key": "C",
        "text": "Pegawai bekerja Programmer coding"
      },
      {
        "key": "D",
        "text": "Compile-time error: Type mismatch object"
      },
      {
        "key": "E",
        "text": "Runtime error: ClassCastException"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-26",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "matrix",
    "questionHtml": "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) AS total_siswa, AVG(nilai) AS rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY."
      },
      {
        "id": "1",
        "text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah."
      },
      {
        "id": "2",
        "text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'."
      },
      {
        "id": "3",
        "text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": false,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-27",
    "subject": "rpl",
    "materi": "PEMROGRAMAN WEB & MOBILE",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "JavaScript Asynchronous & State Management",
    "type": "multi",
    "questionHtml": "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
    "options": [
      {
        "key": "A",
        "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM."
      },
      {
        "key": "B",
        "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya."
      },
      {
        "key": "C",
        "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser."
      },
      {
        "key": "D",
        "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna."
      },
      {
        "key": "E",
        "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-28",
    "subject": "rpl",
    "materi": "VERSION CONTROL SYSTEM & SDLC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Git Workflow & Resolusi Konflik Merge",
    "type": "mcq",
    "questionHtml": "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
    "options": [
      {
        "key": "A",
        "text": "git merge --abort"
      },
      {
        "key": "B",
        "text": "git reset --soft HEAD~1"
      },
      {
        "key": "C",
        "text": "git checkout -b abort-merge"
      },
      {
        "key": "D",
        "text": "git clean -fd"
      },
      {
        "key": "E",
        "text": "git branch -D fitur-login"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-29",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Enkapsulasi, Inheritance & Polimorfisme",
    "type": "matrix",
    "questionHtml": "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
    "statements": [
      {
        "id": "0",
        "text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama."
      },
      {
        "id": "1",
        "text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'."
      },
      {
        "id": "2",
        "text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi."
      },
      {
        "id": "3",
        "text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": true
    },
    "isDiagnostic": false
  },
  {
    "id": "rpl-sim-30",
    "subject": "rpl",
    "materi": "BASIS DATA RELASIONAL & SQL",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Normalisasi 1NF-3NF & Query Kompleks",
    "type": "multi",
    "questionHtml": "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
    "options": [
      {
        "key": "A",
        "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback)."
      },
      {
        "key": "B",
        "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint."
      },
      {
        "key": "C",
        "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara."
      },
      {
        "key": "D",
        "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server."
      },
      {
        "key": "E",
        "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C",
      "D"
    ],
    "isDiagnostic": false
  }
];
