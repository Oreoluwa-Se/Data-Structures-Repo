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

    # loop while left index is less than equals right
    while (left_idx <= right_idx):
    	# only swap when left is greater than and right is less than
    	if array[left_idx] > key and array[right_idx] <key:
    		swap(array, left_idx, right_idx)

    	# if left is less than or equals increment
    	if array[left_idx] <= key:
    		left_idx += 1

    	# if right is greater than or equals decrement
    	if array[right_idx] >= key:
    		right_idx -= 1

    # at end swap 
    swap(array, start, right_idx)

    # check which side is smaller and 
    left_smaller = (right_idx-1) -start < end-(right_idx + 1)

    # if left smaller.. sort smaller array first
    if left_smaller:
    	sortHelper(array, start, right_idx-1)
    	sortHelper(array, right_idx+1, end)
    else:
    	sortHelper(array, right_idx+1, end)
    	sortHelper(array, start, right_idx-1)
 
def swap(a, left, right):
    #print("left index: {}, right index:{}".format(left, right))
    a[left], a[right] = a[right], a[left]