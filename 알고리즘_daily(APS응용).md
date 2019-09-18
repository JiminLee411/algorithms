# 20190918

### SWEP

#### 1. [5185_이진수](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

* 방법

  1. 16진수 하나씩 뽑아서 그 숫자에 맞는 이진수로 변경

  2. 16 -> 10, 10 -> 2 라이브러리 사용

     * **Fail** (6/10)

       ```python
       for tc in range(1, int(input()) + 1):
           N, hex_num = map(str, input().split())
           num = int('0x'+ hex_num, 16)
           res = format(num, 'b')
           tmp = ''
           
           if len(res) % 4 != 0:
               for _ in range(4 - len(res) % 4):
                   tmp += '0'
               res = tmp + res
               
           print('#{} {}'.format(tc, res))
       ```

     * 입력이 `0X000` 일때, `0B0000` 출력되는 부분 보안 -> **Fail** (6/10)

       ```python
       for tc in range(1, int(input()) + 1):
           N, hex_num = map(str, input().split())
           num = int('0x'+ hex_num, 16)
           res = format(num, 'b')
           tmp = ''
           
           for i in hex_num:
               if i != '0':
                   break
               tmp += '0000'
           res = tmp + res
           tmp = ''
           
           for _ in range(4 - len(res) % 4):
               tmp += '0'
           res = tmp + res
           
           print('#{} {}'.format(tc, res))
       ```

     * **PASS** : 변환한 binary 길이가 4의 배수면 % 나머지가 4로 설정되는 것 발견!

       ```python
       for tc in range(1, int(input()) + 1):
           N, hex_num = map(str, input().split())
           num = int('0x'+ hex_num, 16)
           res = format(num, 'b')
           tmp = ''
           
           if len(res) % 4 != 0:
               for _ in range(4 - len(res) % 4):
                   tmp += '0'
               res = tmp + res
               
           print('#{} {}'.format(tc, res))
       ```

       

#### 2. [5186_이진수2](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do#none)

* **PASS** : 10진수 -> 2진수 변환하는 방식으로 알고리즘 구현

  ```python
  for tc in range(1, int(input()) + 1):
      num = float(input())
      num_tmp = num
      tmp = ''
      i = -1
      while num_tmp > 0:
          if len(tmp) == 13:
              tmp = 'overflow'
              break
          if num_tmp >= 2 ** i:
              num_tmp -= 2 ** i
              tmp += '1'
          else:
              tmp += '0'
              
          i -= 1
          
      print('#{} {}'.format(tc, tmp))
  ```



#### 3. [1240_단순이진암호코드]([https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWw8omwKmQQDFAUD&contestProbId=AV15FZuqAL4CFAYD&probBoxId=AW1CLuJK37kDFARC&type=PROBLEM&problemBoxTitle=01.Start%289%EC%9B%9418%EC%9D%BC%2F19%EC%9D%BC%29&problemBoxCnt=3](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWw8omwKmQQDFAUD&contestProbId=AV15FZuqAL4CFAYD&probBoxId=AW1CLuJK37kDFARC&type=PROBLEM&problemBoxTitle=01.Start(9월18일%2F19일)&problemBoxCnt=3)

* **PASS** : 해독표를 `dictionary` 형식으로 저장

  ```python
  def Decoding(r, c):
      totalCode = arr[r][c-55:c+1]
      tmp = [0,0]
  
      decodeTable = {'0001101': 0,
                   '0011001': 1,
                   '0010011': 2,
                   '0111101': 3,
                   '0100011': 4,
                   '0110001': 5,
                   '0101111': 6,
                   '0111011': 7,
                   '0110111': 8,
                   '0001011': 9}
  
      for i in range(4):
          tmp[0] += decodeTable[totalCode[7*(i+1)*2 - 14 : 7*(i+1)*2 - 7]]
          tmp[1] += decodeTable[totalCode[7*(i+1)*2 - 7 : 7*(i+1)*2]]
  
      return 0 if (tmp[0] * 3 + tmp[1]) % 10 != 0 else tmp[0] + tmp[1]
  
  
  for tc in range(1, int(input()) + 1):
      N, M = map(int, input().split())
      arr = [input() for _ in range(N)]
      for r in range(N):
          last = 0
          for c in range(M-1, 0, -1):
              if arr[r][c] == '1':
                  last = 1
                  break
          if last == 1:
              break
  
      res = Decoding(r, c)
      print('#{} {}'. format(tc, res))
  ```

* **변경** : def를 추가하여 메모리와 시간을 줄였다. (코드길이가 늘어남)

  ```python
  def FindCode():
      N, M = map(int, input().split())
      arr = [input() for _ in range(N)]
  
      for r in range(N):
          last = 0
          for c in range(M-1, 0, -1):
              if arr[r][c] == '1':
                  last = 1
                  break
          if last == 1:
              break
      totalCode = arr[r][c-55:c+1]
  
      return Decoding(totalCode)
  
  
  def Decoding(totalCode):
      tmp = [0, 0]
  
      decodeTable = {'0001101': 0,
                   '0011001': 1,
                   '0010011': 2,
                   '0111101': 3,
                   '0100011': 4,
                   '0110001': 5,
                   '0101111': 6,
                   '0111011': 7,
                   '0110111': 8,
                   '0001011': 9}
  
      for i in range(4):
          tmp[0] += decodeTable[totalCode[7*(i+1)*2 - 14 : 7*(i+1)*2 - 7]]
          tmp[1] += decodeTable[totalCode[7*(i+1)*2 - 7 : 7*(i+1)*2]]
  
      return 0 if (tmp[0] * 3 + tmp[1]) % 10 != 0 else tmp[0] + tmp[1]
  
  
  for tc in range(1, int(input()) + 1):
      res = FindCode()
  
      print('#{} {}'. format(tc, res))
  ```



#### [4. 4366_정식이의은행업무]([https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AWMeRLz6kC0DFAXd&solveclubId=AWw8omwKmQQDFAUD&problemBoxTitle=01.Start%289%EC%9B%9418%EC%9D%BC%2F19%EC%9D%BC%29&problemBoxCnt=3&probBoxId=AW1CLuJK37kDFARC](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AWMeRLz6kC0DFAXd&solveclubId=AWw8omwKmQQDFAUD&problemBoxTitle=01.Start(9월18일%2F19일)&problemBoxCnt=3&probBoxId=AW1CLuJK37kDFARC)

* **PASS** : 하나씩 변경해가면서 비교

  ```python
  def Comp(bNum, tNum):
      bLen = len(bNum)
      tLen = len(tNum)
  
      for bit in range(bLen):
          if bNum[bit] == '1':
              bTmp = '0b' + bNum[0:bit] + '0' + bNum[bit + 1:len(bNum)]
          else:
              bTmp = '0b' + bNum[0:bit] + '1' + bNum[bit + 1:len(bNum)]
          dTmp = int(bTmp, 2)
  
          for tri in range(tLen):
              for i in range(3):
                  tTmp = tNum[0:tri] + str(i) + tNum[tri + 1:len(tNum)]
                  dTmp2 = 0
                  for j in range(tLen):
                      dTmp2 += 3**(tLen - j - 1) * int(tTmp[j])
  
                  if dTmp == dTmp2:
                      return dTmp
  
                  
  for tc in range(1, int(input()) + 1):
      bNum = input()
      tNum = input()
      
      res = Comp(bNum, tNum)
      
      print(res)
  ```

  

