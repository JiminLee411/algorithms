import sys

sys.stdin = open('Ladder_input.txt', 'r')

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break

    dir = 0
    while x:
        if y - 1 >= 0 and arr[x][y - 1]:
            while y - 1 >= 0 and arr[x][y - 1]:
                y -= 1
        elif y - 1 >= 0 and arr[x][y - 1]:
            while y + 1 >= 0 and arr[x][y + 1]:
                y += 1
        x -= 1

    print(y)