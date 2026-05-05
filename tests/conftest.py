import pytest
from copy import deepcopy
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src directory to path for importing app
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from app import app, activities

original_activities = deepcopy(activities)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(deepcopy(original_activities))
    yield
    activities.clear()
    activities.update(deepcopy(original_activities))
