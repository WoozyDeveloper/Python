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
card = (0, 0)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                print(board.detectSelectedCard(pos[0], pos[1]))
                card = board.detectSelectedCard(pos[0], pos[1])
                if card != -1:
                    card.calculateRect()
                    if card.getRect().collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = card.ox - mouse_x
                        offset_y = card.oy - mouse_y

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("GATA STOP")
                rectangle_draging = False

        if event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                card.getRect().move_ip(event.rel)
                if card != (0, 0):
                    card.setPosition(event.rel[0], event.rel[1])
                    pos = pygame.mouse.get_pos()
                    board.redrawBoard(card, pos[0], pos[1])
        pygame.display.update()

        clock = pygame.time.Clock()
        clock.tick(60)
