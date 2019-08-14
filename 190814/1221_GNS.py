import sys

sys.stdin = open('1221_input.txt', 'r')
# change = {
#     'ZRO': 0,
#     'ONE': 1,
#     'TWO': 2,
#     'THR': 3,
#     'FOR': 4,
#     'FIV': 5,
#     'SIX': 6,
#     'SVN': 7,
#     'EGT': 8,
#     'NIN': 9
# }
alien_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())

for tc in range(1, T + 1):
    N = input()
    N = int(N[3:])

    numbers = list(map(str, input().split()))
    res = ''
    print('#{}'. format(tc))
    for num in alien_num:
        i = 0
        while num in numbers:
            if numbers[i] == num and len(numbers)== 1:
                print(numbers.pop(i))
            elif numbers[i] == num:
                print(numbers.pop(i), end=' ')
            else:
                i += 1