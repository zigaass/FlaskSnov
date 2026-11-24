from flask import Flask, render_template, request 
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ljubezen", methods = ["POST"])
def love_calc():
    print(request.form)
    i1=request.form["ime1"]
    i2=request.form["ime2"]
    pr = 0
    if ime1.lower() == ime2.lower():
            random.randint(100,100)
            komentar= "Samoljublje"
    if i1.strip().lower() == "žiga" or i2.strip().lower() == "žiga":
        pr = random.randint(90,100)
    elif i1.strip().lower() == "grega" or i2.strip().lower() == "grega":
        pr = random.randint(0,10)
    else:
        pr = random.randint(0,100)
    if pr < 30:
        komentar = "Pozabi"
    elif pr < 70:
        komentar = "Morda"
    else:
        komentar = "Poroka!"

    return render_template("index.html", ime1= i1, ime2 = i2, p = pr, komentar=komentar)

app.run(debug = True)