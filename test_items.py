from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_found_cart_button(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, 'Add to cart button is present'
    


