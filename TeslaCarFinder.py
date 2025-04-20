import pyautogui
import pyperclip
import time
import webbrowser
import requests
import os
from dotenv import load_dotenv

load_dotenv()

target_model = "Model Y"

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
    webbrowser.open("https://tesla.com/tr_tr")
    time.sleep(5)
    pyautogui.moveTo(550,850, duration=1)
    pyautogui.click()

    time.sleep(5)

    pyautogui.hotkey('command','a')
    time.sleep(1)
    pyautogui.hotkey('command','c')
    time.sleep(1)
    pyautogui.hotkey('command','w')

    page_text = pyperclip.paste()

    if target_model in page_text:
        send_telegram_message(f"{target_model} mevcut!")
    else:
        send_telegram_message(f"{target_model} için henüz stok gelmedi!")

    print("2 saat sonra tekrar kontrol edilecek...")
    time.sleep(7200)

