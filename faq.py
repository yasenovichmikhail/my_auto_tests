from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://devtikitop.linuxtech.io/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    link = browser.find_element(By.LINK_TEXT, "FAQ")
    link.click()
    time.sleep(1)

    question1_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][1]")
    question1_open.click()
    time.sleep(1)

    question1_close = browser.find_element(
        By.XPATH, "//summary[@class='FaqInfoItem_faqSummary__eKNYE'][1]")
    question1_close.click()
    time.sleep(1)

    question2_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][2]")
    question2_open.click()
    time.sleep(1)

    question2_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][2]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question2_close.click()
    time.sleep(1)

    question3_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][3]")
    question3_open.click()
    time.sleep(1)

    question3_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][3]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question3_close.click()
    time.sleep(1)

    question4_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][4]")
    question4_open.click()
    time.sleep(1)

    question4_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][4]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question4_close.click()
    time.sleep(1)

    question5_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][5]")
    question5_open.click()
    time.sleep(1)

    question5_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][5]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question5_close.click()
    time.sleep(1)

    question6_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][6]")
    question6_open.click()
    time.sleep(1)

    question6_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][6]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question6_close.click()
    time.sleep(1)

    question7_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][7]")
    question7_open.click()
    time.sleep(1)

    question7_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][7]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question7_close.click()
    time.sleep(1)

    question8_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][8]")
    question8_open.click()
    time.sleep(1)

    question8_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][8]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question8_close.click()
    time.sleep(1)

    #button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
    # button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
