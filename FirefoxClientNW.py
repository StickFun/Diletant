import time
import Additional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Additional import getnamebox
from datetime import datetime


def getlastmessage(driver):
    return driver.find_elements(By.CSS_SELECTOR, '.message--CeFIW')[-1].text if len(driver.find_elements(By.CSS_SELECTOR, '.message--CeFIW')) > 0 else ''

def getLastName(driver):
    return driver.find_elements(By.CSS_SELECTOR, '.messageList--2kDQeQ')[-1].text if len(driver.find_elements(By.CSS_SELECTOR, '.messageList--2kDQeQ')) > 0 else ''

def clickrequired(driver, name, namebox):
    name_form = driver.find_element(By.ID,
                                    namebox)
    name_form.send_keys(name)
    button_join = driver.find_element(By.CSS_SELECTOR, '#room-join')
    button_join.click()

    button_presence = driver.find_elements(By.CSS_SELECTOR, "[aria-label='Только слушать']")
    while len(button_presence) < 1:
        time.sleep(5)
        button_presence = driver.find_elements(By.CSS_SELECTOR, "[aria-label='Только слушать']")

    button_listen = driver.find_element(By.CSS_SELECTOR, "[aria-label='Только слушать']")
    button_listen.click()


def join(link, name):
    driver = webdriver.Firefox()
    driver.get(link)

    try:
        clickrequired(driver, name, getnamebox(link))
    except:
         pass

    time.sleep(5)

    Chat_Box = driver.find_element(By.CSS_SELECTOR, '#message-input')
    Chat_Box.send_keys('Здравствуйте')

    Send_Button = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/main/section/div[3]/section/div/form/div[1]/button/span[1]')

    Send_Button.click()

    lastmessage = getlastmessage(driver)

    c = 0
    while lastmessage.lower() not in ['до свидания', 'всего доброго']:
        if lastmessage == '+':
            groupId = getLastName(driver)[0:4] == '6303'
            c += 1 if groupId else 0
            start_time = datetime.time()
        if datetime.time() - start_time 
        lastmessage = getlastmessage(driver)

    # Bye moment
    #Chat_Box.send_keys(Additional.saygoodbye())
    #Send_Button.click()

    teardown(driver)


def teardown(driver):
    driver.close()



join('https://bbb.ssau.ru/b/yez-jqa-ujc', '6303 Сычев Сергей')
'''
while time.localtime().tm_hour != 8:
    pass
join('https://bbb.ssau.ru/b/cry-hlj-c69-cor', '6303 Сычев Сергей')
while time.localtime().tm_hour != 9 or time.localtime().tm_min < 45:
    pass
join('https://bbb.ssau.ru/b/nmj-iqj-pbs-oan', '6303 Сычев Сергей')
'''