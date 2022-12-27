from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://devtikitop.linuxtech.io/"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    boost_your_tiktok = browser.find_element(
        By.XPATH, "//section[@class='container HeaderOffer_headerOffer__0Nk4c']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", boost_your_tiktok)

    get_more_info1_button = browser.find_element(
        By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed__y2rlJ']")
    time.sleep(2)
    get_more_info1_button.click()
    time.sleep(2)
    make_your_order_text_elt = browser.find_element(
        By.XPATH, "//h2[@class='MakeOrder_title__t4vgt']")
    make_your_order_text = make_your_order_text_elt.text
    assert "MAKE YOUR ORDER" == make_your_order_text
    time.sleep(1)

    browser.back()
    time.sleep(2)

    what_we_offer = browser.find_element(
        By.XPATH, "//section[@class='container'][1]")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", what_we_offer)

    get_more_info2_button = browser.find_element(
        By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed__y2rlJ LinkButton_sizeBig__7aVP_']")
    time.sleep(2)
    get_more_info2_button.click()
    time.sleep(2)
    make_your_order_text_elt = browser.find_element(
        By.XPATH, "//h2[@class='MakeOrder_title__t4vgt']")
    make_your_order_text = make_your_order_text_elt.text
    assert "MAKE YOUR ORDER" == make_your_order_text
    time.sleep(1)

    browser.back()
    time.sleep(2)

    what_done = browser.find_element(
        By.XPATH, "//section[@class='container DoneOrders_container__aI7tA']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", what_done)
    time.sleep(2)

    promotion_formats = browser.find_element(
        By.XPATH, "//section[@class='container'][2]")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", promotion_formats)

    get_more_info3_button = browser.find_element(
        By.XPATH, "//div[@class='PromotionFormatItem_container__f_OBE PromotionFormatItem_containerGetMore__HuFNd']//a[@class='LinkButton_link___jzSK LinkButton_colorWhite__A_Qx3']")
    time.sleep(2)
    get_more_info3_button.click()
    time.sleep(2)
    make_your_order_text_elt = browser.find_element(
        By.XPATH, "//h2[@class='MakeOrder_title__t4vgt']")
    make_your_order_text = make_your_order_text_elt.text
    assert "MAKE YOUR ORDER" == make_your_order_text
    time.sleep(1)

    browser.back()
    time.sleep(2)

    any_questions = browser.find_element(
        By.XPATH, "//section[@class='container AnyQuestions_container__7229q']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", any_questions)
    time.sleep(2)

    get_more_info4_button = browser.find_element(
        By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorBlack__WwvPN']")
    get_more_info4_button.click()
    time.sleep(2)
    faq_text_elt = browser.find_element(
        By.XPATH, "//h1[@class='FaqInfo_title__qU5w9']")
    faq_text = faq_text_elt.text
    assert "POPULAR QUESTIONS" == faq_text
    time.sleep(1)

    browser.back()
    time.sleep(2)

    contact_us_main_button = browser.find_element(
        By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorWhiteWithBorder__zLVqH']")
    contact_us_main_button.click()
    time.sleep(2)
    contact_us_text_elt = browser.find_element(
        By.XPATH, "//h1[@class='ContactUsForm_title__F_181']")
    contact_us_text = contact_us_text_elt.text
    assert "GET IN TOUCH" == contact_us_text
    time.sleep(1)

    browser.back()
    time.sleep(2)

finally:
    time.sleep(2)
    browser.quit()
