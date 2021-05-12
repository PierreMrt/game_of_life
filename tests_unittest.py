import unittest

from main import *


class TestDeadState(unittest.TestCase):
    def test_dead_state(self):
        tests = {
            'test1': {'height': 4, 'width': 3, 'expected':[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]},
            'test2': {'height': 5, 'width': 2, 'expected':[[0,0],[0,0],[0,0],[0,0],[0,0]]},
            'test3': {'height': 3, 'width': 5, 'expected':[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]}
        }

        for key, attrs in tests.items():
            world = World(attrs['width'], attrs['height'])
            actual_board = world.dead_state()
            expected_board = attrs['expected']

            self.assertEqual(actual_board, expected_board, f'Sould be {expected_board}')

class TestCountNeighbours(unittest.TestCase):
    def test_count_neighbours(self):
        board = [
            [0,1,0,1,0,0,1],
            [0,1,1,0,0,0,1],
            [0,0,0,1,1,0,0],
            [1,0,1,1,0,1,1],
            [0,1,0,1,1,1,1]
        ]
        tests = {
            'test1': {'r': 3, 'c': 3, 'expected':5},
            'test2': {'r': 1, 'c': 4, 'expected':3},
            'test3': {'r': 1, 'c': 6, 'expected':1},
            'test4': {'r': 4, 'c': 6, 'expected':3},
            'test5': {'r': 0, 'c':0, 'expected':2}
        }

        for key, attrs in tests.items():
            world = World(5,5)
            count = world.count_neighbours(attrs['r'], attrs['c'], board)
            self.assertEqual(count, attrs['expected'], f"Should be {attrs['expected']}")


class TestNextState(unittest.TestCase):
    def test_next_state(self):
        tests = {
            # 'test1': {'input': [[0,0,0],[0,0,0],[0,0,0],[0,0,0]], 'expected':[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]},
            'test2': {
                'input': [
                    [1,1,0], 
                    [1,1,0], 
                    [1,0,0], 
                    [0,1,1]], 
                'expected':[
                    [1,1,0],
                    [0,0,0],
                    [1,0,1],
                    [0,1,0]]},
            'test3': {
                'input': [
                    [0,1,0,1,0], 
                    [1,1,1,0,0], 
                    [1,0,1,0,1]], 
                'expected':[
                    [1,1,0,0,0],
                    [1,0,0,0,0],
                    [1,0,1,1,0]]}
        }
        
        for key, attrs in tests.items():
            world = World(5,5)
            next_state = world.next_state(attrs['input'])
            self.assertEqual(next_state, attrs['expected'], f"Should be {attrs['expected']}")

if __name__ == '__main__':
    unittest.main()