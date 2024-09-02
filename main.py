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
    # Time-World-Population-Buildings-Corporations
    time_controller = TimeController()
    world = World()

    world.generate_starting_population()
    world.generate_starting_corporations()

    while time_controller.advance_time():
        world.update_employment()
        print(f'Unemployed before hiring: {len(world.unemployed_people)}')
        print(f'Employed before hiring: {len(world.employed_people)}')

        for corporation in Corporation.get_all_formed_corporations():
            world.set_unemployed_people(corporation.hire_employees(world.unemployed_people))
            world.update_employment()

        print(f'Unemployed after hiring: {len(world.unemployed_people)}')
        print(f'Employed after hiring: {len(world.employed_people)}')
        print('--------------------------------------')

