from os import environ
from unittest import TestCase

environ["TESTING"] = "true"

from app import app

class AppTestCase(TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_home(self) -> None:
        get_response = self.client.get("/")
        assert get_response.status_code == 302

        get_response = self.client.get("/home")
        assert get_response.status_code == 200

        html = get_response.get_data(as_text=True)

        assert "<title>Nothing to see here</title>" in html
        assert "<head" in html
        assert "<body" in html

    def test_timeline_page(self) -> None:
        get_response = self.client.get("/timeline")
        assert get_response.status_code == 200

        html = get_response.get_data(as_text=True)

        assert "<input" in html

    def test_timeline_api(self) -> None:
        get_response = self.client.get("/api/timeline_post")

        assert get_response.status_code == 200
        assert get_response.is_json

        json = get_response.get_json()

        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        post_response = self.client.post("/api/timeline_post", data={
            "name":    "########",
            "email":   "hi@ex.co",
            "content": "########"
        })

        assert post_response.status_code == 200

    def test_malformed_timeline_post(self) -> None:
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={
            "email":"john@example.com",
            "content":"Hello world, I'm John!"
        })

        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={
            "name":"John Doe",
            "email":"john@example.com",
            "content":""
        })

        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={
            "name":"John Doe",
            "email":"not-an-email",
            "content":"Hello world, I'm John!"
        })

        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html