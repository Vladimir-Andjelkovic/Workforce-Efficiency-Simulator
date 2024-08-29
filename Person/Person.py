# TODO: Person has several factors that can affect productivity, INTERNAL and EXTERNAL, which can be further categorized
#  into SHORT TERM (affect productivity for a short time) and LONG TERM (affect productivity for a long time)
import random
from Person.InternalFactors import InternalFactors
from Person.ExternalFactors import ExternalFactors
from Algorithms import AlgorithmUtils


# TODO: add unique identifier(UID) for each person
def _read_and_store(file_path) -> list:
    result = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            result.append(line.strip())
    return result


def _check_validation_of_production_modifier(list1, list2, list3) -> bool:
    return (len(list1) == 2 and all(isinstance(i, float) for i in list1) and
            len(list2) == 2 and all(isinstance(i, float) for i in list2) and
            len(list3) == 2 and all(isinstance(i, float) for i in list3))


class Person:
    FIRST_NAMES_PATH = 'Names/Human/First-Names.txt'
    LAST_NAMES_PATH = 'Names/Human/Last-Names.txt'

    GOOD_WORKER_CHANCE: float = 0.8
    LAZY_WORKER_CHANCE: float = 0.1

    # PRODUCTIVITY_MODIFIER list needs to have two elements (min, max)
    PRODUCTIVITY_MODIFIER_GOOD_WORKER: list = [2.0, 3.0]
    PRODUCTIVITY_MODIFIER_NORMAL_WORKER: list = [0.8, 1.99]
    PRODUCTIVITY_MODIFIER_LAZY_WORKER: list = [0.3, 0.79]

    _last_UID = 0
    all_alive_people = []
    number_of_people: int = 0
    base_productivity: float = 1
    all_first_names = _read_and_store(FIRST_NAMES_PATH)
    all_last_names = _read_and_store(LAST_NAMES_PATH)

    def __init__(self, **kwargs):
        # Factors not yet implemented
        self.internal_factors = InternalFactors()
        self.external_factors = ExternalFactors()

        self._generate_UID()
        self.first_name = kwargs.get('first_name', self._generate_first_name())
        self.last_name = kwargs.get('last_name', self._generate_last_name())
        self.age = kwargs.get('age', 20)
        self.current_money = kwargs.get('current_money', 0)
        self.job_title = kwargs.get('job_title', None)
        self.workplace = kwargs.get('workplace', None)
        self.income = kwargs.get('income', 0)

        if _check_validation_of_production_modifier(
                Person.PRODUCTIVITY_MODIFIER_GOOD_WORKER,
                Person.PRODUCTIVITY_MODIFIER_NORMAL_WORKER,
                Person.PRODUCTIVITY_MODIFIER_LAZY_WORKER
        ):
            self.productivity = Person.base_productivity * AlgorithmUtils.calculate_person_starting_productivity(
                Person.GOOD_WORKER_CHANCE,
                Person.LAZY_WORKER_CHANCE,
                Person.PRODUCTIVITY_MODIFIER_GOOD_WORKER,
                Person.PRODUCTIVITY_MODIFIER_NORMAL_WORKER,
                Person.PRODUCTIVITY_MODIFIER_LAZY_WORKER
            )
        else:
            self.productivity = 0.5

        Person.all_alive_people.append(self)

        Person.number_of_people += 1

    @classmethod
    def DEV_get_all_people(cls) -> list:
        return cls.all_alive_people

    def DEV_display_info(self):
        print(f'UID: {self.UID}\n'
              f'Name: {self.first_name} {self.last_name}\n'
              f'Money: {self.current_money}\n'
              f'Job Title: {self.job_title}\n'
              f'Workplace: {self.workplace}\n'
              f'Income: {self.income}\n'
              f'Productivity: {self.productivity}\n'
              f'-----------------------------------------------------------------------------------------\n')

    def _generate_UID(self) -> None:
        Person._last_UID += 1
        self.UID = Person._last_UID

    @staticmethod
    def _generate_first_name() -> str:
        return random.choice(Person.all_first_names)

    @staticmethod
    def _generate_last_name() -> str:
        return random.choice(Person.all_last_names)

    def _die(self) -> None:
        # TODO: instances should not be deleted but kept in separate list of (dead) people for genetic modification of
        #  their children,grandchildren... (genetics will be affected by multiple generation of people)
        Person.number_of_people -= 1
        del self
