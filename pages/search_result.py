from pages.base_page import *
from pages.details import PropertyDetails
from util.util import convert


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_element((By.ID, "results-display"), 6)

    def _get_search_result_cards(self):
        return self.get_elements(By.CSS_SELECTOR, '[data-rf-test-name="mapHomeCard"]')

    def get_total_sarch_result_number(self):
        total_homes_found = self.read((By.CSS_SELECTOR, '[data-rf-test-id="homes-description"]'))

    def read_property_card_price(self, index):
        cards = self._get_search_result_cards()
        price = self.read((By.CSS_SELECTOR, '[data-rf-test-name="homecard-price"]'), cards[index])
        return convert(price)

    def read_property_card_bed_number(self, index):
        cards = self._get_search_result_cards()
        bedrooms = self.read((By.XPATH, "//div[@class='HomeStatsV2 font-size-small ']/div[1]"), cards[index])
        bedrooms_number = bedrooms.split(' ')[0]
        if "-" in bedrooms_number:
            return bedrooms_number.split('-')[1]
        return int(bedrooms_number)

    def read_property_card_bath_number(self, index):
        cards = self._get_search_result_cards()
        baths = self.read((By.XPATH, "//div[@class='HomeStatsV2 font-size-small ']/div[2]"), cards[index])
        baths_number = baths.split(' ')[0]
        if "-" in baths_number:
            return baths_number.split('-')[1]
        return int(baths_number)

    def read_property_card_size_sqft(self, index):
        cards = self._get_search_result_cards()
        sqft = self.read((By.XPATH, "//div[@class='HomeStatsV2 font-size-small ']/div[3]"), cards[index])
        sqft_number = sqft.split(' ')[0]
        if "-" in sqft_number:
            return sqft_number.split('-')[1]
        return convert(sqft_number)

    def read_property_card_address(self, index):
        cards = self._get_search_result_cards()
        address = self.read((By.CSS_SELECTOR, '[data-rf-test-id="abp-streetLine"]'), cards[index], False)
        return address

    def view_property_card(self, index):
        cards = self._get_search_result_cards()
        self.click((By.CSS_SELECTOR, '[data-rf-test-name="basicNode-homeCard"]'), cards[index])
        return PropertyDetails(self.driver)

    def read_search_mode_filter(self):
        return self.read((By.CSS_SELECTOR, '[class*="desktopExposedSearchModeContainer"]'))

    def read_header(self):
        return self.read((By.CSS_SELECTOR, '[data-rf-test-id="h1-header"]'))
