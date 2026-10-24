# -*- coding: utf-8 -*-
"""
TKA PPLG - 25 SOAL LATIHAN EASY (rpl-lat-e-01 s.d. rpl-lat-e-25)
Mengadopsi langsung 25 Soal Autentik Pilihan Ganda dari Simulasi Resmi TKA PPLG Pusmendik
"""

EASY_QUESTIONS = [
  {
    "id": "rpl-lat-e-01",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Profesi & Kewirausahaan PPLG",
    "type": "mcq",
    "questionHtml": "Dalam sebuah tim pengembangan perangkat lunak, terdapat berbagai peran profesi yang saling berkolaborasi. Tugas utama dari seorang <strong>UI/UX Designer</strong> dalam siklus pengembangan aplikasi adalah …",
    "options": [
      {
        "key": "A",
        "text": "Mengelola konfigurasi server dan jaringan agar aplikasi berjalan stabil saat diakses pengguna."
      },
      {
        "key": "B",
        "text": "Merancang tampilan antarmuka (User Interface) dan alur pengalaman pengguna (User Experience) aplikasi."
      },
      {
        "key": "C",
        "text": "Menulis kode program sisi server (backend) untuk memproses transaksi basis data."
      },
      {
        "key": "D",
        "text": "Melakukan pengujian penetrasi keamanan (penetration testing) terhadap celah sistem aplikasi."
      },
      {
        "key": "E",
        "text": "Mengatur proses kompilasi rilis dan distribusi aplikasi ke toko aplikasi (app store)."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "DESAIN PRODUK DIGITAL: UI VS UX",
      "latex": "\\text{UI (Visual Design)} + \\text{UX (User Journey)} \\implies \\text{Usable & Intuitive Product}",
      "legend": "• UI Designer: Tata letak, warna, tipografi, dan komponen visual.<br>• UX Designer: Riset persona, alur navigasi (wireframe/prototype), dan kemudahan interaksi."
    },
    "hints": {
      "concept": "UI berfokus pada estetika visual dan komponen antarmuka, sedangkan UX berfokus pada efisiensi alur serta kepuasan interaksi pengguna.",
      "execution": "Pilihlah peran yang berhubungan langsung dengan desain visual antarmuka dan alur kenyamanan pengguna."
    },
    "explanation": "Tugas utama UI/UX Designer adalah merancang antarmuka grafis (UI) serta alur interaksi dan kenyamanan pengguna (UX). Opsi A adalah tugas DevOps/Sysadmin, Opsi C tugas Backend Developer, Opsi D tugas Security Specialist, dan Opsi E tugas Release Engineer. Jawaban: B.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-02",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Profesi & Kewirausahaan PPLG",
    "type": "mcq",
    "questionHtml": "Sebuah studio gim sedang menyelesaikan pengembangan gim mobile sebelum diluncurkan ke publik. Peran utama seorang <strong>Quality Assurance (QA) Tester</strong> pada tahap tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Merancang karakter 3D, animasi, dan aset visual lingkungan gim."
      },
      {
        "key": "B",
        "text": "Menyusun strategi monetisasi dan kampanye pemasaran gim di media sosial."
      },
      {
        "key": "C",
        "text": "Menguji perangkat lunak/gim secara sistematis untuk menemukan bug dan memastikan kesesuaian dengan spesifikasi."
      },
      {
        "key": "D",
        "text": "Mendesain topologi jaringan lokal untuk kantor operasional studio gim."
      },
      {
        "key": "E",
        "text": "Menulis kontrak kerja sama lisensi dengan investor dan penerbit gim."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "SIKLUS TESTING PERANGKAT LUNAK (QA)",
      "latex": "\\text{Spesifikasi Fitur} \\xrightarrow{\\text{Test Case Execution}} \\text{Bug Tracking} \\to \\text{Release Approval}",
      "legend": "• QA Engineer/Tester bertindak sebagai penjaga gerbang kualitas (quality gatekeeper) sebelum produk didistribusikan."
    },
    "hints": {
      "concept": "Quality Assurance (QA) bertugas memverifikasi fungsionalitas dan mencari celah kesalahan (defect/bug) agar produk siap rilis.",
      "execution": "Cari opsi yang menekankan pengujian sistematis dan verifikasi spesifikasi."
    },
    "explanation": "Peran utama QA Tester adalah merancang skenario pengujian, mengeksekusi test case, menemukan bug, dan memvalidasi apakah gim berjalan sesuai kriteria penerimaan (acceptance criteria). Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-03",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Profesi & Kewirausahaan PPLG",
    "type": "mcq",
    "questionHtml": "Dalam industri pengembangan gim (game development), profesi yang bertanggung jawab merancang mekanik permainan (game mechanics), aturan menang-kalah, sistem level, dan keseimbangan alur permainan (gameplay balancing) adalah …",
    "options": [
      {
        "key": "A",
        "text": "Game Designer"
      },
      {
        "key": "B",
        "text": "Database Administrator"
      },
      {
        "key": "C",
        "text": "Network Engineer"
      },
      {
        "key": "D",
        "text": "Sound Engineer"
      },
      {
        "key": "E",
        "text": "System Administrator"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "GAME DESIGN ARCHITECTURE",
      "latex": "\\text{Core Loop} + \\text{Rules & Mechanics} + \\text{Balancing} \\implies \\text{Game Design Document (GDD)}",
      "legend": "• Game Designer merumuskan visi gameplay, aturan main, dan desain level.<br>• Game Programmer merealisasikan rancangan tersebut ke dalam kode."
    },
    "hints": {
      "concept": "Game Designer adalah arsitek alur permainan dan aturan mekanik gim yang dituangkan ke dalam Game Design Document (GDD).",
      "execution": "Pilihlah profesi yang memegang peran konseptual mekanik gim, bukan infrastruktur jaringan atau audio."
    },
    "explanation": "Game Designer bertanggung jawab menyusun aturan, mekanik, sistem progresi, dan balancing gim. Database Administrator (B) mengelola basis data, Network Engineer (C) mengelola jaringan, dan Sound Engineer (D) memproduksi audio efek. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-04",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Manajemen Proyek & Budaya Mutu",
    "type": "mcq",
    "questionHtml": "Seorang Project Manager memimpin proyek pembuatan sistem informasi rumah sakit. Urutan tahapan dasar manajemen proyek perangkat lunak dari awal hingga selesai yang paling tepat adalah …",
    "options": [
      {
        "key": "A",
        "text": "Pelaksanaan → Perencanaan → Inisiasi → Penutupan"
      },
      {
        "key": "B",
        "text": "Perencanaan → Inisiasi → Penutupan → Pelaksanaan dan Pemantauan"
      },
      {
        "key": "C",
        "text": "Penutupan → Pelaksanaan → Perencanaan → Inisiasi"
      },
      {
        "key": "D",
        "text": "Inisiasi → Perencanaan → Pelaksanaan dan Pemantauan → Penutupan"
      },
      {
        "key": "E",
        "text": "Inisiasi → Penutupan → Perencanaan → Pelaksanaan dan Pemantauan"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "PMBOK / SOFTWARE PROJECT LIFECYCLE",
      "latex": "\\text{Initiating} \\to \\text{Planning} \\to \\text{Executing \\& Monitoring} \\to \\text{Closing}",
      "legend": "• 1. Inisiasi (Charter/Tujuan) → 2. Perencanaan (WBS/Jadwal) → 3. Eksekusi & Monitoring (Coding/Testing) → 4. Penutupan (Handover)."
    },
    "hints": {
      "concept": "Manajemen proyek selalu diawali perumusan tujuan proyek (inisiasi), perencanaan ruang lingkup dan jadwal, eksekusi kerja, hingga serah terima akhir (penutupan).",
      "execution": "Cari opsi yang diawali dengan Inisiasi dan diakhiri dengan Penutupan secara kronologis logis."
    },
    "explanation": "Tahapan standar manajemen proyek (PMBOK/SDLC) adalah: (1) Inisiasi (Initiating), (2) Perencanaan (Planning), (3) Pelaksanaan dan Pemantauan (Executing & Monitoring/Controlling), serta (4) Penutupan (Closing). Jawaban: D.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-05",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Kewirausahaan (Technopreneurship)",
    "type": "mcq",
    "questionHtml": "Sebuah tim wirausaha muda (startup) di bidang PPLG ingin meluncurkan aplikasi pengelola keuangan pelajar dengan modal terbatas dan tenggat waktu cepat. Berdasarkan prinsip technopreneurship, langkah awal paling efektif untuk memvalidasi ide produk ke pasar adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menyewa server berkapasitas tinggi untuk jutaan pengguna sebelum membuat baris kode pertama."
      },
      {
        "key": "B",
        "text": "Membangun produk versi fungsi inti paling esensial (Minimum Viable Product / MVP) untuk menguji respons pengguna nyata."
      },
      {
        "key": "C",
        "text": "Menunggu hingga seluruh 50 fitur tambahan selesai sempurna selama tiga tahun sebelum diperlihatkan kepada calon pengguna."
      },
      {
        "key": "D",
        "text": "Membeli lisensi perangkat lunak enterprise termahal tanpa melakukan riset permasalahan pengguna."
      },
      {
        "key": "E",
        "text": "Mengabaikan umpan balik pengguna awal karena tim pengembang sudah merasa aplikasinya sempurna."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "LEAN STARTUP FRAMEWORK",
      "latex": "\\text{Build (MVP)} \\to \\text{Measure (User Feedback)} \\to \\text{Learn (Iterate/Pivot)}",
      "legend": "• MVP (Minimum Viable Product): Versi produk dengan fitur minimum yang sudah dapat memecahkan masalah inti pengguna."
    },
    "hints": {
      "concept": "Pendekatan Lean Startup menekankan pembuatan MVP untuk memvalidasi hipotesis pasar dengan biaya dan waktu sehemat mungkin.",
      "execution": "Pilihlah langkah yang berorientasi pada perilisan versi sederhana awal untuk menguji respons pasar."
    },
    "explanation": "Langkah awal paling efektif dalam metodologi Lean Startup/Technopreneurship adalah membangun Minimum Viable Product (MVP) untuk menguji respons pengguna secara langsung dan mengumpulkan data valid sebelum menginvestasikan modal besar. Jawaban: B.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-06",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Prinsip K3LH Lingkungan TI",
    "type": "mcq",
    "questionHtml": "Pekerja di bidang pengembangan perangkat lunak dan gim menghabiskan waktu berjam-jam di depan layar monitor. Penerapan <strong>aturan 20-20-20</strong> dalam prinsip Kesehatan dan Keselamatan Kerja (K3) bertujuan untuk …",
    "options": [
      {
        "key": "A",
        "text": "Mempercepat proses kompilasi kode sumber sebanyak 20 persen dalam 20 menit."
      },
      {
        "key": "B",
        "text": "Menghemat konsumsi daya listrik komputer hingga 20 watt setiap 20 detik."
      },
      {
        "key": "C",
        "text": "Mengistirahatkan mata setiap 20 menit dengan melihat objek berjarak 20 kaki (±6 meter) selama 20 detik guna mengurangi kelelahan mata."
      },
      {
        "key": "D",
        "text": "Mengetik minimal 20 baris kode setiap 20 menit dengan maksimal 20 kesalahan sintaks."
      },
      {
        "key": "E",
        "text": "Melakukan restart sistem operasi setiap 20 jam sekali selama 20 menit."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "ATURAN K3LH KESEHATAN MATA (20-20-20 RULE)",
      "latex": "\\text{Tiap 20 Menit Bekerja} \\implies \\text{Lihat Objek 20 Kaki (6 m)} \\times 20 \\text{ Detik}",
      "legend": "• Mencegah Computer Vision Syndrome (CVS), mata kering, dan ketegangan otot akomodasi mata."
    },
    "hints": {
      "concept": "Aturan 20-20-20 adalah protokol standar ergonomi visual bagi praktisi TI yang menatap layar secara intensif.",
      "execution": "Pilihlah opsi yang menjelaskan relaksasi penglihatan mata pada jarak 20 kaki selama 20 detik."
    },
    "explanation": "Aturan 20-20-20 adalah pedoman ergonomi visual K3LH: setiap 20 menit menatap layar, istirahatkan mata dengan memandang objek berjarak 20 kaki (sekitar 6 meter) selama minimal 20 detik untuk mencegah Computer Vision Syndrome. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-07",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Ergonomi Kerja Komputer",
    "type": "mcq",
    "questionHtml": "Untuk mencegah cedera otot dan tulang belakang (<em>musculoskeletal disorders</em>) saat melakukan pemrograman dalam durasi panjang, pengaturan posisi kerja ergonomis yang tepat adalah …",
    "options": [
      {
        "key": "A",
        "text": "Mengatur bagian atas layar monitor sejajar atau sedikit di bawah tinggi mata dengan jarak pandang 50–70 cm serta punggung tersangga tegak."
      },
      {
        "key": "B",
        "text": "Meletakkan monitor jauh di atas kepala sehingga leher terus mendongak ke atas selama bekerja."
      },
      {
        "key": "C",
        "text": "Menggunakan kursi tanpa sandaran dengan posisi layar menempel kurang dari 15 cm dari mata."
      },
      {
        "key": "D",
        "text": "Meletakkan keyboard di atas pangkuan dengan posisi pergelangan tangan menekuk tajam ke atas."
      },
      {
        "key": "E",
        "text": "Mematikan seluruh pencahayaan ruangan hingga gelap gulita dan mengatur kecerahan layar pada tingkat maksimum 100%."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "STANDAR ERGONOMI WORKSTATION",
      "latex": "\\text{Jarak Layar: } 50-70\\text{ cm} \\quad | \\quad \\text{Sudut Siku/Lutut: } 90^{\\circ} \\quad | \\quad \\text{Punggung: Tegak Bersandar}",
      "legend": "• Mencegah Repetitive Strain Injury (RSI) dan nyeri leher/punggung (cervical spondylosis)."
    },
    "hints": {
      "concept": "Posisi kerja ergonomis menjaga sudut leher netral (tidak mendongak/menunduk tajam) dan jarak layar yang aman bagi mata.",
      "execution": "Pilihlah konfigurasi yang menyangga punggung tegak dengan garis pandang sejajar bagian atas monitor."
    },
    "explanation": "Pengaturan ergonomis yang benar adalah monitor berada pada jarak 50–70 cm, bagian atas layar sejajar atau sedikit di bawah mata agar leher berada pada posisi netral (15–20 derajat ke bawah), dan punggung tertopang tegak. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-08",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Pengelolaan Aset Digital & Kolaborasi",
    "type": "mcq",
    "questionHtml": "Lima orang programmer bekerja secara bersamaan mengembangkan modul yang berbeda pada satu proyek aplikasi e-commerce. Agar setiap perubahan kode tercatat riwayatnya, tidak saling menimpa secara acak, dan mudah digabungkan, perangkat pengelolaan aset digital yang wajib digunakan adalah …",
    "options": [
      {
        "key": "A",
        "text": "Aplikasi pengolah gambar bitmap."
      },
      {
        "key": "B",
        "text": "Perangkat lunak antivirus lokal."
      },
      {
        "key": "C",
        "text": "Media penyimpanan flashdisk yang dipinjamkan bergantian."
      },
      {
        "key": "D",
        "text": "Version Control System (seperti Git) dengan mekanisme branching dan merge/pull request."
      },
      {
        "key": "E",
        "text": "Aplikasi pemutar multimedia resolusi tinggi."
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "VERSION CONTROL SYSTEM (VCS)",
      "latex": "\\text{Working Directory} \\xrightarrow{\\text{add}} \\text{Staging} \\xrightarrow{\\text{commit}} \\text{Local Repo} \\xrightarrow{\\text{push}} \\text{Remote}",
      "legend": "• Branching: Bekerja pada fitur terpisah secara paralel.<br>• Merge/Pull Request: Menggabungkan kode dengan tinjauan (code review)."
    },
    "hints": {
      "concept": "Sistem kontrol versi (VCS) mencatat setiap riwayat commit, mencegah penimpaan file yang tidak disengaja, dan memfasilitasi penggabungan (merge).",
      "execution": "Pilihlah teknologi yang standar dipakai industri perangkat lunak untuk kolaborasi kode, yaitu Git."
    },
    "explanation": "Version Control System (seperti Git/GitHub/GitLab) menyediakan mekanisme isolasi cabang (branching), pelacakan riwayat commit, dan penggabungan kode (merge/PR) sehingga kolaborasi multi-programmer berlangsung aman dan teratur. Jawaban: D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-09",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Keamanan Aset Proyek & Kredensial",
    "type": "mcq",
    "questionHtml": "Seorang pengembang aplikasi harus menghubungkan programnya dengan layanan pembayaran pihak ketiga menggunakan API Secret Key dan kata sandi basis data. Praktik pengelolaan aset kode sumber yang paling aman saat proyek diunggah ke repositori Git publik adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menuliskan API Secret Key dan kata sandi secara langsung (hardcoded) di bagian paling atas file index utama."
      },
      {
        "key": "B",
        "text": "Menyimpan kredensial sensitif di dalam file environment (.env) dan mendaftarkan file .env tersebut ke dalam .gitignore."
      },
      {
        "key": "C",
        "text": "Mengunggah tangkapan layar berisi kata sandi basis data ke dalam file README.md agar mudah dibaca publik."
      },
      {
        "key": "D",
        "text": "Mengirimkan kata sandi melalui kolom komentar publik di media sosial proyek."
      },
      {
        "key": "E",
        "text": "Menamai file kode sumber utama dengan kata sandi basis data yang digunakan."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ENVIRONMENT VARIABLES & GITIGNORE",
      "latex": "\\text{Secrets in } \\texttt{.env} \\quad + \\quad \\text{Rule in } \\texttt{.gitignore: } \\texttt{.env} \\implies \\text{Zero Credential Leak}",
      "legend": "• .gitignore memberi tahu Git untuk mengabaikan file tertentu agar tidak pernah ter-commit atau ter-push ke server remote."
    },
    "hints": {
      "concept": "Kredensial rahasia (API key, token, DB password) tidak boleh di-hardcode di kode sumber publik, melainkan disimpan di variabel lingkungan (.env).",
      "execution": "Pilihlah kombinasi penyimpanan pada file .env dan pemfilteran dengan .gitignore."
    },
    "explanation": "Praktik keamanan baku adalah menyimpan kredensial pada file environment (.env) dan mendaftarkan .env ke dalam file .gitignore agar tidak terunggah ke repositori publik. Menulis kredensial di kode (hardcoding) sangat berbahaya karena rentan dicuri bot penyerang. Jawaban: B.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-10",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Prosedur Pengelolaan & Cadangan Aset",
    "type": "mcq",
    "questionHtml": "Dalam pengelolaan aset digital proyek perangkat lunak, risiko kehilangan data akibat kerusakan perangkat keras server dapat diminimalkan melalui prosedur …",
    "options": [
      {
        "key": "A",
        "text": "Menghapus log transaksi basis data setiap satu jam sekali."
      },
      {
        "key": "B",
        "text": "Menyimpan satu-satunya salinan basis data di partisi yang sama dengan file sementara (temp) sistem operasi."
      },
      {
        "key": "C",
        "text": "Menonaktifkan fitur autentikasi pengguna pada server basis data."
      },
      {
        "key": "D",
        "text": "Mengubah seluruh nama tabel basis data setiap hari secara manual."
      },
      {
        "key": "E",
        "text": "Melakukan pencadangan (backup) otomatis secara berkala ke lokasi penyimpanan terpisah serta menguji prosedur pemulihannya (restore)."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "STRATEGI CADANGAN DATA 3-2-1",
      "latex": "3 \\text{ Salinan Data} \\to 2 \\text{ Media Berbeda} \\to 1 \\text{ Salinan Off-site/Cloud}",
      "legend": "• Backup tanpa uji coba pemulihan (restore drill) tidak menjamin ketersediaan data saat terjadi disaster recovery."
    },
    "hints": {
      "concept": "Pencadangan rutin ke media atau lokasi terpisah serta pengujian pemulihan adalah fondasi kelangsungan bisnis (business continuity).",
      "execution": "Pilihlah opsi yang mencakup pencadangan berkala di lokasi berbeda dan verifikasi restore."
    },
    "explanation": "Untuk memitigasi risiko kerusakan fisik server atau bencana, tim wajib menjalankan pencadangan (backup) berkala ke lokasi fisik/cloud terpisah dan memverifikasi kelayakan prosedur restore secara teratur. Jawaban: E.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-11",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Lingkungan Sistem Operasi (CLI Linux)",
    "type": "mcq",
    "questionHtml": "Seorang pengembang gim menggunakan terminal sistem operasi berbasis Linux untuk menyiapkan struktur folder proyek baru. Perintah CLI yang tepat untuk membuat direktori bertingkat <code>src/assets/sprites</code> sekaligus adalah …",
    "options": [
      {
        "key": "A",
        "text": "rm -rf src/assets/sprites"
      },
      {
        "key": "B",
        "text": "mkdir -p src/assets/sprites"
      },
      {
        "key": "C",
        "text": "cat src/assets/sprites"
      },
      {
        "key": "D",
        "text": "ps aux src/assets/sprites"
      },
      {
        "key": "E",
        "text": "kill -9 src/assets/sprites"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "PERINTAH DASAR LINUX CLI",
      "latex": "\\texttt{mkdir -p [path/nested/dir]} \\implies \\text{Membuat direktori induk \& anak sekaligus}",
      "legend": "• \\texttt{-p} (parents): Tidak menghasilkan error jika folder sudah ada, dan membuat seluruh subfolder yang belum tersedia."
    },
    "hints": {
      "concept": "Perintah 'mkdir' (make directory) dengan flag '-p' (parents) membuat seluruh hirarki folder bertingkat dalam satu langkah.",
      "execution": "Pilihlah perintah pembuatan direktori dengan parameter pembuatan folder induk."
    },
    "explanation": "Perintah 'mkdir -p' (make directory parents) digunakan untuk membuat direktori bertingkat secara rekursif jika direktori induknya belum ada. 'rm -rf' untuk menghapus, 'cat' untuk membaca file, dan 'kill' untuk menghentikan proses. Jawaban: B.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-12",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Operasi & Hak Akses File",
    "type": "mcq",
    "questionHtml": "Seorang pengembang aplikasi web sedang menyiapkan proyek pada server lokal Linux untuk keperluan pengujian. Saat aplikasi diakses melalui browser, muncul pesan kesalahan berikut:<br><code>Permission denied: /var/www/html/index.php</code><br>Tindakan perbaikan yang paling tepat untuk mengatasi masalah tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Mengganti kabel jaringan UTP dengan serat optik."
      },
      {
        "key": "B",
        "text": "Memformat ulang seluruh partisi harddisk server."
      },
      {
        "key": "C",
        "text": "Mengubah hak akses (permission) atau kepemilikan (ownership) pada file/direktori proyek agar dapat dibaca oleh layanan web server."
      },
      {
        "key": "D",
        "text": "Menghapus browser pada komputer client dan memasang aplikasi desain grafis."
      },
      {
        "key": "E",
        "text": "Mengubah nama domain aplikasi menjadi alamat MAC Address."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "HAK AKSES FILE LINUX (POSIX PERMISSIONS)",
      "latex": "\\texttt{chmod [mode] file} \\quad | \\quad \\texttt{chown [user]:[group] file}",
      "legend": "• Error 'Permission denied' terjadi saat user proses web server (misal www-data/nginx) tidak memiliki hak baca (r) atau eksekusi (x) pada file."
    },
    "hints": {
      "concept": "Pesan 'Permission denied' menandakan user proses web server tidak memiliki hak izin akses baca/tulis terhadap file yang dituju.",
      "execution": "Pilihlah solusi yang mengoreksi hak akses (chmod) atau kepemilikan file (chown)."
    },
    "explanation": "Pesan 'Permission denied' merupakan indikasi masalah izin baca/eksekusi file pada level sistem operasi. Solusinya adalah menyesuaikan hak akses (chmod) atau kepemilikan file (chown) agar user web server (seperti www-data) dapat membaca file tersebut. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-13",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Infrastruktur & Addressing IPv4 Subnet",
    "type": "mcq",
    "questionHtml": "Cermati data konfigurasi jaringan lokal (LAN) pada infrastruktur pengembangan aplikasi web yang terhubung melalui satu Switch (tanpa Router/VLAN) berikut:<div class=\"net-spec-box\"><div class=\"net-spec-title\"><svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\"><rect x=\"2\" y=\"2\" width=\"20\" height=\"8\" rx=\"2\"/><rect x=\"2\" y=\"14\" width=\"20\" height=\"8\" rx=\"2\"/><line x1=\"6\" y1=\"6\" x2=\"6.01\" y2=\"6\"/><line x1=\"6\" y1=\"18\" x2=\"6.01\" y2=\"18\"/></svg>Topologi Switch LAN Server (Subnet /24)</div><div class=\"net-spec-list\"><div class=\"net-spec-item\">🖥️ <strong>Server Aplikasi:</strong> <span class=\"net-ip-badge\">192.168.10.10/24</span></div><div class=\"net-spec-item\">📁 <strong>File Storage Server:</strong> <span class=\"net-ip-badge\">192.168.10.15/24</span></div><div class=\"net-spec-item\">🗄️ <strong>Database Server:</strong> <span class=\"net-ip-badge\">[ Titik A ]</span></div></div></div>Agar Database Server pada Titik A dapat berkomunikasi langsung dengan Server Aplikasi dan File Storage Server dalam subnet yang sama, alamat IP yang paling tepat dikonfigurasi pada Titik A adalah …",
    "options": [
      {
        "key": "A",
        "text": "192.168.10.10/24"
      },
      {
        "key": "B",
        "text": "192.168.100.20/24"
      },
      {
        "key": "C",
        "text": "192.168.10.255/24"
      },
      {
        "key": "D",
        "text": "192.168.10.20/24"
      },
      {
        "key": "E",
        "text": "10.10.10.20/24"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "RENTANG HOST USABLE IPv4 /24",
      "latex": "\\text{Network: } 192.168.10.0 \\quad | \\quad \\text{Host: } 192.168.10.1 - 192.168.10.254 \\quad | \\quad \\text{Broadcast: } 192.168.10.255",
      "legend": "• IP tidak boleh bentrok (duplikat) dan tidak boleh menggunakan alamat Network (.0) atau Broadcast (.255)."
    },
    "hints": {
      "concept": "Pada subnet /24 (255.255.255.0), tiga oktet pertama harus sama persis (192.168.10.x) dan host ID harus unik serta bukan broadcast (.255).",
      "execution": "Pilihlah IP dengan network 192.168.10.x yang belum digunakan oleh server lain dan bukan alamat broadcast."
    },
    "explanation": "Pada subnet 192.168.10.0/24, rentang host yang valid adalah 192.168.10.1 hingga 192.168.10.254. Opsi A duplikat dengan Server Aplikasi, Opsi B dan E beda network, Opsi C adalah alamat broadcast. Maka IP yang tepat adalah 192.168.10.20/24. Jawaban: D.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-14",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Infrastruktur & Perangkat Jaringan",
    "type": "mcq",
    "questionHtml": "Tim pengembang berada pada jaringan lokal <code>192.168.1.0/24</code>, sedangkan server staging pengujian berada pada segmen jaringan berbeda yaitu <code>10.20.30.0/24</code>. Perangkat jaringan utama yang bertugas menghubungkan kedua jaringan berbeda tersebut dan meneruskan paket data berdasarkan alamat IP adalah …",
    "options": [
      {
        "key": "A",
        "text": "Router"
      },
      {
        "key": "B",
        "text": "Hub"
      },
      {
        "key": "C",
        "text": "Repeater"
      },
      {
        "key": "D",
        "text": "Konektor RJ-45"
      },
      {
        "key": "E",
        "text": "Crimping Tool"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "ROUTING LAYER 3 (NETWORK LAYER)",
      "latex": "\\text{Subnet A (192.168.1.0/24)} \\xleftrightarrow{\\quad\\text{ROUTER}\\quad} \\text{Subnet B (10.20.30.0/24)}",
      "legend": "• Switch/Hub menghubungkan perangkat dalam satu subnet (Layer 2).<br>• Router menghubungkan dua atau lebih subnet/jaringan yang berbeda (Layer 3)."
    },
    "hints": {
      "concept": "Perangkat yang bertugas melakukan routing (perutean paket) antar-segmen jaringan IP yang berbeda adalah Router.",
      "execution": "Pilihlah perangkat Layer 3 OSI yang memiliki kemampuan membaca tabel routing IP."
    },
    "explanation": "Router adalah perangkat jaringan Layer 3 yang berfungsi meneruskan paket data antar-jaringan/subnet yang berbeda berdasarkan IP Address. Switch/Hub bekerja pada jaringan lokal yang sama. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-15",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Arsitektur & Mekanisme TCP/IP",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi mobile mengambil data profil pengguna dari server melalui endpoint REST API menggunakan protokol HTTPS di atas transport TCP. Pernyataan yang tepat mengenai peran layer pada arsitektur TCP/IP dalam proses tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "HTTPS bekerja pada Network Access Layer untuk mengatur sinyal radio Wi-Fi."
      },
      {
        "key": "B",
        "text": "TCP bekerja pada Application Layer untuk merender tampilan CSS di layar ponsel."
      },
      {
        "key": "C",
        "text": "HTTPS bekerja pada Application Layer untuk pertukaran data terenkripsi, sedangkan TCP bekerja pada Transport Layer untuk menjamin pengiriman paket secara andal dan berurutan."
      },
      {
        "key": "D",
        "text": "IP bekerja pada Application Layer untuk menerjemahkan kueri SQL menjadi tabel HTML."
      },
      {
        "key": "E",
        "text": "Transport Layer hanya berfungsi menentukan warna kabel UTP yang digunakan."
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "MODEL 4-LAYER TCP/IP",
      "latex": "\\begin{aligned} \\text{Application} &: \\text{HTTPS, HTTP, DNS, SSH} \\\\ \\text{Transport} &: \\text{TCP (Reliable/Ordered), UDP (Fast/Lossy)} \\\\ \\text{Internet} &: \\text{IP (Addressing \\& Routing), ICMP} \\\\ \\text{Network Access} &: \\text{Ethernet, Wi-Fi, MAC Address} \\end{aligned}",
      "legend": "• TCP menjamin koneksi andal (handshake, ACK, retransmisi).<br>• HTTPS menyediakan pertukaran data terenkripsi SSL/TLS di layer aplikasi."
    },
    "hints": {
      "concept": "HTTPS adalah protokol tingkat aplikasi (Application Layer), sedangkan TCP adalah protokol transmisi handal (Transport Layer).",
      "execution": "Pilihlah opsi yang memetakan HTTPS ke Application Layer dan TCP ke Transport Layer dengan benar."
    },
    "explanation": "Dalam arsitektur TCP/IP, HTTPS berada pada Application Layer (mengatur enkripsi dan format data aplikasi web), sedangkan TCP berada pada Transport Layer (memastikan paket terkirim secara andal, tanpa corrupt, dan berurutan via 3-way handshake). Jawaban: C.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-16",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Struktur Data & Tipe Data Dasar",
    "type": "mcq",
    "questionHtml": "Seorang programmer gim sedang mendeklarasikan empat variabel untuk menyimpan data pemain:<br>1) <code>id_pemain = 1042</code><br>2) <code>nama_user = \"GarudaKnight\"</code><br>3) <code>skor_akurasi = 87.5</code><br>4) <code>status_aktif = True</code><br>Pasangan tipe data yang tepat secara berurutan untuk keempat variabel tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "String, Integer, Boolean, Float"
      },
      {
        "key": "B",
        "text": "Integer, Float, String, Boolean"
      },
      {
        "key": "C",
        "text": "Float, String, Integer, Boolean"
      },
      {
        "key": "D",
        "text": "Integer, String, Float, Boolean"
      },
      {
        "key": "E",
        "text": "Boolean, String, Float, Integer"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "KLASIFIKASI TIPE DATA PRIMITIF",
      "latex": "1042 \\in \\mathbb{Z} \\text{ (Integer)} \\quad | \\quad \\text{\"Text\"} \\in \\text{String} \\quad | \\quad 87.5 \\in \\mathbb{R} \\text{ (Float)} \\quad | \\quad \\text{True/False} \\in \\text{Boolean}",
      "legend": "• int: bilangan bulat.<br>• str: untaian karakter.<br>• float: bilangan desimal berkoma.<br>• bool: nilai logika kebenaran."
    },
    "hints": {
      "concept": "1042 adalah bilangan bulat (integer), \"GarudaKnight\" adalah teks (string), 87.5 berkoma (float), dan True adalah boolean.",
      "execution": "Cocokkan urutan 1 ke 4: Integer, String, Float, Boolean."
    },
    "explanation": "1042 bertipe Integer, \"GarudaKnight\" bertipe String, 87.5 bertipe Float (desimal), dan True bertipe Boolean. Urutan yang benar adalah Integer, String, Float, Boolean. Jawaban: D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-17",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Struktur Data & Tipe Data",
    "type": "mcq",
    "questionHtml": "Sebuah gim RPG membutuhkan struktur data untuk menyimpan ribuan katalog item yang dapat dicari secara instan berdasarkan kode unik item (contoh: <code>\"ITM-099\"</code> memetakan ke objek data <code>\"Pedang Naga\"</code>). Struktur data yang paling efisien untuk kebutuhan pencarian berbasis pasangan kunci-nilai (<em>key-value pair</em>) tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Variabel bertipe karakter tunggal (Char)"
      },
      {
        "key": "B",
        "text": "Dictionary / Hash Map"
      },
      {
        "key": "C",
        "text": "Antrean cetak (Print Spooler)"
      },
      {
        "key": "D",
        "text": "Konstanta bertipe Boolean"
      },
      {
        "key": "E",
        "text": "Komentar dokumentasi program"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "KEY-VALUE DATA STRUCTURE",
      "latex": "\\text{Hash}(\\text{Key}) \\xrightarrow{\\mathcal{O}(1)} \\text{Bucket Index} \\to \\text{Value Retrieval}",
      "legend": "• Dictionary / Hash Map memiliki kompleksitas pencarian rata-rata O(1) berdasarkan kunci unik."
    },
    "hints": {
      "concept": "Struktur data yang mengaitkan setiap 'key' (kunci unik) ke 'value' (nilai data) adalah Dictionary (di Python) atau Hash Map (di Java/C++).",
      "execution": "Pilihlah struktur data koleksi pasangan key-value."
    },
    "explanation": "Dictionary (Python) atau Hash Map (Java/C++) merupakan struktur data asosiatif yang menyimpan pasangan kunci-nilai (key-value) dengan akses pencarian instan rata-rata O(1). Jawaban: B.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-18",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Struktur Kontrol Program (Perulangan & Modulo)",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan program berikut!<br><pre><code>total = 0\nfor i in range(1, 7):\n    if i % 2 == 0:\n        total += i\nprint(total)</code></pre>Output yang dihasilkan ketika program di atas dijalankan adalah …",
    "options": [
      {
        "key": "A",
        "text": "6"
      },
      {
        "key": "B",
        "text": "10"
      },
      {
        "key": "C",
        "text": "12"
      },
      {
        "key": "D",
        "text": "15"
      },
      {
        "key": "E",
        "text": "21"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "TRACE PERULANGAN RANGE & MODULO",
      "latex": "i \\in \\{1, 2, 3, 4, 5, 6\\} \\quad \\land \\quad (i \\pmod 2 == 0) \\implies i \\in \\{2, 4, 6\\}",
      "legend": "• total = 2 + 4 + 6 = 12.<br>• range(1, 7) berhenti sebelum angka 7."
    },
    "hints": {
      "concept": "range(1, 7) menghasilkan bilangan 1 sampai 6. Kondisi i % 2 == 0 hanya menyaring bilangan genap.",
      "execution": "Jumlahkan semua nilai genap dari 1 sampai 6: 2 + 4 + 6."
    },
    "explanation": "Fungsi range(1, 7) melakukan iterasi untuk nilai i = 1, 2, 3, 4, 5, 6. Nilai yang memenuhi kondisi genap (i % 2 == 0) adalah 2, 4, dan 6. Akumulasi total = 2 + 4 + 6 = 12. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-19",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Modularisasi Program & Pemanggilan Fungsi",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program modular berikut!<br><pre><code class=\"language-python\">def hitung(a, b):\n    return a + b + 2\n\ndef proses(x):\n    return x * 2 + 1\n\n# Lengkapi baris 8 di bawah ini\n________________________\nprint(nilai)</code></pre>Agar output program menghasilkan angka <strong>11</strong>, maka pernyataan yang harus dilengkapi pada baris 8 adalah …",
    "options": [
      {
        "key": "A",
        "text": "nilai = proses(3)"
      },
      {
        "key": "B",
        "text": "nilai = hitung(5, 6)"
      },
      {
        "key": "C",
        "text": "nilai = proses(11)"
      },
      {
        "key": "D",
        "text": "nilai = proses(hitung(3, 0))"
      },
      {
        "key": "E",
        "text": "nilai = hitung(11, 0)"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "KOMPOSISI FUNGSI MATEMATIKA",
      "latex": "f(g(a, b)) \\implies \\text{hitung}(3, 0) = 3 + 0 + 2 = 5 \\implies \\text{proses}(5) = 5 \\times 2 + 1 = 11",
      "legend": "• Nilai kembalian fungsi dalam dievaluasi terlebih dahulu sebelum dilewatkan ke fungsi luar."
    },
    "hints": {
      "concept": "Uji setiap opsi dengan mensubstitusikan nilai parameter ke dalam definisi fungsi hitung dan proses.",
      "execution": "Hitung: hitung(3, 0) = 3 + 0 + 2 = 5. Lalu proses(5) = 5 * 2 + 1 = 11."
    },
    "explanation": "Pada opsi D: hitung(3, 0) menghasilkan 3 + 0 + 2 = 5. Kemudian proses(5) menghasilkan 5 * 2 + 1 = 11. Opsi A menghasilkan 7, Opsi B menghasilkan 13, Opsi C menghasilkan 23, Opsi E menghasilkan 13. Jawaban yang tepat adalah D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-20",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Lingkup Variabel (Variable Scope)",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode berikut!<br><pre><code>def hitung_skor(poin_dasar):\n    bonus = 50\n    return poin_dasar + bonus\n\nhasil = hitung_skor(100)\nprint(bonus)</code></pre>Ketika potongan program di atas dijalankan, hal yang akan terjadi pada baris <code>print(bonus)</code> adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menampilkan angka 50 tanpa kesalahan."
      },
      {
        "key": "B",
        "text": "Menampilkan angka 150 tanpa kesalahan."
      },
      {
        "key": "C",
        "text": "Menampilkan angka 100 tanpa kesalahan."
      },
      {
        "key": "D",
        "text": "Menampilkan teks \"poin_dasar + bonus\"."
      },
      {
        "key": "E",
        "text": "Menghasilkan pesan kesalahan (NameError) karena variabel bonus bersifat lokal di dalam fungsi hitung_skor()."
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "LOCAL VS GLOBAL SCOPE",
      "latex": "\\text{Variable inside function} \\implies \\text{Local Scope} \\implies \\text{Inaccessible from global scope}",
      "legend": "• Variabel yang dideklarasikan di dalam blok fungsi dialokasikan pada stack frame lokal dan dihapus saat fungsi selesai."
    },
    "hints": {
      "concept": "Variabel 'bonus' berada di dalam fungsi (local scope). Lingkup global di luar fungsi tidak mengenali variabel tersebut.",
      "execution": "Memanggil variabel lokal di luar lingkup fungsi akan memicu NameError."
    },
    "explanation": "Variabel 'bonus' didefinisikan di dalam fungsi hitung_skor, sehingga memiliki lingkup lokal (local scope). Saat interpreter mencoba mengakses variabel tersebut di lingkup global melalui print(bonus), sistem akan melempar pesan kesalahan NameError: name 'bonus' is not defined. Jawaban: E.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Konsep Dasar OOP (Class & Object)",
    "type": "mcq",
    "questionHtml": "Dalam paradigma Pemrograman Berorientasi Objek (OOP), perbedaan mendasar antara <strong>Class</strong> dan <strong>Object</strong> adalah …",
    "options": [
      {
        "key": "A",
        "text": "Class adalah nilai kembalian fungsi, sedangkan Object adalah operator logika."
      },
      {
        "key": "B",
        "text": "Class adalah cetak biru (blueprint) yang mendefinisikan atribut dan method, sedangkan Object adalah instansiasi nyata dari class tersebut."
      },
      {
        "key": "C",
        "text": "Class hanya dapat menyimpan tipe data Boolean, sedangkan Object hanya menyimpan tipe data String."
      },
      {
        "key": "D",
        "text": "Object dibuat terlebih dahulu di dalam kode sumber sebelum Class didefinisikan."
      },
      {
        "key": "E",
        "text": "Class dan Object hanya dapat digunakan pada bahasa pemrograman tingkat mesin (Assembly)."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "ANALOGI CLASS VS OBJECT",
      "latex": "\\text{Class (Blueprint / Cetak Biru)} \\xrightarrow{\\text{Instansiasi}} \\text{Object (Instans / Rumah Nyata)}",
      "legend": "• Class: Struktur konsep, definisi atribut dan method.<br>• Object: Entitas konkrit di memori dengan nilai state masing-masing."
    },
    "hints": {
      "concept": "Class adalah skema/rancangan cetak biru (seperti denah rumah), sedangkan Object adalah wujud nyata hasil cetakan (rumah jadi).",
      "execution": "Pilihlah definisi yang menyebutkan Class sebagai blueprint dan Object sebagai instansiasi nyata."
    },
    "explanation": "Class merupakan blueprint atau template yang mendefinisikan variabel (atribut) dan perilaku (method), sedangkan Object adalah wujud instansiasi konkrit dari class tersebut yang menempati memori dengan nilai atribut tersendiri. Jawaban: B.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-22",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Instansiasi Class & Object",
    "type": "mcq",
    "questionHtml": "Perhatikan definisi class untuk karakter gim berikut!<br><pre><code>class Karakter:\n    def __init__(self, nama, hp):\n        self.nama = nama\n        self.hp = hp\n    def info(self):\n        return f\"{self.nama} (HP: {self.hp})\"</code></pre>Cara yang tepat untuk membuat objek baru bernama <code>hero1</code> dari class <code>Karakter</code> dengan nama <code>\"Arjuna\"</code> dan hp bernilai <code>100</code> adalah …",
    "options": [
      {
        "key": "A",
        "text": "hero1 = Karakter.info(\"Arjuna\", 100)"
      },
      {
        "key": "B",
        "text": "hero1 = __init__(\"Arjuna\", 100)"
      },
      {
        "key": "C",
        "text": "hero1 = Karakter(\"Arjuna\", 100)"
      },
      {
        "key": "D",
        "text": "class hero1 = Karakter(100)"
      },
      {
        "key": "E",
        "text": "hero1 = self.nama(\"Arjuna\")"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "SINTAKS INSTANSIASI OBJEK (PYTHON)",
      "latex": "\\texttt{nama\\_objek = NamaClass(argumen1, argumen2)}",
      "legend": "• Memanggil NamaClass(...) secara otomatis mengeksekusi constructor \\texttt{__init__} untuk menginisialisasi atribut objek."
    },
    "hints": {
      "concept": "Instansiasi dilakukan dengan memanggil nama kelas seperti fungsi, diikuti argumen yang sesuai dengan parameter constructor __init__.",
      "execution": "Pilihlah sintaks hero1 = Karakter(\"Arjuna\", 100)."
    },
    "explanation": "Di Python, membuat objek dilakukan dengan memanggil nama class diikuti tanda kurung yang berisi argumen constructor: hero1 = Karakter(\"Arjuna\", 100). Constructor __init__ akan terpanggil secara otomatis di latar belakang. Jawaban: C.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-23",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
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
      "title": "PRINSIP ENKAPSULASI & DATA HIDING",
      "latex": "\\text{Private Attribute } (\\texttt{\\_saldo}) \\quad + \\quad \\text{Setter: } \\texttt{set\\_saldo(val) if val } \\ge 0 \\implies \\text{Data Integrity}",
      "legend": "• Enkapsulasi menyembunyikan detail internal objek dan hanya mengizinkan modifikasi melalui method terkontrol (getter & setter)."
    },
    "hints": {
      "concept": "Enkapsulasi melindungi atribut dari manipulasi ilegal dengan menjadikannya private dan menyediakan method setter dengan aturan validasi.",
      "execution": "Pilihlah penerapan atribut private disertai method getter dan setter bervalidasi."
    },
    "explanation": "Prinsip enkapsulasi mengharuskan data sensitif disembunyikan (private) dan hanya dapat diakses atau diubah melalui method getter dan setter. Pada setter, kode validasi disematkan guna memastikan nilai saldo tidak pernah menjadi negatif. Jawaban: A.",
    "isDiagnostic": true
  },
  {
    "id": "rpl-lat-e-24",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Access Modifier (Protected Scope)",
    "type": "mcq",
    "questionHtml": "Dalam perancangan class berorientasi objek, seorang programmer ingin agar atribut <code>kecepatan_maks</code> dapat diakses langsung oleh class <code>Kendaraan</code> itu sendiri maupun oleh subclass turunannya (seperti <code>Mobil</code> dan <code>Motor</code>), tetapi tidak ditujukan untuk diakses bebas oleh bagian luar yang tidak berelasi. Access modifier yang paling sesuai untuk kebutuhan tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "private"
      },
      {
        "key": "B",
        "text": "global"
      },
      {
        "key": "C",
        "text": "static konstanta luar"
      },
      {
        "key": "D",
        "text": "protected"
      },
      {
        "key": "E",
        "text": "anonymous"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "TABEL ACCESS MODIFIERS",
      "latex": "\\begin{array}{|l|c|c|c|} \\hline \\textbf{Modifier} & \\textbf{Same Class} & \\textbf{Subclass} & \\textbf{World} \\\\ \\hline \\text{public} & \\checkmark & \\checkmark & \\checkmark \\\\ \\hline \\text{protected} & \\checkmark & \\checkmark & \\times \\\\ \\hline \\text{private} & \\checkmark & \\times & \\times \\\\ \\hline \\end{array}",
      "legend": "• protected: dapat diakses oleh kelas itu sendiri dan kelas-kelas keturunannya (subclasses)."
    },
    "hints": {
      "concept": "Protected mengizinkan akses bagi kelas induk dan kelas turunannya (inheritance hierarchy), tetapi membatasi akses dari luar.",
      "execution": "Pilihlah access modifier 'protected'."
    },
    "explanation": "Access modifier 'protected' dirancang secara khusus untuk relasi pewarisan: anggota kelas dapat diakses oleh kelas tempat ia dideklarasikan serta kelas-kelas turunannya (subclass), namun terlindung dari akses langsung kode luar. Jawaban: D.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-e-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Pewarisan (Inheritance & Constructor)",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode superclass berikut!<br><pre><code>class Karakter:\n    def __init__(self, nama, hp):\n        self.nama = nama\n        self.hp = hp</code></pre>Untuk membuat subclass <code>MusuhBoss</code> yang mewarisi <code>Karakter</code> serta menambahkan atribut baru <code>elemen</code>, deklarasi kode yang paling tepat adalah …",
    "options": [
      {
        "key": "A",
        "text": "class MusuhBoss:\n    Karakter(nama, hp)"
      },
      {
        "key": "B",
        "text": "def MusuhBoss(Karakter):\n    return nama + hp"
      },
      {
        "key": "C",
        "text": "class MusuhBoss(Karakter):\n    def __init__(self, nama, hp, elemen):\n        super().__init__(nama, hp)\n        self.elemen = elemen"
      },
      {
        "key": "D",
        "text": "class Karakter(MusuhBoss):\n    self.elemen = elemen"
      },
      {
        "key": "E",
        "text": "MusuhBoss = super(Karakter.elemen)"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "SINTAKS INHERITANCE DENGAN SUPER()",
      "latex": "\\begin{aligned} &\\textbf{class } \\text{SubClass}(\\text{SuperClass}): \\\\ &\\quad \\textbf{def } \\text{\\_\\_init\\_\\_}(\\text{self}, a, b, c): \\\\ &\\qquad \\text{super}().\\text{\\_\\_init\\_\\_}(a, b) \\\\ &\\qquad \\text{self}.c = c \\end{aligned}",
      "legend": "• super().__init__(...) mendelegasikan inisialisasi atribut bawaan ke constructor superclass."
    },
    "hints": {
      "concept": "Subclass mewarisi superclass dengan sintaks class Sub(Super):. Konstruktor subclass memanggil super().__init__() untuk mewarisi atribut induk.",
      "execution": "Pilihlah Opsi C yang mendefinisikan class MusuhBoss(Karakter) dengan pemanggilan super().__init__(nama, hp)."
    },
    "explanation": "Deklarasi class turunan dilakukan dengan menuliskan superclass di dalam kurung: class MusuhBoss(Karakter):. Di dalam constructor __init__, pemanggilan super().__init__(nama, hp) wajib dilakukan untuk menginisialisasi atribut induk nama dan hp sebelum menambahkan self.elemen = elemen. Jawaban: C.",
    "isDiagnostic": false
  }
]
