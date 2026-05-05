def test_unregister_success(client):
    # Arrange
    signup_url = "/activities/Chess Club/signup"
    unregister_email = "unregister@mergington.edu"
    client.post(signup_url, params={"email": unregister_email})
    url = "/activities/Chess Club/signup"
    params = {"email": unregister_email}

    # Act
    response = client.delete(url, params=params)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered unregister@mergington.edu from Chess Club"


def test_unregister_not_signed_up(client):
    # Arrange
    url = "/activities/Chess Club/signup"
    params = {"email": "missing@mergington.edu"}

    # Act
    response = client.delete(url, params=params)

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student not signed up"


def test_unregister_invalid_activity(client):
    # Arrange
    url = "/activities/Invalid Activity/signup"
    params = {"email": "test@mergington.edu"}

    # Act
    response = client.delete(url, params=params)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
