from Person.Person import Person


class World:
    initial_population_size = 100
    current_population_size = 0

    def __init__(self):
        # TODO: algorithm for calculating market stability
        self.market_stability = 1

    def get_market_stability(self):
        return self.market_stability

    def generate_starting_population(self, population_size=initial_population_size):
        per1 = Person()