from pages.components.search_type import SearchType
from test_base import *
from pages.home import Home
import pytest
import allure
from util.util import get_now_datetime


class TestSearchToRent(TestBase):

    @pytest.mark.smoke
    @allure.title("Rent - Search")
    @allure.description(" Verify user is able to search for homes to rent - Last run: " + get_now_datetime())
    def test_user_views_search_results_to_rent(self, driver):
        zip_code = "22003"
        state = "VA"

        home = Home(driver)
        results = home.search_to_rent(zip_code)
        assert results.read_header() == f'{zip_code}, {state} rental listings'
        assert results.read_search_type_filter() == 'For rent'

    @pytest.mark.smoke
    @allure.title("Rent - Search")
    @allure.description(" Verify user is able to search for homes to rent - Last run: " + get_now_datetime())
    def test_user_views_rental_property_details(self, driver):
        home = Home(driver)
        results = home.search_to_rent("22003")
        results.get_total_sarch_result_number()

        target_property_result_index = 4
        assert results.read_property_card_price(target_property_result_index) > 100
        assert results.read_property_card_bed_number(target_property_result_index) > 1
        assert results.read_property_card_bath_number(target_property_result_index) > 1
        assert results.read_property_card_size_sqft(target_property_result_index) > 1
        assert results.read_porperty_card_type() == SearchType.RENT.value