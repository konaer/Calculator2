from Calculator.Division import division

def populationmean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return division(total, num_values)
    except ZeroDivisionError:
        print("Error: Divide by 0 is not acceptable")
    except ValueError:
        print("Error: list cannot empty")