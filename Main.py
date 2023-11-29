from copy import deepcopy
from random import shuffle
from Base import Player, valid_attack, valid_defense, show_hand

SUITS = ['♠', '♣', '♦', '♥']
RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DECK = [(rank, suit) for rank in RANKS for suit in SUITS]


def game():
    deck = deepcopy(DECK)
    shuffle(deck)
    trump_card = deck[-1]
    trump_suit = trump_card[1]
    print(f"Trump Suit is {trump_suit}")

    player1, player2 = Player('Player1'), Player('Player2')
    player1.replenish(deck)
    player2.replenish(deck)
    player1.sort_hand(trump_suit)
    player2.sort_hand(trump_suit)

    print(f"PLayer1's cards are {show_hand(player1.hand)}")
    print(f"PLayer2's cards are {show_hand(player2.hand)}")

    if player1.low_trump(trump_suit) < player2.low_trump(trump_suit):
        turn = player1
        other = player2
    elif player1.low_trump(trump_suit) > player2.low_trump(trump_suit):
        turn = player2
        other = player1
    else:
        print("No player has a trump card")
        return -1

    # Game begins
    while True:
        pile = list()

        while True:
            print(f"pile is {show_hand(pile)}")
            for card in turn.hand:
                if valid_attack(card, pile):
                    pile.append(turn.play_card(turn.hand[0]))
                    break
            else:
                turn, other = other, turn
                break

            for card in other.hand:
                if valid_defense(card, pile, trump_suit):
                    pile.append(other.play_card(card))
                    break
            else:
                other.take(pile)
                break

        pile.clear()

        print('turn over')

        if not player1.hand or not player2.hand:
            print('Player1:', show_hand(player1.hand))
            print('Player2:', show_hand(player2.hand))
            print('Game Over')
            return -1


game()