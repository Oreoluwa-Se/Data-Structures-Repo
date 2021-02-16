# Uses python3
import sys

def func(array, div=3):
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

    print(length)
    #buildSequence(array, sorted_array, length)

#def buildSequence(array, sorted_array, length):
#    sequence = []
#    ignore_seq = []

    # indexing valuex
#    row = len(array)
#    col = len(array[0]) - 1

    # maximum value
#    max_val = array[-1][-1]

    # buiding sequence 
#    while length > 0:
#        number_len = []

        # append current index and ignore_seq
#        number_len.append(sorted_array[row])
#        ignore_seq.append(sorted_array[row])

#        while col > 0:
            # column index
#            col = col - sorted_array[row]

            # check value
#            check_val = array[row][col]

            # checks while the value above is same as current value and we haven't added it yet
#            while array[row - 1][col] == check_val and sorted_array[row -1] not in ignore_seq and row > 0:
#                row -= 1

            # append current index and ignore_seq
#            number_len.append(sorted_array[row])
#            ignore_seq.append(sorted_array[row])


        # decrement length
#        length -= 1










if __name__ == '__main__':
    #array = [1, 7, 2, 8, 3, 6, 5]
    array = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
    #array = [3, 3, 3, 3]
    #array = [40]

    func(array)