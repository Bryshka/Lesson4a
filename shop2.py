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
Shop_btn = driver.find_element_by_css_selector('#menu-item-40 > a').click()
HTML_btn = driver.find_element_by_css_selector('#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a').click()
items_count = driver.find_elements_by_class_name("product_cat-html")
if len(items_count) == 3:
    print("В категории 3 товара")
else:
    print("Ошибка. Количество товаров в категории: " + str(len(items_count)))

driver.close()
