import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(1)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
SelRuB_btn = driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3').click()
Rev_btn = driver.find_element_by_css_selector('#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a').click()
Five_btn = driver.find_element_by_css_selector('#commentform > p.comment-form-rating > p > span > a.star-5').click()
Review = driver.find_element_by_css_selector('#comment')
Review.send_keys("Nice book!")
Name = driver.find_element_by_css_selector('#author')
Name.send_keys("Petr")
Mail = driver.find_element_by_css_selector('#email')
Mail.send_keys("Petr@mail.ru")
Sub_btn = driver.find_element_by_css_selector('#submit').click()
time.sleep(3)
driver.close()