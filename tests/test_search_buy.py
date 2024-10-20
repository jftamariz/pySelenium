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
        zip_code = "22180"

        home = Home(driver)
        results = home.search_to_buy(zip_code)
        assert f'{zip_code}', 'homes for sale' in results.read_header()
        assert results.read_search_type_filter() == 'For sale'

    @pytest.mark.smoke
    @allure.title("Buy - Search")
    @allure.description(" Verify user is able to search for homes to buy - Last run: " + get_now_datetime())
    def test_search_to_buy(self, driver):
        home = Home(driver)
        results = home.search_to_buy("20120")
        search_result_total_label = results.get_total_sarch_result_number()

        assert search_result_total_label == len(results.result_list), "The total search result label is 2 more" \
                                                                     " of the actual home listed in the result"
        target_property_result_index = 1
        assert results.read_property_card_price(target_property_result_index) > 1000
        assert results.read_property_card_bed_number(target_property_result_index) > 1
        assert results.read_property_card_bath_number(target_property_result_index) > 1
        assert results.read_property_card_size_sqft(target_property_result_index) > 1
        assert len(results.read_property_card_phone(target_property_result_index)) == 14
