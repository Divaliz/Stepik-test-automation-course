from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    required1 = browser.find_element_by_css_selector(".first_block .first_class .first")
    required1.send_keys("pepega")

    required2 = browser.find_element_by_css_selector(".first_block .second_class .second")
    required2.send_keys("pepega")

    required3 = browser.find_element_by_css_selector(".first_block .third_class .third")
    required3.send_keys("pepega")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    assert "Congratulations! You have successfully registered!" == welcome_text_elt.text

finally:
    time.sleep(10)
    browser.quit()
