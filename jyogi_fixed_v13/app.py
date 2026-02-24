"""
Jyogi AI — Main Application
Vedic Astrology · Tarot Reading · Sacred Offerings

Run locally:
    streamlit run app.py
"""
import datetime as dt
import time

import streamlit as st

# ── Page config (must be first Streamlit call) ─────────────────────────────
st.set_page_config(
    page_title="Jyogi AI — Vedic Astro & Tarot",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Global ── */
.stApp {
    background: radial-gradient(ellipse at top, #1b2340 0%, #0d1117 60%);
    color: #e8e0d0;
    font-family: 'Inter', sans-serif;
}

/* ── Hero Banner ── */
.jyogi-hero {
    text-align: center;
    padding: 2.5rem 2rem 2rem;
    background: linear-gradient(135deg, #1a3a08 0%, #2B7A0B 40%, #c9910a 85%, #FFC340 100%);
    border-radius: 18px;
    margin-bottom: 2rem;
    box-shadow: 0 8px 40px rgba(255,195,64,0.20), 0 2px 10px rgba(0,0,0,0.6);
    border: 1px solid rgba(255,195,64,0.25);
}
.jyogi-hero h1 {
    font-family: 'Cinzel', serif !important;
    font-size: 3.2rem;
    font-weight: 700;
    color: #fff !important;
    margin: 0 0 0.3rem 0;
    text-shadow: 0 2px 12px rgba(0,0,0,0.5);
    letter-spacing: 3px;
}
.jyogi-hero .tagline {
    color: #ffe9a0;
    font-size: 1.05rem;
    letter-spacing: 1.5px;
    margin: 0.2rem 0;
}
.jyogi-hero .sub {
    color: rgba(255,233,160,0.7);
    font-size: 0.82rem;
    font-style: italic;
    margin-top: 0.5rem;
}

/* ── Section headings ── */
h1, h2, h3 { 
    font-family: 'Cinzel', serif !important;
    color: #FFC340 !important; 
}

/* ── Location box ── */
.loc-box {
    background: rgba(255,195,64,0.05);
    border: 1px solid rgba(255,195,64,0.2);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
}
.loc-badge {
    display: inline-block;
    background: rgba(43,122,11,0.3);
    border: 1px solid rgba(43,122,11,0.6);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.82rem;
    color: #90ee90;
    margin-top: 6px;
}

/* ── Gold primary buttons ── */
div.stButton > button {
    background: linear-gradient(90deg, #FFC340 0%, #e6a200 100%);
    color: #1a1200;
    font-weight: 700;
    border: none;
    border-radius: 24px;
    padding: 0.6rem 1.6rem;
    transition: all 0.25s ease;
    letter-spacing: 0.5px;
    font-size: 0.95rem;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(255,195,64,0.45);
}

/* ── Form submit (green) ── */
div.stFormSubmitButton > button {
    background: linear-gradient(90deg, #2B7A0B 0%, #3d9e12 100%) !important;
    color: #fff !important;
    font-weight: 700;
    border: none !important;
    border-radius: 24px !important;
    padding: 0.65rem 2rem !important;
    width: 100%;
    font-size: 1rem;
    letter-spacing: 0.5px;
    transition: all 0.25s ease;
}
div.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 22px rgba(43,122,11,0.45);
}

/* ── Inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div,
.stDateInput > div > div > input,
.stTimeInput > div > div > input,
.stNumberInput > div > div > input {
    background-color: rgba(15, 20, 35, 0.85) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,195,64,0.35) !important;
    border-radius: 10px !important;
    caret-color: #FFC340 !important;
}
/* Placeholder text */
.stTextInput > div > div > input::placeholder,
.stTextArea > div > div > textarea::placeholder {
    color: rgba(232,224,208,0.35) !important;
}
/* Typed text in ALL input types */
input, textarea, select {
    color: #ffffff !important;
}
/* Time/date/number picker typed value */
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    color: #ffffff !important;
    background: rgba(15, 20, 35, 0.85) !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: rgba(255,195,64,0.65) !important;
    box-shadow: 0 0 0 2px rgba(255,195,64,0.15) !important;
}
/* Selectbox selected text */
[data-baseweb="select"] > div {
    color: #ffffff !important;
    background-color: rgba(15, 20, 35, 0.85) !important;
}

/* ── Metric cards ── */
[data-testid="stMetric"] {
    background: rgba(255,195,64,0.06);
    border: 1px solid rgba(255,195,64,0.18);
    border-radius: 12px;
    padding: 0.8rem 1rem;
}
[data-testid="stMetricValue"] {
    color: #FFC340 !important;
    font-family: 'Cinzel', serif;
    font-size: 1.6rem !important;
}
[data-testid="stMetricLabel"] {
    color: rgba(232,224,208,0.7) !important;
    font-size: 0.8rem !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

/* ── Tarot card box ── */
.tarot-card-box {
    background: linear-gradient(160deg, rgba(255,195,64,0.07), rgba(43,122,11,0.06));
    border: 1px solid rgba(255,195,64,0.28);
    border-radius: 14px;
    padding: 18px 12px;
    text-align: center;
    margin-bottom: 1rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    transition: transform 0.2s ease;
}
.tarot-card-box:hover { transform: translateY(-3px); }
.tarot-position {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: rgba(255,195,64,0.7);
    margin-bottom: 10px;
}
.tarot-name {
    font-family: 'Cinzel', serif;
    font-size: 1rem;
    color: #fff;
    margin: 10px 0 6px;
}
.tarot-orient-up   { color: #90ee90; font-size: 0.8rem; }
.tarot-orient-rev  { color: #ffa07a; font-size: 0.8rem; }
.tarot-meaning     { color: rgba(232,224,208,0.6); font-size: 0.78rem; margin-top: 8px; line-height: 1.4; }

/* ── Result sections ── */
.result-section {
    background: rgba(255,255,255,0.025);
    border-left: 3px solid #FFC340;
    border-radius: 0 10px 10px 0;
    padding: 1.2rem 1.5rem;
    margin: 1rem 0;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0e1a 0%, #0d1117 100%) !important;
    border-right: 1px solid rgba(255,195,64,0.12) !important;
}
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p {
    color: #c8bfa8 !important;
}

/* ── Divider ── */
hr { border-color: rgba(255,195,64,0.15) !important; }

/* ── Info/success boxes ── */
[data-testid="stInfo"] {
    background: rgba(43,122,11,0.12) !important;
    border: 1px solid rgba(43,122,11,0.35) !important;
    border-radius: 10px !important;
}
[data-testid="stSuccess"] {
    background: rgba(43,122,11,0.15) !important;
    border: 1px solid rgba(43,122,11,0.4) !important;
    border-radius: 10px !important;
}
[data-testid="stWarning"] {
    background: rgba(255,195,64,0.10) !important;
    border: 1px solid rgba(255,195,64,0.35) !important;
    border-radius: 10px !important;
}

/* ── Code block (chart) ── */
[data-testid="stCode"] {
    background: rgba(0,0,0,0.4) !important;
    border: 1px solid rgba(255,195,64,0.15) !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Imports (after set_page_config) ────────────────────────────────────────
from jyogi.services.cities import get_city_coords, save_custom_city
from jyogi.services.geocode import geocode_city
from jyogi.services.shop import show_shop_page
from jyogi.services.admin import show_admin_panel
from jyogi.pipelines.astrology import generate_astrology_report
from jyogi.pipelines.tarot import generate_tarot_report
from jyogi.reports import pdf_writer
from jyogi import tarot_deck
from jyogi import logger as db

# ── Password Gate ──────────────────────────────────────────────────────────
# Set APP_PASSWORD in your Streamlit secrets or leave blank to disable
def _check_auth() -> bool:
    """Returns True if app is unlocked."""
    # Get password from secrets (empty string = no password required)
    try:
        required_pw = st.secrets.get("APP_PASSWORD", "")
    except Exception:
        required_pw = ""

    # No password set = open access
    if not required_pw:
        return True

    # Already authenticated this session
    if st.session_state.get("authenticated"):
        return True

    # Show login screen
    st.markdown("""
    <div style="max-width:400px;margin:4rem auto;text-align:center;">
        <div style="font-size:3rem;margin-bottom:0.5rem;">🔮</div>
        <div style="font-family:Cinzel,serif;color:#FFC340;font-size:1.8rem;letter-spacing:3px;
             margin-bottom:0.3rem;">JYOGI</div>
        <div style="color:rgba(232,224,208,0.5);font-size:0.85rem;margin-bottom:2rem;font-style:italic;">
            Enter your access key to continue
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pw = st.text_input("Access Key", type="password",
                           placeholder="Enter password...",
                           label_visibility="collapsed")
        if st.button("✨ Enter", use_container_width=True, type="primary"):
            if pw == required_pw:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("❌ Incorrect access key. Please try again.")
    return False

if not _check_auth():
    st.stop()   # halt — nothing below renders until authenticated

# ── Session ID (unique per browser session for logging) ────────────────────
if "session_id" not in st.session_state:
    import uuid
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

# Init the database file on first run
db.init_db()
# ── Hero ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="jyogi-hero">
  <h1>🔮 JYOGI</h1>
  <p class="tagline">Vedic Astrology &nbsp;·&nbsp; Tarot Reading &nbsp;·&nbsp; Sacred Offerings</p>
  <p class="sub">Om Tat Sat — May the stars illuminate your path.</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar navigation ─────────────────────────────────────────────────────
_nav_options = ["🪐 Vedic Astrology & Numerology", "🎴 Tarot Reading", "💎 Shop & Offerings"]

# Show Admin option only if ADMIN_PASSWORD is configured
try:
    _has_admin = bool(st.secrets.get("ADMIN_PASSWORD", ""))
except Exception:
    _has_admin = False
if _has_admin:
    _nav_options.append("🔐 Admin")

mode = st.sidebar.radio("🌟 Choose Your Path", _nav_options)

# ═══════════════════════════════════════════════════════════════════════════
# 1.  VEDIC ASTROLOGY
# ═══════════════════════════════════════════════════════════════════════════
if mode == "🪐 Vedic Astrology & Numerology":
    st.header("💎 Vedic Horoscope & Numerology")

    # ── LOCATION — OUTSIDE form so radio/inputs render dynamically ─────────
    CITY_COORDS = get_city_coords()

    st.markdown('<div class="loc-box">', unsafe_allow_html=True)
    st.markdown("#### 📍 Birth Location")

    loc_tab = st.radio(
        "How would you like to set the location?",
        ["🏙️ Choose from city list", "🔍 Search any city", "🌐 Enter coordinates manually"],
        horizontal=True,
        label_visibility="collapsed",
    )

    # Initialise defaults
    if "astro_lat" not in st.session_state:
        st.session_state["astro_lat"] = 22.26
        st.session_state["astro_lon"] = 84.85
        st.session_state["astro_loc_label"] = "Rourkela"

    # ── Tab 1: City list ────────────────────────────────────────────────────
    if loc_tab == "🏙️ Choose from city list":
        city_options = list(CITY_COORDS.keys()) + ["➕ Add New City"]
        city_choice  = st.selectbox("Select City", city_options, label_visibility="collapsed")

        if city_choice in CITY_COORDS:
            st.session_state["astro_lat"]       = CITY_COORDS[city_choice][0]
            st.session_state["astro_lon"]       = CITY_COORDS[city_choice][1]
            st.session_state["astro_loc_label"] = city_choice

        elif city_choice == "➕ Add New City":
            st.info("Enter the new city details below and save it.")
            ac1, ac2, ac3 = st.columns([2, 1, 1])
            with ac1:
                new_city_name = st.text_input("City Name", placeholder="e.g. Surat")
            with ac2:
                new_city_lat  = st.number_input("Latitude",  value=0.0, format="%.4f", key="nc_lat")
            with ac3:
                new_city_lon  = st.number_input("Longitude", value=0.0, format="%.4f", key="nc_lon")
            if st.button("💾 Save City"):
                try:
                    save_custom_city(new_city_name, new_city_lat, new_city_lon)
                    st.success(f"✅ Saved **{new_city_name}**! Select it from the dropdown above.")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))

    # ── Tab 2: Search ───────────────────────────────────────────────────────
    elif loc_tab == "🔍 Search any city":
        sc1, sc2 = st.columns([4, 1])
        with sc1:
            search_query = st.text_input(
                "City search",
                placeholder="Type city name, e.g. Rourkela, India",
                label_visibility="collapsed",
            )
        with sc2:
            do_search = st.button("🔍 Search")

        if do_search and search_query.strip():
            with st.spinner("Searching…"):
                result = geocode_city(search_query.strip())
            if result:
                st.session_state["astro_lat"]       = result["lat"]
                st.session_state["astro_lon"]       = result["lon"]
                st.session_state["astro_loc_label"] = result["address"]
                st.success(f"✅ Found: {result['address']}")
            else:
                st.warning("❌ City not found. Try a different spelling or add country name.")

    # ── Tab 3: Manual coordinates ───────────────────────────────────────────
    else:
        mc1, mc2 = st.columns(2)
        with mc1:
            manual_lat = st.number_input(
                "Latitude (°N positive, °S negative)",
                value=st.session_state["astro_lat"],
                format="%.4f",
                key="manual_lat",
            )
        with mc2:
            manual_lon = st.number_input(
                "Longitude (°E positive, °W negative)",
                value=st.session_state["astro_lon"],
                format="%.4f",
                key="manual_lon",
            )
        if st.button("✅ Use These Coordinates"):
            st.session_state["astro_lat"]       = manual_lat
            st.session_state["astro_lon"]       = manual_lon
            st.session_state["astro_loc_label"] = f"{manual_lat:.4f}°, {manual_lon:.4f}°"
            st.success("Coordinates saved!")

    # Show current location badge
    st.markdown(
        f'<span class="loc-badge">📌 {st.session_state["astro_loc_label"]} '
        f'({st.session_state["astro_lat"]:.4f}°N, {st.session_state["astro_lon"]:.4f}°E)</span>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # ── CLIENT DETAILS FORM ────────────────────────────────────────────────
    with st.form("astro_form"):
        st.markdown("#### 👤 Client Details")
        col1, col2 = st.columns(2)
        with col1:
            name   = st.text_input("Client Name", "Jyoti")
            b_date = st.date_input(
                "Birth Date",
                min_value=dt.date(1900, 1, 1),
                max_value=dt.date.today(),
                value=dt.date(2002, 8, 17),
            )
        with col2:
            b_time = st.time_input("Birth Time (local IST)", value=dt.time(8, 35), step=60)
            st.caption("Use 24-hour format. Enter exact birth time for accurate Lagna.")

        st.divider()
        user_q    = st.text_area(
            "✨ Specific Question (optional)",
            placeholder="e.g. When will I get married? Should I change jobs? What is blocking my success?",
        )
        submitted = st.form_submit_button("🔮 Generate My Reading", use_container_width=True)

    # ── GENERATE REPORT ────────────────────────────────────────────────────
    if submitted:
        lat = st.session_state["astro_lat"]
        lon = st.session_state["astro_lon"]

        with st.spinner("🌌 Calculating planetary positions…"):
            report = generate_astrology_report(
                name=name,
                date_str=str(b_date),
                time_str=b_time.strftime("%H:%M"),
                lat=float(lat),
                lon=float(lon),
                user_q=user_q,
            )
            # Auto-log this reading (stored locally in jyogi_data.xlsx, never sent to AI)
            try:
                db.log_astrology(
                    client_name=name,
                    birth_date=str(b_date),
                    birth_time=b_time.strftime("%H:%M"),
                    birth_location=st.session_state.get("astro_loc_label", ""),
                    question=user_q,
                    session_id=st.session_state.get("session_id", ""),
                )
            except Exception:
                pass

        # ── Numerology cards ───────────────────────────────────────────────
        st.divider()
        st.markdown("### 🔢 Numerology")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Life Path",  report["lp_num"])
        m2.metric("Archetype",  report["lp_data"].get("title", "-"))
        m3.metric("Lucky Gem",  report["lp_data"].get("lucky_gem", "-"))
        m4.metric("Lucky Colour", report["lp_data"].get("lucky_color", "-"))

        with st.expander("📊 Full Planetary Chart (Sidereal Lahiri)", expanded=False):
            st.code(report["chart_text"])

        # ── AI sections ────────────────────────────────────────────────────
        for icon, title, key in [
            ("🌅", "Lagna & Personality",         "lagna_text"),
            ("🔱", "Current Mahadasha",            "dasha_text"),
            ("🪐", "Saturn Transit — Sadhe Sati",  "ss_text"),
        ]:
            st.markdown(f"### {icon} {title}")
            st.markdown(
                f'<div class="result-section">{report[key]}</div>',
                unsafe_allow_html=True,
            )

        # ── Full Vimshottari Dasha Timeline ───────────────────────────────
        timeline = report.get("analysis", {}).get("dasha", {}).get("timeline", [])
        if timeline:
            with st.expander("📅 Full Vimshottari Dasha Timeline (120 years)", expanded=False):
                current_dasha = report.get("analysis", {}).get("dasha", {}).get("current", "")
                st.markdown(
                    '<div style="font-size:0.8rem;color:rgba(232,224,208,0.55);'
                    'margin-bottom:10px;font-style:italic;">'
                    'The highlighted row is your current active Mahadasha.</div>',
                    unsafe_allow_html=True,
                )
                for row in timeline:
                    is_current = row["lord"] == current_dasha
                    bg   = "rgba(255,195,64,0.12)" if is_current else "rgba(255,255,255,0.02)"
                    border = "rgba(255,195,64,0.5)" if is_current else "rgba(255,255,255,0.07)"
                    tag  = " ◀ NOW" if is_current else ""
                    st.markdown(
                        f'<div style="display:flex;justify-content:space-between;'
                        f'background:{bg};border:1px solid {border};'
                        f'border-radius:8px;padding:7px 14px;margin:3px 0;'
                        f'font-size:0.85rem;">'
                        f'<span style="color:#FFC340;font-weight:{"700" if is_current else "400"};">'
                        f'{row["lord"]} Mahadasha{tag}</span>'
                        f'<span style="color:rgba(232,224,208,0.6);">{row["start"]} → {row["end"]}</span>'
                        f'<span style="color:rgba(232,224,208,0.4);">{row["years"]}</span>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )

        if report.get("qa_text"):
            st.markdown("### 🕉️ Your Question Answered")
            st.markdown(
                f'<div class="result-section">{report["qa_text"]}</div>',
                unsafe_allow_html=True,
            )

        # ── PDF ────────────────────────────────────────────────────────────
        pdf_filename = f"{name}_Astro_Report.pdf"
        if pdf_writer.save_reading_to_pdf(
            pdf_filename, report["sections"],
            title=f"{name} — Vedic Astro Report"
        ):
            with open(pdf_filename, "rb") as f:
                st.download_button(
                    "📄 Download Full PDF Report",
                    f, file_name=pdf_filename, mime="application/pdf",
                    use_container_width=True,
                )

# ═══════════════════════════════════════════════════════════════════════════
# 2.  TAROT READING
# ═══════════════════════════════════════════════════════════════════════════
elif mode == "🎴 Tarot Reading":

    # session state init
    for _k, _d in [("tarot_spread", None), ("tarot_revealed", False),
                   ("tarot_report", None), ("tarot_q", ""), ("tarot_spread_id", "1")]:
        if _k not in st.session_state:
            st.session_state[_k] = _d

    # HEADER
    st.markdown(
        '<div style="text-align:center;padding:1.2rem 1rem 0.5rem;">'
        '<span style="font-size:2.4rem;">🎴</span>'
        '<h2 style="font-family:Cinzel,serif;color:#FFC340;margin:0.3rem 0;">Pro Tarot Reading</h2>'
        '<p style="color:rgba(232,224,208,0.65);font-style:italic;font-size:0.92rem;">'
        'Focus deeply on your question. The cards will reveal what you <strong>need</strong> to know.'
        '</p></div>',
        unsafe_allow_html=True,
    )

    # INPUT PANEL
    ic1, ic2 = st.columns([1, 2])
    with ic1:
        t_name = st.text_input("👤 Client Name", placeholder="e.g. Jyoti", key="tarot_name")
    with ic2:
        options = tarot_deck.get_spread_options()
        spread_labels = [f"{k}: {v['name']}" for k, v in options.items()]
        choice_label  = st.selectbox("🃏 Choose a Spread", spread_labels)
        choice_id     = choice_label.split(":")[0].strip()

    sinfo = options[choice_id]

    # Info badge row
    bc1, bc2, bc3 = st.columns(3)
    def _badge(col, label, val):
        col.markdown(
            f'<div style="background:rgba(255,195,64,0.07);border:1px solid rgba(255,195,64,0.22);'
            f'border-radius:8px;padding:8px 10px;text-align:center;margin-top:8px;">'
            f'<div style="color:rgba(255,195,64,0.7);font-size:0.68rem;text-transform:uppercase;letter-spacing:1px;">{label}</div>'
            f'<div style="color:#fff;font-weight:600;font-size:0.9rem;">{val}</div></div>',
            unsafe_allow_html=True,
        )
    _badge(bc1, "Spread", sinfo["name"])
    _badge(bc2, "Cards", str(sinfo["cards"]))
    _badge(bc3, "Purpose", "Click to reveal" if st.session_state["tarot_spread"] else "Shuffle to begin")

    st.markdown("<div style='margin:0.6rem 0;'></div>", unsafe_allow_html=True)
    user_q = st.text_area(
        "🌟 Your Focus Question",
        placeholder="e.g. Will my relationship improve?  |  Should I change jobs?  |  What energy surrounds me?",
        height=85,
    )

    # ACTION BUTTONS — rendered based on session state so Reveal appears immediately after shuffle
    ab1, ab2, ab3 = st.columns([5, 5, 2])
    with ab1:
        do_shuffle = st.button("🔀 Shuffle & Draw Cards", use_container_width=True)
    with ab2:
        # Show Reveal only when cards are drawn but not yet revealed
        _has_cards    = st.session_state["tarot_spread"] is not None
        _not_revealed = not st.session_state["tarot_revealed"]
        if _has_cards and _not_revealed:
            do_reveal = st.button("✨ Reveal My Destiny", use_container_width=True, type="primary")
        else:
            do_reveal = False
    with ab3:
        if st.session_state["tarot_spread"] is not None:
            if st.button("🔁 New", use_container_width=True):
                for _k in ("tarot_spread", "tarot_report"):
                    st.session_state[_k] = None
                st.session_state["tarot_revealed"] = False
                st.rerun()

    if do_shuffle:
        if not user_q.strip():
            st.warning("⚠️  Please enter your focus question before shuffling.")
        else:
            _bar = st.progress(0, text="🔀  Shuffling the sacred deck…")
            for _p in range(100):
                time.sleep(0.007)
                _bar.progress(_p + 1, text="🔀  Shuffling the sacred deck…")
            _bar.empty()
            st.session_state["tarot_spread"]    = tarot_deck.pull_spread(choice_id)
            st.session_state["tarot_spread_id"] = choice_id
            st.session_state["tarot_q"]         = user_q
            st.session_state["tarot_revealed"]  = False
            st.session_state["tarot_report"]    = None
            st.rerun()   # rerun → Reveal button now appears immediately

    if do_reveal:
        st.session_state["tarot_revealed"] = True
        st.balloons()
        st.rerun()

    # CARD DISPLAY
    if st.session_state["tarot_spread"] and st.session_state["tarot_revealed"]:
        spread_data     = st.session_state["tarot_spread"]
        saved_q         = st.session_state.get("tarot_q", user_q)
        saved_spread_id = st.session_state.get("tarot_spread_id", choice_id)
        saved_sinfo     = options.get(saved_spread_id, sinfo)
        num_cards       = len(spread_data)

        st.divider()

        rh1, rh2 = st.columns([3, 1])
        with rh1:
            st.markdown(
                f'<h3 style="font-family:Cinzel,serif;color:#FFC340;margin:0;">'
                f'Reading for {t_name or "The Seeker"}</h3>'
                f'<p style="color:rgba(232,224,208,0.6);font-style:italic;margin:4px 0 0;">'
                f'\"{saved_q}\"</p>',
                unsafe_allow_html=True,
            )
        with rh2:
            st.markdown(
                f'<div style="text-align:right;padding-top:10px;">'
                f'<span style="background:rgba(255,195,64,0.1);border:1px solid rgba(255,195,64,0.3);'
                f'border-radius:20px;padding:4px 14px;font-size:0.8rem;color:#FFC340;">'
                f'🃏 {num_cards} cards · {saved_sinfo["name"]}</span></div>',
                unsafe_allow_html=True,
            )

        st.markdown("<div style='margin:0.8rem 0;'></div>", unsafe_allow_html=True)

        cols_per_row = min(num_cards, 3)
        card_summary = ""

        for row_start in range(0, num_cards, cols_per_row):
            row_items = spread_data[row_start: row_start + cols_per_row]
            # pad last row
            while len(row_items) < cols_per_row:
                row_items.append(None)
            grid_cols = st.columns(cols_per_row)

            for gcol, item in zip(grid_cols, row_items):
                if item is None:
                    continue
                is_rev    = "[REVERSED]" in item["Card"].upper()
                base_name = item["Card"].split(" [")[0].strip()
                raw_name  = base_name.replace(" ", "_")
                orient    = "🔄 Reversed" if is_rev else "⬆️ Upright"
                o_color   = "#ffa07a"     if is_rev else "#90ee90"

                with gcol:
                    # Position label
                    st.markdown(
                        f'<div style="text-align:center;font-size:0.68rem;text-transform:uppercase;'
                        f'letter-spacing:1.4px;color:rgba(255,195,64,0.6);margin-bottom:6px;">'
                        f'{item["Position"]}</div>',
                        unsafe_allow_html=True,
                    )

                    img_path = tarot_deck.find_card_image(raw_name)
                    img_shown = False
                    if img_path:
                        try:
                            from PIL import Image as _PIL
                            img = _PIL.open(img_path)
                            if is_rev:
                                img = img.rotate(180)
                            st.image(img, width="stretch")
                            img_shown = True
                        except Exception:
                            pass

                    if not img_shown:
                        card_emoji = "🌑" if is_rev else "🌟"
                        st.markdown(
                            f'<div class="tarot-card-box">'
                            f'<div style="font-size:2.8rem;margin:10px 0;">{card_emoji}</div>'
                            f'<div class="tarot-name">{base_name}</div>'
                            f'</div>',
                            unsafe_allow_html=True,
                        )

                    # Name + orientation
                    st.markdown(
                        f'<div style="text-align:center;margin:8px 0 4px;">'
                        f'<strong style="font-family:Cinzel,serif;font-size:0.85rem;">{base_name}</strong><br>'
                        f'<span style="color:{o_color};font-size:0.75rem;">{orient}</span>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                    with st.expander("📖 Meaning & Affirmation"):
                        if item.get("Reversed"):
                            st.markdown(
                                f'<div style="background:rgba(255,100,70,0.08);border-left:3px solid #ffa07a;'
                                f'border-radius:0 8px 8px 0;padding:8px 12px;margin-bottom:6px;">'
                                f'<span style="font-size:0.68rem;text-transform:uppercase;letter-spacing:1px;'
                                f'color:#ffa07a;">🌑 Shadow Seer — Reversed</span><br>'
                                f'<span style="font-size:0.83rem;color:#e8e0d0;">{item.get("ShadowMeaning", item["Meaning"])}</span></div>',
                                unsafe_allow_html=True,
                            )
                        else:
                            st.markdown(
                                f'<div style="background:rgba(144,238,144,0.08);border-left:3px solid #90ee90;'
                                f'border-radius:0 8px 8px 0;padding:8px 12px;margin-bottom:6px;">'
                                f'<span style="font-size:0.68rem;text-transform:uppercase;letter-spacing:1px;'
                                f'color:#90ee90;">🌟 Light Seer — Upright</span><br>'
                                f'<span style="font-size:0.83rem;color:#e8e0d0;">{item.get("LightMeaning", item["Meaning"])}</span></div>',
                                unsafe_allow_html=True,
                            )
                        st.markdown(
                            f'<p style="color:#FFC340;font-size:0.8rem;font-style:italic;margin-top:6px;">'
                            f'✨ {item["Affirmation"]}</p>',
                            unsafe_allow_html=True,
                        )

                card_summary += f"{item['Position']}: {item['Card']} — {item['Meaning']}\n"

        # AI INTERPRETATION
        st.divider()
        st.markdown(
            '<h3 style="font-family:Cinzel,serif;color:#FFC340;">🔮 Jyogi\'s Interpretation</h3>',
            unsafe_allow_html=True,
        )

        if st.session_state["tarot_report"] is None:
            with st.spinner("🌌  Connecting to the astral plane…"):
                report = generate_tarot_report(saved_spread_id, saved_q, t_name)
                st.session_state["tarot_report"] = report
                # Auto-log this reading
                try:
                    db.log_tarot(
                        client_name=t_name,
                        spread_name=report["spread_info"]["name"],
                        cards_count=len(report["spread_data"]),
                        question=saved_q,
                        session_id=st.session_state.get("session_id", ""),
                    )
                except Exception:
                    pass
        else:
            report = st.session_state["tarot_report"]

        st.markdown(
            f'<div class="result-section">{report["ai_answer"]}</div>',
            unsafe_allow_html=True,
        )

        with st.expander("✨ All Affirmations for Today"):
            for item in spread_data:
                is_rev_a = "[REVERSED]" in item["Card"].upper()
                color_a  = "#ffa07a" if is_rev_a else "#FFC340"
                name_a   = item["Card"].split(" [")[0].strip()
                st.markdown(
                    f'<p style="color:{color_a};margin:5px 0;">• <strong>{name_a}</strong>: '
                    f'{item["Affirmation"]}</p>',
                    unsafe_allow_html=True,
                )

        st.divider()
        pdf_fn = f"{t_name or 'Tarot'}_Reading.pdf"
        if pdf_writer.save_reading_to_pdf(
            pdf_fn, report["sections"],
            title=f"{t_name or 'Tarot'} — Jyogi Tarot Reading",
        ):
            with open(pdf_fn, "rb") as _pf:
                st.download_button(
                    "📄 Download Full Reading PDF", _pf,
                    file_name=pdf_fn, mime="application/pdf",
                    use_container_width=True,
                )


# ═══════════════════════════════════════════════════════════════════════════
# 3.  SHOP & OFFERINGS
# ═══════════════════════════════════════════════════════════════════════════
elif mode == "💎 Shop & Offerings":
    show_shop_page()


# ═══════════════════════════════════════════════════════════════════════════
# 4.  ADMIN (only visible when ADMIN_PASSWORD is set in secrets)
# ═══════════════════════════════════════════════════════════════════════════
elif mode == "🔐 Admin":
    show_admin_panel()
