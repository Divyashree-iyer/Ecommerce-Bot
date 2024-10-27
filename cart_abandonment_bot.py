from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# Initialize WebDriver (Make sure to adjust the path to your ChromeDriver)
driver = webdriver.Chrome()

# Define a function to add a product to the cart
def add_to_cart(product_url):
    try:
        # Step 1: Visit the product page
        driver.get(product_url)
        
        # Step 2: Simulate delay to mimic human browsing
        # time.sleep(random.uniform(2, 5))
        
        # Step 3: Find and click the "Add to Cart" button
        add_to_cart_button = driver.find_element(By.XPATH, '//button[contains(text(), "Add to Cart")]')
        
        for i in range(4):
            # Scroll to the button if it’s not visible
            ActionChains(driver).move_to_element(add_to_cart_button).perform()
            # time.sleep(random.uniform(1, 2))
            
            # Click the button
            add_to_cart_button.click()
            time.sleep(1)  # Short delay to wait for the alert to appear
            alert = driver.switch_to.alert  # Switch to the alert
            alert.accept()  # Click OK on the alert
            print(f"Added item from {product_url} to cart.")
            
            # Simulate short wait after adding item to cart
            time.sleep(1)

    except Exception as e:
        print("An error occurred while adding to cart:", e)

# Define a function to simulate cart-stuffing and abandonment
def cart_stuffing_and_abandonment():
    try:
        add_to_cart("http://localhost:3000/product/1")
        
        # Step 4: Simulate cart viewing and abandonment
        print("Viewing cart items before abandoning.")
        # view_cart()
        time.sleep(6)
        print("Abandoning cart and closing browser.")
        
    finally:
        # Step 5: Close the browser to simulate abandonment
        driver.quit()


cart_stuffing_and_abandonment()
