# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_euclid(a, b):

    if a > 0 and b >0:
        # obtain div start
        top = max(a, b)
        bot = min(a, b)

        while bot > 0:
            bot_prev = bot
            div = top // bot

            bot = top - (bot*div)
            top = bot_prev

            
        return top

    return -1


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclid(a, b))
