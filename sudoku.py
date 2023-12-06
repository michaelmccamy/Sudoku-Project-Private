import pygame, sys
from sudoku_generator import SudokuGenerator, generate_sudoku


def draw_grid():
    for i in range(0, 10): #draws horizontal lines
        if i % 3 == 0:
            width = 7
        else:
            width = 3
        pygame.draw.line(screen,
                         (0,0,0),
                         (0, i * 60),
                         (540, i * 60),
                         width)

    for i in range(0, 10): #draws vertical lines
        if i % 3 == 0:
            width = 7
        else:
            width = 3
        pygame.draw.line(screen,
                         (0,0,0),
                         (i * 60, 0),
                         (i * 60, 540),
                         width)


def draw_num(obj):
    font = pygame.font.SysFont(None, 60)
    for row in range(9):
        for column in range(9):
            if obj[row][column] != 0:
                cell_num = obj[row][column]
                cell_text = font.render(str(cell_num), True, pygame.Color('black'))
                screen.blit(cell_text, pygame.Vector2((column*60)+20, (row*60)+15))

def highlight_cell(x, y, color):
    pygame.draw.rect(screen, pygame.Color(color), pygame.Rect(x, y, 60, 60), 5)

#def sketch_num(obj, screen_obj, num):



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((540,540)) #creates a screen of 540x540 pixels
    screen.fill((255, 255, 245)) #sets color of screen
    draw_grid()
    board = generate_sudoku(9,30) #creates board object from SudokuGenerator class
    draw_num(board)

#cells = [] #true false
#for i in range(9):
    #row = []
    #for j in range(9):
     #   row.append(False)
    #cells.append(row)
#draw_grid()
#draw_num(board)
while True:
    for event in pygame.event.get():
        coord = None
        pygame.display.flip()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = 0
            coord = pygame.mouse.get_pos()
            cell_col = coord[0] - (coord[0] % 60)
            cell_row = coord[1] - (coord[1] % 60)
            highlight_cell(cell_col, cell_row, 'blue')
            #if cells[coord[0]//60][coord[1]//60]:
             #   cells[coord[0] // 60][coord[1] // 60] = False
            #else:
             #   cells[coord[0] // 60][coord[1] // 60] = True

            #for i in range(9):
                #for j in range(9):
                    #if cells[i][j] == True:
                        #highlight_cell(cell_col, cell_row, 'blue')
                    #else:
                        #highlight_cell(cell_col, cell_row, 'white')

            click = 1
            #if click == 1:
                #highlight_cell(cell_col, cell_row, 'white')

    #screen.fill((255,255,255))


    #screen.fill((0,0,0))



    #pygame.display.update()
    #draw_num(board)

