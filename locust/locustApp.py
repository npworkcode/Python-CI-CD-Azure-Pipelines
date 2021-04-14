import time
from locust import HttpUser, task, between


class LoadApp(HttpUser):
    wait_time = between(1, 10)

    @task
    def load_home(self):
        self.client.get("/")

    @task(3)
    def load_predict(self):
        response = self.client.post("/predict", json={"CHAS": {"0": 0}, "RM": {"0": 6.575}, "TAX": {"0": 296.0},
                                      "PTRATIO": {"0": 15.3}, "B": {"0": 396.9}, "LSTAT": {"0": 4.98}})
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        if response.elapsed.total_seconds() > 5:
            response.failure("Request took too long")
        time.sleep(5)

