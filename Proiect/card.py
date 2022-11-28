import pygame
"""
    A class that represents a card.
"""


class Card:
    ox = 0  # ox position of the card on ox axis
    oy = 0  # oy position of the card on oy axis
    _picture = None  # picture of the card
    _imageLoad = None
    _color = None  # color of the card
    _value = None  # value of the card
    _symbol = None  # symbol of the card
    _rect = None  # rectangle of the card
    _faceUp = False  # if the card is faced up or not

    def setFaceUp(self, faceUp):
        self._faceUp = faceUp

    """
        Draw the card on the screen.
    """

    def draw(self):
        self._screen.blit(self._imageLoad, (self.ox, self.oy))

    """
        Getter for the rectangle of the card.
    """

    def getRect(self):
        return self._rect

    """
        Create a rect around the card
    """

    def calculateRect(self):
        print('INTRU')
        #self._rect = self._imageLoad.get_rect()
        self._rect = pygame.rect.Rect(self.ox - 484 / (6 * 2), self.oy - 670 /
                                      (6 * 2), self.ox + 484 / (6 * 2), self.oy + 670 / (6 * 2))

    """
        Set the position of the card.
    """

    def setPosition(self, x, y):
        self.ox = x
        self.oy = y

    """
        Constructor
    """

    def __init__(self, picture, color, value, symbol, faceUp=False):
        print(picture)
        self._picture = picture
        self._imageLoad = pygame.image.load(picture)
        self._color = color
        self._value = value
        self._symbol = symbol
        self._faceUp = faceUp

    """
        Getter for the picture
    """

    def getPicture(self):
        return self._picture

    """
        For print
    """

    def __str__(self):
        return self._value + " of " + self._color + " " + self._symbol + " rect --> " + str(self._rect)
