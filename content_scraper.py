from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Configure Selenium WebDriver (Make sure to adjust the path to your ChromeDriver)
driver = webdriver.Chrome()

def visit_product_page(product_url):
    driver.get(product_url)

    # Simulate random delay
    time.sleep(random.uniform(1, 3))

    # Scrape product details
    product_name = driver.find_element(By.TAG_NAME, 'h4').text
    description = driver.find_element(By.TAG_NAME, 'h6').text
    image_url = driver.find_element(By.TAG_NAME, 'img').get_attribute('src')

    print(f"Product Name: {product_name}")
    print(f"Description: {description}")
    print(f"Image URL: {image_url}")

    # Simulate writing a review
    write_review(product_name)

def write_review(product_name):
    # Find and fill the review form
    username_field = driver.find_element(By.XPATH, '//input[@type="text"]')
    review_field = driver.find_element(By.XPATH, "//textarea")

    username_field.send_keys("BotUser")
    time.sleep(1)  # Mimic human-like delay
    time.sleep(1)
    review_field.send_keys("This is a great product! (From Bot)")
    
    submit_button = driver.find_element(By.XPATH, '//button[@type="button"]')
    submit_button.click()

    print(f"Review submitted for {product_name}")
    time.sleep(5)

# Example usage
product_urls = ["http://localhost:3000/product/3"]
for url in product_urls:
    visit_product_page(url)

# Close the driver
driver.quit()
