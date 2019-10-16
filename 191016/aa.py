for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    p = [x for x in range(N + 1)]

    def findSet(x):
        if x != p[x]:
            p[x] = findSet(p[x]) # path-compression
        return p[x]

    ans = N

    for _ in range(M):
        u, v = map(int, input().split())
        a = findSet(u)
        b= findSet(v)

        if a != b:
            p[b] = a
            ans -= 1

    print('#{} {}'. format(tc, ans))