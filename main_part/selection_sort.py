def selection_sort(array):
    comparisons = 0
    for i in range(len(array)):
        min_indx = i
        for j in range(i+1, len(array)):
            comparisons += 1
            if array[j] < array[min_indx]:
                # comparisons += 1
                min_indx = j

        array[i], array[min_indx] = array[min_indx], array[i]

    return comparisons
