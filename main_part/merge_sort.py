comparisons = 0


def test_merge(array):
    merge_sort(array)
    return comparisons


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    global comparisons
    result = []
    left_pointer = 0
    right_pointer = 0

    while (left_pointer < len(left) and right_pointer < len(right)):
        if left[left_pointer] < right[right_pointer]:
            comparisons += 1
            result.append(left[left_pointer])
            left_pointer += 1

        else:
            comparisons += 1
            result.append(right[right_pointer])
            right_pointer += 1

    return result + right[right_pointer:] + left[left_pointer:]
