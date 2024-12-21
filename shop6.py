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
driver.execute_script("window.scrollBy(0, 300);")
Book1_btn = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
time.sleep(5)
Book2_btn = driver.find_element_by_css_selector('#content > ul > li.post-180.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
time.sleep(5)
Basket_btn = driver.find_element_by_css_selector('#wpmenucartli').click()
time.sleep(3)
Del_btn = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a').click()
Undo_btn = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div.woocommerce-message > a').click()
time.sleep(3)
Quan_btn = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
Quan_btn.clear()
Quan_btn.send_keys("3")
Upd_btn = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > input.button').click()
Quan_btn_val =Quan_btn.get_attribute("value")
assert Quan_btn_val == "3"
time.sleep(3)
Apply_btn = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button').click()
Text1 = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > ul > li")
Text1_get_text =Text1.text
assert Text1_get_text == "Please enter a coupon code."
driver.quit()
