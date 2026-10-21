# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Biologi (SMA/MA Saintek)
Dataset: Latihan Tingkat Medium (25 Authentic Questions, bio-lat-m-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

BIOLOGI_MEDIUM_ITEMS = [
    {
        "id": "bio-lat-m-01",
        "materi": "RESPIRASI SELULER (SIKLUS KREBS)",
        "topic": "Produk Katabolisme Oksidatif Per Molekul Glukosa pada Matriks Mitokondria",
        "stem": "Dalam respirasi aerob sel eukariotik, dua molekul asetil koenzim-A ($2\\text{C}$) yang dihasilkan dari dekarboksilasi oksidatif memasuki Siklus Asam Sitrat (Siklus Krebs) di matriks mitokondria. Untuk setiap pemecahan lengkap satu molekul glukosa awal (setara dengan dua putaran Siklus Krebs), produk energi tereduksi dan senyawa samping yang dibebaskan adalah...",
        "correct": "$6\\text{ NADH}$, $2\\text{ FADH}_2$, $2\\text{ ATP}$ (atau $2\\text{ GTP}$), dan $4\\text{ molekul CO}_2$, karena satu putaran Siklus Krebs menghasilkan $3\\text{ NADH}$, $1\\text{ FADH}_2$, $1\\text{ ATP/GTP}$, serta melepaskan $2\\text{ CO}_2$.",
        "distractors": [
            "$2\\text{ NADH}$, $2\\text{ FADH}_2$, $36\\text{ ATP}$, dan $6\\text{ molekul CO}_2$, karena mengabaikan pembagian putaran siklus per molekul asetil ko-A.",
            "$10\\text{ NADH}$, $4\\text{ FADH}_2$, $4\\text{ ATP}$, dan $2\\text{ molekul O}_2$, dihitung dari penggabungan seluruh tahap katabolisme secara acak.",
            "$4\\text{ NADH}$, $0\\text{ FADH}_2$, $2\\text{ ATP}$, dan $2\\text{ molekul asam piruvat}$, karena menyamakan hasil Siklus Krebs dengan fermentasi asam laktat.",
            "$3\\text{ NADH}$, $1\\text{ FADH}_2$, $1\\text{ ATP}$, dan $2\\text{ CO}_2$, yang hanya menghitung hasil satu molekul asetil ko-A (setengah molekul glukosa)."
        ],
        "formula": {
            "title": "STOIKIOMETRI SIKLUS ASAM SITRAT (2 PUTARAN)",
            "latex": "2\\text{ Asetil Ko-A} + 6\\text{NAD}^+ + 2\\text{FAD} + 2\\text{GDP} + 2\\text{P}_i + 4\\text{H}_2\\text{O} \\to 4\\text{CO}_2 + 6\\text{NADH} + 2\\text{FADH}_2 + 2\\text{GTP} + 2\\text{Ko-A}",
            "legend": "• Reaksi pertama: Oksaloasetat ($4\\text{C}$) + Asetil Ko-A ($2\\text{C}$) $\\to$ Sitrat ($6\\text{C}$)<br>• $4\\text{ CO}_2$ melengkapi pelepasan 6 karbon glukosa ($2\\text{ CO}_2$ dari dekarboksilasi piruvat)<br>• Seluruh koenzim tereduksi dikirim ke Rantai Transpor Elektron"
        },
        "hints": {
            "concept": "Satu molekul glukosa menghasilkan 2 asetil Ko-A, sehingga Siklus Krebs berputar 2 kali. Kalikan hasil satu putaran (3 NADH, 1 FADH2, 1 ATP, 2 CO2) dengan dua.",
            "execution": "Hasil total untuk 1 glukosa: 6 NADH, 2 FADH2, 2 ATP, dan 4 CO2."
        }
    },
    {
        "id": "bio-lat-m-02",
        "materi": "FOSFORILASI OKSIDATIF & KEMIOSMOSIS",
        "topic": "Gradien Elektrokimia Proton dan Sintesis ATP Mitchell",
        "stem": "Dalam Rantai Transpor Elektron pada krista (membran dalam) mitokondria, elektron bertenaga tinggi dari NADH dan FADH2 ditransfer melalui kompleks protein I, II, III, dan IV menuju akseptor elektron terakhir yaitu oksigen. Aliran elektron ini memicu pemompaan ion $H^+$ dari matriks mitokondria menuju ruang antarmembran. Mekanisme pembentukan ATP menurut hipotesis kemiosmosis Peter Mitchell adalah...",
        "correct": "Akumulasi ion $H^+$ di ruang antarmembran menciptakan gaya gerak proton ($\\textit{proton-motive force}$); aliran balik ion $H^+$ menuruni gradien konsentrasi kembali ke matriks melalui saluran enzim ATP Sintase memutar rotor enzim untuk memfosforilasi ADP menjadi ATP.",
        "distractors": [
            "Ion $H^+$ langsung mengikat molekul oksigen di ruang antarmembran membentuk hidrogen peroksida bertekanan tinggi yang menekan sintesis ATP.",
            "Elektron langsung melompat keluar membran krista dan membakar gugus fosfat bebas di sitoplasma sel.",
            "Kompleks ATP Sintase memompa molekul glukosa secara transpor aktif primer langsung ke dalam matriks mitokondria.",
            "Penurunan pH di matriks mitokondria memicu pelepasan fosfat anorganik dari membran luar mitokondria."
        ],
        "formula": {
            "title": "MEKANISME KEMIOSMOSIS MITCHELL PADA MITOKONDRIA",
            "latex": "\\Delta \\mu_{\\text{H}^+} = F\\Delta\\psi - 2{,}3 RT\\Delta\\text{pH}; \\quad \\text{Aliran H}^+ \\text{ via F}_0\\text{F}_1\\text{-ATP Sintase} \\implies \\text{ADP} + \\text{P}_i \\to \\text{ATP}",
            "legend": "• Akseptor elektron terakhir: $\\frac{1}{2}\\text{O}_2 + 2\\text{H}^+ + 2e^- \\to \\text{H}_2\\text{O}$<br>• 1 NADH memompa $\\sim 10\\,\\text{H}^+ \\implies \\sim 2{,}5\\,\\text{ATP}$<br>• 1 FADH$_2$ memompa $\\sim 6\\,\\text{H}^+ \\implies \\sim 1{,}5\\,\\text{ATP}$"
        },
        "hints": {
            "concept": "Transpor elektron memompa H+ ke ruang antarmembran. Gradien proton (gaya gerak proton) ini menggerakkan ATP sintase saat H+ mengalir kembali ke matriks, menghasilkan ATP.",
            "execution": "Pilih aliran balik ion H+ menuruni gradien melalui enzim ATP Sintase."
        }
    },
    {
        "id": "bio-lat-m-03",
        "materi": "KATABOLISME ANAEROB (FERMENTASI)",
        "topic": "Tujuan Biologis Regenerasi NAD+ pada Fermentasi Asam Laktat dan Alkohol",
        "stem": "Saat sel otot manusia berolahraga sangat berat dan mengalami kekurangan pasokan oksigen, sel beralih dari respirasi aerob ke fermentasi asam laktat dengan mereduksi asam piruvat menjadi asam laktat menggunakan NADH. Tujuan biologis esensial dari reduksi asam piruvat menjadi asam laktat dalam fermentasi tersebut adalah...",
        "correct": "Meregenerasi molekul $\\text{NAD}^+$ dari $\\text{NADH}$ agar proses glikolisis dapat terus berlangsung menghasilkan pasokan energi darurat $2\\text{ ATP}$ per molekul glukosa tanpa memerlukan oksigen.",
        "distractors": [
            "Menghasilkan tambahan $34\\text{ molekul ATP}$ baru dari pemecahan ikatan laktat secara anaerob.",
            "Menaikkan pH sitosol otot agar enzim-enzim seluler terlindung dari bahaya denaturasi asam.",
            "Mengubah molekul asam laktat menjadi gas oksigen terlarut di dalam miofibril otot lurik.",
            "Menghilangkan rasa lelah otot secara instan dengan mendisosiasi ion kalsium retikulum sarkoplasma."
        ],
        "formula": {
            "title": "REGENERASI NAD+ PADA FERMENTASI ASAM LAKTAT",
            "latex": "\\text{Asam Piruvat} + \\text{NADH} + \\text{H}^+ \\xrightarrow{\\text{Laktat Dehidrogenase}} \\text{Asam Laktat} + \\text{NAD}^+",
            "legend": "• Glikolisis mutlak membutuhkan pasokan $\\text{NAD}^+$ pada tahap gliseraldehida-3-fosfat dehidrogenase<br>• Tanpa oksigen, transpor elektron macet dan pasokan $\\text{NAD}^+$ habis<br>• Fermentasi meregenerasi $\\text{NAD}^+$ demi kelangsungan hidup sel darurat"
        },
        "hints": {
            "concept": "Glikolisis membutuhkan NAD+ untuk memecah glukosa. Jika tidak ada O2, NADH menumpuk dan glikolisis berhenti. Fermentasi mereoksidasi NADH menjadi NAD+ agar glikolisis bisa terus jalan.",
            "execution": "Pilih regenerasi NAD+ agar glikolisis dapat terus berjalan menghasilkan 2 ATP."
        }
    },
    {
        "id": "bio-lat-m-04",
        "materi": "FOTOSINTESIS (SIKLUS CALVIN)",
        "topic": "Tiga Tahapan Utama Reaksi Gelap Fotosintesis",
        "stem": "Reaksi gelap (Siklus Calvin) berlangsung di dalam stroma kloroplas untuk membentuk gula dari $\\text{CO}_2$. Urutan tiga tahapan biokimia utama yang benar dalam Siklus Calvin beserta enzim dan senyawa yang terlibat adalah...",
        "correct": "1. Fiksasi Karbon: Pengikatan gas $\\text{CO}_2$ oleh Ribulosa-1,5-bisfosfat (RuBP) dikatalisis oleh enzim Rubisco membentuk 3-PGA;<br>2. Reduksi: Fosforilasi dan reduksi 3-PGA oleh ATP dan NADPH menghasilkan G3P (PGAL);<br>3. Regenerasi: Penyusunan kembali molekul G3P menggunakan ATP untuk meregenerasi akseptor RuBP.",
        "distractors": [
            "1. Fotolisis air menghasilkan O2; 2. Transpor elektron menghasilkan NADPH; 3. Kemiosmosis membentuk glukosa.",
            "1. Glikolisis memecah RuBP; 2. Siklus asam sitrat menghasilkan CO2; 3. Fosforilasi oksidatif membentuk amilum.",
            "1. Fiksasi O2 oleh klorofil; 2. Reduksi PGA menjadi piruvat; 3. Regenerasi enzim amilase di grana.",
            "1. Pembukaan stomata; 2. Pengikatan nitrogen bebas atmosfer; 3. Sintesis asam amino esensial."
        ],
        "formula": {
            "title": "TAHAPAN UTAMA SIKLUS CALVIN (3 TAHAP)",
            "latex": "3\\text{CO}_2 + 3\\text{RuBP} \\xrightarrow{\\text{Rubisco}} 6\\text{ (3-PGA)} \\xrightarrow{6\\text{ATP} + 6\\text{NADPH}} 6\\text{ G3P} \\xrightarrow{3\\text{ATP}} 1\\text{ G3P (Netto)} + 3\\text{RuBP (Regenerasi)}",
            "legend": "• Tahap 1: Karboksilasi / Fiksasi $\\text{CO}_2$<br>• Tahap 2: Reduksi menggunakan daya asimilasi reaksi terang<br>• Tahap 3: Regenerasi akseptor $\\text{CO}_2$ (RuBP)"
        },
        "hints": {
            "concept": "Tiga tahapan Siklus Calvin: 1) Fiksasi CO2 oleh RuBP (katalis Rubisco), 2) Reduksi 3-PGA menjadi G3P (butuh ATP & NADPH), 3) Regenerasi RuBP (butuh ATP).",
            "execution": "Pilih Fiksasi Karbon -> Reduksi -> Regenerasi RuBP."
        }
    },
    {
        "id": "bio-lat-m-05",
        "materi": "ADAPTASI FOTOSINTESIS (TUMBUHAN C4 VS C3)",
        "topic": "Anatomi Kranz dan Pencegahan Fotorespirasi pada Tumbuhan C4",
        "stem": "Tanaman $C_4$ seperti jagung, tebu, dan sorgum mampu mempertahankan efisiensi fotosintesis yang sangat tinggi pada kondisi iklim panas dan terik dibandingkan tanaman $C_3$. Keunggulan adaptasi anatomi dan fisiologi tumbuhan $C_4$ dalam meminimalkan fotorespirasi adalah...",
        "correct": "Memiliki anatomi Kranz dengan pemisahan spasial: fiksasi awal $\\text{CO}_2$ dilakukan di sel mesofil oleh enzim PEP karboksilase (yang tidak memiliki afinitas terhadap $\\text{O}_2$) membentuk asam malat ($4\\text{C}$), kemudian didekarboksilasi di sel seludang pembuluh ($\\textit{bundle sheath}$) menghasilkan konsentrasi $\\text{CO}_2$ lokal yang tinggi di sekitar enzim Rubisco.",
        "distractors": [
            "Hanya membuka stomata pada malam hari dan menyimpan gas oksigen di dalam vakuola raksasa sel mesofil.",
            "Tidak menggunakan enzim Rubisco sama sekali dan menggantinya dengan pigmen fikosianin alga biru.",
            "Mampu memecah molekul nitrogen bebas untuk menggantikan peran gas karbon dioksida di dalam seludang pembuluh.",
            "Menghentikan reaksi terang sepenuhnya sehingga tidak menghasilkan molekul oksigen yang dapat mengganggu Rubisco."
        ],
        "formula": {
            "title": "MEKANISME PEMISAHAN SPASIAL TUMBUHAN C4",
            "latex": "\\text{Mesofil: PEP} (3\\text{C}) + \\text{HCO}_3^- \\xrightarrow{\\text{PEP Karboksilase}} \\text{Oksaloasetat} (4\\text{C}) \\to \\text{Malat} \\xrightarrow{\\text{Transpor ke Seludang}} \\text{CO}_2 \\uparrow + \\text{Siklus Calvin (Rubisco)}",
            "legend": "• PEP karboksilase memiliki afinitas sangat tinggi terhadap karbon anorganik dan tidak bereaksi dengan $\\text{O}_2$<br>• Konsentrasi $\\text{CO}_2$ tinggi di seludang pembuluh menekan aktivitas oksigenase Rubisco (fotorespirasi ditekan hingga mendekati nol)<br>• Adaptasi optimal di daerah tropis berintensitas cahaya tinggi"
        },
        "hints": {
            "concept": "Tanaman C4 memisahkan fiksasi CO2 secara spasial (tempat): PEP karboksilase di sel mesofil membentuk malat (4C), yang lalu dibawa ke sel seludang pembuluh untuk melepaskan CO2 pekat di depan Rubisco.",
            "execution": "Pilih pemisahan spasial dengan anatomi Kranz, PEP karboksilase di mesofil, dan Rubisco di seludang pembuluh."
        }
    },
    {
        "id": "bio-lat-m-06",
        "materi": "ADAPTASI FOTOSINTESIS (TUMBUHAN CAM)",
        "topic": "Pemisahan Temporal pada Metabolisme Asam Krasulasea (CAM)",
        "stem": "Tanaman kaktus, nanas, dan lidah buaya yang hidup di daerah arid (kering) mengadopsi jalur metabolisme fotosintesis CAM ($\\textit{Crassulacean Acid Metabolism}$) untuk menghemat air. Strategi adaptasi temporal yang dilakukan oleh tumbuhan CAM adalah...",
        "correct": "Membuka stomata hanya pada malam hari untuk memfiksasi $\\text{CO}_2$ menjadi asam malat dan menyimpannya di vakuola, kemudian menutup rapat stomata pada siang hari untuk mencegah transpirasi sementara asam malat dibongkar melepaskan $\\text{CO}_2$ untuk Siklus Calvin menggunakan ATP dan NADPH dari reaksi terang.",
        "distractors": [
            "Membuka stomata pada siang hari terik dan menutupnya pada malam hari seperti tumbuhan normal pada umumnya.",
            "Menggantikan dinding selulosa batang dengan lapisan lilin kalsium karbonat yang tidak membutuhkan gas CO2 sama sekali.",
            "Menghilangkan klorofil daun dan hidup murni sebagai parasit saprofit penyerap nutrisi organik tanah gurun.",
            "Melakukan Siklus Calvin hanya pada saat musim hujan dan mengalami dormansi total selama sembilan bulan kemarau."
        ],
        "formula": {
            "title": "PEMISAHAN TEMPORAL METABOLISME TUMBUHAN CAM",
            "latex": "\\begin{aligned} \\text{Malam Hari (Stomata Buka):} & \\quad \\text{CO}_2 + \\text{PEP} \\to \\text{Malat} \\to \\text{Disimpan di Vakuola} \\\\ \\text{Siang Hari (Stomata Tutup):} & \\quad \\text{Malat di Vakuola} \\to \\text{CO}_2 + \\text{Piruvat} \\to \\text{Siklus Calvin (Stroma)} \\end{aligned}",
            "legend": "• Menutup stomata siang hari menghemat air hingga $95\\%$ dibanding tanaman biasa<br>• Fiksasi awal dan Siklus Calvin terjadi di sel yang sama tetapi berbeda waktu (pemisahan temporal)<br>• Reaksi terang menghasilkan ATP/NADPH hanya pada siang hari"
        },
        "hints": {
            "concept": "Tumbuhan CAM memisahkan fiksasi CO2 secara temporal (waktu): stomata buka malam hari (ikat CO2 jadi asam malat simpan di vakuola), stomata tutup siang hari (malat dipecah lepas CO2 untuk siklus Calvin).",
            "execution": "Pilih pembukaan stomata malam hari (fiksasi CO2 ke vakuola) dan penutupan stomata siang hari (Siklus Calvin)."
        }
    },
    {
        "id": "bio-lat-m-07",
        "materi": "REPLIKASI DNA",
        "topic": "Sintesis Untai Maju (Leading) dan Untai Lambat (Lagging)",
        "stem": "Dalam replikasi DNA eukariotik, enzim DNA polimerase III hanya mampu mensintesis untai DNA baru dengan arah pertumbuhan dari ujung $5'$ ke $3'$. Akibat dari sifat antiparalel heliks ganda DNA cetakan pada garpu replikasi ($\\textit{replication fork}$) adalah...",
        "correct": "Untai maju ($\\textit{leading strand}$) disintesis secara kontinu searah garpu replikasi, sedangkan untai lambat ($\\textit{lagging strand}$) disintesis secara diskontinu menjauhi garpu replikasi membentuk segmen-segmen pendek yang disebut fragmen Okazaki.",
        "distractors": [
            "Kedua untai baru disintesis secara serentak kontinu tanpa terputus-putus menggunakan enzim RNA ligase.",
            "Untai maju disintesis ke arah 3' ke 5', sedangkan untai lambat sama sekali tidak membutuhkan molekul primer RNA.",
            "Fragmen Okazaki hanya dibentuk pada untai cetakan yang mengandung basa purin lebih dari 80%.",
            "Enzim helikase mensintesis untai maju sedangkan DNA polimerase hanya mensintesis fragmen Okazaki."
        ],
        "formula": {
            "title": "MEKANISME GARPU REPLIKASI DNA",
            "latex": "\\text{Leading Strand: } 5' \\to 3' \\text{ (Kontinu)}; \\quad \\text{Lagging Strand: } 5' \\to 3' \\text{ (Fragmen Okazaki diskontinu disambung Ligase)}",
            "legend": "• Helikase: Membuka heliks ganda DNA<br>• Primase: Meletakkan primer RNA sebagai titik awal sintesis<br>• DNA Polimerase I: Menghilangkan primer RNA dan menggantinya dengan DNA<br>• DNA Ligase: Menggabungkan celah fosfodiester antarfragmen Okazaki"
        },
        "hints": {
            "concept": "DNA polimerase hanya bisa memanjang dari 5' ke 3'. Untai yang searah bukaan garpu disintesis kontinu (leading strand). Untai berlawanan disintesis bertahap sebagai potongan-potongan (lagging strand, fragmen Okazaki).",
            "execution": "Pilih leading strand kontinu dan lagging strand diskontinu (fragmen Okazaki)."
        }
    },
    {
        "id": "bio-lat-m-08",
        "materi": "REGULASI EKSPRESI GEN PROKARIOTIK",
        "topic": "Mekanisme Induksi Operon Lac pada Bakteri Escherichia coli",
        "stem": "Model operon $\\textit{lac}$ pada bakteri $\\textit{Escherichia coli}$ mengatur ekspresi gen yang bertanggung jawab atas metabolisme laktosa. Ketika bakteri ditumbuhkan pada media yang mengandung laktosa namun tidak mengandung glukosa, operon $\\textit{lac}$ akan diinduksi secara aktif melalui mekanisme...",
        "correct": "Molekul alolaktosa (induser turunan laktosa) berikatan dengan protein represor lac, menyebabkan perubahan konformasi protein represor sehingga terlepas dari daerah operator, memungkinkan RNA polimerase mentranskripsi gen struktural $\\textit{lacZ}$, $\\textit{lacY}$, dan $\\textit{lacA}$.",
        "distractors": [
            "Laktosa berikatan langsung dengan RNA polimerase memicu mutasi permanen pada daerah promotor operon.",
            "Protein represor lac menempel semakin erat pada operator untuk mempercepat penempelan ribosom bakteri.",
            "Glukosa disintesis secara spontan dari asam amino sitosol untuk memblokir kerja enzim permease laktosa.",
            "Gen lacZ melepaskan plasmid rekombinan yang menghancurkan seluruh dinding sel bakteri inang."
        ],
        "formula": {
            "title": "REGULASI NEGATIF & POSITIF OPERON LAC",
            "latex": "\\text{Ada Laktosa} \\implies \\text{Alolaktosa mengikat Represor} \\implies \\text{Represor Inaktif (Lepas dari Operator)} \\implies \\text{Transkripsi Gen Berjalan}",
            "legend": "• Gen struktural: $\\textit{lacZ}$ ($\\beta$-galaktosidase), $\\textit{lacY}$ (permease), $\\textit{lacA}$ (transasetilase)<br>• Tanpa laktosa: Represor aktif menempel di operator, memblokir RNA polimerase<br>• Tanpa glukosa: cAMP tinggi $\\implies$ kompleks CAP-cAMP menempel di promotor (transkripsi maksimal)"
        },
        "hints": {
            "concept": "Laktosa (alolaktosa) bertindak sebagai induser. Alolaktosa mengikat represor lac sehingga represor inaktif dan lepas dari operator. Jalur transkripsi RNA polimerase menjadi terbuka.",
            "execution": "Pilih alolaktosa berikatan dengan represor sehingga terlepas dari operator."
        }
    },
    {
        "id": "bio-lat-m-09",
        "materi": "MUTASI GEN (MUTASI TITIK)",
        "topic": "Analisis Jenis Mutasi Titik: Silent, Missense, dan Nonsense",
        "stem": "Suatu mutasi titik terjadi pada urutan nukleotida gen yang mengkode rantai polipeptida fungsional. Apabila terjadi substitusi satu pasang basa nitrogen yang menyebabkan perubahan satu kodon asam amino menjadi kodon stop terminasi ($\\text{UAA}$, $\\text{UAG}$, atau $\\text{UGA}$), jenis mutasi tersebut beserta akibat biologisnya adalah...",
        "correct": "Mutasi tanpa arti ($\\textit{nonsense mutation}$); translasi terhenti secara prematur menghasilkan rantai polipeptida yang jauh lebih pendek dan hampir selalu kehilangan fungsi biologisnya.",
        "distractors": [
            "Mutasi bisu ($\\textit{silent mutation}$); menghasilkan asam amino yang sama persis sehingga struktur dan fungsi protein tidak berubah.",
            "Mutasi salah arti ($\\textit{missense mutation}$); hanya mengubah satu jenis asam amino dan protein tetap selesai ditranslasikan hingga ujung.",
            "Mutasi pergeseran rangka ($\\textit{frameshift mutation}$); terjadi penambahan atau pengurangan tiga basa nitrogen yang mempertahankan kodon stop normal.",
            "Mutasi netral; asam amino yang berubah memiliki sifat kimia identik sehingga enzim bekerja dengan efisiensi dua kali lipat."
        ],
        "formula": {
            "title": "KLASIFIKASI MUTASI TITIK PADA SINTESIS PROTEIN",
            "latex": "\\begin{aligned} \\text{Silent:} & \\quad \\text{Kodon Berubah} \\to \\text{Asam Amino Sama} \\\\ \\text{Missense:} & \\quad \\text{Kodon Berubah} \\to \\text{Asam Amino Berbeda} \\\\ \\text{Nonsense:} & \\quad \\text{Kodon Berubah} \\to \\text{Kodon STOP Prematur (Protein Terpotong)} \\end{aligned}",
            "legend": "• Kodon Stop: UAA, UAG, UGA<br>• Nonsense mutation menghasilkan polipeptida terpotong (trunkasi)<br>• Contoh klinis: Beberapa bentuk $\\beta$-talasemia mayor dan kistik fibrosis berat"
        },
        "hints": {
            "concept": "Perubahan kodon menjadi kodon stop disebut mutasi tanpa arti (nonsense mutation). Translasi berhenti lebih awal sehingga rantai polipeptida terpotong pendek.",
            "execution": "Pilih mutasi tanpa arti (nonsense mutation) yang menghasilkan polipeptida pendek."
        }
    },
    {
        "id": "bio-lat-m-10",
        "materi": "MUTASI KROMOSOM (ABERASI NUMERIK)",
        "topic": "Mekanisme Gagal Berpisah (Nondisjunction) dan Aneuploidi",
        "stem": "Kelainan genetik sindrom Down mayoritas ($95\\%$) disebabkan oleh trisomi kromosom nomor 21 ($47, XX,+21$ atau $47, XY,+21$). Peristiwa gagal berpisah ($\\textit{nondisjunction}$) yang mendasari terbentuknya gamet dengan kromosom ekstra tersebut dapat terjadi selama...",
        "correct": "Anafase I (gagal berpisahnya pasangan kromosom homolog) atau Anafase II (gagal berpisahnya pasangan kromatid saudara) pada proses oogenesis atau spermatogenesis orang tua.",
        "distractors": [
            "Interfase fase S, di mana molekul DNA gagal melakukan replikasi semikonservatif di dalam nukleus.",
            "Telofase mitosis pada saat pembelahan sel-sel epitel jaringan somatik embrio.",
            "Sitokinesis pembelahan biner amitosis pada sel-sel bakteri usus halus ibu.",
            "Profase I saat terjadi pertukaran segmen kromatid non-saudara pada proses pindah silang kiasma."
        ],
        "formula": {
            "title": "MEKANISME NONDISJUNCTION PADA MEIOSIS",
            "latex": "\\begin{aligned} \\text{Nondisjunction Meiosis I:} & \\quad \\text{Kromosom homolog gagal pisah} \\implies 50\\% (n+1), \\ 50\\% (n-1) \\\\ \\text{Nondisjunction Meiosis II:} & \\quad \\text{Kromatid saudara gagal pisah} \\implies 50\\% n, \\ 25\\% (n+1), \\ 25\\% (n-1) \\end{aligned}",
            "legend": "• Gamet $(n+1) = 24$ kromosom dibuahi gamet normal $(n=23) \\implies$ Zigot $(2n+1) = 47$ kromosom<br>• Trisomi 21 menghasilkan fenotipe fisik dan perkembangan khas sindrom Down<br>• Frekuensi nondisjunction meningkat seiring bertambahnya usia maternal"
        },
        "hints": {
            "concept": "Nondisjunction (gagal berpisah) adalah kegagalan pemisahan kromosom homolog pada Anafase I atau kegagalan pemisahan kromatid saudara pada Anafase II.",
            "execution": "Pilih Anafase I atau Anafase II pada proses meiosis pembentukan gamet."
        }
    },
    {
        "id": "bio-lat-m-11",
        "materi": "PENYIMPANGAN SEMU MENDEL (KRIPTOMERI)",
        "topic": "Pewarisan Warna Bunga Linaria maroccana (Rasio 9 : 3 : 4)",
        "stem": "Warna bunga tanaman $\\textit{Linaria maroccana}$ dikendalikan oleh dua pasang gen: gen $A$ (ada pigmen antosianin), gen $a$ (tidak ada antosianin), gen $B$ (reaksi plasma sel bersifat basa), dan gen $b$ (plasma bersifat asam). Pigmen antosianin memunculkan warna ungu pada plasma basa ($A\\_B\\_$) dan warna merah pada plasma asam ($A\\_bb$), sedangkan tanaman tanpa antosianin ($aaB\\_$ dan $aabb$) selalu berwarna putih. Jika tanaman berbunga ungu ($AaBb$) disilangkan dengan tanaman berbunga merah ($Aabb$), rasio fenotipe keturunan yang dihasilkan adalah...",
        "correct": "$3\\text{ Ungu} : 3\\text{ Merah} : 2\\text{ Putih}$ (atau disederhanakan dari $6 : 6 : 4$), karena persilangan alel $A$ ($Aa \\times Aa$) menghasilkan $\\frac{3}{4} A\\_$ dan $\\frac{1}{4} aa$ (putih); sedangkan persilangan alel $B$ ($Bb \\times bb$) menghasilkan $\\frac{1}{2} Bb$ dan $\\frac{1}{2} bb$. Maka ungu ($A\\_Bb$) = $\\frac{3}{4} \\times \\frac{1}{2} = \\frac{3}{8}$, merah ($A\\_bb$) = $\\frac{3}{4} \\times \\frac{1}{2} = \\frac{3}{8}$, dan putih ($aa\\_\\_$) = $\\frac{1}{4} = \\frac{2}{8}$.",
        "distractors": [
            "$9\\text{ Ungu} : 3\\text{ Merah} : 4\\text{ Putih}$, yang merupakan rasio klasik keturunan F2 hasil persilangan sesama dihibrid heterozigot AaBb x AaBb.",
            "$1\\text{ Ungu} : 1\\text{ Merah} : 1\\text{ Putih} : 1\\text{ Kuning}$, dihitung dari asumsi pemisahan bebas empat warna tanpa kriptomeri.",
            "$12\\text{ Ungu} : 3\\text{ Merah} : 1\\text{ Putih}$, yang merupakan rasio karakteristik penyimpangan epistasis dominan.",
            "$15\\text{ Ungu} : 1\\text{ Putih}$, yang merupakan rasio karakteristik penyimpangan polimeri gen ganda."
        ],
        "formula": {
            "title": "PERSILANGAN KRIPTOMERI AABb X AAbb",
            "latex": "\\begin{aligned} Aa \\times Aa & \\implies \\frac{3}{4} A\\_ \\text{ (Ada pigmen)}, \\quad \\frac{1}{4} aa \\text{ (Tanpa pigmen / Putih)} \\\\ Bb \\times bb & \\implies \\frac{1}{2} Bb \\text{ (Basa)}, \\quad \\frac{1}{2} bb \\text{ (Asam)} \\\\ \\text{Ungu } (A\\_Bb) & = \\frac{3}{4} \\times \\frac{1}{2} = \\frac{3}{8}; \\quad \\text{Merah } (A\\_bb) = \\frac{3}{4} \\times \\frac{1}{2} = \\frac{3}{8}; \\quad \\text{Putih } (aa\\_\\_) = \\frac{1}{4} = \\frac{2}{8} \\end{aligned}",
            "legend": "• Kriptomeri: Sifat gen dominan yang tersembunyi jika tidak bersama gen dominan lain<br>• Rasio akhir: $3\\text{ Ungu} : 3\\text{ Merah} : 2\\text{ Putih}$<br>• Total 8 kombinasi gamet"
        },
        "hints": {
            "concept": "Hitung probabilitas per pasang gen: Aa x Aa -> 3/4 A_ dan 1/4 aa. Bb x bb -> 1/2 Bb dan 1/2 bb. Ungu = A_Bb (3/4 * 1/2 = 3/8). Merah = A_bb (3/4 * 1/2 = 3/8). Putih = aa (1/4 = 2/8).",
            "execution": "Rasio fenotipe: 3 Ungu : 3 Merah : 2 Putih."
        }
    },
    {
        "id": "bio-lat-m-12",
        "materi": "PAUTAN GEN & PINDAH SILANG (CROSSING OVER)",
        "topic": "Penentuan Nilai Pindah Silang (NPS) pada Lalat Buah Drosophila",
        "stem": "Dalam eksperimen persilangan uji ($\\textit{test cross}$) lalat buah $\\textit{Drosophila melanogaster}$ betina bertubuh kelabu sayap panjang heterozigot ($BbVv$) dengan jantan bertubuh hitam sayap vestigial resesif homozigot ($bbvv$), diperoleh data keturunan sebagai berikut:<br>• Tubuh kelabu, sayap panjang (Parental): 965 ekor<br>• Tubuh hitam, sayap vestigial (Parental): 945 ekor<br>• Tubuh kelabu, sayap vestigial (Rekombinan): 185 ekor<br>• Tubuh hitam, sayap panjang (Rekombinan): 205 ekor<br>Besarnya persentase Nilai Pindah Silang (NPS / frekuensi rekombinasi) dan jarak genetik antara gen warna tubuh dan bentuk sayap adalah...",
        "correct": "$\\text{NPS} = 17\\%$ dengan jarak genetik $17\\text{ sentimorgan (cM)}$, karena total individu rekombinan adalah $185 + 205 = 390\\text{ ekor}$, dan total seluruh keturunan adalah $965 + 945 + 185 + 205 = 2.300\\text{ ekor}$. Nilai pindah silang dihitung dengan rumus: $\\text{NPS} = \\frac{\\sum \\text{Rekombinan}}{\\sum \\text{Total Individu}} \\times 100\\% = \\frac{390}{2300} \\times 100\\% \\approx 16{,}96\\% \\approx 17\\%$.",
        "distractors": [
            "$\\text{NPS} = 83\\%$ dengan jarak genetik $83\\text{ cM}$, dihitung dari persentase kombinasi parental bukan rekombinan.",
            "$\\text{NPS} = 50\\%$ dengan jarak genetik $50\\text{ cM}$, karena mengasumsikan pemilahan bebas Mendel sempurna tanpa pautan gen.",
            "$\\text{NPS} = 8{,}5\\%$ dengan jarak genetik $8{,}5\\text{ cM}$, karena keliru membagi jumlah rekombinan dengan angka dua.",
            "$\\text{NPS} = 0\\%$ dengan jarak genetik $0\\text{ cM}$, karena mengasumsikan pautan sempurna tanpa pernah terjadi kiasma kromatid."
        ],
        "formula": {
            "title": "PERHITUNGAN NILAI PINDAH SILANG (NPS / MAP DISTANCE)",
            "latex": "\\text{NPS} = \\frac{\\text{Jumlah Tipe Rekombinan}}{\\text{Jumlah Total Keturunan}} \\times 100\\% = \\frac{185 + 205}{2300} \\times 100\\% = \\frac{390}{2300} \\times 100\\% = 16{,}96\\% \\approx 17\\%",
            "legend": "• $1\\%\\text{ Rekombinasi} = 1\\text{ Unit Peta (map unit / centimorgan)}$<br>• Nilai $< 50\\%$ membuktikan bahwa kedua gen tertaut pada kromosom yang sama<br>• Pindah silang terjadi saat profase I meiosis (tahap pakiten)"
        },
        "hints": {
            "concept": "Rumus NPS = (Total Rekombinan / Total Seluruh Keturunan) * 100%. 1% NPS = 1 centimorgan (cM).",
            "execution": "Rekombinan = 185 + 205 = 390. Total = 965 + 945 + 185 + 205 = 2300. NPS = (390 / 2300) * 100% = 17% (17 cM)."
        }
    },
    {
        "id": "bio-lat-m-13",
        "materi": "PAUTAN SEKS (HEREDITAS TERPAUT KROMOSOM X)",
        "topic": "Pewarisan Penyakit Hemofilia pada Manusia",
        "stem": "Hemofilia merupakan kelainan pembekuan darah yang diwariskan secara resesif terpaut kromosom X ($X^h$). Seorang wanita dengan pembekuan darah normal yang ayahnya seorang penderita hemofilia menikah dengan seorang pria normal. Peluang pasangan tersebut memiliki anak laki-laki yang menderita hemofilia dari seluruh kemungkinan anak mereka adalah...",
        "correct": "$25\\%$ (atau $1$ dari $4$ kemungkinan anak), karena wanita tersebut pasti membawa alel hemofilia dari ayahnya sehingga bergenotipe pembawa ($X^H X^h$) dan pria bergenotipe normal ($X^H Y$). Persilangan menghasilkan anak: $X^H X^H$ ($25\\%$, wanita normal), $X^H X^h$ ($25\\%$, wanita carrier), $X^H Y$ ($25\\%$, pria normal), dan $X^h Y$ ($25\\%$, pria hemofilia).",
        "distractors": [
            "$50\\%$, yang merupakan peluang anak laki-laki menderita hemofilia jika yang ditanyakan khusus di antara anak laki-laki saja.",
            "$0\\%$, karena berasumsi bahwa wanita normal selalu menghasilkan keturunan yang $100\\%$ terbebas dari hemofilia.",
            "$75\\%$, dihitung dari rasio dominan sifat normal yang keliru diterapkan pada alel resesif.",
            "$12{,}5\\%$, dihitung dari pembagian ganda persentase pembawa sifat terpaut autosom."
        ],
        "formula": {
            "title": "PERSILANGAN PAUTAN X HEMOFILIA",
            "latex": "P: X^H X^h \\ (\\text{Wanita Carrier}) \\times X^H Y \\ (\\text{Pria Normal}) \\implies F_1: X^H X^H (25\\%), \\ X^H X^h (25\\%), \\ X^H Y (25\\%), \\ X^h Y (25\\%)",
            "legend": "• Ayah wanita penderita ($X^h Y$) $\\implies$ mewariskan $X^h$ kepada anak perempuannya ($X^H X^h$)<br>• Peluang anak laki-laki hemofilia dari total seluruh kelahiran = $25\\%$<br>• Peluang di antara anak laki-laki saja = $\\frac{1}{2} = 50\\%$"
        },
        "hints": {
            "concept": "Ibu memiliki ayah hemofilia, maka ibu pasti heterozigot/carrier (X^H X^h). Ayah normal (X^H Y). Dari 4 kemungkinan keturunan (XHXH, XHXh, XHY, XhY), anak laki-laki hemofilia adalah XhY (1 dari 4 = 25%).",
            "execution": "Pilih 25% dari total seluruh anak."
        }
    },
    {
        "id": "bio-lat-m-14",
        "materi": "FISIOLOGI KARDIOVASKULAR",
        "topic": "Sistem Penghantar Listrik Jantung dan Nodus Sinoatrial (SA Node)",
        "stem": "Otot jantung memiliki kemampuan untuk berkontraksi secara ritmis dan otomatis tanpa stimulasi dari saraf luar karena adanya jaringan konduksi khusus. Struktur yang bertindak sebagai pemacu alami jantung ($\\textit{natural pacemaker}$) yang menentukan frekuensi denyut jantung dasar adalah...",
        "correct": "Nodus Sinoatrial (SA node), terletak di dinding atrium kanan dekat muara vena cava superior, yang menghasilkan potensial aksi spontan dengan frekuensi intrinsik tertinggi ($70-80\\text{ kali/menit}$).",
        "distractors": [
            "Nodus Atrioventrikular (AV node), yang berfungsi mempercepat laju impuls hingga sepuluh kali lipat saat menuju apeks jantung.",
            "Berkas His (Atrioventricular bundle), yang memproduksi hormon epinefrin langsung ke dalam bilik ventrikel kiri.",
            "Serabut Purkinje, yang mengatur penutupan katup semilunaris aorta pada saat fase diastol jantung.",
            "Septum interventrikularis, yang memompa darah kotor dari bilik kanan menuju ke pembuluh balik otak."
        ],
        "formula": {
            "title": "JALUR KONDUKSI LISTRIK JANTUNG",
            "latex": "\\text{Nodus SA (Pacemaker)} \\to \\text{Jalur Internodal} \\to \\text{Nodus AV (Jeda } 0{,}1\\text{ s)} \\to \\text{Berkas His} \\to \\text{Serabut Purkinje} \\to \\text{Ventrikel}",
            "legend": "• Nodus SA mendepolarisasi atrium memicu sistol atrium (gelombang P pada EKG)<br>• Jeda $0{,}1\\text{ sekon}$ di nodus AV memberi waktu ventrikel terisi darah penuh sebelum sistol ventrikel<br>• Serabut Purkinje menyebarkan impuls cepat dari apeks ke dasar ventrikel (kompleks QRS)"
        },
        "hints": {
            "concept": "Pemacu alami jantung (pacemaker) adalah nodus sinoatrial (SA node) di dinding serambi kanan. Nodus SA mengawali potensial aksi secara ritmis.",
            "execution": "Pilih Nodus Sinoatrial (SA node)."
        }
    },
    {
        "id": "bio-lat-m-15",
        "materi": "FISIOLOGI RESPIRASI (TRANSPOR GAS)",
        "topic": "Transpor Karbon Dioksida dan Pergeseran Klorida (Chloride Shift)",
        "stem": "Sekitar $70\\%$ gas karbon dioksida ($\\text{CO}_2$) hasil metabolisme sel diangkut dalam darah dalam bentuk ion bikarbonat ($\\text{HCO}_3^-$) di dalam plasma darah. Di dalam eritrosit, $\\text{CO}_2$ bereaksi dengan air membentuk $\\text{H}_2\\text{CO}_3$ dikatalisis enzim anhidrase karbonat, yang kemudian terurai menjadi $\\text{H}^+$ dan $\\text{HCO}_3^-$. Ketika ion $\\text{HCO}_3^-$ berdifusi keluar dari eritrosit menuju plasma, keseimbangan muatan listrik eritrosit dipertahankan melalui mekanisme...",
        "correct": "Pergeseran klorida ($\\textit{chloride shift}$), yaitu masuknya ion klorida ($\\text{Cl}^-$) dari plasma darah ke dalam eritrosit melalui protein penukar anion ($\\textit{anion exchanger 1}$) untuk mengimbangi keluarnya ion $\\text{HCO}_3^-$.",
        "distractors": [
            "Pengeluaran ion natrium ($\text{Na}^+$) secara transpor aktif primer oleh pompa membran eritrosit.",
            "Masuknya ion kalsium ($\text{Ca}^{2+}$) yang memicu koagulasi darah langsung di dalam kapiler jaringan.",
            "Pelepasan molekul gas nitrogen dari hemoglobin untuk menetralkan muatan positif ion hidrogen bebas.",
            "Penyerapan molekul urea dari plasma ke dalam inti sel eritrosit matang."
        ],
        "formula": {
            "title": "KIMIA TRANSPORTASI CO2 & PERGESERAN KLORIDA",
            "latex": "\\text{CO}_2 + \\text{H}_2\\text{O} \\xrightleftharpoons{\\text{Anhidrase Karbonat}} \\text{H}_2\\text{CO}_3 \\rightleftharpoons \\text{H}^+ + \\text{HCO}_3^- \\quad \\text{dan} \\quad \\text{Efluks HCO}_3^- \\iff \\text{Influks Cl}^-",
            "legend": "• Enzim anhidrase karbonat mempercepat reaksi hingga $10^6$ kali<br>• $\\text{H}^+$ ditangkap oleh deoksihemoglobin (efek penyangga mencegah asidosis eritrosit)<br>• Masuknya ion $\\text{Cl}^-$ ke eritrosit disebut fenomena Hamburger (Chloride Shift)"
        },
        "hints": {
            "concept": "Keluarnya ion negatif bikarbonat (HCO3-) dari eritrosit diimbangi dengan masuknya ion negatif klorida (Cl-) dari plasma. Fenomena ini disebut chloride shift (pergeseran klorida).",
            "execution": "Pilih pergeseran klorida (chloride shift), masuknya ion Cl- ke dalam eritrosit."
        }
    },
    {
        "id": "bio-lat-m-16",
        "materi": "FISIOLOGI EKSKRESI & OSMOREGULASI",
        "topic": "Peran Hormon Antidiuretik (ADH) pada Tubulus Pengumpul Ginjal",
        "stem": "Ketika seseorang mengonsumsi sedikit air atau berkeringat banyak di cuaca panas, osmolaritas plasma darah meningkat dideteksi oleh osmoreseptor di hipotalamus. Hipofisis posterior kemudian mensekresikan hormon antidiuretik (ADH / vasopresin) ke dalam sirkulasi darah. Mekanisme seluler hormon ADH dalam menghemat air pada nefron ginjal adalah...",
        "correct": "ADH berikatan dengan reseptor $V_2$ di sel epitel tubulus pengumpul ($\\textit{collecting duct}$), memicu insersi saluran air akuaporin-2 ke membran apikal sehingga permeabilitas air meningkat drastis dan air diserap kembali secara osmosis ke medula ginjal yang hiperosmotik, menghasilkan volume urin sedikit dan pekat.",
        "distractors": [
            "ADH menyumbat lubang glomerulus sehingga proses filtrasi darah berhenti total selama beberapa jam.",
            "ADH merangsang pembongkaran protein albumin di kapsula Bowman untuk menyerap kelebihan garam natrium.",
            "ADH memicu sekresi ion kalium secara masif di tubulus kontortus proksimal sehingga urin menjadi cair dan bening.",
            "ADH menghancurkan lapisan medula ginjal sehingga urin langsung dialirkan ke pembuluh limfa."
        ],
        "formula": {
            "title": "MEKANISME KERJA HORMON ADH (AKUAPORIN-2)",
            "latex": "\\text{Osmolaritas Darah} \\uparrow \\implies \\text{ADH} \\uparrow \\implies \\text{Insersi Akuaporin-2 di Duktus Pengumpul} \\implies \\text{Reabsorpsi Air} \\uparrow \\implies \\text{Urin Pekat, Sedikit}",
            "legend": "• Kekurangan ADH memicu penyakit Diabetes Insipidus (urin sangat encer melimpah hingga $20\\text{ liter/hari}$)<br>• Alkohol menghambat pelepasan ADH $\\implies$ memicu dehidrasi dan sering berkemih<br>• Membantu memulihkan volume darah dan tekanan darah normal"
        },
        "hints": {
            "concept": "ADH bekerja pada tubulus pengumpul nefron. ADH merangsang penempatan saluran air (akuaporin-2) ke membran sel, meningkatkan penyerapan kembali air sehingga urin pekat dan sedikit.",
            "execution": "Pilih insersi saluran air akuaporin-2 di tubulus pengumpul yang meningkatkan reabsorpsi air."
        }
    },
    {
        "id": "bio-lat-m-17",
        "materi": "FISIOLOGI ENDOKRIN & HOMEOSTASIS",
        "topic": "Regulasi Umpan Balik Kadar Glukosa Darah oleh Insulin dan Glukagon",
        "stem": "Homeostasis konsentrasi glukosa darah manusia normal dipertahankan pada kisaran $70-110\\text{ mg/dL}$ melalui mekanisme umpan balik negatif hormon pankreas. Setelah seseorang mengonsumsi makanan kaya karbohidrat, peningkatan kadar glukosa darah akan merangsang respon endokrin berupa...",
        "correct": "Sel beta pulau Langerhans pankreas mensekresikan insulin, yang merangsang translokasi transporter GLUT-4 pada sel otot rangka dan adiposa untuk menyerap glukosa, serta merangsang glikogenesis (pembentukan glikogen) di organ hati.",
        "distractors": [
            "Sel alfa pankreas mensekresikan glukagon untuk memicu glikogenolisis dan glukoneogenesis di hati.",
            "Kelenjar medula adrenal mensekresikan epinefrin untuk menguraikan cadangan protein menjadi asam laktat.",
            "Korteks adrenal mensekresikan hormon aldosteron untuk mengekskresikan glukosa berlebih lewat tubulus ginjal.",
            "Kelenjar tiroid memproduksi tiroksin yang mengubah glukosa menjadi kalsitonin padat pada tulang."
        ],
        "formula": {
            "title": "HOMEOSTASIS GLUKOSA DARAH PANKREATIK",
            "latex": "\\begin{aligned} \\text{Glukosa Darah Tinggi (Pasca Makan):} & \\quad \\text{Sel } \\beta \\to \\text{Insulin} \\to \\text{Penyerapan Seluler & Glikogenesis Hati} \\\\ \\text{Glukosa Darah Rendah (Puasa):} & \\quad \\text{Sel } \\alpha \\to \\text{Glukagon} \\to \\text{Glikogenolisis & Glukoneogenesis} \\end{aligned}",
            "legend": "• Insulin memfasilitasi masuknya glukosa ke jaringan perifer via GLUT-4<br>• Glukagon bekerja secara antagonis menaikkan kadar gula darah saat puasa<br>• Kerusakan sel beta pankreas memicu Diabetes Melitus Tipe 1"
        },
        "hints": {
            "concept": "Gula darah naik -> sel beta pankreas sekresikan insulin -> memicu penyerapan glukosa oleh sel tubuh dan pembentukan glikogen di hati -> gula darah kembali normal.",
            "execution": "Pilih sekresi insulin oleh sel beta pulau Langerhans pankreas."
        }
    },
    {
        "id": "bio-lat-m-18",
        "materi": "SISTEM GERAK & KONTRAKSI OTOT",
        "topic": "Mekanisme Pergeseran Filamen (Sliding Filament Theory)",
        "stem": "Menurut teori pergeseran filamen ($\\textit{Sliding Filament Theory}$) pada kontraksi serat otot lurik, siklus pembentukan jembatan silang ($\\textit{cross-bridge}$) antara kepala miosin dan filamen aktin diawali oleh peristiwa...",
        "correct": "Pelepasan ion $\\text{Ca}^{2+}$ dari retikulum sarkoplasma yang berikatan dengan subunit troponin C, menyebabkan perubahan konformasi tropomiosin sehingga tempat pengikatan ($\\textit{binding site}$) miosin pada aktin terbuka.",
        "distractors": [
            "Pengikatan ion kalsium pada molekul titin yang memicu pemanjangan pita I dan zona H secara serentak.",
            "Hidrolisis molekul ATP oleh aktin yang menyebabkan filamen tebal menciut hingga lenyap dari sarkomer.",
            "Penempelan asetilkolin langsung pada kepala miosin yang mendorong miofibril bergeser ke arah luar tendon.",
            "Penurunan kadar asam laktat di dalam mitokondria yang mengendurkan serat kolagen otot."
        ],
        "formula": {
            "title": "SIKLUS KONTRAKSI JEMBATAN SILANG AKTIN-MIOSIN",
            "latex": "\\text{Ca}^{2+} + \\text{Troponin C} \\implies \\text{Pergeseran Tropomiosin} \\implies \\text{Situs Aktin Terbuka} \\implies \\text{Power Stroke Miosin (Pelepasan ADP + P}_i\\text{)}",
            "legend": "• ATP mengikat kepala miosin untuk melepaskannya dari aktin pasca power stroke<br>• Jika ATP habis pasca kematian $\\implies$ Rigor Mortis (kaku mayat)<br>• Kontraksi memperpendek sarkomer, zona H, dan pita I; pita A tetap konstan"
        },
        "hints": {
            "concept": "Ion Ca2+ dilepas dari retikulum sarkoplasma -> berikatan dengan troponin -> menggeser tropomiosin -> binding site miosin pada aktin terbuka -> jembatan silang terbentuk.",
            "execution": "Pilih ion Ca2+ berikatan dengan troponin C menggeser tropomiosin membuka binding site aktin."
        }
    },
    {
        "id": "bio-lat-m-19",
        "materi": "SISTEM IMUNITAS ADAPTIF",
        "topic": "Pengenalan Antigen oleh Sel T Helper (MHC II) vs Sel T Sitotoksik (MHC I)",
        "stem": "Dalam sistem imun spesifik, sel T penolong ($\\text{T helper} / \\text{CD4}^+$) dan sel T sitotoksik ($\\text{CTL} / \\text{CD8}^+$) mengenali fragmen antigen yang dipresentasikan di permukaan sel inang melalui molekul Mayor Histocompatibility Complex (MHC). Perbedaan target pengenalan antara kedua jenis limfosit T tersebut adalah...",
        "correct": "Sel T $\\text{CD4}^+$ mengenali antigen eksogen yang dipresentasikan oleh molekul $\\text{MHC Kelas II}$ pada sel penyaji antigen (APC seperti sel dendritik, makrofag, sel B); sedangkan sel T $\\text{CD8}^+$ mengenali antigen endogen (seperti virus/kanker) yang dipresentasikan oleh $\\text{MHC Kelas I}$ pada semua sel tubuh berinti.",
        "distractors": [
            "Sel T CD4+ mengenali molekul glukosa bebas dalam darah, sedangkan sel T CD8+ hanya mengenali antigen bakteri tanpa melibatkan molekul MHC.",
            "MHC Kelas I hanya terdapat pada sel darah merah tanpa inti, sedangkan MHC Kelas II terdapat pada sel saraf otak saja.",
            "Sel T CD8+ memproduksi antibodi terlarut, sedangkan sel T CD4+ menelan bakteri secara fagositosis utuh.",
            "Sel T CD4+ menghancurkan MHC Kelas II sedangkan sel T CD8+ mensintesis molekul komplemen di hati."
        ],
        "formula": {
            "title": "KAIDAH INTERAKSI LIMFOSIT T DENGAN MOLEKUL MHC",
            "latex": "\\text{Kaidah Aturan 8:} \\quad \\text{CD4} \\times \\text{MHC II} = 8; \\quad \\text{CD8} \\times \\text{MHC I} = 8",
            "legend": "• $\\text{CD4}^+$ mengikat $\\text{MHC II}$ (antigen eksogen yang difagositosis oleh APC)<br>• $\\text{CD8}^+$ mengikat $\\text{MHC I}$ (antigen intraseluler pada semua sel berinti)<br>• Aktivasi $\\text{CD4}^+$ memicu pelepasan sitokin interleukinergik"
        },
        "hints": {
            "concept": "Gunakan aturan perkalian 8: CD4 x MHC II = 8 (T helper kenali APC); CD8 x MHC I = 8 (T sitotoksik kenali semua sel berinti).",
            "execution": "Pilih CD4+ mengenali MHC II pada APC dan CD8+ mengenali MHC I pada semua sel berinti."
        }
    },
    {
        "id": "bio-lat-m-20",
        "materi": "GENETIKA POPULASI (HARDY-WEINBERG)",
        "topic": "Perhitungan Frekuensi Pembawa Sifat (Carrier) Penyakit Resesif",
        "stem": "Dalam suatu populasi manusia yang beranggotakan $10.000$ orang dan berada dalam kesetimbangan Hardy-Weinberg, terdapat 16 orang yang menderita albino (kelainan terpaut autosom resesif, $aa$). Jumlah individu di dalam populasi tersebut yang normal tetapi membawa sifat albino (heterozigot / $\\textit{carrier}$, $Aa$) diperkirakan sebanyak...",
        "correct": "$768$ orang, karena frekuensi homozigot resesif $q^2 = \\frac{16}{10.000} = 0{,}0016$, sehingga frekuensi alel resesif $q = \\sqrt{0{,}0016} = 0{,}04$. Karena $p + q = 1$, maka frekuensi alel dominan $p = 1 - 0{,}04 = 0{,}96$. Frekuensi heterozigot adalah $2pq = 2 \\times 0{,}96 \\times 0{,}04 = 0{,}0768$ ($7{,}68\\%$). Jumlah individu carrier adalah $0{,}0768 \\times 10.000 = 768\\text{ orang}$.",
        "distractors": [
            "9.216 orang, yang merupakan jumlah individu normal homozigot dominan (AA).",
            "384 orang, dihitung jika lupa mengalikan perkalian alel dengan koefisien dua pada rumus 2pq.",
            "160 orang, dihitung dari asumsi rasio linear persentase penderita albino.",
            "9.984 orang, yang merupakan jumlah total seluruh individu berfenotipe normal gabungan homozigot dan heterozigot."
        ],
        "formula": {
            "title": "PERHITUNGAN FREKUENSI GENOTIPE HARDY-WEINBERG",
            "latex": "q^2 = \\frac{16}{10.000} = 0{,}0016 \\implies q = 0{,}04; \\quad p = 1 - 0{,}04 = 0{,}96; \\quad 2pq = 2(0{,}96)(0{,}04) = 0{,}0768; \\quad N_{Aa} = 0{,}0768 \\times 10.000 = 768",
            "legend": "• $q^2 = 0{,}0016$ (Penderita albino $aa$)<br>• $p^2 = (0{,}96)^2 = 0{,}9216$ (Normal homozigot $AA = 9.216\\text{ orang}$)<br>• $2pq = 768\\text{ orang}$ (Carrier $Aa$)<br>• Total populasi: $9.216 + 768 + 16 = 10.000\\text{ orang}$"
        },
        "hints": {
            "concept": "Cari q dulu dari q^2 = 16/10.000 = 0,0016 -> q = 0,04. Lalu p = 1 - 0,04 = 0,96. Jumlah carrier = 2pq * total populasi.",
            "execution": "2pq = 2 * 0,96 * 0,04 = 0,0768. Jumlah carrier = 0,0768 * 10.000 = 768 orang."
        }
    },
    {
        "id": "bio-lat-m-21",
        "materi": "BIOTEKNOLOGI MOLEKULER (PCR)",
        "topic": "Tiga Siklus Suhu Termal pada Reaksi Berantai Polimerase (PCR)",
        "stem": "Polymerase Chain Reaction (PCR) adalah metode amplifikasi jutaan salinan segmen DNA target secara in vitro. Satu siklus PCR terdiri atas tiga tahap perubahan suhu termal berurutan. Urutan tahapan suhu yang benar beserta peristiwa molekuler yang terjadi pada setiap tahap adalah...",
        "correct": "1. Denaturasi ($\\sim 94-96^\\circ\\text{C}$): Pemutusan ikatan hidrogen untuk memisahkan heliks ganda DNA menjadi dua untai tunggal;<br>2. Penempelan / Annealing ($\\sim 50-65^\\circ\\text{C}$): Penempelan primer oligonukleotida pada sekuens komplemen untai tunggal DNA;<br>3. Pemanjangan / Elongasi ($\\sim 72^\\circ\\text{C}$): Sintesis untai DNA baru oleh enzim termostabil Taq DNA polimerase.",
        "distractors": [
            "1. Hibridisasi ($72^\circ\\text{C}$); 2. Denaturasi enzim ($50^\circ\\text{C}$); 3. Isolasi plasmid ($95^\circ\\text{C}$).",
            "1. Annealing ($95^\circ\\text{C}$); 2. Elongasi ($4^\circ\\text{C}$); 3. Pembekuan DNA ($72^\circ\\text{C}$).",
            "1. Transkripsi ($60^\circ\\text{C}$); 2. Translasi ($90^\circ\\text{C}$); 3. Replikasi RNA ($37^\circ\\text{C}$).",
            "1. Sentrifugasi ($100^\circ\\text{C}$); 2. Elektroforesis ($72^\circ\\text{C}$); 3. Pemotongan restriksi ($55^\circ\\text{C}$)."
        ],
        "formula": {
            "title": "SIKLUS TERMAL AMPLIFIKASI PCR",
            "latex": "\\text{Amplifikasi Eksponensial: } N_t = N_0 \\times 2^n \\quad (n = \\text{jumlah siklus})",
            "legend": "• Denaturasi: $95^\\circ\\text{C}$ (memisahkan utas ganda)<br>• Annealing: $55^\\circ\\text{C}$ (primer menempel spesifik)<br>• Elongasi: $72^\\circ\\text{C}$ (aktivitas optimal DNA polimerase dari bakteri termofilik $\\textit{Thermus aquaticus}$)"
        },
        "hints": {
            "concept": "Urutan suhu PCR: Denaturasi (~95 C, buka pita DNA), Annealing (~55 C, primer nempel), Elongasi (~72 C, enzim Taq polimerase bekerja memanjangkan DNA).",
            "execution": "Pilih Denaturasi (94-96 C) -> Annealing (50-65 C) -> Elongasi (72 C)."
        }
    },
    {
        "id": "bio-lat-m-22",
        "materi": "BIOTEKNOLOGI MEDIS (HIBRIDOMA)",
        "topic": "Pembuatan Antibodi Monoklonal melalui Fusi Sel Hibridoma",
        "stem": "Antibodi monoklonal yang digunakan dalam imunoterapi target kanker dan tes diagnostik (seperti rapid test) diproduksi melalui teknologi hibridoma. Sel hibridoma dibuat dengan menggabungkan dua jenis sel, yaitu...",
        "correct": "Sel limfosit B mencit yang telah diimunisasi antigen (penghasil antibodi spesifik) dengan sel kanker mieloma (memiliki sifat membelah diri tanpa batas / immortal).",
        "distractors": [
            "Sel darah merah manusia dengan sel bakteri $\\textit{Escherichia coli}$ penghasil enzim restriksi.",
            "Sel limfosit T sitotoksik dengan sel ragi $\\textit{Saccharomyces}$ pembentuk dinding selulosa.",
            "Sel punca embrionik dengan sel sperma mamalia yang diradiasi sinar gamma intensitas tinggi.",
            "Sel makrofag monosit dengan sel virus influenza yang telah dinonaktifkan."
        ],
        "formula": {
            "title": "PRINSIP TEKNOLOGI HIBRIDOMA KÖHLER & MILSTEIN",
            "latex": "\\text{Sel B Imun} \\ (\\text{Penghasil Antibodi}) + \\text{Sel Mieloma} \\ (\\text{Abadi/Kanker}) \\xrightarrow{\\text{PEG}} \\text{Sel Hibridoma} \\implies \\text{Antibodi Monoklonal}",
            "legend": "• Seleksi media HAT (Hipoxantin, Aminopterin, Timidin) menyaring hanya sel fusi yang hidup<br>• Menghasilkan antibodi seragam yang mengikat satu epitop spesifik tunggal<br>• Dianugerahi Hadiah Nobel Fisiologi atau Kedokteran 1984"
        },
        "hints": {
            "concept": "Hibridoma adalah fusi sel B (yang membuat antibodi spesifik) dengan sel mieloma/kanker (yang membelah terus-menerus/imortal).",
            "execution": "Pilih sel limfosit B dengan sel kanker mieloma."
        }
    },
    {
        "id": "bio-lat-m-23",
        "materi": "EKOLOGI SUKSESI",
        "topic": "Perbedaan Suksesi Primer dan Suksesi Sekunder",
        "stem": "Pasca letusan dahsyat gunung berapi pulau Krakatau tahun 1883, seluruh permukaan pulau tertutup lelehan lava pijar beku yang memusnahkan seluruh kehidupan dan lapisan tanah tanpa menyisakan bahan organik sama sekali. Proses kolonisasi dan perkembangan komunitas hayati baru yang terjadi di pulau tersebut merupakan contoh...",
        "correct": "Suksesi primer, karena diawali dari substrat batuan anorganik tandus tanpa tanah; dimulai dari organisme perintis (seperti lumut kerak / $\\textit{lichen}$ dan lumut kerak biru-hijau) yang melapukkan batu menjadi tanah hingga akhirnya terbentuk komunitas klimaks.",
        "distractors": [
            "Suksesi sekunder, karena letusan gunung hanya mematikan vegetasi pohon tanpa merusak komunitas mikroba tanah asal.",
            "Degradasi klimaks permanen, di mana ekosistem tidak akan pernah mampu dihuni kembali oleh makhluk hidup.",
            "Biomagnifikasi ekologis, di mana polutan logam berat terkonsentrasi di puncak rantai makanan pulau.",
            "Evolusi konvergen habitat, di mana tanaman darat berubah menjadi terumbu karang laut dalam."
        ],
        "formula": {
            "title": "SUKSESI PRIMER VS SUKSESI SEKUNDER",
            "latex": "\\begin{aligned} \\text{Suksesi Primer:} & \\quad \\text{Substrat Baru Tanpa Tanah} \\to \\text{Perintis (Lichen)} \\to \\text{Rumput} \\to \\text{Semak} \\to \\text{Hutan Klimaks} \\\\ \\text{Suksesi Sekunder:} & \\quad \\text{Gangguan (Kebakaran, Banjir)} \\to \\text{Tanah & Benih Tetap Ada} \\to \\text{Pemulihan Lebih Cepat} \\end{aligned}",
            "legend": "• Letusan Krakatau menghancurkan seluruh lapisan tanah $\\implies$ Suksesi Primer<br>• Organisme perintis membentuk tanah humus awal dari pelapukan batuan lava<br>• Suksesi membutuhkan waktu puluhan hingga ratusan tahun mencapai klimaks"
        },
        "hints": {
            "concept": "Jika gangguan menghancurkan seluruh tanah hingga hanya tersisa batuan tandus (seperti lahar beku Krakatau), itu adalah suksesi primer (dimulai oleh lumut kerak perintis).",
            "execution": "Pilih suksesi primer yang dimulai dari organisme perintis."
        }
    },
    {
        "id": "bio-lat-m-24",
        "materi": "MEKANISME SPESIASI & EVOLUSI",
        "topic": "Spesiasi Alopatrik Akibat Isolasi Geografis",
        "stem": "Terbentuknya dua spesies tupai tanah yang berbeda di tebing utara ($\\textit{Ammospermophilus harrisii}$) dan tebing selatan ($\\textit{Ammospermophilus leucurus}$) ngarai Grand Canyon merupakan contoh klasik spesiasi alopatrik. Mekanisme evolusi yang mendorong terbentuknya dua spesies baru tersebut adalah...",
        "correct": "Penghalang geografis fisik (ngarai yang dalam) memisahkan satu populasi leluhur menjadi dua populasi terisolasi, menghentikan aliran gen ($\\textit{gene flow}$), sehingga kedua populasi mengalami mutasi independen, seleksi alam terhadap lingkungan lokal, dan hanyutan genetik hingga terjadi isolasi reproduksi.",
        "distractors": [
            "Kedua populasi kawin silang secara intensif setiap musim semi menghasilkan spesies poliploidi mandul.",
            "Tupai tebing utara bermutasi menjadi karnivora pemangsa tupai tebing selatan.",
            "Terjadi kepunahan massal akibat meteorit yang hanya jatuh di dasar sungai ngarai.",
            "Kedua populasi tetap memiliki aliran gen bebas tanpa hambatan reproduksi morfologis."
        ],
        "formula": {
            "title": "TAHAPAN SPESIASI ALOPATRIK",
            "latex": "\\text{Populasi Tunggal} \\xrightarrow{\\text{Barier Geografis}} \\text{Aliran Gen Terputus} \\xrightarrow{\\text{Seleksi & Drift Berbeda}} \\text{Isolasi Reproduksi} \\implies 2\\text{ Spesies Baru}",
            "legend": "• Alopatrik: Terjadi di tempat berbeda karena barier fisik (sungai, gunung, ngarai)<br>• Simpatrik: Terjadi di area geografis yang sama (misal poliploidi pada tumbuhan)<br>• Uji akhir spesies: Jika barier hilang, keduanya tidak dapat menghasilkan keturunan fertil"
        },
        "hints": {
            "concept": "Spesiasi alopatrik dipicu oleh pemisahan geografis (ngarai/sungai). Aliran gen terhenti, mutasi dan seleksi alam lokal bekerja terpisah, hingga akhirnya terbentuk isolasi reproduksi.",
            "execution": "Pilih penghalang geografis menghentikan aliran gen memicu isolasi reproduksi."
        }
    },
    {
        "id": "bio-lat-m-25",
        "materi": "JARINGAN & ANATOMI TUMBUHAN",
        "topic": "Diferensiasi Kambium Vaskular pada Batang Dikotil",
        "stem": "Aktivitas pertumbuhan sekunder meristem lateral (kambium vaskular) pada batang tumbuhan dikotil berkayu menyebabkan pertambahan diameter batang setiap tahunnya. Arah pembelahan sel-sel kambium vaskular dan jaringan yang dihasilkannya adalah...",
        "correct": "Membelah ke arah dalam membentuk xilem sekunder (kayu), dan membelah ke arah luar membentuk floem sekunder (kulit kayu bagian dalam); aktivitas ke arah dalam lebih aktif daripada ke arah luar.",
        "distractors": [
            "Membelah ke arah dalam membentuk epidermis berstomata, dan ke arah luar membentuk kambium gabus pelindung.",
            "Membelah ke arah dalam membentuk floem primer, dan membelah ke arah luar membentuk endodermis kedap air.",
            "Membelah ke arah luar membentuk empulur parenkim spons, dan ke arah dalam membentuk stomata lentisel.",
            "Membelah ke arah samping membentuk kolenkim dan sklerenkim serat tanpa menghasilkan pembuluh angkut."
        ],
        "formula": {
            "title": "AKTIVITAS KAMBIUM VASKULAR PADA BATANG DIKOTIL",
            "latex": "\\text{Kambium Vaskular} \\implies \\begin{cases} \\text{Ke Arah Dalam} & \\to \\text{Xilem Sekunder (Lingkaran Tahun)} \\\\ \\text{Ke Arah Luar} & \\to \\text{Floem Sekunder} \\end{cases}",
            "legend": "• Xilem sekunder menyusun sebagian besar kayu batang<br>• Perbedaan curah hujan musiman memicu lebar lingkaran tahun berbeda<br>• Felogen (kambium gabus) membelah ke luar membentuk felem (gabus) dan ke dalam membentuk feloderm"
        },
        "hints": {
            "concept": "Kambium vaskular: membelah ke dalam membentuk xilem sekunder (kayu), membelah ke luar membentuk floem sekunder (kulit kayu). Pertumbuhan ke dalam lebih cepat.",
            "execution": "Pilih membelah ke dalam membentuk xilem sekunder dan ke luar membentuk floem sekunder."
        }
    }
]
