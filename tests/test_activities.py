def test_get_all_activities(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "description" in data["Chess Club"]
    assert "participants" in data["Chess Club"]
    assert isinstance(data["Chess Club"]["participants"], list)


def test_get_activities_returns_expected_fields(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    activity = response.json()["Programming Class"]
    assert set(activity.keys()) >= {"description", "schedule", "max_participants", "participants"}
    assert isinstance(activity["max_participants"], int)
    assert isinstance(activity["participants"], list)
