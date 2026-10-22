/**
 * TKA MASTERY HUB - Foreign Language Leakage Sanitizer
 * Strips all embedded translations from options and question stems across 6 foreign languages:
 * Bahasa Arab, Jerman, Prancis, Korea, Jepang, and Mandarin.
 * Preserves translations on opt.translation for interlinear display when translation mode is ON.
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const files = [
  { lang: 'arab', file: 'questions_bahasa_arab.js', varName: 'TKA_BAHASA_ARAB_QUESTIONS' },
  { lang: 'jerman', file: 'questions_bahasa_jerman.js', varName: 'TKA_BAHASA_JERMAN_QUESTIONS' },
  { lang: 'prancis', file: 'questions_bahasa_prancis.js', varName: 'TKA_BAHASA_PRANCIS_QUESTIONS' },
  { lang: 'korea', file: 'questions_bahasa_korea.js', varName: 'TKA_BAHASA_KOREA_QUESTIONS' },
  { lang: 'jepang', file: 'questions_bahasa_jepang.js', varName: 'TKA_BAHASA_JEPANG_QUESTIONS' },
  { lang: 'mandarin', file: 'questions_bahasa_mandarin.js', varName: 'TKA_BAHASA_MANDARIN_QUESTIONS' }
];

const wordReplacements = [
  // French
  { pattern: /'beurre'\s*\(mentega\)/g, replacement: "'beurre'" },
  { pattern: /'craindre'\s*\(khawatir akan\)/g, replacement: "'craindre'" },
  // German
  { pattern: /'aufstehen'\s*\(bangun tidur\)/g, replacement: "'aufstehen'" },
  { pattern: /'verpassen'\s*\(ketinggalan kereta\)/g, replacement: "'verpassen'" },
  { pattern: /'der Zeuge'\s*\(saksi\)/g, replacement: "'der Zeuge'" },
  // Japanese
  { pattern: /'たかい'\s*\(mahal\)/g, replacement: "'たかい'" },
  { pattern: /'たべます'\s*\(makan\)/g, replacement: "'たべます'" },
  { pattern: /'かきます'\s*\(menulis \/ Kakimasu\)/g, replacement: "'かきます'" },
  { pattern: /'行きました'\s*\(pergi\)/g, replacement: "'行きました'" },
  { pattern: /'ひきます'\s*\(memetik\/memainkan alat musik dawai\)/g, replacement: "'ひきます'" },
  // Arabic
  { pattern: /'وَقَى'\s*\(memelihara\/menjaga\)/g, replacement: "'وَقَى'" },
  { pattern: /'كَرِيمٌ'\s*\(dermawan\)/g, replacement: "'كَرِيمٌ'" },
  { pattern: /'شُجَاعٌ'\s*\(pemberani\)/g, replacement: "'شُجَاعٌ'" },
  { pattern: /'طَاهِرٌ'\s*\(suci\)/g, replacement: "'طَاهِرٌ'" },
  // Mandarin
  { pattern: /'一'\s*\(satu\)/g, replacement: "'一'" },
  { pattern: /'打'\s*\(bermain\/memukul\)/g, replacement: "'打'" },
  { pattern: /'很好'\s*\(sangat bagus\)/g, replacement: "'很好'" },
  // Korean
  { pattern: /'가다'\s*\(pergi\)/g, replacement: "'가다'" },
  { pattern: /'먹다'\s*\(makan\)/g, replacement: "'먹다'" },
  { pattern: /'책'\s*\(buku,\s*ber-batchim\s*ㄱ\)/g, replacement: "'책' (ber-batchim ㄱ)" },
  { pattern: /'음악'\s*\(musik,\s*ber-batchim\s*ㄱ\)/g, replacement: "'음악' (ber-batchim ㄱ)" },
  { pattern: /'밥'\s*\(nasi,\s*ber-batchim\s*ㅂ\)/g, replacement: "'밥' (ber-batchim ㅂ)" },
  { pattern: /'김치'\s*\(kimchi,\s*berakhiran\s*vokal\s*ㅣ\)/g, replacement: "'김치' (berakhiran vokal ㅣ)" },
  { pattern: /'만나다'\s*\(bertemu\)/g, replacement: "'만나다'" },
  { pattern: /'보고 싶다'\s*\(ingin menonton\)/g, replacement: "'보고 싶다'" },
  { pattern: /'먹다'\s*\(makan,\s*ber-batchim\s*ㄱ\)/g, replacement: "'먹다' (ber-batchim ㄱ)" },
  { pattern: /'오른쪽'\s*\(arah kanan,\s*ber-batchim\s*ㄱ\)/g, replacement: "'오른쪽' (ber-batchim ㄱ)" },
  { pattern: /'지하 2층'\s*\(lantai bawah tanah 2,\s*ber-batchim\s*ㅇ\)/g, replacement: "'지하 2층' (ber-batchim ㅇ)" },
  { pattern: /'이야기하다'\s*\(berbicara\)/g, replacement: "'이야기하다'" },
  { pattern: /'포장하다'\s*\(membungkus\)/g, replacement: "'포장하다'" },
  { pattern: /'많다'\s*\(banyak,\s*ber-batchim 많 dengan vokal ㅏ\)/g, replacement: "'많다' (ber-batchim 많 dengan vokal ㅏ)" },
  { pattern: /'일어나다'\s*\(bangun\)/g, replacement: "'일어나다'" },
  { pattern: /'오다'\s*\(datang\/turun hujan\)/g, replacement: "'오다'" },
  { pattern: /'오다'\s*\(datang\)/g, replacement: "'오다'" },
  { pattern: /'오다'\s*\(turun hujan\)/g, replacement: "'오da'" },
  { pattern: /'듣다'\s*\(mendengarkan,\s*ber-batchim\s*ㄷ\s*tak beraturan\)/g, replacement: "'듣다' (ber-batchim ㄷ tak beraturan)" },
  { pattern: /'전공하다'\s*\(mengambil jurusan\)/g, replacement: "'전공하다'" },
  { pattern: /'하다'\s*\(setelah makan\)/g, replacement: "'하다'" },
  { pattern: /'먹다'\s*\(sebelum minum obat\)/g, replacement: "'먹다'" },
  { pattern: /'입실하다'\s*\(masuk ruang\)/g, replacement: "'입실하다'" },
  { pattern: /'춥다'\s*\(dingin\)/g, replacement: "'춥다'" },
  { pattern: /'만들다'\s*\(membuat,\s*batchim\s*ㄹ\)/g, replacement: "'만들다' (batchim ㄹ)" },
  { pattern: /'낫다'\s*\(sembuh,\s*batchim\s*ㅅ\)/g, replacement: "'낫다' (batchim ㅅ)" },
  { pattern: /'마시다'\s*\(minum\)/g, replacement: "'마시다'" },
  { pattern: /'공부하다'\s*\(belajar\)/g, replacement: "'공부하다'" },
  { pattern: /'비싸다'\s*\(mahal\)/g, replacement: "'비싸다'" },
  { pattern: /'앉다'\s*\(duduk\)/g, replacement: "'앉다'" },
  { pattern: /'붙다'\s*\(menempel\)/g, replacement: "'붙다'" },
  { pattern: /'챙기다'\s*\(menyiapkan\/membawa\)/g, replacement: "'챙기다'" },
  { pattern: /'멈추다'\s*\(berhenti\)/g, replacement: "'멈추다'" },
  { pattern: /'취소하다'\s*\(membatalkan\)/g, replacement: "'취소하다'" },
  { pattern: /'닫다'\s*\(menutup,\s*ber-batchim\s*ㄷ\)/g, replacement: "'닫다' (ber-batchim ㄷ)" },
  { pattern: /'연습하다'\s*\(berlatih\)/g, replacement: "'연습하다'" },
  { pattern: /'잃다'\s*\(hilang\/kehilangan\)/g, replacement: "'잃다'" },
  { pattern: /'읽다'\s*\(membaca\)/g, replacement: "'읽다'" },
  { pattern: /'취소되다'\s*\(dibatalkan\)/g, replacement: "'취소되다'" },
  { pattern: /'복잡하다'\s*\(rumit\)/g, replacement: "'복잡하다'" },
  { pattern: /'생각하다'\s*\(berpikir\)/g, replacement: "'생각하다'" },
  { pattern: /'지정되다'\s*\(ditetapkan\)/g, replacement: "'지정되다'" },
  { pattern: /'쓰러지다'\s*\(pingsan\/jatuh roboh\)/g, replacement: "'쓰러지다'" },
  { pattern: /'갇혀 있다'\s*\(terjebak terkurung\)/g, replacement: "'갇혀 있다'" },
  { pattern: /'높다'\s*\(tinggi\)/g, replacement: "'높다'" },
  { pattern: /'알다'\s*\(tahu\/mengetahui,\s*ber-batchim\s*ㄹ\)/g, replacement: "'알다' (ber-batchim ㄹ)" },
  { pattern: /'접속하다'\s*\(mengakses\/login\)/g, replacement: "'접속하다'" },
  { pattern: /'무너지다'\s*\(runtuh\/roboh\)/g, replacement: "'무너지다'" },
  { pattern: /'쉬다'\s*\(beristirahat\)/g, replacement: "'쉬다'" },
  { pattern: /'듣다'\s*\(mendengar\)/g, replacement: "'듣다'" },
  { pattern: /'보다'\s*\(menonton\)/g, replacement: "'보다'" },
  { pattern: /'않다'\s*\(tidak mengenakan\)/g, replacement: "'않다'" },
  { pattern: /'목격하다'\s*\(menyaksikan\)/g, replacement: "'목격하다'" },
  { pattern: /'배우다'\s*\(mempelajari\)/g, replacement: "'배우다'" },
  { pattern: /'횡령하다'\s*\(menggelapkan dana\)/g, replacement: "'횡령하다'" },
  { pattern: /'늦다'\s*\(terlambat\)/g, replacement: "'늦다'" },
  { pattern: /'속다'\s*\(tertipu\)/g, replacement: "'속다'" }
];

function sanitizeQuestionHtml(html, lang) {
  if (!html) return html;
  let res = html;

  // 1. Remove whole-line Indonesian translation sentences in parentheses
  const lines = res.split('\n');
  const filteredLines = lines.filter(line => {
    const trimmed = line.trim();
    if (trimmed.startsWith('(') && (trimmed.endsWith(')') || trimmed.endsWith(').'))) {
      const inside = trimmed.slice(1, trimmed.endsWith(').') ? -2 : -1).trim();
      if (/^[A-ZÀ-ÿ]/.test(inside) && inside.split(/\s+/).length >= 3 && !inside.startsWith('Pilihlah') && !inside.startsWith('Catatan')) {
        return false;
      }
    }
    return true;
  });
  res = filteredLines.join('\n');

  // 2. Remove inline word translations
  wordReplacements.forEach(({ pattern, replacement }) => {
    res = res.replace(pattern, replacement);
  });

  return res;
}

function splitOption(text, lang) {
  const t = text.trim();
  if (!t.includes('(')) return null;

  const indoStarters = [
    'Karakter', 'Kalimat', 'Kedua', 'Pernyataan', 'Penggunaan', 'Bentuk rancangan', 'Konsep',
    'Makna', 'Perannya', 'Penerapan', 'Penataan', 'Ketika', 'Pronomina', 'Kelulusan',
    'Ibu kota', 'Botol', 'Faktor', 'Dalam tradisi', 'Membersihkan', 'Melakukan ritual',
    'Kabuki', 'Jejaring', 'Kamar', 'Menyerahkan', 'Wajib diletakkan', 'Melakukan tindakan',
    'Karena helaian', 'Kelicikan', 'Kekuatan', 'Kesetiaan', 'Wajib memasukkan', 'Kereta G102',
    'Keterikatan batin', 'Tepat berada', 'Isim mutsanna', 'Jama\' mudzakkar', 'Fi\'il Salim',
    'Fi\'il Mahmuz', 'Fi\'il Mudha\'af', 'Shifat Musyabbahah', 'Tidak ada pertentangan',
    'Membuang sisa', 'Keterlibatan aktif', 'Huruf vokal', 'Karena bunga'
  ];

  if (indoStarters.some(s => t.startsWith(s))) return null;
  const m = t.match(/^([^\(]+?)\s*\((.+)\)(.*)$/);
  if (!m) return null;

  const foreign = m[1].trim();
  const inside = m[2].trim();
  const trailing = m[3] ? m[3].trim() : '';

  if (foreign.split(/\s+/).length > 10) return null;

  let fullExplanation = inside;
  if (trailing) {
    if (trailing === '.') {
      fullExplanation += '.';
    } else {
      fullExplanation += ' ' + trailing;
    }
  }

  return { foreign, explanation: fullExplanation };
}

let grandTotalOptions = 0;
let grandTotalQCleaned = 0;

files.forEach(f => {
  const fullPath = path.join(__dirname, '..', 'data', f.file);
  const rawCode = fs.readFileSync(fullPath, 'utf8');

  const ctx = { window: {} };
  vm.createContext(ctx);
  vm.runInContext(rawCode, ctx);
  const questions = ctx.window[f.varName];

  if (!Array.isArray(questions)) {
    throw new Error(`Failed to load ${f.varName} from ${f.file}`);
  }

  let optCount = 0;
  let qCount = 0;

  questions.forEach(q => {
    // Sanitize questionHtml
    const originalHtml = q.questionHtml;
    const cleanHtml = sanitizeQuestionHtml(originalHtml, f.lang);
    if (originalHtml !== cleanHtml) {
      q.questionHtml = cleanHtml;
      qCount++;
    }

    // Sanitize options
    (q.options || []).forEach(opt => {
      const split = splitOption(opt.text, f.lang);
      if (split) {
        opt.text = split.foreign;
        opt.translation = split.explanation;
        optCount++;
      }
    });
  });

  grandTotalOptions += optCount;
  grandTotalQCleaned += qCount;

  // Write back to file cleanly
  const outputCode = `// TKA MASTERY HUB - ${f.lang.toUpperCase()} QUESTIONS DATABASE
// Automatically sanitized: pure foreign questions and options, translation available via toggle
window.${f.varName} = ${JSON.stringify(questions, null, 2)};
`;

  fs.writeFileSync(fullPath, outputCode, 'utf8');
  console.log(`[${f.lang.toUpperCase()}] Updated ${f.file}: ${qCount} questions sanitized, ${optCount} options split.`);
});

console.log(`\n========================================`);
console.log(`GRAND TOTAL: ${grandTotalQCleaned} questions sanitized, ${grandTotalOptions} options cleanly split.`);
console.log(`========================================\n`);
