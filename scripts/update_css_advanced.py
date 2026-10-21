"""
Append CSS tokens and styles for advanced subjects to style.css
"""
import os

style_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "style.css")

with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add CSS variables under :root
var_anchor = "  --eng-accent: #fbbf24;"
var_addon = """  --eng-accent: #fbbf24;

  /* 4. Matematika Lanjutan (Electric Cyan) */
  --mtk_lanjut-bg: rgba(8, 28, 36, 0.78);
  --mtk_lanjut-border: 2.5px solid #0891b2;
  --mtk_lanjut-top-bar: #06b6d4;
  --mtk_lanjut-shadow: 6px 6px 0px #000000;
  --mtk_lanjut-accent: #22d3ee;

  /* 5. Bahasa Indonesia Lanjutan (Teal Sage) */
  --ind_lanjut-bg: rgba(10, 29, 27, 0.78);
  --ind_lanjut-border: 2.5px solid #0d9488;
  --ind_lanjut-top-bar: #14b8a6;
  --ind_lanjut-shadow: 6px 6px 0px #000000;
  --ind_lanjut-accent: #2dd4bf;

  /* 6. Bahasa Inggris Lanjutan (Cyber Violet) */
  --eng_lanjut-bg: rgba(26, 14, 38, 0.78);
  --eng_lanjut-border: 2.5px solid #9333ea;
  --eng_lanjut-top-bar: #a855f7;
  --eng_lanjut-shadow: 6px 6px 0px #000000;
  --eng_lanjut-accent: #c084fc;"""

if var_anchor in css:
    css = css.replace(var_anchor, var_addon)
    print("Added CSS variables.")

# Add theme card rules
card_styles = """
/* =========================================================================
   ADVANCED SUBJECTS (MATEMATIKA, INDONESIA, INGGRIS LANJUTAN)
   ========================================================================= */
.neo-deck-card.mtk_lanjut {
  background: var(--mtk_lanjut-bg);
  border: var(--mtk_lanjut-border);
  border-top: 5px solid var(--mtk_lanjut-top-bar);
  box-shadow: var(--mtk_lanjut-shadow);
}
.neo-deck-card.mtk_lanjut:hover {
  box-shadow: 10px 10px 0px #000000;
  border-color: #22d3ee;
}
.card-subject-tag.mtk_lanjut {
  background: rgba(6, 182, 212, 0.2);
  color: #22d3ee;
  border: 1px solid rgba(6, 182, 212, 0.45);
}
.btn-card-enter.mtk_lanjut {
  background: linear-gradient(135deg, #0891b2, #06b6d4);
  color: #ffffff;
}

.neo-deck-card.ind_lanjut {
  background: var(--ind_lanjut-bg);
  border: var(--ind_lanjut-border);
  border-top: 5px solid var(--ind_lanjut-top-bar);
  box-shadow: var(--ind_lanjut-shadow);
}
.neo-deck-card.ind_lanjut:hover {
  box-shadow: 10px 10px 0px #000000;
  border-color: #2dd4bf;
}
.card-subject-tag.ind_lanjut {
  background: rgba(20, 184, 166, 0.2);
  color: #2dd4bf;
  border: 1px solid rgba(20, 184, 166, 0.45);
}
.btn-card-enter.ind_lanjut {
  background: linear-gradient(135deg, #0d9488, #14b8a6);
  color: #ffffff;
}

.neo-deck-card.eng_lanjut {
  background: var(--eng_lanjut-bg);
  border: var(--eng_lanjut-border);
  border-top: 5px solid var(--eng_lanjut-top-bar);
  box-shadow: var(--eng_lanjut-shadow);
}
.neo-deck-card.eng_lanjut:hover {
  box-shadow: 10px 10px 0px #000000;
  border-color: #c084fc;
}
.card-subject-tag.eng_lanjut {
  background: rgba(168, 85, 247, 0.2);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.45);
}
.btn-card-enter.eng_lanjut {
  background: linear-gradient(135deg, #7e22ce, #a855f7);
  color: #ffffff;
}

/* Deck Group Switcher Tabs */
.deck-group-switcher {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin: 0 auto 20px auto;
  max-width: 500px;
  padding: 4px;
  background: rgba(15, 23, 42, 0.85);
  border: 1.5px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-pill);
}
.btn-group-tab {
  flex: 1;
  padding: 8px 16px;
  border-radius: var(--radius-pill);
  border: none;
  background: transparent;
  color: #94a3b8;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.2s ease;
}
.btn-group-tab.active {
  background: #3b82f6;
  color: #ffffff;
  box-shadow: 0 0 12px rgba(59, 130, 246, 0.5);
}
"""

css += card_styles

with open(style_path, "w", encoding="utf-8") as f:
    f.write(css)

print("style.css updated with advanced subjects styles.")
