# import pygame  # make sure you pip3 install pygame
# import sys

   
# def main():
#     gameLoop()
        
    
# def processGridClick(row,column):
#     #
#     # This function is invoked whenever the user clicks on a square in the 3x3 
#     # Tic Tac Toe grid. 
#     #
#     # Parameters:
#     #    row:    the 0 based row # of the square clicked on 
#     #    column: the 0 based column # of the square clicked on 
#     # 
#     print(f"Grid coordinates ({row},{column}) were clicked")

#     #
#     # Using a 2 dimensional list, if the row,column square hasn't been clicked before, 
#     # then your code should use the draw_x_o() function to set the square to either an X or O
#     #
    

# def check_for_winner():
#     #
#     # This function (which you need to write) checks to see if there is a game winner or tie game.
#     # It is invoked after processGridClick() returns, after each mouse click
#     #
#     #
#     # If there is a winner, it must set the winner global variable to either "X" or "O"
#     # If there is a tie game, it must the winner global variable to "Tie Game"
#     # If there is no winnner / tie yet, leave the winner variable set to "None"
#     #

#     global winner
#     winner = None
import pygame
import sys

def main():
    gameLoop()
    
LINE_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE
xo_grid = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
screen = None
winner = None

def processGridClick(row, column):
    global xo_grid
    global winner
    if xo_grid[row][column] == '' and winner is None:
        xo_grid[row][column] = 'X'  
        draw_x_o(row, column, 'X')  
        check_for_winner()
        if winner is None:
            O()

def O():
    global xo_grid
    global winner
    if winner is None:
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if xo_grid[i][j] == '':
                    xo_grid[i][j] = 'O'
                    draw_x_o(i, j, 'O')  # Draws O on the screen if I'm not mistaken
                    check_for_winner()
                    return

def check_for_winner():
    global winner
    for i in range(BOARD_SIZE):
        if xo_grid[i][0] == xo_grid[i][1] == xo_grid[i][2] != '':
            winner = xo_grid[i][0]
            return
        if xo_grid[0][i] == xo_grid[1][i] == xo_grid[2][i] != '':
            winner = xo_grid[0][i]
            return
    if xo_grid[0][0] == xo_grid[1][1] == xo_grid[2][2] != '':
        winner = xo_grid[0][0]
        return
    if xo_grid[0][2] == xo_grid[1][1] == xo_grid[2][0] != '':
        winner = xo_grid[0][2]
        return
    if all(x != '' for row in xo_grid for x in row):
        winner = 'Tie Game'
        return
    winner = None

############################################################################################
# You should not modify the code below this line 
############################################################################################

# Constants
LINE_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_SIZE = 3
SQUARE_SIZE = WIDTH // BOARD_SIZE

#globals
screen = None
winner = None

def Init():
    # Initialize Pygame
    
    global screen
    pygame.init()

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Initialize the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    
    # Draw the grid
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

#
# Function to draw X or O
# Parameters:
#   row  - 0 based row nunumber of the square to change to X or O
#   col  - 0 based column nunumber of the rentangle to X or O
#   XorO - either an 'X' or 'O' string indicating what to display in the correponding grid square
#
def draw_x_o(row, col, XorO):
    global screen
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if XorO == 'X':
        pygame.draw.line(screen, LINE_COLOR, (x - SQUARE_SIZE // 4, y - SQUARE_SIZE // 4),
                         (x + SQUARE_SIZE // 4, y + SQUARE_SIZE // 4), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (x + SQUARE_SIZE // 4, y - SQUARE_SIZE // 4),
                         (x - SQUARE_SIZE // 4, y + SQUARE_SIZE // 4), LINE_WIDTH)
    elif XorO == 'O':
        pygame.draw.circle(screen, LINE_COLOR, (x, y), SQUARE_SIZE // 4, LINE_WIDTH)
        
    else: 
        raise Exception("Illegal value " + XorO + " draw_x_o")


def gameLoop():

    Init()
    
    while winner == None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                processGridClick(clicked_row, clicked_col)
                check_for_winner()
 
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(30)
        
    if winner == 'X' or winner == 'O':
        input (winner + " won!  Press enter to exit")
    elif winner != None:
        input ("Tie game!  Press enter to exit")
        

if __name__=="__main_":
    main()