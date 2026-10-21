# Rencana Implementasi: Ekspansi 3 Mata Pelajaran Tingkat Lanjut (405 Butir Soal Autentik Pusmendik)

**Goal:** Mengintegrasikan 3 mata pelajaran lanjutan (**Matematika Lanjutan**, **Bahasa Indonesia Lanjutan**, dan **Bahasa Inggris Lanjutan**) ke dalam TKA Mastery Hub dengan total **405 butir soal baru** (masing-masing 135 butir: 35 Mudah, 35 Sedang, 35 Sulit, 30 Simulasi HOTS) sesuai silabus resmi Pusmendik / BSKAP Kemendikbudristek, tanpa duplikasi, lengkap dengan KaTeX, Formula HUD, Hint bertingkat, dan integrasi UI responsif.

**Arsitektur & Pendekatan:**
1. **Modular Question Repositories**: Setiap mapel lanjutan memiliki berkas data independen (`data/questions_mtk_lanjut.js`, `data/questions_ind_lanjut.js`, `data/questions_eng_lanjut.js`) untuk menjaga performa loading dan isolasi dependensi.
2. **Aggregator Registration**: `data/questions_db.js` mendaftarkan ketiga mapel ini ke dalam `window.TKA_DATABASE` lengkap dengan SVG icon, badge spesialisasi, dan metadata silabus.
3. **Pusmendik Syllabus Compliance**: Menjamin kedalaman materi tingkat lanjut (Fase F SMA):
   - *Matematika Lanjutan*: Polinomial (Horner, Sisa, Vieta), Matriks & Determinan 2x2/3x3, Irisan Kerucut (Parabola, Elips, Hiperbola), Trigonometri Lanjut (Sudut Ganda, Identitas, Persamaan Cosinus/Sinus), Vektor Ruang, dan Kalkulus Lanjut (Limit Trigonometri, Turunan Rantai, Optimasi, Luas Integral).
   - *Bahasa Indonesia Lanjutan*: Teks Akademik/Karya Ilmiah (Abstrak, Sitasi APA, Sintesis Pustaka), Logika & Penalaran Kritis (Silogisme, Entimem, *Fallacies*: Ad Hominem, Straw Man, Slippery Slope, False Dilemma), Resensi & Evaluasi Kebijakan Publik (Tone, Bias, EYD V, Kohesi-Koherensi), Kritik Sastra Lanjutan (Stilistika, Semiotika, Konflik Batin).
   - *Bahasa Inggris Lanjutan (CEFR B2–C1)*: Academic Discourse & Argumentation, Authorial Stance & Nuanced Tone (Skeptical, Ambivalent, Laudatory), Hedging & Modality, Advanced Discourse Markers (*notwithstanding, albeit, conversely, hitherto*), Inversion & Subjunctive Conditionals, Cross-Text Argumentative Synthesis.
4. **UI/UX Hub Integration**: Penambahan tabs / selector mapel lanjutan di Navbar dan Home Panorama Deck dengan warna aksen unik (Cyan untuk MTK Lanjut, Emerald Neon untuk IND Lanjut, Purple Rose untuk ENG Lanjut) tanpa mengganggu tata letak responsif yang sudah diperbaiki.

---

## Breakdown Tugas (Task Breakdown)

### Fase 1: Generator & Bank Soal Autentik (3 x 135 = 405 Soal)
- [ ] **Task 1.1: Bangun Generator Script Berstandar Pusmendik** (`scripts/generate_advanced_subjects.py`)
  - Distribusi per mapel: 35 Easy (`-lat-e-01` s.d. `35`), 35 Medium (`-lat-m-01` s.d. `35`), 35 Hard (`-lat-h-01` s.d. `35`), 30 Simulation HOTS (`-sim-01` s.d. `30`).
  - Total ID: 135 ID unik per mata pelajaran.
  - Skema data ketat: `id`, `subject`, `materi`, `mode`, `difficulty`, `topic`, `type`, `questionHtml` (KaTeX LaTeX delimiters `$...$`), `options` (5 butir: A-E), `correctKey`, `formulaHud` (`title`, `latex`, `legend`), `hints` (`concept`, `execution`), `explanation`, `isDiagnostic: false`.
- [ ] **Task 1.2: Eksekusi & Validasi Berkas Data**
  - Generate `data/questions_mtk_lanjut.js` (`window.TKA_MTK_LANJUT_QUESTIONS`)
  - Generate `data/questions_ind_lanjut.js` (`window.TKA_IND_LANJUT_QUESTIONS`)
  - Generate `data/questions_eng_lanjut.js` (`window.TKA_ENG_LANJUT_QUESTIONS`)
  - Script validasi otomatis: cek 0 duplicate ID, verifikasi 135 soal per file, cek validitas `correctKey` terhadap list options, verifikasi format KaTeX.

### Fase 2: Database Registry & Loader Integration
- [ ] **Task 2.1: Daftarkan ke `data/questions_db.js`**
  - Inisialisasi pool data baru dari `window.TKA_MTK_LANJUT_QUESTIONS`, `TKA_IND_LANJUT_QUESTIONS`, `TKA_ENG_LANJUT_QUESTIONS`.
  - Daftarkan `mtk_lanjut` (Aksen: Cyan `#06b6d4`, Badge: "Kalkulus & Geometri Analitik").
  - Daftarkan `ind_lanjut` (Aksen: Teal `#14b8a6`, Badge: "Logika Formal & Wacana Kritis").
  - Daftarkan `eng_lanjut` (Aksen: Violet `#a855f7`, Badge: "Advanced Academic CEFR B2-C1").
  - Update status di `TKA_ELECTIVE_CATALOG` agar mapel yang sudah tersedia berstatus aktif.
- [ ] **Task 2.2: Hubungkan Script Tag di `index.html`**
  - Sertakan ketiga file baru sebelum `data/questions_db.js`.
  - Bump cache query version ke `style.css?v=11.0` dan `app.js?v=11.0`.

### Fase 3: Engine Logic & Navigation Routing (`app.js`)
- [ ] **Task 3.1: Konfigurasi State Mapel di `app.js`**
  - Perluas validasi `currentSubject` agar mengenali `'mtk_lanjut'`, `'ind_lanjut'`, `'eng_lanjut'`.
  - Pasang handler seleksi mapel di Training Lab & Exam Arena untuk memuat pool 135 soal yang sesuai.
- [ ] **Task 3.2: Navbar & Subject Filter Extension**
  - Tambahkan pill/tab switcher atau dropdown kelompok mapel ("Mapel Utama" vs "Mapel Lanjutan") pada navigasi atas agar Navbar tetap bersih dan tidak sesak di layar mobile.
  - Perbarui generator Panorama Deck di Home untuk merender kartu interaktif mapel lanjutan.

### Fase 4: Desain & Token Visual (`style.css`)
- [ ] **Task 4.1: Token Warna & Style Khas Mapel Lanjutan**
  - Tambahkan kelas gradien kartu: `.card-mtk_lanjut`, `.card-ind_lanjut`, `.card-eng_lanjut`.
  - Aksen glow dan border color neon yang harmonis dengan Dark Theme Slate yang ada.
- [ ] **Task 4.2: Audit Responsivitas & Overflow Check**
  - Verifikasi tidak ada teks atau tombol yang bertabrakan di viewport sempit (360px - 500px).

### Fase 5: QA & Pengujian Regresi
- [ ] **Task 5.1: Sintaksis & Bundle Integrity**
  - Jalankan `node -c app.js`, `node -c data/questions_db.js`, serta berkas soal baru.
- [ ] **Task 5.2: Uji Validasi Pool & Shuffle**
  - Pastikan pengerjaan soal mode Latihan (Mudah, Sedang, Sulit) dan Simulasi (30 HOTS) dapat berjalan lancar dengan timer, navigasi nomor, penanda ragu-ragu, dan evaluasi hasil.
- [ ] **Task 5.3: Update Dokumentasi & Sinkronisasi `MEMORY.md`**
  - Catat penambahan struktur data dan arsitektur v11.0 di `MEMORY.md`.
