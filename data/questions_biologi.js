/**
 * TKA MASTERY HUB — QUESTIONS_BIOLOGI.JS (135 SOAL AUTENTIK)
 */
window.TKA_BIOLOGI_QUESTIONS = [
  {
    "id": "bio-lat-e-01",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": true
  },
  {
    "id": "bio-lat-e-02",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-03",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-04",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": true
  },
  {
    "id": "bio-lat-e-05",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-06",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-07",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-08",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-09",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-10",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-11",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-12",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-13",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-14",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-15",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-16",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-17",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-18",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-19",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-20",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-21",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-22",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-23",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-24",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-25",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-26",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-27",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-28",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-29",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-30",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-31",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-32",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-33",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-34",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-e-35",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "easy",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-01",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-02",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-03",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-04",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-05",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-06",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-07",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-08",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-09",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-10",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-11",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-12",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-13",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-14",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-15",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-16",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-17",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-18",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-19",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-20",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-21",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-22",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-23",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-24",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-25",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-26",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-27",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-28",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-29",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-30",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-31",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-32",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-33",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-34",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-m-35",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "medium",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-01",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-02",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-03",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-04",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-05",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-06",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-07",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-08",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-09",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-10",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-11",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-12",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-13",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-14",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-15",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-16",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-17",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-18",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-19",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-20",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-21",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-22",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-23",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-24",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-25",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-26",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-27",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-28",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-29",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-30",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-31",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-32",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-33",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
      }
    ],
    "correctKeys": [
      "A",
      "B",
      "C"
    ],
    "formulaHud": {
      "title": "MEKANISME PEMBENTUKAN URIN DI NEFRON",
      "latex": "\\text{Filtrasi (Glomerulus)} \\to \\text{Reabsorpsi (TK Proksimal)} \\to \\text{Augmentasi (TK Distal)}",
      "legend": "• Urin Primer: Bebas sel darah & protein besar<br>• Urin Sekunder: Bebas glukosa & asam amino<br>• Urin Sebenarnya: Menuju tubulus kolektivus"
    },
    "hints": {
      "concept": "Hukum Termodinamika II membatasi transfer energi (Hukum 10% Lindeman). Energi mengalir satu arah (unidirectional) dari matahari, bukan siklis.",
      "execution": "Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis."
    },
    "explanation": "Analisis multi-jawaban: Pilihan A, B, dan C benar. Konsumen puncak memiliki energi paling sedikit dan aliran energi tidak siklis. Kunci jawaban: A, B, C.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-34",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "formulaHud": {
      "title": "METABOLISME KATABOLISME GLUKOSA",
      "latex": "\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\to 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + 36\\text{–}38\\,\\text{ATP}",
      "legend": "• Glikolisis: Sitosol (2 ATP, 2 NADH)<br>• Siklus Krebs: Matriks mitokondria<br>• Rantai Transpor Elektron: Krista"
    },
    "hints": {
      "concept": "Asam piruvat (3C) diubah menjadi Asetil Ko-A (2C) dengan melepaskan satu molekul CO₂ dan mereduksi NAD⁺ menjadi NADH.",
      "execution": "Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH."
    },
    "explanation": "Analisis biologis: Karena 1 molekul glukosa menghasilkan 2 asam piruvat, maka hasil total dekarboksilasi oksidatif adalah 2 Asetil Ko-A, 2 CO₂, dan 2 NADH. Jawaban tepat: A.",
    "isDiagnostic": false
  },
  {
    "id": "bio-lat-h-35",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "latihan",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
      }
    ],
    "correctAnswers": {
      "0": true,
      "1": true,
      "2": true,
      "3": false
    },
    "formulaHud": {
      "title": "PRINSIP SEGREGASI & ASORTASI BEBAS",
      "latex": "\\text{Dihibrid}: 9 : 3 : 3 : 1, \\quad \\text{Sentral Dogma}: \\text{DNA} \\xrightarrow{\\text{Transkripsi}} \\text{mRNA} \\xrightarrow{\\text{Translasi}} \\text{Polipeptida}",
      "legend": "• Transkripsi di nukleus oleh RNA Polimerase<br>• Translasi di ribosom oleh tRNA (antikodon)"
    },
    "hints": {
      "concept": "Hemofilia adalah kelainan resesif terpaut kromosom X ($X^h$). Ayah normal ($X^H Y$) selalu mewariskan $X^H$ normal kepada seluruh anak perempuannya.",
      "execution": "Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom."
    },
    "explanation": "Evaluasi biologi: Pernyataan 4 salah karena hemofilia terpaut pada kromosom kelamin X (gonosom), bukan autosom.",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-01",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-02",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-03",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-04",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-05",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-06",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-07",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-08",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-09",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-10",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-11",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-12",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-13",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-14",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-15",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-16",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-17",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-18",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-19",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-20",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-21",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-22",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-23",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-24",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-25",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-26",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-27",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
    "id": "bio-sim-28",
    "subject": "biologi",
    "materi": "BIOLOGI SEL & METABOLISME ENZIMATIS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Respirasi Seluler & Enzim",
    "type": "mcq",
    "questionHtml": "Pada proses respirasi aerob sel eukariotik, tahapan dekarboksilasi oksidatif asam piruvat yang berlangsung di matriks mitokondria menghasilkan produk berupa...",
    "options": [
      {
        "key": "A",
        "text": "2 Asetil Ko-A, 2 CO₂, dan 2 NADH"
      },
      {
        "key": "B",
        "text": "2 Asam sitrat, 2 FADH₂, dan 2 ATP"
      },
      {
        "key": "C",
        "text": "2 Asam laktat, 2 NAD⁺, dan 4 ATP"
      },
      {
        "key": "D",
        "text": "2 Oksaloasetat, 4 CO₂, dan 2 FADH₂"
      },
      {
        "key": "E",
        "text": "2 Etanol, 2 CO₂, dan 2 ATP netto"
      }
    ],
    "correctKey": "A",
    "isDiagnostic": false
  },
  {
    "id": "bio-sim-29",
    "subject": "biologi",
    "materi": "GENETIKA & POLA HEREDITAS",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sintesis Protein & Hukum Mendel",
    "type": "matrix",
    "questionHtml": "Seorang pria normal bergolongan darah A heterozigot menikah dengan wanita pembawa sifat hemofilia (carrier) bergolongan darah B heterozigot. Analisislah kemungkinan genotipe dan fenotipe keturunan mereka:",
    "statements": [
      {
        "id": "0",
        "text": "Peluang lahir anak bergolongan darah O (genotipe $I^O I^O$) adalah 25%."
      },
      {
        "id": "1",
        "text": "Semua anak perempuan dari pasangan tersebut dipastikan hidup normal (tidak menderita hemofilia)."
      },
      {
        "id": "2",
        "text": "Peluang anak laki-laki yang lahir menderita hemofilia adalah 50%."
      },
      {
        "id": "3",
        "text": "Penyakit hemofilia diwariskan melalui gen dominan yang terpaut pada kromosom autosom."
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
    "id": "bio-sim-30",
    "subject": "biologi",
    "materi": "FISIOLOGI ORGAN & EKOLOGI",
    "mode": "simulasi",
    "difficulty": "hard",
    "topic": "Sistem Ekskresi Nefron & Aliran Energi",
    "type": "multi",
    "questionHtml": "Pilihlah pernyataan yang BENAR mengenai hukum aliran energi dan biomassa pada rantai makanan suatu ekosistem terestrial:",
    "options": [
      {
        "key": "A",
        "text": "Hanya sekitar 10% energi yang berhasil ditransfer dari satu tingkat trofik ke tingkat trofik berikutnya."
      },
      {
        "key": "B",
        "text": "Sebagian besar energi hilang ke lingkungan dalam bentuk energi panas hasil metabolisme dan respirasi sel."
      },
      {
        "key": "C",
        "text": "Piramida energi selalu berbentuk tegak dan tidak pernah ditemukan dalam bentuk terbalik."
      },
      {
        "key": "D",
        "text": "Konsumen tersier selalu menyimpan total energi kimia lebih besar daripada produsen autotrof."
      },
      {
        "key": "E",
        "text": "Aliran energi dalam ekosistem berlangsung secara siklis berputar tanpa membutuhkan input energi surya."
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
