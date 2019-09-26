# 위상정렬 - DFS
# def DFS(v):
#     visit[v] = True
#     for w in G[v]:
#         if not visit[w]:
#             DFS(w)
#
#         stack.append(v)
# V, E = map(int, input().split())
#
# G = [[] for i in range(V + 1)]

# 계산기

# target = input()
# rank = {'(': 3, '*': 2, '/': 2, '-': 1, '+': 1}
# now = 0
# stack = []
# tmp = ''
# res = ''
# for i in target:
#     if i in '0123456789':
#         tmp.append(i)
#     elif not stack:
#         stack.append(i)
#         now = rank[i]
#     elif rank[i] > now:
#         stack.append(i)
#         now = rank[i]
#     elif rank[i] <= now:
#         tmp.append(stack.pop())
#         now = rank[stack(-1)]
# for i in range(len(stack)):
#     tmp.append(stack.pop())
#
# print(tmp)
#
# for i in range tmp:
#     if i in '0123456789':


# 부분집합의 합
# arr = 'ABC'
# N = len(arr)
# bits = [0] * N
#
# def subset(k, n):   # k = 현재 노드의 높이, n: 단말 노드의 높이
#     if k == n:  # 단말 노드에 도착
#         for i in range(N):
#             if bits[i]:
#                 print(arr[i], end=' ')
#         print()
#         return
#     bits[k] = 1 # 해당 인덱스의 요소를 부분집합에 포함하겠다는 의미
#     subset(k + 1, n)    # 왼쪽
#     bits[k] = 0
#     subset(k + 1, n)    # 오른쪽
# subset(0, N)    # 0 = 어떤 선택도 하지 않았다.
#                 # N = 해야할 선택의 수
#
# list2의 부분집합의 합 문제 풀어보기
# bits = [0] * 12
# def subset(k, n):
#     global N, K, ans
#     if k == n:
#         cnt = S = 0
#         for i in range(n):
#             if bits[i]:
#                 cnt, S = cnt + 1, S + (i + 1)
#         if cnt == N and S == K:
#             ans += 1
#     else:
#         bits[k] = 1; subset(k + 1, n)
#         bits[k] = 0; subset(k + 1, n)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     ans = 0
#     subset(0, 12)
#     print('#{} {}'.format(tc, ans))
#
#
# def subset(k, n, cnt, sum_now):
#     global ans, N, K
#     if cnt > N or sum_now > K:
#         return
#     if k == n:
#         if cnt == N and sum_now == K:
#             ans += 1
#         return
#
#     subset(k + 1, n, cnt, sum_now)
#     subset(k + 1, n, cnt + 1, sum_now + k)
#
# T = int(input())
# numbers = [i for i in range(1, 13)]
#
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     ans = 0
#     tmp = 0
#     subset(1, 13, 0, 0)
#     print('#{} {}'.format(tc, ans))
#
# def subset(k, n, cnt, sum_now):
#     global ans, N, K
#     if cnt > N or sum_now > K:
#         return 0
#     if k == n:
#         if cnt == N and sum_now == K:
#             return 1
#         else:
#             return 0
#     subset(k + 1, n, cnt, sum_now)
#     subset(k + 1, n, cnt + 1, sum_now + k)
#
#     ret = 0
#     ret += subset(k + 1, n, cnt + 1, sum_now + k)
#     ret += subset(k + 1, n, cnt, sum_now)
#     return ret
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#
#     print('#{} {}'.format(tc, subset(1, 13, 0, 0)))

# 순열
# 중복순열
# arr = 'ABC'
# N = len(arr)
#
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             print(arr[i], arr[j], arr[k])

# 일반 순열
# arr = 'ABC'
# N = len(arr)
#
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         for k in range(N):
#             if i == k or j ==k:
#                 continue
#             print(arr[i], arr[j], arr[k])

# order를 훑으면서 전의 값을 알아
# arr = 'ABC'
# N = len(arr)
# order = [0] * N     # 실제 요소들의 순서(index를 기록)
#
# def perm(k, n):
#     if k == n:
#         for i in range(N):
#             print(arr[order[i]], end=' ')
#         print()
#         return
#     used = [False] * N
#     for i in range(k):  # 지금까지 선택한 k개의 원소를 확인
#         used[order[i]] = True
#
#     for i in range(N):  # 선택한 요소들에 대해
#         if used[i]:
#             continue
#         order[k] = i
#         perm(k + 1, n)
#
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         for k in range(N):
#             if i == k or j ==k:
#                 continue
#             print(arr[i], arr[j], arr[k])

# 지금까지 선택한 요소들이 뭔지 저장해서 썼다 지웠다 하면서 사용
# arr = 'ABC'
# N = len(arr)
# order = [0] * N     # 실제 요소들의 순서(index를 기록)
# used = [0] * N
#
# def perm(k, n):
#     if k == n:
#         for i in range(N):
#             print(arr[order[i]], end=' ')
#         print()
#         return
#     for i in range(k):  # 지금까지 선택한 k개의 원소를 확인
#         used[order[i]] = True
#
#     for i in range(N):  # 선택한 요소들에 대해
#         if used[i]:
#             continue
#         used[i] = 1
#         order[k] = i
#         perm(k + 1, n)
#         used[i] = 0
#
# perm(0, N)

# 매개변수 자체로 저장해 넘겨준다
arr = 'ABC'
N = len(arr)
order = [0] * N     # 실제 요소들의 순서(index를 기록)

def perm(k, n, used):
    if k == n:
        for i in range(N):
            print(order[i], end=' ')
        print()
        return

    for i in range(N):
        if used & (1 << i):
            continue
        order[k] = i
        perm(k + 1, n, used | (1 << i))

perm(0, N, 0)


# 동전 교환 문제
# coin = [1, 4, 6]
# choose = [0] * 100
# def coinChange(k, n):       #k: 선택한 동전의 수, n: 거스름돈 금액
#     if n == 0:
#         for i in range(k):
#             print(choose[i], end=' ')
#         print()
#         return
#     for c in coin:
#         if c > n:
#             continue
#         choose[k] = c
#         coinChange(k + 1, n - c)
#
# coinChange(0, 8)

# 동전 문제 최적화
# coin = [6, 4, 1] # 순서를 내림차순으로
# choose = [0] * 100
# MIN = 0xffffff
# def coinChange(k, n):       #k: 선택한 동전의 수, n: 거스름돈 금액
#     global MIN
#     if k >= MIN:
#         return
#     if n == 0:
#         MIN = min(k, MIN)
#         for i in range(k):
#             print(choose[i], end=' ')
#         print()
#         return
#     for c in coin:
#         if c > n:
#             continue
#         choose[k] = c
#         coinChange(k + 1, n - c)
#
# coinChange(0, 8)

# arr = 'ABC'
# N = len(arr)
# order = [0] * N         # 원소의 인덱스의 순서를 저장
# def perm(k, n, used):
#     if k == n:          # 하나의 순열을 생성
#         for i in range(n):
#             print(arr[order[i]], end=' ')
#         print()
#         return
#
#     for i in range(n):
#         if used & (1 << i):
#             continue
#         order[k] = i
#         perm(k + 1, used | (1 << i))
#
# perm(0, N, 0)           # 0: 선택한 수, N: 전체원소수, 0: 선택한 요소들의 집합\

# 병합정렬
# arr = [6, 4, 2, 5, 1, 9, 2, 11, 8, 7]

# def getMin(first, last):
#     if first == last:
#         return arr[first]
#     mid = (first + last) >> 1
#     return min(getMin(first, mid), getMin(mid + 1, last))

# print(getMin(0, len(arr) - 1 ))

# 퀵정렬
