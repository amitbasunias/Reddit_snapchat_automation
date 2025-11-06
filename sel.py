from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import PointerInput
from selenium.webdriver.common import actions as interaction
import time

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Pixel_XL',  # Replace with your device name
    'automationName': 'UiAutomator2',
}
# Initialize the Appium WebDriver directly with desired capabilities
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

# Add your automation code here (e.g., login, interact with elements)
# ... (your previous code)

'''actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(675, 1953)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(672, 850)
actions.w3c_actions.pointer_action.release()
actions.perform()'''

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Snapchat")
el1.click()
time.sleep(5)
el2 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.snapchat.android:id/login_text")
el3.click()


# Wait for some time (replace this with your actual interactions)
time.sleep(5)

# Quit the driver
driver.quit()
