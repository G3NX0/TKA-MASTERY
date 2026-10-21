const fs = require('fs');
const vm = require('vm');

const appCode = fs.readFileSync('app.js', 'utf8');
const rplCode = fs.readFileSync('data/questions_rpl.js', 'utf8');

const sandbox = {
  window: {},
  document: {
    getElementById: () => null,
    querySelectorAll: () => []
  },
  navigator: {}
};
vm.createContext(sandbox);

vm.runInContext(rplCode, sandbox);
const questions = sandbox.window.TKA_RPL_QUESTIONS;

console.log('Total RPL questions loaded:', questions.length);

const setupScript = appCode.slice(appCode.indexOf('function escapeHtml'), appCode.indexOf('function renderQuestion'));
vm.runInContext(setupScript, sandbox);

let withCodeCount = 0;
let errors = 0;

questions.forEach((q, idx) => {
  try {
    const raw = q.questionHtml || q.question;
    const formatted = sandbox.formatContentWithCode(raw);
    if (raw && raw.includes('```')) {
      withCodeCount++;
      if (!formatted.includes('code-snippet-box')) {
        console.error('Question ' + q.id + ' has code block but missing code-snippet-box!');
        errors++;
      }
      if (formatted.includes('___CODE_BLOCK_TOKEN_')) {
        console.error('Question ' + q.id + ' contains unresolved placeholder!');
        errors++;
      }
      if (/<p>\s*<div class="code-snippet-box"/.test(formatted)) {
        console.error('Question ' + q.id + ' has code box directly inside <p>!');
        errors++;
      }
    }
  } catch (err) {
    console.error('Error on question ' + q.id + ':', err);
    errors++;
  }
});

console.log('--- AUDIT SUMMARY ---');
console.log('Total RPL questions with code blocks verified:', withCodeCount);
console.log('Errors detected:', errors);
if (errors === 0) {
  console.log('SUCCESS: All PPLG / RPL code snippets formatted and verified with 100% accuracy!');
} else {
  process.exit(1);
}
