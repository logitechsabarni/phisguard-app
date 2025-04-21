
# 🛡️ PhishGuard - Email Phishing Detector (Console App)

PhishGuard is a simple AI-powered console application that helps detect phishing emails using basic machine learning and rule-based techniques.

## 🚀 Features

- Detects phishing emails using a trained ML model (Logistic Regression)
- Highlights suspicious keywords (e.g., "click", "verify", "urgent")
- Extracts and displays links from email content
- Provides confidence score and simple recommendations
- Console-based interface (no GUI)

## 📦 Requirements

Install dependencies using pip:

```bash
pip install scikit-learn pandas numpy nltk
```

## 🛠️ How to Run

1. Clone or download this repository.
2. Open terminal and run:

```bash
python phishguard_app.py
```

3. Paste email content when prompted.
4. Type `exit` to quit the program.

## 💡 Example Input

```
Dear user, your email is scheduled for deactivation. Click here http://fake-link.com to prevent it.
```

## 📄 Output Example

- Phishing Risk: High ⚠️
- Confidence: 87.23%
- Suspicious words: click, deactivate
- Links found: http://fake-link.com

## 🧠 ML Model

- Trained using a small sample dataset with `CountVectorizer` and `LogisticRegression`.
- Can be improved by expanding the dataset.

It is a protype only and not a fully functional ML model made by me.
https://phisguard-app-1.onrender.com
