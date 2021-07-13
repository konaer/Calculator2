from Calculator.Square import squaring
from Calculator.Division import division
from Statistics.PopulationMean import populationmean

def variance(num):
    try:
        num_values = len(num)
        pop_mean = populationmean(num)

        x = 0
        for i in num:
            x = x + squaring(i-pop_mean)
        return division(x, num_values)
    except ZeroDivisionError:
        print("Error: Divide by 0 is not acceptable")
    except ValueError:
        print("Error: list cannot empty")