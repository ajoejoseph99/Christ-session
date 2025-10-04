from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>Hello from Cloud Run!</h1><p>This app is running in {os.getenv('K_SERVICE', 'local')} revision {os.getenv('K_REVISION', 'local')}.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
