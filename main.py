import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.suit + ' ' + self.value


class Deck:
    def __init__(self, cards_per_suit):
        self.suites = ['heart', 'diamond', 'spades', 'clubs']
        self.pack = [Card(suit, value) for value in range(1, cards_per_suit) for suit in self.suites]

    def shuffle(self):
        random.shuffle(self.pack)

    def get_cards(self, quantity):
        iteration = 1
        length = len(self.pack)
        while iteration <= quantity:
            yield self.pack[length - iteration]
            del self.pack[length - iteration]
            iteration += 1

    def __str__(self):
        return self.pack


class Hand:
    def __init__(self, cards_per_hand, deck):
        self.cards = [card for card in deck.get_cards(cards_per_hand)]

    def get_value(self):
        return sum([card.value for card in self.cards])


class Player:
    def __init__(self, name, deck, coin_set):
        self.has_big_blind = False
        self.has_small_blind = False
        self.name = name
        self.hand = Hand(5, deck)
        self.coin_set = coin_set

    def __str__(self):
        return self.name

    def get_hand(self):
        return self.hand

    def ask_for_fold(self):
        return input(self.name + ', do you want to fold?')


class Game:
    coin_set = {
        '10': 20,
        '25': 8,
        '50': 4,
        '100': 2,
        '200': 1
    }
    def __init__(self):
        self.deck = Deck(14)
        self.dealed_cards = None
        self.deck.shuffle()
        self.num_of_players = int(input('Number of players: '))
        self.names = []
        iteration = 0
        while iteration < self.num_of_players:
            self.names.append(input('Name of Player ' + str((iteration + 1)) + ': '))
            iteration += 1

        self.players = [Player(name, self.deck, self.coin_set) for name in self.names]

    def shuffle_players(self):
        random.shuffle(self.players)

    def deal_initial_cards(self):
        self.dealed_cards = [card for card in self.deck.get_cards(3)]

    def start(self):
        self.shuffle_players()
        currently_active = self.players
        self.deal_initial_cards()
        while len(currently_active) > 1:
            for player in currently_active:
                print(player.get_hand().cards)
                if player.ask_for_fold() == 'Y':
                    currently_active.remove(player)






if __name__ == '__main__':
    game = Game()
    game.start()
    print(game.dealed_cards)
