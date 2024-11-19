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
            #      self.browser.delete_all_cookies()
                 
            self.browser.get(WebLoginPage.LOGIN_URL)
            self.browser.maximize_window()
            time.sleep(10)


                 
        
      def select_the_login_name(self):
            select_login_name=self.browser.find_element(*WebLoginPage.login_name)
            select_login_name.send_keys("abdelrahmannasser")

      def select__the_pass_word(self):
            select_login_password=self.browser.find_element(*WebLoginPage.thepassword)
            select_login_password.send_keys("rhrS!Jr5FPaKuV")

      def select_login_button(self):
            click_login_button  = self.browser.find_element(*WebLoginPage.login_button)
           
            ActionChains(self.browser).click(click_login_button).perform()
            time.sleep(2)
            
              
              
              
    

           
     
               

               
               
              
               
     