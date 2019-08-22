# python-style
# for i in range(1, 4):
#     S.append(1)
#
# print(S.pop())

# ------------- 재귀 호출 -------------------------------------------#
# 1. 재귀적으로 문제를 해결
# - 재귀적 정의를 코드 구현할 때
# - 좀 더 작은 문제의 해를 이용해서 좀 더 큰 문제의 해를 구하는 과정
# -> 분할정복, DP

# 1. 재귀
# def printHello(i, n):
#     if i > n:
#         return
#     else:
#         print(i, 'Hello')
#         printHello(i + 1, n)
#         print(i, 'Hello')
#
# printHello(1, 3)

# 2. 재귀
# cnt = 0
# bits = [0] * 3
# def printHello(i, n):
#     global cnt
#     if i == n:
#         cnt += 1
#         print(bits)
#         return
#     else:
#         bits[i] = 1; printHello(i + 1, n)
#         bits[i] = 0; printHello(i + 1, n)
#
# printHello(0, 3)
# print('cnt = ', cnt)

# 3. factorial
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return fact(n - 1) * n
#
# res = fact(3)
#
# print(res)

# 4. 피보나치 수열 - 많은 중복이 발생
# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#
#     return fibo(n - 1) + fibo(n - 2)
#
# print(fibo(40))

# --------------- Memoization ----------------------------- #
# memo = [-1] * (101)
# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#     if memo[n] != -1: # 답을 구했으면
#         return memo[n]
#
#     memo[n] = fibo(n - 1) + fibo(n - 2)
#     return memo[n]
#
# print(fibo(40))

# ---------------   DP   ------------------------------------ #
# memo = [-1] * (101)
# def fibo(n):
#
#     memo[0], memo[1] = 0, 1
#
#     for i in range(2, n + 1): # i: 문제를 식별하는 값
#         memo[i] = memo[i - 1] + memo[i - 2]
#
#     return memo[n]
#
# print(fibo(40))
#
# memo2 = [0, 1]
# def fibo(n):
#
#     for i in range(2, n + 1): # i: 문제를 식별하는 값
#         memo2.append(memo2[i - 1] + memo2[i - 2])
#
#     return memo2[n]
#
# print(fibo(40))

# ---------------- DFS ------------------------------------#
import sys

sys.stdin = open('DFS_input.txt')

def DFS(v):
    S = []
    # 시작점을 방문하고, 스택에 push
    visit[v] = True
    print(v, end=' ')
    S.append(v)
    # 빈 스택이 아닐동안 반복
    while S:
        for w in G[v]:
            # v의 방문하지 않은 인접정점 w에 찾아서
            if not visit[w]:
                # w를 방문하고, v를 스택에 push
                visit[w] = True
                print(w, end=' ')
                S.append(w)
                # v를 w로 설정
                v = w
                break
            # 만약, 인접정점이 없다면, 스택에서 pop()해서
            else:
                # v로 설정
                v = S.pop()
V, E = map(int, input().split()) # 정점수, 간선수
G = [[] for _ in range(V + 1)] # 1 ~ V 까지
visit = [False] * (V + 1) # 방문정보

for _ in range(E):
    u, V = map(int, input().split())
    G[u].append(V)
    G[V].append(u) # 무향 그래프니까

DFS(1)


# -------------DFS with 재귀호출 ---------------- #
# import sys
#
# sys.stdin = open('DFS_input.txt')
#
# def DFS(v): # v = 현재 방문하는 정점
#     visit[v] = True
#     print(v, end=' ')
#
#     for w in G[v]:
#         # v의 방문하지 않은 인접정점 w에 찾아서
#         if not visit[w]:
#             DFS(w)
#
# V, E = map(int, input().split()) # 정점수, 간선수
# G = [[] for _ in range(V + 1)] # 1 ~ V 까지
# visit = [False] * (V + 1) # 방문정보
#
# for _ in range(E):
#     u, V = map(int, input().split())
#     G[u].append(V)
#     G[V].append(u) # 무향 그래프니까
#
# DFS(1)