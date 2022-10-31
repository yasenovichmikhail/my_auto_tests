from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element(By.ID, value="treasure")
    treasure = element.get_attribute("valuex")
    x = treasure
    y = calc(x)

    input1 = browser.find_element(By.ID, value='answer')
    input1.send_keys(y)
    
    option1 = browser.find_element(By.ID, value="robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(30)

    browser.quit()

# не забываем оставить пустую строку в конце файла