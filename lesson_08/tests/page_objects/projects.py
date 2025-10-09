import requests


class ProjectsAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.projects_endpoint = "/api-v2/projects"

    def create_project(self, payload):
        url = f"{self.base_url}{self.projects_endpoint}"
        return requests.post(url, headers=self.headers, json=payload)

    def update_project(self, project_id, payload):
        url = f"{self.base_url}{self.projects_endpoint}/{{{project_id}}}"
        return requests.put(url, headers=self.headers, json=payload)

    def get_project(self, project_id):
        url = f"{self.base_url}{self.projects_endpoint}/{{{project_id}}}"
        return requests.get(url, headers=self.headers)
