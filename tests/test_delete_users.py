import allure
from allure_commons.types import Severity
from rest_api_project.utils.api_helper import api_request


@allure.title("Удаление пользователя")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Удаление пользователя")
def test_deletion_of_user(get_base_api_url, create_user):

    response = api_request(get_base_api_url, endpoint=f"/users/{create_user}", method="DELETE")

    assert response.status_code == 204
    assert response.text == ""


@allure.title("Удаление пользователя с несуществующим id")
@allure.severity(Severity.CRITICAL)
@allure.tag("api")
@allure.story("Удаление пользователя")
def test_deletion_of_user_with_unknown_id(get_base_api_url):

    response = api_request(get_base_api_url, endpoint="/users/unknown_id", method="DELETE")

    assert response.status_code == 204
    assert response.text == ""
