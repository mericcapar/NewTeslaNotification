import pyautogui
import pyperclip
import time
import webbrowser
import requests
import os
from dotenv import load_dotenv

load_dotenv()

target_models= ["Arkadan İtiş", 'arkadan itiş', 'Arkadan Itiş','Arkadan Çekiş', 'Arkadan çekiş', 'arkadan çekiş']

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID1')

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(url, params=params)
    return response.json()

while True:
    webbrowser.open("https://tesla.com/tr_tr")
    time.sleep(10)
    pyautogui.moveTo(550,850, duration=1)
    pyautogui.click()

    time.sleep(5)

    pyautogui.hotkey('command','a')
    time.sleep(1)
    pyautogui.hotkey('command','c')
    time.sleep(1)
    pyautogui.hotkey('command','w')

    page_text = pyperclip.paste()

    found_models = [model for model in target_models if model in page_text]

    if found_models:
        for model in found_models:
            send_telegram_message(f"{model} modeli mevcut!")
    else:
        print("Stok yok")

    print("Yarim saat sonra tekrar kontrol edilecek...")
    time.sleep(600)

