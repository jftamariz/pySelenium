from pages.search_result import SearchPage
from selenium.webdriver.common.by import By


class Rentals(SearchPage):

    def __init__(self, driver):
        super().__init__(driver)

    def read_porperty_card_type(self, index: int) -> str:
        return self.read((By.CSS_SELECTOR, '[class*="RichSelect__button"]'))
