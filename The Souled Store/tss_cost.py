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
base_url = 'https://www.thesouledstore.com/men/t-shirts'
driver.get(base_url)

# Wait for the page to load initially
time.sleep(10)
height=driver.execute_script('return document.body.scrollHeight')
while True:
    # Scroll to a position slightly above the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 400);")
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if height == new_height:
        break
    height = new_height
# # Function to scroll to the bottom of the page
# def scroll_to_bottom(driver):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(15)  # Wait for the new products to load

# # Infinite scrolling
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     scroll_to_bottom(driver)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

tshirt_detail = []

# Extract product details
tshirt_elements = driver.find_elements(By.CSS_SELECTOR, 'div.productlist.custom-full-border.productCard')

for element in tshirt_elements:
    try:
        title = element.find_element(By.CSS_SELECTOR, 'h5.text-left').text
    except:
        title = None

    try:
        mrp = element.find_element(By.CSS_SELECTOR, 'span.product-price').text
    except:
        mrp = None

    try:
        sp = element.find_element(By.CSS_SELECTOR, 'span.offer.fsemibold').text
    except:
        sp = None

    try:
        category = element.find_element(By.CSS_SELECTOR, 'div.listprice.ecltext').text
    except:
        category = None

    tshirt_info = {
        'Title': title,
        'Category': category,
        'MRP': mrp,
        'SP': sp
    }
    tshirt_detail.append(tshirt_info)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(tshirt_detail)


# Save the DataFrame to a CSV file
df.to_csv('TheSouledStore_tshirt_info.csv', index=False)

# Close the browser
driver.quit()
