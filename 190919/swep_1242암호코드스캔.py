import sys

sys.stdin = open('input.txt', 'r')
def FindCode():
    tmp = [0, 0]

    DECODE = {
        (3, 2, 1, 1): 0,
        (2, 2, 2, 1): 1,
        (2, 1, 2, 2): 2,
        (1, 4, 1, 1): 3,
        (1, 1, 3, 2): 4,
        (1, 2, 3, 1): 5,
        (1, 1, 1, 4): 6,
        (1, 3, 1, 2): 7,
        (1, 2, 1, 3): 8,
        (3, 1, 1, 2): 9
    }

    for r in range(N):
        arr = total[r].rstrip('0')
        if not arr:
            continue
        t = format(int('0x' + arr, 16), 'b')
        c = len(arr) - 1
        while c >=0:
            if arr[c] == '1' and (total[r - 1][c] =='0' or r == 0):
                code = []
                for i in range(8):
                    c2 = c3 = c4 = 0
                    while arr[c] == '1': c4 , c = c4 + 1, c - 1
                    while arr[c] == '0': c3 , c = c3 + 1, c - 1
                    while arr[c] == '1': c2, c = c2 + 1, c - 1

                    MIN = min(c2, c3, c4)
                    print(7 - (c2//MIN, c3//MIN, c4//MIN), c2//MIN, c3//MIN, c4//MIN)
                    code.append(DECODE[7 - (c2//MIN, c3//MIN, c4//MIN), c2//MIN, c3//MIN, c4//MIN])
                a = code[0] + code[2] + code[4] + code[6]
                b = code[1] + code[3] + code[5] + code[7]

                if (a * 3 + b) % 10 == 0:
                    return a + b
                else:
                    return 0
            c -= 1
    return 0

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    total = [input() for _ in range(N)]

    res = FindCode()

    print('#{} {}'. format(tc, res))