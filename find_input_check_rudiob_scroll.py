from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, value="input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, value='answer')
    input1.send_keys(y)
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    option1 = browser.find_element(By.ID, value="robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, value="robotsRule")
    option2.click()
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(30)

    browser.quit()

# не забываем оставить пустую строку в конце файла
