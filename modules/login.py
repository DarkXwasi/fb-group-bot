from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def fb_login(uid, password, headless=False):
    try:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get("https://www.facebook.com/")
        time.sleep(3)

        driver.find_element(By.ID, "email").send_keys(uid)
        driver.find_element(By.ID, "pass").send_keys(password + Keys.RETURN)
        time.sleep(6)

        if "login" in driver.current_url or "checkpoint" in driver.current_url:
            print("[-] Login failed:", uid)
            driver.quit()
            return None

        print("[+] Login success:", uid)
        return driver
    except Exception as e:
        print("[-] Error logging in:", e)
        return None