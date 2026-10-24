# -*- coding: utf-8 -*-
"""
TKA PPLG - 35 SOAL SIMULASI RESMI (rpl-sim-01 s.d. rpl-sim-35)
Mengadopsi langsung materi autentik Simulasi Resmi TKA PPLG Pusmendik
- 25 Soal Pilihan Ganda (MCQ): rpl-sim-01 s.d. rpl-sim-25
- 5 Soal Pilihan Ganda Kompleks (Multi): rpl-sim-26 s.d. rpl-sim-30
- 5 Soal Kategori Benar/Salah (Matrix): rpl-sim-31 s.d. rpl-sim-35
"""

SIMULASI_QUESTIONS = [
  # =============================================================
  # BAGIAN I: 25 SOAL PILIHAN GANDA SIMULASI (rpl-sim-01 s.d. 25)
  # =============================================================

  # --- ADOPSI LANGSUNG SOAL 26 S.D. 30 PDF ---
  {
    "id": "rpl-sim-01",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Enkapsulasi & Access Modifier",
    "type": "mcq",
    "questionHtml": "Pada aplikasi dompet digital, atribut <code>saldo</code> pada class <code>Dompet</code> tidak boleh diubah secara langsung dari luar class menjadi nilai negatif (misalnya <code>dompet1.saldo = -500000</code>). Penerapan prinsip enkapsulasi yang paling tepat untuk mengatasi masalah tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menetapkan atribut saldo sebagai private dan menyediakan method getter serta setter/mutator yang memvalidasi agar nilai transaksi tidak negatif."
      },
      {
        "key": "B",
        "text": "Menetapkan atribut saldo sebagai variabel global publik tanpa method apa pun."
      },
      {
        "key": "C",
        "text": "Menghapus atribut saldo dari class Dompet dan menyimpannya di judul jendela browser."
      },
      {
        "key": "D",
        "text": "Mengubah tipe data saldo menjadi teks biasa agar tidak bisa dikurangi."
      },
      {
        "key": "E",
        "text": "Mendeklarasikan ulang class Dompet setiap kali pengguna menekan tombol layar."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OOP: ENKAPSULASI SALDO REKENING",
      "latex": "\\text{Attribute: } -\\text{saldo} \\;(\\text{private}) \\quad \\mid \\quad +\\text{setSaldo}(x): \\; \\text{if } x \\ge 0 \\implies \\text{saldo} = x",
      "legend": "• Enkapsulasi menyembunyikan representasi internal objek dari akses langsung luar.<br>• Mutator/setter mengontrol perubahan data melalui validasi bisnis logis."
    },
    "hints": {
      "concept": "Enkapsulasi menyembunyikan state internal objek dengan modifier private dan hanya mengizinkan modifikasi melalui method mutator terproteksi.",
      "execution": "Pilihlah opsi yang menetapkan atribut sebagai private serta menyediakan method getter dan setter bervalidasi."
    },
    "explanation": "Sesuai prinsip dasar Enkapsulasi, atribut saldo harus disembunyikan (dijadikan private) agar tidak bisa dimanipulasi sewenang-wenang dari luar class. Akses terhadap saldo dikontrol melalui method getter (untuk membaca) dan setter (untuk mengubah), di mana setter dapat memvalidasi nilai input agar saldo tidak menjadi negatif. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-02",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Access Modifier (Protected Visibility)",
    "type": "mcq",
    "questionHtml": "Berdasarkan standar visibilitas <em>access modifier</em> dalam pemrograman berorientasi objek, atribut atau method yang ditetapkan sebagai <strong>protected</strong> (dilambangkan dengan tanda tagar <code>#</code> pada diagram kelas UML) memiliki ruang lingkup akses yang …",
    "options": [
      {
        "key": "A",
        "text": "Hanya dapat diakses oleh class itu sendiri dan class turunannya (subclass)."
      },
      {
        "key": "B",
        "text": "Dapat diakses secara bebas tanpa batasan oleh file kode program mana pun di seluruh dunia."
      },
      {
        "key": "C",
        "text": "Hanya dapat diakses oleh fungsi di luar class yang tidak memiliki izin keamanan."
      },
      {
        "key": "D",
        "text": "Otomatis terkunci secara permanen dan tidak dapat dibaca oleh objek apa pun."
      },
      {
        "key": "E",
        "text": "Hanya dapat dibuka saat komputer tidak terhubung ke jaringan internet."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "UML ACCESS MODIFIERS VISIBILITY",
      "latex": "\\begin{aligned} + & \\text{ : Public (Seluruh lingkup)} \\\\ \\# & \\text{ : Protected (Class itu sendiri \\& Subclass)} \\\\ - & \\text{ : Private (Hanya internal class)} \\end{aligned}",
      "legend": "• Protected (#): Memberikan visibilitas khusus pada hierarki pewarisan (inheritance) tanpa mengeksposnya ke publik umum."
    },
    "hints": {
      "concept": "Modifier protected dirancang khusus untuk mendukung mekanisme pewarisan (inheritance).",
      "execution": "Pilihlah cakupan yang mengizinkan akses bagi class itu sendiri dan class-class turunannya (subclass)."
    },
    "explanation": "Access modifier protected (#) membatasi aksesibilitas elemen kelas sehingga hanya dapat diakses oleh metode di dalam kelas itu sendiri serta kelas-kelas turunannya (subclasses) melalui hierarki pewarisan (inheritance). Publik umum di luar hierarki tidak dapat mengakses anggota protected tersebut. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-03",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Pewarisan (Inheritance) & super() Constructor",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Python relasi inheritance berikut:<br><pre><code class=\"language-python\">class Kendaraan:\n    def __init__(self, merk, tahun):\n        self.merk = merk\n        self.tahun = tahun\n\nclass Mobil(Kendaraan):\n    def __init__(self, merk, tahun, jumlah_pintu):\n        super().__init__(merk, tahun)\n        self.jumlah_pintu = jumlah_pintu</code></pre>Peran utama pemanggilan fungsi <code>super().__init__(merk, tahun)</code> di dalam constructor class <code>Mobil</code> adalah …",
    "options": [
      {
        "key": "A",
        "text": "Mengeksekusi inisialisasi atribut merk dan tahun yang didefinisikan pada constructor superclass Kendaraan."
      },
      {
        "key": "B",
        "text": "Menghapus seluruh memori objek Kendaraan dari sistem komputer."
      },
      {
        "key": "C",
        "text": "Mengubah class Mobil menjadi class yang tidak memiliki method apa pun."
      },
      {
        "key": "D",
        "text": "Menghentikan jalannya program secara otomatis karena terjadi duplikasi atribut."
      },
      {
        "key": "E",
        "text": "Mengonversi seluruh variabel string menjadi angka biner."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OOP: SUPERCLASS INITIALIZATION",
      "latex": "\\texttt{super().\\_\\_init\\_\\_(args)} \\implies \\text{Panggil Constructor SuperClass untuk inisialisasi atribut warisan}",
      "legend": "• Menjamin konsistensi atribut dasar superclass sebelum subclass menambahkan atribut spesifiknya sendiri (`self.jumlah_pintu`)."
    },
    "hints": {
      "concept": "Fungsi super() merujuk pada superclass (kelas induk). Pemanggilan super().__init__() menjalankan konstruktor kelas induk.",
      "execution": "Pilihlah jawaban yang menjelaskan eksekusi inisialisasi atribut merk dan tahun pada superclass Kendaraan."
    },
    "explanation": "Pemanggilan `super().__init__(merk, tahun)` berfungsi memanggil konstruktor dari superclass (`Kendaraan`) untuk menginisialisasi atribut `merk` dan `tahun` yang didefinisikan pada kelas induk tersebut. Hal ini mencegah duplikasi kode dan memastikan objek anak (`Mobil`) memiliki state dasar yang lengkap sesuai rancangan kelas induknya. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-04",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Polymorphism & Method Overriding",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi pengolah gambar memiliki class induk <code>BangunDatar</code> dengan method <code>hitung_luas()</code>. Class turunan <code>Lingkaran</code> dan <code>PersegiPanjang</code> masing-masing mendefinisikan kembali method <code>hitung_luas()</code> dengan rumus perhitungan matematika yang berbeda. Konsep OOP yang diterapkan saat kedua class turunan tersebut mendefinisikan kembali method dengan nama yang sama persis untuk menghasilkan perilaku spesifik adalah …",
    "options": [
      {
        "key": "A",
        "text": "Polymorphism melalui mekanisme method overriding"
      },
      {
        "key": "B",
        "text": "Serialisasi data melalui format JSON"
      },
      {
        "key": "C",
        "text": "Dekomposisi algoritma sekuensial"
      },
      {
        "key": "D",
        "text": "Kompilasi kode program menjadi bytecode assembly"
      },
      {
        "key": "E",
        "text": "Instansiasi variabel global di luar memori"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OOP: POLYMORPHISM VIA OVERRIDING",
      "latex": "\\text{Interface: } \\text{hitung\\_luas}() \\implies \\begin{cases} \\pi \\cdot r^2 & \\text{pada Lingkaran} \\\\ p \\cdot l & \\text{pada PersegiPanjang} \\end{cases}",
      "legend": "• Satu nama antarmuka method yang sama memiliki banyak bentuk implementasi spesifik pada masing-masing kelas turunan."
    },
    "hints": {
      "concept": "Satu nama method yang sama tetapi memiliki perilaku implementasi berbeda pada berbagai kelas turunan merupakan inti dari konsep polymorphism (banyak bentuk).",
      "execution": "Pilihlah Polymorphism melalui mekanisme method overriding."
    },
    "explanation": "Penerapan di mana class turunan mendefinisikan ulang method yang ada pada class induknya dengan nama dan parameter yang sama persis namun logika berbeda merupakan wujud nyata dari konsep Polymorphism melalui mekanisme Method Overriding. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-05",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Output Polymorphism",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program pengujian polymorphism berikut:<br><pre><code class=\"language-python\">class BangunDatar:\n    def hitung_luas(self):\n        return 0\n\nclass Lingkaran(BangunDatar):\n    def __init__(self, r):\n        self.r = r\n    def hitung_luas(self):\n        return (22 / 7) * self.r * self.r\n\nclass Persegi(BangunDatar):\n    def __init__(self, sisi):\n        self.sisi = sisi\n    def hitung_luas(self):\n        return self.sisi * self.sisi\n\nclass PersegiPanjang(BangunDatar):\n    def __init__(self, p, l):\n        self.p = p\n        self.l = l\n    def hitung_luas(self):\n        return self.p * self.l\n\ndaftar_bentuk = [Lingkaran(7), Persegi(5), PersegiPanjang(4, 6)]\nfor bentuk in daftar_bentuk:\n    print(bentuk.hitung_luas())</code></pre>Output berurutan yang dihasilkan dari eksekusi loop program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "154.0 lalu 25 lalu 24"
      },
      {
        "key": "B",
        "text": "0 lalu 0 lalu 0"
      },
      {
        "key": "C",
        "text": "49.0 lalu 20 lalu 10"
      },
      {
        "key": "D",
        "text": "154.0 lalu 20 lalu 24"
      },
      {
        "key": "E",
        "text": "Error: List tidak dapat menampung objek berbeda class"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "TRACE POLYMORPHIC DISPATCH",
      "latex": "\\begin{aligned} 1.\\; \\text{Lingkaran}(r=7) & : \\frac{22}{7} \\times 7 \\times 7 = 154.0 \\\\ 2.\\; \\text{Persegi}(s=5) & : 5 \\times 5 = 25 \\\\ 3.\\; \\text{PersegiPanjang}(p=4, l=6) & : 4 \\times 6 = 24 \\end{aligned}",
      "legend": "• Tiap elemen daftar memanggil implementasi method `hitung_luas()` miliknya sendiri secara dinamis saat runtime."
    },
    "hints": {
      "concept": "Lakukan perhitungan matematika untuk masing-masing objek: Lingkaran r=7, Persegi s=5, PersegiPanjang 4x6.",
      "execution": "(22/7)*7*7 = 154.0. 5*5 = 25. 4*6 = 24."
    },
    "explanation": "Pada iterasi pertama, `Lingkaran(7)` dieksekusi: (22/7) * 7 * 7 = 154.0. Pada iterasi kedua, `Persegi(5)` dieksekusi: 5 * 5 = 25. Pada iterasi ketiga, `PersegiPanjang(4, 6)` dieksekusi: 4 * 6 = 24. Urutan output yang dicetak adalah 154.0, 25, dan 24. Jawaban: A.",
    "isDiagnostic": False
  },

  # --- SOAL 06 S.D. 25: 20 SOAL HOTS 5 ELEMEN RESMI PUSMENDIK ---
  {
    "id": "rpl-sim-06",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Manajemen Proyek Agile/Scrum & Velocity",
    "type": "mcq",
    "questionHtml": "Sebuah tim Scrum memiliki data historis kecepatan penyelesaian (<em>Velocity</em>) selama 4 Sprint berturut-turut: 30, 34, 32, dan 32 Story Points (rata-rata = 32 SP per Sprint). Product Backlog saat ini menyisakan 160 Story Points total fitur yang harus diselesaikan untuk peluncuran rilis akbar. Berdasarkan prinsip empiris Scrum, estimasi jumlah Sprint yang dibutuhkan tim untuk menyelesaikan rilis tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "5 Sprint"
      },
      {
        "key": "B",
        "text": "1 Sprint"
      },
      {
        "key": "C",
        "text": "10 Sprint"
      },
      {
        "key": "D",
        "text": "2 Sprint"
      },
      {
        "key": "E",
        "text": "16 Sprint"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "AGILE RELEASE PLANNING FORMULA",
      "latex": "\\text{Estimated Sprints} = \\left\\lceil \\frac{\\text{Total Backlog Points}}{\\text{Average Velocity}} \\right\\rceil = \\frac{160}{32} = 5 \\text{ Sprints}",
      "legend": "• Velocity rata-rata: (30 + 34 + 32 + 32) / 4 = 32 SP/Sprint.<br>• Kapasitas empiris terbukti dapat diandalkan untuk proyeksi jadwal rilis."
    },
    "hints": {
      "concept": "Hitung rata-rata velocity lalu bagi total story point backlog dengan rata-rata velocity tersebut.",
      "execution": "160 / 32 = 5."
    },
    "explanation": "Rata-rata kecepatan penyelesaian (Velocity) tim adalah (30 + 34 + 32 + 32) / 4 = 32 Story Points per Sprint. Untuk menyelesaikan sisa backlog sebesar 160 Story Points, perkiraan jumlah Sprint yang dibutuhkan adalah 160 / 32 = 5 Sprint. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-07",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "HAKI & Perlindungan Program Komputer",
    "type": "mcq",
    "questionHtml": "Di Indonesia, perlindungan hukum Hak Kekayaan Intelektual (HAKI) untuk karya program komputer (perangkat lunak) secara yuridis diatur dalam <strong>Undang-Undang Republik Indonesia Nomor 28 Tahun 2014</strong> tentang …",
    "options": [
      {
        "key": "A",
        "text": "Hak Cipta (Copyright)"
      },
      {
        "key": "B",
        "text": "Paten Sederhana Perangkat Keras"
      },
      {
        "key": "C",
        "text": "Desain Tata Letak Sirkuit Terpadu"
      },
      {
        "key": "D",
        "text": "Merek dan Indikasi Geografis"
      },
      {
        "key": "E",
        "text": "Rahasia Dagang Pertanian"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "HAKI: SOFTWARE LEGAL REGIME",
      "latex": "\\text{Source Code \\& Binary} \\in \\text{UU No. 28/2014 tentang Hak Cipta (Pasal 40 ayat 1 huruf s)}",
      "legend": "• Program Komputer dilindungi sebagai ciptaan dalam rezim Hak Cipta (otomatis timbul saat karya diwujudkan/deklaratif)."
    },
    "hints": {
      "concept": "Kode program komputer dan aplikasinya dilindungi dalam rezim hukum Hak Cipta, bukan paten industri.",
      "execution": "Pilihlah Hak Cipta (Copyright)."
    },
    "explanation": "Di bawah hukum Indonesia (UU No. 28 Tahun 2014 Pasal 40 ayat 1 huruf s), Program Komputer secara tegas diakui dan dilindungi sebagai salah satu ciptaan yang dilindungi dalam rezim Hak Cipta. Hak cipta timbul secara deklaratif seketika ciptaan tersebut diwujudkan dalam bentuk nyata (kode sumber). Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-08",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Technopreneurship: Validasi Pasar & Pivot",
    "type": "mcq",
    "questionHtml": "Sebuah startup software meluncurkan aplikasi pencatatan keuangan untuk warung kelontong. Setelah 3 bulan, metrik retensi menunjukkan pengguna hanya membuka aplikasi sekali lalu menghapusnya. Hasil wawancara mendalam mendapati bahwa pemilik warung merasa repot mengetik data di layar sentuh, tetapi sangat antusias bila pencatatan dilakukan cukup dengan memotret bon/struk belanja menggunakan kamera. Perubahan strategi bisnis dan produk secara terarah berdasarkan pembelajaran tervalidasi ini dalam metodologi Lean Startup disebut …",
    "options": [
      {
        "key": "A",
        "text": "Pivot"
      },
      {
        "key": "B",
        "text": "Bankruptcy"
      },
      {
        "key": "C",
        "text": "Perseverance buta"
      },
      {
        "key": "D",
        "text": "Downsizing paksa"
      },
      {
        "key": "E",
        "text": "Deprecate server"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LEAN STARTUP: THE PIVOT CONCEPT",
      "latex": "\\text{Validated Learning (Feedback)} \\implies \\text{Pivot: Structured course correction to test a new hypothesis}",
      "legend": "• Pivot bukan kegagalan total, melainkan adaptasi cerdas model produk untuk mencapai Product-Market Fit."
    },
    "hints": {
      "concept": "Istilah perubahan haluan strategi produk berdasarkan umpan balik nyata pengguna untuk menemukan kecocokan pasar (product-market fit).",
      "execution": "Pilihlah istilah 'Pivot'."
    },
    "explanation": "Dalam technopreneurship dan Lean Startup (Eric Ries), 'Pivot' adalah koreksi arah terstruktur yang dirancang untuk menguji hipotesis baru mengenai produk atau model bisnis berdasarkan pembelajaran tervalidasi (validated learning) dari respon nyata pengguna di pasar. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-09",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Budaya Mutu: Peer Code Review",
    "type": "mcq",
    "questionHtml": "Dalam tim rekayasa perangkat lunak profesional, setiap baris kode baru dilarang langsung digabungkan (merge) ke cabang utama sebelum melalui proses <strong>Peer Code Review</strong> oleh sesama rekan pengembang. Manfaat utama praktik ini dari sudut pandang pemeliharaan perangkat lunak jangka panjang adalah …",
    "options": [
      {
        "key": "A",
        "text": "Mendeteksi kelemahan logika, celah keamanan, dan 'code smell' sedini mungkin, sekaligus meratakan transfer pengetahuan (knowledge sharing) antar-anggota tim."
      },
      {
        "key": "B",
        "text": "Membuktikan siapa programmer yang paling hebat dan mempermalukan programmer pemula."
      },
      {
        "key": "C",
        "text": "Memperpanjang birokrasi agar rilis aplikasi tertunda selama berbulan-bulan."
      },
      {
        "key": "D",
        "text": "Menggantikan seluruh proses kompilasi kode pada sistem operasi."
      },
      {
        "key": "E",
        "text": "Menghapus kebutuhan pengujian unit test dan dokumentasi antarmuka."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ENGINEERING EXCELLENCE: CODE REVIEW",
      "latex": "\\text{Peer Review} \\implies \\text{Defect Detection} \\uparrow \\; + \\; \\text{Shared Codebase Ownership} \\uparrow \\; + \\; \\text{Bus Factor} \\downarrow",
      "legend": "• Mengurangi ketergantungan pada satu orang (Bus Factor) dan memastikan kode mematuhi panduan gaya (style guide) tim."
    },
    "hints": {
      "concept": "Code review bertujuan untuk meningkatkan kualitas kode, mencegah bug lolos ke produksi, dan memfasilitasi pertukaran ilmu.",
      "execution": "Pilihlah opsi yang menyebutkan deteksi kelemahan logika, celah keamanan, dan knowledge sharing."
    },
    "explanation": "Peer Code Review adalah praktik standar industri di mana sesama pengembang memeriksa kode rekan kerja sebelum digabung. Praktik ini efektif mendeteksi cacat logika, potensi celah keamanan (seperti SQL injection), menjaga konsistensi gaya kode, serta menyebarkan pemahaman arsitektur sistem secara merata di dalam tim (shared ownership). Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-10",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Keamanan Kredensial & Secrets Management",
    "type": "mcq",
    "questionHtml": "Di server produksi, penyimpanan kata sandi basis data dan token rahasia secara aman (<em>Hardening Secrets</em>) sebaiknya tidak ditulis langsung (<em>hardcoded</em>) di dalam kode sumber aplikasi. Praktik terbaik standar industri untuk menyuplai rahasia tersebut ke aplikasi backend yang berjalan di dalam container adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menginjeksi kredensial melalui Environment Variables (variabel lingkungan sistem) yang disuntikkan secara dinamis saat runtime dari Secret Vault atau orkestrator."
      },
      {
        "key": "B",
        "text": "Menulis kata sandi di baris komentar pertama file index.html."
      },
      {
        "key": "C",
        "text": "Menempelkan catatan kertas berisi kata sandi di atas casing monitor server."
      },
      {
        "key": "D",
        "text": "Menyimpan kata sandi di dalam gambar PNG logo perusahaan."
      },
      {
        "key": "E",
        "text": "Mengirimkan kata sandi melalui pesan SMS terbuka ke seluruh staf setiap 5 menit."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "THE TWELVE-FACTOR APP: CONFIG IN ENVIRONMENT",
      "latex": "\\text{Factor III (Config)}: \\quad \\text{Store config in the environment } (\\text{Strict separation of config from code})",
      "legend": "• Kode program dapat di-open source kapan saja tanpa khawatir membocorkan password produksi."
    },
    "hints": {
      "concept": "Prinsip Twelve-Factor App menyatakan konfigurasi rahasia harus disimpan terpisah dari kode sumber, menggunakan Environment Variables.",
      "execution": "Pilihlah injeksi melalui Environment Variables saat runtime."
    },
    "explanation": "Berdasarkan prinsip 'The Twelve-Factor App', konfigurasi yang bervariasi antar-lingkungan (khususnya kredensial sensitif) tidak boleh di-hardcode di dalam kode program. Praktik terbaik adalah menyuntikkannya sebagai Environment Variables saat aplikasi dijalankan (runtime) dari sistem manajemen rahasia terenkripsi (seperti HashiCorp Vault atau Docker/K8s Secrets). Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-11",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Ketahanan Data & Prosedur Backup 3-2-1",
    "type": "mcq",
    "questionHtml": "Sebuah studio gim mengalami bencana kebakaran pada gedung kantor utama tempat server penyimpanan data lokal berada. Untungnya, studio tersebut menerapkan strategi <strong>Backup 3-2-1</strong> dengan disiplin. Bagian dari strategi 3-2-1 manakah yang menjamin seluruh aset kode sumber gim mereka selamat dan dapat dipulihkan secara penuh?",
    "options": [
      {
        "key": "A",
        "text": "Aturan angka '1', yaitu menyimpan minimal 1 salinan cadangan di lokasi fisik terpisah / off-site (misal Cloud Storage terenkripsi)."
      },
      {
        "key": "B",
        "text": "Aturan angka '3', yaitu mencetak kode sumber di 3 lembar kertas HVS."
      },
      {
        "key": "C",
        "text": "Aturan angka '2', yaitu menyalin data ke 2 folder berbeda di dalam laptop yang ikut terbakar."
      },
      {
        "key": "D",
        "text": "Kabel listrik komputer yang terbuat dari bahan tembaga tebal."
      },
      {
        "key": "E",
        "text": "Sertifikat garansi monitor kantor yang masih aktif."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OFF-SITE DATA SURVIVABILITY",
      "latex": "\\text{Disaster at Site A } (\\text{Fire/Theft}) \\land 1\\text{ Off-site Copy at Site B (Cloud)} \\implies \\text{Full Data Recovery Possible}",
      "legend": "• Salinan di lokasi fisik berbeda mengeliminasi risiko kegagalan satu lokasi (Single Point of Facility Failure)."
    },
    "hints": {
      "concept": "Angka '1' dalam aturan 3-2-1 mewakili 1 salinan di lokasi terpisah (off-site/cloud), yang melindungi dari kehancuran fisik di lokasi lokal.",
      "execution": "Pilihlah aturan angka '1' (off-site / cloud)."
    },
    "explanation": "Dalam aturan backup 3-2-1, angka '1' menegaskan kewajiban menyimpan minimal 1 salinan data di luar lokasi fisik utama (off-site atau cloud). Jika kantor utama mengalami bencana kehancuran total (seperti kebakaran atau banjir), salinan off-site ini menjadi penjamin tunggal bahwa data perusahaan dapat dipulihkan secara utuh. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-12",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "K3LH & Ergonomi Penglihatan (Aturan 20-20-20)",
    "type": "mcq",
    "questionHtml": "Dalam panduan K3LH industri perangkat lunak, pencegahan <em>Computer Vision Syndrome (CVS)</em> yang menyebabkan mata kering, penglihatan kabur, dan sakit kepala pada programmer diatur melalui pedoman <strong>20-20-20</strong>. Penerapan pedoman 20-20-20 yang benar adalah …",
    "options": [
      {
        "key": "A",
        "text": "Setiap 20 menit menatap layar, istirahatkan mata selama 20 detik dengan melihat objek yang berjarak minimal 20 kaki (sekitar 6 meter)."
      },
      {
        "key": "B",
        "text": "Bekerja terus menerus selama 20 jam, tidur selama 20 menit, dan mengonsumsi 20 gelas kopi."
      },
      {
        "key": "C",
        "text": "Menyetel kecerahan monitor pada angka 20% dengan jarak wajah 20 milimeter dari layar."
      },
      {
        "key": "D",
        "text": "Mengedipkan mata sebanyak 20 kali dalam durasi 20 jam kerja."
      },
      {
        "key": "E",
        "text": "Membeli monitor baru setiap 20 hari kerja selama 20 tahun."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "K3LH VISION PROTECTION: RULE OF 20-20-20",
      "latex": "20\\text{ min (Screen)} \\to 20\\text{ sec (Break)} \\to 20\\text{ feet / 6 meters (Focal Relaxation)}",
      "legend": "• Merelaksasi otot siliaris mata yang tegang akibat terus-menerus memfokuskan pandangan pada jarak dekat."
    },
    "hints": {
      "concept": "Aturan ini dibuat oleh American Optometric Association: 20 menit bekerja, 20 detik istirahat, pandang sejauh 20 kaki (6 meter).",
      "execution": "Pilihlah opsi yang merinci 20 menit, 20 detik, dan 20 kaki / 6 meter."
    },
    "explanation": "Aturan 20-20-20 adalah pedoman ergonomi visual standar: setiap 20 menit bekerja di depan layar komputer, istirahatkan mata selama minimal 20 detik dengan mengalihkan fokus pandangan ke objek berjarak setidaknya 20 kaki (sekitar 6 meter) untuk merelaksasi otot fokus mata dan memicu refleks berkedip alami. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-13",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Alur Kerja Git: Percabangan Git Flow",
    "type": "mcq",
    "questionHtml": "Dalam model percabangan <strong>Git Flow</strong>, cabang (branch) khusus yang dibuat langsung dari cabang <code>main</code> (produksi) untuk segera memperbaiki cacat kritis (bug) yang sedang merugikan pengguna di server langsung, lalu segera digabungkan kembali ke <code>main</code> dan <code>develop</code>, disebut …",
    "options": [
      {
        "key": "A",
        "text": "Hotfix Branch"
      },
      {
        "key": "B",
        "text": "Feature Branch"
      },
      {
        "key": "C",
        "text": "Experimental Branch"
      },
      {
        "key": "D",
        "text": "Archive Branch"
      },
      {
        "key": "E",
        "text": "Staging Backup Branch"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GIT FLOW: HOTFIX BRANCH LIFECYCLE",
      "latex": "\\texttt{main} \\xrightarrow{\\text{branch}} \\texttt{hotfix/v1.0.1} \\xrightarrow{\\text{patch}} \\begin{cases} \\text{merge into } \\texttt{main} \\\\ \\text{merge into } \\texttt{develop} \\end{cases}",
      "legend": "• Menangani insiden produksi darurat tanpa harus menunggu fitur-fitur baru di cabang `develop` selesai."
    },
    "hints": {
      "concept": "Cabang darurat untuk perbaikan cepat langsung dari produksi dinamakan 'hotfix'.",
      "execution": "Pilihlah 'Hotfix Branch'."
    },
    "explanation": "Dalam arsitektur Git Flow, cabang Hotfix dibuat langsung dari cabang produksi `main` untuk menangani insiden kritis mendesak yang ditemukan di lingkungan produksi. Setelah perbaikan selesai dan diverifikasi, cabang hotfix segera digabungkan (merge) ke `main` (dengan tagging rilis baru) serta digabungkan ke `develop` agar perbaikan tersebut tidak hilang pada rilis berikutnya. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-14",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Perhitungan Subnetting IPv4 (/28)",
    "type": "mcq",
    "questionHtml": "Laboratorium komputer RPL membutuhkan subnetting untuk menghubungkan 12 komputer workstation ke jaringan sekolah. Administrator mengalokasikan subnet:<div class=\"net-spec-box\"><div class=\"net-spec-title\"><svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\"><circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z\"/></svg>Alokasi Subnet Workstation Lab</div><div class=\"net-spec-list\"><div class=\"net-spec-item\">🌐 <strong>Subnet Alokasi:</strong> <span class=\"net-ip-badge\">172.16.5.0/28</span> (Kebutuhan: 12 workstation)</div></div></div>Berapakah jumlah total host valid yang dapat digunakan pada subnet tersebut, serta berapakah nilai Subnet Mask-nya?",
    "options": [
      {
        "key": "A",
        "text": "14 host valid dan Subnet Mask 255.255.255.240"
      },
      {
        "key": "B",
        "text": "16 host valid dan Subnet Mask 255.255.255.248"
      },
      {
        "key": "C",
        "text": "30 host valid dan Subnet Mask 255.255.255.224"
      },
      {
        "key": "D",
        "text": "6 host valid dan Subnet Mask 255.255.255.252"
      },
      {
        "key": "E",
        "text": "12 host valid dan Subnet Mask 255.255.255.192"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IPV4 SUBNETTING: PREFIX /28",
      "latex": "H = 32 - 28 = 4 \\implies \\text{Total IP} = 2^4 = 16, \\quad \\text{Host Valid} = 16 - 2 = 14",
      "legend": "• Subnet Mask oktet terakhir: $128 + 64 + 32 + 16 = 240$.<br>• Subnet Mask lengkap: 255.255.255.240."
    },
    "hints": {
      "concept": "Prefix /28 menyisakan 4 bit host (32 - 28 = 4). Total IP = 2^4 = 16. Host valid = 16 - 2 = 14. Oktet terakhir: 11110000 = 240.",
      "execution": "Pilihlah 14 host valid dan subnet mask 255.255.255.240."
    },
    "explanation": "Pada notasi CIDR /28, jumlah bit untuk host adalah 32 - 28 = 4 bit. Jumlah total alamat IP yang tersedia adalah 2^4 = 16. Mengurangi 1 network address dan 1 broadcast address, diperoleh 14 IP host valid (cukup untuk 12 workstation). Subnet mask oktet ke-4 memiliki 4 bit biner satu (11110000 = 128+64+32+16 = 240), sehingga subnet mask lengkapnya adalah 255.255.255.240. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-15",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Sistem Operasi Linux: Kepemilikan & Hak Akses Berkas",
    "type": "mcq",
    "questionHtml": "Pada server Linux, file konfigurasi backend <code>config.json</code> dimiliki oleh user <code>root</code> dan group <code>root</code> dengan izin <code>-rw-------</code>. Akibatnya, server web yang berjalan dengan pengguna <code>www-data</code> gagal membaca file tersebut dan memicu error <em>Permission Denied</em>. Perintah Linux yang paling tepat untuk mengubah kepemilikan file tersebut menjadi milik <code>www-data</code> adalah …",
    "options": [
      {
        "key": "A",
        "text": "`sudo chown www-data:www-data config.json`"
      },
      {
        "key": "B",
        "text": "`sudo chmod 000 config.json`"
      },
      {
        "key": "C",
        "text": "`sudo rm -f config.json`"
      },
      {
        "key": "D",
        "text": "`sudo ifconfig www-data up`"
      },
      {
        "key": "E",
        "text": "`sudo reboot now`"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LINUX FILE OWNERSHIP: CHOWN COMMAND",
      "latex": "\\texttt{chown [user]:[group] [target\\_file]} \\implies \\text{Transfer file ownership to specified service account}",
      "legend": "• `chown`: Change Owner.<br>• `chmod`: Change Mode (Permissions: rwx)."
    },
    "hints": {
      "concept": "Untuk mengubah pemilik (owner) dan grup file di Linux digunakan perintah `chown` (change owner), bukan chmod.",
      "execution": "Pilihlah perintah `sudo chown www-data:www-data config.json`."
    },
    "explanation": "Perintah `chown` (change owner) adalah utilitas Linux untuk mengganti kepemilikan pengguna dan grup pada suatu berkas. Dengan menjalankan `sudo chown www-data:www-data config.json`, kepemilikan berkas diserahkan kepada akun layanan web server (`www-data`), sehingga aplikasi yang berjalan di bawah akun tersebut dapat membaca konfigurasi tanpa hambatan izin akses. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-16",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Arsitektur TCP/IP: DNS CNAME Record",
    "type": "mcq",
    "questionHtml": "Sebuah domain web <code>portal.smkhebat.sch.id</code> dikonfigurasi sebagai <strong>alias</strong> (nama samaran) yang merujuk pada domain utama <code>utama.smkhebat.sch.id</code>, sehingga jika alamat IP server utama berubah, administrator tidak perlu mengupdate banyak catatan IP secara manual. Catatan DNS yang digunakan untuk membuat alias tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "CNAME (Canonical Name) Record"
      },
      {
        "key": "B",
        "text": "A (Address) Record"
      },
      {
        "key": "C",
        "text": "PTR (Pointer) Record"
      },
      {
        "key": "D",
        "text": "SOA (Start of Authority) Record"
      },
      {
        "key": "E",
        "text": "NS (Name Server) Record"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DNS ALIASING MECHANISM",
      "latex": "\\text{portal.smkhebat.sch.id} \\xrightarrow{\\text{CNAME}} \\text{utama.smkhebat.sch.id} \\xrightarrow{\\text{A Record}} 103.10.5.2",
      "legend": "• CNAME memetakan satu nama domain (alias) ke nama kanonikal lain.<br>• Perubahan IP di A record domain kanonikal otomatis berlaku untuk seluruh domain aliasnya."
    },
    "hints": {
      "concept": "Catatan DNS untuk menetapkan alias nama domain ke nama domain lain disebut Canonical Name (CNAME).",
      "execution": "Pilihlah CNAME Record."
    },
    "explanation": "CNAME Record (Canonical Name Record) adalah tipe catatan DNS yang memetakan sebuah nama alias (alias domain) ke nama domain yang sebenarnya (canonical domain). Keuntungan CNAME adalah jika alamat IP server berubah, administrator cukup memperbarui satu A Record milik domain kanonikal saja. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-17",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Protokol HTTP: Status Code 401 vs 403",
    "type": "mcq",
    "questionHtml": "Dalam pengujian keamanan REST API, seorang pengguna yang belum login mencoba mengakses halaman data rahasia dan menerima respons kode status HTTP <code>401 Unauthorized</code>. Sementara itu, pengguna lain yang sudah berhasil login sebagai 'Siswa' mencoba menghapus akun pengguna lain dan menerima respons kode status HTTP <code>403 Forbidden</code>. Perbedaan semantik teknis yang benar antara kode 401 dan 403 adalah …",
    "options": [
      {
        "key": "A",
        "text": "401 menandakan kegagalan Otentikasi (identitas pengguna belum terverifikasi/belum login), sedangkan 403 menandakan kegagalan Otorisasi (identitas terverifikasi tetapi tidak memiliki hak akses/izin atas aksi tersebut)."
      },
      {
        "key": "B",
        "text": "401 menandakan kabel jaringan putus, sedangkan 403 menandakan komputer server meledak."
      },
      {
        "key": "C",
        "text": "401 untuk browser Chrome, sedangkan 403 khusus untuk browser Firefox."
      },
      {
        "key": "D",
        "text": "Kedua kode memiliki arti yang identik dan hanya perbedaan angka keberuntungan."
      },
      {
        "key": "E",
        "text": "401 menandakan server sedang memproses data, sedangkan 403 menandakan proses selesai sukses."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "HTTP STATUS CODES: AUTHENTICATION VS AUTHORIZATION",
      "latex": "\\begin{aligned} \\text{HTTP 401} & : \\text{Unauthenticated (Who are you? Missing valid credentials)} \\\\ \\text{HTTP 403} & : \\text{Forbidden / Unauthorized (I know who you are, but you cannot access this)} \\end{aligned}",
      "legend": "• 401: Perlu login/sertakan token header.<br>• 403: Identitas sah, namun peran/role tidak mencukupi (Insufficient Permissions)."
    },
    "hints": {
      "concept": "401 = Otentikasi (siapa kamu?). 403 = Otorisasi/Hak Akses (kamu boleh melakukan ini atau tidak?).",
      "execution": "Pilihlah perbedaan antara Authentication (401) dan Authorization (403)."
    },
    "explanation": "Dalam spesifikasi RFC HTTP: Kode 401 Unauthorized secara teknis berarti unauthenticated (klien belum menyertakan kredensial otentikasi yang valid). Kode 403 Forbidden berarti server mengenali siapa klien tersebut (sudah login), namun aturan hak akses (Role-Based Access Control) melarang klien tersebut mengeksekusi sumber daya atau aksi tersebut. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-18",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Trace Logika Perulangan & Percabangan",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program filter data berikut:<br><pre><code class=\"language-python\">angka = [12, 17, 24, 33, 40, 51]\nhasil = []\nfor a in angka:\n    if a % 2 == 0 and a > 20:\n        hasil.append(a)\nprint(hasil)</code></pre>Output yang dicetak oleh program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "[24, 40]"
      },
      {
        "key": "B",
        "text": "[12, 24, 40]"
      },
      {
        "key": "C",
        "text": "[17, 33, 51]"
      },
      {
        "key": "D",
        "text": "[24]"
      },
      {
        "key": "E",
        "text": "[]"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LOGICAL PREDICATE TRACING",
      "latex": "P(a) = (a \\pmod 2 = 0) \\land (a > 20) \\implies \\text{Bilangan Genap yang Lebih Besar dari 20}",
      "legend": "• 12: Genap, tapi 12 tidak > 20 (False)<br>• 17: Ganjil (False)<br>• 24: Genap dan > 20 (True -> append)<br>• 33: Ganjil (False)<br>• 40: Genap dan > 20 (True -> append)<br>• 51: Ganjil (False)<br>• Hasil akhir: [24, 40]"
    },
    "hints": {
      "concept": "Dua syarat harus terpenuhi sekaligus: bilangan genap (`a % 2 == 0`) DAN lebih besar dari 20 (`a > 20`).",
      "execution": "Periksa: 12 (tidak > 20), 24 (cocok), 40 (cocok). Hasil = [24, 40]."
    },
    "explanation": "Kondisi `a % 2 == 0 and a > 20` memerlukan bilangan tersebut genap sekaligus lebih besar dari 20. Dari list `[12, 17, 24, 33, 40, 51]`, angka 12 ditolak karena tidak lebih besar dari 20. Angka 17, 33, dan 51 ditolak karena ganjil. Hanya angka 24 dan 40 yang memenuhi kedua syarat tersebut, sehingga dicetak `[24, 40]`. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-19",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Manipulasi Slicing & Panjang List",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode pemotongan list (slicing) berikut:<br><pre><code class=\"language-python\">bahasa = [\"C++\", \"Java\", \"Python\", \"Go\", \"Rust\"]\npilihan = bahasa[1:4]\nprint(pilihan)</code></pre>Output yang dicetak oleh baris kode di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "['Java', 'Python', 'Go']"
      },
      {
        "key": "B",
        "text": "['C++', 'Java', 'Python']"
      },
      {
        "key": "C",
        "text": "['Java', 'Python', 'Go', 'Rust']"
      },
      {
        "key": "D",
        "text": "['C++', 'Rust']"
      },
      {
        "key": "E",
        "text": "['Python', 'Go']"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "LIST SLICING SEMANTICS",
      "latex": "L[\\text{start}:\\text{stop}] \\implies \\text{Elemen dari indeks } \\text{start} \\text{ inklusif s.d. } \\text{stop}-1 \\text{ eksklusif}",
      "legend": "• Indeks 0: 'C++'<br>• Indeks 1: 'Java'<br>• Indeks 2: 'Python'<br>• Indeks 3: 'Go'<br>• Indeks 4: 'Rust'<br>• Slice [1:4] mengambil indeks 1, 2, dan 3: `['Java', 'Python', 'Go']`."
    },
    "hints": {
      "concept": "Slicing [1:4] mengambil elemen mulai dari indeks 1 sampai dengan sebelum indeks 4 (yaitu indeks 1, 2, dan 3).",
      "execution": "Indeks 1 adalah Java, 2 adalah Python, 3 adalah Go."
    },
    "explanation": "Pada Python, notasi slicing `list[start:stop]` mengambil elemen dimulai dari indeks `start` hingga tepat sebelum indeks `stop` (indeks `stop` bersifat eksklusif). Dengan list `bahasa`, indeks 1 adalah 'Java', indeks 2 adalah 'Python', dan indeks 3 adalah 'Go'. Indeks 4 ('Rust') tidak disertakan. Maka outputnya adalah `['Java', 'Python', 'Go']`. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-20",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Modularisasi Fungsi & Parameter Default",
    "type": "mcq",
    "questionHtml": "Perhatikan fungsi perhitungan harga diskon berikut:<br><pre><code class=\"language-python\">def hitung_diskon(harga, persen=10):\n    return harga - (harga * persen / 100)\n\ntotal1 = hitung_diskon(100000)\ntotal2 = hitung_diskon(100000, 25)\nprint(int(total1), int(total2))</code></pre>Output yang dicetak oleh program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "90000 75000"
      },
      {
        "key": "B",
        "text": "100000 75000"
      },
      {
        "key": "C",
        "text": "90000 100000"
      },
      {
        "key": "D",
        "text": "80000 70000"
      },
      {
        "key": "E",
        "text": "Error: Parameter kedua wajib disertakan"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DEFAULT PARAMETER COMPUTATION",
      "latex": "\\begin{aligned} \\text{total1} & = 100000 - (100000 \\times 10\\%) = 90000 \\\\ \\text{total2} & = 100000 - (100000 \\times 25\\%) = 75000 \\end{aligned}",
      "legend": "• Pemanggilan pertama menggunakan default persen = 10.<br>• Pemanggilan kedua menimpa nilai default dengan persen = 25."
    },
    "hints": {
      "concept": "Jika argumen kedua tidak diberikan, fungsi menggunakan nilai parameter default (persen = 10). Jika diberikan, nilai default ditimpa.",
      "execution": "total1 = 100000 - 10000 = 90000. total2 = 100000 - 25000 = 75000."
    },
    "explanation": "Pada `total1`, pemanggilan `hitung_diskon(100000)` hanya menyertakan 1 argumen, sehingga parameter `persen` menggunakan nilai default 10: 100000 - 10% = 90000. Pada `total2`, pemanggilan `hitung_diskon(100000, 25)` secara eksplisit mengisi nilai `persen = 25`: 100000 - 25% = 75000. Maka dicetak `90000 75000`. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Manipulasi Dictionary: Update & Key Existence",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode manipulasi dictionary berikut:<br><pre><code class=\"language-python\">stok = {\"buku\": 15, \"pensil\": 20}\nstok[\"penghapus\"] = 10\nstok[\"buku\"] += 5\n\nprint(stok.get(\"buku\"), stok.get(\"penggaris\", 0))</code></pre>Output yang dihasilkan dari eksekusi baris terakhir program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "20 0"
      },
      {
        "key": "B",
        "text": "15 None"
      },
      {
        "key": "C",
        "text": "20 None"
      },
      {
        "key": "D",
        "text": "20 Error: KeyError"
      },
      {
        "key": "E",
        "text": "15 0"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DICTIONARY SAFE GET LOOKUP",
      "latex": "D.\\text{get}(k, \\text{default}) = \\begin{cases} D[k] & \\text{if } k \\in D \\\\ \\text{default} & \\text{if } k \\notin D \\end{cases}",
      "legend": "• `stok['buku'] += 5` mengubah nilai buku dari 15 menjadi 20.<br>• `stok.get('penggaris', 0)` mencari kunci yang tidak ada, sehingga mengembalikan nilai cadangan default 0."
    },
    "hints": {
      "concept": "Nilai buku bertambah dari 15 + 5 = 20. Method get('penggaris', 0) mengembalikan fallback default 0 karena kunci 'penggaris' tidak ada.",
      "execution": "Hasil: 20 0."
    },
    "explanation": "Baris `stok['buku'] += 5` memperbarui nilai pada kunci 'buku' dari 15 menjadi 20. Method `stok.get('buku')` mengembalikan 20. Sementara itu, pemanggilan `stok.get('penggaris', 0)` mencari kunci 'penggaris' yang tidak ada di dalam dictionary; karena parameter fallback `0` disertakan, method mengembalikan angka 0 secara aman tanpa melemparkan KeyError. Maka outputnya adalah `20 0`. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-22",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Constructor & Parameter Self",
    "type": "mcq",
    "questionHtml": "Dalam pemrograman Python berbasis objek, parameter pertama pada pendefinisian method di dalam class selalu dinamai <code>self</code> (misalnya <code>def tampil(self):</code>). Fungsi fundamental dari parameter <code>self</code> tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Mewakili referensi memori terhadap instans objek spesifik yang sedang memanggil method tersebut saat runtime."
      },
      {
        "key": "B",
        "text": "Mengunci seluruh file kode sumber agar tidak dapat disalin oleh orang lain."
      },
      {
        "key": "C",
        "text": "Mengonversi seluruh variabel instans menjadi variabel global sistem operasi."
      },
      {
        "key": "D",
        "text": "Mempercepat kecepatan koneksi internet saat aplikasi dijalankan."
      },
      {
        "key": "E",
        "text": "Menghapus objek secara otomatis begitu method selesai dipanggil."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OOP: INSTANCE REFERENCE (SELF)",
      "latex": "o.\\text{method}() \\iff \\text{Class}.\\text{method}(o) \\implies \\texttt{self} \\equiv \\text{Pointer ke objek } o",
      "legend": "• Menjamin setiap objek dapat membaca dan mengubah state atributnya sendiri secara independen dari objek lain."
    },
    "hints": {
      "concept": "Di Python, kata kunci `self` merujuk langsung ke instans objek yang sedang aktif mengeksekusi metode.",
      "execution": "Pilihlah jawaban yang menjelaskan representasi referensi terhadap instans objek yang sedang memanggil method."
    },
    "explanation": "Parameter `self` dalam method Python adalah konvensi eksplisit yang mewakili instans objek itu sendiri. Ketika sebuah objek memanggil method (misal `objek.tampil()`), Python secara otomatis melewatkan objek tersebut sebagai argumen pertama ke parameter `self`, memungkinkan method mengakses dan memanipulasi atribut spesifik milik objek tersebut. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-23",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Enkapsulasi & Name Mangling di Python",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode class berikut:<br><pre><code class=\"language-python\">class Pengguna:\n    def __init__(self, username, pin):\n        self.username = username\n        self.__pin = pin # Private attribute\n\nu = Pengguna(\"admin\", 1234)\nprint(u.__pin)</code></pre>Apa yang terjadi ketika baris terakhir <code>print(u.__pin)</code> dieksekusi?",
    "options": [
      {
        "key": "A",
        "text": "Terjadi AttributeError karena Python menerapkan 'name mangling' yang mengubah nama atribut internal menjadi `_Pengguna__pin`."
      },
      {
        "key": "B",
        "text": "Program mencetak angka 1234 secara normal tanpa hambatan."
      },
      {
        "key": "C",
        "text": "Komputer otomatis ter-restart untuk mengamankan data PIN."
      },
      {
        "key": "D",
        "text": "Mencetak string '***' sebagai sensor otomatis."
      },
      {
        "key": "E",
        "text": "Nilai PIN terhapus permanen dari memori objek."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PYTHON PRIVATE ATTRIBUTE NAME MANGLING",
      "latex": "\\texttt{self.\\_\\_attr} \\xrightarrow{\\text{Name Mangling}} \\texttt{\\_ClassName\\_\\_attr}",
      "legend": "• Akses langsung dari luar (`u.__pin`) gagal melempar AttributeError.<br>• Akses internal masih bisa dibuka lewat `u._Pengguna__pin` (konvensi enkapsulasi)."
    },
    "hints": {
      "concept": "Atribut dengan dua garis bawah di depan (`__pin`) mengalami name mangling di Python, sehingga akses langsung `u.__pin` menimbulkan AttributeError.",
      "execution": "Pilihlah jawaban yang menjelaskan AttributeError akibat mekanisme name mangling."
    },
    "explanation": "Pada Python, atribut yang diawali dengan dua garis bawah (seperti `__pin`) mengalami mekanisme name mangling untuk mencegah konflik penamaan pada subclass dan menyimulasikan atribut private. Secara internal, nama atribut diubah menjadi `_Pengguna__pin`. Upaya mengakses `u.__pin` secara langsung dari luar class akan memicu `AttributeError: 'Pengguna' object has no attribute '__pin'`. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-24",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Inheritance: Pewarisan Atribut & Method",
    "type": "mcq",
    "questionHtml": "Perhatikan hierarki kelas hewan berikut:<br><pre><code class=\"language-python\">class Hewan:\n    def bernapas(self):\n        return \"Menghirup oksigen\"\n\nclass Kucing(Hewan):\n    def bersuara(self):\n        return \"Meow\"\n\nk = Kucing()\nprint(k.bernapas(), \"dan\", k.bersuara())</code></pre>Karakteristik fundamental konsep <strong>Inheritance</strong> yang dibuktikan oleh baris output di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "Class anak (Kucing) mewarisi seluruh kemampuan/method dari class induk (Hewan) sehingga objek k dapat memanggil bernapas() sekaligus method uniknya bersuara()."
      },
      {
        "key": "B",
        "text": "Class Hewan otomatis terhapus saat class Kucing dibuat."
      },
      {
        "key": "C",
        "text": "Method bernapas() hanya dapat dijalankan di dalam kandang fisik."
      },
      {
        "key": "D",
        "text": "Kucing dilarang memiliki method sendiri selain yang ada di Hewan."
      },
      {
        "key": "E",
        "text": "Program memicu error karena Kucing tidak memiliki constructor."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OOP: INHERITANCE REUSABILITY",
      "latex": "\\text{Kucing} \\subseteq \\text{Hewan} \\implies \\text{Methods}(k) = \\text{Methods}(\\text{Hewan}) \\cup \\text{Methods}(\\text{Kucing})",
      "legend": "• Subclass memperluas (extends) fungsi superclass tanpa menulis ulang method dasar yang sudah ada."
    },
    "hints": {
      "concept": "Kelas turunan (anak) otomatis memiliki akses ke semua method publik yang didefinisikan pada kelas induk.",
      "execution": "Pilihlah opsi yang menjelaskan pewarisan method dari class induk ke class anak."
    },
    "explanation": "Inheritance (Pewarisan) memungkinkan class turunan (`Kucing`) secara otomatis mewarisi perilaku dan atribut dari class induk (`Hewan`). Oleh karena itu, objek `k` yang diinstansiasi dari class `Kucing` dapat langsung memanggil method warisan `bernapas()` sekaligus method khususnya sendiri `bersuara()`. Output: 'Menghirup oksigen dan Meow'. Jawaban: A.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Polymorphism: Antarmuka Terpadu Multi-Objek",
    "type": "mcq",
    "questionHtml": "Perhatikan sistem penggajian karyawan berikut:<br><pre><code class=\"language-python\">class KaryawanTetap:\n    def hitung_gaji(self):\n        return 5000000\n\nclass KaryawanKontrak:\n    def hitung_gaji(self):\n        return 3500000\n\ndef cetak_slip(k):\n    print(\"Gaji:\", k.hitung_gaji())\n\ncetak_slip(KaryawanTetap())\ncetak_slip(KaryawanKontrak())</code></pre>Kelebihan utama penggunaan pendekatan polimorfik pada fungsi <code>cetak_slip(k)</code> di atas jika perusahaan menambah tipe baru <code>KaryawanMagang</code> di masa depan adalah …",
    "options": [
      {
        "key": "A",
        "text": "Fungsi cetak_slip() tidak perlu diubah sama sekali (memenuhi prinsip Open/Closed Principle), cukup buat class KaryawanMagang yang memiliki method hitung_gaji()."
      },
      {
        "key": "B",
        "text": "Seluruh database perusahaan harus diinstal ulang dari awal."
      },
      {
        "key": "C",
        "text": "Karyawan Magang dilarang menerima gaji dalam bentuk uang."
      },
      {
        "key": "D",
        "text": "Fungsi cetak_slip() harus ditulis ulang menjadi 10 fungsi berbeda."
      },
      {
        "key": "E",
        "text": "Program akan otomatis berhenti bekerja."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "SOLID: OPEN/CLOSED PRINCIPLE (OCP)",
      "latex": "\\text{Open for Extension} \\land \\text{Closed for Modification} \\implies \\text{Polymorphic Function Extensibility}",
      "legend": "• Menambah jenis karyawan baru tidak merusak atau memerlukan pengubahan pada logika fungsi pencetakan slip gaji."
    },
    "hints": {
      "concept": "Prinsip Open/Closed (OCP): kode terbuka untuk penambahan fitur baru tetapi tertutup untuk modifikasi kode yang sudah stabil.",
      "execution": "Pilihlah jawaban yang menegaskan bahwa fungsi cetak_slip() tidak perlu diubah saat ada kelas karyawan baru."
    },
    "explanation": "Keunggulan utama Polymorphism adalah mendukung prinsip Open/Closed Principle (OCP). Fungsi `cetak_slip(k)` dirancang fleksibel menerima objek apa pun yang memiliki antarmuka `hitung_gaji()`. Jika kelak ditambah kelas baru `KaryawanMagang`, kita tidak perlu menyentuh atau memodifikasi fungsi `cetak_slip()`. Cukup pastikan kelas baru mengimplementasikan method `hitung_gaji()`. Jawaban: A.",
    "isDiagnostic": False
  },

  # =============================================================
  # BAGIAN II: 5 SOAL PILIHAN GANDA KOMPLEKS (rpl-sim-26 s.d. 30)
  # Mengadopsi Soal 43, 44, 46, 47, 49 dari PDF Asli
  # =============================================================
  {
    "id": "rpl-sim-26",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Prinsip Manajemen Proyek Agile/Scrum",
    "type": "multi",
    "questionHtml": "Dalam ekosistem industri perangkat lunak modern, kerangka kerja <strong>Agile/Scrum</strong> diterapkan secara luas untuk menghadapi perubahan kebutuhan pasar yang dinamis. Berdasarkan prinsip-prinsip <em>Agile Manifesto</em> dan panduan Scrum resmi, pilihlah <strong>3 pernyataan yang BENAR</strong> mengenai pelaksanaan proyek perangkat lunak!<br><br><small>Petunjuk: Centang 3 pilihan yang benar.</small>",
    "options": [
      {
        "key": "A",
        "text": "Perubahan kebutuhan perangkat lunak di tengah proyek ditolak keras demi menjaga kepatuhan jadwal awal dokumen kontrak."
      },
      {
        "key": "B",
        "text": "Tim pengembangan berkolaborasi secara intensif setiap hari dengan pemangku kepentingan bisnis selama siklus Sprint berjalan."
      },
      {
        "key": "C",
        "text": "Perangkat lunak yang berfungsi dengan baik (working software) adalah ukuran utama kemajuan proyek."
      },
      {
        "key": "D",
        "text": "Tim melakukan refleksi dan evaluasi berkala (Sprint Retrospective) untuk memperbaiki efektivitas cara kerja dan proses pengembangan."
      },
      {
        "key": "E",
        "text": "Dokumentasi tebal ribuan lembar wajib diselesaikan secara sempurna sebelum baris kode pertama diizinkan untuk ditulis."
      }
    ],
    "correctKeys": ["B", "C", "D"],
    "formulaHud": {
      "title": "AGILE MANIFESTO 4 CORE VALUES",
      "latex": "\\begin{aligned} \\text{Individuals \\& Interactions} & > \\text{Processes \\& Tools} \\\\ \\text{Working Software} & > \\text{Comprehensive Documentation} \\\\ \\text{Customer Collaboration} & > \\text{Contract Negotiation} \\\\ \\text{Responding to Change} & > \\text{Following a Plan} \\end{aligned}",
      "legend": "• Agile merangkul perubahan (Welcome changing requirements).<br>• Nilai kemajuan utama diukur dari perangkat lunak yang berfungsi (Working software)."
    },
    "hints": {
      "concept": "Manifesto Agile mengutamakan kolaborasi intensif, perangkat lunak yang berfungsi nyata, dan kemampuan beradaptasi lewat retrospeksi.",
      "execution": "Pernyataan 2 (B), 3 (C), dan 4 (D) benar. Pernyataan 1 salah (Agile menyambut perubahan). Pernyataan 5 salah (Waterfall mindset)."
    },
    "explanation": "Pilihan yang BENAR adalah B, C, dan D (Pernyataan 2, 3, dan 4). Prinsip Agile menyambut baik perubahan kebutuhan (Opsi A salah) dan memprioritaskan software yang berfungsi dibandingkan dokumentasi yang tebal berlebihan (Opsi E salah). Jawaban: B, C, D.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-27",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Pengelolaan Aset & Keamanan Git Repository",
    "type": "multi",
    "questionHtml": "Keamanan repositori kode program merupakan tanggung jawab fundamental setiap pengembang perangkat lunak untuk melindungi aset digital perusahaan. Pilihlah <strong>3 pernyataan yang BENAR</strong> terkait prosedur keamanan aset kode pada repositori Git!<br><br><small>Petunjuk: Centang 3 pilihan yang benar.</small>",
    "options": [
      {
        "key": "A",
        "text": "Menyimpan file `.env` berisi kata sandi database dan API key ke dalam public repository agar rekan satu tim dapat langsung menggunakannya."
      },
      {
        "key": "B",
        "text": "Memasukkan file `.env` dan folder dependensi (seperti `node_modules` atau `venv`) ke dalam file `.gitignore` agar tidak terlacak oleh Git."
      },
      {
        "key": "C",
        "text": "Menggunakan pasangan kunci otentikasi SSH (SSH Key pair) untuk akses repositori remote sebagai alternatif yang lebih aman daripada kata sandi biasa."
      },
      {
        "key": "D",
        "text": "Segera melakukan revoke (pencabutan) dan rotasi rahasia jika API key tidak sengaja terdorong (pushed) ke repositori publik."
      },
      {
        "key": "E",
        "text": "Membagikan akun GitHub pribadi kepada seluruh tim pengembang untuk mempermudah pengerjaan commit proyek bersama."
      }
    ],
    "correctKeys": ["B", "C", "D"],
    "formulaHud": {
      "title": "GIT REPOSITORY HYGIENE & SECRETS GOVERNANCE",
      "latex": "\\texttt{.gitignore} \\ni \\texttt{.env} \\quad \\land \\quad \\text{Auth via SSH Key} \\quad \\land \\quad \\text{Leak Response} \\implies \\text{Revoke \\& Rotate}",
      "legend": "• Jangan pernah membagikan akun personal (gunakan GitHub Organization & Teams).<br>• Jangan commit berkas kredensial atau folder dependensi ke Git tree."
    },
    "hints": {
      "concept": "Lindungi kredensial dengan .gitignore, gunakan otentikasi SSH Key pair, dan segera cabut (revoke) kunci jika terjadi kebocoran.",
      "execution": "Pernyataan B, C, dan D benar. Pernyataan A salah (bocorkan kredensial). Pernyataan E salah (langgar prinsip akuntabilitas akun)."
    },
    "explanation": "Pilihan yang BENAR adalah B, C, dan D (Pernyataan 2, 3, dan 4). Menyimpan password di repositori publik (Opsi A) adalah celah keamanan fatal. Membagikan akun pribadi (Opsi E) melanggar prinsip akuntabilitas dan jejak audit (audit trail). Jawaban: B, C, D.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-28",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Arsitektur & Protokol TCP/IP (DNS, HTTP, UDP)",
    "type": "multi",
    "questionHtml": "Dalam pengembangan perangkat lunak berbasis jaringan dan gim online, berbagai protokol pada arsitektur TCP/IP memiliki peran spesifik. Pilihlah <strong>3 pernyataan yang BENAR</strong> terkait fungsi protokol dan mekanisme komunikasi jaringan!<br><br><small>Petunjuk: Centang 3 pilihan yang benar.</small>",
    "options": [
      {
        "key": "A",
        "text": "Application Layer pada model TCP/IP bertugas menentukan ukuran diameter fisik tembaga pada kabel UTP."
      },
      {
        "key": "B",
        "text": "Protokol DNS (Domain Name System) berfungsi menerjemahkan nama domain (seperti `api.studigim.id`) menjadi alamat IP numerik."
      },
      {
        "key": "C",
        "text": "Dalam komunikasi layanan web berbasis REST API menggunakan protokol HTTP/HTTPS, metode POST umumnya digunakan client untuk mengirim data baru ke server."
      },
      {
        "key": "D",
        "text": "Protokol UDP pada Transport Layer sering digunakan untuk transmisi pergerakan posisi pemain gim multiplayer real-time karena memiliki latensi dan overhead yang rendah."
      },
      {
        "key": "E",
        "text": "Alamat MAC (Media Access Control) bekerja pada Application Layer untuk mengenkripsi kueri SQL secara otomatis."
      }
    ],
    "correctKeys": ["B", "C", "D"],
    "formulaHud": {
      "title": "TCP/IP PROTOCOL SUITE MAPPING",
      "latex": "\\begin{aligned} \\text{Application} & : \\text{DNS (Port 53), HTTP/HTTPS (Port 80/443)} \\\\ \\text{Transport} & : \\text{UDP (Low Latency), TCP (Reliable)} \\\\ \\text{Data Link} & : \\text{MAC Address (Layer 2)} \\end{aligned}",
      "legend": "• Kabel tembaga diatur Physical Layer (bukan Application).<br>• MAC address bekerja di Data Link Layer (bukan Application Layer)."
    },
    "hints": {
      "concept": "DNS menerjemahkan nama domain ke IP. HTTP POST mengirim data baru ke API. UDP digunakan untuk transmisi koordinat game karena cepat tanpa overhead.",
      "execution": "Pernyataan B, C, dan D benar. Pernyataan A salah (kabel fisik). Pernyataan E salah (MAC bukan di Application Layer)."
    },
    "explanation": "Pilihan yang BENAR adalah B, C, dan D (Pernyataan 2, 3, dan 4). Pernyataan A salah karena kabel fisik diatur pada Physical Layer / Network Interface Layer. Pernyataan E salah karena alamat MAC bekerja pada Data Link Layer (Layer 2) dan tidak mengenkripsi SQL. Jawaban: B, C, D.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-29",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Struktur Data List & Kontrol Perulangan",
    "type": "multi",
    "questionHtml": "Perhatikan potongan program penyaringan skor turnamen gim berikut:<br><pre><code class=\"language-python\">skor_pemain = [45, 80, 92, 60, 88]\nperingkat_atas = []\nfor s in skor_pemain:\n    if s >= 80:\n        peringkat_atas.append(s)\nprint(len(peringkat_atas))</code></pre>Pilihlah <strong>3 pernyataan yang BENAR</strong> berdasarkan analisis alur logika dan struktur data pada potongan program di atas!<br><br><small>Petunjuk: Centang 3 pilihan yang benar.</small>",
    "options": [
      {
        "key": "A",
        "text": "Variabel `skor_pemain` dan `peringkat_atas` menggunakan struktur data list/array untuk menampung sekumpulan elemen secara berurutan."
      },
      {
        "key": "B",
        "text": "Perulangan `for` pada program tersebut hanya memeriksa elemen pertama (45) dan elemen terakhir (88) saja."
      },
      {
        "key": "C",
        "text": "Struktur kontrol percabangan `if s >= 80:` berfungsi menyaring agar hanya skor bernilai 80 ke atas yang dimasukkan ke dalam list `peringkat_atas`."
      },
      {
        "key": "D",
        "text": "Setelah perulangan selesai dieksekusi, isi dari `peringkat_atas` adalah `[80, 92, 88]` dan output `print(len(peringkat_atas))` adalah 3."
      },
      {
        "key": "E",
        "text": "Nilai 60 ikut ditambahkan ke dalam list `peringkat_atas` karena berada tepat di tengah daftar."
      }
    ],
    "correctKeys": ["A", "C", "D"],
    "formulaHud": {
      "title": "TRACE LIST FILTERING ALGORITHM",
      "latex": "S = [45, 80, 92, 60, 88] \\xrightarrow{s \\ge 80} P = [80, 92, 88] \\implies |P| = 3",
      "legend": "• 45 < 80 (Lewat)<br>• 80 >= 80 (Masuk)<br>• 92 >= 80 (Masuk)<br>• 60 < 80 (Lewat)<br>• 88 >= 80 (Masuk)<br>• Hasil akhir peringkat_atas: [80, 92, 88], panjang list = 3."
    },
    "hints": {
      "concept": "List menyimpan data berurutan. Percabangan if menyaring skor >= 80. Elemen yang lolos adalah 80, 92, dan 88 (total 3 elemen).",
      "execution": "Pernyataan A, C, dan D benar. Pernyataan B salah (for memeriksa semua elemen). Pernyataan E salah (60 tidak lolos kondisi >= 80)."
    },
    "explanation": "Pilihan yang BENAR adalah A, C, dan D (Pernyataan 1, 3, dan 4). Pernyataan B salah karena for mengiterasi seluruh elemen list dari awal hingga akhir. Pernyataan E salah karena angka 60 tidak memenuhi syarat s >= 80 sehingga diabaikan. Jawaban: A, C, D.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-30",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Enkapsulasi & Pewarisan (Inheritance)",
    "type": "multi",
    "questionHtml": "Perhatikan potongan program rancangan class entitas gim berikut:<br><pre><code class=\"language-python\">class EntitasGim:\n    def __init__(self, nama, hp):\n        self.nama = nama\n        self._hp = hp\n    def get_hp(self):\n        return self._hp\n    def terima_damage(self, nilai):\n        self._hp = max(0, self._hp - nilai)\n\nclass Pemain(EntitasGim):\n    def __init__(self, nama, hp, koin):\n        super().__init__(nama, hp)\n        self.koin = koin</code></pre>Pilihlah <strong>3 pernyataan yang BENAR</strong> berdasarkan analisis rancangan class di atas!<br><br><small>Petunjuk: Centang 3 pilihan yang benar.</small>",
    "options": [
      {
        "key": "A",
        "text": "Class `EntitasGim` merupakan subclass (kelas turunan) dari class `Pemain`."
      },
      {
        "key": "B",
        "text": "Class `Pemain` mewarisi atribut dan method dari class `EntitasGim` melalui mekanisme inheritance."
      },
      {
        "key": "C",
        "text": "Penulisan atribut `_hp` dengan garis bawah menandakan bahwa atribut tersebut akan otomatis terhapus setiap kali method dipanggil."
      },
      {
        "key": "D",
        "text": "Method `terima_damage(self, nilai)` menjaga integritas data atribut `_hp` agar nilainya tidak pernah turun menjadi bilangan negatif di bawah 0."
      },
      {
        "key": "E",
        "text": "Pemanggilan `super().__init__(nama, hp)` di dalam constructor `Pemain` berfungsi menjalankan inisialisasi atribut `nama` dan `_hp` milik superclass `EntitasGim`."
      }
    ],
    "correctKeys": ["B", "D", "E"],
    "formulaHud": {
      "title": "OOP: INHERITANCE & STATE INTEGRITY",
      "latex": "\\text{Class Pemain extends EntitasGim} \\quad \\land \\quad \\text{terima\\_damage}(\\Delta): \\; \\text{\\_hp} = \\max(0, \\text{\\_hp} - \\Delta)",
      "legend": "• `Pemain` adalah subclass, `EntitasGim` adalah superclass.<br>• `max(0, ...)` menjamin HP tidak pernah bernilai minus.<br>• `super()` meneruskan inisialisasi dasar ke superclass."
    },
    "hints": {
      "concept": "Pemain mewarisi EntitasGim. Method terima_damage menjaga nilai hp >= 0 dengan fungsi max. super() menginisialisasi superclass.",
      "execution": "Pernyataan B, D, dan E benar. Pernyataan A salah (terbalik). Pernyataan C salah (garis bawah satu adalah konvensi protected/private internal)."
    },
    "explanation": "Pilihan yang BENAR adalah B, D, dan E (Pernyataan 2, 4, dan 5). Pernyataan A salah karena `Pemain` yang merupakan turunan dari `EntitasGim`, bukan sebaliknya. Pernyataan C salah karena garis bawah satu (`_hp`) adalah konvensi atribut terlindungi (protected/internal), bukan tanda penghapusan memori otomatis. Jawaban: B, D, E.",
    "isDiagnostic": False
  },

  # =============================================================
  # BAGIAN III: 5 SOAL KATEGORI BENAR/SALAH (rpl-sim-31 s.d. 35)
  # Mengadopsi Soal 31, 33, 35, 37, 41 dari PDF Asli
  # =============================================================
  {
    "id": "rpl-sim-31",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Profesi, Manajemen Proyek & Budaya Mutu",
    "type": "matrix",
    "questionHtml": "Dalam ekosistem industri perangkat lunak modern, setiap profesi dan peran memiliki tanggung jawab spesifik dalam siklus manajemen proyek. Tentukan <strong>Benar</strong> atau <strong>Salah</strong> untuk setiap pernyataan berikut!",
    "statements": [
      {
        "id": "0",
        "text": "Scrum Master bertanggung jawab menetapkan prioritas fitur bisnis dan menjual produk langsung ke konsumen akhir."
      },
      {
        "id": "1",
        "text": "Product Owner bertugas mengelola daftar Product Backlog serta memaksimalkan nilai produk bagi pengguna."
      },
      {
        "id": "2",
        "text": "Pengujian perangkat lunak secara berkelanjutan (Continuous Testing) oleh Quality Assurance membantu mendeteksi bug sedini mungkin sebelum rilis produksi."
      }
    ],
    "correctAnswers": {
      "0": False,
      "1": True,
      "2": True
    },
    "formulaHud": {
      "title": "SCRUM ROLES RESPONSIBILITY MATRIX",
      "latex": "\\begin{aligned} \\text{Product Owner} & : \\text{Backlog Priority \\& Value Maximizer (Business)} \\\\ \\text{Scrum Master} & : \\text{Process Coach \\& Impediment Remover} \\\\ \\text{QA Tester} & : \\text{Quality Verification \\& Defect Prevention} \\end{aligned}",
      "legend": "• Menetapkan prioritas bisnis adalah tugas Product Owner, BUKAN Scrum Master."
    },
    "hints": {
      "concept": "Scrum Master memfasilitasi proses tim dan membuang halangan, Product Owner mengelola backlog & prioritas bisnis, QA menjaga mutu dengan pengujian berkelanjutan.",
      "execution": "Pernyataan 0 Salah. Pernyataan 1 Benar. Pernyataan 2 Benar."
    },
    "explanation": "Pernyataan 0 SALAH (menetapkan prioritas bisnis produk adalah tugas Product Owner, sedangkan Scrum Master bertugas memfasilitasi kerangka kerja Scrum dan mengatasi hambatan tim). Pernyataan 1 BENAR (Product Owner adalah pemilik dan pengelola tunggal dari Product Backlog). Pernyataan 2 BENAR (Continuous Testing oleh tim QA bertujuan menangkap cacat sistem sedini mungkin). Jawaban: S - B - B.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-32",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "K3LH Lingkungan TI & Ergonomi Kerja",
    "type": "matrix",
    "questionHtml": "Penerapan prinsip K3LH dan ergonomi sangat penting untuk mencegah gangguan kesehatan kerja pada programmer. Tentukan <strong>Benar</strong> atau <strong>Salah</strong> untuk setiap pernyataan berikut!",
    "statements": [
      {
        "id": "0",
        "text": "Aturan 20-20-20 menganjurkan agar setiap 20 menit menatap layar, istirahatkan mata selama 20 detik dengan melihat objek sejauh 20 kaki (sekitar 6 meter)."
      },
      {
        "id": "1",
        "text": "Menatap layar monitor dari jarak 5 cm dalam ruangan yang gelap gulita merupakan posisi kerja yang sangat dianjurkan untuk meningkatkan fokus pengkodean."
      },
      {
        "id": "2",
        "text": "Menggunakan kursi ergonomis dengan penopang punggung (lumbar support) membantu menjaga postur tulang belakang tetap tegak dan mengurangi ketegangan otot leher."
      }
    ],
    "correctAnswers": {
      "0": True,
      "1": False,
      "2": True
    },
    "formulaHud": {
      "title": "ERGONOMI PROGRAMMER: STANDARD GUIDELINES",
      "latex": "\\text{Jarak Layar} \\approx 50\\text{--}70\\text{ cm} \\quad \\land \\quad \\text{Pencahayaan Cukup} \\quad \\land \\quad \\text{Sudut Pandang } 15^{\\circ}\\text{--}20^{\\circ} \\text{ ke Bawah}",
      "legend": "• Menatap layar dari jarak 5 cm dalam gelap merusak penglihatan dan memicu ketegangan mata parah (Eye Strain & Asthenopia)."
    },
    "hints": {
      "concept": "Aturan 20-20-20 benar. Jarak monitor 5 cm di ruang gelap sangat berbahaya bagi mata (salah). Kursi ergonomis penopang punggung benar.",
      "execution": "Pernyataan 0 Benar. Pernyataan 1 Salah. Pernyataan 2 Benar."
    },
    "explanation": "Pernyataan 0 BENAR (Aturan 20-20-20 adalah pedoman baku relaksasi mata optometri). Pernyataan 1 SALAH (Jarak ideal mata ke layar adalah 50–70 cm dengan pencahayaan ruangan yang memadai; jarak 5 cm di ruang gelap merusak mata). Pernyataan 2 BENAR (Kursi ergonomis dengan lumbar support dirancang menjaga kurva alami tulang belakang). Jawaban: B - S - B.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-33",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Sistem Operasi Linux & Hak Akses Berkas",
    "type": "matrix",
    "questionHtml": "Seorang pengembang sedang mengatur hak akses file dan direktori aplikasi web pada server berbasis Linux. Tentukan <strong>Benar</strong> atau <strong>Salah</strong> untuk setiap pernyataan berikut!",
    "statements": [
      {
        "id": "0",
        "text": "Perintah `chmod 755 deploy.sh` memberikan hak baca, tulis, dan eksekusi (rwx) kepada pemilik file (owner), serta hak baca dan eksekusi (r-x) kepada group dan others."
      },
      {
        "id": "1",
        "text": "Direktori `/var/www/html/uploads` yang berfungsi menyimpan file unggahan pengguna memerlukan izin tulis (write permission) bagi user layanan web server."
      },
      {
        "id": "2",
        "text": "Memberikan hak akses `chmod 777` pada seluruh file konfigurasi rahasia di server produksi merupakan praktik keamanan standar yang sangat dianjurkan."
      }
    ],
    "correctAnswers": {
      "0": True,
      "1": True,
      "2": False
    },
    "formulaHud": {
      "title": "LINUX PERMISSION SECURITY HYGIENE",
      "latex": "755 = (4+2+1)(4+0+1)(4+0+1) = \\texttt{rwxr-xr-x} \\quad \\mid \\quad 777 = \\texttt{rwxrwxrwx} \\; (\\text{CRITICAL SECURITY RISK})",
      "legend": "• chmod 777 memberi izin tulis kepada siapapun di internet/sistem, membuka celah eksekusi kode jahat (Remote Code Execution)."
    },
    "hints": {
      "concept": "chmod 755 memberikan rwx pada owner dan r-x pada grup/others (benar). Folder uploads butuh hak tulis server (benar). chmod 777 pada file rahasia server produksi adalah celah keamanan fatal (salah).",
      "execution": "Pernyataan 0 Benar. Pernyataan 1 Benar. Pernyataan 2 Salah."
    },
    "explanation": "Pernyataan 0 BENAR (7 = 4+2+1 [rwx], 5 = 4+1 [r-x] untuk group dan others). Pernyataan 1 BENAR (Layanan web server memerlukan izin tulis [write] untuk menyimpan berkas yang diunggah pengguna ke direktori server). Pernyataan 2 SALAH (Memberikan chmod 777 berarti siapapun pengguna di sistem dapat membaca, memodifikasi, dan menghapus berkas konfigurasi rahasia, melanggar prinsip Least Privilege). Jawaban: B - B - S.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-34",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Analisis Struktur Kontrol Program",
    "type": "matrix",
    "questionHtml": "Perhatikan potongan program pemeriksaan ketuntasan nilai berikut:<br><pre><code class=\"language-python\">nilai = [70, 85, 60, 90, 75]\njumlah_lulus = 0\nfor n in nilai:\n    if n >= 75:\n        jumlah_lulus += 1\nprint(jumlah_lulus)</code></pre>Tentukan <strong>Benar</strong> atau <strong>Salah</strong> untuk setiap pernyataan berikut!",
    "statements": [
      {
        "id": "0",
        "text": "Perulangan `for` digunakan untuk memeriksa setiap elemen nilai di dalam daftar nilai secara berurutan."
      },
      {
        "id": "1",
        "text": "Nilai 75 memenuhi kondisi percabangan sehingga dihitung masuk ke dalam kategori lulus."
      },
      {
        "id": "2",
        "text": "Pada akhir eksekusi program, nilai yang tersimpan di dalam variabel `jumlah_lulus` adalah 2."
      }
    ],
    "correctAnswers": {
      "0": True,
      "1": True,
      "2": False
    },
    "formulaHud": {
      "title": "TRACE LOOP EVALUATION",
      "latex": "n \\in [70, 85, 60, 90, 75] \\land n \\ge 75 \\implies \\{85, 90, 75\\} \\implies \\text{jumlah\\_lulus} = 3 \\neq 2",
      "legend": "• 70: False<br>• 85: True (lulus=1)<br>• 60: False<br>• 90: True (lulus=2)<br>• 75: True (lulus=3)"
    },
    "hints": {
      "concept": "Periksa kondisi: operator >= mencakup angka 75. Hitung berapa angka yang >= 75: 85, 90, 75 (ada 3 angka, bukan 2).",
      "execution": "Pernyataan 0 Benar. Pernyataan 1 Benar. Pernyataan 2 Salah."
    },
    "explanation": "Pernyataan 0 BENAR (for loop membaca elemen list secara sekuensial). Pernyataan 1 BENAR (karena operator relasional yang digunakan adalah `>=` [lebih besar atau sama dengan], maka nilai 75 memenuhi syarat). Pernyataan 2 SALAH (elemen yang memenuhi syarat adalah 85, 90, dan 75, sehingga nilai akhir `jumlah_lulus` adalah 3, bukan 2). Jawaban: B - B - S.",
    "isDiagnostic": False
  },
  {
    "id": "rpl-sim-35",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "simulasi",
    "difficulty": "simulation_hots",
    "topic": "Enkapsulasi & Validasi Data Mutator",
    "type": "matrix",
    "questionHtml": "Perhatikan potongan kode class <code>AkunGim</code> berikut:<br><pre><code class=\"language-python\">class AkunGim:\n    def __init__(self, username):\n        self.username = username\n        self.__level = 1\n    def get_level(self):\n        return self.__level\n    def naik_level(self, xp):\n        if xp >= 100:\n            self.__level += 1</code></pre>Tentukan <strong>Benar</strong> atau <strong>Salah</strong> untuk setiap pernyataan berikut!",
    "statements": [
      {
        "id": "0",
        "text": "Penulisan atribut `__level` (dengan dua garis bawah di depan) menerapkan mekanisme penyembunyian data (private attribute) agar tidak diakses langsung secara sembarangan dari luar class."
      },
      {
        "id": "1",
        "text": "Tujuan utama enkapsulasi pada class `AkunGim` adalah agar semua variabel internal dapat dimodifikasi bebas tanpa aturan validasi oleh bagian program mana pun."
      },
      {
        "id": "2",
        "text": "Method `naik_level(self, xp)` bertindak sebagai mutator terproteksi yang memastikan kenaikan level hanya terjadi apabila syarat `xp >= 100` terpenuhi."
      }
    ],
    "correctAnswers": {
      "0": True,
      "1": False,
      "2": True
    },
    "formulaHud": {
      "title": "ENCAPSULATION & DATA INTEGRITY RULE",
      "latex": "\\text{Enkapsulasi} \\implies \\text{Proteksi State Internal Object} \\quad \\land \\quad \\text{Modifikasi HANYA lewat Aturan Validasi}",
      "legend": "• Enkapsulasi justru MEMBATASI modifikasi liar, bukan membebaskan modifikasi tanpa aturan."
    },
    "hints": {
      "concept": "Atribut __level adalah private (benar). Enkapsulasi bertujuan membatasi modifikasi liar, bukan membebaskannya (salah). Method naik_level memvalidasi xp >= 100 (benar).",
      "execution": "Pernyataan 0 Benar. Pernyataan 1 Salah. Pernyataan 2 Benar."
    },
    "explanation": "Pernyataan 0 BENAR (Awalan `__` pada Python menerapkan name mangling untuk menyembunyikan atribut dari akses langsung luar). Pernyataan 1 SALAH (Tujuan utama enkapsulasi justru sebaliknya: melindungi integritas data internal agar TIDAK dapat dimodifikasi secara bebas atau sembarangan tanpa melewati aturan validasi). Pernyataan 2 BENAR (Method `naik_level` memvalidasi bahwa hanya jika syarat `xp >= 100` dipenuhi barulah atribut `__level` dinaikkan). Jawaban: B - S - B.",
    "isDiagnostic": False
  }
]

print("Loaded 35 simulasi questions.")
