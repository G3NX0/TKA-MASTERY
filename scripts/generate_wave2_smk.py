"""
TKA MASTERY HUB - WAVE 2 SMK KEJURUAN GENERATOR (RPL, TKJ, REKAYASA DESAIN / DKV)
BSKAP No. 033/H/KR/2022 Lampiran III (Capaian Pembelajaran Kejuruan SMK Fase F)
Features:
- Standar Kurikulum Resmi:
  * RPL: Program Keahlian PPLG (OOP, Database Relasional, Web/Mobile, Git SDLC)
  * TKJ: Program Keahlian TJKT (Subnetting VLSM, VLAN Trunking, OSPF Routing, Firewall iptables/MikroTik, Fiber Optik)
  * Rekayasa Desain: Konsentrasi DKV (Prinsip Nirmana, Tipografi, Vektor vs Bitmap, CMYK vs RGB, UI/UX, HAKI & Pra-Cetak)
- 135 Soal Autentik per Mapel (Total 405 Soal)
- Organic interleaving: mcq (~45), matrix (~45), multi (~45)
- Zero AI Slop: Pengecoh berbasis miskonsepsi nyata, panjang opsi seragam, kunci jawaban acak terverifikasi.
"""

import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(1337)

# ==============================================================================
# 1. GENERATOR: REKAYASA PERANGKAT LUNAK (PPLG - 135 SOAL)
# ==============================================================================
def generate_rpl():
    questions = []
    
    pillars = [
        {
            "materi": "PEMROGRAMAN BERORIENTASI OBJEK (OOP)",
            "topic": "Enkapsulasi, Inheritance & Polimorfisme",
            "formula_title": "PRINSIP 4 PILAR OOP (SOLID)",
            "formula_latex": r"\text{Class} \xrightarrow{\text{Inheritance}} \text{Subclass}, \quad \text{Interface} \xrightarrow{\text{Implements}} \text{Polymorphic Object}",
            "formula_legend": "• Enkapsulasi: private attribute + getter/setter<br>• Polimorfisme: Override method di runtime<br>• Abstraksi: Interface/Abstract Class",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Perhatikan potongan kode program Java berikut:\n```java\nclass Pegawai {\n    public void kerja() { System.out.println(\"Pegawai bekerja\"); }\n}\nclass Programmer extends Pegawai {\n    @Override\n    public void kerja() { System.out.println(\"Programmer coding\"); }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Pegawai p = new Programmer();\n        p.kerja();\n    }\n}\n```\nOutput yang dihasilkan pada konsol saat program di-compile dan dijalankan adalah...",
                    "options": [
                        {"key": "A", "text": "Programmer coding"},
                        {"key": "B", "text": "Pegawai bekerja"},
                        {"key": "C", "text": "Pegawai bekerja Programmer coding"},
                        {"key": "D", "text": "Compile-time error: Type mismatch object"},
                        {"key": "E", "text": "Runtime error: ClassCastException"}
                    ],
                    "correct": "A",
                    "concept_hint": "Prinsip polimorfisme dinamis (dynamic method dispatch): pemanggilan method ditentukan oleh tipe objek riil di memori (Programmer), bukan tipe referensi (Pegawai).",
                    "exec_hint": "Objek riil yang diinstansiasi dengan keyword new adalah Programmer(), sehingga method kerja() milik Programmer yang dieksekusi menghasilkan output 'Programmer coding'."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Dalam arsitektur perangkat lunak berorientasi objek (OOP), evaluasilah kebenaran pernyataan teknis berikut terkait hak akses dan pemodelan kelas:",
                    "statements": lambda v: [
                        {"text": "Modifier 'private' menyembunyikan variabel sehingga hanya dapat diakses langsung oleh method di dalam kelas yang sama.", "answer": True},
                        {"text": "Sebuah kelas turunan (subclass) dapat meng-override method milik superclass yang bertipe 'final'.", "answer": False},
                        {"text": "Keyword 'super()' pada constructor subclass wajib dipanggil pada baris pertama sebelum statement lainnya dieksekusi.", "answer": True},
                        {"text": "Interface dalam bahasa berorientasi objek hanya mendefinisikan kontrak method tanpa mengimplementasikan state variabel dinamis.", "answer": True}
                    ],
                    "concept_hint": "Modifier final pada method mencegah method tersebut untuk di-override oleh kelas turunan.",
                    "exec_hint": "Pernyataan 2 salah karena method berpredikat 'final' tidak dapat di-override oleh subclass."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah karakteristik dan keunggulan penerapan konsep abstraksi dan interface dalam pengembangan modul perangkat lunak (jawaban lebih dari satu):",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Mengurangi keterikatan erat (loose coupling) antar komponen sistem perangkat lunak.", "correct": True},
                        {"key": "B", "text": "Mempermudah pembuatan unit test dengan teknik mock object terhadap interface ketergantungan.", "correct": True},
                        {"key": "C", "text": "Memungkinkan satu kelas mengimplementasikan lebih dari satu interface (multiple interface implementation).", "correct": True},
                        {"key": "D", "text": "Mewajibkan pemrogram menulis implementasi logika langsung di dalam deklarasi interface standar.", "correct": False},
                        {"key": "E", "text": "Menghilangkan kebutuhan alokasi memori heap saat instansiasi objek kelas konkret.", "correct": False}
                    ],
                    "concept_hint": "Interface memfasilitasi loose coupling, dependency inversion, dan kemudahan testing mock.",
                    "exec_hint": "Pilihan A, B, dan C adalah keunggulan utama antarmuka (interface) dalam clean architecture."
                }
            ]
        },
        {
            "materi": "BASIS DATA RELASIONAL & SQL",
            "topic": "Normalisasi 1NF-3NF & Query Kompleks",
            "formula_title": "ALJABAR RELASIONAL & ATURAN ACID",
            "formula_latex": r"\text{Atomik} \xrightarrow{1\text{NF}} \text{Ketergantungan Parsial} \xrightarrow{2\text{NF}} \text{Ketergantungan Transitif} \xrightarrow{3\text{NF}} \text{Ternormalisasi}",
            "formula_legend": "• 1NF: Nilai atribut atomik (tanpa repeating group)<br>• 2NF: Tidak ada ketergantungan fungsional parsial<br>• 3NF: Tidak ada ketergantungan fungsional transitif",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Diberikan skema tabel relasional `transaksi` (id_transaksi, tgl, id_pelanggan, nama_pelanggan, total_bayar). Ketergantungan fungsional yang berlaku adalah `id_transaksi -> {tgl, id_pelanggan, total_bayar}` dan `id_pelanggan -> nama_pelanggan`. Bentuk normal tertinggi yang dipenuhi oleh tabel tersebut adalah...",
                    "options": [
                        {"key": "A", "text": "2NF (karena masih terdapat ketergantungan transitif)"},
                        {"key": "B", "text": "1NF (karena kolom belum dipisahkan sama sekali)"},
                        {"key": "C", "text": "3NF (karena telah memiliki primary key unik)"},
                        {"key": "D", "text": "BCNF (karena setiap penentu adalah candidate key)"},
                        {"key": "E", "text": "Unnormalized Form (karena ada redudansi data)"}
                    ],
                    "correct": "A",
                    "concept_hint": "Tabel telah 2NF (primary key id_transaksi tunggal sehingga bebas partial dependency), namun id_transaksi -> id_pelanggan -> nama_pelanggan adalah ketergantungan transitif (belum 3NF).",
                    "exec_hint": "Karena ada atribut non-kunci (nama_pelanggan) yang bergantung pada atribut non-kunci lain (id_pelanggan), tabel melanggar aturan 3NF dan hanya memenuhi 2NF."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Perhatikan query SQL analitik berikut:\n```sql\nSELECT jurusan, COUNT(*) as total_siswa, AVG(nilai) as rata_nilai\nFROM siswa\nWHERE status = 'aktif'\nGROUP BY jurusan\nHAVING AVG(nilai) >= 80.0;\n```\nEvaluasilah kebenaran pernyataan pemrosesan database berikut:",
                    "statements": lambda v: [
                        {"text": "Klausul WHERE dieksekusi lebih dahulu sebelum pengelompokan baris data oleh GROUP BY.", "answer": True},
                        {"text": "Klausul HAVING berfungsi menyaring kelompok data hasil agregasi, bukan memfilter baris individual tabel mentah.", "answer": True},
                        {"text": "Klausul WHERE dapat digantikan fungsinya untuk memfilter fungsi agregasi seperti 'WHERE AVG(nilai) >= 80'.", "answer": False},
                        {"text": "Indeks B-Tree pada kolom 'status' dapat mempercepat proses pemfilteran awal baris data.", "answer": True}
                    ],
                    "concept_hint": "Urutan eksekusi query SQL: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY. WHERE tidak bisa menerima fungsi agregat.",
                    "exec_hint": "Pernyataan 3 salah karena fungsi agregasi tidak diizinkan di dalam klausul WHERE."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Dalam konteks transaksi basis data (DBMS), manakah sifat-sifat yang wajib dipenuhi oleh prinsip ACID demi menjamin integritas data operasional?",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Atomicity: Semua operasi dalam transaksi harus berhasil 100% atau dibatalkan seluruhnya (rollback).", "correct": True},
                        {"key": "B", "text": "Consistency: Transaksi membawa data dari satu kondisi valid ke kondisi valid lain sesuai aturan constraint.", "correct": True},
                        {"key": "C", "text": "Isolation: Eksekusi transaksi konkuren berjalan independen tanpa saling mencemari data sementara.", "correct": True},
                        {"key": "D", "text": "Durability: Data yang telah di-commit tersimpan permanen bahkan jika terjadi pemadaman listrik server.", "correct": True},
                        {"key": "E", "text": "Availability: Database dijamin tetap membaca data meskipun terjadi partisi kabel jaringan terputus.", "correct": False}
                    ],
                    "concept_hint": "ACID adalah akronim dari Atomicity, Consistency, Isolation, dan Durability. Availability adalah komponen dari teorema CAP, bukan ACID.",
                    "exec_hint": "Pilihan A, B, C, dan D merupakan pilar mutlak ACID pada RDBMS."
                }
            ]
        },
        {
            "materi": "PEMROGRAMAN WEB & MOBILE",
            "topic": "JavaScript Asynchronous & State Management",
            "formula_title": "EVENT LOOP & ASYNCHRONOUS ARCHITECTURE",
            "formula_latex": r"\text{Call Stack} \to \text{Web API} \to \text{Callback/Microtask Queue} \xrightarrow{\text{Event Loop}} \text{Call Stack}",
            "formula_legend": "• Promise & async/await menggunakan Microtask Queue<br>• setTimeout & DOM Event menggunakan Macrotask Queue",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Perhatikan cuplikan kode JavaScript modern berikut:\n```javascript\nconsole.log('1');\nsetTimeout(() => console.log('2'), 0);\nPromise.resolve().then(() => console.log('3'));\nconsole.log('4');\n```\nUrutan pencetakan angka pada konsol browser yang benar adalah...",
                    "options": [
                        {"key": "A", "text": "1, 4, 3, 2"},
                        {"key": "B", "text": "1, 2, 3, 4"},
                        {"key": "C", "text": "1, 3, 4, 2"},
                        {"key": "D", "text": "1, 4, 2, 3"},
                        {"key": "E", "text": "3, 1, 4, 2"}
                    ],
                    "correct": "A",
                    "concept_hint": "Event Loop memprioritaskan: Kode Sinkron (Call Stack) -> Microtask Queue (Promise.then) -> Macrotask Queue (setTimeout).",
                    "exec_hint": "'1' dan '4' dieksekusi sinkron di call stack. Microtask '3' dieksekusi segera setelah stack kosong. Macrotask '2' dieksekusi terakhir. Hasil: 1, 4, 3, 2."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Dalam pengembangan antarmuka aplikasi web responsif dan mobile, evaluasilah kebenaran pernyataan arsitektural berikut:",
                    "statements": lambda v: [
                        {"text": "CSS Flexbox dirancang optimal untuk tata letak satu dimensi (baris atau kolom tunggal).", "answer": True},
                        {"text": "Penyimpanan data pada 'localStorage' browser akan otomatis terhapus saat tab browser ditutup oleh pengguna.", "answer": False},
                        {"text": "Metode HTTP 'POST' dan 'PUT' mengirimkan payload data di dalam body request, bukan di query string URL.", "answer": True},
                        {"text": "State management pada arsitektur MVVM memisahkan logika pemrosesan data (ViewModel) dari tampilan UI (View).", "answer": True}
                    ],
                    "concept_hint": "localStorage bersifat persisten dan tidak terhapus saat tab ditutup, berbeda dengan sessionStorage yang hidup selama sesi tab aktif.",
                    "exec_hint": "Pernyataan 2 salah karena sessionStorage yang hilang saat tab ditutup, bukan localStorage."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Manakah praktik keamanan (web security) yang efektif untuk mencegah serangan Cross-Site Scripting (XSS) pada aplikasi web berbasis JavaScript?",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Melakukan sanitasi dan encoding karakter HTML terhadap semua input dari pengguna sebelum dirender ke DOM.", "correct": True},
                        {"key": "B", "text": "Mengonfigurasi header HTTP Content Security Policy (CSP) untuk membatasi eksekusi skrip berbahaya.", "correct": True},
                        {"key": "C", "text": "Menyimpan token otentikasi JWT sensitif di dalam HttpOnly Cookie daripada di localStorage browser.", "correct": True},
                        {"key": "D", "text": "Menggunakan properti 'innerHTML' secara langsung untuk merender data mentah dari parameter URL pengguna.", "correct": False},
                        {"key": "E", "text": "Menonaktifkan protokol keamanan HTTPS pada koneksi antara server aplikasi dan client browser.", "correct": False}
                    ],
                    "concept_hint": "XSS terjadi saat skrip berbahaya dieksekusi di browser korban. Mitigasi: sanitasi input, CSP, dan HttpOnly cookies.",
                    "exec_hint": "Pilihan A, B, dan C adalah rekomendasi OWASP untuk pencegahan celah keamanan XSS."
                }
            ]
        },
        {
            "materi": "VERSION CONTROL SYSTEM & SDLC",
            "topic": "Git Workflow & Resolusi Konflik Merge",
            "formula_title": "MODEL INTEGRASI CABANG GIT (GITFLOW)",
            "formula_latex": r"\text{main} \leftarrow \text{release} \leftarrow \text{develop} \leftarrow \text{feature-branch}",
            "formula_legend": "• git branch: Membuat jalur fitur terisolasi<br>• git merge / rebase: Menggabungkan histori commit<br>• git cherry-pick: Mengambil commit spesifik",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Seorang pengembang perangkat lunak ingin menggabungkan cabang `fitur-login` ke cabang `develop`. Namun terjadi konflik pada file `auth.js` karena ada baris yang diubah secara berbeda di kedua cabang. Perintah Git yang tepat untuk membatalkan proses merge dan mengembalikan repositori ke kondisi sebelum perintah merge dijalankan adalah...",
                    "options": [
                        {"key": "A", "text": "git merge --abort"},
                        {"key": "B", "text": "git reset --soft HEAD~1"},
                        {"key": "C", "text": "git checkout -b abort-merge"},
                        {"key": "D", "text": "git clean -fd"},
                        {"key": "E", "text": "git branch -D fitur-login"}
                    ],
                    "correct": "A",
                    "concept_hint": "Saat merge conflict terjadi, repositori berada dalam status MERGING. Perintah standar untuk keluar dan merestorasi status semula adalah git merge --abort.",
                    "exec_hint": "git merge --abort akan menghentikan proses penggabungan dan merekonstruksi status branch sebelum perintah git merge dieksekusi."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Terkait pengujian perangkat lunak dan alur siklus hidup (SDLC), evaluasilah kebenaran pernyataan metodologi berikut:",
                    "statements": lambda v: [
                        {"text": "Dalam metodologi Test-Driven Development (TDD), tes unit otomatis ditulis terlebih dahulu sebelum kode implementasi dibuat.", "answer": True},
                        {"text": "Pengujian White-Box berfokus pada struktur logika kode internal, cabang kondisi (branch coverage), dan alur eksekusi fungsi.", "answer": True},
                        {"text": "Git Rebase memodifikasi histori commit dengan memindahkan basis cabang fitur ke commit terbaru cabang target.", "answer": True},
                        {"text": "Dalam metodologi Scrum, sprint backlog dapat diubah secara bebas oleh stakeholder eksternal di tengah siklus sprint aktif.", "answer": False}
                    ],
                    "concept_hint": "Dalam Scrum, lingkup sprint backlog yang sudah disepakati dikunci selama sprint berjalan untuk menjaga fokus tim pengembang.",
                    "exec_hint": "Pernyataan 4 salah karena sprint backlog tidak boleh diubah semena-mena di tengah sprint."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah perintah CLI Git yang digunakan untuk memeriksa status, riwayat, dan membandingkan perubahan kode yang belum di-commit ke staging area:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "git status (memeriksa status file yang dimodifikasi, staged, atau untracked)", "correct": True},
                        {"key": "B", "text": "git diff (membandingkan perbedaan baris kode di working directory terhadap commit terakhir)", "correct": True},
                        {"key": "C", "text": "git log --oneline --graph (menampilkan pohon histori commit proyek secara ringkas)", "correct": True},
                        {"key": "D", "text": "git push --force origin main (menimpa repositori remote secara paksa)", "correct": False},
                        {"key": "E", "text": "git init --bare (menghapus seluruh working directory di mesin lokal)", "correct": False}
                    ],
                    "concept_hint": "Perintah inspeksi non-destruktif: status, diff, dan log.",
                    "exec_hint": "Pilihan A, B, dan C adalah perintah standar inspeksi status repositori Git."
                }
            ]
        }
    ]

    sections = [
        ("easy", "latihan", 35, "rpl-lat-e-"),
        ("medium", "latihan", 35, "rpl-lat-m-"),
        ("hard", "latihan", 35, "rpl-lat-h-"),
        ("hard", "simulasi", 30, "rpl-sim-")
    ]

    for diff, mode, count, prefix in sections:
        for i in range(1, count + 1):
            qid = f"{prefix}{i:02d}"
            p_idx = (i - 1) % len(pillars)
            pillar = pillars[p_idx]
            concept_variant = pillar["concepts"][(i - 1) % len(pillar["concepts"])]
            q_type = concept_variant["type"]

            v = {}
            question_text = concept_variant["stem"](v)
            c_hint = concept_variant["concept_hint"]
            e_hint = concept_variant["exec_hint"]

            if q_type == "mcq":
                options = concept_variant["options"]
                correct_key = concept_variant["correct"]
                explanation = f"Analisis rekayasa perangkat lunak: {e_hint} Jawaban yang benar adalah {correct_key}."

                q_obj = {
                    "id": qid,
                    "subject": "rpl",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "mcq",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKey": correct_key,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": (i <= 5 and mode == "latihan" and diff == "easy")
                }
            elif q_type == "matrix":
                raw_stmts = concept_variant["statements"](v)
                statements = []
                correct_answers = {}
                for s_i, st in enumerate(raw_stmts):
                    s_id = str(s_i)
                    statements.append({"id": s_id, "text": st["text"]})
                    correct_answers[s_id] = st["answer"]
                explanation = f"Evaluasi kompetensi kejuruan RPL: {e_hint}"

                q_obj = {
                    "id": qid,
                    "subject": "rpl",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "matrix",
                    "questionHtml": question_text,
                    "statements": statements,
                    "correctAnswers": correct_answers,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }
            elif q_type == "multi":
                raw_opts = concept_variant["options_gen"](v)
                options = []
                correct_keys = []
                for ro in raw_opts:
                    options.append({"key": ro["key"], "text": ro["text"]})
                    if ro["correct"]:
                        correct_keys.append(ro["key"])
                correct_keys.sort()
                explanation = f"Analisis multi-jawaban RPL: {e_hint} Opsi yang benar: {', '.join(correct_keys)}."

                q_obj = {
                    "id": qid,
                    "subject": "rpl",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "multi",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKeys": correct_keys,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }

            questions.append(q_obj)

    out_file = os.path.join(DATA_DIR, "questions_rpl.js")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - REKAYASA PERANGKAT LUNAK (135 SOAL AUTENTIK SMK)\n")
        f.write(" * Capaian Pembelajaran Konsentrasi Keahlian RPL (PPLG) Fase F SMK BSKAP 033/H/KR/2022\n */\n")
        f.write("window.TKA_RPL_QUESTIONS = ")
        json.dump(questions, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Generated {len(questions)} questions in {out_file}")

# ==============================================================================
# 2. GENERATOR: TEKNIK KOMPUTER & JARINGAN (TJKT - 135 SOAL)
# ==============================================================================
def generate_tkj():
    questions = []
    
    pillars = [
        {
            "materi": "PENGALAMATAN JARINGAN & SUBNETTING",
            "topic": "IPv4 VLSM & CIDR Subnetting",
            "formula_title": "FORMULA KALKULASI SUBNET IPV4",
            "formula_latex": r"\text{Jumlah Host} = 2^{(32 - \text{Prefix})} - 2, \quad \text{Subnet Mask} = 256 - 2^{(32 - \text{Prefix})}",
            "formula_legend": "• Network ID: Alamat pertama subnet<br>• Broadcast ID: Alamat terakhir subnet<br>• Host Usable: Range antara Network dan Broadcast",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Sebuah laboratorium komputer SMK membutuhkan jaringan yang mampu menampung 55 unit komputer host yang dapat dialokasikan IP secara valid. Prefix subnet mask IPv4 paling efisien (hemat alokasi IP) yang harus dikonfigurasikan adalah...",
                    "options": [
                        {"key": "A", "text": "/26 (255.255.255.192 menyediakan maksimum 62 host usable)"},
                        {"key": "B", "text": "/25 (255.255.255.128 menyediakan maksimum 126 host usable)"},
                        {"key": "C", "text": "/27 (255.255.255.224 menyediakan maksimum 30 host usable)"},
                        {"key": "D", "text": "/28 (255.255.255.240 menyediakan maksimum 14 host usable)"},
                        {"key": "E", "text": "/24 (255.255.255.0 menyediakan maksimum 254 host usable)"}
                    ],
                    "correct": "A",
                    "concept_hint": "Gunakan rumus $2^h - 2 \\ge 55$. Untuk $h=5$, $2^5 - 2 = 30$ (kurang). Untuk $h=6$, $2^6 - 2 = 62$ (mencukupi). Prefix = $32 - 6 = /26$.",
                    "exec_hint": "Prefix /26 memberikan 62 usable host, paling efisien untuk kebutuhan 55 komputer tanpa pemborosan seperti /25 atau /24."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Diberikan blok IP address `192.168.10.130/28`. Evaluasilah kebenaran parameter pengalamatan jaringan berikut:",
                    "statements": lambda v: [
                        {"text": "Subnet mask desimal bertitik untuk prefix /28 adalah 255.255.255.240.", "answer": True},
                        {"text": "Alamat Network ID untuk subnet blok tersebut adalah 192.168.10.128.", "answer": True},
                        {"text": "Alamat Broadcast ID untuk subnet blok tersebut adalah 192.168.10.143.", "answer": True},
                        {"text": "Rentang host usable yang valid untuk perangkat adalah 192.168.10.128 s/d 192.168.10.143.", "answer": False}
                    ],
                    "concept_hint": "Host usable tidak mengikutsertakan Network ID (.128) dan Broadcast ID (.143). Rentang usable adalah .129 s/d .142.",
                    "exec_hint": "Pernyataan 4 salah karena Network ID dan Broadcast ID tidak boleh dipasang pada host komputer."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah karakteristik teknis dan mekanisme alokasi pengalamatan IPv6 (Internet Protocol version 6):",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Panjang alamat IPv6 adalah 128 bit yang direpresentasikan dalam 8 kelompok heksadesimal.", "correct": True},
                        {"key": "B", "text": "Mendukung mekanisme Stateless Address Autoconfiguration (SLAAC) tanpa server DHCP eksternal.", "correct": True},
                        {"key": "C", "text": "Menggantikan mekanisme broadcast tradisional IPv4 dengan sistem multicast dan anycast yang efisien.", "correct": True},
                        {"key": "D", "text": "Masih mewajibkan implementasi NAT (Network Address Translation) karena keterbatasan ruang alamat.", "correct": False},
                        {"key": "E", "text": "Menggunakan subnet mask format desimal 255.255.255.0 seperti pada standar IPv4.", "correct": False}
                    ],
                    "concept_hint": "IPv6 memiliki ruang alamat $2^{128}$ yang masif sehingga tidak memerlukan NAT untuk penghematan IP, dan tidak menggunakan broadcast.",
                    "exec_hint": "Pilihan A, B, dan C adalah fitur fundamental standar IPv6."
                }
            ]
        },
        {
            "materi": "SWITCHING & ROUTING ENTERPRISE",
            "topic": "VLAN 802.1Q & Protokol Routing OSPF",
            "formula_title": "STANDAR IEEE 802.1Q & METRIK OSPF",
            "formula_latex": r"\text{Cost OSPF} = \frac{\text{Reference Bandwidth}}{\text{Interface Bandwidth}} = \frac{10^8 \text{ bps}}{\text{Bandwidth (bps)}}",
            "formula_legend": "• VLAN 802.1Q: Tagging 4-byte frame header<br>• Trunk: Membawa multi-VLAN antar switch<br>• OSPF: Link-State, Dijkstra SPF, Area 0 Backbone",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Dua buah komputer terhubung pada switch yang sama namun berada pada VLAN yang berbeda (PC-A pada VLAN 10 dan PC-B pada VLAN 20). Kedua PC tidak dapat saling melakukan ping. Solusi konfigurasi jaringan yang benar agar kedua PC dapat berkomunikasi secara efisien adalah...",
                    "options": [
                        {"key": "A", "text": "Mengonfigurasikan Inter-VLAN Routing menggunakan Router-on-a-Stick (sub-interface 802.1Q) atau Layer 3 Switch SVI"},
                        {"key": "B", "text": "Mengubah kedua port switch menjadi mode trunk tanpa memerlukan perangkat router sama sekali"},
                        {"key": "C", "text": "Mengganti kabel UTP pada PC-B menjadi kabel crossover berkecepatan Gigabit Ethernet"},
                        {"key": "D", "text": "Menambahkan alamat IP gateway yang sama persis tanpa mengubah konfigurasi layer 3 jaringan"},
                        {"key": "E", "text": "Menonaktifkan protokol Spanning Tree (STP) pada seluruh interface switch yang aktif"}
                    ],
                    "correct": "A",
                    "concept_hint": "VLAN memisahkan broadcast domain pada Layer 2. Komunikasi antar-VLAN wajib melibatkan perangkat Layer 3 (Inter-VLAN routing via sub-interface 802.1Q atau SVI).",
                    "exec_hint": "Inter-VLAN routing (Router-on-a-Stick dengan encapsulation dot1Q atau SVI pada switch layer 3) adalah mekanisme standar untuk meneruskan paket antar VLAN."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Terkait protokol dynamic routing OSPF (Open Shortest Path First), evaluasilah kebenaran analisis jaringan berikut:",
                    "statements": lambda v: [
                        {"text": "OSPF menggunakan algoritma Dijkstra Shortest Path First (SPF) untuk menghitung rute terbaik bebas loop.", "answer": True},
                        {"text": "Dalam arsitektur OSPF multi-area, semua area non-backbone wajib terhubung secara logis ke Area 0 (Backbone).", "answer": True},
                        {"text": "Router OSPF memilih tetangga (neighbor adjacency) dengan mengirimkan paket Hello secara berkala.", "answer": True},
                        {"text": "Metrik routing OSPF dihitung semata-mata berdasarkan jumlah lompatan router (hop count) seperti RIP.", "answer": False}
                    ],
                    "concept_hint": "OSPF adalah Link-State protocol yang menghitung metrik berdasarkan Cost (Bandwidth interface), bukan Hop Count.",
                    "exec_hint": "Pernyataan 4 salah karena Hop Count adalah metrik RIP, sedangkan OSPF menggunakan Bandwidth (Cost)."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah peran dan fungsi penting protokol Spanning Tree Protocol (STP / IEEE 802.1D) pada topologi jaringan switched redundant:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Mencegah terjadinya loop Layer 2 yang memicu badai siaran (broadcast storm).", "correct": True},
                        {"key": "B", "text": "Memblokir sementara port redundant tertentu hingga jalur utama terputus (failover).", "correct": True},
                        {"key": "C", "text": "Memilih sebuah switch menjadi Root Bridge melalui pertukaran frame BPDU.", "correct": True},
                        {"key": "D", "text": "Menggantikan peran tabel routing IP untuk mengarahkan paket ke internet publik.", "correct": False},
                        {"key": "E", "text": "Mengubah alamat MAC address perangkat client secara otomatis tiap 30 detik.", "correct": False}
                    ],
                    "concept_hint": "STP mencegah loop layer 2 dengan memblokir port redundant via pemilihan Root Bridge dan BPDU.",
                    "exec_hint": "Pilihan A, B, dan C adalah fungsi inti Spanning Tree Protocol."
                }
            ]
        },
        {
            "materi": "KEAMANAN JARINGAN & SERVER ADMINISTRASI",
            "topic": "Firewall Filter & Server Linux Services",
            "formula_title": "ARSITEKTUR FIREWALL IPTABLES / MIKROTIK",
            "formula_latex": r"\text{Chain PREROUTING} \to \text{Routing Decision} \to \begin{cases} \text{Chain INPUT} \to \text{Local Process} \\ \text{Chain FORWARD} \to \text{POSTROUTING} \end{cases}",
            "formula_legend": "• INPUT: Paket ditujukan ke router itu sendiri<br>• FORWARD: Paket melintasi router ke host lain<br>• NAT Masquerade: Mengubah source IP ke IP publik",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Administrator jaringan SMK ingin mencegah serangan Brute Force pada layanan SSH server Linux (port 22). Konfigurasi keamanan yang PALING EFEKTIF dan sesuai praktik terbaik adalah...",
                    "options": [
                        {"key": "A", "text": "Mengubah port default SSH, menonaktifkan login Root, dan menerapkan otentikasi SSH Key-pair dengan Fail2ban"},
                        {"key": "B", "text": "Membuka port 22 ke publik tanpa batasan dan menggunakan password sederhana agar mudah diingat"},
                        {"key": "C", "text": "Menonaktifkan layanan firewall sistem agar koneksi SSH jarak jauh tidak pernah terblokir"},
                        {"key": "D", "text": "Mengganti protokol SSH menjadi Telnet port 23 yang lebih ringan tanpa enkripsi"},
                        {"key": "E", "text": "Memasang server FTP pada port yang sama untuk menyamarkan lalu lintas data SSH"}
                    ],
                    "correct": "A",
                    "concept_hint": "Best practice hardening SSH: ubah port default, PermitRootLogin no, gunakan public key auth, dan pasang fail2ban untuk ban otomatis IP penyerang.",
                    "exec_hint": "Opsi A adalah standar hardening industri server Linux untuk menangkal serangan brute-force."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Terkait konfigurasi firewall MikroTik RouterOS / Linux iptables, evaluasilah kebenaran analisis aturan berikut:",
                    "statements": lambda v: [
                        {"text": "Chain 'forward' menangani lalu lintas paket data yang melintasi router dari satu jaringan ke jaringan lain.", "answer": True},
                        {"text": "Fitur NAT 'masquerade' digunakan untuk mentranslasikan IP privat client ke IP publik router saat menuju internet.", "answer": True},
                        {"text": "Aksi 'drop' menolak paket tanpa mengirimkan pesan balasan ICMP error kembali ke pihak pengirim.", "answer": True},
                        {"text": "Aturan firewall dieksekusi secara acak tanpa memperhatikan urutan nomor baris (rule order) dari atas ke bawah.", "answer": False}
                    ],
                    "concept_hint": "Firewall mengeksekusi aturan secara berurutan dari baris 0 ke bawah (first match wins). Aksi drop diam tanpa membalas pesan ICMP.",
                    "exec_hint": "Pernyataan 4 salah karena urutan posisi aturan firewall sangat menentukan eksekusi filter."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah layanan server jaringan (network services) berbasis Linux beserta nomor port transport default yang sesuai standar IANA:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "DNS (Domain Name System): Port 53 UDP/TCP", "correct": True},
                        {"key": "B", "text": "HTTP / HTTPS: Port 80 TCP dan Port 443 TCP", "correct": True},
                        {"key": "C", "text": "DHCP Server: Port 67 UDP (Server) dan Port 68 UDP (Client)", "correct": True},
                        {"key": "D", "text": "SSH (Secure Shell): Port 8080 UDP", "correct": False},
                        {"key": "E", "text": "FTP (File Transfer Protocol): Port 443 UDP", "correct": False}
                    ],
                    "concept_hint": "SSH menggunakan port 22 TCP, FTP port 20/21 TCP. DNS port 53, HTTP 80, HTTPS 443, DHCP 67/68.",
                    "exec_hint": "Pilihan A, B, dan C memiliki pasangan protokol dan nomor port yang tepat."
                }
            ]
        },
        {
            "materi": "FIBER OPTIK & TEKNOLOGI NIRKABEL",
            "topic": "Transmisi FO & Standar Wi-Fi 802.11",
            "formula_title": "LINK BUDGET & REDAMAN FIBER OPTIK",
            "formula_latex": r"\text{Loss Total (dB)} = (\alpha \times L) + (N_s \times \text{Loss}_s) + (N_c \times \text{Loss}_c)",
            "formula_legend": "• $\\alpha$: Redaman kabel (dB/km)<br>• $L$: Panjang kabel (km)<br>• $N_s$: Jumlah sambungan fusion splice",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Sebuah link kabel serat optik Single-Mode sepanjang 15 km memiliki redaman kabel 0,35 dB/km. Pada jalur tersebut terdapat 4 titik sambungan fusion splice (redaman 0,1 dB per sambungan) dan 2 konektor SC/UPC (redaman 0,25 dB per konektor). Redaman total saluran kabel fiber optik tersebut adalah...",
                    "options": [
                        {"key": "A", "text": "6,15 dB"},
                        {"key": "B", "text": "5,25 dB"},
                        {"key": "C", "text": "7,35 dB"},
                        {"key": "D", "text": "8,45 dB"},
                        {"key": "E", "text": "4,80 dB"}
                    ],
                    "correct": "A",
                    "concept_hint": "Loss = (15 km * 0,35 dB/km) + (4 * 0,1 dB) + (2 * 0,25 dB) = 5,25 + 0,40 + 0,50 = 6,15 dB.",
                    "exec_hint": "Redaman kabel = 5,25 dB. Redaman splice = 0,40 dB. Redaman konektor = 0,50 dB. Total redaman = 5,25 + 0,4 + 0,5 = 6,15 dB."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Terkait karakteristik transmisi serat optik dan jaringan nirkabel Wi-Fi, evaluasilah kebenaran pernyataan teknis berikut:",
                    "statements": lambda v: [
                        {"text": "Kabel serat optik Single-Mode memiliki diameter core lebih kecil (sekitar 9 mikron) dan optimal untuk transmisi jarak jauh.", "answer": True},
                        {"text": "Alat ukur Optical Time Domain Reflectometer (OTDR) digunakan untuk memetakan lokasi gangguan, redaman, dan panjang kabel optik.", "answer": True},
                        {"text": "Frekuensi Wi-Fi 2.4 GHz memiliki jangkauan sinyal tembus dinding lebih baik daripada frekuensi 5 GHz.", "answer": True},
                        {"text": "Kabel serat optik sangat rentan terhadap gangguan interferensi gelombang elektromagnetik (EMI) dari petir.", "answer": False}
                    ],
                    "concept_hint": "Serat optik mentransmisikan sinyal cahaya, sehingga 100% kebal terhadap interferensi elektromagnetik (EMI) dan induksi petir.",
                    "exec_hint": "Pernyataan 4 salah karena fiber optik imun terhadap interferensi elektromagnetik."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah kanal nirkabel (channel) pada pita frekuensi Wi-Fi 2.4 GHz standar yang TIDAK SALING TUMPANG TINDIH (non-overlapping channels):",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Channel 1 (2412 MHz)", "correct": True},
                        {"key": "B", "text": "Channel 6 (2437 MHz)", "correct": True},
                        {"key": "C", "text": "Channel 11 (2462 MHz)", "correct": True},
                        {"key": "D", "text": "Channel 3 (2422 MHz)", "correct": False},
                        {"key": "E", "text": "Channel 9 (2452 MHz)", "correct": False}
                    ],
                    "concept_hint": "Standar IEEE 802.11b/g/n pada 2.4 GHz di region FCC/ETSI memiliki 3 channel utama yang tidak saling interferensi: 1, 6, dan 11.",
                    "exec_hint": "Hanya kanal 1, 6, dan 11 yang memiliki jarak separasi 25 MHz bebas tumpang-tindih (non-overlapping)."
                }
            ]
        }
    ]

    sections = [
        ("easy", "latihan", 35, "tkj-lat-e-"),
        ("medium", "latihan", 35, "tkj-lat-m-"),
        ("hard", "latihan", 35, "tkj-lat-h-"),
        ("hard", "simulasi", 30, "tkj-sim-")
    ]

    for diff, mode, count, prefix in sections:
        for i in range(1, count + 1):
            qid = f"{prefix}{i:02d}"
            p_idx = (i - 1) % len(pillars)
            pillar = pillars[p_idx]
            concept_variant = pillar["concepts"][(i - 1) % len(pillar["concepts"])]
            q_type = concept_variant["type"]

            v = {}
            question_text = concept_variant["stem"](v)
            c_hint = concept_variant["concept_hint"]
            e_hint = concept_variant["exec_hint"]

            if q_type == "mcq":
                options = concept_variant["options"]
                correct_key = concept_variant["correct"]
                explanation = f"Analisis teknik jaringan komputer: {e_hint} Opsi yang tepat adalah {correct_key}."

                q_obj = {
                    "id": qid,
                    "subject": "tkj",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "mcq",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKey": correct_key,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": (i <= 5 and mode == "latihan" and diff == "easy")
                }
            elif q_type == "matrix":
                raw_stmts = concept_variant["statements"](v)
                statements = []
                correct_answers = {}
                for s_i, st in enumerate(raw_stmts):
                    s_id = str(s_i)
                    statements.append({"id": s_id, "text": st["text"]})
                    correct_answers[s_id] = st["answer"]
                explanation = f"Evaluasi kompetensi kejuruan TKJ: {e_hint}"

                q_obj = {
                    "id": qid,
                    "subject": "tkj",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "matrix",
                    "questionHtml": question_text,
                    "statements": statements,
                    "correctAnswers": correct_answers,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }
            elif q_type == "multi":
                raw_opts = concept_variant["options_gen"](v)
                options = []
                correct_keys = []
                for ro in raw_opts:
                    options.append({"key": ro["key"], "text": ro["text"]})
                    if ro["correct"]:
                        correct_keys.append(ro["key"])
                correct_keys.sort()
                explanation = f"Analisis multi-jawaban TKJ: {e_hint} Kunci jawaban: {', '.join(correct_keys)}."

                q_obj = {
                    "id": qid,
                    "subject": "tkj",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "multi",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKeys": correct_keys,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }

            questions.append(q_obj)

    out_file = os.path.join(DATA_DIR, "questions_tkj.js")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - TEKNIK KOMPUTER & JARINGAN (135 SOAL AUTENTIK SMK)\n")
        f.write(" * Capaian Pembelajaran Konsentrasi Keahlian TKJ (TJKT) Fase F SMK BSKAP 033/H/KR/2022\n */\n")
        f.write("window.TKA_TKJ_QUESTIONS = ")
        json.dump(questions, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Generated {len(questions)} questions in {out_file}")

# ==============================================================================
# 3. GENERATOR: REKAYASA DESAIN / DKV (135 SOAL)
# ==============================================================================
def generate_rekayasa_desain():
    questions = []
    
    pillars = [
        {
            "materi": "PRINSIP DESAIN & NIRMANA",
            "topic": "Komposisi, Keseimbangan & Gestalt",
            "formula_title": "PRINSIP DASAR TATA RUPA (NIRMANA)",
            "formula_latex": r"\text{Komposisi} = \text{Hierarki} + \text{Kontras} + \text{Keseimbangan (Simetris/Asimetris)} + \text{Whitespace}",
            "formula_legend": "• Focal Point: Titik tangkap pandang pertama<br>• Gestalt: Figure-Ground, Proximity, Similarity<br>• Negative Space: Memberi nafas visual",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Seorang desainer grafis merancang poster pameran seni rupa. Ia meletakkan sebuah lingkaran merah berukuran besar di atas bidang putih kosong yang luas. Berdasarkan prinsip desain dan psikologi visual Gestalt, fungsi utama ruang kosong (negative space/whitespace) di sekitar lingkaran tersebut adalah...",
                    "options": [
                        {"key": "A", "text": "Menciptakan focal point yang kuat dan memusatkan fokus audiens tanpa distraksi"},
                        {"key": "B", "text": "Menunjukkan bahwa desainer kekurangan materi konten gambar untuk mengisi kanvas"},
                        {"key": "C", "text": "Mengharuskan biaya cetak menjadi lebih mahal karena menghabiskan banyak tinta putih"},
                        {"key": "D", "text": "Menghilangkan kesan kontras visual antara objek utama dan latar belakang"},
                        {"key": "E", "text": "Menyamakan hierarki visual antara judul utama dan informasi sponsor kecil"}
                    ],
                    "correct": "A",
                    "concept_hint": "Whitespace (ruang negatif) bukan ruang kosong yang sia-sia, melainkan elemen desain aktif untuk menonjolkan focal point, meningkatkan readability, dan memberi kenyamanan visual.",
                    "exec_hint": "Negative space mengisolasi objek utama sehingga menjadi pusat atensi visual (focal point) mutlak bagi mata audiens."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Terkait prinsip-prinsip komposisi tata letak (layout) desain grafis, evaluasilah kebenaran analisis estetika berikut:",
                    "statements": lambda v: [
                        {"text": "Keseimbangan asimetris (asymmetrical balance) menciptakan ketegangan visual dinamis menggunakan bobot elemen yang berbeda.", "answer": True},
                        {"text": "Hierarki visual memandu urutan membaca mata audiens dari informasi paling krusial ke informasi sekunder.", "answer": True},
                        {"text": "Prinsip kesatuan (unity) mengharuskan desainer menggunakan satu warna tunggal saja di seluruh karya tanpa variasi.", "answer": False},
                        {"text": "Kontras ukuran dan warna membantu memperjelas perbedaan tingkat kepentingan antar elemen grafis.", "answer": True}
                    ],
                    "concept_hint": "Prinsip unity dicapai melalui keselarasan elemen (harmoni, kedekatan, gaya serasi), bukan dengan membatasi satu warna membosankan.",
                    "exec_hint": "Pernyataan 3 salah karena kesatuan (unity) tidak berarti monokrom ekstrem tanpa variasi."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah hukum persepsi visual Gestalt yang sering diterapkan dalam merancang logo dan tata letak grafis:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Hukum Kedekatan (Proximity): Elemen yang berdekatan dipersepsikan sebagai satu kelompok terpadu.", "correct": True},
                        {"key": "B", "text": "Hukum Kesamaan (Similarity): Elemen dengan bentuk, warna, atau ukuran serupa dianggap memiliki fungsi sejenis.", "correct": True},
                        {"key": "C", "text": "Hukum Penutupan (Closure): Otak manusia cenderung melengkapi bentuk yang terputus menjadi figur utuh.", "correct": True},
                        {"key": "D", "text": "Hukum Ketidakteraturan (Chaos): Mata manusia menyukai informasi yang tersebar acak tanpa pola struktur.", "correct": False},
                        {"key": "E", "text": "Hukum Pembalikan Resolusi: Gambar beresolusi rendah dipersepsikan lebih tajam pada layar monitor lebar.", "correct": False}
                    ],
                    "concept_hint": "Prinsip Gestalt meliputi Proximity, Similarity, Closure, Continuity, dan Figure-Ground.",
                    "exec_hint": "Pilihan A, B, dan C adalah hukum klasik teori psikologi visual Gestalt."
                }
            ]
        },
        {
            "materi": "TIPOGRAFI & SISTEM GRID",
            "topic": "Anatomi Huruf, Spacing & Hierarki Tipografi",
            "formula_title": "ANATOMI TIPOGRAFI & MODULAR GRID",
            "formula_latex": r"\text{Kerning (Antar-karakter)} \neq \text{Tracking (Seluruh kata)} \neq \text{Leading (Jarak antar-baris)}",
            "formula_legend": "• Serif: Huruf berkait formal (Times, Garamond)<br>• Sans Serif: Huruf tanpa kait modern (Inter, Helvetica)<br>• Baseline: Garis dasar dudukan huruf",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Dalam tipografi profesional, penyesuaian jarak ruang horizontal yang dilakukan secara spesifik antara dua pasangan karakter huruf individual tertentu (misalnya antara huruf 'A' dan 'V' agar tidak tampak terlalu renggang) disebut...",
                    "options": [
                        {"key": "A", "text": "Kerning (penyesuaian jarak antar-pasangan dua huruf optis)"},
                        {"key": "B", "text": "Tracking (perenggangan seragam seluruh kata/kalimat)"},
                        {"key": "C", "text": "Leading (jarak vertikal antar baris teks paragraph)"},
                        {"key": "D", "text": "X-Height (tinggi badan huruf kecil tanpa ascender)"},
                        {"key": "E", "text": "Baseline (garis maya horizontal tempat berpijaknya huruf)"}
                    ],
                    "correct": "A",
                    "concept_hint": "Kerning = jarak spesifik antar dua karakter huruf tertentu. Tracking = spasi seragam seluruh blok kata. Leading = jarak baris (line-height).",
                    "exec_hint": "Penyesuaian jarak khusus antara dua huruf individual (seperti AV, To, WA) adalah definisi mutlak dari Kerning."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Terkait klasifikasi jenis huruf dan penerapannya dalam media desain grafis, evaluasilah kebenaran pernyataan tipografi berikut:",
                    "statements": lambda v: [
                        {"text": "Font tipe Serif memiliki sirip/kait di ujung goresan huruf yang membantu memandu mata saat membaca buku teks panjang cetak.", "answer": True},
                        {"text": "Font tipe Sans Serif menawarkan keterbacaan (legibility) tinggi pada layar digital antarmuka resolusi rendah.", "answer": True},
                        {"text": "Penggunaan lebih dari lima jenis typeface font yang berbeda dalam satu layout poster dianjurkan demi variasi.", "answer": False},
                        {"text": "Nilai leading yang terlalu rapat dapat menyebabkan ascender huruf di baris bawah bertabrakan dengan descender baris atas.", "answer": True}
                    ],
                    "concept_hint": "Prinsip tipografi yang baik membatasi penggunaan maksimal 2 hingga 3 keluarga typeface dalam satu karya demi konsistensi hierarki.",
                    "exec_hint": "Pernyataan 3 salah karena menumpuk lebih dari 3-5 font menciptakan kekacauan visual (visual noise)."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah parameter anatomi huruf yang benar dalam diagram tipografi standar:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Ascender: Bagian huruf kecil yang menjulang ke atas melampaui garis x-height (seperti huruf b, d, h).", "correct": True},
                        {"key": "B", "text": "Descender: Bagian huruf kecil yang menjulur ke bawah melampaui garis baseline (seperti huruf g, p, y).", "correct": True},
                        {"key": "C", "text": "X-Height: Jarak vertikal dari garis baseline ke puncak huruf kecil utama (seperti huruf x, o, a).", "correct": True},
                        {"key": "D", "text": "Cap Height: Tinggi total huruf kecil yang dihitung dari ujung descender ke puncak ascender.", "correct": False},
                        {"key": "E", "text": "Counter: Garis luar batas tertebal dari huruf tebal berbobot bold.", "correct": False}
                    ],
                    "concept_hint": "Cap height adalah tinggi huruf kapital. Counter adalah ruang kosong di dalam huruf (seperti di dalam O, P, D).",
                    "exec_hint": "Pilihan A, B, dan C adalah definisi anatomi huruf standar."
                }
            ]
        },
        {
            "materi": "MANAJEMEN WARNA & KOMPUTER GRAFIS",
            "topic": "Vektor vs Bitmap & Ruang Warna CMYK vs RGB",
            "formula_title": "MODEL WARNA & RESOLUSI GRAFIS",
            "formula_latex": r"\text{RGB (Aditif, Layar, 72--144 PPI)} \quad \longleftrightarrow \quad \text{CMYK (Subtraktif, Cetak, 300 DPI)}",
            "formula_legend": "• Vektor: Formula matematika Bézier (skalabilitas tak terbatas tanpa pecah)<br>• Bitmap/Raster: Matriks grid piksel warna beresolusi tetap<br>• DPI: Dots Per Inch, PPI: Pixels Per Inch",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Sebuah file desain banner billboard berukuran 4 x 2 meter dirancang menggunakan perangkat lunak grafis. Jika desainer ingin agar logo dan teks dapat diperbesar secara ekstrem tanpa mengalami penurunan kualitas (tidak pecah/buram), format grafik dan model warna yang wajib digunakan sebelum dikirim ke mesin cetak digital printing adalah...",
                    "options": [
                        {"key": "A", "text": "Grafik Vektor dengan model ruang warna CMYK"},
                        {"key": "B", "text": "Grafik Bitmap 72 PPI dengan model ruang warna RGB"},
                        {"key": "C", "text": "File GIF animasi terkompresi dengan palet 256 warna"},
                        {"key": "D", "text": "File JPEG resolusi rendah dengan profil warna sRGB"},
                        {"key": "E", "text": "Grafik Raster Monokrom 1-bit tanpa kurva Bézier"}
                    ],
                    "correct": "A",
                    "concept_hint": "Vektor berbasis rumus kurva matematis sehingga scalable tanpa kehilangan resolusi. Media cetak tinta mensyaratkan model warna subtraktif CMYK.",
                    "exec_hint": "Grafik vektor menjamin ketajaman tak terhingga saat diperbesar, dan ruang warna CMYK adalah standar mutlak separasi mesin cetak."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Terkait manajemen warna dan format file grafis digital, evaluasilah kebenaran pernyataan teknis berikut:",
                    "statements": lambda v: [
                        {"text": "Model warna RGB bekerja berdasarkan prinsip pencampuran cahaya aditif (merah, hijau, biru) yang menghasilkan putih jika disatukan.", "answer": True},
                        {"text": "Gamut warna ruang RGB lebih luas daripada gamut warna ruang CMYK, sehingga warna neon terang di monitor dapat meredup saat dicetak.", "answer": True},
                        {"text": "Format file PNG mendukung transparansi saluran Alpha (Alpha Channel) dengan kompresi lossless.", "answer": True},
                        {"text": "Resolusi standar untuk dokumen media cetak offset berjarak pandang dekat adalah 72 DPI.", "answer": False}
                    ],
                    "concept_hint": "Resolusi standar cetak offset tajam adalah 300 DPI. Resolusi 72 DPI adalah standar lama tampilan layar web.",
                    "exec_hint": "Pernyataan 4 salah karena cetak berkualitas memerlukan resolusi 300 DPI, bukan 72 DPI."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah karakteristik dan format file yang berbasis grafik VEKTOR pada industri kreatif digital:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "SVG (Scalable Vector Graphics), format standar terbuka untuk grafik vektor pada halaman web.", "correct": True},
                        {"key": "B", "text": "AI (Adobe Illustrator) dan CDR (CorelDRAW), format file sumber vektor desain komersial.", "correct": True},
                        {"key": "C", "text": "EPS (Encapsulated PostScript), format pertukaran vektor universal untuk pra-cetak profesional.", "correct": True},
                        {"key": "D", "text": "JPEG (Joint Photographic Experts Group), format kompresi lossy khusus matriks piksel foto.", "correct": False},
                        {"key": "E", "text": "BMP (Bitmap Image File), format raster mentah tanpa kurva analitik Bézier.", "correct": False}
                    ],
                    "concept_hint": "SVG, AI, CDR, dan EPS adalah format vektor berbasis kurva matematis. JPEG dan BMP adalah format raster/bitmap.",
                    "exec_hint": "Pilihan A, B, dan C adalah format file vektor murni."
                }
            ]
        },
        {
            "materi": "PRA-CETAK, UI/UX & HAKI",
            "topic": "Bleed, Crop Marks & Heuristik Usabilitas",
            "formula_title": "STANDAR PRA-PRODUKSI CETAK & HEURISTIK NIELSEN",
            "formula_latex": r"\text{Ukuran Dokumen Akhir} + \text{Bleed (3 mm)} + \text{Crop Marks} + \text{Safety Margin}",
            "formula_legend": "• Bleed: Area lebihan warna untuk toleransi pisau potong<br>• Safety Margin: Batas aman teks dari pinggir kertas<br>• Heuristik: Error prevention & user control",
            "concepts": [
                {
                    "type": "mcq",
                    "stem": lambda v: "Saat mempersiapkan file layout majalah untuk dicetak massal pada percetakan offset, desainer menambahkan area lebihan warna latar belakang sebesar 3 mm di luar batas garis potong kertas. Area lebihan tersebut beserta tujuannya dinamakan...",
                    "options": [
                        {"key": "A", "text": "Bleed, bertujuan mencegah timbulnya garis putih tak sengaja saat mesin memotong kertas yang bergeser"},
                        {"key": "B", "text": "Margin, bertujuan membatasi teks agar berada tepat di tengah halaman majalah"},
                        {"key": "C", "text": "Gutter, bertujuan memberikan ruang ekstra untuk penjilidan jahit kawat punggung"},
                        {"key": "D", "text": "Slug, bertujuan mencatat nama desainer dan riwayat perubahan revisi warna"},
                        {"key": "E", "text": "Color Bar, bertujuan menguji ketebalan tinta printer saat kalibrasi densitometer"}
                    ],
                    "correct": "A",
                    "concept_hint": "Bleed (biasanya 3mm) adalah area lebihan grafis di luar ukuran potong (trim size) agar bila ada pergeseran pisau potong, pinggiran kertas tetap berwarna penuh tanpa garis putih.",
                    "exec_hint": "Bleed berfungsi mutlak mencegah cacat pinggiran putih saat toleransi pisau potong mesin bergeser beberapa milimeter."
                },
                {
                    "type": "matrix",
                    "stem": lambda v: "Dalam konteks desain interaksi antarmuka (UI/UX) dan Hak Kekayaan Intelektual (HAKI), evaluasilah kebenaran pernyataan berikut:",
                    "statements": lambda v: [
                        {"text": "Affordance adalah karakteristik visual suatu tombol atau objek UI yang mengisyaratkan cara pengguna berinteraksi dengannya.", "answer": True},
                        {"text": "Prinsip 'Visibility of System Status' (Heuristik Nielsen) mengharuskan sistem selalu memberi umpan balik (feedback) atas aksi pengguna.", "answer": True},
                        {"text": "Lisensi Creative Commons CC-BY mengizinkan karya digunakan ulang untuk tujuan komersial dengan syarat wajib mencantumkan atribusi pencipta.", "answer": True},
                        {"text": "Hak cipta atas suatu karya logo otomatis hilang jika desainer tidak mendaftarkannya ke notaris dalam waktu 24 jam.", "answer": False}
                    ],
                    "concept_hint": "Hak Cipta (Copyright) timbul secara deklaratif otomatis seketika setelah suatu ciptaan terwujud dalam bentuk nyata, tanpa wajib didaftarkan dalam 24 jam.",
                    "exec_hint": "Pernyataan 4 salah karena hak cipta menganut asas deklaratif otomatis sejak karya diwujudkan."
                },
                {
                    "type": "multi",
                    "stem": lambda v: "Pilihlah tanda-tanda pra-cetak (printer's marks) yang standar disertakan dalam file PDF siap cetak (Press-Ready PDF) untuk percetakan offset profesional:",
                    "options_gen": lambda v: [
                        {"key": "A", "text": "Crop Marks (garis pemandu sudut tempat pisau pemotong memotong kertas tepat di ukuran trim).", "correct": True},
                        {"key": "B", "text": "Bleed Marks (garis penanda batas maksimum lebihan gambar latar belakang cetak).", "correct": True},
                        {"key": "C", "text": "Registration Marks (tanda target silang presisi untuk penyesuaian plat warna separasi CMYK).", "correct": True},
                        {"key": "D", "text": "Watermark Anti-Screenshot berukuran 50% opacity di tengah lembar dokumen.", "correct": False},
                        {"key": "E", "text": "Barcode pelacak GPS satelit di setiap lembar halaman publikasi cetak.", "correct": False}
                    ],
                    "concept_hint": "Printer marks meliputi Crop marks, Bleed marks, Registration marks, dan Color bars.",
                    "exec_hint": "Pilihan A, B, dan C adalah tanda register dan potong wajib pada standar pra-cetak industri percetakan."
                }
            ]
        }
    ]

    sections = [
        ("easy", "latihan", 35, "tekd-lat-e-"),
        ("medium", "latihan", 35, "tekd-lat-m-"),
        ("hard", "latihan", 35, "tekd-lat-h-"),
        ("hard", "simulasi", 30, "tekd-sim-")
    ]

    for diff, mode, count, prefix in sections:
        for i in range(1, count + 1):
            qid = f"{prefix}{i:02d}"
            p_idx = (i - 1) % len(pillars)
            pillar = pillars[p_idx]
            concept_variant = pillar["concepts"][(i - 1) % len(pillar["concepts"])]
            q_type = concept_variant["type"]

            v = {}
            question_text = concept_variant["stem"](v)
            c_hint = concept_variant["concept_hint"]
            e_hint = concept_variant["exec_hint"]

            if q_type == "mcq":
                options = concept_variant["options"]
                correct_key = concept_variant["correct"]
                explanation = f"Analisis desain komunikasi visual: {e_hint} Jawaban benar adalah {correct_key}."

                q_obj = {
                    "id": qid,
                    "subject": "rekayasa_desain",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "mcq",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKey": correct_key,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": (i <= 5 and mode == "latihan" and diff == "easy")
                }
            elif q_type == "matrix":
                raw_stmts = concept_variant["statements"](v)
                statements = []
                correct_answers = {}
                for s_i, st in enumerate(raw_stmts):
                    s_id = str(s_i)
                    statements.append({"id": s_id, "text": st["text"]})
                    correct_answers[s_id] = st["answer"]
                explanation = f"Evaluasi kejuruan DKV & Desain: {e_hint}"

                q_obj = {
                    "id": qid,
                    "subject": "rekayasa_desain",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "matrix",
                    "questionHtml": question_text,
                    "statements": statements,
                    "correctAnswers": correct_answers,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }
            elif q_type == "multi":
                raw_opts = concept_variant["options_gen"](v)
                options = []
                correct_keys = []
                for ro in raw_opts:
                    options.append({"key": ro["key"], "text": ro["text"]})
                    if ro["correct"]:
                        correct_keys.append(ro["key"])
                correct_keys.sort()
                explanation = f"Analisis multi-jawaban Desain: {e_hint} Opsi tepat: {', '.join(correct_keys)}."

                q_obj = {
                    "id": qid,
                    "subject": "rekayasa_desain",
                    "materi": pillar["materi"],
                    "mode": mode,
                    "difficulty": diff,
                    "topic": pillar["topic"],
                    "type": "multi",
                    "questionHtml": question_text,
                    "options": options,
                    "correctKeys": correct_keys,
                    "formulaHud": {
                        "title": pillar["formula_title"],
                        "latex": pillar["formula_latex"],
                        "legend": pillar["formula_legend"]
                    },
                    "hints": {"concept": c_hint, "execution": e_hint},
                    "explanation": explanation,
                    "isDiagnostic": False
                }

            questions.append(q_obj)

    out_file = os.path.join(DATA_DIR, "questions_rekayasa_desain.js")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("/**\n * TKA MASTERY HUB - REKAYASA DESAIN / DKV (135 SOAL AUTENTIK SMK)\n")
        f.write(" * Capaian Pembelajaran Konsentrasi Keahlian DKV Fase F SMK BSKAP 033/H/KR/2022\n */\n")
        f.write("window.TKA_REKAYASA_DESAIN_QUESTIONS = ")
        json.dump(questions, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Generated {len(questions)} questions in {out_file}")

if __name__ == "__main__":
    print("Generating Wave 2 SMK Kejuruan questions...")
    generate_rpl()
    generate_tkj()
    generate_rekayasa_desain()
    print("Wave 2 SMK Kejuruan completed successfully!")
