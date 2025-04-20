pip install scikit-learn pandas numpy nltk
phishguard_code = """
import re
import nltk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

nltk.download('punkt')

# Sample dataset (Phishing = 1, Safe = 0)
data = [
    ("Your account has been suspended. Click here to verify.", 1),
    ("Congratulations! You’ve won a $1000 gift card. Click now!", 1),
    ("Please update your bank details immediately.", 1),
    ("Final warning: Your email will be deactivated!", 1),
    ("Meeting rescheduled to Monday, let me know if it works.", 0),
    ("Here’s the project report. Check and revert back.", 0),
    ("Team lunch at 1 PM tomorrow.", 0),
    ("The server maintenance is complete, all systems normal.", 0),
]

# Split data
texts, labels = zip(*data)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(labels)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Optional: evaluate
print("\n[Model Evaluation]")
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# ---- Email Scanner ----
def extract_links(text):
    return re.findall(r'http[s]?://\S+', text)

def highlight_suspicious_words(text):
    suspicious_words = ["urgent", "click", "verify", "login", "password", "update", "deactivate", "suspend"]
    words = nltk.word_tokenize(text.lower())
    flagged = [word for word in words if word in suspicious_words]
    return flagged

def scan_email(email_text):
    vectorized = vectorizer.transform([email_text])
    prediction = clf.predict(vectorized)[0]
    probability = clf.predict_proba(vectorized)[0][1] * 100

    links = extract_links(email_text)
    flagged_words = highlight_suspicious_words(email_text)

    print("\n--- Scan Result ---")
    print(f"Phishing Risk: {'High ⚠️' if prediction == 1 else 'Low ✅'}")
    print(f"Confidence: {probability:.2f}%")

    if flagged_words:
        print(f"\n⚠️ Suspicious words found: {', '.join(set(flagged_words))}")
    if links:
        print(f"\n🔗 Links found:")
        for link in links:
            print(f"  - {link}")

    print("\n🛡️ Recommendation: Be cautious if the email urges immediate action or contains suspicious links.")

# ---- Main Loop ----
while True:
    print("\n📥 Paste the email content below (or type 'exit' to quit):")
    user_input = input(">>> ")
    if user_input.strip().lower() == 'exit':
        break
    scan_email(user_input)
