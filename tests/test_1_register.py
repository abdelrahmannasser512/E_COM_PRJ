from pages.register import Register
from selenium.webdriver.support.ui import WebDriverWait
import time

def test_register(browser):
    register_page=Register(browser)
    register_page.load()
    register_page.click_continue()
    register_page.select_first_name()
    register_page.select_last_name()
    register_page.select_e_mail()
    register_page.select_country()
    register_page.select_city()
    register_page.select_state()
    register_page.select_address_1()
    register_page.select_zip_code()
    register_page.select_the_login_name()
    register_page.select__the_pass_word()
    register_page.select_confirm_pass_word()
    register_page.click_privacy_policy()
    register_page.click_continue_button()


    time.sleep(10)
    

