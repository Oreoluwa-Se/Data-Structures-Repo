# Uses python3
import sys

def func(array):
    if not len(array):
        return

    elif len(array) == 1:
        return array[0]

    # base case
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])

    return maxSums[-1]

def funcOpt(array):
    if not len(array):
        return

    elif len(array) == 1:
        return array[0]

    # base case
    second = array[0]
    first  = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second, first = first, second

    return first


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
