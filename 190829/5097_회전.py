import sys
sys.stdin = open('5097_input.txt', 'r')

for t in range(1, int(input()) + 1):
    N, M  = map(int, input().split())
    arr = list(map(int, input().split()))
    calc = M % N
    print('#{} {}'. format(t, arr[calc]))