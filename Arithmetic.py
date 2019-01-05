# -*- coding: utf-8 -*-
# Get arithmetic result of 2
import unittest


def arithmetic(first, second, operand):
    if str(operand) == '+':
        summary = first + second
    elif str(operand) == '-':
        summary = first - second
    elif str(operand) == '/':
        summary = first / second
    elif str(operand) == '*':
        summary = first * second
    else:
        summary = "Неизвестная операция"
    return summary


print(arithmetic(3, 4, '*'))


class ArithmeticTestCase(unittest.TestCase):

    def test_plus(self):

        self.assertEqual(arithmetic(3, 4, '+'), 7)

    def test_minus(self):

        self.assertEqual(arithmetic(3, 4, '-'), -1)

    def test_multiply(self):

        self.assertEqual(arithmetic(3, 4, '*'), 12)

    def test_divide(self):

        self.assertEqual(arithmetic(3, 4, '/'), 3 / 4)

    def test_unknown(self):

        self.assertEqual(arithmetic(3, 4, '.'), "Неизвестная операция")


if __name__ == "__main__":
    unittest.main()
