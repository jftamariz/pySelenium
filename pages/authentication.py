from pages.base_page import *
from pages.account import *
import time


class Authentication(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.wait_element((By.CSS_SELECTOR, "[data-rf-test-name='dialogGutsNode']"))

    def write_email(self, email_address):
        self.write((By.CSS_SELECTOR, "input[name='emailInput']"), email_address)

    def write_password(self, password):
        time.sleep(2)
        self.write((By.CSS_SELECTOR, "input[name='passwordInput']"), password)

    def write_email_create_account(self, email_address):
        self.write((By.ID, "email_create"), email_address)

    def click_sign_in(self):
        self.click((By.CSS_SELECTOR, "input[value='Sign in']"))

    def sign_in(self):
        self.click_sign_in()
        return Account(self.driver)

    def click_create_account(self):
        self.click((By.ID, "SubmitCreate"))

    def read_error_create_account(self):
        error = self.read((By.ID, "create_account_error"))
        print("  error : "+ error)
        return self.read((By.ID, "create_account_error"))

    def read_error_sign_in(self):
        error = self.ready((By.CLASS_NAME, "alert alert-danger"))
        print("  sign in error: "+ error)

    def click_continue_with_email(self):
        self.click((By.CSS_SELECTOR, "[data-rf-test-name='submitButton']"))