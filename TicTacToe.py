import pygame


class Button():
    def __init__(self, xy, w, h, i):
        self.rectcoord = (xy, (w, h))
        self.rect = pygame.Rect(self.rectcoord)
        self.index = i
    def rectcollide(self, cp): 
        mx, my = pygame.mouse.get_pos()
        if self.rect.collidepoint(mx, my) and board[self.index][1] == 2:
            board[self.index][1] = cp
            boardupdate((self.rect[0], self.rect[1]), cp, self.index)
            boardcheckwin(board, cp)



pygame.init()

width = 400
height = 400

pygame.display.set_caption("Tic Tac Toe");
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)


rects = []   #list to hold all rect objects to detect clicks
#  0 = cross
#  1 = circle
#  2 = none
#  [(x, y), element]
board = [[(50, 50), 2],  [(150, 50), 2],  [(250, 50), 2],    # a list holding a tuple and a state for each element,
         [(50, 150), 2], [(150, 150), 2], [(250, 150), 2],   # the tuple holds the position(x, y) and the state holds current    
         [(50, 250), 2], [(150, 250), 2], [(250, 250), 2]]   # state of the square(if he has a cross(0), circle(1) ou none of those(2)) 

index = 0                                                         
for square in board:                              #creates 9 Button classes, 1 for each square in the board
    b = Button(square[0], 100, 100, index)        #and append everthing to a "rects" list
    index += 1
    rects.append(b)

def boardupdate(pos, player, elem):
    mydict ={
        0 : (255, 0, 0),
        1 : (0, 0, 255)
    }
    board[elem][1] = player                    
    if player == 0:
        drawcross(mydict[player], elem)
    else:
        drawcircle(mydict[player], elem)
    players[0] = (player + 1) % 2


def drawcross(player, elem):
    pygame.draw.line(screen, player, (board[elem][0][0]+25, board[elem][0][1]+25), (board[elem][0][0]+75, board[elem][0][1]+75), width=5)
    pygame.draw.line(screen, player, (board[elem][0][0]+75, board[elem][0][1]+25), (board[elem][0][0]+25, board[elem][0][1]+75), width=5)
def drawcircle(player, elem):
    pygame.draw.circle(screen, player, (board[elem][0][0]+50, board[elem][0][1]+50), 30)
    pygame.draw.circle(screen, black, (board[elem][0][0]+50, board[elem][0][1]+50), 25)

def resetboard():
    for i in range(9):
        board[i][1] = 2
        screen.fill(black)
    drawboard()

def boardcheckwin(b, cp):
    #checks all 8 possible ways to win, if true, gives win to "cp(current player)" player
    if (  (b[0][1] == cp and b[1][1] == cp and b[2][1] == cp)
        or(b[3][1] == cp and b[4][1] == cp and b[5][1] == cp)
        or(b[6][1] == cp and b[7][1] == cp and b[8][1] == cp)
        or(b[0][1] == cp and b[3][1] == cp and b[6][1] == cp)
        or(b[1][1] == cp and b[4][1] == cp and b[7][1] == cp)
        or(b[2][1] == cp and b[5][1] == cp and b[8][1] == cp)
        or(b[2][1] == cp and b[4][1] == cp and b[6][1] == cp)
        or(b[0][1] == cp and b[4][1] == cp and b[8][1] == cp)
    ):
        winner = "Cross"
        if cp == 1:
            winner = "Circle"
        print(winner + " player won!")
        resetboard()
    else:
        # checks for all board filled but no winner
        count = 0
        for i in range(9):
            if b[i][1] == 2:
                count+=1
        if count == 0:
            print("No player won")
            resetboard()
 

def drawboard():
    for lin in range(4):
        pygame.draw.line(screen, white, (50, lin*100+50), (350, lin*100+50), width=2)
    for col in range(4):
        pygame.draw.line(screen, white, (col*100+50, 50), (col*100+50, 350), width=2)

drawboard()    # draw the initial board
players = [0]  # initial player
gameover = False

while not gameover:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                resetboard()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for rect in rects:
                rect.rectcollide(players[0])
                

    pygame.display.update()
    clock.tick_busy_loop(60)

pygame.quit()