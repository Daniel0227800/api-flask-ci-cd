from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, esta API usa CI/CD con GitHub Actions 🚀"

if __name__ == '__main__':
    app.run()
