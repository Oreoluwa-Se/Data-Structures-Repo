# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
    
def lcm_eff(a,b):
    if a > 0 and b >0:
        div = gcd_euclid(a,b)

        return int((a*b)/div)

    return -1


def gcd_euclid(a, b):
    # obtain div start
    top = max(a, b)
    bot = min(a, b)

    while bot > 0:
        bot_prev = bot
        div = top // bot

        bot = top - (bot*div)
        top = bot_prev

            
    return top

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_eff(a, b))

