# launch the browser
#open url
# find element by id/class
#perform action (click/type)
# verify result
# close browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_web_interaction():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.powerlearnprojectafrica.org/")

        academy = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "PLP Academy"))
        )
        academy.click()
        time.sleep(2)

        # Switch to the new tab that opened
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)

        print("Current url:", driver.current_url)
        assert "academy" in driver.current_url, "Navigation to Academy failed"

        login = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='login']"))
        )
        login.click()

        webdriver_wait = WebDriverWait(driver, 10)
        webdriver_wait.until(EC.url_contains("login"))

        # Fill in the email
        email = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email.send_keys("your LMS email")

        # Fill in the password
        password = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password.send_keys("Your LMS passeword")

        # click sign in button
        sign_in = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='root']/div[1]/div[2]/div[2]/form/button")
            )
        )
        sign_in.click()

        time.sleep(3)



        #if password is wrong it clicks on forgot password link
        forgot_password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div[1]/div[2]/div[2]/form/div[3]/div/a"))
        )
        forgot_password.click()

        #email if auto filled
        email = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email.send_keys("Your email")

        #button to get an email for password reset
        request_password_reset = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[1]/div[2]/div[2]/form/button"))
        )   
        request_password_reset.click()

        # login link
        new_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[1]/div[2]/div[2]/form/div[2]/a"))
        )       
        new_login.click()

        # raise a ticket
        raise_ticket = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/button[1]"))
        )
        raise_ticket.click()

    finally:
        input("Press Enter to close the browser...")
        driver.quit()


test_web_interaction()
