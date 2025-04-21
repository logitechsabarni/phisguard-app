pip install flask
from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

# HTML and JS combined in a string
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>PhishGuard Prototype</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 2em;
      max-width: 600px;
      margin: auto;
    }
    .prototype-disclaimer {
      background: #fff3cd;
      color: #856404;
      border: 1px solid #ffeeba;
      padding: 0.75em;
      border-radius: 4px;
      margin-bottom: 1em;
      font-size: 0.95rem;
    }
    input, button {
      width: 100%;
      margin-top: 0.5em;
      padding: 0.7em;
      font-size: 1rem;
    }
    #result {
      margin-top: 1em;
      font-weight: bold;
      font-size: 1.1rem;
    }
  </style>
</head>
<body>

  <h2>PhishGuard</h2>
  <div class="prototype-disclaimer">
    ⚠️ <strong>Prototype only:</strong> The scan feature is currently simulated for demonstration purposes. Real-time phishing detection will be integrated in a future update.
  </div>

  <input
    type="text"
    id="email-input"
    placeholder="Enter email or URL to scan"
  />
  <button id="scan-btn">Scan Email</button>

  <div id="result"></div>

  <script>
    document.getElementById('scan-btn').addEventListener('click', async () => {
      const resultEl = document.getElementById('result');
      const userInput = document.getElementById('email-input').value.trim();

      if (!userInput) {
        resultEl.textContent = '❗ Please enter a valid email or URL.';
        return;
      }

      resultEl.textContent = '🔍 Scanning…';

      try {
        const res = await fetch('/scan', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ input: userInput })
        });

        const data = await res.json();
        resultEl.textContent = data.verdict;
      } catch (err) {
        resultEl.textContent = '❌ Error: Could not connect to scanner.';
      }
    });
  </script>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    user_input = data.get('input', '')

    # Log the input (optional)
    print(f"User input received: {user_input}")

    # Simulated phishing verdicts
    verdicts = [
        '✅ Safe to proceed!',
        '⚠️ Warning: This could be a phishing link!',
        '🔒 Suspicious content detected – proceed with caution.'
    ]

    return jsonify({ 'verdict': random.choice(verdicts) })

if __name__ == '__main__':
    app.run(debug=True)
