arr = 'ABCD'
N = 4

for set in range(1 << N):
    A, B = [], []
    for i in range(N):
        if set & (1 << i):
            A.append(arr[i])
        else:
            B.append(arr[i])
    if len(A) == len(B):
        print(A, B)