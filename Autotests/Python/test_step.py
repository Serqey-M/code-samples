from datetime import datetime
import logging
import time
import pytest
import yaml
from testpage import OperationsHelper

with open('D:\code-samples\Autotests\\testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

    
def test_step1(browser):
    logging.info('Test1 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'test1 failed'


def test_step2(browser):
    logging.info('Test2 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_login_text() == f'Hello, {testdata["username"]}', 'test2 failed'


def test_step3(browser):
    logging.info('Test3 Starting')
    testpage = OperationsHelper(browser)
    time.sleep(testdata['sleep_time'])
    testpage.click_create_post_button()
    title = str(datetime.now())
    testpage.enter_post_titl(title)
    testpage.enter_post_description(testdata['new_post_description'])
    testpage.enter_post_content(testdata['new_post_content'])
    testpage.click_save_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_added_post_titl() == title, 'test3 failed'


def test_step4(browser):
    logging.info('Test4 Starting')
    testpage = OperationsHelper(browser)
    testpage.click_сontact()
    testpage.enter_сontact_name(testdata['username'])
    testpage.enter_сontact_email(testdata['email'])
    testpage.enter_сontact_content(testdata['contact_content'])
    testpage.click_сontact_btn()
    time.sleep(testdata['sleep_time'])
    assert testpage.alert() == 'Form successfully submitted', 'test4 failed'
    

if __name__ == '__main__':
    pytest.main(['-v'])