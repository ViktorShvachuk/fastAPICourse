import json


def test_create_job(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2022-07-20"
    }

    response = client.post("/jobs/create-job", json.dumps(data))
    assert response.status_code == 200


def test_tetreive_job_by_id(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2022-07-20"
    }

    client.post("/jobs/create-job", json.dumps(data))

    response = client.get("/jobs/get/1")

    assert response.status_code == 200
    assert response.json()["title"] == data["title"]
