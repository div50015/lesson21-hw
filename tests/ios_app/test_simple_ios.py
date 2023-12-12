from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure


def test_add_text_at_ui_elements():
    with allure.step('Type email'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com' + '\n')

    with allure.step('Verify added row'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('hello@browserstack.com'))