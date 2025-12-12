import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="EcoScanner", page_icon="🌿", layout="centered")

# ---------------- DARK THEME CSS ----------------
CSS = """
<style>
.stApp {
    background: linear-gradient(135deg, #1a0033, #330066, #660099);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #ffffff;
    padding: 20px;
}
.big-title {
    font-size:40px;
    text-align:center;
    font-weight:700;
    margin-top:-10px;
    color:#e1bee7;
}
.subtitle {
    text-align:center;
    color:#ce93d8;
    margin-top:-10px;
    margin-bottom:10px;
}
.mascot {
    text-align:center;
    font-size:70px;
    margin-top:-14px;
}
@keyframes bounce {0%,20%,50%,80%,100% {transform:translateY(0);} 40% {transform:translateY(-10px);} 60% {transform:translateY(-6px);}}
@keyframes wiggle {0%,100% {transform:rotate(0deg);} 25% {transform:rotate(10deg);} 75% {transform:rotate(-10deg);}}
@keyframes hop {0%,20%,50%,80%,100% {transform:translateY(0);} 40% {transform:translateY(-15px);} 60% {transform:translateY(-10px);}}
.mascot.bounce {animation: bounce 1.5s infinite; color:#ffeb3b;}
.mascot.wiggle {animation: wiggle 1s infinite; color:#ffeb3b;}
.mascot.hop {animation: hop 1.5s infinite; color:#ffeb3b;}
.achievement-badge {
    font-size:30px; 
    animation: pop 0.7s; 
    display:inline-block; 
    margin:5px; 
    color:#ffd700;
}
@keyframes pop {0% {transform: scale(0);} 70% {transform: scale(1.3);} 100% {transform: scale(1);}}
.progress-container {
    height:22px;
    background:#4a0073;
    border-radius:14px;
    overflow:hidden;
    margin-top:10px;
}
.progress-bar {
    height:100%;
    background:#d1c4e9;
}
.stButton>button {
    background-color:#6a0dad; 
    color:#fff; 
    font-weight:bold; 
    border-radius:12px; 
    height:40px;
}
audio { display:none; } /* hide audio player */
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
for key in ['mode','achievements','leaderboard','quiz_index','quiz_score','music_played']:
    if key not in st.session_state:
        if key in ['achievements','leaderboard']: st.session_state[key] = []
        elif key in ['quiz_index','quiz_score']: st.session_state[key] = 0
        else: st.session_state[key] = False if key=='music_played' else 'scanner'

# ---------------- MASCOT ----------------
def mascot(animation='bounce'):
    st.markdown(f"<div class='mascot {animation}'>🐣🌿</div>", unsafe_allow_html=True)
    st.markdown("<div class='big-title'>EcoScanner Deluxe</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Cute, interactive, mobile-friendly eco app!</div>", unsafe_allow_html=True)

mascot()

# ---------------- BACKGROUND MUSIC (ONLINE) ----------------
if not st.session_state['music_played']:
    music_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="{music_url}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )
    st.session_state['music_played'] = True

# ---------------- APP TABS ----------------
tabs = st.tabs(["Scanner","Quiz","Challenge","Achievements"])

# ---------------- SCANNER MODE ----------------
with tabs[0]:
    st.session_state['mode'] = 'scanner'
    mascot('bounce')
    st.header("🔎 Scanner Mode")

    material = st.selectbox("Material", ["Cotton","Jute","Plastic","Metal","Glass","Cardboard"])
    packaging = st.selectbox("Packaging", ["Plastic Wrapper","Cardboard Box","Cloth Bag","Glass Jar","No Packaging","Paper Wrap"])
    category = st.selectbox("Category", ["Clothing","Food","Accessories","Cosmetics","Utensils","Other"])
    eco_traits = st.multiselect("Eco Features", ["Recyclable","Non Recyclable","Organic","Plastic-Free"])
    guess = st.slider("Your guess for eco score", 0, 100, 50)

    if st.button("✨ Analyze"):
        score = 50
        if material in ["Plastic"]: score -=25
        if material in ["Glass"]: score +=20
        if packaging in ["Plastic Wrapper"]: score -=15
        if packaging in ["Paper Wrap","Glass Jar"]: score +=10
        score += len(eco_traits)*10
        score = max(0,min(100,score))

        st.subheader("📊 Eco Score")
        st.markdown(
            f"<div class='progress-container'><div class='progress-bar' style='width:{score}%;'></div></div>",
            unsafe_allow_html=True
        )
        diff = abs(score-guess)
        st.markdown(f"<span style='color:#ffffff;'>**Score:** {score}/100</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#ffffff;'>Your guess: {guess} — Difference: {diff}</span>", unsafe_allow_html=True)

        if score>=75 or diff==0:
            st.session_state['achievements'].append("Perfect Scanner! 🌿")
            st.balloons()

# ---------------- QUIZ MODE ----------------
with tabs[1]:
    st.session_state['mode'] = 'quiz'
    mascot('wiggle')
    st.header("❓ Quiz Mode")

    questions = [
        {"q":"Which material is most eco-friendly?","options":["Plastic","Organic Cotton","Polyester"],"answer":"Organic Cotton"},
        {"q":"Which packaging is best?","options":["Plastic Wrap","Glass Jar","Aluminium Foil"],"answer":"Glass Jar"},
        {"q":"Eco-friendly energy source?","options":["Coal","Diesel","Solar"],"answer":"Solar"}
    ]

    idx = st.session_state['quiz_index']
    if idx < len(questions):
        q = questions[idx]
        choice = st.radio(q['q'], q['options'])
        if st.button("Submit Answer"):
            if choice==q['answer']:
                st.session_state['quiz_score'] += 1
                st.success("Correct! 🌱")
                st.session_state['achievements'].append(f"Quiz Q{idx+1} Master! 🏅")
                st.balloons()
            else:
                st.error(f"Wrong! Answer: {q['answer']}")
            st.session_state['quiz_index'] += 1
    else:
        st.markdown(f"<span style='color:#ffffff;'>Quiz complete! Score: {st.session_state['quiz_score']}/{len(questions)}</span>", unsafe_allow_html=True)
        if st.session_state['quiz_score'] == len(questions):
            st.session_state['achievements'].append("Quiz Master! 🌟")
            st.balloons()
        if st.button("Restart Quiz"):
            st.session_state['quiz_index'] = 0
            st.session_state['quiz_score'] = 0

# ---------------- CHALLENGE MODE ----------------
with tabs[2]:
    st.session_state['mode'] = 'challenge'
    mascot('hop')
    st.header("⚡ Challenge Mode")

    traits = ["Recycled","Plastic","Organic","Solar","Toxic Chemicals","Glass Packaging"]
    shown = random.sample(traits,3)
    st.write("### Traits of Product:")
    for t in shown: st.markdown(f"<span style='color:#ffffff;'>- {t}</span>", unsafe_allow_html=True)

    guess = st.slider("Your guess for eco score",0,100,50,key="challenge_guess")

    if st.button("Reveal Score"):
        score = 50
        for t in shown:
            if t in ["Recycled","Organic","Solar","Glass Packaging"]: score+=15
            else: score-=20
        score = max(0,min(100,score))
        st.markdown(f"<span style='color:#ffffff;'>### Real Score: {score}</span>", unsafe_allow_html=True)
        diff = abs(score-guess)
        st.markdown(f"<span style='color:#ffffff;'>Difference: {diff}</span>", unsafe_allow_html=True)

        st.session_state['leaderboard'].append(score)
        st.session_state['leaderboard'] = sorted(st.session_state['leaderboard'], reverse=True)[:5]

        if diff <= 10:
            st.success("Amazing guess! 🌱✨")
            st.session_state['achievements'].append("Challenge Winner! 🏆")
            st.balloons()

    st.subheader("🏆 Leaderboard")
    for i, s in enumerate(st.session_state['leaderboard']):
        st.markdown(f"<span style='color:#ffffff;'>{i+1}. Score: {s}</span>", unsafe_allow_html=True)

# ---------------- ACHIEVEMENTS ----------------
with tabs[3]:
    st.header("🪄 Achievements")
    if st.session_state['achievements']:
        for a in st.session_state['achievements']:
            st.markdown(f"<span class='achievement-badge'>🏅 {a}</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span style='color:#ffffff;'>No achievements unlocked yet.</span>", unsafe_allow_html=True)

