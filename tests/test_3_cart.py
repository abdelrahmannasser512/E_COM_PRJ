from pages.complete_shopping import CompleteShopping
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_cart(browser):
    cart_page=CompleteShopping(browser)
    cart_page.load()
    cart_page.click_jewelry_icon()
    cart_page.add_to_cart_flower_girl()
    
    cart_page.click_shopping_cart()
    
    cart_page.click_terms_of_service_checkbox()
    cart_page.click_checkout_button()
    time.sleep(3)

