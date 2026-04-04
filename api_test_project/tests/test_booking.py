import pytest
import json

with open("config/testData.json", "r") as f:
    test_data = json.load(f)

def test_booking(api):
    resp = api.get("/booking")
    data_list = resp.json()
    assert resp.status_code == 200
    data_id = data_list[0]["bookingid"]

    resp2 = api.get(f"/booking/{data_id}")
    data = resp2.json()
    assert resp2.status_code == 200
    assert "firstname" in data
    assert "lastname" in data

def test_booking_not_found(api):
    resp = api.get("/booking/99999")
    assert resp.status_code == 404


@pytest.mark.parametrize("data", test_data)
def test_create_booking(data, api):
    resp3 = api.post("/booking", json=data)
    data_create = resp3.json()
    assert resp3.status_code == 200
    assert data_create["booking"]["firstname"] == data["firstname"]
    assert data_create["booking"]["lastname"] == data["lastname"]

def test_update_booking(api):
    resp = api.get("/booking")
    booking_id = resp.json()[0]["bookingid"]
    update_data = {
        "firstname": "Updated",
        "lastname": "Name",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-05"}
    }
    resp5 = api.put(f"/booking/{booking_id}", json=update_data)
    assert resp5.status_code == 200
    assert resp5.json()["firstname"] == "Updated"

