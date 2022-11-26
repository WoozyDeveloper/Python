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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(board.detectSlotPosition(pos[0], pos[1]))
