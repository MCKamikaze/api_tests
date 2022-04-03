import requests
from data.api_endpoints import Endpoints
import names
import json
import pytest


class LimitReachedException(Exception):
    """Raised when too many requests were made to the API (status code 429)"""

    pass


class NoNationalityException(Exception):
    """Raised when no nationailty is found for a given name"""

    pass


def generate_name() -> str:
    return names.get_first_name()


def generate_age(name: str) -> int:
    age_url = Endpoints.GetAge.value + f"?name={name}"
    result = get_response_as_dict(age_url)
    return result.get("age")


def generate_gender(name: str) -> str:
    gender_url = Endpoints.GetGender.value + f"?name={name}"
    result = get_response_as_dict(gender_url, "gender")
    return result.get("gender")


def generate_nationality(name: str) -> list:
    nationality_url = Endpoints.GetNationality.value + f"?name={name}"
    result = get_response_as_dict(nationality_url)

    try:
        if not result.get("country"):
            raise NoNationalityException(f"No nationality available for name: {name}")

        max_prob_country = max(result.get("country"), key=lambda x: x["probability"])
    except NoNationalityException as e:
        pytest.fail(str(e))
    return max_prob_country.get("country_id")


def get_response_as_dict(url):
    try:
        response = requests.get(url)
        if response.status_code == 429:
            raise LimitReachedException(f"Request limit reached for url: {url}")
        result = json.loads(response.text)
    except LimitReachedException as e:
        pytest.fail(str(e))
    return result
