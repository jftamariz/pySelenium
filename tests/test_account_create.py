from test_base import *
from pages.home import Home
from util.util import *


class TestAccountCreate(TestBase):



    @allure.title("Login - Create new account")
    @allure.description(" Verify user is able to create a new account - Last run: "+ getNowDateTime())
    def test_login_create_account(self, driver):

        auth = Home(driver).sign_in()
        auth.write_email_create_account("testing")
        auth.click_create_account()
        auth.sleep(3)
        auth.read_error_create_account()
       

