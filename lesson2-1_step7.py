from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("treasure")
    valuex = x_element.get_attribute("valuex")
    y = calc(valuex)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    flesh_is_weak = browser.find_element_by_id("robotCheckbox")
    flesh_is_weak.click()
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
