import requests


class GiphyApi:
    def __init__(self):
        self.giphy_url = "https://api.giphy.com/v1/gifs"
        self.api_key = ""

    def init_app(self, app):
        self.api_key = app.config.get("GIPHY_API_KEY", "")

    def search(self, query):
        result = requests.get(
            f"{self.giphy_url}/search",
            params={
                "api_key": self.api_key,
                "limit": 12,
                "rating": "g",
                "q": query
            }
        )

        return result.json()

    def get(self, ids):
        result = requests.get(
            f"{self.giphy_url}",
            params={
                "api_key": self.api_key,
                "ids": ids
            }
        )

        return result.json()
