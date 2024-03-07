import allure
import json
import jsonschema
from allure_commons.types import Severity

from rest_api_project.utils.api_helper import api_request
from rest_api_project.utils.resource import load_schema


@allure.title("Создание пользователя")
@allure.severity(Severity.BLOCKER)
@allure.tag("api")
@allure.story("Создание пользователя")
def test_create_user(get_base_api_url):
    schema = load_schema("create_user.json")
    body = json.loads('{"name": "morpheus1", "job": "leader_new"}')

    response = api_request(get_base_api_url, endpoint="/users", method="POST", data=body)
    resp_body = response.json()

    assert response.status_code == 201
    assert response.json()["name"] == "morpheus1"
    assert response.json()["job"] == "leader_new"
    jsonschema.validate(resp_body, schema)


@allure.title("Создание пользователя с одним параметром")
@allure.severity(Severity.BLOCKER)
@allure.tag("api")
@allure.story("Создание пользователя")
def test_create_user_with_name_only(get_base_api_url):
    schema = load_schema("create_with_name_only.json")
    body = json.loads('{"name": "morpheus1"}')

    response = api_request(get_base_api_url, endpoint="/users", method="POST", data=body)
    resp_body = response.json()

    assert response.status_code == 201
    assert response.json()["name"] == "morpheus1"
    jsonschema.validate(resp_body, schema)
