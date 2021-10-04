import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
size = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
# size = [i for i in range(6, 14)]


def read_data(filename):
    dataset = []
    with open(filename, 'r') as data:
        for line in data:
            one_test = list(map(lambda x: x.strip(), line.split(', ')))
            dataset.append(one_test)

    return dataset


def data_avg(alg_name, dataset):
    alg_random = list(filter(lambda x: x[0] == alg_name, dataset))
    alg_random_avg_time = []
    alg_random_avg_comparisons = []

    for size_num in size:
        current_size_time = []
        current_size_comprarisons = []
        for test in alg_random:
            if int(test[1]) == size_num:
                current_size_time.append(float(test[2]))
                current_size_comprarisons.append(int(test[3]))

        alg_random_avg_time.append(
            sum(current_size_time)/len(current_size_time))
        alg_random_avg_comparisons.append(
            int(sum(current_size_comprarisons)/len(current_size_comprarisons)))

    return (alg_random_avg_time, alg_random_avg_comparisons)


def visualisation(filename, type, expetiment_title, save_to):
    '''
    type = 0 for execution time visualization
    type = 1 for No. of comparisons visualization

    '''
    dataset = read_data(filename)
    merge = data_avg('MERGE', dataset)
    insertion = data_avg('INSERTION', dataset)
    selection = data_avg('SELECTION', dataset)
    shell = data_avg('SHELL', dataset)

    # SMOOTH LINES
    from scipy.interpolate import make_interp_spline
    sizenew = np.linspace(np.array(size).min(), np.array(size).max(), 200) 
    spl = make_interp_spline(size, merge[type], k=3)
    merge_smooth = spl(sizenew)
    plt.yscale("log")
    plt.plot(sizenew, merge_smooth, label='Merge sort', color="b")

    sizenew = np.linspace(np.array(size).min(), np.array(size).max(), 200) 
    spl = make_interp_spline(size, insertion[type], k=3)
    merge_smooth = spl(sizenew)
    plt.yscale("log")
    plt.plot(sizenew, merge_smooth, label='Insertion sort', color="r")

    sizenew = np.linspace(np.array(size).min(), np.array(size).max(), 200) 
    spl = make_interp_spline(size, selection[type], k=3)
    merge_smooth = spl(sizenew)
    plt.yscale("log")
    plt.plot(sizenew, merge_smooth, label='Selection sort', color="y")

    sizenew = np.linspace(np.array(size).min(), np.array(size).max(), 200) 
    spl = make_interp_spline(size, shell[type], k=3)
    merge_smooth = spl(sizenew)
    plt.yscale("log")
    plt.plot(sizenew, merge_smooth, label='Shell sort', color="c")

    # ORDINARY LINES
    # plt.plot(size, merge[type], label='Merge sort')
    # plt.plot(size, insertion[type], label='Insertion sort')
    # plt.plot(size, selection[type], label='Selection sort')
    # plt.plot(size, shell[type], label='Shell sort')



    if type == 0:
        plt.ylabel('Execution time')
    else:
        plt.ylabel('No. of comparisons')

    plt.xlabel('Array size')
    plt.title(expetiment_title)
    plt.legend()
    # plt.show()
    plt.savefig(f'img/{save_to}.png', transparent=True)

    return


if __name__ == "__main__":
    print('Visualisation part')
    # Uncomment certain lines if you want to run testing
    # visualisation('random_arrays.csv', 0, 'EXPERIMENT 1\nRandom array', 'exp_1_random_time')
    # visualisation('random_arrays.csv', 1, 'EXPERIMENT 1\nRandom array', 'exp_1_random_comparisons')
    # visualisation('increasing_arrays.csv', 0, 'EXPERIMENT 2\nIncreasing array', 'exp_2_increasing_time')
    # visualisation('increasing_arrays.csv', 1, 'EXPERIMENT 2\nIncreasing array', 'exp_2_increasing_comparisons')
    # visualisation('decreasing_arrays.csv', 0, 'EXPERIMENT 3\nDecreasing array', 'exp_3_decreasing_time')
    # visualisation('decreasing_arrays.csv', 1, 'EXPERIMENT 3\nDecreasing array', 'exp_3_decreasing_comparisons')
    # visualisation('set_of_three.csv', 0, 'EXPERIMENT 4\n{1, 2, 3} array', 'exp_4_set_of_three_time')
    # visualisation('set_of_three.csv', 1, 'EXPERIMENT 4\n{1, 2, 3} array', 'exp_4_set_of_three_comparisons')
