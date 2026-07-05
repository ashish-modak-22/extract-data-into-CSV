# 📰 The Hindu News Article Scraper using Selenium (Python)

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![ChromeDriver](https://img.shields.io/badge/Chrome%20WebDriver-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)

</div>


## 📌 Project Overview
 
This project is a **web automation and data extraction project** built using **Selenium in Python**.
The script automatically visits **The Hindu news website**, extracts article information, and stores the data into a **CSV file** for further use.
 
The extracted data includes:
- Serial Number (SL No)
- Article Headline
- Article URL (Link)
This project focuses on **real-world web scraping**, automation logic, and structured data storage.
 
---
 
## ⚙️ Technologies Used
 
- **Python**
- **Selenium WebDriver**
- **Google Chrome (Headless Mode)**
- **WebDriver Manager** (auto-installs the matching ChromeDriver)
- **CSV Module**
- **VS Code**

---

## 🚀 Features
 
- Runs Chrome in **headless mode** (no visible browser window)
- Automatically downloads/manages the correct **ChromeDriver** version via `webdriver-manager`
- Automatically opens *The Hindu* news website
- Fetches multiple news article links using **XPath**
- Extracts article headlines and URLs
- Stores data in a structured **CSV file**
- CSV file contains:
  - SL No
  - Headline
  - URL
- Waits for user input (`ENTER`) before closing the browser session
- Fully automated scraping process
---
 
## 🧠 Project Workflow
 
1. Configure Chrome options (`--headless`, `--disable-gpu`)
2. Launch Google Chrome using Selenium WebDriver, with ChromeDriver auto-installed via `webdriver-manager`
3. Open **The Hindu** official news website
4. Locate article elements using **XPath** (`//a[contains(@href, 'article')]`)
5. Extract:
   - Article headlines
   - Corresponding URLs
6. Generate a CSV file
7. Save extracted data in the following format:
   - SL No | Headline | URL
8. Wait for user confirmation (`ENTER`) before quitting the driver

---

## 📊 Output Format (CSV)
 
The generated CSV file (`HINDU.csv`) contains the following columns:
 
| SL No | Headline | URL |
|------|----------|-----|
| 1 | Sample News Title | https://www.thehindu.com/... |
 
---
 
## 🖼️ Project Snapshot
 
![Project Output Screenshot](csv_snapshot.png)
 
---
 
```
the-hindu-news-scraper/
│
├── csv_extract.py
├── HINDU.csv
├── csv_snapshot.png
└── README.md
```
 
---
 
## ▶️ How to Run the Project
 
**1️⃣ Clone the repository**
```bash
git clone https://github.com/ashish-modak-22/csv_file_extraction.git
```
 
**2️⃣ Install required libraries**
```bash
pip install selenium webdriver-manager
```
 
**3️⃣ Run the script**
```bash
python csv_extract.py
```
 
---
 

## 📌 Requirements
 
- Python 3.x
- Google Chrome browser
- Selenium library
- WebDriver Manager library (`webdriver-manager`)
---
 
## 🎯 Learning Outcomes
 
- Hands-on experience with real-world web scraping
- Learned to extract text and attributes using XPath
- Learned CSV file handling in Python
- Improved understanding of Selenium automation workflow (headless mode, service management)
- Understood dynamic website scraping challenges
---
 
## 👨‍💻 Author
 
- **Ashish Modak**
- Selenium Automation Learner | Python Programmer | C/C++ DSA Enthusiast
---
 
**Important Modification:** An explicit wait can be added for the WebDriver (e.g., using `WebDriverWait` with `expected_conditions`) as per certain conditions, for a smoother and more reliable scraping process.
