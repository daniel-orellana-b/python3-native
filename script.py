from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.primefaces.org/primereact-v5/#/datatable/selection"
checkbox_name = "Blue Band"

driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)

try:
    checkbox = driver.find_element(By.XPATH, f'//td[contains(text(), "{checkbox_name}")]//preceding-sibling::td[@class="p-selection-column"]//div[contains(@class, "p-checkbox-box")]')
    checkbox.click()
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()