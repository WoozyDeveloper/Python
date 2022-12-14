import pygame

from card import Card
from board import Board

pygame.init()
pygame.display.set_caption('Solitaire')

(width, height) = (1600, 700)
screen = pygame.display.set_mode((width, height))

running = True

board = Board()
board.setScreen(screen)
board.loadCards()
print('scriu')
board.printDeck()
print('scri2222u')

board.shuffleDeck()  # shuffle the deck
board.prepareBoard()  # prepare the board by placing the cards

rectangle_draging = False  # True if the user is dragging a card
card = (0, 0)  # here we store the card that is being moved

takenFrom = -1  # variable that remembers the slot from which the card was taken
# variable that remembers the initial position of the card
initialCardPosition = (0, 0)
previousCard = None
movingCards = set()  # set of cards that are being moved

while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # grabbing the card
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                movingCards.clear()
                takenFrom = board.detectSlotPosition(pos[0], pos[1])
                if takenFrom == 10:  # click lonely card
                    print("TAP ON LONELY CARD!!!")
                    card = board.getFakeCard()
                    board.goToNextCard()
                    rectangle_draging = True
                if True:
                    card = board.detectSelectedCard(pos[0], pos[1])
                    #print("carrrd=", card)
                    if card != -1 and card != board.getFakeCard():
                        if len(board.getSlot(takenFrom)) > 1:
                            previousCard = board.getSlot(takenFrom)[-2]
                        #print('PREVIOUS CARD', previousCard)
                        if type(card) is Card:
                            initialCardPosition = card.getPosition()

                    if type(card) is Card:
                        rectangle_draging = True
                #screen.fill((0, 0, 255))
                # pygame.display.flip()
                board.redrawBoard(movingCards, pos[0], pos[1])

        # releasing the card
        if event.type == pygame.MOUSEBUTTONUP:
            # TODO multiple card bug
            if event.button == 1 and type(card) is Card:

                droppedAt = board.detectSlotPosition(pos[0], pos[1])
                if not board.isMoveValid(card, droppedAt):
                    droppedAt = -1
                # if the card is placed in a valid position (slot)
                if card != (0, 0) and rectangle_draging and droppedAt != -1:
                    if droppedAt < 6:
                        currentSlot = board.getSlot(droppedAt)

                        board.placeCardInSlot(takenFrom, droppedAt, card)
                        for c in movingCards:
                            board.placeCardInSlot(takenFrom, droppedAt, c)
                    else:
                        board.placeCardInFinalSlot(takenFrom, droppedAt, card)
                    # refresh the screen
                    screen.fill((0, 0, 255))
                    board.redrawBoard(movingCards, pos[0], pos[1])

                else:
                    card.setPosition(
                        initialCardPosition[0], initialCardPosition[1])

                    for i in range(0, len(currentSlot) - 1):
                        if currentSlot[i] == card:
                            for j in range(i, len(currentSlot)):
                                print(j)
                                currentSlot[j].setPosition(
                                    initialCardPosition[0], initialCardPosition[1] + 20 * (j - i))
                    # refresh the screen

                screen.fill((0, 0, 255))
                board.redrawBoard(
                    movingCards, initialCardPosition[0], initialCardPosition[1])
                board.printSlots()
                rectangle_draging = False
                board.printDeck()

        # moving the card
        if event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                if type(card) is Card and takenFrom != 10:
                    #print("DAU DRAG")
                    currentSlot = board.getSlot(takenFrom)
                    card.setPosition(pos[0], pos[1])
                    for i in range(0, len(currentSlot) - 1):
                        if currentSlot[i] == card:
                            for j in range(i+1, len(currentSlot)):
                                # print(j)
                                currentSlot[j].setPosition(
                                    pos[0], pos[1] + 20 * (j - i + 1))
                                movingCards.add(currentSlot[j])

                    screen.fill((0, 0, 255))
                    board.redrawBoard(movingCards, pos[0], pos[1])
                elif type(card) is Card and card == board.getFakeCard():
                    # board.goToNextCard()
                    print(card)
                    card.setPosition(pos[0], pos[1])
                    #board.getFakeCard().setPosition(pos[0], pos[1])
                    screen.fill((0, 0, 255))
                    board.redrawBoard(card, pos[0], pos[1])

    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(60)
