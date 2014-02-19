from functools import reduce
from random import randint


def solver(*args):
    return max(args) - min(args)


tests = []

for _ in range(20):
    t = [randint(-100, 0) / (10 ** randint(0, 3)) for _ in range(randint(1, 20))]
    ans = round(solver(*t), 4)
    print('{{"input": {0},\n"answer": {1},\n"explanation": "{2}-{3}"}},\n'.format(
        t, ans, max(t), min(t) if min(t) >= 0 else "({0})".format(min(t))))



