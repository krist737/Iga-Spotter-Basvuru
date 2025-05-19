from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

URL = "https://www.istairport.com/havalimani/iga-spotter/"

def form_acildi_mi():
    try:
        response = requests.get(URL, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        uyari = soup.find(string=lambda text: text and "Maximum başvuru sayısına ulaşılmıştır" in text)
        return uyari is None
    except:
        return False

@app.route("/")
def ana_sayfa():
    return "✅ Form kontrol servisi çalışıyor!"

@app.route("/durum")
def durum():
    acik = form_acildi_mi()
    return jsonify({"form_acik": acik})

# Render için port ayarı
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
