import pytest 
import uuid
from app import app 

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "UP"}

def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data,list)
    assert len(data)>=1

def test_register(client):
    email = f"{uuid.uuid4()}@gmail.com"
    response = client.post("/register",json={"name":"rahul","email":email})
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "User added successfully"
   