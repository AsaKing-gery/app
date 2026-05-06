
import time
import random
import requests

SERVER = "http://127.0.0.1:8000"

def simulate(robot_id):
    while True:
        data = {
            "robot_id": robot_id,
            "battery": random.randint(20,100),
            "x": random.randint(0,10),
            "y": random.randint(0,10),
            "status": "IDLE"
        }
        requests.post(SERVER+"/update", params=data)
        time.sleep(2)

if __name__ == "__main__":
    simulate("robot_1")
