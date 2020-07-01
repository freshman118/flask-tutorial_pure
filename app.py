from flask import Flask, request, render_template, redirect, url_for, flash
import MySQLdb
from db import get_db

app = Flask(__name__)
app.secret_key = "uiouoiueoirq"


@app.route('/index')
def index():
    return 'Index page'


@app.route("/test")
def test():
    return redirect(url_for("index"))


@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        message = None
        po_username = request.form.get("username")
        po_password = request.form.get("password")
        db = get_db()
        db.execute('SELECT * FROM user WHERE username = "%s"' % po_username)
        db_user = db.fetchone()

        if not db_user or po_password != db_user[2]:
            message = "Password or username is error"
        if not message:
            return redirect(url_for("index"))

        flash(message)

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
