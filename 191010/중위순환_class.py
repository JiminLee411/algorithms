import sys; sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())    # 노드수, 간선수
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

arr = list(map(int, input().split()))
for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    if L[p] == 0: L[p] = c
    else: R[p] = c
    P[c] = p    # 부모 정보는 필요한 경우에 저장해서 사용

# -------------------------------------- #
# ------------ 중위 순회 1 ---------------
def inorder(v):     # V = 현재 노드
    if v == 0: return
    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])

# ------------ 중위 순회 2 ----------------
def inorder(v):     # V = 현재 노드
    if L[v]:
        inorder(L[v])
    print(v, end=' ')
    if R[v]:
        inorder(R[v])
# ---------------------------------------
inorder(1)