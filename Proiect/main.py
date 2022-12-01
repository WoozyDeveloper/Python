import pygame

from card import Card
from board import Board

pygame.init()
pygame.display.set_caption('Solitaire')

(width, height) = (1800, 900)
screen = pygame.display.set_mode((width, height))

running = True

board = Board()
board.setScreen(screen)
board.loadCards()
# board.printDeck()

board.shuffleDeck()  # shuffle the deck
board.prepareBoard()  # prepare the board by placing the cards

rectangle_draging = False  # True if the user is dragging a card
card = (0, 0)  # here we store the card that is being moved

takenFrom = -1  # variable that remembers the slot from which the card was taken
# variable that remembers the initial position of the card
initialCardPosition = (0, 0)
previousCard = None
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # grabbing the card
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                takenFrom = board.detectSlotPosition(pos[0], pos[1])
                card = board.detectSelectedCard(pos[0], pos[1])
                if len(board.getSlot(takenFrom)) > 1:
                    previousCard = board.getSlot(takenFrom)[-2]
                print('PREVIOUS CARD', previousCard)
                if type(card) is Card:
                    initialCardPosition = card.getPosition()
                print(card)

                if type(card) is Card:
                    rectangle_draging = True

        # releasing the card
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and type(card) is Card:

                droppedAt = board.detectSlotPosition(pos[0], pos[1])
                if not board.isMoveValid(card, droppedAt):
                    droppedAt = -1
                    # if the card is placed in a valid position (slot)
                if card != (0, 0) and rectangle_draging and droppedAt != -1:
                    board.placeCardInSlot(takenFrom, droppedAt, card)
                    screen.fill((0, 0, 0))
                    board.redrawBoard(card, pos[0], pos[1])

                else:  # if the card is placed in a non-valid position (slot)
                    if board.cardsInSlot(takenFrom) > 1:
                        currentSlot = board.getSlot(takenFrom)
                        board.placeCardInSlot(takenFrom, takenFrom, card)
                        if previousCard.isFacedUp() == False:
                            board.reverseLastMove(takenFrom)
                    else:
                        card.setPosition(
                            initialCardPosition[0], initialCardPosition[1])

                        board.placeCardInSlot(takenFrom, takenFrom, card)
                    screen.fill((0, 0, 0))
                    board.redrawBoard(
                        card, initialCardPosition[0], initialCardPosition[1])

                board.printSlots()
                rectangle_draging = False

        # moving the card
        if event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                if type(card) is Card:
                    card.setPosition(pos[0], pos[1])
                    screen.fill((0, 0, 0))
                    board.redrawBoard(card, pos[0], pos[1])

    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60)
