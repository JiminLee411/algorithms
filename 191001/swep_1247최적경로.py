import sys

sys.stdin = open('swep_1247_input.txt', 'r')

def DFS(k):
    global MIN, tmp
    if not 0 in visit:
        MIN = min(MIN, tmp + abs(home[0] - money[k][0]) + abs(home[1] - money[k][1]))
        return
    for i in range(N):
        if tmp + abs(money[k][0] - money[i][0]) + abs(money[k][1] - money[i][1]) >= MIN:
            continue
        if not visit[i]:
            visit[i] = 1
            tmp += abs(money[k][0] - money[i][0]) + abs(money[k][1] - money[i][1])
            DFS(i)
            tmp -= abs(money[k][0] - money[i][0]) + abs(money[k][1] - money[i][1])
            visit[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = arr[0:2]
    home = arr[2:4]
    money = [arr[2*i:(i + 1)*2] for i in range(2, N + 2)]
    MIN = 1000
    tmp = 0
    visit = [0] * (N)
    for i in range(N):
        tmp = abs(company[0] - money[i][0]) + abs(company[1] - money[i][1])
        DFS(i)

    print(MIN)


