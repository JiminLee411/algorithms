import sys

sys.stdin = open('03_input.txt', 'r')


T = int(input())

for test_case in range(1, T + 1):
    card_num = int(input())
    value = input()

    max_num = int(max(value))
    count = [0] * (max_num + 1)
    card_list = []
    num = 0

    for i in value:
        card_list.append(int(i))
        count[max_num-int(i)] += 1

    for i in range(max_num + 1):
        if count[i] == max(count):
            num = max_num - i
            break

    print('#{} {} {}'.format(test_case, num, count[- num - 1]))
