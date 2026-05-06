
class RobotState:
    def __init__(self, id):
        self.id = id
        self.position = (0,0)
        self.battery = 100
        self.status = "IDLE"
        self.task = None
