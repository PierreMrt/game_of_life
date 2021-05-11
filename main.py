import random

def dead_state(width, height):
    board = []
    for r in range(height):
        board.append([0] * width)
    return board

def random_state(width, height):
    board = dead_state(width, height)
    for r in range(height):
        for c in range(width):
            if random.random() >= 0.5:
                board[r][c] = 1 
    return board

def render(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                board[r][c] = ' # '
            else:
                board[r][c] = '   '
    
    print(' ' + '---' * len(board[0]))
    for r in board:
        s = ''.join(r)
        print(f'|{s}|')
    print(' ' + '---' * len(board[0]))

def next_board_state(board):
    neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    rules = {
        'die'    : (0, 1, 4, 5, 6, 7, 8),
        'survive': (2, 3),
        'birth'  : (3)
    }
    for r in len(board):
        for c in len(board[0]):
            nb_neighbours = 0
            for n in neighbours:
                nb_neighbours += board[r + n[0]][c + n[1]]
            if r[r][c] == 1 and nb_neighbours == 2:
                pass

            



if __name__ == '__main__':
    board = random_state(20, 20)
    render(board)


        