# ui_test_project 🟡

Browser UI automation using **Selenium Remote WebDriver** against a containerized **Selenium Grid**, structured with the **Page Object Model**.

> **Status:** Works locally once the Grid is up. The smoke test is skipped in CI (no Grid container there) — re-enable with `SELENIUM_HUB_RUNNING=1`.

## Stack

- **Python 3.11+**, `pytest`, `selenium`
- **Selenium Grid** via `docker-compose.yml` (Hub + Chrome node)
- **Page Object Model** under `pages/`
- `python-dotenv`, `PyYAML` for config

## Layout

```
ui_test_project/
├── config/config.yaml        # base_url, selenium_hub, browser
├── docker-compose.yml        # Selenium Grid (hub + chrome)
├── pages/
│   └── login_page.py         # POM example
├── utils/
│   └── driver_factory.py     # create_remote_driver()
├── tests/
│   ├── test_first.py
│   ├── test_login.py
│   └── test_ui_demo.py       # gated by SELENIUM_HUB_RUNNING
├── conftest.py               # driver + config fixtures
├── pytest.ini
└── requirements.txt
```

## Run locally

```bash
cd ui_test_project
pip install -r requirements.txt

# 1. Start the Selenium Grid
docker compose up -d

# 2. Enable the gated smoke test and run
export SELENIUM_HUB_RUNNING=1
pytest tests/ -v

# 3. Tear down when done
docker compose down
```

The Selenium Hub console lives at <http://localhost:4444> while the Grid is running.

## Why the test is skipped in CI

`test_open_home` hits a live external site via a Selenium Grid on `localhost:4444`. The current CI job doesn't provision that Grid as a service container, so the test is gated behind `SELENIUM_HUB_RUNNING=1` to keep the pipeline green. Follow-up: add a Grid service container to the workflow and drop the gate.
