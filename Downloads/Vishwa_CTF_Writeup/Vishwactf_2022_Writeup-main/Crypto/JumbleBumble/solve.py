
from math import exp, log

lines = []

with open("JumbleBumble.txt", "r") as f:
    lines = f.readlines()

# https://stackoverflow.com/a/356206
def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n <= x:
        high *= 2
    low = high/2
    while low < high:
        mid = int((low + high) // 2) + 1
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

while len(lines):
    if lines[-1] == '\n':
        lines.pop()
    c = int(lines.pop())
    e = int(lines.pop())
    n = int(lines.pop())

    m = int(find_invpow(c, 4))
    print(bytes.fromhex(hex(m)[2:]))
