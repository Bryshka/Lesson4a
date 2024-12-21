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
Email = driver.find_element_by_css_selector('#username')
Email.send_keys("4abka@mail.ru")
Password = driver.find_element_by_css_selector('#password')
Password.send_keys("Reg13579!")
Log_btn = driver.find_element_by_css_selector('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button').click()
time.sleep(3)
Logout = driver.find_element_by_css_selector("#page-36 > div > div.woocommerce > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a")
Logout_get_text = Logout.text
assert Logout_get_text == "Logout"
driver.close()