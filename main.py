import DEV_TOOLS.Helper as dev_helper

import random
from Environment.Building import Building
from Person.Person import Person
from Time.TimeController import TimeController
from Corporation.Corporation import Corporation
import matplotlib.pyplot as plt
from World.WorldEvents import World
from Algorithms import AlgorithmUtils

if __name__ == '__main__':
    print(AlgorithmUtils.calculate_employee_salary(
        World.jobs_base_salary['default'],
        'default',
        0.00,
        'Master',
        500000.00,
        1.00
    ))
