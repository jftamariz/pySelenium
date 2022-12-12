import pytest


class TestBase():


    @staticmethod
    def skip_test(message=None):
        from colorama import Fore, Back, Style, init
        init()
        print(Fore.YELLOW," [Skip] - Test Case:  {0}".format(message))
        pytest.skip(" [Skip] - Test Case:  {0}".format(message))
        print(Style.RESET_ALL)

