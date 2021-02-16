# Uses python3
import sys

#def get_majority_element(a, left, right):
#    if left == right:
#        return -1
#    if left + 1 == right:
#       return a[left]
    #write your code here
#    return -1

def get_majority_element_faster(a, left, right):
    # create dictionary
    unique = set(a)

    # if no unique return 0
    if len(unique) == len(a):
        return 0

    # all the same in the array
    if len(unique) == 1:
        return 1

    # turn list to dictionary
    count_dict = dict.fromkeys(unique, 0)

    # loop array
    for num in a:
        count_dict[num] += 1

    # check if max value is less than halfof the length
    if max(count_dict.values()) > len(a) // 2:
        return 1

    return 0

def get_majority_element_comment(a, left, right):
    # printouts
    print("left: {}".format(left))
    print("right: {}".format(right))
    print("array: {}".format(a[left:right+1]))

    # base case is only one thing left
    if left == right:
        print("returned value: {}".format(a[left]))
        print("=========")
        print(" ")
        return a[left]

    # splitting criteria
    mid = left + (right - left) // 2
    print("array length: {}".format(len(a[left:right+1])))
    print("value: {}, location: {}".format(a[mid], mid))
    print("=========")
    print(" ")
    # left side run
    left_side = get_majority_element(a, left, mid)
    print("left_side: {}".format(left_side))

    right_side = get_majority_element(a, mid+1, right)
    print("right_side: {}".format(right_side))

    # if left and right return the same
    if left_side == right_side:
        print("left_right equal:{}".format(left_side))
        print("=========")
        print(" ")
        return left_side
    else:
        print("left_side: {}, right_side: {}".format(left_side, right_side))
        # count majority between secitons
        l_count = count_maj(a, left, mid, left_side)
        r_count = count_maj(a, mid + 1, right, right_side)  
        if l_count > r_count:
            print("left_side majority, value: {}\n".format(left_side))
            return left_side
        elif l_count < r_count:
            print("right_side majority, value: {}\n".format(right_side))
            return right_side
        else:
            print("Tie..so we take average, value: {}\n".format(right_side))
            return 0.5*(right_side + left_side)

def get_majority_element(a, left, right):
    #extract majority element
    if len(set(a)) != len(a):
        maj = get_majority_element_help(a, left, right)

        if count_maj(a, left, right, maj) > len(a)//2:
            return 1
    return 0 


def get_majority_element_help(a, left, right):

    # base case is only one thing left
    if left == right:
        return a[left]

    # splitting criteria
    mid = left + (right - left) // 2

    # left side run
    left_side = get_majority_element_help(a, left, mid)

    right_side = get_majority_element_help(a, mid+1, right)

    # if left and right return the same
    if left_side == right_side:
        return left_side
    else:
        # count majority between secitons
        l_count = count_maj(a, left, mid, left_side)
        r_count = count_maj(a, mid + 1, right, right_side)  
        if l_count > r_count:
            return left_side
        elif l_count < r_count:
            return right_side
        else:
            return 0.5*(right_side + left_side)


def count_maj(a, left, right, key):
    # count variable
    count = 0
    
    idx = left
    
    # use while loop
    while idx <= right:
        if a[idx] == key:
            count += 1

        # increment idx
        idx += 1

    # return count
    return count 


    








if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n-1))

