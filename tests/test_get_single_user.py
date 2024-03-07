import allure
import jsonschema
from allure_commons.types import Severity

from rest_api_project.utils.api_helper import api_request
from rest_api_project.utils.resource import load_schema


@allure.title("Получение данных пользователя по id")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Получение данных пользователя")
def test_get_single_user_by_id(get_base_api_url):
    user_id = 2

    schema = load_schema("single_user.json")

    response = api_request(get_base_api_url, endpoint=f"/users/{user_id}", method="GET")
    resp_body = response.json()

    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id
    jsonschema.validate(resp_body, schema)


@allure.title("Получение данных несуществующего пользователя по id")
@allure.severity(Severity.MINOR)
@allure.tag("api")
@allure.story("Получение данных пользователя")
def test_get_single_user_by_nonexistent_id(get_base_api_url):

    response = api_request(get_base_api_url, endpoint="/users/unknown_id", method="GET")

    assert response.status_code == 404
    assert response.text == "{}"

