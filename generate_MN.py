from functools import reduce
from random import randint


def solver(*args):
    return max(args) - min(args)


tests = []

for _ in range(20):
    t = [randint(-100, 100) / (10 ** randint(0, 3)) for _ in range(randint(1, 20))]
    ans = round(solver(*t), 4)
    print('{{"input": {0},\n"answer": {1}\n}},\n'.format(t, ans))



