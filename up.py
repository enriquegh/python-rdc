import os
import logging

logging.basicConfig(level=logging.DEBUG)
from appium import webdriver
caps = {
    'username': os.environ['SAUCE_USERNAME'],
    'accessKey': os.environ['SAUCE_ACCESS_KEY'],
    'deviceName': 'iPhone_SE_POC101',
    'platformName': 'iOS',
    'name': "UP Test",
    'app': 'storage:filename=iOS.RealDevice.SauceLabs.Mobile.Sample.app.2.6.0.ipa'
}


sauce_url = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'


driver = webdriver.Remote(command_executor=sauce_url, desired_capabilities=caps)
driver.page_source
driver.quit()
