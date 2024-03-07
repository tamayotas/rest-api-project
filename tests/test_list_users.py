import allure
import pytest
import jsonschema
from allure_commons.types import Severity

from rest_api_project.utils.api_helper import api_request
from rest_api_project.utils.resource import load_schema


@allure.title("Получение списка пользователей")
@allure.severity(Severity.BLOCKER)
@allure.tag("api")
@allure.story("Получение списка пользователей")
@pytest.mark.parametrize("id_", [1, 2])
def test_get_list_users_with_page_id(get_base_api_url, id_):
    params = {"page": id_}
    schema = load_schema("list_users.json")

    response = api_request(get_base_api_url, endpoint="/users", method="GET", params=params)
    resp_body = response.json()

    assert response.status_code == 200
    assert response.json()["page"] == id_
    jsonschema.validate(resp_body, schema)


@allure.title("Получение списка пользователей с неверным параметром")
@allure.severity(Severity.TRIVIAL)
@allure.tag("api")
@allure.story("Получение списка пользователей")
def test_get_list_users_with_wrong_parameter(get_base_api_url):
    page_id = 2
    schema = load_schema("list_users.json")
    params = {"pe": page_id}

    response = api_request(get_base_api_url, endpoint="/users", method="GET", params=params)
    resp_body = response.json()

    assert response.status_code == 200
    assert response.json()["page"] == 1
    jsonschema.validate(resp_body, schema)


@allure.title("Получение списка пользователей с несуществующим значением параметра")
@allure.severity(Severity.NORMAL)
@allure.tag("api")
@allure.story("Получение списка пользователей")
def test_get_list_users_with_nonexistent_parameter(get_base_api_url):
    page_id = 9999999
    params = {"page": page_id}

    schema = load_schema("list_users_with_nonexistent_parameter.json")

    response = api_request(get_base_api_url, endpoint="/users", method="GET", params=params)
    resp_body = response.json()

    assert response.status_code == 200
    assert response.json()["page"] == page_id
    jsonschema.validate(resp_body, schema)
