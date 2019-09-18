import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    num = float(input())
    num_tmp = num
    tmp = ''
    i = -1
    while num_tmp > 0:
        if len(tmp) == 13:
            tmp = 'overflow'
            break

        if num_tmp >= 2 ** i:
            num_tmp -= 2 ** i
            tmp += '1'
        else:
            tmp += '0'
        i -= 1
    print('#{} {}'.format(tc, tmp))