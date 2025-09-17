import json, random, sys
from time import sleep
from modules.login import fb_login
from modules.group_scraper import get_posts
from modules.group_engager import react_post, comment_post

with open("config.json") as f:
    config = json.load(f)

accounts = config["accounts"]
group_url = config["target_group"]
limit = config["settings"]["limit_posts_per_account"]
delay_min = config["settings"]["delay_min_seconds"]
delay_max = config["settings"]["delay_max_seconds"]
headless = config["settings"]["headless"]

for acc in accounts:
    uid, pwd = acc["uid"], acc["password"]
    print(f"\n[+] Logging in: {uid}")
    driver = fb_login(uid, pwd, headless=headless)
    if not driver:
        continue

    posts = get_posts(driver, group_url, limit=limit)
    for url in posts:
        reaction = random.choice(config["reaction_types"])
        comment = random.choice(config["comment_texts"])
        react_post(driver, url, reaction)
        sleep(random.uniform(delay_min, delay_max))
        comment_post(driver, url, comment)
        sleep(random.uniform(delay_min, delay_max))

    driver.quit()