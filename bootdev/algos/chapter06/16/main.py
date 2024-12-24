import math


def prime_factors(n):
    pfs = []
    while n % 2 == 0:
        pfs.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pfs.append(i)
            n = n / i

    if n > 2:
        pfs.append(int(n))

    return pfs
