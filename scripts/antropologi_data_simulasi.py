# -*- coding: utf-8 -*-
"""
antropologi_data_simulasi.py
-----------------------------
35 Authentic Simulasi CBT HOTS Questions for TKA 2026 Antropologi (SMA/MA Soshum).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
Composition:
- 25 MCQ items (ant-sim-01 .. ant-sim-25)
- 5 Multi-select items (ant-sim-26 .. ant-sim-30)
- 5 Matrix Benar-Salah items (ant-sim-31 .. ant-sim-35)
"""

ANTROPOLOGI_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 MCQ ITEMS (ant-sim-01 .. ant-sim-25)
    # -------------------------------------------------------------
    {
        "id": "ant-sim-01",
        "materi": "ANTROPOLOGI EKONOMI & KEKERABATAN",
        "topic": "Institusi Potlatch pada Suku Kwakiutl menurut Franz Boas",
        "stem": "Dalam kajian etnografi Franz Boas pada masyarakat adat Kwakiutl di pesisir barat laut Pasifik Amerika Utara, tradisi potlatch dilakukan oleh para kepala suku dengan menghancurkan selimut tembaga berharga dan membagikan berton-ton makanan kepada tamu dari klan lain. Ditinjau dari fungsi antropologi ekonomi dan prestise sosial, upacara potlatch bertujuan untuk...",
        "correct": "Mengonversi akumulasi kekayaan materi menjadi prestise simbolik tertinggi dan mempertegas posisi status sosial kepemimpinan melalui mekanisme redistribusi bersaing yang mengikat kewajiban timbal balik klan lawan.",
        "distractors": [
            "Membuang seluruh sisa barang dagangan impor yang kedaluwarsa demi menghindari pengenaan pajak perdagangan.",
            "Menyerahkan seluruh kepemilikan tanah ulayat klan kepada pedagang kulit bulu asal perserikatan bangsa Eropa.",
            "Meminta bantuan militer kepada suku tetangga untuk bersama-sama menyerang armada kapal perang angkatan laut.",
            "Menghukum anggota klan yang terbukti melakukan pelanggaran hukum adat berupa pencurian ternak kuda liar."
        ],
        "formula": {
            "title": "MEKANISME POTLATCH KWAKIUTL (FRANZ BOAS)",
            "latex": "\\text{Akumulasi Materi} \\xrightarrow{\\mathbf{\\text{Penghancuran/Redistribusi}}} \\mathbf{\\text{Prestise Simbolik (Status)}} + \\begin{cases} \\text{Kewajiban Balas Tamu} \\\\ \\text{Keseimbangan Ekologis Regional} \\\\ \\text{Pengukuhan Hierarki Klan} \\end{cases}",
            "legend": "• Menunjukkan ekonomi moral dan pertarungan status simbolik non-kapitalistik"
        },
        "hints": {
            "concept": "Potlatch pada suku Kwakiutl adalah mekanisme redistribusi bersaing untuk mengonversi kekayaan materi menjadi prestise simbolik dan status sosial.",
            "execution": "Pilih opsi konversi kekayaan materi menjadi prestise simbolik dan redistribusi bersaing yang mengikat kewajiban timbal balik."
        }
    },
    {
        "id": "ant-sim-02",
        "materi": "ETNOGRAFI INDONESIA: SISTEM RELIGI",
        "topic": "Upacara Pemakaman Rambu Solo' di Tana Toraja",
        "stem": "Masyarakat adat Toraja di Sulawesi Selatan menggelar upacara kematian Rambu Solo' dengan mengorbankan puluhan kerbau belang (Tedong Bonga) dan babi, serta menyimpan jenazah bangsawan di liang tebing batu pahat Londa atau Kete Kesu. Makna kosmologis pengorbanan Tedong Bonga dalam mengantarkan arwah leluhur menurut keyakinan Aluk Todolo adalah...",
        "correct": "Sebagai kendaraan suci arwah orang yang meninggal (To Madingin) agar mampu menempuh perjalanan gaib dengan selamat menuju alam keabadian peristirahatan leluhur (Puya) sesuai derajat kebangsawanan ampu tana.",
        "distractors": [
            "Sebagai jaminan uang ganti rugi pembebasan lahan perkebunan cengkeh milik keluarga duka yang telah digusur.",
            "Sebagai simbol penyerahan kekuasaan politik distrik kepada aparat perwakilan kantor keresidenan kolonial.",
            "Sebagai sarana menyuap para pemuka agama luar agar bersedia mendoakan keselamatan warga desa dari wabah kolera.",
            "Sebagai bentuk pemusnahan hewan ternak yang tertular penyakit kuku dan mulut agar tidak menular ke desa tetangga."
        ],
        "formula": {
            "title": "KOSMOLOGI RAMBU SOLO' ALUK TODOLO",
            "latex": "\\text{Kematian (To Makuang)} \\xrightarrow{\\mathbf{\\text{Rambu Solo' (Tedong Bonga)}}} \\mathbf{\\text{Arwah Menuju Puya (Surga)}} \\implies \\text{Transformasi Status Menjadi Leluhur Pelindung (Tomatua)}" ,
            "legend": "• Kerbau belang melambangkan kendaraan roh ke alam baka sekaligus penanda stratifikasi bangsawan"
        },
        "hints": {
            "concept": "Dalam Aluk Todolo Rambu Solo', kerbau belang Tedong Bonga dikorbankan sebagai kendaraan arwah menuju alam peristirahatan leluhur (Puya).",
            "execution": "Pilih: Sebagai kendaraan suci arwah menuju alam peristirahatan leluhur (Puya) sesuai derajat kebangsawanan."
        }
    },
    {
        "id": "ant-sim-03",
        "materi": "ANTROPOLOGI KESEHATAN (ETNOMEDISIN)",
        "topic": "Etiologi Penyakit Naturalistik: Konsep Masuk Angin & Kerokan Jawa",
        "stem": "Dalam kajian antropologi medis (etnomedisin), sistem medis tradisional dibedakan menjadi etiologi personalistik dan naturalistik oleh George M. Foster. Konsep penyakit 'masuk angin' pada masyarakat Jawa yang disembuhkan melalui terapi 'kerokan' menggunakan koin minyak kelapa diklasifikasikan ke dalam etiologi naturalistik karena...",
        "correct": "Penyakit diyakini timbul akibat terganggunya keseimbangan unsur internal tubuh (humoral) oleh anasir dingin dari angin luar, di mana kerokan berfungsi membuka pori-pori kulit untuk mengeluarkan hawa angin berlebih.",
        "distractors": [
            "Penyakit dianggap sebagai akibat kutukan teluh dan guna-guna yang dikirim oleh dukun santet musuh bebuyutan keluarga.",
            "Penyakit disebabkan oleh gigitan serangga parasit mikroskopis beracun yang hanya dapat dibunuh dengan radiasi sinar gamma.",
            "Penyakit muncul karena arwah nenek moyang marah akibat makam keramatnya tidak diberi sesajen kepala kerbau putih.",
            "Penyakit timbul karena pelanggaran pantangan adat memancing ikan di muara sungai larangan saat bulan purnama."
        ],
        "formula": {
            "title": "DIKOTOMI ETIOLOGI MEDIS (GEORGE M. FOSTER)",
            "latex": "\\text{Sistem Medis} \\implies \\begin{cases} \\mathbf{\\text{Naturalistik:}} & \\mathbf{\\text{Ketidakseimbangan unsur tubuh/alam (angin, panas-dingin, humoral)}} \\\\ \\text{Personalistik:} & \\text{Intervensi agen aktif gaib (roh leluhur, dewa, tukang sihir/dukun)} \\end{cases}",
            "legend": "• Masuk angin dan kerokan adalah contoh murni sistem patologi humoral/naturalistik lokal"
        },
        "hints": {
            "concept": "Etiologi naturalistik melihat penyakit sebagai akibat ketidakseimbangan unsur fisik/alamiah tubuh (humoral panas-dingin, kelebihan angin), bukan akibat guna-guna roh.",
            "execution": "Pilih penjelasan bahwa masuk angin adalah ketidakseimbangan humoral oleh anasir dingin/angin dan kerokan memulihkan keseimbangan."
        }
    },
    {
        "id": "ant-sim-04",
        "materi": "SISTEM KEKERABATAN NUSANTARA",
        "topic": "Komparasi Sistem Kekerabatan Unilateral vs Bilateral di Indonesia",
        "stem": "Keanekaragaman sistem kekerabatan di Nusantara tercermin dalam pola penarikan garis keturunan. Masyarakat Batak menarik garis keturunan melalui pihak ayah (patrilineal/marga), Minangkabau melalui pihak ibu (matrilineal/suku), sedangkan suku Jawa menarik garis keturunan bilateral (parental). Implikasi antropologis dari sistem bilateral pada masyarakat Jawa adalah...",
        "correct": "Seorang anak memperhitungkan hubungan kekerabatan secara seimbang dan setara dari pihak keluarga ayah maupun ibu, tanpa adanya klan unilateral tertutup sehingga ruang lingkup kerabat meluas ke dua sisi sanak saudara.",
        "distractors": [
            "Seorang anak laki-laki sulung secara mutlak menguasai seluruh harta pusaka tinggi tanpa hak bagi anak perempuan kandung.",
            "Garis keturunan dan hak waris marga hanya diakui sah jika anak tersebut dilahirkan di rumah panggung kediaman paman mertua.",
            "Seorang suami diwajibkan meninggalkan desa kelahirannya dan tinggal menetap di istana rumah gadang milik saudara ibu mertua.",
            "Seluruh anak keturunan otomatis menyandang gelar kebangsawanan datuk dari pihak saudara laki-laki kandung ibu kandungnya."
        ],
        "formula": {
            "title": "KLASIFIKASI GARIS KETURUNAN NUSANTARA",
            "latex": "\\text{Sistem Kekerabatan} = \\begin{cases} \\text{Patrilineal (Batak):} & \\text{Garis Ayah (Marga, Anak Laki-laki)} \\\\ \\text{Matrilineal (Minang):} & \\text{Garis Ibu (Suku, Rumah Gadang, Mamak)} \\\\ \\mathbf{\\text{Bilateral/Parental (Jawa):}} & \\mathbf{\\text{Garis Seimbang Ayah \\& Ibu (Kedua Pihak Setara)}} \\end{cases}",
            "legend": "• Menunjukkan keragaman struktur organisasi sosial kekerabatan masyarakat adat Indonesia"
        },
        "hints": {
            "concept": "Sistem bilateral (parental) menghitung garis keturunan secara seimbang dari kedua sisi orang tua (ayah dan ibu secara setara).",
            "execution": "Pilih opsi hubungan kekerabatan seimbang dan setara dari pihak ayah maupun ibu tanpa klan unilateral tertutup."
        }
    },
    {
        "id": "ant-sim-05",
        "materi": "ETNOLINGUISTIK & KEARIFAN LOKAL",
        "topic": "Fenomena Punahnya Kosakata Agraris Lokal Jawa & Pranata Mangsa",
        "stem": "Kajian antropologi linguistik (etnolinguistik) menemukan bahwa modernisasi pertanian dan mekanisasi traktor telah menyebabkan hilangnya puluhan istilah lokal agraris Jawa seperti 'wiwit' (ritual awal panen), 'ani-ani' (pisau ketam padi), serta perhitungan musim 'pranata mangsa'. Dari kacamata antropologi budaya, punahnya khazanah leksikon lokal agraris tersebut menandakan...",
        "correct": "Pelemahan sistem pengetahuan tradisional (indigenous knowledge) dan terputusnya relasi sakral-ekologis antara petani dengan siklus ritus daur tanam padi akibat tergeser oleh rasionalitas teknologi mekanis monokultur.",
        "distractors": [
            "Peningkatan kualitas gizi dan keanekaragaman hayati varietas padi unggul hasil rekayasa genetik laboratorium universitas.",
            "Keberhasilan program industrialisasi nasional dalam menghapus seluruh bahasa daerah demi pemberlakuan bahasa seragam.",
            "Kemenangan kelas borjuasi pedesaan dalam memonopoli penjualan pupuk subsidi kimiawi buatan pabrik transnasional.",
            "Penurunan tingkat melek huruf dan penurunan minat bersekolah anak-anak pemuda pedesaan di sektor perguruan tinggi."
        ],
        "formula": {
            "title": "HIPOTESIS SAPIR-WHORF & LEKSIKON AGRARIS",
            "latex": "\\text{Bahasa} \\xleftrightarrow{\\text{Refleksi}} \\text{Sistem Kognitif/Kultur} \\implies \\begin{cases} \\text{Leksikon Hilang} \\\\ \\text{Mekanisasi Modern} \\end{cases} \\implies \\mathbf{\\text{Erosi Indigenous Knowledge Agraris}}",
            "legend": "• Bahasa merefleksikan cara pandang kebudayaan terhadap relasi manusia dan alam sekitar"
        },
        "hints": {
            "concept": "Kosakata lokal agraris adalah bagian dari indigenous knowledge. Hilangnya kosakata mencerminkan erosi pengetahuan ekologis lokal dan keterputusan relasi kultural dengan alam.",
            "execution": "Pilih: Pelemahan sistem pengetahuan tradisional dan terputusnya relasi sakral-ekologis petani dengan ritus daur tanam."
        }
    },
    {
        "id": "ant-sim-06",
        "materi": "DIFUSI KEBUDAYAAN & PRASEJARAH",
        "topic": "Pengaruh Tradisi Perunggu Dongson terhadap Seni Logam Nekara Nusantara",
        "stem": "Penemuan nekara perunggu tipe Pejeng di Bali dan moko di Kepulauan Alor membuktikan adanya hubungan difusi kebudayaan Zaman Logam antara kebudayaan Dongson (Vietnam Utara) dengan masyarakat kepulauan Nusantara. Karakteristik adaptasi kultural lokal pada nekara Pejeng yang membedakannya dari nekara Dongson daratan Asia Tenggara adalah...",
        "correct": "Bentuk badannya yang ramping menyerupai dandang terbalik dengan pola hias geometris stilasi kedok muka (topeng) bermata belo yang mencerminkan ekspresi magis-religius megalitik khas lokal Nusantara.",
        "distractors": [
            "Penggunaan tulisan hieroglif paku bertuliskan nama-nama firaun penguasa lembah Sungai Nil dari kerajaan Mesir Kuno.",
            "Bahan dasar pembuatannya yang menggunakan campuran lelehan emas murni dan berlian intan dari pulau Madagaskar.",
            "Adanya relief gambar perahu kora-kora yang dilengkapi persenjataan senapan mesin otomatis buatan pabrik Eropa.",
            "Bentuk persegi empat beroda gerobak yang ditarik oleh sepasang sapi perah asal daratan padang rumput Argentina."
        ],
        "formula": {
            "title": "DIFUSI KEBUDAYAAN DONGSON KE NUSANTARA",
            "latex": "\\text{Kebudayaan Dongson (Vietnam)} \\xrightarrow{\\mathbf{\\text{Difusi Maritim Logam}}} \\text{Nusantara} \\xrightarrow{\\mathbf{\\text{Local Genius}}} \\begin{cases} \\mathbf{\\text{Nekara Tipe Pejeng (Bali)}} \\\\ \\mathbf{\\text{Moko (Alor, NTT)}} \\end{cases}",
            "legend": "• Menunjukkan kemampuan 'local genius' nenek moyang merekayasa seni tuang logam perunggu"
        },
        "hints": {
            "concept": "Nekara tipe Pejeng khas lokal Nusantara memiliki bentuk ramping seperti dandang terbalik dengan hiasan kedok muka (topeng) mata belo khas megalitik lokal.",
            "execution": "Pilih bentuk ramping menyerupai dandang dengan stilasi kedok muka (topeng) bermata belo khas ekspresi lokal."
        }
    },
    {
        "id": "ant-sim-07",
        "materi": "ANTROPOLOGI RAGAWI (PALEOANTROPOLOGI)",
        "topic": "Kedudukan Taksonomi Fosil Homo erectus soloensis (Ngandong)",
        "stem": "Fosil manusia purba yang ditemukan di endapan teras Bengawan Solo di Desa Ngandong, Blora, oleh von Koenigswald dan Oppenoorth diklasifikasikan sebagai *Homo erectus soloensis*. Secara anatomis ragawi, fosil ini dianggap mewakili bentuk peralihan evolutif (*transitional form*) menuju *Homo sapiens* karena memiliki ciri kraniologis...",
        "correct": "Volume kapasitas tempurung otak mencapai 1.000 hingga 1.300 cc dengan tengkorak lebih tebal, dahi lebih miring, serta tonjolan alis mata (torus supraorbitalis) yang masih sangat kekar dibanding manusia modern.",
        "distractors": [
            "Kapasitas otak hanya 400 cc dengan rahang sangat maju mirip primata simpanse tanpa kemampuan berjalan tegak lurus.",
            "Gigi taring berukuran raksasa sepanjang sepuluh sentimeter yang menyerupai gigi karnivora harimau purba bertaring pedang.",
            "Tulang leher yang menyatu dengan tulang dada sehingga tidak dapat menolehkan kepala ke arah kanan maupun kiri.",
            "Volume otak mencapai 2.500 cc dengan rahang sama sekali tidak memiliki gigi taring maupun gigi geraham pencerna rumput."
        ],
        "formula": {
            "title": "EVOLUSI KAPASITAS OTAK HOMINID",
            "latex": "\\text{Australopithecus } (\\approx 450\\text{ cc}) \\to \\text{H. erectus Trinil } (\\approx 900\\text{ cc}) \\xrightarrow{\\mathbf{\\text{H. soloensis}}} \\mathbf{1.000-1.300\\text{ cc}} \\to \\text{H. sapiens } (\\approx 1.400\\text{ cc})",
            "legend": "• Homo soloensis merepresentasikan fase erectus lanjut (progresif) di Jawa sebelum kehadiran sapiens"
        },
        "hints": {
            "concept": "Homo erectus soloensis memiliki kapasitas otak 1.000-1.300 cc, dahi miring, tengkorak tebal, dan torus supraorbitalis kekar (fase peralihan).",
            "execution": "Pilih kapasitas otak 1.000-1.300 cc dengan dahi miring dan torus supraorbitalis kekar."
        }
    },
    {
        "id": "ant-sim-08",
        "materi": "KEARIFAN LOKAL & ADAPTASI EKOLOGI",
        "topic": "Sistem Pertanian Nyabuk Gunung / Sengkedan di Pegunungan Jawa",
        "stem": "Di kawasan dataran tinggi lereng Gunung Sindoro dan Dieng, petani tradisional mempraktikkan teknik 'nyabuk gunung' (membuat terasering bertingkat melingkari lereng punggung bukit seperti sabuk pinggang). Dilihat dari perspektif antropologi ekologi, kearifan lokal sistem 'nyabuk gunung' berfungsi adaptif sebagai...",
        "correct": "Strategi rekayasa bentang alam untuk memecah laju aliran air permukaan (run-off), mereduksi risiko longsor tebing curam, dan menjaga humus kesuburan tanah vulkanik agar dapat diolah secara lestari.",
        "distractors": [
            "Simbol pembatas wilayah kerajaan kuno yang tidak boleh dilewati oleh para pedagang kuda keliling antardesa.",
            "Media ritual pemujaan roh dewa angin agar tidak menerbangkan jerami padi kering ke permukiman rumah panggung warga.",
            "Bentuk protes sosial buruh tani kepada tuan tanah kolonial dengan cara mencangkul bukit hingga tidak dapat ditanami.",
            "Sistem pertahanan parit jebakan anti-pencuri yang sengaja dibuat untuk menggagalkan pelarian prajurit musuh bebuyutan."
        ],
        "formula": {
            "title": "ANTROPOLOGI EKOLOGI: KEARIFAN NYABUK GUNUNG",
            "latex": "\\text{Lereng Curam} + \\text{Hujan Lebat} \\xrightarrow{\\mathbf{\\text{Kearifan Nyabuk Gunung}}} \\begin{cases} \\mathbf{\\text{Teras Melingkar Lereng (Sabuk)}} \\\\ \\mathbf{\\text{Reduksi Run-off \\& Erosi Humus}} \\\\ \\mathbf{\\text{Pertanian Berkelanjutan (Lestari)}} \\end{cases}",
            "legend": "• Menggambarkan adaptasi cerdas masyarakat tradisional terhadap tantangan ekosistem perbukitan"
        },
        "hints": {
            "concept": "Nyabuk gunung adalah adaptasi ekologis berupa pembuatan terasering melingkari lereng bukit untuk mencegah erosi, menahan run-off, dan menjaga kesuburan tanah.",
            "execution": "Pilih: Strategi rekayasa bentang alam memecah aliran permukaan, mereduksi risiko longsor, dan menjaga kesuburan tanah."
        }
    },
    {
        "id": "ant-sim-09",
        "materi": "RITUS DAUR HIDUP (RITES OF PASSAGE)",
        "topic": "Simbolisme Ritual Tedak Siten pada Etnis Jawa",
        "stem": "Upacara adat Tedak Siten (turun tanah) digelar saat seorang bayi menginjak usia 7 lapan (sekitar 245 hari / 7-8 bulan). Dalam upacara ini, sang anak dituntun menginjak bubur jadah 7 warna, menaiki tangga tebu arjuna, dan dimasukkan ke dalam kurungan ayam yang berisi aneka benda (buku, uang, cermin). Makna antropologis dari tahapan memasukkan anak ke dalam kurungan ayam tersebut adalah...",
        "correct": "Simbolisasi perkenalan anak pada realitas dunia sosial bermasyarakat dan proyeksi simbolik penuntun minat bakat masa depan anak saat dewasa dalam mengarungi kehidupan yang penuh batasan norma.",
        "distractors": [
            "Hukuman pengasingan bagi anak balita yang menangis saat upacara ruwatan desa sedang berlangsung di pendapa balai kota.",
            "Ritual mengorbankan ayam jago aduan agar arwah penunggu sungai tidak menculik balita saat mandi di sumber mata air.",
            "Cara memeriksa apakah bayi tersebut memiliki penyakit rabun mata ayam dengan cara mengujinya di kegelapan malam.",
            "Simbol penyerahan anak kepada pemuka agama untuk dijadikan murid pertapa di puncak bukit selama tujuh tahun penuh."
        ],
        "formula": {
            "title": "SIMBOLISME RITUAL TEDAK SITEN",
            "latex": "\\text{Tedak Siten} \\implies \\begin{cases} \\text{Jadah 7 Warna:} & \\text{Ketabahan melalui lika-liku kehidupan} \\\\ \\text{Tangga Tebu Arjuna:} & \\text{Tekad meraih cita-cita luhur (Anteping Kalbu)} \\\\ \\mathbf{\\text{Kurungan Ayam:}} & \\mathbf{\\text{Dunia Sosial, Norma Etika, \\& Minat Bakat Masa Depan}} \\end{cases}",
            "legend": "• Menandai peralihan status ontologis anak dari dunia kandungan/pangkuan menuju dunia bumi nyata"
        },
        "hints": {
            "concept": "Kurungan ayam pada Tedak Siten menyimbolkan batas dunia sosial di mana anak diperkenalkan pada masyarakat dan benda-benda di dalamnya memprediksi minat bakat masa depannya.",
            "execution": "Pilih opsi perkenalan anak pada realitas dunia sosial bermasyarakat dan proyeksi minat bakat masa depan anak."
        }
    },
    {
        "id": "ant-sim-10",
        "materi": "FOLKLOR & SENI PERTUNJUKAN",
        "topic": "Atraksi Kesenian Debus Banten & Mistisisme Tarekat",
        "stem": "Kesenian bela diri dan atraksi Debus di Banten menampilkan kemahiran para pemain menusuk bagian tubuh dengan paku besar (gedebus), mengiris lidah dengan golok, atau menyiram tubuh dengan air keras tanpa mengalami luka. Berdasarkan kajian antropologi religi dan sejarah kebudayaan, akar kultural atraksi kekebalan tubuh Debus berasal dari...",
        "correct": "Praktik mistisisme dan zikir tarekat Rifa'iyah (dan Qadiriyah) yang berakulturasi dengan seni bela diri kanuragan lokal untuk membangkitkan keyakinan spiritual dan ketahanan perlawanan rakyat masa Kesultanan Banten.",
        "distractors": [
            "Praktek perdukunan voodoo dari pedagang budak kepulauan Karibia yang terdampar di pesisir Selat Sunda.",
            "Metode bedah plastik modern yang diajarkan oleh tim dokter bedah militer garnisun kolonial Hindia Belanda.",
            "Sirkus akrobatik komersial yang diperkenalkan oleh rombongan seniman jalanan asal dataran Tiongkok selatan.",
            "Ritual pengorbanan budak sahaya tawanan perang sebelum armada kapal perang Banten berlayar menuju Batavia."
        ],
        "formula": {
            "title": "GENEALOGI KULTURAL SENI DEBUS BANTEN",
            "latex": "\\text{Zikir/Mistisisme Tarekat Rifa'iyah} + \\text{Ilmu Bela Diri Kanuragan Sunda} \\xrightarrow{\\mathbf{\\text{Akulturasi Kesultanan}}} \\mathbf{\\text{Seni Debus Banten}}",
            "legend": "• Menggabungkan dimensi religiositas Islam sufistik dengan ketahanan fisik-magis lokal"
        },
        "hints": {
            "concept": "Debus Banten berakar dari mistisisme zikir tarekat sufi (khususnya Rifa'iyah) yang berpadu dengan kanuragan bela diri lokal untuk membela kesultanan.",
            "execution": "Pilih: Praktik mistisisme dan zikir tarekat Rifa'iyah yang berakulturasi dengan seni bela diri kanuragan lokal."
        }
    },
    {
        "id": "ant-sim-11",
        "materi": "STRATIFIKASI SOSIAL & PERKAWINAN ADAT",
        "topic": "Dinamika Perkawinan Endogami Kasta (Asu Pundhung) di Bali",
        "stem": "Dalam sistem pelapisan sosial tradisional Bali masa lalu (Wangsa), terdapat aturan larangan perkawinan kasta ketat seperti 'Asu Pundhung' (perempuan golongan Triwangsa menikah dengan laki-laki kasta Sudra/Jaba) yang dahulu berakibat pada sanksi pengusiran dari desa (maselong). Dalam perkembangan antropologi hukum adat modern di Bali, aturan tersebut kini telah dihapus karena...",
        "correct": "Bertentangan dengan prinsip hak asasi manusia, kesetaraan gender, dan telah dibatalkan melalui keputusan resmi Majelis Utama Desa Pakraman/Desa Adat demi keadilan sosial dan keharmonisan keluarga.",
        "distractors": [
            "Seluruh keturunan kasta ksatria telah meninggalkan pulau Bali dan pindah kewarganegaraan ke negara bagian Australia.",
            "Pemerintah kolonial Belanda telah melarang seluruh warga masyarakat Bali menggelar upacara pernikahan secara agama Hindu.",
            "Terjadi kepunahan total seluruh warga kasta Sudra akibat bencana alam meletusnya Gunung Agung pada zaman kuno.",
            "Seluruh pura keluarga pemerajan di Bali diwajibkan untuk dihancurkan dan diganti dengan balai pertemuan politik sekuler."
        ],
        "formula": {
            "title": "TRANSFORMASI HUKUM ADAT PERKAWINAN BALI",
            "latex": "\\text{Asu Pundhung / Alangkahi Karang} \\xrightarrow{\\mathbf{\\text{Keputusan Majelis Desa Adat}}} \\mathbf{\\text{Penghapusan Sanksi Kasta}} \\implies \\text{Kesetaraan HAM \\& Keadilan Sosial}",
            "legend": "• Menunjukkan sifat hukum adat yang dinamis menyesuaikan tuntutan nilai kemanusiaan universal"
        },
        "hints": {
            "concept": "Sanksi larangan perkawinan antarkasta seperti Asu Pundhung telah dicabut secara resmi oleh majelis adat karena bertentangan dengan HAM dan kesetaraan.",
            "execution": "Pilih opsi pertentangan dengan HAM dan kesetaraan gender serta telah dibatalkan resmi oleh Majelis Desa Adat."
        }
    },
    {
        "id": "ant-sim-12",
        "materi": "ETNOBOTANI & SISTEM PENGETAHUAN",
        "topic": "Pengetahuan Empiris Jamu Tradisional Jawa & Verifikasi Saintifik",
        "stem": "Etnobotani mempelajari bagaimana kelompok etnis memanfaatkan tumbuhan obat di lingkungan sekitarnya. Nenek moyang masyarakat Jawa meracik jamu 'beras kencur' untuk menghangatkan badan dan 'kunyit asam' untuk meredakan nyeri menstruasi. Berdasarkan antropologi kognitif, keabsahan sistem pengetahuan obat tradisional tersebut bersumber dari...",
        "correct": "Akumulasi pengalaman empiris bertahap selama ratusan tahun melalui proses uji coba kultural (trial and error) yang diwariskan lisan dan terdokumentasi dalam serat/naskah kuno seperti Serat Centhini.",
        "distractors": [
            "Hasil penelitian klinis laboratorium farmasi modern yang didanai oleh lembaga kesehatan dunia WHO pada abad ke-16.",
            "Petunjuk manual mesin pabrik kimia sintetis asal Eropa yang diterjemahkan secara rahasia oleh mata-mata kerajaan.",
            "Wahyu gaib yang melarang warga mengonsumsi ramuan tumbuhan kecuali bila diperintahkan oleh gubernur jenderal VOC.",
            "Hukuman pidana kerja paksa yang mewajibkan seluruh perempuan menumbuk akar tanaman racun setiap pagi hari."
        ],
        "formula": {
            "title": "TRANSMISI KNOWLEDGE ETNOBOTANI JAMU",
            "latex": "\\text{Trial \\& Error Empiris} \\xrightarrow{\\text{Generasi ke Generasi}} \\mathbf{\\text{Indigenous Botanical Wisdom}} \\xrightarrow{\\text{Kodifikasi}} \\begin{cases} \\text{Serat Centhini} \\\\ \\text{Tradisi Racik Jamu} \\\\ \\mathbf{\\text{Etnomedisin Jawa}} \\end{cases}",
            "legend": "• Sistem pengetahuan lokal memiliki landasan empiris tersendiri sebelum pembuktian laboratorium modern"
        },
        "hints": {
            "concept": "Sistem obat tradisional etnis bersumber dari akumulasi empiris uji coba bertahap (trial & error) ratusan tahun yang terdokumentasi dalam naskah kuno seperti Serat Centhini.",
            "execution": "Pilih: Akumulasi pengalaman empiris bertahap melalui trial and error kultural yang diwariskan dan tercatat dalam serat kuno."
        }
    },
    {
        "id": "ant-sim-13",
        "materi": "KOMODIFIKASI BUDAYA & PARIWISATA",
        "topic": "Transformasi Tari Kecak Uluwatu: dari Ritual Sakral ke Komoditas Turis",
        "stem": "Tari Kecak di Bali awalnya berakar dari bagian paduan suara ritus sakral kesurupan Sanghyang Dedari untuk menolak bala di desa. Pada tahun 1930-an, seniman Wayan Limbak bersama pelukis Walter Spies merekonstruksinya menjadi drama tari epos Ramayana berdurasi tetap yang kini dipentaskan rutin bagi wisatawan di tebing Uluwatu. Fenomena ini dalam antropologi pariwisata dikenal sebagai...",
        "correct": "Komodifikasi budaya dan desakralisasi seni (proses pengemasan unsur kebudayaan sakral menjadi produk hiburan estetis bernilai ekonomi untuk konsumsi industri pariwisata).",
        "distractors": [
            "Etnosida terencana untuk melenyapkan seluruh peninggalan agama Hindu dari tanah kepulauan Bali.",
            "Xenofobia massal yang dilakukan oleh para penari pura terhadap turis asing yang berkunjung ke pantai.",
            "Asimilasi biologis antara pendatang asal mancanegara dengan penduduk desa nelayan tradisional lokal.",
            "Pemberontakan serikat pekerja panggung teater rakyat menuntut pembagian laba tiket pertunjukan."
        ],
        "formula": {
            "title": "DINAMIKA KOMODIFIKASI BUDAYA (TOURIST ART)",
            "latex": "\\text{Sanghyang Dedari (Ritual Sakral)} \\xrightarrow{\\mathbf{\\text{Walter Spies \\& Limbak (1930)}}} \\mathbf{\\text{Tari Kecak Ramayana}} \\xrightarrow{\\text{Pasar Turisme}} \\mathbf{\\text{Komodifikasi Budaya}}",
            "legend": "• Mengubah fungsi ritual sakral penolak bala menjadi seni pertunjukan komersial dengan durasi terukur"
        },
        "hints": {
            "concept": "Komodifikasi budaya adalah transformasi seni sakral lokal menjadi produk komoditas tontonan estetis bernilai ekonomi bagi konsumsi turis.",
            "execution": "Pilih istilah komodifikasi budaya dan desakralisasi seni untuk konsumsi industri pariwisata."
        }
    },
    {
        "id": "ant-sim-14",
        "materi": "KEARIFAN LOKAL BAHARI & HUKUM ADAT",
        "topic": "Praktik Sasi Lompa di Maluku Tengah & Konservasi Sumber Daya Ikan",
        "stem": "Masyarakat Negeri Haruku di Maluku Tengah memiliki tradisi 'Sasi Lompa', yaitu pemberlakuan larangan adat sakral untuk menangkap ikan lompa (*Thryssa baelama*) di perairan muara Sungai Learisa Kayeli selama periode waktu tertentu. Ketika masa sasi dibuka oleh Raja dan Kewang (polisi adat), warga memanen ikan bersama-sama. Manfaat antropologis-ekologis dari pranata Sasi Lompa tersebut adalah...",
        "correct": "Mencegah penangkapan ikan berlebih (overfishing) dan memberi kesempatan bagi ikan lompa untuk bereproduksi serta membesar, sehingga menjamin kelestarian ekosistem perairan dan ketahanan pangan desa secara berkelanjutan.",
        "distractors": [
            "Memusnahkan seluruh habitat ikan air tawar agar muara sungai dapat dialihfungsikan menjadi dermaga kapal kontainer batu bara.",
            "Memberikan hak monopoli tangkapan ikan kepada kapal pukat harimau milik konglomerat asing asal negara tetangga.",
            "Mewajibkan warga desa menjual seluruh hasil tangkapan laut kepada tuan tanah feodal dengan harga paling murah.",
            "Menghukum warga masyarakat yang tidak berpartisipasi dalam upacara penyerahan upeti kepada istana kerajaan seberang lautan."
        ],
        "formula": {
            "title": "MEKANISME PRANATA SASI LOMPA (MALUKU)",
            "latex": "\\text{Kewang (Polisi Adat)} \\implies \\mathbf{\\text{Tutup Sasi (Moratorium Adat)}} \\xrightarrow{\\text{Regenerasi Ikan}} \\mathbf{\\text{Buka Sasi (Panen Kolektif)}} \\implies \\text{Konservasi Lestari}",
            "legend": "• Bukti efektivitas hukum adat dalam memelihara keseimbangan daya dukung ekosistem bahari"
        },
        "hints": {
            "concept": "Sasi Lompa adalah instrumen kearifan lokal konservasi laut Maluku untuk mencegah overfishing, memberi waktu ikan bertelur/membesar, dan menjaga keberlanjutan pangan.",
            "execution": "Pilih: Mencegah penangkapan berlebih (overfishing), memberi waktu reproduksi ikan, dan menjamin kelestarian pangan."
        }
    },
    {
        "id": "ant-sim-15",
        "materi": "ARSITEKTUR VERNAKULAR & EKOLOGI",
        "topic": "Adaptasi Arsitektur Rumah Honai Suku Dani di Lembah Baliem",
        "stem": "Rumah adat Honai milik suku Dani di Lembah Baliem Papua dibangun dengan bentuk bundar melingkar, berdinding kayu tebal tanpa jendela, beratap kerucut jerami/rumput ilalang tebal, dan memiliki perapian api unggun di bagian tengah lantai bawah. Struktur arsitektur vernakular ini mencerminkan adaptasi ekologis masyarakat terhadap...",
        "correct": "Suhu udara dingin ekstrem pegunungan tinggi Lembah Baliem pada malam hari, di mana ketiadaan jendela dan atap jerami tebal memerangkap panas perapian serta menahan hembusan angin kencang.",
        "distractors": [
            "Ancaman gelombang pasang tsunami samudra yang sering menyapu pesisir pantai pulau-pulau karang terluar.",
            "Serangan kawanan nyamuk malaria rawa pasang surut dataran rendah hutan mangrove pesisir selatan.",
            "Kebutuhan menampung ratusan ekor unta tunggangan yang melintasi jalur perdagangan gurun pasir tandus.",
            "Kewajiban adat menyembunyikan emas batangan murni dari inspeksi petugas perpajakan kolonial Hindia Belanda."
        ],
        "formula": {
            "title": "ADAPTASI ARSITEKTUR HONAI PAPUA",
            "latex": "\\begin{pmatrix} \\text{Bentuk Melingkar Tanpa Jendela} \\\\ \\text{Atap Ilalang Kerucut Tebal} \\\\ \\text{Perapian Tengah (Tungku)} \\end{pmatrix} \\xrightarrow{\\mathbf{\\text{Respons Ekologis}}} \\mathbf{\\text{Memerangkap Panas Terhadap Iklim Dingin Pegunungan}}",
            "legend": "• Arsitektur vernakular adalah manifestasi teknologi adaptif lokal terhadap kondisi iklim mikro setempat"
        },
        "hints": {
            "concept": "Rumah Honai dirancang melingkar, rapat tanpa jendela, beratap jerami, dan berapian di tengah untuk menahan udara dingin di pegunungan tinggi Lembah Baliem.",
            "execution": "Pilih opsi adaptasi terhadap suhu udara dingin ekstrem pegunungan Lembah Baliem pada malam hari."
        }
    },
    {
        "id": "ant-sim-16",
        "materi": "HUBUNGAN ANTARKELOMPOK & PRASANGKA",
        "topic": "Etnosentrisme vs Xenofobia dalam Masyarakat Perkotaan Multikultural",
        "stem": "Dalam masyarakat perkotaan yang majemuk, sering muncul sikap etnosentrisme dan xenofobia. Perbedaan konseptual mendasar antara etnosentrisme dan xenofobia dalam kajian antropologi sosial adalah...",
        "correct": "Etnosentrisme memandang dan menilai kebudayaan kelompok lain secara sepihak menggunakan standar nilai budayanya sendiri sebagai tolok ukur keunggulan, sedangkan xenofobia merupakan ketakutan atau kebencian tak rasional terhadap orang asing atau unsur luar.",
        "distractors": [
            "Etnosentrisme merupakan rasa cinta berlebihan kepada bangsa lain, sedangkan xenofobia adalah kebencian mendalam kepada keluarga sendiri.",
            "Etnosentrisme hanya terjadi pada suku terasing di pedalaman hutan, sedangkan xenofobia hanya dialami oleh para pejabat pemerintah pusat.",
            "Etnosentrisme adalah keinginan menyatukan seluruh bahasa daerah menjadi satu, sedangkan xenofobia adalah penolakan terhadap pemilu.",
            "Etnosentrisme didasarkan pada perhitungan ilmu ekonomi pasar modal, sedangkan xenofobia didasarkan pada ajaran tasawuf sufi."
        ],
        "formula": {
            "title": "KOMPARASI ETNOSENTRISME VS XENOFOBIA",
            "latex": "\\begin{cases} \\mathbf{\\text{Etnosentrisme:}} & \\text{Menilai budaya lain dengan standar budaya in-group (In-group superiority)} \\\\ \\mathbf{\\text{Xenofobia:}} & \\text{Ketakutan tak berdasar, permusuhan, \\& kebencian terhadap orang asing/unsur luar} \\end{cases}",
            "legend": "• Menunjukkan dua bentuk prasangka sosial yang menghambat integrasi harmonis multikultural"
        },
        "hints": {
            "concept": "Etnosentrisme = mengukur budaya luar dengan tolok ukur budaya sendiri (merasa budayanya superior). Xenofobia = ketakutan atau kebencian tak berdasar terhadap orang asing.",
            "execution": "Pilih definisi etnosentrisme mengukur budaya lain dengan standar sendiri vs xenofobia ketakutan/kebencian tak rasional terhadap orang luar."
        }
    },
    {
        "id": "ant-sim-17",
        "materi": "SISTEM PERKAWINAN ADAT NUSANTARA",
        "topic": "Institusi Mahar/Belis pada Masyarakat Adat Manggarai (Flores, NTT)",
        "stem": "Pada masyarakat adat Manggarai di Pulau Flores (NTT), perkawinan adat selalu melibatkan penyerahan 'belis' (mahar perkawinan) berupa sejumlah hewan ternak (kuda, kerbau) dan kain tenun Songke dari pihak keluarga laki-laki kepada keluarga perempuan. Makna antropologis dari institusi belis tersebut bukan sebagai transaksi jual beli manusia, melainkan...",
        "correct": "Sebagai simbol penghormatan tertinggi terhadap martabat perempuan, pengikat tali persaudaraan antara klan pemberi istri (Woe/Anak Rona) dan klan penerima istri (Anak Wina), serta pemenuhan legitimasi hukum adat bagi status anak keturunan.",
        "distractors": [
            "Sebagai pembayaran upeti budak tawanan perang kepada para perwira tentara ekspedisi asing dari seberang pulau.",
            "Sebagai sarana melunasi utang pajak tanah perkebunan kopi kepada administratur perusahaan multinasional barat.",
            "Sebagai cara menyogok kepala desa agar bersedia menerbitkan kartu keluarga palsu bagi imigran gelap dari perbatasan.",
            "Sebagai syarat membebaskan seorang mempelai pria dari ancaman hukuman penjara akibat perkelahian massal antardesa."
        ],
        "formula": {
            "title": "FUNGSI SOSIAL BELIS MANGGARAI (FLORES)",
            "latex": "\\text{Penyerahan Belis} \\xrightarrow{\\mathbf{\\text{Bukan Jual-Beli}}} \\begin{cases} \\mathbf{\\text{Penghormatan Martabat Perempuan}} \\\\ \\mathbf{\\text{Pengikat Aliansi Klan (Anak Rona } \\leftrightarrow \\text{ Anak Wina)}} \\\\ \\mathbf{\\text{Legitimasi Status Ontologis Keturunan}} \\end{cases}",
            "legend": "• Belis adalah pranata aliansi sosial dan rekognisi martabat perempuan dalam struktur kekerabatan timur"
        },
        "hints": {
            "concept": "Belis bukan harga jual beli wanita, melainkan simbol penghormatan perempuan, perajut aliansi kekerabatan klan (Anak Rona dan Anak Wina), serta legitimasi anak.",
            "execution": "Pilih: Simbol penghormatan martabat perempuan, perajut aliansi kekerabatan klan, dan legitimasi hukum adat anak."
        }
    },
    {
        "id": "ant-sim-18",
        "materi": "TEORI EVOLUSI RELIGI",
        "topic": "Teori Asal Mula Religi (Animisme) menurut Edward Burnett Tylor",
        "stem": "Dalam buku monumentalnya *Primitive Culture* (1871), antropolog Edward B. Tylor mengemukakan teori mengenai asal-mula religi pada masyarakat manusia paling awal (animisme). Menurut Tylor, konsep mengenai adanya roh atau jiwa (*soul*) pertama kali lahir di benak manusia purba karena ketidakmampuan mereka menjelaskan dua peristiwa alamiah sehari-hari, yaitu...",
        "correct": "Pengalaman bermimpi (di mana tubuh fisik tertidur namun jiwa tampak berkelana) dan peristiwa kematian (di mana napas dan daya hidup hilang dari raga fisik seseorang).",
        "distractors": [
            "Pergantian gerhana matahari total dan gempa bumi vulkanik dahsyat yang menenggelamkan pulau tempat tinggal mereka.",
            "Penemuan cara menggosok serpihan batu rijang untuk memercikkan bunga api unggun pada saat musim dingin berkepanjangan.",
            "Kelahiran bayi kembar siam yang dianggap sebagai tanda kemurkaan dewa petir penguasa puncak gunung berapi keramat.",
            "Pertarungan antara kawanan gajah purba mammoth melawan sekelompok harimau pemangsa di padang rumput sabana liar."
        ],
        "formula": {
            "title": "TEORI ANIMISME EDWARD B. TYLOR (1871)",
            "latex": "\\begin{pmatrix} \\mathbf{\\text{Pengalaman Mimpi (Raga Diam, Jiwa Melanglang)}} \\\\ \\mathbf{\\text{Peristiwa Kematian (Hilangnya Nafas Hidup)}} \\end{pmatrix} \\implies \\mathbf{\\text{Konsepsi Jiwa/Roh (Anima)}} \\to \\text{Animisme}",
            "legend": "• Dari kesadaran adanya jiwa ganda berkembang menjadi keyakinan pada roh leluhur, dewa, hingga monoteisme"
        },
        "hints": {
            "concept": "Tylor menyatakan animisme lahir dari upaya manusia awal memahami mimpi (jiwa berkelana saat raga tidur) dan kematian (nafas hidup meninggalkan raga).",
            "execution": "Pilih: Pengalaman bermimpi dan peristiwa kematian."
        }
    },
    {
        "id": "ant-sim-19",
        "materi": "ETNOGRAFI INDONESIA: MASYARAKAT ADAT",
        "topic": "Diferensiasi Kultural & Aturan Adat Urang Kanekes (Baduy Luar vs Baduy Dalam)",
        "stem": "Masyarakat adat Urang Kanekes (Baduy) di Pegunungan Kendeng, Banten, terbagi atas kelompok Baduy Dalam (Tangtu) dan Baduy Luar (Panamping). Ciri kultural pembeda yang paling mencolok antara kedua kelompok tersebut dalam ketaatan menjaga amanat adat (*pikukuh*) adalah...",
        "correct": "Baduy Dalam mengenakan pakaian putih alami tanpa jahitan berikat kepala putih dan menolak sama sekali intervensi teknologi modern serta transportasi mesin, sedangkan Baduy Luar mengenakan pakaian warna hitam/biru tua dan memiliki toleransi terbatas terhadap interaksi dunia luar.",
        "distractors": [
            "Baduy Dalam bermata pencaharian sebagai pedagang valuta asing di pelabuhan, sedangkan Baduy Luar bertani rempah cengkeh di bukit.",
            "Baduy Dalam memeluk agama resmi dari peradaban Timur Tengah, sedangkan Baduy Luar menganut ajaran animisme suku pedalaman.",
            "Baduy Dalam diwajibkan menempuh pendidikan sarjana di luar negeri, sedangkan Baduy Luar dilarang membaca buku pelajaran sekolah.",
            "Baduy Dalam memilih kepala desa melalui sistem pemungutan suara elektronik, sedangkan Baduy Luar dipimpin oleh gubernur jenderal."
        ],
        "formula": {
            "title": "DIFERENSIASI BADUY DALAM VS BADUY LUAR",
            "latex": "\\text{Urang Kanekes} \\implies \\begin{cases} \\mathbf{\\text{Baduy Dalam (Tangtu):}} & \\text{Baju putih alami, tanpa mesin, isolasi ketat pikukuh} \\\\ \\mathbf{\\text{Baduy Luar (Panamping):}} & \\text{Baju hitam/biru tua, perantara budaya, toleransi terbatas} \\end{cases}",
            "legend": "• Menunjukkan mekanisme pertahanan kebudayaan adat menghadapi tekanan penetrasi modernitas"
        },
        "hints": {
            "concept": "Baduy Dalam memakai busana putih/ikat kepala putih, mutlak patuh pikukuh tanpa teknologi/kendaraan; Baduy Luar busana hitam/biru tua, bertindak sebagai penyaring/penyangga dunia luar.",
            "execution": "Pilih: Baduy Dalam berpakaian putih alami menolak teknologi, Baduy Luar berpakaian hitam/biru tua bertoleransi terbatas."
        }
    },
    {
        "id": "ant-sim-20",
        "materi": "ANTROPOLOGI LINGUISTIK & KEPULAUAN",
        "topic": "Pembagian Rumpun Bahasa Austronesia vs Non-Austronesia (Papua)",
        "stem": "Kepulauan Indonesia memiliki keanekaragaman linguistik luar biasa dengan lebih dari 700 bahasa daerah. Secara garis besar, para ahli memetakan bahasa-bahasa di Indonesia ke dalam dua rumpun utama, yaitu rumpun Austronesia dan kelompok Non-Austronesia (Papua). Batas biogeografis dan linguistik penting yang memisahkan persebaran kedua kelompok bahasa ini adalah...",
        "correct": "Wilayah Pulau Halmahera bagian utara dan pesisir utara Papua hingga pedalaman, di mana bahasa-bahasa Non-Austronesia (Papua) terkonsentrasi di pedalaman Pulau Papua dan pulau sekitarnya sedangkan Austronesia mendominasi kawasan barat dan selatan Nusantara.",
        "distractors": [
            "Selat Sunda yang memisahkan seluruh bahasa di Pulau Sumatra dengan bahasa di Pulau Jawa tanpa ada persamaan kosakata.",
            "Selat Bali yang membatasi penggunaan bahasa beraksara Pallawa dengan bahasa rumpun Indo-Eropa di kawasan Pasifik timur.",
            "Sungai Kapuas di Kalimantan Barat yang memisahkan penutur bahasa Sino-Tibet dengan bahasa Afroasiatika Afrika utara.",
            "Garis Khatulistiwa yang membelah wilayah Indonesia menjadi zona pengguna huruf hieroglif utara dan huruf paku selatan."
        ],
        "formula": {
            "title": "PETA LINGUISTIK NUSANTARA",
            "latex": "\\text{Bahasa di RI} \\implies \\begin{cases} \\mathbf{\\text{Austronesia:}} & \\text{Sumatra, Jawa, Bali, NTB, NTT, Sul, Maluku Slt, Pasifik} \\\\ \\mathbf{\\text{Non-Austronesia (Papua):}} & \\text{Papua Pedalaman, Halmahera Utara, Alor-Pantar, Timor Leste} \\end{cases}",
            "legend": "• Menunjukkan dua gelombang migrasi manusia purba prasejarah ke wilayah kepulauan Nusantara"
        },
        "hints": {
            "concept": "Bahasa Non-Austronesia (Papua) terkonsentrasi di pedalaman Pulau Papua dan pulau sekitarnya (seperti Halmahera Utara, Alor-Pantar), sementara Austronesia mendominasi barat dan selatan Nusantara.",
            "execution": "Pilih opsi persebaran bahasa Non-Austronesia di pedalaman Papua/Halmahera Utara dan Austronesia di barat/selatan Nusantara."
        }
    },
    {
        "id": "ant-sim-21",
        "materi": "ETNOGRAFI INDONESIA: SISTEM RELIGI",
        "topic": "Upacara Yadnya Kasada Masyarakat Adat Suku Tengger",
        "stem": "Setiap malam ke-14 bulan Kasada penanggalan tradisional Tengger, masyarakat adat suku Tengger yang bermukim di kawasan kaldera Gunung Bromo berkumpul menggelar upacara 'Yadnya Kasada'. Puncak ritual ditandai dengan melempar aneka hasil bumi, sayuran, dan ternak ke dalam kawah berasap Gunung Bromo. Asal-usul mitologis dan makna sosial upacara Kasada tersebut berkaitan dengan...",
        "correct": "Peringatan janji pengorbanan anak bungsu (Raden Kusuma) pasangan leluhur Roro Anteng dan Joko Seger kepada dewa Bromo demi keselamatan dan kemakmuran seluruh keturunan warga suku Tengger.",
        "distractors": [
            "Perayaan hari ulang tahun raja Majapahit Hayam Wuruk saat menaklukkan benteng pertahanan kerajaan Blambangan.",
            "Pemberian upeti kepada petugas kehutanan kolonial Belanda agar warga diizinkan menebang pohon pinus di hutan lindung.",
            "Ritual membuang racun belerang yang mencemari saluran irigasi persawahan warga di lereng barat Gunung Semeru.",
            "Upacara pelantikan bupati kepala daerah tingkat dua yang baru terpilih dalam kontestasi pemilihan umum daerah."
        ],
        "formula": {
            "title": "MITOLOGI YADNYA KASADA TENGGER",
            "latex": "\\begin{pmatrix} \\text{Roro An-TENG} \\\\ \\text{Joko Se-GER} \\end{pmatrix} \\xrightarrow{\\text{Nazar Anak Bungsu (Raden Kusuma)}} \\mathbf{\\text{Kawah Gunung Bromo}} \\implies \\mathbf{\\text{Yadnya Kasada (Harmoni Kosmis)}}",
            "legend": "• Mewujudkan bakti leluhur dan permohonan berkah keselamatan serta hasil panen melimpah"
        },
        "hints": {
            "concept": "Yadnya Kasada berakar dari mitos pasangan leluhur Tengger (Roro Anteng dan Joko Seger) yang menepati janji mempersembahkan hasil bumi ke kawah Bromo demi keselamatan warga.",
            "execution": "Pilih: Peringatan janji pengorbanan anak bungsu Raden Kusuma pasangan Roro Anteng dan Joko Seger ke dewa Bromo."
        }
    },
    {
        "id": "ant-sim-22",
        "materi": "ANTROPOLOGI EKONOMI & RESIPROSITAS",
        "topic": "Tiga Tipologi Resiprositas menurut Marshall Sahlins",
        "stem": "Antropolog Marshall Sahlins membagi sistem pertukaran resiprositas ke dalam tiga bentuk: resiprositas umum (_generalized reciprocity_), resiprositas seimbang (_balanced reciprocity_), dan resiprositas negatif (_negative reciprocity_). Praktik di mana seorang pemburu membagikan hasil buruan daging rusa kepada seluruh kerabat di kampung tanpa mencatat nilai utang dan tanpa menuntut imbalan dalam batas waktu tertentu merupakan contoh dari...",
        "correct": "Resiprositas umum (generalized reciprocity), yaitu pertukaran sosial murni tanpa pamrih perhitungan waktu atau nilai nominal pengembalian karena dilandasi ikatan kekerabatan erat dan solidaritas moral komunal.",
        "distractors": [
            "Resiprositas negatif (negative reciprocity), yaitu upaya mendapatkan keuntungan sebesar-besarnya dengan mengorbankan pihak lain.",
            "Resiprositas seimbang (balanced reciprocity), yaitu pertukaran komoditas langsung dengan nilai sepadan dalam jangka waktu pasti.",
            "Sistem pasar bebas oligopoli, yaitu penetapan harga sepihak oleh segelintir pedagang tengkulak kartel perdagangan.",
            "Sistem lelang terbuka perbankan, yaitu penjualan agunan jaminan nasabah gagal bayar kepada penawar harga tertinggi."
        ],
        "formula": {
            "title": "TIPOLOGI RESIPROSITAS MARSHALL SAHLINS",
            "latex": "\\text{Resiprositas} = \\begin{cases} \\mathbf{\\text{Umum (Generalized):}} & \\mathbf{\\text{Beri tanpa pamrih/batas waktu (Keluarga/Klan)}} \\\\ \\text{Seimbang (Balanced):} & \\text{Tukar nilai setara dengan tenggat waktu (Teman/Mitra)} \\\\ \\text{Negatif (Negative):} & \\text{Cari untung sepihak/tuntas tawar-menawar (Orang Luar)} \\end{cases}",
            "legend": "• Semakin dekat jarak sosial antarpelaku, semakin umum dan tanpa pamrih bentuk resiprositasnya"
        },
        "hints": {
            "concept": "Resiprositas umum (generalized) adalah pertukaran tanpa menghitung nilai imbalan atau tenggat waktu pengembalian, umumnya berlangsung antarkeluarga/kerabat dekat.",
            "execution": "Pilih: Resiprositas umum (generalized reciprocity) tanpa perhitungan waktu atau nominal pengembalian berkat ikatan kerabat erat."
        }
    },
    {
        "id": "ant-sim-23",
        "materi": "DINAMIKA KEBUDAYAAN & ASIMILASI",
        "topic": "Asimilasi & Akulturasi Budaya Tionghoa Peranakan di Pesisir Jawa",
        "stem": "Di kawasan pesisir utara Pulau Jawa (Pesisiran), interaksi intensif antara warga keturunan Tionghoa dan masyarakat pribumi selama berabad-abad melahirkan kebudayaan 'Tionghoa Peranakan'. Hasil perpaduan kultural ini tampak nyata dalam kesenian Gambang Kromong, busana Kebaya Encim, serta kuliner Lontong Cap Go Meh. Ciri khas kultural yang menandai kebudayaan Peranakan tersebut adalah...",
        "correct": "Terjadinya akulturasi dan kreolisasi yang harmonis di mana unsur bahasa lokal Melayu/Jawa, busana nusantara, dan estetika Tiongkok melebur membentuk identitas budaya baru tanpa menghilangkan warisan leluhur.",
        "distractors": [
            "Penolakan mutlak warga Tionghoa untuk memakan makanan lokal berbahan dasar santan kelapa dan bumbu rempah-rempah.",
            "Kewajiban seluruh warga pribumi mengganti nama marganya dengan nama marga kaisar Dinasti Ming dari Tiongkok.",
            "Penghapusan seluruh perayaan tahun baru Imlek dan pembongkaran klenteng bersejarah oleh para pemuka masyarakat lokal.",
            "Pemberlakuan undang-undang apartheid pemukiman tertutup yang melarang perkawinan campur antarras di seluruh pulau."
        ],
        "formula": {
            "title": "AKULTURASI BUDAYA PERANAKAN PESISIR",
            "latex": "\\text{Budaya Tionghoa} + \\text{Budaya Lokal Pesisir Jawa} \\xrightarrow{\\mathbf{\\text{Kontak Abad ke Abad}}} \\mathbf{\\text{Kultur Tionghoa Peranakan}} \\implies \\begin{cases} \\text{Kebaya Encim} \\\\ \\text{Gambang Kromong} \\\\ \\text{Lontong Cap Go Meh} \\end{cases}",
            "legend": "• Menunjukkan kelenturan budaya lokal dan perantau menciptakan sintesis identitas budaya hibrid"
        },
        "hints": {
            "concept": "Budaya Tionghoa Peranakan adalah buah akulturasi dan kreolisasi harmonis yang memadukan unsur Tiongkok dan lokal Nusantara membentuk identitas baru.",
            "execution": "Pilih: Terjadinya akulturasi dan kreolisasi yang harmonis melebur membentuk identitas budaya baru."
        }
    },
    {
        "id": "ant-sim-24",
        "materi": "ANTROPOLOGI MARITIM & KEARIFAN LOKAL",
        "topic": "Tabu Bahari & Solidaritas Pelaut Ulung Suku Mandar (Perahu Sandeq)",
        "stem": "Pelaut ulung suku Mandar di Sulawesi Barat terkenal dengan perahu cadik tradisional 'Sandeq' yang mampu melayari perairan luas hingga ke Selat Makassar. Saat berlayar mencari ikan terbang (torani), para pelaut memegang teguh berbagai pantangan (tabu), seperti dilarang berkata kasar, dilarang membuang abu dapur sembarangan, dan wajib menjaga kerukunan antatawa kapal (punggawa dan sawi). Fungsi antropologis pranata tabu bahari tersebut adalah...",
        "correct": "Membangun disiplin psikologis kolektif, menjaga soliditas kekompakan awak kapal saat menghadapi amukan badai samudra, serta menjaga keharmonisan sakral dengan entitas alam gaib penguasa lautan.",
        "distractors": [
            "Membatasi jumlah ikan tangkapan agar harga jual ikan asin di pasar pelelangan melonjak menjadi setinggi mungkin.",
            "Mencegah awak perahu mendengar siaran radio navigasi cuaca yang dipancarkan oleh stasiun meteorologi nasional.",
            "Menghukum para pemuda kampung yang tidak menguasai bahasa asing persemakmuran maritim internasional.",
            "Menjamin bahwa perahu Sandeq hanya boleh dinakhodai oleh warga keturunan bangsawan istana kerajaan Eropa."
        ],
        "formula": {
            "title": "FUNGSI INTEGRATIF TABU BAHARI PELAUT",
            "latex": "\\text{Kondisi Bahari Ekstrem (Badai/Laut Terbuka)} \\xrightarrow{\\mathbf{\\text{Pranata Tabu}}} \\begin{cases} \\mathbf{\\text{Disiplin Kolektif Awak (Sawi)}} \\\\ \\mathbf{\\text{Kohesi Sosial Anti-Konflik}} \\\\ \\mathbf{\\text{Ketenangan Mental Psikologis}} \\end{cases}",
            "legend": "• Tabu bekerja sebagai mekanisme kontrol sosial yang vital bagi keselamatan pelayaran tradisional"
        },
        "hints": {
            "concept": "Tabu bahari bagi pelaut tradisional berfungsi menjaga kekompakan (kohesi), mencegah konflik batin di tengah laut berisiko tinggi, dan menjaga disiplin mental awak.",
            "execution": "Pilih opsi membangun disiplin psikologis kolektif, menjaga soliditas kekompakan awak kapal, dan keharmonisan sakral."
        }
    },
    {
        "id": "ant-sim-25",
        "materi": "PERUBAHAN SOSIAL BUDAYA & GLOBALISASI",
        "topic": "Transformasi Nilai Masyarakat Adat Sasak di Desa Wisata Sade Lombok",
        "stem": "Desa adat Sade di Pulau Lombok, yang dihuni oleh masyarakat suku Sasak tradisional dengan rumah berlantai tanah liat campur kotoran kerbau, kini telah berkembang menjadi destinasi pariwisata internasional. Masuknya arus wisatawan dan komersialisasi kerajinan tenun ikat Sasak membawa dampak ganda (*double-edged sword*) bagi masyarakat adat Sade, yaitu...",
        "correct": "Meningkatkan pendapatan ekonomi warga dan kebanggaan identitas kultural lokal, namun di sisi lain memicu komersialisasi relasi sosial, pergeseran orientasi nilai religiositas, dan ketergantungan ekonomi pada fluktuasi pasar pariwisata.",
        "distractors": [
            "Punahnya seluruh populasi suku Sasak akibat terjangkit wabah penyakit menular yang dibawa oleh kapal pesiar mewah.",
            "Kewajiban seluruh warga desa Sade untuk merobohkan rumah adat bale tani dan membangun gedung pencakar langit kaca.",
            "Terhapusnya seluruh dialek bahasa Sasak dan diwajibkannya bahasa Latin kuno sebagai bahasa percakapan sehari-hari.",
            "Pengalihan kepemilikan seluruh tanah ulayat desa Sade kepada konsorsium maskapai penerbangan multinasional."
        ],
        "formula": {
            "title": "DIALEKTIKA PARIWISATA DESA ADAT",
            "latex": "\\text{Arus Wisata Komersial} \\implies \\begin{cases} \\mathbf{\\text{Dampak Positif:}} & \\text{Diversifikasi pendapatan, revitalisasi tenun ikat} \\\\ \\mathbf{\\text{Dampak Negatif:}} & \\text{Komodifikasi relasi, distorsi nilai sakral, vulnerabilitas ekonomi} \\end{cases}",
            "legend": "• Menunjukkan kerentanan dan ketahanan masyarakat adat dalam merespons penetrasi globalisasi"
        },
        "hints": {
            "concept": "Dampak ganda pariwisata: positif pada peningkatan ekonomi dan kebanggaan budaya; negatif pada komodifikasi relasi sosial dan distorsi nilai sakral.",
            "execution": "Pilih: Meningkatkan pendapatan dan kebanggaan budaya, namun memicu komersialisasi relasi dan pergeseran orientasi nilai."
        }
    },

    # -------------------------------------------------------------
    # 5 MULTI-SELECT ITEMS (ant-sim-26 .. ant-sim-30)
    # -------------------------------------------------------------
    {
        "id": "ant-sim-26",
        "materi": "KONSEP DASAR KEBUDAYAAN",
        "topic": "Tiga Wujud Kebudayaan menurut J.J. Honigmann & Koentjaraningrat",
        "stem": "Dalam menganalisis fenomena kebudayaan suatu masyarakat, antropolog mengklasifikasikan kebudayaan ke dalam tiga wujud yang saling berkaitan. Manakah pernyataan berikut yang TEPAT mengenai ketiga wujud kebudayaan tersebut? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Wujud gagasan bersifat abstrak, berada di dalam alam pikiran manusia, mencakup ide, sistem nilai, norma, dan hukum adat yang berfungsi sebagai pedoman berkehidupan."},
            {"key": "B", "text": "Wujud aktivitas atau sistem sosial berupa serangkaian tindakan berpola manusia yang saling berinteraksi dan berhubungan satu sama lain dalam kehidupan bermasyarakat sehari-hari."},
            {"key": "C", "text": "Wujud artefak atau kebudayaan fisik mencakup segala benda konkret dan hasil karya tangan manusia yang dapat diraba, dilihat, dan didokumentasikan secara visual."},
            {"key": "D", "text": "Wujud kebudayaan secara mutlak diwariskan secara biologis melalui ikatan kromosom sel telur dan sel sperma tanpa memerlukan proses pembelajaran sosial."},
            {"key": "E", "text": "Wujud artefak fisik kebudayaan bersifat kekal abadi dan tidak dapat mengalami perubahan meskipun masyarakat pendukungnya mengalami revolusi teknologi."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "TIGA WUJUD KEBUDAYAAN",
            "latex": "\\begin{aligned} \\text{Wujud 1 (Gagasan): } & \\text{Ide, Nilai, Norma (Abstrak)} \\\\ \\text{Wujud 2 (Aktivitas): } & \\text{Sistem Sosial, Tindakan Berpola (Konkret Interaksi)} \\\\ \\text{Wujud 3 (Artefak): } & \\text{Benda Fisik, Alat, Karya Material (Konkret Raba)} \\end{aligned}",
            "legend": "• Kebudayaan dipelajari melalui enkulturasi, bukan diwariskan secara biologis genetik"
        },
        "hints": {
            "concept": "Tiga wujud kebudayaan: gagasan (abstrak/ide), aktivitas (tindakan sosial berpola), dan artefak (benda fisik konkret). Kebudayaan diwariskan lewat belajar (enkulturasi), bukan genetika.",
            "execution": "Pilih 3 pernyataan pertama (A, B, C). Tolak pernyataan D (pewarisan biologis) dan E (artefak kekal)."
        }
    },
    {
        "id": "ant-sim-27",
        "materi": "METODOLOGI PENELITIAN ETNOGRAFI",
        "topic": "Prinsip-Prinsip Utama Metode Observasi Partisipasi (Participant Observation)",
        "stem": "Metode observasi partisipasi (*participant observation*) yang dipelopori oleh Bronislaw Malinowski merupakan metode khas dalam penelitian etnografi antropologi. Manakah pernyataan berikut yang BENAR terkait penerapan metode observasi partisipasi di lapangan? (Pilihlah TIGA jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Peneliti tinggal menetap di tengah komunitas masyarakat yang diteliti dalam jangka waktu yang relatif lama (imersi budaya mendalam)."},
            {"key": "B", "text": "Peneliti berupaya mempelajari dan menguasai bahasa lokal setempat guna menangkap sudut pandang asli warga pribumi (perspektif emik)."},
            {"key": "C", "text": "Peneliti ikut terlibat secara aktif dalam berbagai aktivitas keseharian warga masyarakat tanpa kehilangan kepekaan analisis kritis."},
            {"key": "D", "text": "Peneliti hanya menyebarkan angket kuesioner tertutup melalui pos tanpa perlu berkunjung langsung menemui warga komunitas lokal."},
            {"key": "E", "text": "Peneliti memaksakan nilai-nilai moral budaya asalnya untuk merombak kebiasaan hidup warga masyarakat yang dianggap terbelakang."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "TRIAS METODE MALINOWSKI (OBSERVASI PARTISIPASI)",
            "latex": "\\text{Observasi Partisipasi} \\implies \\begin{cases} \\mathbf{\\text{1. Imersi Lapangan (Tinggal Bersama Komunitas)}} \\\\ \\mathbf{\\text{2. Penguasaan Bahasa Asli (Perspektif Emik)}} \\\\ \\mathbf{\\text{3. Keterlibatan Aktivitas Nyata Harian}} \\end{cases}",
            "legend": "• Menangkap 'the native's point of view, his relation to life, to realize his vision of his world'"
        },
        "hints": {
            "concept": "Observasi partisipasi: tinggal bersama komunitas dalam waktu lama, belajar bahasa lokal untuk perspektif emik, dan terlibat dalam aktivitas nyata warga.",
            "execution": "Pilih 3 opsi pertama (A, B, C). Tolak D (kuesioner pos) dan E (pemaksaan nilai moral)."
        }
    },
    {
        "id": "ant-sim-28",
        "materi": "SISTEM RELIGI & KOSMOLOGI",
        "topic": "Komponen-Komponen Sistem Religi menurut Koentjaraningrat",
        "stem": "Prof. Dr. Koentjaraningrat merumuskan bahwa sistem religi dalam kebudayaan manusia tersusun atas komponen-komponen pokok yang saling bertautan. Manakah di antara unsur-unsur berikut yang merupakan komponen sistem religi menurut Koentjaraningrat? (Pilihlah EMPAT jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Emosi keagamaan (getaran jiwa yang menyebabkan manusia melakukan tindakan ritual sakral)."},
            {"key": "B", "text": "Sistem keyakinan (doktrin, konsep kosmos, konsepsi dewa, arwah leluhur, dan alam baka)."},
            {"key": "C", "text": "Sistem upacara keagamaan dan sarana ritual (sesaji, mantra, doa, dan tempat peribadatan)."},
            {"key": "D", "text": "Umat keagamaan (kelompok komunitas pemeluk yang menjalankan keyakinan dan upacara tersebut)."},
            {"key": "E", "text": "Sistem pembagian dividen saham modal perbankan syariah pada pasar bursa modal sekunder."}
        ],
        "correctKeys": ["A", "B", "C", "D"],
        "formula": {
            "title": "4 KOMPONEN SISTEM RELIGI (KOENTJARANINGRAT)",
            "latex": "\\text{Sistem Religi} = \\begin{cases} \\mathbf{\\text{1. Emosi Keagamaan}} & \\text{(Pemicu getaran sakral)} \\\\ \\mathbf{\\text{2. Sistem Keyakinan}} & \\text{(Mitologi, kosmologi, teologi)} \\\\ \\mathbf{\\text{3. Sistem Upacara \\& Sarana}} & \\text{(Ritual, sesaji, tempat suci)} \\\\ \\mathbf{\\text{4. Umat Agama}} & \\text{(Komunitas penganut)} \\end{cases}",
            "legend": "• Membentuk kesatuan fungsional yang menyatukan masyarakat dalam ikatan suci transendental"
        },
        "hints": {
            "concept": "Empat komponen religi Koentjaraningrat: emosi keagamaan, sistem keyakinan, sistem upacara dan sarananya, serta umat penganut religi.",
            "execution": "Pilih 4 opsi pertama (A, B, C, D). Tolak E (dividen saham perbankan)."
        }
    },
    {
        "id": "ant-sim-29",
        "materi": "KEARIFAN LOKAL NUSANTARA",
        "topic": "Praktik Kearifan Lokal Konservasi Ekologis di Indonesia",
        "stem": "Kearifan lokal (*indigenous knowledge*) terbukti efektif dalam memelihara keseimbangan daya dukung lingkungan di berbagai penjuru Nusantara. Manakah di antara tradisi adat berikut yang berfungsi sebagai kearifan lokal dalam konservasi sumber daya alam? (Pilihlah EMPAT jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Sistem Subak di Bali yang mengatur tata kelola distribusi air persawahan secara berkeadilan berlandaskan filosofi Tri Hita Karana."},
            {"key": "B", "text": "Pranata Sasi di Maluku yang memberlakukan larangan adat berkala untuk memanen hasil laut dan darat demi regenerasi biologi hayati."},
            {"key": "C", "text": "Hutan Larangan Tana' Ulen pada masyarakat Dayak Kenyah di Kalimantan Timur yang menjaga keutuhan hutan primer dari perambahan."},
            {"key": "D", "text": "Hukum Adat Pikukuh pada suku Baduy di Banten yang melarang penebangan sembarangan dan melarang mengubah kontur alami tanah lereng."},
            {"key": "E", "text": "Penggunaan racun pukat harimau dan bahan peledak potasium sianida untuk memanen ikan terumbu karang di perairan laut dangkal."}
        ],
        "correctKeys": ["A", "B", "C", "D"],
        "formula": {
            "title": "KEARIFAN LOKAL KONSERVASI NUSANTARA",
            "latex": "\\begin{aligned} \\text{Subak (Bali): } & \\text{Distribusi Air, Tri Hita Karana} \\\\ \\text{Sasi (Maluku): } & \\text{Moratorium Penangkapan Ikan} \\\\ \\text{Tana' Ulen (Dayak): } & \\text{Perlindungan Hutan Primer} \\\\ \\text{Pikukuh (Baduy): } & \\text{Larangan Ubah Bentang Lahan} \\end{aligned}",
            "legend": "• Kearifan tradisional merupakan benteng pertahanan ekologis terbaik komunitas adat"
        },
        "hints": {
            "concept": "Contoh kearifan lokal konservasi: Subak Bali, Sasi Maluku, Tana' Ulen Dayak, dan Pikukuh Baduy. Racun potasium adalah perusak lingkungan.",
            "execution": "Pilih 4 opsi kearifan lokal konservasi (A, B, C, D). Tolak opsi E (bom potasium sianida)."
        }
    },
    {
        "id": "ant-sim-30",
        "materi": "FOLKLOR & TRADISI LISAN",
        "topic": "Karakteristik Utama Folklor menurut Jan Harold Brunvand",
        "stem": "Folklor merupakan bagian dari kebudayaan suatu kolektif yang tersebar dan diwariskan secara turun-temurun. Berdasarkan teori Jan Harold Brunvand, manakah ciri-ciri utama folklor yang BENAR? (Pilihlah EMPAT jawaban yang benar!)",
        "options": [
            {"key": "A", "text": "Penyebaran dan pewarisannya dilakukan secara lisan dari mulut ke mulut antargenerasi."},
            {"key": "B", "text": "Bersifat anonim (nama pencipta pertamanya sudah tidak diketahui lagi oleh warga kolektif)."},
            {"key": "C", "text": "Memiliki varian-varian yang berbeda-beda dalam versi penceritaannya (berbentuk rumus atau formulaik)."},
            {"key": "D", "text": "Mempunyai fungsi penting dalam kehidupan bersama, seperti alat pendidikan, pelipur lara, dan kontrol norma sosial."},
            {"key": "E", "text": "Didaftarkan secara resmi hak paten hak ciptanya ke kantor kementerian hukum atas nama pengarang pribadi."}
        ],
        "correctKeys": ["A", "B", "C", "D"],
        "formula": {
            "title": "CIRI-CIRI FOLKLOR (JAN HAROLD BRUNVAND)",
            "latex": "\\text{Folklor} = \\begin{cases} \\mathbf{\\text{1. Transmisi Lisan}} & \\mathbf{\\text{3. Memiliki Varian / Formulaik}} \\\\ \\mathbf{\\text{2. Anonim}} & \\mathbf{\\text{4. Berfungsi Kolektif (Edukasi, Kontrol Sosial)}} \\end{cases}",
            "legend": "• Folklor hidup dalam memori kolektif masyarakat tradisional sebelum era media massa modern"
        },
        "hints": {
            "concept": "Ciri folklor menurut Brunvand: lisan, anonim, memiliki varian/versi yang berbeda, berbentuk formulaik, dan berfungsi kolektif.",
            "execution": "Pilih 4 ciri pertama (A, B, C, D). Tolak E (pendaftaran hak cipta paten individu)."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH ITEMS (ant-sim-31 .. ant-sim-35)
    # -------------------------------------------------------------
    {
        "id": "ant-sim-31",
        "materi": "SISTEM KEKERABATAN NUSANTARA",
        "topic": "Evaluasi Fakta Sistem Kekerabatan & Pola Menetap Pascanikah",
        "stem": "Berikut disajikan pernyataan mengenai sistem kekerabatan dan pola menetap pascanikah pada masyarakat adat di Indonesia. Tentukan apakah masing-masing pernyataan BENAR atau SALAH!",
        "statements": [
            {
                "text": "Pada sistem kekerabatan patrilineal masyarakat Batak, garis keturunan ditarik melalui pihak ayah dan anak laki-laki mewarisi klan marga.",
                "correct": "Benar"
            },
            {
                "text": "Pola menetap pascanikah matrilokal (uxorilokal) adalah pola di mana pasangan pengantin baru menetap di lingkungan kediaman kerabat pihak suami.",
                "correct": "Salah"
            },
            {
                "text": "Masyarakat Minangkabau menganut sistem kekerabatan matrilineal di mana harta pusaka tinggi diwariskan turun-temurun kepada anak perempuan.",
                "correct": "Benar"
            },
            {
                "text": "Sistem kekerabatan bilateral (parental) pada suku Jawa hanya mengakui hak waris dari pihak ayah dan menghapus hubungan darah dengan pihak ibu.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI SISTEM KEKERABATAN ADAT",
            "latex": "\\begin{aligned} \\text{Batak Patrilineal: } & \\text{Benar (Garis Ayah, Marga Laki-laki)} \\\\ \\text{Matrilokal (Uxorilokal): } & \\text{Salah (Tinggal di kerabat Istri, bukan Suami)} \\\\ \\text{Minang Matrilineal: } & \\text{Benar (Garis Ibu, Pusaka Tinggi ke Perempuan)} \\\\ \\text{Jawa Bilateral: } & \\text{Salah (Mengakui setara kedua belah pihak)} \\end{aligned}",
            "legend": "• Menunjukkan ketepatan penguasaan struktur kekerabatan dan pola menetap antropologis"
        },
        "hints": {
            "concept": "1=Benar (Batak patrilineal garis ayah). 2=Salah (Matrilokal tinggal di kerabat ISTRI, patrilokal tinggal di kerabat suami). 3=Benar (Minang matrilineal pusaka tinggi ke perempuan). 4=Salah (Jawa bilateral mengakui setara kedua belah pihak).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "ant-sim-32",
        "materi": "ETNOGRAFI INDONESIA: RELIGI & RITUS",
        "topic": "Evaluasi Fakta Upacara Adat & Religi Tradisional Nusantara",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap pernyataan terkait upacara adat dan tradisi religius pada kelompok etnis di Indonesia!",
        "statements": [
            {
                "text": "Upacara Ngaben di Bali merupakan ritus kremasi jenazah umat Hindu yang bertujuan melepaskan atma dari ikatan keduniawian unsur Panca Maha Bhuta.",
                "correct": "Benar"
            },
            {
                "text": "Tiwah adalah upacara kematian tingkat akhir pada suku Dayak penganut Kaharingan untuk mengantarkan arwah leluhur menuju Lewu Tatau.",
                "correct": "Benar"
            },
            {
                "text": "Tradisi Pasola di Sumba merupakan upacara pemujaan leluhur Marapu yang menampilkan atraksi perang lempar tombak kayu di atas punggung kuda.",
                "correct": "Benar"
            },
            {
                "text": "Upacara Rambu Solo' di Tana Toraja dilaksanakan dengan bersuka cita melepaskan lampion terbang ke angkasa pada saat perayaan tahun baru panen padi.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI UPACARA ADAT NUSANTARA",
            "latex": "\\begin{aligned} \\text{Ngaben (Bali): } & \\text{Benar (Penyucian Atma, Kremasi Panca Maha Bhuta)} \\\\ \\text{Tiwah (Dayak): } & \\text{Benar (Kaharingan, Arwah ke Lewu Tatau)} \\\\ \\text{Pasola (Sumba): } & \\text{Benar (Ritus Marapu, Ketangkasan Kuda)} \\\\ \\text{Rambu Solo' (Toraja): } & \\text{Salah (Rambu Solo' adalah upacara duka kematian, bukan lampion tahun baru)} \\end{aligned}",
            "legend": "• Upacara adat merefleksikan kosmologi sakral dan hubungan manusia dengan alam baka"
        },
        "hints": {
            "concept": "1=Benar (Ngaben penyucian atma). 2=Benar (Tiwah mengantar arwah ke Lewu Tatau). 3=Benar (Pasola tradisi Marapu di Sumba). 4=Salah (Rambu Solo' adalah upacara kematian berduka dengan korban kerbau, bukan lampion).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "ant-sim-33",
        "materi": "TEORI ANTROPOLOGI & PARADIGMA",
        "topic": "Evaluasi Teori Tokoh Utama Antropologi Dunia",
        "stem": "Berikut disajikan pernyataan mengenai tokoh peletak dasar antropologi beserta teori-teori pentingnya. Tentukan apakah masing-masing pernyataan BENAR atau SALAH!",
        "statements": [
            {
                "text": "Franz Boas dikenal sebagai Bapak Antropologi Amerika yang mempelopori aliran Partikularisme Historis dan menolak keras determinisme rasial.",
                "correct": "Benar"
            },
            {
                "text": "Bronislaw Malinowski mengembangkan teori Fungsionalisme Struktural yang menegaskan bahwa seluruh institusi sosial diciptakan untuk memenuhi kebutuhan biologis individu.",
                "correct": "Benar"
            },
            {
                "text": "Clifford Geertz memandang kebudayaan sebagai teks simbolik yang maknanya harus ditafsirkan melalui deskripsi mendalam (thick description).",
                "correct": "Benar"
            },
            {
                "text": "Claude Lévi-Strauss adalah tokoh utama teori Evolusionisme Unilinear yang menyatakan bahwa seluruh kebudayaan berkembang melintasi tahapan liar, biadab, ke beradab.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI PARADIGMA TEORI ANTROPOLOGI",
            "latex": "\\begin{aligned} \\text{Franz Boas: } & \\text{Benar (Partikularisme Historis, Anti-Rasisme)} \\\\ \\text{Malinowski: } & \\text{Benar (Fungsionalisme Kebutuhan Biologis/Psikologis)} \\\\ \\text{Clifford Geertz: } & \\text{Benar (Antropologi Simbolik / Interpretatif, Thick Description)} \\\\ \\text{Lévi-Strauss: } & \\text{Salah (Lévi-Strauss tokoh Strukturalisme; Evolusionisme unilinear: Morgan/Tylor)} \\end{aligned}",
            "legend": "• Pemetaan akurat paradigma antropologi dari fungsionalisme hingga simbolik interpretatif"
        },
        "hints": {
            "concept": "1=Benar (Boas partikularisme historis). 2=Benar (Malinowski fungsionalisme kebutuhan). 3=Benar (Geertz kebudayaan sebagai teks, thick description). 4=Salah (Lévi-Strauss adalah bapak Strukturalisme; teori evolusionisme liar-biadab-beradab adalah Lewis Henry Morgan).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "ant-sim-34",
        "materi": "ANTROPOLOGI RAGAWI & PALEOANTROPOLOGI",
        "topic": "Evaluasi Temuan Fosil Manusia Purba di Indonesia",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan terkait fosil hominid prasejarah yang ditemukan di wilayah kepulauan Indonesia!",
        "statements": [
            {
                "text": "Eugène Dubois menemukan fosil Pithecanthropus erectus (Homo erectus) di endapan Sungai Bengawan Solo dekat Desa Trinil, Ngawi, pada tahun 1891.",
                "correct": "Benar"
            },
            {
                "text": "Homo floresiensis yang ditemukan di Gua Liang Bua Flores memiliki tinggi badan sekitar 1 meter dan sering dijuluki 'Hobbit' oleh para ilmuwan.",
                "correct": "Benar"
            },
            {
                "text": "Meganthropus paleojavanicus memiliki rahang sangat kekar dan diperkirakan hidup sebagai pemakan daging karnivora murni di puncak pohon cemara.",
                "correct": "Salah"
            },
            {
                "text": "Homo wajakensis ditemukan di Campurdarat Tulungagung dan digolongkan sebagai manusia purba jenis Australopithecus yang belum berjalan tegak.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI HOMINID PRASEJARAH INDONESIA",
            "latex": "\\begin{aligned} \\text{Trinil (Dubois): } & \\text{Benar (Pithecanthropus erectus 1891)} \\\\ \\text{Liang Bua (Flores): } & \\text{Benar (Homo floresiensis, kerdil pulau/Hobbit)} \\\\ \\text{Meganthropus: } & \\text{Salah (Rahang kekar pemakan tumbuhan/herbivora)} \\\\ \\text{Homo wajakensis: } & \\text{Salah (Wajak adalah Homo sapiens modern awal, bukan Australopithecus)} \\end{aligned}",
            "legend": "• Menunjukkan kejelasan silsilah fosil hominid prasejarah di wilayah kepulauan Indonesia"
        },
        "hints": {
            "concept": "1=Benar (Dubois temukan Pithecanthropus di Trinil 1891). 2=Benar (Homo floresiensis dijuluki The Hobbit tinggi 106 cm). 3=Salah (Meganthropus adalah pemakan tumbuhan/tumbuhan dan buah, bukan karnivora pohon). 4=Salah (Homo wajakensis adalah Homo sapiens modern awal).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Salah, 4=Salah."
        }
    },
    {
        "id": "ant-sim-35",
        "materi": "DINAMIKA & PERUBAHAN KEBUDAYAAN",
        "topic": "Evaluasi Konsep Perubahan Kebudayaan: Akulturasi, Asimilasi, Difusi",
        "stem": "Berikut disajikan pernyataan mengenai konsep-konsep dinamika kebudayaan dalam ilmu antropologi. Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan!",
        "statements": [
            {
                "text": "Akulturasi terjadi ketika dua kebudayaan berbeda bertemu dan saling berinteraksi, menghasilkan kebudayaan baru tanpa menghilangkan ciri kepribadian asli masing-masing.",
                "correct": "Benar"
            },
            {
                "text": "Asimilasi merupakan proses peleburan dua kebudayaan atau lebih menjadi satu kebudayaan baru yang disertai dengan hilangnya identitas khas kebudayaan asal masing-masing.",
                "correct": "Benar"
            },
            {
                "text": "Difusi kebudayaan hanya dapat berlangsung melalui peperangan militer dan pemusnahan total terhadap etnis yang ditaklukkan.",
                "correct": "Salah"
            },
            {
                "text": "Glokalisasi adalah fenomena penyesuaian produk atau gagasan global dengan kondisi dan nilai-nilai selera kebudayaan lokal setempat.",
                "correct": "Benar"
            }
        ],
        "formula": {
            "title": "KONSEP DINAMIKA KEBUDAYAAN",
            "latex": "\\begin{aligned} \\text{Akulturasi: } & \\text{Benar (A + B } \\to \\text{ AB; kepribadian asli bertahan)} \\\\ \\text{Asimilasi: } & \\text{Benar (A + B } \\to \\text{ C; ciri lama lebur)} \\\\ \\text{Difusi: } & \\text{Salah (Dapat terjadi lewat migrasi damai, perdagangan, media)} \\\\ \\text{Glokalisasi: } & \\text{Benar (Global + Lokal, adaptasi selera setempat)} \\end{aligned}",
            "legend": "• Menunjukkan proses adaptasi dan perjumpaan kebudayaan di era modern dan tradisional"
        },
        "hints": {
            "concept": "1=Benar (Akulturasi: unsur baru berpadu tanpa hilangkan ciri lama). 2=Benar (Asimilasi: melebur menjadi budaya baru dan ciri lama sirna). 3=Salah (Difusi bisa lewat perdagangan, migrasi damai, bukan hanya perang). 4=Benar (Glokalisasi = global + lokal).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Salah, 4=Benar."
        }
    }
]
