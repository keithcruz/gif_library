import requests


class GiphyApi:
    def __init__(self):
        self.giphy_url = "https://api.giphy.com/v1/gifs"
        self.api_key = ""

    def init_app(self, app):
        self.api_key = app.config.get("GIPHY_API_KEY", "")

    def search(self, query, offset):
        result = requests.get(
            f"{self.giphy_url}/search",
            params={
                "api_key": self.api_key,
                "limit": 12,
                "rating": "g",
                "q": query,
                "offset": offset
            },
            timeout=10
        )

        return result.json()
