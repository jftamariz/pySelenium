from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PropertyDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_element((By.CSS_SELECTOR, '[data-rf-test-id="mediaBrowser"]'), 6)

    def read_price(self):
        return self.read((By.CSS_SELECTOR, '[data-rf-test-id="abp-price"]'))