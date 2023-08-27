def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        
        return "Error!"