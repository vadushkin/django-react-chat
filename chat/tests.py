from rest_framework.test import APITestCase


class TestMessage(APITestCase):
    message_url = "/api/messages"

    def test_post_message(self):
        test_payload = {
            "username": "Oak",
            "message": "I'm the biggest plant in the world",
        }

        response = self.client.post(self.message_url, data=test_payload)
        result = response.json()

        self.assertEqual(response.status_code, 200)

        self.assertEqual(result, [])
        self.assertNotEqual(result, ())
