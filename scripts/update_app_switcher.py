"""
Update app.js untuk menambahkan switcher grup Mapel Wajib vs Mapel Lanjutan
dan aktivasi interaksi kartu elektif yang sudah tersedia 135 soal.
"""
import re

with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Tambahkan activeDeckGroup di state
old_state = "currentSubject: 'mtk',       // 'mtk' | 'ind' | 'eng' | 'diag'"
new_state = "currentSubject: 'mtk',       // 'mtk' | 'ind' | 'eng' | 'mtk_lanjut' | 'ind_lanjut' | 'eng_lanjut' | 'diag'\n    activeDeckGroup: 'wajib',    // 'wajib' | 'lanjut'"

code = code.replace(old_state, new_state)

# 2. Update renderHomeDeck agar menerima group ('wajib' vs 'lanjut')
old_render_deck = """  function renderHomeDeck() {
    if (!els.cardsDeckContainer || !window.TKA_DATABASE) return;

    els.cardsDeckContainer.innerHTML = '';

    // USER REQUIREMENT:
    // Left: Bahasa Indonesia (inward curve)
    // Center: Matematika (proud center)
    // Right: Bahasa Inggris (inward curve)
    const panoramaDeck = [
      { key: 'ind', panoramaClass: 'panorama-left' },
      { key: 'mtk', panoramaClass: 'panorama-center' },
      { key: 'eng', panoramaClass: 'panorama-right' }
    ];"""

new_render_deck = """  function renderHomeDeck(group = state.activeDeckGroup) {
    if (!els.cardsDeckContainer || !window.TKA_DATABASE) return;

    els.cardsDeckContainer.innerHTML = '';
    state.activeDeckGroup = group;

    const panoramaDeck = group === 'lanjut' ? [
      { key: 'ind_lanjut', panoramaClass: 'panorama-left' },
      { key: 'mtk_lanjut', panoramaClass: 'panorama-center' },
      { key: 'eng_lanjut', panoramaClass: 'panorama-right' }
    ] : [
      { key: 'ind', panoramaClass: 'panorama-left' },
      { key: 'mtk', panoramaClass: 'panorama-center' },
      { key: 'eng', panoramaClass: 'panorama-right' }
    ];"""

code = code.replace(old_render_deck, new_render_deck)

# 3. Update initMobilePanorama agar mengenali tombol orbit dinamis
old_init_pano = """  function initMobilePanorama() {
    const navPills = document.querySelectorAll('.mobile-panorama-nav .btn-pano-pill');
    if (!els.cardsDeckContainer) return;

    const cards = els.cardsDeckContainer.querySelectorAll('.neo-deck-card');
    const subjectOrder = ['ind', 'mtk', 'eng'];"""

new_init_pano = """  function initMobilePanorama() {
    if (!els.cardsDeckContainer) return;

    const cards = els.cardsDeckContainer.querySelectorAll('.neo-deck-card');
    const isLanjut = state.activeDeckGroup === 'lanjut';
    const subjectOrder = isLanjut ? ['ind_lanjut', 'mtk_lanjut', 'eng_lanjut'] : ['ind', 'mtk', 'eng'];
    
    // Update orbit controller pills dynamically
    const navContainer = document.getElementById('mobilePanoramaNav');
    if (navContainer) {
      navContainer.innerHTML = isLanjut ? `
        <button class="btn-pano-pill" data-pano="ind_lanjut" title="Pindah ke B. Indonesia Lanjutan">
          <span class="pano-pill-badge ind">IND+</span>
          <span class="pano-pill-label">B. Indo Lanjut</span>
        </button>
        <button class="btn-pano-pill active" data-pano="mtk_lanjut" title="Pindah ke Matematika Lanjutan">
          <span class="pano-pill-badge mtk">MTK+</span>
          <span class="pano-pill-label">MTK Lanjut</span>
        </button>
        <button class="btn-pano-pill" data-pano="eng_lanjut" title="Pindah ke B. Inggris Lanjutan">
          <span class="pano-pill-badge eng">ENG+</span>
          <span class="pano-pill-label">B. Ing Lanjut</span>
        </button>
      ` : `
        <button class="btn-pano-pill" data-pano="ind" title="Pindah ke Bahasa Indonesia">
          <span class="pano-pill-badge ind">IND</span>
          <span class="pano-pill-label">B. Indonesia</span>
        </button>
        <button class="btn-pano-pill active" data-pano="mtk" title="Pindah ke Matematika">
          <span class="pano-pill-badge mtk">MTK</span>
          <span class="pano-pill-label">Matematika</span>
        </button>
        <button class="btn-pano-pill" data-pano="eng" title="Pindah ke Bahasa Inggris">
          <span class="pano-pill-badge eng">ENG</span>
          <span class="pano-pill-label">B. Inggris</span>
        </button>
      `;
    }
    const navPills = document.querySelectorAll('.mobile-panorama-nav .btn-pano-pill');"""

code = code.replace(old_init_pano, new_init_pano)

# 4. Tambahkan initial center dan switcher listener di initHomeViews
old_init_call = "renderHomeDeck();\n    initMobilePanorama();"
new_init_call = """renderHomeDeck('wajib');
    initMobilePanorama();

    // Listener Group Switcher (Mapel Wajib vs Mapel Lanjutan)
    const switcher = document.getElementById('deckGroupSwitcher');
    if (switcher) {
      switcher.querySelectorAll('.btn-group-tab').forEach(tab => {
        tab.addEventListener('click', () => {
          switcher.querySelectorAll('.btn-group-tab').forEach(t => t.classList.remove('active'));
          tab.classList.add('active');
          const group = tab.dataset.deck;
          renderHomeDeck(group);
          initMobilePanorama();
        });
      });
    }"""

code = code.replace(old_init_call, new_init_call)

# 5. Pasang navigasi klik pada kartu elektif yang aktif
old_elective_card = """        <div class="elective-card-bottom">
          <span class="elective-status-pill">${item.available}</span>
          <span class="elective-id-tag">#${item.id}</span>
        </div>"""

new_elective_card = """        <div class="elective-card-bottom">
          <span class="elective-status-pill ${item.targetSubjectKey ? 'ready' : ''}">${item.available}</span>
          ${item.targetSubjectKey ? `<button class="btn-open-elective-hub" data-target="${item.targetSubjectKey}">Buka Modul 135 Soal &rarr;</button>` : `<span class="elective-id-tag">#${item.id}</span>`}
        </div>"""

code = code.replace(old_elective_card, new_elective_card)

# Tambahkan listener buka elective hub
old_elective_loop_end = "els.electiveGridContainer.appendChild(card);\n    });\n  }"
new_elective_loop_end = """els.electiveGridContainer.appendChild(card);
    });

    els.electiveGridContainer.querySelectorAll('.btn-open-elective-hub').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const targetSubj = btn.dataset.target;
        if (targetSubj) navigateTo('subject', targetSubj);
      });
    });
  }"""

code = code.replace(old_elective_loop_end, new_elective_loop_end)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("app.js updated successfully with deck switcher and elective launcher.")
