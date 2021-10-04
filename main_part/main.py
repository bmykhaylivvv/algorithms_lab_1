import random
from time import time
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import test_merge
from shell_sort import shell_sort


def test_sort_algorithm(algorithm, algorithm_name, array, size):
    start_time = time()
    comparisons = algorithm(array)
    processing_time = time() - start_time

    data_string = f'{algorithm_name}, {size}, {processing_time}, {comparisons}'
    return data_string


def create_array(size, increasing=False, decreasing=False, set_of_three=False):
    if increasing:
        return sorted([random.choice([i for i in range(size)]) for _ in range(size)])

    elif decreasing:
        return sorted([random.choice([i for i in range(size)]) for _ in range(size)])[::-1]

    elif set_of_three:
        return [random.choice([1, 2, 3]) for _ in range(size)]

    else:
        return [random.choice([i for i in range(size)]) for _ in range(size)]


def random_array_test():

    with open('random_arrays.csv', 'w') as random_arrays:

        for _ in range(5):
            size = 2**7
            while size <= 2**15:
                print(size)

                print('Creating array')
                array = create_array(size)
                print('Array has been created')

                random_arrays.write(test_sort_algorithm(
                    selection_sort, 'SELECTION', array.copy(), size) + "\n")
                random_arrays.write(test_sort_algorithm(
                    insertion_sort, 'INSERTION', array.copy(), size) + "\n")
                random_arrays.write(test_sort_algorithm(
                    test_merge, 'MERGE', array.copy(), size) + "\n")
                random_arrays.write(test_sort_algorithm(
                    shell_sort, 'SHELL', array.copy(), size) + "\n")

                size *= 2


def increasing_array_test():

    with open('increasing_arrays.csv', 'w') as increasing_arrays:
        size = 2**7

        while size <= 2**15:
            print(size)


            print('Creating array')
            array = create_array(size, increasing=True)
            print('Array has been created')

            increasing_arrays.write(test_sort_algorithm(
                selection_sort, 'SELECTION', array.copy(), size) + "\n")
            increasing_arrays.write(test_sort_algorithm(
                insertion_sort, 'INSERTION', array.copy(), size) + "\n")
            increasing_arrays.write(test_sort_algorithm(
                test_merge, 'MERGE', array.copy(), size) + "\n")
            increasing_arrays.write(test_sort_algorithm(
                shell_sort, 'SHELL', array.copy(), size) + "\n")

            size *= 2


def decreasing_array_test():

    with open('decreasing_arrays.csv', 'w') as decreasing_arrays:
        size = 2**7

        while size <= 2**15:
            print(size)


            print('Creating array')
            array = create_array(size, decreasing=True)
            print('Array has been created')

            decreasing_arrays.write(test_sort_algorithm(
                selection_sort, 'SELECTION', array.copy(), size) + "\n")
            decreasing_arrays.write(test_sort_algorithm(
                insertion_sort, 'INSERTION', array.copy(), size) + "\n")
            decreasing_arrays.write(test_sort_algorithm(
                test_merge, 'MERGE', array.copy(), size) + "\n")
            decreasing_arrays.write(test_sort_algorithm(
                shell_sort, 'SHELL', array.copy(), size) + "\n")

            size *= 2


def set_of_three_array_test():

    with open('set_of_three.csv', 'w') as set_of_three_arrays:

        for _ in range(3):
            size = 2**7
            while size <= 2**15:
                print(size)

                print('Creating array')
                array = create_array(size)
                print('Array has been created')

                set_of_three_arrays.write(test_sort_algorithm(
                    selection_sort, 'SELECTION', array.copy(), size) + "\n")
                set_of_three_arrays.write(test_sort_algorithm(
                    insertion_sort, 'INSERTION', array.copy(), size) + "\n")
                set_of_three_arrays.write(test_sort_algorithm(
                    test_merge, 'MERGE', array.copy(), size) + "\n")
                set_of_three_arrays.write(test_sort_algorithm(
                    shell_sort, 'SHELL', array.copy(), size) + "\n")

                size *= 2


def main():
    # print('--- TEST 1 is running ---')
    # random_array_test()
    # print('--- TEST 2 is running ---')
    # increasing_array_test()
    # print('--- TEST 3 is running ---')
    # decreasing_array_test()
    # print('--- TEST 4 is running ---')
    # set_of_three_array_test()


if __name__ == "__main__":
    main()
