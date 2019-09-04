## 190904

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

  

* 14501.퇴사 - 최적해문제 / 바이너리 카운팅 / 백트래킹

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