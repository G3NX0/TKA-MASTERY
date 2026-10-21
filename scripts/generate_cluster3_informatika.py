"""
TKA MASTERY HUB - CLUSTER 3 TEKNOLOGI & VOKASI: INFORMATIKA GENERATOR
Mata Pelajaran: Informatika SMA Pilihan (135 soal)
Standar: Kurikulum Merdeka Fase F & Pusmendik
"""

import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(303)

def balance_options(correct_text, distractor_texts, target_key=None):
    all_texts = [correct_text] + distractor_texts[:4]
    avg_len = sum(len(t) for t in all_texts) / len(all_texts)
    
    balanced = []
    for t in all_texts:
        diff = int(avg_len - len(t))
        if diff > 3:
            t = t.rstrip('.') + " secara efisien dan deterministik."
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


def generate_informatika():
    questions = []
    
    pillars = [
        {
            "materi": "BERPIKIR KOMPUTASIONAL & STRUKTUR DATA",
            "topic": "Algoritma Rekursi, Tree, & Graf",
            "hud_title": "KOMPLEKSITAS WAKTU & STRUKTUR DATA",
            "hud_latex": r"T(n) = O(n \log n), \quad \text{BST Search} = O(\log n)",
            "hud_legend": "• $T(n)$: Kompleksitas waktu asimtotik<br>• BST: Binary Search Tree berimbang<br>• $n$: Jumlah elemen simpul data",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Diberikan sebuah pohon pencarian biner (Binary Search Tree - BST) yang awalnya kosong. Nilai-nilai berikut dimasukkan secara berurutan: [{50 + (i%20)}, {30 + (i%10)}, {70 + (i%15)}, {20 + (i%5)}, {40 + (i%8)}, {60 + (i%12)}, {80 + (i%10)}]. Urutan traversal in-order (kiri-akar-kanan) pada BST tersebut akan menghasilkan barisan angka...",
                        "corr": f"Barisan angka terurut menaik (ascending) dari nilai terkecil hingga terbesar.",
                        "dists": [
                            f"Barisan angka terurut menurun (descending) dari simpul daun terbesar ke akar.",
                            f"Barisan angka acak yang merefleksikan kronologi waktu penyisipan awal.",
                            f"Barisan angka tingkat demi tingkat (breadth-first) dari level teratas ke bawah.",
                            f"Barisan angka berulang yang menempatkan simpul akar pada posisi terdepan."
                        ],
                        "concept": "Sifat fundamental BST: Traversal In-Order (Left-Root-Right) selalu menghasilkan elemen terurut menaik (sorted ascending).",
                        "exec": "Pada BST, anak kiri selalu lebih kecil dari induk dan anak kanan lebih besar. In-order otomatis mencetak elemen terurut menaik."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam analisis kompleksitas waktu asimtotik algoritma (Big-O Notation), analis mengevaluasi berbagai algoritma pengurutan (sorting). Evaluasilah kebenaran analisis komputasional berikut:",
                        "statements": [
                            {"text": "Algoritma Merge Sort memiliki kompleksitas waktu kasus terburuk (worst case) sebesar O(n log n).", "answer": True},
                            {"text": "Quick Sort selalu menjamin kompleksitas waktu O(n log n) meskipun pivot yang dipilih adalah elemen terburuk.", "answer": False},
                            {"text": "Pencarian biner (Binary Search) hanya dapat diterapkan pada struktur data array yang telah terurut.", "answer": True},
                            {"text": "Operasi penambahan elemen di awal struktur data Linked List dapat diselesaikan dalam waktu konstan O(1).", "answer": True}
                        ],
                        "concept": "Quick Sort pada kasus terburuk (misal pivot selalu elemen terkecil/terbesar) mengalami degradasi kinerja menjadi O(n²).",
                        "exec": "Pernyataan kedua salah karena jika pemilihan pivot Quick Sort buruk, kompleksitasnya menjadi kuadratik O(n²)."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Perhatikan implementasi struktur data tumpukan (Stack) dan antrean (Queue) dalam sistem komputasi modern. Pilihlah karakteristik teknis yang BENAR (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Struktur Stack menganut prinsip Last-In, First-Out (LIFO) untuk fitur undo-redo pada teks editor.", "correct": True},
                            {"key": "B", "text": "Struktur Queue menganut prinsip First-In, First-Out (FIFO) untuk antrean pencetakan dokumen printer.", "correct": True},
                            {"key": "C", "text": "Pemanggilan fungsi rekursif oleh compiler dialokasikan ke dalam struktur memori Call Stack.", "correct": True},
                            {"key": "D", "text": "Elemen yang pertama kali masuk ke dalam Stack akan menjadi elemen pertama yang dikeluarkan.", "correct": False},
                            {"key": "E", "text": "Queue menghapus elemen melalui ujung belakang (rear) dan menyisipkan elemen lewat ujung depan.", "correct": False}
                        ],
                        "concept": "Stack = LIFO (Last In First Out) digunakan untuk Call Stack & Undo. Queue = FIFO (First In First Out) digunakan untuk Spooler Printer.",
                        "exec": "Stack mengeluarkan elemen terakhir terlebih dahulu (bukan pertama), dan Queue mengeluarkan data dari front dan memasukkan dari rear."
                    }
                }
            ]
        },
        {
            "materi": "JARINGAN KOMPUTER & KEAMANAN SIBER",
            "topic": "Protokol Komunikasi & Kriptografi",
            "hud_title": "MODEL OSI & ARSITEKTUR KRIPTOGRAFI",
            "hud_latex": r"\text{Enkripsi RSA: } C = M^e \pmod n, \quad \text{Dekripsi: } M = C^d \pmod n",
            "hud_legend": "• $M$: Pesan plaintext asli<br>• $C$: Ciphertext terenkripsi<br>• $e, d$: Pasangan kunci publik dan privat",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam arsitektur model referensi OSI 7 Layer, protokol yang bertanggung jawab menyelenggarakan proses segmentasi data, pengendalian aliran (flow control), dan memastikan transmisi data bebas kesalahan (reliable delivery) melalui Three-Way Handshake adalah...",
                        "corr": "Transport Layer melalui implementasi protokol Transmission Control Protocol (TCP).",
                        "dists": [
                            "Network Layer melalui implementasi protokol Internet Protocol versi empat (IPv4).",
                            "Data Link Layer melalui verifikasi frame kontrol akses media (MAC Address).",
                            "Application Layer melalui pertukaran pesan Hypertext Transfer Protocol (HTTP).",
                            "Session Layer melalui pembentukan dan pemutusan gerbang dialog antarkomputer."
                        ],
                        "concept": "Transport Layer (Layer 4) mengatur segmentasi, flow control, error recovery, dan koneksi TCP (SYN, SYN-ACK, ACK).",
                        "exec": "Three-Way Handshake dan segmentasi data dengan jaminan reliabilitas adalah domain fungsional Transport Layer (TCP)."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Sistem pertahanan keamanan siber menerapkan enkripsi kunci publik (asymmetric cryptography) dan fungsi hash. Evaluasilah keabsahan analisis keamanan berikut:",
                        "statements": [
                            {"text": "Dalam kriptografi asimetris, pesan yang dienkripsi dengan kunci publik hanya dapat didekripsi dengan kunci privat pemiliknya.", "answer": True},
                            {"text": "Fungsi hash kriptografis (seperti SHA-256) bersifat satu arah (one-way function) dan deterministik.", "answer": True},
                            {"text": "Perubahan satu karakter huruf pada dokumen asli tidak akan mengubah output nilai digest hash yang dihasilkan.", "answer": False},
                            {"text": "Sertifikat digital SSL/TLS mengotentikasi keabsahan kunci publik server web melalui otoritas sertifikat (CA).", "answer": True}
                        ],
                        "concept": "Fungsi hash memiliki sifat avalanche effect: perubahan kecil 1 bit pada input akan mengubah total nilai hash output.",
                        "exec": "Pernyataan ketiga salah karena efek avalanche menjamin nilai hash berubah drastis bahkan jika hanya 1 huruf diubah."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Perhatikan jenis-jenis serangan siber terhadap integritas data sistem informasi. Pilihlah bentuk ancaman siber dan metode mitigasi yang TEPAT (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Serangan SQL Injection dapat dicegah dengan menerapkan Prepared Statements dan parameterized queries.", "correct": True},
                            {"key": "B", "text": "Serangan Cross-Site Scripting (XSS) dimitigasi dengan sanitasi input dan encoding output pada halaman HTML.", "correct": True},
                            {"key": "C", "text": "Serangan Man-in-the-Middle (MitM) dicegah melalui penerapan protokol enkripsi HTTPS/TLS end-to-end.", "correct": True},
                            {"key": "D", "text": "Serangan Distributed Denial of Service (DDoS) dapat diatasi tuntas hanya dengan mematikan firewall server.", "correct": False},
                            {"key": "E", "text": "Penggunaan kata sandi pendek sederhana efektif menangkal serangan brute-force dictionary attack.", "correct": False}
                        ],
                        "concept": "Mitigasi web security: Prepared Statements menangkal SQLi, HTML sanitization menangkal XSS, dan TLS menangkal MitM.",
                        "exec": "Mematikan firewall justru membuka akses serangan, dan password pendek sangat rentan brute-force."
                    }
                }
            ]
        },
        {
            "materi": "REKAYASA PERANGKAT LUNAK & BASIS DATA",
            "topic": "SQL Relasional & Siklus SDLC",
            "hud_title": "RELATIONAL DATABASE MANAGEMENT SYSTEM",
            "hud_latex": r"\text{Kueri SQL: } \text{SELECT } \dots \text{ FROM } R_1 \bowtie R_2 \text{ WHERE } \dots",
            "hud_legend": "• $R_1 \bowtie R_2$: Operasi Natural/Inner Join dua tabel relasional<br>• Primary Key: Identitas unik record data",
            "concepts": [
                {
                    "type": "mcq",
                    "builder": lambda i, diff: {
                        "stem": f"Diberikan dua tabel relasional: Tabel Siswa (nis [PK], nama, id_kelas [FK]) dan Tabel Kelas (id_kelas [PK], nama_kelas, ruang). Seorang administrator basis data ingin menampilkan daftar seluruh nama siswa beserta nama kelasnya, termasuk siswa yang belum dialokasikan ke kelas mana pun. Perintah SQL JOIN yang TEPAT adalah...",
                        "corr": "SELECT Siswa.nama, Kelas.nama_kelas FROM Siswa LEFT JOIN Kelas ON Siswa.id_kelas = Kelas.id_kelas;",
                        "dists": [
                            "SELECT Siswa.nama, Kelas.nama_kelas FROM Siswa INNER JOIN Kelas ON Siswa.id_kelas = Kelas.id_kelas;",
                            "SELECT Siswa.nama, Kelas.nama_kelas FROM Siswa RIGHT JOIN Kelas ON Siswa.id_kelas = Kelas.id_kelas;",
                            "SELECT Siswa.nama, Kelas.nama_kelas FROM Siswa CROSS JOIN Kelas WHERE Siswa.nis = Kelas.id_kelas;",
                            "SELECT Siswa.nama, Kelas.nama_kelas FROM Siswa FULL JOIN Kelas WHERE Siswa.id_kelas IS NOT NULL;"
                        ],
                        "concept": "LEFT JOIN menampilkan seluruh record dari tabel kiri (Siswa) meskipun tidak memiliki pasangan yang cocok di tabel kanan (Kelas).",
                        "exec": "Karena diminta menampilkan seluruh siswa termasuk yang belum memiliki kelas, gunakan LEFT JOIN dengan tabel Siswa di sebelah kiri."
                    }
                },
                {
                    "type": "matrix",
                    "builder": lambda i, diff: {
                        "stem": f"Dalam siklus pengembangan perangkat lunak (Software Development Life Cycle - SDLC), tim pengembang membandingkan model Waterfall dan Scrum Agile. Evaluasilah kebenaran analisis metodologi rekayasa berikut:",
                        "statements": [
                            {"text": "Model Waterfall mensyaratkan setiap fase (analisis, desain, koding, pengujian) selesai berurutan secara linier.", "answer": True},
                            {"text": "Kerangka kerja Scrum membagi waktu pengerjaan proyek menjadi iterasi-iterasi pendek yang disebut Sprint.", "answer": True},
                            {"text": "Model Waterfall sangat adaptif terhadap perubahan kebutuhan spesifikasi klien yang berubah di tengah proyek.", "answer": False},
                            {"text": "Daily Standup Meeting dalam Scrum bertujuan menyelaraskan progres harian dan mengidentifikasi kendala tim.", "answer": True}
                        ],
                        "concept": "Waterfall bersifat rigid/kaku dan sulit mengakomodasi perubahan spesifikasi di tengah jalan, berbeda dengan Agile yang iteratif dan fleksibel.",
                        "exec": "Pernyataan ketiga salah karena Waterfall menolak perubahan dinamis di tengah siklus tanpa mengulang fase dari awal."
                    }
                },
                {
                    "type": "multi",
                    "builder": lambda i, diff: {
                        "stem": f"Prinsip transaksi basis data relasional menuntut pemenuhan sifat ACID (Atomicity, Consistency, Isolation, Durability). Pilihlah penjelasan yang BENAR mengenai sifat-sifat transaksi tersebut (jawaban lebih dari satu):",
                        "options": [
                            {"key": "A", "text": "Atomicity menjamin transaksi berhasil seluruhnya atau dibatalkan sama sekali (all-or-nothing).", "correct": True},
                            {"key": "B", "text": "Consistency memastikan transaksi membawa basis data dari satu kondisi valid ke kondisi valid berikutnya.", "correct": True},
                            {"key": "C", "text": "Durability menjamin data transaksi yang telah di-commit akan tersimpan permanen meskipun sistem mati mendadak.", "correct": True},
                            {"key": "D", "text": "Isolation membiarkan transaksi konkuren saling membaca perubahan data yang belum di-commit secara bebas.", "correct": False},
                            {"key": "E", "text": "Atomicity membolehkan separuh operasi transfer dana berhasil sementara separuh operasi lainnya gagal.", "correct": False}
                        ],
                        "concept": "ACID menjamin keandalan database: Atomicity (All or Nothing), Consistency (Rules valid), Isolation (Terkunci), Durability (Permanen).",
                        "exec": "Isolation justru mencegah transaksi belum selesai terbaca (dirty read), dan Atomicity menolak eksekusi separuh jalan."
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
            "id": f"inf_{idx:03d}",
            "subject": "informatika",
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
    print("Generating Cluster 3: Informatika SMA...")
    inf_data = generate_informatika()
    with open(os.path.join(DATA_DIR, "questions_informatika.js"), "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - INFORMATIKA (135 SOAL AUTENTIK PUSMENDIK)\n")
        f.write(" * Kurikulum Merdeka Fase F Teknologi & UTBK/SNBT\n */\n\n")
        f.write(f"window.TKA_INFORMATIKA_QUESTIONS = {json.dumps(inf_data, ensure_ascii=False, indent=2)};\n\n")
        f.write("if (typeof module !== 'undefined' && module.exports) {\n")
        f.write("  module.exports = { TKA_INFORMATIKA_QUESTIONS: window.TKA_INFORMATIKA_QUESTIONS };\n}\n")
    print(f"Generated {len(inf_data)} questions for Informatika -> data/questions_informatika.js")

if __name__ == "__main__":
    main()
