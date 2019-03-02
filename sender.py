from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
driver.get("https://web.telegram.org/#/login")
x = input("Are You logged in ? y/n: ")
while x:
    if(x == 'y'):
        yes = 'Done'
        with open("ids.txt", "r") as ins:
            array = []
            for line in ins:
                array.append(line)
                driver.get('https://web.telegram.org/#/im?p='+line.rstrip('\n'))
                text = 'Write Your Msg Here...'
                txt = driver.find_element_by_class_name('composer_rich_textarea')
                txt.send_keys('test')
                txt.send_keys(Keys.ENTER)
				print('Finished')

        break
    else:
       x = input("Are You logged in ? y/n: ")


