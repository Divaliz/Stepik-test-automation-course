from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    browser.find_element_by_tag_name("select").click()
    ans = str(int(x) + int(y))
    browser.find_element_by_css_selector("[value='" + ans + "']").click()
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
