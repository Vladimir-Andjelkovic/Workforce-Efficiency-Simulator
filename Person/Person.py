# TODO: Person has several factors that can affect productivity, INTERNAL and EXTERNAL, which can be further categorized
#  into SHORT TERM (affect productivity for a short time) and LONG TERM (affect productivity for a long time)
import random
from Person.InternalFactors import InternalFactors
from Person.ExternalFactors import ExternalFactors
from Helper.Helper import Helper


class Person:

    GOOD_WORKER_CHANCE: float = 0.8
    LAZY_WORKER_CHANCE: float = 0.05

    # PRODUCTIVITY_MODIFIER list needs to have two elements (min, max)
    # TODO: add some validation
    PRODUCTIVITY_MODIFIER_GOOD_WORKER: list = [2, 3]
    PRODUCTIVITY_MODIFIER_NORMAL_WORKER: list = [0.8, 1.99]
    PRODUCTIVITY_MODIFIER_LAZY_WORKER: list = [0.3, 0.79]

    helper = Helper()
    all_people = []
    number_of_people: int = 0
    base_productivity: float = 1

    def __init__(self, **kwargs):
        self.internal_factors = InternalFactors()
        self.external_factors = ExternalFactors()

        self.age = kwargs.get('age', 20)
        self.current_money = kwargs.get('current_money', 0)
        self.job_title = kwargs.get('job_title', None)
        self.workplace = kwargs.get('workplace', None)
        self.income = kwargs.get('income', 0)

        self.first_name = self.__generate_first_name()
        self.last_name = self.__generate_last_name()
        self.productivity = self.base_productivity
        self.all_people.append(self)

        Person.number_of_people += 1

        self.__calculate_starting_productivity()

    @classmethod
    def DEV_get_all_people(cls) -> list:
        return cls.all_people

    def DEV_display_info(self):
        print(f'Name: {self.first_name} {self.last_name}\n'
              f'Money: {self.current_money}\n'
              f'Job Title: {self.job_title}\n'
              f'Workplace: {self.workplace}\n'
              f'Income: {self.income}\n'
              f'Productivity: {self.productivity}\n'
              f'-----------------------------------------------------------------------------------------\n')

    def __calculate_starting_productivity(self) -> None:
        random_productivity_modifier: float = 1
        productivity_chance: float = random.random()

        if productivity_chance >= self.GOOD_WORKER_CHANCE:
            random_productivity_modifier = self.helper.random_float_from_list(self.PRODUCTIVITY_MODIFIER_GOOD_WORKER)
        elif self.GOOD_WORKER_CHANCE > productivity_chance > self.LAZY_WORKER_CHANCE:
            random_productivity_modifier = self.helper.random_float_from_list(self.PRODUCTIVITY_MODIFIER_NORMAL_WORKER)
        elif productivity_chance <= self.LAZY_WORKER_CHANCE:
            random_productivity_modifier = self.helper.random_float_from_list(self.PRODUCTIVITY_MODIFIER_LAZY_WORKER)

        self.productivity *= random_productivity_modifier

    def __generate_first_name(self) -> str:
        return self.helper.get_random_line_from_txt("HumanNames/US-FIRST-NAMES.txt")

    def __generate_last_name(self) -> str:
        return self.helper.get_random_line_from_txt("HumanNames/US-LAST-NAMES.txt")

    def __die(self) -> None:
        self.number_of_people -= 1
        del self

