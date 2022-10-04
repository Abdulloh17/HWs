def binary_search(searchlist, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == searchlist[mid]:
        return mid

    if element < searchlist[mid]:
        return binary_search(searchlist, element, start, mid-1)
    else:
        return binary_search(searchlist, element, mid+1, end)

element = 28
searchlist = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

print(f'Searching for: {element}')
print(f'Index of {element}: {binary_search(searchlist, element, 0, len(searchlist))}')

def bubble_sort(list1):
    length = len(list1)
    for i in range(length):
        for j in range(0, length-i-1):
            if list1[j] > list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp

num = [4, 3, 7, 2, 9, 1]

bubble_sort(num)
print(num)




