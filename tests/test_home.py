import unittest
from selenium import webdriver
#from pages.login import WebLoginPage
from pages.home import HomePage
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_add_to_cart(driver):
        
        # Home Page: Add products to cart
        homepage = HomePage(driver)
        homepage.add_products_to_cart("//*[@id='block_frame_featured_1769']/div/div[1]/div[2]/div[3]/a/i")
        time.sleep(1)
        homepage.add_products_to_cart("//*[@id='block_frame_latest_1770']/div/div[2]/div[2]/div[3]/a/i")
        time.sleep(1)
        homepage.add_products_to_cart("//*[@id='block_frame_bestsellers_1771']/div/div[2]/div[2]/div[3]/a/i")
        time.sleep(1)

        # Navigate to Cart Page
        homepage.navigate_to_cart_page()
        time.sleep(2) 

        
        #self.assertIn("Shopping Cart", self.driver.current_url)
