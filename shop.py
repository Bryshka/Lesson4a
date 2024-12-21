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
Book1_btn = driver.find_element_by_css_selector("#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3").click()
Book1 = driver.find_element_by_css_selector("#product-181 > div.summary.entry-summary > h1")
Book1_get_text = Book1.text
assert Book1_get_text == "HTML5 Forms"

driver.close()
