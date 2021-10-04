def shell_sort(array):
    comparisons = 0
    gap = len(array) // 2
    while gap > 0:
        for i in range(gap, len(array)):
            current = array[i]
            j = i
            comparisons += 1
            while j >= gap and array[j - gap] > current:
                comparisons += 1
                array[j] = array[j - gap]
                j -= gap

            array[j] = current
        gap = gap // 2

    return comparisons
