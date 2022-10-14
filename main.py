import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
X = datetime.datetime.now()
os.environ['PATH'] += "SeleniumDrivers"
options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe" ## Change this to your browser path
chrome_driver_binary = "SeleniumDrivers\chromedriver.exe"  ### Change this to your driver path
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

## Workings...
driver.get("https://github.com/")
driver.implicitly_wait(3)
my_element = driver.find_element(By.CSS_SELECTOR, 'a[href="/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home"]')
my_element.click()
my_element = driver.find_element(By.CSS_SELECTOR, 'a[href="/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home"]')
my_element.click()
driver.implicitly_wait(3)
my_element = driver.find_element(By.ID,"login_field")
gmail = "your_email" ## Change this to your email
my_element.send_keys(gmail)   
my_element = driver.find_element(By.ID,"password")
password = "your_password"   ### change this your password here
my_element.send_keys(password) 
my_element.send_keys(Keys.ENTER)
driver.implicitly_wait(3)
my_element = driver.find_element(By.CSS_SELECTOR, 'a[data-hovercard-url="/Git_Username/Repo_name/hovercard"]')  ### /GithubUsername/PrivateRepoName/hovercard
my_element.click()
driver.implicitly_wait(3)
my_element = driver.find_element(By.CSS_SELECTOR, 'span[class="d-none d-md-flex flex-items-center"]')
my_element.click()
driver.implicitly_wait(3)
my_element = driver.find_element(By.CSS_SELECTOR, 'button[class="dropdown-item btn-link"]')
my_element.click()
driver.implicitly_wait(3)
my_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Name your file…"]')
my_element.send_keys(str(X))
driver.implicitly_wait(3)
my_element = driver.find_element(By.ID,"submit-file")
my_element.click()
