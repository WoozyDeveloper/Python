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
board.shuffleDeck()
board.prepareBoard()

rectangle_draging = False
card = (0, 0)
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # grabbing the card
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                card = board.detectSelectedCard(pos[0], pos[1])
                print(card)

                if card != -1:
                    card.calculateRect()
                    if card.getRect().collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = card.ox - mouse_x
                        offset_y = card.oy - mouse_y

        # releasing the card
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("GATA STOP")
                rectangle_draging = False

        # moving the card
        if event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                card.getRect().move_ip(pos)
                if card != (0, 0):
                    card.setPosition(pos[0], pos[1])

        # update the screen
        if card != (0, 0) and rectangle_draging:
            screen.fill((0, 0, 0))
            board.redrawBoard(card, pos[0], pos[1])
            pygame.display.update()

        # constant frame rate
        clock = pygame.time.Clock()
        clock.tick(120)
