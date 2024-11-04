from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select

class CompleteShopping:
    shopping_cart_button=(By.XPATH,'//span[@class="cart-label"]')
    jewelry_icon=(By.XPATH,'//*[@class="top-menu notmobile"]/li/a[@href="/jewelry"]')
    add_to_cart_flower_girl_button=(By.XPATH,'//*[@id="main"]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]/button[1]')
    terms_of_service_checkbox=(By.XPATH,"//input[@id='termsofservice']")
    checkout_button=(By.XPATH,"//button[@id='checkout']")
    def __init__(self,browser):
        self.browser=browser
    def click_jewelry_icon(self):
        select_jewelry_icon=ActionChains(self.browser).click(self.browser.find_element(*CompleteShopping.jewelry_icon)).perform()
    
    def add_to_cart_flower_girl(self):
        select_add_to_cart_flower_girl_button=ActionChains(self.browser).click(self.browser.find_element(*CompleteShopping.add_to_cart_flower_girl_button)).perform()
    def click_shopping_cart(self):
        select_shopping_cart_button=ActionChains(self.browser).click(self.browser.find_element(*CompleteShopping.shopping_cart_button)).perform()
    def click_terms_of_service_checkbox(self):
        select_terms_of_service_checkbox=ActionChains(self.browser).click(self.browser.find_element(*CompleteShopping.terms_of_service_checkbox)).perform()
    def click_checkout_button(self):
        select_checkout_button=ActionChains(self.browser).click(self.browser.find_element(*CompleteShopping.checkout_button)).perform()
        
    


