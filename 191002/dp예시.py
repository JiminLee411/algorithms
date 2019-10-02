# -------------- 일반적 ------------------------------------ #
stick = ['B', 'Y', 'RR']
def makeStick(n, s):
    if n == 0:
        print(s)
    else:
        for i in stick:
            if n >= len(i):
                makeStick(n - len(i), s + i)
makeStick(50, '')


# --------------- 발견한 점화식 이용 ------------------------ #
stcik = ['B', 'Y', 'RR']


def makeStick(n):
    if n == 1: return 2
    if n == 2: return 5

    return makeStick(n - 1) * 2 + makeStick(n - 2)


print(makeStick(50))


# ------------ 점화식 + memoization ----------------------- #
stcik = ['B', 'Y', 'RR']
memo = [-1] * 100


def makeStick(n):
    if n == 1: return 2
    if n == 2: return 5
    if memo[n] != -1: return memo[n]

    memo[n] = makeStick(n - 1) * 2 + makeStick(n - 2)

    return memo[n]


print(makeStick(50))