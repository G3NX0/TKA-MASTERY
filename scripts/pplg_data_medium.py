# -*- coding: utf-8 -*-
MEDIUM_QUESTIONS = [
  {
    "id": "rpl-lat-m-01",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Kewirausahaan & HAKI Perangkat Lunak",
    "type": "mcq",
    "questionHtml": "Sebuah tim pengembang SMK merilis modul perpustakaan kode berlisensi <strong>GNU General Public License (GPL) v3</strong>. Sebuah perusahaan rintisan (startup) bermaksud mengintegrasikan modul tersebut ke dalam produk komersial mereka. Berdasarkan karakteristik lisensi GPL v3, konsekuensi hukum yang WAJIB ditaati perusahaan tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Perusahaan bebas menutup seluruh kode sumber produk komersialnya tanpa kewajiban apa pun asalkan membayar royalti."
      },
      {
        "key": "B",
        "text": "Perusahaan wajib merilis seluruh kode sumber produk komersial turunannya ke publik dengan lisensi yang sama (copyleft)."
      },
      {
        "key": "C",
        "text": "Perusahaan harus menghapus nama pencipta asli dari berkas dokumentasi agar tidak terjadi konflik hak cipta."
      },
      {
        "key": "D",
        "text": "Modul GPL sama sekali tidak boleh digunakan untuk tujuan bisnis atau operasional organisasi apa pun."
      },
      {
        "key": "E",
        "text": "Hak cipta modul otomatis berpindah menjadi milik perusahaan begitu kode diunduh."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "SOFTWARE LICENSING: COPYLEFT VS PERMISSIVE",
      "latex": "\\text{GPL (Viral Copyleft)} \\implies \\text{Derived Works MUST be Open Source under GPL}",
      "legend": "• GPL (Copyleft): Karya turunan wajib open source berlisensi setara.<br>• MIT / Apache / BSD (Permissive): Boleh dijadikan proprietary tertutup dengan tetap menyertakan hak cipta asli."
    },
    "hints": {
      "concept": "Lisensi GPL bersifat 'viral copyleft'. Karya turunan atau aplikasi yang menggabungkan kode GPL wajib membuka kode sumbernya di bawah lisensi GPL yang sama.",
      "execution": "Pilihlah opsi yang menyebutkan kewajiban menyertakan dan membuka kode sumber produk turunan di bawah lisensi setara."
    },
    "explanation": "Karakteristik utama lisensi GNU GPL (General Public License) adalah sifat copyleft (timbal balik), yaitu setiap perangkat lunak turunan yang mengintegrasikan kode berlisensi GPL wajib mendistribusikan kode sumbernya secara terbuka di bawah lisensi yang sama jika dirilis ke publik. Jawaban: B.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-02",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Manajemen Proyek Agile/Scrum",
    "type": "mcq",
    "questionHtml": "Dalam sesi <em>Sprint Planning</em> pada pengembangan perangkat lunak metode Scrum, tim pengembang melakukan estimasi beban kerja menggunakan teknik <em>Planning Poker</em>. Jika terjadi perbedaan poin estimasi yang sangat mencolok antar-programmer (misalnya satu developer memberi 2 poin sedangkan developer lain memberi 13 poin), tindakan yang paling tepat dilakukan adalah …",
    "options": [
      {
        "key": "A",
        "text": "Langsung mengambil angka rata-rata hitung matematis dari kedua nilai tersebut tanpa diskusi."
      },
      {
        "key": "B",
        "text": "Memberikan kesempatan kepada pemberi estimasi terendah dan tertinggi untuk menjelaskan asumsi dan kompleksitas teknisnya sebelum estimasi ulang."
      },
      {
        "key": "C",
        "text": "Scrum Master secara sepihak memaksakan angka estimasi yang sesuai dengan tenggat waktu pimpinan."
      },
      {
        "key": "D",
        "text": "Menghapus user story tersebut dari Product Backlog karena dianggap tidak layak dikerjakan."
      },
      {
        "key": "E",
        "text": "Menyerahkan penentuan poin kepada Product Owner karena memiliki otoritas penuh atas bisnis."
      }
    ],
    "formulaHud": {
      "title": "AGILE ESTIMATION CONVERGENCE",
      "latex": "\\Delta_{\\text{Story Points}} > \\text{Threshold} \\implies \\text{Discussion (Min vs Max)} \\to \\text{Re-estimate}",
      "legend": "• Planning Poker mengungkap perbedaan persepsi kompleksitas & risiko teknis.<br>• PO menjelaskan kriteria penerimaan; Dev Team berdiskusi untuk mencapai konsensus."
    },
    "hints": {
      "concept": "Perbedaan estimasi ekstrem menunjukkan adanya asumsi teknis atau risiko tersembunyi yang belum diketahui salah satu pihak.",
      "execution": "Pilihlah langkah kolaboratif di mana kedua pihak yang memberi nilai ekstrem mendiskusikan asumsi mereka untuk mencapai konsensus tim."
    },
    "explanation": "Dalam Planning Poker, perbedaan nilai estimasi yang ekstrem (misalnya 2 vs 13) menandakan adanya gap pemahaman: pihak yang memberi nilai 2 mungkin melihat solusi sederhana yang belum disadari orang lain, atau pihak yang memberi 13 menyadari adanya risiko teknis berat. Diskusi antara nilai terendah dan tertinggi dilakukan untuk menyelaraskan asumsi sebelum putaran voting ulang. Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-m-03",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Software Quality Assurance (SQA) & Mutu",
    "type": "mcq",
    "questionHtml": "Sebuah tim rekayasa perangkat lunak menerapkan prinsip <em>Continuous Integration / Continuous Deployment (CI/CD)</em>. Tahap <em>automated unit testing</em> dan <em>static code analysis</em> selalu dijalankan setiap kali ada pull request baru. Tujuan utama menempatkan pengujian otomatis di awal alur pipeline (<em>shift-left testing</em>) adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menggantikan peran seluruh pengembang manusia dengan kecerdasan buatan."
      },
      {
        "key": "B",
        "text": "Menemukan dan memperbaiki cacat program (bug) sedini mungkin saat biaya perbaikannya masih paling rendah."
      },
      {
        "key": "C",
        "text": "Menghilangkan kebutuhan dokumentasi teknis dan arsitektur sistem secara total."
      },
      {
        "key": "D",
        "text": "Menunda waktu peluncuran aplikasi ke pasar agar pelanggan merasa produk lebih eksklusif."
      },
      {
        "key": "E",
        "text": "Mengharuskan server produksi dimatikan secara total selama proses pengujian berlangsung."
      }
    ],
    "formulaHud": {
      "title": "COST OF QUALITY: SHIFT-LEFT TESTING",
      "latex": "\\text{Cost}(\\text{Bug Discovery}) \\propto \\text{Stage of SDLC}: \\quad \\text{Dev} \\ll \\text{QA} \\ll \\text{Staging} \\lll \\text{Production}",
      "legend": "• Menemukan bug di tahap pengkodean (Unit Test): Biaya perbaikan 1x.<br>• Menemukan bug setelah rilis ke produksi: Biaya perbaikan bisa mencapai 30x–100x."
    },
    "hints": {
      "concept": "Prinsip shift-left testing berorientasi pada pencegahan cacat sejak awal siklus pengkodean.",
      "execution": "Pilihlah jawaban yang menyoroti efisiensi biaya dan deteksi dini bug sebelum mencapai tahap rilis."
    },
    "explanation": "Prinsip Shift-Left Testing menggeser pengujian ke tahap awal siklus pengembangan. Menurut riset rekayasa perangkat lunak (Boehm & Basili), biaya memperbaiki cacat program yang ditemukan pada tahap koding/unit test jauh lebih murah hingga puluhan kali lipat dibandingkan jika bug tersebut lolos sampai lingkungan produksi. Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-m-04",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Profesi & Technopreneurship PPLG",
    "type": "mcq",
    "questionHtml": "Dalam startup teknologi bidang perangkat lunak, produk awal yang dirilis ke pasar dengan fitur paling mendasar tetapi sudah mampu menyelesaikan masalah inti pengguna serta memvalidasi hipotesis bisnis dikenal sebagai …",
    "options": [
      {
        "key": "A",
        "text": "Minimum Viable Product (MVP)"
      },
      {
        "key": "B",
        "text": "Final Enterprise Release"
      },
      {
        "key": "C",
        "text": "Deprecated Legacy System"
      },
      {
        "key": "D",
        "text": "Proof of Hardware Concept"
      },
      {
        "key": "E",
        "text": "Disposable Throwaway Script"
      }
    ],
    "formulaHud": {
      "title": "LEAN STARTUP METHODOLOGY",
      "latex": "\\text{Build (MVP)} \\to \\text{Measure (User Feedback)} \\to \\text{Learn (Pivot or Persevere)}",
      "legend": "• MVP: Versi produk dengan fitur esensial minimum untuk menguji respon pasar nyata dengan biaya & waktu seminimal mungkin."
    },
    "hints": {
      "concept": "Istilah ini dipopulerkan oleh metodologi Lean Startup untuk menguji produk secara cepat dan terukur.",
      "execution": "Pilihlah istilah yang merupakan singkatan dari versi produk minimum yang berfungsi layak."
    },
    "explanation": "Minimum Viable Product (MVP) adalah versi awal produk perangkat lunak yang hanya memuat fitur-fitur esensial utama untuk menyelesaikan masalah spesifik pengguna dan mengumpulkan masukan nyata secara cepat dengan sumber daya seminimal mungkin. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-05",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Manajemen Proyek & Budaya Mutu",
    "type": "mcq",
    "questionHtml": "Pada akhir setiap Sprint, tim Scrum mengadakan pertemuan khusus berdurasi 1–2 jam untuk mengevaluasi proses kerja internal tim, menemukan hal-hal yang berjalan baik, hambatan komunikasi, serta merumuskan aksi perbaikan konkret untuk Sprint berikutnya. Pertemuan ini disebut …",
    "options": [
      {
        "key": "A",
        "text": "Daily Standup Meeting"
      },
      {
        "key": "B",
        "text": "Sprint Retrospective"
      },
      {
        "key": "C",
        "text": "Product Backlog Refinement"
      },
      {
        "key": "D",
        "text": "Sprint Review bersama Klien"
      },
      {
        "key": "E",
        "text": "Architecture Review Board"
      }
    ],
    "formulaHud": {
      "title": "SCRUM CEREMONIES: REVIEW VS RETROSPECTIVE",
      "latex": "\\text{Sprint Review (Focus on Product Increment)} \\quad \\mid \\quad \\text{Sprint Retrospective (Focus on Team Process \\& Culture)}",
      "legend": "• Sprint Review: Demonstrasi fitur produk ke pemangku kepentingan.<br>• Sprint Retrospective: Refleksi internal cara kerja tim (Start, Stop, Continue)."
    },
    "hints": {
      "concept": "Bedakan antara evaluasi hasil produk (Review) dengan evaluasi proses dan cara kerja tim (Retrospective).",
      "execution": "Pilihlah seremoni yang fokus utamanya adalah perbaikan proses kerja dan hubungan internal tim pengembang."
    },
    "explanation": "Sprint Retrospective adalah seremoni Scrum di mana seluruh tim pengembang melakukan refleksi internal mengenai cara kerja, alat, komunikasi, dan relasi selama Sprint yang baru selesai, guna merancang rencana aksi peningkatan mutu kerja pada Sprint berikutnya. Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-m-06",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Pengelolaan Aset Digital & Version Control",
    "type": "mcq",
    "questionHtml": "Dua pengembang perangkat lunak mengerjakan modul yang sama pada cabang (branch) berbeda. Saat dilakukan penggabungan cabang menggunakan perintah <code>git merge feature-pembayaran</code>, Git menampilkan pesan:<br><pre><code>CONFLICT (content): Merge conflict in controllers/payment.py\nAutomatic merge failed; fix conflicts and then commit the result.</code></pre>Langkah teknis yang benar dan aman untuk menyelesaikan masalah tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menghapus folder `.git` agar seluruh riwayat konflik hilang dan repositori menjadi bersih."
      },
      {
        "key": "B",
        "text": "Membuka file `payment.py`, menganalisis penanda konflik (`<<<<<<<`, `=======`, `>>>>>>>`), memilih/menggabungkan baris kode yang benar, menyimpan file, lalu menjalankan `git add` dan `git commit`."
      },
      {
        "key": "C",
        "text": "Mematikan paksa komputer server agar Git membatalkan merge secara otomatis tanpa jejak."
      },
      {
        "key": "D",
        "text": "Menjalankan perintah `git push --force` ke server produksi agar konflik tertimpa secara otomatis."
      },
      {
        "key": "E",
        "text": "Mengganti nama ekstensi file `payment.py` menjadi `payment.txt` agar Git tidak mengenali file kode tersebut."
      }
    ],
    "formulaHud": {
      "title": "GIT CONFLICT RESOLUTION WORKFLOW",
      "latex": "\\text{Conflict Markers} \\to \\text{Manual Resolution} \\to \\texttt{git add <file>} \\to \\texttt{git commit -m \"fix conflict\"}",
      "legend": "• <<<<<<< HEAD: Perubahan di cabang saat ini.<br>• =======: Pembatas konflik.<br>• >>>>>>> branch: Perubahan dari cabang yang digabungkan."
    },
    "hints": {
      "concept": "Konflik Git terjadi jika baris file yang sama diubah secara berbeda oleh dua commit. Programmer harus memutuskan logika mana yang dipertahankan.",
      "execution": "Pilihlah urutan: periksa penanda konflik, selesaikan manual, tandai selesai dengan `git add`, dan rekam dengan `git commit`."
    },
    "explanation": "Langkah standar menyelesaikan Git merge conflict adalah memeriksa file yang berkonflik, menyunting penanda konflik (`<<<<<<<`, `=======`, `>>>>>>>`) untuk memastikan logika kode yang benar tetap utuh, lalu menandai file dengan `git add payment.py` dan membuat commit penyelesaian menggunakan `git commit`. Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-m-07",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Keamanan Aset Proyek & Kredensial",
    "type": "mcq",
    "questionHtml": "Dalam pengembangan web, file <code>.env</code> digunakan untuk menyimpan variabel lingkungan rahasia seperti kunci API, token OAuth, dan kata sandi basis data. Agar file sensitif ini tidak terunggah ke repositori publik (GitHub/GitLab), tindakan pencegahan standar industri yang wajib dilakukan adalah …",
    "options": [
      {
        "key": "A",
        "text": "Mencantumkan nama file `.env` di dalam berkas konfigurasi `.gitignore` sejak inisialisasi awal proyek."
      },
      {
        "key": "B",
        "text": "Mengubah seluruh kata sandi menjadi teks kosong setiap kali programmer melakukan `git push`."
      },
      {
        "key": "C",
        "text": "Mengompresi file `.env` menjadi file ZIP dengan kata sandi sederhana."
      },
      {
        "key": "D",
        "text": "Menyalin file `.env` ke folder `node_modules` agar diabaikan sistem operasi."
      },
      {
        "key": "E",
        "text": "Mengunggah file `.env` ke branch khusus yang diberi nama 'secret-branch'."
      }
    ],
    "formulaHud": {
      "title": "CREDENTIAL SECURITY: GITIGNORE PATTERN",
      "latex": "\\texttt{.gitignore} \\ni \\texttt{.env} \\implies \\text{Secret Keys Excluded from Version Control Tracking}",
      "legend": "• Praktik baik: Sertakan `.env.example` (template kosong tanpa rahasia) di repositori.<br>• File `.env` asli tidak boleh pernah berada dalam pohon commit Git."
    },
    "hints": {
      "concept": "File `.gitignore` memberi instruksi kepada Git untuk tidak melacak atau menyertakan file/folder tertentu ke dalam staging area.",
      "execution": "Pilihlah konfigurasi yang memanfaatkan file `.gitignore` untuk mencegah pelacakan berkas rahasia."
    },
    "explanation": "Menambahkan baris `.env` ke dalam file `.gitignore` memastikan bahwa Git tidak akan pernah melacak atau mengunggah file yang berisi kredensial rahasia ke repositori remote, mencegah kebocoran data sensitif ke publik. Sebagai gantinya, tim biasanya menyertakan `.env.example` sebagai referensi struktur konfigurasi. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-08",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "K3LH Lingkungan TI & Ergonomi",
    "type": "mcq",
    "questionHtml": "Seorang programmer yang bekerja 8–10 jam sehari di depan komputer sering mengeluhkan rasa pegal, nyeri tajam, dan mati rasa pada pergelangan tangan serta jari-jari tangan. Gangguan kesehatan akibat gerakan repetitif dan posisi pergelangan tangan yang menekan meja secara tidak ergonomis ini dikenal secara medis sebagai …",
    "options": [
      {
        "key": "A",
        "text": "Carpal Tunnel Syndrome (CTS)"
      },
      {
        "key": "B",
        "text": "Tinnitus Akut"
      },
      {
        "key": "C",
        "text": "Insomnia Degeneratif"
      },
      {
        "key": "D",
        "text": "Skoliosis Struktural"
      },
      {
        "key": "E",
        "text": "Vertigo Paroksismal"
      }
    ],
    "formulaHud": {
      "title": "ERGONOMI PROGRAMMER: REPETITIVE STRAIN INJURY",
      "latex": "\\text{Sudut Pergelangan} \\approx 180^{\\circ} \\text{ (Netral)} \\implies \\text{Pencegahan Tekanan Saraf Medianus (CTS)}",
      "legend": "• Carpal Tunnel Syndrome: Tertekannya saraf medianus di pergelangan tangan akibat mengetik terus-menerus tanpa penopang ergonomis."
    },
    "hints": {
      "concept": "Sindrom lorong karpal menyerang pergelangan tangan akibat penekanan saraf medianus dalam waktu berkepanjangan.",
      "execution": "Pilihlah istilah medis untuk gangguan saraf pergelangan tangan pada pengguna komputer (singkatan CTS)."
    },
    "explanation": "Carpal Tunnel Syndrome (CTS) adalah gangguan ergonomis yang umum menyerang pengembang perangkat lunak akibat penekanan saraf medianus pada lorong karpal di pergelangan tangan, dipicu oleh mengetik dalam durasi panjang dengan sudut tangan yang tidak netral. Pencegahannya melibatkan penggunaan wrist rest dan keyboard ergonomis. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-09",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Prosedur Pengelolaan & Strategi Backup",
    "type": "mcq",
    "questionHtml": "Strategi cadangan data (backup) standar internasional yang diterapkan pada pusat data industri perangkat lunak adalah <strong>Aturan 3-2-1</strong>. Makna teknis yang benar dari angka 3, 2, dan 1 dalam aturan tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Membuat 3 salinan data, disimpan pada 2 jenis media penyimpanan berbeda, dengan 1 salinan berada di lokasi terpisah (off-site / cloud)."
      },
      {
        "key": "B",
        "text": "Melakukan backup setiap 3 hari sekali, menggunakan 2 jenis kata sandi, dan dikerjakan oleh 1 orang teknisi."
      },
      {
        "key": "C",
        "text": "Menyimpan data di 3 harddisk internal komputer yang sama selama 2 tahun dan menghapus 1 salinan lama."
      },
      {
        "key": "D",
        "text": "Membagi file menjadi 3 partisi, menyalinnya ke 2 folder lokal, dan mengompresnya 1 kali."
      },
      {
        "key": "E",
        "text": "Mengharuskan sistem di-restart 3 kali, diperiksa oleh 2 manajer, sebelum 1 file dipindahkan."
      }
    ],
    "formulaHud": {
      "title": "DATA RESILIENCE: ATURAN BACKUP 3-2-1",
      "latex": "3\\text{ Salinan Data} \\quad \\to \\quad 2\\text{ Media Berbeda (e.g. SSD \\& NAS)} \\quad \\to \\quad 1\\text{ Off-site (Cloud/DRC)}",
      "legend": "• Menjamin pemulihan data (Disaster Recovery) meskipun server lokal mengalami kebakaran, pencurian, atau serangan ransomware."
    },
    "hints": {
      "concept": "Aturan 3-2-1 menjamin redundansi data di media fisik lokal berbeda dan salinan aman di luar lokasi fisik gedung (cloud/off-site).",
      "execution": "Pilihlah jawaban yang merinci 3 salinan data, 2 media berbeda, dan 1 salinan off-site."
    },
    "explanation": "Aturan Backup 3-2-1 adalah praktik terbaik pemulihan bencana (Disaster Recovery): simpan minimal 3 salinan data (1 data primer + 2 backup), simpan salinan pada minimal 2 media teknologi berbeda (misalnya SSD server lokal dan storage server NAS), serta letakkan minimal 1 salinan di lokasi fisik terpisah (off-site seperti cloud storage). Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-10",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Budaya Kerja 5S/5R dalam Lingkungan RPL",
    "type": "mcq",
    "questionHtml": "Penerapan budaya kerja industri <strong>5S / 5R</strong> (Ringkas, Rapi, Resik, Rawat, Rajin) tidak hanya berlaku pada kebersihan fisik laboratorium, melainkan juga pada manajemen repositori perangkat lunak. Praktik di bawah ini yang mencerminkan prinsip <strong>Ringkas (Seiri / Sort)</strong> pada manajemen kode program adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menghapus kode yang sudah tidak dipakai (dead code), variabel yang tidak digunakan, serta cabang repositori sementara (feature branch) yang sudah selesai di-merge."
      },
      {
        "key": "B",
        "text": "Mengatur indentasi seluruh baris kode menggunakan spasi ganda secara manual."
      },
      {
        "key": "C",
        "text": "Menulis komentar penjelasan pada setiap kata kunci program tanpa kecuali."
      },
      {
        "key": "D",
        "text": "Menyimpan seluruh file kode, berkas instalasi, dan file musik programmer di desktop komputer kerja."
      },
      {
        "key": "E",
        "text": "Membiarkan semua pesan error debug tetap aktif pada server rilis produksi."
      }
    ],
    "formulaHud": {
      "title": "BUDAYA INDUSTRI: 5S PADA SOFTWARE ENGINEERING",
      "latex": "\\text{Seiri (Ringkas)} \\implies \\text{Pilah \\& Singkirkan Elemen Tak Berguna (Dead Code / Stale Branches)}",
      "legend": "• Seiri (Ringkas): Buang yang tidak terpakai.<br>• Seiton (Rapi): Susun modul teratur.<br>• Seiso (Resik): Bersihkan linting & warnings.<br>• Seiketsu (Rawat): Standardisasi aturan kode.<br>• Shitsuke (Rajin): Disiplin review & CI/CD."
    },
    "hints": {
      "concept": "Prinsip Seiri (Ringkas) menekankan pemisahan dan pembuangan hal-hal yang tidak diperlukan dari lingkungan kerja.",
      "execution": "Pilihlah tindakan yang melibatkan pembersihan dead code dan branch usang yang sudah tidak memiliki fungsi produktif."
    },
    "explanation": "Dalam konteks rekayasa perangkat lunak, prinsip Ringkas (Seiri) diimplementasikan dengan memilah komponen yang diperlukan dan menyingkirkan elemen yang tidak berguna, seperti menghapus dead code (kode yang tidak pernah dieksekusi), membersihkan dependensi yang usang, dan menghapus stale branches di repositori Git. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-11",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Subnetting IPv4 & Komunikasi Jaringan",
    "type": "mcq",
    "questionHtml": "Dua komputer pengembang masing-masing dikonfigurasi dengan alamat IP sebagai berikut:<div class=\"net-spec-box\"><div class=\"net-spec-title\"><svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\"><rect x=\"2\" y=\"2\" width=\"20\" height=\"8\" rx=\"2\"/><line x1=\"6\" y1=\"6\" x2=\"6.01\" y2=\"6\"/></svg>Konfigurasi Host Switch Layer-2 (Tanpa Router)</div><div class=\"net-spec-list\"><div class=\"net-spec-item\">💻 <strong>Komputer A:</strong> <span class=\"net-ip-badge\">192.168.1.50/24</span></div><div class=\"net-spec-item\">💻 <strong>Komputer B:</strong> <span class=\"net-ip-badge\">192.168.2.50/24</span></div></div></div>Kedua komputer ditancapkan ke port switch layer-2 yang sama tanpa perangkat router. Apa yang akan terjadi jika Komputer A mencoba mengirim paket data langsung ke Komputer B (misalnya dengan <code>ping 192.168.2.50</code>)?",
    "options": [
      {
        "key": "A",
        "text": "Komunikasi langsung berhasil lancar karena switch otomatis merutekan subnet yang berbeda."
      },
      {
        "key": "B",
        "text": "Komunikasi gagal karena kedua komputer berada pada subnet jaringan yang berbeda dan membutuhkan router (default gateway) untuk meneruskan paket."
      },
      {
        "key": "C",
        "text": "Komputer B akan otomatis mengubah alamat IP-nya menjadi satu segmen dengan Komputer A."
      },
      {
        "key": "D",
        "text": "Kabel UTP yang terhubung ke Komputer B akan langsung mengalami korsleting fisik."
      },
      {
        "key": "E",
        "text": "Data berhasil terkirim asalkan sistem operasi kedua komputer sama-sama Linux."
      }
    ],
    "formulaHud": {
      "title": "IPV4 SUBNETTING: NETWORK BOUNDARY",
      "latex": "\\text{Prefix /24} \\implies \\text{Subnet Mask: } 255.255.255.0 \\implies \\text{Network ID } 192.168.1.0 \\neq 192.168.2.0",
      "legend": "• Perangkat pada Network ID berbeda TIDAK BISA berkomunikasi langsung pada Layer 2 (Switch).<br>• Diperlukan perangkat Layer 3 (Router/Default Gateway) untuk merutekan paket antar-subnet."
    },
    "hints": {
      "concept": "Prefix /24 berarti 24 bit pertama (3 oktet pertama) adalah alamat network. Bandingkan 192.168.1.x dengan 192.168.2.x.",
      "execution": "Karena network ID berbeda, paket tidak bisa dikirimkan secara broadcast layer 2 langsung tanpa bantuan router."
    },
    "explanation": "Dengan prefix /24, subnet mask adalah 255.255.255.0. Komputer A berada pada network 192.168.1.0/24 sedangkan Komputer B berada pada network 192.168.2.0/24. Karena berada pada subnet logis yang berbeda, switch Layer 2 tidak dapat meneruskan komunikasi antar-subnet tersebut tanpa bantuan perangkat Layer 3 (Router). Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-m-12",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Troubleshooting Konektivitas Client-Server & Port",
    "type": "mcq",
    "questionHtml": "Sebuah aplikasi web frontend diuji coba untuk menghubungi backend REST API yang berjalan di port <code>8080</code> pada server remote. Saat tombol kirim ditekan, aplikasi menampilkan error: <em>Connection Refused (ERR_CONNECTION_REFUSED)</em>. Setelah diperiksa dengan ping, server merespons <code>0% packet loss</code>. Penyebab teknis yang PALING MUNGKIN dari kegagalan koneksi tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Layanan web backend (service daemon) belum berjalan pada server atau port 8080 terblokir oleh firewall."
      },
      {
        "key": "B",
        "text": "Kabel serat optik bawah laut antar-pulau terputus total."
      },
      {
        "key": "C",
        "text": "Layar monitor server remote dalam kondisi mati (sleep mode)."
      },
      {
        "key": "D",
        "text": "Browser client kehabisan kapasitas memori RAM penyimpanan cookie."
      },
      {
        "key": "E",
        "text": "Protokol IP pada router client berubah otomatis menjadi IPv6 murni."
      }
    ],
    "formulaHud": {
      "title": "NETWORK TROUBLESHOOTING: PING VS PORT",
      "latex": "\\text{Ping OK (ICMP Layer 3)} \\land \\text{Connection Refused (TCP Layer 4)} \\implies \\text{Service Down / Port Blocked}",
      "legend": "• ICMP Echo (Ping): Memvalidasi konektivitas host level IP.<br>• TCP Connection Refused: Host aktif, namun tidak ada proses yang mendengarkan (listening) di port target, atau firewall menolak paket SYN."
    },
    "hints": {
      "concept": "Ping yang berhasil membuktikan jalur fisik dan perutean IP berfungsi. Masalah terjadi di Transport/Application Layer.",
      "execution": "Pilihlah kemungkinan di mana service aplikasi belum listening pada port 8080 atau ditolak oleh firewall lokal server."
    },
    "explanation": "Ketika ping berhasil (host reachable di layer 3), tetapi koneksi TCP ditolak dengan 'Connection Refused', artinya paket SYN TCP sampai ke server target namun server langsung membalas dengan paket RST (Reset). Hal ini terjadi karena tidak ada aplikasi yang sedang mendengarkan (listening) di port 8080 atau port tersebut diblokir oleh firewall server. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-13",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Arsitektur & Protokol TCP/IP (DNS)",
    "type": "mcq",
    "questionHtml": "Saat seorang pengguna membuka alamat <code>https://api.sekolahsakti.sch.id</code> pada peramban web, sistem pertama kali melakukan resolusi DNS (Domain Name System). Jenis catatan DNS (<em>DNS Record</em>) yang berfungsi memetakan nama domain/subdomain tersebut secara langsung ke sebuah <strong>alamat IPv4 numerik</strong> server hosting adalah …",
    "options": [
      {
        "key": "A",
        "text": "A Record"
      },
      {
        "key": "B",
        "text": "CNAME Record"
      },
      {
        "key": "C",
        "text": "MX Record"
      },
      {
        "key": "D",
        "text": "TXT Record"
      },
      {
        "key": "E",
        "text": "PTR Record"
      }
    ],
    "formulaHud": {
      "title": "DNS RECORD TYPES & RESOLUTION",
      "latex": "\\text{Domain Name} \\xrightarrow{\\text{A Record}} \\text{IPv4 Address (e.g. 103.25.10.5)}",
      "legend": "• A Record: Nama host ke IPv4.<br>• AAAA Record: Nama host ke IPv6.<br>• CNAME: Alias nama host ke nama domain lain.<br>• MX: Mail eXchange (server email)."
    },
    "hints": {
      "concept": "Catatan DNS dasar untuk alamat IPv4 terdiri dari satu huruf kapital pertama dalam alfabet.",
      "execution": "Pilihlah catatan DNS bertipe 'A' (Address Record)."
    },
    "explanation": "A Record (Address Record) adalah jenis record DNS yang paling mendasar, berfungsi menerjemahkan (memetakan) sebuah nama domain atau subdomain menjadi alamat IPv4 numerik 32-bit dari server tujuan. CNAME untuk alias nama, MX untuk server mail, dan TXT untuk verifikasi kepemilikan/SPF. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-14",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Komunikasi Web REST API HTTP Methods",
    "type": "mcq",
    "questionHtml": "Dalam perancangan layanan web berbasis RESTful API, metode HTTP dirancang dengan sifat tertentu. Metode HTTP yang bersifat <strong>Idempoten</strong> (artinya mengeksekusi permintaan yang sama berkali-kali menghasilkan status akhir sistem yang sama persis seperti jika dieksekusi satu kali) adalah …",
    "options": [
      {
        "key": "A",
        "text": "POST"
      },
      {
        "key": "B",
        "text": "PUT"
      },
      {
        "key": "C",
        "text": "CONNECT"
      },
      {
        "key": "D",
        "text": "PATCH (bila menambahkan nilai counter secara incremental)"
      },
      {
        "key": "E",
        "text": "TRACE tanpa parameter"
      }
    ],
    "formulaHud": {
      "title": "REST API: IDEMPOTENCY PROPERTY",
      "latex": "f(f(x)) = f(x) \\implies \\text{Idempotent Methods: GET, PUT, DELETE, HEAD, OPTIONS}",
      "legend": "• PUT /users/1 (dengan payload lengkap) bersifat idempoten: jika dikirim 5 kali berturut-turut, state data user 1 tetap identik.<br>• POST /users/orders TIDAK idempoten: jika dikirim 5 kali, akan tercipta 5 pesanan baru yang berbeda."
    },
    "hints": {
      "concept": "Idempoten berarti pemanggilan berulang kali tidak mengubah hasil akhir data di server melampaui hasil panggilan pertama.",
      "execution": "Metode PUT menggantikan representasi sumber daya secara menyeluruh sehingga berkali-kali dipanggil statusnya tetap sama."
    },
    "explanation": "Metode PUT, GET, dan DELETE didefinisikan sebagai metode idempoten dalam spesifikasi HTTP RFC 7231. Jika client mengirim permintaan `PUT /api/produk/10` dengan data harga Rp 50.000 sebanyak 10 kali, nilai harga produk di database tetap Rp 50.000. Sebaliknya, metode POST tidak idempoten karena setiap request POST biasanya membuat record data entitas baru. Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-m-15",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Operasi Linux & Hak Akses File",
    "type": "mcq",
    "questionHtml": "Pada server Linux, seorang web administrator menjalankan perintah:<br><pre><code>chmod 644 /var/www/html/index.php</code></pre>Arti representasi izin hak akses oktal <code>644</code> terhadap file tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Owner memiliki hak Read & Write (rw-); Group dan Others hanya memiliki hak Read (r--)."
      },
      {
        "key": "B",
        "text": "Owner memiliki hak Read, Write, Execute (rwx); Group memiliki hak Write; Others tidak punya hak."
      },
      {
        "key": "C",
        "text": "Semua pengguna memiliki hak Read dan Write secara setara tanpa batasan."
      },
      {
        "key": "D",
        "text": "File tersebut otomatis terenkripsi dan hanya dapat dibuka oleh user root."
      },
      {
        "key": "E",
        "text": "Owner memiliki hak eksekusi saja, sedangkan publik memiliki hak baca dan tulis."
      }
    ],
    "formulaHud": {
      "title": "LINUX PERMISSION OCTAL CALCULATION",
      "latex": "\\text{Octal: } r=4, \\; w=2, \\; x=1 \\implies 6 = 4+2 \\; (rw-), \\quad 4 = 4 \\; (r--)",
      "legend": "• Digit 1 (Owner): 6 = Read + Write (4+2).<br>• Digit 2 (Group): 4 = Read only.<br>• Digit 3 (Others/Public): 4 = Read only.<br>• Format string: <code>-rw-r--r--</code>"
    },
    "hints": {
      "concept": "Nilai biner/oktal permission: Read = 4, Write = 2, Execute = 1. Angka 6 = 4 + 2 (Read & Write). Angka 4 = 4 (Read).",
      "execution": "Owner = 6 (Read+Write), Group = 4 (Read), Others = 4 (Read)."
    },
    "explanation": "Dalam notasi oktal Linux: Read (r) bernilai 4, Write (w) bernilai 2, dan Execute (x) bernilai 1. Digit pertama (6) untuk Owner bernilai 4+2 = Read & Write. Digit kedua (4) untuk Group bernilai 4 = Read. Digit ketiga (4) untuk Others bernilai 4 = Read. Format simboliknya adalah `-rw-r--r--`. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-16",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Analisis Struktur Data List / Array (Index Shifting)",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program manipulasi list berikut:<br><pre><code class=\"language-python\">inventori = [\"Pedang\", \"Perisai\", \"Ramuan\", \"Panah\"]\ninventori.append(\"Kunci\")\ninventori.pop(1)\nprint(inventori[1], len(inventori))</code></pre>Output yang dihasilkan saat program di atas dieksekusi adalah …",
    "options": [
      {
        "key": "A",
        "text": "Perisai 5"
      },
      {
        "key": "B",
        "text": "Ramuan 4"
      },
      {
        "key": "C",
        "text": "Pedang 4"
      },
      {
        "key": "D",
        "text": "Ramuan 5"
      },
      {
        "key": "E",
        "text": "Panah 3"
      }
    ],
    "formulaHud": {
      "title": "LIST OPERATION: APPEND & POP INDEX SHIFTING",
      "latex": "L_0 = [P, S, R, A] \\xrightarrow{\\text{append}(K)} [P, S, R, A, K] \\xrightarrow{\\text{pop}(1)} [P, R, A, K]",
      "legend": "• Awal: <code>['Pedang', 'Perisai', 'Ramuan', 'Panah']</code>.<br>• Setelah append('Kunci'): panjang list menjadi 5.<br>• Setelah pop(1): elemen indeks 1 ('Perisai') dihapus, elemen berikutnya bergeser ke kiri.<br>• Indeks 1 yang baru adalah 'Ramuan' dan total elemen adalah 4."
    },
    "hints": {
      "concept": "Method pop(i) menghapus elemen pada indeks i dan menggeser seluruh elemen di sebelah kanannya satu posisi ke kiri.",
      "execution": "Hitung: indeks 1 semula adalah 'Perisai'. Setelah dihapus, 'Ramuan' (semula indeks 2) bergeser menjadi indeks 1. Jumlah elemen = 4 + 1 - 1 = 4."
    },
    "explanation": "Pada awal program, inventori berisi 4 elemen. Baris `append('Kunci')` menambah elemen di akhir sehingga menjadi `['Pedang', 'Perisai', 'Ramuan', 'Panah', 'Kunci']` (panjang 5). Baris `pop(1)` menghapus elemen pada indeks 1 yaitu 'Perisai'. Akibatnya elemen di kanannya bergeser ke kiri, sehingga `inventori[1]` kini bernilai 'Ramuan' dan panjang list (`len`) menjadi 4. Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-m-17",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Modularisasi Fungsi: Return Value vs Print",
    "type": "mcq",
    "questionHtml": "Perhatikan dua subprogram berikut:<br><pre><code class=\"language-python\">def hitung_luas(panjang, lebar):\n    return panjang * lebar\n\ndef cetak_header(judul):\n    print(\"===\", judul, \"===\")\n\na = hitung_luas(5, 4)\nb = cetak_header(\"Laporan\")\nprint(a, b)</code></pre>Output yang dicetak pada baris terakhir <code>print(a, b)</code> adalah …",
    "options": [
      {
        "key": "A",
        "text": "20 None"
      },
      {
        "key": "B",
        "text": "20 === Laporan ==="
      },
      {
        "key": "C",
        "text": "None None"
      },
      {
        "key": "D",
        "text": "20 Error"
      },
      {
        "key": "E",
        "text": "20 0"
      }
    ],
    "formulaHud": {
      "title": "FUNCTION MODULARITY: RETURN VS PROCEDURE",
      "latex": "\\text{def f(): return v} \\implies \\text{Variable stores } v \\quad \\mid \\quad \\text{def g(): print(v)} \\implies \\text{Variable stores } \\texttt{None}",
      "legend": "• Fungsi `hitung_luas` memiliki return statement sehingga mengembalikan nilai numerik 20.<br>• Prosedur `cetak_header` hanya mencetak ke layar tanpa return, sehingga secara implisit mengembalikan `None`."
    },
    "hints": {
      "concept": "Di Python, fungsi yang tidak memiliki pernyataan `return` eksplisit akan selalu mengembalikan objek `None`.",
      "execution": "`a` menampung nilai return 20. `b` menampung hasil pemanggilan fungsi yang tidak me-return apa pun (`None`)."
    },
    "explanation": "Fungsi `hitung_luas(5, 4)` mengembalikan nilai hasil perkalian yaitu 20, sehingga variabel `a = 20`. Sementara itu, fungsi `cetak_header` hanya melakukan efek samping mencetak string ke konsol tanpa pernyataan `return`, sehingga nilai kembalian default fungsi di Python adalah `None` (`b = None`). Oleh karena itu, `print(a, b)` menghasilkan `20 None`. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-18",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Struktur Data Dictionary & Key-Value Lookup",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode kamus data (dictionary) di Python berikut:<br><pre><code class=\"language-python\">peserta = {\n    \"101\": {\"nama\": \"Budi\", \"nilai\": 85},\n    \"102\": {\"nama\": \"Siti\", \"nilai\": 92},\n    \"103\": {\"nama\": \"Andi\", \"nilai\": 78}\n}\n\ntotal = 0\nfor k in peserta:\n    total += peserta[k][\"nilai\"]\nrata_rata = total / len(peserta)\nprint(f\"{rata_rata:.1f}\")</code></pre>Output yang dihasilkan dari eksekusi kode program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "85.0"
      },
      {
        "key": "B",
        "text": "85.0"
      },
      {
        "key": "C",
        "text": "85.0"
      },
      {
        "key": "D",
        "text": "85.0"
      },
      {
        "key": "E",
        "text": "90.0"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "DICTIONARY ITERATION & AVERAGE CALCULATION",
      "latex": "\\bar{x} = \\frac{\\sum_{i=1}^{n} \\text{nilai}_i}{n} = \\frac{85 + 92 + 78}{3} = \\frac{255}{3} = 85.0",
      "legend": "• Perulangan `for k in peserta:` mengiterasi kunci utama dictionary ('101', '102', '103').<br>• `peserta[k]['nilai']` mengakses data nilai masing-masing peserta.<br>• Total = 255; Jumlah peserta = 3; Rata-rata = 85.0."
    },
    "hints": {
      "concept": "Jumlahkan semua nilai: 85 + 92 + 78 = 255. Bagi dengan jumlah peserta (3).",
      "execution": "255 / 3 = 85.0."
    },
    "explanation": "Iterasi dictionary menjumlahkan nilai ketiga siswa: 85 + 92 + 78 = 255. Nilai rata-rata diperoleh dengan membagi total dengan panjang dictionary (3), yaitu 255 / 3 = 85.0. Format `:.1f` mencetaknya dengan satu angka desimal: '85.0'. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-19",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Trace Algoritma Perulangan Bersarang (Nested Loops)",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program perulangan bersarang berikut:<br><pre><code class=\"language-python\">counter = 0\nfor i in range(1, 4):\n    for j in range(i, 4):\n        counter += 1\nprint(counter)</code></pre>Berapakah nilai akhir variabel <code>counter</code> setelah seluruh perulangan selesai dieksekusi?",
    "options": [
      {
        "key": "A",
        "text": "6"
      },
      {
        "key": "B",
        "text": "9"
      },
      {
        "key": "C",
        "text": "12"
      },
      {
        "key": "D",
        "text": "3"
      },
      {
        "key": "E",
        "text": "16"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "NESTED LOOP TRACING",
      "latex": "\\text{Total Iterasi} = \\sum_{i=1}^{3} (4 - i) = (4-1) + (4-2) + (4-3) = 3 + 2 + 1 = 6",
      "legend": "• i = 1: j berjalan dari 1 s.d. 3 (3 kali: j=1, 2, 3).<br>• i = 2: j berjalan dari 2 s.d. 3 (2 kali: j=2, 3).<br>• i = 3: j berjalan dari 3 s.d. 3 (1 kali: j=3).<br>• Total counter = 3 + 2 + 1 = 6."
    },
    "hints": {
      "concept": "Lakukan trace untuk setiap nilai i (1, 2, 3). Range(i, 4) berhenti sebelum angka 4.",
      "execution": "Hitung jumlah perulangan dalam untuk setiap i: i=1 ada 3 iterasi, i=2 ada 2 iterasi, i=3 ada 1 iterasi. Jumlahkan: 3 + 2 + 1 = 6."
    },
    "explanation": "Pada `i = 1`, loop dalam `range(1, 4)` berjalan untuk j = 1, 2, 3 (3 kali). Pada `i = 2`, loop dalam `range(2, 4)` berjalan untuk j = 2, 3 (2 kali). Pada `i = 3`, loop dalam `range(3, 4)` berjalan untuk j = 3 (1 kali). Total penambahan nilai counter adalah 3 + 2 + 1 = 6. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-m-20",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Lingkup Variabel: Local vs Global Scope",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program mengenai cakupan variabel berikut:<br><pre><code class=\"language-python\">bonus = 5000\n\ndef hitung_gaji(pokok):\n    bonus = 2000\n    return pokok + bonus\n\nhasil = hitung_gaji(10000)\nprint(hasil, bonus)</code></pre>Output yang dicetak oleh program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "12000 5000"
      },
      {
        "key": "B",
        "text": "12000 2000"
      },
      {
        "key": "C",
        "text": "15000 5000"
      },
      {
        "key": "D",
        "text": "17000 2000"
      },
      {
        "key": "E",
        "text": "Error: UnboundLocalError"
      }
    ],
    "formulaHud": {
      "title": "VARIABLE SCOPE: LOCAL SHADOWING",
      "latex": "\\text{Inside function: } \\text{bonus}_{\\text{local}} = 2000 \\quad \\mid \\quad \\text{Outside function: } \\text{bonus}_{\\text{global}} = 5000",
      "legend": "• Pendefinisian `bonus = 2000` di dalam fungsi menciptakan variabel lokal yang menaungi (shadowing) variabel global.<br>• Variabel global di luar fungsi tidak mengalami perubahan nilai tanpa kata kunci `global`."
    },
    "hints": {
      "concept": "Variabel di dalam fungsi bersifat lokal kecuali dideklarasikan dengan kata kunci `global`. Variabel global di luar tidak berubah.",
      "execution": "Di dalam fungsi: pokok (10000) + bonus lokal (2000) = 12000. Di luar fungsi: bonus global tetap 5000."
    },
    "explanation": "Variabel `bonus = 2000` yang dibuat di dalam fungsi `hitung_gaji` merupakan variabel lokal (local scope) yang menutupi variabel global hanya di dalam tubuh fungsi tersebut. Hasil fungsi adalah 10000 + 2000 = 12000. Saat fungsi selesai, variabel `bonus` di lingkup global tetap tidak berubah yaitu 5000. Oleh karena itu, outputnya adalah `12000 5000`. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Class, Object & Constructor Default Parameters",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode class berikut:<br><pre><code class=\"language-python\">class Produk:\n    def __init__(self, nama, harga, stok=10):\n        self.nama = nama\n        self.harga = harga\n        self.stok = stok\n\np1 = Produk(\"Mouse Gaming\", 150000)\np2 = Produk(\"Keyboard Mekanik\", 350000, 25)\np1.stok = 5\n\nprint(p1.stok, p2.stok)</code></pre>Output yang dicetak oleh baris terakhir program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "5 25"
      },
      {
        "key": "B",
        "text": "5 5"
      },
      {
        "key": "C",
        "text": "10 25"
      },
      {
        "key": "D",
        "text": "5 10"
      },
      {
        "key": "E",
        "text": "Error: p1.stok is private"
      }
    ],
    "formulaHud": {
      "title": "OOP: INSTANCE ATTRIBUTE INDEPENDENCE",
      "latex": "p_1.\\text{stok} \\cap p_2.\\text{stok} = \\emptyset \\implies \\text{Perubahan pada } p_1 \\text{ tidak mempengaruhi } p_2",
      "legend": "• p1 diinstansiasi tanpa argumen stok ketiga, sehingga memakai default value stok = 10.<br>• p2 diinstansiasi dengan stok = 25.<br>• `p1.stok = 5` hanya memodifikasi atribut instans milik p1 secara independen."
    },
    "hints": {
      "concept": "Setiap instans objek dari sebuah class mengalokasikan ruang memori sendiri untuk atribut instansnya.",
      "execution": "p1.stok diubah menjadi 5. p2.stok tetap 25 sesuai inisialisasi constructor-nya."
    },
    "explanation": "Objek `p1` dan `p2` adalah dua instans independen dari class `Produk`. Pada saat pembuatan, `p1.stok` bernilai 10 (dari default parameter), dan `p2.stok` bernilai 25. Perintah `p1.stok = 5` hanya mengubah nilai atribut pada objek `p1`. Nilai atribut pada objek `p2` tetap 25. Maka outputnya adalah `5 25`. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-22",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Inheritance & Method Overriding",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program relasi class berikut:<br><pre><code class=\"language-python\">class Kendaraan:\n    def __init__(self, merk):\n        self.merk = merk\n    def info_energi(self):\n        return \"Bahan bakar umum\"\n\nclass MotorListrik(Kendaraan):\n    def info_energi(self):\n        return \"Baterai daya listrik\"\n\nk = Kendaraan(\"Yamaha\")\nm = MotorListrik(\"Gesits\")\nprint(k.info_energi(), \"|\", m.info_energi())</code></pre>Konsep OOP yang ditunjukkan oleh pendefinisian ulang method <code>info_energi()</code> pada class <code>MotorListrik</code> beserta outputnya adalah …",
    "options": [
      {
        "key": "A",
        "text": "Method Overriding, menghasilkan: Bahan bakar umum | Baterai daya listrik"
      },
      {
        "key": "B",
        "text": "Method Overloading, menghasilkan: Bahan bakar umum | Bahan bakar umum"
      },
      {
        "key": "C",
        "text": "Multiple Inheritance, menghasilkan: Baterai daya listrik | Baterai daya listrik"
      },
      {
        "key": "D",
        "text": "Data Abstraction, menghasilkan: Error: method duplicate"
      },
      {
        "key": "E",
        "text": "Interface Segregation, menghasilkan: None | None"
      }
    ],
    "formulaHud": {
      "title": "OOP: METHOD OVERRIDING IN INHERITANCE",
      "latex": "\\text{SubClass.method()} \\text{ mereplace implementasi } \\text{SuperClass.method()}",
      "legend": "• Subclass mewarisi seluruh perilaku superclass namun dapat mengganti (override) perilaku method spesifik sesuai kebutuhannya.<br>• Objek superclass tetap mengeksekusi method aslinya."
    },
    "hints": {
      "concept": "Mendefinisikan method dengan nama dan parameter sama di kelas anak untuk menggantikan method kelas induk disebut method overriding.",
      "execution": "k.info_energi() memanggil versi Kendaraan, m.info_energi() memanggil versi turunan MotorListrik."
    },
    "explanation": "Pendefinisian method dengan nama yang sama persis di kelas turunan (`MotorListrik`) untuk menggantikan method milik superclass (`Kendaraan`) adalah bentuk Method Overriding. Objek `k` memanggil method aslinya ('Bahan bakar umum'), sedangkan objek `m` memanggil versi yang sudah dioverride ('Baterai daya listrik'). Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-23",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Dynamic Polymorphism & Duck Typing",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program sistem notifikasi berikut:<br><pre><code class=\"language-python\">class EmailSender:\n    def kirim(self, pesan):\n        return f\"Kirim Email: {pesan}\"\n\nclass SMSSender:\n    def kirim(self, pesan):\n        return f\"Kirim SMS: {pesan}\"\n\ndef siarkan(layanan, teks):\n    return layanan.kirim(teks)\n\ne = EmailSender()\ns = SMSSender()\nprint(siarkan(e, \"Halo\"), \"#\", siarkan(s, \"Pagi\"))</code></pre>Karakteristik utama dari konsep <strong>Polymorphism</strong> yang tercermin pada fungsi <code>siarkan()</code> di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "Fungsi `siarkan()` dapat menerima objek dari class apa pun asalkan objek tersebut memiliki method `kirim()` dengan antarmuka yang serasi."
      },
      {
        "key": "B",
        "text": "Fungsi `siarkan()` mewajibkan semua parameter dikonversi menjadi tipe data integer."
      },
      {
        "key": "C",
        "text": "Seluruh class diwajibkan menghapus constructor `__init__` agar dapat diproses."
      },
      {
        "key": "D",
        "text": "Kedua objek dipaksa menggunakan alokasi memori fisik yang sama di harddisk."
      },
      {
        "key": "E",
        "text": "Fungsi `siarkan()` hanya dapat dijalankan pada lingkungan sistem operasi Windows."
      }
    ],
    "formulaHud": {
      "title": "OOP: POLYMORPHISM & DUCK TYPING",
      "latex": "\"\\text{If it walks like a duck and quacks like a duck, it's a duck}\" \\implies \\text{Uniform Interface invocation}",
      "legend": "• Polymorphism memungkinkan kode client memanggil antarmuka seragam (`layanan.kirim()`) pada objek-objek berbeda tanpa perlu memeriksa tipe class konkretnya."
    },
    "hints": {
      "concept": "Polymorphism berarti 'banyak bentuk': satu fungsi pemanggil yang sama dapat berinteraksi dengan berbagai objek berbeda.",
      "execution": "Pilihlah jawaban yang menjelaskan fleksibilitas fungsi `siarkan()` dalam menerima objek berbeda yang memiliki method `kirim()`."
    },
    "explanation": "Polymorphism memungkinkan pemanggilan method yang seragam (`layanan.kirim()`) pada berbagai objek dari kelas yang berbeda (`EmailSender` maupun `SMSSender`). Fungsi `siarkan()` tidak perlu peduli objek berasal dari class apa, asalkan memiliki method `kirim()`. Ini merupakan inti dari konsep dynamic polymorphism dan duck typing. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-24",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Enkapsulasi & Validasi Data Mutator",
    "type": "mcq",
    "questionHtml": "Perhatikan perancangan class akun perbankan berikut:<br><pre><code class=\"language-python\">class RekeningBank:\n    def __init__(self, nomor, saldo_awal):\n        self.nomor = nomor\n        self.__saldo = max(0, saldo_awal)\n    \n    def get_saldo(self):\n        return self.__saldo\n        \n    def setor(self, jumlah):\n        if jumlah > 0:\n            self.__saldo += jumlah\n            return True\n        return False\n\nr = RekeningBank(\"001\", 100000)\nr.setor(-50000)\nprint(r.get_saldo())</code></pre>Berapakah output yang dihasilkan dari kode program di atas, dan mengapa?",
    "options": [
      {
        "key": "A",
        "text": "100000, karena metode mutator setor() menolak penambahan nilai negatif sehingga saldo tidak berubah."
      },
      {
        "key": "B",
        "text": "50000, karena setoran negatif otomatis mengurangi saldo akun."
      },
      {
        "key": "C",
        "text": "0, karena terjadi error validasi yang me-reset saldo awal."
      },
      {
        "key": "D",
        "text": "150000, karena tanda minus diubah menjadi nilai mutlak positif."
      },
      {
        "key": "E",
        "text": "Error: AttributeError: private variable cannot be accessed."
      }
    ],
    "formulaHud": {
      "title": "ENCAPSULATION: CONTROLLED MUTATION",
      "latex": "\\text{setor}(\\Delta) = \\begin{cases} \\text{saldo} + \\Delta & \\text{if } \\Delta > 0 \\\\ \\text{saldo} & \\text{if } \\Delta \\le 0 \\end{cases}",
      "legend": "• Enkapsulasi melindungi integritas data internal objek dari manipulasi tidak valid dari luar class.<br>• Nilai `jumlah = -50000` tidak memenuhi syarat `jumlah > 0`, sehingga method mengabaikannya."
    },
    "hints": {
      "concept": "Periksa kondisi percabangan di dalam method setor(): `if jumlah > 0:`. Apakah -50000 > 0?",
      "execution": "Karena kondisi bernilai False, saldo tidak bertambah dan tetap bernilai 100000."
    },
    "explanation": "Pada class `RekeningBank`, atribut `__saldo` dienkapsulasi secara private. Method `setor(jumlah)` memiliki aturan validasi `if jumlah > 0`. Karena argumen yang dikirimkan adalah `-50000` (tidak lebih dari 0), kondisi tidak terpenuhi dan saldo tidak dimodifikasi. Pemanggilan `r.get_saldo()` tetap mengembalikan saldo awal yaitu 100000. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-m-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Class Attribute vs Instance Attribute",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program class berikut:<br><pre><code class=\"language-python\">class Siswa:\n    sekolah = \"SMK Negeri 1\"\n    def __init__(self, nama):\n        self.nama = nama\n\ns1 = Siswa(\"Budi\")\ns2 = Siswa(\"Ani\")\nSiswa.sekolah = \"SMK Pusat Keunggulan\"\n\nprint(s1.sekolah, \"-\", s2.sekolah)</code></pre>Perbedaan mendasar antara <code>Class Attribute</code> (seperti <code>sekolah</code>) dan <code>Instance Attribute</code> (seperti <code>nama</code>) yang dibuktikan oleh output program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "Class attribute dibagi bersama (shared) oleh seluruh objek dari class tersebut, sehingga perubahannya berdampak pada semua objek (output: SMK Pusat Keunggulan - SMK Pusat Keunggulan)."
      },
      {
        "key": "B",
        "text": "Class attribute hanya dapat dibaca oleh objek pertama saja (output: SMK Pusat Keunggulan - SMK Negeri 1)."
      },
      {
        "key": "C",
        "text": "Instance attribute otomatis tersimpan di server cloud eksternal."
      },
      {
        "key": "D",
        "text": "Class attribute tidak dapat dimodifikasi setelah class pertama kali didefinisikan."
      },
      {
        "key": "E",
        "text": "Program menghasilkan Error: Siswa object has no attribute sekolah."
      }
    ],
    "formulaHud": {
      "title": "OOP: CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE",
      "latex": "\\text{Class Attribute } (\\text{Shared Namespace}) \\quad \\text{vs} \\quad \\text{Instance Attribute } (\\text{Unique per Object})",
      "legend": "• `sekolah`: Didefinisikan di luar method, milik class, dibagikan ke seluruh instans.<br>• `self.nama`: Didefinisikan di dalam `__init__`, unik untuk setiap instans objek."
    },
    "hints": {
      "concept": "Class attribute adalah variabel milik class yang nilainya dibagi bersama oleh seluruh instans objek yang dibuat dari class tersebut.",
      "execution": "Mengubah `Siswa.sekolah` memperbarui nilai bagi seluruh objek (`s1` dan `s2`)."
    },
    "explanation": "Variabel `sekolah` yang didefinisikan langsung di dalam tubuh class adalah Class Attribute. Variabel ini dimiliki bersama oleh seluruh instans (`s1`, `s2`). Ketika `Siswa.sekolah` diubah menjadi 'SMK Pusat Keunggulan', perubahan ini terefleksi pada seluruh objek yang mengakses atribut tersebut. Outputnya adalah `SMK Pusat Keunggulan - SMK Pusat Keunggulan`. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  }
]

print('Loaded 25 items.')
