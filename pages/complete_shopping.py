from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CompleteShopping:
    home_URL = "https://automationteststore.com"
    shopping_cart_button = (By.XPATH, '//span[@class="cart-label"]')
    fragrance_icon = (By.XPATH, '//*[@id="categorymenu"]/nav[1]/ul[1]/li[5]/a[1]')
    men_fragrance_icon = (By.XPATH, '//*[@id="maincontainer"]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/img[1]')
    ck_deodorant_icon = (By.XPATH, '//*[@id="maincontainer"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/img[1]')
    add_to_cart_button = (By.XPATH, '//*[@id="product"]/fieldset[1]/div[4]/ul[1]/li[1]/a[1]')
    continue_shopping = (By.XPATH, '//*[@id="cart"]/div[1]/div[3]/div[1]/a[1]')
    checkout_button = (By.XPATH, '//*[@id="cart_checkout2"]')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10) 

    def load(self):
        
        self.browser.get(CompleteShopping.home_URL)
        self.browser.maximize_window()
        time.sleep(3)  

    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            assert element is not None , "element not found "
            element.click()
        except Exception as e:
            raise Exception(f"Unable to click element with locator {locator}: {e}")

    def click_fragrance_icon(self):
        self.click_element(CompleteShopping.fragrance_icon)

    def click_men_fragrance_icon(self):
        self.click_element(CompleteShopping.men_fragrance_icon)

    def click_ck_deodorant_icon(self):
        self.click_element(CompleteShopping.ck_deodorant_icon)

    def click_add_to_cart(self):
        self.click_element(CompleteShopping.add_to_cart_button)
    def click_continue_shopping(self):
        self.click_element(CompleteShopping.continue_shopping)
    def click_checkout(self):
        self.click_element(CompleteShopping.checkout_button)
