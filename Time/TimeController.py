import time


class TimeController:
    def __init__(self, max_days: int = 2, time_interval: int = 1):
        """
        Controls the passage of time

        Parameters:
        max_days      (int): maximum number of days that the simulation will run
        time_interval (int): time interval when the loop starts again (ex. when set to X, all logic for actions will be
                             calculated every X day/days)
        """
        self.max_days = max_days
        self.current_day = 0
        self.time_interval = time_interval

    def get_max_days(self) -> int:
        return self.max_days

    def set_max_days(self, value: int) -> None:
        self.max_days = value

    def get_current_day(self) -> int:
        return self.current_day

    def set_current_day(self, value: int) -> None:
        self.current_day = value

    def get_time_interval(self) -> int:
        return self.time_interval

    def set_time_interval(self, value: int) -> None:
        self.time_interval = value

    def advance_time(self) -> bool:
        if self.current_day >= self.max_days:
            return False
        self.current_day += self.time_interval
        return True

