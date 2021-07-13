import random

# Generate a list of N random numbers with a seed and between a range of numbers
def n_ramdom_int_number(n,lowRange,highRange):
    data=[]
    random.seed(5)
    for i in range(n):
        data.append(random.randint(lowRange,highRange))
    return data

def n_ramdom_float_number(n,lowRange,highRange):
    data=[]
    random.seed(5)
    for i in range(n):
        data.append(random.uniform(lowRange,highRange))
    return data