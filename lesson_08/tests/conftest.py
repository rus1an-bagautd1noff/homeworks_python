import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("API_URL")


@pytest.fixture(scope="session")
def auth_header():
    token = os.getenv("API_TOKEN")
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def project_id():
    return os.getenv("PROJECT_ID")
