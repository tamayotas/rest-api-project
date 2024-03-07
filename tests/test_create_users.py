import allure
import requests
import json
import jsonschema as jsonschema
from allure_commons.types import Severity

from rest_api_project.utils.api_helper import api_request
from rest_api_project.utils.resource import load_schema
from rest_api_project.utils.allure_attach import response_logging, response_attaching


@allure.title("Создание пользователя")
@allure.severity(Severity.BLOCKER)
@allure.tag("api")
@allure.story("Создание пользователя")
def test_create_user(get_base_api_url):
    schema = load_schema("create_user.json")
    body = json.loads('{"name": "morpheus1", "job": "leader_new"}')

    response = api_request(get_base_api_url, endpoint="/users", method="POST", data=body)

    assert response.status_code == 201
    assert response.json()["name"] == "morpheus1"
    assert response.json()["job"] == "leader_new"
    jsonschema.validate(instance=response.json(), schema=schema)


@allure.title("Создание пользователя с одним параметром")
@allure.severity(Severity.BLOCKER)
@allure.tag("api")
@allure.story("Создание пользователя")
def test_create_user_with_name_only(get_base_api_url):
    schema = load_schema("create_with_name_only.json")
    body = json.loads('{"name": "morpheus1"}')

    response = api_request(get_base_api_url, endpoint="/users", method="POST", data=body)

    assert response.status_code == 201
    assert response.json()["name"] == "morpheus1"
    jsonschema.validate(instance=response.json(), schema=schema)
