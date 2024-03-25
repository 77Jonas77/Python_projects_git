"""Gra w kolko i krzyzyk"""

board = [
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
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print('\n' * 2)


def reset_game():
    """ Resetuje statystyki gry """
    print_board()
    global board, ROUND, P1_SIGN, P2_SIGN
    board = [
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
           or (board[position - 1] == 'X' or board[position - 1] == 'O')):

        position = int(input(
            f'Type position PLAYER {1 if ROUND % 2 == 1 else 2} (1-9): ')
        )

        if position < 1 or position > 9:
            print("Position out of range!")
        if board[position - 1] != ' ':
            print("Already MARKED!")
    print('\n'*2)
    return position


def check_play_again():
    """ Pyta uzytkownika o to czy chce zagrac jeszcze raz """
    choice = 'WRONG'

    while choice.lower() != 'yes' and choice.lower() != 'no':  # sprawdzenie popr input
        choice = input("Do you want to play again? (yes/no) : ")

        if choice in ('yes', 'no'):
            print("Invalid answer!\n")

    return False if choice.lower() == 'no' else True


def check_win():
    """ Sprawdza w każdej rundzie, czy gra została wygrana """
    # Sprawdzenie poziomych linii
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            print(
                f'Player {1 if board[i] == P1_SIGN else 2} wins!')
            reset_game()
            return True

    # Sprawdzenie pionowych linii
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            print(f'Player {1 if board[i] == P1_SIGN else 2} wins!')
            reset_game()
            return True

    # Sprawdzenie przekątnych
    if board[0] == board[4] == board[8] != ' ':
        print(f'Player {1 if board[0] == P1_SIGN else 2} wins!')
        reset_game()
        return True
    if board[2] == board[4] == board[6] != ' ':
        print(f'Player {1 if board[2] == P1_SIGN else 2} wins!')
        reset_game()
        return True

    # Sprawdzenie remisu
    if ' ' not in board:
        print("It's a tie!")
        reset_game()
        return True

    return False  # Jeśli żaden warunek nie został spełniony, gra trwa dalej


def make_move(pos):
    """ Odpowiada za wykonanie ruchu w tablicy """
    if ROUND % 2 == 1:
        board[pos - 1] = P1_SIGN
    else:
        board[pos - 1] = P2_SIGN


def first_round():
    """Przebieg 1. rundy"""
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
