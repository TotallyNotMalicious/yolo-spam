from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import os
import time
import random

def main(code, message, delay):
    times_sent = 0
    while True:     
        url = f'https://onyolo.com/m/{code}'
        
        options = Options()
        options.headless = False
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = wd.Chrome('chromedriver.exe', options=options)
    
        driver.get(url)
        os.system('cls')
        driver.find_element_by_id('text').send_keys(message)
        driver.find_element_by_id('send-button').click()
        driver.close()
        times_sent += 1
        print(f'Sent {times_sent} Times Successfully')
        time.sleep(delay)

def getthegoodies():
    os.system('title Yolo Spammer')
    os.system('cls')
    code = input('Yolo Code: ') # https://onyolo.com/m/THE-YOLO-CODE
    os.system('cls')
    message = input('Message To Spam: ')
    os.system('cls')
    delay = int(input('Delay Between Messages (seconds): ')) # because we're civil people
    os.system('cls')
    main(code, message, delay)

getthegoodies()