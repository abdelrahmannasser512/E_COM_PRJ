from pages.login import WebLoginPage
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_login(browser):
    login_page=WebLoginPage(browser)
    login_page.load()
    login_page.select_the_login_name()
    time.sleep(5)
    login_page.select__the_pass_word()
    time.sleep(5)
    login_page.select_login_button()
    time.sleep(3)



    