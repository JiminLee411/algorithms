import sys

sys.stdin = open('01_input.txt', 'r')

while 1:
    tc_num = int(input())
    if 1 <= tc_num <= 50:
        break

for tc in range(tc_num):
    while 1:
        numbers = int(input())
        if 5 <= numbers <= 1000:
            break

    num_list = list(map(int,input().split()))

    for num in range(len(num_list) - 1, 0, -1):
        for comp in range(num):
            if num_list[comp] > num_list[comp + 1]:
                num_list[comp], num_list[comp + 1] = num_list[comp + 1], num_list[comp]
    if num_list[-1] > 1000000:
        print('범위를 초과했습니다. 범위는 1 <= compared numbers <= 1000000')
    result = num_list[-1] - num_list[0]

    print('#{} {}'.format(tc + 1, result))

