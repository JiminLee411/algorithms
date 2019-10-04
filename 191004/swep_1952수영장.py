import sys

sys.stdin = open('swep_1952_input.txt', 'r')

for tc in range(1, int(input()) + 1):
    d, m, tM, y = map(int, input().split())
    month = list(map(int, input().split()))


