from collections import Counter

def mode(num):
    try:
        num_values = len(num)
        count = Counter(num)
        get_mode = dict(count)
        mode = [k for k, v in get_mode.items() if v == max(list(count.values()))]
        get_mode = mode[0]
        return get_mode
    except ZeroDivisionError:
        print("Error: Divide by 0 is not acceptable")
    except ValueError:
        print("Error: list cannot empty")