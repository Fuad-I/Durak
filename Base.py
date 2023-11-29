RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = list()
        self.memory = {}
        self.turn = False

    def show_hand(self):
        return [f"{card[0]}{card[1]}" for card in self.hand]

    def take(self, pile):
        self.hand.extend(pile)
        print(f"{self.name} takes {', '.join([f'{card[0]}{card[1]}' for card in pile])}")

    def play_card(self, card):
        print(f"{self.name} played {card[0]}{card[1]}")
        self.hand.remove(card)
        return card

    def replenish(self, deck):
        while deck and len(self.hand) < 6:
            self.hand.append(deck.pop(0))

    def low_trump(self, trump_suit):
        temp = [card[0] for card in self.hand if card[1] == trump_suit]
        if temp:
            return min(temp)
        return 15

    def sort_hand(self, trump_suit):
        temp1, temp2 = list(), list()
        self.hand.sort()
        for card in self.hand:
            if card[1] == trump_suit:
                temp1.append(card)
            else:
                temp2.append(card)
        self.hand.clear()
        self.hand.extend(temp2)
        self.hand.extend(temp1)


def valid_defense(card, pile, trump_suit):
    last_card = pile[-1]
    if last_card[1] == card[1] and RANKS.index(card[0]) > RANKS.index(last_card[0]):
        return True
    if card[1] == trump_suit and last_card[1] != trump_suit:
        return True
    return False


def valid_attack(card, pile):
    if not pile:
        return True
    if card[0] in (item[0] for item in pile):
        return True
    return False


def show_cards(lst):
    return ', '.join([f"{card[0]}{card[1]}" for card in lst])


def get_rank(card):
    return RANKS.index(card)
