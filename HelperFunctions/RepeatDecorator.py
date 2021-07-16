def repeat(func):
    def wrapper_repeat():
        func()
        func()
    return wrapper_repeat()