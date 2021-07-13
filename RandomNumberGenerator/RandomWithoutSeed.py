import random

def random_float_without_seed(a,b):
    random_float_without_seed = random.uniform(a,b)
    return random_float_without_seed

def random_int_without_seed(a,b):
    random_int_without_seed = random.randint(a, high=b)
    return random_int_without_seed


