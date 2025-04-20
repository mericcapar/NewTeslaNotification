import pyautogui
import time

print("Fareyi istediğin yere getir, Command+C ile çık.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x} | Y: {y}", end='\r')  
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nKoordinat okuma durduruldu.")
