import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml



class TestSearchLocators:
    ids = dict()
    with open('D:\code-samples\Autotests\locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['XPATH'].keys():
        ids[locator] = (By.XPATH, locators['XPATH'][locator])
    for locator in locators['CSS_SELECTOR'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['CSS_SELECTOR'][locator])


class OperationsHelper(BasePage):

    def enter_terxt_into_field(self, locator, word, description = None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exeption while operation with {locator}')
            return False
        return True
    
    def click_button(self, locator, description = None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exepption with click')
            return False
        logging.debug(f'Click {element_name} button')
        return True

    def get_text_from_element(self, locator, description = None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text


    # Ввод текста
    def enter_login(self, word):
        self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description = 'login form')

    def enter_pass(self, word):
        self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description = 'pass form')
  
    def enter_post_titl(self, word):
        self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_FORM_POST_TITLE'], word, description = 'post title form')

    def enter_post_description(self, word):
        self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_FORM_POST_DESCRIPTION'], word, description = 'post description form')
    
    def enter_post_content(self, word):
        self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_FORM_POST_CONTENT'], word, description = 'post content form')

    def enter_сontact_name(self, word):
        self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_NAME'], word, description = 'name content form')

    def enter_сontact_email(self, word):
        self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_EMAIL'], word, description = 'email content form')

    def enter_сontact_content(self, word):
        self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_CONTENT'], word, description = 'contact content form')

    # клик 
    
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_save_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_SAVE_POST_BTN'], description='save post')

    def click_сontact(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT'], description='contact')

    def click_сontact_btn(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description='contact btn')

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CREATE_POST_BTN'], description='create post')

    # получить 
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'])
    
    def get_added_post_titl(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_POST_NAME'])
    
    def get_login_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_USER_PROFILE_LINK'])


    def alert(self):
        alert = self.get_alert_text()
        logging.info(alert)
        return alert
    

