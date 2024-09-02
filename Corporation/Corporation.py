# corpa productivity formula
# average productivity score of employees (internal)
# market conditions (external)
# workplace culture (internal / prob later after adding person traits and compatibility score with others)
# tech level (internal)
# TODO: expand as factors expand
import random
from Algorithms import AlgorithmUtils


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

    def __init__(self, world):
        self._generate_CID()
        self._generate_name()
        self.world = world
        self.max_number_of_employees = random.randint(10, 100)

        Corporation.formed_corporations.append(self)

    @staticmethod
    def get_all_formed_corporations() -> list:
        return Corporation.formed_corporations

    def get_CID(self):
        return self.CID

    def get_name(self):
        return self.name

    def set_name(self, value: str):
        self.name = value

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

    def hire_employees(self, unemployed_people: list):
        # TODO: After adding HR, number of employees that can be hired in one time interval should be based on the
        #  resources available to the HR department
        unemployed_people.sort(key=lambda instance: instance.productivity, reverse=True)

        candidates = []

        while len(candidates) < self.max_number_of_employees:
            if len(unemployed_people) > 0:
                candidate = unemployed_people.pop(0)
                candidates.append(candidate)
                # TODO: jobs relevant to industry
                job_position = 'worker'
                salary = AlgorithmUtils.calculate_employee_salary(
                    self.world.jobs_base_salary[job_position],
                    job_position,
                    0,
                    candidate.education_level,
                    500000.00,
                    1.0
                )
                candidate.assign_job(self, job_position, salary)

        return unemployed_people
