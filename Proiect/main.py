import pygame

from card import Card
from board import Board

pygame.init()
pygame.display.set_caption('Solitaire')

(width, height) = (1920, 1080)
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
                print(card)

                if card != -1:
                    rectangle_draging = True

        # releasing the card
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                droppedAt = board.detectSlotPosition(pos[0], pos[1])
                if card != (0, 0) and rectangle_draging:
                    board.placeCardInSlot(takenFrom, droppedAt, card)
                    screen.fill((0, 0, 0))
                    board.redrawBoard(card, pos[0], pos[1])
                    print("GATA STOP")
                    print(droppedAt)
                    print("GATA STOP")

                rectangle_draging = False

        # moving the card
        if event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                if card != (0, 0):
                    card.setPosition(pos[0], pos[1])
                    screen.fill((0, 0, 0))
                    board.redrawBoard(card, pos[0], pos[1])

    pygame.display.flip()
    # update the screen
    # if card != (0, 0) and rectangle_draging:

    # constant frame rate
    clock = pygame.time.Clock()
    clock.tick(60)
