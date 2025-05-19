from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

URL = "https://www.istairport.com/havalimani/iga-spotter/"

def form_acildi_mi():
    try:
        response = requests.get(URL, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        uyari = soup.find(string=lambda text: text and "Başvurular en üst sınıra ulaşmıştır" in text)
        return uyari is None  # Uyarı yoksa form açılmıştır
    except:
        return False  # Hata varsa form kapalı varsay

@app.route("/")
def ana_sayfa():
    return "✅ Form kontrol servisi çalışıyor!"

@app.route("/durum")
def durum():
    acik = form_acildi_mi()
    return jsonify({"form_acik": acik})
