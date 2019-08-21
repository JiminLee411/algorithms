import sys

sys.stdin = open('input.txt', 'r')

for t in range(1, int(input()) + 1):
    N = input()
    tmp = []
    for i in N:
        if i in '{(':
            tmp.append(i)

        if i == ')':
            if tmp.pop() == '(':
                res = 1
            else:
                res = 0
                break
        if i == '}':
            if tmp.pop() == '{':
                res = 1
            else:
                res = 0
                break
    if tmp:
        res = 0

    print('#{} {}'.format(t, res))
