arr = 'ABC'
bits = [0] * n

for i in range(2):
    bits[0] = i
    for i in range(2):
        bits[1] = i
        for i in range(2):
            bits[2] = i
            print(bits, end='> ')
            for i in range(len(bits)):
                if bits[i]: print(arr[i], end=' ')
            print()

def subset(k, n):
    if k == n:
        print(bits, end='> ')
        for i in range(len(bits)):
            if bits[i]: print(arr[i], end=' ')
        print()
        return

    for i in range(2):
        bits[k] = i
        # 재귀 호출
        subset(k + 1, n)