# -*- coding: utf-8 -*-
HARD_QUESTIONS = [
  {
    "id": "rpl-lat-h-01",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Analisis Metrik Proyek Scrum (Burndown Chart)",
    "type": "mcq",
    "questionHtml": "Dalam Sprint berdurasi 10 hari kerja dengan total komitmen 80 Story Points, pada hari ke-6 grafik <em>Sprint Burndown Chart</em> menunjukkan sisa pekerjaan masih berada di angka 65 Story Points, jauh di atas garis ideal (<em>ideal guideline</em> = 32 Story Points). Tim juga mendeteksi adanya penambahan 3 <em>user story</em> baru tanpa persetujuan di tengah Sprint (<em>scope creep</em>). Keputusan manajemen teknis yang PALING TEPAT dan profesional dilakukan oleh Scrum Master bersama Product Owner adalah …",
    "options": [
      {
        "key": "A",
        "text": "Memerintahkan seluruh tim pengembang bekerja lembur 24 jam nonstop setiap hari hingga akhir Sprint."
      },
      {
        "key": "B",
        "text": "Mengeluarkan user story baru yang belum terencana dari Sprint Backlog dan menegosiasikan kembali prioritas backlog bersama Product Owner agar tim fokus menyelesaikan Sprint Goal inti."
      },
      {
        "key": "C",
        "text": "Mengubah angka estimasi story points dari 65 menjadi 30 secara sepihak di dashboard agar laporan terlihat hijau."
      },
      {
        "key": "D",
        "text": "Membatalkan seluruh metodologi Scrum dan beralih ke model Waterfall murni pada hari yang sama."
      },
      {
        "key": "E",
        "text": "Mengabaikan grafik burndown karena metrik tersebut tidak memiliki korelasi dengan kemajuan perangkat lunak."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "AGILE VELOCITY & BURNDOWN ANALYSIS",
      "latex": "\\text{Deviasi} = \\text{Remaining Points} - \\text{Ideal Points} = 65 - 32 = +33 \\text{ SP} \\implies \\text{Scope Renegotiation Required}",
      "legend": "• Scope Creep: Penambahan lingkup pekerjaan di tengah Sprint mengancam tercapainya Sprint Goal.<br>• Prinsip Scrum: Lindungi kapasitas tim pengembang dengan menegosiasikan atau mendescope backlog non-kritis ke Product Backlog."
    },
    "hints": {
      "concept": "Jika sisa pekerjaan jauh lebih besar daripada waktu tersisa akibat scope creep, solusi agile adalah renegosiasi cakupan pekerjaan (descope backlog non-esensial), bukan memaksakan lembur yang merusak kualitas.",
      "execution": "Pilihlah tindakan proteksi terhadap Sprint Goal melalui renegosiasi backlog bersama Product Owner."
    },
    "explanation": "Dalam Scrum, ketika terjadi deviasi signifikan antara kemajuan riil dan garis ideal burndown chart (terlebih akibat scope creep), Scrum Master dan Product Owner harus berkolaborasi dengan tim pengembang untuk mereview Sprint Backlog. Fitur-fitur tambahan yang tidak krusial harus dikembalikan ke Product Backlog agar tim dapat memfokuskan sisa kapasitas kerja untuk mencapai Sprint Goal yang telah disepakati. Jawaban: B.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-02",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "HAKI & Risiko Pelanggaran Lisensi Perangkat Lunak",
    "type": "mcq",
    "questionHtml": "Sebuah perusahaan perangkat lunak menggabungkan pustaka kode berlisensi <strong>AGPL (Affero General Public License) v3</strong> ke dalam arsitektur backend layanan SaaS (<em>Software-as-a-Service</em>) berbasis cloud mereka. Perusahaan tersebut tidak pernah mendistribusikan file biner kepada pengguna, melainkan hanya menyediakan akses interaktif melalui browser. Berdasarkan klausul khusus lisensi AGPL v3, implikasi hukum bagi perusahaan tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Perusahaan tidak berkewajiban membuka kode sumber karena tidak mendistribusikan salinan biner perangkat lunak secara fisik."
      },
      {
        "key": "B",
        "text": "Perusahaan WAJIB menyediakan seluruh kode sumber lengkap dari layanan SaaS tersebut kepada seluruh pengguna yang mengaksesnya melalui jaringan."
      },
      {
        "key": "C",
        "text": "Perusahaan hanya perlu membayar biaya langganan bulanan kepada Free Software Foundation (FSF)."
      },
      {
        "key": "D",
        "text": "Lisensi AGPL v3 otomatis berubah menjadi lisensi MIT yang permisif jika berjalan di server cloud."
      },
      {
        "key": "E",
        "text": "Aplikasi cloud tersebut secara otomatis ditutup paksa oleh sistem operasi server."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "SOFTWARE LICENSING: AGPL NETWORK COPYLEFT",
      "latex": "\\text{AGPL v3: Section 13 (Remote Network Interaction)} \\implies \\text{Source Code MUST be Offered to Network Users}",
      "legend": "• GPL Standar: Kewajiban copyleft hanya terpicu saat distribusi biner (Distribution Loophole).<br>• AGPL: Menutup celah cloud/SaaS; siapapun yang berinteraksi via jaringan berhak meminta kode sumber lengkap."
    },
    "hints": {
      "concept": "Lisensi Affero GPL (AGPL) diciptakan khusus untuk menutup 'ASP loophole', mewajibkan penyedia SaaS membuka kode sumber kepada siapapun yang berinteraksi lewat jaringan.",
      "execution": "Pilihlah jawaban yang menegaskan kewajiban membuka source code lengkap kepada pengguna yang mengakses via web/jaringan."
    },
    "explanation": "Klausul Pasal 13 pada lisensi AGPL v3 dirancang khusus untuk mengatasi 'SaaS/ASP loophole' pada GPL standar. Jika perangkat lunak yang menggunakan kode AGPL dimodifikasi dan dijalankan di server sehingga pengguna berinteraksi dengannya melalui jaringan komputer (seperti web SaaS), penyedia layanan wajib memberikan akses kode sumber lengkap kepada para pengguna jaringan tersebut. Jawaban: B.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-03",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Arsitektur Perangkat Lunak & Clean Architecture",
    "type": "mcq",
    "questionHtml": "Dalam prinsip <em>Clean Architecture</em> (Robert C. Martin), terdapat <strong>Dependency Rule</strong> yang menyatakan bahwa arah ketergantungan (<em>dependency</em>) antar-lapisan kode hanya boleh mengarah ke dalam (<em>inward</em>). Jika sebuah modul <code>Entities</code> (lapisan terdalam) membutuhkan pemanggilan kueri basis data SQL (lapisan terluar <code>Frameworks & Drivers</code>), teknik arsitektur yang WAJIB diterapkan agar prinsip Dependency Inversion tidak dilanggar adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menulis kode koneksi SQL dan string kueri langsung di dalam konstruktor Entity."
      },
      {
        "key": "B",
        "text": "Mendefinisikan antarmuka/kontrak (interface / repository pattern) pada lapisan Use Cases, lalu implementasi detail SQL diinjeksikan dari lapisan terluar (Dependency Injection)."
      },
      {
        "key": "C",
        "text": "Menghapus lapisan Entities dan menyatukan seluruh logika bisnis ke dalam controller web."
      },
      {
        "key": "D",
        "text": "Mengganti seluruh basis data relasional dengan file teks catatan sementara."
      },
      {
        "key": "E",
        "text": "Mengizinkan lapisan inti mengimpor driver MySQL secara langsung agar eksekusi lebih cepat."
      }
    ],
    "formulaHud": {
      "title": "CLEAN ARCHITECTURE: DEPENDENCY INVERSION PRINCIPLE",
      "latex": "\\text{High-Level Modules (Core Logic)} \\to \\text{Abstraction (Interface)} \\leftarrow \\text{Low-Level Details (SQL DB)}",
      "legend": "• Inti domain (Entities/Use Cases) tidak boleh bergantung pada detail teknologi (DB/Framework).<br>• Gunakan Repository Interface di lapisan dalam dan Database Repository Implementation di lapisan luar."
    },
    "hints": {
      "concept": "Prinsip Dependency Inversion membalik ketergantungan langsung ke database dengan memanfaatkan abstraksi interface/repository.",
      "execution": "Pilihlah solusi yang menggunakan interface/kontrak di layer dalam dengan injeksi ketergantungan dari luar."
    },
    "explanation": "Prinsip dasar Clean Architecture adalah isolasi aturan bisnis inti dari teknologi eksternal. Agar lapisan dalam tidak bergantung pada detail basis data di lapisan luar, diterapkan pola Repository: lapisan dalam mendefinisikan interface/abstraksi kontrak data, sedangkan modul basis data di lapisan luar mengimplementasikan interface tersebut dan diinjeksikan saat runtime (Dependency Injection). Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-h-04",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Budaya Mutu & Static Code Analysis (SonarQube)",
    "type": "mcq",
    "questionHtml": "Sebuah pipeline CI/CD dikonfigurasi dengan <strong>Quality Gate</strong> menggunakan alat analisis statis SonarQube. Pipeline mengalami kegagalan build (<em>Quality Gate Failed</em>) dengan metrik:<br>• <em>Code Coverage on New Code</em>: 62% (Target minimum: 80%)<br>• <em>Security Vulnerabilities</em>: 0<br>• <em>Bugs</em>: 0<br>• <em>Duplicated Lines Density</em>: 1.2% (Batas maksimum: 3%)<br>Langkah rekayasa yang WAJIB diambil oleh pengembang sebelum rilis dapat disetujui adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menurunkan target batas minimum coverage di server CI/CD menjadi 50% secara diam-diam."
      },
      {
        "key": "B",
        "text": "Menulis skenario pengujian unit otomatis (automated unit tests) tambahan untuk menguji percabangan logika baru hingga cakupan kode mencapai minimal 80%."
      },
      {
        "key": "C",
        "text": "Menghapus seluruh fitur baru dari aplikasi agar tidak ada baris kode baru yang diukur."
      },
      {
        "key": "D",
        "text": "Mengganti nama file kode sumber menjadi file gambar agar tidak dipindai oleh alat analisis."
      },
      {
        "key": "E",
        "text": "Menambahkan komentar kosong sebanyak 10.000 baris untuk menaikkan volume file."
      }
    ],
    "formulaHud": {
      "title": "CODE COVERAGE METRIC",
      "latex": "\\text{Coverage} = \\frac{\\text{Executed Lines / Branches in Tests}}{\\text{Total Executable Lines of New Code}} \\times 100\\%",
      "legend": "• Coverage 62% < 80% menandakan 38% logika baru belum terverifikasi oleh test runner.<br>• Tindakan mutu rekayasa: Tulis unit test untuk menguji jalur kode yang belum ter-cover."
    },
    "hints": {
      "concept": "Kegagalan Quality Gate akibat rendahnya cakupan kode (coverage) diatasi dengan melengkapi skenario pengujian otomatis, bukan melonggarkan standar mutu.",
      "execution": "Pilihlah opsi penulisan unit test tambahan untuk menguji percabangan logika kode baru."
    },
    "explanation": "Quality Gate gagal karena metrik Code Coverage pada kode baru hanya 62%, di bawah ambang batas wajib 80%. Artinya, lebih dari sepertiga baris kode baru belum teruji oleh skenario pengujian otomatis. Langkah standar rekayasa perangkat lunak adalah menulis skenario unit test tambahan (menguji kondisi normal dan batas) hingga cakupan pengujian melampaui 80%. Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-h-05",
    "subject": "rpl",
    "materi": "WAWASAN DUNIA KERJA BIDANG PPLG",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Software Testing: Piramida Pengujian (Test Pyramid)",
    "type": "mcq",
    "questionHtml": "Dalam perancangan strategi pengujian perangkat lunak modern (<em>The Practical Test Pyramid</em> oleh Martin Fowler), alokasi proporsi jenis pengujian yang ideal dari tingkat paling banyak ke paling sedikit adalah …",
    "options": [
      {
        "key": "A",
        "text": "Unit Tests terbanyak (fondasi luas), Service/Integration Tests sedang, dan UI/End-to-End Tests paling sedikit (puncak piramida)."
      },
      {
        "key": "B",
        "text": "Manual UI Tests 90%, Automated Integration Tests 10%, dan Unit Tests 0%."
      },
      {
        "key": "C",
        "text": "End-to-End Tests terbanyak, Unit Tests sedang, dan Kompilasi paling sedikit."
      },
      {
        "key": "D",
        "text": "Seluruh pengujian dilakukan secara acak tanpa pembagian tingkatan piramida."
      },
      {
        "key": "E",
        "text": "Hanya melakukan pengujian stres (Stress Testing) tanpa pernah menguji fungsionalitas."
      }
    ],
    "formulaHud": {
      "title": "THE TEST PYRAMID PARADIGM",
      "latex": "\\text{Piramida: } \\underbrace{\\text{Unit Tests (Fast, Cheap, Granular)}}_{\\approx 70\\%} > \\underbrace{\\text{Integration Tests}}_{\\approx 20\\%} > \\underbrace{\\text{E2E / UI Tests (Slow, Costly, Brittle)}}_{\\approx 10\\%}",
      "legend": "• Anti-pattern 'Ice Cream Cone': Terlalu banyak manual/E2E test menyebabkan build sangat lambat dan rapuh terhadap perubahan UI kecil."
    },
    "hints": {
      "concept": "Unit test cepat dan murah dieksekusi, sehingga harus menjadi fondasi terbanyak. E2E test lambat dan mahal sehingga ditempatkan di puncak piramida.",
      "execution": "Pilihlah struktur: Unit Tests terbanyak di dasar, Integration di tengah, UI/E2E paling sedikit di puncak."
    },
    "explanation": "Piramida Pengujian menganjurkan struktur di mana Unit Test menjadi fondasi terbesar (cepat dieksekusi, murah, mengisolasi fungsi/metode secara spesifik), diikuti Integration Test pada lapisan tengah (memverifikasi interaksi antar-modul/database), dan E2E/UI Test dengan proporsi paling sedikit di puncak karena prosesnya lambat, berat sumber daya, dan rentan terhadap flakiness. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-06",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Pengelolaan Aset Git: Rebase Interaktif",
    "type": "mcq",
    "questionHtml": "Seorang programmer sedang merapikan riwayat commit lokal pada cabang fitur sebelum mengajukan Pull Request ke tim. Cabang tersebut memiliki 4 commit kecil berturut-turut yang hanya memperbaiki salah ketik: <code>fix typo 1</code>, <code>fix typo 2</code>, <code>fix lagi</code>, <code>fix final</code>. Perintah Git yang tepat untuk menggabungkan (squash) keempat commit tersebut menjadi satu commit deskriptif yang rapi adalah …",
    "options": [
      {
        "key": "A",
        "text": "`git rebase -i HEAD~4` lalu mengubah penanda pada commit kedua hingga keempat menjadi `squash` atau `s`."
      },
      {
        "key": "B",
        "text": "`git delete HEAD~4` dilanjutkan dengan memformat ulang drive komputer."
      },
      {
        "key": "C",
        "text": "`git clone --mirror` ke folder sementara dan menghapus riwayat log."
      },
      {
        "key": "D",
        "text": "`git push --all` ke server produksi tanpa review."
      },
      {
        "key": "E",
        "text": "`git revert HEAD~4` yang membatalkan seluruh kode yang telah diketik."
      }
    ],
    "formulaHud": {
      "title": "GIT WORKFLOW: INTERACTIVE REBASE SQUASH",
      "latex": "\\texttt{git rebase -i HEAD\\textasciitilde N} \\implies \\text{Linearize \\& Squash Commits } (C_1 + C_2 + C_3 \\to C_{\\text{clean}})",
      "legend": "• `pick`: Pertahankan commit.<br>• `squash` (s): Gabungkan commit ke commit sebelumnya dengan menyatukan pesan commit.<br>• Menghasilkan commit history yang bersih, atomik, dan mudah diaudit."
    },
    "hints": {
      "concept": "Perintah rebase interaktif dengan opsi -i memungkinkan pengembang menggabungkan beberapa commit riwayat lokal menjadi satu (squash).",
      "execution": "Pilihlah perintah `git rebase -i HEAD~4` dengan perintah `squash`."
    },
    "explanation": "Perintah `git rebase -i HEAD~4` membuka teks editor interaktif untuk 4 commit terakhir. Dengan mengubah kata kunci dari `pick` menjadi `squash` (atau `s`) pada commit-commit kecil perbaikan typo, Git akan melebur commit-commit tersebut ke commit awal sebelumnya menjadi satu commit terpadu, menjaga riwayat git tetap bersih dan informatif. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-07",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Keamanan Repositori & Penanganan Kebocoran Kredensial",
    "type": "mcq",
    "questionHtml": "Seorang anggota tim tanpa sengaja melakukan commit dan push file konfigurasi yang memuat <strong>Private API Secret Key</strong> layanan pembayaran ke repositori publik GitHub. Menghapus file tersebut melalui commit baru (<code>git rm file.env</code> dan <code>git push</code>) TIDAK MENYELESAIKAN masalah keamanan karena kunci rahasia masih tersimpan di dalam riwayat commit (<em>commit history</em>). Urutan prosedur darurat penanggulangan insiden (<em>incident response</em>) yang PALING TEPAT dan WAJIB dilakukan pertama kali adalah …",
    "options": [
      {
        "key": "A",
        "text": "Segera melakukan *Revoke / Invalidate* (mencabut dan merotasi) API Secret Key tersebut di dashboard penyedia layanan, kemudian membersihkan riwayat commit menggunakan alat seperti `git-filter-repo` atau BFG Repo-Cleaner."
      },
      {
        "key": "B",
        "text": "Menghapus akun GitHub pengembang dan berpura-pura insiden tersebut tidak pernah terjadi."
      },
      {
        "key": "C",
        "text": "Mengirim email massal kepada seluruh pengguna aplikasi meminta mereka tidak menyalin kunci rahasia tersebut."
      },
      {
        "key": "D",
        "text": "Mematikan server produksi selama 3 bulan hingga riwayat commit terhapus dengan sendirinya."
      },
      {
        "key": "E",
        "text": "Mengubah nama file di repositori menjadi `bukan_rahasia.txt`."
      }
    ],
    "formulaHud": {
      "title": "CREDENTIAL LEAK INCIDENT RESPONSE",
      "latex": "1.\\; \\text{Revoke \\& Rotate Key (Paling Utama)} \\quad \\to \\quad 2.\\; \\text{Audit Logs} \\quad \\to \\quad 3.\\; \\text{Purge History (git-filter-repo)}",
      "legend": "• Asumsi Keamanan: Begitu terdorong ke remote publik, kunci dianggap telah terkompromi (compromised) dalam hitungan detik oleh bot perayap publik."
    },
    "hints": {
      "concept": "Prioritas nomor satu saat kredensial bocor adalah mematikan fungsi kredensial itu (revoke & rotate) agar tidak dapat digunakan peretas, baru kemudian membersihkan riwayat commit.",
      "execution": "Pilihlah tindakan pencabutan (revoke) dan rotasi API key sesegera mungkin disusul pembersihan riwayat Git."
    },
    "explanation": "Prinsip utama penanganan kebocoran kredensial adalah: asumsikan kunci tersebut sudah terkompromi oleh bot pemindai publik dalam hitungan detik. Oleh karena itu, langkah pertama yang mutlak wajib dilakukan adalah me-revoke (membatalkan/mencabut) API Key lama di dashboard penyedia dan menerbitkan kunci baru (rotasi). Setelah akses peretas dinetralisasi, barulah riwayat repositori dibersihkan dengan `git-filter-repo` atau BFG Repo-Cleaner. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-08",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Business Continuity: Metrik RTO dan RPO",
    "type": "mcq",
    "questionHtml": "Dalam perancangan <em>Disaster Recovery Plan (DRP)</em> sistem perangkat lunak perbankan, tim arsitek menetapkan metrik: <strong>RTO = 15 Menit</strong> dan <strong>RPO = 0 Detik</strong>. Penjelasan makna teknis yang benar dari kombinasi target metrik tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Sistem wajib pulih dan beroperasi kembali maksimal dalam 15 menit setelah insiden (RTO), serta tidak boleh ada kehilangan data transaksi sama sekali (RPO 0 detik melalui replikasi sinkron)."
      },
      {
        "key": "B",
        "text": "Data hanya dibackup setiap 15 menit dan sistem diizinkan mati selama 0 hari."
      },
      {
        "key": "C",
        "text": "Pengguna harus menunggu 15 menit setiap kali melakukan transaksi transfer."
      },
      {
        "key": "D",
        "text": "Server dimatikan selama 15 menit setiap tengah malam untuk pendinginan mesin."
      },
      {
        "key": "E",
        "text": "Biaya operasional server turun sebesar 15% setiap transaksi bernilai 0 rupiah."
      }
    ],
    "formulaHud": {
      "title": "DISASTER RECOVERY METRICS: RTO VS RPO",
      "latex": "\\text{RTO (Recovery Time Objective)} = \\Delta t_{\\text{Downtime}} \\quad \\mid \\quad \\text{RPO (Recovery Point Objective)} = \\Delta t_{\\text{Max Data Loss}}",
      "legend": "• RTO: Batas waktu maksimal pemulihan sistem hingga online kembali.<br>• RPO: Batas toleransi maksimal data yang hilang (RPO = 0 artinya replikasi data real-time tanpa kehilangan 1 bit transaksi pun)."
    },
    "hints": {
      "concept": "RTO berkaitan dengan WAKTU pemulihan sistem (Downtime). RPO berkaitan dengan TITIK data yang hilang (Data Loss).",
      "execution": "RTO 15 menit = maksimal sistem mati 15 menit. RPO 0 detik = nol kehilangan data transaksi."
    },
    "explanation": "Recovery Time Objective (RTO) adalah durasi waktu maksimal yang ditoleransi untuk memulihkan sistem perangkat lunak setelah bencana terjadi (15 menit). Recovery Point Objective (RPO) adalah batas maksimal usia data yang boleh hilang diukur dalam waktu; RPO 0 detik berarti arsitektur menggunakan replikasi sinkron multi-region sehingga tidak ada satu pun transaksi yang hilang saat terjadi bencana. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-09",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Budaya Kerja: Blameless Post-Mortem",
    "type": "mcq",
    "questionHtml": "Setelah terjadi insiden <em>outage</em> sistem berskala besar akibat kesalahan konfigurasi seorang engineer junior, tim rekayasa perangkat lunak berkumpul untuk melakukan analisis insiden. Prinsip <strong>Blameless Post-Mortem</strong> yang dijunjung tinggi dalam budaya kerja rekayasa modern menginstruksikan bahwa pertemuan tersebut harus difokuskan pada …",
    "options": [
      {
        "key": "A",
        "text": "Mencari kambing hitam dan memberikan sanksi pemotongan gaji kepada engineer yang melakukan eksekusi perintah."
      },
      {
        "key": "B",
        "text": "Menganalisis kelemahan sistem, kegagalan guardrail/proses otomatisasi, serta merancang tindakan pencegahan sistemik agar kesalahan manusia yang sama tidak berakibat fatal di masa depan."
      },
      {
        "key": "C",
        "text": "Menghapus seluruh rekaman log insiden dari server agar tidak terlihat oleh auditor."
      },
      {
        "key": "D",
        "text": "Melarang seluruh engineer junior menyentuh papan ketik komputer selama 6 bulan."
      },
      {
        "key": "E",
        "text": "Menutup perusahaan dan mengembalikan modal kepada investor."
      }
    ],
    "formulaHud": {
      "title": "SRE CULTURE: BLAMELESS POST-MORTEM",
      "latex": "\\text{Focus: } \\frac{\\text{System Deficiencies \\& Missing Safeguards}}{\\text{Human Inevitability}} \\implies \\text{Continuous Systemic Resilience}",
      "legend": "• Premis SRE: Manusia pasti melakukan kesalahan (human error is inevitable).<br>• Jika kesalahan satu orang bisa meruntuhkan sistem, maka yang salah adalah arsitektur pelindungnya (lack of guardrails)."
    },
    "hints": {
      "concept": "Budaya blameless berfokus pada mengapa sistem mengizinkan kesalahan itu terjadi, bukan menghukum individu yang tidak sengaja melakukannya.",
      "execution": "Pilihlah opsi yang menekankan perbaikan sistem, guardrail, dan pencegahan sistemik."
    },
    "explanation": "Dalam budaya rekayasa perangkat lunak modern (Google SRE / DevOps), Blameless Post-Mortem berangkat dari prinsip bahwa kesalahan manusia tidak terelakkan. Fokus penyelidikan bukan menyalahkan individu, melainkan menganalisis faktor sistemik: mengapa sistem mengizinkan aksi berbahaya dijalankan tanpa konfirmasi otomatis, mengapa pengujian otomatis tidak mendeteksinya, dan bagaimana membangun guardrail pelindung untuk mencegah insiden berulang. Jawaban: B.",
    "isDiagnostic": false,
    "correctKey": "B"
  },
  {
    "id": "rpl-lat-h-10",
    "subject": "rpl",
    "materi": "KECAKAPAN KERJA DASAR, K3LH, DAN BUDAYA KERJA",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Keamanan Kredensial SSH & Izin Berkas Kunci Privat",
    "type": "mcq",
    "questionHtml": "Seorang pengembang mencoba menghubungkan komputer lokalnya ke server remote menggunakan kunci SSH privat: <code>ssh -i ~/.ssh/id_ed25519 user@10.0.0.1</code>. Namun, koneksi ditolak seketika oleh klien SSH dengan pesan:<br><pre><code>@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nPermissions 0777 for '/home/user/.ssh/id_ed25519' are too open.\nIt is required that your private key files are NOT accessible by others.\nLoad key \"/home/user/.ssh/id_ed25519\": bad permissions</code></pre>Perintah perbaikan izin berkas yang benar agar koneksi SSH dapat berjalan aman adalah …",
    "options": [
      {
        "key": "A",
        "text": "`chmod 600 ~/.ssh/id_ed25519`"
      },
      {
        "key": "B",
        "text": "`chmod 777 ~/.ssh/id_ed25519`"
      },
      {
        "key": "C",
        "text": "`rm -rf ~/.ssh`"
      },
      {
        "key": "D",
        "text": "`chown nobody ~/.ssh/id_ed25519`"
      },
      {
        "key": "E",
        "text": "`chmod 000 ~/.ssh/id_ed25519`"
      }
    ],
    "formulaHud": {
      "title": "SSH PRIVATE KEY SECURITY: PERMISSION MATRIX",
      "latex": "\\text{Kunci Privat SSH Wajib: } \\texttt{chmod 600} \\implies \\text{Owner Read+Write (rw-------), Group=None, Others=None}",
      "legend": "• Klien OpenSSH menolak memuat kunci privat jika group atau others memiliki hak akses apa pun.<br>• Izin 600 (atau 400) menjamin hanya pengguna pemilik yang berhak membaca berkas kunci."
    },
    "hints": {
      "concept": "File kunci privat SSH harus terlindungi ketat. Hanya pemilik file yang boleh membaca dan menulis (6 = 4+2), pengguna lain tidak boleh memiliki akses apa pun (00).",
      "execution": "Pilihlah perintah `chmod 600` untuk berkas private key."
    },
    "explanation": "Klien OpenSSH memiliki mekanisme keamanan ketat yang menolak menggunakan file kunci privat jika izin berkasnya terlalu longgar (misalnya 777). File privat hanya boleh diakses oleh pemiliknya sendiri secara eksklusif. Perintah `chmod 600 ~/.ssh/id_ed25519` memberikan hak baca dan tulis (rw-) hanya kepada pemilik, serta mencabut seluruh hak akses bagi grup dan orang lain (---), sehingga memenuhi persyaratan keamanan OpenSSH. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-11",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Perhitungan Subnetting VLSM IPv4 (/29)",
    "type": "mcq",
    "questionHtml": "Sebuah klaster server aplikasi mikroservis diberikan alokasi blok jaringan IPv4:<div class=\"net-spec-box\"><div class=\"net-spec-title\"><svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.2\"><circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z\"/></svg>Alokasi Blok Subnet CIDR Server</div><div class=\"net-spec-list\"><div class=\"net-spec-item\">🌐 <strong>Alamat Blok:</strong> <span class=\"net-ip-badge\">192.168.10.64/29</span></div></div></div>Berapakah jumlah alamat IP host yang VALID dan dapat digunakan untuk server, serta berapakah alamat Broadcast dari subnet tersebut?",
    "options": [
      {
        "key": "A",
        "text": "6 IP host valid (192.168.10.65 s.d. 192.168.10.70) dan Broadcast: 192.168.10.71"
      },
      {
        "key": "B",
        "text": "8 IP host valid (192.168.10.64 s.d. 192.168.10.71) dan Broadcast: 192.168.10.72"
      },
      {
        "key": "C",
        "text": "14 IP host valid (192.168.10.65 s.d. 192.168.10.78) dan Broadcast: 192.168.10.79"
      },
      {
        "key": "D",
        "text": "30 IP host valid (192.168.10.65 s.d. 192.168.10.94) dan Broadcast: 192.168.10.95"
      },
      {
        "key": "E",
        "text": "2 IP host valid (192.168.10.65 s.d. 192.168.10.66) dan Broadcast: 192.168.10.67"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "IPV4 SUBNETTING FORMULA: PREFIX /29",
      "latex": "H = 32 - 29 = 3 \\implies \\text{Total IP} = 2^3 = 8, \\quad \\text{Host Valid} = 2^3 - 2 = 6",
      "legend": "• Network Address: 192.168.10.64<br>• Rentang Host: 192.168.10.65 s.d. 192.168.10.70 (6 host)<br>• Broadcast Address: 192.168.10.64 + 7 = 192.168.10.71"
    },
    "hints": {
      "concept": "Prefix /29 menyisakan 32 - 29 = 3 bit untuk host. Total IP = 2^3 = 8. Host valid = 8 - 2 = 6.",
      "execution": "Hitung: 64 (Network). 65 s.d. 70 (Host). 71 (Broadcast)."
    },
    "explanation": "Pada subnet `/29`, jumlah bit host adalah 32 - 29 = 3 bit. Total alamat IP per subnet adalah 2^3 = 8 IP. Alamat network awal adalah 192.168.10.64. Alamat broadcast adalah alamat terakhir dari blok tersebut, yaitu 192.168.10.64 + 7 = 192.168.10.71. Jumlah IP host yang valid yang dapat digunakan perangkat adalah total dikurangi 2 (Network & Broadcast), yaitu 6 host, dengan rentang 192.168.10.65 hingga 192.168.10.70. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-12",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Linux Diagnostic Tools: Port & Socket Auditing",
    "type": "mcq",
    "questionHtml": "Seorang DevOps engineer ingin memastikan apakah server backend Node.js benar-benar sedang mendengarkan (<em>listening</em>) pada port TCP <code>3000</code> dan melihat Process ID (PID) program yang menjalankannya di Linux. Perintah utilitas modern yang PALING CEPAT dan tepat digunakan di terminal Linux adalah …",
    "options": [
      {
        "key": "A",
        "text": "`ss -tulpn | grep 3000`"
      },
      {
        "key": "B",
        "text": "`ping 3000`"
      },
      {
        "key": "C",
        "text": "`traceroute -p 3000`"
      },
      {
        "key": "D",
        "text": "`cat /etc/hosts`"
      },
      {
        "key": "E",
        "text": "`ifconfig eth0 down`"
      }
    ],
    "formulaHud": {
      "title": "LINUX SOCKET STATISTICS (SS) FLAGS",
      "latex": "\\texttt{ss -tulpn}: \\quad -t \\text{ (TCP)}, \\; -u \\text{ (UDP)}, \\; -l \\text{ (Listening)}, \\; -p \\text{ (Process/PID)}, \\; -n \\text{ (Numeric)}",
      "legend": "• `ss` adalah pengganti modern berkinerja tinggi untuk `netstat` usang di Linux kernel modern."
    },
    "hints": {
      "concept": "Perintah `ss` (Socket Statistics) dengan kombinasi flag tulpn menyaring port TCP/UDP yang sedang listening beserta nomor PID prosesnya.",
      "execution": "Pilihlah perintah `ss -tulpn` yang dipadukan dengan pipa `grep 3000`."
    },
    "explanation": "Perintah `ss` (Socket Statistics) adalah alat standar modern di Linux untuk memeriksa koneksi dan status socket jaringan. Flag `-t` (TCP), `-u` (UDP), `-l` (listening sockets), `-p` (menampilkan Process ID dan nama program), dan `-n` (menampilkan angka port numerik bukan nama layanan), jika dipadukan dengan `grep 3000`, akan secara instan menampilkan apakah port 3000 aktif beserta PID aplikasinya. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-13",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Protokol Transport: TCP 3-Way Handshake vs UDP Latency",
    "type": "mcq",
    "questionHtml": "Dalam pengembangan game aksi daring multiplayer kompetitif (FPS) berkecepatan tinggi, pergerakan posisi koordinat karakter pemain (<em>movement packet</em>) dikirimkan dari klien ke server menggunakan protokol <strong>UDP</strong>, bukan TCP. Alasan teknis utama di balik pemilihan UDP tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "TCP memiliki mekanisme retransmisi (ACK/Retransmission) dan Head-of-Line Blocking yang menyebabkan penundaan (latensi/lag) tinggi saat ada paket yang hilang, sedangkan UDP berorientasi pada kecepatan tanpa retransmisi paket usang."
      },
      {
        "key": "B",
        "text": "UDP secara otomatis meningkatkan daya baterai smartphone pemain sebesar dua kali lipat."
      },
      {
        "key": "C",
        "text": "Protokol TCP hanya dapat bekerja pada komputer yang terhubung kabel serat optik."
      },
      {
        "key": "D",
        "text": "UDP mengenkripsi seluruh grafik model 3D secara otomatis pada Layer 2."
      },
      {
        "key": "E",
        "text": "TCP melarang pengiriman data berupa angka desimal koordinat koordinat."
      }
    ],
    "formulaHud": {
      "title": "TRANSPORT LAYER: TCP VS UDP TRADE-OFF",
      "latex": "\\text{TCP: Reliability (ACK + 3-Way Handshake)} \\implies \\text{Higher Latency} \\quad \\mid \\quad \\text{UDP: Minimal Overhead} \\implies \\text{Lowest Latency}",
      "legend": "• Game real-time lebih mementingkan paket koordinat terbaru daripada menunggu retransmisi koordinat lama yang sudah kadaluarsa (obsolete)."
    },
    "hints": {
      "concept": "Pada data koordinat real-time, jika paket koordinat 1 detik lalu hilang, mengirim ulang paket lama itu tidak berguna karena sudah digantikan oleh posisi sekarang. Retransmisi TCP justru memicu lag.",
      "execution": "Pilihlah jawaban yang menyoroti retransmisi dan latensi TCP yang dihindari oleh UDP."
    },
    "explanation": "TCP menjamin keandalan pengiriman dengan mekanisme 3-Way Handshake, acknowledgement (ACK), dan pengiriman ulang (retransmisi) jika paket hilang, yang memicu fenomena Head-of-Line Blocking. Pada game real-time (seperti FPS), data pergerakan koordinat pemain harus tiba dengan latensi sekecil mungkin. Jika sebuah paket posisi hilang, pengiriman ulang tidak ada gunanya karena sudah digantikan oleh koordinat baru pemain. UDP dipilih karena tidak memiliki beban retransmisi sehingga meminimalkan lag. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-14",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Keamanan Web & Cross-Origin Resource Sharing (CORS)",
    "type": "mcq",
    "questionHtml": "Aplikasi Single Page Application (SPA) yang berjalan di <code>https://app.toko.com</code> melakukan permintaan AJAX POST dengan header kustom <code>Authorization: Bearer xyz</code> ke server backend di <code>https://api.toko.com/orders</code>. Sebelum permintaan POST sebenarnya dikirim, peramban web client secara otomatis mengirimkan permintaan pendahuluan (<em>Preflight Request</em>) dengan metode HTTP …",
    "options": [
      {
        "key": "A",
        "text": "OPTIONS"
      },
      {
        "key": "B",
        "text": "HEAD"
      },
      {
        "key": "C",
        "text": "CONNECT"
      },
      {
        "key": "D",
        "text": "TRACE"
      },
      {
        "key": "E",
        "text": "GET"
      }
    ],
    "formulaHud": {
      "title": "CORS PREFLIGHT MECHANISM",
      "latex": "\\text{Client Browser} \\xrightarrow{\\texttt{OPTIONS /orders}} \\text{Server API} \\xrightarrow{\\texttt{Access-Control-Allow-Origin}} \\text{Browser fires Actual POST}",
      "legend": "• Preflight OPTIONS: Memeriksa apakah server mengizinkan Origin pemanggil, HTTP Method yang dituju, dan Header kustom sebelum request utama dijalankan."
    },
    "hints": {
      "concept": "Mekanisme keamanan CORS pada peramban web mengirimkan HTTP OPTIONS request otomatis untuk mengecek izin server.",
      "execution": "Pilihlah metode HTTP OPTIONS."
    },
    "explanation": "Ketika permintaan lintas-origin (Cross-Origin) bukan merupakan 'Simple Request' (misalnya karena menggunakan header kustom Authorization atau format Content-Type: application/json), spesifikasi CORS W3C/WHATWG mewajibkan peramban mengirimkan Preflight Request menggunakan metode HTTP OPTIONS ke server tujuan untuk memastikan server mengizinkan interaksi tersebut. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-15",
    "subject": "rpl",
    "materi": "TEKNOLOGI JARINGAN KOMPUTER",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Infrastruktur Web: Reverse Proxy & SSL Termination",
    "type": "mcq",
    "questionHtml": "Dalam arsitektur perangkat lunak skala produksi, server <strong>Nginx</strong> sering ditempatkan di depan sekumpulan server aplikasi (seperti Node.js atau Python Gunicorn) sebagai <strong>Reverse Proxy</strong> dan menangani <em>SSL Termination</em>. Manfaat arsitektural utama dari konfigurasi ini adalah …",
    "options": [
      {
        "key": "A",
        "text": "Nginx membebaskan server aplikasi backend dari beban komputasi berat enkripsi/dekripsi HTTPS/TLS, sekaligus bertindak sebagai penyeimbang beban (Load Balancer) dan penyedia cache aset statis."
      },
      {
        "key": "B",
        "text": "Nginx otomatis menulis ulang kode logika backend menjadi bahasa mesin secara instan."
      },
      {
        "key": "C",
        "text": "Nginx menghapus seluruh sertifikat keamanan SSL agar situs dapat diakses tanpa kata sandi."
      },
      {
        "key": "D",
        "text": "Nginx menggantikan seluruh fungsi basis data relasional di server pusat."
      },
      {
        "key": "E",
        "text": "Nginx membatasi akses aplikasi sehingga hanya dapat dikunjungi oleh satu komputer saja dalam satu waktu."
      }
    ],
    "formulaHud": {
      "title": "REVERSE PROXY & SSL TERMINATION PATTERN",
      "latex": "\\text{Client} \\xrightarrow{\\text{HTTPS (TLS/SSL)}} \\underbrace{\\text{Nginx Reverse Proxy}}_{\\text{SSL Termination \\& Load Balancer}} \\xrightarrow{\\text{HTTP Internal}} \\text{App Servers (Node/Python)}",
      "legend": "• Keamanan terpusat (sertifikat SSL diatur di satu titik Nginx).<br>• Server aplikasi internal fokus pada eksekusi kode bisnis tanpa overhead kriptografi TLS."
    },
    "hints": {
      "concept": "SSL termination membongkar enkripsi HTTPS di layer reverse proxy sehingga server backend internal hanya memproses data secara ringan dan efisien.",
      "execution": "Pilihlah jawaban yang menjelaskan offloading enkripsi SSL, load balancing, dan caching aset."
    },
    "explanation": "Menjadikan Nginx sebagai Reverse Proxy dengan SSL Termination memusatkan manajemen sertifikat keamanan TLS di satu gerbang depan. Nginx menangani beban pemrosesan kriptografi TLS yang intensif, mendistribusikan beban lalu lintas (Load Balancing) ke server backend, serta melayani berkas statis (gambar, JS, CSS) dengan efisiensi tinggi, membebaskan server aplikasi untuk memproses logika bisnis murni. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-16",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Trace Rekursi & Kondisi Basis (Base Case)",
    "type": "mcq",
    "questionHtml": "Perhatikan fungsi rekursif berikut:<br><pre><code class=\"language-python\">def misteri(n):\n    if n <= 1:\n        return 1\n    return n * misteri(n - 2)\n\nprint(misteri(5))</code></pre>Berapakah nilai yang dicetak oleh pemanggilan <code>misteri(5)</code> di atas?",
    "options": [
      {
        "key": "A",
        "text": "15"
      },
      {
        "key": "B",
        "text": "120"
      },
      {
        "key": "C",
        "text": "25"
      },
      {
        "key": "D",
        "text": "5"
      },
      {
        "key": "E",
        "text": "Error: RecursionError / Stack Overflow"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "RECURSION TRACE WITH STEP-2",
      "latex": "m(5) = 5 \\times m(3) = 5 \\times (3 \\times m(1)) = 5 \\times 3 \\times 1 = 15",
      "legend": "• Langkah 1: misteri(5) = 5 * misteri(3)<br>• Langkah 2: misteri(3) = 3 * misteri(1)<br>• Langkah 3: misteri(1) memenuhi `n <= 1` (Base Case), mengembalikan 1.<br>• Unwinding: 5 * 3 * 1 = 15 (perkalian bilangan ganjil)."
    },
    "hints": {
      "concept": "Perhatikan pengurangan pada pemanggilan rekursif: n - 2, bukan n - 1.",
      "execution": "Lacak runtutan: 5 * misteri(3) -> 5 * (3 * misteri(1)) -> 5 * 3 * 1 = 15."
    },
    "explanation": "Pemanggilan `misteri(5)` menghasilkan evaluasi rantai: `5 * misteri(3)`. Kemudian `misteri(3)` mengevaluasi `3 * misteri(1)`. Karena pada `misteri(1)` nilai `n = 1` memenuhi kondisi basis `n <= 1`, fungsi mengembalikan angka 1. Hasil totalnya adalah `5 * 3 * 1 = 15`. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-17",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Python LEGB Scope Rule (UnboundLocalError)",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode program Python berikut:<br><pre><code class=\"language-python\">x = 10\n\ndef ubah():\n    print(x)\n    x = 20\n\nubah()</code></pre>Apa yang terjadi ketika fungsi <code>ubah()</code> dipanggil?",
    "options": [
      {
        "key": "A",
        "text": "Mencetak 10 lalu variabel x berubah menjadi 20."
      },
      {
        "key": "B",
        "text": "Terjadi UnboundLocalError karena x dianggap variabel lokal (akibat assignment x = 20), tetapi dirujuk oleh print(x) sebelum diberi nilai inisialisasi."
      },
      {
        "key": "C",
        "text": "Mencetak 20."
      },
      {
        "key": "D",
        "text": "Mencetak None."
      },
      {
        "key": "E",
        "text": "Program berjalan tanpa output apa pun."
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "PYTHON LEGB SCOPE RESOLUTION",
      "latex": "\\text{Assignment } (x = 20) \\implies x \\in \\text{Local Scope} \\implies \\text{print}(x) \\text{ references unassigned local variable}",
      "legend": "• Python memindai seluruh tubuh fungsi saat kompilasi ke bytecode. Jika ada assignment ke variabel x di mana pun dalam fungsi, x otomatis ditandai sebagai Local variable untuk seluruh fungsi.<br>• Akses baca sebelum baris assignment memicu `UnboundLocalError`."
    },
    "hints": {
      "concept": "Di Python, penugasan variabel (`x = 20`) di dalam fungsi menyebabkan variabel tersebut menjadi lokal di seluruh tubuh fungsi tersebut, sehingga pembacaan sebelumnya menjadi invalid.",
      "execution": "Pilihlah opsi yang menjelaskan terjadinya UnboundLocalError."
    },
    "explanation": "Pada Python, keberadaan baris `x = 20` di dalam fungsi `ubah()` menyebabkan kompilator menetapkan bahwa `x` adalah variabel lokal (local scope) di sepanjang fungsi tersebut. Akibatnya, ketika baris `print(x)` mencoba membaca nilai `x` sebelum baris penugasan `x = 20` dieksekusi, Python melemparkan `UnboundLocalError: local variable 'x' referenced before assignment`. Untuk membaca dan mengubah variabel global, diperlukan deklarasi eksplisit `global x`. Jawaban: B.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-18",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Jebakan Mutabilitas Parameter Default (Mutable Default Arguments)",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode fungsi berikut:<br><pre><code class=\"language-python\">def tambah_data(item, daftar=[]):\n    daftar.append(item)\n    return daftar\n\na = tambah_data(\"Apel\")\nb = tambah_data(\"Jeruk\")\nprint(a, b)</code></pre>Output yang dicetak oleh program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "['Apel', 'Jeruk'] ['Apel', 'Jeruk']"
      },
      {
        "key": "B",
        "text": "['Apel'] ['Jeruk']"
      },
      {
        "key": "C",
        "text": "['Apel'] ['Apel', 'Jeruk']"
      },
      {
        "key": "D",
        "text": "['Jeruk'] ['Jeruk']"
      },
      {
        "key": "E",
        "text": "Error: Default argument cannot be a list"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "PYTHON MUTABLE DEFAULT ARGUMENT TRAP",
      "latex": "\\text{Default arg } \\texttt{daftar=[]} \\text{ dievaluasi HANYA SEKALI saat definisi fungsi} \\implies \\text{Objek list dibagi bersama}",
      "legend": "• List adalah objek mutable.<br>• Pemanggilan pertama: `daftar` diisi 'Apel'.<br>• Pemanggilan kedua: `daftar` yang sama diisi 'Jeruk'.<br>• Variabel a dan b merujuk pada objek list yang sama di memori."
    },
    "hints": {
      "concept": "Di Python, parameter default dibuat sekali saat fungsi didefinisikan, bukan setiap kali fungsi dipanggil. Menggunakan objek mutable (seperti list []) menyimpan riwayat modifikasi sebelumnya.",
      "execution": "Kedua variabel menunjuk ke list yang sama yang sekarang berisi Apel dan Jeruk."
    },
    "explanation": "Ini adalah perilaku klasik Python yang dikenal sebagai 'Mutable Default Argument Trap'. Argumen default `daftar=[]` dibuat satu kali saja saat fungsi didefinisikan. Pada pemanggilan pertama `tambah_data('Apel')`, list default dimodifikasi berisi `['Apel']`. Pada pemanggilan kedua `tambah_data('Jeruk')`, list default yang sama dimodifikasi kembali sehingga menjadi `['Apel', 'Jeruk']`. Variabel `a` dan `b` keduanya merujuk ke objek list yang sama, sehingga dicetak `['Apel', 'Jeruk'] ['Apel', 'Jeruk']`. Solusi yang benar adalah menggunakan `daftar=None`. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-19",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Optimasi Kompleksitas Algoritma (Two-Pointer O(N))",
    "type": "mcq",
    "questionHtml": "Diberikan sebuah list bilangan bulat yang <strong>telah terurut menaik</strong> (misal: <code>[2, 7, 11, 15]</code>) dan sebuah target jumlah <code>target = 9</code>. Programmer ingin mencari dua bilangan yang jika dijumlahkan menghasilkan target tersebut. Strategi algoritma terstruktur dengan efisiensi waktu <strong>O(N)</strong> dan efisiensi ruang <strong>O(1)</strong> yang paling optimal adalah …",
    "options": [
      {
        "key": "A",
        "text": "Menggunakan teknik Dua Penunjuk (Two-Pointer): satu penunjuk di awal (kiri) dan satu di akhir (kanan), lalu menggeser penunjuk berdasarkan perbandingan jumlah dengan target."
      },
      {
        "key": "B",
        "text": "Menggunakan dua perulangan bersarang (nested loops) untuk mencoba semua kombinasi pasangan elemen secara brute force."
      },
      {
        "key": "C",
        "text": "Mengacak urutan list berulang kali sampai secara kebetulan menemukan pasangan yang cocok."
      },
      {
        "key": "D",
        "text": "Mengonversi seluruh angka menjadi string lalu menghitung jumlah karakter spasi."
      },
      {
        "key": "E",
        "text": "Menghapus seluruh angka ganjil sebelum melakukan pencarian."
      }
    ],
    "formulaHud": {
      "title": "TWO-POINTER ALGORITHM ON SORTED ARRAY",
      "latex": "S = A[\\text{left}] + A[\\text{right}] \\implies \\begin{cases} \\text{left}++ & \\text{if } S < \\text{target} \\\\ \\text{right}-- & \\text{if } S > \\text{target} \\\\ \\text{FOUND} & \\text{if } S = \\text{target} \\end{cases}",
      "legend": "• Waktu: $O(N)$ (hanya satu lintasan).<br>• Ruang: $O(1)$ (tidak memerlukan memori tambahan hash table)."
    },
    "hints": {
      "concept": "Karena array sudah terurut, kita bisa memanfaatkan dua penunjuk di ujung kiri dan kanan. Jika jumlah terlalu kecil, geser penunjuk kiri ke kanan. Jika terlalu besar, geser penunjuk kanan ke kiri.",
      "execution": "Pilihlah teknik Two-Pointer."
    },
    "explanation": "Pada array yang sudah terurut, teknik Dua Penunjuk (Two-Pointer) adalah solusi paling optimal dengan kompleksitas waktu linier O(N) dan memori konstan O(1). Penunjuk kiri dimulai dari indeks 0 dan penunjuk kanan dari indeks terakhir (N-1). Jika jumlah kedua elemen lebih kecil dari target, penunjuk kiri digeser maju; jika lebih besar, penunjuk kanan digeser mundur. Ini jauh lebih efisien dibandingkan nested loops yang berbiaya O(N^2). Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-20",
    "subject": "rpl",
    "materi": "PEMROGRAMAN TERSTRUKTUR",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Struktur Data Hash Map & Pencarian O(1)",
    "type": "mcq",
    "questionHtml": "Dalam sistem pemrosesan jutaan data transaksi e-commerce, programmer perlu sering memeriksa keberadaan ID transaksi pelanggan. Struktur data di bawah ini yang menyediakan operasi pencarian elemen rata-rata berkinerja paling cepat, yaitu berbiaya waktu <strong>O(1)</strong> (waktu konstan), adalah …",
    "options": [
      {
        "key": "A",
        "text": "Hash Map / Dictionary (menggunakan fungsi hash untuk pemetaan kunci langsung ke lokasi memori)"
      },
      {
        "key": "B",
        "text": "Singly Linked List tak terurut (pencarian linier O(N))"
      },
      {
        "key": "C",
        "text": "Array biasa tak terurut (pencarian linier O(N))"
      },
      {
        "key": "D",
        "text": "Queue berbasis antrean FIFO (pencarian O(N))"
      },
      {
        "key": "E",
        "text": "File teks sekuensial yang dibaca baris per baris dari harddisk"
      }
    ],
    "formulaHud": {
      "title": "TIME COMPLEXITY: HASH LOOKUP",
      "latex": "\\text{Hash Function: } h(k) \\to \\text{Index} \\implies \\text{Average Lookup Time} = \\mathcal{O}(1)",
      "legend": "• Hash Map / Dictionary: Memetakan key ke nilai dengan direct memory indexing.<br>• Bandingkan dengan Array tak terurut: Memeriksa elemen satu per satu memerlukan $O(N)$."
    },
    "hints": {
      "concept": "Pencarian berbiaya konstan O(1) memanfaatkan fungsi hash yang langsung memetakan kunci unik ke alamat memori penyimpanan.",
      "execution": "Pilihlah Hash Map / Dictionary."
    },
    "explanation": "Struktur data Hash Map (dikenal sebagai Dictionary di Python atau HashMap di Java) menggunakan fungsi hash matematis untuk mengonversi kunci menjadi indeks array internal. Rata-rata operasi pencarian, penyisipan, dan penghapusan bernilai konstan O(1), sangat ideal untuk pencarian data bervolume besar dibandingkan array atau linked list yang memerlukan waktu O(N). Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-21",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Multiple Inheritance & Method Resolution Order (MRO)",
    "type": "mcq",
    "questionHtml": "Perhatikan hierarki pewarisan berganda (<em>Multiple Inheritance / Diamond Problem</em>) di Python berikut:<br><pre><code class=\"language-python\">class A:\n    def halo(self):\n        return \"A\"\n\nclass B(A):\n    def halo(self):\n        return \"B\"\n\nclass C(A):\n    def halo(self):\n        return \"C\"\n\nclass D(B, C):\n    pass\n\nd = D()\nprint(d.halo())</code></pre>Output yang dicetak oleh program di atas beserta aturan penentu urutan pencarian method-nya adalah …",
    "options": [
      {
        "key": "A",
        "text": "B, karena algoritma C3 Linearization pada Method Resolution Order (MRO) memeriksa class B sebelum class C."
      },
      {
        "key": "B",
        "text": "C, karena class C didefinisikan paling akhir."
      },
      {
        "key": "C",
        "text": "A, karena class A adalah superclass puncak."
      },
      {
        "key": "D",
        "text": "Error: DiamondInheritanceAmbiguityError."
      },
      {
        "key": "E",
        "text": "None, karena class D hanya berisi pass."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OOP: PYTHON C3 LINEARIZATION (MRO)",
      "latex": "\\text{MRO}(D) = [D, B, C, A, \\text{object}] \\implies d.\\text{halo}() \\text{ menemukan } B.\\text{halo}() \\text{ pertama kali}",
      "legend": "• Urutan pendefinisian: `class D(B, C)` mengutamakan class B dari kiri ke kanan.<br>• Method Resolution Order menjamin urutan eksekusi method deterministik tanpa ambiguitas."
    },
    "hints": {
      "concept": "Di Python, pewarisan berganda diatur oleh MRO (Method Resolution Order) dari kiri ke kanan. D mewarisi B lalu C, sehingga method di B akan dipanggil pertama.",
      "execution": "D tidak punya method halo, maka cari ke B. B memiliki halo() yang mengembalikan 'B'."
    },
    "explanation": "Python menyelesaikan masalah ambiguitas pewarisan berganda (Diamond Problem) menggunakan algoritma C3 Linearization yang menghasilkan Method Resolution Order (MRO). Karena class `D` didefinisikan sebagai `class D(B, C)`, urutan pencariannya adalah `[D, B, C, A, object]`. Saat `d.halo()` dipanggil, method ditemukan pertama kali pada class `B`, sehingga mencetak 'B'. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-22",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Desain OOP: Dependency Inversion & Loose Coupling",
    "type": "mcq",
    "questionHtml": "Perhatikan rancangan dua class sistem pelaporan berikut:<br><pre><code class=\"language-python\">class MySQLDatabase:\n    def simpan(self, data):\n        print(\"Simpan ke MySQL:\", data)\n\nclass LaporanPenjualan:\n    def __init__(self):\n        self.db = MySQLDatabase() # Ketergantungan langsung (Tight Coupling)\n    def proses(self, data):\n        self.db.simpan(data)</code></pre>Kelemahan arsitektur perangkat lunak pada rancangan class <code>LaporanPenjualan</code> di atas beserta solusi refaktorisasi terbaik sesuai prinsip SOLID adalah …",
    "options": [
      {
        "key": "A",
        "text": "Tight Coupling (terikat erat); jika ingin mengganti database ke PostgreSQL, kode LaporanPenjualan harus diubah. Solusinya: terapkan Dependency Injection dengan menyuntikkan objek database dari luar melalui parameter constructor."
      },
      {
        "key": "B",
        "text": "LaporanPenjualan tidak boleh memiliki fungsi simpan sama sekali."
      },
      {
        "key": "C",
        "text": "Nama variabel harus selalu diawali dengan tiga tanda garis bawah."
      },
      {
        "key": "D",
        "text": "MySQLDatabase harus dihapus dan diganti dengan variabel string lokal biasa."
      },
      {
        "key": "E",
        "text": "Class LaporanPenjualan seharusnya mewarisi secara langsung seluruh fungsi sistem operasi."
      }
    ],
    "formulaHud": {
      "title": "SOLID: DEPENDENCY INVERSION PRINCIPLE",
      "latex": "\\text{High-level } (\\text{Laporan}) \\text{ tidak boleh instansiasi langsung } \\text{Low-level } (\\text{MySQL}) \\implies \\text{Inject Dependency via } \\texttt{\\_\\_init\\_\\_}(self, db)",
      "legend": "• Tight Coupling: Keterikatan keras membuat pengujian (unit testing/mocking) dan penggantian komponen menjadi sangat sulit."
    },
    "hints": {
      "concept": "Melakukan `new` atau instansiasi langsung modul konkret di dalam constructor menciptakan keterikatan keras (tight coupling).",
      "execution": "Pilihlah solusi yang menyebutkan keterikatan erat (tight coupling) dan perbaikan melalui Dependency Injection."
    },
    "explanation": "Pada kode tersebut, `LaporanPenjualan` menginstansiasi langsung `MySQLDatabase()` di dalam constructor-nya. Ini menciptakan keterikatan keras (Tight Coupling) dan melanggar Dependency Inversion Principle. Jika sistem ingin diuji dengan mock database atau beralih ke PostgreSQL, kode `LaporanPenjualan` harus dimodifikasi ulang. Solusi terbaik adalah Dependency Injection: objek database dilewatkan sebagai argumen constructor `def __init__(self, db): self.db = db`. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-23",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Abstract Base Class & Kontrak Antarmuka",
    "type": "mcq",
    "questionHtml": "Perhatikan perancangan kelas abstrak Python berikut:<br><pre><code class=\"language-python\">from abc import ABC, abstractmethod\n\nclass Pembayaran(ABC):\n    @abstractmethod\n    def bayar(self, jumlah):\n        pass\n\nclass PembayaranQRIS(Pembayaran):\n    pass\n\np = PembayaranQRIS()</code></pre>Apa yang terjadi ketika baris terakhir <code>p = PembayaranQRIS()</code> dijalankan?",
    "options": [
      {
        "key": "A",
        "text": "Terjadi TypeError karena PembayaranQRIS belum mengimplementasikan method abstrak bayar(), sehingga tidak dapat diinstansiasi."
      },
      {
        "key": "B",
        "text": "Objek berhasil dibuat dan method bayar otomatis mengembalikan angka nol."
      },
      {
        "key": "C",
        "text": "Sistem membuka kamera smartphone secara otomatis untuk memindai kode QR."
      },
      {
        "key": "D",
        "text": "Class Pembayaran otomatis terhapus dari sistem."
      },
      {
        "key": "E",
        "text": "Program mencetak None tanpa error."
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OOP: ABSTRACT METHOD ENFORCEMENT",
      "latex": "\\text{SubClass} \\text{ without implementation of } @abstractmethod \\implies \\text{TypeError: Can't instantiate abstract class}",
      "legend": "• Kelas abstrak bertindak sebagai kontrak wajib.<br>• Setiap subclass konkret WAJIB melakukan override pada seluruh method berdekorator `@abstractmethod`."
    },
    "hints": {
      "concept": "Kelas yang mewarisi `ABC` dan memiliki method abstrak tidak dapat diinstansiasi menjadi objek jika subclass belum mengimplementasikan method abstrak tersebut.",
      "execution": "Pilihlah opsi yang menyebutkan TypeError kegagalan instansiasi kelas abstrak."
    },
    "explanation": "Modul `abc` (Abstract Base Classes) pada Python menerapkan penegakan kontrak antarmuka secara ketat. Ketika sebuah subclass (`PembayaranQRIS`) mewarisi kelas abstrak (`Pembayaran`) tetapi tidak meng-override method yang diberi dekorator `@abstractmethod` (`bayar`), Python melarang instansiasi kelas tersebut dan melemparkan `TypeError: Can't instantiate abstract class PembayaranQRIS with abstract method bayar`. Jawaban: A.",
    "isDiagnostic": false
  },
  {
    "id": "rpl-lat-h-24",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Design Pattern: Pola Perancangan Observer",
    "type": "mcq",
    "questionHtml": "Dalam sistem gim petualangan daring, ketika status kesehatan (HP) karakter pemain berubah menjadi 0 (mati), berbagai modul perlu segera merespons secara otomatis: modul Audio memutar efek suara kematian, modul UI menampilkan layar Game Over, dan modul Server mengirim status ke database. Pola desain berorientasi objek (<em>Design Pattern</em>) yang PALING TEPAT digunakan agar entitas Pemain tidak terikat erat dengan ketiga modul tersebut adalah …",
    "options": [
      {
        "key": "A",
        "text": "Observer Pattern (Publisher-Subscriber)"
      },
      {
        "key": "B",
        "text": "Singleton Pattern"
      },
      {
        "key": "C",
        "text": "Flyweight Pattern"
      },
      {
        "key": "D",
        "text": "Adapter Pattern"
      },
      {
        "key": "E",
        "text": "Prototype Pattern"
      }
    ],
    "formulaHud": {
      "title": "DESIGN PATTERN: OBSERVER (PUB-SUB)",
      "latex": "\\text{Subject (Karakter)} \\xrightarrow{\\text{notify()}} \\begin{cases} \\text{Audio Observer} \\\\ \\text{UI Observer} \\\\ \\text{Database Observer} \\end{cases}",
      "legend": "• Menetapkan relasi one-to-many antar objek.<br>• Ketika status Subject berubah, semua Observer yang terdaftar akan diberitahu dan diperbarui secara otomatis tanpa keterikatan keras."
    },
    "hints": {
      "concept": "Pola di mana satu objek (Subject) memberi tahu banyak objek lain (Observers/Listeners) saat terjadi peristiwa tertentu tanpa perlu tahu detail implementasi mereka.",
      "execution": "Pilihlah Observer Pattern (atau Publish-Subscribe)."
    },
    "explanation": "Observer Pattern (sering diimplementasikan sebagai sistem Event Listener / Publisher-Subscriber) mendefinisikan relasi satu-ke-banyak di mana ketika objek subjek (Pemain) mengalami perubahan status (misal kematian), ia secara otomatis memberi tahu (notify) seluruh observer terdaftar (Audio, UI, Jaringan) tanpa perlu mengetahui detail internal dari masing-masing observer tersebut, menjaga arsitektur tetap loosely coupled. Jawaban: A.",
    "isDiagnostic": false,
    "correctKey": "A"
  },
  {
    "id": "rpl-lat-h-25",
    "subject": "rpl",
    "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Objek Mutabel: Shallow Copy vs Deep Copy",
    "type": "mcq",
    "questionHtml": "Perhatikan potongan kode manipulasi objek dan referensi memori berikut:<br><pre><code class=\"language-python\">import copy\n\nclass Karakter:\n    def __init__(self, nama, atribut):\n        self.nama = nama\n        self.atribut = atribut\n\nk1 = Karakter(\"Ksatria\", {\"hp\": 100, \"mp\": 50})\nk2 = copy.copy(k1) # Shallow Copy\nk2.nama = \"Pemanah\"\nk2.atribut[\"hp\"] = 80\n\nprint(k1.nama, k1.atribut[\"hp\"])</code></pre>Output yang dicetak oleh baris terakhir program di atas adalah …",
    "options": [
      {
        "key": "A",
        "text": "Ksatria 80"
      },
      {
        "key": "B",
        "text": "Ksatria 100"
      },
      {
        "key": "C",
        "text": "Pemanah 80"
      },
      {
        "key": "D",
        "text": "Pemanah 100"
      },
      {
        "key": "E",
        "text": "Error: ShallowCopyException"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "OOP MEMORY: SHALLOW COPY VS DEEP COPY",
      "latex": "k_1.\\text{atribut} \\equiv k_2.\\text{atribut} \\implies \\text{Perubahan atribut bersarang pada } k_2 \\text{ ikut mengubah } k_1",
      "legend": "• Shallow Copy (`copy.copy`): Menggandakan objek terluar, namun atribut yang berupa objek bersarang (seperti dictionary) hanya disalin alamat referensinya.<br>• Untuk menggandakan struktur bersarang secara terisolasi penuh, wajib menggunakan `copy.deepcopy()`."
    },
    "hints": {
      "concept": "Shallow copy menyalin objek utama, tetapi objek bersarang (dictionary atribut) tetap merujuk pada alamat memori yang sama.",
      "execution": "k2.nama diganti 'Pemanah' tidak mempengaruhi k1.nama ('Ksatria'). Tetapi k2.atribut['hp'] = 80 mengubah dictionary bersama, sehingga k1.atribut['hp'] juga menjadi 80."
    },
    "explanation": "Pada Shallow Copy (`copy.copy`), objek `k2` dibuat sebagai objek instans baru terpisah dari `k1`, sehingga perubahan `k2.nama = 'Pemanah'` tidak mengubah `k1.nama` (tetap 'Ksatria'). Namun, atribut bersarang yang merupakan objek mutabel (`self.atribut` berupa dictionary) hanya disalin alamat referensi memorinya. Akibatnya, `k1.atribut` dan `k2.atribut` menunjuk pada dictionary yang sama di memori. Mengubah `k2.atribut['hp'] = 80` ikut mengubah `k1.atribut['hp']` menjadi 80. Jawaban: A.",
    "isDiagnostic": false
  }
]

print('Loaded 25 items.')
