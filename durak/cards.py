'''
This list will contain a list of mappings from suit to card.
'''
from methods import DurakCards 

def card_mappings():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

    cards = [DurakCards(suit, card) for suit in suits for card in ranks]

    return cards 

print(card_mappings())
