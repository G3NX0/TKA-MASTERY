# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Biologi (SMA/MA Saintek)
Dataset: Latihan Tingkat Easy (25 Authentic Questions, bio-lat-e-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

BIOLOGI_EASY_ITEMS = [
    {
        "id": "bio-lat-e-01",
        "materi": "BIOLOGI SEL & ORGANEL",
        "topic": "Fungsi Organel Sintesis dan Modifikasi Protein",
        "stem": "Dalam sel eukariotik sekretori seperti sel asinar pankreas yang memproduksi enzim pencernaan, protein disintesis oleh ribosom yang melekat pada membran organel tertentu sebelum dimodifikasi lebih lanjut dan dikemas ke dalam vesikel sekretori. Urutan organel yang dilalui oleh protein sekretori sejak disintesis hingga diekskresikan keluar sel adalah...",
        "correct": "Ribosom $\\rightarrow$ Retikulum Endoplasma Kasar $\\rightarrow$ Vesikel Transpor $\\rightarrow$ Badan Golgi $\\rightarrow$ Vesikel Sekretori $\\rightarrow$ Membran Plasma (Eksositosis).",
        "distractors": [
            "Ribosom $\\rightarrow$ Mitokondria $\\rightarrow$ Lisosom $\\rightarrow$ Badan Golgi $\\rightarrow$ Dinding Sel.",
            "Retikulum Endoplasma Halus $\\rightarrow$ Peroksisom $\\rightarrow$ Sentriol $\\rightarrow$ Membran Plasma.",
            "Nukleolus $\\rightarrow$ Vakuola Sentral $\\rightarrow$ Kloroplas $\\rightarrow$ Badan Golgi $\\rightarrow$ Sitosol.",
            "Ribosom $\\rightarrow$ Badan Golgi $\\rightarrow$ Retikulum Endoplasma Kasar $\\rightarrow$ Nukleus $\\rightarrow$ Membran Plasma."
        ],
        "formula": {
            "title": "JALUR ENDOMEMBRAN SEKRESI PROTEIN SELULER",
            "latex": "\\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi di RE Kasar}} \\text{Badan Golgi (Glikosilasi)} \\xrightarrow{\\text{Vesikel}} \\text{Eksositosis}",
            "legend": "• RE Kasar: Melipat dan memberi modifikasi awal polipeptida<br>• Badan Golgi: Memilah, menandai (sorting), dan mengemas protein sekretori<br>• Eksositosis: Penggabungan vesikel sekretori dengan membran plasma"
        },
        "hints": {
            "concept": "Protein sekretori diproduksi di RE kasar, dibawa vesikel transpor ke cis-Golgi, dimatangkan di trans-Golgi, lalu dibawa vesikel sekretori menuju membran plasma.",
            "execution": "Urutan tepat: Ribosom -> RE Kasar -> Vesikel Transpor -> Badan Golgi -> Vesikel Sekretori -> Membran Plasma."
        }
    },
    {
        "id": "bio-lat-e-02",
        "materi": "TRANSPOR MEMBRAN SEL",
        "topic": "Fenomena Plasmolisis pada Sel Tumbuhan",
        "stem": "Ketika sel epidermis daun tanaman $\\textit{Rhoeo discolor}$ dimasukkan ke dalam larutan sukrosa $20\\%$ (larutan hipertonik terhadap cairan sel), terjadi peristiwa lepasnya membran plasma dari dinding sel tumbuhan. Fenomena ini disebut...",
        "correct": "Plasmolisis, terjadi karena molekul air berosmosis keluar dari vakuola sel menuju larutan sukrosa yang memiliki potensial air lebih rendah sehingga protoplasma mengerut.",
        "distractors": [
            "Lisis (sitolisis), terjadi karena air berdifusi masuk secara masif menyebabkan dinding sel pecah akibat tekanan osmosis tinggi.",
            "Turgiditas, terjadi karena sel menyerap air garam secara difusi terfasilitasi hingga vakuola mengembang maksimal.",
            "Krenasi, terjadi karena dinding sel selulosa tumbuhan hancur lebur larut dalam molekul sukrosa pekat.",
            "Deplasmolisis, terjadi karena zat terlarut sukrosa dipompa masuk secara transpor aktif primer melawan gradien konsentrasi."
        ],
        "formula": {
            "title": "PRINSIP OSMOSIS PADA SEL TUMBUHAN",
            "latex": "\\Psi_w = \\Psi_s + \\Psi_p; \\quad \\Psi_{w,\\text{dalam}} > \\Psi_{w,\\text{luar}} \\implies \\text{Efluks Air} \\implies \\text{Plasmolisis}",
            "legend": "• Larutan hipertonik memiliki potensial air ($\Psi_w$) lebih rendah<br>• Air bergerak spontan dari potensial tinggi ke rendah (keluar sel)<br>• Protoplas mengerut menjauhi dinding sel kaku = Plasmolisis"
        },
        "hints": {
            "concept": "Sel tumbuhan di lingkungan hipertonik akan kehilangan air lewat osmosis. Dinding sel tetap kaku, tetapi protoplasma mengerut terlepas dari dinding.",
            "execution": "Peristiwa mengerutnya protoplasma dan terlepasnya membran dari dinding sel disebut plasmolisis."
        }
    },
    {
        "id": "bio-lat-e-03",
        "materi": "ENZIMOLOGI & METABOLISME",
        "topic": "Pengaruh Suhu terhadap Kecepatan Reaksi Enzim",
        "stem": "Grafik laju reaksi enzimatik terhadap suhu menunjukkan peningkatan kecepatan hingga mencapai suhu optimum (sekitar $37-40^\\circ\\text{C}$ pada manusia), namun laju reaksi menurun drastis hingga mendekati nol saat suhu dinaikkan melampaui $60^\\circ\\text{C}$. Penyebab utama penurunan drastis laju reaksi enzim pada suhu tinggi tersebut adalah...",
        "correct": "Denaturasi protein enzim; energi kinetik termal yang berlebihan memutuskan ikatan hidrogen dan interaksi nonkovalen penstabil konformasi tiga dimensi sisi aktif enzim sehingga substrat tidak dapat berikatan lagi.",
        "distractors": [
            "Substrat mengalami hidrolisis spontan menjadi gas karbon dioksida sebelum sempat bertumbukan dengan enzim.",
            "Enzim kehabisan energi aktivasi karena seluruh molekul ATP di dalam bejana reaksi telah terurai habis.",
            "Terbentuknya kompleks enzim-substrat yang bersifat kovalen permanen sehingga enzim tidak dapat melepaskan produk.",
            "Enzim membeku dan mengkristal menjadi endapan kalsium fosfat yang tidak dapat larut dalam air."
        ],
        "formula": {
            "title": "PENGARUH SUHU TERHADAP AKTIVITAS ENZIM",
            "latex": "\\text{Suhu Rendah: Inaktif (Kinetik Rendah)}; \\quad T_{\\text{opt}}: V_{\\max}; \\quad T > 55^\\circ\\text{C}: \\text{Denaturasi Termal}",
            "legend": "• Enzim adalah biokatalisator berbahan dasar protein globular<br>• Panas ekstrem merusak struktur sekunder dan tersier sisi aktif<br>• Kerusakan konformasi 3D bersifat ireversibel (denaturasi)"
        },
        "hints": {
            "concept": "Enzim adalah protein. Suhu tinggi merusak ikatan non-kovalen yang mempertahankan bentuk sisi aktifnya. Proses perusakan bentuk struktur protein ini disebut denaturasi.",
            "execution": "Pilih opsi yang menjelaskan denaturasi protein enzim dan kerusakan konformasi sisi aktif."
        }
    },
    {
        "id": "bio-lat-e-04",
        "materi": "KATABOLISME GLUKOSA (RESPIRASI AEROB)",
        "topic": "Tahap Glikolisis dan Hasil Produk Bersih",
        "stem": "Glikolisis merupakan tahapan awal katabolisme karbohidrat yang berlangsung di sitoplasma (sitosol) sel. Dalam pemecahan satu molekul glukosa ($6\\text{C}$) menjadi dua molekul asam piruvat ($3\\text{C}$), dihasilkan produk bersih ($\\textit{net yield}$) berupa...",
        "correct": "2 molekul Asam Piruvat, 2 molekul ATP bersih (karena menghasilkan 4 ATP tetapi mengonsumsi 2 ATP di awal), dan 2 molekul NADH.",
        "distractors": [
            "2 molekul Asetil Ko-A, 4 molekul ATP bersih, dan 2 molekul FADH2.",
            "1 molekul Asam Sitrat, 2 molekul CO2, dan 36 molekul ATP.",
            "2 molekul Asam Laktat, 2 molekul NAD+, dan 0 molekul ATP.",
            "2 molekul Etanol, 2 molekul CO2, dan 38 molekul ATP bersih."
        ],
        "formula": {
            "title": "PERSAMAAN REAKSI BERSIH GLIKOLISIS",
            "latex": "\\text{Glukosa} + 2\\text{NAD}^+ + 2\\text{ADP} + 2\\text{P}_i \\to 2\\text{ Asam Piruvat} + 2\\text{NADH} + 2\\text{H}^+ + 2\\text{ATP}",
            "legend": "• Fase Investasi Energi: Membutuhkan 2 ATP<br>• Fase Pemanenan Energi: Menghasilkan 4 ATP & 2 NADH<br>• Hasil Bersih: 2 Piruvat + 2 ATP Netto + 2 NADH"
        },
        "hints": {
            "concept": "Glikolisis memecah glukosa (6C) menjadi 2 piruvat (3C). Total dibuat 4 ATP tetapi 2 ATP dipakai di tahap investasi, sehingga hasil bersih 2 ATP dan 2 NADH.",
            "execution": "Produk bersih: 2 Asam Piruvat, 2 ATP bersih, dan 2 NADH."
        }
    },
    {
        "id": "bio-lat-e-05",
        "materi": "ANABOLISME (FOTOSINTESIS)",
        "topic": "Reaksi Terang dan Fotolisis Air pada Kloroplas",
        "stem": "Dalam fotosintesis tumbuhan hijau, reaksi terang berlangsung di membran tilakoid kloroplas. Oksigen ($\\text{O}_2$) yang dilepaskan ke atmosfer oleh tumbuhan hijau selama fotosintesis berasal dari peristiwa...",
        "correct": "Fotolisis air (pemecahan molekul $\\text{H}_2\\text{O}$ oleh energi foton cahaya pada kompleks fotosistem II) yang menghasilkan elektron, proton $\\text{H}^+$, dan gas $\\text{O}_2$.",
        "distractors": [
            "Reduksi gas karbon dioksida ($\text{CO}_2$) oleh enzim Rubisco pada tahap fiksasi Siklus Calvin.",
            "Penguraian molekul glukosa cadangan di dalam stroma kloroplas pada malam hari.",
            "Fotofosforilasi siklik yang melibatkan pelepasan oksigen dari membran luar kloroplas.",
            "Oksidasi molekul NADPH menjadi NADP+ pada membran grana saat reaksi gelap."
        ],
        "formula": {
            "title": "REAKSI FOTOLISIS AIR PADA FOTOSISTEM II",
            "latex": "2\\text{H}_2\\text{O} \\xrightarrow{h\\nu, \\text{ OEC pada PS II}} 4\\text{H}^+ + 4e^- + \\text{O}_2(g)",
            "legend": "• Dibuktikan oleh eksperimen Ruben & Kamen menggunakan isotop $^{18}\\text{O}$<br>• Elektron menggantikan kekosongan elektron pada pusat reaksi $P_{680}$<br>• Gas $\\text{O}_2$ dilepaskan melalui stomata"
        },
        "hints": {
            "concept": "Eksperimen isotop membuktikan bahwa O2 yang dilepas tanaman berasal dari H2O, bukan dari CO2. Air dipecah oleh cahaya di FS II (fotolisis air).",
            "execution": "Pilih fotolisis air pada fotosistem II."
        }
    },
    {
        "id": "bio-lat-e-06",
        "materi": "GENETIKA MOLEKULER (STRUKTUR DNA)",
        "topic": "Aturan Pasangan Basa Nitrogen Chargaff",
        "stem": "Analisis biokimia terhadap sampel DNA heliks ganda dari suatu spesies bakteri menunjukkan bahwa proporsi basa nitrogen adenin ($\\text{A}$) adalah $28\\%$. Berdasarkan aturan kesetaraan Chargaff dan ikatan hidrogen komplementer, persentase basa nitrogen sitosin ($\\text{C}$) dalam DNA bakteri tersebut adalah...",
        "correct": "$22\\%$, karena menurut aturan Chargaff jumlah $\\text{A} = \\text{T}$ dan $\\text{G} = \\text{C}$. Jika $\\text{A} = 28\\%$, maka $\\text{T} = 28\\%$ (total $\\text{A} + \\text{T} = 56\\%$). Sisanya adalah $\\text{G} + \\text{C} = 100\\% - 56\\% = 44\\%$, sehingga persentase sitosin adalah $\\text{C} = \\frac{44\\%}{2} = 22\\%$.",
        "distractors": [
            "$28\\%$, karena seluruh keempat jenis basa nitrogen selalu memiliki proporsi persentase yang identik.",
            "$44\\%$, dihitung dari pengurangan total persentase tanpa membagi dua pasangan guanin dan sitosin.",
            "$14\\%$, dihitung dari pembagian persentase adenin dengan jumlah rantai ganda heliks DNA.",
            "$56\\%$, karena menyamakan persentase sitosin dengan jumlah gabungan adenin dan timin."
        ],
        "formula": {
            "title": "ATURAN CHARGAFF PADA DNA DOUBLE HELIX",
            "latex": "\\%A = \\%T; \\quad \\%G = \\%C; \\quad (\\%A + \\%T) + (\\%G + \\%C) = 100\\%",
            "legend": "• $\%A = 28\\% \\implies \\%T = 28\\%$<br>• $\\%G + \\%C = 100\\% - 56\\% = 44\\%$<br>• $\\%C = \\%G = 22\\%$ (terdapat 3 ikatan hidrogen antara G dan C)"
        },
        "hints": {
            "concept": "Pada DNA utas ganda: %A = %T dan %G = %C. Jumlah total A + T + G + C = 100%.",
            "execution": "A = 28% -> T = 28%. A + T = 56%. Maka G + C = 44%. C = 44% / 2 = 22%."
        }
    },
    {
        "id": "bio-lat-e-07",
        "materi": "SINTESIS PROTEIN",
        "topic": "Transkripsi dan Penentuan Kodon mRNA",
        "stem": "Suatu untai cetakan DNA ($\\textit{DNA template / antisense}$) memiliki urutan basa nitrogen dari ujung $3'$ ke $5'$ sebagai berikut:<br>$$3'\\text{-TAC–GGA–TTC–CGA–ACT-}5'$$<br>Urutan basa nitrogen pada molekul $\\text{mRNA}$ (kodon) yang terbentuk hasil transkripsi adalah...",
        "correct": "$5'\\text{-AUG–CCU–AAG–GCU–UGA-}3'$, karena transkripsi membentuk rantai komplementer antiparalel dengan mengganti basa adenin pada DNA menjadi urasil pada RNA, timin menjadi adenin, sitosin menjadi guanin, dan guanin menjadi sitosin.",
        "distractors": [
            "$5'\\text{-AUG–CCA–AAG–GCU–UGA-}3'$, akibat salah menyalin pasangan basa sitosin menjadi adenin.",
            "$3'\\text{-AUG–CCU–AAG–GCU–UGA-}5'$, karena orientasi arah polaritas ujung 5' dan 3' terbalik.",
            "$5'\\text{-ATG–CCT–AAG–GCT–TGA-}3'$, karena masih mengandung basa nitrogen timin yang tidak terdapat pada molekul RNA.",
            "$5'\\text{-UAC–GGA–UUC–CGA–ACU-}3'$, yang hanya menyalin untai cetakan dengan sekadar mengganti timin menjadi urasil."
        ],
        "formula": {
            "title": "ATURAN TRANSKRIPSI DNA KE MRNA",
            "latex": "\\text{DNA Template } (3' \\to 5') \\xrightarrow{\\text{RNA Polimerase}} \\text{mRNA } (5' \\to 3') \\quad (\\text{A} \\to \\text{U}, \\text{T} \\to \\text{A}, \\text{C} \\to \\text{G}, \\text{G} \\to \\text{C})",
            "legend": "• TAC $\\to$ AUG (Kodon Start / Metionin)<br>• GGA $\\to$ CCU (Prolin)<br>• TTC $\\to$ AAG (Lisin)<br>• CGA $\\to$ GCU (Alanin)<br>• ACT $\\to$ UGA (Kodon Stop)"
        },
        "hints": {
            "concept": "mRNA dibuat komplementer terhadap template (antisense) dengan arah 5' -> 3'. Pada RNA, tidak ada T, digantikan oleh U.",
            "execution": "T->A, A->U, C->G, G->C. Maka: TAC -> AUG, GGA -> CCU, TTC -> AAG, CGA -> GCU, ACT -> UGA."
        }
    },
    {
        "id": "bio-lat-e-08",
        "materi": "PEMBELAHAN SEL (MITOSIS)",
        "topic": "Ciri Khas Tahap Metafase pada Pembelahan Mitosis",
        "stem": "Pengamatan preparat mikroskopis sel ujung akar bawang merah ($\\textit{Allium cepa}$) menunjukkan benang-benang spindel telah terbentuk sempurna dan seluruh kromosom berjajar tunggal di bidang ekuator sel. Ciri tersebut menandakan bahwa sel sedang berada pada tahap...",
        "correct": "Metafase, di mana kromosom terkondensasi maksimal dan pelat metafase terbentuk dengan kinetokor setiap kromatid terikat pada mikrotubulus spindel dari kutub berlawanan.",
        "distractors": [
            "Profase, di mana membran inti baru mulai melarut dan benang kromatin mulai memadat.",
            "Anafase, di mana kromatid saudara telah terpisah ditarik menuju kutub sel yang berlawanan.",
            "Telofase, di mana membran inti terbentuk kembali dan sitokinesis mulai berlangsung.",
            "Interfase fase G1, di mana sel melakukan replikasi organel tanpa adanya pemadatan kromosom."
        ],
        "formula": {
            "title": "TAHAPAN PEMBELAHAN MITOSIS",
            "latex": "\\text{Profase} \\to \\text{Metafase (Kromosom di Ekuator)} \\to \\text{Anafase (Kromatid Berpisah)} \\to \\text{Telofase}",
            "legend": "• Metafase merupakan tahap terbaik untuk pengamatan kariotipe kromosom<br>• Kromosom berada pada tingkat kondensasi tertinggi<br>• Checkpoint spindel memastikan pembagian kromatid seimbang"
        },
        "hints": {
            "concept": "Kata kunci: kromosom berjajar di bidang ekuator / pelat tengah sel. Ini adalah ciri khas metafase.",
            "execution": "Pilih Metafase."
        }
    },
    {
        "id": "bio-lat-e-09",
        "materi": "HEREDITAS MENDEL (PERSILANGAN MONOHIBRID)",
        "topic": "Persilangan Monohibrid Dominan Penuh",
        "stem": "Tanaman kacang ercis batang tinggi ($TT$) disilangkan dengan tanaman kacang ercis batang pendek ($tt$). Seluruh keturunan pertama ($F_1$) memiliki fenotipe batang tinggi ($Tt$). Jika sesama tanaman $F_1$ disilangkan satu sama lain menghasilkan 160 tanaman keturunan kedua ($F_2$), jumlah tanaman $F_2$ yang diperkirakan berbatang tinggi adalah...",
        "correct": "120 tanaman, karena rasio fenotipe keturunan $F_2$ pada persilangan monohibrid dominan penuh menurut Hukum Mendel I adalah $3\\text{ Tinggi} : 1\\text{ Pendek}$, sehingga jumlah tanaman tinggi adalah $\\frac{3}{4} \\times 160 = 120\\text{ tanaman}$.",
        "distractors": [
            "40 tanaman, yang merupakan jumlah tanaman berfenotipe batang pendek resesif.",
            "80 tanaman, dihitung jika mengasumsikan rasio fenotipe satu banding satu seperti uji silang (test cross).",
            "160 tanaman, karena mengira sifat pendek hilang sepenuhnya dan tidak dapat muncul kembali pada generasi kedua.",
            "100 tanaman, dihitung dari pembagian rata persentase sembarang tanpa acuan hukum Mendel."
        ],
        "formula": {
            "title": "HUKUM MENDEL I (PERSILANGAN MONOHIBRID)",
            "latex": "F_1 \\times F_1: Tt \\times Tt \\implies \\text{Genotipe } 1TT : 2Tt : 1tt; \\quad \\text{Fenotipe } 3\\text{ Tinggi} : 1\\text{ Pendek}",
            "legend": "• Frekuensi fenotipe dominan (Tinggi) = $\\frac{3}{4} = 75\\%$<br>• Jumlah tanaman tinggi = $\\frac{3}{4} \\times 160 = 120\\text{ tanaman}$<br>• Frekuensi fenotipe resesif (Pendek) = $\\frac{1}{4} = 25\\%$ ($40\\text{ tanaman}$)"
        },
        "hints": {
            "concept": "Persilangan F1 x F1 (Tt x Tt) menghasilkan rasio fenotipe 3 tinggi : 1 pendek. Fraksi tanaman tinggi adalah 3/4.",
            "execution": "Jumlah = 3/4 * 160 = 120 tanaman."
        }
    },
    {
        "id": "bio-lat-e-10",
        "materi": "GOLONGAN DARAH & HEREDITAS MANUSIA",
        "topic": "Pewarisan Sistem Golongan Darah ABO",
        "stem": "Seorang ibu bergolongan darah A heterozigot ($I^A I^O$) menikah dengan seorang ayah bergolongan darah B heterozigot ($I^B I^O$). Pasangan tersebut memiliki kemungkinan melahirkan anak dengan golongan darah...",
        "correct": "Empat kemungkinan: Golongan darah A, B, AB, atau O dengan peluang masing-masing sebesar $25\\%$ ($1 : 1 : 1 : 1$), karena kombinasi gamet menghasilkan genotipe $I^A I^B$ (AB), $I^A I^O$ (A), $I^B I^O$ (B), dan $I^O I^O$ (O).",
        "distractors": [
            "Hanya golongan darah AB $100\\%$ karena sifat A dan B bersifat kodominan murni.",
            "Hanya golongan darah A dan B masing-masing $50\\%$ tanpa kemungkinan lahirnya anak golongan O.",
            "Golongan darah O $75\\%$ dan golongan darah AB $25\\%$.",
            "Hanya golongan darah O karena alel resesif selalu mendominasi dalam perkawinan heterozigot."
        ],
        "formula": {
            "title": "SISTEM GOLONGAN DARAH ABO (ALEL GANDA)",
            "latex": "P: I^A I^O \\times I^B I^O \\implies F_1: 25\\% I^A I^B (\\text{AB}), \\ 25\\% I^A I^O (\\text{A}), \\ 25\\% I^B I^O (\\text{B}), \\ 25\\% I^O I^O (\\text{O})",
            "legend": "• Alel $I^A$ dan $I^B$ bersifat kodominan terhadap satu sama lain<br>• Alel $I^A$ dan $I^B$ dominan terhadap alel $I^O$<br>• Perkawinan heterozigot A x B dapat menghasilkan seluruh 4 fenotipe ABO"
        },
        "hints": {
            "concept": "Gamet ibu: I^A dan I^O. Gamet ayah: I^B dan I^O. Silangkan keduanya dalam papan catur Punnett 2x2.",
            "execution": "Hasil: I^A I^B (AB), I^A I^O (A), I^B I^O (B), I^O I^O (O). Keempatnya mungkin terjadi dengan peluang masing-masing 25%."
        }
    },
    {
        "id": "bio-lat-e-11",
        "materi": "PERTUMBUHAN & PERKEMBANGAN TUMBUHAN",
        "topic": "Peran Hormon Auksin pada Fototropisme",
        "stem": "Koleoptil kecambah tanaman yang diletakkan di dekat jendela akan tumbuh membengkok ke arah datangnya sinar matahari (fototropisme positif). Fenomena pembengkokan batang ini terjadi karena...",
        "correct": "Hormon auksin terdegradasi atau bermigrasi menjauhi cahaya ke sisi batang yang terlindung dari cahaya (sisi gelap), menyebabkan sel-sel pada sisi gelap mengalami pemanjangan lebih cepat dibandingkan sisi yang terkena cahaya.",
        "distractors": [
            "Hormon sitokinin diproduksi secara berlebih pada sisi terang sehingga menghambat pertumbuhan sel batang.",
            "Cahaya matahari merangsang sintesis hormon giberelin di pucuk batang untuk membakar klorofil.",
            "Sel-sel pada sisi terang mengalami pembelahan meiosis lebih cepat daripada sel pada sisi gelap.",
            "Asam absisat terkonsentrasi di sisi gelap menyebabkan stomata menutup dan batang menciut."
        ],
        "formula": {
            "title": "MEKANISME FOTOTROPISME & DISTRIBUSI AUKSIN",
            "latex": "\\text{Cahaya Unilateral} \\implies \\text{Auksin berpindah ke sisi gelap} \\implies \\text{Pemanjangan sel asimetris} \\implies \\text{Batang membengkok ke cahaya}",
            "legend": "• Percobaan Frits Went & Charles Darwin pada koleoptil rumput<br>• Auksin merangsang pompa proton ($H^+$) melonggarkan dinding sel (teori pertumbuhan asam)<br>• Sisi gelap memanjang lebih cepat $\\implies$ lentur ke arah cahaya"
        },
        "hints": {
            "concept": "Auksin peka terhadap cahaya. Di sisi terkena cahaya, auksin berkurang/rusak. Di sisi gelap, auksin melimpah sehingga sel-sel sisi gelap memanjang lebih cepat.",
            "execution": "Pilih jawaban yang menjelaskan akumulasi auksin di sisi gelap yang memicu pemanjangan sel asimetris."
        }
    },
    {
        "id": "bio-lat-e-12",
        "materi": "JARINGAN HEWAN & FISIOLOGI",
        "topic": "Karakteristik dan Lokasi Otot Polos dalam Tubuh",
        "stem": "Jaringan otot yang memiliki ciri-ciri berbentuk gelendong dengan ujung meruncing, memiliki satu inti sel di tengah, bekerja secara involunter (di luar kesadaran), serta tidak memiliki pola lurik melintang ditemukan pada organ...",
        "correct": "Dinding saluran pencernaan lambung dan usus halus, serta pembuluh darah dan saluran kemih.",
        "distractors": [
            "Dinding ventrikel dan atrium jantung mamalia.",
            "Otot bisep dan trisep yang melekat pada rangka tulang lengan atas.",
            "Lidah dan otot diafragma pernapasan sukarela.",
            "Otot betis (gastroknemius) yang berfungsi untuk berlari cepat."
        ],
        "formula": {
            "title": "KLASIFIKASI JARINGAN OTOT HEWAN",
            "latex": "\\text{Otot Polos: Gelendong, 1 Inti Sentral, Involunter, Non-Lurik} \\quad (\\text{Organ Dalam})",
            "legend": "• Otot Rangka: Silindris panjang, banyak inti di tepi, lurik, volunter (sadar)<br>• Otot Jantung: Silindris bercabang (diskus interkalaris), 1-2 inti, lurik, involunter<br>• Otot Polos: Mengatur peristaltik saluran cerna & vasokonstriksi pembuluh"
        },
        "hints": {
            "concept": "Ciri: gelendong, satu inti di tengah, involunter, tidak bergaris lurik. Ini adalah ciri khas otot polos (otot organ dalam).",
            "execution": "Otot polos menyusun organ-organ viseral dalam seperti lambung, usus, dan pembuluh darah."
        }
    },
    {
        "id": "bio-lat-e-13",
        "materi": "SISTEM PEREDARAN DARAH MANUSIA",
        "topic": "Aliran Darah pada Peredaran Darah Besar (Sistemik)",
        "stem": "Urutan jalur peredaran darah besar (sirkulasi sistemik) yang benar pada tubuh manusia yang bertugas mengedarkan darah kaya oksigen dari jantung ke seluruh jaringan tubuh adalah...",
        "correct": "Ventrikel kiri (bilik kiri) $\\rightarrow$ Aorta $\\rightarrow$ Arteri $\\rightarrow$ Kapiler seluruh tubuh $\\rightarrow$ Vena cava $\\rightarrow$ Atrium kanan (serambi kanan).",
        "distractors": [
            "Ventrikel kanan $\\rightarrow$ Arteri pulmonalis $\\rightarrow$ Paru-paru $\\rightarrow$ Vena pulmonalis $\\rightarrow$ Atrium kiri.",
            "Atrium kiri $\\rightarrow$ Ventrikel kanan $\\rightarrow$ Vena porta hepatika $\\rightarrow$ Ginjal $\\rightarrow$ Aorta.",
            "Ventrikel kiri $\\rightarrow$ Arteri pulmonalis $\\rightarrow$ Jaringan otak $\\rightarrow$ Vena pulmonalis $\\rightarrow$ Bilik kanan.",
            "Atrium kanan $\\rightarrow$ Vena cava $\\rightarrow$ Seluruh tubuh $\\rightarrow$ Aorta $\\rightarrow$ Ventrikel kiri."
        ],
        "formula": {
            "title": "SIRKULASI SISTEMIK VS PULMONAL",
            "latex": "\\text{Sirkulasi Besar: Bilik Kiri (O}_2\\text{) } \\to \\text{Aorta} \\to \\text{Seluruh Tubuh} \\to \\text{Vena Cava (CO}_2\\text{)} \\to \\text{Serambi Kanan}",
            "legend": "• Bilik Kiri memiliki otot miokardium paling tebal untuk memompa darah ke seluruh tubuh<br>• Sirkulasi Kecil: Bilik Kanan $\\to$ Paru-paru $\\to$ Serambi Kiri<br>• Membawa nutrisi dan oksigen serta mengangkut sisa metabolisme"
        },
        "hints": {
            "concept": "Peredaran darah besar bermula dari bilik kiri (ventrikel kiri) memompa darah bersih via aorta ke seluruh tubuh, lalu kembali via vena kava ke serambi kanan (atrium kanan).",
            "execution": "Urutan: Bilik kiri -> Aorta -> Seluruh tubuh -> Vena kava -> Serambi kanan."
        }
    },
    {
        "id": "bio-lat-e-14",
        "materi": "SISTEM PENCERNAAN & ENZIM",
        "topic": "Fungsi Enzim Pencernaan Getah Pankreas",
        "stem": "Getah pankreas yang dialirkan ke dalam duodenum (usus dua belas jari) mengandung enzim amilase, tripsinogen (diaktifkan menjadi tripsin), dan lipase. Enzim lipase pankreas berfungsi spesifik untuk menghidrolisis...",
        "correct": "Trigliserida (lemak) yang telah diemulsikan oleh cairan empedu menjadi asam lemak dan gliserol.",
        "distractors": [
            "Polipeptida protein menjadi oligopeptida rantai pendek dalam suasana asam kuat.",
            "Polisakarida amilum menjadi disakarida maltosa pada rongga mulut.",
            "Asam nukleat DNA menjadi basa purin dan pirimidin bebas di lambung.",
            "Disakarida sukrosa menjadi monosakarida glukosa dan fruktosa murni."
        ],
        "formula": {
            "title": "PENCERNAAN ENZIMATIK LIPID",
            "latex": "\\text{Lemak} + \\text{Garam Empedu} \\to \\text{Emulsi Lemak} \\xrightarrow{\\text{Lipase Pankreas}} \\text{Asam Lemak} + 2\\text{-Monogliserida} + \\text{Gliserol}",
            "legend": "• Empedu hati: Emulsifikasi mekanik (memperluas area permukaan lipid)<br>• Lipase pankreas (steapsin): Memutus ikatan ester trigliserida<br>• Produk diserap oleh pembuluh kil (lakteal) di vili usus"
        },
        "hints": {
            "concept": "Lipase memecah lemak (trigliserida) menjadi asam lemak dan gliserol. Garam empedu membantu mengemulsikannya terlebih dahulu.",
            "execution": "Pilih hidrolisis trigliserida (lemak) menjadi asam lemak dan gliserol."
        }
    },
    {
        "id": "bio-lat-e-15",
        "materi": "SISTEM PERNAPASAN MANUSIA",
        "topic": "Pertukaran Gas pada Alveolus Paru-Paru",
        "stem": "Pertukaran gas oksigen ($\\text{O}_2$) dan karbon dioksida ($\\text{CO}_2$) antara udara di dalam rongga alveolus paru-paru dengan darah di dalam kapiler pembuluh darah berlangsung secara pasif melalui proses...",
        "correct": "Difusi sederhana, didorong oleh perbedaan tekanan parsial gas di mana $P_{\\text{O}_2}$ di alveolus ($104\\text{ mmHg}$) lebih tinggi daripada di kapiler darah deoksigenasi ($40\\text{ mmHg}$).",
        "distractors": [
            "Transpor aktif primer, yang membutuhkan penguraian energi ATP oleh pompa molekul hemoglobin pada eritrosit.",
            "Osmosis gas terlarut, yang dipicu oleh perbedaan konsentrasi ion natrium pada dinding epitel bronkiolus.",
            "Endositosis makrofag, di mana gelembung udara ditelan utuh oleh vakuola sel darah putih alveolar.",
            "Filtrasi tekanan hidrostatis, yang memompa gas melewati membran basalis secara mekanis murni."
        ],
        "formula": {
            "title": "HUKUM DIFUSI GAS FICK PADA MEMBRAN RESPIRASI",
            "latex": "\\text{Laju Difusi} \\propto \\frac{\\Delta P \\cdot A}{d}; \\quad P_{\\text{O}_2,\\text{alveolus}} (104\\text{ mmHg}) > P_{\\text{O}_2,\\text{kapiler}} (40\\text{ mmHg}) \\implies \\text{O}_2 \\text{ Masuk ke Darah}",
            "legend": "• Difusi gas bersifat pasif tanpa memerlukan energi ATP<br>• Membran alveolar sangat tipis ($0{,}5\\,\\mu\\text{m}$) dengan luas permukaan masif ($70\\,\\text{m}^2$)<br>• $\\text{CO}_2$ berdifusi berlawanan arah dari darah ke alveolus ($45 \\to 40\\text{ mmHg}$)"
        },
        "hints": {
            "concept": "Pertukaran gas O2 dan CO2 di alveolus terjadi murni secara difusi sederhana mengikuti penurunan tekanan parsial gas (dari tekanan parsial tinggi ke rendah).",
            "execution": "Pilih difusi sederhana berdasarkan perbedaan tekanan parsial gas."
        }
    },
    {
        "id": "bio-lat-e-16",
        "materi": "SISTEM EKSKRESI (NEFRON GINJAL)",
        "topic": "Tahap Pembentukan Urin Primer di Glomerulus",
        "stem": "Proses pembentukan urin pada ginjal manusia diawali dengan tahap filtrasi darah yang berlangsung di glomerulus kapsula Bowman. Komponen darah yang TIDAK ditemukan di dalam filtrat glomerulus (urin primer) pada kondisi ginjal yang sehat adalah...",
        "correct": "Sel-sel darah (eritrosit, leukosit, trombosit) dan protein berukuran besar (seperti albumin), karena pori-pori endotel glomerulus dan podosit menahannya.",
        "distractors": [
            "Molekul glukosa dan asam amino bebas yang larut dalam plasma darah.",
            "Ion-ion garam anorganik seperti natrium, kalium, dan klorida.",
            "Molekul air dan zat sisa metabolisme nitrogen berupa urea.",
            "Vitamin yang larut dalam air dan senyawa asam urat encer."
        ],
        "formula": {
            "title": "KOMPOSISI FILTRAT GLOMERULUS (URIN PRIMER)",
            "latex": "\\text{Urin Primer} = \\text{Plasma Darah Bebas Protein & Sel Darah} \\quad (\\text{Air, Glukosa, Asam Amino, Urea, Ion-ion})",
            "legend": "• Filtrasi dipengaruhi tekanan hidrostatis darah glomerulus ($55\\text{ mmHg}$)<br>• Keberadaan protein di urin = Albuminuria (kerusakan filtrasi glomerulus)<br>• Glukosa dan asam amino nantinya direabsorpsi 100% di tubulus proksimal"
        },
        "hints": {
            "concept": "Membran filtrasi glomerulus menahan sel darah dan makromolekul protein besar (seperti albumin). Glukosa, asam amino, air, dan urea lolos menjadi urin primer.",
            "execution": "Pilih sel-sel darah dan protein berukuran besar (albumin)."
        }
    },
    {
        "id": "bio-lat-e-17",
        "materi": "SISTEM SARAF & KOORDINASI",
        "topic": "Perambatan Impuls Saraf dan Transmisi Sinaps",
        "stem": "Ketika potensial aksi mencapai ujung akson (terminal prasinaptik) sebuah sel neuron, peristiwa biokimia yang secara langsung memicu pelepasan neurotransmiter (seperti asetilkolin) dari vesikel sinaps ke celah sinaps adalah...",
        "correct": "Membukanya saluran kalsium berpintu voltase ($\\text{voltage-gated Ca}^{2+}\\text{ channels}$) yang memicu influks ion $\\text{Ca}^{2+}$ ke dalam sitosol terminal prasinaptik.",
        "distractors": [
            "Keluarnya ion kalium secara masif yang menyebabkan membran sinaps membeku.",
            "Penyerapan molekul ATP secara fagositosis oleh reseptor pascasinaps.",
            "Penghentian sintesis protein secara permanen di badan sel neuron.",
            "Terjadinya depolarisasi retrograde yang membalikkan arah aliran impuls kembali ke dendrit."
        ],
        "formula": {
            "title": "TRANSMISI SINAPS KIMIAWI NEURON",
            "latex": "\\text{Depolarisasi Terminal} \\implies \\text{Influks Ca}^{2+} \\implies \\text{Fusi Vesikel Sinaps} \\implies \\text{Eksositosis Neurotransmiter}",
            "legend": "• Ion $\\text{Ca}^{2+}$ intraseluler memicu protein SNARE untuk fusi vesikel<br>• Neurotransmiter melintasi celah sinaps ($20\\text{ nm}$) secara difusi<br>• Berikatan dengan reseptor pascasinaps membuka kanal ion ligand-gated"
        },
        "hints": {
            "concept": "Potensial aksi membuka kanal Ca2+ berpintu voltase di ujung akson. Masuknya ion Ca2+ memicu vesikel sinaps berfusi dengan membran dan melepaskan neurotransmiter.",
            "execution": "Pilih terbukanya kanal kalsium berpintu voltase dan influks ion Ca2+."
        }
    },
    {
        "id": "bio-lat-e-18",
        "materi": "SISTEM IMUNITAS TUBUH",
        "topic": "Perbedaan Kekebalan Humoral dan Seluler",
        "stem": "Dalam sistem imun adaptif spesifik manusia, imunitas humoral diperantarai oleh sel limfosit B, sedangkan imunitas seluler diperantarai oleh sel limfosit T. Peran utama sel limfosit B yang telah berdiferensiasi menjadi sel plasma adalah...",
        "correct": "Memproduksi dan mensekresikan molekul antibodi (imunoglobulin) spesifik dalam jumlah besar ke dalam sirkulasi darah dan limfa untuk menetralkan antigen patogen ekstraseluler.",
        "distractors": [
            "Menghancurkan sel inang yang terinfeksi virus secara langsung dengan mensekresikan perforin dan granzim.",
            "Melakukan fagositosis menelan bakteri patogen utuh seperti yang dilakukan oleh neutrofil dan makrofag.",
            "Menghasilkan senyawa histamin dalam jumlah besar untuk memicu reaksi anafilaktik alergi lokal.",
            "Bermutasi menjadi keping darah (trombosit) untuk membendung pendarahan luka terbuka."
        ],
        "formula": {
            "title": "CABANG SISTEM IMUN ADAPTIF SPESIFIK",
            "latex": "\\begin{aligned} \\text{Imunitas Humoral:} & \\quad \\text{Sel B} \\to \\text{Sel Plasma} \\to \\text{Sekresi Antibodi (IgG, IgM, dll)} \\\\ \\text{Imunitas Seluler:} & \\quad \\text{Sel T Sitotoksik (CD8}^+\\text{)} \\to \\text{Lisis Sel Terinfeksi (Perforin)} \\end{aligned}",
            "legend": "• Sel plasma dapat memproduksi hingga 2000 molekul antibodi per detik<br>• Antibodi bekerja via netralisasi, aglutinasi, presipitasi, dan fiksasi komplemen<br>• Sel B memori bertahan lama untuk respons sekunder cepat"
        },
        "hints": {
            "concept": "Sel B berdiferensiasi menjadi sel plasma yang memproduksi antibodi spesifik untuk imunitas humoral (melawan patogen di cairan tubuh). Sel T sitotoksik membunuh sel terinfeksi secara langsung.",
            "execution": "Pilih memproduksi dan mensekresikan antibodi spesifik."
        }
    },
    {
        "id": "bio-lat-e-19",
        "materi": "EKOLOGI & EKOSISTEM",
        "topic": "Piramida Energi dan Efisiensi Ekologis 10%",
        "stem": "Dalam suatu ekosistem padang rumput, biomassa produsen (rumput) mampu mengikat energi surya sebesar $100.000\\text{ kJ}$. Mengacu pada hukum termodinamika dan kaidah transfer energi efisiensi ekologis Lindeman (rata-rata efisiensi $10\\%$ antar tingkat trofik), jumlah energi yang tersedia bagi konsumen tersier (trofik IV, seperti elang) adalah...",
        "correct": "$100\\text{ kJ}$, karena pada setiap perpindahan tingkat trofik hanya sekitar $10\\%$ energi yang ditransformasikan menjadi biomassa trofik berikutnya: Produsen ($100.000\\text{ kJ}$) $\\rightarrow$ Konsumen I ($10.000\\text{ kJ}$) $\\rightarrow$ Konsumen II ($1.000\\text{ kJ}$) $\\rightarrow$ Konsumen III ($100\\text{ kJ}$).",
        "distractors": [
            "$10.000\\text{ kJ}$, yang merupakan jumlah energi yang diterima oleh konsumen primer (herbivor).",
            "$1.000\\text{ kJ}$, yang merupakan jumlah energi yang diterima oleh konsumen sekunder (karnivor kecil).",
            "$50.000\\text{ kJ}$, dihitung jika mengasumsikan efisiensi transfer energi sebesar 50% pada tiap trofik.",
            "$10\\text{ kJ}$, dihitung jika trofik elang diperlakukan sebagai tingkat trofik kelima (konsumen kuaterner)."
        ],
        "formula": {
            "title": "HUKUM EFISIENSI ENERGI EKOLOGIS (ATURAN 10%)",
            "latex": "E_n = E_1 \\times (0{,}10)^{n-1}; \\quad E_4 = 100.000 \\times (0{,}10)^3 = 100.000 \\times 0{,}001 = 100\\text{ kJ}",
            "legend": "• Trofik 1 (Produsen): $100.000\\text{ kJ}$<br>• Trofik 2 (Konsumen Primer): $10.000\\text{ kJ}$<br>• Trofik 3 (Konsumen Sekunder): $1.000\\text{ kJ}$<br>• Trofik 4 (Konsumen Tersier): $100\\text{ kJ}$ ($90\\%$ energi hilang sebagai panas & respirasi)"
        },
        "hints": {
            "concept": "Aturan Lindeman: Hanya sekitar 10% energi berpindah ke tingkat trofik berikutnya (90% hilang sebagai panas respirasi dan ekskresi).",
            "execution": "Produsen (100.000) -> K1 (10.000) -> K2 (1.000) -> K3 (100 kJ)."
        }
    },
    {
        "id": "bio-lat-e-20",
        "materi": "BIOTEKNOLOGI KONVENSIONAL",
        "topic": "Mikroorganisme dalam Pembuatan Produk Bioteknologi Pangan",
        "stem": "Dalam pembuatan tempe dari bahan baku kedelai, terjadi proses fermentasi miselium jamur yang menguraikan protein kompleks kedelai menjadi asam amino yang mudah dicerna. Mikroorganisme utama yang berperan dalam fermentasi tempe tersebut adalah...",
        "correct": "$\\textit{Rhizopus oryzae}$ dan $\\textit{Rhizopus oligosporus}$, kapang kelompok Zygomycota yang membentuk hifa putih mengikat biji kedelai menjadi massa padat kompak.",
        "distractors": [
            "$\\textit{Saccharomyces cerevisiae}$, khamir uniseluler yang digunakan untuk fermentasi alkohol roti dan bir.",
            "$\\textit{Lactobacillus bulgaricus}$, bakteri asam laktat yang digunakan dalam pembuatan yogurt susu.",
            "$\\textit{Acetobacter xylinum}$, bakteri yang memproduksi pelikel selulosa pada pembuatan nata de coco.",
            "$\\textit{Neurospora crassa}$, jamur Ascomycota berspora jingga pada pembuatan oncom merah."
        ],
        "formula": {
            "title": "FERMENTASI PANGAN TRADISIONAL",
            "latex": "\\text{Kedelai} \\xrightarrow{\\textit{Rhizopus oligosporus}} \\text{Tempe (Enzim Protease, Lipase, Fitase)}",
            "legend": "• Hifa miselium menembus kotiledon kedelai melunakkan tekstur<br>• Enzim protease menguraikan protein menjadi asam amino bebas<br>• Kandungan isoflavon antioksidan menjadi lebih aktif dan bioavailable"
        },
        "hints": {
            "concept": "Jamur pembuat tempe adalah Rhizopus oryzae dan Rhizopus oligosporus (kapang tempe).",
            "execution": "Pilih Rhizopus oryzae / Rhizopus oligosporus."
        }
    },
    {
        "id": "bio-lat-e-21",
        "materi": "BIOTEKNOLOGI MODERN",
        "topic": "Peran Enzim Restriksi Endonuklease dan DNA Ligase",
        "stem": "Dalam teknologi rekayasa genetika pembuatan insulin manusia menggunakan plasmid bakteri (teknologi DNA rekombinan), dua jenis enzim yang mutlak diperlukan untuk memotong fragmen gen insulin dan menyambungkannya ke dalam vektor plasmid bakteri berturut-turut adalah...",
        "correct": "Enzim restriksi endonuklease (seperti $\\textit{EcoRI}$) untuk memotong urutan basa pengenal spesifik, dan DNA ligase untuk mengkatalisis pembentukan ikatan fosfodiester penyambung fragmen DNA.",
        "distractors": [
            "Enzim DNA polimerase untuk memotong untai ganda, dan RNA primase untuk mengikat fragmen intron.",
            "Enzim helikase untuk memotong ikatan hidrogen, dan enzim amilase untuk menyatukan dinding sel bakteri.",
            "Enzim tripsin untuk menghancurkan asam nukleat, dan enzim reverse transkriptase untuk menyambung protein.",
            "Enzim lisosom untuk membelah kromosom, dan enzim polimerase Taq untuk membungkus kapsid virus."
        ],
        "formula": {
            "title": "TEKNOLOGI DNA REKOMBINAN (POTONG & SAMBUNG)",
            "latex": "\\text{DNA Donor} + \\text{Plasmid} \\xrightarrow{\\text{Restriksi Endonuklease}} \\text{Sticky Ends} \\xrightarrow{\\text{DNA Ligase}} \\text{Plasmid Rekombinan}",
            "legend": "• Restriksi Endonuklease: Gunting molekuler pemotong sekuens palindromik<br>• DNA Ligase: Lem molekuler pembentuk ikatan fosfodiester gula-fosfat<br>• Ditransformasikan ke sel inang $\\textit{E. coli}$ untuk ekspresi insulin"
        },
        "hints": {
            "concept": "Gunting molekuler = enzim restriksi endonuklease. Lem molekuler = DNA ligase.",
            "execution": "Pilih restriksi endonuklease (pemotong) dan DNA ligase (penyambung)."
        }
    },
    {
        "id": "bio-lat-e-22",
        "materi": "EVOLUSI (BUKTI HOMOLOGI)",
        "topic": "Homologi Struktur Anatomi sebagai Bukti Evolusi Divergen",
        "stem": "Struktur anatomi sirip paus, sayap kelelawar, kaki depan kucing, dan lengan manusia tersusun atas pola susunan kerangka tulang yang sama (humerus, radius, ulna, karpal, metakarpal, dan falang), meskipun fungsinya sangat berbeda (berenang, terbang, berjalan, dan memegang). Hubungan struktur organ ini disebut...",
        "correct": "Homologi, membuktikan terjadinya evolusi divergen dari satu nenek moyang mamalia purba yang sama ($\\textit{common ancestor}$) yang beradaptasi menempati relung lingkungan yang berbeda.",
        "distractors": [
            "Analogi, membuktikan evolusi konvergen di mana organ berbeda asal-usul berkembang menjalankan fungsi yang sama.",
            "Organ vestigial, yaitu sisa organ masa lalu yang telah menyusut dan kehilangan seluruh fungsinya.",
            "Variasi mutasi buatan, yang sengaja dirancang manusia melalui proses inseminasi buatan selektif.",
            "Atavisme fosil, yaitu pemunculan sifat purba yang merugikan kelangsungan hidup populasi."
        ],
        "formula": {
            "title": "HOMOLOGI VS ANALOGI ORGAN EVOLUSI",
            "latex": "\\text{Homologi: Struktur Sama, Fungsi Berbeda} \\iff \\text{Evolusi Divergen (Common Ancestor)}",
            "legend": "• Sayap burung dan sirip paus = Homolog (berasal dari tungkai depan tetrapoda)<br>• Sayap serangga dan sayap burung = Analog (fungsi sama terbang, struktur asal berbeda)<br>• Homologi merupakan bukti kuat kesatuan filogenetik makhluk hidup"
        },
        "hints": {
            "concept": "Homologi: asal struktur tulang sama tetapi fungsi berbeda (evolusi divergen). Analogi: asal struktur berbeda tetapi fungsi sama (evolusi konvergen).",
            "execution": "Pilih Homologi (evolusi divergen dari nenek moyang yang sama)."
        }
    },
    {
        "id": "bio-lat-e-23",
        "materi": "SPESIASI & HUKUM HARDY-WEINBERG",
        "topic": "Syarat Berlakunya Kesetimbangan Frekuensi Genetik Hardy-Weinberg",
        "stem": "Hukum Hardy-Weinberg menyatakan bahwa frekuensi alel dan genotipe dalam suatu populasi akan tetap konstan dari generasi ke generasi apabila memenuhi syarat-syarat tertentu. Kondisi yang MENYEBABKAN berlakunya kesetimbangan Hardy-Weinberg adalah...",
        "correct": "Ukuran populasi sangat besar, terjadi perkawinan acak ($\\textit{random mating}$), tidak ada mutasi, tidak ada aliran gen (migrasi masuk atau keluar), dan tidak ada seleksi alam.",
        "distractors": [
            "Ukuran populasi sangat kecil sehingga hanyutan genetik ($\\textit{genetic drift}$) bekerja secara dominan.",
            "Terjadi perkawinan assortatif non-acak di mana individu hanya kawin dengan sesama fenotipe serupa.",
            "Tingkat laju mutasi spontan sangat tinggi untuk memunculkan alel-alel baru setiap generasi.",
            "Adanya tekanan seleksi alam yang kuat yang memusnahkan individu bergenotipe heterozigot."
        ],
        "formula": {
            "title": "PERSAMAAN KESETIMBANGAN HARDY-WEINBERG",
            "latex": "p + q = 1; \\quad p^2 + 2pq + q^2 = 1",
            "legend": "• $p$ = frekuensi alel dominan; $q$ = frekuensi alel resesif<br>• $p^2$ = genotipe homozigot dominan, $2pq$ = heterozigot, $q^2$ = homozigot resesif<br>• 5 Syarat mutlak: Populasi besar, acak, tanpa mutasi, tanpa migrasi, tanpa seleksi"
        },
        "hints": {
            "concept": "Kesetimbangan genetik hanya berlaku jika tidak ada faktor evolusi yang bekerja: populasi besar, kawin acak, tidak ada mutasi, migrasi, maupun seleksi alam.",
            "execution": "Pilih opsi yang memuat kelima syarat ketiadaan gaya evolusi tersebut."
        }
    },
    {
        "id": "bio-lat-e-24",
        "materi": "BIODIVERSITAS & EKOLOGI LINGKUNGAN",
        "topic": "Fenomena Eutrofikasi Perairan Akibat Limbah Fosfat",
        "stem": "Pembuangan limbah detergen fosfat dan sisa pupuk pertanian nitrogen ke danau dapat memicu pertumbuhan alga dan eceng gondok yang sangat pesat menutupi permukaan air ($\\textit{blooming algae}$). Dampak ekologis paling mematikan bagi kehidupan ikan di danau tersebut adalah...",
        "correct": "Penurunan drastis kadar oksigen terlarut ($\\text{Dissolved Oxygen / DO}$) air danau karena bakteri pengurai aerobik mengonsumsi oksigen secara masif saat menguraikan biomassa alga yang mati massal di dasar danau.",
        "distractors": [
            "Peningkatan konsentrasi gas ozon terlarut yang membakar sisik ikan secara spontan.",
            "Suhu air danau meningkat hingga melampaui titik didih air akibat reaksi fotosintesis eceng gondok.",
            "Air danau membeku menjadi lapisan es padat karena cahaya matahari terhalang alga.",
            "Ikan-ikan berevolusi menjadi amfibi darat secara instan dalam kurun waktu satu minggu."
        ],
        "formula": {
            "title": "MEKANISME EUTROFIKASI DAN ANPOSIA AKUATIK",
            "latex": "\\text{Limbah } N, P \\implies \\text{Blooming Alga} \\implies \\text{Kematian Alga} \\xrightarrow{\\text{Bakteri Pengurai}} \\text{Konsumsi O}_2 \\uparrow \\implies \\text{DO} \\downarrow \\implies \\text{Kematian Ikan}",
            "legend": "• Eutrofikasi: Penyuburan berlebih badan air oleh hara nutrien anorganik<br>• Biochemical Oxygen Demand (BOD) meningkat tajam<br>• Kondisi anoksia/hipoksia mematikan organisme perairan berinsang"
        },
        "hints": {
            "concept": "Ketika alga yang meledak populasinya mati, bakteri dekomposer aerob menguraikannya dan menyedot habis oksigen terlarut (DO turun drastis), menyebabkan ikan mati lemas.",
            "execution": "Pilih penurunan drastis kadar oksigen terlarut (DO) akibat aktivitas bakteri pengurai."
        }
    },
    {
        "id": "bio-lat-e-25",
        "materi": "REPRODUKSI & EMBRIOLOGI HEWAN",
        "topic": "Tahap Gastrulasi dan Pembentukan Tiga Lapisan Germinal",
        "stem": "Dalam perkembangan embrio hewan triploblastik, tahap blastula mengalami proses invaginasi seluler membentuk gastrula dengan rongga arkenteron (gastrocoel) dan tiga lapisan germinal embrionik. Lapisan ektoderm pada perkembangan organogenesis selanjutnya akan berdiferensiasi membentuk...",
        "correct": "Sistem saraf (otak dan sumsum tulang belakang) serta lapisan epidermis kulit dan derivatnya (rambut, kuku, dan reseptor sensori).",
        "distractors": [
            "Sistem rangka tulang sejati, otot lurik, sistem sirkulasi jantung, dan ginjal pembentuk urin.",
            "Lapisan epitel saluran pencernaan lambung, usus, serta organ hati dan pankreas.",
            "Jaringan ikat darah, limfa, pembuluh darah kapiler, dan gonad reproduksi testis/ovarium.",
            "Lapisan endotel dinding pembuluh darah paru-paru dan lapisan pleura pelindung dada."
        ],
        "formula": {
            "title": "TAKDIR LAPISAN GERMINAL EMBRIO (DERIVAT TRIPLOBLASTIK)",
            "latex": "\\begin{aligned} \\text{Ektoderm:} & \\quad \\text{Sistem Saraf, Epidermis Kulit, Organ Indera} \\\\ \\text{Mesoderm:} & \\quad \\text{Otot, Rangka, Jantung, Pembuluh Darah, Ginjal, Gonad} \\\\ \\text{Endoderm:} & \\quad \\text{Saluran Pencernaan, Hati, Pankreas, Paru-Paru} \\end{aligned}",
            "legend": "• Gastrulasi adalah peletakan dasar rencana tubuh hewan<br>• Ektoderm = Lapisan luar pelindung dan integrasi saraf<br>• Mesoderm = Penggerak dan transportasi internal<br>• Endoderm = Sistem pencernaan dan respirasi dalam"
        },
        "hints": {
            "concept": "Ektoderm (luar) membentuk sistem saraf (otak, sumsum tulang belakang) dan kulit luar (epidermis). Mesoderm membentuk otot, tulang, jantung. Endoderm membentuk saluran pencernaan dan hati.",
            "execution": "Pilih sistem saraf dan epidermis kulit."
        }
    }
]
