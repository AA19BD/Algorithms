n = int(input())
for _ in range(n):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word[1: len(word) - 1])) + word[len(word) - 1], end='\n')
    else:
        print(word, end ='\n')