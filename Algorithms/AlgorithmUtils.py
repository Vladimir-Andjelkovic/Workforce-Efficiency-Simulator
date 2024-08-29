import random
from Helper import Helper


def calculate_corporation_productivity(employee_productivity=0, market_stability=0, tech_level=0):
    return employee_productivity * market_stability * tech_level


def calculate_person_starting_productivity(
        good_worker_chance,
        lazy_worker_chance,
        productivity_modifier_good_worker,
        productivity_modifier_normal_worker,
        productivity_modifier_lazy_worker
):
    random_productivity_modifier: float = 1
    productivity_chance: float = random.random()

    if productivity_chance >= good_worker_chance:
        random_productivity_modifier = Helper.random_float_from_list(productivity_modifier_good_worker)
    elif good_worker_chance > productivity_chance > lazy_worker_chance:
        random_productivity_modifier = Helper.random_float_from_list(productivity_modifier_normal_worker)
    elif productivity_chance <= lazy_worker_chance:
        random_productivity_modifier = Helper.random_float_from_list(productivity_modifier_lazy_worker)

    return random_productivity_modifier
