from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
# Path to your ChromeDriver executable
service = Service(executable_path="chromedriver.exe")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service)

# Open Bewakoof T-shirt page
base_url = 'https://www.uniqlo.com/in/en/men/tops/ut-graphic-tees'
driver.get(base_url)

# Wait for the page to load initially
time.sleep(10)

tshirt_detail = []

# Extract product details
tshirt_elements = driver.find_elements(By.CSS_SELECTOR, 'div.fr-product-card.default')

for element in tshirt_elements:
    try:
        title = element.find_element(By.CSS_SELECTOR, 'h2.description.decscription-text.fr-no-uppercase').text
    except:
        title = None

    try:
        mrp = element.find_element(By.CSS_SELECTOR, 'div.dual-price-original span.fr-price-currency span').text
    except:
        mrp = None

    try:
        sp = element.find_element(By.CSS_SELECTOR, 'span.price-limited span.fr-price-currency span').text
    except:
        sp = element.find_element(By.CSS_SELECTOR, 'span.price-original span.fr-price-currency span').text

#     try:
#         rating = element.find_element(By.CSS_SELECTOR, 'div.listprice.ecltext').text
#     except:
#         rating = None

    tshirt_info = {
        'Title': title,
#         'Ratin': rating,
        'MRP': mrp,
        'SP': sp
    }
    tshirt_detail.append(tshirt_info)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(tshirt_detail)


# Save the DataFrame to a CSV file
df.to_csv('uniqlo_tshirt_info3.csv', index=False)

# Close the browser
driver.quit()