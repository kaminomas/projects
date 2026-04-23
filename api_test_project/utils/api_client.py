import requests


class Client:
    def __init__(self, base_url, auth_strategy=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth_strategy = auth_strategy

    def login(self, username, password):
        if self.auth_strategy is None:
            return None
        return self.auth_strategy.authenticate(
            base_url=self.base_url,
            username=username,
            password=password,
            session=self.session,
        )

    def request(self, method, path, **kwargs):
        request_kwargs = dict(kwargs)
        if self.auth_strategy is not None:
            request_kwargs = self.auth_strategy.prepare_request_kwargs(
                method=method,
                path=path,
                **request_kwargs,
            )
        return self.session.request(method, f"{self.base_url}{path}", **request_kwargs)

    def get(self, path):
        return self.request("GET", path)

    def post(self, path, json=None):
        return self.request("POST", path, json=json)

    def put(self, path, json=None):
        return self.request("PUT", path, json=json)
