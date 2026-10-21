# -*- coding: utf-8 -*-
"""
sejarah_lanjut_data_simulasi.py
--------------------------------
35 Authentic Simulasi CBT HOTS Questions for TKA 2026 Sejarah Lanjut (SMA/MA Soshum).
Anchored on Pusmendik Kemendikdasmen standards & BSKAP 033/H/KR/2024.
Composition:
- 25 MCQ items (sejl-sim-01 .. sejl-sim-25)
- 5 Multi-select items (sejl-sim-26 .. sejl-sim-30)
- 5 Matrix Benar-Salah items (sejl-sim-31 .. sejl-sim-35)
"""

SEJARAH_LANJUT_SIMULASI_ITEMS = [
    # -------------------------------------------------------------
    # 25 MCQ ITEMS (sejl-sim-01 .. sejl-sim-25)
    # -------------------------------------------------------------
    {
        "id": "sejl-sim-01",
        "materi": "DEMOKRASI PARLEMENTER (1950-1959)",
        "topic": "Jatuhnya Kabinet Sukiman & Perjanjian Mutual Security Act (MSA) 1951",
        "stem": "Kabinet Sukiman-Suwirjo (1951–1952) terpaksa mengembalikan mandat kepemerintahannya kepada Presiden Soekarno setelah dijatuhi mosi tidak percaya di parlemen. Krisis politik fundamental yang menyebabkan jatuhnya Kabinet Sukiman tersebut dipicu oleh...",
        "correct": "Penandatanganan nota kesepakatan bantuan ekonomi dan militer Mutual Security Act (MSA) antara Menteri Luar Negeri Achmad Soebardjo dengan Duta Besar AS Merle Cochran yang dinilai melanggar prinsip politik luar negeri bebas-aktif dan menyeret Indonesia ke blok Barat.",
        "distractors": [
            "Penolakan perwira angkatan laut terhadap pembelian kapal perang destroyer dari persemakmuran kerajaan Inggris.",
            "Kegagalan menteri pertanian menumpas serangan hama belalang di persawahan sepanjang pantai utara pulau Madura.",
            "Keputusan menteri dalam negeri membatalkan pelaksanaan pemilihan umum dewan perwakilan rakyat tingkat pertama.",
            "Tuntutan serikat buruh pelabuhan Tanjung Perak agar seluruh modal asing milik pengusaha Belanda disita tanpa ganti rugi."
        ],
        "formula": {
            "title": "KRONOLOGI JATUHNYA KABINET SUKIMAN (1952)",
            "latex": "\\text{Bantuan MSA (AS)} \\implies \\mathbf{\\text{Klausul Komitmen Pertahanan Blok Barat}} \\xrightarrow{\\mathbf{\\text{Kritik Parlemen/Masyumi}}} \\begin{cases} \\text{Pelanggaran Prinsip Bebas-Aktif} \\\\ \\text{Mosi Tidak Percaya DPR} \\\\ \\mathbf{\\text{Kabinet Sukiman Mundur (Feb 1952)}} \\end{cases}",
            "legend": "• Menegaskan komitmen keras parlemen era 1950-an terhadap doktrin 'Mendayung Antara Dua Karang' Hatta"
        },
        "hints": {
            "concept": "Kabinet Sukiman jatuh karena penandatanganan kerja sama bantuan MSA dengan AS oleh Menlu Achmad Soebardjo, yang dianggap melanggar politik luar negeri bebas aktif.",
            "execution": "Pilih opsi penandatanganan Mutual Security Act (MSA) dengan Dubes AS yang dinilai melanggar prinsip politik bebas-aktif."
        }
    },
    {
        "id": "sejl-sim-02",
        "materi": "KEBIJAKAN EKONOMI PASCA-KEMERDEKAAN",
        "topic": "Sistem Ekonomi Gerakan Benteng & Fenomena 'Ali-Baba' (1950-1953)",
        "stem": "Menteri Perdagangan Prof. Dr. Sumitro Djojohadikoesoemo pada masa Kabinet Natsir mencetuskan 'Gerakan Benteng' untuk menumbuhkan kelas pengusaha pribumi melalui pemberian lisensi impor khusus dan kredit perbankan negara. Namun program ini dinilai gagal mencapai target kemandirian ekonomi akibat fenomena 'Ali-Baba', yaitu...",
        "correct": "Kecenderungan pengusaha pribumi ('Ali') yang hanya menjadi tameng perantara dengan menjual kembali lisensi impor istimewa dan fasilitas kredit negara kepada pengusaha non-pribumi/Tionghoa ('Baba') demi keuntungan komisi jangka pendek tanpa membangun industri nyata.",
        "distractors": [
            "Penyitaan paksa seluruh perahu nelayan tradisional oleh kongsi pedagang rempah asal kepulauan Maluku.",
            "Pemberontakan laskar bersenjata di kawasan perkebunan tembakau Deli yang menolak penggunaan mata uang rupiah.",
            "Penolakan para pedagang pasar tradisional untuk menerima pembayaran transaksi menggunakan wesel pos pos giro.",
            "Kewajiban seluruh saudagar kain batik untuk mengekspor seluruh hasil produksinya ke pasar Uni Soviet."
        ],
        "formula": {
            "title": "ANATOMI DISTORSI SISTEM ALI-BABA",
            "latex": "\\text{Gerakan Benteng} \\xrightarrow{\\text{Distorsi Moral Hazard}} \\underbrace{\\text{Pengusaha Pribumi (Ali)}}_{\\text{Penerima Hak Lisensi Impor}} \\xrightarrow{\\text{Jual Lisensi}} \\underbrace{\\text{Pengusaha Non-Pribumi (Baba)}}_{\\text{Penyedia Modal Riil}}",
            "legend": "• Menyebabkan devisa negara terkuras dan gagal melahirkan borjuasi nasional yang kompetitif"
        },
        "hints": {
            "concept": "Sistem Ali-Baba adalah fenomena distorsi di mana pengusaha pribumi (Ali) hanya menjual lisensi impor dari pemerintah kepada pengusaha non-pribumi (Baba) demi keuntungan instan.",
            "execution": "Pilih: Pengusaha pribumi (Ali) menjual lisensi impor kepada pengusaha non-pribumi (Baba) demi komisi instan."
        }
    },
    {
        "id": "sejl-sim-03",
        "materi": "INTEGRASI WILAYAH NASIONAL",
        "topic": "Perjanjian New York 1962 & Penyelesaian Sengketa Irian Barat",
        "stem": "Sengketa diplomatik dan konfrontasi militer antara Indonesia dan Belanda mengenai Irian Barat akhirnya diselesaikan melalui penandatanganan Perjanjian New York (_New York Agreement_) pada 15 Agustus 1962 atas prakarsa diplomat AS Ellsworth Bunker. Ketentuan fundamental yang disepakati dalam perjanjian tersebut mengenai administrasi Irian Barat adalah...",
        "correct": "Belanda menyerahkan administrasi Irian Barat kepada otoritas transisi PBB yaitu UNTEA (_United Nations Temporary Executive Authority_), yang selanjutnya menyerahkan wilayah tersebut kepada Republik Indonesia paling lambat 1 Mei 1963 disertai kewajiban menggelar Penentuan Pendapat Rakyat (Pepera).",
        "distractors": [
            "Penetapan wilayah Irian Barat sebagai koloni persemakmuran otonom kerajaan Belanda selama seratus tahun ke depan.",
            "Pemisahan wilayah Papua menjadi lima negara bagian independen di bawah perlindungan militer Pakta ANZUS.",
            "Kewajiban pemerintah Indonesia membagi dua hasil tambang emas Grasberg dengan kementerian luar negeri Australia.",
            "Penghapusan seluruh hak pilih penduduk asli pulau Papua dalam pemilihan umum badan perwakilan daerah."
        ],
        "formula": {
            "title": "TAHAPAN PERJANJIAN NEW YORK (15 AGUSTUS 1962)",
            "latex": "\\text{Belanda} \\xrightarrow{\\text{1 Okt 1962}} \\mathbf{\\text{UNTEA (PBB)}} \\xrightarrow{\\mathbf{\\text{1 Mei 1963}}} \\mathbf{\\text{Administrasi RI}} \\xrightarrow{\\mathbf{\\text{Juli-Agt 1969}}} \\mathbf{\\text{Pepera (Integrasi Mutlak ke NKRI)}}",
            "legend": "• Delegasi RI dipimpin Menlu Dr. Soebandrio<br>• Hasil Pepera 1969 disahkan secara bulat oleh Sidang Umum PBB lewat Resolusi 2504"
        },
        "hints": {
            "concept": "Perjanjian New York 1962 menetapkan Belanda menyerahkan Irian Barat ke UNTEA (PBB), lalu UNTEA menyerahkannya ke RI (1 Mei 1963) dengan syarat diadakan Pepera.",
            "execution": "Pilih opsi: Belanda menyerahkan Irian Barat kepada UNTEA, yang kemudian menyerahkannya ke RI disertai kewajiban menggelar Pepera."
        }
    },
    {
        "id": "sejl-sim-04",
        "materi": "PROKLAMASI KEMERDEKAAN",
        "topic": "Rapat Raksasa Lapangan Ikada 19 September 1945",
        "stem": "Pada tanggal 19 September 1945, sekitar 300.000 rakyat Jakarta berhimpun di Lapangan Ikada (sekarang kawasan Monas) dengan bersenjatakan golok, bambu runcing, dan spanduk kemerdekaan, dikepung oleh barikade tentara Jepang bersenjata lengkap dengan senapan mesin dan tank. Makna kepemimpinan kenegarawanan Ir. Soekarno pada peristiwa Ikada tersebut adalah...",
        "correct": "Menunjukkan kepada dunia dan tentara pendudukan Jepang bahwa kedaulatan pemerintah Republik Indonesia memiliki legitimasi dan kepatuhan penuh dari rakyat jelata, di mana Soekarno berhasil membubarkan massa secara damai dan tertib hanya dengan pidato singkat tanpa memicu pertumpahan darah massal.",
        "distractors": [
            "Memerintahkan massa rakyat melancarkan serangan serentak membakar seluruh tank baja militer Jepang di lapangan.",
            "Menyerahkan teks naskah proklamasi kepada komando tentara Sekutu yang baru mendarat di pelabuhan Tanjung Priok.",
            "Mengumumkan penundaan kemerdekaan hingga tiba keputusan resmi dari sidang dewan keamanan Perserikatan Bangsa-Bangsa.",
            "Menunjuk para jenderal militer kekaisaran Jepang untuk duduk sebagai menteri pertahanan dalam kabinet presidensial."
        ],
        "formula": {
            "title": "SIGNIFIKANSI HISTORIS RAPAT IKADA 1945",
            "latex": "\\text{Rapat Ikada} \\implies \\begin{cases} \\mathbf{\\text{Uji Otoritas:}} & \\text{Rakyat hanya tunduk pada komando Bung Karno, bukan moncong senjata Jepang} \\\\ \\mathbf{\\text{Kemenangan Moral:}} & \\text{Menghindari pembantaian massal yang dapat menggagalkan legitimasi RI} \\\\ \\mathbf{\\text{Pesan Internasional:}} & \\text{Kemerdekaan RI didukung bulat oleh seluruh lapisan rakyat} \\end{cases}",
            "legend": "• Pidato Soekarno berlangsung sangat singkat (hanya beberapa menit) meminta rakyat percaya pada pemerintah dan pulang tertib"
        },
        "hints": {
            "concept": "Rapat Ikada 19 September 1945 membuktikan wibawa pemerintah RI: rakyat patuh pada Soekarno untuk pulang damai, menghindari pembantaian oleh tentara Jepang.",
            "execution": "Pilih: Menunjukkan pemerintah RI memiliki kepatuhan rakyat penuh, di mana Soekarno membubarkan massa damai tanpa pertumpahan darah."
        }
    },
    {
        "id": "sejl-sim-05",
        "materi": "PERLAWANAN DAERAH TERHADAP KOLONIALISME",
        "topic": "Perjanjian Bongaya 1667 & Keruntuhan Hegemoni Kesultanan Gowa",
        "stem": "Setelah pertempuran berdarah melawan pasukan gabungan VOC pimpinan Cornelis Speelman dan sekutunya Aru Palakka dari Bone, Sultan Hasanuddin dari Kesultanan Gowa-Tallo terpaksa menandatangani Perjanjian Bongaya pada 18 November 1667. Klausul paling merugikan yang meruntuhkan status Gowa sebagai penguasa maritim kawasan timur Nusantara adalah...",
        "correct": "Kewajiban menutup pelabuhan Somba Opu bagi seluruh pedagang asing non-Belanda, menyerahkan hak monopoli perdagangan rempah mutlak kepada VOC, serta meruntuhkan seluruh benteng pertahanan Gowa kecuali Benteng Ujung Pandang (Fort Rotterdam).",
        "distractors": [
            "Penyatuan seluruh armada perahu phinisi Gowa ke dalam armada angkatan perang kekaisaran Dinasti Qing Tiongkok.",
            "Pemberian mandat kepada raja Ternate untuk memungut bea cukai di sepanjang perairan Selat Makassar.",
            "Kewajiban para bangsawan Makassar memeluk agama Kristen Protestan dan menetap di perumahan benteng Batavia.",
            "Penghapusan seluruh hukum syariat Islam di wilayah jazirah Sulawesi Selatan oleh pendeta kerajaan Belanda."
        ],
        "formula": {
            "title": "KLAUSUL UTAMA PERJANJIAN BONGAYA (1667)",
            "latex": "\\text{Perjanjian Bongaya} \\implies \\begin{cases} \\mathbf{\\text{1. Monopoli Dagang:}} & \\text{VOC memonopoli perdagangan di pelabuhan Somba Opu} \\\\ \\mathbf{\\text{2. Pembongkaran Benteng:}} & \\text{Semua benteng diruntuhkan kecuali Benteng Ujung Pandang} \\\\ \\mathbf{\\text{3. Pengusiran Bangsa Lain:}} & \\text{Pedagang Portugis, Inggris, Denmark dilarang berniaga} \\\\ \\mathbf{\\text{4. Pengakuan Aru Palakka:}} & \\text{Aru Palakka diakui sebagai Raja Bone yang merdeka dari Gowa} \\end{cases}",
            "legend": "• Menandai runtuhnya kedaulatan maritim Kerajaan Gowa-Tallo di perairan Indonesia Timur"
        },
        "hints": {
            "concept": "Perjanjian Bongaya 1667 memaksa Hasanuddin mengakui monopoli VOC, menutup pelabuhan bagi pedagang asing selain VOC, dan meruntuhkan benteng pertahanan Gowa.",
            "execution": "Pilih opsi menutup pelabuhan bagi pedagang non-Belanda, monopoli rempah kepada VOC, dan meruntuhkan benteng pertahanan kecuali Fort Rotterdam."
        }
    },
    {
        "id": "sejl-sim-06",
        "materi": "PEMBENTUKAN TENTARA NASIONAL",
        "topic": "Dekrit Pembentukan TKR 5 Oktober 1945 & Pemilihan Jenderal Soedirman",
        "stem": "Pemerintah Republik Indonesia menerbitkan maklumat resmi pembentukan Tentara Keamanan Rakyat (TKR) pada 5 Oktober 1945 untuk menggantikan Badan Keamanan Rakyat (BKR) yang pasif. Alasan strategis dinaikkannya status organisasi bersenjata menjadi tentara reguler pertahanan negara pada saat itu adalah...",
        "correct": "Meningkatnya eskalasi ancaman militer akibat pendaratan pasukan tentara Sekutu (AFNEI) yang diboncengi tentara NICA/Belanda yang bertekad menegakkan kembali kekuasaan kolonial di Indonesia dengan kekuatan senjata.",
        "distractors": [
            "Perintah dari Markas Besar Perserikatan Bangsa-Bangsa agar Indonesia mengirim pasukan perdamaian ke semenanjung Sinai.",
            "Tuntutan para perwira tentara kekaisaran Jepang agar senjata mereka dibeli dengan mata uang emas batangan.",
            "Penolakan rakyat pedesaan terhadap pengesahan bendera Merah Putih sebagai simbol resmi kenegaraan.",
            "Rencana pembubaran seluruh kementerian kabinet presidensial pertama bentukan Presiden Soekarno."
        ],
        "formula": {
            "title": "EVOLUSI TENTARA NASIONAL INDONESIA",
            "latex": "\\underbrace{\\text{BKR (22 Agt 1945)}}_{\\text{Badan Kepolisian/Penolong Korban}} \\xrightarrow{\\mathbf{\\text{AFNEI \\& NICA Mendarat}}} \\underbrace{\\mathbf{\\text{TKR (5 Okt 1945)}}}_{\\mathbf{\\text{Tentara Bersenjata Resmi}}} \\longrightarrow \\text{TRI (1946)} \\longrightarrow \\text{TNI (3 Juni 1947)}",
            "legend": "• Konferensi TKR di Yogyakarta (12 Nov 1945) memilih Kolonel Soedirman (usia 29 tahun) sebagai Panglima Besar"
        },
        "hints": {
            "concept": "TKR dibentuk pada 5 Oktober 1945 karena situasi darurat militer: Sekutu (AFNEI) dan NICA mendarat untuk mengembalikan penjajahan Belanda dengan kekerasan.",
            "execution": "Pilih: Meningkatnya eskalasi ancaman militer akibat kedatangan tentara Sekutu (AFNEI) yang diboncengi tentara NICA."
        }
    },
    {
        "id": "sejl-lat-sim-07",
        "id": "sejl-sim-07",
        "materi": "DEMOKRASI TERPIMPIN (1959-1965)",
        "topic": "Konfrontasi Indonesia-Malaysia & Dwikora 1964",
        "stem": "Pada tanggal 3 Mei 1964 di Jakarta, Presiden Soekarno mengumumkan Dwi Komando Rakyat (Dwikora) dengan semboyan terkenal 'Ganyang Malaysia'. Landasan ideologis dan geopolitik yang mendasari penentangan keras pemerintah Indonesia terhadap pembentukan Federasi Malaysia adalah...",
        "correct": "Keyakinan bahwa pembentukan Federasi Malaysia merupakan proyek 'Neokolonialisme dan Imperialisme' (Nekolim) buatan Inggris yang dirancang untuk mengepung kedaulatan Republik Indonesia dan melestarikan pangkalan militer Barat di Asia Tenggara.",
        "distractors": [
            "Keinginan pemerintah Indonesia untuk menguasai seluruh cadangan minyak bumi dan gas alam di lepas pantai Brunei Darussalam.",
            "Penolakan parlemen Malaysia terhadap penggunaan bahasa Melayu sebagai bahasa resmi pergaulan antarnegara rumpun serumpun.",
            "Perjanjian rahasia antara perwira militer Indonesia dengan pemerintah komunis Kuba untuk mendirikan pangkalan angkatan laut di Selat Malaka.",
            "Tuntutan para pengusaha karet alam Sumatera agar pelabuhan Singapura ditutup secara permanen bagi pelayaran niaga."
        ],
        "formula": {
            "title": "DOKTRIN KONFRONTASI DWIKORA (1964)",
            "latex": "\\text{Pembentukan Malaysia (Tengku Abdul Rahman)} \\xrightarrow{\\mathbf{\\text{Analisis Sukarno: Proyek Nekolim Inggris}}} \\mathbf{\\text{Dwikora (3 Mei 1964)}} \\implies \\begin{cases} \\text{1. Perhebat ketahanan revolusi Indonesia} \\\\ \\text{2. Bantu perjuangan rakyat Sabah, Sarawak, Brunei, Malaya} \\end{cases}",
            "legend": "• Berujung pada konfrontasi bersenjata di perbatasan Kalimantan dan keluarnya Indonesia dari PBB pada 1965"
        },
        "hints": {
            "concept": "Soekarno menentang pembentukan Malaysia karena menganggapnya sebagai proyek 'Nekolim' (neokolonialisme) Inggris yang menjadi pangkalan ancaman bagi Indonesia.",
            "execution": "Pilih: Keyakinan bahwa Federasi Malaysia adalah proyek Neokolonialisme Inggris (Nekolim) untuk mengepung kedaulatan RI."
        }
    },
    {
        "id": "sejl-sim-08",
        "materi": "PERJUANGAN DIPLOMASI KEMERDEKAAN",
        "topic": "Perundingan Linggarjati 1946 & Kompromi Teritorial",
        "stem": "Perundingan Linggarjati yang berlangsung di Kuningan, Jawa Barat, pada November 1946 dipimpin oleh Perdana Menteri Sutan Sjahrir dan komisi jenderal Belanda pimpinan Willem Schermerhorn. Butir kesepakatan teritorial pokok dalam naskah persetujuan Linggarjati yang sempat memicu perdebatan sengit di dalam negeri adalah...",
        "correct": "Pemerintah Belanda mengakui secara _de facto_ wilayah kekuasaan Republik Indonesia hanya meliputi wilayah Jawa, Madura, dan Sumatera.",
        "distractors": [
            "Penyerahan kedaulatan mutlak seluruh bekas Hindia Belanda dari Sabang sampai Merauke kepada kabinet Sjahrir.",
            "Peleburan seluruh pulau Kalimantan dan Sulawesi ke dalam zona otonomi militer kerajaan Britania Raya.",
            "Kewajiban bagi TNI untuk menyerahkan seluruh meriam rampasan perang kepada markas besar tentara Gurkha.",
            "Penetapan mata uang gulden Belanda sebagai satu-satunya alat pembayaran yang sah di seluruh kepulauan Indonesia."
        ],
        "formula": {
            "title": "TIGA BUTIR POKOK PERSETUJUAN LINGGARJATI (1946)",
            "latex": "\\text{Linggarjati} \\implies \\begin{cases} \\mathbf{\\text{1. Pengakuan De Facto:}} & \\mathbf{\\text{RI hanya meliputi Jawa, Madura, dan Sumatera}} \\\\ \\mathbf{\\text{2. Pembentukan RIS:}} & \\text{RI menjadi salah satu negara bagian dalam Republik Indonesia Serikat} \\\\ \\mathbf{\\text{3. Uni Indonesia-Belanda:}} & \\text{RIS dan Belanda membentuk Uni di bawah Mahkota Ratu Belanda} \\end{cases}",
            "legend": "• Ditandatangani resmi 25 Maret 1947<br>• Dilanggar sepihak oleh Belanda melalui Agresi Militer Belanda I (21 Juli 1947)"
        },
        "hints": {
            "concept": "Perjanjian Linggarjati mengakui wilayah de facto RI secara terbatas, yaitu hanya Jawa, Madura, dan Sumatera.",
            "execution": "Pilih opsi: Pengakuan de facto wilayah RI hanya meliputi Jawa, Madura, dan Sumatera."
        }
    },
    {
        "id": "sejl-sim-09",
        "materi": "KONFLIK POLITIK REGIONAL ERA 1950-AN",
        "topic": "Pemberontakan PRRI/Permesta & Keterlibatan Asing (1958)",
        "stem": "Pemberontakan Pemerintah Revolusioner Republik Indonesia (PRRI) diproklamasikan oleh Letkol Ahmad Husein di Padang pada 15 Februari 1958, disusul oleh Piagam Perjuangan Rakyat Semesta (Permesta) di Manado. Bukti keterlibatan intervensi intelijen asing dalam membantu persenjataan dan logistik militer PRRI/Permesta terungkap ke publik secara tak terbantahkan melalui insiden...",
        "correct": "Ditembak jatuhnya pesawat pembom B-26 Invader milik pemberontak di perairan Ambon oleh tembakan TNI yang dipiloti oleh agen rahasia CIA asal Amerika Serikat bernama Allen Lawrence Pope pada 18 Mei 1958.",
        "distractors": [
            "Terdamparnya kapal selam bertenaga nuklir milik Uni Soviet di lepas pantai teluk Manado tanpa awak kapal.",
            "Ditemukannya peti-peti amunisi buatan pabrik senjata kekaisaran Austro-Hungaria di pedalaman hutan Bukit Barisan.",
            "Tertangkapnya perwira komando angkatan darat kerajaan Belanda saat menyamar sebagai saudagar kain sutra di pasar Bukittinggi.",
            "Pengakuan menteri luar negeri Jepang di forum PBB bahwa mereka mengirim tentara bayaran ke Minahasa."
        ],
        "formula": {
            "title": "KASUS ALLEN POPE & INTERVENSI CIA PADA PRRI/PERMESTA (1958)",
            "latex": "\\text{Pesawat B-26 Ditembak Jatuh (18 Mei 1958)} \\implies \\mathbf{\\text{Pilot Allen Pope (Agen CIA) Tertangkap}} \\implies \\begin{cases} \\text{Bukti intervensi terselubung AS terbongkar} \\\\ \\text{Washington menghentikan bantuan militer PRRI} \\\\ \\text{TNI (Operasi 17 Agustus & Merdeka) memadamkan pemberontakan} \\end{cases}",
            "legend": "• Menjadi pukulan diplomasi telak bagi AS dan memaksa Presiden Eisenhower melunakkan sikap diplomatik terhadap Soekarno"
        },
        "hints": {
            "concept": "Bukti keterlibatan CIA Amerika Serikat pada PRRI/Permesta terbongkar saat pesawat bomber B-26 yang dipiloti agen CIA Allen Pope ditembak jatuh di Ambon (18 Mei 1958).",
            "execution": "Pilih opsi ditembak jatuhnya pesawat bomber B-26 di perairan Ambon yang dipiloti agen CIA Allen Lawrence Pope."
        }
    },
    {
        "id": "sejl-sim-10",
        "materi": "ERA REFORMASI 1998",
        "topic": "Tragedi Trisakti 12 Mei 1998 & Gelombang Eskalasi Kerusuhan",
        "stem": "Aksi damai mahasiswa Universitas Trisakti menuntut reformasi ekonomi dan politik pada 12 Mei 1998 berujung pada penembakan peluru tajam oleh aparat keamanan di depan kampus Grogol Jakarta. Gugurnya empat mahasiswa Trisakti (Elang Mulia Lesmana, Hafidin Royan, Heri Hertanto, dan Hendriawan Sie) memiliki makna historis menentukan karena...",
        "correct": "Menjadi martir ('Pahlawan Reformasi') yang meruntuhkan legitimasi moral pemerintah Orde Baru, menyatukan seluruh elemen bangsa dalam mosi tidak percaya, dan menjadi pemicu langsung ledakan demonstrasi massa yang memaksa pengunduran diri Soeharto sembilan hari kemudian.",
        "distractors": [
            "Mendorong Dewan Keamanan PBB mengirim pasukan multinasional untuk menduduki seluruh instalasi kementerian di Jakarta.",
            "Mengakibatkan dibatalkannya seluruh jadwal penerbangan komersial internasional di kawasan Asia Tenggara selama satu tahun.",
            "Memaksa para pemilik modal perbankan swasta menutup seluruh kantor cabang bank mereka di luar negeri.",
            "Menyebabkan dibubarkannya struktur kepolisian daerah dan pengalihan tugas yudisial kepada pimpinan serikat buruh."
        ],
        "formula": {
            "title": "TITIK BALIK SEJARAH: TRAGEDI TRISAKTI 12 MEI 1998",
            "latex": "\\begin{aligned} \\text{Penembakan 4 Mahasiswa Trisakti} & \\implies \\mathbf{\\text{Gugurnya Pahlawan Reformasi}} \\\\ & \\implies \\begin{cases} \\text{Kerusuhan Massal Jakarta (13-15 Mei)} \\\\ \\text{Pendudukan Gedung DPR/MPR oleh Ribuan Mahasiswa} \\\\ \\mathbf{\\text{Pengunduran Diri Soeharto (21 Mei 1998)}} \\end{cases} \\end{aligned}",
            "legend": "• Menjadi simbol perjuangan demokrasi dan penegakan supremasi hukum di Indonesia"
        },
        "hints": {
            "concept": "Tragedi Trisakti 12 Mei 1998 melahirkan 'Pahlawan Reformasi' yang memicu kemarahan publik luas dan menjadi katalis utama jatuhnya Soeharto 21 Mei 1998.",
            "execution": "Pilih: Menjadi martir Pahlawan Reformasi yang meruntuhkan legitimasi moral Orba dan memicu gelombang desakan pengunduran diri Soeharto."
        }
    },
    {
        "id": "sejl-sim-11",
        "materi": "ERA REFORMASI (1998-SEKARANG)",
        "topic": "Amandemen Konstitusi UUD 1945 (1999-2002)",
        "stem": "Dalam kurun waktu empat tahun berturut-turut (1999–2002), Sidang Tahunan MPR RI berhasil mengesahkan empat kali amandemen terhadap Undang-Undang Dasar 1945. Salah satu substansi reformasi ketatanegaraan paling penting dari amandemen tersebut untuk mencegah terulangnya kekuasaan presiden yang otoriter adalah...",
        "correct": "Pembatasan masa jabatan Presiden dan Wakil Presiden Republik Indonesia menjadi maksimal dua periode (masing-masing 5 tahun per periode) serta pembentukan Mahkamah Konstitusi (MK) untuk menguji konstitusionalitas undang-undang terhadap UUD.",
        "distractors": [
            "Penghapusan seluruh hak asasi manusia warga negara dalam mengemukakan pendapat di muka umum.",
            "Penyerahan hak pengangkatan menteri negara kepada pertimbangan para perwira dewan pertahanan militer.",
            "Pemberian wewenang kepada Dewan Perwakilan Daerah untuk membubarkan dewan perwakilan rakyat hasil pemilu.",
            "Penerapan sistem monarki konstitusional di mana presiden dipilih seumur hidup oleh dewan penasihat istana."
        ],
        "formula": {
            "title": "HASIL KUNCI AMANDEMEN UUD 1945 (1999–2002)",
            "latex": "\\text{Amandemen UUD 1945} \\iff \\begin{cases} \\mathbf{\\text{Pasal 7:}} & \\mathbf{\\text{Presiden memegang jabatan 5 thn, dapat dipilih kembali HANYA 1 KALI}} \\\\ \\mathbf{\\text{Pasal 24C:}} & \\mathbf{\\text{Pembentukan Mahkamah Konstitusi (Judicial Review)}} \\\\ \\text{Lembaga Baru:}} & \\text{Dewan Perwakilan Daerah (DPD) & Komisi Yudisial (KY)} \\\\ \\text{Kedaulatan:}} & \\text{Kedaulatan di tangan rakyat dilaksanakan menurut UUD (bukan di MPR)} \\end{cases}",
            "legend": "• Menghilangkan doktrin supremasi mutlak presiden (_executive heavy_) warisan era sebelumnya"
        },
        "hints": {
            "concept": "Amandemen UUD 1945 (Pasal 7) membatasi masa jabatan presiden maksimal 2 periode (10 tahun) dan membentuk Mahkamah Konstitusi (MK).",
            "execution": "Pilih opsi pembatasan masa jabatan presiden maksimal 2 periode serta pembentukan Mahkamah Konstitusi (MK)."
        }
    },
    {
        "id": "sejl-sim-12",
        "materi": "HISTORIOGRAFI HINDU-BUDDHA",
        "topic": "Teori Masuknya Pengaruh Hindu-Buddha: Teori Arus Balik (F.D.K. Bosch)",
        "stem": "Dalam perdebatan teori masuk dan berkembangnya kebudayaan Hindu-Buddha di kepulauan Nusantara, teori 'Arus Balik' yang diajukan oleh Dr. F.D.K. Bosch dinilai paling mampu menjelaskan peran aktif bangsa Indonesia. Argumentasi ilmiah pokok yang menopang Teori Arus Balik tersebut adalah...",
        "correct": "Kaum terpelajar dan pemuda dari kepulauan Nusantara secara aktif berlayar ke India untuk menimba ilmu agama dan filsafat di pusat-pusat keilmuan seperti Universitas Nalanda, lalu kembali ke tanah air untuk mengajarkan dan menyebarkan ajaran tersebut kepada masyarakatnya.",
        "distractors": [
            "Pasukan ksatria penakluk asal India menginvasi pulau Jawa dengan kekuatan senjata perang gajah lalu mendirikan koloni penindas.",
            "Para saudagar kasta Waisya memaksakan pernikahan dagang dengan putri-putri kepala suku di seluruh pedalaman Sumatera.",
            "Para biksu India diculik oleh para bajak laut Selat Sunda dan dipaksa menuliskan prasasti batu menggunakan huruf Pallawa.",
            "Kaisar India mengeluarkan dekrit kerajaan yang mewajibkan seluruh penduduk kepulauan Asia Tenggara membayar upeti beras."
        ],
        "formula": {
            "title": "TEORI ARUS BALIK BOSCH (EVIDENCE PRASASTI NALANDA 860 M)",
            "latex": "\\text{Arus Balik} \\implies \\underbrace{\\text{Pelajar Nusantara Berlayar ke India (Nalanda)}}_{\\text{Inisiatif & Agensi Aktif Pribumi}} \\xrightarrow{\\text{Mendalami Dharma}} \\underbrace{\\text{Kembali ke Nusantara Menjadi Tokoh Agama/Pujangga}}_{\\text{Penyebaran Mandiri}}",
            "legend": "• Dibuktikan oleh Prasasti Nalanda: Raja Balaputradewa dari Sriwijaya membangun asrama bagi pelajar Sriwijaya di Nalanda, India"
        },
        "hints": {
            "concept": "Teori Arus Balik F.D.K. Bosch menekankan peran aktif pemuda Nusantara yang belajar ke India (seperti Nalanda), lalu pulang menyebarkan ilmunya.",
            "execution": "Pilih opsi pemuda Nusantara secara aktif berlayar belajar ke India (Universitas Nalanda) lalu pulang menyebarkan ajaran di tanah air."
        }
    },
    {
        "id": "sejl-sim-13",
        "materi": "PERLAWANAN MARITIM TERHADAP PORTUGIS",
        "topic": "Sultan Baabullah & Pengusiran Portugis dari Ternate 1575",
        "stem": "Sultan Baabullah dari Kesultanan Ternate memimpin perang semesta rakyat Maluku melawan penjajah Portugis yang berpusat di Benteng Gamlamo (Nostra Senhora da Victoria) hingga bangsa Portugis terusir dari Ternate pada tahun 1575. Peristiwa tragis yang menyulut sumpah perang total Sultan Baabullah adalah...",
        "correct": "Pembunuhan licik dan keji terhadap ayahandanya, Sultan Khairun, oleh gubernur Portugis Diogo Lopes de Mesquita di dalam benteng sesaat setelah kedua belah pihak mengucapkan sumpah persahabatan damai.",
        "distractors": [
            "Pencurian seluruh pohon cengkih purba di lereng Gunung Gamalama oleh tentara angkatan laut Spanyol.",
            "Penolakan perwira militer Portugis untuk membagikan meriam perunggu kepada para petani kelapa di pulau Tidore.",
            "Tenggelamnya kapal layar permaisuri sultan di perairan Laut Maluku akibat hantaman badai topan tropis.",
            "Penerbitan surat izin monopoli rempah-rempah yang ditandatangani oleh Paus di Roma untuk pedagang Inggris."
        ],
        "formula": {
            "title": "PENGUSIRAN PORTUGIS OLEH SULTAN BAABULLAH (1570-1575)",
            "latex": "\\text{Pembunuhan Sultan Khairun (1570)} \\implies \\mathbf{\\text{Pengepungan Benteng Gamlamo Selama 5 Tahun}} \\implies \\begin{cases} \\text{Portugis kehabisan pasokan makanan} \\\\ \\mathbf{\\text{Portugis menyerah & terusir ke Timor (1575)}} \\\\ \\text{Ternate mencapai puncak kekuasaan di 72 pulau} \\end{cases}",
            "legend": "• Sultan Baabullah digelari 'Penguasa 72 Pulau' (_De Heer van Twee-en-Zeventig Eilanden_)"
        },
        "hints": {
            "concept": "Sultan Baabullah mengepung benteng Portugis selama 5 tahun hingga terusir pada 1575 karena ayahnya, Sultan Khairun, dibunuh secara licik di benteng Portugis.",
            "execution": "Pilih: Pembunuhan licik terhadap ayahnya, Sultan Khairun, oleh gubernur Portugis Diogo Lopes de Mesquita di dalam benteng."
        }
    },
    {
        "id": "sejl-sim-14",
        "materi": "KOLONIALISME HINDIA BELANDA",
        "topic": "Kebijakan Herman Willem Daendels: Jalan Raya Pos (Grote Postweg)",
        "stem": "Gubernur Jenderal Herman Willem Daendels (1808–1811) yang dikirim oleh Raja Louis Napoleon memerintahkan pembangunan Jalan Raya Pos (_Grote Postweg_) sepanjang kurang lebih 1.000 km dari Anyer hingga Panarukan dengan mengorbankan ribuan nyawa rakyat akibat kerja paksa (rodi). Alasan militer-strategis paling mendesak dari pembangunan jalan pos tersebut adalah...",
        "correct": "Mempercepat mobilisasi pasukan tentara dan logistik militer di sepanjang Pulau Jawa guna mempertahankan tanah Jawa dari kemungkinan serangan invasi armada laut kerajaan Inggris (Britania Raya).",
        "distractors": [
            "Mempermudah pengangkutan turis liburan keluarga bangsawan Eropa menuju tempat peristirahatan di pegunungan Dieng.",
            "Membangun jalur balap kereta kuda internasional untuk menarik penanaman modal perbankan dari Amerika Utara.",
            "Menghubungkan seluruh istana kesultanan tradisional agar para pangeran keraton dapat mengadakan upacara pernikahan bersama.",
            "Menyediakan rute jalan kaki khusus bagi para pekerja migran yang ingin berziarah ke makam-makam wali sanga."
        ],
        "formula": {
            "title": "FUNGSI STRATEGIS GROTE POSTWEG (1808)",
            "latex": "\\text{Tugas Utama Daendels} = \\mathbf{\\text{Pertahankan Jawa dari Invasi Inggris}} \\implies \\mathbf{\\text{Pembangunan Jalan Raya Pos Anyer-Panarukan}} \\implies \\begin{cases} \\text{Mobilisasi Kilat Pasukan Infantri/Artileri} \\\\ \\text{Komunikasi Cepat Pos Militer} \\\\ \\text{Kerja Rodi Memakan Ribuan Korban Pribumi} \\end{cases}",
            "legend": "• Daendels dikenal dengan julukan 'Marsekal Guntur' (_de IJzeren Maarschalk_)"
        },
        "hints": {
            "concept": "Daendels membangun Jalan Raya Pos Anyer-Panarukan untuk kepentingan pertahanan militer: mempermudah mobilitas pasukan menahan invasi armada Inggris.",
            "execution": "Pilih opsi: Mempercepat mobilisasi pasukan dan logistik militer untuk mempertahankan Jawa dari serangan invasi armada laut Inggris."
        }
    },
    {
        "id": "sejl-sim-15",
        "materi": "PERPECAHAN KEPEMIMPINAN NASIONAL",
        "topic": "Pengunduran Diri Mohammad Hatta Sebagai Wakil Presiden (1 Desember 1956)",
        "stem": "Pada tanggal 1 Desember 1956, Drs. Mohammad Hatta secara resmi mengajukan pengunduran dirinya dari jabatan Wakil Presiden Republik Indonesia, yang menandai berakhirnya era 'Dwi-Tunggal' Soekarno-Hatta. Faktor ketidaksepahaman prinsipil yang menyebabkan Bung Hatta memilih mundur adalah...",
        "correct": "Perbedaan pandangan yang kian tajam mengenai arah demokrasi di mana Bung Karno semakin condong ke arah Demokrasi Terpimpin yang menyertakan PKI dan memusatkan kekuasaan pada figur presiden, sementara Bung Hatta tetap berpegang teguh pada supremasi hukum demokrasi parlementer dan menolak keterlibatan komunisme.",
        "distractors": [
            "Keinginan Bung Hatta untuk kembali memimpin pergerakan laskar gerilya bersenjata di pegunungan Sumatera Barat.",
            "Penolakan kabinet kementerian terhadap rencana Bung Hatta menerbitkan buku teks tata bahasa ekonomi kerakyatan.",
            "Sengketa kepemilikan tanah perkebunan teh di kawasan lereng Gunung Salak antara keluarga kedua tokoh proklamator.",
            "Tuntutan dewan jenderal angkatan laut agar jabatan wakil presiden dialihkan kepada perwira aktif militer."
        ],
        "formula": {
            "title": "PECAHNYA DWI-TUNGGAL SOEKARNO-HATTA (1956)",
            "latex": "\\Delta \\text{Visi Kepemimpinan} = \\begin{cases} \\mathbf{\\text{Bung Karno:}} & \\text{Revolusi belum selesai, persatuan Nasakom, Demokrasi Terpimpin} \\\\ \\mathbf{\\text{Bung Hatta:}} & \\mathbf{\\text{Fokus pembangunan ekonomi, menolak PKI, demokrasi berdasar hukum (Pasal 27)}} \\end{cases}",
            "legend": "• Mundurnya Hatta memicu gelombang kekecewaan daerah luar Jawa (mendorong pergolakan Dewan Banteng, Gajah, Manguni)"
        },
        "hints": {
            "concept": "Bung Hatta mundur karena menolak arah Demokrasi Terpimpin Soekarno yang otoriter dan menyertakan PKI, serta berbeda pandangan tentang tata negara dan hukum.",
            "execution": "Pilih perbedaan tajam mengenai arah demokrasi di mana Soekarno condong ke Demokrasi Terpimpin & PKI sementara Hatta konsisten pada supremasi hukum demokrasi."
        }
    },
    {
        "id": "sejl-sim-16",
        "materi": "ERA ORDE BARU (1966-1998)",
        "topic": "Peristiwa Malari 15 Januari 1974 & Dominasi Modal Asing",
        "stem": "Peristiwa Malapetaka Lima Belas Januari (Malari) meletus di Jakarta pada 15 Januari 1974 saat kunjungan Perdana Menteri Jepang Kakuei Tanaka. Isu substansial yang disuarakan oleh para mahasiswa pimpinan Hariman Siregar dalam demonstrasi yang berujung kerusuhan tersebut adalah...",
        "correct": "Kritik keras terhadap dominasi modal asing (terutama korporasi Jepang) yang dianggap mematikan pengusaha lokal serta kecaman atas gurita kekuasaan para Asisten Pribadi (Aspri) Presiden yang korup di lingkaran dalam Istana.",
        "distractors": [
            "Tuntutan agar pemerintah Orde Baru membeli seluruh obligasi surat utang perbankan pemerintah Uni Soviet.",
            "Penolakan terhadap penyelenggaraan pekan olahraga nasional di kompleks stadion Gelora Bung Karno.",
            "Permintaan agar bahasa Jepang diwajibkan menjadi bahasa pengantar di seluruh perguruan tinggi negeri.",
            "Keinginan kaum muda untuk membubarkan seluruh organisasi serikat pramuka kepanduan nasional."
        ],
        "formula": {
            "title": "ANATOMI PERISTIWA MALARI (15 JANUARI 1974)",
            "latex": "\\text{Isu Malari} = \\begin{cases} \\mathbf{\\text{Ekonomi:}} & \\text{Dominasi penanaman modal Jepang, mematikan industri rakyat} \\\\ \\mathbf{\\text{Politik:}} & \\text{Kekuasaan bayangan Asisten Pribadi Presiden (Aspri: Ali Moertopo, Soedjono Hoemardani)} \\\\ \\mathbf{\\text{Dampak Rezim:}} & \\mathbf{\\text{Pemberedelan pers (Harian KAMI, Pedoman, Indonesia Raya) \\& pembubaran Aspri}} \\end{cases}",
            "legend": "• Menandai awal pengetatan kontrol represif rezim Orde Baru terhadap gerakan mahasiswa di kampus"
        },
        "hints": {
            "concept": "Peristiwa Malari 1974 dipicu kritik terhadap dominasi modal asing (Jepang) dan kekuasaan para Asisten Pribadi (Aspri) Presiden Soeharto yang dinilai korup.",
            "execution": "Pilih: Kritik keras terhadap dominasi modal asing (korporasi Jepang) serta kecaman atas kekuasaan Asisten Pribadi (Aspri) Presiden."
        }
    },
    {
        "id": "sejl-sim-17",
        "materi": "ERA REFORMASI (1998-SEKARANG)",
        "topic": "Pembentukan Komisi Pemberantasan Korupsi (KPK) Tahun 2002",
        "stem": "Salah satu capaian institusional terpenting era Reformasi dalam mewujudkan tata kelola pemerintahan yang bersih dan bebas korupsi, kolusi, dan nepotisme (KKN) adalah disahkannya Undang-Undang No. 30 Tahun 2002 pada masa pemerintahan Presiden Megawati Soekarnoputri. UU tersebut mengamanatkan pembentukan...",
        "correct": "Komisi Pemberantasan Tindak Pidana Korupsi (KPK) sebagai lembaga independen yang berwenang melakukan penyelidikan, penyidikan, dan penuntutan kasus korupsi luar biasa (_extraordinary crime_).",
        "distractors": [
            "Mahkamah Militer Luar Biasa untuk mengadili para perwira komando pertahanan yang melakukan pelanggaran disiplin.",
            "Badan Arbitrase Nasional untuk menyelesaikan sengketa harga tanah warisan para bangsawan feodal keraton.",
            "Komite Sensor Nasional untuk mengawasi dan menyaring seluruh tayangan film komersial layar lebar.",
            "Dewan Stabilitas Moneter untuk menentukan besaran suku bunga kredit pinjaman bagi para pemilik modal asing."
        ],
        "formula": {
            "title": "MANDAT REFORMASI: PEMBENTUKAN KPK (UU 30/2002)",
            "latex": "\\text{Tap MPR XI/1998 (Bebas KKN)} \\xrightarrow{\\mathbf{\\text{UU No. 30/2002 (Era Megawati)}}} \\mathbf{\\text{Komisi Pemberantasan Korupsi (KPK)}} \\implies \\begin{cases} \\text{Lembaga Negara Independen} \\\\ \\text{Wewenang Super: Sadap, Sidik, Tuntut} \\\\ \\text{Fokus Kasus Penegak Hukum & Penyelenggara Negara} \\end{cases}",
            "legend": "• Ketua pertama KPK: Taufiequrachman Ruki (periode 2003-2007)"
        },
        "hints": {
            "concept": "UU No. 30/2002 pada era Presiden Megawati melahirkan Komisi Pemberantasan Korupsi (KPK) sebagai lembaga independen pemberantas korupsi.",
            "execution": "Pilih opsi: Komisi Pemberantasan Tindak Pidana Korupsi (KPK) sebagai lembaga independen penyelidik, penyidik, dan penuntut korupsi."
        }
    },
    {
        "id": "sejl-sim-18",
        "materi": "SEJARAH DUNIA: PERANG DINGIN",
        "topic": "Pembentukan Pakta Pertahanan Warsawa 1955",
        "stem": "Uni Soviet bersama tujuh negara satelit sosialis di Eropa Timur (antara lain Polandia, Jerman Timur, Cekoslowakia, dan Hungaria) menandatangani pembentukan Pakta Warsawa (_Warsaw Pact_) pada Mei 1955. Katalis langsung yang mendorong Uni Soviet membentuk aliansi militer tersebut adalah...",
        "correct": "Resmi diterimanya Republik Federal Jerman (Jerman Barat) ke dalam keanggotaan aliansi militer North Atlantic Treaty Organization (NATO) yang dinilai Moskow sebagai ancaman re-militerisasi langsung terhadap keamanan blok Timur.",
        "distractors": [
            "Serangan armada kapal induk angkatan laut Jepang ke pangkalan pelabuhan militer Vladivostok di Samudra Pasifik.",
            "Penolakan pemerintah kerajaan Mesir untuk membagikan deviden tarif Terusan Suez kepada perbankan Uni Soviet.",
            "Rencana pembangunan stasiun satelit orbit angkasa luar bersama antara Amerika Serikat dan kekaisaran Ethiopia.",
            "Penyatuan mata uang franc Perancis dengan mata uang mark Jerman dalam pasar bersama benua Eropa."
        ],
        "formula": {
            "title": "RESPON GEOPOLITIK: KELAHIRAN PAKTA WARSAWA (1955)",
            "latex": "\\begin{aligned} \\text{NATO Berdiri (1949)} & \\xrightarrow{\\mathbf{\\text{Jerman Barat Masuk NATO (Mei 1955)}}} \\mathbf{\\text{Kelahiran Pakta Warsawa (14 Mei 1955)}} \\\\ & \\implies \\text{Polarisasi Total Sistem Blok Bipolar di Eropa (Besi Tirai)} \\end{aligned}",
            "legend": "• Dibubarkan secara resmi di Praha pada 1 Juli 1991 seiring runtuhnya hegemoni Soviet"
        },
        "hints": {
            "concept": "Pakta Warsawa dibentuk pada Mei 1955 sebagai reaksi langsung atas masuknya Jerman Barat ke dalam NATO yang memicu kekhawatiran militer Soviet.",
            "execution": "Pilih opsi: Masuknya Republik Federal Jerman (Jerman Barat) ke dalam keanggotaan aliansi militer NATO."
        }
    },
    {
        "id": "sejl-sim-19",
        "materi": "SEJARAH DUNIA: PERANG DINGIN",
        "topic": "Perang Korea (1950-1953) & Gencatan Senjata Panmunjom",
        "stem": "Perang Korea meletus pada 25 Juni 1950 ketika pasukan Korea Utara (didukung Uni Soviet dan Tiongkok) melintasi Garis Paralel ke-38 dan menginvasi Korea Selatan (didukung koalisi PBB pimpinan AS). Perang dahsyat ini diakhiri pada Juli 1953 melalui penandatanganan Perjanjian Gencatan Senjata Panmunjom yang menghasilkan konsensus...",
        "correct": "Pembentukan Zona Demiliterisasi (DMZ) selebar 4 km di sekitar Garis Lintang Paralel 38 derajat Utara sebagai garis batas gencatan senjata permanen tanpa adanya penandatanganan perjanjian damai definitif.",
        "distractors": [
            "Penyatuan seluruh semenanjung Korea di bawah kepemimpinan presiden terpilih secara demokratis di Seoul.",
            "Peleburan seluruh kekuatan militer semenanjung Korea ke dalam armada komando pasukan perdamaian PBB.",
            "Penyerahan kepemilikan kepulauan Jeju kepada kekaisaran Jepang sebagai kompensasi ganti rugi perang.",
            "Pembubaran seluruh pangkalan militer Amerika Serikat di kawasan Asia Timur dan penarikan pasukan sekutu."
        ],
        "formula": {
            "title": "STATUS KUO PERANG KOREA (PANMUNJOM 1953)",
            "latex": "\\text{Gencatan Senjata 1953} \\implies \\begin{cases} \\mathbf{\\text{Garis Paralel 38° Utara:}} & \\mathbf{\\text{Zona Demiliterisasi (DMZ)}} \\\\ \\mathbf{\\text{Status De Jure:}} & \\mathbf{\\text{Secara teknis masih dalam kondisi perang (Armistice, bukan Damai)}} \\\\ \\text{Dua Entitas:}} & \\text{DPRK (Utara - Kim Il Sung) vs ROK (Selatan - Syngman Rhee)} \\end{cases}",
            "legend": "• Menjadi 'Proxy War' pertama berskala besar yang menewaskan jutaan jiwa dalam Perang Dingin"
        },
        "hints": {
            "concept": "Perang Korea berakhir dengan kesepakatan gencatan senjata di Panmunjom (1953) yang menetapkan DMZ di Garis Paralel 38 tanpa traktat perdamaian definitif.",
            "execution": "Pilih pembentukan Zona Demiliterisasi (DMZ) di Garis Paralel 38° Utara tanpa perjanjian damai definitif."
        }
    },
    {
        "id": "sejl-sim-20",
        "materi": "SEJARAH DUNIA: PERJANJIAN PERDAMAIAN",
        "topic": "Perjanjian Perdamaian Camp David 1978",
        "stem": "Presiden AS Jimmy Carter memediasi pertemuan rahasia selama 12 hari di Camp David, Maryland, antara Presiden Mesir Anwar Sadat dan Perdana Menteri Israel Menachem Begin pada September 1978. Terobosan diplomatik bersejarah yang dicapai dari Perjanjian Damai Camp David (_Camp David Accords_) adalah...",
        "correct": "Penandatanganan traktat perdamaian resmi pertama antara negara Arab (Mesir) dengan Israel, di mana Israel setuju mengembalikan seluruh Semenanjung Sinai kepada Mesir dan Mesir secara resmi mengakui kedaulatan negara Israel serta membuka Terusan Suez bagi kapal Israel.",
        "distractors": [
            "Pemberian mandat penuh kepada tentara Mesir untuk menduduki seluruh kota pelabuhan Tel Aviv.",
            "Pembentukan sistem mata uang bersama dinar-shekel untuk seluruh transaksi perdagangan di Laut Mati.",
            "Penyatuan angkatan udara kedua negara untuk bersama-sama melancarkan serangan terhadap imperium Turki.",
            "Penghapusan seluruh perbatasan internasional dan penyerahan tanah Palestina kepada komisi perlindungan PBB."
        ],
        "formula": {
            "title": "POKOK PERSETUJUAN CAMP DAVID (1978/1979)",
            "latex": "\\text{Camp David (Sadat + Begin)} \\implies \\begin{cases} \\mathbf{\\text{Semenanjung Sinai Dikembalikan ke Mesir}} \\\\ \\mathbf{\\text{Mesir Jadi Negara Arab Pertama yang Mengakui Kedaulatan Israel}} \\\\ \\text{Pemberian Hadiah Nobel Perdamaian 1978 kepada Sadat & Begin} \\end{cases}",
            "legend": "• Mengakibatkan Mesir dikucilkan oleh negara-negara Arab dan terbunuhnya Anwar Sadat pada 1981"
        },
        "hints": {
            "concept": "Camp David 1978 adalah perjanjian damai pertama negara Arab (Mesir) dengan Israel: Sinai dikembalikan ke Mesir dan Mesir mengakui kedaulatan Israel.",
            "execution": "Pilih: Traktat damai pertama negara Arab (Mesir) dengan Israel: Sinai dikembalikan dan Mesir mengakui kedaulatan Israel."
        }
    },
    {
        "id": "sejl-sim-21",
        "materi": "SEJARAH DUNIA: HAK ASASI MANUSIA",
        "topic": "Deklarasi Universal Hak Asasi Manusia (UDHR) PBB 1948",
        "stem": "Majelis Umum Perserikatan Bangsa-Bangsa mengesahkan Deklarasi Universal Hak Asasi Manusia (_Universal Declaration of Human Rights_ / UDHR) di Paris pada 10 Desember 1948 di bawah kepemimpinan Eleanor Roosevelt. Latar belakang historis mendalam yang mendorong komunitas internasional melahirkan instrumen HAM universal tersebut adalah...",
        "correct": "Refleksi moral dan trauma mendalam atas kejahatan kemanusiaan luar biasa, genosida Holokaus, dan penindasan fasisme brutal yang melanda dunia selama Perang Dunia II, sehingga diperlukan standar etik global perlindungan martabat kemanusiaan.",
        "distractors": [
            "Keinginan mendirikan satu agama tunggal dunia yang diwajibkan bagi seluruh bangsa tanpa terkecuali.",
            "Tuntutan serikat pekerja tambang emas di Afrika Selatan agar seluruh tambang dinasionalisasi oleh PBB.",
            "Kesepakatan pembagian zona penangkapan ikan paus di Samudra Arktik bagi negara-negara industri.",
            "Perintah penarikan seluruh buku undang-undang pidana nasional dan penggantiannya dengan piagam kerajaan Inggris."
        ],
        "formula": {
            "title": "LANDASAN MORAL UDHR (10 DESEMBER 1948)",
            "latex": "\\Delta \\text{Etika Global} = \\underbrace{\\text{Trauma Perang Dunia II (Genosida Holokaus, Fasisme, Kejahatan Perang)}}_{\\text{Pelanggaran Martabat Manusia Terburuk}} \\longrightarrow \\mathbf{\\text{Deklarasi Universal HAM 1948 (30 Pasal)}}",
            "legend": "• Diperingati sebagai Hari Hak Asasi Manusia Sedunia setiap tanggal 10 Desember"
        },
        "hints": {
            "concept": "UDHR 1948 dirumuskan PBB sebagai tanggapan atas kengerian dan genosida Perang Dunia II agar martabat manusia memiliki payung perlindungan universal.",
            "execution": "Pilih opsi refleksi trauma atas genosida Holokaus dan penindasan fasisme selama Perang Dunia II."
        }
    },
    {
        "id": "sejl-sim-22",
        "materi": "SEJARAH EKONOMI DUNIA",
        "topic": "Krisis Ekonomi Malaise 1929 & Runtuhnya Industri Gula Hindia Belanda",
        "stem": "Krisis keuangan global yang dikenal sebagai 'The Great Depression' (Zaman Malaise) meletus pasca-jatuhnya bursa saham Wall Street New York pada Oktober 1929 (_Black Tuesday_). Dampak destruktif yang dialami perekonomian Hindia Belanda di sektor perkebunan akibat krisis Malaise tersebut adalah...",
        "correct": "Kolapsnya industri gula pasir Jawa akibat anjloknya harga komoditas ekspor gula di pasar dunia dan penutupan pasar tujuan ekspor internasional, yang memaksa penutupan puluhan pabrik gula dan pemutusan hubungan kerja massal bagi ratusan ribu buruh tani.",
        "distractors": [
            "Pemberian pinjaman uang emas tanpa bunga oleh pemerintah kolonial kepada seluruh keluarga buruh tani miskin.",
            "Peningkatan volume ekspor kopi dan teh hingga sepuluh kali lipat ke pasar negara-negara Eropa Timur.",
            "Penyitaan seluruh tanah perkebunan swasta oleh para sultan tradisional untuk dibagikan secara gratis.",
            "Pengalihan seluruh mata uang gulden menjadi mata uang peso perak dalam perdagangan pasar lokal."
        ],
        "formula": {
            "title": "IMPAK MALAISE 1929 TERHADAP EKONOMI KOLONIAL",
            "latex": "\\text{Black Tuesday Wall Street (1929)} \\implies \\begin{cases} \\mathbf{\\text{Permintaan Dunia Anjlok:}} & \\text{Gula pasir Jawa (komoditas primadona) kehilangan pasar} \\\\ \\mathbf{\\text{Chadbourne Agreement (1931):}} & \\text{Pembatasan kuota produksi gula global} \\\\ \\mathbf{\\text{Dampak Sosial di Jawa:}} & \\text{Pabrik gula tutup, upah kuli anjlok drastis, kelaparan} \\end{cases}",
            "legend": "• Mengakhiri masa keemasan Hindia Belanda sebagai eksportir gula terbesar kedua di dunia setelah Kuba"
        },
        "hints": {
            "concept": "Zaman Malaise 1929 menghancurkan industri gula Jawa: harga dunia anjlok, ekspor terhenti, pabrik gula gulung tikar, dan kemiskinan merajalela.",
            "execution": "Pilih: Kolapsnya industri gula Jawa akibat anjloknya harga ekspor dunia, penutupan pabrik gula, dan PHK massal."
        }
    },
    {
        "id": "sejl-sim-23",
        "materi": "HISTORIOGRAFI INDONESIA",
        "topic": "Pendekatan Sejarah Kritis & Konsep Kausalitas Multidimensional",
        "stem": "Seorang sejarawan kontemporer mengkaji pecahnya Perang Diponegoro (1825–1830). Alih-alih hanya berfokus pada insiden pematokan tanah makam leluhur Diponegoro di Tegalrejo oleh Residen Smissaert, peneliti tersebut menganalisis tekanan sistem sewa tanah, beban pajak kolonial yang mencekik (_pajak bekti, pintu gerbang, kepala_), serta kekecewaan bangsawan kraton Yogyakarta. Cara pandang analitis ini mencerminkan prinsip sejarah kritis berupa...",
        "correct": "Membedakan antara sebab pemicu langsung (_trigger/casus belli_) dengan sebab-sebab struktural mendalam (_underlying factors_) dalam rangka menyusun eksplanasi kausalitas multikausal.",
        "distractors": [
            "Menolak seluruh fakta empiris di lapangan dan menggantinya dengan ramalan mistik jangka jayabaya.",
            "Mengharuskan penulisan sejarah murni menggunakan bahasa Belanda kuno agar terlihat otentik.",
            "Menghilangkan nama tokoh-tokoh pahlawan daerah dari narasi demi menjaga persatuan politik.",
            "Memandang bahwa setiap peperangan masa lalu selalu digerakkan oleh konspirasi tunggal agen rahasia."
        ],
        "formula": {
            "title": "DIKOTOMI SEBAB LANGSUNG VS SEBAB STRUKTURAL",
            "latex": "\\text{Kausalitas Sejarah} = \\underbrace{\\mathbf{\\text{Sebab Pemicu (Casus Belli)}}}_{\\text{Patok tanah makam di Tegalrejo}} + \\underbrace{\\mathbf{\\text{Sebab Struktural (Underlying Causes)}}}_{\\text{Beban pajak, krisis agraria, intervensi kraton}}",
            "legend": "• Menghindari jebakan reduksionisme monokausal dalam metodologi sejarah modern"
        },
        "hints": {
            "concept": "Pematokan tanah Tegalrejo adalah pemicu langsung (casus belli), sedangkan beban pajak dan masalah agraria adalah faktor struktural mendalam (multikausal).",
            "execution": "Pilih: Membedakan sebab pemicu langsung (casus belli) dengan sebab struktural mendalam dalam kausalitas multikausal."
        }
    },
    {
        "id": "sejl-sim-24",
        "materi": "PERADABAN ISLAM NUSANTARA",
        "topic": "Peranan Wali Sanga & Pendekatan Akulturasi Budaya Sunan Kalijaga",
        "stem": "Dalam proses penyebaran dakwah Islam di tanah Jawa pada abad XV–XVI, para Wali Sanga menerapkan pendekatan persuasif kultural tanpa kekerasan. Salah satu manifestasi paling termasyhur dari strategi akulturasi kultural Sunan Kalijaga adalah...",
        "correct": "Memanfaatkan kesenian wayang kulit purwa dan gending gamelan Jawa (seperti tembang Ilir-Ilir dan Dandanggula) yang disisipi nilai-nilai tauhid dan ajaran Islam, serta tradisi Grebeg Maulud (Sekaten).",
        "distractors": [
            "Menghancurkan seluruh kompleks bangunan berarsitektur joglo dan mewajibkan pembangunan kubah bergaya Persia.",
            "Melarang seluruh masyarakat menyantap makanan tradisional dan mewajibkan impor buah kurma dari jazirah Arab.",
            "Mengganti seluruh sistem hukum pidana adat dengan hukum perdata maritim kerajaan Romawi kuno.",
            "Mengharuskan seluruh penduduk mengubah nama keluarga mereka ke dalam bahasa Yunani klasik."
        ],
        "formula": {
            "title": "STRATEGI DAKWAH KULTURAL SUNAN KALIJAGA",
            "latex": "\\text{Dakwah Kultural} = \\underbrace{\\text{Bentuk/Wadah Kesenian Tradisi (Wayang, Gamelan, Sekaten)}}_{\\text{Diterima Akrab oleh Rakyat}} + \\underbrace{\\mathbf{\\text{Substansi Nilai Ajaran Tauhid/Fikih Islam}}}_{\\mathbf{\\text{Transformasi Religius Tanpa Gejolak}}}",
            "legend": "• Sunan Kalijaga menciptakan karakter wayang Semar, Petruk, Gareng, Bagong sebagai alegori dakwah"
        },
        "hints": {
            "concept": "Sunan Kalijaga terkenal dengan dakwah kultural: memanfaatkan media wayang kulit, tembang gamelan (Ilir-Ilir), dan Sekaten sebagai sarana dakwah.",
            "execution": "Pilih opsi pemanfaatan kesenian wayang kulit, tembang gending gamelan, dan perayaan Sekaten bermuatan nilai tauhid."
        }
    },
    {
        "id": "sejl-sim-25",
        "materi": "HISTORIOGRAFI NASIONAL",
        "topic": "Deklarasi Kemerdekaan & Legitimasi Hukum Internasional",
        "stem": "Pada tanggal 17 Agustus 1945, proklamasi kemerdekaan Republik Indonesia dinyatakan secara sepihak (_unilateral declaration of independence_). Menurut perspektif hukum tata negara dan sejarah diplomasi, syarat konstitutif dan deklaratif yang segera dipenuhi oleh para pendiri bangsa dalam sidang PPKI 18–19 Agustus 1945 untuk mengukuhkan status Indonesia sebagai negara berdaulat adalah...",
        "correct": "Menetapkan UUD 1945 sebagai hukum dasar konstitusi, memilih Presiden dan Wakil Presiden, membagi wilayah administratif ke dalam 8 provinsi, serta membentuk Komite Nasional Indonesia Pusat (KNIP) dan Badan Keamanan Rakyat.",
        "distractors": [
            "Menerbitkan sertifikat kepemilikan saham pada seluruh bursa efek perbankan internasional di kota London.",
            "Meminta persetujuan resmi dari seluruh gubernur jenderal koloni wilayah Pasifik di bawah kekuasaan Inggris.",
            "Menyewa pulau terluar di Samudra Hindia untuk dijadikan pangkalan armada perang kapal selam asing.",
            "Menghapuskan seluruh sistem perpajakan daerah dan membebaskan bea masuk bagi produk impor luar negeri."
        ],
        "formula": {
            "title": "UNSUR NEGARA BERDAULAT (KONVENSI MONTEVIDEO 1933)",
            "latex": "\\text{Syarat Negara} = \\begin{cases} \\mathbf{\\text{Konstitutif:}} & \\text{Wilayah (8 Provinsi), Rakyat (Bangsa Indonesia), Pemerintah Berdaulat (Presiden/Wapres/UUD)} \\\\ \\mathbf{\\text{Deklaratif:}} & \\text{Pengakuan Negara Lain (Mesir, India, Suriah, dll)} \\end{cases}",
            "legend": "• Sidang PPKI 18-19 Agustus 1945 meletakkan fondasi hukum ketatanegaraan pertama RI"
        },
        "hints": {
            "concept": "Sidang PPKI 18-19 Agustus memenuhi syarat berdirinya negara: mengesahkan UUD 1945, memilih Presiden-Wapres, menetapkan 8 provinsi, dan membentuk KNIP.",
            "execution": "Pilih: Menetapkan UUD 1945, memilih Presiden dan Wakil Presiden, membagi 8 provinsi, serta membentuk KNIP dan BKR."
        }
    },

    # -------------------------------------------------------------
    # 5 MULTI-SELECT ITEMS (sejl-sim-26 .. sejl-sim-30)
    # -------------------------------------------------------------
    {
        "id": "sejl-sim-26",
        "materi": "METODOLOGI RISET SEJARAH",
        "topic": "Empat Tahapan Baku Penelitian Sejarah Kritis",
        "stem": "Dalam metodologi penelitian sejarah ilmiah, sejarawan wajib menempuh serangkaian prosedur baku yang ketat untuk mengonstruksi masa lalu secara objektif. Manakah di antara pernyataan-pernyataan berikut yang secara tepat menggambarkan tahapan-tahapan riset sejarah tersebut? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Heuristik merupakan tahapan melacak, mencari, dan mengumpulkan jejak-jejak masa lalu atau sumber sejarah yang relevan dengan topik penelitian."},
            {"key": "B", "text": "Kritik ekstern berfokus pada pengujian otentisitas fisik dokumen seperti usia kertas, keaslian tinta, gaya tulisan, dan stempel."},
            {"key": "C", "text": "Historiografi merupakan proses penulisan kembali laporan sejarah secara sistematis dan analitis berdasarkan fakta-fakta yang telah diinterpretasikan."},
            {"key": "D", "text": "Interpretasi merupakan tahapan menghafal tanggal-tanggal peristiwa masa lalu tanpa perlu memberikan analisis eksplanasi sebab-akibat."},
            {"key": "E", "text": "Kritik intern bertujuan menolak seluruh kesaksian para pelaku sejarah yang berasal dari golongan rakyat jelata."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "EMPAT TAHAP RISET SEJARAH ILMIAH",
            "latex": "\\text{Metodologi Riset} \\equiv \\mathbf{\\text{Heuristik (A)}} \\longrightarrow \\mathbf{\\text{Verifikasi/Kritik (B)}} \\longrightarrow \\text{Interpretasi} \\longrightarrow \\mathbf{\\text{Historiografi (C)}}",
            "legend": "• Heuristik: Pelacakan sumber<br>• Kritik: Pengujian keaslian (ekstern) & kebenaran isi (intern)<br>• Historiografi: Sintesis penulisan sejarah"
        },
        "hints": {
            "concept": "Tahapan riset sejarah: 1. Heuristik (mencari sumber), 2. Kritik/Verifikasi ekstern & intern, 3. Interpretasi, 4. Historiografi (penulisan). D dan E salah.",
            "execution": "Pilih opsi A, B, dan C."
        }
    },
    {
        "id": "sejl-sim-27",
        "materi": "PROKLAMASI & PEMBENTUKAN NEGARA",
        "topic": "Keputusan Fundamental Sidang PPKI 18-19 Agustus 1945",
        "stem": "Sidang Panitia Persiapan Kemerdekaan Indonesia (PPKI) yang diselenggarakan pada tanggal 18 dan 19 Agustus 1945 berhasil meletakkan pilar-pilar dasar ketatanegaraan Republik Indonesia yang baru merdeka. Manakah dari keputusan-keputusan berikut yang merupakan hasil resmi sidang PPKI tersebut? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Mengesahkan Undang-Undang Dasar Negara Republik Indonesia (UUD 1945) beserta Pembukaannya."},
            {"key": "B", "text": "Memilih dan menetapkan Ir. Soekarno sebagai Presiden dan Drs. Mohammad Hatta sebagai Wakil Presiden RI."},
            {"key": "C", "text": "Membagi wilayah kedaulatan Republik Indonesia ke dalam delapan provinsi serta merancang pembentukan dua belas kementerian departemen."},
            {"key": "D", "text": "Membubarkan seluruh laskar pemuda bersenjata dan melarang penggunaan mata uang rupiah di pasar komersial."},
            {"key": "E", "text": "Menyetujui pembentukan negara monarki federal serikat di bawah naungan persemakmuran mahkota kerajaan Belanda."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "KEPUTUSAN KUNCI PPKI (18-19 AGUSTUS 1945)",
            "latex": "\\text{Hasil PPKI} = \\begin{cases} \\mathbf{\\text{18 Agt:}} & \\mathbf{\\text{Pengesahan UUD 1945 (A), Pemilihan Soekarno-Hatta (B), Tugas Presiden dibantu Komite}} \\\\ \\mathbf{\\text{19 Agt:}} & \\mathbf{\\text{Pembagian 8 Provinsi (C), Pembentukan 12 Kementerian, Komite Nasional Daerah}} \\end{cases}",
            "legend": "• Delapan Provinsi Perdana: Sumatera, Jawa Barat, Jawa Tengah, Jawa Timur, Sunda Kecil, Maluku, Sulawesi, Kalimantan"
        },
        "hints": {
            "concept": "Sidang PPKI 18-19 Agustus menghasilkan: pengesahan UUD 1945, pemilihan Soekarno-Hatta, dan pembagian 8 provinsi serta 12 departemen. D dan E salah.",
            "execution": "Pilih opsi A, B, dan C."
        }
    },
    {
        "id": "sejl-sim-28",
        "materi": "PERJUANGAN DIPLOMASI KEMERDEKAAN",
        "topic": "Tokoh Negarawan Diplomat Indonesia Era Revolusi (1945-1949)",
        "stem": "Dalam mempertahankan kemerdekaan menghadapi agresi militer Belanda, Indonesia menempuh strategi diplomasi internasional yang dipimpin oleh para tokoh diplomat ulung. Manakah pasangan tokoh dengan peran diplomasi bersejarah berikut yang benar? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Sutan Sjahrir memimpin delegasi Indonesia dalam Perundingan Linggarjati 1946–1947 serta berpidato memukau di hadapan Dewan Keamanan PBB di Lake Success."},
            {"key": "B", "text": "Amir Sjarifuddin bertindak sebagai ketua delegasi Republik Indonesia dalam Perundingan Renville di atas kapal USS Renville pada akhir 1947 hingga Januari 1948."},
            {"key": "C", "text": "Drs. Mohammad Hatta memimpin delegasi Republik Indonesia dalam Konferensi Meja Bundar (KMB) di Den Haag tahun 1949 yang menghasilkan penyerahan kedaulatan."},
            {"key": "D", "text": "Mr. Kasman Singodimedjo menandatangani persetujuan pembubaran Tentara Nasional Indonesia di markas besar komando AFNEI."},
            {"key": "E", "text": "dr. Soetomo memimpin perundingan penyerahan wilayah Irian Barat kepada perwakilan komisi jasa baik di Jenewa Swiss."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "TRIO DIPLOMAT KUNCI REVOLUSI (1946-1949)",
            "latex": "\\begin{cases} \\mathbf{\\text{Sutan Sjahrir (A):}} & \\text{Linggarjati (1946) & Pidato Gemilang di PBB Lake Success (1947)} \\\\ \\mathbf{\\text{Amir Sjarifuddin (B):}} & \\text{Renville (1947-1948)} \\\\ \\mathbf{\\text{Mohammad Hatta (C):}} & \\text{Konferensi Meja Bundar Den Haag (1949)} \\end{cases}",
            "legend": "• Berhasil membawa kemerdekaan Indonesia diakui secara de jure oleh masyarakat internasional"
        },
        "hints": {
            "concept": "Sjahrir memimpin Linggarjati & forum PBB (A), Amir Sjarifuddin memimpin Renville (B), dan Hatta memimpin KMB (C). D dan E salah.",
            "execution": "Pilih opsi A, B, dan C."
        }
    },
    {
        "id": "sejl-sim-29",
        "materi": "DEMOKRASI PARLEMENTER (1950-1959)",
        "topic": "Empat Partai Pemenang Pemilu Pertama Tahun 1955",
        "stem": "Pemilihan Umum pertama tahun 1955 berlangsung dengan partisipasi rakyat yang sangat tinggi (mencapai lebih dari 90%) dalam suasana yang jujur, aman, dan demokratis. Manakah di antara partai-partai politik berikut yang berhasil menduduki posisi 'Empat Besar' pemenang suara terbanyak dalam Pemilu 1955? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Partai Nasional Indonesia (PNI) yang memperoleh 57 kursi di parlemen dewan perwakilan rakyat."},
            {"key": "B", "text": "Masyumi (Majelis Syuro Muslimin Indonesia) yang memperoleh 57 kursi di parlemen."},
            {"key": "C", "text": "Nahdlatul Ulama (NU) yang tampil sebagai kekuatan politik Islam tradisionalis dengan perolehan 45 kursi."},
            {"key": "D", "text": "Partai Golongan Karya (Golkar) yang memenangkan mayoritas mutlak 80% kursi parlemen."},
            {"key": "E", "text": "Partai Demokrat Rakyat Baru yang didirikan oleh para pengusaha perkebunan swasta Belanda."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "EMPAT BESAR PARTAI PEMENANG PEMILU 1955",
            "latex": "\\text{Empat Besar 1955} \\implies \\begin{cases} \\mathbf{\\text{1. PNI:}} & \\mathbf{\\text{8,4 juta suara (57 kursi)}} \\\\ \\mathbf{\\text{2. Masyumi:}} & \\mathbf{\\text{7,9 juta suara (57 kursi)}} \\\\ \\mathbf{\\text{3. NU:}} & \\mathbf{\\text{6,9 juta suara (45 kursi)}} \\\\ \\mathbf{\\text{4. PKI:}} & \\text{6,1 juta suara (39 kursi)} \\end{cases}",
            "legend": "• Menunjukkan peta sosiologis aliran politik Indonesia: Nasionalis, Islam Modernis, Islam Tradisionalis, dan Komunis"
        },
        "hints": {
            "concept": "Empat partai besar pemenang Pemilu 1955 adalah PNI, Masyumi, NU, dan PKI. Golkar (D) baru berdiri era Orba. E adalah organisasi fiktif.",
            "execution": "Pilih opsi A (PNI), B (Masyumi), dan C (Nahdlatul Ulama)."
        }
    },
    {
        "id": "sejl-sim-30",
        "materi": "GERAKAN REFORMASI 1998",
        "topic": "Agenda Enam Tuntutan Pokok Gerakan Reformasi Mahasiswa 1998",
        "stem": "Gerakan mahasiswa Indonesia tahun 1998 merumuskan 'Enam Tuntutan Reformasi' sebagai agenda mendesak untuk membongkar tatanan korup dan otoriter rezim Orde Baru. Manakah di antara poin-poin berikut yang termasuk ke dalam Enam Tuntutan Pokok Reformasi 1998? (Pilih TIGA jawaban yang benar)",
        "options": [
            {"key": "A", "text": "Adili Soeharto dan kroni-kroninya serta usut tuntas harta kekayaan hasil korupsi, kolusi, dan nepotisme (KKN)."},
            {"key": "B", "text": "Lakukan amandemen terhadap Undang-Undang Dasar 1945 guna membatasi kekuasaan presiden yang berlebihan."},
            {"key": "C", "text": "Hapuskan Dwi Fungsi ABRI dari ranah politik dan pemerintahan agar militer kembali profesional pada fungsi pertahanan negara."},
            {"key": "D", "text": "Bubarkan seluruh universitas dan perguruan tinggi swasta di seluruh wilayah ibu kota Jakarta."},
            {"key": "E", "text": "Wajibkan seluruh warga negara menjadi anggota partai politik tunggal bentukan dewan pimpinan militer."}
        ],
        "correctKeys": ["A", "B", "C"],
        "formula": {
            "title": "ENAM TUNTUTAN REFORMASI 1998",
            "latex": "\\text{Agenda Reformasi} \\iff \\begin{cases} \\mathbf{\\text{1. Adili Soeharto & Kroninya (A)}} \\\\ \\mathbf{\\text{2. Amandemen UUD 1945 (B)}} \\\\ \\mathbf{\\text{3. Penghapusan Dwi Fungsi ABRI (C)}} \\\\ \\text{4. Pelaksanaan Otonomi Daerah Seluas-luasnya} \\\\ \\text{5. Penegakan Supremasi Hukum & HAM} \\\\ \\text{6. Pembentukan Pemerintahan Bersih Bebas KKN} \\end{cases}",
            "legend": "• Menjadi kompas haluan transformasi ketatanegaraan Indonesia pasca-runtuhnya Orde Baru"
        },
        "hints": {
            "concept": "Tuntutan Reformasi 1998: 1. Adili Soeharto & kroni, 2. Amandemen UUD 1945, 3. Hapus Dwi Fungsi ABRI, 4. Otonomi daerah, 5. Supremasi hukum, 6. Bebas KKN. D dan E salah.",
            "execution": "Pilih opsi A, B, dan C."
        }
    },

    # -------------------------------------------------------------
    # 5 MATRIX BENAR-SALAH ITEMS (sejl-sim-31 .. sejl-sim-35)
    # -------------------------------------------------------------
    {
        "id": "sejl-sim-31",
        "materi": "PERADABAN KUNO & KERAJAAN MARITIM",
        "topic": "Evaluasi Fakta Sejarah Kerajaan Hindu-Buddha di Nusantara",
        "stem": "Berikut adalah pernyataan mengenai dinamika sejarah dan peninggalan peradaban kerajaan-kerajaan Hindu-Buddha di Nusantara. Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan!",
        "statements": [
            {
                "text": "Prasasti Kedukan Bukit (682 M) mencatat perjalanan suci (siddhayatra) Dapunta Hyang membawa 20.000 tentara yang menjadi bukti awal berdirinya Kemaharajaan Sriwijaya.",
                "correct": "Benar"
            },
            {
                "text": "Candi Borobudur dibangun pada masa pemerintahan Dinasti Sanjaya yang beraliran Hindu Siwa murni sebagai tempat penyimpanan abu jenazah raja.",
                "correct": "Salah"
            },
            {
                "text": "Raja Kertanegara dari Singasari mengirim Ekspedisi Pamalayu (1275 M) untuk menjalin persekutuan maritim di Selat Malaka guna membendung ancaman ekspansi bala tentara Mongol Dinasti Yuan.",
                "correct": "Benar"
            },
            {
                "text": "Kitab Sutasoma yang memuat semboyan kebangsaan 'Bhinneka Tunggal Ika' ditulis oleh Mpu Prapanca pada masa kejayaan Kerajaan Kediri.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI HISTORIS KERAJAAN HINDU-BUDDHA",
            "latex": "\\begin{aligned} \\text{Borobudur: } & \\mathbf{\\text{Wangsa Syailendra (Buddha Mahayana)}}, \\text{ bukan Sanjaya (Hindu)} \\\\ \\text{Sutasoma: } & \\mathbf{\\text{Karya Mpu Tantular era Majapahit}}, \\text{ bukan Mpu Prapanca / Kediri} \\end{aligned}",
            "legend": "• Ekspedisi Pamalayu: Kertanegara membendung Kubilai Khan<br>• Kedukan Bukit: Bukti epigrafis tertua imperium maritim Sriwijaya"
        },
        "hints": {
            "concept": "Pernyataan 1 Benar (Kedukan Bukit Dapunta Hyang). Pernyataan 2 Salah (Borobudur dibangun Syailendra/Buddha, bukan Sanjaya/Hindu). Pernyataan 3 Benar (Pamalayu hadapi Mongol). Pernyataan 4 Salah (Sutasoma karya Mpu Tantular di Majapahit, bukan Prapanca di Kediri).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "sejl-sim-32",
        "materi": "ERA KOLONIALISME HINDIA BELANDA",
        "topic": "Evaluasi Kebijakan Kolonial VOC hingga Politik Etis",
        "stem": "Tentukan status kebenaran (BENAR / SALAH) dari pernyataan-pernyataan di bawah ini terkait kebijakan pemerintah kolonial di Indonesia!",
        "statements": [
            {
                "text": "Hak Ekstirpasi yang diterapkan VOC adalah hak untuk menebang dan memusnahkan pohon pala dan cengkih guna menjaga kestabilan harga rempah di pasar dunia.",
                "correct": "Benar"
            },
            {
                "text": "Kebijakan Landrent System (Sewa Tanah) yang diterapkan Thomas Stamford Raffles berhasil menyejahterakan rakyat Jawa karena menghapus seluruh sistem perpajakan desa.",
                "correct": "Salah"
            },
            {
                "text": "Buku novel Max Havelaar yang membongkar penderitaan rakyat Lebak Banten akibat pemerasan sistem tanam paksa ditulis oleh Eduard Douwes Dekker dengan nama pena Multatuli.",
                "correct": "Benar"
            },
            {
                "text": "Kebijakan Politik Etis dirancang dan didanai penuh oleh perserikatan buruh sosialis pribumi tanpa campur tangan ratu kerajaan Belanda.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "ANALISIS KEBIJAKAN KOLONIAL",
            "latex": "\\begin{aligned} \\text{Ekstirpasi: } & \\text{Benar (Pemusnahan pohon rempah untuk kontrol suplai monopoli VOC)} \\\\ \\text{Landrent Raffles: } & \\text{Salah (Gagal karena birokrasi korup, rakyat belum paham ekonomi uang)} \\\\ \\text{Max Havelaar: } & \\text{Benar (Karya Multatuli mengguncang parlemen Belanda 1860)} \\\\ \\text{Politik Etis: } & \\text{Salah (Dicanangkan Ratu Wilhelmina dalam pidato takhta 1901)} \\end{aligned}",
            "legend": "• Menunjukkan dinamika kritik kemanusiaan terhadap eksploitasi kolonial di Hindia Belanda"
        },
        "hints": {
            "concept": "1=Benar (Ekstirpasi tebang pohon rempah). 2=Salah (Landrent Raffles gagal dan tetap membebani rakyat dengan sewa tanah). 3=Benar (Max Havelaar karya Multatuli). 4=Salah (Politik Etis dicanangkan Ratu Wilhelmina atas usul van Deventer).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "sejl-sim-33",
        "materi": "REVOLUSI KEMERDEKAAN (1945-1949)",
        "topic": "Evaluasi Peristiwa Perjuangan Fisik & Diplomasi Revolusi RI",
        "stem": "Berikut disajikan pernyataan mengenai peristiwa-peristiwa penting pada masa Revolusi Kemerdekaan Indonesia (1945–1949). Tentukan apakah masing-masing pernyataan BENAR atau SALAH!",
        "statements": [
            {
                "text": "Perjanjian Roem-Roijen (Mei 1949) menghasilkan kesepakatan kembalinya pemerintah Republik Indonesia ke ibu kota Yogyakarta dan penghentian perang gerilya.",
                "correct": "Benar"
            },
            {
                "text": "Agresi Militer Belanda I dilancarkan oleh Belanda pada 21 Juli 1947 sebagai bentuk ketaatan terhadap butir-butir traktat Perundingan Linggarjati.",
                "correct": "Salah"
            },
            {
                "text": "Komisi Tiga Negara (KTN) yang dibentuk PBB terdiri atas Australia (pilihan Indonesia), Belgia (pilihan Belanda), dan Amerika Serikat (penengah netral).",
                "correct": "Benar"
            },
            {
                "text": "Konferensi Meja Bundar (KMB) menetapkan bahwa status wilayah Irian Barat langsung menjadi bagian mutlak RIS pada hari penyerahan kedaulatan 27 Desember 1949.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "KRONOLOGI DIPLOMASI REVOLUSI (1947-1949)",
            "latex": "\\begin{aligned} \\text{Roem-Roijen: } & \\text{Benar (Moh. Roem & Van Roijen: Soekarno-Hatta kembali ke Yogya)} \\\\ \\text{Agresi I: } & \\text{Salah (Belanda melanggar sepihak Perjanjian Linggarjati)} \\\\ \\text{KTN: } & \\text{Benar (Australia, Belgia, AS memediasi Renville)} \\\\ \\text{Irian Barat KMB: } & \\text{Salah (Statusnya ditunda dan dirundingkan dalam 1 tahun)} \\end{aligned}",
            "legend": "• Menunjukkan jalan panjang kombinasi diplomasi dan perjuangan senjata menegakkan kedaulatan"
        },
        "hints": {
            "concept": "1=Benar (Roem-Roijen pulihkan Yogya). 2=Salah (Agresi I adalah pengkhianatan sepihak Belanda atas Linggarjati). 3=Benar (Anggota KTN: Australia, Belgia, AS). 4=Salah (KMB menunda status Irian Barat selama satu tahun).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    },
    {
        "id": "sejl-sim-34",
        "materi": "DEMOKRASI TERPIMPIN (1959-1965)",
        "topic": "Evaluasi Kebijakan & Peristiwa Era Demokrasi Terpimpin",
        "stem": "Tentukan kategori BENAR atau SALAH untuk setiap pernyataan terkait dinamika politik dan ekonomi era Demokrasi Terpimpin di bawah pimpinan Presiden Soekarno!",
        "statements": [
            {
                "text": "Manipol-USDEK yang ditetapkan sebagai Garis-Garis Besar Haluan Negara bersumber dari pidato kepresidenan Soekarno berjudul 'Penemuan Kembali Revolusi Kita' pada 17 Agustus 1959.",
                "correct": "Benar"
            },
            {
                "text": "Presiden Soekarno membubarkan DPR hasil Pemilu 1955 pada tahun 1960 karena DPR menolak menyetujui Rancangan Anggaran Pendapatan dan Belanja Negara (RAPBN) yang diajukan pemerintah.",
                "correct": "Benar"
            },
            {
                "text": "Politik Mercusuar era Demokrasi Terpimpin berhasil menghentikan inflasi dan menjadikan rupiah mata uang paling bernilai tinggi di kawasan Asia Tenggara.",
                "correct": "Salah"
            },
            {
                "text": "Operasi Senopati adalah operasi militer pimpinan Angkatan Darat yang berhasil membebaskan Sabah dan Sarawak dari cengkeraman federasi Malaysia.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "DINAMIKA DEMOKRASI TERPIMPIN (1959-1965)",
            "latex": "\\begin{aligned} \\text{Manipol USDEK: } & \\text{Benar (UUD 45, Sosialisme Ind, Demokrasi Terpimpin, Ekonomi Terpimpin, Kepribadian Ind)} \\\\ \\text{Pembubaran DPR 1960: } & \\text{Benar (DPR tolak RAPBN, diganti DPR-Gotong Royong)} \\\\ \\text{Ekonomi Mercusuar: } & \\text{Salah (Proyek boros memicu hiperinflasi 650\\%)} \\\\ \\text{Operasi Dwikora: } & \\text{Salah (Sabah-Sarawak tetap bergabung ke Malaysia)} \\end{aligned}",
            "legend": "• Menunjukkan sentralisasi kekuasaan ekstrem dan krisis ekonomi moneter di ujung rezim Orde Lama"
        },
        "hints": {
            "concept": "1=Benar (Manipol USDEK dari pidato 17 Agt 1959). 2=Benar (DPR dibubarkan karena tolak RAPBN 1960). 3=Salah (Politik Mercusuar malah memicu hiperinflasi 650%). 4=Salah (Sabah dan Sarawak tidak berhasil dibebaskan).",
            "execution": "Tentukan: 1=Benar, 2=Benar, 3=Salah, 4=Salah."
        }
    },
    {
        "id": "sejl-sim-35",
        "materi": "SEJARAH DUNIA: PERANG DINGIN",
        "topic": "Evaluasi Fakta Sejarah Perang Dingin & Hubungan Internasional",
        "stem": "Berikut adalah pernyataan mengenai dinamika geopolitik Perang Dingin global antara Blok Barat (Amerika Serikat) dan Blok Timur (Uni Soviet). Tentukan kategori BENAR atau SALAH untuk setiap butir pernyataan!",
        "statements": [
            {
                "text": "Runtuhnya Tembok Berlin pada 9 November 1989 menjadi simbol runtuhnya Tirai Besi komunisme di Eropa dan membuka jalan bagi reunifikasi negara Jerman.",
                "correct": "Benar"
            },
            {
                "text": "Blokade Berlin (1948–1949) oleh Uni Soviet berhasil memotong seluruh pasokan udara Sekutu hingga memaksa pasukan Amerika Serikat meninggalkan Eropa.",
                "correct": "Salah"
            },
            {
                "text": "Krisis Rudal Kuba 1962 dipicu oleh pemasangan instalasi peluncur rudal balistik nuklir berhulu ledak milik Uni Soviet di wilayah Kuba.",
                "correct": "Benar"
            },
            {
                "text": "Perang Vietnam berakhir pada tahun 1975 dengan kemenangan telak pihak Vietnam Selatan yang berhasil menaklukkan ibu kota Hanoi.",
                "correct": "Salah"
            }
        ],
        "formula": {
            "title": "EVALUASI PERISTIWA PERANG DINGIN",
            "latex": "\\begin{aligned} \\text{Tembok Berlin: } & \\text{Benar (Runtuh 9 Nov 1989, Reunifikasi Jerman 1990)} \\\\ \\text{Berlin Airlift: } & \\text{Salah (Sekutu berhasil mengirim bantuan lewat jembatan udara Berlin Airlift)} \\\\ \\text{Krisis Kuba: } & \\text{Benar (Rudal Soviet di Kuba mengancam daratan AS)} \\\\ \\text{Perang Vietnam: } & \\text{Salah (Saigon jatuh April 1975, Vietnam bersatu di bawah rezim komunis Utara)} \\end{aligned}",
            "legend": "• Menandai babak akhir pertarungan bipolar dua negara adidaya nuklir dunia"
        },
        "hints": {
            "concept": "1=Benar (Tembok Berlin runtuh 1989). 2=Salah (Sekutu berhasil mematahkan Blokade Berlin lewat operasi udara Berlin Airlift). 3=Benar (Krisis Kuba dipicu rudal Soviet di Kuba). 4=Salah (Vietnam Utara komunis yang menang dengan jatuhnya Saigon 1975).",
            "execution": "Tentukan: 1=Benar, 2=Salah, 3=Benar, 4=Salah."
        }
    }
]
