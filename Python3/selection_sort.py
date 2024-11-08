def selection_sort(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]
    return lst
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(int(input()))
print(selection_sort(arr))