from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")

#Countdown page - "Gateway Countdown"
def home():
    return render_template("home.html")

@app.route("/more")

#Second page - "More about Gateway"
def more():
    return render_template("more.html")

@app.route("/updates")

#Third page - "All updates"
def updates():
    return render_template("updates.html")


if __name__ == "__main__":
    app.run()
