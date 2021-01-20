from selenium import webdriver
import time

# Username and password prompt
username_text = input('Type username: ')
password_text = input('Type password: ')
account_number_text = input('Type account number: ')

# Initiating the driver
driver = webdriver.Chrome()
driver.get('www.brokeragesite.com')

# Initial log in table
username = driver.find_element_by_id('username')
username.send_keys(username_text)

sign_in = driver.find_element_by_tag_name('button')
sign_in.click()

time.sleep(1.0)

# Next level log in
password = driver.find_element_by_id('password')
password.send_keys(password_text)

submit = driver.find_element_by_xpath('/html/body/div/div/div/main/div/div/div[4]/div[1]/form/button')
submit.click()

time.sleep(3.0)

# Searching for account by entering account number
account_number = driver.find_element_by_id('account')
account_number.send_keys(account_number_text)

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
