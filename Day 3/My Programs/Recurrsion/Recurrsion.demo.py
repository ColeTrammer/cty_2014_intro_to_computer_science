"""
Day 8
Recursion demonstration
"""

"""
@param x An int. We want the sum from 1 to x
@return The sum from 1 to x

An iterative implentation of the sum from 1 to x
"""

def sum_iterative(x):
    sum = 0      # define an accumulator
    while x >= 0:# Iterate backwards from x to 0
        sum += x # Add x to sum
        x -= 1   # Subtract 1 from x
    return sum   # Return the final sum


"""
@ param x An int. We want the sum from 1 to x
@return   The sum of 1 to x

A recursive implementation of the sum from 1 to x
"""


def sum_recursion(x):

    if x == 0:      #BASE CASE
        return 0
    elif x > 0:     #RECURSIVE CASE
        return x + sum_recursion(x - 1)
    else:
        return 0
"""
@param n   is the number to run factorial on
@return    returns the factorial of n

iterative way to find n!
"""


def factorial_iterative(n):
    output = 1
    while n > 0:
        output *= n
        n -= 1
    return output


"""
@param n  is the number to find the factorial of
@return   returns n!

recursive method to find n!
"""


def factorial_recursive(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial_recursive(n - 1)
    else:
        return 0


"""
@ param n   the number to find the fibonacci term of
@ return    the n th term of the fibonacci sequence

iterative way to find the nth term of the fibonacci sequence
"""


def fib_iterative(n):
    x = 1
    y = 1
    while n > 2:
        z = y
        y += x
        x = z
        n -= 1
    return y

"""
@ param n   the number to find the fibonacci term of
@ return    the n th term of the fibonacci sequence

recursive way to find the nth term of the fibonacci sequence
"""


def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    else:
        return 0
"""

"""


def main():
    print "Welcome to recursion!"
    print sum_iterative(5)
    print sum_recursion(6)
    print factorial_iterative(5)
    print factorial_recursive(6)
    print fib_iterative(5)
    print fib_recursive(6)


if __name__ == "__main__":
    main()