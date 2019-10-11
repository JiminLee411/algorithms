import sys; sys.stdin = open('swep_5174_input.txt', 'r')

def addTree(v):
    global cnt
    if tree[0][v]:
        cnt += 1
        addTree(tree[0][v])
    if tree[1][v]:
        cnt += 1
        addTree(tree[1][v])

for tc in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0] * (E + 2) for _ in range(2)]
    cnt = 1
    for i in range(0, len(arr), 2):
        if tree[0][arr[i]] == 0:
            tree[0][arr[i]] = arr[i + 1]
        else:
            tree[1][arr[i]] = arr[i + 1]
    addTree(N)

    print('#{} {}'. format(tc, cnt))
