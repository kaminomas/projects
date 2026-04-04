import requests

class Client:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        resp = requests.post(f"{self.base_url}/auth", json={"username": username, "password": password})
        self.token = resp.json()["token"]


    def get(self, path):
        return requests.get(f"{self.base_url}{path}")

    def post(self, path, json=None):
        return requests.post(f"{self.base_url}{path}", json=json)

    def put(self, path, json=None):
        return requests.put(f"{self.base_url}{path}", json=json, headers={"Cookie": f"token={self.token}"})


