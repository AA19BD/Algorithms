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