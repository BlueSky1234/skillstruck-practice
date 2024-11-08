def snail(snail_map):
    test = []
    test.extend(x for x in snail_map)
    if snail_map == [[]]:
        return []
    elif snail_map == [[1]]:
        return [1]
    else:
        result = []
        size = len(snail_map)
        while result != test:
            
            result.extend(snail_map[layer:stop])
            for x in snail_map[1:]:
                result.append(x[-1])
            result.extend(snail_map[-1][1::-1])
            for x in snail_map[(-1 * (size - 1)):1:-1]:
                result.append(x[0])
            layer += 1
            stop += 1
        return print(result)
    print(snail([[1,2,3],
         [8,9,4],
         [7,6,5]]))