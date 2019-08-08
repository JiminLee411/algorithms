import sys

sys.stdin = open('10164_input.txt', 'r')

N = int(input())

board = [[0] * 101 for _ in range(101)]
cnt = [0 for i in range(N)]
for i in range(N):
    value = list(map(int, input().split()))
    for x in range(value[0], value[2] + value[0]):
        for y in range(value[1], value[3] + value[1]):
            board[x][y] = i + 1
for j in range(N):
    for i in range(101):
        cnt[j] += board[i].count(j+1)
    print(cnt[j])
