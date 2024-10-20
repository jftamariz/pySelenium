import re
from pages.base_page import *
from pages.details import PropertyDetails
from util.util import convert


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_element((By.ID, "results-display"), 6)
        self.result_list = self._get_search_result_cards();

    def _get_search_result_cards(self):
        return self.get_elements(By.CSS_SELECTOR, '[data-rf-test-name="mapHomeCard"]')

    def get_total_sarch_result_number(self):
        total_homes = self.read((By.CSS_SELECTOR, '[data-rf-test-id="homes-description"]'))
        return int(re.search(r'of (.*?) homes', total_homes).group(1))

    def read_property_card_price(self, index):
        cards = self.result_list
        price = self.read((By.CSS_SELECTOR, '[class*="Homecard__Price"]'), cards[index])
        return convert(price)

    def read_property_card_bed_number(self, index):
        cards = self.result_list
        bedrooms = self.read((By.CSS_SELECTOR, '[class*="Homecard__Stats--beds"]'), cards[index])
        bedrooms_number = bedrooms.split(' ')[0]
        if "-" in bedrooms_number:
            return bedrooms_number.split('-')[1]
        return int(bedrooms_number)

    def read_property_card_bath_number(self, index):
        cards = self.result_list
        baths = self.read((By.CSS_SELECTOR, '[class*="Homecard__Stats--baths"]'), cards[index])
        baths_number = baths.split(' ')[0]
        if "-" in baths_number:
            return baths_number.split('-')[1]
        return int(float(baths_number))

    def read_property_card_size_sqft(self, index):
        cards = self.result_list
        sqft = self.read((By.CSS_SELECTOR, '[class*="Homecard__Stats--sqft"]'), cards[index])
        sqft_number = sqft.split(' ')[0]
        if "-" in sqft_number:
            return sqft_number.split('-')[1]
        return convert(sqft_number)

    def read_property_card_address(self, index: int) -> str:
        cards = self.result_list
        address = self.read((By.CSS_SELECTOR, '[class*="Homecard__Address"]'), cards[index])
        return address

    def read_property_card_phone(self, index: int) -> str:
        cards = self.result_list
        return self.read((By.CSS_SELECTOR, '[class*="Homecard__Attribution"]'), cards[index])

    def view_property_card(self, index: int) -> None:
        cards = self.result_list
        self.click((By.CSS_SELECTOR, '[data-rf-test-name="basicNode-homeCard"]'), cards[index])

        return PropertyDetails(self.driver)

    def read_search_type_filter(self) -> str:
        filters = self.get_elements(By.CSS_SELECTOR, '[class*="RichSelect__button"]')
        return self.read((By.XPATH, ".//p"), filters[0])

    def read_header(self) -> str:
        return self.read((By.CSS_SELECTOR, '[data-rf-test-id="h1-header"]'))
