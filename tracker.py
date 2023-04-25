import os
import time
import requests
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://web.whatsapp.com') 
input('Choose Contact then press ENTER')

action = webdriver.ActionChains(driver)



status_element_xpath = '/html/body/div[1]/div/div/div[5]/div/header/div[2]/div[2]'
try:        # Get contact header if possible
    name_element_xpath = '/html/body/div[1]/div/div/div[5]/div/header/div[2]/div'
    target = driver.find_element("xpath", name_element_xpath)
except:
    target = "Unkown"
current_status = 0


def isOnline():
    # global target
    try:
        element = driver.find_element("xpath", status_element_xpath)
        # print(element.text)
        print(f'[*] Status: Online  [{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]')
        return True
    except Exception as e:
        print(f'[*] Status: Offline [{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]')
        #print(e)
        return False
    
    
  
def calculate_time(t):
    if t < 60:
        return(str(t)+' s')
    else:
        return(str(t // 60)+' m')
    
while(True):
    time.sleep(2)
    xoffset = random.randint(0,2)
    yoffset = random.randint(0,2)
    action.move_by_offset(xoffset,yoffset).perform()    # to make sure browser process doesn't sleep
    # print(f"[*] Mouse Moved: {xoffset},{yoffset}")
    if isOnline() and current_status == 0:
        print('"' + target.text + '" Went Online [' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ']')
        time_1 = time.time()
        current_status = 1
    if not isOnline() and current_status == 1:
        time_2 = time.time()
        time_interval = time_2 - time_1
        print('"' + target.text + '" Went Offline [' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '][' + str(time_interval) + ' S]')
        current_status = 0
    action.move_by_offset(-xoffset,-yoffset).perform()
    
        


    
    


