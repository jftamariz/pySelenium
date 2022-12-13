from pages.base_page import *
from pages.authentication import *
from pages.cart import *


class CreateAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait_element((By.ID, "customer_firstname"))

    def write_first_name(self, firstname):
        self.write((By.ID, "customer_firstname"))

    def write_last_name(self, lastname):
        self.write((By.ID, "customer_lastname"))

    def read_email(self):
        return self.read((By.ID, "email"))

    def write_password(self, password):
        self.write((By.ID, "passwd"))

    def write_address(self, address):
        self.write((By.ID, "address1"))

    def write_city(self, city):
        self.write((By.ID, "city"))

    def write_state(self, state):
        self.select_options((By.ID, "id_state"), "Virginia")

    def write_zipcode(self, zipcode):
        self.write((By.ID, "postcode"))

    def read_country(self):
        return self.read((By.ID, "uniform-id_country"))

    def write_mobile_phone(self, mobile_phone):
        self.write((By.ID, "phone_mobile"))

    def read_alias(self):
        return self.read((By.ID, "alias"))

    def click_register(self):
        self.click((By.ID, "submitAccount"))



