from appium import webdriver
from appium.options.android import UiAutomator2Options


class BasePage:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "appium:deviceName": "Galaxy A7 (2016)",
            "appium:udid": "33002ba21785c219",
            "appium:platformVersion": "7",
            "appium:appPackage": "com.sec.android.app.popupcalculator",
            "appium:appActivity": "com.sec.android.app.popupcalculator.Calculator",
            "appium:automationName": "UiAutomator2",
            "appium:ignoreHiddenApiPolicyError": True,
            "appium:noReset": True
        }

        options = UiAutomator2Options().load_capabilities(desired_cap)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

    def quit(self):
        self.driver.quit()