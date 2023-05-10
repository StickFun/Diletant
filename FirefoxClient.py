import time
import Additional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Additional import getnamebox
from datetime import datetime


def getlastmessage(driver):
    #https://stackoverflow.com/questions/27003423/staleelementreferenceexception-on-python-selenium
    # ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    # last_message = WebDriverWait(driver, 1, ignored_exceptions=ignored_exceptions) \
    #     .until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.message--CeFIW')[-1]))
    return driver.find_elements(By.CSS_SELECTOR, '.message--CeFIW')[-1].text if len(driver.find_elements(By.CSS_SELECTOR, '.message--CeFIW')) > 0 else ''



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

    Send_Button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div[3]/section/div/form/div[1]/button/span[1]')

    Send_Button.click()

    lastmessage = getlastmessage(driver)

    time.sleep(5)
    while lastmessage.lower() not in ['до свидания', 'всего доброго']:
        time.sleep(1)
        lastmessage = getlastmessage(driver)

    # Bye moment
    Chat_Box.send_keys(Additional.saygoodbye())
    Send_Button.click()

    teardown(driver)


def teardown(driver):
    driver.close()




while  time.localtime().tm_hour != 15 or time.localtime().tm_min < 15:
    pass
join('https://bbb.ssau.ru/b/n9g-cjr-2ux', '6303 Сычев Сергей')
