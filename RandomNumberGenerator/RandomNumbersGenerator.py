from RandomNumberGenerator.RandomWithSeed import random_float_with_seed, random_int_with_seed


def n_ramdom_int_number(n,lowRange,highRange):
    for i in range(n):
        l = list(random_int_with_seed(lowRange,highRange))
    return l

def n_ramdom_float_number(n,lowRange,highRange):
    for i in range(n):
        l = list(random_float_with_seed(lowRange,highRange))
    return l