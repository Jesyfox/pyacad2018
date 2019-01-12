from threading import Thread


def counter(name, n):
    ''',jgfkjgfv,jyhvfl

    :param name: ngmhfcgmhg
    :param n: hvgjh,vf
    :return: kjf,jhvg,jhv
    '''
    for i in range(n):
        print(name, i)


# t1 = Thread(target=counter, args=('first', 1000000))
# t2 = Thread(target=counter, args=('second', 1000000))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()

counter('first', 1000000)
counter('second', 1000000)
