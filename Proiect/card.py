"""
    A class that represents a card.
"""


class Card:

    _picture = None  # picture of the card
    _color = None  # color of the card
    _value = None  # value of the card
    _symbol = None  # symbol of the card

    """
        Constructor
    """

    def __init__(self, picture, color, value, symbol):
        self._picture = picture
        self._color = color
        self._value = value
        self._symbol = symbol

    """
        Getter for the picture
    """

    def getPicture(self):
        return self._picture

    """
        For print
    """

    def __str__(self):
        return self._value + " of " + self._color + " " + self._symbol
