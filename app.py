pip install flask scikit-learn pandas numpy nltk
from flask import Flask, request, render_template_string
import re
import nltk
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Sample dataset (Phishing = 1, Safe = 0)
data = [
    ("Your account has been suspended. Click here to verify.", 1),
    ("Congratulations! You’ve won a $1000 gift card. Click now!", 1),
    ("Please update your bank details immediately.", 1),
    ("Meeting rescheduled to Monday, let me know if it works.", 0),
    ("Here’s the project report. Check and revert back.", 0),
]

# Train model
texts, labels = zip(*data)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(labels)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = LogisticRegression()
clf.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template_string(open('index.html').read())

@app.route('/scan_email', methods=['POST'])
def scan_email():
    email_content = request.form['email_content']
    prediction = clf.predict(vectorizer.transform([email_content]))[0]
    probability = clf.predict_proba(vectorizer.transform([email_content]))[0][1] * 100
    
    # HTML response based on prediction
    result = f"<h3>Phishing Risk: {'High ⚠️' if prediction == 1 else 'Low ✅'}</h3>"
    result += f"<p>Confidence: {probability:.2f}%</p>"
    
    if prediction == 1:
        result += "<p>⚠️ This email seems suspicious. Be cautious.</p>"
    else:
        result += "<p>✅ This email appears to be safe.</p>"

    return result

if __name__ == '__main__':
    app.run(debug=True)
