import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/healthcheck")
def healthcheck():
    return "The app is working!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host="0.0.0.0", port=port)
