
class SchedulerAgent:
    def assign_task(self, task, robots):
        candidates = [r for r in robots.values() if r.status=="IDLE" and r.battery>30]
        if not candidates:
            return None
        best = max(candidates, key=lambda r: r.battery)
        best.task = task
        best.status = "BUSY"
        return best.id
