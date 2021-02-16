# Uses python3
import sys
import random

def randomized_quick_sort(array, start, end):
    # base case -> only one element in array
    if start >= end:
        return

    # randomly pick 
    k = random.randint(start, end)
    swap(array, k, start)

    # call the partitioner
    left_idx, right_idx = partitioner(array, start, end)

    # check which side is smaller and 
    left_smaller = (right_idx-1) -start < end-left_idx

    # if left smaller.. sort smaller array first
    if left_smaller:
        randomized_quick_sort(array, start, right_idx-1)
        randomized_quick_sort(array, left_idx, end)
    else:
        randomized_quick_sort(array, left_idx, end)
        randomized_quick_sort(array, start, right_idx-1)



def partitioner(array, start, end):
    # instatiations
    key = array[start]
    left_idx = start + 1 
    right_idx = end

    # locator
    track = [0]*len(array)

    # loop while left index is less than equals right
    while (left_idx <= right_idx):
        # only swap when left is greater than and right is less than
        if array[left_idx] > key and array[right_idx] <key:
            swap(array, left_idx, right_idx)

        if array[left_idx] == key:
            track[left_idx] = 1
            
        # if left is less than or equals increment
        if array[left_idx] <= key:
            left_idx += 1

        if array[right_idx] == key:
            track[right_idx] = 1

        # if right is greater than or equals decrement
        if array[right_idx] >= key:
            right_idx -= 1

    # at end swap 
    swap(array, start, right_idx)
    swap(track, start, right_idx)
    
    if sum(track) >0:
        left_idx, right_idx = org(track, array, right_idx)

    return left_idx, right_idx

def swap(a, left, right):
    
    a[left], a[right] = a[right], a[left]

def org(track, array, key_loc):
    
    left_idx, right_idx = key_loc+1, key_loc-1

    for i in range(len(track)):
        if track[i]:
            if i < key_loc and right_idx > 0:
                swap(array, i, right_idx)
                right_idx -= 1 
                

            elif i > key_loc and left_idx < len(array):
                swap(array, i, left_idx)
                left_idx += 1

    left_idx = min(len(array)-1, left_idx-1)
    right_idx = max(0,right_idx +1)
    
    return  left_idx, right_idx

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
