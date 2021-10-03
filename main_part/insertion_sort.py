def insertion_sort(array):
    comparisons = 0
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            comparisons += 1
            # move all element larger than key one position right
            array[j + 1] = array[j]
            j -= 1

        # Put key on its suitable place
        # EXAMPLE
        # [2, 1]
        # 1) i = 0 -- skip
        # 2) i = 1
        #     key = array[i]
        #     j = 0
        #     key[i] < array[j] and j >= 0
        #     j -= 1 (j == -1)
        #     array[j + 1] = array[-1 + 1] =  array[0] = key

        array[j + 1] = key
    
    return comparisons