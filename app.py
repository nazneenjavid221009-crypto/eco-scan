import streamlit as st
import random
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="EcoScanner Deluxe", page_icon="🌿", layout="centered")

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

# ---------------- BACKGROUND MUSIC ----------------
if not st.session_state['music_played']:
    # Load local MP3 file
    audio_file = "background.mp3"  # Place your file in the same folder
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
    # Convert to base64 to embed hidden audio
    b64 = base64.b64encode(audio_bytes).decode()
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )
    st.session_state['music_played'] = True

#
