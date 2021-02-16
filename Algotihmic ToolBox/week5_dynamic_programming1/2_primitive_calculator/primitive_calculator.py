# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def opt_seq(n):
    div = [1, 1/2, 1/3]

    return mat_form(div, n)
    


def mat_form(div, n):    
    # reaorder divisor from small to max
    div_sort(div)

    # storage matrix
    array = [[x for x in range(n +1)] for y in range(len(div))]

    for i in range(1, len(div)):
        for j in range(1, n + 1):
            if div[i] == j:
                array[i][j] = 1

            elif div[i] > j:
                array[i][j] = array[i-1][j] 

            elif j % div[i] == 0:
                array[i][j] = 1 + array[i][int(j/div[i])]

            else:
                array[i][j] = min(array[i-1][j], 1 + array[i][j - 1])
        
    return unravel_path(array, n, div)
    
def unravel_path(array, n, div):
    # sequence list
    seq = []
    min_val = array[-1][-1]

    # init j
    i = len(div) - 1
    j = n

    while j >= 1:
        #print("i:{}".format(i))
        #print("j:{}".format(j))
        seq.append(j)

        while min_val == array[i-1][j] and i>=0:
            i = i - 1

        # compare minval subtracting 1
        min_val = array[i][j-1]
        nxt = j-1

        if j % div[i] == 0:
            if array[i][j//div[i]] <= array[i][j//div[i]]:
                min_val = array[i][j//div[i]]
                nxt = j //div[i]

        # compare min val
        j = nxt




        

    return sorted(seq)
    

def div_sort(div):
    # reorder the array
    for i in range(len(div)):
        div[i] = int(1/div[i])

    div = sorted(div)


input = sys.stdin.read()
n = int(input)
sequence = list(opt_seq(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
