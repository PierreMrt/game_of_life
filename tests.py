from main import *

def title(name):
    print('-'*30)
    print(f'TESTING {name}')

def test_dead_state():
    title('dead_state')
    tests = {
        'test1': {'height': 4, 'width': 3, 'expected':[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]},
        'test2': {'height': 5, 'width': 2, 'expected':[[0,0],[0,0],[0,0],[0,0],[0,0]]},
        'test3': {'height': 3, 'width': 5, 'expected':[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]}
    }

    for key, attrs in tests.items():
        world = World(attrs['width'], attrs['height'])
        actual_board = world.dead_state()
        expected_board = attrs['expected']

        if actual_board == expected_board:
            print(f'PASSED {key}')
        else:
            print(f'FAILED {key}')

def test_count_neighbours():
    title('count_neighbours')
    board = [
        [0,1,0,1,0,0,1],
        [0,1,1,0,0,0,1],
        [0,0,0,1,1,0,0],
        [1,0,1,1,0,1,1],
        [0,1,0,1,1,0,1]
    ]
    tests = {
        'test1': {'r': 3, 'c': 3, 'expected':5},
        'test2': {'r': 1, 'c': 4, 'expected':3},
        'test3': {'r': 1, 'c': 6, 'expected':1}
    }

    for key, attrs in tests.items():
        world = World(5,5)
        count = World.count_neighbours(world, attrs['r'], attrs['c'], board)
        if count == attrs['expected']:
            print(f'PASSED {key}')
        else:
            print(f'FAILED {key}')
    
if __name__ == '__main__':
    test_dead_state()
    test_count_neighbours()