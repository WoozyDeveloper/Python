
"""
    This class is used to create a board for the game.
    The board contains the cards that are in the game.
"""

import random
import pygame
import os

from card import Card


class Board:
    _xSpaceBetweenCards = 300  # space between cards on ox(in pixels)
    # space between cards on oy (when we place them on slots with the first faced forward and the others backwards)
    _ySpaceBetweenCards = 30
    _screen = None
    _cards = []  # deck of cards
    _cardSlots = []  # the 6 slots with cards

    """
        Setter method for the screen.
    """

    def setScreen(self, screen):
        self._screen = screen

    """
        Detect on which slot the card goes based on its position
    """

    def detectSlotPosition(self, x, y):
        # detect the slot position
        for i in range(0, 6):
            if x > self._xSpaceBetweenCards * i + 15 and x < self._xSpaceBetweenCards * i + 200 and y > 15 and y < self._screen.get_rect().height / 2:
                return i
        return -1

    """
        Load all the cards from the img folder into a deck.
        In each card object put the corresponding picture, color, value and symbol based on the name of the file.
    """

    def loadCards(self):
        # go through all the files in the img folder
        for file in os.listdir("img"):
            if file.endswith(".svg"):  # file is a .svg
                # get information from the name of the file
                cardSymbol = file.split("-")[0].lower()
                cardValue = file.split("-")[1].split(".")[0]

                # get the color of the card based on the symbol
                if cardSymbol == 'club' or cardSymbol == 'spade':
                    cardColor = 'black'
                else:
                    cardColor = 'red'

                # create a card object
                card = Card("img/" + file, cardColor, cardValue, cardSymbol)

                # add the card to the deck
                self._cards.append(card)

    """
        Shuffle the deck of cards.
    """

    def shuffleDeck(self):
        # shuffle the deck of cards
        random.shuffle(self._cards)

    """
        ceva print cu ce face prepareBoard
    """

    def prepareBoard(self):
        # create the card slots
        self._cardSlots = []
        for i in range(0, 6):
            self._cardSlots.append([])

        # put the cards in the card slots
        for i in range(0, 6):
            for j in range(0, i + 1):
                self._cardSlots[i].append(self._cards.pop())

        # print card slots and put the cards on the screen
        for i in range(0, 6):
            print("Slot " + str(i))
            for index, card in enumerate(self._cardSlots[i]):
                if index < i:
                    faceUp = False
                else:
                    faceUp = True
                self.putCard(card, self._xSpaceBetweenCards * i +
                             20, index * self._ySpaceBetweenCards + 20, faceUp)
                print(card)
            print("")

    """
        Print all the cards in the deck.
    """

    def printDeck(self):
        for card in self._cards:
            print(card)
        print("Total cards: " + str(len(self._cards)))

    """
        Place a card on the board on (ox, oy).
        A slot is a place where the player can place a card.
    """

    def putCard(self, card, ox, oy, faceUp=True):
        # load the image
        card = card

        # if the card is face up, we get the image of the card
        if faceUp:
            cardImage = card.getPicture()
        else:
            # else we print the back of the card
            cardImage = "img/BACK.png"
        img = pygame.image.load(cardImage)

        # resize the image
        width = img.get_rect().width
        height = img.get_rect().height
        if faceUp:
            img = pygame.transform.scale(img, (width / 3, height / 3))
        else:
            img = pygame.transform.scale(img, (width / 6, height / 6))

        self._screen.blit(img, (ox, oy))
        pygame.display.update()
