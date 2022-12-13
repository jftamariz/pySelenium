from selenium.webdriver.common.by import By
from pages.search_result import SearchPage


class Homes(SearchPage):

    def __init__(self, driver):
        super().__init__(driver)

    def read_property_card_phone(self, index):
        cards = self._get_search_result_cards()
        phone = self.read((By.CSS_SELECTOR, '[class="brokerageDisclaimerV2"]'), cards[index], False)
        return phone