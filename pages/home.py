from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.product_add_button
        #self.product_1_add_button = (By.XPATH, "//*[@id="block_frame_featured_1769"]/div/div[1]/div[2]/div[3]/a/i")
        self.cart_page_link = (By.XPATH, "/html/body/div/header/div[2]/div/div[3]/ul/li/a")

    def add_products_to_cart(self,add_button):
        product_add_button = (By.XPATH, add_button)
        product_add_button = self.driver.find_elements(*self.add_button)
        product_add_button.click()


    def navigate_to_cart_page(self):
        self.driver.find_element(*self.cart_page_link).click()