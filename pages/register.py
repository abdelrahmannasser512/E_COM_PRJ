from selenium.webdriver.common.by import By
from selenium import webdriver
import pickle
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select





class Register:
    
    URL= r"https://automationteststore.com/index.php?rt=account/login"
    coninue_button=(By.XPATH,"//button[@title='Continue']")
    first_name=(By.XPATH,'//*[@id="AccountFrm_firstname"]')
    last_name=(By.XPATH,'//*[@id="AccountFrm_lastname"]')
    email=(By.XPATH,'//*[@id="AccountFrm_email"]')
    adrress_1=(By.XPATH,'//*[@id="AccountFrm_address_1"]')
    city=(By.XPATH,'//*[@id="AccountFrm_city"]')
    state=(By.XPATH,'//*[@id="AccountFrm_zone_id"]')
    country=(By.XPATH,'//*[@id="AccountFrm_country_id"]')
    login_name=(By.XPATH,"//input[@name='loginname']")
    thepassword=(By.XPATH,"//input[@name='password']")
    confirm_password=(By.XPATH,"//input[@name='confirm']")
    privacy_policy=(By.XPATH,"//input[@type='checkbox']")
    ZIP_CODE=(By.XPATH,"//input[@name='postcode']")
    continue_button2=(By.XPATH,"//button[@title='Continue']")




    def __init__(self,browser):
        self.browser=browser

    def load(self):
        self.browser.get(Register.URL)
        self.browser.maximize_window()
    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            assert element is not None , "element not found "
            element.click()
        except Exception as e:
            raise Exception(f"Unable to click element with locator {locator}: {e}")
    def send_element_keys(self, locator,sended_item):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            assert element is not None , "element not found "
            element.send_keys(sended_item)
        except Exception as e:
            raise Exception(f"Unable to click element with locator {locator}: {e}")

    def click_continue(self):

        self.click_element(Register.coninue_button)
        time.sleep(5)
    def select_first_name(self):
        self.send_element_keys(Register.first_name,"Abdelrahman")
        
    def select_last_name(self):
        self.send_element_keys(Register.first_name,"sayednasserahmed")

    def select_e_mail(self):
        self.send_element_keys(Register.email,"sayednasserahmed")

    def select_country(self):
        country_dropdown = self.browser.find_element(*Register.country)
        select = Select(country_dropdown)
        select.select_by_value("63")

    def select_state(self):
        state_dropdown = self.browser.find_element(*Register.state)
        select = Select(state_dropdown)
        select.select_by_value("1008")

    def select_city(self):
        self.send_element_keys(Register.city,"4hhn.cairo.egypt.africa")

    def select_address_1(self):
        self.send_element_keys(Register.adrress_1,"4hhn.cairo.egypt.africa")

    def select_zip_code(self):
        self.send_element_keys(Register.adrress_1,"10025")

    def select_the_login_name(self):
        self.send_element_keys(Register.login_name,"abdelrahmannasser")

    def select__the_pass_word(self):
        self.send_element_keys(Register.thepassword,"rhrS!Jr5FPaKuV")

    def select_confirm_pass_word(self):
        self.send_element_keys(Register.coninue_button,"rhrS!Jr5FPaKuV")

    def click_privacy_policy(self):

        self.click_element(Register.privacy_policy)
    def click_continue_button(self):

        self.click_element(Register.continue_button2)
        time.sleep(5)
        webdriver.Chrome().quit()