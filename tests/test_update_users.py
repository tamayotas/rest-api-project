import allure
import json
from allure_commons.types import Severity
import jsonschema as jsonschema

from rest_api_project.utils.api_helper import api_request
from rest_api_project.utils.resource import load_schema


@allure.title("Обновление данных пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Обновление данных пользователя")
def test_update_user(get_base_api_url, create_user):

    schema = load_schema("update_user.json")
    body = json.loads('{"name": "kotofeus", "job": "watcher"}')

    response = api_request(get_base_api_url, endpoint=f"/users/{create_user}", method="PUT", data=body)

    assert response.status_code == 200
    assert response.json()["name"] == "kotofeus"
    assert response.json()["job"] == "watcher"
    jsonschema.validate(instance=response.json(), schema=schema)


@allure.title("Обновление данных не существующего пользователя")
@allure.severity(Severity.MINOR)
@allure.tag("api")
@allure.story("Обновление данных пользователя")
def test_update_non_existent_user(get_base_api_url):

    schema = load_schema("update_user.json")
    body = json.loads('{"name": "kotofeus", "job": "watcher"}')

    response = api_request(get_base_api_url, endpoint="/users/some_id", method="PUT", data=body)

    assert response.status_code == 200
    assert response.json()["name"] == "kotofeus"
    assert response.json()["job"] == "watcher"
    jsonschema.validate(instance=response.json(), schema=schema)
