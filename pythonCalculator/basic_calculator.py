def add(x, y):
    return float(x) + (float(y))

def subtract(x, y):
    return float(x) - (float(y))

def multiply(x, y):
    return round(float(x) * (float(y)), 10)

def divide(x, y):
    return round(float(x) / (float(y)), 10)

def pos_neg(x):
    return float(x) * -1
      
def clearThis():
    return str()
    
def clearAll():
    return str(), str()
    
def operation(operator, x, y):
    if operator == '+':
        return add(x, y)
    elif operator == '-':
        return subtract(x, y)
    elif operator == '*':
        return multiply(x, y)
    elif operator == '/':
        return divide(x, y)
        