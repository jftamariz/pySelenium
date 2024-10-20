from pages.home import Home
from util.util import get_now_datetime
import allure
import pytest


@pytest.mark.usefixtures("user_email_password_required")
class TestLogin:

    @pytest.mark.smoke
    @allure.title("Login successful")
    @allure.description(" Verify user is able to login successfuly  - Last run: "+ get_now_datetime())
    def test_login_successful(self, driver, user):
        sign_in = Home(driver).sign_in()
        sign_in.write_email(user["email"])
        sign_in.click_continue_with_email()
        sign_in.write_password(user["password"])
        sign_in.click_continue_with_email()
        
        assert sign_in.get_display_name()
        sign_in.logout()
        
    @allure.title("Login with invalid email")
    @allure.description(" Verify user is not able to login with invalid format email - Last run: "+ get_now_datetime())
    def test_login_invalid_email(self, driver):
        sign_in = Home(driver).sign_in()
        sign_in.write_email("invalid-emailgmail.com")
        sign_in.click_continue_with_email()
        error_str = sign_in.read_error_alert()
        assert error_str == "Please enter a valid email address",\
            "Expected: 'Please enter a valid email address' invalid email error.   Actual: {0}".format(error_str)

    @allure.title("Login with missing password")
    @allure.description(" Verify error is displayed when user logs in with missing password- Last run: "+ get_now_datetime())
    def test_login_missing_password(self, driver, user):
        sign_in = Home(driver).sign_in()
        sign_in.write_email(user["email"])
        sign_in.click_continue_with_email()
        sign_in.click_continue_with_email()
        error_str = sign_in.read_error_alert()
        assert error_str == "Required field",\
            " Expected: 'Required field' missing password error.   Actual: {0}".format(error_str)

    @allure.title("Login with wrong password")
    @allure.description(" Verify user is not able to login after entering wrong password - Last run: "+ get_now_datetime())
    def test_login_wrong_password(self, driver, user):
        sign_in = Home(driver).sign_in()
        sign_in.write_email(user["email"])
        sign_in.click_continue_with_email()
        sign_in.write_password("wrong password")
        sign_in.click_continue_with_email()
        error_str = sign_in.read_sign_in_error()
        assert error_str == "The email address and/or password you entered do not match any accounts on record. " + \
                            "Need help?\nReset your password.", \
                            " Expected: 'authentication failed.' wrong password error.   Actual: {0}".format(error_str)
