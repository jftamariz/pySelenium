from test_base import *
from pages.home import Home


class TestAccountCreate(TestBase):



    @allure.title("Login - Create new account")
    def test_login_create_account(self, driver):

        auth = Home(driver).sign_in()
        auth.write_email_create_account("testing")
        auth.click_create_account()
        auth.sleep(3)
        auth.read_error_create_account()
       
