/**
 * TKA MASTERY HUB — QUESTIONS_INFORMATIKA.JS (135 SOAL DENGAN SCAFFOLDING LENGKAP PADA LATIHAN)
 */
window.TKA_INFORMATIKA_QUESTIONS = [
  {
    "id": "inf_001",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [51, 31, 71, 21, 41, 61, 81]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_002",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_003",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_004",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [54, 34, 74, 24, 44, 64, 84]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_005",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_006",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_007",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [57, 37, 77, 22, 47, 67, 87]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "B",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(B) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_008",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_009",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_010",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [60, 30, 80, 20, 42, 70, 80]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_011",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_012",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_013",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [63, 33, 83, 23, 45, 61, 83]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "D",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(D) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_014",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_015",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_016",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [66, 36, 71, 21, 40, 64, 86]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_017",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_018",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_019",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [69, 39, 74, 24, 43, 67, 89]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "B",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(B) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_020",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_021",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_022",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [52, 32, 77, 22, 46, 70, 82]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "B",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(B) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_023",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_024",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_025",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [55, 35, 80, 20, 41, 61, 85]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_026",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_027",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_028",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [58, 38, 83, 23, 44, 64, 88]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      }
    ],
    "correctAnswer": "E",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(E) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_029",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_030",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_031",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [61, 31, 71, 21, 47, 67, 81]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_032",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_033",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_034",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [64, 34, 74, 24, 42, 70, 84]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "B",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_035",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "easy",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_036",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_037",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [67, 37, 77, 22, 45, 61, 87]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      }
    ],
    "correctAnswer": "B",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(B) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_038",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_039",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_040",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [50, 30, 80, 20, 40, 64, 80]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_041",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_042",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_043",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [53, 33, 83, 23, 43, 67, 83]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "B",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(B) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_044",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_045",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_046",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [56, 36, 71, 21, 46, 70, 86]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      }
    ],
    "correctAnswer": "E",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(E) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_047",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_048",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_049",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [59, 39, 74, 24, 41, 61, 89]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      }
    ],
    "correctAnswer": "D",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(D) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_050",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_051",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_052",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [62, 32, 77, 22, 44, 64, 82]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "B",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(B) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_053",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_054",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_055",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [65, 35, 80, 20, 47, 67, 85]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_056",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_057",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_058",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [68, 38, 83, 23, 42, 70, 88]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "E",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_059",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_060",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_061",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [51, 31, 71, 21, 45, 61, 81]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "C",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      }
    ],
    "correctAnswer": "D",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(D) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_062",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_063",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_064",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [54, 34, 74, 24, 40, 64, 84]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      }
    ],
    "correctAnswer": "E",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(E) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_065",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_066",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_067",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [57, 37, 77, 22, 43, 67, 87]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_068",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_069",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_070",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "medium",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [60, 30, 80, 20, 46, 70, 80]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "B",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(B) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_071",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_072",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_073",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [63, 33, 83, 23, 41, 61, 83]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      }
    ],
    "correctAnswer": "E",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(E) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_074",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_075",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_076",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [66, 36, 71, 21, 44, 64, 86]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "D",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(D) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_077",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_078",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_079",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [69, 39, 74, 24, 47, 67, 89]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "B",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "C",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      }
    ],
    "correctAnswer": "E",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(E) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_080",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_081",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_082",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [52, 32, 77, 22, 42, 70, 82]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "A",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(A) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_083",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_084",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_085",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [55, 35, 80, 20, 45, 61, 85]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_086",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_087",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_088",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [58, 38, 83, 23, 40, 64, 88]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_089",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_090",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_091",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [61, 31, 71, 21, 43, 67, 81]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_092",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_093",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_094",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [64, 34, 74, 24, 46, 70, 84]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_095",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_096",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_097",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [67, 37, 77, 22, 41, 61, 87]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "B",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      }
    ],
    "correctAnswer": "E",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(E) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_098",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_099",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_100",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [50, 30, 80, 20, 44, 64, 80]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "B",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_101",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_102",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_103",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [53, 33, 83, 23, 47, 67, 83]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "formula_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
    "formula_latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
    "formula_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
    "concept_hint": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
    "execution_hint": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "C",
    "formulaHud": {
      "title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
      "latex": "T(n) = O(n \\log n), \\quad \\text{BST Search} = O(\\log n)",
      "legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data"
    },
    "hints": {
      "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
      "execution": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik.</p><p><strong>3. Kesimpulan & Kunci Jawaban:</strong><br>Berdasarkan kaidah dan analisis di atas, opsi yang paling tepat adalah <strong>(C) Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.</strong>.</p></div>"
  },
  {
    "id": "inf_104",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "formula_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
    "formula_latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
    "formula_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
    "concept_hint": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
    "execution_hint": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ],
    "formulaHud": {
      "title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
      "latex": "\\text{Enkripsi RSA: } C = M^e \\pmod n, \\quad \\text{Dekripsi: } M = C^d \\pmod n",
      "legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat"
    },
    "hints": {
      "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
      "execution": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah.</p><p><strong>3. Verifikasi Validitas Pernyataan (Tabel Benar-Salah):</strong><br>• <em>Pernyataan 1</em>: \"Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 2</em>: \"Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.\" &rarr; <strong>BENAR</strong><br>• <em>Pernyataan 3</em>: \"Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.\" &rarr; <strong>SALAH</strong><br>• <em>Pernyataan 4</em>: \"Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).\" &rarr; <strong>BENAR</strong><br></p></div>"
  },
  {
    "id": "inf_105",
    "subject": "informatika",
    "mode": "latihan",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "formula_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
    "formula_latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
    "formula_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
    "concept_hint": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
    "execution_hint": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ],
    "formulaHud": {
      "title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
      "latex": "\\text{Kueri SQL: } \\text{SELECT } \\dots \\text{ FROM } R_1 \\bowtie R_2 \\text{ WHERE } \\dots",
      "legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data"
    },
    "hints": {
      "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
      "execution": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
    },
    "explanation": "<div class=\"solution-content\"><p><strong>1. Identifikasi Materi & Konsep Dasar:</strong><br>ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).</p><p><strong>2. Langkah Analisis & Eksekusi:</strong><br>Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan.</p><p><strong>3. Evaluasi Pilihan Ganda Kompleks:</strong><br>• <strong>Opsi (A):</strong> Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing). &rarr; <em>Sesuai dengan stimulus dan kaidah materi</em>.<br>Kesimpulan: Kunci kombinasi yang benar adalah <strong>A</strong>.</p></div>"
  },
  {
    "id": "inf_106",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [56, 36, 71, 21, 42, 70, 86]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      }
    ],
    "correctAnswer": "B"
  },
  {
    "id": "inf_107",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_108",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_109",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [59, 39, 74, 24, 45, 61, 89]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      }
    ],
    "correctAnswer": "C"
  },
  {
    "id": "inf_110",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_111",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_112",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [62, 32, 77, 22, 40, 64, 82]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "D"
  },
  {
    "id": "inf_113",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_114",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_115",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [65, 35, 80, 20, 43, 67, 85]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "C"
  },
  {
    "id": "inf_116",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_117",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_118",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [68, 38, 83, 23, 46, 70, 88]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "E",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      }
    ],
    "correctAnswer": "D"
  },
  {
    "id": "inf_119",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_120",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_121",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [51, 31, 71, 21, 41, 61, 81]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "B",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "E",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      }
    ],
    "correctAnswer": "D"
  },
  {
    "id": "inf_122",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_123",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_124",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [54, 34, 74, 24, 44, 64, 84]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "E",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      }
    ],
    "correctAnswer": "B"
  },
  {
    "id": "inf_125",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_126",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_127",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [57, 37, 77, 22, 47, 67, 87]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      },
      {
        "key": "B",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "C",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      }
    ],
    "correctAnswer": "E"
  },
  {
    "id": "inf_128",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_129",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_130",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [60, 30, 80, 20, 42, 70, 80]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "D",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "A"
  },
  {
    "id": "inf_131",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_132",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  },
  {
    "id": "inf_133",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "mcq",
    "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
    "topic": "Algoritma Rekursi, Tree, & Graf",
    "question": "Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [63, 33, 83, 23, 45, 61, 83]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
    "options": [
      {
        "key": "A",
        "text": "Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah."
      },
      {
        "key": "B",
        "text": "Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar."
      },
      {
        "key": "C",
        "text": "Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
      },
      {
        "key": "D",
        "text": "Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar."
      },
      {
        "key": "E",
        "text": "Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal secara efisien dan deterministik."
      }
    ],
    "correctAnswer": "D"
  },
  {
    "id": "inf_134",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "matrix",
    "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
    "topic": "Protokol Komunikasi & Kriptografi",
    "question": "Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
    "statements": [
      {
        "text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.",
        "answer": true
      },
      {
        "text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.",
        "answer": true
      },
      {
        "text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.",
        "answer": false
      },
      {
        "text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).",
        "answer": true
      }
    ]
  },
  {
    "id": "inf_135",
    "subject": "informatika",
    "mode": "simulasi",
    "difficulty": "hard",
    "type": "multi",
    "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
    "topic": "SQL Relasional & Siklus SDLC",
    "question": "Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
    "options": [
      {
        "key": "A",
        "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).",
        "correct": true
      },
      {
        "key": "B",
        "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.",
        "correct": true
      },
      {
        "key": "C",
        "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.",
        "correct": true
      },
      {
        "key": "D",
        "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.",
        "correct": false
      },
      {
        "key": "E",
        "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.",
        "correct": false
      }
    ]
  }
];
