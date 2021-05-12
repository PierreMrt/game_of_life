import random
import copy
import os
import time

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.initial_proportion = 0.5
        self.neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        self.rules = {
            'die'    : [0, 1, 4, 5, 6, 7, 8],
            'survive': [2, 3],
            'birth'  : [3]
            }
        self.initial_state = self.random_state()
    
    def dead_state(self):
        board = []
        for r in range(self.height):
            board.append([0] * self.width)
        return board

    def random_state(self):
        board = self.dead_state()
        for r in range(self.height):
            for c in range(self.width):
                if random.random() >= self.initial_proportion:
                    board[r][c] = 1 
        return board

    @staticmethod
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

    def next_state(self, board):
        next_board = copy.deepcopy(board)
        for r in range(len(board)):
            for c in range(len(board[0])):
                nb_neighbours = 0
                for n in self.neighbours:
                    try:
                        nb_neighbours += board[r + n[0]][c + n[1]]
                    except IndexError:
                        pass
                if board[r][c] == 1 and nb_neighbours in self.rules['survive']:
                    next_board[r][c] = 1
                elif board[r][c] == 1 and nb_neighbours in self.rules['die']:
                    next_board[r][c] = 0
                elif board[r][c] == 0 and nb_neighbours in self.rules['birth']:
                    next_board[r][c] = 1    
        return next_board

    def run(self):
        board = copy.deepcopy(self.initial_state)
        self.render(board)

        while True:
            time.sleep(0.1)
            board = self.next_state(board)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.render(board)

        

            
def main():
    world = World(150, 50)
    world.run()

if __name__ == '__main__':
    main()


        