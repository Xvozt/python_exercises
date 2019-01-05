# -*- coding: utf-8 -*-
# Get arithmetic result of 2 
def arithmetic(first, second, operand):
    if str(operand) == '+':
        summary = first + second
        print(summary)
    elif str(operand) == '-':
        summary = first - second
        print(summary)
    elif str(operand) == ':':
        summary = first / second
        print(summary)
    elif str(operand) == '*':
        summary = first * second
        print(summary)
    else:
        print("Неизвестная операция")


arithmetic(5, 2, '=')
