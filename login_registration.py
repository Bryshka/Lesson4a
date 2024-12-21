import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

Account_btn = driver.find_element_by_css_selector('#menu-item-50 > a').click()
Email = driver.find_element_by_css_selector('#reg_email')
Email.send_keys("4abka@mail.ru")
Password = driver.find_element_by_css_selector('#reg_password')
Password.send_keys("Reg13579!")
Reg_btn = driver.find_element_by_css_selector('#customer_login > div.u-column2.col-2 > form > p.woocomerce-FormRow.form-row > input.woocommerce-Button.button').click()
time.sleep(3)
driver.close()


