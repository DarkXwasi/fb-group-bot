from selenium.webdriver.common.by import By
import time

def react_post(driver, post_url, reaction="like"):
    driver.get(post_url)
    time.sleep(3)
    try:
        like_btn = driver.find_element(By.XPATH, "//div[@aria-label='Like']")
        like_btn.click()
        print(f"[+] Reacted on {post_url}")
    except Exception as e:
        print("[-] React failed:", e)

def comment_post(driver, post_url, text):
    driver.get(post_url)
    time.sleep(3)
    try:
        box = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true']")
        box.click()
        box.send_keys(text + "\n")
        print(f"[+] Commented: {text}")
    except Exception as e:
        print("[-] Comment failed:", e)