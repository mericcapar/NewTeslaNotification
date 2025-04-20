import pyautogui
import time
import webbrowser
import pyperclip

# 1. Tarayıcıyı aç ve siteye git
webbrowser.open("https://www.tesla.com/tr_tr")
time.sleep(5)  # Sayfanın yüklenmesini bekle

# 2. "Envanteri Keşfedin" butonunun olduğu konuma git
# Bu kısımdaki koordinatları senin ekranına göre ayarlaman gerekir
pyautogui.moveTo(555, 850, duration=1)  # örnek koordinat
pyautogui.click()


time.sleep(6)

# 3. Sayfanın tümünü seç ve kopyala (Command+A, Command+C)
pyautogui.hotkey('command', 'a')
time.sleep(1)
pyautogui.hotkey('command', 'c')
time.sleep(1)
pyautogui.hotkey('command','w')

page_text = pyperclip.paste()

# 5. İçerikte Model Y var mı kontrol et
if "Model Y" in page_text:
    print("✅ Aranan araç mevcut.")
else:
    print("❌ Henüz stok gelmedi.")
