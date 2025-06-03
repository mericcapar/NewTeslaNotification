import time
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

target_models = ["Arkadan İtiş", 'arkadan itiş', 'Arkadan Itiş','Arkadan Çekiş', 'Arkadan çekiş', 'arkadan çekiş']

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(url, params=params)
    return response.json()

while True:
    print("Sayfa kontrol ediliyor...")

    try:
        response = requests.get("https://www.tesla.com/tr_tr", timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        found_models = [model for model in target_models if model in page_text]

        if found_models:
            for model in found_models:
                send_telegram_message(f"{model} modeli mevcut!")
        else:
            print("Stok yok")

    except Exception as e:
        print("Hata oluştu:", e)

    print("Yarım saat sonra tekrar kontrol edilecek...\n")
    time.sleep(1800)  # 30 dakika
