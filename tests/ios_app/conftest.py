import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from dotenv import load_dotenv
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "ios",
        "platformVersion": "13",
        "deviceName": "iPhone XS",

        # Set URL of the application under test
        "app": "bs://bfc9cb387aa35409d0506f4fa345e2ab8fd20135",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Mobile Tests Lesson 21",
            "buildName": "browserstack-build-2",
            "sessionName": "BStack ios_test",

            # Set your access credentials
            "userName": f'{login}',
            "accessKey": f'{password}'
        }
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()