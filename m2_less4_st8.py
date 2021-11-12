import time
import math
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
print('Git train')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(chrome_options=chrome_options)

try:
    driver.implicitly_wait(5)
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    button = driver.find_element_by_id('book')
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')

    )
    button.click()

    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    out = math.log(abs(12 * math.sin(int(x))), math.e)
    input1 = driver.find_element_by_id("answer")
    input1.send_keys(str(out))

    button = driver.find_element_by_id("solve")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

