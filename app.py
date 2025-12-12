import streamlit as st

# -------------------------------
# Load CSS
# -------------------------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------
# Background music (autoplay & hidden)
# -------------------------------
st.markdown(
    """
    <audio autoplay loop controls style="display:none">
        <source src="bg_music.mp3" type="audio/mp3">
    </audio>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# App Header
# -------------------------------
st.title("🌱 Eco-Scanner 9000™")
st.subheader("Discover how eco-friendly your product really is!")

# -------------------------------
# User guess input
# -------------------------------
guess = st.number_input(
    "Guess your product's eco-friendliness (%)",
    min_value=0, max_value=100, step=1
)

# -------------------------------
# Display Results button
# -------------------------------
if st.button("Show Results"):
    # Example AI-generated eco-score
    eco_score = 75  # Replace this with your AI model output

    # Display eco-score in pastel card
    st.markdown(
        f"""
        <div style='background-color: rgba(193, 240, 246, 0.7); padding: 20px; border-radius: 15px;'>
            🌿 <b>Your product's eco-friendliness:</b> {eco_score}%
        </div>
        """,
        unsafe_allow_html=True
    )

    # Button to check guess accuracy
    if st.button("Check your guess accuracy"):
        accuracy = 100 - abs(eco_score - guess)
        st.markdown(
            f"""
            <div style='background-color: rgba(255, 209, 220, 0.7); padding: 20px; border-radius: 15px;'>
                🎯 <b>Your guess accuracy:</b> {accuracy}%
            </div>
            """,
            unsafe_allow_html=True
        )

    # Button to show AI explanation
    if st.button("Show AI Explanation"):
        explanation = """
        Our AI analyzed your product based on sustainability, resource usage,
        and eco-impact. Higher scores mean greener products! 🌎💚
        """
        st.markdown(
            f"""
            <div style='background-color: rgba(247, 227, 255, 0.7); padding: 20px; border-radius: 15px;'>
                💡 <b>AI Explanation:</b> {explanation}
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------
# Footer
# -------------------------------
st.markdown("Made with ❤️ for a greener future!")
