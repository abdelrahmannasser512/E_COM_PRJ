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



class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # locators
        self.product_quantity_field = (By.XPATH, "//*[@id="cart_quantity66"]") 
        self.update_button = (By.XPATH, "//*[@id="cart_update"]") 
        self.delete_button = (By.XPATH, "//*[@id="cart"]/div/div[1]/table/tbody/tr[2]/td[7]/a/i")  
        self.checkout_button = (By.XPATH, "//*[@id="cart_checkout1"]")
        self.confirm_order_button = (By.XPATH, "//*[@id="checkout_btn"]") 

    def increase_product_quantity(self, quantity):
        quantity_field = self.driver.find_elements(*self.product_quantity_field)
        quantity_field.clear() 
        quantity_field.send_keys(quantity)
        click_update = self.driver.find_elements(*self.update_button)
        click_update.click()

    def delete_product(self):
        delete_buttons = self.driver.find_elements(*self.delete_button)
        delete_buttons.click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def confirm_checkout(self):
        self.driver.find_element(*self.confirm_order_button).click()