# api_test_project 🟢

End-to-end REST API tests against [restful-booker](https://restful-booker.herokuapp.com/), with a pluggable auth layer and Allure reporting. Runs in GitHub Actions on every push.

## Stack

- **Python 3.11+**, `pytest`, `requests`
- **Allure** for human-readable reports (`allure-pytest`)
- **PyYAML** for config, **jsonpath-ng** for response assertions
- **Docker** service in CI: `mwinteringham/restfulbooker` on `:3001`

## What's interesting here

- **Pluggable auth strategy** (`utils/auth.py`) — `CookieTokenAuth` and `BearerTokenAuth` share one `BaseAuthStrategy` interface. Switching between them is a one-line config change, not a code rewrite.
- **Swappable credential encryptors** — `PlainTextEncryptor`, `Md5Encryptor`, `Sha256Encryptor` behind a `CredentialEncryptor` ABC, so the same test suite can target APIs that hash passwords differently.
- **Factory wiring** — `build_auth_strategy(auth_type, encrypt_type)` is driven by `config/config.yaml` keys `auth_type` and `password_encrypt_type`.

## Layout

```
api_test_project/
├── config/
│   ├── config.yaml        # base_url, credentials, auth_type, encrypt_type
│   └── testData.json      # booking fixtures
├── utils/
│   ├── api_client.py      # thin requests wrapper, auth-strategy aware
│   ├── auth.py            # auth strategies + credential encryptors
│   └── config_loader.py
├── tests/
│   ├── test_auth_strategy.py          # unit tests for auth layer
│   ├── test_restful_booker_ping_api.py
│   └── test_booking.py                # end-to-end CRUD
├── conftest.py            # session fixtures: config + authed api client
├── pytest.ini
└── requirements.txt
```

## Run locally

```bash
cd api_test_project
pip install -r requirements.txt

# 1. Start the mock API on :3001
docker run -d -p 3001:3001 mwinteringham/restfulbooker:latest

# 2. Run the suite
pytest tests/ -v

# Optional: Allure report
pytest tests/ -v --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Run in CI

Every push triggers [`.github/workflows/test.yml`](../.github/workflows/test.yml), which spins up the `mwinteringham/restfulbooker` service container and runs the full suite against it.

## Config

`config/config.yaml`:

```yaml
base_url: "http://localhost:3001"
ping_path: "/ping"
time_out: 5
max_avg_time_ms: 500
username: "admin"
password: "password123"
auth_type: "cookie_token"          # or "bearer_token"
password_encrypt_type: "plain"     # or "md5" / "sha256"
```
