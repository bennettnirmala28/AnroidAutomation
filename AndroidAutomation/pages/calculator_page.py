from appium.webdriver.common.appiumby import AppiumBy
from AndroidAutomation.base.base_page import BasePage

class CalculatorPage(BasePage):
    # Locators for the calculator buttons
    button_2 = (AppiumBy.ID,"com.sec.android.app.popupcalculator:id/bt_02")
    button_3 = (AppiumBy.ID,"com.sec.android.app.popupcalculator:id/bt_03")
    button_plus = (AppiumBy.ID,"com.sec.android.app.popupcalculator:id/bt_add")
    button_equal = (AppiumBy.ID,"com.sec.android.app.popupcalculator:id/bt_equal")
    result_field = (AppiumBy.ID,"com.sec.android.app.popupcalculator:id/txtCalc_RealTimeResult")

    def press_2(self):
        self.driver.find_element(*self.button_2).click()

    def press_3(self):
        self.driver.find_element(*self.button_3).click()

    def press_plus(self):
        self.driver.find_element(*self.button_plus).click()

    def press_equal(self):
        self.driver.find_element(*self.button_equal).click()

    def get_result(self):
        return self.driver.find_element(*self.result_field).text
