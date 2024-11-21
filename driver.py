from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Instantiate the Chrome WebDriver correctly
driver = webdriver.Chrome(executable_path='C:\Users\joshz\.cache\selenium\chromedriver\win64\129.0.6668.100\chromedriver.exe')

# Now open the URL
driver.get("https://umd.libcal.com/reserve/mckeldin/carrels-4hr")

# Access the location of the ChromeDriver service
location = driver.service.path

# Print the location of the WebDriver service
print(location)

# Close the driver properly
driver.quit()
