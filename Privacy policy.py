from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://devtikitop.linuxtech.io/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()

    Privacy_policy_button = browser.find_element(By.XPATH, "//button[@class='ButtonTermsPrivacy_btn__12u2U ButtonTermsPrivacy_linkFooter__BtSNv'][1]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", Privacy_policy_button)
    time.sleep(2)
    Privacy_policy_button.click()
    time.sleep(2)

    google_services_link = browser.find_element(By.LINK_TEXT, "Google Play Services")
    browser.execute_script("return arguments[0].scrollIntoView(true);", google_services_link)
    time.sleep(2)
    google_services_link.click()
    time.sleep(2)

    new_window_google_services = browser.window_handles[1]
    browser.switch_to.window(new_window_google_services)

    google_services_text_elt = browser.find_element(By.XPATH, "//h1[@class='devsite-page-title']")
    google_services_text = google_services_text_elt.text
    assert "GOOGLE ANALYTICS FOR FIREBASE TERMS OF SERVICE" == google_services_text
    time.sleep(2)
    browser.close()

    main_window = browser.window_handles[0]
    browser.switch_to.window(main_window)
    time.sleep(2)

    google_analytics_link = browser.find_element(By.LINK_TEXT, "Google Analytics for Firebase")
    google_analytics_link.click()
    time.sleep(2)

    new_window_google_analytic = browser.window_handles[1]
    browser.switch_to.window(new_window_google_analytic)

    google_analytics_text_elt = browser.find_element(By.XPATH, "//h1[@class='devsite-page-title']")
    google_analytics_text = google_analytics_text_elt.text
    assert "GOOGLE ANALYTICS FOR FIREBASE TERMS OF SERVICE" == google_analytics_text
    time.sleep(2)
    browser.close()

    browser.switch_to.window(main_window)
    time.sleep(2)

    firebase_link = browser.find_element(By.LINK_TEXT, "Firebase Crashlytics")
    firebase_link.click()
    time.sleep(2)

    new_window_firebase = browser.window_handles[1]
    browser.switch_to.window(new_window_firebase)

    firebase_text_elt = browser.find_element(By.XPATH, "//h1[@class='devsite-page-title']")
    firebase_text = firebase_text_elt.text
    assert "FIREBASE CRASHLYTICS AND FIREBASE APP DISTRIBUTION TERMS OF SERVICE" == firebase_text
    time.sleep(2)
    browser.close()

    browser.switch_to.window(main_window)
    time.sleep(2)

    privacy_policy_close_button = browser.find_element(By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorBlack__4euz_']")
    privacy_policy_close_button.click()
    time.sleep(2)

finally:
    time.sleep(2)
    browser.quit()
