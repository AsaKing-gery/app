
class StateAgent:
    def __init__(self):
        self.robots = {}

    def update(self, robot_id, data):
        self.robots[robot_id] = data

    def get_all(self):
        return self.robots
