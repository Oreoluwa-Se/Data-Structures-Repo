# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # returns index
    return binary_search_helper(a, left, right, x)


def binary_search_helper(a, left, right, key):
    """
        Takes sorted array and  compares middle value with key 
    """
    # pre check -> empty list, or key not in array
    if not a:
        return -1

    # handling cases where the value is not in the array
    if key > a[-1]:
        return -1

    if key < a[0]:
        return -1


    #loop until left side equals the right side
    while left <= right:
        # calculate mid point
        mid_ = left + ((right - left) // 2)

        if a[mid_] == key:
            return mid_

        # comparison -> if less than
        elif key < a[mid_]:
            right = mid_ - 1

        else:
            left = mid_ + 1

    # if at the end return -1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
