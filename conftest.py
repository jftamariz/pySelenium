import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'tests'))


def pytest_addoption(parser):
	parser.addoption('--env', action='store', help=' - environment', default='qa')
	parser.addoption('--browser', action='store', help=' - browser type', default='chrome')
	parser.addoption('--email', action='store', help=' - Existing user account email', default='')
	parser.addoption('--pwd', action='store', help=' - Existing user accoutn password', default='')
	parser.addoption('--host', action='store', help=' - Host IP', default='127.0.0.1')
	parser.addoption('--port', action='store', help=' - Port', default='4444')
	parser.addoption('--localdriver', action='store_true', help=' - Run selenium locally', default=False)


@pytest.fixture(scope="session")
def test_args(request):
	return {"env":request.config.getoption("--env"),
			"browser":request.config.getoption("--browser"),
			"email":request.config.getoption("--email"),
			"password":request.config.getoption("--pwd"),
			"host":request.config.getoption("--host"),
			"port":request.config.getoption("--port"),
			"localdriver":request.config.getoption("--localdriver")}

def enum(**named_values):
	return type('Enum', (), named_values)


@pytest.fixture(scope="session")
def ENV():
	return enum(PROD='production', STG='staging', QA='qa', DEV='dev')