import unittest
from selenium import webdriver
from LoginPage import LoginPage
from home_page import HomePage
import time


def test_add_to_cart(self):
        
        # Home Page: Add products to cart
        homepage = HomePage(self.driver)
            homepage.add_product_to_cart("//*[@id="block_frame_featured_1769"]/div/div[1]/div[2]/div[3]/a/i")
            time.sleep(1)
            homepage.add_product_to_cart("//*[@id="block_frame_latest_1770"]/div/div[2]/div[2]/div[3]/a/i")
            time.sleep(1)
            homepage.add_product_to_cart("//*[@id="block_frame_bestsellers_1771"]/div/div[2]/div[2]/div[3]/a/i")
            time.sleep(1)

        # Navigate to Cart Page
        homepage.navigate_to_cart_page()
        time.sleep(2) 

        
        self.assertIn("Shopping Cart", self.driver.current_url)
