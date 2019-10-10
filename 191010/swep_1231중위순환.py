import sys; sys.stdin = open('swep_1231_input.txt', 'r')

def inorder(v):
    global res
    if L[v]:
        inorder(L[v])
    res += P[v]
    if R[v]:
        inorder(R[v])

for tc in range(1, 11):
    V = int(input())
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    res = ''
    for _ in range(V):
        arr = list(input().split())

        for i in range(1, len(arr)):
            if i == 1:
                P[int(arr[0])] = arr[i]
            elif i == 2:
                L[int(arr[0])] = int(arr[i])
            elif i == 3:
                R[int(arr[0])] = int(arr[i])

    inorder(1)
    print('#{} {}'. format(tc, res))
