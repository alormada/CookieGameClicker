from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie_button = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

beginning_time = time.time()
timeout = beginning_time + 60*5

# while time.time() < timeout:
#     current_time = time.time()
#     if current_time >= beginning_time + 5:
#
#     cookie_button.click()


while True:
    right_panel = driver.find_element(By.ID, value="store").find_elements(By.CSS_SELECTOR, value="b")
    buttons = driver.find_element(By.ID, value="store").find_elements(By.CSS_SELECTOR, value="div")
    for i in range(len(right_panel) - 2, -1, -1):
        print(i)
        n = int(right_panel[i].text.strip().replace(",","").split("-")[1])
        your_money = int(driver.find_element(By.XPATH, value='//*[@id="money"]').text.replace(",", ""))
        button = buttons[i]
        if n <= your_money:
            button.click()
            break
        print(n)
        print(your_money)
    time.sleep(2)


driver.quit()