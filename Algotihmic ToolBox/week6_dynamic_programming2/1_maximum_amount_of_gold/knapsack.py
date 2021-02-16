# Uses python3
import sys

def optimal_weight(capacity, items):
    # w* s weights array and W is the total capacity
    # initialize 2 d array
    knapsackVal = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]

    # double loop
    for i in range(1, len(items)+1):
        # extract current weight and value
        currWeight = items[i - 1]
        currValue = items[i - 1]

        # second loop 
        for c in range(capacity+1):
            # copy above
            if currWeight > c:
                knapsackVal[i][c] = knapsackVal[i-1][c]

            else:
                # compate
                knapsackVal[i][c] = max(knapsackVal[i-1][c], currValue + knapsackVal[i-1][c - currWeight])

    return knapsackVal[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
