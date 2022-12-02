def insertion_sort(arr: list):
    # soring in ascending order
    """
    insertion sort works by incrementally sorting the left part of the array.
    we select the first element of the array as our starting point and compare
    it with its adjacent element, if it is smaller, we keep moving it to the left
    until no element is smaller to it (to its left). Doing so for every element in
    the array, we end up with a sorted array.
    """

    array_length = len(arr)
    current = 0

    while current < array_length:
        if current == 0:
            pass
        else:
            i = current
            while i > 0:
                if arr[i] < arr[i-1]:
                    # swap
                    temp = arr[i]
                    arr[i] = arr[i-1]
                    arr[i-1] = temp
                    i -= 1
                else:
                    break
        current += 1
    return arr


if __name__ == '__main__':
    insertion_sort(arr)