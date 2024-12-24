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


class WebLoginPage:

      LOGIN_URL=r"https://automationteststore.com/index.php?rt=account/login"
      login_name=(By.XPATH,'//*[@id="loginFrm_loginname"]')
      thepassword=(By.XPATH,'//*[@id="loginFrm_password"]')
      login_button=(By.XPATH,'//*[@id="loginFrm"]/fieldset[1]/button[1]')
         

      def __init__(self,browser):
            self.browser=browser
         
      def load(self):                 
            self.browser.get(WebLoginPage.LOGIN_URL)
            self.browser.maximize_window()
            time.sleep(10)
      def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            assert element is not None , "element not found "
            element.click()
        except Exception as e:
            raise Exception(f"Unable to click element with locator {locator}: {e}")

      def select_the_login_name(self):
            self.click_element(WebLoginPage.login_name).send_keys("abdelrahmannasser")
      def select__the_pass_word(self):
            self.click_element(WebLoginPage.thepassword).send_keys("rhrS!Jr5FPaKuV")
      def select_login_button(self):
            self.click_element(WebLoginPage.login_button) 
            time.sleep(2)
            
              
              
              
    

           
     
               

               
               
              
               
     