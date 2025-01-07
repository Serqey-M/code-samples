import pytest
import requests
import yaml


with open ('D:\Новая папка\Autotests\Test_API\config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address, notMe_post_title = data['address_post'], data['notMe_post_title']
    new_post_title, new_post_description, new_post_content = data['new_post_title'],data['new_post_description'], data['new_post_content']
S = requests.Session()


def test_notMe_post(user_login):
    res = S.get(url = address, headers = {'X-Auth-Token': user_login}, params = {"owner": 'notMe'}).json()['data']
    r = [i['title'] for i in res]
    assert notMe_post_title in r, 'Test_notMe_post Failed'


def test_new_post(user_login):
    S.post(url = address, headers = {'X-Auth-Token': user_login}, data = {'title': new_post_title, 'description': new_post_description, 'content': new_post_content})
    res = S.get(url = address, headers = {'X-Auth-Token': user_login}).json()['data']
    r = [i['title'] for i in res] 
    assert new_post_title in r, 'Test_new_post Failed'

if __name__ == '__main__':
    pytest.main(['-v'])