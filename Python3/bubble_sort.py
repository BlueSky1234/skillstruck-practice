def bubble_sort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1)-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(int(input()))

print(bubble_sort(arr))