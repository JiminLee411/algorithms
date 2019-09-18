import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, hex_num = map(str, input().split())
    num = int('0x'+ hex_num, 16)
    res = format(num, 'b')
    tmp = ''
    if len(res) % 4 != 0:
        for _ in range(4 - len(res) % 4):
            tmp += '0'
        res = tmp + res
    print('#{} {}'.format(tc, res))