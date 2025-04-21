
 🛡️ PhishGuard - Email Phishing Detector (Console App)

PhishGuard is a simple AI-powered console application that helps detect phishing emails using basic machine learning and rule-based techniques.

🚀 Features

- Detects phishing emails using a trained ML model (Logistic Regression)
- Highlights suspicious keywords (e.g., "click", "verify", "urgent")
- Extracts and displays links from email content
- Provides confidence score and simple recommendations
- Console-based interface (no GUI)

 📦 Requirements

Install dependencies using pip:

bash
pip install scikit-learn pandas numpy nltk


 🛠️ How to Run

1. Clone or download this repository.
2. Open terminal and run:

bash
python phishguard_app.py


3. Paste email content when prompted.
4. Type `exit` to quit the program.

💡 Example Input


Dear user, your email is scheduled for deactivation. Click here http://fake-link.com to prevent it.


📄 Output Example

- Phishing Risk: High ⚠️
- Confidence: 87.23%
- Suspicious words: click, deactivate
- Links found: http://fake-link.com (A similar prototype which I have generated below and it generates almost similar types of messages only).

🧠 ML Model

- Trained using a small sample dataset with `CountVectorizer` and `LogisticRegression`.
- Can be improved by expanding the dataset.

It is a protype only and not a fully functional ML model.
The link to this prototype app is:
https://phisguard-app-1.onrender.com


Absolutely! Here's a polished message you can paste directly into your **README.md** under a section like `## Disclaimer & Future Scope`:

⚠️ Disclaimer & 🚀 Future Scope

 PhishGuard is currently a prototype built for demonstration purposes during a hackathon. The app stimulates phishing detection using randomly generated results to showcase the intended functionality and user experience because the detection requires highly advanced technology and it is going to take some time to built it completely. A fully functional machine learning model is currently under development to provide real-time phishing detection and enhanced email safety.

🔮 Future Potential:
In its full version, PhishGuard is envisioned to:
- Use a trained machine learning model for accurate phishing detection.
- Analyze email content** and detect suspicious links, fake domains, and sender impersonation.
- Warn users about fraudulent payment links or fake OTP/payment gateways.
- Offer browser extension support and email client integration.
- Maintain a real-time database of phishing sources and deliver timely warnings.

This prototype demonstrates the core vision of the project and lays the groundwork for future development.
Lastly the website which focuses on its future uses is given below:
https://aisite.10web.io/56/usually-capable-bull/
It is an overall website which can be published for future uses which tells us about its uses and what purposes this app will serve in the near future.



