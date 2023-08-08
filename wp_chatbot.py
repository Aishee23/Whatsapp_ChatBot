import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import pandas as pd
import numpy as np
keyboard = Controller()
si=pd.read_csv("parade1.csv")

def send_whatsapp_message(phno):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no="+91"+phno, 
            message="Happy Independence Day",tab_close=True
        )
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))
no=np.array(si[0])
for num in no:
    send_whatsapp_message(str(num))
