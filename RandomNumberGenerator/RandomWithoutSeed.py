import random

def random_float_without_seed(a,b):
    num = random.uniform(a,b)
    yield num

def random_int_without_seed(a,b):
    num = random.randint(a, high=b)
    yield num


