import RandomNumberGenerator.NRandomNumbers
import RandomNumberGenerator.RandomWithSeed
import RandomNumberGenerator.RandomWithoutSeed

class RandomNumberGenerator:
    result = 0
    data = []

    def __init__(self):
        pass

    def randomNumberWithSeed(self, a, b):
        self.result = RandomNumberGenerator.random_float_with_seed(a, b)
        return self.result

    def randomNumberWithoutSeed(self, a, b):
        self.result = RandomNumberGenerator.random_float_without_seed(a,b)
        return self.result

    def nRandomNumberWithSeed(self, n, lowRange,highRange):
        self.result = RandomNumberGenerator.n_ramdom_float_number(n,lowRange,highRange)
        return self.result