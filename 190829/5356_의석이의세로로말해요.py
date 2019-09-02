import sys

sys.stdin = open('5356_input.txt', 'r')
for t in range(1, int(input()) + 1):
    words = []
    max_word = 0
    for _ in range(5):
        word = input()
        max_word = max(max_word,len(word))

        words.append(word)
        for c in range(max_word):
            for r in range(5):
                if len(words[r]) <= c:
                    continue
                else:
                    print(words[r][c], end='')

    print()