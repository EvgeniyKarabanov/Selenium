import time
import math
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(chrome_options=chrome_options)

try:

    driver.get("http://suninjuly.github.io/alert_accept.html")
    driver.find_element_by_tag_name("button").click()
    confirm = driver.switch_to_alert()
    confirm.accept()
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    out = math.log(abs(12 * math.sin(int(x))), math.e)
    input1 = driver.find_element_by_id("answer")
    input1.send_keys(str(out))

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

