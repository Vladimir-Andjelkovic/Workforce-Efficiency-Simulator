

class Building:
    def __init__(self, floor_count: int = 1, cleanliness: float = 1.00, aesthetics: float = 1.00, **kwargs):
        self.floor_count = floor_count
        self.cleanliness = cleanliness
        self.aesthetics = aesthetics

        for key, value in kwargs.items():
            setattr(self, key, value)
