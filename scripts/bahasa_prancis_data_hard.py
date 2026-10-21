# -*- coding: utf-8 -*-
"""
BAHASA PRANCIS - PAKET SOAL LATIHAN SULIT (HARD / HOTS) - 25 BUTIR
Standar: Kurikulum Merdeka TKA 2026 / BSKAP 033/H/KR/2024 / CEFR B1 (DELF B1 / Baccalauréat)
Distribusi:
- 8 Butir: Le Conditionnel (Présent & Passé) serta Struktur Hipotesis Bersyarat (Phrases avec 'Si')
- 9 Butir: Le Subjonctif Présent (Déclencheurs de nécessité, volonté, sentiment, doute & verbes irréguliers)
- 8 Butir: Voix passive, Pronoms relatifs composés (auquel, avec lequel), Connecteurs logiques (bien que, afin que) & Civilisation Francophone HOTS
"""

BAHASA_PRANCIS_HARD_ITEMS = [
    {
        "id": "fra-lat-h-01",
        "materi": "GRAMMAIRE AVANCÉE: L'HYPOTHÈSE AVEC 'SI' (IRRÉEL DU PRÉSENT)",
        "topic": "Pengandaian Kontrafaktual Masa Kini Menggunakan Rumus 'Si + Imparfait -> Conditionnel Présent'",
        "stem": "Dua mahasiswa memimpikan keliling dunia di sela-sela ujian:\n'Si nous ( ... ) assez d'économies sur notre compte bancaire, nous ( ... ) un grand voyage à travers toute l'Amérique du Sud pendant six mois.'\nPasangan bentuk kata kerja yang TEPAT untuk memenuhi kaidah pengandaian tak nyata masa kini (Irréel du présent) adalah...",
        "correct": "avions / ferions (klausa pengandaian 'si' menggunakan Imparfait 'avions' dan klausa akibat menggunakan Conditionnel Présent 'ferions').",
        "distractors": [
            "avons / ferons (bentuk pengandaian kemungkinan masa depan nyata yang menggunakan Présent dan Futur Simple).",
            "aurions / faisions (urutan terbalik yang salah besar karena bahasa Prancis melarang mutlak verba Conditionnel berada di dalam anak kalimat si).",
            "avions eu / aurions fait (bentuk pengandaian penyesalan masa lampau Irréel du passé dengan Plus-que-parfait dan Conditionnel Passé).",
            "aurons / ferions (penggunaan Futur Simple pada klausa si yang dilarang keras dalam sintaksis baku bahasa Prancis)."
        ],
        "formula": {
            "title": "L'HYPOTHÈSE AVEC 'SI': IRRÉEL DU PRÉSENT",
            "latex": "\\mathbf{Si} + \\mathbf{Imparfait (avions)}, \\quad \\mathbf{Conditionnel \\text{ } Présent (ferions)}",
            "legend": "• Menyatakan situasi hipotetis yang bertentangan dengan fakta kenyataan saat ini.<br>• ATURAN EMAS: Kata 'Si' TIDAK PERNAH boleh diikuti oleh kata kerja bentuk Conditionnel!"
        },
        "hints": {
            "concept": "Struktur pengandaian tidak nyata pada masa kini (Irréel du présent) dibentuk dengan pola: 'Si + Imparfait, ... Conditionnel Présent'. Ingat pepatah tata bahasa Prancis terkenal: 'Les si n'aiment pas les -rais' (Kata 'si' tidak pernah boleh diikuti langsung oleh akhiran Conditionnel -rais/-rait).",
            "execution": "Si + Imparfait (avions) -> Conditionnel Présent (ferions)."
        }
    },
    {
        "id": "fra-lat-h-02",
        "materi": "GRAMMAIRE AVANCÉE: LE SUBJONCTIF PRÉSENT (LA NÉCESSITÉ)",
        "topic": "Pemicu Subjonctif Impersonal 'il faut que' dengan Verba Tidak Beraturan 'faire'",
        "stem": "Instruksi tegas direktur operasional kepada seluruh tim teknis:\n'Pour respecter les délais de livraison imposés par le client, il faut absolument que vous ( ... ) tous les tests de sécurité avant ce soir.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'faire' untuk subjek 'vous' adalah...",
        "correct": "fassiez (akar tidak beraturan fass- + akhiran Subjonctif persona kedua jamak -iez).",
        "distractors": [
            "faites (bentuk Présent de l'indicatif yang keliru karena klausa il faut que mewajibkan modus Subjonctif).",
            "faisiez (bentuk Imparfait dari indikatif yang keliru fungsi modalitas).",
            "feriez (bentuk Conditionnel Présent yang tidak cocok dengan pemicu keniscayaan il faut que).",
            "faissiez (kesalahan ortografi dengan menggandakan huruf konsonan s ganda pada bentuk subjonctif)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF PRÉSENT: VERBE FAIRE",
            "latex": "\\text{Déclencheur: } \\mathbf{Il \\text{ } faut \\text{ } que} \\quad \\implies \\quad \\text{vous } \\mathbf{fassiez} \\quad (\\text{radical: fass-})",
            "legend": "• Ungkapan impersonal kewajiban 'il faut que' SELALU menuntut modus Subjonctif.<br>• Verba faire berubah akar menjadi 'fass-': que je fasse, que nous fassions, que vous fassiez."
        },
        "hints": {
            "concept": "Frasa impersonal 'il faut que' (harus/wajib bahwa) adalah pemicu mutlak modus Subjonctif. Kata kerja 'faire' memiliki akar Subjonctif tidak beraturan, yaitu 'fass-'. Untuk subjek 'vous', bentuknya adalah 'fassiez' (que vous fassiez).",
            "execution": "il faut que + vous + faire -> 'fassiez'."
        }
    },
    {
        "id": "fra-lat-h-03",
        "materi": "GRAMMAIRE AVANCÉE: LE SUBJONCTIF PRÉSENT (LE SENTIMENT)",
        "topic": "Ekspresi Perasaan Emosional yang Memicu Subjonctif dari Verba 'être'",
        "stem": "Seorang ibu mengungkapkan kebahagiaan atas prestasi anaknya:\n'Je suis tellement fière et heureuse que tu ( ... ) parmi les lauréats du concours national de piano.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'être' untuk persona kedua tunggal 'tu' adalah...",
        "correct": "sois (bentuk Subjonctif Présent persona kedua tunggal dari verba tidak beraturan être).",
        "distractors": [
            "es (bentuk indikatif waktu sekarang yang keliru karena ungkapan perasaan bahagia être heureux que mewajibkan subjonctif).",
            "soit (bentuk Subjonctif untuk persona ketiga tunggal il/elle).",
            "soyez (bentuk Subjonctif untuk persona kedua jamak/formal vous).",
            "seras (bentuk Futur Simple indikatif yang melanggar tuntutan modus perasaan emosional)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DU VERBE ÊTRE",
            "latex": "\\text{Expression de sentiment (être heureux que)} \\quad \\implies \\quad \\text{Subjonctif: } \\mathbf{que \\text{ } tu \\text{ } sois}",
            "legend": "• Konjugasi Subjonctif être: que je sois, que tu sois, qu'il soit, que nous soyons, que vous soyez, qu'ils soient.<br>• Persona 'tu' berakhiran huruf '-s' (sois)."
        },
        "hints": {
            "concept": "Ungkapan perasaan hati atau emosi (seperti 'être fier/heureux que') mewajibkan kata kerja dalam anak kalimat menggunakan modus Subjonctif. Bentuk Subjonctif untuk verba 'être' dengan subjek 'tu' adalah 'sois' (que tu sois).",
            "execution": "sentiment 'heureuse que' + tu -> 'sois'."
        }
    },
    {
        "id": "fra-lat-h-04",
        "materi": "GRAMMAIRE AVANCÉE: LA VOIX PASSIVE",
        "topic": "Transformasi Kalimat Pasif Waktu Lampau dengan Pelaku Tindakan Preposisi 'par'",
        "stem": "Dalam ulasan sejarah arsitektur Prancis abad kesembilan belas:\n'La célèbre tour métallique de Paris ( ... ) en 1889 par l'ingénieur Gustave Eiffel à l'occasion de l'Exposition universelle.'\nPasangan kata kerja bantu dan Participe Passé pasif yang TEPAT untuk subjek feminin tunggal 'La célèbre tour' adalah...",
        "correct": "a été conçue (bentuk pasif Passé Composé: a été + Participe Passé feminin tunggal conçue dengan tanda cédille dan accord -e).",
        "distractors": [
            "a conçu (bentuk aktif yang salah makna karena membuat menara Eiffel merancang insinyur Gustave Eiffel).",
            "est conçue (bentuk pasif Présent yang bertentangan dengan penanda sejarah masa lampau en 1889).",
            "a été conçu (kesalahan mengabaikan penyesuaian gender feminin -e untuk kata benda la tour).",
            "avait été concurrue (kesalahan pemilihan bentuk verba yang tidak bermakna merancang)."
        ],
        "formula": {
            "title": "LA VOIX PASSIVE AU PASSÉ COMPOSÉ",
            "latex": "\\text{Sujet (Fém. Sing.)} + \\mathbf{a \\text{ } été} + \\mathbf{conçue} + \\mathbf{par} + \\text{Agent}",
            "legend": "• Struktur pasif Passé Composé: avoir été + Participe Passé.<br>• Participe Passé selalu bersepakat dengan subjek penerima: la tour (feminin) $\\rightarrow$ conçue."
        },
        "hints": {
            "concept": "Kalimat pasif dalam waktu lampau Passé Composé dibentuk dengan: 'a été / ont été + Participe Passé'. Karena subjeknya adalah 'La célèbre tour' (feminin tunggal), Participe Passé dari verba 'concevoir' harus diberi akhiran feminin '-e' (conçue, dengan tanda cédille ç).",
            "execution": "Pasif lampau feminin = 'a été conçue'."
        }
    },
    {
        "id": "fra-lat-h-05",
        "materi": "GRAMMAIRE AVANCÉE: LES CONNECTEURS LOGIQUES AVEC LE SUBJONCTIF",
        "topic": "Konjungsi Pertentangan 'bien que' yang Mewajibkan Pemakaian Modus Subjonctif",
        "stem": "Dalam artikel opini ekonomi tentang tren konsumsi masyarakat:\n'Bien que les prix de l'énergie ( ... ) considérablement ces derniers mois, la consommation globale d'électricité ne diminue pas.'\nBentuk konjugasi kata kerja 'augmenter' yang TEPAT setelah konjungsi subordinatif 'bien que' untuk subjek jamak 'les prix' adalah...",
        "correct": "aient augmenté (bentuk Subjonctif Passé yang dituntut oleh konjungsi konsesif 'bien que').",
        "distractors": [
            "ont augmenté (bentuk indikatif Passé Composé yang keliru karena konjungsi bien que mewajibkan subjonctif).",
            "augmentent (bentuk Présent indikatif yang melanggar aturan modus anak kalimat konsesif).",
            "augmentaient (bentuk Imparfait indikatif yang tidak berstatus subjonctif).",
            "avaient augmenté (bentuk Plus-que-parfait indikatif yang salah modus)."
        ],
        "formula": {
            "title": "CONNECTEUR CONCESSIF: BIEN QUE + SUBJONCTIF",
            "latex": "\\mathbf{Bien \\text{ } que} + \\text{Subjonctif} \\quad (\\text{les prix } \\rightarrow \\mathbf{aient \\text{ } augmenté})",
            "legend": "• 'Bien que' (meskipun/walaupun) SELALU mewajibkan verba dalam modus Subjonctif.<br>• Dilarang keras menggunakan Indikatif setelah 'bien que'!"
        },
        "hints": {
            "concept": "Konjungsi konsesif 'bien que' (meskipun/walaupun) dalam bahasa Prancis selalu menuntut kata kerja dalam modus Subjonctif. Karena peristiwanya sudah tuntas terjadi, digunakan Subjonctif Passé: 'aient augmenté' (ils aient + augmenté).",
            "execution": "bien que + les prix (jamak) -> 'aient augmenté'."
        }
    },
    {
        "id": "fra-lat-h-06",
        "materi": "GRAMMAIRE AVANCÉE: PRONOMS RELATIFS COMPOSÉS (LEQUEL, AUQUEL...)",
        "topic": "Pronomina Relatif Majemuk Maskulin Tunggal dengan Preposisi 'à' (auquel)",
        "stem": "Dalam laporan evaluasi seminar ilmiah kedokteran:\n'Le colloque international sur les neurosciences ( ... ) nous avons assisté la semaine dernière a apporté des éclairages novateurs.'\nBentuk pronomina relatif majemuk yang TEPAT untuk menggantikan kata benda maskulin tunggal 'le colloque' yang terikat dengan verba 'assister à' adalah...",
        "correct": "auquel (kontraksi preposisi à + lequel yang dituntut oleh verba assister à sesuatu).",
        "distractors": [
            "duquel (kontraksi preposisi de + lequel yang hanya digunakan untuk verba berpreposisi de).",
            "lequel (pronomina relatif majemuk tanpa preposisi yang keliru untuk valensi verba assister à).",
            "dans lequel (frasa preposisional spasial di dalam yang tidak membentuk kolokasi resmi assister à un événement).",
            "à laquelle (bentuk feminin yang keliru gender untuk kata maskulin le colloque)."
        ],
        "formula": {
            "title": "PRONOMS RELATIFS COMPOSÉS AVEC LA PRÉPOSITION À",
            "latex": "\\text{le colloque (Masc. Sing.)} + \\mathbf{assister \\text{ } à} \\quad \\implies \\quad \\mathbf{à} + \\mathbf{lequel} = \\mathbf{auquel}",
            "legend": "• Menggantikan benda non-manusia yang diawali preposisi à.<br>• à + lequel = auquel; à + laquelle = à laquelle; à + lesquels = auxquels; à + lesquelles = auxquelles."
        },
        "hints": {
            "concept": "Kata kerja 'assister' (menghadiri) selalu berpasangan dengan preposisi 'à' (assister à quelque chose). Untuk benda maskulin tunggal 'le colloque', preposisi 'à' berkontraksi dengan pronomina relatif majemuk 'lequel' menjadi 'auquel'.",
            "execution": "assister à + le colloque -> 'auquel'."
        }
    },
    {
        "id": "fra-lat-h-07",
        "materi": "GRAMMAIRE AVANCÉE: LE CONDITIONNEL PASSÉ (LE REGRET)",
        "topic": "Menyatakan Penyesalan Masa Lampau Menggunakan Rumus 'aurais / serais + Participe Passé'",
        "stem": "Seorang pelamar kerja menyesali keterlambatan pengiriman berkasnya:\n'Si j'avais envoyé mon dossier de candidature plus tôt, j'( ... ) la chance de passer l'entretien d'embauche.'\nBentuk Conditionnel Passé yang TEPAT dari verba 'avoir' untuk melengkapi kalimat pengandaian masa lampau (Irréel du passé) tersebut adalah...",
        "correct": "aurais eu (bentuk Conditionnel Passé persona pertama tunggal: aurais + Participe Passé eu).",
        "distractors": [
            "avais eu (bentuk Plus-que-parfait indikatif yang hanya boleh berada di anak kalimat si, bukan klausa utama).",
            "aurais (bentuk Conditionnel Présent yang keliru waktu karena penyesalan merujuk pada peristiwa masa lalu).",
            "ai eu (bentuk Passé Composé indikatif yang menyatakan kepastian fakta, bukan pengandaian kontrafaktual).",
            "serais eu (kesalahan fatal kata kerja bantu sein/être untuk verba avoir)."
        ],
        "formula": {
            "title": "L'HYPOTHÈSE AVEC 'SI': IRRÉEL DU PASSÉ (LE REGRET)",
            "latex": "\\mathbf{Si} + \\mathbf{Plus-que-parfait (avais envoyé)}, \\quad \\mathbf{Conditionnel \\text{ } Passé (aurais eu)}",
            "legend": "• Menyatakan penyesalan atau situasi yang tidak pernah terjadi di masa lampau.<br>• Rumus Conditionnel Passé: avoir/être au conditionnel présent + Participe Passé."
        },
        "hints": {
            "concept": "Pengandaian kontrafaktual masa lampau (Irréel du passé / penyesalan) memiliki rumus baku: 'Si + Plus-que-parfait, ... Conditionnel Passé'. Kalimat anak: 'Si j'avais envoyé...'. Kalimat utama: Conditionnel Passé dari avoir = 'j'aurais eu'.",
            "execution": "Conditionnel Passé dari avoir untuk persona 'je' = 'aurais eu'."
        }
    },
    {
        "id": "fra-lat-h-08",
        "materi": "CIVILISATION & HISTOIRE: LE SIÈCLE DES LUMIÈRES",
        "topic": "Pengaruh Gerakan Filsafat Pencerahan Abad ke-18 dan Tokoh Utamanya di Prancis",
        "stem": "Bacalah wacana sejarah pemikiran Prancis berikut:\n'Au dix-huitième siècle, le mouvement intellectuel et philosophique des \"Lumières\", incarné par des penseurs illustres tels que Voltaire, Montesquieu, Rousseau et Diderot, a profondément transformé la société européenne. En prônant l'usage souverain de la raison critique, la tolérance religieuse, la séparation des pouvoirs politiques et la liberté individuelle contre l'absolutisme monarchique et l'obscurantisme clérical, ils ont posé les fondements idéologiques majeurs qui ont conduit à la Révolution française de 1789.'\nBerdasarkan wacana di atas, nilai fundamental yang diperjuangkan oleh para filsuf era 'Lumières' adalah...",
        "correct": "Pemberdayaan akal budi kritis, toleransi beragama, pemisahan kekuasaan negara, dan kebebasan individu melawan tirani monarki absolut.",
        "distractors": [
            "Penguatan kekuasaan mutlak raja tanpa batas dan penghapusan seluruh hak asasi warga sipil.",
            "Penolakan mutlak terhadap ilmu pengetahuan alam dan penegakan teokrasi keagamaan garis keras.",
            "Penghapusan seluruh institusi peradilan umum demi membentuk sistem kediktatoran militer tunggal.",
            "Pemberantasan karya sastra dan pembakaran seluruh ensiklopedia ilmiah dari perpustakaan publik."
        ],
        "formula": {
            "title": "LES LUMIÈRES ET LA RÉVOLUTION FRANÇAISE",
            "latex": "\\text{Philosophes (Voltaire, Rousseau, Montesquieu)} \\implies \\text{Raison, Tolérance, Liberté, Séparation des pouvoirs}",
            "legend": "• Menentang absolutisme monarki dan dogma keagamaan kolot.<br>• Meletakkan dasar ideologi Deklarasi Hak Asasi Manusia 1789."
        },
        "hints": {
            "concept": "Teks secara eksplisit menguraikan nilai inti para pemikir 'Lumières': 'l'usage souverain de la raison critique, la tolérance religieuse, la séparation des pouvoirs politiques et la liberté individuelle contre l'absolutisme monarchique'.",
            "execution": "Nilai fundamental = akal budi kritis, toleransi, pemisahan kekuasaan, dan kebebasan individu."
        }
    },
    {
        "id": "fra-lat-h-09",
        "materi": "GRAMMAIRE AVANCÉE: LE SUBJONCTIF PRÉSENT (LE DOUTE)",
        "topic": "Verba Keraguan 'douter que' yang Mewajibkan Pemakaian Modus Subjonctif",
        "stem": "Dalam perdebatan mengenai prakiraan cuaca di pegunungan:\n'Le ciel est encore très couvert ce matin; je doute fort que nous ( ... ) faire cette randonnée au sommet aujourd'hui.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'pouvoir' untuk subjek 'nous' adalah...",
        "correct": "puissions (akar tidak beraturan puiss- + akhiran Subjonctif persona pertama jamak -ions).",
        "distractors": [
            "pouvons (bentuk Présent de l'indicatif yang keliru karena verba douter que mengekspresikan keraguan mutlak).",
            "pouvions (bentuk Imparfait indikatif yang salah fungsi gramatikal).",
            "pourrions (bentuk Conditionnel Présent yang tidak dapat menjadi pelengkap klausa douter que).",
            "puissons (kesalahan penambahan akhiran -ons indikatif pada akar subjonctif puiss-)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DU VERBE POUVOIR (DOUTE)",
            "latex": "\\text{Expression de doute (douter que)} \\quad \\implies \\quad \\text{Subjonctif: } \\mathbf{que \\text{ } nous \\text{ } puissions}",
            "legend": "• Konjugasi Subjonctif pouvoir: que je puisse, que tu puisses, qu'il puisse, que nous puissions, que vous puissiez, qu'ils puissent.<br>• Radical tidak beraturan: 'puiss-'."
        },
        "hints": {
            "concept": "Kata kerja 'douter que' (meragukan bahwa) mengekspresikan ketidakpastian/keraguan, sehingga WAJIB diikuti oleh modus Subjonctif. Verba 'pouvoir' memiliki akar Subjonctif tidak beraturan 'puiss-'. Untuk subjek 'nous', bentuknya adalah 'puissions'.",
            "execution": "douter que + nous + pouvoir -> 'puissions'."
        }
    },
    {
        "id": "fra-lat-h-10",
        "materi": "GRAMMAIRE AVANCÉE: PRONOMS RELATIFS COMPOSÉS (AVEC LEQUEL...)",
        "topic": "Pronomina Relatif Majemuk dengan Preposisi 'avec' untuk Benda Maskulin Jamak",
        "stem": "Dalam panduan penggunaan perangkat lunak desain grafis:\n'Voici les nouveaux outils numériques ( ... ) nos graphistes ont conçu la maquette du site internet.'\nBentuk pronomina relatif majemuk yang TEPAT setelah preposisi sarana 'avec' untuk kata benda maskulin jamak 'les outils' adalah...",
        "correct": "avec lesquels (preposisi avec + pronomina relatif majemuk maskulin jamak lesquels).",
        "distractors": [
            "avec laquelle (bentuk feminin tunggal yang keliru gender dan jumlah untuk kata benda maskulin un outil).",
            "avec lequel (bentuk maskulin tunggal yang keliru jumlah untuk kata benda jamak les outils).",
            "avec lesquelles (bentuk feminin jamak yang keliru gender).",
            "avec qui (pronomina qui setelah preposisi yang hanya diperuntukkan secara khusus bagi manusia, bukan peralatan non-persona)."
        ],
        "formula": {
            "title": "PRONOMS RELATIFS COMPOSÉS APRÈS PRÉPOSITION",
            "latex": "\\text{les outils (Masc. Plur.)} + \\mathbf{avec} \\quad \\implies \\quad \\mathbf{avec \\text{ } lesquels}",
            "legend": "• Merujuk pada benda mati (non-personne): gunakan lequel / laquelle / lesquels / lesquelles.<br>• 'avec qui' hanya sah bila merujuk pada manusia."
        },
        "hints": {
            "concept": "Setelah preposisi (seperti avec, pour, sur, dans), jika yang dirujuk adalah benda mati (les outils, maskulin jamak), bahasa Prancis mewajibkan pemakaian pronomina relatif majemuk 'lesquels' (avec lesquels). Rujukan 'avec qui' hanya boleh untuk manusia.",
            "execution": "les outils (maskulin jamak) + avec -> 'avec lesquels'."
        }
    },
    {
        "id": "fra-lat-h-11",
        "materi": "GRAMMAIRE AVANCÉE: LE SUBJONCTIF DU VERBE AVOIR",
        "topic": "Konjugasi Subjonctif dari Kata Kerja 'avoir' untuk Persona Ketiga Tunggal 'il/elle'",
        "stem": "Sebelum keberangkatan rombongan ekspedisi ke kutub utara:\n'Le guide exige que chaque participant ( ... ) un équipement thermique parfaitement adapté aux températures négatives.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'avoir' untuk persona ketiga tunggal 'chaque participant' adalah...",
        "correct": "ait (bentuk Subjonctif Présent persona ketiga tunggal dari verba tidak beraturan avoir).",
        "distractors": [
            "a (bentuk Présent de l'indicatif yang keliru karena verba tuntutan exiger que mewajibkan subjonctif).",
            "avait (bentuk Imparfait indikatif yang tidak berstatus subjonctif).",
            "aura (bentuk Futur Simple indikatif yang salah modus).",
            "aie (bentuk Subjonctif persona pertama tunggal untuk subjek je)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DU VERBE AVOIR",
            "latex": "\\text{Subjonctif avoir: } \\text{que j'aie, que tu aies, } \\mathbf{qu'il \\text{ } ait}, \\text{ que nous ayons, que vous ayez, qu'ils aient}",
            "legend": "• Verba tuntutan / perintah (exiger que) mewajibkan Subjonctif.<br>• chaque participant = il $\\rightarrow$ 'qu'il ait'."
        },
        "hints": {
            "concept": "Kata kerja tuntutan/kehendak 'exiger que' (menuntut agar) mewajibkan pemakaian modus Subjonctif. Konjugasi Subjonctif verba 'avoir' untuk persona ketiga tunggal (il/elle/chaque participant) adalah 'ait' (qu'il ait).",
            "execution": "exiger que + chaque participant + avoir -> 'ait'."
        }
    },
    {
        "id": "fra-lat-h-12",
        "materi": "CIVILISATION & SOCIÉTÉ: LA FRANCOPHONIE DANS LE MONDE",
        "topic": "Status Bahasa Prancis sebagai Bahasa Resmi dan Bahasa Kerja Internasional di Berbagai Benua",
        "stem": "Bacalah wacana kebahasaan global berikut:\n'L'Organisation internationale de la Francophonie (OIF) regroupe des dizaines d'États à travers les cinq continents. Au-delà de l'Europe (France, Belgique, Suisse, Luxembourg), le français occupe une place prépondérante sur le continent africain, où il constitue la langue d'enseignement et d'administration dans de nombreux pays de l'Afrique subsaharienne et du Maghreb. En Amérique du Nord, la province canadienne du Québec préserve farouchement son identité linguistique francophone par des lois de protection rigoureuses.'\nBerdasarkan wacana di atas, salah satu bukti nyata vitalitas global bahasa Prancis di luar benua Eropa adalah...",
        "correct": "Perannya yang dominan sebagai bahasa administrasi dan pendidikan di banyak negara Afrika, serta status resminya di provinsi Quebec (Kanada).",
        "distractors": [
            "Penetapan bahasa Prancis sebagai bahasa wajib satu-satunya di seluruh negara bagian Amerika Serikat.",
            "Kewajiban seluruh penduduk benua Asia untuk menguasai sastra Prancis klasik sebelum bekerja.",
            "Penggantian total seluruh bahasa lokal di Amerika Latin dengan dialek bahasa Prancis abad pertengahan.",
            "Penghapusan seluruh bahasa pribumi di Afrika demi melarang penggunaan bahasa selain bahasa Prancis."
        ],
        "formula": {
            "title": "LA FRANCOPHONIE DANS LE MONDE",
            "latex": "\\text{Francophonie globale} = \\text{Afrique (Enseignement/Admin)} + \\text{Québec (Nord-Amérique)} + \\text{Europe}",
            "legend": "• Bahasa Prancis adalah salah satu dari sedikit bahasa yang dituturkan di 5 benua.<br>• Merupakan bahasa resmi di PBB, Uni Eropa, dan Olimpiade."
        },
        "hints": {
            "concept": "Teks secara lugas memaparkan bahwa di luar Eropa, bahasa Prancis memegang peran vital di benua Afrika sebagai bahasa pendidikan dan administrasi, serta di Amerika Utara khususnya provinsi Quebec (Kanada).",
            "execution": "Pilihan yang menyebutkan peran administrasi/pendidikan di Afrika dan status di provinsi Quebec."
        }
    },
    {
        "id": "fra-lat-h-13",
        "materi": "GRAMMAIRE AVANCÉE: LE CONDITIONNEL DE L'INFORMATION INCERTAINE",
        "topic": "Penggunaan Conditionnel dalam Bahasa Jurnalistik untuk Menyatakan Berita yang Belum Terkonfirmasi",
        "stem": "Dalam warta berita kilat harian tentang peristiwa bencana alam:\n'D'après les premières dépêches d'agences de presse, le séisme ( ... ) plusieurs blessés graves dans le sud de l'île.'\nBentuk kata kerja yang TEPAT dalam laras bahasa jurnalistik Prancis untuk menyatakan peristiwa yang belum diverifikasi secara resmi (information non confirmée) adalah...",
        "correct": "aurait fait (bentuk Conditionnel Passé yang digunakan untuk melaporkan informasi faktual yang belum terkonfirmasi oleh pihak berwenang).",
        "distractors": [
            "a fait (bentuk Passé Composé indikatif yang menegaskan fakta kepastian mutlak tanpa jarak jurnalistik).",
            "faisait (bentuk Imparfait indikatif yang mengaburkan sifat kesegaran berita bencana).",
            "fera (bentuk Futur Simple indikatif yang keliru menempatkan bencana yang sudah terjadi ke masa depan).",
            "fasse (bentuk Subjonctif yang tidak memiliki fungsi sintaksis sebagai predikat utama kalimat berita)."
        ],
        "formula": {
            "title": "CONDITIONNEL JOURNALISTIQUE (INFORMATION INCERTAINE)",
            "latex": "\\text{D'après les sources... } + \\mathbf{Conditionnel \\text{ (aurait fait)}} = \\text{diduga telah memakan korban}",
            "legend": "• Standar etika jurnalistik Prancis untuk menjaga jarak objektivitas berita dugaan.<br>• Padanan: 'diduga telah menyebabkan / dikabarkan bahwa...'."
        },
        "hints": {
            "concept": "Dalam bahasa jurnalistik Prancis, untuk memberitakan suatu informasi yang baru didengar dan belum dikonfirmasi secara resmi oleh otoritas, wajib digunakan bentuk Conditionnel (Conditionnel journalistique). Untuk kejadian lampau, digunakan Conditionnel Passé: 'aurait fait'.",
            "execution": "Berita dugaan jurnalistik masa lampau = 'aurait fait'."
        }
    },
    {
        "id": "fra-lat-h-14",
        "materi": "GRAMMAIRE AVANCÉE: LE SUBJONCTIF DU VERBE ALLER",
        "topic": "Bentuk Subjonctif Tidak Beraturan dari Kata Kerja 'aller' (que nous allions)",
        "stem": "Dokter spesialis kesehatan kerja memberikan rekomendasi tegas:\n'Il est primordial que mon collègue et moi ( ... ) consulter un ergothérapeute pour nos douleurs dorsales récurrentes.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'aller' untuk subjek 'mon collègue et moi' (nous) adalah...",
        "correct": "allions (akar kata kerja all- + akhiran Subjonctif persona pertama jamak -ions).",
        "distractors": [
            "aillons (kesalahan mempertahankan akar tunggal aill- pada persona jamak nous).",
            "allons (bentuk Présent de l'indicatif yang keliru karena il est primordial que menuntut modus subjonctif).",
            "allionss (kesalahan ejaan penambahan huruf s ganda di akhir kata).",
            "irions (bentuk Conditionnel Présent yang tidak cocok dengan pemicu keniscayaan il est primordial que)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DU VERBE ALLER (ALTERNANCE DE RADICAL)",
            "latex": "\\text{que j'aille, que tu ailles, qu'il aille, } \\mathbf{que \\text{ } nous \\text{ } allions}, \\text{ que vous alliez, qu'ils aillent}",
            "legend": "• Subjonctif verba aller memiliki dua akar: 'aill-' (tunggal & ils) dan 'all-' (nous & vous).<br>• Mon collègue et moi = nous $\\rightarrow$ 'que nous allions'."
        },
        "hints": {
            "concept": "Kata kerja 'aller' pada modus Subjonctif memiliki pergantian akar: 'aill-' untuk je/tu/il/ils (que j'aille, qu'ils aillent) dan 'all-' untuk nous/vous (que nous allions, que vous alliez). Untuk subjek 'mon collègue et moi' (= nous), bentuknya adalah 'allions'.",
            "execution": "nous + Subjonctif dari aller = 'allions'."
        }
    },
    {
        "id": "fra-lat-h-15",
        "materi": "GRAMMAIRE AVANCÉE: LE PARTICIPE PRÉSENT AVANCÉ",
        "topic": "Penggunaan Participe Présent Mandiri sebagai Pengganti Klausa Relatif Kausal",
        "stem": "Dalam pengumuman resmi pembatalan jadwal penerbangan:\n'( ... ) d'importantes turbulences atmosphériques sur la trajectoire de vol, le commandant de bord a pris la décision de faire demi-tour.'\nBentuk Participe Présent dari kata kerja 'craindre' (khawatir akan) yang TEPAT untuk mengawali kalimat sebab tersebut adalah...",
        "correct": "Craignant (akar nous au présent craign- + akhiran Participe Présent -ant).",
        "distractors": [
            "Craint (bentuk Participe Passé yang bermakna pasif ditakuti, bukan aktif mengkhawatirkan).",
            "En craignant (bentuk Gérondif yang keliru karena subjek aksi sebab tidak bertindak simultan dengan cara tindakan).",
            "Craignait (bentuk Imparfait indikatif yang tidak dapat mengawali klausa partisipial tanpa kata sambung).",
            "Ayant craint (bentuk majemuk yang kurang ringkas dibandingkan Participe Présent langsung untuk situasi aktif)."
        ],
        "formula": {
            "title": "LE PARTICIPE PRÉSENT CAUSAL",
            "latex": "\\text{Craignant la tempête... } \\iff \\text{Comme il craignait la tempête, le commandant...}",
            "legend": "• Berfungsi menggantikan klausa sebab (comme / parce que).<br>• Dibentuk dari akar nous au présent: nous craignons $\\rightarrow$ craign- + -ant = craignant."
        },
        "hints": {
            "concept": "Le Participe Présent dibentuk dari akar 'nous' waktu sekarang (nous craignons -> craign-) + akhiran '-ant' (craignant). Participe Présent dapat berdiri sendiri tanpa 'en' untuk menggantikan klausa kausalitas (Karena mengkhawatirkan adanya turbulensi...).",
            "execution": "Participe Présent dari craindre = 'Craignant'."
        }
    },
    {
        "id": "fra-lat-h-16",
        "materi": "GRAMMAIRE AVANCÉE: LES CONNECTEURS DU BUT (POUR QUE / AFIN QUE)",
        "topic": "Konjungsi Tujuan 'afin que' yang Menuntut Subjonctif Bila Subjek Berbeda",
        "stem": "Seorang insinyur perangkat lunak mendokumentasikan kode program:\n'L'architecte système a rédigé un guide technique très détaillé afin que les nouveaux développeurs ( ... ) comprendre immédiatement l'architecture du projet.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'pouvoir' untuk subjek jamak 'les nouveaux développeurs' adalah...",
        "correct": "puissent (konjugasi Subjonctif Présent persona ketiga jamak yang dituntut oleh konjungsi tujuan afin que).",
        "distractors": [
            "peuvent (bentuk Présent indikatif yang melanggar hukum modus konjungsi tujuan afin que).",
            "pourront (bentuk Futur Simple indikatif yang salah modus).",
            "pouvaient (bentuk Imparfait indikatif yang salah modus).",
            "puissiez (bentuk Subjonctif untuk persona kedua jamak vous)."
        ],
        "formula": {
            "title": "EXPRESSION DU BUT: AFIN QUE + SUBJONCTIF",
            "latex": "\\mathbf{afin \\text{ } que / pour \\text{ } que} + \\text{Subjonctif (sujets différents)}",
            "legend": "• Bila subjek kedua klausa berbeda (L'architecte vs les développeurs), gunakan afin que + Subjonctif.<br>• les développeurs (ils) $\\rightarrow$ 'puissent'."
        },
        "hints": {
            "concept": "Konjungsi tujuan 'afin que' (agar/supaya) selalu mewajibkan kata kerja dalam modus Subjonctif bila subjek kedua klausa berbeda. Subjek klausa kedua adalah 'les nouveaux développeurs' (= ils). Bentuk Subjonctif dari 'pouvoir' untuk 'ils' adalah 'puissent'.",
            "execution": "afin que + ils + pouvoir -> 'puissent'."
        }
    },
    {
        "id": "fra-lat-h-17",
        "materi": "GRAMMAIRE AVANCÉE: LE SUBJONCTIF DU VERBE SAVOIR",
        "topic": "Akar Subjonctif Tidak Beraturan dari Kata Kerja 'savoir' (sach-)",
        "stem": "Instruksi kepala sekolah menjelang simulasi evakuasi kebakaran:\n'Il est indispensable que chaque élève ( ... ) exactement quelle issue de secours emprunter en cas d'urgence.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'savoir' untuk persona ketiga tunggal 'chaque élève' adalah...",
        "correct": "sache (akar tidak beraturan sach- + akhiran Subjonctif persona ketiga tunggal -e).",
        "distractors": [
            "sait (bentuk Présent de l'indicatif yang keliru karena il est indispensable que menuntut subjonctif).",
            "sachent (bentuk konjugasi Subjonctif persona ketiga jamak ils/elles yang keliru jumlah untuk subjek tunggal chaque élève).",
            "savait (bentuk Imparfait indikatif yang salah modus).",
            "saura (bentuk Futur Simple indikatif yang salah modus)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DU VERBE SAVOIR",
            "latex": "\\text{Radical irrégulier: } \\mathbf{sach-} \\quad \\rightarrow \\quad \\text{qu'il/elle } \\mathbf{sache}",
            "legend": "• Konjugasi Subjonctif savoir: que je sache, que tu saches, qu'il sache, que nous sachions, que vous sachiez, qu'ils sachent.<br>• chaque élève = il $\\rightarrow$ 'sache'."
        },
        "hints": {
            "concept": "Kata kerja 'savoir' (mengetahui) memiliki akar Subjonctif tidak beraturan yang unik: 'sach-'. Akhiran untuk orang ketiga tunggal (il/elle/chaque élève) adalah '-e'. Maka bentuknya adalah 'sache'.",
            "execution": "savoir di Subjonctif untuk chaque élève = 'sache'."
        }
    },
    {
        "id": "fra-lat-h-18",
        "materi": "CIVILISATION & PATRIMOINE: LE REPAS GASTRONOMIQUE DES FRANÇAIS (UNESCO)",
        "topic": "Pengakuan Warisan Budaya Takbenda UNESCO atas Ritual Santap Gastronomi Prancis",
        "stem": "Bacalah wacana kebudayaan Prancis berikut:\n'En 2010, l'UNESCO a inscrit \"le repas gastronomique des Français\" sur la liste représentative du patrimoine culturel immatériel de l'humanité. Cette reconnaissance internationale ne célèbre pas seulement l'excellence de recettes raffinées, mais avant tout une pratique sociale coutumière destinée à célébrer les moments les plus importants de la vie. Ce rituel communautaire accorde une place primordiale à la convivialité, au partage, au choix minutieux d'ingrédients de terroir et au respect d'un schéma strict: apéritif, entrée, plat de résistance avec poisson ou viande, fromage, dessert et digestif, le tout harmonieusement accordé avec des vins spécifiques.'\nBerdasarkan teks di atas, esensi utama pengakuan UNESCO terhadap santap gastronomi Prancis adalah...",
        "correct": "Praktik sosial komunal yang merayakan kebersamaan (convivialité), tradisi berbagi, perpaduan hidangan dengan anggur, dan struktur susunan menu yang teratur.",
        "distractors": [
            "Penetapan harga makanan termahal di seluruh restoran berbintang Michelin di kota Paris.",
            "Kewajiban seluruh warga negara Prancis untuk memakan daging olahan setiap hari tanpa sayuran.",
            "Larangan menyajikan makanan lokal khas daerah selain hidangan resmi istana kepresidenan.",
            "Pemberian subsidi uang tunai kepada masyarakat yang mengonsumsi makanan cepat saji impor."
        ],
        "formula": {
            "title": "LE REPAS GASTRONOMIQUE (PATRIMOINE UNESCO 2010)",
            "latex": "\\text{Patrimoine immatériel} = \\text{Pratique sociale} + \\text{Convivialité} + \\text{Structure des plats} + \\text{Accord mets-vins}",
            "legend": "• Bukan sekadar resep masak, melainkan ritual sosial kebersamaan kultural.<br>• Menyatukan seni memilih bahan, tata meja, dan etika makan bersama."
        },
        "hints": {
            "concept": "Teks menegaskan bahwa pengakuan UNESCO bukan hanya soal resep mewah, melainkan: 'une pratique sociale coutumière ... accorde une place primordiale à la convivialité, au partage ... et au respect d'un schéma strict ... le tout harmonieusement accordé avec des vins'.",
            "execution": "Esensi = Praktik sosial perayaan kebersamaan (convivialité), struktur urutan menu, dan harmoni anggur."
        }
    },
    {
        "id": "fra-lat-h-19",
        "materi": "GRAMMAIRE AVANCÉE: ACCORD DU PARTICIPE PASSÉ AVEC UN VERBE PRONOMINAL RÉCIPROQUE",
        "topic": "Penentuan Fungsi Objek Langsung (COD) vs Tak Langsung (COI) pada Verba Refleksif Resiprokal",
        "stem": "Dalam kisah persahabatan dua penulis terkenal:\n'Pendant plus de vingt ans, ces deux écrivains se sont ( ... ) des lettres d'admiration mutuelle chaque semaine.'\nBentuk Participe Passé dari kata kerja 's'écrire' yang TEPAT untuk kalimat tersebut adalah...",
        "correct": "écrit (tanpa accord -s karena pronomina resiprokal 'se' berfungsi sebagai objek tak langsung COI: écrire à quelqu'un; sedangkan COD-nya 'des lettres' berada di belakang kata kerja).",
        "distractors": [
            "écrits (kesalahan penambahan accord jamak -s karena salah mengira pronomina resiprokal se sebagai COD).",
            "écrite (kesalahan penambahan bentuk feminin tunggal).",
            "écrites (kesalahan menyelaraskan dengan objek des lettres yang posisinya berada di belakang kata kerja).",
            "écrivaient (bentuk Imparfait yang merusak konstruksi Passé Composé se sont)."
        ],
        "formula": {
            "title": "ACCORD DU PARTICIPE PASSÉ DES VERBES PRONOMINAUX",
            "latex": "\\text{écrire } \\mathbf{à \\text{ } quelqu'un} \\implies \\text{'se' est } \\mathbf{COI} \\quad \\implies \\quad \\mathbf{PAS \\text{ } D'ACCORD} \\quad (\\text{se sont } \\mathbf{écrit})",
            "legend": "• Pertanyaan kunci: Ils ont écrit à qui? $\\rightarrow$ à eux-mêmes ('se' = COI).<br>• Objek langsung (des lettres) berada SETELAH kata kerja $\\rightarrow$ Tidak ada accord!"
        },
        "hints": {
            "concept": "Aturan sulit verba pronominal: Participe Passé hanya bersepakat jika pronomina refleksifnya adalah COD. Kata kerja 'écrire' menuntut preposisi 'à' (écrire à quelqu'un). Jadi 'se' di sini adalah COI (menulis kepada satu sama lain). Karena COD-nya 'des lettres' terletak SETELAH verba, Participe Passé TIDAK MENDAPAT AKHIRAN apapun (écrit).",
            "execution": "se = COI, COD di belakang -> Participe Passé tetap tanpa accord = 'écrit'."
        }
    },
    {
        "id": "fra-lat-h-20",
        "materi": "GRAMMAIRE AVANCÉE: LE PLUS-QUE-PARFAIT DE L'INDICATIF",
        "topic": "Menyatakan Anterioritas Waktu di Masa Lampau Menggunakan Plus-que-parfait",
        "stem": "Dalam laporan penyelidikan kasus pencurian karya seni di museum:\n'Quand la police est arrivée sur les lieux du crime, les cambrioleurs ( ... ) déjà toutes les issues de secours du bâtiment.'\nBentuk kata kerja bantu dan Participe Passé pada kala Plus-que-parfait yang TEPAT dari kata kerja 'bloquer' untuk subjek jamak 'les cambrioleurs' adalah...",
        "correct": "avaient bloqué (Plus-que-parfait dengan kata kerja bantu avaient + Participe Passé bloqué untuk menyatakan aksi yang selesai sebelum polisi tiba).",
        "distractors": [
            "ont bloqué (bentuk Passé Composé yang keliru karena tidak menunjukkan tingkatan anterioritas waktu lampau sebelum peristiwa lampau lain).",
            "bloquaient (bentuk Imparfait yang menyatakan proses berlangsung, bukan aksi tuntas sebelum kedatangan polisi).",
            "étaient bloqués (bentuk pasif yang keliru memutarbalikkan peran pencuri menjadi pihak yang terblokir).",
            "bloqueront (bentuk Futur Simple yang bertentangan dengan kerangka narasi investigasi masa lalu)."
        ],
        "formula": {
            "title": "LE PLUS-QUE-PARFAIT: L'ANTÉRIORITÉ DANS LE PASSÉ",
            "latex": "\\mathbf{Plus-que-parfait (avaient bloqué)} \\quad \\rightarrow \\quad \\mathbf{Passé \\text{ } Composé (est arrivée)}",
            "legend": "• Aksi pertama yang terjadi lebih dulu di masa lalu: Plus-que-parfait (avoir/être à l'imparfait + Participe Passé).<br>• Aksi kedua yang menyusul: Passé Composé."
        },
        "hints": {
            "concept": "Plus-que-parfait digunakan untuk menyatakan peristiwa masa lalu yang terjadi dan tuntas LEBIH DULU daripada peristiwa masa lalu lainnya (anterioritas). Perampok sudah memblokir pintu (aksi 1) SEBELUM polisi tiba (aksi 2: est arrivée). Rumusnya: Imparfait dari avoir (avaient) + Participe Passé (bloqué).",
            "execution": "Aksi lampau lebih dulu = 'avaient bloqué'."
        }
    },
    {
        "id": "fra-lat-h-21",
        "materi": "GRAMMAIRE AVANCÉE: LE SUBJONCTIF APRÈS LES VERBES D'OPINION À LA FORME NÉGATIVE",
        "topic": "Pembalikan Modus Indikatif Menjadi Subjonctif Saat Verba Opini Dibentuk Negatif",
        "stem": "Dalam perdebatan politik mengenai efektivitas undang-undang baru:\n'Le député de l'opposition affirme: \"Je ne pense absolument pas que cette réforme fiscale ( ... ) une solution équitable pour la classe moyenne.\"' \nBentuk konjugasi kata kerja 'être' yang TEPAT setelah verba opini bentuk negatif 'ne pas penser que' adalah...",
        "correct": "soit (bentuk Subjonctif Présent persona ketiga tunggal yang wajib dipicu oleh verba opini yang dinegasikan).",
        "distractors": [
            "est (bentuk Indikatif yang hanya digunakan bila verba opini berbentuk kalimat positif afirmatif).",
            "sera (bentuk Futur Simple indikatif yang salah modus untuk opini negatif).",
            "serait (bentuk Conditionnel yang tidak mencerminkan modus wajib subjonctif setelah ne pas penser que).",
            "soient (bentuk Subjonctif jamak yang keliru jumlah untuk subjek tunggal cette réforme fiscale)."
        ],
        "formula": {
            "title": "VERBES D'OPINION: AFFIRMATIF (INDICATIF) VS NÉGATIF (SUBJONCTIF)",
            "latex": "\\text{Je pense qu'elle } \\mathbf{est} \\text{ (Indicatif)} \\quad \\leftrightarrow \\quad \\text{Je ne pense pas qu'elle } \\mathbf{soit} \\text{ (Subjonctif)}",
            "legend": "• Kalimat afirmatif (penser/croire que): kepastian $\\rightarrow$ Indicatif.<br>• Kalimat negatif (ne pas penser/croire que): ketidakpastian/keraguan $\\rightarrow$ SUBJONCTIF."
        },
        "hints": {
            "concept": "Verba opini seperti 'penser' dan 'croire' diikuti oleh Indikatif bila kalimatnya POSITIF (Je pense que c'est bien). Namun, bila verba opini tersebut berbentuk NEGATIF (Je ne pense pas que...), ia memicu ketidakpastian dan WAJIB diikuti oleh modus SUBJONCTIF. Subjonctif dari 'être' untuk 'cette réforme' (= elle) adalah 'soit'.",
            "execution": "ne pas penser que + elle -> 'soit'."
        }
    },
    {
        "id": "fra-lat-h-22",
        "materi": "CIVILISATION & PRINCIPES RÉPUBLICAINS: LA LAÏCITÉ EN FRANCE",
        "topic": "Makna Konseptual dan Yuridis Prinsip 'Laïcité' dalam Republik Prancis",
        "stem": "Bacalah teks konstitusi kewarganegaraan Prancis berikut:\n'La laïcité est un principe constitutionnel fondamental de la République française, consacré notamment par la loi historique de 1905 sur la séparation des Églises et de l'État. Elle garantit à la fois la liberté absolue de conscience (liberté de croire ou de ne pas croire) et la stricte neutralité religieuse de l'État et de ses services publics. Dans l'espace scolaire public, ce principe protège les élèves de tout prosélytisme afin de préserver l'égalité et l'émancipation citoyenne.'\nBerdasarkan teks di atas, definisi paling komprehensif dari prinsip 'laïcité' di Prancis adalah...",
        "correct": "Netralitas mutlak institusi negara terhadap agama yang berdampingan dengan jaminan kebebasan nurani warga untuk beriman atau tidak beriman.",
        "distractors": [
            "Pelarangan total terhadap seluruh peribadatan agama secara privat di dalam rumah masing-masing warga.",
            "Penetapan salah satu agama resmi tunggal yang wajib dipeluk oleh seluruh pegawai negeri dan pejabat pemerintah.",
            "Pemberian kewenangan kepada para pemuka agama untuk menyusun kurikulum sains di universitas negeri.",
            "Kewajiban menghapus seluruh bangunan rumah ibadah bersejarah demi memajukan modernisasi tata kota."
        ],
        "formula": {
            "title": "LE PRINCIPE DE LAÏCITÉ (LOI DE 1905)",
            "latex": "\\text{Laïcité} = \\text{Neutralité de l'État} + \\text{Liberté de conscience} + \\text{Égalité de tous les citoyens}",
            "legend": "• Pemisahan total antara urusan agama dan administrasi negara.<br>• Melindungi hak setiap warga negara untuk memilih keyakinan tanpa diskriminasi."
        },
        "hints": {
            "concept": "Teks mendefinisikan laïcité sebagai dua pilar yang menyatu: 'garantit à la fois la liberté absolue de conscience (liberté de croire ou de ne pas croire) et la stricte neutralité religieuse de l'État et de ses services publics'.",
            "execution": "Definisi = Netralitas institusi negara berdampingan dengan jaminan kebebasan nurani warga."
        }
    },
    {
        "id": "fra-lat-h-23",
        "materi": "GRAMMAIRE AVANCÉE: LA CONCORDANCE DES TEMPS AU DISCOURS INDIRECT DU PASSÉ",
        "topic": "Pergeseran Kala Waktu dari Présent Menjadi Imparfait dalam Kalimat Wicara Tak Langsung Lampau",
        "stem": "Seorang juru bicara kepresidenan mengutip ucapan menteri dalam konferensi pers:\nUcapan langsung: Le ministre a déclaré hier: «Je suis déterminé à accélérer la transition écologique.»\nBentuk kalimat wicara tak langsung (Discours indirect au passé) yang BENAR secara gramatika adalah...",
        "correct": "Le ministre a déclaré hier qu'il était déterminé à accélérer la transition écologique.",
        "distractors": [
            "Le ministre a déclaré hier qu'il est déterminé à accélérer la transition écologique.",
            "Le ministre a déclaré hier qu'il sera déterminé à accélérer la transition écologique.",
            "Le ministre a déclaré hier qu'il soit déterminé à accélérer la transition écologique.",
            "Le ministre a déclaré hier qu'il avait été déterminé à accélérer la transition écologique."
        ],
        "formula": {
            "title": "CONCORDANCE DES TEMPS AU PASSÉ (DISCOURS INDIRECT)",
            "latex": "\\text{Verbe introducteur au passé (a déclaré)}: \\quad \\mathbf{Présent} \\quad \\rightarrow \\quad \\mathbf{Imparfait (était)}",
            "legend": "• Bila verba pengantar berbentuk lampau (a déclaré), terjadi pergeseran kala waktu.<br>• Présent (je suis) bergeser menjadi Imparfait (il était)."
        },
        "hints": {
            "concept": "Dalam transformasi wicara tidak langsung (Discours indirect), jika kata kerja pengantarnya berada dalam kala lampau (a déclaré), maka kata kerja di dalam kutipan wajib bergeser: Présent berubah menjadi Imparfait (je suis -> il était).",
            "execution": "je suis -> bergeser menjadi 'il était'."
        }
    },
    {
        "id": "fra-lat-h-24",
        "materi": "GRAMMAIRE AVANCÉE: LE SUBJONCTIF DU VERBE VOULOIR",
        "topic": "Bentuk Subjonctif Tidak Beraturan dari Kata Kerja 'vouloir' (veui- / voul-)",
        "stem": "Instruksi tegas pelatih kepala sebelum laga final kejuaraan:\n'Pour remporter ce match décisif, il est primordial que nous ( ... ) la victoire avec plus de détermination que nos adversaires.'\nBentuk konjugasi Subjonctif Présent dari kata kerja 'vouloir' untuk subjek 'nous' adalah...",
        "correct": "voulions (akar persona nous/vous voul- + akhiran Subjonctif persona pertama jamak -ions).",
        "distractors": [
            "veuillions (kesalahan mempertahankan akar persona tunggal veuill- pada persona jamak nous).",
            "voulons (bentuk Présent de l'indicatif yang salah modus karena klausa il est primordial que menuntut subjonctif).",
            "voudrions (bentuk Conditionnel Présent yang tidak sesuai fungsi klausa subordinatif kehendak).",
            "voulaient (bentuk Imparfait indikatif orang ketiga jamak)."
        ],
        "formula": {
            "title": "LE SUBJONCTIF DU VERBE VOULOIR",
            "latex": "\\text{que je veuille, que tu veuilles, qu'il veuille, } \\mathbf{que \\text{ } nous \\text{ } voulions}, \\text{ que vous vouliez, qu'ils veuillent}",
            "legend": "• Seperti halnya aller, verba vouloir memiliki dua akar: 'veuill-' (tunggal & ils) dan 'voul-' (nous & vous).<br>• nous $\\rightarrow$ 'que nous voulions'."
        },
        "hints": {
            "concept": "Kata kerja 'vouloir' di Subjonctif mengalami pemisahan akar: 'veuill-' untuk tunggal dan orang ketiga jamak (que je veuille, qu'ils veuillent), tetapi kembali ke akar 'voul-' untuk nous dan vous (que nous voulions, que vous vouliez).",
            "execution": "nous + Subjonctif dari vouloir = 'voulions'."
        }
    },
    {
        "id": "fra-lat-h-25",
        "materi": "GRAMMAIRE AVANCÉE: LA PROPOSITION PARTICIPE ABSOLUE",
        "topic": "Klausa Partisipial Independen Lampau (Participe Passé Composé) Tanpa Konjungsi",
        "stem": "Dalam catatan perjalanan ekspedisi ilmiah di samudra:\n'( ... ) toutes les vérifications techniques sur les instruments de mesure, l'équipe océanographique a levé l'ancre au crépuscule.'\nBentuk klausa partisipial majemuk yang TEPAT untuk menyatakan tindakan yang telah diselesaikan secara tuntas sebelum keberangkatan kapal adalah...",
        "correct": "Ayant terminé (forme composée du participe: ayant + Participe Passé terminé untuk menyatakan aksi tuntas sebelum verba utama).",
        "distractors": [
            "En terminant (Gérondif yang keliru menyatakan aksi sedang berjalan simultan bersamaan dengan pengangkatan jangkar).",
            "Terminé (Participe Passé tunggal yang tidak memiliki subjek aktif untuk menjalankan aksi verifikasi).",
            "Terminant (Participe Présent tunggal yang mengabaikan aspek ketuntasan mendahului).",
            "Pour terminer (konstruksi infinitif tujuan yang mengubah makna urutan waktu menjadi tujuan masa depan)."
        ],
        "formula": {
            "title": "LE PARTICIPE PASSÉ COMPOSÉ (FORME COMPOSÉE)",
            "latex": "\\mathbf{Ayant \\text{ } terminé} \\dots \\iff \\text{Après avoir terminé toutes les vérifications, l'équipe...}",
            "legend": "• Menyatakan aksi lampau yang telah selesai sempurna sebelum aksi pada kalimat utama berlangsung.<br>• Memadatkan gaya penulisan sastrawi dan akademis tingkat tinggi."
        },
        "hints": {
            "concept": "Le Participe Passé Composé (Ayant terminé / Étant parti) digunakan dalam laras bahasa formal untuk memadatkan klausa subordinatif temporal yang bermakna 'setelah menyelesaikan...' (après avoir terminé...).",
            "execution": "Setelah selesai memeriksa = 'Ayant terminé'."
        }
    }
]
