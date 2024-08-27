import random


class Helper:
    def __init__(self):
        pass

    def random_float_from_list(self, list_values: list[float]) -> float | None:
        low_value = list_values[0]
        high_value = list_values[1]
        return random.uniform(low_value, high_value)

    def get_random_line_from_txt(self, file_path) -> str | ValueError:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        if not lines:
            return ValueError("First name file is empty.")

        return random.choice(lines).strip()
