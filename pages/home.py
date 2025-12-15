from pages.base_page import *
from pages.authentication import *
from pages.cart import *
from pages.homes import Homes
from pages.rentals import Rentals


class Home(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
        if self.driver.current_url != "https://www.redfin.com":
            self.driver.get("https://www.redfin.com");
        self.wait_element((By.CSS_SELECTOR, '[data-rf-test-name="search-box-input"]'))

    def load(self):
        self.driver.get("https://www.redfin.com")
     
    def sign_in(self):
        self.wait_element((By.CSS_SELECTOR, '[data-rf-test-name="SignInLink"]')).click()
        return Authentication(self.driver)

    def search_to_buy(self, search_term: str) -> Homes:
        # self.click((By.CSS_SELECTOR, '[data-text="Buy"]'))
        # self.click((By.CSS_SELECTOR, '[data-rf-test-name="search-box-input"]'))
        # self.write((By.CSS_SELECTOR, '[data-rf-test-name="search-box-input"]'), search_term)
        # self.click((By.CSS_SELECTOR, '[data-rf-test-name="searchButton"]'))
        self.driver.get('https://www.redfin.com/zipcode/'+search_term)
        return Homes(self.driver)

    def search_to_rent(self, search_term: str) -> Rentals:
        self.click((By.CSS_SELECTOR, '[data-text="Rent"]'))
        self.write((By.CSS_SELECTOR, '[data-rf-test-name="search-box-input"]'), search_term)
        self.click((By.CSS_SELECTOR, '[data-rf-test-name="searchButton"]'))
        return Rentals(self.driver)
