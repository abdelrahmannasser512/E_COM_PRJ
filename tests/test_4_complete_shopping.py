from pages.complete_shopping import CompleteShopping
import time

def test_Complete_shopping(browser):
    complete_Shopping=CompleteShopping(browser)
    complete_Shopping.load()
    time.sleep(2)
    complete_Shopping.click_fragrance_icon()
    time.sleep(2)
    complete_Shopping.click_men_fragrance_icon()
    time.sleep(2)
    complete_Shopping.click_ck_deodrant_icon()
    time.sleep(2)
    complete_Shopping.click_add_to_cart_ck_deodrant_button()
    time.sleep(2)
    complete_Shopping.click_checkout_button()
    time.sleep(5)