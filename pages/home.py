from pages.base_page import *
from pages.authentication import *
from pages.cart import *
from selenium.webdriver.common.action_chains import ActionChains

class Home(BasePage):


    def __init__(self, driver):
        self.driver = driver
        
        if self.driver.current_url != "http://automationpractice.com/index.php":
            self.driver.get("http://automationpractice.com/index.php");
     
        self.wait_element((By.ID, "header_logo"))
        self.wait_element((By.ID, "homeslider"))


    def load(self):
        self.driver.get("http://automationpractice.com/index.php")
     
    def sign_in(self):
        self.wait_element((By.XPATH, "//a[@class='login']")).click()
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
        '''
            return list of Elements representing all Featured Products in the Home page
        '''
        home_items_region = self.wait_element((By.ID, "homefeatured"))
        return self.get_elements(By.XPATH, "li", home_items_region)

    def add_to_cart_home_feature_item_by_index(self, idx):
        '''
            Clicks on Add To Cart button from Featured Products in the Home page
        '''
        item = self.__get_home_feature_items()[idx]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", item)

        ActionChains(self.driver).move_to_element(item).perform()
   
        btn_add_cart = item.find_element(By.XPATH, "div/div[2]/div[2]/a[1]")
 
        btn_add_cart.click()
        self.wait_element((By.XPATH, "//*[@title='Continue shopping']")).click()
        self.sleep(2)
    

    