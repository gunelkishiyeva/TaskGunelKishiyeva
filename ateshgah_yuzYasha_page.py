from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Ateshgah Insurance Company's website
driver.get('http://www.ateshgah.com')

# Find and click the "Online əldə et" button
elede_et_button = driver.find_element(By.LINK_TEXT, 'Online əldə et')
elede_et_button.click()

# Wait for the button to be visible
button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//a[@href="https://polis.ateshgah.com/ops/VoluntaryHealth?lang=az"]/img'))
)

# Click the button
button.click()

# Fill in the form fields
driver.find_element(By.NAME, 'StartDate').send_keys('2023-07-05')  
driver.find_element(By.NAME, 'EndDate').send_keys('2023-07-10')  
driver.find_element(By.NAME, 'PolicyHolder.IdCode').send_keys('7LHNM2K')  
driver.find_element(By.NAME, 'PolicyHolder.IdSeries').send_keys('AZE')  
driver.find_element(By.NAME, 'PolicyHolder.IdNumber').send_keys('17946310')  

checkboxes = driver.find_elements("css selector", ".checkbox__label--selector")

# Iterate over the checkboxes and click on them 
for checkbox in checkboxes:
    driver.execute_script("arguments[0].click();", checkbox)

# Introduce a delay before clicking the button

wait = WebDriverWait(driver, 20)

# Click the button 
calculate_button = driver.find_element(By.CLASS_NAME, 'button__submit')
driver.execute_script("arguments[0].click();", calculate_button)

try:
    # Wait for the alert to appear
    alert = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'alert')))
    
    # Get the text from the alert
    alert_text = alert.text
    
    # Create a timestamp for the report file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Specify the file path for the report
    report_file = f'report_{timestamp}.txt'
    
    # Save the alert text to the report file
    with open(report_file, 'w', encoding='utf-8') as file:
        file.write(alert_text)
    
    print(f"Web report saved to: {os.path.abspath(report_file)}")
    
except Exception as e:
    print(f"Error occurred: {str(e)}")

# Close the browser
driver.quit()
