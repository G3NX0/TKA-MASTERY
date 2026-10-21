/**
 * TKA MASTERY HUB: PRODUCTION APPLICATION ENGINE (V3.0)
 * Architecture: True Multi-Page Views, 3D Panorama Curved Cockpit,
 * Domain-Aware Scaffolding, Strict 3-Level Filtering, Anti-Spoiler Practice,
 * Integrated 15-Question Diagnostic Assessment & Prescriptive Roadmap.
 */

(function () {
  'use strict';

  // =========================================================================
  // APPLICATION STATE
  // =========================================================================
  const state = {
    currentView: 'home',         // 'home' | 'subject' | 'workspace' | 'results'
    currentSubject: 'mtk',       // 'mtk' | 'ind' | 'eng' | 'mtk_lanjut' | 'ind_lanjut' | 'eng_lanjut' | 'diag'
    activeDeckGroup: 'wajib',    // 'wajib' | 'lanjut'
    selectedDifficulty: 'easy',  // 'easy' | 'medium' | 'hard' (Strictly 3 levels)
    sessionMode: 'latihan',      // 'latihan' | 'simulasi' | 'diagnostik'
    
    exam: {
      questions: [],
      currentIndex: 0,
      answers: {},               // { [index]: selectedKey }
      flags: {},                 // { [index]: boolean }
      startTime: null,
      remainingSeconds: 30 * 60,
      timerInterval: null,
      isTimerPaused: false,
      strikes: 0,
      maxStrikes: 3,
      isFinished: false,
      isReviewMode: false
    },
    isModalOpen: false
  };

  // =========================================================================
  // DOM ELEMENT SELECTORS
  // =========================================================================
  const els = {
    // Views
    viewHome: document.getElementById('viewHome'),
    viewSubject: document.getElementById('viewSubject'),
    viewWorkspace: document.getElementById('viewWorkspace'),
    viewResults: document.getElementById('viewResults'),

    // Navbar
    mainNavbarWrapper: document.getElementById('mainNavbarWrapper'),
    pillNavbar: document.getElementById('pillNavbar'),
    liquidIndicator: document.getElementById('liquidIndicator'),
    navTabsRail: document.getElementById('navTabsRail'),
    navBtns: document.querySelectorAll('.nav-pill-btn'),
    btnNavLogo: document.getElementById('btnNavLogo'),
    navBtnDiag: document.getElementById('navBtnDiag'),

    // Home Deck, Diagnostic Hero Banner & 19 Elective Catalog
    cardsDeckContainer: document.getElementById('cardsDeckContainer'),
    btnLaunchDiagnosticBanner: document.getElementById('btnLaunchDiagnosticBanner'),
    btnStartDiagnosticCta: document.getElementById('btnStartDiagnosticCta'),
    homeTotalSoalStat: document.getElementById('homeTotalSoalStat'),
    btnToggleElectiveCatalog: document.getElementById('btnToggleElectiveCatalog'),
    electiveGridWrapper: document.getElementById('electiveGridWrapper'),
    electiveGridContainer: document.getElementById('electiveGridContainer'),
    electiveClusterTabs: document.getElementById('electiveClusterTabs'),
    toggleElectiveLabel: document.getElementById('toggleElectiveLabel'),

    // Dedicated Subject Page
    btnSubjectBackToHome: document.getElementById('btnSubjectBackToHome'),
    subjectHubTitle: document.getElementById('subjectHubTitle'),
    subjectHubDesc: document.getElementById('subjectHubDesc'),
    levelPills: document.querySelectorAll('.level-pill'),
    btnStartLatihan: document.getElementById('btnStartLatihan'),
    btnStartSimulasi: document.getElementById('btnStartSimulasi'),

    // Workspace Operational Bar
    btnQuitSession: document.getElementById('btnQuitSession'),
    infoSubjectName: document.getElementById('infoSubjectName'),
    infoModeBadge: document.getElementById('infoModeBadge'),
    hudStrikeBox: document.getElementById('hudStrikeBox'),
    strikeDots: document.querySelectorAll('.dot-strike'),
    hudTimerBox: document.getElementById('hudTimerBox'),
    hudTimerDigits: document.getElementById('hudTimerDigits'),
    btnToggleFullscreen: document.getElementById('btnToggleFullscreen'),
    btnOpenGridDrawer: document.getElementById('btnOpenGridDrawer'),
    gridDrawerIndicator: document.getElementById('gridDrawerIndicator'),

    // Question Paper
    paperQMateriBadge: document.getElementById('paperQMateriBadge'),
    paperQNum: document.getElementById('paperQNum'),
    paperQTopic: document.getElementById('paperQTopic'),
    paperQTypeBadge: document.getElementById('paperQTypeBadge'),
    paperQDiff: document.getElementById('paperQDiff'),
    paperQText: document.getElementById('paperQText'),
    paperOptionsList: document.getElementById('paperOptionsList'),

    // Bottom Scaffolding & Domain-Aware Elements (Apple HIG Inline Accordion)
    scaffoldingBottomPanel: document.getElementById('scaffoldingBottomPanel'),
    scaffoldItemFormula: document.getElementById('scaffoldItemFormula'),
    btnToggleFormulaHud: document.getElementById('btnToggleFormulaHud'),
    formulaHudBtnLabel: document.getElementById('formulaHudBtnLabel'),
    formulaHudHeader: document.getElementById('formulaHudHeader'),
    formulaStatusPill: document.getElementById('formulaStatusPill'),
    scaffoldItemClue1: document.getElementById('scaffoldItemClue1'),
    btnToggleClue1: document.getElementById('btnToggleClue1'),
    clue1StatusPill: document.getElementById('clue1StatusPill'),
    scaffoldItemClue2: document.getElementById('scaffoldItemClue2'),
    btnToggleClue2: document.getElementById('btnToggleClue2'),
    clue2StatusPill: document.getElementById('clue2StatusPill'),
    scaffoldItemSolution: document.getElementById('scaffoldItemSolution'),
    btnToggleSolution: document.getElementById('btnToggleSolution'),
    solutionStatusPill: document.getElementById('solutionStatusPill'),
    drawerFormulaHud: document.getElementById('drawerFormulaHud'),
    formulaHudContent: document.getElementById('formulaHudContent'),
    drawerClue1: document.getElementById('drawerClue1'),
    clue1Body: document.getElementById('clue1Body'),
    drawerClue2: document.getElementById('drawerClue2'),
    clue2Body: document.getElementById('clue2Body'),
    drawerSolution: document.getElementById('drawerSolution'),
    solutionBodyContent: document.getElementById('solutionBodyContent'),

    // Workspace Navigation Footer (Split Left / Right)
    btnPaperPrev: document.getElementById('btnPaperPrev'),
    btnPaperFlag: document.getElementById('btnPaperFlag'),
    btnPaperNext: document.getElementById('btnPaperNext'),
    btnPaperSubmit: document.getElementById('btnPaperSubmit'),
    btnReviewBackResults: document.getElementById('btnReviewBackResults'),

    // Desktop CBT Question Navigator Card (V5.0)
    cbtNavigatorCard: document.getElementById('cbtNavigatorCard'),
    cbtProgressBadge: document.getElementById('cbtProgressBadge'),
    cbtChipsGrid: document.getElementById('cbtChipsGrid'),
    cbtSidebarSubmitBox: document.getElementById('cbtSidebarSubmitBox'),
    btnCbtSidebarSubmit: document.getElementById('btnCbtSidebarSubmit'),

    // Question Grid Drawer (Mobile Responsive)
    gridDrawerOverlay: document.getElementById('gridDrawerOverlay'),
    gridDrawerSheet: document.getElementById('gridDrawerSheet'),
    btnCloseGridDrawer: document.getElementById('btnCloseGridDrawer'),
    gridNumbersContainer: document.getElementById('gridNumbersContainer'),
    btnGridDrawerSubmit: document.getElementById('btnGridDrawerSubmit'),

    // Proctor Modal
    proctorModal: document.getElementById('proctorModal'),
    proctorStrikeCount: document.getElementById('proctorStrikeCount'),
    proctorMessageText: document.getElementById('proctorMessageText'),
    btnProctorResume: document.getElementById('btnProctorResume'),

    // App In-App Confirm Modal & Pre-Submission Audit Sheet
    appConfirmModal: document.getElementById('appConfirmModal'),
    appConfirmTitle: document.getElementById('appConfirmTitle'),
    appConfirmMessage: document.getElementById('appConfirmMessage'),
    btnAppConfirmCancel: document.getElementById('btnAppConfirmCancel'),
    btnAppConfirmOk: document.getElementById('btnAppConfirmOk'),
    auditCountAnswered: document.getElementById('auditCountAnswered'),
    auditCountFlagged: document.getElementById('auditCountFlagged'),
    auditCountEmpty: document.getElementById('auditCountEmpty'),
    auditWarningBox: document.getElementById('auditWarningBox'),
    auditWarningText: document.getElementById('auditWarningText'),
    auditChipsGrid: document.getElementById('auditChipsGrid'),

    // Results View & Diagnostic Assessment
    reportScore: document.getElementById('reportScore'),
    reportTitle: document.getElementById('reportTitle'),
    reportSubtitle: document.getElementById('reportSubtitle'),
    reportCorrect: document.getElementById('reportCorrect'),
    reportWrong: document.getElementById('reportWrong'),
    reportTime: document.getElementById('reportTime'),
    reportPace: document.getElementById('reportPace'),
    diagnosticEvaluationBox: document.getElementById('diagnosticEvaluationBox'),
    diagMtkScore: document.getElementById('diagMtkScore'),
    diagMtkStatus: document.getElementById('diagMtkStatus'),
    diagMtkTopicList: document.getElementById('diagMtkTopicList'),
    diagIndScore: document.getElementById('diagIndScore'),
    diagIndStatus: document.getElementById('diagIndStatus'),
    diagIndTopicList: document.getElementById('diagIndTopicList'),
    diagEngScore: document.getElementById('diagEngScore'),
    diagEngStatus: document.getElementById('diagEngStatus'),
    diagEngTopicList: document.getElementById('diagEngTopicList'),
    diagPrescriptionText: document.getElementById('diagPrescriptionText'),
    btnReportReview: document.getElementById('btnReportReview'),
    btnReportReturn: document.getElementById('btnReportReturn'),
    priorityCardsList: document.getElementById('priorityCardsList')
  };

  // =========================================================================
  // LIQUID SPRING NAVBAR
  // =========================================================================
  function updateLiquidNavbarIndicator(targetBtn, withSquash = true) {
    if (!targetBtn || !els.liquidIndicator || !els.navTabsRail) return;

    const railRect = els.navTabsRail.getBoundingClientRect();
    const btnRect = targetBtn.getBoundingClientRect();

    const leftOffset = btnRect.left - railRect.left;
    const btnWidth = btnRect.width;

    if (withSquash) {
      els.liquidIndicator.style.transform = `translateX(${leftOffset}px) scaleX(1.14)`;
      setTimeout(() => {
        els.liquidIndicator.style.transform = `translateX(${leftOffset}px) scaleX(1.0)`;
      }, 180);
    } else {
      els.liquidIndicator.style.transform = `translateX(${leftOffset}px)`;
    }

    els.liquidIndicator.style.width = `${btnWidth}px`;

    els.navBtns.forEach(btn => btn.classList.remove('active'));
    targetBtn.classList.add('active');
  }

  function syncNavbarState(navKey) {
    const btn = document.querySelector(`.nav-pill-btn[data-nav="${navKey}"]`);
    if (btn) updateLiquidNavbarIndicator(btn, true);
  }

  function initNavbar() {
    els.navBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const navKey = btn.dataset.nav;
        if (navKey === 'home') {
          navigateTo('home');
        } else if (navKey === 'diag') {
          launchDiagnosticSession();
        } else {
          navigateTo('subject', navKey);
        }
      });
    });

    if (els.btnNavLogo) {
      els.btnNavLogo.addEventListener('click', () => {
        navigateTo('home');
      });
    }

    window.addEventListener('resize', () => {
      const activeBtn = document.querySelector('.nav-pill-btn.active');
      if (activeBtn) updateLiquidNavbarIndicator(activeBtn, false);
    });

    setTimeout(() => {
      const activeBtn = document.querySelector('.nav-pill-btn.active');
      if (activeBtn) updateLiquidNavbarIndicator(activeBtn, false);
    }, 150);
  }

  // =========================================================================
  // MULTI-PAGE VIEW ROUTER
  // =========================================================================
  function navigateTo(viewName, subjectKey = null) {
    state.currentView = viewName;
    if (subjectKey) state.currentSubject = subjectKey;

    // Reset view visibility
    [els.viewHome, els.viewSubject, els.viewWorkspace, els.viewResults].forEach(v => {
      if (v) v.classList.remove('active');
    });

    // Hide pill navbar when in workspace view to maximize focus
    if (viewName === 'workspace') {
      els.mainNavbarWrapper.classList.add('hidden-simulation');
    } else {
      els.mainNavbarWrapper.classList.remove('hidden-simulation');
    }

    const safeScrollTop = () => {
      try {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      } catch (e) {
        window.scrollTo(0, 0);
      }
    };

    if (viewName === 'home') {
      syncNavbarState('home');
      els.viewHome.classList.add('active');
      safeScrollTop();
    } 
    else if (viewName === 'subject') {
      syncNavbarState(state.currentSubject);
      renderSubjectHub(state.currentSubject);
      els.viewSubject.classList.add('active');
      safeScrollTop();
    }
    else if (viewName === 'workspace') {
      els.viewWorkspace.classList.add('active');
      syncFullscreenButtonState();
      safeScrollTop();
    }
    else if (viewName === 'results') {
      els.mainNavbarWrapper.classList.remove('hidden-simulation');
      els.viewResults.classList.add('active');
      safeScrollTop();
    }
  }

  // =========================================================================
  // VIEW 1: HOME 3D PANORAMA DECK RENDERER
  // =========================================================================
  function renderHomeDeck(group = state.activeDeckGroup) {
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
    ];

    panoramaDeck.forEach(item => {
      const key = item.key;
      const s = window.TKA_DATABASE[key];
      if (!s) return;

      const SUBJECT_LABELS = { mtk: 'Matematika', ind: 'B. Indonesia', eng: 'B. Inggris', mtk_lanjut: 'Matematika Tingkat Lanjut', ind_lanjut: 'B. Indonesia Tingkat Lanjut', eng_lanjut: 'B. Inggris Tingkat Lanjut' };
      const subjectLabel = SUBJECT_LABELS[key] || 'Mapel';

      const card = document.createElement('div');
      card.className = `neo-deck-card ${key} ${item.panoramaClass}`;
      card.dataset.subject = key;

      card.innerHTML = `
        <div class="card-inner-top">
          <div class="card-badge-row">
            <span class="card-subject-tag ${key}">${s.badge}</span>
            <span class="card-subject-glyph ${key}">${s.iconSvg || ''}</span>
          </div>
          <h3 class="card-subject-name">${s.title}</h3>
          <p class="card-subject-desc">${s.description}</p>
        </div>

        <div class="card-inner-bottom">
          <div class="card-meta-spec">
            <div class="spec-col">
              <span class="spec-label">BANK SOAL</span>
              <span class="spec-value">${s.totalPool} Butir</span>
            </div>
            <div class="spec-divider"></div>
            <div class="spec-col right-col">
              <span class="spec-label">STANDARISASI</span>
              <span class="spec-value">HOTS Teruji</span>
            </div>
          </div>

          <button class="btn-card-enter ${key}">
            <span>Buka Modul ${subjectLabel}</span>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
          </button>
        </div>
      `;

      // Dual listener: bind enter button and card container for touch-device safety
      const enterBtn = card.querySelector('.btn-card-enter');
      if (enterBtn) {
        enterBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          navigateTo('subject', key);
        });
      }

      card.addEventListener('click', () => {
        navigateTo('subject', key);
      });

      els.cardsDeckContainer.appendChild(card);
    });
  }

  function initHomeListeners() {
    if (els.btnLaunchDiagnosticBanner) {
      els.btnLaunchDiagnosticBanner.addEventListener('click', () => {
        launchDiagnosticSession();
      });
    }

    if (els.btnStartDiagnosticCta) {
      els.btnStartDiagnosticCta.addEventListener('click', (e) => {
        e.stopPropagation();
        launchDiagnosticSession();
      });
    }

    if (els.homeTotalSoalStat && window.TKA_DATABASE) {
      const total = Object.values(window.TKA_DATABASE).reduce((acc, sub) => acc + (sub.questions ? sub.questions.length : 0), 0);
      if (total > 0) els.homeTotalSoalStat.textContent = total.toLocaleString('id-ID');
    }

    const catalogWrapper = els.electiveGridWrapper || els.electiveGridContainer;
    if (els.btnToggleElectiveCatalog && catalogWrapper) {
      els.btnToggleElectiveCatalog.addEventListener('click', () => {
        const isHidden = catalogWrapper.classList.contains('hidden');
        if (isHidden) {
          renderElectiveCatalog('all');
          catalogWrapper.classList.remove('hidden');
          els.btnToggleElectiveCatalog.classList.add('expanded');
          els.btnToggleElectiveCatalog.setAttribute('aria-expanded', 'true');
          if (els.toggleElectiveLabel) els.toggleElectiveLabel.textContent = 'Tutup Katalog 19 Mapel Pilihan';
        } else {
          catalogWrapper.classList.add('hidden');
          els.btnToggleElectiveCatalog.classList.remove('expanded');
          els.btnToggleElectiveCatalog.setAttribute('aria-expanded', 'false');
          if (els.toggleElectiveLabel) els.toggleElectiveLabel.textContent = 'Buka Katalog 19 Mapel Pilihan';
        }
      });
    }

    // Cluster Filter Tabs Listener
    if (els.electiveClusterTabs) {
      els.electiveClusterTabs.addEventListener('click', (e) => {
        const btn = e.target.closest('.btn-cluster-tab');
        if (!btn || btn.classList.contains('active')) return;
        els.electiveClusterTabs.querySelectorAll('.btn-cluster-tab').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const cluster = btn.dataset.cluster || 'all';
        renderElectiveCatalog(cluster);
      });
    }

    // Deck Group Switcher: Wajib ↔ Lanjutan
    const switcherEl = document.getElementById('deckGroupSwitcher');
    if (switcherEl) {
      switcherEl.addEventListener('click', (e) => {
        const btn = e.target.closest('.btn-group-tab');
        if (!btn || btn.classList.contains('active')) return;
        const group = btn.dataset.deck;
        switcherEl.querySelectorAll('.btn-group-tab').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        renderHomeDeck(group);
        initMobilePanorama();
      });
    }
  }

  function initMobilePanorama() {
    if (!els.cardsDeckContainer) return;

    const cards = els.cardsDeckContainer.querySelectorAll('.neo-deck-card');
    const isLanjut = state.activeDeckGroup === 'lanjut';
    const subjectOrder = isLanjut ? ['ind_lanjut', 'mtk_lanjut', 'eng_lanjut'] : ['ind', 'mtk', 'eng'];
    
    // Update orbit controller pills dynamically
    const navContainer = document.getElementById('mobilePanoramaNav');
    if (navContainer) {
      navContainer.innerHTML = isLanjut ? `
        <button type="button" class="btn-pano-pill" data-pano="ind_lanjut" title="Pindah ke B. Indonesia Lanjutan">
          <span class="pano-pill-badge ind_lanjut">IND+</span>
          <span class="pano-pill-label">Indo</span>
        </button>
        <button type="button" class="btn-pano-pill active" data-pano="mtk_lanjut" title="Pindah ke Matematika Lanjutan">
          <span class="pano-pill-badge mtk_lanjut">MTK+</span>
          <span class="pano-pill-label">MTK</span>
        </button>
        <button type="button" class="btn-pano-pill" data-pano="eng_lanjut" title="Pindah ke B. Inggris Lanjutan">
          <span class="pano-pill-badge eng_lanjut">ENG+</span>
          <span class="pano-pill-label">Inggris</span>
        </button>
      ` : `
        <button type="button" class="btn-pano-pill" data-pano="ind" title="Pindah ke Bahasa Indonesia">
          <span class="pano-pill-badge ind">IND</span>
          <span class="pano-pill-label">Indo</span>
        </button>
        <button type="button" class="btn-pano-pill active" data-pano="mtk" title="Pindah ke Matematika">
          <span class="pano-pill-badge mtk">MTK</span>
          <span class="pano-pill-label">MTK</span>
        </button>
        <button type="button" class="btn-pano-pill" data-pano="eng" title="Pindah ke Bahasa Inggris">
          <span class="pano-pill-badge eng">ENG</span>
          <span class="pano-pill-label">Inggris</span>
        </button>
      `;
    }
    const navPills = document.querySelectorAll('.mobile-panorama-nav .btn-pano-pill');

    function updatePanorama3DStates(activeSubject) {
      const activeIdx = subjectOrder.indexOf(activeSubject);

      cards.forEach(card => {
        const cardSubj = card.dataset.subject;
        const cardIdx = subjectOrder.indexOf(cardSubj);
        card.classList.remove('is-active-center', 'is-peek-left', 'is-peek-right');

        if (cardIdx === activeIdx) {
          card.classList.add('is-active-center');
        } else if (cardIdx < activeIdx) {
          card.classList.add('is-peek-left');
        } else {
          card.classList.add('is-peek-right');
        }
      });

      if (navPills.length) {
        navPills.forEach(p => {
          const isActive = p.dataset.pano === activeSubject;
          p.classList.toggle('active', isActive);
          p.setAttribute('aria-selected', isActive ? 'true' : 'false');
        });
      }
    }

    let isProgrammaticScroll = false;
    let programmaticScrollTimer = null;

    if (navPills.length) {
      navPills.forEach(pill => {
        pill.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          const targetSubject = pill.dataset.pano;
          
          // Lock programmatic scroll to prevent scroll-event flutter
          isProgrammaticScroll = true;
          clearTimeout(programmaticScrollTimer);
          updatePanorama3DStates(targetSubject);

          const targetCard = els.cardsDeckContainer.querySelector(`.neo-deck-card[data-subject="${targetSubject}"]`);
          if (targetCard) {
            try {
              targetCard.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
            } catch (err) {
              targetCard.scrollIntoView();
            }
          }

          programmaticScrollTimer = setTimeout(() => {
            isProgrammaticScroll = false;
          }, 500);
        });
      });
    }

    // Dynamic 3D Curvature Sync on Swipe & Scroll (De-bounced, single-instance)
    let scrollTimeout;
    const onDeckScroll = () => {
      if (isProgrammaticScroll) return;
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => {
        if (isProgrammaticScroll) return;
        const containerRect = els.cardsDeckContainer.getBoundingClientRect();
        const centerX = containerRect.left + containerRect.width / 2;
        let closestCard = null;
        let minDistance = Infinity;

        cards.forEach(card => {
          const rect = card.getBoundingClientRect();
          const cardCenter = rect.left + rect.width / 2;
          const dist = Math.abs(centerX - cardCenter);
          if (dist < minDistance) {
            minDistance = dist;
            closestCard = card;
          }
        });

        if (closestCard) {
          updatePanorama3DStates(closestCard.dataset.subject);
        }
      }, 50);
    };

    if (els.cardsDeckContainer._deckScrollHandler) {
      els.cardsDeckContainer.removeEventListener('scroll', els.cardsDeckContainer._deckScrollHandler);
    }
    els.cardsDeckContainer._deckScrollHandler = onDeckScroll;
    els.cardsDeckContainer.addEventListener('scroll', onDeckScroll, { passive: true });

    // Initial Load: Center on the middle card with 3D Panorama Curvature
    setTimeout(() => {
      const centerSubj = state.activeDeckGroup === 'lanjut' ? 'mtk_lanjut' : 'mtk';
      updatePanorama3DStates(centerSubj);
      const centerCard = els.cardsDeckContainer.querySelector(`.neo-deck-card[data-subject="${centerSubj}"]`);
      if (centerCard) {
        try {
          centerCard.scrollIntoView({ behavior: 'auto', inline: 'center', block: 'nearest' });
        } catch (err) {
          centerCard.scrollIntoView();
        }
      }
    }, 80);
  }

  function renderElectiveCatalog(activeCluster = 'all') {
    if (!els.electiveGridContainer) return;

    const catalog = window.TKA_ELECTIVE_CATALOG || [];
    const filtered = (activeCluster === 'all') 
      ? catalog 
      : catalog.filter(item => item.clusterId === activeCluster);

    els.electiveGridContainer.innerHTML = '';

    filtered.forEach(item => {
      const card = document.createElement('div');
      card.className = `elective-card ${item.clusterId || ''} ${item.isReady ? 'is-ready' : 'is-pending'}`;
      card.style.setProperty('--cluster-accent', item.clusterColor || '#38bdf8');

      card.innerHTML = `
        <div class="elective-card-header">
          <div class="elective-card-tags">
            <span class="elective-cluster-tag" style="background: ${item.clusterColor}15; color: ${item.clusterColor}; border-color: ${item.clusterColor}40;">
              ${item.clusterTag || item.clusterName}
            </span>
            <span class="elective-sub-badge">${item.badge}</span>
          </div>
          <span class="elective-status-indicator ${item.isReady ? 'ready' : 'pending'}">
            <span class="status-dot"></span>
            ${item.isReady ? ((window.TKA_DATABASE && window.TKA_DATABASE[item.targetSubjectKey]) ? window.TKA_DATABASE[item.targetSubjectKey].totalPool + ' Soal TKA 2026' : (item.statusText || 'Aktif')) : 'Antrean Rilis'}
          </span>
        </div>

        <div class="elective-card-title-row">
          <div class="elective-icon-wrap" style="color: ${item.clusterColor}; background: ${item.clusterColor}12; border-color: ${item.clusterColor}30;">
            ${item.iconSvg || `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/></svg>`}
          </div>
          <div class="elective-title-group">
            <h4 class="elective-card-title">${item.title}</h4>
            <span class="elective-cluster-subtitle">${item.clusterName}</span>
          </div>
        </div>

        <div class="elective-card-body">
          <div class="elective-content-block topics-block">
            <div class="content-block-label">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              <span>CAKUPAN MATERI PUSMENDIK / BSKAP</span>
            </div>
            <p class="content-block-desc">${item.topics}</p>
          </div>

          <div class="elective-content-block comp-block" style="border-left-color: ${item.clusterColor};">
            <div class="content-block-label">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>TARGET STANDAR KOMPETENSI ANALITIS</span>
            </div>
            <p class="content-block-desc">${item.targetCompetency}</p>
          </div>
        </div>

        <div class="elective-card-footer">
          ${item.isReady && item.targetSubjectKey ? `
            <button class="btn-open-elective-hub" data-target="${item.targetSubjectKey}" style="--btn-accent: ${item.clusterColor};">
              <span>Buka Modul Latihan &amp; Ujian</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
          ` : `
            <div class="elective-queue-notice">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/></svg>
              <span>${item.statusText || 'Dalam Antrean Produksi Kluster'}</span>
            </div>
          `}
        </div>
      `;
      els.electiveGridContainer.appendChild(card);
    });

    // Attach click listeners for ready cards (both card body and action button)
    els.electiveGridContainer.querySelectorAll('.elective-card.is-ready').forEach(card => {
      card.style.cursor = 'pointer';
      card.addEventListener('click', () => {
        const btn = card.querySelector('.btn-open-elective-hub');
        const targetSubj = btn ? btn.dataset.target : null;
        if (targetSubj) navigateTo('subject', targetSubj);
      });
    });

    els.electiveGridContainer.querySelectorAll('.btn-open-elective-hub').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const targetSubj = btn.dataset.target;
        if (targetSubj) navigateTo('subject', targetSubj);
      });
    });
  }

  // =========================================================================
  // VIEW 2: DEDICATED SUBJECT PAGE RENDERER
  // =========================================================================
  function renderSubjectHub(subjectKey) {
    const s = window.TKA_DATABASE[subjectKey];
    if (!s) return;

    if (els.viewSubject) {
      els.viewSubject.setAttribute('data-subject-theme', subjectKey);
      els.viewSubject.classList.remove('subject-animating');
      void els.viewSubject.offsetWidth; // Force reflow to re-trigger CSS animations
      els.viewSubject.classList.add('subject-animating');
    }

    els.subjectHubTitle.textContent = s.title;
    els.subjectHubDesc.textContent = s.description;

    // Strict 3-level reset: default to 'easy'
    state.selectedDifficulty = 'easy';
    els.levelPills.forEach(p => {
      p.classList.toggle('active', p.dataset.diff === 'easy');
    });
  }

  function initSubjectHubListeners() {
    els.btnSubjectBackToHome.addEventListener('click', () => {
      navigateTo('home');
    });

    // Level Picker (Strictly 3 levels: Mudah, Sedang, Sulit)
    els.levelPills.forEach(pill => {
      pill.addEventListener('click', () => {
        els.levelPills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.selectedDifficulty = pill.dataset.diff;
      });
    });

    // Launch Training Lab
    els.btnStartLatihan.addEventListener('click', () => {
      launchSession('latihan', state.selectedDifficulty);
    });

    // Launch Exam Arena (Curated hardest mix)
    els.btnStartSimulasi.addEventListener('click', () => {
      launchSession('simulasi', 'hard');
    });
  }

  // =========================================================================
  // SESSION LAUNCHER (TRAINING / SIMULATION / DIAGNOSTIC)
  // =========================================================================
  function launchSession(mode, difficulty) {
    const sKey = state.currentSubject;
    const sData = window.TKA_DATABASE[sKey];
    if (!sData) return;

    state.sessionMode = mode;
    state.selectedDifficulty = difficulty;

    // Filter questions robustly by mode and difficulty
    let pool = [];
    if (mode === 'simulasi') {
      pool = sData.questions.filter(q => q.mode === 'simulasi' || q.difficulty === 'simulation_hots');
      if (pool.length === 0) {
        pool = sData.questions.filter(q => q.difficulty === 'hard');
      }
    } else {
      // mode === 'latihan'
      const targetDiff = difficulty || state.selectedDifficulty || 'easy';
      pool = sData.questions.filter(q => q.mode === 'latihan' && q.difficulty === targetDiff);
      // Fallback 1: match difficulty only
      if (pool.length === 0) {
        pool = sData.questions.filter(q => q.difficulty === targetDiff && q.difficulty !== 'simulation_hots');
      }
      // Fallback 2: all latihan questions
      if (pool.length === 0) {
        pool = sData.questions.filter(q => q.mode === 'latihan' || (q.mode !== 'simulasi' && q.difficulty !== 'simulation_hots'));
      }
    }

    if (pool.length === 0) {
      pool = sData.questions;
    }

    // Reset exam state
    state.exam.questions = pool;
    state.exam.currentIndex = 0;
    state.exam.answers = {};
    state.exam.flags = {};
    state.exam.strikes = 0;
    state.exam.isFinished = false;
    state.exam.isReviewMode = false;
    state.exam.startTime = Date.now();

    // Setup Workspace Meta Header
    els.infoSubjectName.textContent = sData.title;
    els.infoModeBadge.className = `info-mode-badge ${mode}`;
    els.infoModeBadge.textContent = mode === 'latihan' ? 'LATIHAN MANDIRI' : 'SIMULASI HOTS';
    els.infoModeBadge.style.color = '';

    if (mode === 'simulasi') {
      document.body.classList.add('session-mode-simulasi');
      els.scaffoldingBottomPanel.classList.add('hidden');
      els.hudStrikeBox.classList.remove('hidden');
      els.hudTimerBox.classList.remove('hidden');
      updateStrikeDots(0);
      startTimer(60 * 60); // 60 minutes for 30 HOTS simulation questions

      const reqFs = document.documentElement.requestFullscreen || document.documentElement.webkitRequestFullscreen;
      if (reqFs && typeof reqFs === 'function') {
        reqFs.call(document.documentElement).catch(() => {});
      }
    } else {
      document.body.classList.remove('session-mode-simulasi');
      els.scaffoldingBottomPanel.classList.remove('hidden');
      els.hudStrikeBox.classList.add('hidden');
      els.hudTimerBox.classList.add('hidden');
      stopTimer();
    }

    navigateTo('workspace');
    renderQuestion(0);
  }

  // =========================================================================
  // INTEGRATED 15-QUESTION DIAGNOSTIC SESSION
  // =========================================================================
  function launchDiagnosticSession() {
    if (!window.TKA_DATABASE) return;

    const mtkDiag = (window.TKA_DATABASE.mtk?.questions || []).filter(q => q.isDiagnostic);
    const indDiag = (window.TKA_DATABASE.ind?.questions || []).filter(q => q.isDiagnostic);
    const engDiag = (window.TKA_DATABASE.eng?.questions || []).filter(q => q.isDiagnostic);

    const pool = [...mtkDiag, ...indDiag, ...engDiag];
    if (pool.length === 0) return;

    state.sessionMode = 'diagnostik';
    state.currentSubject = 'diag';
    state.selectedDifficulty = 'all';

    state.exam.questions = pool;
    state.exam.currentIndex = 0;
    state.exam.answers = {};
    state.exam.flags = {};
    state.exam.strikes = 0;
    state.exam.isFinished = false;
    state.exam.isReviewMode = false;
    state.exam.startTime = Date.now();

    els.infoSubjectName.textContent = 'Tes Diagnostik (15 Soal)';
    els.infoModeBadge.className = 'info-mode-badge diagnostik';
    els.infoModeBadge.textContent = 'DIAGNOSTIK';
    els.infoModeBadge.style.color = '';

    // No scaffolding in diagnostic evaluation
    els.scaffoldingBottomPanel.classList.add('hidden');
    els.hudStrikeBox.classList.add('hidden');
    els.hudTimerBox.classList.remove('hidden');
    startTimer(25 * 60);

    syncNavbarState('diag');
    navigateTo('workspace');
    renderQuestion(0);
  }

  // =========================================================================
  // FULLSCREEN BUTTON STATE SYNCHRONIZATION
  // =========================================================================
  function syncFullscreenButtonState() {
    const isFsSupported = !!(document.fullscreenEnabled || document.webkitFullscreenEnabled || (document.documentElement && (document.documentElement.requestFullscreen || document.documentElement.webkitRequestFullscreen)));
    if (els.btnToggleFullscreen) {
      if (!isFsSupported) {
        els.btnToggleFullscreen.style.display = 'none';
        return;
      }
      els.btnToggleFullscreen.style.display = '';
      const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement);
      const textSpan = els.btnToggleFullscreen.querySelector('.fs-text');
      if (textSpan) textSpan.textContent = isFs ? 'Kecilkan' : 'Layar Penuh';
      const iconSvg = els.btnToggleFullscreen.querySelector('svg');
      if (iconSvg) {
        if (isFs) {
          iconSvg.innerHTML = '<path d="M8 3v3a2 2 0 0 1-2 2H3m18 0h-3a2 2 0 0 1-2-2V3m0 18v-3a2 2 0 0 1 2-2h3M3 16h3a2 2 0 0 1 2 2v3"/>';
        } else {
          iconSvg.innerHTML = '<path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/>';
        }
      }
    }
  }

  // =========================================================================
  // HELPER: QUESTION CORRECTNESS & ANSWERED EVALUATOR
  // =========================================================================
  function isQuestionAnswered(q, ans) {
    if (ans === undefined || ans === null) return false;
    const isMulti = q.type === 'multi' || q.type === 'multiple_response';
    const isMatrix = q.type === 'matrix' || q.type === 'complex_table';

    if (isMulti) {
      return Array.isArray(ans) && ans.length > 0;
    }
    if (isMatrix) {
      const statements = getNormalizedStatements(q);
      if (!statements.length) return false;
      return typeof ans === 'object' && statements.every(s => ans[s.id] !== undefined);
    }
    return true;
  }

  function checkQuestionCorrectness(q, ans) {
    if (!ans) return false;
    const isMulti = q.type === 'multi' || q.type === 'multiple_response';
    const isMatrix = q.type === 'matrix' || q.type === 'complex_table';

    if (isMulti) {
      if (!Array.isArray(ans)) return false;
      const correctKeys = q.correctKeys || (Array.isArray(q.correctAnswers) ? q.correctAnswers : (Array.isArray(q.correctAnswer) ? q.correctAnswer : [q.correctAnswer || q.correctKey]));
      if (ans.length !== correctKeys.length) return false;
      return correctKeys.every(k => ans.includes(k));
    } else if (isMatrix) {
      if (typeof ans !== 'object' || Array.isArray(ans)) return false;
      const statements = getNormalizedStatements(q);
      if (!statements.length) return false;
      return statements.every(stmt => {
        const correctChoice = getStatementCorrectAnswer(q, stmt);
        const userChoice = ans[stmt.id];
        return userChoice === correctChoice;
      });
    } else {
      const correctKey = q.correctKey || q.correctAnswer;
      return ans === correctKey;
    }
  }

  // =========================================================================
  // CBT CHIPS NAVIGATOR STATE SYNCHRONIZATION
  // =========================================================================
  function updateNavigatorChipsState() {
    const total = state.exam.questions.length;
    let answeredCount = 0;

    state.exam.questions.forEach((q, idx) => {
      const ans = state.exam.answers[idx];
      const hasAnswered = isQuestionAnswered(q, ans);
      if (hasAnswered) answeredCount++;
    });

    if (els.cbtProgressBadge) {
      els.cbtProgressBadge.textContent = `${answeredCount} / ${total}`;
    }
    if (els.gridDrawerIndicator) {
      els.gridDrawerIndicator.textContent = `${state.exam.currentIndex + 1} / ${total}`;
    }

    // Render Desktop Right-Hand Sidebar Chips
    if (els.cbtChipsGrid) {
      // Retain or create the liquid gliding indicator pill
      let glider = els.cbtChipsGrid.querySelector('.cbt-active-glider');
      if (!glider) {
        glider = document.createElement('div');
        glider.className = 'cbt-active-glider';
      }

      els.cbtChipsGrid.innerHTML = '';
      els.cbtChipsGrid.appendChild(glider);

      state.exam.questions.forEach((q, idx) => {
        const chip = document.createElement('button');
        const isActive = (idx === state.exam.currentIndex);
        const ans = state.exam.answers[idx];
        const isFlagged = !!(state.exam.flags && state.exam.flags[idx]);

        let chipClasses = ['cbt-chip'];
        if (isActive) chipClasses.push('active');

        if (state.exam.isReviewMode) {
          const isCorrect = checkQuestionCorrectness(q, ans);
          chipClasses.push(isCorrect ? 'review-correct' : 'review-wrong');
        } else {
          const hasAnswered = isQuestionAnswered(q, ans);
          if (hasAnswered) chipClasses.push('answered');
          if (isFlagged) chipClasses.push('flagged');
        }

        chip.className = chipClasses.join(' ');
        chip.textContent = String(idx + 1).padStart(2, '0');
        chip.title = `Lompat ke Soal ${idx + 1}${isFlagged ? ' (Ragu-Ragu)' : ''}`;
        chip.addEventListener('click', () => {
          renderQuestion(idx);
        });
        els.cbtChipsGrid.appendChild(chip);
      });

      // Animate fluid liquid glider with soft bounce positioning
      requestAnimationFrame(() => {
        const activeChip = els.cbtChipsGrid.querySelector('.cbt-chip.active');
        if (activeChip && glider) {
          glider.style.width = `${activeChip.offsetWidth}px`;
          glider.style.height = `${activeChip.offsetHeight}px`;
          glider.style.transform = `translate3d(${activeChip.offsetLeft}px, ${activeChip.offsetTop}px, 0)`;
          glider.classList.add('visible');
        }
      });
    }

    // Render Mobile Drawer Chips
    if (els.gridNumbersContainer) {
      els.gridNumbersContainer.innerHTML = '';
      state.exam.questions.forEach((q, idx) => {
        const chip = document.createElement('button');
        const isActive = (idx === state.exam.currentIndex);
        const ans = state.exam.answers[idx];
        const isFlagged = !!(state.exam.flags && state.exam.flags[idx]);

        let chipClasses = ['grid-chip-item'];
        if (isActive) chipClasses.push('active');

        if (state.exam.isReviewMode) {
          const isCorrect = checkQuestionCorrectness(q, ans);
          chipClasses.push(isCorrect ? 'review-correct' : 'review-wrong');
        } else {
          const hasAnswered = isQuestionAnswered(q, ans);
          if (hasAnswered) chipClasses.push('answered');
          if (isFlagged) chipClasses.push('flagged');
        }

        chip.className = chipClasses.join(' ');
        chip.textContent = String(idx + 1).padStart(2, '0');
        chip.title = `Soal ${idx + 1}${isFlagged ? ' (Ragu-Ragu)' : ''}`;
        chip.addEventListener('click', () => {
          closeGridDrawer();
          renderQuestion(idx);
        });
        els.gridNumbersContainer.appendChild(chip);
      });
    }
  }

  // =========================================================================
  // CONTEXTUAL SCAFFOLDING ACCORDION (APPLE HIG HARDWARE-ACCELERATED GRID)
  // =========================================================================
  function getAccordionList() {
    return [
      { item: els.scaffoldItemFormula, collapse: els.drawerFormulaHud, btn: els.btnToggleFormulaHud, pill: els.formulaStatusPill },
      { item: els.scaffoldItemClue1, collapse: els.drawerClue1, btn: els.btnToggleClue1, pill: els.clue1StatusPill },
      { item: els.scaffoldItemClue2, collapse: els.drawerClue2, btn: els.btnToggleClue2, pill: els.clue2StatusPill },
      { item: els.scaffoldItemSolution, collapse: els.drawerSolution, btn: els.btnToggleSolution, pill: els.solutionStatusPill }
    ];
  }

  function closeSingleAccordion(itemEl, collapseEl, triggerBtn, statusPill) {
    if (!itemEl || !itemEl.classList.contains('is-open')) return;

    itemEl.classList.remove('is-open');
    if (triggerBtn) triggerBtn.setAttribute('aria-expanded', 'false');
    if (statusPill) statusPill.textContent = 'Buka';

    // Clear any inline styles so pure CSS Grid handles transition cleanly
    if (collapseEl) {
      collapseEl.style.height = '';
      collapseEl.style.display = '';
      collapseEl.style.opacity = '';
    }
  }

  function toggleAccordionItem(itemEl, collapseEl, triggerBtn, statusPill, onOpenCallback) {
    if (!itemEl) return;
    const isOpen = itemEl.classList.contains('is-open');

    if (isOpen) {
      // 1. Smooth collapse via CSS transition
      closeSingleAccordion(itemEl, collapseEl, triggerBtn, statusPill);

      // 2. Scroll recovery: ONLY if user scrolled so far down that the header is off the top
      const itemRect = itemEl.getBoundingClientRect();
      if (itemRect.top < 64) {
        itemEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    } else {
      // 1. Auto-collapse other open accordion items so user stays focused
      getAccordionList().forEach(acc => {
        if (acc.item && acc.item !== itemEl && acc.item.classList.contains('is-open')) {
          closeSingleAccordion(acc.item, acc.collapse, acc.btn, acc.pill);
        }
      });

      // Clear any inline styles
      if (collapseEl) {
        collapseEl.style.height = '';
        collapseEl.style.display = '';
        collapseEl.style.opacity = '';
      }

      if (typeof onOpenCallback === 'function') {
        onOpenCallback();
      }
      triggerKaTeX();

      // 2. Open item: class toggle triggers silky 60/120 FPS CSS grid interpolation
      itemEl.classList.add('is-open');
      if (statusPill) statusPill.textContent = 'Tutup';
      if (triggerBtn) triggerBtn.setAttribute('aria-expanded', 'true');

      // 3. Smart, gentle scroll check ONLY if the card is clipped near viewport bottom
      setTimeout(() => {
        const itemRect = itemEl.getBoundingClientRect();
        const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
        
        // If the button is too close to bottom edge or off-screen, gently bring into reading view
        if (itemRect.bottom > viewportHeight - 60 || itemRect.top < 70) {
          itemEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }, 70);
    }
  }

  function resetAllAccordionItems() {
    getAccordionList().forEach(({ item, collapse, btn, pill }) => {
      if (item) item.classList.remove('is-open');
      if (collapse) {
        collapse.style.height = '';
        collapse.style.display = '';
        collapse.style.opacity = '';
      }
      if (btn) btn.setAttribute('aria-expanded', 'false');
      if (pill) pill.textContent = 'Buka';
    });
  }

  // =========================================================================
  // CODE SNIPPET BOX & SYNTAX HIGHLIGHTING (IDE TERMINAL ENGINE)
  // =========================================================================
  function escapeHtml(str) {
    if (str === null || str === undefined) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  const CODE_JAVA_KEYWORDS = new Set([
    'class', 'extends', 'implements', 'public', 'private', 'protected',
    'static', 'final', 'void', 'return', 'new', 'this', 'super', 'if',
    'else', 'for', 'while', 'do', 'try', 'catch', 'finally', 'throw', 'throws',
    'import', 'package', 'interface', 'abstract', 'instanceof', 'switch', 'case',
    'default', 'break', 'continue', 'const', 'let', 'var', 'function', 'async',
    'await', 'export', 'from', 'typeof'
  ]);

  const CODE_JAVA_TYPES = new Set([
    'String', 'int', 'double', 'float', 'boolean', 'char', 'byte', 'short',
    'long', 'Object', 'Main', 'Pegawai', 'Programmer', 'System', 'Promise',
    'Array', 'Map', 'Set', 'Integer', 'Boolean', 'Double', 'Float', 'Character',
    'Exception', 'List', 'ArrayList', 'HashMap', 'HashSet', 'console', 'JSON'
  ]);

  const CODE_SQL_KEYWORDS = new Set([
    'SELECT', 'FROM', 'WHERE', 'GROUP', 'BY', 'ORDER', 'HAVING', 'INSERT',
    'INTO', 'UPDATE', 'DELETE', 'JOIN', 'INNER', 'LEFT', 'RIGHT', 'OUTER',
    'ON', 'AS', 'AND', 'OR', 'NOT', 'IN', 'BETWEEN', 'LIKE', 'IS', 'NULL',
    'COUNT', 'AVG', 'SUM', 'MAX', 'MIN', 'DISTINCT', 'LIMIT', 'OFFSET',
    'UNION', 'ALL', 'CREATE', 'TABLE', 'ALTER', 'DROP', 'PRIMARY', 'KEY',
    'FOREIGN', 'REFERENCES', 'VALUES', 'SET', 'DEFAULT', 'CHECK', 'INDEX',
    'VIEW', 'TRIGGER', 'PROCEDURE', 'FUNCTION', 'TRANSACTION', 'COMMIT', 'ROLLBACK'
  ]);

  function highlightCodeSyntax(code, lang) {
    const l = (lang || '').toLowerCase();
    const tokenRegex = /(\/\/[^\n]*|\/\*[\s\S]*?\*\/|--[^\n]*|"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*'|@\w+|\b\d+(?:\.\d+)?\b|\b[a-zA-Z_]\w*\b|[^\s\w])/g;

    let result = '';
    let lastIndex = 0;
    let match;

    while ((match = tokenRegex.exec(code)) !== null) {
      if (match.index > lastIndex) {
        result += escapeHtml(code.slice(lastIndex, match.index));
      }
      lastIndex = tokenRegex.lastIndex;

      const val = match[1];
      const esc = escapeHtml(val);

      if (val.startsWith('//') || val.startsWith('/*') || val.startsWith('--')) {
        result += `<span class="tok-comment">${esc}</span>`;
      } else if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        result += `<span class="tok-str">${esc}</span>`;
      } else if (val.startsWith('@')) {
        result += `<span class="tok-annot">${esc}</span>`;
      } else if (/^\d/.test(val)) {
        result += `<span class="tok-num">${esc}</span>`;
      } else if (l === 'java' || l === 'javascript' || l === 'js') {
        if (CODE_JAVA_KEYWORDS.has(val)) {
          result += `<span class="tok-kw">${esc}</span>`;
        } else if (CODE_JAVA_TYPES.has(val)) {
          result += `<span class="tok-type">${esc}</span>`;
        } else if (['println', 'print', 'setTimeout', 'resolve', 'reject', 'then', 'log', 'kerja', 'toString'].includes(val)) {
          result += `<span class="tok-fn">${esc}</span>`;
        } else {
          result += esc;
        }
      } else if (l === 'sql') {
        if (CODE_SQL_KEYWORDS.has(val.toUpperCase())) {
          result += `<span class="tok-kw">${esc.toUpperCase()}</span>`;
        } else {
          result += esc;
        }
      } else {
        result += esc;
      }
    }

    if (lastIndex < code.length) {
      result += escapeHtml(code.slice(lastIndex));
    }
    return result;
  }

  function renderCodeBox(code, lang) {
    const rawLang = (lang || '').trim();
    const displayLang = rawLang ? rawLang.toUpperCase() : 'CODE';
    const highlighted = highlightCodeSyntax(code, rawLang);
    const lineCount = code.split('\n').length;
    const lineNumbers = Array.from({ length: lineCount }, (_, i) => `<span>${i + 1}</span>`).join('');
    const encoded = encodeURIComponent(code);

    return `<div class="code-snippet-box" data-raw-code="${encoded}">
      <div class="code-box-header">
        <div class="code-box-header-left">
          <div class="mac-dots" aria-hidden="true">
            <span class="mac-dot red"></span>
            <span class="mac-dot yellow"></span>
            <span class="mac-dot green"></span>
          </div>
          <span class="code-lang-badge">${displayLang}</span>
        </div>
        <div class="code-box-header-right">
          <button type="button" class="btn-copy-code" onclick="window.copyCodeSnippet(this)" title="Salin potongan kode">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
              <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
            </svg>
            <span>Salin</span>
          </button>
        </div>
      </div>
      <div class="code-box-body">
        <div class="code-line-numbers" aria-hidden="true">${lineNumbers}</div>
        <pre class="code-pre"><code class="code-content language-${displayLang.toLowerCase()}">${highlighted}</code></pre>
      </div>
    </div>`;
  }

  window.copyCodeSnippet = function(button) {
    if (!button) return;
    const box = button.closest('.code-snippet-box');
    if (!box) return;
    const rawEncoded = box.getAttribute('data-raw-code');
    const code = rawEncoded ? decodeURIComponent(rawEncoded) : (box.querySelector('.code-content')?.textContent || '');

    const finishCopy = () => {
      const originalHtml = button.innerHTML;
      button.classList.add('copied');
      button.innerHTML = `
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        <span>Tersalin!</span>
      `;
      setTimeout(() => {
        button.classList.remove('copied');
        button.innerHTML = originalHtml;
      }, 2000);
    };

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(code).then(finishCopy).catch(() => {
        fallbackCopy(code, finishCopy);
      });
    } else {
      fallbackCopy(code, finishCopy);
    }
  };

  function fallbackCopy(text, cb) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
      if (cb) cb();
    } catch (e) {
      console.warn('Fallback copy failed', e);
    }
    document.body.removeChild(ta);
  }

  function formatContentWithCode(content, inlineOnly = false) {
    if (!content || typeof content !== 'string') return content || '';

    // If pure inline string without code block and without double-newlines
    if (inlineOnly || (!content.includes('```') && !content.includes('\n\n'))) {
      return content.replace(/`([^`\n]+)`/g, (m, inline) => `<code class="inline-code">${escapeHtml(inline)}</code>`);
    }

    const blocks = [];
    const placeholderPrefix = '___CODE_BLOCK_TOKEN_';
    let processed = content.replace(/```([a-zA-Z0-9_-]*)\s*([\s\S]*?)```/g, (match, lang, code) => {
      const idx = blocks.length;
      blocks.push(renderCodeBox(code.trim(), lang.trim()));
      return `\n\n${placeholderPrefix}${idx}___\n\n`;
    });

    processed = processed.replace(/`([^`\n]+)`/g, (m, inline) => {
      return `<code class="inline-code">${escapeHtml(inline)}</code>`;
    });

    const rawParts = processed.split(/\r?\n\r?\n/);
    const htmlParts = rawParts.map(part => {
      const trimmed = part.trim();
      if (!trimmed) return '';
      const tokenMatch = trimmed.match(new RegExp(`^${placeholderPrefix}(\\d+)___$`));
      if (tokenMatch) {
        const idx = parseInt(tokenMatch[1], 10);
        return blocks[idx] || '';
      }
      if (/<\/?(p|div|section|table|tr|td|th|ul|ol|li|h[1-6])\b/i.test(trimmed)) {
        return trimmed;
      }
      return `<p>${trimmed.replace(/\r?\n/g, '<br>')}</p>`;
    });

    let result = htmlParts.filter(Boolean).join('\n');
    blocks.forEach((blockHtml, i) => {
      result = result.replace(new RegExp(`${placeholderPrefix}${i}___`, 'g'), blockHtml);
    });

    return result;
  }

  // =========================================================================
  // QUESTION RENDERER & DOMAIN-AWARE SCAFFOLDING
  // =========================================================================
  function renderQuestion(index) {
    const q = state.exam.questions[index];
    if (!q) return;

    state.exam.currentIndex = index;

    // Header Badges
    if (els.paperQMateriBadge) {
      const materiText = q.materi || (q.topic ? q.topic.split(' ')[0] : 'MATERI');
      els.paperQMateriBadge.textContent = materiText.toUpperCase();
      const subj = q.subject || state.currentSubject || 'mtk';
      els.paperQMateriBadge.className = `paper-q-materi-badge ${subj}`;
    }

    els.paperQNum.textContent = `SOAL ${String(index + 1).padStart(2, '0')}`;
    els.paperQTopic.textContent = q.topic || 'Penalaran Akademik';
    const diffLabels = {
      easy: 'MUDAH',
      medium: 'SEDANG',
      hard: 'SULIT',
      simulation_hots: 'HOTS SIMULASI'
    };
    els.paperQDiff.textContent = diffLabels[q.difficulty] || (q.difficulty || 'SEDANG').toUpperCase();
    els.paperQDiff.className = `paper-q-diff ${q.difficulty || 'medium'}`;

    if (els.paperQTypeBadge) {
      if (q.type === 'matrix' || q.type === 'complex_table') {
        els.paperQTypeBadge.textContent = 'TABEL BENAR-SALAH';
        els.paperQTypeBadge.className = 'paper-q-type-badge matrix';
      } else if (q.type === 'multi' || q.type === 'multiple_response') {
        els.paperQTypeBadge.textContent = 'PILIHAN GANDA KOMPLEKS (MULTI)';
        els.paperQTypeBadge.className = 'paper-q-type-badge multi';
      } else {
        els.paperQTypeBadge.textContent = 'PILIHAN GANDA';
        els.paperQTypeBadge.className = 'paper-q-type-badge';
      }
    }

    els.gridDrawerIndicator.textContent = `${index + 1} / ${state.exam.questions.length}`;

    // Question body text: separate stimulus and prompt when available
    if (q.stimulus) {
      els.paperQText.innerHTML = `
        <section class="question-stimulus">
          <div class="question-stimulus-label">STIMULUS WACANA</div>
          ${formatContentWithCode(q.stimulus)}
        </section>
        <div class="question-prompt">${formatContentWithCode(q.questionHtml || (q.question ? `<p>${q.question}</p>` : ''))}</div>
      `;
    } else {
      els.paperQText.innerHTML = formatContentWithCode(q.questionHtml || (q.question ? `<p>${q.question}</p>` : ''));
    }

    // Domain-Aware Scaffolding Setup (Training Mode or Review Mode)
    if (state.sessionMode === 'latihan' || state.exam.isReviewMode) {
      document.body.classList.remove('session-mode-simulasi');
      if (els.scaffoldingBottomPanel) els.scaffoldingBottomPanel.classList.remove('hidden');

      // Reset all accordion items on question change
      resetAllAccordionItems();

      // Domain-Aware Button Labels & Drawer Headers (All 25 Subjects Supported)
      const subj = q.subject || state.currentSubject || 'mtk';
      if (['mtk', 'mtk_lanjut', 'fisika', 'kimia'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Rumus & Teorema';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'TEOREMA & FORMULA UMUM:';
      } else if (['biologi'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Konsep & Siklus Biologis';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'KONSEP & SIKLUS BIOLOGIS:';
      } else if (['ekonomi'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Hukum & Persamaan Ekonomi';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'HUKUM EKONOMI & PERSAMAAN MATEMATIS:';
      } else if (['geografi'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Prinsip & Sistem Spasial';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'PRINSIP GEOGRAFI & SISTEM SPASIAL:';
      } else if (['sosiologi', 'antropologi'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Teori & Paradigma Sosial';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'PARADIGMA & TEORI SOSIAL-BUDAYA:';
      } else if (['sejarah_lanjut'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Kronologi & Kausalitas';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'KONSEP HISTORIS & KAUSALITAS SEJARAH:';
      } else if (['informatika', 'rpl', 'tkj', 'rekayasa_desain'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Sintaks & Arsitektur Sistem';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'ARSITEKTUR, PROTOKOL & STANDAR TEKNIK:';
      } else if (['pkk'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Prinsip Produksi & Finansial';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'PRINSIP PRODUKSI & ANALISIS KEUANGAN:';
      } else if (['ind', 'ind_lanjut'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Kaidah Bahasa & Pola Logika';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'KAIDAH LOGIKA & STRUKTUR WACANA:';
      } else if (['eng', 'eng_lanjut'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Reading Strategy & Syntax Key';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'READING STRATEGY & DISCOURSE KEY:';
      } else if (['bahasa_arab', 'bahasa_jepang', 'bahasa_mandarin', 'bahasa_jerman', 'bahasa_prancis', 'bahasa_korea'].includes(subj)) {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Tata Bahasa & Pola Kalimat';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'KAIDAH TATA BAHASA & STRUKTUR KALIMAT:';
      } else {
        if (els.formulaHudBtnLabel) els.formulaHudBtnLabel.textContent = 'Rumus & Konsep Kunci';
        if (els.formulaHudHeader) els.formulaHudHeader.textContent = 'KONSEP & FORMULA KUNCI:';
      }

      // Formula / Domain HUD content
      const formulaData = q.formulaHud || (q.formula_title ? {
        title: q.formula_title,
        latex: q.formula_latex || '',
        legend: q.formula_legend || ''
      } : null);

      if (formulaData && state.sessionMode === 'latihan') {
        if (els.scaffoldItemFormula) els.scaffoldItemFormula.classList.remove('hidden');
        if (typeof formulaData === 'object' && formulaData !== null) {
          let hudHtml = '';
          if (formulaData.title) {
            hudHtml += `<div style="font-family: var(--font-mono); font-size: 11px; font-weight: 800; color: #60a5fa; margin-bottom: 8px;">${formulaData.title}</div>`;
          }
          if (formulaData.latex) {
            hudHtml += `<div class="formula-latex-block" style="font-size: 16px; margin: 8px 0;">$$\\displaystyle ${formulaData.latex}$$</div>`;
          }
          if (formulaData.legend) {
            hudHtml += `<div class="formula-legend-block" style="margin-top: 10px; font-size: 13.5px; color: #94a3b8; line-height: 1.6;">${formulaData.legend}</div>`;
          }
          if (els.formulaHudContent) els.formulaHudContent.innerHTML = hudHtml;
        } else {
          if (els.formulaHudContent) els.formulaHudContent.innerHTML = `$$\\displaystyle ${formulaData}$$`;
        }
      } else {
        if (els.scaffoldItemFormula) els.scaffoldItemFormula.classList.add('hidden');
      }

      // Conceptual Clues
      const hintsData = q.hints || ((q.concept_hint || q.execution_hint) ? {
        concept: q.concept_hint || '',
        execution: q.execution_hint || ''
      } : null);

      if (hintsData && state.sessionMode === 'latihan') {
        if (els.scaffoldItemClue1) els.scaffoldItemClue1.classList.remove('hidden');
        if (els.scaffoldItemClue2) els.scaffoldItemClue2.classList.remove('hidden');
        if (els.clue1Body) els.clue1Body.innerHTML = formatContentWithCode(hintsData.concept || 'Tidak ada petunjuk konsep.');
        if (els.clue2Body) els.clue2Body.innerHTML = formatContentWithCode(hintsData.execution || 'Tidak ada petunjuk eksekusi.');
      } else {
        if (els.scaffoldItemClue1) els.scaffoldItemClue1.classList.add('hidden');
        if (els.scaffoldItemClue2) els.scaffoldItemClue2.classList.add('hidden');
      }

      // Solution (Anti-Spoiler: Official key only displayed during Review Mode!)
      let rawSolution = q.explanation || q.solution || 'Panduan pengerjaan bertahap tersedia.';
      let solutionHtml = formatContentWithCode(rawSolution);
      if (state.exam.isReviewMode) {
        let keyText = '';
        if (q.type === 'matrix' || q.type === 'complex_table') {
          const stList = q.statements || q.tableStatements || [];
          keyText = stList.map((s, i) => {
            const sid = s.id !== undefined ? s.id : String(i);
            const isB = (q.correctAnswers && q.correctAnswers[sid] === true) ||
                        (q.correctAnswer && q.correctAnswer[sid] === 'B') ||
                        s.answer === 'B' || s.answer === true || s.isCorrect === true;
            return `[${i+1}] ${isB ? 'BENAR' : 'SALAH'}`;
          }).join(' • ');
        } else if (q.type === 'multi' || q.type === 'multiple_response') {
          keyText = (q.correctKeys || q.correctAnswers || []).join(', ');
        } else {
          keyText = q.correctKey || q.correctAnswer || '-';
        }

        solutionHtml = `
          <div class="review-key-banner">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
            <span>KUNCI JAWABAN RESMI: <strong>${keyText}</strong></span>
          </div>
        ` + solutionHtml;
      }
      if (els.solutionBodyContent) els.solutionBodyContent.innerHTML = solutionHtml;

      if (state.exam.isReviewMode) {
        // Automatically open the solution drawer in review mode!
        setTimeout(() => {
          if (els.scaffoldItemSolution && els.drawerSolution && !els.scaffoldItemSolution.classList.contains('is-open')) {
            toggleAccordionItem(els.scaffoldItemSolution, els.drawerSolution, els.btnToggleSolution, els.solutionStatusPill);
          }
        }, 120);
      }
    } else {
      // STRICT SIMULATION LOCKDOWN (Zero Clues, Zero Formula, Zero Explanation)
      document.body.classList.add('session-mode-simulasi');
      if (els.scaffoldingBottomPanel) els.scaffoldingBottomPanel.classList.add('hidden');
      resetAllAccordionItems();
      if (els.formulaHudContent) els.formulaHudContent.innerHTML = '';
      if (els.clue1Body) els.clue1Body.innerHTML = '';
      if (els.clue2Body) els.clue2Body.innerHTML = '';
      if (els.solutionBodyContent) els.solutionBodyContent.innerHTML = '';
    }

    // Render Options based on question type
    renderOptions(q, index);

    // Prev / Next button states
    els.btnPaperPrev.disabled = (index === 0);

    if (state.exam.isReviewMode) {
      // In review mode: NEVER show submit buttons!
      els.btnPaperSubmit.classList.add('hidden');
      if (els.btnReviewBackResults) els.btnReviewBackResults.classList.remove('hidden');
      if (els.cbtSidebarSubmitBox) els.cbtSidebarSubmitBox.classList.add('hidden');

      if (index === state.exam.questions.length - 1) {
        els.btnPaperNext.classList.add('hidden');
      } else {
        els.btnPaperNext.classList.remove('hidden');
      }
    } else {
      // Normal exam mode:
      if (els.btnReviewBackResults) els.btnReviewBackResults.classList.add('hidden');
      if (els.cbtSidebarSubmitBox) els.cbtSidebarSubmitBox.classList.remove('hidden');

      if (index === state.exam.questions.length - 1) {
        els.btnPaperNext.classList.add('hidden');
        els.btnPaperSubmit.classList.remove('hidden');
      } else {
        els.btnPaperNext.classList.remove('hidden');
        els.btnPaperSubmit.classList.add('hidden');
      }
    }

    // Flag (Ragu-Ragu) Button State
    if (els.btnPaperFlag) {
      if (state.exam.isReviewMode) {
        els.btnPaperFlag.classList.add('hidden');
      } else {
        els.btnPaperFlag.classList.remove('hidden');
        const isFlagged = !!(state.exam.flags && state.exam.flags[index]);
        els.btnPaperFlag.classList.toggle('active-flag', isFlagged);
      }
    }

    // Sync Navigator Chips
    updateNavigatorChipsState();

    // Trigger KaTeX Typesetting
    triggerKaTeX();
  }

  function getNormalizedOptions(question) {
    if (Array.isArray(question.options)) return question.options;
    if (typeof question.options === 'object' && question.options !== null) {
      return Object.entries(question.options).map(([k, v]) => ({ key: k, text: v }));
    }
    return [];
  }

  function getNormalizedStatements(question) {
    const raw = question.statements || question.tableStatements || [];
    return raw.map((item, idx) => {
      if (typeof item === 'string') {
        return { id: String(idx), text: item };
      }
      return {
        id: item.id !== undefined ? String(item.id) : String(idx),
        text: item.text || item.statement || '',
        answer: item.answer !== undefined ? item.answer : item.isCorrect,
        isCorrect: item.isCorrect
      };
    });
  }

  function getStatementCorrectAnswer(question, stmt) {
    const sid = stmt.id;
    if (question.correctAnswers && question.correctAnswers[sid] !== undefined) {
      const val = question.correctAnswers[sid];
      return val === true || val === 'B' || val === 'b' || val === 'true';
    }
    if (question.correctAnswer && typeof question.correctAnswer === 'object') {
      const val = question.correctAnswer[sid];
      return val === true || val === 'B' || val === 'b' || val === 'true';
    }
    if (stmt.answer !== undefined) {
      return stmt.answer === 'B' || stmt.answer === true || stmt.answer === 'b' || stmt.answer === 'true';
    }
    if (stmt.isCorrect !== undefined) {
      return stmt.isCorrect === true || stmt.isCorrect === 'true';
    }
    return false;
  }

  function renderOptions(question, qIndex) {
    els.paperOptionsList.innerHTML = '';
    const isReview = state.exam.isReviewMode;
    const isMatrix = question.type === 'matrix' || question.type === 'complex_table';
    const isMulti = question.type === 'multi' || question.type === 'multiple_response';

    if (isMatrix) {
      // 1. Benar / Salah Statement Table
      const tableWrapper = document.createElement('div');
      tableWrapper.className = 'matrix-table-wrapper';

      const table = document.createElement('table');
      table.className = 'matrix-table';
      table.innerHTML = `
        <thead>
          <tr>
            <th class="col-stmt">Pernyataan Evaluasi</th>
            <th class="col-opt">Benar</th>
            <th class="col-opt">Salah</th>
          </tr>
        </thead>
        <tbody></tbody>
      `;

      const tbody = table.querySelector('tbody');
      const ansObj = state.exam.answers[qIndex] || {};
      const stList = getNormalizedStatements(question);

      stList.forEach(stmt => {
        const tr = document.createElement('tr');
        const userChoice = ansObj[stmt.id]; // true | false | undefined
        const correctChoice = getStatementCorrectAnswer(question, stmt);

        let benarClasses = ['matrix-toggle-pill'];
        let salahClasses = ['matrix-toggle-pill'];

        if (userChoice === true) benarClasses.push('chosen');
        if (userChoice === false) salahClasses.push('chosen');

        if (isReview) {
          if (correctChoice === true) {
            benarClasses.push('correct-reveal');
          }
          if (correctChoice === false) {
            salahClasses.push('correct-reveal');
          }
          if (userChoice === true && correctChoice !== true) {
            benarClasses.push('wrong-choice');
          }
          if (userChoice === false && correctChoice !== false) {
            salahClasses.push('wrong-choice');
          }
        }

        tr.innerHTML = `
          <td class="col-stmt-text">${formatContentWithCode(stmt.text, true)}</td>
          <td class="col-opt-cell">
            <button type="button" class="${benarClasses.join(' ')}" data-stmt="${stmt.id}" data-val="true" ${isReview ? 'disabled' : ''}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Benar</span>
            </button>
          </td>
          <td class="col-opt-cell">
            <button type="button" class="${salahClasses.join(' ')}" data-stmt="${stmt.id}" data-val="false" ${isReview ? 'disabled' : ''}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
              <span>Salah</span>
            </button>
          </td>
        `;

        if (!isReview) {
          const btnB = tr.querySelector('button[data-val="true"]');
          const btnS = tr.querySelector('button[data-val="false"]');

          btnB.addEventListener('click', () => {
            state.exam.answers[qIndex] = state.exam.answers[qIndex] || {};
            state.exam.answers[qIndex][stmt.id] = true;
            renderOptions(question, qIndex);
            updateNavigatorChipsState();
          });

          btnS.addEventListener('click', () => {
            state.exam.answers[qIndex] = state.exam.answers[qIndex] || {};
            state.exam.answers[qIndex][stmt.id] = false;
            renderOptions(question, qIndex);
            updateNavigatorChipsState();
          });
        }

        tbody.appendChild(tr);
      });

      tableWrapper.appendChild(table);
      els.paperOptionsList.appendChild(tableWrapper);

    } else if (isMulti) {
      // 2. Multi-Select Complex Multiple Choice
      const selectedKeys = Array.isArray(state.exam.answers[qIndex]) ? state.exam.answers[qIndex] : [];
      const correctKeys = question.correctKeys || (Array.isArray(question.correctAnswer) ? question.correctAnswer : [question.correctAnswer || question.correctKey]);
      const opts = getNormalizedOptions(question);

      opts.forEach(opt => {
        const isSelected = selectedKeys.includes(opt.key);
        const btn = document.createElement('button');
        btn.type = 'button';

        let btnClasses = ['paper-opt-btn', 'multi-checkbox'];
        if (isSelected) btnClasses.push('selected');

        if (isReview) {
          btn.disabled = true;
          if (correctKeys.includes(opt.key)) {
            btnClasses.push('review-key-correct');
          }
          if (isSelected && !correctKeys.includes(opt.key)) {
            btnClasses.push('review-key-wrong');
          }
        }

        btn.className = btnClasses.join(' ');
        btn.innerHTML = `
          <span class="multi-check-indicator ${isSelected ? 'checked' : ''}">
            ${isSelected ? '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>' : ''}
          </span>
          <span class="p-opt-key">${opt.key}</span>
          <span class="p-opt-text">${formatContentWithCode(opt.text, true)}</span>
        `;

        if (!isReview) {
          btn.addEventListener('click', () => {
            let cur = Array.isArray(state.exam.answers[qIndex]) ? [...state.exam.answers[qIndex]] : [];
            if (cur.includes(opt.key)) {
              cur = cur.filter(k => k !== opt.key);
            } else {
              cur.push(opt.key);
              cur.sort();
            }
            state.exam.answers[qIndex] = cur;
            renderOptions(question, qIndex);
            updateNavigatorChipsState();
          });
        }

        els.paperOptionsList.appendChild(btn);
      });

    } else {
      // 3. Single Choice (Standard A–E)
      const selectedKey = state.exam.answers[qIndex];
      const correctKey = question.correctKey || question.correctAnswer;
      const opts = getNormalizedOptions(question);

      opts.forEach(opt => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `paper-opt-btn ${selectedKey === opt.key ? 'selected' : ''}`;

        if (isReview) {
          btn.disabled = true;
          if (opt.key === correctKey) {
            btn.style.borderColor = 'var(--accent-emerald)';
            btn.style.background = 'rgba(16, 185, 129, 0.16)';
          } else if (selectedKey === opt.key && opt.key !== correctKey) {
            btn.style.borderColor = 'var(--accent-crimson)';
            btn.style.background = 'rgba(244, 63, 94, 0.16)';
          }
        }

        btn.innerHTML = `
          <span class="p-opt-key">${opt.key}</span>
          <span class="p-opt-text">${formatContentWithCode(opt.text, true)}</span>
        `;

        if (!isReview) {
          btn.addEventListener('click', () => {
            state.exam.answers[qIndex] = opt.key;
            renderOptions(question, qIndex);
            updateNavigatorChipsState();
          });
        }

        els.paperOptionsList.appendChild(btn);
      });
    }

    triggerKaTeX();
  }

  let katexRetryCount = 0;
  const MAX_KATEX_RETRIES = 25; // Extended retry window for mobile networks

  function triggerKaTeX() {
    if (!window.renderMathInElement) {
      if (katexRetryCount < MAX_KATEX_RETRIES) {
        katexRetryCount++;
        setTimeout(triggerKaTeX, 150);
      }
      return;
    }
    katexRetryCount = 0;

    const mathOptions = {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false }
      ],
      ignoredClasses: ["code-snippet-box", "code-pre", "code-content", "inline-code"],
      ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
      throwOnError: false,
      errorColor: '#ef4444'
    };

    const safeMathRender = (elem) => {
      if (!elem) return;
      try {
        window.renderMathInElement(elem, mathOptions);
      } catch (err) {
        console.warn('KaTeX render warning:', err);
      }
    };

    safeMathRender(els.paperQText);
    safeMathRender(els.paperOptionsList);

    if (els.formulaHudContent) safeMathRender(els.formulaHudContent);
    if (els.solutionBodyContent) safeMathRender(els.solutionBodyContent);
    if (els.clue1Body) safeMathRender(els.clue1Body);
    if (els.clue2Body) safeMathRender(els.clue2Body);
  }

  // =========================================================================
  // IN-APP MODAL HELPER (ZERO WINDOW.BLUR LOCKS)
  // =========================================================================
  // =========================================================================
  // IN-APP MODAL HELPER (ZERO WINDOW.BLUR LOCKS & GUARANTEED DISPLAY)
  // =========================================================================
  function showAppConfirm({ title, message, okText = 'Ya, Kumpulkan Ujian', cancelText = 'Periksa Kembali', onOk, onCancel }) {
    state.isModalOpen = true;
    if (els.appConfirmTitle) els.appConfirmTitle.textContent = title;
    if (els.appConfirmMessage) els.appConfirmMessage.textContent = message;

    if (els.btnAppConfirmOk) {
      const span = els.btnAppConfirmOk.querySelector('span');
      if (span) span.textContent = okText;
      else els.btnAppConfirmOk.textContent = okText;
    }
    if (els.btnAppConfirmCancel) {
      const span = els.btnAppConfirmCancel.querySelector('span');
      if (span) span.textContent = cancelText;
      else els.btnAppConfirmCancel.textContent = cancelText;
    }

    const cleanup = () => {
      state.isModalOpen = false;
      if (els.appConfirmModal) {
        els.appConfirmModal.classList.add('hidden');
        els.appConfirmModal.style.display = 'none'; // Overcome inline style fallback!
      }
      if (els.btnAppConfirmOk) els.btnAppConfirmOk.onclick = null;
      if (els.btnAppConfirmCancel) els.btnAppConfirmCancel.onclick = null;
    };

    if (els.btnAppConfirmOk) {
      els.btnAppConfirmOk.onclick = () => {
        cleanup();
        if (onOk) onOk();
      };
    }

    if (els.btnAppConfirmCancel) {
      els.btnAppConfirmCancel.onclick = () => {
        cleanup();
        if (onCancel) onCancel();
      };
    }

    if (els.appConfirmModal) {
      els.appConfirmModal.classList.remove('hidden');
      els.appConfirmModal.style.display = 'flex'; // Explicit flex display!
    }
  }

  function promptSubmitExam() {
    if (state.exam.isReviewMode) return; // Never submit in review mode

    let answeredCount = 0;
    let flaggedCount = 0;
    const unansweredIndices = [];

    state.exam.questions.forEach((q, idx) => {
      const ans = state.exam.answers[idx];
      const hasAnswered = isQuestionAnswered(q, ans);

      if (hasAnswered) answeredCount++;
      else unansweredIndices.push(idx + 1);

      if (state.exam.flags && state.exam.flags[idx]) {
        flaggedCount++;
      }
    });

    const total = state.exam.questions.length;
    const unAnswered = total - answeredCount;

    // Populate Audit Metric Counters
    if (els.auditCountAnswered) els.auditCountAnswered.textContent = answeredCount;
    if (els.auditCountFlagged) els.auditCountFlagged.textContent = flaggedCount;
    if (els.auditCountEmpty) els.auditCountEmpty.textContent = unAnswered;

    // Handle Dynamic Warning Box
    if (els.auditWarningBox) {
      if (unAnswered > 0) {
        els.auditWarningBox.classList.remove('hidden');
        if (els.auditWarningText) {
          els.auditWarningText.innerHTML = `<strong>Peringatan Penting:</strong> Masih terdapat <strong>${unAnswered}</strong> butir soal yang belum diisi (Nomor: <strong>${unansweredIndices.join(', ')}</strong>). Pastikan seluruh lembar jawaban sebelum pengumpulan final.`;
        }
      } else if (flaggedCount > 0) {
        els.auditWarningBox.classList.remove('hidden');
        if (els.auditWarningText) {
          els.auditWarningText.innerHTML = `<strong>Catatan:</strong> Masih terdapat <strong>${flaggedCount}</strong> nomor yang ditandai <strong>Ragu-Ragu</strong>. Anda dapat meninjau kembali pilihan jawaban sekarang.`;
        }
      } else {
        els.auditWarningBox.classList.add('hidden');
      }
    }

    // Populate Interactive Pre-Submission Audit Chips Map
    if (els.auditChipsGrid) {
      els.auditChipsGrid.innerHTML = '';
      state.exam.questions.forEach((q, idx) => {
        const chip = document.createElement('button');
        chip.type = 'button';
        const ans = state.exam.answers[idx];
        const hasAns = isQuestionAnswered(q, ans);
        const isFlagged = !!(state.exam.flags && state.exam.flags[idx]);

        let chipClass = 'audit-chip-item';
        if (isFlagged) chipClass += ' flagged';
        else if (hasAns) chipClass += ' answered';
        else chipClass += ' empty';

        chip.className = chipClass;
        chip.textContent = String(idx + 1).padStart(2, '0');
        chip.title = `Soal ${idx + 1}: ${isFlagged ? 'Ragu-Ragu' : (hasAns ? 'Sudah Terjawab' : 'Belum Diisi')} (Klik untuk loncat)`;

        chip.addEventListener('click', () => {
          // Close audit modal and immediately jump to this question
          if (els.appConfirmModal) {
            els.appConfirmModal.classList.add('hidden');
            els.appConfirmModal.style.display = 'none';
          }
          state.isModalOpen = false;
          renderQuestion(idx);
        });

        els.auditChipsGrid.appendChild(chip);
      });
    }

    const confirmMsg = `Pastikan seluruh lembar jawaban Anda telah diperiksa. Setelah dikumpulkan, sesi ujian resmi akan ditutup dan nilai dihitung secara permanen.`;

    showAppConfirm({
      title: 'Rekapitulasi Lembar Jawaban',
      message: confirmMsg,
      okText: 'Ya, Kumpulkan Ujian',
      cancelText: 'Periksa Kembali',
      onOk: () => {
        closeGridDrawer();
        if (document.fullscreenElement && document.exitFullscreen) {
          document.exitFullscreen().catch(() => {});
        }
        finishExam();
      }
    });
  }

  // =========================================================================
  // WORKSPACE NAVIGATION & ZERO-FRICTION CONTROLS
  // =========================================================================
  function initWorkspaceNavigation() {
    // Zero-friction Back button with In-App Confirm (No Window.Blur)
    els.btnQuitSession.addEventListener('click', () => {
      state.exam.isReviewMode = false;
      if (state.sessionMode === 'simulasi' && !state.exam.isFinished) {
        showAppConfirm({
          title: 'Batalkan Simulasi?',
          message: 'Keluar sekarang akan membatalkan sesi ujian simulasi dan tidak menyimpan skor. Yakin ingin keluar?',
          okText: 'Ya, Keluar',
          cancelText: 'Tetap Lanjut',
          onOk: () => {
            stopTimer();
            if (document.fullscreenElement && document.exitFullscreen) {
              document.exitFullscreen().catch(() => {});
            }
            navigateTo('subject', state.currentSubject);
          }
        });
        return;
      }

      stopTimer();
      if (state.sessionMode === 'diagnostik') {
        navigateTo('home');
      } else {
        navigateTo('subject', state.currentSubject);
      }
    });

    // Prev Button
    els.btnPaperPrev.addEventListener('click', () => {
      if (state.exam.currentIndex > 0) {
        renderQuestion(state.exam.currentIndex - 1);
      }
    });

    // Flag (Ragu-Ragu) Button Toggle
    if (els.btnPaperFlag) {
      els.btnPaperFlag.addEventListener('click', () => {
        if (state.exam.isReviewMode) return;
        const idx = state.exam.currentIndex;
        if (!state.exam.flags) state.exam.flags = {};
        state.exam.flags[idx] = !state.exam.flags[idx];
        els.btnPaperFlag.classList.toggle('active-flag', !!state.exam.flags[idx]);
        updateNavigatorChipsState();
      });
    }

    // Next Button
    els.btnPaperNext.addEventListener('click', () => {
      if (state.exam.currentIndex < state.exam.questions.length - 1) {
        renderQuestion(state.exam.currentIndex + 1);
      }
    });

    // Review Mode: Return to Results Dashboard (No False Re-submission!)
    if (els.btnReviewBackResults) {
      els.btnReviewBackResults.addEventListener('click', () => {
        navigateTo('results');
      });
    }

    // Normal Submit Buttons (Bottom Footer + Right Sidebar + Mobile Drawer)
    els.btnPaperSubmit.addEventListener('click', promptSubmitExam);
    if (els.btnCbtSidebarSubmit) {
      els.btnCbtSidebarSubmit.addEventListener('click', promptSubmitExam);
    }
    if (els.btnGridDrawerSubmit) {
      els.btnGridDrawerSubmit.addEventListener('click', promptSubmitExam);
    }

    // Fullscreen Toggle Button (F11 Workaround with strictly accurate state)
    if (els.btnToggleFullscreen) {
      els.btnToggleFullscreen.addEventListener('click', () => {
        const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement);
        if (!isFs) {
          const reqFs = document.documentElement.requestFullscreen || document.documentElement.webkitRequestFullscreen;
          if (reqFs && typeof reqFs === 'function') {
            reqFs.call(document.documentElement).catch(err => {
              console.warn('Fullscreen denied:', err);
              syncFullscreenButtonState();
            });
          }
        } else {
          const exitFs = document.exitFullscreen || document.webkitExitFullscreen;
          if (exitFs && typeof exitFs === 'function') {
            exitFs.call(document).catch(err => {
              console.warn('Exit fullscreen error:', err);
              syncFullscreenButtonState();
            });
          }
        }
      });
    }

    document.addEventListener('fullscreenchange', syncFullscreenButtonState);
    document.addEventListener('webkitfullscreenchange', syncFullscreenButtonState);

    // Scaffolding Drawer Toggles (Apple HIG Inline Accordion with Anime.js)
    if (els.btnToggleFormulaHud) {
      els.btnToggleFormulaHud.addEventListener('click', () => {
        toggleAccordionItem(els.scaffoldItemFormula, els.drawerFormulaHud, els.btnToggleFormulaHud, els.formulaStatusPill);
      });
    }

    if (els.btnToggleClue1) {
      els.btnToggleClue1.addEventListener('click', () => {
        toggleAccordionItem(els.scaffoldItemClue1, els.drawerClue1, els.btnToggleClue1, els.clue1StatusPill);
      });
    }

    if (els.btnToggleClue2) {
      els.btnToggleClue2.addEventListener('click', () => {
        toggleAccordionItem(els.scaffoldItemClue2, els.drawerClue2, els.btnToggleClue2, els.clue2StatusPill);
      });
    }

    if (els.btnToggleSolution) {
      els.btnToggleSolution.addEventListener('click', () => {
        toggleAccordionItem(els.scaffoldItemSolution, els.drawerSolution, els.btnToggleSolution, els.solutionStatusPill);
      });
    }

    // Question Number Navigator Grid (Mobile Drawer fallback)
    els.btnOpenGridDrawer.addEventListener('click', openGridDrawer);
    els.btnCloseGridDrawer.addEventListener('click', closeGridDrawer);
    els.gridDrawerOverlay.addEventListener('click', (e) => {
      if (e.target === els.gridDrawerOverlay) closeGridDrawer();
    });
  }

  function openGridDrawer() {
    els.gridNumbersContainer.innerHTML = '';
    state.exam.questions.forEach((q, idx) => {
      const chip = document.createElement('button');
      const isAnswered = (state.exam.answers[idx] !== undefined);
      const isActive = (idx === state.exam.currentIndex);

      chip.className = `grid-chip-item ${isActive ? 'active' : ''} ${isAnswered ? 'answered' : ''}`;
      chip.textContent = String(idx + 1).padStart(2, '0');

      chip.addEventListener('click', () => {
        closeGridDrawer();
        renderQuestion(idx);
      });

      els.gridNumbersContainer.appendChild(chip);
    });

    els.gridDrawerOverlay.classList.remove('hidden');
  }

  function closeGridDrawer() {
    els.gridDrawerOverlay.classList.add('hidden');
  }

  // =========================================================================
  // STRICT 3-STRIKE PROCTORING ENGINE (SIMULATION ONLY)
  // =========================================================================
  function triggerProctorViolation(reason) {
    if (state.currentView !== 'workspace' || state.sessionMode !== 'simulasi' || state.exam.isFinished) return;

    state.exam.strikes += 1;
    updateStrikeDots(state.exam.strikes);
    pauseTimer();

    els.proctorStrikeCount.textContent = `STRIKE ${state.exam.strikes} DARI ${state.exam.maxStrikes}`;
    els.proctorMessageText.textContent = `Terdeteksi: ${reason}. Fokus layar hilang. Ujian TKA menuntut integritas dan pengawasan konsentrasi penuh.`;

    els.proctorModal.classList.remove('hidden');

    if (state.exam.strikes >= state.exam.maxStrikes) {
      els.proctorMessageText.textContent = `BATAS MAKSIMUM 3 STRIKE TERLAMPAUI! Sesi ujian Anda otomatis dikumpulkan demi integritas skor.`;
      setTimeout(() => {
        els.proctorModal.classList.add('hidden');
        finishExam();
      }, 2400);
    }
  }

  function updateStrikeDots(count) {
    els.strikeDots.forEach((dot, idx) => {
      if (idx < count) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }

  function initProctorListeners() {
    document.addEventListener('visibilitychange', () => {
      if (state.isModalOpen) return;
      if (document.hidden && state.sessionMode === 'simulasi') {
        triggerProctorViolation('Pindah tab browser atau jendela diminimalkan');
      }
    });

    window.addEventListener('blur', () => {
      if (state.isModalOpen) return;
      if (state.sessionMode === 'simulasi') {
        triggerProctorViolation('Jendela browser kehilangan fokus');
      }
    });

    els.btnProctorResume.addEventListener('click', () => {
      els.proctorModal.classList.add('hidden');
      resumeTimer();
      if (document.documentElement.requestFullscreen) {
        document.documentElement.requestFullscreen().catch(() => {});
      }
    });
  }

  // =========================================================================
  // COUNTDOWN TIMER ENGINE
  // =========================================================================
  function startTimer(totalSeconds) {
    stopTimer();
    state.exam.remainingSeconds = totalSeconds;
    updateTimerDisplay();

    state.exam.timerInterval = setInterval(() => {
      if (state.exam.isTimerPaused) return;

      state.exam.remainingSeconds -= 1;
      updateTimerDisplay();

      if (state.exam.remainingSeconds <= 0) {
        stopTimer();
        finishExam();
      }
    }, 1000);
  }

  function pauseTimer() { state.exam.isTimerPaused = true; }
  function resumeTimer() { state.exam.isTimerPaused = false; }

  function stopTimer() {
    if (state.exam.timerInterval) {
      clearInterval(state.exam.timerInterval);
      state.exam.timerInterval = null;
    }
  }

  function updateTimerDisplay() {
    const mins = Math.floor(state.exam.remainingSeconds / 60);
    const secs = state.exam.remainingSeconds % 60;
    els.hudTimerDigits.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }

  // =========================================================================
  // EXAM COMPLETION & DIAGNOSTIC RESULTS EVALUATION
  // =========================================================================
  function finishExam() {
    stopTimer();
    document.body.classList.remove('session-mode-simulasi');
    state.exam.isFinished = true;

    let correct = 0;
    let wrong = 0;
    const total = state.exam.questions.length;

    let mtkCorrect = 0, mtkTotal = 0;
    let indCorrect = 0, indTotal = 0;
    let engCorrect = 0, engTotal = 0;

    state.exam.questions.forEach((q, idx) => {
      const ans = state.exam.answers[idx];
      const isCorrect = checkQuestionCorrectness(q, ans);
      if (isCorrect) correct++;
      else wrong++;

      const subj = q.subject || state.currentSubject;
      if (subj === 'mtk') { mtkTotal++; if (isCorrect) mtkCorrect++; }
      else if (subj === 'ind') { indTotal++; if (isCorrect) indCorrect++; }
      else if (subj === 'eng') { engTotal++; if (isCorrect) engCorrect++; }
    });

    const score = ((correct / total) * 100).toFixed(1);
    const timeSpent = Math.max(1, Math.round((Date.now() - state.exam.startTime) / 1000));
    const mins = Math.floor(timeSpent / 60);
    const secs = timeSpent % 60;
    const pace = (timeSpent / total).toFixed(1);

    els.reportScore.textContent = score;
    els.reportTitle.textContent = score >= 75 ? 'Pencapaian Sangat Baik!' : 'Perlu Evaluasi Konseptual';

    const mtkPct = mtkTotal > 0 ? Math.round((mtkCorrect / mtkTotal) * 100) : 0;
    const indPct = indTotal > 0 ? Math.round((indCorrect / indTotal) * 100) : 0;
    const engPct = engTotal > 0 ? Math.round((engCorrect / engTotal) * 100) : 0;

    if (state.sessionMode === 'diagnostik') {
      els.reportSubtitle.textContent = `Menjawab benar ${correct} dari ${total} butir soal diagnostik 3 Mata Pelajaran.`;

      if (els.diagnosticEvaluationBox) {
        els.diagnosticEvaluationBox.classList.remove('hidden');

        if (els.diagMtkScore) els.diagMtkScore.textContent = `${mtkCorrect}/${mtkTotal} (${mtkPct}%)`;
        if (els.diagIndScore) els.diagIndScore.textContent = `${indCorrect}/${indTotal} (${indPct}%)`;
        if (els.diagEngScore) els.diagEngScore.textContent = `${engCorrect}/${engTotal} (${engPct}%)`;

        function getStatusMeta(pct) {
          if (pct < 60) return { text: 'Prioritas Utama', cls: 'priority' };
          if (pct < 80) return { text: 'Perlu Latihan', cls: 'fair' };
          return { text: 'Kompeten', cls: 'good' };
        }

        const mtkMeta = getStatusMeta(mtkPct);
        const indMeta = getStatusMeta(indPct);
        const engMeta = getStatusMeta(engPct);

        if (els.diagMtkStatus) { els.diagMtkStatus.textContent = mtkMeta.text; els.diagMtkStatus.className = `d-sub-status ${mtkMeta.cls}`; }
        if (els.diagIndStatus) { els.diagIndStatus.textContent = indMeta.text; els.diagIndStatus.className = `d-sub-status ${indMeta.cls}`; }
        if (els.diagEngStatus) { els.diagEngStatus.textContent = engMeta.text; els.diagEngStatus.className = `d-sub-status ${engMeta.cls}`; }

        function renderSubjectTopicChips(container, subKey) {
          if (!container) return;
          container.innerHTML = '';
          const subQuestions = state.exam.questions
            .map((q, idx) => ({ q, idx, isCorrect: checkQuestionCorrectness(q, state.exam.answers[idx]) }))
            .filter(item => (item.q.subject || state.currentSubject) === subKey);

          subQuestions.forEach(item => {
            const chip = document.createElement('div');
            chip.className = `diag-topic-chip ${item.isCorrect ? 'correct' : 'wrong'}`;
            chip.innerHTML = `
              <span class="chip-topic-name">${item.q.topic}</span>
              <span class="chip-status-icon">${item.isCorrect ? '✓' : '✗'}</span>
            `;
            container.appendChild(chip);
          });
        }

        renderSubjectTopicChips(els.diagMtkTopicList, 'mtk');
        renderSubjectTopicChips(els.diagIndTopicList, 'ind');
        renderSubjectTopicChips(els.diagEngTopicList, 'eng');
      }
    } else {
      els.reportSubtitle.textContent = `Menjawab benar ${correct} dari ${total} butir soal ${state.currentSubject.toUpperCase()}.`;
      if (els.diagnosticEvaluationBox) {
        els.diagnosticEvaluationBox.classList.add('hidden');
      }
    }

    // Render Actionable Priority Learning Cards into #priorityCardsList
    if (els.priorityCardsList) {
      els.priorityCardsList.innerHTML = '';

      let priorityData = [];
      if (state.sessionMode === 'diagnostik') {
        function getSubjectWrongTopics(subKey) {
          return state.exam.questions
            .filter((q, idx) => (q.subject || state.currentSubject) === subKey && !checkQuestionCorrectness(q, state.exam.answers[idx]))
            .map(q => q.topic);
        }

        const mtkWrongs = getSubjectWrongTopics('mtk');
        const indWrongs = getSubjectWrongTopics('ind');
        const engWrongs = getSubjectWrongTopics('eng');

        const formatFocusTopics = (wrongs) => {
          if (wrongs.length === 0) return 'Penguasaan 100% pada semua pilar uji diagnostik. Pertahankan konsistensi & pace penalaran.';
          return 'Topik yang teridentifikasi butuh penguatan: ' + wrongs.join(', ');
        };

        priorityData = [
          {
            key: 'mtk',
            name: 'Matematika',
            scorePct: mtkPct,
            topics: formatFocusTopics(mtkWrongs),
            actionText: 'Buka Training Lab Matematika',
            tag: mtkPct < 60 ? 'Prioritas 1: Kritis' : (mtkPct < 80 ? 'Prioritas 2: Perlu Penguatan' : 'Prioritas 3: Pemantapan')
          },
          {
            key: 'ind',
            name: 'Bahasa Indonesia',
            scorePct: indPct,
            topics: formatFocusTopics(indWrongs),
            actionText: 'Buka Training Lab B. Indonesia',
            tag: indPct < 60 ? 'Prioritas 1: Kritis' : (indPct < 80 ? 'Prioritas 2: Perlu Penguatan' : 'Prioritas 3: Pemantapan')
          },
          {
            key: 'eng',
            name: 'Bahasa Inggris',
            scorePct: engPct,
            topics: formatFocusTopics(engWrongs),
            actionText: 'Buka Training Lab B. Inggris',
            tag: engPct < 60 ? 'Prioritas 1: Kritis' : (engPct < 80 ? 'Prioritas 2: Perlu Penguatan' : 'Prioritas 3: Pemantapan')
          }
        ].sort((a, b) => a.scorePct - b.scorePct);
      } else {
        const subjKey = state.currentSubject;
        const subjInfo = window.TKA_DATABASE?.[subjKey] || { title: 'Mata Pelajaran' };
        const scorePct = Math.round((correct / total) * 100);
        priorityData = [
          {
            key: subjKey,
            name: subjInfo.title || 'Mata Pelajaran',
            scorePct: scorePct,
            topics: 'Review dan evaluasi mendalam pada butir soal yang keliru',
            actionText: `Latih Ulang ${subjInfo.title}`,
            tag: scorePct < 60 ? 'Prioritas 1: Kritis' : (scorePct < 80 ? 'Prioritas 2: Perlu Penguatan' : 'Prioritas 3: Pemantapan')
          }
        ];
      }

      priorityData.forEach(item => {
        const card = document.createElement('div');
        card.className = `priority-card-item ${item.key}`;
        card.innerHTML = `
          <div class="priority-card-header">
            <div class="priority-card-title-group">
              <span class="priority-subject-tag ${item.key}">${item.name}</span>
              <span class="priority-urgency-badge ${item.scorePct < 60 ? 'urgent' : (item.scorePct < 80 ? 'medium' : 'good')}">
                ${item.tag}
              </span>
            </div>
            <span class="priority-score-pill">${item.scorePct}% Akurasi</span>
          </div>
          <p class="priority-card-desc">
            Fokus esensial materi: <strong>${item.topics}</strong>. Rekonstruksi pola penalaran bertahap dengan scaffolding teori tanpa batas waktu.
          </p>
          <div class="priority-card-action">
            <button class="btn-priority-launch ${item.key}" data-subject="${item.key}">
              <span>${item.actionText}</span>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
          </div>
        `;

        const launchBtn = card.querySelector('.btn-priority-launch');
        if (launchBtn) {
          launchBtn.addEventListener('click', () => {
            state.exam.isReviewMode = false;
            navigateTo('subject', item.key);
          });
        }

        els.priorityCardsList.appendChild(card);
      });
    }

    els.reportCorrect.textContent = correct;
    els.reportWrong.textContent = wrong;
    els.reportTime.textContent = `${mins}m ${secs}s`;
    els.reportPace.textContent = `${pace} dtk`;

    const exitFs = document.exitFullscreen || document.webkitExitFullscreen;
    if (exitFs && typeof exitFs === 'function') {
      exitFs.call(document).catch(() => {});
    }

    navigateTo('results');
  }

  function initResultsListeners() {
    els.btnReportReview.addEventListener('click', () => {
      state.exam.isReviewMode = true;
      navigateTo('workspace');
      renderQuestion(0);
    });

    els.btnReportReturn.addEventListener('click', () => {
      state.exam.isReviewMode = false;
      if (state.sessionMode === 'diagnostik') {
        navigateTo('home');
      } else {
        navigateTo('subject', state.currentSubject);
      }
    });
  }

  // =========================================================================
  // BOOTSTRAP INITIALIZATION
  // =========================================================================
  function initApp() {
    initNavbar();
    renderHomeDeck();
    initHomeListeners();
    initMobilePanorama();
    initSubjectHubListeners();
    initWorkspaceNavigation();
    initProctorListeners();
    initResultsListeners();

    // Default to Home View
    navigateTo('home');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
  } else {
    initApp();
  }

})();
