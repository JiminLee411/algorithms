import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    result = 0

    for num in range(2, len(height) - 2):
        compare_num = [height[num - 2], height[num - 1], height[num], height[num + 1], height[num + 2]]

        # bubble sort를 이용해 list 정렬
        for j in range(len(compare_num) - 1, 0, -1):

            for i in range(j):  # n - 1 ~ 1만금 반벅
                if compare_num[i] > compare_num[i + 1]:
                    compare_num[i], compare_num[i + 1] = compare_num[i + 1], compare_num[i]

        if compare_num[-1] == height[num]:
            result += compare_num[-1] - compare_num[-2]

    print('#{} {}'.format(tc + 1, result))