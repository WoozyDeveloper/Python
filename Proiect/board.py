
"""
    This class is used to create a board for the game.
    The board contains the cards that are in the game.
"""

import pygame
import os

from card import Card


class Board:
    _screen = None
    _cards = []
    _cardSlots = None  # the 6 slots with cards

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

    def printDeck(self):
        for card in self._cards:
            print(card)

    """
        Place a card on the board on the selected slot.
        A slot is a place where the player can place a card.
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
