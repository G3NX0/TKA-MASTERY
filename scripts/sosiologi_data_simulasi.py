# -*- coding: utf-8 -*-
"""
sosiologi_data_simulasi.py
--------------------------
35 Authentic HOTS Simulation Questions for TKA 2026 Sosiologi (SMA/MA Soshum).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
IDs: sos-sim-01 .. sos-sim-35
Breakdown:
- 25 Single MCQ HOTS (sos-sim-01 .. sos-sim-25)
- 5 Multi-select HOTS (sos-sim-26 .. sos-sim-30)
- 5 Matrix Benar-Salah HOTS (sos-sim-31 .. sos-sim-35)
"""

SOSIOLOGI_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 SINGLE MCQ HOTS (sos-sim-01 to sos-sim-25)
    # -------------------------------------------------------------
    {
        "id": "sos-sim-01",
        "materi": "KELOMPOK SOSIAL & KEBERAGAMAN BUDAYA",
        "topic": "Sikap Etnosentrisme vs Relativisme Budaya",
        "stem": "Seorang wisatawan perkotaan yang berkunjung ke sebuah desa pedalaman mengunggah video di media sosial yang mengejek upacara pemakaman adat setempat sebagai 'tradisi pemborosan yang tidak higienis dan primitif'. Tindakan wisatawan tersebut mencerminkan sikap...",
        "correct": "Etnosentrisme, yaitu kecenderungan memandang dan menilai kebudayaan kelompok lain secara sepihak dengan menggunakan tolok ukur nilai dan standar kebudayaan kelompoknya sendiri.",
        "distractors": [
            "Relativisme Budaya (_Cultural Relativism_), yaitu usaha memahami praktik kebudayaan lain dari sudut pandang konteks nilai masyarakat setempat.",
            "Xenosentrisme, yaitu sikap mengagumi kebudayaan bangsa asing secara berlebihan dan merendahkan budaya bangsa sendiri.",
            "Pluralisme kultural, yaitu pengakuan tulus atas kesetaraan hak hidup berbagai kebudayaan dalam tatanan demokrasi.",
            "Asimilasi budaya sukarela yang menyatukan tradisi perdesaan dengan tradisi metropolitan."
        ],
        "formula": {
            "title": "KOMPARASI SIKAP TERHADAP PERBEDAAN BUDAYA",
            "latex": "\\begin{cases} \\mathbf{\\text{Etnosentrisme:}} & \\mathbf{\\text{Menilai budaya lain dengan standar budayanya sendiri (Superioritas Suku/In-Group)}} \\\\ \\mathbf{\\text{Relativisme Budaya:}} & \\text{Memahami budaya dalam konteks nilai masyarakat pelaku itu sendiri (Objektif)} \\\\ \\mathbf{\\text{Xenosentrisme:}} & \\text{Menganggap budaya asing lebih hebat dan merendahkan budaya sendiri} \\end{cases}",
            "legend": "• Etnosentrisme berlebihan dapat menjadi pemicu prasangka rasial dan konflik horizontal antar-etnis"
        },
        "hints": {
            "concept": "Etnosentrisme = menilai kebudayaan kelompok lain dengan tolak ukur budaya sendiri (menganggap budaya sendiri paling benar/superior). Relativisme budaya = memahami kebudayaan dari sudut pandang konteks aslinya.",
            "execution": "Pilih: Etnosentrisme."
        }
    },
    {
        "id": "sos-sim-02",
        "materi": "KONSEP DASAR & INTERAKSI SOSIAL",
        "topic": "Tiga Premis Dasar Interaksionisme Simbolik Herbert Blumer",
        "stem": "Herbert Blumer merumuskan tiga premis dasar dalam teori Interaksionisme Simbolik. Premis yang menyatakan bahwa 'makna yang dimiliki oleh suatu objek atau simbol tidak bersifat statis sejak lahir, melainkan terus dimodifikasi dan disempurnakan melalui proses penafsiran (_interpretative process_) yang dilakukan oleh individu saat berinteraksi dengan orang lain' mencerminkan premis ke-...",
        "correct": "Premis Ketiga, yaitu makna-makna tersebut ditangani dan dimodifikasi melalui suatu proses penafsiran yang digunakan oleh seseorang dalam menghadapi hal-hal yang dijumpainya.",
        "distractors": [
            "Premis Pertama, yaitu manusia bertindak terhadap sesuatu berdasarkan makna yang dimiliki hal tersebut bagi mereka.",
            "Premis Kedua, yaitu makna tersebut berasal dari atau muncul dari interaksi sosial yang dilakukan seseorang dengan sesamanya.",
            "Premis Mutlak Durkheimian, yang menyatakan simbol diciptakan oleh genetik biologis sejak zaman purba.",
            "Premis Fungsionalisme Parsonian, yang menolak adanya interpretasi subjektif dari pelaku sosial."
        ],
        "formula": {
            "title": "TIGA PREMIS INTERAKSIONISME SIMBOLIK HERBERT BLUMER",
            "latex": "\\begin{cases} \\mathbf{\\text{Premis 1:}} & \\text{Manusia bertindak berdasarkan makna yang diberikan pada objek} \\\\ \\mathbf{\\text{Premis 2:}} & \\text{Makna muncul dari interaksi sosial dengan orang lain} \\\\ \\mathbf{\\text{Premis 3:}} & \\mathbf{\\text{Makna dimodifikasi melalui proses interpretasi reflektif diri saat berinteraksi}} \\end{cases}",
            "legend": "• Menekankan sifat aktif dan kreatif manusia sebagai agen penafsir simbol dalam realitas sehari-hari"
        },
        "hints": {
            "concept": "Tiga premis Blumer: 1. Manusia bertindak berdasarkan makna; 2. Makna lahir dari interaksi sosial; 3. Makna dimodifikasi melalui proses penafsiran reflektif individu.",
            "execution": "Pilih: Premis Ketiga."
        }
    },
    {
        "id": "sos-sim-03",
        "materi": "KONFLIK SOSIAL & RESOLUSI KONFLIK",
        "topic": "Bentuk Akomodasi: Stalemate",
        "stem": "Dalam Perang Dingin antara Blok Barat (AS) dan Blok Timur (Uni Soviet), kedua negara adidaya saling bersaing dan mengancam dengan persenjataan nuklir mutakhir. Namun, perang terbuka antarkedua pihak tidak pernah pecah karena masing-masing pihak menyadari bahwa serangan nuklir pertama akan langsung dibalas dengan pemusnahan total kedua belah pihak (_Mutual Assured Destruction_). Bentuk akomodasi konflik tersebut dalam sosiologi dikenal sebagai...",
        "correct": "_Stalemate_, yaitu keadaan di mana pertentangan atau konflik terhenti dengan sendirinya pada suatu titik tertentu karena kedua pihak memiliki kekuatan yang seimbang sehingga tidak ada pihak yang dapat maju atau mundur.",
        "distractors": [
            "Ajudikasi, di mana kedua presiden menandatangani pengakuan bersalah di pengadilan hak asasi manusia.",
            "Koersi, di mana Uni Soviet berhasil menaklukkan Washington DC dengan serangan darat kilat.",
            "Mediasi, di mana pihak ketiga menetapkan sanksi denda finansial kepada kedua negara.",
            "Eliminasi, di mana salah satu pihak menyerah secara sukarela tanpa syarat."
        ],
        "formula": {
            "title": "BENTUK AKOMODASI STALEMATE",
            "latex": "\\text{Kekuatan Pihak A } (F_A) \\approx \\text{Kekuatan Pihak B } (F_B) \\implies \\text{Biaya Konflik Terlalu Hancur} \\implies \\mathbf{\\text{Stalemate (Jalan Buntu Damai Seimbang)}}",
            "legend": "• Contoh lain: Gencatan senjata di Semenanjung Korea di sepanjang Garis Lintang 38°"
        },
        "hints": {
            "concept": "Kondisi konflik terhenti otomatis karena kekuatan kedua pihak seimbang dan saling mengunci sehingga tidak ada yang bisa menang disebut Stalemate.",
            "execution": "Pilih: Stalemate."
        }
    },
    {
        "id": "sos-sim-04",
        "materi": "SOSIALISASI & MEDIA MASSA",
        "topic": "Pengaruh Media Massa Algoritmik dalam Sosialisasi Sekunder Remaja",
        "stem": "Sebuah penelitian sosiologis pada remaja perkotaan menunjukkan bahwa paparan konten video pendek berdurasi singkat di media sosial secara terus-menerus membentuk persepsi mereka mengenai standar tubuh ideal (_body image_), gaya busana, hingga kosakata gaul baru. Ditinjau dari fungsi sosialisasi sekunder, peran media massa algoritmik tersebut beroperasi melalui mekanisme...",
        "correct": "Penanaman norma dan pembentukan habitus baru secara difusif melalui repetisi simbolik yang mengarahkan pembentukan konsep diri (_self-concept_) dan konformitas gaya hidup kelompok sebaya daring.",
        "distractors": [
            "Pemaksaan fisik secara militer yang mewajibkan remaja menyetorkan uang jajan ke rekening pengembang aplikasi.",
            "Pemberian sertifikat ijazah profesi hukum yang diakui resmi oleh Mahkamah Konstitusi.",
            "Penggantian ikatan biologis orang tua kandung secara administratif menurut undang-undang perdata.",
            "Pemberian vaksin kekebalan tubuh terhadap penyakit infeksi menular secara otomatis."
        ],
        "formula": {
            "title": "MEKANISME SOSIALISASI MEDIA MASSA KONTEMPORER",
            "latex": "\\text{Algoritma Kurasi Konten} \\xrightarrow{\\text{Repetisi Simbolik}} \\text{Kultivasi Nilai \\& Standar Sosial} \\implies \\mathbf{\\text{Konformitas Identitas \\& Konsumsi}}",
            "legend": "• George Gerbner: Teori Kultivasi (_Cultivation Theory_) membuktikan paparan media jangka panjang membentuk konstruksi realitas sosial"
        },
        "hints": {
            "concept": "Media massa sebagai agen sosialisasi sekunder bekerja melalui repetisi simbolik yang membentuk habitus, konsep diri, dan konformitas gaya hidup.",
            "execution": "Pilih: Penanaman norma dan pembentukan habitus baru secara difusif melalui repetisi simbolik yang mengarahkan konsep diri."
        }
    },
    {
        "id": "sos-sim-05",
        "materi": "KELOMPOK SOSIAL & STRUKTUR SOSIAL",
        "topic": "Kelompok Primer (Primary Group) Charles Horton Cooley",
        "stem": "Charles Horton Cooley membagi kelompok sosial menjadi kelompok primer (_primary group_) dan kelompok sekunder (_secondary group_). Karakteristik mendasar yang menjadikan kelompok primer (seperti keluarga batih dan sahabat karib) sangat krusial bagi kehidupan individu adalah...",
        "correct": "Hubungan antaranggota bersifat tatap muka langsung (_face-to-face_), intim, personal, mendalam, dan memiliki keterikatan afeksi emosional yang menjadi wadah utama pembentukan kepribadian dasar manusia.",
        "distractors": [
            "Hubungan antaranggotanya diatur oleh anggaran dasar formal tertulis dan terbatas pada urusan bisnis kantor.",
            "Jumlah anggotanya mencapai puluhan ribu orang yang tersebar di berbagai benua tanpa pernah bertemu langsung.",
            "Keanggotaan dapat diperjualbelikan melalui bursa efek dengan sertifikat kepemilikan modal saham.",
            "Kelompok ini hanya beranggotakan para pejabat kementerian yang memegang kekuasaan politik eksekutif."
        ],
        "formula": {
            "title": "COOLEY: PRIMARY GROUP VS SECONDARY GROUP",
            "latex": "\\begin{cases} \\mathbf{\\text{Kelompok Primer:}} & \\mathbf{\\text{Tatap Muka Langsung, Intim, Personal, Emosional, Jumlah Kecil (Keluarga, Sahabat)}} \\\\ \\mathbf{\\text{Kelompok Sekunder:}} & \\text{Formal, Impersonal, Kontraktual, Spesifik, Skala Besar (Organisasi, Serikat, PT)} \\end{cases}",
            "legend": "• Kelompok primer merupakan agen pertama pencetak nilai-nilai kemanusiaan dasar"
        },
        "hints": {
            "concept": "Kelompok primer Cooley: tatap muka langsung (face to face), intim, personal, hubungan batin mendalam, pembentuk kepribadian dasar (keluarga, sahabat karib).",
            "execution": "Pilih opsi: Hubungan tatap muka langsung (face-to-face), intim, personal, mendalam, dan keterikatan afeksi emosional."
        }
    },
    {
        "id": "sos-lat-m-06",
        "materi": "STRATIFIKASI SOSIAL & KETIMPANGAN GENDER",
        "topic": "Manifestasi Ketimpangan Gender: Beban Ganda (Double Burden) dan Subordinasi",
        "stem": "Seorang perempuan yang bekerja purnawaktu sebagai akuntan di sebuah perusahaan tetap dituntut oleh norma masyarakatnya untuk menyelesaikan seluruh pekerjaan domestik rumah tangga (memasak, mencuci baju, membersihkan rumah, dan merawat anak) tanpa bantuan suami sepulang dari kantor. Dalam sosiologi gender, kondisi ketidakadilan tersebut dinamakan...",
        "correct": "Beban Ganda (_Double Burden_), yaitu bentuk ketimpangan gender di mana perempuan memikul beban kerja produktif di ranah publik sekaligus beban kerja domestik reproduktif di ranah domestik secara berlebihan.",
        "distractors": [
            "Marginalisasi ekonomi murni, di mana perempuan dilarang membuka rekening tabungan bank sendiri.",
            "Stereotipe gender pelabelan, di mana perempuan dianggap selalu lebih emosional daripada laki-laki.",
            "Kekerasan fisik domestik langsung yang mengakibatkan luka fisik berat pada tubuh korban.",
            "Emansipasi wanita sempurna, di mana beban kerja telah terbagi rata secara profesional."
        ],
        "formula": {
            "title": "BENTUK-BENTUK KETIDAKADILAN GENDER (GENDER INEQUALITY)",
            "latex": "\\begin{cases} \\mathbf{\\text{1. Marginalisasi:}} & \\text{Peminggiran ekonomi perempuan dari akses modal/pekerjaan} \\\\ \\mathbf{\\text{2. Subordinasi:}} & \\text{Anggapan kedudukan perempuan nomor dua di bawah laki-laki} \\\\ \\mathbf{\\text{3. Stereotipe:}} & \\text{Pelabelan negatif sepihak berdasarkan jenis kelamin} \\\\ \\mathbf{\\text{4. Kekerasan:}} & \\text{Kekerasan fisik, psikis, atau seksual berbasis gender} \\\\ \\mathbf{\\text{5. Beban Ganda:}} & \\mathbf{\\text{Beban kerja domestik + publik ditanggung sendirian oleh perempuan}} \\end{cases}",
            "legend": "• Menghambat pemberdayaan perempuan dan pencapaian Sustainable Development Goals (SDG 5)"
        },
        "hints": {
            "concept": "Perempuan yang bekerja mencari nafkah di kantor sekaligus memikul seluruh pekerjaan rumah tangga domestik sendirian mengalami Beban Ganda (Double Burden).",
            "execution": "Pilih: Beban Ganda (Double Burden)."
        }
    },
    {
        "id": "sos-sim-07",
        "materi": "STRATIFIKASI SOSIAL & MOBILITAS SOSIAL",
        "topic": "Mobilitas Sosial Vertikal Turun (Social Sinking) Akibat Disrupsi Teknologi",
        "stem": "Seorang pemilik studio foto tradisional dan gerai cetak klise analog yang sebelumnya mapan dan berpenghasilan tinggi terpaksa menutup usahanya karena bangkrut setelah munculnya kamera telepon pintar digital dan platform media sosial. Kini ia beralih profesi menjadi kurir pengantar paket lepas dengan penghasilan tidak menentu. Fenomena perpindahan posisi sosial tersebut merupakan contoh dari...",
        "correct": "Mobilitas Sosial Vertikal Turun (_Social Sinking_) intragenerasi.",
        "distractors": [
            "Mobilitas Sosial Vertikal Naik (_Social Climbing_) antargenerasi.",
            "Mobilitas Sosial Horizontal, karena kedua profesi tersebut sama-sama membutuhkan penggunaan sepeda motor.",
            "Mobilitas Struktural Positif, yang menaikkan status ekonomi seluruh keluarga besarnya.",
            "Stagnasi sosial tertutup yang dialami oleh masyarakat kasta sudra di masa feodal."
        ],
        "formula": {
            "title": "MEKANISME SOCIAL SINKING INTRAGENERASI",
            "latex": "\\text{Pengusaha Studio Mapan (Kelas Menengah Atas)} \\xrightarrow{\\text{Disrupsi Inovasi / Kebangkrutan}} \\text{Kurir Lepas (Kelas Bawah)} \\implies \\mathbf{\\text{Social Sinking Intragenerasi}}",
            "legend": "• Intragenerasi: Penurunan dialami oleh orang yang sama dalam kurun masa hidupnya sendiri"
        },
        "hints": {
            "concept": "Dari pengusaha studio foto mapan turun menjadi kurir lepas berpenghasilan tidak menentu dalam masa hidupnya sendiri = Mobilitas Sosial Vertikal Turun (Social Sinking) intragenerasi.",
            "execution": "Pilih: Mobilitas Sosial Vertikal Turun (Social Sinking) intragenerasi."
        }
    },
    {
        "id": "sos-sim-08",
        "materi": "STRATIFIKASI SOSIAL & KEKUASAAN POLITIK",
        "topic": "Hukum Besi Oligarki (Iron Law of Oligarchy) Robert Michels",
        "stem": "Sosiolog politik Robert Michels merumuskan tesis terkenal 'Hukum Besi Oligarki' (_Iron Law of Oligarchy_). Makna dari hukum sosiologis tersebut dalam konteks organisasi modern dan partai politik adalah...",
        "correct": "Setiap organisasi formal berskala besar (bahkan yang semula didirikan atas dasar cita-cita demokrasi sekalipun) pada akhirnya pasti akan dikuasai dan dikendalikan oleh segelintir elit kecil pengurus yang mempertahankan kekuasaan demi kepentingan kelompoknya sendiri.",
        "distractors": [
            "Seluruh partai politik pasti akan membubarkan diri secara sukarela setelah memenangkan pemilihan umum.",
            "Masyarakat selalu dipimpin oleh seorang kaisar turun-temurun yang memiliki kekuatan supranatural gaib.",
            "Kekuasaan politik selalu terdistribusi secara merata kepada seluruh anggota partai hingga tingkat ranting terendah.",
            "Partai politik diwajibkan oleh konstitusi untuk membagikan seluruh aset keuangannya kepada warga miskin."
        ],
        "formula": {
            "title": "HUKUM BESI OLIGARKI ROBERT MICHELS",
            "latex": "\\text{Organisasi Skala Besar} \\implies \\text{Spesialisasi \\& Birokratisasi} \\implies \\mathbf{\\text{Kekuasaan Terkonsentrasi pada Segelintir Elit (Oligarki)}}",
            "legend": "• Slogan Michels: _'Who says organization, says oligarchy'_ (Barangsiapa mengatakan organisasi, ia mengatakan oligarki)"
        },
        "hints": {
            "concept": "Iron Law of Oligarchy (Robert Michels): semua organisasi besar (termasuk partai demokratis) pasti berujung dikuasai oleh segelintir elit kecil (oligarki) yang melanggengkan kekuasaan.",
            "execution": "Pilih opsi: Setiap organisasi besar pada akhirnya pasti akan dikuasai oleh segelintir elit kecil pengurus demi kepentingan kelompoknya."
        }
    },
    {
        "id": "sos-sim-09",
        "materi": "PENYIMPANGAN SOSIAL & PENGENDALIAN SOSIAL",
        "topic": "Penyimpangan Primer vs Penyimpangan Sekunder Edwin M. Lemert",
        "stem": "Edwin M. Lemert membagi perilaku menyimpang menjadi dua tingkatan: Penyimpangan Primer (_Primary Deviance_) dan Penyimpangan Sekunder (_Secondary Deviance_). Karakteristik utama dari Penyimpangan Primer yang membedakannya dari penyimpangan sekunder adalah...",
        "correct": "Penyimpangan bersifat temporer (sementara), tidak dilakukan secara berulang, pelakunya masih dapat diterima oleh masyarakat umum, dan tindakan tersebut tidak menjadi bagian dari gaya hidup permanen pelakunya.",
        "distractors": [
            "Penyimpangan yang dilakukan berulang kali oleh residivis kejahatan berat yang sudah keluar masuk penjara berkali-kali.",
            "Penyimpangan yang pelakunya telah membentuk geng kriminal terorganisir dan memiliki senjata api rakitan.",
            "Penyimpangan yang mengakibatkan pembubaran parlemen negara dan perubahan konstitusi undang-undang dasar.",
            "Penyimpangan yang dilakukan secara terang-terangan di hadapan majelis hakim pengadilan internasional."
        ],
        "formula": {
            "title": "LEMERT: PENYIMPANGAN PRIMER VS SEKUNDER",
            "latex": "\\begin{cases} \\mathbf{\\text{Penyimpangan Primer:}} & \\mathbf{\\text{Temporer, tidak berulang, dapat ditolerir masyarakat, peran sosial tidak runtuh}} \\\\ \\mathbf{\\text{Penyimpangan Sekunder:}} & \\text{Berulang, gaya hidup permanen, telah dilabeli jahat, identitas diri residivis} \\end{cases}",
            "legend": "• Contoh primer: Terlambat masuk kelas sesekali; Contoh sekunder: Gembong pengedar narkoba"
        },
        "hints": {
            "concept": "Penyimpangan primer = temporer, insidental, pelakunya masih diterima masyarakat, belum menjadi gaya hidup. Penyimpangan sekunder = permanen, berulang, diinternalisasi sebagai gaya hidup dan identitas diri.",
            "execution": "Pilih: Penyimpangan bersifat temporer, tidak berulang, pelakunya masih diterima masyarakat, dan bukan gaya hidup permanen."
        }
    },
    {
        "id": "sos-sim-10",
        "materi": "PENYIMPANGAN SOSIAL & TEORI KRIMINOLOGI",
        "topic": "Teknik Netralisasi (Techniques of Neutralization) Sykes dan Matza",
        "stem": "Gresham M. Sykes dan David Matza menyatakan bahwa para pelaku kejahatan dan pelanggar norma sosial sering kali tidak menolak nilai-nilai moral masyarakat secara mutlak, melainkan menggunakan 'Teknik Netralisasi' untuk membenarkan tindakan melanggar hukum di hadapan nuraninya sendiri. Seorang siswa yang tertangkap menyontek lalu membela diri dengan berkata, *'Guru kami tidak pernah mengajar materi ini dengan jelas dan sengaja membuat soal yang mustahil dikerjakan!'*, menerapkan teknik netralisasi berupa...",
        "correct": "Mengutuk yang Mengutuk (_Condemnation of the Condemners_), di mana pelaku menyangkal kesalahannya dengan cara menyerang motif, keadilan, atau perilaku pihak yang berwenang menghukumnya.",
        "distractors": [
            "Penyangkalan Tanggung Jawab (_Denial of Responsibility_), dengan menyatakan dirinya dipaksa oleh takdir gaib.",
            "Penyangkalan Kerugian (_Denial of Injury_), dengan menyatakan tidak ada satu orang pun yang dirugikan secara materi.",
            "Penyangkalan Korban (_Denial of the Victim_), dengan menyatakan korban memang pantas menerima perlakuan buruk tersebut.",
            "Banding ke Loyalitas yang Lebih Tinggi (_Appeal to Higher Loyalties_), demi membela kehormatan geng persaudaraan."
        ],
        "formula": {
            "title": "LIMA TEKNIK NETRALISASI SYKES DAN MATZA",
            "latex": "\\begin{cases} \\text{1. Denial of Responsibility:} & \\text{'Itu bukan salah saya, saya dipaksa keadaan'} \\\\ \\text{2. Denial of Injury:} & \\text{'Toh tidak ada orang yang terluka / rugi'} \\\\ \\text{3. Denial of the Victim:} & \\text{'Dia memang pantas mendapatkannya'} \\\\ \\mathbf{\\text{4. Condemnation of Condemners:}} & \\mathbf{\\text{'Kalian para guru/polisi juga munafik \\& tidak adil'}} \\\\ \\text{5. Appeal to Higher Loyalties:} & \\text{'Saya lakukan demi solidaritas teman/keluarga'} \\end{cases}",
            "legend": "• Pelaku menggunakan rasionalisasi kognitif ini sebelum atau sesudah melakukan penyimpangan sosial"
        },
        "hints": {
            "concept": "Sykes & Matza: Menyalahkan balik pihak guru/penilai yang dianggap tidak adil adalah teknik 'Condemnation of the Condemners' (Mengutuk yang Mengutuk).",
            "execution": "Pilih: Mengutuk yang Mengutuk (Condemnation of the Condemners)."
        }
    },
    {
        "id": "sos-sim-11",
        "materi": "KONFLIK SOSIAL & RESOLUSI KONFLIK",
        "topic": "Dinamika Pembentukan Kelompok Kepentingan Ralf Dahrendorf",
        "stem": "Dalam teori konflik Ralf Dahrendorf, proses terjadinya konflik sosial melibatkan transformasi dari kelompok semu (_quasi-group_) menjadi kelompok kepentingan (_interest-group_). Karakteristik dari 'Kelompok Semu' (_Quasi-Group_) sebelum meletusnya konflik terbuka adalah...",
        "correct": "Kumpulan individu yang menempati posisi kekuasaan yang sama dan memiliki kepentingan laten (tersembunyi) yang identik, namun belum terorganisir secara sadar dan belum memiliki struktur organisasi perlawanan bersama.",
        "distractors": [
            "Kelompok massa bersenjata yang telah menyatakan perang kemerdekaan secara resmi melalui siaran radio.",
            "Partai politik pemenang pemilu yang telah menguasai seluruh kursi di lembaga parlemen negara.",
            "Organisasi teroris transnasional yang memiliki markas bawah tanah di perbatasan benua.",
            "Sekelompok warga yang sedang berbelanja pakaian seragam di pasar swalayan tanpa kepentingan politik."
        ],
        "formula": {
            "title": "TRANSFORMASI KELOMPOK KONFLIK MENURUT DAHRENDORF",
            "latex": "\\text{Quasi-Group (Kelompok Semu: Kepentingan Laten)} \\xrightarrow{\\text{Kesadaran Kolektif \\& Pengorganisasian}} \\mathbf{\\text{Interest-Group (Kelompok Kepentingan: Kepentingan Manifes)}} \\xrightarrow{} \\text{Aksi Konflik Terbuka}",
            "legend": "• Syarat organisasi: kepemimpinan, ideologi tandingan, sarana komunikasi, dan kebebasan berkumpul"
        },
        "hints": {
            "concept": "Quasi-group (kelompok semu) Dahrendorf: individu yang berada dalam posisi yang sama dan memiliki kepentingan laten identik, tapi belum terorganisir dan belum sadar bergerak bersama.",
            "execution": "Pilih: Kumpulan individu yang menempati posisi sama dengan kepentingan laten, namun belum terorganisir secara sadar."
        }
    },
    {
        "id": "sos-sim-12",
        "materi": "KONFLIK SOSIAL & RESOLUSI KONFLIK",
        "topic": "Model Mediasi Transformatif (Transformative Mediation)",
        "stem": "Dalam menangani perseteruan warisan tanah yang meretakkan keharmonisan antarsaudara kandung, seorang mediator profesional menerapkan pendekatan 'Mediasi Transformatif' (_Transformative Mediation_). Tujuan utama dari mediasi transformatif yang membedakannya dari mediasi komersial biasa adalah...",
        "correct": "Fokus pada pemberdayaan para pihak (_empowerment_) dan pengakuan saling memahami perasaan (_recognition_), guna memulihkan relasi kemanusiaan yang retak alih-alih sekadar memaksakan pembagian nominal materi semata.",
        "distractors": [
            "Memaksa kedua pihak menjual tanah sengketa ke perusahaan swasta lalu membagi uangnya sama rata di kantor polisi.",
            "Menjatuhkan vonis hukuman penjara bagi saudara kandung yang berbicara dengan nada suara tinggi.",
            "Menyita tanah warisan tersebut menjadi aset milik pribadi sang mediator sebagai imbalan jasa konsultasi.",
            "Mengusir kedua pihak dari desa agar sengketa tersebut tidak membebani anggaran belanja daerah."
        ],
        "formula": {
            "title": "DUA PILAR UTAMA MEDIASI TRANSFORMATIF (BUSH & FOLGER)",
            "latex": "\\text{Mediasi Transformatif} \\iff \\mathbf{\\text{Empowerment (Pemberdayaan Kapasitas Diri)}} + \\mathbf{\\text{Recognition (Saling Mengakui Perspektif Lawan)}}",
            "legend": "• Mengubah pola interaksi destruktif menjadi konstruktif dalam memulihkan tatanan kohesi sosial keluarga"
        },
        "hints": {
            "concept": "Mediasi transformatif (Bush & Folger) bertujuan pada dua hal: Empowerment (pemberdayaan para pihak) dan Recognition (saling mengakui dan memahami perspektif lawan), memulihkan relasi sosial.",
            "execution": "Pilih: Fokus pada pemberdayaan (empowerment) dan pengakuan saling memahami (recognition) guna memulihkan relasi kemanusiaan."
        }
    },
    {
        "id": "sos-sim-13",
        "materi": "PERUBAHAN SOSIAL & INTEGRASI SOSIAL",
        "topic": "Proses Disorganisasi Sosial Menuju Reorganisasi Sosial",
        "stem": "Masuknya teknologi transportasi daring (ojek dan taksi online) pada masa awal kemunculannya sempat memicu gelombang demonstrasi anarkis dan bentrokan fisik di jalan raya dengan pengemudi angkutan konvensional. Namun, setelah pemerintah mengeluarkan regulasi zona penjemputan resmi dan tarif batas atas/bawah yang adil, kedua kelompok transportasi dapat beroperasi berdampingan secara tertib. Rangkaian proses perubahan sosial tersebut mencerminkan dinamika...",
        "correct": "Disorganisasi sosial sementara yang kemudian disusul oleh proses Reorganisasi sosial (pembentukan norma, aturan kelembagaan, dan struktur penyesuaian baru).",
        "distractors": [
            "Kehancuran peradaban total yang tidak mungkin pernah dipulihkan kembali oleh hukum negara.",
            "Penyimpangan sekunder permanen yang dilakukan oleh seluruh penduduk kota metropolitan.",
            "Kemunduran evolusi biologis masyarakat kota kembali ke zaman purba berburu dan meramu.",
            "Pembentukan kasta tertutup baru yang melarang perkawinan antarkeluarga pengemudi kendaraan."
        ],
        "formula": {
            "title": "DIALEKTIKA DISORGANISASI DAN REORGANISASI SOSIAL",
            "latex": "\\text{Inovasi Teknologi / Disrupsi} \\xrightarrow{\\text{Benturan Nilai \\& Norma Lama}} \\mathbf{\\text{Disorganisasi (Ketegangan/Konflik)}} \\xrightarrow{\\text{Adaptasi Regulasi Baru}} \\mathbf{\\text{Reorganisasi (Keseimbangan Baru / Equilibrium)}}",
            "legend": "• Menunjukkan elastisitas institusi masyarakat dalam mencapai ekuilibrium dinamis baru"
        },
        "hints": {
            "concept": "Perubahan sosial yang diawali kekacauan/konflik sementara saat norma lama runtuh (disorganisasi), lalu tercapai keseimbangan dan aturan baru (reorganisasi).",
            "execution": "Pilih: Disorganisasi sosial sementara yang disusul oleh proses Reorganisasi sosial."
        }
    },
    {
        "id": "sos-sim-14",
        "materi": "PERUBAHAN SOSIAL & TEORI EVOLUSI",
        "topic": "Teori Evolusi Sosio-Kultural Gerhard Lenski: Teknologi dan Surplus Informasi",
        "stem": "Sosiolog Gerhard Lenski dalam teori evolusi sosio-kulturalnya membagi tahapan perkembangan masyarakat berdasarkan tingkat teknologi yang dikuasai: masyarakat pemburu-peramu, hortikultura, pastoral, agraris, hingga masyarakat industri modern. Menurut Lenski, faktor paling menentukan yang memicu peningkatan stratifikasi ketimpangan sosial ekstrem pada masyarakat agraris tradisional adalah...",
        "correct": "Diciptakannya teknologi bajak bertenaga hewan dan irigasi yang melahirkan surplus pangan masif, di mana surplus tersebut kemudian dimonopoli dan dikuasai oleh segelintir elit penguasa feudal dan tuan tanah.",
        "distractors": [
            "Kepunahan total seluruh tanaman padi liar akibat bencana banjir bandang zaman glasial.",
            "Ketiadaan bahasa lisan yang membuat para petani tidak dapat berkomunikasi satu sama lain.",
            "Larangan dari dewan gereja abad pertengahan bagi kaum tani untuk mengonsumsi daging hewan.",
            "Penetapan undang-undang anti-monopoli yang membagi tanah negara secara gratis kepada seluruh budak."
        ],
        "formula": {
            "title": "TEORI EVOLUSI SOSIO-KULTURAL GERHARD LENSKI",
            "latex": "\\text{Kemajuan Teknologi Pertanian (Bajak Hewan)} \\implies \\mathbf{\\text{Surplus Pangan Berlebih}} \\xrightarrow{\\text{Monopoli Elit Feudal}} \\mathbf{\\text{Puncak Ketimpangan Stratifikasi Sosial Ekstrem}}",
            "legend": "• Pada masyarakat industri, ketimpangan kembali sedikit menurun berkat tuntutan demokratisasi dan pendidikan massal"
        },
        "hints": {
            "concept": "Lenski: pada masyarakat agraris, inovasi bajak hewan menciptakan surplus pangan masif. Surplus ini dimonopoli oleh raja/tuan tanah feodal, menciptakan puncak ketimpangan sosial tertinggi dalam sejarah.",
            "execution": "Pilih opsi: Teknologi bajak bertenaga hewan menghasilkan surplus pangan yang dimonopoli oleh elit penguasa feudal dan tuan tanah."
        }
    },
    {
        "id": "sos-sim-15",
        "materi": "PERUBAHAN SOSIAL & GLOBALISASI",
        "topic": "Konsep Glokalisasi (Glocalization) Roland Robertson",
        "stem": "Sebuah waralaba restoran cepat saji internasional asal Amerika Serikat yang beroperasi di Indonesia tidak hanya menjual menu burger sapi standar global, melainkan juga meluncurkan menu khusus burger nasi rendang, ayam goreng sambal ulek matah, dan minuman es cendol dawet. Sosiolog Roland Robertson mengkaji fenomena perpaduan antara produk global dan unsur kebudayaan lokal ini sebagai...",
        "correct": "Glokalisasi (_Glocalization_), yaitu proses interaksi dinamis di mana produk atau budaya global diadaptasi, dimodifikasi, dan disesuaikan dengan selera dan nilai-nilai kebudayaan lokal setempat.",
        "distractors": [
            "Imperialisme kultural mutlak, di mana budaya lokal dimusnahkan seratus persen oleh kekuatan korporasi asing.",
            "Westernisasi buta, di mana masyarakat Indonesia sepenuhnya meninggalkan seluruh makanan tradisional nenek moyang.",
            "Eksklusi ekonomi proteksionis, di mana pemerintah melarang seluruh investasi asing masuk ke pasar domestik.",
            "Konsumerisme regresif, yang memicu kepunahan seluruh sawah tanaman padi di pulau Jawa."
        ],
        "formula": {
            "title": "SINTESIS GLOKALISASI ROLAND ROBERTSON",
            "latex": "\\mathbf{\\text{Global (Standardisasi Dunia)}} + \\mathbf{\\text{Lokal (Konteks Kebudayaan Setempat)}} \\implies \\mathbf{\\text{Glokalisasi (Glocalization / Think Globally, Act Locally)}}",
            "legend": "• Membuktikan bahwa masyarakat lokal bukanlah penerima pasif, melainkan agen yang merekonstruksi produk global"
        },
        "hints": {
            "concept": "Glokalisasi (Roland Robertson): adaptasi produk atau nilai global agar sesuai dengan konteks dan cita rasa lokal (Think global, act local).",
            "execution": "Pilih: Glokalisasi (Glocalization)."
        }
    },
    {
        "id": "sos-sim-16",
        "materi": "MASALAH SOSIAL & TATA RUANG PERKOTAAN",
        "topic": "Fenomena Segregasi Keruangan: Gated Communities vs Slum Area",
        "stem": "Di kawasan pinggiran kota megapolitan metropolitan, tampak pemandangan kontras di mana kompleks perumahan mewah berpagar tinggi dengan penjagaan satpam privat dan kamera CCTV 24 jam (_gated communities_) berdiri berdampingan tepat di sebelah perkampungan kumuh padat tanpa sanitasi air bersih (_slum area_). Fenomena ini dalam sosiologi perkotaan dikaji sebagai...",
        "correct": "Segregasi Spasial Keruangan (_Spatial Segregation_), yang mencerminkan polarisasi kelas sosial ekonomi ekstrem yang diwujudkan dalam pemisahan fisik lingkungan tempat tinggal dan minimnya interaksi sosial antar-strata.",
        "distractors": [
            "Integrasi sosial fungsional sempurna, di mana warga kedua pemukiman saling bertukar rumah setiap akhir pekan.",
            "Akulturasi budaya arsitektur tradisional yang menjaga keharmonisan estetika lingkungan perdesaan.",
            "Bentuk gotong royong modern yang didanai sepenuhnya oleh kas rukun tetangga setempat.",
            "Hasil dari program pemerataan pembangunan nasional yang berhasil menghapus kesenjangan pendapatan."
        ],
        "formula": {
            "title": "SEGREGASI SPASIAL PERKOTAAN (SPATIAL SEGREGATION)",
            "latex": "\\text{Disparitas Pendapatan Ekstrem} \\implies \\begin{cases} \\mathbf{\\text{Gated Communities:}} & \\text{Enklave elit eksklusif, privatisasi keamanan, rasa takut kejahatan} \\\\ \\mathbf{\\text{Slum Areas:}} & \\text{Keterpinggiran spasial, defisit sanitasi, kerentanan penggusuran} \\end{cases} \\implies \\mathbf{\\text{Fraktur Sosial Kota}}",
            "legend": "• Memperlemah kohesi sosial dan menumbuhkan prasangka kelas antargolongan warga"
        },
        "hints": {
            "concept": "Pemisahan fisik tempat tinggal antara perumahan mewah berpagar tertutup (gated communities) dan kawasan kumuh (slums) mencerminkan Segregasi Spasial Keruangan (Spatial Segregation).",
            "execution": "Pilih: Segregasi Spasial Keruangan (Spatial Segregation)."
        }
    },
    {
        "id": "sos-sim-17",
        "materi": "MASALAH SOSIAL & KETIMPANGAN SOSIAL",
        "topic": "Analisis Sosiologis Lingkaran Setan Kemiskinan (Vicious Circle of Poverty)",
        "stem": "Ragnar Nurkse merumuskan teori 'Lingkaran Setan Kemiskinan' (_The Vicious Circle of Poverty_). Dalam perspektif sosiologi pendidikan dan keluarga, rantai jebakan kemiskinan antargenerasi tersebut beroperasi melalui siklus kausalitas...",
        "correct": "Keluarga miskin berpendapatan rendah $\\to$ ketidakmampuan membiayai nutrisi gizi anak dan pendidikan bermutu $\\to$ anak putus sekolah dan kekurangan keterampilan keahlian $\\to$ anak hanya terserap di sektor kerja informal berupah rendah saat dewasa $\\to$ melahirkan keluarga miskin baru.",
        "distractors": [
            "Keluarga kaya membagi seluruh warisannya kepada pengemis $\\to$ pengemis menjadi jutawan $\\to$ jutawan membeli bank $\\to$ bank membebaskan bunga.",
            "Pemerintah menaikkan pajak ekspor $\\to$ mata uang melemah $\\to$ rakyat menolak bekerja $\\to$ negara dibubarkan dewan keamanan PBB.",
            "Anak petani memenangkan medali emas olimpiade $\\to$ diangkat menjadi menteri $\\to$ seluruh petani menjadi konglomerat seketika.",
            "Kemiskinan terjadi murni karena adanya kutukan mistis yang diwariskan melalui garis keturunan ibu kandung."
        ],
        "formula": {
            "title": "SIKLUS PERANGKAP KEMISKINAN ANTARGENERASI",
            "latex": "\\text{Pendapatan Rendah} \\to \\text{Gizi/Kesehatan Buruk} \\to \\text{Pendidikan Rendah} \\to \\text{Produktivitas/Karier Rendah} \\to \\mathbf{\\text{Kemiskinan Berulang}}",
            "legend": "• Pemutus rantai paling efektif: Intervensi gizi 1.000 Hari Pertama Kehidupan (HPK) dan beasiswa pendidikan vokasi/tinggi berkualitas"
        },
        "hints": {
            "concept": "Vicious circle of poverty dalam sosiologi: Pendapatan rendah -> defisit gizi & pendidikan anak -> rendahnya keahlian kerja saat dewasa -> pendapatan rendah berulang pada generasi berikutnya.",
            "execution": "Pilih opsi rantai kausalitas: Keluarga miskin berpendapatan rendah -> tak mampu biaya nutrisi/sekolah -> putus sekolah/keahlian rendah -> kerja informal upah rendah -> keluarga miskin baru."
        }
    },
    {
        "id": "sos-sim-18",
        "materi": "KEARIFAN LOKAL & PEMBERDAYAAN KOMUNITAS",
        "topic": "Kearifan Lokal Subak di Bali sebagai Integrasi Ekologis dan Religius (Tri Hita Karana)",
        "stem": "Sistem irigasi pertanian tradisional _Subak_ di Bali telah diakui oleh UNESCO sebagai Warisan Budaya Dunia. Dalam perspektif sosiologi lingkungan, keunggulan tata kelola Subak yang mampu bertahan selama lebih dari seribu tahun terletak pada penerjemahan filosofi kearifan lokal 'Tri Hita Karana' ke dalam tata kelola sosial, yaitu...",
        "correct": "Menjaga keseimbangan harmonis antara hubungan manusia dengan Sang Pencipta (_Parahyangan_ melalui pura pura air), hubungan harmonis antarsesama manusia (_Pawongan_ melalui musyawarah gotong royong pembagian debit air yang adil), dan hubungan harmonis manusia dengan alam lingkungan (_Palemahan_ melalui rotasi tanam serentak pencegah hama).",
        "distractors": [
            "Penjualan hak guna air irigasi kepada konglomerat perhotelan swasta asing dengan harga komersial tertinggi.",
            "Pemberian hak monopoli air mutlak kepada kepala desa terkaya tanpa kewajiban membagi kepada petani miskin.",
            "Penggunaan pestisida kimia beracun dosis tinggi secara rahasia di malam hari untuk membasmi burung sawah.",
            "Pemberantasan seluruh tradisi ritual keagamaan di sawah demi mengejar target panen padi empat kali setahun."
        ],
        "formula": {
            "title": "TRILOGI TRI HITA KARANA DALAM SISTEM SUBAK",
            "latex": "\\text{Kearifan Subak} \\equiv \\begin{cases} \\mathbf{\\text{Parahyangan:}} & \\text{Harmoni Teologis: Pura Ulun Danu, Pura Tirta} \\\\ \\mathbf{\\text{Pawongan:}} & \\mathbf{\\text{Harmoni Sosial: Musyawarah mufakat, transparansi alokasi debit air}} \\\\ \\mathbf{\\text{Palemahan:}} & \\text{Harmoni Ekologis: Manajemen terasering, siklus bera, bebas hama alami} \\end{cases}",
            "legend": "• Menjadi model kelembagaan pengelolaan sumber daya milik bersama (_Common Pool Resources_) dunia"
        },
        "hints": {
            "concept": "Subak di Bali berlandaskan filosofi Tri Hita Karana: Parahyangan (manusia dengan Tuhan/pura air), Pawongan (manusia dengan sesama/gotong royong adil alokasi air), Palemahan (manusia dengan alam/tata rotasi tanam).",
            "execution": "Pilih opsi yang menjabarkan keseimbangan Parahyangan (pura air), Pawongan (musyawarah pembagian air adil), dan Palemahan (rotasi tanam serentak)."
        }
    },
    {
        "id": "sos-sim-19",
        "materi": "KEARIFAN LOKAL & PEMBERDAYAAN KOMUNITAS",
        "topic": "Tangga Partisipasi Warga Sherry Arnstein: Partisipasi Semu vs Kontrol Warga",
        "stem": "Sherry Arnstein dalam artikel klasiknya _A Ladder of Citizen Participation_ merumuskan 8 anak tangga partisipasi masyarakat dalam program pembangunan. Kondisi di mana warga desa diundang menghadiri rapat di balai desa hanya untuk mendengarkan pidato pejabat dan diminta menandatangani daftar hadir agar proyek terlihat sah di atas kertas, namun masukan aspirasi warga sama sekali tidak didengar atau diakomodasi, berada pada tingkatan...",
        "correct": "Partisipasi Semu / Simbolis (_Tokenism_), di mana keterlibatan warga hanya sebagai formalitas permukaan (seperti sekadar diinformasikan atau diajak konsultasi pura-pura) tanpa adanya pemberian kekuasaan nyata (_citizen power_).",
        "distractors": [
            "Kontrol Warga Penuh (_Citizen Control_), di mana warga memegang wewenang penuh dalam perencanaan dan penggunaan anggaran.",
            "Kemitraan Sejajar (_Partnership_), di mana warga dan pemerintah berbagi kekuasaan dan tanggung jawab secara berimbang.",
            "Delegasi Kekuasaan (_Delegated Power_), di mana warga memegang hak veto terhadap setiap rancangan kebijakan publik.",
            "Kondisi Anarki Murni, di mana masyarakat desa mengusir seluruh aparat birokrasi dari wilayahnya."
        ],
        "formula": {
            "title": "TANGGA PARTISIPASI WARGA SHERRY ARNSTEIN (1969)",
            "latex": "\\begin{cases} \\mathbf{\\text{Citizen Power (Kekuasaan Riil):}} & \\text{Citizen Control } \\to \\text{ Delegated Power } \\to \\text{ Partnership} \\\\ \\mathbf{\\text{Tokenism (Partisipasi Semu):}} & \\mathbf{\\text{Placation } \\to \\text{ Consultation } \\to \\text{ Informing (Sekadar Diberi Tahu/Daftar Hadir)}} \\\\ \\mathbf{\\text{Non-Participation:}} & \\text{Therapy } \\to \\text{ Manipulation (Eksploitasi Warga Tanpa Suara)} \\end{cases}",
            "legend": "• Pemberdayaan sejati harus mencapai anak tangga kemitraan dan kontrol warga penuh"
        },
        "hints": {
            "concept": "Arnstein Ladder of Participation: Warga hanya diundang hadir tanda tangan tanpa didengar aspirasinya = Tokenism (partisipasi semu/simbolis).",
            "execution": "Pilih: Partisipasi Semu / Simbolis (Tokenism)."
        }
    },
    {
        "id": "sos-sim-20",
        "materi": "METODOLOGI PENELITIAN SOSIAL",
        "topic": "Uji Hipotesis Hubungan Antar-Variabel Penelitian Sosial Kuantitatif",
        "stem": "Seorang mahasiswa sosiologi meneliti hubungan antara Tingkat Pendidikan Orang Tua (Variabel Bebas / $X$) dengan Tingkat Aspirasi Melanjutkan Studi Anak ke Perguruan Tinggi (Variabel Terikat / $Y$). Berdasarkan analisis uji korelasi Pearson, diperoleh nilai koefisien korelasi $r = +0{,}78$ dengan nilai signifikansi $p = 0{,}001$ ($p < 0{,}05$). Kesimpulan sosiologis dan metodologis yang valid dari hasil penelitian tersebut adalah...",
        "correct": "Terdapat hubungan positif yang kuat dan signifikan secara statistik antara tingkat pendidikan orang tua dengan aspirasi studi anak; semakin tinggi tingkat pendidikan orang tua, semakin tinggi pula dorongan aspirasi pendidikan anak ke perguruan tinggi.",
        "distractors": [
            "Tingkat pendidikan orang tua tidak memiliki pengaruh apa pun terhadap masa depan anak.",
            "Terdapat hubungan negatif sempurna di mana orang tua berpendidikan tinggi selalu melarang anaknya kuliah.",
            "Nilai signifikansi membuktikan bahwa data yang dikumpulkan oleh peneliti palsu dan melanggar hukum.",
            "Semua anak dari keluarga buta huruf dipastikan tidak memiliki cita-cita hidup sama sekali."
        ],
        "formula": {
            "title": "INTERPRETASI KOEFISIEN KORELASI PEARSON (R)",
            "latex": "\\begin{aligned} r & = +0{,}78 \\implies \\mathbf{\\text{Korelasi Positif Kuat }} (0{,}70 \\le r < 0{,}90) \\\\ p & = 0{,}001 < \\alpha = 0{,}05 \\implies \\mathbf{\\text{Tolak } H_0 \\text{ (Hubungan Signifikan Bukan Kebetulan Acak)}} \\end{aligned}",
            "legend": "• Menunjukkan peran modal budaya keluarga (_cultural capital_) dalam menumbuhkan motivasi prestasi anak"
        },
        "hints": {
            "concept": "Nilai r = +0,78 (positif kuat) dan p = 0,001 (< 0,05 signifikan). Berarti terdapat hubungan positif kuat dan signifikan antara pendidikan orang tua dan aspirasi kuliah anak.",
            "execution": "Pilih opsi yang menyatakan adanya hubungan positif yang kuat dan signifikan secara statistik."
        }
    },
    {
        "id": "sos-sim-21",
        "materi": "KONSEP DASAR & TEORI SOSIOLOGI",
        "topic": "Etnometodologi Harold Garfinkel: Eksperimen Pelanggaran (Breaching Experiments)",
        "stem": "Sosiolog Harold Garfinkel menciptakan metode 'Eksperimen Pelanggaran' (_Breaching Experiments_) dalam kajian Etnometodologi. Dalam eksperimen ini, para mahasiswa diminta pulang ke rumah orang tua mereka lalu bertindak kaku layaknya tamu penginapan asing yang sopan berlebihan (misalnya meminta izin resmi sebelum membuka lemari es atau menawarkan uang sewa kamar). Tujuan ilmiah dari metode eksperimen pelanggaran Garfinkel tersebut adalah...",
        "correct": "Membongkar dan menyingkap aturan-aturan tak terucapkan (_taken-for-granted assumptions_) dan norma tersembunyi yang menopang keteraturan interaksi sosial sehari-hari masyarakat yang biasanya tidak disadari oleh para pelakunya.",
        "distractors": [
            "Menguji ketahanan fisik para mahasiswa terhadap pukulan kemarahan orang tua di ruang makan.",
            "Mendorong anak-anak muda untuk memutuskan tali silaturahmi keluarga secara permanen.",
            "Membuktikan bahwa orang tua tidak memiliki kasih sayang biologis terhadap anak kandungnya.",
            "Mengumpulkan bukti tindak pidana penipuan perhotelan yang dilakukan oleh orang tua di rumah."
        ],
        "formula": {
            "title": "PRINSIP ETNOMETODOLOGI HAROLD GARFINKEL",
            "latex": "\\text{Melanggar Norma Spontan (Breaching)} \\implies \\text{Kebingungan / Kemarahan Subjek} \\implies \\mathbf{\\text{Aturan Tak Tertulis (Taken-for-Granted) Terungkap Gamblang}}",
            "legend": "• Etnometodologi mempelajari metode-metode praktis yang digunakan orang awam dalam menata kehidupan sehari-harinya"
        },
        "hints": {
            "concept": "Breaching experiments Garfinkel sengaja melanggar norma kewajaran sehari-hari untuk mengungkap aturan tak tertulis (taken-for-granted rules) yang menopang keteraturan sosial.",
            "execution": "Pilih: Membongkar aturan tak terucapkan (taken-for-granted assumptions) dan norma tersembunyi yang menopang keteraturan sosial sehari-hari."
        }
    },
    {
        "id": "sos-sim-22",
        "materi": "METODOLOGI PENELITIAN SOSIAL",
        "topic": "Etika Penelitian Sosial: Persetujuan Setelah Penjelasan (Informed Consent)",
        "stem": "Sebelum melakukan wawancara mendalam mengenai riwayat trauma perundungan (_bullying_) pada siswa SMA, peneliti memberikan lembar penjelasan lengkap mengenai tujuan penelitian, jaminan kerahasiaan identitas nama samaran (_anonymity_), hak untuk menolak menjawab pertanyaan sensitif, dan hak untuk mengundurkan diri kapan saja tanpa sanksi apa pun. Lembar persetujuan sukarela yang ditandatangani oleh responden tersebut dinamakan...",
        "correct": "_Informed Consent_ (Persetujuan Setelah Penjelasan Lengkap).",
        "distractors": [
            "Surat Perjanjian Utang Piutang Bermeterai Sepuluh Ribu Rupiah.",
            "Surat Pernyataan Pelepasan Hak Asasi Manusia di Hadapan Notaris.",
            "Surat Kuasa Khusus Pengalihan Seluruh Aset Kekayaan Responden.",
            "Surat Perintah Penahanan Sementara dari Kejaksaan Negeri."
        ],
        "formula": {
            "title": "STANDAR ETIKA RISET SOSIAL KONTEMPORER",
            "latex": "\\text{Etika Riset} \\equiv \\begin{cases} \\mathbf{\\text{1. Informed Consent:}} & \\mathbf{\\text{Persetujuan sukarela setelah memahami tujuan \\& risiko riset}} \\\\ \\mathbf{\\text{2. Anonymity \\& Confidentiality:}} & \\text{Kerahasiaan identitas \\& privasi data subjek penelitian} \\\\ \\mathbf{\\text{3. Do No Harm:}} & \\text{Perlindungan dari bahaya fisik, psikologis, maupun sosial} \\end{cases}",
            "legend": "• Pelanggaran etika riset membatalkan keabsahan moral dan legal karya ilmiah di komunitas akademik internasional"
        },
        "hints": {
            "concept": "Lembar persetujuan sukarela responden setelah memahami tujuan, hak, dan jaminan kerahasiaan penelitian disebut Informed Consent.",
            "execution": "Pilih: Informed Consent (Persetujuan Setelah Penjelasan Lengkap)."
        }
    },
    {
        "id": "sos-sim-23",
        "materi": "KELOMPOK SOSIAL & BUDAYA POPULER",
        "topic": "Fenomena Neotribalisme Michel Maffesoli dalam Komunitas Penggemar Daring",
        "stem": "Sosiolog Prancis Michel Maffesoli mencetuskan konsep 'Neotribalisme' (_Neo-tribalism_) untuk mendeskripsikan dinamika kelompok masyarakat pascamodern. Karakteristik dari kelompok suku-suku baru (_tribes_) era kontemporer seperti komunitas penggemar musik K-Pop, komunitas otomotif, atau komunitas gim daring adalah...",
        "correct": "Kelompok terbentuk atas dasar kesamaan selera emosional, hobi, dan gaya hidup sesaat, dengan struktur ikatan yang cair, keanggotaan lintas batas geografis nasional yang fleksibel, dan tidak menuntut komitmen seumur hidup.",
        "distractors": [
            "Kelompok terbentuk berdasarkan garis keturunan darah leluhur purba yang wajib tinggal di dalam satu rumah adat yang sama.",
            "Kelompok memiliki pasukan bersenjata tajam yang bertugas memerangi kelompok suku tetangga setiap malam.",
            "Keanggotaan bersifat tertutup kaku di mana anggotanya dilarang menikah dengan orang di luar marga kelompok.",
            "Kelompok didirikan oleh dekrit presiden militer dan anggotanya wajib membayar upeti hasil bumi sebulan sekali."
        ],
        "formula": {
            "title": "NEOTRIBALISME MICHEL MAFFESOLI DI ERA PASCAMODERN",
            "latex": "\\text{Komunitas Era Baru} \\equiv \\mathbf{\\text{Afeksi Emosional}} + \\mathbf{\\text{Ikatan Cair/Fleksibel}} + \\mathbf{\\text{Lintas Geografis (Global)}} + \\mathbf{\\text{Berbasis Minat/Gaya Hidup}}",
            "legend": "• Menggantikan ikatan kelas sosial konvensional dengan identitas komunitas kultural sementara"
        },
        "hints": {
            "concept": "Neotribalisme Maffesoli: kelompok komunitas baru berbasis kesamaan emosional, hobi, dan gaya hidup (fandom, gamer), ikatannya cair dan fleksibel lintas batas negara.",
            "execution": "Pilih opsi: Kelompok terbentuk atas dasar kesamaan selera emosional/hobi, struktur cair, keanggotaan fleksibel lintas geografis."
        }
    },
    {
        "id": "sos-sim-24",
        "materi": "PERUBAHAN SOSIAL & STRUKTUR SOSIAL",
        "topic": "Kesenjangan Generasi (Generation Gap) dalam Etos Kerja dan Nilai Budaya",
        "stem": "Dalam sebuah organisasi perkantoran modern, sering timbul friksi kerja antara kelompok pimpinan senior (Generasi _Baby Boomers_ / Gen X) yang menjunjung tinggi loyalitas jam kerja kantor fisik dan hierarki kaku, dengan kelompok staf muda (Generasi Milenial dan Gen Z) yang menuntut fleksibilitas kerja jarak jauh (_remote work_), keseimbangan hidup-kerja (_work-life balance_), dan komunikasi egaliter. Fenomena sosiologis ini dikaji sebagai...",
        "correct": "Kesenjangan Generasi (_Generation Gap_), yaitu perbedaan nilai, norma, persepsi, dan etos perilaku antargenerasi akibat perbedaan konteks historis, perkembangan teknologi, dan kondisi sosio-kultural saat mereka mengalami masa sosialisasi primer.",
        "distractors": [
            "Bentuk pemberontakan kriminal bersenjata yang dilakukan oleh para pemuda melawan kedaulatan negara.",
            "Kegagalan total sistem pendidikan dasar nasional yang menghasilkan lulusan buta huruf.",
            "Penyimpangan seksual masif yang melanggar aturan tata susila dan hukum adat perdata.",
            "Gejala penurunan kecerdasan otak manusia akibat radiasi menara satelit komunikasi."
        ],
        "formula": {
            "title": "KOHORT GENERASIONAL DALAM PERUBAHAN SOSIAL",
            "latex": "\\text{Konteks Sejarah \\& Teknologi Era Sosialisasi} \\implies \\mathbf{\\text{Habitus Generasional Berbeda}} \\implies \\mathbf{\\text{Generation Gap (Ketegangan Nilai Antargenerasi)}}",
            "legend": "• Menuntut kepemimpinan adaptif dan dialog lintas generasi yang inklusif di tempat kerja"
        },
        "hints": {
            "concept": "Perbedaan pandangan, nilai kerja, dan norma perilaku antargenerasi akibat perbedaan konteks sejarah dan sosialisasi disebut Kesenjangan Generasi (Generation Gap).",
            "execution": "Pilih: Kesenjangan Generasi (Generation Gap)."
        }
    },
    {
        "id": "sos-sim-25",
        "materi": "KONFLIK SOSIAL & PERILAKU KOLEKTIF",
        "topic": "Teori Nilai Tambah Perilaku Kolektif (Value-Added Theory) Neil Smelser",
        "stem": "Sosiolog Neil Smelser merumuskan 'Teori Nilai Tambah' (_Value-Added Theory_) untuk menjelaskan terjadinya perilaku kolektif berupa kerusuhan massa (_mob/riot_). Menurut Smelser, kerusuhan massa hanya dapat meletus jika terpenuhi enam determinan berurutan: Konduktivitas Struktural, Ketegangan Struktural, Berkembangnya Kepercayaan Bersama, Faktor Pemicu, Mobilisasi Partisipan, dan...",
        "correct": "Pengendalian Sosial yang Lemah / Tidak Berfungsi (_Ineffective Operation of Social Control_), di mana aparat penegak hukum lambat mengantisipasi, terpecah, atau kehilangan legitimasi di mata massa.",
        "distractors": [
            "Keberadaan instruksi tertulis langsung dari Mahkamah Agung luar negeri.",
            "Pembagian sembako gratis dari pemerintah yang dibagikan secara serentak di alun-alun.",
            "Penutupan seluruh akses internet dan pemadaman aliran listrik selama satu pekan penuh.",
            "Kedatangan pesawat antariksa asing yang mendarat di pusat kerumunan massa."
        ],
        "formula": {
            "title": "ENAM DETERMINAN NILAI TAMBAH PERILAKU KOLEKTIF SMELSER",
            "latex": "\\begin{cases} \\text{1. Structural Conduciveness:} & \\text{Kondisi struktur sosial memungkinkan terjadinya aksi} \\\\ \\text{2. Structural Strain:} & \\text{Ketegangan/ketidakadilan dirasakan bersama} \\\\ \\text{3. Generalized Belief:} & \\text{Munculnya persepsi bersama mengenai sumber masalah} \\\\ \\text{4. Precipitating Factors:} & \\text{Peristiwa dramatis pemantik kemarahan} \\\\ \\text{5. Mobilization for Action:} & \\text{Penggerakan massa ke lokasi kejadian} \\\\ \\mathbf{\\text{6. Operation of Social Control:}} & \\mathbf{\\text{Kegagalan/Kelumpuhan kontrol sosial aparat penegak hukum}} \\end{cases}",
            "legend": "• Jika kontrol sosial aparat berjalan efektif dan adil, eskalasi kerusuhan dapat dicegah sedini mungkin"
        },
        "hints": {
            "concept": "Enam faktor Smelser penentu kerusuhan massa: 1. Konduktivitas struktural, 2. Ketegangan struktural, 3. Kepercayaan umum, 4. Faktor pemicu, 5. Mobilisasi aksi, 6. Pengendalian sosial (kontrol sosial yang lemah/gagal).",
            "execution": "Pilih: Pengendalian Sosial yang Lemah / Tidak Berfungsi (Ineffective Operation of Social Control)."
        }
    },

    # -------------------------------------------------------------
    # 5 MULTI-SELECT HOTS (sos-sim-26 to sos-sim-30)
    # -------------------------------------------------------------
    {
        "id": "sos-sim-26",
        "materi": "KELOMPOK SOSIAL & STRUKTUR SOSIAL",
        "topic": "Karakteristik Utama Kelompok Sosial Primer (Primary Group)",
        "stem": "Kelompok primer memegang peranan krusial dalam transmisi nilai dan pembentukan karakter manusia. Manakah TIGA karakteristik utama dari kelompok sosial primer menurut Charles Horton Cooley? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Hubungan antaranggota berlangsung secara tatap muka langsung (_face-to-face_) dalam interaksi yang intens dan akrab."},
            {"key": "B", "text": "Jumlah anggota kelompok relatif kecil sehingga setiap orang saling mengenal kepribadian masing-masing secara mendalam."},
            {"key": "C", "text": "Hubungan bersifat langgeng, intim, personal, dan didasari oleh keterikatan kasih sayang emosional yang tulus."},
            {"key": "D", "text": "Hubungan antaranggota diikat oleh kontrak kerja formal tertulis dengan pembagian upah gaji per jam."},
            {"key": "E", "text": "Keanggotaan kelompok berjumlah ratusan ribu orang yang hanya bertemu secara daring di media sosial."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "CIRI UTAMA PRIMARY GROUP COOLEY",
            "latex": "\\text{Primary Group} \\equiv \\begin{cases} \\mathbf{\\text{1. Face-to-Face Interaction}} \\\\ \\mathbf{\\text{2. Small Group Size (Intim \\& Mendalam)}} \\\\ \\mathbf{\\text{3. Emotional \\& Enduring Ties (Batiniah)}} \\\\ \\text{4. Sumber utama pembentukan moral diri} \\end{cases}",
            "legend": "• A, B, C BENAR: Esensi sosiologis kelompok primer (keluarga, sahabat karib)<br>• D dan E adalah karakteristik kelompok sekunder modern"
        },
        "hints": {
            "concept": "Karakteristik kelompok primer Cooley: tatap muka langsung (A), anggota kecil saling kenal akrab (B), hubungan intim langgeng personal afeksi emosional (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "sos-sim-27",
        "materi": "STRATIFIKASI SOSIAL & MOBILITAS SOSIAL",
        "topic": "Faktor Penghambat Terjadinya Mobilitas Sosial Vertikal Naik",
        "stem": "Dalam masyarakat, peluang individu untuk menaikkan kedudukan sosialnya dapat terhambat oleh berbagai faktor struktural dan kultural. Manakah TIGA faktor berikut yang merupakan penghambat nyata bagi mobilitas sosial vertikal naik? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Sistem stratifikasi sosial tertutup (seperti sistem kasta kaku atau feodalisme) yang melarang perpindahan lapisan sosial sejak lahir."},
            {"key": "B", "text": "Diskriminasi rasial, etnis, agama, atau gender yang menutup akses kelompok minoritas terhadap pendidikan tinggi dan pekerjaan prestisius."},
            {"key": "C", "text": "Kemiskinan struktural akut yang membatasi kemampuan keluarga membiayai modal usaha dan pendidikan anak ke jenjang perguruan tinggi."},
            {"key": "D", "text": "Tersedianya beasiswa pendidikan tinggi meritokratis secara terbuka bagi seluruh anak berprestasi dari keluarga miskin."},
            {"key": "E", "text": "Penerapan sistem rekrutmen pegawai berbasis uji kompetensi objektif tanpa koneksi kolusi dan nepotisme."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "FAKTOR PENGHAMBAT MOBILITAS SOSIAL VERTIKAL",
            "latex": "\\text{Hambatan Mobilitas} \\equiv \\mathbf{\\text{Sistem Kasta Tertutup}} + \\mathbf{\\text{Diskriminasi Struktural}} + \\mathbf{\\text{Jebakan Kemiskinan}}",
            "legend": "• A, B, C BENAR: Faktor struktural pengekang mobilitas sosial vertikal naik<br>• D dan E adalah faktor pendorong (fasilitator) mobilitas sosial"
        },
        "hints": {
            "concept": "Faktor penghambat mobilitas sosial vertikal: stratifikasi tertutup (A), diskriminasi ras/etnis/gender (B), kemiskinan struktural (C). Beasiswa dan meritokrasi adalah faktor pendorong.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "sos-sim-28",
        "materi": "KONFLIK SOSIAL & RESOLUSI KONFLIK",
        "topic": "Bentuk Akomodasi Resolusi Konflik Tanpa Kekerasan Fisik",
        "stem": "Dalam ilmu sosiologi, konflik dapat diredam dan diselesaikan melalui berbagai proses akomodasi tanpa pertumpahan darah. Manakah TIGA bentuk akomodasi berikut yang tergolong sebagai mekanisme penyelesaian konflik secara damai dan nir-kekerasan? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Mediasi, di mana pihak ketiga yang netral membantu memfasilitasi dialog dan perundingan antarpihak yang bersengketa."},
            {"key": "B", "text": "Arbitrase, di mana sengketa diselesaikan melalui majelis arbiter yang putusannya bersifat mengikat dan ditaati kedua pihak."},
            {"key": "C", "text": "Kompromi, di mana kedua belah pihak bersedia saling mengurangi tuntutan demi tercapainya mufakat bersama."},
            {"key": "D", "text": "Koersi, di mana pihak yang kuat menggunakan ancaman senjata dan kekerasan fisik untuk memaksa lawan tunduk."},
            {"key": "E", "text": "Pemberontakan kudeta militer berdarah yang menggulingkan pemerintahan sah."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "BENTUK AKOMODASI DAMAI (PEACEFUL ACCOMMODATION)",
            "latex": "\\text{Akomodasi Damai} \\equiv \\mathbf{\\text{Mediasi}} + \\mathbf{\\text{Arbitrase}} + \\mathbf{\\text{Kompromi}} + \\text{Konsiliasi} + \\text{Ajudikasi}",
            "legend": "• A, B, C BENAR: Bentuk akomodasi beradab dan nir-kekerasan<br>• D dan E menggunakan paksaan fisik atau kekerasan bersenjata"
        },
        "hints": {
            "concept": "Bentuk akomodasi damai nir-kekerasan: Mediasi (A), Arbitrase (B), Kompromi (C). Koersi dan kudeta mengandalkan kekerasan/ancaman fisik.",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "sos-sim-29",
        "materi": "MASALAH SOSIAL & KETIMPANGAN SOSIAL",
        "topic": "Dampak Negatif Kesenjangan Sosial Ekonomi Ekstrem",
        "stem": "Ketimpangan sosial ekonomi yang terlampau curam di suatu negara memicu berbagai konsekuensi negatif bagi kohesi kemasyarakatan. Manakah TIGA dampak negatif sosiologis berikut yang dipicu oleh lebarnya kesenjangan sosial ekonomi? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Meningkatnya kecemburuan sosial dan kebencian kelas antara kaum miskin tertindas terhadap kelompok elit kaya."},
            {"key": "B", "text": "Meningkatnya angka tindak kriminalitas konvensional seperti pencurian, perampokan, dan penipuan akibat desakan ekonomi bertahan hidup."},
            {"key": "C", "text": "Melemahnya modal sosial (_social trust_), erosi solidaritas warga, dan meningkatnya kerentanan terhadap disintegrasi bangsa."},
            {"key": "D", "text": "Terwujudnya stabilitas keamanan nasional yang abadi tanpa perlu pengamanan aparat kepolisian."},
            {"key": "E", "text": "Penghapusan seluruh utang luar negeri negara oleh lembaga moneter dunia secara cuma-cuma."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "PATOLOGI SOSIAL AKIBAT KETIMPANGAN EKSTREM",
            "latex": "\\text{Gini Ratio Tinggi} \\implies \\begin{cases} \\mathbf{\\text{Kecemburuan Sosial \\& Polarisasi Kelas}} \\\\ \\mathbf{\\text{Peningkatan Kriminalitas Konvensional}} \\\\ \\mathbf{\\text{Erosi Social Capital \\& Disintegrasi}} \\end{cases}",
            "legend": "• A, B, C BENAR: Dampak destruktif kesenjangan sosial terhadap ketahanan nasional"
        },
        "hints": {
            "concept": "Dampak negatif kesenjangan ekonomi ekstrem: kecemburuan sosial (A), naiknya kriminalitas akibat desakan hidup (B), melemahnya modal sosial dan disintegrasi (C).",
            "execution": "Pilih A, B, dan C."
        }
    },
    {
        "id": "sos-sim-30",
        "materi": "METODOLOGI PENELITIAN SOSIAL",
        "topic": "Prinsip Dasar Etika Penelitian Sosial Lapangan",
        "stem": "Dalam melaksanakan penelitian sosial yang melibatkan subjek manusia, peneliti terikat oleh kaidah etika ilmiah internasional. Manakah TIGA prinsip etika penelitian sosial berikut yang WAJIB ditaati oleh seorang peneliti? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Memperoleh persetujuan sukarela setelah memberikan penjelasan lengkap (_Informed Consent_) dari responden sebelum pengumpulan data."},
            {"key": "B", "text": "Menjamin kerahasiaan identitas pribadi responden (_Anonymity and Confidentiality_) dengan menyamarkan nama asli dan data sensitif."},
            {"key": "C", "text": "Prinsip tidak menimbulkan bahaya atau kerugian fisik, mental, maupun sosial bagi subjek yang diteliti (_Do No Harm_)."},
            {"key": "D", "text": "Memanipulasi atau merekayasa kutipan wawancara narasumber agar sesuai dengan hipotesis pribadi peneliti."},
            {"key": "E", "text": "Mempublikasikan nomor kartu identitas dan alamat rumah pribadi informan secara terbuka di media massa tanpa izin."}
        ],
        "correctAnswer": ["A", "B", "C"],
        "formula": {
            "title": "TRIAS ETIKA RISET SOSIAL (THE BELMONT REPORT STANDARDS)",
            "latex": "\\text{Etika Penelitian} \\equiv \\mathbf{\\text{Informed Consent}} + \\mathbf{\\text{Anonymity / Kerahasiaan}} + \\mathbf{\\text{Prinsip Do No Harm}}",
            "legend": "• A, B, C BENAR: Landasan moral mutlak peneliti sosial<br>• D dan E adalah pelanggaran berat etika akademik (_academic misconduct_)"
        },
        "hints": {
            "concept": "Tiga pilar etika penelitian sosial: Informed Consent (A), Anonymity/Confidentiality kerahasiaan identitas (B), Do No Harm melindungi subjek dari kerugian (C).",
            "execution": "Pilih A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH HOTS (sos-sim-31 to sos-sim-35)
    # -------------------------------------------------------------
    {
        "id": "sos-sim-31",
        "type": "matrix",
        "materi": "KONSEP DASAR & HAKIKAT SOSIOLOGI",
        "topic": "Hakikat, Ciri, dan Objek Kajian Sosiologi",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai hakikat, ciri keilmuan, dan objek kajian sosiologi!",
        "statements": [
            {
                "text": "Sosiologi merupakan ilmu sosial murni (pure science) dan bukan ilmu pengetahuan terapan semata.",
                "correct": True
            },
            {
                "text": "Sosiologi bersifat kumulatif, artinya teori-teori sosiologi yang ada saat ini dibangun dan disempurnakan berdasarkan teori-teori yang telah dikemukakan sebelumnya.",
                "correct": True
            },
            {
                "text": "Tugas utama sosiolog adalah menentukan vonis moral apakah suatu tradisi budaya di masyarakat itu berdosa atau mulia.",
                "correct": False
            },
            {
                "text": "Paradigma Fakta Sosial Émile Durkheim memandang hukum, norma, dan pranata sosial sebagai realitas objektif eksternal yang memaksa tindakan individu.",
                "correct": True
            }
        ],
        "formula": {
            "title": "PRINSIP HAKIKAT ILMU SOSIOLOGI",
            "latex": "\\text{Ciri Sosiologi: Empiris, Teoretis, Kumulatif, Non-Etis}, \\quad \\text{Fakta Sosial: Eksternal, Koersif, General}",
            "legend": "• Pernyataan 1 BENAR: Sosiologi berfokus pada pencarian hukum umum masyarakat (pure science)<br>• Pernyataan 2 BENAR: Definisi ciri kumulatif keilmuan sosiologi<br>• Pernyataan 3 SALAH: Sosiologi bersifat non-etis, dilarang menjatuhkan vonis moral baik/buruk atau dosa/mulia<br>• Pernyataan 4 BENAR: Inti ontologi fakta sosial Durkheim"
        },
        "hints": {
            "concept": "Sosiologi = pure science, kumulatif, dan non-etis (tidak menilai dosa/mulia). Fakta sosial Durkheim = eksternal dan memaksa (koersif).",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Benar."
        }
    },
    {
        "id": "sos-sim-32",
        "type": "matrix",
        "materi": "SOSIALISASI & DINAMIKA KEPRIBADIAN",
        "topic": "Tahap Sosialisasi, Pembentukan Diri, dan Agen Sosialisasi",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai proses sosialisasi dan pembentukan kepribadian!",
        "statements": [
            {
                "text": "Menurut George Herbert Mead, pada tahap Game Stage seorang anak telah mampu memahami perannya sendiri dan peran lawan mainnya dalam satu sistem aturan terstruktur.",
                "correct": True
            },
            {
                "text": "Charles Horton Cooley menyatakan bahwa kepribadian seseorang berkembang secara biologis dari dalam genetik tanpa dipengaruhi oleh persepsi penilaian orang lain.",
                "correct": False
            },
            {
                "text": "Keluarga berperan sebagai agen sosialisasi primer karena menjadi lingkungan pertama yang menanamkan fondasi nilai moral dan afeksi dasar pada anak.",
                "correct": True
            },
            {
                "text": "Sosialisasi antisipatoris (anticipatory socialization) adalah proses di mana seseorang mempelajari norma dan nilai kelompok acuan sebelum ia resmi bergabung ke dalam kelompok tersebut.",
                "correct": True
            }
        ],
        "formula": {
            "title": "TEORI PERKEMBANGAN DIRI DAN SOSIALISASI",
            "latex": "\\text{Mead: Game Stage (Aturan Terstruktur)}, \\quad \\text{Cooley: Looking-Glass Self (Pengaruh Orang Lain)}, \\quad \\text{Anticipatory Socialization}",
            "legend": "• Pernyataan 1 BENAR: Definisi baku game stage Mead (seperti sepak bola)<br>• Pernyataan 2 SALAH: Teori Looking-Glass Self Cooley justru membuktikan diri dibentuk melalui cermin penilaian orang lain, bukan murni genetik<br>• Pernyataan 3 BENAR: Fungsi mutlak keluarga sebagai agen primer<br>• Pernyataan 4 BENAR: Definisi sosialisasi antisipatoris Merton"
        },
        "hints": {
            "concept": "Game stage = paham aturan tim. Cooley looking-glass self membuktikan diri dibentuk oleh cermin sosial orang lain (bukan genetik murni). Keluarga adalah agen primer. Sosialisasi antisipatoris = adaptasi norma sebelum bergabung resmi.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Benar."
        }
    },
    {
        "id": "sos-sim-33",
        "type": "matrix",
        "materi": "STRATIFIKASI SOSIAL & DIFERENSIASI SOSIAL",
        "topic": "Stratifikasi, Diferensiasi, dan Mobilitas Sosial",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai struktur pelapisan dan pembedaan sosial!",
        "statements": [
            {
                "text": "Diferensiasi sosial membagi masyarakat secara vertikal menjadi kelas-kelas sosial berjenjang yang memiliki hak dan kekuasaan berbeda.",
                "correct": False
            },
            {
                "text": "Dalam sistem kasta tradisional tertutup, mobilitas sosial vertikal naik antar-kasta mustahil dilakukan karena status sosial didasarkan pada kelahiran (ascribed status).",
                "correct": True
            },
            {
                "text": "Seorang guru SMA yang dipindahtugaskan mengajar di SMA lain dengan pangkat dan gaji pokok yang sama mengalami mobilitas sosial horizontal.",
                "correct": True
            },
            {
                "text": "Konsolidasi sosial memperkuat interseksi dengan cara menyilangkan keanggotaan suku dan agama sehingga menghilangkan potensi konflik horizontal.",
                "correct": False
            }
        ],
        "formula": {
            "title": "STRUKTUR SOSIAL DAN MOBILITAS",
            "latex": "\\text{Diferensiasi: Horizontal}, \\quad \\text{Stratifikasi: Vertikal}, \\quad \\text{Konsolidasi } \\ne \\text{ Interseksi}",
            "legend": "• Pernyataan 1 SALAH: Diferensiasi membagi secara horizontal/sejajar, yang membagi vertikal adalah stratifikasi sosial<br>• Pernyataan 2 BENAR: Ciri kasta tertutup berbasis ascribed status kelahiran<br>• Pernyataan 3 BENAR: Mutasi sederajat tanpa perubahan strata adalah mobilitas horizontal<br>• Pernyataan 4 SALAH: Konsolidasi justru menumpangkan identitas secara paralel yang mempertegas polarisasi, bukan persilangan interseksi"
        },
        "hints": {
            "concept": "Diferensiasi = horizontal (bukan vertikal). Kasta tertutup = ascribed status (tak bisa naik kasta). Mutasi sederajat = mobilitas horizontal. Konsolidasi = mempertegas polarisasi kelompok (kebalikan dari interseksi).",
            "execution": "Pernyataan 1: Salah; Pernyataan 2: Benar; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "sos-sim-34",
        "type": "matrix",
        "materi": "PERUBAHAN SOSIAL & TEORI GLOBALISASI",
        "topic": "Teori Perubahan Sosial, Modernisasi, dan Ketergantungan",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai perubahan sosial dan teori modernitas!",
        "statements": [
            {
                "text": "Teori Siklus memandang bahwa setiap peradaban manusia pasti akan mengalami fase kelahiran, kejayaan, keruntuhan, dan kembali ke awal secara berulang.",
                "correct": True
            },
            {
                "text": "William F. Ogburn menyatakan bahwa cultural lag terjadi karena kebudayaan non-material (nilai moral dan norma hukum) berubah jauh lebih cepat mendahului kebudayaan material (teknologi fisik).",
                "correct": False
            },
            {
                "text": "Teori Ketergantungan (Dependency Theory) menyatakan bahwa keterbelakangan negara Dunia Ketiga disebabkan oleh penghisapan surplus oleh negara maju di pusat kapitalisme global.",
                "correct": True
            },
            {
                "text": "Glokalisasi adalah proses peleburan total budaya lokal hingga lenyap digantikan oleh standarisasi produk budaya Barat secara mutlak.",
                "correct": False
            }
        ],
        "formula": {
            "title": "TEORI PERUBAHAN SOSIAL DAN GLOBALISASI",
            "latex": "\\text{Siklus: Spengler/Toynbee}, \\quad \\text{Cultural Lag: Material Lebih Cepat dari Non-Material}, \\quad \\text{Dependensia: Frank}, \\quad \\text{Glokalisasi: Global + Lokal}",
            "legend": "• Pernyataan 1 BENAR: Karakteristik teori siklus peradaban<br>• Pernyataan 2 SALAH: Ogburn menyatakan kebudayaan MATERIAL berubah lebih CEPAT, sedangkan non-material tertinggal lambat<br>• Pernyataan 3 BENAR: Tesis utama Andre Gunder Frank dalam teori dependensia<br>• Pernyataan 4 SALAH: Glokalisasi justru memadukan budaya global dengan konteks lokal, bukan pemusnahan budaya lokal"
        },
        "hints": {
            "concept": "Teori siklus = peradaban lahir, jaya, runtuh berulang. Cultural lag = teknologi material berubah LEBIH CEPAT mendahului norma non-material. Dependensia = eksploitasi metropolis atas satelit. Glokalisasi = perpaduan produk global dengan konteks lokal.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Salah; Pernyataan 3: Benar; Pernyataan 4: Salah."
        }
    },
    {
        "id": "sos-sim-35",
        "type": "matrix",
        "materi": "METODOLOGI PENELITIAN SOSIAL",
        "topic": "Pendekatan, Instrumen, dan Etika Penelitian Sosial",
        "stem": "Tentukan kebenaran dari masing-masing pernyataan berikut mengenai metodologi penelitian sosial!",
        "statements": [
            {
                "text": "Penelitian kualitatif mengedepankan pemahaman mendalam (Verstehen) atas makna tindakan sosial dari sudut pandang subjektif para informan.",
                "correct": True
            },
            {
                "text": "Teknik Snowball Sampling sangat efektif digunakan untuk meneliti populasi yang tertutup, tersembunyi, atau kelompok marginal yang sulit dijangkau.",
                "correct": True
            },
            {
                "text": "Uji reliabilitas dilakukan untuk memastikan bahwa alat ukur kuesioner benar-benar mengukur variabel konsep teoritis yang hendak diukur.",
                "correct": False
            },
            {
                "text": "Prinsip Informed Consent mewajibkan peneliti untuk memaksa responden menjawab seluruh pertanyaan rahasia meskipun responden merasa trauma dan ketakutan.",
                "correct": False
            }
        ],
        "formula": {
            "title": "METODOLOGI DAN ETIKA RISET SOSIAL",
            "latex": "\\text{Kualitatif: Verstehen (Makna)}, \\quad \\text{Snowball: Populasi Tersembunyi}, \\quad \\text{Validitas: Mengukur yang Benar}, \\quad \\text{Reliabilitas: Konsistensi Hasil}",
            "legend": "• Pernyataan 1 BENAR: Hakikat riset kualitatif Weberian<br>• Pernyataan 2 BENAR: Keunggulan teknik sampling bola salju untuk populasi sensitif/tersembunyi<br>• Pernyataan 3 SALAH: Mengukur apa yang hendak diukur adalah VALIDITAS; Reliabilitas adalah konsistensi/keandalan hasil ukur berulang<br>• Pernyataan 4 SALAH: Informed consent justru menjamin keikutsertaan sukarela dan hak mundur kapan saja tanpa paksaan"
        },
        "hints": {
            "concept": "Kualitatif = Verstehen/makna tindakan. Snowball sampling = untuk populasi tersembunyi. Mengukur apa yang hendak diukur adalah VALIDITAS (bukan reliabilitas). Informed consent melarang pemaksaan dan menjamin hak sukarela.",
            "execution": "Pernyataan 1: Benar; Pernyataan 2: Benar; Pernyataan 3: Salah; Pernyataan 4: Salah."
        }
    }
]
