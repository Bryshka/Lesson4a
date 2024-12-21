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
Basket_btn = driver.find_element_by_css_selector('#wpmenucartli').click()
wait = WebDriverWait(driver,10)
Proceed = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#page-34 > div > div.woocommerce > div.cart-collaterals > div > div > a"))).click()
Firstname = driver.find_element_by_css_selector('#billing_first_name')
Firstname.send_keys("Ivan")
Lastname = driver.find_element_by_css_selector('#billing_last_name')
Lastname.send_keys("Ivanov")
Phone = driver.find_element_by_css_selector("#billing_phone")
Phone.send_keys("3246587460")
Adress = driver.find_element_by_css_selector("#billing_address_1")
Adress.send_keys("Main street")
Town = driver.find_element_by_css_selector("#billing_city")
Town.send_keys("Jacarta")
ZIP = driver.find_element_by_css_selector("#billing_postcode")
ZIP.send_keys("435678")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
Check_btn = driver.find_element_by_css_selector("#payment_method_cheque").click()
Place_btn = driver.find_element_by_css_selector("#place_order").click()
Text1 = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
Text2 = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#page-35 > div > div.woocommerce > table.shop_table.order_details > tfoot > tr:nth-child(3) > td"),"Check Payments"))
driver.quit()

