from flask import Flask, render_template, url_for,request, redirect,flash,session

from flask_session import Session
import sqlite3
from scrap import data,currency
from time import gmtime, strftime


import os
SECRET_KEY = os.urandom(32)




app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] ="filesystem"
Session(app)


con = sqlite3.connect("redd.db")
db = con.cursor()
# con.close()

headers = ("Rank" ,"Name", "Price", "24 hours", "7 days", "Market")

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/login_validation", methods = ["POST"])
def login_validation():
    un = request.form.get("username_l")
    pw = request.form.get("password_l")
    con = sqlite3.connect("redd.db")
    db=  con.cursor()
    db.execute("""SELECT * FROM 'red' WHERE username='{}' """.format(un))
    rows = db.fetchall()
    if len(rows)>0:
        session["user_id"] = rows[0][0]
        return redirect("/history.html")
    else:
        return redirect("home.html")


    print

@app.route("/register", methods = ["POST"])
def register():
    un_r = request.form.get("username_r")
    em_r = request.form.get("email_r")
    pw_r = request.form.get("pw_r")
    con = sqlite3.connect("redd.db")
    db = con.cursor()
    db.execute("INSERT INTO 'red' VALUES (?,?,?)",(un_r,em_r,pw_r))

    con.commit()
    flash("Welcome, now pelase login into your own CryptoBook")
    return render_template("/home.html")


@app.route("/market.html")
def market():
    return render_template("market.html", data =data , header = headers)

@app.route("/sell.html", methods = ["GET", "POST"])
def sell():
    if request.method == "GET":
        return render_template("sell.html", data=currency)

    else:
        con = sqlite3.connect("redd.db")
        db = con.cursor()
        name = request.form.get("something")
        value = request.form.get("crypto_amount_sell")
        amount = 20
        day = strftime("%d %b %Y", gmtime())
        time = strftime("%H:%M:%S",gmtime())
        sell ="Sell"
        db.execute("INSERT INTO 'sell' VALUES (?,?,?,?,?,?)",(name,amount, value,day,time,sell))
        con.commit()
        return redirect("/history.html")

@app.route("/buy.html", methods = ["GET", "POST"])
def buy():

    if request.method == "GET":
        return render_template("buy.html",data =currency)
    else:
        con = sqlite3.connect("redd.db")
        db = con.cursor()
        name = request.form.get("something")
        value = request.form.get("crypto_amount")
        amount = 20
        day = strftime("%d %b %Y", gmtime())
        time = strftime("%H:%M:%S", gmtime())
        status = "Buy"
        db.execute("INSERT INTO 'buy' VALUES (?,?,?,?,?,?)",(name,amount, value,day, time, status))
        con.commit()
        return redirect("/history.html")



@app.route("/history.html")
def history():
    def buy():
        con = sqlite3.connect("redd.db")
        db = con.cursor()
        db.execute("""SELECT * FROM 'buy' ORDER BY Day,Hour""")
        items = db.fetchall()
        # for item in items:
        #     xd.append(item)
        return items

    def sell():
        con = sqlite3.connect("redd.db")
        db = con.cursor()
        db.execute("""SELECT * FROM 'sell' ORDER BY Day,Hour""")
        items = db.fetchall()
        # for item in items:
        #     xd.append(item)
        return items

    some = buy()
    so = sell()
    lol = []
    for somes in some:
        lol.append(somes)
    for xd in so:
        lol.append(xd)

    loll = sorted(lol, key=lambda x: (x[4], x[3]))
    print(loll)

    return render_template("history.html",data = loll)

@app.route("/chart.html")
def chart():
    return render_template("chart.html", data= currency)
@app.route("/logout")
def logout():
    # session.pop("user_id")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)