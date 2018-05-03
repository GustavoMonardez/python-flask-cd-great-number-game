from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    if not "rand_num" in session:
        session["rand_num"] = random.randrange(1, 101)
    if not "display_box" in session:
        session["display_box"] = "invisible"     
    if not "msg" in session:
        session["msg"] = ""   
    if not "play_again" in session:
        session["play_again"] = "invisible"   
    if not "guess-form" in session:
        session['guess-form'] = "guess-form"
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():    
    guess = request.form["guess"]
    print("rand:", session["rand_num"])
    print("guess", guess)
    if int(guess) == session["rand_num"]:
        session["display_box"] = "success"
        session["msg"] = guess + " was the number!"
        session["play_again"] = "play-again"
        session['guess-form'] = "invisible"
        print(guess, " was the number!")
    elif int(guess) > session["rand_num"]:
        session["display_box"] = "danger"
        session["msg"] = "Too high!"
        print("Too high!")
    else:
        session["display_box"] = "danger"
        session["msg"] = "Too low!"
        print("Too low!")
    
    return redirect("/")

@app.route("/play_again", methods=["POST"])
def play_again():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)