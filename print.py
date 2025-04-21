import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys

# Common password for all users
common_password = "123405abcdae"


# Function to perform login and take screenshot
def login_and_screenshot(user):
    # Set the path to your GeckoDriver executable
    gecko_path = "geckodriver.exe"

    # Create a Firefox driver
    service = FirefoxService(executable_path=gecko_path)
    driver = webdriver.Firefox(service=service)

    # Open your site's login page
    driver.get("https://prova.fundacaocefetminas.org.br/")

    # Perform login
    username_input = driver.find_element("name", "username")  # Adjust based on your HTML structure
    password_input = driver.find_element("name", "password")  # Adjust based on your HTML structure

    username_input.send_keys(user)
    password_input.send_keys(common_password)
    password_input.send_keys(Keys.ENTER)

    # Wait for the page to load (you might need to adjust the sleep time)
    time.sleep(3)

    height = driver.execute_script('return document.documentElement.scrollHeight')
    width = driver.execute_script('return document.documentElement.scrollWidth')
    driver.set_window_size(width, height + 200)  # the trick

    # Take a screenshot of the entire page
    driver.save_screenshot(f"./screenshots/{user}.png")

    # Close the browser
    driver.quit()


# Read usernames from the CSV file
csv_file_path = "usernames.csv"  # Update with the actual path to your CSV file

with open(csv_file_path, "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)

    # Skip the header if it exists
    next(csv_reader, None)

    # Iterate through the usernames and perform login and screenshot
    for row in csv_reader:
        username = row[1]  # Assuming the username is in the first column, adjust if necessary
        login_and_screenshot(username)
