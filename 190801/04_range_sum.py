import sys

sys.stdin = open('04_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    numbers, sum_num = map(int, input().split())
    num_list = list(map(int, input().split()))

    res = []

    for i in range(len(num_list) - sum_num + 1):
        sum = 0
        for j in range(sum_num):
            sum += num_list[i + j]
        res.append(sum)

    print('#{} {}'.format(test_case, max(res) - min(res)))