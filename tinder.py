from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import time
import sys

#gets credentials
usr = input('Enter your username or email: ')
pwd = getpass('Enter your password: ')

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
driver.get('https://www.tinder.com/');

main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle
loginButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button'))
    )
loginButton.click()
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to.window(signin_window_handle)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
login_btn = driver.find_element_by_name('login')
login_btn.submit()

driver.switch_to.window(main_window_handle) 

for person in range(100):
	likeButton = WebDriverWait(driver, 10).until(
	        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'))
	    )
	likeButton.click()
	time.sleep(1);
	driver.refresh()

sys.exit("Finished!")