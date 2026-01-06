import requests
import time

# Give the server time to start
time.sleep(3)

response = requests.get(
    "http://localhost:8000/predict",
    params={"text": "smoke-test"}
)

assert response.status_code == 200
print("Smoke test passed")
