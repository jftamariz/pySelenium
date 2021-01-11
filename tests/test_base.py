import sys
import os
import pytest
import time
import allure
from selenium import webdriver
from util.driver_factory import *



class TestBase():

    
    @pytest.fixture(scope="session")
    def driver(request, test_args):
        driver = DriverFactory.create_web_driver(**test_args)
        if driver:
            return driver
        else:
            TestBase.skip_test(" invalid Driver. ")
    
    @pytest.fixture(scope="session")
    def setup_teardown(request, driver):
        # Setup


        yield
        # Tear Down 
        driver.close()
        driver.quit()
        

    @pytest.fixture
    def user(request, test_args):
        if  test_args["email"] and test_args["password"]:
            return {"email":test_args["email"],
                    "password": test_args["password"]}
        else:
            return None

    @staticmethod
    def skip_test( message=None):
        from colorama import Fore, Back, Style, init
        init()
        print(Fore.YELLOW," [Skip] - Test Case:  {0}".format(message))
        pytest.skip(" [Skip] - Test Case:  {0}".format(message))
        print(Style.RESET_ALL)

