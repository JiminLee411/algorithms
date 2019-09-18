import sys

sys.stdin = open('input.txt', 'r')
def FindCode():
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    for r in range(N):
        last = 0
        for c in range(M-1, 0, -1):
            if arr[r][c] == '1':
                last = 1
                break
        if last == 1:
            break
    totalCode = arr[r][c-55:c+1]

    return Decoding(totalCode)

def Decoding(totalCode):
    tmp = [0, 0]

    decodeTable = {'0001101': 0,
                 '0011001': 1,
                 '0010011': 2,
                 '0111101': 3,
                 '0100011': 4,
                 '0110001': 5,
                 '0101111': 6,
                 '0111011': 7,
                 '0110111': 8,
                 '0001011': 9}

    for i in range(4):
        tmp[0] += decodeTable[totalCode[7*(i+1)*2 - 14 : 7*(i+1)*2 - 7]]
        tmp[1] += decodeTable[totalCode[7*(i+1)*2 - 7 : 7*(i+1)*2]]

    return 0 if (tmp[0] * 3 + tmp[1]) % 10 != 0 else tmp[0] + tmp[1]

for tc in range(1, int(input()) + 1):
    res = FindCode()

    print('#{} {}'. format(tc, res))