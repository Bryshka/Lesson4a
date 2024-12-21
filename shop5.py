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
Book1_btn = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
time.sleep(5)
Count = driver.find_element_by_css_selector("#wpmenucartli > a > span.cartcontents")
Count_get_text =Count.text
assert Count_get_text == "1 Item"
price = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount")
price_get_text =price.text
assert price_get_text == "₹180.00"
Basket_btn = driver.find_element_by_css_selector('#wpmenucartli').click()
wait = WebDriverWait(driver,10)
Subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span"),"₹180.00"))
Total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td"),"₹183.60"))
driver.quit()