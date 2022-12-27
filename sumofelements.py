from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def sum(x, z):
    return x + z

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, value="num1")
    x = int(num1.text)
    num2 = browser.find_element(By.ID, value="num2")
    z = int(num2.text)
    y = sum(x, z)
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))
    
    #input1 = browser.find_element(By.ID, value='answer')
    #input1.send_keys(y)
    
    #option1 = browser.find_element(By.ID, value="robotCheckbox")
    #option1.click()

    #option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    #option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(10)

    browser.quit()

# не забываем оставить пустую строку в конце файла