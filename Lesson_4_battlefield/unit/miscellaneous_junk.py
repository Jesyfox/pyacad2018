from time import time


def waiter(recharge):
    while True:
        timer = time()
        while True:
            # if you want some fast battle research
            # append some ZEROS to this num  \/
            if (time() - timer) < (recharge/1000):
                yield True
            else:
                yield False
                break


def geometric_average(arr: list):
    power = 1 / len(arr)
    res = 1
    for i in arr:
        res *= i
    return res**power
