
class StrategyAgent:
    def avoid_conflict(self, robots):
        seen = set()
        for r in robots.values():
            if r.position in seen:
                return "CONFLICT"
            seen.add(r.position)
        return "SAFE"
