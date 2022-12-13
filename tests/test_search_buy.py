from test_base import *
from pages.home import Home
import pytest
import allure
from util.util import get_now_datetime


class TestSearchToBuy(TestBase):

    @pytest.mark.smoke
    @allure.title("Rent - Search")
    @allure.description(" Verify user is able to search for homes to rent - Last run: " + get_now_datetime())
    def test_user_views_search_results_to_buy(self, driver):
        zip_code = "22003"

        home = Home(driver)
        results = home.search_to_buy(zip_code)
        assert results.read_header() == f'{zip_code} Homes for Sale'
        assert results.read_search_mode_filter() == 'For sale'

    @pytest.mark.smoke
    @allure.title("Buy - Search")
    @allure.description(" Verify user is able to search for homes to buy - Last run: " + get_now_datetime())
    def test_search_to_buy(self, driver):
        home = Home(driver)
        results = home.search_to_buy("22003")
        results.get_total_sarch_result_number()
        target_property_result_index = 1
        results.read_property_card_price(target_property_result_index)
        total_bebs = results.read_property_card_bed_number(target_property_result_index)
        total_baths = results.read_property_card_bath_number(target_property_result_index)
        total_sqft = results.read_property_card_size_sqft(target_property_result_index)
        phone = results.read_property_card_phone(target_property_result_index)

        results.view_property_card(0)
        results.sleep(4)

