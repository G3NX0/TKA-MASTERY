# -*- coding: utf-8 -*-
"""
Script to generate the exhaustive Master Prompt for Claude Expansion (>= 5,000 words).
Outputs:
  - docs/MASTER_PROMPT_CLAUDE_EXPANSION.md
  - docs/master_prompt_printable.html
  - docs/MASTER_PROMPT_CLAUDE_EXPANSION.pdf (via msedge headless)
"""

import os
import subprocess

def generate_master_prompt():
    prompt_text = """# MASTER ARCHITECTURAL PROMPT: PENGEMBANGAN KURIKULUM HOTS, EKSPANSI 19 MATA UJI PILIHAN, DAN REFACTOR UI/UX ENGINE PADA TKA MASTERY HUB

---

## BAGIAN I: IDENTITAS SISTEM, DIREKTIF PERILAKU, DAN EFISIENSI TOKEN

### 1.1 Peran dan Persona Profesional
Anda bertindak sebagai **Principal Assessment Architect, Lead Pedagogical Engineer, dan Senior Fullstack/UI-UX Designer**. Anda memiliki otoritas teknis tertinggi dalam merancang instrumen evaluasi standar nasional Indonesia (Pusmendik / Pusat Asesmen Pendidikan Kemendikbudristek) dan Kurikulum Merdeka Fase F (SMA/MA Kelas 11 dan 12). 

Tugas Anda bukan memberikan ceramah teoritis, bukan berbasa-basi, dan bukan memuji keputusan yang medioker. Tugas Anda adalah:
1. Membaca dan menganalisis seluruh spesifikasi arsitektur platform TKA Mastery Hub secara holistik.
2. Membuat **Implementation Plan (Rencana Eksekusi Bertahap)** yang presisi, terukur, dan bebas celah logika sebelum memproduksi artefak kode.
3. Memproduksi bank soal asli (authentic question bank) untuk seluruh mata pelajaran pilihan jenjang SMA dengan standar HOTS (Higher Order Thinking Skills) autentik tanpa ada satu pun butir soal duplikat.
4. Menyediakan artefak data dalam format kode produksi JavaScript modular (`data/questions_[mapel].js`) yang siap pakai tanpa memerlukan perbaikan format tambahan dari pihak pengguna.
5. Memperbaiki dan memperhalus defisit UI/UX yang masih ada di antarmuka pengujian (khususnya tata letak navigasi footer di tablet/desktop dan integrasi typesetting KaTeX) dengan standar aksesibilitas WCAG AAA dan Apple Human Interface Guidelines.

### 1.2 Aturan Anti-Verbosity dan Konservasi Token (Token FinOps Guardrail)
Pengguna memiliki model Claude tingkat tinggi dengan jendela konteks dan kuota token yang substansial. Namun, kuota tersebut tidak boleh disia-siakan untuk obrolan repetitif atau kalimat pengantar yang tidak bernilai guna (*zero token slop*). Anda terikat oleh aturan komunikasi ketat berikut:
- **Dilarang Keras Berbasa-basi:** Jangan memulai respon dengan kalimat pembuka seperti "Tentu, saya akan membantu Anda", "Senang sekali bekerja sama", atau "Baik, berikut adalah...". Langsung mulai dari judul dokumen, rencana eksekusi, atau blok data kode.
- **Rencana Eksekusi Di Awal:** Sebelum mengeluarkan data soal atau patch kode, sajikan *Implementation Plan* ringkas berbasis tabel atau checklist terstruktur mengenai target cakupan topik, alokasi tingkat kognitif, dan struktur file yang akan diproduksi.
- **Eksekusi Langsung (Action-First):** Berikan hasil produksi data yang utuh. Jangan memotong kode dengan komentar malas seperti `// lanjutkan soal 5 sampai 135 seperti contoh di atas...`. Setiap butir soal harus ditulis secara lengkap dan valid secara sintaksis.
- **Penyerahan Hasil yang Dapat Ditempel Langsung:** Seluruh bank soal wajib dibungkus dalam blok kode JavaScript mandiri yang menyuntikkan data ke namespace global `window.TKA_[MAPEL_KEY]_QUESTIONS`, sehingga pengguna dapat menyimpannya langsung ke dalam berkas tanpa perlu melakukan konversi format manual.

---

## BAGIAN II: SPESIFIKASI ARSITEKTUR PLATFORM TKA MASTERY HUB

### 2.1 Arsitektur Aplikasi Klien (Single Page Application - Vanilla JS Engine)
Platform TKA Mastery Hub dibangun tanpa framework berat (No React, No Vue, No Tailwind). Arsitektur aplikasi sepenuhnya berbasis Vanilla JavaScript murni, Semantic HTML5, dan Custom Modular CSS yang dirancang untuk performa ekstrem dengan latensi nol. Komponen inti arsitektur meliputi:
1. **View Router Monolitik:** Dikelola melalui fungsi `navigateTo(viewName, subjectKey)` di `app.js` yang mengatur empat kontainer tampilan utama:
   - `#viewHome`: Tampilan beranda dengan hero banner asesmen diagnostik, dek 3D panorama cockpit interaktif, switch kategori kelompok mapel (Wajib vs Lanjutan), dan katalog 19 mapel pilihan.
   - `#viewSubject`: Launchpad dedicated per mata pelajaran yang memisahkan jalur latihan santai (Training Lab) dengan 3 level kesulitan (Mudah, Sedang, Sulit) dan jalur simulasi terikat waktu (Exam Arena).
   - `#viewWorkspace`: Workstation pengerjaan soal dengan split-paper layout, formula drawer, clue drawer bertingkat, sticky timer HUD, navigasi nomor soal adaptif, dan modal audit konfirmasi pengumpulan.
   - `#viewResults`: Dashboard pasca-ujian dengan visualisasi radar kompetensi, rincian skor per topik, breakdown akurasi, dan mode review kunci jawaban anti-spoiler.
2. **Sistem Database Modular Terdesentralisasi:**
   Setiap mata pelajaran dikelola dalam berkas skrip terpisah di direktori `data/questions_[mapel].js`. Berkas-berkas ini mendefinisikan array global `window.TKA_[MAPEL_KEY]_QUESTIONS`. Berkas agregator pusat `data/questions_db.js` bertugas mendaftarkan array tersebut ke dalam objek utama `window.TKA_DATABASE` dan mengelola metadata 19 mata pelajaran pilihan pada `window.TKA_ELECTIVE_CATALOG`.

### 2.2 Desain Visual Cyber Neo-Brutalism & Glassmorphism
Antarmuka TKA Mastery Hub mengadopsi estetika *Dark Cyber Cockpit* dengan palet obsidian gelap yang dipadukan dengan aksen neon fungsional:
- **Canvas Base:** Obsidian Primer (`#07090e`), Glass Elevation (`#0f1420`), Elevated Surface (`#161e30`).
- **Aksen Tematik Mapel:**
  - Matematika Wajib: Electric Cobalt (`#2563eb`) & Cyan Glow (`#60a5fa`).
  - Bahasa Indonesia Wajib: Vivid Emerald (`#059669`) & Mint Glow (`#34d399`).
  - Bahasa Inggris Wajib: Warm Amber (`#d97706`) & Gold Glow (`#fbbf24`).
  - Matematika Lanjutan: Deep Cyan / Aqua Neon (`#0891b2` & `#22d3ee`).
  - Bahasa Indonesia Lanjutan: Teal Forest (`#0d9488` & `#2dd4bf`).
  - Bahasa Inggris Lanjutan: Cyber Purple / Violet Neon (`#7e22ce` & `#c084fc`).
- **Typography & Typesetting:** Menggunakan font Inter dan SF Pro Text untuk teks narasi, JetBrains Mono untuk metrik data angka/timer, serta KaTeX v0.16.9 untuk rendering rumus matematis dan notasi ilmiah.

---

## BAGIAN III: STANDARISASI KURIKULUM PUSMENDIK DAN TAKSONOMI BLOOM FASE F

### 3.1 Kerangka Regulasi dan Capaian Pembelajaran (BSKAP No. 033/H/KR/2024)
Seluruh materi uji wajib merujuk secara ketat pada Capaian Pembelajaran Fase F (Kelas 11–12 SMA) sesuai ketetapan Badan Standar, Kurikulum, dan Asesmen Pendidikan (BSKAP) serta kisi-kisi Asesmen Bakat Minat (ABM) dan Tes Kemampuan Akademik (TKA) resmi Pusmendik. Standar ini menuntut:
1. **Konteks Nyata (Real-World Contextual Grounding):** Tidak ada soal yang menanyakan definisi hafalan kosong atau rumus teoritis tanpa terapan. Setiap butir soal harus diikat pada fenomena alam, isu sosiologis, studi rekayasa teknologi, data ekonomi terkini, atau wacana kebudayaan otentik.
2. **Distribusi Tingkat Kognitif Taksonomi Bloom Terevisi:**
   - **Tingkat Mudah (Easy - C1/C2 Kontekstual):** Mengidentifikasi fakta dari wacana, menghitung parameter tunggal dengan variabel terdefinisi jelas, atau membaca informasi eksplisit dari grafik dan tabel.
   - **Tingkat Sedang (Medium - C3/C4 Analitis):** Mengkorelasikan dua atau lebih konsep yang berbeda, mendiagnosis sebab-akibat suatu anomali fisis/sosial, menginterpretasikan data tren majemuk, atau mengeliminasi hipotesis yang tidak konsisten dengan data stimulus.
   - **Tingkat Sulit (Hard - C4-C6 Evaluatif & Kreasi Solutif):** Mengambil keputusan strategis berbasis multi-kriteria, membuktikan rumus dalam kondisi batas tertentu, mengevaluasi validitas argumen dalam teks kontradiktif, atau merumuskan model matematis dari suatu persoalan dunia nyata yang kompleks.

### 3.2 Karakteristik dan Spesifikasi Wacana Stimulus HOTS
Wacana stimulus merupakan fondasi utama dari setiap soal standar Pusmendik. Anda wajib mematuhi parameter berikut:
- **Panjang Stimulus:** Wacana harus memiliki panjang antara **120 hingga 180 kata**. Hindari wacana terlalu pendek yang menghilangkan konteks (di bawah 50 kata) dan hindari wacana terlalu panjang seperti artikel koran penuh (di atas 300 kata) yang menguras habis durasi ujian 30 menit.
- **Kepadatan Informasi:** Stimulus wajib memuat data kuantitatif atau kualitatif yang konkret: tabel ringkas (3-4 baris), kutipan argumen dari dua perspektif, parameter eksperimen fisika/kimia, diagram alir proses, atau analogi fungsional.
- **Independensi Kunci:** Pertanyaan inti tidak boleh menanyakan hal sepele yang dapat dijawab langsung dengan membaca sepintas. Jawaban harus menuntut pemrosesan mental: sintesis informasi dari teks digabungkan dengan penguasaan konsep esensial mapel.

---

## BAGIAN IV: KATALOG LENGKAP 19 MATA UJI PILIHAN JENJANG SMA

Platform TKA Mastery Hub menyediakan katalog 19 mata pelajaran pilihan jenjang SMA. Anda bertugas menyusun bank soal lengkap untuk seluruh 19 mata pelajaran berikut sesuai silabus resmi:

### RUMPUN MIPA / SAINTEK & TEKNOLOGI
1. **Fisika (ID: `fisika`, Prefix: `fis_`):**
   - *Cakupan Topik:* Kinematika Vektor, Dinamika Partikel & Gravitasi Newton, Usaha & Energi Potensial, Momentum & Impuls Tumbukan, Fluida Statis & Dinamis, Termodinamika & Siklus Carnot, Gelombang Bunyi & Cahaya (Efek Doppler, Difraksi), Elektrostatika & Rangkaian Arus Searah/Bolak-Balik, Induksi Elektromagnetik Faraday-Lenz, Teori Relativitas Khusus, dan Pengantar Fisika Kuantum.
   - *Target Kompetensi:* Pemodelan matematis gerak fisis, analisis grafik hubungan variabel, perhitungan kesetimbangan energi, dan analisis eksperimen laboratorium.
2. **Kimia (ID: `kimia`, Prefix: `kim_`):**
   - *Cakupan Topik:* Struktur Atom & Teori Mekanika Kuantum, Sistem Periodik & Ikatan Kimia (Kovalen, Logam, Intermolekuler), Stoikiometri Reaksi Larutan & Gas, Termokimia & Hukum Hess, Kinetika Reaksi & Orde Reaksi, Kesetimbangan Kimia ($K_c, K_p$), Larutan Asam-Basa & Penyangga (Buffer), Kelarutan & Hasil Kali Kelarutan ($K_{sp}$), Sifat Koligatif Larutan, Elektrokimia (Sel Volta & Elektrolisis), Kimia Karbon & Gugus Fungsi Organik, Makromolekul (Polimer, Karbohidrat, Protein).
   - *Target Kompetensi:* Perhitungan kuantitatif stoikiometris, interpretasi diagram fasa, penentuan potensial sel, penulisan mekanisme reaksi, dan analisis bahaya bahan kimia.
3. **Biologi (ID: `biologi`, Prefix: `bio_`):**
   - *Cakupan Topik:* Struktur & Transport Membran Sel, Enzim & Katabolisme/Anabolisme Respirasi Seluler, Sintesis Protein & Kode Genetik, Pembelahan Sel (Mitosis & Meiosis), Pola Hereditas Mendel & Penyimpangan Semu, Mutasi Gen & Kromosom, Bioteknologi Konvensional & Modern (CRISPR, Kultur Jaringan), Fisiologi Tumbuhan (Fotosintesis, Fitohormon), Fisiologi Sistem Organ Manusia (Saraf, Imun, Endokrin), Ekologi Populasi & Biogeokimia, serta Teori & Mekanisme Evolusi.
   - *Target Kompetensi:* Analisis diagram jalur biokimia, pemecahan silsilah pewarisan sifat (pedigree chart), evaluasi respon imun, dan analisis data gangguan ekosistem.
4. **Matematika Tingkat Lanjut (ID: `mtk-lanjut`, Prefix: `mtkl_`):**
   - *Cakupan Topik:* Polinomial, Operasi Aljabar Suku Banyak, Teorema Sisa & Faktor, Matriks Ordo $3 \times 3$, Invers & Determinan Sistem Persamaan Linear, Vektor Ruang Dimensi Tiga (Dot & Cross Product), Geometri Analitik Bidang (Irisan Kerucut: Parabola, Elips, Hiperbola), Limit Fungsi Aljabar & Trigonometri di Titik Tertentu dan Tak Hingga, Turunan Fungsi Trigonometri & Aplikasinya, dan Integral Substitusi/Parsial Luas & Volume Benda Putar.
   - *Target Kompetensi:* Pembuktian analitis aljabar abstrak, transformasi spasial geometris 3D, dan dekomposisi kalkulus diferensial-integral lanjutan.
5. **Informatika (ID: `informatika`, Prefix: `inf_`):**
   - *Cakupan Topik:* Berpikir Komputasional (Dekomposisi, Pola, Abstraksi), Notasi Algoritma Pseudocode & Flowchart, Struktur Data Linear (Stack, Queue, Array), Struktur Data Non-Linear (Binary Tree, Graph Berbobot), Analisis Kompleksitas Waktu Algoritma ($O(1), O(n), O(n \log n)$), Arsitektur Komputer & Organisasi Sistem Operasi, Protokol Jaringan & Model TCP/IP, Alamat IPv4/IPv6 & Subnetting, Keamanan Siber (Enkripsi, Serangan Phishing/DDoS), serta Analisis Dampak Sosial Informatika dan Etika Kecerdasan Buatan.
   - *Target Kompetensi:* Penelusuran trace eksekusi kode algoritma, identifikasi bug logis, perancangan skema subnet jaringan, dan evaluasi kerentanan keamanan sistem.
6. **Teknik Rekayasa Perangkat Lunak (RPL) (ID: `rpl`, Prefix: `rpl_`):**
   - *Cakupan Topik:* Metodologi Pengembangan Perangkat Lunak (Agile, Scrum, Waterfall), Analisis Kebutuhan Sistem & Pemodelan Diagram UML (Use Case, Class Diagram, Activity Diagram), Pemrograman Berorientasi Objek (OOP: Encapsulation, Inheritance, Polymorphism, Abstraction), Pemrograman Web Frontend & Backend (REST API, CRUD), Manajemen Basis Data Relasional (SQL, Normalisasi Database 1NF-3NF, Foreign Key Constraints), Pengujian Perangkat Lunak (Unit Testing, Integration Testing, Whitebox/Blackbox), Version Control System (Git branching, merge, pull request), dan Penerapan Desain Arsitektur MVC.
   - *Target Kompetensi:* Analisis kode modular OOP, penyusunan query SQL kompleks (JOIN, GROUP BY, HAVING), pembacaan diagram kelas UML, dan perancangan skenario unit testing perangkat lunak.
7. **Teknik Komputer & Rekayasa Jaringan (TKJ) (ID: `tkj`, Prefix: `tkj_`):**
   - *Cakupan Topik:* Topologi Jaringan Komputer Fisis & Logis, Standar Kabel UTP & Fiber Optic, Konfigurasi Switch & Router (Routing Statis, OSPF, RIP), Konsep Virtual LAN (VLAN & Trunking 802.1Q), Layanan Server Jaringan (DHCP, DNS, Web Server, FTP, Proxy), Keamanan Jaringan Firewall (Packet Filtering, NAT, DMZ), Pemantauan Jaringan & Analisis Trafik (Wireshark, SNMP, Bandwidth Management), Jaringan Nirkabel (Wireless Standard 802.11, WPA2/WPA3 Encryption), dan Perawatan serta Troubleshooting Masalah Jaringan Lokal (LAN).
   - *Target Kompetensi:* Diagnosa pesan error jaringan melalui traceroute/ping, kalkulasi subnetting VLSM/CIDR, penentuan aturan access-list firewall, dan pemecahan masalah konektivitas client-server.

### RUMPUN IPS / SOSHUM & HUMANIORA
8. **Ekonomi (ID: `ekonomi`, Prefix: `eko_`):**
   - *Cakupan Topik:* Kelangkaan & Biaya Peluang, Mekanisme Pasar Bebas (Permintaan, Penawaran, Elastisitas Harga & Silang), Struktur Pasar (Persaingan Sempurna, Monopoli, Oligopoli), Teori Perilaku Konsumen (Utilitas Ordinal/Kardinal) & Produsen (Isoquant-Isocost), Pendapatan Nasional (GDP, GNP, NNI, Pendapatan Per Kapita, Indeks Gini), Inflasi & Pengangguran, Kebijakan Fiskal (Pajak, APBN/APBD) & Kebijakan Moneter (Operasi Pasar Terbuka, Diskonto, Giro Wajib Minimum), Perdagangan Internasional & Neraca Pembayaran, Kurs Valuta Asing, serta Akuntansi Dasar (Persamaan Dasar, Jurnal Umum, Buku Besar, Penyesuaian, dan Laporan Keuangan Neraca/Laba Rugi).
   - *Target Kompetensi:* Interpretasi kurva pergeseran ekuilibrium pasar, pemodelan matematis elastisitas dan fungsi laba maksimum, analisis dampak intervensi suku bunga acuan, dan pencatatan transaksi jurnal akuntansi.
9. **Geografi (ID: `geografi`, Prefix: `geo_`):**
   - *Cakupan Topik:* Prinsip Dasar & Pendekatan Geografi (Spasial, Ekologis, Kompleks Wilayah), Kartografi & Interpretasi Citra Penginderaan Jauh, Sistem Informasi Geografis (SIG) & Pemodelan Layer Peta Spasial, Dinamika Litosfer (Tektonisme Lempeng, Vulkanisme, Seisme, Pelapukan), Atmosfer & Iklim (Lapisan Atmosfer, Klasifikasi Iklim Koppen/Schmidt-Ferguson, El Nino/La Nina), Hidrosfer (Siklus Air, DAS, Konservasi Air Tanah), Dinamika Biosfer & Persebaran Bioma Dunia/Fauna Wallace-Weber, Antroposfer & Demografi (Piramida Penduduk, Mortalitas, Migrasi), Pengelolaan Sumber Daya Alam Berkelanjutan, serta Mitigasi Bencana Alam dan Tata Ruang Wilayah Pedesaan-Perkotaan.
   - *Target Kompetensi:* Analisis spasial citra satelit, penghitungan skala peta kontur interval, evaluasi daya dukung lahan lingkungan, dan perancangan strategi mitigasi risiko kebencanaan.
10. **Sosiologi (ID: `sosiologi`, Prefix: `sos_`):**
    - *Cakupan Topik:* Objek Kajian Sosiologi & Tokoh Klasik (Durkheim, Marx, Weber), Interaksi Sosial & Pembentukan Lembaga/Institusi Sosial, Sosialisasi & Pembentukan Kepribadian, Nilai dan Norma Sosial, Perilaku Menyimpang & Teori Pengendalian Sosial, Struktur Sosial & Stratifikasi/Diferensiasi Sosial, Hubungan Antar-Kelompok & Harmoni Sosial, Dinamika Konflik Sosial & Resolusi Kekerasan, Perubahan Sosial dalam Masyarakat Modern & Globalisasi, Masalah Ketimpangan Sosial Struktural di Indonesia, Kearifan Lokal & Pemberdayaan Komunitas, serta Metodologi Penelitian Sosial (Kualitatif Etnografi vs Kuantitatif Survei).
    - *Target Kompetensi:* Dekonstruksi akar masalah konflik horizontal, analisis data statistik ketimpangan sosial, penerapan teori sosiologis terhadap fenomena disrupsi digital, dan evaluasi etika riset empiris.
11. **Sejarah Tingkat Lanjut (ID: `sejarah-lanjut`, Prefix: `sejl_`):**
    - *Cakupan Topik:* Metodologi Penelitian Sejarah & Kritik Sumber (Heuristik, Kritik Ekstern/Intern, Interpretasi, Historiografi), Peradaban Kuno Dunia dan Pengaruhnya Terhadap Hukum dan Pemerintahan, Dinamika Kerajaan Hindu-Buddha dan Islam di Nusantara Jalur Rempah, Kolonialisme & Imperialisme Bangsa Barat di Indonesia, Strategi Pergerakan Nasional & Lahirnya Kesadaran Kebangsaan (1908-1945), Pendudukan Militer Jepang & Proklamasi Kemerdekaan, Revolusi Fisik & Diplomasi Mempertahankan Kemerdekaan (1945-1949), Demokrasi Parlementer & Demokrasi Terpimpin, Perang Dingin & Gerakan Non-Blok, Orde Baru hingga Era Reformasi 1998, dan Konflik Geopolitik Global Kontemporer.
    - *Target Kompetensi:* Uji validitas kredibilitas arsip primer vs sekunder, analisis kausalitas dialektis peristiwa sejarah besar, identifikasi bias perspektif historiografi, dan kontekstualisasi peristiwa masa lalu dengan kebijakan masa kini.
12. **Antropologi (ID: `antropologi`, Prefix: `ant_`):**
    - *Cakupan Topik:* Pengantar Antropologi & Konsep Kebudayaan (Wujud Kebudayaan, Unsur Universal Kebudayaan), Antropologi Ragawi/Biologis & Evolusi Fisik Manusia, Keragaman Etnolinguistik & Pemetaan Suku Bangsa di Indonesia, Sistem Kekerabatan & Struktur Perkawinan Adat (Patrilineal, Matrilineal, Bilateral), Sistem Religi, Mitos, Ritual & Simbolisme Tradisional, Sistem Mata Pencaharian Tradisional & Pertukaran Resiprositas/Redistribusi, Dinamika Budaya (Akulturasi, Asimilasi, Difusi, Inkulturasi), Folklor Tradisi Lisan & Pelestarian Warisan Budaya Takbenda, serta Isu-isu Antropologi Terapan (Multikulturalisme, Hak Masyarakat Adat, Konflik Antar-Suku).
    - *Target Kompetensi:* Penghindaran etnosentrisme melalui penerapan prinsip relativisme budaya, pembedahan bagan silsilah kekerabatan masyarakat adat, dan analisis simbolik makna ritual kebudayaan.

### RUMPUN BAHASA & SASTRA
13. **Bahasa & Sastra Indonesia Lanjut (ID: `indo-lanjut`, Prefix: `indl_`):**
    - *Cakupan Topik:* Morfologi & Proses Pembentukan Kata Majemuk, Sintaksis Kalimat Transformasional & Kalimat Efektif Akademik, Semantik Makna Leksikal, Gramatikal, Pergeseran Makna (Peyoratif, Amelioratif), Kajian Wacana Kritis (Critical Discourse Analysis), Stilistika Bahasa & Majas Retorika dalam Teks Pidato, Kritik Sastra Berbagai Pendekatan (Strukturalisme, Sosiologi Sastra, Psikoanalisis), Analisis Unsur Intrinsik & Ekstrinsik Puisi/Prosa/Drama Kontemporer, dan Teknik Penulisan Esai Argumentatif Ilmiah Berbasis Korpus Bahasa.
    - *Target Kompetensi:* Dekonstruksi ideologi terselubung dalam wacana publik, apresiasi estetika stilistika karya sastra pemenang penghargaan, analisis ambiguitas semantis klausa kompleks, dan rekonstruksi teks formal sesuai PUEBI.
14. **Bahasa & Sastra Inggris Lanjut (ID: `inggris-lanjut`, Prefix: `engl_`):**
    - *Cakupan Topik:* Advanced Syntax & Inversion Structures, Subjunctive Mood & Complex Conditionals, Rhetorical Devices (Metaphor, Irony, Hyperbole, Litotes) in Authentic Literary Excerpts, Critical Discourse Analysis of Editorial Articles, Synthesis of Multi-Text Perspectives (CEFR B2 to C1 Academic Level), British and American Classical & Modern Prose Deconstruction, Academic Argumentation & Counter-Argument Refutation, and Formal Tone Register Differentiation.
    - *Target Kompetensi:* Evaluating authorial bias and tone, extracting implicit inferences from nuanced texts, identifying structural coherence in academic expositions, and resolving complex grammatical constraints.
15. **Bahasa Arab (ID: `bahasa-arab`, Prefix: `arb_`):**
    - *Cakupan Topik:* Kaidah Nahwu Terapan (I'rab Kalimat: Marfu'at, Manshubat, Majrurat), Isim Mu'rab & Isim Mabni, Susunan Idhafah & Na'at Man'ut, Kaidah Shorof (Tashrif Lughawi & Istilahi Wazan Kata Kerja Fi'il Tsulatsi Mujarrad/Mazid), Pemahaman Teks Faktual Kontemporer Tanpa Harakat (Gundul), Kosakata Tematik Pendidikan, Sains, dan Hubungan Internasional, serta Pengenalan Balaghah Dasar (Tasybih, Majaz Haqiqi/Majazi).
    - *Target Kompetensi:* Menganalisis kedudukan sintaksis harakat akhir kata dalam kalimat, membaca dan menyimpulkan wacana berita berbahasa Arab, dan memilih pasangan kata kerja-huruf jar yang tepat.
16. **Bahasa Jepang (ID: `bahasa-jepang`, Prefix: `jpn_`):**
    - *Cakupan Topik:* Penguasaan Kanji Standar SMA/N4-N3, Pola Kalimat dan Tatabahasa (Bunpou: Bentuk Syarat ~tara/~ba/~nara, Bentuk Pasif/Kausatif ~seru/~rareru), Ungkapan Tingkat Kesopanan Bahasa (Sonkeigo, Kenjougo, Teineigo), Pemahaman Wacana Panjang (Dokkai) Bertema Budaya, Teknologi, dan Kehidupan Sehari-hari Jepang, serta Frasa Idiomatik Percakapan Bisnis/Formal.
    - *Target Kompetensi:* Membaca wacana faktual ber-kanji secara tepat, menentukan ekspresi kesopanan sesuai hierarki sosial penutur, dan menyimpulkan implikasi tersembunyi dalam dialog percakapan.
17. **Bahasa Mandarin (ID: `bahasa-mandarin`, Prefix: `man_`):**
    - *Cakupan Topik:* Karakter Hanzi Esensial (Goresan & Radikal Pembentuk Makna), Struktur Kalimat Dasar & Kompleks (SPO, Kalimat Partikel 把 bǎ dan 被 bèi), Aspek Waktu & Partikel Aspektual (了 le, 过 guò, 着 zhe), Komposisi Kata Hubung Majemuk (Bukan hanya... melainkan... 不但...而且...), Pemahaman Wacana Membaca Standar HSK Level 3–4, dan Pemahaman Konteks Budaya Peribahasa Chengyu Populer.
    - *Target Kompetensi:* Membaca teks bertuliskan Hanzi tanpa pinyin, mendeteksi kesalahan tata bahasa letak kata keterangan/partikel, dan menganalisis ide pokok wacana deskriptif/eksposisi.
18. **Bahasa Jerman (ID: `bahasa-jerman`, Prefix: `ger_`):**
    - *Cakupan Topik:* Deklinasi Artikel dan Kata Benda pada Kasus Nominativ, Akkusativ, Dativ, dan Genitiv, Preposisi Bergantung Kasus (Wechselpräpositionen), Kata Kerja Modal & Separable Verbs (Trennbare Verben), Konjugasi Waktu Lampau (Perfekt & Präteritum), Subordinate Clauses (Nebensatz: weil, dass, wenn, obwohl), Pengantar Konjunktiv II untuk Kalimat Pengandaian Sopan, serta Pemahaman Teks Tertulis (Leseverstehen) Standar CEFR A2–B1.
    - *Target Kompetensi:* Menentukan akhiran adjektiva sesuai deklinasi gramatikal yang tepat, merekonstruksi urutan kata kerja di akhir klausa anak (Nebensatz), dan membedah wacana tematik lingkungan/kehidupan remaja Jerman.
19. **Bahasa Prancis (ID: `bahasa-prancis`, Prefix: `fra_`):**
    - *Cakupan Topik:* Sistem Kala Bahasa Prancis (Passé Composé vs Imparfait, Futur Simple, Conditionnel Présent), Kata Ganti Objek Langsung dan Tak Langsung (COD/COI: le, la, les, lui, leur, y, en), Kesesuaian Partisip Lampau (Accord du Participe Passé), Kalimat Pengandaian dengan 'Si', Struktur Kalimat Negasi Kompleks (ne... jamais, ne... plus, ne... rien), serta Pemahaman Wacana Teks Standar DELF A2–B1.
    - *Target Kompetensi:* Memilih aspek kala lampau yang tepat sesuai konteks aksi tuntas vs deskripsi latar, menggantikan frasa nomina dengan pronomina yang benar, dan menarik simpulan dari teks argumentasi singkat.
20. **Bahasa Korea (ID: `bahasa-korea`, Prefix: `kor_`):**
    - *Cakupan Topik:* Konstruksi Kalimat Hangeul Lanjutan, Sistem Partikel Kasus Subjek, Objek, Topik, Lokasi, dan Arah, Tingkatan Tutur Kehormatan (Formal Deferensial -seupnida, Informal Sopan -yo, serta Honorifik Kosakata Khusus), Pola Konjungsi Kompleks Pengandaian, Sebab-Akibat, dan Kontradiksi (~eumyeon, ~nikka, ~jiman, ~neunde), Bentuk Waktu Lampau, Sedang, dan Masa Depan, serta Pemahaman Teks Narasi/Wawancara Standar TOPIK I Level 2 s/d TOPIK II Level 3.
    - *Target Kompetensi:* Menganalisis ketepatan pemakaian partikel kehormatan dalam konteks sosial formal, mengidentifikasi tujuan komunikasi penutur dalam wacana dialog, dan menyimpulkan isi paragraf berita populer Korea.
21. **Teknik Rekayasa & Desain (ID: `rekayasa-desain`, Prefix: `tekd_`):**
    - *Cakupan Topik:* Prinsip Dasar Rekayasa Desain (Design Thinking: Empathize, Define, Ideate, Prototype, Test), Ergonomi Fisik & Antropometri dalam Desain Produk, Dasar Kekuatan Bahan Teknik & Pemilihan Material (Logam, Polimer, Komposit), Pembacaan Gambar Teknik Proyeksi Ortogonal & Isometrik Standar ISO, Dasar Mekatronika Sederhana (Sensor, Aktuator, Rangkaian Logika Kontrol), Siklus Hidup Produk (Product Life Cycle), dan Analisis Kegagalan Desain serta Kepatuhan Standar Keamanan Fungsional Produk.
    - *Target Kompetensi:* Membaca dan menginterpretasi dimensi gambar teknik mesin/arsitektur, mengevaluasi kesesuaian antropometri terhadap rancangan kursi/meja kerja kerja ergonomis, dan merancang alur solusi rekayasa terhadap persoalan mekanis.

---

## BAGIAN V: STRUKTUR DATA SOAL, VALIDASI TIPE, DAN ATURAN KATEX

### 5.1 Skema Objek Soal JavaScript
Setiap butir soal wajib didefinisikan sebagai objek JavaScript murni dalam array global:
```javascript
window.TKA_[MAPEL_KEY]_QUESTIONS = [
  // Tipe 1: Single Choice (Pilihan Ganda A-E)
  {
    id: "fis_001",
    type: "single_choice",
    difficulty: "medium", // "easy" | "medium" | "hard"
    topic: "Dinamika Partikel & Hukum Newton",
    stimulus: "Sebuah balok bermassa $m_1 = 4\\text{ kg}$ berada di atas bidang miring kasar dengan sudut kemiringan $\\theta = 30^\\circ$ terhadap horizontal. Koefisien gesek kinetik antara balok dan permukaan bidang miring adalah $\\mu_k = 0{,}2$. Balok tersebut dihubungkan dengan tali ringan tak elastis melewati katrol licin tanpa gesekan ke balok kedua bermassa $m_2 = 6\\text{ kg}$ yang tergantung bebas secara vertikal. Percepatan gravitasi bumi diasumsikan $g = 10\\text{ m/s}^2$. Sistem dilepaskan dari keadaan diam pada saat $t = 0$.",
    question: "Besar percepatan gerak kedua balok dan tegangan tali penghubung sesaat setelah sistem dilepaskan berturut-turut adalah...",
    options: {
      A: "$3{,}31\\text{ m/s}^2$ dan $40{,}1\\text{ N}$",
      B: "$3{,}31\\text{ m/s}^2$ dan $33{,}1\\text{ N}$",
      C: "$4{,}24\\text{ m/s}^2$ dan $34{,}6\\text{ N}$",
      D: "$4{,}24\\text{ m/s}^2$ dan $40{,}1\\text{ N}$",
      E: "$5{,}12\\text{ m/s}^2$ dan $29{,}3\\text{ N}$"
    },
    correctAnswer: "A",
    clues: [
      "Clue 1: Uraikan gaya-gaya pada balok pertama di sepanjang bidang miring: komponen berat sejajar bidang $m_1 g \\sin\\theta$, gaya gesek $f_k = \\mu_k m_1 g \\cos\\theta$, dan tegangan tali $T$.",
      "Clue 2: Terapkan Hukum II Newton $\\Sigma F = m_{total} a$ secara simultan untuk kedua benda: $m_2 g - T - m_1 g \\sin\\theta - f_k = (m_1 + m_2) a$."
    ],
    solution: "1. Komponen gaya normal pada bidang miring: $N = m_1 g \\cos 30^\\circ = 4 \\times 10 \\times \\frac{\\sqrt{3}}{2} \\approx 34{,}64\\text{ N}$.\\n2. Gaya gesek kinetik: $f_k = \\mu_k N = 0{,}2 \\times 34{,}64 \\approx 6{,}93\\text{ N}$.\\n3. Gaya penarik vertikal balok kedua: $W_2 = m_2 g = 6 \\times 10 = 60\\text{ N}$. Komponen berat balok 1: $W_{1x} = m_1 g \\sin 30^\\circ = 20\\text{ N}$.\\n4. Resultan gaya: $\\Sigma F = W_2 - W_{1x} - f_k = 60 - 20 - 6{,}93 = 33{,}07\\text{ N}$.\\n5. Percepatan sistem: $a = \\frac{\\Sigma F}{m_1 + m_2} = \\frac{33{,}07}{10} \\approx 3{,}31\\text{ m/s}^2$.\\n6. Tegangan tali: $T = m_2(g - a) = 6(10 - 3{,}31) = 6 \\times 6{,}69 \\approx 40{,}14\\text{ N}$."
  },

  // Tipe 2: Complex Table (Pilihan Ganda Kompleks Benar / Salah)
  {
    id: "fis_014",
    type: "complex_table",
    difficulty: "hard",
    topic: "Termodinamika & Efisiensi Mesin",
    stimulus: "Siklus Carnot hipotetis beroperasi di antara reservoir suhu tinggi $T_H = 800\\text{ K}$ dan reservoir suhu rendah $T_C = 400\\text{ K}$. Dalam satu siklus lengkap, mesin menyerap kalor sebesar $Q_H = 2400\\text{ J}$ dari reservoir panas. Seorang insinyur mengusulkan modifikasi dengan menaikkan suhu reservoir tinggi sebesar $100\\text{ K}$ atau menurunkan suhu reservoir rendah sebesar $100\\text{ K}$ dengan biaya operasional yang sama.",
    question: "Berdasarkan prinsip hukum Termodinamika, tentukan kebenaran dari setiap pernyataan evaluatif berikut!",
    tableStatements: [
      {
        text: "Efisiensi awal mesin sebelum modifikasi adalah tepat sebesar $50\\%$.",
        answer: "B"
      },
      {
        text: "Menurunkan suhu reservoir rendah menjadi $300\\text{ K}$ menghasilkan kenaikan efisiensi yang lebih besar daripada menaikkan suhu reservoir tinggi menjadi $900\\text{ K}$.",
        answer: "B"
      },
      {
        text: "Kalor yang dibuang ke reservoir dingin pada siklus awal sebelum modifikasi adalah sebesar $1600\\text{ J}$.",
        answer: "S"
      }
    ],
    correctAnswer: { "0": "B", "1": "B", "2": "S" },
    clues: [
      "Clue 1: Rumus efisiensi ideal mesin Carnot adalah $\\eta = 1 - \\frac{T_C}{T_H}$.",
      "Clue 2: Evaluasi turunan parsial efisiensi terhadap $T_C$ dan $T_H$ untuk membandingkan sensitivitas perubahan suhu."
    ],
    solution: "1. Efisiensi mula-mula: $\\eta_1 = 1 - \\frac{400}{800} = 0{,}50 = 50\\%$ (Pernyataan 1 BENAR).\\n2. Skenario A (naikkan $T_H$): $\\eta_A = 1 - \\frac{400}{900} = 1 - 0{,}444 = 55{,}56\\%$. Skenario B (turunkan $T_C$): $\\eta_B = 1 - \\frac{300}{800} = 1 - 0{,}375 = 62{,}5\\%$. Kenaikan pada Skenario B lebih tinggi secara signifikan (Pernyataan 2 BENAR).\\n3. Kalor yang dibuang pada siklus awal: $Q_C = Q_H(1 - \\eta) = 2400(1 - 0{,}5) = 1200\\text{ J}$, bukan $1600\\text{ J}$ (Pernyataan 3 SALAH)."
  }
];
```

### 5.2 Protokol KaTeX & LaTeX Rendering (Bebas Bocor Sintaks)
- **Aturan Double Backslash:** Di dalam string JavaScript, semua perintah LaTeX wajib menggunakan double backslash: `\\frac`, `\\sqrt`, `\\Delta`, `\\theta`, `\\mu`, `\\times`, `\\int`, `\\approx`. Jika hanya ditulis satu backslash `\f`, interpreter JavaScript akan mengubahnya menjadi karakter kontrol *form-feed* (`\x0c`) dan merusak tampilan browser.
- **Pembatas Eksplisit:** Setiap formula inline wajib diawali dan diakhiri tanda dollar `$formula$`, dan formula blok tengah wajib menggunakan `$$formula$$`. Dilarang menampilkan teks matematis telanjang tanpa pembatas (misal: `1/2 gt^2` harus ditulis `$\\frac{1}{2}gt^2$`).
- **Standardisasi Desimal:** Penulisan koma desimal Indonesia di dalam formula matematika LaTeX wajib menggunakan kurung kurawal `0{,}5` atau spasi tipis agar KaTeX tidak menganggap koma sebagai pemisah argumen fungsi (yang menghasilkan spasi terlalu lebar jika ditulis `$0,5$`).

---

## BAGIAN VI: ELIMINASI BIAS & ALGORITMA INTERLEAVED SHUFFLE

### 6.1 Kegagalan Desain Pola Lama (Predictable Grouping Bug)
Pada rilis awal platform, ditemukan kelemahan fatal: seluruh soal bertipe `complex_table` (Tabel Benar/Salah) selalu terkumpul di nomor-nomor akhir ujian (misalnya nomor 26 s/d 35). Kelemahan ini membuat simulasi menjadi mudah ditebak, merusak alur konsentrasi kognitif peserta, dan menyimpang dari format asli UTBK/Pusmendik di mana soal pilihan ganda kompleks disebarkan secara organik di antara soal-soal pilihan ganda biasa.

### 6.2 Aturan Sebar Acak Terstruktur (Stratified Interleaving Protocol)
Saat menyusun atau mengenerate 135 butir soal per mata pelajaran:
1. Soal `complex_table` wajib disebar dengan frekuensi berkala yang tidak monoton (misalnya berada di nomor 4, 9, 15, 21, 28, 33 pada paket simulasi 35 butir).
2. Tiga level kesulitan (Mudah, Sedang, Sulit) pada paket Latihan Mandiri harus terdistribusi secara independen di bank soal, tetapi saat diakses dalam mode Simulasi Campur, urutan soal harus mengombinasikan tingkat kesulitan secara dinamis (tidak monoton dari mudah ke sulit).
3. Distribusi kunci jawaban pilihan ganda (A, B, C, D, E) pada 135 soal wajib memiliki proporsi seimbang (~20% per huruf $\pm 3\%$) untuk mencegah bias tebakan pada satu opsi tertentu.

---

## BAGIAN VII: REFACTOR UI/UX FOOTER WORKSPACE & AKSESIBILITAS

### 7.1 Kelemahan Layout Footer Lama pada Tablet & Desktop
Di layar tablet (iPad Pro, iPad Air, Galaxy Tab) dan layar monitor desktop, tombol `#btnPaperPrev` (Sebelumnya) dan `#btnPaperFlag` (Ragu-Ragu) sebelumnya bertumpuk atau terlalu rapat di sudut kiri bawah, sementara tombol `#btnPaperNext` (Selanjutnya) berada sangat jauh di sudut kanan bawah. Hal ini menyebabkan:
- Visual imbalance yang buruk karena ruang tengah kosong melompong.
- Ergonomi tablet terganggu karena jempol kanan dan kiri pengguna tidak memiliki pembagian kontrol navigasi yang seimbang.
- Risiko misclick tinggi antara tombol "Sebelumnya" dan tombol "Ragu-Ragu" saat menggunakan layar sentuh tablet.

### 7.2 Solusi Desain: 3-Zone Symmetrical Navigation Grid
Anda diinstruksikan untuk memastikan CSS pada `.paper-footer` mengadopsi arsitektur 3-Zona Simetris:
```css
/* WORKSPACE NAVIGATION FOOTER (STRICT 3-ZONE ERGONOMIC GRID) */
.paper-footer {
  display: grid !important;
  grid-template-columns: auto 1fr auto !important;
  align-items: center !important;
  gap: 16px !important;
  width: 100% !important;
  border-top: 2px solid #1f293d !important;
  padding: 24px 0 max(16px, env(safe-area-inset-bottom)) 0 !important;
  margin-top: 32px !important;
}

/* Zone 1: Left Nav (Sebelumnya) */
#btnPaperPrev {
  justify-self: start !important;
  min-height: 48px !important;
  min-width: 130px !important;
  padding: 12px 20px !important;
}

/* Zone 2: Center Utility (Ragu-Ragu) */
#btnPaperFlag {
  justify-self: center !important;
  min-height: 48px !important;
  min-width: 140px !important;
  padding: 12px 22px !important;
  border-radius: var(--radius-md) !important;
  font-family: var(--font-mono) !important;
  font-weight: 800 !important;
}

/* Zone 3: Right Action (Selanjutnya / Kumpulkan) */
.paper-footer-right {
  justify-self: end !important;
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
}

.paper-footer-right button {
  min-height: 48px !important;
  min-width: 130px !important;
  padding: 12px 22px !important;
}

/* Mobile Responsiveness Override (<= 640px) */
@media (max-width: 640px) {
  .paper-footer {
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: space-between !important;
    gap: 10px !important;
  }
  #btnPaperFlag {
    order: 3 !important;
    width: 100% !important;
    margin-top: 6px !important;
  }
  #btnPaperPrev {
    order: 1 !important;
    flex: 1 !important;
  }
  .paper-footer-right {
    order: 2 !important;
    flex: 1 !important;
  }
}
```

---

## BAGIAN VIII: PROTOKOL EKSEKUSI PRODUKSI BERTAHAP (WAVE RELEASES)

Untuk menjamin kualitas dan stabilitas token tanpa terjadi kegagalan muat atau data terpotong, seluruh 19 mata pelajaran pilihan dikerjakan dalam 4 Gelombang Rilis Terukur:

### Gelombang 1: Saintek & Teknologi Inti (Target: 540 Soal)
- [ ] **Fisika:** 135 Soal (`data/questions_fisika.js`, prefix `fis_001` s/d `fis_135`).
- [ ] **Kimia:** 135 Soal (`data/questions_kimia.js`, prefix `kim_001` s/d `kim_135`).
- [ ] **Biologi:** 135 Soal (`data/questions_biologi.js`, prefix `bio_001` s/d `bio_135`).
- [ ] **Informatika:** 135 Soal (`data/questions_informatika.js`, prefix `inf_001` s/d `inf_135`).

### Gelombang 2: Soshum & Humaniora Inti (Target: 540 Soal)
- [ ] **Ekonomi:** 135 Soal (`data/questions_ekonomi.js`, prefix `eko_001` s/d `eko_135`).
- [ ] **Geografi:** 135 Soal (`data/questions_geografi.js`, prefix `geo_001` s/d `geo_135`).
- [ ] **Sosiologi:** 135 Soal (`data/questions_sosiologi.js`, prefix `sos_001` s/d `sos_135`).
- [ ] **Sejarah Tingkat Lanjut:** 135 Soal (`data/questions_sejarah_lanjut.js`, prefix `sejl_001` s/d `sejl_135`).

### Gelombang 3: Rekayasa Terapan & Budaya (Target: 540 Soal)
- [ ] **Teknik Rekayasa Perangkat Lunak (RPL):** 135 Soal (`data/questions_rpl.js`, prefix `rpl_001` s/d `rpl_135`).
- [ ] **Teknik Komputer & Jaringan (TKJ):** 135 Soal (`data/questions_tkj.js`, prefix `tkj_001` s/d `tkj_135`).
- [ ] **Antropologi:** 135 Soal (`data/questions_antropologi.js`, prefix `ant_001` s/d `ant_135`).
- [ ] **Teknik Rekayasa & Desain:** 135 Soal (`data/questions_rekayasa_desain.js`, prefix `tekd_001` s/d `tekd_135`).

### Gelombang 4: Bahasa Asing Pilihan (Target: 810 Soal)
- [ ] **Bahasa Arab:** 135 Soal (`data/questions_arab.js`, prefix `arb_001` s/d `arb_135`).
- [ ] **Bahasa Jepang:** 135 Soal (`data/questions_jepang.js`, prefix `jpn_001` s/d `jpn_135`).
- [ ] **Bahasa Mandarin:** 135 Soal (`data/questions_mandarin.js`, prefix `man_001` s/d `man_135`).
- [ ] **Bahasa Jerman:** 135 Soal (`data/questions_jerman.js`, prefix `ger_001` s/d `ger_135`).
- [ ] **Bahasa Prancis:** 135 Soal (`data/questions_prancis.js`, prefix `fra_001` s/d `fra_135`).
- [ ] **Bahasa Korea:** 135 Soal (`data/questions_korea.js`, prefix `kor_001` s/d `kor_135`).

---

## BAGIAN X: RUBRIK PENILAIAN, DIAGNOSTIK PRESKRIPTIF, DAN ANALISIS DEFISIT

### 10.1 Arsitektur Diagnostik Preskriptif (Bukan Sekadar Persentase Skor)
Salah satu kelemahan terbesar sistem CBT konvensional adalah hanya menampilkan skor akhir berupa persentase angka (misalnya "Skor Anda: 68%"). TKA Mastery Hub menuntut mesin asesmen diagnostik preskriptif yang mampu membedah kelemahan kognitif siswa secara spesifik dan objektif.

Setiap mata pelajaran yang Anda susun wajib memiliki parameter diagnostik yang dapat diolah oleh mesin analisis `#viewResults`:
1. **Diagnosis Defisit Berbasis Sub-Topik (Deficit Gap Matrix):**
   - Siswa yang gagal pada butir soal tertentu harus langsung dipetakan ke materi spesifik yang belum dikuasai.
   - Contoh output diagnostik yang diinginkan: *"Siswa menunjukkan penguasaan tinggi pada Termodinamika Dasar (Akurasi 90%), namun mengalami defisit parah pada Dinamika Rotasi & Momen Inersia di tingkat kognitif C4 (Akurasi 25%, rerata durasi pengerjaan 3 menit 12 detik). Rekomendasi: Perkuat analisis diagram benda bebas pada benda tegar."*
2. **Karakteristik Tiga Domain Kompetensi Radar Chart:**
   - **Pemahaman Konseptual (Conceptual Understanding):** Menguji kemampuan siswa mendefinisikan batas fisis, menjelaskan prinsip hukum alam/sosial, dan membaca tren data dasar.
   - **Kecakapan Prosedural (Procedural Fluency):** Menguji ketepatan langkah komputasi matematis, substitusi variabel, dan kecepatan penarikan formula baku.
   - **Penalaran Pemecahan Masalah (Problem Solving & HOTS):** Menguji kemampuan mentransfer konsep ke skenario baru yang belum pernah ditemui sebelumnya, mengevaluasi data yang bertentangan, dan memvalidasi kebenaran hipotesis.

### 10.2 Formula Pembobotan dan Penalti Waktu (Adaptive Timing Metric)
Dalam mode Simulasi Realistis, alokasi waktu ideal adalah $\approx 51{,}4$ detik per butir soal (35 butir soal dalam 30 menit). Algoritma evaluasi hasil akan menilai efisiensi pengerjaan:
- Waktu pengerjaan $< 20$ detik dengan jawaban salah: Terindikasi tebakan acak (*blind guessing*).
- Waktu pengerjaan $> 120$ detik: Terindikasi kesulitan metodologis (*procedural bottleneck*).
- Setiap butir soal dalam bank data harus dirancang secara realistis agar dapat dipecahkan oleh siswa terlatih dalam rentang waktu 45 hingga 75 detik jika konsep dasarnya telah dipahami.

---

## BAGIAN XI: KAMUS ERROR DAN QUALITY ASSURANCE GATE (20 CHECKLIST WAJIB)

Sebelum menyerahkan berkas JavaScript bank soal apa pun kepada pengguna, Anda WAJIB memverifikasi bahwa data telah lulus 20 kriteria pengujian berikut tanpa ada satu pun pelanggaran:

### Kelompok Validasi Data & Sintaksis (Checklist 1–7)
1. **[ ] Zero Syntax Error:** File lolos uji validasi parser JavaScript tanpa ada syntax error, bracket yang tidak tertutup, atau koma hilang.
2. **[ ] Double Backslash Integrity:** Tidak ada satupun formula matematika yang menggunakan single backslash (`\\frac`, bukan `\frac`).
3. **[ ] Delimiter Enclosure:** Seluruh rumus matematika inline terbungkus `$ ... $` dan rumus display terbungkus `$$ ... $$`.
4. **[ ] Unique ID Assertion:** Setiap butir soal dari nomor 1 hingga 135 memiliki ID unik dengan format prefix standar tanpa ada ID kembar.
5. **[ ] Correct Answer Mapping:** Properti `correctAnswer` untuk tipe `single_choice` hanya bernilai salah satu dari `"A"`, `"B"`, `"C"`, `"D"`, atau `"E"`.
6. **[ ] Complex Table Alignment:** Properti `correctAnswer` untuk tipe `complex_table` berupa objek dengan key indeks string `{"0": "B", "1": "S", ...}` yang panjangnya sama persis dengan jumlah elemen pada array `tableStatements`.
7. **[ ] Two-Tier Clues:** Setiap butir soal memiliki tepat 2 elemen string di dalam array `clues`: Clue 1 berupa konsep kunci dan Clue 2 berupa panduan eksekusi awal.

### Kelompok Kualitas Pedagogis & Anti-Slop (Checklist 8–14)
8. **[ ] Realistic Word Count:** Panjang wacana stimulus berada di rentang 120 hingga 180 kata, padat fakta/data, dan tidak bertele-tele.
9. **[ ] No Repetitive Numbers:** Tidak ada butir soal yang sekadar mengganti variabel angka dari soal sebelumnya dalam satu paket mapel yang sama.
10. **[ ] Interleaved Complex Distribution:** Soal tipe `complex_table` tersebar secara acak proporsional di seluruh nomor ujian, bukan menumpuk di 5 nomor terakhir.
11. **[ ] Option Length Uniformity:** Panjang teks opsi jawaban (A, B, C, D, E) relatif homogen untuk menghindari bias di mana jawaban terpanjang selalu menjadi kunci jawaban.
12. **[ ] Plausible Distractors:** Opsi pengecoh (distractor) dirancang berbasis miskonsepsi umum siswa (misalnya salah tanda plus/minus, lupa mengonversi satuan ke SI, atau salah membedakan jari-jari dengan diameter).
13. **[ ] Cognitive Depth:** Soal level Sulit (Hard) benar-benar menuntut penalaran C4-C6 (analisis, evaluasi, sintesis), bukan sekadar perhitungan aritmatika panjang yang membosankan.
14. **[ ] Authentic Context:** Stimulus mengangkat isu relevan: transisi energi terbarukan, rekayasa kecerdasan buatan, stabilitas pangan, mitigasi bencana gempa bumi, atau dinamika masyarakat digital.

### Kelompok Kompatibilitas UI/UX & Browser (Checklist 15–20)
15. **[ ] Indonesian Decimal Format:** Angka desimal ditulis dengan format Indonesia menggunakan koma di dalam KaTeX (`0{,}5` atau `$3{,}14$`).
16. **[ ] Safe String Escaping:** Karakter kutip dua (`"`) di dalam string soal di-escape dengan benar (`\"`) agar tidak memutus literal string JavaScript.
17. **[ ] Step-by-Step Solution:** Properti `solution` memuat pembahasan terurut nomor (1, 2, 3...) yang menjelaskan logika eliminasi jawaban salah dan pembuktian jawaban benar.
18. **[ ] Mobile & Tablet Legibility:** Format tabel stimulus dirancang ringkas (maksimal 3–4 kolom) agar tidak terpotong (overflow horizontal) di layar tablet maupun smartphone.
19. **[ ] Non-Biased Key Proportion:** Distribusi kunci jawaban A, B, C, D, dan E seimbang (masing-masing sekitar 18%–22% dari total 135 soal).
20. **[ ] Standalone Script Loading:** File JavaScript dapat di-load secara mandiri melalui tag `<script src="...">` tanpa menimbulkan dependensi silang yang merusak urutan inisialisasi aplikasi.

---

## BAGIAN XII: INSTRUKSI EKSEKUSI PERDANA (INITIAL KICKOFF ACTION)

Ketika Anda menerima prompt ini dari pengguna bersama nama mata pelajaran target (misalnya: **Fisika**, **Kimia**, **Biologi**, atau **Informatika**):
1. **Langkah 1 (Implementation Plan):**
   Sajikan tabel rencana produksi 135 butir soal yang memuat:
   - Distribusi Bab / Sub-materi Kurikulum Merdeka Fase F.
   - Alokasi jumlah butir soal per tingkat kognitif (Mudah: 30, Sedang: 30, Sulit: 30, Simulasi: 45).
   - Sebaran nomor soal untuk tipe `single_choice` dan `complex_table`.
2. **Langkah 2 (Eksekusi Kode Tanpa Basa-Basi):**
   Langsung hasilkan blok kode produksi JavaScript lengkap yang mendefinisikan array data soal sesuai skema Bagian V.
3. **Langkah 3 (Panduan Registrasi):**
   Sertakan baris kode ringkas pendaftaran mapel baru ke dalam `window.TKA_DATABASE` di `data/questions_db.js` dan tag `<script>` cache-busted untuk `index.html`.

Dilarang menunda eksekusi dengan meminta konfirmasi berulang. Ambil keputusan teknis terbaik secara mandiri, pertahankan standar HOTS tertinggi, dan serahkan hasil kerja kelas dunia.

---
*DOKUMEN SPESIFIKASI INI BERLAKU SEBAGAI PEDOMAN RESMI PENGEMBANGAN KURIKULUM DAN ENGINE TKA MASTERY HUB.*
"""
    return prompt_text

def main():
    docs_dir = os.path.join(os.getcwd(), 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    
    prompt_content = generate_master_prompt()
    md_path = os.path.join(docs_dir, 'MASTER_PROMPT_CLAUDE_EXPANSION.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(prompt_content)
    
    words = prompt_content.split()
    word_count = len(words)
    print(f"[OK] Master prompt written to: {md_path}")
    print(f"[INFO] Total word count: {word_count} words")
    
    # Generate HTML printable version for PDF conversion
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Master Architectural Prompt - TKA Mastery Hub</title>
<style>
  @page {{
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
  }}
  body {{
    font-family: 'Segoe UI', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.5;
    font-size: 11pt;
    padding: 0;
    margin: 0;
  }}
  h1 {{
    color: #0f172a;
    font-size: 18pt;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 6px;
    margin-top: 0;
  }}
  h2 {{
    color: #1e3a8a;
    font-size: 13pt;
    margin-top: 18px;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 4px;
    page-break-after: avoid;
  }}
  h3 {{
    color: #1d4ed8;
    font-size: 11pt;
    margin-top: 12px;
    page-break-after: avoid;
  }}
  p, li {{
    font-size: 10pt;
    color: #334155;
  }}
  pre, code {{
    font-family: 'Consolas', 'Courier New', monospace;
    background: #f1f5f9;
    font-size: 8.5pt;
    border-radius: 4px;
  }}
  pre {{
    padding: 10px;
    border: 1px solid #cbd5e1;
    white-space: pre-wrap;
    word-break: break-word;
    page-break-inside: avoid;
  }}
  code {{
    padding: 2px 4px;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 9pt;
    page-break-inside: avoid;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 6px 10px;
    text-align: left;
  }}
  th {{
    background: #e2e8f0;
    color: #0f172a;
    font-weight: 700;
  }}
  .badge {{
    display: inline-block;
    padding: 2px 8px;
    font-size: 8pt;
    font-weight: bold;
    border-radius: 9999px;
    background: #dbeafe;
    color: #1e40af;
  }}
</style>
</head>
<body>
  <div style="text-align: right; margin-bottom: 15px;">
    <span class="badge">SPECIFICATION ARTIFACT — PUSMENDIK FASE F</span>
  </div>
  <pre style="background: transparent; border: none; font-family: inherit; font-size: 10pt; white-space: pre-wrap;">{prompt_content}</pre>
</body>
</html>
"""
    html_path = os.path.join(docs_dir, 'master_prompt_printable.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"[OK] Printable HTML written to: {html_path}")
    
    # Generate PDF using Microsoft Edge headless
    pdf_path = os.path.join(docs_dir, 'MASTER_PROMPT_CLAUDE_EXPANSION.pdf')
    edge_cmd = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    try:
        subprocess.run(edge_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if os.path.exists(pdf_path):
            print(f"[SUCCESS] PDF successfully created: {pdf_path} (Size: {os.path.getsize(pdf_path)} bytes)")
        else:
            print("[WARN] PDF not found after command execution.")
    except Exception as e:
        print(f"[ERROR] PDF generation failed: {e}")

if __name__ == '__main__':
    generate_master_prompt()
    main()
