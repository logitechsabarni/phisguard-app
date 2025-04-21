pip install Flask scikit-learn numpy nltk plotly
import re
import nltk
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import plotly.express as px
import plotly.io as pio

# Initialize Flask app
app = Flask(__name__)

# Initialize NLTK
nltk.download('punkt')

# Sample dataset
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

texts, labels = zip(*data)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Track scan history
scan_history = []

# Helper functions for phishing detection
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

    scan_result = {
        "prediction": "High ⚠️" if prediction == 1 else "Low ✅",
        "confidence": f"{probability:.2f}%",
        "flagged_words": ', '.join(set(flagged_words)),
        "links": links
    }

    scan_history.append(scan_result)
    return scan_result

# Route for scanning emails
@app.route('/scan', methods=['POST'])
def scan():
    email_text = request.form['email_text']
    scan_result = scan_email(email_text)
    return render_template('result.html', scan_result=scan_result)

# Route for displaying dashboard
@app.route('/')
def dashboard():
    # Create a pie chart
    phishing_count = sum([1 for result in scan_history if result['prediction'] == "High ⚠️"])
    safe_count = len(scan_history) - phishing_count
    labels = ['Phishing', 'Safe']
    values = [phishing_count, safe_count]

    fig = px.pie(names=labels, values=values, title='Phishing vs Safe Emails')
    graph_html = pio.to_html(fig, full_html=False)

    return render_template('dashboard.html', scan_history=scan_history, graph_html=graph_html)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
