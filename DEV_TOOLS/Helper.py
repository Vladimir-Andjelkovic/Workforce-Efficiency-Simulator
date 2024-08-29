TCOLORS = {
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'BLUE': '\033[34m',
    'YELLOW': '\033[33m',
    'BOLD': '\033[1m',
    'UNDERLINED': '\033[4m',
    'RESET': '\033[0m'
}


def check_duplicates(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        num_of_duplicates = 0

        for x in lines:
            x1 = x.strip()
            line_count = 0
            for y in lines:
                y1 = y.strip()
                if y1 == x1:
                    line_count += 1

            if line_count > 1:
                num_of_duplicates += 1
                print(f'Line {TCOLORS['RED']}{x}{TCOLORS["RESET"]} '
                      f'appears {TCOLORS['RED']}{line_count}{TCOLORS['RESET']} times!')
        print(f'\nNumber of duplicates: {num_of_duplicates}')
