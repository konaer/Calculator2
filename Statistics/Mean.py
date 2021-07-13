from Calculator.Addition import addition
from Calculator.Division import division

def mean(data):
    try:
        num_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)
        return division(total, num_values)

    except ZeroDivisionError:
        print("Error: Divide by 0 is not acceptable")
    except ValueError:
        print("Error: list cannot empty")