import math


def selection_sort(arr: list):
    """
    sorting in ascending order (increasing).
    in short, the algorithm works by selecting the smallest number and move it to the beginning of the
    array, and then finding the second-smallest number and move it next to the first smallest.
    Doing so for every item in the array we will end up with a sorted array.
    """
    array_length = len(arr)
    # indicating the largest position in the sorted section
    current_sorted = 0

    # 10 5 2 1 3

    while current_sorted < array_length - 1:
        current_num = arr[current_sorted]
        smallest = math.inf
        smallest_index = 0
        for k in range(current_sorted, array_length):
            num = arr[k]
            if num < smallest:
                smallest_index = k
                smallest = num
        # swap smallest with the current num
        arr[current_sorted] = smallest
        arr[smallest_index] = current_num
        current_sorted += 1

    return arr


def test_selection_sort():
    test_array = [10, 5, 1, 3, 0]
    print("original:   ", test_array)
    selection_sort(test_array)
    print("bubble sort:", test_array)


if __name__ == "__main__":
    test_selection_sort()




