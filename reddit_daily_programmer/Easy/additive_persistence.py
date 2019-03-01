"""Challenge is to calculate the additive persistence of a number,
defined as how many loops you have to do summing its digits
until you get a single digit number.
Take an integer N:
Add its digits
Repeat until the result has 1 digit
The total number of iterations is the additive persistence of N.
Your challenge today is to implement a function
that calculates the additive persistence of a number.

Bonus:
The really easy solution manipulates the input to convert the number
to a string and iterate over it.
Try it without making the number a string, decomposing it into digits
while keeping it a number.
On some platforms and languages,
if you try and find ever larger persistence values you'll quickly learn about
your platform's
big integer interfaces (e.g. 64 bit numbers).
"""


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def persistance(n):
    add_persistance = 0
    while n > 9:
        n = sum_digits(n)
        add_persistance += 1
    return add_persistance


def main():
    for example in (13, 1234, 9876, 199, 25252, 3323, 1241252521):
        print(example, persistance(example))


main()
