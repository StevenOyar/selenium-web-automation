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

    # Launch the browser
    driver = webdriver.Chrome()

    try:
        # Open URL
        driver.get("https://www.coursera.org/")

        # finds and clicks the Launch a New Career
        launch_a_new_career = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='rendered-content']/div/main/div/section[1]/div/div/div/div/div/div/div[1]/div/a")))
        launch_a_new_career.click()
        # verification of the launch career is opened
        print("the launch career page is successfully opened")
        assert "career-academy" in driver.current_url, "Navigation to Career Academy failed"
        
        time.sleep(5)
        # Accept cookies
        accept_cookies = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        accept_cookies.click()
        time.sleep(5)  # waiting time


        project_manager = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Project Manager"))
            )
        project_manager.click()
        print("project manages courss loaded")

        time.sleep(5)  # waiting time

        # choose a microsoft course
        microsoft_project = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='rendered-content']/div/div/div[3]/div/main/div/section/div/div/div/div[2]/section/ul/li[2]/div/div/div/a/div[1]/h3"))
            )
        microsoft_project.click()

        time.sleep(2)  # waiting time

        #click of the join free button
        join_now = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='rendered-content']/div/span/div/nav/div[3]/div/div/div/div[2]/button[2]/span")))
        join_now.click()

      

    finally:
        input("\nPress Enter to close browser...")
        driver.quit()


test_web_interaction()