import sys

sys.stdin = open('swep_1247_input.txt', 'r')

def DFS(k):
    global MIN, tmp
    if not 0 in visit:
        MIN = min(MIN, tmp + abs(home[0] - money[k][0]))
        return


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = arr[0:2]
    home = arr[2:4]
    money = [arr[2*i:(i + 1)*2] for i in range(2, N + 2)]
    MIN = 0xfffff
    tmp = 0
    visit = [0] * (N)
    DFS(0)


