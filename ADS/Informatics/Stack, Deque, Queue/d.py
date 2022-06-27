<<<<<<< HEAD
with open('./d.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    sorted_list_9 = []
    sorted_list_10 = []
    sorted_list_11 = []
    for i in range(len(lines)):
        if lines[len(lines)-1] == lines[i]:
            lines[i] += '\n'
        if lines[i].split()[0] == '9':
            sorted_list_9.append(lines[i])
        if lines[i].split()[0] == '10':
            sorted_list_10.append(lines[i] )
        if lines[i].split()[0] == '11':
            sorted_list_11.append(lines[i])


    sum_of_sorted_lists = sorted_list_9 + sorted_list_10 + sorted_list_11
    print(*sum_of_sorted_lists, sep = '')










    f.close()
=======
f = open('d.txt','r')
d = dict()

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

for i in sum_of_lists:
    print(i)

# with open('d.txt', 'w') as f:
#     for i in sum_of_lists:
#         print(i, end='\n',file=f)
#
f.close()
>>>>>>> 675f5f5296ef812815d41748a2bbe08c7eb58d52
