import json
import jsonschema
from allure_commons.types import Severity

from rest_api_project.utils.api_helper import api_request
from rest_api_project.utils.resource import load_schema
import allure


@allure.title("Создание пользователя")
@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.story("Создание пользователя")
def test_creation_of_user(get_base_api_url):
    schema = load_schema("register_user.json")
    body = json.loads('{"email": "eve.holt@reqres.in", "password": "pistol"}')

    response = api_request(get_base_api_url, endpoint="/register", method="POST", data=body)
    resp_body = response.json()

    assert response.status_code == 200
    assert response.json()["id"] == 4

    jsonschema.validate(resp_body, schema)


@allure.title("Создание пользователя с незаполненным email")
@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.story("Создание пользователя")
def test_creation_of_user_with_miss_email(get_base_api_url):
    body = json.loads('{"password": "some_password"}')

    response = api_request(get_base_api_url, endpoint="/register", method="POST", data=body)

    assert response.status_code == 400
    assert response.text == '{"error":"Missing email or username"}'
