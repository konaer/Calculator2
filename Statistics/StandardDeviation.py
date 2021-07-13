from Calculator.SquareRoot import squarerooting
from Statistics.Variance import variance

def stddev(num):
    try:
        variance_float = variance(num)
        return round(squarerooting(variance_float), 5)
    except ZeroDivisionError:
        print("Error: Divide by 0 is not acceptable")
    except ValueError:
        print("Error: list cannot empty")