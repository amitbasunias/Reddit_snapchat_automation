
import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "Appium",
	"appium:deviceName": "86b6b7a1",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 360000,
	"appium:connectHardwareKeyboard": True
})


def addsnap(user):
	try:
		driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

		el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chrome")
		el1.click()


		el2 = driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/url_bar")
		el2.click()
		el2.send_keys(f"snapchat.com/add/{user}")
		el3 = driver.find_element(by=AppiumBy.XPATH, value=f"//android.widget.TextView[@resource-id=\"com.android.chrome:id/line_2\" and @text=\"snapchat.com/add/{user}\"]")
		el3.click()
		time.sleep(5)

		el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open in Snapchat")
		el8.click()
		time.sleep(3)
		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(557, 1443)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(519, 1435)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(3)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(878, 136)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(4)


		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(500, 1392)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.move_to_location(544, 693)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(804, 674)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(3)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(807, 878)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(4)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(818, 1076)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(3)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(824, 1258)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(5)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(821, 1443)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(5)


		'''actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(454, 353)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(796, 1949)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(544, 1451)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(549, 1424)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(840, 160)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(840, 1658)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(832, 1655)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)'''

		actions = ActionChains(driver)
		actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
		actions.w3c_actions.pointer_action.move_to_location(535, 2278)
		actions.w3c_actions.pointer_action.pointer_down()
		actions.w3c_actions.pointer_action.pause(0.1)
		actions.w3c_actions.pointer_action.release()
		actions.perform()
		time.sleep(2)

	except Exception as e:
		print(f"An error occurred while processing user '{user}': {e}")
	finally:
		# Make sure to quit the driver even if an exception occurs
		if 'driver' in locals():
			driver.quit()




