from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element_by_id("book").click()
    x = browser.find_element_by_id("input_value")
    xvalue = calc(x.text)
    browser.find_element_by_class_name("form-control").send_keys(xvalue)
    browser.find_element_by_id("solve").click()

finally:
    time.sleep(30)
    browser.quit()
