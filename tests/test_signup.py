def test_signup_success(client):
    # Arrange
    url = "/activities/Chess Club/signup"
    params = {"email": "test@mergington.edu"}

    # Act
    response = client.post(url, params=params)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@mergington.edu for Chess Club"


def test_signup_duplicate_prevented(client):
    # Arrange
    url = "/activities/Chess Club/signup"
    params = {"email": "duplicate@mergington.edu"}
    client.post(url, params=params)

    # Act
    response = client.post(url, params=params)

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_invalid_activity(client):
    # Arrange
    url = "/activities/Invalid Activity/signup"
    params = {"email": "test@mergington.edu"}

    # Act
    response = client.post(url, params=params)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
