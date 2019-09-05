import copy
def find(arr_1, arr_2, arr_3):
    n = copy.deepcopy(arr_1)
    if len(n) == N + (N-1):
        result.append(n)
    else:
        if not arr_1:
            arr_1.append(arr_2.pop(0))
            find(arr_1, arr_2, arr_3)
        else:
            if sum(arr_3) != 0:
                for i in range(len(arr_3)):
                    if arr_3[i] != 0:
                        arr_3[i] -= 1
                        arr_1.append(y_m[i])
                        arr_1.append(arr_2.pop(0))
                        find(arr_1,arr_2, arr_3)
                        arr_2.insert(0, arr_1.pop())
                        arr_1.pop()
                        arr_3[i] += 1
            else:
                arr_1.append(arr_2.pop())
                find(arr_1, arr_2, arr_3)
                arr_2.append(arr_1.pop())

def cal(arr_s):
    imsi = []
    print(len(arr_s))
    for i in arr_s:
        a = 0
        b = ''
        for j in i:
            if str(j).isdigit():
                if not a :
                    if b == '-':
                        a -= j
                    elif b == '+':
                        a += j
                    elif b == 'x' or b == '/':
                        a = 0
                    else:
                        a = j
                else:
                    if b == '+':
                        a = a + j
                    elif b == '-':
                        a = a - j
                    elif b == 'x':
                        a = a * j
                    elif b == '/':
                        if a >= 0:
                            a = a // j
                        else:
                            a = -(abs(a) // j)
                    b = ''
            else:
                b = j
        imsi.append(a)
    print(max(imsi), min(imsi))
N = int(input())
base = list(map(int, input().split()))
y_m = ['+','-','x','/']
y_n = list(map(int, input().split()))
result = []
sick = []
find(sick, base, y_n)
cal(result)