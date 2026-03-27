import requests

def test_booker_ping_api(config_data):
    times = []

    url = config_data["base_url"] + config_data["ping_path"]
    timeout = config_data["time_out"]
    max_avg_time_ms = config_data["max_avg_time_ms"]

    for _ in range(5):
        resp = requests.get(url, timeout=timeout)
        assert resp.status_code == 201
        times.append(resp.elapsed.total_seconds() * 1000)

        print(times)

        avg_time = sum(times) / len(times)
        assert avg_time < max_avg_time_ms
