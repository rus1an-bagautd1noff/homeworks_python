import pytest
from page_objects.projects import ProjectsAPI


@pytest.mark.usefixtures("base_url", "auth_header")
class TestProjects:
    @pytest.fixture(autouse=True)
    def setup(self, base_url, auth_header):
        self.projects_api = ProjectsAPI(base_url, auth_header)

    def test_create_project_success(self):
        payload = {"name": "Test Project", "description": "Automated test project"}
        response = self.projects_api.create_project(payload)
        assert response.status_code == 201
        assert "id" in response.json()

    def test_create_project_invalid_data(self):
        payload = {"name": ""}  # Пустое имя
        response = self.projects_api.create_project(payload)
        assert response.status_code == 400

    def test_update_project_success(self, project_id):
        payload = {"name": "Updated Test Project"}
        response = self.projects_api.update_project(project_id, payload)
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Test Project"

    def test_update_project_invalid_id(self):
        payload = {"name": "Updated Test Project"}
        response = self.projects_api.update_project("invalid_id", payload)
        assert response.status_code == 404

    def test_get_project_success(self, project_id):
        response = self.projects_api.get_project(project_id)
        assert response.status_code
