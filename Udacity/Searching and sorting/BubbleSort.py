




def BubbleSort(list: list[int])->list[int]:#O(n^2), Space complexity of O(1).
    for i in range(0,len(list)-1):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list


num = [5, 3, 8, 6, 7, 2]
print(f" BubbleSort's result {BubbleSort(num)}")