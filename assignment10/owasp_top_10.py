from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv
from pathlib import Path

# ----- ----- selectors from DOM ----- -----
# document.querySelectorAll("a[href*='/Top10/A']")

def main():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless=new')

    driver = webdriver.Chrome(options=opts)

    URL = "https://owasp.org/www-project-top-ten/"
    CSS_LIST = "a[href*='/Top10/A']"
    XPATH_TOP10 = (
        "(//h2[contains(., 'Top 10 Web Application Security Risks')]"
        " | //h3[contains(., 'Top 10 Web Application Security Risks')])[1]"
        "/following-sibling::ul[1]//a[contains(@href, '/Top10/A')]"
    )

    try:
        driver.get(URL)
        time.sleep(3 + random.random()*2)

        links = driver.find_elements(By.XPATH, XPATH_TOP10)
        # print("found links:", len(links))
        vulnerabilities = []
        for link in links:
            title = (link.text or "").strip()
            href = link.get_attribute("href")
            vulnerabilities.append({"Title": title, "Link": href})
        # print("Count of vulnerabilites:", len(vulnerabilities))
        for vulnerability in vulnerabilities:
            print("-", vulnerability["Title"], "|", vulnerability["Link"])
        # send to CSV
        out_path = Path(__file__).resolve().parent.parent / "csv" / "owasp_top_10.csv"
        with out_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Link"])
            writer.writeheader()
            writer.writerows(vulnerabilities)
        
        print(f"Wrote {len(vulnerabilities)} rows to {out_path}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()