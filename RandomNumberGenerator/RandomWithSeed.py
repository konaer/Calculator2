import random

def random_float_with_seed(a,b):
    random.seed(5)
    num = random.uniform(a,b)
    yield num

def random_int_with_seed(a,b):
    random.seed(5)
    num = random.randint(a, b)
    yield num