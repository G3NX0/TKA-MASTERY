# TKA Mastery Hub — Project Context & Engineering Handover Memory

> **Dokumen ini adalah single source of truth (SSOT) teknis untuk agen AI / engineer berikutnya.**
> Baca dokumen ini terlebih dahulu sebelum mengeksekusi instruksi baru agar context tersambung 100% instan tanpa latency.

---

## 1. Identitas & Lokasi Proyek
* **Nama Proyek:** TKA Mastery Hub — Elite Academic Workstation
* **Path Repositori:** `C:\Users\glixer\.gemini\antigravity-ide\scratch\tka-mastery-hub`
* **Local Dev Server:** `python -m http.server 3000` (Akses browser: `http://localhost:3000/index.html`)
* **Arsitektur:** Pure Native Frontend (Vanilla HTML5 + Vanilla CSS3 + Modern ES6+ JavaScript), KaTeX untuk mathematical formula rendering, zero heavy framework bloat.

---

## 2. Struktur File & Database Soal (V12.0)
```text
tka-mastery-hub/
├── index.html                     # Shell utama aplikasi SPA (Multi-View Stage, Cache v=12.0)
├── style.css                      # Design system (Neo-Brutalism + Cyber Glassmorphism, 4.900+ baris)
├── app.js                         # State manager, universal Pusmendik adapter, KaTeX renderer
├── MEMORY.md                      # Handover memory ini
└── data/
    # Mapel Wajib (3 Mapel = 405 Soal)
    ├── questions_mtk.js               # 135 Soal Matematika (Pusmendik)
    ├── questions_ind.js               # 135 Soal Bahasa Indonesia (Pusmendik)
    ├── questions_eng.js               # 135 Soal Bahasa Inggris (Pusmendik)
    # Mapel Tingkat Lanjut SMA (3 Mapel = 405 Soal)
    ├── questions_mtk_lanjut.js        # 135 Soal Matematika Tingkat Lanjut (Pusmendik)
    ├── questions_ind_lanjut.js        # 135 Soal Bahasa Indonesia Tingkat Lanjut (Pusmendik)
    ├── questions_eng_lanjut.js        # 135 Soal Bahasa Inggris Tingkat Lanjut (Pusmendik)
    # Kluster 1: Saintek Inti (3 Mapel = 405 Soal)
    ├── questions_fisika.js            # 135 Soal Fisika (Pusmendik MIPA)
    ├── questions_kimia.js             # 135 Soal Kimia (Pusmendik MIPA)
    ├── questions_biologi.js           # 135 Soal Biologi (Pusmendik MIPA)
    # Kluster 2: Soshum Inti (4 Mapel = 540 Soal)
    ├── questions_ekonomi.js           # 135 Soal Ekonomi (Pusmendik IPS)
    ├── questions_geografi.js          # 135 Soal Geografi (Pusmendik IPS)
    ├── questions_sosiologi.js         # 135 Soal Sosiologi (Pusmendik IPS)
    ├── questions_sejarah_lanjut.js    # 135 Soal Sejarah Tingkat Lanjut (Pusmendik IPS)
    # Kluster 3: Teknologi & Vokasi (5 Mapel = 675 Soal)
    ├── questions_informatika.js       # 135 Soal Informatika (Pusmendik SMA)
    ├── questions_pkk.js               # 135 Soal Produk Kreatif dan Kewirausahaan (Pilihan Wajib SMK)
    ├── questions_rpl.js               # 135 Soal Pengembangan Perangkat Lunak dan Gim (SMK/MAK)
    ├── questions_tkj.js               # 135 Soal Teknik Jaringan Komputer dan Telekomunikasi (SMK/MAK)
    ├── questions_rekayasa_desain.js   # 135 Soal Desain Komunikasi Visual (SMK/MAK)
    # Kluster 4: Bahasa Asing & Budaya (7 Mapel = 945 Soal)
    ├── questions_bahasa_arab.js       # 135 Soal Bahasa Arab (Pusmendik)
    ├── questions_bahasa_jepang.js     # 135 Soal Bahasa Jepang (Pusmendik)
    ├── questions_bahasa_mandarin.js   # 135 Soal Bahasa Mandarin (Pusmendik)
    ├── questions_bahasa_jerman.js     # 135 Soal Bahasa Jerman (Pusmendik)
    ├── questions_bahasa_prancis.js    # 135 Soal Bahasa Prancis (Pusmendik)
    ├── questions_bahasa_korea.js      # 135 Soal Bahasa Korea (Pusmendik)
    ├── questions_antropologi.js       # 135 Soal Antropologi (Pusmendik)
    └── questions_db.js                # Master DB Aggregator & Elective Catalog Registry (25 Mapel)
```
* **Status Bank Soal (Terverifikasi Forensik):** **2.825 Soal Autentik Aktif (3 Mapel Wajib @ 135 Soal + 22 Mapel Pilihan/Lanjut @ 110 Soal)**. 
* **Distribusi Format Standar Pusmendik:**
  - Pilihan Ganda Tunggal (`mcq`): 2.566 soal
  - Pilihan Ganda Kompleks / Multi-jawaban (`multi`): 124 soal (100% valid >1 jawaban benar)
  - Tabel Pernyataan Benar/Salah (`matrix`): 135 soal (100% tervalidasi kunci per butir pernyataan)
* **Subject Capability Suite (Bespoke per Mapel):**
  - Bahasa Jepang: Furigana Toggle (ON/OFF)
  - Bahasa Mandarin: Pinyin Toggle (ON/OFF)
  - Bahasa Arab: Harakat Toggle (ON/OFF) + RTL layout support
  - Kimia: Modal Interaktif Tabel Periodik Unsur (IUPAC) dengan pencarian langsung
  - Fisika: Modal Referensi Konstanta Baku Fisika Saintek
  - TKJ & Informatika: Modal Kalkulator Subnetting CIDR (IPv4 VLSM)
  - PKK & Ekonomi: Modal Kalkulator Break-Even Point (BEP & Margin Kontribusi)
  - RPL & Informatika: Modal Scratchpad Interactive Trace Table (Algoritma/Dry-Run)
* **100% Nomenklatur Pusmendik Kemendikdasmen & BSKAP 033/H/KR/2022:**
  - Matematika (Wajib) $\rightarrow$ **Matematika**
  - Sejarah (Tingkat Lanjut) $\rightarrow$ **Sejarah Tingkat Lanjut**
  - RPL $\rightarrow$ **Pengembangan Perangkat Lunak dan Gim (SMK/MAK)**
  - TKJ $\rightarrow$ **Teknik Jaringan Komputer dan Telekomunikasi (SMK/MAK)**
  - Rekayasa Desain $\rightarrow$ **Desain Komunikasi Visual (SMK/MAK)**
  - PKK $\rightarrow$ **Produk Kreatif dan Kewirausahaan (SMK/MAK)**
* **Zero AI Slop & Zero Duplicates:** 0 duplikasi teks global lintas file, 0 duplicate IDs, sebaran kunci jawaban 20 A-E seimbang, dan 0 string padding kurung buatan.

---

## 3. Arsitektur View & Alur Pengguna (SPA Router)
Semua tampilan dikendalikan di [app.js](file:///C:/Users/glixer/.gemini/antigravity-ide/scratch/tka-mastery-hub/app.js) dengan class `.stage-view.active`:
1. **`#viewHome` (Beranda):**
   - **3D Curved Panorama Deck:** 3 Card mapel utama (`ind`, `mtk`, `eng`) dengan orientasi silinder 3D (`is-active-center`, `is-peek-left`, `is-peek-right`) yang sinkron saat digeser (swipe/touch) atau diklik.
   - **Bespoke Cyber-Cockpit Orbit Switcher (`#mobilePanoramaNav`):** Pil navigasi unik di bawah deck dengan segmented dock kapsul recessed, micro-badge icon SVG, dan live pulsing spark per subjek.
   - **Banner Tes Diagnostik Cepat:** Akses instan ke 15 soal gabungan.
   - **Katalog 19 Mapel Pilihan:** Accordion drawer pemetaan kompetensi Kurikulum Merdeka & SNBT.
2. **`#viewSubject` (Halaman Subjek):**
   - Dua launchpad: **Training Lab (Latihan)** dengan pemilih level (Mudah/Sedang/Sulit) dan **Exam Arena (Simulasi Ujian Realistis)** dengan timer 30 menit.
3. **`#viewExam` (Workstation Ujian & Latihan):**
   - Split paper layout, floating sticky timer HUD, KaTeX math typesetting, interactive option badges.
   - Latihan mode: Tersedia drawer Clue, Rumus HUD, dan Solusi Bertahap.
   - Simulasi mode: Wajib fullscreen (F11), no-clue, dan **Strict 3-Strike Proctoring** (blur/focus switch detection modal warning).
4. **`#viewResults` (Analisis Pasca-Ujian):**
   - Score breakdown, akurasi per topik, radar analysis, log pelanggaran proctoring, dan mode review kunci jawaban.

---

## 4. Design System & UI/UX Standards
* **Palette Tokens:**
  - Obsidian Dark Canvas: `--bg-primary: #07090e`, `--bg-surface: #0f1420`, `--bg-elevated: #161e30`.
  - Matematika: Electric Cobalt (`#2563eb`), Cyan glow (`#60a5fa`).
  - Bahasa Indonesia: Vivid Emerald (`#059669`), Mint glow (`#34d399`).
  - Bahasa Inggris: Radiant Warm Amber (`#d97706`), Gold glow (`#fbbf24`).
  - Warning / Proctor: Crimson (`#f43f5e`).
* **Navbar Mobile (Pinterest Floating Dock):**
  - Pada layar HP (`<= 768px`), navbar otomatis melayang di bawah: `position: fixed; bottom: max(20px, env(safe-area-inset-bottom)); left: 50%; max-width: 460px; border-radius: 26px; padding: 7px 10px; background: rgba(13, 18, 30, 0.95);`.
  - Logo lingkaran merah disembunyikan di mobile (`.pill-badge { display: none !important; }`) agar 5 tab (`Home`, `MTK`, `IND`, `ENG`, `Diag`) memiliki ruang ergonomis seimbang dengan target sentuh `min-height: 48px` (WCAG / Apple HIG compliant).
  - Indikator aktif berupa micro-capsule bar glowing 16px x 3px dengan warna tematik subjek.
* **Subject Card Deck Architecture (V10.0 Anti-Compact Refactor):**
  - Mobile Card Width: Ditingkatkan dari `clamp(240px, 66vw, 260px)` yang mencekik konten menjadi `clamp(310px, 84vw, 380px)`. Memberikan ruang horizontal lega (+100px) sehingga badge judul panjang tidak bertubrukan dengan glyph.
  - Internal Breathing Room: Padding internal ditingkatkan menjadi `28px 24px` di mobile dan `34px 28px` di desktop. Min-height `420px` (mobile) / `440px` (desktop).
  - Header & Glyph: Badge pill rounded (`border-radius: 999px; font-weight: 750;`) dengan glyph icon di dalam glass frame berdimensi `38px x 38px`.
  - Stats Spec HUD: `card-meta-spec` dilengkapi `.spec-divider` vertikal di antara `BANK SOAL` dan `STANDARISASI` dengan background dark glass `rgba(8, 12, 22, 0.65)`.
  - Primary CTA: Target sentuh ergonomis `min-height: 48px` (mobile) / `52px` (desktop) dengan micro-animation hover panah.
* **Modern Brutalism UI & Antislop Enforcement (V12.1):**
  - **100% Zero Gradients:** Seluruh 44 deklarasi `gradient` (radial ambient glow orbs, linear button/card/tab fades, body background glows) dieliminasi total dari `style.css`.
  - **Arsitektur Flat Solid Brutalist:** Menggunakan warna flat solid berkarakter tegas (`var(--bg-surface, #0f1420)`, `#2563eb`, `#059669`, `#d97706`, `#7e22ce`), garis batas struktural tebal (`border: 2px solid #000000` / `var(--border)`), dan stripe arsitektural solid (`border-top: 5px solid ...`).
  - **Hard Offset Shadows:** Menghapus semua blur glow lembut (`rgba(..., 0.45)`). Mengadopsi hard unblurred shadows murni Neo-Brutalism: `box-shadow: 2px 2px 0px #000000`, `4px 4px 0px #000000`, hingga `8px 8px 0px #000000`.
  - **Pencegahan AI-Slop (antislop-ui compliant):** Tidak ada radial ambient orbs yang melayang di belakang hero/katalog, tidak ada visual pill berlebihan tanpa fungsi, tidak ada soft fuzzy shadows.
* **Cache Busting:** Link stylesheet di `index.html` menggunakan query versioning `v=12.1-brutalism`. Bump versi ini setiap mengubah CSS/JS agar browser pengguna langsung me-refresh tampilan tanpa cached style lama.

---

## 5. Status Rencana Aksi (Implementation Plan Checklist)
* **FASE 1: PERBAIKAN INTEGRITAS DATA BANK SOAL (100% PASS)**
  - [x] **Task 1.1**: Hapus seluruh 38 teks kurung pembocor (*artificial padding*) di `questions_mtk.js` (Selesai, 0 padding).
  - [x] **Task 1.2**: Perbaiki schema `correctKey` pada `questions_mtk_lanjut.js` agar terbaca valid A-E (Selesai, valid).
  - [x] **Task 1.3**: Acak opsi jawaban (*Fisher-Yates*) dan distribusikan kunci merata (~20% per opsi A-E) di `questions_eng_lanjut.js` & `questions_ind_lanjut.js` (Selesai, masing-masing tepat 20 A, 20 B, 20 C, 20 D, 20 E).
  - [x] **Task 1.4**: Perbaiki duplicate ID di `questions_bahasa_mandarin.js` dan `questions_sosiologi.js` (Selesai, 0 dupID).
  - [x] **Task 1.5**: Jalankan `audit_questions.py` untuk memastikan audit 100% PASS (Selesai, 2.825 soal PASS).
* **FASE 2: SUBJECT CAPABILITY REGISTRY DI APP.JS (100% IMPLEMENTED)**
  - [x] **Task 2.1**: Definisikan registry konfigurasi kemampuan mapel (`SUBJECT_CAPABILITIES`) di `app.js` (Furigana, Pinyin, Harakat, Periodic Table, Constants, Subnetting, BEP, Trace Table).
  - [x] **Task 2.2**: Tambahkan logic penyaluran toolbar dinamis pada header workstation (`#paperTopRow` / `#workspaceToolbarTools`).
  - [x] **Task 2.3**: Integrasikan state handler untuk toggle transliterasi & modal popover.
* **FASE 3: DESAIN KOMPONEN UI & RESPONSIVE HARDENING (100% VERIFIED)**
  - [x] **Task 3.1**: Markup HTML modal dan popover di `index.html` (Tabel Periodik Kimia, Subnetting, BEP).
  - [x] **Task 3.2**: Styling Neo-Brutalist di `style.css` untuk tools mapel, modal tabel periodik, dan toggle pills.
  - [x] **Task 3.3**: Zero-Overflow & iOS/iPad Hardening di `style.css` (`overflow-x: hidden`, safe-area insets, target sentuh 44px, breakpoint 1024px & 768px).
  - [x] **Task 3.4**: Validasi sintaks kode (`node -c app.js` passed, exit code 0).
* **TABEL PERIODIK UNSUR IUPAC (AUTHENTIC DESIGN)**
  - 118 unsur kimia lengkap (Hidrogen 1 s.d. Oganeson 118).
  - Grid 18-kolom standar IUPAC dengan baris terpisah untuk deret Lantanida (57-71) & Aktinida (89-103).
  - Interactive Element Inspector Banner di bagian atas (Simbol besar, Nama, Nomor Atom, Massa Relatif, Konfigurasi Elektron, Golongan & Periode, Bilangan Oksidasi, Wujud 298 K).
  - Live search input & filter pill kategori warna (Alkali, Alkali Tanah, Transisi, Metaloid, Nonlogam, Halogen, Gas Mulia, Lantanida, Aktinida).

---

## 6. ATURAN KERJA & DISIPLIN TEKNIS (KRUSIAL UNTUK AI SELANJUTNYA)

1. **DILARANG KERAS MENJALANKAN `browser_subagent`:**
   - **Instruksi Mutlak User:** *"saya ga mau kamu yang ujki coba, itu bikin kinerja kamu lambatr saya saja yang uji coba"*.
   - **JANGAN PERNAH** memanggil tool `browser_subagent`. Uji coba visual dilakukan langsung oleh pengguna.
2. **Kecepatan Eksekusi (Zero Bloat, Direct Action):**
   - Jangan melakukan analisis berputar-putar tanpa aksi.
   - Karena file `style.css` berukuran 150 KB (6.000+ baris), gunakan script Python via `run_command` untuk melacak baris secara instan (<2 detik).
3. **Validasi Sintaks Cepat:**
   - Setelah mengedit JavaScript di `app.js` atau `data/`, selalu jalankan `node -c <filename>` untuk memverifikasi zero syntax regression.
4. **Prinsip Komunikasi (Principal Engineer & Lead UI/UX):**
   - Kritis, pragmatis, anti-yes-man.
   - Langsung ke inti solusi, tolak over-engineering, dan sorot trade-off teknis secara transparan.

---
*Updated: 2026-10-21 — TKA Mastery Hub Engineering Handover*

