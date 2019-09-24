import sys

sys.stdin = open('input.txt', 'r')
def FindCode():
    tmp = [0, 0]

    DECODE = {
        '211': 0,
        '221': 1,
        '122': 2,
        '411': 3,
        '132': 4,
        '231': 5,
        '114': 6,
        '312': 7,
        '213': 8,
        '112': 9
    }

    

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    

    print('#{} {}'. format(tc, res))