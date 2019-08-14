# 문자열 reverse

word = 'algorithm'
res = ''
for i in range(len(word) - 1, -1, -1):
    res += word[i]
print(res)

s = 'Reverse this strings'
res = s[::-1]
print(res)

# atio()함수 구현
# 반대
arr = '123456'
num = 0

for c in arr:
    num = num * 10 + (ord(c) - ord('0'))

print(num)

#atio
word = ''
word += num % 10
while num:
    word += num % 10
    num = num // 10
word = word[::-1]
print(word)

p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

# 1. 문자열.find() 사용
idx = t.find(p)
print(p)
print(t[idx:])


# 2. Brute-Force1
m, n = len(p), len(t)
for i in range(n - m + 1):
    j = 0
    while j < m:
        if p[j] != t[i + j]: break
        j += 1

    if j == m:
        print(t[i:])
        break


# 3. Brute-Force2
i = j = 0
while i < n:
    if p[j] != t[i]:
        i = i - j
        j = -1

    i, j = i + 1, j + 1
    if j == m:
        print(t[i- j:])
        break
