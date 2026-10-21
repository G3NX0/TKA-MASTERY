# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Produk Kreatif dan Kewirausahaan (PKK SMK/MAK)
Dataset: Hard Practice (25 Authentic Questions, pkk-lat-h-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

PKK_HARD_ITEMS = [
    {
        "id": "pkk-lat-h-01",
        "materi": "KELAYAKAN INVESTASI USAHA",
        "topic": "Net Present Value (NPV) & Keputusan Kelayakan Modal",
        "stem": "Unit produksi permesinan presisi SMK berencana membeli mesin CNC 5-Axis seharga Rp100.000.000 (Initial Outlay). Mesin ini diproyeksikan menghasilkan arus kas masuk bersih (Net Cash Flow) sebesar Rp40.000.000 per tahun selama 3 tahun berturut-turut. Jika tingkat diskonto (Cost of Capital / WACC) yang ditetapkan sebesar 10% per tahun (faktor diskonto: Tahun 1 = 0,9091; Tahun 2 = 0,8264; Tahun 3 = 0,7513), evaluasi kelayakan finansial investasi tersebut adalah...",
        "correct": "Layak diterima (Feasible), karena menghasilkan nilai Net Present Value (NPV) positif sebesar Rp+6.480.000 (Present Value arus kas masuk Rp106.480.000 dikurangi investasi awal Rp100.000.000).",
        "distractors": [
            "Wajib ditolak keras, karena arus kas masuk tiga tahun hanya menghasilkan Rp120.000.000 yang dipotong inflasi menjadi minus Rp15.000.000.",
            "Layak diterima dengan syarat sekolah meminjam uang rentenir dengan suku bunga mengambang di atas 50% per semester.",
            "Tidak layak, karena perhitungan NPV bernilai negatif Rp-10.000.000 setelah memperhitungkan biaya sewa aula sekolah.",
            "Netral, karena nilai uang di masa depan selalu dianggap sama persis dengan nilai uang saat ini menurut asas akuntansi tunai."
        ],
        "formula": {
            "title": "FORMULA NET PRESENT VALUE (NPV)",
            "latex": "NPV = \\sum_{t=1}^{n} \\frac{CF_t}{(1 + r)^t} - C_0 = (40jt \\times 0{,}9091) + (40jt \\times 0{,}8264) + (40jt \\times 0{,}7513) - 100jt",
            "legend": "• $PV_1 = 40.000.000 \\times 0{,}9091 = 36.364.000$<br>• $PV_2 = 40.000.000 \\times 0{,}8264 = 33.056.000$<br>• $PV_3 = 40.000.000 \\times 0{,}7513 = 30.052.000$<br>• $\\text{Total PV Arus Kas} = 36.364.000 + 33.056.000 + 30.052.000 = \\text{Rp}106.480.000$<br>• $NPV = 106.480.000 - 100.000.000 = \\text{Rp}+6.480.000$ ($NPV > 0 \\implies$ Layak Diterima)"
        },
        "hints": {
            "concept": "NPV adalah selisih antara nilai sekarang arus kas masuk (PV of Inflows) dengan nilai investasi awal. Jika NPV > 0, proyek investasi dinyatakan layak diterima.",
            "execution": "Total PV = 40jt * (0,9091 + 0,8264 + 0,7513) = 40jt * 2,662 = 106.480.000. NPV = 106.480.000 - 100.000.000 = +Rp6.480.000."
        }
    },
    {
        "id": "pkk-lat-h-02",
        "materi": "MANAJEMEN KUALITAS STATISTIK (SPC)",
        "topic": "Statistical Process Control: X-bar Chart & Batas Kendali",
        "stem": "Dalam produksi massal poros engkol silinder mini di Teaching Factory SMK, diameter standar ditetapkan pada spesifikasi 20,00 mm. Tim Quality Assurance mengambil sampel acak harian dan memplot hasil pengukuran pada peta kendali (X-bar chart). Data menunjukkan selama 8 hari berturut-turut, rata-rata diameter berada di antara garis tengah (Center Line) dan batas kendali atas (Upper Control Limit / UCL) tanpa satu pun titik yang jatuh di bawah Center Line. Berdasarkan kaidah Western Electric Rules, kesimpulan status proses produksi tersebut adalah...",
        "correct": "Proses berada di luar kendali statistik (Out of Statistical Control) akibat adanya gejala pergeseran proses (run/trend) yang memerlukan investigasi keausan mata pahat mesin bubut.",
        "distractors": [
            "Proses berada dalam kendali sempurna karena tidak ada titik pengukuran yang melintasi garis batas kendali atas (UCL).",
            "Mesin CNC harus segera dimusnahkan karena hukum fisika melarang poros logam memiliki diameter 20 milimeter.",
            "Karyawan bengkel berhak mendapatkan kenaikan gaji 100% karena grafik menunjukkan stabilitas garis lurus tanpa gelombang.",
            "Seluruh produk poros engkol harus dicairkan kembali ke tungku peleburan logam tanpa perlu memeriksa mata pahat."
        ],
        "formula": {
            "title": "ATURAN ANOMALI PETA KENDALI SPC (WESTERN ELECTRIC RULES)",
            "latex": "\\text{Run Violation: } 8 \\text{ atau lebih titik berturut-turut berada pada satu sisi Center Line} \\implies \\text{Special Cause Variation}",
            "legend": "• Run Rule: 8 titik beruntun pada satu sisi CL menunjukkan pergeseran rata-rata proses secara sistematis (bukan variasi alami/common cause)<br>• Penyebab Tipikal: Keausan alat potong (tool wear), penurunan tekanan fluida pendingin, atau pemuaian panas mesin"
        },
        "hints": {
            "concept": "Berdasarkan kaidah SPC, jika ada 8 titik berturut-turut di salah satu sisi Center Line, terjadi anomali run (Special Cause Variation) sehingga proses out of control.",
            "execution": "Proses out of statistical control akibat gejala run/trend pergeseran proses."
        }
    },
    {
        "id": "pkk-lat-h-03",
        "materi": "TOTAL PRODUCTIVE MAINTENANCE (TPM)",
        "topic": "Pengukuran Overall Equipment Effectiveness (OEE)",
        "stem": "Sebuah lini perakitan komponen elektronika SMK beroperasi dengan data harian: Ketersediaan Mesin (Availability Rate) = 90%, Efisiensi Kinerja Mesin (Performance Rate) = 85%, dan Tingkat Kualitas Produk Bebas Cacat (Quality Rate) = 95%. Berapakah nilai Overall Equipment Effectiveness (OEE) mesin tersebut dan bagaimana statusnya terhadap standar kelas dunia (World Class OEE minimal 85%)?",
        "correct": "72,68%, yang menunjukkan kinerja mesin masih berada di bawah standar kelas dunia (World Class) sehingga memerlukan penerapan pemeliharaan preventif (Preventive Maintenance) yang lebih disiplin.",
        "distractors": [
            "90,00%, karena nilai OEE secara otomatis mengikuti nilai metrik tertinggi dari ketiga parameter mesin.",
            "85,00%, yang berarti mesin telah tepat memenuhi standar kelas dunia tanpa perlu evaluasi pemborosan waktu henti.",
            "270,0%, dihitung dari penjumlahan langsung ketiga persentase metrik operasional harian.",
            "50,00%, karena efisiensi mesin di sekolah selalu dibagi dua akibat libur akhir pekan."
        ],
        "formula": {
            "title": "FORMULA OVERALL EQUIPMENT EFFECTIVENESS (OEE)",
            "latex": "OEE = \\text{Availability} \\times \\text{Performance} \\times \\text{Quality} = 0{,}90 \\times 0{,}85 \\times 0{,}95 = 0{,}72675 \\approx 72{,}68\\%",
            "legend": "• Availability (90%): Rasio waktu operasi aktual terhadap waktu operasi terencana<br>• Performance (85%): Rasio kecepatan produksi aktual terhadap kapasitas kecepatan ideal mesin<br>• Quality (95%): Rasio produk baik terhadap total produk yang diproses<br>• Benchmark World Class: OEE $\\ge 85\\%$ (Availability $\\ge 90\\%$, Performance $\\ge 95\\%$, Quality $\\ge 99{,}9\\%$)"
        },
        "hints": {
            "concept": "OEE dihitung dengan mengalikan Availability x Performance x Quality. Nilai < 85% berada di bawah standar World Class.",
            "execution": "0,90 * 0,85 * 0,95 = 0,72675 = 72,68% (di bawah standar World Class 85%)."
        }
    },
    {
        "id": "pkk-lat-h-04",
        "materi": "ANALISIS BIAYA & TITIK IMPAS",
        "topic": "Titik Impas Multi-Produk (Sales Mix BEP)",
        "stem": "Unit konveksi siswa SMK memproduksi dua jenis produk: Kemeja Kerja (Produk A) dan Kaos Olahraga (Produk B) dengan proporsi bauran penjualan (Sales Mix) 40% : 60%. Margin Kontribusi per unit adalah Rp50.000 untuk Kemeja dan Rp20.000 untuk Kaos. Jika total Biaya Tetap (Fixed Cost) bersama adalah Rp32.000.000 per bulan, total volume gabungan kedua produk yang harus terjual untuk mencapai titik impas (BEP) adalah...",
        "correct": "1.000 unit gabungan, terdiri atas 400 unit Kemeja (40%) dan 600 unit Kaos (60%), dihitung berdasarkan Margin Kontribusi Rata-Rata Tertimbang sebesar Rp32.000 per unit.",
        "distractors": [
            "640 unit gabungan, dihitung dengan membagi biaya tetap dengan margin kontribusi kemeja saja.",
            "1.600 unit gabungan, dihitung dengan membagi biaya tetap dengan margin kontribusi kaos olahraga saja.",
            "500 unit gabungan, karena target produksi bulanan siswa dibatasi maksimal oleh kepala bengkel.",
            "2.000 unit gabungan, dihitung dari penjumlahan biaya tetap dengan selisih margin kedua produk."
        ],
        "formula": {
            "title": "TITIK IMPAS MULTI-PRODUK (WEIGHTED AVERAGE BEP)",
            "latex": "\\overline{WCM} = (W_A \\times CM_A) + (W_B \\times CM_B) = (0{,}4 \\times 50.000) + (0{,}6 \\times 20.000) = 20.000 + 12.000 = \\text{Rp}32.000",
            "legend": "• $\\text{BEP Total} = \\frac{FC}{\\overline{WCM}} = \\frac{32.000.000}{32.000} = 1.000 \\text{ unit}$<br>• Alokasi: Produk A $= 40\\% \\times 1.000 = 400$ unit; Produk B $= 60\\% \\times 1.000 = 600$ unit"
        },
        "hints": {
            "concept": "Cari Margin Kontribusi Tertimbang: (0,4 x 50.000) + (0,6 x 20.000) = 20.000 + 12.000 = 32.000. BEP Total = 32.000.000 / 32.000 = 1.000 unit.",
            "execution": "1.000 unit gabungan (400 Kemeja dan 600 Kaos)."
        }
    },
    {
        "id": "pkk-lat-h-05",
        "materi": "MANAJEMEN RISIKO OPERASIONAL",
        "topic": "Failure Mode and Effects Analysis (FMEA) & RPN",
        "stem": "Dalam evaluasi proses pembuatan panel pintu mobil berbahan komposit serat rami di bengkel SMK, tim Quality Engineering mengidentifikasi potensi kegagalan: 'Perekatan resin tidak merata yang menyebabkan delaminasi lapisan'. Penilaian parameter risiko menunjukkan: Tingkat Keparahan (Severity / S) = 8, Tingkat Kejadian (Occurrence / O) = 5, dan Kemampuan Deteksi (Detection / D) = 6. Berapakah nilai Risk Priority Number (RPN) dari kegagalan tersebut dan apa tindak lanjutnya?",
        "correct": "RPN = 240, yang tergolong berisiko tinggi (karena melebihi batas kritis tipikal industri yaitu RPN 100), sehingga memerlukan tindakan korektif segera berupa kalibrasi dispenser resin otomatis dan inspeksi ultrasonik.",
        "distractors": [
            "RPN = 19, dihitung dari penjumlahan ketiga nilai parameter, sehingga tidak memerlukan tindakan pencegahan apa pun.",
            "RPN = 40, karena tingkat kejadian dikalikan tingkat keparahan tanpa memperhitungkan faktor deteksi operator.",
            "RPN = 1.000, yang berarti pabrik harus ditutup secara permanen oleh pengawas ketenagakerjaan daerah.",
            "RPN = 48, dihitung dengan membagi tingkat keparahan dengan selisih waktu pengeringan resin."
        ],
        "formula": {
            "title": "FORMULA RISK PRIORITY NUMBER (FMEA)",
            "latex": "RPN = S \\times O \\times D = 8 \\times 5 \\times 6 = 240",
            "legend": "• Severity (S = 8): Dampak kegagalan sangat serius terhadap fungsi produk dan keselamatan<br>• Occurrence (O = 5): Frekuensi kemunculan cacat tergolong sedang-tinggi<br>• Detection (D = 6): Metode deteksi saat ini memiliki probabilitas lolos sedang<br>• Ambang RPN: > 100-120 mewajibkan rencana tindakan korektif (Corrective Action Plan) sebelum produksi massal"
        },
        "hints": {
            "concept": "RPN dihitung dari perkalian S x O x D. RPN = 8 x 5 x 6 = 240. Nilai > 100 mewajibkan tindakan korektif segera.",
            "execution": "RPN = 240 (kategori risiko tinggi, butuh tindakan mitigasi segera)."
        }
    },
    {
        "id": "pkk-lat-h-06",
        "materi": "HAK CIPTA & LISENSI PERANGKAT LUNAK",
        "topic": "Lisensi Perangkat Lunak: GPL v3 Copyleft vs MIT Permissive",
        "stem": "Siswa SMK Jurusan Rekayasa Perangkat Lunak mengembangkan platform aplikasi manajemen bengkel berbasis komersial yang akan dijual lisensinya secara tertutup (closed-source proprietary) kepada jaringan bengkel resmi. Dalam pengembangannya, siswa berniat menyertakan pustaka kode (library) sumber terbuka yang berlisensi GNU General Public License versi 3 (GPL v3). Ditinjau dari aspek kepatuhan hukum HAKI dan lisensi open source, konsekuensi dari tindakan tersebut adalah...",
        "correct": "Terjadinya pelanggaran lisensi jika kode tetap ditutup, karena klausul 'copyleft' (viral clause) pada GPL v3 mewajibkan seluruh kode program turunan yang digabungkan ikut dibuka kode sumbernya (open source) dengan lisensi GPL v3 yang sama.",
        "distractors": [
            "Aman secara hukum tanpa syarat apa pun, karena perangkat lunak buatan siswa sekolah bebas dari jeratan hukum hak cipta internasional.",
            "Aplikasi otomatis menjadi milik pemerintah Republik Indonesia tanpa hak royalti bagi siswa.",
            "Pemilik bengkel resmi wajib membayar royalti tambahan sebesar 80% langsung kepada pencipta kernel Linux.",
            "Siswa diperbolehkan menutup kode asalkan mereka menghapus seluruh komentar teks di baris awal file program."
        ],
        "formula": {
            "title": "TAKSONOMI LISENSI OPEN SOURCE (OPEN SOURCE INITIATIVE)",
            "latex": "\\text{GPL v3 (Strong Copyleft)} \\implies \\text{Derivative Works MUST be GPL v3 (Open)}; \\quad \\text{MIT/Apache (Permissive)} \\implies \\text{Closed Allowed}",
            "legend": "• GPL (General Public License): Bersifat resiprokal (viral). Menggabungkan kode GPL mewajibkan seluruh proyek berlisensi GPL<br>• MIT / BSD / Apache 2.0: Bersifat permisif, mengizinkan penggunaan dalam software komersial tertutup dengan tetap menyertakan atribusi copyright asli"
        },
        "hints": {
            "concept": "GPL v3 bersifat Strong Copyleft (resiprokal/viral). Menautkan kode proprietary dengan pustaka GPL mewajibkan seluruh kode turunan dibuka (open source).",
            "execution": "Terjadi pelanggaran jika kode tetap ditutup, karena sifat copyleft GPL v3 mewajibkan turunan dibuka."
        }
    },
    {
        "id": "pkk-lat-h-07",
        "materi": "MANAJEMEN RANTAI PASOK (SCM)",
        "topic": "Fenomena Bullwhip Effect dan Strategi Mitigasi VMI",
        "stem": "Dalam rantai pasok suku cadang sepeda motor buatan unit SMK, fluktuasi pesanan sebesar 5% di tingkat bengkel eceran (retailer) berubah menjadi lonjakan pesanan 18% di tingkat distributor grosir, dan membesar menjadi distorsi lonjakan pesanan 45% di pabrik manufaktur suku cadang. Dampak amplifikasi variabilitas permintaan ke arah hulu ini dinamakan Bullwhip Effect. Langkah integrasi rantai pasok paling mutakhir untuk mengeliminasi fenomena tersebut adalah...",
        "correct": "Menerapkan sistem Vendor-Managed Inventory (VMI) dan berbagi data transaksi titik penjualan (Point of Sale / POS) secara waktu nyata (real-time data sharing) di seluruh rantai pasok.",
        "distractors": [
            "Menimbun persediaan suku cadang hingga sepuluh kali lipat di gudang sekolah untuk berspekulasi terhadap harga besi.",
            "Memutuskan seluruh jalur komunikasi digital antar toko dan kembali menggunakan surat pos tercatat manual.",
            "Menaikkan batas minimal pesanan (Batch Order Size) menjadi sepuluh kontainer untuk setiap bengkel kecil di desa.",
            "Mengganti seluruh pemasok baja dengan pengepul besi tua tanpa perjanjian jaminan mutu pasokan."
        ],
        "formula": {
            "title": "FENOMENA BULLWHIP EFFECT DALAM SUPPLY CHAIN",
            "latex": "\\text{Bullwhip Ratio} = \\frac{\\sigma^2_{\\text{Orders}}}{\\sigma^2_{\\text{Demand}}} > 1 \\implies \\text{Distorsi Informasi Teramplifikasi ke Hulu}",
            "legend": "• Penyebab: Order batching, price fluctuation/diskon temporer, rationing and shortage gaming, lack of demand visibility<br>• Solusi: Vendor-Managed Inventory (VMI), Collaborative Planning Forecasting and Replenishment (CPFR), Electronic Data Interchange (EDI)"
        },
        "hints": {
            "concept": "Bullwhip effect terjadi akibat distorsi informasi permintaan di hulu rantai pasok. Solusinya adalah transparansi data POS real-time dan Vendor-Managed Inventory (VMI).",
            "execution": "Menerapkan Vendor-Managed Inventory (VMI) dan berbagi data POS real-time."
        }
    },
    {
        "id": "pkk-lat-h-08",
        "materi": "ANALISIS KEGAGALAN BISNIS (KEUANGAN)",
        "topic": "Model Prediksi Kepailitan: Altman Z-Score",
        "stem": "Guru pembimbing kewirausahaan mengevaluasi kondisi solvabilitas sebuah CV rintisan alumni SMK manufaktur yang telah berjalan 3 tahun menggunakan model Altman Z-Score untuk perusahaan non-manufaktur/UKM: $Z = 6{,}56 X_1 + 3{,}26 X_2 + 6{,}72 X_3 + 1{,}05 X_4$. Hasil perhitungan menghasilkan nilai skor akhir $Z = 1{,}15$. Berdasarkan batas interpretasi zona Altman Z-Score ($Z < 1{,}23$ Distress; $1{,}23 \\le Z \\le 2{,}90$ Grey; $Z > 2{,}90$ Safe), kondisi bisnis CV tersebut adalah...",
        "correct": "Zona Bahaya (Distress Zone), yang mengindikasikan probabilitas tinggi mengalami kepailitan finansial dalam kurun 1-2 tahun ke depan bila tidak dilakukan restrukturisasi utang dan modal kerja.",
        "distractors": [
            "Zona Aman (Safe Zone), yang berarti perusahaan memiliki cadangan kas melimpah dan siap melakukan ekspansi cabang ke mancanegara.",
            "Zona Abu-abu (Grey Zone), di mana probabilitas kebangkrutan sama persis dengan probabilitas memenangkan undian berhadiah bank.",
            "Zona Nol Risiko, karena seluruh utang perusahaan dijamin sepenuhnya oleh dana abadi pendidikan nasional.",
            "Perusahaan otomatis dibubarkan oleh kementerian hukum pada hari penghitungan skor selesai dilakukan."
        ],
        "formula": {
            "title": "AMBANG BATAS ALTMAN Z-SCORE (EMERGING MARKET / PRIVATE FIRMS)",
            "latex": "Z < 1{,}23 \\implies \\text{Distress Zone (High Bankruptcy Risk)}; \\quad Z > 2{,}90 \\implies \\text{Safe Zone}",
            "legend": "• $Z = 1{,}15 < 1{,}23 \\implies$ Masuk kategori Distress Zone (Gawat Finansial)<br>• Parameter: $X_1$ (Working Capital/Total Assets), $X_2$ (Retained Earnings/Total Assets), $X_3$ (EBIT/Total Assets), $X_4$ (Book Value Equity/Total Liabilities)"
        },
        "hints": {
            "concept": "Berdasarkan pedoman Altman Z-Score: Z < 1,23 masuk Distress Zone (Zona Bahaya Kebangkrutan). Nilai 1,15 jelas berada di Distress Zone.",
            "execution": "Zona Bahaya (Distress Zone) dengan risiko tinggi kepailitan."
        }
    },
    {
        "id": "pkk-lat-h-09",
        "materi": "METODE PENINGKATAN KUALITAS (SIX SIGMA)",
        "topic": "Siklus DMAIC & Kapabilitas Proses ($C_p$ dan $C_{pk}$)",
        "stem": "Dalam proyek Six Sigma untuk mengurangi tingkat cacat solderan PCB di Teaching Factory Elektronika SMK, tim proyek telah mendefinisikan masalah tingginya retak solder (Define) dan mengukur baseline cacat saat ini sebesar 15.000 DPMO (Measure). Langkah logis dan terstruktur berikutnya yang wajib dieksekusi oleh tim menurut fase DMAIC adalah...",
        "correct": "Fase Analyze, yaitu melakukan analisis akar penyebab (Root Cause Analysis) menggunakan diagram Fishbone dan metode 5-Why untuk mengidentifikasi variabel kritis penyebab retak solder.",
        "distractors": [
            "Fase Control, yaitu langsung membuat jadwal piket kebersihan laboratorium untuk mengunci proses yang belum diperbaiki.",
            "Fase Improve, yaitu langsung membeli mesin oven reflow baru seharga ratusan juta rupiah tanpa menyelidiki penyebab masalah.",
            "Fase Re-Define, yaitu mengubah batas toleransi cacat menjadi 50.000 DPMO agar produk cacat dianggap normal.",
            "Fase Dismiss, yaitu membubarkan tim proyek dan mengalihkan tanggung jawab kepada siswa kelas sepuluh."
        ],
        "formula": {
            "title": "SEKUENSI SIKLUS DMAIC (SIX SIGMA ROADMAP)",
            "latex": "\\text{Define} \\longrightarrow \\text{Measure} \\longrightarrow \\mathbf{Analyze} \\longrightarrow \\text{Improve} \\longrightarrow \\text{Control}",
            "legend": "• Define: Menentukan masalah bisnis, sasaran proyek, dan Critical to Quality (CTQ)<br>• Measure: Mengukur kinerja proses saat ini (baseline metric & DPMO)<br>• Analyze: Mengidentifikasi akar masalah mendasar (Fishbone, Pareto, FMEA, Uji Hipotesis)<br>• Improve: Merancang dan menguji solusi perbaikan<br>• Control: Memastikan hasil perbaikan bertahan secara berkelanjutan"
        },
        "hints": {
            "concept": "Urutan metodologi Six Sigma DMAIC adalah: Define -> Measure -> Analyze -> Improve -> Control. Setelah Measure adalah Analyze.",
            "execution": "Fase Analyze (analisis akar penyebab masalah)."
        }
    },
    {
        "id": "pkk-lat-h-10",
        "materi": "MANAJEMEN PROYEK (CPM / PERT)",
        "topic": "Jalur Kritis (Critical Path Method) dan Waktu Penyelesaian",
        "stem": "Proyek perakitan mesin pemotong rumput bertenaga surya oleh siswa SMK memiliki empat aktivitas: Aktivitas A (Desain Rangka, durasi 4 hari); Aktivitas B (Fabrikasi Logam, bergantung pada A, durasi 6 hari); Aktivitas C (Perakitan Sirkuit Surya, bergantung pada A, durasi 3 hari); dan Aktivitas D (Integrasi Akhir dan Pengujian, bergantung pada selesainya B dan C, durasi 5 hari). Jalur kritis (Critical Path) dan total durasi minimum penyelesaian proyek adalah...",
        "correct": "Jalur A-B-D dengan total durasi minimum 15 hari, di mana keterlambatan 1 hari pada aktivitas B akan langsung menunda tanggal penyelesaian akhir seluruh proyek.",
        "distractors": [
            "Jalur A-C-D dengan total durasi 12 hari, karena sirkuit surya membutuhkan waktu pengerjaan yang paling singkat.",
            "Jalur B-C dengan total durasi 9 hari, dihitung tanpa memperhitungkan tahapan desain awal dan integrasi akhir.",
            "Jalur A-B-C-D dengan total durasi 18 hari, yang diperoleh dengan menjumlahkan durasi keempat aktivitas secara serentak berurutan.",
            "Jalur Bebas dengan total durasi 3 hari, karena perakitan sirkuit surya dapat diabaikan bila cuaca sedang mendung."
        ],
        "formula": {
            "title": "PENENTUAN JALUR KRITIS (CRITICAL PATH METHOD)",
            "latex": "\\begin{aligned} \\text{Jalur 1 (A-B-D)} &: 4 + 6 + 5 = 15 \\text{ hari (Jalur Terpanjang = Critical Path)} \\\\ \\text{Jalur 2 (A-C-D)} &: 4 + 3 + 5 = 12 \\text{ hari (Memiliki Total Float / Slack } 3 \\text{ hari)} \\end{aligned}",
            "legend": "• Critical Path: Jalur terpanjang dari awal hingga akhir proyek yang menentukan durasi tercepat penyelesaian proyek<br>• Sifat Aktivitas Kritis: Float / Slack = 0 (Keterlambatan pada jalur ini berdampak langsung pada keterlambatan proyek)"
        },
        "hints": {
            "concept": "Hitung durasi tiap jalur: A-B-D = 4 + 6 + 5 = 15 hari. A-C-D = 4 + 3 + 5 = 12 hari. Jalur kritis adalah jalur terpanjang (A-B-D = 15 hari).",
            "execution": "Jalur A-B-D dengan total durasi 15 hari."
        }
    },
    {
        "id": "pkk-lat-h-11",
        "materi": "VALUASI STARTUP & PENDANAAN",
        "topic": "Pre-Money vs Post-Money Valuation dan Dilusi Saham",
        "stem": "Sebuah startup agritech rintisan siswa SMK memiliki valuasi awal sebelum investasi (Pre-Money Valuation) sebesar Rp800.000.000. Seorang investor malaikat (Angel Investor) menyuntikkan modal segar sebesar Rp200.000.000 secara tunai. Berapakah valuasi pasca-investasi (Post-Money Valuation) dan berapa persentase kepemilikan saham yang diperoleh investor baru tersebut?",
        "correct": "Post-Money Valuation sebesar Rp1.000.000.000 dan kepemilikan saham investor sebesar 20%, sehingga porsi kepemilikan pendiri awal terdelusi menjadi 80%.",
        "distractors": [
            "Post-Money Valuation sebesar Rp600.000.000 dan investor menguasai 33,3% saham perusahaan rintisan.",
            "Post-Money Valuation sebesar Rp1.600.000.000 dan investor berhak atas seluruh hak paten produk.",
            "Post-Money Valuation sebesar Rp800.000.000 dan saham investor dihitung sebagai utang piutang bunga nol persen.",
            "Post-Money Valuation sebesar Rp200.000.000 dan pendiri rintisan kehilangan seluruh hak kelola usaha."
        ],
        "formula": {
            "title": "FORMULA VALUASI STARTUP & DILUSI SAHAM",
            "latex": "\\text{Post-Money} = \\text{Pre-Money} + \\text{Investment}; \\quad \\text{Share\\%} = \\frac{\\text{Investment}}{\\text{Post-Money}} \\times 100\\%",
            "legend": "• $\\text{Post-Money} = 800.000.000 + 200.000.000 = \\text{Rp}1.000.000.000$<br>• Kepemilikan Investor $= \\frac{200.000.000}{1.000.000.000} \\times 100\\% = 20\\%$<br>• Dilusi Pendiri: Semula 100% $\\rightarrow$ Terdelusi menjadi $80\\%$"
        },
        "hints": {
            "concept": "Post-money = Pre-money + Investasi. Persentase saham investor = Investasi / Post-money.",
            "execution": "Post-money = 800jt + 200jt = 1 Milyar. Saham investor = 200jt / 1 M = 20%."
        }
    },
    {
        "id": "pkk-lat-h-12",
        "materi": "KESELAMATAN & KESEHATAN KERJA (K3LH)",
        "topic": "Nilai Ambang Batas (NAB) Kebisingan (Permenaker No. 5/2018)",
        "stem": "Di bengkel penempaan dan permesinan SMK, tingkat kebisingan mesin press hidrolik terukur konstan pada intensitas 88 dBA. Berdasarkan Peraturan Menteri Ketenagakerjaan No. 5 Tahun 2018 tentang Keselamatan dan Kesehatan Kerja Lingkungan Kerja, durasi paparan kebisingan maksimal yang diperkenankan bagi seorang pekerja tanpa alat pelindung telinga (earmuff/earplug) per hari kerja adalah...",
        "correct": "Maksimal 4 jam per hari kerja, karena standar NAB kebisingan menetapkan batas 85 dBA untuk 8 jam kerja dan setiap kenaikan 3 dBA memotong waktu paparan aman sebesar separuhnya (halving rate).",
        "distractors": [
            "Maksimal 8 jam per hari kerja, karena seluruh kebisingan di bawah 100 dBA dianggap aman bagi organ pendengaran manusia.",
            "Maksimal 15 menit per hari kerja, karena telinga manusia akan langsung mengalami ketulian permanen pada suara 80 dBA.",
            "Bebas tanpa batas waktu, asalkan pekerja mengenakan kacamata pelindung bening dan sarung tangan karet.",
            "Maksimal 24 jam sehari semalam, asalkan ruang bengkel dilengkapi dengan kipas angin berkecepatan tinggi."
        ],
        "formula": {
            "title": "NILAI AMBANG BATAS KEBISINGAN (PERMENAKER 5/2018)",
            "latex": "\\text{Waktu Paparan Aman: } 85\\text{ dBA} \\implies 8\\text{ jam}; \\quad 88\\text{ dBA} \\implies 4\\text{ jam}; \\quad 91\\text{ dBA} \\implies 2\\text{ jam}",
            "legend": "• Exchange Rate (Halving Rule): Kenaikan 3 dB (A) memotong durasi aman menjadi 50%<br>• Pengendalian Hirarki K3: Eliminasi sumber bising $\\rightarrow$ Enclosure/Peredam Akustik $\\rightarrow$ Rotasi Kerja $\\rightarrow$ APD (Ear plug / Ear muff NRR tinggi)"
        },
        "hints": {
            "concept": "Standar NAB Permenaker 5/2018: 85 dBA = 8 jam. Kenaikan 3 dBA menjadi 88 dBA memotong waktu aman menjadi setengahnya yaitu 4 jam.",
            "execution": "Maksimal 4 jam per hari kerja (aturan 3 dBA exchange rate)."
        }
    },
    {
        "id": "pkk-lat-h-13",
        "materi": "MANAJEMEN KETENAGAKERJAAN & HUKUM",
        "topic": "Regulasi PKWT dan Uang Kompensasi (PP No. 35/2021)",
        "stem": "Sebuah unit Teaching Factory SMK berbentuk badan usaha merekrut seorang teknisi terampil dengan status Perjanjian Kerja Waktu Tertentu (PKWT) selama masa kontrak 12 bulan penuh dengan upah tetap Rp4.000.000 per bulan. Pada saat masa kontrak 12 bulan tersebut berakhir dan tidak diperpanjang, kewajiban normatif pengusaha menurut PP No. 35 Tahun 2021 tentang PKWT, Alih Daya, Waktu Kerja, dan PHK adalah...",
        "correct": "Wajib membayar Uang Kompensasi PKWT sebesar 1 bulan upah (Rp4.000.000) kepada pekerja yang telah menyelesaikan masa kerja minimal 1 bulan atau lebih secara penuh.",
        "distractors": [
            "Tidak memiliki kewajiban finansial apa pun karena kontrak PKWT berakhir demi hukum tanpa adanya pesangon PHK.",
            "Wajib menyerahkan separuh aset tanah bengkel sekolah sebagai ganti rugi pemutusan hubungan kemitraan.",
            "Wajib membayar uang pesangon sebesar sepuluh kali lipat upah ditambah tunjangan perumahan seumur hidup.",
            "Memotong sisa upah pekerja sebesar 50% sebagai biaya administrasi pembersihan seragam kerja."
        ],
        "formula": {
            "title": "FORMULA UANG KOMPENSASI PKWT (PP 35/2021 PASAL 16)",
            "latex": "\\text{Uang Kompensasi} = \\frac{\\text{Masa Kerja (Bulan)}}{12} \\times 1 \\text{ Bulan Upah} = \\frac{12}{12} \\times \\text{Rp}4.000.000 = \\text{Rp}4.000.000",
            "legend": "• Subjek: Pekerja PKWT yang memiliki masa kerja minimal 1 bulan terus-menerus<br>• Pelaksanaan: Wajib diberikan pada saat berakhirnya jangka waktu PKWT (bahkan jika diperpanjang, kompensasi periode pertama wajib dibayarkan terlebih dahulu)"
        },
        "hints": {
            "concept": "Berdasarkan PP 35/2021, pekerja PKWT berhak atas uang kompensasi di akhir kontrak. Untuk masa kerja tepat 12 bulan, besaran kompensasi adalah 1 bulan upah.",
            "execution": "Wajib membayar Uang Kompensasi sebesar 1 bulan upah (Rp4.000.000)."
        }
    },
    {
        "id": "pkk-lat-h-14",
        "materi": "PERPAJAKAN USAHA (TAXATION)",
        "topic": "PPh Final UMKM (PP No. 55/2022) dan Batas Omzet Bebas Pajak",
        "stem": "Seorang wirausahawan muda alumni SMK mendirikan usaha bengkel las berbentuk Wajib Pajak Orang Pribadi (WP OP) dengan peredaran bruto (omzet) pada tahun pajak berjalan sebesar Rp650.000.000. Berdasarkan Peraturan Pemerintah No. 55 Tahun 2022 (harmonisasi UU HPP), ketentuan omzet sampai dengan Rp500.000.000 setahun tidak dikenai pajak (PTKP Omzet). Berapakah jumlah Pajak Penghasilan (PPh) Final UMKM tarif 0,5% yang wajib disetor ke kas negara?",
        "correct": "Rp750.000, dihitung dari tarif 0,5% dikalikan bagian omzet kena pajak sebesar Rp150.000.000 (total omzet Rp650.000.000 dikurangi batas pembebasan Rp500.000.000).",
        "distractors": [
            "Rp3.250.000, dihitung secara keliru dari tarif 0,5% yang langsung dikalikan seluruh total omzet Rp650.000.000 tanpa memperhitungkan fasilitas pembebasan.",
            "Rp6.500.000, karena tarif pajak UMKM diatur secara sepihak sebesar 1% oleh dinas pendapatan daerah setempat.",
            "Rp0 (Nihil), karena usaha milik alumni sekolah kejuruan otomatis dibebaskan dari seluruh jenis kewajiban perpajakan negara selamanya.",
            "Rp15.000.000, dihitung dari tarif pajak badan hukum perseroan terbatas skala multinasional."
        ],
        "formula": {
            "title": "PPH FINAL UMKM WAJIB PAJAK ORANG PRIBADI (PP 55/2022)",
            "latex": "\\text{PPh Final} = 0{,}5\\% \\times (\\text{Omzet Bruto} - \\text{Pembebasan Rp}500\\text{ Juta}) = 0{,}5\\% \\times (650jt - 500jt) = \\text{Rp}750.000",
            "legend": "• WP OP UMKM: Fasilitas batasan peredaran bruto tidak kena pajak sampai dengan Rp500 juta dalam 1 Tahun Pajak<br>• Dasar Pengenaan Pajak (DPP): Rp650.000.000 - Rp500.000.000 = Rp150.000.000<br>• PPh Terutang: $0{,}005 \\times 150.000.000 = \\text{Rp}750.000$"
        },
        "hints": {
            "concept": "Sesuai PP 55/2022, WP Orang Pribadi UMKM mendapat pembebasan omzet hingga Rp500 juta. Pajak 0,5% hanya dikenakan pada selisih omzet di atas Rp500 juta.",
            "execution": "PPh = 0,5% x (650jt - 500jt) = 0,5% x 150jt = Rp750.000."
        }
    },
    {
        "id": "pkk-lat-h-15",
        "materi": "MANAJEMEN KUALITAS & ISO",
        "topic": "ISO 9001:2015: Pengendalian Output Tidak Sesuai",
        "stem": "Dalam audit sertifikasi sistem manajemen mutu ISO 9001:2015 di unit manufaktur SMK, auditor menemukan bahwa 50 batang poros bubut yang tidak memenuhi spesifikasi toleransi diameter (cacat/reject) diletakkan berdampingan di palet yang sama dengan produk yang telah lulus uji QC tanpa label penanda. Klausul ISO 9001:2015 yang dilanggar dan tindakan mitigasi standar yang wajib dilakukan adalah...",
        "correct": "Klausul 8.7 (Pengendalian Output yang Tidak Sesuai), yang mewajibkan identifikasi visual yang jelas, pemisahan fisik (karantina), dan penetapan status disposisi agar produk cacat tidak terkirim atau terpakai secara tidak sengaja.",
        "distractors": [
            "Klausul 5.1 (Kepemimpinan), yang mewajibkan kepala sekolah mencabut beasiswa seluruh siswa yang mengoperasikan mesin bubut.",
            "Klausul 7.1 (Sumber Daya), yang mewajibkan sekolah mengganti seluruh palet kayu menjadi palet baja nirkarat tahan gempa.",
            "Klausul 4.1 (Konteks Organisasi), yang mengharuskan unit bengkel dipindahkan lokasinya ke luar batas administrasi kabupaten.",
            "Klausul 9.3 (Tinjauan Manajemen), yang mewajibkan pembatalan seluruh kontrak kerja sama industri secara sepihak."
        ],
        "formula": {
            "title": "PRINSIP ISO 9001:2015 KLAUSUL 8.7 (NONCONFORMING OUTPUTS)",
            "latex": "\\text{Non-Conforming Output} \\implies \\text{Segregasi Fisik (Karantina)} + \\text{Label Merah (Identifikasi)} + \\text{Disposisi (Rework/Scrap)}",
            "legend": "• Tujuan Klausul 8.7: Mencegah unintended delivery atau unintended use dari produk cacat<br>• Opsi Disposisi: (a) Tindakan koreksi/pengerjaan ulang (rework), (b) Pemisahan/penahanan (containment), (c) Pemberitahuan kepada pelanggan, (d) Konsesi izin pelepasan"
        },
        "hints": {
            "concept": "Klausul ISO 9001:2015 untuk penanganan produk reject/tidak sesuai adalah Klausul 8.7 (Control of nonconforming outputs) dengan segregasi fisik dan pelabelan karantina.",
            "execution": "Klausul 8.7 (Pengendalian Output yang Tidak Sesuai) dan pemisahan karantina berlabel jelas."
        }
    },
    {
        "id": "pkk-lat-h-16",
        "materi": "TEKNOLOGI PENGEMASAN PANGAN",
        "topic": "Modified Atmosphere Packaging (MAP) vs Vacuum",
        "stem": "Unit produksi pengolahan hasil nabati SMK memproduksi keripik jamur tiram krispi. Produk mengalami masalah cepat melempem (tengik) dalam waktu 3 minggu akibat oksidasi asam lemak tak jenuh dan penyerapan uap air. Teknologi pengemasan modern yang paling efektif untuk memperpanjang umur simpan (shelf-life) hingga 12 bulan tanpa menggunakan bahan pengawet kimia berbahaya adalah...",
        "correct": "Modified Atmosphere Packaging (MAP) dengan teknik Nitrogen Flushing dan kemasan multilayer aluminium foil (barrier tinggi), yang menggantikan gas oksigen di dalam kemasan dengan gas nitrogen inert (N₂).",
        "distractors": [
            "Mengemas keripik menggunakan kantong plastik kresek transparan tipis yang diikat dengan tali rafia basah.",
            "Menyemprotkan cairan pestisida dosis rendah secara langsung ke permukaan keripik sebelum dimasukkan ke dalam toples kaca.",
            "Merendam keripik jamur di dalam air gula pekat kemudian membekukannya di dalam lemari es kamar mandi sekolah.",
            "Menutup kemasan menggunakan staples besi berkarat tanpa merekatkan lapisan plastik dengan alat continuous sealer."
        ],
        "formula": {
            "title": "PRINSIP PACKAGING MODIFIED ATMOSPHERE (MAP PANGAN)",
            "latex": "\\text{Shelf-life Extension} \\propto \\frac{1}{[O_2]} \\times \\text{Barrier}_{\\text{Alufoil}} \\implies \\text{Nitrogen Flushing (Inert N}_2 > 98\\%)",
            "legend": "• Mekanisme Kerusakan: Oksidasi lipid (tengik) dipicu oleh $O_2$ dan cahaya; Kehilangan kerenyahan dipicu oleh Water Vapor Transmission Rate (WVTR)<br>• Solusi MAP: Evakuasi udara diganti dengan $N_2$ (mencegah oksidasi dan berfungsi sebagai bantal pelindung mekanis dari remuknya keripik)"
        },
        "hints": {
            "concept": "Teknik terbaik memperpanjang umur simpan produk krispi berminyak tanpa pengawet adalah MAP (Modified Atmosphere Packaging) via Nitrogen Flushing dalam kemasan aluminium foil.",
            "execution": "Modified Atmosphere Packaging (MAP) dengan Nitrogen Flushing dan kemasan multilayer aluminium foil."
        }
    },
    {
        "id": "pkk-lat-h-17",
        "materi": "REKAYASA NILAI & BIAYA (TARGET COSTING)",
        "topic": "Target Costing dan Value Engineering",
        "stem": "Tim wirausaha SMK Desain Produk berniat meluncurkan kursi belajar ergonomis. Berdasarkan riset pasar, harga kompetitif yang bersedia dibayar oleh konsumen (Target Price) adalah Rp250.000 per unit. Manajemen sekolah menetapkan target margin laba kotor yang diharapkan sebesar 30% dari harga jual. Jika estimasi biaya produksi saat ini adalah Rp200.000 per unit, besarnya pengurangan biaya (Cost Reduction Target) yang harus dicapai melalui Rekayasa Nilai (Value Engineering) adalah...",
        "correct": "Rp25.000 per unit, karena Biaya Target (Target Cost) adalah Rp175.000 (Rp250.000 dikurangi margin laba Rp75.000), sehingga terdapat selisih efisiensi sebesar Rp25.000 dari biaya saat ini Rp200.000.",
        "distractors": [
            "Rp75.000 per unit, karena pengurangan biaya harus disamakan secara mutlak dengan total laba yang disetorkan ke kas sekolah.",
            "Rp50.000 per unit, dihitung dari selisih antara harga jual target dengan biaya produksi rancangan awal.",
            "Rp0 per unit, karena produk ergonomis sekolah diperbolehkan menjual dengan margin laba minus.",
            "Rp100.000 per unit, karena siswa diwajibkan bekerja lembur tanpa memperoleh kompensasi uang makan siang."
        ],
        "formula": {
            "title": "FORMULA TARGET COSTING (VALUE ENGINEERING)",
            "latex": "\\text{Target Cost} = \\text{Target Price} - \\text{Target Profit}; \\quad \\Delta \\text{Cost} = \\text{Current Cost} - \\text{Target Cost}",
            "legend": "• Target Price = Rp250.000<br>• Target Profit (30%) = $0{,}30 \\times 250.000 = \\text{Rp}75.000$<br>• Target Cost = $250.000 - 75.000 = \\text{Rp}175.000$<br>• Target Pengurangan Biaya = $200.000 - 175.000 = \\text{Rp}25.000$ per unit"
        },
        "hints": {
            "concept": "Target Cost = Target Price - Target Profit = 250.000 - 75.000 = 175.000. Pengurangan Biaya = Biaya Sekarang (200.000) - Target Cost (175.000) = 25.000.",
            "execution": "Rp25.000 per unit efisiensi yang harus dicapai."
        }
    },
    {
        "id": "pkk-lat-h-18",
        "materi": "STRATEGI WARALABA (FRANCHISE)",
        "topic": "Struktur Finansial Waralaba: Franchise Fee vs Royalty Fee",
        "stem": "Sebuah usaha minuman kopi susu literan karya Teaching Factory SMK telah sukses membuka 5 cabang mandiri dan kini menawarkan kemitraan waralaba (franchise). Dalam prospektus penawaran, tertulis dua komponen biaya: Biaya A sebesar Rp20.000.000 dibayar satu kali di awal untuk hak lisensi merek dan pelatihan selama 3 tahun, sedangkan Biaya B sebesar 5% dari omzet kotor bulanan dibayarkan secara rutin setiap tanggal 5. Definisi yang tepat untuk Biaya A dan Biaya B tersebut adalah...",
        "correct": "Biaya A adalah Franchise Fee (Biaya Awal Waralaba) dan Biaya B adalah Royalty Fee (Biaya Royalti Operasional Berkelanjutan).",
        "distractors": [
            "Biaya A adalah Royalty Fee dan Biaya B adalah Franchise Fee.",
            "Biaya A adalah Pajak Bumi dan Bangunan dan Biaya B adalah Upah Lembur Karyawan Toko.",
            "Biaya A adalah Biaya Asuransi Kebakaran dan Biaya B adalah Denda Keterlambatan Pengiriman Kopi.",
            "Biaya A adalah Uang Jaminan Sewa Tempat dan Biaya B adalah Beban Penyusutan Mesin Kasir."
        ],
        "formula": {
            "title": "STRUKTUR KONTRAK FINANSIAL WARALABA (PP 42/2007)",
            "latex": "\\text{Total Biaya Mitra} = \\text{Franchise Fee (Lump-Sum Initial)} + \\sum_{t} \\text{Royalty Fee (\\% Turnover)} + \\text{Marketing Levy}",
            "legend": "• Franchise Fee: Biaya hak penggunaan merek, SOP, resep rahasia, dan training awal (dibayar sekali di muka)<br>• Royalty Fee: Biaya keberlanjutan dukungan teknis, riset pengembangan produk, dan supervisi kualitas (dibayar persentase periodik dari omzet)"
        },
        "hints": {
            "concept": "Biaya lisensi satu kali di awal = Franchise Fee. Persentase berkala dari omzet bulanan = Royalty Fee.",
            "execution": "Biaya A = Franchise Fee; Biaya B = Royalty Fee."
        }
    },
    {
        "id": "pkk-lat-h-19",
        "materi": "MANAJEMEN KONTINUITAS BISNIS (BCP)",
        "topic": "RTO vs RPO dalam Business Continuity Plan",
        "stem": "Platform e-commerce rintisan siswa SMK mengalami insiden kegagalan server basis data akibat lonjakan lalu lintas promosi diskon tanggal kembar. Dalam dokumen Business Continuity Plan (BCP) dan Disaster Recovery Plan (DRP), tim IT menetapkan target Recovery Time Objective (RTO) maksimal 2 jam dan Recovery Point Objective (RPO) maksimal 15 menit. Arti praktis dari RTO dan RPO tersebut bagi operasional bisnis adalah...",
        "correct": "Sistem wajib pulih dan beroperasi normal kembali paling lambat dalam waktu 2 jam sejak terjadinya bencana (RTO), dan toleransi kehilangan data transaksi maksimal adalah data 15 menit terakhir sebelum insiden (RPO).",
        "distractors": [
            "Sistem hanya boleh online selama 2 jam per hari dan seluruh transaksi harus dihapus setiap 15 menit.",
            "Pengembang berhak tidur selama 2 jam sebelum membaca pesan peringatan kegagalan server.",
            "Perusahaan harus membayar denda ganti rugi kepada seluruh pengguna sebesar Rp2.000.000 setiap 15 menit server padam.",
            "Server cadangan dilarang dinyalakan sebelum 2 jam pemadaman total berlangsung."
        ],
        "formula": {
            "title": "METRIK KONTINUITAS BENCANA (ISO 22301 / BCP)",
            "latex": "\\text{RTO} = \\text{Target Durasi Down-time}; \\quad \\text{RPO} = \\text{Toleransi Kehilangan Data (Data Loss Window)}",
            "legend": "• RTO (Recovery Time Objective): Batas waktu maksimal pemulihan sistem ke kondisi operasional setelah gangguan<br>• RPO (Recovery Point Objective): Titik waktu toleransi hilangnya data transaksi akibat disaster (menentukan frekuensi backup data)"
        },
        "hints": {
            "concept": "RTO = target waktu pemulihan sistem (berapa lama boleh mati). RPO = toleransi kehilangan data (seberapa banyak data boleh hilang sebelum waktu backup terakhir).",
            "execution": "Sistem pulih maksimal 2 jam (RTO) dan batas hilang data maksimal 15 menit (RPO)."
        }
    },
    {
        "id": "pkk-lat-h-20",
        "materi": "STRATEGI DISTRIBUSI & OMNICHANNEL",
        "topic": "Omnichannel Retailing vs Multichannel",
        "stem": "Sebuah merek jaket pengendara motor buatan siswa SMK menjual produknya melalui gerai toko fisik di sekolah, website resmi, dan toko resmi di tiga marketplace online. Pelanggan dapat memesan jaket melalui aplikasi smartphone, memilih ukuran di etalase web, lalu mencoba dan mengambil barang secara langsung di toko fisik (Click and Collect), serta mengembalikan barang di toko jika ukuran tidak pas dengan sinkronisasi inventaris stok otomatis. Pendekatan integrasi ritel ini disebut...",
        "correct": "Omnichannel Retailing, yaitu integrasi menyeluruh tanpa batas (seamless) dari semua saluran penjualan yang menyatukan pengalaman berbelanja pelanggan dan sinkronisasi data inventaris secara waktu nyata.",
        "distractors": [
            "Multichannel Konvensional, di mana setiap saluran penjualan beroperasi secara terisolasi tanpa sinkronisasi stok dan memiliki harga berbeda-beda.",
            "Single Channel Tradisional, di mana penjualan hanya dilakukan dengan menjajakan barang dari pintu ke pintu warga.",
            "Pemasaran Piramida Terlarang, di mana pembeli jaket diwajibkan mencari lima anggota baru untuk mendapatkan resi pengiriman.",
            "Dark Store Eksklusif, di mana toko fisik dilarang menerima kunjungan manusia dan hanya melayani kurir robot terbang."
        ],
        "formula": {
            "title": "EVOLUSI MODEL RITEL MODERN",
            "latex": "\\text{Single Channel} \\longrightarrow \\text{Multichannel (Siloed)} \\longrightarrow \\text{Omnichannel (Unified \& Seamless)}",
            "legend": "• Multichannel: Banyak kanal namun berjalan terpisah (silo); stok web beda dengan stok toko fisik<br>• Omnichannel: Semua kanal terintegrasi penuh; pelanggan menikmati pengalaman berbelanja holistik terpadu (BOPIS/Click & Collect, real-time inventory)"
        },
        "hints": {
            "concept": "Integrasi lintas kanal fisik dan digital secara mulus (pesan online ambil di toko, data stok sinkron) merupakan definisi Omnichannel Retailing.",
            "execution": "Omnichannel Retailing."
        }
    },
    {
        "id": "pkk-lat-h-21",
        "materi": "STRATEGI PENETAPAN HARGA DINAMIS",
        "topic": "Elastisitas Harga Permintaan ($E_d$) dan Dampak ke Total Pendapatan",
        "stem": "Usaha sablon casing smartphone siswa SMK memiliki koefisien elastisitas harga permintaan ($E_d$) sebesar $-2{,}5$ (bersifat elastis). Dalam rapat evaluasi akhir bulan, manajer pemasaran mengusulkan untuk menaikkan harga jual produk sebesar 20% demi melipatgandakan pendapatan total (Total Revenue). Ditinjau dari prinsip ekonomi mikro dan teori penetapan harga, keputusan menaikkan harga tersebut adalah...",
        "correct": "Keliru, karena untuk produk yang bersifat elastis ($|E_d| > 1$), kenaikan harga sebesar 20% akan memicu penurunan kuantitas permintaan yang jauh lebih besar (turun sekitar 50%), sehingga total pendapatan usaha justru akan anjlok drastis.",
        "distractors": [
            "Sangat tepat, karena kenaikan harga pada produk elastis selalu otomatis meningkatkan laba bersih sebesar kuadrat koefisien elastisitas.",
            "Netral, karena perubahan harga pada kurva elastis tidak akan pernah mempengaruhi kuantitas unit barang yang terjual di pasar.",
            "Ilegal, karena hukum persaingan usaha melarang penyesuaian harga jual melebihi 5% per tahun kalender.",
            "Tepat, asalkan siswa mengurangi volume produksi barang menjadi hanya satu unit per bulan."
        ],
        "formula": {
            "title": "HUBUNGAN ELASTISITAS PERMINTAAN DENGAN TOTAL REVENUE (TR)",
            "latex": "|E_d| > 1 \\text{ (Elastis)} \\implies P \\uparrow \\implies Q \\downarrow\\downarrow \\implies TR \\downarrow; \\quad P \\downarrow \\implies TR \\uparrow",
            "legend": "• $E_d = \\frac{\\% \\Delta Q}{\\% \\Delta P} = -2{,}5$<br>• Kenaikan harga 20% ($+\\% \\Delta P = +20\\%$) memicu penurunan permintaan: $\\% \\Delta Q = -2{,}5 \\times 20\\% = -50\\%$<br>• Dampak ke TR: Pendapatan total turun drastis (kebijakan yang benar untuk produk elastis adalah menurunkan harga atau memberi promo)"
        },
        "hints": {
            "concept": "Pada permintaan elastis (|Ed| > 1), kenaikan harga menyebabkan penurunan persentase kuantitas yang lebih besar sehingga Total Revenue (TR) justru menurun.",
            "execution": "Keliru, karena kenaikan harga pada produk elastis justru menjatuhkan Total Pendapatan (TR)."
        }
    },
    {
        "id": "pkk-lat-h-22",
        "materi": "MANAJEMEN ENERGI & LINGKUNGAN",
        "topic": "ISO 14001 dan Analisis Siklus Hidup Produk (LCA)",
        "stem": "Dalam rangka menerapkan prinsip Industri Hijau (Green Industry) dan sertifikasi ISO 14001 pada unit pembuatan furnitur kayu daur ulang siswa SMK, tim melakukan Life Cycle Assessment (LCA) mulai dari ekstraksi palet bekas, proses pemotongan, perakitan, pengecatan menggunakan pernis water-based, hingga pembuangan akhir oleh konsumen. Pendekatan penilaian dampak lingkungan dari awal pembentukan hingga akhir masa pakai produk ini disebut...",
        "correct": "Cradle-to-Grave (dari buaian hingga liang lahat), yang mengkaji jejak karbon dan dampak ekologis produk secara holistik di setiap tahapan siklus hidupnya.",
        "distractors": [
            "Gate-to-Gate, yang hanya menghitung jejak karbon saat kayu berada di atas meja pemotongan gergaji mesin.",
            "Cradle-to-Gate, yang berhenti menghitung dampak lingkungan tepat saat produk dimuat ke dalam truk distributor sekolah.",
            "Linear Waste Burning, yaitu pendekatan membakar seluruh serbuk gergaji kayu di halaman belakang sekolah secara terbuka.",
            "Ad-hoc Carbon Offset, yaitu sekadar menanam satu pohon bunga mawar di depan ruang kepala sekolah tanpa mengukur emisi."
        ],
        "formula": {
            "title": "BATASAN LIFE CYCLE ASSESSMENT (ISO 14040/14044)",
            "latex": "\\text{Cradle-to-Grave} = \\text{Raw Material Extraction} + \\text{Manufacturing} + \\text{Distribution} + \\text{Use Phase} + \\text{End-of-Life Disposal}",
            "legend": "• Cradle-to-Grave: Cakupan penuh dari ekstraksi bahan baku hingga pembuangan akhir/daur ulang<br>• Cradle-to-Cradle (Circular Economy): Limbah akhir diolah kembali menjadi bahan baku siklus industri baru<br>• Cradle-to-Gate: Cakupan dari ekstraksi bahan baku hingga pintu gerbang pabrik (sebelum sampai konsumen)"
        },
        "hints": {
            "concept": "Penilaian siklus hidup produk secara komprehensif dari ekstraksi bahan mentah sampai pembuangan akhir oleh konsumen disebut Cradle-to-Grave.",
            "execution": "Cradle-to-Grave (dari buaian hingga liang lahat)."
        }
    },
    {
        "id": "pkk-lat-h-23",
        "materi": "AUDIT ENERGI INDUSTRI",
        "topic": "Intensitas Konsumsi Energi (IKE) dan Payback Penghematan",
        "stem": "Audit energi di bengkel fabrikasi logam SMK mencatat total konsumsi listrik tahunan sebesar 120.000 kWh dengan tarif industri Rp1.500 per kWh (biaya tahunan Rp180.000.000). Konsultan menyarankan penggantian sistem penerangan konvensional dengan lampu LED pintar berbiaya investasi Rp15.000.000 yang mampu menghemat konsumsi energi bengkel sebesar 10% per tahun. Jangka waktu pengembalian investasi (Simple Payback Period) dari efisiensi energi tersebut adalah...",
        "correct": "10 bulan (atau 0,83 tahun), dihitung dari biaya investasi Rp15.000.000 dibagi dengan nilai penghematan listrik tahunan sebesar Rp18.000.000 (10% dari Rp180.000.000).",
        "distractors": [
            "24 bulan, karena penghematan energi listrik baru diakui secara resmi setelah masa garansi lampu LED berakhir.",
            "12 bulan, dihitung dengan asumsi tarif listrik industri mengalami kenaikan 100% setiap pergantian musim kemarau.",
            "5 bulan, dihitung dari selisih antara konsumsi energi bengkel dengan kapasitas daya gardu trafo sekolah.",
            "36 bulan, karena investasi efisiensi energi wajib diamortisasi selama masa belajar siswa tiga tahun penuh."
        ],
        "formula": {
            "title": "PAYBACK PERIOD PROYEK EFISIENSI ENERGI",
            "latex": "\\text{Penghematan Tahunan} = 10\\% \\times \\text{Rp}180.000.000 = \\text{Rp}18.000.000; \\quad \\text{Payback} = \\frac{15.000.000}{18.000.000} = 0{,}833 \\text{ tahun} \\approx 10 \\text{ bulan}",
            "legend": "• Investasi: Rp15.000.000<br>• Penghematan Listrik per Bulan: $\\frac{18.000.000}{12} = \\text{Rp}1.500.000$/bulan<br>• Payback: $15jt / 1{,}5jt = 10$ bulan (Sangat layak dan cepat menghasilkan ROI positif)"
        },
        "hints": {
            "concept": "Penghematan tahunan = 10% x 180jt = 18jt/tahun (1,5jt/bulan). Payback = Investasi / Penghematan = 15jt / 18jt = 0,833 tahun = 10 bulan.",
            "execution": "10 bulan (atau 0,83 tahun)."
        }
    },
    {
        "id": "pkk-lat-h-24",
        "materi": "STRATEGI KELUAR WIRAUSAHA (EXIT STRATEGY)",
        "topic": "Opsi Exit: M&A vs IPO Papan Akselerasi vs MBO",
        "stem": "Sebuah startup Internet of Things (IoT) otomotif yang didirikan alumni SMK telah membukukan pertumbuhan pendapatan 200% per tahun selama 4 tahun berturut-turut. Para pendiri ingin merealisasikan nilai kapitalisasi pasar perusahaan dengan menjual sebagian kepemilikan saham kepada publik melalui pencatatan perdana di Bursa Efek Indonesia (BEI) khusus untuk segmen perusahaan rintisan dan UMKM. Papan pencatatan BEI yang dirancang secara khusus untuk mengakomodasi kebutuhan emiten skala tersebut adalah...",
        "correct": "Papan Akselerasi, yang memberikan relaksasi persyaratan aset berwujud bersih dan masa operasional bagi perusahaan rintisan dan UKM berbadan hukum PT untuk melantai di bursa efek.",
        "distractors": [
            "Papan Utama, yang hanya diperuntukkan bagi korporasi konglomerasi raksasa dengan rekam jejak laba bersih berturut-turut minimal 3 tahun.",
            "Papan Pengembangan, yang ditujukan untuk perusahaan menengah yang telah membukukan laba operasional stabil skala puluhan miliar.",
            "Papan Pemantauan Khusus, yang diperuntukkan bagi emiten bermasalah yang sedang terancam sanksi delisting dari bursa efek.",
            "Papan Monopoli Negara, yang hanya memuat daftar emiten badan usaha milik negara di sektor pertahanan militer."
        ],
        "formula": {
            "title": "STRUKTUR PAPAN PENCATATAN BURSA EFEK INDONESIA (BEI)",
            "latex": "\\text{Papan Utama (Blue Chip)} \\longleftrightarrow \\text{Papan Pengembangan (Mid-Cap)} \\longleftrightarrow \\text{Papan Akselerasi (SMEs/Startups)}",
            "legend": "• Papan Akselerasi (POJK No. 53/POJK.04/2017 & Peraturan BEI I-V): Ditujukan untuk UKM & startup dengan karakteristik pertumbuhan tinggi namun aset berwujud bersih boleh di bawah Rp5 Miliar dan boleh belum membukukan laba bersih komersial"
        },
        "hints": {
            "concept": "Bursa Efek Indonesia (BEI) menyediakan Papan Akselerasi secara khusus untuk memfasilitasi pencatatan saham perdana (IPO) bagi UMKM dan startup rintisan.",
            "execution": "Papan Akselerasi BEI."
        }
    },
    {
        "id": "pkk-lat-h-25",
        "materi": "AKUISISI & STRUKTUR PENDANAAN",
        "topic": "Struktur Bagi Hasil & Perlindungan Hak Suara (Term Sheet)",
        "stem": "Dalam menegosiasikan lembar kesepakatan investasi (Term Sheet) dengan modal ventura (Venture Capital), pendiri startup siswa SMK ingin memastikan bahwa mereka tidak dapat dipecat secara sepihak dari posisi Direktur Utama oleh investor meskipun kepemilikan persentase saham pendiri terdelusi menjadi minoritas di masa depan. Instrumen hak proteksi yuridis yang paling tepat dicantumkan dalam perjanjian pemegang saham (Shareholders Agreement) adalah...",
        "correct": "Penerbitan Saham dengan Hak Suara Multipel (Multiple Voting Shares / Dual-Class Shares) atau klausul Hak Veto (Protective Provisions) khusus bagi pendiri atas keputusan pengangkatan dan pemberhentian direksi.",
        "distractors": [
            "Menyetujui klausul likuidasi penuh di mana seluruh modal disetor otomatis hangus bila pendiri jatuh sakit flu.",
            "Memberikan seluruh sertifikat saham perusahaan kepada investor tanpa membuat perjanjian pemegang saham.",
            "Menjual saham menggunakan sistem arisan berantai keluarga di mana pemegang saham diundi setiap arisan bulanan.",
            "Menerbitkan saham tanpa hak suara sama sekali bagi pendiri dan menyerahkan kuasa bank kepada pihak ketiga anonim."
        ],
        "formula": {
            "title": "INSTRUMEN TATA KELOLA KENDALI PENDIRI (FOUNDER CONTROL)",
            "latex": "\\text{Dual-Class Shares: } \\text{Saham Seri B (Founder)} \\implies 10\\times \\text{Voting Rights}; \\quad \\text{Saham Seri A (Investor)} \\implies 1\\times \\text{Voting Right}",
            "legend": "• Protective Provisions / Veto Rights: Klausul yang mewajibkan persetujuan tertulis pendiri untuk keputusan strategis (pemberhentian founder, merger, penjualan aset inti)<br>• Regulasi Indonesia: POJK No. 22/POJK.04/2021 mengizinkan penerapan Saham dengan Hak Suara Multipel (SHSM) bagi emiten inovatif"
        },
        "hints": {
            "concept": "Untuk melindungi posisi kendali pendiri saat saham terdelusi, digunakan instrumen Dual-Class Shares (Saham dengan Hak Suara Multipel / SHSM) atau klausul Protective Provisions/Hak Veto.",
            "execution": "Saham dengan Hak Suara Multipel (Dual-Class Shares) atau klausul Hak Veto khusus pendiri."
        }
    }
]
