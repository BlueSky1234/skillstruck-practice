def merge_sort(list1):
    if len(list1)  > 1:
        mid = len(list1)//2
        L = list1[:mid]
        R = list1[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list1[k] = L[i]
                i += 1
            else:
                list1[k] = R[j]
                j +=1
            k+=1
        while i < len(L):
            list1[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list1[k] = R[j]
            j += 1
            k += 1

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(int(input()))
merge_sort(arr)
print(arr)