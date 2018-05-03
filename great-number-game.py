from flask import Flask, render_template, redirect
from random import Random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess")
def guess():
    pass

if __name__ == "__main__":
    app.run(debug=True)