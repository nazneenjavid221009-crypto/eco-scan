import streamlit as st
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="EcoScanner", page_icon="🌿", layout="centered")

# ---------------- LOAD CSS ----------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
for key in ['achievements','quiz_score','music_played']:
    if key not in st.session_state:
        st.session_state[key] = [] if key == 'achievements' else 0

# ---------------- HEADER ----------------
st.markdown("<div class='mascot bounce'>🌍🌿</div>", unsafe_allow_html=True)
st.markdown("<div class='big-title'>EcoScanner</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Scan products. Grow trees. Save Earth.</div>", unsafe_allow_html=True)

# ---------------- BACKGROUND MUSIC ----------------
if not st.session_state.music_played:
    st.markdown("""
    <audio autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)
    st.session_state.music_played = True

# ---------------- TABS ----------------
tabs = st.tabs(["🔎 Scanner", "⚡ Rapid Fire Quiz", "🏆 Achievements"])

# ===================== SCANNER =====================
with tabs[0]:
    st.header("🔍 Eco Scanner")

    material = st.selectbox("Material", ["Plastic", "Cotton", "Jute", "Glass", "Metal"])
    packaging = st.selectbox("Packaging", ["Plastic Wrapper", "Paper Wrap", "Cloth Bag", "Glass Jar", "No Packaging"])
    eco_traits = st.multiselect("Eco Features", ["Recyclable", "Organic", "Plastic-Free"])
    guess = st.slider("Guess the Eco Score", 0, 100, 50)

    if st.button("✨ Scan Product"):
        with st.spinner("🌿 Scanning environmental impact..."):
            progress = st.progress(0)
            for i in range(0, 101, 10):
                progress.progress(i)
                time.sleep(0.05)

        # ----- ECO SCORE LOGIC -----
        score = 50
        if material == "Plastic":
            score -= 25
        if material in ["Jute", "Glass"]:
            score += 20
        if packaging == "Plastic Wrapper":
            score -= 15
        if packaging in ["Paper Wrap", "Cloth Bag", "Glass Jar"]:
            score += 10
        score += len(eco_traits) * 10
        score = max(0, min(100, score))

        # ----- TREE GROWTH -----
        if score <= 30:
            tree, msg = "🌱", "Needs improvement"
        elif score <= 60:
            tree, msg = "🌿", "Good start"
        elif score <= 80:
            tree, msg = "🌳", "Eco friendly"
        else:
            tree, msg = "🌲", "Excellent choice!"

        st.markdown(f"<div class='tree'>{tree}</div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center;'>{msg}</h3>", unsafe_allow_html=True)

        st.markdown(f"### 🌍 Eco Score: **{score}/100**")
        st.markdown(f"Your guess difference: **{abs(score - guess)}**")

        # ----- SUGGESTIONS -----
        st.subheader("🌱 Better Alternatives")
        if material == "Plastic":
            st.info("Use **steel or glass bottles** instead of plastic 🥤")
        if packaging == "Plastic Wrapper":
            st.info("Choose **paper or cloth packaging** 📦")
        if score >= 75:
            st.success("Great eco-friendly choice! 🌍")

        if score >= 80:
            st.session_state.achievements.append("Eco Champion 🌲")
            st.balloons()

# ===================== RAPID FIRE QUIZ =====================
with tabs[1]:
    st.header("⚡ Rapid Fire Quiz")

    questions = [
        ("Which decomposes fastest?", ["Plastic", "Banana Peel", "Glass"], "Banana Peel"),
        ("Best renewable energy?", ["Coal", "Solar", "Diesel"], "Solar"),
        ("Which bag is eco-friendly?", ["Plastic", "Cloth", "Polythene"], "Cloth")
    ]

    q = random.choice(questions)
    ans = st.radio(q[0], q[1])

    if st.button("⚡ Answer"):
        if ans == q[2]:
            st.success("Correct! 🌱")
            st.session_state.quiz_score += 1
            st.session_state.achievements.append("Rapid Fire Star ⚡")
            st.balloons()
        else:
            st.error(f"Wrong! Correct answer: {q[2]}")

# ===================== ACHIEVEMENTS =====================
with tabs[2]:
    st.header("🏆 Achievements")

    if st.session_state.achievements:
        for a in set(st.session_state.achievements):
            st.markdown(f"<div class='badge'>🏅 {a}</div>", unsafe_allow_html=True)
    else:
        st.info("No achievements yet. Start scanning! 🌱")



