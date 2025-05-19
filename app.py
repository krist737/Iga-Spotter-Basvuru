from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            # E-postayı bir dosyaya kaydet (isteğe bağlı)
            with open("emails.txt", "a") as f:
                f.write(email + "\n")
            return "Başvuru alındı, teşekkürler!"
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render bunu bekliyor
    app.run(host="0.0.0.0", port=port)
