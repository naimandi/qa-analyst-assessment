import requests
import pytest


"""
solution.py

This is an API testing script that uses `pytest`. 

The tests use the public JSONPlaceholder API (https://jsonplaceholder.typicode.com)
to verify API operations such as GET, POST, and error handling.

"""

TARGET_API = "https://jsonplaceholder.typicode.com"

class TestJSONPlaceholderAPI:
    def test_fetch_user_successfully(self):
        """
        Test GET /users/1 returns status code 200 and contains the required fields
        """
        # send a GET request for user with ID 1
        response = requests.get(f"{TARGET_API}/users/1")
        # check the response status code
        assert response.status_code == 200, "Expected status code 200 (OK)"
        user = response.json() # parse JSON response
        required_fields = ["id", "name", "email"]
        for field in required_fields: # check if required fields are in the response
            assert field in user, f"Missing field: {field}"
        
    def test_create_new_post(self):
        """
        Test POST /posts returns status code 201 and includes all expected fields with correct values
        """
        # define payload
        content = {
            "title": "My test post",
            "body": "testing.....",
            "userId": 1
        }

        # send POST request 
        response = requests.post(f"{TARGET_API}/posts", json=content)
        
        # check that the post was created successfully
        assert response.status_code == 201, "Expected status code 201 (Created)"
        
        # parse JSON response
        data = response.json()

        expected_fields = ["title", "body", "userId", "id"]
        for field in expected_fields:  # check that all expected fields are present
            assert field in data, f"Missing field: {field}"

        # check that the response fields have the same values as the request payload        
        for key in ["title", "body", "userId"]:
            assert data[key] == content[key], f"Field '{key}' value does not match payload"

            
    def test_handle_nonexistent_user(self):
        """
        Test GET /users/999 returns status code 404 and an empty response for a non-existent user
        """
        # send a GET request for a user ID that does not exist
        response = requests.get(f"{TARGET_API}/users/999")

        # check the response status code
        assert response.status_code == 404, "Expected status code 404 (Not Found)"
    
        assert response.json() == {}  # check that an empty JSON object is returned 