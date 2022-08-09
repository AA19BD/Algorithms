
f = open('input.txt','r', encoding='utf-8')

list_of_9 = []
list_of_10 = []
list_of_11 = []

for line in f.read().split('\n'):
    new_line = line.split()
    if new_line[0] == '9':
        list_of_9.append(line)
    if new_line[0] == '10':
        list_of_10.append(line)
    if new_line[0] == '11':
        list_of_11.append(line)

sum_of_lists = list_of_9 + list_of_10 + list_of_11

# for i in sum_of_lists:
#     print(i)

with open('output.txt', 'w') as f:
    for i in sum_of_lists:
        print(i, end='\n',file=f)

f.close()