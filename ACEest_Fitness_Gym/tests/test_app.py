import sys
import os

# Add parent folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app



def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_members():
    tester = app.test_client()
    response = tester.get('/members')
    assert response.status_code == 200


def test_workouts():
    tester = app.test_client()
    response = tester.get('/workouts')
    assert response.status_code == 200