from time import time


def waiter(recharge):
    while True:
        timer = time()
        while True:
            time_passed = (time() - timer)
            need_to_be_passed = (recharge/1000)
            if time_passed >= need_to_be_passed:
                yield True
                break
            else:
                yield False


def geometric_average(arr: list):
    power = 1 / len(arr)
    res = 1
    for i in arr:
        res *= i
    return res**power
