import sys
sys.stdin = open('input.txt', 'r')
for t in range(1, int(input()) + 1):
    value = list(input().split())
    num = []
    for i in range(len(value)):
        if value[i] == '.':
            if i == len(value) - 1 and len(num) == 1:
                print('#{} {}'.format(t, num[0]))
            else:
                print('#{} error'.format(t))
                break
        elif value[i].isnumeric():
            num.append(int(value[i]))
        elif value[i] in '+*/-' and len(num) >= 2:
            if value[i] == '+':
                tmp = num.pop(-2) + num.pop(-1)
                num.append(tmp)
            elif value[i] == '-':
                tmp = num.pop(-2) - num.pop(-1)
                num.append(tmp)
            elif value[i] == '*':
                tmp = num.pop(-2) * num.pop(-1)
                num.append(tmp)
            elif value[i] == '/':
                tmp = num.pop(-2) // num.pop(-1)
                num.append(tmp)
        else:
            print('#{} error'.format(t))
            break
