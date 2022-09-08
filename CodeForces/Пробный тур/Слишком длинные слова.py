n = int(input())
for _ in range(n):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word[1: len(word) - 1])) + word[len(word) - 1], end='\n')
    else:
        print(word, end ='\n')

count_word = int(input())
res = str()
while count_word >= 0:
    word = str(input())
    if len(word) > 10:
        res += word[0] + str(len(word)-2) + word[len(word)-1] + "\n"
    else:
        res += word + "\n"
    count_word -= 1

print(res)