# pySelenium

It’s a Selenium and Pytest based automation framework.  

REDFIN  (https://www.redfin.com) website is used to demonstrate its UI E2E test capabilities.

### Run Tests on Docker Containers 
PySelenium tests can be run using 2 Docker containers, one container with Chrome or Firefox web browser and 
the other containers running the Selenium-Pytest automation scripts.

1.  Install the required applications

  * Docker 19+
  * Allure 2.13+
  
2.  Run Smoke tests with Chrome browser in two Docker containers

```
  $ ./runPySeleniumTests.sh —smoke —docker   
```

3.  Run Regression tests with Firefox browser
```
  $ ./runPySeleniumTests.sh  —docker —browser firefox
```

4.  View test results with Allure reports.  Test results should be saved under directory /test_results/allure_results 
```
  $ allure serve test_results/allure_results 
```

5.  Don’t forget to bring down the containers after tests are finished
```
  $ docker-compose down
```

### Run Tests Local - Mac
Running tests on a Mac will require more installation than running on them a Docker container

1.  Install the required applications

	*  Python 3.5+
	*  Pip
	*  VirtualEnv
	*  Allure 2.13+
	
	Optional
	*  [Chromedriver](https://chromedriver.chromium.org/downloads) - this repo includes a Chromedriver executable under  the /driver folder.  Feel free to download a different version.
	*  [Gheckodriver](https://github.com/mozilla/geckodriver/releases) - this repo includes a Firefox-Geckodriver executable under the /driver folder.  Feel free to download a different version.
	
  _Note:  These browser driver executables may need updated access mode_
  ```
    $ chmod +x chromedriver
  ```
  
2.  Create and activate a Virtual Environment
```
  $ virtuaenv pyselenium_env

	$ source pyselenium_env/bin/activate 
```

3.  Install Dependencies
```
  $ pip install -r requirements.txt
```

4.  Run Smoke tests with Chrome browser 
```
  $ ./runPySeleniumTests.sh 
```

5.  Run Regression with Firefox
```
  $ /runPySeleniumTests.sh  —browser Firefox
```

6.  Run Regression with test cases requiring login credentials from a registered user
```
  $ ./runPySeleniumTests.sh —email some_email@gmail.com  —password same_valid_password  
```

7.  View test results with Allure reports.  Test results should be saved under directory /test_results/allure_results 
```
  $ allure serve test_results/allure_results 
```

8.  Don’t forget to bring down the containers after tests are finished.
```
  $ docker-compose down
```

### Run Parallel Tests Local - Mac
Automation tests can also be run in parallel.  Please complete steps 1-3 from the above Run Test Local section.

1.  Run Regression tests in parallel with Chrome browser.  Example below will run tests in parallel with 3 Chrome browsers max
```
  $ pytest -s -n 3 tests/ --localdrive --alluredir=test_results/allure_results/
```
