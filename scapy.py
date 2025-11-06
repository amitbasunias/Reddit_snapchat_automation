import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import openai
from selenium.webdriver.edge.options import Options
# Import Options for Chrome (use EdgeOptions for Edge)

def scaping(username, password, number, subreddit):
    options = Options()
    options.headless = True

    #driver = webdriver.Edge(options=options)
    driver = webdriver.Edge()
    reddit_username = username
    reddit_password = password
    if subreddit == "dirtysnapchat":
        url = "https://www.reddit.com/r/DirtySnapchat/search?q=M4F&restrict_sr=on&include_over_18=on&sort=new&t=all"
    else:
        url = "https://www.reddit.com/r/DirtySnapchat/search?q=M4F&restrict_sr=on&include_over_18=on&sort=new&t=all"
    max_posts_to_scrape = int(number)
    snapchat_usernames = set()  # Use a set to avoid duplicates

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
    driver.get(url)

    # Scroll down the page to load more posts
    for i in range(max_posts_to_scrape // 25):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the page to load

    # Find and extract the links to individual posts
    # Find and extract the links to individual posts
    page_source = driver.page_source
    post_links = re.findall(r'href="/r/.*?/comments/.*?/"', page_source)
    print(post_links)
    snaplist = []
    # Visit each post and scrape content
    for link in post_links:
        post_url = "https://www.reddit.com" + link.strip('href="')  # Construct the full post URL
        driver.get(post_url)
        time.sleep(2)  # Wait for the post to load

        # Extract and parse the page content for the individual post
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # Find and extract the post title
        post_title = soup.find("h1", class_="_eYtD2XCVieq6emjKBH3m").get_text()

        # Find and extract the post body
        try:
            post_body = soup.find("div", class_="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root").get_text()
        except:
            post_body = post_title
        posttext = f"{post_title} \n {post_body}"

        api_key = "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"

        # Initialize the OpenAI API client
        openai.api_key = api_key
        # Define the prompt for the model
        prompt = f"find snapchat id from following text, only provide the id: {posttext}"

        # Make an API call to the 'davinci' model
        response = openai.completions.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=2000  # You can adjust this as needed
        )

        # Extract the generated text from the API response
        snapid = response.choices[0].text
        if len(snapid.split()) == 1:
            snaplist.append(snapid)
            print(f"Got a Snapchat ID: {snapid}")

        time.sleep(5)

        # Extract the last word (Snapchat username) from the title and body

    # Close the web driver
    '''validsnap = list(snapchat_usernames)
    validsnapchat = []
    '''
    validsnapchat = []
    # Loop through Snapchat usernames and visit profiles
    for name in snaplist:
        driver.get(f"https://www.snapchat.com/add/{name}")
        title = driver.title
        print(title)
        if " Snapchat Stories, Spotlight & Lenses" in title and len(name) >= 6:
            print(f"{name} appended")
            validsnapchat.append(name)
            time.sleep(2)


    # Close the web driver
    driver.quit()
    return validsnapchat
