from flask import Flask

app = Flask(__name__)

# Test!
@app.route("/")
def home():
    return "Hi Lins!"
