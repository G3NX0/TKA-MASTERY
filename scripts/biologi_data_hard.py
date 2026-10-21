# -*- coding: utf-8 -*-
"""
TKA 2026 - PUSMENDIK KEMENDIKDASMEN
Mata Pelajaran Pilihan: Biologi (SMA/MA Saintek)
Dataset: Latihan Tingkat Hard (25 Authentic Questions, bio-lat-h-01 to 25)
Standards: BSKAP No. 033/H/KR/2024 & Pusmendik CBT HOTS Framework
"""

BIOLOGI_HARD_ITEMS = [
    {
        "id": "bio-lat-h-01",
        "materi": "RESPIRASI SELULER & BIOENERGETIKA",
        "topic": "Efek Racun Sianida vs Uncoupler DNP pada Rantai Transpor Elektron",
        "stem": "Dalam penelitian metabolisme seluler, dua zat kimia beracun diberikan pada suspensi mitokondria terisolasi:<br>• Senyawa $A$ (Sianida / $\\text{CN}^-$): Menghambat kerja enzim sitokrom $c$ oksidase (Kompleks IV) secara ireversibel.<br>• Senyawa $B$ (2,4-Dinitrofenol / DNP): Bertindak sebagai ionofor proton lipofilik yang membawa ion $\\text{H}^+$ melintasi membran dalam mitokondria tanpa melalui ATP Sintase ($\\textit{uncoupler}$).<br>Efek metabolik yang teramati terhadap konsumsi oksigen ($\\text{O}_2$) dan sintesis $\\text{ATP}$ pada masing-masing perlakuan adalah...",
        "correct": "Senyawa $A$ menghentikan konsumsi $\\text{O}_2$ dan menghentikan sintesis $\\text{ATP}$; sedangkan Senyawa $B$ meningkatkan laju konsumsi $\\text{O}_2$ disertai penghentian sintesis $\\text{ATP}$ (energi dilepaskan sebagai panas / termogenesis berlebih).",
        "distractors": [
            "Kedua senyawa sama-sama menghentikan konsumsi oksigen dan melipatgandakan sintesis ATP sebesar sepuluh kali lipat.",
            "Senyawa A meningkatkan konsumsi oksigen, sedangkan Senyawa B menurunkan suhu sel menjadi beku mutlak.",
            "Senyawa A memicu fermentasi asam sitrat di dalam krista, sedangkan Senyawa B mengubah glukosa menjadi glikogen secara spontan.",
            "Senyawa B memblokir Kompleks I sedangkan Senyawa A memutar balik rotor ATP Sintase memproduksi glukosa."
        ],
        "formula": {
            "title": "MEKANISME PENGHAMBATAN VS DISSIPASI PROTON TRANSFOR ELEKTRON",
            "latex": "\\begin{aligned} \\text{Sianida (CN}^-\\text{):} & \\quad \\text{Inhibisi Kompleks IV} \\implies \\text{Aliran } e^- \\text{ Macet} \\implies \\text{Konsumsi O}_2 = 0, \\ \\text{Sintesis ATP} = 0 \\\\ \\text{DNP (Uncoupler):} & \\quad \\text{Disipasi Gradien H}^+ \\implies \\text{Aliran } e^- \\text{ Maksimal (Konsumsi O}_2 \\uparrow), \\ \\text{ATP Sintase Mati} \\implies \\Delta H \\text{ (Panas)} \\end{aligned}",
            "legend": "• Kompleks IV mentransfer elektron ke $\\text{O}_2$; inhibisi $\\text{CN}^-$ mematikan rantai pernapasan total<br>• DNP merusak gradien kemiosmosis Mitchell tanpa memblokir rantai transpor elektron<br>• Menjelaskan mengapa keracunan DNP menyebabkan hipertermia fatal"
        },
        "hints": {
            "concept": "Sianida memblokir transfer elektron ke O2 pada kompleks IV (konsumsi O2 berhenti, ATP berhenti). DNP adalah uncoupler yang membocorkan gradien H+ (transpor elektron bekerja kencang membakar O2, tapi ATP tidak terbentuk, energi jadi panas).",
            "execution": "Pilih: Sianida menghentikan O2 dan ATP; DNP meningkatkan O2 dan menghentikan ATP (termogenesis)."
        }
    },
    {
        "id": "bio-lat-h-02",
        "materi": "REGULASI METABOLISME & ALOSTERIK",
        "topic": "Regulasi Alosterik Enzim Fosfofruktokinase-1 (PFK-1) pada Glikolisis",
        "stem": "Enzim fosfofruktokinase-1 (PFK-1) merupakan enzim penentu laju ($\\textit{committed step}$) yang mengkatalisis fosforilasi fruktosa-6-fosfat menjadi fruktosa-1,6-bisfosfat dalam jalur glikolisis. Ketika muatan energi seluler sangat tinggi (konsentrasi ATP sel melimpah dan siklus asam sitrat jenuh oleh sitrat), aktivitas enzim PFK-1 akan...",
        "correct": "Dihambat secara alosterik oleh ATP berkonsentrasi tinggi dan sitrat; ATP berikatan pada situs alosterik berafinitas rendah menurunkan afinitas PFK-1 terhadap substratnya sehingga glikolisis diperlambat untuk mencegah pemborosan bahan bakar glukosa.",
        "distractors": [
            "Ditingkatkan secara masif oleh ATP untuk mempercepat penimbunan asam laktat di mitokondria.",
            "Dihidrolisis menjadi asam amino bebas oleh sitrat sehingga reaksi glikolisis berjalan irreversibel.",
            "Diaktifkan oleh kelebihan sitrat untuk memicu sintesis asam nukleat DNA dalam sitoplasma.",
            "Mengubah fruktosa menjadi amilum kristal yang disimpan permanen di dalam lisosom."
        ],
        "formula": {
            "title": "REGULASI ALOSTERIK ENZIM PFK-1 GLIKOLISIS",
            "latex": "\\text{Aktivator Alosterik: AMP, ADP, Fruktosa-2,6-bisfosfat} \\quad \\iff \\quad \\text{Inhibitor Alosterik: ATP Konsentrasi Tinggi, Sitrat}",
            "legend": "• PFK-1 memiliki 2 situs pengikatan ATP: situs katalitik (afinitas tinggi) dan situs regulasi alosterik (afinitas rendah)<br>• Fruktosa-2,6-bisfosfat adalah aktivator paling poten yang diproduksi saat hormon insulin tinggi<br>• Contoh klasik umpan balik negatif (feedback inhibition) seluler"
        },
        "hints": {
            "concept": "PFK-1 adalah enzim pengatur utama glikolisis. Jika energi sel sudah melimpah (ATP dan sitrat tinggi), keduanya bertindak sebagai inhibitor alosterik untuk mengerem glikolisis.",
            "execution": "Pilih dihambat secara alosterik oleh ATP tinggi dan sitrat."
        }
    },
    {
        "id": "bio-lat-h-03",
        "materi": "FOTOSINTESIS & FOTORESPIRASI (JALUR C2)",
        "topic": "Aktivitas Oksigenase Rubisco dan Biokimia Fotorespirasi",
        "stem": "Enzim Rubisco (Ribulosa-1,5-bisfosfat karboksilase/oksigenase) memiliki sisi aktif yang mampu mengikat $\\text{CO}_2$ maupun $\\text{O}_2$ secara kompetitif. Pada kondisi cuaca panas terik ketika stomata tanaman $C_3$ menutup untuk mencegah transpirasi sehingga rasio $[\text{O}_2]/[\text{CO}_2]$ di mesofil meningkat, Rubisco mengikat oksigen memicu jalur fotorespirasi. Senyawa awal yang dihasilkan dan organel yang terlibat dalam siklus daur ulang karbon fotorespirasi adalah...",
        "correct": "Terbentuk 1 molekul 3-PGA ($3\\text{C}$) dan 1 molekul 2-fosfoglikolat ($2\\text{C}$); daur ulang senyawa fosfoglikolat menjadi 3-PGA melibatkan kerja sama terkoordinasi tiga organel seluler: Kloroplas, Peroksisom, dan Mitokondria, dengan mengonsumsi ATP dan melepaskan $\\text{CO}_2$.",
        "distractors": [
            "Terbentuk 2 molekul glukosa bebas; proses daur ulang berlangsung murni di dalam vakuola dan badan Golgi.",
            "Terbentuk gas metana dan amonia; berlangsung di dalam ribosom dan sentriol tanpa mengonsumsi energi.",
            "Terbentuk asam piruvat dan asetil Ko-A; proses berlangsung di dinding selulosa dan retikulum endoplasma halus.",
            "Terbentuk asam malat dan PEP; berlangsung di seludang pembuluh tanpa melibatkan peroksisom."
        ],
        "formula": {
            "title": "REAKSI OKSIGENASE RUBISCO & JALUR C2 FOTORESPIRASI",
            "latex": "\\text{RuBP } (5\\text{C}) + \\text{O}_2 \\xrightarrow{\\text{Rubisco}} 3\\text{-PGA } (3\\text{C}) + 2\\text{-Fosfoglikolat } (2\\text{C}) \\xrightarrow{\\text{Kloroplas } \\to \\text{ Peroksisom } \\to \\text{ Mitokondria}} \\text{Pelepasan CO}_2",
            "legend": "• Fotorespirasi merugikan tumbuhan karena menyia-nyiakan hingga $25-50\\%$ energi hasil fotosintesis tanpa menghasilkan ATP atau gula<br>• Peroksisom mengubah glikolat menjadi glioksilat dan menghasilkan $\\text{H}_2\\text{O}_2$ (diurai katalase)<br>• Mitokondria melepaskan $\\text{CO}_2$ dan $\\text{NH}_3$ pada konversi 2 glisin $\\to$ serin"
        },
        "hints": {
            "concept": "Rubisco + O2 menghasilkan 3-PGA (3C) dan 2-fosfoglikolat (2C). Daur ulang glikolat (jalur C2) melibatkan 3 organel: Kloroplas -> Peroksisom -> Mitokondria.",
            "execution": "Pilih 3-PGA dan 2-fosfoglikolat dengan keterlibatan Kloroplas, Peroksisom, dan Mitokondria."
        }
    },
    {
        "id": "bio-lat-h-04",
        "materi": "EKSPRESI GEN & PEMROSESAN RNA EUKARIOTIK",
        "topic": "Pematangan Pra-mRNA: Capping, Polyadenylation, dan Splicing Alternatif",
        "stem": "Transkrip primer (pre-mRNA) eukariotik di dalam nukleus harus mengalami modifikasi pascatranskripsi sebelum diekspor ke sitoplasma untuk translasi. Fenomena di mana satu gen tunggal mampu mengkode beberapa varian protein (isoform) yang berbeda fungsinya dalam jaringan tubuh yang berlainan dimungkinkan oleh mekanisme...",
        "correct": "Splicing alternatif ($\\textit{alternative RNA splicing}$); kompleks spliceosome memotong intron dan menggabungkan ekson-ekson dalam kombinasi yang berbeda-beda dari satu transkrip pre-mRNA yang sama.",
        "distractors": [
            "Mutasi titik spontan yang secara teratur mengubah kodon stop menjadi asam amino triptofan.",
            "Penambahan tudung 7-metilguanosin pada ujung 3' secara acak oleh enzim DNA polimerase.",
            "Penggandaan kromosom somatik secara poliploidi pada setiap diferensiasi sel organ.",
            "Replikasi DNA secara semikonservatif yang menyisipkan sekuens transposon retrovirus."
        ],
        "formula": {
            "title": "PEMROSESAN PRE-MRNA & ALTERNATIVE SPLICING",
            "latex": "\\text{Pre-mRNA: } [\\text{Cap 5}']-\\text{E1-I1-E2-I2-E3}-[\\text{Poly-A 3}'] \\xrightarrow{\\text{Spliceosome}} \\begin{cases} \\text{Isoform A: } \\text{E1-E2-E3} \\\\ \\text{Isoform B: } \\text{E1-E3} \\end{cases}",
            "legend": "• Tudung $5'$ ($7\\text{-metilguanosin}$): Melindungi dari degradasi eksonuklease & sinyal inisiasi ribosom<br>• Ekor Poly-A $3'$ ($100-250\\text{ residu A}$): Memfasilitasi ekspor nukleus & stabilitas translasi<br>• Alternative splicing menjelaskan mengapa $\\sim 20.000$ gen manusia dapat menghasilkan $> 100.000$ protein berbeda"
        },
        "hints": {
            "concept": "Satu gen dapat menghasilkan beberapa jenis protein berbeda melalui pemotongan intron dan penyambungan kombinasi ekson yang berbeda-beda. Ini disebut penyambungan alternatif (alternative splicing).",
            "execution": "Pilih splicing alternatif (alternative RNA splicing) oleh kompleks spliceosome."
        }
    },
    {
        "id": "bio-lat-h-05",
        "materi": "EPIGENETIKA & KROMATIN",
        "topic": "Pengaruh Metilasi DNA dan Asetilasi Histon terhadap Transkripsi Gen",
        "stem": "Modifikasi epigenetik mengatur aksesibilitas kromatin terhadap faktor transkripsi tanpa mengubah urutan basa nitrogen DNA. Kombinasi modifikasi epigenetik yang paling kuat diasosiasikan dengan penonaktifan ekspresi gen (pembungkaman gen / $\\textit{gene silencing}$) dan pemadatan kromatin menjadi heterokromatin adalah...",
        "correct": "Hipermetilasi DNA pada residu sitosin di pulau CpG ($\\textit{CpG islands}$) dan deasetilasi ekor protein histon (oleh enzim Histone Deacetylase / HDAC).",
        "distractors": [
            "Hipometilasi DNA total disertai hiperasetilasi ekor histon oleh Histone Acetyltransferase (HAT).",
            "Fosforilasi ikatan fosfodiester DNA oleh enzim RNA polimerase pada daerah promotor gen.",
            "Pemutusan ikatan hidrogen antaruntai heliks ganda DNA secara enzimatik permanen.",
            "Penyisipan gugus sulfat pada basa timin yang memicu pembukaan struktur heliks ganda menjadi eukromatin."
        ],
        "formula": {
            "title": "KODE HISTON & STATUS REGULASI EPIGENETIK",
            "latex": "\\begin{aligned} \\text{Heterokromatin (Gen Tidak Aktif):} & \\quad \\text{Metilasi DNA } \\uparrow + \\text{Deasetilasi Histon (HDAC)} \\implies \\text{Kromatin Padat Tertutup} \\\\ \\text{Eukromatin (Gen Aktif Ditranskripsi):} & \\quad \\text{Demetilasi DNA } \\downarrow + \\text{Asetilasi Histon (HAT)} \\uparrow \\implies \\text{Kromatin Longgar Terbuka} \\end{aligned}",
            "legend": "• Metilasi sitosin membentuk $5\\text{-metilsitosin}$ menarik protein pengikat metil (MBD)<br>• Deasetilasi mengembalikan muatan positif lisin pada histon $\\implies$ mengikat erat fosfat DNA negatif<br>• Berperan penting dalam diferensiasi seluler, inaktivasi kromosom X, dan karsinogenesis"
        },
        "hints": {
            "concept": "Gene silencing (gen mati): DNA termetilasi tinggi (hipermetilasi CpG) dan histon terdeasetilasi (HDAC), membuat kromatin padat mengunci akses RNA polimerase. Sebaliknya, asetilasi membuka kromatin.",
            "execution": "Pilih hipermetilasi DNA pada CpG dan deasetilasi histon (HDAC)."
        }
    },
    {
        "id": "bio-lat-h-06",
        "materi": "REKAYASA GENETIKA MODERN (CRISPR-CAS9)",
        "topic": "Peran Single Guide RNA (sgRNA) dan Motif PAM pada Pengeditan Gen",
        "stem": "Teknologi penyuntingan genom presisi CRISPR-Cas9 diadaptasi dari sistem imun adaptif bakteri terhadap bakteriofag. Enzim endonuklease Cas9 dipandu oleh molekul $\\textit{single guide RNA}$ (sgRNA) untuk memotong untai ganda DNA target ($\\textit{double-strand break / DSB}$). Syarat mutlak pada DNA target agar enzim Cas9 dapat mengenali, menempel, dan memotong sekuens DNA komplemen target adalah...",
        "correct": "Adanya sekuens pendek Protospacer Adjacent Motif (PAM, urutan spesifik $5'\\text{-NGG-}3'$) yang terletak tepat di sebelah hilir (arah 3') dari sekuens protospacer target pada untai DNA non-komplemen.",
        "distractors": [
            "Adanya sekuens promotor TATA box yang berjarak persis sepuluh pasang basa dari kodon inisiasi AUG.",
            "Adanya primer RNA oligonukleotida yang disintesis sebelumnya oleh enzim primase mitokondria.",
            "Target DNA harus berupa untai tunggal yang telah dipanaskan hingga suhu denaturasi $95^\circ\\text{C}$.",
            "Daerah target harus berada di ujung telomer kromosom dan memiliki panjang minimal 10.000 pasang basa."
        ],
        "formula": {
            "title": "MEKANISME PENGENALAN TARGET CRISPR-CAS9",
            "latex": "\\text{DNA Target} + \\text{PAM } (5'\\text{-NGG-}3') \\xleftarrow{\\text{sgRNA spacer } (20\\text{ nt})} \\text{Cas9 Endonuklease} \\implies \\text{DSB } (3\\text{ bp upstream PAM})",
            "legend": "• Tanpa PAM ($5'\\text{-NGG-}3'$), Cas9 tidak dapat membuka heliks ganda DNA target<br>• PAM mencegah bakteri memotong lokus CRISPR-nya sendiri (mekanisme self vs non-self)<br>• Pemotongan untai ganda diperbaiki sel via NHEJ (mutasi knockout) atau HDR (insersi gen presisi)"
        },
        "hints": {
            "concept": "Cas9 membutuhkan motif PAM (Protospacer Adjacent Motif, yaitu sekuens 5'-NGG-3') tepat di samping sekuens target untuk bisa menempel dan memotong untai ganda DNA.",
            "execution": "Pilih adanya sekuens Protospacer Adjacent Motif (PAM, 5'-NGG-3')."
        }
    },
    {
        "id": "bio-lat-h-07",
        "materi": "PENYIMPANGAN SEMU MENDEL (GEN KOMPLEMENTER)",
        "topic": "Persilangan Gen Komplementer Bunga Lathyrus odoratus (Rasio 9 : 7)",
        "stem": "Pada tanaman kacang manis $\\textit{Lathyrus odoratus}$, warna ungu pada bunga ditentukan oleh kerja sama dua gen komplementer: gen $C$ (mengkode enzim aktivator prekursor pigmen) dan gen $P$ (mengkode enzim pengubah kromogen menjadi antosianin ungu). Jika salah satu atau kedua gen dominan tersebut tidak hadir (genotipe $C\\_pp$, $ccP\\_$, atau $ccpp$), bunga akan berwarna putih. Jika tanaman berbunga ungu heterozigot ganda ($CcPp$) disilangkan dengan sesamanya menghasilkan 320 bibit tanaman, jumlah tanaman yang menghasilkan bunga berwarna putih adalah...",
        "correct": "140 tanaman, karena persilangan dihibrid heterozigot ganda ($CcPp \\times CcPp$) pada gen komplementer menghasilkan rasio fenotipe $9\\text{ Ungu } (C\\_P\\_) : 7\\text{ Putih } (C\\_pp, ccP\\_, ccpp)$. Fraksi tanaman berbunga putih adalah $\\frac{7}{16}$, sehingga jumlahnya adalah $\\frac{7}{16} \\times 320 = 140\\text{ tanaman}$.",
        "distractors": [
            "180 tanaman, yang merupakan jumlah tanaman berbunga ungu (9/16 dari 320).",
            "20 tanaman, dihitung jika hanya genotipe homozigot resesif ganda ccpp yang dianggap berwarna putih.",
            "80 tanaman, dihitung jika mengasumsikan rasio fenotipe satu banding tiga seperti monohibrid.",
            "160 tanaman, dihitung dari pembagian rata separuh tanaman ungu dan separuh putih."
        ],
        "formula": {
            "title": "PERSILANGAN GEN KOMPLEMENTER (RASIO 9 : 7)",
            "latex": "CcPp \\times CcPp \\implies \\begin{cases} 9\\text{ } C\\_P\\_ & \\to \\text{Ungu} \\\\ 3\\text{ } C\\_pp + 3\\text{ } ccP\\_ + 1\\text{ } ccpp = 7 & \\to \\text{Putih} \\end{cases} \\implies N_{\\text{putih}} = \\frac{7}{16} \\times 320 = 140",
            "legend": "• Kedua enzim $C$ dan $P$ harus fungsional agar jalur biosintesis pigmen ungu selesai<br>• Mutasi resesif pada salah satu gen memutus rantai reaksi biokimia $\\implies$ pigmen gagal terbentuk<br>• Rasio $9 : 7$ adalah modifikasi dari rasio dihibrid standar $9 : 3 : 3 : 1$"
        },
        "hints": {
            "concept": "Gen komplementer: Ungu = C_P_ (9/16). Putih = sisa kombinasi lainnya (7/16).",
            "execution": "Jumlah putih = (7 / 16) * 320 = 7 * 20 = 140 tanaman."
        }
    },
    {
        "id": "bio-lat-h-08",
        "materi": "PEMETAAN KROMOSOM (THREE-POINT TESTCROSS)",
        "topic": "Penentuan Urutan Gen Melalui Analisis Rekombinan Ganda",
        "stem": "Dalam persilangan uji tiga titik ($\\textit{three-point testcross}$) lalat buah $\\textit{Drosophila}$ untuk tiga gen tertaut autosom ($a, b, c$), diperoleh data fenotipe keturunan dengan frekuensi tertinggi adalah tipe parental ($a^+ b^+ c^+$ dan $a\\ b\\ c$), sedangkan fenotipe dengan frekuensi paling langka (rekombinan ganda / $\\textit{double crossover}$) adalah ($a^+ b\\ c^+$ dan $a\\ b^+\\ c$). Berdasarkan perbandingan antara alel parental dan rekombinan ganda, gen yang terletak di posisi tengah pada lokus kromosom adalah...",
        "correct": "Gen $b$, karena pada peristiwa pindah silang ganda (double crossover), hanya alel dari gen yang berada di posisi tengah yang tertukar relatif terhadap alel-alel dari kedua gen penanda di tepi (gen $b$ tertukar: $a^+$ berpasangan dengan $b$ dan $c^+$, serta $a$ berpasangan dengan $b^+$ dan $c$).",
        "distractors": [
            "Gen $a$, karena gen $a$ selalu dituliskan pertama kali dalam notasi alfabet genetika klasik.",
            "Gen $c$, karena gen $c$ terletak di ujung terminal kromatid yang paling mudah mengalami delesi.",
            "Ketiga gen terletak melingkar sehingga tidak memiliki konsep posisi tengah maupun tepi.",
            "Gen $b$ dan gen $a$ bertukar posisi secara acak pada setiap pembelahan mitosis somatik."
        ],
        "formula": {
            "title": "ATURAN PENENTUAN URUTAN GEN PADA THREE-POINT TESTCROSS",
            "latex": "\\text{Parental: } a^+ b^+ c^+ \\text{ & } a b c \\quad \\iff \\quad \\text{Double Crossover: } a^+ b c^+ \\text{ & } a b^+ c \\implies \\text{Gen } b \\text{ di tengah (Urutan: } a-b-c\\text{)}",
            "legend": "• Tipe parental memiliki frekuensi anakan tertinggi<br>• Tipe rekombinan ganda memiliki frekuensi anakan terendah<br>• Bandingkan DCO dengan parental: alel yang 'berbeda sendiri' berada di lokus tengah"
        },
        "hints": {
            "concept": "Bandingkan tipe DCO (frekuensi terkecil) dengan parental. Pada parental: a+ b+ c+ dan a b c. Pada DCO: a+ b c+ dan a b+ c. Perhatikan bahwa hanya alel b yang berpindah kubu. Maka lokus b berada di tengah.",
            "execution": "Urutan gen pada kromosom adalah a - b - c (gen b di tengah)."
        }
    },
    {
        "id": "bio-lat-h-09",
        "materi": "EPISTASIS RESESIF PADA MANUSIA",
        "topic": "Fenotipe Bombay (Interaksi Resesif Lokus H dengan Golongan Darah ABO)",
        "stem": "Fenotipe Bombay merupakan fenomena genetika langka di mana seorang individu secara serologis teruji bergolongan darah O, padahal kedua orang tuanya bergolongan darah AB ($I^A I^B$). Penjelasan genetik molekuler dari fenotipe Bombay tersebut adalah...",
        "correct": "Epistasis resesif oleh lokus gen $H$; individu tersebut homozigot resesif ($hh$) sehingga enzim fukosiltransferase inaktif dan tidak mampu membentuk substansi dasar antigen H pada membran eritrosit, akibatnya enzim glikosiltransferase $I^A$ dan $I^B$ tidak memiliki substrat untuk menempelkan gula penentu antigen A atau B.",
        "distractors": [
            "Terjadi mutasi delesi seluruh kromosom nomor 9 yang membawa lokus gen ABO pada sel telur ibu.",
            "Antibodi anti-A dan anti-B mengendapkan seluruh eritrosit sehingga menghasilkan darah transparan.",
            "Gen $I^A$ dan $I^B$ mengalami transkripsi terbalik menjadi molekul lipid glikogen di limpa.",
            "Individu tersebut memiliki golongan darah rhesus null yang menolak seluruh ikatan hemoglobin."
        ],
        "formula": {
            "title": "MEKANISME BIOKIMIA FENOTIPE BOMBAY (EPISTASIS HH)",
            "latex": "\\text{Prekursor Karbohidrat} \\xrightarrow{\\text{Gen } H \\ (hh: \\text{Gagal})} \\text{Substansi H} \\xrightarrow{\\text{Enzim } I^A / I^B} \\text{Antigen A / Antigen B}",
            "legend": "• Genotipe normal: $H\\_ I^A I^B \\implies$ Fenotipe AB<br>• Fenotipe Bombay: $hh I^A I^B \\implies$ Tidak ada antigen H, A, maupun B $\\implies$ Terbaca golongan O semu<br>• Plasma darah pasien Bombay mengandung antibodi anti-A, anti-B, dan anti-H (hanya bisa menerima transfusi dari sesama donor Bombay)"
        },
        "hints": {
            "concept": "Fenotipe Bombay adalah contoh epistasis resesif. Tanpa alel H dominan (genotipe hh), substansi H tidak terbentuk, sehingga antigen A dan B tidak bisa ditempelkan ke eritrosit, tampak seperti golongan O.",
            "execution": "Pilih epistasis resesif oleh lokus gen H (homozigot hh gagal membentuk substansi H)."
        }
    },
    {
        "id": "bio-lat-h-10",
        "materi": "GENETIKA POPULASI & SELEKSI ALAM",
        "topic": "Perubahan Frekuensi Alel Akibat Seleksi Melawan Homozigot Resesif Letal",
        "stem": "Dalam suatu populasi terisolasi yang semula berada dalam kesetimbangan dengan frekuensi alel resesif letal $q_0 = 0{,}20$ (seperti pada penyakit resesif mematikan di usia anak-anak sebelum reproduksi, koefisien seleksi $s = 1$). Jika seluruh individu homozigot resesif ($aa$) gagal bertahan hidup dan tidak menghasilkan keturunan sama sekali, frekuensi alel resesif pada generasi berikutnya ($q_1$) setelah satu generasi seleksi adalah...",
        "correct": "$q_1 = 0{,}167$ (atau $\\frac{1}{6}$), karena menurut persamaan seleksi genetik melawan alel resesif letal lengkap ($s = 1$): $q_1 = \\frac{q_0}{1 + q_0} = \\frac{0{,}20}{1 + 0{,}20} = \\frac{0{,}20}{1{,}20} = \\frac{1}{6} \\approx 0{,}167$.",
        "distractors": [
            "$q_1 = 0{,}00$, karena berasumsi bahwa alel resesif letal langsung lenyap 100% dari populasi dalam satu generasi.",
            "$q_1 = 0{,}10$, dihitung dari asumsi penurunan frekuensi linear sebesar separuh nilai awal.",
            "$q_1 = 0{,}04$, yang merupakan frekuensi awal genotipe homozigot resesif (q0 kuadrat).",
            "$q_1 = 0{,}20$, karena menganggap hukum Hardy-Weinberg tetap mempertahankan frekuensi alel konstan meskipun ada seleksi mematikan."
        ],
        "formula": {
            "title": "PERSAMAAN SELEKSI ALAM TERHADAP ALEL RESESIF LETAL (s = 1)",
            "latex": "q_1 = \\frac{q_0}{1 + q_0} = \\frac{0{,}20}{1 + 0{,}20} = \\frac{0{,}20}{1{,}20} = \\frac{1}{6} \\approx 0{,}1667; \\quad q_n = \\frac{q_0}{1 + n \\cdot q_0}",
            "legend": "• Alel resesif terlindung dari seleksi di dalam tubuh individu heterozigot carrier ($Aa$)<br>• Seleksi alam menurunkan frekuensi alel letal dengan laju yang semakin lambat ketika $q$ mendekati nol<br>• Menjelaskan mengapa penyakit genetik resesif langka tidak pernah punah total dari populasi manusia"
        },
        "hints": {
            "concept": "Gunakan rumus seleksi alam untuk alel resesif letal (s=1): q1 = q0 / (1 + q0).",
            "execution": "q1 = 0,20 / (1 + 0,20) = 0,20 / 1,20 = 1/6 = 0,167."
        }
    },
    {
        "id": "bio-lat-h-11",
        "materi": "FISIOLOGI EKSKRESI (MEDULA GINJAL)",
        "topic": "Sistem Pengali Arus Bolak-Balik (Countercurrent Multiplier) Ansa Henle",
        "stem": "Kemampuan nefron jukstamedularis mamalia untuk menghasilkan urin yang sangat pekat (hiperosmotik hingga $1.200\\text{ mOsm/L}$) bergantung pada gradien osmolaritas medula ginjal yang dibangun oleh sistem pengali arus bolak-balik ($\\textit{countercurrent multiplier}$). Perbedaan fungsional antara pars desenden dan pars asenden ansa Henle yang menciptakan gradien tersebut adalah...",
        "correct": "Pars desenden tipis sangat permeabel terhadap air tetapi kedap terhadap garam $\\text{NaCl}$, sedangkan pars asenden tebal aktif memompa ion $\\text{Na}^+$ dan $\\text{Cl}^-$ keluar ke cairan interstisial tetapi kedap sempurna terhadap air.",
        "distractors": [
            "Pars desenden memompa glukosa keluar, sedangkan pars asenden menyerap urea secara endositosis fagositik.",
            "Pars desenden kedap terhadap air tetapi permeabel terhadap gas oksigen, sedangkan pars asenden memompa hormon aldosteron.",
            "Kedua lengkung sama-sama memompa air keluar secara transpor aktif primer menggunakan pompa natrium ATP Sintase.",
            "Pars asenden menyerap air secara masif sedangkan pars desenden mengekskresikan sel darah merah utuh ke pelvis ginjal."
        ],
        "formula": {
            "title": "MEKANISME COUNTERCURRENT MULTIPLIER ANSA HENLE",
            "latex": "\\begin{aligned} \\text{Lengkung Desenden:} & \\quad \\text{Permeabel Air (Efluks H}_2\\text{O via Akuaporin-1)} \\implies \\text{Filtrat Semakin Pekat (1200 mOsm/L)} \\\\ \\text{Lengkung Asenden Tebal:} & \\quad \\text{Kedap Air + Pompa Aktif NKCC2 (Na}^+\\text{-K}^+\\text{-2Cl}^-\\text{)} \\implies \\text{Interstisial Medula Hiperosmotik} \\end{aligned}",
            "legend": "• Vasa rekta bertindak sebagai penukar arus bolak-balik (countercurrent exchanger) pasif<br>• Urea berkontribusi sekitar $50\\%$ pada hiperosmolaritas medula dalam<br>• Memungkinkan ginjal mengekskresikan kelebihan garam dengan kehilangan air minimal"
        },
        "hints": {
            "concept": "Lengkung desenden Henle permeabel air dan kedap garam (air keluar -> filtrat makin pekat). Lengkung asenden tebal kedap air dan memompa aktif garam NaCl keluar (interstisial jadi sangat pekat).",
            "execution": "Pilih pars desenden permeabel air kedap garam, pars asenden aktif memompa NaCl dan kedap air."
        }
    },
    {
        "id": "bio-lat-h-12",
        "materi": "FISIOLOGI KARDIOVASKULAR & HEMODINAMIKA",
        "topic": "Hukum Frank-Starling pada Kontraktilitas Jantung",
        "stem": "Hukum Frank-Starling tentang jantung ($\\textit{Frank-Starling law of the heart}$) menyatakan hubungan mendasar antara volume pengisian ventrikel pada akhir diastol dengan kekuatan kontraksi sistol jantung. Mekanisme fisis-seluler yang mendasari fenomena adaptasi tersebut adalah...",
        "correct": "Peningkatan pengisian darah ($\\textit{end-diastolic volume / preload}$) meregangkan miokardium ventrikel, membawa panjang sarkomer mendekati panjang optimum ($2{,}2\\,\\mu\\text{m}$) di mana tumpang tindih filamen aktin-miosin paling ideal dan afinitas troponin C terhadap ion $\\text{Ca}^{2+}$ meningkat, menghasilkan gaya kontraksi ($\\textit{stroke volume}$) yang lebih kuat.",
        "distractors": [
            "Peregangan ventrikel menghancurkan nodus SA sehingga jantung berdenyut menggunakan pacu listrik otot diafragma.",
            "Peningkatan volume darah menyebabkan otot bilik jantung mengalami hipertrofi nekrosis seketika.",
            "Darah di dalam ventrikel mendidih melepaskan gelembung gas nitrogen yang menekan katup mitral secara mekanik.",
            "Tekanan darah tinggi memicu pelepasan hormon paratiroid yang menyerap kalsium keluar dari sel otot jantung."
        ],
        "formula": {
            "title": "HUKUM FRANK-STARLING PADA VENTRIKEL JANTUNG",
            "latex": "\\text{Venous Return} \\uparrow \\implies \\text{EDV (Preload)} \\uparrow \\implies \\text{Regangan Sarkomer Menuju Optimum} \\implies \\text{Gaya Kontraksi (Stroke Volume)} \\uparrow",
            "legend": "• Menjamin curah jantung ventrikel kanan dan kiri selalu seimbang secara intrinsik<br>• Curah Jantung ($CO = HR \\times SV$)<br>• Pada gagal jantung kongestif, regangan berlebih melampaui panjang optimum $\\implies$ penurunan daya pompa"
        },
        "hints": {
            "concept": "Hukum Frank-Starling: semakin banyak darah masuk ke ventrikel (preload naik), semakin meregang sarkomer otot jantung mendekati panjang optimal, menghasilkan kontraksi dan volume sekuncup (stroke volume) yang lebih kuat.",
            "execution": "Pilih peregangan sarkomer mendekati panjang optimum meningkatkan tumpang tindih aktin-miosin dan gaya kontraksi."
        }
    },
    {
        "id": "bio-lat-h-13",
        "materi": "NEUROBIOLOGI (POTENSIAL MEMBRAN)",
        "topic": "Persamaan Goldman-Hodgkin-Katz dan Potensial Istirahat Neuron",
        "stem": "Potensial membran istirahat ($\\textit{resting membrane potential}$) pada akson neuron mamalia bernilai sekitar $-70\\text{ mV}$ (bagian dalam bermuatan relatif negatif terhadap cairan ekstraseluler). Berdasarkan persamaan Goldman-Hodgkin-Katz (GHK), faktor biologi seluler yang paling dominan menetapkan nilai potensial istirahat mendekati potensial kesetimbangan kalium ($\\approx -90\\text{ mV}$) adalah...",
        "correct": "Permeabilitas membran saat istirahat terhadap ion $\\text{K}^+$ jauh lebih tinggi ($20-50\\text{ kali lipat}$) dibandingkan terhadap ion $\\text{Na}^+$ akibat adanya saluran bocor kalium ($\\text{K}^+\\text{ leak channels}$) yang selalu terbuka, diiringi kerja elektrogenik pompa $\\text{Na}^+/\\text{K}^+$ ATPase yang memompa $3\\text{ Na}^+$ keluar dan $2\\text{ K}^+$ ke dalam.",
        "distractors": [
            "Membran akson memiliki permeabilitas ion natrium yang tak terbatas sehingga ion natrium bebas melompat masuk ke mitokondria.",
            "Molekul DNA bermuatan positif pekat keluar meninggalkan sitosol sel saraf melalui pori-pori nukleus.",
            "Adanya ion kalsium yang menetralkan seluruh muatan listrik negatif protein intraseluler.",
            "Selubung mielin mengalirkan elektron bebas dari dendrit langsung menuju nodus Ranvier secara kontinu."
        ],
        "formula": {
            "title": "PERSAMAAN GOLDMAN-HODGKIN-KATZ (GHK)",
            "latex": "V_m = \\frac{RT}{F} \\ln \\left( \\frac{P_{\\text{K}}[\\text{K}^+]_{o} + P_{\\text{Na}}[\\text{Na}^+]_{o} + P_{\\text{Cl}}[\\text{Cl}^-]_{i}}{P_{\\text{K}}[\\text{K}^+]_{i} + P_{\\text{Na}}[\\text{Na}^+]_{i} + P_{\\text{Cl}}[\\text{Cl}^-]_{o}} \\right) \\approx -70\\text{ mV}",
            "legend": "• Karena $P_{\\text{K}} \\gg P_{\\text{Na}}$ saat istirahat, $V_m$ didominasi oleh gradien ion $\\text{K}^+$<br>• Protein anion intraseluler ($A^-$) yang besar tidak dapat menembus membran<br>• Pompa $3\\text{ Na}^+ / 2\\text{ K}^+$ ATPase mempertahankan gradien konsentrasi jangka panjang"
        },
        "hints": {
            "concept": "Pada keadaan istirahat, membran jauh lebih permeabel terhadap K+ (lewat K+ leak channels) dibanding Na+. Difusi keluar K+ bersama protein anion intraseluler menciptakan potensial negatif -70 mV, distabilkan pompa 3Na+/2K+ ATPase.",
            "execution": "Pilih tingginya permeabilitas ion K+ (saluran bocor K+) dan pompa 3Na+/2K+ ATPase."
        }
    },
    {
        "id": "bio-lat-h-14",
        "materi": "FISIOLOGI ENDOKRIN & STRES (SUMBU HPA)",
        "topic": "Sumbu Hipotalamus-Hipofisis-Adrenal (Sumbu HPA) dan Kortisol",
        "stem": "Dalam respon fisiologis terhadap stres kronis berkepanjangan, tubuh mengaktifkan sumbu neuroendokrin Hipotalamus–Hipofisis–Adrenal (Sumbu HPA). Kaskade sekresi hormon berurutan beserta mekanisme umpan balik negatif penyeimbang homeostasis adalah...",
        "correct": "Hipotalamus mensekresikan Corticotropin-Releasing Hormone (CRH) $\\rightarrow$ merangsang hipofisis anterior mensekresikan Adrenocorticotropic Hormone (ACTH) $\\rightarrow$ merangsang korteks adrenal mensekresikan hormon glukokortikoid (Kortisol); kadar kortisol bebas yang tinggi di darah memberikan umpan balik negatif menghambat pelepasan CRH dan ACTH.",
        "distractors": [
            "Medula adrenal mensekresikan insulin $\\rightarrow$ hipofisis posterior mensekresikan hormon pertumbuhan $\\rightarrow$ hipotalamus melepaskan melatonin pembakar lemak.",
            "Kelenjar tiroid memproduksi kalsitonin $\\rightarrow$ merangsang pankreas memproduksi kortisol $\\rightarrow$ memicu umpan balik positif menaikkan suhu tubuh.",
            "Hipofisis anterior memproduksi prolaktin $\\rightarrow$ korteks adrenal memproduksi adrenalin $\\rightarrow$ hipotalamus melepaskan hormon antidiuretik.",
            "Korteks adrenal mensekresikan tiroksin $\\rightarrow$ hipofisis mensekresikan oksitosin $\\rightarrow$ hipotalamus menghentikan respirasi aerob."
        ],
        "formula": {
            "title": "KASKADE HORMONAL SUMBU HPA (HYPOTHALAMIC-PITUITARY-ADRENAL)",
            "latex": "\\text{Stres} \\implies \\text{Hipotalamus (CRH)} \\xrightarrow{(+)} \\text{Hipofisis Anterior (ACTH)} \\xrightarrow{(+)} \\text{Korteks Adrenal (Kortisol)} \\xrightarrow{(-)} \\text{Loop Umpan Balik Negatif}",
            "legend": "• Kortisol memicu glukoneogenesis, proteolisis, lipolisis, dan supresi inflamasi/imun<br>• Kerusakan kontrol umpan balik negatif $\\implies$ Sindrom Cushing (hiperkortisolisme)<br>• Destruksi autoimun korteks adrenal $\\implies$ Penyakit Addison"
        },
        "hints": {
            "concept": "Sumbu HPA: Hipotalamus melepas CRH -> memicu Hipofisis Anterior melepas ACTH -> memicu Korteks Adrenal melepas Kortisol. Kortisol tinggi memberikan umpan balik negatif menghambat hipotalamus & hipofisis.",
            "execution": "Pilih kaskade CRH -> ACTH -> Kortisol dengan umpan balik negatif kortisol."
        }
    },
    {
        "id": "bio-lat-h-15",
        "materi": "FISIOLOGI TUMBUHAN (TRANSLOKASI FLOEM)",
        "topic": "Hipotesis Aliran Tekanan Massal (Pressure-Flow Hypothesis) Ernst Münch",
        "stem": "Mekanisme translokasi asimilat hasil fotosintesis (terutama sukrosa) dari organ sumber ($\\textit{source}$, seperti daun dewasa) ke organ penampung ($\\textit{sink}$, seperti akar dan buah) melalui pembuluh tapis floem dijelaskan oleh hipotesis aliran tekanan ($\\textit{Pressure-Flow Hypothesis}$). Penggerak fisik utama aliran massal getah floem tersebut adalah...",
        "correct": "Pemuatan aktif sukrosa ke dalam elemen pembuluh tapis di organ $\\textit{source}$ menurunkan potensial air secara drastis, memicu osmosis air dari xilem tetangga masuk ke floem sehingga menciptakan tekanan turgor hidrostatis yang tinggi; sebaliknya di organ $\\textit{sink}$ sukrosa dibongkar keluar sehingga air berosmosis kembali ke xilem, menghasilkan gradien tekanan hidrostatis yang mendorong aliran getah dari sumber ke penampung.",
        "distractors": [
            "Gaya kapilaritas dan daya hisap transpirasi daun yang menarik molekul gula ke atas melawan gravitasi.",
            "Aktivitas silia dan flagela mikroskopis yang bergetar di sepanjang dinding sel tapis floem.",
            "Adanya gelembung udara oksigen yang mendorong cairan getah gula secara pneumatik termal.",
            "Pembelahan mitosis kambium pembuluh yang secara fisik mendorong molekul sukrosa ke ujung akar."
        ],
        "formula": {
            "title": "MEKANISME ALIRAN TEKANAN FLOEM (MÜNCH)",
            "latex": "\\Delta P = P_{\\text{source}} - P_{\\text{sink}} > 0; \\quad \\Psi_{s,\\text{source}} \\downarrow \\implies \\text{Air Masuk} \\implies P_{\\text{turgor}} \\uparrow; \\quad \\text{Laju Aliran } J_v = L_p \\Delta P",
            "legend": "• Pemuatan floem (phloem loading) membutuhkan transpor aktif kotransporter sukrosa-$H^+$ (memerlukan ATP)<br>• Pembongkaran floem (phloem unloading) terjadi di organ pemakai/penyimpan<br>• Mengalirkan getah floem secara bidirectional (bisa ke atas menuju tunas/bunga atau ke bawah menuju umbi)"
        },
        "hints": {
            "concept": "Di daun (source), gula dimuat ke floem -> air xilem masuk ke floem secara osmosis -> tekanan turgor naik tinggi. Di sink, gula dibongkar -> air keluar -> tekanan turgor rendah. Beda tekanan hidrostatis ini mendorong aliran cairan getah floem.",
            "execution": "Pilih pembentukan gradien tekanan turgor hidrostatis akibat pemuatan dan pembongkaran sukrosa osmotik."
        }
    },
    {
        "id": "bio-lat-h-16",
        "materi": "TRANSDUKSI SINYAL SELULER",
        "topic": "Jalur Reseptor Terhubung Protein G (GPCR) dan Second Messenger cAMP",
        "stem": "Pengikatan hormon epinefrin pada reseptor $\\beta$-adrenergik di membran sel hepatosit (hati) memicu penguraian cepat cadangan glikogen menjadi glukosa darah (glikogenolisis). Urutan kaskade transduksi sinyal intraseluler yang benar adalah...",
        "correct": "Epinefrin berikatan dengan GPCR $\\rightarrow$ Aktivasi protein $G_s$ (mengikat GTP) $\\rightarrow$ Stimulasi enzim adenilat siklase $\\rightarrow$ Sintesis second messenger cAMP dari ATP $\\rightarrow$ Aktivasi Protein Kinase A (PKA) $\\rightarrow$ Fosforilasi kaskade glikogen fosforilase kinase dan glikogen fosforilase.",
        "distractors": [
            "Epinefrin masuk ke dalam inti sel $\\rightarrow$ berikatan dengan DNA $\\rightarrow$ memotong ikatan glikogen secara hidrolisis asam.",
            "Epinefrin berikatan dengan reseptor tirosin kinase $\\rightarrow$ autofosforilasi $\\rightarrow$ membuka saluran ion kalium di vakuola.",
            "Epinefrin merangsang lisosom memakan mitokondria untuk melepaskan molekul glukosa cadangan.",
            "Epinefrin menginaktifkan adenilat siklase $\\rightarrow$ menurunkan kadar cAMP $\\rightarrow$ memicu sintesis glikogen polimer."
        ],
        "formula": {
            "title": "KASKADE PENGUATAN SINYAL GLIKOGENOLISIS OLEH EPINEFRIN",
            "latex": "1\\text{ Epinefrin} \\to 1\\text{ GPCR} \\to \\sim 10\\, G_{\\alpha\\text{-GTP}} \\to \\sim 10\\text{ Adenilat Siklase} \\to 10^3\\text{ cAMP} \\to 10^3\\text{ PKA} \\to 10^6\\text{ Glukosa-1-P}",
            "legend": "• Penguatan sinyal (amplification cascade) jutaan kali lipat dalam hitungan detik<br>• Enzim fosfodiesterase (PDE) mendegradasi cAMP menjadi $5'\\text{-AMP}$ untuk mematikan sinyal<br>• Kafein menghambat PDE $\\implies$ mempertahankan cAMP tetap tinggi"
        },
        "hints": {
            "concept": "Epinefrin -> GPCR -> Protein Gs (GTP) -> Adenilat siklase -> cAMP -> PKA -> aktivasi glikogen fosforilase -> pelepasan glukosa.",
            "execution": "Pilih kaskade GPCR -> Gs -> adenilat siklase -> cAMP -> PKA -> aktivasi glikogen fosforilase."
        }
    },
    {
        "id": "bio-lat-h-17",
        "materi": "SIKLUS SEL & ONKOLOGI MOLEKULER",
        "topic": "Peran Protein Tumor Suppressor p53 dan Retinoblastoma (Rb)",
        "stem": "Pengendalian siklus sel pada titik pemeriksaan G1/S ($\\textit{G1/S checkpoint}$) sangat krusial untuk mencegah proliferasi sel yang mengalami kerusakan materi genetik. Dua protein penekan tumor ($\\textit{tumor suppressor}$) utama yang bertindak sebagai rem molekuler pada fase ini adalah p53 dan Retinoblastoma (Rb). Mekanisme kerja molekuler protein p53 ketika mendeteksi adanya kerusakan DNA adalah...",
        "correct": "p53 terstabilisasi dan bertindak sebagai faktor transkripsi untuk mengekspresikan protein p21 (inhibitor CDK); p21 menghambat kompleks Cyclin D-CDK4/6 dan Cyclin E-CDK2, mencegah fosforilasi protein Rb sehingga Rb tetap mengikat dan membungkam faktor transkripsi E2F, menghentikan siklus sel pada fase G1 untuk memberi waktu perbaikan DNA (atau memicu apoptosis via Bax jika kerusakan terlalu parah).",
        "distractors": [
            "p53 memotong rantai DNA menjadi fragmen-fragmen kecil agar sel dapat langsung memasuki fase anafase pembelahan mitosis.",
            "p53 memfosforilasi molekul tubulin agar gelendong pembelahan terbentuk di dalam membran nukleus interfase.",
            "p53 menghancurkan seluruh mitokondria sel sehingga pembelahan sel beralih ke respirasi kemosintesis belerang.",
            "p53 memicu translasi onkogen Ras untuk mempercepat penggandaan kromatid secara tak terkendali."
        ],
        "formula": {
            "title": "CHECKPOINT G1/S: REGULASI P53 & JALUR RETINOBLASTOMA",
            "latex": "\\text{Kerusakan DNA} \\implies \\text{p53} \\uparrow \\implies \\text{p21} \\uparrow \\implies \\text{CDK terhambat} \\implies \\text{Rb Hipofosforilasi (Aktif Mengikat E2F)} \\implies \\text{Cell Cycle Arrest di G1}",
            "legend": "• p53 dijuluki 'Penjaga Genom' (Guardian of the Genome)<br>• Mutasi inaktivasi gen TP53 ditemukan pada $> 50\\%$ seluruh jenis kanker manusia<br>• Kegagalan fungsi p53 memungkinkan sel bermutasi membelah tanpa kontrol membentuk tumor ganas"
        },
        "hints": {
            "concept": "p53 mendeteksi kerusakan DNA -> aktifkan p21 -> hambat kompleks Cyclin-CDK -> Rb tetap mengikat E2F (inaktif) -> siklus sel tertahan di G1 untuk perbaikan DNA atau apoptosis.",
            "execution": "Pilih p53 memicu ekspresi p21 menghambat CDK, mempertahankan Rb mengikat E2F sehingga siklus sel terhenti di G1."
        }
    },
    {
        "id": "bio-lat-h-18",
        "materi": "BIOLOGI PERKEMBANGAN (GEN MORFOGENESIS)",
        "topic": "Peran Gen Homeobox (Hox Genes) dalam Pola Tubuh Hewan",
        "stem": "Dalam perkembangan embrio hewan dari serangga hingga mamalia, susunan segmen tubuh di sepanjang sumbu antero-posterior (kepala, toraks, abdomen) ditentukan oleh kelompok gen homeotik ($\\textit{Hox genes}$). Fenomena molekuler penting yang dikenal sebagai kolinearitas spasial dan temporal dari gen-gen $\\textit{Hox}$ adalah...",
        "correct": "Urutan susunan fisik gen-gen $\\textit{Hox}$ di sepanjang untai kromosom (dari ujung 3' ke 5') tepat sejajar dengan urutan ekspresi spasialnya di sepanjang tubuh dari anterior ke posterior, serta waktu ekspresinya selama perkembangan embrio (gen ujung 3' diekspresikan lebih awal di wilayah anterior).",
        "distractors": [
            "Gen Hox diekspresikan secara acak di setiap sel tubuh tanpa mempedulikan posisi fisik pada kromosom.",
            "Gen Hox hanya aktif pada hewan dewasa pasca metamorfosis dan tidak memiliki peran apapun pada embrio.",
            "Kolinearitas berarti gen Hox hanya mampu ditranskripsi jika sel mengandung kloroplas fungsional.",
            "Setiap mutasi pada gen Hox selalu menghasilkan individu yang tidak memiliki materi genetik sama sekali."
        ],
        "formula": {
            "title": "PRINSIP KOLINEARITAS GEN HOX (HOMEOTIK)",
            "latex": "\\text{Kromosom (3'} \\to \\text{5'): } \\text{Hox1 (Anterior/Awal)} \\to \\text{Hox4 (Toraks)} \\to \\text{Hox9} \\to \\text{Hox13 (Posterior/Akhir)}",
            "legend": "• Gen Hox mengkode faktor transkripsi yang memiliki domain pengikat DNA (homeodomain $60\\text{ asam amino}$)<br>• Mutasi homeotik (misal Antennapedia pada $\\textit{Drosophila}$) dapat menyebabkan kaki tumbuh di tempat antena<br>• Bukti konservasi evolusioner mendalam regulasi morfogenesis bilateria"
        },
        "hints": {
            "concept": "Kolinearitas gen Hox: urutan gen pada kromosom (3' ke 5') mencerminkan urutan bagian tubuh dari anterior (kepala) ke posterior (ekor) dan urutan waktu kemunculannya saat embriogenesis.",
            "execution": "Pilih urutan gen pada kromosom sejajar dengan urutan spasial anterior-posterior dan waktu ekspresinya."
        }
    },
    {
        "id": "bio-lat-h-19",
        "materi": "IMUNOPATOLOGI (HIPERSENSITIVITAS TIPE I)",
        "topic": "Mekanisme Degranulasi Sel Mast pada Reaksi Anafilaksis Diperantarai IgE",
        "stem": "Reaksi alergi berat (hipersensitivitas tipe I / anafilaksis) terhadap kacang tanah atau sengatan lebah dapat memicu syok anafilaksis yang mengancam jiwa dalam hitungan menit. Mekanisme imunologis yang mendasari pelepasan masif mediator inflamasi pada paparan sekunder alergen adalah...",
        "correct": "Alergen mengikat silang ($\\textit{cross-linking}$) minimal dua molekul antibodi $\\text{IgE}$ spesifik yang telah tertambat pada reseptor $\\text{Fc}\\varepsilon\\text{RI}$ di permukaan sel mast dan basofil, memicu influks kalsium dan degranulasi eksositosis cepat histamin, leukotrien, dan prostaglandin yang menyebabkan vasodilatasi sistemik dan bronkokonstriksi.",
        "distractors": [
            "Antibodi IgG dan IgM mengaktifkan komplemen jalur alternatif yang melisiskan sel eritrosit di ginjal.",
            "Limfosit T sitotoksik membunuh sel-sel epitel kulit menggunakan enzim perforin dan granzim secara langsung.",
            "Sel dendritik memproduksi racun botulinum yang membekukan saluran pernapasan atas.",
            "Molekul alergen menembus mitokondria sel mast dan menghentikan pembentukan energi ATP secara permanen."
        ],
        "formula": {
            "title": "PATOFISIOLOGI REAKSI ANAFILAKSIS (HIPERSENSITIVITAS TIPE I)",
            "latex": "\\text{Paparan Ulang Alergen} + 2\\text{ IgE/Fc}\\varepsilon\\text{RI Cross-link} \\implies \\text{Degranulasi Sel Mast} \\implies \\text{Histamin} \\uparrow \\implies \\begin{cases} \\text{Vasodilatasi Masif (Tekanan Darah Drop)} \\\\ \\text{Bronkokonstriksi (Sesak Napas Berat)} \\end{cases}",
            "legend": "• Fase Sensitisasi: Paparan pertama memicu sel B memproduksi antibodi $\\text{IgE}$ yang menempel di sel mast<br>• Fase Reaksi: Paparan berikutnya memicu degranulasi seketika ($< 15\\text{ menit}$)<br>• Penanganan darurat: Injeksi epinefrin (adrenalin) intramuskular untuk bronkodilasi dan vasokonstriksi"
        },
        "hints": {
            "concept": "Alergi tipe I: diperantarai IgE pada reseptor Fc-epsilon-RI sel mast. Saat alergen datang lagi, alergen mengikat-silang IgE -> sel mast degranulasi -> lepas histamin -> vasodilatasi masif & bronkokonstriksi.",
            "execution": "Pilih cross-linking antibodi IgE pada sel mast yang memicu degranulasi cepat histamin."
        }
    },
    {
        "id": "bio-lat-h-20",
        "materi": "MIKROBIOLOGI & RESISTENSI ANTIBIOTIK",
        "topic": "Mekanisme Resistensi Bakteri MRSA terhadap Antibiotik Beta-Laktam",
        "stem": "Strain bakteri $\\textit{Staphylococcus aureus}$ resisten metisilin (MRSA) kebal terhadap hampir seluruh antibiotik golongan beta-laktam (seperti penisilin, amoksisilin, dan sefalosporin). Mekanisme genetik-biokimia utama yang memberikan resistensi tingkat tinggi pada bakteri MRSA adalah...",
        "correct": "Perolehan gen $\\textit{mecA}$ melalui transfer gen horizontal yang mengkode protein pengikat penisilin alternatif PBP2a ($\\textit{Penicillin-Binding Protein 2a}$); protein PBP2a memiliki afinitas pengikatan yang sangat rendah terhadap antibiotik beta-laktam sehingga sintesis dinding sel peptidoglikan bakteri tetap berlangsung normal meskipun terdapat antibiotik berkonsentrasi tinggi.",
        "distractors": [
            "Bakteri mengganti dinding sel peptidoglikannya menjadi dinding sel selulosa seperti tumbuhan tingkat tinggi.",
            "Bakteri mensekresikan enzim amilase yang menghancurkan struktur asam nukleat manusia.",
            "Bakteri bermutasi menjadi virus litik intraseluler obligat yang tidak memiliki membran sel.",
            "Bakteri menghentikan sintesis protein seluler dan bertahan hidup murni menggunakan energi foton sinar ultraviolet."
        ],
        "formula": {
            "title": "MEKANISME MOLEKULER RESISTENSI PBP2A PADA MRSA",
            "latex": "\\text{Kaset Kromosom } \\textit{SCCmec} \\to \\text{Ekspresi Gen } \\textit{mecA} \\to \\text{PBP2a (Afinitas } \\beta\\text{-Laktam Sangat Rendah)} \\implies \\text{Sintesis Peptidoglikan Utuh}",
            "legend": "• Antibiotik $\\beta$-laktam bekerja menginaktivasi PBP normal (transpeptidase pembentuk ikatan silang peptidoglikan)<br>• PBP2a tidak dapat diinaktivasi oleh metisilin atau penisilin turunan lainnya<br>• Membutuhkan terapi antibiotik lini akhir seperti vankomisin atau daptomisin"
        },
        "hints": {
            "concept": "MRSA membawa gen mecA yang mengkode PBP2a (Penicillin-Binding Protein 2a alternatif). PBP2a tidak bisa diikat oleh antibiotik beta-laktam, sehingga dinding sel bakteri tetap terbentuk.",
            "execution": "Pilih gen mecA yang mengkode protein PBP2a berafinitas rendah terhadap beta-laktam."
        }
    },
    {
        "id": "bio-lat-h-21",
        "materi": "EKOLOGI POPULASI MATEMATIS",
        "topic": "Model Pertumbuhan Logistik dan Analisis Daya Dukung Lingkungan (K)",
        "stem": "Dinamika pertumbuhan populasi suatu spesies hewan di alam terbatas mengikuti persamaan diferensial logistik Verhulst:<br>$$\\frac{dN}{dt} = r N \\left(1 - \\frac{N}{K}\\right)$$<br>di mana $r$ adalah laju pertumbuhan intrinsik per kapita, $N$ adalah ukuran populasi, dan $K$ adalah daya dukung lingkungan ($\\textit{carrying capacity}$). Laju pertambahan populasi per satuan waktu ($\\frac{dN}{dt}$) akan mencapai nilai maksimum absolutnya ketika ukuran populasi ($N$) bernilai...",
        "correct": "$N = \\frac{K}{2}$ (separuh dari daya dukung lingkungan), karena grafik laju pertambahan populasi terhadap $N$ berbentuk kurva parabola dengan titik puncak maksimum tepat pada $N = \\frac{K}{2}$, di mana turunan kedua $\\frac{d^2N}{dt^2} = 0$ (titik belok kurva sigmoid $S$).",
        "distractors": [
            "$N = K$, di mana laju pertambahan populasi justru bernilai nol ($dN/dt = 0$) karena daya dukung lingkungan telah jenuh penuh.",
            "$N = 0$, di mana tidak ada individu organisme yang mampu bereproduksi menghasilkan anakan baru.",
            "$N = 2K$, di mana terjadi mortalitas massal akibat kompetisi intraspesifik yang melampaui batas ekosistem.",
            "$N = \\frac{K}{4}$, di mana populasi masih berada pada fase lag awal dengan laju pertumbuhan yang lambat."
        ],
        "formula": {
            "title": "MODEL PERTUMBUHAN LOGISTIK & LAJU MAKSIMUM (MSY)",
            "latex": "f(N) = rN - \\frac{r}{K}N^2 \\implies \\frac{df}{dN} = r - \\frac{2r}{K}N = 0 \\implies N = \\frac{K}{2}; \\quad \\left(\\frac{dN}{dt}\\right)_{\\max} = \\frac{rK}{4}",
            "legend": "• Titik $N = K/2$ merupakan dasar teori Maximum Sustainable Yield (MSY) pada pengelolaan perikanan dan kehutanan<br>• Pada $N < K/2$: Pertumbuhan dipercepat (akselerasi positif)<br>• Pada $N > K/2$: Pertumbuhan melambat akibat resistensi lingkungan"
        },
        "hints": {
            "concept": "Laju pertambahan dN/dt = rN(1 - N/K) adalah fungsi kuadrat terhadap N. Puncaknya tercapai pada turunan = 0, yaitu saat N = K/2 (separuh kapasitas daya dukung).",
            "execution": "Pilih N = K/2 (separuh daya dukung lingkungan)."
        }
    },
    {
        "id": "bio-lat-h-22",
        "materi": "BIOGEOGRAFI PULAU (MACARTHUR-WILSON)",
        "topic": "Model Keseimbangan Dinamis Biogeografi Pulau",
        "stem": "Teori Biogeografi Pulau yang dikembangkan oleh Robert MacArthur dan E.O. Wilson memprediksi jumlah kekayaan spesies ($S$) pada suatu pulau saat mencapai titik kesetimbangan dinamis antara laju imigrasi spesies baru ($I$) dan laju kepunahan spesies lokal ($E$). Berdasarkan model ini, pulau yang diprediksi memiliki jumlah spesies paling tinggi pada titik kesetimbangan adalah pulau yang...",
        "correct": "Berukuran besar dan terletak dekat dengan daratan utama ($\\textit{mainland}$); ukuran besar menyediakan variasi habitat melimpah serta populasi besar yang menurunkan laju kepunahan, sementara jarak dekat memaksimalkan laju imigrasi kolonisasi spesies baru.",
        "distractors": [
            "Berukuran kecil dan terletak sangat terisolasi jauh di tengah samudra luas.",
            "Berukuran besar namun terletak sangat terisolasi dengan suhu udara di bawah nol derajat Celsius.",
            "Berukuran kecil dan terletak dekat karena pulau kecil tidak memiliki pemangsa puncak karnivora.",
            "Memiliki luas daratan yang selalu tenggelam pasang surut air laut setiap enam jam sekali."
        ],
        "formula": {
            "title": "MODEL KESETIMBANGAN KEKAYAAN SPESIES PULAU (MACARTHUR-WILSON)",
            "latex": "S_{\\text{eq}} \\iff \\text{Laju Imigrasi } (I) = \\text{Laju Kepunahan } (E); \\quad S_{\\text{Besar, Dekat}} \\gg S_{\\text{Kecil, Jauh}}",
            "legend": "• Efek Jarak: Mengendalikan Laju Imigrasi (Pulau dekat memiliki $I$ tinggi)<br>• Efek Ukuran: Mengendalikan Laju Kepunahan (Pulau besar memiliki kapasitas relung luas $\\implies E$ rendah)<br>• Menjadi pilar teori desain cagar alam konservasi terfragmentasi (SLOSS debate)"
        },
        "hints": {
            "concept": "Menurut MacArthur-Wilson: Pulau besar punya kepunahan rendah (banyak relung & sumber daya). Pulau dekat punya imigrasi tinggi (mudah dicapai). Kombinasi terbaik = Besar dan Dekat.",
            "execution": "Pilih pulau berukuran besar dan terletak dekat daratan utama."
        }
    },
    {
        "id": "bio-lat-h-23",
        "materi": "EVOLUSI MOLEKULER & JAM MOLEKULER",
        "topic": "Teori Netral Evolusi Molekuler Motoo Kimura dan Jam Molekuler",
        "stem": "Teori Netral Evolusi Molekuler yang diajukan oleh Motoo Kimura (1968) menyatakan bahwa pada tingkat urutan nukleotida DNA dan asam amino protein, mayoritas mutasi yang mengalami fiksasi dalam populasi bersifat netral terhadap seleksi alam. Konsekuensi matematis fundamental dari teori netral ini terhadap konsep 'Jam Molekuler' ($\\textit{Molecular Clock}$) adalah...",
        "correct": "Laju fiksasi mutasi netral per satuan waktu ($k$) sama persis dengan laju mutasi netral ($u$) terlepas dari ukuran populasi ($k = u$), sehingga substitusi basa molekuler terakumulasi pada laju konstan yang proporsional dengan waktu divergensi geologis sejak berpisahnya dua spesies.",
        "distractors": [
            "Laju evolusi molekuler berbanding lurus dengan kuadrat jumlah populasi sehingga jam molekuler hanya berlaku pada populasi kecil.",
            "Setiap mutasi molekuler selalu dipicu oleh seleksi alam darwinian yang menguntungkan kelangsungan hidup.",
            "Semua protein di dalam tubuh berevolusi dengan kecepatan laju substitusi yang identik persis tanpa perbedaan.",
            "Jam molekuler hanya dapat diukur menggunakan isotop radioaktif uranium pada sampel fosil batuan beku."
        ],
        "formula": {
            "title": "TEORI NETRAL DAN LAJU FIKSASI SUBSTITUSI MOLEKULER",
            "latex": "k = 2N_e u \\times \\left(\\frac{1}{2N_e}\\right) = u; \\quad D = 2 u t \\implies t = \\frac{D}{2u}",
            "legend": "• Jumlah mutasi baru per generasi dalam populasi diploid = $2 N_e u$<br>• Peluang fiksasi mutasi netral murni karena genetic drift = $\\frac{1}{2 N_e}$<br>• Hasil kali keduanya: $k = u$ (independen dari ukuran populasi $N_e$)<br>• Memungkinkan penaksiran waktu percabangan pohon filogenetik ($t$)"
        },
        "hints": {
            "concept": "Teori Netral Kimura: Laju substitusi fiksasi mutasi netral k = u (sama dengan laju mutasi itu sendiri, tidak bergantung ukuran populasi N). Ini mendasari konsep jam molekuler konstan.",
            "execution": "Pilih laju fiksasi mutasi netral sama dengan laju mutasi (k = u) sehingga akumulasi substitusi konstan terhadap waktu."
        }
    },
    {
        "id": "bio-lat-h-24",
        "materi": "FISIOLOGI REPRODUKSI WANITA",
        "topic": "Lonjakan Hormon Luteinizing (LH Surge) dan Pemicu Ovulasi",
        "stem": "Dalam siklus ovarium wanita, ovulasi (pelepasan oosit sekunder dari folikel Graaf yang matang) terjadi tepat sekitar hari ke-14. Peristiwa endokrin yang secara langsung memicu terjadinya ovulasi adalah...",
        "correct": "Lonjakan tajam hormon LH ($\\textit{LH surge}$) yang dipicu oleh mekanisme umpan balik positif dari kadar estrogen (estradiol) berkonsentrasi tinggi yang disekresikan secara kontinu oleh folikel Graaf matang selama lebih dari 36 jam.",
        "distractors": [
            "Penurunan drastis hormon progesteron akibat atrofi dini korpus luteum pada fase folikuler awal.",
            "Umpan balik negatif hormon testosteron yang memblokir pelepasan hormon GnRH di hipotalamus.",
            "Kenaikan hormon prolaktin yang merangsang lisis dinding ovarium secara mekanik enzimatis.",
            "Pelepasan hormon oksitosin dalam jumlah besar oleh endometrium rahim fase menstruasi."
        ],
        "formula": {
            "title": "MEKANISME UMPAN BALIK POSITIF OVULASI (LH SURGE)",
            "latex": "\\text{Folikel Matang} \\to \\text{Estrogen Sangat Tinggi } (>200\\text{ pg/mL}) \\implies \\text{Umpan Balik Positif ke Hipofisis} \\implies \\text{Lonjakan LH} \\implies \\text{Ovulasi (Jam ke-36)}",
            "legend": "• Pada kadar rendah-sedang: Estrogen memberikan umpan balik negatif menekan FSH/LH<br>• Pada akhir fase folikuler: Estrogen tinggi beralih memicu umpan balik positif masif<br>• LH memicu penyelesaian meiosis I oosit dan aktivasi enzim proteolitik dinding folikel"
        },
        "hints": {
            "concept": "Sebelum ovulasi, estrogen folikel Graaf yang sangat tinggi memicu umpan balik positif ke hipofisis anterior, menghasilkan lonjakan masif hormon LH (LH surge) yang memicu ovulasi.",
            "execution": "Pilih lonjakan hormon LH (LH surge) akibat umpan balik positif estrogen konsentrasi tinggi."
        }
    },
    {
        "id": "bio-lat-h-25",
        "materi": "NEUROBIOLOGI SENSORIK (FOTOTRANSDUKSI RETINA)",
        "topic": "Mekanisme Molekuler Fototransduksi pada Sel Batang Retina",
        "stem": "Mekanisme fototransduksi pada sel fotoreseptor batang ($\\textit{rod cells}$) retina mata dalam merespon datangnya foton cahaya berbeda unik dari neuron sensorik lainnya. Ketika foton cahaya diserap oleh molekul fotopigmen rodopsin, perubahan potensial membran sel fotoreseptor yang terjadi beserta mekanismenya adalah...",
        "correct": "Sel mengalami hiperpolarisasi (bukan depolarisasi); fotoisomerisasi retinal mengaktifkan protein transdusin $\\rightarrow$ stimulasi fosfodiesterase (PDE) memecah cGMP menjadi $5'\\text{-GMP} \\rightarrow$ penutupan saluran ion $\\text{Na}^+$ berpintu cGMP $\\rightarrow$ influks $\\text{Na}^+$ terhenti sementara efluks $\\text{K}^+$ berlanjut $\\rightarrow$ penurunan pelepasan neurotransmiter glutamat ke sel bipolar.",
        "distractors": [
            "Sel mengalami depolarisasi masif akibat terbukanya jutaan saluran kalsium berpintu voltase di segmen luar.",
            "Molekul rodopsin meledak melepaskan panas yang mendidihkan cairan humor vitreus bola mata.",
            "Saluran ion klorida terpompa keluar menyebabkan potensial membran melonjak positif $+50\\text{ mV}$.",
            "Sel fotoreseptor memproduksi hormon melatonin yang melarutkan pigmen melanin koroid mata."
        ],
        "formula": {
            "title": "KASKADE BIOKIMIA FOTOTRANSDUKSI RETINA",
            "latex": "h\\nu + \\text{Rodopsin (11-}\\textit{cis}\\text{)} \\to \\text{Metarodopsin II} \\to \\text{Transdusin} \\to \\text{PDE} \\to \\text{cGMP} \\downarrow \\implies \\text{Kanal Na}^+ \\text{ Tutup} \\implies \\text{Hiperpolarisasi (-70 mV)}",
            "legend": "• Dalam gelap: cGMP tinggi $\\implies$ kanal $\\text{Na}^+$ terbuka ($\\textit{dark current}$) $\\implies$ sel terdepolarisasi ($-40\\text{ mV}$) melepas glutamat kontinu<br>• Dalam terang: Kanal $\\text{Na}^+$ menutup $\\implies$ sel hiperpolarisasi $\\implies$ pelepasan glutamat terhenti<br>• Sel bipolar mendeteksi ketiadaan glutamat sebagai sinyal persepsi cahaya"
        },
        "hints": {
            "concept": "Di dalam gelap, sel batang terdepolarisasi (-40 mV). Saat terkena cahaya, cGMP dipecah oleh PDE, kanal Na+ menutup, sehingga sel batang terhiperpolarisasi (-70 mV) dan mengurangi sekresi glutamat.",
            "execution": "Pilih sel mengalami hiperpolarisasi akibat penutupan saluran ion Na+ berpintu cGMP."
        }
    }
]
