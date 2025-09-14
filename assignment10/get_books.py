# Task 1: Review robots.txt to Ensure Policy Compliance
    # Durham County Library robots.txt:
    # - User-agent section used: *
    # - Disallow: Disallow: /staff/
    # - Crawl-delay: n/a

    # Bibliocommons robots.txt:
    # - User-agent section used: *
    # - Disallow: /v2/availability/ but no issues for /v2/search/
    # - Crawl-delay: 120
    # - OK to fetch a single results page with 2s delay? No - need 120 seconds

# Task 2: Understanding HTML and the DOM for the Durham Library Site
# ----- ----- ----- selectors from DOM ----- ----- -----
# CSS_RESULT_LI = "li.row.cp-search-result-item"
# CSS_TITLE = "h2.cp-title .title-content"
# CSS_AUTHOR_LINKS = ".cp-by-author-block a"
# CSS_FMT_YEAR_WRAPPER = ".cp-format-info .display-info"
# CSS_FMT_YEAR_SPAN = ".display-info-primary"

# Task 3: Write a Program to Extract this Data
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
# import csv
import json

opts = webdriver.ChromeOptions()
opts.add_argument('--headless')

driver = webdriver.Chrome(options=opts)

SEARCH_URL = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
CSS_RESULT_LI           = "li.row.cp-search-result-item"
CSS_TITLE               = "h2.cp-title .title-content"
CSS_AUTHOR_LINKS        = ".cp-by-author-block a"
CSS_FMT_YEAR_WRAPPER    = ".cp-format-info .display-info"
CSS_FMT_YEAR_SPAN       = ".display-info-primary"
# Optional:
CRAWL_DELAY             = 120

driver.get(SEARCH_URL)
# print("Title: ", driver.title)
cards = driver.find_elements(By.CSS_SELECTOR, CSS_RESULT_LI)
print("cards found: ", len(cards))
sleep(5)
results = []

for li in cards:
    # Title
    try:
        title = li.find_element(By.CSS_SELECTOR, CSS_TITLE).text.strip()
    except Exception:
        title = ""

    # Author
    authors = []
    for a in li.find_elements(By.CSS_SELECTOR, CSS_AUTHOR_LINKS):
        txt = (a.text or "").strip()
        if txt:
            authors.append(txt)
    author_string = "; ".join(authors)

    #Format-Year
    try:
        wrapper = li.find_element(By.CSS_SELECTOR, CSS_FMT_YEAR_WRAPPER)
        format_year = wrapper.find_element(By.CSS_SELECTOR, CSS_FMT_YEAR_SPAN).text.strip()
    except Exception:
        format_year = ""

    results.append({"Title": title, "Authors": author_string, "Format-Year": format_year})

# print("rows built: ", len(results))
# print(results)
df = pd.DataFrame(results, columns=["Title", "Authors", "Format-Year"])

driver.quit()

# Task 4: Write out the Data
print(df.head(10))

# to CSV
df.to_csv("get_books.csv", index=False)
# to JSON
with open("get_books.json", "w", encoding="utf-8") as json_file:
    json.dump(results, json_file, indent=4, ensure_ascii=False)

# Task 5: Ethical Web Scraping
# see ethical_scraping.txt file
# Task 6: Scraping Structured Data
