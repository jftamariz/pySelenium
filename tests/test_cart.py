from test_base import *
from pages.home import Home
import pytest
import allure
from util.util import get_now_datetime


class TestCart(TestBase):
    
    @pytest.mark.smoke
    @allure.title("Cart - add item")
    @allure.description(" Verify user is able to add item to the cart - Last run: "+ get_now_datetime())
    def test_add_item_to_cart(self, driver):
        home = Home(driver)
        home.add_to_cart_home_feature_item_by_index(0)
        home.add_to_cart_home_feature_item_by_index(3)
        items = home.cart().get_cart_items()
        
        assert len(items) == 2," - Expected for two products to be Cart.    Actual: {0} products are in the Cart".format(len(items))
    
 