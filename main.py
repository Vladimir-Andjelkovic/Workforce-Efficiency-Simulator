import random
from Environment.Building import Building
from Person.Person import Person
from Time.TimeController import TimeController

if __name__ == "__main__":

    target_population = 50
    x = 0
    while x < target_population:
        person_info = {
            "age": random.randint(18, 70),
            "current_money": random.randint(500, 3000)
        }
        person = Person(**person_info)
        x += 1

    time_controller = TimeController()

    # while time_controller.advance_time():
    #     pass

    for person in Person.DEV_get_all_people():
        person.DEV_display_info()
