import pytest
import requests
from Lesson8.config import BASE_URL, HEADERS


@pytest.fixture
def api_headers():
    return HEADERS.copy()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def test_project_data():
    return {
        "title": "Test Project API",
        "description": "Test project created by API",
        "icon": "📋"
    }


@pytest.fixture
def created_project_id(api_headers, base_url, test_project_data):
    """Фикстура создает проект и возвращает его ID для тестов"""
    response = requests.post(
        f"{base_url}/projects",
        headers=api_headers,
        json=test_project_data
    )

    if response.status_code == 201:
        project_id = response.json()["id"]
        yield project_id

        # Cleanup - удаляем проект после теста
        requests.delete(
            f"{base_url}/projects/{project_id}",
            headers=api_headers
        )
    else:
        pytest.skip(f"Failed to create test project: {response.status_code}")
