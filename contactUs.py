from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://devtikitop.linuxtech.io/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    signup_button = browser.find_element(By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    signup_button.click()
    time.sleep(2)

    link = browser.find_elements(By.LINK_TEXT, "Contact Us")[1]
    link.click()
    time.sleep(1)

    # находим элемент, содержащий текст
    text_contact_us_elt = browser.find_element(
        By.XPATH, "//h1[@class='ContactUsForm_title__F_181']")
    # записываем в переменную text_contact_us текст из элемента text_contact_us_elt
    text_contact_us = text_contact_us_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "GET IN TOUCH" == text_contact_us

    first_name = browser.find_element(By.ID, 'name')
    first_name.send_keys("Bobby")
    time.sleep(1)
    email = browser.find_element(By.ID, 'email')
    email.send_keys("qa4@fexbox.org")
    time.sleep(1)
    message = browser.find_element(By.ID, 'message')
    message.send_keys("Hello Hello Hello Hello")
    time.sleep(1)

    # Отправляем заполненную форму
    send_button = browser.find_element(
        By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
