import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Username and password prompt
username_text = input('Enter Apex username: ')
password_text = input('Enter Apex password: ')
account_number_text = input('Enter Apex account number: ')
simply_safe_email_text = input('Enter Simply Safe Email: ')
simply_safe_password_text = input('Enter Simply Safe password: ')

# Initiating the driver
driver = webdriver.Chrome()
driver.get('https://public-apps.apexclearing.com')

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

# Parsing csv data
df = pd.read_csv('/home/gage/Downloads/positions-export.csv')

ticker_price_amount = df[['Symbol', 'Qty', 'Price']]

ticker_price_amount.to_csv('SimplySafeData.csv', index=False)

os.remove('/home/gage/Downloads/positions-export.csv')

# Returning data to Simply Safe website
driver = webdriver.Chrome()
driver.get('https://www.simplysafedividends.com/')

# Simply Safe log in
log_in = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/ul[1]/li[5]/a')))
log_in.click()

# Simply safe email
simply_safe_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login')))
simply_safe_email.send_keys(simply_safe_email_text)

enter_log_in = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form/div'
                                                                                         '/input')))
enter_log_in.click()

# Simply safe password
simply_safe_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
simply_safe_password.send_keys(simply_safe_password_text)

enter_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form'
                                                                                           '/div/input')))
enter_password.click()

# Navigate to portfolio update source
portfolio_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav'
                                                                                           '"]/div[1]/a')))
portfolio_menu.click()

# Select portfolio
my_portfolio = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav"]/div['
                                                                                         '1]/div/div/nav/section['
                                                                                         '1]/a[1]')))
my_portfolio.click()

# Selecting import data
import_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="investments'
                                                                                        '"]/header/div[1]/div/a')))
import_menu.click()

spreadsheet_selection = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*['
                                                                                                  '@id="investments'
                                                                                                  '"]/header/div['
                                                                                                  '1]/div/div/a[1]')))
spreadsheet_selection.click()

# Choose account
investment_account = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div'
                                                                                               '/article/div/a[2]')))
investment_account.click()

# Navigate to file options
file_choice = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="spreadsheet'
                                                                                        '_import_file"]')))
file_choice.send_keys('/home/gage/PycharmProjects/Portfolio update/SimplySafeData.csv')

# Finally, uploading the document and close driver
upload_csv = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/article/div['
                                                                                       '3]/a[1]')))
upload_csv.click()

os.remove('/home/gage/PycharmProjects/Portfolio update/SimplySafeData.csv')

driver.close()
