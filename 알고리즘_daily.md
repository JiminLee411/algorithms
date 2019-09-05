# 190904

SE - 9월 4, 5일 집중실습

* [추억의 2048게임](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWw8omwKmQQDFAUD&contestProbId=AWbrg9uabZsDFAWQ&probBoxId=AWz0cii6NfIDFAVU&type=PROBLEM&problemBoxTitle=집중실습%289월05일%29&problemBoxCnt=4)

  * 성공!

    ```python
    def leftNup(n):
        global tmp
        for c in range(n - 1):
            while tmp[c] == 0 and (sum(tmp[c:]) != 0):
                tmp.append(tmp.pop(c))
        for c in range(n - 1):
            if tmp[c] == tmp[c+1]:
                tmp[c] += tmp.pop(c+1)
                tmp.append(0)
    
    def rightNdown(n):
        global tmp
        for c in range(n - 1, 0, -1):
            while tmp[c] == 0 and (sum(tmp[0:c]) != 0):
                tmp.pop(c)
                tmp = [0] + tmp
        for c in range(n - 1, 0, -1):
            if tmp[c] == tmp[c-1]:
                tmp[c - 1] += tmp.pop(c)
                tmp = [0] + tmp
    
    
    for t in range(1, int(input()) + 1):
        N, S = map(str, input().split())
        N = int(N)
        board = []
        tmp2 = []
        res = []
        for _ in range(N):
            tmp = list(map(int, input().split()))
            if S == 'left':
                leftNup(N)
                res.append(' '.join(list(map(str, tmp))))
            elif S == 'right':
                rightNdown(N)
                res.append(' '.join(list(map(str, tmp))))
            else:
                board.append(tmp)
        if S == 'up':
            for col in range(N):
                tmp = [row[col] for row in board]
                leftNup(N)
                tmp2.append(tmp)
            for col in range(N):
                tmp = [row[col] for row in tmp2]
                res.append(' '.join(list(map(str, tmp))))
        elif S == 'down':
            for col in range(N):
                tmp = [row[col] for row in board]
                rightNdown(N)
                tmp2.append(tmp)
            for col in range(N):
                tmp = [row[col] for row in tmp2]
                res.append(' '.join(list(map(str, tmp))))
    
        print('#{}'. format(t))
        for i in range(N):
            print(res[i])
    ```

* [4615_재밌는오셀로게임](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWw8omwKmQQDFAUD&contestProbId=AWQmA4uK8ygDFAXj&probBoxId=AWz0ceLaNeEDFAVU&type=PROBLEM&problemBoxTitle=%EC%A7%91%EC%A4%91%EC%8B%A4%EC%8A%B5%289%EC%9B%9404%EC%9D%BC%29&problemBoxCnt=4)

  * 성공!

    ```python
    def check(cr, cc, n, turn):
        if turn == 1: next = 2
        else: next = 1
        for r in range(-1,2):
            for c in range(-1,2):
                i = 1
                while (-1 < cr+r*i < n) and (-1 < cc+c*i < n) and board[cr + r*i][cc + c*i] == next:
                    if (-1 < cr+r*(i+1) < n) and (-1 < cc+c*(i+1) < n) and board[cr + r*(i+1)][cc + c*(i+1)] == turn:
                        for j in range(1, i + 2):
                            board[cr + r*j][cc + c*j] = turn
                    i += 1
    
    
    for t in range(1, int(input()) + 1):
        N, M = map(int, input().split())
        board = [[0 for c in range(N)] for r in range(N)]
        b = w = 0
        board[(N>>1) - 1][(N>>1) - 1] = 2
        board[(N>>1) - 1][N>>1] = 1
        board[N>>1][(N>>1) - 1] = 1
        board[N>>1][N>>1] = 2
    
        for _ in range(M):
            r,c,turn = map(int, input().split())
            board[r - 1][c - 1] = turn
            check(r - 1, c - 1, N, turn)
        for i in range(N):
            b += board[i].count(1)
            w += board[i].count(2)
        print('#{} {} {}'. format(t, b, w))
    ```

    

백준

* [1759.암호만들기](https://www.acmicpc.net/problem/1759)

  > 알파벳 증가하는 순서로 배열
  >
  > - 만약 6개 중 4개를 골라내면 조합, 6개 중 4개를 골라 순서대로 나열하면 순열
  > - 전체 원소 6개 중 원소 4개인 부분집합 만들어 풀 수 있다.

  * 풀이

    * 부분집합

      ```python
      pwd = []
      alpha = ('a', 'e', 'i', 'o', 'u')
      def backtrack(k, mo, ja): # mo : 모음 개수, ja : 자음 개수
          if len(pwd) == L:
              print(pwd)
              return
          if k == C:
              return
          pwd.append(arr[k])
          a = b= 0
          if arr[k] in alpha: a = 1
          else: b = 1
          backtrack(k + 1, mo + a, ja + b) # k번째 요소를 포함하는 경우
          pwd.pop()
          backtrack(k + 1, mo, ja) # k번째 요소를 포함하지 않는 경우
      
      L, C = map(int, input().split())
      arr = list(input().split())
      arr.sort()
      
      backtrack(0, 0, 0)
      ```

    * 조합 `6C4`

      ```python
      pwd = []
      alpha = ('a', 'e', 'i', 'o', 'u')
      choose = []
      def comb(k ,start): # k: 지금까지 선택한 개수, start: 반복문의 시작값
          if k == L:
              print(choose)
              return
          for i in range(start, C):
              # i번째 정보를 저장
              choose.append(arr[i])
              a = b= 0
              if arr[k] in alpha: a = 1
              else: b = 1
              comb(k + 1, i + 1)
              choose.pop()
      
      L, C = map(int, input().split())
      arr = list(input().split())
      arr.sort()
      
      comb(0, 0)
      ```

      * 중복 순열 `3π2`

        ```python
        arr = 'ABC'
        N = len(arr)
        
        for i in range(N):
            for j in range(N):
        		print(arr[i], arr[j])
        ```

      * 순열 `3P2`

        ```python
        arr = 'ABC'
        N = len(arr)
        
        for i in range(N):
            for j in range(N):
                if i == j : continue
        		print(arr[i], arr[j])
        ```

      * 조합 `3C2`

        ```python
        arr = 'ABC'
        N = len(arr)
        
        for i in range(N):
            for j in range(i + 1, N):
        print(arr[i], arr[j])
        ```

      * 중복 조합 `3H2`

        ```python
        arr = 'ABC'
        N = len(arr)
        
        for i in range(N):
            for j in range(i, N):
        		print(arr[i], arr[j])
        ```

* 1697.숨박꼭질

  > BFS로 풀어야한다 -> DFS는 시간이 많이 걸린다.

  

* [14501.퇴사](https://www.acmicpc.net/problem/14501) - 최적해문제 / 바이너리 카운팅 / 백트래킹

  > 상담일들의 부분집합을 생성해서 각 상담기간이 겹치는 부분집합은 제외
  >
  > 상담기간이 겹치지 않는 부분집합에 포함된 상담일의 이익의 총합이 최대인 것을 찾는다.

  * 부분집합 - 바이너리 카운팅 : 선택일자들의 상담기간이 겹치는지 조사 / 백트래킹

  * 선생님 풀이 - 백트래킹

    ```python
    N = int(input())
    arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    def backtrack(day, p): # day: 결정할 일 p: 지금까지 이익
    
        if day > N + 1: return
        if day == N + 1:
            global ans
            ans = max(ans, p)
            return
        # 상담을 하는 경우
        backtrack(day + arr[day][0], p + arr[day][1])
        # 상담을 하지 않는 경우
        backtrack(day + 1, p)
    
    
    backtrack(1,0)
    print(ans)
    ```

    * DFS를 할 땐, 썻다 지웠다하고, BFS를 할 땐  `queue` 에 다 넣으면 된다.



# 190905

## 백준

1. [15686.치킨배달](https://www.acmicpc.net/problem/15686)

   * 백트래킹으로 풀어보기 - 시간 초과

     ```python
     N, M = map(int, input().split())
     city = [list(map(int, input().split())) for _ in range(N)]
     visit = []
     res = 0xffffff
     
     def chickenStore(row, col, store):
         global res
         if store > M: return
         if store == M:
             res = min(res, chickenLoad())
             return
         for r in range(N):
             for c in range(N):
                 if r < row or (r == row and c <= col):
                     continue
                 if city[r][c] == 2:
                     visit.append([r, c])
                     chickenStore(r, c, store + 1)
                     visit.pop()
                     chickenStore(r, c, store)
     def chickenLoad():
         total = 0
         for r in range(N):
             for c in range(N):
                 if city[r][c] == 1:
                     minDist = N*2
                     for cr, cc in visit:
                         minDist = min(minDist, abs(r - cr) + abs(c - cc))
                     total += minDist
         return total
     
     chickenStore(-1, -1, 0)
     print(res)
     ```

   * 집과 치킨집 위치를 따로 저장해서 반복을 없애기 - 시간초과

     ```python
     N, M = map(int, input().split())
     city = [list(map(int, input().split())) for _ in range(N)]
     visit = []
     home = []
     chicken = []
     res = 0xffffff
     
     def chickenStore(row, col, store):
         global res
         if store > M: return
         if store == M:
             res = min(res, chickenLoad())
             return
         for r, c in chicken:
             if r < row or (r == row and c <= col):
                 continue
             visit.append([r, c])
             chickenStore(r, c, store + 1)
             visit.pop()
             chickenStore(r, c, store)
             
     def chickenLoad():
         total = 0
         for r, c in home:
             minDist = N*2
             for cr, cc in visit:
                 minDist = min(minDist, abs(r - cr) + abs(c - cc))
             total += minDist
         return total
     
     for r in range(N):
         for c in range(N):
             if city[r][c] == 1:
                 home.append([r, c])
             if city[r][c] == 2:
                 chicken.append([r, c])
     chickenStore(-1, -1, 0)
     
     print(res)
     ```

   * 거리계산을 미리 리스트에 넣어서 반복을 없애기 - 성공!!

     ```python
     N, M = map(int, input().split())
     city = [list(map(int, input().split())) for _ in range(N)]
     visit = []
     home = []
     chicken = []
     res = 0xffffff
     
     def chickenStore(idx, last, store):
         global res
         global M
         if store > M: return
         if store == M:
             res = min(res, chickenLoad())
             return
         if idx < last:
             visit.append(idx)
             chickenStore(idx + 1, last, store + 1)
             visit.pop()
             chickenStore(idx + 1, last, store)
     
     def chickenLoad():
         total = 0
         for i in range(len(dist)):
             minDist = N*2
             for j in visit:
                 minDist = min(minDist, dist[i][j])
             total += minDist
         return total
     
     for r in range(N):
         for c in range(N):
             if city[r][c] == 1:
                 home.append([r, c])
             if city[r][c] == 2:
                 chicken.append([r, c])
     
     dist = [[] for _ in range(len(home))]
     for i in range(len(home)):
         for rr, cc in chicken:
             dist[i].append(abs(home[i][0] - rr) + abs(home[i][1] - cc))
     chickenStore(0, len(dist[0]), 0)
     
     print(res)
     ```

2. [17144.미세먼지안녕!](https://www.acmicpc.net/problem/17144)

   * 미세먼지 분포 알고리즘

     ```python
     import sys
     import operator
     
     sys.stdin = open('BJ_17144_input.txt', 'r')
     
     R, C, T = map(int, input().split())
     room = [list(map(int, input().split())) for _ in range(R)]
     spread = [[0 for _ in range(C)] for _ in range(R)]
     
     for r in range(R):
         for c in range(C):
             if room[r][c] > 0:
                 dust = room[r][c] // 5
                 for y, x in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                     if (r + y < 0 or r + y >= R) or (c + x < 0 or c + x >= C):
                         continue
                     if room[r + y][c + x] >= 0:
                         spread[r + y][c + x] += dust
                         room[r][c] -= dust
     for r in range(R):
         room[r] = list(map(operator.add,room[r],spread[r]))
     ```

   * **공기청정기 바람 추가 작성 필요!!**

     ```python
     
     ```

     