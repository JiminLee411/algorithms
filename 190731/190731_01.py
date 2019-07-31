import sys
sys.stdin = open('input.txt', 'r')

# 01. max() 메서드 이용
for tc in range(10):
    N = int(input())
    height = list(map(int, input().split()))
    result = 0
    for num in range(2, len(height) - 2):
        if height[num] > height[num - 1] and height[num] > height[num - 2] and height[num] > height[num + 1] and height[num] > height[num + 2]:
            result += height[num] - max(height[num - 1], height[num - 2], height[num + 1], height[num + 2])

    print('#{} {}'.format(tc + 1, result))
