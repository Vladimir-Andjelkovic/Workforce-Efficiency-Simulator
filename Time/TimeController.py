import time


class TimeController:
    def __init__(self, max_days=360, time_interval=30):
        self.max_days = max_days
        self.current_day = 0
        self.time_interval = time_interval

    def advance_time(self) -> bool:
        if self.current_day >= self.max_days:
            return False
        self.current_day += self.time_interval
        return True

