import time
import pandas as pd
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Set up Chrome Options
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)

# Set up Chrome Service
service = Service(ChromeDriverManager().install())
driver = uc.Chrome(options=chrome_options)

# Congress Bills URL
url = "https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%2C%22congress%22%3A119%7D"
driver.get(url)

# Wait for page to load
time.sleep(5)

# Find Bills
bills = driver.find_elements(By.CSS_SELECTOR, 'li.expanded')

# Store Data
bill_data = []

for bill in bills[:10]: # Only get the first 10 bills for testing purposes
    try:
        name = bill.find_element(By.CSS_SELECTOR, 'span.result-heading').text.strip()
        title = bill.find_element(By.CSS_SELECTOR, 'span.result-title').text.strip()
        sponsors = bill.find_element(By.CSS_SELECTOR, 'span.result-item').text.strip()
        status = bill.find_element(By.CSS_SELECTOR, 'li.selected').text.strip()
    except:
        name, title, sponsors, status = 'N/A', 'N/A', 'N/A', 'N/A'
    print(name, title, sponsors, status)

    bill_data.append([name, title, sponsors, status])

# Close the browser
driver.quit()

# Save to CSV
df_bills = pd.DataFrame(bill_data, columns=['Name', 'Title', 'Sponsors', 'Status'])
df_bills.to_csv('congress_bills.csv', index=False)
print("Data saved to congress_bills.csv")