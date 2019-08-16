import sys

sys.stdin = open('4865_input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):
    char = set(input())
    target = input()
    value = set(target)
    comp = {}

    for elem in value:
        if elem in char:
            comp[elem] = target.count(elem)
    print('#{} {}'. format(tc, max(comp.values())))