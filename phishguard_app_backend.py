pip install flask scikit-learn pandas numpy nltk
from flask import Flask, render_template, request, jsonify
import re
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')

app = Flask(__name__)

# Sample dataset (phishing = 1, safe = 0)
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

# Prepare data
texts, labels = zip(*data)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(labels)

# Train model
model = LogisticRegression()
model.fit(X, y)

# Helper functions
def extract_links(text):
    return re.findall(r'http[s]?://\S+', text)

def highlight_suspicious_words(text):
    suspicious_words = ["urgent", "click", "verify", "login", "password", "update", "deactivate", "suspend"]
    words = nltk.word_tokenize(text.lower())
    return [word for word in words if word in suspicious_words]

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    email_text = request.form.get('emailText', '')
    vectorized = vectorizer.transform([email_text])
    prediction = model.predict(vectorized)[0]
    probability = model.predict_proba(vectorized)[0][1] * 100

    links = extract_links(email_text)
    flagged_words = highlight_suspicious_words(email_text)

    result = {
        "phishing": bool(prediction),
        "confidence": f"{probability:.2f}",
        "flagged_words": flagged_words,
        "links": links
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
