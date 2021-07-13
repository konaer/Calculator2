import random

def random_float_with_seed(a,b):
    random.seed(5)
    random_float_with_seed = random.uniform(a,b)
    return random_float_with_seed

def random_int_with_seed(a,b):
    random.seed(5)
    random_int_with_seed = random.randint(a, high=b)
    return random_int_with_seed