

T = int(input())

for tc in range(1, T + 1):
    word = input()
    div = word.split('*')
    front = word[0]
    end = word[-1]
    end = end[::-1]
    if front == end[0:len(front)] or front[0:len(end)] == end:
        res = 1
    else:
        res = 0
    if word[0] == '*' or word[-1] == '*':
        res = 1

    if res:
        print('#{} Exist'.format(tc))
    else:
        print('#{} Not exist'.format(tc))


