import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

FB_EMAIL = "email"
FB_PASSWORD = "password"
POST_TEXT = "Hello from Selenium"

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 25)

try:
    # Open Facebook
    driver.get("https://www.facebook.com")
    time.sleep(10)

    # Login
    email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password = wait.until(EC.visibility_of_element_located((By.ID, "pass")))

    email.send_keys(FB_EMAIL)
    time.sleep(10)

    password.send_keys(FB_PASSWORD)
    time.sleep(10)

    password.send_keys(Keys.ENTER)
    time.sleep(10)

    # Wait for home feed
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='feed']")))
    time.sleep(10)

    # Create post
    post_box = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox']"))
    )
    post_box.click()
    time.sleep(10)

    post_box.send_keys(POST_TEXT)
    time.sleep(10)

    post_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Post']"))
    )
    post_button.click()
    time.sleep(10)

    wait.until(EC.invisibility_of_element(post_button))
    time.sleep(10)

    # -------- LOGOUT --------

    # Open account menu
    account_menu = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@aria-label='Account']")
        )
    )
    account_menu.click()
    time.sleep(10)

    # Click logout
    logout_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Log out']")
        )
    )
    logout_button.click()
    time.sleep(10)

finally:
    driver.quit()
