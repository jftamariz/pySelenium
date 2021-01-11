from pages.base_page import *

class Cart(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.wait_text_element((By.XPATH, "//h1[@class='page-heading']"), "SHOPPING-CART SUMMARY")

    def read_cart_message(self):
        return self.read((By.XPATH, "//*[@id='center_column']/p"))


    def get_cart_items(self):
        cart_table = self.wait_element((By.ID, "cart_summary"))
        return self.get_elements(By.XPATH, "tbody/tr", cart_table)