import random

def quickSort(array):
    # call helper function    
    sortHelper(array, 0, len(array)-1)
    return array

     
def sortHelper(array, start, end):
    # base case -> only one element in array
    if start >= end:
        return

    # randomly pick 
    k = random.randint(start, end)
    swap(array, k, start)

    # instatiations
    key = array[start]
    left_idx = start + 1 
    right_idx = end
    last_dup = 0
    sim = 0
    #print("key:{}".format(key))
    # loop while left index is less than equals right
    while (left_idx < right_idx):
        # only swap when left is greater than and right is less than
        if array[left_idx] > key and array[right_idx] < key:
            swap(array, left_idx, right_idx)

        if array[left_idx] == key:
            # check if next is bigger
            swap(array, left_idx, left_idx + 1)
            sim += 1

        # if left is less than or equals increment
        if array[left_idx] < key:
            left_idx += 1


        if array[right_idx] == key:
            sim += 1
            # check if next is bigger
            swap(array, right_idx-1, right_idx)

        # if right is greater than or equals decrement
        if array[right_idx] > key:
            right_idx -= 1

    #print(array)
    
    #print("left_idx: {}".format(left_idx))
    #print("right_idx: {}".format(right_idx))
    # at end swap 
    #swap(array, start, right_idx)
    #print("fin")

    # check which side is smaller and 
    left_smaller = (right_idx-1-sim) -start < end-(right_idx + 1)

    # if left smaller.. sort smaller array first
    if left_smaller:
       sortHelper(array, start, right_idx-1-sim)
       sortHelper(array, right_idx+1, end)
    else:
       sortHelper(array, right_idx+1, end)
       sortHelper(array, start, right_idx-1-sim)
 
def swap(a, left, right):
    #print("left index: {}, right index:{}".format(left, right))
    a[left], a[right] = a[right], a[left]


if __name__ == "__main__":
    #cases
    #array = [3,2,3]
    array = [2, 3, 2, 2, 9, -1]
    #array = [-3,-2,2]
    #array = [-11,2,2,-3,-9,16]
    #array = [7, 6, 10, 5, 9, 2, 6, 1, 10, 6,-11,2,2,-3,-9,16,-3,-2,2,2, 3, 9, 2, 2]
    #array = [2, 3, 9, 2, 2]
    #array = [2, 3, 9, 2, 9]
    quickSort(array)

    print(array)