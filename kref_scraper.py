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
url = "https://secure.kentucky.gov/kref/publicsearch/AllContributors?FirstName=&LastName=&FromOrganizationName=&ElectionDate=01%2F01%2F0001&City=&State=&Zip=&Employer=&Occupation=&OtherOccupation=&MinAmount=&MaxAmount=&MinimalDate=&MaximalDate=&ContributionMode=&ContributionSearchType=All&PageSize=10&PageIndex=0&ReportId="
driver.get(url)

# Wait for page to load
time.sleep(5)


# Store Data
gift_data = []

while True: # Loop through all pages
        # Find Gifts
        gifts = driver.find_elements(By.CSS_SELECTOR, 'tr')

        for gift in gifts[1:]: # skip the header row and limit to the first 10 records for testing purposes
            try:
                # Extract all <td> elements
                cells = gift.find_elements(By.CSS_SELECTOR, 'td')

                # Ensure that the row has the correct number of columns
                if len(cells) >= 6:
                    amount = cells[0].text.strip()
                    date = cells[1].text.strip()
                    recipient = cells[2].text.strip()
                    donor = cells[3].text.strip()
                    report = cells[4].text.strip()
                    occupation = cells[5].text.strip()
                    contribution_type = cells[6].text.strip()
                    contribution_mode = cells[7].text.strip()
                    street = cells[8].text.strip()
                    city = cells[9].text.strip()
                    state = cells[10].text.strip()
                    zip_code = cells[11].text.strip()
                    employer = cells[12].text.strip()
                else:
                    amount, date, recipient, donor, report, occupation = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                    contribution_type, contribution_mode, street, city, state, zip_code, employer = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
            except Exception as e:
                print(f"Error processing row: {e}")
                amount, date, recipient, donor, report, occupation = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
                contribution_type, contribution_mode, street, city, state, zip_code, employer = 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'
            
            print(amount, date, recipient, donor, report, occupation, contribution_type, contribution_mode, street, city, state, zip_code, employer)
            gift_data.append([amount, date, recipient, donor, report, occupation, contribution_type, contribution_mode, street, city, state, zip_code, employer])

        # Check if the next page button exists and is enabled
        try:
            next_page = driver.find_element(By.CSS_SELECTOR, "li.page-item.active + li.page-item a")
            if 'disabled' in next_page.get_attribute('class'):
                break
            next_page.click()
            time.sleep(5) # Wait for page to load
        except Exception as e:
            print(f"Error processing next page: {e}")
            break
# Close the browser
driver.quit()

# Save to CSV
df_gifts = pd.DataFrame(gift_data, columns=[amount, date, recipient, donor, report, occupation, contribution_type, contribution_mode, street, city, state, zip_code, employer])
df_gifts.to_csv('kref_donations.csv', index=False)
print("Data saved to kref_donations.csv")