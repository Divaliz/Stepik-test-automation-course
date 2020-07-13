from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    value_x = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(value_x)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_class_name("form-check-input").click()
    browser.find_element_by_id("robotsRule").click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
