from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from util.util import convert


class PropertyDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        p = driver.current_window_handle
        for tab in self.driver.window_handles:
            # switch focus to child window
            if tab != p:
                driver.switch_to.window(tab)

        self.wait_element((By.CSS_SELECTOR, '[data-rf-test-id="mediaBrowser"]'), 6)

    def price(self):
        return convert(self.read((By.XPATH, '//div[@data-rf-test-id="abp-price"]/div')))

    def bedrooms(self):
        return convert(self.read((By.XPATH, '//div[@data-rf-test-id="abp-beds"]/div')))

    def bathrooms(self):
        return int(float(self.read((By.XPATH, '//div[@data-rf-test-id="abp-baths"]/div'))))

    def sqft(self):
        return convert(self.read((By.XPATH, '//div[@data-rf-test-id="abp-sqFt"]/span')))
