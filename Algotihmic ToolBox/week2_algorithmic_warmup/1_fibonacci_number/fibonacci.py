# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())

def calc_fib2(n):
    if n-1 <= 1:
        return n-1

    # calculation is not equal    
    prev = 0
    curr = 1

    for i in range(n- 2):
        prev, curr = curr, prev + curr

    return curr

print(calc_fib2(n))
