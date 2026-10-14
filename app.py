import streamlit as st

st.set_page_config(
    page_title="Aster | Sustainable Wardrobe",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Stylish custom background and card-based layout
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

.stApp {
    background:
      radial-gradient(circle at 12% 8%, rgba(177, 205, 157, .26), transparent 27%),
      radial-gradient(circle at 90% 18%, rgba(219, 195, 153, .25), transparent 24%),
      linear-gradient(135deg, #f7f6ef 0%, #edf2e8 48%, #f4eee4 100%);
    color: #24352b;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
.block-container { max-width: 1120px; padding-top: 2rem; padding-bottom: 3rem; }
.hero {
    padding: 2.3rem 2.5rem;
    border-radius: 28px;
    color: #f8f7f0;
    background: linear-gradient(115deg, #203f32 0%, #42664c 55%, #82956b 100%);
    box-shadow: 0 18px 45px rgba(35, 61, 44, .16);
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero:after {
    content: "✳";
    position: absolute; right: 35px; top: -38px;
    font-size: 190px; color: rgba(255,255,255,.08);
}
.eyebrow { text-transform: uppercase; letter-spacing: .18em; font-size: .75rem; color: #d7e4ca; font-weight: 700; }
.hero h1 { font-family: 'Playfair Display', Georgia, serif; font-size: clamp(2.2rem, 5vw, 3.7rem); margin: .35rem 0 .4rem; color: #fffdf6; }
.hero p { font-size: 1.05rem; max-width: 680px; color: #e9efe3; line-height: 1.65; }
.pill { display: inline-block; border: 1px solid rgba(255,255,255,.35); padding: .4rem .8rem; border-radius: 999px; font-size: .8rem; margin: .3rem .25rem 0 0; }
.section-title { font-family: 'Playfair Display', Georgia, serif; color: #294b36; font-size: 1.7rem; margin: 1.4rem 0 .2rem; }
.subtle { color: #647466; }
div[data-testid="stForm"], div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,.76);
    border: 1px solid rgba(68, 94, 69, .13);
    border-radius: 20px;
    padding: 1rem 1.2rem;
    box-shadow: 0 10px 28px rgba(38, 58, 42, .06);
}
.stButton > button, .stFormSubmitButton > button {
    background: #2d563c; color: white; border: 0; border-radius: 12px;
    padding: .65rem 1.2rem; font-weight: 700; transition: all .2s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background: #1f402c; color: white; transform: translateY(-1px);
}
div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
    border-radius: 10px;
}
.metric-card {
    background: rgba(255,255,255,.78); border: 1px solid rgba(68,94,69,.12);
    padding: 1.2rem; border-radius: 18px; min-height: 130px;
}
.metric-card strong { display:block; font-size: 1.05rem; color: #2d563c; margin-bottom: .35rem; }
.metric-card span { color: #637267; font-size: .9rem; line-height: 1.5; }
.outfit-card {
    background: #fffdf8; border-left: 5px solid #779365; padding: 1rem 1.2rem;
    border-radius: 14px; margin: .5rem 0; box-shadow: 0 8px 20px rgba(45,68,47,.07);
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">Wear thoughtfully · Live sustainably</div>
  <h1>Aster</h1>
  <p>Your personal sustainable wardrobe companion. Rediscover outfits from clothes you already own, spend more mindfully, and make everyday style a little greener.</p>
  <span class="pill">🌿 SDG 12</span>
  <span class="pill">Digital wardrobe</span>
  <span class="pill">Mindful fashion</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Build a look from your own wardrobe</div>', unsafe_allow_html=True)
st.markdown('<p class="subtle">Tell Aster a little about your day and the pieces you have available.</p>', unsafe_allow_html=True)

left, right = st.columns([1.05, 0.95], gap="large")

with left:
    with st.form("wardrobe_form"):
        occasion = st.selectbox("What's the occasion?", ["College / everyday", "Office", "Party", "Formal event", "Outdoor"])
        weather = st.selectbox("What's the weather like?", ["Hot", "Mild", "Cold", "Rainy"])
        style = st.selectbox("Your style mood", ["Casual", "Formal", "Minimal", "Sporty", "Traditional"])
        tops = st.text_input("Tops you own", "white shirt, black t-shirt")
        bottoms = st.text_input("Bottoms you own", "blue jeans, black trousers")
        shoes = st.text_input("Footwear you own", "sneakers, formal shoes")
        submitted = st.form_submit_button("✨ Create my outfit", use_container_width=True)

with right:
    st.markdown("""
    <div class="metric-card">
      <strong>Less buying. More styling.</strong>
      <span>Aster is designed around the idea that the most sustainable outfit may be one already hanging in your wardrobe.</span>
    </div><br>
    <div class="metric-card">
      <strong>How it works</strong>
      <span>1. Add clothing you own<br>2. Choose an occasion and weather<br>3. Get a simple outfit suggestion<br>4. Rewear, remix and repeat</span>
    </div><br>
    <div class="metric-card">
      <strong>Our mission</strong>
      <span>Make everyday fashion more affordable and reduce unnecessary clothing waste through mindful wardrobe choices.</span>
    </div>
    """, unsafe_allow_html=True)

if submitted:
    def first_item(value, fallback):
        items = [x.strip() for x in value.split(",") if x.strip()]
        return items[0] if items else fallback

    weather_tips = {
        "Hot": "Choose breathable fabrics and lighter layers.",
        "Mild": "A light layer can help if the temperature changes.",
        "Cold": "Add a warm layer you already own.",
        "Rainy": "Choose weather-appropriate shoes and a water-resistant outer layer.",
    }
    occasion_tips = {
        "College / everyday": "Mix wardrobe basics for a comfortable everyday look.",
        "Office": "Keep the outfit neat and coordinated.",
        "Party": "Refresh an existing outfit with one accessory.",
        "Formal event": "Choose clean lines and coordinated colours.",
        "Outdoor": "Prioritise comfort and suitable footwear.",
    }
    st.markdown('<div class="section-title">Your Aster outfit</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="outfit-card"><strong>👕 Top</strong><br>{first_item(tops, "Choose a top you already own")}</div>
    <div class="outfit-card"><strong>👖 Bottom</strong><br>{first_item(bottoms, "Choose a suitable bottom you already own")}</div>
    <div class="outfit-card"><strong>👟 Footwear</strong><br>{first_item(shoes, "Choose comfortable footwear you already own")}</div>
    """, unsafe_allow_html=True)
    st.success(f"Weather tip: {weather_tips[weather]}")
    st.info(f"Styling tip for {occasion.lower()} ({style.lower()}): {occasion_tips[occasion]}")
    st.caption("Prototype note: current recommendations use simple rules. A trained AI model and saved wardrobe features are future improvements.")

st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="metric-card"><strong>♻ Rewear</strong><span>Try new combinations before purchasing more clothes.</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="metric-card"><strong>🧵 Repair</strong><span>Extend the life of pieces you already love.</span></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric-card"><strong>🤝 Rehome</strong><span>Consider donating or reselling items you no longer use.</span></div>', unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center;color:#6b7c6c;margin-top:2rem;font-size:.85rem">
Aster · Student prototype · Aligned with UN Sustainable Development Goal 12: Responsible Consumption and Production
</p>
""", unsafe_allow_html=True)
