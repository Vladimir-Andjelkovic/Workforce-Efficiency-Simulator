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


def calculate_employee_salary(
        start_base_salary: float,
        job_role,
        experience,
        education_level,
        corporation_profit,
        market_demand
) -> float:
    """
    Calculates the salary for the employee

    Parameters:
    start_base_salary  (float): Abstract number set at the world creation.
    job_role             (str): Job role of the employee.
    experience         (float): Experience level of the employee (presented in years).
    education_level      (str): Education of the employee.
    corporation_profit (float): Yearly profit of the company.
    market_demand      (float): Market demand of the job role.


    Returns:
    float: The calculated salary
    """

    #     Notes to self: Average college graduates make up 35-40 % of the population, from which 60-70 % have bachelors,
    #     20-30 % have master and 1-5 % have PhD
    base_salary = {
        # TODO: add/calculate additional jobs and their salaries
    }.get(job_role, start_base_salary)

    experience_factor = 0.03  # 3% increase in salary for each year of exp
    if experience >= 1:
        base_salary += base_salary * (experience * experience_factor)

    # TODO: multiplier should be dynamic, calculated for each corpa
    education_multiplier = {
        'Bachelor': 1.0,
        'Master': 1.3,
        'PhD': 1.7
    }.get(education_level, 0.7)
    base_salary *= education_multiplier

    profit_multiplier = 1.0
    if corporation_profit > 1000000.00:
        # increase based on company yearly profit for each million
        profit_multiplier = 1.0 + (corporation_profit / 1000000.00)
    base_salary *= profit_multiplier

    base_salary *= market_demand

    return base_salary
