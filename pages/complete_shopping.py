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
    home_URL=r"https://automationteststore.com"
    shopping_cart_button=(By.XPATH,'//span[@class="cart-label"]')
    fragrance_icon=(By.XPATH,'//*[@id="categorymenu"]/nav[1]/ul[1]/li[5]/a[1]')
    men_fragrance_icon=(By.XPATH,'//*[@id="maincontainer"]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/img[1]')
    
    ck_deodrant_icon=(By.XPATH,'//*[@id="maincontainer"]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/img[1]')
    
    add_to_cart_ck_deodrant_button=(By.XPATH,'//*[@id="product"]/fieldset[1]/div[4]/ul[1]/li[1]/a[1]')
    
    continue_shopping=(By.XPATH,'//*[@id="cart"]/div[1]/div[3]/div[1]/a[1]')
    checkout_button=(By.XPATH,'//*[@id="cart_checkout2"]')
    def __init__(self,browser):
        self.browser=browser
    def load(self):
            #      self.browser.delete_all_cookies()
                 
            self.browser.get(CompleteShopping.home_URL)
            self.browser.maximize_window()
            time.sleep(3)

    def click_fragrance_icon(self):
        find_fragrance_icon = self.browser.find_element(*CompleteShopping.fragrance_icon)
        select_fragrance_icon_icon = ActionChains(self.browser).click(find_fragrance_icon).perform()
    def click_men_fragrance_icon(self):
        find_men_fragrance_icon = self.browser.find_element(*CompleteShopping.men_fragrance_icon)
        select_fragrance_icon_icon = ActionChains(self.browser).click(find_men_fragrance_icon).perform()
    def click_ck_deodrant_icon(self):
        find_ck_deodrant_icon = self.browser.find_element(*CompleteShopping.ck_deodrant_icon)
        select_fragrance_icon_icon = ActionChains(self.browser).click(find_ck_deodrant_icon).perform()
    
    def click_add_to_cart_ck_deodrant_button(self):
        find_click_add_to_ck_deodrant__button=ActionChains(self.browser).click(self.browser.find_element(*CompleteShopping.add_to_cart_ck_deodrant_button)).perform()
    def click_checkout_button(self):
        find_select_checkout_button=ActionChains(self.browser).click(self.browser.find_element(*CompleteShopping.checkout_button)).perform()
        
    


