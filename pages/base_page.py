import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class BasePage(object):
    """
    Base class that all page objects inheret from
    """
    __env = None

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, *by_loc):
        return self.driver.find_element(*by_loc)

    def get_elements(self, by, locator, element=None):
        if element:
            return element.find_elements(by, locator)
        else:
            return self.driver.find_elements(by, locator)

    def click(self, by_loc, element=None):
        if element:
            self.wait_element(by_loc, 3, element, False).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_loc)).click()

    def write(self, by_loc, message):
        input_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_loc))
        input_field.clear()
        input_field.send_keys(message)

    def read(self, by_loc, element=None, ignore_error=True):
        return self.wait_element(by_loc, 3, element, ignore_error).text

    def wait_element(self, by_loc, wait_time=6, element=None, ignore_error=True):
        """
            wait for element, and handled exception
        """
        try:
            if element:
                return WebDriverWait(element, wait_time).until(
                    EC.element_to_be_clickable(by_loc))
            else:
                return WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable(by_loc))

        except TimeoutException as e:
            if not ignore_error:
                print(" TimeoutException - Waiting for element: "+str(e))
            return None

    def wait_element_visibility(self, element):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of(element))

    def wait_text_element(self, by_loc, wait_text, wait_time=20):
        return WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(by_loc, wait_text))
   
    def sleep(self, time_sec):
        time.sleep(time_sec)

    def logout(self):
        self.hover_element(self.get_display_name())
        self.driver.find_element(By.LINK_TEXT, "Sign out").click()

    def read_error_alert(self):
        return self.read((By.CSS_SELECTOR, "[data-rf-test-id='validationFeedback']"))

    def read_sign_in_error(self):
        return self.read((By.CSS_SELECTOR, "[data-rf-test-name='message']"))

    def select_options(self, by_loc, value):
        select_by_value = Select(self.get_element(by_loc))
        select_by_value.select_by_visible_text(value)

    def zoom_out(self):
        self.driver.execute_script("document.body.style.zoom='zoom %'")

    def get_display_name(self):
        return self.wait_element((By.CSS_SELECTOR, '[data-rf-test-name="displayName"]'))

    def hover_element(self, elem):
        ActionChains(self.driver).move_to_element(elem).perform()

    def get_inner_html(self, elem):
        return elem.get_attribute('innerHTML')