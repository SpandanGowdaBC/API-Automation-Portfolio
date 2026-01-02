import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        # We add headers to mimic a real browser to avoid 403 Forbidden errors
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        # Pass self.headers in every request
        response = requests.get(url, headers=self.headers)
        return response

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def put(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=payload, headers=self.headers)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response