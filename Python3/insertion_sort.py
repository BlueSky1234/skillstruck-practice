def insertion_sort(list1):
    insert_spot = 0 
    val_to_insert = 0

    for i in range(1, len(list1)):
        val_to_insert = list1[i]
        insert_spot = i

        while insert_spot > 0 and list1[insert_spot  - 1] > val_to_insert:
            list1[insert_spot] = list1[insert_spot - 1]
            insert_spot -= 1
        list1[insert_spot] = val_to_insert
    return list1

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(int(input()))

print(insertion_sort(arr))