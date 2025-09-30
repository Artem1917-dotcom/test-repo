import requests
from Lesson8.config import BASE_URL, HEADERS

class ProjectsClient:
    """Client для работы с API проектов Yougile"""
    
    def __init__(self, base_url=BASE_URL, headers=HEADERS):
        self.base_url = base_url
        self.headers = headers
    
    def create_project(self, project_data):
        """
        POST /api-v2/projects - Создание проекта
        Обязательные поля: title
        """
        response = requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=project_data
        )
        return response
    
    def get_project(self, project_id):
        """
        GET /api-v2/projects/{id} - Получение проекта по ID
        """
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response
    
    def update_project(self, project_id, update_data):
        """
        PUT /api-v2/projects/{id} - Обновление проекта
        """
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=update_data
        )
        return response
    
    def delete_project(self, project_id):
        """
        DELETE /api-v2/projects/{id} - Удаление проекта
        """
        response = requests.delete(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response