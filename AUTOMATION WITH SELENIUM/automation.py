from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

def human_delay(min_s=0.5, max_s=1.5):
    time.sleep(random.uniform(min_s, max_s))

driver.get("https://www.google.com")
human_delay()

search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
search_box.click()
human_delay()
search_box.send_keys("Selenium Python tutorial")
human_delay()
search_box.send_keys(Keys.RETURN)

wait.until(EC.presence_of_element_located((By.ID, "search")))
human_delay(2, 3)

driver.get("https://example.com")
wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

heading = driver.find_element(By.TAG_NAME, "h1")
print(heading.text)

link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "More information...")))
human_delay()
link.click()

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
human_delay(2, 3)

print(driver.title)
print(driver.current_url)

driver.quit()
