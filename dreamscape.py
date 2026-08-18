from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "dreamscape"

if __name__ == "__main__":
    # paths to signed cert and rsa key
    app.run(ssl_context=("cert.pem", "key.pem"))