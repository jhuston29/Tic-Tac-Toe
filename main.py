import pygame
from GameOverMessage import PopUp

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define Variables
background_colour = WHITE
line_color = BLACK
x_color = BLACK
o_color = BLACK
size = 1000; # Game Board Size
square_dim = size/3;
gap = 0.05*size;
shape_size = 0.1*size;
line_thk = int(0.01*size);


# Define screen object
screen = pygame.display.set_mode((size, size))

# Set the caption of the screen
pygame.display.set_caption('Tic-Tac-Toe')

# Draw Game Board
def drawBoard():
    screen.fill(background_colour)
    hline1 = pygame.draw.line(screen, line_color, (gap, square_dim), (size-gap, square_dim), line_thk) # position (width, height)
    hline2 = pygame.draw.line(screen, line_color, (gap, square_dim*2), (size-gap, square_dim*2), line_thk) # position (width, height)
    vline1 = pygame.draw.line(screen, line_color, (square_dim, gap), (square_dim, size-gap), line_thk) # position (width, height)
    vline2 = pygame.draw.line(screen, line_color, (square_dim*2, gap), (square_dim*2, size-gap), line_thk) # position (width, height)
    # Update the display using flip
    pygame.display.flip()

# Switch Player Fucntion
def switch_player(player):
    if player == 1:
        return 2
    if player == 2:
        return 1

def get_BoxCenter(pos=(float('nan'), float('nan')), box=None):
    if pos[0] < size/3 and pos[1] < size/3 or box == 1: # Box 1
        center = (size/6, size/6)
        box = 1
        return center, box
    elif size/3 < pos[0] < 2*size/3 and pos[1] < size/3 or box == 2: # Box 2
        center = (3*size/6, size/6)
        box = 2
        return center, box
    elif pos[0] > 2*size/3 and pos[1] < size/3 or box == 3: # Box 3
        center = (5*size/6, size/6)
        box = 3
        return center, box
    elif pos[0] < size/3 and size/3 < pos[1] < 2*size/3 or box == 4: # Box 4
        center = (size/6, 3*size/6)
        box = 4
        return center, box
    elif size/3 < pos[0] < 2*size/3 and size/3 < pos[1] < 2*size/3 or box == 5: # Box 5
        center = (3*size/6, 3*size/6)
        box = 5
        return center, box
    elif pos[0] > size/3 and size/3 < pos[1] < 2*size/3 or box == 6: # Box 6
        center = (5*size/6, 3*size/6)
        box = 6
        return center, box
    elif pos[0] < size/3 and pos[1] > size/3 or box == 7: # Box 7
        center = (size/6, 5*size/6)
        box = 7
        return center, box
    elif size/3 < pos[0] < 2*size/3 and pos[1] > size/3 or box == 8: # Box 8
        center = (3*size/6, 5*size/6)
        box = 8
        return center, box
    elif pos[0] > size/3 and pos[1] > size/3 or box == 9: # Box 9
        center = (5*size/6, 5*size/6)
        box = 9
        return center, box

def drawX(center):
    x = center[0]
    y = center[1]
    pygame.draw.lines(screen, x_color, True, [(x-shape_size,y-shape_size),(x+shape_size,y+shape_size)], line_thk)
    pygame.draw.lines(screen, x_color, True, [(x-shape_size,y+shape_size),(x+shape_size,y-shape_size)], line_thk)
    pygame.display.flip()

def drawO(center):
    pygame.draw.circle(screen, o_color, center, shape_size, width=line_thk)
    pygame.display.flip()

def drawLine(start_box, end_box):
    start = get_BoxCenter(box=start_box)
    end = get_BoxCenter(box=end_box)
    start_x = start[0][0]
    start_y = start[0][1]
    end_x = end[0][0]
    end_y = end[0][1]
    if start_x == end_x:
        start_y = start_y - 0.1 * size
        end_y = end_y + 0.1 * size
    elif start_y == end_y:
        start_x = start_x - 0.1 * size
        end_x = end_x + 0.1 * size
    elif start_x < end_x:
        start_x = start_x - 0.1 * size
        end_x = end_x + 0.1 * size
        start_y = start_y - 0.1 * size
        end_y = end_y + 0.1 * size
    else:
        start_x = start_x + 0.1 * size
        end_x = end_x - 0.1 * size
        start_y = start_y - 0.1 * size
        end_y = end_y + 0.1 * size
    pygame.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), int(0.5*line_thk))
    pygame.display.flip()

def checkBoard(board):
    box1 = board[0][0]; box2 = board[0][1]; box3 = board[0][2];
    box4 = board[1][0]; box5 = board[1][1]; box6 = board[1][2];
    box7 = board[2][0]; box8 = board[2][1]; box9= board[2][2];
    if box1 == box2 == box3 != None:
        drawLine(1, 3)
        return True, True
    elif box4 == box5 == box6 != None:
        drawLine(4, 6)
        return True, True
    elif box7 == box8 == box9 != None:
        drawLine(7, 9)
        return True, True
    elif box1 == box4 == box7 != None:
        drawLine(1, 7)
        return True, True
    elif box2 == box5 == box8 != None:
        drawLine(2, 8)
        return True, True
    elif box3 == box6 == box9 != None:
        drawLine(3, 9)
        return True, True
    elif box1 == box5 == box9 != None:
        drawLine(1, 9)
        return True, True
    elif box3 == box5 == box7 != None:
        drawLine(3, 7)
        return True, True
    elif not any(box == None for row in board for box in row):
        return True, False
    else:
        return False, False

def checkSpace(player, box, board):
    if player == 1:
        shape = "X"
    elif player == 2:
        shape = "O"
    if box == 1:
        open = board[0][0]
        if open == None:
            board[0][0] = shape
            return True
    elif box == 2:
        open = board[0][1]
        if open == None:
            board[0][1] = shape
            return True
    elif box == 3:
        open = board[0][2]
        if open == None:
            board[0][2] = shape
            return True
    elif box == 4:
        open = board[1][0]
        if open == None:
            board[1][0] = shape
            return True
    elif box == 5:
        open = board[1][1]
        if open == None:
            board[1][1] = shape
            return True
    elif box == 6:
        open = board[1][2]
        if open == None:
            board[1][2] = shape
            return True
    elif box == 7:
        open = board[2][0]
        if open == None:
            board[2][0] = shape
            return True
    elif box == 8:
        open = board[2][1]
        if open == None:
            board[2][1] = shape
            return True
    elif box == 9:
        open = board[2][2]
        if open == None:
            board[2][2] = shape
            return True

def main():
    # Variable to keep our game loop running
    running = True
    player = 1 # Define Starting Player (Player 1 - X; Player 2 - O)
    game_over = False
    game_board = [[None, None, None],
                  [None, None, None],
                  [None, None, None]];
    drawBoard()
    # Game Loop
    while running:
        # for loop through the event queue
        for event in pygame.event.get():
            if not game_over:
                # Detect Mouse Click
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    center, box = get_BoxCenter(pos=pos)
                    open = checkSpace(player, box, game_board)
                    if open:
                        # print(box)
                        # print(game_board)
                        if player == 1:
                            drawX(center)
                           # print("X")
                        elif player == 2:
                            drawO(center)
                           # print("O")
                        game_over, winner = checkBoard(game_board)
                        if not game_over:
                            player = switch_player(player)
                    else:
                        print("Spot is already Filled. Try Again.")
                if game_over:
                    # print("GAME OVER")
                    popupW = 0.5*size
                    popupH = 0.25*size
                    if not winner:
                        text = f"Tie Game."
                    else:
                        text = f"Player {player} Wins!"
                    popup = PopUp(text, x=size/2-popupW/2, y=size/2-popupH/2, width=popupW, height=popupH)
                    popup.draw(screen)
                    pygame.display.update()
            else:
                done = popup.handle_event(event)
                if not done and done is not None:
                    game_over, game_board = restart()
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

def restart():
    game_over = False
    game_board = [[None, None, None],
                  [None, None, None],
                  [None, None, None]];
    screen.fill(BLACK)
    pygame.display.flip()
    drawBoard()
    return game_over, game_board


if __name__ == '__main__':
    main()
