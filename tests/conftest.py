import pytest
from config import BASE_URL
from utils.api_client import APIClient

@pytest.fixture(scope="class")
def api_client(request):
    client = APIClient(BASE_URL)
    # Attach client to the test class so we can use self.client
    request.cls.client = client
    yield client