from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Instantiate the Chrome WebDriver correctly
driver = webdriver.Chrome()

# Now open the URL
driver.get("https://umd.libcal.com/reserve/mckeldin/carrels-4hr")

# Access the location of the ChromeDriver service
location = driver.service.path

# Print the location of the WebDriver service
print(location)

# Close the driver properly
driver.quit()
