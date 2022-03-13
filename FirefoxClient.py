import time
import Additional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Additional import getnamebox


def getlastmessage(driver):
    return driver.find_elements(By.CSS_SELECTOR, '.message--CeFIW')[-1].text if len(driver.find_elements(By.CSS_SELECTOR, '.message--CeFIW')) > 0 else ''


def clickrequired(driver, name, namebox):
    name_form = driver.find_element(By.ID,
                                    namebox)  # Нужно ID ссылки конференции засовывать в строку
    name_form.send_keys(name)

    button_join = driver.find_element(By.ID, 'room-join')
    button_join.click()

    time.sleep(5)

    button_listen = driver.find_element(By.CSS_SELECTOR, "[aria-label='Только слушать']")
    button_listen.click()


def join(link, name):
    driver = webdriver.Firefox()
    driver.get(link)

    try:
        clickrequired(driver, name, getnamebox(link))
    except:
         pass
    LastMessage = getlastmessage(driver)
    while LastMessage.lower() not in ['до свидания', 'всего доброго']:
        time.sleep(3)
        LastMessage = getlastmessage(driver)

    Chat_Box = driver.find_element(By.CSS_SELECTOR, '#message-input')
    Chat_Box.send_keys(Additional.saygoodbye())

    Send_Button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div[3]/section/div/form/div[1]/button/span[1]')
    Send_Button.click()

    teardown(driver)


def teardown(driver):
    driver.close()


join('https://bbb.ssau.ru/b/gew-x5n-wxi-tcd', 'Маркелов')

