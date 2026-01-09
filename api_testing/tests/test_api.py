from pathlib import Path
from jsonschema import validate, exceptions
import requests
import pytest
import json


@pytest.fixture
def base_url(scope="session"):
    url="https://fake-json-api.mock.beeceptor.com"
    return url

@pytest.fixture
def companies_schema():
    return load_json_schema("companies_schema.json")

def load_json_schema(filename):
    schema_path = Path(__file__).parent / "schemas" / filename
    with open(schema_path, 'r') as file:
        return json.load(file)


@pytest.mark.positive
def test_get_companies(base_url, companies_schema):
    url = f"{base_url}/companies"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    try:
        validate(instance=response.json(), schema=companies_schema)
    except exceptions.ValidationError as e:
        pytest.fail(f"JSON schema | El contrato no coincide: {e.message}")

@pytest.mark.negative
def test_get_companies_invalid_endpoint(base_url):
    url = f"{base_url}/invalid_companies"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    jsonData = response.json()

    assert len(jsonData["paths"]) != 0, "Paths están vacíos"




