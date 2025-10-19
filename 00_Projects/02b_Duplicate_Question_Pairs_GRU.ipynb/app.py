import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ---------------------------
# Load Model and Tokenizer
# ---------------------------
@st.cache_resource
def load_all():
    model = load_model("GRU_model.keras")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

model, tokenizer = load_all()
MAX_LEN = 30

# ---------------------------
# App Design
# ---------------------------
st.set_page_config(page_title="Duplicate Question Detector", page_icon="❓", layout="wide")

st.markdown(
    """
    <style>
    body { background-color: #0e1117; color: #fafafa; }
    .main { background-color: #111418; padding: 2rem; border-radius: 1rem; }
    .title { font-size: 2rem; font-weight: 700; text-align: center; color: #4ade80; }
    .subtitle { text-align: center; color: #a3a3a3; margin-bottom: 2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">🤖 Quora Duplicate Question Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detect whether two questions have the same meaning using a GRU Deep Learning model</div>', unsafe_allow_html=True)

# ---------------------------
# Input Form
# ---------------------------
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    q1 = st.text_area("Enter Question 1:", placeholder="e.g., How can I learn Python easily?")
    q2 = st.text_area("Enter Question 2:", placeholder="e.g., What is the best way to learn Python?")
    submit = st.button("🔍 Check Similarity")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# Prediction Logic
# ---------------------------
def predict_duplicate(q1, q2):
    q1_seq = tokenizer.texts_to_sequences([q1])
    q2_seq = tokenizer.texts_to_sequences([q2])

    q1_pad = pad_sequences(q1_seq, maxlen=MAX_LEN, padding='post')
    q2_pad = pad_sequences(q2_seq, maxlen=MAX_LEN, padding='post')

    prob = model.predict([q1_pad, q2_pad])[0][0]
    label = "Duplicate" if prob > 0.5 else "Not Duplicate"
    return prob, label

# ---------------------------
# Output Display
# ---------------------------
if submit:
    if q1.strip() == "" or q2.strip() == "":
        st.warning("Please enter both questions before submitting.")
    else:
        with st.spinner("Analyzing..."):
            prob, label = predict_duplicate(q1, q2)

        st.success(f"**Prediction:** {label}")
        st.metric(label="Similarity Score", value=f"{prob:.4f}")

        if label == "Duplicate":
            st.info("These questions mean almost the same thing.")
        else:
            st.warning("These questions likely have different meanings.")

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using Streamlit and Deep Learning (GRU)</p>",
    unsafe_allow_html=True
)
