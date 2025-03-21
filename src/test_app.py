from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_signup_for_activity():
    response = client.post("/activities/Chess Club/signup?email=test@mergington.edu")
    assert response.status_code == 200
    assert response.json() == {"message": "Signed up test@mergington.edu for Chess Club"}

def test_unregister_from_activity():
    client.post("/activities/Chess Club/signup?email=test@mergington.edu")
    response = client.post("/activities/Chess Club/unregister?email=test@mergington.edu")
    assert response.status_code == 200
    assert response.json() == {"message": "Unregistered test@mergington.edu from Chess Club"}

def test_unregister_not_signed_up():
    response = client.post("/activities/Chess Club/unregister?email=not_signed_up@mergington.edu")
    assert response.status_code == 400
    assert response.json() == {"detail": "Student is not signed up for this activity"}