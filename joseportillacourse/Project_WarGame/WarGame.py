"""Gra w wojne"""
import random

# zmienne globalne
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13,
          'Ace': 14}


class Card:
    """Klasa reprezentujaca karte w grze"""

    def __init__(self, suit, rank):
        """Inicjalizacja pol klasowych"""
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        """Reprezentacja naszej karty"""
        return str(self.rank) + " of " + str(self.suit)


class Deck:
    """Klasa reprezentujaca zestaw kart w talii"""

    def __init__(self):
        """Tworzenie decku"""

        self.deck_of_cards = []
        for suit in suits:
            for rank in ranks:
                self.deck_of_cards.append(Card(suit, rank))

    def __str__(self):
        return str(self.deck_of_cards)

    def shuffle(self):
        """Tasujemy kary"""
        random.shuffle(self.deck_of_cards)

    def deal_one(self):
        """Pobranie jednej karty z decku"""
        return self.deck_of_cards.pop()


class Player:
    """Klasa reprezentujaca deck gracza"""

    def __init__(self, nickname):
        self.nickname = nickname
        self.player_deck = []

    def remove_card(self):
        """Usuwanie karty z decku"""
        return self.player_deck.pop(0)

    def add_cards(self, new_cards):
        """Dodawanie karty do decku"""

        # 2+ cards
        if type(new_cards) is type([]):
            # Poprawny format karty
            for card in new_cards:
                if type(card) is not Card:
                    print("Niepoprawny input kart")
                    break
            else:
                # poprawny
                self.player_deck.extend(new_cards)
        else:
            if type(new_cards) is not Card:
                print("Niepoprawny input kart")
            else:
                # 1 card
                self.player_deck.append(new_cards)

    def __str__(self):
        return f"{self.nickname} has {len(self.player_deck)} cards."


class GameLogic:
    """Klasa odpowiadajaca za logike gry"""
    round = 1

    def __init__(self):
        self.p1 = Player("Player 1")
        self.p2 = Player("Player 2")

        self.deck = Deck()
        self.deck.shuffle()

    def split_cards(self):
        """Podzial kart z decku pomiedzy 2 graczy"""
        for _ in range(26):
            self.p1.add_cards(self.deck.deal_one())
        for _ in range(26):
            self.p2.add_cards(self.deck.deal_one())

    def play_game(self):
        """Symulacja rozgrywki"""

        # gra dopoki ktorys z graczy nie ma wyst ilosci kart
        game_on = True
        while game_on:
            # is -> porownuje miejsca w pamieci || != wartosci pod obiektami
            print("Round {}".format(GameLogic.round))
            GameLogic.round += 1

            if len(self.p1.player_deck) == 0:
                print("Player 2 won")
                break
            if len(self.p2.player_deck) == 0:
                print("Player 1 won")
                break

            # nowa runda

            p1_cards_round = [self.p1.remove_card()]
            p2_cards_round = [self.p2.remove_card()]

            at_war = True

            while at_war:
                # 1 gracz wygrywa
                if p1_cards_round[-1].value > p2_cards_round[-1].value:
                    self.p1.add_cards(p1_cards_round)
                    self.p1.add_cards(p2_cards_round)
                    print("p1 wins round {}".format(GameLogic.round))
                    at_war = False

                # 2 gracz wygrywa
                elif p1_cards_round[-1].value < p2_cards_round[-1].value:
                    self.p2.add_cards(p1_cards_round)
                    self.p2.add_cards(p2_cards_round)
                    print("p2 wins round {}".format(GameLogic.round))
                    at_war = False

                # wojna!
                else:
                    print("WARRRRR!")

                    # sprawdzenie czy gracza maja enough kart do wojny
                    if len(self.p1.player_deck) < 5:
                        print("Player 2 won!")
                        print("Player 1 not enough cards!")
                        game_on = False
                        break
                    if len(self.p2.player_deck) < 5:
                        print("Player 1 won!")
                        print("Player 2 not enough cards!")
                        game_on = False
                        break
                    # karty do dolu dla p1 i p2
                    for _ in range(5):
                        p1_cards_round.append(self.p1.remove_card())
                        p2_cards_round.append(self.p2.remove_card())


if __name__ == "__main__":
    # sprawdzenia

    gl = GameLogic()
    gl.split_cards()
    gl.play_game()

    # print(gl.p1.player_deck[0])
    # print(gl.p2.player_deck[0])
