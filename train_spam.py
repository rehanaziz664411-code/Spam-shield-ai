import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# --- 1. DATA PREPARATION ---
# Example dataset (Spam vs Ham)
data = {
    'text': [
        'Get a free iPhone now! Click here', 
        'Hey, are we still meeting for lunch?', 
        'URGENT: Your account has been suspended. Verify now', 
        'Can you send me the report by 5 PM?', 
        'WINNER! You have won a $1000 cash prize',
        'Call me when you are free'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}
df = pd.DataFrame(data)

# --- 2. NLP PIPELINE ---
tfidf = TfidfVectorizer(stop_words='english', lowercase=True)
X = tfidf.fit_transform(df['text'])
y = df['label']

# --- 3. MODEL TRAINING ---
model = MultinomialNB()
model.fit(X, y)

# --- 4. SAVE ASSETS ---
with open('spam_model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf, f)

print(" Email Spam AI Trained!")
