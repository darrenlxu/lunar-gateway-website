from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/more")

def more():
    return render_template("more.html")

@app.route("/updates")
def updates():
    return render_template("updates.html")

if __name__ == "__main__":
    app.run()
