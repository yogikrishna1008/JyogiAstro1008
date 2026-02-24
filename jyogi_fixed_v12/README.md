# 🔮 Jyogi AI — Vedic Astrology & Tarot

A production-ready Streamlit app combining Vedic Astrology, Tarot Reading, and a Crystal Shop.

## Architecture
```
jyogi_app/
├── app.py                        ← Main controller (run this)
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── secrets.toml.example      ← Copy to secrets.toml, add your key
└── jyogi/                        ← Package
    ├── config.py                 ← Constants + AI system prompts
    ├── calc_engine.py            ← Swiss Ephemeris (Sidereal Lahiri)
    ├── numerology.py             ← Life Path calculation
    ├── tarot_deck.py             ← Full 78-card Rider-Waite deck
    ├── inventory.py              ← Shop products & reviews
    ├── clients/
    │   └── ai.py                 ← OpenAI client (cached)
    ├── engines/
    │   └── rules_engine.py       ← Lagna lord, Dasha parsing
    ├── pipelines/
    │   ├── astrology.py          ← Full Vedic report generation
    │   └── tarot.py              ← Tarot report + AI interpretation
    ├── reports/
    │   └── pdf_writer.py         ← ReportLab PDF generator
    └── services/
        ├── cities.py             ← City coordinates + session state
        ├── geocode.py            ← Nominatim geocoding (cached)
        └── shop.py               ← Shop/Offerings UI page
```

## Local Setup

```bash
# 1. Clone and navigate
git clone https://github.com/YOUR_USERNAME/jyogi-app.git
cd jyogi-app

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate          # Mac/Linux
# venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Add your OpenAI API key
mkdir -p .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit secrets.toml and add your real key

# 5. Run
streamlit run app.py
```

## Streamlit Cloud Deployment

1. Push to GitHub (private repo is fine)
2. Go to share.streamlit.io → New App → Select repo
3. Main file: `app.py`
4. In Settings → Secrets, add:
   ```
   OPENAI_API_KEY = "sk-proj-..."
   ```

## Key Technical Notes

- **Zodiac system:** Sidereal / Lahiri Ayanamsa (NOT tropical)
- **Sadhe Sati:** Calculated from transit Saturn vs natal Moon (real-time)
- **Tarot reversals:** Treated as internal blocks, not bad luck
- **AI model:** Fine-tuned `ft:gpt-4o-mini-2024-07-18:personal:jyogi-v1:D01bAaRr`
- **Tarot deck:** Full 78 cards (22 Major + 56 Minor Arcana)

## What's Local-Only (Never Push to GitHub)

| File | Reason |
|------|--------|
| `.streamlit/secrets.toml` | Contains API key |
| `venv/` | Local Python environment |
| `__pycache__/` | Python cache |
| `*.pdf` | Generated test reports |

## Future Enhancements

- [ ] Upload your own Canva logo → `images/logo.png` → add to header
- [ ] Upload Rider-Waite card images → `cards/` folder
- [ ] WhatsApp/Razorpay order integration for shop
- [ ] Client history database (SQLite)
- [ ] React frontend + FastAPI backend (Phase 2)
