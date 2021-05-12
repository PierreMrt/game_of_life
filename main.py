import random
import copy
import os
import time

def dead_state(width, height):
    board = []
    for r in range(height):
        board.append([0] * width)
    return board

def random_state(width, height):
    board = dead_state(width, height)
    for r in range(height):
        for c in range(width):
            if random.random() >= 0.8:
                board[r][c] = 1 
    return board

def render(board):
    render_board = copy.deepcopy(board)
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                render_board[r][c] = '#'
            else:
                render_board[r][c] = ' '
    
    print(' ' + '-' * len(board[0]))
    for r in render_board:
        s = ''.join(r)
        print(f'|{s}|')
    print(' ' + '-' * len(board[0]))

def next_board_state(board):
    neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    rules = {
        'die'    : [0, 1, 4, 5, 6, 7, 8],
        'survive': [2, 3],
        'birth'  : [3]
    }
    next_board = copy.deepcopy(board)
    for r in range(len(board)):
        for c in range(len(board[0])):
            nb_neighbours = 0
            for n in neighbours:
                try:
                    nb_neighbours += board[r + n[0]][c + n[1]]
                except IndexError:
                    pass
            if board[r][c] == 1 and nb_neighbours in rules['survive']:
                next_board[r][c] = 1
            elif board[r][c] == 1 and nb_neighbours in rules['die']:
                next_board[r][c] = 0
            elif board[r][c] == 0 and nb_neighbours in rules['birth']:
                next_board[r][c] = 1
    
    return next_board

            
def main():
    board = random_state(150, 50)
    render(board)

    while True:
        time.sleep(0.1)
        board = next_board_state(board)
        os.system('cls' if os.name == 'nt' else 'clear')
        render(board)


if __name__ == '__main__':
    main()


        