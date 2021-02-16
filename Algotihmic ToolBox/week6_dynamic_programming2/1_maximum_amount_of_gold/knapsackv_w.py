# Uses python3
import sys

def optimal_weight(items, capacity):
	# initialize 2 d array
    knapsackVal = [[0 for x in range(capacity +1)] for y in range(len(items) + 1)]

    # double loop
    for i in range(1, len(items)+1):
    	# extract current weight and value
    	currWeight = items[i - 1][1]
    	currValue = items[i - 1][0]

    	# second loop 
    	for c in range(capacity+1):
    		# copy above
    		if currWeight > c:
    			knapsackVal[i][c] = knapsackVal[i-1][c]

    		else:
    			# compate
    			knapsackVal[i][c] = max(knapsackVal[i-1][c], currValue + knapsackVal[i-1][c - currWeight])

    return [knapsackVal[-1][-1], backTrack(knapsackVal, items)]

def backTrack(knapsackVal, items):
	seq = []

	# get current index
	i = len(knapsackVal) -1
	c = len(knapsackVal[0]) - 1

	while i > 0:
		if knapsackVal[i][c] == knapsackVal[i-1][c]:
			i -= 1

		else:
			# can append sequence or indicies seq.append(items[i-1])
			seq.append(i - 1)
			
			# update item column and sequence
			c -= items[i-1][1]
			i -= 1

		# ending statement
		if c == 0:
			break

	return list(reversed(seq))



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
