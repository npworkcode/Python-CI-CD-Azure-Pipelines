import time
from locust import HttpUser, task, between

class FlaskHttpUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def load_home(self):
        self.client.get("/")

    @task(3)
    def load_predict(self):
        self.client.get("/predict")