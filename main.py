
from fastapi import FastAPI
from app.agents.state_agent import StateAgent
from app.agents.scheduler_agent import SchedulerAgent
from app.agents.strategy_agent import StrategyAgent
from app.models.robot_state import RobotState

app = FastAPI()

state_agent = StateAgent()
scheduler = SchedulerAgent()
strategy = StrategyAgent()

@app.get("/")
def root():
    return {"msg": "Multi-Robot Agent System Running"}

@app.post("/update")
def update(robot_id: str, battery: int, x: int, y: int, status: str):
    r = RobotState(robot_id)
    r.battery = battery
    r.position = (x, y)
    r.status = status
    state_agent.update(robot_id, r)
    return {"ok": True}

@app.post("/assign_task")
def assign(task: str):
    robots = state_agent.get_all()
    rid = scheduler.assign_task(task, robots)
    return {"assigned_to": rid}

@app.get("/check_conflict")
def check():
    robots = state_agent.get_all()
    return {"status": strategy.avoid_conflict(robots)}
