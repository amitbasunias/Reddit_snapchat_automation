from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import re

# Path to your Chrome executable
#chrome_executable_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# Set up the Chrome web driver
#service = Service(chrome_executable_path)
#options = webdriver.ChromeOptions()

def scaping(username, password, number, subreddit):
    driver = webdriver.Edge()
    reddit_username = username
    reddit_password = password
    if subreddit == "dirtysnapchat":
        url = "https://www.reddit.com/r/DirtySnapchat/search?q=M4F&restrict_sr=on&include_over_18=on&sort=new&t=all"
    else:
        url = "https://www.reddit.com/r/DirtySnapchat/search?q=M4F&restrict_sr=on&include_over_18=on&sort=new&t=all"
    max_posts_to_scrape = int(number)
    snapchat_usernames = []
    # Load the Reddit login page
    driver.get("https://www.reddit.com/login")

    # Find the login form elements
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    time.sleep(2)
    # Fill in the login credentials and submit
    username_field.send_keys(reddit_username)
    time.sleep(2)
    password_field.send_keys(reddit_password)
    time.sleep(2)
    password_field.send_keys(Keys.RETURN)

    # Wait for the login to complete (you can add additional waits or checks here)
    time.sleep(10)
    print("printing for sleep")
    # Load the subreddit's posts page
    driver.get("https://www.reddit.com/r/DirtySnapchat/search?q=M4F&restrict_sr=on&include_over_18=on&sort=new&t=all")

    # Scroll down the page to load more posts
    for i in range(max_posts_to_scrape // 25):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the page to load

    # Extract and parse the page content
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # Find and extract the titles of posts
    post_titles = []
    for post in soup.find_all("h3", class_="_eYtD2XCVieq6emjKBH3m"):
        post_titles.append(post.get_text())

    # Extract the last word (Snapchat username) from each title
    for title in post_titles:
        words = title.split()
        if words:
            last_word = words[-1]
            # Validate if it's a valid Snapchat username (e.g., at least 3 characters)
            if re.match(r"^[A-Za-z0-9]{3,}$", last_word):
                snapchat_usernames.append(last_word)

    # Close the web driver
    validsnapchat = []

    # Loop through Snapchat usernames and visit profiles
    for name in snapchat_usernames:
        driver.get(f"https://www.snapchat.com/add/{name}")
        title = driver.title
        print(title)
        if " Snapchat Stories, Spotlight & Lenses" in title and len(name) >= 7:
            validsnapchat.append(name)
            print(f"{name} appended")
            time.sleep(2)

    # Close the web driver
    driver.quit()


    return validsnapchat
