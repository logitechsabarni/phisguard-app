from flask import Flask, render_template_string, request
import random
import time

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>PhishGuard Prototype</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f9;
            color: #333;
        }
        h1 {
            color: #4CAF50;
        }
        textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 5px;
            background-color: #fff;
            max-width: 400px;
        }
        .loading {
            font-size: 24px;
            text-align: center;
            padding: 10px;
        }
        .loading span {
            display: inline-block;
            border-radius: 50%;
            border: 5px solid #4CAF50;
            border-top-color: transparent;
            width: 24px;
            height: 24px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <h1>PhishGuard Email Scanner</h1>
    <form method="POST" action="/scan">
        <label for="email">Paste Email Content:</label><br>
        <textarea name="email" rows="10" cols="50"></textarea><br><br>
        <input type="submit" value="Scan Email">
    </form>
    {% if result %}
        <div class="result">
            <h2>Scan Result: {{ result }}</h2>
        </div>
    {% elif loading %}
        <div class="loading">
            <span></span>
            <p>Scanning...</p>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/scan", methods=["POST"])
def scan():
    email_content = request.form.get("email")

    # Fake scan result using random choice
    loading = True
    time.sleep(2)  # Simulate scanning delay

    result = random.choice([
        "✅ This email looks safe!",
        "⚠️ This email might be a phishing attempt!",
        "🚨 Warning: Suspicious links detected!",
        "🔍 Unable to verify sender, be cautious."
    ])

    return render_template_string(HTML_TEMPLATE, result=result, loading=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
