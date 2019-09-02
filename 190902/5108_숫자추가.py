import sys

sys.stdin = open('5108_input.txt', 'r')

for t in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        idx, value = map(int, input().split())
        arr. append(arr[N-1])
        for i in range(1, N - idx):
            arr[N - i] = arr[N - i - 1]
        arr[idx] = value
        N = N + 1

    print(arr[L])