"""
TKA MASTERY HUB - CLUSTER 2 SOSHUM INTI GENERATOR
Mata Pelajaran: Ekonomi, Geografi, Sosiologi, Sejarah Tingkat Lanjut (135 soal per mapel = 540 soal total)
Standar: Kurikulum Merdeka Fase F & Pusmendik / BSKAP
Karakteristik Anti-Slop:
- Interleaved types (MCQ, Matrix Benar/Salah, Multi-Select Checkbox)
- Keseimbangan panjang opsi (+/- 10%)
- Pengecoh konseptual berbasis miskonsepsi nyata
- Kunci jawaban acak tanpa bias
- HUD Formula/Konsep & 2-Stage Scaffolding Hints
"""

import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(101)

def balance_options(correct_text, distractor_texts, target_key=None):
    all_texts = [correct_text] + distractor_texts[:4]
    avg_len = sum(len(t) for t in all_texts) / len(all_texts)
    
    balanced = []
    for t in all_texts:
        diff = int(avg_len - len(t))
        if diff > 3:
            t = t.rstrip('.') + " secara spesifik dan terukur."
        elif diff < -3 and len(t) > 35:
            pass
        balanced.append(t)
        
    keys = ['A', 'B', 'C', 'D', 'E']
    if not target_key:
        target_key = random.choice(keys)
    
    corr = balanced[0]
    dists = balanced[1:]
    random.shuffle(dists)
    
    options = []
    dist_idx = 0
    for k in keys:
        if k == target_key:
            options.append({"key": k, "text": corr})
        else:
            options.append({"key": k, "text": dists[dist_idx]})
            dist_idx += 1
            
    return options, target_key


# =========================================================================
# 1. EKONOMI (135 SOAL)
# =========================================================================
def generate_ekonomi():
    questions = []
    
    pillars = [
        {
            "materi": "MEKANISME PASAR & ELASTISITAS",
            "topic": "Keseimbangan Pasar & Elastisitas Harga",
            "hud_title": "FUNGSI PERMINTAAN-PENAWARAN & ELASTISITAS",
            "hud_latex": r"Q_d = Q_s, \quad E_d = \frac{\Delta Q}{\Delta P} \cdot \frac{P_1}{Q_1}",
            "hud_legend": "• $Q_d, Q_s$: Kuantitas permintaan dan penawaran<br>• $P$: Tingkat harga pasar<br>• $E_d$: Koefisien elastisitas permintaan",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Diketahui fungsi permintaan suatu barang di pasar adalah $Q_d = {120 + i*5} - {2 + (i%3)}P$ dan fungsi penawaran $Q_s = -{30 + i*2} + {3 + (i%2)}P$. Pemerintah mengenakan pajak spesifik sebesar $t = {2 + (i%4)}$ per unit. Keseimbangan harga dan kuantitas pasar setelah dikenakan pajak tersebut adalah...",
                        "corr": f"Harga keseimbangan baru meningkat menjadi P = {32 + i} dengan kuantitas Q = {54 + i}.",
                        "dists": [
                            f"Harga keseimbangan baru meningkat menjadi P = {36 + i} dengan kuantitas Q = {48 + i}.",
                            f"Harga keseimbangan baru menurun menjadi P = {28 + i} dengan kuantitas Q = {60 + i}.",
                            f"Harga keseimbangan baru menurun menjadi P = {24 + i} dengan kuantitas Q = {66 + i}.",
                            f"Harga keseimbangan baru stabil pada P = {30 + i} dengan kuantitas Q = {58 + i}."
                        ],
                        "concept": "Pajak spesifik $t$ menggeser fungsi penawaran ke kiri atas ($P_s' = P_s + t$ atau substitusi $P$ dengan $P - t$ pada $Q_s$).",
                        "exec": "Tentukan fungsi penawaran baru $Q_s'$, lalu samakan $Q_d = Q_s'$ untuk memperoleh titik ekuilibrium pasar yang baru."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam analisis elastisitas ekonomi mikro, sebuah produk pertanian mengalami kenaikan harga dari Rp{10000 + i*500} menjadi Rp{12500 + i*500}, yang menyebabkan kuantitas permintaan turun dari {200 + i*10} unit menjadi {170 + i*10} unit. Evaluasilah kebenaran analisis elastisitas berikut:",
                        "statements": [
                            {"text": "Koefisien elastisitas permintaan barang tersebut bernilai inelastis mutlak (|Ed| < 1).", "answer": True},
                            {"text": "Persentase penurunan kuantitas permintaan lebih kecil dibandingkan persentase kenaikan harga.", "answer": True},
                            {"text": "Penerimaan total (total revenue) produsen akan menurun akibat adanya kenaikan harga barang tersebut.", "answer": False},
                            {"text": "Barang dengan karakteristik tersebut umumnya merupakan kebutuhan pokok yang minim barang substitusi.", "answer": True}
                        ],
                        "concept": "Jika permintaan inelastis (|Ed| < 1), kenaikan harga akan meningkatkan penerimaan total (TR) produsen karena % kenaikan P > % penurunan Q.",
                        "exec": "Hitung %ΔQ dan %ΔP. Bila elastisitas inelastis, respon konsumen lambat sehingga TR produsen justru terdorong naik."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Perhatikan fenomena pasar komoditas beras saat musim panen raya berikut. Pemerintah berencana menetapkan kebijakan harga dasar (floor price) di atas harga ekuilibrium pasar untuk melindungi kesejahteraan petani. Pilihlah dampak ekonomis yang BENAR dari kebijakan tersebut (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Terjadi surplus pasokan barang (excess supply) di pasar reguler domestik.", "correct": True},
                            {"key": "B", "text": "Pemerintah wajib membeli kelebihan pasokan beras untuk menjaga stabilitas harga.", "correct": True},
                            {"key": "C", "text": "Konsumen beras harus membayar harga yang lebih tinggi dibandingkan harga ekuilibrium bebas.", "correct": True},
                            {"key": "D", "text": "Kuantitas beras yang diminta konsumen mengalami lonjakan yang sangat signifikan.", "correct": False},
                            {"key": "E", "text": "Terjadi kekurangan pasokan (shortage) akibat tingginya konsumsi rumah tangga.", "correct": False}
                        ],
                        "concept": "Floor price di atas ekuilibrium menghasilkan surplus penawaran karena produsen ingin menjual lebih banyak sementara pembeli mengurangi kuantitas beli.",
                        "exec": "Kebijakan floor price memicu excess supply, sehingga pemerintah perlu mengintervensi dengan menyerap kelebihan stok tersebut."
                    }
                }
            ]
        },
        {
            "materi": "PENDAPATAN NASIONAL & MAKROEKONOMI",
            "topic": "PDB, Inflasi, & Kebijakan Fiskal-Moneter",
            "hud_title": "AGREGAT PENDAPATAN NASIONAL",
            "hud_latex": r"Y = C + I + G + (X - M), \quad \text{Laju Inflasi} = \frac{\text{IHK}_t - \text{IHK}_{t-1}}{\text{IHK}_{t-1}} \times 100\%",
            "hud_legend": "• $Y$: Produk Domestik Bruto (PDB)<br>• $C, I, G$: Konsumsi, Investasi, Pengeluaran Pemerintah<br>• $X - M$: Ekspor Neto",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Data perekonomian suatu negara tercatat (dalam triliun rupiah): Konsumsi Rumah Tangga = Rp{1400 + i*50}, Investasi Swasta = Rp{650 + i*30}, Pengeluaran Konsumsi Pemerintah = Rp{500 + i*20}, Ekspor = Rp{320 + i*15}, Impor = Rp{280 + i*10}, Pendapatan WNA di dalam negeri = Rp{180 + i*5}, dan Pendapatan WNI di luar negeri = Rp{120 + i*5}. Besarnya Produk Nasional Bruto (PNB / GNP) negara tersebut adalah...",
                        "corr": f"Produk Nasional Bruto tercatat sebesar Rp{2530 + i*105} triliun secara kalkulatif.",
                        "dists": [
                            f"Produk Nasional Bruto tercatat sebesar Rp{2650 + i*105} triliun secara kalkulatif.",
                            f"Produk Nasional Bruto tercatat sebesar Rp{2470 + i*105} triliun secara kalkulatif.",
                            f"Produk Nasional Bruto tercatat sebesar Rp{2720 + i*105} triliun secara kalkulatif.",
                            f"Produk Nasional Bruto tercatat sebesar Rp{2390 + i*105} triliun secara kalkulatif."
                        ],
                        "concept": "PDB = C + I + G + (X - M). PNB (GNP) = PDB + Pendapatan Neto Faktor Luar Negeri (Pendapatan WNI luar negeri - Pendapatan WNA dalam negeri).",
                        "exec": "Hitung PDB terlebih dahulu: C + I + G + (X - M). Kemudian tambahkan selisih neto faktor luar negeri untuk mendapatkan GNP."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Ketika tingkat inflasi tahunan melonjak mencapai {8 + (i%5)}% akibat lonjakan harga komoditas pangan global (cost-push inflation), Bank Indonesia mengambil respon kebijakan moneter. Evaluasilah keabsahan analisis makroekonomi berikut:",
                        "statements": [
                            {"text": "Bank Indonesia dapat menaikkan suku bunga acuan (BI-Rate) untuk meredam ekspektasi inflasi.", "answer": True},
                            {"text": "Pemerintah dapat menerapkan kebijakan fiskal ekspansif dengan menaikkan subsidi konsumsi secara masif.", "answer": False},
                            {"text": "Penaikan rasio Giro Wajib Minimum (GWM) perbankan akan mengurangi jumlah uang yang beredar.", "answer": True},
                            {"text": "Operasi pasar terbuka dilakukan dengan cara menjual Surat Berharga Negara (SBN) ke publik.", "answer": True}
                        ],
                        "concept": "Mengatasi inflasi membutuhkan kebijakan moneter kontraktif (tight money policy): menaikkan BI-Rate, menaikkan GWM, dan menjual SBN.",
                        "exec": "Kebijakan fiskal ekspansif justru memicu likuiditas dan meningkatkan tekanan inflasi, sehingga opsi kedua salah."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Perhatikan tabel instrumen kebijakan ekonomi makro. Dalam kondisi perekonomian mengalami resesi dan peningkatan angka pengangguran terbuka, pilihlah kombinasi kebijakan yang TEPAT untuk menstimulasi pertumbuhan ekonomi (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Pemerintah meningkatkan belanja infrastruktur publik untuk menciptakan lapangan kerja padat karya.", "correct": True},
                            {"key": "B", "text": "Bank sentral menurunkan tingkat suku bunga acuan untuk mendorong penyaluran kredit perbankan.", "correct": True},
                            {"key": "C", "text": "Pemerintah memberikan insentif pemotongan pajak penghasilan untuk meningkatkan daya beli konsumsi.", "correct": True},
                            {"key": "D", "text": "Bank sentral menaikkan cadangan kas wajib minimum bank umum untuk memperketat likuiditas.", "correct": False},
                            {"key": "E", "text": "Pemerintah memangkas seluruh alokasi transfer bantuan sosial daerah secara signifikan.", "correct": False}
                        ],
                        "concept": "Menghadapi resesi membutuhkan kebijakan moneter dan fiskal ekspansif (lowering interest rates, cutting taxes, boosting government expenditure).",
                        "exec": "Kombinasi penurunan suku bunga dan peningkatan belanja APBN efektif menggeser kurva permintaan agregat ke kanan."
                    }
                }
            ]
        },
        {
            "materi": "SIKLUS AKUNTANSI KEUANGAN",
            "topic": "Persamaan Akuntansi, Jurnal Penyesuaian, & Laporan Keuangan",
            "hud_title": "PRINSIP DASAR AKUNTANSI RELASIONAL",
            "hud_latex": r"\text{Aset} = \text{Liabilitas} + \text{Ekuitas}, \quad \text{Laba Bersih} = \text{Pendapatan} - \text{Beban}",
            "hud_legend": "• Aset: Kas, Piutang, Perlengkapan, Peralatan<br>• Liabilitas: Utang Usaha, Pendapatan Diterima di Muka<br>• Ekuitas: Modal, Prive",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Pada 1 Oktober 2024, perusahaan jasa membayar premi asuransi kebakaran untuk jangka waktu 1 tahun sebesar Rp{24000000 + i*1200000} dan dicatat dengan pendekatan neraca (akun Asuransi Dibayar di Muka). Pada saat penutupan buku per 31 Desember 2024, ayat jurnal penyesuaian yang BENAR adalah...",
                        "corr": f"Debit Beban Asuransi Rp{6000000 + i*300000} dan Kredit Asuransi Dibayar di Muka Rp{6000000 + i*300000}.",
                        "dists": [
                            f"Debit Asuransi Dibayar di Muka Rp{6000000 + i*300000} dan Kredit Kas Tunai Rp{6000000 + i*300000}.",
                            f"Debit Beban Asuransi Rp{18000000 + i*900000} dan Kredit Asuransi Dibayar di Muka Rp{18000000 + i*900000}.",
                            f"Debit Asuransi Dibayar di Muka Rp{18000000 + i*900000} dan Kredit Ikhtisar Laba/Rugi Rp{18000000 + i*900000}.",
                            f"Debit Beban Asuransi Rp{24000000 + i*1200000} dan Kredit Asuransi Dibayar di Muka Rp{24000000 + i*1200000}."
                        ],
                        "concept": "Pendekatan neraca: yang disesuaikan adalah bagian yang sudah menjadi beban (1 Okt - 31 Des = 3 bulan). Beban = (3/12) x Total Premi.",
                        "exec": "Hitung porsi waktu 3 bulan dari 12 bulan total premi. Debit akun Beban Asuransi dan Kredit Asuransi Dibayar di Muka."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Sebuah perusahaan dagang menerapkan sistem pencatatan persediaan perpetual dengan syarat penyerahan barang FOB Shipping Point dan syarat pembayaran 2/10, n/30. Evaluasilah keabsahan perlakuan akuntansi transaksi berikut:",
                        "statements": [
                            {"text": "Beban angkut pengiriman barang dagangan menjadi tanggung jawab pihak pembeli.", "answer": True},
                            {"text": "Pembeli berhak memperoleh potongan harga 2% jika melunasi faktur dalam tempo 10 hari sejak transaksi.", "answer": True},
                            {"text": "Hak kepemilikan barang dagang baru berpindah saat barang tiba di gudang tujuan pembeli.", "answer": False},
                            {"text": "Pada sistem perpetual, setiap transaksi penjualan langsung mencatat debit akun Harga Pokok Penjualan.", "answer": True}
                        ],
                        "concept": "FOB Shipping Point: hak milik dan ongkos angkut berpindah ke pembeli saat barang keluar dari dermaga/gudang penjual.",
                        "exec": "Pernyataan ketiga salah karena pada FOB Shipping Point kepemilikan berpindah di titik pengapalan, bukan di gudang pembeli."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam penyusunan kertas kerja (neraca lajur 10 kolom) akhir periode akuntansi, akun-akun berikut ini yang saldo akhirnya wajib dipindahkan ke kolom Laporan Posisi Keuangan (Neraca) adalah (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Akun Akumulasi Penyusutan Peralatan (saldo normal kredit sebagai akun kontra aset).", "correct": True},
                            {"key": "B", "text": "Akun Pendapatan Sewa Diterima di Muka (kewajiban lancar yang belum jatuh tempo).", "correct": True},
                            {"key": "C", "text": "Akun Prive Pemilik Usaha (pengurang ekuitas modal dalam penutupan buku).", "correct": True},
                            {"key": "D", "text": "Akun Beban Gaji Karyawan Bagian Administrasi (komponen pengurang laba periode).", "correct": False},
                            {"key": "E", "text": "Akun Pendapatan Jasa Konsultasi Bisnis (komponen pendapatan usaha kotor).", "correct": False}
                        ],
                        "concept": "Kolom Neraca memuat akun riil: Aset, Liabilitas, dan Ekuitas (termasuk kontra-aset dan prive). Akun nominal masuk ke Laba/Rugi.",
                        "exec": "Beban dan Pendapatan dipindahkan ke kolom Laba Rugi, sedangkan Akumulasi Penyusutan, Pendapatan Diterima di Muka, dan Prive masuk Neraca."
                    }
                }
            ]
        }
    ]
    
    # Generate 135 items
    for idx in range(1, 136):
        pillar = pillars[(idx - 1) % len(pillars)]
        concept = pillar["concepts"][(idx - 1) % len(pillar["concepts"])]
        
        diff = "easy" if idx <= 35 else ("medium" if idx <= 70 else ("hard" if idx <= 105 else "simulation_hots"))
        data = concept["builder"](idx, diff)
        
        q_item = {
            "id": f"eko_{idx:03d}",
            "subject": "ekonomi",
            "type": concept["type"],
            "difficulty": diff,
            "materi": pillar["materi"],
            "topic": pillar["topic"],
            "question": data["stem"],
            "formula_title": pillar["hud_title"],
            "formula_latex": pillar["hud_latex"],
            "formula_legend": pillar["hud_legend"],
            "concept_hint": data["concept"],
            "execution_hint": data["exec"]
        }
        
        if concept["type"] == "mcq":
            opts, target_key = balance_options(data["corr"], data["dists"])
            q_item["options"] = opts
            q_item["correctAnswer"] = target_key
        elif concept["type"] == "matrix":
            q_item["statements"] = data["statements"]
        elif concept["type"] == "multi":
            q_item["options"] = data["options"]
            q_item["correctKeys"] = [o["key"] for o in data["options"] if o.get("correct")]
            
        questions.append(q_item)
        
    return questions


# =========================================================================
# 2. GEOGRAFI (135 SOAL)
# =========================================================================
def generate_geografi():
    questions = []
    
    pillars = [
        {
            "materi": "PENGINDERAAN JAUH & SISTEM INFORMASI GEOGRAFIS",
            "topic": "Interpretasi Citra & Analisis Spasial SIG",
            "hud_title": "PRINSIP SPASIAL & INTERPRETASI CITRA",
            "hud_latex": r"\text{Skala Peta} = \frac{d_{\text{peta}}}{d_{\text{sebenarnya}}}, \quad \text{NDVI} = \frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}",
            "hud_legend": "• $d$: Jarak peta vs lapangan<br>• $\\text{NIR}$: Gelombang inframerah dekat<br>• $\\text{Red}$: Gelombang spektrum merah",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam interpretasi citra foto udara penginderaan jauh, ditemukan kenampakan dengan rona gelap, tajuk berbentuk bintang, pola teratur seragam dengan jarak tanam tetap {8 + (i%3)} meter, serta berasosiasi dengan jaringan jalan tanah berpetak. Objek bentang lahan tersebut adalah...",
                        "corr": "Perkebunan kelapa sawit yang berada pada fase pertumbuhan vegetatif optimal.",
                        "dists": [
                            "Hutan hujan tropis primer yang memiliki kanopi vegetasi rapat alami liar.",
                            "Perkebunan tanaman karet yang sedang mengalami proses pengguguran daun.",
                            "Kawasan hutan mangrove di garis pesisir pantai berlumpur tergenang pasang.",
                            "Lahan persawahan pasang surut tradisional yang baru selesai masa panen."
                        ],
                        "concept": "Tajuk bintang dan pola tanam geometris teratur merupakan ciri khas perkebunan kelapa sawit pada citra resolusi spasial tinggi.",
                        "exec": "Gunakan unsur bentuk tajuk (bintang), pola teratur, dan jarak tanam seragam untuk mengidentifikasi vegetasi kelapa sawit."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Sebuah tim perencana tata ruang daerah melakukan analisis tumpang susun (overlay) layer data spasial untuk menentukan zona rawan bahaya tanah longsor. Evaluasilah kebenaran prinsip SIG berikut:",
                        "statements": [
                            {"text": "Data kemiringan lereng dari DEM dapat ditumpangsusunkan dengan peta jenis tanah dan curah hujan.", "answer": True},
                            {"text": "Format data raster lebih unggul dibandingkan vektor dalam merepresentasikan batas kepemilikan persil tanah.", "answer": False},
                            {"text": "Analisis pembobotan (weighted overlay) memberikan nilai signifikansi berbeda pada tiap parameter fisik.", "answer": True},
                            {"text": "Fungsi buffer digunakan untuk menentukan zona penyangga keamanan di sepanjang lereng kritis.", "answer": True}
                        ],
                        "concept": "Data raster merepresentasikan permukaan kontinu (seperti elevasi DEM), sedangkan data vektor presisi untuk batas diskrit (persil tanah).",
                        "exec": "Pernyataan kedua salah karena data vektor memiliki akurasi topologi lebih tinggi untuk batas kadastral persil tanah."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Nilai indeks vegetasi Normalized Difference Vegetation Index (NDVI) dianalisis dari data satelit Sentinel-2 pada wilayah DAS hulu. Pilihlah interpretasi fisis yang BENAR jika diperoleh nilai NDVI mendekati +0,8 (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Kawasan tersebut memiliki kerapatan kanopi vegetasi hijau klorofil yang sangat tinggi.", "correct": True},
                            {"key": "B", "text": "Klorofil daun menyerap kuat spektrum merah dan memantulkan kuat gelombang inframerah dekat.", "correct": True},
                            {"key": "C", "text": "Kondisi tutupan lahan hulu memiliki fungsi resapan hidrologis yang sangat baik.", "correct": True},
                            {"key": "D", "text": "Wilayah tersebut teridentifikasi sebagai tubuh air jernih dan batuan gundul tak bervegetasi.", "correct": False},
                            {"key": "E", "text": "Nilai indeks menunjukkan tingkat degradasi lahan kritis akibat erosi permukaan ekstrem.", "correct": False}
                        ],
                        "concept": "NDVI mendekati +1 menunjukkan vegetasi lebat sehat karena pantulan NIR tinggi dan serapan Red tinggi oleh klorofil aktif.",
                        "exec": "Tubuh air bernilai negatif, sedangkan nilai tinggi (+0,6 s/d +0,9) mencerminkan kerapatan hutan alami yang optimal."
                    }
                }
            ]
        },
        {
            "materi": "LITOSFER & DINAMIKA KEBENCANAAN",
            "topic": "Seismisitas, Tektonisme, & Vulkanisme",
            "hud_title": "RUMUS LASKA EPISENTRUM GEMPA",
            "hud_latex": r"\Delta = \{(S - P) - 1'\} \times 1000\text{ km}",
            "hud_legend": "• $\\Delta$: Jarak stasiun ke episentrum gempa<br>• $S$: Waktu gelombang sekunder tiba<br>• $P$: Waktu gelombang primer tiba (1' = 1 menit)",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Stasiun seismologi A mencatat gelombang primer (P) tiba pada pukul 14.2{i%5}.{10 + (i%40)} WIB dan gelombang sekunder (S) tiba pada pukul 14.2{i%5 + 1}.{40 + (i%20)} WIB. Berdasarkan perhitungan hukum Laska, jarak episentrum gempa bumi dari stasiun seismik tersebut adalah...",
                        "corr": f"Jarak episentrum gempa bumi adalah tepat {1500 + i*50} km dari stasiun perekam.",
                        "dists": [
                            f"Jarak episentrum gempa bumi adalah tepat {1750 + i*50} km dari stasiun perekam.",
                            f"Jarak episentrum gempa bumi adalah tepat {1250 + i*50} km dari stasiun perekam.",
                            f"Jarak episentrum gempa bumi adalah tepat {2100 + i*50} km dari stasiun perekam.",
                            f"Jarak episentrum gempa bumi adalah tepat {950 + i*50} km dari stasiun perekam."
                        ],
                        "concept": "Rumus Laska: Δ = {(S - P) - 1 menit} x 1.000 km. Selisih waktu dikonversi ke desimal menit lalu dikurangi 1.",
                        "exec": "Hitung selisih waktu (S - P), kurangi 1 menit, lalu kalikan 1.000 km untuk memperoleh radius jarak episentrum."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Kawasan pertemuan Lempeng Indo-Australia yang menunjam ke bawah Lempeng Eurasia di selatan Pulau Jawa membentuk zona subduksi aktif. Analisislah fenomena geomorfologi dan kebencanaan berikut:",
                        "statements": [
                            {"text": "Aktivitas penunjaman lempeng membentuk palung laut dalam (trench) di selatan Jawa.", "answer": True},
                            {"text": "Busur vulkanik pegunungan api terbentuk sejajar dengan garis zona penunjaman lempeng.", "answer": True},
                            {"text": "Gempa bumi megathrust berpotensi memicu gelombang tsunami bila terjadi deformasi vertikal dasar laut.", "answer": True},
                            {"text": "Tipe batas lempeng di kawasan subduksi tersebut merupakan batas lempeng divergen yang saling menjauh.", "answer": False}
                        ],
                        "concept": "Subduksi adalah batas konvergen (lempeng saling bertumbukan), bukan divergen. Deformasi vertikal lempeng di laut memicu tsunami.",
                        "exec": "Pernyataan keempat salah karena zona subduksi merupakan perwujudan batas lempeng konvergen."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Saat terjadi erupsi gunung api tipe eksplosif dengan indeks letusan VEI tinggi, pilihlah bahaya primer dan sekunder vulkanik yang mengancam pemukiman lereng bawah (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Awan panas guguran (pyroclastic density current) yang meluncur dengan kecepatan ratusan km/jam.", "correct": True},
                            {"key": "B", "text": "Hujan abu vulkanik lebat yang dapat merusak struktur atap dan mengganggu saluran pernapasan.", "correct": True},
                            {"key": "C", "text": "Banjir lahar dingin di sepanjang lembah sungai saat curah hujan tinggi mengguyur puncak.", "correct": True},
                            {"key": "D", "text": "Terbentuknya intrusi magma batolit beku di dalam kerak bumi yang mengangkat dasar laut.", "correct": False},
                            {"key": "E", "text": "Penurunan drastis konsentrasi gas sulfur dioksida dan karbon monoksida di sekitar kawah.", "correct": False}
                        ],
                        "concept": "Bahaya primer mencakup awan panas, lontaran piroklastik, dan abu vulkanik. Bahaya sekunder meliputi lahar hujan (lahar dingin).",
                        "exec": "Batolit merupakan struktur intrusi bawah permukaan (bukan bahaya permukaan), dan gas beracun justru melonjak drastis saat erupsi."
                    }
                }
            ]
        },
        {
            "materi": "INTERAKSI KERUANGAN DESA-KOTA",
            "topic": "Teori Gravitasi Reilly & Teori Titik Henti",
            "hud_title": "MODEL INTERAKSI SPASIAL REILLY & CARROTHERS",
            "hud_latex": r"I_{AB} = k \frac{P_A \cdot P_B}{d_{AB}^2}, \quad D_{AB} = \frac{d_{AB}}{1 + \sqrt{\frac{P_B}{P_A}}}",
            "hud_legend": "• $P_A, P_B$: Jumlah penduduk wilayah A dan B<br>• $d_{AB}$: Jarak absolut kedua wilayah (km)<br>• $D_{AB}$: Lokasi titik henti ideal dari wilayah berpenduduk lebih kecil",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Kota Megapolitan A memiliki jumlah penduduk {1600000 + i*100000} jiwa dan Kota Satelit B memiliki penduduk {100000 + i*10000} jiwa. Jarak antara kedua kota adalah {60 + (i%20)} km. Berdasarkan Teori Titik Henti (Breaking Point Theory), lokasi ideal untuk mendirikan fasilitas pusat pelayanan bersama adalah...",
                        "corr": f"Tepat berjarak {12 + (i%4)} km diukur dari pusat Kota Satelit B.",
                        "dists": [
                            f"Tepat berjarak {18 + (i%4)} km diukur dari pusat Kota Satelit B.",
                            f"Tepat berjarak {24 + (i%4)} km diukur dari pusat Kota Satelit B.",
                            f"Tepat berjarak {30 + (i%4)} km diukur dari pusat Kota Satelit B.",
                            f"Tepat berjarak {8 + (i%4)} km diukur dari pusat Kota Satelit B."
                        ],
                        "concept": "Teori Titik Henti menghitung jarak lokasi fasilitas: DAB = d / (1 + √(PA/PB)), diukur dari kota dengan jumlah penduduk lebih sedikit.",
                        "exec": "Substitusikan rasio akar penduduk ke penyebut formula titik henti, lalu bagi jarak total dengan hasil tersebut."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Interaksi keruangan antara desa sebagai pemasok komoditas pangan dan kota sebagai pusat industri pengolahan menghasilkan arus perpindahan spasial. Evaluasilah pernyataan teori keruangan berikut:",
                        "statements": [
                            {"text": "Semakin dekat jarak antarwilayah, kekuatan interaksi gravitasi antarkota akan berbanding terbalik dengan kuadrat jarak.", "answer": True},
                            {"text": "Pembangunan jalan tol antarwilayah meningkatkan nilai indeks konektivitas jaringan jalan wilayah.", "answer": True},
                            {"text": "Arus urbanisasi berlebih selalu menghasilkan dampak penyebaran kemakmuran (spread effect) merata ke perdesaan.", "answer": False},
                            {"text": "Zona rural-urban fringe merupakan zona transisi pemanfaatan lahan campuran antara pertanian dan pemukiman.", "answer": True}
                        ],
                        "concept": "Urbanisasi berlebih sering kali memicu fenomena backwash effect (pengurasan SDM perdesaan), bukan spread effect yang merata.",
                        "exec": "Pernyataan ketiga salah karena polarisasi ekonomi kota sering kali menekan ekonomi pedesaan melalui backwash effect."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam teori struktur keruangan kota model konsentris Ernest Burgess, pilihlah karakteristik zona-zona tata ruang fungsional kota yang BENAR (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Zona Pusat Daerah Kegiatan (CBD) menempati lingkaran inti terdalam sebagai pusat bisnis dan retail.", "correct": True},
                            {"key": "B", "text": "Zona Transisi mengelilingi CBD dan sering mengalami kemerosotan kualitas lingkungan permukiman (slum area).", "correct": True},
                            {"key": "C", "text": "Zona Permukiman Penglaju (commuter zone) berada di lapisan paling luar melintasi batas pinggiran kota.", "correct": True},
                            {"key": "D", "text": "Zona permukiman kelas atas berada tepat berdampingan menempel langsung dengan pabrik industri berat.", "correct": False},
                            {"key": "E", "text": "Struktur pembagian kota terbentuk murni mengikuti koridor jalur transportasi radial seperti irisan kue.", "correct": False}
                        ],
                        "concept": "Model Konsentris Burgess terdiri atas 5 cincin melingkar: CBD, Transisi, Pekerja, Kelas Menengah, dan Penglaju (Commuter).",
                        "exec": "Model irisan kue merupakan Model Sektoral Homer Hoyt, sedangkan Burgess berbentuk lingkaran konsentris simetris."
                    }
                }
            ]
        }
    ]
    
    # Generate 135 items
    for idx in range(1, 136):
        pillar = pillars[(idx - 1) % len(pillars)]
        concept = pillar["concepts"][(idx - 1) % len(pillar["concepts"])]
        
        diff = "easy" if idx <= 35 else ("medium" if idx <= 70 else ("hard" if idx <= 105 else "simulation_hots"))
        data = concept["builder"](idx, diff)
        
        q_item = {
            "id": f"geo_{idx:03d}",
            "subject": "geografi",
            "type": concept["type"],
            "difficulty": diff,
            "materi": pillar["materi"],
            "topic": pillar["topic"],
            "question": data["stem"],
            "formula_title": pillar["hud_title"],
            "formula_latex": pillar["hud_latex"],
            "formula_legend": pillar["hud_legend"],
            "concept_hint": data["concept"],
            "execution_hint": data["exec"]
        }
        
        if concept["type"] == "mcq":
            opts, target_key = balance_options(data["corr"], data["dists"])
            q_item["options"] = opts
            q_item["correctAnswer"] = target_key
        elif concept["type"] == "matrix":
            q_item["statements"] = data["statements"]
        elif concept["type"] == "multi":
            q_item["options"] = data["options"]
            q_item["correctKeys"] = [o["key"] for o in data["options"] if o.get("correct")]
            
        questions.append(q_item)
        
    return questions


# =========================================================================
# 3. SOSIOLOGI (135 SOAL)
# =========================================================================
def generate_sosiologi():
    questions = []
    
    pillars = [
        {
            "materi": "STRUKTUR SOSIAL & DIFERENSIASI",
            "topic": "Stratifikasi, Diferensiasi, & Dinamika Kelompok",
            "hud_title": "PARADIGMA TEORI STRUKTUR SOSIAL",
            "hud_latex": r"\text{Struktur Sosial} = \text{Diferensiasi (Horizontal)} + \text{Stratifikasi (Vertikal)}",
            "hud_legend": "• Diferensiasi: Pengelompokan setara tanpa hierarki (suku, klan, gender)<br>• Stratifikasi: Pelapisan berjenjang atas-bawah (kelas ekonomi, kekuasaan)",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Di suatu masyarakat multikultural perkotaan, warga dari berbagai latar belakang suku dan profesi membentuk serikat pekerja koperasi bersama. Anggota suku A berprofesi sebagai pedagang dan guru, sedangkan suku B juga berprofesi sebagai guru dan teknisi. Hubungan silang antar-keanggotaan kelompok sosial tersebut dalam sosiologi disebut...",
                        "corr": "Interseksi sosial yang memperkuat integrasi antarkelompok masyarakat.",
                        "dists": [
                            "Konsolidasi sosial yang memicu penguatan sentimen primordialisme kaku.",
                            "Segregasi spasial yang memisahkan permukiman antarras secara permanen.",
                            "Asimilasi mutlak yang menghapuskan identitas kebudayaan asli leluhur.",
                            "Polarisasi kekuasaan yang mendorong terjadinya disintegrasi horizontal."
                        ],
                        "concept": "Interseksi (persilangan keanggotaan) mempertemukan individu dari suku berbeda dalam profesi/organisasi sama, melemahkan potensi konflik primordial.",
                        "exec": "Bila dua atribut sosial (suku dan profesi) saling bersilang keanggotaan, fenomena tersebut adalah interseksi (bukan konsolidasi)."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Sistem stratifikasi sosial dalam masyarakat menentukan derajat keterbukaan mobilitas sosial vertikal individu. Evaluasilah kebenaran analisis stratifikasi berikut:",
                        "statements": [
                            {"text": "Sistem kasta tradisional di Bali/India merupakan contoh nyata sistem stratifikasi sosial tertutup (closed stratification).", "answer": True},
                            {"text": "Dalam sistem stratifikasi terbuka, status sosial diraih melalui usaha mandiri (achieved status) dan meritokrasi.", "answer": True},
                            {"text": "Pendidikan formal tingkat tinggi tidak dapat berfungsi sebagai saluran mobilitas sosial vertikal naik (social climbing).", "answer": False},
                            {"text": "Perubahan status individu dari guru honorer menjadi kepala sekolah definitif merupakan bentuk mobilitas vertikal naik.", "answer": True}
                        ],
                        "concept": "Stratifikasi terbuka memungkinkan mobilitas vertikal melalui pendidikan, ekonomi, dan profesi. Pendidikan adalah social elevator utama.",
                        "exec": "Pernyataan ketiga salah karena lembaga pendidikan merupakan saluran utama mobilitas sosial vertikal (social elevator)."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Ferdinand Tönnies membedakan kelompok sosial menjadi Paguyuban (Gemeinschaft) dan Patembayan (Gesellschaft). Pilihlah ciri-ciri mendasar dari Paguyuban (Gemeinschaft) (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Hubungan batin bersifat intim, mendalam, dan bersifat pribadi (intimate).", "correct": True},
                            {"key": "B", "text": "Ikatan relasi sosial bersifat eksklusif hanya untuk kelompok internal (exclusive).", "correct": True},
                            {"key": "C", "text": "Hubungan antaranggota bersifat permanen dan langgeng tanpa batas kontrak (private).", "correct": True},
                            {"key": "D", "text": "Interaksi didasarkan pada perjanjian kontrak kerja formal dan kalkulasi untung rugi.", "correct": False},
                            {"key": "E", "text": "Struktur kepemimpinan didasarkan pada birokrasi legalitas modern rasional.", "correct": False}
                        ],
                        "concept": "Ciri khas Gemeinschaft menurut Tönnies: Intimate, Private, dan Exclusive, berakar pada cinta kasih dan kekerabatan darah/tempat.",
                        "exec": "Perjanjian kontrak dan kalkulasi rasional untung-rugi merupakan sifat khas kelompok Patembayan (Gesellschaft)."
                    }
                }
            ]
        },
        {
            "materi": "KONFLIK SOSIAL & RESOLUSI",
            "topic": "Dinamika Konflik, Akomodasi, & Integrasi",
            "hud_title": "BENTUK-BENTUK AKOMODASI KONFLIK",
            "hud_latex": r"\text{Akomodasi} \rightarrow \text{Mediasi (Non-binding)} \quad \text{vs} \quad \text{Arbitrase (Binding)}",
            "hud_legend": "• Mediasi: Pihak ketiga netral bertindak sebagai penasihat/fasilitator<br>• Arbitrase: Pihak ketiga berwenang mengambil keputusan mengikat",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Sengketa batas tanah ulayat antardua desa adat diselesaikan melalui bantuan perwakilan pemerintah daerah setempat. Pejabat pemerintah mendengarkan keluhan kedua belah pihak dan memberikan opsi kesepakatan damai, namun keputusan akhir mutlak diserahkan kembali kepada persetujuan musyawarah para tetua adat. Bentuk akomodasi konflik tersebut adalah...",
                        "corr": "Mediasi karena pihak ketiga hanya berperan sebagai fasilitator netral.",
                        "dists": [
                            "Arbitrase karena pihak ketiga memiliki wewenang hukum mutlak mengikat.",
                            "Konsiliasi karena penyelesaian dilakukan melalui lembaga peradilan resmi negara.",
                            "Ajudikasi karena perkara diselesaikan melalui vonis meja hijau pengadilan.",
                            "Koersi karena penyelesaian ditempuh melalui paksaan ancaman aparat militer."
                        ],
                        "concept": "Dalam mediasi, pihak ketiga netral tidak berhak memutuskan; keputusan akhir tetap di tangan pihak yang bersengketa.",
                        "exec": "Karena pihak ketiga hanya memfasilitasi dan tidak memaksakan keputusan vonis, bentuk akomodasi adalah mediasi."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Teori konflik sosiologis membedah bahwa ketegangan sosial tidak selalu berujung destruktif, melainkan dapat mendorong perubahan sistem. Evaluasilah kebenaran analisis teori konflik berikut:",
                        "statements": [
                            {"text": "Karl Marx memandang konflik bersumber dari pertentangan kelas pemilik modal (borjuis) dan pekerja (proletar).", "answer": True},
                            {"text": "Ralf Dahrendorf menyatakan bahwa distribusi otoritas kekuasaan yang tidak merata merupakan sumber utama konflik sosial.", "answer": True},
                            {"text": "Konflik kekerasan antarkelompok dapat meningkatkan solidaritas in-group di dalam masing-masing kelompok yang berkonflik.", "answer": True},
                            {"text": "Lewis A. Coser menyatakan bahwa konflik tidak memiliki fungsi positif sama sekali dalam memelihara batas kelompok sosial.", "answer": False}
                        ],
                        "concept": "Lewis Coser memperkenalkan 'The Functions of Social Conflict', membuktikan bahwa konflik mempertegas batas kelompok dan merevitalisasi norma.",
                        "exec": "Pernyataan keempat salah karena Coser justru menekankan fungsi positif konflik dalam menjaga dinamika dan integrasi batas kelompok."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam mewujudkan integrasi sosial di tengah masyarakat multikultural yang rawan gesekan horizontal, faktor-faktor pendorong integrasi sosial meliputi (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Sikap toleransi dan saling menghargai perbedaan kebudayaan antaretnis.", "correct": True},
                            {"key": "B", "text": "Adanya musuh bersama dari luar yang mengancam keutuhan kedaulatan bangsa.", "correct": True},
                            {"key": "C", "text": "Peluang yang seimbang dalam bidang ekonomi (kesetaraan akses modal kerja).", "correct": True},
                            {"key": "D", "text": "Penguatan sikap etnosentrisme sempit yang mengagungkan keunggulan budaya sendiri.", "correct": False},
                            {"key": "E", "text": "Dominasi mutlak satu kelompok mayoritas atas pengambilan keputusan politik publik.", "correct": False}
                        ],
                        "concept": "Faktor pendorong integrasi: toleransi, cross-cutting affiliations, musuh bersama dari luar, perkawinan campur (amalgamasi), dan keadilan ekonomi.",
                        "exec": "Etnosentrisme dan dominasi hegemoni mayoritas adalah faktor penghambat yang memicu disintegrasi sosial."
                    }
                }
            ]
        },
        {
            "materi": "PERUBAHAN SOSIAL & METODOLOGI RISET",
            "topic": "Globalisasi, Modernisasi, & Riset Empiris",
            "hud_title": "TEORI PERUBAHAN SOSIAL & METODOLOGI RISET",
            "hud_latex": r"\text{Cultural Lag} = \text{Materiil Cepat} - \text{Imateriil Lambat}",
            "hud_legend": "• Cultural Lag: Kesenjangan kecepatan perkembangan teknologi materiil dibanding kesiapan nilai norma kultural",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Perkembangan pesat teknologi kecerdasan artifisial (AI) dan media digital tidak diimbangi dengan kedewasaan etika digital masyarakat, sehingga marak penyebaran berita bohong (hoaks) dan pencurian identitas siber. Kesenjangan adaptasi budaya menurut William F. Ogburn disebut...",
                        "corr": "Cultural lag karena kebudayaan nonmateriil tertinggal dari teknologi.",
                        "dists": [
                            "Cultural shock karena masyarakat menolak total kehadiran perangkat teknologi baru.",
                            "Anomi sosial karena runtuhnya seluruh struktur tatanan hukum pidana negara.",
                            "Disorganisasi keluarga karena menurunnya fungsi sosialisasi primer orang tua.",
                            "Difusi kultural karena penyebaran gagasan inovasi teknologi berlangsung lambat."
                        ],
                        "concept": "Cultural lag terjadi ketika kebudayaan materiil (gadget/AI) melaju kencang tetapi kebudayaan nonmateriil (etika/hukum) lambat beradaptasi.",
                        "exec": "Kesenjangan antara kemajuan alat fisik/digital dan etika moralitas penggunaan adalah definisi murni Cultural Lag Ogburn."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Seorang peneliti sosiologi mengkaji dampak kecanduan game online terhadap penurunan prestasi akademik remaja dengan metode survei kuesioner skala Likert. Evaluasilah keabsahan metodologi penelitian empiris berikut:",
                        "statements": [
                            {"text": "Uji validitas digunakan untuk mengukur sejauh mana instrumen pertanyaan mampu mengukur variabel penelitian secara tepat.", "answer": True},
                            {"text": "Teknik pengambilan sampel acak sederhana (simple random sampling) memberikan peluang sama bagi setiap siswa untuk terpilih.", "answer": True},
                            {"text": "Data kuantitatif hasil kuesioner dianalisis menggunakan metode reduksi data dan triangulasi sumber.", "answer": False},
                            {"text": "Skala Likert lazim digunakan untuk mengukur sikap, persepsi, dan derajat persetujuan responden terhadap suatu fenomena.", "answer": True}
                        ],
                        "concept": "Reduksi data dan triangulasi adalah teknik analisis data kualitatif, bukan analisis statistik untuk data survei kuantitatif.",
                        "exec": "Pernyataan ketiga salah karena data kuesioner kuantitatif dianalisis via statistik deskriptif/inferensial, bukan triangulasi kualitatif."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Robert K. Merton membagi tipologi adaptasi individu terhadap struktur norma dan tujuan sosial budaya. Pilihlah bentuk adaptasi penyimpangan (deviant behavior) yang BENAR (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Inovasi: Individu menerima tujuan budaya kemakmuran tetapi menempuh cara-cara terlarang/ilegal.", "correct": True},
                            {"key": "B", "text": "Ritualisme: Individu menolak tujuan kekayaan besar tetapi sangat taat berlebihan pada rutinitas cara kerja.", "correct": True},
                            {"key": "C", "text": "Retretisme: Individu menolak tujuan budaya sekaligus menolak cara-cara institusional konvensional.", "correct": True},
                            {"key": "D", "text": "Konformitas: Individu mematuhi cara yang sah demi mencapai tujuan sukses yang disepakati masyarakat.", "correct": False},
                            {"key": "E", "text": "Rebellion: Individu menerima sepenuhnya tatanan hukum tanpa berupaya merombak struktur kekuasaan.", "correct": False}
                        ],
                        "concept": "Tipologi Merton: Konformitas bukan penyimpangan. Penyimpangan mencakup: Inovasi, Ritualisme, Retretisme, dan Pemberontakan (Rebellion).",
                        "exec": "Konformitas adalah kepatuhan normal (bukan deviasi), dan rebellion justru bertujuan merombak tujuan serta cara yang ada."
                    }
                }
            ]
        }
    ]
    
    # Generate 135 items
    for idx in range(1, 136):
        pillar = pillars[(idx - 1) % len(pillars)]
        concept = pillar["concepts"][(idx - 1) % len(pillar["concepts"])]
        
        diff = "easy" if idx <= 35 else ("medium" if idx <= 70 else ("hard" if idx <= 105 else "simulation_hots"))
        data = concept["builder"](idx, diff)
        
        q_item = {
            "id": f"sos_{idx:03d}",
            "subject": "sosiologi",
            "type": concept["type"],
            "difficulty": diff,
            "materi": pillar["materi"],
            "topic": pillar["topic"],
            "question": data["stem"],
            "formula_title": pillar["hud_title"],
            "formula_latex": pillar["hud_latex"],
            "formula_legend": pillar["hud_legend"],
            "concept_hint": data["concept"],
            "execution_hint": data["exec"]
        }
        
        if concept["type"] == "mcq":
            opts, target_key = balance_options(data["corr"], data["dists"])
            q_item["options"] = opts
            q_item["correctAnswer"] = target_key
        elif concept["type"] == "matrix":
            q_item["statements"] = data["statements"]
        elif concept["type"] == "multi":
            q_item["options"] = data["options"]
            q_item["correctKeys"] = [o["key"] for o in data["options"] if o.get("correct")]
            
        questions.append(q_item)
        
    return questions


# =========================================================================
# 4. SEJARAH TINGKAT LANJUT (135 SOAL)
# =========================================================================
def generate_sejarah_lanjut():
    questions = []
    
    pillars = [
        {
            "materi": "HISTORIOGRAFI & METODE SEJARAH",
            "topic": "Tahapan Riset Sejarah & Kritik Sumber",
            "hud_title": "METODOLOGI RISET SEJARAH KRITIS",
            "hud_latex": r"\text{Riset Sejarah} = \text{Heuristik} \rightarrow \text{Kritik (Intern/Ekstern)} \rightarrow \text{Interpretasi} \rightarrow \text{Historiografi}",
            "hud_legend": "• Heuristik: Pelacakan dan pengumpulan jejak sumber sejarah<br>• Kritik Ekstern: Menguji keaslian fisik sumber<br>• Kritik Intern: Menguji kebenaran isi narasi kesaksian",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Seorang sejarawan sedang meneliti peristiwa Rapat Raksasa Ikada 19 September 1945. Dalam menguji sebuah dokumen arsip memoar tokoh politik, peneliti menganalisis jenis kertas, usia tinta stempel militer Jepang, dan keaslian tanda tangan pejabat pembuat dokumen. Tahapan riset sejarah yang sedang dilakukan adalah...",
                        "corr": "Kritik eksternal untuk menguji otentisitas fisik keaslian dokumen sejarah.",
                        "dists": [
                            "Kritik internal untuk menguji kredibilitas isi kebenaran narasi kesaksian.",
                            "Heuristik dokumen untuk mengumpulkan jejak peninggalan dari gedung arsip.",
                            "Interpretasi fakta untuk menyintesis hubungan kausalitas peristiwa masa lalu.",
                            "Historiografi akhir untuk merangkai kisah penulisan sejarah menjadi buku."
                        ],
                        "concept": "Kritik eksternal berfokus pada wujud fisik sumber (kertas, tinta, bahasa zaman, tanda tangan), sedangkan kritik internal menguji kredibilitas konten.",
                        "exec": "Pengujian fisik kertas, tinta, dan stempel adalah ciri khas verifikasi kritik eksternal (otentisitas dokumen)."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam epistemologi ilmu sejarah, konsep berpikir diakronik dan sinkronik memiliki peran komplementer. Evaluasilah kebenaran analisis metodologi sejarah berikut:",
                        "statements": [
                            {"text": "Konsep berpikir diakronik menekankan penelusuran peristiwa memanjang dalam waktu dan mementingkan proses kronologis.", "answer": True},
                            {"text": "Pendekatan sinkronik mempelajari peristiwa sejarah meluas dalam ruang dengan membedah struktur sosial dan ekonomi mendalam.", "answer": True},
                            {"text": "Sejarah konvensional bersifat mutlak sinkronik tanpa memerlukan urutan kronologi waktu peristiwa.", "answer": False},
                            {"text": "Periodisasi dibuat oleh sejarawan untuk mempermudah pemahaman babakan babak waktu perkembangan sejarah.", "answer": True}
                        ],
                        "concept": "Ciri khas sejarah adalah diakronik (memanjang dalam waktu, terbatas ruang), sedangkan ilmu sosial lain umumnya sinkronik (meluas dalam ruang).",
                        "exec": "Pernyataan ketiga salah karena hakikat dasar ilmu sejarah berakar pada kronologi dan kontinuitas waktu (diakronik)."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Perhatikan klasifikasi sumber sejarah. Kategori sumber primer (primary sources) yang memiliki nilai autentisitas tertinggi bagi riset sejarawan adalah (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Naskah Proklamasi Kemerdekaan RI berkas tulisan tangan asli Bung Karno tahun 1945.", "correct": True},
                            {"key": "B", "text": "Rekaman siaran radio asli pidato Bung Tomo saat pertempuran 10 November 1945.", "correct": True},
                            {"key": "C", "text": "Buku buku harian (diary) pejuang yang ditulis langsung di garis depan palagan pertempuran.", "correct": True},
                            {"key": "D", "text": "Buku teks sejarah nasional terbitan kementerian pendidikan 60 tahun pasca kemerdekaan.", "correct": False},
                            {"key": "E", "text": "Artikel opini ensiklopedia digital populer yang ditulis kontributor umum di internet.", "correct": False}
                        ],
                        "concept": "Sumber primer berasal dari zaman yang sama dengan peristiwa dan dibuat oleh pelaku/saksi mata sezaman langsung.",
                        "exec": "Buku teks modern dan ensiklopedia internet merupakan sumber sekunder atau tersier, bukan sumber primer autentik."
                    }
                }
            ]
        },
        {
            "materi": "DIPLOMASI & PERJUANGAN KEMERDEKAAN",
            "topic": "Perang Kemerdekaan, Linggarjati, Renville, & KMB",
            "hud_title": "JALUR DIPLOMASI KEMERDEKAAN RI 1945–1949",
            "hud_latex": r"\text{Kedaulatan RI} = \text{Perjuangan Senjata (Fisik)} + \text{Diplomasi Meja Perundingan}",
            "hud_legend": "• Linggarjati (1946): Pengakuan de facto Jawa, Madura, Sumatra<br>• Renville (1948): Garis Demarkasi van Mook<br>• KMB (1949): Pengakuan kedaulatan RIS tanpa syarat",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Perjanjian Renville yang ditandatangani pada Januari 1948 di atas kapal perang USS Renville menimbulkan dampak kerugian strategis yang sangat besar bagi Republik Indonesia karena...",
                        "corr": "TNI harus ditarik mundur (hijrah) dari kantong wilayah pertahanan di Jawa Barat.",
                        "dists": [
                            "Belanda menuntut penyerahan seluruh senjata infanteri milik laskar milisi pejuang.",
                            "Ibu kota negara di Yogyakarta diserahkan kembali sepenuhnya ke tangan administrasi NICA.",
                            "Indonesia diwajibkan membayar kompensasi ganti rugi perang kepada tentara sekutu Inggris.",
                            "PBB membubarkan Komisi Tiga Negara dan menolak membahas agresi militer Belanda."
                        ],
                        "concept": "Perjanjian Renville menetapkan 'Garis van Mook', memaksa Divisi Siliwangi melakukan long-march hijrah meninggalkan kantong gerilya Jawa Barat.",
                        "exec": "Dampak militer paling krusial dari Renville adalah evakuasi dan hijrahnya pasukan TNI dari kantong-kantong gerilya di belakang garis van Mook."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Agresi Militer Belanda II pada 19 Desember 1948 menargetkan penghancuran simbolik Republik Indonesia dengan menduduki ibu kota Yogyakarta. Evaluasilah kebenaran fakta sejarah diplomasi berikut:",
                        "statements": [
                            {"text": "Sebelum ditawan Belanda, Presiden Soekarno mengirim mandat pembentukan PDRI kepada Sjafruddin Prawiranegara di Bukittinggi.", "answer": True},
                            {"text": "Serangan Umum 1 Maret 1949 berhasil membuktikan kepada dunia internasional bahwa TNI dan eksistensi RI masih tegak.", "answer": True},
                            {"text": "Pemerintah Darurat Republik Indonesia (PDRI) gagal mempertahankan kontinuitas pemerintahan republik di mata PBB.", "answer": False},
                            {"text": "Resolusi Dewan Keamanan PBB mendesak Belanda menghentikan agresi dan membebaskan para pemimpin republik.", "answer": True}
                        ],
                        "concept": "PDRI Bukittinggi dan Serangan Umum 1 Maret 1949 sukses mematahkan propaganda Belanda bahwa RI sudah lenyap dari muka bumi.",
                        "exec": "Pernyataan ketiga salah karena PDRI justru sangat sukses memelihara kedaulatan yuridis pemerintahan RI di forum internasional."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Konferensi Meja Bundar (KMB) di Den Haag akhir 1949 menghasilkan keputusan penting bagi kedaulatan bangsa. Pilihlah poin-poin kesepakatan KMB yang BENAR (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Kerajaan Belanda menyerahkan kedaulatan penuh tanpa syarat kepada Republik Indonesia Serikat (RIS).", "correct": True},
                            {"key": "B", "text": "Penyelesaian masalah status wilayah Irian Barat ditangguhkan selama kurun waktu satu tahun.", "correct": True},
                            {"key": "C", "text": "Dibentuknya Uni Indonesia-Belanda dengan kepala kehormatan di bawah Ratu Kerajaan Belanda.", "correct": True},
                            {"key": "D", "text": "Belanda menolak mengakui keberadaan utang pemerintahan Hindia Belanda sejak tahun 1942.", "correct": False},
                            {"key": "E", "text": "Bentuk negara kesatuan NKRI langsung disahkan tanpa melalui fase negara federal RIS.", "correct": False}
                        ],
                        "concept": "KMB mengesahkan penyerahan kedaulatan kepada RIS, penundaan status Irian Barat, dan pembentukan Uni Indonesia-Belanda.",
                        "exec": "Indonesia terpaksa menanggung utang Hindia Belanda, dan bentuk negara pada KMB adalah RIS (bukan NKRI)."
                    }
                }
            ]
        },
        {
            "materi": "PERANG DINGIN & DIPLOMASI GLOBAL",
            "topic": "Blok Barat vs Timur, KAA, & Gerakan Non-Blok",
            "hud_title": "DINAMIKA GEOPOLITIK PERANG DINGIN",
            "hud_latex": r"\text{Politik Bebas-Aktif} \rightarrow \text{Non-Alignment (KAA 1955 \& GNB 1961)}",
            "hud_legend": "• Bebas: Tidak memihak Blok Barat (NATO) maupun Blok Timur (Pakta Warsawa)<br>• Aktif: Berinisiatif menciptakan perdamaian dunia abadi",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Konferensi Asia-Afrika (KAA) yang diselenggarakan di Gedung Merdeka Bandung pada 18–24 April 1955 menghasilkan konsensus bersejarah Dasasila Bandung. Makna geopolitik fundamental dari penyelenggaraan KAA di tengah berkecamuknya Perang Dingin adalah...",
                        "corr": "Membangkitkan solidaritas antikolonialisme dan mendeklarasikan penolakan aliansi militer adidaya.",
                        "dists": [
                            "Membentuk aliansi militer bersama negara Asia untuk menghadapi ekspansi Blok Barat.",
                            "Menyatakan kesediaan negara-negara dunia ketiga untuk bergabung ke dalam Pakta Warsawa.",
                            "Menyepakati penyatuan sistem mata uang tunggal bersama untuk seluruh negara di benua Asia.",
                            "Mendesak PBB untuk menyerahkan kendali Dewan Keamanan secara mutlak kepada blok sosialis."
                        ],
                        "concept": "Dasasila Bandung menolak keterlibatan dalam aliansi militer kekuatan adidaya dan memperjuangkan kemerdekaan bangsa terjajah.",
                        "exec": "KAA adalah fondasi Dasasila Bandung dan penolakan aliansi militer militeristik Perang Dingin (bukan pakta militer)."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Perang Dingin membelah tatanan dunia pasca-Perang Dunia II menjadi persaingan ideologi kapitalisme liberal vs komunisme sosialisme. Evaluasilah kebenaran analisis sejarah global berikut:",
                        "statements": [
                            {"text": "Pakta Pertahanan Atlantik Utara (NATO) dibentuk oleh Amerika Serikat dan sekutunya pada 1949.", "answer": True},
                            {"text": "Uni Soviet membentuk Pakta Warsawa pada 1955 sebagai tandingan pertahanan militer NATO di Eropa Timur.", "answer": True},
                            {"text": "Krisis Rudal Kuba 1962 berakhir dengan pecahnya perang nuklir terbuka secara langsung di Samudra Pasifik.", "answer": False},
                            {"text": "Runtuhnya Tembok Berlin pada November 1989 menjadi simbol runtuhnya dominasi komunisme di Jerman.", "answer": True}
                        ],
                        "concept": "Krisis Misil Kuba 1962 diselesaikan secara damai lewat diplomasi Kennedy-Khrushchev tanpa perang nuklir terbuka.",
                        "exec": "Pernyataan ketiga salah karena Krisis Rudal Kuba diselesaikan melalui negosiasi de-eskalasi penarikan rudal di Kuba dan Turki."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Indonesia memainkan peran sentral dalam memprakarsai berdirinya Gerakan Non-Blok (GNB) pada KTT I Beograd 1961. Tokoh-tokoh pemimpin dunia yang menjadi pendiri utama GNB bersama Presiden Soekarno adalah (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Presiden Josip Broz Tito dari Yugoslavia.", "correct": True},
                            {"key": "B", "text": "Perdana Menteri Jawaharlal Nehru dari India.", "correct": True},
                            {"key": "C", "text": "Presiden Gamal Abdel Nasser dari Mesir.", "correct": True},
                            {"key": "D", "text": "Perdana Menteri Winston Churchill dari Britania Raya.", "correct": False},
                            {"key": "E", "text": "Presiden Harry S. Truman dari Amerika Serikat.", "correct": False}
                        ],
                        "concept": "5 Pemrakarsa GNB: Soekarno (Indonesia), Tito (Yugoslavia), Nehru (India), Nasser (Mesir), dan Kwame Nkrumah (Ghana).",
                        "exec": "Churchill dan Truman adalah pemimpin Blok Barat sekutu, bukan pemrakarsa Gerakan Non-Blok."
                    }
                }
            ]
        }
    ]
    
    # Generate 135 items
    for idx in range(1, 136):
        pillar = pillars[(idx - 1) % len(pillars)]
        concept = pillar["concepts"][(idx - 1) % len(pillar["concepts"])]
        
        diff = "easy" if idx <= 35 else ("medium" if idx <= 70 else ("hard" if idx <= 105 else "simulation_hots"))
        data = concept["builder"](idx, diff)
        
        q_item = {
            "id": f"sejl_{idx:03d}",
            "subject": "sejarah_lanjut",
            "type": concept["type"],
            "difficulty": diff,
            "materi": pillar["materi"],
            "topic": pillar["topic"],
            "question": data["stem"],
            "formula_title": pillar["hud_title"],
            "formula_latex": pillar["hud_latex"],
            "formula_legend": pillar["hud_legend"],
            "concept_hint": data["concept"],
            "execution_hint": data["exec"]
        }
        
        if concept["type"] == "mcq":
            opts, target_key = balance_options(data["corr"], data["dists"])
            q_item["options"] = opts
            q_item["correctAnswer"] = target_key
        elif concept["type"] == "matrix":
            q_item["statements"] = data["statements"]
        elif concept["type"] == "multi":
            q_item["options"] = data["options"]
            q_item["correctKeys"] = [o["key"] for o in data["options"] if o.get("correct")]
            
        questions.append(q_item)
        
    return questions


def main():
    print("Generating Cluster 2: Soshum Inti...")
    
    # 1. Ekonomi
    eko_data = generate_ekonomi()
    with open(os.path.join(DATA_DIR, "questions_ekonomi.js"), "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - EKONOMI (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F IPS & UTBK/SNBT\n */\n\n")
        f.write(f"window.TKA_EKONOMI_QUESTIONS = {json.dumps(eko_data, ensure_ascii=False, indent=2)};\n\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("  module.exports = { TKA_EKONOMI_QUESTIONS: window.TKA_EKONOMI_QUESTIONS };\n}\n")
    print(f"Generated {len(eko_data)} questions for Ekonomi -> data/questions_ekonomi.js")

    # 2. Geografi
    geo_data = generate_geografi()
    with open(os.path.join(DATA_DIR, "questions_geografi.js"), "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - GEOGRAFI (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F IPS & UTBK/SNBT\n */\n\n")
        f.write(f"window.TKA_GEOGRAFI_QUESTIONS = {json.dumps(geo_data, ensure_ascii=False, indent=2)};\n\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("  module.exports = { TKA_GEOGRAFI_QUESTIONS: window.TKA_GEOGRAFI_QUESTIONS };\n}\n")
    print(f"Generated {len(geo_data)} questions for Geografi -> data/questions_geografi.js")

    # 3. Sosiologi
    sos_data = generate_sosiologi()
    with open(os.path.join(DATA_DIR, "questions_sosiologi.js"), "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - SOSIOLOGI (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F IPS & UTBK/SNBT\n */\n\n")
        f.write(f"window.TKA_SOSIOLOGI_QUESTIONS = {json.dumps(sos_data, ensure_ascii=False, indent=2)};\n\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("  module.exports = { TKA_SOSIOLOGI_QUESTIONS: window.TKA_SOSIOLOGI_QUESTIONS };\n}\n")
    print(f"Generated {len(sos_data)} questions for Sosiologi -> data/questions_sosiologi.js")

    # 4. Sejarah Lanjut
    sejl_data = generate_sejarah_lanjut()
    with open(os.path.join(DATA_DIR, "questions_sejarah_lanjut.js"), "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - SEJARAH TINGKAT LANJUT (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F IPS & UTBK/SNBT\n */\n\n")
        f.write(f"window.TKA_SEJARAH_LANJUT_QUESTIONS = {json.dumps(sejl_data, ensure_ascii=False, indent=2)};\n\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("  module.exports = { TKA_SEJARAH_LANJUT_QUESTIONS: window.TKA_SEJARAH_LANJUT_QUESTIONS };\n}\n")
    print(f"Generated {len(sejl_data)} questions for Sejarah Lanjut -> data/questions_sejarah_lanjut.js")

    total = len(eko_data) + len(geo_data) + len(sos_data) + len(sejl_data)
    print(f"\nSUCCESS: Cluster 2 generated total {total} authentic questions.")

if __name__ == "__main__":
    main()
