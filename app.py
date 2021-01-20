from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('www.brokerage.com')

# Initial log in table
username = driver.find_element_by_id('username')

username.send_keys('JohnDoe22')

password = driver.find_element_by_id('password')

password.send_keys('Password1234')

sign_in = driver.find_element_by_tag_name('button')

sign_in.click()

time.sleep(3.0)

# Searching for account by entering account number
account_number = driver.find_element_by_id('account')

account_number.send_keys('555-555-555')

search = driver.find_element_by_xpath('//*[@id="app-menu"]/form/div[2]/button')

search.click()

time.sleep(1.0)

# Loading overview of positions
positions = driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[2]/div[5]/div/div/header/span[2]/a/div")

positions.click()

time.sleep(1.0)

# Finally, downloading csv of positions and closing browser
download_file = driver.find_element_by_xpath('/html/body/div[2]/div/div/section/div[2]/div['
                                             '2]/div/ui-grid-export-tools/div/export-ui-grid-csv/button')

download_file.click()

time.sleep(2.0)

driver.close()
