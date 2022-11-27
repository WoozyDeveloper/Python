import pygame
from card import Card
from board import Board

pygame.init()
pygame.display.set_caption('Solitaire')

(width, height) = (1920, 1080)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

running = True

board = Board()
board.setScreen(screen)
board.loadCards()
# board.printDeck()
board.shuffleDeck()
board.prepareBoard()

rectangle_draging = False
rectangle = (0, 0)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                print(board.detectSelectedCard(pos[0], pos[1]))
                rectangle = board.detectSelectedCard(pos[0], pos[1])
                rectangle.calculateRect()
                print(rectangle.getRect())
                print((rectangle))
                if rectangle.getRect().collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.ox - mouse_x
                    offset_y = rectangle.oy - mouse_y

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_draging = False

        if event.type == pygame.MOUSEMOTION:
            print("FAC DRAGGING")
            if rectangle_draging:
                rectangle.getRect().move_ip(event.rel)
                if rectangle != (0, 0):
                    rectangle.setPosition(event.rel[0], event.rel[1])

        board.redrawBoard()

        pygame.display.update()
