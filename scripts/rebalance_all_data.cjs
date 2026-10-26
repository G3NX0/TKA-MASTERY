/**
 * TKA MASTERY HUB - MASTER BATCH REBALANCER & SANITIZER
 * Eliminates predictable key patterns, strips synthetic AI filler padding,
 * and balances option keys evenly (~20% A-E) across all 25 subjects.
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DATA_DIR = path.join(__dirname, '..', 'data');

// Known synthetic distractor filler phrases across all subjects
const FILLERS = [
  /demi mencegah terjadinya risiko kepailitan finansial dan kerugian modal kerja jangka panjang/gi,
  /ditinjau dari sistem kekerabatan tradisional dan struktur organisasi sosial masyarakat adat/gi,
  /ditinjau dari timbangan morfologi shorof wazan tsulatsi dan faedah semantiknya/gi,
  /ditinjau dari register kesantunan bahasa keigo serta kaidah konjugasi verba/gi,
  /ditinjau dari kronologi peristiwa sejarah nasional dan dinamika geopolitik kawasan/gi,
  /ditinjau dari register kesantunan komunikasi sosial dan kaidah nada pinyin/gi,
  /sesuai dengan prinsip efisiensi alokasi sumber daya langka dan teori utilitas konsumen/gi,
  /sesuai dengan spesifikasi protokol komunikasi standar dan arsitektur sistem operasi/gi,
  /ditinjau dari dinamika diferensiasi sosial horizontal dan polarisasi stratifikasi kelas/gi,
  /sesuai dengan dinamika sirkulasi atmosferik global dan klasifikasi zona agroklimat wilayah/gi,
  /diturunkan dari analisis evolusi ragawi manusia dan dinamika linguistik antropologis/gi,
  /sesuai dengan jalur metabolisme enzimatik terkoordinasi dan hukum konservasi energi biokimia/gi,
  /,?\s*as explicitly outlined through critical reading analysis and syntactic discourse structure/gi,
  /,?\s*derived from deductive paragraph reasoning and standard grammatical concord in academic English/gi,
  /,?\s*verified through textual evidence synthesis and objective macro-linguistic comprehension/gi,
  /sesuai dengan ketentuan standar mutu industri kontemporer dan perlindungan kepentingan hak/gi,
  /demi mencegah terjadinya degradasi throughput pada link jaringan backbone utama/gi,
  /sesuai dengan ketentuan best practice arsitektur jaringan komputer enterprise modern/gi,
  /diturunkan dari analisis struktur kalimat bertingkat pola klausula subordinatif/gi,
  /ditinjau dari register kesantunan berbahasa serta kaidah deklinasi artikel/gi,
  /menurut prinsip pencatatan persamaan dasar akuntansi dan pengakuan pendapatan beban berbasis/gi,
  /sesuai dengan konteks semantik paragraf deduktif-induktif dan piramida informasi wacana/gi,
  /menurut prinsip keterbacaan teks ekspositori analitis dan pedoman umum ejaan bahasa Indonesia/gi,
  /sesuai dengan ketentuan best practice prinsip tata rupa Nirmana dan psikologi persepsi visual/gi,
  /sesuai dengan kaidah interpretasi makna simbolik tebal \(thick description\) dan kajian emik/gi,
  /diturunkan dari analisis struktur kalimat bertingkat pola Nebensatz subordinatif/gi,
  /demi mencegah terjadinya degradasi kualitas estetika pada media reproduksi cetak maupun digital/gi,
  /diturunkan dari analisis struktur sosio-historis dan kontinuitas perubahan peradaban bangsa/gi,
  /diturunkan dari analisis struktur klausa kalimat bertingkat tata bahasa Mandarin/gi,
  /ditinjau dari instrumen transmisi kebijakan moneter bank sentral dan stimulus fiskal negara/gi,
  /sesuai dengan konfigurasi orbital molekul terdelokalisasi dan hibridisasi valensi atom pusat/gi,
  /diturunkan dari relasi energi bebas Gibbs dan potensial elektroda standar reduksi Nernst/gi,
  /ditinjau dari relasi energi bebas Gibbs dan potensial elektroda standar reduksi Nernst/gi,
  /ditinjau dari persamaan diferensial gerak harmonik sederhana dan osilasi teredam/gi,
  /menurut interpretasi fisis persamaan Maxwell dan teori gelombang elektromagnetik/gi,
  /menurut prinsip keamanan kriptografis dan mekanisme mitigasi kerentanan siber terpadu/gi,
  /한국어 통사 구조상 인과 접속 표지 및 피동·사동 파생 규칙을 위배합니다/gi,
  /문장 성분 간의 호응 관계 및 필수적 논항 요구 조건을 충족하지 못합니다/gi,
  /d'après les normes de communication pragmatique socioculturelle française/gi,
  /conformément au contexte sémantique de l'Académie française et du texte/gi,
  /menurut norma komunikasi situasional dan etika pragmatik budaya Tionghoa/gi,
  /sesuai konteks semantik wacana dokkai dan kaidah ortografi kanji baku/gi,
  /diturunkan dari analisis filologis leksikografi bahasa Arab standar modern/gi,
  /menurut konteks sintaksis wacana peradaban Islam dan literasi teks qira'ah fusha/gi,
  /ditinjau dari teori endosimbiosis serial serta adaptasi morfofisiologi seleksi alam populasi/gi,
  /diturunkan dari analisis segregasi alel independen hukum Mendel dan genetika molekuler/gi,
  /sesuai dengan kaidah interpretasi eksplanasi kausalitas historis dan analisis sinkronik-diakronik/gi,
  /sesuai dengan fungsi manifes dan fungsi laten institusi sosial dalam menjaga integrasi/gi
];

function sanitizeOptionText(t) {
  if (typeof t !== 'string') return t;
  let s = t;
  // Deduplicate adjacent repeating phrases >= 20 chars
  s = s.replace(/(.{20,}?)\s*\1+/g, '$1');
  // Strip known artificial filler phrases
  for (const f of FILLERS) {
    s = s.replace(f, '');
  }
  // Remove dangling trailing connectors or punctuation
  s = s.replace(/,\s*(?:sesuai dengan|ditinjau dari|menurut prinsip|demi mencegah|diturunkan dari|berdasarkan kaidah)\.?$/i, '');
  s = s.replace(/\s+/g, ' ').replace(/\s+\./g, '.').trim();
  return s;
}

// PRNG for deterministic reproducible shuffling
function createRng(seedStr) {
  let h = 0x811c9dc5;
  for (let i = 0; i < seedStr.length; i++) {
    h ^= seedStr.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return function() {
    h = Math.imul(h ^ (h >>> 16), 2246822507);
    h = Math.imul(h ^ (h >>> 13), 3266489909);
    h ^= h >>> 16;
    return (h >>> 0) / 4294967296;
  };
}

function shuffleWithRng(arr, rng) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

function syncExplanation(exp, oldKey, newKey) {
  if (!exp || typeof exp !== 'string') return exp;
  if (!oldKey || oldKey === newKey) return exp;

  let res = exp;
  // Replace standard patterns: "Kunci Jawaban: (A)" -> "Kunci Jawaban: (B)"
  res = res.replace(/(Kunci\s+Jawaban:\s*\(?)[A-E](\)?)/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(Jawaban\s*(?:yang\s+benar)?:\s*\(?)[A-E](\)?)/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(Correct\s+Answer:\s*<\/strong>\s*\(?)[A-E](\)?)/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(Correct\s+Answer:\s*\(?)[A-E](\)?)/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(option\s*\()[A-E](\))/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(opsi\s*\()[A-E](\))/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(pilihan\s*\()[A-E](\))/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(opsi\s+)[A-E](\s+adalah|\s+benar|\s+tepat)/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(pilihan\s+)[A-E](\s+adalah|\s+benar|\s+tepat)/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);
  res = res.replace(/(jawaban\s+yang\s+(?:paling\s+)?(?:benar|tepat)\s+adalah\s+(?:\(?))[A-E](\)?)/gi, (m, p1, p2) => `${p1}${newKey}${p2}`);

  return res;
}

function processSubjectFile(filename) {
  const fpath = path.join(DATA_DIR, filename);
  const rawContent = fs.readFileSync(fpath, 'utf8');

  // Find window variable name
  const varMatch = rawContent.match(/(window\.[A-Za-z0-9_]+)\s*=\s*/);
  if (!varMatch) {
    console.error(`Skipping ${filename}: no window variable found.`);
    return;
  }
  const fullVarName = varMatch[1];
  const shortVarName = fullVarName.replace('window.', '');

  const sandbox = { window: {} };
  vm.runInNewContext(rawContent, sandbox);
  const questions = sandbox.window[shortVarName];
  if (!Array.isArray(questions)) {
    console.error(`Skipping ${filename}: questions is not an array.`);
    return;
  }

  const rng = createRng(filename + '_tka_v12');

  // Group standard MCQs by pack
  const packs = {};
  questions.forEach((q, idx) => {
    if (q.type === 'mcq' && Array.isArray(q.options) && q.options.length >= 4) {
      const mode = q.mode || 'latihan';
      const diff = q.difficulty || 'medium';
      const packKey = `${mode}_${diff}`;
      if (!packs[packKey]) packs[packKey] = [];
      packs[packKey].push(idx);
    }
  });

  const LETTERS = ['A', 'B', 'C', 'D', 'E'];

  Object.entries(packs).forEach(([packKey, qIndices]) => {
    const N = qIndices.length;
    // Generate balanced target keys
    const targetKeys = [];
    for (let i = 0; i < N; i++) {
      targetKeys.push(LETTERS[i % 5]);
    }
    shuffleWithRng(targetKeys, rng);

    qIndices.forEach((qIdx, i) => {
      const q = questions[qIdx];
      const targetKey = targetKeys[i];
      const oldKey = q.correctKey || q.correctAnswer;

      // 1. Sanitize distractor filler texts in options
      q.options.forEach(opt => {
        if (typeof opt.text === 'string') {
          opt.text = sanitizeOptionText(opt.text);
        }
      });

      // 2. Identify correct option and distractors
      const correctOpt = q.options.find(o => o.key === oldKey);
      if (!correctOpt) {
        // If old key not found, skip re-keying
        return;
      }
      const distractors = q.options.filter(o => o !== correctOpt);

      // Shuffle distractors
      shuffleWithRng(distractors, rng);

      // Place correctOpt at target index
      const targetIdx = LETTERS.indexOf(targetKey);
      const newOptions = [
        ...distractors.slice(0, targetIdx),
        correctOpt,
        ...distractors.slice(targetIdx)
      ];

      // Re-assign keys A, B, C, D, E
      newOptions.forEach((opt, idx) => {
        opt.key = LETTERS[idx] || String.fromCharCode(65 + idx);
      });

      q.options = newOptions;
      q.correctKey = targetKey;
      if (q.correctAnswer && typeof q.correctAnswer === 'string') {
        q.correctAnswer = targetKey;
      }

      // 3. Sync explanation
      q.explanation = syncExplanation(q.explanation, oldKey, targetKey);
    });
  });

  // Re-serialize back to file with proper window assignment
  const serialized = `/**\n * TKA MASTERY HUB - AUTENTIK & BALANCED DATASET\n * Subject: ${shortVarName}\n * Keys rebalanced ~20% A-E, AI distractor padding sanitized.\n */\n\n${fullVarName} = ${JSON.stringify(questions, null, 2)};\n`;

  fs.writeFileSync(fpath, serialized, 'utf8');

  // Verify key distribution
  const finalKeyCounts = {};
  const finalRanks = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };
  const mcqs = questions.filter(q => q.type === 'mcq' && Array.isArray(q.options));

  mcqs.forEach(q => {
    finalKeyCounts[q.correctKey] = (finalKeyCounts[q.correctKey] || 0) + 1;
    const sorted = [...q.options].sort((a,b) => (b.text||'').length - (a.text||'').length);
    const r = sorted.findIndex(o => o.key === q.correctKey) + 1;
    if (r >= 1 && r <= 5) finalRanks[r]++;
  });

  console.log(`${filename.padEnd(30)} | MCQs: ${String(mcqs.length).padStart(3)} | Keys: ${JSON.stringify(finalKeyCounts)} | Ranks: ${JSON.stringify(finalRanks)}`);
}

function runAll() {
  const files = fs.readdirSync(DATA_DIR).filter(f => f.startsWith('questions_') && f !== 'questions_db.js');
  console.log(`Processing ${files.length} question files...`);
  files.forEach(f => {
    processSubjectFile(f);
  });
  console.log('Batch rebalancing completed successfully.');
}

runAll();
