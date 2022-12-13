from pages.base_page import *
from pages.authentication import *
from pages.cart import *
from pages.homes import Homes
from pages.rentals import Rentals
from pages.search_result import SearchPage
from selenium.webdriver.common.action_chains import ActionChains


class Home(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        
        if self.driver.current_url != "https://www.redfin.com":
            self.driver.get("https://www.redfin.com");
        self.wait_element((By.CSS_SELECTOR, '[data-rf-test-name="search-box-input"]'))

    def load(self):
        self.driver.get("https://www.redfin.com")
     
    def sign_in(self):
        self.wait_element((By.CSS_SELECTOR, '[data-rf-test-name="SignInLink"]')).click()
        return Authentication(self.driver)

    def cart(self):
        self.click((By.XPATH, "//div[@class='shopping_cart']/a"))
        return Cart(self.driver)

    def contact_us(self):
        pass

    def women(self):
        pass

    def dresses(self):
        pass

    def __get_home_feature_items(self):   
        """
            return list of Elements representing all Featured Products in the Home page
        """
        home_items_region = self.wait_element((By.ID, "homefeatured"))
        return self.get_elements(By.XPATH, "li", home_items_region)

    def add_to_cart_home_feature_item_by_index(self, idx):
        """
            Clicks on Add To Cart button from Featured Products in the Home page
        """
        item = self.__get_home_feature_items()[idx]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", item)

        ActionChains(self.driver).move_to_element(item).perform()
   
        btn_add_cart = item.find_element(By.XPATH, "div/div[2]/div[2]/a[1]")
 
        btn_add_cart.click()
        self.wait_element((By.XPATH, "//*[@title='Continue shopping']")).click()
        self.sleep(2)

    def search_to_buy(self, search_term) -> Homes:
        self.click((By.CSS_SELECTOR, '[data-rf-test-name="searchTab"]'))
        self.write((By.CSS_SELECTOR, '[data-rf-test-name="search-box-input"]'), "22003")
        self.click((By.CSS_SELECTOR, '[data-rf-test-name="searchButton"]'))
        self.sleep(3)
        return Homes(self.driver)

    def search_to_rent(self, search_term) -> Rentals:
        self.click((By.CSS_SELECTOR, '[data-rf-test-name="rentTab"]'))
        self.write((By.CSS_SELECTOR, '[data-rf-test-name="search-box-input"]'), "22003")
        self.click((By.CSS_SELECTOR, '[data-rf-test-name="searchButton"]'))
        self.sleep(3)
        return Rentals(self.driver)