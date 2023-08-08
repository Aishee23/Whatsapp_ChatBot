import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import pandas as pd
import numpy as np
keyboard = Controller()
si=pd.read_csv("parade.csv",header=None)
def send_whatsapp_message(phno,msg):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phno,             
            message=msg,
            tab_close=True
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
ms=str(input("Enter message to send : "))
for num in no:
    if num.startswith("+91"):
        send_whatsapp_message(str(num),ms)
    else:
        send_whatsapp_message("+91"+str(num),ms)
