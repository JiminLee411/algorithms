import sys

sys.stdin = open('10815_input.txt', 'r')

M = int(input())
my = list(map(int, input().split()))
N = int(input())
value = list(map(int, input().split()))
comp = ['0' for _ in range(N)]

for i in range(N):
    if value[i] in my:
        comp[i] = '1'

res = ' '.join(comp)
print(res)

