from test_base import *
from pages.home import Home
from pages.cart import Cart

class TestLogin(TestBase):

    @pytest.mark.smoke
    @allure.title("Login successful")
    def test_login_successful(self, driver, user):
        if user is None :
            TestBase.skip_test(" login_successful - This test required a regustered user's email and password.  \n  Please provide user email (--email) and password  (--pwd) as command line arguments and try again")
        
        sign_in = Home(driver).sign_in()
        sign_in.write_email(user["email"])
        sign_in.write_password(user["password"])
        account = sign_in.sign_in()
        
        assert account.read_account_welcome_msg() == "Welcome to your account. Here you can manage all of your personal information and orders."," Expected a successful Sign in"
        sign_in.logout()
        
    @allure.title("Login with invalid email")
    def test_login_invalid_email(self, driver):

        sign_in = Home(driver).sign_in()
        sign_in.write_email("invalid-emailgmail.com")
        sign_in.click_sign_in()
        error_str = sign_in.read_error_alert()
        assert error_str == "Invalid email address."," Expected: 'Invalid email address.' invalid email error.   Actual: {0}".format(error_str)

    @allure.title("Login with missing password")
    def test_login_missing_password(self, driver):
        sign_in = Home(driver).sign_in()
        sign_in.write_email("some-valid-email@gmail.com")
        sign_in.click_sign_in()
        error_str = sign_in.read_error_alert()
        assert error_str == "Password is required."," Expected: 'Password is required.' missing password error.   Actual: {0}".format(error_str)

    @allure.title("Login with wrong password")
    def test_login_wrong_password(self, driver, user):
        if user is None:
            TestBase.skip_test(" login_wrong_password -  User email and Password not provided as command line argument.  Please provide user email and password and try again")
       
        sign_in = Home(driver).sign_in()
        sign_in.write_email(user["email"])
        sign_in.write_password("wrong password")
        sign_in.click_sign_in()
        error_str = sign_in.read_error_alert()
        assert error_str == "Authentication failed."," Expected: 'authentication failed.' wrong password error.   Actual: {0}".format(error_str)
    