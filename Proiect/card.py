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

    def getSymbol(self):
        return self._symbol

    """
        Getter for the color
        
        Args:
            no arguments
        Returns:
            returns the color of the card
    """

    def getColor(self):
        return self._color

    """
        Getter for the value of the card

        Args:
            no arguments
        Returns:
            returns the value of the card
    """

    def getValue(self):
        return self._value

    """
        Getter for the position of the card.
        
        Args:
            no arguments
        Returns:
            returns a tuple (x,y) representing the position on the screen of the card
    """

    def getPosition(self):
        return (self.ox, self.oy)

    """
        Getter to see if the card is faced up or not

        Args:
            no arguments
        Returns:
            returns True if the card is faced up, False otherwise
    """

    def isFacedUp(self):
        return self._faceUp

    """
        Set the card faced up or faced down.

        Args:
            faceUp - value that needs to be set to the card
        Returns:
            void
    """

    def setFaceUp(self, faceUp):
        self._faceUp = faceUp

    """
        Draw the card on the screen.

        Args:
            no arguments
        Returns:
            void
    """

    def draw(self):
        self._screen.blit(self._imageLoad, (self.ox, self.oy))

    """
        Getter for the rectangle of the card.

        Args:
            no arguments
        Returns:
            returns the rectangle that represents the card
    """

    def getRect(self):
        return self._rect

    """
        Create a rect around the card

        Args:
            no arguments
        Returns:
            void
    """

    def calculateRect(self):
        #self._rect = self._imageLoad.get_rect()
        self._rect = pygame.rect.Rect(self.ox - 484 / (6 * 2), self.oy - 670 /
                                      (6 * 2), self.ox + 484 / (6 * 2), self.oy + 670 / (6 * 2))

    """
        Set the position of the card.

        Args:
            x: ox position on the screen
            y: oy position on the screen
        Returns:
            void
    """

    def setPosition(self, x, y):
        self.ox = x
        self.oy = y

    """
        Constructor

        Args:
            picture: path to the picture of the card
            color: color of the card
            value: value of the card
            symbol: symbol of the card
            faceUp: boolean value that sets the card faced up or down
        Returns:
            void
    """

    def __init__(self, picture, color, value, symbol, faceUp=False):
        # print(picture)
        self._picture = picture
        self._imageLoad = pygame.image.load(picture).convert_alpha()
        self._color = color
        self._value = value
        self._symbol = symbol
        self._faceUp = faceUp

    """
        Getter for the picture

        Args:
            no arguments
        Returns:
            returns the picture of the card
    """

    def getPicture(self):
        return self._picture

    """
        For print

        Args:
            no arguments
        Returns:
            returns a string with information about the card (value, color, symbol, rectangle)
    """

    def __str__(self):
        return self._value + " of " + self._color + " " + self._symbol + " rect --> " + str(self._rect)
