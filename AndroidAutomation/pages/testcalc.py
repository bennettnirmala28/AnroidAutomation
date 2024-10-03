from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

desired_cap = {
    "platformName": "Android",
    "appium:deviceName":"Galaxy A7 (2016)",
    "appium:udid": "33002ba21785c219",
    "appium:platformVersion":"7",
    "appium:appPackage":"com.sec.android.app.popupcalculator",
    "appium:appActivity":"com.sec.android.app.popupcalculator.Calculator",
    "appium:automationName":"UiAutomator2",
    "appium:ignoreHiddenApiPolicyError":True,
    "appium:noReset":True
}

options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote('http://localhost:4723/wd/hub',options=options)

# Add a wait to allow the app to load properly
driver.implicitly_wait(40)

# Optionally, perform operations (e.g., click buttons)
# Example: Click "2", "+", "3", "=" on the calculator

driver.find_element(By.ID,"com.sec.android.app.popupcalculator:id/bt_02").click()
driver.find_element(By.ID,"com.sec.android.app.popupcalculator:id/bt_add").click()
driver.find_element(By.ID,"com.sec.android.app.popupcalculator:id/bt_03").click()
driver.find_element(By.ID,"com.sec.android.app.popupcalculator:id/bt_equal").click()

# Close the app after performing operations
driver.quit()


