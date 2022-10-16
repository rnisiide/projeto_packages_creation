# Submodulo de operacoes aritmeticas 

def sum(value1, value2):
    result = value1 + value2
    return f'The sum of {value1:.2f} and {value2:.2f} is {result:.2f}.\nIts mathematic expresion is: {value1} + {value2} = {result:.2f}'

def subtraction(value1, value2):
    result = value1 - value2
    return f'The subtraction of {value2:.2f} from {value1:.2f} is {result:.2f}.\nIts mathematic expression is: {value1} - {value2} = {result:.2f}'

def multiplication(value1, value2):
    result = value1 * value2
    return f'{value2:.2f} multiplied by {value1:.2f} is {result:.2f}\nIts mathematic expression is: {value1} * {value2} = {result:.2f}'

def division(value1, value2):    
    result = value1 / value2
    return f'{value2:.2f} divided by {value1:.2f} is {result:.2f}\nIts mathematic expression is: {value1} / {value2} = {result:.2f}'