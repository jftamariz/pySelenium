import os
import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import subprocess
import socket
import time 
from tests.test_base import TestBase
from sys import platform

class DriverFactory:

    @staticmethod
    def create_web_driver(**kwargs):
        '''
            Returns a WebDriver instance based on configurationa and capabilities provided under kwargs
            kwargs -  A {} with the following parameters:
                browser:  
        ''' 
        if kwargs["browser"] == "chrome":

            if kwargs["localdriver"]:
                chromedriver_path = DriverFactory.get_filedriver_exe("chrome")
             
                if os.path.exists(chromedriver_path):
                    os.environ["webdriver.chrome.driver"] = chromedriver_path
                else:
                    raise Exception(" [E] - Chromedriver file is not found: "+chromedriver_path)
                
                return webdriver.Chrome(chromedriver_path)

            # Wait for Seleinum docker container URL and Port connection to be open
            if not DriverFactory.isOpen(kwargs["host"], int(kwargs["port"])):
                TestBase.skip_test(" Running in DOCKER:CHROME mode -  Attempting to reach Selenium standalone continaer at http://{0}:{1}/ FAILED.\n  Provide an open --host and/or --port values and try again.".format(kwargs["host"], kwargs["port"] ))
                return None

            return webdriver.Remote("http://"+kwargs["host"]+":"+kwargs["port"]+"/wd/hub", DesiredCapabilities.CHROME)
   

        elif kwargs["browser"] == "firefox":
            if kwargs["localdriver"]:
                firefoxdriver_path = DriverFactory.get_filedriver_exe("firefox")

                if os.path.exists(firefoxdriver_path):
                    os.environ["webdriver.gecko.driver"] = firefoxdriver_path
                else:
                    raise Exception(" [E] - Firefoxdriver file is not found: "+firefoxdriver_path)

                return webdriver.Firefox(executable_path=firefoxdriver_path)

            # Wait for Seleinum docker container URL and Port connection to be open
            if not DriverFactory.isOpen(kwargs["host"], int(kwargs["port"])):
                TestBase.skip_test(" Running in DOCKER:FIREFOX mode -  Attempting to reach Selenium standalone continaer at http://{0}:{1}/ FAILED.\n  Provide an open --host and/or --port values and try again.".format(kwargs["host"], kwargs["port"] ))
                return None

            return webdriver.Remote("http://"+kwargs["host"]+":"+kwargs["port"]+"/wd/hub", DesiredCapabilities.FIREFOX)
   


        elif kwargs["browser"] == "ie":
            if not kwargs["localdriver"]:
                TestBase.skip_test(" Running in DOCKER:IE mode is not supported.  IE is only supported running Local webdriver (--localdriver)")
                return None

            iedriver_path_file = DriverFactory.get_filedriver_exe("ie")

            if os.path.exists(iedriver_path_file):
                os.environ["webdriver.ie.driver"] = iedriver_path_file
            else:
                raise Exception(" [E] - IE Driver Server file is not found: "+iedriver_path_file)

            return webdriver.Ie(executable_path=iedriver_path_file)

        elif kwargs["browser"] == "safari":
            if not kwargs["localdriver"]:
                TestBase.skip_test(" Running in DOCKER:SAFARI mode is not supported.  SAFARI is only supported running Local webdriver (--localdriver)")
                return None

            if not 'darwin' in platform.lower():
                TestBase.skip_test(" - Attempting to run test on Safari running on Windows or Linux?  Only supports Safari on Mac")
     
            return webdriver.Safari()

        else:
            TestBase.skip_test(" -  Browser type {0} not recognize.  Provide from supported browsers (--browser) Chrome, Safari, Firefox and IE".format(kwargs["browser"]))
            return None


    @staticmethod
    def get_filedriver_exe(browser):
        ''' 
            Returns the name of the executable driver file based on browser type.  
            Note:
            1.  Make sure driver file is set to be able to execute (i.e. chmod +x geckodriver)
            2.  Chromdedriver download - https://chromedriver.chromium.org/downloads
            3.  Filrefox driver download - https://github.com/mozilla/geckodriver/releases
        '''
        if browser == "firefox":
            if 'darwin' in platform.lower():
                return os.path.join(os.getcwd(),'drivers','geckodriver')
            elif 'win32' in platform.lower():
                return os.path.join(os.getcwd(),'drivers','geckodriver.exe')
            elif 'linux' in platform.lower():
                return os.path.join(os.getcwd(),'drivers','geckodriver_linux')
        elif browser == "chrome":
            if 'darwin' in platform.lower():
                return os.path.join(os.getcwd(),'drivers','chromedriver_87')
            elif 'win32' in platform.lower():
                return os.path.join(os.getcwd(),'drivers','chromedriver_87.exe')
            elif 'linux' in platform.lower():
                return os.path.join(os.getcwd(),'drivers','chromedriver_linux')
        elif browser == "ie":
            if 'darwin' in platform.lower():
                TestBase.skip_test(" - Attempting to run test(s) using IE on Mac.  Only supports IE on Windows")
                return None
            elif 'win32' in platform.lower():
                return os.path.join(os.getcwd(),'drivers','iedriverserver.exe')
            elif 'linux' in platform.lower():
                TestBase.skip_test(" - Attempting to run test(s) using IE on Linux.  Only supports IE on Windows")
                return None    
        

    @staticmethod
    def isOpen(ip, port, wait_time=5):
        '''
            Return True if Selenium Node or Standalone cotainer is up and running.  
            Wait for 'wait_time' seconds before it returns False if url and port is closed.
        '''
        result = False
        for i in range(wait_time):
            try:
                t_start = time.time()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((ip, port))
                result = True
                break
            except:
                result = False
            finally:
                t_end = time.time()
                time.sleep(1)
                s.close()
     
        if result:
            from colorama import Fore, Style, init
            init()
            print(Fore.CYAN,  Style.BRIGHT, " http://{0}:{1} is open and ready - {2:.1f}s".format(ip, port, (t_end-t_start)))
            print(Style.RESET_ALL, Fore.RESET)
        
        return result

        
