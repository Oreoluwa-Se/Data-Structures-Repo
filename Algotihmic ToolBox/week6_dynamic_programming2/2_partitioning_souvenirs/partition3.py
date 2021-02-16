# Uses python3
import sys
import itertools

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def function(array, div=3):
    # base case
    if sum(array) % div != 0:
        return 0

    # find the sim we are looking for
    else:
        split_count = sum(array)//div

    # sort array of values
    sorted_array = sorted(array)

    # create array
    search_array = [[0 for x in range(split_count + 1)] for y in range(len(sorted_array) + 1)]

    # length tracker
    length = 0

    # loop through the array twice
    for row in range(1, len(sorted_array) + 1):
        # row value
        row_val = sorted_array[row - 1] 

        for col in range(1, split_count + 1):
            # cases where the row value is greater than current col
            if row_val > col:
                search_array[row][col] = search_array[row - 1][col]
            else:
                search_array[row][col] = max(search_array[row - 1][col], 
                    row_val + search_array[row - 1][col - row_val])

            if search_array[row][col] == split_count:
                length +=1
    
    # return final
    if length >= 3:
        return 1
    else:
        return 0 


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(function(A))

