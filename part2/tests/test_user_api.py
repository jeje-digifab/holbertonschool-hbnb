import unittest
from app import create_app
from app.services.facade import HBnBFacade


class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.facade = HBnBFacade()
        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@example.com",
            "password": "securepassword"
        }

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json=self.user_data)
        self.assertEqual(response.status_code, 201)

        user = response.get_json()
        print(f"Created user: {user}")

        # Check that the created user is present in the list of users
        all_users = self.facade.get_all_users()
        self.assertIn(user['email'], [u.email for u in all_users])

    def test_create_user_and_check_uuid(self):
        response = self.client.post('/api/v1/users/', json=self.user_data)
        self.assertEqual(response.status_code, 201)

        user = response.get_json()
        print(f"Created user UUID: {user['id']}")

        # Check that the UUID of the user is valid
        self.assertIsNotNone(user['id'])

    def test_create_user_with_duplicate_email(self):
        # Create the first user
        response = self.client.post('/api/v1/users/', json=self.user_data)
        self.assertEqual(response.status_code, 201)

        # Attempt to create a user with the same email
        response_duplicate = self.client.post(
            '/api/v1/users/', json=self.user_data)
        # Expecting an error for duplicate email
        self.assertEqual(response_duplicate.status_code, 400)

    def test_create_user_with_empty_password(self):
        # Attempt to create a user with an empty password
        invalid_user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "empty_password@example.com",
            "password": ""
        }
        response = self.client.post('/api/v1/users/', json=invalid_user_data)
        # Expecting an error for empty password
        self.assertEqual(response.status_code, 400)

    def test_create_user_with_short_password(self):
        # Attempt to create a user with a too-short password
        invalid_user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "short_password@example.com",
            "password": "123"
        }
        response = self.client.post('/api/v1/users/', json=invalid_user_data)
        # Expecting an error for short password
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
