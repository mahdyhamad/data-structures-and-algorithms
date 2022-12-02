def bubble_sort(arr: list):
    # sorting in ascending order (increasing)
    array_length = len(arr)
    # array with one item can not be sorted
    if array_length == 1:
        return arr

    for _ in range(array_length - 1):
        i = 0
        j = 1
        for k in range(array_length - 1):
            first_item = arr[i]
            second_item = arr[j]
            if first_item > second_item:
                # swap
                arr[i] = second_item
                arr[j] = first_item
            i += 1
            j += 1
    return arr


def test_bubble_sort():
    test_array = [10, 5, 1, 3, 0]
    print("original:   ", test_array)
    bubble_sort(test_array)
    print("bubble sort:", test_array)


if __name__ == "__main__":
    test_bubble_sort()

