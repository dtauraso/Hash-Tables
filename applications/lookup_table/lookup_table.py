import math
import random

caches = {  'power': {},
            'factorial': {}}

def power_has_input(x, y):
    global caches
    if x in caches['power']:
        if y in caches['power'][x]:
            return True
    return False

def factorial_has_input(x):
    global caches
    if x in caches['factorial']:
        return True
    return False

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    global caches
    v = 0
    if power_has_input(x, y):
        v = caches['power'][x][y]
    else:

        caches['power'][x] = {y: math.pow(x, y)}
        v = caches['power'][x][y]
    if factorial_has_input(v):
        v = caches['factorial'][v]
    else:
        # caches['factorial'][v]
        caches['factorial'][v] = math.factorial(v)
        v = caches['factorial'][v]
    v //= (x + y)
    v %= 982451653

    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
