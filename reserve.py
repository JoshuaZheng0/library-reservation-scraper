import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Setup logging to log into a file
logging.basicConfig(filename="selenium_task_scheduler.log", level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

logging.info("Script started")

options = Options()
options.add_argument("--headless")
service = Service('C:/Users/joshz/.cache/selenium/chromedriver/win64/129.0.6668.100/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

def scrape(url, driver, time_slot_selectors):
    try:
        driver.get(url)
        driver.implicitly_wait(0.5)
        time.sleep(5)

        title = driver.title
        logging.info(f"Visiting {title} at {url}")

        for i in range(5):
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "fc-next-button"))
            )
            next_button.click()
            time.sleep(1)

        for time_slot_selector in time_slot_selectors:
            try:
                time_slot = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, time_slot_selector))
                )
                driver.execute_script("arguments[0].scrollIntoView();", time_slot)
                time_slot.click()
                time.sleep(2)
            except Exception as e:
                logging.error(f"Time slot not available: {e}")
                      
        submit_button = driver.find_element(By.ID, 'submit_times')
        submit_button.click()
        logging.info("Submit Times button clicked")

        time.sleep(2)

        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "terms_accept"))
        )
        continue_button.click()

        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fname"))
        )
        first_name_input.send_keys("Joshua")

        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "lname"))
        )
        last_name_input.send_keys("Zheng")

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys("jzheng30@terpmail.umd.edu")

        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "q16114"))
        )
        input_field.send_keys("120906930")

        time.sleep(1)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn-form-submit"))
        )
        submit_button.click()

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        logging.error(traceback.format_exc())

if __name__ == "__main__":
    start_url = 'https://umd.libcal.com/reserve/mckeldin/carrels-4hr'

    now = datetime.now()
    future_date = now + timedelta(days=5)
    formatted_date = future_date.strftime("%A, %B %d, %Y").replace(" 0", " ")
    room_number = 7235
    time_slots = ["6:00PM", "7:00PM", "8:00PM", "9:00PM"]
    time_slot_selectors = [
        f'a.fc-timeline-event[title="{time} {formatted_date} - {room_number} - Available"]' for time in time_slots
    ]

    try:
        scrape(start_url, driver, time_slot_selectors)
    finally:
        driver.quit()
        logging.info("Script finished")
