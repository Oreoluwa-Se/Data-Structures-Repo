#Uses python3

import sys

def lcs2(a, b):
    
    # generate 2 x 2 array
    lcs = [[[None, 0, None, None] for x in range(len(a) + 1)] for y in range(len(b) + 1)]
    
    # loop through array
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if b[i - 1] == a[j - 1]:
                lcs[i][j] = [b[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]

            else:
                if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]

                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]

    # return the build sequence
    return seqBuild(lcs)

def seqBuild(lcs):
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1

    # backpropagate through array
    while i != 0 and j != 0:
        currEntry = lcs[i][j]

        if currEntry[0] is not None:
            sequence.append(currEntry[0])

        i = currEntry[2]
        j = currEntry[3]

    #print(list(reversed(sequence)))
    return len(sequence)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
