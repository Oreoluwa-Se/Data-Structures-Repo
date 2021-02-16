# Uses python3
import sys

def get_number_of_inversion(array, b, left, right):
    if len(array) <=1:
        return 0

    _, count = get_number_of_inversions_v1(array)
    
    return count



def get_number_of_inversions_v1(array):
    tot_count = 0
    # at base case return array
    if len(array) == 1:
        return array, 0

    # calculate mid point
    mid = len(array)// 2

    # traverse left side, and right side
    left_side, left_count = get_number_of_inversions_v1(array[:mid])
    right_side, right_count = get_number_of_inversions_v1(array[mid:])
    #print("left_side: {}".format(left_side))
    #print("right_side: {}".format(right_side))
    # sort and calculate inv
    array, inv_count = mergedSorted(left_side, right_side)
    

    tot_count += (inv_count + left_count + right_count)

    # merged
    return array, tot_count

def mergedSorted(left_side, right_side):
    inv_count = 0

    sorted_ = [None]*(len(left_side) + len(right_side)) 
    # counter
    k =i = j = 0
    
    idx = 0

    # loop for inv count
    for i in range(len(left_side)):
        #print("left : {}".format(left_side[i]))
        #print("right : {}".format(right_side[idx]))
        for idx in range(len(right_side)):
            if left_side[i] > right_side[idx]:
                inv_count += 1 



    # loop begins
    while i < len(left_side) and j < len(right_side):
        # check if left side is bigger than right side
        #print("left_side: {}, right_side: {}".format(left_side[i], right_side[j]))      

        if left_side[i] <= right_side[j] :
            sorted_[k] = left_side[i]
            i += 1
        else:
            sorted_[k] = right_side[j]
            #inv_count += 1
            j += 1

        k += 1

    # finish loop on left side
    while i < len(left_side):
        # look for internal inv_counts
        #if  left_side[i] > left_side[i-1]:
         #   print("here left side prev > next")
          #  inv_count += 1

        # insert into k
        sorted_[k] = left_side[i]
        i += 1
        k += 1

    # finish loop on right side
    while j < len(right_side):
        #print(j)
        # look for internal inv_counts
        #if right_side[j] > right_side[j-1]:
         #   print("here right side prev > next")
          #  inv_count += 1

        # insert into sorted
        sorted_[k] = right_side[j]
        j += 1
        k += 1

    return sorted_, inv_count




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    b=0
    #b = 1 *[0]
    #a = [2, 3, 9, 2, 9]
    print(get_number_of_inversion(a, b, 0, len(a)))
