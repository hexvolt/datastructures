# A quick-sort algorithm workflow can be illustrated in the following steps:
# a = [5, 4, 0, 1, 3, 5, 6, 9]
# a = [5, 4, 0, 1, 3, 5, 6| 9]
# a = [5, 4, 0, 1, 3, 5| 6, 9]
# a = [3, 4, 0, 1, 5, 5| 6, 9]
# a = [3, 4, 0, 1, 5| 5, 6, 9]
# a = [3, 4, 0, 1| 5, 5, 6, 9]
# a = [0, 4, 3, 1| 5, 5, 6, 9]
# a = [0, 1, 3, 4| 5, 5, 6, 9]
#
# Complexity: O(n*log n) - average, O(n^2) - worst case


def make_pivot(array, first, last):

    pivot = array[last]

    left = first
    right = last - 1

    while True:
        while array[left] < pivot and left < right:
            left += 1

        while array[right] >= pivot and left < right:
            right -= 1

        if left < right:
            array[left], array[right] = array[right], array[left]
        else:
            break

    if array[left] > pivot:
        # moving pivot to new position
        array[last], array[left] = array[left], array[last]

    return left


def quick_sort(array, first=0, last=None):

    last = (len(array) - 1) if last is None else last

    if first >= last:
        return

    split_point = make_pivot(array, first, last)

    quick_sort(array, first, split_point - 1)
    quick_sort(array, split_point + 1, last)


if __name__ == '__main__':
    array = [5, 4, 0, 1, 3, 5, 6, 9]
    print(array)

    quick_sort(array)
    print(array)
