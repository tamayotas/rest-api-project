import json
import allure
import pytest
from rest_api_project.utils.api_helper import api_request

BASE_API_URL = "https://reqres.in/api"


@pytest.fixture
def get_base_api_url():
    return BASE_API_URL


@allure.title("Создание тестового пользователя")
@pytest.fixture(scope="function")
def create_user(get_base_api_url):

    body = json.loads('{"name": "morpheus1", "job": "leader_new"}')

    response = api_request(get_base_api_url, endpoint="/users", method="POST", data=body)
    return response.json()["id"]
