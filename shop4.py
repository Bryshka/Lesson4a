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
Book1_btn = driver.find_element_by_css_selector("#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3").click()
Old_price = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span")
Old_price_get_text =Old_price.text
assert Old_price_get_text == "₹600.00"
New_price = driver.find_element_by_css_selector("#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span")
New_price_get_text = New_price.text
assert New_price_get_text == "₹450.00"
Book_list = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#product-169 > div.images > a > img"))).click()
Book_list_close = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close"))).click()
driver.quit()


