import sys
sys.stdin = open('input.txt', 'r')


def battle(l, r):
    if cards[l] == cards[r]:
        return l
    elif cards[l] == 1:
        return r if cards[r]==2 else l
    elif cards[l] == 2:
        return r if cards[r]==3 else l
    elif cards[l] == 3:
        return r if cards[r]==1 else l

def tournament(group):
    if len(group) < 2:
        return group[0]

    left = tournament(group[:(len(group) + 1) //2])
    right = tournament(group[(len(group) + 1) //2:])

    return battle(left, right)


for t in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int,input().split()))
    tmp = list(range(N))
    res = tournament(tmp) + 1

    print('#{} {}'. format(t, res))