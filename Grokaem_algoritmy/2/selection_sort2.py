def smallest_elem(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = smallest_elem(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selection_sort([5, 3, 6, 2, 10]))