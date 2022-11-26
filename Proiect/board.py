import pygame
import os

from card import Card

"""
    This class is used to create a board for the game.
    The board contains the cards that are in the game.
"""


class Board:
    _screen = None
    _cards = None
    _cardSlots = None  # the 6 slots with cards

    def __init__(self, cards):
        self._cards = cards

    """
        Setter method for the screen.
    """

    def setScreen(self, screen):
        self._screen = screen

    """
        Load all the cards from the img folder into a deck.
    """

    def loadCards(self):
        for file in os.listdir("img"):
            if file.endswith(".svg"):
                cardSymbol = file.split("-")[0].lower()
                cardValue = file.split("-")[1].split(".")[0]
                if cardSymbol == 'CLUB' or cardSymbol == 'SPADE':
                    cardColor = 'black'
                else:
                    cardColor = 'red'

                card = Card("img/" + file, cardColor, cardValue, cardSymbol)
                self._cards.append(card)

    """
        Place a card on the board.
    """

    def putCard(self):
        card = self._cards[0]
        cardImage = card.getPicture()
        img = pygame.image.load(cardImage)

        width = img.get_rect().width
        height = img.get_rect().height
        img = pygame.transform.scale(img, (width / 3, height / 3))

        self._screen.blit(img, (0, 0))
        pygame.display.update()
