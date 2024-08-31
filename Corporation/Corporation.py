# corpa productivity formula
# average productivity score of employees (internal)
# market conditions (external)
# workplace culture (internal / prob later after adding person traits and compatibility with others)
# tech level (internal)
# TODO: expand as factors expand
import random
from Person.Person import Person
from World.WorldEvents import World


class Corporation:
    _last_CID = 0
    all_available_corporation_names = []
    corporation_names_paths = {
        'food_industry': 'Names/Corporation/FoodIndustry.txt',
        'paper_industry': 'Names/Corporation/PaperIndustry.txt'
    }

    try:
        for key, value in corporation_names_paths.items():
            with open(value, 'r') as f:
                for line in f.readlines():
                    all_available_corporation_names.append(line.strip())
    except FileNotFoundError:
        print('Some or all corporation names files not found.')

    formed_corporations = []
    all_employees = []

    def __init__(self):
        self._generate_CID()
        self._generate_name()

        Corporation.formed_corporations.append(self)

    def get_CID(self):
        return self.CID

    def get_name(self):
        return self.name

    def _generate_CID(self):
        Corporation._last_CID += 1
        self.CID = Corporation._last_CID

    def _generate_name(self):
        if len(Corporation.all_available_corporation_names) > 0:
            random_name = random.choice(Corporation.all_available_corporation_names)
            self.name = random_name
            Corporation.all_available_corporation_names.remove(random_name)
        else:
            print('There are no corporation names to choose from')

    def hire_employee(self, employee: Person):
        # TODO: algorithm for calculating salary
        pass
