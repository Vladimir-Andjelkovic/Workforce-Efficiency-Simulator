from Corporation.Corporation import Corporation
from Person.Person import Person


class World:
    # TODO: maybe store alive (and dead) humans here, depending on the future logic
    initial_population_size: int = 1000
    initial_corporation_count: int = 10
    employed_people = []
    unemployed_people = []

    jobs_base_salary = {
        # TODO: add jobs and their base salaries go here (abstract starting point)
        'worker': 50000.00,
        'developer': 90000.00
    }

    def __init__(self):
        # TODO: algorithm for calculating market stability
        self.market_stability: float = 1.00

    @staticmethod
    def update_employment():
        for person in Person.all_alive_people:
            if person.get_workplace():
                World.employed_people.append(person)
            else:
                World.unemployed_people.append(person)

    def get_market_stability(self) -> float:
        return self.market_stability

    def set_market_stability(self, value: float) -> None:
        self.market_stability = value

    def get_employed_people(self) -> list:
        return self.employed_people

    def set_employed_people(self, people: list) -> None:
        self.employed_people = people

    def get_unemployed_people(self) -> list:
        return self.unemployed_people

    def set_unemployed_people(self, people: list) -> None:
        self.unemployed_people = people

    def generate_starting_population(self, population_size=initial_population_size):
        for person in range(population_size):
            Person(self)

    def generate_starting_corporations(self, corporation_count=initial_corporation_count):
        for corporation in range(corporation_count):
            Corporation(self)
