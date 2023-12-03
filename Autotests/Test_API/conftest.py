import requests
import pytest
import yaml

with open ('D:\Новая папка\Autotests\Test_API\config.yaml', encoding = 'utf-8') as f:
    data = yaml.safe_load(f)
    address, username, password = data['address'], data['username'], data['password']

S = requests.Session()

@pytest.fixture
def user_login():
    res1 = S.post(url = address, data = {'username': username, 'password': password})
    return res1.json()['token']




