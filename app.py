from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, esta API usa CI/CD con GitHub Actions 🚀"

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)