from selenium import webdriver
import os
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    req = browser.find_elements_by_class_name("form-control")
    for line in req:
        line.send_keys("pepega")
    snd_file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    with open("file.txt", "w") as file:
        file.write("pepega_clap")
        file_path = os.path.join(current_dir, 'file.txt')
    snd_file.send_keys(file_path)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
