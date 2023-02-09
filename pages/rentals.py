from pages.search_result import SearchPage
from selenium.webdriver.common.by import By


class Rentals(SearchPage):

    def __init__(self, driver):
        super().__init__(driver)

    def read_porperty_card_type(self, index: int) -> str:
        cards = self._get_search_result_cards()
        property_type = self.read((By.CSS_SELECTOR, '[class*="PropertyTypeDisplay"]'), cards[index], False)
        return property_type
