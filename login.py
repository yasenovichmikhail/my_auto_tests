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

    login_tab = browser.find_element(By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")
    login_tab.click()
    time.sleep(1)

    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("qa@fexbox.org")
    time.sleep(1)

    input_password = browser.find_element(By.NAME, "password")
    input_password.send_keys("qwertyasd")
    time.sleep(1)

    login_button = browser.find_element(By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")
    login_button.click()
    time.sleep(2)

    auth_text_elt = browser.find_element(By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK ButtonHeaderProfile_button__756EG']")
    auth_text = auth_text_elt.text
    assert "Profile" == auth_text

    profile_button = browser.find_element(By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK ButtonHeaderProfile_button__756EG']")
    profile_button.click()
    time.sleep(2)

    my_profile_button = browser.find_element(By.XPATH, "//li[@class='ModalButtonProfile_item__FhMKh'][1]")
    my_profile_button.click()
    time.sleep(2)

    your_profile_text_elt = browser.find_element(By.XPATH, "//h2[@class='AccountComponent_title__gZO_n']")
    your_profile_text = your_profile_text_elt.text
    assert "YOUR PROFILE" == your_profile_text
    time.sleep(2)

    logout_button = browser.find_element(By.XPATH, "//button[@class='ButtonLogOut_btn__Loorl ButtonLogOut_typeAccount__awNPC']")
    logout_button.click()
    time.sleep(2)

    logout_confirm_button = browser.find_element(By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3 CustomButton_typeModalAsk__sQjdZ']")
    logout_confirm_button.click()
    time.sleep(2)

    signup_text_elt = browser.find_element(By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    signup_text = signup_text_elt.text
    assert "Sign Up" == signup_text
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
