import sys

sys.stdin = open('4873_input.txt', 'r')

def erase(N, len_N):
    tmp = ''
    for i in range(len_N - 1):
        if N[i] == N[i + 1]:
            tmp = N[0:i] + N[i + 2:len_N]
            return erase(tmp, len(tmp))
    return N

for t in range(1, int(input()) + 1):
    N = input()
    res = erase(N, len(N))
    print('#{} {}'. format(t, len(res)))
