import unittest
from uuid import uuid4
from app import app


class FlaskAuthTests(unittest.TestCase):
    def setUp(self):
        """
        Тестовий клієнт Flask.
        """
        self.client = app.test_client()
        self.client.testing = True

    # ---------------------------------------------------
    # REGISTER
    # ---------------------------------------------------

    def test_register_success(self):

        response = self.client.post(
            "/register",
            data={"username": "testuser1" + str(uuid4()), "password": "123456"},
        )

        # redirect на /login
        self.assertEqual(response.status_code, 302)

    def test_register_short_password(self):

        response = self.client.post(
            "/register", data={"username": "testuser2" + str(uuid4()), "password": "123"}
        )

        self.assertEqual(response.status_code, 400)

    def test_register_duplicate(self):

        self.client.post(
            "/register", data={"username": "dupuser", "password": "123456"}
        )

        response = self.client.post(
            "/register", data={"username": "dupuser", "password": "123456"}
        )

        self.assertEqual(response.status_code, 409)

    # ---------------------------------------------------
    # LOGIN
    # ---------------------------------------------------

    def test_login_success(self):

        self.client.post(
            "/register", data={"username": "loginuser", "password": "strongpass"}
        )

        response = self.client.post(
            "/login", data={"username": "loginuser", "password": "strongpass"}
        )

        self.assertEqual(response.status_code, 302)

    def test_login_wrong_password(self):

        self.client.post(
            "/register", data={"username": "wrongpassuser", "password": "strongpass"}
        )

        response = self.client.post(
            "/login", data={"username": "wrongpassuser", "password": "wrong"}
        )

        self.assertEqual(response.status_code, 401)

    def test_login_user_not_found(self):

        response = self.client.post(
            "/login", data={"username": "ghost", "password": "123456"}
        )

        self.assertEqual(response.status_code, 401)

    # ---------------------------------------------------
    # PROFILE
    # ---------------------------------------------------

    def test_profile_without_login(self):

        response = self.client.get("/profile")

        self.assertEqual(response.status_code, 302)

    def test_profile_with_login(self):

        self.client.post(
            "/register", data={"username": "profileuser", "password": "123456"}
        )

        self.client.post(
            "/login", data={"username": "profileuser", "password": "123456"}
        )

        response = self.client.get("/profile")

        self.assertEqual(response.status_code, 200)

    # ---------------------------------------------------
    # LOGOUT
    # ---------------------------------------------------

    def test_logout(self):

        self.client.post(
            "/register", data={"username": "logoutuser", "password": "123456"}
        )

        self.client.post(
            "/login", data={"username": "logoutuser", "password": "123456"}
        )

        response = self.client.get("/logout")

        self.assertEqual(response.status_code, 302)


    def test_calc(self):
        response = self.client.post(
            "/calc", data={"n1": "1", "n2": "1"}
        )


        self.assertEqual(response.text, "2")


if __name__ == "__main__":
    unittest.main()
