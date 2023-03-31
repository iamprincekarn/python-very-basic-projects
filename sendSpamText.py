import pyautogui as pg
import time
time.sleep(10)
for i in range(100):
    pg.write(str(i+1) + "Spam message send krna seekh rha hu")
    pg.press("Enter")
  
#iske bd isko jo interface milega wha pe message likhna start kr dega for 100 times, agr whatsapp pr kisi ke chat pe jayega toh usko send hone lgega message
