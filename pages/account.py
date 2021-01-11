from pages.base_page import *

class Account(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.wait_text_element((By.XPATH, "//h1[@class='page-heading']"), "MY ACCOUNT")

    def read_account_welcome_msg(self):
        return self.read((By.XPATH, "//div[@id='center_column']/p"))

    def order_history_details(self):
        pass

    def credit_slips(self):
        pass

    def addresses(self):
        pass

    def personal_information(self):
        pass

    def wish_list(self):
        pass

