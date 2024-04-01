"""Calc using dict"""


# waznym wnioskiem jest tez wsm to, ze tutaj sa namespacey
# tzn global / local (dlatego nazwy zmiennych w metodach
# nie powinny byc takie same
def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def add(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def check_input_num(number_index):
    """Check input number"""
    # wprowadzenie 1 liczby
    is_valid = False
    while not is_valid:
        num = input(f"Enter {number_index} number: ")
        if not num.isnumeric():
            print("Invalid")
            continue
        else:
            return int(num)


def show_available_operations():
    """Showing available operations"""
    print("Available operations:")
    for indx, operation in enumerate(operations.keys()):
        print(f"{indx + 1}. {operations[operation].__name__} ({operation})")
    print()


def check_input_operation():
    is_valid = False
    while not is_valid:
        oper = input(f"Enter operator: ")
        if oper not in operations.keys():
            print("Invalid")
            continue
        else:
            return operations[oper]


def does_player_continue_msg():
    answer = input("Do yo want to continue? Type: (yes/no) or (y/n): ")
    return answer.lower() == "yes" or answer.lower() == "y"


def does_player_reset_msg():
    answer = input(
        "Does yo want to continue from scratch? Type: (yes/no) or (y/n): ")
    return answer.lower() == "yes" or answer.lower() == "y"


def default_round():
    # wprowadzenie 1 liczby
    first_num = check_input_num("first")

    # wprowadzenie operacji
    show_available_operations()
    operation = check_input_operation()

    # wprowadzenie 2 liczby
    second_num = check_input_num("second")

    # wynik
    print("Result of operation: ", operation(first_num, second_num))
    return operation(first_num, second_num)


def run_fresh_calc():
    # inicjajca
    round_number = 3

    # hello_msg
    print(logo)

    # default round
    res = default_round()

    # another round
    is_continue = does_player_continue_msg()

    is_reset = does_player_reset_msg()

    if is_reset:
        run_fresh_calc()

    while is_continue:
        new_num = check_input_num(round_number)
        round_number += 1

        oper = check_input_operation()

        res = oper(res, new_num)
        print("Result of operation: ", res)

        # czy koniec
        is_continue = does_player_continue_msg()
        if not is_continue:
            print("See u next time!")
            break

        # czy reset
        is_reset = does_player_reset_msg()
        if is_reset:
            run_fresh_calc()


operations = {
    "/": divide,
    "*": multiply,
    "+": add,
    "-": substract
}

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

if __name__ == "__main__":
    run_fresh_calc()
