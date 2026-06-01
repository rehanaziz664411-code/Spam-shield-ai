import streamlit as st
import pickle

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="AI Spam Shield", page_icon="")

# Load Assets
@st.cache_resource
def load_nlp_assets():
    with open('spam_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    return model, tfidf

model, tfidf = load_nlp_assets()

# --- 2. UI ---
st.title(" AI Email & SMS Spam Shield")
st.write("Paste a message below to check if it's safe or a scam.")

message_input = st.text_area("Enter Message Content:", height=150, placeholder="e.g., Congratulations! You've won a gift card...")

if st.button("Analyze Message 🔍"):
    if message_input.strip():
        # Transform input
        data_vectorized = tfidf.transform([message_input])
        
        # Predict
        prediction = model.predict(data_vectorized)[0]
        probability = model.predict_proba(data_vectorized).max()
        
        st.divider()
        if prediction == 'spam':
            st.error(f" ALERT: THIS MESSAGE IS SPAM!")
            st.write(f"Confidence Level: **{probability*100:.2f}%**")
            st.warning("Action: Do not click any links or share personal info.")
        else:
            st.success(f" CLEAR: THIS MESSAGE IS SAFE (HAM)")
            st.write(f"Confidence Level: **{probability*100:.2f}%**")
    else:
        st.warning("Please enter a message to scan.")

# --- 3. FOOTER ---
st.sidebar.info("This AI uses Multinomial Naive Bayes and TF-IDF Vectorization to detect linguistic patterns common in phishing and spam attacks.")
