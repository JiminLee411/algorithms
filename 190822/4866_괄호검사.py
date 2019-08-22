import sys

sys.stdin = open('4866_input.txt', 'r')

for t in range(1, int(input()) + 1):
    N = input()
    tmp = []
    res = 1
    for i in N:
        if len(tmp) == 0 and i in '})':
            res = 0
            break
        elif i in '{(':
            tmp.append(i)

        if i == ')':
            if tmp.pop() != '(':
                res = 0
                break
        if i == '}':
            if tmp.pop() != '{':
                res = 0
                break
    if tmp:
        res = 0

    print('#{} {}'.format(t, res))