from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Username and password prompt
username_text = input('Enter username: ')
password_text = input('Enter password: ')
account_number_text = input('Enter account number: ')

# Initiating the driver
driver = webdriver.Chrome()
driver.get('www.randombrokeragewebsite.com')

# Initial log in table
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
username.send_keys(username_text)

sign_in = driver.find_element_by_tag_name('button')
sign_in.click()

# Next level log in
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
password.send_keys(password_text)

submit = driver.find_element_by_xpath('/html/body/div/div/div/main/div/div/div[4]/div[1]/form/button')
submit.click()

# Searching for account by entering account number
account_number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'account')))
account_number.send_keys(account_number_text)

search = driver.find_element_by_xpath('//*[@id="app-menu"]/form/div[2]/button')
search.click()

# Loading overview of positions
positions = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                      "2]/div/div/section/div[2]/div["
                                                                                      "5]/div/div/header/span["
                                                                                      "2]/a/div")))
positions.click()

# Finally, downloading csv of positions and closing browser
download_file = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div['
                                                                                          '2]/div/div/section/div['
                                                                                          '2]/div[ '
                                                                                          '2]/div/ui-grid-export'
                                                                                          '-tools/div/export-ui-grid'
                                                                                          '-csv/button')))
download_file.click()

time.sleep(2.0)

driver.close()
