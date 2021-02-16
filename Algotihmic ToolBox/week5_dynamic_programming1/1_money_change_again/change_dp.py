# Uses python3
import sys
import numpy as np


def get_change(m):
    #write your code here
    coin_set = [1, 10, 5]

    return min_finder(matrix_create, coin_set, m, "val")

def matrix_create(coin_set, number):
    # create matrix
    calc_mat =  np.ones((len(coin_set), (number+1)))*np.inf

    for i in range(len(coin_set)):
        
        # start from j = 1.. left most is zero
        for j in range(number+1):

            # at the begining
            if i == 0:
                if j % coin_set[i] == 0:
                    calc_mat[i, j] = j // coin_set[i]
    
            # scenario where the coin is bigger than current money branch
            elif coin_set[i] > j:
                calc_mat[i, j] = calc_mat[i-1, j]

            # for all other cases
            else:
                calc_mat[i, j] = min(calc_mat[i-1, j], 1 + calc_mat[i ,j-coin_set[i]])


    return calc_mat

# takes the function call for creating the matrix 
def min_finder(matrix_create, coin_set, number, check="num"):
    # sort the coin set
    coin_set = sorted(coin_set)

    # calculates the minimum from each coin
    calc_mat = matrix_create(coin_set, number)
    print(calc_mat)
    if check.lower() == "num":
        if calc_mat[-1, -1] == np.inf:
            return -1
        else: 
            return calc_mat[-1, -1]

    
    # storage for coin list   
    list_coins = []
    
    i = len(coin_set) - 1
    j = number

    # loop in reverse
    while j > 0:
        min_coint = calc_mat[i, j]

        # check till we find 
        while calc_mat[i, j] == min_coint and i >= 0:
            i -= 1

        # reset i and append to list
        i = i + 1
        list_coins.append(coin_set[i])

        # calulate new j location
        j = j - coin_set[i]


    return list_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
