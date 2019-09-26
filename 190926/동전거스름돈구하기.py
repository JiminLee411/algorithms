# 동전 교환 문제
# coins = [1, 4, 6]
# choose = []
# def coinChange(k, n):       #k: 선택한 동전의 수, n: 거스름돈 금액
#     if n == 0:
#         print(choose)
#     else:
#         for coin in coins:
#             if coin > n: continue
#             choose.append(coin)
#             coinChange(k+1, n - coin)
#             choose.pop()
#
# coinChange(0, 8)

# 동전 문제 최적화
coin = [6, 4, 1] # 순서를 내림차순으로
choose = []
memo = [-1] * 100

def coinChange(n):       #k: 선택한 동전의 수, n: 거스름돈 금액
    if n == 0: return 0
    if memo[n] != -1: return memo[n]
    MIN = 0xffffff
    for c in coin:
        if c > n: continue
        ret = coinChange(n - c) + 1
        if ret < MIN: MIN = ret
    memo[n] = MIN
    return MIN

print(coinChange(80))

# 동전 문제 최적화 (동적할당)
coin = [6, 4, 1] # 순서를 내림차순으로
choose = []
memo = [-1] * 100

def coinChange(n):       #k: 선택한 동전의 수, n: 거스름돈 금액
    memo[0] = 0
    for i in range(1, n + 1):
        MIN = 0xffffff
        for c in coin:
            if c > i: continue
            ret = memo[i - c] + 1
            if ret < MIN: MIN = ret
        memo[i] = MIN

    return memo[n]

print(coinChange(80))


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
# perm(0, N, 0)