
"""
    This class is used to create a board for the game.
    The board contains the cards that are in the game.
"""

import random
import pygame
import os

from card import Card


YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


class Board:
    _xSpaceBetweenCards = 300  # space between cards on ox(in pixels)
    # space between cards on oy (when we place them on slots with the first faced forward and the others backwards)
    _ySpaceBetweenCards = 30
    _screen = None
    _cards = []  # deck of cards
    _cardSlots = []  # the 6 slots with cards
    _facedUpCards = []  # cards that have their face up

    """
        Returns the slot
    """

    def getSlot(self, slot):
        return self._cardSlots[slot]

    def printSlots(self):
        for i in range(0, 6):
            print("Slot " + str(i) + " " + str(len(self._cardSlots[i])))
            for card in self._cardSlots[i]:
                print(card)
            print("")

        print("------------------------------")

    """
        Returns the number of cards in the slot
    """

    def cardsInSlot(self, slot):
        return len(self._cardSlots[slot])

    """
        Swap the last card to let the player see it.
    """

    def reverseLastMove(self, slot):
        if len(self._cardSlots[slot]) > 1:
            self._cardSlots[slot][-2].setFaceUp(False)
        else:
            self._cardSlots[slot][-1].setFaceUp(False)

    """
        This method is used to put a card on the screen with the right allignment
    """

    def aproximatePositionCardToSlot(self, card, slotIndex):
        referencePosition = self._cardSlots[slotIndex][0].getPosition()
        if len(self._cardSlots[slotIndex]) <= 1:
            card.setPosition(referencePosition[0], referencePosition[1])
        else:
            card.setPosition(referencePosition[0], referencePosition[1] +
                             self._ySpaceBetweenCards * (len(self._cardSlots[slotIndex]) - 1))

    def isMoveValid(self, card, toSlot):
        previousCard = None
        if len(self._cardSlots[toSlot]):
            previousCard = self._cardSlots[toSlot][-1]

        if previousCard == None:
            return True
        if int(previousCard.getValue()) - int(card.getValue()) != 1 or previousCard.getColor() == card.getColor():
            return False
        return True

    """
        Place the card in the new slot
            - remove the card from the old slot
            - add the card to the new slot
    """

    def placeCardInSlot(self, fromSlot, toSlot, card):

        # # TODO: validate the move
        # # remove the card from the slot
        if toSlot != -1 and type(card) is Card:
            if card in self._cardSlots[fromSlot]:
                if len(self._cardSlots[fromSlot]) > 0:
                    self._cardSlots[fromSlot].remove(card)
                if len(self._cardSlots[fromSlot]) > 0 and fromSlot != toSlot:
                    self._cardSlots[fromSlot][-1].setFaceUp(True)
            # add the card to the slot
            self._cardSlots[toSlot].append(card)
            self.aproximatePositionCardToSlot(card, toSlot)

    """
        Setter method for the screen.
    """

    def setScreen(self, screen):
        self._screen = screen

    """
        Returns the index of the card in the slot
    """

    def getCardIndexInSlot(self, card, slot):
        return self._cardSlots[slot].index(card)

    """
        Check if the cards below are faced up and in the correct order according to the game
    """

    def checkCardsBelow(self, card, slot):
        for i in range(0, len(self._cardSlots[slot]) - 1):
            if self._cardSlots[slot][i] == card:
                for j in range(i+1, len(self._cardSlots[slot])):
                    card1 = self._cardSlots[slot][j-1]
                    card2 = self._cardSlots[slot][j]

                    if card1.isFacedUp() == False or card2.isFacedUp() == False or int(card1.getValue()) - int(card2.getValue()) != 1 or card1.getColor() == card2.getColor():
                        return False
                    else:
                        return True
        return True
    """
        Detect the selected card
    """

    def detectSelectedCard(self, x, y):
        # detect the slot position
        for i in range(0, 6):
            if x > self._xSpaceBetweenCards * i + 15 and x < self._xSpaceBetweenCards * i + 200:
                # TODO: see what card on OY is selected
                cardsInSlot = len(self._cardSlots[i])
                for j in range(0, cardsInSlot):
                    if y > self._ySpaceBetweenCards * j + 15 and y < self._ySpaceBetweenCards * (j + 1) + 15:
                        if self.checkCardsBelow(self._cardSlots[i][j], i) == True:
                            return self._cardSlots[i][j]
                # if we have at least a card in the slot
                if (self._cardSlots[i]):
                    # PUNE POP AICI ???? #nu tin minte ce face asta
                    return self._cardSlots[i][-1]
                return 0  # if the slot is empty
        return -1

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
        self._screen.fill((0, 0, 255))
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
            #print("Slot " + str(i))
            for index, card in enumerate(self._cardSlots[i]):
                if index < i:
                    faceUp = False
                else:
                    faceUp = True

                # place the card with the face up or down
                card.setFaceUp(faceUp)

                # set the position of the card inside the card object
                card.setPosition(self._xSpaceBetweenCards *
                                 i + 20, index * self._ySpaceBetweenCards + 20)
                card.calculateRect()
                # put the card on the screen
                self.putCard(card, self._xSpaceBetweenCards * i +
                             20, index * self._ySpaceBetweenCards + 20, faceUp)
                # print(card)
            # print("")

        # put the 4 empty slots on the screen

        # 1
        fakeCard = Card("img/heartSymbol.png", "red",
                        "0", "heart", faceUp=True)
        self.putCard(fakeCard, 50, 550)

        # 2
        fakeCard = Card("img/diamondSymbol.png", "red",
                        "0", "diamond", faceUp=True)
        self.putCard(fakeCard, 250, 550)

        # 3
        fakeCard = Card("img/spadeSymbol.png", "black",
                        "0", "spade", faceUp=True)
        self.putCard(fakeCard, 450, 550)

        # 4
        fakeCard = Card("img/clubSymbol.png", "black",
                        "0", "club", faceUp=True)
        self.putCard(fakeCard, 650, 550)

    def redrawBoard(self, movingCards, x, y):

        #self._screen.fill((0, 0, 255))

        for i in range(0, 6):
            #print("Slot " + str(i))
            for index, currentCard in enumerate(self._cardSlots[i]):
                # put on the board all the cards, except the selected one (the one that is being moved)
                if currentCard not in movingCards:
                    self.putCard(currentCard, currentCard.ox,
                                 currentCard.oy, currentCard.isFacedUp())

        myCards = list(movingCards)
        for i in range(len(myCards)):
            self.putCard(myCards[i], myCards[i].ox,
                         myCards[i].oy, myCards[i].isFacedUp())

        # self.putCard(card, card.ox,
        #              card.oy, card.isFacedUp())  # place the moving card for that frame on the board

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
        if card.isFacedUp():
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
            if card.getValue() == "0":
                div = 10
                if card.getSymbol() == "heart":
                    div = 8
                elif card.getSymbol() == "diamond":
                    div = 3
                elif card.getSymbol() == "spade":
                    div = 8
                elif card.getSymbol() == "club":
                    div = 8
                img = pygame.transform.scale(img, (width / div, height / div))
        else:
            img = pygame.transform.scale(img, (width / 6, height / 6))
        # pygame.display.update()
        self._screen.blit(img, (ox, oy))
