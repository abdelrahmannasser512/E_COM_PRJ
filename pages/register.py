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

    def click_continue(self):

        click_continue_button_element = self.browser.find_element(*Register.coninue_button)
        ActionChains(self.browser).click(click_continue_button_element).perform()
        time.sleep(5)
    def select_first_name(self):
        select_first_name_blank=self.browser.find_element(*Register.first_name)
        select_first_name_blank.send_keys("Abdelrahman")

    def select_last_name(self):
        select_last_name_blank=self.browser.find_element(*Register.last_name)
        select_last_name_blank.send_keys("sayednasserahmed")

    def select_e_mail(self):
        select_email=self.browser.find_element(*Register.email)
        select_email.send_keys("abdelrahmannasser512@gmail.com")
    def select_country(self):

        country_dropdown = self.browser.find_element(*Register.country)
        select = Select(country_dropdown)
        select.select_by_value("63")
    def select_state(self):

        state_dropdown = self.browser.find_element(*Register.state)
        select = Select(state_dropdown)
        select.select_by_value("1008")
    def select_city(self):
        select_city=self.browser.find_element(*Register.city)
        select_city.send_keys("4hhn.cairo.egypt.africa")
    def select_address_1(self):
        select_address_1=self.browser.find_element(*Register.adrress_1)
        select_address_1.send_keys("4hhn.cairo.egypt.africa")
    def select_zip_code(self):
        select_zip_code=self.browser.find_element(*Register.ZIP_CODE)
        select_zip_code.send_keys("4hhn.cairo.egypt.africa")

    def select_the_login_name(self):
        select_login_name=self.browser.find_element(*Register.login_name)
        select_login_name.send_keys("abdelrahmannasser")

    def select__the_pass_word(self):
        select_login_password=self.browser.find_element(*Register.thepassword)
        select_login_password.send_keys("rhrS!Jr5FPaKuV")

    def select_confirm_pass_word(self):
        select_confirm_password=self.browser.find_element(*Register.confirm_password)
        select_confirm_password.send_keys("rhrS!Jr5FPaKuV")
    def click_privacy_policy(self):

        click_privacy_polic_element = self.browser.find_element(*Register.privacy_policy)
        ActionChains(self.browser).click(click_privacy_polic_element).perform()
    def click_continue_button(self):

        click_continue_button_element = self.browser.find_element(*Register.continue_button2)
        ActionChains(self.browser).click(click_continue_button_element).perform()
        time.sleep(5)
        webdriver.Chrome().quit()