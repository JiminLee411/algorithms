import sys

sys.stdin = open('swep_5202input.txt', 'r')

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda element:element[1])
    choose = []
    choose.append(arr[0])
    tmp = arr[0][1]
    for i in range(N):
        if arr[i][0] < tmp:
            continue
        choose.append(arr[i])
        tmp = arr[i][1]

    print('#{} {}'.format(t, len(choose)))
