import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

with open('D:\code-samples\Autotests\\testdata.yaml') as f:
    testdata = yaml.safe_load(f)

    
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['address']

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
        except:
            logging.exeption('Find element exeption')
            element = None
        return element
    
        
    def get_element_property(self, locator, el_property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(el_property)
        else:
            logging.error(f'Property {property} not found in element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)   
        except:
            logging.exception('Exeption while open site')
            start_browsing = None
        return start_browsing
    
    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exeption with alert')
            return None
