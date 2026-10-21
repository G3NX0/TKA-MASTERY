/**
 * TKA MASTERY HUB — QUESTIONS_FISIKA.JS (135 SOAL AUTENTIK)
 */
window.TKA_FISIKA_QUESTIONS = [
  {
    "id": "fis-lat-e-01",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 30\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$5.5\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$4.9\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$4.4\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$6.1\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$3.9\\text{ m/s²}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": true
  },
  {
    "id": "fis-lat-e-02",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-03",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-04",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 40\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$981\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$946\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$906\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$856\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$871\\text{ Hz}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": true
  },
  {
    "id": "fis-lat-e-05",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-06",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-07",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 90\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18.9\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$20.6\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$19.4\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$20.0\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$18.4\\text{ m/s²}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-08",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-09",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-10",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 20\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$815\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$890\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$800\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$850\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$925\\text{ Hz}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 20} \\times 800 = 850\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 20} \\times 800 = 850\\text{ Hz}$. Sehingga opsi yang benar adalah D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-11",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-12",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-13",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 70\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$13.6\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$14.7\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$15.3\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$14.1\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$13.1\\text{ m/s²}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 70(0{,}6) = -2.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 14.1\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 70(0{,}6) = -2.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 14.1\\text{ m/s}^2$. Sehingga opsi yang benar adalah D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-14",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-15",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-16",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 25\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$828\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$938\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$903\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$813\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$863\\text{ Hz}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 25} \\times 800 = 863\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 25} \\times 800 = 863\\text{ Hz}$. Sehingga opsi yang benar adalah E.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-17",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-18",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-19",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 50\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$9.6\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$8.5\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$8.0\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$10.2\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$9.0\\text{ m/s²}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 50(0{,}6) = 10.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 9.0\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 50(0{,}6) = 10.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 9.0\\text{ m/s}^2$. Sehingga opsi yang benar adalah E.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-20",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-21",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-22",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 30\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$877\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$842\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$952\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$827\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$917\\text{ Hz}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 30} \\times 800 = 877\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 30} \\times 800 = 877\\text{ Hz}$. Sehingga opsi yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-23",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-24",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-25",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 30\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$4.9\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$3.9\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$5.5\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$4.4\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$6.1\\text{ m/s²}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$. Sehingga opsi yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-26",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-27",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-28",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 35\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$931\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$891\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$966\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$841\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$856\\text{ Hz}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 35} \\times 800 = 891\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 35} \\times 800 = 891\\text{ Hz}$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-29",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-30",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-31",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 90\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$20.0\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$19.4\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$18.9\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$20.6\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$18.4\\text{ m/s²}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-32",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-33",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-34",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 40\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$981\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$946\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$906\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$871\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$856\\text{ Hz}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-e-35",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-01",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 30\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$6.1\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$4.9\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$4.4\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$3.9\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$5.5\\text{ m/s²}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-02",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-03",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-04",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 40\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$946\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$981\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$906\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$871\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$856\\text{ Hz}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-05",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-06",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-07",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 90\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18.4\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$18.9\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$19.4\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$20.6\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$20.0\\text{ m/s²}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-08",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-09",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-10",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 20\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$925\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$800\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$890\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$850\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$815\\text{ Hz}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 20} \\times 800 = 850\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 20} \\times 800 = 850\\text{ Hz}$. Sehingga opsi yang benar adalah D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-11",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-12",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-13",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 70\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$13.6\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$15.3\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$14.7\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$14.1\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$13.1\\text{ m/s²}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 70(0{,}6) = -2.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 14.1\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 70(0{,}6) = -2.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 14.1\\text{ m/s}^2$. Sehingga opsi yang benar adalah D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-14",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-15",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-16",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 25\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$828\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$938\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$813\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$903\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$863\\text{ Hz}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 25} \\times 800 = 863\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 25} \\times 800 = 863\\text{ Hz}$. Sehingga opsi yang benar adalah E.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-17",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-18",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-19",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 50\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$10.2\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$9.6\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$8.5\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$8.0\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$9.0\\text{ m/s²}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 50(0{,}6) = 10.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 9.0\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 50(0{,}6) = 10.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 9.0\\text{ m/s}^2$. Sehingga opsi yang benar adalah E.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-20",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-21",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-22",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 30\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$877\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$827\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$842\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$917\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$952\\text{ Hz}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 30} \\times 800 = 877\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 30} \\times 800 = 877\\text{ Hz}$. Sehingga opsi yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-23",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-24",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-25",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 30\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$4.9\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$3.9\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$5.5\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$6.1\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$4.4\\text{ m/s²}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$. Sehingga opsi yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-26",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-27",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-28",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 35\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$841\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$891\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$966\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$931\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$856\\text{ Hz}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 35} \\times 800 = 891\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 35} \\times 800 = 891\\text{ Hz}$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-29",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-30",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-31",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 90\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18.9\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$19.4\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$20.6\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$20.0\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$18.4\\text{ m/s²}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-32",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-33",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-34",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 40\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$946\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$981\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$906\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$856\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$871\\text{ Hz}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-m-35",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-01",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 30\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$5.5\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$4.9\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$3.9\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$4.4\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$6.1\\text{ m/s²}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-02",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-03",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-04",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 40\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$871\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$981\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$906\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$856\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$946\\text{ Hz}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-05",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-06",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-07",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 90\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$20.6\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$20.0\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$19.4\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$18.9\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$18.4\\text{ m/s²}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-08",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-09",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-10",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 20\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$815\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$925\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$800\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$850\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$890\\text{ Hz}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 20} \\times 800 = 850\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 20} \\times 800 = 850\\text{ Hz}$. Sehingga opsi yang benar adalah D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-11",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-12",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-13",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 70\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$15.3\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$13.6\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$13.1\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$14.1\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$14.7\\text{ m/s²}$"
      }
    ],
    "correctKey": "D",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 70(0{,}6) = -2.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 14.1\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 70(0{,}6) = -2.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 14.1\\text{ m/s}^2$. Sehingga opsi yang benar adalah D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-14",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-15",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-16",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 25\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$813\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$828\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$903\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$938\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$863\\text{ Hz}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 25} \\times 800 = 863\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 25} \\times 800 = 863\\text{ Hz}$. Sehingga opsi yang benar adalah E.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-17",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-18",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-19",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 50\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$9.6\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$8.0\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$10.2\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$8.5\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$9.0\\text{ m/s²}$"
      }
    ],
    "correctKey": "E",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 50(0{,}6) = 10.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 9.0\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 50(0{,}6) = 10.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 9.0\\text{ m/s}^2$. Sehingga opsi yang benar adalah E.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-20",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-21",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-22",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 30\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$877\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$827\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$952\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$917\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$842\\text{ Hz}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 30} \\times 800 = 877\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 30} \\times 800 = 877\\text{ Hz}$. Sehingga opsi yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-23",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-24",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-25",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 30\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$4.9\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$3.9\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$4.4\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$5.5\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$6.1\\text{ m/s²}$"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 30(0{,}6) = 22.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 4.9\\text{ m/s}^2$. Sehingga opsi yang benar adalah A.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-26",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-27",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-28",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 35\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$856\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$891\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$966\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$841\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$931\\text{ Hz}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 35} \\times 800 = 891\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 35} \\times 800 = 891\\text{ Hz}$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-29",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-30",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "EFEK FOTOLISTRIK EINSTEIN",
      "latex": "E_k = hf - W_0 = h(f - f_0)",
      "legend": "• $E_k$: Energi kinetik elektron (J/eV)<br>• $h$: Konstanta Planck ($6{{,}}63 \\times 10^{-34}$ J·s)<br>• $W_0$: Fungsi kerja logam (eV)"
    },
    "hints": {
      "concept": "Teori klasik memprediksi butuh waktu akumulasi energi dan intensitas tinggi pasti bisa melepaskan elektron, yang bertentangan dengan kenyataan fotolistrik.",
      "execution": "Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$."
    },
    "explanation": "Analisis opsi multi-jawaban: Pilihan A, B, dan C adalah bukti mutlak foton sebagai paket energi diskret kuantum $E = hf$. Jawaban benar: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-31",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 90\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18.9\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$19.4\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$20.0\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$18.4\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$20.6\\text{ m/s²}$"
      }
    ],
    "correctKey": "B",
    "formulaHud": {
      "title": "HUKUM II NEWTON & GLBB",
      "latex": "\\Sigma F = m \\cdot a, \\quad v_t^2 = v_0^2 + 2as",
      "legend": "• $\\Sigma F$: Gaya total (N)<br>• $m$: Massa (kg)<br>• $a$: Percepatan (m/s²)"
    },
    "hints": {
      "concept": "Uraikan gaya $F$ ke sumbu horizontal ($F\\cos\\theta$) dan vertikal ($F\\sin\\theta$), lalu tentukan gaya normal $N = mg - F\\sin\\theta$.",
      "execution": "Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$."
    },
    "explanation": "Langkah penyelesaian: Gaya normal $N = 4(10) - 90(0{,}6) = -14.0\\text{ N}$. Gaya gesek $f_k = \\mu_k N$. Percepatan $a = \\frac{F_x - f_k}{m} = 19.4\\text{ m/s}^2$. Sehingga opsi yang benar adalah B.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-32",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PERSAMAAN KONTINUITAS & BERNOULLI",
      "latex": "A_1 v_1 = A_2 v_2, \\quad P_1 + \\frac{1}{2}\\rho v_1^2 + \\rho g h_1 = P_2 + \\frac{1}{2}\\rho v_2^2 + \\rho g h_2",
      "legend": "• $A$: Luas penampang (m²)<br>• $v$: Kelajuan fluida (m/s)<br>• $P$: Tekanan absolut (Pa)"
    },
    "hints": {
      "concept": "Teorema Torricelli menyatakan $v = \\sqrt{2gh}$, di mana kelajuan pancaran tidak bergantung pada massa jenis fluida maupun luas penampang lubang.",
      "execution": "Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Kelajuan hanya ditentukan oleh kedalaman fluida $h$ dan percepatan gravitasi $g$.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-33",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "formulaHud": {
      "title": "EFISIENSI MESIN CARNOT",
      "latex": "\\eta = 1 - \\frac{T_C}{T_H} = \\frac{W}{Q_H}",
      "legend": "• $\\eta$: Efisiensi termal<br>• $T_H$: Suhu reservoir panas (K)<br>• $T_C$: Suhu reservoir dingin (K)"
    },
    "hints": {
      "concept": "$E_k = \\frac{3}{2}kT$ dan $v_{rms} = \\sqrt{\\frac{3RT}{M}}$. Gas ideal mengabaikan gaya antarmolekul.",
      "execution": "Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus."
    },
    "explanation": "Analisis opsi multi-jawaban: Kelajuan $v_{rms}$ berbanding terbalik terhadap akar massa molekul $\\sqrt{M}$, bukan berbanding lurus. Jawaban benar: A, C, D.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-34",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 40\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$871\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$946\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$906\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$981\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$856\\text{ Hz}$"
      }
    ],
    "correctKey": "C",
    "formulaHud": {
      "title": "EFEK DOPPLER GELOMBANG BUNYI",
      "latex": "f_p = \\left(\\frac{v \\pm v_p}{v \\mp v_s}\\right) f_s",
      "legend": "• $f_p$: Frekuensi pendengar (Hz)<br>• $f_s$: Frekuensi sumber (Hz)<br>• $v$: Cepat rambat bunyi (m/s)"
    },
    "hints": {
      "concept": "Sumber bunyi mendekati pengamat diam ($v_p = 0$), sehingga penyebut berkurang ($v - v_s$), menghasilkan frekuensi yang lebih tinggi.",
      "execution": "Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$."
    },
    "explanation": "Langkah penyelesaian: Rumus: $f_p = \\frac{340}{340 - 40} \\times 800 = 906\\text{ Hz}$. Sehingga opsi yang benar adalah C.",
    "isDiagnostic": false
  },
  {
    "id": "fis-lat-h-35",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "IMPEDANSI RANGKAIAN R-L-C SERI",
      "latex": "Z = \\sqrt{R^2 + (X_L - X_C)^2}, \\quad X_L = \\omega L, \\quad X_C = \\frac{1}{\\omega C}",
      "legend": "• $Z$: Impedansi total ($\\Omega$)<br>• $X_L$: Reaktansi induktif ($\\Omega$)<br>• $X_C$: Reaktansi kapasitif ($\\Omega$)"
    },
    "hints": {
      "concept": "Saat resonansi, sifat induktif dan kapasitif saling meniadakan, sehingga arus efektif $I = \\frac{V}{Z} = \\frac{V}{R}$ mencapai nilai maksimum.",
      "execution": "Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum."
    },
    "explanation": "Evaluasi pernyataan berdasar kaidah fisis: Karena impedansi minimum, arus justru berada pada titik puncak (maksimum), bukan minimum.",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-01",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 30\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$4.4\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$4.9\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$3.9\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$5.5\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$6.1\\text{ m/s²}$"
      }
    ],
    "correctKey": "B",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-02",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-03",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-04",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 40\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$856\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$946\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$906\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$871\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$981\\text{ Hz}$"
      }
    ],
    "correctKey": "C",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-05",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-06",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-07",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 90\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$18.9\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$18.4\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$19.4\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$20.6\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$20.0\\text{ m/s²}$"
      }
    ],
    "correctKey": "C",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-08",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-09",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-10",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 20\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$925\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$815\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$890\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$850\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$800\\text{ Hz}$"
      }
    ],
    "correctKey": "D",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-11",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-12",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-13",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 70\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$15.3\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$13.6\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$13.1\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$14.1\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$14.7\\text{ m/s²}$"
      }
    ],
    "correctKey": "D",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-14",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-15",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-16",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 25\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$903\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$828\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$813\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$938\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$863\\text{ Hz}$"
      }
    ],
    "correctKey": "E",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-17",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-18",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-19",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 50\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.4$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$10.2\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$8.5\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$9.6\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$8.0\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$9.0\\text{ m/s²}$"
      }
    ],
    "correctKey": "E",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-20",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 1.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 5.0 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-21",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-22",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 30\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$877\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$952\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$827\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$917\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$842\\text{ Hz}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-23",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-24",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-25",
    "subject": "fisika",
    "materi": "KINEMATIKA & DINAMIKA GERAK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Gerak Lurus & Hukum Newton",
    "type": "mcq",
    "questionHtml": "Sebuah balok bermassa $4\\text{ kg}$ ditarik di atas lantai mendatar kasar dengan gaya konstan $F = 30\\text{ N}$ membentuk sudut $37^\\circ$ terhadap horizontal ($\\cos 37^\\circ = 0{,}8$, $\\sin 37^\\circ = 0{,}6$). Koefisien gesek kinetik antara balok dan lantai adalah $\\mu_k = 0.2$. Jika percepatan gravitasi $g = 10\\text{ m/s}^2$, percepatan gerak balok tersebut adalah...",
    "options": [
      {
        "key": "A",
        "text": "$4.9\\text{ m/s²}$"
      },
      {
        "key": "B",
        "text": "$4.4\\text{ m/s²}$"
      },
      {
        "key": "C",
        "text": "$3.9\\text{ m/s²}$"
      },
      {
        "key": "D",
        "text": "$6.1\\text{ m/s²}$"
      },
      {
        "key": "E",
        "text": "$5.5\\text{ m/s²}$"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-26",
    "subject": "fisika",
    "materi": "FLUIDA STATIS & DINAMIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Tekanan Hidrostatis & Hukum Bernoulli",
    "type": "matrix",
    "questionHtml": "Sebuah tangki penampung air berukuran besar memiliki lubang kebocoran kecil pada kedalaman $h = 2.25\\text{ meter}$ di bawah permukaan air terbuka ($g = 10\\text{ m/s}^2$). Analisislah pernyataan mekanika fluida berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Kelajuan semburan air yang keluar dari lubang adalah tepat 6.71 m/s sesuai teorema Torricelli."
      },
      {
        "id": "1",
        "text": "Jika diameter lubang diperbesar dua kali lipat, kelajuan semburan air keluar akan meningkat dua kali lipat."
      },
      {
        "id": "2",
        "text": "Debit air yang keluar berbanding lurus dengan luas penampang lubang kebocoran tangki."
      },
      {
        "id": "3",
        "text": "Massa jenis fluida mempengaruhi kelajuan pancaran semburan air teoritis dari lubang."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": false,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-27",
    "subject": "fisika",
    "materi": "TERMODINAMIKA & TEORI KINETIK GAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Termodinamika & Siklus Mesin Kalor",
    "type": "multi",
    "questionHtml": "Berdasarkan teori kinetik gas ideal, manakah pernyataan di bawah ini yang benar mengenai partikel gas monoatomik dalam wadah tertutup?",
    "options": [
      {
        "key": "A",
        "text": "Energi kinetik rata-rata partikel gas hanya dipengaruhi oleh suhu mutlak sistem gas."
      },
      {
        "key": "B",
        "text": "Kelajuan efektif partikel gas ($v_{rms}$) berbanding lurus dengan akar massa molekul gas."
      },
      {
        "key": "C",
        "text": "Tumbukan yang terjadi antar partikel gas maupun dengan dinding bejana bersifat lenting sempurna."
      },
      {
        "key": "D",
        "text": "Tekanan gas terjadi akibat transfer momentum partikel saat bertumbukan dengan dinding bejana."
      },
      {
        "key": "E",
        "text": "Gaya tarik-menarik antar molekul gas ideal sangat kuat pada kerapatan partikel tinggi."
      }
    ],
    "correctKeys": [
      "A",
      "C",
      "D"
    ],
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-28",
    "subject": "fisika",
    "materi": "GELOMBANG BUNYI & ELEKTROMAGNETIK",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Doppler & Intensitas Bunyi",
    "type": "mcq",
    "questionHtml": "Sebuah mobil ambulans bergerak dengan kelajuan $v_s = 35\\text{ m/s}$ sambil membunyikan sirine berfrekuensi $f_s = 800\\text{ Hz}$ mendekati seorang pengamat yang sedang berdiri diam di tepi jalan raya. Jika cepat rambat bunyi di udara adalah $v = 340\\text{ m/s}$, maka frekuensi sirine yang didengar oleh pengamat adalah...",
    "options": [
      {
        "key": "A",
        "text": "$931\\text{ Hz}$"
      },
      {
        "key": "B",
        "text": "$891\\text{ Hz}$"
      },
      {
        "key": "C",
        "text": "$841\\text{ Hz}$"
      },
      {
        "key": "D",
        "text": "$966\\text{ Hz}$"
      },
      {
        "key": "E",
        "text": "$856\\text{ Hz}$"
      }
    ],
    "correctKey": "B",
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-29",
    "subject": "fisika",
    "materi": "LISTRIK DINAMIS & RANGKAIAN AC",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Hukum Kirchhoff & Impedansi R-L-C",
    "type": "matrix",
    "questionHtml": "Pada kondisi resonansi rangkaian seri $R-L-C$ bolak-balik, evaluasilah kebenaran pernyataan karakteristik kelistrikan berikut:",
    "statements": [
      {
        "id": "0",
        "text": "Besar reaktansi induktif sama persis dengan besar reaktansi kapasitif ($X_L = X_C$)."
      },
      {
        "id": "1",
        "text": "Impedansi total rangkaian mencapai nilai minimum yang setara dengan nilai hambatan murni resistor ($Z = R$)."
      },
      {
        "id": "2",
        "text": "Faktor daya rangkaian bolak-balik pada keadaan resonansi bernilai maksimum yaitu $\\cos\\phi = 1$."
      },
      {
        "id": "3",
        "text": "Arus efektif yang mengalir pada rangkaian mencapai nilai paling minimum."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "isDiagnostic": false
  },
  {
    "id": "fis-sim-30",
    "subject": "fisika",
    "materi": "FISIKA MODERN & RELATIVITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Efek Fotolistrik & Dilatasi Waktu",
    "type": "multi",
    "questionHtml": "Pada fenomena efek fotolistrik, manakah fakta eksperimental yang TIDAK DAPAT dijelaskan oleh teori gelombang cahaya klasik Maxwell?",
    "options": [
      {
        "key": "A",
        "text": "Elektron langsung terlepas tanpa jeda waktu tunda (kurang dari $10^{-9}$ detik) saat cahaya berfrekuensi cukup menyinari logam."
      },
      {
        "key": "B",
        "text": "Adanya frekuensi ambang batas ($f_0$); cahaya dengan $f < f_0$ tidak dapat melepaskan elektron berapapun intensitasnya."
      },
      {
        "key": "C",
        "text": "Energi kinetik maksimum fotoelektron tidak bergantung pada intensitas cahaya datang, melainkan hanya frekuensi foton."
      },
      {
        "key": "D",
        "text": "Peningkatan intensitas cahaya menambah jumlah elektron yang terlepas per satuan waktu jika $f > f_0$."
      },
      {
        "key": "E",
        "text": "Cahaya merambat lurus dengan kelajuan gelombang transversal di ruang hampa udara."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "isDiagnostic": false
  }
];
