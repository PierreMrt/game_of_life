from main import *

def test_dead_state():
    tests = {
        'test1': {'height': 4, 'width': 3, 'expected':[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]},
        'test2': {'height': 5, 'width': 2, 'expected':[[0,0],[0,0],[0,0],[0,0],[0,0]]},
        'test3': {'height': 3, 'width': 5, 'expected':[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]}
    }

    for key, attrs in tests.items():
        actual_board = dead_state(attrs['width'], attrs['height'])
        expected_board = attrs['expected']

        if actual_board == expected_board:
            print(f'PASSED {key}')
        else:
            print(f'FAILED {key}')
    


if __name__ == '__main__':
    test_dead_state()