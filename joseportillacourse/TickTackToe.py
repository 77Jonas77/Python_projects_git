BOARD = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' '
]

ROUND = 1
P1_SIGN = ""
P2_SIGN = ""


def print_board():
    """ Wyswietla aktualny stan planszy """
    print(f"== RUNDA {ROUND} ==", '\n' * 2)
    print(f" {BOARD[0]} | {BOARD[1]} | {BOARD[2]} ")
    print(f"-----------")
    print(f" {BOARD[3]} | {BOARD[4]} | {BOARD[5]} ")
    print(f"-----------")
    print(f" {BOARD[6]} | {BOARD[7]} | {BOARD[8]} ")
    print('\n' * 2)


def reset_game():
    print_board()
    global BOARD, ROUND, P1_SIGN, P2_SIGN
    BOARD = [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' '
    ]
    ROUND = 1
    P1_SIGN = ""
    P2_SIGN = ""


def hello_msg():
    """ Wyswietla przywitanie w grze """
    print("======TIC TAC TOE GAME!======\n      Good luck have fun", '\n' * 3)


def sign_choice():
    """ Metoda odpowiadajaca za wybor znaku przez gracza """
    choice = 'WRONG'

    while choice.lower() != 'x' and choice.lower() != 'o':  # sprawdzenie popr input
        choice = input("Choose your sign: ")

        if choice.lower() != 'x' and choice.lower() != 'o':
            print("Invalid sign chosen!\n")
    global P1_SIGN, P2_SIGN

    if choice.lower() == 'x':
        P1_SIGN = 'X'
        P2_SIGN = 'O'
    else:
        P1_SIGN = 'O'
        P2_SIGN = 'X'


def input_position():
    """
     Odpowiada za wczytanie pozycji od gracza
     pozycje -> od gory 1...9 kolejno na planszy
    """
    position = " "
    while not position.isdigit():
        position = input(
            f'Type position PLAYER {1 if ROUND % 2 == 1 else 2} (1-9): '
        )

    position = int(position)
    # wprowadzenie pozycji dla danego gracza i spr poprawnosci
    while ((position < 1 or position > 9)
           or (BOARD[position - 1] == 'X' or BOARD[position - 1] == 'O')):

        position = int(input(
            f'Type position PLAYER {1 if ROUND % 2 == 1 else 2} (1-9): ')
        )

        if position < 1 or position > 9:
            print("Position out of range!")
        if BOARD[position - 1] != ' ':
            print("Already MARKED!")
    print('\n'*2)
    return position


def check_play_again():
    """ Pyta uzytkownika o to czy chce zagrac jeszcze raz """
    choice = 'WRONG'

    while choice.lower() != 'yes' and choice.lower() != 'no':  # sprawdzenie popr input
        choice = input("Do you want to play again? (yes/no) : ")

        if choice != 'yes' and choice != 'no':
            print("Invalid answer!\n")

    return False if choice.lower() == 'no' else True


def check_win():
    """ Sprawdza w każdej rundzie, czy gra została wygrana """
    # Sprawdzenie poziomych linii
    for i in range(0, 9, 3):
        if BOARD[i] == BOARD[i + 1] == BOARD[i + 2] != ' ':
            print(
                f'Player {1 if BOARD[i] == P1_SIGN else 2} wins!')
            reset_game()
            return True

    # Sprawdzenie pionowych linii
    for i in range(3):
        if BOARD[i] == BOARD[i + 3] == BOARD[i + 6] != ' ':
            print(f'Player {1 if BOARD[i] == P1_SIGN else 2} wins!')
            reset_game()
            return True

    # Sprawdzenie przekątnych
    if BOARD[0] == BOARD[4] == BOARD[8] != ' ':
        print(f'Player {1 if BOARD[0] == P1_SIGN else 2} wins!')
        reset_game()
        return True
    if BOARD[2] == BOARD[4] == BOARD[6] != ' ':
        print(f'Player {1 if BOARD[2] == P1_SIGN else 2} wins!')
        reset_game()
        return True

    # Sprawdzenie remisu
    if ' ' not in BOARD:
        print("It's a tie!")
        reset_game()
        return True

    return False  # Jeśli żaden warunek nie został spełniony, gra trwa dalej


def make_move(pos):
    """ Odpowiada za wykonanie ruchu w tablicy """
    global BOARD
    if ROUND % 2 == 1:
        BOARD[pos - 1] = P1_SIGN
    else:
        BOARD[pos - 1] = P2_SIGN


def first_round():
    global ROUND
    hello_msg()

    # 1 runda
    print_board()
    sign_choice()
    make_move(input_position())
    ROUND += 1


def one_plus_round():
    """ Odpowiada za rundy 1+ """
    global ROUND

    # roundy do momentu wygranej
    while not check_win():
        print_board()
        make_move(input_position())
        ROUND += 1


def play_game():
    """Logika gry"""

    global ROUND

    # first game
    first_round()
    one_plus_round()

    # if players want to play more
    while check_play_again():
        first_round()
        one_plus_round()
    else:
        print("Thank you for playing! See you next time!")


play_game()
