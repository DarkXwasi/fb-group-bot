from selenium.webdriver.common.by import By
import time

def get_posts(driver, group_url, limit=5):
    driver.get(group_url)
    time.sleep(5)
    posts = []
    links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/posts/']")
    for a in links:
        if len(posts) >= limit:
            break
        href = a.get_attribute("href")
        if href and href not in posts:
            posts.append(href)
    print(f"[+] Found {len(posts)} posts")
    return posts