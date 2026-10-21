# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Biologi (SMA/MA Saintek)
Dataset: Simulasi CBT HOTS (35 Authentic Questions, bio-sim-01 to 35)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
Composition:
  - 25 Authentic Single MCQ HOTS (bio-sim-01 to 25)
  - 5 Complex Multi-select HOTS (bio-sim-26 to 30)
  - 5 Matrix Benar-Salah HOTS (bio-sim-31 to 35)
"""

BIOLOGI_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 SINGLE MCQ HOTS (bio-sim-01 to bio-sim-25)
    # -------------------------------------------------------------
    {
        "id": "bio-sim-01",
        "materi": "TRANSPOR MEMBRAN AKTIF",
        "topic": "Pompa Na+/K+ ATPase dan Transpor Sekunder Glukosa Usus",
        "stem": "Penyerapan glukosa dari lumen usus halus ke dalam sel epitel enterosit berlangsung secara transpor aktif sekunder melalui simporter SGLT-1 ($\\text{Na}^+\\text{-Glucose Cotransporter 1}$). Jika enterosit diberi racun ouabain yang menghambat kerja enzim pompa $\\text{Na}^+/\\text{K}^+$ ATPase pada membran basolateral secara spesifik, dampak yang akan terjadi terhadap penyerapan glukosa adalah...",
        "correct": "Penyerapan glukosa di membran apikal terhenti total; inhibisi pompa $\\text{Na}^+/\\text{K}^+$ ATPase menyebabkan konsentrasi $\\text{Na}^+$ intraseluler meningkat dan gradien konsentrasi elektrokimia natrium melenyap, sehingga simporter SGLT-1 kehilangan gaya penggerak transpor glukosa melawan gradiennya.",
        "distractors": [
            "Penyerapan glukosa meningkat sepuluh kali lipat karena glukosa langsung berdifusi bebas menembus membran tanpa natrium.",
            "Glukosa diubah menjadi gas metana dan diekskresikan kembali ke rongga lambung secara spontan.",
            "Simporter SGLT-1 beralih menggunakan gradien ion kalsium untuk memompa glukosa keluar menuju feses.",
            "Enterosit membelah diri secara meiosis menghasilkan jutaan sel usus baru yang kebal terhadap racun ouabain."
        ],
        "formula": {
            "title": "MEKANISME TRANSPOR AKTIF SEKUNDER SGLT-1",
            "latex": "\\text{Pompa } \\text{Na}^+/\\text{K}^+\\text{ ATPase} \\implies [\\text{Na}^+]_i \\ll [\\text{Na}^+]_o \\implies \\text{Gradien Na}^+ \\text{ Menggerakkan Kotranspor Glukosa via SGLT-1}",
            "legend": "• Ouabain dan digitalis adalah glikosida jantung penghambat pompa $\\text{Na}^+/\\text{K}^+$ ATPase<br>• Transpor aktif sekunder tidak memakai ATP langsung, melainkan memanfaatkan energi potensial gradien ionik hasil transpor primer<br>• Di membran basolateral, glukosa keluar ke darah via difusi terfasilitasi GLUT-2"
        },
        "hints": {
            "concept": "SGLT-1 membutuhkan gradien natrium (Na+ luar tinggi, Na+ dalam rendah). Gradien ini dijaga oleh pompa Na+/K+ ATPase di membran basolateral. Jika pompa dihambat ouabain, gradien Na+ hilang, maka penyerapan glukosa terhenti.",
            "execution": "Pilih: penyerapan glukosa terhenti karena lenyapnya gradien konsentrasi natrium penggerak SGLT-1."
        }
    },
    {
        "id": "bio-sim-02",
        "materi": "BIOKIMIA PROTEIN & ALOSTERIK",
        "topic": "Kooperativitas Kurva Pengikatan Oksigen Hemoglobin vs Mioglobin",
        "stem": "Kurva pengikatan oksigen terhadap tekanan parsial oksigen ($P_{\\text{O}_2}$) pada mioglobin berbentuk hiperbola curam, sedangkan pada hemoglobin darah berbentuk sigmoid (kurva S). Karakteristik kurva sigmoid pada hemoglobin mencerminkan sifat fungsional...",
        "correct": "Kooperativitas positif pengikatan alosterik (efek homotropik); pengikatan molekul oksigen pertama pada salah satu subunit heme memicu perubahan konformasi kuaterner dari keadaan tegang (Tense / T state) berafinitas rendah menjadi keadaan rileks (Relaxed / R state) yang meningkatkan afinitas pengikatan oksigen pada subunit-subunit berikutnya.",
        "distractors": [
            "Inhibisi kompetitif ireversibel oleh molekul karbon monoksida yang mengkatalisis pemecahan rantai globin.",
            "Denaturasi termal selektif yang menyebabkan hemoglobin kehilangan ion besi ferro di kapiler paru-paru.",
            "Reaksi enzimatik proteolisis di mana molekul hemoglobin memakan molekul mioglobin otot rangka.",
            "Transpor pasif difusi terfasilitasi yang membutuhkan pembongkaran membran eritrosit secara periodik."
        ],
        "formula": {
            "title": "MODEL ALOSTERIK MWC KOOPERATIVITAS HEMOGLOBIN",
            "latex": "\\text{Hemoglobin: Tetramer } \\alpha_2\\beta_2; \\quad \\text{Keadaan T (Tense, Afinitas Rendah)} \\xrightleftharpoons{4\\text{O}_2} \\text{Keadaan R (Relaxed, Afinitas Tinggi)}",
            "legend": "• Mioglobin adalah monomer tunggal (tanpa interaksi antar-subunit) $\\implies$ Kurva Hiperbolik murni<br>• Hemoglobin adalah tetramer $\\implies$ Kooperativitas kurva Sigmoidal<br>• Memungkinkan saturasi $98\\%$ di paru-paru ($P_{\\text{O}_2} = 100\\text{ mmHg}$) dan pelepasan efektif di jaringan aktif ($P_{\\text{O}_2} = 20-40\\text{ mmHg}$)"
        },
        "hints": {
            "concept": "Kurva sigmoid hemoglobin disebabkan oleh kooperativitas positif: pengikatan O2 pada satu subunit memicu perubahan konformasi T -> R yang mempermudah pengikatan O2 berikutnya.",
            "execution": "Pilih kooperativitas positif pengikatan alosterik (transisi keadaan Tense ke Relaxed)."
        }
    },
    {
        "id": "bio-sim-03",
        "materi": "BIOENERGETIKA KATABOLISME",
        "topic": "Perbedaan Shuttle Malat-Aspartat vs Gliserol-3-Fosfat pada Hasil Bersih ATP",
        "stem": "Dalam respirasi aerob sel eukariotik, dua molekul NADH yang dihasilkan dari glikolisis di sitosol tidak dapat menembus membran dalam mitokondria secara langsung sehingga harus mentransfer elektronnya melalui sistem ulang-alik ($\\textit{shuttle system}$). Sel jantung dan hati menggunakan sistem ulang-alik malat-aspartat, sedangkan sel otot rangka dan otak menggunakan sistem ulang-alik gliserol-3-fosfat. Perbedaan hasil perolehan ATP netto per molekul glukosa antara kedua jaringan tersebut adalah...",
        "correct": "Sistem malat-aspartat menghasilkan $32\\text{ ATP}$ netto (karena elektron sitosol diserahkan ke $\\text{NAD}^+$ matriks pada Kompleks I), sedangkan sistem gliserol-3-fosfat menghasilkan $30\\text{ ATP}$ netto (karena elektron diserahkan ke $\\text{FAD}$ membran pada Kompleks II yang memotong satu situs pemompaan proton).",
        "distractors": [
            "Sistem malat-aspartat menghasilkan 38 ATP sedangkan gliserol-3-fosfat menghasilkan hanya 2 ATP seperti fermentasi laktat.",
            "Sistem gliserol-3-fosfat menghasilkan 36 ATP sedangkan malat-aspartat menghasilkan 12 ATP akibat hilangnya ion sitrat.",
            "Kedua sistem menghasilkan jumlah ATP yang identik persis yaitu 24 ATP di semua jenis sel eukariotik.",
            "Sistem malat-aspartat mengonsumsi ATP sedangkan gliserol-3-fosfat memproduksi asam lemak bebas di krista."
        ],
        "formula": {
            "title": "PERBANDINGAN SISTEM SHUTTLE ELEKTRON SITOSOL",
            "latex": "\\begin{aligned} \\text{Malat-Aspartat (Hati, Jantung):} & \\quad \\text{NADH}_{\\text{sitosol}} \\to \\text{NADH}_{\\text{matriks}} \\implies 2{,}5\\text{ ATP per NADH} \\implies \\text{Total } 32\\text{ ATP} \\\\ \\text{Gliserol-3-Fosfat (Otot, Otak):} & \\quad \\text{NADH}_{\\text{sitosol}} \\to \\text{FADH}_{2\\text{ (membran)}} \\implies 1{,}5\\text{ ATP per FADH}_2 \\implies \\text{Total } 30\\text{ ATP} \\end{aligned}",
            "legend": "• 1 Glukosa menghasilkan 2 NADH di sitosol (glikolisis)<br>• Masuk via Kompleks I (NADH matriks) = memompa 10 proton $\\implies 2{,}5\\text{ ATP}$<br>• Masuk via Kompleks II (FADH$_2$) = memompa 6 proton $\\implies 1{,}5\\text{ ATP}$<br>• Selisih 2 ATP netto per molekul glukosa"
        },
        "hints": {
            "concept": "Shuttle malat-aspartat menyerahkan elektron ke NAD+ matriks (Kompleks I, 2,5 ATP/NADH -> total 32 ATP). Shuttle gliserol-3-fosfat menyerahkan elektron ke FAD (Kompleks II, 1,5 ATP/FADH2 -> total 30 ATP).",
            "execution": "Pilih: malat-aspartat menghasilkan 32 ATP (via Kompleks I) dan gliserol-3-fosfat menghasilkan 30 ATP (via Kompleks II)."
        }
    },
    {
        "id": "bio-sim-04",
        "materi": "FOTOSINTESIS MOLEKULER",
        "topic": "Siklus Kok dan Kompleks Pelepasan Oksigen (OEC) pada Fotosistem II",
        "stem": "Fotolisis molekul air pada Fotosistem II (PS II) dikatalisis oleh gugus anorganik kluster mangan-kalsium ($\\text{Mn}_4\\text{CaO}_5$) yang terletak di sisi lumen tilakoid, dikenal sebagai Kompleks Pelepasan Oksigen ($\\textit{Oxygen-Evolving Complex / OEC}$). Berdasarkan model siklus Kok (Kok's S-state cycle), berapa jumlah foton cahaya yang harus diserap secara berturut-turut oleh pusat reaksi $P_{680}$ untuk memicu pelepasan satu molekul gas $\\text{O}_2$ tunggal?",
        "correct": "4 foton cahaya; karena pelepasan satu molekul $\\text{O}_2$ membutuhkan penarikan empat elektron dari dua molekul air ($2\\text{H}_2\\text{O} \\rightarrow 4\\text{H}^+ + 4e^- + \\text{O}_2$), sehingga OEC harus melalui transisi 4 tingkat oksidasi penyimpanan muatan (dari keadaan dasar $S_0$ hingga $S_4$ yang melepaskan $\\text{O}_2$).",
        "distractors": [
            "1 foton cahaya, karena satu foton mampu membelah seratus molekul air sekaligus secara kuantum resonansi.",
            "2 foton cahaya, dihitung dari koefisien dua pada rumus kimia molekul air reaktan.",
            "6 foton cahaya, sesuai dengan jumlah molekul karbon dioksida pada persamaan reaksi fotosintesis global.",
            "8 foton cahaya, karena setiap proton H+ membutuhkan dua kali eksitasi fotofosforilasi siklik."
        ],
        "formula": {
            "title": "SIKLUS S-STATE KOK PADA KOMPLEKS OEC (PS II)",
            "latex": "2\\text{H}_2\\text{O} \\xrightarrow{4\\,h\\nu} 4\\text{H}^+ + 4e^- + \\text{O}_2; \\quad S_0 \\xrightarrow{h\\nu} S_1 \\xrightarrow{h\\nu} S_2 \\xrightarrow{h\\nu} S_3 \\xrightarrow{h\\nu} [S_4] \\to S_0 + \\text{O}_2",
            "legend": "• Pusat reaksi $P_{680}^+$ adalah oksidan biologis terkuat yang diketahui di alam ($E^\\circ \\approx +1{,}25\\text{ V}$)<br>• Setiap penyerapan 1 foton memindahkan 1 elektron ($S_n \\to S_{n+1}$)<br>• Keadaan metastabil $S_4$ secara spontan mengoksidasi $2\\text{H}_2\\text{O}$ melepaskan $\\text{O}_2$ dan kembali ke $S_0$"
        },
        "hints": {
            "concept": "Reaksi fotolisis air: 2 H2O -> 4 H+ + 4 e- + O2. Dibutuhkan 4 elektron, dan setiap foton mengeksitasi 1 elektron. Jadi butuh 4 foton untuk 1 molekul O2.",
            "execution": "Pilih 4 foton cahaya (untuk mengekstraksi 4 elektron dari 2 H2O)."
        }
    },
    {
        "id": "bio-sim-05",
        "materi": "REPLIKASI DNA & PEMELIHARAAN GENOM",
        "topic": "Aktivitas Eksonuklease 3' ke 5' pada Proofreading DNA Polimerase",
        "stem": "Tingkat ketelitian replikasi DNA sangat luar biasa tinggi dengan tingkat kesalahan hanya sekitar satu kesalahan per satu miliar nukleotida ($10^{-9}$). Ketelitian tinggi ini sebagian besar ditentukan oleh kemampuan koreksi pembacaan ($\\textit{proofreading}$) intrinsik pada enzim DNA polimerase III. Aktivitas enzimatik yang bertanggung jawab atas mekanisme $\\textit{proofreading}$ tersebut adalah...",
        "correct": "Aktivitas eksonuklease $3' \\rightarrow 5'$; ketika basa yang salah dipasangkan di ujung 3', DNA polimerase berhenti bergerak maju, mundur satu langkah untuk memotong dan membuang nukleotida yang salah pasang tersebut, lalu melanjutkan kembali sintesis polimerisasi $5' \\rightarrow 3'$.",
        "distractors": [
            "Aktivitas endonuklease restriksi yang memotong seluruh untai cetakan DNA parental menjadi fragmen pendek.",
            "Aktivitas telomerase yang menambahkan sekuens heksanukleotida berulang untuk menutupi kesalahan pasangan basa.",
            "Aktivitas ligase yang menyambung ikatan hidrogen purin menjadi ikatan kovalen ganda.",
            "Aktivitas eksonuklease 5' ke 3' yang memakan primer RNA pada seluruh kromosom secara acak."
        ],
        "formula": {
            "title": "MEKANISME PROOFREADING 3' -> 5' EKSONUKLEASE",
            "latex": "\\text{Laju Salah Pasang Awal: } 10^{-4} - 10^{-5} \\xrightarrow{\\text{Eksonuklease } 3' \\to 5'} 10^{-7} \\xrightarrow{\\text{Mismatch Repair Post-Replikasi}} 10^{-9}",
            "legend": "• Situs katalitik polimerisasi ($5' \\to 3'$) terpisah secara spasial dari situs eksonuklease proofreading ($3' \\to 5'$)<br>• Ketidakcocokan geometri basa salah pasang memicu pergeseran ujung $3'$ ke situs eksonuklease<br>• Mutasi pada domain proofreading memicu sindrom kerapuhan genom dan kanker kolorektal (Lynch syndrome)"
        },
        "hints": {
            "concept": "Aktivitas proofreading DNA polimerase berjalan berlawanan arah dengan arah sintesis, yaitu memotong dari ujung 3' ke belakang: eksonuklease 3' -> 5'.",
            "execution": "Pilih aktivitas eksonuklease 3' ke 5'."
        }
    },
    {
        "id": "bio-sim-06",
        "materi": "SINTESIS PROTEIN & TRANSLASI",
        "topic": "Peran Faktor Elongasi EF-Tu, EF-G, dan Hidrolisis GTP di Ribosom",
        "stem": "Dalam tahap pemanjangan rantai polipeptida (elongasi translasi) pada ribosom bakteri, molekul aminoasil-tRNA diantarkan ke situs A ($\\textit{aminoacyl site}$) ribosom dengan bantuan faktor elongasi EF-Tu terikat GTP. Peristiwa translokasi ribosom berikutnya yang memindahkan peptidil-tRNA dari situs A ke situs P ($\\textit{peptidyl site}$) dikatalisis oleh...",
        "correct": "Faktor elongasi EF-G (translokase) dengan mengonsumsi energi dari hidrolisis molekul GTP menjadi GDP, mendorong ribosom bergerak maju sejauh tepat satu kodon (tiga nukleotida) ke arah ujung 3' mRNA.",
        "distractors": [
            "Enzim DNA helikase yang membakar molekul glukosa bebas di dalam cairan sitoplasma.",
            "Faktor terminasi RF-1 yang menambahkan molekul air pada ujung amino terminal rantai polipeptida.",
            "Kompleks proteasom 26S yang mencerna subunit besar 50S menjadi asam amino bebas.",
            "Enzim aminoasil-tRNA sintetase yang melepaskan ikatan peptidil secara hidrolisis asam kuat."
        ],
        "formula": {
            "title": "SIKLUS ELONGASI TRANSLASI & KONSUMSI ENERGI",
            "latex": "\\text{Aminoasil-tRNA} \\cdot \\text{EF-Tu} \\cdot \\text{GTP} \\to \\text{Situs A} \\implies \\text{Pembentukan Ikatan Peptida} \\implies \\text{EF-G} \\cdot \\text{GTP} \\to \\text{Translokasi Ribosom}",
            "legend": "• Setiap penambahan 1 asam amino mengonsumsi 4 ikatan fosfat berenergi tinggi: 2 ATP (saat penempelan asam amino ke tRNA oleh sintetase) + 1 GTP (pengikatan EF-Tu ke situs A) + 1 GTP (translokasi EF-G)<br>• Menjamin fidelitas pembacaan kodon mRNA yang sangat tinggi"
        },
        "hints": {
            "concept": "Translokasi ribosom (menggeser ribosom sejauh 1 kodon memindahkan tRNA dari situs A ke P) dikatalisis oleh faktor elongasi EF-G dengan energi dari hidrolisis GTP.",
            "execution": "Pilih faktor elongasi EF-G (translokase) menggunakan energi hidrolisis GTP."
        }
    },
    {
        "id": "bio-sim-07",
        "materi": "SITOGENETIKA KANKER (ABERASI STRUKTURAL)",
        "topic": "Translokasi Resiprokal Kromosom Philadelphia t(9;22) pada CML",
        "stem": "Pada pasien penderita Leukemia Mieloid Kronis (CML), pemeriksaan kariotipe sumsum tulang menunjukkan adanya kelainan kromosom Philadelphia yang terbentuk akibat translokasi resiprokal antara kromosom nomor 9 dan nomor 22, dinotasikan sebagai $t(9;22)(q34;q11)$. Konsekuensi molekuler dari translokasi ini yang memicu proliferasi sel darah putih tak terkendali adalah...",
        "correct": "Terbentuknya gen fusi onkogenik $\\textit{BCR-ABL}$ yang mengkode protein chimera dengan aktivitas tirosin kinase yang aktif secara konstitutif (terus-menerus memfosforilasi protein target tanpa memerlukan stimulasi faktor pertumbuhan luar).",
        "distractors": [
            "Hilangnya gen globin sehingga sel darah putih kehilangan kemampuan mengangkut gas karbon dioksida.",
            "Terjadinya duplikasi seluruh telomer sel darah yang menyebabkan sel darah mengalami penuaan seketika.",
            "Pembentukan kloroplas buatan di dalam sitoplasma limfosit yang memproduksi racun sianida.",
            "Mutasi titik pada gen insulin pankreas yang menghentikan metabolisme karbohidrat sel darah merah."
        ],
        "formula": {
            "title": "ONKOGENESIS FUSI BCR-ABL & TERAPI TARGET IMATINIB",
            "latex": "\\text{Translokasi } t(9;22) \\implies \\text{Gen Fusi } BCR\\text{-}ABL1 \\implies \\text{Tirosin Kinase Konstitutif} \\implies \\text{CML} \\xrightarrow{\\text{Inhibitor Imatinib}} \\text{Remisi Molekuler}",
            "legend": "• Lokus ABL1 dari kromosom 9q34 bergabung dengan lokus BCR di kromosom 22q11<br>• Menghasilkan kromosom 22 abnormal yang memendek (Kromosom Philadelphia)<br>• Obat inhibitor tirosin kinase target spesifik (Imatinib / Gleevec) memblokir situs pengikatan ATP BCR-ABL"
        },
        "hints": {
            "concept": "Translokasi t(9;22) menggabungkan gen BCR dan ABL menjadi gen fusi BCR-ABL yang menghasilkan protein tirosin kinase yang selalu aktif (konstitutif), memicu leukemia CML.",
            "execution": "Pilih terbentuknya gen fusi onkogenik BCR-ABL penghasil tirosin kinase aktif konstitutif."
        }
    },
    {
        "id": "bio-sim-08",
        "materi": "HEREDITAS ATAVISME (INTERAKSI GEN)",
        "topic": "Persilangan Bentuk Pial Ayam RrPp x Rrpp",
        "stem": "Bentuk pial (jengger) pada ayam dikendalikan oleh interaksi dua pasang gen non-alelik: gen $R$ dan $P$. Interaksi alel menghasilkan empat fenotipe: Walnut ($R\\_P\\_$), Rose ($R\\_pp$), Pea ($rrP\\_$), dan Single ($rrpp$). Jika ayam jantan berpial Walnut heterozigot ganda ($RrPp$) disilangkan dengan ayam betina berpial Rose heterozigot ($Rrpp$), persentase kemungkinan diperoleh keturunan berpial Pea adalah...",
        "correct": "$12{,}5\\%$ (atau $1$ dari $8$ anak), karena dari persilangan genotipe alel pertama ($Rr \\times Rr$) menghasilkan $\\frac{1}{4} rr$, dan persilangan alel kedua ($Pp \\times pp$) menghasilkan $\\frac{1}{2} P\\_$. Sifat pial Pea memiliki genotipe $rrP\\_$, sehingga peluangnya adalah $\\frac{1}{4} \\times \\frac{1}{2} = \\frac{1}{8} = 12{,}5\\%$.",
        "distractors": [
            "$25{,}0\\%$, dihitung jika hanya memperhitungkan segregasi salah satu pasang gen secara terpisah.",
            "$37{,}5\\%$, yang merupakan persentase perolehan anak ayam berpial Walnut (3/8).",
            "$6{,}25\\%$, dihitung jika mengasumsikan persilangan sesama dihibrid heterozigot ganda (1/16).",
            "$0\\%$, karena berasumsi pial Pea tidak mungkin muncul dari induk berpial Rose."
        ],
        "formula": {
            "title": "PERSILANGAN ATAVISME PIAL AYAM RrPp X Rrpp",
            "latex": "\\begin{aligned} Rr \\times Rr & \\implies \\frac{3}{4} R\\_, \\quad \\frac{1}{4} rr \\\\ Pp \\times pp & \\implies \\frac{1}{2} P\\_, \\quad \\frac{1}{2} pp \\\\ \\text{Pea } (rrP\\_) & = \\frac{1}{4} \\times \\frac{1}{2} = \\frac{1}{8} = 12{,}5\\% \\end{aligned}",
            "legend": "• Walnut ($R\\_P\\_$) = $\\frac{3}{4} \\times \\frac{1}{2} = \\frac{3}{8} = 37{,}5\\%$<br>• Rose ($R\\_pp$) = $\\frac{3}{4} \\times \\frac{1}{2} = \\frac{3}{8} = 37{,}5\\%$<br>• Pea ($rrP\\_$) = $\\frac{1}{4} \\times \\frac{1}{2} = \\frac{1}{8} = 12{,}5\\%$<br>• Single ($rrpp$) = $\\frac{1}{4} \\times \\frac{1}{2} = \\frac{1}{8} = 12{,}5\\%$"
        },
        "hints": {
            "concept": "Pial Pea = rrP_. Dari Rr x Rr didapat rr = 1/4. Dari Pp x pp didapat P_ = 1/2. Kalikan keduanya.",
            "execution": "Peluang Pea = 1/4 * 1/2 = 1/8 = 12,5%."
        }
    },
    {
        "id": "bio-sim-09",
        "materi": "EPIGENETIKA & KOMPENSASI DOSIS",
        "topic": "Hipotesis Lyon dan Inaktivasi Kromosom X pada Kucing Kaliko",
        "stem": "Pola belang tiga warna (hitam, oranye, dan putih / kaliko) pada bulu kucing hampir selalu ditemukan pada kucing betina ($XX$) dan sangat jarang pada jantan ($XY$). Gen pengkode warna bulu hitam ($X^B$) dan oranye ($X^O$) tertaut pada kromosom X secara kodominan, sedangkan bercak putih dikode oleh gen autosom $S$. Dasar sitogenetika yang menjelaskan mengapa warna hitam dan oranye muncul berselingan dalam bentuk mozaik pada kucing betina heterozigot ($X^B X^O$) adalah...",
        "correct": "Hipotesis Lyon (inaktivasi kromosom X acak); pada tahap awal perkembangan embrio, salah satu dari dua kromosom X di setiap sel somatik betina dipadatkan secara acak dan permanen menjadi badan Barr ($\\textit{Barr body}$), sehingga sel dengan kromosom $X^O$ aktif mengekspresikan pigmen oranye dan sel dengan kromosom $X^B$ aktif mengekspresikan pigmen hitam.",
        "distractors": [
            "Kucing jantan tidak memiliki melanin sama sekali di dalam folikel rambut kulitnya.",
            "Terjadi pindah silang meiosis yang terus-menerus memotong kromosom Y menjadi fragmen oranye.",
            "Warna oranye disebabkan oleh infeksi bakteri parasit obligat yang hanya menyerang sel jantan.",
            "Hormon testosteron mengubah seluruh pigmen hitam menjadi pigmen putih transparan."
        ],
        "formula": {
            "title": "HIPOTESIS LYON & INAKTIVASI KROMOSOM X (BADAN BARR)",
            "latex": "\\text{Embrio Heterozigot } X^B X^O \\xrightarrow{\\text{Inaktivasi Acak}} \\begin{cases} X^B \\text{ Aktif} & \\to \\text{Bercak Bulu Hitam} \\\\ X^O \\text{ Aktif} & \\to \\text{Bercak Bulu Oranye} \\end{cases} \\implies \\text{Mozaik Kaliko}",
            "legend": "• Dikendalikan oleh gen non-coding RNA $\\textit{Xist}$ (X-inactive specific transcript)<br>• Kromosom X terinaktivasi membentuk Heterokromatin padat di tepi membran nukleus (Badan Barr)<br>• Kucing jantan kaliko sangat langka dan hanya mungkin jika memiliki kelainan aneuploidi sindrom Klinefelter ($XXY$)"
        },
        "hints": {
            "concept": "Pada betina XX, salah satu kromosom X dinonaktifkan secara acak menjadi badan Barr di setiap sel embrio (Hipotesis Lyon). Sel yang mengaktifkan XB jadi hitam, sel yang mengaktifkan XO jadi oranye, membentuk mozaik belang kaliko.",
            "execution": "Pilih hipotesis Lyon: inaktivasi acak salah satu kromosom X menjadi badan Barr."
        }
    },
    {
        "id": "bio-sim-10",
        "materi": "PEWARISAN NON-MENDELIAN (MITOKONDRIA)",
        "topic": "Pola Pewarisan Maternal Penyakit Genetik Mitokondria",
        "stem": "Seorang pria menderita penyakit neuropati optik herediter Leber (LHON), yaitu kelainan atrofi saraf mata yang disebabkan oleh mutasi titik pada DNA mitokondria (mtDNA). Pria tersebut menikah dengan seorang wanita normal yang terbebas dari mutasi DNA mitokondria. Peluang anak-anak mereka (baik laki-laki maupun perempuan) mewarisi penyakit LHON tersebut dari ayahnya adalah...",
        "correct": "$0\\%$, karena materi genetik mitokondria diwariskan secara maternal murni (eksklusif dari ibu); mitokondria dari sperma ayah yang berada di bagian leher/ekor sperma tidak ikut masuk atau didegradasi secara selektif oleh ubiquitin sel telur pasca fertilisasi.",
        "distractors": [
            "100% pada anak laki-laki dan 0% pada anak perempuan karena penyakit terpaut kromosom Y.",
            "50% pada seluruh anak karena alel mitokondria memilah secara bebas menurut Hukum Mendel II.",
            "100% pada seluruh anak karena DNA mitokondria bersifat dominan absolut di atas DNA inti.",
            "25% pada anak perempuan pertama dan 75% pada anak laki-laki bungsu."
        ],
        "formula": {
            "title": "HUKUM PEWARISAN MATERNAL DNA MITOKONDRIA",
            "latex": "\\begin{aligned} \\text{Ibu Sakit} \\times \\text{Ayah Normal} & \\implies 100\\% \\text{ Seluruh Anak (Laki-laki & Perempuan) Mewarisi Mutasi} \\\\ \\text{Ayah Sakit} \\times \\text{Ibu Normal} & \\implies 0\\% \\text{ Anak Mewarisi Mutasi (Semua Anak Normal)} \\end{aligned}",
            "legend": "• Zigot mewarisi $> 100.000$ salinan mtDNA murni dari sitoplasma oosit ibu<br>• Mitokondria sperma dihancurkan melalui autofagi terinduksi fertilisasi<br>• Heteroplasmi: Variasi proporsi mtDNA mutan vs normal antar jaringan menentukan derajat keparahan klinis"
        },
        "hints": {
            "concept": "DNA mitokondria diwariskan 100% dari ibu (maternal inheritance). Ayah TIDAK PERNAH mewariskan mitokondria kepada anak-anaknya.",
            "execution": "Karena ayahnya yang sakit dan ibunya normal, peluang anaknya mewarisi penyakit adalah 0%."
        }
    },
    {
        "id": "bio-sim-11",
        "materi": "FISIOLOGI GINJAL & TEKANAN DARAH",
        "topic": "Kaskade Sistem Renin-Angiotensin-Aldosteron (RAAS)",
        "stem": "Saat terjadi dehidrasi berat atau pendarahan akut, penurunan tekanan darah arterial dan penurunan konsentrasi $\\text{NaCl}$ di tubulus distal dideteksi oleh sel makula densa dan sel jukstaglomerulus arteriol aferen ginjal. Respon endokrin ginjal yang memicu kaskade sistem RAAS untuk memulihkan tekanan darah adalah...",
        "correct": "Sel jukstaglomerulus mensekresikan enzim renin ke dalam darah $\\rightarrow$ renin memotong angiotensinogen dari hati menjadi Angiotensin I $\\rightarrow$ enzim ACE (di endotel kapiler paru-paru) mengubah Angiotensin I menjadi Angiotensin II aktif $\\rightarrow$ Angiotensin II memicu vasokonstriksi arteriol sistemik kuat dan merangsang korteks adrenal mensekresikan hormon aldosteron untuk meningkatkan reabsorpsi $\\text{Na}^+$ dan air di ginjal.",
        "distractors": [
            "Ginjal mensekresikan hormon insulin yang mengubah urea menjadi glukosa untuk menaikkan volume darah secara osmosis.",
            "Makula densa memproduksi hormon tiroksin yang menghancurkan pembuluh darah vena untuk menghentikan aliran balik.",
            "Kapsula Bowman mensekresikan eritropoietin yang langsung memicu pembekuan darah di bilik kiri jantung.",
            "Sel jukstaglomerulus menyerap seluruh molekul aldosteron dari darah untuk diekskresikan ke dalam kantung kemih."
        ],
        "formula": {
            "title": "KASKADE BIOKIMIA SISTEM RAAS GINJAL",
            "latex": "\\text{Hipotensi/Hipovolemia} \\implies \\text{Renin} + \\text{Angiotensinogen} \\to \\text{Ang I} \\xrightarrow{\\text{ACE}} \\text{Ang II} \\implies \\begin{cases} \\text{Vasokonstriksi Kuat (TD } \\uparrow) \\\\ \\text{Aldosteron } \\uparrow \\implies \\text{Retensi Na}^+ \\text{ & Air} \\end{cases}",
            "legend": "• Angiotensin II juga menstimulasi rasa haus di hipotalamus dan sekresi ADH<br>• Obat antihipertensi ACE inhibitor (kaptopril) dan ARB (losartan) bekerja memblokir sistem ini<br>• Mekanisme homeostatis kunci pemelihara Mean Arterial Pressure (MAP)"
        },
        "hints": {
            "concept": "Sistem RAAS: Ginjal lepas Renin -> ubah Angiotensinogen jadi Ang I -> ACE ubah jadi Ang II -> Ang II memicu vasokonstriksi dan sekresi Aldosteron (retensi Na+ & air).",
            "execution": "Pilih sekresi renin memicu pembentukan Angiotensin II dan aldosteron."
        }
    },
    {
        "id": "bio-sim-12",
        "materi": "FISIOLOGI RESPIRASI (EFEK BOHR)",
        "topic": "Pergeseran Kurva Disosiasi Oksihemoglobin pada Jaringan Aktif",
        "stem": "Saat otot rangka manusia melakukan kontraksi anaerobik intensif, terjadi peningkatan produksi asam laktat (penurunan pH / peningkatan $[\\text{H}^+]$), peningkatan tekanan parsial $\\text{CO}_2$, kenaikan suhu lokal, serta peningkatan kadar $2,3\\text{-bisfosfogliserat}$ ($2,3\\text{-BPG}$). Pengaruh perubahan kondisi mikrolingkungan ini terhadap kurva disosiasi oksihemoglobin (Efek Bohr) dan pasokan oksigen ke jaringan otot adalah...",
        "correct": "Kurva disosiasi oksihemoglobin bergeser ke arah kanan (afinitas hemoglobin terhadap $\\text{O}_2$ menurun), sehingga hemoglobin lebih mudah melepaskan molekul oksigen ke jaringan otot yang sedang aktif bermetabolisme.",
        "distractors": [
            "Kurva disosiasi bergeser ke arah kiri (afinitas $\\text{O}_2$ meningkat drastis), sehingga hemoglobin mengikat oksigen sangat kuat dan tidak melepaskannya.",
            "Molekul hemoglobin terurai menjadi asam amino bebas dan berhenti mengalir di dalam pembuluh darah kapiler.",
            "Afinitas hemoglobin terhadap gas karbon monoksida menjadi nol mutlak tanpa mempengaruhi ikatan oksigen.",
            "Kurva disosiasi berubah menjadi garis vertikal lurus sempurna menolak penyerapan molekul oksigen di paru-paru."
        ],
        "formula": {
            "title": "EFEK BOHR & PERGESERAN KURVA DISOSIASI HEMOGLOBIN",
            "latex": "\\text{Pergeseran ke Kanan (Pelepasan O}_2 \\uparrow): \\quad [\\text{H}^+] \\uparrow (\\text{pH} \\downarrow), \\ P_{\\text{CO}_2} \\uparrow, \\ \\text{Suhu} \\uparrow, \\ 2,3\\text{-BPG} \\uparrow",
            "legend": "• Menggeser $P_{50}$ (tekanan parsial untuk saturasi $50\\%$) ke nilai yang lebih tinggi<br>• Ion $\\text{H}^+$ dan $\\text{CO}_2$ menstabilkan konformasi Tense (T state) hemoglobin<br>• Adaptasi fisiologis sempurna: jaringan yang paling membutuhkan oksigen mendapat suplai pelepasan $\\text{O}_2$ paling banyak"
        },
        "hints": {
            "concept": "Efek Bohr: asam (pH turun), CO2 naik, suhu naik, 2,3-BPG naik -> kurva disosiasi geser ke KANAN -> afinitas turun -> O2 lebih mudah dilepas ke jaringan.",
            "execution": "Pilih pergeseran kurva ke kanan mempermudah pelepasan oksigen ke jaringan aktif."
        }
    },
    {
        "id": "bio-sim-13",
        "materi": "NEUROBIOLOGI (KONDUKSI SALTATORI)",
        "topic": "Peran Selubung Mielin dan Patofisiologi Multipel Sklerosis",
        "stem": "Serat saraf bermielin memiliki kecepatan konduksi impuls potensial aksi yang jauh lebih cepat (hingga $120\\text{ m/s}$) dibandingkan serat saraf tak bermielin ($1-2\\text{ m/s}$). Percepatan laju hantaran impuls ini dimungkinkan oleh mekanisme konduksi saltatori, di mana potensial aksi...",
        "correct": "Hanya dibangkitkan pada celah nodus Ranvier yang kaya saluran $\\text{Na}^+$ berpintu voltase; selubung mielin bertindak sebagai isolator listrik dengan resistensi tinggi dan kapasitansi rendah yang memungkinkan arus elektrotonik lokal mengalir cepat meloncat dari satu nodus Ranvier ke nodus berikutnya.",
        "distractors": [
            "Merambat merayap secara lambat di seluruh permukaan selubung lipid mielin tanpa melewati membran plasma.",
            "Menghidrolisis lapisan fosfolipid mielin menjadi bahan bakar pembakar neurotransmiter di badan sel neuron.",
            "Mengalir secara konduksi kawat tembaga murni bebas hambatan langsung dari otak ke ujung jari.",
            "Memicu pembentukan sinapsis elektrik baru di dalam selubung sel Schwann pada setiap mikron akson."
        ],
        "formula": {
            "title": "FISIKA KONDUKSI SALTATORI PADA AKSON BERMIELIN",
            "latex": "v_{\\text{konduksi}} \\propto \\lambda = \\sqrt{\\frac{r_m}{r_i}}; \\quad \\text{Mielin: } r_m \\text{ (resistensi membran)} \\uparrow, \\ C_m \\text{ (kapasitansi)} \\downarrow \\implies \\text{Depolarisasi Melompat di Nodus Ranvier}",
            "legend": "• Sel Schwann membentuk mielin di PNS, Oligodendrosit di CNS<br>• Multipel Sklerosis (MS): Penyakit autoimun perusak selubung mielin CNS $\\implies$ kebocoran arus $\\implies$ blokade konduksi saraf<br>• Menghemat konsumsi energi metabolik pompa $\\text{Na}^+/\\text{K}^+$"
        },
        "hints": {
            "concept": "Konduksi saltatori: impuls 'meloncat' dari nodus Ranvier ke nodus Ranvier berikutnya karena mielin bertindak sebagai isolator listrik. Potensial aksi hanya terjadi di nodus Ranvier.",
            "execution": "Pilih potensial aksi meloncat dari nodus Ranvier ke nodus berikutnya karena mielin sebagai isolator."
        }
    },
    {
        "id": "bio-sim-14",
        "materi": "IMUNOLOGI MOLEKULER (DIVERSITAS ANTIBODI)",
        "topic": "Rekombinasi Somatik V(D)J oleh Enzim RAG-1 dan RAG-2",
        "stem": "Tubuh manusia mampu memproduksi lebih dari $10^{11}$ varian antibodi yang berbeda dengan spesifisitas antigenik unik, padahal genom manusia hanya memiliki sekitar $20.000$ gen total. Mekanisme genetika molekuler pada sel limfosit B yang bertanggung jawab menghasilkan keanekaragaman reseptor antibodi yang sangat masif tersebut adalah...",
        "correct": "Rekombinasi somatik $V(D)J$; pemotongan dan penyambungan acak segmen gen Variable (V), Diversity (D), dan Joining (J) pada lokus rantai berat dan rantai ringan imunoglobulin oleh kompleks enzim rekombinase RAG-1 dan RAG-2 selama pematangan sel B di sumsum tulang.",
        "distractors": [
            "Penyalinan antigen patogen secara fotosintesis molekuler oleh sel darah putih di kelenjar timus.",
            "Mutasi nondisjunction kromosom somatik yang menggandakan seluruh genom menjadi poliploidi 16n.",
            "Transkripsi terbalik asam lemak jenuh menjadi urutan asam deoksiribonukleat di hati.",
            "Penempelan molekul kolesterol secara kovalen pada daerah konstan rantai berat antibodi."
        ],
        "formula": {
            "title": "MEKANISME KERAGAMAN ANTIBODI SUSUMU TONEGAWA",
            "latex": "\\text{Diversitas Total} = \\text{Kombinatorial } V(D)J \\times \\text{Diversitas Sambungan (TdT)} \\times \\text{Kombinasi Rantai Berat & Ringan} \\times \\text{Hipermutasi Somatik} > 10^{11}",
            "legend": "• Dianugerahi Hadiah Nobel 1987 untuk Susumu Tonegawa<br>• Enzim RAG-1/RAG-2 memotong sinyal rekombinasi (RSS)<br>• TdT (Terminal deoxynucleotidyl transferase) menambahkan nukleotida acak di titik sambungan"
        },
        "hints": {
            "concept": "Keanekaragaman antibodi triliunan jenis dihasilkan oleh pemotongan dan penyambungan acak segmen gen V, D, dan J (rekombinasi somatik V(D)J) yang dipotong oleh enzim RAG-1 dan RAG-2.",
            "execution": "Pilih rekombinasi somatik V(D)J oleh enzim RAG-1 dan RAG-2."
        }
    },
    {
        "id": "bio-sim-15",
        "materi": "FISIOLOGI TUMBUHAN (TRANSPOR AIR XILEM)",
        "topic": "Teori Kohesi-Tegangan (Cohesion-Tension Theory) Dixon-Joly",
        "stem": "Bagaimana pohon-pohon raksasa seperti $\\textit{Sequoia sempervirens}$ yang tingginya mencapai lebih dari 100 meter mampu mengangkut ribuan liter air dari tanah hingga ke pucuk daun tertinggi tanpa adanya pompa mekanik dijelaskan oleh Teori Kohesi-Tegangan ($\\textit{Cohesion-Tension Theory}$). Gaya fisik utama yang menggerakkan kolom air tersebut adalah...",
        "correct": "Transpirasi air melalui stomata daun menghasilkan tegangan negatif (tekanan hisap hidrostatik) pada mesofil daun yang menarik kolom air tak terputus ke atas melalui pembuluh xilem, didukung oleh gaya kohesi kuat antarmolekul air (ikatan hidrogen) dan adhesi air pada dinding hidrofilik trakea/trakeid xilem.",
        "distractors": [
            "Tekanan akar yang memompa air secara aktif dari korteks ke pucuk pohon dengan tekanan hidrostatik 100 atm.",
            "Aktivitas pompa natrium kalium pada sel parenkim spons yang mendorong molekul air ke atas.",
            "Gaya gravitasi bumi yang membalikkan arah aliran air tanah menjadi bertekanan positif ke atas.",
            "Kavitasi dan embolisme udara yang memecah pembuluh xilem menjadi saluran vakum termal."
        ],
        "formula": {
            "title": "TEORI KOHESI-TEGANGAN DIXON & JOLY",
            "latex": "\\Psi_{\\text{tanah}} (-0{,}3\\text{ MPa}) > \\Psi_{\\text{akar}} (-0{,}6\\text{ MPa}) > \\Psi_{\\text{batang}} (-0{,}8\\text{ MPa}) > \\Psi_{\\text{daun}} (-1{,}5\\text{ MPa}) > \\Psi_{\\text{atmosfer}} (-100\\text{ MPa})",
            "legend": "• Gradien potensial air ($\Psi_w$) yang menurun secara kontinu dari tanah ke udara atmosfer<br>• Kohesi ikatan hidrogen air memiliki kekuatan tarik (tensile strength) $> 20\\text{ MPa}$ mencegah putusnya benang air<br>• Tanpa memerlukan pengeluaran energi metabolik ATP langsung oleh tumbuhan"
        },
        "hints": {
            "concept": "Air ditarik ke atas oleh tarikan transpirasi daun (tegangan negatif) yang merambat sepanjang benang air kontinu berkat gaya kohesi (ikatan hidrogen sesama air) dan adhesi (ke dinding xilem).",
            "execution": "Pilih tarikan transpirasi (tegangan negatif) didukung kohesi ikatan hidrogen dan adhesi dinding xilem."
        }
    },
    {
        "id": "bio-sim-16",
        "materi": "FOTOPERIODISME & FITOKROM",
        "topic": "Peran Fitokrom Pr dan Pfr pada Pembungaan Tumbuhan Hari Pendek",
        "stem": "Fotoperiodisme tumbuhan dalam mengatur waktu pembungaan dikendalikan oleh pigmen fotoreseptor fitokrom yang memiliki dua bentuk konversi fotokimia: $P_r$ (menyerap cahaya merah $660\\text{ nm}$) dan $P_{fr}$ (menyerap cahaya merah jauh $730\\text{ nm}$). Pada tanaman hari pendek ($\\textit{Short-Day Plants / SDP}$ seperti krisan dan dahlia), faktor lingkungan kritis yang memicu terjadinya induksi pembungaan adalah...",
        "correct": "Panjang periode kegelapan malam hari yang kontinu (tak terputus) harus melampaui batas periode kritis; penyinaran sekejap dengan cahaya merah ($\\textit{night break}$) di tengah malam akan mengubah $P_r$ menjadi $P_{fr}$ yang bertindak sebagai inhibitor pembungaan pada tanaman hari pendek.",
        "distractors": [
            "Panjang siang hari harus minimal 18 jam dengan intensitas cahaya ultraviolet maksimum.",
            "Tanaman harus disiram dengan air es bersuhu nol derajat selama fase pembungaan.",
            "Kandungan hormon auksin pada pucuk apikal harus dinaikkan sepuluh kali lipat melampaui giberelin.",
            "Tanaman harus disimpan di dalam ruangan tanpa udara selama tiga hari berturut-turut."
        ],
        "formula": {
            "title": "FOTOKONVERSI FITOKROM & FOTOPERIODISME",
            "latex": "P_r \\ (\\text{Bentuk Inaktif, } 660\\text{ nm}) \\xrightleftharpoons[\\text{Merah Jauh (730 nm) / Gelap Lambat}]{\\text{Cahaya Merah (660 nm)}} P_{fr} \\ (\\text{Bentuk Aktif, } 730\\text{ nm})",
            "legend": "• Tanaman Hari Pendek (SDP) sebenarnya adalah 'Tanaman Malam Panjang'<br>• $P_{fr}$ menghambat pembungaan pada SDP, tetapi merangsang pembungaan pada LDP (Tanaman Hari Panjang)<br>• Night break dengan kilatan cahaya merah membatalkan pembungaan SDP"
        },
        "hints": {
            "concept": "Tanaman hari pendek (SDP) sebenarnya membutuhkan malam panjang tak terputus. Kilatan cahaya di tengah malam (night break) mengubah Pr jadi Pfr yang menghambat pembungaan SDP.",
            "execution": "Pilih periode malam kontinu melampaui batas kritis, di mana flash cahaya merah malam hari menghambat pembungaan."
        }
    },
    {
        "id": "bio-sim-17",
        "materi": "EMBRIOLOGI & FERTILISASI",
        "topic": "Pencegahan Polispermi: Reaksi Cepat vs Reaksi Kortikal Lambat",
        "stem": "Untuk mencegah masuknya lebih dari satu sperma ke dalam sel telur (pencegahan polispermi yang dapat menyebabkan zigot poliploidi mematikan), oosit mamalia dan bulu babi mengaktifkan dua mekanisme pertahanan. Mekanisme blokade polispermi lambat ($\\textit{slow block to polyspermy}$) berlangsung melalui...",
        "correct": "Reaksi kortikal ($\\textit{cortical reaction}$); fusi sperma memicu gelombang pelepasan ion $\\text{Ca}^{2+}$ intraseluler yang menyebabkan eksositosis granula kortikal ke ruang perivitelin, memodifikasi reseptor zona pelusida (reaksi zona) dan mengeraskan membran fertilisasi sehingga sperma lain tidak dapat menembus.",
        "distractors": [
            "Depolarisasi listrik seketika dari $-70\\text{ mV}$ menjadi $+20\\text{ mV}$ akibat influks ion natrium (blokade cepat).",
            "Pelepasan gas hidrogen sulfida yang membunuh seluruh sperma di dalam tuba fallopi.",
            "Pembelahan meiosis II oosit yang melontarkan badan polar kedua ke luar ovarium.",
            "Penghancuran total sitoplasma oosit oleh enzim lisosom sel folikel korona radiata."
        ],
        "formula": {
            "title": "DUA TAHAP PENCEGAHAN POLISPERMI PADA FERTILISASI",
            "latex": "\\begin{aligned} \\text{Blokade Cepat (Fast Block):} & \\quad \\text{Depolarisasi Listrik Membran (Influks Na}^+\\text{, durasi 1 menit)} \\\\ \\text{Blokade Lambat (Slow Block):} & \\quad \\text{Gelombang Ca}^{2+} \\to \\text{Eksositosis Granula Kortikal} \\to \\text{Reaksi Zona/Pengerasan Membran Fertilisasi} \\end{aligned}",
            "legend": "• Pada mamalia, blokade cepat tidak teramati, mengandalkan reaksi zona kortikal lambat<br>• Enzim granula kortikal memotong reseptor ZP3/ZP2 pada zona pelusida<br>• Polispermi pada manusia bersifat letal (embrio triploid $69$ kromosom gagal berkembang)"
        },
        "hints": {
            "concept": "Blokade lambat polispermi adalah reaksi kortikal: gelombang ion Ca2+ memicu granula kortikal melepas enzim yang mengeraskan zona pelusida (reaksi zona) sehingga sperma lain terblokir.",
            "execution": "Pilih reaksi kortikal: pelepasan granula kortikal yang mengeraskan membran fertilisasi / zona pelusida."
        }
    },
    {
        "id": "bio-sim-18",
        "materi": "BIOTEKNOLOGI SEL PUNCA (STEM CELLS)",
        "topic": "Induksi Pluripotensi Sel Somatik (iPSCs) Menggunakan Faktor Yamanaka",
        "stem": "Penemuan sel punca pluripoten terinduksi ($\\textit{induced Pluripotent Stem Cells / iPSCs}$) oleh Shinya Yamanaka (2006) membuktikan bahwa sel somatik dewasa yang telah terdiferensiasi (seperti fibroblas kulit) dapat diprogram ulang kembali menjadi sel punca dengan kemampuan pluripoten mirip sel punca embrionik. Empat faktor transkripsi kunci ($\\textit{Yamanaka factors}$) yang dimasukkan untuk memicu dediferensiasi tersebut adalah...",
        "correct": "Oct3/4, Sox2, Klf4, dan c-Myc (faktor OSKM), yang bekerja secara sinergis mengaktifkan jaringan gen pluripotensi embrionik dan membungkam gen spesifik diferensiasi sel somatik melalui remodelling epigenetik global.",
        "distractors": [
            "Insulin, Glukagon, Adrenalin, dan Tiroksin yang memicu glikogenesis pada sel punca.",
            "DNA polimerase, RNA primase, Helikase, dan Ligase pembuat untai Okazaki.",
            "p53, Rb, CDK4, dan Siklin D yang memblokir siklus sel pada fase interfase G0.",
            "Amilase, Tripsin, Lipase, dan Pepsinogen pengurai dinding sel fibroblas."
        ],
        "formula": {
            "title": "FAKTOR REPROGRAMMING YAMANAKA (OSKM)",
            "latex": "\\text{Fibroblas Dewasa} + \\{ \\text{Oct4}, \\text{Sox2}, \\text{Klf4}, \\text{c-Myc} \\} \\xrightarrow{\\text{Remodelling Epigenetik}} \\text{iPSCs Pluripoten}",
            "legend": "• Dianugerahi Hadiah Nobel Fisiologi atau Kedokteran 2012<br>• Menghilangkan dilema etika destruksi embrio manusia pada terapi sel punca<br>• Sel iPSCs mampu berdiferensiasi menjadi ketiga lapisan germinal (ektoderm, mesoderm, endoderm)"
        },
        "hints": {
            "concept": "Empat faktor transkripsi Yamanaka (OSKM) adalah: Oct3/4, Sox2, Klf4, dan c-Myc.",
            "execution": "Pilih Oct3/4, Sox2, Klf4, dan c-Myc."
        }
    },
    {
        "id": "bio-sim-19",
        "materi": "GENETIKA FORENSIK & BIOINFORMATIKA",
        "topic": "DNA Profiling Menggunakan Lokus Short Tandem Repeats (STR)",
        "stem": "Dalam identifikasi forensik korban kecelakaan dan penentuan uji paternitas ayah kandung, metode baku emas yang digunakan secara global adalah analisis DNA Profiling berbasis lokus Short Tandem Repeats (STR). Keunggulan ilmiah penanda molekuler STR dibandingkan penanda gen fungsional biasa adalah...",
        "correct": "Lokus STR terletak pada daerah non-coding DNA dengan tingkat polimorfisme variasi jumlah pengulangan unit basa ($2-6\\text{ bp}$) yang sangat tinggi antar-individu dalam populasi, diwariskan secara kodominan menurut hukum Mendel, dan memiliki laju amplifikasi PCR yang stabil bahkan dari sampel DNA yang terdegradasi.",
        "distractors": [
            "Lokus STR mengkode antibodi pelindung terhadap racun arsenik di sumsum tulang belakang.",
            "Lokus STR selalu memiliki urutan basa nukleotida yang identik persis pada seluruh umat manusia di bumi.",
            "Lokus STR hanya dapat ditemukan pada kromosom kelamin Y pria dan tidak ada pada wanita.",
            "Lokus STR bermutasi setiap hari menghasilkan jutaan jenis golongan darah baru."
        ],
        "formula": {
            "title": "PRINSIP PROFILING LOKUS STR FORENSIK (CODIS)",
            "latex": "\\text{Genotipe STR: Jumlah Pengulangan Alel (misal D13S317: } [\\text{TATC}]_8 / [\\text{TATC}]_{12}\\text{)} \\implies P_{\\text{cocok acak}} < 10^{-15}",
            "legend": "• Sistem FBI CODIS menggunakan 20 lokus STR independen standar<br>• Probabilitas kecocokan dua individu acak bukan kembar identik mendekati 1 banding 1 triliun<br>• Deteksi ukuran fragmen menggunakan elektroforesis kapiler dengan fluoresensi"
        },
        "hints": {
            "concept": "STR adalah pengulangan unit pendek (2-6 bp) pada daerah non-coding DNA. Polimorfismenya sangat tinggi (jumlah repetisinya bervariasi antarindividu), stabil diamplifikasi PCR, dan diwariskan menurut hukum Mendel.",
            "execution": "Pilih lokus STR di daerah non-coding dengan polimorfisme jumlah pengulangan sangat tinggi dan stabil diamplifikasi PCR."
        }
    },
    {
        "id": "bio-sim-20",
        "materi": "EKOLOGI KOMUNITAS (SPESIES KUNCI)",
        "topic": "Eksperimen Robert Paine: Peran Bintang Laut Pisaster ochraceus",
        "stem": "Dalam studi ekologi komunitas laut intertidal berbatu, ekolog Robert Paine menghilangkan seluruh populasi bintang laut predator $\\textit{Pisaster ochraceus}$ dari zona eksperimen. Dampak ekologis dramatis yang teramati setelah pengeluaran spesies bintang laut tersebut adalah...",
        "correct": "Terjadi keruntuhan keanekaragaman hayati komunitas; populasi kerang remis $\\textit{Mytilus californianus}$ (mangsa utama) meledak dan memonopoli seluruh ruang permukaan batu intertidal, menyingkirkan spesies teritip, alga, dan siput laut lainnya hingga keanekaragaman spesies anjlok dari 15 spesies menjadi hanya 1 spesies tunggal.",
        "distractors": [
            "Seluruh populasi kerang remis punah seketika akibat kehabisan mangsa bintang laut.",
            "Terumbu karang tumbuh subur menutupi pantai intertidal membentuk atol raksasa.",
            "Air laut di perairan tersebut berubah menjadi tawar akibat penghentian siklus garam.",
            "Semua alga laut berevolusi menjadi tanaman mangrove berakar napas."
        ],
        "formula": {
            "title": "KONSEP SPESIES KUNCI (KEYSTONE SPECIES) ROBERT PAINE",
            "latex": "\\text{Keberadaan Predator Kunci } (\\textit{Pisaster}) \\implies \\text{Kontrol Kompetitor Dominan } (\\textit{Mytilus}) \\implies \\text{Diversitas Komunitas Terjaga}",
            "legend": "• Spesies kunci (Keystone Species): Spesies dengan pengaruh ekologis disproporsional besar terhadap komunitas relatif terhadap kelimpahan biomassa dasarnya<br>• Mencegah eksklusi kompetitif (competitive exclusion) oleh kompetitor superior<br>• Bukti pentingnya predator puncak dalam pelestarian biodiversitas"
        },
        "hints": {
            "concept": "Bintang laut Pisaster adalah spesies kunci. Ketika diambil, mangsa utamanya (kerang Mytilus) meledak populasinya dan memonopoli ruang batu, menyingkirkan spesies lain sehingga keanekaragaman hayati anjlok.",
            "execution": "Pilih meledaknya populasi kerang Mytilus yang memonopoli ruang dan meruntuhkan keanekaragaman hayati."
        }
    },
    {
        "id": "bio-sim-21",
        "materi": "SIKLUS BIOGEOKIMIA (SIKLUS NITROGEN)",
        "topic": "Peran Mikroorganisme Tanah pada Nitrifikasi dan Denitrifikasi",
        "stem": "Dalam siklus biogeokimia nitrogen di dalam tanah, senyawa amonium ($\\text{NH}_4^+$) hasil dekomposisi diubah menjadi bentuk nitrat ($\\text{NO}_3^-$) yang mudah diserap oleh akar tumbuhan, dan sebagian dikembalikan ke atmosfer sebagai gas $\\text{N}_2$. Urutan mikroorganisme tanah yang terlibat dalam proses nitrifikasi tahap 1, nitrifikasi tahap 2, dan denitrifikasi berturut-turut adalah...",
        "correct": "$\\textit{Nitrosomonas}$ (mengoksidasi $\\text{NH}_4^+$ menjadi $\\text{NO}_2^-$), $\\textit{Nitrobacter}$ (mengoksidasi $\\text{NO}_2^-$ menjadi $\\text{NO}_3^-$), dan $\\textit{Pseudomonas denitrificans}$ (mereduksi $\\text{NO}_3^-$ menjadi gas $\\text{N}_2$ dalam kondisi anaerob).",
        "distractors": [
            "$\\textit{Rhizobium}$ (menghasilkan urea), $\\textit{Azotobacter}$ (memecah nitrit), dan $\\textit{Escherichia coli}$ (membakar amonia).",
            "$\\textit{Lactobacillus}$ (membuat amonium), $\\textit{Streptococcus}$ (mengoksidasi nitrat), dan $\\textit{Clostridium}$ (menyerap sulfur).",
            "$\\textit{Saccharomyces}$ (mengikat N2), $\\textit{Aspergillus}$ (membuat amonium), dan $\\textit{Bacillus thuringiensis}$ (mereduksi fosfat).",
            "$\\textit{Nitrobacter}$ (membuat amonia), $\\textit{Nitrosomonas}$ (membuat gas N2), dan $\\textit{Methanobacterium}$ (membentuk asam cuka)."
        ],
        "formula": {
            "title": "REAKSI BIOKIMIA SIKLUS NITROGEN TANAH",
            "latex": "\\begin{aligned} \\text{Nitritasi:} & \\quad 2\\text{NH}_4^+ + 3\\text{O}_2 \\xrightarrow{\\textit{Nitrosomonas}} 2\\text{NO}_2^- + 4\\text{H}^+ + 2\\text{H}_2\\text{O} \\\\ \\text{Nitratasi:} & \\quad 2\\text{NO}_2^- + \\text{O}_2 \\xrightarrow{\\textit{Nitrobacter}} 2\\text{NO}_3^- \\\\ \\text{Denitrifikasi:} & \\quad 2\\text{NO}_3^- \\xrightarrow{\\textit{Pseudomonas}} 2\\text{NO}_2^- \\to 2\\text{NO} \\to \\text{N}_2\\text{O} \\to \\text{N}_2(g) \\end{aligned}",
            "legend": "• Nitrifikasi adalah proses kemosintesis aerobik obligat<br>• Denitrifikasi adalah proses respirasi anaerobik bakteri pereduksi nitrat pada tanah becek tergenang air<br>• Fiksasi biologis dilakukan oleh $\\textit{Rhizobium}$ (simbiosis) dan $\\textit{Azotobacter}$ (hidup bebas)"
        },
        "hints": {
            "concept": "Nitrifikasi 1 (amonium -> nitrit) oleh Nitrosomonas. Nitrifikasi 2 (nitrit -> nitrat) oleh Nitrobacter. Denitrifikasi (nitrat -> gas N2) oleh Pseudomonas denitrificans.",
            "execution": "Pilih urutan Nitrosomonas -> Nitrobacter -> Pseudomonas denitrificans."
        }
    },
    {
        "id": "bio-sim-22",
        "materi": "MEKANISME SELEKSI ALAM POPULASI",
        "topic": "Seleksi Terarah, Penstabilan, dan Pemecah (Disruptive Selection)",
        "stem": "Dalam suatu populasi burung pemakan biji-bijian di kepulauan terpencil, biji tanaman yang tersedia di habitat mengalami diferensiasi ekstrem: hanya tersedia biji berukuran sangat lunak dan kecil, serta biji berukuran sangat keras dan besar; biji berukuran sedang lenyap akibat kekeringan. Seleksi alam yang terjadi menyebabkan burung berparuh kecil dan burung berparuh besar mampu bertahan hidup dengan efisien, sedangkan burung berparuh sedang terseleksi negatif dan berkurang drastis. Bentuk seleksi alam ini diklasifikasikan sebagai...",
        "correct": "Seleksi pemecah ($\\textit{disruptive / diversifying selection}$), di mana tekanan lingkungan menguntungkan kedua fenotipe ekstrem pada kedua ujung kurva distribusi dan menyeleksi terhadap fenotipe rata-rata intermediet.",
        "distractors": [
            "Seleksi penstabilan ($\\textit{stabilizing selection}$), yang menguntungkan fenotipe rata-rata dan menyeleksi kedua fenotipe ekstrem.",
            "Seleksi terarah ($\\textit{directional selection}$), yang menggeser seluruh kurva distribusi ke arah salah satu fenotipe ekstrem saja.",
            "Seleksi seksual intraspesifik, yang hanya dipengaruhi oleh perkelahian fisik antarpejantan burung.",
            "Seleksi artifisial domestikasi, yang sengaja dirancang oleh pemulia tanaman pangan komersial."
        ],
        "formula": {
            "title": "TIGA RAGAM UTAMA SELEKSI ALAM PADA POPULASI",
            "latex": "\\begin{aligned} \\text{Stabilizing:} & \\quad \\text{Varian Ekstrem Tersingkir} \\implies \\text{Puncak Rata-rata Menyempit} \\\\ \\text{Directional:} & \\quad \\text{Satu Varian Ekstrem Diuntungkan} \\implies \\text{Kurva Bergeser ke Satu Arah} \\\\ \\text{Disruptive:} & \\quad \\text{Kedua Varian Ekstrem Diuntungkan} \\implies \\text{Terbentuk 2 Puncak Kurva (Bimodal)} \\end{aligned}",
            "legend": "• Disruptive selection dapat menjadi pemicu awal terjadinya spesiasi simpatrik<br>• Menghasilkan polimorfisme stabil dalam populasi alami<br>• Teramati nyata pada burung finch pemecah biji Afrika ($\\textit{Pyrenestes ostrinus}$)"
        },
        "hints": {
            "concept": "Kedua fenotipe ekstrem (kecil dan besar) diuntungkan sementara fenotipe sedang/rata-rata tersingkir. Ini disebut seleksi pemecah (disruptive selection).",
            "execution": "Pilih seleksi pemecah (disruptive / diversifying selection)."
        }
    },
    {
        "id": "bio-sim-23",
        "materi": "TEORI ENDOSIMBIOSIS (EVOLUSI SEL)",
        "topic": "Bukti Biokimia dan Sitologis Asal-Usul Mitokondria dan Kloroplas",
        "stem": "Teori Endosimbiosis Serial ($\\textit{Serial Endosymbiosis Theory}$) yang dipopulerkan oleh Lynn Margulis menyatakan bahwa mitokondria dan kloroplas berevolusi dari prokariota aerobik dan sianobakteri fotosintetik yang ditelan oleh sel eukariota primitif. Bukti molekuler dan struktural yang paling meyakinkan yang mendukung teori endosimbiosis tersebut adalah...",
        "correct": "Mitokondria dan kloroplas memiliki molekul DNA sirkular ganda telanjang (tanpa histon) seperti bakteri, memiliki ribosom tipe 70S yang rentan terhadap antibiotik antibakteri, membelah diri secara biner ($\\textit{binary fission}$) independen dari siklus sel inang, serta memiliki membran ganda di mana membran dalamnya memiliki komposisi lipid kardiolipin khas membran bakteri.",
        "distractors": [
            "Keduanya memiliki dinding selulosa tebal dan mampu melakukan pembelahan reduksi meiosis empat tahap.",
            "Keduanya menghasilkan spora aseksual bertudung protein seperti cendawan basidiomycota.",
            "Keduanya memiliki retikulum endoplasma dan badan Golgi internal tersendiri di dalam matriksnya.",
            "Keduanya dapat bermutasi menjadi virus bakteriofag jika sel inang mengalami dehidrasi."
        ],
        "formula": {
            "title": "BUKTI EVOLUSIONER TEORI ENDOSIMBIOSIS SERIAL",
            "latex": "\\text{Prokariot Bebas} \\xrightarrow{\\text{Endositosis Tanpa Digesti}} \\text{Simbiosis Mutualisme Obligat} \\implies \\text{Organel Eukariotik Berkelanjutan}",
            "legend": "• Filogeni gen 16S rRNA menempatkan mitokondria di kelompok $\\alpha\\text{-proteobacteria}$<br>• Kloroplas berkerabat terdekat dengan sianobakteri $\\textit{Prochloron}$<br>• Membran luar berasal dari vakuola fagosom sel inang, membran dalam dari bakteri endosimbion"
        },
        "hints": {
            "concept": "Bukti endosimbiosis: DNA sirkular mirip bakteri, ribosom 70S, pembelahan biner mandiri, membran ganda, dan membran dalam mengandung kardiolipin.",
            "execution": "Pilih DNA sirkular tanpa histon, ribosom 70S, pembelahan biner, dan membran dalam berlipid kardiolipin."
        }
    },
    {
        "id": "bio-sim-24",
        "materi": "FISIOLOGI PENCERNAAN & ABSORPSI LIPID",
        "topic": "Pembentukan Misel dan Jalur Kilomikron pada Pembuluh Lakteal",
        "stem": "Proses penyerapan hasil pencernaan lemak (asam lemak rantai panjang dan 2-monogliserida) di usus halus berbeda dari jalur penyerapan glukosa dan asam amino. Setelah diresorpsi ke dalam sitosol enterosit, jalur perakitan dan transportasi molekul lipid menuju sirkulasi sistemik adalah...",
        "correct": "Asam lemak rantai panjang disintesis ulang menjadi trigliserida di retikulum endoplasma halus, dikemas bersama kolesterol, fosfolipid, dan apolipoprotein B-48 membentuk partikel lipoprotein kilomikron, kemudian disekresikan via eksositosis ke pembuluh kil (lakteal) sistem limfatik sebelum masuk ke vena subklavia sinistra melalui duktus torasikus.",
        "distractors": [
            "Asam lemak langsung berdifusi masuk ke kapiler darah porta hepatika menuju organ hati tanpa membentuk lipoprotein.",
            "Trigliserida dipecah menjadi gas karbon dioksida di dalam inti sel enterosit dan diekskresikan lewat alveolus.",
            "Misel empedu menembus membran basolateral secara utuh dan mengalir ke ginjal untuk disaring menjadi urin primer.",
            "Asam lemak diikat oleh molekul hemoglobin eritrosit untuk dibakar menjadi energi panas di limpa."
        ],
        "formula": {
            "title": "JALUR PENYERAPAN LIPID MAKANAN (KILOMIKRON)",
            "latex": "\\text{Misel Lumen} \\to \\text{Difusi ke Enterosit} \\xrightarrow{\\text{RE Halus}} \\text{Trigliserida} \\xrightarrow{\\text{Golgi}} \\text{Kilomikron} \\xrightarrow{\\text{Eksositosis}} \\text{Pembuluh Lakteal} \\to \\text{Duktus Torasikus} \\to \\text{Darah}",
            "legend": "• Asam lemak rantai pendek/sedang ($< 12\\text{C}$) dapat langsung masuk kapiler vena porta<br>• Pembuluh lakteal mengalirkan cairan limfa berwarna putih susu ($\\textit{chyle}$)<br>• Enzim Lipoprotein Lipase (LPL) di kapiler jaringan memecah kilomikron melepas asam lemak ke adiposit/otot"
        },
        "hints": {
            "concept": "Lemak disintesis ulang jadi trigliserida di RE halus, dikemas jadi kilomikron, lalu dieksositosis ke pembuluh kil/lakteal (sistem limfatik) -> duktus torasikus -> vena subklavia.",
            "execution": "Pilih pembentukan kilomikron di enterosit dan eksositosis ke pembuluh lakteal (sistem limfatik)."
        }
    },
    {
        "id": "bio-sim-25",
        "materi": "TERMOREGULASI & JARINGAN ADIPOSA COKELAT",
        "topic": "Termogenesis Tanpa Menggigil Melalui Protein Uncoupling UCP-1",
        "stem": "Bayi baru lahir dan mamalia yang berhibernasi memiliki cadangan jaringan lemak cokelat ($\\textit{Brown Adipose Tissue / BAT}$) yang melimpah untuk mempertahankan suhu tubuh tanpa menggigil ($\\textit{non-shivering thermogenesis}$). Mekanisme molekuler yang memungkinkan jaringan lemak cokelat membakar bahan bakar lipid secara murni menghasilkan panas adalah...",
        "correct": "Membran dalam mitokondria sel lemak cokelat mengekspresikan protein uncoupling UCP-1 (termogenin) berkonsentrasi tinggi yang memintas aliran proton kembali ke matriks tanpa melalui ATP Sintase, mendisipasi gradien elektrokimia proton secara langsung menjadi energi termal murni.",
        "distractors": [
            "Sel lemak cokelat memecah molekul kalsium karbonat secara pembakaran api terbuka di dalam vakuola.",
            "Mitochondria memutar balik enzim Rubisco untuk memfiksasi gas karbon dioksida di dalam aliran darah.",
            "Jaringan lemak cokelat bergetar secara mekanik dengan frekuensi ultrasound membakar selulosa kulit.",
            "Terjadi reaksi fusi nuklir hidrogen pada tetesan lipid sitoplasma sel adiposa cokelat."
        ],
        "formula": {
            "title": "MEKANISME TERMOGENIN (UCP-1) PADA MITOKONDRIA BAT",
            "latex": "\\text{Aktivasi } \\beta_3\\text{-Adrenergik} \\implies \\text{Lipolisis} \\implies \\text{Asam Lemak Mengaktifkan UCP-1} \\implies \\text{Bocornya Gradien H}^+ \\implies \\text{Disipasi Panas 100\\%}",
            "legend": "• Warna cokelat disebabkan oleh tingginya kepadatan mitokondria berpigmen sitokrom besi<br>• Normalnya kemiosmosis menghasilkan $ATP$; UCP-1 memutus hubungan (uncoupling) respirasi dari fosforilasi<br>• Perlindungan vital bagi bayi yang belum memiliki refleks menggigil otot rangka yang matang"
        },
        "hints": {
            "concept": "Lemak cokelat (BAT) memiliki protein UCP-1 (termogenin) di membran dalam mitokondria. UCP-1 membocorkan gradien H+ kembali ke matriks tanpa lewat ATP sintase, sehingga 100% energi disipasi menjadi panas.",
            "execution": "Pilih ekspresi protein uncoupling UCP-1 (termogenin) yang memintas gradien proton menjadi energi termal murni."
        }
    },

    # -------------------------------------------------------------
    # 5 COMPLEX MULTI-SELECT HOTS (bio-sim-26 to bio-sim-30)
    # -------------------------------------------------------------
    {
        "id": "bio-sim-26",
        "type": "multi",
        "materi": "FOTOSINTESIS (REAKSI TERANG)",
        "topic": "Karakteristik Fotofosforilasi Nonsiklik vs Siklik pada Kloroplas",
        "stem": "Reaksi terang fotosintesis pada membran tilakoid kloroplas dapat berlangsung melalui jalur fotofosforilasi nonsiklik dan fotofosforilasi siklik. Manakah TIGA pernyataan berikut yang merupakan karakteristik khas dari jalur fotofosforilasi nonsiklik? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Melibatkan kerja sama terkoordinasi antara Fotosistem II ($P_{680}$) dan Fotosistem I ($P_{700}$) secara berurutan."},
            {"key": "B", "text": "Menghasilkan molekul ATP, molekul NADPH, dan melepaskan gas oksigen ($\\text{O}_2$) hasil fotolisis air."},
            {"key": "C", "text": "Terjadi aliran elektron searah (unidirectional) dari molekul pendonor air ($\\text{H}_2\\text{O}$) hingga diterima oleh akseptor terakhir $\\text{NADP}^+$."},
            {"key": "D", "text": "Hanya melibatkan Fotosistem I ($P_{700}$) saja tanpa pernah menghasilkan gas oksigen maupun molekul NADPH."},
            {"key": "E", "text": "Elektron berenergi tinggi yang dieksitasi dari pusat reaksi akan kembali berputar ke fotosistem yang sama."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "PERBANDINGAN FOTOFOSFORILASI NONSIKLIK VS SIKLIK",
            "latex": "\\begin{aligned} \\text{Nonsiklik (Skema Z):} & \\quad \\text{PS II} \\to \\text{Sitokrom } b_6f \\to \\text{PS I} \\to \\text{NADP}^+ \\implies \\text{ATP} + \\text{NADPH} + \\text{O}_2 \\\\ \\text{Siklik:} & \\quad \\text{PS I} \\to \\text{Ferredoksin} \\to \\text{Sitokrom } b_6f \\to \\text{PS I} \\implies \\text{Hanya ATP} \\end{aligned}",
            "legend": "• A, B, C BENAR: Definisi dan produk lengkap fotofosforilasi nonsiklik (Z-scheme)<br>• D dan E SALAH: Merupakan karakteristik fotofosforilasi siklik (hanya PS I, siklus elektron tertutup, hanya hasilkan ATP untuk kebutuhan ekstra Siklus Calvin)"
        },
        "hints": {
            "concept": "Fotofosforilasi nonsiklik melibatkan PS II & PS I, ada fotolisis air menghasilkan O2, dan menghasilkan ATP serta NADPH. Fotofosforilasi siklik hanya melibatkan PS I dan hanya menghasilkan ATP.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "bio-sim-27",
        "type": "multi",
        "materi": "EVOLUSI SEL & ENDOSIMBIOSIS",
        "topic": "Bukti Ilmiah Teori Endosimbiosis Mitokondria dan Kloroplas",
        "stem": "Teori Endosimbiosis Serial Lynn Margulis didukung oleh serangkaian bukti ilmiah sitologis, biokimia, dan genetika molekuler yang kuat. Manakah TIGA fakta ilmiah berikut yang membuktikan bahwa mitokondria dan kloroplas berevolusi dari organisme prokariota purba? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Keduanya memiliki materi genetik mandiri berupa molekul DNA sirkular ganda telanjang tanpa ikatan protein histon, mirip kromosom bakteri."},
            {"key": "B", "text": "Keduanya memiliki ribosom tipe 70S yang peka terhadap antibiotik penghambat sintesis protein bakteri (seperti kloramfenikol), bukan ribosom 80S eukariotik."},
            {"key": "C", "text": "Keduanya memperbanyak diri di dalam sel melalui mekanisme pembelahan biner ($\\textit{binary fission}$) yang menyerupai cara pembelahan bakteri."},
            {"key": "D", "text": "Keduanya memiliki dinding selulosa kaku berlapis lignin yang tidak dapat ditembus oleh molekul air."},
            {"key": "E", "text": "Keduanya mampu hidup mandiri di luar sel inang dalam media kultur garam anorganik tanpa enzim apapun."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "BUKTI UTAMA TEORI ENDOSIMBIOSIS SERIAL",
            "latex": "\\text{Organel Eukariotik} \\equiv \\text{Prokariot Simbion} \\implies \\text{DNA Sirkular} + \\text{Ribosom 70S} + \\text{Pembelahan Biner}",
            "legend": "• A BENAR: DNA sirkular prokariotik<br>• B BENAR: Ribosom 70S (subunit 50S + 30S)<br>• C BENAR: Pembelahan biner independen<br>• D dan E SALAH: Mitokondria/kloroplas tidak berdinding selulosa dan gen-gen esensialnya telah berpindah ke nukleus sehingga menjadi endosimbion obligat"
        },
        "hints": {
            "concept": "Tiga bukti endosimbiosis utama: DNA sirkular tanpa histon (A), ribosom tipe prokariot 70S (B), dan pembelahan biner mandiri (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "bio-sim-28",
        "type": "multi",
        "materi": "FISIOLOGI RESPIRASI MANUSIA",
        "topic": "Faktor-Faktor yang Menggeser Kurva Oksihemoglobin ke Kanan (Efek Bohr)",
        "stem": "Efek Bohr memfasilitasi pelepasan oksigen dari oksihemoglobin di jaringan kapiler organ tubuh yang sedang aktif bermetabolisme. Manakah TIGA kondisi fisiologis berikut yang secara langsung menyebabkan pergeseran kurva disosiasi oksihemoglobin ke arah kanan? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Penurunan nilai pH plasma darah (peningkatan konsentrasi ion hidrogen $[\\text{H}^+]$ / suasana asidosis metabolik)."},
            {"key": "B", "text": "Peningkatan tekanan parsial gas karbon dioksida ($P_{\\text{CO}_2}$) di dalam kapiler jaringan."},
            {"key": "C", "text": "Peningkatan suhu jaringan tubuh lokal (misalnya selama aktivitas olahraga berat atau demam tinggi)."},
            {"key": "D", "text": "Penurunan konsentrasi molekul alosterik 2,3-bisfosfogliserat (2,3-BPG) di dalam eritrosit hingga mendekati nol."},
            {"key": "E", "text": "Penurunan tekanan parsial gas karbon dioksida disertai penurunan suhu jaringan hingga mendekati titik beku."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "REGULASI PERGESERAN KURVA OKSIDISIASI HEMOGLOBIN",
            "latex": "\\text{Pergeseran Kanan (Afinitas Turun, Lepas O}_2\\text{)}: \\quad \\text{pH} \\downarrow, \\ P_{\\text{CO}_2} \\uparrow, \\ T \\uparrow, \\ \\text{2,3-BPG} \\uparrow",
            "legend": "• A, B, C BENAR: Ketiganya merupakan kondisi khas jaringan aktif yang menstabilkan bentuk deoksihemoglobin (T-state)<br>• D dan E SALAH: Penurunan 2,3-BPG, penurunan $P_{\\text{CO}_2}$, dan penurunan suhu justru menggeser kurva ke KIRI (afinitas $\\text{O}_2$ naik, seperti pada hemoglobin fetus HbF)"
        },
        "hints": {
            "concept": "Kurva geser kanan (afinitas O2 turun, O2 mudah lepas): pH turun (asam), CO2 naik, Suhu naik, 2,3-BPG naik.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "bio-sim-29",
        "type": "multi",
        "materi": "SISTEM IMUNITAS BAWAAN (INNATE IMMUNITY)",
        "topic": "Komponen Pertahanan Imun Non-Spesifik Lini Pertama dan Kedua",
        "stem": "Sistem kekebalan bawaan ($\\textit{innate immunity}$) memberikan respons pertahanan garis depan yang cepat dan non-spesifik terhadap invasi patogen. Manakah TIGA komponen atau mekanisme berikut yang termasuk ke dalam sistem imunitas bawaan (non-spesifik) tubuh manusia? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Rintangan fisik dan kimiawi permukaan tubuh, seperti lapisan keratin epidermis kulit, asam lambung (HCl), dan enzim lisozim pada air mata."},
            {"key": "B", "text": "Aktivitas sel fagositik (neutrofil, monosit, dan makrofag jaringan) yang menelan dan mencerna mikroorganisme patogen."},
            {"key": "C", "text": "Sel pembunuh alami ($\\textit{Natural Killer / NK cells}$) yang mendeteksi dan melisiskan sel tumor atau sel terinfeksi virus yang kehilangan ekspresi MHC Kelas I."},
            {"key": "D", "text": "Produksi antibodi imunoglobulin G (IgG) berafinitas tinggi oleh sel plasma hasil klonal seleksi limfosit B."},
            {"key": "E", "text": "Pembentukan sel T memori spesifik antigen yang bertahan hidup puluhan tahun pasca vaksinasi."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "ARSITEKTUR SISTEM IMUNITAS MANUSIA",
            "latex": "\\begin{aligned} \\text{Imunitas Bawaan (Non-spesifik):} & \\quad \\text{Lini 1 (Kulit, Mukosa, Lisozim)} + \\text{Lini 2 (Fagosit, NK Cells, Komplemen, Inflamasi)} \\\\ \\text{Imunitas Adaptif (Spesifik):} & \\quad \\text{Lini 3 (Sel B/Antibodi, Sel T Sitotoksik/Helper, Sel Memori)} \\end{aligned}",
            "legend": "• A, B, C BENAR: Merupakan pilar imunitas bawaan (respon instan hitungan jam tanpa memori antigen)<br>• D dan E SALAH: Merupakan cabang imunitas adaptif / didapat (spesifik dan memiliki memori)"
        },
        "hints": {
            "concept": "Imunitas bawaan (non-spesifik): barrier fisik/kimia (A), sel fagosit neutrofil/makrofag (B), dan Natural Killer cells (C). Antibodi dan sel memori termasuk imunitas adaptif (spesifik).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "bio-sim-30",
        "type": "multi",
        "materi": "GENETIKA HEREDITAS MANUSIA",
        "topic": "Pola Karakteristik Kelainan Genetik Resesif Terpaut Kromosom X",
        "stem": "Penyakit genetik resesif terpaut kromosom X (seperti hemofilia A dan buta warna merah-hijau) memiliki pola silsilah keluarga ($\\textit{pedigree}$) yang khas. Manakah TIGA pernyataan berikut yang secara ilmiah BENAR mengenai pola pewarisan sifat resesif terpaut kromosom X? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Frekuensi kemunculan penyakit pada laki-laki jauh lebih tinggi daripada perempuan karena laki-laki bersifat hemizigotik ($X^h Y$) dan hanya membutuhkan satu salinan alel resesif untuk berekspresi."},
            {"key": "B", "text": "Seorang ayah yang menderita kelainan ($X^h Y$) TIDAK AKAN PERNAH mewariskan alel penyakit tersebut kepada anak laki-lakinya, karena ayah selalu mewariskan kromosom Y kepada anak laki-laki."},
            {"key": "C", "text": "Semua anak perempuan dari seorang ayah yang menderita kelainan ($X^h Y$) dipastikan akan menjadi pembawa sifat ($\\textit{carrier}$, $X^H X^h$) jika ibunya normal homozigot."},
            {"key": "D", "text": "Penyakit diwariskan secara langsung dari ayah penderita ke seluruh anak laki-lakinya secara eksklusif."},
            {"key": "E", "text": "Seorang wanita penderita hemofilia dapat lahir dari pasangan ibu normal non-carrier dan ayah normal murni."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "HUKUM PEWARISAN TERPAUT KROMOSOM X RESESIF",
            "latex": "\\text{Ayah } X^h Y \\implies \\begin{cases} \\text{Kepada Seluruh Anak Laki-laki } (Y): & 0\\% \\text{ Tertular dari Ayah} \\\\ \\text{Kepada Seluruh Anak Perempuan } (X^h): & 100\\% \\text{ Menjadi Carrier } (X^H X^h) \\end{cases}",
            "legend": "• Pola pewarisan bersilang (criss-cross inheritance): Kakek penderita mewariskan ke cucu laki-laki via anak perempuan carrier<br>• A, B, C BENAR: Sesuai hukum transmisi kromosom seks kelamin<br>• D SALAH: Pewarisan ayah ke anak laki-laki hanya untuk gen terpaut Y (holandrik)"
        },
        "hints": {
            "concept": "Pewarisan terpaut X: laki-laki lebih sering terkena karena hemizigot (A). Ayah mewariskan Y ke anak laki-laki sehingga tidak menularkan alel Xh ke anak laki-laki (B). Ayah mewariskan Xh ke semua anak perempuannya (C).",
            "execution": "Pilih A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH HOTS (bio-sim-31 to bio-sim-35)
    # -------------------------------------------------------------
    {
        "id": "bio-sim-31",
        "type": "matrix",
        "materi": "RESPIRASI SELULER & BIOENERGETIKA",
        "topic": "Tahapan Katabolisme Glukosa dan Neraca Energi ATP",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai metabolisme katabolisme respirasi seluler aerob dan anaerob!",
        "statements": [
            {
                "text": "Glikolisis berlangsung di dalam sitosol sel dan tidak membutuhkan keberadaan gas oksigen secara langsung.",
                "correct": True
            },
            {
                "text": "Siklus Asam Sitrat (Krebs) melepaskan seluruh enam atom karbon dari satu molekul glukosa awal dalam bentuk gas CO2.",
                "correct": False
            },
            {
                "text": "Oksigen molekuler (O2) bertindak sebagai akseptor elektron terakhir pada Rantai Transpor Elektron mitokondria membentuk molekul air (H2O).",
                "correct": True
            },
            {
                "text": "Fermentasi asam laktat menghasilkan total 36 ATP netto per molekul glukosa melalui kemiosmosis mitokondria.",
                "correct": False
            }
        ],
        "formula": {
            "title": "NERACA BIOENERGETIKA RESPIRASI AEROB",
            "latex": "\\text{Glikolisis (Sitosol)} \\to \\text{DO Piruvat (2 CO}_2\\text{)} \\to \\text{Siklus Krebs (4 CO}_2\\text{)} \\to \\text{Kemiosmosis (O}_2 \\to \\text{H}_2\\text{O)}",
            "legend": "• Pernyataan 1 BENAR: Glikolisis adalah jalur universal anaerob sitosol<br>• Pernyataan 2 SALAH: Siklus Krebs hanya melepaskan $4\\text{ CO}_2$ (2 putaran); $2\\text{ CO}_2$ lainnya telah dilepaskan pada tahap Dekarboksilasi Oksidatif asam piruvat<br>• Pernyataan 3 BENAR: Peran respirasi oksigen aerob<br>• Pernyataan 4 SALAH: Fermentasi asam laktat hanya menghasilkan $2\\text{ ATP}$ netto dari glikolisis murni"
        },
        "hints": {
            "concept": "Glikolisis di sitosol tanpa O2. Dari 6 CO2: 2 CO2 di Dekarboksilasi Oksidatif, 4 CO2 di Siklus Krebs (jadi pernyataan 2 salah). O2 akseptor elektron terakhir jadi H2O. Fermentasi hanya 2 ATP.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "bio-sim-32",
        "type": "matrix",
        "materi": "BIOLOGI MOLEKULER & REPLIKASI DNA",
        "topic": "Struktur Asam Nukleat, Replikasi Semikonservatif, dan Dogma Sentral",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai struktur materi genetik dan sintesis protein seluler!",
        "statements": [
            {
                "text": "Dua untai polinukleotida pada molekul heliks ganda DNA tersusun secara antiparalel, di mana satu untai berorientasi 5' ke 3' dan untai komplemennya berorientasi 3' ke 5'.",
                "correct": True
            },
            {
                "text": "Pasangan basa nitrogen guanin dan sitosin (G-C) dihubungkan oleh dua ikatan hidrogen, sedangkan adenin dan timin (A-T) dihubungkan oleh tiga ikatan hidrogen.",
                "correct": False
            },
            {
                "text": "Eksperimen Meselson-Stahl membuktikan bahwa replikasi DNA berlangsung secara semikonservatif, di mana setiap DNA anakan terdiri atas satu untai induk lama dan satu untai baru.",
                "correct": True
            },
            {
                "text": "Kodon inisiasi translasi pada semua molekul mRNA eukariotik adalah AUG yang mengkode asam amino metionin.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP STRUKTUR DNA & DOGMA SENTRAL",
            "latex": "\\text{DNA Antiparalel: } 5' \\to 3' \\iff 3' \\to 5'; \\quad \\text{Ikatan H: } A=T \\ (2\\text{ ikatan}), \\ G \\equiv C \\ (3\\text{ ikatan}); \\quad \\text{Start Codon: AUG}",
            "legend": "• Pernyataan 1 BENAR: Sifat antiparalel Watson-Crick<br>• Pernyataan 2 SALAH: Terbalik! G-C memiliki 3 ikatan hidrogen (lebih stabil/titik leleh tinggi), A-T hanya memiliki 2 ikatan hidrogen<br>• Pernyataan 3 BENAR: Eksperimen isotop nitrogen $^{15}\\text{N}$ dan $^{14}\\text{N}$ Meselson-Stahl (1958)<br>• Pernyataan 4 BENAR: Kodon AUG adalah start kodon universal"
        },
        "hints": {
            "concept": "Untai DNA antiparalel (5' ke 3' dan 3' ke 5'). Pasangan G-C punya 3 ikatan hidrogen, A-T punya 2 ikatan hidrogen (pernyataan 2 terbalik). Replikasi semikonservatif (Meselson-Stahl). Kodon start = AUG (metionin).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "bio-sim-33",
        "type": "matrix",
        "materi": "FISIOLOGI EKSKRESI NEFRON GINJAL",
        "topic": "Filtrasi, Reabsorpsi, Augmentasi, dan Kontrol Hormonal Urin",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai struktur dan fungsi nefron ginjal manusia!",
        "statements": [
            {
                "text": "Seluruh molekul glukosa dan asam amino pada orang sehat direabsorpsi 100% kembali ke dalam darah di tubulus kontortus proksimal.",
                "correct": True
            },
            {
                "text": "Filtrasi darah di glomerulus menghasilkan urin sesungguhnya yang siap dialirkan langsung menuju ureter.",
                "correct": False
            },
            {
                "text": "Hormon aldosteron merangsang reabsorpsi ion natrium (Na+) dan ekskresi ion kalium (K+) di tubulus kontortus distal.",
                "correct": True
            },
            {
                "text": "Kekurangan produksi hormon antidiuretik (ADH) menyebabkan penyakit Diabetes Melitus yang ditandai dengan kadar gula urin tinggi.",
                "correct": False
            }
        ],
        "formula": {
            "title": "MEKANISME EKSKRESI NEFRON GINJAL",
            "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Urin Primer} \\xrightarrow{\\text{TKP}} \\text{Urin Sekunder} \\xrightarrow{\\text{TKD & Augmentasi}} \\text{Urin Sesungguhnya}",
            "legend": "• Pernyataan 1 BENAR: Reabsorpsi obligat glukosa & asam amino di tubulus proksimal via kotranspor natrium<br>• Pernyataan 2 SALAH: Glomerulus menghasilkan urin primer (bukan urin sesungguhnya)<br>• Pernyataan 3 BENAR: Fungsi hormon aldosteron korteks adrenal<br>• Pernyataan 4 SALAH: Kekurangan ADH memicu Diabetes Insipidus (urin banyak & encer tanpa gula); Diabetes Melitus disebabkan defisiensi insulin"
        },
        "hints": {
            "concept": "Glukosa direabsorpsi 100% di TKP. Glomerulus menghasilkan urin primer (bukan urin sesungguhnya). Aldosteron menyerap Na+ dan buang K+ di TKD. Kekurangan ADH memicu Diabetes Insipidus, bukan Diabetes Melitus.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "bio-sim-34",
        "type": "matrix",
        "materi": "HEREDITAS & GENETIKA POPULASI",
        "topic": "Hukum Mendel, Pautan Seks, dan Kesetimbangan Hardy-Weinberg",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai prinsip-prinsip genetika klasik dan populasi!",
        "statements": [
            {
                "text": "Menurut Hukum Mendel II (Asortasi Bebas), alel-alel dari gen yang berbeda memilah secara bebas satu sama lain selama pembentukan gamet, asalkan gen-gen tersebut terletak pada kromosom yang berbeda atau berjauhan.",
                "correct": True
            },
            {
                "text": "Peristiwa pautan gen (gene linkage) terjadi apabila dua gen terletak pada kromosom yang berbeda dan memilah secara bebas.",
                "correct": False
            },
            {
                "text": "Seorang anak laki-laki buta warna dapat lahir dari pasangan ibu pembawa sifat (carrier) dan ayah berpenlihatan normal.",
                "correct": True
            },
            {
                "text": "Hanyutan genetik (genetic drift) memiliki dampak perubahan frekuensi alel yang jauh lebih signifikan pada populasi berukuran kecil dibandingkan populasi besar.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP GENETIKA MENDELIAN & EVOLUSI POPULASI",
            "latex": "\\text{Linkage} \\iff \\text{Gen pada Kromosom Sama}; \\quad \\text{Drift} \\propto \\frac{1}{2N_e}; \\quad \\text{Pewarisan Buta Warna: } X^C X^c \\times X^C Y \\implies X^c Y",
            "legend": "• Pernyataan 1 BENAR: Syarat berlakunya Hukum Asortasi Bebas Mendel II<br>• Pernyataan 2 SALAH: Pautan gen terjadi jika gen-gen terletak pada KROMOSOM YANG SAMA (berdekatan), sehingga tidak memilah bebas<br>• Pernyataan 3 BENAR: Anak laki-laki ($X^c Y$) mewarisi alel $X^c$ dari ibu carrier ($X^C X^c$)<br>• Pernyataan 4 BENAR: Efek leher botol (bottleneck) dan efek pendiri (founder effect) sangat drastis pada populasi kecil"
        },
        "hints": {
            "concept": "Hukum Mendel II berlaku untuk gen di kromosom berbeda. Pautan gen terjadi pada gen di KROMOSOM YANG SAMA (pernyataan 2 salah). Anak laki-laki buta warna dapat lahir dari ibu carrier (XCXc x XCY -> XcY). Genetic drift berdampak besar pada populasi kecil.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "bio-sim-35",
        "type": "matrix",
        "materi": "EKOLOGI & ALIRAN ENERGI",
        "topic": "Rantai Makanan, Piramida Ekologi, dan Suksesi",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai dinamika ekosistem dan aliran materi-energi!",
        "statements": [
            {
                "text": "Piramida energi dalam suatu ekosistem alami selalu berbentuk tegak (tidak pernah terbalik) karena sebagian energi selalu terdisipasi sebagai panas pada setiap kenaikan tingkat trofik.",
                "correct": True
            },
            {
                "text": "DDT dan logam berat seperti raksa mengalami biomagnifikasi, di mana konsentrasi racun per satuan massa tubuh justru menurun pada tingkat trofik puncak.",
                "correct": False
            },
            {
                "text": "Simbiosis mutualisme mikoriza antara jamur dengan akar tumbuhan membantu penyerapan unsur fosfor dan air oleh tumbuhan.",
                "correct": True
            },
            {
                "text": "Suksesi sekunder berlangsung lebih cepat mencapai komunitas klimaks dibandingkan suksesi primer karena lapisan tanah dan bank biji masih tersisa di habitat.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP ALIRAN ENERGI & DINAMIKA EKOLOGI",
            "latex": "\\text{Hukum Termodinamika II: Entropi } \\uparrow \\implies \\text{Piramida Energi Selalu Tegak}; \\quad \\text{Biomagnifikasi: Konsentrasi Toksin di Trofik Puncak } \\uparrow",
            "legend": "• Pernyataan 1 BENAR: Sesuai Hukum Termodinamika II, energi tidak dapat didaur ulang dan selalu berkurang di trofik atas<br>• Pernyataan 2 SALAH: Biomagnifikasi berarti konsentrasi racun yang tidak dapat terurai MAKRO-TERKONSENTRASI di trofik puncak (seperti DDT pada elang botak)<br>• Pernyataan 3 BENAR: Mikoriza memperluas area serapan hara fosfat tanaman<br>• Pernyataan 4 BENAR: Suksesi sekunder memiliki modal tanah humus awal yang subur"
        },
        "hints": {
            "concept": "Piramida energi selalu tegak (Hukum II Termodinamika). Biomagnifikasi: racun terakumulasi PALING TINGGI di konsumen puncak (pernyataan 2 salah). Mikoriza membantu serap fosfat. Suksesi sekunder lebih cepat dari suksesi primer karena tanah sudah ada.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    }
]
