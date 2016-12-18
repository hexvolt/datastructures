# A merge-sort algorithm workflow can be illustrated in the following steps:
# [5, 4, 0, 1, 3, 5, 6, 9]
# [5, 4, 0, 1] [3, 5, 6, 9]
# [5, 4] [0, 1] [3, 5] [6, 9]
# [5] [4] [0] [1] [3] [5] [6] [9]
# [4, 5] [0, 1] [3, 5] [6, 9]
# [0, 1, 4, 5] [3, 5, 6, 9]
# [0, 1, 3, 4, 5, 6, 9]
#
# Complexity: O(n*log n)


def merge(a, b):
    result = []
    
    while a and b:
        if a[0] <= b[0]:
            result.append(a[0])
            del a[0]
        else:
            result.append(b[0])
            del b[0]
    
    result += a + b
    
    return result 


def merge_sort(array):
    length = len(array)
    
    if length <= 1:
        return array
    
    split_point = length / 2
    
    left = merge_sort(array[:split_point])
    right = merge_sort(array[split_point:])
    
    return merge(left, right)    


if __name__ == '__main__':
    a = [5, 4, 0, 1, 3, 5, 6, 9]
    print(merge_sort(a))
