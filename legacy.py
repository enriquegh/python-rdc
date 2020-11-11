import os
import logging

logging.basicConfig(level=logging.DEBUG)
from appium import webdriver
caps = {
    'deviceName': 'iPhone_SE_POC101',
    'platformName': 'iOS',
    'name': "Legacy Test",
    'testobject_api_key': os.environ['SAUCE_RDC_API_KEY']
}


sauce_url = 'https://us1.appium.testobject.com/wd/hub'


driver = webdriver.Remote(command_executor=sauce_url, desired_capabilities=caps)
driver.page_source
driver.quit()
