def typeChecker(func):
    def wrapper_typeCheck():
        print(type(func()))
        return func()
    return wrapper_typeCheck()