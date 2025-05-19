
from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    durum = "Açık"
    email_list = []
    
    if os.path.exists("emails.txt"):
        with open("emails.txt", "r") as f:
            email_list = [line.strip() for line in f.readlines()]
    
    if "maksimum" in email_list:
        durum = "Kapalı"
    
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        if email:
            with open("emails.txt", "a") as f:
                f.write(f"{email}\n")

    return render_template("index.html", durum=durum)
