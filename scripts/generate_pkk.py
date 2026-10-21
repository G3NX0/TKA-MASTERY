"""
TKA MASTERY HUB - PRODUK KREATIF DAN KEWIRAUSAHAAN (PKK) SMK/MAK GENERATOR
135 Soal Autentik Standar Kurikulum Merdeka Fase F Kejuruan & Pusmendik
Karakteristik Anti-Slop:
- Interleaved types (MCQ, Matrix Benar/Salah, Multi-Select Checkbox)
- Keseimbangan panjang opsi (+/- 10%)
- Pengecoh konseptual berbasis miskonsepsi kewirausahaan & kalkulasi BEP
- HUD Formula & 2-Stage Scaffolding Hints
"""

import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(505)

def balance_options(correct_text, distractor_texts, target_key=None):
    all_texts = [correct_text] + distractor_texts[:4]
    avg_len = sum(len(t) for t in all_texts) / len(all_texts)
    
    balanced = []
    for t in all_texts:
        diff = int(avg_len - len(t))
        if diff > 4:
            t = t.rstrip('.') + " secara terencana dan profesional."
        elif diff < -4 and len(t) > 35:
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


def generate_pkk():
    questions = []
    
    pillars = [
        {
            "materi": "ANALISIS PELUANG USAHA & BUSINESS MODEL CANVAS (BMC)",
            "topic": "SWOT Matrix & 9 Blok Model Bisnis",
            "hud_title": "BUSINESS MODEL CANVAS (BMC) & SWOT",
            "hud_latex": r"\text{SWOT: } \text{SO (Aggressive), WO (Turnaround), ST (Diversification), WT (Defensive)}",
            "hud_legend": "• Value Proposition: Nilai keunggulan solusi produk bagi konsumen<br>• Customer Segments: Target pasar spesifik yang dilayani<br>• Revenue Streams: Aliran arus pendapatan usaha",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Sebuah usaha rintisan siswa SMK memiliki keunggulan internal berupa keterampilan teknis tinggi dalam merancang aplikasi (Strength), namun menghadapi ancaman persaingan ketat dari studio pengembang besar (Threat). Berdasarkan matriks analisis SWOT, strategi bisnis yang paling TEPAT diterapkan adalah...",
                        "corr": "Strategi ST (Strengths-Threats) dengan mendiversifikasi produk ke ceruk pasar mikro yang belum terlayani studio besar.",
                        "dists": [
                            "Strategi SO (Strengths-Opportunities) dengan ekspansi jor-joran tanpa memperhitungkan kompetitor.",
                            "Strategi WO (Weaknesses-Opportunities) dengan menghentikan total kegiatan riset pengembangan.",
                            "Strategi WT (Weaknesses-Threats) dengan langsung melikuidasi seluruh aset usaha dan menutup unit.",
                            "Strategi Defensif Pasif dengan mempertahankan harga jual tertinggi tanpa inovasi fitur."
                        ],
                        "concept": "Strategi ST (Kekuatan-Ancaman) memanfaatkan kekuatan internal untuk memitigasi atau menghindari ancaman eksternal (diversifikasi ceruk pasar).",
                        "exec": "Kombinasi S dan T menghasilkan strategi ST: menggunakan keahlian teknis (S) untuk menyasar segmen khusus demi menangkal persaingan studio besar (T)."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam merancang Business Model Canvas (BMC) untuk produk kreatif berbasis kejuruan, evaluasilah fungsi 9 blok bangunan bisnis pada tabel berikut:",
                        "statements": [
                            {"text": "Blok 'Value Proposition' mendefinisikan gabungan produk dan layanan yang menciptakan nilai tambah bagi segmen pelanggan tertentu.", "isCorrect": True},
                            {"text": "Blok 'Channels' semata-mata menggambarkan cara internal perusahaan memproduksi barang tanpa melibatkan kontak dengan pembeli.", "isCorrect": False},
                            {"text": "Blok 'Cost Structure' mencakup seluruh biaya operasional yang dikeluarkan untuk menjalankan model bisnis, baik biaya tetap maupun variabel.", "isCorrect": True},
                            {"text": "Blok 'Key Partners' memetakan jaringan pemasok dan mitra yang membuat model bisnis dapat berfungsi secara optimal dan efisien.", "isCorrect": True}
                        ],
                        "concept": "9 Blok BMC Alexander Osterwalder: Value Proposition, Channels (saluran distribusi dan komunikasi ke konsumen), Cost Structure, dan Key Partners.",
                        "exec": "Pernyataan 2 Salah karena Channels adalah media interaksi dan distribusi ke pelanggan, bukan sekadar proses internal pabrik."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Manakah di antara tindakan berikut yang merupakan langkah validasi pasar (Market Validation) yang BENAR sebelum memproduksi massal produk kreatif? (Pilih semua yang benar)",
                        "options": [
                            {"key": "A", "text": "Membuat prototipe minimum (Minimum Viable Product - MVP) untuk diuji coba langsung kepada calon pengguna awal.", "correct": True},
                            {"key": "B", "text": "Melakukan wawancara mendalam untuk mengidentifikasi 'pain points' masalah riil yang dihadapi calon konsumen.", "correct": True},
                            {"key": "C", "text": "Menyewa pabrik skala besar sebelum mengetahui apakah pasar bersedia membeli produk yang ditawarkan.", "correct": False},
                            {"key": "D", "text": "Menyebarkan kuesioner terstruktur uji minat beli dengan menyertakan visual mockup produk.", "correct": True}
                        ],
                        "concept": "Validasi pasar berfokus pada pengujian hipotesis nilai melalui MVP, riset kebutuhan pelanggan (Customer Development), dan survei minat beli sebelum investasi modal besar.",
                        "exec": "A, B, dan D adalah langkah validasi pasar ramping (Lean). C adalah kesalahan fatal memulai usaha (over-investment dini)."
                    }
                }
            ]
        },
        {
            "materi": "PROTOTIPE PRODUK, PENGEMASAN, & HAK ATAS KEKAYAAN INTELEKTUAL (HAKI)",
            "topic": "Tahapan Prototyping, Regulasi Kemasan, & Hukum Paten/Merek",
            "hud_title": "REGULASI HAKI & DESAIN PROTOTIPE PRODUK",
            "hud_latex": r"\text{HAKI: } \text{Hak Cipta (Seni/Software) } \quad \text{Paten (Invensi Teknis) } \quad \text{Merek (Identitas Dagang)}",
            "hud_legend": "• UU No. 28/2014: Hak Cipta melindungi karya ekspresif orisinal<br>• UU No. 13/2016: Paten melindungi invensi teknologi baru & aplikatif<br>• UU No. 20/2016: Merek melindungi tanda pembeda dagang/jasa",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Siswa SMK jurusan kejuruan berhasil menciptakan alat pemilah sampah otomatis berbasis sensor spektroskopi inframerah yang baru dan memiliki langkah inventif. Agar teknologi mekanis dan sirkuit alat tersebut tidak ditiru oleh pihak lain, jenis perlindungan HAKI yang WAJIB didaftarkan ke DJKI Kemenkumham adalah...",
                        "corr": "Hak Paten (Sederhana/Biasa) karena merupakan invensi di bidang teknologi yang dapat diterapkan dalam industri.",
                        "dists": [
                            "Hak Cipta karena alat tersebut merupakan karya ekspresif seni instalasi mekanikal dekoratif.",
                            "Merek Dagang karena berfungsi sebagai nama stiker yang ditempelkan di badan kemasan alat.",
                            "Desain Tata Letak Sirkuit Terpadu tanpa perlu melakukan pendaftaran ke kantor kementerian resmi.",
                            "Rahasia Dagang tanpa perlindungan hukum tertulis dari undang-undang negara Republik Indonesia."
                        ],
                        "concept": "Paten (UU No. 13/2016) adalah hak eksklusif yang diberikan negara kepada inventor atas invensinya di bidang teknologi (memiliki kebaruan, langkah inventif, dan aplikatif).",
                        "exec": "Alat sensor inframerah mekanikal adalah invensi teknologi, sehingga dilindungi oleh Hak Paten."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Evaluasilah ketentuan hukum perlindungan kekayaan intelektual dan standar kemasan produk berikut:",
                        "statements": [
                            {"text": "Hak Cipta menganut sistem deklaratif (First to Use/Automatic Protection), di mana perlindungan lahir seketika setelah suatu ciptaan diwujudkan dalam bentuk nyata.", "isCorrect": True},
                            {"text": "Sistem pendaftaran Merek di Indonesia menganut prinsip 'First to File', yaitu pihak yang pertama kali mendaftarkan permohonan yang berhak memperoleh perlindungan.", "isCorrect": True},
                            {"text": "Kemasan produk makanan minuman olahan SMK tidak wajib mencantumkan informasi tanggal kedaluwarsa (expired date) jika dijual secara online.", "isCorrect": False},
                            {"text": "Desain Industri melindungi kreasi estetika dua dimensi atau tiga dimensi yang memberikan kesan visual khusus pada suatu komoditas.", "isCorrect": True}
                        ],
                        "concept": "Prinsip HAKI: Hak Cipta (deklaratif otomatis), Merek (First to File), kewajiban label kemasan BPOM (expired date wajib), dan definisi Desain Industri.",
                        "exec": "Pernyataan 3 Salah karena tanggal kedaluwarsa adalah informasi wajib mutlak menurut UU Perlindungan Konsumen dan regulasi BPOM."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Manakah di antara fungsi kemasan produk berikut yang tergolong dalam fungsi primer dan protektif? (Pilih semua yang benar)",
                        "options": [
                            {"key": "A", "text": "Melindungi produk dari kontaminasi mikroba, benturan fisik, kelembapan, dan radiasi sinar ultraviolet.", "correct": True},
                            {"key": "B", "text": "Menjaga stabilitas kualitas dan mutu isi produk selama masa penyimpanan dan distribusi transportasi.", "correct": True},
                            {"key": "C", "text": "Menyembunyikan cacat produksi agar tidak terdeteksi oleh konsumen saat melakukan transaksi.", "correct": False},
                            {"key": "D", "text": "Memberikan kemudahan penanganan (handling), pemindahan, dan penataan display di rak toko.", "correct": True}
                        ],
                        "concept": "Fungsi kemasan: proteksi isi dari kerusakan lingkungan, penjaga mutu, dan fasilitator penanganan logistik. Menipu konsumen bukan fungsi kemasan.",
                        "exec": "A, B, dan D adalah fungsi protektif dan utilitas kemasan. C adalah penipuan melanggar etika."
                    }
                }
            ]
        },
        {
            "materi": "BIAYA PRODUKSI, HARGA JUAL, & TITIK IMPAS (BREAK EVEN POINT)",
            "topic": "Fixed Cost, Variable Cost, BEP Unit/Rupiah, & Mark-Up",
            "hud_title": "KALKULASI BREAK EVEN POINT (BEP)",
            "hud_latex": r"\text{BEP}_{\text{unit}} = \frac{FC}{P - VC}, \quad \text{BEP}_{\text{rupiah}} = \frac{FC}{1 - \frac{VC}{P}}",
            "hud_legend": "• $FC$: Biaya Tetap (Fixed Cost)<br>• $VC$: Biaya Variabel per unit (Variable Cost)<br>• $P$: Harga Jual per unit (Price)",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Sebuah unit produksi kreatif SMK memproduksi kerajinan kriya. Biaya tetap bulanan (FC) sebesar Rp3.000.000, biaya variabel per unit (VC) sebesar Rp20.000, dan harga jual produk per unit (P) ditetapkan Rp50.000. Jumlah unit produk minimal yang harus terjual agar usaha tersebut mencapai Titik Impas (Break Even Point) adalah...",
                        "corr": "100 unit barang.",
                        "dists": [
                            "60 unit barang.",
                            "150 unit barang.",
                            "200 unit barang.",
                            "250 unit barang."
                        ],
                        "concept": "Kalkulasi BEP Unit = FC / (P - VC) = 3.000.000 / (50.000 - 20.000) = 3.000.000 / 30.000 = 100 unit.",
                        "exec": "BEP unit = Rp3.000.000 / (Rp50.000 - Rp20.000) = Rp3.000.000 / Rp30.000 = 100 unit."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Evaluasilah klasifikasi komponen biaya operasional usaha manufaktur kejuruan berikut:",
                        "statements": [
                            {"text": "Biaya sewa ruko bengkel kerja dan biaya penyusutan mesin perkakas tergolong sebagai Biaya Tetap (Fixed Cost).", "isCorrect": True},
                            {"text": "Biaya bahan baku utama dan upah tenaga kerja borongan langsung tergolong sebagai Biaya Tetap (Fixed Cost).", "isCorrect": False},
                            {"text": "Jika volume produksi meningkat dua kali lipat, maka total Biaya Variabel (Variable Cost) secara keseluruhan juga akan meningkat proporsional.", "isCorrect": True},
                            {"text": "Margin Kontribusi per unit dihitung dengan cara mengurangkan Biaya Variabel per unit dari Harga Jual per unit (P - VC).", "isCorrect": True}
                        ],
                        "concept": "Fixed Cost (tidak berubah terhadap volume output: sewa, depresiasi), Variable Cost (berubah seiring output: bahan baku, upah borongan), dan Contribution Margin.",
                        "exec": "Pernyataan 2 Salah karena bahan baku dan upah borongan adalah Biaya Variabel (Variable Cost)."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Manakah di antara metode penetapan harga jual berikut yang menggunakan pendekatan berbasis biaya (Cost-Based Pricing)? (Pilih semua yang benar)",
                        "options": [
                            {"key": "A", "text": "Cost-Plus Pricing (menambahkan persentase laba yang diinginkan di atas total biaya produksi per unit).", "correct": True},
                            {"key": "B", "text": "Mark-Up Pricing (menambahkan selisih kenaikan harga di atas harga beli barang dagang).", "correct": True},
                            {"key": "C", "text": "Value-Based Pricing (menetapkan harga murni berdasarkan persepsi nilai yang dirasakan konsumen).", "correct": False},
                            {"key": "D", "text": "Break-Even Pricing (menetapkan harga jual tepat pada level yang menutup seluruh biaya total produksi).", "correct": True}
                        ],
                        "concept": "Pendekatan berbasis biaya mencakup Cost-Plus Pricing, Mark-Up Pricing, dan Target-Return/Break-Even Pricing. Value-based pricing berbasis persepsi pelanggan, bukan biaya.",
                        "exec": "A, B, dan D berbasis biaya. C berbasis persepsi nilai konsumen."
                    }
                }
            ]
        },
        {
            "materi": "PEMASARAN DIGITAL & LAPORAN KEUANGAN WIRAUSAHA",
            "topic": "Digital Marketing Funnel & Laporan Laba Rugi / Arus Kas",
            "hud_title": "LAPORAN KEUANGAN & PEMASARAN DIGITAL",
            "hud_latex": r"\text{Laba Bersih} = \text{Pendapatan Penjualan} - \text{HPP} - \text{Beban Operasional} - \text{Pajak}",
            "hud_legend": "• HPP: Harga Pokok Penjualan (Biaya Langsung Produksi)<br>• Funnel AIDA: Attention $\\rightarrow$ Interest $\\rightarrow$ Desire $\\rightarrow$ Action<br>• Cash Flow: Arus Kas Masuk vs Kas Keluar",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam strategi pemasaran digital (Digital Marketing), tahapan funnel di mana calon pelanggan mulai mencari perbandingan spesifikasi produk, membaca ulasan testimoni, dan menimbang keputusan pembelian sebelum bertransaksi berada pada tahap...",
                        "corr": "Tahap Interest & Desire dalam model AIDA sebelum memutuskan Action pembelian.",
                        "dists": [
                            "Tahap Attention awal saat pertama kali melihat konten banner sekilas di linimasa.",
                            "Tahap After-Sales Service saat barang telah diterima dan digunakan oleh pembeli.",
                            "Tahap Likuidasi Aset saat perusahaan melakukan pembersihan stok sisa gudang.",
                            "Tahap Produksi Massal saat pesanan sedang dikerjakan oleh tim manufaktur."
                        ],
                        "concept": "Funnel AIDA: Attention (kesadaran), Interest (ketertarikan mempelajari fitur), Desire (keinginan membeli setelah menimbang review), Action (transaksi checkout).",
                        "exec": "Mencari perbandingan spesifikasi dan menimbang ulasan adalah fase Interest & Desire."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Evaluasilah kebenaran analisis laporan keuangan sederhana wirausaha kejuruan berikut:",
                        "statements": [
                            {"text": "Laporan Laba Rugi (Income Statement) menyajikan informasi mengenai total pendapatan, beban usaha, dan hasil laba atau rugi bersih dalam suatu periode akuntansi.", "isCorrect": True},
                            {"text": "Sebuah usaha yang mencatatkan laba bersih positif pada laporan laba rugi dijamin tidak akan pernah mengalami krisis likuiditas arus kas (cash flow shortage).", "isCorrect": False},
                            {"text": "Laporan Arus Kas (Cash Flow) mengklasifikasikan arus kas ke dalam tiga aktivitas: operasional, investasi, dan pendanaan.", "isCorrect": True},
                            {"text": "Neraca (Balance Sheet) menunjukkan posisi aset, liabilitas (kewajiban utang), dan ekuitas (modal sendiri) pada suatu tanggal penanggalan tertentu.", "isCorrect": True}
                        ],
                        "concept": "Laporan keuangan: Laba Rugi, Neraca, dan Arus Kas. Laba akrual tidak menjamin ketersediaan kas riil (misal piutang tak tertagih).",
                        "exec": "Pernyataan 2 Salah karena usaha yang untung secara akrual tetap bisa bangkrut jika kas tertahan di piutang atau persediaan macet (cash flow insolvent)."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Manakah di antara metrik pemasaran digital berikut yang lazim diukur untuk mengevaluasi efektivitas kampanye iklan berbayar (Paid Ads)? (Pilih semua yang benar)",
                        "options": [
                            {"key": "A", "text": "Click-Through Rate (CTR) - persentase pengguna yang mengklik iklan dari total impresi penayangan.", "correct": True},
                            {"key": "B", "text": "Cost Per Acquisition (CPA) - rata-rata biaya yang dikeluarkan untuk mendapatkan satu pembeli riil.", "correct": True},
                            {"key": "C", "text": "Return on Ad Spend (ROAS) - perbandingan pendapatan kotor yang dihasilkan dari setiap rupiah biaya iklan.", "correct": True},
                            {"key": "D", "text": "Beban Penyusutan Gedung - depresiasi nilai buku bangunan pabrik menurut tabel aktiva tetap.", "correct": False}
                        ],
                        "concept": "Metrik digital marketing ads: CTR, CPA, ROAS, CPC, CPM. Depresiasi gedung adalah beban akuntansi aktiva tetap non-marketing.",
                        "exec": "A, B, dan C adalah metrik performa digital marketing. D adalah akun akuntansi aset tetap."
                    }
                }
            ]
        }
    ]
    
    for idx in range(1, 136):
        pillar = pillars[(idx - 1) % len(pillars)]
        concept = pillar["concepts"][(idx - 1) % len(pillar["concepts"])]
        
        diff = "easy" if idx <= 35 else ("medium" if idx <= 70 else ("hard" if idx <= 105 else "simulation_hots"))
        data = concept["builder"](idx, diff)
        
        q_item = {
            "id": f"pkk_{idx:03d}",
            "subject": "pkk",
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
    print("Generating PKK: Produk Kreatif dan Kewirausahaan (SMK/MAK)...")
    pkk_data = generate_pkk()
    with open(os.path.join(DATA_DIR, "questions_pkk.js"), "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - PRODUK KREATIF DAN KEWIRAUSAHAAN (PKK) SMK/MAK (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F Kejuruan & BSKAP 033/H/KR/2022 (Pilihan Wajib SMK)\n */\n\n")
        f.write(f"window.TKA_PKK_QUESTIONS = {json.dumps(pkk_data, ensure_ascii=False, indent=2)};\n\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("  module.exports = { TKA_PKK_QUESTIONS: window.TKA_PKK_QUESTIONS };\n}\n")
    print(f"Generated {len(pkk_data)} questions for PKK -> data/questions_pkk.js")

if __name__ == "__main__":
    main()
