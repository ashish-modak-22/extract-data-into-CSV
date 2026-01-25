from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.thehindu.com/")

headlines = driver.find_elements("xpath", "//a[contains(@href, 'article')]")

with open("HINDU.csv", "w", newline="", encoding="utf-8")as file:
    writer = csv.writer(file)
    writer.writerow(["SL.NO.", "HEADLINE", "URL"])

    for i, headline in enumerate(headlines,start=1):
        href = headline.get_attribute("href")
        article = headline.text.strip()

        if href and article:
            writer.writerow([i, article, href])

input("All the articles with their respective URL are saved to the CSV file. To close this operation, press ENTER")

driver.quit()
