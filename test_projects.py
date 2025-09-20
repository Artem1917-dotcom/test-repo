import pytest
from projects_client import ProjectsClient

class TestProjectsAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = ProjectsClient()
        self.valid_project_data = {
            "title": "Test Project",
            "description": "Test project description",
            "icon": "🚀"
        }
        self.update_data = {
            "title": "Updated Project Title",
            "description": "Updated description",
            "icon": "⭐"
        }
    
    def test_create_project_positive(self):
        response = self.client.create_project(self.valid_project_data)
        assert response.status_code == 201
        project_id = response.json()["id"]
        self.client.delete_project(project_id)
    
    def test_create_project_minimal_positive(self):
        minimal_data = {"title": "Minimal Project"}
        response = self.client.create_project(minimal_data)
        assert response.status_code == 201
        project_id = response.json()["id"]
        self.client.delete_project(project_id)
    
    def test_get_project_positive(self, created_project_id):
        response = self.client.get_project(created_project_id)
        assert response.status_code == 200
        assert response.json()["id"] == created_project_id
    
    def test_update_project_positive(self, created_project_id):
        response = self.client.update_project(created_project_id, self.update_data)
        assert response.status_code == 200
    
    def test_create_project_negative_no_title(self):
        invalid_data = {"description": "Project without title"}
        response = self.client.create_project(invalid_data)
        assert response.status_code == 400
    
    def test_get_project_negative_not_found(self):
        response = self.client.get_project("non-existent-project-id-12345")
        assert response.status_code == 404
    
    def test_update_project_negative_not_found(self):
        response = self.client.update_project("non-existent-project-id-12345", self.update_data)
        assert response.status_code == 404